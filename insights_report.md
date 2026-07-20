# Project Insights — 2026-07-20

Generated: 2026-07-20T06:31:52Z
Corrected: 2026-07-20T07:58Z — see **Corrections** below before acting on any recommendation.

---

## Corrections (applied 2026-07-20T07:58Z)

Verification against the live queue, `TASK_CLAIMS.json` and recent autopsies found **four of this
report's conclusions wrong**. They are corrected here rather than silently rewritten.

**1. The "stalled chains" finding was wrong on three of four counts.** The report applied the
skill's own continuity caveat ("a successor under a NEW number is still a successor") to the
*historical* chains and then failed to apply it to the current ones. Checking only for a
same-base successor in the queue is exactly the error that caveat exists to prevent.

| Claim | Report said | Actually |
|---|---|---|
| MECH-463 | dead, no successor | **Live campaign.** V3-EXQ-785 autopsied and superseded; successor **V3-EXQ-787** queued under a new number, itself autopsied, `H-endogenous-hazard-geometry` ELIMINATED; lit-pull 2026-07-20 raised `lit_conf` 0 -> 0.747. 8 task claims. |
| INV-088 | dead, no successor | **Owned.** Substrate-plane owner recorded plus a live SD-070/783 clearing path; `mech457_retention_trajectory_probe` written up AND implemented (ree-v3 `7e4f6e932b`). 7 task claims. |
| INV-089 | decision owed | **Decision already recorded.** Four autopsies, including a dedicated `failure_autopsy_INV-089-INV-090-wellposedness_2026-07-16`. The chain 743 -> 746 -> 746a/b/c was adjudicated, not dropped. |

Only the *shape* of the original observation survives: these chains have no same-base successor.
That is not evidence of abandonment, and should not have been reported as such.

**2. Recommendation 1 is superseded.** `failure_autopsy_V3-EXQ-604c_2026-07-20` (status
`confirmed`) landed at ~06:37Z, six minutes after this report generated, and resolves MECH-314:

- **MECH-314 (parent) and MECH-314a: `supports` STANDS. No substrate work is owed.** The run
  succeeded; the D3 divergence flag was withdrawn.
- **MECH-314b / MECH-314c: `non_contributory`.** Uncertainty and learning-progress are global
  scalars broadcast across the K candidates, so a delta of 0.0 is an arithmetic identity, not a
  measurement. They are behaviourally inert at selection *by construction* and untestable by any
  selection-level DV.
- The named remedy is an **`amend` on ARC-065** (give 314b/314c the per-candidate treatment
  MECH-314a already has) — **not** `modulatory-bias-selection-authority`, which this report
  nominated. That amend is confirmed and **not yet applied** to `substrate_queue.json`.
- The **re-derive brake FIRES** (ceiling-hits 3/3/3 against a threshold of 2). A further
  same-claim ablation is **REFUSED** — it would return 0.0 deterministically. A DV swap alone is
  not a viable escape either.

So MECH-314's July failure volume is substantially a **measurement-instrument defect**, not the
substrate starvation this report inferred from the raw FAIL count. In work-graph terms the node
is `complex (probe-gated)` with the probe already run, not `complicated (buildable)`.

**3. What still stands.** The experiment-health numbers, the data-source caveat (the ERROR-rate
blind spot), the substrate ready/blocked counts, the literature finding (zero open items), the
queue-composition finding (7 of 10 are re-letter re-runs), and recommendation 4. Recommendation 3
is discharged — the zworld encoder guard was verified sound (9/9 contracts).

**Method note for the next run of this skill:** claim-level FAIL counts are a *starting point*,
not a finding. Before calling any claim stalled, check `TASK_CLAIMS.json` (including `done`
entries with completion notes), recent autopsies, and successors under new EXQ numbers. A high
FAIL count against a claim whose parent reads `supports` usually means a vacuous criterion, not a
missing substrate.

---

## Experiment Health

