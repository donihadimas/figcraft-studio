---
name: figcraft-icon-craft
description: "Master rules, mathematical keyline grids, and execution pipelines for designing studio-grade App Launcher Icons (Android Adaptive, iOS Squircle), brand logos, and 24px in-app vector SVG icons inside FigCraft. Integrates FigCraft MCP and Python scripts. Use when designing logos, app icons, favicons, or vector feature icons in FigCraft."
argument-hint: "[app name or icon concept]"
license: MIT
metadata:
  author: Doni Hadimas
  version: "1.0.0"
---

# FigCraft Icon & Logo Craft Specialist

Professional framework, keyline geometry, and execution pipeline for crafting studio-grade **App Launcher Icons**, **Brand Logos**, and **In-App Vector Feature Icons (SVG & PNG)** directly inside **FigCraft**.

---

## 1. The 5 Golden Invariants of Icon Design

Every icon or logo designed in FigCraft must satisfy these five non-negotiable rules:

1. **The 16px–1024px Scalability Law (Silhouette First)**:
   - An icon must be instantly identifiable as a solid silhouette at **16×16px** (favicon / notification) and **48×48px** (phone home screen), while appearing rich and textured at **1024×1024px** (App Store / Play Store listing).
   - **Anti-Clutter Rule**: Strictly prohibit fine lines ($< 6\text{px}$ on 1024 canvas), micro-ornaments, paragraphs of text, or realistic photographic details that degrade into visual noise at small sizes.
2. **Single Focal Metaphor**:
   - Exactly **one dominant hero symbol** (e.g., a crescent moon, a compass needle, or a geometric arch). Never merge 3+ unrelated metaphors into a single icon frame.
   - Secondary accents (such as a tiny star or light gleam) must remain subordinate ($\le 20\%$ of total visual weight).
3. **Decoupled 2-Layer Architecture (Adaptive Standard)**:
   - Never design a flat, single-layer raster file for mobile apps.
   - Always structure your FigCraft frame with two discrete top-level layers:
     * **`[Background]`**: 1024×1024 solid color or subtle radiant gradient.
     * **`[Foreground]`**: Transparent 1024×1024 layer containing the hero symbol centered strictly inside the Safe Zone.
4. **Optical vs. Geometric Centering**:
   - Asymmetrical shapes (such as crescent moons, play triangles, or stars) must be **optically centered** rather than placed at the exact mathematical bounding-box center. Shift visual weight toward the optical center of gravity ($+20\text{px}$ to $+40\text{px}$ offset adjustment).
5. **Lighting & Specular Hairlines (Anti-Flat / Anti-Slop)**:
   - Avoid completely flat matte fills and avoid garish 2010s skeuomorphic bevels.
   - Use subtle 90° or 135° directional lighting, soft ambient occlusion depth, and a **1px inner specular hairline border** (`rgba(255, 255, 255, 0.18)` on dark surfaces or `rgba(0, 0, 0, 0.08)` on light surfaces) to separate the icon from dynamic OS wallpapers.

---

## 2. Keylines & Mathematical Grid Systems

### A. Android Adaptive Icon (Master 1024×1024 Canvas)
Android displays icons inside various OEM masks (circles, squircles, rounded squares, teardrops).

```
+-------------------------------------------------------+  (0, 0)
| [OUTER CANVAS: 1024 x 1024]                           |
|                                                       |
|       +---------------------------------------+       |
|       | [OEM MASK VIEWPORT: dia 682px / 72dp] |       |
|       |                                       |       |
|       |       +-----------------------+       |       |
|       |       | [SAFE ZONE: dia 626px]|       |       |
|       |       |  Hero Symbol strictly |       |       |
|       |       |  inside this circle   |       |       |
|       |       +-----------------------+       |       |
|       |                                       |       |
|       +---------------------------------------+       |
|                                                       |
+-------------------------------------------------------+  (1024, 1024)
```

* **Full Dimensions**: $1024 \times 1024\text{px}$ (108dp base).
* **OEM Visible Mask**: Circle diameter of **682px** (72dp base).
* **Safe Zone**: Circle diameter of **626px** (66dp base) centered at $(512, 512)$.
* **Hard Rule**: No critical elements of the foreground logo may spill outside the 626px circle. The remaining outer canvas is bleed area used by OS parallax and wobble physics.

### B. Apple iOS App Icon (Master 1024×1024 Canvas)
* **Canvas**: $1024 \times 1024\text{px}$ solid square.
* **Curvature Mask**: Continuous superellipse squircle with curvature formula:
  $$\left|\frac{x}{512}\right|^{4.5} + \left|\frac{y}{512}\right|^{4.5} = 1 \quad (\text{equivalent to corner radius } \approx 224\text{px})$$
* **Safe Live Area**: $800 \times 800\text{px}$ centered (margin $112\text{px}$ on all four edges).
* **Zero Transparency**: iOS strictly rejects alpha channels / transparent backgrounds on App Store icons.

