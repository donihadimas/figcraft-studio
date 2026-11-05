---
name: figcraft-to-code
description: "Convert FigCraft frames, components, and design tokens into production code (React, Next.js, Tailwind CSS, shadcn/ui, Flutter, React Native, SwiftUI, Jetpack Compose). Uses inspect_document, inspect.code, variable exports, and visual screenshot comparison. Use when turning a FigCraft design into code or syncing tokens to a repository."
---

# FigCraft-to-Code Handoff Pipeline

Translates designs from an active FigCraft canvas (or `.figcraft` file) into clean, responsive, token-compliant application code.

## Step 1: Connect & Inspect the Target Design in FigCraft

1. Ensure FigCraft is running in attach mode (`ensure-figcraft.ps1`).
2. Call `figcraft/inspect_document` (`{"depth": 6, "allPages": false}`) or `figcraft/get_node` on the selected/target frame IDs.
3. Capture a reference image of the target frame(s) using `figcraft/screenshot` (`{"ids": [<frameId>]}`) so you have both the **exact JSON layer tree** and the **visual truth**.

## Step 2: Extract Code & Design Tokens from FigCraft Engine

Run FigCraft's built-in Dev Mode inspection commands via `figcraft/run_command`:
- **Layer Code & Specs**: `{"command": "inspect.code", "params": {"id": <nodeId>}}` and `{"command": "inspect.properties", "params": {"id": <nodeId>}}`
- **Variables / Tokens**: `{"command": "variable.list"}` and `{"command": "style.list"}`
- **Export Vector/Image Assets**: Use `figcraft/export` (`{"ids": [<iconOrImageNodeId>], "format": "svg" | "png" | "webp", "path": "<project-assets-dir>/<name>.svg"}`) to extract icons and illustrations directly into the project's asset directory.

## Step 3: Map FigCraft Auto-Layout & Tokens to Target Stack

Query `ui-ux-pro-max` for stack-specific implementation rules if needed (`python "$HOME/.gemini/config/plugins/figcraft-studio/skills/ui-ux-pro-max/scripts/search.py" "<pattern>" --stack <stack>`), and map properties systematically:

| FigCraft Property | Web (Tailwind v4 / React) | Mobile (Flutter / React Native / Compose) |
| :--- | :--- | :--- |
| `layout: "horizontal"` | `flex flex-row` | `Row` / `flexDirection: 'row'` |
| `layout: "vertical"` | `flex flex-col` | `Column` / `flexDirection: 'column'` |
| `layout: "grid"` | `grid grid-cols-N` | `GridView` / `LazyVerticalGrid` |
| `gap: 16` | `gap-4` | `SizedBox(height/width: 16)` / `gap: 16` |
| `padding: [24, 32, 24, 32]` | `py-6 px-8` | `EdgeInsets.symmetric(vertical: 24, horizontal: 32)` |
| `sizingH: "fill"` | `w-full flex-1` | `Expanded` / `Modifier.fillMaxWidth()` |
| `sizingV: "hug"` | `h-auto` | `MainAxisSize.min` / `wrapContentHeight()` |
| Bound Variable `brand/primary` | `bg-primary text-primary-foreground` | Theme semantic color token |

## Step 4: Verify Code Against FigCraft Screenshot

1. Never hardcode raw hex values in components when the project uses CSS variables or theme tokens—sync FigCraft variables to `globals.css` / `tokens.json` / theme files first.
2. Replace fixed desktop pixel widths from FigCraft (`width: 1440`) with responsive containers (`max-w-7xl mx-auto px-4 sm:px-6 lg:px-8` and `min-h-[100dvh]`).
3. Ensure interactive states (`hover`, `focus-visible`, `active`, `disabled`) and accessibility attributes (`aria-label`, semantic tags) are implemented even if only the default state was drawn on the canvas.
