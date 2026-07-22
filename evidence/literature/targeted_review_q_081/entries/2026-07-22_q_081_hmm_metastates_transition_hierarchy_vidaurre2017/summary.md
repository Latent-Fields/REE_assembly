# Brain network dynamics are hierarchically organized in time (Vidaurre et al., 2017) -- Q-081

## What the paper did

The authors fitted a hidden Markov model to resting-state fMRI from 820 Human Connectome Project
subjects, treating whole-brain activity as passing through a small repertoire of recurring
network states, each state defined as a graph of interacting regions. Having inferred the state
sequence, they asked what structure the transitions carry.

Two results. Transitions are non-random -- given the current state, some successors are far more
likely than others. And that sequencing is itself hierarchically organised: the states partition
into two "metastates", one comprising sensory and motor networks and the other higher-order
cognitive networks, with the brain tending to cycle within a metastate and cross between them
more rarely. The fraction of time a subject spends in each state and metastate turns out to be a
stable individual trait: consistent within subject, heritable, and correlated with cognitive
measures.

## Key findings relevant to Q-081

I include this for the method, not the neuroscience. Q-081's `what_would_answer` names
"recurrent-state / transition-matrix / cross-stream-lag analysis" as the falsifier shape, and
this is that analysis carried out at scale on real data, which is more instructive than any
methods paper about what it takes to make the result stick.

Three things port. The pipeline itself -- per-timepoint multivariate signal, discrete state
inference, transition probability matrix, test for structure in the matrix -- is precisely what
a per-step REE recorder would feed, and it is worth knowing it works on data far noisier than
REE's will be. The metastate result matters more than it first appears: it demonstrates that the
analysis can find organisation *above* the level of individual states, in how the transitions
themselves group. That is the right level of description for "homologous transition motifs across
streams", which is otherwise a phrase without an estimator behind it.

The third is the validation strategy, and it is the part most worth copying. What makes the
states credible is not any property of the state sequence. It is that occupancy is
subject-consistent, heritable, and predicts cognitive traits -- the states were anchored to
something outside the trace. Any statistic inferred by an unsupervised model over its own data
will look structured; what stops that being circular is an external hook.

## How this translates to REE

The pipeline transfers. The null does not, and this is the sharpest caveat in the pull.

Vidaurre et al.'s discriminating test is that transitions are non-random. In resting fMRI that is
a real finding, because no one set the transition rates -- whatever structure appears is the
brain's. In REE the update periods are in the config: E1 every step, E2 every three, E3 every
ten. Non-random transition structure follows from the scheduler, before any learning has
happened, before the streams have interacted at all. A REE analysis that reused this null would
return a PASS with certainty and would have measured the config file. That is Q-081's Outcome B
recorded as Outcome A -- and Q-081's own text already names the rate-matched shuffle control as
non-optional for exactly this reason. This paper is the concrete illustration of why.

The external-anchor lesson transfers with more force than the pipeline does. REE has no
heritability and no cognitive traits to correlate against. Its available anchor is the ablation
series INV-091's falsifier already specifies: remove event broadcasts, remove mode conditioning,
force lockstep, randomise the rates, and require the cross-stream statistic to *move*. A
statistic that survives every ablation unchanged was measuring the scheduler.

## Limitations and caveats

HMM results depend on the chosen number of states; the method will not choose K for you, and an
unfortunate K can create or hide apparent hierarchy. Resting-state fMRI is slow, indirect and
haemodynamically smeared -- REE's telemetry is none of those, which mostly helps, but it means
the noise regime the method was tuned for is not REE's.

The deeper structural mismatch: fMRI regions are homogeneous measurements of one substrate at one
sampling rate. REE's streams differ in dimensionality (z_self and z_world at 32, z_harm_a at 16,
z_beta at 64), in semantics, and in update rate. The HMM here never confronts the multi-rate
alignment problem, so it says nothing about how to build a joint state space across streams
ticking at 1, 3 and 10 -- which is the first design decision REE's run has to make, and one this
literature leaves open.

GOV-ANALOGY-1: analogy only. That the brain has metastates is not evidence that REE does.

## Confidence

0.63. Source quality 0.88 -- PNAS, n=820, from the group that maintains the HMM tooling, with
heritability and trait-prediction giving it external anchoring that most dynamic functional
connectivity work lacks. Mapping fidelity 0.66: the method maps well and the substrate loosely.
Transfer risk 0.45, sitting almost entirely in the null-model mismatch -- which is identified,
understood, and correctable rather than lurking.

Literature confidence 0.63; experimental confidence for Q-081 remains 0.0. Nothing here is
evidence that REE's streams share organisation. It is evidence about how one would find out, and
a specific warning about the way that analysis would most easily fool us.
