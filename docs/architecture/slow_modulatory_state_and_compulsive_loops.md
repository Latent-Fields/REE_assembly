# Slow Modulatory State and Compulsive Loops

**Status:** V4/V5 compass. Location anchor for the candidate claims reaped from the
[2026-06-06 neuroimmune-modulation / compulsive-loops thought intake](../../evidence/planning/thought_intake_2026-06-06_neuroimmune_modulation_compulsive_loops.md).
**Off the V3 critical path.** No substrate, no experiment in V3 until routed by an explicit version decision.

---

## Seed

A saved Neuroscience News item — *"Brain Immune Cells Drive Compulsive Behavior"*
([microglia-calcium-signaling-anxiety-ocd-30687](https://neurosciencenews.com/microglia-calcium-signaling-anxiety-ocd-30687/);
primary study Nagarajan et al., *Molecular Psychiatry*, 2026-04-13: Hoxb8 microglia intracellular Ca²⁺
signaling as a bidirectional optogenetic switch for anxiety/OCD-spectrum grooming) — prompted a single
REE-relevant architectural idea:

> Compulsive behaviour may be shaped by **slow background substrate-state modulators**, not only by fast
> cognitive beliefs, rewards, or action-selection loops. A loop can be hard to release because the *field
> is biased*, not because the goal is *valued*.

**Precision guardrail (carried on every claim below).** The paper's mechanism is a *fast / causal*
microglial Ca²⁺ switch, **not** a demonstrated slow tonic process. "Slow modulation" is the REE-side
abstraction the saved item prompted, not the paper's claim. Do **not** cite this study as evidence for
slowness, do **not** reduce OCD/compulsion to inflammation, and do **not** imply REE or AI systems have
immune cells — the analogue is *slow substrate-state modulation*, not biology.

---

## What REE already owns (and why these are not duplicates)

| Layer | Existing REE claims |
|---|---|
| Compulsion **mechanisms** | SD-034 (closure operator / right-moment release), MECH-268 (dACC PE-saturation, urgency accumulator), SD-045 (action-chunk runaway-chunking → OCD ritual, Graybiel 2008), ARC-071 (policy-composition slow accumulator), MECH-124 (consolidation-loop → option contraction) |
| Slow **neuromodulator** layer | SD-037 (orexin-analog broadcast gain modulator — closest existing "slow control-plane modulator"), SD-036 (GABA decay), MECH-186/187/188 (5-HT goal-pipeline gain) |
| Slow **physiological bias** on the harm stream | SD-048 (sensitisation-spike = inflammatory-sensitisation analog; fatigue-drift = allostatic-load analog) |
| Decommit / commitment / residue | ARC-016 (commitment threshold), MECH-342 (maintenance-time decommit), IMPL-005 (residue persistence as structural memory) |
| Psychiatric failure-axis | MECH-088 (four-plane taxonomy; the OCD/compulsion axis) |

REE therefore already runs the *mechanisms* of compulsion and *has* a slow modulator slot. The genuinely-new
content is **(a)** a value-INDEPENDENT route to loop stickiness — the existing slow modulators (SD-037) act
on `z_harm` / drive-seeding and the existing PE-saturation (MECH-268) is fast and within-loop, neither
carries explicit authority over the *decommit-friction / release* landscape; and **(b)** the observation
that compulsion is best described as a *composition* over the scattered terms, not any single scalar.

---

## Reaped claims (registered 2026-06-09, `candidate` / `substrate_conditional` / `implementation_phase: v4` / `version_relevance: v4_v5`)

### MECH-369 — Slow substrate-state modulator with authority over compulsive-loop stickiness {#mech-369}

A slowly-varying, broadly-projecting modulatory state biases the decommit-friction / commitment-threshold /
action-release landscape so loops become sticky or hard to release **independently of represented goal value
or fast prediction-error**. Distinct from MECH-268 (fast, within-loop), SD-037 (gain over `z_harm` /
drive-seeding, no release authority), and MECH-106 (value-driven threshold). Most naturally an *amendment*
extending the SD-037 slow-modulator cluster with a decommit-friction authority channel.
`depends_on`: SD-037, SD-036, MECH-268, SD-034, ARC-016, MECH-342, SD-048.

### MECH-370 — Composed compulsion-risk readout {#mech-370}

`compulsion_risk = f(loop_reinforcement, threat_salience, residue_persistence, decommit_friction,
slow_modulatory_state)` — a unification of quantities REE already represents separately
(loop_reinforcement ~ SD-045/ARC-071; threat_salience ~ harm stream/MECH-268; residue_persistence ~
IMPL-005; decommit_friction ~ ARC-016/MECH-342/SD-034; slow_modulatory_state ~ MECH-369/SD-037/SD-036).
Asserts the *composition* is the right level of description for compulsion, letting governance ask "is this
loop stuck because it is valued, or because the field is biased?".
`depends_on`: SD-045, ARC-071, MECH-268, IMPL-005, MECH-369, ARC-016, MECH-342.

### Q-063 — Modulator-trapped loop vs valued repeated goal {#q-063}

How does REE distinguish a high-value, legitimately-repeated goal from a slow-modulator-trapped compulsive
loop (release blocked by decommit-friction, not by value)? And can offline integration reduce stickiness
*without* eroding the non-erasable harm residue protected by INV-004/INV-006? `epistemic_category` set
`substrate_conditional` explicitly so `narrow_open_question` does not fire.
`depends_on`: MECH-369, MECH-370, ARC-016, SD-034.

---

## V3 vs V4 boundary

**Containment-only in V3.** The compulsion *mechanisms* (SD-034/MECH-268/SD-045/ARC-071) and the slow
*neuromodulator* layer (SD-036/SD-037) are already implemented; the SD-033 OCD-axis is governed by
[`sd033_governance_plan.md`](../../evidence/planning/sd033_governance_plan.md). Do **not** build a
value-independent stickiness modulator or a unified compulsion-risk readout in V3 — a probe would be
vacuous until the slow-modulator-class distinction is actually built. Promote/demote is suppressed by
`substrate_conditional`; these do not pressure V3 governance.

## Cross-repo (NOT claims.yaml)

The AI-cognitive-failure-taxonomy analogue — a *slow-modulator axis* beneath named failure modes
(context-window pressure, memory weighting, tool-retry pressure, unresolved alerts, resource constraints,
explicitly substrate-state and *not* biology) — belongs in `Latent-Fields/ai-cognitive-failure-taxonomy`,
tracked there, not here.
