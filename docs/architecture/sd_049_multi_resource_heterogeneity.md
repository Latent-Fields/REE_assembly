---
nav_exclude: true
---

# SD-049: Multi-Resource Heterogeneity

**Claim ID:** SD-049
**Subject:** `environment.multi_resource_heterogeneity`
**Status:** IMPLEMENTED (Phase 1, env-only) -- 2026-05-03
**Registered:** 2026-05-03
**Implemented (Phase 1):** 2026-05-03
**Phase 2 (encoder identity expansion + SD-032 consumer cascade):** REGISTERED, not implemented. See substrate_queue.json SD-049 entry. Validation experiment for the full claim (V3-EXQ-514: goal_resource_r lift + identity-recovery probe + wanting != liking trajectory dissociation) lands after Phase 2.
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
