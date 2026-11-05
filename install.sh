#!/usr/bin/env bash
# ==============================================================================
#  🎨 FigCraft-Studio Universal Installer (macOS, Linux, WSL, Git Bash)
#  Repository: https://github.com/donihadimas/figcraft-studio
# ==============================================================================

set -e

REPO_URL="https://github.com/donihadimas/figcraft-studio.git"

CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
GRAY='\033[0;90m'
NC='\033[0m'

clear 2>/dev/null || true
echo -e "${CYAN}============================================================${NC}"
echo -e "${CYAN}        🎨 FigCraft-Studio Universal Installer              ${NC}"
echo -e "${CYAN}============================================================${NC}"
echo -e "${GRAY}Industrial UI/UX Design Engineering & FigCraft MCP Suite.\n${NC}"

if ! command -v git >/dev/null 2>&1; then
    echo -e "${RED}❌ Error: Git tidak ditemukan.${NC}"
    exit 1
fi

SCOPE="${1:-}"
if [ -z "$SCOPE" ]; then
    echo -e "${YELLOW}Pilih mode instalasi:\n${NC}"
    echo -e "  [1] Global Installation (~/.gemini/config/plugins/figcraft-studio)"
    echo -e "  [2] Project-Scoped Installation (.agents/plugins/figcraft-studio)\n"
    read -p "Masukkan pilihan [1 atau 2] (Default: 1): " INPUT_CHOICE
    if [ "$INPUT_CHOICE" = "2" ]; then SCOPE="project"; else SCOPE="global"; fi
fi

if [ "$SCOPE" = "project" ]; then
    TARGET_DIR="$(pwd)/.agents/plugins/figcraft-studio"
else
    TARGET_DIR="$HOME/.gemini/config/plugins/figcraft-studio"
fi

mkdir -p "$(dirname "$TARGET_DIR")"

if [ -d "$TARGET_DIR/.git" ]; then
    echo -e "\n${YELLOW}🔄 Memperbarui figcraft-studio (git pull)...${NC}"
    git -C "$TARGET_DIR" pull --rebase || true
    echo -e "${GREEN}✅ Berhasil diperbarui!${NC}"
elif [ ! -d "$TARGET_DIR" ]; then
    echo -e "\n${YELLOW}⬇️ Mengunduh figcraft-studio dari GitHub...${NC}"
    git clone "$REPO_URL" "$TARGET_DIR"
    echo -e "${GREEN}✅ Berhasil di-clone ke: $TARGET_DIR${NC}"
fi

chmod +x "$TARGET_DIR/scripts/ensure-figcraft.sh" 2>/dev/null || true

echo -e "\n${GREEN}============================================================${NC}"
echo -e "${GREEN} 🎉 FigCraft-Studio Berhasil Terpasang!${NC}"
echo -e "${GREEN}============================================================${NC}"
echo -e "Silakan Restart / Reload Window Antigravity Anda."
echo -e "${GRAY}Dokumentasi: https://github.com/donihadimas/figcraft-studio${NC}\n"
