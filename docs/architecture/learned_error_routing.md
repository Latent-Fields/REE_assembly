---
title: "Learned Error Routing: Error as Information, Error as Threat (MECH-590, MECH-591)"
parent: "Control, Precision & Neuromodulation"
grandparent: Architecture
nav_order: 23
status: candidate
status_asof: 2026-09-25
status_claim: MECH-590
---

# Learned Error Routing: Error as Information, Error as Threat

**Claim IDs:** MECH-590 (learned routing significance of prediction error), MECH-591 (error route
conditions the locus of correction; v5)
**Origin:** thought-intake
[thought_intake_2026-09-25_error_as_information_error_as_threat.md](../../evidence/planning/thought_intake_2026-09-25_error_as_information_error_as_threat.md),
from raw thought `docs/thoughts/2026-09-25_error_as_information_error_as_threat.md`.
**Status:** candidate, substrate_conditional. DO NOT build in V3; DO NOT queue an experiment.

## 1. The decomposition

```text
PE_t  = mismatch content / magnitude        -> consumed by world and self models (E1/E2 learning)
C_t   = context and inferred cause           -> ARC-037 / MECH-585 attribution, hazard, controllability,
                                                social evaluation, safe-base cues
R_t   = learned route P(epistemic / threat / repair / hold | PE_t, C_t, history)
                                             -> consumed by the control plane: MECH-046 mode prior into
                                                SD-032a, SD-069 phasic burst, SD-099 defensive orienting,
                                                MECH-104 volatility interrupt, MECH-261 write gating
```

Invariant (non-overwrite): R_t may change the gain and control authority of an error's salience readout,
but never the mismatch content the models learn from. Pattern shared with ARC-132 (separable attractor
axes) and MECH-586 (uncertainty redirects control, does not discount cost).

## 2. What REE already owns (do not rebuild)

- Detection and precision: MECH-043, MECH-069, MECH-059, SD-020/MECH-258, MECH-585, MECH-510.
- Epistemic branch: MECH-482/483 (epistemic deficit, orient/survey), MECH-395, MECH-388, MECH-314a/b/c,
  MECH-205.
- Threat/defence hinge: MECH-046 + SD-035 (CeA/BLA), SD-032a, MECH-259, MECH-104, SD-069, MECH-106,
  MECH-489/SD-099.
- Mode-gated learning target: MECH-261, MECH-368, MECH-511.
- Fixed special case: MECH-111 (moderate PE = curiosity).

What is missing: nothing LEARNS that the agent's own error events predict aversive consequences. Every
PE-triggered lever in ree_core is fixed-sign, non-trainable arithmetic:
`ree_core/regulators/phasic_surprise_burst.py` ("No nn.Module, no learned parameters"),
`ree_core/pag/defensive_orienting.py` ("Non-trainable"), `ree_core/amygdala/cea.py` / `bla.py`
("Non-trainable: pure arithmetic"). The nearest trainable host is
`ree_core/pfc/trainable_escape_affordance_learner.py` (MECH-376 P_safety; `use_trainable_escape_affordance_learner`
default False). Its inputs are compact state features plus an action embedding, with no PE-event feature,
and it only biases action scores.

## 3. MECH-590 -- learned routing significance of prediction error {#mech-590}

See the claims.yaml entry. Predictions (thought sec 9) for a later /thought-digestion pass:
(1) matched error, different routing; (2) threat pairing shifts the learning target from causal model
correction to threat-context acquisition; (3) safe error-and-repair experience partly restores epistemic
routing (the human data suggest persistence through extinction: Riesel et al. 2012); (4) error-threat
coupling is context-specific before it generalises; immediate global generalisation implicates an
implementation shortcut; (5) see MECH-591.

## 4. MECH-591 -- error route conditions the locus of correction (v5) {#mech-591}

See the claims.yaml entry. It couples to LOVE-4 (`evidence/planning/loveability_ethical_agency_v5_plan.md`).
Its discriminating readout: safe-base protection must preserve error magnitude.

## 5. V3 experiment sketch (for a FUTURE /queue-experiment; NOT queueable now)

**Gates (all must hold before queueing):**
- G1: a native waking learner is live. The ree_core-owned trainer with a gradient-reach guard, at the
  current front (`evidence/planning/native_waking_trainer_design_20260925.md`), must be built and green
  on E1/E2 at the recipe's config.
- G2: a learned error-consequence routing head is built (complicated/buildable): a small trainable head
  whose input includes error-event features (world-forward PE magnitude, SD-069 event flag, the
  running-variance excess) plus context features. Its target is an aversive/control-loss outcome within
  k ticks. Its output modulates at least one existing route lever (SD-069 temp_delta sign/magnitude,
  SD-099 onset threshold, MECH-046 mode-prior write). Extending MECH-376's learner with a PE-event input
  is one option. A new flagged head is the other. Default OFF, parity-preserving.
- G3: /governance routes MECH-590 to V3, and welfare review under SENT-2 clears the threat-paired arm.

**Arms (matched seeds, matched training budget, matched total PE statistics):**
- A safe-error: world-forward PE events followed by safe continuation.
- B error-threat: PE events above threshold followed within k ticks by a hazard onset or harm pulse
  (viability preserved), regardless of location.
- C unpaired-hazard: the same hazard count and magnitude as B, delivered independently of PE events.
- D shuffled-timing: B's hazard events with timing shuffled relative to PE events.
- E head-lesioned B: B with the G2 routing head frozen at init. This is the mechanism control. A B-vs-A
  difference that survives in E is NOT learned error routing.
- F forced-neutral check: after development, each arm gets a forced neutral learning block, to show it
  can still correct the model.

**Probe:** in a neutral environment, an identical benign mismatch: a harmless transition-rule
perturbation, e.g. an action-effect remap or object relocation in one region, with no harm available.

**DVs:**
- (i) route readouts at the probe: SD-069 burst level/sign, SD-099 trigger rate, SalienceCoordinator mode
  probabilities, commit latency, selection entropy, SD-099 orient/withdraw split.
- (ii) model correction: reduction in world-forward loss on the perturbed transitions over N ticks after
  the probe, localised to the responsible component.
- (iii) threat-context acquisition: routing-head output on the probe context.
- Primary: B vs A (and C, D) differ on (i) AND show the (ii)/(iii) dissociation of Prediction 2; E removes
  the difference.

**Non-degeneracy preconditions (a null under any unmet one is uninterpretable, not evidence against):**
- P1: G1 holds; E1/E2 grads nonzero over the window at the run config.
- P2: error events are decorrelated from state/location identity (for example, perturbation sites
  randomised per episode), so only the error-event CLASS predicts the aversive outcome. Otherwise B
  learns place-threat (MECH-376 / residue field), not error-threat.
- P3: in B the routing head predicts the aversive outcome above a shuffled baseline. In A and D it does
  not.
- P4: raw PE magnitude at the probe is matched across arms within a pre-registered tolerance (detection
  preserved; the non-overwrite invariant is checkable).
- P5: every arm corrects the model in block F (no arm is simply unable to learn).

**Context-specificity follow-on (Prediction 4):** pair errors with threat only under one SD-065 safety-cue
state, and probe under both.

## 6. Out of scope

Social shame, status or humiliation machinery in V3 (sec 10 explicitly). Rewarding error production
(noisy-TV; MECH-458). Suppressing real-threat defence (the target is discrimination, not global curiosity).
No human phenomenology claims (shame, anxiety) are asserted as equivalences.
