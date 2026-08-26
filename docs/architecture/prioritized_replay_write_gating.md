---
title: Prioritized replay write-gating (MECH-443 / MECH-444)
parent: "Sleep & Offline Integration"
grandparent: Architecture
nav_order: 7
---

# Prioritized replay write-gating (MECH-443 / MECH-444)

**Status:** candidate (registered 2026-06-19). Architecture stub for two
candidate mechanisms imported via the Convergence Demand Pipeline row **CDQ-005**
(MuZero / EfficientZero *reanalyze* intake, `REE_convergence/sources/muzero/`).

**Off the V3 critical path.** Both claims are `candidate / substrate_ceiling /
generation:v3 / v3_pending:true`; they block no V3 closure node. The pipeline
surfaces ideas; decide-whether-to-build is a later governance step.

---

## What is already owned: MECH-319 (the binary gate)

`arc_062_rule_apprehension:GAP-K` is the replay-write-gating node. Its claim
**MECH-319** (`simulation_mode_rule_write_gating`, provisional; V3-EXQ-628
PASS/supports) is a **binary** categorical gate on the rule-arbitration layer:
during a ghost / replay / DMN pass (`caller_sim=True`) the gate either **blocks**
arbitration-weight writes (the MECH-319 normal regime) or **admits** them (the
`admit_writes=True` V3-EXQ-543c/628 falsifier). It is all-or-nothing. It says
nothing about *ordering* among the replayed transitions it admits, nor about the
*freshness* of the targets they carry.

Module: `ree-v3/ree_core/regulators/simulation_mode_rule_gate.py`
(`SimulationModeRuleGate`, primitive `effective_simulation_mode(simulation_mode,
site) -> bool`), consulted at the `GatedPolicy.forward` and
`LateralPFCAnalog.update` call sites.

## The non-duplicative import: grade the admitted writes

MuZero/EfficientZero *reanalyze* contributes two things the binary gate does not
cover. Both are **enrichments of the existing MECH-319 write primitive**, not a
parallel module — which is why they are `substrate_ceiling` (the current gate is
too coarse to carry the signal) rather than a new substrate.

### MECH-443 — priority-weighted replay write selection {#mech-443}

When the replay write channel is open, the admitted transitions should update the
rule-arbitration layer in **graded priority order**, weighted by an update-utility
signal (a surprise / value-prediction-error / coverage proxy), not uniformly.
External analog: EfficientZero/MuZero prioritized experience replay (priority ~
value-prediction error). MECH-443 is the **WHICH / HOW-STRONGLY** complement to
MECH-319's **WHETHER** gate.

**Biology (lit-pull 2026-06-19, SUPPORTED-with-refinement;
`evidence/literature/targeted_review_replay_prioritization_mech_319/`):**
hippocampal SWR replay is demonstrably prioritized, not uniform — Mattar & Daw
2018 (expected-value-of-backup = gain × need), Ólafsdóttir 2015 (motivational
relevance gates replayed content), Haga & Fukai 2018 (reward-anchored reverse
replay gates *which* pathway is strengthened), Milstein 2022 (reward-biased replay
emerges from CA3 constraints). **Load-bearing refinement (Carey et al. 2019):**
replay can be biased *away* from the currently-most-valuable outcome, so the
priority is the value of the **update** (gain × need), **NOT reward magnitude**.
A MECH-443 implementation that equates priority with reward level or
committed-policy value is biologically falsified.

**Falsifier:** a per-transition update-utility (surprise/value-error) priority
weight on admitted replay writes lifts rule-arbitration retention/selectivity (or
committed-rule entropy) strictly above a **matched-total-write-mass** uniform-admit
control on ≥2/3 seeds. If inert vs uniform admit — or if it helps only by raising
total write mass — MECH-443 earns no keep over the binary gate.

### MECH-444 — staleness-gated target refresh on replay write {#mech-444}

The more speculative leg. An admitted replayed transition should not write its
stored (ghost-derived, possibly stale) target verbatim; the target should be
**recomputed against the current model/policy** before it updates the rule layer,
and the write down-weighted/skipped when the recomputed target has not drifted
(low staleness ⇒ low update value). This is the *reanalyze* trick (re-run the
model on stored trajectories for fresh targets) + EfficientZero off-policy/staleness
correction. It guards the failure MECH-319 was built to prevent (overcommitment to
ghost-derived weights) from re-entering *through* the prioritized admitted-write
channel MECH-443 opens — so the priority signal (443) and the freshness signal
(444) must operate together.

**Biology:** supported **by analogy**, not by a directly-documented cellular
operation (hence lower confidence and separate registration). Mattar & Daw's
*gain* term *is* a staleness measure (a backup has high gain precisely when the
current estimate is most outdated); Ólafsdóttir's generative preplay shows replay
produces goal-current content rather than verbatim playback. Honest caveat: no
recording study demonstrates a literal "recompute-the-target-then-write"
hippocampal operation.

**Falsifier:** recomputing the replay write target against the current model
before it updates the rule layer (and down-weighting low-drift writes) produces
*less* rule-arbitration drift / overcommitment than writing the stored stale
target, on ≥2/3 seeds, on the MECH-319 `admit_writes=True` drift-inducing
substrate — i.e. the V3-EXQ-628 block-vs-admit divergence is attenuated by the
refresh. If it does not attenuate drift, the staleness gate is inert.

---

## Relationship to MECH-319 and to each other

| | MECH-319 (owned) | MECH-443 (candidate) | MECH-444 (candidate) |
|---|---|---|---|
| Question | *Whether* a sim-mode pass may write | *Which / how strongly* admitted transitions write | *How fresh* each admitted write's target is |
| Form | Binary gate | Graded priority (update-utility) | Target recompute + drift down-weighting |
| Evidence | V3-EXQ-628 PASS | candidate (lit SUPPORTED-w-refinement) | candidate (lit supported-by-analogy) |

MECH-443 and MECH-444 **compose**: prioritized writing of *stale* targets would
re-introduce the very drift MECH-319 prevents, so the priority and freshness
signals are intended to operate jointly on the same admitted-write channel.

## Provenance

- Demand-queue row: `evidence/planning/convergence_demand_queue.v1.json` (CDQ-005)
- Pipeline plan: `evidence/planning/convergence_demand_pipeline_plan.md` (LOW-MUZERO node)
- Intake pack: `REE_convergence/sources/muzero/`
- Promotion packet: `REE_convergence/handoff/packets/outbox/2026-06-19_cpkt_muzero_reanalyze.json`
- Biology: `evidence/literature/targeted_review_replay_prioritization_mech_319/`
