---
nav_exclude: true
---

# SD-017: Minimal Sleep-Phase Architecture (V3)

**Claim ID:** SD-017
**Subject:** `sleep_phase.minimal_sleep_infrastructure_v3`
**Status:** candidate
**Registered:** 2026-04-05
**Depends on:** MECH-092, ARC-038, ARC-007, SD-014
**Blocks:** ARC-045, MECH-166, MECH-167 (and transitively all claims requiring attribution mapping convergence)

---

## Roadmap Change

**Previous position:** All sleep/consolidation phases were V4 scope.
(`v3_v4_transition_boundary.md` previously stated: "V3 is fully online, no sleep/consolidation cycle.")

**New position (2026-04-05):** A minimal sleep-phase infrastructure is a V3 requirement.

**Why the change:**
Hippocampal attribution mapping -- the core E3 function that enables contextual goal-directed navigation -- requires offline consolidation phases to converge. Without them:
- Context representations remain globally undifferentiated (cosine_sim -> 1.0) regardless of training duration or supervised signal strength (Law 2016: stabilisation requires ~3 interleaved sessions of multi-context exposure, not achievable online alone)
- Slot structure cannot be installed before slot-filling (Sanders et al. 2020: prior must be learned before posterior inference is informative -- MECH-166)
- The agent navigates as if all contexts are the same -- monostrategy, the "fish swimming the same route" failure

This is not a V4 edge case. It appears in V3 and blocks the E3 goal and harm streams from producing useful attribution estimates.

---

## The Three Information Phases

| Phase | Biological Analog | Function | REE Mechanism |
|-------|------------------|----------|---------------|
| **Waking** | Online encoding | Gather what is out there | E1 world model, hippocampus raw experience logging, MECH-092 quiescent replay |
| **SWS-analog** | Slow-wave sleep, hip -> cx | Form the slots -- schema abstraction, which distinctions matter | Hippocampus-to-cortex replay pass updating context templates |
| **REM-analog** | REM reactivation | Fill the slots -- causal attribution from co-correlational ordering | Attribution replay, filling context slots with evidence estimates |

The **information direction switch** between phases does real computational work:
- SWS-direction (hippocampus -> cortex): schema installation. The hippocampus proposes which context distinctions are structurally relevant; the neocortex (E1, E3 context memory) receives and stabilises these as attractors.
- REM-direction: filling. With stable context attractors now installed, recent trajectory evidence is replayed and attributed to the correct context slots, building co-correlational estimates (which outcomes co-occur with which contexts).

Without the direction switch, online encoding fills both roles simultaneously and does neither well.

---

## V3 Minimal Implementation

This is distinct from the full V4 sleep machinery (MECH-120-123). V3 requires:

### SWS-analog pass
- Triggered: at end of a training epoch or after K episodes (configurable)
- Mechanism: hippocampal module runs a schema-consolidation pass in the hippocampus-to-cortex direction
  - Distinct from MECH-092 (waking quiescence replay, which is hippocampus-internal)
  - Updates context templates in ContextMemory (the "slot structure")
  - Does NOT require z_goal (ARC-038 compliant: no active goal during consolidation)
- Output: differentiated context attractors in ContextMemory (cosine_sim < 0.95 target)

### REM-analog pass
- Triggered: after SWS-analog (slots must exist before filling)
- Mechanism: causal attribution replay
  - Replays recent trajectory buffer through the attribution pipeline
  - Fills context slots with co-correlational evidence (which harm events, which benefit events, which action sequences co-occurred with which context)
  - Ordering matters: earlier events in a trajectory contribute causal precedence to later outcomes
- Output: updated attribution maps -- residue field geometry shaped by context-specific evidence

### What this is NOT
- Not MECH-120 (SHY synaptic homeostasis with normalisation) -- that remains V4
- Not MECH-121 (full NREM SWR+spindle pipeline) -- that remains V4
- Not MECH-122 (thalamo-cortical spindle bursts) -- V4
- Not MECH-123 (REM precision prior recalibration) -- V4
- Not MECH-092 (waking quiescent replay) -- that is the V3 prerequisite, already implemented

SD-017 is the minimal infrastructure that makes MECH-092 useful: without schema installation first, the quiescent replay has no stable context structure to organise into.

---

