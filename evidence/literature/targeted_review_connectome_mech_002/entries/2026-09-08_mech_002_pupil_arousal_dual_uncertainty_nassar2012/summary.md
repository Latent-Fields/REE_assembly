# Nassar et al. (2012) -- Rational regulation of learning dynamics by pupil-linked arousal systems

**Claim tested:** MECH-002 (Precision control analogues shape cognitive regimes)
**Direction:** mixed | **Confidence:** 0.65

## What the paper did

Thirty subjects estimated the mean of a Gaussian process that occasionally, without warning, jumped
to a new value. A normative Bayesian model defines two quantities in such a task: *change-point
probability* -- how likely it is the process just shifted -- and *relative uncertainty* -- how
reliably recent data pin down the current state. Nassar and colleagues measured pupil diameter,
carefully excluding luminance effects, and asked whether either quantity was visible in it.

Both were, on different timescales. Brief evoked pupil changes tracked change-point probability.
Baseline pupil diameter tracked relative uncertainty, and also individual differences in how often
subjects expected the process to jump. Together the two metrics predicted how much a new
observation moved the subject's next estimate. Then, in a second experiment (N=29), they manipulated
pupil diameter directly -- unexpected auditory fixation cues, independent of both task structure and
luminance -- and the manipulation changed how much new data influenced belief.

I included this entry specifically as an adversarial test of MECH-002's design constraint, and it
did not resolve the way the claim would prefer.

## Findings relevant to MECH-002 -- the supporting half

MECH-002's constraint is that expected and unexpected uncertainty "are distinct control channels,
not a single precision scalar". The first half of that is exactly what this paper demonstrates in
humans: two normatively distinct uncertainty quantities are separately encoded, and each separately
predicts belief updating. A single scalar cannot do that. Yu and Dayan gave us the normative
argument for why two channels are necessary; this is the closest thing in the directory to a
measurement showing a brain actually maintaining both. That is real support, and it is support for
the part of MECH-002 that is architecturally load-bearing.

## Findings relevant to MECH-002 -- the complicating half

The trouble is where the two signals were found. MECH-002 follows Yu and Dayan in assigning
unexpected uncertainty to the noradrenergic channel and expected uncertainty to the cholinergic one.
Here, both quantities rode on pupil-linked arousal -- the canonical LC-NE proxy -- separated by
*timescale* (evoked versus tonic baseline) rather than by chemistry.

If that is the real factorisation, then REE has the right number of channels and the wrong carving.
Two independent `alpha` terms are not the same object as a phasic/tonic decomposition within one
gain system: the latter implies the channels share a carrier and therefore trade off against each
other, which two free parameters do not. This is the same worry raised in the Yu and Dayan entry --
that paper's own remark that ACh and NE interactions are "part-antagonistic, part-synergistic" --
arriving here from an empirical direction instead of a theoretical one. Two independent lines
converging on the same concern about the implementation is worth more attention than either alone.

The sharper problem is the causal manipulation. It produced an **inverted-U**, not a monotone
effect. Raising pupil diameter increased learning rate when baseline was low, and slightly
*decreased* it when baseline was already high. REE's precision terms multiply prediction error, so
raising `alpha_k` monotonically raises the influence of error on belief. In the high-baseline regime
the biological system does the opposite. That is the most directly falsifying observation anywhere
in this directory, and unlike most of what is here it is testable in substrate rather than only
arguable: drive a precision term across its range and check whether belief-update magnitude is
monotone in it. If REE's is and the brain's is not, we should know that explicitly rather than
inherit it as an unexamined difference.

## How to weigh this, honestly

The obvious rejoinder is that pupil is not a neuromodulator. It correlates with locus coeruleus
activity, but it is also driven by cholinergic activity and by superior colliculus. So "both signals
live in the NE system" is an over-reading; the defensible statement is "both signals live in
pupil-linked arousal, which is not chemically resolved." That matters a great deal here, because the
very question at issue is whether ACh and NE carry separable signals -- and a measure that cannot
distinguish them is poorly placed to adjudicate it. This is why the entry is scored mixed at 0.65
rather than as a strong weakening result. It raises the question properly; it does not settle it.

The task is also a simple one-dimensional inference problem with an explicit generative model,
several orders of abstraction below the settings where MECH-002's regimes -- confidence, alarm,
clarity, patience -- are supposed to become visible.

## Confidence reasoning

Source quality 0.85: Nature Neuroscience, adequate N in both arms, quantities defined in advance by
a normative model rather than fitted post hoc, and a real causal manipulation rather than correlation
alone. Mapping fidelity 0.70: the normative quantities map cleanly onto MECH-002's two uncertainties;
the loose joint is pupil-to-neuromodulator. Transfer risk 0.40: human data, but an indirect proxy and
a much simpler task than the target regimes.

Aggregate 0.65, direction mixed. Its value to governance is not the confirmation it supplies but the
two constraints it places on implementation: the channels may share a carrier, and the gain-to-update
relation may not be monotone. Both are cheaper to discover here than in substrate.
