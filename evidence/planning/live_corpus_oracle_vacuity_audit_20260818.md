# Live-corpus test suites -- oracle-vacuity audit by fault injection (non-IGW sweep)

**Date:** 2026-08-18
**Chip:** `chip-20260818-live-corpus-oracle-vacuity-sweep`
**Precedent:** FM11d (`test_backfill_failure_record_run_role.py`, REE_assembly `48bae8be81`)
and the IGW generator sweep, `evidence/planning/igw_test_oracle_vacuity_audit_20260818.md`

**Status: COMPLETE. All three findings are FIXED and landed (`ed839b9771`).
Nothing here is awaiting user action.** One UNRELATED pre-existing trunk failure
is reported in section 5 -- it is not a vacuity finding and was deliberately not
touched.

## 1. Question

Two confirmed instances of one defect class exist: a test whose **oracle is computed
by the function under test**, so reverting that function empties the oracle and the
assertion passes against nothing. Does the shape exist in the six non-IGW suites that
carry the live-corpus signature?

Suites audited (all in `REE_assembly/scripts/`):

    test_check_manifest_degeneracy_consistency.py
    test_check_plan_status_table_sync.py
    test_check_skill_improvement_recurrence.py
    test_default_off_drift_guard.py
    test_validate_literature.py
    test_verify_literature_identifiers.py

## 2. Method

For each suite, the predicate/loader helpers in the module under test were monkeypatched
to their plausible pre-fix / degenerate return (constant `True`, constant `False`, empty
collection, `None`, identity), the test module re-imported, and the live-corpus cases
re-run. **A test that stays GREEN under a revert it is supposed to catch is the finding.**
Corpus-drift scenarios were injected directly as well: loader returning empty, corpus
file missing, named ids removed, registry emptied.

Before/after states were measured against the *committed* file (`git show HEAD:...`),
not from memory.

### Two method traps that produced wrong numbers on the first pass

Both are worth knowing because each silently produces a *confident* wrong answer.

1. **Patch the module object the TEST actually holds.** `test_validate_literature.py`
   and `test_default_off_drift_guard.py` load their subject through
   `importlib.util.spec_from_file_location` under an ALIAS
   (`ree_validate_literature_under_test`). Patching `importlib.import_module
   ("validate_literature")` patches a *different object*, and every injection appears
   to be absorbed -- reading as "vacuous under everything" when in fact nothing was
   injected at all. Patch `test_module.V` / `test_module.g` instead.
2. **Match the helper's real return ARITY and truthiness.** `already_codified` returns
   `None`-or-dict, not a `(bool, reason)` tuple; injecting `(False, None)` is TRUTHY and
   simulates *everything codified*, the opposite of the intended revert.
   `iter_record_paths` returns a 2-tuple, so `-> []` raises `ValueError` and the test
   goes RED for the wrong reason -- which reads as a working guard.

## 3. Result: 3 of 6 suites CLEAN, 3 findings (all fixed)

### Clean, and why -- negative results, stated so they are not re-audited

| Suite | Why it is immune |
|---|---|
| `test_check_manifest_degeneracy_consistency.py` | `TestLiveCorpus.test_corrected_trio_is_clean_on_disk` is negative-only, but its partner `TestIncidentReplay.test_pre_fix_trio_is_flagged` asserts the POSITIVE direction over the same `check_run` and goes RED under `check_run -> clean` (verified). The partner rule is satisfied. Corpus drift degrades to SKIP, never to a false GREEN. |
| `test_check_plan_status_table_sync.py` | `test_live_tree_parses_without_exploding` already carries real non-vacuity guards (`assertGreater(len(plans), 10)`, `assertGreater(compared, 0)`) and goes RED on an empty `PLANNING_DIR` and on `n_rows == 0`. `test_a_reconciled_plan_reports_clean` is negative-only but partnered: **13 of 25** tests in the suite go RED under `check_plan -> always-clean`. |
| `test_default_off_drift_guard.py` | Independent LITERAL oracle plus an explicit cardinality guard: `assert len(knobs) > 100`, `sum(k.claim_ids) > 50`, and named-knob assertions (`harm_surprise_pe_enabled`, `use_hierarchical_goal_credit`). Both live tests go RED under `parse_knobs -> {}`; the misattribution revert `knob_site -> "config.py:0"` is caught too. |

