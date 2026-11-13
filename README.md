# 🎨 FigCraft Design Studio (`figcraft-studio`)

**Industrial-Grade UI/UX Design Engineering & FigCraft MCP Automation Suite for Google Antigravity, Claude Code, Cursor, and AI Coding Agents.**

`figcraft-studio` turns your AI coding agent into a Principal UI/UX Designer & Design Engineer. It automatically launches the **FigCraft Desktop App** in live attach mode (`--control 7979`), queries a local BM25 design intelligence database (**192 product color palettes, 79 UI styles, 74 font pairings, 119 UX guidelines, 22 tech stacks**), enforces studio-grade optical geometry, and self-audits every canvas via screenshot against a **100-Point Design Critique Rubric**.

---

## ⚡ Quick Install

### 1. Google Antigravity (One-Line Installer)

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/donihadimas/figcraft-studio/main/install.ps1 | iex
```

**macOS / Linux / Git Bash:**
```bash
curl -fsSL https://raw.githubusercontent.com/donihadimas/figcraft-studio/main/install.sh | bash
```

---

### 2. Claude Code Marketplace (`/plugin`)

Run directly inside **Claude Code**:
```bash
# 1. Add the marketplace repository
/plugin marketplace add donihadimas/figcraft-studio

# 2. Install the plugin
/plugin install figcraft-studio@figcraft-studio
```

Or via terminal CLI:
```bash
claude plugin marketplace add donihadimas/figcraft-studio
claude plugin install figcraft-studio@figcraft-studio
```

---

### 3. Universal Agent Skills CLI (`skills.sh` — Cursor, Windsurf, Claude, Antigravity, Copilot)

Install all 13 skills or pick specific skills with `npx skills`:
```bash
# Install all skills in figcraft-studio
npx skills add donihadimas/figcraft-studio

# Or install specific skills only
npx skills add donihadimas/figcraft-studio --skill ui-optical-polish --skill ux-flows-and-states
```

---

## 🧩 14 Bundled Skills (100% Self-Contained)

| Skill | Layer | Description |
| :--- | :--- | :--- |
| **`figcraft-automator`** | Engine & Attach | Auto-launches `figcraft --control 7979`, checks TCP port `7979`, and executes atomic `batch` operations + `screenshot` verification loops. |
| **`figcraft-design-system`** | Tokens & Kits | Builds 3-layer Design Tokens (`Primitive -> Semantic -> Component`), Light/Dark Variable Collections, Typography/Paint Styles, and Master Components + Variants. |
| **`figcraft-icon-craft`** | App Icons & Logos | Master rules, mathematical keylines (Android Adaptive Safe Area $\varnothing 626$px, iOS Squircle), optical balance, 2-layer decoupled export, and Python asset slicing. |
| **`figcraft-mobile-ui`** | Mobile (iOS/Android) | Designs iOS (`393×852`) and Android (`412×917`) screens with Safe Area clearance, 44pt/48dp touch targets, 4/8dp spacing rhythm, and crisp vector icons. |
| **`figcraft-web-ui`** | Web, Landing & SaaS | Designs Desktop Web (`1440px`), Landing Pages, Portfolios, and SaaS Dashboards with Mandatory Design Read, 3 Dials (`Variance`, `Motion`, `Density`), and Bento Grids. |
| **`figcraft-to-code`** | Dev Handoff | Converts FigCraft frames, variables, and vector assets (`inspect.code` + `inspect_document` + `screenshot`) into production React, Next.js, Tailwind, Flutter, or Compose code. |
| **`ui-ux-pro-max`** | Design Intelligence | Local Python BM25 search engine (`scripts/search.py`) with 79 UI styles, 192 product palettes, 74 font pairings, 119 UX rules, 25 chart types, and 22 stacks. |
| **`design-taste-frontend`** | Anti-Slop Web | Hard layout discipline, 3 Design Dials, serif/palette cliché bans, hero constraints, and GSAP/Motion skeletons. |
| **`frontend-design`** | Studio Direction | Two-pass studio planning (token system + wireframe -> anti-cliché review -> build -> visual critique). |
| **`ui-optical-polish`** | Surface & Geometry | Concentric border-radius formula ($R_{\text{outer}} = R_{\text{inner}} + P$), dark-mode surface luminance stepping, 1px specular hairlines, multi-layer shadows, and `tabular-nums`. |
| **`ux-flows-and-states`** | Product Completeness | Enforces the 5-State UI Matrix (*Ideal, Empty/Zero-Data, Geometry-Matched Skeleton Loading, Inline/Banner Error, Stress/Overflow*) + 5 interactive control states. |
| **`ux-writing-microcopy`** | Copy & Realism | Eliminates AI clichés (`"Supercharge"`, `"Submit"`, `"Lorem ipsum"`, `"John Doe"`) and seeds domain-realistic Indonesian/Global names, IDR/USD figures, and verb-first CTAs. |
| **`ui-motion-choreography`** | Interaction Physics | Frequency-Speed Law (`100–150ms` micro-interactions), Exit-Faster-Than-Enter (`-25%` close duration), origin-aware popover scaling, and `prefers-reduced-motion` parity. |
| **`ui-critic-audit`** | Visual QA | 100-Point Industrial Design Rubric across Hierarchy, Auto-Layout Geometry, Optical Contrast, Anti-Slop Authenticity, and Copy Realism with automatic corrective passes. |

---

## 📦 Repository Structure

```text
figcraft-studio/
├── .claude-plugin/
│   ├── marketplace.json               # Claude Code Marketplace catalog manifest
│   └── plugin.json                    # Claude Code Plugin manifest
├── plugin.json                        # Google Antigravity Plugin manifest
├── skill.json                         # Universal Agent Skills (skills.sh) manifest
├── README.md                          # Documentation
├── install.ps1                        # Windows universal installer (Antigravity & Claude Code)
├── install.sh                         # macOS / Linux universal installer
├── assets/
│   └── logo.svg                       # Plugin icon
├── rules/
│   └── AGENTS.md                      # Always-On Golden Pipeline & UI/UX Invariants
├── references/
│   └── vector-icons-24px.md           # 60+ normalized 24x24 SVG paths for FigCraft vector nodes
├── scripts/
│   ├── ensure-figcraft.ps1            # Auto-detect & launch FigCraft (--control 7979) on Windows
│   └── ensure-figcraft.sh             # Auto-detect & launch FigCraft (--control 7979) on macOS/Linux
└── skills/                            # 13 modular skills + ui-ux-pro-max CSV database
```

---

## 🛠️ Prerequisites

1. **FigCraft Desktop App** (`figcraft.exe` / `FigCraft.app`) installed.
2. **Python 3.x** (standard library only, zero `pip` packages required) for `ui-ux-pro-max/scripts/search.py`.
3. **FigCraft MCP Entry**:
   ```json
   {
     "mcpServers": {
       "figcraft": {
         "command": "C:\\Program Files\\FigCraft\\figcraft-cli.exe",
         "args": ["mcp", "--attach", "7979"]
       }
     }
   }
   ```

---

## 📄 License

MIT © [Doni Hadimas](https://github.com/donihadimas)
