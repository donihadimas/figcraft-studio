---
name: figcraft-design-system
description: "Build 3-layer Design Systems (Primitive -> Semantic -> Component tokens), Light/Dark mode Variable Collections, Paint/Text Styles, and reusable Master Components with Variants inside FigCraft. Use when creating a design system, token collection, theme variables, style library, or component kit in FigCraft."
---

# FigCraft Design System Architect

Builds systematic, token-driven design foundations inside FigCraft combining `ui-ux-pro-max` intelligence with FigCraft's native Variables, Styles, and Component Variants engine.

## Step 1: Ensure FigCraft & Generate Token Direction

1. Ensure FigCraft is running in attach mode via `ensure-figcraft.ps1`.
2. Query `ui-ux-pro-max` to generate a product-tailored palette and typography specification:
   ```powershell
   python "$HOME/.gemini/config/plugins/figcraft-studio/skills/ui-ux-pro-max/scripts/search.py" "<product_type> <industry> <vibe>" --design-system -p "<Project Name>"
   ```

**Completion criterion:** You have concrete hex values for Light & Dark semantic tokens (`background`, `foreground`, `card`, `primary`, `secondary`, `accent`, `muted`, `border`, `destructive`) and font pairings (`heading`, `body`, `mono`).

## Step 2: Create 3-Layer Variable Collections (Light & Dark Modes)

Use `figcraft/run_command` or `figcraft/batch` with `variable.*` commands to create a structured variable system rather than hardcoding hex colors on individual layers:

### Variable Commands in FigCraft
- `variable.createCollection`: `{"name": "1. Primitives"}` / `{"name": "2. Semantic Tokens"}`
- `variable.addMode`: `{"collection": <collectionId>, "name": "Dark"}` (renaming default mode to `"Light"` via `variable.renameMode`)
- `variable.create`: `{"collection": <collectionId>, "name": "color/bg/primary", "type": "color", "value": "#FFFFFF"}`
- `variable.set`: `{"id": <varId>, "mode": <modeId>, "value": "#09090B"}`
- `variable.bind`: `{"ids": [<nodeId>], "field": "fill" | "stroke" | "cornerRadius" | "gap" | "padding", "variable": <varId>}`

### Canonical Semantic Token Matrix
| Token Name | Role | Light Mode Example | Dark Mode Example |
| :--- | :--- | :--- | :--- |
| `surface/background` | Root page/screen canvas | `#FAFAFA` | `#09090B` |
| `surface/card` | Elevated container / card | `#FFFFFF` | `#18181B` |
| `surface/muted` | Secondary / subtle container | `#F4F4F5` | `#27272A` |
| `text/primary` | Headlines & primary body | `#09090B` | `#FAFAFA` |
| `text/secondary` | Supporting copy & labels | `#52525B` | `#A1A1AA` |
| `brand/primary` | Primary interactive CTA | `#2563EB` | `#3B82F6` |
| `brand/on-primary` | Label on primary CTA | `#FFFFFF` | `#FFFFFF` |
| `border/default` | Hairlines & input borders | `#E4E4E7` | `#27272A` |
| `status/danger` | Destructive / error state | `#DC2626` | `#EF4444` |

## Step 3: Register Paint & Text Styles

Create reusable document styles using `style.create`:
- **Typography Scale** (8pt-aligned line heights):
  - `Display / LG`: 48px, lineHeight 56, tracking -0.02em, Bold
  - `Heading / H1`: 32px, lineHeight 40, tracking -0.02em, Bold
  - `Heading / H2`: 24px, lineHeight 32, tracking -0.01em, SemiBold
  - `Heading / H3`: 18px, lineHeight 26, SemiBold
  - `Body / Regular`: 16px, lineHeight 24, Regular
  - `Body / Small`: 14px, lineHeight 20, Regular
  - `Caption / Label`: 12px, lineHeight 16, Medium

## Step 4: Build Master Components & Variants on a Dedicated Page

1. Create or select a `"Foundations & Components"` page (`page.add` -> `{"name": "Foundations & Components"}`).
2. Organize specimens inside labeled `section` or `frame` containers:
   - **Color Palette Swatches**: Grid of cards displaying token name, hex code, and contrast badge.
   - **Typography Specimens**: Vertical auto-layout stack showing each text style in context.
   - **Core UI Components**:
     - `Button` (Variants: `Variant=Primary|Secondary|Outline|Ghost`, `Size=SM|MD|LG`, `State=Default|Hover|Disabled`)
     - `Input Field` (Label above, input box `min-h: 44px`, helper/error text below, `gap: 6`)
     - `Badge / Status Pill`
     - `Card` & `Modal / Dialog`
3. Convert frames to master components using `component.create` (`{"ids": [<frameId>]}`) and group variants with `component.combineVariants`.
4. Instantiate components on product screens using `instance.create` (`{"component": <componentId>, "parent": <screenId>}`).

## Step 5: Visual Verification

Call `view.zoomFit` and `figcraft/screenshot` to verify swatch alignment, text legibility across Light/Dark frames, and clean auto-layout spacing.
