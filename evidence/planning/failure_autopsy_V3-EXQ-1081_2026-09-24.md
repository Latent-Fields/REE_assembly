# Failure autopsy -- V3-EXQ-1081 (SD-PP-B1 world_forward -> E3 ranking reach probe)

- **Status**: `awaiting_human_confirmation` (STAGING -- subagent of `/governance` session `governance-20260924-workset`; nothing committed, no claim opened, hypothesis ledger not written)
- **CONFIRMED 2026-09-24T07:29:21Z** at the /governance interactive gate (session governance-20260924). Confirmed as drafted: SD-PP-B1 closed premise-false; GFLAG-0437 resolved in the same cycle. Recommendation-ledger: rec-20260924-002ff612. Hypothesis ledger applied (Step 9b).
- **Generated**: 2026-09-24T06:02:41Z
- **Run**: `v3_exq_1081_sdppb1_world_forward_ranking_reach_probe_20260923T222438Z_v3` (ree-worker-3, ree-v3 `c6aa52d9`, clean tree, 6543 s)
- **Purpose / outcome**: diagnostic, claim-free (`claim_ids: []`), **PASS**
- **Self-route**: `sleep_head_change_reaches_e3_ranking__rollout_yes__curiosity_undetermined`
- **Indexer adjudication flag**: `precondition_unmet`
- **bears_on**: `SD-PP-B1-world-forward-behavioural-consumer` (token reused verbatim from failure_autopsy_V3-EXQ-1073_2026-09-22), MECH-572, MECH-573, MECH-574, INV-063
- **Governance refs**: GFLAG-0413 (commission), GFLAG-0437 (premise correction, OPEN), rec-20260923-e1e14f35

---

## 1. Gate checks (Step 2a)

| Check | Result |
|---|---|
| `check_dry_run_citations.py` over run_id + V3-EXQ-1081 | 0 dry, 1 clean (exit 0) |
| `check_autopsy_coverage.py V3-EXQ-1081` | AVAILABLE YES -- no prior autopsy |
| `validate_experiments.py --checks dry_run_unreachable_criterion` | no finding for 1081 |
| `validate_recording.py` on pack + flat manifest | both OK, 0 always-core gaps |

`dry_run_checked: true`, `excluded_dry_run_ids: []`.

## 2. Facts (no interpretation)

**Design.** Per seed: P0 world_forward reconstruction training (alpha_world 0.9, done read), a 180-step wake window, snapshot S_pre, one `force_cycle()` with `use_sleep_world_forward_consolidation=True`, snapshot S_post. Ten yoked twins rebuilt from state_dicts, one shared env driven by twin A, identical per-step RNG. DV = fraction of fresh E3 selects whose argmin first-action class differs from A's (`top1_diff_rate`). MECH-314a armed in all twins (`curiosity_candidate_source="e2_world_forward"`, novelty only, visitation source, `curiosity_novelty_weight` at its 0.05 default -- not overridden by the driver).

**Preconditions.** Load-bearing (gate C1/C2): `yoke_exact` 0.0 / 0.0 / 0.0; `sleep_moved_head` 0.033 / 0.029 / 0.036; `positive_control_reach` (REINIT_BOTH) 0.248 / 0.228 / 0.644 vs 0.10; `n_ticks` 105 / 123 / 317 -- **all met, 3/3 seeds**. C3-scoped (`applies_to: C3_curiosity_route`): `curiosity_route_live` 1.0 on 3/3 (met); **`curiosity_route_positive_control` 0.0095 / 0.0163 / 0.0063 vs 0.10 -- UNMET 3/3.**

**Per-twin top-1 change rate vs A** (NULL = 0.0 exactly on every seed, so rate = excess):

| Twin | seed 42 (n=105) | seed 123 (n=123) | seed 456 (n=317) | seeds >= 0.05 |
|---|---|---|---|---|
| SLEEP_BOTH (C1, load-bearing) | 0.048 (5) | 0.122 (15) | 0.448 (142) | **2/3** |
| SLEEP_ROLLOUT_ONLY (C2) | 0.048 (5) | 0.114 (14) | 0.454 (144) | 2/3 |
| SLEEP_CURIOSITY_ONLY (C3) | 0.000 | 0.008 (1) | 0.000 | undetermined (0 determinate seeds) |
| SLEEP_X4_BOTH (C4, recorded) | 0.219 | 0.285 | 0.517 | 3/3 |
| FULL_SLEEP (C5, context) | 0.048 | 0.122 | 0.448 | 2/3 -- identical to SLEEP_BOTH |
| NOISE_MATCHED (C6, context) | 0.067 (7) | 0.057 (7) | 0.451 (143) | **3/3** |
| REINIT_BOTH (+ctrl) | 0.248 | 0.228 | 0.644 | 3/3 |
| REINIT_CURIOSITY_ONLY (+ctrl C3) | 0.010 (1) | 0.016 (2) | 0.006 (2) | 0/3 |

