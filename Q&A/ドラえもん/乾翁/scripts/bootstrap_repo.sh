#!/usr/bin/env bash
# =====================================================================
# scripts/bootstrap_repo.sh
# Shikiben (識扁) V2.6.0 Repository Bootstrap, Sanitizer & Verifier
# =====================================================================
set -euo pipefail

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

INIT_ONLY=false
AUTO_COMMIT=false

for arg in "$@"; do
  case "$arg" in
    --init-only) INIT_ONLY=true ;;
    --commit)    AUTO_COMMIT=true ;;
    -h|--help)
      echo "Usage: ./scripts/bootstrap_repo.sh [--init-only] [--commit]"
      echo "  --init-only : ディレクトリ階層と .gitignore のみ生成して終了します"
      echo "  --commit    : サニタイズ・全検分パス後に匿名署名で初回コミットを実行します"
      exit 0
      ;;
  esac
done

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# 【照会3対応】HuggingFace / PyTorch キャッシュをリポジトリ直下の .cache/ に強制局所化
export HF_HOME="${REPO_ROOT}/.cache/huggingface"
export TORCH_HOME="${REPO_ROOT}/.cache/torch"
export MPLBACKEND="Agg"

echo -e "${BLUE}======================================================================${NC}"
echo -e "${BLUE} Shikiben (識扁) V2.6.0 - Bootstrap, Sanitizer & Security Verifier${NC}"
echo -e "${BLUE}======================================================================${NC}"

# ---------------------------------------------------------------------
# 1. ディレクトリ構造と局所キャッシュフォルダの初期化
# ---------------------------------------------------------------------
echo -e "\n${BLUE}[1/6] ディレクトリ階層および局所キャッシュ領域を初期化しています...${NC}"

DIRS=(
  ".github/workflows"
  ".cache/huggingface"
  ".cache/torch"
  "docs"
  "schemas/v2.6"
  "src"
  "sidecar"
  "simulations/archive_v25"
  "simulations/v26_canonical"
  "tests"
  "scripts"
)

for d in "${DIRS[@]}"; do
  mkdir -p "$d"
done
echo -e "  ${GREEN}[OK]${NC} 全ディレクトリおよび .cache/ 局所化領域を確保しました。"

# ---------------------------------------------------------------------
# 2. .gitignore の確定生成
# ---------------------------------------------------------------------
cat << 'EOF' > .gitignore
# Python bytecode & tool caches
__pycache__/
*.py[cod]
*$py.class
*.egg-info/
build/
dist/
.pytest_cache/
.ruff_cache/

# Virtual environments
.venv/
venv/
env/

# Localized HuggingFace / PyTorch model caches (never commit)
.cache/
models/

# OS & Editor artifacts
.DS_Store
Thumbs.db
.vscode/
.idea/

# Runtime logs & local env
*.log
.env
EOF
echo -e "  ${GREEN}[OK]${NC} .gitignore (.cache/ 除外設定済) を確定しました。"

if [ "$INIT_ONLY" = true ]; then
  echo -e "\n${GREEN}[✔] 初期化完了。各ファイルを配置した後に ./scripts/bootstrap_repo.sh を実行してください。${NC}"
  exit 0
fi

# ---------------------------------------------------------------------
# 3. 【照会2対応】Markdown転記汚染（U+00A0 等の不可視文字・改行）の機械的サニタイズ
# ---------------------------------------------------------------------
echo -e "\n${BLUE}[2/6] Markdown転記に伴う不可視空白・改行コードの機械的サニタイズを実行中...${NC}"

python3 - << 'EOF'
import pathlib

target_exts = {".py", ".yml", ".yaml", ".json", ".toml", ".md", ".sh", ".txt"}
sanitized_count = 0

for path in pathlib.Path(".").rglob("*"):
    if not path.is_file():
        continue
    if any(part in {".git", ".venv", "venv", ".cache", "__pycache__"} for part in path.parts):
        continue
    if path.suffix in target_exts or path.name.startswith("Dockerfile"):
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            continue
        # U+00A0 (NBSP), U+200B (ゼロ幅空白), U+FEFF (BOM), CRLF を純粋な ASCII 空白・LF へ正規化
        cleaned = (
            text.replace("\u00a0", " ")
                .replace("\u200b", "")
                .replace("\ufeff", "")
                .replace("\r\n", "\n")
        )
        if cleaned != text:
            path.write_text(cleaned, encoding="utf-8")
            sanitized_count += 1
            print(f"  [SANITIZED] 不可視文字を除去・正規化しました: {path}")

print(f"  [SUMMARY] サニタイズ完了 (修復ファイル数: {sanitized_count})")
EOF

# ---------------------------------------------------------------------
# 4. 必須ファイル群の配置チェック
# ---------------------------------------------------------------------
echo -e "\n${BLUE}[3/6] V2.6.0 必須ファイル群の配置状況を検分しています...${NC}"

REQUIRED_FILES=(
  "README.md"
  "pyproject.toml"
  "requirements.txt"
  ".github/workflows/ci.yml"
  "docs/SPECIFICATION_V2.6.md"
  "schemas/v2.6/crisis_spike.json"
  "schemas/v2.6/attractor_spike.json"
  "src/shikiben_trm_v26.py"
  "sidecar/trm_proxy.py"
  "sidecar/hardware_harvester_v2.py"
  "sidecar/Dockerfile.sidecar"
  "sidecar/docker-compose.yml"
  "sidecar/README.md"
  "simulations/v26_canonical/07_internal_dynamics_superconducting_final.py"
  "simulations/v26_canonical/08_viscoelastic_sensitivity_analysis.py"
  "simulations/v26_canonical/09_full_stack_shikiben_v26.py"
  "simulations/v26_canonical/10_breathing_anchor_full_stack_v26.py"
  "simulations/v26_canonical/11_human_meta_damping_v26.py"
  "tests/test_trm_v26_benchmark.py"
  "tests/test_sidecar_proxy.py"
)

