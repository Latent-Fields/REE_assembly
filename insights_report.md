# Project Insights — 2026-09-25

Generated: 2026-09-25T06:07:20Z
Front re-authored at: 2026-09-25T06:07:20Z (REE_assembly origin/master `8bdeda873a`), from the breakthrough integration pass synthesis.

> **Provenance.** The front sections (everything above **Experiment Health**) and **Recommendations** were
> re-authored on 2026-09-25 by session `bt0925-insights` (orchestrator `orchestrate-20260924-breakthrough`,
> chip `chip-20260925-insights-front-refresh`) from
> [`evidence/planning/breakthrough_pass_synthesis_20260925.md`](evidence/planning/breakthrough_pass_synthesis_20260925.md)
> (`08c6ed0c53`) and the records it cites. The sections from **Experiment Health** through
> **Human-Intervention Patterns** are the 2026-09-08 `/dual-insights` fleet measurement (window
> 2026-08-09 → 2026-09-07). They were **not re-measured** in this revision, so read their numbers as dated
> 2026-09-08. A fresh `/dual-insights` run owns that refresh.
> Every front finding below comes from small Mac probes at world_dim=32 (the deployed value) unless stated.
> Domains are given per finding, exactly as the synthesis gives them. Nothing here promotes or demotes a
> claim. Registry consequences were routed to `/governance` as flags (GFLAG-0479, 0481, 0484-0491).

---

## Where the front moved since 2026-09-08

### The live front is the native learning loop itself: at REEConfig defaults ree_core does no waking gradient learning, so the closed loop is not closed inside ree_core

- **Ready & not-yet-implemented** (buildable now): none un-owned. The root build, a ree_core-owned native waking trainer, is designed (`0c0f5b76ec`), but its architecture and sequencing are held for the user and `/governance` (Q4a-d). The one piece being built under the orchestrator's delegation is the grad-reach guard, as a pure instrument. It is in flight (see below).

**What the census measured** (`gradient_reach_census_20260925.md`, `940c690c9dd`; domain **D1, reach**, explicitly not D2):

- At defaults, 40 train-mode ticks build **0 optimizers**, and 716,769 of 717,825 parameters never change.
- Every trained parameter is trained by an optimizer that a *driver* builds.
- No driver recipe trains everything the agent reads when it acts. Every recipe leaves at least 6 randomly initialised modules on the act path.

Every broken edge the pass found is a local symptom of that one structural fact.

The 2026-09-08 front, re-measured:

| 2026-09-08 front item | state on 2026-09-25 |
|---|---|
| V3-EXQ-1010, the H-F over-capacity decoder sweep, "queued and running" | **Ran 2026-09-09.** It confirmed H-F ("content discarded at encode") at **D1**: the observation->z_world code is externally decodable from banked frozen latents. The 09-08 "queued and running" line is stale. Two follow-on runs are recorded in the GOV-JURIS-1 evidence-domain stamp: V3-EXQ-1041 (2026-09-15) found D0 instrument validity contested, and V3-EXQ-1023a (2026-09-17) closed the training-budget branch on a transfer-rate argument. |
| z_world D2, "no intervention on the encoded content has been shown to change E1/E2 prediction or E3 selection" | **z_world D2 REACHED** at E1 and at E3 selection, in both configs (`zself_causal_reach_trace_20260924.md`, `884a6b1ca3`, Section 4). The record states its own scope limit: this shows the encoded z_world is *used*. It does not show *which content* is used, so it does not answer H-F at D2. |
| `zworld_actor_adequacy_locus` as the live question | Its framing was already flagged as possibly mis-posed (GFLAG-0312, governance 2026-09-17). The pass puts the wall one level below it: whether the modules the agent reads when it acts are trained at all. |

## The live campaign — what the front rests on, and what is in flight

