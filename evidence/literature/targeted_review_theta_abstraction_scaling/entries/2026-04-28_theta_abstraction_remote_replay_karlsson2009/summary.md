# Karlsson & Frank 2009 — Awake replay of remote experiences in the hippocampus

According to PubMed: Karlsson & Frank. *Nat Neurosci* 12(7):913-918 (2009). [DOI 10.1038/nn.2344](https://doi.org/10.1038/nn.2344). PMID 19525943.

## What the paper did

The authors recorded from rat dorsal CA1 during awake behaviour on a multi-arm maze and during subsequent sleep, and asked a focused question: when awake replay happens, does it reactivate the *current* environment or can it reactivate *remote* (previously experienced, different environment) trajectories?

The result challenges the dichotomy that had dominated the field. Awake replay frequently reactivates stored representations from previous experiences in different environments, with these remote replays as common as local replays of the current environment. The remote replays were more robust when the rat had recently been in motion, suggesting that brief quiescent pauses during active behaviour (rather than extended rest periods) are the time when this content surfaces. Sleep replay does the same kind of remote-content reactivation, with quantitative but not qualitative differences from awake remote replay.

## Why this matters for REE's question

This paper directly informs the architectural distinction between waking and sleep theta function in REE's [MECH-272](ree-v3/ree_core/sleep/routing_gate.py) routing gate and [MECH-285](ree-v3/ree_core/sleep/replay_sampler.py) sleep replay sampler. The user's architectural intuition was that sleep theta would carry higher-abstraction content than waking theta. Karlsson & Frank 2009 partially weakens that reading.

The biology shows that *stored, non-current content reactivates in both waking and sleep*. The functional difference is not "sleep accesses the cognitive map; waking is locked to current experience" — that dichotomy is wrong. The actual difference is in context (sensory input present in waking, absent in sleep) and in oscillatory profile (theta in REM has different statistics than awake theta), not in whether stored content is accessed.

This has two implications for REE's substrate plan:

1. **The MECH-285 sleep replay sampler should have a waking analog.** Brief quiescent pauses during awake behaviour are when remote replay surfaces — REE's existing sampler is gated to the sleep cycle, but the biology says the same priority-weighted sampling should run during waking quiescent moments too. This may not require a new substrate; it may just require lifting the sleep-only gate on MECH-285 invocation.

2. **The waking-vs-sleep theta abstraction-content distinction the user proposed is more nuanced than "sleep = abstract, waking = concrete."** Both states access stored traces. The functional difference is in *which* traces are most likely to surface (sleep favours full compositional recombination; waking quiescence favours goal-relevant nearby traces) rather than in whether traces are accessed at all.

For the type-prototype lit-pull's verdict that waking learning is sufficient for some abstraction (Schapiro 2016), this paper provides convergent evidence — the cognitive-map-access machinery is on during waking, not gated to sleep. Sleep enhances rather than gates abstraction extraction.

## What it does NOT settle

The "remote experiences" in this paper are spatial trajectories from a previous physical environment — not abstract, type-level, or option-level remote content. Whether awake replay reactivates non-spatial stored traces is plausible but not directly demonstrated in this paper. Subsequent Frank-lab work has supported the extension into hierarchical-task content, but Karlsson 2009 itself stays in the spatial domain.

The paper does not support a clean qualitative waking-vs-sleep dissociation. It shows that stored content reactivates in both. Quantitative differences (replay rate, replay quality, gamma synchrony per Carr et al. 2012, separate entry in this review) are real but do not amount to "different content domains."

The architectural commitment that "sleep extracts type-prototypes from compositional replay" needs to be qualified: extraction happens in both states; sleep enhances it but is not the gating step.

## Confidence reasoning

I sit this at 0.84. Source quality 0.88 — *Nat Neurosci*, decisive single-unit methodology, well-replicated framework. Mapping fidelity 0.74 because the awake-vs-sleep replay reactivation finding maps onto MECH-272 / MECH-285 architecture but partially weakens the simple sleep-extracts-abstraction reading the user's architectural intuition implied. Transfer risk 0.30 because the "awake replay reactivates stored traces" finding is now well-replicated and the architectural extension to non-spatial remote content is supported by subsequent work.
