---
closure_plan:
  id: arc_062_rule_apprehension
  title: "Rule Apprehension"
  registered: 2026-05-09
  scope_claims: [MECH-309, ARC-062, ARC-063, ARC-064, ARC-065, MECH-312, MECH-312a, MECH-312b, MECH-312c, MECH-312d, MECH-313, MECH-314, MECH-314a, MECH-314b, MECH-314c, MECH-316, MECH-317, MECH-318, MECH-319, Q-043, Q-044, Q-045, SD-054, SD-029, MECH-269]
  sibling_plans: [commitment_closure, sleep_substrate, sd033_governance, goal_pipeline, self_attribution]
  nodes:
    - id: "arc_062_rule_apprehension:GAP-A"
      title: "ARC-062 substrate not implemented (gated-policy heads + learned context discriminator)"
      phase: 1
      status: done
      severity: load-bearing
      owner_exq: V3-EXQ-542
      unblocks_claims: [ARC-062, MECH-309]
      depends_on: []
      cross_plan_link: ["commitment_closure:GAP-1"]
      last_updated: 2026-05-09
    - id: "arc_062_rule_apprehension:GAP-B"
      title: "MECH-309 falsifier: V3-EXQ-543e FAIL non_contributory diagnosed as confound-free head-input bottleneck -> option 2 (head-input augmentation)"
      phase: 2
      status: in-progress
      severity: load-bearing
      owner_exq: V3-EXQ-543g
      unblocks_claims: [MECH-309, ARC-062]
      depends_on: ["arc_062_rule_apprehension:GAP-A"]
      cross_plan_link: ["commitment_closure:GAP-1"]
      last_updated: 2026-05-17
      resume_condition: "IN-PROGRESS 2026-05-17 (blocked on the option-2 ARC-062 substrate change). V3-EXQ-543e ran to completion 2026-05-17T01:02Z (real run, exit ok, ~79 min) and registered FAIL non_contributory {ARC-062: weakens, MECH-309: non_contributory} -- same inert-gating signature as 543b/c/d (probe-gate FAIL all 3 gated-arm seeds; D1=D2=0.0, D3=-0.13). A /diagnose-errors root-cause (failure_autopsy_EXQ-543e_2026-05-17.{md,json}) discriminated the three hypotheses with a direct harness replicating 543e's exact ARM_2 P0 path: H1 (SP-CEM not engaging) FALSE -- candidates have 4.95 unique first-action classes, entropy 1.26, support_preserving_active=0 is the expected stratified-elites signature per V3-EXQ-567; H2 (probe-feature masking / 543b Cause-1 repeat) FALSE -- world_states[0] pairwise L2=0.0 (fix in place), world_states[1] L2~0.013 (~1000x larger than 543b 1e-5, non-degenerate); H3 (genuine substrate finding) CONFIRMED -- the ~5 first-action classes are compressed by E2 world-forward to only 0.22% of the z_world signal magnitude (norm 0.67, cross-candidate std 0.0015) before reaching the z_world-only ARC-062 head, so the head cannot produce behavioural divergence. This is the FIRST 543-lineage run with the 2026-05-11 candidate-distinguishability confound provably absent, so the persistent inert-gating cleanly isolates the ARC-062 head input contract as the bottleneck (substrate is sound but under-fed). The non_contributory direction is left as-is and NOT force-mapped; contributory weight is captured by the autopsy. Next action: /implement-substrate to augment the ARC-062 GatedPolicy head input with the first-action one-hot (pre-registered option 2; quantitatively justified by the autopsy), then re-issue the falsifier as V3-EXQ-543f via /queue-experiment (543d 2x2 factorial + SP-CEM unchanged; only the head input contract changes; supersedes V3-EXQ-543e). ARC-062 substrate-rationale retirement NOT recommended -- the substrate is under-fed, not redundant."
    - id: "arc_062_rule_apprehension:GAP-C"
      title: "ARC-062 discriminator output not routed to SD-033a LateralPFCAnalog.update() source vector"
      phase: 3
      status: in-progress
      severity: high
      owner_exq: TBD
      unblocks_claims: [SD-033a, MECH-262, SD-034]
      depends_on: ["arc_062_rule_apprehension:GAP-B"]
      cross_plan_link: ["commitment_closure:GAP-1"]
      last_updated: 2026-05-17
      substrate_note: "Substrate implemented 2026-05-17 (pre-GAP-B-PASS pre-positioning). LateralPFCConfig.use_discriminator_source (bool, default False) + discriminator_pool_weight (float, 0.3) + discriminator_proj (nn.Linear(1, rule_dim)) added. LateralPFCAnalog.update() gains optional disc_output param. REEConfig gains lateral_pfc_use_discriminator_source + lateral_pfc_discriminator_pool_weight. agent.py reordered: gated_policy block now before lateral_pfc block so gp_output.gating_weight is available as disc_output. 484/484 contracts PASS; 543f dry-run exit 0. All defaults False/0 -- bit-identical backward compat. Validation EXQ (commitment_closure:GAP-1 2-arm ablation) deferred until V3-EXQ-543f returns a contributory result."
    - id: "arc_062_rule_apprehension:GAP-D"
      title: "E3 optimiser does not include lateral_pfc_analog.rule_bias_head.parameters() (SD-033a bias head untrained)"
      phase: 3
      status: in-progress
      severity: high
      owner_exq: TBD
      unblocks_claims: [SD-033a, MECH-262]
      depends_on: ["arc_062_rule_apprehension:GAP-C"]
      cross_plan_link: ["commitment_closure:GAP-1"]
      last_updated: 2026-05-17
      substrate_note: "Substrate implemented 2026-05-17 (pre-GAP-B-PASS pre-positioning). LateralPFCConfig.train_rule_bias_head (bool, default False) added; when True last Linear is NOT zeroed at init. LateralPFCAnalog.bias_head_parameters() method added for optimizer inclusion. REEConfig gains lateral_pfc_train_rule_bias_head (bool, default False). Experiment use: optim.Adam(list(agent.lateral_pfc.bias_head_parameters()), lr=LR) in P1 optimizer. Gradient path: E3 loss -> score_bias -> compute_bias() -> rule_bias_head weights. Default False preserves existing zeroed-last-Linear behavior. Validation EXQ deferred until V3-EXQ-543f contributory result."
    - id: "arc_062_rule_apprehension:GAP-E"
      title: "Multi-strategy scaling probe (>2 strategies) -- distinguishes ARC-062 weak from ARC-063 strong"
      phase: 4
      status: deferred
      severity: medium
      owner_exq: null
      unblocks_claims: [ARC-063]
      depends_on: ["arc_062_rule_apprehension:GAP-B"]
      last_updated: 2026-05-09
    - id: "arc_062_rule_apprehension:GAP-F"
      title: "Clinical / failure-mode tests (trauma-schema / paranoid-rule-field / depressive-rollout-constraint) -- ARC-063 falsifiable predictions (b)"
      phase: 5
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: [ARC-063]
      depends_on: ["arc_062_rule_apprehension:GAP-E"]
      last_updated: 2026-05-09
    - id: "arc_062_rule_apprehension:GAP-G"
      title: "Sleep-vs-waking refinement asymmetry tests -- ARC-063 falsifiable predictions (c) and Pull C lit-pull placeholder"
      phase: 5
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: [ARC-063]
      depends_on: ["arc_062_rule_apprehension:GAP-E"]
      cross_plan_link: ["sleep_substrate:GAP-1"]
      last_updated: 2026-05-09
    - id: "arc_062_rule_apprehension:GAP-H"
      title: "ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-043 / Q-044 / Q-045 ablation EXQs pending"
      phase: "2-3"
      status: partial
      severity: medium
      owner_exq: "V3-EXQ-544 + V3-EXQ-545 (done); Q-043 / Q-044 / Q-045 TBD"
      unblocks_claims: [ARC-065, Q-043, Q-044, Q-045]
      depends_on: ["arc_062_rule_apprehension:GAP-B"]
      last_updated: 2026-05-10
    - id: "arc_062_rule_apprehension:GAP-I"
      title: "ARC-064 bottom-up rule-discovery cluster (MECH-316 / MECH-317 / MECH-318 absorption check done); empirical gate pending"
      phase: "2-3"
      status: partial
      severity: medium
      owner_exq: "TBD (V3-EXQ-543c-successor; gated on GAP-B + GAP-C)"
      unblocks_claims: [ARC-064, MECH-316, MECH-317, MECH-318]
      depends_on: ["arc_062_rule_apprehension:GAP-B", "arc_062_rule_apprehension:GAP-C"]
      last_updated: 2026-05-10
    - id: "arc_062_rule_apprehension:GAP-J"
      title: "MECH-312 precision-gating family registered (MECH-312a / MECH-312b / MECH-312c / MECH-312d sub-MECHs)"
      phase: "2-3"
      status: open
      severity: low
      owner_exq: null
      unblocks_claims: [MECH-312, MECH-312a, MECH-312b, MECH-312c, MECH-312d]
      depends_on: ["arc_062_rule_apprehension:GAP-B"]
      last_updated: 2026-05-17
    - id: "arc_062_rule_apprehension:GAP-K"
      title: "MECH-319 simulation-mode rule-write-gating: substrate landed; V3-EXQ-543c-successor falsifier pending"
      phase: "2-3"
      status: in-progress
      severity: medium
      owner_exq: "V3-EXQ-546 (done); V3-EXQ-543c-successor TBD"
      unblocks_claims: [MECH-319]
      depends_on: ["arc_062_rule_apprehension:GAP-B", "arc_062_rule_apprehension:GAP-H", "arc_062_rule_apprehension:GAP-I"]
      last_updated: 2026-05-10
---
# Rule Apprehension Plan (ARC-062 / MECH-309 / ARC-063)

