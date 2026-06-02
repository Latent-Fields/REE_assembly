# MECH-090 Release-Path Audit -- degraded-readiness mid-commitment coverage

**Generated:** 2026-06-02T15:26:55Z
**Audit session:** mech090-release-path-audit-20260602T152057Z
**Routed by:** failure_autopsy_V3-EXQ-592f_2026-06-02 Section 9.1 (user-confirmed option b, 2026-06-02)
**Predecessor amend:** MECH-090 substrate_queue AMEND (commit aab1e61d96, admission-only + audit hint)
**Status:** audit complete; routing fork open (B2 vs B3, see Section 6)

---

## 1. Question and scope

V3-EXQ-592f confirmed (controlled state-machine probe) that MECH-090's R-c
readiness conjunction is **admission-only**: the `score_margin` gate
(`BetaGate.should_admit_elevation`) and the `nav_competence` EMA
(`CommitReadiness.is_above_floor`) both **fire** as predicates mid-commitment
(nav_blocks advance 6/stage in stages C/D) but neither calls
`beta_gate.release()` nor clears `e3._committed_trajectory` when readiness
fails **while the agent is already beta-elevated**. The 592f gap is a
localised reach-falsification of the implicit "R-c governs maintenance too"
assumption -- NOT a falsification of the MECH-090 base claim (EXQ-049e PASS
preserved) nor of the R-c admission integration (V3-EXQ-592d 4-arm validator
remains live on the admission axis).

Per the user-confirmed option (b) "admission-only + audit", this audit asks of
each of the four EXISTING release pathways one concrete question:

> **Does this pathway fire (call `beta_gate.release()` and/or clear
> `e3._committed_trajectory`) when nav_competence / commit-readiness has been
> LOW for K consecutive ticks while `beta_gate.is_elevated`?**

If yes for any pathway -> B1 (no new substrate; clear the 592f
`pending_retest_after_substrate`). If a gap is found with pathway-resident
biology coverage -> B2 (amend that pathway's substrate_queue entry, NOT
MECH-090). If the gap exceeds existing biology -> B3 (commission a /lit-pull).

---

## 2. Method

Read each pathway's live code under `ree-v3/ree_core/` plus its claim/biology
coverage. The decisive site for ALL release authority is the block of
`beta_gate.is_elevated`-guarded release branches in
`REEAgent.select_action` (`ree_core/agent.py:2780-2931`): six release
pathways, each of which calls `beta_gate.release()` + resets
`_committed_step_idx` + clears `_committed_anchor_keys`. The audit traces what
TRIGGERS each branch and whether degraded nav_competence / commit-readiness is
ever a sufficient (or even an input) condition.

---

## 3. Per-pathway verdicts

| # | Pathway | Trigger (verbatim from code) | Covers degraded readiness? |
|---|---------|------------------------------|----------------------------|
| 1 | ARC-028 / MECH-105 hippocampal-completion | `completion_signal >= 0.75`, where `completion_signal = sigmoid(-best_score*0.5)`, `best_score = min residue cost` | **NO -- directionally opposite** |
| 2 | MECH-091 urgency-interrupt | `beta_gate.is_elevated AND z_harm_a/z_harm_un.norm() > urgency_threshold(0.8)` | **NO -- threat axis only** |
| 3 | V_s anchor invalidation (MECH-269/284/287) | `use_vs_commit_release(False)` AND committed-entry anchor key dropped from active set | **NO -- schema-staleness axis, gated OFF by default** |
| 4 | SD-034 closure operator | rule_state delta `< 0.001` for 3 ticks AND beta elevated AND mode allowed AND `write_gate(sd_033a) >= 0.5` | **NO -- rule-stability (positive completion) axis** |

### 3.1 ARC-028 / MECH-105 hippocampal-completion -- NO (directionally opposite)

`BetaGate.receive_hippocampal_completion` (`ree_core/heartbeat/beta_gate.py:164`)
releases iff `completion_signal >= completion_release_threshold` (default 0.75).
`HippocampalModule.compute_completion_signal`
(`ree_core/hippocampal/module.py:1655`) computes:

```
best_score = min residue cost across trajectories   (lower = better)
completion_signal = sigmoid(-best_score * 0.5)      -> [0.5, 1.0)
  near 0 residue (GOOD trajectory found)  -> signal ~1.0   -> RELEASE
  high residue   (POOR options)           -> signal ~0.5   -> stays elevated
```