The front now rests on **probe records, not on a queued experiment**. The one EXQ row is the pass's entry point and is not a live run. Nothing on the experiment queue belongs to this front (ree-v3 queue checked about 2026-09-25T06:06Z: it holds three claimed items, none of them on this front).

| run / record | role | what it established (domain) |
|---|---|---|
| **V3-EXQ-1078** (2026-09-23; autopsy confirmed 2026-09-24) | **1 (lead)** | The entry point, not a live run. Its confirmed autopsy found "no loss reaches self_encoder". The z_self trace and the census re-measured that finding and generalised it. Its `Adam(agent.parameters())` recipe is the census canary (recipe A). |
| `gradient_reach_census_20260925.md` (`940c690c9dd`) | 2 (headline) | No waking gradient learning at defaults. Every recipe leaves at least 6 random act-path modules: `harm_eval_head` is untrained in 4 of 5 recipes (it is read on every E3 tick); the all-ON recipe trains neither E1 nor E2-self; the beta/theta/delta depth stack is random in 4 of 5; `terrain_prior` is untrained in 5 of 5. **D1 (reach).** |
| `zself_causal_reach_trace_20260924.md` (`884a6b1ca3`) | 3 | **z_self:** nothing trains the DR-13 GRU. Even when it is trained, no valuation consumer reads z_self: 0 of 68 E3 ticks and 0 of 12 episodes changed action. **D3 (negative)** for z_self->selection; **D2 at E1**. **z_world:** **D2 reached** at E1 and E3 selection (which content is used is not established). |
| Proposals: `monostrategy_type_a_vs_b_discrimination_20260924.md` (`948d58cd3e`), `action_decoder_training_trace_20260924.md` (`622716398d4`), `action_decoder_training_causal_probe_20260925.md` (`a369f411ff8`) | 4 | Proposals are state-invariant. The hippocampal `action_object_decoder` is never trained anywhere. Training it alone **FAILED** the pre-registered criteria (5 seeds). The proposal edge is a **codec with three coupled defects**: an untrained decoder, an unbounded decode fed to E2 as the action, and a first CEM iteration that samples about 12x off-range. **D0 (trace) + D2 (probe, FAIL).** The repertoire collapse is Type A (absence at generation). No ree-v3 ecology meets the Type-B prerequisites, so dynamic coordination has not earned a build. **D1/D2.** |
| `e2_rollout_divergence_and_proposal_state_dependence_20260924.md` + addenda 1-3 (`f300ebf64d`, `2d848ca2d3`, `ca212aff26`, `1b09b81b4d`) | 5 | The E2 world head has no waking objective. Even when trained, it is action-blind, because the agent's own one-action behaviour starves it of action coverage. A fresh head on action-diverse data works: executed-action pick 0.74-0.82 on PCA-32. **D1/D2.** Over 98% of E3's across-candidate score variance comes from rollout steps beyond 5; a depth-1 read of E3's own scorer tracks true consequence, and the full horizon does not. **D2.** |
| `e3_evaluation_edge_test_20260924.md` + addenda (`4ea0931b0f`, `7f852bcf4b`, `8ab5ce6fc1`, `5e3c956b41`) | 6 | Nothing calibrates E3's main channels against grounded outcome. With benefit shaping enabled, the benefit head trains and beats a shuffled control 3 of 3 times, but harm rises 3-5x. **D3 on env reward.** |
| `residue_consumer_reach_world_dim32_20260924.md` (`82819a1058`); `relational_edge_consumer_reach_20260924.md` (`410e589ce1`) | 7 | The GFLAG-0441 residue fix is correct as geometry (D1), but the consumer response cannot be told apart from a shuffled control: **D2 (negative)**. MECH-468 dumps have zero production callers, so the typed-vs-collapsed discrimination cannot run: **D0**. |

**Falsified in the pass (pre-registered where marked):**

