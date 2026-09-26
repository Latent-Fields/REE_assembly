Status: processed
Intake: evidence/planning/thought_intake_2026-09-26_endogenous_operating_point_regulation_and_regime_coordination.md
Claims registered: ARC-155, ARC-156, Q-111

# Endogenous Operating-Point Regulation and Regime Coordination

**Date:** 2026-09-26  
**Status:** Thought intake — synthesis from confirmed failure autopsies and cross-model red-team review  
**Scope:** Architectural hypothesis, not implementation instruction

## Core observation

REE increasingly contains machinery capable of learning, prediction, action selection, threat response, freezing, safety veto, mode switching, plasticity, developmental exploration, memory revision and other forms of control.

The recent failure autopsies suggest that the next major deficit may not be another missing cognitive subsystem.

Instead, the emerging problem is that REE does not yet reliably regulate **when existing mechanisms should dominate, how strongly their signals should count, when a cognitive regime should terminate, or how several controllers should coexist without one accidentally nullifying the others**.

A useful provisional formulation is:

> REE may possess much of the machinery required for several cognitive regimes while lacking sufficiently endogenous regulation of the operating points, transitions and interactions that determine when the organism should become what.

This is not yet evidence for a central executive or monolithic controller. The observed failures are more consistent with a **distributed coordination problem** involving calibration, state transition, causal routing and arbitration.

## Why this hypothesis has become visible now

Earlier failures in REE could often be explained by missing or weak component machinery: inadequate representations, poor prediction, absent consumers, weak training, insufficient exploration, measurement artefacts or incomplete integration.

As these layers have become increasingly testable and separable, a different class of failure has become easier to see.

In several recent cases, a mechanism is implemented and locally functional, yet organism-level behaviour still fails because:

- its operating threshold no longer matches the scale of the learned signal;
- the cognitive regime prevents generation of the information required to leave that regime;
- another control pathway removes the behavioural degrees of freedom required for the mechanism to matter;
- or multiple control quantities are expressed on incompatible or unstable scales.

The question therefore shifts from:

> “What cognitive component is absent?”

toward:

> “What regulates the relative authority, operating scale and transitions of the components that already exist?”

## Cross-autopsy evidence

### 1. Freeze becomes a self-locking regime

The PAG freeze gate currently compares a fixed threshold with a harm-related representation whose magnitude increases substantially during training.

In the autopsied regime, the trained harm signal sits well above the freeze threshold from the beginning of the episode. Freeze therefore activates immediately and persists.

The important point is not simply that the threshold is badly calibrated.

The attempted release pathway is itself source-starved by the frozen state. Its candidate release evidence depends on events that are produced by continued interaction with the world. But complete freezing suppresses that interaction.

The system therefore has a circular failure:

**leave freeze when evidence changes → evidence cannot change because the organism is frozen.**

This suggests a more general requirement:

> A strong cognitive regime should not depend exclusively on consequences suppressed by that regime to determine whether the regime should terminate.

Some form of regime-independent or regime-surviving evidence pathway may therefore be required.

### 2. Control operating points are not invariant to learned signal scale

The mode-governance experiments show a related problem.

Signals such as dACC prediction error can grow far beyond fixed caps or saturation constants. A supposedly graded transformation can then reduce to little more than a gain change because the incoming signal lives almost entirely in the saturated region.

Conversely, the candidate effort signal can be orders of magnitude smaller than the E3 payoff scale and therefore becomes behaviourally irrelevant at its shipped operating point.

The common feature is that fixed numerical constants are being applied to learned quantities whose distributions change:

- across training;
- across individuals/seeds;
- across developmental stage;
- and possibly across cognitive state.

This suggests that some control variables may need to be defined relative to endogenous scale estimates rather than absolute raw magnitudes.

### 3. Locally valid controllers can become behaviourally irrelevant

The endogenous safety-veto machinery provides another useful example.