**Data-source caveat (read before using the numbers below).** Two sources disagree and
neither alone is sufficient:

- `runner_status.json` is **stale** — `last_updated` is `2026-06-09T06:00:15Z`, 41 days
  behind. Under Phase 3 the coordinator DB + `phase3:` manifest writers are authoritative;
  `runner_status.json` is no longer being maintained. It is used below **only** for the
  historical ERROR rate.
- Evidence manifests (3211 with a `run_id`) are current through `2026-07-19T235543Z`, but
  **cannot measure the ERROR rate at all**: an ERROR is a crash *before* the manifest is
  written, so ERROR runs are structurally invisible to a manifest scan. The `error_rate=0.0%`
  a naive manifest scan reports is an artifact, not a finding.

**Historical outcome mix** (runner_status, 840 completed entries through 2026-06-09):

| Result | Count | Share |
|---|---:|---:|
| PASS | 283 | 33.7% |
| FAIL | 437 | 52.0% |
| ERROR | 87 | **10.4%** |
| UNKNOWN | 32 | 3.8% |
| INCONCLUSIVE | 1 | 0.1% |

**Current outcome mix** (manifests, PASS/FAIL only — ERROR not observable):

| Window | n | PASS | FAIL | PASS rate |
|---|---:|---:|---:|---:|
| Since 2026-06-01 | 866 | 297 | 565 | 34.3% |
| Since 2026-07-01 | 584 | 214 | 366 | 36.6% |

PASS rate is stable at ~34-37% across both windows and matches the all-time 33.7%.
There is no recent regression in experiment yield — this is the project's steady state.
(119 distinct runs carry a July timestamp; the 584 figure counts all manifests written
in July, including re-emissions.)

### High-iteration chains (July, >=3 distinct letters)

| Chain | Iters | Outcomes | Claims |
|---|---:|---|---|
| EXQ-778 | 9 (`-,a..h`) | PASS,PASS,FAIL,FAIL,FAIL,FAIL,PASS,PASS,PASS | INV-047, MECH-168, MECH-169, SD-068 |
| EXQ-746 | 4 (`-,a,b,c`) | FAIL,FAIL,FAIL,FAIL | INV-089 |
| EXQ-733 | 3 (`-,b,c`) | FAIL,PASS,PASS | MECH-456 |
| EXQ-785 | 3 (`-,a,b`) | FAIL,FAIL,FAIL | MECH-463 |

EXQ-778 is a **healthy** long chain — it converged (last three iterations PASS). EXQ-746
(INV-089, 4/4 FAIL) and EXQ-785 (MECH-463, 3/3 FAIL) are the two that iterated without
converging, and **neither has a successor queued**.

Historical worst chains, for context — these are the ones the continuity caveats exist for:
`EXQ-085` (14 iters, 14 FAIL, MECH-071), `EXQ-514` (13, SD-049), `EXQ-418` (13, SD-016/017),
`EXQ-543` (10), `EXQ-490` (10). Per the skill's attribution caveat, the letter count on these
is **not** a per-claim indictment — EXQ-085's later letters re-tagged away from MECH-071.

### Claim FAIL concentration (July, excluding `non_contributory`/`superseded`)

| Claim | July FAILs | Queued successor? |
|---|---:|---|
| **MECH-457** | 13 | Yes — V3-EXQ-789 (prio 55), 742a (claimed) |
| **MECH-314** | 8 | **No — nothing queued** |
| INV-088 | 4 | No |
| INV-089 | 4 | **No** (EXQ-746 chain dead at `c`) |
| MECH-463 | 4 | **No** (EXQ-785 chain dead at `b`) |
| MECH-095 | 3 | No |

MECH-457 and MECH-314 together account for **21 of July's claim-attributed FAILs** — more
than the next ten claims combined.

### Rework volume

29 July manifests carry a `supersedes` field; 45 per-claim `evidence_direction` entries are
marked `superseded` or `non_contributory`. Roughly a quarter of July's runs are corrections
of earlier runs rather than new questions.

