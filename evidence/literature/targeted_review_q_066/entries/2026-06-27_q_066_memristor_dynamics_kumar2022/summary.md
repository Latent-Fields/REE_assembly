# Dynamical memristors for higher-complexity neuromorphic computing (Kumar, Wang, Strachan, Yang & Lu, 2022)

**Claim under test:** Q-066 — can a candidate physical cognitive substrate (here, memristive media) instantiate REE's cognifold primitives (ARC-089) without losing auditability, stability, or hard safety boundaries? This entry speaks to the **instantiation** axis.

## Framing

Q-066 is explicitly POST-V5 and off the V3 critical path. No physical REE substrate exists to measure. Everything in this entry is device-physics *capability* literature mapped speculatively against REE's primitive list — a derivation against device specs, not a measurement of REE. That posture sets a low ceiling on mapping fidelity and a high floor on transfer risk regardless of how strong the source is.

## What the paper covers and the key finding

This Nature Reviews Materials review argues that memristors "naturally embody higher-order dynamics through their internal electrophysical processes," so a single device can functionally replace an elaborate digital circuit. It catalogues which dynamics arise *natively* from internal state variables: volatile versus non-volatile resistance state, short- and long-term plasticity, threshold/spiking and self-oscillation, chaos, and locally-active negative-differential-resistance behaviour. The relevant point for Q-066 is that much of the ARC-089 primitive list — persistent state, history-dependent deformation, multi-timescale dynamics, oscillatory propagation, attractor/threshold transitions — is presented as intrinsic device physics rather than something bolted on with surrounding circuitry. On the instantiation axis this is supportive: the medium plausibly *instantiates* rather than merely *approximates* these primitives.

## Mapping to REE and caveats

The mapping_caveat is decisive here. Demonstrating that a device exhibits oscillation, attractors, or plasticity in a benchmark crossbar is not a demonstration that REE's *specific* primitives survive in the medium — REE's simulated-action deformation and its offline-reintegration step have no tested analog in this review — nor that REE's hard safety gate is realisable. There is no physical REE substrate to check any of this against. I therefore log it **mixed** (leaning supports on instantiation only), with mapping_fidelity 0.3 and transfer_risk 0.85 despite source_quality 0.95.

The standing tension that recurs across the whole Q-066 pull begins here: the higher-order dynamics this review celebrates are emergent products of *stochastic* ionic/filamentary processes. "Native instantiation" and "uncontrolled variability/drift" are two faces of the same physics — which is precisely why the stability and auditability entries (Zhao 2020, Qin 2026) weaken the very clauses this one supports. The paper offers richer dynamics but no verification or hard-gating mechanism. Confidence 0.42.
