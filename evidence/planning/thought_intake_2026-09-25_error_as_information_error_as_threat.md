# Thought Intake: Error as Information, Error as Threat -- Learned Routing Significance of Prediction Error

**Date:** 2026-09-25
**Raw thought file:** `docs/thoughts/2026-09-25_error_as_information_error_as_threat.md`
**Session:** thought-backlog-20260925 (orchestrated backlog pass; drafting agent ING-D)

## Verbatim prompt (core proposal)

> Prediction error need not have a fixed affective or control meaning. [...] The computational
> distinction is not that one system detects prediction error and the other does not. Both detect it.
> The distinction is that the error has acquired a different **learned routing significance**.

The thought separates three things: (1) the mismatch itself; (2) the inferred cause and consequence of
the mismatch; (3) the learned control-plane significance of being in error, i.e. whether a mismatch
recruits curiosity/orienting/model revision, threat/defence/rapid action, repair, an uncertainty hold,
or a graded mixture. It proposes the decomposition `PE_t` (content/magnitude), `C_t` (context and
inferred cause), and `R_t = P(epistemic / threat / repair / hold | PE_t, C_t, history)`. The control
plane consumes `R_t`; world and self models consume `PE_t`. The invariant is that the history-dependent
route must never overwrite the error itself. The developmental hypothesis: two agents with matched error
statistics but different histories (errors followed by safe continuation vs errors followed by an
aversive, control-losing transition) should route an identical benign mismatch differently, before any
new harm occurs. The thought gives five predictions: matched error, different routing; threat pairing
changes the target of learning; safety restores epistemic routing; context-specificity before
generalisation; safe base protects correction without suppressing error. It gives a V3 experiment seed
explicitly gated on the native waking learner, a later social extension (LOVE-2/4/5), and cautions (do
not reward error, do not suppress real threat responses, arousal is not defensiveness, no phenomenology
smuggling, judge by model correction and not behaviour). The school example is motivational, not
evidence.

## What's new vs. existing REE docs/claims (novelty table)

