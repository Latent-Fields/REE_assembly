Status: processed

Processed in:
- docs/claims/claims.yaml (MECH-098 encoder.reafference_cancellation, candidate; MECH-099 visual_streams.three_pathway_architecture, candidate)
- ree-v3/CLAUDE.md (SD-007 encoder.perspective_corrected_world_latent: IMPLEMENTED 2026-03-18; MECH-101 fix: z_world_raw_prev as reafference input)
- ree-v3/ree_core/latent/stack.py (ReafferencePredictor implementation; z_world_corrected = z_world_raw - ReafferencePredictor(z_world_raw_prev, a_prev))

---

# Three-Stream Architecture and Reafference Cancellation

**Date:** 2026-03-17
**Status:** processed (registered MECH-098, MECH-099; SD-007 implemented)
**Connects to:** SD-005, SD-007, MECH-069, MECH-095, MECH-096, ARC-017

---

## Trigger

SD-003 V3 experiment series (EXQ-002 through EXQ-012) plateaued at calibration_gap ≈ 0.027
(spurious BCE artifact) or collapsed to 0.0007 (signed regression, EXQ-012). The analysis
revealed two fundamental problems:

1. **E2 identity shortcut** — E2_world barely distinguishes between action outcomes because
   both `z_world_actual` and `z_world_cf` encode the same current egocentric view neighbourhood,
   regardless of action taken.

2. **SD-005 PASS was too permissive** — EXQ-001 only tested that z_self and z_world have
   slightly different aggregate correlations. body_selectivity_margin was negative (-0.137),
   meaning z_world was MORE sensitive to body movement than z_self was. The functional
   separation needed for SD-003 was never actually tested.

---

## Root cause: the egocentric view conflates perspective shift with world change

When the agent moves, the egocentric `world_state` observation changes because the *view
shifts* — not because the *world content* changed. E2_world is trained on this mixed signal:
most of the variation in z_world is just "I moved, view shifted", not "the world changed."

This is the E2 identity shortcut seen in training (e2_world_loss ≈ 0.0003 for 5×5 view):
E2 correctly learns that z_world doesn't change much step-to-step in content, because the
perspective shift is the dominant signal and the world content is stable. The learning goal
and the world structure conspire to make the identity shortcut optimal.

---

## The biological solution: reafference cancellation at the encoder level

Area MSTd (Gu et al. 2008, Nature Neuroscience 11:1201–1210) shows the biological answer:

- MSTd receives visual optic flow, vestibular (inertial self-motion), AND efference copy
  from premotor cortex simultaneously.
- It contains two neuron populations:
  - **Congruent neurons**: visual and vestibular heading preferences aligned — fires when
    visual motion is consistent with self-motion (reafference — expected perspective shift).
    Interpretation: world content is stable, I moved.
  - **Incongruent neurons**: preferences opposite — fires when visual motion does NOT match
    expected self-motion (exafference — genuine world change).
    Interpretation: the world changed beyond what my movement predicts.

This decomposition happens at early visual processing (MSTd is in the extrastriate cortex),
before information reaches hippocampus or prefrontal planning circuits. The encoder stage
in REE should implement this same decomposition.

The efference copy pathway (premotor → PPC via SLF I/II/III, confirmed by HCP tractography,
Rolls et al. 2023) delivers the motor command prediction to the parietal encoder. The
cerebellum (Wolpert & Kawato 1998) generates the forward model prediction of expected
sensory reafference from that command.

---

## Three visual streams, not two

HCP resting-state connectome analysis (Haak & Beckmann 2018, Cortex 98:73–83, n=470)
found a **triple dissociation** — three anatomically distinct white-matter-tract-level
pathways:

| Stream | Pathway | Function | REE mapping |
|--------|---------|---------|-------------|
| Dorsal | IPS/occipitoparietal | Self-motion, spatial action | z_self / SELF_SENSORY |
| Ventral | VO/PHC | Object identity, content | z_world content / WORLD |
| Lateral (third) | MT→MST/FST→STS | Dynamic motion, agency | Agency/harm channel → E3 |

