# Thought intake: affect status matrix + awe placement

**Date:** 2026-06-07  
**Status:** thought intake / planning scaffold. Not a claim cluster yet.  
**Origin:** user note during REE-v3 organism/weaning discussion: a table of primitive proto-affects and compound affects, with explicit status slots for whether each is incorporated into REE design, considered, theorised-and-understood, theorised-but-not-understood, deferred, or unregistered, would be useful. Awe should be included, but probably not as a base primitive.

**Relationship to existing repo material:** extends, does not replace:

- `docs/architecture/affect_primitives.md` -- current harm register + Extension Register beyond harm.
- `evidence/planning/thought_intake_2026-06-01_protofeelings_audit_register.md` -- earlier proto-feelings audit-register thought.
- MECH-112, SD-011/SD-019, MECH-219, MECH-302/303/304, MECH-353/354/355/356, MECH-314, MECH-320, and V4 social/ethics thoughts.

---

## 1. Core idea

REE needs a **single affect-status matrix** spanning:

1. **primitive / base proto-affects** -- low-level control streams already needed for V3 action arbitration;
2. **proto-affects / control signals** -- standing streams that bias salience, commitment, action, learning, recovery, or mode;
3. **compound affects** -- higher states assembled from multiple streams, self/world modelling, memory, social attribution, or model-accommodation;
4. **meta-affects** -- signals about the relation between the agent's current model and the encountered world, including awe/wonder.

The matrix should not be an "emotion module". It is a **registry / maturity map**: one row per affect-like signal, with status, substrate, evidence, developmental timing, neighbour-differentiation, and smallest testable proxy.

This prevents two opposite errors:

- **overbuilding by human emotion name** (e.g. adding "awe" before the self/world/model-accommodation substrates exist);
- **under-registering important compound affects** until they are needed, leaving no place for them in the developmental map.

---

## 2. Proposed status categories

The matrix should use explicit status slots. Suggested columns:

| Column | Meaning |
|---|---|
| `affect_id` | stable registry label, not necessarily a claim ID |
| `kind` | primitive / proto-affect / compound / meta-affect |
| `REE_status` | incorporated / partially incorporated / considered / theorised-understood / theorised-not-understood / deferred / unregistered |
| `claim_backing` | SD/MECH/ARC/Q claim IDs, or none |
| `developmental_stage` | V3-core / late-V3 / V4-childhood / V5-social-adolescent / V6+ multimodal/embodied / theory-only |
| `substrate_requirements` | streams or mechanisms that must already exist |
| `computational_role` | what it changes: salience, E3 scoring, commitment, recovery, learning, horizon, self-weight, etc. |
| `neighbour_differentiation` | what it must not be collapsed into |
| `evidence_state` | lit-grounded / implemented / evidence-supported / pending experiment / speculative |
| `smallest_testable_proxy` | minimal experiment or behavioural signature |
| `pathology_if_absent` | failure mode when missing |
| `pathology_if_overactive` | failure mode when excessive |

A compact enum for `REE_status`:

- **incorporated** -- implemented or explicitly present in current design;
- **partially_incorporated** -- substrate exists but register/design/test incomplete;
- **considered** -- discussed and placed but no claim/design;
- **theorised_understood** -- plausible mechanism and neighbour-differentiation exist;
- **theorised_not_understood** -- recognised as important but mechanism uncertain;
- **deferred** -- intentionally later developmental stage;
- **do_not_build_yet** -- premature or dangerous before prerequisites;
- **unregistered** -- absent from the matrix.

---

## 3. Seed rows for the matrix

This is a starting scaffold, not the final registry.

| Affect / proto-affect | Kind | Current REE status | Existing anchors | Placement / note |
|---|---|---|---|---|
| Harm intensity | primitive | incorporated | SD-011, `z_harm_s` | V3-core sensory-discriminative harm stream. |
| Harm unpleasantness | primitive/proto-affect | incorporated/design-present | SD-019a, `z_harm_un` | Immediate affective "stop this now" stream; distinct from raw intensity and suffering. |
| Harm suffering | proto-affect/load state | incorporated/design-present | SD-019b, MECH-219, `z_harm_a` | Slow accumulated burden; controllability/escapability-sensitive. |
| Wanting / incentive salience | proto-affect | incorporated | MECH-112, `z_goal` | Approach/attractor formation; distinct from liking. |
| Liking / hedonic valuation | proto-affect | partially incorporated / deferred | MECH-112; benefit register deferred | Needs explicit status: REE has wanting/benefit machinery, but full hedonic/consummatory liking register is not yet complete. |
| Tonic vigor / opportunity cost of time | proto-affect / action-energy modulator | partially incorporated / v3_pending | MECH-320, ARC-068 | Alters action density / no-op opportunity cost; currently tied to 624-series retests. |
| Curiosity / novelty / uncertainty / learning-progress | proto-affect / exploration control | partially incorporated; evidence emerging | ARC-065, MECH-313/314/314a/b/c, Q-044 | 604c supports MECH-314 parent and novelty load-bearing once candidate diversity + modulatory authority are valid. |
| Relief | proto-affect | incorporated / registered | MECH-302 | Phasic offset-of-harm reinforcer; not safety or soothing. |
| Safety | proto-affect | incorporated / registered | MECH-303/304 | Learned predictor of threat-absence; not merely low harm. |
| Soothing / comfort | compound / social proto-affect | deferred / V4-social | MECH-355 | Down-regulates ongoing stress response, canonically via conspecific; do not fold into relief/safety. |
| Autonomic rebound | proto-affect / recovery modulator | V3-candidate | MECH-356 | Endogenous recovery-rate boost at stressor offset; sibling of soothing. |
| Effort / fatigue stop-recover | proto-affect / homeostatic cost | V3-minimal gated | MECH-354, SD-012, SD-017 | Stop-and-recover signal; not suffering/helplessness. |
| Blocked agency / control-failure | proto-affect | V3-candidate | MECH-353, `z_block` | Assert pole of blocked action while capacity belief retained; not harm. |
| Coercion / domination / injustice | compound social affect | deferred | V4 stub | Needs other-agent model; do not build as V3 primitive. |
| Disgust / contamination | proto-affect/compound | considered | SD-033/034 links | Candidate later row; must distinguish contamination/avoidance from harm and OCD-like checking. |
| Care / attachment | compound social affect | deferred | V4 ethics/social cluster | Requires other-agent model + co-regulation. |
| Grief / panic-loss | compound social affect | deferred | V4/V5 social cluster | Loss/attachment severance; not just harm or sadness. |
| Guilt / repair | compound moral affect | deferred / V4 | V4 ethics cluster | Should be built only with repair pathway; guilt != shame/self-condemnation. |
| Shame | compound social self-affect | do_not_build_yet / high risk | V4 ethics cluster | Dangerous before self/other/social-evaluation + repair separation. |
| Play | compound developmental mode | deferred / V4-V5 | play-mode substrate absent in V3 | Requires safe-enough world, exploration, self/other or object affordance modelling. |
| Awe / wonder / reverence | compound/meta-affect | theorised_not_understood; unregistered before this thought | no claim yet | Not base primitive. Candidate V4/V5 meta-affect: vastness + accommodation pressure + low immediate threat + horizon-widening + self-weight reduction + model-expansion gain. |

