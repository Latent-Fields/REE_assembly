# Project Insights — 2026-09-08

Generated: 2026-09-08T07:17:33Z
Recommendations fixed at: 2026-09-08T07:17:33Z (REE_assembly `ca527de428`; last-hour commit check run immediately before writing)

> **Provenance.** This is a fresh `/dual-insights` fleet measurement (window 2026-08-09 → 2026-09-07,
> 30 days). It replaces the 2026-09-02 revision, whose front sections were written by the cross-plan
> root-cause synthesis session and whose appendix carried the 2026-08-25 measurements unrefreshed. The
> synthesis record itself is unchanged and still the plan of record for the front:
> [`evidence/planning/cross_plan_root_cause_synthesis_20260902.md`](evidence/planning/cross_plan_root_cause_synthesis_20260902.md).
> Every number below was re-measured this run; nothing is carried forward verbatim.

---

## Where the front moved since 2026-09-02

### The live front is the encoder side of the observation -> z_world interface: H-F "content discarded at encode" is the one alive hypothesis on `zworld_actor_adequacy_locus`

- **Ready & not-yet-implemented** (buildable now): none — the only 2 ready-and-unbuilt substrate entries are registration-only DVs, and the three builds the 2026-09-02 report named (SD-018 amend, SD-e1 ITEM 3, E3 rung 3) have all landed. The buildable-now item is an *experiment*: the over-capacity decoder sweep named by the V3-EXQ-1008 autopsy (queued 18:13Z as V3-EXQ-1010 by the Wave-5 fresh-fill session; running).

The 2026-09-02 report named three items on the v3 critical path. All three have moved:

| item (2026-09-02) | state on 2026-09-08 |
|---|---|
| SD-018 directional resource-field amend — "un-owned" | **Landed** (ree-v3 `028a625e09`, REE_assembly `baf4941661`); substrate entry `amend_implemented_pending_validation`, `ready: true`. Validation run V3-EXQ-978 FAILed 2026-09-03 and was autopsied the same day; chips `sd018-directional-field-amend`, `sd018-fieldhead-validation-run`, `sd018-p0a-field-weight-seam` all `done`. |
| SD-e1 var-bar portfolio (`sd_e1_var_bar_readout_crush`) — "unqueued" | **Ran** as V3-EXQ-1006 (2026-09-06, diagnostic PASS). Registry: 2 confirmed (`H-fidelity-anchor`, `H-goal-orthogonal-dispersion`), 1 alive (`H-readout-saturation`). The recorded observation bottleneck is discharged; the registry's own `live_gate` now reads *"a governance DECISION on which denominator settles Leg B, not a measurement."* |
| E3 channel-scale normalisation (rung 3, MECH-439) — "to be decided with GFLAG-0051" | **Decided 2026-09-04 (V3-required) and BUILT** — ree-v3 `c47b885` (2026-09-07), chip `e3-channel-commensurability` `done`. |

`f_dominance_conversion_ceiling` now **declares** all three as `depends_on_unresolved` with `node_class: complicated (buildable)` — the 2026-09-02 Recommendation 2 ("declare the gate") is applied.

## The live campaign — what the front rests on, and what is in flight

Snapshot 07:17Z: nothing queued (empty since 2026-09-07T23:39Z). Corrected at close: the lead run was queued at 18:13Z and is running. Lead first.

| run | role | what it established |
|---|---|---|
| **V3-EXQ-1010** (queued 2026-09-08T18:13Z, RUNNING on DLAPTOP at 2026-09-08T19:58:53Z) | **1 (lead)** | Over-capacity decoder sweep on the banked 1002/1008 latents -- adjudicates H-F, the last alive hypothesis on `zworld_actor_adequacy_locus` |
| V3-EXQ-1008 (2026-09-07, autopsy confirmed 2026-09-08) | 2 | H-E (channel input capacity) ELIMINATED, H-C (geometry mismatch) SPLIT — the encoding discards decision-relevant content; names the over-capacity decoder sweep on the banked latents as the H-F discriminator |
| V3-EXQ-1002 (2026-09-05) | 3 | H-B (consumer learning) ELIMINATED, H-D (warm-up is not the locus) CONFIRMED on the same frozen-latent dataset |
| V3-EXQ-1006 (2026-09-06, cluster autopsy 09-07) | 4 | SD-e1 var-bar portfolio: fidelity-anchor and goal-orthogonal-dispersion CONFIRMED; both Leg-B denominators recorded; remaining gate is a decision |
| V3-EXQ-978 (2026-09-03) | 5 | SD-018 directional-field head validation FAILed the behavioural precondition (above-random foraging still unmet); autopsied same day |

