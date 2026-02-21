#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

DOCS_DIR="${REPO_ROOT}/docs/architecture"
STATIC_MMD="${DOCS_DIR}/architecture_static.mmd"
TYPED_MMD="${DOCS_DIR}/architecture_typed_dataflow.mmd"
SEQUENCE_MMD="${DOCS_DIR}/episode_sequence.mmd"
STREAMS_MD="${DOCS_DIR}/streams.md"
ROUTING_YAML="${DOCS_DIR}/stream_routing.v1.yaml"

for f in \
  "${STATIC_MMD}" \
  "${TYPED_MMD}" \
  "${SEQUENCE_MMD}" \
  "${STREAMS_MD}" \
  "${ROUTING_YAML}"
do
  if [[ ! -f "${f}" ]]; then
    echo "Missing required file: ${f}" >&2
    exit 1
  fi
done

tmpdir="$(mktemp -d)"
trap 'rm -rf "${tmpdir}"' EXIT

sort_unique() {
  sort -u "$1" > "$2"
}

set_diff() {
  local left="$1"
  local right="$2"
  local out="$3"
  comm -23 "${left}" "${right}" > "${out}"
}

extract_yaml_components() {
  awk '
    /^components:/ { in_components=1; next }
    /^edges:/ { in_components=0 }
    in_components && /^  - / {
      sub(/^  - /, "", $0)
      print
    }
  ' "${ROUTING_YAML}"
}

extract_mmd_components() {
  grep -Eho 'ENV\.world_state|EXT\.external_inputs|BOUNDARY\.typed_payload_boundary|REE\.[A-Za-z0-9_]+' \
    "${STATIC_MMD}" "${TYPED_MMD}" "${SEQUENCE_MMD}"
}

extract_sequence_participants() {
  awk '/^  participant / { print $4 }' "${SEQUENCE_MMD}"
}

extract_yaml_streams() {
  awk '
    /^edges:/ { in_edges=1; next }
    in_edges && /stream: / {
      sub(/^.*stream: /, "", $0)
      print
    }
  ' "${ROUTING_YAML}"
}

extract_typed_streams() {
  awk -F'|' '
    /-->\|/ {
      gsub(/^[[:space:]]+|[[:space:]]+$/, "", $2)
      if ($2 != "") print $2
    }
  ' "${TYPED_MMD}"
}

extract_declared_streams() {
  sed -n 's/^- `\([^`]*\)`$/\1/p' "${STREAMS_MD}"
}

extract_yaml_components > "${tmpdir}/yaml_components.raw"
extract_mmd_components > "${tmpdir}/mmd_components.raw"
extract_sequence_participants > "${tmpdir}/sequence_components.raw"
extract_yaml_streams > "${tmpdir}/yaml_streams.raw"
extract_typed_streams > "${tmpdir}/typed_streams.raw"
extract_declared_streams > "${tmpdir}/declared_streams.raw"

sort_unique "${tmpdir}/yaml_components.raw" "${tmpdir}/yaml_components.set"
sort_unique "${tmpdir}/mmd_components.raw" "${tmpdir}/mmd_components.set"
sort_unique "${tmpdir}/sequence_components.raw" "${tmpdir}/sequence_components.set"
sort_unique "${tmpdir}/yaml_streams.raw" "${tmpdir}/yaml_streams.set"
sort_unique "${tmpdir}/typed_streams.raw" "${tmpdir}/typed_streams.set"
sort_unique "${tmpdir}/declared_streams.raw" "${tmpdir}/declared_streams.set"

set_diff "${tmpdir}/yaml_components.set" "${tmpdir}/mmd_components.set" "${tmpdir}/missing_components"
set_diff "${tmpdir}/sequence_components.set" "${tmpdir}/yaml_components.set" "${tmpdir}/unknown_sequence_components"
set_diff "${tmpdir}/yaml_streams.set" "${tmpdir}/typed_streams.set" "${tmpdir}/missing_typed_streams"
set_diff "${tmpdir}/typed_streams.set" "${tmpdir}/yaml_streams.set" "${tmpdir}/unknown_typed_streams"
set_diff "${tmpdir}/yaml_streams.set" "${tmpdir}/declared_streams.set" "${tmpdir}/missing_declared_streams"

has_errors=0

report_set() {
  local label="$1"
  local file="$2"
  if [[ -s "${file}" ]]; then
    has_errors=1
    echo "${label}:" >&2
    sed 's/^/  - /' "${file}" >&2
  fi
}

report_set "Components in routing YAML missing from Mermaid views" "${tmpdir}/missing_components"
report_set "Sequence participants not declared in routing YAML components" "${tmpdir}/unknown_sequence_components"
report_set "Routing streams missing from typed dataflow diagram" "${tmpdir}/missing_typed_streams"
report_set "Typed dataflow streams missing from routing YAML" "${tmpdir}/unknown_typed_streams"
report_set "Routing streams missing from streams.md declarations" "${tmpdir}/missing_declared_streams"

if [[ "${has_errors}" -ne 0 ]]; then
  exit 1
fi

echo "Architecture diagram consistency check passed."
