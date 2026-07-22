# Dynamical Similarity Analysis (Ostrow et al., 2023) -- Q-081

## What the paper did

DSA answers a question that had no good answer: how do you tell whether two recurrent networks
implement the same computation? The standard tools -- CKA, representational similarity analysis,
Procrustes -- compare the *geometry* of latent states. Ostrow et al.'s observation is that this
is the wrong level. In recurrent systems the computation lives in the dynamics, and two networks
running equivalent dynamics need not have equivalent geometry.

Their method builds a high-dimensional linear approximation of each system's dynamics using
data-driven Koopman/DMD techniques (including delay embedding, HAVOK-style, so nonlinear
behaviour is captured in a linear operator on an augmented space), then compares the two
operators using an extension of Procrustes analysis that accounts for how a vector field
transforms under an orthogonal change of basis. Four case studies show DSA distinguishing
conjugate from non-conjugate RNNs and identifying different learning rules without supervision,
in settings where the geometric measures cannot.

## Key findings relevant to Q-081

Search 6 asks whether systems with different representations can exhibit homologous dynamics,
and names conjugacy, manifold alignment and Koopman methods as the threads to pull. DSA is what
happens when someone pulls them, and it is the only item in this pull whose substrate is the same
kind of object REE is: artificial recurrent networks with latent states, not brains.

The load-bearing content is the negative claim, and it changes what the prospective REE run
should compute. If equivalent dynamics need not produce equivalent geometry, then a cross-stream
analysis built on correlation, CKA, or any geometric alignment between z_self, z_world, z_harm_a
and z_beta could report zero shared structure while homologous transition motifs were sitting
right there. That is Outcome A misread as Outcome C -- an integration gap declared where none
exists. Given that the streams have different dimensionalities (32, 32, 16, 64) and no shared
basis, geometric comparison between them is close to meaningless anyway; DSA says the meaningful
comparison is at the level of the dynamics operator.

The positive claim is that this comparison is actually computable from trajectories, which is
what a per-step recorder would produce. That is the good news for the recording run: the analysis
Q-081 wants exists, has an implementation, and was validated on objects of REE's kind.

## How this translates to REE

Adopt the level, not the pipeline unmodified. Three problems have to be solved first, and two of
them are REE's alone.

DSA supplies a similarity score and no null distribution. That is exactly the gap Q-081 is most
exposed at -- a bare DSA score between E1 and E3 traces is uninterpretable, and interpreting it
generously is how Outcome B gets recorded as Outcome A. The surrogate has to be built separately
(see the Lancaster et al. 2018 entry in this directory) and the score reported against it.

The validation setting is whole systems trained on the same task and compared. REE's streams are
not independent systems: E2 consumes E1's output, the beta gate reads across, the control plane
conditions several at once. Shared dynamics between causally coupled sub-streams may be direct
consequence of the wiring rather than emergent shared organisation. DSA cannot tell those apart,
and Q-081's Outcome B is precisely "coordinated only by explicitly wired gates". This is the
strongest argument for making the ablation series load-bearing rather than the similarity score:
what discriminates A from B is not the score's magnitude but whether it survives removing the
wiring.

And the multi-rate problem is untouched by the paper. E1 produces a sample every step, E3 one
every ten. Any joint analysis requires a resampling or embedding choice, and that choice is
itself a modelling decision that can create or destroy apparent similarity. There is no
off-the-shelf answer here; the run will have to make a choice, document it, and control for it.

## Limitations and caveats

It is a conference method paper validated on case studies rather than a settled technique, and
it is already contested: a 2026 follow-up (*Beyond DSA: Conjugacy-based Comparison of Dynamical
Systems*, arXiv:2607.04493) asks whether orthogonal alignment is necessary and sufficient for
topological comparison at all. So a DSA score should be read as evidence of dynamical similarity,
not as a conjugacy certificate. Delay-embedding dimension and DMD rank are free parameters and
the results depend on them.

No GOV-ANALOGY-1 issue arises for the method itself -- this is not a brain-to-REE analogy but a
technique developed for artificial recurrent networks, which is why its transfer risk is the
lowest in this pull. The caution is different in kind: adopting a method is not evidence, and a
well-chosen statistic returning a number is not a finding.

## Confidence

0.72, the highest here. Source quality 0.75 -- NeurIPS 2023, MIT, public code, but a method paper
with case-study validation and live methodological disagreement downstream. Mapping fidelity 0.80,
the highest in the pull, because the object it compares is the same kind of object as a REE
stream. Transfer risk 0.20: no species, modality or clinical transfer is involved at all.

Literature confidence 0.72; experimental confidence for Q-081 stays 0.0. This paper supplies a
tool, not a result. It tells us which statistic to compute and warns that the obvious one would
have given the wrong answer in the wrong direction.
