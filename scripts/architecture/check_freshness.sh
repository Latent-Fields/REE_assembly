#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
cd "${REPO_ROOT}"

BASE_REF="${1:-}"
HEAD_REF="${2:-}"

if [[ -z "${BASE_REF}" || -z "${HEAD_REF}" ]]; then
  if git rev-parse --verify HEAD~1 >/dev/null 2>&1; then
    BASE_REF="HEAD~1"
    HEAD_REF="HEAD"
  else
    echo "Freshness check skipped: not enough history to diff." >&2
    exit 0
  fi
fi

changed_file_list="$(git diff --name-only "${BASE_REF}" "${HEAD_REF}" || true)"
if [[ -z "${changed_file_list}" ]]; then
  echo "Freshness check passed: no changed files in diff range."
  exit 0
fi

tmpdir="$(mktemp -d)"
trap 'rm -rf "${tmpdir}"' EXIT
printf "%s\n" "${changed_file_list}" > "${tmpdir}/changed.txt"

# Architecture source files that should trigger a diagram review.
grep -E '^docs/architecture/.*\.md$|^docs/(REE_ARCHITECTURE_SNAPSHOT_.*\.md|invariants\.md|glossary\.md|REE_MIN_SPEC\.md|claims/(claims\.yaml|claim_index\.md))$' \
  "${tmpdir}/changed.txt" \
  | grep -Ev '^docs/architecture/(diagram_views\.md|streams\.md)$' \
  > "${tmpdir}/source_changed.txt" || true

# Files that count as explicit triple-view diagram maintenance.
grep -E '^docs/architecture/(architecture_static\.mmd|architecture_typed_dataflow\.mmd|episode_sequence\.mmd|streams\.md|stream_routing\.v1\.yaml|diagram_views\.md|architecture_static\.svg|architecture_typed_dataflow\.svg|episode_sequence\.svg)$' \
  "${tmpdir}/changed.txt" \
  > "${tmpdir}/diagram_changed.txt" || true

if [[ -s "${tmpdir}/source_changed.txt" && ! -s "${tmpdir}/diagram_changed.txt" ]]; then
  echo "Architecture freshness check failed." >&2
  echo "Source architecture files changed, but no triple-view diagram files changed." >&2
  echo >&2
  echo "Changed source files:" >&2
  sed 's/^/  - /' "${tmpdir}/source_changed.txt" >&2
  echo >&2
  echo "Update at least one of:" >&2
  echo "  - docs/architecture/architecture_static.mmd" >&2
  echo "  - docs/architecture/architecture_typed_dataflow.mmd" >&2
  echo "  - docs/architecture/episode_sequence.mmd" >&2
  echo "  - docs/architecture/stream_routing.v1.yaml" >&2
  echo "  - docs/architecture/streams.md" >&2
  exit 1
fi

echo "Architecture freshness check passed."
