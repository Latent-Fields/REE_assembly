# V4 Developmental Testing Harness — Spec Sketch

**Registered:** 2026-04-21
**Purpose:** testing harness for ARC-059 / MECH-275/276/277/278 validation. Primary target is MECH-278 (object-schema formation via experimental action); secondary targets are MECH-277 (action-space discovery), MECH-276 (scientist-agent principle), and MECH-275 (sleep-phase aggregation).
**Status:** design sketch, not a full spec. Reserved as the V4 flagship harness so V3 work doesn't accidentally close off options the harness will need.

## Why this needs a purpose-built harness

The current CausalGridWorld does not support MECH-278 validation. Objects in CGW are effectively textures — they don't carry bundled affordances that respond distinguishably to intervention. The agent can't push, carry, or place anything; there is no interventional signature to discover.

MECH-278 requires:

1. **A body with an action palette rich enough to produce distinguishable interventions** — not just locomotion. Carry, push, place, and context-sensitive use.
2. **Objects whose features bundle consistently under intervention** — "this shape reliably does this cluster of things when pushed / carried / proximate / placed". Without consistent bundling, there is nothing to discover.
3. **Consequences that matter** — object affordances must influence goals, enemies, or landmarks, so the agent has reason to perform the interventions in the first place.

## Body spec — action palette

- Locomotion: move N/S/E/W.
- Carry: pick up / put down (agent holds at most one object; carrying modifies what the agent's proximity does).
- Push: apply directional force to adjacent object without carrying (object translates with resistance; different from carrying).
- Use (optional stage-2): context-sensitive interaction when adjacent to a compatible object.

The distinction between carry and push is load-bearing for MECH-278: carrying moves the object *and its affordance region* with the agent, while pushing translates the object through the world. Different interventional signatures.

## Object spec — affordance bundling

An object is `(marker, affordance_bundle)`. The marker is a shape/colour identity; the affordance bundle is what the object does under each intervention type.

**Starter set — 2 object kinds × 3 affordances each:**

| Object  | Proximity                       | Carry                              | Push / Place                                  |
|---------|---------------------------------|------------------------------------|-----------------------------------------------|
| Key     | nothing                         | unlocks adjacent door on entry     | placed on pressure-plate → opens bridge       |
| Lantern | reveals adjacent hidden square  | illuminates 3x3 region around agent| placed → static 3x3 illuminated region        |

**Extended set (stage-2 experiments):**

| Object  | Proximity                       | Carry / Push                          | Interaction                                   |
|---------|---------------------------------|---------------------------------------|-----------------------------------------------|
| Block   | nothing                         | pushes but does not carry             | blocks enemy path, blocks line-of-sight       |
| Lure    | nothing (inert)                 | carried like normal object            | placed → enemies move toward it, not agent    |
| Switch  | toggles remote feature on entry | neither carry nor push                | stationary                                    |

The set is deliberately small. Two object kinds with three affordances each is enough to produce an interventional-signature discrimination task; scaling up inflates state complexity without adding conceptual validation.

## Validation protocols

**Protocol 1 — observation-only control.**
Agent observes scripted or random-mover interactions with objects but cannot act. Prediction: fails to form stable object-schemas, because MECH-278 requires experimental action (not observation). Expected baseline for the correlational-learner null.

**Protocol 2 — experimental-action condition.**
Agent has full action palette; tasks require solving goal-puzzles that reward correct object use (unlock door with key, illuminate dark corridor with lantern, etc.). Prediction: forms stable object-schemas via the interventional signature, transfers affordance predictions to novel instances of the same object kind.

**Protocol 3 — ablated action palette.**
Agent has locomotion only (no carry, no push). Prediction: forms partial schemas — the proximity affordances are learnable, but carry-dependent and push-dependent affordances are not. Distinguishes which parts of the object-schema are action-dependent.

**Protocol 4 — confounder isolation.**
Introduce a feature that correlates with object presence but is not part of the object's causal signature (e.g., ambient tint shifts when a key is nearby but ambient tint doesn't change when the key is moved). Prediction: MECH-276 scientist-agent closure isolates the confounder via interventional contrast; a correlational-aggregation learner does not. This is the cleanest discrimination between MECH-276 and naive correlation.

