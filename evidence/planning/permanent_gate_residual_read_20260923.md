# Residual registry-blocked row read -- permanent-block sweep, closing tranche

**Session** exciting-morse-761f4a (chip-20260923-permanent-gate-residual-read-v2)
**Date** 2026-09-23T06:38:26Z
**Outcome** ZERO further permanent blocks. No `experiment_gate` written. claims.yaml unchanged.

## What this closes

Half A of user ruling rec-20260923-4e4795c2 (backfill claims.yaml `experiment_gate` from the
proposals registry), narrowed by rec-20260923-ebd1895f to PERMANENT BLOCKS ONLY. Two tranches had
already landed on REE_assembly master:

* `dd9f368110` -- the 7 claims whose registry row carries `status=gated`.
* `e411012039` -- ARC-120 and IMPL-023, the two permanent blocks found by reading candidates.

Those two tranches read only 14 of the 119 registry-blocked claims that lacked a gate, and the
shortlist came from three independently-phrased text sweeps over `release_condition` /
`blocked_note` / `gating_reason`. Every new phrasing found something the previous ones missed
(sweep 2 found ARC-073 / MECH-054 / SD-039; sweep 3 found ARC-121), which is the signature of an
unreliable denominator. This session read the remaining rows directly instead of sweeping them.

## Denominator, measured from `origin/master` (not the shared dirty worktree)

| Quantity | Count |
|---|---|
| Claims FILTER G reports blocked (`proposal_feasibility.load_proposal_block_index`) | 130 |
| Of those, already carrying `experiment_gate` | 13 |
| Blocked and ungated | 117 |
| Already read by the prior tranches (judged releasable) | 13 |
| **Read in full by this session** | **104** |

Blocking status over the 104: `blocked_substrate` 99, `deferred_substrate_not_ready` 4,
`proposed_blocked_substrate` 1.

Read scope was stronger than the chip's own recipe: FILTER G's index keeps only the FIRST blocking
proposal per claim, so this session enumerated EVERY experimental proposal row per claim
(115 rows over the 104 claims) and read `release_condition`, `blocked_note`, `gating_reason` and
`blocked_by` on each.

## Verdict

**90 of the 104 carry gating prose, and every single one names a condition that would release it.**
Named release triggers, in rough order of frequency: a named substrate build routed to
`/implement-substrate`; an upstream claim or substrate_queue entry reaching validated; a specific
EXQ landing or being adjudicated; a governance adjudication or claim narrowing; a multi-agent /
language / V4-V5 substrate landing. Under the governing principle -- `experiment_gate` owns
PERMANENT blocks, FILTER G owns RELEASABLE ones -- none of these may be gated. A static gate on a
substrate-releasable claim converts a self-releasing block into a permanent silence that nothing
detects, because `experiment_gate` has no programmatic writer and no auto-release.

Claims read and judged RELEASABLE (90):

```
ARC-003, ARC-008, ARC-019, ARC-044, ARC-048, ARC-055, ARC-078, INV-040, INV-044, INV-051
INV-060, INV-063, INV-064, INV-065, INV-072, INV-086, INV-092, INV-093, INV-095, INV-104
MECH-002, MECH-003, MECH-004, MECH-006, MECH-011, MECH-012, MECH-013, MECH-014, MECH-016
MECH-018, MECH-019, MECH-023, MECH-024, MECH-028, MECH-031, MECH-034, MECH-035, MECH-037
MECH-038, MECH-039, MECH-042, MECH-043, MECH-044, MECH-048, MECH-049, MECH-050, MECH-053
MECH-057b, MECH-064, MECH-065, MECH-066, MECH-067, MECH-077, MECH-085, MECH-088
MECH-127, MECH-140, MECH-142, MECH-151, MECH-160, MECH-170, MECH-178, MECH-179, MECH-182
MECH-184, MECH-191, MECH-192, MECH-193, MECH-203, MECH-213, MECH-221, MECH-222, MECH-228
MECH-236, MECH-251, MECH-255, MECH-269, MECH-330, MECH-333, MECH-426, MECH-470, MECH-471
MECH-474, MECH-494, MECH-495, MECH-561, Q-061, Q-064, Q-081, SD-086
```