The live question has moved one layer further in: `zworld_actor_adequacy_locus` (registered 2026-09-04, claims MECH-457 / INV-088). V3-EXQ-1002 (2026-09-05) eliminated H-B (consumer learning) and confirmed H-D (warm-up is not the locus); V3-EXQ-1008 (autopsy confirmed 2026-09-08, ~1 h before this report) eliminated H-E (channel input capacity) and **split H-C (geometry mismatch), leaving H-F "content discarded at encode" as the one alive, unadjudicated hypothesis**. The autopsy names the next gate: an over-capacity decoder sweep on the already-banked 1002/1008 latents. It was not queued at 07:17Z; it was queued at 18:13Z as V3-EXQ-1010 and is running (correction at close).

---

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

Each item below passed the four gates (liveness executed, named target is the autopsy's/registry's own, not already applied, not brake-refused) at 2026-09-08T07:17:33Z. The last-hour commit check found the 1008 autopsy (`3f86587d6d`) and the 09-08 thought-intake registrations; nothing supersedes the items below.

1. **V3-EXQ-1010 — the H-F over-capacity decoder sweep on `zworld_actor_adequacy_locus` — is queued and running; it is the one live gate on the conversion-ceiling root, and nothing needs queueing.** *[Correction 2026-09-08T19:58:53Z: the 19:50Z version of this line said "queue it"; it had already been queued at 18:13Z by `w5-freshfill-20260908` (ree-v3 `203ad0b`) and was at 27% on DLAPTOP when this session re-checked the queue at close. Registry `live_gate` corrected in the same commit.]* Named by confirmed `failure_autopsy_V3-EXQ-1008_2026-09-08`: same banked V3-EXQ-1002/1008 latents, seeds, held-out split and standardiser; only decoder capacity varied, from the consumer's exact 32->128 policy net up to a deliberately over-parameterised decoder. It adjudicates the last alive hypothesis (H-F, content discarded at encode). Owner: `chip-20260908-w5-s1-zworld-front` (claimed by `xenodochial-austin-8c5984`). The rung-3 validation is likewise owned (`chip-20260907-e3-commensurability-validation`, claimed by `w5-freshfill-20260908`; its first target V3-EXQ-1012 was blocked as tautological, `088fbec4c9`). Next action for this session: none.
2. **Applied 2026-09-08T19:50:33Z (user-approved, session `dual-insights-20260908-followup`) — the two items this report originally recommended here:**
   - *SD-e1 Leg-B denominator DECIDED: same-start.* Recorded in `decision_log.v1.jsonl#2026-09-08T19:50:33Z`; `H-readout-saturation` CONFIRMED, `sd_e1_var_bar_readout_crush` decided (3 of 3 legs). Consequence carried to `f_dominance_conversion_ceiling` item 2: the 0.002 var bar must be re-registered relative to same-start real-endpoint variance before any further SD-e1 var-bar run. `ready` stays false; all three dependency items re-worded to their current state (SD-018 landed, validation owed; rung 3 built, validation owed).
   - *Hero re-pointed to `conversion_ceiling_root`* and its decision block rewritten to name the decoder sweep (item 1 above) and the rung-3 validation; GFLAG-0115 resolved. `CURRENT_FRONT.md` now derives the correct live question.
3. **Work the flag backlog from the oldest end.** 114 open flags, oldest 31 days, 48 of them `stale_note` (the cheapest type to clear). The 2026-09-01 triage recorded 25 STILL-HOLDS + 7 PARTIAL; a second pass keyed on age rather than type would retire the 2026-08-08 cohort. This is `/governance` work — reported here as the throughput finding, not chipped.

**Reported, not recommended (owned elsewhere):**
- The **over-capacity decoder sweep** that adjudicates H-F on `zworld_actor_adequacy_locus` is named by the 1008 autopsy confirmed ~1 h before this report. It is the next experiment on the live front and the queue is empty, but it is `/governance`'s to chip after Step 2b ratification, and governance is active now.
- **`f_dominance_conversion_ceiling` `ready` re-evaluation** once (1) lands — a governance disposition, not a build.
- **No substrate-build recommendation this run:** the two ready-and-unbuilt entries are registration-only, every repeat-FAIL chain has a confirmed autopsy naming a non-build cause, and `next_implement_substrate` correctly reads "none".
- **Open chips tripled (33 → 111)** but 102 of them are ≤7 days old and only 2 exceed 14 days — spawn volume, not accumulation. No triage recommended; `audit_orphan_chips.py` covers it on cadence.
