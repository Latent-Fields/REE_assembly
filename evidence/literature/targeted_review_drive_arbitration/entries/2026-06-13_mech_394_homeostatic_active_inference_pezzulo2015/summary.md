# Active Inference, homeostatic regulation and adaptive behavioural control (Pezzulo, Rigoli & Friston 2015)

**Claim(s):** MECH-394 (multidrive arbitration policy) · cross-ref ARC-073 (play-to-real transition)
**Direction:** supports · **Confidence:** 0.68
**Source:** Pezzulo, Rigoli & Friston (2015), *Progress in Neurobiology* 134:17-35. According to PubMed, [DOI: 10.1016/j.pneurobio.2015.09.001](https://doi.org/10.1016/j.pneurobio.2015.09.001).

## What the paper did

This is a theoretical synthesis, not an experiment. Pezzulo, Rigoli, and Friston set out to connect two research streams that usually run in separate channels: Active Inference (the Bayesian, free-energy formulation of perception and action) and the associative-learning tradition that explains behaviour through multiple controllers -- Pavlovian, habitual, goal-directed. Their move is to recast those classical controllers not as mechanistically distinct boxes but as "successive hierarchical contextualisations" of one underlying sensorimotor inference. In doing so they generalise Active Inference to interoception and homeostasis, arguing that homeostatic and allostatic regulation is achieved by treating bodily set-points as *priors* -- and that "priors act as drives or goals to enslave action."

## Key findings relevant to the claim

Two ideas earn this paper its place against MECH-394. First, **drives are priors**. If each homeostatic need is a prior expectation about an interoceptive state, then a *drive* just is a prior with enough precision to recruit action toward fulfilling it. That immediately reframes the multidrive problem: several simultaneously-active drives are several priors competing for control of the behavioural output, and the competition is resolved by **precision-weighting** -- how confidently each prior is held. This is precisely the soft-competitive, non-winner-take-all mechanism MECH-394 posits, expressed in the vocabulary REE already uses elsewhere (precision-selection, soft-competitive disinhibition). Second, the **hierarchical-contextualisation** move grounds MECH-394's "over context" orchestration variable: context is what sets which drive-prior is currently most precise, so the same drive vector yields different winners in different situations. And the exploratory-versus-homeostatic balance that MECH-394's notes attribute (loosely) to "Pezzulo 2014" is articulated here as the trade-off between epistemic value (information gain) and pragmatic value (homeostatic fulfilment) -- the same trade-off ARC-073 operationalises as the play-to-real transition by competence saturation.

## How it translates to REE

For MECH-394 this is the formal scaffold rather than the data. It tells REE *what kind of object* an arbitration policy is: a precision-weighted competition among drive-priors, contextually re-weighted. It legitimises the central design commitment -- soft competition, not a fixed priority -- by deriving it from a normative principle (expected free-energy minimisation) rather than asserting it. It also ties the drives-and-motivation roadmap back to the goal pipeline: priors-as-drives is the same machinery that seeds z_goal, so the arbitration MECH-394 layers on top is continuous with goal seeding rather than a bolt-on.

## Limitations and caveats

The honest limit is that a framework is not a policy. The paper dissolves the boundaries between controllers and tells you competition happens by precision-weighting, but it does *not* pin down the specific arbitration rule MECH-394 must commit to -- soft-competitive disinhibition versus weighted blend versus winner-take-all. It under-determines exactly the decision the V4 work has to make. There is also a substrate precondition lurking: the soft competition the framework promises only emerges if the drive set-points are actually represented as priors with *calibrated* precision. If REE's substrate cannot hold homeostatic set-points that way, arbitration could collapse to whichever drive carries the largest raw error -- a single-axis winner, the very thing MECH-394 denies. Finally, a citation-hygiene note: the claim's "Pezzulo 2014" resolves to this 2015 *Progress in Neurobiology* review (and the broader Pezzulo homeostatic-active-inference program); the year drift is recorded so the registry reference is traceable.

## Confidence reasoning

Source quality is good but reflects review status, not primary data (0.80). Mapping fidelity is high on vocabulary alignment -- priors-as-drives, precision-weighted soft competition, context-as-precision-setter are almost a direct gloss of MECH-394 -- but the framework licenses the architecture without testing it, so I hold the aggregate at 0.68. Transfer risk is low: this is computational theory, intended to be substrate-general. Raises MECH-394's literature confidence only; the claim remains substrate_conditional V4 with exp_conf = 0.
