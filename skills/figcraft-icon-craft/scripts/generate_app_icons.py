#!/usr/bin/env python3
"""
generate_app_icons.py
Automated Slicing & Resizing Pipeline for Android & iOS App Launcher Icons.
Part of the figcraft-icon-craft skill inside figcraft-studio.
"""

import sys
import os
import json
import argparse
from pathlib import Path

ANDROID_MIPMAPS = {
    "mipmap-mdpi": 108,
    "mipmap-hdpi": 162,
    "mipmap-xhdpi": 216,
    "mipmap-xxhdpi": 324,
    "mipmap-xxxhdpi": 432,
}

IOS_SIZES = [
    {"size": "20x20", "idiom": "iphone", "scale": "2x", "px": 40},
    {"size": "20x20", "idiom": "iphone", "scale": "3x", "px": 60},
    {"size": "29x29", "idiom": "iphone", "scale": "2x", "px": 58},
    {"size": "29x29", "idiom": "iphone", "scale": "3x", "px": 87},
    {"size": "40x40", "idiom": "iphone", "scale": "2x", "px": 80},
    {"size": "40x40", "idiom": "iphone", "scale": "3x", "px": 120},
    {"size": "60x60", "idiom": "iphone", "scale": "2x", "px": 120},
    {"size": "60x60", "idiom": "iphone", "scale": "3x", "px": 180},
    {"size": "20x20", "idiom": "ipad", "scale": "1x", "px": 20},
    {"size": "20x20", "idiom": "ipad", "scale": "2x", "px": 40},
    {"size": "29x29", "idiom": "ipad", "scale": "1x", "px": 29},
    {"size": "29x29", "idiom": "ipad", "scale": "2x", "px": 58},
    {"size": "40x40", "idiom": "ipad", "scale": "1x", "px": 40},
    {"size": "40x40", "idiom": "ipad", "scale": "2x", "px": 80},
    {"size": "76x76", "idiom": "ipad", "scale": "1x", "px": 76},
    {"size": "76x76", "idiom": "ipad", "scale": "2x", "px": 152},
    {"size": "83.5x83.5", "idiom": "ipad", "scale": "2x", "px": 167},
    {"size": "1024x1024", "idiom": "ios-marketing", "scale": "1x", "px": 1024},
]

def ensure_pillow():
    try:
        from PIL import Image
        return Image
    except ImportError:
        print("[!] Pillow is not installed. Please run: pip install pillow", file=sys.stderr)
        sys.exit(1)

def slice_android_adaptive(foreground_path, background_path, android_res_dir, Image):
    res_dir = Path(android_res_dir)
    res_dir.mkdir(parents=True, exist_ok=True)
    
    fg_img = Image.open(foreground_path).convert("RGBA") if foreground_path else None
    bg_img = Image.open(background_path).convert("RGBA") if background_path else None

    for folder, dim in ANDROID_MIPMAPS.items():
        target_dir = res_dir / folder
        target_dir.mkdir(parents=True, exist_ok=True)

        if bg_img:
            resized_bg = bg_img.resize((dim, dim), Image.Resampling.LANCZOS)
            resized_bg.save(target_dir / "ic_launcher_background.png", "PNG")
        
        if fg_img:
            resized_fg = fg_img.resize((dim, dim), Image.Resampling.LANCZOS)
            resized_fg.save(target_dir / "ic_launcher_foreground.png", "PNG")
            
    print(f"[✓] Android adaptive mipmaps generated successfully in: {res_dir}")

def slice_ios(master_path, ios_assets_dir, Image):
    assets_dir = Path(ios_assets_dir)
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    master_img = Image.open(master_path).convert("RGB")
    contents_images = []

    for item in IOS_SIZES:
        dim = item["px"]
        filename = f"Icon-App-{item['size']}@{item['scale']}.png"
        out_path = assets_dir / filename
        
        resized = master_img.resize((dim, dim), Image.Resampling.LANCZOS)
        resized.save(out_path, "PNG")
        
        contents_images.append({
            "size": item["size"],
            "idiom": item["idiom"],
            "filename": filename,
            "scale": item["scale"]
        })

    contents_json = {
        "images": contents_images,
        "info": {
            "version": 1,
            "author": "xcode"
        }
    }
    
    with open(assets_dir / "Contents.json", "w", encoding="utf-8") as f:
        json.dump(contents_json, f, indent=2)

    print(f"[✓] iOS AppIcon.appiconset generated successfully in: {assets_dir}")

def main():
    parser = argparse.ArgumentParser(description="Slice and generate Android & iOS app launcher icons from 1024x1024 master assets.")
    parser.add_argument("--master", help="Path to 1024x1024 master flattened icon (for iOS & stores)")
    parser.add_argument("--foreground", help="Path to 1024x1024 transparent foreground icon (for Android adaptive)")
    parser.add_argument("--background", help="Path to 1024x1024 background icon (for Android adaptive)")
    parser.add_argument("--android-res", help="Path to android/app/src/main/res directory")
    parser.add_argument("--ios-assets", help="Path to ios/Runner/Assets.xcassets/AppIcon.appiconset directory")

    args = parser.parse_args()
    Image = ensure_pillow()

    if args.android_res and (args.foreground or args.background):
        slice_android_adaptive(args.foreground, args.background, args.android_res, Image)
        
    if args.ios_assets and args.master:
        slice_ios(args.master, args.ios_assets, Image)

    if not args.android_res and not args.ios_assets:
        print("[!] No output directory specified. Use --android-res and/or --ios-assets.")

if __name__ == "__main__":
    main()

