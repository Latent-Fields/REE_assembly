# Maingret et al. 2016 — Hippocampo-cortical coupling selects mPFC as the write target

## What the paper did

Maingret and colleagues trained rats on a spatial memory task specifically calibrated to engage encoding but not produce next-day recall under baseline conditions — a weakly-encoded memory. During post-training NREM sleep, they used closed-loop stimulation to reinforce the naturally occurring temporal coordination between three events: hippocampal sharp-wave ripples, cortical delta waves, and cortical spindles. Control animals received the same total number of stimulation pulses but timed to decouple these three events rather than reinforce their phase relationship. Recall on the next day was at chance in controls and well above chance in the reinforced group, and multi-site recordings showed a specific reorganisation of mPFC ensemble activity — not a general cortical effect.

## Why this matters for MECH-261

This is the tightest available causal evidence that the MECH-261 write gate is two things simultaneously: phase-selected on the carrier rhythms, and cortical-site-specific in its output. Latchoumane 2017 (companion entry) shows that the phase geometry of the SO-spindle-ripple triple is necessary for consolidation. Maingret shows that the phase-respecting geometry routes the consolidation signal preferentially to mPFC. This is exactly the abstraction MECH-261 asks for: an operating-mode signal that opens a particular target channel in the dict-keyed write registry. In REE the target is SD-033a, the lateral-PFC-analog; in the rodent work the target is mPFC, the rodent homologue of the cluster of prefrontal areas that SD-033a is meant to capture.

The practical implication for the implementation is that the biological substrate does not treat "lateral-PFC" as a generic destination that receives whatever the hippocampus sends. The destination is a function of the phase relationship between three carrier rhythms that individually correspond to the operating mode (slow oscillation = SWS mode), the thalamic licensing event (spindle), and the content (ripple-embedded replay). The REE abstraction is faithful to this when the SWS mode signal is elevated *and* the write gate for SD-033a is opened *and* the content offered is replay-flavoured; MECH-261 already captures the ordering via the coordinator's mode probabilities and the registry's per-mode weights. The biological addition this paper makes is that the phase relationship is the realisation of that conjunction, not a separate layer.

## Limitations

Maingret focus on rodent mPFC, not on the finer subdivisions of primate lateral PFC that SD-033a draws its functional specification from (rule representation, context-dependent gating, Rushworth's effort-value integration). The homology cost is small but real. The stimulation is delivered during natural NREM and shows that the phase geometry is sufficient to convert a failed consolidation into a successful one; it does not establish that MECH-261's *other* mode gates (REM, waking-quiet) follow the same structure. For REM evidence see the Boyce 2016 entry; for the waking-quiet case Tambini and Davachi 2019 (already in the prior targeted_review_systems_consolidation_waking_propagation pull) is the closest equivalent.

## Confidence reasoning

High source quality (Nature Neuroscience, closed-loop causal, behavioural readout on a task pre-calibrated to isolate the consolidation effect). High mapping fidelity because Maingret's primary finding is subdivision-selective — the cortical reorganisation happened in mPFC, not generically. Transfer risk moderate at 0.25 because the rodent-primate PFC homology is the main residual gap and is already documented in SD-033's design doc. Overall 0.82.
