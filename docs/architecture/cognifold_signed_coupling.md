---
title: Cognifold Signed Coupling (ARC-084 / MECH-363 / Q-058)
parent: "Roadmap & Planning (V4+)"
grandparent: Architecture
nav_order: 1
---

# Cognifold Signed Coupling (ARC-084 / MECH-363 / Q-058)

**Status:** candidate cluster, V4/V5, off the V3 critical path. Registered 2026-06-09 from the competitive-interactions thought intake.

**Source intake:** [evidence/planning/thought_intake_2026-06-06_competitive_interactions_cognifold_stability.md](../../evidence/planning/thought_intake_2026-06-06_competitive_interactions_cognifold_stability.md)
**Raw thought:** [docs/thoughts/2026-06-06_competitive_interactions_cognifold_stability.md](../thoughts/2026-06-06_competitive_interactions_cognifold_stability.md)
**Empirical anchor (verified):** Luppi, A. I. et al., "Competitive interactions shape mammalian brain network dynamics and computation." *Nature Neuroscience* **29**(4):915-933 (2026). DOI [10.1038/s41593-026-02205-3](https://www.nature.com/articles/s41593-026-02205-3).

> This is a **stub / compass anchor**, not a build spec. It exists to give the registered claims a `location:` target and to record the design questions. No V3 substrate work is licensed by this document. Promotion to a V4 design spec requires an explicit version decision and (per the biology-before-formal-definitions rule) a biology lit-pull on signed coupling first.

---

## The idea

A cognifold cannot be "everything positively coupled to everything". An all-positive routed-field model is unstable: every salient stream reinforces every other, producing runaway resonance, over-synchronisation, and loss of modular segregation. Luppi et al. show empirically (human / macaque / mouse whole-brain models) that combining **modular cooperative** interactions with **diffuse long-range competitive** interactions reproduces mammalian dynamics far better than cooperative-only models, and that competition raises synergy, hierarchy, and neuromorphic-computing performance.

The REE extraction is a structural one: **signed competitive coupling may be a necessary generative ingredient of stable cognifold dynamics** — not damage, not punishment, not synaptic inhibition, and not merely an error-correction afterthought.

## <a id="arc-084"></a>ARC-084 — Typed signed cognifold coupling

The cognifold represents inter-field coupling as a typed, signed edge:

```
cognifold_edge = {source, target, sign, gain, precision, gate, timescale, write_authority}
```

with three coupling modes:

1. **Cooperative** (sign > 0) — binding, coherent trajectory generation, shared context.
2. **Competitive** (sign < 0) — suppress incompatible trajectories, preserve boundaries, prevent runaway resonance, stop one field absorbing all others.
3. **Gated-decoupling** — temporarily isolate simulation, offline integration, or unsafe action candidates from release authority.

The genuinely-new element is the **`sign` as a first-class, explicit edge property** at the cognifold-field level — competition represented structurally, not left to emerge from selection softmaxes.

**V3 reality (containment-only — do NOT build a parallel signed-edge module):** REE already runs competition, but locally and implicitly:

| Coupling mode | Existing V3 instance |
|---|---|
| Competitive (local) | BG winner-take-all lateral inhibition + Cisek/Kalaska affordance-competition ([MECH-090](claims-map)); symmetric Go/NoGo dMSN/iMSN competitive model (ARC-030); top-k competitive selection into E3 (MECH-254) |
| Gated-decoupling | MECH-094 waking-only write gate; MECH-090 commitment latch; MECH-261 mode-conditioned write gating |
| Cooperative | latent binding, trajectory generation across E1/E2 |

This is structurally the same situation as the [attention = distributed precision-selection] map (ARC-005, MECH-251/254/255/259/261/347, SD-032a): **REE owns the pieces but lacks the explicit map.** ARC-084 is a unifying MAP / commitment, not a new module.

## <a id="mech-363"></a>MECH-363 — Diffuse long-range competition as a generative stability requirement

Stable, synergistic, hierarchical cognifold dynamics require signed competitive coupling — specifically **diffuse, long-range** competition between distant fields with **opposite profiles** — not merely local damping. Falsifiable in principle by a multi-field coupling ablation (cooperative-only vs cooperative+long-range-competitive on the same field set), but **substrate-gated**: V3 has no explicit multi-field signed-edge layer to ablate, so a probe today would be vacuous.

**Two NON-equivalent failure axes (do not conflate):**

- **(a) Runaway positive coupling / hypersync** — MECH-363's target. REE analogues: feedback entrapment, shared delusional coupling, over-stabilised attractor (MECH-076). Addressed by signed-coupling damping.
- **(b) Monostrategy / regime-collapse** — the *opposite* pole (too little apprehended structure, not too much coupling). Owned by MECH-309 / ARC-062 / ARC-063. Addressed by the rule-apprehension layer, **not** by competitive damping.

## <a id="q-058"></a>Q-058 — Explicit vs emergent competition, and the safety taxonomy

Which subsystems genuinely need an *explicit* signed competitive edge rather than the existing local softmax/WTA? And what are the safety differences between inhibition, competition, decommitment, and residue-based veto across waking action, simulation, and offline integration? Open design questions:

1. Which inter-field couplings need an explicit `sign` vs existing local softmax/WTA (MECH-090/ARC-030/MECH-254)?
2. Safety differences between inhibition, competition, decommitment (MECH-090/MECH-105), and residue-based veto (harm stream, SD-010/SD-011)?
3. How should competitive coupling differ across waking action vs simulation (MECH-094) vs offline integration (MECH-272/273 sleep cluster)?
4. Should the AI-cognitive-failure taxonomy be re-indexed by missing/misweighted competitive coupling? (Cross-repo: `Latent-Fields/ai-cognitive-failure-taxonomy`, not REE_assembly.)

---

## Cautions (carry forward verbatim)

- Competition **!=** synaptic inhibition (Luppi et al. say so explicitly).
- A competitive/negative edge is **not** intrinsically harmful, pathological, or ethically negative.
- Competition is **not** reward subtraction / punishment — it is a structural relation between active fields.
- The paper does **not** prove REE's architecture; it is corroborating compass, not evidence for a claim.
- **Do not** "add inhibition everywhere." The correct extraction is: *preserve signed competitive coupling as a possible constructive cognifold primitive.*
- **Do not** make this a V3 implementation target absent a specific failure or explicit version decision.

## Dependency wiring

- ARC-084 `depends_on` ARC-005 (control plane routes precision and modes).
- MECH-363 `depends_on` ARC-084, ARC-005.
- Q-058 `depends_on` ARC-084, MECH-363.

All three: `status: candidate`, `epistemic_category: substrate_conditional`, `implementation_phase: v4`, `version_relevance: v4_v5`. Whether to take them into V4 design work is a later, explicit decision.