| Thread in the raw thought | Existing REE coverage | Verdict |
|---|---|---|
| Both agents detect PE; detection and precision are not where the difference lies | **MECH-043** (DA precision weighting of unsigned PE), **MECH-069** (sensory / motor-sensory / harm-goal errors are incommensurable), **MECH-059** (confidence channel distinct from residual error), **SD-020 / MECH-258** (z_harm_a as precision-weighted harm-surprise PE), **MECH-585** (harm PE reads as world surprise only from a competent calibrated predictor) | Already owned. Cross-ref only. |
| Moderate PE is intrinsically rewarding; "alarm-surprise" must be told apart from "curiosity-surprise" | **MECH-111** (v3, candidate): moderate E1 PE generates positive valence. Its notes say: "The architecture needs to distinguish alarm-surprise (high magnitude, harmful context) from curiosity-surprise (moderate magnitude, safe novel context). This distinction may route through z_beta." | Owned as a FIXED magnitude-plus-context partition, with the routing left unresolved. The thought's mapping is LEARNED from error-consequence history and differs at MATCHED magnitude and context. That is new (next row but three). MECH-111 is extended, not amended. |
| Epistemic branch (orient, information-seeking, counterfactual breadth, replay priority, model plasticity) | **MECH-482** (epistemic_deficit accumulator), **MECH-483** (orient/survey regime), **MECH-395** (cue-triggered pre-approach orienting), **MECH-388** (epistemic action pressure), **MECH-314a/b/c** (curiosity sub-flavours), **MECH-205** (surprise-gated generative replay), **MECH-489 / SD-099** (defensive orienting: freeze -> orient/identify -> valence-gated approach/withdraw on unidentified onset) | Already owned. This answers the thought's own sec 14 item 4: MECH-482/483 cover the epistemic branch. The missing piece is on the threat-association side. |
| Threat branch: fast salience classification changes mode priors before slow explanation completes | **MECH-046** (CeA analogue writes a mode prior into the SalienceCoordinator from fast salience classification of z_harm_a), **SD-035** (BLA+CeA, "two peer non-trainable arithmetic modules"), **SD-032a** (salience-network coordinator, operating-mode variable), **MECH-259** (switch threshold), **MECH-104** (unexpected harm spikes commitment uncertainty), **SD-069** (phasic surprise burst on the E3 softmax), **MECH-106** (valence-asymmetric commitment threshold), **MECH-074c** (CeA fast priming) | The hinge machinery is owned and largely built. But every lever is keyed either to HARM (z_harm_a) or to FIXED-SIGN surprise arithmetic. None assigns a learned threat significance to the agent's own error events. Checked in code, see V3 feasibility below. |
| Threat routing changes the TARGET of learning (threat-context acquisition vs causal model correction), not the amount | **MECH-261** (operating mode gates which substrates may write: E3, episodic memory, policy, autonomic), **MECH-368** (event-level write-authority gate conditioned on PE, salience, pathway state...), **MECH-511** (deep-update eligibility includes "current mode") | Owned as mechanism. The thought's Prediction 2 is a consequence of the new route (below) feeding MECH-261's existing write gating. Folded into MECH-590 as a stated consequence, not registered separately. |
| **The routing significance of a PE event is a learned, history- and context-conditioned mapping acquired from what has historically FOLLOWED PE; dissociable from detection, magnitude and precision; at matched error statistics, error-consequence history changes the route** | No claim states this. Nearest: MECH-111 (fixed mapping); **MECH-510** (PE precision/salience separable from generative precision, not a learned consequence-conditioned route); MECH-511 (eligibility for deep revision, not a control route); **MECH-376** (trainable P_safety over state/cue/action/context; learns what STATES predict threat, has no own-error-event input); **MECH-078** (amygdala over-valences novel TERRITORY); **MECH-247** (trauma-shaped hypervigilant PERCEPTUAL priors); **ARC-037 / MECH-585** (attribute the CAUSE of an error, not its learned control consequence) | **Genuinely new -> registered as MECH-590.** |
| Invariant: the learned route must not overwrite or attenuate the error content | **ARC-132** (an attractor's carried quantities, valence vs predictive reliability among them, stay separable), **MECH-586** (sibling shape: uncertainty redirects control but must not discount adverse cost), MECH-059, MECH-069 | The separability pattern is owned. Its application to PE routing is a clause of MECH-590. |
| Pathology is overgeneralisation: benign errors inherit threat routing learned where error predicted harm | MECH-078, **MECH-541** (over-stabilised compensation), MECH-376 (contrastive target against safety overgeneralisation), **MECH-124 / MECH-208** (harm-weighted replay contracts options, avoidance in safe contexts), **ARC-086** (latent vulnerability axes) | Adjacent. Folded into MECH-590 (failure-mode clause and Prediction 4). ARC-086 axis membership left to /governance. |
| Reversibility under safe error-and-repair experience (Prediction 3) | **MECH-133** (safety memory must outcompete the threat attractor at state construction), MECH-376 | A prediction of MECH-590. Left for /thought-digestion. |
| The route recruited at detection conditions the later attribution locus of correction (LOVE-4); a safe base protects correction by changing the route, not by attenuating the error (sec 6, Prediction 5) | **MECH-413** (LOVE-4: correction without self-valence collapse; attribution locus 'I erred' vs 'I am unloveable'), **INV-082** (loveability as safe-base prerequisite), **MECH-414** (love-mediated repair), **MECH-382** (distancing operator) | Adjacent but distinct. MECH-413 fixes WHERE correction lands. It says nothing about the upstream control regime or about the MECHANISM of safe-base protection. **Registered narrowly as MECH-591 (v5).** |
| Do not reward being wrong / noisy-TV | MECH-458 (curiosity is an exploitation amplifier), MECH-441, MECH-314c | Owned. Design caution. |
| Arousal is not defensiveness | MECH-463, MECH-580, ARC-044 | Owned. Cross-ref. |
| Social extension (public exposure, status threat, rupture, reparable harm, global condemnation) | LOVE-2..LOVE-5 in `loveability_ethical_agency_v5_plan.md`; MECH-413/414; INV-082 | Owned as v5 plan territory. Not registered separately. |
| School / educational example | none needed | Motivational only, per the thought itself. Not claim material. |

## Key formulations (verbatim, load-bearing)

> The computational distinction is not that one system detects prediction error and the other does
> not. Both detect it. The distinction is that the error has acquired a different **learned routing
> significance**.

> The important invariant is that **the history-dependent control interpretation of an error must not
> overwrite the error itself**.

> A threat-conditioned learner can be highly plastic in the wrong target space.

> The pathology or developmental failure would be **overgeneralisation**: error events that are
> epistemically benign inherit the threat routing learned in contexts where error historically
> predicted harm, punishment, rejection, or loss of control.

> If "safety" works only by reducing or hiding prediction error, it has failed the intended mechanism.

> An intelligent system should not merely detect that it was wrong. It should learn what being wrong
> means in context -- while preserving access to the evidence that made the error visible.

## Affected existing claims

- **MECH-111** -- extended, not amended. MECH-111 is the fixed magnitude-plus-context special case. Its
  own open note ("alarm-surprise vs curiosity-surprise ... may route through z_beta") is partly answered
  by MECH-590: the split is at least partly learned from consequence history. Cross-ref only. (Its
  `location` anchor `docs/architecture/approach_avoidance_symmetry.md#mech-111` does not resolve; no such
  file exists. See next steps.)
- **MECH-046 / SD-035 / SD-032a / SD-069 / SD-099 / MECH-104** -- named as the existing hinge loci that a
  learned route would feed. All are fixed-arithmetic today. Not modified.
- **MECH-261 / MECH-368 / MECH-511** -- the write-gating machinery through which a threat route changes
  the target of learning. Cross-ref only.
- **MECH-482 / MECH-483 / MECH-395 / MECH-489** -- the epistemic and defensive-orienting consumers. Not
  modified.
- **MECH-510** -- distinguished: separable PE precision is not a learned, consequence-conditioned route.
- **MECH-376** -- distinguished, and named as the nearest trainable host: it learns threat-absence over
  state/cue/action, not the threat significance of the agent's own error events.
- **MECH-078 / MECH-247 / MECH-541** -- distinguished (territory over-valencing / perceptual prior shaping
  / over-stabilised compensation).
- **MECH-413 / INV-082 / MECH-414** -- MECH-591 supplies an upstream-regime and mechanism-of-protection
  constraint on LOVE-4. They are not amended.

No existing claim's status, confidence or evidence record was touched.

## Candidate claims -- REGISTERED this pass

- **MECH-590** -- `control_plane.learned_error_routing_significance`. The routing significance of a
  prediction-error event is a learned, history- and context-conditioned mapping, dissociable from
  detection, magnitude and precision. The learned route modulates the control/salience readout of an
  error and never overwrites the mismatch content. `status: candidate`,
  `epistemic_category: substrate_conditional`, `implementation_phase: v4`, `version_relevance: v4_v5`.
  Flagged for a /governance routing decision (the non-social core could be routed to V3 once the native
  waking trainer is live).
- **MECH-591** -- `development.error_route_conditions_correction_locus`. Under social correction, the
  error route recruited at detection conditions the attribution locus of MECH-413. A safe base protects
  correction by changing the route of a large error, not by attenuating it. `status: candidate`,
  `epistemic_category: substrate_conditional`, `implementation_phase: v5`, `version_relevance: v4_v5`.

Both use `polarity: asserts` and `registered_utc: 2026-09-25`. Architecture stub:
`docs/architecture/learned_error_routing.md`. Neither claim authorises a V3 build or a V3 experiment
today.

## Literature (metadata-level check via PubMed, abstracts read; full texts NOT read)

- Hajcak & Foti 2008, Psychol Sci 19(2):103-8, doi:10.1111/j.1467-9280.2008.02053.x. Errors potentiate
  defensive startle, and ERN magnitude predicts the potentiation: errors prime defensive motivation.
- Riesel, Weinberg, Endrass, Kathmann & Hajcak 2012, Psychophysiology 49(2):239-47,
  doi:10.1111/j.1469-8986.2011.01298.x. Punishing errors enlarges the ERN. The enlargement **persisted
  through an extinction phase** and was larger with trait anxiety. Directly relevant to the history
  dependence and to Prediction 3: reversal may be slow or context-bound.
- Meyer et al. 2015, J Abnorm Child Psychol 43(5):821-9, doi:10.1007/s10802-014-9918-1. Hostile or
  authoritarian parenting at ~3 years prospectively predicted a larger ERN at ~6 years, and the ERN
  mediated harsh parenting -> child anxiety. This is the closest human anchor for the developmental
  hypothesis. It is correlational and prospective, not a manipulation.
- Cole, Cibrian, Mirzadegan & Meyer 2022, Dev Psychobiol 64(7):e22318, doi:10.1002/dev.22318. Task
  punishment potentiated the ERN in children, more so with anxiety and with age.

**A tension to record honestly.** In these data the threat history changes the **amplitude of the early
error-monitoring response itself** (ERN, anterior cingulate). So in brains, the "routing" is at least
partly implemented as a GAIN change on an error-monitoring signal. That fits the thought's "routing, not
detection" framing only if the ERN is read as a salience/control readout (REE's dACC-analog, SD-032b /
MECH-258, which reads precision-weighted PE) rather than as the world-model mismatch content. MECH-590
is therefore worded so that the learned route may modulate the gain of the error's CONTROL/SALIENCE
readout, while the mismatch content consumed by world/self-model learning stays untouched. If a later
pull shows punishment history degrades the error signal that drives model correction itself, the
non-overwrite clause is a design requirement for REE, not a biological mirror. It should then be
re-labelled that way.

