---
closure_plan:
  id: arc_062_rule_apprehension
  title: "Rule Apprehension (ARC-062 / MECH-309 / ARC-063)"
  registered: 2026-05-09
  scope_claims: [MECH-309, ARC-062, ARC-063, SD-054, SD-029, MECH-269]
  sibling_plans: [commitment_closure, sleep_substrate, sd033_governance, goal_pipeline, self_attribution]
  nodes:
    - id: "arc_062_rule_apprehension:GAP-A"
      title: "ARC-062 substrate not implemented (gated-policy heads + learned context discriminator)"
      phase: 1
      status: open
      severity: load-bearing
      owner_exq: TBD
      unblocks_claims: [ARC-062, MECH-309]
      depends_on: []
      cross_plan_link: ["commitment_closure:GAP-1"]
      last_updated: 2026-05-09
    - id: "arc_062_rule_apprehension:GAP-B"
      title: "MECH-309 monomodal-collapse falsifier unrun (ARM_0 single-head vs ARM_1 gated-heads on SD-054)"
      phase: 2
      status: open
      severity: load-bearing
      owner_exq: TBD
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
| GAP-A | 1 | open | nothing | Implement gated_policy.py module + flag + contracts; queue Phase 1 substrate-readiness EXQ | TBD | 2026-05-09 |
| GAP-B | 2 | open | GAP-A | Pre-register Phase 2 acceptance criteria (already drafted above); queue 2-arm + density gradient EXQs | TBD | 2026-05-09 |
| GAP-C | 3 | open | GAP-B PASS | Wire discriminator output into LateralPFCAnalog.update() source vector | TBD | 2026-05-09 |
| GAP-D | 3 | open | GAP-C | Add bias head params to E3 optimiser; default-flag flip; queue GAP-1 validation EXQ | TBD | 2026-05-09 |
| GAP-E | 4 | deferred | GAP-D PASS | Extend SD-054 to ≥3 strategies; 3-arm scaling experiment | n/a in V3 | 2026-05-09 |
| GAP-F | 5 | deferred V4 | GAP-E outcome | none in V3 | n/a | 2026-05-09 |
| GAP-G | 5 | deferred V4 | sleep_substrate plan progression | Pull C lit-pull (sleep-vs-waking refinement biology) when ARC-063 V4 work opens | n/a | 2026-05-09 |

Status values: `open`, `in-progress`, `blocked`, `paused`, `partial`,
`done`, `deferred`. A `paused` row carries a resume condition in the
[Decision log](#decision-log).

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
