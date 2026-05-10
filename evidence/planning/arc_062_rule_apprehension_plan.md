---
closure_plan:
  id: arc_062_rule_apprehension
  title: "Rule Apprehension (ARC-062 / MECH-309 / ARC-063 / ARC-064 / ARC-065 / MECH-312-cluster / MECH-319)"
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
      title: "MECH-309 monomodal-collapse falsifier unrun (ARM_0 single-head vs ARM_1 gated-heads on SD-054)"
      phase: 2
      status: queued
      severity: load-bearing
      owner_exq: V3-EXQ-543
      unblocks_claims: [MECH-309, ARC-062, SD-029]
      depends_on: ["arc_062_rule_apprehension:GAP-A"]
      cross_plan_link: ["commitment_closure:GAP-1"]
      last_updated: 2026-05-09
    - id: "arc_062_rule_apprehension:GAP-C"
      title: "ARC-062 discriminator output not routed to SD-033a LateralPFCAnalog.update() source vector"
      phase: 3
      status: open
      severity: high
      owner_exq: TBD
      unblocks_claims: [SD-033a, MECH-262, SD-034]
      depends_on: ["arc_062_rule_apprehension:GAP-B"]
      cross_plan_link: ["commitment_closure:GAP-1"]
      last_updated: 2026-05-09
    - id: "arc_062_rule_apprehension:GAP-D"
      title: "E3 optimiser does not include lateral_pfc_analog.rule_bias_head.parameters() (SD-033a bias head untrained)"
      phase: 3
      status: open
      severity: high
      owner_exq: TBD
      unblocks_claims: [SD-033a, MECH-262]
      depends_on: ["arc_062_rule_apprehension:GAP-C"]
      cross_plan_link: ["commitment_closure:GAP-1"]
      last_updated: 2026-05-09
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
| GAP-B | 2 | queued | V3-EXQ-543b run | V3-EXQ-543 ran (script declared PASS; reclassified non_contributory 2026-05-10 -- see decision-log "GAP-B reclassified non_contributory; jump to Phase 3 design"). Successor V3-EXQ-543b authored 2026-05-10 same day, smoke-PASS, queued (Mac, 120 min). Four corrections: (A) gated_policy.parameters() in dedicated Adam during P1 (LR_GATED_POLICY=5e-4); (B) phased training P0=40 encoder warmup -> P1=60 frozen-encoder + scaffolding diversification loss (head-pair output L2 + discriminator output variance) -> P2=8 eval; (C) behavioral-divergence probe at PROBE_INTERVAL_P1_EPS=5, mid-P1 inert-gating short-circuit at MID_TRAINING_EP=30 with INERT_GATING_THRESHOLD=0.05 TV-distance; (D) hardened C3 with C3_TRANSIT_RATE_FLOOR=0.05 + np.nanmean + min 2 valid seeds per arm. P1 training is scaffolding pressure (NOT REINFORCE on env reward); full REINFORCE deferred to Phase 3 GAP-C/D. Awaiting runner pickup. | V3-EXQ-543b | 2026-05-10 |
| GAP-C | 3 | open | GAP-B (via V3-EXQ-543b) PASS | Wire discriminator output into LateralPFCAnalog.update() source vector. NOTE 2026-05-10: GAP-C scope partially absorbed into V3-EXQ-543b (gated_policy params in optimizer is a Phase-3 deliverable). Remaining GAP-C work: explicit LateralPFCAnalog wiring after 543b PASS confirms training-time gating produces behavioral divergence. | TBD | 2026-05-10 |
| GAP-D | 3 | open | GAP-C | Add bias head params to E3 optimiser; default-flag flip; queue GAP-1 validation EXQ. NOTE 2026-05-10: bias-head-in-optimizer also partially absorbed into 543b. | TBD | 2026-05-10 |
| GAP-E | 4 | deferred | GAP-D PASS | Extend SD-054 to ≥3 strategies; 3-arm scaling experiment | n/a in V3 | 2026-05-09 |
| GAP-F | 5 | deferred V4 | GAP-E outcome | none in V3 | n/a | 2026-05-09 |
| GAP-G | 5 | deferred V4 | sleep_substrate plan progression | Pull C lit-pull (sleep-vs-waking refinement biology) when ARC-063 V4 work opens | n/a | 2026-05-09 |
| GAP-H | 2-3 | registered | claims-only registration | ARC-065 diversity-generation cluster registered (ARC-065 anchor + MECH-313 noise-floor + MECH-314 structured-curiosity + MECH-314a/b/c sub-flavours + Q-043 weight calibration + Q-044 sub-flavour independence + Q-045 313-vs-260 collapse). V3 falsification path = V3-EXQ-543b/c (script-write deferred to next session). | V3-EXQ-543b/c | 2026-05-10 |
| GAP-I | 2-3 | registered | claims-only registration | ARC-064 bottom-up rule-discovery cluster registered (ARC-064 anchor + MECH-316 cross-episode regularities + MECH-317 behavioural pattern compression + MECH-318 rule-state abstraction provisional). MECH-315 absorbed into MECH-292/293 ghost-goal substrate per Pull 2 R5. V3 falsification path: substrate-design EXQ deferred (requires multi-rule-context substrate beyond SD-054 alone). | TBD | 2026-05-10 |
| GAP-J | 2-3 | registered | claims-only registration | MECH-312 parent + MECH-312a/b/c/d sub-MECHs registered (uncertainty / practice-maturity / affective-stream-modulation / V_s-freshness-modulation). MECH-312e controllability/agency deferred per Pull 3 R5 (substrate not available). Multiplicative-gate combination rule registered as architectural default; additive-logit baseline is the V3-EXQ-543b/c falsifying alternative. | V3-EXQ-543b/c | 2026-05-10 |
| GAP-K | 2-3 | registered | claims-only registration | MECH-319 simulation-mode rule-write-gating substrate registered as REE-novel substrate-level instantiation of MECH-094 at the arbitration layer. SWR machinery + reverse-replay are the substrate anchors; the categorical write-gate function is REE-novel. V3 falsification path: artificial-write-channel-routing config flag in V3-EXQ-543c. | V3-EXQ-543c | 2026-05-10 |

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
