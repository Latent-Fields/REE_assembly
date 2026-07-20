---
title: "SD-049: Multi-Resource Heterogeneity"
parent: "Development & Curriculum"
grandparent: Architecture
nav_order: 12
status: candidate/v3_pending
status_asof: 2026-07-10
status_claim: SD-049
---

# SD-049: Multi-Resource Heterogeneity

**Claim ID:** SD-049
**Subject:** `environment.multi_resource_heterogeneity`
**Status:** IMPLEMENTED (Phase 2 hybrid encoder, encoder + Phase 1 env substrate) -- 2026-05-04
**Registered:** 2026-05-03
**Implemented (Phase 1, env-only):** 2026-05-03
**Implemented (Phase 2 hybrid encoder):** 2026-05-04 (encoder side; Option C per verdict.md, lit-anchored at confidence 0.78)
**Validation experiment:** V3-EXQ-514 queued 2026-05-04 (estimated_minutes=90). PASS clears Phase 2 + lifts SD-015 promotable; FAIL routes to verdict.md 6-row interpretation grid including the Woo/Spelke substrate-ceiling falsifier branch.
**Phase 3 (SD-032 consumer cascade reading per_axis_drive directly):** REGISTERED in substrate_queue.json SD-049-PHASE-3 entry; action-triggered by V3-EXQ-514 failure on SD-032-mediated pathway only (not predicted by encoder-driven failure modes per verdict.md).
**Origin:** Substrate-roadmap H-priority #2 (`docs/architecture/substrate_roadmap.md`).
Trigger: the wanting/liking + identity-distinct-goal cohort (MECH-229, MECH-230,
MECH-117, MECH-216, ARC-030, ARC-032, Q-030, SD-015) operates on a substrate
where every resource is interchangeable. The `goal_resource_r` correlation has
sat at 0.066 across the EXQ-085x iteration cluster despite contact-gated z_goal
seeding -- a signature of "there is nothing for the resource encoder to encode."
Fuller-scope per user direction 2026-05-03: include a non-homeostatic
novelty/information channel and a per-axis drive system, with a curriculum-
introduction hook so downstream developmental-schedule work has the substrate
it needs.
**Depends on:** SD-012 (homeostatic drive -- per-axis extension required),
SD-015 (z_resource encoder -- the upstream substrate this enables),
SD-005 (self/world latent split -- z_world routing must hold under multiple
resource identities)

---

## Problem

CausalGridWorldV3's resource model treats all resources as interchangeable
units of a single appetitive class. Every resource cell carries the same
benefit; consumption updates a single scalar drive (SD-012, `drive_weight=2.0`);
the z_resource encoder (SD-015) sees no identity-bearing signal to encode.

This is too thin a substrate for the cohort of claims about
**identity-distinct goals**:

- **MECH-229** (active, `drive.wanting_liking_behavioral_dissociation`)
  is the wanting-vs-liking dissociation. The dissociation is meaningful
  only when the agent can want one thing while consuming a different
  thing. With a single resource type, "wanting" and "liking" are two
  views of the same scalar drive against a single satiating object;
  PASS evidence (EXQ-074f) was obtained on z_world fallback seeding,
  not via genuine identity-distinct wanting.
- **MECH-230** (provisional, `drive.goal_state_latent_structure`) is the
  z_goal latent-structure claim. The structure is *trivial* if there
  is only one possible goal identity; the EQN already documents
  z_goal_norm=0.0 in dry-run conditions because there is no resource
  contact to seed any structure.
- **MECH-117** (stable, `wanting.liking_trajectory_dissociation`)
  evidence cohort needs identity-distinct redirect targets to
  separate the "approach what you want" trajectory class from the
  "approach what is satiating right now" class. Currently the
  C2 PASS in EXQ-074d came from a single redirect to a moved single-type
  resource -- a degenerate special case of the claim.
- **MECH-216** (provisional, `goal.e1_schema_wanting`) requires schema
  salience seeding on identity-distinct cues. EXQ-263b confirmed
  schema salience seeding works mechanically; what it cannot test is
  whether the schema *generalises across distinct goal identities*.
- **ARC-030** (candidate, `architecture.approach_avoidance_symmetry`)
  needs go/nogo channels operating across multiple goal identities to
  test the symmetry claim non-trivially.
- **ARC-032** (candidate, `architecture.theta_frontal_hippocampal_goal`)
  needs goal-identity-distinct theta routing for the frontal-hippocampal
  goal-maintenance signature to be discriminable from generic activity.
- **Q-030** (open, `goal_representation.resource_world_permutations`)
  is the explicit 6-cell `z_resource × z_world` routing sweep open
  question. The question is well-posed only when `z_resource` carries
  identity, not just presence.
- **SD-015** (candidate, `goal_representation.z_resource_encoder`) sits
  blocked at `goal_resource_r=0.066` because the resource encoder has
  nothing to encode beyond presence/absence. SD-049 is the upstream
  substrate fix that gives SD-015 a learnable signal.

The unifying diagnosis: **the cohort sits at substrate-thinness, not
claim error.** A single-resource substrate is to identity-distinct-goal
claims what a single-causal-source substrate (SD-047 problem) was to
agency-detection-comparator claims. Both are V3-tractable in principle;
both need the substrate to carry the dimensions the claim wants to
test.

**Architectural reading:** these are substrate-ceiling-adjacent failures.
The cohort is not formally tagged `epistemic_category: substrate_ceiling`
because the failures are mostly null/inconclusive rather than the
clean C4-only-PASS signature that prompted SD-047. But the substrate
prescription is the same: enrich the env so the claims can be honestly
tested.

---

## Mechanism

SD-049 makes three additions to CausalGridWorldV3, layered on top of
SD-012's homeostatic drive system:

### Addition 1: Multiple resource identities

The env carries `n_resource_types: int` (default 3) qualitatively distinct
resource types, each with:

- **A unique identity tag** in observations (one-hot or low-D embedding
  passed through obs_dict to the encoder).
- **A type-specific spawn distribution** (each type spawns in its own
  cell-set or with its own spatial bias, so identity is co-located with
  spatial signature).
- **A type-specific benefit profile** (which drive axis it satiates,
  by how much, with what satiation curve).

Suggested default identities for the V3 substrate, biased toward
maximum dissociability:

| identity | drive axis | satiation curve | comment |
|---|---|---|---|
| `food` | hunger | sigmoidal saturating | classic homeostatic appetitive |
| `water` | thirst | sharper saturation, faster onset | distinct homeostatic axis -- supports approach-avoidance symmetry tests across drives |
| `novelty` / `information` | curiosity | non-homeostatic; benefit decays with familiarity, not satiation | this is the load-bearing one for wanting/liking dissociation -- it generates "wanting" without monotonic satiation |