---

## Substrate Bottlenecks

Substrate queue: **118 entries**, 56 `ready: true` / 62 `ready: false`.

**Ready and not yet implemented: 17.** Priority-1 entries, ordered by claims unblocked:

| SD | Unblocks | Failure records |
|---|---:|---:|
| `scaffolded_sd054_onboarding` | 20 claims | 28 |
| `modulatory-bias-selection-authority` | **18 claims** | **15** |
| `sd_actor_critic_action_learning` | 3 (incl. MECH-457, f_dominance ceiling) | 1 |
| `crf-availability-maintenance` | 3 | 5 |
| `rebinding-harness-p0-coverage-decoupling` | 1 (MECH-456) | 1 |
| SD-047 | MECH-098, MECH-099 | 0 |
| SD-048 | ARC-058, ARC-033, ARC-061 | 0 |
| MECH-302 | MECH-302, MECH-303 | 0 |
| `mech457_consummatory_act` | MECH-457, INV-088 | 0 |

**Blocked (`depends_on_unresolved`): 37**, dominated by the SD-026/027/028 and SD-033*
clusters — SD-033 alone waits on 7 unresolved claims, and SD-033b/c/d/e each wait on SD-033
plus more.

**Highest failure-record counts** (experiments that failed citing a missing/incomplete SD):
`scaffolded_sd054_onboarding` 28, `f_dominance_conversion_ceiling` 26,
`modulatory-bias-selection-authority` 15, `ARC-062` 11, `v4_loop_segregation` 10,
`MECH-256` 10, `SD-049-PHASE-2` 9.

**The key cross-reference.** The two claims driving July's FAIL volume both map onto
priority-1 substrate that is marked `ready: true` and is *not* implemented:

- **MECH-314** (8 FAILs, nothing queued) → `modulatory-bias-selection-authority`,
  `ready: true`, prio 1, **15 failure records**, unblocks 18 claims.
- **MECH-457** (13 FAILs) → `sd_actor_critic_action_learning` (`ready: true`, prio 1) and
  `mech457_consummatory_act` (`ready: true`, proposed). Its third entry,
  `mech457_competence_bootstrap_explorer`, is `blocked_pending_discrimination` with 6
  failure records — i.e. the blocked path is the one that has been absorbing the failures.

> Caveat on the two entries above: both carry `status: implemented` while
> `implementation_status` is null and `ready: true`. The fields disagree. Treat "ready and
> not implemented" as *needs a human readiness call*, not as a settled build order.

---

## Governance State

- Claims with `v3_pending: true`: **224**
- Claims with `implementation_phase: v3`: **328**
- Pending experiment review: **1** item — `v3_exq_785a_mech463_arousal_exogenous_urgency_decomp_...` (FAIL, MECH-463). Review backlog is effectively clear.
- Evidence rework (July): 29 manifests with `supersedes`, 45 `superseded`/`non_contributory` per-claim directions.
- Queue depth: **10 items** — 4 claimed, 6 pending. **7 of 10 are re-letter re-runs**
  (708a, 742a, 737a, 728a, 734a, 699a, 699b); only 789/790/791 are new questions. Four of
  those re-runs (742a, 737a, 728a, 734a) are the *same* correction — "re-run under the
  zworld encoder guard".

---

## Literature Coverage

`evidence_backlog.v1.json` holds **362 items**, of which **361 need `experimental`
evidence and exactly 1 needs `literature`** — and that one is already `covered`.

- Priority-1 literature items still open: **none**
- Total open literature items: **0**

Literature is **not** a bottleneck for this project right now. The backlog is almost purely
experimental: 141 `open`, 160 `in_progress`, 61 `covered`. The 37 `lit-pull` mentions in
recent session history reflect work already absorbed, not outstanding demand.

---

## Human-Intervention Patterns

Session-type frequency across the last ~400 lines of `WORKSPACE_STATE.md` (mention counts,
so indicative rather than exact session counts):

