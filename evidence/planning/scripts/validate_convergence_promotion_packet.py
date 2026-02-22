#!/usr/bin/env python3
"""Validate convergence promotion packet JSON files against schema."""

from __future__ import annotations

import argparse
import json
import sys
from glob import glob
from pathlib import Path

from jsonschema import Draft202012Validator

from build_convergence_intake_queue import _packet_gate_evaluation


def _load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _format_path(path_parts: list[object]) -> str:
    if not path_parts:
        return "<root>"
    return ".".join(str(p) for p in path_parts)


def _default_schema_path(repo_root: Path) -> Path:
    return repo_root / "evidence" / "planning" / "schemas" / "v1" / "convergence_promotion_packet.schema.json"


def _resolve(repo_root: Path, raw_path: str) -> Path:
    path = Path(raw_path)
    if path.is_absolute():
        return path
    return repo_root / path


def _resolve_inputs(repo_root: Path, raw_inputs: list[str], input_glob: str) -> list[Path]:
    if input_glob:
        full_pattern = input_glob if Path(input_glob).is_absolute() else (repo_root / input_glob).as_posix()
        return [Path(p) for p in sorted(glob(full_pattern))]
    return [_resolve(repo_root, raw_input) for raw_input in raw_inputs]


def main() -> int:
    repo_root = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--schema",
        type=Path,
        default=_default_schema_path(repo_root),
        help="Path to convergence promotion packet schema JSON.",
    )
    parser.add_argument("--input", nargs="+", default=[], help="One or more packet JSON file paths.")
    parser.add_argument(
        "--input-glob",
        default="",
        help="Glob pattern for packet JSON files (absolute or repo-relative).",
    )
    parser.add_argument(
        "--check-gate-readiness",
        action="store_true",
        help="Also evaluate gate readiness (beyond schema validity).",
    )
    parser.add_argument(
        "--fail-on-gate-failure",
        action="store_true",
        help="Return non-zero when a packet is schema-valid but gate-blocked.",
    )
    args = parser.parse_args()

    if not args.input and not args.input_glob:
        parser.error("Provide --input and/or --input-glob.")

    schema_path = _resolve(repo_root, str(args.schema))
    if not schema_path.exists():
        print(f"Schema not found: {schema_path}", file=sys.stderr)
        return 2

    schema = _load_json(schema_path)
    validator = Draft202012Validator(schema)
    input_paths = _resolve_inputs(repo_root, args.input, args.input_glob)
    if args.input_glob and not input_paths:
        print(f"No packet files matched: {args.input_glob}")
        return 0

    any_invalid = False
    any_gate_blocked = False
    for input_path in input_paths:
        if not input_path.exists():
            print(f"Input not found: {input_path}", file=sys.stderr)
            return 2

        try:
            payload = _load_json(input_path)
        except json.JSONDecodeError as exc:
            print(f"INVALID: {input_path} (JSON parse error: {exc})")
            any_invalid = True
            continue

        errors = sorted(validator.iter_errors(payload), key=lambda e: list(e.path))
        if not errors:
            print(f"VALID: {input_path}")
            if args.check_gate_readiness:
                gate_ready, gate_failures, placeholder_found, placeholder_hits = _packet_gate_evaluation(payload)
                if gate_ready:
                    print(f"GATE-READY: {input_path}")
                else:
                    any_gate_blocked = True
                    print(f"GATE-BLOCKED: {input_path}")
                    for reason in gate_failures:
                        print(f"- gate_failure: {reason}")
                    if placeholder_found:
                        for hit in placeholder_hits[:10]:
                            print(f"- placeholder_hit: {hit}")
            continue

        any_invalid = True
        print(f"INVALID: {input_path}")
        for err in errors:
            location = _format_path(list(err.path))
            print(f"- {location}: {err.message}")

    if any_invalid:
        return 1
    if args.fail_on_gate_failure and any_gate_blocked:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