`test_verify_literature_identifiers.py` has **no live-corpus class at all** -- every class
is `FixtureCase` (tempdir) or pure-unit with literal oracles; `REPO_ROOT` is used only to
copy scripts INTO a fixture repo. It is immune by construction on the live-corpus axis,
which is why its one finding (F3) is a registry-cardinality shape rather than a corpus one.

### FINDING F1 -- `test_check_skill_improvement_recurrence.py::TestLiveCorpusSmoke`

**The FM11d shape, exactly.** The test built its oracle by filtering `audit()`'s **own**
`excluded_already_codified` output for the seed-44 artifacts:

    codified_artifacts = {a for r in result["excluded_already_codified"] for a in r["artifacts"]}
    seed44_files = {a for a in codified_artifacts if "539-540" in a or "538a" in a}
    if seed44_files:
        self.assertTrue(len(seed44_files) >= 1)          # `if X: assert X` -- a tautology
    self.assertFalse(candidate_artifacts & seed44_files)  # empty & anything == empty

Reverting `already_codified` to never-fire empties `excluded_already_codified`, which
empties `seed44_files`, which makes the intersection empty, which passes. The one real
assertion evaporates with the thing it is testing. Three `skipTest` gates in front of it
converted the remaining corpus-drift routes into silent stand-downs.

Measured (BEFORE, `git show HEAD`):

| injection | verdict |
|---|---|
| none (baseline) | GREEN (correctly) |
| `already_codified -> None` **(primary target)** | **GREEN, asserting nothing** |
| `already_codified -> {...}` (everything codified) | GREEN |
| `cluster_qualifies -> (False, ...)` | **GREEN, asserting nothing** |
| `cluster_hits -> []` | **GREEN, asserting nothing** |
| `scan_autopsy_file -> []` | **GREEN, asserting nothing** |
| `load_skill_lines -> []` | SKIP (silent stand-down) |
| `extract_salient_tokens -> set()` | SKIP (silent stand-down) |

Live state at audit time: 38 hits, 13972 skill lines, 8 candidates / 5 excluded / 12
sub-threshold, and the intersection that formed the sole assertion was `[]`.

**Repair.** Independent oracle plus guards that FAIL rather than skip; no assertion weakened:

- literal `SEED44_ARTIFACTS` frozenset, checked for presence against the **filesystem**
  (`glob` over `evidence/planning/`), never derived from `audit()`;
- `_live_inputs()` fails loudly on an absent corpus, zero hits, or zero skill lines,
  each with a "re-point this at a fixture corpus" instruction;
- new standalone `test_the_live_corpus_is_actually_loaded`, which additionally asserts the
  SCANNERS still see the two artifacts -- independent of what `audit()` later does with them;
- new POSITIVE assertion that the seed-44 pattern IS in `excluded_already_codified`
  (this is what catches the primary revert; the old intersection test could not);
- the original negative assertion retained unweakened.

Re-verified BOTH ways -- every previously-vacuous injection now RED, baseline still GREEN:

| injection | before | after |
|---|---|---|
| none | GREEN | **GREEN** |
| `already_codified -> None` | GREEN (vacuous) | **RED** |
| `cluster_qualifies -> (False, ...)` | GREEN (vacuous) | **RED** |
| `cluster_hits -> []` | GREEN (vacuous) | **RED** |
| `scan_autopsy_file -> []` | GREEN (vacuous) | **RED** |
| `load_skill_lines -> []` | SKIP | **RED** |
| `extract_salient_tokens -> set()` | SKIP | **RED** |
| `already_codified -> {...}` | GREEN | GREEN (see below) |

`already_codified -> {...}` (over-suppression) stays GREEN in both, correctly: the seed-44
artifacts are *supposed* to be excluded, so this class cannot discriminate that direction.
It is gated by the fixture partner `TestAuditEndToEnd.test_qualifying_uncodified_cluster_is_a_candidate`,
**verified RED** under the same injection.

### FINDING F2 -- `test_validate_literature.py::LiveCorpusTest`

The class is honestly documented as a crash-smoke ("it must run, not that it is clean"),
and asserting a finding COUNT here would rightly be wrong -- it would fail on every
legitimate literature pull. But "it must run" is only meaningful if it ran over
**something**, and the test could not tell 2213 records from 0:

    self.assertEqual(rc, 0, ...)                       # true on an empty corpus
    self.assertIn("validate_literature:", out.getvalue())  # true on an empty corpus

