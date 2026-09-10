# An abstract, multiply-read confidence signal in orbitofrontal cortex (Masset et al., 2020)

**Claim tested:** ARC-055 -- verisimilitude signal availability: V(t) and D_V must be explicitly available to E3 selection and influence E1/E2 learning updates.
**Direction:** supports | **Confidence:** 0.76

## What the paper did

Rats made two-alternative choices on the basis of either olfactory or auditory evidence, and expressed their confidence through how long they were willing to wait for a delayed reward. Single orbitofrontal neurons were recorded throughout. The design has a criterion built into it that most confidence studies do not: to count as supporting metacognition, the authors argue, a confidence representation must be *abstract* -- it must arise irrespective of the source of the information, and it must inform more than one confidence-guided behaviour. Modality was varied to test the first; two behavioural readouts were measured to test the second.

Both were confirmed. OFC neurons encoded statistical decision confidence independently of sensory modality, and their activity predicted trial-by-trial time investment *and* cross-trial choice strategy updating.

## How this translates to REE

This is the entry in this pull that comes closest to ARC-055's actual assertion, and the reason is that the paper independently arrived at nearly the same criterion. ARC-055 does not merely say a verisimilitude signal exists; it says it must be explicit rather than epiphenomenal, and the justification it gives is that several consumers -- E3 trajectory selection, E1 state representation, E2 transition modelling, learning update prioritisation -- must all read the same quantity. A signal that is genuinely shared in that way has a structural signature: invariance to what produced it, and more than one reader. That is exactly what "abstraction" names here, and it is what was measured.

The two consumers are the interesting part. Time investment is an immediate action-selection consumer. Cross-trial strategy updating is a learning-update consumer. They straddle the very division ARC-055 draws between the E3 leg and the E1/E2 leg, and they are shown to be fed by one representation rather than two. An architecture in which confidence were reconstructed separately by each consumer, or in which it were a by-product of the decision process visible only to that process, would not produce this result.

## Limitations and confidence reasoning

Three limits, and I want to be plain about the third because it is the one that most tempts over-reading.

First, the evidence is predictive, not causal. Neurons whose activity predicts two behaviours establish that the signal is *available* to both; they do not establish that either behaviour would fail without it. The causal half has to be imported, and the Lak et al. (2014) entry in this same directory supplies it -- while also complicating it considerably.

Second, decision confidence about a completed perceptual choice is a narrower quantity than a running verisimilitude of a whole world model. One could have an abstract per-decision confidence exactly like this one with no global V(t) anywhere in the system.

Third, and most importantly: there is no temporal-depth component in this paper at all. D_V is simply not addressed. ARC-055 is a conjunction -- V(t) *and* D_V must be explicitly available -- and this entry speaks to one conjunct. Cited as support for the claim as a whole it would overstate by half.

Source quality is 0.90: Cell, single-unit resolution, the modality control designed in rather than argued post hoc, two independent behavioural readouts. Mapping fidelity is 0.78, the highest in this pull, because the paper's own abstraction criterion is close to a restatement of ARC-055's explicitness requirement. Transfer risk is 0.35 for the rodent-to-architecture mapping, which is a mapping of computational role rather than of anatomy. The aggregate sits at 0.76, deliberately below the mapping-fidelity figure, held down by the missing D_V conjunct.
