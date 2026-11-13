#!/usr/bin/env python3
"""
remove_bg.py
Industrial-Grade AI Background Removal & Asset Preparation CLI.
Powered by BRIA RMBG 2.0 via rembg & ONNX Runtime.

Part of the `figcraft-remove-bg` skill inside FigCraft Design Studio.

Features:
- State-of-the-art neural background removal (BRIA RMBG 2.0)
- Ghost noise elimination (removes faint alpha fringe < 10)
- Tight bounding-box cropping
- Android Adaptive Icon safe-zone centering (1024x1024 canvas, Safe Area phi 626px)
- Pre-crop bounding box support (isolates subject inside complex cards/squircles)
- Alpha mask matte export
- Single file or batch directory processing
"""

import sys
import math
import argparse
from pathlib import Path

def ensure_dependencies():
    missing = []
    try:
        import PIL
        from PIL import Image
    except ImportError:
        missing.append("pillow")
    
    try:
        import rembg
    except ImportError:
        missing.append("rembg")
        
    try:
        import onnxruntime
    except ImportError:
        missing.append("onnxruntime")
        
    if missing:
        print(f"[!] Missing required Python dependencies: {', '.join(missing)}", file=sys.stderr)
        print(f"    Please install via: pip install {' '.join(missing)}", file=sys.stderr)
        sys.exit(1)

def process_image(
    input_path: Path,
    output_path: Path,
    clean_alpha: bool = True,
    alpha_threshold: int = 10,
    crop_tight: bool = False,
    adaptive_icon: bool = False,
    crop_box: tuple = None,
    target_size: int = 480,
    mask_only: bool = False,
    verbose: bool = True
):
    from PIL import Image
    import rembg

    if verbose:
        print(f"[*] Processing: {input_path.name}")

    img = Image.open(input_path).convert("RGBA")

    # Optional pre-crop to focus on region of interest
    if crop_box:
        if verbose:
            print(f"    Pre-cropping region: {crop_box}")
        img = img.crop(crop_box)

    # Neural background removal
    if verbose:
        print("    Running neural background removal (BRIA RMBG 2.0)...")
    extracted = rembg.remove(img)

    # Clean ghost alpha noise
    if clean_alpha:
        clean_img = Image.new("RGBA", extracted.size, (0, 0, 0, 0))
        for y in range(extracted.height):
            for x in range(extracted.width):
                r, g, b, a = extracted.getpixel((x, y))
                if a >= alpha_threshold:
                    clean_img.putpixel((x, y), (r, g, b, a))
        extracted = clean_img

    # Alpha mask matte mode
    if mask_only:
        alpha_channel = extracted.split()[3]
        output_path.parent.mkdir(parents=True, exist_ok=True)
        alpha_channel.save(output_path, "PNG")
        if verbose:
            print(f"[✓] Saved alpha mask matte: {output_path}")
        return output_path

    # Tight crop
    bbox = extracted.getbbox()
    if not bbox:
        print(f"[!] Warning: Entire image was identified as background for {input_path.name}", file=sys.stderr)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        extracted.save(output_path, "PNG")
        return output_path

    tight = extracted.crop(bbox)
    tw, th = tight.size
    if verbose:
        print(f"    Extracted subject bbox: {bbox} ({tw}x{th} px)")

    # Android Adaptive Icon Mode
    if adaptive_icon:
        dim = 1024
        # Scale subject to target size while preserving aspect ratio
        scaled_w = target_size
        scaled_h = int(scaled_w * (th / tw))
        scaled = tight.resize((scaled_w, scaled_h), Image.Resampling.LANCZOS)

        canvas = Image.new("RGBA", (dim, dim), (0, 0, 0, 0))
        fx = (dim - scaled_w) // 2
        fy = (dim - scaled_h) // 2
        canvas.paste(scaled, (fx, fy), scaled)

        # Verify safe area adherence
        max_dist = 0
        for y in range(dim):
            for x in range(dim):
                if canvas.getpixel((x, y))[3] > 0:
                    d = math.hypot(x - 512, y - 512)
                    if d > max_dist:
                        max_dist = d

        final_img = canvas
        if verbose:
            print(f"    [✓] Centered on 1024x1024 canvas for Android Adaptive Icon.")
            print(f"    [✓] Max radius from center: {max_dist:.1f}px (Safe Area limit = 313px, margin = {313 - max_dist:.1f}px)")
    elif crop_tight:
        final_img = tight
    else:
        final_img = extracted

    output_path.parent.mkdir(parents=True, exist_ok=True)
    final_img.save(output_path, "PNG")
    if verbose:
        print(f"[✓] Successfully exported: {output_path} ({final_img.size[0]}x{final_img.size[1]} px)")

    return output_path

