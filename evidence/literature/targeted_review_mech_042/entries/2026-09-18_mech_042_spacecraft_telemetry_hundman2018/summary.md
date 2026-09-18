# Detecting spacecraft anomalies using LSTMs and nonparametric dynamic thresholding (Hundman et al., 2018)

## What the paper did

A JPL team built and deployed an anomaly-detection system over the telemetry channels of two real
missions -- the SMAP satellite and the Mars Science Laboratory rover, Curiosity. LSTMs predict each
channel forward; the prediction residual is thresholded by an unsupervised, nonparametric,
dynamically-recomputed scheme; and a set of false-positive mitigation strategies sits on top.
Evaluation is against expert-labelled anomaly ground truth from the missions themselves. The
stated motivation is operational: spacecraft return more telemetry than operations engineers can
watch, and the point of the system is to reduce monitoring burden and operational risk.

## Why it is here

MECH-042 proposes that REE expose low-bandwidth read-only channels reporting internal
control-plane state, for safety diagnostics, without adding decision pathways. It is worth
recording that this is not a speculative architecture. It is how safety-critical autonomous
systems are actually operated, and this paper is a well-cited, peer-reviewed instance of the
pattern working in production on hardware we cannot reach to repair.

That corroborates the architectural premise -- a telemetry surface is a legitimate safety
instrument for an autonomous system whose internal faults would otherwise only surface through
their consequences. It is the engineering counterpart to the clinical evidence in the Moorman
entry, and the two are independent in domain, which is most of why I wanted both.

## The two operational lessons I would carry into the experiment

The first is that **false positives, not misses, dominate**. The authors treat false-positive
mitigation as first-class design work, because a detector over a large channel fleet that alarms
too often is operationally useless however sensitive it is. MECH-042's telemetry detector faces
exactly this asymmetry: the claim names seven-odd channels -- `current_precision`,
`running_variance`, `is_committed` / `beta_elevated`, `e3_steps_per_tick`,
`CommitReadiness.get_state`, `SalienceCoordinator` operating mode, residue coverage -- and a
per-channel detector bank will alarm far more often than a single behaviour-stream detector on
harm or reward. If the multiple-comparison cost is not paid inside the threshold, the matched
false-alarm-rate requirement will quietly do it instead, by forcing the telemetry detector so
conservative that its lead time vanishes. That is a real way for sub-claim (2) to fail for a
reason that has nothing to do with whether the channels carry the information.

The second is that **static thresholds do not survive regime change**. The paper needed dynamic,
nonparametric thresholds because what counts as anomalous on a telemetry channel depends on the
operating regime. REE's channels have this property acutely: what counts as anomalous
`current_precision` early in a life is not what counts as anomalous late in one. A fixed
pre-registered threshold risks either missing the injected pathology or firing continuously
through the developmental ramp. MECH-042 wants pre-registration *and* regime-adaptivity, and those
pull against each other -- the resolution is presumably to pre-register the threshold *rule*
(calibrated on control runs) rather than the threshold value.

## The gap, which is the whole reason confidence is 0.68

This paper does not measure lead time of a telemetry detector against a behaviour-stream detector,
because a spacecraft has no behaviour stream in the relevant sense. Telemetry is essentially the
only observable there is. Sub-claim (2) is specifically a *comparative* claim, and this paper can
only speak to the viability of one of its two arms.

So it should be cited as evidence that the telemetry-detector arm is buildable and operationally
worthwhile. It is not evidence that the telemetry arm wins, and stretching it that way would be
the kind of move the Mormann entry in this same directory exists to warn against.

Lesser caveats: an LSTM predictive-residual detector is far heavier than the pre-registered
detector MECH-042 envisages, so none of the performance figures transfer. The anomalies are real
and exogenous rather than injected, and the ground-truth labelling is acknowledged incomplete --
which is worth noting as a place REE is genuinely better off, since injecting the pathology at a
known tick gives it exact ground truth the mission data never had. And "anomaly" here means
departure from learned nominal behaviour, a weaker target than identifying a specific named
control-plane fault.

## Confidence

0.68. Source quality 0.8, mapping fidelity 0.55 -- the binding constraint, because the
architectural pattern maps almost exactly while the comparative proposition is untested here --
and transfer risk 0.35.
