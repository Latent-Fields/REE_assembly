# Reliability of analog resistive switching memory for neuromorphic computing (Zhao, Gao, Tang, Qian & Wu, 2020)

**Claim under test:** Q-066 — can a candidate physical substrate scale without losing *stability*? This entry is the central weakening evidence on the **stability** axis.

## Framing

POST-V5 derivation; no physical REE substrate exists. The reliability data here are measured on memory crossbars for DNN inference, not on REE, so the transfer to REE's abstract stability/safety invariants is speculative even though the underlying device measurements are real.

## What the paper covers and the key finding

This Applied Physics Reviews paper is a comprehensive reliability review of analog RRAM/memristors for neuromorphic use, and it names the bottleneck plainly: reliability — endurance and retention degradation, read/write noise and disturbance. It catalogues the stability-threatening non-idealities: cycle-to-cycle (C2C) and device-to-device (D2D) conductance variability, conductance drift and relaxation over time, retention loss, finite endurance, random telegraph noise (RTN), and a limited number of stable distinguishable conductance states (the broader analog in-memory literature typically reports only ~4–6 bits of effective precision). Crucially, these are framed as intrinsic to the stochastic set/reset filament physics — *mitigable* via write-verify, closed-loop programming, and multi-device redundancy, but not *eliminable*.

## Mapping to REE

For Q-066 this directly weakens the "scales without losing stability" clause. The substrate's persistent state is not a clean latch: it drifts and fluctuates stochastically, so any hard threshold encoded in conductance is a moving target. A value written as a hard safety boundary at write-time will have moved by read-time, and the available mitigations are statistical, never a hard guarantee — so a deterministic, externally-checkable threshold cannot be assumed without continuous re-verification overhead.

## Caveats and confidence

The mapping_caveat is that drift and variability measured on DNN-inference crossbars do not, by themselves, prove that REE's *specific* stability and safety invariants would break — they only remove the comfortable assumption that "persistent state" means "stable, auditable state." That assumption is exactly what a physical-cognifold proposal would have to defend, and this review shows it cannot be taken for granted. Logged **weakens**, source_quality 0.9, mapping_fidelity 0.3, transfer_risk 0.85, confidence 0.45. Together with the spintronics review this completes the standing Q-066 tension: the same analog internal-state physics that genuinely instantiates the cognitive primitives is the direct source of the stability failure documented here.
