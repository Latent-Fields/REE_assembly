# Failure autopsy: V3-EXQ-606 (MECH-318 GAP-I premature gate)

- **Run**: `v3_exq_606_arc064_gap_i_mech318_multi_rule_empirical_gate_20260521T090253Z_v3`
- **Queue ID**: V3-EXQ-606
- **Outcome**: FAIL, `evidence_direction: non_contributory`, `claim_ids: [MECH-318]`
- **Executed**: 2026-05-21T09:02:53Z on DLAPTOP-4.local
- **Autopsy session**: failure-autopsy-V3-EXQ-606-mech318-20260529T165710Z
- **Scope**: single target; cross-references the in-flight V3-EXQ-490g cohort autopsy at the tail-signature layer without absorbing.
- **Status**: confirmed (user reviewed Step 8 gate 2026-05-29).

## Facts reconstruction

### Manifest

- `gates_on_exq: V3-EXQ-543k` (script-declared scientific gate, [ree-v3/experiments/v3_exq_606_arc064_gap_i_mech318_multi_rule_empirical_gate.py:25](https://github.com/Latent-Fields/ree-v3/blob/main/experiments/v3_exq_606_arc064_gap_i_mech318_multi_rule_empirical_gate.py) line 25 "Scientific gate: interpret only after V3-EXQ-543k contributory PASS (GAP-B).")
- Pre-existing `evidence_direction_note`: "Premature GAP-I gate: run before V3-EXQ-543k contributory PASS (plan resume_condition). C3 rule_state_active PASS (wiring live); C1/C2 behavioral cross-regime failed (1/3 seeds only). Re-queue after GAP-B closure."
- Accepted into governance 2026-05-21 (review_tracker decision_log: "606 MECH-318 premature NC").
- Acceptance flags:
  - `C1_cross_regime: False`  (ARM_2 |reef_frac_eval_H - reef_frac_eval_V| >= 0.12 in >= 2 seeds)
  - `C2_cluster_advantage: False` (ARM_2 cross-regime delta > ARM_0 in >= 2 seeds)
  - `C3_rule_state_active: True` (ARM_2 mean rule_state L2 norm >= 0.005 in >= 2 seeds)
- Per-seed details (3 seeds per arm):
  - ARM_0 cluster_off: rule_state_norm=0 across all seeds; reef_frac_eval=(0.164, 0.0, 0.0); cross_regime_delta=0 by construction.
  - ARM_1 single_regime: rule_state_norm=(0.124, 0.282, 0.064) -- substrate fires; reef_frac=(0.325, 0.0, 0.0); cross_regime_delta=0 (single-axis training by design).
  - ARM_2 multi_rule: rule_state_norm=(0.110, 0.265, 0.073) -- substrate fires; cross_regime_delta=(0.186, 0.0, 0.0). Seed 42 clears the C1 floor (0.186 >= 0.12) with reef_frac_H=0.240 / reef_frac_V=0.054. Seeds 7 and 17 produce reef_frac=0 in both eval axes -- policy never visits reef cells in eval.

### Script

- Pass criteria (script `__main__`): `C1 AND C2 AND C3 -> MECH-318 superseded-by-cluster reading; FAIL -> MECH-318 remains candidate (may motivate dedicated substrate).`
- Script-declared interpretation gate (literal): "Scientific gate: interpret only after V3-EXQ-543k contributory PASS (GAP-B)."
- Script-declared scope caveat: "Episode-boundary multi-rule via alternating bipartite axis; not within-step rule switch. MECH-316/317 not tested (no V3 modules)."
- Env: SD-054 reef + hazard_food_attraction substrate (`reef_bipartite_layout=True`, axis alternation across P1 training episodes); 20/40/16 ep budget P0/P1/P2; 100 steps/ep; 3 seeds (42, 7, 17); 3 arms (cluster_off / single_regime / multi_rule).

### Queue entry

- `gates_on_exq: V3-EXQ-543k` declared in the manifest (and in the script). The gating predecessor V3-EXQ-543k actually ran 2026-05-22T09:17Z and registered FAIL/mixed (`mode_separation_score=0.483 < floor=0.5`, basin stability not met). V3-EXQ-606 executed **2026-05-21T09:02Z, one day before its own scientific gate**.
- `experiment_purpose: evidence`.
- Successor V3-EXQ-606b was queued dry_run-only 2026-05-23 then held (per arc_062 GAP-I resume_condition); a second 606b run 2026-05-27 produced FAIL/weakens same C1/C2/C3 pattern (per review_tracker decision_log 2026-05-27).

### Expected vs observed

- Expected at PASS (per script docstring): C1 AND C2 AND C3 -> MECH-318 "superseded-by-cluster" reading clears (SD-033a + ARC-062 absorbs the in-V3 portion); the multi-rule-context substrate (SD-054 bipartite axis alternation) carries enough rule-context bandwidth that a within-episode behavioural signature differentiates between cluster-OFF and cluster-ON multi-rule arms.
- Observed: C3 wiring-active PASSes (rule_state buffer accumulates non-zero norm in 3/3 seeds for both single-regime and multi-rule arms). C1 cross-regime fails: only seed 42 in ARM_2 clears the discrimination floor; seeds 7 and 17 produce reef_frac=0 in both eval axes (policy never inhabits reef cells in eval). C2 cluster-advantage fails for the same reason (ARM_2 and ARM_0 both report delta=0 in 2 of 3 seeds; ARM_0 by construction).
- Failed criterion type: **discrimination criteria (C1, C2) fail with an absolute wiring criterion (C3) passing**. The classic substrate-ceiling fingerprint, but the "ceiling" here is a downstream-policy-monomodal-collapse fingerprint, not a per-stream-V_s-bandwidth ceiling.

## Claim-layer mapping

[claims.yaml MECH-318](../../docs/claims/claims.yaml) (entry around line 28877):

- `status: candidate`, `v3_pending: true`, `implementation_phase: v3`.
- `depends_on: [ARC-064, ARC-065, MECH-316, MECH-317]`. None of MECH-316/317 has a V3 module; the script's docstring already records this.
- 2026-05-10 absorption-check VERDICT B (partial absorption):
  - W1 (recurrent topology) absorbed by E1 LSTM + SD-033a EMA.
  - W2 (trained across many tasks) **NOT ABSORBED** -- multi-task training distribution blocked on multi-rule-context substrate; SD-054 single-context insufficient.
  - W3 (hidden state encodes task identity) absorbed by ARC-062 Phase 1 gated_policy multi-stream discriminator + SD-033a rule_state buffer.
  - W4 (biases action selection) absorbed by SD-033a compute_bias + ARC-062 gated_policy heads composing additively into dacc_score_bias.
  - W5 (cross-episode hidden-state continuity) **NOT ABSORBED** -- all V3 candidate substrates reset per episode; V4-scope.
- Existing `evidence_quality_note`: "Empirical retire-vs-promote verdict therefore DEFERRED to V3-EXQ-543c-successor on multi-rule-context substrate, sequenced after ARC-062 Phase 2 GAP-B PASS (V3-EXQ-543b) and ARC-062 Phase 3 GAP-C wiring closure." The 543b/543c lineage has since superseded into 543g/h/i/k/l (per claims.yaml + 543l autopsy 2026-05-27); GAP-B status is in-progress, transitively waiting on V3-EXQ-598b's substrate-enrichment-first reading.

`claim_ids` accuracy: The script tags **only MECH-318**, which is correct -- MECH-316 and MECH-317 have no V3 modules so this experiment cannot test them. No tag drift from a predecessor (this is the first scripted MECH-318 evidence run).

**Did the test let the claim express itself?** No. Two prerequisite gates are missing:

- **Upstream gate (declared by the script itself)**: V3-EXQ-543k contributory PASS. The script literally prints "Scientific gate: interpret only after V3-EXQ-543k contributory PASS." 606 ran the day before 543k; 543k FAILed.
- **Substrate gate from the absorption check**: W2 (multi-task training distribution) is named as NOT ABSORBED in V3. SD-054 with episode-boundary axis alternation is the closest V3 approximation, but its bandwidth-for-W2 cannot be evaluated while the upstream policy is monomodal (MECH-309 monomodal-collapse failure mode still active per 543l autopsy 2026-05-27, 598b governance 2026-05-29).

## Biological-reference triage

- **Closest mammalian reference**: orbitofrontal cortex (OFC) cognitive map (Wilson, Takahashi, Schoenbaum & Niv 2014; Schuck et al. 2016 OFC encodes task state). Computational analog: meta-RL recurrent task-state representation (Wang et al. 2018 "Prefrontal cortex as a meta-reinforcement learning system"; Duan et al. 2016 RL^2; Botvinick et al. 2019 review).
- **Required surrounding system**: multi-task training distribution sufficient for the recurrent state to encode task identity (Duan 2016 RL^2 constructively requires this; this is W2 in the absorption-check schema).
- **Biological translation vs formal-definition import**: biological translation with a well-anchored computational reference. Lit-pull `evidence/literature/targeted_review_arc_064_bottom_up_rule_discovery/synthesis.md` exists. **Not the SD-003 / SD-010-11 formal-definition-import failure mode.** No biology-divergence load-bearing signal.
- **Does the failure resemble a missing-dependency signature in the biological reference?** Yes. W2 (multi-task training) is named as NOT ABSORBED in V3; the policy-side prerequisite (rule-context distinct enough to drive bandwidth into the rule-state) requires the upstream MECH-309 monomodal collapse to clear. The empirical FAIL is consistent with running the test while that prerequisite is unmet.
- **Lit_conf vs exp_conf**: exp_conf for MECH-318 is currently zero (no contributory evidence yet); lit_conf is moderate from the targeted_review_arc_064 pull. Quadrant: low-exp / moderate-lit = "plausible_unproven." 606's non_contributory disposition leaves this quadrant unchanged. Not a novel-discovery quadrant signature.

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (premature) | Script declared `gates_on_exq=V3-EXQ-543k` and the gate was not cleared. MECH-318 evidence_quality_note already routes empirical verdict to V3-EXQ-543c-successor on multi-rule-context substrate. |
| Biological reference | clear | OFC task state + Wang 2018 RL^2 well-anchored; targeted_review_arc_064 lit-pull present; no biology-divergence gap. |
| **Prerequisites** | **missing (dominant)** | Gating predecessor V3-EXQ-543k FAIL/mixed 2026-05-22 (mode_separation_score=0.483 < floor=0.5). MECH-309 monomodal-collapse upstream still active per 543l autopsy 2026-05-27 and 598b governance 2026-05-29. W2 multi-task-training prerequisite for MECH-318 NOT ABSORBED in V3 per absorption-check VERDICT B 2026-05-10. |
| Implementation | partial | SD-033a LateralPFCAnalog rule_state + ARC-062 Phase 1 gated_policy + bipartite axis alternation present. C3 PASS confirms wiring is live; rule_state_norm 0.06-0.28 across seeds. ARC-062 Phase 3 GAP-C closure (discriminator -> rule_state source vector) landed 2026-05-17 but downstream MECH-309 collapse not yet resolved. |
| Environment | adequate-for-wiring / borderline-for-claim | SD-054 reef + hazard_food_attraction + bipartite axis present (V3-EXQ-521 PASS substrate readiness). Whether episode-boundary axis alternation carries W2 bandwidth at all is the falsifiable open question -- but cannot be answered while upstream GAP-B keeps the policy monomodal. |
| Measurement | adequate (but uninformative under collapse) | C1 / C2 / C3 well-formed criteria; C3 confirms wiring; C1 / C2 measure behavioural cross-regime which requires the policy to inhabit goal-rich (reef-vs-forage) states. With monomodal policy, eval reef_frac collapses to 0 in 2 of 3 seeds, rendering C1 / C2 measurement uninformative for MECH-318 specifically. |
| Integration | partial | rule_state buffer integrates per-tick (W3); compute_bias composes additively into dacc_score_bias (W4); discriminator -> rule_state source vector wired (GAP-C closure 2026-05-17). W2 multi-task training pressure to make the discriminator content-distinct across rules is missing. |
| Scale / capacity | unknown | Cannot evaluate; the upstream prerequisite blocks. |

**Dominant diagnosis**: **prerequisites-missing (gating predecessor V3-EXQ-543k failure + W2 multi-task-training absorption gap)** with substrate-uniform monomodal-V_s monostrategy tail signature as a co-factor (the same structural property the GAP-4 Tier-1 cohort autopsy + V3-EXQ-543l autopsy + V3-EXQ-598b governance routing all name).

**Recommended `epistemic_category`** (manifest-side recommendation only -- not applied here): `substrate_ceiling`. Note this label is most informative for claims with mixed contributory evidence under capacity-blind substrate; MECH-318 currently has no contributory evidence at all, so the indexer-side dispatch behaviour is already a no-op (the v3_pending gate alone suppresses promote/demote recommendations). The label is recorded for completeness and to mark the kinship with V3-EXQ-598b's MECH-262 reclassification 2026-05-29.

## Cluster pattern (cross-reference, not absorption)

V3-EXQ-606 shares the *substrate-uniform 2-of-3-seed-collapse-to-zero* failure shape with:

| Experiment | Claim | Absolute / negative-control criterion | Discrimination criteria | Tail signature |
|---|---|---|---|---|
| V3-EXQ-606 (this autopsy) | MECH-318 | C3 wiring PASS | C1 cross-regime FAIL (1/3 seeds clear floor), C2 cluster-advantage FAIL | 2/3 seeds reef_frac_eval=0 in both axes |
| V3-EXQ-483c | SD-037 / MECH-280 / MECH-281 | substrate-readiness PASS preceding | behavioural Tier-1 FAIL | substrate-uniform; covered by 490g cohort autopsy |
| V3-EXQ-603c | Q-045 / MECH-313 / MECH-260 | substrate-readiness PASS preceding | phased-training FAIL | substrate-uniform; covered by 490g cohort autopsy |
| V3-EXQ-543l | ARC-062 / MECH-309 | substrate-readiness PASS preceding | branch-e diff-ON gated arms 3/3 inert | monomodal-V_s collapse |
| V3-EXQ-598b | SD-033a / MECH-262 | C1 frozen silent PASS + C2 trainable nonzero PASS | C3 trainable not monomodal FAIL | trained head moves but rule-state monomodal |

**Reading 1 (substrate-enrichment / training-regime)**: a single structural property -- "V3 substrate at default config under standard training does not produce non-trivial goal-rich state coverage" -- drives all of these. The right response is substrate-enrichment at the training-regime level (the GAP-4 cohort autopsy is routing toward this, A2 scaffolded SD-054 onboarding).

**Reading 2 (per-experiment-prerequisites)**: 606 is structurally distinct from the GAP-4 cluster because its dominant layer is prerequisites-at-GAP-B (a tactical gating-predecessor-FAIL), not training-regime-substrate-at-GAP-4. The tail signature is shared but the load-bearing layer is different.

**Decision**: cross-reference (not absorb). 606's load-bearing layer is the script-declared prerequisite gate (V3-EXQ-543k), not the GAP-4 training-regime gap. The GAP-4 enrichment will likely also unblock 606 transitively (because clearing GAP-B / MECH-309 collapse requires the same goal-rich state coverage), but 606's autopsy should not be redundant with the cohort autopsy's recommendations.

## Learning extracted

- The script's own `gates_on_exq: V3-EXQ-543k` is the load-bearing fact. 606 ran before its scientific gate, and the gate has not yet cleared. This is a process-discipline learning, not a substrate or claim learning.
- The substrate-uniform monomodal-V_s monostrategy collapse pattern that drives the GAP-4 Tier-1 cohort also drives 606's C1 / C2 failure even at a fair test (the discrimination criteria measure behavioural cross-regime which requires the policy to inhabit goal-rich states). This reinforces the broader cohort-level reading that the same training-regime gap is the limiting factor across multiple substrate-layer claims.
- MECH-318 W2 (multi-task training distribution) absorption check VERDICT B from 2026-05-10 remains accurate: V3 has no W2 substrate today. SD-054 episode-boundary axis alternation is the closest approximation but cannot be evaluated independently of the upstream policy-side collapse.
- The autopsy confirms the existing governance routing (substrate_queue implementation_hint + claims.yaml evidence_quality_note + arc_062 plan resume_condition) without recommending any new writes.

## Repair pathway

- Routing: **governance-confirmation** (no-op). The existing writes already implement the correct routing:
  - `substrate_queue.json` MECH-318 entry already records `implementation_hint: "Absorption check 2026-05-10 verdict B PARTIALLY ABSORBED. W1+W3+W4 borne by SD-033a LateralPFCAnalog rule_state + ARC-062 Phase 1 gated_policy multi-stream context discriminator + ARC-062 Phase 3 GAP-C planned wiring. W2 (multi-task training) NOT ABSORBED -- blocked on multi-rule-context substrate. W5 (cross-episode hidden-state continuity) NOT ABSORBED -- likely V4-scope. NO NEW V3 SUBSTRATE COMMISSIONED. V3-EXQ-606 non_contributory (premature vs 543k gate)."`
  - `claims.yaml` MECH-318 `evidence_quality_note` already routes the empirical verdict downstream to V3-EXQ-543c-successor on multi-rule-context substrate.
  - `arc_062_rule_apprehension_plan.md` GAP-I `resume_condition` already holds V3-EXQ-606b queueing until 543k successor contributory PASS + GAP-B resolves.
- Substrate-queue write: `action = "none"`. No new substrate to commission; existing MECH-318 entry is correct.
- Claims.yaml write: no edit recommended (user choice 2026-05-29). MECH-318 already carries v3_pending=true + evidence_quality_note routing the verdict downstream. Adding `epistemic_category=substrate_ceiling + pending_retest_after_substrate=true` would be defensible parallel to V3-EXQ-598b's MECH-262 reclassification but would have no indexer-side effect on a v3_pending=true claim with zero contributory evidence; deferred to governance discretion at a later cycle if the kinship needs explicit governance-side marking.
- Manifest write: no edit. `evidence_direction: non_contributory` is already correct.
- Routing label: `governance-demotion` is INAPPROPRIATE here (MECH-318 is candidate v3_pending with no contributory supports to demote). The autopsy artifact's `routing` field is `governance-confirmation` (a no-op confirmation that the 2026-05-21 review's non_contributory disposition was correct).

## Draft `evidence_quality_note` addition (NOT applied here)

For governance reference if a later cycle decides to mark the autopsy explicitly in claims.yaml MECH-318 (user 2026-05-29 chose NOT to apply this in this autopsy artifact):

> V3-EXQ-606 (2026-05-21) FAIL non_contributory confirmed via /failure-autopsy 2026-05-29 as premature GAP-I gate (ran one day before declared gating predecessor V3-EXQ-543k, which FAILed mode_separation_score=0.483 < floor=0.5 on 2026-05-22). C3 wiring active PASSed (rule_state_norm 0.06-0.28 across seeds); C1 / C2 behavioural cross-regime failed under the substrate-uniform monomodal-V_s monostrategy tail signature also driving V3-EXQ-543l / V3-EXQ-598b / the GAP-4 Tier-1 cohort. Empirical retire-vs-promote verdict still DEFERRED to V3-EXQ-543c-successor on multi-rule-context substrate after GAP-B closure (cf. existing absorption-check W2 / W5 gap framing).

## User-confirmed Step 8 disposition

- Routing: Option 1 (governance-confirmation; recommended_substrate_queue_entry.action = "none"; no manifest write; no claims.yaml write).
- MECH-318 claim writes: Option 1 (no claim-side changes).
