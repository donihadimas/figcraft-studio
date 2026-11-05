---
name: figcraft-automator
description: "Auto-launch FigCraft GUI in attach mode (--control 7979) and execute atomic canvas operations via FigCraft MCP. Use whenever a user asks to open FigCraft, check FigCraft connection, create or modify frames/layers/shapes/text in FigCraft, run batch commands, manage pages/files, or verify canvas designs via screenshot."
---

# FigCraft Automator & Core Engine

Ensures the FigCraft desktop GUI is running with its control server active on port `7979` before executing any `figcraft` MCP tool calls, and enforces atomic `batch` construction + visual screenshot verification.

## Step 1: Auto-Launch & Verify Attach Mode (Mandatory First Step)

Before calling any `figcraft` MCP tool in a session, verify or launch FigCraft automatically without asking the user to open it manually:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "$HOME/.gemini/config/plugins/figcraft-studio/scripts/ensure-figcraft.ps1"
```

**Completion criterion:** Output contains `STATUS=READY` or `STATUS=STARTED` on `PORT=7979`, and calling `figcraft/inspect_document` returns the active document JSON.

## Step 2: Inspect Document State Before Mutating

Call `figcraft/inspect_document` (`{"depth": 3}`) to read:
- Existing pages (`pages`) and `currentPage`
- Existing top-level frames and their `absoluteBounds` (so new frames are placed with a `100px` horizontal gap to the right of existing frames instead of overlapping at `x: 0, y: 0`)
- Registered `styles` and `variables` count

## Step 3: Build Layouts Atomically via `batch`

Use `figcraft/batch` to group related layer creations and property updates into **one undo step**.
- Reference earlier steps within the same batch using `{"$step": n}` (zero-based index of the command in `commands`).
- If any command in a `batch` fails, the entire batch rolls back cleanly.

### Coordinate & Auto-Layout Rules
1. **Page Coordinates**: `1 unit = 1 px` at 100% zoom; `x` increases right, `y` increases **down**.
2. **Relative Positioning**: `x` and `y` in `create_node` / `set_properties` are **relative to the parent frame** (groups do not count as coordinate origins).
3. **Auto-Layout Frames**: Children inside an auto-layout frame (`layout: "horizontal" | "vertical" | "grid"`) ignore manual `x`/`y`. Control layout via:
   - Container props: `layout` (`"horizontal"` | `"vertical"` | `"grid"`), `gap` (number), `padding` (`number` or `[top, right, bottom, left]`), `mainAlign` (`"min"` | `"center"` | `"max"` | `"spaceBetween"`), `crossAlign` (`"min"` | `"center"` | `"max"`), `wrap` (`boolean`).
   - Child sizing props: `sizingH` (`"fixed"` | `"hug"` | `"fill"`), `sizingV` (`"fixed"` | `"hug"` | `"fill"`).
4. **Colors**: Always `#RRGGBB` or `#RRGGBBAA` (or gradient objects `{"type": "linearGradient", "stops": ["#hex1", "#hex2"]}`).
5. **Text Wrapping**: A text node hugs its content on a single line unless `width` is explicitly set or `sizingH: "fill"` is applied inside an auto-layout parent.

### Canonical `batch` Skeleton
```json
{
  "label": "Create Card Component",
  "commands": [
    {
      "command": "node.create",
      "params": {
        "type": "frame",
        "name": "Feature Card",
        "x": 100,
        "y": 100,
        "width": 360,
        "height": 220,
        "props": {
          "layout": "vertical",
          "padding": [24, 24, 24, 24],
          "gap": 12,
          "fill": "#18181B",
          "cornerRadius": 16,
          "stroke": "#27272A",
          "strokeWeight": 1,
          "sizingV": "hug"
        }
      }
    },
    {
      "command": "node.create",
      "params": {
        "type": "text",
        "name": "Card Title",
        "parent": { "$step": 0 },
        "text": "Instant Settlement",
        "props": {
          "fontFamily": "Inter",
          "fontStyle": "SemiBold",
          "fontSize": 20,
          "fill": "#FAFAFA",
          "sizingH": "fill"
        }
      }
    },
    {
      "command": "node.create",
      "params": {
        "type": "text",
        "name": "Card Body",
        "parent": { "$step": 0 },
        "text": "Reconcile cross-border transfers in under 400ms with zero intermediary fees.",
        "props": {
          "fontFamily": "Inter",
          "fontStyle": "Regular",
          "fontSize": 14,
          "lineHeight": 21,
          "fill": "#A1A1AA",
          "sizingH": "fill"
        }
      }
    }
  ]
}
```

## Step 4: Visual Verification Loop (Mandatory Before Completion)

Every visual change MUST be verified before reporting completion:
1. Call `figcraft/run_command` with `{"command": "view.zoomFit"}` so the user's FigCraft viewport frames the work.
2. Call `figcraft/screenshot` (passing `ids: [<rootFrameId>]` or omitting `ids` for the whole page).
3. Inspect the returned PNG for:
   - Text clipping, overflow, or unintended line wraps
   - Colliding elements or missing `sizingH: "fill"` / `sizingV: "hug"`
   - Low contrast between text and surface fills
4. Fix any visual defects with `set_properties` or `batch` and re-screenshot until clean.

## Key Engine Commands Reference

| Category | Command ID | Parameters |
| :--- | :--- | :--- |
| **Frame Presets** | `frame.create` | `{"preset": "iPhone 16" \| "Android Compact" \| "Desktop" \| "Slide 16:9", "name": "...", "x": 0, "y": 0}` |
| **Starter Templates** | `file.newFromTemplate` | `{"id": "mobile-app" \| "landing-page" \| "dashboard" \| "design-system" \| "wireframe-kit" \| "slides" \| "icon-set"}` |
| **Pages** | `page.add`, `page.select`, `page.rename`, `page.setBackground` | `{"name": "..."}` / `{"id": 1}` / `{"color": "#09090B"}` |
| **Viewport** | `view.zoomFit`, `view.zoomSelection`, `window.focus` | `{}` |
| **File I/O** | `open_file`, `save_file`, `export` | `path`, `format` (`png`\|`svg`\|`pdf`\|`webp`\|`fig`), `scale` |
