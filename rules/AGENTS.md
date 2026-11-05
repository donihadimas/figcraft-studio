# Always-On Rules: `figcraft-studio` (Industrial UI/UX & FigCraft Pipeline)

These rules apply whenever designing interfaces in **FigCraft** or building/polishing **Web & Mobile UI** in code.

---

## 1. Mandatory FigCraft Execution Pipeline

Whenever a task involves FigCraft (`figcraft` MCP server):

1. **Auto-Launch Attach Mode First**: Never ask the user to open FigCraft manually. Run:
   - **Windows (PowerShell)**:
     ```powershell
     powershell -NoProfile -ExecutionPolicy Bypass -File "$HOME/.gemini/config/plugins/figcraft-studio/scripts/ensure-figcraft.ps1"
     ```
   - **macOS / Linux (Bash)**:
     ```bash
     bash "$HOME/.gemini/config/plugins/figcraft-studio/scripts/ensure-figcraft.sh"
     ```
   - **MCP Hot-Bridge Fallback**: If the IDE started before FigCraft was open and native `call_mcp_tool` cached a startup connection error, invoke FigCraft MCP tools directly via `node "$HOME/.gemini/config/plugins/figcraft-studio/scripts/figcraft-call.mjs" --file <tool_name> <args.json>`.
2. **Inspect Before Mutating**: Call `figcraft/inspect_document` (`{"depth": 3}`) to check existing frames/pages and avoid overlapping coordinates at `(0, 0)`. Place new top-level frames with a `80–100px` horizontal gap to the right of existing frames.
3. **Atomic `batch` Construction**: Group related node creations into a single `figcraft/batch` call using `{"$step": n}` parent references.
4. **Vector Icons Only (Zero Emoji Rule)**: Never use emojis (`🏠`, `⚙️`, `🔔`) as UI icons. Read `$HOME/.gemini/config/plugins/figcraft-studio/references/vector-icons-24px.md` and use exact `24×24` SVG path strings with `type: "vector"` and `"fills": []` inside `props` for outline icons.
5. **Mandatory Visual Self-Critique (`screenshot`)**: Every FigCraft build MUST end with `view.zoomFit` + `figcraft/screenshot`. Inspect the rendered PNG against the **100-Point UI Critic Rubric** (`ui-critic-audit`) and fix any text clipping, collision, or contrast defect before finishing.

---

## 2. Industrial UI/UX Craft Invariants (Canvas & Code)

1. **Design Intelligence First**: For any new product, screen, or landing page, query `ui-ux-pro-max` first:
   ```powershell
   python "$HOME/.gemini/config/plugins/figcraft-studio/skills/ui-ux-pro-max/scripts/search.py" "<product> <industry> <vibe>" --design-system -p "<Project>"
   ```
2. **Concentric Border-Radius Math (`ui-optical-polish`)**:
   Nested rounded containers must obey:
   $$R_{\text{outer}} = R_{\text{inner}} + \text{Padding}$$
   *(e.g., Card `cornerRadius: 16` + `padding: 8` $\rightarrow$ Inner item `cornerRadius: 8`).*
3. **Surface Elevation & Hairlines (`ui-optical-polish`)**:
   - **Dark Mode**: Communicate elevation via surface luminance stepping (`#09090B` canvas $\rightarrow$ `#121215` card $\rightarrow$ `#18181B` elevated popover) + `1px` subtle border (`#27272A` / `white/10`), never heavy black drop shadows.
   - **Light Mode**: Use `1px` low-opacity border (`#09090B0F`) + 2-layer ambient/key drop shadow.
   - **Tabular Numerals**: All prices, metrics, percentages, timers, and table numbers must use `tabular-nums` (`tnum`).
4. **Zero Placeholder & Action-First Microcopy (`ux-writing-microcopy`)**:
   - Strictly ban `Lorem ipsum`, `John Doe`, `Item 1 / Item 2`, `"Supercharge Your Workflow"`, and generic `"Submit"` / `"Click Here"` buttons.
   - Seed realistic domain data (authentic Indonesian/Global names, realistic `Rp` / `USD` figures with thousand separators, real payment/bank/tech labels) and verb+object CTA labels (*"Transfer Rp 1.250.000"*, *"Buat Proyek"*).
5. **5-State Completeness (`ux-flows-and-states`)**:
   - Account for *Ideal*, *Empty (Zero-Data with CTA)*, *Skeleton Loading (geometry-matched)*, *Inline/Banner Error*, and *Stress/Overflow* states.
6. **Motion Physics (`ui-motion-choreography`)**:
   - High-frequency micro-interactions (`100–150ms`), spatial overlays (`160–200ms`), and **Exit Faster Than Enter** (`-25%` duration on close).

---

## 3. On-Demand Skill Routing

Load the specific skill when deep domain rules are needed:
- **Mobile App (iOS/Android)**: `figcraft-mobile-ui` (Safe areas `59px`/`34px`, `44pt`/`48dp` touch targets, `4/8dp` grid)
- **Web / Landing / SaaS Dashboard**: `figcraft-web-ui` + `design-taste-frontend` (Design Read, 3 Dials, Bento rules)
- **Design Tokens & Components**: `figcraft-design-system` (Variables Light/Dark, Styles, Variants)
- **FigCraft $\rightarrow$ Code Handoff**: `figcraft-to-code` (`inspect.code` + `variable.list` + `screenshot`)
- **Visual QA & Redesign Critique**: `ui-critic-audit` (100-Point Rubric)
