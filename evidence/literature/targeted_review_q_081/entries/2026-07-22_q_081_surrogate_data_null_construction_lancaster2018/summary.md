# Surrogate data for hypothesis testing of physical systems (Lancaster et al., 2018) -- Q-081

## What the paper did

A sixty-page Physics Reports review of surrogate data testing: how to construct an ensemble of
signals that match your data in every respect except the property you are trying to detect, so
that a statistic exceeding its surrogate distribution means something. It covers the surrogate
families in use -- Fourier-transform based methods and their amplitude-adjusted and iterative
refinements, and beyond them surrogates for uncorrelated and correlated noise, for nonlinearity,
and for coupling and synchronisation between systems -- compares their performance on simulated
and experimental data, and ships a MATLAB toolbox.

The organising distinction is between typical realisations (generated from a fitted model) and
constrained realisations, which are "computed directly from the data, producing surrogates that
replicate all characteristics of the original data except the specific property being tested".
The reason the field converged on constrained realisations is stated plainly: for a test of
temporal structure you need surrogates that "maintain the same serial correlations, i.e. the same
autocorrelation function as the original data", otherwise significance is trivially achieved by
destroying something you never meant to test.

## Key findings relevant to Q-081

This is the entry that speaks most directly to the ask. The telemetry audit that landed on
2026-07-22 established that Q-081 cannot be tested retrospectively and needs a prospective
per-step recording run, which makes null construction the live question rather than a downstream
detail. Q-081's own non-degeneracy guard already says the cross-stream statistic must be computed
against a rate-matched shuffle control, and that a result which merely recovers the configured
update periods is Outcome B rather than a PASS. This review is the methodology for building that
control -- and it sharpens the requirement in a way the claim text does not yet capture.

The constrained-realisation principle says the surrogate must preserve everything except the
property under test. Applied to REE that means preserving each stream's update period, its
marginal distribution, *and its own autocorrelation*, while destroying only the relation between
streams. The "rate-matched shuffle" as currently written in the claim would preserve the first
and possibly the second. If it does not preserve within-stream temporal structure, then a
cross-stream statistic can clear it purely because each stream is individually smooth in time --
significance achieved by destroying something we never meant to test, which is the exact failure
mode the review was written to prevent. That is a small correction to Q-081's guard and worth
making before the run rather than after.

The second transferable constraint governs the choice of statistic itself. The whole apparatus
rests on the discriminating statistic being sensitive to the tested property and insensitive to
everything the surrogates preserve. For REE this rules out, a priori and without needing to run
anything, any statistic that is a function of the update rates -- which is a useful filter to
apply to candidate statistics while the recorder is still being designed.

## How this translates to REE

Concretely: the surrogate should be a block permutation applied within each stream's own tick
grid, preserving tick times and within-stream temporal correlation while breaking cross-stream
alignment; and it should be validated before use, by showing it kills a statistic known to be
artefactual (something computed purely from the update periods) while sparing one known to be
real (something injected deliberately). Surrogate ensembles are cheap in a simulation, unlike in
physiology where the data are what they are, so there is no excuse for skipping the validation
step.

The review's coupling and synchronisation surrogates are the relevant family rather than the
nonlinearity ones, because cross-stream organisation is a coupling-detection problem.

## Limitations and caveats

Two, and the first is the reason this is not scored higher. The review treats signals sampled on
a common regular grid. REE's streams are sampled at 1, 3 and 10 steps, and the unequal-rate case
is not covered -- so the rate-matched surrogate has to be designed for REE rather than looked up,
which is the step where an error would be easiest to make and hardest to notice.

The second is a limit on what surrogate testing can ever deliver here. It establishes that a
statistic exceeds a null. It does not establish that the statistic measures shared *organisation*
rather than direct wiring. Outcome B in Q-081's taxonomy is "streams are coordinated only by
explicitly wired gates", and wired coordination is real coordination -- it will clear any
surrogate test, correctly. Only the ablation series separates A from B. This is worth being
blunt about: a significant result against a well-built surrogate is necessary for Outcome A and
does not come close to sufficient.

No GOV-ANALOGY-1 exposure -- this is statistical methodology, not a claim about brains.

## Confidence

0.76, the second-highest in this pull, and for an unglamorous reason: it is the standard
reference for the exact thing the audit says the run needs. Source quality 0.88 (Physics Reports,
comparative evaluation across surrogate types, toolbox provided). Mapping fidelity 0.72, held
down only by the unequal-sampling gap. Transfer risk 0.20 -- methodology is substrate-neutral by
construction.

Literature confidence 0.76; experimental confidence for Q-081 remains 0.0. This is a paper about
how to avoid fooling ourselves, and it contains no evidence whatever about whether REE's streams
share organisation.
