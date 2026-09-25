---
title: Plasticity Write-Authority Gating (admission side)
parent: "Control, Precision & Neuromodulation"
grandparent: Architecture
nav_order: 9
---

# Plasticity Write-Authority Gating (admission side)

**Status:** candidate-claim home doc. NOT a substrate-design memo, NOT a V3 critical-path item.
**Registered claims:** MECH-368, Q-062, MECH-431; plasticity-governance cluster (2026-09-25): ARC-151, ARC-152, MECH-592, MECH-593, ARC-153, ARC-154, Q-109 (all `candidate / substrate_conditional / implementation_phase:v4 / version_relevance:v4_v5`).
**Seed:** [thought_intake_2026-06-06_learning_onset_single_connection_gate.md](../../evidence/planning/thought_intake_2026-06-06_learning_onset_single_connection_gate.md)
→ raw: [docs/thoughts/2026-06-06_learning_onset_single_connection_gate.md](../thoughts/2026-06-06_learning_onset_single_connection_gate.md)
**Empirical anchor (compass only):** Schreiner, Brudner, Li, Pearson & Mooney, "A synaptic locus of song learning," *Nature* 2026, DOI 10.1038/s41586-026-10510-x — a cortico-basal-ganglia synapse class as the first-expression/maintenance locus of zebra-finch song learning. A genuine primary study but single-system/localisation in scope; it motivates the architecture, it does not supply citable mechanism evidence for any REE claim.

---

## The gap this addresses

REE built the **closure / protection** side of durable plasticity:

- **INV-074** — plasticity-crystallization necessity (universal invariant).
- **MECH-333 / MECH-334** — critical-period open-phase handling + closure with EWC write-protect of *already-written* weights (Kirkpatrick 2017 anchor).
- **ARC-075** — infant-curriculum plasticity-magnitude asymmetry.
- Design doc: [critical_period_crystallization.md](critical_period_crystallization.md).

REE never built the complementary **admission** side: *what earns durable write in the first place.* The channel-level decision exists — **MECH-261** mode-conditioned write gating decides which substrates can write per operating mode, and **MECH-094** gates by content provenance — but nothing gates **which individual events within an already-open write channel are licensed to durably deform the model**. If every prediction error in an open channel writes, that is the undifferentiated-global-update / catastrophic-interference failure mode.

### Why the episodic path doesn't already cover it

The four-state ladder from the raw thought (Observed → Flagged → Write-eligible → Consolidated) is mostly instantiated **for episodic memory**: salience/dopaminergic tagging (flag) → replay-buffer candidacy → **MECH-285** consolidation-priority by V_s residual (durable write at consolidation). On that path, "write-eligible" ≈ "tagged for replay," and admission is effectively handled.

The under-covered path is the **online world-model / policy weight-update** path (E1/E2 forward models, policy). There, the mode gate (MECH-261) opens the channel, but there is no explicit per-event admission gate. **MECH-368** is scoped to *that* path specifically, to avoid duplicating the episodic machinery.

---

## MECH-368 — event-level write-authority gate

A per-event transition `observed → write-eligible` over the durable model-update path, conditioned on:

```
write_eligible = f(prediction_error, salience, pathway_state,
                   residue_status, goal_relevance, plasticity_eligibility)
```

- **Distinct from MECH-261**: mode-grain channel gating vs event-grain admission within an open channel.
- **Distinct from MECH-094**: provenance/source gate vs admission gate.
- **Distinct from MECH-283**: that is the retrieval-side (recognition-for-recall) analogue of the same eligibility-before-use pattern.
- **Complementary to INV-074 / MECH-334**: admission (what gets written) vs protection (what stays written).

`depends_on`: MECH-261, MECH-094, INV-074, SD-032a, INV-034.

## Q-062 — is it needed?

The falsifier. Once a model-update substrate exists with an open online write channel: does per-event admission gating add anything over channel-gating (MECH-261) + provenance (MECH-094) + offline consolidation-priority (MECH-285)? If a substrate gating only the channel and prioritising only at consolidation still avoids catastrophic interference on the online path, MECH-368 earns no keep.

