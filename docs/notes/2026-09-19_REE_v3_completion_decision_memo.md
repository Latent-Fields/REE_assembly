---
nav_exclude: true
---

# Decision memo: next research-to-build priorities for REE-v3

Prepared for Daniel Golden — 19 September 2026

## Decision

Prioritise the observation-to-consumer interface before adding curiosity, sleep, new scaffolds or other higher-level mechanisms. The evidence shows that `z_world` is improving upstream prediction while producing little improvement in consumer action agreement: V3-EXQ-1023 raised held-out R² by 0.1184 but action agreement by only 0.0081, still below the 0.85 target.

## Top three priorities

1. **Make representations usable by the installed consumers.**
   Test decoder-relative representation learning and action-conditioned predictive learning using matched capacities, budgets and held-out episodes. Separate external decodability, capacity-matched consumer learning and native consumer use. Treat simple conditioning, task-aware shaping and receiver learning as distinct explanations.
2. **Determine whether consumer learning is limited by policy capacity or shared-parameter interference.**
   Compare incumbent and fresh consumers on data containing distinguishable action–outcome situations. Measure learning, state-dependent selection, effective rank, unit activity and shared-loss gradients. Test conflict-management methods only if destructive interference is observed.
3. **Demonstrate a native causal path before evaluating downstream mechanisms.**
   Show that one learned, action-relevant distinction changes E1/E2 prediction, E3 selection and a meaningful closed-loop outcome, with matched, mismatched and zeroed-content controls. Only then make orienting, attribution, rule, commitment, curiosity and sleep tests decisive.

## Key competing explanations

- **Representation-access failure:** information is present in `z_world` but poorly conditioned for the bounded consumers.
- **Insufficient consumer or policy learning:** the current consumer lacks capacity, exposure or plasticity; the 20-episode near-single-action result does not distinguish these possibilities.
- **Shared-optimization interference:** objectives for prediction, preservation and decision-making damage one another through shared parameters.
- **Insufficient action-conditioned prediction:** the representation does not preserve distinctions needed for multi-step control.
- **Measurement or substrate failure:** communication-subspace, epistemic-deficit and sleep findings remain non-contributory or readiness-limited and should not yet be treated as established mechanisms.

## Immediate next diagnostic

Run the smallest representation-access-versus-consumer-trainability comparison:

- reuse frozen checkpoints and episode-disjoint data;
- compare the current representation with simple, training-fitted conditioning controls such as PCA or ZCA, keeping their purposes separate;
- retrain matched incumbent and fresh consumers for each coordinate system, or apply an exact input compensation where valid;
- hold architecture, targets, exposure and learning budget fixed;
- measure external decodability, consumer learning, native action agreement, state-dependent selection and closed-loop outcomes;
- include correctly paired, mismatched and zeroed-content controls.

Interpretation should be conditional:

- If conditioning rescues consumer learning, support an access or optimisation explanation.
- If fresh consumers learn while incumbents fail, investigate learning-history or plasticity effects.
- If gradients measurably damage one consumer while improving another, test shared-optimization interference.
- If none of these signatures appears, investigate whether the representation lacks action-conditioned, multi-step predictive sufficiency.

Do not treat higher auxiliary-head scores, increased action entropy, a measurement-validity pass or a powerful external decoder as evidence of native competence. The immediate objective is a competent observation–prediction–selection loop.

## Export note

This repository copy preserves the edited decision memo retrieved on 19 September 2026. Markdown punctuation escapes and a stray token were removed; the incomplete trailing phrase was omitted. The full research map contains the supporting literature and evidence.

[Full research map](2026-09-19_REE_v3_completion_research_map.md)
