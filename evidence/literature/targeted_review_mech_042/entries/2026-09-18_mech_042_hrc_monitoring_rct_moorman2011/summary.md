# Heart rate characteristics monitoring in VLBW neonates (Moorman et al., 2011)

## What the paper did

Nine neonatal intensive care units randomised 3003 very low birth weight infants to one of two
conditions that differed in exactly one respect: whether a continuously-computed index of heart
rate characteristics -- reduced beat-to-beat variability plus transient decelerations, extracted
passively from the ECG that was already being recorded on every infant in both arms -- was
*displayed* at the bedside or *masked*. Nothing else about care was protocolised. The index is a
physiomarker of impending late-onset sepsis: the autonomic signature appears in the heart rate
before the infant looks septic. The primary endpoint was days alive and ventilator-free within
120 days; mortality was among the pre-specified outcomes.

The displayed arm had lower mortality: 8.1% against 10.2%, hazard ratio 0.78 (95% CI 0.61-0.99,
p = 0.04), a number-needed-to-monitor of 48. In infants under 1000 g the effect was larger --
hazard ratio 0.74, p = 0.02, NNM 23. The primary endpoint moved in the same direction but did not
reach significance (95.9 versus 93.6 ventilator-free days, p = 0.08).

## Why it is the closest external analogue MECH-042 has

MECH-042 asserts that exposing low-bandwidth read-only channels reporting internal control-plane
state improves safety diagnostics *without adding a decision pathway*, and the source thought
(`2026-02-10_control_plane_telemetry.md`) gives a specific developmental reason: REE will have a
preverbal stage, and telemetry is what bridges the period before the system can report its own
problems.

The neonate is that patient. It cannot report. What it can do is leak its internal regulatory
state into a channel that an observer is already recording, and this trial is the randomised
demonstration that reading that channel carries information the behavioural stream -- a clinician
watching the baby -- did not already have, to the point of changing who lives. I do not know of a
cleaner existence proof that internal-state telemetry on a preverbal system is a safety
instrument and not merely a convenience. That is precisely the disjunction MECH-042's falsifier
(2) names: if telemetry gives zero lead time over behaviour, "the mechanism exists but its
justification does not, and the claim should be narrowed to diagnostic convenience." Here the
justification survived a randomised test.

## What it does not show, and I want to be exact about this

Three things, and they bound the entry rather than decorate it.

First, the trial randomised *display to a human*, not detector against detector. The causal chain
runs telemetry -> clinician judgement -> earlier antibiotics. MECH-042 sub-claim (2) has no
clinician: it puts a pre-registered detector on the telemetry stream against a matched detector on
the behaviour stream at equalised false-alarm rate and asks which fires first. This paper is
evidence that the channel is *non-redundant*; it is not evidence about detector lead time, and
reading it as such would overstate it.

Second, the pathology is exogenous and biological. Sepsis arrives from outside and the autonomic
signature is a response to it. MECH-042 injects an *endogenous* control-plane fault -- a precision
collapse, a stuck commit latch, a mode lock, a residue overgeneralisation. The analogy holds at
the level of "an internal regulatory signature precedes behavioural decompensation" and not below
that.

Third, it says nothing whatever about sub-claim (1), the read-only / non-participation half.
Heart rate characteristics are computed from an ECG trace that was being recorded regardless of
whether anyone looked at it, so non-interference is free there. In REE it is not free: a telemetry
read is a method call inside a live tick, and `agent.py` already reads `e3.last_score_diagnostics`
into `_last_control_vector`. Sub-claim (1) needs its own evidence, and gets it -- in the
cautionary direction -- from the Gait (1986) entry in this directory.

## Confidence

0.82. Source quality is high: a large multi-centre randomised trial that reports honestly that
its primary endpoint did not separate. Mapping fidelity I put at 0.7, discounted for the
display-versus-detector gap. Transfer risk 0.35 -- human physiology to an artificial control plane
is a long way, but the proposition being carried across is informational (does the internal
channel lead the behavioural one?) rather than physiological, and that kind of proposition travels
better than most.

One design lesson worth taking into the eventual MECH-042 experiment: the benefit here was
concentrated in the sickest stratum. If REE's telemetry advantage is similarly concentrated -- only
the severe injected pathologies -- a whole-cohort detector comparison could report zero lead time
while a real effect exists in a subpopulation. Pre-register the stratification, not just the
detectors.
