#!/usr/bin/env python3
"""test_evidence_strip_data.py -- standalone tests for the evidence_strip_data
draft. Run directly:

    /opt/local/bin/python3 test_evidence_strip_data.py

Exit code 0 on pass, 1 on first failure (prints which assertion failed).
No pytest dependency -- this is a scratchpad draft, keep it runnable anywhere.
"""

import json
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import evidence_strip_data as esd  # noqa: E402

REAL_REPO_ROOT = "/Users/dgolden/REE_Working/REE_assembly"

_failures = []


def check(label, cond):
    if cond:
        print("PASS: %s" % label)
    else:
        print("FAIL: %s" % label)
        _failures.append(label)


def check_raises_nothing(label, fn):
    try:
        result = fn()
        print("PASS: %s (no exception, returned %r)" % (
            label, result if not isinstance(result, dict) else "<dict, %d keys>" % len(result)))
        return result
    except Exception as exc:  # the one thing this module must never do
        print("FAIL: %s raised %r" % (label, exc))
        _failures.append(label)
        return None


# ---------------------------------------------------------------------------
# Fixture builders
# ---------------------------------------------------------------------------

GOOD_CLOSURE_MD = """# REE-v3 Closure Status (snapshot)

Generated: 2026-09-07T04:21:26Z

## Overall

- Weighted progress: **73.0%** across 97 non-deferred nodes in 17 plan(s) with closure frontmatter.
- Remaining (open/in-progress/blocked/partial): **33** nodes.
- Assembly frontier (required, under construction): **10** nodes.
- Deferred (not required for v3 closure): 10 nodes.
- Done: 64 nodes.
"""

GOOD_CLAIMS_YAML = """\
- id: INV-001
  title: "example"
  status: active
- id: INV-002
  title: "example 2"
  status: active
- id: MECH-001
  title: "example 3"
  status: provisional
- id: MECH-002
  title: "example 4"
  status: candidate   # inline comment on an enum value, must not corrupt the parse
"""


def _mk_manifest(run_id, extra=None):
    d = {"run_id": run_id, "outcome": "PASS"}
    if extra:
        d.update(extra)
    return d


def build_repo(tmpdir, with_closure=True, with_claims=True, with_experiments=True,
                corrupt_claims=False, corrupt_closure=False, empty_experiments_dir=False):
    root = os.path.join(tmpdir, "REE_assembly")
    os.makedirs(root, exist_ok=True)

    if with_closure:
        planning = os.path.join(root, "evidence", "planning")
        os.makedirs(planning, exist_ok=True)
        text = "not a closure file at all {{{ broken" if corrupt_closure else GOOD_CLOSURE_MD
        with open(os.path.join(planning, "closure_status.md"), "w", encoding="utf-8") as fh:
            fh.write(text)

    if with_claims:
        claims_dir = os.path.join(root, "docs", "claims")
        os.makedirs(claims_dir, exist_ok=True)
        text = "{{{ not: valid: yaml: [[[" if corrupt_claims else GOOD_CLAIMS_YAML
        with open(os.path.join(claims_dir, "claims.yaml"), "w", encoding="utf-8") as fh:
            fh.write(text)

    if with_experiments:
        exp_dir = os.path.join(root, "evidence", "experiments")
        os.makedirs(exp_dir, exist_ok=True)
        if not empty_experiments_dir:
            # a real flat manifest
            with open(os.path.join(exp_dir, "run_a_v3.json"), "w", encoding="utf-8") as fh:
                json.dump(_mk_manifest("run_a"), fh)
            # a non-manifest index file sitting flat alongside it -- must be excluded
            with open(os.path.join(exp_dir, "review_tracker.json"), "w", encoding="utf-8") as fh:
                json.dump({"reviewed_run_ids": ["run_a"]}, fh)
            # a corrupt flat json file -- must be skipped, not fatal
            with open(os.path.join(exp_dir, "run_broken_v3.json"), "w", encoding="utf-8") as fh:
                fh.write("{not valid json")
            # a nested runs/ pack manifest, distinct run_id
            pack_dir = os.path.join(exp_dir, "exp_one", "runs", "run_b")
            os.makedirs(pack_dir, exist_ok=True)
            with open(os.path.join(pack_dir, "manifest.json"), "w", encoding="utf-8") as fh:
                json.dump(_mk_manifest("run_b"), fh)
            # a nested pack manifest that DUPLICATES the flat run_a -- must
            # collapse to one when counted (union by run_id)
            dup_dir = os.path.join(exp_dir, "exp_one", "runs", "run_a")
            os.makedirs(dup_dir, exist_ok=True)
            with open(os.path.join(dup_dir, "manifest.json"), "w", encoding="utf-8") as fh:
                json.dump(_mk_manifest("run_a"), fh)
            # an auxiliary state dir that must be excluded even though it
            # holds a *.json file
            aux_dir = os.path.join(exp_dir, "_partial")
            os.makedirs(aux_dir, exist_ok=True)
            with open(os.path.join(aux_dir, "should_not_count.json"), "w", encoding="utf-8") as fh:
                json.dump(_mk_manifest("run_should_not_count"), fh)

    return root


