# Keylines & Grid Specifications for App Icons & Logos

Comprehensive mathematical dimensions and pixel reference tables for Android, iOS, Web Favicons, and In-App SVG icons.

---

## 1. Android Adaptive Icon Resolution Matrix

Android Adaptive Icons require two distinct layers:
- `ic_launcher_background.png`
- `ic_launcher_foreground.png` (transparent background)

| Density Bucket | Scale Factor | Canvas Size (108dp) | OEM Mask (72dp) | Safe Zone ($\varnothing$ 66dp) | Output Folder |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **mdpi** | 1.0x | 108 × 108 px | 72 × 72 px | $\varnothing$ 66 px | `res/mipmap-mdpi/` |
| **hdpi** | 1.5x | 162 × 162 px | 108 × 108 px | $\varnothing$ 99 px | `res/mipmap-hdpi/` |
| **xhdpi** | 2.0x | 216 × 216 px | 144 × 144 px | $\varnothing$ 132 px | `res/mipmap-xhdpi/` |
| **xxhdpi** | 3.0x | 324 × 324 px | 216 × 216 px | $\varnothing$ 198 px | `res/mipmap-xxhdpi/` |
| **xxxhdpi** | 4.0x | 432 × 432 px | 288 × 288 px | $\varnothing$ 264 px | `res/mipmap-xxxhdpi/` |
| **Play Store Master** | ~9.48x | **1024 × 1024 px** | 682 × 682 px | $\varnothing$ **626 px** | Google Play Console (512x512) |

---

## 2. Apple iOS App Icon Dimensions (`AppIcon.appiconset`)

Apple iOS requires single flattened raster images without transparency.

| Target Platform / Device | Idiom | Size (Points) | Scale | Target Pixel Dimensions | Filename |
| :--- | :--- | :--- | :--- | :--- | :--- |
| iPhone Notification | iphone | 20 × 20 pt | 2x, 3x | 40 × 40 px, 60 × 60 px | `Icon-App-20x20@2x.png` |
| iPhone Settings | iphone | 29 × 29 pt | 2x, 3x | 58 × 58 px, 87 × 87 px | `Icon-App-29x29@2x.png` |
| iPhone Spotlight | iphone | 40 × 40 pt | 2x, 3x | 80 × 80 px, 120 × 120 px | `Icon-App-40x40@2x.png` |
| iPhone App (Home) | iphone | 60 × 60 pt | 2x, 3x | 120 × 120 px, 180 × 180 px | `Icon-App-60x60@2x.png` |
| iPad App (Home) | ipad | 76 × 76 pt | 2x | 152 × 152 px | `Icon-App-76x76@2x.png` |
| iPad Pro App | ipad | 83.5 × 83.5 pt| 2x | 167 × 167 px | `Icon-App-83.5x83.5@2x.png` |
| **App Store Master** | ios-marketing | 1024 × 1024 pt | 1x | **1024 × 1024 px** | `Icon-App-1024x1024@1x.png` |

---

## 3. Web & Favicon Standards

| Asset Type | Dimensions | Format | Usage |
| :--- | :--- | :--- | :--- |
| Favicon Small | 16 × 16 px | `.png`, `.ico` | Browser tab bar |
| Favicon Standard | 32 × 32 px | `.png`, `.ico` | High-DPI browser tabs |
| Apple Touch Icon | 180 × 180 px | `.png` | iOS Safari Home Screen bookmark |
| PWA Manifest Icon | 192 × 192 px | `.png` | Android Chrome install prompt |
| PWA Splash/Store | 512 × 512 px | `.png` | PWA splash screen & Windows store |
| Vector Icon | Vector | `.svg` | Modern browser scalable favicon |

---

## 4. In-App Vector Icons (24×24dp Standard)

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <!-- Active live drawing area: (x: 2 to 22, y: 2 to 22) -->
  <!-- 2px perimeter safety margin -->
</svg>
```

