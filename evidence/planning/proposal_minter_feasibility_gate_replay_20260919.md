# Proposal minter feasibility gate -- held-out replay, 2026-09-19

Recorded 2026-09-19T10:36:58Z by session `elated-chandrasekhar-4a6e6a`, working
`chip-20260918-proposal-minter-feasibility-gate-and-backfill-tier` (USER DIRECTION 2026-09-18:
"the minter must only mint experiments which are actually possible given the substrate").

The chip made **validation the deliverable, not the filter**: replay every candidate cheap
signal against refused and succeeded proposals, keep only what separates them, and say so
plainly if nothing does. **Nothing cheap does.** What shipped is the pair that are loop-breakers
by construction. Code: `REE_Working/scripts/proposal_feasibility.py` (predicates + cache writer),
wired into `proposal_routine_tick.py` and `proposal_backlog_dripfeed.py`.

## Held-out sets

Built from the chip ledger (`chip_ledger.load_chips()`, archived fields read through
`chip_ledger.archived_field`), all 593 `chip-proposal-*` chips ever recorded
(402 withdrawn / 111 done / 80 open at measurement).

- **REFUSED (substrate)** -- 71 claims. A chip carrying an explicit
  `PRE-FLIGHT / PRODUCER-TRACE / MEASURED VERDICT: RED` whose reason is not a missing
  falsifier or "already answered", plus `done` chips resolved to a `blocked_substrate` /
  `deferred_substrate_not_ready` disposition, plus the chip's eight named lineages (ARC-046,
  MECH-465, ARC-057, MECH-467, INV-095, SD-033d, MECH-237, SD-024).
- **SUCCEEDED** -- 19 claims. `done` chips whose proposal reached `queued` / `executed`, plus
  the six claims behind the chip's named successes: SD-077 (V3-EXQ-1040), SD-074 (784a),
  SD-106 (1041), MECH-482 (964b), SD-082 (1046), SD-098 (1055). V3-EXQ-1044 carries no
  `claim_id` on its queue entry and is not joinable.
- Five claims appear in BOTH (MECH-162, -439, -464, -467, -489) and are excluded from the
  per-signal table below; they are what the time-aware replay further down is for.

## Per-signal result

| signal | caught REFUSED (of 71) | WRONGLY BLOCKED SUCCEEDED (of 19) | shipped |
|---|---|---|---|
| E -- claim has no `what_would_answer` | 38 | **10** | **yes -- USER DECISION**, see below |
| a -- recorded RED verdict on a prior chip for the claim (time-aware, as implemented) | see below | **0 of 23 mints** | **yes (FILTER F)** |
| a' -- claim has a `blocked_substrate` proposal disposition | 36 | 2 (ARC-019, MECH-471) | no -- 0 live effect: no claim today has both a blocked and a still-`proposed` experimental item |
| b -- own claim has build-outstanding substrate_queue entry | 2 | 2 (MECH-428, SD-098) | no |
| b -- TRANSITIVE `depends_on` has build-outstanding entry | 34 | **11** | no |
| b -- own claim has `ready: false` entry | 7 | 1 (SD-098) | no |
| b -- TRANSITIVE `depends_on` has `ready: false` entry | 44 | **12** | no |
| b -- `v3_pending` | 0 | 1 (MECH-482) | no |
| b -- TRANSITIVE `depends_on` has a blocked-disposition proposal | 67 | **14** | no |
| `pending_retest_after_substrate` set | 5 | 9 (of 24 incl. BOTH) | no |
| `pending_substrate_reconfirmation` set | 3 | 0 | no -- catches almost nothing |
| c -- mechanism behind a default-off config flag | -- | -- | **not computable cheaply**, see below |

"Build-outstanding" reuses `substrate_queue_writeback_drift.entry_asserts_build_outstanding`
rather than a new status parser (substrate_queue `status` is free-form prose on ~40 entries).

**Why (b) fails.** The `depends_on` graph is dense: most claims reach *some* unlanded
substrate_queue node, so reachability does not separate feasible from infeasible. It closes
FILTER B's stated gap (the EXP-0662 / INV-024 shape) only by also closing V3-EXQ-1046, -1055
and -964b. The own-claim variants fail for a structural reason: an entry that owes
**validation** is validated *by* the experiment -- SD-098's entry was `ready: false` because
V3-EXQ-1055 had not run yet. Own-claim substrate debt is frequently the opposite of infeasible.

**Why (c) is not computable.** `claims.yaml` has no claim->flag field (field survey: no key
matching flag/config/default/enabl). Comment-derived attribution from `ree_core/utils/config.py`
is a documented false-positive source (MECH-104 / `use_phasic_burst`,
`default_off_drift_audit_2026-07-21.md`); ~288 knobs default `False` while the experiment
harness sets them on, so "defaults off" is noise; and a proposal does not declare its flags --
the *design* does, after minting. Inertness at production defaults is what a producer trace
finds. It belongs in the cache (d), recorded by the session that ran the trace.

