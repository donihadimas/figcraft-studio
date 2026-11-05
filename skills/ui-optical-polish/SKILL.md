---
name: ui-optical-polish
description: "Enforce studio-grade optical precision, concentric border-radius math, layered elevation & specular borders, tabular numerals, and optical icon/text alignment across FigCraft designs and Web/Mobile UI code. Use when polishing UI components, designing cards/modals/buttons/tables, or fixing interfaces that look flat, amateur, or AI-generated."
---

# UI Optical Polish & Surface Craft

Eliminates subtle geometric and optical flaws that distinguish amateur/AI-generated UI from Apple, Linear, Raycast, and Stripe craftsmanship. Apply these rules both when constructing frames in **FigCraft** and when writing **CSS/Tailwind/Mobile** code.

## 1. Concentric Border-Radius Mathematics

Nested rounded containers with the same `cornerRadius` create an ugly, pinched optical bulge at the corners. Always compute nested radii using the concentric formula:

$$R_{\text{outer}} = R_{\text{inner}} + \text{Padding}$$

| Outer Radius ($R_{\text{outer}}$) | Container Padding ($P$) | Inner Element Radius ($R_{\text{inner}}$) | FigCraft / Tailwind Mapping |
| :--- | :--- | :--- | :--- |
| `24px` (`rounded-3xl`) | `12px` (`p-3`) | `12px` (`rounded-xl`) | Outer `cornerRadius: 24`, `padding: 12` $\rightarrow$ Inner `cornerRadius: 12` |
| `20px` | `8px` (`p-2`) | `12px` (`rounded-xl`) | Outer `cornerRadius: 20`, `padding: 8` $\rightarrow$ Inner `cornerRadius: 12` |
| `16px` (`rounded-2xl`) | `8px` (`p-2`) | `8px` (`rounded-lg`) | Outer `cornerRadius: 16`, `padding: 8` $\rightarrow$ Inner `cornerRadius: 8` |
| `14px` | `6px` (`p-1.5`) | `8px` (`rounded-lg`) | Outer `cornerRadius: 14`, `padding: 6` $\rightarrow$ Inner `cornerRadius: 8` |
| `12px` (`rounded-xl`) | `4px` (`p-1`) | `8px` (`rounded-lg`) | Segmented Control / Tab Container (`12px`) $\rightarrow$ Active Pill (`8px`) |

**Floor Rule**: If $R_{\text{outer}} - P \le 2\text{px}$, clamp $R_{\text{inner}}$ to `4px` (never `0px` inside a rounded parent).

## 2. Surface Luminance, Specular Hairlines & Layered Shadows

### Dark Mode Elevation = Luminance (Not Drop Shadow)
Drop shadows are nearly invisible on dark backgrounds (`#09090B`). In dark mode, communicate elevation by stepping surface luminance upward + adding a `1px` top/inner border highlight:
- **Level 0 (Canvas)**: `#09090B` (`zinc-950`)
- **Level 1 (Card / Sidebar)**: `#121215` with `1px` stroke `#27272A` (`#FFFFFF12`)
- **Level 2 (Elevated Modal / Popover / Active Card)**: `#18181B` (`zinc-900`) with `1px` stroke `#3F3F46` (`#FFFFFF1F`) + subtle inner top highlight (`inset 0 1px 0 rgba(255,255,255,0.08)`)
- **Level 3 (Floating Command Bar / Tooltip)**: `#27272A` (`zinc-800`)

### Light Mode Elevation = Tinted Multi-Layer Shadow + Hairline Ring
Never use a single muddy black shadow (`0 4px 10px rgba(0,0,0,0.25)`). Combine a `1px` low-opacity border with a 2-layer ambient + key shadow:
- **FigCraft `effects`**:
  ```json
  "stroke": "#09090B0F",
  "strokeWeight": 1,
  "effects": [
    {"type": "dropShadow", "color": "#09090B08", "offset": [0, 1], "radius": 2},
    {"type": "dropShadow", "color": "#09090B0D", "offset": [0, 8], "radius": 24}
  ]
  ```
- **Tailwind CSS**:
  `ring-1 ring-zinc-950/5 shadow-[0_1px_2px_rgba(9,9,11,0.04),0_8px_24px_rgba(9,9,11,0.05)]`

## 3. Optical Alignment vs. Mathematical Centering

1. **Asymmetric Icon-Button Padding**:
   - A button with a leading icon (`[Icon] Label`) looks lopsided with equal horizontal padding.
   - Apply **less padding on the icon side** than the text side: e.g. `padding: [10, 16, 10, 12]` (`pl-3 pr-4 py-2.5`) with `gap: 8`.
   - For trailing arrow/chevron buttons (`Label [→]`), apply `padding: [10, 12, 10, 16]` (`pl-4 pr-3 py-2.5`).
2. **Triangular / Play / Chevron Optical Offset**:
   - A play triangle (`▶`) or right chevron (`›`) inside a circular button has its visual center of mass shifted left of its bounding box center. Shift the vector `1px–1.5px` toward the pointed tip (`x + 1.5`) so it appears optically centered.
3. **Badge & Input Vertical Baseline**:
   - Uppercase status badges (`ACTIVE`, `PRO`) have no descenders (`g, y, p`), so mathematical vertical centering makes them look slightly too low on some fonts. Use `lineHeight` equal to `fontSize` (`leading-none`) inside a fixed-height pill (`height: 22px` or `24px`, `crossAlign: "center"`).

## 4. Typographic Precision & Tabular Numerals

| Element | Font Size | Tracking (`letterSpacing`) | Line Height | Mandatory OpenType / CSS Rule |
| :--- | :--- | :--- | :--- | :--- |
| **Display Hero** | `48–72px` | `-0.03em` to `-0.025em` | `1.05–1.1` | `text-wrap: balance` |
| **Section H1/H2** | `28–40px` | `-0.02em` | `1.15–1.2` | `text-wrap: balance` |
| **Card Title (H3)** | `18–20px` | `-0.01em` | `1.3` | `font-semibold` |
| **Body Copy** | `15–16px` | `0em` | `1.5–1.6` | `max-w-[65ch]`, `text-wrap: pretty` |
| **UI Control / Table Cell** | `13–14px` | `0em` | `1.4` | Single line unless long prose |
| **Numeric Metrics / Prices / Timers** | Any | `-0.01em` | `1.2` | **`tabular-nums` (`tnum`)** + right-align in tables |

**Completion Criterion**: Every nested container obeys $R_{\text{outer}} = R_{\text{inner}} + P$, every numeric column/metric uses tabular alignment, and surface borders use subtle hairlines (`6–12%` opacity) instead of heavy high-contrast strokes.