Desync 0.0 and non-finite ticks 0 for every twin on every seed. Candidate set identical to A: 0.0 for every rollout-carrying twin, 1.0 for both curiosity-only twins (by construction). `rank_discordance_mean` on curiosity-only twins: SLEEP 0.002 / 0.005 / 0.001; REINIT 0.018 / 0.053 / 0.001 of candidate pairs.

**Sleep's effect on the head** (flat manifest `arm_results`): `head_max_abs_change` 0.00805 / 0.00797 / 0.00803 (the fresh-Adam bound is 8 steps x 1e-3 = 0.008); `head_rel_l2_change` 0.033 / 0.029 / 0.036; non-head rel-L2 0.076 / 0.066 / 0.066. Held-out MSE pre -> post 3.24e-5 -> 3.74e-5, 2.87e-5 -> 6.99e-5, 3.07e-5 -> 1.37e-4 (x1.16 / x2.43 / x4.45); persistence-relative skill 0.212 -> 0.142, 0.177 -> -0.260, 0.060 -> -0.596. A's novelty deviation range / E3 score range: 0.047 / 0.070 / 0.0025; `a_near_tie_frac` 0.048 / 0.016 / 0.079.

**Expected vs observed.** Driver pre-stated: C1 pass => the sleep-sized change reaches ranking; "if C6 reaches as often as C1, the reach is generic sensitivity to a head change of that size, not something specific to the sleep direction". Observed: C1 2/3 PASS; C6 3/3.

## 3. The unmet precondition and whether the self-route survives

**Which precondition:** `curiosity_route_positive_control`, all three seeds. A random world head swapped into ONLY the MECH-314a per-candidate summary read changes the E3 top-1 on 1 of 105, 2 of 123 and 2 of 317 ticks.

**Why the run-level flag fires:** `build_experiment_indexes.py::_compute_adjudication` fires `precondition_unmet` on any recomputed-unmet precondition and does not read `applies_to`. The driver scoped this control to C3 only, and C3 honours it (state `undetermined`, 0 determinate seeds). Nothing gating C1 or C2 is unmet.

**Was the assumption really unmet?** Yes, genuinely -- for C3. At the default `curiosity_novelty_weight` 0.05 (with `normalize_score_bias_to_e3_range` OFF), the novelty term spans <= 7% of the E3 score range, so a head change on that channel can only flip the argmin at near-ties. The precondition test is correct, not wrong.

**Does the self-route survive?** Yes, as literally stated -- `rollout_yes` and `curiosity_undetermined` are both correct -- but narrowed twice:

1. **Magnitude-generic, not sleep-specific.** NOISE_MATCHED clears the bar on 3/3 seeds vs C1's 2/3, and is at or above SLEEP_BOTH on 2 of 3 seeds (42: 7 vs 5 ticks; 456: 143 vs 142). Only seed 123 shows sleep above noise (15 vs 7). By the driver's own C6 reading, what the run shows is that E3 ranking is sensitive to a world-head displacement of one sleep cycle's size, and the sleep direction adds nothing measurable.
2. **At the edge of the bar.** Seed 42 misses by one tick (5/105; 6 needed), with 0 changes in its first 20 paired ticks. Its `a_near_tie_frac` is also exactly 5/105, which fits flips at near-ties, but per-tick records are not in the manifest. Seed 456 is sensitive to every head change (REINIT 0.64, NOISE 0.45). The robust statement is "reaches, via rollout", not "reaches strongly".

The adjudication flag is therefore **CLEARED for C1/C2** (a scoping artefact) and **STANDS for C3** (already encoded in the label as `undetermined`, never as `no`).

## 4. Premise re-measurement (every premise the task rests on)