The novelty/information channel is non-negotiable for fuller scope.
Without it, all three resource types are isomorphic-modulo-drive-axis
and the wanting/liking dissociation collapses to "which drive is
currently most depleted." The novelty channel breaks that symmetry by
producing prospective wanting that does not reduce a homeostatic
deficit -- exactly the structural distinction MECH-229 wants to test.

### Addition 2: Per-axis homeostatic drive system

SD-012's single `drive_weight=2.0` scalar must become a per-axis vector.
Each drive axis has independent depletion dynamics, an independent
drive-weight, and contributes additively (or per a configurable
combiner) to the goal-conditioning signal that flows through to z_goal
and downstream policy.

This is a non-trivial substrate edit: SD-012's homeostatic drive system
is the upstream substrate for MECH-229, MECH-230, SD-015, and the
EXQ-085x iteration cluster. The per-axis change cascades into:

- **Encoder side:** drive state must be a vector; the goal-conditioning
  pathway must select-or-combine across axes.
- **E3 evaluation side:** value reads must be per-axis or a learned
  combination.
- **All experiments tagging SD-012:** any experiment that reads or
  modulates `drive_weight` will need to be re-confirmed under the per-
  axis substrate. This triggers `pending_substrate_reconfirmation` on
  SD-012-emergent invariants per the invariant-types governance rule.

### Addition 3: Curriculum-introduction hook

A `resource_introduction_schedule: dict[str, int]` env knob controls
when each resource type becomes available during a multi-episode run.
Schedule defaults to "all types available from step 0 of episode 0" so
existing experiments are unchanged; populated, it produces curricula
like:

```python
{"food": 0, "water": 5000, "novelty": 10000}
```

reading as: food available from step 0; water introduced at step 5000;
novelty at step 10000. Resource types that have not yet been introduced
do not spawn and do not appear in obs_dict.

This hook is the substrate scaffold for downstream developmental-
schedule work. It is added now because (a) the substrate code path is
being touched anyway, (b) introducing the hook later would require a
second cascade through the same files, (c) defaults are inert so it
costs nothing to leave it unused. The hook itself is not the
developmental schedule -- that is downstream design work that uses the
hook -- but it is the substrate prerequisite without which the
schedule cannot be expressed.

### Why fuller scope?

A minimal 2-type substrate (food + water, both homeostatic) would let
MECH-229 PASS by exploiting drive-axis dissociation alone -- which is
not the claim under test. The wanting/liking dissociation is supposed
to be observable on a single drive axis when the wanting-target
differs from the satiating-target. The non-homeostatic novelty channel
is what produces that case: agent can "want" novelty (predictive
salience, schema seeding) while "liking" food consumption (reward
signal). The dissociation is then between *what is being approached*
and *what is reducing a deficit*, which is the structural shape the
claim asserts. A 2-type homeostatic-only substrate cannot generate
this case.

---

## Calibration target

When fully enabled (3 types, per-axis drive, curriculum off), an episode
of random-policy agent should produce all three resource types being
encountered with roughly comparable rates. Rough target:

- Each homeostatic resource type contacted >= 2 times per 200-step
  episode (so satiation dynamics have room to operate).
- Novelty cells contacted >= 5 times per 200-step episode (novelty
  decays per-cell, so re-contacts are needed to observe the decay
  curve).

Below those rates the substrate is effectively single-type (one
identity dominates the experience). Above the upper bound (every cell
spawns every type every tick), the spatial structure that supports
identity-discrimination collapses.

---

## Child mechanisms (deferred)

If SD-049 is implemented and validated, child claims register the
distinct identity-discrimination capacities. Following the
biology-before-formal-definitions rule, these are deferred to the
implementation phase rather than registered now:

- **MECH-(TBD): non-homeostatic novelty signal class** -- novelty as a
  benefit signal whose consumption-trace decays with familiarity rather
  than satiation. Used by MECH-216 schema-wanting and MECH-229
  wanting-side.
- **MECH-(TBD): per-axis drive arbitration** -- the structural rule
  governing how multi-axis drive deficits combine into a single
  trajectory selection. Used by ARC-030 approach-avoidance symmetry.
- **MECH-(TBD): identity-tagged z_resource encoding** -- the operation
  by which z_resource carries identity beyond presence. Used by SD-015,
  Q-030.

Registering these without an implementation invites the SD-003
overreach pattern (28 FAILs before substrate caught up). Hold for
post-validation walk.

---

## Architecture context

SD-049 sits at the **environmental substrate** layer, parallel to
SD-022 (body-damage substrate), SD-029 (scheduled external hazard),
SD-035 (amygdala analog), SD-047 (multi-source dynamics). It modifies
the env's observation generation and the homeostatic drive accounting;
it does not modify the agent's encoder, predictor, or selector
architectures (those consume the new dimensions but do not change
shape).

**Relation to SD-047** (multi_source_dynamics, in implementation now):
independent and complementary. SD-047 enriches the env's
**agent-independent causal background** for agency-detection
comparators. SD-049 enriches the env's **agent-relevant goal vocabulary**
for wanting/liking and identity-distinct-goal claims. The two SDs touch
overlapping files (`causal_grid_world.py`) but operate on disjoint
mechanisms. Expected merge order: SD-047 lands first (already in
implementation); SD-049 layers on top.

**Relation to SD-022 / SD-029**: layered on top, not replacing. SD-022
gives the body-damage substrate its harm-stream identity; SD-029 gives
external hazards their scheduled-source identity. SD-049 is the
appetitive-side analog: it gives resources their identity.

**Distinct from V4 multi-agent ecology**: V4-1 (multi-agent ecology)
introduces other agents whose goal-pursuit is genuinely intentional.
SD-049's novelty channel is the closest V3-tractable analog of "another
goal-bearer" but it is structurally inanimate -- it does not *pursue*
anything. The wanting/liking cohort can be tested without inter-agent
goal interaction; that is the V3-tractable scope claim being made here.

