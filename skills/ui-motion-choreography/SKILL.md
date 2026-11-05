---
name: ui-motion-choreography
description: "Apply design-engineering motion laws (Frequency-Speed Law, Exit-Faster-Than-Enter, Origin-Aware Popover Scaling, Spring Physics, and Reduced-Motion Accessibility) when specifying prototypes in FigCraft or implementing animations in React/Next.js/Tailwind/Mobile."
---

# UI Motion Choreography & Interaction Physics

Guides transition timing, easing curves, and spatial continuity so interfaces feel responsive and physical (Linear / Raycast / iOS standard) rather than sluggish or gimmicky.

## 1. The Frequency-Speed Law

Animation duration is inversely proportional to how frequently a user triggers the interaction:

| Interaction Tier | Examples | Duration (Enter) | Duration (Exit) | Easing / Physics |
| :--- | :--- | :--- | :--- | :--- |
| **Tier 1: High-Frequency Micro** (100×/day) | Button press, Hover state, Toggle switch, Tab switch, Command Palette (`⌘K`) | `100–150ms` | `80–120ms` | `cubic-bezier(0.16, 1, 0.3, 1)` (Fast ease-out) |
| **Tier 2: Spatial Overlay** (20×/day) | Dropdown menu, Tooltip, Popover, Toast, Select list | `160–200ms` | `120–150ms` | `cubic-bezier(0.22, 1, 0.36, 1)` + scale `0.96 -> 1` |
| **Tier 3: Structural Sheet / Modal** (5×/day) | Dialog modal, Mobile bottom sheet, Slide-over drawer | `240–320ms` | `180–220ms` | Spring (`stiffness: 380, damping: 30`) |
| **Tier 4: Page / Narrative Choreography** (1×/visit) | Hero entrance stagger, Onboarding reveal | `400–600ms` | `250ms` | `cubic-bezier(0.16, 1, 0.3, 1)`, stagger `40–60ms` |

## 2. Core Choreography Rules

1. **Exit Faster Than Enter**: Closing a modal, drawer, or dropdown must always take **25–30% less time** than opening it. Once the user dismisses an element, get it out of their way immediately.
2. **Origin-Aware Scaling (No `scale(0)`)**:
   - Never animate popovers or modals from `scale(0)` (looks like a cartoon). Animate from `scale(0.95)` or `scale(0.97)` + `opacity: 0` to `scale(1)` + `opacity: 1`.
   - Set `transform-origin` to match the trigger location (e.g., `origin-top-right` for a profile menu in the top-right navbar, `origin-bottom` for a dock tooltip).
3. **GPU-Composited Properties Only**:
   - Animate `transform` (`translate3d`, `scale`, `rotate`) and `opacity`.
   - Never animate `width`, `height`, `top`, `left`, `margin`, or `padding` on continuous frames without FLIP / Motion `layout` projection, as they trigger expensive browser layout recalculations.
4. **Tactile Press Feedback**:
   - Interactive buttons and cards compress slightly on `:active` / tap: `active:scale-[0.98]` or `active:translate-y-[1px]` within `80ms`.
5. **Mandatory `prefers-reduced-motion` Parity**:
   - When reduced motion is active, replace spatial `translate`/`scale` movement with a clean `120ms` opacity crossfade so functionality and state feedback remain clear without vestibular motion.
