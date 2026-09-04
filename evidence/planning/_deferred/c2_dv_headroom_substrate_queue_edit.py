"""Deferred registry edit for substrate_queue entry dv-dynamic-range-precondition-class.

Narrow structural read-modify-write (CLAUDE.md "Prevention"): loads the file, mutates ONE
entry's fields, writes back. Re-reads the live file at apply time, per the concurrency rule.

Apply ONLY when `task_claim.py check --resources
REE_assembly/evidence/planning/substrate_queue.json` exits 0 (the governance-20260904-1347
pause lock released). Never force through the lock.

    /opt/local/bin/python3 <this file> [--dry-run]
"""
import json
import sys
from pathlib import Path

QUEUE = Path("/Users/dgolden/REE_Working/REE_assembly/evidence/planning/substrate_queue.json")
SD_ID = "dv-dynamic-range-precondition-class"

PATCH = {
    "status": "implemented_pending_validation",
    "status_phase": "validation_owed",
    "implementation_status": "implemented",
    "implemented_utc": "2026-09-04T16:44:00Z",
    "implemented_session": "campaign-c2-build-20260904",
    "implemented_commit_ree_v3": "8e133d26ed",
    "implementation_note": (
        "BUILT AND LANDED ree-v3 main 8e133d26ed (verified on origin/main 2026-09-04), "
        "harness-only per the governance-20260903T2013 red-team scope. TWO HALVES. "
        "(1) Runtime, opt-in: experiments/_metrics.py `dv_achievable()` + "
        "`dv_headroom_check(name, dv_name=, criterion_threshold=, control_values=|achievable=, "
        "statistic=, dv_bounds=, margin=)` -> `p0_readiness_gate()`, declaring precondition "
        "kind `dv_headroom`. It rides the gate's existing single-bound path (measured = what "
        "the DV can achieve, threshold = what the criterion requires, direction lower), so an "
        "unmet entry raises P0NotReady and the caller writes the substrate_not_ready_requeue "
        "manifest it already writes. Four achievable statistics, matched to the corpus "
        "failures and NOT interchangeable: `range` (983/994), `max_abs` (993), "
        "`ceiling_headroom` (981's saturated baseline; needs dv_bounds), `floor_headroom`; or "
        "`achievable=` for an analytic ceiling (951c's zero reachable ticks). Reproduces every "
        "autopsy number: 983 3.2x, 993 13.2x, 994 25.6x, 981 precision-margin 51.3x, and 981 "
        "C1 achievable 1.0 < required 1.154. NO INDEXER CHANGE NEEDED -- the REE_assembly "
        "indexer recomputes met from (measured, threshold, direction) and is kind-agnostic, so "
        "an unmet entry adjudicates as precondition_unmet on its own. "
        "(2) Static, WARN-only: validate_experiments.py "
        "`--checks criterion_exceeds_achievable_range`, same family as "
        "dry_run_unreachable_criterion. Sub-case (a) multiplicative threshold on a "
        "unit-interval DV (981 C1: 2x a 0.5771 baseline = 1.154 on a [0,1] DV); sub-case (b) "
        "absolute floor on a derived-range statistic (983 decline_gap 0.15). Scanned on "
        "load-bearing criteria AND on readiness preconditions, because 981's OWN (b) instance "
        "is a precondition (precision_margin_norm_elevated_under_hv, 0.01 floor vs 0.000195 "
        "available). Never hardens the exit code in any mode -- it cannot PROVE unreachability "
        "(the baseline is a runtime quantity); it reports that nothing establishes the "
        "threshold's feasibility. Fires 110/1423 (7.7%); restricting to the corpus's own "
        "`load_bearing: True` tag cut that from 210 (14.5%) while KEEPING both known carriers "
        "(981, 983). Silenced by any mention of dv_headroom in the file (deliberately generous "
        "-- the point is to make the author answer the question); explicit opt-out "
        "CRITERION_ACHIEVABLE_RANGE_EXEMPT. "
        "BOUNDARY HELD: substrate_paths unchanged (validate_experiments.py + "
        "experiments/_metrics.py::p0_readiness_gate); ree_core/environment NOT touched and "
        "severity NOT raised, so the 1,201 drivers importing causal_grid_world are unaffected "
        "and Step 2.5c does not block. Byte-identical for every driver that does not opt in "
        "(pinned by test_p0_readiness_gate_is_byte_identical_for_drivers_that_do_not_opt_in "
        "and test_no_shipped_driver_currently_declares_the_new_kind). "
        "PRECEDENT: V3-EXQ-777a hand-rolled this guard locally (score_dv_headroom_seeds, "
        "'the guard V3-EXQ-777 lacked') -- one driver inventing it after losing a run is the "
        "argument for putting it where the next driver inherits it. "
        "GATES: 47 new contracts in tests/contracts/test_criterion_exceeds_achievable_range_lint.py; "
        "full tests/contracts green on the hub (4614 passed, 25 skipped, 1 xfailed, 43 "
        "subtests, exit 0); pre-commit gate 689 contracts passed; full-corpus "
        "validate_experiments.py exit 0 (unchanged). Also documented: ree-v3/CLAUDE.md "
        "'DV-headroom class' section + tests/contracts/LINT_INDEX.md row (count refreshed "
        "20 -> 28). "
        "VALIDATION OWED, and it is NOT a separate mint job: the six headroom-derived redesign "
        "queues of campaign C2 items 2-5 (983/991/993 redesigns, 642c, 981a, 963b, 822e) each "
        "declare the dv_headroom precondition, and they are the validation. "
        "Registry write DEFERRED at build time behind the governance-20260904-1347 exact-file "
        "pause lock on this file and applied once it cleared."
    ),
}


def main() -> int:
    dry = "--dry-run" in sys.argv
    doc = json.loads(QUEUE.read_text(encoding="utf-8"))          # fresh read at apply time
    rows = doc.get("queue") if isinstance(doc.get("queue"), list) else doc.get("items")
    if rows is None:
        print("REFUSE: no queue/items array found")
        return 2
    hits = [r for r in rows if (r.get("sd_id") or r.get("id")) == SD_ID]
    if len(hits) != 1:
        print(f"REFUSE: expected exactly 1 entry for {SD_ID}, found {len(hits)}")
        return 2
    entry = hits[0]
    if entry.get("implementation_status") == "implemented":
        print(f"NO-OP: {SD_ID} already marked implemented "
              f"({entry.get('implemented_utc')}, {entry.get('implemented_session')})")
        return 0
    before = {k: entry.get(k) for k in PATCH}
    entry.update(PATCH)
    print(f"entry {SD_ID}: {len(PATCH)} field(s) set")
    for k in PATCH:
        if k != "implementation_note":
            print(f"  {k}: {before[k]!r} -> {entry[k]!r}")
    if dry:
        print("(dry run -- nothing written)")
        return 0
    # ensure_ascii=True + indent=2 + trailing newline is the file's CANONICAL
    # serialization -- verified byte-identical on a round-trip of the untouched file.
    # ensure_ascii=False reformats 5 unrelated entries (non-ASCII escapes such as
    # "§" become literal characters), which would land other sessions' lines in
    # this commit as a diff they never wrote. Do not "improve" this.
    QUEUE.write_text(json.dumps(doc, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(f"wrote {QUEUE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
