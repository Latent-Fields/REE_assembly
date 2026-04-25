# Makino, Wang & McHugh 2024 — BLA-CA1 Theta Coupling and Fear Memory Age (MECH-074d)

**Source:** Makino Y, Wang Y, McHugh TJ. "Multi-regional control of amygdalar dynamics reliably reflects fear memory age." *Nature Communications* 15:10283. DOI: 10.1038/s41467-024-54273-3

## What the paper did

Makino et al. performed longitudinal multisite electrophysiological recordings from hippocampal CA1, BLA, and anterior cingulate cortex (ACC) in freely behaving mice during recent and remote contextual fear memory recall. Using LFP spectral analysis and machine learning classifiers (LightGBM and Transformer), they characterised how inter-regional oscillatory coupling changes with memory age. Key finding: remote fear memory recall is characterised by weaker but more *rhythmic* BLA gamma activity, which is distally entrained by CA1 theta oscillations. Classifiers trained on these three-region oscillatory features (primarily BLA gamma + CA1 theta) reliably distinguish remote from recent memory expression.

## Key findings relevant to MECH-074d

The central relevance to MECH-074d is the CA1 theta → BLA gamma entrainment relationship during fear memory recall. This shows that hippocampal CA1 activity has a direct modulatory influence on BLA gamma oscillations during fear-related processing, establishing the oscillatory substrate for a CA1 → BLA information channel. For MECH-074d, this suggests that the hippocampal representations active during a harm event (the CA1 patterns that would be the attribution target of MECH-074d's remap_signal) have a direct oscillatory communication pathway to BLA during the recall/reconsolidation window. The ACC contribution to BLA entrainment in remote memory is also relevant: SD-032a (SalienceCoordinator) involves ACC-like structure interactions, and its coupling to BLA during remote memory may reflect the evaluation of harm-PE in a broader circuit context.

## Translation to MECH-074d

MECH-074d requires BLAAnalog to receive information about which CA1 latent codes were active during harm (attribution step) before emitting remap_signal. The CA1 theta → BLA gamma entrainment documented by Makino et al. provides a plausible oscillatory mechanism for this: during the harm-PE window, CA1 theta sweeps across recently active place fields, and this sequence entrains BLA gamma activity, effectively transmitting the contextual map to BLA for attribution evaluation. This is indirect support — the paper is about recall, not about harm-PE-triggered remapping — but the circuit architecture is consistent.

## Limitations and caveats

The paper characterises oscillatory coupling during *recall* (passive memory expression), not during harm-PE-triggered remapping events. MECH-074d's remap_signal is a discrete event-driven signal, not an ongoing oscillatory entrainment state. The remote vs recent distinction in Makino et al. is about memory age (consolidation stage), not about PE amplitude; these are orthogonal variables. Whether BLA gamma entrainment by CA1 theta specifically increases on harm-PE spike trials (the MECH-074d trigger) is not testable from this dataset. Evidence is therefore indirect: supportive of the circuit substrate but not of the specific trigger mechanism.

## Confidence

0.62. High-quality Nat Commun multisite recording from the McHugh lab. Mapping fidelity limited because paper addresses oscillatory recall dynamics rather than acute harm-PE-triggered remapping. Supports circuit substrate, not trigger mechanism.
