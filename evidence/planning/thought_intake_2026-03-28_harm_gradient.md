# Thought Intake: Harm Gradient Has Piecewise-Continuous Structure

**Date:** 2026-03-28
**Raw thought:** `docs/thoughts/2026-03-28_harm_gradient_piecewise_continuous_structure.md`
**Session context:** Emerged during ARC-024 literature pull (Fanselow predatory imminence
continuum / Mobbs 2007 vmPFC-PAG shift). ARC-024 posits a continuous harm gradient; the
biological literature reveals a separable piecewise structure that ARC-024 does not capture.

---

## Summary of Insight

ARC-024 correctly claims that the world harm-gradient is continuous and learnable. But the
Fanselow predatory imminence continuum (PIC) shows biological harm representation has
piecewise-continuous structure: response *topography* (form) transitions **discretely** at
threshold imminence levels (pre-encounter -> post-encounter -> circa-strike), while response
*vigour* varies continuously within each mode. This is not a contradiction of ARC-024 but a
separable claim about the internal structure of harm_eval's learned representation.

Mobbs 2007 provides corroborating human neural evidence: the vmPFC -> PAG transition at
threshold threat imminence is itself a discrete shift (not a smooth gradient), with distinct
neural signatures above and below the transition point.

The piecewise structure has architectural importance: a pure continuous gradient representation
would not trigger emergency defensive responses until harm is already very high; discrete
mode-transitions enable abrupt escalation at critical thresholds. This may be important for
safety-critical behaviour in V4 agents.

---

## Claims Registered

| ID | Title | Type | Phase | Description |
|----|-------|------|-------|-------------|
| MECH-224 | harm_eval.piecewise_gradient_structure | mechanism | v4 | E3 harm_eval learns both continuous intensity and discrete mode-transition thresholds corresponding to pre-encounter/post-encounter/circa-strike modes |

---

## Dependency Graph

```
MECH-224 (harm_eval.piecewise_gradient_structure)
  depends: ARC-024 (continuous harm gradient exists and is learnable)
  depends: MECH-071 (drive architecture -- panic/escape mode may require separate drive channel)
  compatible with (not contradicted by): ARC-024
```

---

## Validation Path

**V3 (binary test):** Does harm_eval output distribution show bimodal or trimodal clustering
rather than unimodal smooth distribution? Measure: histogram of harm_eval scores across
trajectories with varying threat proximity. Accept if 2-3 clusters with inter-cluster gaps
are detectable.

**V4 (full test):** Can agent learn to transition between qualitatively different defensive
strategies (routing modification, freezing, emergency escape) at discrete harm-gradient
thresholds? Accept if ablating threshold-crossing behaviour degrades emergency responses
disproportionately compared to continuous avoidance.

---

## Literature Support

- **Fanselow 2022 / predatory imminence continuum (PIC):** Pre-encounter (foraging mode),
  post-encounter (freezing/flight suppression), circa-strike (explosive escape/biting).
  Vigour continuous within mode; form discrete at threshold.
- **Mobbs 2007:** vmPFC dominant under distal threat (cognitive appraisal); PAG dominant
  under proximal threat (pre-wired defence). Neural signature is discrete, not graded.
