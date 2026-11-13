---
name: figcraft-remove-bg
description: "Studio-grade AI background removal using BRIA RMBG 2.0 via rembg and ONNX Runtime. Removes backgrounds from icons, logos, portraits, and product mockups with sub-pixel matting, ghost-alpha noise cleanup, tight subject cropping, and Android Adaptive Icon safe-zone centering (1024x1024, phi 626px). Integrates with FigCraft MCP and pipeline scripts. Use when removing backgrounds from canvas assets, extracting transparent logo marks, or preparing transparent foregrounds in FigCraft."
argument-hint: "[image path or directory] [--tight] [--adaptive-icon]"
license: MIT
metadata:
  author: Doni Hadimas
  version: "1.0.0"
---

# FigCraft AI Background Removal Specialist (BRIA RMBG 2.0)

Industrial-grade background removal and transparent asset synthesis for **FigCraft Design Studio**, powered by the state-of-the-art **BRIA RMBG 2.0** neural model running locally via `rembg` and **ONNX Runtime**.

---

## 1. The 4 Non-Negotiable Invariants of Transparent Assets

Every transparent layer extracted or processed in FigCraft must strictly satisfy:

1. **Zero Ghost Pixels ($\alpha < 10 \to 0$)**:
   - Neural models produce faint probability tails ($\alpha = 1 \dots 9$) around transparent regions. If left unfiltered, these cause dark smudges, fringe lines, and halos when composited over dark or light UI backgrounds.
   - All extractions must filter ghost alpha artifacts to pure `(0, 0, 0, 0)` while preserving smooth sub-pixel anti-aliasing on edges ($\alpha \ge 10$).
2. **Sub-Pixel Anti-Aliased Matting**:
   - Strictly prohibit hard binary thresholding or magic-wand jagged cuts. RMBG 2.0 provides continuous alpha gradation across edge gradients (hair, glass, specular metallic ribbons, cloth).
3. **Decoupled 2-Layer Mobile Architecture**:
   - Mobile launcher icons must NEVER merge the foreground symbol with the background tile into a single flat layer.
   - Foreground marks must be extracted independently and placed on a 1024×1024 transparent canvas respecting the **Android Safe Area Circle** ($\varnothing 626\text{px}$ diameter, radius $\le 313\text{px}$).
4. **Region-of-Interest (ROI) Isolation for Nested Cards**:
   - When a logo or mark is embedded inside a rounded card, squircle tile, or presentation container, RMBG 2.0 may identify the *entire card* as the primary subject.
   - Use `--crop-box <x0> <y0> <x1> <y1>` to crop slightly inside the container borders before AI segmentation so only the hero emblem is extracted.

---

## 2. CLI Execution & Tooling

The companion Python CLI script is located at:
`$HOME/.gemini/config/plugins/figcraft-studio/scripts/remove-bg.py`
*(also accessible via `skills/figcraft-remove-bg/scripts/remove_bg.py`)*

### A. Quick Commands

```powershell
# 1. Standard Transparent Extraction
python "$HOME/.gemini/config/plugins/figcraft-studio/scripts/remove-bg.py" "input.png" -o "output.png"

# 2. Tight Crop (Trims transparent padding to exact subject bbox)
python "$HOME/.gemini/config/plugins/figcraft-studio/scripts/remove-bg.py" "input.png" --tight -o "output_tight.png"

# 3. Android Adaptive Icon Foreground (1024x1024 canvas, phi 626px safe zone)
python "$HOME/.gemini/config/plugins/figcraft-studio/scripts/remove-bg.py" "logo_master.png" --adaptive-icon -o "ic_launcher_foreground.png"

# 4. Nested Logo Extraction from Squircle Card (with Pre-Crop)
python "$HOME/.gemini/config/plugins/figcraft-studio/scripts/remove-bg.py" "app_icon_card.png" --crop-box 190 150 870 810 --adaptive-icon -o "ic_launcher_foreground.png"

# 5. Batch Process Entire Directory of Assets
python "$HOME/.gemini/config/plugins/figcraft-studio/scripts/remove-bg.py" "raw_assets/" -o "clean_assets/"

# 6. Export Alpha Matte Mask Only (Black & White PNG)
python "$HOME/.gemini/config/plugins/figcraft-studio/scripts/remove-bg.py" "portrait.jpg" --mask-only -o "portrait_mask.png"
```

---

## 3. Workflow Inside FigCraft Canvas

When interacting with a FigCraft `.figcraft` document via FigCraft MCP:

```
[FigCraft Canvas]
       │
       ▼  (1) figcraft/export (nodeId, format: "png")
[Raw Node Image]
       │
       ▼  (2) python remove-bg.py input.png --tight -o clean.png
[Transparent Cutout]
       │
       ▼  (3) figcraft/batch (create image fill or transparent vector/layer)
[Clean Transparent FigCraft Node]
```

### Step-by-Step Canvas Pipeline:
1. **Export the Target Layer**:
   ```json
   {
     "nodeId": "<layer_id>",
     "format": "png",
     "scale": 2
   }
   ```
2. **Execute Background Removal**:
   Run `remove-bg.py` on the exported image with `--tight` or `--adaptive-icon`.
3. **Inspect the Resulting Bounding Box**:
   The script outputs the exact non-zero bounding box and dimensions.
4. **Re-insert into FigCraft**:
   Create a new node or replace the layer fill with the transparent PNG path.

---

## 4. Integration with App Icon Craft (`figcraft-icon-craft`)

When designing launcher icons:
- Export the **`[Background]`** frame to `ic_launcher_background.png` (1024×1024 solid/gradient).
- Run `remove-bg.py --adaptive-icon` on the 3D emblem or symbol to produce `ic_launcher_foreground.png`.
- Run `generate_app_icons.py` from `figcraft-icon-craft` to slice the decoupled layers into Android density mipmaps (`mdpi` 108px up to `xxxhdpi` 432px) and iOS App Icon sets.

---

## 5. Prerequisites & Environment Setup

`remove-bg.py` automatically checks for and loads:
- **`pillow`** ($\ge 10.0.0$)
- **`rembg`** ($\ge 2.0.80$, uses BRIA RMBG 2.0 ONNX model)
- **`onnxruntime`** (CPU, DirectML, or CUDA acceleration)

Model weights (`bria-rmbg.onnx`) are automatically downloaded on first execution and cached permanently in `~/.rembg/models/bria-rmbg/`, requiring zero external API keys and executing entirely offline.
