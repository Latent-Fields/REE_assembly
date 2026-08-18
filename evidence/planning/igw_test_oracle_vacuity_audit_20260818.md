# IGW generator test suites -- oracle-vacuity audit by fault injection

**Date:** 2026-08-18
**Chip:** `chip-20260816-igw-test-oracle-vacuity-audit`
**Method precedent:** FM11d, `test_backfill_failure_record_run_role.py` (REE_assembly `48bae8be81`)

**Status: COMPLETE. The one finding is FIXED and landed; nothing here is awaiting user action.**

## Question

FM11d was a test whose *oracle came from the function under test*: it built its set of
"non-post_build run stamps" by calling `G._failure_record_run_role()`, so reverting that
function emptied the set and every `assertNotIn` passed against nothing. Both halves of the
fix were ungated on trunk and nobody knew.

Does the same shape exist in the other six IGW generator suites?

## Method

For each suite, the predicate/normaliser helpers in `generate_inter_governance_workset.py`
it leans on were monkeypatched to their plausible pre-fix / degenerate return (constant
`True`, constant `False`, empty collection, identity), the test module re-imported, and every
case re-run. **A test that stays GREEN under a revert it is supposed to catch is the finding.**

42 (suite x helper x degenerate) injections were run. Raw results and the harness are
reproducible from the method above; the discriminating outcomes are recorded below.

## Result: 5 of 6 suites CLEAN, 1 finding

### Clean, and why -- these are negative results, stated so they are not re-audited

| Suite | Why it is immune |
|---|---|
| `..._blocked_substrate` | Fully fixture-driven (tempdir `claims.yaml` / `substrate_queue.json` / proposals). Literal oracles, `assertIsNotNone(item)` presence guards, and a positive control (`test_without_blocked_substrate_proposal_same_claim_renders_ready` asserts `ready`) that goes red on over-blocking. |
| `..._proposal_lane` | Fully fixture-driven; asserts exact `(lane, skill)` tuples against literals, with `assertIn` presence guards. |
| `..._confirmer_adjudication` | `_LaneFixture`-based. `test_mech_203_is_NOT_covered...` is an `assertNotIn`, but carries its own `assertIn("MECH-203", by_cid)` presence guard, and its partner `test_mech_191_carries_its_adjudication` goes RED under `_confirmer_adjudicated_proposals -> {}`. The pair is gated. |
| `..._experiment_lane_staleness` | Fixture literals (`STALE_WORKTREE_QUEUE`, `INCIDENT_QUEUE`) passed directly into the helpers, plus tempdir git repos. `test_stale_worktree_alone_misses_the_queued_work` is vacuous under `_confirmer_queued_claims -> set()`, but its partner `test_merged_snapshot_sees_all_of_it` asserts `assertIn` on the same helper and goes RED. Gated. |
| `..._synthesis_lane_staleness` | `_FixtureQueue`-based, and it **already carries an explicit non-vacuity partner**: `NoBuildLandedSubstrateIsOfferedAnywhereTest.test_the_invariant_is_actually_exercised` fails when the live corpus stops containing a build-complete entry. Verified RED under `_substrate_by_id -> {}`. This is the model the finding below was repaired against. |

The recurring correct pattern: an `assertNotIn`/`assertEqual([], ...)` test is allowed to be
vacuous **provided a partner test asserts the positive direction over the same helper**.

### FINDING -- `..._substrate_staleness.py::LiveSubstrateQueueTest`

The suite's *fixture* class (`ConfirmedIncidentReplayTest`) is correctly gated: its negative
control asserts an exact expected list, so over-suppression goes red. The suite's **live-corpus**
class was not. Both its tests built their oracle from `_substrate_ready_items()` /
`_substrate_by_id()` over the live `substrate_queue.json`, with no non-vacuity guard.

The emptying route is `_load_substrate_queue()`, which **fails open** -- returns `[]` on a
missing, renamed or unparseable file. Correct for the generator (a broken input must not wedge
the workset); fatal for a test reading its output as an oracle.

Verified by injection -- **both tests GREEN while asserting nothing**:

| corpus state | live entries | `ready` | `test_no_landed_incident_item_is_ready` |
|---|---|---|---|
| as-is (today) | 160 | 4 | GREEN (correctly) |
| queue file MISSING | 0 | 0 | **GREEN, asserting nothing** |
| queue empty (`queue: []`) | 0 | 0 | **GREEN, asserting nothing** |
| queue file UNPARSEABLE | 0 | 0 | **GREEN, asserting nothing** |
| the 5 incident ids REMOVED | 155 | 4 | **GREEN, asserting nothing** |

`test_scaffolded_curriculum_rebalance_is_resolved` additionally used `skipTest` on a missing
entry -- a silent stand-down indistinguishable from the fix having been reverted.

Not yet a live defect: all five incident ids are present and build-complete today, and the
tests *do* currently go RED under their primary target revert. But the live `ready` set holds
only **4** items -- one governance pass from 0, at which point the class asserts nothing and
would never say so.

## Repair

Independent oracle + non-vacuity guards, no assertion weakened:

- `setUpClass` parses `substrate_queue.json` **raw** (`json.loads`), calling no generator
  helper, so a parse failure surfaces as a failure rather than as an empty oracle.
- `_assert_corpus_loaded()` -- an empty oracle is a FAILURE in this class, never a quiet pass.
- New `test_the_live_corpus_is_actually_loaded` -- standalone, and cross-checks the raw entry
  count against the generator's own loader so a silent drop on either side is caught.
- Per-id presence asserted against the raw file, and the status compared to a **literal**
  `BUILD_LANDED_STATUSES` frozenset -- deliberately *not* derived from
  `_status_implementation_complete()`, which is the predicate under test.
- `skipTest` -> loud failure carrying a "re-point this test at a fixture corpus" instruction,
  following the synthesis suite's precedent.

### Re-verified by injection BOTH ways

| injection | before fix | after fix |
|---|---|---|
| queue MISSING / empty / UNPARSEABLE | GREEN (vacuous) | **RED** |
| 5 incident ids removed | GREEN (vacuous) | **RED** (`no_landed` only -- correctly scoped) |
| scaffolded id removed | GREEN (skipped) | **RED** (`scaffolded` only) |
| `_substrate_implementation_complete -> False` (FM3 pre-fix) | RED | **RED** (preserved) |
| `_status_implementation_complete -> False` | RED | **RED** (preserved) |
| `_status_resolved -> False` | RED | **RED** (preserved) |
| `_substrate_resolved -> False` | RED (`scaffolded`) | **RED** (preserved) |
| no injection, clean corpus | GREEN | **GREEN** |

Over-suppression (`-> True`) remains gated by the fixture partner
`ConfirmedIncidentReplayTest.test_pre_stopgap_board_still_surfaces_the_genuinely_unbuilt`,
confirmed RED in both directions.

Suite: 20 -> 21 tests. All six suites green: **113 passed, 35 subtests** (was 112).
`..._completed_retest.py` re-run as a regression check: 60 passed.

## Standing lesson

The generator's helpers **fail open by design**. Any test that reads their output as an oracle
inherits that fail-open as *silent vacuity*. Such a test needs either a partner asserting the
positive direction over the same helper, or an oracle read independently of it -- raw committed
data or a literal.
