#!/usr/bin/env python3
"""
Validation suite for the public REE Explorer export.

Stdlib-only (imports the exporter module for its scrub regexes + validator).
Runs the exporter once, then asserts the published output is leak-free and
in-scope. Also unit-tests the sensitive-pattern scrub with positive controls
so the safety net itself is proven to fire.

Run standalone:
    /opt/local/bin/python3 scripts/test_export_public_explorer.py
Or under pytest:
    pytest scripts/test_export_public_explorer.py
Exit code 0 == all checks pass; non-zero == failure.
"""
import json
import sys
from pathlib import Path

import export_public_explorer as exp

OUT_DIR = exp.OUT_DIR


# --- positive controls: the scrub MUST catch these -------------------------
LEAK_SAMPLES = [
    "ssh ree@91.98.130.117",
    "hub at 10.8.0.1:8787",
    "worker ree-cloud-4 idle",
    "runs on DLAPTOP-4.local",
    "/Users/dgolden/REE_Working/secret.txt",
    "/home/ree/coordinator-spool/pending/",
    "api_key = sk-ABCDEF0123456789ABCDEF",
    "see /etc/systemd/system/ree-runner.service",
]
# These must NOT be flagged (avoid over-redaction of legitimate science text).
CLEAN_SAMPLES = [
    "SD-016 ContextMemory diversification loss 4-arm ablation",
    "MECH-423 cross-model super-additivity weakened at seed 13",
    "Slot diversity 0.199 vs 0.191; entropy 2.772",
    "Hippocampal CA3 pattern completion gate",
]


def test_scrub_catches_leaks():
    failures = []
    for s in LEAK_SAMPLES:
        hit = any(pat.search(s) for _, pat in exp.SENSITIVE_PATTERNS)
        if not hit:
            failures.append(f"leak NOT caught: {s!r}")
    assert not failures, "\n".join(failures)


def test_scrub_allows_clean_science():
    failures = []
    for s in CLEAN_SAMPLES:
        for name, pat in exp.SENSITIVE_PATTERNS:
            if pat.search(s):
                failures.append(f"clean text over-redacted by '{name}': {s!r}")
    assert not failures, "\n".join(failures)


def _ensure_export():
    # Build the export (idempotent; overwrites previous output).
    rc = exp.main.__wrapped__ if hasattr(exp.main, "__wrapped__") else None
    # main() parses argv; call it with no args by temporarily clearing argv.
    saved = sys.argv
    try:
        sys.argv = ["export_public_explorer.py"]
        code = exp.main()
    finally:
        sys.argv = saved
    assert code == 0, f"exporter returned {code}"


def test_outputs_valid_and_in_scope():
    _ensure_export()
    failures = exp.validate_outputs()
    assert not failures, "validate_outputs reported:\n  " + "\n  ".join(failures)


def test_expected_files_exist():
    _ensure_export()
    for name in ("index.json", "claims_public.json", "experiments_public.json",
                 "mechanisms_public.json", "help_wanted.json", "orientation.json"):
        assert (OUT_DIR / name).exists(), f"missing {name}"


def test_no_future_stage_claims():
    _ensure_export()
    claims = json.loads((OUT_DIR / "claims_public.json").read_text(encoding="utf-8"))
    # Status labels of excluded raw statuses should never appear.
    bad_status = {"Candidate", "Open", "Legacy", "Retired", "Deprecated"}
    for c in claims:
        assert c["status"] not in bad_status, f"{c['id']} has withheld status {c['status']}"


def test_pending_is_count_only():
    _ensure_export()
    index = json.loads((OUT_DIR / "index.json").read_text(encoding="utf-8"))
    prc = index.get("pending_review_count")
    assert prc is None or isinstance(prc, int), "pending must be a bare int or null"
    text = (OUT_DIR / "index.json").read_text(encoding="utf-8").lower()
    for token in ("run_id", "exq-", "queue_id"):
        assert token not in text, f"index.json leaks pending detail token: {token}"


ALL_TESTS = [
    test_scrub_catches_leaks,
    test_scrub_allows_clean_science,
    test_expected_files_exist,
    test_outputs_valid_and_in_scope,
    test_no_future_stage_claims,
    test_pending_is_count_only,
]


def main():
    failed = 0
    for t in ALL_TESTS:
        try:
            t()
            print(f"PASS  {t.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL  {t.__name__}\n      {e}")
        except Exception as e:  # noqa: BLE001
            failed += 1
            print(f"ERROR {t.__name__}\n      {type(e).__name__}: {e}")
    print(f"\n{len(ALL_TESTS) - failed}/{len(ALL_TESTS)} checks passed.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
