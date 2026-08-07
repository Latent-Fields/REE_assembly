# Thought intake: trajectory selection as coherence-weighted least action

**Date:** 2026-04-23 (raw); intake written 2026-06-05
**Status:** intake / structural analogy (NOT a registered claim)
**Raw thought file:** `docs/thoughts/2026-04-23_path_integral_constraints_search.md`
**Origin:** user mapping of REE trajectory selection (E1/E2/hippocampal rollout -> E3
commitment) onto least-action / path-integral formalism: candidate trajectories interfere,
coherent ones survive, E3 commitment is the stationary/symmetry-breaking event.
**Anchors:** INV-002 (coherence), ARC-018 (rollout viability mapping), MECH-061 (commitment
boundary), MECH-269 (verisimilitude), MECH-270 (ephaptic coupling), and Friston FEP as the
nearest existing neuroscience framing.

---

## 1. Core idea

Selection probability `P(tau) ~ exp(-beta E(tau)) * C(tau)`, where `E(tau)` is integrated
prediction error / constraint cost (the "action functional" analogue) and `C(tau)` is
cross-system temporal/phase coherence (the "interference phase" analogue). Stationary,
maximally-coherent trajectories dominate; E3 commitment = symmetry-breaking collapse onto one.
The author is explicit that this is a **structural analogy, not identity** (no quantum claim).

## 2. What is new vs what REE already has

| Element | Already in REE? | Verdict |
|---|---|---|
| Trajectory competition + thresholded commitment (E3) | **Yes** -- MECH-061 (commitment boundary), ARC-018 (rollout) | Confirms |
| Coherence as a multiplicative selection term beyond error minimisation | **Partial** -- INV-002 + verisimilitude MECH-269 assert coherence matters; the *multiplicative `exp(-beta E)*C` form* is new phrasing | Extension (formal, not substrate) |
| Distinction from FEP (REE adds value/harm weighting + explicit commitment gate) | **Yes** -- this is a standing REE-vs-FEP point | Confirms / sharpens |
| Phase/ephaptic coupling as the coherence carrier | **Yes** -- MECH-270 (ephaptic substrate) | Confirms |
| `hbar`-analogue temperature controlling trajectory diversity | **Loosely** -- exploration temperature exists in selection; not framed as an action-landscape control | Minor extension |

**Verdict: a re-description of REE's existing coherence-gated selection in physics language.**
Its real, non-metaphorical payload is one sharp empirical question (below). The risk the
thought itself names -- "many systems can be reformulated as optimisation over trajectories,
so formal similarity proves nothing" -- is correct and is the reason this is intake, not a claim.

## 3. The load-bearing question (shared with the binding intake)

**Is `C(tau)` non-reducible to `E(tau)`?** i.e. does a coherence term change which trajectory
is selected *independently* of prediction-error magnitude? The thought gives the right
falsification protocol:
- Operationalise `C(tau)` as cross-correlation / temporal-consistency across E1/E2/sensory
  streams, defined independently of outcome.
- Ablate `C(tau)` and compare against a pure `exp(-beta E)` selector.
- Unsupported if removing `C` produces no behavioural difference, or if `C` collapses into a
  reparameterisation of `E`.

This is the **same discriminator** as `thought_intake_2026-04-23_binding.md` section 3 --
binding-coherence and trajectory-coherence are the same `C(tau)`. **One coherence-ablation
experiment settles both intakes.** Do not design two.

## 4. Candidate claims

**RESOLVED 2026-08-07 -- no registration owed; the gate below was honoured and then DISCHARGED by
experiment.** The shared coherence-non-reducibility discriminator RAN as the
`V3-EXQ-641a -> 720 -> 725 -> 725a` lineage and came back **NO-CLAIM**: coherence-SPECIFICITY is
settled negative. The one decoupled positive salvaged from it is **MECH-456** (entity rebinding
under perturbation -- the twin binding intake's "Candidate MECH (rebinding-under-perturbation)"),
registered 2026-07-10 via `/claim-synthesis` from
`evidence/planning/claim_synthesis_rebinding_under_perturbation_2026-07-10.md`; MECH-456's own
title and notes record that it rests on `E(tau)` / stability machinery and explicitly does NOT
inherit the `C(tau)` formal import this intake warned about. See also **MECH-125**
(`coherence.multiconstraint_viability`), which already carries the
`C(tau)/R(tau)/F(tau)/I(tau)/P(tau)` selection-functional framing.

- **Candidate Q** (selection.coherence_nonreducibility) -- merged with the binding intake's Q.
  **SETTLED NO-CLAIM (V3-EXQ-725a). Not registered, and should not be** -- registering an answered
  question would re-open a closed lineage.
- **No new MECH/ARC until the ablation runs.** Per memory `feedback_biology_before_formal_definitions`,
  a formal-physics import (path integral / least action) is exactly the "philosophy-right /
  mechanism-wrong" risk class; registering an ARC on the strength of the analogy alone is
  contraindicated. Convert to a claim only if the coherence-ablation produces a behavioural
  divergence a pure error-minimiser cannot.

## 5. Affected existing claims / docs

- MECH-061, ARC-018, INV-002, MECH-269, MECH-270 -- all cited, none modified by this intake.
- If the ablation supports `C`-non-reducibility, the home doc is the verisimilitude /
  coherence architecture rather than a new "path integral" doc (avoid the physics framing in
  canonical docs; keep it as the intake's heuristic origin only).

## 6. Next steps (gated)

1. **Co-design the coherence-ablation experiment with the binding intake** (single run, two
   intakes settled). Primary acceptance: a behavioural difference between `exp(-beta E)*C` and
   `exp(-beta E)` selectors under matched error.
2. Hold all ARC/MECH registration until that result exists.

## 7. Cross-references

- Raw: `docs/thoughts/2026-04-23_path_integral_constraints_search.md`; twin intake
  `thought_intake_2026-04-23_binding.md`.
- Claims: INV-002, ARC-018, MECH-061, MECH-269, MECH-270.
- Memory: `feedback_biology_before_formal_definitions` (formal-import caution).