Not yet pulled (candidates for /lit-pull): fear-generalisation gradients (Lissek et al. 2008; Dunsmoor &
Paz 2015) for Prediction 4; extinction renewal and context specificity (Bouton 2004) for Prediction 3;
stressor controllability and the mPFC (Maier & Seligman 2016) for the "loss of control" pairing.
None of these is verified here.

## Next steps

1. **Literature pull before hardening** (`/lit-pull`, targeted review for MECH-590): confirm the four
   ERN papers above at full text, and add fear-generalisation, extinction-renewal and controllability
   anchors. The ERN amplitude-vs-content tension above is the specific question.
2. **V3 routing decision (/governance), not now.** The non-social core (MECH-590) is a plausible V3
   target, but only after the native waking trainer is live, which is the current front
   (`docs/CURRENT_FRONT.md`: "at REEConfig defaults ree_core does no waking gradient learning"). It also
   needs a learned error-consequence routing head that does not exist. Every PE-triggered control lever
   in ree_core today is fixed-sign, non-trainable arithmetic. See the feasibility verdict and the
   experiment sketch in `docs/architecture/learned_error_routing.md`. Do not queue before both gates
   clear.
3. **Welfare:** the threat-paired developmental arm is an aversive-contingency manipulation. Any future
   experiment falls under **SENT-2** (welfare budget: sustained negative-valence exposure,
   helplessness-like conditions) and needs welfare review before queueing.
4. **Registry hygiene (flag, not fixed here):** MECH-111's `location` points to a file that does not exist
   (`docs/architecture/approach_avoidance_symmetry.md`).
5. **Digestion:** the five predictions and their controls (sec 9-10) are ready material for a later
   `/thought-digestion` pass on MECH-590 (`what_would_answer`). Not drafted in this pass.
6. **Sibling governance rule:** GOV-FRONTIER-1 (registered the same day from `thought_intake_2026-09-24_experimental_learning_beyond_literature.md`) applies to MECH-590: its learning law has adjacent literature (ERN / punishment-history work) but no direct mechanism, so it is a frontier mechanism under that doctrine -- buildable default-OFF, with a RAISED experimental burden.
7. Raw thought marked `Status: processed` with this intake linked.