| Activity | Mentions |
|---|---:|
| governance | 266 |
| autopsy / failure-autopsy | 168 / 85 |
| queue-experiment | 91 |
| implement-substrate | 56 |
| lit-pull | 37 |
| claim-synthesis | 34 |
| update-docs | 27 |
| morning-digest | 17 |

Friction markers in the same window: `BLOCKED` 82, `STALE` 76, `REFUSED` 23, `SWEPT` 17,
`substrate_not_ready` 17, `CONTAMINATION` 5, `WITHDRAWN` 4, `NOT LANDED` 3, `SKEW` 2,
`PHANTOM` 2.

**Recurrently needs human judgement:**
- **Failure adjudication** — autopsy is the second-most-mentioned activity after governance.
  `REFUSED` (23) is the signature: sessions repeatedly declining to re-letter an experiment
  because the DV instrument is wrong. The 2026-07-20 `v4_loop_segregation` exhaustion
  withdrawal is the canonical case — a terminal negative verdict overturned on re-reading
  the DV as hold-weighted (form 2).
- **Substrate readiness calls** — `substrate_not_ready` (17) marks experiments run against
  substrate that turned out not to support them. This is a pre-run judgement that is being
  made after the compute is spent.
- **Concurrency repair** — `SWEPT` 17, `CONTAMINATION` 5, `SKEW` 2, `NOT LANDED` 3.
  Non-trivial and still recurring, though `ree_commit.py` + the pre-push hook have moved
  this from silent to detected.

**Low-friction / headless-safe:** `lit-pull` (backlog empty, no open items), `update-docs`,
`morning-digest`, `insights`. Experiment review is also near-clear at 1 pending.

---

## Recommendations

1. ~~**Resolve `modulatory-bias-selection-authority`.**~~ **SUPERSEDED — see Corrections §2.**
   The MECH-314 justification does not hold: the parent claim and MECH-314a read `supports`
   and owe no substrate work, while 314b/314c are `non_contributory` through a structurally
   vacuous criterion. The correct, confirmed action is an **`amend` on ARC-065**, not this
   node. `modulatory-bias-selection-authority` may still merit attention on its own 15
   failure records and 18 unblocked claims, but that case now has to be made independently
   rather than inherited from MECH-314's FAIL count.

   **Replacement action:** apply the confirmed `recommended_substrate_queue_entry` from
   `failure_autopsy_V3-EXQ-604c_2026-07-20.json` (action `amend`, target `ARC-065`, priority 1,
   unblocks MECH-314b/314c/Q-044) to `evidence/planning/substrate_queue.json`. Verified not yet
   applied: ARC-065's `failure_record` entries are all dated 2026-06-07.

2. ~~**Decide what happens to the three dead chains.**~~ **WITHDRAWN — see Corrections §1.**
   MECH-463 is a live campaign with a queued successor under a new number, INV-088 has a
   substrate-plane owner and a live clearing path, and INV-089 was adjudicated across four
   autopsies including a well-posedness review. No decision is owed on any of them. The
   underlying observation — no *same-base* successor — was real but is not evidence of
   abandonment.

3. **The queue is 70% re-runs, and four are one correction — batch or root-cause it.**
   742a, 737a, 728a and 734a are all "re-run under the zworld encoder guard": one substrate
   defect generating four separate compute jobs. Confirm the guard is correct once, then run
   the four; running four experiments against an unconfirmed guard multiplies the cost of
   being wrong. Related: `sd_actor_critic_action_learning` is `ready: true` prio 1 and
   unblocks both MECH-457 and the `f_dominance_conversion_ceiling` (26 failure records) —
   resolving it may retire several of these re-runs outright.

4. **Retire or repair `runner_status.json`.** It has been stale for 41 days and this skill
   depends on it for the only ERROR-rate signal available (manifests structurally cannot
   report ERROR). Either point the ERROR path at the coordinator DB, or the historical
   10.4% error rate is the last measurement the project will have.