---

## 4. Awe placement

Awe should be represented, but **not implemented as a V3 primitive**.

Working hypothesis:

> Awe is a compound/meta-affect generated when the world-model encounters perceived vastness or high-scale coherence that cannot be assimilated into the current model without accommodation, while immediate threat does not dominate action. Its function is to suspend exploitative commitment, widen horizon, reduce self-central weighting, increase accommodation/rebinding gain, and tag the episode for replay/consolidation.

Minimal REE decomposition:

| Component | REE-facing interpretation |
|---|---|
| perceived vastness | world-model scale / depth / causal-complexity exceeds current compression |
| need for accommodation | prediction/compression failure requiring schema update, not simple novelty |
| low immediate threat or threat-contained | harm system does not force immediate avoidance/freeze |
| high coherence / beauty / meaning | structure is not noise; it invites model expansion |
| small-self / self-weight reduction | temporary reduction of self-centred priority relative to world/other/global model |
| horizon widening | lower immediate-commitment pressure, broaden planning/replay window |
| consolidation tag | replay/DMN-style binding; possible V5 language/interface relevance |

Candidate consumers:

- reduce immediate E3 commitment pressure unless threat dominates;
- increase curiosity/accommodation gain;
- tag state for offline replay/consolidation;
- reduce self-priority weighting in social/world-model evaluation;
- increase epistemic humility / caution around the encountered object.

Candidate pathology if absent:

- purely exploitative curiosity with no reverent pause;
- failure to recognise world-model insufficiency when encountering scale/beauty/complexity;
- premature compression of the unfamiliar into existing categories.

Candidate pathology if overactive:

- paralysis / submissive freeze in front of vastness or authority;
- grandiosity / meaning-overfitting;
- capture by charismatic or high-scale stimuli;
- reduced discrimination between beauty, threat, authority, and truth.

Therefore awe belongs in the matrix as **theorised_not_understood / V4-V5 / do_not_build_until_substrates_exist**, with a future `/lit-pull` before any claim is minted.

---

## 5. Literature anchors from quick research pass

- Keltner & Haidt (2003), *Cognition and Emotion*: awe prototype = perceived vastness + need for accommodation; hedonic tone varies by threat, beauty, exceptional ability, virtue, supernatural. This directly supports treating awe as a compound/meta-affect rather than a base primitive.
- Berridge / Robinson reward literature: wanting and liking are dissociable reward components; supports keeping wanting/liking as separate rows.
- Niv, Daw, Joel & Dayan (2007): tonic dopamine/opportunity cost of time grounds vigor as action-density/opportunity-cost control rather than generic reward.
- Panksepp/Biven primary-process affective systems are useful as a biological catalogue, but Barrett/constructed-emotion work cautions against treating every named human emotion as a hardwired primitive. REE should therefore track both **stream-level primitives** and **constructed/compound affect states**.

---

## 6. Recommended instantiation in REE_assembly

1. Create a concrete matrix artifact, probably:
   - `evidence/planning/proto_affective_status_matrix.v1.md`, or
   - a generated data file plus human-readable doc: `docs/assets/data/affect_status_matrix.json` + `docs/architecture/affect_status_matrix.md`.
2. Cross-link from `docs/architecture/affect_primitives.md` after the matrix exists. Do not overload the existing harm/extension register with every compound emotion.
3. Add `Awe / wonder / reverence` as a **deferred compound/meta-affect row**, not a claim.
4. Add a future `/lit-pull` chip: `targeted_review_awe_wonder_model_accommodation_small_self`.
5. Gate any claim-minting on prerequisites:
   - stable self/world model;
   - model-scale/compression-pressure metric;
   - immediate-threat override logic;
   - horizon/commitment modulation;
   - replay/consolidation tag;
   - social/self-weight modulation if using reverence/elevation variants.
6. Keep the design rule: **implementation follows failure signatures, not emotion names**. The matrix is allowed now; awe implementation is not.

---

## 7. One-line routing verdict

Build the **affect-status matrix** now as governance/bookkeeping; place awe in it as a deferred V4/V5 compound/meta-affect requiring model-accommodation and self/world-scale substrates before any implementation claim is minted.
