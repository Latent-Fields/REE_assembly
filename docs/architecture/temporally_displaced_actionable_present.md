---
title: Temporally Displaced Actionable Present
parent: "Executive & PFC Control"
grandparent: Architecture
nav_order: 26
status: candidate
status_asof: 2026-08-25
status_claim: ARC-129
---

# Temporally Displaced Actionable Present

**Claim IDs:** ARC-129 (core displacement claim), MECH-501 (interrupt-triggered reconstruction), MECH-502 (nested multi-scale horizons)
**Origin:** thought-intake [thought_intake_2026-08-12_affordance_indexed_temporally_displaced_present.md](../../evidence/planning/thought_intake_2026-08-12_affordance_indexed_temporally_displaced_present.md), from raw thought `docs/thoughts/2026-08-12_affordance_indexed_temporally_displaced_present.md`
**Companion (separate thought, processed independently):** `docs/thoughts/2026-08-12_ephaptic_aggregation_hippocampal_now_proposal_generation.md` proposes one candidate biological realisation (fast ephaptic/oscillatory aggregation feeding hippocampal-analogue proposal generation). This doc is architecture-level and agnostic to that mechanism.
**Status:** candidate / substrate_conditional / implementation_phase v4. Promote/demote-suppressed. Not a V3 build target.

> This is a **control-plane compass doc**, not a V3 implementation target. All three claims
> registered here are `substrate_conditional` / `implementation_phase: v4` -- they reframe and
> extend already-built V3 machinery (ARC-002, ARC-016, MECH-061, MECH-090, MECH-342, ARC-070)
> rather than proposing new V3 substrate. Do not build a displaced-present substrate or queue a
> V3 experiment from this doc without an explicit version-routing decision.

---

## 1. What already exists (do not duplicate)

REE already has substantial commitment/forward-prediction machinery that this thought reasons
about, but none of it currently addresses **what state a downstream consumer treats as "now."**

- **ARC-002** -- E2 is the fast, action-conditioned forward predictor of affordances
  (`world_forward`/`action_object`). Its predictions are consumed as an EVALUATION signal
  (are these action-conditioned predictions useful for discriminating viable from non-viable
  actions), not as a candidate **source** for the current-state estimate itself.
- **ARC-016** -- the precision-to-commitment circuit: E3-derived prediction variance drives a
  relative commitment threshold gating BetaGate/action-selection. This is the existing "how
  confident must REE be to commit" mechanism; it says nothing about what state is fed to
  proposal-generation once committed.
- **ARC-029** -- committed vs. uncommitted operating modes produce measurably distinct harm
  outcomes (the behavioural consequence layer split from ARC-016).
- **MECH-061** -- commit-boundary token: pre-commit E2 predictions and post-commit realised harm
  already carry distinct information (validated at ree-v1-minimal scale, EVB-0041 PASS). Existing
  precedent that "what a prediction stream means" changes character at the commit boundary --
  but not that the CURRENT-STATE ESTIMATE itself shifts.
- **MECH-090** -- BG-level beta-oscillation-analogue gating of E3-to-action-selection
  propagation; a surprise-gated interrupt can re-open the gate without full de-commitment
  (EXQ-062b). Governs propagation/action authority, not the state representation.
- **MECH-342** -- maintenance-time readiness-driven commitment-release coupling (decommit).
  Also an action-authority mechanism, not a state-representation mechanism.