| Premise | Source | Re-measured 2026-09-24 | Verdict |
|---|---|---|---|
| e2.world_forward has no default-on route to E3 (SD-PP-B1 title) | substrate_queue.json | ree-v3 HEAD `4fc6f3d`: `e2_fast.py` `rollout_with_world` calls `self.world_forward(z_world, action)` inside the horizon loop at ~:822, unconditionally; HippocampalModule calls `rollout_with_world` at module.py 1113 / 1342 / 1384 / 2284 / 2895 / 3031; E3 reads `Trajectory.world_states` (`_get_world_states` :1301). Empirically, REINIT_BOTH moves the top-1 on 23-64% of ticks and changes the candidate set on 100% of ticks | **FALSE** (GFLAG-0437 correct) |
| "e3_selector.py's only reference to world_forward is a docstring" | B1 implementation_hint | literally true (line 1286), but E3 consumes the head's OUTPUT via world_states | true but misleading |
| MECH-314a e2_world_forward source is the cheapest consumer to probe | B1 hint / GFLAG-0413 option A | positive control 0/3; at weight 0.05 the route has no top-1 authority over head changes | **wrong consumer** |
| GFLAG-0437's scratch probe showed only STRUCTURAL reach | GFLAG-0437 | now measured at sleep-sized magnitude: reach exists (2/3), magnitude-generic | superseded by measurement |
| 1073 figures provisional because alpha_world 0.3 < SD-008 floor | MECH-572 note | this run at 0.9 shows the same optimiser-bound displacement and head degradation | the alpha caveat does not rescue sleep |
| Sleep changes only the head | implicit | non-head rel-L2 ~0.07, but FULL_SLEEP = SLEEP_BOTH top-1 on 3/3 -- the non-head change adds no ranking effect | holds for ranking |

## 5. Claim-layer map

Claim-free. No claim is adjudicated or credited. The run bears on MECH-572/573/574 and INV-063 leg B only through SD-PP-B1, whose cap on those claims ("mechanistic/local only, because no route") this run removes as a premise. Their other caps remain: the sign of the sleep update (MECH-572/574; re-observed here), head readability (SD-PP-B5 / MECH-573), and untrained evaluators in any P0-only protocol. `per_claim_recommendation` is `{}`.

## 6. Biological-reference triage

The route under test is a faithful translation. Hippocampal prospective sweeps (vicarious trial-and-error, preplay) run the current world model forward and are valued downstream by striatal and orbitofrontal circuits; offline replay reshapes that model before the next waking sweep. REE's HippocampalModule -> `E2.rollout_with_world` -> `E3.score_trajectory` is that loop. What the biology says should also be present, and is absent here: trained valuation of rolled-out states (E3 at its P0 state) and a consolidation update that improves the model rather than overwriting it. The 314a one-step novelty read is closer to a formal curiosity channel, and at its default weight it is negligible for top-1 selection. No lit-pull commission; no claim is under test.

## 7. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | claim-free; bears on SD-PP-B1 premise |
| Biological reference | clear | prospective hippocampal simulation feeding valuation; see section 6 |
| Developmental / dependency prerequisites | partial | E3 evaluators untrained (P0 trains e2 only); encoder untrained; head only modestly above copy-the-input (skill 0.21 / 0.18 / 0.06). Bounds the meaning of "reach"; not the existence of a route |
| Implementation completeness | complete | rollout route unconditional and live. 314a route **coupled but inert at top-1, by default**: missing link = *neutralising guard or default* (`curiosity_novelty_weight` 0.05, score-bias normalisation OFF, novelty <= 7% of score range). Not a defect of the build under test -- 314a was never the native consumer |
| Environment adequacy | adequate | for a ranking-reach question (5x5, 1 hazard, 1 resource, alpha_world 0.9) |
| Measurement adequacy | adequate (C1/C2); partial (C3) | NULL bit-exact, REINIT positive control 3/3, NOISE_MATCHED context, determinacy gating. C3's top-1 DV cannot register the curiosity route at this weight; rank_discordance is the only (ungated) readout. The 5% bar at n=105 makes seed 42 a one-tick call |
| Integration adequacy | coupled (rollout); coupled but inert (314a) | FULL_SLEEP = SLEEP_BOTH: the world head is the only sleep-changed path into ranking here |
| Scale / capacity | adequate | 3 seeds, 105-317 paired ticks |

**Failure-location (GOV-FAILLOC-1):** mechanism `established`, measures `partial` (C3 only), environment `established`, ree `false`. **Net: not a failure read.** The PASS stands on the load-bearing criterion; the one undetermined criterion is a MEASURES limit on the curiosity route at default weight, correctly declared by the driver. Nothing is chargeable to REE.

## 8. Learning extracted