### C. In-App Vector Feature Icons (24×24dp SVG Standard)
* **Canvas**: $24 \times 24\text{px}$, `viewBox="0 0 24 24"`.
* **Live Area**: $20 \times 20\text{px}$ with a uniform $2\text{px}$ outer padding.
* **Stroke Standard**: Uniform $1.5\text{px}$ or $2.0\text{px}$ stroke width.
* **Terminal Points**: Always apply `stroke-linecap="round"` and `stroke-linejoin="round"`.

---

## 3. Geometric & Boolean Construction (Islamic & Brand Motifs)

When creating icons for religious, heritage, or spiritual products like **Shaumi**:

1. **The Golden Crescent (Hilal)**:
   - Construct using boolean subtraction of two circles:
     * Outer circle: Radius $R_1 = 260\text{px}$ at $(512, 512)$.
     * Subtraction cutter circle: Radius $R_2 = 210\text{px}$ offset to $(560, 480)$.
   - Rotate the crescent tilt angle by $-15^\circ$ to $-25^\circ$ to evoke upward spiritual aspiration.
2. **Rub el Hizb (8-Point Islamic Star)**:
   - Overlay two identical squares rotated $45^\circ$ relative to each other, with corner radius $r = 8\text{px}$ on the vertices for tactile softness.
3. **Mihrab / Islamic Arch**:
   - Construct a horseshoe or pointed arch (ogee curve) with symmetrical cubic bezier control points.
4. **Concentric Container Math**:
   - Always enforce:
     $$R_{\text{outer}} = R_{\text{inner}} + \text{Padding}$$

---

## 4. FigCraft MCP Execution Workflow

To design, review, and export icons inside FigCraft:

### Step 1: Auto-Launch FigCraft Attach Mode
Always run `ensure-figcraft.ps1` (Windows) or `ensure-figcraft.sh` (macOS/Linux) before calling MCP tools.

### Step 2: Initialize Icon Canvas with Keyline Guides
Use `figcraft/batch` to create:
1. Top-level frame: `Icon_Master_1024` ($1024 \times 1024\text{px}$).
2. Layer `[Background]`: Solid fill or radial gradient.
3. Layer `[Guide_SafeZone]` (temporary/hidden during export): Circle $626 \times 626\text{px}$ with dashed outline at $(199, 199)$.
4. Layer `[Foreground]`: Group containing the hero vector paths.

### Step 3: Build the Vector Artwork
* Use `create_node` with `type: "vector"` and SVG `props.paths` or boolean combinations (`subtract`, `union`).
* Add 1px specular inner stroke to foreground elements:
  ```json
  "strokes": [{"type": "solid", "color": {"r": 1, "g": 1, "b": 1, "a": 0.22}}],
  "strokeWeight": 2
  ```

### Step 4: Visual Inspection & Verification
* Call `view.zoomFit` + `figcraft/screenshot`.
* Check against the 100-Point Audit: Is the logo centered optically? Is it legible when looking at the thumbnail?

### Step 5: Export Deliverables via `figcraft/export`
Call `figcraft/export` for production assets:
```json
// 1. Full iOS & Store Master (1024x1024 PNG)
{"ids": ["Icon_Master_1024"], "format": "png", "size": "1024w", "path": "path/to/app_icon_full.png"}

// 2. Android Adaptive Foreground (1024x1024 PNG with transparent bg)
{"ids": ["Foreground_Group"], "format": "png", "size": "1024w", "path": "path/to/app_icon_foreground.png"}

// 3. Android Adaptive Background (1024x1024 PNG)
{"ids": ["Background_Layer"], "format": "png", "size": "1024w", "path": "path/to/app_icon_background.png"}

// 4. In-App Vector Icon (SVG)
{"ids": ["Icon_Vector_Layer"], "format": "svg", "svgSimplifyStroke": true, "path": "path/to/icon.svg"}
```

---

## 5. Automated Python Slicing Pipeline

When FigCraft exports the 1024×1024 master, run the Python utility script to populate Android and iOS mipmaps:

```powershell
python "$HOME/.gemini/config/plugins/figcraft-studio/skills/figcraft-icon-craft/scripts/generate_app_icons.py" \
  --master "path/to/app_icon_full.png" \
  --foreground "path/to/app_icon_foreground.png" \
  --background "path/to/app_icon_background.png" \
  --android-res "shaumi-mobile/android/app/src/main/res" \
  --ios-assets "shaumi-mobile/ios/Runner/Assets.xcassets/AppIcon.appiconset"
```

---

## 6. Icon Design Checklist (Gate Approval)

Before shipping any icon to production, verify:
- [ ] **Android Safe Zone**: Entire foreground logo sits within the 626px circle diameter.
- [ ] **iOS Squircle Clearance**: No critical details within 112px of the 1024 canvas edges.
- [ ] **16px Favicon Test**: Is the silhouette instantly readable at thumbnail size?
- [ ] **Zero Slop**: No generic neon glow blobs or random purple mesh gradients.
- [ ] **Contrast Ratio**: At least 4.5:1 luminance contrast against both pure black (#000000) and pure white (#FFFFFF) device wallpapers.