The release fires on a **positive completion event** ("a good plan/state was
found"). Degraded nav_competence means poor candidate trajectories (high
residue cost), which pushes `completion_signal` **toward 0.5 -- away from the
0.75 release threshold**. Low readiness therefore SUPPRESSES this release; the
agent stays committed. This pathway is the exact opposite of a
degraded-readiness abort. Biology: Lisman & Grace 2005 subiculum->NAc->VP->VTA
dopamine-on-good-completion -- a reward/quality signal, not a competence-failure
signal.

### 3.2 MECH-091 urgency-interrupt -- NO (threat axis only)

`ree_core/agent.py:2787-2820`: the only inputs are `beta_gate.is_elevated` and
`z_harm_a.norm()` (or `z_harm_un.norm()` under SD-019a) vs `urgency_threshold`
(default 0.8). No `commit_readiness`, `nav_competence`, or `score_margin` term.
The SD-037 MECH-281 consumer-cascade (`override_beta_interrupt_gain`, lines
2798-2809) scales the threshold by `override_signal = f(drive_level +
sustained-threat z_harm window)` -- still NOT readiness. Threat-escalation and
readiness-decay are orthogonal axes: a stuck-mid-commitment agent with degraded
readiness but `z_harm_a` below threshold never trips this. Biology: STN/GPe
nociceptive-escalation urgency burst -- explicitly threat-driven.

### 3.3 V_s anchor invalidation (MECH-269/284/287) -- NO (schema-staleness, default OFF)

There IS a release coupling here that the other pathways lack: `ree_core/agent.py:2834-2851`
(the "MECH-269 / MECH-090 read-side hook: V_s -> commit release"). When
`use_vs_commit_release` is True AND beta is elevated, it releases beta if a
commit-entry-snapshotted anchor key has dropped out of the active anchor set
(`not self._committed_anchor_keys.issubset(current_keys)`). Anchors drop via
MECH-284 staleness hysteresis or MECH-287 broadcast invalidation.

Two facts make this NOT cover the 592f gap:

1. **Gated OFF by default.** `use_vs_commit_release: bool = False`
   (`ree_core/utils/config.py:913`, `:2982`, `:3596`). The pathway is inert in
   the default substrate.
2. **Wrong axis even when ON.** The V_s signal is per-stream verisimilitude,
   computed as an identity-prediction proxy `score = clip(1 - ||z_curr -
   z_prev|| / (||z_curr|| + eps))` over the latent streams
   (`HippocampalModule.update_per_stream_vs`). Its input streams are
   `z_world / z_self / z_harm_s / z_harm_a / z_goal / z_beta` -- **commit-readiness
   / nav_competence is NOT one of them.** So this fires on **schema staleness**
   (the committed-to world region became invalidated -- the world changed under
   the agent), not on **motor incompetence** (the agent is executing badly but
   the world-schema is stable). A stuck agent with degraded nav_competence and a
   stable world schema would not trip it. Biology: Vinogradova 2001 / O'Mara
   2009 CA1/CA3 mismatch comparator -- a world/context-fidelity signal, not a
   motor-readiness signal.

### 3.4 SD-034 closure operator -- NO (rule-stability / positive completion)

`ree_core/governance/closure_operator.py` completion detector fires when
rule_state delta `< completion_rule_delta_threshold` (0.001) for
`completion_stable_ticks` (3) AND beta elevated AND `current_mode in
allowed_closure_modes` AND `write_gate("sd_033a") >= closure_min_sd033a_gate`
(0.5). It reads rule_state (LateralPFC), beta_elevated, operating_mode, and the
sd_033a gate -- **no nav_competence / commit_readiness / score_margin input.**
Closure = the abstract rule representation has STABILIZED (a satisficing /
"rule complete" signal). Biology: Rich & Shapiro 2009 OFC sequence-completion
cells; Collins & Frank 2014 task-set disengagement-on-completion.

**Edge case (load-bearing):** a degraded-readiness agent COULD coincidentally
have a stable rule_state (rule settled while the agent is stuck unable to
execute it) and trip closure. But that is a **false-positive coincidence** --
closure fires because the rule settled, with no verification that the agent has
the competence to execute it. It is orthogonal coverage, not principled
degraded-readiness release. Treating closure as the home for the 592f gap would
conflate "rule complete" with "motor program failed" -- biologically distinct.

---

## 4. New finding -- existing goal-disengagement biology already surveyed (adjacent, not on the latch)