The veto can fire, remain quiet in an appropriate control condition, and reach action selection.

Yet if another control mechanism has already collapsed behaviour into a single executed action, the veto has no remaining behavioural freedom over which to operate.

Thus a mechanism can be:

- implemented;
- causally connected;
- locally responsive;
- and still irrelevant to organism-level behaviour.

This is not a simple missing-wire problem.

It indicates that REE needs to consider **interaction between controllers**, including which mechanism has causal precedence, whether one mechanism suppresses the evidence or action space required by another, and whether several controllers can operate simultaneously without destructive interference.

## Important negative evidence

Not all recent failures fit the dynamic-control hypothesis.

Some autopsies were better explained by:

- underpowered or improperly induced positive controls;
- stale or mismatched historical baselines;
- environment contamination;
- measurement criteria that could not discriminate the manipulation;
- or provenance defects.

This matters.

The emerging dynamic-control interpretation should therefore not be treated as a universal explanation for REE failure.

The convergence is strongest in the family involving:

- freeze and release;
- mode switching;
- signal gain and scaling;
- safety veto;
- effort/value control;
- and behavioural regime transitions.

That concentration makes the hypothesis more credible than a post-hoc explanation applied indiscriminately to every failed experiment.

## Three candidate hypotheses

### H1 — Adaptive control normalization

**Hypothesis:**  
Control signals whose scale changes through learning or context require endogenous normalization, calibration or other adaptive operating-point regulation.

**Candidate affected quantities include:**

- harm-related latent magnitude;
- prediction error;
- salience;
- effort;
- confidence/precision;
- uncertainty;
- threat;
- arbitration signals.

**Failure expected if absent:**

- permanent threshold crossing;
- permanently silent control channels;
- saturation;
- brittle seed dependence;
- development-dependent failure;
- controller dominance determined by arbitrary numerical scale rather than information content.

**Falsifier:**

If fixed raw operating points remain functionally stable across training, seeds and contexts, and adaptive normalization provides no improvement in regime stability or causal discrimination, this hypothesis is weakened.

### H2 — Regime-independent escape evidence

**Hypothesis:**  
Any strong regime that suppresses normal interaction or information gathering requires at least one endogenous source of evidence capable of causing its termination that is not itself eliminated by the regime.

Freeze is the clearest current example, but the principle may extend to:

- habitual dominance;
- attentional fixation;
- exploit-only states;
- defensive modes;
- suppressed plasticity;
- strong commitment;
- high-confidence attractors.

**Failure expected if absent:**

- self-locking states;
- perseveration;
- inability to recover from environmental change;
- inability to reopen exploration or plasticity;
- mono-strategy behaviour.

**Falsifier:**

If regimes can reliably terminate appropriately using only signals generated by the regime's own restricted behaviour, then an independent escape pathway is unnecessary.

### H3 — Distributed controller arbitration

**Hypothesis:**  
REE requires some mechanism by which simultaneously active control systems regulate their relative causal authority without one accidentally eliminating the behavioural or informational substrate needed by another.

This need not be a separate executive module.

It could emerge from:

- reciprocal inhibition;
- neuromodulatory gain;
- normalization;
- precision weighting;
- hysteresis;
- state-dependent routing;
- basal-ganglia-like gating;
- oscillatory or synchrony-dependent coupling;
- salience competition;
- multi-timescale control.

**Failure expected if absent:**

- freeze nullifying safety veto;
- habit nullifying deliberation;
- threat suppressing model repair;
- exploration preventing commitment;
- commitment preventing necessary exploration;
- multiple controllers firing correctly while behaviour remains pathological.

**Falsifier:**

If the existing controllers compose appropriately once their individual scales and inputs are corrected, then no additional arbitration principle is required.

## A related but distinct issue: signal validity

The effort-control autopsy exposes an additional principle:

> A live signal is not necessarily a valid signal.

A candidate effort quantity derived largely from harm-model error should not be rescued merely by multiplying it until it affects behaviour.

