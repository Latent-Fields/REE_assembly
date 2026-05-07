# Threshold Supervisor: Scattered Mechanisms Survey

Registered: 2026-05-07
Status: research-anchor survey supporting Q-041

## Purpose

REE has accumulated several adaptive-threshold and adaptive-baseline mechanisms,
each scoped to one substrate. The brain dynamically manages thresholds for
commitment, release, surprise, urgency, and pass/fail across multiple
timescales -- and this is a stability lever, not just a tuning knob. This
document inventories what is already adaptive in REE, the timescale each
operates on, and what a unified meta-level "threshold supervisor" would have
to add that is not already covered.

This is a registration anchor for Q-041. It is not a design doc. The
substrate question is what the experiments referenced from Q-041 are meant
to resolve.

## Existing scattered mechanisms

| Locus | Adaptive quantity | Update timescale | Read by | Notes |
|-------|-------------------|------------------|---------|-------|
| ARC-016 (E3 dynamic precision) | precision = f(running variance of E3 prediction error) | per-step EMA, ~10-100 steps | E3 score weighting; commit threshold via relative ratio | Internal to E3. Does not adapt cross-substrate thresholds. EXQ-018b PASS validated the variance-driven relative-threshold path; EXQ-396a/b and EXQ-454 reclassified non_contributory under the V_s-monostrategy substrate gap. |
| MECH-258 / SD-032b (dACC pe_cap, FIFO action history) | precision-weighted PE normaliser, recency action-history window | window = 8 actions (dacc_suppression_memory) | dACC bundle -> E3 score_bias | Partial volatility tracking. NOT a Behrens-2007-style explicit volatility estimator; the pe_cap is a fixed scale parameter, not learned. |
| SD-032c (AIC-analog interoceptive baseline EMA) | drive/fatigue baseline against which z_harm_a salience is computed | EMA, alpha set per AICConfig | aic_salience, harm_s_gain | Floats with z_harm_a -- urgency is computed against a moving baseline rather than a fixed threshold. Drive-dependent by construction. |
| SD-032d (PCC-analog stability scalar) | scalar in [0,1] from success EMA + drive_level + steps-since-last-offline | success_alpha=0.02 (~50-step half-life); offline_recency_window=500 | SalienceCoordinator effective_threshold | Modulates the SD-032a switch threshold. Ties offline cadence to threshold sensitivity. |
| SD-032e (pACC drive bias EMA) | bounded drive_bias added to SD-012 drive_level | alpha=0.002 (~347-step half-life) | GoalState, SalienceCoordinator, AIC, PCC, dACC bundle | Slowest of the cingulate cluster. The meaning of "drive=0.7" drifts under chronic load. Closest existing analogue to neuromodulator-setpoint chronic shift. |
| MECH-040 (safety baseline / volatility) | dual control channels (provisional, no genuine evidence) | unspecified | control_plane | Registered but never validated on real substrate. |
| MECH-204 (REM zero-point capture) | precision_at_rem_entry snapshot for sleep recalibration | per-sleep-bout | (capture-only; no writeback) | Captures the recalibration target but does not act on it. The sleep-side writeback is unimplemented -- this is the most obvious gap. |

Timescale spread is wide -- ~10 steps (ARC-016 EMA) up to ~350 steps (SD-032e
pACC drive bias) -- but no mechanism operates at the cross-substrate /
sleep-bout / multi-day timescale at which neuromodulator setpoints
recalibrate biologically.

## What is missing

A meta-level threshold supervisor would adapt pass/fail or commit/release
thresholds across substrates based on system-wide instability metrics.
Specifically:

1. **Cross-substrate volatility tracking.** Each adaptive locus above tracks
   variance internal to its own signal. Nothing aggregates across loci.
   A genuine volatility estimator (Behrens et al 2007, Nat Neurosci) would
   read multiple PE streams jointly and emit a system-level learning-rate
   signal that downstream thresholds consume.

2. **Sleep-mediated writeback.** MECH-204 captures a precision zero-point at
   REM entry but the writeback path that uses it to recalibrate waking
   thresholds is absent. The brain treats sleep as global recalibration
   (Tononi & Cirelli 2014, Neuron, SHY); REE captures the snapshot and
   discards it.

3. **Setpoint drift under chronic load.** SD-032e's pACC drive bias is the
   closest existing analogue but is scoped to a single substrate (drive_level
   write-back from z_harm_a). Chronic-stress 5-HT/DA setpoint shifts in
   biology recalibrate many downstream thresholds simultaneously
   (commit, release, surprise) -- REE has no joint mechanism.

4. **Coherence guarantee.** Independent EMAs at different timescales can
   drift into incoherent regimes (e.g., high pACC drive_bias with low PCC
   stability scalar). A supervisor would either enforce a coherence
   constraint or expose the divergence as an instability signal in its
   own right.

## Why this is a question, not a substrate

The natural temptation is to write this as a SD ("SD-NNN: threshold
supervisor module that reads all adaptive loci and emits joint
recalibration signals"). I have resisted that for two reasons:

- **Premature commitment.** Whether the supervisor is needed at all is an
  open empirical question. The scattered mechanisms may already produce
  coherent meta-stability under realistic load -- the V_s-monostrategy
  substrate gap currently masks the dependent behaviour, so we do not
  yet know.
- **V3-vs-V4 placement is genuinely uncertain.** The simplest threshold
  supervisor is a slow EMA of EMAs -- could land in V3. The full
  sleep-mediated writeback supervisor requires MECH-204 to act on its
  snapshot, which depends on the sleep substrate enrichment (MECH-285,
  MECH-286, INV-049 implementation). That is a V4 commitment.

Q-041 registers the question. If experimental evidence licenses a
substrate-level commitment, the cluster (SD + supporting MECH) follows.

## Anchor literature (registration-time, pre-lit-pull)

- Behrens et al. 2007. Learning the value of information in an uncertain world. Nat Neurosci 10:1214-1221. -- dACC tracks volatility and adjusts learning rate accordingly.
- Friston & Adams 2013 / Adams, Shipp & Friston 2013. Predictions not commands: active inference in the motor system. -- precision-weighted PE as the canonical adaptive-control variable.
- Tononi & Cirelli 2014. Sleep and the price of plasticity. Neuron 81:12-34. -- SHY: sleep as global synaptic recalibration. Bears directly on the MECH-204 writeback gap.

A targeted lit-pull on "adaptive learning rate dACC volatility" + "neuromodulator setpoint chronic stress recalibration" + "synaptic homeostasis SHY recalibration" is the natural Q-041 successor; staged here as a follow-on rather than gating the registration.

## Observable signature for a working supervisor

Under sustained drive_level=0.9 for ~1000 steps, an agent equipped with a
meta-level threshold supervisor should show coherent shift across
substrates -- effective commit threshold, effective beta-gate release
threshold, AIC switch threshold, dACC pe_cap normalisation should move
together along a single low-dimensional trajectory consistent with a
shared volatility/setpoint signal. Without a supervisor, the adaptive loci
move independently -- the trajectory is high-dimensional and substrate-
specific.

This is the signature the Q-041 diagnostic experiment proposal targets.
