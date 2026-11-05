---
name: figcraft-web-ui
description: "Design distinctive desktop web interfaces, landing pages, portfolios, and SaaS dashboards inside FigCraft. Applies Taste-Skill anti-slop rules, 3 Design Dials (Variance, Motion, Density), Bento grids, and studio-grade typography. Use when designing websites, landing pages, web apps, or admin dashboards in FigCraft."
---

# FigCraft Web, Landing Page & Dashboard Specialist

Combines the studio-grade aesthetic discipline of `design-taste-frontend` and `frontend-design` with `ui-ux-pro-max` data to build web layouts, landing pages, and SaaS dashboards directly on the FigCraft canvas.

## Step 1: Output Design Read & Set the 3 Dials

1. Ensure FigCraft is running in attach mode (`ensure-figcraft.ps1`).
2. State a one-line **Design Read** before creating nodes:
   > *"Reading this as: `<page kind>` for `<audience>`, with a `<vibe>` language, leaning toward `<aesthetic family>`."*
3. Set the 3 Dials (`1–10`):
   - `DESIGN_VARIANCE` (default `7` for landing pages, `4` for dense SaaS dashboards)
   - `MOTION_INTENSITY` (default `6`)
   - `VISUAL_DENSITY` (default `4` for marketing/editorial, `7–8` for analytics/admin dashboards)
4. Query `ui-ux-pro-max` with the dials to retrieve curated palette, typography, and layout patterns:
   ```powershell
   python "$HOME/.gemini/config/plugins/figcraft-studio/skills/ui-ux-pro-max/scripts/search.py" "<query>" --design-system --variance 7 --density 4 -p "<Project>"
   ```

## Step 2: Frame Setup & Grid Architecture in FigCraft

Use `frame.create` with `"preset": "Desktop"` (`1440px` width) and `layout: "vertical"`, `sizingV: "hug"`:
- **Container Max-Width**: Inside `1440px` full-bleed sections, constrain content containers to `1200px` or `1280px` width (`padding: [80, 120, 80, 120]` for marketing sections; `padding: [24, 32, 24, 32]` for dashboards).
- **12-Column Visual Rhythm**: Attach a layout grid via `grid.add` (`{"ids": [<frameId>], "grid": {"pattern": "columns", "count": 12, "gutter": 24, "margin": 120}}`) when precision alignment is needed.

## Step 3: Landing Page Anti-Slop Rules in FigCraft

1. **Navigation Bar**:
   - Single line, height `64–72px` (`max 80px`), `mainAlign: "spaceBetween"`, `crossAlign: "center"`.
   - Brand mark on left, 3–5 concise nav links in center/right, 1 primary CTA pill/button on far right.
2. **Hero Section Discipline**:
   - Must fit within the initial `900px` viewport height.
   - **Max 4 text elements**: (1) Optional Eyebrow, (2) Headline (`48–64px`, max 2 lines), (3) Subtext (`18px`, max 20 words, max 3 lines), (4) CTA row (1 primary CTA + optional secondary CTA).
   - **Anti-Center Bias**: When `DESIGN_VARIANCE > 4`, prefer **50/50 Split Hero** (left copy stack + right interactive product preview frame/visual) or **Asymmetric Editorial Hero** over generic centered text on a dark purple mesh.
   - **Social Proof / Logo Wall**: Place in a dedicated strip **below** the hero frame, never crammed inside the hero text stack.
3. **Bento Grid & Section Diversity**:
   - Never repeat the same 3-equal-card row twice in a row. Alternate layout families: Split Feature, Asymmetric Bento Grid (`2+1` or `1+2` cells), High-Contrast Metric Strip, Editorial Quote, Interactive Spec Matrix.
   - **Eyebrow Restraint**: At most 1 tracked-out uppercase eyebrow label per 3 sections.
   - **Bento Background Variation**: Vary cell fills (subtle surface tint, accent card, data chart preview, vector diagram) instead of 6 identical flat cards.

## Step 4: SaaS Dashboard & Data-Dense Web UI Rules

When designing internal tools, admin consoles, or analytics dashboards (`VISUAL_DENSITY: 7–8`):
- **App Shell Layout**: Horizontal root frame (`1440 × 960`), left Sidebar (`width: 240–260px`, `fill`, `stroke` divider) + right Main Workspace (`sizingH: "fill"`, `layout: "vertical"`).
- **Top Header Bar**: Breadcrumb + Global Search (`⌘K` badge) + Filter pills + Primary Action button (`height: 60px`).
- **KPI Summary Strip**: 3–4 metric cards with label, primary tabular figure (`28–32px SemiBold`), delta badge (`+12.4%` in semantic emerald/red), and sparkline vector path.
- **Charts & Tables**: Draw crisp vector line/area/bar charts (`type: "vector"`) with axis labels and legends, paired with a structured data table frame using `horizontal` auto-layout rows, status badges, and right-aligned numeric columns.

## Step 5: Self-Critique via `screenshot`

1. Run `view.zoomFit` and capture `figcraft/screenshot` of the full desktop frame (and individual sections if tall).
2. Audit against the brief:
   - Are any headlines wrapping past 2 lines or overlapping adjacent containers?
   - Are CTA button labels on a single line with WCAG AA contrast?
   - Does every auto-layout container have proper `sizingH` / `sizingV` (`hug` vs `fill`) so nothing clips?
3. Refine with `set_properties` / `batch` before finishing.