**Protocol 5 — sleep-aggregation ablation (links to MECH-275).**
Run Protocol 2 with and without a sleep-phase aggregation step. Prediction: sleep-phase aggregation stabilises object-schemas across episodes, particularly when per-episode experimental evidence is ambiguous. Without it, schemas remain episode-local.

## Complexity ladder

- **L0** — 1 object kind, 2 affordances, 5x5 grid. Sanity: can the agent form even a trivial schema?
- **L1** — 2 object kinds, 3 affordances each, 8x8 grid. Starter validation condition.
- **L2** — introduce confounders (Protocol 4).
- **L3** — introduce novel object combinations at test time (e.g., lantern + lure placed together — agent must predict their combined effect without having seen the combination).
- **L4** — introduce other agents as stage-3 bridge (enemies with simple policies; later, cooperating agents). Feeds ARC-010 / MECH-274 validation.

## Build strategy

MiniGrid is the natural starting point — key/door/ball/box are already implemented, agent carry is native, grid semantics are standard. What MiniGrid does not provide and we would need to add:

- Lantern (illumination region that moves with the carrier; reveals hidden features).
- Lure (enemy-attracting placed object).
- Switch (remote-feature toggle).
- Confounder-injection hooks (ambient features that correlate with object presence but not intervention).
- Enemy agents with separable policies (Protocol L4, stage-3).

Alternative: a custom lightweight gridworld if MiniGrid's assumptions get in the way. Bias toward extending MiniGrid — rewriting the env from scratch wastes a year of prior art.

## Known risks

- **Affordance-bundle confounds:** if the 3 affordances per object are themselves correlated (e.g., only keys can be carried AND only keys unlock doors), the agent can't separate "being a key" from "being carryable-and-unlocks-doors". Need at least one shared affordance across kinds (both key and lantern can be carried) so the discrimination isn't trivial.
- **Task coupling:** if goal-reward tightly depends on correct object use, the agent may learn object-use as a policy without forming explicit schemas. The validation signature has to be decomposition quality, not task reward alone — probe with novel combinations (L3) and affordance predictions, not just end-task success.
- **Observation-only protocol calibration:** Protocol 1's prediction is "fails to form schemas", but this needs a sensible baseline — if the observation-only agent has a sufficiently rich passive model, it might form schemas from demonstrated affordances. Calibrate the demonstration density so Protocol 1 is a genuine null rather than a disguised Protocol 2.
- **Carry semantics:** the hardest spec question is what "carrying a lantern" means in the latent. The lantern's illumination region must travel with the agent in the observation (the 3x3 around agent reveals features), but the *object itself* is also in the agent's hand. How the z_world latent represents "this region is illuminated because of a thing I'm holding" is non-trivial and is exactly what MECH-278 is supposed to discover. Don't pre-engineer it.
- **MiniGrid ceiling:** if L3/L4 complexity saturates MiniGrid's rendering or semantics, graduate to a richer env. Set a re-evaluation gate at L2 completion.

## Integration notes

- Harness work should start before V3 closes — not to run V4 experiments, but to pin down object-affordance decisions that V3's z_world might otherwise prematurely commit to.
- A V3 developmental sub-experiment using L0/L1 is possible — ablate the engineered z_world (SD-005), replace with encoder trained only on the agent's sensory stream, and test whether experimental action in L1 recovers an object-schema decomposition that matches the engineered one. This is the cleanest V3-scale test of MECH-278's architectural shortcut flag.
- Scripts for this harness live in a V4-reserved directory; do not queue them to V3's experiment runner yet. Spec freeze before implementation.

## How to apply

- When V3 z_world design questions arise, check whether the answer forecloses a harness validation protocol. If yes, push back on the V3 design unless there is a strong V3-local reason for the commitment.
- When extending the object set beyond the starter L1 spec, preserve the discrimination constraint: at least one affordance must be shared across kinds so the agent can't collapse object-identity onto a single affordance.
- When designing Protocol 4 confounders, the confounder must survive intervention contrast (i.e., be genuinely correlational and not causally tied to the object's affordance bundle). A confounder that couples into affordances is not a confounder — it's a real feature.