def main():
    parser = argparse.ArgumentParser(
        description="Studio-Grade AI Background Removal via BRIA RMBG 2.0 (FigCraft Studio Skill)"
    )
    parser.add_argument("input", help="Path to input image or directory")
    parser.add_argument("-o", "--output", help="Output image or directory path")
    parser.add_argument("--tight", action="store_true", help="Crop tightly to subject bounding box")
    parser.add_argument("--adaptive-icon", action="store_true", help="Scale and center within Android Adaptive 1024x1024 safe area (phi 626px)")
    parser.add_argument("--target-size", type=int, default=480, help="Subject dimension inside adaptive icon (default: 480)")
    parser.add_argument("--crop-box", nargs=4, type=int, metavar=("X0", "Y0", "X1", "Y1"), help="Pre-crop box coordinates before AI processing")
    parser.add_argument("--no-clean-alpha", action="store_true", help="Disable ghost alpha thresholding")
    parser.add_argument("--alpha-thresh", type=int, default=10, help="Alpha threshold to strip ghost noise (default: 10)")
    parser.add_argument("--mask-only", action="store_true", help="Export black & white alpha mask matte instead of transparent RGBA")
    parser.add_argument("-q", "--quiet", action="store_true", help="Suppress progress logs")

    args = parser.parse_args()
    ensure_dependencies()

    input_path = Path(args.input).resolve()
    if not input_path.exists():
        print(f"[!] Input path not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    crop_box = tuple(args.crop_box) if args.crop_box else None

    if input_path.is_file():
        if args.output:
            output_path = Path(args.output).resolve()
        else:
            suffix = "_fg.png" if args.adaptive_icon else "_transparent.png"
            output_path = input_path.parent / f"{input_path.stem}{suffix}"

        process_image(
            input_path=input_path,
            output_path=output_path,
            clean_alpha=not args.no_clean_alpha,
            alpha_threshold=args.alpha_thresh,
            crop_tight=args.tight,
            adaptive_icon=args.adaptive_icon,
            crop_box=crop_box,
            target_size=args.target_size,
            mask_only=args.mask_only,
            verbose=not args.quiet
        )
    elif input_path.is_dir():
        out_dir = Path(args.output).resolve() if args.output else input_path / "transparent_outputs"
        extensions = {".png", ".jpg", ".jpeg", ".webp"}
        files = [f for f in input_path.iterdir() if f.is_file() and f.suffix.lower() in extensions]

        if not files:
            print(f"[!] No valid images found in: {input_path}", file=sys.stderr)
            sys.exit(0)

        print(f"[*] Processing {len(files)} images in directory: {input_path}")
        for f in files:
            suffix = "_fg.png" if args.adaptive_icon else "_transparent.png"
            dest = out_dir / f"{f.stem}{suffix}"
            process_image(
                input_path=f,
                output_path=dest,
                clean_alpha=not args.no_clean_alpha,
                alpha_threshold=args.alpha_thresh,
                crop_tight=args.tight,
                adaptive_icon=args.adaptive_icon,
                crop_box=crop_box,
                target_size=args.target_size,
                mask_only=args.mask_only,
                verbose=not args.quiet
            )
        print(f"[✓] Finished batch processing into: {out_dir}")

if __name__ == "__main__":
    main()
