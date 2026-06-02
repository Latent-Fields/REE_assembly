# Outstanding-tasks triage (2026-06-02)

Triage of five outstanding items, with a verdict (needed?), current tracking, and
the carry-forward mechanism. Investigated read-only 2026-06-02. This memo is the
durable backlog entry; the genuinely-actionable items also have launchable task chips.

---

## 1. MECH-090 release-path audit (after V3-EXQ-592f) — NEEDED, OPEN

**What:** The 592f failure autopsy (failure_autopsy_V3-EXQ-592f_2026-06-02.{md,json})
found MECH-090's R-c integration is **admission-only**: the readiness-conjunction gate
guards commit *entry* but does not couple to beta_gate.release()/`_committed_trajectory`
clearing when a failure occurs *while already committed*. User-confirmed option (b): NOT a
new R-c-level release coupling, but an AUDIT of four EXISTING release pathways to see if any
already provides maintenance-time release authority:
1. ARC-028 / MECH-105 hippocampal-completion (does it fire on mid-program degraded nav_competence?)
2. MECH-091 urgency-interrupt (z_harm_a.norm() threshold — fires on escalation, not on readiness decay)
3. V_s anchor invalidation MECH-269 / MECH-284 / MECH-287 (does sustained low readiness register as staleness?)
4. SD-034 closure operator (mode-conditioned at sd_033a write_gate >= min; orthogonal to readiness)

**Conditional chain (from the autopsy):** B1 = a pathway covers it -> clear the 592f
`pending_retest_after_substrate` flag, no new substrate work. B2 = gap found but an existing
lit-pull covers it -> open/amend the *affected pathway's* substrate_queue entry (NOT MECH-090).
B3 = gap exceeds current biology -> commission a `/lit-pull` at the disambiguating question.

**Status:** unstarted. Routed only inside the MECH-090 substrate_queue `amend_hint`
(amend_pending=false) + IGW-20260602-022; no execution container. 592f manifest
`pending_retest_after_substrate=true` stays TRUE until this resolves.

**Carry-forward:** task chip "MECH-090 release-path audit (4 pathways, B1/B2/B3)". An
`/implement-substrate`-style audit session: read the four pathways' code + biology coverage,
return B1/B2/B3, route any gap to the affected pathway (not MECH-090), and clear or hold the
592f flag accordingly. **Unblocked — can run now.**

---

## 2. substrate_queue back-fill (landed-but-not-queued) — NOT BLOCKING, DEFER

**What:** ~36 substrates documented IMPLEMENTED in ree-v3/CLAUDE.md have no entry in
evidence/planning/substrate_queue.json (mostly foundational/early: SD-003/007/008/009/010/011/012/014/017/023,
MECH-091/100/105/106/112/203/216/259/260/261, ARC-028/030/033, etc.).

**Verdict:** substrate_queue.json is an **intentionally-partial forward-planning document**
(read by serve.py morning-agenda "cusp items" = `ready==true AND status!=implemented`, and by
the governance reconcile loop). Entries are added when a substrate is in-flight or recently
landed with active validation work — not as a census of all implementations. Missing early
entries are a **historical/audit gap, not a governance blocker**: serve.py correctly filters
implemented substrates out, and nothing depends on the missing entries. The queue's own
`next_implement_substrate.rationale` (2026-04-27) already notes some landed-but-unqueued
substrates "worth back-filling on next reconcile".

**Carry-forward:** **Do NOT bulk back-fill.** On the next `/governance` reconcile, opportunistically
add `status: implemented` stub entries (with `metric_trajectory: null`, `validation_experiment:`
their already-run EXQ) for the 3-5 most recent un-queued landings. A full historical extraction
of metric trajectories from manifests is a V4-planning research artifact, not a current need.
No chip — folded into the governance routine.

---

## 3. MECH-341 post-616 branch (A-vs-B / stratified_temperature) — AMEND DONE, RE-RUN OPEN

**What / status:** The 2026-06-01 amend (stratified_within_class_temperature lever + A-vs-B
partial-redundancy probe via the existing use_support_preserving_cem / use_e3_score_diversity
flags) is **IMPLEMENTED** (655/655 contracts). Its validation **V3-EXQ-614c ran but FAILed on
instrumentation defects, not substrate** (per failure_autopsy_V3-EXQ-614c_2026-06-01):
(a) the entropy metric measured `argmin(last_scores)` which is temperature-INVARIANT by
construction (the lever only affects committed-action class selection downstream); within-class
firing diagnostics weren't recorded. (b) C1 used a per-seed band predicate where a cross-seed-mean
predicate was intended (ARM_0 cross-seed mean 0.7999 ~= the 0.800 target, but 0/3 seeds in band).
C3 substrate-readiness PASSed 3/3 on all arms.

