# Aston-Jones & Cohen 2005 -- adaptive gain theory of LC-NE (MECH-313)

According to PubMed, Aston-Jones & Cohen (2005), *An integrative theory of locus
coeruleus-norepinephrine function: adaptive gain and optimal performance*, Annu Rev Neurosci
([DOI](https://doi.org/10.1146/annurev.neuro.28.061604.135709)).

**What the paper says.** Reviewing monkey neurophysiology and accompanying models, the authors
propose that LC neurons operate in two modes. A **phasic** mode is driven by the outcome of
task-related decision processes and facilitates the ensuing behaviour -- this is exploitation. A
**tonic** mode emerges *when utility in the task wanes*, and is associated with disengagement
from the current task and a search for alternative behaviours -- this is exploration. Crucially,
LC receives direct input from anterior cingulate (ACC) and orbitofrontal (OFC) cortices, which
monitor task-related utility; these frontal areas are proposed to *produce* the phasic/tonic LC
patterns to optimise utility over short and long timescales.

**Why it matters for MECH-313.** MECH-313 (`stochastic_noise_floor`) names the LC-NE tonic
firing as its biological substrate but is currently registered as a **state-independent** noise
floor (a post-softmax max-entropy / temperature analog, SAC-style). The adaptive-gain theory is
the biological warrant that this state-independence is *incomplete*: the tonic exploration signal
is itself conditioned on, and modulated by, task utility. The exploration "floor" rises as
utility/certainty wanes and gives way to phasic exploitation as utility/certainty returns -- a
state-conditioned, self-annealing signal, not a fixed one. This is exactly the property the
CDQ-002 NoisyNet import proposes to add (learned, state-dependent, self-annealing parametric
noise). So the candidate refinement of MECH-313 is biology-anchored, not merely an engineering
convenience -- which is the discipline this lit-pull exists to enforce (the SD-003 / SD-010-011
"philosophy-right / mechanism-wrong" failure mode).

**Caveat and confidence.** The paper grounds state-conditioning at the systems/utility level
(ACC/OFC -> LC mode switching), one level of description above NoisyNet's per-parameter weight
noise; the "tonic-vs-phasic mode" to "learned per-parameter sigma" mapping is an analogy. It also
does not speak to the REE-side question the V3-EXQ-687 autopsy raised -- whether such a floor
*propagates* through to a committed/argmax action. I score it `supports` at 0.78: strong, canonical
source quality, moderate mapping fidelity (right phenomenon, different level of description),
moderate transfer risk (monkey systems neuroscience to the REE selection pathway). It supports the
state-conditioned *refinement* of MECH-313, and in doing so flags that MECH-313's current
state-independent framing is biologically under-specified.
