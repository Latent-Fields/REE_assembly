# Precision Control

**Claim Type:** mechanism_hypothesis  
**Scope:** Precision control analogues and cognitive regimes  
**Depends On:** ARC-005, INV-008, ARC-004  
**Status:** candidate  
**Claim ID:** MECH-002
<a id="mech-002"></a>

---

Source: `docs/processed/legacy_tree/architecture/precision_control.md`

# Precision control (monoamine analogue)

REE uses depth-indexed precision gains \(\alpha_k\) to control how strongly errors at different depths shape belief and action.

## Minimal knobs

For each depth \(k\):

- `alpha_k` multiplies the prediction error term in training / inference.
- Optionally, `alpha_k` modulates sampling temperature (higher precision → lower entropy).

## Functional roles (analogue)

Precision control does not merely tune learning rates. It induces **qualitatively distinct cognitive regimes** by reshaping how and where temporal collapse, commitment, and exploration occur.

### Functional regimes (analogue)

- Dopamine-like (commitment / trajectory locking):
	Increases precision at action and policy depths.
	Promotes temporal collapse of a selected trajectory.
	Phenomenology: confidence, motivation, goal-directed flow.
	Pathology when excessive: over-commitment, mania, compulsivity.

- Noradrenaline-like (global uncertainty / interrupt):
	Transiently increases global gain and resets prior expectations.
	Breaks existing phase-locks and suspends temporal collapse.
	Phenomenology: alarm, vigilance, attentional narrowing.
	Pathology when excessive: panic, hypervigilance, fragmentation.

- Acetylcholine-like (sensory precision / corrigibility):
	Increases precision at sensory depths (\(\alpha_\gamma\)).
	Forces perceptual updating against top-down prediction.
	Phenomenology: clarity, vividness, perceptual anchoring.
	Pathology when excessive: sensory overload, derealisation.

- Serotonin-like (anti-collapse / horizon widening):
	Reduces premature commitment by limiting precision escalation.
	Stabilises exploratory hippocampal rollouts across longer horizons.
	Phenomenology: patience, emotional buffering, tolerance of ambiguity.
	Pathology when excessive: apathy, blunted affect, indecision.

⸻

Precision as a controller of temporal experience

Precision allocation determines whether temporally displaced predictions are:
- Collapsed into a lived present (high action-depth precision),
- Held in exploratory suspension (balanced precision),
- Or fragmented into competing, incoherent trajectories (misallocated precision).

Thus, shifts in precision do not merely alter accuracy or learning speed.
They alter:
- Whether a unitary “now” is constructed,
- How tightly perception is bound to action,
- How emotion and value predictions bias trajectory selection,
- And whether experience feels continuous, urgent, fragmented, or unreal.

## Astrocyte-aware regulatory stack

**Note:** The above framing treats monoamines as direct control knobs. A more neuroscience-informed perspective reinterprets monoamines as **broadcast meta-regulatory signals** that bias a slower astrocytic regulatory substrate, which then modulates precision/gain/plasticity with spatial and temporal lags.

See `docs/astrocyte_aware_regulatory_stack/` for:

- Why monoamines are not direct knobs (astrocytes mediate their effects).
- How to model the slow regulatory field \(R(x,t)\) that produces \(\alpha_k(x,t)\).
- Implications for care budget, inertia, and sleep recalibration.

For REE-v0, the direct-knob model (above) is a valid simplification. Future implementations should account for the layered regulatory architecture documented in the astrocyte-aware module.
---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- MECH-002

## References / Source Fragments

- `docs/processed/legacy_tree/architecture/precision_control.md`