**Registered:** 2026-05-09
**Status:** active
**Scope:** the rule-apprehension architectural slot identified by MECH-309's
logical-necessity claim. ARC-062 weak reading is the V3-tractable
instantiation; ARC-063 strong reading is the V4-deferred biology-faithful
elaboration. SD-054 reef substrate provides the substrate the falsifier runs
on; SD-029 monomodal-collapse measurement provides the dependent variable.
Sibling plans: [commitment_closure_plan.md](./commitment_closure_plan.md)
(GAP-1 SD-033a bias head training is downstream of this plan's Phase 3),
[self_attribution_plan.md](./self_attribution_plan.md), [goal_pipeline_plan.md](./goal_pipeline_plan.md),
[sleep_substrate_plan.md](./sleep_substrate_plan.md), and
[sd033_governance_plan.md](./sd033_governance_plan.md).

This plan is the durable resume-point for rule-apprehension cluster work
across sessions. When work pauses to handle adjacent paths, the deviation is
logged in the [Decision log](#decision-log) with a resume condition.

---

## One-line framing

> **MECH-309: trainers weight rules they do not invent.** Without a
> non-Bayesian rule-creator at the policy layer, gradient descent on a
> parametric policy collapses to the smoothest single regime good-enough
> across the whole state space. ARC-062 is the V3-tractable architectural
> slot for the rule-creator (gated-policy heads + learned context
> discriminator); ARC-063 is the V4-deferred biology-faithful elaboration
> (distributed CandidateRule field). The SD-054 reef substrate is the
> falsifier; the SD-029 monomodal-collapse measurement is the dependent
> variable; biology has been pulled to ground R1 / R2 / R3 / R4 with
> resolved defaults.

---

## Source artefacts

Provenance for every gap and decision in this plan:

| Artefact | Role |
|---|---|
| MECH-309 / ARC-062 / ARC-063 entries in [docs/claims/claims.yaml](../claims/claims.yaml) | Cluster registration 2026-05-08 -- diagnostic + V3 weak + V4 strong |
| [docs/architecture/rule_apprehension_layer.md](../../docs/architecture/rule_apprehension_layer.md) | 2026-05-04 thought-intake on tolerance-gated rule apprehension |
| [evidence/literature/targeted_review_arc_062_rule_apprehension/SYNTHESIS.md](../literature/targeted_review_arc_062_rule_apprehension/SYNTHESIS.md) | Pull A (8 entries) -- R1 / R2 / R3 verdicts |
| [evidence/literature/targeted_review_arc_062_refuge_forage_ecology/SYNTHESIS.md](../literature/targeted_review_arc_062_refuge_forage_ecology/SYNTHESIS.md) | Pull B (6 entries) -- R4 verdict |
| [docs/architecture/sd_054_reef_enrichment_substrate.md](../../docs/architecture/sd_054_reef_enrichment_substrate.md) | SD-054 reef substrate spec (Phase 2 falsifier env) |
| [evidence/planning/commitment_closure_plan.md](./commitment_closure_plan.md) GAP-1 | Sibling plan; SD-033a bias head training is downstream of this plan's Phase 3 |
| [docs/architecture/sd_033a_lateral_pfc_analog.md](../../docs/architecture/sd_033a_lateral_pfc_analog.md) | SD-033a substrate spec (where the discriminator output gets wired) |
| substrate_queue.json ARC-062 entry (added by this plan registration) | Implementation status anchor |
| Empirical anchors: V3-EXQ-522 substrate-ceiling PASS under heuristic policy; V3-EXQ-433e/433f/523/523a/523b non_contributory under trained policy | The monomodal-collapse signature MECH-309 explains |

---

## Existing substrate (do not duplicate)

What is already in place vs what this plan adds:

| Function | Component | Location | Status |
|---|---|---|---|
| Reef + food-attracted-hazard substrate (Phase 2 falsifier env) | SD-054 reef enrichment substrate | `ree-v3/ree_core/environment/causal_grid_world.py` | implemented; V3-EXQ-521 substrate-readiness PASS 7/7 |
| Multi-arm sweep template (V3-EXQ-522 reef vs heuristic) | Existing experiment scaffolding | `ree-v3/experiments/` | available; reuse pattern |
| SD-033a LateralPFCAnalog (rule_state buffer + bias head) | downstream consumer of ARC-062 discriminator | `ree-v3/ree_core/pfc/lateral_pfc_analog.py` | implemented 2026-04-20; bias head untrained -- the closure-plan GAP-1 |
| SalienceCoordinator + MECH-261 write-gate registry | mode-conditioning the discriminator output (hypothesis_tag generalisation) | `ree-v3/ree_core/cingulate/salience_coordinator.py` | implemented; write_gate("sd_033a") consumed by SD-033a |
| E3Selector | downstream consumer of score_bias from SD-033a | `ree-v3/ree_core/predictors/e3_selector.py` | implemented; `select(score_bias=...)` parameter wired |
| MECH-269 V_s monostrategy substrate | upstream representational precondition (regions must be discriminably represented before the discriminator can route) | `ree-v3/ree_core/hippocampal/`, `ree-v3/ree_core/regulators/vs_rollout_gate.py` | Phase 1 + Phase 2 (ii / iii) + Phase 3 staleness implemented |

What this plan adds:
- New `ree_core/policy/gated_policy.py` module: two scoring heads sharing E3 encoder features + small context discriminator.
- REEConfig flag `use_gated_policy` (default False, bit-identical OFF).
- Wiring from discriminator output into SD-033a `LateralPFCAnalog.update()` source vector (Phase 3).
- Trainable bias head with E3 optimiser inclusion (Phase 3).
- Validation EXQs at Phase 1 (substrate-readiness diagnostic) and Phase 2 (monomodal-collapse falsifier).

---

## Gap inventory

Seven gaps, ordered by leverage. Each is the basis for one row of the
[Status table](#status-table) below.

| Gap | Subject | Severity | Unblocks |
|---|---|---|---|
| **GAP-A** | ARC-062 substrate not implemented: no gated-policy module, no learned context discriminator, no `use_gated_policy` flag | load-bearing | All downstream gaps; the entire MECH-309 falsification chain |
| **GAP-B** | MECH-309 monomodal-collapse falsifier unrun on SD-054 (ARM_0 single-head E3 vs ARM_1 gated-heads with discriminator) | load-bearing | MECH-309 promotion candidate -> provisional; ARC-062 architectural validation; SD-029 measurement gate |
| **GAP-C** | ARC-062 discriminator output not routed to SD-033a `LateralPFCAnalog.update()` source vector. Without this routing, discriminator's training signal does not reach the rule_state EMA | high | SD-033a bias-head training (commitment_closure GAP-1); MECH-262 rule-selective persistence; SD-034 closure-mode-gating from a real rule_state |
| **GAP-D** | E3 optimiser does not include `lateral_pfc_analog.rule_bias_head.parameters()`. Bias head stays at frozen-zero (Go-side mechanically silent) until parameters are added to the optimiser | high | SD-033a behavioural validation; Go-side bias pathway |
| **GAP-E** | Multi-strategy scaling probe (>2 strategies in same env) unscoped. Distinguishes ARC-062 weak-reading sufficiency from ARC-063 strong-reading necessity per the Rigotti 2013 mixed-selectivity caveat (Pull A entry) | medium (V4 flag) | ARC-063 V4 implementation gate |
| **GAP-F** | Clinical / failure-mode tests (trauma-schema / paranoid-rule-field / depressive-rollout-constraint) -- ARC-063 falsifiable predictions (b). Cannot be implemented within ARC-062 alone per the cluster claim text | low (V4 deferred) | ARC-063 V4 |
| **GAP-G** | Sleep-vs-waking refinement asymmetry tests -- ARC-063 falsifiable predictions (c). Also placeholder for the Pull C lit-pull (sleep-vs-waking refinement) deferred from the Pull A / Pull B sequence | low (V4 deferred) | ARC-063 V4; cross-link to sleep_substrate GAP-1 |

---

## Sequenced plan

Six phases. Each phase is small and verifiable. Phases 1-3 are V3 in-scope;
Phase 4 surfaces V4 as load-bearing or not; Phase 5 is V4-deferred.

### Phase 1: ARC-062 substrate landing (GAP-A)

Smallest scope, highest leverage. Without the substrate the entire
falsification chain cannot run.

Deliverables:

1. **New module** `ree-v3/ree_core/policy/gated_policy.py` with `GatedPolicy`
   class. Two scoring heads sharing E3 encoder features (depending on R3
   instantiation choice -- see Open Questions); small context discriminator
   (~16-32 hidden units; sigmoid output over 2 heads). Symmetry-broken init
   so the heads can differentiate from step 0.
2. **Discriminator inputs** = multi-stream per Pull A R1 verdict:
   `(z_world, z_self, z_harm_a)`. Concatenated, projected through a small
   MLP, scalar-sigmoid output in [0, 1]. R1-reduced single-stream variants
   reserved for Pull A R1 falsifier ARM_1a/b/c (see Phase 2).
3. **REEConfig flag** `use_gated_policy` (default False, bit-identical OFF).
   Per-knob defaults: `gated_policy_n_heads = 2`, `gated_policy_disc_hidden = 24`,
   `gated_policy_disc_init_scale = 0.1` (small enough to avoid early
   discriminator over-commitment).
4. **Contract tests** in `ree-v3/tests/contracts/test_gated_policy.py`:
   C1 default-off no-op; C2 backward-compat with all existing experiments;
   C3 discriminator output in [0, 1]; C4 head differentiation under
   symmetry-broken init; C5 simulation-mode gating per MECH-094 (ghost /
   replay paths must not advance discriminator state).
5. **Substrate-readiness diagnostic EXQ** via `/queue-experiment` skill.
   Five sub-tests: (UC1) module instantiates and forward-passes; (UC2)
   master-OFF no-op (bit-identical to baseline E3); (UC3) discriminator
   output varies with `z_world` (input sensitivity); (UC4) head
   differentiation under training pressure; (UC5) MECH-094 simulation gate.

Phase 1 PASS = 5/5 sub-tests + 244+/244+ existing preflight + contracts.

### Phase 2: MECH-309 monomodal-collapse falsifier on SD-054 (GAP-B)

The architecturally load-bearing experiment. Tests the MECH-309 logical-
necessity claim and validates ARC-062's V3 weak-reading instantiation.

Deliverables:

1. **2-arm experiment** ARM_0 (single-head E3, baseline) vs ARM_1 (gated
   heads + discriminator on multi-stream input) on SD-054 reef +
   `hazard_food_attraction` substrate. Same env config, same seeds, same
   training budget; only manipulated variable is `use_gated_policy`.
2. **Hazard-density gradient sub-arms** ARM_1_low / ARM_1_med / ARM_1_high
   to test density-tracking acceptance criterion (Pull B verdict). Density
   levels chosen so ARM_1_med matches V3-EXQ-522 baseline.
3. **R1 input-ablation sub-arms** ARM_1a (`z_world` only), ARM_1b
   (`z_world + z_self`), ARM_1c (full three-stream). Per Pull A R1 verdict:
   ARM_1c expected to clear the falsifier most cleanly; ARM_1a may collapse
   to ARM_0 baseline. Single-arm Phase 2 first; multi-arm Phase 2b if
   single-arm passes.
4. **Pre-registered acceptance criteria** per Pull B R4 verdict (multi-
   signature tolerance window, PASS rule = at least 2 of 4 criteria hold
   with no contradictory signal):

   | Criterion | Test | Source |
   |---|---|---|
   | C1 density-tracking | monotone refuge-use response across hazard density (more hazards → more refuge-use, with chronic-high-risk reduction at high end) | Lima & Bednekoff 1999 |
   | C2 state-dependence | monotone refuge-use response across `drive_level` (underfed → less refuge-use, well-fed → more refuge-use) | Balaban-Feld 2019 |
   | C3 risk-type dissociation | distinct response to feeding-risk (food-attracted hazards in forage zone) vs transit-risk (transitions between reef and forage zone) | Eccard 2020 |
   | C4 cross-seed variation | non-zero coefficient of variation in `reef_visit_fraction` across seeds | Eccard 2020 + Crowell 2016 |

   FAIL signatures (any one is unambiguous): total invariance across all
   four criteria (the unambiguous monomodal-collapse signature MECH-309
   predicts); refuge-use monotonically *increases* with chronic high-risk
   regimes (biologically inverted -- naive "always-flee-when-hazard-present"
   policy rather than relative-risk-pattern-dependent policy).

5. **Falsification routing** from Phase 2 outcome:
   - PASS at option (iii) score_bias level → unblocks Phase 3 (close
     commitment_closure GAP-1).
   - FAIL at option (iii) → route discriminator output to option (i)
     BG-side score-aggregation first (cheaper retry per Gurney/Humphries/
     Redgrave 2015 anchor); then option (ii) trajectory-proposal-level
     hippocampal preplay seeding per Pfeiffer & Foster 2013 anchor; then
     ARC-063 V4 strong reading.
   - Partial PASS (1/4 criteria) → diagnostic via Sundell 2004 partial-
     replication framing; consider Pull A Capkova/Mansouri 2025 OFC /
     PS / ACC sub-function dissociation as next-thing-to-wire.

Phase 2 PASS gates Phase 3.

### Phase 3: Wire discriminator → SD-033a (closes commitment_closure GAP-1)

Completes the architectural loop: ARC-062 generates the rule signal,
SD-033a integrates it into a committed rule_state, the bias head emits
per-candidate score_bias, E3 selects under that bias.

Deliverables:

1. **Add `discriminator_proj` to `LateralPFCAnalog.update()` source vector**
   (GAP-C). Projection from discriminator output (or its pre-softmax logits,
   depending on dimensionality choice) into `rule_dim`. Source vector
   becomes `delta_proj(z_delta) + world_pool_weight * world_proj(z_world) +
   discriminator_pool_weight * discriminator_proj(disc_output)`.
2. **Make bias head trainable** (GAP-D). Add
   `lateral_pfc_analog.rule_bias_head.parameters()` to the E3 optimiser
   (or to a separate Adam at the same learning rate). Gradient flows from
   E3 score-aggregation through `score_bias` back to head weights via the
   existing E3 loss path -- no separate loss term needed.
3. **Default-flag flip** for rule-cue-tagged experiments: when
   `use_gated_policy=True`, also set `use_lateral_pfc_analog=True` by
   default. Other experiments unchanged.
4. **Validation EXQ for GAP-1**: 2-arm ablation (head trainable vs
   frozen-zero) on the ARC-062 + SD-054 stack. Pre-registered acceptance
   per the rewritten commitment_closure GAP-1 Phase 1 deliverable list:
   trainable arm shows non-zero `score_bias` after N episodes AND
   non-trivial reef/forage strategy split (cross-link to ARC-062's
   monomodal-collapse falsifier).

Phase 3 PASS = closes commitment_closure GAP-1 (status `blocked → done`).

### Phase 4: Multi-strategy scaling probe (GAP-E)

Tests ARC-062 weak-reading sufficiency at scale. Runs after Phase 3 PASS.

Deliverables:

1. **SD-054 extension to ≥3 strategies** (e.g., reef + forage + scout, or
   reef + forage A + forage B). Env-only extension; no agent code changes.
2. **3-arm experiment** ARM_0 single-head, ARM_1 ARC-062 weak-reading
   (2 heads), ARM_2 ARC-062 weak-reading (3+ heads). Acceptance per Pull A
   R2 verdict (Rigotti 2013 mixed-selectivity caveat): ARM_1 expected to
   start failing in the 3+ strategy regime; ARM_2 (more heads) may help
   but is engineering-only and does not address the high-dimensional
   mixed-selectivity gap. ARM_2 success surfaces ARC-062 as scalable;
   ARM_2 failure surfaces ARC-063 as load-bearing.

Phase 4 outcome: either confirms ARC-062 V3-sufficient (defer ARC-063 to
genuine V4 work) or surfaces ARC-063 as the next-thing-to-implement.

### Phase 5: V4 deferrals (GAP-F + GAP-G)

Genuinely V4-bound. Flag-only for now.

- **GAP-F clinical / failure-mode tests** (trauma-schema, paranoid-rule-
  field, depressive-rollout-constraint, OCD over-generation, attachment-
  mediated approach-avoid biasing). Per ARC-063 claim text: these "cannot
  be implemented within ARC-062 alone -- they need ARC-063's named
  CandidateRule structure for residue attribution." V4 implementation gate.
- **GAP-G sleep-vs-waking refinement asymmetry** (waking does substantial
  rule-update; sleep does compression / renormalisation / counterfactual
  recombination on top). Also serves as placeholder for **Pull C
  literature pull** (sleep-vs-waking refinement biology) which was
  deferred from the Pull A / Pull B sequence. Cross-link to
  [sleep_substrate_plan.md](./sleep_substrate_plan.md) GAP-1 (the parent
  sleep substrate plan).

### Phase 6: Cross-plan audit

After Phase 3 PASS, walk the apprehension → commitment → closure pipeline
end-to-end:

ARC-062 discriminator → SD-033a `rule_state` (gate-modulated EMA) →
`compute_bias` per-candidate → score_bias added to E3 candidate scores →
E3 selects under modified scoring → committed trajectory enters BetaGate
elevation → MECH-090 latch → execution → SD-034 closure operator on rule
completion → MECH-260 No-Go injection on completed rule → MECH-268 dACC
PE reset.

Deliverable: one integration smoke test in `ree-v3/tests/contracts/`
exercising the full path. Confirms wiring + cross-plan consistency.

---

## Status table

The resume primitive. Updated every session that touches this cluster.

| Gap | Phase | Status | Blocking on | Next action | Owner-EXQ | Last updated |
|---|---|---|---|---|---|---|
| GAP-A | 1 | done | nothing | Substrate landed (ree_core/policy/gated_policy.py + use_gated_policy flag + REEAgent wiring + 5 contract tests + V3-EXQ-542 substrate-readiness diagnostic 5/5 PASS) | V3-EXQ-542 | 2026-05-09 |
| GAP-B | 2 | in-progress | V3-EXQ-543g result (REINFORCE outcome-coupled P1 loss replacing diversification regularizer; queued 2026-05-17; 543f FAIL autopsied) | **UPDATE 2026-05-17 (V3-EXQ-543e FAIL diagnosed -> option 2):** V3-EXQ-543e ran to completion 2026-05-17T01:02Z (real run, exit ok, ~79 min) and registered **FAIL non_contributory {ARC-062: weakens, MECH-309: non_contributory}** -- same inert-gating signature as 543b/c/d (probe-gate FAIL all 3 gated-arm seeds; reef_fraction ARM_0=ARM_1=0.6918, ARM_2=ARM_3=0.5600; D1=D2=0.0, D3=-0.13). A /diagnose-errors root-cause (`failure_autopsy_EXQ-543e_2026-05-17.{md,json}`) ran a direct harness replicating 543e's exact ARM_2 P0 path and discriminated the three hypotheses: **H1 FALSE** (candidates have 4.95 unique first-action classes / entropy 1.26; `support_preserving_active=0` is the expected stratified-elites signature per V3-EXQ-567 -- SP-CEM IS engaging); **H2 FALSE** (world_states[0] pairwise L2=0.0 confirms the world_states[1] fix is in place; world_states[1] L2~0.013, ~1000x larger than 543b's 1e-5 -- probe features non-degenerate); **H3 CONFIRMED** (the ~5 first-action classes are compressed by E2 world-forward to only **0.22%** of the z_world signal magnitude before reaching the z_world-only ARC-062 head). This is the FIRST 543-lineage run with the 2026-05-11 candidate-distinguishability confound **provably absent**, so the persistent inert-gating cleanly isolates the **ARC-062 head input contract** as the bottleneck -- substrate is sound but under-fed. The `non_contributory` direction is left as-is and **NOT force-mapped**; contributory weight is captured by the autopsy + this routing. **Routing: pre-registered option 2** -- /implement-substrate to augment the GatedPolicy head input with the first-action one-hot, then re-issue as **V3-EXQ-543f** via /queue-experiment (543d 2x2 factorial + SP-CEM substrate unchanged; only the head input contract changes; supersedes V3-EXQ-543e). ARC-062 substrate-rationale retirement NOT recommended (under-fed, not redundant). GAP-C/GAP-D stay open, sequenced after a contributory falsifier PASS. See decision-log 2026-05-17. Handoff: V3-EXQ-543e is a completed FAIL now diagnosed -- flag for next governance pass to add run_id to reviewed_run_ids.<br><br>**PRIOR 2026-05-16 (falsifier re-issued on SP-CEM):** GAP-B open -> in-progress. The MECH-309 monomodal-collapse falsifier was re-issued as **V3-EXQ-543e** via /queue-experiment and is now running. 543e = the canonical 543d 2x2 factorial (ARM_0 gated/dacc OFF, ARM_1 dacc-only, ARM_2 gated-only, ARM_3 both; pre-registered D1-D4; PASS=D2 AND D3; claim_ids [ARC-062, MECH-309]; per-claim direction grid) with the ONLY change being all 4 arms now build the agent with support-preserving CEM (use_support_preserving_cem=True + support_preserving_stratified_elites=True + support_preserving_ao_std_floor=0.2 + support_preserving_min_first_action_classes=2 -- the exact config V3-EXQ-567 validated PASS for ARC-065). supersedes V3-EXQ-543d. Local smoke dry-run PASS (12 verdict lines, 36 progress lines, SP-CEM flags verified reaching config.hippocampal in all 4 arms, runner-conformance validated). The 543b/c/d evidence stays non_contributory/weakens (ran on the invalidated collapsed CEM) and is NOT force-mapped -- 543e is the FIRST contributory test of MECH-309. On completion: route per the pre-registered D-grid (PASS D2 AND D3 -> close GAP-B + unblock GAP-C/D; FAIL D1-only -> ARC-062 substrate-rationale review; FAIL all-D-null -> option 2 head-input augmentation). See decision-log 2026-05-16 (V3-EXQ-543e queued).<br><br>**PRIOR 2026-05-16 (closure-map reconciliation):** GAP-B blocked -> open. V3-EXQ-567 PASS (evidence_direction=supports, ARC-065) lifts natural selected_action_entropy 0.012->0.497 and candidate support 1.007->2.810 -- the candidate-feature variance the 2026-05-11 gate required. Next action: re-issue the MECH-309 monomodal-collapse falsifier on the SP-CEM substrate via /queue-experiment. The 543b/c/d non_contributory/superseded evidence was run under the OLD collapsed CEM and is not force-mapped. See decision-log 2026-05-16.<br><br>**UPDATE 2026-05-11 (EXQ-543c review):** V3-EXQ-543c ran 19:02Z and registered FAIL `non_contributory` for both ARC-062 + MECH-309 -- probe_gate_arm_failed on all 3 ARM_1c seeds (n_inert_gating_seeds_arm1c=3); per-seed metrics floating-point-identical between ARM_0 and ARM_1c across reef_fraction / rho / forage_hazard / transit_hazard / risk_type_ratio. 543c is a strict replication of 543b's inert-gating signature on SD-054 bipartite even with the world_states[1] Cause-1 fix applied. V3-EXQ-543d (2x2 factorial of use_gated_policy x use_dacc with MECH-260 anti-recency=0.5; supersedes 543c) is already queued and running -- its outcome supersedes 543c interpretation per its pre-registered D1-D4 grid. See decision-log 2026-05-11 (EXQ-543c) entry for the full routing logic.<br><br>**PRIOR 2026-05-11**: V3-EXQ-543b ran 2026-05-10 and registered `non_contributory` with `inert_gating_detected` on all 3 seeds; mean_tv_distance = max = min = 0.0 exact across 3 seeds x 12 windows x 32 probe states. Diagnose-errors session 2026-05-11T06:35Z--06:44Z surfaced two distinct causes: (1) script-level bug -- candidate_features = world_states[0] = initial_z_world (identical across K candidates by E2FastPredictor convention); (2) substrate-level finding -- even with the bug fixed (world_states[0] -> world_states[1]), CEM proposer at init produces 8 candidates with shared argmax-first-action, continuous-action vectors differing only ~1e-4, post-action world_states diverging only ~1e-5; ARC-062 head consumes z_world-only inputs that are structurally near-indistinguishable. Status `in-progress -> blocked` pending CEM-candidate-distinguishability substrate-readiness diagnostic that characterises first-action entropy, continuous-action L2 spread, and world_states-1 pairwise distance at init and during P0/P1 training. Three architectural options surfaced for downstream resolution (see decision-log 2026-05-11 for the full rationale): (1) land Cause-1 microscopic fix and rerun; (2) augment GatedPolicy head input with first-action (substrate change to ARC-062 contract; belongs under /implement-substrate); (3) **env-side diversification** -- design SD-054 (or successor) so the signals ARC-062 needs are structurally guaranteed-present per candidate by construction (user-direction, 2026-05-11). unblocks_claims tightened to [MECH-309, ARC-062]; SD-029 dropped per claim_ids accuracy rule (SD-054 is not SD-029's measurement substrate). | V3-EXQ-543g | 2026-05-17 |
| GAP-C | 3 | in-progress | GAP-B PASS (V3-EXQ-543g; substrate pre-implemented 2026-05-17) | Substrate DONE (discriminator_proj routing to LateralPFCAnalog.update(); 484/484 PASS). Validation EXQ (commitment_closure:GAP-1 2-arm ablation) deferred until 543g returns contributory result. | TBD | 2026-05-17 |
| GAP-D | 3 | in-progress | GAP-C | Substrate DONE (train_rule_bias_head flag + bias_head_parameters() method; 484/484 PASS). Validation EXQ deferred until 543g contributory result. | TBD | 2026-05-17 |
| GAP-E | 4 | deferred | GAP-D PASS | Extend SD-054 to ≥3 strategies; 3-arm scaling experiment | n/a in V3 | 2026-05-09 |
| GAP-F | 5 | deferred V4 | GAP-E outcome | none in V3 | n/a | 2026-05-09 |
| GAP-G | 5 | deferred V4 | sleep_substrate plan progression | Pull C lit-pull (sleep-vs-waking refinement biology) when ARC-063 V4 work opens | n/a | 2026-05-09 |
| GAP-H | 2-3 | partial | MECH-318 / MECH-319 substrates + Q-043 / Q-044 / Q-045 ablation queue | ARC-065 diversity-generation cluster registered. **MECH-313 substrate landed 2026-05-10** (`ree_core/policy/noise_floor.py` + `REEConfig.use_noise_floor`/`noise_floor_alpha`/`noise_floor_min_temperature` + `select_action` e3.select call site + 11 contract tests + V3-EXQ-544 substrate-readiness diagnostic 5/5 PASS + design doc + claims.yaml status `candidate -> candidate_substrate_landed`). **MECH-314 / MECH-314a/b/c substrate landed 2026-05-10** (`ree_core/policy/structured_curiosity.py` + `StructuredCuriosity` + `StructuredCuriosityConfig` + `REEConfig.use_structured_curiosity` master + 3 independently-togglable sub-flavour switches (`use_curiosity_novelty`/`_uncertainty`/`_learning_progress`) + per-sub-flavour weights + `select_action` `dacc_score_bias` composition site between MECH-295 and MECH-313 + 13 contract tests + V3-EXQ-545 substrate-readiness diagnostic 5/5 PASS smoke + design doc + claims.yaml status `candidate -> candidate_substrate_landed` for parent + 3 children). MECH-318 / MECH-319 substrates + Q-043 / Q-044 / Q-045 ablation experiments remain to be authored. V3 falsification paths: Q-044 three-arm ablation (314a-OFF / 314b-OFF / 314c-OFF) on V3-EXQ-543b/c successors AFTER MECH-318/319 absorption checks; Q-045 4-arm ablation (MECH-313 vs MECH-260 collapse) on V3-EXQ-543b/c successors. | V3-EXQ-544 (done) + V3-EXQ-545 (done) / Q-043 / Q-044 / Q-045 EXQs TBD | 2026-05-10 |
| GAP-I | 2-3 | partial | empirical retire-vs-promote on multi-rule-context substrate (V3-EXQ-543c-successor; downstream of GAP-B + GAP-C closure) | ARC-064 bottom-up rule-discovery cluster registered (ARC-064 anchor + MECH-316 cross-episode regularities + MECH-317 behavioural pattern compression + MECH-318 rule-state abstraction provisional). MECH-315 absorbed into MECH-292/293 ghost-goal substrate per Pull 2 R5. **MECH-318 absorption check done 2026-05-10**: VERDICT (B) PARTIALLY ABSORBED (`REE_assembly/docs/architecture/mech_318_absorption_check.md`). Within-V3 functional weight borne by SD-033a LateralPFCAnalog rule_state + ARC-062 Phase 1 gated_policy discriminator + ARC-062 Phase 3 GAP-C planned wiring. W2 (multi-task training) + W5 (cross-episode continuity) gaps remain; W2 blocked on multi-rule-context substrate, W5 likely V4-scope. NO new V3 substrate commissioned. claims.yaml MECH-318 evidence_quality_note + notes updated; status retained `candidate` pending V3-EXQ-543c-successor empirical gate. MECH-316 / MECH-317 absorption checks separately scoped. V3 falsification path: substrate-design EXQ deferred (requires multi-rule-context substrate beyond SD-054 alone). | TBD (V3-EXQ-543c-successor; gated on GAP-B + GAP-C) | 2026-05-10 |
| GAP-J | 2-3 | open | claims-only registration; **blocked on GAP-B** (additive-logit comparison requires non-inert gating) | MECH-312 parent + MECH-312a/b/c/d sub-MECHs registered (uncertainty / practice-maturity / affective-stream-modulation / V_s-freshness-modulation). MECH-312e controllability/agency deferred per Pull 3 R5 (substrate not available). Multiplicative-gate combination rule registered as architectural default; additive-logit baseline needs a 543g-successor arm (V3-EXQ-543b/c listed as owner is stale -- all non_contributory due to inert-gating, not a multiplicative-vs-additive comparison). depends_on updated to [GAP-B] 2026-05-17. | TBD (543g-successor) | 2026-05-17 |
| GAP-K | 2-3 | in-progress | V3-EXQ-543c-successor (admit_writes=True falsifier with replay-driven invocation) AFTER MECH-313 / MECH-314 / MECH-318 sibling substrates land | MECH-319 simulation-mode rule-write-gating substrate registered as REE-novel substrate-level instantiation of MECH-094 at the arbitration layer. SWR machinery + reverse-replay are the substrate anchors; the categorical write-gate function is REE-novel. **MECH-319 substrate landed 2026-05-10** (`ree_core/regulators/simulation_mode_rule_gate.py` + `SimulationModeRuleGate` + `SimulationModeRuleGateConfig` + `REEConfig.use_simulation_mode_rule_gate` master + `simulation_mode_rule_gate_admit_writes` V3-EXQ-543c falsifier inverse-debug flag + `select_action` GatedPolicy + LateralPFCAnalog call-site wiring + 15 contract tests + V3-EXQ-546 substrate-readiness diagnostic 6/6 PASS smoke + design doc + claims.yaml status `candidate -> candidate_substrate_landed`). MECH-094 NOT modified per Pull 3 R1 + Pull 4 R3 KEEP-AS-IS verdicts. V3 falsification path: artificial-write-channel-routing config flag in V3-EXQ-543c-successor (paired arm: `admit_writes=False` MECH-319 normal vs `admit_writes=True` falsifier with replay-driven invocation; predicted monomodal-collapse re-emergence under the falsifier arm). | V3-EXQ-546 (done) / V3-EXQ-543c-successor TBD | 2026-05-10 |

Status values: `open`, `in-progress`, `blocked`, `paused`, `partial`,
`done`, `deferred`, `registered`. `registered` = claims registered in
claims.yaml; substrate / experiments not yet built. A `paused` row
carries a resume condition in the [Decision log](#decision-log).

---

## Open questions (resolved defaults)

All four open questions sketched at plan-doc registration have biology-
anchored defaults from Pull A and Pull B. Defaults can be revisited if
Phase 1 / Phase 2 evidence motivates a change.

### R1 — Discriminator input streams

**Default: multi-stream `(z_world, z_self, z_harm_a)`.** Single-stream
`z_world`-only is the impoverished case and is reserved for the Phase 2
input-ablation sub-arm.

**Justification (Pull A SYNTHESIS verdict 1):**
- Miller & Cohen 2001 *Annu Rev Neurosci* ([DOI 10.1146/annurev.neuro.24.1.167](https://doi.org/10.1146/annurev.neuro.24.1.167)) — explicit "inputs, internal states, and outputs" framing.
- Rigotti et al. 2013 *Nature* ([DOI 10.1038/nature12160](https://doi.org/10.1038/nature12160)) — single-cell mixed selectivity to multiple task variables.
- Mitchell et al. 2016 *J Neurosci* ([DOI 10.1523/JNEUROSCI.0810-16.2016](https://doi.org/10.1523/JNEUROSCI.0810-16.2016)) — macaque MD network includes insular (interoceptive) cluster as first-class member.

**Falsifier path:** Phase 2 ARM_1a / b / c sub-arms test whether the
multi-stream default is necessary or whether single-stream suffices on
SD-054. PASS at ARM_1a alone would weaken the multi-stream commitment
for V3 scope (engineering-overhead-without-benefit).

### R2 — Discrete heads vs continuous gating

**Default: N=2 heads at Phase 1.** Substrate-constrained: SD-054 reef-vs-
forage is a 2-mode partition by experimental construction, so 2 heads is
the right Phase 1 commitment regardless of biology.

**Caveat (Pull A SYNTHESIS verdict 3):** Rigotti et al. 2013's mixed-
selectivity finding argues PFC's biological mechanism is high-dimensional
continuous mixed selectivity, not discrete head selection. ARC-062's
two-head architecture is a low-dimensional approximation suitable for
SD-054 but expected to break at multi-strategy scaling (Phase 4 / GAP-E).

**Falsifier path:** Phase 4 / GAP-E multi-strategy scaling probe is the
test. ARM_1 (2 heads) failing on a 3+ strategy substrate routes the
diagnosis toward ARC-063 V4 strong reading (distributed CandidateRule
field with continuous tolerance gates).

### R3 — Gating site

**Default: Phase-1 commitment to score_bias level (option iii, current
SD-033a substrate).** Engineering reasons dominate: SD-033a is wired,
`rule_state` buffer exists, gradient path through E3 score-aggregation
is clean.

**Justification (Pull A SYNTHESIS verdict 2):** All three sites are
biologically real; the architectural commitment is a routing choice.
- Option (i) BG-side score-aggregation: Gurney/Humphries/Redgrave 2015 *PLoS Biology* ([DOI 10.1371/journal.pbio.1002034](https://doi.org/10.1371/journal.pbio.1002034)) — cortico-striatal action-reinforcement interface.
- Option (ii) trajectory-proposal hippocampal preplay: Pfeiffer & Foster 2013 *Nature* ([DOI 10.1038/nature12112](https://doi.org/10.1038/nature12112)) — goal-biased forward sequence in rat CA1.
- Option (iii) PFC top-down score_bias: Miller & Cohen 2001; Bongard & Nieder 2010 *PNAS* ([DOI 10.1073/pnas.0909180107](https://doi.org/10.1073/pnas.0909180107)) — PFC rule-coding units controlling information flow.

**Falsification chain:** PASS at option (iii) → close commitment_closure
GAP-1; FAIL at option (iii) → route discriminator to (i) BG-side first
(cheaper retry), then (ii) trajectory-proposal-level, then ARC-063 V4
strong reading.

### R4 — Phase 2 acceptance threshold tolerance window

**Default: multi-signature tolerance window with 4 acceptance criteria,
PASS rule = at least 2 of 4 hold across seeds with no contradictory
signal.** Specific criteria captured in the Phase 2 deliverable table
above (C1 density-tracking, C2 state-dependence, C3 risk-type
dissociation, C4 cross-seed variation).

**Justification (Pull B SYNTHESIS R4 verdict):**
- Lima & Bednekoff 1999 *Am Nat* ([DOI 10.1086/303202](https://doi.org/10.1086/303202)) — canonical theory: allocation tracks temporal risk pattern; chronic-high-risk reduces refuge-use (counterintuitive prediction distinguishing rule-following from naive policy).
- Beauchamp & Ruxton 2010 *Am Nat* ([DOI 10.1086/657437](https://doi.org/10.1086/657437)) — theoretical reassessment: even canonical theory has caveats; field has retained spirit while weakening specifics.
- Sundell et al. 2004 *Oecologia* ([DOI 10.1007/s00442-004-1490-x](https://doi.org/10.1007/s00442-004-1490-x)) — vole field test: 1/5 predictions replicated; partial-replication is the realistic empirical baseline.
- Balaban-Feld et al. 2019 *Oecologia* ([DOI 10.1007/s00442-019-04395-z](https://doi.org/10.1007/s00442-019-04395-z)) — direct fish-refuge state-dependent allocation (highest mapping fidelity to SD-054).
- Eccard et al. 2020 *Oecologia* ([DOI 10.1007/s00442-020-04773-y](https://doi.org/10.1007/s00442-020-04773-y)) — individual variation + risk-type dissociation in voles.
- Crowell et al. 2016 *Ecol Evol* ([DOI 10.1002/ece3.1940](https://doi.org/10.1002/ece3.1940)) — refuge-distance gradient + species variation.

**Sharper FAIL signatures** (any one is unambiguous):
- Total invariance across all four criteria — the unambiguous monomodal-
  collapse signature MECH-309 predicts.
- Refuge-use *increases* monotonically with chronic high-risk regimes —
  biologically inverted; naive "always-flee-when-hazard-present" policy.

---

## Decision log

Append-only. Every architectural choice + every deviation pause / resume.

### 2026-05-17 - GAP-J depends_on corrected to [GAP-B]; stale owner_exq updated

GAP-J `depends_on: []` was a documentation bug. The additive-logit-vs-multiplicative-gate
comparison (MECH-312's core test) is not interpretable while gating is inert -- a contributory
GAP-B result is a prerequisite. Added `depends_on: ["arc_062_rule_apprehension:GAP-B"]`.
`owner_exq` updated from stale `V3-EXQ-543b/c` (all non_contributory for inert-gating reasons
unrelated to combination-rule architecture) to `TBD (543g-successor)`.

### 2026-05-17 - V3-EXQ-543e FAIL non_contributory diagnosed (H3 confirmed): route to pre-registered option 2 (ARC-062 head-input augmentation)

V3-EXQ-543e ran to completion on DLAPTOP-4.local 2026-05-16T23:42:42Z ->
2026-05-17T01:02:03Z (real run, `exit_reason: ok`, `actual_secs=4760.7`,
NOT a crash) and registered **FAIL** with
`evidence_direction: non_contributory`,
`per_claim {ARC-062: weakens, MECH-309: non_contributory}` (pre-registered
`_compute_per_claim_direction` grid; NOT force-mapped). reef_fraction
ARM_0=ARM_1_dacc_only=0.6918, ARM_2_gated_only=ARM_3_both=0.5600; D1 and
D2 deltas exactly 0.0, D3=-0.1317; probe-gate FAIL all 3 seeds in both
gated arms -- the same inert-gating signature as 543b/c/d.

Per the memory rule (non_contributory results need /diagnose-errors, not
force-mapping) the user routed this to /diagnose-errors. A direct
diagnostic harness replicated 543e's exact ARM_2 (gated ON, dacc OFF) P0
stepping path and instrumented
`agent.hippocampal.get_last_propose_diagnostics()` plus the pairwise L2
spread of the exact `candidate_features` tensor the probe uses
(`cat([c.world_states[1] for c in candidates[:8]])`). The three
hypotheses were discriminated:

- **H1 (SP-CEM not engaging at probe time): FALSE.**
  `candidate_unique_first_action_classes` mean **4.95**,
  `candidate_first_action_entropy` mean **1.26**, 32 candidates/propose.
  `support_preserving_active=0/22` is the EXPECTED signature when
  stratified-elites delivers diversity without the injection path
  (V3-EXQ-567's own notes record exactly this). The candidate population
  is genuinely first-action-diverse.
- **H2 (probe-feature masking / 543b Cause-1 repeat): FALSE.**
  `world_states[0]` pairwise meanL2 = **0.0 exact** (confirms the
  world_states[1] fix is correctly in place -- the script is not reading
  the identical pre-action z_world); `world_states[1]` pairwise meanL2
  ~ **0.013**, ~1000x larger than 543b's ~1.2e-5. The probe features are
  non-degenerate.
- **H3 (genuine substrate finding): CONFIRMED.** `world_states[1]` vector
  norm/candidate 0.6705; cross-candidate per-dim std 0.001473; ratio
  **0.0022 (0.22%)**. SP-CEM/stratified produces ~5 distinct first-action
  classes, but E2's world-forward model compresses that categorical
  diversity to 0.22% of the z_world signal magnitude before it reaches
  the z_world-only ARC-062 `GatedPolicy` head. The head cannot convert a
  0.22%-relative signal into behavioural divergence; the probe correctly
  detects inert-gating. (Secondary: only ~9-10% of steps generate fresh
  candidates via an E3 tick; the rest return the MECH-057a cached set --
  expected heartbeat behaviour, not the bottleneck.)

**Interpretation.** 543e is the FIRST run in the 543 lineage where the
2026-05-11 candidate-distinguishability confound is **provably absent**.
With that confound removed, the persistent inert-gating is a clean,
confound-free isolation of the ARC-062 head's z_world-only input contract
as the architectural bottleneck. The substrate (SP-CEM/stratified) is
sound but the head is under-fed: the discriminating signal lives in
action space (4.95 classes) but not in the head's z_world input space.
The script's pre-registered grid maps the probe-gate short-circuit to
`non_contributory` (a conservative pre-registration authored when the
substrate confound was still suspected); the underlying finding is the
substrate-level result the MECH-309 / ARC-062 narrative predicts. The
`non_contributory` manifest direction is left as-is and NOT force-mapped
-- contributory weight is captured by this decision-log entry and the
autopsy artifact, not by relabelling.

**Routing decision: pre-registered option 2 (ARC-062 head-input
augmentation).** Of the three pre-registered FAIL routes (D1-only ->
ARC-062 substrate-rationale review; option 2 head-input augmentation;
ARC-062 retirement / ARC-063 V4 escalation), the diagnosis directly
selects option 2 and quantitatively justifies it: feed the first-action
one-hot (≈5 distinct classes, the strong signal) directly into the
`GatedPolicy` head input rather than relying on the 0.22%-relative
z_world projection. ARC-062 substrate-rationale retirement is explicitly
NOT recommended -- the substrate is under-fed, not redundant; the
mechanism is sound and option 2 is a small, well-scoped contract change.

**Next action.** /implement-substrate: augment the ARC-062
`GatedPolicy` head input with the first-action one-hot (a change to the
ARC-062 head input contract registered in ree-v3/CLAUDE.md -- belongs
under /implement-substrate, not /queue-experiment). Then re-issue the
falsifier as **V3-EXQ-543f** via /queue-experiment: the canonical 543d
2x2 factorial and the SP-CEM substrate are unchanged; only the head
input contract changes. supersedes V3-EXQ-543e. GAP-B stays
`in-progress`, blocked on the option-2 substrate change; GAP-C / GAP-D
stay `open`, sequenced after a contributory falsifier PASS.

**Artifacts.** `evidence/planning/failure_autopsy_EXQ-543e_2026-05-17.md`
+ `.json`. Diagnostic harness `/tmp/diag_543e_spcem.py` (throwaway, not
committed). claims.yaml NOT modified; review_tracker.json NOT modified
(diagnose-errors boundary -- V3-EXQ-543e is a completed FAIL now
diagnosed; flag for the next governance/review pass to add the run_id to
`reviewed_run_ids`).

### 2026-05-16 - V3-EXQ-543e queued: MECH-309 monomodal-collapse falsifier re-issued on the SP-CEM substrate (GAP-B open -> in-progress)

Executes the next action set by the 2026-05-16 closure-map reconciliation
entry below. The CEM-candidate-distinguishability gate having been
satisfied by V3-EXQ-567 PASS (ARC-065 SP-CEM), the MECH-309
monomodal-collapse falsifier was re-issued via the /queue-experiment
skill as **V3-EXQ-543e** (`v3_exq_543e_arc062_spcem_falsifier.py`),
supersedes V3-EXQ-543d.

**Design decision: substrate correction, not redesign.** 543e is a
lettered iteration of the 543 falsifier line per the EXQ versioning
policy -- the scientific question (MECH-309 logical necessity) is
unchanged; the prior 543b/c/d runs were invalidated because they ran on
the OLD collapsed CEM. The canonical 543d 2x2 factorial design is kept
verbatim: arms (ARM_0 gated/dacc OFF, ARM_1 dacc-only
suppression_weight=0.5, ARM_2 gated-only, ARM_3 both), the pre-registered
D1-D4 cross-arm grid, PASS=D2 AND D3, the FAIL-routing tree,
claim_ids=[ARC-062, MECH-309], and the per-claim evidence-direction grid
are all unchanged. The SINGLE change is that the shared
`_make_agent_and_env` `from_dims` call now enables support-preserving CEM
on **all four arms** (it is the fixed substrate, not a factorial axis):
`use_support_preserving_cem=True`,
`support_preserving_stratified_elites=True`,
`support_preserving_ao_std_floor=0.2`,
`support_preserving_min_first_action_classes=2` -- the exact
configuration V3-EXQ-567 validated PASS for ARC-065 (lifted natural
selected_action_entropy 0.0124 -> 0.49, candidate support 1.00 -> 2.80).
No further architectural decision among the three 2026-05-11 options was
required -- the "substrate redesign" branch was effectively taken and
validated by the ARC-065 SP-CEM line, as recorded in the reconciliation
entry below.

**Evidence-validity note.** The 543b/c/d evidence remains
non_contributory / weakens and is explicitly NOT force-mapped: it was
collected on the invalidated collapsed-CEM substrate where the ARC-062
gated heads had no candidate-feature variance to discriminate on
(~1e-4..1e-5 spread). V3-EXQ-543e is the FIRST contributory test of the
MECH-309 monomodal-collapse claim.

**Verification.** /queue-experiment code-review pass + smoke dry-run:
exit 0; 12 verdict lines (4 arms x 3 seeds); 36 `[train] ep N/M` progress
lines with the loop-bound `total_train_episodes` denominator; 12
`Seed/Condition` boundary lines; `gated_policy`/`dacc` toggling correctly
per arm; SP-CEM flags independently verified reaching
`config.hippocampal` in all 4 arms; D1-D4 printout works; ASCII-only;
`validate_experiments.py` runner-conformance PASS; `validate_queue.py`
PASS. Queued (priority 1, DLAPTOP-4.local affinity matching the 543b/c/d
precedent, 540 min, episodes_per_run=108, seeds=3, conditions=4) and
auto-claimed by runner DLAPTOP-4.local at 2026-05-16T23:42:41Z.

**Next action.** On 543e completion, review the outcome and route per
the pre-registered D-grid: PASS (D2 AND D3) closes GAP-B (`in-progress ->
done`) and unblocks GAP-C / GAP-D Phase 3 wiring (discriminator ->
SD-033a LateralPFCAnalog; commitment_closure GAP-1); FAIL D1-only routes
to ARC-062 substrate-rationale review; FAIL all-D-null routes to option 2
head-input augmentation (/implement-substrate). GAP-C / GAP-D remain
`open`, correctly sequenced after the falsifier result.

### 2026-05-16 - Closure-map reconciliation: ARC-065 SP-CEM (V3-EXQ-567) satisfies the GAP-B CEM-candidate-distinguishability gate

Staleness pass triggered after a closure-map review found the plan
status tables 5-8 days behind the runner (now at V3-EXQ-581).

The 2026-05-11 GAP-B bottleneck was: CEM candidate collapse leaves
candidate-feature variance too low for the ARC-062 gated heads to
discriminate, so the MECH-309 monomodal-collapse falsifier line
(V3-EXQ-543b superseded; 543c / 543d non_contributory) could not
deliver. V3-EXQ-567 (PASS, evidence_direction=supports, ARC-065) is the
support-preserving CEM fix: ARM_1 (SP-CEM + stratified + ao_std_floor)
vs ARM_0 (normal CEM) lifts natural selected_action_entropy
0.0124 -> 0.4965 (delta 0.484) and candidate support 1.007 -> 2.810.
That is exactly the candidate-feature variance the 2026-05-11 gate
required. The "substrate redesign" branch of the 2026-05-11 three-way
decision was effectively taken and validated by the ARC-065 SP-CEM line
(V3-EXQ-567 / 573; V3-EXQ-568 differentiable-CEM substrate SD-055 5/5 UC).

Action taken: GAP-B status blocked -> open; owner_exq set to a re-issued
MECH-309 monomodal-collapse falsifier on the SP-CEM substrate (via
/queue-experiment, not yet queued). GAP-C / GAP-D remain `open`,
correctly sequenced after the falsifier re-run. The 543b/c/d evidence
stays non_contributory/superseded (run under the old collapsed CEM) and
must NOT be force-mapped -- the re-run on SP-CEM is the contributory test.

### 2026-05-11 - V3-EXQ-543c FAIL (probe-gate FAIL, non_contributory): isolated-substrate replication confirms ARM_1c inert-gating; superseded by V3-EXQ-543d 2x2 factorial (already running on DLAPTOP-4.local)

V3-EXQ-543c ran 2026-05-11T19:02Z (DLAPTOP-4.local) and registered FAIL with
`evidence_direction: "non_contributory"` per the per-claim grid -- both
ARC-062 and MECH-309 mapped to `non_contributory`. The acceptance grid
recorded `probe_gate_arm_failed=true` with `n_inert_gating_seeds_arm1c=3`
(all 3 seeds in ARM_1c flagged `p1_inert_gating_detected: true`) and the
overall result keyed off the probe gate: only `C4_cross_seed_variation` of
the four substantive criteria passed; `C1_density_tracking` was
`non_contributory_phase2a_corrected_single_density`; `C2_state_dependence`,
`C3_risk_type_dissociation`, and the `pass_rule_met` all FAIL. Per the
pre-registered D-criteria interpretation in the manifest's
`evidence_direction_per_claim`, probe-gate FAIL is the second of the three
pre-registered outcomes, and routes ARC-062 + MECH-309 to `non_contributory`
(neither supports nor weakens) rather than to a `weakens` reading.

**Interpretation (per pre-registered grid):** ARM_1c (full three-stream
gated heads) exhibits the same inert-gating signature 543b surfaced. The
mean `tv_distance` across all 12 probe windows in ARM_1c remains in the
1e-7 to 1e-9 range across all 3 seeds -- well below
`INERT_GATING_THRESHOLD = 0.05`. Per-seed `mean_reef_fraction`,
`rho_drive_vs_reef`, `forage_hazard_rate`, `transit_hazard_rate`, and
`risk_type_ratio` are **floating-point-identical** between ARM_0 and
ARM_1c for every seed pair (seed 0: reef=0.0/0.0, rho=0.164/-0.128;
seed 1: reef=0.87/0.87, rho=-0.049/-0.049; seed 2: reef=0.0/0.0,
rho=0.223/0.223). ARM_1c is a strict replication of the 543b finding on
a different substrate (SD-054 bipartite reef-vs-forage with the post-543b
`world_states[1]` Cause-1 fix incorporated): when ARC-062 runs in
architectural isolation from the MECH-260 + SD-032a/b + SD-033a/b cluster
it was designed to live in, the gated-policy heads cannot produce
behavioural divergence even with the script-level bug fixed.

**Supersession:** V3-EXQ-543d is the natural successor. It is **already
queued and running on DLAPTOP-4.local** (queued 2026-05-11T19:11Z by
parallel session `queue-v3-exq-543d-2026-05-11T1911Z`, claim_id ARC-062,
540 min estimate, picks up after V3-EXQ-540a finishes ~20:30Z). 543d is a
2x2 factorial of `(use_gated_policy, use_dacc)` with MECH-260 anti-recency
`suppression_weight=0.5` on the dACC-ON arms -- testing directly whether
the 543c inert-gating signature reflects (a) actual ARC-062 substrate
failure or (b) absence of BG cluster wiring. **The 543d outcome
supersedes the 543c interpretation.** Per the 543d pre-registered D-grid:
- PASS (D2 AND D3) -> cluster-wiring is the missing piece, both
  substrates contribute -> ARC-062 weak-reading sustained; 543c's
  isolated-substrate inert-gating attributable to missing dACC.
- D1-only PASS -> dACC alone explains alternation; ARC-062 substrate
  redundant; route to ARC-062 substrate-rationale review.
- All-D-null FAIL -> route to option (2) head-input augmentation per the
  2026-05-11 (earlier) decision-log entry on GAP-B blocked-status.

**No new GAP-B status change from 543c alone.** GAP-B remains
`blocked` per the prior 2026-05-11 entry. The CEM-candidate-
distinguishability substrate-readiness diagnostic that was named as the
gate to unblock GAP-B is **partially addressed** by 543d as a
load-bearing-by-cluster falsifier; if 543d clears PASS, the substrate-
readiness diagnostic remains needed only as an explanatory artifact (the
question "what made the difference" rather than "is the substrate
testable"). If 543d FAILs all-D-null, the substrate-readiness diagnostic
escalates to required-before-next-step.

**Files touched in this session:** `arc_062_rule_apprehension_plan.md`
(this decision-log entry); review tracker; WORKSPACE_STATE.md. No
claims.yaml edits; no claim status change (ARC-062 / MECH-309 statuses
unchanged -- evidence is non_contributory, neither supports nor weakens).
The 543c manifest already carries
`evidence_direction_per_claim: {ARC-062: non_contributory,
MECH-309: non_contributory}` and `failure_signatures: []`, so no per-claim
override edit needed. No script written; supersession handled at the
queue level by V3-EXQ-543d (already pushed by parallel session
`queue-v3-exq-543d`). The next plan-doc edit on GAP-B will be authored
after 543d completes.

### 2026-05-11 - GAP-B status `in-progress -> blocked`: V3-EXQ-543b diagnose-errors surfaced CEM-candidate-distinguishability as upstream bottleneck

V3-EXQ-543b ran on Mac 2026-05-10T13:25Z--17:26Z (240 min) and registered
`non_contributory` for ARC-062 / MECH-309 / SD-029 with the
`inert_gating_detected` short-circuit firing on every one of 3 seeds at
MID_TRAINING_EP=30. The behavioural-divergence probe recorded
`mean_tv_distance = max_tv_distance = min_tv_distance = 0.0` (exact float
zero) across **all** 3 seeds x 12 probe windows x 32 probe states.
Exact zero across that variation is not numerical noise -- it is
structural. A diagnose-errors session 2026-05-11T06:35Z--06:44Z (TASK_CLAIMS
session_id `diagnose-v3-exq-543c-2026-05-11T0635Z`) traced the failure to
two distinct causes:

**Cause 1 (script-level bug):** `candidate_features` was built by stacking
`candidates[i].world_states[0]` across the first N_PROBE_CANDIDATES
candidates. By E2FastPredictor convention (`ree_core/predictors/e2_fast.py:316`),
`world_states[0] = initial_z_world` -- the pre-action z_world, IDENTICAL
across all K candidates from a single CEM proposal step. So
`candidate_features` was a [K, world_dim] tensor with K copies of the
same row. Consequence chain: `head_0(features)` and `head_1(features)`
each emit the same scalar across every K row -> `gated_score_bias =
w*h0 + (1-w)*h1` is constant in K -> `softmax(-constant_vector / T)`
is uniform -> TV distance vs the bypass-uniform softmax is exactly
0 for every probe state, every seed, every probe window. The
diversification loss `(head_0_bias - head_1_bias)^2.mean()` was
non-zero only because of the symmetry-broken bias init at
`gated_policy.py:217` (head_0.bias = +0.05, head_1.bias = -0.05);
gradients flowed only into those scalar bias terms (clamped at +/-0.1
by `bias_scale`), never into feature-conditional weights, so the heads
could never learn per-state specialisation regardless of episode count.

**Cause 2 (substrate-level finding, surfaced by direct numerical probe
after the Cause-1 fix was written):** with `world_states[0]` replaced by
`world_states[1]` (first POST-action predicted z_world per candidate),
the pairwise max-diff across 8 candidates becomes **1.2e-5** at t=1,
growing to 2.8e-3 by t=30 -- distinguishable in principle but
microscopic. Resulting `gated_score_bias` varies by ~4e-7 across K;
TV-distance vs bypass ~8.6e-8, still well below `INERT_GATING_THRESHOLD=
0.05`. The deeper finding: at init the CEM proposer produces 8
candidates that all share argmax-first-action=3 with continuous-action
vectors differing only ~1e-4. E2 world_forward is a small-residual
model so post-action z_world diverges by only ~1e-5 at t=1. The ARC-062
substrate is being asked to discriminate between candidates that are
**structurally near-indistinguishable** at the input it consumes
(z_world-only). 543b's "inert gating" signal was over-attributed to
the script bug; even with the bug fixed, the substrate-readiness
premise of the falsifier is in doubt.

**Three architectural options surfaced for resolution:**

  1. **Land Cause-1 fix only (microscopic) and rerun.** Cheap probe; high
     probability of another inert-gating result. Use the result to
     formally retire the "world_states-only head input is sufficient"
     assumption and route to a substrate redesign. Risk: another 4-hour
     non-informative runner slot; result will be hard to disentangle
     from the substrate-design question (substrate intrinsically inert
     vs features-not-distinguishable-enough).

  2. **Augment GatedPolicy head input with first-action.** Concatenate
     the candidate's first-action one-hot to the head input
     (head input dim grows from `world_dim` to `world_dim + action_dim`).
     This is no longer a one-line script fix -- it changes the GatedPolicy
     contract registered in CLAUDE.md and modifies the ARC-062 Phase-1
     substrate. Belongs under `/implement-substrate`, not
     `/diagnose-errors`.

  3. **Env-side diversification: design the world to definitely have the
     signals.** (User direction, 2026-05-11.) Build the substrate so that
     the ARC-062 head consumes inputs that are guaranteed-distinguishable
     across the candidate pool by construction. Concrete instantiations
     to evaluate: (a) extend SD-054 reef partition so reef-vs-forage
     contrast forces actively-different first-action argmaxes per
     candidate; (b) inject env-side stochasticity at episode start so the
     initial z_world carries policy-relevant variance the proposer must
     pass through; (c) curriculum-level perturbation ensuring multiple
     candidate trajectories are individually-distinguishable at t=1.
     This option turns the question "can the substrate produce divergence
     under free parameters" into "given a world where divergence is
     structurally necessary for survival, does the substrate produce
     it" -- a sharper falsifier than the current SD-054 single-density
     setup.

**Decision:** GAP-B status moves from `in-progress` to `blocked`. The
next step is **not** to re-queue the falsifier. A substrate-readiness
diagnostic must characterise CEM-proposer candidate-distinguishability
at init and during training (first-action entropy, continuous-action
L2 spread, world_states-1 pairwise distance, scaled across P0 / P1
training) before any one of the three options is chosen. The
substrate-readiness diagnostic will be authored via
`/queue-experiment` in a separate session (user direction). The plan-
of-record GAP-B `unblocks_claims` field is tightened to
`[MECH-309, ARC-062]`; SD-029 dropped because the SD-054 substrate is
not SD-029's measurement substrate (claim_ids accuracy rule applies
to plan-doc dependency edges too).

Files touched in this session: `arc_062_rule_apprehension_plan.md`
(this entry + GAP-B YAML node status / title / owner_exq /
unblocks_claims / resume_condition + closure-map row); REE_assembly
commit + push pending below. No claims.yaml edits; no claim status
changes (ARC-062 / MECH-309 / SD-029 statuses unchanged). No
substrate-side code touched. Removed in cleanup: scratch
`v3_exq_543c_arc062_phase3_optimized_falsifier_features_fix.py`
script + its dry-run manifest + dry-run signal file (diagnose-errors
session never queued).

Cross-plan links: `commitment_closure:GAP-1` (SD-033a bias head
training) remains blocked transitively via GAP-C (which is itself
blocked on GAP-B). `arc_062:GAP-I` (MECH-318 empirical retire-vs-
promote) remains gated on V3-EXQ-543c-successor; the substrate-
readiness diagnostic does NOT count as that successor.

### 2026-05-10 - GAP-K close: MECH-319 simulation-mode rule-write-gate substrate landed

Third of four ARC-064/ARC-065 child substrates landed today (after
MECH-313 noise-floor + MECH-314 structured-curiosity earlier the same
day; MECH-318 absorption-check is the fourth, completed mid-day with
VERDICT (B) PARTIALLY ABSORBED). MECH-319 substrate is a unified
arbitration-layer simulation-mode write gate that consolidates the
categorical replay-tag gating logic across the existing arbitration-
write call sites (GatedPolicy.forward, LateralPFCAnalog.update) and
exposes a single seam for V3-EXQ-543c-successor falsifier control via
the `admit_writes` inverse-debug flag.

**Module landed.** `ree-v3/ree_core/regulators/simulation_mode_rule_gate.py`
(`SimulationModeRuleGate` + `SimulationModeRuleGateConfig` +
`SimulationModeRuleGateDiagnostics`). Pure-arithmetic regulator (no
`nn.Module` inheritance, no learned parameters); sibling to
`GABAergicDecayRegulator` (SD-036) and `BroadcastOverrideRegulator`
(SD-037). Single primitive `effective_simulation_mode(simulation_mode,
site) -> bool` translating `(master_on, admit_writes, caller_sim)`
into the final admit/block decision per the truth table:

| master | admit_writes | caller_sim | output |
|--------|--------------|------------|--------|
| OFF    | (any)        | (any)      | identity (caller_sim) |
| ON     | False        | False      | False (admit waking) |
| ON     | False        | True       | True  (block sim, MECH-319 normal) |
| ON     | True         | False      | False (admit waking; flag inert) |
| ON     | True         | True       | False (admit sim, V3-EXQ-543c falsifier) |

Idempotent for waking calls regardless of `admit_writes` -- the
falsifier-control asymmetry surfaces only at `caller_sim=True` (replay
paths, ghost-goal probes, DMN passes). Per-site diagnostic counters
(`gated_policy`, `lateral_pfc`, `default`) on `n_calls_total`,
`n_waking_admitted`, `n_simulation_blocked`, `n_simulation_admitted`.

**Config wired through REEConfig + REEConfig.from_dims.**
`use_simulation_mode_rule_gate: bool = False` (master, bit-identical
OFF). `simulation_mode_rule_gate_admit_writes: bool = False`
(V3-EXQ-543c falsifier inverse-debug flag). Construction raises
`ValueError` on `admit_writes=True` without master ON (loud-not-silent
guard against mis-configuration -- the falsifier flag is meaningless
without the substrate to gate).

**Agent wiring at two existing arbitration-write call sites in
`REEAgent.select_action`:** (1) GatedPolicy block: literal
`simulation_mode=False` replaced by
`gate.effective_simulation_mode(False, site=SITE_GATED_POLICY)` and
passed to `gated_policy.forward(...)`. (2) LateralPFCAnalog block:
consult gate via `eff_sim = gate.effective_simulation_mode(False,
site=SITE_LATERAL_PFC)`; skip `lateral_pfc.update(...)` when
`eff_sim=True`, else proceed with existing MECH-261 mode-conditioned
EMA. `compute_bias` still runs (arbitration RECEIVES the bias even
during simulation; only the write-back into `rule_state` is gated).
Per-episode `reset()` clears diagnostic counters.

**MECH-094 NOT modified per Pull 3 R1 + Pull 4 R3 KEEP-AS-IS verdicts.**
The gate is a pre-call coordinator that wraps the `simulation_mode`
argument that callers ALREADY pass. With MECH-319 disabled, every
arbitration-write call site behaves bit-identically to its pre-MECH-319
form. This is the load-bearing architectural invariant -- MECH-094
names the principle (categorical phi(z) write gate keyed to a
hypothesis tag), MECH-319 names the substrate-level instantiation at
the rule-arbitration layer (SWR machinery as the categorical signal,
arbitration-weight updates as the function-site).

**Backward compatibility verified.** 288/288 contract + preflight
tests PASS with master OFF (regression-clean; suite was 273
pre-MECH-319, plus 15 new MECH-319 contracts in
`tests/contracts/test_mech_319_simulation_mode_rule_gate.py`).

**Validation experiment.** V3-EXQ-546 substrate-readiness diagnostic
queued. Six sub-tests UC1-UC5 + UC3b precondition (instantiation +
diagnostic keys; master-OFF backward-compat; truth-table coverage
across the 6 valid `(master, admit_writes, caller_sim)` combinations;
precondition raises `ValueError`; select_action wiring contract --
gate sees waking calls from both `gated_policy` and `lateral_pfc`
sites after one `act_with_split_obs` tick, `n_simulation_*` counters
remain zero on the waking path; MECH-094 invariance -- master-OFF and
master-ON-with-waking-caller produce bit-identical wiring outputs).
Smoke 6/6 PASS 2026-05-10 (manifest scrubbed; runner will write the
canonical PASS manifest from the queued entry).

**Phase 1 vs Phase 2.** Substrate landing only. The behavioural test
that flips `admit_writes=True` and routes a replay-driven invocation
through the rule-arbitration layer is V3-EXQ-543c-successor, deferred
until the MECH-313 / MECH-314 / MECH-318 sibling substrates have
landed AND a replay/DMN call site emerges that exercises
`caller_sim=True` against the wired arbitration sites. Today's commit
exposes the seam and counters; the falsifier validation is downstream.

**Lit-pull synthesis decision.** Existing Pull 3 SYNTHESIS
(`evidence/literature/targeted_review_mech_312_arbitration_divergences/`,
8 entries, lit_conf 0.866 on MECH-094) was judged sufficient -- it
explicitly resolves R1 GENUINE-NOVELTY-CONFIRMED (conf 0.72) with the
substrate-availability anchors (Joo & Frank 2018 SWR review + Foster
& Wilson 2006 reverse replay discriminable signature), and Pull 4 R3
gives the KEEP-AS-IS recommendation that MECH-094 stays as the
architectural principle while MECH-319 instantiates it at the
substrate level. No additional implementation-detail lit-pull
commissioned for this substrate landing.

**Out of scope (separate spawned tasks):** MECH-313 / MECH-314 /
MECH-318 (separately scoped per spawn -- all complete same day);
V3-EXQ-543c-successor falsifier authoring (downstream of this
substrate AND the MECH-313/314/318 sessions).

**Files touched:** `ree-v3/ree_core/regulators/simulation_mode_rule_gate.py`
(NEW); `ree-v3/ree_core/regulators/__init__.py` (export);
`ree-v3/ree_core/utils/config.py` (`REEConfig` fields + `from_dims`
kwargs); `ree-v3/ree_core/agent.py` (import + `__init__`
instantiation + `select_action` GatedPolicy + LateralPFC call-site
wiring + `reset` hook); `ree-v3/tests/contracts/test_mech_319_simulation_mode_rule_gate.py`
(NEW, 15 tests); `ree-v3/experiments/v3_exq_546_mech319_simulation_mode_rule_gate_substrate_readiness.py`
(NEW); `ree-v3/experiment_queue.json` (V3-EXQ-546 appended);
`ree-v3/CLAUDE.md` (MECH-319 SD entry appended); `REE_assembly/docs/architecture/mech_319_simulation_mode_rule_gate.md`
(NEW); `REE_assembly/docs/claims/claims.yaml` (MECH-319 status
`candidate -> candidate_substrate_landed` + evidence_quality_note +
notes update); `REE_assembly/docs/assets/data/claims.json` (rebuilt
by `build_claims_json.py`); `REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md`
(GAP-K row + this decision-log entry); `WORKSPACE_STATE.md`;
`TASK_CLAIMS.json`.

### 2026-05-10 - GAP-I MECH-318 absorption check done: VERDICT (B) PARTIALLY ABSORBED into SD-033a + ARC-062 cluster

MECH-318 (`rule_state_abstraction_substrate` / meta-RL recurrent task-state
representation, Wang 2018 + Duan 2016 RL^2) was registered 2026-05-10 with the
provisional flag `registration_provisional_pending_meta_rl_absorption_check`.
This session ran the architectural absorption check that flag commissioned --
auditing the existing `ree-v3` substrate against the five Wang 2018 / Duan 2016
load-bearing properties before committing to a new substrate landing.

Memo: `REE_assembly/docs/architecture/mech_318_absorption_check.md`.

Three candidate substrates audited:

1. **E1 LSTM** (`ree-v3/ree_core/predictors/e1_deep.py` E1DeepPredictor +
   ContextMemory). Recurrent topology yes; trained-on-rule-discrimination NO;
   per-episode `reset_hidden_state()` so cross-episode continuity NO; bias on
   action selection only indirect (associative prior into HippocampalModule;
   SD-016 cue_terrain_proj into E3). Subtotal: topology-only absorption,
   functional role no.
2. **SD-033a LateralPFCAnalog rule_state buffer** (`ree-v3/ree_core/pfc/
   lateral_pfc_analog.py`). Closest match to "rule-state representation that
   biases action selection". Recurrence-as-EMA per Choice A3 (gate-modulated
   EMA, not LSTM/GRU). Bias head currently frozen-random with last Linear
   zeroed (Choice A2; phased training deferred). rule_state buffer reset per
   episode (V4 extension if cross-episode required). MECH-261 mode-conditioned
   write-gate registry generalises MECH-094 hypothesis tag at the rule-state
   slot.
3. **MECH-269 anchor sets + per-region V_s** (`ree-v3/ree_core/hippocampal/
   anchor_set.py`). Discrete-symbolic state-label encoding via
   `(scale, segment_id, stream_mixture)` keying with dual-trace preservation
   (Bouton 2004). Closer to Schuck 2016 / Wilson 2014 OFC-cognitive-map biology
   than to Wang 2018 RL^2. Architecturally adjacent rather than competing with
   the SD-033a + ARC-062 arm.

Mapping the five Wang 2018 properties onto existing substrate:

- W1 recurrent topology: absorbed (E1 LSTM topology + SD-033a EMA recurrence).
- W2 trained across many tasks: NOT ABSORBED. No multi-task training distribution
  exists in V3 (SD-054 is single-context). This is a *training methodology +
  environment* gap, not a substrate gap.
- W3 hidden state encodes task identity: absorbed by ARC-062 Phase 1
  gated_policy multi-stream (z_world, z_self, z_harm_a) context discriminator
  (per-tick rule-context discrimination, trained on score-aggregation gradient)
  + SD-033a rule_state buffer (substrate-ready, content-empty until Phase 3
  GAP-C wires the discriminator output into the rule_state update path).
- W4 biases action selection: absorbed by SD-033a `compute_bias()` and ARC-062
  gated_policy heads; both compose additively into `dacc_score_bias` before
  E3.select().
- W5 cross-episode hidden-state continuity (the defining RL^2 property): NOT
  ABSORBED. All three candidate substrates reset per episode. SD-033a's notes
  field already records "Cross-episode carry-over is NOT implemented (V3
  simplification; V4 extension if required)". This is likely V4-scope.

**Verdict: (B) PARTIALLY ABSORBED.** The within-V3 portion of MECH-318
(W1 + W3 + W4) is borne by the SD-033a + ARC-062 + ARC-062-Phase-3 cluster.
The within-episode part of Wang 2018 instantiates cleanly on the existing
substrate once Phase 3 GAP-C wires the discriminator into the rule_state
update path. The cross-episode RL^2 part (W5) and the multi-task training
property (W2) remain as MECH-318's legitimate residual scope IF the empirical
verdict turns out to require a dedicated substrate.

NO NEW V3 SUBSTRATE COMMISSIONED. The empirical retire-vs-promote verdict
is deferred to a V3-EXQ-543c-successor on multi-rule-context substrate,
sequenced after:
- ARC-062 Phase 2 GAP-B PASS (V3-EXQ-543b)
- ARC-062 Phase 3 GAP-C wiring closure (discriminator -> SD-033a rule_state)
- A multi-rule-context substrate (SD-054 extension to >=2 reef configurations,
  or equivalent) so the falsifier can exercise the within-episode adaptation
  signature MECH-318 names.

If post-Phase-3 the SD-033a + ARC-062 cluster produces the within-episode
rule-state-adaptation behavioural signature on multi-rule-context substrate,
MECH-318 retires as `superseded` with `superseded_by: SD-033a + ARC-062
(cluster)`. If the cluster fails the signature, MECH-318 promotes to
`candidate -> active` and motivates a dedicated substrate landing (likely
V4-scope given the W5 gap).

Files touched:
- `REE_assembly/docs/architecture/mech_318_absorption_check.md` (new memo)
- `REE_assembly/docs/claims/claims.yaml` (MECH-318 title + evidence_quality_note
  + notes update; status retained `candidate` pending empirical verdict)
- `REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md` (GAP-I
  status row + this entry)
- `REE_Working/TASK_CLAIMS.json` (session claim)
- `WORKSPACE_STATE.md`

Out of scope (separate spawned tasks):
- MECH-313 / MECH-314 / MECH-319 substrates (separately scoped per spawn).
- MECH-316 (`cross_episode_regularity_extraction`, Schapiro 2017 CLS +
  Stachenfeld 2017 SR) absorption check.
- MECH-317 (`behavioural_pattern_compression`, Smith & Graybiel + option-critic)
  absorption check.
- The V3-EXQ-543c-successor experiment authoring (downstream of this verdict
  AND ARC-062 Phase 2 + Phase 3 closure AND multi-rule-context substrate).

Forward-link from the absorption-check memo: until the V3-EXQ-543c-successor
verdict lands, MECH-318's within-episode functional weight is borne by
- SD-033a LateralPFCAnalog rule_state buffer (`ree-v3/ree_core/pfc/
  lateral_pfc_analog.py`; design doc `REE_assembly/docs/architecture/
  sd_033a_lateral_pfc_analog.md`)
- ARC-062 Phase 1 GatedPolicy + context discriminator (`ree-v3/ree_core/
  policy/gated_policy.py`; V3-EXQ-542 5/5 PASS 2026-05-09)
- ARC-062 Phase 3 GAP-C wiring (this plan-of-record's Phase 3 / GAP-C row;
  blocked on Phase 2 GAP-B PASS via V3-EXQ-543b).

### 2026-05-10 - GAP-H further partial close: MECH-314 structured-curiosity substrate cluster landed

Second of the four ARC-065 child substrates landed (MECH-313 noise-floor
landed earlier the same day). Resolves the Pull 1 SYNTHESIS R1 BOTH-CHANNELS-
NEEDED commitment: with MECH-313 + MECH-314 both substrate-landed, ARC-065
carries the full cluster commitment for behavioural-diversity generation.
Remaining ARC-065 / ARC-064 children (MECH-318, MECH-319) continue as
separate spawned tasks.

Substrate:
- Module: `ree-v3/ree_core/policy/structured_curiosity.py`
  (StructuredCuriosity + StructuredCuriosityConfig). Pure-arithmetic, no
  learned parameters, no `nn.Module` inheritance; sibling to MECH-313
  NoiseFloor in the `ree_core.policy` package.
- Three sub-flavours implemented as a single module with master + 3
  independently-togglable sub-flavour switches (per Pull 1 R3 verdict NOT
  to collapse them prematurely; Q-044 holds the resolution path):
    - MECH-314a striatal novelty: per-candidate min-distance from candidate's
      first-step z_world to nearest ACTIVE ResidueField RBF center, normalised
      by candidate-pool mean norm. Genuinely per-candidate [K].
    - MECH-314b frontopolar uncertainty: `e3._running_variance` scalar
      broadcast across [K] (Phase 1; per-candidate refinement deferred to
      Phase 2 follow-on requiring an E1 forward-variance head).
    - MECH-314c learning progress: EMA of `|PE_t - PE_{t-K}|` (Schmidhuber
      first-difference) where PE feed is `e3._running_variance` per tick;
      broadcast scalar across [K] (Phase 1; per-candidate refinement deferred).
- Config: `REEConfig.use_structured_curiosity` (default False; bit-identical
  OFF master) + `use_curiosity_novelty` / `_uncertainty` / `_learning_progress`
  (defaults True) + per-sub-flavour weights (default 0.05 each) + `bias_scale`
  clamp (default 0.1, mirrors `lateral_pfc_bias_scale`) + LP EMA alpha (0.1)
  and window K (5). All wired through `REEConfig.from_dims()`.
- Algorithm: per waking tick, `compute_score_bias` returns `[K]` non-positive
  tensor (lower-is-better convention; curiosity makes novel/uncertain/LP-rich
  candidates more attractive). Composed additively into `dacc_score_bias` in
  `REEAgent.select_action()` immediately after the MECH-295 liking-bridge
  block and BEFORE the MECH-313 noise-floor temperature lift (curiosity
  affects scores; noise floor affects temperature; orthogonal).
- LP feed: `update_prediction_error(pe_scalar=e3._running_variance,
  simulation_mode=False)` called after each `e3.select` cycle in
  `select_action`; advances the 314c LP buffer for next tick.
- MECH-094: `compute_score_bias(simulation_mode=True)` returns `zeros[K]` and
  increments only the simulation-skip counter; `update_prediction_error(
  simulation_mode=True)` no-op on the LP buffer. Match the
  SD-035 / MECH-279 / `gated_policy` / MECH-313 simulation_mode pattern.

Architectural-placement note: a separate `StructuredCuriosity` module at
the `e3.select()` call site, in parallel with MECH-313 NoiseFloor and the
GatedPolicy bias chain. The same Phase-1 placement-vs-consolidation note
that MECH-313 carries applies here -- whether the policy-layer regulators
ultimately consolidate into one module is OPEN pending MECH-318 / MECH-319
substrates and Q-043 / Q-044 calibration. The separate-module choice keeps
each sub-flavour independently togglable, which is what Q-044 needs.
Re-evaluate at the point Q-044 / Q-043 are queued.

Phase 1 honest-scoping caveat: 314a is genuinely per-candidate. 314b and
314c are state-dependent global scalars broadcast across [K] in Phase 1.
The architectural shape is correct (bonus magnitude varies with global
uncertainty / LP; substrate exposes the falsification surface), and Q-044's
three-arm ablation IS a flag-set decision -- the substrate guarantees each
sub-flavour can be turned on/off independently. What Phase 1 does NOT
deliver: distinguishable behavioural signatures per sub-flavour at the
candidate-selection level (broadcast-scalar 314b/c shifts every candidate's
score by the same amount and does not change selection ordering). Per-
candidate refinement of 314b (E1 forward-variance head) and 314c (per-
candidate LP estimate) is a Phase 2 follow-on, deferred until Q-044
surfaces concrete need.

Lit-pull synthesis decision: Pull 1 (`evidence/literature/
targeted_review_arc_065_behavioral_diversity_generation/SYNTHESIS.md`,
9 entries, lit_conf 0.78-0.82) judged sufficient -- it explicitly resolves
R1 BOTH-CHANNELS-NEEDED (Wilson 2014 + Faisal 2008 + Friston 2015), R3
PROMOTE-TO-CLUSTER + sub-flavour split with biological anchors per
sub-flavour (Wittmann 2008 striatal novelty for 314a; Daw 2006 + Friston
2010/2015 EFE for 314b; Schmidhuber 1991 + Pathak 2017 for 314c, flagged
"least biologically anchored / potentially-discardable-if-314a+314b-suffice"),
and R4 continuous-in-computation-triggered-in-dominance. Magnitudes
intentionally not pinned by the lit-pull (Q-043 calibration sweep is the
empirical route; Q-044 three-arm ablation is the sub-flavour independence
falsifier). No additional implementation-detail lit-pull commissioned.

Validation: V3-EXQ-545 substrate-readiness diagnostic (UC1 instantiation;
UC2 master-OFF backward-compat; UC3 sub-flavour flag-set isolation --
314a-only / 314b-only / 314c-only / all-off-master-on each behave correctly,
which is the architectural prerequisite making Q-044 three-arm ablation a
flag-set decision; UC4 select_action wiring contract; UC5 MECH-094
simulation gate). 5/5 PASS smoke 2026-05-10 (manifest scrubbed; runner
will write the canonical PASS manifest from the queued entry).

Contract tests: `tests/contracts/test_mech_314_curiosity.py` 13/13 PASS
(C1 default-off no-op; C2 each sub-flavour fires independently; C3
additive composition; C4 MECH-094 simulation gate; C5 backward-compat
config matrix; reset clears LP buffer + diagnostics; input validation).
Full contracts suite 273/273 PASS (was 253 + 13 new + 7 preflight
unchanged) -- regression-clean; bit-identical OFF guarantee holds.

Status: claims.yaml MECH-314 + MECH-314a + MECH-314b + MECH-314c
all `candidate -> candidate_substrate_landed`; v3_pending: true retained
on all four pending Q-044 three-arm ablation. `evidence_quality_note`
on each entry extended with the substrate-landing implementation note +
Phase-1 honest-scoping caveat for the broadcast-scalar sub-flavours.

Out of scope (separate spawned tasks):
- MECH-318 (rule-state abstraction substrate -- ARC-064 child).
- MECH-319 (simulation-mode rule-write gating).
- Q-043 weight calibration sweep.
- Q-044 three-arm ablation experiment itself (queued AFTER substrate
  landing AND MECH-318/319 absorption checks).
- Q-045 4-arm ablation experiment (MECH-313 vs MECH-260 collapse).
- V3-EXQ-543c (curiosity + meta-RL recurrent baselines arm class).
- Phase 2 per-candidate refinement of 314b/c.

Files touched (this session):
- ree-v3/ree_core/policy/structured_curiosity.py (new, ~330 lines).
- ree-v3/ree_core/policy/__init__.py (export).
- ree-v3/ree_core/utils/config.py (REEConfig fields + from_dims kwargs).
- ree-v3/ree_core/agent.py (import + __init__ instantiation + reset hook
  + select_action score_bias composition + LP feed after e3.select).
- ree-v3/tests/contracts/test_mech_314_curiosity.py (new, 13 tests).
- ree-v3/experiments/v3_exq_545_mech314_structured_curiosity_substrate_readiness.py (new).
- ree-v3/experiment_queue.json (V3-EXQ-545 appended).
- REE_assembly/docs/architecture/mech_314_structured_curiosity_bonus.md (new).
- REE_assembly/docs/claims/claims.yaml (MECH-314 + 314a/b/c status +
  evidence_quality_note + parent notes update).
- REE_assembly/docs/assets/data/claims.json (rebuilt by build_claims_json.py).
- REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
  (GAP-H row + this decision-log entry).
- WORKSPACE_STATE.md, TASK_CLAIMS.json.

### 2026-05-10 - GAP-H partial close: MECH-313 noise-floor substrate landed

First of the four ARC-065 child substrates (MECH-313 noise-floor / MECH-314
structured-curiosity / MECH-318 / MECH-319) landed. Resolves the Pull 1
SYNTHESIS R2 LOAD-BEARING tag for the LC-NE-tonic analog channel; remaining
ARC-065 children continue as separate spawned tasks.

Substrate:
- Module: `ree-v3/ree_core/policy/noise_floor.py` (NoiseFloor + NoiseFloorConfig).
  Pure-arithmetic regulator (no learned parameters; no nn.Module inheritance);
  matches the SD-035 / SD-036 / SD-037 regulator pattern.
- Algorithm at the e3.select() call site in REEAgent.select_action():
  `effective_T = max(baseline_T + noise_floor_alpha, noise_floor_min_temperature)`.
- Config: `REEConfig.use_noise_floor` (default False; bit-identical OFF) +
  `noise_floor_alpha` (default 0.1; SAC-entropy-bonus analog) +
  `noise_floor_min_temperature` (default 1.0; matches existing E3 baseline).
  Wired through `REEConfig.from_dims()`.
- MECH-094 honoured via `compute_effective_temperature(simulation_mode=True)`
  returning baseline unchanged + simulation-skip counter only.

Phase-1 instantiation choice (NOT a settled architectural commitment) --
deviation from the original notes-field implementation hint ("SAC-style
entropy regularisation in the existing GatedPolicy module's per-head
softmax temperature; one-line config addition; no separate substrate
component required"): a SEPARATE NoiseFloor module at the e3.select()
call site rather than per-head temperature inside GatedPolicy. Phase-1
reasoning: MECH-313 is state-independent and currently must fire on
baseline E3 selection too (which the per-head approach inside GatedPolicy
would miss with GatedPolicy disabled). Whether the policy-layer regulators
ultimately consolidate into one module is OPEN pending MECH-314 /
MECH-318 / MECH-319 implementations -- those substrates may make different
placement choices that motivate revisiting MECH-313's placement (MECH-314
structured-curiosity in particular may fit naturally inside GatedPolicy
as a per-head bonus, in which case MECH-313 may want to co-locate). Re-
evaluate at the point Q-045's 4-arm ablation is queued (i.e. once MECH-314
is also landed and the whole ARC-065 surface is visible). The Phase-1
module surface + config knobs are stable; what could move is the file
location and call site. Hint updated in claims.yaml notes field with the
same softening.

Validation:
- V3-EXQ-544 substrate-readiness diagnostic, 5/5 PASS smoke (UC1
  instantiation; UC2 master-OFF backward-compat; UC3 lift-arithmetic
  sweep across alpha/min_temperature; UC4 select_action wiring contract
  via act_with_split_obs; UC5 MECH-094 simulation gate). Manifests
  scrubbed; runner will write the canonical PASS manifest from the
  queued entry.
- 11 contract tests in `tests/contracts/test_mech_313_noise_floor.py`
  PASS; full contracts suite 253/253 PASS (regression-clean -- bit-
  identical OFF guarantee holds).

Status: claims.yaml MECH-313 `status: candidate -> candidate_substrate_landed`
with `v3_pending: true` retained until Q-045 behavioural validation runs.
Design doc `REE_assembly/docs/architecture/mech_313_stochastic_noise_floor.md`
landed.

What this enables:
- Q-045 4-arm ablation (both-OFF / 313 only / 260 only / both ON) on
  V3-EXQ-543b/c successors -- the falsifier of whether MECH-313 and
  MECH-260 collapse into a single anti-monostrategy substrate.
- Q-043 parametric sweep on `noise_floor_alpha` and
  `noise_floor_min_temperature` (downstream of Q-045 if MECH-313 is
  shown load-bearing).
- The 2026-05-10 sleep-substrate reclassification cohort (V3-EXQ-418m /
  436b / 500b / 503b) gains one of the two upstream channels needed
  for non-degenerate waking diversity.

Out of scope (separate spawned tasks):
- MECH-314 / MECH-314a/b/c structured-curiosity substrates.
- MECH-318 / MECH-319 substrates.
- The Q-045 4-arm ablation experiment itself (queued AFTER MECH-314
  also lands so the 4-arm matrix can be exercised meaningfully).

Files touched: `ree-v3/ree_core/policy/noise_floor.py` (new),
`ree-v3/ree_core/policy/__init__.py` (export), `ree-v3/ree_core/utils/config.py`
(REEConfig fields + from_dims kwargs), `ree-v3/ree_core/agent.py` (import +
__init__ instantiation + reset hook + select_action e3.select effective-T
override), `ree-v3/tests/contracts/test_mech_313_noise_floor.py` (new, 11
tests), `ree-v3/experiments/v3_exq_544_mech313_noise_floor_substrate_readiness.py`
(new), `ree-v3/experiment_queue.json` (V3-EXQ-544 appended),
`REE_assembly/docs/architecture/mech_313_stochastic_noise_floor.md` (new),
`REE_assembly/docs/claims/claims.yaml` (MECH-313 status + notes update),
`REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md` (GAP-H
status row + this entry), `REE_assembly/WORKSPACE_STATE.md`,
`REE_Working/TASK_CLAIMS.json`.

### 2026-05-10 - Pending FAIL triage: ARC-065 dependents reclassified non_contributory

Triggered by user observation: with ARC-065 (behavioral-diversity-generation
pathway) registered as a foundational upstream cluster on 2026-05-10, a number
of completed experiments that appeared to have FAILed are actually
non_contributory because they require behavioural diversity AS INPUT (not as
output) and the agent is presently in monomodal collapse without ARC-065
substrate landed.

Reclassifications (all in REE_assembly/evidence/experiments/):

- **V3-EXQ-418l** (SD-017 sleep action_bias_div discriminative pair):
  with_action_bias_div = without_action_bias_div = 0.000450 bit-identical
  every seed; signed_diff = 0.0; abs_diff = 0.0; slot_diversity also
  bit-identical. Sleep cannot diversify what was never diverse.
  Reclassified `evidence_direction: weakens -> non_contributory`.
- **V3-EXQ-436a** (SD-017 + ARC-045 + MECH-166 sleep refinement of
  context-conditioned harm threshold): waking and SWS_THEN_REM produced
  bit-identical slot_cosine_sim and harm_rate_dangerous in every seed
  (seed 42: waking 0.000966 = SWS_THEN_REM 0.000966 for slot; waking
  0.003697 = SWS_THEN_REM 0.003697 for harm_dang). Sleep refinement of
  bit-identical waking content can only produce bit-identical sleep
  content. Reclassified `evidence_direction: weakens -> non_contributory`
  for all three claims.
- **V3-EXQ-530c** (ARC-016 dynamic-precision precision-to-commit pathway):
  ARM_0 (use_dacc=False) and ARM_1 (use_dacc=True) bit-identical at
  commit_rate=1.0 and precision=211.85. Precision-to-commit pathway
  cannot register signal under saturated commit policy. Reclassified
  `evidence_direction: weakens -> non_contributory`. Supersedes the
  morning-digest /diagnose-errors deferral with the upstream-substrate
  explanation; Q-042 contract test C0 (rv differs from precision_init)
  was passed -- the issue is downstream behavioural saturation, not
  rv liveness.

NOT reclassified -- one pending FAIL:

- **V3-EXQ-141d** (MECH-111 novelty drive ablation): per_seed_action_
  divergence ~56% (actions DO diverge), but mean_entropy_gap = 7.4e-15
  and mean_cell_gap = -0.67. This experiment IS the diversity-generator
  test, not a diversity consumer. Kept `evidence_direction: weakens`
  against MECH-111 specifically (falsifies the strong reading: novelty-
  bonus-alone-produces-diversity), but added cross-link note tying its
  FAIL pattern to ARC-065 R1 BOTH-CHANNELS-NEEDED verdict (novelty
  bonus alone insufficient without LC-NE-tonic noise floor MECH-313).
  Read together with the cluster registration, this run is informative
  evidence FOR the multi-channel cluster shape.

Precedent for the pattern: SD-029 retest cohort (V3-EXQ-433 / 433a /
433b / 470 reclassified non_contributory 2026-04-25 .. 2026-05-08
because monomodal policy could not generate balanced agent-vs-env
event distributions for C2 / C3 measurement; substrate -- scheduled_
external_hazard env knob -- was in place). Today's reclassification
generalises that precedent from "substrate-not-generating-balanced-
events" to "substrate-not-generating-behavioural-diversity-period",
which is the ARC-065 cluster's whole reason to exist.

How this came about (root-cause reflection): ARC-065 was registered
2026-05-10 (today) but the experiments above were authored across
2026-05-08 .. 2026-05-09, before the cluster existed. The sleep_
substrate_plan.md GAP-2 owner-EXQ list (265a + 418l + 436a + 500a +
503a) was framed against an implicit assumption that the agent would
have natural waking diversity for sleep to refine. The 543/543b
sequence and the cluster registration revealed that the assumption
was load-bearing and not yet substantiated. There is no question of
"work that should have been blocked" in a strict sense -- the gating
claim (ARC-065) did not exist when the experiments were authored.
What was missing was a registered upstream behavioural-diversity
precondition. Now that ARC-065 is registered, we have the gate.

What is now blocked given ARC-065:

| Plan / cohort | Blocking | Resume condition |
|---|---|---|
| sleep_substrate_plan.md GAP-2 (Phase 2 owner-EXQ list 418l + 436a + 500a + 503a) | upstream-blocked by ARC-065 substrate | V3-EXQ-543b/c PASS demonstrating non-degenerate behavioural diversity in waking phase, then re-queue 418m / 436b / 500b / 503b under the diversity-substrate stack |
| arc_062 GAP-B (already ran_inconclusive) | already in V3-EXQ-543b pickup | unchanged -- 543b is the falsifier path |
| arc_062 GAP-C / GAP-D (Phase 3 wiring) | downstream of GAP-B / V3-EXQ-543b PASS | unchanged |
| Future ARC-016 / dACC precision-to-commit retests | upstream-blocked by ARC-065 substrate | ARC-065 substrate produces non-degenerate cross-seed commit-rate variation, then re-queue V3-EXQ-530d |
| Future SD-029 retests | upstream-blocked by ARC-065 (and MECH-269 V_s -- pre-existing) | ARC-065 + MECH-269 V_s both landed |

Sub-plan note for rule apprehension: ARC-065 cluster is a SIBLING
plan to arc_062 rather than a sub-plan. The dependency direction is
ARC-065 (foundational, depends_on []) -> ARC-062 (top-down rule
selection, presupposes diversity to choose between) and ARC-064
(bottom-up rule extraction, presupposes diversity to extract patterns
from). The arc_062 plan-doc currently contains the cluster
registration in its decision log (2026-05-10 entry above this one);
if ARC-065 / ARC-064 substrate work grows beyond what the arc_062
status table can absorb, the appropriate move is to spin up
`arc_065_behavioral_diversity_plan.md` and `arc_064_bottom_up_rule_
extraction_plan.md` as siblings to this plan, with cross-plan-link
fields wiring them into the gap inventories. Defer until V3-EXQ-543b
PASS clarifies which substrate ARC-065 actually needs.

Files touched: REE_assembly/evidence/experiments/v3_exq_418l_*,
v3_exq_436a_*, v3_exq_530c_*, v3_exq_141d_* manifests
(evidence_direction + evidence_direction_per_claim +
evidence_direction_note); REE_assembly/evidence/experiments/review_
tracker.json (4 reviewed_run_ids appended; last_review_utc forwarded;
discussion_notes session-block appended); arc_062_rule_apprehension_
plan.md (this entry); sleep_substrate_plan.md (GAP-2
upstream-block note); WORKSPACE_STATE.md; TASK_CLAIMS.json.

### 2026-05-10 - Cluster registration session: ARC-064 + ARC-065 + MECH-312 sub-MECH split + MECH-319 registered

Major architectural commitment session. Eighteen new claim entries
landed in `docs/claims/claims.yaml` (claims.json count 591 -> 609);
governance pipeline ran clean (1017 runs / 1278 lit entries / 282
proposals; 7 indexed pending review). No experiment scripts written
this session per scope-discipline (V3-EXQ-543b/c authoring is the next
session).

**New cluster anchors (architectural commitments, both v3_pending):**

- **ARC-065** — `behavioral_diversity_generation_pathway`
  (multi-substrate distributed: LC-NE tonic + frontopolar curiosity
  + striatal novelty + hippocampal trajectory sampling). Per Pull 1
  PROMOTE-TO-CLUSTER (conf 0.82) + Pull 4 R4 HYBRID-naming. Logically
  upstream of both ARC-062 top-down and ARC-064 bottom-up rule
  pathways: trainers do not invent diversity any more than they
  invent rules.
- **ARC-064** — `bottom_up_behavioral_pattern_extraction_pathway`
  (hippocampal_CLS_bi_pathway + dorsolateral_striatum_chunking +
  OFC_cognitive_map analog). Per Pull 2 PROMOTE-AS-SEPARATE-CLUSTER
  (conf 0.84) + Pull 4 R4 HYBRID-naming. Architectural counterpart
  to ARC-062: where ARC-062 receives a context cue and selects a
  policy mode, ARC-064 receives observed-behaviour and extracts
  cross-episode regularities. Both presuppose ARC-065 upstream.

**New mechanism claims (all candidate, v3_pending):**

ARC-065 children:
- **MECH-313** — `stochastic_noise_floor` (max_entropy_policy_
  regularisation_LC_NE_tonic_analog). Distinct from MECH-260 dACC
  anti-recency; Q-045 falsifies the collapse question.
- **MECH-314** — `structured_curiosity_bonus`
  (frontopolar_uncertainty_driven_exploration_expected_free_energy_
  analog). Parent of three sub-flavours that Pull 1 R3 explicitly
  recommended NOT to collapse prematurely:
  - **MECH-314a** novelty_bonus_striatal_analog (Wittmann 2008)
  - **MECH-314b** uncertainty_driven_curiosity_frontopolar_analog
    (Daw 2006 + Friston EFE)
  - **MECH-314c** learning_progress_curiosity_intrinsic_motivation_
    analog (Schmidhuber/Pathak; least biologically anchored —
    flagged as potentially-discardable if 314a + 314b suffice)

ARC-064 children:
- **MECH-316** — `cross_episode_regularity_extraction`
  (episodic_RL_successor_representation_CLS_monosynaptic_analog;
  Schapiro 2017 + Stachenfeld 2017)
- **MECH-317** — `behavioural_pattern_compression`
  (option_formation_striatal_chunking_analog; Smith & Graybiel +
  Bacon/Harb/Precup option-critic)
- **MECH-318** — `rule_state_abstraction_substrate`
  (meta_RL_recurrent_task_state_representation; Wang 2018 + Duan
  2016 RL^2). Flagged registration_provisional_pending_meta_rl_
  absorption_check — may be absorbed into existing latent stack
  if V3-EXQ-543c absorption check shows the recurrent state
  already supports rule-state abstraction.

MECH-312 sub-MECH split (Pull 3 R5, conf 0.78):
- **MECH-312** (parent, reworded as
  `rule_arbitration_multi_variable_multi_channel_dynamic_within_
  session`) — registered as fresh parent claim with multiplicative-
  gate as architectural-default-pending-empirical-validation per
  Pull 3 R4 (conf 0.74); additive-logit baseline is the
  falsifying alternative in V3-EXQ-543b/c.
- **MECH-312a** uncertainty_reliability_weighting (Daw 2005 / Lee
  2014; LOW divergence)
- **MECH-312b** practice_maturity_weighting (Smith & Graybiel +
  Stachenfeld 2017 SR maturation; LOW-MEDIUM divergence)
- **MECH-312c** affective_stream_modulation_of_arbitration_REE_
  novel (SD-010/011 anchored structurally; functional consequence
  is REE-novel; MEDIUM-HIGH divergence)
- **MECH-312d** V_s_freshness_modulation_per_region_REE_novel
  (Behrens 2007 + Bouton 2004 nearest cousins; per-region scope
  + rule-trust function REE-novel; HIGH divergence)
- **MECH-312e** controllability/agency modulation (Gershman 2021
  anchor) — DEFERRED per Pull 3 R5 pending V3 substrate
  availability; flagged in MECH-312 evidence_quality_note.

REE-novel arbitration substrate:
- **MECH-319** — `simulation_mode_rule_write_gating_categorical_
  replay_tag` (SWR_machinery_substrate_REE_novel_function).
  Per Pull 3 R1 GENUINE-NOVELTY-CONFIRMED (conf 0.72) + Pull 4 R3
  KEEP-AS-IS. Substrate-availability premise is well-anchored
  (Joo & Frank 2018 SWR review + Foster & Wilson 2006 reverse
  replay); the specific REE function (categorical write-gate at
  the arbitration layer keyed to a simulation-mode tag) is the
  REE-novel claim. **MECH-094 NOT MODIFIED** per Pull 3 R1 + Pull 4
  R3 KEEP-AS-IS — MECH-094 names the architectural principle;
  MECH-319 is its substrate-level instantiation at the arbitration
  layer.

**New open questions:**
- **Q-043** — relative-weight calibration of MECH-313 vs MECH-314
  (parametric sweep on V3-EXQ-543b)
- **Q-044** — independence of MECH-314a/b/c sub-flavours (three-arm
  ablation; defer empirical resolution)
- **Q-045** — MECH-313 vs MECH-260 collapse question (4-arm
  ablation: both-OFF / 313-only / 260-only / both-ON on V3-EXQ-543b)

**MECH-315 absorption (no new claim):** Per Pull 2 R5 verdict (conf
0.74), MECH-315 candidate (proposal-diversity-channel via
hippocampal trajectory sampling, Pfeiffer & Foster 2013) is
ABSORBED into existing MECH-292 ranked ghost-goal bank + MECH-293
awake ghost-goal probes substrate. NOT registered as a separate
claim. Cross-reference notes added to MECH-292 + MECH-293
evidence_quality_note.

**HYBRID-naming convention rationale (Pull 4 R4):** Cluster claims
carry titles that name BOTH the REE-internal architectural-function
name AND the literature anchors, making the cluster machine-grep-
able under both REE-native search ("behavioral diversity",
"bottom-up rule discovery") and literature-search ("MaxEnt RL",
"frontopolar curiosity", "successor representation", "option-
critic", "OFC cognitive map", "contention-scheduling-arbitration").
Pull 4 R4 distributed claim names across KEEP-AS-IS (4 genuine REE
divergences), RENAME-TO-EXISTING (none applied this session — all
literature-anchored claims went HYBRID), and HYBRID (the bulk of
new registrations).

**DEFERRED candidates flagged for follow-up lit-pulls (NOT
registered as claims this session):**

- **Candidate MECH-320** — `interrupted_task_resumption_substrate`
  + V_s context-saving extension + reconciliation-rule Q-claim.
  Per memory entry `project_interrupted_task_resumption_gap.md`:
  REE has world-staleness invalidation but no Zeigarnik-style
  "agent was working on X, got interrupted, resume when capacity
  allows" mechanism. Anchors: Zeigarnik 1927 + Altmann & Trafton
  2002 + Cai 2009 + Mason & Macrae 2007 + Christoff 2009.
  Deferred from this registration session pending dedicated
  lit-pull commission.
- **Candidate ARC-XXX** — `imagination_learning_constraint_
  principle`. Per memory entry `project_imagination_learning_
  constraints.md`: explicit ARC-level commitment articulating
  LICIT (consistency, plan-optimisation, schema integration) vs
  FORBIDDEN (world-model updates, prediction validation, novel-
  fact generation) classes of learning from imagination.
  Currently implicit in MECH-094 / MECH-272 / MECH-273 substrate
  gating; needs explicit articulation as architectural commitment.
  Anchors: Stickgold 2013 + Cai 2009 + Schapiro 2017 CLS +
  confabulation literature + FEP epistemic value. Deferred
  pending dedicated lit-pull commission.

**Forward link.** V3-EXQ-543b and V3-EXQ-543c are the next-session
authoring targets via `/queue-experiment` skill. V3-EXQ-543b is
the noise-floor + gating arm class (Q-043 weight sweep + Q-045
4-arm ablation + multiplicative-gate vs additive-logit baseline);
V3-EXQ-543c is the curiosity + meta-RL recurrent baselines arm
class (MECH-314a/b/c absorption check + MECH-318 latent-stack
absorption check). Per Pull 4 R5 sequencing recommendation, the
two scripts split the original V3-EXQ-543b 5-arm protocol so
each script remains reviewable and falsifiable in isolation.

**Status table updates.** Five new gap rows registered (GAP-H
ARC-065 cluster + GAP-I ARC-064 cluster + GAP-J MECH-312-cluster +
GAP-K MECH-319 + status-value `registered` introduced for
claims-registered-but-experiments-not-yet-queued items).

**Cross-references.** ARC-063 V4 strong-reading evidence_quality_
note still references MECH-310/311/312/313 sub-claims-to-register
placeholder list; that placeholder list is now stale (MECH-312/313
are registered with different functional content per Pull 1-4
verdicts). Out of scope for this session per the prompt's "DO NOT
MODIFY MECH-094" rule (which extended in spirit to ARC-063 stale
cross-references); flag for separate cleanup session.

### 2026-05-10 - V3-EXQ-543b authored + queued (Phase 3-corrected falsifier)

V3-EXQ-543b authored same session as the reclassify decision. Script
`ree-v3/experiments/v3_exq_543b_arc062_phase3_optimized_falsifier.py`
implements the four corrections from the reclassify entry (CORRECTION A
gated_policy params in optimizer; CORRECTION B phased training P0=40 / P1=60 /
P2=8; CORRECTION C behavioral-divergence probe with mid-training inert-gating
short-circuit; CORRECTION D hardened C3 with transit-rate floor and nanmean).

P1 training-pressure honest scope. Per the design-trade discussion in this
session: rigorous REINFORCE on environmental reward would require accessing
E3 raw candidate scores at decision time and re-running gated_policy forward
with grad on cached features at episode end -- doable but adds significant
agent.py modification surface for one experiment. The 543b script instead
uses a SCAFFOLDING DIVERSIFICATION LOSS in P1 (negative head-pair output L2
+ negative discriminator output variance, sampled over a static probe buffer
collected during P0). This guarantees gated_policy parameters MOVE under any
non-trivial gradient pressure, satisfying the "in optimizer" requirement
from the reclassify spec. The behavioral-divergence probe (CORRECTION C) is
the architectural test: does the parameter movement translate to
context-conditional behavioral divergence on SD-054? If yes, the C2/C3/C4
acceptance grid applies. If no (probe TV-distance below 0.05 at mid-P1),
the seed/arm is marked non_contributory_inert_gating. Full REINFORCE-on-
environmental-reward is deferred to Phase 3 GAP-C/D when the discriminator
is wired into SD-033a LateralPFCAnalog.update() and the bias head joins the
composite E3 optimizer (commitment_closure GAP-1).

Smoke verification (`--dry-run`, p0_eps=3 / p1_eps=4 / p2_eps=2,
steps_per_episode=30, 3 seeds x 2 arms): script runs end-to-end in 175s,
manifest writes correctly, sentinel emitted, ARM_1c probe collects 32 states
with applicable=True. Probe mean_tv=0.0 in dry-run is expected (only 4 SGD
steps total; contract test C4 needed 200 SGD steps to see >5x head
divergence). Full run has P1=60 episodes x 4 SGD steps/ep = 240 steps,
above the 200 demonstrated to produce divergence.

Substrate readiness: ARC-062 GatedPolicy (landed 2026-05-09 GAP-A done) is
the only V3 substrate this experiment depends on. No additional substrate
work required. The MECH-313 / MECH-314 / MECH-318 / MECH-319 substrate gap
identified in the cluster-registration session is NOT in this experiment's
scope -- per the reclassify spec, V3-EXQ-543b is the corrected Phase 2
falsifier on the existing GatedPolicy substrate alone. The cluster-
registration session's expanded V3-EXQ-543b/c definitions (Q-043 noise-
floor sweep, Q-045 4-arm ablation, MECH-314a/b/c absorption check, MECH-318
absorption check) are deferred to follow-on experiments after the
underlying substrate lands via /lit-pull + /implement-substrate sessions
for MECH-313, MECH-314 (a/b/c), MECH-318, MECH-319.

Queue entry: Mac (DLAPTOP-4.local), priority=2, estimated_minutes=120,
episodes_per_run=108, seeds=3, conditions=2, supersedes=V3-EXQ-543. Smoke
PASS; validate_queue OK.

Status table updated: GAP-B `ran_inconclusive -> queued`; owner-EXQ
V3-EXQ-543b retained.

### 2026-05-10 - GAP-B reclassified non_contributory; jump to Phase 3 design (V3-EXQ-543b)

V3-EXQ-543 ran (3062s elapsed, manifest
`v3_exq_543_arc062_phase2a_monomodal_collapse_falsifier_20260509T214517Z_v3.json`).
Script declared `outcome=PASS, pass_rule_met=true (n_criteria_passed=2: C3+C4)`.
On review the PASS was reclassified `non_contributory` for all three tagged
claims (MECH-309, ARC-062, SD-029). Three independent issues, each sufficient
on its own to disqualify the result as a falsifier of MECH-309:

1. **C3 (risk-type dissociation) is a divide-by-near-zero artifact.** ARM_1c
   seed 0 had `transit_hazard_rate=0.0` (zero transit-regime hazards), so
   `risk_type_ratio = forage_rate / ~0 = 74883`. The arm-mean (24961) is
   dominated by that single seed. Per-seed ratios for ARM_1c are
   `[74883, 0.022, 0.024]` -- two of three seeds are *below* ARM_0's mean of
   0.082. C3 measured degenerate-trajectory geometry, not a behavioral
   dissociation between forage and transit risk weighting.
2. **ARM_1c seed 2 is byte-identical to ARM_0 seed 2.** Every reported metric
   matches exactly: mean_reef_fraction (0.26598), rho_drive_vs_reef (-0.0283),
   hazard rates, n_steps, per_episode_reef_fractions, warmup rewards. With
   gated_policy params intentionally NOT in the optimizer (Phase 2a tested
   structural-sufficiency-at-init) and `disc_init_scale=0.1` producing
   sigmoid-near-0.5 gating, the gating layer was inert for this seed -- the
   same RNG stream produced identical trajectories. The "random init breaks
   symmetry" assumption was too weak.
3. **C2 (state dependence) -- the criterion most directly tied to MECH-309's
   rule-apprehension prediction -- FAILED.** ARM_1c mean_abs_rho=0.111 vs
   ARM_0=0.291; the gated arm shows *less* state-dependent reef behavior, not
   more. ARM_1c per-seed reef-fractions `[0.0, 0.0006, 0.266]` indicate seeds
   0/1 abandoned reef-foraging entirely while seed 2 was the inert-gating
   clone of baseline.

**Design defect.** Phase 2a-at-init tested whether a randomly-initialised
gating layer could produce structural sufficiency without training. That is
not what MECH-309 predicts -- MECH-309 says trainers / agents *weight rules
they do not invent*, which means rule apprehension is a learning-time
acquisition under selection pressure, not an at-init property. With untrained
gating + sigmoid-near-0.5 init, the only two outcomes available were
(i) inert gating clones baseline (seed 2) or (ii) random-init noise disrupts
baseline without producing context-conditional behavior (seeds 0/1). Neither
falsifies MECH-309. Phase 2b density-gradient and Phase 2b R1 input-ablation
sub-arms inherit the same defect and are skipped.

**Skip-to-Phase-3 decision.** Successor V3-EXQ-543b becomes GAP-B owner and
moves directly to Phase 3 design: gated_policy params *in* the optimizer,
phased training schedule, with the additional instrumentation from session
feedback below. GAP-C and GAP-D scopes partially absorb into 543b
(specifically: gated_policy + bias-head added to E3 optimiser is a
prerequisite of any meaningful training-time test of MECH-309). Remaining
GAP-C work after 543b PASS is the explicit `LateralPFCAnalog.update()`
wiring of the discriminator output.

**Session feedback -- "rough-and-ready behavioral divergence check."** The
session insight: if rule apprehension is itself a *quick rough-and-ready
rule* (the MECH-309 framing), then we are missing a *quick rough-and-ready
means of ensuring the rule apprehended is behaviourally different.* The
EXQ-543 result demonstrates the gap: end-of-run reef-fraction / rho /
risk-ratio statistics are too far downstream to detect inert gating until
~50 minutes of compute have been spent. Worse, when they do detect it, the
signal is contaminated by random-init disruption.

V3-EXQ-543b will add a **behavioral-divergence probe**: every N training
episodes (default N=5), sample policy action distributions at a fixed set of
probe states under (a) `use_gated_policy=True` and (b) the baseline policy,
then report mean action-mismatch rate (or KL divergence). The probe states
should span the SD-054 reef context (high-density reef, transit corridor,
mixed) so that any context-conditional gating shows up as divergence on the
context-discriminative subset and convergence elsewhere. Pre-registered
inert-gating threshold: if mean mismatch rate stays below 0.05 by mid-
training, flag the run as inert-gating and short-circuit (mark
`non_contributory: inert_gating_detected_during_training`). This is the
"rough-and-ready" instrumentation -- it does not assert MECH-309 itself, but
it ensures the substrate is actually generating differentiable behavior
before the downstream falsifier metrics are even read.

Acceptance for V3-EXQ-543b: same C2/C3/C4 + F1/F2 grid as 543, *plus* the
divergence-probe gate. Run is `non_contributory` if probe gate fails
(inert gating, no behavioral signal to interpret). Run is a clean falsifier
attempt if probe gate passes (mean mismatch >= 0.05 by mid-training across
seeds), in which case C2/C3/C4/F1/F2 are interpreted on their original
acceptance grid. C3 dissociation calculation will be hardened against the
divide-by-near-zero artifact (require `transit_hazard_rate > 0.05` for the
per-seed ratio to enter the arm-mean; otherwise the seed contributes
`np.nan` and the arm-mean uses `np.nanmean`, with seed-count reported).

Status table updated: GAP-B `queued -> ran_inconclusive`, owner-EXQ shifted
to V3-EXQ-543b (to be queued same session). GAP-C/GAP-D last-updated
forwarded to 2026-05-10 with the partial-absorption note.

### 2026-05-09 - GAP-A done (Phase 1 substrate landed; V3-EXQ-542 5/5 PASS)

Phase 1 substrate landed. New module
[ree-v3/ree_core/policy/gated_policy.py](../../../ree-v3/ree_core/policy/gated_policy.py)
implements `GatedPolicy` (N=2 scoring heads sharing E3 candidate features +
3-stream context discriminator on `(z_world, z_self, z_harm_a)`) plus
`GatedPolicyConfig` and `GatedPolicyOutput`. Symmetry-broken init on the
heads' last-Linear bias (+/- `head_init_bias_offset` default 0.05) so the
two heads can differentiate from step 0 under any training pressure.
`disc_init_scale=0.1` keeps the discriminator output near 0.5 at init,
avoiding early head over-commitment.

REEConfig flag `use_gated_policy` (default False, bit-identical OFF) wired
through `REEConfig.from_dims` with per-knob defaults (`gated_policy_n_heads=2`,
`gated_policy_disc_hidden=24`, `gated_policy_disc_init_scale=0.1`,
`gated_policy_head_hidden=32`, `gated_policy_bias_scale=0.1`,
`gated_policy_head_init_bias_offset=0.05`).

REEAgent wiring composes `gated_policy_score_bias` additively into
`dacc_score_bias` immediately before the MECH-295 block, parallel to the
dACC / lateral_pfc / ofc composition pattern. **No connection to SD-033a
in Phase 1** -- that wiring is Phase 3 (closes commitment_closure GAP-1)
per the plan-of-record. Per-episode `reset()` clears diagnostic counters
on the GatedPolicy module (no persistent state to clear; module is
stateless across ticks).

5 contract tests in
[ree-v3/tests/contracts/test_gated_policy.py](../../../ree-v3/tests/contracts/test_gated_policy.py)
landed: C1 default-off no-op + C2 backward-compat + C3 discriminator output
in [0, 1] across diverse latents + C4 head differentiation under training
pressure (output-divergence metric, >5x growth on held-out batch after 200
SGD steps) + C5 MECH-094 simulation_mode gate. All 5 PASS; full ree-v3
preflight + contracts 249/249 PASS (244 prior + 5 new). Bit-identical OFF
guarantee verified.

V3-EXQ-542 substrate-readiness diagnostic 5/5 PASS (Mac runner,
2026-05-09T20:22:11Z, `v3_exq_542_arc062_gated_policy_substrate_readiness_v3_20260509T202211Z.json`).
Five sub-tests UC1-UC5 cover forward-pass instantiation, master-OFF
no-op, discriminator input sensitivity, head differentiation under
training pressure, and MECH-094 simulation gate. UC2 z_world pixel-match
across flag-off vs flag-on dropped from acceptance criteria because the
GatedPolicy `nn.Linear` inits consume the global RNG between paths so
the rest of the agent's randomly-initialised weights diverge by
construction; substrate-level backward-compat (flag OFF -> module is
None; flag ON -> module instantiates without raising; both sense() clean)
is the right contract at the substrate layer, and the pixel-level no-op
is exercised by contract test C1 against a single agent that never
instantiates GatedPolicy. UC3 threshold for discriminator output range
set to 0.001 (above floating-point noise floor; substantial discriminator
variation is a Phase-2 training signal, not a Phase-1 init signal --
disc_init_scale=0.1 deliberately keeps the sigmoid output flat near 0.5
at init).

GAP-A status `open` -> `done` in YAML frontmatter and body status table;
`last_updated` 2026-05-09; owner_exq populated as V3-EXQ-542. Phase 2
(GAP-B monomodal-collapse falsifier on SD-054) remains `open` and is the
next-thing-to-queue (separate session per the plan-of-record's six-phase
sequencing -- do not bundle Phase 2 EXQ in this same session).

Cross-plan link: commitment_closure_plan.md GAP-1 remains `blocked` on
both arc_062 GAP-A (now done) and arc_062 GAP-B (still open). GAP-1
unblock cascade requires Phase 2 PASS (then Phase 3 wires discriminator
into SD-033a `LateralPFCAnalog.update()` source vector + adds bias-head
parameters to E3 optimiser).

### 2026-05-09 - Plan registered

Plan-of-record `arc_062_rule_apprehension_plan.md` registered as a sibling
to `commitment_closure_plan.md` / `sleep_substrate_plan.md` /
`sd033_governance_plan.md` / `goal_pipeline_plan.md` /
`self_attribution_plan.md`. Seven gaps surfaced and sequenced into six
phases. R1 / R2 / R3 / R4 open questions resolved with biology-anchored
defaults from two preceding lit-pulls (Pull A targeted_review_arc_062_
rule_apprehension/ 8 entries 2026-05-09T19:19Z; Pull B
targeted_review_arc_062_refuge_forage_ecology/ 6 entries 2026-05-09T19:34Z).

Cross-plan link to `commitment_closure_plan.md` GAP-1 established: the
SD-033a bias-head training problem (load-bearing in commitment_closure)
is now reframed as downstream of this plan's Phase 3 (GAP-C + GAP-D).
The original commitment_closure GAP-1 Phase 1 deliverables are rewritten
to drop the oracle-supervised "rule-cue gridworld" curriculum (which
MECH-309 says cannot exist honestly in REE) in favour of joint training
through ARC-062's discriminator-driven gradient path.

substrate_queue.json edits: ARC-062 entry added with priority 2,
ready=true, status=candidate_v3_pending, design_doc pointing at this
plan, implementation_hint summarising Phase 1 deliverables. MECH-309 and
ARC-063 are diagnostic / V4-deferred and do not need substrate_queue
entries.

The closure-tab visualisation will pick up this plan automatically as a
new column on the next /api/closure poll.

### 2026-05-08 - Cluster registered (pre-plan)

MECH-309 / ARC-062 / ARC-063 cluster registered in claims.yaml from the
SD-054 substrate-purpose-validation discussion. SD-054 substrate carried
behavioural diversity under heuristic policy (V3-EXQ-522 substrate-
ceiling PASS) but every SD-029 retest under trained policy
(V3-EXQ-433e/433f/523/523a/523b) returned non_contributory for the same
reason: insufficient agent-caused trials, monomodal V_s monostrategy
substrate-ceiling pattern. Diagnosis: substrate is not the bottleneck;
the trained policy lacks a rule-apprehension layer. MECH-309 reframes
monomodal collapse from a training failure into the predicted equilibrium
output of an architecture whose only learners are updaters.

---

## Cross-plan link with commitment_closure_plan.md

This plan and `commitment_closure_plan.md` share two load-bearing claims:

1. **SD-033a bias head training (commitment_closure GAP-1).** The
   commitment_closure plan's Phase 1 originally proposed a phased pre-
   training-on-rule-cue-curriculum approach. That approach presupposed
   an oracle `rule_cue_id` label that the architecture (per MECH-309)
   says cannot exist honestly in REE. With ARC-062 in place, the bias
   head trains jointly with E3 via the existing score-aggregation
   gradient path, with the rule signal arriving from ARC-062's
   discriminator rather than from an oracle. The commitment_closure
   GAP-1 row is reframed as `blocked` on this plan's GAP-A and GAP-B.

2. **MECH-094 / MECH-261 mode-conditioning generalisation.** The MECH-261
   write-gate registry on SD-032a SalienceCoordinator generalises the
   MECH-094 hypothesis-tag write gate to the apprehension layer. ARC-062
   discriminator output flows through this same registry (when wired to
   SD-033a's `update()` per Phase 3, the gate-modulated EMA on
   `rule_state` consumes `write_gate("sd_033a")` which is itself mode-
   conditioned). Internal-replay mode (`write_gate("sd_033a") = 0.05`)
   blocks the apprehension layer from updating on replay content -- the
   same MECH-094 invariant the closure operator relies on.

Sessions that touch *both* plans (e.g. discriminator-output-routing
to the closure operator's mode-conditioning gate) should update the
[Status table](#status-table) on both this plan and the commitment_
closure plan.

---

## Resume ritual

When picking up rule-apprehension cluster work after a deviation:

1. Read this plan document first.
2. Read the [Status table](#status-table) and identify the row that was
   `paused` or `in-progress`.
3. If `paused`, find its entry in the [Decision log](#decision-log) and
   confirm the resume condition has fired.
4. If `in-progress`, find the most recent decision-log entry for that
   phase and continue from the last concrete action.
5. Update the row's `Last updated` field and `Status` if it changes.
6. Append a new decision-log entry for any architectural choice made
   during the resumed session.
7. If the work touches the [commitment_closure_plan.md](./commitment_closure_plan.md)
   cross-link concerns (SD-033a bias head training, MECH-261 mode-
   conditioning), update both plans' status tables.

Sessions that do NOT touch rule-apprehension cluster work do not need to
read this document. Sessions that DO touch this work read this document
before any code or experiment edit.

---

## See also

- [evidence/planning/commitment_closure_plan.md](./commitment_closure_plan.md) — sibling plan; GAP-1 SD-033a bias head training is downstream of this plan's Phase 3
- [evidence/planning/sleep_substrate_plan.md](./sleep_substrate_plan.md) — sibling plan; GAP-G cross-link for sleep-vs-waking refinement (V4 deferred)
- [evidence/planning/sd033_governance_plan.md](./sd033_governance_plan.md) — OCD-specific test-battery sub-plan (sibling to commitment_closure)
- [evidence/planning/self_attribution_plan.md](./self_attribution_plan.md) — sibling plan
- [evidence/planning/goal_pipeline_plan.md](./goal_pipeline_plan.md) — sibling plan
- [evidence/planning/substrate_queue.json](./substrate_queue.json) — ARC-062 entry added by this plan registration
- [evidence/literature/targeted_review_arc_062_rule_apprehension/SYNTHESIS.md](../literature/targeted_review_arc_062_rule_apprehension/SYNTHESIS.md) — Pull A 8 entries (R1 / R2 / R3 verdicts)
- [evidence/literature/targeted_review_arc_062_refuge_forage_ecology/SYNTHESIS.md](../literature/targeted_review_arc_062_refuge_forage_ecology/SYNTHESIS.md) — Pull B 6 entries (R4 verdict)
- [docs/architecture/rule_apprehension_layer.md](../../docs/architecture/rule_apprehension_layer.md) — 2026-05-04 thought-intake
- [docs/architecture/sd_054_reef_enrichment_substrate.md](../../docs/architecture/sd_054_reef_enrichment_substrate.md) — SD-054 reef substrate spec
- [docs/architecture/sd_033a_lateral_pfc_analog.md](../../docs/architecture/sd_033a_lateral_pfc_analog.md) — SD-033a substrate spec (Phase 3 wiring target)