**Open item:** **V3-EXQ-614d** — corrected harness: measure the committed-action class
distribution (temperature-sensitive), record `mech341_n_within_class_sampled` /
`mech341_last_within_class_temperature`, fix C1 to a cross-seed-mean predicate; same 4-arm
{None,0.5,1.0,2.0} sweep on the SD-056-amended baseline. Gates MECH-341 v3_pending clearance,
Q-054 re-issue (as V3-EXQ-616a), and arc_062_rule_apprehension:GAP-B (V3-EXQ-543l cohort).

**Carry-forward:** task chip "Queue V3-EXQ-614d (MECH-341 corrected harness)" via `/queue-experiment`.
**Unblocked — can run now.**

---

## 4. SD-013 contradiction / threshold resolution — NOT A FALSIFICATION, LOW-PRI / GATED

**What:** The "contradiction" is a **threshold-calibration conflict**, not a mechanism
falsification: EXQ-330a (raw Euclidean gap, 2.0x lift threshold) FAILed 7/10 seeds, while
EXQ-353 (normalized gap vs shuffled-action baseline, 1.2x threshold) PASSed all seeds 1.34-1.69x
on the same mechanism. EXQ-330a was already reclassified `does_not_support -> non_contributory`
(2026-04-17) with a note: "the 2.0x threshold is wrong, not SD-013". conflicts.md still lists
SD-013 conflict_ratio=0.25 (7 supports / 1 weakens). Residual real gap: `interventional_margin=0.1`
(the ReLU margin-loss target) was never empirically validated and may need to scale with z_harm_s
magnitude.

**Verdict:** open but **low-urgency and gated** — the resolution (an `interventional_margin` sweep:
{0.05, 0.1, 0.2, 0.5}, measuring counterfactual gap in confounded vs non-confounded states) belongs
in self_attribution_plan GAP-2 Phase 2, which is itself gated on the MECH-269 V_s monostrategy
landing. The conflict_ratio is already below the 0.3 governance-alarm threshold given the 330a
reclassification.

**Carry-forward:** record as a self_attribution GAP-2 Phase-2 follow-on (interventional_margin
calibration sweep). No chip now — gated on upstream V_s landing. Revisit when GAP-2 Phase 2 opens.

---

## 5. Architecture-epoch stale-evidence review — NEEDED, REAL GAP

**What:** Current epoch gating (planning_criteria.v1.yaml: epoch_start_utc=2026-02-27,
`stale_if_timestamp_before_epoch_start`) is **time-only** — it excludes pre-hybrid-guardrails
synthetic runs and nothing else. There is **no mechanism** that flags evidence as stale when a
substrate it mechanistically DEPENDS ON changes *after* the evidence was recorded (but after the
epoch start). `pending_substrate_reconfirmation` covers emergent INVARIANTS only (manual flag);
`pending_retest_after_substrate` appears in autopsy docs but is **informational** — the indexer
(build_experiment_indexes.py) does NOT read it to exclude evidence from scoring. Given the large
volume of substrate landings across 2026-05 / 2026-06 (ARC-062/065, SD-049/054/056, MECH-307/341,
scaffolded_sd054, etc.), April/early-May evidence on those mechanisms may now be mechanistically stale
yet still weighting claim confidence.

**Carry-forward:** task chip "Architecture-epoch stale-evidence review". Two parts:
(a) **Indexer enhancement** — teach build_experiment_indexes.py to honor a machine-readable
`pending_retest_after_substrate` (or a `superseded_by_substrate: <SD-id>@<date>`) manifest field so
manually-identified stale evidence is `scoring_excluded` rather than silently weighting confidence.
(b) **Scoped review** — for claims whose `depends_on`/`emergent_from` include substrates landed
2026-05-09..2026-06-02, list evidence recorded BEFORE the landing; decide per-entry: re-validate,
mark `pending_retest_after_substrate`, or keep (weak dependence). Consider a date-stamped
`substrate_dependencies.json` registry to automate the cross-reference going forward, and add an
"evidence-staleness audit" checklist step to the substrate-landing routine.

---

## Disposition summary

| Item | Needed? | Action | Chip? |
|------|---------|--------|-------|
| 1 MECH-090 release-path audit | Yes, open | /implement-substrate audit, B1/B2/B3 | Yes |
| 2 substrate_queue back-fill | Not blocking | opportunistic on next /governance | No |
| 3 MECH-341 614d | Yes (re-run) | /queue-experiment V3-EXQ-614d | Yes |
| 4 SD-013 threshold | Low-pri, gated | self_attribution GAP-2 Phase-2 margin sweep | No |
| 5 epoch stale-evidence | Yes, real gap | indexer enhancement + scoped review | Yes |
