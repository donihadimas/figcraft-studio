---
name: figcraft-mobile-ui
description: "Design professional iOS and Android mobile app screens and flows in FigCraft. Enforces safe-area insets, status/home indicator clearance, 44pt/48dp touch targets, 4/8dp spacing rhythm, vector icons (no emojis), and Light/Dark parity. Use when designing mobile apps, iOS/Android screens, React Native, Flutter, SwiftUI, or Jetpack Compose UI in FigCraft."
---

# FigCraft Mobile UI Specialist (iOS & Android)

Designs production-grade mobile interfaces in FigCraft following platform-native ergonomics (Apple HIG & Material Design 3) and the canonical mobile checklist from `ui-ux-pro-max`.

## Step 1: Auto-Launch FigCraft & Research Mobile Palette/Pattern

1. Run `ensure-figcraft.ps1` to verify FigCraft is attached on port `7979`.
2. Query `ui-ux-pro-max` for domain-appropriate mobile palettes and UX guidelines:
   ```powershell
   python "$HOME/.gemini/config/plugins/figcraft-studio/skills/ui-ux-pro-max/scripts/search.py" "<app_category> mobile app" --design-system -p "<AppName>"
   ```

## Step 2: Select Native Device Preset & Grid Rhythm

Create screens using `frame.create` with official presets and place multi-screen flows horizontally with `gap: 80px` between screens:

| Platform | FigCraft Preset Name | Dimensions (px) | Safe Area Top | Safe Area Bottom | Min Touch Target |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **iOS Standard** | `iPhone 16` | `393 × 852` | `59px` (Dynamic Island) | `34px` (Home Indicator) | `44 × 44 pt` |
| **iOS Pro Max** | `iPhone 16 Pro Max` | `440 × 956` | `59px` | `34px` | `44 × 44 pt` |
| **Android Compact** | `Android Compact` | `412 × 917` | `24–36dp` (Status Bar) | `24dp` (Gesture Bar) | `48 × 48 dp` |
| **Tablet** | `iPad Pro 11"` | `834 × 1194` | `24px` | `20px` | `44 × 44 pt` |

## Step 3: Enforce Anatomy of a Mobile Screen in FigCraft

Structure every mobile screen frame as a `vertical` Auto-Layout container (`width: 393`, `height: 852`, `layout: "vertical"`, `gap: 0`, `clip: true`) divided into 3 structural zones:

1. **Top System & App Bar Zone (`sizingH: "fill"`, `sizingV: "hug"`)**:
   - **Status Bar** (`height: 54px`, `padding: [18, 24, 8, 24]`, `mainAlign: "spaceBetween"`): Time (`9:41`, `SemiBold`, `15px`) on left; Cellular/Wi-Fi/Battery vector shapes on right.
   - **Navigation Header** (`height: 48–56px`, `padding: [8, 20, 8, 20]`): Back button/title/action icons with minimum `44×44` tap frame containers.
2. **Scrollable Content Body (`sizingH: "fill"`, `sizingV: "fill"`, `layout: "vertical"`, `padding: [16, 20, 24, 20]`, `gap: 16` or `20`)**:
   - Follow a strict **4/8dp spacing rhythm** (`4, 8, 12, 16, 20, 24, 32`).
   - **Cards & Lists**: Use subtle 1px borders (`strokeWeight: 1`) or surface elevation contrast (`#18181B` on `#09090B` dark, or `#FFFFFF` on `#F4F4F5` light), `cornerRadius: 16` or `20`.
   - **Typography Scale (Mobile)**:
     - Screen Title: `24–28px` Bold, `lineHeight: 32`
     - Section Header: `17–18px` SemiBold, `lineHeight: 24`
     - Primary Body / List Title: `15–16px` Medium/Regular, `lineHeight: 22`
     - Secondary Meta / Caption: `12–13px` Regular, `lineHeight: 18` (never `< 11px`)
3. **Bottom Navigation / Sticky CTA Zone (`sizingH: "fill"`, `sizingV: "hug"`)**:
   - **Bottom Tab Bar**: Max **4–5 destinations**. `padding: [10, 16, 28, 16]` (includes bottom safe-area inset for Home Indicator pill `134×5px`, `cornerRadius: 100`).
   - Active tab uses brand primary fill/text; inactive tabs use muted foreground with `>= 3:1` icon contrast.

## Step 4: Mobile Anti-Slop & Quality Rules

- **Zero Emoji Icons**: Never place emojis (`🏠`, `⚙️`, `🔔`) as navigation or UI icons in FigCraft. Construct crisp vector paths (`type: "vector"` with SVG `path` data) or geometric icon primitives inside `24×24` frames with consistent `1.5px` or `2px` strokes.
- **No Edge-to-Edge Text**: Keep horizontal screen padding at `16px` or `20px` minimum.
- **State Coverage**: When designing multi-screen flows, include realistic data (no `Lorem ipsum` or `Item 1, Item 2`), plus empty/loading/active states or Light + Dark mode companion screens when requested.
- **Prototype Links**: Connect multi-screen flows using `proto.action.add` so the user can preview interactive transitions in FigCraft.

## Step 5: Mandatory Visual Check

Run `view.zoomFit` and `figcraft/screenshot` on all created mobile screens. Verify:
- [ ] Content does not overflow `852px` height or collide with the bottom tab bar / home indicator
- [ ] All text wraps cleanly (`sizingH: "fill"` inside vertical auto-layout frames)
- [ ] Contrast meets WCAG AA (`>= 4.5:1` for body text, `>= 3:1` for UI controls)