- **MECH-434** -- epistemic commitment timing: WHEN to stop gathering evidence and commit,
  inverted-U between epistemic-freezing and anti-epistemic-panic. Adjacent ("when is a
  prediction good enough to act on") but scoped to the inference layer's evidence-gathering
  decision, not to what "now" means for downstream consumers.
- **ARC-070 / MECH-321** -- recursive multi-level POLICY-PRIMITIVE decomposition (re-segmenting
  a candidate action sequence into finer sub-elements at a V_s boundary). A control-flow/
  execution-structure hierarchy, not a temporal-displacement hierarchy.

None of the above is re-asserted below. Targeted search of `claims.yaml` for
intentional-binding / chronostasis / postdictive-reconstruction / saccadic-remapping /
readiness-potential framing, and for sensor-latency-compensation / state-extrapolation framing,
returned zero hits -- the psychophysical anchor and the "state fed downstream is itself a
prediction" framing are genuinely new to the registry.

## 2. The gap: three distinct novel threads

### 2a. The displaced present itself (ARC-129)

The thought's central claim is that the state REE's downstream proposal-generation and
action-evaluation machinery treats as "the current state" may be better modelled as a
short-horizon, forward-displaced prediction ŝ(t+τ) -- where τ is set by the causal-effect
timescale of whichever action REE is presently committed to -- rather than the literal most
recently encoded latent. Displacement magnitude should scale with commitment quality: larger
when the committed trajectory is well-predicted and low-variance (ARC-016's own variance
signal), collapsing toward the immediate encoded state when uncommitted or when prediction
quality is poor. This is orthogonal to ARC-002: ARC-002 says E2's action-conditioned predictions
are useful for scoring candidates; ARC-129 proposes that one of those same predictions (the one
along the currently committed trajectory) could additionally BE the current-state input other
machinery consumes as "now." The affordance-indexed smearing detail (different affordances imply
different τ_a, so "now" need not be one uniform time-slice) is folded into ARC-129's own
definition rather than given a separate claim ID -- it is a parametrisation of the same
mechanism, not an independently testable structure.

### 2b. Interrupt-triggered reconstruction (MECH-501)

If ARC-129 is right, a sufficiently consequential prediction violation should produce an
explicit, measurable BACKWARD reconstruction of the state estimate -- the forward-displaced
ŝ(t+τ) collapsing toward a less-displaced, evidence-corrected ŝ(t) -- distinct from and
downstream of MECH-090 (gate re-opening) and MECH-342 (decommit), which govern whether/when
ACTION authority releases but say nothing about what happens to the state REPRESENTATION at that
moment. The raw thought's falsifiable prediction ("unexpected interruption ... should sometimes
reveal the forward displacement of subjective now through temporal reversal, expansion,
discontinuity or related timing illusions") is the psychophysical analogue this mechanism claim
is loosely (not mechanistically) modelled on.

### 2c. Nested multi-scale displacement horizons (MECH-502)

REE can hold commitments at multiple simultaneous scales (a footfall-level motor commitment
nested within a path-level commitment nested within a destination-level goal commitment, in the
walking-with-a-cup example). ARC-129 as stated is a single-horizon claim; MECH-502 generalises it
to potentially several concurrently-active, differently-scoped displacement horizons, with local
correction at a fine grain not necessarily requiring re-opening of a coarser commitment. This is
explicitly distinguished from ARC-070/MECH-321's nesting, which is a POLICY-DECOMPOSITION-depth
(execution-primitive) hierarchy, not a temporal-displacement hierarchy -- the two nestings could
in principle be independent axes, and MECH-502 does not assert they must coincide.

## 3. Explicitly out of scope here

- The reinterpretation of Libet-style readiness-potential findings (raw thought section
  "Reconsidering neural decisions that precede reported conscious decisions") is an
  interpretive/philosophical framing compatible with ARC-129, not an independently testable
  REE-architectural claim; it is not given its own claim ID.
- "Prediction and postdiction need not be opposites" (raw thought section) is general framing
  supporting MECH-501's falsifiability, not a separate structural claim.
- The full falsifiable-consequences / behavioural-experiment list (raw thought, "Falsifiable
  consequences") is rich but premature before any of ARC-129/MECH-501/MECH-502 is routed to V3 --
  do not queue an experiment from it without that routing decision first, per the same discipline
  used for the companion persistence-taxonomy intake.

## 4. Literature to mine before any of this hardens

Per the raw thought: intentional binding, action-effect temporal prediction and learned
action-effect latency recalibration, sensorimotor temporal recalibration, chronostasis,
predictive remapping and postdictive reconstruction around saccades, readiness potentials and
the empirical complications to the classical Libet interpretation (readiness-potential
accumulation models, probe-based intention timing, retrospective-clock-report instability),
motor commitment, affordance theory, and hierarchical control. None of this has been pulled yet;
MECH-501 in particular should not be treated as literature-grounded until the postdictive/
chronostasis family has been checked against a specific citation.
