# Failure autopsy — V3-EXQ-874b (MECH-467 three-leg distractor battery)

- **Status:** confirmed (interactive gate, 2026-08-17)
- **Generated:** 2026-08-17T14:46:54Z
- **Scope:** single
- **Run:** `v3_exq_874b_mech467_distractor_three_leg_battery_20260816T222900Z_v3`
- **Queue id:** V3-EXQ-874b (supersedes V3-EXQ-874)
- **Claims:** MECH-467
- **Outcome:** FAIL — `non_degenerate: false`, all four arms gate-RED
- **Self-route:** `substrate_not_ready_requeue` — **upheld** (see §3)
- **Prior autopsy:** `failure_autopsy_V3-EXQ-874_2026-08-03` (confirmed) — this is MECH-467's **second** autopsy

---

## 1. Dry-run gate (Step 2a)

`scripts/check_dry_run_citations.py` over the target: **0 dry cited, 0 dry in named families, 0 ambiguous, 1 clean, 0 unknown** (exit 0). The manifest carries `smoke: false` and no top-level `dry_run`. No cluster or population statistic is used in this autopsy, so no further ids were in scope.

- `dry_run_checked: true`
- `excluded_dry_run_ids: []`

## 2. Recording provenance

`ree-v3/validate_recording.py --paths <manifest>` → **OK, 1 complete, 0 always-core gaps, 0 thin-pack provenance drops, 0 schema warnings.** `recording_schema: rec/v1`, `substrate_hash: a191a7b1…`, `substrate_stable_across_run: true`, `machine: ree-cloud-2`, `machine_class: linux-x86_64-py3.10-torch2.12.0+cpu`, `elapsed_seconds: 3500.9`, `seeds: [42, 43, 44]`, full `config` present.

**There is no recording gap.** Every always-core field is present, so the routing below is *not* a recording-debt route. The instrumentation problems in §4 are genuine measurement/design gaps — quantities that were never computed — not readouts that existed and were discarded. One qualification: the env supplies `done_cause` in `info` and the driver does not record it (§4.1), which *is* recording-debt in the narrow sense; it is folded into the successor spec rather than routed separately.

## 3. Facts — what failed, and what did not

The combination rule: an arm dissociates iff storage-site drift < 0.05 **and** selection-path `operative_rule_fidelity` ≥ 0.90 **and** wrong-target excess over the measured chance baseline ≥ 0.10. Aggregate `non_degenerate` = ANY arm green.

**The sole failing precondition, in every arm, is `leg_c_event_floor`.** Pooled target-consumption events (correct *or* incorrect) per arm, against a pre-registered floor of 15:

| Arm | events pooled (3 seeds) | floor | met |
|---|---|---|---|
| ARM_PRECOMMIT_SIMPLE | 1 | 15 | ✗ |
| ARM_REPLAY_SIMPLE | 3 | 15 | ✗ |
| ARM_PRECOMMIT_COMPLEX | 4 | 15 | ✗ |
| ARM_REPLAY_COMPLEX | 0 | 15 | ✗ |

Every other precondition passed in every arm: `distractor_encoded_in_active_representation` (0.022–0.032 vs floor 0.01), `selection_path_rule_read_live` (135–248 vs floor 1), `operative_rule_fidelity_instrument_sensitive` (−0.395 to +0.043 vs ceiling 0.70), `chance_baseline_not_saturated` (0.0–0.64 vs ceiling 0.95).

So the run is **vacuous by its own pre-registered gate, and correctly so**. `degeneracy_reason` states it exactly: *"No arm is scored; this run is NOT a refutation."* The self-route `substrate_not_ready_requeue` is upheld. **Nothing here weighs against MECH-467.**

### 3a. The redesign's own hypothesis was tested and REFUTED — this is the load-bearing positive result

874b is not a repeat of 874. It was built on a measured pre-authoring probe that explicitly **rejected** the 874 autopsy's "denser targets and/or a longer horizon" recommendation:

> *"The agent does not fail to COMPLETE an approach; it barely MOVES… A longer horizon on the SAME geometry multiplies a ~0 event rate by a constant… What actually moved the number was shrinking the arena."*

The redesign therefore took the arena from 10×10/5 resources to **6×6/12 resources** (≈3× density) over **900** eval ticks, and the probe at 6×6/6 had measured **3 events per 300 ticks = 0.0100 events/tick**.

**The realised run:**

| | probe (6×6, 6 resources, 300 ticks) | run (6×6, **12** resources, 900 ticks × 12 cells) |
|---|---|---|
| events / tick | 0.0100 | **0.00117** |

**8.5× worse than the probe, at double the resource density.** The geometry hypothesis is refuted on its own terms. This is the single most informative thing the run produced: it eliminates a live explanation that had already consumed one full redesign cycle, and it re-implicates the hypothesis the 874 autopsy named first and 874b set aside — *"the same substrate limitation (no sustained multi-step commitment)… re-appearing inside the two INCLUDED arms."*

### 3b. Even with zero truncation the floor was unreachable

At the observed per-tick rates, reaching 15 pooled events per arm requires **≈17,200 ticks (SIMPLE)** or **≈8,380 ticks (COMPLEX)** per arm, against the 2,700 budgeted (3 seeds × 900). Fixing the early termination in §4.1 alone would **not** have rescued the run — the shortfall is 3–6× beyond the window, not a rounding error. Any successor that only lengthens the window repeats 874's mistake one level up.

## 4. Three defects the manifest does not report

### 4.1 37% of the pre-registered exposure window was never run, and nothing records it

`n_ticks` per cell should be 900. Realised:

| ruleset | per-cell ticks | realised | truncated cells |
|---|---|---|---|
| SIMPLE | 900, 900, 820, 900, 676, 382 | 4578/5400 (**85%**) | 3/6 |
| COMPLEX | 139, 60, 107, 133, 900, 900 | 2239/5400 (**41%**) | 4/6 |
| **total** | | **6817/10800 (63.1%)** | **7/12** |

The eval loop ends `if done: break`, with no reset and no re-entry. Since warmup (80) + eval (900) = 980 < `max_episode_steps` (1500), the step cap cannot fire; the env's terminal is `done = _health_depleted or _step_cap_reached`, so **every truncation is `health_depleted` — the agent starved to death.** `p0_aborted` is `False` in all 12 cells, so this is not a training abort.

This is self-reinforcing: no consumption → health decays → episode ends → fewer ticks in which to consume. The env exposes `done_cause` in `info`; the driver never reads it, no cell carries a truncation flag, and **no precondition tests window completeness** — so a 60-tick cell and a 900-tick cell enter the pooled denominator indistinguishably.

### 4.2 The rule-set complexity axis is confounded with nutritive density

`num_resources` is fixed at 12 while `resource_type_distribution` sets spawn weights and only type 0 carries benefit (`resource_type_benefit_amplitudes` = (1,0) / (1,0,0,0)):

- SIMPLE (1.0, 1.0) → goal share 0.500 → **6 of 12** benefit-bearing
- COMPLEX (1.5, 1, 1, 1) → goal share 0.333 → **4 of 12** benefit-bearing

Adding distractor *types* silently removes a third of the food. COMPLEX realised 41% of its window against SIMPLE's 85%, and mean survival was 373 vs 763 ticks. Duncan's rule-set-complexity manipulation is therefore **not separable from a survival manipulation**, and any cross-ruleset comparison in this design is confounded.

Note the direction is not the naive one: COMPLEX's *event rate* was actually **higher** (0.00179 vs 0.00087 /tick). SIMPLE is rate-limited; COMPLEX is truncation-limited. Two different binding constraints wearing one FAIL.

### 4.3 `z_goal_stream.writer_defect: true` is a FALSE POSITIVE