- **R5b + R2 as a harm repair.** It **FAILED** a pre-registered replication on 5 fresh seeds. Harm was better than native on 1 of 5 seeds, and R2 was necessary on 0 of 5. The earlier 2-of-3 came from hazard-trapped starts. Record: `r5b_r2_fresh_seed_replication_20260924.md` (`fc987f3b057`); GFLAG-0489 corrects GFLAG-0487.
- **Decoder training alone as the proposal repair.** It **FAILED** pre-registered criteria P and C (`a369f411ff8`; GFLAG-0490).
- **Class-balanced replay as the E2 coverage repair.** It fails, because missing classes cannot be reweighted into existence. Exploration coverage does work.
- **The grounded-valuation battery as first designed.** Its absolute harm-floor detector for reward hacking missed the positive control. The pre-registered repair **FAILED** on fresh seed 45, and the stop rule was honoured (`28ebf56955`).
- Three independent tests showed that **proposal diversity without a grounded evaluator is undirected**: it buys harm on benign starts.

**Structural reading.** The failures are coupled:

- Proposals need a working codec.
- E2 needs action coverage from proposals.
- E3 needs informative rollouts (shallow or fixed) and grounded channel worth.
- All of it needs a native learner that ree_core does not have.

Each single-factor repair either did nothing or exposed the next defect it had been masking. The parts are now partitioned and named. Validating them one at a time in the native regime is not possible, because each depends on the others.

**In flight.** Both workers were launched 2026-09-25T05:54Z under the orchestrator's standing delegation. They are named here as in flight only; no outcome is claimed.

- `campaign-20260925-bt0925-guard`: the grad-reach guard is landing on ree-v3 main as a **pure instrument**. It adds new files only, is imported by nothing, and ships no trainer and no default change. Q4a-d stay open.
- `campaign-20260925-bt0925-nulldet`: a **pre-registered relative-to-null** reward-hacking detector probe for the grounded-valuation battery, on fresh seeds 61-65. Its pre-registration landed before any run (REE_assembly `789b61f6958`). Q1's options all need a valid detector first, and the choice between them stays open.

---

> *The sections from here through Human-Intervention Patterns are the 2026-09-08 `/dual-insights` measurement. They were not refreshed in the 2026-09-25 front revision.*

## Experiment Health

- **Total runs:** 152 (PASS: 74 | FAIL: 74 | ERROR: 4 | **error rate: 2.6%**) — window: 2026-08-09T00:20Z → 2026-09-07T23:38Z, source: coordinator DB `results` + `experiments` on hub `ree@91.98.130.117` via `scripts/experiment_error_rate.py --days 30`.
  - **0 phantom completions**, 0 bookkeeping gaps, 0 operator cancellations, 0 results without manifest — so 2.6% is a point estimate, not an interval (tool upper bound equals the point: 2.63%).
  - PASS rate **48.7%** (74/152), up from 36.3% (81/223) in the 2026-08-25 window. Volume is down ~32% (223 → 152 runs).
  - Per machine: ree-cloud-2 64, ree-worker-1 31, ree-worker-3 29, ree-cloud-4 23, ree-cloud-3 2, the Mac 3 (DLAPTOP-4/-5 aliases). Last result: ree-worker-3, 2026-09-07T23:38:27Z.
- **Last ERROR recorded fleet-wide:** the tool reports **"(none on record)"** from the per-machine `runner_status/` split — that split is retired (0 files read; CLAUDE.md A-93), so this field is structurally empty now and the DB's 4 ERROR rows are the whole measurement. The four are identifiable from on-disk ERROR manifests and each was re-lettered to a PASS within a day: V3-EXQ-918 (08-11 → 918a PASS 08-12), V3-EXQ-926 (08-13 → 926a PASS 08-14), V3-EXQ-944a (08-22 → 944b PASS 08-25), V3-EXQ-591g (09-02 → 591h PASS 09-03).
- **Unmeasurable bucket (stated, not estimated):** transient/infra crashes (exit `137/-9/-11/-15/143`, no sentinel) are intercepted upstream and retried in-queue; they leave no row anywhere. A *deterministic* crash of that class retries forever and is invisible to every source.

