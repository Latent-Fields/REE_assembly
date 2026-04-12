# Goal / Wanting Signal Chain — Provenance Map

**Scope:** z_goal seeding, wanting pathway, and approach motivation in V3  
**Status:** Diagnostic / architectural note  
**Claim IDs:** SD-012, SD-015, SD-018, MECH-112, MECH-216, ARC-030, INV-065  
**Created:** 2026-04-12  
**Why this file exists:** EXQ-322, EXQ-328, EXQ-331 produced a cascade of
non_contributory FAILs. Root cause is not amplification failure (SD-012 drive
modulation is correctly implemented) but a structural bootstrap gap in the signal
chain. This document maps the chain to show where the gap is and what each queued
experiment targets.

---

## 1. The Chain: Source to Behavior

```
world_obs [250 or 300 dims]
  |
  +--[ResourceEncoder (SD-015)]---> z_resource [32]
  |       supervised by: max(resource_field_view)         [TRAINED; wired into seeding]
  |       resource_prox_pred_r [0,1]                     [TRAINED; not wired as drive signal]
  |
  +--[SplitEncoder z_world path]---> z_world [32]
  |       supervised by: event_CE (SD-009) + proximity_head (SD-018)
  |
  +--[E1 LSTM hidden state]---> schema_salience [0,1]    (MECH-216)
          supervised by: resource_proximity_target (SD-018 target)
          gated by: schema_wanting_enabled flag (default False)

obs_body[3]  (agent_energy, [0,1])
  |--> drive_level = 1.0 - energy                        [SD-012, WIRED]

obs_body[11] (benefit_exposure, [0,1])
  |--> raw benefit contact signal                        [WIRED; zero except at contact]
```

**GoalState.update() comparator (SD-012):**
```
effective_benefit = benefit_exposure * z_goal_seeding_gain * (1 + drive_weight * drive_level)
if effective_benefit > benefit_threshold (0.1):
    z_goal <- (1 - alpha_goal) * z_goal + alpha_goal * z_source
              where z_source = z_resource (if SD-015 enabled) else z_world
```

**update_schema_wanting() comparator (MECH-216):**
```
if schema_salience >= schema_wanting_threshold (0.3):
    wanting_value = schema_salience * schema_wanting_gain * max(drive_level, 0.1)
    ResidueField.update_valence(z_world, VALENCE_WANTING, wanting_value)
```

**Downstream:**
```
z_goal (GoalState) -> E3.score_trajectory() via goal_weight
VALENCE_WANTING (ResidueField) -> hippocampal replay prioritization, trajectory scoring
```

---

## 2. Signal Provenance Table

| Signal | Source channel | Encoder/module | Supervision target | Discrimination | Wired into behavior? | Known failure mode |
|--------|---------------|----------------|--------------------|---------------|----------------------|--------------------|
| `z_resource` | `world_obs` | `ResourceEncoder` | `max(resource_field_view)` | resource-type cells vs background | YES — seeded into GoalState when use_resource_encoder=True | Sparse training signal in random-walk warmup; position-correlated signal |
| `resource_prox_pred_r` | `z_resource` | `ResourceEncoder.resource_prox_head` | `max(resource_field_view)` | proximity regression | **NO** — computed but not used as drive signal | Output consumed only by training loss; never reads downstream as motivation |
| `drive_level` | `obs_body[3]` | `compute_drive_level()` | none (derived directly) | energy depletion vs satiation | YES — scales effective_benefit in GoalState.update() | Amplifies seeding at contact only; does not cause approach |
| `benefit_exposure` | `obs_body[11]` | none (env scalar) | none (ground truth) | contact vs non-contact (binary at threshold) | YES — input to GoalState.update() | **Contact-gated**: zero except at resource cell entry; bootstrap deadlock |
| `z_world` | `world_obs` | `SplitEncoder` | event-CE + proximity_head | scene encoding (full position + content) | YES — fallback z_goal seed; E3 trajectory scoring | Position-confounded; after respawn z_world at new location has no goal signal |
| `schema_salience` | E1 LSTM hidden[0][-1] | `schema_readout_head` | `resource_proximity_target` | resource cue presence from E1 sequence model | **Conditional** — only when `schema_wanting_enabled=True` (default False) | Requires trained E1 with resource encounter history; also sparse in warmup |
| `z_goal` | GoalState attractor | GoalState.update() | benefit_exposure (above threshold) | goal maintained vs zero | YES — E3 trajectory scoring via goal_proximity() | Never activated if contact never occurs (EXQ-322: n_cosine_samples=0) |
| `VALENCE_WANTING` | ResidueField | update_schema_wanting() / update_benefit_salience() | benefit_salience (serotonin) | wanting terrain in residue field | YES — replay prioritization + hippocampal navigation | Zero unless schema_wanting writes occur |

