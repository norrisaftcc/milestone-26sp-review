#!/usr/bin/env bash
# Build the binder: markdown sources in inputs/ -> .docx files in outputs/.
#
# Minimal pipeline per #10. Uses pandoc with the reference doc at
# inputs/design/binder-reference.docx if present (per the audit in
# #8 / PR #9), otherwise falls back to pandoc's defaults so the
# designer has something concrete to react to.
#
# Usage:
#   scripts/build_binder.sh           # build all binder sources
#   scripts/build_binder.sh --clean   # remove outputs/*.docx first
#
# Prerequisite: pandoc on PATH. Install on macOS via: brew install pandoc

set -eo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REFERENCE_DOC="$REPO_ROOT/inputs/design/binder-reference.docx"
OUT_DIR="$REPO_ROOT/outputs"

# Sources in binder order. Internal-only documents (`# Purpose of work.md`,
# `# PHILOSOPHICAL ISSUES.md`) are deliberately excluded — those are author
# scratchpads, not binder content per the project's own framing.
SOURCES=(
  "inputs/Spring_2026_Performance_Objectives.md"
  "inputs/raw_material/Objective_1_Cross-Departmental_Capstone_Collaboration_Framework.md"
  "inputs/raw_material/Objective_2_Source_Control_Version_Control_Instructional_Modules.md"
  "inputs/raw_material/Objective_3_Ghost_Student_Discovery_Tool.md"
  "inputs/raw_material/obj1_research_support.md"
  "inputs/raw_material/obj3_research_support.md"
)

if ! command -v pandoc >/dev/null 2>&1; then
  cat >&2 <<'EOM'
ERROR: 'pandoc' is not on PATH.

Install on macOS:
    brew install pandoc

Install on Ubuntu/Debian:
    sudo apt install pandoc

Then re-run: scripts/build_binder.sh
EOM
  exit 1
fi

if [ "${1:-}" = "--clean" ]; then
  echo "Cleaning $OUT_DIR/*.docx"
  rm -f "$OUT_DIR"/*.docx
fi

mkdir -p "$OUT_DIR"

PANDOC_ARGS=()
if [ -f "$REFERENCE_DOC" ]; then
  PANDOC_ARGS+=(--reference-doc="$REFERENCE_DOC")
  echo "Using reference doc: $REFERENCE_DOC"
else
  echo "No reference doc at $REFERENCE_DOC — using pandoc defaults."
  echo "  (The audit in PR #9 recommends building a reference.docx once the"
  echo "   designer settles on fonts. This script will pick it up automatically"
  echo "   the moment it lands at that path.)"
fi

echo
echo "Building binder -> $OUT_DIR"
echo "------------------------------------------------------------"

built=0
missing=0
for src in "${SOURCES[@]}"; do
  src_path="$REPO_ROOT/$src"
  if [ ! -f "$src_path" ]; then
    echo "  SKIP  $src (not found)"
    missing=$((missing + 1))
    continue
  fi
  base="$(basename "$src" .md)"
  dst="$OUT_DIR/${base}.docx"
  printf "  ->    %s\n" "$dst"
  pandoc "$src_path" "${PANDOC_ARGS[@]}" -o "$dst"
  built=$((built + 1))
done

echo "------------------------------------------------------------"
echo "Built $built file(s); skipped $missing missing source(s)."
echo "Review the .docx files in $OUT_DIR/."

# Exit non-zero if any source from the allowlist was missing — silent
# partial builds would hand the designer or author an incomplete review
# set without anyone noticing.
[ "$missing" -eq 0 ]