**High-iteration chains (3+ lettered iterations lifetime), active in this window** — 17 bases qualify; the ones with 2+ runs in window:

| chain | runs in window | outcomes | claim_ids |
|---|---|---|---|
| EXQ-861 | 7 (`b c d e f g h`) | 6 FAIL, **861f PASS** (08-23); g/h FAIL after it | INV-050, MECH-180 (861d also MECH-122) |
| EXQ-603 | 4 (`s t u v`) | 3 FAIL → **603v PASS** (08-27) | MECH-357 |
| EXQ-906 | 4 (`. a b c`) | 3 PASS, 1 FAIL | (untagged) |
| EXQ-436 | 3 (`e f g`) | 3 FAIL | SD-017, ARC-045, MECH-166 |
| EXQ-822 | 3 (`c d e`) | 822c PASS → 822d, 822e FAIL | SD-078, SD-082 |
| EXQ-910 | 3 (`. a b`) | 2 FAIL → **910b PASS** | MECH-489 |
| EXQ-937 | 3 (`. a b`) | 1 FAIL → 2 PASS | MECH-449, ARC-107 |
| EXQ-944 | 3 (`. a b`) | FAIL, ERROR → **944b PASS** | MECH-091 |
| EXQ-642 | 3 (`a b c`) | 2 FAIL → **642c PASS** | (untagged, diagnostic) |
| EXQ-228 | 3 (`b c d`) | 3 FAIL | ARC-032 |
| EXQ-894 | 2 (`b c`) | 2 FAIL | MECH-074d |
| EXQ-571 | 2 (`b c`) | 571b PASS, 571c FAIL | MECH-439 |
| EXQ-963 | 2 (`. a`) | 2 FAIL | MECH-063, SD-069 |
| EXQ-993 / 983 | 2 each | 2 FAIL each | ARC-021 + EXT-003/MECH-069; EXT-002 + ARC-013 |

All-time across 3,925 manifest files (988 distinct V3 run stems): **495 distinct EXQ bases**. Deepest lineage is still EXQ-603 (23 letters; 603v is the first PASS since 603n).

- **Recurring trouble spots** (claim_ids in 2+ ERROR entries): **none.** All four ERROR runs carry no claim tags on the crashed manifest; their lineages are four distinct claim sets.
- **Repeat-FAIL claims in window** (2+ FAILs): ARC-032 ×3 (228b/c/d), SD-017 / ARC-045 / MECH-166 ×3 (436e/f/g), MECH-489 ×2 (910, 910a — then PASS). Each is autopsied (see liveness below).

- **Stalled chains** (FAIL with no successor): **None — every candidate chain has an autopsy, an owner, or a successor.**

  14 FAIL runs in window have no same-base successor letter: 905a, 324d, 190a, 902, 912, 228d, 920, 874b, 956, 436g, 969, 971, 978, 1002. **Every one is named by at least one confirmed `failure_autopsy_*` file, searched by contents** (range 1–9 mentions; 436g sits in the 966-436g-951-959-822d cluster of 2026-08-30, 978 has its own 2026-09-03 autopsy, 1002 its own 2026-09-05 autopsy). The Phase-A2 liveness check was then executed per *claim* for the 12 claims those runs carry — MECH-075, SD-020, MECH-022, SD-048, ARC-032, MECH-467, SD-017, ARC-045, MECH-166, INV-088, MECH-457, MECH-489. Leg 2 (autopsies by contents) came back non-empty for all 12: MECH-022 2 (newest 08-09) … MECH-457 45 (newest 09-08). Leg 4 (commits in 7 d) is non-empty for SD-017 (4), MECH-489 (4), ARC-045 (3), INV-088 (3), MECH-457 (3), MECH-166 (2), SD-048 (1). Leg 1 is weak this run for a structural reason: `TASK_CLAIMS.json` is now a 24-hour-retention render (see Governance State), so it only shows MECH-467's claim. No claim came back empty on all legs.