- **SD-PP-B1's premise was a grep artefact.** The only literal `world_forward` token in `e3_selector.py` is a docstring, but E3 consumes the head's output through `Trajectory.world_states`. A consumer search has to follow the data, not the identifier.
- **The default rollout route carries essentially all world-head reach into E3 ranking** (SLEEP_ROLLOUT_ONLY ~= SLEEP_BOTH on 3/3). The MECH-314a route carries almost none at its default weight.
- **A sleep-sized head change is at the edge of ranking reach, and the reach is not specific to the sleep direction at this norm.** A norm-matched random direction clears the bar on 3/3. Sleep beats noise on seed 123 only (15 vs 7 ticks); seed 42 is 5 vs 7 and seed 456 is 142 vs 143. There is one noise draw per seed and no CI, so what E3 ranking registers here is the magnitude of the change, not its content.
- **The same cycle that reaches E3 degrades the head on 3/3 seeds.** The route exists, and what it would carry into behaviour today is damage, not consolidation.
- **Indexer gap (hygiene):** `_compute_adjudication` ignores `applies_to`, so a correctly scoped, non-load-bearing positive control raises a run-level `precondition_unmet`. Four flat manifests carry `applies_to` (V3-EXQ-418e x2, 418g, 1081).

Node class: the B1 question was `complex (probe-gated)`; the probe has read out and **no residual unknown is owned by the row**. The remaining organism-level blockers already have owners (MECH-572/574 sleep objective; SD-PP-B5 / MECH-573 readability).

## 9. Recommended disposition and routing

**Run:** `evidence_direction` non_contributory (as stamped), `epistemic_category` standard, mark reviewed; clear `precondition_unmet` as C3-scoped. Routing: **governance** (no build, no re-queue, no lit-pull). Re-derive brake: not applicable (claim-free). Granularity-debt trigger: does not fire (no claim cluster).

**Draft evidence_quality_note** (for the run record; claim-free, so not written onto any claim):

> V3-EXQ-1081 (diagnostic, claim-free, PASS 2026-09-23, ree-worker-3, alpha_world 0.9, 3 seeds; failure_autopsy_V3-EXQ-1081_2026-09-24). Yoked-twin counterfactual: a single force_cycle world-head change, swapped into E3 through the DEFAULT proposer-rollout route, re-ranks the E3 top-1 on 5/105, 15/123, 142/317 ticks (C1 2/3 at a 5% bar; NULL twin 0.0 bit-exact; REINIT_BOTH positive control 0.25/0.23/0.64). The reach is magnitude-generic: a norm-matched random head direction re-ranks 7/105, 7/123, 143/317 ticks (3/3). The MECH-314a curiosity route has no top-1 authority at curiosity_novelty_weight 0.05 (random-head positive control 0.009/0.016/0.006, below the 0.10 floor on 3/3), so C3 is undetermined, not negative. The indexer's precondition_unmet flag is that C3-scoped control (applies_to is not read by the indexer); it does not touch C1/C2. Establishes: SD-PP-B1's 'no default-on consumer of e2.world_forward' premise is FALSE (GFLAG-0437). Does NOT establish: that sleep improves anything -- the same cycle DEGRADED held-out world-forward skill on 3/3 seeds -- nor reach through TRAINED evaluators (E3 at its P0 state).

### SD-PP-B1 substrate_queue change (recommended: `amend` -> CLOSED, premise false)

`target_sd_id: SD-PP-B1-world-forward-behavioural-consumer`

