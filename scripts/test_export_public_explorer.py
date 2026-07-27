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

The export is redirected to a TEMP DIR -- see the _REAL_OUT_DIR block below.
"""
import atexit
import json
import shutil
import sys
import tempfile
from pathlib import Path

import export_public_explorer as exp

# --- redirect the export away from the tracked output dir -------------------
# The exporter writes into `exp.OUT_DIR`, which by default is the TRACKED
# docs/public_explorer/data/. Running this suite therefore used to regenerate
# six tracked JSON files as a side effect: measured 2026-07-27, a single run
# left +1979/-484 across four of them, because the published export had been
# stale since 2026-06-15 and the test refreshed it.
#
# That is a real hazard in this repo, not untidiness. REE_assembly is a shared
# multi-session checkout, so tracked files left dirty by a test are exactly
# what the next session's whole-file read-modify-write sweeps into ITS commit
# (root CLAUDE.md, "Read-modify-write contamination"). A test must not stage
# work for someone else to land.
#
# `OUT_DIR` is a module-level global that the exporter re-reads at call time in
# BOTH main() and validate_outputs(), so rebinding it once here covers the
# whole suite. It is deliberately NOT restored afterwards: validate_outputs()
# is called after main() and must see the same directory.
_REAL_OUT_DIR = exp.OUT_DIR
_TMP_OUT_DIR = Path(tempfile.mkdtemp(prefix="ree_public_explorer_test_"))
atexit.register(shutil.rmtree, _TMP_OUT_DIR, ignore_errors=True)
exp.OUT_DIR = _TMP_OUT_DIR

OUT_DIR = _TMP_OUT_DIR


# --- positive controls: the scrub MUST catch these -------------------------
LEAK_SAMPLES = [
    "ssh user@203.0.113.10",
    "hub at 192.0.2.1:8787",
    "worker ree-cloud-4 idle",
    "runs on WORKSTATION.local",
    "/Users/example/REE_Working/secret.txt",
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


_EXPORT_DONE = False


def _ensure_export():
    # Build the export into the temp dir. Cached: four tests below need the
    # output and the exporter is the slow part of this suite.
    global _EXPORT_DONE
    if _EXPORT_DONE:
        return
    # main() parses argv; call it with no args by temporarily clearing argv.
    saved = sys.argv
    try:
        sys.argv = ["export_public_explorer.py"]
        code = exp.main()
    finally:
        sys.argv = saved
    assert code == 0, f"exporter returned {code}"
    _EXPORT_DONE = True


def test_export_does_not_touch_tracked_output_dir():
    """The redirect above must hold -- otherwise this suite dirties the repo.

    Guards the redirect itself rather than trusting it, in the same spirit as
    the LEAK_SAMPLES positive controls: a safety net that is never exercised is
    not known to work. If someone re-points OUT_DIR at the real directory, or
    the exporter starts resolving its own path internally instead of reading
    the module global, this fails instead of silently rewriting tracked JSON.
    """
    _ensure_export()
    assert exp.OUT_DIR == _TMP_OUT_DIR, (
        f"exporter OUT_DIR was re-pointed at {exp.OUT_DIR}, expected the temp dir"
    )
    assert OUT_DIR != _REAL_OUT_DIR, "suite is asserting against the tracked dir"
    # The export ran; if it landed anywhere, it landed in the temp dir.
    assert (_TMP_OUT_DIR / "index.json").exists(), (
        f"export did not write into the temp dir {_TMP_OUT_DIR} -- the redirect "
        f"is not being honoured and output may have gone to {_REAL_OUT_DIR}"
    )


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
    test_export_does_not_touch_tracked_output_dir,
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
