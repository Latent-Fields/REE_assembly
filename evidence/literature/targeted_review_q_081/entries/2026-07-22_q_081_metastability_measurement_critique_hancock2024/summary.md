# Metastability demystified (Hancock et al., 2024) -- Q-081, INV-091

## What the paper did

This is a consensus review, not a study. Eleven authors -- including Kelso, who originated
the coordination-dynamics account, alongside the whole-brain-modelling and information-theoretic
groups who have since built on it -- set out to fix a problem they name plainly: the neuroscience
literature uses metastability "heuristically, and sometimes inaccurately". The review separates
three things that get conflated: the physical system, its attractor landscape (a theoretical
construct), and the observable spatiotemporal patterns in data. It then walks the practical
signatures actually computed on empirical data -- standard deviation of the Kuramoto order
parameter (std-KOP), of the spectral radius of time-varying functional connectivity (std-SPECT),
of intrinsic ignition (std-IGNITE), and the mean variance of the leading eigenvector (mean-VAR)
-- and says what each can and cannot establish.

Metastability proper is defined against the alternatives: mono-stability, multi-stability, and
instability. What distinguishes it is that the landscape contains saddles -- regions that attract
in some directions and repel in others -- so the system "approaches successive saddle-like regions,
dwells near each for some time, and spontaneously escapes to visit another". Multi-stability, by
contrast, requires noise to kick the system between genuinely stable attractors. The two look
similar in data and are not the same thing.

## Key findings relevant to Q-081

The load-bearing content is negative, and it lands directly on the Outcome A / Outcome B
discrimination that Q-081 is built around.

Box 2's first misconception is that observing switching between distinct states with long
periods of stability suffices to infer metastability. It does not: within dynamical systems
theory "this is a necessary but not sufficient condition", because the same appearance is
"shared by both metastable and multi-stable systems". The review is equally direct about the
signatures themselves -- they "do not disambiguate metastable or multi-stable dynamics", and
"are not meant to be used as tests for deciding whether a system is metastable or not, but only
to assess the degree to which a given system displays specific necessary, but not sufficient
signatures". On std-KOP specifically: a high variance "could reflect either metastable or
multi-stable dynamics, or it could even reflect mere random fluctuations within the system".

Two further points bear on how a REE result would have to be reported. First, "normative values
are not available for the different signatures, and so the most common approach is to contrast
different groups or conditions against a reference". The field does not have an absolute number
either; it works in contrasts. Second, the review's own summary of the empirical literature is
that both increases and decreases in metastability signatures track cognitive and
neuropsychiatric impairment -- lower std-KOP in Alzheimer disease and with ageing, but *higher*
mean-VAR in early psychosis and chronic schizophrenia -- from which it concludes there "may be a
'sweet spot' for metastability in healthy brain functioning".

## How this translates to REE

That "sweet spot" is, as far as I can tell, the only independent external articulation of what
INV-091 asserts: that cross-stream similarity has a viable band, with fragmentation below it and
collapse above. It was arrived at from clinical neuroimaging, with no reference to REE, and it
has the same non-monotonic shape INV-091 predicts. That is worth something -- though it is worth
being clear that a non-monotonic *dose-response in a different substrate* is a reason to take the
hypothesis seriously, not a reason to believe it holds here.

For Q-081 the transfer is almost entirely methodological, and it is a warning. The telemetry
audit landed on 2026-07-22 established that this cluster needs a prospective per-step recording
run. This review constrains what that run's analysis may claim. The naive analysis -- cluster
each stream's per-step state, show the clusters recur, show the transitions are non-random --
is exactly the necessary-but-not-sufficient inference Box 2 forbids. Worse, in REE it is
structurally guaranteed to succeed: E1 updates every step, E2 every three, E3 every ten, so
recurrent configurations and non-random transitions follow from the clock alone. That is Outcome
B wearing Outcome A's clothes.

Two design consequences follow. The statistic must be reported as a contrast -- against a
rate-matched surrogate, and against ablation arms -- never as an absolute, because the field
that invented these measures has no normative values either. And the discriminating comparison
has to be something a rate-matched shuffle *destroys*, which rules out any statistic that is a
function of the update periods.

## Limitations and caveats

The hard limit is that every concrete signature reviewed is defined over oscillatory phase.
std-KOP is the variance of a Kuramoto order parameter over Hilbert-transformed regional signals;
std-SPECT and mean-VAR are eigen-decompositions of phase-difference connectivity matrices. REE's
streams are not oscillators and carry no phase, so none of these is portable. The raw thought is
explicit that the aim is abstract coupling principles and not imported oscillatory mechanisms,
and this entry should not be read as importing them by the back door. What transfers is the
inferential discipline, not the estimator.

There is also an asymmetry that cuts against REE rather than for it. The review's subject is a
physical system observed through noisy measurement, whose generating parameters are inaccessible.
REE's are in a config file. Where a neuroimaging study cannot easily construct the "structure
trivially implied by the configured rates" null, REE can construct it exactly -- which makes that
null obligatory here in a way it is not there. Being able to build the strongest null is good
news for the experiment and bad news for any result that skips it.

And GOV-ANALOGY-1: none of this is evidence about REE. A brain that balances integration against
segregation tells us the question is well-posed in at least one system. It tells us nothing about
whether REE's streams do anything of the kind.

## Confidence

0.62, and MIXED rather than supports. Source quality is as high as this literature offers (0.92):
Nature Reviews Neuroscience, and the author list spans the camps that disagree with each other,
which is what makes its negative conclusions hard to dismiss as one school's preference. Mapping
fidelity is 0.62 -- the concepts map well, the measurements not at all. Transfer risk 0.45,
moderate rather than high, because what is being transferred is a constraint on inference
(necessary vs sufficient; contrast vs absolute) rather than a technique, and constraints of that
kind survive substrate change better than estimators do.

The honest summary: this is the most useful single item in this pull, and most of its usefulness
is in telling us which analyses would have been worthless. Literature confidence 0.62;
experimental confidence for Q-081 and INV-091 remains 0.0, and nothing here moves it.
