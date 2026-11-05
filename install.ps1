# ==============================================================================
#  🎨 FigCraft-Studio Universal Installer (Windows PowerShell)
#  Repository: https://github.com/donihadimas/figcraft-studio
# ==============================================================================

[CmdletBinding()]
param (
    [ValidateSet("global", "project", "")]
    [string]$Scope = "",
    [switch]$NonInteractive
)

$ErrorActionPreference = "Stop"
$RepoUrl = "https://github.com/donihadimas/figcraft-studio.git"

Clear-Host
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "        🎨 FigCraft-Studio Universal Installer              " -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Industrial UI/UX Design Engineering & FigCraft MCP Suite.`n" -ForegroundColor Gray

# 1. Check prerequisites
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Error: Git tidak ditemukan di komputer ini." -ForegroundColor Red
    Write-Host "Silakan install Git terlebih dahulu: winget install Git.Git`n" -ForegroundColor Yellow
    exit 1
}

# 2. Select Installation Scope
$choice = $Scope
if (-not $choice) {
    if ($NonInteractive) {
        $choice = "global"
    } else {
        Write-Host "Pilih mode instalasi yang Anda inginkan:`n" -ForegroundColor Yellow
        Write-Host "  [1] Global Installation (Rekomendasi)" -ForegroundColor White
        Write-Host "      -> Dipasang di: $HOME\.gemini\config\plugins\figcraft-studio" -ForegroundColor Gray
        Write-Host "      -> Otomatis aktif di SEMUA project di komputer ini.`n" -ForegroundColor Gray
        
        Write-Host "  [2] Project-Scoped Installation" -ForegroundColor White
        Write-Host "      -> Dipasang di: .agents\plugins\figcraft-studio" -ForegroundColor Gray
        Write-Host "      -> Hanya aktif di folder project saat ini (bisa di-commit ke Git tim).`n" -ForegroundColor Gray

        $inputChoice = Read-Host "Masukkan pilihan [1 atau 2] (Default: 1)"
        if ($inputChoice -eq "2") { $choice = "project" } else { $choice = "global" }
    }
}

# 3. Determine target directory
if ($choice -eq "project") {
    $targetDir = Join-Path (Get-Location) ".agents\plugins\figcraft-studio"
    Write-Host "`n📦 Memilih instalasi: Project-Scoped" -ForegroundColor Cyan
} else {
    $targetDir = Join-Path $HOME ".gemini\config\plugins\figcraft-studio"
    Write-Host "`n📦 Memilih instalasi: Global" -ForegroundColor Cyan
}

Write-Host "📁 Target direktori: $targetDir" -ForegroundColor Gray

# 4. Clone or update repository
$parentDir = Split-Path -Parent $targetDir
if (-not (Test-Path $parentDir)) {
    New-Item -ItemType Directory -Path $parentDir -Force | Out-Null
}

if (Test-Path "$targetDir\.git") {
    Write-Host "`n🔄 Plugin sudah terpasang. Mengambil pembaruan terbaru (git pull)..." -ForegroundColor Yellow
    try {
        git -C $targetDir pull --rebase 2>&1 | Out-Null
        Write-Host "✅ Berhasil diperbarui ke versi terbaru!" -ForegroundColor Green
    } catch {
        Write-Host "⚠️ Tidak dapat melakukan git pull, menggunakan versi lokal saat ini." -ForegroundColor DarkYellow
    }
} elseif (-not (Test-Path $targetDir)) {
    Write-Host "`n⬇️ Mengunduh figcraft-studio dari GitHub..." -ForegroundColor Yellow
    git clone $RepoUrl $targetDir
    Write-Host "✅ Berhasil di-clone ke: $targetDir" -ForegroundColor Green
}

# 5. Check & Configure FigCraft MCP in ~/.gemini/config/mcp_config.json
$mcpConfigPath = Join-Path $HOME ".gemini\config\mcp_config.json"
$figcraftCli = "$env:ProgramFiles\FigCraft\figcraft-cli.exe"
if (-not (Test-Path $figcraftCli)) {
    $cmd = Get-Command figcraft-cli -ErrorAction SilentlyContinue
    if ($cmd) { $figcraftCli = $cmd.Source }
}

if (Test-Path $mcpConfigPath) {
    try {
        $mcpJson = Get-Content $mcpConfigPath -Raw | ConvertFrom-Json
        if (-not $mcpJson.mcpServers) {
            $mcpJson | Add-Member -MemberType NoteProperty -Name "mcpServers" -Value ([pscustomobject]@{})
        }
        if (-not $mcpJson.mcpServers.PSObject.Properties["figcraft"]) {
            $mcpJson.mcpServers | Add-Member -MemberType NoteProperty -Name "figcraft" -Value ([pscustomobject]@{
                command = $figcraftCli
                args = @("mcp", "--attach", "7979")
            })
            $mcpJson | ConvertTo-Json -Depth 10 | Set-Content $mcpConfigPath -Encoding UTF8
            Write-Host "✅ MCP server 'figcraft' (--attach 7979) ditambahkan ke mcp_config.json" -ForegroundColor Green
        } else {
            Write-Host "✅ MCP server 'figcraft' sudah terdaftar di mcp_config.json" -ForegroundColor Green
        }
    } catch {
        Write-Host "⚠️ Gagal memperbarui mcp_config.json secara otomatis: $_" -ForegroundColor DarkYellow
    }
}

# 6. Check Python 3 for ui-ux-pro-max
if (Get-Command python -ErrorAction SilentlyContinue) {
    Write-Host "✅ Python terdeteksi untuk mesin pencari ui-ux-pro-max" -ForegroundColor Green
} else {
    Write-Host "⚠️ Python 3 belum terdeteksi di PATH (dibutuhkan oleh search.py di ui-ux-pro-max)." -ForegroundColor Yellow
}

Write-Host "`n============================================================" -ForegroundColor Green
Write-Host " 🎉 FigCraft-Studio Berhasil Terpasang!" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host "Silakan Restart / Reload Window Antigravity Anda." -ForegroundColor White
Write-Host "Dokumentasi: https://github.com/donihadimas/figcraft-studio" -ForegroundColor Gray
Write-Host "============================================================`n" -ForegroundColor Green
