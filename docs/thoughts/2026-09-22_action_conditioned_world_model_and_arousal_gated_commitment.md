Status: processed
Intake: evidence/planning/thought_intake_2026-09-22_action_conditioned_world_model_and_arousal_gated_commitment.md
Claims registered: MECH-580

# Action-conditioned world model, dynamic precision, and arousal control of commitment

**Date:** 2026-09-22
**Status:** processed 2026-09-22 -- ingested to the intake above (MECH-580, `candidate` / `substrate_conditional`). T1/T2/T3a/T3b already owned; see the intake novelty table.
**Parent thought family:** Control plane / commitment / E1-E2 forward models
**Companion thoughts:** `2026-09-02_decision_useful_counterfactual_world_models_under_uncertainty.md` (action-effect vs absolute prediction; already ingested into ARC-002), `2026-09-18_affordance_valuation_bridge_sensory_to_commitment.md`

## Verbatim prompt (user, 2026-09-22)

> it seems to me that an action conditioned world model is an owed capability of REE and a genuinely
> dynamic precision control and arousal control that can alter selection for commitment. Should this be
> planned and incorporated into REE?

## Authorship note

The prompt above is the user's. Everything below was drafted by the session at the user's
instruction ("draft it") after a substrate and registry check, and is the session's expansion of
the prompt, not the user's own further words. Treat the expansion as a proposal to be checked
against `claims.yaml`, not as a captured conviction.

## Core thought

Three capabilities are named as owed. Each is a control-plane requirement on how a candidate future
becomes a committed action:

1. **An action-conditioned world model.** A forward model that predicts the next latent state given
   the current state AND the agent's own candidate action, trained so that its multi-step rollouts stay
   consistent. The contrast is an action-blind or single-step model: it can be accurate at "what
   happens next" while carrying no information about "what changes because of THIS candidate action",
   and so cannot separate candidate futures for selection. Without it E3 scores near-identical
   futures and commitment has nothing to choose between.

2. **Genuinely dynamic precision control.** Precision derived online from the system's own
   prediction-error statistics, not a fixed gain, and wired so that it changes selection and
   commitment (commit when variance falls; sharpen or soften the selection distribution with
   precision). "Genuinely" is doing work: a precision that is computed but consumed only as telemetry
   is not control.

3. **Arousal control that can alter selection for commitment.** A locus-coeruleus / noradrenaline
   analogue whose level changes what gets committed. The thought's own sharpening, made while
   checking the substrate, is that arousal has THREE separable faces on commitment and they must not
   be conflated:
   - **WHEN** -- the cadence of E3 updates (z_beta -> heartbeat rate).
   - **WHETHER** -- the commit threshold / gate: does commitment fire at all on this evidence.
   - **WHICH-SET** -- the BREADTH of the candidate set admitted to the commit gate. A global scalar
     cannot reorder candidate scores (it is argmax-invariant), so the only way a scalar arousal
     signal can change WHICH candidate is committed is by changing how many candidates are eligible:
     high phasic arousal narrows the admitted set toward the incumbent (exploit), low/tonic arousal
     widens it (explore). This is the adaptive-gain picture read onto a basal-ganglia eligibility
     envelope rather than onto a score reweighting.

## The dependency ordering the thought asserts

The WHICH-SET face presupposes capability 1. If candidate futures are not action-discriminable, a
breadth change admits or excludes nothing that differs, so any test of arousal's WHICH-SET face is
vacuous until the world model separates candidates. The WHEN and WHETHER faces do NOT presuppose it:
a threshold or a cadence can be moved and measured on near-identical candidates. So the observed
inertness of the commit-readiness gate and of the endogenous arousal signal (measured 2026-09-18 and
2026-09-22) is NOT explained by the world-model gap; those are separate instrument defects with
their own repairs.

## What "planned and incorporated" would mean

Not a new architecture plan. The expectation going in is that REE already holds most of this as
registered claims and partly as substrate, and that the deliverable is (a) a precise map of what is
owned, (b) any genuinely new claim registered narrowly, and (c) a routing decision on the two
arousal-side instrument defects.

## Possible affected components

E1 / E2 forward models (action conditioning, rollout consistency); E3 selector (precision-derived
commit gate, commit temperature, BG eligibility envelope); control plane (z_beta, urgency,
commit-readiness); heartbeat / MultiRateClock; BetaGate.

## Do not harden

Do not harden any of this until compared against existing REE mechanisms and literature.
Registering as `candidate` is not hardening.