---

## Scope and the V3-vs-V4 boundary

V4-scoped because the `goal_relevance` input depends on a competitive z_goal (the GAP-4 goal-pipeline blocker — z_goal salience is not yet competitive in default V3 config; see `project_v3_v4_boundary`). `substrate_conditional`: promote/demote suppressed, kept out of the IGW experiment-proposal lane, off the V3/GAP-7 critical path. **Do not build in V3 until routed by experiment (Q-062).**

**Reduced form (possible earlier pull):** a goal-free variant gated on `prediction_error + salience + provenance + plasticity_eligibility` (dropping `goal_relevance`) sits only on already-implemented substrate (MECH-261, MECH-094, SD-032a). If a specific online-learning interference failure surfaces in V3, that reduced gate could be pulled forward as a targeted fix without waiting for the goal pipeline. Flagged here, not committed.

---

## <a id="mech-431"></a>MECH-431 — Two-factor (tag-and-capture) write-eligibility

Reaped from the autobiographical_memory_v4:ABM-9 biology /lit-pull (2026-06-13). Refines MECH-368's `plasticity_eligibility` term from a scalar instantaneous gate into the **eligibility-then-capture structure** the cellular and behavioural tagging literature describes. A local event sets a transient, input-specific eligibility **tag**; a durable model/policy write is consummated only if that tag **captures** a separately-gated plasticity/consolidation-resource signal within a time window. A tagged-eligible event can still fail to write if no capture signal arrives, and an arriving capture signal can rescue a recently-tagged weak event.

- depends_on: MECH-368, MECH-285 (candidate capture-resource signal = consolidation-priority by V_s residual), MECH-261 (gates the channel the tag lives in).
- Anchors: Ballarini et al 2009 *PNAS* (behavioural tagging — weak training yields LTM only if novelty supplies plasticity-related products within a window); Frey & Morris 1997 *Nature* (synaptic tagging and capture); Redondo & Morris 2011 *Nat Rev Neurosci*.
- Falsifier: if a single-stage eligibility test (no separate capture stage, no time window) prevents catastrophic interference on the online model-update path just as well, the two-factor structure earns no keep over MECH-368.

`status: candidate`, `epistemic_category: substrate_conditional`, `implementation_phase: v4`, `version_relevance: v4_v5`. Off the V3 critical path; do not build in V3 until routed by experiment.

---

---

## Plasticity-governance cluster (registered 2026-09-25)

Seeded by [thought_intake_2026-05-21_gated_plasticity.md](../../evidence/planning/thought_intake_2026-05-21_gated_plasticity.md)
and [thought_intake_2026-05-04_smoothened_da_ach.md](../../evidence/planning/thought_intake_2026-05-04_smoothened_da_ach.md),
registered after the biology gate was met 2026-09-19 (`evidence/literature/targeted_review_gated_plasticity_biology`).
Cites, does not restate: MECH-083 (ACh plasticity gain), INV-056 (selective neoteny), INV-074 (crystallization),
ARC-093 / MECH-398..400 / Q-072 (cortical plasticity-gain side), MECH-453 (TAN-pause window). The 2026-08-24 intake
already showed the signal -> eligibility -> permitted-update -> durable-commit cut is owned by this doc's claims plus
MECH-261 / MECH-094 / MECH-067; this cluster adds only what the literature pull surfaced.

Four wording decisions bind every claim below: gate **polarity is de-repression** (default blocked, fails closed --
Vanevski & Xu 2015); permission is binary-by-condition but **write magnitude is a gain with an interior optimum**
(Bolognani 2006); the striatal window is a **closed loop** (Kim 2019); and it is **not a learning-rate knob**
(Uribe-Cano & Kottmann 2026). All striatal evidence is dorsolateral-striatal motor/effort -- a procedural locus.

