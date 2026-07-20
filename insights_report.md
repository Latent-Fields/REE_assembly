# Project Insights — 2026-07-20

Generated: 2026-07-20T06:31:52Z

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

1. **Resolve `modulatory-bias-selection-authority` — it is the single highest-leverage
   node on the board.** It is `ready: true`, priority 1, carries **15 failure records**, and
   unblocks **18 claims** including MECH-314. MECH-314 took 8 FAILs in July and has **zero
   queued successors** — the chain is not stalled for lack of ideas. First step is to settle
   the field disagreement noted above (`status: implemented` vs null `implementation_status`):
   if it is genuinely unbuilt, build it; if it is built, its 15 failure records are
   misattributed and MECH-314's ceiling is somewhere else.

2. **Decide explicitly what happens to the three dead chains: INV-089 (EXQ-746, 4/4 FAIL),
   MECH-463 (EXQ-785, 3/3 FAIL), and INV-088 (4 FAILs).** None has a successor queued and
   none has a `ready` substrate entry attributed to it except `mech457_consummatory_act`
   (INV-088). Per the skill's continuity caveat, check each for a successor under a *new*
   EXQ number and for `evidence_direction_per_claim` exclusions before concluding they are
   abandoned — but if they genuinely are, that should be a recorded decision, not attrition.

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