def main():
    tmp = tempfile.mkdtemp(prefix="evidence_strip_test_")
    try:
        # -------------------------------------------------------------
        # 1. Fully missing repo root -> None (nothing derivable at all)
        # -------------------------------------------------------------
        missing_root = os.path.join(tmp, "does_not_exist")
        result = check_raises_nothing(
            "missing root entirely -> no exception",
            lambda: esd.gather_evidence_figures(missing_root),
        )
        check("missing root entirely -> returns None", result is None)

        # -------------------------------------------------------------
        # 2. Repo dir exists but is completely empty -> None
        # -------------------------------------------------------------
        empty_root = os.path.join(tmp, "empty_repo")
        os.makedirs(empty_root, exist_ok=True)
        result = check_raises_nothing(
            "empty repo dir -> no exception",
            lambda: esd.gather_evidence_figures(empty_root),
        )
        check("empty repo dir -> returns None", result is None)

        # -------------------------------------------------------------
        # 3. Only closure present and good; claims + experiments absent
        #    -> closure keys present, claims_*/runs_logged ABSENT (not 0)
        # -------------------------------------------------------------
        only_closure_root = build_repo(
            os.path.join(tmp, "only_closure"),
            with_closure=True, with_claims=False, with_experiments=False,
        )
        result = check_raises_nothing(
            "closure-only repo -> no exception",
            lambda: esd.gather_evidence_figures(only_closure_root),
        )
        if result is not None:
            check("closure-only: closure_pct present", result.get("closure_pct") == 73.0)
            check("closure-only: closure_done present", result.get("closure_done") == 64)
            check("closure-only: closure_remaining present", result.get("closure_remaining") == 33)
            check("closure-only: closure_total present", result.get("closure_total") == 97)
            check("closure-only: claims_total ABSENT (not 0, not None-as-value)",
                  "claims_total" not in result)
            check("closure-only: claims_active ABSENT", "claims_active" not in result)
            check("closure-only: runs_logged ABSENT", "runs_logged" not in result)

        # -------------------------------------------------------------
        # 4. Corrupt claims.yaml, good closure, good experiments
        #    -> claims_* keys absent; closure + runs_logged still work
        # -------------------------------------------------------------
        corrupt_claims_root = build_repo(
            os.path.join(tmp, "corrupt_claims"),
            with_closure=True, with_claims=True, with_experiments=True,
            corrupt_claims=True,
        )
        result = check_raises_nothing(
            "corrupt claims.yaml -> no exception",
            lambda: esd.gather_evidence_figures(corrupt_claims_root),
        )
        if result is not None:
            check("corrupt claims: claims_total ABSENT", "claims_total" not in result)
            check("corrupt claims: claims_by_status ABSENT", "claims_by_status" not in result)
            check("corrupt claims: closure_pct still present", result.get("closure_pct") == 73.0)
            check("corrupt claims: runs_logged still present (union dedup = 2)",
                  result.get("runs_logged") == 2)

        # -------------------------------------------------------------
        # 5. Corrupt closure_status.md, good claims, good experiments
        #    -> closure_* keys absent (or partially absent); claims/runs OK
        # -------------------------------------------------------------
        corrupt_closure_root = build_repo(
            os.path.join(tmp, "corrupt_closure"),
            with_closure=True, with_claims=True, with_experiments=True,
            corrupt_closure=True,
        )
        result = check_raises_nothing(
            "corrupt closure_status.md -> no exception",
            lambda: esd.gather_evidence_figures(corrupt_closure_root),
        )
        if result is not None:
            check("corrupt closure: closure_pct ABSENT", "closure_pct" not in result)
            check("corrupt closure: closure_done ABSENT", "closure_done" not in result)
            check("corrupt closure: claims_active present and correct",
                  result.get("claims_active") == 2)
            check("corrupt closure: claims_provisional present and correct",
                  result.get("claims_provisional") == 1)
            check("corrupt closure: claims_candidate present (inline-comment status parsed clean)",
                  result.get("claims_candidate") == 1)
            check("corrupt closure: claims_total present", result.get("claims_total") == 4)

        # -------------------------------------------------------------
        # 6. evidence/experiments/ directory entirely missing
        #    -> runs_logged ABSENT (not 0)
        # -------------------------------------------------------------
        no_exp_root = build_repo(
            os.path.join(tmp, "no_experiments"),
            with_closure=True, with_claims=True, with_experiments=False,
        )
        result = check_raises_nothing(
            "missing evidence/experiments/ -> no exception",
            lambda: esd.gather_evidence_figures(no_exp_root),
        )
        if result is not None:
            check("missing experiments dir: runs_logged ABSENT (dir doesn't exist)",
                  "runs_logged" not in result)

        # -------------------------------------------------------------
        # 7. evidence/experiments/ exists but is genuinely empty
        #    -> runs_logged == 0 (a real zero, distinguishable from absent)
        # -------------------------------------------------------------
        empty_exp_root = build_repo(
            os.path.join(tmp, "empty_experiments"),
            with_closure=True, with_claims=True, with_experiments=True,
            empty_experiments_dir=True,
        )
        result = check_raises_nothing(
            "empty evidence/experiments/ dir -> no exception",
            lambda: esd.gather_evidence_figures(empty_exp_root),
        )
        if result is not None:
            check("empty experiments dir present -> runs_logged present as int 0",
                  "runs_logged" in result and result["runs_logged"] == 0)

        # -------------------------------------------------------------
        # 8. Full good repo -> exercises exclusion + dedup rules together:
        #    review_tracker.json excluded, corrupt flat json skipped,
        #    run_a counted once despite flat+pack duplication, run_b
        #    counted from pack-only, _partial/ dir excluded entirely.
        #    Expect exactly 2 (run_a, run_b) -- NOT 3, NOT 4.
        # -------------------------------------------------------------
        full_good_root = build_repo(os.path.join(tmp, "full_good"))
        result = check_raises_nothing(
            "full synthetic good repo -> no exception",
            lambda: esd.gather_evidence_figures(full_good_root),
        )
        if result is not None:
            check("full good repo: runs_logged == 2 (dedup + exclusions correct)",
                  result.get("runs_logged") == 2)
            check("full good repo: claims_by_status is a dict with 3 statuses",
                  isinstance(result.get("claims_by_status"), dict)
                  and len(result["claims_by_status"]) == 3)

        # -------------------------------------------------------------
        # 9. Happy path against the REAL repo (skipped gracefully if this
        #    box doesn't have it -- but on this box it must be present).
        # -------------------------------------------------------------
        if os.path.isdir(REAL_REPO_ROOT):
            real_result = check_raises_nothing(
                "REAL repo run -> no exception",
                lambda: esd.gather_evidence_figures(REAL_REPO_ROOT),
            )
            check("REAL repo: result is not None", real_result is not None)
            if real_result:
                check("REAL repo: closure_pct is a float", isinstance(real_result.get("closure_pct"), float))
                check("REAL repo: closure_done + closure_remaining == closure_total",
                      real_result.get("closure_done", -1) + real_result.get("closure_remaining", -1)
                      == real_result.get("closure_total", -2))
                check("REAL repo: claims_total > 1000", real_result.get("claims_total", 0) > 1000)
                check("REAL repo: claims_active + claims_provisional + claims_candidate <= claims_total",
                      (real_result.get("claims_active", 0) + real_result.get("claims_provisional", 0)
                       + real_result.get("claims_candidate", 0)) <= real_result.get("claims_total", 0))
                check("REAL repo: runs_logged > 2000 (union of flat + nested pack layouts)",
                      real_result.get("runs_logged", 0) > 2000)
                print()
                print("REAL repo figures:")
                print(json.dumps(real_result, indent=2, sort_keys=True))
        else:
            print("SKIP: real repo not present at %s on this box" % REAL_REPO_ROOT)

        # -------------------------------------------------------------
        # claim/evidence join: fail-open + never-fabricate-zero
        # -------------------------------------------------------------
        check_raises_nothing(
            "claim-evidence join fail-open -> no exception",
            test_claim_evidence_fail_open,
        )

    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print()
    if _failures:
        print("%d FAILURE(S):" % len(_failures))
        for f in _failures:
            print("  - %s" % f)
        return 1
    print("ALL CHECKS PASSED")
    return 0



