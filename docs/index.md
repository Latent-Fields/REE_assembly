---
title: Home
nav_order: 1
---

# Reflective-Ethical Engine (REE)

REE is a cognitive architecture specification for agents that must act under uncertainty while affecting others.

The distinguishing requirement is **moral continuity**: an agent cannot discharge ethical responsibility by optimising it away. Even correct choices generate *moral residue* — persistent geometric cost that propagates forward and constrains future policy selection.

REE is not a moral rule engine. It does not assume ethical cost can be eliminated. It treats ethics as a structural constraint on the prediction-error minimisation loop, not as a separate module bolted on.

---

## Latest result — 2026-04-03

**EXQ-223 PASS: Minimal mind confirmed.**

The REE core loop — E1 (associative world model) + E2 (fast transition predictor) +
HippocampalModule (trajectory proposal) + go/no-go selection + raw harm/reward signals —
produces stable navigation, harm avoidance, and resource acquisition without deliberation,
goal evaluation, or commitment machinery. 3/3 criteria met across 3 independent seeds
(harm_ratio 0.29–0.39; REE reward ~4.5× random).

**The circuit topology of EXQ-223 matches the zebrafish larva (5–7 dpf) at the level of
named structures.** Dorsal pallium (E1) → cerebellum (E2) → lateral pallium (hippocampal
module) → optic tectum + reticulospinal neurons (go/no-go) → lateral habenula (harm
signal). The larva has no mature prefrontal cortex — no commitment architecture — which
is exactly what the ablation removes. This is the only vertebrate for which the entire
~100,000-neuron CNS has been functionally imaged during behaviour (Ahrens et al., 2013,
*Nature Methods*). The match was derived from functional-architecture arguments; it was not
built to fit the biology.

→ [Full analysis with circuit table and references](changelog.md#2026-04-03-exq-223-pass--minimal-mind-hypothesis-confirmed)

---

## Where to start

| Document | What it covers |
|----------|----------------|
| [Architecture overview](architecture/overview.md) | The three irreducible functions (persistence, reachability, commitment) and how E1/E2/E3 implement them |
| [Core invariants](invariants.md) | Non-negotiable architectural constraints with claim IDs |
| [Glossary](glossary.md) | Canonical terminology — start here if terms are unfamiliar |
| [Roadmap](roadmap.md) | Programme phases, phase-gate criteria, current status |
| [Failure modes](REE_failure_modes.md) | What the architecture is designed to prevent and why |

---

## Architecture

REE is organised into five computational components:

- **E1 (Deep Predictor)** — long-horizon recurrent context model; maintains world, self, and value across time
- **E2 (Fast Predictor)** — fast transition model `f(z_t, a_t) → z_{t+1}`; operates on the conceptual sensorium (z_gamma / z_world), not raw sensory streams
- **L-space (Fused Manifold)** — multi-depth latent state stratified by prediction horizon; z_self (motor-sensory, E2's domain) and z_world (causal footprint, residue, E3's domain)
- **E3 (Trajectory Selector)** — selects a coherent future trajectory by minimising reality cost, ethical cost, and residue curvature; includes hippocampal map, trajectory proposal, and commitment gating
- **Hippocampal Systems** — explicit multi-step rollouts and path memory; navigates residue-field terrain using E1 as associative prior

See the [architecture section](architecture/) for detailed per-component documentation.

---

## Claims and evidence

REE claims are typed (INV / ARC / MECH / Q / IMPL), registered with confidence scores, and governed through an experiment-evidence pipeline. Promotion and demotion decisions require experimental evidence from a real implementation substrate.

- [Claims index](claims/claim_index.md) — all registered claims with status and dependencies
- [Conflicts](conflicts/) — documented design tensions and their resolutions
- [Governance state](../evidence/GOVERNANCE_STATE.md) — promotion/demotion history

---

## Implementation substrates

| Substrate | Status | Role |
|-----------|--------|------|
| ree-v3 | Active development | Primary implementation target post-V2 hard stop |
| ree-v2 | Complete | Qualification lane; 15 experiments run (6 PASS / 7 FAIL) |
| ree-v1-minimal | Active (baseline) | Parity substrate |

The V2 experiment series triggered three hard-stop criteria, formalising the V3 transition. The core V3 design decisions are SD-004 (action objects as hippocampal map backbone), SD-005 (z_self/z_world latent split), and SD-006 (asynchronous multi-rate execution).

---

## Contribute compute

REE experiments run on donated GPU and CPU time. If you have a machine with spare capacity, you can contribute in a few minutes — no account needed to get started, everything is open source.

→ [Contribute compute](contribute.html)

---

## Philosophical foundations

REE's design is grounded in five axioms about the structure of ethical agency. See [five axioms](architecture/five_axioms_foundations.md) and the associated [unpublished Synthese paper](https://github.com/Latent-Fields/REE_assembly) for the formal argument.