## FILTER F as implemented -- time-aware replay

Each historical mint is replayed against only the verdicts recorded **before** its
`spawned_at`, with substrate_queue landings as-of that time.

- **Known-good mints wrongly blocked: 0 of 23** (17 ledger mints + the 6 named).
- **Refused mints it would have prevented: 2 of 61** (MECH-384 `exp-1011`, MECH-469
  `exp-1072`). Small, and honestly so: explicit verdict lines only began on 2026-09-10, and
  most refusals in the record are the *first* for their claim. A broader disposition-based count
  finds 23 of 95 refused outcomes were re-mints after an earlier refusal of the same claim
  (MECH-467 x3, MECH-426 x2, MECH-037 x2, ...), but that cohort is dominated by the 2026-09-02
  positional-proposal-id mass-mint and is contaminated in exactly the way
  `proposal_backlog_dripfeed.DEFAULT_FLOOR`'s comment already records.
- **Forward effect: 36 claims** carry an unreleased substrate-RED today and can no longer be
  re-minted under a regenerated EXP id. Live dry-run: `EXP-0662` (INV-024) and `EXP-1390`
  (ARC-057), both still `proposed`, both now skipped.
- **Named refused lineages, today:** ARC-057, INV-095, MECH-237, MECH-467, SD-033d blocked by F
  (MECH-237 / MECH-467 also by E, SD-033d also by D). ARC-046 and MECH-465 have no open
  experimental proposal -- nothing to mint. **SD-024 is NOT covered**: its PRODUCER-TRACE RED
  is a governance-ratification hold recorded on a non-proposal chip
  (`chip-20260915-sd024-standing-density-redesign`), which F deliberately does not read, and
  EXP-1391 stays mintable. Owed: the Orchestrator records it with
  `proposal_feasibility.py record` (it is its verdict to transcribe, not this session's).

**A bug the replay caught.** The first implementation ordered one chip's verdicts by their
timestamps. The superseding MEASURED RED on `exp-0944-paced` (MECH-237), `exp-0720` (INV-095)
and `exp-1176-paced` (SD-033d) carries a date-only or malformed stamp (`Recorded 2026-09-15 by`,
`06:5xZ`), so it tied with the older AMBER beneath it and the AMBER won -- three of the eight
named lineages read as feasible. Verdicts are PREPENDED, so prompt order is now the authority
within a chip (`current_chip_verdict`). A second, smaller one: a RED that merely *cites*
`what_would_answer` (SD-033d: the field forbids a run) was being ignored as a no-falsifier RED;
the detector now matches the Orchestrator's actual wording.

**What F pins.** Blocking is by claim, and a chip verdict can only be superseded by a verdict
on a newer chip for that claim -- which the block prevents from being minted. 30 of the 36
pinned claims appear in no substrate_queue `unblocks_claims`, so for them the cache is the only
release: a recorded GREEN re-trace, or the RED re-recorded with a producer path.
`proposal_feasibility.py pinned` lists them.

## FILTER E -- the measured cost of a decision already made

The user decided on 2026-09-18 that the minter skips claims with no falsifier; it is
implemented as decided. The replay shows what it costs, which was not known when it was
decided: **10 of the 19 succeeded claims have no `what_would_answer` today** -- MECH-143,
MECH-144, MECH-161, MECH-471, SD-009, SD-074, SD-075, SD-077, SD-082, SD-106 -- including four
of the six joinable named successes. Those designs were derived from the claim's notes and
substrate_queue validation specs, not from a registered falsifier.

The filter is still coherent *given* pre-flight question (g), which since 2026-09-16 RED-marks
exactly these claims one stage later, at the cost of a pre-flight each and (before that) an
Opus design pass. But the two together now exclude a class of proposal that historically ran
and produced evidence. Live effect: 101 of 169 `proposed` experimental items back a claim with
no falsifier; the mintable pool is 15. The lever is falsifier authoring (`/governance`,
`queuefloor_recurrence_rootcause_staged_20260915.md` P4), and SD-type claims are the obvious
first tranche: 5 of the 10 are `SD-*`, whose substrate_queue entry usually already states the
validation experiment. Raised as a `kind: decision` chip rather than softened here.

## Part 1 cleanup performed

41 OPEN, UNCLAIMED `chip-proposal-exp-*` chips backed a no-falsifier claim (0 were claimed).
39 withdrawn via `chip_ledger.py resolve --status withdrawn`, each note naming this chip and
stating the proposal stays in the registry. **2 left open and reported**, because they carry a
pre-flight AMBER (judged queueable with a named change) and a withdrawal is irreversible:
`chip-proposal-exp-1222-paced` (SD-086) and `chip-proposal-exp-0878-paced` (MECH-131).

## Reproduce

Scratch replay scripts were session-local. The shipped predicates are importable:
`proposal_feasibility.verdict_events_by_claim`, `recorded_infeasibility_reason`,
`pinned_claims`. Re-run the per-signal table before re-adding any dropped signal.