## Relationship to Existing Claims

| Claim | Relationship |
|-------|-------------|
| MECH-092 | V3 prerequisite (waking quiescent replay, already implemented); SD-017 extends it with bidirectional offline phases |
| ARC-038 | Waking consolidation mode (no z_goal, map geometry update) -- the SWS-analog pass is the offline instantiation of this principle |
| ARC-045 | Asserts bidirectionality is necessary; SD-017 is the design decision that implements it |
| MECH-166 | Slot-formation/filling temporal separation -- grounded by SD-017's two-phase structure |
| MECH-165 | Replay diversity (forward/reverse balance) -- V4 extension; requires MECH-166 first |
| MECH-120-123 | Full sleep machinery -- V4; SD-017 is the V3 scaffold they extend |

---

## Evidence Grounding

- **Law et al. 2016** (Hippocampus 26:1560): context representations require ~3 interleaved sessions to stabilise -- grounds the necessity of periodic offline phases for schema formation
- **Sanders, Wilson & Gershman 2020** (eLife): context discrimination bounded by learned prior quality -- grounds the slot-formation-before-filling requirement (MECH-166)
- **Bengio et al. 2009** (ICML): staged/easy-to-hard training necessary for non-convex representation learning -- grounds Phase 0 -> SWS -> REM staging (ARC-042)
- **Ego-Stengel & Wilson 2010** (Hippocampus): disrupting waking rest ripples impairs subsequent spatial learning -- grounds necessity of offline phases (not just online training)

---

## Bayesian Reasoning Framework (INV-044)

SD-017 is not merely a training convenience -- it implements the architectural prerequisites for approximate Bayesian contextual inference.

**Prior construction (SWS-analog = slot-formation):** The SWS-analog pass builds P(context) -- the prior over context types. Before this pass, the system has no stable schema of which contextual distinctions are structurally relevant. The hippocampus-to-cortex propagation installs context attractors: compressed representations abstracted from the full episodic record.

**Posterior inference (REM-analog = slot-filling):** The REM-analog pass performs P(context | evidence) -- posterior inference given the installed prior. With context attractors stable, trajectory evidence can be attributed to the correct slot. Without the prior, the posterior is undefined -- all evidence competes for globally undifferentiated representations.

**Why co-computing fails (INV-044):** An online system attempting both functions simultaneously never constructs a stable prior. Every new episode shifts the schema, preventing attribution from converging. The result is cosine_sim -> 1.0 regardless of training duration -- exactly the MECH-153 failure mode documented by Law et al. 2016.

**Bidirectional flow as generative/recognition duality (ARC-045):**
- Hip->Cx direction (SWS-analog): generative model installation -- hippocampus proposes structure, neocortex stabilises as attractors
- Cx->Hip direction (REM-analog): recognition pass -- prediction error signals update the posterior

This maps onto the generative/recognition duality of hierarchical Bayesian models (predictive coding, Friston 2005-2010) without requiring explicit probability distributions.

**What this is NOT:**
- Not formal Bayesian inference (no explicit P(context) distribution)
- Not approximate message passing or belief propagation
- Not Bayesian parameter estimation

It is structural isomorphism with approximate Bayesian contextual inference: the information geometry required for context-sensitive attribution to emerge. SD-017 moves ree-v3 from purely discriminative/reactive (observe -> respond) to a system that maintains and updates a structured generative model of context.

**Homeostatic accumulators as empirical Bayes (MECH-167):** The slow EMA accumulators (z_harm_a, drive_level) implement empirical Bayes over need states. The accumulated baseline is the running prior; deviations are precision-weighted signals. INV-044 applies: the accumulator must converge before deviations are interpretable.

---

## V3 Build Order Impact

SD-017 must be implemented before the following V3 goals become achievable:
1. Reliable context discrimination (MECH-153/ARC-042) -- EXQ-239 tests the online proxy; SD-017 is the full solution
2. Attribution mapping convergence (E3 residue field organised by context) -- currently unachievable without slot-formation
3. Goal and harm stream integration with context -- z_goal seeding and z_harm_a accumulation need context identity to produce interpretable attribution

Until SD-017 is implemented, ree-v3 is behaviourally an online agent whose hippocampus has the machinery for context-sensitive attribution but cannot activate it -- the maps stay flat.
