# Thought: Failure autopsy needs explicit failure-location buckets

**Date:** 2026-08-09  
**Status:** thought intake / methodology proposal

Recent inspection of V3-EXQ-906 suggests that REE failure autopsy does not yet discriminate sharply enough between fundamentally different meanings of experimental failure.

At minimum, a failed experiment should consider four distinct failure locations:

1. **REE FAILED** — the tested capability or behaviour was afforded a fair test, the intended mechanism was functioning sufficiently to instantiate it, the measures were capable of detecting it, and the environment provided the necessary information/opportunity, but REE nevertheless failed to demonstrate the predicted competence.

2. **THE MECHANISM FAILED** — REE as a larger system should not be blamed because the specific mechanism under test did not instantiate, train, activate, propagate, or causally influence the relevant downstream behaviour as intended.

3. **THE MEASURES FAILED** — the phenomenon may have occurred, but the assay, metric, threshold, logging, instrumentation, aggregation, or analysis was incapable of detecting or discriminating it reliably.

4. **THE ENVIRONMENT FAILED** — the experimental ecology did not provide a valid opportunity for the predicted behaviour or competence to emerge. Examples include inadequate behavioural headroom, unreachable resources, unsafe spawning, premature termination, confounded incentives, or harm becoming effective before the agent has actionable perceptual access to its cause.

These categories need not always be mutually exclusive. An experiment may expose multiple failures, and uncertainty should remain explicit where localisation is impossible.

The distinction matters because each bucket implies a different successor:

- REE failure → investigate the organism/capability.
- Mechanism failure → repair, replace, or falsify the proposed mechanism.
- Measurement failure → redesign instrumentation or assay.
- Environment failure → redesign the ecology/task before drawing conclusions about REE or the mechanism.

V3-EXQ-906 provides a motivating example. Visual organism-level inspection exposed environmental-design problems that the existing automated failure-autopsy framing did not initially recognise. In particular, subsequent source inspection indicated that harm could begin substantially outside the hazard sensory window, meaning an apparent failure of adaptive avoidance could instead reflect an environment that did not provide actionable information before damage.

## Suggested action

Update the failure-autopsy skill/process so that every failed experiment explicitly performs failure-location triage across at least these four buckets before assigning interpretation or proposing a successor. Require evidence for and against each applicable bucket, permit mixed/uncertain classifications, and prevent an experiment from being described as evidence of **REE failure** unless mechanism, measurement, and environmental adequacy have been sufficiently established.

This may also provide a useful general framework for interpreting behavioural experiments: before asking whether REE demonstrated competence, establish that the mechanism instantiated, the measurement could see competence, and the environment afforded competence.
