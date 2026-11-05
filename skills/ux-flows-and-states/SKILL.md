---
name: ux-flows-and-states
description: "Design complete 5-State UI Matrices (Ideal, Empty/Zero-Data, Skeleton Loading, Error/Offline, and Stress/Overflow edge cases) and multi-step user flows. Use when designing product screens in FigCraft or building production frontend/mobile features so interfaces never ship with only the Happy Path."
---

# UX Flows, Edge Cases & 5-State Completeness

Prevents the #1 product design tell of AI-generated interfaces: shipping only the **Happy Path** with 3 perfectly symmetrical items. Industrial-grade UI accounts for every lifecycle state of data and user interaction.

## 1. The Mandatory 5-State Matrix

Whenever designing a data-driven screen, component, or flow (in FigCraft or in code), evaluate and cover the **5 States**:

| State | Visual & Structural Specification | Anti-Pattern (Banned) |
| :--- | :--- | :--- |
| **1. Ideal (Populated)** | Realistic variance in item lengths (short & long names, varied badge statuses, realistic timestamps and currency figures). | 3 identical cards with equal 2-line descriptions and sequential numbers (`100`, `200`, `300`). |
| **2. Empty (Zero-Data)** | Centered container (`max-w: 360px`) inside the list/table region containing: (a) Subtle monochrome vector illustration or `40×40` tinted icon badge, (b) Clear title (`"Belum ada transaksi"`), (c) 1-sentence explanation of value, (d) Primary onboarding CTA (`"+ Buat Invoice Pertama"`). | Blank white/dark box or plain text `"No data found"`. |
| **3. Loading (Skeleton)** | Geometry-matched skeleton placeholders (`#27272A` dark / `#E4E4E7` light, `cornerRadius` matching final text/avatar nodes) preserving exact layout height to prevent Cumulative Layout Shift (`CLS = 0`). | Generic centered circular spinner (`⏳`) replacing the entire page container. |
| **4. Error / Partial Failure** | **Inline Field Error**: `1px` `#EF4444` border + icon + actionable message `6px` below the input. **Section/Network Error**: Subtle tinted alert banner (`fill: "#EF444414"`, `stroke: "#EF444440"`) with `"Coba Lagi"` button while preserving cached/surrounding UI. | Full-screen red crash page for a non-fatal API timeout, or wiping out user form input on submit error. |
| **5. Stress / Edge Overflow** | Long user names (`"Dr. Raden Mas Suryo Hadiningrat, S.Kom., M.T."`), large currency figures (`"Rp 948.250.000.000"`), 0 notifications vs `99+` badge, multi-line tags wrapping cleanly (`wrap: true`). | Fixed-height containers (`sizingV: "fixed"`) that clip wrapped text, or horizontal flex rows without truncation/wrapping rules. |

## 2. Interactive Component State Matrix

Every interactive control (Button, Input, Select, List Row, Tab, Card) requires explicit visual tokens across **5 interaction states**:

1. **Default**: Base fill, default border hairline, resting label contrast (`>= 4.5:1`).
2. **Hover (Pointer devices)**: Luminance shift (`+6%` in dark mode, `-4%` in light mode) or border prominence increase (`#27272A` $\rightarrow$ `#52525B`).
3. **Focus-Visible (Keyboard / A11y)**: `2px` high-contrast focus ring with `2px` offset (`ring-2 ring-offset-2`). Never remove focus outlines without a high-visibility replacement.
4. **Active / Pressed**: Slight physical compression (`scale(0.98)` or `-1px` Y translation) + deeper fill shade.
5. **Disabled**: Opacity `40–50%` OR muted semantic surface (`#F4F4F5` / `#18181B`) with muted text (`#A1A1AA` / `#52525B`), non-interactive cursor.

## 3. Multi-Screen Flow Ergonomics in FigCraft

When asked to design a feature flow in FigCraft:
1. Place frames horizontally from left to right on the canvas in chronological task order (`x` offset = `frameWidth + 80px`).
2. Include the **Trigger State** (Screen 1) $\rightarrow$ **Input / Modal / Action State** (Screen 2) $\rightarrow$ **Confirmation / Updated State** (Screen 3), plus an **Empty or Error companion frame** positioned below (`y` offset = `frameHeight + 100px`) when relevant.
3. Connect primary CTAs between frames using `proto.action.add` so the flow is immediately testable in FigCraft Prototype Preview.
