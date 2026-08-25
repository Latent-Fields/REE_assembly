# Thought Intake: The Affordance-Indexed, Temporally Displaced Present

**Date:** 2026-08-25
**Raw thought file:** `docs/thoughts/2026-08-12_affordance_indexed_temporally_displaced_present.md`
**Companion thought (mechanistic hypothesis, processed separately -- see note below):**
`docs/thoughts/2026-08-12_ephaptic_aggregation_hippocampal_now_proposal_generation.md`
**Session:** ree-thought-intake-displaced-present-1ecf2e (worktree), 2026-08-25

## Note on the companion thought

The two 2026-08-12 thoughts are explicitly linked (the ephaptic thought's header names this one
as "Associated thought") but are epistemically distinct objects: this one is a
phenomenological/computational-timing hypothesis about what "now" is; the companion is a specific
candidate *biological* mechanism (ephaptic/oscillatory aggregation feeding hippocampal-analogue
proposal generation) for how a fast actionable-now estimate might be constructed. Per the task
instructions they are processed as separate thoughts. At the time this intake was written, another
session (`mech-266-rescore-circling-2d31ca`) was concurrently processing the ephaptic companion
thought into its own Stage 2 intake and claim registrations on the same shared files
(`claims.yaml`, `claims.json`, `WORKSPACE_STATE.md`). This is legitimate different-task overlap
(two thought-intakes appending distinct new entries), not duplicated work; the claims registered
below cross-reference the companion thought by filename only, not by claim ID (its claim IDs were
not yet known at write time and are not needed for this intake's own claims to stand).

## Verbatim prompt (core proposal)

> The subjective present may not correspond to the objective physical instant conventionally
> labelled *now*. Instead, the rich sensory and agentive experience of "now" may be a
> **short-horizon predictive construction displaced slightly into the physical future**, organised
> around the consequences of actions to which the organism is presently committed... The stronger
> proposal is: **The state experienced as the present may itself be a prediction: an
> affordance-indexed estimate of the organism and world at the short future horizon at which
> presently committed action is expected to take effect.**

The thought develops this into an architecture-shaped structure: (1) before commitment, multiple
candidate action-conditioned futures `a1 -> P(s(t+tau)|a1)`, `a2 -> ...` branch, and branching is
functionally useful (it is where choice can occur); (2) commitment reduces uncertainty about the
organism's *own* future behaviour, converting a branch into a "predictive tube," and this
self-generated predictability is what the thought argues licenses forward displacement of "now";
(3) the committed trajectory has a **commitment horizon** -- within it, prediction is precise and
sensory evidence corrects rather than re-decides; beyond it, futures branch again; (4) commitments
can nest at multiple simultaneous scales (footfall / path / destination); (5) affordances change
function across the commitment boundary -- before, they define choices; after, they support
execution/correction only; (6) small prediction errors are absorbed by correction, but sufficiently
large ones should trigger interrupt and reopen branching; (7) an interrupt should be visible, in
principle, as a *backward* reconstruction of the state estimate -- from the forward-displaced
predicted-now back toward a less-displaced corrected-now -- which the thought explicitly frames as
a falsifiable prediction (interruption should sometimes produce temporal-reversal-like timing
illusions); (8) for REE specifically, this reframes the architecture as `generate branching futures
-> compare -> commit -> protect execution -> predict through the committed trajectory -> smooth
deviations -> detect violations -> interrupt -> reopen choice`, rather than merely `generate
futures -> choose minimum cost`.

## What's new vs. existing REE docs/claims (novelty table)

| Thread in the raw thought | Existing REE coverage | Verdict |
|---|---|---|
| E2 forward-predicts action-conditioned affordance consequences, usable to evaluate candidates | **ARC-002** (E2 is the fast forward predictor of affordances) | Already owned. The raw thought's E2/E3/commitment sketch in "Implications for REE" restates this machinery; not re-asserted. |
| E3-derived prediction variance drives a relative commitment threshold gating action-selection ("commitment creates predictability" as *governed by* precision) | **ARC-016** (precision-to-commitment circuit) | Already owned for the environment/harm-precision direction. The thought's specific claim that commitment additionally licenses a forward-displaced *state estimate* (not just an action-selection threshold) is NOT covered -- see ARC-129 below. |
| Committed vs. uncommitted modes produce distinct behavioural/harm outcomes | **ARC-029** | Already owned; not re-asserted. |
| Pre-commit and post-commit prediction/error streams carry distinct information; "what a prediction means" changes at the commit boundary | **MECH-061** (commit-boundary token reclassification, EVB-0041 PASS) | Already owned as precedent that state/error semantics shift at commitment; does not itself claim the *current-state estimate* shifts forward in time. Cross-referenced, not duplicated. |
| BG-level gating of E3-to-action-selection propagation; surprise-gated interrupt can re-open the gate without full de-commitment | **MECH-090** (incl. EXQ-062b surprise-selectivity result) | Already owned for gate/propagation authority. Says nothing about what happens to the *state representation* treated as "now" at interrupt -- that gap is MECH-501 below. |
| Maintenance-time decommit / release coupling | **MECH-342** | Already owned; an action-authority mechanism, cross-referenced not duplicated. |
| WHEN to stop gathering evidence and commit (epistemic vs. pragmatic value trade-off) | **MECH-434** (epistemic commitment timing) | Already owned, inference-layer scoped. Adjacent to the thought's "commitment horizon" reasoning; cross-referenced. |
| Recursive multi-level nesting in REE's control architecture | **ARC-070 / MECH-321** (policy-primitive decomposition depth, V_s-boundary-triggered re-segmentation) | Already owned, but on a DIFFERENT axis (execution/control-primitive granularity, not temporal-displacement horizon). The thought's "nested commitments imply nested temporal horizons" is a distinct nesting claim -- see MECH-502 below. |
| The current-state estimate consumed by downstream proposal-generation/evaluation machinery is itself a short-horizon forward prediction rather than the literal most-recent encoded latent, with displacement conditioned on commitment quality | No existing claim asserts this; ARC-002/ARC-016/MECH-090 govern prediction-for-evaluation and commitment/gating, not what "current state" means as an input. Targeted search for "actionable now" / "predictive present" / sensor-latency-compensation / state-extrapolation framing: zero hits. | **Genuinely new -> registered as ARC-129.** |
| A major prediction violation should trigger a measurable backward reconstruction of the state estimate itself (distinct from gate re-opening or decommit) | No existing claim; MECH-090/MECH-342 cover action authority, not state representation. Targeted search for intentional-binding / chronostasis / postdictive-reconstruction / saccadic-remapping / readiness-potential framing: zero hits. | **Genuinely new -> registered as MECH-501.** |
| Multiple simultaneously-active commitments at different behavioural scales imply multiple concurrently-valid displacement horizons, not one global scalar | ARC-070/MECH-321 nest on a different axis (see above); ARC-016/MECH-090 currently model a single commit/uncommitted state. | **Genuinely new -> registered as MECH-502.** |
| Affordance-indexed smearing: different affordances (`a`) have different characteristic horizons `tau_a`, so "now" is not one uniform time-slice | No existing claim; closest is ARC-002's affordance-conditioning of E2's *predictions*, not of the *current-state estimate*. | Folded into ARC-129's own definition (a parametrisation of the same mechanism) rather than given a separate claim ID -- not independently testable apart from ARC-129. |
| Reinterpretation of Libet-style readiness-potential findings under an action-dependent, reconstructive "now" | No existing claim; this is interpretive/philosophical framing over established (non-REE) literature. | Not claim-worthy on its own; compatible with ARC-129, not separately registered. |
| "Prediction and postdiction need not be opposites" | General framing supporting MECH-501's falsifiability. | Not claim-worthy on its own. |
| Full falsifiable-consequences / behavioural-experiment list (raw thought's closing section) | N/A -- design material | Explicitly premature before ARC-129/MECH-501/MECH-502 are routed to V3; not queued. |

## Key formulations (verbatim, load-bearing)

> The state experienced as the present may itself be a prediction: an affordance-indexed estimate
> of the organism and world at the short future horizon at which presently committed action is
> expected to take effect.

> Commitment creates predictability.

> Before commitment, alternatives must remain available. After commitment, alternatives must
> normally lose authority.

> Unexpected interruption of a highly predictable action-linked sequence should sometimes reveal
> the forward displacement of subjective now through temporal reversal, expansion, discontinuity
> or related timing illusions.

> We may not experience the world precisely where it physically is. We experience the richly
> predicted point at which we are presently able to act upon it.

## Affected existing claims

- **ARC-002** -- cross-referenced only (E2's forward predictions are the candidate *source* ARC-129
  proposes a downstream consumer might read as "now"); not amended, not re-asserted.
- **ARC-016** -- cross-referenced as the proposed governor of ARC-129's displacement magnitude
  (commitment quality / E3-derived variance); not amended.
- **MECH-061** -- cross-referenced as existing precedent that state/error semantics shift at the
  commit boundary; not amended.
- **MECH-090** -- cross-referenced as the existing gate/interrupt substrate MECH-501's
  state-reconstruction claim sits downstream of, and MECH-502's nested-horizons claim implies may
  need multiple concurrently-active instances; not amended.
- **MECH-342** -- cross-referenced as the existing action-release mechanism MECH-501 is distinct
  from; not amended.
- **MECH-434** -- cross-referenced as the adjacent "when is a prediction good enough" inference-
  layer claim; not amended.
- **ARC-070 / MECH-321** -- cross-referenced and explicitly distinguished (different nesting axis)
  by MECH-502; not amended.

No existing claim's status, confidence, or evidence record was touched.

## Candidate claims -- REGISTERED this pass (not "for future registration")

Per standing practice (thought-intake registers genuinely-new ideas into `claims.yaml` in the
same pass, version-scoped, rather than leaving them as prose), the following were registered
directly:

- **ARC-129** -- `commitment.temporally_displaced_actionable_present`. `status: candidate`,
  `epistemic_category: substrate_conditional` (set explicitly), `implementation_phase: v4`,
  `version_relevance: v4_v5`. `depends_on`: ARC-002, ARC-016, MECH-061, MECH-090.
- **MECH-501** -- `commitment.interrupt_triggered_now_reconstruction`. Same status/category/phase
  pattern. `depends_on`: ARC-129, MECH-090, MECH-342.
- **MECH-502** -- `commitment.nested_multiscale_displacement_horizons`. Same status/category/phase
  pattern. `depends_on`: ARC-129, ARC-070, ARC-016, MECH-090.

All three: `status: candidate`, `polarity: asserts`, `registered_utc: 2026-08-25`. Compass /
architectural framing only -- promote/demote and `narrow_open_question` are suppressed by the
explicit `epistemic_category: substrate_conditional`; none of the three should be read as a V3
build authorization. Full comparison against existing machinery, and the explicit "out of scope"
list, is in the new architecture doc
`docs/architecture/temporally_displaced_actionable_present.md`.

## Next steps

1. **Literature pull, before hardening any of the three claims further**: intentional binding,
   action-effect temporal prediction and learned action-effect latency recalibration,
   sensorimotor temporal recalibration, chronostasis, predictive remapping and postdictive
   reconstruction around saccades, readiness potentials and the empirical complications to the
   classical Libet interpretation, motor commitment, affordance theory, hierarchical control.
   MECH-501 in particular should not be treated as literature-grounded until the postdictive/
   chronostasis family has been checked against a specific citation (none is verified yet -- the
   raw thought names the phenomena but not a specific paper).
2. **Version-routing decision**: all three registered claims are parked `v4`/`substrate_conditional`
   by default, per standing practice for thought-intake registrations. A future `/governance`
   cycle can route any of them onto V3 explicitly if a cheap, non-degenerate test becomes
   available.
3. **Behavioural/falsifiable-consequences design** (raw thought's closing sections) is rich
   (recalibrating action-effect latency, commitment-vs-preparation dissociation, interruption
   timing illusions, familiarity/predictability manipulations) but is explicitly premature before
   any of ARC-129/MECH-501/MECH-502 is routed to V3 -- do not queue an experiment from this list
   without that routing decision first.
4. **Check back with the companion ephaptic-aggregation intake once it lands** (session
   `mech-266-rescore-circling-2d31ca` was actively processing it concurrently with this session) --
   its claim IDs are not yet known here and were not needed for ARC-129/MECH-501/MECH-502 to
   stand on their own, but a future governance pass should confirm the two intakes' `depends_on`
   graphs are mutually cross-referenced once both are committed.
5. Raw thought file `docs/thoughts/2026-08-12_affordance_indexed_temporally_displaced_present.md`
   marked `Status: processed` with this intake linked, per the Stage 1/2 linking convention.
