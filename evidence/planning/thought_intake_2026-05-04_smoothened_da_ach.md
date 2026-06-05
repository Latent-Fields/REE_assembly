# Thought intake: striatal dopamine-acetylcholine timing windows as E3 reinforcement write-gate

**Date:** 2026-05-04 (raw); intake written 2026-06-05
**Status:** intake / candidate (NOT yet registered). Folds into the plasticity-governance cluster.
**Raw thought file:** `docs/thoughts/2026-05-04_smoothened_modulation_ACh_Dopamine_learning.md`
**Origin:** Uribe-Cano & Kottmann 2026 (iScience) -- Smoothened (a GPCR) on striatal cholinergic
interneurons modulates dopamine-associated acetylcholine pauses, altering DA-ACh coordination,
motor learning, and effort management. User: "also very relevant for REE."
**Anchors:** MECH-083 (ACh as meta-level plasticity gain: durable-write vs read-through),
MECH-061 / BetaGate (E3 basal-ganglia commitment), the gated_plasticity cluster
(`thought_intake_2026-05-21_gated_plasticity.md`), sleep substrate (SD-017 / MECH-204),
`docs/architecture/psychiatric_failure_modes.md`.

---

## 1. Core idea

Striatal reinforcement is **dopamine-acetylcholine temporally-windowed policy-writing**, not
dopamine-weighted action selection. Cholinergic-interneuron pauses open brief plasticity-permissive
windows in which dopamine can write recently-active corticostriatal policies. "Dopamine says
*this mattered*; acetylcholine says *this is the window in which it may be written*; Smoothened-like
modulation says *how persistently to write*." Smoothened ablation accelerated motor learning but
impaired effort/timing recalibration -> the persistence-vs-flexibility trade-off E3 must manage.

## 2. What is new vs what REE already has

| Element | Already in REE? | Verdict |
|---|---|---|
| ACh gates whether a teaching signal teaches | **Yes** -- MECH-083 (ACh meta-level plasticity gain), and the gated_plasticity cluster's ACh-timing-window | Confirms; this is the **striatal-specific, DA-ACh-coordination** instance |
| E3 basal-ganglia commitment + BetaGate | **Yes** -- MECH-061, BetaGate (MECH-090) | Confirms |
| **E3 commitment also creates a biologically-timed reinforcement EVIDENCE RECORD** (commit record + outcome marker + plasticity window + persistence bias + effort trace), with rule content distributed across hippocampal rollout / cortex / striatal windows / sleep -- not all in BG | **Partial** -- distributed-rule idea aligns with hippocampal-rollout claims; the "BG writes a tagged record, sleep refines it" framing is sharper | **Extension** |
| **Persistence-vs-flexibility tuning** as a separable E3 operation (distinct from action selection / reinforcement marking / plasticity permission) | **No explicit claim** | **NOVEL** -- the 5-way separation (select / mark / permit / persist / effort-calibrate) |
| Smoothened as one exemplar of a general "plasticity-window modulator" class | n/a | Framing -- the thought correctly says do NOT overcentralise Smoothened |
| Psychiatric mapping (addiction = excess persistence; OCD = impaired flexibility/extinction; Parkinson's = disrupted DA-ACh; apathy/mania/ADHD) | **Partial** -- psychiatric_failure_modes.md exists; DA-ACh-timing axis is a new lens | **Extension** for the computational-psychiatry atlas |

**Verdict: a striatal-specific deepening of the plasticity-governance cluster.** It is the
*E3/basal-ganglia* instance of the same "learning requires a permitted write window" principle the
2026-05-21 gated_plasticity thought states generally. Register them together: gated_plasticity =
the general typed-write-permission frame; this = the DA-ACh striatal write-window + persistence/
flexibility tuning + the BG-as-evidence-record refinement.

## 3. Computational abstraction (from the thought, usable as v3-proxy sketch)

`policy_update = DA_event * ACh_gate * context_match * policy_trace_strength * effort_adjustment`,
with ACh_gate in [0,1] (write-window openness) and a persistence/flexibility parameter standing in
for Smoothened. High ACh_gate -> strong write-through; low -> DA noted but weak consolidation. Does
NOT require modelling Smoothened directly. Connects to sleep: waking lays tagged traces; sleep
replays/compresses/generalises/reassigns them.

## 4. Candidate claims

- **MECH (striatal-DA-ACh-windowed-write)** -- striatal reinforcement is temporally coordinated
  DA-ACh write-gating, not scalar DA update; CIN pauses create plasticity-permissive windows.
  *[lit-anchored; instance of MECH-083]*
- **ARC (E3-DA-ACh-coordination-layer)** -- E3 BG commitment includes a DA-ACh layer determining
  which recently-active policy traces become eligible for reinforcement, separate from which action
  is selected. *[novel architectural update]*
- **ARC (separate-select-mark-permit-persist-calibrate)** -- distinguish action selection /
  reinforcement marking / plasticity permission / persistence tuning / effort calibration as
  partially-separable operations. *[novel]*
- **Q (ach-windows-tag-for-sleep)** -- do ACh-gated waking write-windows create trace-tags that
  sleep/offline later uses for bucket refinement / compression / context reassignment? *[open;
  ties to SD-017 sleep]*

## 5. Affected existing claims / docs

- MECH-083 (cite as the general ACh-gain claim this instantiates), MECH-061 / MECH-090 (BG
  commitment), SD-017 / MECH-204 (sleep refinement of tagged traces).
- `docs/architecture/psychiatric_failure_modes.md` (DA-ACh-timing axis across addiction / OCD /
  Parkinson's / apathy / mania / ADHD).
- Home doc at registration: the basal-ganglia / commitment-gating architecture, cross-linked to
  the gated_plasticity cluster and sleep.

## 6. Next steps (gated)

1. **Register with the gated_plasticity cluster** (one pass): general write-permission frame +
   this striatal DA-ACh instance + the 2026-06-01 plasticity-window neuromodulator note. Cite
   MECH-083; do not duplicate it.
2. Per memory `feedback_biology_before_formal_definitions`, fold into the plasticity-cluster
   lit-pull (the ACh-DA half overlaps Berridge/Hasselmo + this iScience source).
3. V3-tractable sliver: the persistence-vs-flexibility tuning could be probed against the
   monostrategy / over-persistence failures already in the queue -- flag if a matching signature appears.

## 7. Cross-references

- Raw: `docs/thoughts/2026-05-04_smoothened_modulation_ACh_Dopamine_learning.md` (Uribe-Cano &
  Kottmann 2026, iScience).
- Claims: MECH-083, MECH-061, MECH-090, SD-017, MECH-204.
- Cluster: `thought_intake_2026-05-21_gated_plasticity.md`, `docs/thoughts/2026-06-01_plasticity_window_neuromodulators.md`.
- Memory: `project_plasticity_window_neuromodulators`, `feedback_biology_before_formal_definitions`.
