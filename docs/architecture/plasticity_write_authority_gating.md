# Plasticity Write-Authority Gating (admission side)

**Status:** candidate-claim home doc. NOT a substrate-design memo, NOT a V3 critical-path item.
**Registered claims:** MECH-368, Q-062 (both `candidate / substrate_conditional / implementation_phase:v4 / version_relevance:v4_v5`).
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

## Relationship to the two adjacent notes (cross-reference, NOT conflation)

| Note | Grain | Question |
|---|---|---|
| [2026-06-01 plasticity-window-neuromodulators](../thoughts/2026-06-01_plasticity_window_neuromodulators.md) | **window / global state** (ACh/PV/BDNF learning-rate gain) | when is the system in a high-plasticity regime? |
| **This doc / MECH-368** | **event / local** | does *this* event earn durable write? |
| INV-074 / MECH-333 / MECH-334 closure side | **window closure** | when does plasticity crystallize / lock? |

A window-level plasticity gain can be open while a given event still fails the event-level admission gate, and vice versa. The three are sequential complements, not substitutes — do not merge them.

---

## Deliberately not registered

- **Harm-residue opening *write* authority without opening *action* authority** (posed against INV-011 / SD-010 / SD-011) — a sharp but separate axis; held pending an explicit decision.
- The ladder endpoints (Observed = perception/E1; Consolidated = sleep/replay MECH-273/275/285) — already owned; not re-registered.