- `status`: `proposed_REGISTRATION_ONLY_not_a_build_authorisation` -> `closed_premise_false__default_consumer_exists__GFLAG_0437__V3_EXQ_1081`
- `title` -> "CLOSED 2026-09-24 -- premise false (GFLAG-0437, V3-EXQ-1081): e2.world_forward already reaches E3 candidate ranking by default through HippocampalModule -> E2.rollout_with_world -> E3.score_trajectory; no consumer build is owed"
- `node_class`: remove `complex (probe-gated)` (the probe has read out; no residual unknown owned by the row). `ready` stays false (nothing to build).
- `implementation_hint` -> replaced by the "NO BUILD OWED" text in the JSON artifact (states the route, the 1081 numbers, that the MECH-314a route is the wrong consumer, and what still caps organism-level evidence).
- Retract (keep them, marked RETRACTED): `why_no_existing_owner`, `event_or_manipulation_produced` / `dv_or_instrument_exposed` ("NOT PRODUCED / NOT EXPOSED -- this is the gap"), `ready_blocked_by` ("governance must decide which consumer becomes canonical" -- moot).
- Append `failure_record` item: run_id `v3_exq_1081_..._v3`, metric = the per-twin table above, target "reach bar 0.05 on >= 2/3 seeds -- MET via the default rollout route; the 'no route' premise is refuted", `resolved: resolved`.
- `severity: cosmetic` (a premise error in a registration-only row; no evidence corrupted, though V3-EXQ-1073's preregistered Result-4 ceiling cites it: driver ~:194-196, ~:2333-2334). `substrate_paths`: `ree_core/predictors/e2_fast.py::rollout_with_world`, `ree_core/hippocampal/module.py`, `ree_core/predictors/e3_selector.py::_get_world_states`.
- `unblocks_claims`: drop ARC-137. Its access-repair readout (executed behaviour and ecological consequence with upstream content held fixed) is untouched by 1081.
- Do **not** mint a replacement row. "Reach through trained evaluators / behavioural consequence" is a maturity condition that any organism-level assay has to meet anyway, and the sleep-sign and readability blockers already have rows and claims.

### GFLAG-0437

**Resolve**, in the same cycle that applies the SD-PP-B1 amend, so the flag does not close while the false title persists. Draft resolution note (JSON `gflag_0437_recommendation.resolution_note_draft`): premise-false confirmed by code re-read at ree-v3 `4fc6f3d` (the run itself executed `c6aa52d9`) and empirically by V3-EXQ-1081. The sleep-sized reach is not specific to the sleep direction at this norm. The MECH-572/573/574 / INV-063 leg-B "mechanistic-only" cap is no longer justified by the absence of a route. What remains is the sign of the sleep update, head readability, and untrained evaluators. The MECH-314a route named in B1's hint is not a viable consumer at weight 0.05.

### Read-across (not adjudicated; governance may append)

- **MECH-572**: displacement sits at the optimiser bound at alpha_world 0.9 (max |d| 0.00805 / 0.00797 / 0.00803 vs 0.008), and held-out MSE worsens x1.16-x4.45. That is *consistent with* the optimiser-bounded-displacement premise, and it removes the alpha-0.3 PROVISIONAL caveat on that point. It is **not diagnostic of the displacement-to-residual ratio account**: pre-sleep residual is about constant across seeds (3.24e-5 / 2.87e-5 / 3.07e-5), so the ratio is fixed while damage spans 4x. That spread is content dependence, which MECH-572 neither predicts nor contradicts (red-team F2). Optional note line drafted in the JSON; mark it a re-reading, not scoring evidence.
- **MECH-573**: pre-sleep skill only 0.06-0.21 above copy-the-input at alpha 0.9. Descriptive only.
- **MECH-314a / `curiosity_subflavour_authority` H-novelty-per-candidate** (confirmed by V3-EXQ-604c): **no conflict.** 604c contrasted novelty ON vs OFF; this run contrasts two heads under novelty ON. Do not read it as weakening.
- **INV-063 leg B**: the "no behavioural route" half of the organism-level blocker is gone; the "sleep makes the readout worse" half is re-observed (3/3). Stays `substrate_conditional`.

### Hypothesis-space ledger (Step 9b, drafted only)

No leg adjudicated, no fanout, no Mode A/B/C/D event. One **text correction** proposed for the confirming session: `precision_provenance_consolidation_gain.decision.observation_bottleneck` currently names "no default-on behavioural consumer of it exists (SD-PP-B1)" as a blocker. Drop that clause and cite GFLAG-0437 / V3-EXQ-1081. No invariant is touched.

### Follow-on (reported, not spawned)

- **Indexer hygiene:** make `_compute_adjudication` in `REE_assembly/evidence/experiments/scripts/build_experiment_indexes.py` honour a precondition's `applies_to` (a precondition scoped to a non-load-bearing criterion should not raise the run-level `precondition_unmet`, or should raise a distinct scoped flag). Low priority; 4 manifests affected. A generic route, not governance work, so it is chippable. Chip it from the governance session if the user wants it.
- **V3-EXQ-1073 preregistration Result-4 cap rationale** cites the false B1 premise. Correct it by a note line (governance) and do not edit the landed driver.

## 10. Step 7b / 7c

- **7b** (`autopsy_pre_routing_checks.py`): 0 fires. C1-C3 and C7 are inapplicable because the target is claim-free and has no arm array. C5 was applicable and silent.
- **7c** (red-team, **fable** -- cross-model; drafting on Opus): **CONTESTED (narrowly), routing CONFIRMED.**
  - F1: "no more than a norm-matched random direction" is false on seed 123 (sleep 15/123 vs noise 7/123). Confirmer: arm_results per-seed top1. **Accepted**; B1 hint, GFLAG note and learning reworded.
  - F2: the MECH-572 "signature" framing over-read a fixed-ratio case. Confirmer: the mse_pre column. **Accepted**; read-across reframed.
  - Confirmed: B1 premise-false closure; the precondition_unmet flag is exactly 3 C3-scoped entries; head_max_abs is the world head; the 0.05 default is not overridden; FULL_SLEEP is a distinct build.
  - Hygiene: H1 (Result-4 citation) was rejected on re-check, since the 1073 driver cites it; H4 (run commit vs re-read HEAD) is fixed; H2, H3 and H5 are noted.