- **Data-quality observations (verified):**
  - **Rework volume:** of 3,925 manifest files, 432 declare `supersedes` and 272 are marked `evidence_direction: superseded`.
  - 84 of the 152 classified runs are `experiment_purpose: diagnostic` (vs 64 `evidence`) — the window is majority-diagnostic, consistent with a front that is being localised rather than tested.
  - The queue has been **empty since 2026-09-07T23:39:46Z** (~7.5 h at generation). Over the window it never held more than 6 items; most snapshots show 0–1.

---

## Substrate Bottlenecks

`evidence/planning/substrate_queue.json` — 177 entries (161 on 2026-08-25). Counts use the boolean `ready` field; the free-text `status` field still carries prose paragraphs on ~40 entries and is not tallied.

- **Ready: 80 / 177.** Of those, **2 are ready and not implemented, and both are `proposed_REGISTRATION_ONLY_not_a_build`** (`mech317-action-chunk-boundary-instrument`, `mech092-replay-consumer-missing`) — registered DVs, not builds. **Effective ready-and-unbuilt cognitive machinery: 0.** The `next_implement_substrate` pointer (2026-08-21 reconcile) still reads *"there is no next implement-substrate build right now"*; the three builds that did land since (SD-018 amend, SD-e1 ITEM 3, E3 rung 3) were all routed by autopsy/governance, not by the pointer.
- **Not built: 36** — 6 `candidate_v3_pending` (MECH-256/257/316/317, ARC-064, SD-054), 6 `pending_implementation`, 2 `proposed`, 1 `probe_queued` (`sd_salience_contested_mode_occupancy`), 1 `design_question`, 11 with no `status` string, the rest explicitly gated/retired/wontfix.
- **Declared critical-path gate:** `f_dominance_conversion_ceiling` (`ready: false`, 27 failure records, +1 since 08-25) now carries three named `depends_on_unresolved` items. Two are landed (SD-018 amend; E3 rung 3), one is at a decision (SD-e1 Leg-B denominator). Its `ready` flag has not been re-evaluated since those landed.
- **Failure-record dating is not measurable this run:** 0 records carry a date inside the window, because the record entries do not carry a date field the scanner can read. Lifetime load only.

**SDs with the heaviest failure records** — 103 of 177 entries carry at least one:

| SD | failure records | state |
|---|---|---|
| `scaffolded_sd054_onboarding` | 28 | ready, implemented (603n PASS) |
| `f_dominance_conversion_ceiling` | 27 | not ready; 3 declared deps, 2 landed |
| `modulatory-bias-selection-authority` | 16 | implemented |
| `ARC-062` | 11 | phase 1 implemented, evidence-gated (543k/598) |
| `v4_loop_segregation` | 10 | implemented 2026-06-27 |
| `MECH-256` | 10 | candidate_v3_pending |
| `contextmemory-write-path-addressing-degeneracy` | 9 | implemented_pending_validation |
| `SD-049-PHASE-2` | 9 | phase 2 implemented |
| `SD-016` | 9 | implemented, ready |
| `ARC-065` | 8 | ceiling lifted (569i PASS) |

Cross-referencing against the chains above: this window's repeat-FAIL chains (861, 436, 228, 894, 963, 822d/e) are each carried by a confirmed autopsy, and none of them names a missing build as the cause; the heaviest failure-record nodes are implemented. No substrate-build recommendation follows from FAIL volume this run.

---

## Governance State