The lateral/third stream terminates near TPJ (posterior STS → right TPJ). This is the
stream that processes biological motion and social/agency signals. It is the anatomical
location of MECH-095 (TPJ comparator).

This directly grounds MECH-069 (incommensurability): the three error channels are
incommensurable in part because they run on three anatomically distinct hardware pathways
with distinct white matter tracts. Collapsing them is anatomically incorrect.

---

## Implications for SD-005 and SD-007

**SD-005 (z_self/z_world split)** as currently implemented is a structural wiring change
(two encoder heads). It is necessary but not sufficient. The functional requirement is:

- z_world arriving at E2_world and E3 should be **perspective-corrected** — the encoder
  must subtract the expected view shift (predicted from z_self change / efference copy)
  before producing z_world.
- Only the residual after perspective correction represents genuine world-state content.

**SD-007 (new design decision)**: `encoder.perspective_corrected_world_latent` — the
encoder uses its z_self prediction (E2_self output for the current step) to predict
the expected perspective shift, and produces z_world as the residual after that prediction
is applied. This is the MSTd-equivalent computation, implemented at the REE encoder stage.

---

## Implications for MECH-096 (dual-stream encoder)

MECH-096 should be updated from "dual-stream" to "three-stream encoder" with:
- Dorsal head (→z_self): egocentric, action-relevant, motor-coupled, high temporal resolution
- Ventral head (→z_world content): perspective-corrected, object-identity, sustained
- Lateral head (→agency/harm input for E3): dynamic motion, biological motion, harm-salient events

The lateral head feeds E3's harm evaluation directly, bypassing the E2 forward model stage.
This would give E3 direct access to harm-salient sensory events without requiring E2 to
encode them in z_world — a separate, faster channel.

---

## Redesigned SD-003/SD-005 experimental test

The existing EXQ-001 (SD-005) must be replaced with a properly controlled test:

**Event-conditional measurement** (three event types explicitly separated):
1. **Empty-space moves**: agent traverses hazard-free corridor. z_self should change;
   perspective-corrected z_world should be *more stable* than raw z_world.
2. **Env-caused hazard**: agent position contaminated without agent movement. z_world
   should change (genuine world event); z_self should respond less than z_world.
3. **Agent-caused hazard entry**: both change. After perspective correction, the z_world
   change should be *larger* relative to baseline than in empty-space moves.

**E2 action-conditional divergence** (the SD-003 prerequisite):
- At near-hazard positions, `||E2(z_world_corrected, a_actual) - E2(z_world_corrected, a_cf)||`
  should be significantly larger than at safe positions. This tests whether the corrected
  z_world actually allows E2 to learn action-conditional transitions.

**Body selectivity as FAIL criterion** (not just world selectivity):
- `z_self_body_delta_corr > z_world_body_delta_corr` must hold (currently it is inverted).
- `z_world_world_delta_corr > z_self_world_delta_corr` must hold with meaningful margin (>0.1).

---

## Related Claims

- MECH-098: encoder.reafference_cancellation (new)
- MECH-099: visual_streams.three_pathway_architecture (new)
- SD-007: encoder.perspective_corrected_world_latent (new design decision)
- MECH-095: TPJ comparator (updated with lateral stream evidence)
- MECH-096: dual-stream encoder (updated to three-stream)
- MECH-069: error signal incommensurability (updated with anatomical evidence)
- ARC-017: sensory stream tags (three-stream mapping added)
- SD-005: z_self/z_world split (functional requirement strengthened)
- SD-003: causal attribution (requires SD-007 reafference correction)

## Literature

- Gu, Angelaki & DeAngelis (2008) Nature Neuroscience 11:1201–1210 — MSTd congruent/incongruent
- Haak & Beckmann (2018) Cortex 98:73–83 (PMC5780302) — three-stream HCP connectome
- Wolpert & Kawato (1998) Trends Cogn Sci 2(9):338–347 — cerebellar forward models
- Rolls et al. (2023) Cerebral Cortex 33:3142 — HCP PPC effective connectivity
- Pitcher & Ungerleider (2021) Trends Cogn Sci 25:100–110 — third visual pathway review
