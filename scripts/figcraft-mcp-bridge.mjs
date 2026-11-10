#!/usr/bin/env node
/**
 * FigCraft Auto-Attach MCP Bridge
 * Automatically launches `figcraft --control 7979` if port 7979 is not listening,
 * waits until ready, and then bridges stdio to `figcraft-cli mcp --attach 7979`.
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
    const socket = new net.Socket();
    let settled = false;
    const done = (ok) => {
      if (!settled) {
        settled = true;
        socket.destroy();
        resolve(ok);
      }
    };
    socket.setTimeout(timeout);
    socket.once("connect", () => done(true));
    socket.once("timeout", () => done(false));
    socket.once("error", () => done(false));
    socket.connect(port, host);
  });
}

async function ensureGuiRunning() {
  if (await checkPort(PORT)) return;

  if (isWin) {
    // Use Start-Process -WindowStyle Normal so FigCraft does not inherit SW_HIDE from the IDE language server
    const ps = spawn(
      "powershell.exe",
      [
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-Command",
        `Start-Process -FilePath '${figcraftGui}' -ArgumentList '--control','${PORT}' -WindowStyle Normal`,
      ],
      { stdio: "ignore", windowsHide: true }
    );
    ps.unref();
  } else {
    const gui = spawn(figcraftGui, ["--control", String(PORT)], {
      detached: true,
      stdio: "ignore",
      windowsHide: false,
    });
    gui.unref();
  }

  const maxAttempts = 50; // 50 * 200ms = 10s
  for (let i = 0; i < maxAttempts; i++) {
    await new Promise((r) => setTimeout(r, 200));
    if (await checkPort(PORT)) return;
  }
}

await ensureGuiRunning();

const child = spawn(figcraftCli, ["mcp", "--attach", String(PORT)], {
  stdio: "inherit",
});

child.on("exit", (code) => {
  process.exit(code ?? 0);
});
