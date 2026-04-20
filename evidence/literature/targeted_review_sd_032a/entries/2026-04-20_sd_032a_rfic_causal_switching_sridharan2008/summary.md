# Sridharan, Levitin & Menon 2008 -- rFIC causal role in CEN/DMN switching

## What the paper did

Three fMRI experiments in healthy adults: (i) an auditory event-segmentation task, (ii) a visual attention oddball task, and (iii) task-free resting state. The authors asked whether there is a network that *causes* the transition between the central-executive network (CEN, the canonical task-positive frontoparietal system) and the default-mode network (DMN, the task-negative internal system). They used chronometric analysis of activation onset latencies and Granger causality on the BOLD time series to infer directionality.

The result: the right fronto-insular cortex (rFIC, anterior insula) together with the dorsal anterior cingulate cortex forms a third network -- the salience network -- whose activation precedes and Granger-causes transitions in both CEN and DMN. The rFIC is the strongest causal node. The finding replicated across all three paradigms, meaning the switching role is not task-specific.

## Why this matters for SD-032a

SD-032a specifies a salience-network coordinator that aggregates dACC PE bundle + drive_level + offline-state into an `operating_mode` soft probability vector and a discrete `mode_switch_trigger`. The architectural intuition is that modes are reconfigured by a dedicated coordinator, not by each subdivision acting independently. Sridharan's data is the cleanest biological license for that intuition: the AIC+dACC aggregate is causally *upstream* of the networks it switches, rather than being a readout of them. That directionality is exactly what SD-032a asserts when it says the coordinator "reads all subdivisions' signals" and emits the mode vector + trigger.

The mapping into ree-v3 is reasonably direct. SalienceCoordinator.tick() reads the dACC bundle (analogue of the dACC node in Sridharan's salience network), drive_level (interoceptive contribution -- extending the Sridharan framing via Craig 2009), and the offline-mode flag (proxy for PCC stability, SD-032d). It emits the softmax-weighted operating_mode vector and the MECH-259 threshold-crossing trigger. The implementation choice to make the coordinator produce a discrete mode at threshold crossing -- rather than a purely graded modulation -- is an ree-v3 design decision, and Sridharan does not test it directly; the biological BOLD signal varies continuously. The validation experiment V3-EXQ-446 is what actually tests whether the discrete-switch framing survives empirically.

## Limitations and caveats

Two non-trivial caveats. First, Sridharan's Granger causality analysis rests on BOLD time-series inference, which is indirect evidence of neural directionality -- haemodynamic lag can distort Granger estimates. The replication by Goulden 2014 using DCM on ICA time courses addresses this criticism and is why I have also included that paper in this pull. Second, Sridharan identifies rFIC specifically (right-lateralised), whereas ree-v3's SalienceCoordinator is not lateralised. This is a faithful simplification for a computational substrate -- the lateralisation in humans is a biological fact but not obviously a functional constraint on the aggregation architecture.

The four-mode discretisation (external_task, internal_planning, internal_replay, offline_consolidation) is ree-v3's extension beyond Sridharan's two-network frame. Internal_replay and offline_consolidation do not map cleanly onto CEN/DMN; they require additional biological grounding from Carr/Jadhav/Frank 2011 and Tambini & Davachi 2019, which live in the parent SD-032 directory and are referenced there under the MECH-261 write-gating profile.

## Confidence reasoning

I assigned 0.85 rather than higher because the paper robustly licenses the architectural role of AIC+dACC as a causal switching coordinator (strong source quality, replicated, foundational) but does not directly test the four-mode extension or the discrete-switch vs graded-modulation choice. Mapping fidelity is 0.80: the switcher-coordinator role transfers cleanly, the mode granularity does not. Transfer risk is low-moderate: this is a human fMRI study, so the architectural mapping is plausible but the biological timescale (BOLD, seconds) is orders of magnitude slower than ree-v3 action ticks -- a consideration for anyone tempted to read specific cycle-count predictions from the biology.

The honest summary: Sridharan licenses "salience aggregate is causally upstream of mode switching" as an architectural principle. It does not license the specific four-mode vector, the softmax aggregation rule, or the hysteresis-based trigger. Those are implementation choices that V3-EXQ-446 must validate on their own merits.