The manifest reports `writer_calls: 0, ticks_total: 28674, writer_defect: true, n_agents: 6`, and `pending_review.md` consequently lists this run under **"Dead z_goal stream"** — a standing public record asserting the E3 goal term, MECH-293 ghost probes, MECH-288, MECH-189, SD-057 and the frontopolar read all silently no-opped.

**They did not.** The driver calls `agent.update_z_goal(...)` inside `_step`, which runs in both warmup and eval. The accumulator call is `zg_acc.observe(agent)`, placed at the end of the per-ruleset loop in `run_seed` — so it observes the **P0 base agent**, while every cell steps a **clone** from `clone_trained_agent`. `n_agents: 6` = 2 rulesets × 3 seeds base agents, not the 12 stepping clones. The base agents accumulated `z_goal_ticks_total` during P0 training, where `update_z_goal` is legitimately never called.

**Independent proof the writer ran:** `goal_live_at_warmup_end: true` in **9 of 12 cells**. `GoalState.is_active()` returns true iff `_z_goal.abs().sum() > 1e-6`, and `update_z_goal` is the sole writer of z_goal in the substrate. z_goal cannot be non-zero unless the writer ran.

The generalizable gap is in `experiments/_lib/z_goal_stream.py`, whose documented inference is *"`writer_calls == 0` with `ticks_total > 0` → the defect"*. That inference is **wrong for a training-phase agent**, which is stepped but never written. Confirmed at the gate: fix belongs in the lib, not only in this driver.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | Leg (c) never fired; legs (a)/(b) informative. The claim was not given conditions in which it could express itself, so nothing weighs against it. |
| Biological reference | **clear** | Gaspelin & Luck (registered-then-suppressed vs never-encoded, Pd analogue), Duncan 2008 (goal neglect: describable ≠ operative), Adams & Gaspelin 2021. `evidence/literature/targeted_review_mech_467` exists. Not a formal-definition import; the translation is faithful and the redesign is explicitly lit-driven. |
| Prerequisites | **missing** | Sustained multi-step commitment (874's hypothesis, re-implicated by §3a) and a survivable energy economy under pinned internal operating modes. |
| Implementation completeness | **partial** | Driver is otherwise strong, but: truncation unflagged (§4.1), accumulator mis-targeted (§4.3), and `selection_path_rule_read_live`'s stated control ("ticks where `e3_tick` is True **and z_goal is live**") does not match its code, which tests only `goal_state is not None and len(candidates) >= 3`. |
| Environment adequacy | **wrong pressures** | 6×6 / 12 resources / 0 hazards still starves the agent in 7/12 cells; complexity axis confounded with food supply (§4.2). |
| Measurement adequacy | **under-instrumented** | No movement or approach-initiation counters, no `done_cause`, no window-completeness precondition. `distractor_proximity_rate` is **1.0 in every cell**, so leg (a)'s encoding index has no absent-distractor contrast and spans 0.018–0.047 against the probe's 0.000–0.706. The fidelity-sensitivity control is pooled across seeds, masking ARM_REPLAY_COMPLEX s43 at 0.715 > the 0.70 ceiling. |
| Integration adequacy | **coupled but unstable** | The driver names the circularity itself: events → benefit exposure → z_goal live → goal-directed selection → events. The battery must bootstrap through its own dependent variable. |
| Scale / capacity | **likely insufficient** | 8,380–17,200 ticks/arm needed vs 2,700 budgeted (§3b). |

### 5a. Failure-location summary (GOV-FAILLOC-1)

| Bucket | Established? | Basis |
|---|---|---|
| MECHANISM FAILED | **not_established** | Implementation reads *partial* — three defects in §4. |
| MEASURES FAILED | **not_established** | Measurement reads *under-instrumented*. |
| ENVIRONMENT FAILED | **not_established** | Environment reads *wrong pressures*. |
| REE FAILED | **false** | Requires all three independently adequate; none is. |

**Net classification: MIXED — dominantly ENVIRONMENT + MEASURES, not chargeable to REE.** No statement of the form "REE cannot resist distractors" is licensed by this run.

## 6. The one positive scientific result — leg 2 dissociates at the two read sites

Restricted to the **9 cells where z_goal was actually live** (the 3 dead-z_goal cells are excluded: all three report `operative_rule_fidelity` of exactly `1.0000` with control ≈ 0, which is the signature of comparing a zero reference against a zero current — vacuous, and correctly predicted before being checked):

- storage-site `final_rule_drift`: **0.004 – 0.384**
- selection-path `operative_rule_fidelity`: **0.985 – 1.000**
- cells with drift > 0.05 (storage NOT intact) **and** fidelity ≥ 0.90 (selection intact): **6 of 9**

The storage-site rule vector drifts substantially while the rule actually steering E3 selection stays faithful to the warmup-established rule. **The redesign's central methodological bet is vindicated on REE's own substrate**: reading rule state at a storage site does not track the operative rule, exactly as Duncan's goal-neglect mechanism predicts.

**Caveats, stated rather than buried.** This is *not* a scored criterion — every arm's gate was RED, so nothing here is a verdict. The fidelity control exceeds its 0.70 ceiling in one live cell (ARM_REPLAY_COMPLEX s43, 0.715), so that cell's fidelity reading carries no information about rule content. And the observation is n=9 cells across 3 seeds.

**Why it still matters beyond this run.** MECH-467's own text says REE's distractor evidence is *"RULE CORRUPTION ONLY"*, owned by MECH-262 and resting on storage-site rule-drift measurements (V3-EXQ-484 and successors). If the storage-site read does not track the operative rule, then that body of evidence may not license conclusions about the rule that actually steers action. Confirmed at the gate: recommend governance record this on **both MECH-467 and MECH-262**, as an exposure to be examined — explicitly **not** a re-adjudication of any prior run, which this autopsy did not perform.

## 7. Learning extracted

1. **Arena geometry was not the binding constraint on leg (c).** The 6×6/3×-density redesign produced 0.00117 events/tick against the probe's 0.0100 — 8.5× worse at 2× density. The hypothesis is refuted, and one redesign cycle bought that elimination.
2. **The 874 autopsy's original commitment-deficit hypothesis is back in play**, having been set aside by 874b's probe on evidence that did not transfer to the full run.
3. **A pre-authoring probe measured on a differently-configured agent does not transfer.** The probe ran a P0-trained agent with the mode pinned from tick 0; the run inserts an 80-step unpinned warmup, uses distractor-bearing envs, and clones the agent per cell. Probe-to-run transfer needs its own check, not an assumption.
4. **An eval loop that breaks on `done` silently converts agent death into a shorter measurement window.** Any pooled denominator over such a loop is a denominator over an unrecorded, cell-varying budget.
5. **Adding resource *types* at fixed `num_resources` removes food.** A complexity axis built this way is confounded with survival.
6. **`z_goal_stream`'s writer inference is unsafe for training-phase agents**, and observing a base agent instead of the stepping clone publishes a false `writer_defect` into `pending_review.md` — a defect record that looks exactly like the real thing.
7. **Storage-site and selection-path rule reads dissociate in 6/9 live cells** — Duncan's distinction is real on this substrate.
8. **A precondition's prose control and its code can disagree** (`selection_path_rule_read_live` claims to test z_goal liveness and does not), which matters because the prose is what a later reader adjudicates against.

## 8. Repair pathway

**Node classification** (`work_graph_debt_vocabulary.md`): `complex (probe-gated) / puzzle (known rules)`. The frame is well-posed — we know what leg (c) needs — but *why* the agent will not eat is a missing fact with **four live hypotheses**, so this is a spike, and per GOV-FANOUT-1 a *portfolio* rather than one more sequential letter.

**Routing: `queue-experiment`, as a 4-leg fan-out** (confirmed at the gate). Each leg sits on a distinct axis family with a declared null:

| Leg | Axis family | Probe | Null |
|---|---|---|---|
| H-commitment | `process` | Measure approach-run length directly — consecutive ticks moving toward one target — rather than inferring it from the event count | Approach runs are as long as a successful consume requires; commitment is not the constraint |
| H-energy | `environment` | Decouple survival from the measurement window (health decay disabled or satiety clamped) at identical geometry | Event rate per *realised* tick is unchanged; starvation only shortened the window, it did not suppress eating |
| H-denominator | `measurement` | Decompose "0 events" into never-approached vs approached-and-failed-to-arrive, with movement and approach-initiation counters, `done_cause`, and a window-completeness precondition | The decomposition is uninformative because approaches are initiated and complete at the observed rate |
| H-cadence | `selection` | Test whether the ~10% genuine-E3-tick fraction (0.091–0.126 across all cells) bounds the achievable event rate | Events do not cluster on E3 ticks; cadence does not bound the rate |

**Not routed to `implement-substrate`.** The re-derive brake reports **0 prior `substrate_ceiling` autopsies** for MECH-467 (this is autopsy #2, and #1 was `measurement_test_design_defect`), so the brake does not fire and no same-claim re-queue is forbidden. More substantively, naming a substrate build now would be picking one of the four hypotheses before the discrimination has been run — the error GOV-FANOUT-1 exists to prevent. `recommended_substrate_queue_entry.action: none`.

**Mandatory in any successor, independent of which leg wins:** record `done_cause` and a per-cell truncation flag; add a window-completeness precondition; hold benefit-bearing resource *count* (not total resource count) constant across the ruleset axis; observe the stepping clones in `zg_acc`; and align `selection_path_rule_read_live`'s code with its stated control.

**Separately routed (confirmed at the gate):** a guard in `experiments/_lib/z_goal_stream.py` so a driver observing a non-eval-stepped agent is caught rather than publishing a false `writer_defect`. Classified `degrading` — it does not invalidate 874b's verdict (the vacuity stands on the event floor alone) but it corrupts a standing cross-run record.

## 9. Draft `evidence_quality_note` for governance

**MECH-467** (recommended verbatim):

> [2026-08-17 governance, V3-EXQ-874b, confirmed failure_autopsy_V3-EXQ-874b_2026-08-17, second experimental test]: the leg-(c) redesign FAILED to produce a denominator — 1/3/4/0 pooled consumption events per arm against a pre-registered floor of 15, all four arms gate-RED, `non_degenerate: false`. Nothing weighs against the claim. The redesign's own hypothesis is REFUTED and that is the informative result: 874b took the arena to 6x6 at ~3x resource density on a probe measuring 0.0100 events/tick, and realised 0.00117 events/tick — 8.5x worse at double the density. Arena geometry was not the binding constraint, and the V3-EXQ-874 autopsy's commitment-deficit hypothesis is re-implicated. Three defects the manifest does not report: (1) 7 of 12 cells terminated early on `health_depleted`, so only 63.1% of the pre-registered exposure window was realised and no cell records it; (2) the rule-set-complexity axis is confounded with nutritive density (SIMPLE 6/12 benefit-bearing, COMPLEX 4/12), so COMPLEX realised 41% of its window vs SIMPLE's 85%; (3) `z_goal_stream.writer_defect: true` is a FALSE POSITIVE — the accumulator observed the P0 base agents, not the 12 stepping clones, and `goal_live_at_warmup_end` is true in 9/12 cells. At observed rates the floor needs 8,380–17,200 ticks/arm vs 2,700 budgeted, so lengthening the window alone cannot rescue this design. non_contributory / standard (measurement + environment test-design defect). Failure-location MIXED, not chargeable to REE. Route: /queue-experiment as a GOV-FANOUT-1 4-leg portfolio (process / environment / measurement / selection) — NOT another lettered re-pose of the same design. SEPARATE FINDING, recorded on MECH-262 as well: in the 9 live-z_goal cells, storage-site rule drift (0.004–0.384) and selection-path operative-rule fidelity (0.985–1.000) DISSOCIATE in 6/9, so a storage-site rule read does not track the operative rule on this substrate.

**MECH-262** (recommended verbatim):

> [2026-08-17, from confirmed failure_autopsy_V3-EXQ-874b_2026-08-17, cross-claim exposure — NOT a re-adjudication]: V3-EXQ-874b instrumented rule state at TWO sites simultaneously and they dissociate. In the 9 cells where z_goal was live, storage-site `rule_state` drift ranged 0.004–0.384 while selection-path `operative_rule_fidelity` (Spearman rank correlation of per-candidate goal scores under the current vs the warmup-established z_goal) ranged 0.985–1.000; 6 of 9 cells show storage NOT intact (drift > 0.05) while selection IS intact (fidelity >= 0.90). This is Duncan 2008's goal-neglect distinction — describable rule vs operative rule — reproduced on REE's substrate. MECH-262 owns rule corruption and its evidence (V3-EXQ-484 and successors) is read at the STORAGE SITE, so that evidence may not license conclusions about the rule actually steering action. Flagged as an exposure to examine on the next MECH-262 cycle. Caveats: not a scored criterion (all arms gate-RED); n = 9 cells / 3 seeds; the fidelity-sensitivity control exceeds its 0.70 ceiling in one live cell (ARM_REPLAY_COMPLEX seed 43, 0.715). No prior run was re-adjudicated by this autopsy.

## 10. Gate outcomes

- **Re-derive brake (MOVE-3):** MECH-467 ceiling hits under R1–R3 = **0**. Does **not** fire. No re-queue is refused.
- **Granularity-debt recurrence trigger:** `granularity_debt_cluster.py MECH-467` → 1 prior target, 1 file, alignment distribution `unclear=1`, **no target reads `weakened`**. Does **not** fire. This is measurement/implementation debt, not granularity debt — the count (this makes 2) is not sufficient on its own.
- **GOV-FAILLOC-1:** MIXED (§5a).
- **Growth-restriction check (Step 9b):** N/A — no existing hypothesis-space question names MECH-467, so §11 registers a new one and a new question cannot carry a restriction.

## 11. Hypothesis-space ledger (Step 9b, Mode A)

New question `mech467_legc_event_denominator_cause` registered with the 4 legs of §8 pre-registered **before** their adjudicating runs exist (`pre_registered_utc = 2026-08-17T14:46:54Z`, all `alive`, `initial_frozen_count = initial_frozen_count_at_registration = 4`). All four axes (`process`, `environment`, `measurement`, `selection`) already exist in `axis_families.map`, so no new family row is needed.

## 12. Follow-on NOT chipped

Per CLAUDE.md Session Land Protocol step 6 (2026-07-30, user-instructed): a `/failure-autopsy` session does not `spawn_task` follow-on that depends on its own not-yet-ratified routing. The fan-out portfolio, the MECH-262 exposure note and the `z_goal_stream.py` guard are all this autopsy's own recommendations; `/governance` chips them once Step 2b/4/6a ratifies. Reported inline instead.

## 13. Still owed — the next autopsy target

**V3-EXQ-935** (`v3_exq_935_mech266_margin_normalised_cap_rule_20260817T075758Z_v3`, MECH-266 + SD-032a) is a `experiment_purpose: diagnostic` FAIL and therefore a mandatory autopsy trigger in its own right. It shares **no** failure shape with 874b — every readiness gate is green (5/5 seeds), z_goal is healthy (`active_frac` 0.99998), and it genuinely adjudicated its pre-registered hypothesis (H-RULE rejected in favour of the H-IDIO null, C1 2/5 vs a 0.667 floor). It is a clean adjudication needing a verdict, not a starved run — which is why it was not folded into this artifact as a cluster member. It carries fan-out ledger implications of its own (successor to GOV-FANOUT-1 leg H1 / V3-EXQ-934). Reported inline per the `/failure-autopsy` carve-out rather than chipped.