MISSING_COUNT=0
for f in "${REQUIRED_FILES[@]}"; do
  if [ -s "$f" ]; then
    echo -e "  ${GREEN}[OK]${NC}      $f"
  else
    echo -e "  ${RED}[MISSING]${NC} $f"
    MISSING_COUNT=$((MISSING_COUNT + 1))
  fi
done

if [ "$MISSING_COUNT" -gt 0 ]; then
  echo -e "\n${YELLOW}[!] 未配置の必須ファイルが ${MISSING_COUNT} 件あります。配置後に再実行してください。${NC}"
  exit 1
fi

# ---------------------------------------------------------------------
# 5. Ruff 自動整形・構文検分・JSON検証・Pytest (全14項目) の実行
# ---------------------------------------------------------------------
echo -e "\n${BLUE}[4/6] 構文解析 (Ruff / AST) および JSON-LD スキーマ検証を実行中...${NC}"

if command -v ruff >/dev/null 2>&1; then
  ruff check --fix src sidecar simulations/v26_canonical tests
  ruff format src sidecar simulations/v26_canonical tests
  echo -e "  ${GREEN}[RUFF-OK]${NC} Ruff による静的解析とコードフォーマットが完了しました。"
fi

python3 -c "
import json, pathlib
for p in ['schemas/v2.6/crisis_spike.json', 'schemas/v2.6/attractor_spike.json']:
    data = json.loads(pathlib.Path(p).read_text(encoding='utf-8'))
    assert data['\$schema'].endswith('2020-12/schema')
    assert len(data['examples']) >= 1
    print(f'  [JSON-OK] {p}')
"

python3 -m py_compile \
  src/shikiben_trm_v26.py \
  sidecar/trm_proxy.py \
  sidecar/hardware_harvester_v2.py \
  simulations/v26_canonical/*.py \
  tests/test_trm_v26_benchmark.py \
  tests/test_sidecar_proxy.py
echo -e "  ${GREEN}[AST-OK]${NC} 全 Python ファイルのバイトコードコンパイルに成功しました。"

echo -e "\n${BLUE}[5/6] 自動回帰テストスイート (pytest 全14項目) を実行しています...${NC}"
if python3 -c "import pytest, aiohttp, numpy" >/dev/null 2>&1; then
  python3 -m pytest
else
  echo -e "  ${YELLOW}[WARN] pytest または aiohttp が未導入です: pip install -e '.[dev]' を実行してください。${NC}"
fi

# ---------------------------------------------------------------------
# 6. 【照会1対応】身元隠蔽Git署名設定とプライバシー走査つきコミット
# ---------------------------------------------------------------------
echo -e "\n${BLUE}[6/6] Git 匿名署名設定と身元隠蔽チェックを実行しています...${NC}"

if [ ! -d ".git" ]; then
  git init -b main
fi

# リポジトリローカルのコミッター情報を「tsunenonaniarazu / 非常名」へ強制固定
git config --local user.name "tsunenonaniarazu / 非常名"
git config --local user.email "noreply@chihen.net"
echo -e "  ${GREEN}[IDENTITY]${NC} Git Author 固定完了: $(git config --local user.name) ($(git config --local user.email))"

# 個人環境パス (/Users/xxx や /home/xxx) の混入チェック
if grep -rnE "(/Users/[a-zA-Z0-9_-]+|/home/[a-zA-Z0-9_-]+)" README.md pyproject.toml docs/ src/ sidecar/ simulations/ tests/ 2>/dev/null; then
  echo -e "  ${RED}[SECURITY VETO] ローカル環境の個人ディレクトリパスが検出されました。上記該当箇所を修正してください。${NC}"
  exit 1
else
  echo -e "  ${GREEN}[PRIVACY-OK]${NC} ローカル個人パスの混入なし（クリーン状態）。"
fi

if [ "$AUTO_COMMIT" = true ]; then
  git add .
  if git diff --cached --quiet; then
    echo -e "  ${YELLOW}[GIT] コミットすべき差分はありません。${NC}"
  else
    GIT_AUTHOR_NAME="tsunenonaniarazu / 非常名" \
    GIT_AUTHOR_EMAIL="noreply@chihen.net" \
    GIT_COMMITTER_NAME="tsunenonaniarazu / 非常名" \
    GIT_COMMITTER_EMAIL="noreply@chihen.net" \
    git commit -m "feat(v2.6.0): anchor Shikiben V2.6.0 specification, TRM-EcoGuard sidecar, and canonical test suite"
    echo -e "  ${GREEN}[✔] 匿名署名による確定コミットが完了しました。${NC}"
  fi
else
  echo -e "  ${GREEN}[READY]${NC} 全4点の照会対策および検分が完了しました。コミットするには以下を実行してください："
  echo -e "          ${YELLOW}./scripts/bootstrap_repo.sh --commit${NC}"
fi

echo -e "${BLUE}======================================================================${NC}"