Not noted in the 592f autopsy's Section 4/9.1 routing assumptions: an existing
lit-pull **`evidence/literature/targeted_review_goal_disengagement/`
(2026-05-19, 9 entries)** already surveys the disengagement / unattainability /
action-crisis biology and was the pull that built **MECH-340
PersistenceAppraisal** (ARC-079 / Q-053: `license = control_efficacy * (1 -
goal_unattainability)`; disengage when `license < persistence_floor`).

This matters for the B2/B3 determination because the autopsy's Section 4 framed
the gap as "release-side anchors are different (Lisman & Grace, Foster &
Wilson)" and Section 7 said "no new lit-pull required" -- without referencing
the goal_disengagement pull. That pull is the closest existing biology to a
degraded-efficacy abort. But two distinctions keep it from being a clean B1/B2:

1. **Wrong substrate / level.** MECH-340 consumes this biology at the
   **ghost-goal bank** (whether to keep an UNATTAINABLE GOAL as a re-probe
   target; `ree_core/hippocampal/ghost_goal_bank.py` +
   `persistence_appraisal_compute.py`), NOT at the **beta-gate
   motor-program-maintenance latch**. The 592f gap is one level lower: abort an
   in-progress committed MOTOR PROGRAM, not abandon a goal.
2. **Explicit design warning against autopsy option (a).** The pull's
   Brandstaetter 2013 (action-crisis) and Klinger 1975 (incentive-disengagement
   cycle) entries argue the disengagement trigger is **an extended, contested,
   metabolically-costly PHASE, not a one-shot threshold flag**, and that
   within-crisis goal-devaluation is a SYMPTOM not the trigger. A K-consecutive-
   ticks-below-floor Schmitt flag at the latch (autopsy option (a)) is the
   "premature-disengagement pole" this biology specifically warns against. So
   even routing the existing appraisal to the latch is not a trivial wiring
   extension -- it inherits a "must be a contested state with reengagement
   coupled in" constraint.

This pull also does NOT survey the lower-level **motor-program-cessation**
biology (STN beta-decay distinct from urgency-burst; Aron stop-signal /
action-cancellation; pallidal disengagement) that would be the natural home if
the latch abort is a distinct motor substrate rather than a goal-level
disengagement readout.

---

## 5. Routing determination

- **B1 (a pathway covers it): RULED OUT.** All four named pathways verdict NO,
  with code evidence (Section 3). None fires on degraded nav_competence /
  commit-readiness mid-commitment. The 592f `pending_retest_after_substrate`
  flag therefore does **not** clear by audit closure; the 592f manifest is NOT
  edited by this audit.

- **The gap is real and is one of two architectural framings (the disambiguating
  fork):**
  - **(H1) goal-level disengagement readout.** The latch abort is the same
    construct as MECH-340 goal-disengagement, just read at the commitment-latch
    level. Existing biology (`targeted_review_goal_disengagement`) covers the
    appraisal; the work is to route a persistence/efficacy appraisal to the
    beta-gate latch as a NEW release pathway -- heeding the contested-state /
    reengagement-coupled / not-a-one-shot-flag constraint. This is a **B2-style**
    outcome (amend the relevant pathway's -- here a NEW disengagement-release --
    substrate_queue entry, NOT MECH-090), with the caveat that it is a wiring +
    appraisal-design extension, not a pure wiring change.
  - **(H2) distinct motor-program-cessation substrate.** The latch abort is a
    lower-level motor-cancellation mechanism (STN beta-decay / stop-signal /
    pallidal disengagement), biologically distinct from goal-level
    disengagement, and NOT surveyed by any existing lit-pull. This is a
    **B3-style** outcome: commission a /lit-pull at the motor-cessation biology
    before any code, then route per B3a/B3b/B3c.

- **Why this is not a clean autopsy-style B3-fresh-pull NOR a clean B2-existing-
  biology call:** the goal-level horn (H1) IS already surveyed (so it is not
  "gap exceeds ALL existing biology"); the motor-cessation horn (H2) is NOT
  surveyed (so it is not "existing biology fully covers it"). The fork is
  precisely whether degraded-readiness latch-release is goal-level disengagement
  (H1, existing biology) or motor-program cessation (H2, unsurveyed) -- and that
  is an architectural-level disambiguation the audit surfaces but should not
  unilaterally resolve, because the 592f autopsy's routing did not have the
  goal_disengagement pull in view.

**Disambiguating question (for the lit-pull, if H2 / B3 is chosen):**

