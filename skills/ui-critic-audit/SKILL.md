---
name: ui-critic-audit
description: "Run a rigorous 100-Point Visual QA & Anti-Slop Design Critique on any FigCraft canvas (via screenshot + inspect_document) or Web/Mobile UI. Detects layout collisions, concentric radius errors, low contrast, generic AI tells, and executes corrective fixes before delivery."
---

# UI Critic & 100-Point Visual QA Auditor

Acts as a Principal Design Critic. Run this audit before finalizing any major design in FigCraft or frontend/mobile code, or whenever the user asks to review/critique/improve an existing UI.

## Step 1: Capture Visual & Structural Evidence

1. **In FigCraft**: Call `figcraft/inspect_document` (`{"depth": 5}`) AND `figcraft/screenshot` on the target frame(s).
2. **In Code**: Inspect the component markup/styles and any rendered preview/screenshot.

## Step 2: Score Against the 100-Point Industrial Design Rubric

Evaluate the interface across 5 categories (20 points each). Any score below **85/100** or any **Critical Fail** requires an immediate refinement pass before presenting the work as finished:

### 1. Visual Hierarchy & Squint Test (20 pts)
- [ ] **Focal Point (8 pts)**: When squinting at the screenshot, is there an unmistakable #1 primary element (Headline/Primary Metric) and #1 primary action (CTA)?
- [ ] **Typographic Contrast (6 pts)**: Clear jump between Heading (`24–56px` Bold/SemiBold), Body (`15–16px` Regular), and Meta/Label (`12–13px` Muted). No two adjacent hierarchy levels share the same size + weight + color.
- [ ] **Surface Grouping (6 pts)**: Related items are grouped by proximity (`gap: 8–12px`) and separated from other groups by larger whitespace (`gap: 24–48px`) or a subtle `1px` hairline—without wrapping every single item in a redundant card box.

### 2. Layout Geometry & Auto-Layout Integrity (20 pts)
- [ ] **Zero Clipping / Collision (8 pts)**: No text overflows its parent frame, collides with sibling nodes, or wraps awkwardly (e.g. a button label wrapping onto 2 lines).
- [ ] **Grid & Rhythm Alignment (6 pts)**: All paddings, gaps, and sizes sit on the `4/8px` spatial scale (`4, 8, 12, 16, 20, 24, 32, 48, 64`). Left edges of stacked elements align cleanly on shared x-coordinates.
- [ ] **Safe Area & Viewport Discipline (6 pts)**: Mobile screens respect top status bar (`54px`) and bottom home indicator (`34px`); Web heroes fit inside the initial viewport without pushing the primary CTA below the fold.

### 3. Optical Craft & Color Contrast (20 pts)
- [ ] **WCAG AA Contrast (8 pts)**: Primary/secondary text meets `>= 4.5:1` against its actual background fill; interactive controls and icons meet `>= 3:1`.
- [ ] **Concentric Radii (6 pts)**: Nested rounded elements follow $R_{\text{outer}} = R_{\text{inner}} + \text{Padding}$.
- [ ] **Border & Shadow Restraint (6 pts)**: Hairlines use subtle alpha/muted tokens (`6–12%` contrast), not harsh `1px solid #888`; dark mode uses surface luminance stepping instead of muddy black shadows.

### 4. Anti-Slop & Authenticity Check (20 pts)
- [ ] **No AI Palette/Gradient Clichés (7 pts)**: Free of unrequested purple/cyan neon glows, generic centered dark-mesh heroes, or unrequested beige+brass templates.
- [ ] **No Emoji Icons or Fake Chrome (7 pts)**: All icons are proper vector paths (`24×24` or `16×16` consistent stroke); no `🎨 🚀 ⚡` emojis used as structural UI icons.
- [ ] **Layout Variety (6 pts)**: Does not repeat identical 3-column card rows or tracked-out uppercase eyebrows above every single section.

### 5. UX Copy & State Realism (20 pts)
- [ ] **Zero Placeholder Slop (8 pts)**: No `Lorem ipsum`, `John Doe`, `Item 1 / Item 2`, or generic `"Submit"` / `"Learn More"` buttons.
- [ ] **Tabular Numerals & Formatting (6 pts)**: Prices, percentages, dates, and IDs are realistic and aligned.
- [ ] **Interaction Affordance (6 pts)**: Active, selected, muted, and secondary controls are visually distinct.

## Step 3: Execute Immediate Corrective Pass

For every failed checkbox identified in Step 2:
1. Apply the fix immediately via `figcraft/batch` / `figcraft/set_properties` (or code edit).
2. Re-run `figcraft/screenshot` to confirm the fix resolved the issue visually.
3. Report the final audit score and key improvements concisely to the user.