| injection | before | after |
|---|---|---|
| none (live corpus = 2213 records) | GREEN | **GREEN** |
| `iter_record_paths -> ([], [])` (tree renamed/empty) | **GREEN, asserting nothing** | **RED** |
| `collect_findings -> ([], 0)` (zero records) | **GREEN, asserting nothing** | **RED** |
| `collect_findings -> ([], 999)` (records, no findings) | GREEN | **GREEN** (correct) |

**Repair.** A record-COUNT non-vacuity guard, which is a statement about **coverage, not
cleanliness** -- it stays true after every legitimate literature pull however many findings
that pull produces. The last row is the load-bearing negative control: the fix must NOT
convert this into a cleanliness assertion, and it does not. Added a standalone
`test_the_live_corpus_is_actually_reachable` reading the count from `collect_findings`
directly, so a change to the report's output format cannot silently disarm the CLI guard.

### FINDING F3 -- `test_verify_literature_identifiers.py::TestReportOnlyKinds`

Same defect class, registry rather than corpus. Both tests iterate a registry owned by the
module under test, with no cardinality guard, so emptying either side runs the loop body
zero times:

    for check in V.CHECKS_REPORT_ONLY:            # empty -> body never runs
        ...
    for check in V.CHECKS_NETWORKED + V.CHECKS_OFFLINE:
        self.assertNotIn(check, V.CHECKS_REPORT_ONLY)   # vacuous if EITHER side empties

This matters in the direction the class itself names: a kind missing from `REPORT_ONLY_KINDS`
is printed as advisory while actually gating.

| injection | before | after |
|---|---|---|
| none | GREEN / GREEN | **GREEN / GREEN** |
| `CHECKS_REPORT_ONLY -> []` | **GREEN / GREEN** (both vacuous) | **RED / RED** |
| `REPORT_ONLY_KINDS -> set()` | GREEN / RED | GREEN / **RED** |
| `CHECKS_NETWORKED + CHECKS_OFFLINE -> []` | **GREEN** (vacuous) / GREEN | **RED** / GREEN |

**Repair.** The guard that `TestWaivers.test_every_waiver_states_a_reason` in the **same file**
already uses for `V.WAIVERS` (`self.assertTrue(V.WAIVERS)`) -- an in-file precedent, applied
to the two registries. `TestWaivers` is itself CLEAN for exactly this reason and is the model.

## 4. Suite state

`439 -> 441 passed, 20 subtests` across the six suites (+2 non-vacuity tests). No assertion
weakened, none removed. Landed `ed839b9771`.

## 5. UNRELATED pre-existing trunk failure -- reported, deliberately NOT fixed

`test_check_plan_status_table_sync.py::TestLivePlanningDir::test_a_reconciled_plan_reports_clean`
**fails on trunk**, before and after this work, and is not a vacuity finding -- it is the
checker working correctly:

    GAP-1  row 'Last updated' 2026-07-29 is OLDER than node last_updated 2026-08-18 (20 days behind)
    GAP-2  row 'Last updated' 2026-07-29 is OLDER than node last_updated 2026-08-18 (20 days behind)
    GAP-6  row 'Last updated' 2026-08-15 is OLDER than node last_updated 2026-08-18 (3 days behind)

Cause: `b289311feb` ("steward D-007: re-point self_attribution GAP-1/GAP-2/GAP-6 frontmatter
gates at the LIVE blocker") bumped the frontmatter `last_updated` on those three nodes without
updating the status-table rows in `evidence/planning/self_attribution_plan.md`. The fix is to
reconcile the three rows in that plan -- **owned by the steward D-007 work, not by this sweep**,
and the chip's standing instruction is not to weaken an assertion to make it pass.

## 6. Standing lesson (extends the IGW sweep's)

The IGW sweep's lesson was: helpers that **fail open by design** hand their fail-open to any
test that reads their output as an oracle. This sweep adds two more routes to the same defect,
neither of which involves a fail-open loader:

- **A filter over the function's own output is an oracle taken from the function under test.**
  `{x for x in f(corpus) if <pattern>}` is not an independent oracle, however specific the
  pattern looks. Name the expected members as LITERALS and check their presence against raw
  data. `if X: assert X` is a tautology, not a guard.
- **Iterating a registry owned by the module under test needs a cardinality floor.** An empty
  `for` body and a passing test are indistinguishable. This applies to `assertNotIn` loops in
  both directions -- an emptied registry on EITHER side of the membership test is vacuous.

And the general rule from both sweeps holds: an `assertNotIn` / `assertEqual([], ...)` test may
legitimately be vacuous **provided a partner asserts the positive direction over the same
helper**. Three of the six suites here were clean for exactly that reason.