- **Claims pending V3 substrate:** `v3_pending: true` on **261** claims; `implementation_phase: v3` on 434.
- **Pending promotion/demotion decisions: 2** — `MECH-535` and `MECH-536` (both `hold_pending_v3_substrate`, `pending_user`), rows first appeared 2026-09-07T04:27Z (registered by the 2026-09-07 catatonia lit-pull). 210 of 212 decision rows are `applied`. File generated 2026-09-07T04:19Z; lives at `evidence/experiments/promotion_demotion_recommendations.md`.
- **Governance flags (`governance_flags.v1.json`): 226 total — 114 `open`, 106 `resolved`, 6 `superseded`.** Open by type: `stale_note` 48, `evidence_discrepancy` 40, `contested_disposition` 25, `promotion_review` 7 (120 non-terminal incl. superseded). Oldest open: GFLAG-0012 / -0013 / -0016, raised 2026-08-08 — **31 days**. This is the real decision backlog; the promotion/demotion table is short because it is curated.
- **Evidence superseded (rework):** 272 manifest files marked `superseded`, 432 declaring `supersedes` (lifetime).
- **`pending_review.md`** (generated 2026-09-07T04:20Z): **1 item** — `v3_exq_1006_sd_e1_var_bar_portfolio_fidelity_anchor_20260906T195135Z_v3`, diagnostic PASS. It is already covered by the confirmed `failure_autopsy_dv-headroom-diagnostics-cluster_2026-09-07` (1006/970a/972a/1009); it is not yet in `review_tracker.json`. Marking it reviewed is the active governance session's Step 1 work.
- **Closure (`closure_status.md`):** v3 weighted progress **73.0%** across 97 non-deferred nodes; **33 remaining**, 64 done, 10 assembly-frontier, 10 deferred. Unchanged from the 2026-09-07 `CURRENT_FRONT.md` snapshot.
- **`TASK_CLAIMS.json` is coordinator-authoritative with 24-hour `done` retention** (cutover 2026-08-28, materializer message *"claims 135 kept / 1026 aged-out"*): the render holds 139 entries (135 done, 4 active, 0 stale) against **1,161 lifetime claims** in the DB. Churn is reported in `dual_insights_report.md`.

---

## Literature Coverage

- **Priority-1 backlog items still open: none.** `evidence_backlog.v1.json` (967 items) now emits **510 literature-needed items: 494 `open`, 16 `in_progress`** — all `medium` priority except 4 `low`. This answers the probe the 2026-08-25 report left open: the channel was never drained, the backlog generator simply was not emitting literature items then (0 → 510).
- **In progress (16):** ARC-037, ARC-082, ARC-083, EXT-001, EXT-007, INV-086, MECH-161, MECH-162, MECH-219, MECH-290, MECH-308, MECH-325, MECH-326, MECH-441, MECH-482, SD-019b.
- **Corpus:** 509 entries under `evidence/literature/` (458 on 08-25, **+51 in two weeks**). Newest, all 2026-09-08: `targeted_review_arc_043`, `_arc_034`, `_connectome_arc_031`, `_connectome_arc_020`, `_inv_093`, `_inv_092`, `_inv_063`.
- **Covered in recent sessions (WORKSPACE_STATE + git log, 30 d):** 56 lit-pull session blocks; 35 `lit-pull:` commits in the last 7 days alone — INV-093, INV-092, INV-063, INV-040, IMPL-026/027, MECH-535/536, EXT-008, ARC-012/015/020/031/034/043, ARC-121, MECH-069/ARC-021, ARC-008/009, the sleep-reorganisation batch (MECH-533/122/285/SD-017/ARC-137/MECH-462/529/166/ARC-045/MECH-092/272), EXT-006. The automated morning pull (`lit-pull-am-b`, ARC-044 + ARC-047) holds an active claim at generation time.

---

## Human-Intervention Patterns

Derived from 605 dated `WORKSPACE_STATE.md` blocks in window (peak days: 2026-08-28 ×67, 09-07 ×61, 09-01 ×55) and the error analysis:

