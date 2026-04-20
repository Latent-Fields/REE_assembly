# Boyce et al. 2016 — REM theta is a causally separate gate from SWS consolidation

## What the paper did

Boyce and colleagues optogenetically silenced medial-septal GABAergic neurons in mice using ArchT expressed in Vgat-Cre lines. These neurons generate the hippocampal theta rhythm; silencing them attenuates theta without disturbing sleeping behaviour. Critically, the silencing was closed-loop and conditional on the current sleep stage: they silenced specifically during REM epochs in one condition, and specifically during non-REM (NREM or waking quiet) epochs in a second condition, each for matched durations and each within a critical window after learning. Memory was assessed via novel object-place recognition and contextual fear conditioning. REM-specific silencing abolished consolidation in both tasks; non-REM silencing had no measurable effect.

## Why this matters for MECH-261

MECH-261's dict-keyed write-gate registry assumes that operating modes are functionally dissociable channels — that the SWS write and the REM write are not variants of the same operation scaled differently, but different operations using different machinery. Boyce are the cleanest causal evidence for this. The temporal specificity is the crucial control: the same optogenetic silencing, same neurons, same duration, same task, same animal, only the sleep stage of delivery differing between conditions — and the outcome inverts from abolished consolidation to no effect. This cannot be explained by a shared carrier rhythm model.

In the REE abstraction this says: `write_gate("sd_033a" | REM_mode)` and `write_gate("sd_033a" | SWS_mode)` are not linked. Each mode opens a different set of channels, potentially with different default targets, and the gating substrates (theta generator for REM, thalamic reticular + cortical slow oscillator for SWS) do not overlap. The current SD-017 implementation treats SWS and REM as sequential passes with different functions (schema installation vs attribution replay); this is consistent with Boyce. What the Boyce result specifically adds for MECH-261 is a warrant for the default REM mode weights differing from the default SWS mode weights in the write-gate registry — not by coincidence but as the biological implementation of the separation.

The result also puts a constraint on REE's SD-017 REM pass: if the pass is gated by a mode scalar alone (a coordinator output) and does not have its own theta-analog clocking, it is a reduced model of the biology. The reduced model may still behave correctly in the current V3 experiments because the clock-free abstraction is sufficient for the metric targets; but a V4 implementation that wants to capture the Boyce causal structure should add a REM-mode internal rhythm that gates when the write is actually delivered, not merely whether the mode is active.

## Limitations

Boyce do not show target-specific routing — that is, they do not establish which cortical subdivision the REM-mode theta gates write preferentially into. The Maingret/Helfrich pair establishes subdivision selectivity for SWS; the equivalent REM experiment does not yet exist in a form cleanly translatable to SD-033 subdivisions. This is why the MECH-261 REM gate implementation currently routes writes to "residue replay" and "HC viability" rather than to a specific SD-033 subdivision — the biology supports a REM-specific gate but not a specific REM-mode cortical target.

The manipulation silences theta generally during REM; it does not dissociate forward versus reverse theta-phase replay (the Poe 2017 theme). For the REE implementation this finer structure is V4 scope.

## Confidence reasoning

Source quality very high (Science, optogenetic causal, rigorous within-state control). Mapping fidelity 0.75 — the mode-separability claim is tightly mapped; the target-selectivity question is not addressed. Transfer risk 0.25 because theta and medial-septal GABAergic generators are well-conserved and the rodent-to-human extrapolation is supported by parallel human literature on REM theta. Overall 0.80.