> When a committed motor program's execution readiness (motor competence /
> action-value decisiveness) degrades mid-execution -- absent an acute threat
> spike (MECH-091 covers that), absent a positive completion signal (ARC-028
> covers that), and absent world-schema/context invalidation (MECH-269b/V_s
> covers that) -- which biological substrate aborts the committed program? Is it
> (i) a lower-level motor-cancellation circuit (STN beta-decay distinct from the
> urgency burst; Aron stop-signal; pallidal disengagement), or (ii) a
> commitment-latch-level readout of the SAME goal-level disengagement appraisal
> already surveyed in targeted_review_goal_disengagement (Wrosch / Brandstaetter
> / Klinger / Husain), or (iii) is admission-only the correct architectural
> commitment for the latch, with degraded-readiness abort properly living only
> at the goal level (MECH-340) and a V4 reclassification of the reach axis?

---

## 6. Recommended next step (routing fork -- user decision)

The audit cleanly closes B1 (no existing pathway covers the gap) and surfaces a
two-horned fork that the 592f autopsy's routing did not anticipate (because it
did not reference the goal_disengagement pull). Recommended options, in order:

1. **B3 -- commission a /lit-pull at the disambiguating question above
   (recommended).** Targets the unsurveyed motor-cessation horn (H2) and the
   level-disambiguation (goal-level disengagement vs motor-latch abort vs
   admission-only-is-correct). Does NOT re-survey goal-disengagement. Output
   routes to B3a (existing pathway absorbs) / B3b (new substrate entry; the only
   branch where autopsy option (a) R-c-level release coupling can resurface, and
   only if the biology supports readiness-driven release at the R-c level) /
   B3c (substrate_ceiling / V4 reclassification of the reach axis).
2. **B2 -- treat H1 as settled: route the existing MECH-340 / disengagement
   appraisal to the beta-gate latch as a new release pathway,** registered on a
   NEW disengagement-release substrate_queue entry (NOT MECH-090), heeding the
   contested-state / not-a-one-shot-flag constraint. Skips the lit-pull on the
   bet that the latch abort IS goal-level disengagement.
3. **B3c now -- accept admission-only as the architectural commitment** and
   reclassify the 592f reach axis as substrate_ceiling / V4, on the reading that
   degraded-readiness abort properly lives only at the goal level (MECH-340) and
   the four existing latch-release pathways (completion / threat / schema /
   rule-completion) are the biologically complete set for the latch.

In all three, the 592f manifest's `pending_retest_after_substrate` stays TRUE
until the chosen branch lands (per autopsy 9.1).

---

## 7. What this audit does NOT change

- **592f manifest:** NOT edited. `pending_retest_after_substrate` stays TRUE
  (B1 ruled out; no definite landing branch yet). The
  `does_not_support -> non_contributory` + `substrate_ceiling` re-tag at the
  reach axis is governance's separate job (autopsy Section 9 item 2).
- **claims.yaml:** NOT edited. MECH-090 stays active; admission axis intact;
  V3-EXQ-592d 4-arm validator remains live on the admission axis.
- **MECH-090 substrate_queue entry:** NOT edited by this audit. The prior AMEND
  (commit aab1e61d96) already recorded the admission-only commitment + audit
  targets; any new release substrate (B2/B3b) registers on a NEW / the AFFECTED
  pathway's entry, not MECH-090's, per user-confirmed item 1.
- **Pathway code:** read-only audit; no code edited.

---

## Appendix: code sites

| Pathway | Trigger code | Claim/biology |
|---|---|---|
| Hippocampal-completion | `beta_gate.py:164` receive_hippocampal_completion; `module.py:1655` compute_completion_signal; `agent.py:2689` _e3_tick call | ARC-028/MECH-105; Lisman & Grace 2005 |
| Urgency-interrupt | `agent.py:2787-2820` | MECH-091; STN/GPe nociceptive escalation |
| V_s commit-release | `agent.py:2834-2851`; flag `config.py:913` use_vs_commit_release=False; `module.py` update_per_stream_vs | MECH-269/284/287; Vinogradova 2001, O'Mara 2009 |
| Closure operator | `closure_operator.py` tick() completion detector | SD-034; Rich & Shapiro 2009, Collins & Frank 2014 |
| Relief-completion (5th release path, for completeness) | `agent.py:2859-2877` | MECH-302/SD-050; suffering-derivative |
| Conditioned/contextual safety (6th/7th, for completeness) | `agent.py:2884-2931` | MECH-304/SD-051, MECH-303/SD-052 |
| Goal-level disengagement (adjacent, NOT on the latch) | `ghost_goal_bank.py` + `persistence_appraisal_compute.py` | MECH-340/ARC-079/Q-053; targeted_review_goal_disengagement 2026-05-19 |