**Distinct from differentiated coping channels** (substrate-roadmap
M-priority #5, not yet registered): that SD addresses MECH-102's
substrate-ceiling by giving the agent multiple **action** modalities.
SD-049 gives the env multiple **resource** modalities. Independently
implementable.

---

## What this SD enables

**Primary unblocks (cohort blocked at substrate thinness):**

- **SD-015** (`goal_representation.z_resource_encoder`, candidate) --
  the z_resource encoder has nothing to encode under single-type
  substrate. SD-049 provides the identity dimension. Pre-registered
  prediction: `goal_resource_r` should rise from 0.066 (single-type
  baseline) to >= 0.5 with three identity-distinct types after the
  encoder retrains on the enriched substrate.
- **MECH-229** (`drive.wanting_liking_behavioral_dissociation`, active)
  -- enables the discriminative experiment: agent wants novelty cell
  while liking food cell. PASS expected as `wanting_target != liking_target`
  at the trajectory level on >= 60% of seeded episodes.
- **MECH-230** (`drive.goal_state_latent_structure`, provisional) --
  z_goal latent should show non-trivial multi-modal structure under
  multiple resource identities. PASS expected as ANOVA on z_goal
  cluster IDs grouped by current-target-identity p < 0.01 across seeds.
- **Q-030** (`goal_representation.resource_world_permutations`, open) --
  the 6-cell `z_resource × z_world` routing sweep becomes well-posed.
  Routing-asymmetry signature predicted as r_z_resource_to_z_world > 0.3
  under identity-distinct types vs ~ 0 under single-type baseline.

**Secondary unblocks (downstream structural claims):**

- **MECH-117** (`wanting.liking_trajectory_dissociation`, stable) -- the
  cohort it sits in benefits from genuine identity-distinct redirect
  targets; supports its current stable rating with non-degenerate
  evidence.
- **MECH-216** (`goal.e1_schema_wanting`, provisional) -- schema
  generalisation across identity-distinct cues becomes testable.
- **ARC-030** (`architecture.approach_avoidance_symmetry`, candidate) --
  go/nogo symmetry tests across identity-distinct goal types.
- **ARC-032** (`architecture.theta_frontal_hippocampal_goal`, candidate)
  -- goal-identity-distinct theta routing becomes discriminable.

**Substrate scaffolding for downstream developmental-schedule work:**

- The `resource_introduction_schedule` hook is the prerequisite for
  any curriculum design that introduces resource types in stages.
  Without the hook, the substrate cannot express a developmental
  trajectory; with the hook (defaults inert), curriculum design becomes
  a separate downstream design exercise that does not require another
  substrate edit.

**Indirectly relevant:**

- **SD-012** (`environment.homeostatic_drive`, provisional) requires
  per-axis extension under SD-049. This is a substrate-changing edit
  to a provisional claim; per the invariant-types governance rule,
  SD-012-emergent invariants will receive `pending_substrate_reconfirmation`
  flags after the per-axis change lands. This is expected and tracked
  in the implementation plan.

---

## Validation experiment (deferred -- pre-registered protocol)

**Pre-registered protocol for SD-049 validation -- substrate gradient sweep:**

The validation must distinguish four states: substrate too thin (current
baseline), substrate enriched but agent did not learn the identity
distinction, substrate enriched and identity learned, substrate
overshoot (so many types the encoder cannot resolve any of them).

ARM definitions:

- **ARM_0 (OFF baseline):** `multi_resource_heterogeneity_enabled=False`.
  Single-type substrate (current behaviour). Expected to replicate
  baseline `goal_resource_r = 0.066`-tier signal.
- **ARM_1 (2-type homeostatic):** food + water, no novelty channel.
  Drive-axis dissociation only; tests whether dissociation can be
  achieved trivially via drive-axis routing.
- **ARM_2 (3-type, default):** food + water + novelty. The fuller-scope
  configuration. The discriminative pre-registered prediction lives
  here.
- **ARM_3 (5-type):** food, water, novelty, plus two additional
  identities (e.g. shelter, social-proxy). Tests substrate overshoot
  -- if encoder can resolve 3 but not 5, the substrate calibration
  has an upper bound that should be documented.

**Pre-registered predictions:**

- `goal_resource_r` rises monotonically from ARM_0 -> ARM_2, with
  ARM_2 - ARM_0 >= 0.4 (target: 0.066 -> >= 0.5).
- `wanting_target != liking_target` trajectory fraction is near-zero
  in ARM_0 and ARM_1 (because either wanting and liking are the same
  thing, or they trivially follow drive deficit), and >= 0.6 in ARM_2.
- Per-axis drive-deficit ANOVA on z_goal cluster ID is non-significant
  (p > 0.1) in ARM_0/ARM_1 and significant (p < 0.01) in ARM_2.
- Encoder identity-recovery accuracy (held-out: predict resource
  identity from z_resource alone) is at-chance in ARM_0, > 0.6 in
  ARM_2, falls back toward chance in ARM_3.

**Interpretation grid:**

| ARM_2 outcome | ARM_0 outcome | Reading |
|---|---|---|
| All four predictions confirmed | Baseline replicates | **SD-049 validated.** Cohort unblocked. SD-015 promotable; MECH-229 / MECH-230 / Q-030 evidence accumulates honestly. |
| `goal_resource_r` rises but `wanting != liking` does not | Baseline replicates | **Substrate works, claim under test does not.** SD-015 promotable; MECH-229 dissociation diagnosis re-opens (the substrate gives it the chance and it didn't take it). |
| `goal_resource_r` does not rise even in ARM_2 | Baseline replicates | **Encoder bottleneck downstream of substrate.** Investigate SD-015 implementation -- substrate provides the signal but encoder cannot capture it. Routes work to encoder fix, not further substrate enrichment. |
| ARM_3 outperforms ARM_2 | Either | **Calibration miscalibrated upward.** Increase default `n_resource_types` to whatever ARM_3 used; document the upper bound elsewhere. |
| ARM_3 << ARM_2 | Either | **Encoder capacity bound around 3 types.** Note as architectural finding; default stays at 3. |
| All arms FAIL `wanting != liking` | Baseline replicates | **Wanting/liking dissociation is not behaviourally observable in this substrate family at all.** Route MECH-229 from V3-tractable to substrate_conditional with V4 dependency on V4-1 multi-agent ecology (where genuine "wanting another agent" emerges). This is the falsifier branch parallel to SD-047's Woo/Spelke branch. |

This is a falsifiable substrate test: each row maps a distinct
experimental signature to a distinct architectural conclusion, including
a clean route from falsification to V4-bound re-classification.

**Lit-pull provenance:** the literature anchoring the wanting/liking
dissociation discriminative-feature choice (Berridge & Robinson on
incentive salience vs hedonic impact, plus identity-distinct goal
selection literature) is in `evidence/literature/targeted_review_sd_049/`
(written same session as design doc).

---

## Implementation surface

**ree-v3 / `ree_core/environment/causal_grid_world.py`** (must wait for
SD-047 implementation to land, since both touch the same file):

```python
@dataclass
class ResourceTypeConfig:
    name: str
    drive_axis: str
    benefit_curve: Literal["sigmoidal_saturating", "sharp_saturation",
                            "novelty_decay"] = "sigmoidal_saturating"
    spawn_density: float = 0.05
    benefit_amplitude: float = 1.0

@dataclass
class PerAxisDriveConfig:
    enabled: bool = False
    axes: list[str] = field(default_factory=lambda: ["hunger", "thirst", "curiosity"])
    per_axis_weight: dict[str, float] = field(default_factory=lambda: {
        "hunger": 2.0, "thirst": 2.0, "curiosity": 1.0
    })
    combiner: Literal["sum", "max", "learned"] = "sum"

@dataclass
class MultiResourceHeterogeneityConfig:
    enabled: bool = False  # master switch; bit-identical OFF
    resource_types: list[ResourceTypeConfig] = field(
        default_factory=lambda: [
            ResourceTypeConfig("food", "hunger", "sigmoidal_saturating"),
            ResourceTypeConfig("water", "thirst", "sharp_saturation"),
            ResourceTypeConfig("novelty", "curiosity", "novelty_decay"),
        ]
    )
    per_axis_drive: PerAxisDriveConfig = field(default_factory=PerAxisDriveConfig)
    resource_introduction_schedule: dict[str, int] = field(default_factory=dict)
```

**Bit-identical OFF requirement:** when `enabled=False`, the env's
internal RNG sequence and per-tick state-update path must match the
pre-SD-049 baseline exactly. All multi-resource RNG draws must live
inside an `if cfg.enabled:` branch; do not draw RNG values that get
discarded. This preserves all existing experiment reproducibility,
identical to SD-047's bit-identical OFF requirement.

**Per-resource-type bit-identical OFF**: each resource type can be
disabled independently for ablation studies (e.g. food + water enabled,
novelty disabled, to recover ARM_1 from ARM_2 without code change).

**Encoder side (ree-v3 / `ree_core/encoder/...`):** z_resource must
expand to carry identity. Current single-channel `z_resource` becomes
either (a) a one-hot identity slot concatenated with magnitude, or
(b) a low-D learned embedding. The choice is empirical and itself a
candidate child mechanism (registerable as MECH-(TBD) post-validation).

**Drive system side (ree-v3 / drive accounting):** per-axis vector
replacing single scalar; combiner pluggable. Cascades into goal-
conditioning pathway and downstream value reads.

**Sequencing**: cannot start substrate code change until SD-047 lands
and releases `causal_grid_world.py`. Until then, substrate edit is
scoped but not begun. See open TASK_CLAIMS for SD-047 implementation
session status.

---

## Related claims

- **SD-015** -- primary unblock; the upstream substrate this enables.
- **MECH-229** -- primary behavioral test of the wanting/liking
  dissociation that becomes possible.
- **MECH-230** -- z_goal latent structure that becomes non-trivial.
- **Q-030** -- the explicit 6-cell routing question that becomes
  well-posed.
- **MECH-117** -- supports its current stable rating with non-
  degenerate evidence.
- **MECH-216** -- schema generalisation across identity-distinct cues.
- **ARC-030** -- approach-avoidance symmetry across goal types.
- **ARC-032** -- theta-routing across goal identities.
- **SD-012** -- substrate-conditional dependency; per-axis extension
  required, triggers `pending_substrate_reconfirmation` on
  SD-012-emergent invariants.
- **SD-005** -- self/world latent split must continue to hold under
  multiple resource identities; depends_on but not modified.
- **SD-047** -- parallel substrate enrichment, independently
  implementable but file-coordination required (both touch
  causal_grid_world.py).

## Lit-pull recommendation (pre-implementation)

Before substrate work begins, commission a focused lit-pull on:

- Wanting vs liking dissociation (Berridge & Robinson canonical;
  ventral pallidum vs nucleus accumbens; opioid vs dopamine).
- Multi-resource foraging and identity-distinct goal selection
  (optimal foraging theory anchors; primate / rodent multi-resource
  experimental work).
- Non-homeostatic motivation (curiosity, novelty-seeking, intrinsic
  motivation in animals; predictive salience without consummatory
  reward).
- Developmental introduction order of motivational classes (developmental
  psychology on staged motivational maturation -- relevant for the
  curriculum hook's downstream validation).

This follows the biology-before-formal-definitions rule: SD-049 is
operationally simple but the *signature features* the encoder should
learn (identity tag vs spatial bias vs benefit-curve shape vs drive-
axis coupling) are empirical questions about how biological
goal-discrimination systems actually represent identity-distinct goals.
Skipping this risks a philosophy-right / mechanism-wrong implementation
that produces a clean PASS on a wrong test.

Anchor candidates:

- Berridge & Robinson 2016, AJP (incentive salience review)
- Smith et al. 2010 (ventral pallidum hedonic hotspots)
- Stephens & Krebs 1986 (optimal foraging theory baseline)
- Berlyne 1960; Kidd & Hayden 2015 (curiosity / non-homeostatic
  motivation review)
- Spelke developmental work on object-kind discrimination (relevant
  for the curriculum-introduction hook)

---

## Phase 1 implementation note (2026-05-03)

The substrate-side additions (multi-identity resources + curriculum hook)
and a Phase 1 per-axis drive vector parallel to the legacy `agent_energy`
scalar were implemented on 2026-05-03 in
`ree-v3/ree_core/environment/causal_grid_world.py` as flat kwargs on
`CausalGridWorld.__init__`. See `ree-v3/CLAUDE.md` SD-049 section for the
full data-flow / config surface / smoke results.

Deviation from the SD doc that requires explicit follow-on tracking: the
per-axis drive vector is implemented as PARALLEL to `agent_energy` rather
than REPLACING it. The legacy single-scalar drive_level pathway through
every SD-032 consumer (AIC / PCC / pACC / dACC / salience / override /
MECH-295 bridge) continues to read `obs_body[3]` (which is overridden by
`1.0 - combiner(per_axis_drive)` when per-axis is enabled). The per-axis
vector is observable through `obs_dict["per_axis_drive"]` for new
experiments and the deferred Phase 2 encoder upgrade. This is a cleaner
phased landing: Phase 1 lands the env substrate without the cascade
through every consumer; Phase 2 cascades the per-axis read sites into
the SD-032 cluster with explicit consumer-by-consumer migration.

**Phase 2 scope (deferred, registered in `substrate_queue.json`):**
1. `z_resource` encoder identity expansion: one-hot identity slot
   concatenated with magnitude OR low-D learned embedding on the larger
   world_obs (325 ARM_2 / 375 ARM_3). The existing ResourceEncoder reads
   the larger obs unchanged but does not yet produce an identity-aware
   latent; Phase 2 adds the supervised identity-recovery head and the
   phased-training protocol (P0 frozen identity-classifier head; P1
   joint training on the identity-aware z_resource).
2. SD-032 consumer cascade: AIC, PCC, pACC, dACC, salience coordinator,
   override regulator, MECH-295 bridge each migrate from reading
   `goal_state._last_drive_level` (the collapsed scalar) to reading
   `obs_dict["per_axis_drive"]` directly when SD-049 per-axis is on.
   Triggers `pending_substrate_reconfirmation` on SD-012-emergent
   invariants per the invariant-types governance rule.
3. Validation experiment V3-EXQ-514: 4-arm substrate gradient sweep
   exercising the trained identity-aware z_resource. Pre-registered
   acceptance: ARM_2 - ARM_0 `goal_resource_r` lift >= 0.4 (target
   0.066 -> >= 0.5); identity-recovery linear probe accuracy > 0.6 in
   ARM_2; `wanting_target != liking_target` trajectory fraction >= 0.6
   in ARM_2 (near zero in ARM_0 / ARM_1); per-axis drive ANOVA on
   z_goal cluster IDs p < 0.01 in ARM_2. Five-row interpretation grid
   per Validation Experiment section above (including the Woo/Spelke
   falsifier branch routing MECH-229 to substrate_conditional with V4-1
   multi-agent-ecology dependency on flat-failure).

**Phase 1 validation experiment (V3-EXQ-513):** substrate-readiness
diagnostic only. 4-arm sweep + curriculum check. 13 acceptance criteria:
C0 bit-identical OFF; C1a-b ARM_1 novelty-gated + food/water spawn;
C2a-f ARM_2 substrate signatures (world_obs_dim, per-type spawn,
per-axis drive evolution, contact counts, novelty familiarity growth,
agent_energy divergence from legacy path); C3a-b ARM_3 obs-dim and
4-of-5 type spawn; CC1-2 curriculum gates water at step 0 and releases
at step 1000. PASS = SD-049 substrate is calibrated and ready for
Phase 2. FAIL on C0 -> bit-identical OFF guarantee broken; FAIL on
C2c -> per-axis depletion not running; FAIL on CC1/CC2 -> curriculum
hook miswired.

**Phase 1 validation outcome (V3-EXQ-513):** PASS 13/13 on 2026-05-03.
Substrate calibrated, Phase 2 unblocked.

---

## Phase 2 implementation note (2026-05-04)

The encoder-side Phase 2 follow-on landed on 2026-05-04, anchored on the
2026-05-04 lit-pull verdict
(`evidence/literature/targeted_review_sd_049_encoder_identity_expansion/
verdict.md`, **Option C hybrid at confidence 0.78**). The verdict
recommendation: shared trunk MLP encoder + identity-classifier head
(cross-entropy on `obs_dict["sd049_consumed_type_tag_this_tick"]`) +
magnitude head (existing SD-018 `resource_prox_head` pattern preserved).

### Implementation surface

`ree-v3/ree_core/latent/stack.py` -- `ResourceEncoder` extended:

```python
class ResourceEncoder(nn.Module):
    def __init__(self, world_obs_dim, z_resource_dim=32, hidden_dim=64,
                 use_identity_classifier=False, n_resource_types=3):
        super().__init__()
        # Shared trunk (Schapiro 2017 monosynaptic-analog)
        self.encoder = nn.Sequential(
            nn.Linear(world_obs_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, z_resource_dim),
        )
        # Magnitude head (SD-018 pattern preserved)
        self.resource_prox_head = nn.Sequential(
            nn.Linear(z_resource_dim, 1),
            nn.Sigmoid(),
        )
        # Identity-classifier head (Schapiro 2017 trisynaptic-analog readout;
        # Ballesta-Padoa-Schioppa 2019 labeled-line per-type populations;
        # Quiroga 2005 sparse explicit-code readouts)
        if use_identity_classifier:
            self.identity_head = nn.Linear(z_resource_dim, n_resource_types)
        else:
            self.identity_head = None

    def forward(self, world_obs):
        z_resource = self.encoder(world_obs)
        resource_prox_pred_r = self.resource_prox_head(z_resource)
        identity_logits = (
            self.identity_head(z_resource)
            if self.identity_head is not None
            else None
        )
        return z_resource, resource_prox_pred_r, identity_logits
```

`ree-v3/ree_core/utils/config.py` -- `LatentStackConfig` gains:

```python
use_identity_classifier: bool = False
identity_classifier_n_types: int = 3
```

`ree-v3/ree_core/agent.py` -- new `compute_resource_identity_loss` method:
cross-entropy on `obs_dict["sd049_consumed_type_tag_this_tick"]` (1..n_types
when consumption fired this tick; 0 otherwise -- skip supervision when 0).

`ree-v3/ree_core/environment/causal_grid_world.py` -- env now caches the
consumed-type tag BEFORE clearing the cell tag in the resource-consumption
branch and surfaces it as `info["sd049_consumed_type_tag_this_tick"]`. This
is the supervision target for the identity classifier; without this fix the
training loop would never receive a non-zero target because the cell tag
was being cleared before the info dict was built.

### Design choice: trunk-output preservation rather than concat

The verdict.md offered three Option-C instantiations: (1) shared-backbone-
split-heads with `z_resource = concat(z_trunk, identity_softmax)`; (2)
single-output-with-supervision (classifier as training-only auxiliary
head); (3) two parallel encoders. The implementation chose **a hybrid of
(1) and (2)**: identity_logits is exposed as a SEPARATE LatentState field
(not concatenated into z_resource), preserving `z_resource_dim=32` so
GoalState seeding (`z_goal_dim=32`) continues to work without a projection
layer or dim-mismatch shim. The classifier head's gradient still shapes
the trunk via the supervised cross-entropy loss (as in instantiation 1),
but downstream consumers read just the trunk output (as in instantiation
2). This is the minimum-cost realization of the Option-C hybrid that
respects existing GoalState dim contracts.

### Phased training (V3-EXQ-514 methodology)

- **P0 (joint training):** enable `use_identity_classifier=True`; backprop
  identity cross-entropy + resource_prox MSE + downstream task losses
  through the trunk. Default 30 episodes per arm.
- **P1 (frozen-classifier continuation):** freeze
  `identity_head.requires_grad_(False)`; continue trunk training under
  E1/E3/downstream task losses + resource_prox loss only. Default 10
  episodes per arm. Trunk develops similarity structure beyond what
  classifier supervision alone provides (Schapiro 2016 distributed
  substrate development).
- **P2 (evaluation):** measure goal_resource_r, identity-recovery linear-
  probe accuracy, per-axis drive evolution. Default 15 episodes per arm.

### Validation experiment (V3-EXQ-514) acceptance criteria

10 pre-registered checks across the 4-arm sweep (ARM_0 OFF baseline /
ARM_1 2-type / ARM_2 3-type default / ARM_3 5-type overshoot):

- **C0 ARM_0 baseline replicates:** `goal_resource_r >= 0.06` (V3-EXQ-322a
  baseline floor).
- **C1a ARM_1 obs_dim:** 250 + 3*25 = 325.
- **C1b ARM_1 classifier trains:** P0 last-quartile classifier loss
  decreases relative to first-quartile / random-init (~ln(3) = 1.10).
- **C2a ARM_2 obs_dim:** 325.
- **C2b ARM_2 goal_resource_r target:** `goal_resource_r >= 0.5` (target
  lift from EXQ-085x 0.066 baseline).
- **C2c ARM_2 lift over ARM_0:** `goal_resource_r_arm2 - goal_resource_r_arm0
  >= 0.2`.
- **C2d ARM_2 identity-recovery:** linear-probe accuracy on z_resource >
  0.6 (load-bearing signal per the verdict).
- **C2e ARM_2 per-axis drive evolves:** peak drive > 0.02 (sanity matching
  V3-EXQ-513 Phase 1 substrate readiness).
- **C3a ARM_3 obs_dim:** 250 + 5*25 = 375.
- **C3b ARM_3 classifier did fire:** P0 last-quartile loss > 0 (no crash
  on 5-type config).

PASS = all 10. PASS reading: SD-049 Phase 2 hybrid encoder validated.
SD-015 promotable; SD-049 v3_pending may be cleared (pending governance
review). FAIL maps to the 6-row interpretation grid in verdict.md
including the Woo/Spelke-style substrate-ceiling falsifier branch (joint
failure across ARM_2 AND ARM_3 with similar magnitude routes MECH-229 to
substrate_conditional with V4-1 multi-agent ecology dependency).

### Phase 3 follow-on (LANDED 2026-05-31)

The SD-032 consumer cascade was originally registered as deferred,
action-triggered by V3-EXQ-514 failure on the SD-032-mediated mode-
switching pathway only. It was instead landed **proactively** on
2026-05-31 under explicit user direction (AskUserQuestion at
2026-05-31T12:52Z confirmed: Full per-consumer axis-aware design,
substrate-only this session, no claim flips). The cascade is now in
place; the original deferred status is retained here for historical
reference.

The seven SD-032 consumers (AIC, PCC, pACC, dACC, SalienceCoordinator,
BroadcastOverrideRegulator, MECH-295 liking-bridge) now accept an
optional `per_axis_drive: Sequence[float] | numpy.ndarray |
torch.Tensor` kwarg on their `tick()` / `forward()` entry points, plus
a per-consumer combiner config knob.

When `per_axis_drive=None` (the default, taken when the master flag
`REEConfig.use_sd049_per_axis_consumer_cascade` is `False` OR when the
env does not surface `obs_dict["per_axis_drive"]`), every consumer
falls back to its legacy scalar `drive_level` path -- **bit-identical
OFF**, verified at 628/628 contracts + 7/7 preflight PASS.

When the master flag is `True` and `obs_dict["per_axis_drive"]` is
piped into `agent.sense()` via the new `obs_per_axis_drive` kwarg, the
agent's `_per_axis_drive_for_consumers()` gate threads the vector into
all eight consumer call sites with their per-consumer combiner.

Combiner defaults are biology-anchored:

| Consumer  | Combiner | Reading |
|-----------|----------|---------|
| AIC       | `max`    | urgency / interoceptive salience tracks the worst-deficit axis |
| PCC       | `mean`   | whole-organism fatigue integrates across axes |
| pACC      | `sum`    | allostatic-load accumulation (Baliki 2012) |
| dACC      | `max`    | control demand follows the most-pressing axis |
| Salience  | `max`    | external-task affinity scales with worst axis |
| Override  | `max`    | orexin recruits on worst-deficit axis (Mileykovskiy 2005) |
| MECH-295  | `max`    | fallback when `goal_axis_idx` is `None` |

MECH-295 additionally supports **axis-matched routing** -- the
canonical case the SD-049 design predicts axis-distinguishable output
for (MECH-229 wanting/liking dissociation, MECH-117 trajectory
dissociation, MECH-216 schema generalisation, Q-030 routing). When the
caller supplies `goal_axis_idx: int` (the resource-type index the
current goal corresponds to), both the anticipatory liking write at
the goal location AND the per-candidate approach cue scale with
`per_axis_drive[goal_axis_idx]` rather than the combined scalar. The
agent attribute `self._current_goal_axis_idx` (default `None`) is the
read site; experiment harnesses that wire identity-distinct goals set
this when an axis-tagged goal is active.

Shared helper module `ree_core/utils/per_axis_drive.py` provides
`collapse_per_axis_drive(vec, mode)`, `select_axis(vec, axis_idx)`,
and `validate_combiner(mode)` -- one validated implementation used
across all seven consumers + the contract test suite. Accepts python
sequences, numpy arrays, and torch tensors interchangeably; clips
output to `[0, 1]`; raises `ValueError` on unknown combiner modes.

Phase 3 contract tests live in
`tests/contracts/test_sd049_phase3_consumer_cascade.py` (28
contracts covering helper correctness, config defaults, per-consumer
bit-identical-OFF, per-consumer combiner correctness, MECH-295
axis-matched routing, and agent-level wiring).

**What Phase 3 does NOT include this pass:**

1. Behavioural validation of axis-distinguishable downstream effects.
   The V3-EXQ-514 successor work (the MECH-229 wanting/liking
   dissociation test on the full cascade) is owned by IGW-20260531-012
   under `goal_pipeline:GAP-2`; Phase 3 here is substrate-only.
2. `claims.yaml` flips. No claim status updates, no
   `pending_substrate_reconfirmation` flag changes on SD-012-emergent
   invariants. The invariant-types governance rule says
   `pending_substrate_reconfirmation` is appropriate when a substrate
   in an invariant's `emergent_from` drops below active; SD-012 has
   not changed status here -- only the consumer interface has -- so
   that flag is held for the /governance cycle that processes the
   first behavioural validation experiment on the full cascade.
3. Per-axis pACC drive_bias vector. pACC's autonomic write-back
   pathway is still whole-organism (`z_harm_a_norm` is the input,
   `drive_bias` is a scalar EMA). Per-axis pACC would be its own
   SD-level claim; pACC.tick now caches a per-axis-derived scalar
   diagnostic + offers `effective_drive_from_per_axis(vec, combiner)`
   as a helper, but the EMA accumulation logic is unchanged.
4. `_current_goal_axis_idx` agent-side wiring from `z_goal` /
   `z_resource` / `obs_dict["resource_type_at_agent"]` to a concrete
   axis index. The substrate accepts the index; the routing layer
   (which axis a given `z_goal` corresponds to) is its own design
   decision and depends on the SD-049 Phase 2 hybrid encoder's
   identity classifier output. Until that layer lands,
   `_current_goal_axis_idx` defaults to `None` and MECH-295 uses the
   combiner fallback (which still preserves backward-compat behaviour
   while exposing the per-axis vector for diagnostics).

The cascade is now in place; the original action-trigger
characterisation ("cleanup-of-substrate-coverage refinement, not an
acceptance-criterion prerequisite") is preserved here for historical
reference. Future behavioural experiments that want the full
axis-matched MECH-295 path enabled set
`use_sd049_per_axis_consumer_cascade=True` on the agent config and
provide `obs_per_axis_drive=obs_dict["per_axis_drive"]` to
`agent.sense()` on each tick.

### What this Phase does NOT settle

1. The wanting != liking trajectory dissociation (MECH-229 primary
   behavioural test) is not directly measured by V3-EXQ-514 acceptance
   criteria. Identity-recovery + goal_resource_r lift are the proxies
   the verdict commits to. A deeper MECH-229 behavioural test would
   require a custom paradigm (agent prefers X while satiating on Y) and
   is deferred to a follow-on EXQ post-V3-EXQ-514 PASS.
2. Whether to use contrastive supervision on the trunk in addition to
   the identity-classifier supervision. The verdict left this open;
   Phase 2 lands without contrastive aux loss. If V3-EXQ-514 ARM_2
   produces high identity-recovery but low goal_resource_r lift, this
   is one Phase 2.5 refinement to consider.
3. The SD-012 emergent-invariant `pending_substrate_reconfirmation` flag.
   Phase 2 does not change SD-012's interface (drive_level scalar still
   semantically meaningful via the combiner); whether the encoder change
   re-opens SD-012-emergent invariants for reconfirmation is a governance
   call deferred to the next governance cycle.

## Drive-coupling amend (kappa-scale + standing differential depletion) -- IMPLEMENTED 2026-06-17

Routed by the confirmed `failure_autopsy_V3-EXQ-514r_2026-06-17` (overshoot
disambiguator) to unblock the **MECH-436** drive-state-modulated-wanting leg
(`candidate` / `substrate_ceiling` / `pending_retest_after_substrate`). 514r
proved the drive channel CAN carve `most_wanted` at magnitude 5.0 (flips on 2/5
guard-passing seeds, non-zero on all 5), so 514q's natural `delta = 0.0` is a
drive-MAGNITUDE / environment artifact, **not** a falsification. The amend adds
the two coupled levers the autopsy prescribed (kappa **load-bearing**), both
no-op-default / bit-identical OFF; it **promotes nothing** (MECH-436 stays held
until the retest scores).

**Why both levers are needed.** `wanting[k] = base_value[k] * (1 + kappa *
per_axis_drive[k])`. For drive to flip the argmax between a high-`base_value`
object and a high-`drive` object, `kappa * (drive_i - drive_j)` must overcome the
`base_value` ratio. Two facts block this on the current substrate: (i) the fixed
`kappa = 2.0` times the in-run spread `~0.006` contributes `~0.012` -- swamped by
real `base_value` gaps that **exceed 0.5** on seeds 45/46/47; (ii) the P2 foraging
ecology **fully restores** the contacted axis to 0 on consumption, and the WL bank
is scored *around* consumption events, so the spread at scoring time is equalised
to `~0.006`. Scaling `kappa` (lever a) makes a realistic spread competitive with
the real base-value landscape; making the depletion **stand** (lever b) keeps the
spread argmax-relevant at the scoring moment.

| Lever | Knob | Default (no-op) | Effect when set | Locus |
|-------|------|-----------------|-----------------|-------|
| (a) kappa scale (load-bearing) | `GoalConfig.incentive_drive_kappa_scale` (surfaced via `from_dims`) | `1.0` (effective kappa unchanged) | effective kappa = `incentive_drive_kappa_weight * incentive_drive_kappa_scale`; a realistic per-axis drive spread competes with real object `base_value` gaps | `ree_core/goal.py` `IncentiveTokenBank.wanting()` |
| (b) standing differential depletion | `CausalGridWorldV2.per_axis_restoration_fraction` (env-only kwarg, not in `from_dims`) | `1.0` (full restore to 0 = pre-amend) | `restore = cur_drive * curve_mult * fraction`; `<1` leaves **standing** drive on restored axes -> a persistent argmax-relevant spread (paired with the existing divergent `per_axis_drive_decay`) | `ree_core/environment/causal_grid_world.py` |

Contract: `ree-v3/tests/contracts/test_sd049_phase2_drive_coupling.py` (C1 kappa
default bit-identical; C2 scale flips a `most_wanted` argmax the unscaled kappa
cannot; C3 full restore bit-identical; C4 partial restore leaves standing drive on
a real consumption step; C5 `from_dims` wiring; C6 clamp/fallback). MECH-094 N/A
(env stream + waking bank arithmetic). Phased training N/A (scalar arithmetic).
MECH-229 leg (a) (V3-EXQ-514o PASS 0.80) UNTOUCHED.

**Validation experiment: V3-EXQ-514s** (the 514r-successor MECH-436 retest) --
re-run the 514r overshoot + OFF/bank-disabled + recalibrated-argmax-relevance
readiness controls on the kappa-scaled + partial-restoration substrate.
Pre-registered promotion target: natural `mean(WL_drive - WL_nodrive) >=
max(k*pstdev(delta), 0.15)` on `>=2/3` seeds converts MECH-436 `substrate_ceiling
-> supports`. Non-vacuity preconditions self-route `substrate_not_ready_requeue`,
never a false `weakens`. `claim_ids=[MECH-436]`.

## Drive-coupling amend: BOUNDED kappa raise + deeper standing spread -- IMPLEMENTED 2026-06-19

Routed by the confirmed `failure_autopsy_V3-EXQ-514s_2026-06-18` (user-adjudicated:
clean self-route, substrate-ceiling **PARTIALLY LIFTED**). 514s ran the 2026-06-17
levers at `kappa_scale=6.0` + `restoration=0.3` and MET all five non-vacuity
preconditions, proving **lever (b) standing-differential-depletion WORKED**
(`enriched_spread_met` 1.0, `mean_drive_spread_max` 0.211 vs 514q's equalised
`~0.006`). The residual shortfall is localized to **lever (a)**: the WL metric is
argmax-flip-gated and on 3/5 seeds the real `base_value` gaps exceed what
`kappa=6.0 x spread~0.2` flips at natural magnitude (natural delta mean 0.064 <
margin 0.15; 2/5 seeds clear; overshoot mag 5.0 still flips 4/5).

This amend is a **calibration** of the existing no-op-default levers -- NO new flag,
NO `ree_core` default change. The bounded operating point (the V3-EXQ-514t retest
config):

| lever | retest value | bound rationale |
|---|---|---|
| (a) `incentive_drive_kappa_scale` | `6.0 -> 12.0` (effective kappa `2.0*12=24`) | a MODERATE `base_value` gap (1.0 vs 0.6) flips under a realistic standing spread `~0.25` while a CLEARLY-LARGER 10x gap (1.0 vs 0.10) does NOT -- drive carves near-ties without overriding a decisive gap. Kappa-alone could not close the gap *boundedly* (the `~0.2` natural spread is `~25x` smaller than the mag-5.0 overshoot), hence pairing with (b). |
| (b) `per_axis_restoration_fraction` | `0.3 -> 0.15` (WL-scoring env only) | leaves `~0.43` standing drive on a just-consumed axis (vs `~0.35` at 0.3) so the divergent-decay per-axis differences -- and the argmax-relevant spread -- are larger at the WL scoring moment; less kappa needed per flip. Training ecology stays 603n-canonical so survival/foraging competence is preserved. |

**Bounded constraints (the two new contracts).** `C7` OFF-floor-hard-zero: kappa
multiplies ONLY the per-axis drive term, so at ZERO drive `wanting()==base_value`
for ANY `kappa_scale` -- raising kappa cannot manufacture a drive-induced
dissociation absent a drive signal (the substrate guarantee behind the
`wl_off_floor_fraction ~ 0` control). `C8` bounded / MECH-229 leg-(a) intact: at
`kappa_scale=12.0` a clearly-larger 10x `base_value` gap is NOT flipped by a
realistic standing spread -> drive does not dominate `base_value` (a sated agent
still wants the clearly-better object). Brackets `C2` (a moderate gap IS flipped).
9/9 `test_sd049_phase2_drive_coupling.py` + goal/environment subsystem contracts +
7/7 preflight PASS; the bounded kappa math verified against the live `wanting()`
formula and the restoration lever against the live env.

**MECH-229 leg (a) wanting!=liking (V3-EXQ-514o PASS 0.80) UNTOUCHED.** No claims.yaml
status flips -- MECH-436 stays `candidate` / `substrate_ceiling` /
`pending_retest_after_substrate` until the retest scores.

**Validation experiment: V3-EXQ-514t** (the 514s-successor MECH-436 retest;
supersedes V3-EXQ-514s) -- same overshoot + OFF + recalibrated-argmax-relevance +
enriched-spread controls on the `kappa_scale=12.0` + `restoration=0.15` substrate.
Same promotion target; the five non-vacuity preconditions self-route
`substrate_not_ready_requeue` (never a false `weakens`); a preconditions-met FAIL
with overshoot still flipping routes another bounded retune (514u), NOT a
falsification. `claim_ids=[MECH-436]`; machine any.

## Density-preserving spawn (per-type density held constant across arms) -- IMPLEMENTED 2026-07-20

**Motivating failure.** `failure_autopsy_V3-EXQ-693a_2026-06-21` (confirmed):
ARM_2 (3type+novelty) `behav_contact_rate` **0.0099-0.0188** against a
`CONSUMPTION_FLOOR` of `0.02`, plus hazard-stage survival failing on 2/3 seeds ->
0 contributing runs -> non-vacuity `R1`/`R2`/`R3` all unmet. 693a already carried
the full 603n curriculum AND the 514t WL-harness port, so the shortfall was not a
harness defect.

**Root cause (code trace).** The SD-049 spawn branch in `reset()` drew a FIXED
budget and then SPLIT it across the active types:

```python
n_to_spawn = min(self.num_resources, len(forage_pool))   # fixed TOTAL
# ... then each spawned cell draws a type by weighted choice
```

So an n-type arm has ~n-fold lower density *per type* than a 1-type arm. Measured
at the canonical `num_resources=5`:

| n_resource_types | per-type spawn counts | note |
|---|---|---|
| 1 | `[5]` | |
| 2 | `[3, 2]` | |
| 3 | `[2, 1, 2]` | ARM_2 -- one type gets a single cell |
| 5 | `[2, 0, 1, 0, 2]` | ARM_3 -- **two types spawn zero cells** |

This is the ~2-3x band the observed contact shortfall sits in.

**Why this is more than a threshold shortfall -- it is a design confound.** The
4-arm substrate gradient varies per-type density *as well as* heterogeneity, so
`C_GR`'s ARM_2-ARM_0 lift is not attributable to identity alone. This also offers
a parsimonious reading of the pre-registered 693a watch item (`C_GR` margin
near-zero, and *negative* in ARM_3): ARM_3 is the arm with the most types and
therefore the sparsest per type, and on the table above it is the arm where two
types never spawn at all. A density-driven artifact of that shape would be easy
to misread as a genuine conversion-side falsification of SD-049 Phase 2.

**The lever.** `CausalGridWorldV2.sd049_preserve_per_type_density` (default
`False`, bit-identical). When `True`, `num_resources` is read as a
PER-ACTIVE-TYPE count:

```python
desired = self.num_resources * len(active_types)   # density-preserving
n_to_spawn = min(desired, len(forage_pool))
```

Scaling is on `len(active_types)`, **not** `n_resource_types`, so a type still
behind a `resource_introduction_schedule` gate does not inflate the budget --
per-type density stays constant as the curriculum introduces types, which is the
property the Stage-0/0b onboarding sequence needs.

**Truncation is surfaced, not silent.** `forage_pool` capacity can cap the scaled
budget, and a silent cap would reproduce exactly the confound this lever removes
-- invisibly. `obs_dict["sd049_density_budget_truncated"]` is `True` whenever the
pool bound the budget; `obs_dict["sd049_preserve_per_type_density"]` reports the
flag. Any experiment relying on constant per-type density MUST gate on the former
(treat a truncated run as substrate-not-ready, never as a weakens). The flag is
cleared per episode so the no-active-types edge case cannot leave a stale read.

**Bit-identical OFF.** The budget expression and the RNG draw sequence are
unchanged on the default path. Activation smoke 2026-07-20, all PASS: default
holds total 5 at 1/2/3/5 types; flag on gives totals 5/10/15/25 with per-type mean
exactly 5.00; truncation fires on a size-8 grid at `desired=200`; both diagnostics
present in `obs_dict` on ON and OFF paths.

**Scope.** This is the ENV half of the 693a autopsy's recommended amend. The
curriculum-calibration half (`scaffolded_sd054_onboarding` Stage-H / hazard-stage
survival, 2/3 seeds failing) lives under `ree-v3/experiments/` and therefore
belongs to `/queue-experiment`; it was chipped as a separate session 2026-07-20.
The two are kept separable deliberately, so a retest can attribute hazard-stage
survival failure to resource starvation or rule it out.

**No claims.yaml status flips.** SD-049 / SD-015 / MECH-229 / MECH-230 / MECH-436
are untouched; the 693a per-claim `non_contributory` tags stand until a retest
scores on the corrected substrate.

**Validation experiment: NOT YET QUEUED.** The natural owner is a `V3-EXQ-693b`
re-issue of 693a with `sd049_preserve_per_type_density=True`, retaining 693a's
three non-vacuity self-route guards and the `C_GR` watch item. Acceptance follows
the autopsy's `target` verbatim: ARM_2 `behav_contact_rate > 0.02` and
hazard-stage survival on >= 2/3 seeds.
