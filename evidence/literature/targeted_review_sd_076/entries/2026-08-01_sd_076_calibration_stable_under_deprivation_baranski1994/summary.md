# Baranski, Pigeau & Angus (1994) -- On the ability to self-monitor cognitive performance during sleep deprivation: a calibration study

**Why this paper.** This entry was commissioned by the GOV-FANOUT-1 H3 discrimination
(`failure_autopsy_V3-EXQ-794a_2026-07-31.json`) to answer a specific, narrow question the
autopsy itself flagged as missing: what is the *expected magnitude* of waking metacognitive
overconfidence drift, independent of the smoke-vs-full-loop discrepancy the autopsy already
resolved? Without that fact, there was no way to judge whether V3-EXQ-794a's tiny, sub-threshold
effect (a log-ratio swing of only ~0.02 between the LO and HI asymmetry doses) is itself
biologically plausible, or whether it is evidence that the asymmetric-EMA mechanism form is
simply wrong (H3, the driver's own pre-registered fallback).

**What the paper did.** Sixteen male participants performed sustained cognitive work over a
three-day period including a mental-arithmetic task: on each trial they reported a sum and then
rated their subjective confidence in that answer. This design is unusual among the sleep and
confidence literature in that it measures confidence in the participant's OWN response accuracy,
trial by trial -- not a belief about the external world, and not a global self-assessment. That
makes it, of everything found in this pull, the closest paradigm match to what SD-076 actually
claims: an asymmetric running estimate of one's own predictive accuracy.

**Key finding.** Raw performance (speed and accuracy of mental addition) deteriorated with
fatigue and recovered after one night of sleep, exactly as expected. But the metacognitive
measures -- calibration (the correlation between confidence and accuracy), resolution (the
ability to discriminate correct from incorrect answers), and the validity of subjective certainty
-- were **all statistically unaffected by sleep deprivation**. The authors' own conclusion is that
people retain fairly reliable internal feedback about their performance during sustained,
vigilant cognitive work, in the absence of external feedback from the environment.

**How this translates to REE.** SD-076 posits that a waking asymmetric-EMA process causes an
agent's precision/confidence estimate to inflate over a wake episode because good news about
one's own accuracy is incorporated faster than bad news. This paper, measuring exactly the
construct SD-076 encodes -- confidence about self-accuracy, not world-belief -- finds no such
drift under three days of extended wakefulness in a reasonably instrumented human sample. Read
plainly, that is *counter*-evidence to the premise that a large, easily measurable waking
confidence drift should exist at all. Read against V3-EXQ-794a specifically, it reframes the
autopsy's open question: the observed effect was small and sub-threshold, not large and
threshold-clearing. If the human calibration literature's best answer to "how much drift should
we expect" is "not much, and possibly none we can reliably detect," then a small effect is not
obviously an artifact of the wrong mechanism form (H3) -- it may be closer to the biologically
defensible magnitude than a large one would have been. This nudges the fanout question toward H1
(F1 damping) or H2 (exposure) rather than H3, without eliminating H3, exactly as the autopsy's own
smoke-comparison finding already did from a different angle.

**Limitations and honesty about the mapping.** This is a *deprivation* study, not a
*REM-recalibration* study -- it tells us that waking calibration holds up under sustained
wakefulness, but it says nothing about whether REM sleep specifically (as opposed to any recovery
sleep, or simply rest) is the mechanism holding it stable, so it cannot directly test MECH-204's
serotonergic-withdrawal claim. The sample is small (N=16), single-lab, and from 1994, restricted
to young males performing one narrow task; a null in this population and task does not prove a
null everywhere. And a failure to detect drift with this study's power is not the same as proving
drift is exactly zero -- it bounds the plausible magnitude from above, it does not pin it down.

**Confidence reasoning.** Mapping fidelity is unusually high for this claim (0.75) because the
measured construct is SD-076's actual construct rather than a proxy for it -- most literature on
optimism bias and belief updating (already covered elsewhere in this directory) measures
first-order world-beliefs, not second-order self-accuracy confidence. Source quality is moderate
(0.7): small sample, dated, single lab, but methodologically careful calibration/resolution
analysis purpose-built for this exact question. Transfer risk (0.35) reflects the domain gap
between a human mental-arithmetic task and an RL agent's running-variance estimate, which remains
real but is smaller here than for the world-belief papers. Aggregate confidence 0.68.