def test_claim_evidence_fail_open():
    """The claim/evidence join must fail open exactly like the other sources.

    Added alongside _gather_claim_evidence. Covers: file absent, file
    present but not JSON, valid JSON of the wrong shape, and entries that
    are individually malformed. None may raise, and none may fabricate a
    zero for a source that could not be read.
    """
    import json as _json
    import tempfile
    import shutil

    root = tempfile.mkdtemp()
    try:
        expdir = os.path.join(root, "evidence", "experiments")
        os.makedirs(expdir)
        target = os.path.join(expdir, "claim_evidence.v1.json")

        # 1. absent -> no evidence keys at all (not zeros)
        got = esd._gather_claim_evidence(root)
        assert got == {}, "absent join should yield {}, got %r" % (got,)

        # 2. present but not JSON
        with open(target, "w") as fh:
            fh.write("{ this is not json")
        got = esd._gather_claim_evidence(root)
        assert got == {}, "unparseable join should yield {}, got %r" % (got,)

        # 3. valid JSON, wrong shape (entries missing / not a list)
        for payload in ({}, {"entries": "nope"}, {"entries": None}, []):
            with open(target, "w") as fh:
                _json.dump(payload, fh)
            got = esd._gather_claim_evidence(root)
            assert got == {}, "bad shape %r should yield {}, got %r" % (payload, got)

        # 4. malformed individual entries must be skipped, not fatal
        with open(target, "w") as fh:
            _json.dump({"entries": [
                None,
                "string-not-dict",
                {"claim_id": "MECH-1", "evidence_class": "exp:sim",
                 "evidence_direction": "supports"},
                {"evidence_direction": "weakens"},
            ]}, fh)
        got = esd._gather_claim_evidence(root)
        assert got["evidence_entries"] == 4, got
        assert got["claims_with_supporting_evidence"] == 1, got
        assert got["evidence_supports"] == 1, got
        assert got["evidence_weakens"] == 1, got

        # 5. a direction that never occurs must be ABSENT, not 0
        with open(target, "w") as fh:
            _json.dump({"entries": [{"claim_id": "X", "evidence_direction": "supports",
                                     "evidence_class": "exp:sim"}]}, fh)
        got = esd._gather_claim_evidence(root)
        assert "evidence_weakens" not in got, \
            "a direction with no occurrences must be absent, not zero: %r" % (got,)
    finally:
        shutil.rmtree(root, ignore_errors=True)

    print("  ok: claim-evidence join fails open and never fabricates zeros")

if __name__ == "__main__":
    sys.exit(main())
