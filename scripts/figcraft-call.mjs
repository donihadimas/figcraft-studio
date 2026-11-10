#!/usr/bin/env node
/**
 * Direct FigCraft MCP Tool Caller (Fallback & CLI Bridge)
 * Usage:
 *   node figcraft-call.mjs <tool_name> '<json_args>'
 *   node figcraft-call.mjs --file <tool_name> <path_to_json_args>
 */

import net from "node:net";
import fs from "node:fs";
import { spawn } from "node:child_process";

const PORT = Number(process.env.FIGCRAFT_PORT || 7979);
const HOST = "127.0.0.1";

function findBinary(candidates) {
  for (const p of candidates) {
    if (p && fs.existsSync(p)) return p;
  }
  return candidates[0];
}

const isWin = process.platform === "win32";
const figcraftGui = findBinary(
  isWin
    ? [
        process.env.FIGCRAFT_PATH,
        "C:\\Program Files\\FigCraft\\figcraft.exe",
        `${process.env.LOCALAPPDATA || ""}\\Programs\\FigCraft\\figcraft.exe`,
      ]
    : [
        process.env.FIGCRAFT_PATH,
        "/usr/bin/figcraft",
        "/usr/local/bin/figcraft",
        "/Applications/FigCraft.app/Contents/MacOS/figcraft",
      ]
);
const figcraftCli = findBinary(
  isWin
    ? [
        process.env.FIGCRAFT_CLI_PATH,
        "C:\\Program Files\\FigCraft\\figcraft-cli.exe",
        `${process.env.LOCALAPPDATA || ""}\\Programs\\FigCraft\\figcraft-cli.exe`,
      ]
    : [
        process.env.FIGCRAFT_CLI_PATH,
        "/usr/bin/figcraft-cli",
        "/usr/local/bin/figcraft-cli",
        "/Applications/FigCraft.app/Contents/MacOS/figcraft-cli",
      ]
);

function checkPort(port, host = HOST, timeout = 400) {
  return new Promise((resolve) => {
    const s = new net.Socket();
    let done = false;
    const finish = (ok) => {
      if (!done) {
        done = true;
        s.destroy();
        resolve(ok);
      }
    };
    s.setTimeout(timeout);
    s.once("connect", () => finish(true));
    s.once("timeout", () => finish(false));
    s.once("error", () => finish(false));
    s.connect(port, host);
  });
}

async function ensureGui() {
  if (await checkPort(PORT)) return;
  const g = spawn(figcraftGui, ["--control", String(PORT)], {
    detached: true,
    stdio: "ignore",
  });
  g.unref();
  for (let i = 0; i < 50; i++) {
    await new Promise((r) => setTimeout(r, 200));
    if (await checkPort(PORT)) return;
  }
}

const argv = process.argv.slice(2);
let toolName = argv[0];
let toolArgs = {};

if (argv[0] === "--file") {
  toolName = argv[1];
  toolArgs = JSON.parse(fs.readFileSync(argv[2], "utf8"));
} else {
  toolName = argv[0] || "inspect_document";
  toolArgs = argv[1] ? JSON.parse(argv[1]) : {};
}

await ensureGui();

const proc = spawn(figcraftCli, ["mcp", "--attach", String(PORT)], {
  stdio: ["pipe", "pipe", "inherit"],
});

proc.stdin.write(
  JSON.stringify({
    jsonrpc: "2.0",
    id: 1,
    method: "initialize",
    params: {
      protocolVersion: "2024-11-05",
      capabilities: {},
      clientInfo: { name: "figcraft-caller", version: "1.0" },
    },
  }) + "\n"
);

let buffer = "";
proc.stdout.on("data", (chunk) => {
  buffer += chunk.toString("utf8");
  const lines = buffer.split("\n");
  buffer = lines.pop() || "";
  for (const line of lines) {
    if (!line.trim()) continue;
    let msg;
    try {
      msg = JSON.parse(line);
    } catch {
      continue;
    }
    if (msg.id === 1) {
      proc.stdin.write(
        JSON.stringify({
          jsonrpc: "2.0",
          method: "notifications/initialized",
        }) + "\n"
      );
      proc.stdin.write(
        JSON.stringify({
          jsonrpc: "2.0",
          id: 2,
          method: "tools/call",
          params: {
            name: toolName,
            arguments: toolArgs,
          },
        }) + "\n"
      );
    } else if (msg.id === 2) {
      if (msg.error) {
        console.error(JSON.stringify(msg.error, null, 2));
        proc.kill();
        process.exit(1);
      }
      const content = msg.result?.content || [];
      for (const item of content) {
        if (item.type === "text") {
          console.log(item.text);
        } else if (item.type === "image") {
          const outPath = toolArgs._saveScreenshot || "figcraft-screenshot.png";
          fs.writeFileSync(outPath, Buffer.from(item.data, "base64"));
          console.log(`SCREENSHOT_SAVED=${outPath}`);
        }
      }
      proc.kill();
      process.exit(0);
    }
  }
});

