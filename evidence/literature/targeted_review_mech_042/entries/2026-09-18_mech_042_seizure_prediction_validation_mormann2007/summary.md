# Seizure prediction: the long and winding road (Mormann et al., 2007)

## What the paper did

This is a critical review, in *Brain*, of roughly three decades of work on predicting epileptic
seizures from continuous EEG. The problem it reviews is structurally the one MECH-042 sub-claim
(2) proposes to run: you have a continuous internal-state signal and a manifestation stream, and
you want to know whether a detector on the internal signal fires before the manifestation, by
enough margin to be useful.

The review's finding is that the field's early answer -- yes, reliably, with minutes of warning --
did not survive. Results reported through the 1990s were, in the authors' words, not reproduced by
more recent evaluations. What changed was not the algorithms but the evaluation: once detectors
were benchmarked against random predictors operating at the *same* false-prediction rate, once
thresholds were chosen out-of-sample, and once testing was done prospectively on long continuous
recordings rather than on selected preictal and interictal segments, most of the advantage
disappeared. The review catalogues the pitfalls and proposes validation guidelines.

Notably, the authors include the groups responsible for the optimistic early results. This is a
field publicly correcting itself, which is part of why I weight it.

## Why it belongs in the MECH-042 file

MECH-042's `what_would_answer` already contains the right instinct: *"Degenerate if the
behaviour-stream detector is given a looser threshold than the telemetry detector (match
false-alarm rates on control runs first)."* This paper is the external evidence that this
particular precaution is not fussiness. It is the difference between a real lead-time result and
thirty years of irreproducible ones -- because a detector's apparent lead time can nearly always
be bought by letting it alarm more often, and unless the two detectors are pinned to the same
false-alarm rate on control runs, that is exactly what the comparison silently measures.

The review supplies a guard set that REE should adopt more or less wholesale:

- benchmark against a chance/surrogate predictor at matched false-prediction rate;
- choose the detector threshold, channel set and any hyperparameter *out of sample*, before
  looking at the pathology runs;
- declare what counts as "onset" on the manifestation stream in advance, because moving that
  threshold moves the measured lead time without touching either detector;
- report consistency across the whole seed/pathology set, never best-of.

That last one deserves emphasis. A predictor that looks strong on a subset of patients or channels
can be at chance overall. MECH-042 already asks for sign-consistency across at least three seeds
and at least two pathology types; this review is the reason that requirement is load-bearing
rather than ceremonial.

## Where the analogy breaks, in both directions

I want to be careful not to over-apply the caution, because two disanalogies favour REE.

REE *injects* its pathology at a known tick. The ground-truth onset time is known exactly, which
removes one of the largest error sources the review identifies -- in seizure prediction, onset has
to be inferred from the same data that the detector reads, and the EEG-onset versus
clinical-onset choice moves the answer directly. REE also gets to run matched control seeds as
many times as it likes, so the false-alarm rate can be calibrated empirically rather than
estimated from scarce unrepeatable recordings.

One disanalogy cuts against REE, though, and it is the sharper of the two: the review's cohorts
are large relative to three seeds by two pathology types. A design that small is *more* exposed to
a lucky-subset result, not less. If anything, MECH-042's seed requirement is a floor that should
rise once the pilot shows the effect size.

And the review is from 2007. The field has since produced better-controlled positive results,
including implanted advisory-device trials. So the honest reading is "this is how the comparison
must be run", not "this comparison has been settled negatively". That is why this entry is
`mixed` rather than `weakens`: it does not say internal signals carry no pre-transition
information. It says the evidence to date had not been gathered in a way that could establish it.

## Confidence

0.78. High source quality (0.85) and unusually high mapping fidelity (0.8) -- what transfers here
is an evaluation protocol, and the two problems really are the same comparison. Transfer risk is
low (0.25) for the same reason: a warning about unmatched false-alarm rates is domain-independent.
The aggregate sits below source quality because the paper's substantive verdict is nearly two
decades old, while its methodological verdict is not.