- **Tasks that recurrently required human input:**
  - **Governance decisions** — 114 open flags with a 31-day-old head; 2 `pending_user` rows; the SD-e1 Leg-B denominator decision; user decisions logged in window include E3 normalisation V3-required (09-04), hub runner retired (08-30), clinical-hours guard removed (08-28). 43 blocks record a `user-instructed` / `user decision`; 6 record an `AskUserQuestion`; 8 record a pause for user input.
  - **Gate holds** — 91 blocks carry a `HOLD` / `GATE STILL CLOSED` marker (MECH-152 measurement redesign held since 21 Aug is the recurring one).
  - **Coordination-plane repair** — the `metaworker` family is the single largest session type (173 blocks: dispatcher / healer / orchestrator), and 23 blocks open with `NOT LANDED:`.
- **Low-friction headless tasks:**
  - **lit-pull** — 56 blocks, scheduled morning pulls running unattended; +51 corpus entries in two weeks with no recorded intervention.
  - **failure-autopsy** — 116 autopsy documents in window; median landed-to-autopsied latency **0.09 days** (91 of 108 current-flow cases same day). The 4 diagnostics owed on 09-07 were cleared as a cluster the same day; 1008 was autopsied within a day of running.
  - **thought-intake / thought-digestion** — 37 blocks, 23 commits in 7 days, no intervention markers.
  - **diagnose-errors** — 10 blocks; all 4 ERRORs re-lettered to a PASS within a day.

---

## Recommendations

These restate the synthesis's Section 5. They are **decisions held for the user and `/governance`, not taken**. The `/insights` four-gate liveness procedure was not re-run for this revision.

1. **The gate is a ree_core-owned native waking trainer with a grad-reach guard, the root that the other broken edges hang off, and its architecture and sequencing (Q4a-d) are held for the user and /governance**. Design record: `native_waking_trainer_design_20260925.md` (`0c0f5b76ec`). Worker L's recommendation, not taken:
   - A hybrid WakingTrainer: the existing phased trainers become scheduled members, with per-tick online losses only for the REINFORCE heads.
   - Land the guard, a trainer skeleton and a `harm_eval` loss on main first, default-OFF.
   - Then run the coupled repair on an ree-v3 `integration/<slug>` branch, gated by the pre-registered closed-loop criterion.

   The guard needs no architecture decision. It is landing now as an instrument that decides none of Q4a-d (in flight, above).
2. **After (1), a coupled repair campaign on an ree-v3 integration branch** (CLAUDE.md's sanctioned exception). Its parts are validated together, not one at a time:
   - a whole-codec repair, or action-space proposals;
   - E2 world-head action coverage;
   - grounded main-channel valuation, with the relative-to-null detector first (in flight).

   The acceptance criterion is a pre-registered closed-loop criterion on env reward, with shuffled controls and hazard-trapped/benign stratification. Q1 (the valuation options) and Q2 (the repair order) are held.
3. **Registry rows are owed via flags.** This is `/governance` work, reported here and not chipped:
   - z_self valuation consumer: GFLAG-0481
   - codec: GFLAG-0488 / 0490
   - native trainer, `harm_eval_head` and depth stack: GFLAG-0491
   - E2 world objective: GFLAG-0485
   - commit-gate caveat: GFLAG-0486

   Also owed: the GOV-JURIS-1 evidence-domain stamp (`evidence/planning/current_front_evidence_domain.json`, governance Step 7a) is still anchored on the 2026-09-09 decoder sweep. It still lists z_world D2 as untested, so `CURRENT_FRONT.md` now renders it **STALE** until it is re-stated.

**Reported, not recommended:**

- `insights_report.html` was not re-rendered in this revision. The markdown is the source `generate_current_front.py` reads.
- The Experiment Health, Substrate, Governance State, Literature and Human-Intervention sections below the front are the 2026-09-08 measurement. Refreshing them is a `/dual-insights` run.