Five rows were the closest calls and are recorded so a successor does not re-adjudicate them:

* **MECH-474** -- explicitly "NOT ROUTABLE TO /implement-substrate AS-IS" (a write-enabled
  counterfactual regime would contradict MECH-094, status stable). RELEASABLE anyway: the row names
  the releasing move, a governance narrowing of the four-regime menu to three, and states the design
  is buildable as a 3-regime falsifier the moment that lands.
* **MECH-142** -- "This is not a buildable gap", but names (A) build orthogonal axes or (B) reframe
  onto an already-orthogonal channel pair as the governance decision that releases it.
* **MECH-151** -- routes to a governance adjudication of ARC-007 with two named outcomes, one of
  which retires the proposal. A condition is still named.
* **MECH-140** -- "NO NEW BUILD is owed ... Do NOT /implement-substrate", and ARC-110's segregated-loop
  conversion ceiling is called INTRINSIC. Still releasable: the row names a validation
  (GAP-A lift generalisation at the segregated-loop locus with a valid same-layer null).
* **MECH-561** -- "This status is never auto-cleared -- a session must clear it deliberately once
  (a)-(c) hold." Never AUTO-cleared is not permanent; (a)-(c) are named and ride on V3-EXQ-1043a.

## The 14 that cannot be judged at all -- cannot-determine, NOT permanent

Fourteen rows carry a blocking status with **no `release_condition`, no `blocked_note` and no
`gating_reason`** -- nothing to read:

```
ARC-049, ARC-063, ARC-064, ARC-071, INV-056, INV-089, MECH-141, MECH-183, MECH-197
MECH-312, MECH-343, Q-019, Q-088, SD-092
```

Twelve are auto-minted generic `claim_probe_*` rows (`dispatch_mode: targeted_probe` or
`discriminative_pair`, boilerplate `objective`) whose status was set with no recorded reason.
Two are manual rows: MECH-343 carries a `blocked_by` naming two owned substrate_queue entries
(`modulatory-bias-selection-authority`, SD-061), i.e. releasable by build; Q-019 carries
`blocked_by: []` -- literally an empty blocker list under `status: blocked_substrate`.

**These were deliberately NOT gated.** "The row names no releasing condition" is satisfied
vacuously by a row that names nothing, and reading it as PERMANENT would gate on the ABSENCE of
information -- the negative-instrument failure CLAUDE.md's "General Rules" section names: nothing
found must not read the same as the search broke. Gating them would convert an unaudited, reasonless
suppression into a permanent one.

No claim_type pre-filter was applied (settled, per `scripts/proposal_routine_tick.py`), and none of
the 14 is an `implementation_note` or `reference_note` -- the one shape (IMPL-023 / IMPL-026 /
IMPL-027) where a gate is defensible without prose.

## Residual gap this read exposes, and what it is NOT

The 14 reasonless rows are a live hole in FILTER G's own denominator. FILTER G blocks on `status`
alone, so each of these suppresses proposal minting for its claim with no auditable reason and no
release predicate -- and because there is no condition recorded, there is nothing any readiness
audit can ever check to release them. `audit_blocked_proposal_unblockers.py` reasons over named
unblockers; a row naming none is invisible to it.

The fix is NOT an `experiment_gate` (that is the wrong instrument, per above) and not a text sweep.
It is for `/governance` to give each of the 14 either a recorded release condition or an explicit
permanent disposition. **Routed as GFLAG-0424** (`stale_note`, naming all 14 claim ids,
REE_assembly `bead1094ea`) rather than chipped: giving a registry row a disposition is governance's
own work, and a flag lands in the worklist governance re-derives each cycle instead of becoming a
second, staler tracker. Not actioned here.

## State after this session

`experiment_gate` count on REE_assembly `origin/master` is UNCHANGED at 13:
ARC-112, ARC-113, ARC-120, ARC-130, IMPL-023, IMPL-026, IMPL-027, MECH-177, MECH-334, MECH-465,
SD-032a, SD-056, SD-099.

Half A of rec-20260923-4e4795c2, as narrowed by rec-20260923-ebd1895f, is now COMPLETE: every
registry-blocked claim lacking a gate has been read in full, and the permanent set is closed at 13.
