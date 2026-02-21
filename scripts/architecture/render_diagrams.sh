#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
DOCS_DIR="${REPO_ROOT}/docs/architecture"

if ! command -v mmdc >/dev/null 2>&1; then
  echo "mmdc (Mermaid CLI) is required. Install with: npm install -g @mermaid-js/mermaid-cli" >&2
  exit 1
fi

"${SCRIPT_DIR}/check_consistency.sh"

mmdc -i "${DOCS_DIR}/architecture_static.mmd" -o "${DOCS_DIR}/architecture_static.svg"
mmdc -i "${DOCS_DIR}/architecture_typed_dataflow.mmd" -o "${DOCS_DIR}/architecture_typed_dataflow.svg"
mmdc -i "${DOCS_DIR}/episode_sequence.mmd" -o "${DOCS_DIR}/episode_sequence.svg"

echo "Rendered architecture SVGs in ${DOCS_DIR}."