---

## 3. The Bootstrap Gap

The chain has a circular dependency that prevents cold-start seeding:

```
z_goal needed for approach motivation
    -> approach motivation needed to reach resources
       -> resource contact needed to produce benefit_exposure > 0
          -> benefit_exposure needed to cross benefit_threshold
             -> threshold crossing needed to seed z_goal
```

SD-012's drive modulation (`effective_benefit = benefit_exposure * (1 + 2 * drive_level)`)
correctly amplifies the signal **when contact happens**, but does not cause contact to happen.
With `drive_level=1.0` (fully depleted), a single contact produces
`effective_benefit = 0.04 * 1 * 3 = 0.12 > 0.1` threshold — so SD-012 works correctly.
The problem is that random-walk warmup produces near-zero contact rate, so the threshold is
rarely reached at all, not that it is too high when reached.

This is the root cause of the non_contributory cascade:
- **EXQ-322 (SD-015):** `n_cosine_samples=0` — z_goal never seeded, so the comparison
  between RESOURCE_SEED and WORLD_SEED conditions could not be measured.
- **EXQ-328 (MECH-112):** `z_goal_norm=0.0` across all 6 seeds/conditions — same root.
- **EXQ-331 (ARC-030):** "Go sub-channel making zero difference" — with z_goal=0, the
  approach drive is zero in both JOINT and HARM_ONLY conditions.

The failure is at the **benefit_exposure** stage: the signal source is contact-gated
(binary: 0 except at resource cell entry) and contact is rare under random walk.

---

## 4. Wanting vs Liking — The Architectural Distinction

The gap corresponds to the Berridge wanting/liking dissociation:

| Component | Signal type | Trigger | Biology | REE module |
|-----------|------------|---------|---------|------------|
| Liking | hedonic impact | contact (resource consumed) | opioid system, NAc shell | `benefit_exposure` / `obs_body[11]` |
| Wanting | incentive salience | cue detection (resource visible) | dopamine, NAc core, VTA | **missing until MECH-216 is enabled** |

The current contact-gated pathway implements liking-triggered goal seeding, not
wanting-triggered approach motivation. Without a cue-based wanting signal, the agent
has no motivation to approach resources before first contact — which is the behavioral
equivalent of having no appetite until food is already in your mouth.

MECH-112 (wanting/liking dissociation) cannot be tested until both signals exist
independently. The claim requires wanting to fire on cue detection and liking to fire
on contact, and for these to dissociate under resource relocation. That test is
vacuous if the wanting pathway is a zero vector throughout.

---

## 5. What EXQ-326 / EXQ-332 Target in This Chain

**EXQ-326 (wanting_gradient_nav_fix, in queue):**
- Enables `schema_wanting_enabled=True` — wires schema_salience from E1 LSTM into
  VALENCE_WANTING writes on each tick when salience > threshold.
- Enables `use_resource_proximity_head=True` — SD-018 supervision forces z_world to
  represent resource proximity, giving E1 something discriminative to read from.
- Sets `drive_weight=2.0` (SD-012) — correct amplification when contact does happen.
- Three-phase training: P0 encoder warmup (proximity supervision active, no goal
  seeding), P1 wanting active (schema_wanting writes VALENCE_WANTING into residue
  field), P2 evaluation (benefit_ratio lifted vs ablation baseline).

The VALENCE_WANTING terrain in the residue field acts as a cue-driven gradient field
for trajectory scoring — the hippocampal navigator prefers trajectories through
high-VALENCE_WANTING regions even before z_goal is seeded from contact. This breaks
the bootstrap: the agent can develop approach tendency from field-view signals,
encounter resources more often, and then seed z_goal from those encounters.

**EXQ-332 (MECH-216 predictive wanting, in queue):**
- Redesigns the supervision target for the schema_readout_head: instead of
  current resource_proximity (reactive detection), the target is
  `future_resource_encounter` (binary: did the agent collect a resource in the next
  10 steps, computed from episode-level replay of cached E1 LSTM states).
- Attenuates direct resource gradient in observation (`resource_obs_scale=0.3`)
  so Landmark B (a predictive environmental cue co-located near resources) becomes
  the dominant discriminative input.
- This makes schema_salience genuinely predictive: it fires on landmark detection
  before the resource is in immediate field of view, enabling earlier approach
  initiation. Compare `corr(schema_salience, future_encounter)` vs
  `corr(schema_salience, current_prox)` to distinguish predictive from reactive.

