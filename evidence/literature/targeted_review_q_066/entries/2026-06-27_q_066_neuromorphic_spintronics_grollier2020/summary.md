# Neuromorphic spintronics (Grollier, Querlioz, Camsari, Everschor-Sitte, Fukami & Stiles, 2020)

**Claim under test:** Q-066 — can spintronic-memristive media instantiate REE's cognifold primitives without losing auditability, stability, or hard safety boundaries? This entry speaks to the **instantiation** axis (strongly) and the **auditability** axis (negatively).

## Framing

As with the rest of the Q-066 pull, this is a POST-V5 derivation against device-physics specs, not a measurement of any REE substrate. Mapping fidelity is held low and transfer risk high accordingly.

## What the paper covers and the key finding

This Nature Electronics review is the definitive map of the spintronic substrate. It ties physical phenomena to neuromorphic primitives: magnetic tunnel junctions (MTJs) as non-volatile synapses/memory with retention without refresh; spin-torque nano-oscillators for oscillatory computing and coupled-oscillator synchronisation; superparamagnetic/stochastic MTJs that exploit thermal fluctuations for probabilistic computation and true random-number generation; domain walls and skyrmions as mobile state; and magnetisation configurations that settle into attractor states for pattern completion. On Q-066's instantiation axis this is arguably the strongest evidence of any candidate substrate: stochastic transition, oscillatory propagation, non-volatile persistent state, and attractor dynamics are all *native*.

## Why it cuts both ways

The same property that makes spintronics a strong instantiation candidate undercuts the auditability requirement. Spintronics explicitly *harnesses stochasticity as a computational resource* — p-bits, Bayesian/probabilistic inference, population coding. When stochastic switching is the compute mechanism, behaviour is intrinsically probabilistic: you get soft statistical tendencies, not deterministic externally-inspectable gates. And many implementations are reservoir-computing-based, where, as the review notes, the details of the network need not be known but significant post-processing is required — the opposite of the external inspectability REE's hard safety boundary demands.

## Mapping to REE and caveats

The mapping_caveat is that spintronic stochasticity "as a resource" is the inverse of what REE's hard safety boundary needs. A substrate that computes *via* thermal-noise switching cannot natively provide a deterministic simulated-vs-released action gate, and there is no physical REE substrate to test the gate against. Logged **mixed** — best-in-class instantiation evidence, but probabilistic-by-construction operation weakens hard auditability — with mapping_fidelity 0.3, transfer_risk 0.85, source_quality 0.95, confidence 0.42.