<a id="arc-151"></a>
### ARC-151 -- gate polarity: default-blocked (de-repression)

A teaching signal releases a write already staged at its target; it neither carries the content nor opens a window.
Specificity lives on the target. MECH-261 / MECH-368 / MECH-431 / MECH-453 are read with this polarity, so controller
faults fail closed. Folds the intake's signals-as-proposals and typed-controller candidates.

<a id="arc-152"></a>
### ARC-152 -- target-depth-graded release

Release requirement grows monotonically with target depth; extends INV-020 / MECH-064 / MECH-067 / ARC-020
stratification (actor, channel, phase) to ordinary experiential learning; generalises MECH-511's local-vs-deep E1
routing. The eight-rung ladder is illustrative. Grading must not become hardening (INV-056).

<a id="mech-592"></a>
### MECH-592 -- developmental operators reused under restriction

Adult reuse of a developmental operator is correct only as a de-repressed, target-restricted gain with an interior
optimum; unrestricted reuse impairs learning (Bolognani 2006). INV-056's retained plasticity = capacity under a gate.

<a id="mech-593"></a>
### MECH-593 -- refused deep writes are retained, not discarded

Real-provenance, ethically salient signals refused on depth grounds persist as unresolved records for offline
integration. Provenance-refused simulated content (MECH-094 / INV-011) leaves no record. Not a definition of residue.

<a id="arc-153"></a>
### ARC-153 -- ethics governs self-modification

Harm/residue signals (not an ethics module, INV-001) are inputs to deep-target release; runtime plasticity selection
is how INV-093's floor is held during learning. Injection routes stay with INV-020 / MECH-064; rollback with
MECH-392 / MECH-471.

<a id="arc-154"></a>
### ARC-154 -- E3 DA-ACh coordination layer

Separable from the DA signal, the cholinergic window (MECH-453) and the selector; sets their coupling, and so which
traces (MECH-452) are reinforced and how persistently. Interior-optimum setpoint trading acquisition against
effort/persistence recalibration. Absorbs the persist + calibrate residual of the five-way separation candidate.

<a id="q-109"></a>
### Q-109 -- is the TAN-pause window the tag that sleep captures?

Striatal procedural path only: is MECH-453's window the tag stage of MECH-431 tag-and-capture, captured offline via
MECH-322 / MECH-285, or independent of it? Window membership and value tags are confounded by the closed loop.

<a id="mech-453"></a>
### MECH-453 (cross-reference; optional re-home)

Owns the intake's striatal windowed-write candidate. Amended 2026-09-25 (closed loop; not a learning-rate knob;
contrast vs admission; release-vs-credit level shift). Registered 2026-06-23 from the V3-EXQ-700 thought.

Status of all entries: candidate / substrate_conditional / v4 / v4_v5. **DO NOT build in V3.**

## Relationship to the two adjacent notes (cross-reference, NOT conflation)

| Note | Grain | Question |
|---|---|---|
| [2026-06-01 plasticity-window-neuromodulators](../thoughts/2026-06-01_plasticity_window_neuromodulators.md) | **window / global state** (ACh/PV/BDNF learning-rate gain) | when is the system in a high-plasticity regime? |
| **This doc / MECH-368** | **event / local** | does *this* event earn durable write? |
| **ARC-152 (this doc, 2026-09-25)** | **target depth** | how much release does a write into *this* target require? |
| INV-074 / MECH-333 / MECH-334 closure side | **window closure** | when does plasticity crystallize / lock? |

A window-level plasticity gain can be open while a given event still fails the event-level admission gate, and vice versa. The three are sequential complements, not substitutes — do not merge them.

---

## Deliberately not registered

- **Harm-residue opening *write* authority without opening *action* authority** (posed against INV-011 / SD-010 / SD-011) — a sharp but separate axis; held pending an explicit decision.
- The ladder endpoints (Observed = perception/E1; Consolidated = sleep/replay MECH-273/275/285) — already owned; not re-registered.