Control signals need meaningful provenance.

This issue intersects dynamic coordination but should remain conceptually separate. Scaling and arbitration cannot repair a control quantity whose semantics are wrong.

## Possible biological analogy

The biological brain does not appear to rely on one global executive scalar controlling all cognition.

Instead, dynamic regime regulation appears distributed across interacting systems involving, among other candidates:

- neuromodulatory gain;
- locus-coeruleus/noradrenergic state;
- acetylcholine;
- dopamine;
- serotonin;
- thalamocortical routing;
- basal-ganglia gating;
- salience systems;
- hippocampal mismatch and novelty;
- hypothalamic and brainstem state;
- precision regulation;
- oscillatory and synchrony-dependent coordination.

The relevant lesson for REE may therefore not be to construct a “controller”.

It may be to ensure that control signals are:

1. appropriately scaled;
2. causally mutually visible where required;
3. able to survive the regimes they regulate;
4. able to alter the relative influence of other systems;
5. and capable of producing reversible transitions rather than one-way locks.

Speculative mechanisms such as ephaptic or field-like coordination remain interesting but should not be invoked unless simpler distributed coordination mechanisms prove insufficient.

## Architectural implication

The emerging blind spot may be better described as:

> **Endogenous operating-point regulation and regime coordination**

rather than simply “dynamic control”.

REE may already contain many of the required control mechanisms.

What may be absent is the distributed machinery by which the organism:

- calibrates those mechanisms to its current internal scale;
- knows when a regime has ceased to be useful;
- preserves routes for evidence capable of ending that regime;
- and arbitrates among several controllers without destructive interference.

This predicts a distinctive class of failure:

> The correct machinery exists, but the organism does not autonomously create the conditions under which that machinery can be used appropriately.

## Experimental strategy

The next step should not be to build a general controller.

Instead, the three candidate hypotheses should be tested separately.

The highest-value immediate experiment is the freeze-lock confirmer because it can establish whether the current lock is indeed produced by the predicted interaction between trained signal magnitude, static threshold and absent release.

After that, minimal discriminating experiments should test:

1. whether normalization stabilizes control across training and seeds;
2. whether a movement-independent endogenous signal can terminate freeze appropriately;
3. whether independent controller recalibration is sufficient for composition, or whether explicit arbitration remains necessary.

Each experiment should preserve:

- endogenous information only;
- no oracle knowledge of the experimental condition;
- explicit ablations;
- behavioural consequences;
- and clear falsifiers.

## Relationship to the integrated organism experiment

This finding does not imply that full dynamic-control architecture must be completed before an integrated organism experiment.

However, an integrated experiment is difficult to interpret if the organism can be deterministically trapped by a static control threshold before its higher-level mechanisms have an opportunity to operate.

At minimum, known regime-locking artefacts should therefore be resolved or explicitly controlled before interpreting organism-level failure as evidence against E1/E2/E3 or the broader REE architecture.

A later integrated experiment may itself become the strongest test of the distributed-control hypothesis.

## Governance recommendation

Do not govern the proposition:

> “REE needs a dynamic controller.”

That claim is too broad and risks prematurely turning a useful metaphor into architecture.

Instead, govern the narrower candidate hypotheses independently:

- adaptive control normalization;
- regime-independent escape evidence;
- distributed controller arbitration.

Keep signal validity as a related but distinct concern.

Each should remain independently falsifiable.

## Provisional conclusion

REE's next major blind spot may not be another organ.

It may be the principle by which the organs already present continually regulate one another.

The strongest current evidence suggests that the organism still lacks robust endogenous answers to three questions:

> **How strong should this signal count right now?**

> **When should this regime end?**

> **What happens when two valid controllers want incompatible things?**

Those questions now arise from observed failures rather than architectural intuition alone.

The important next move is therefore not to design the answer in advance.

It is to make those questions experimentally unavoidable.