---

## 6. Open Gap: resource_prox_pred_r is Computed but Not Consumed

`ResourceEncoder.resource_prox_pred_r` is computed on every call to `LatentStack.encode()`
when `use_resource_encoder=True`. Its training loss (MSE against `max(resource_field_view)`)
backpropagates through ResourceEncoder weights. But the **output value** of
`resource_prox_pred_r` is never read downstream by any behavioral module.

Compare this to MECH-216's `schema_salience`, which IS wired: when
`schema_wanting_enabled=True`, `schema_salience` writes into VALENCE_WANTING each tick.

The `resource_prox_pred_r` output could serve as a simpler, more direct wanting
signal than `schema_salience` — it is already calibrated to `[0,1]` (Sigmoid) and
supervised by resource proximity. However, directly wiring it would create a reactive
(non-predictive) wanting signal. EXQ-332's future-target redesign of schema_salience
is the preferred solution because it captures anticipatory wanting, not just reactive
detection.

This gap is not a bug — it is the correct design choice to prefer the predictive
pathway — but it should be documented so that ablation experiments can isolate the
two pathways: `resource_prox_pred_r` as reactive wanting vs `schema_salience` as
predictive wanting.

---

## 7. Verification Checklist for New Wanting Experiments

Before claiming z_goal seeding is functional in an experiment:

1. **n_seeding_events > 0** — at least one z_goal update must have occurred
   (check: `goal_norm_peak > 1e-6` across all seeds)
2. **n_cosine_samples > 0** — seeding must have occurred in enough episodes to
   measure the z_resource vs z_world cosine similarity comparison
3. **benefit_ratio > 0** — agent must be collecting resources in at least some
   episodes (otherwise the behavioral test is vacuous)
4. **schema_salience distribution** — if MECH-216 is enabled, verify
   schema_salience is not always < threshold (check histogram, not just mean)
5. **VALENCE_WANTING writes** — check `mech216_write_count` or equivalent
   diagnostic that wanting terrain is actually being written

If any of (1)-(3) are zero, the experiment is non_contributory for the same
reason as EXQ-322/328/331. Report as non_contributory, do not reassign outcome.

---

## 8. Related Claims and Experiments

| Claim | Role in chain | Gate status |
|-------|--------------|-------------|
| SD-012 | Drive-scaled benefit threshold (correctly implemented) | VALIDATED conceptually; EXQ-233 non_contributory due to gap |
| SD-015 | ResourceEncoder object-type seeding | IMPLEMENTED; EXQ-322 non_contributory (gap at benefit_exposure) |
| SD-018 | z_world resource proximity supervision (prerequisite for MECH-216) | IMPLEMENTED; required for schema readout training |
| MECH-112 | Wanting/liking dissociation | BLOCKED — requires both wanting and liking signals to exist independently |
| MECH-216 | E1 predictive wanting via schema_salience | IMPLEMENTED; enabled by EXQ-326 |
| ARC-030 | D1/D2 approach-avoidance balance | BLOCKED — approach side zero until wanting seeded |
| INV-065 | Proxy goal necessity (FIRST-PAPER GATE) | Blocked on benefit_ratio > 0 evidence |
| EXQ-326 | wanting_gradient_nav_fix — wires MECH-216 as approach signal | In queue, pending |
| EXQ-327 | MECH-163 goal-conditioned navigation | Blocked on EXQ-326 PASS |
| EXQ-332 | MECH-216 predictive wanting (future-target) | In queue, lower priority than 326 |

---

## Notes on Supervision Signal Quality

`max(resource_field_view)` as a supervision target for `ResourceEncoder` is a proximity
scalar, not a categorical identity signal. The claim that it "forces z_resource to represent
resource-type features, not spatial position" (SD-015 doc) requires a qualification: it
forces z_resource to detect resource-type cells in world_obs, which IS identity-based
(resource cells have a distinct type encoding in CausalGridWorldV2), but the training
signal is sparse at any given position unless the agent is near a resource.

The identity-generalization property (works after respawn because resource cell type
is the same across locations) depends on:
- The resource cell encoding in world_obs being type-consistent (not position-encoded).
- The encoder seeing sufficient examples of resource cells during training.

In practice, the second condition is violated in random-walk warmup before EXQ-326 enables
the wanting gradient. Post-EXQ-326, the approach tendency generated by VALENCE_WANTING
terrain increases resource encounter rate, which in turn provides denser training signal
for ResourceEncoder. The two pathways are therefore mutually reinforcing once either
achieves minimal activation — the problem is only in cold-start.
