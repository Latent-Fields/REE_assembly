---
title: "MECH-342: Maintenance-time readiness-driven commitment-release coupling"
parent: "Executive & PFC Control"
grandparent: Architecture
nav_order: 5
---

# MECH-342: Maintenance-time readiness-driven commitment-release coupling

**Claim ID:** MECH-342
**Subject:** control_plane.commit_maintenance_release
**Status:** IMPLEMENTED
**Registered:** 2026-06-02
**Depends on:** MECH-090 (commit-entry predicate / R-c readiness conjunction; beta-gate latch + CommitReadiness signal)
**Blocks:** V3-EXQ-592f reach-axis retest (`pending_retest_after_substrate`); the implicit "R-c governs maintenance/release too" claim that 592f localised as a substrate gap.

## Problem

V3-EXQ-592f (controlled state-machine probe, 2026-06-01; FAIL_NO_RELEASE_AUTHORITY)
confirmed that the MECH-090 R-c readiness conjunction is **admission-only**. The
two readiness predicates -- `BetaGate.should_admit_elevation` (within-tick
decisiveness / score_margin) and `CommitReadiness.is_above_floor` (across-tick
nav_competence) -- gate `beta_gate.elevate()` only on commit **entry** (bistable:
`result.committed AND NOT beta_gate.is_elevated`). When execution readiness
degrades **while the agent is already beta-elevated**, the predicates still fire
as diagnostics (nav_blocks advanced 6/stage in 592f stages C/D) but neither
calls `beta_gate.release()` nor clears `e3._committed_trajectory`. 592f measured
zero state-occupancy suppression and zero decommit transitions across stages
B/C/D.

The MECH-090 release-path audit (`evidence/planning/mech090_release_path_audit_2026-06-02.md`)
ruled out (B1) all four existing release pathways covering this degraded-readiness-
mid-commitment case:

| Pathway | Trigger | Covers degraded readiness? |
|---|---|---|
| ARC-028 / MECH-105 hippocampal-completion | `completion_signal >= 0.75` (options GOOD) | NO -- directionally opposite (degraded readiness pushes the signal AWAY from release) |
| MECH-091 urgency-interrupt | `z_harm_a/z_harm_un.norm() > threshold` | NO -- threat axis only |
| V_s commit-release (MECH-269/284/287) | committed anchor key dropped (schema staleness); `use_vs_commit_release` default OFF | NO -- schema axis, not readiness |
| SD-034 closure operator | rule_state stabilised (positive completion) | NO -- rule-stability axis |

The motor-program-cessation lit-pull
(`evidence/literature/targeted_review_mech_090_release_motor_cessation/SYNTHESIS.md`)
returned **verdict B3b**: open a NEW substrate for a graded/online, targeted,
R-c/beta-gate-level maintenance-time release on degraded decisiveness. Anchors:

- **Resulaj/Kiani/Wolpert/Shadlen 2009 (Nature)** -- changes-of-mind: an
  already-initiated action is reversed by continued internal evidence. Commitment
  is NOT an irreversible latch; the TRIGGER is a bounded accumulation of evidence.
- **Cavanagh/Frank et al. 2011 (Nat Neurosci)** -- the STN (REE's beta-gate
  substrate) dynamically and bidirectionally modulates the commitment threshold;
  disabling it produces *impulsive under-commitment*, not stable holding. An
  admission-only beta gate is a lesioned STN. (REFUTES "admission-only is correct".)
- **Falasconi/Kanodia/Arber 2025 (Nature)** -- BG output (SNr) bidirectionally and
  **movement-specifically** licenses/suppresses ongoing motor programs in real
  time; a distinct, faster substrate than slow goal-level disengagement.
- **Wessel/Diesburg et al. 2022 (Curr Biol)** -- the canonical stop-signal STN
  brake is external-cue-triggered and **non-selective** -- the WRONG model/scope.
  Already covered in REE by MECH-091 (the threat analog).

This is the autopsy's option (a) ("a new R-c-level release coupling") resurfacing
under B3b -- but the biology adds two binding constraints the naive option-(a)
sketch lacked (graded-online, not a Schmitt flag; targeted + hysteretic with a
reengagement path).

## Solution

A NEW pure-arithmetic regulator, `CommitMaintenanceRelease`
(`ree-v3/ree_core/policy/commit_maintenance_release.py`), and a release branch in
`REEAgent.select_action` that mirrors the MECH-091 urgency-interrupt template.
The SAME two R-c readiness signals that MECH-090 AND-composes to **admit** a
commitment here drive a graded, bounded-accumulation **release** of an
already-elevated beta latch when they degrade mid-commitment.

### Accumulator dynamics (per maintenance tick, only while beta is elevated)

```
deficit_d = clip((score_margin_floor - score_margin) / score_margin_floor, 0, 1)
            # within-tick DECISIVENESS axis (Hanes & Schall accumulator reading;
            # 0 when margin healthy OR no decisiveness signal -> inert axis)
deficit_n = clip((nav_floor - nav_competence) / nav_floor, 0, 1)
            # across-tick MOTOR-READINESS axis (Cisek-Kalaska affordance prep +
            # Roesch premature-commit; 0 when no nav signal -> inert axis)
combined  = max(deficit_d, deficit_n)
            # OR-composition: EITHER axis failing drives release pressure.
            # The De Morgan dual of the MECH-090 AND admission, conflict-graded
            # by the worse axis (Cavanagh/Frank).

recovered = (margin >= score_margin_reengage OR no margin signal)
            AND (nav >= nav_reengage OR no nav signal)

if combined > 0:   pressure += accumulation_rate * combined   # drift-to-bound (Resulaj)
elif recovered:    pressure  = max(0, pressure - leak_rate)    # reengagement path
else:              pressure  unchanged                         # dead-band hold (contested phase)
pressure = clip(pressure, 0, pressure_cap)

fire = pressure >= release_bound      # on fire, pressure resets to 0
```

On fire the caller releases the **specific committed program** (targeted, not a
global brake): `beta_gate.release(); _committed_step_idx = 0;
_committed_anchor_keys = None; e3._committed_trajectory = None`. Pressure is reset
to 0 at commit **entry** (each committed program accumulates independently) and on
fire.

### Why this satisfies the binding constraints

1. **Graded / online, not a one-shot Schmitt flag.** A single below-floor tick
   does not release; pressure drifts to the bound over
   `release_bound / accumulation_rate` ticks at maximum deficit (5 at defaults),
   and proportionally more ticks at smaller deficits (conflict-scaled). This is
   Resulaj bounded accumulation + Cavanagh conflict-graded threshold, and it
   honours the Brandstaetter/Klinger contested-phase warning that disengagement
   is an extended phase, not a flag.
2. **Targeted + hysteretic with a reengagement path.** The release touches only
   the active beta latch + committed trajectory (Falasconi movement-specific, not
   Wessel non-selective). The separate `reengage` levels (above the floors) create
   a hysteresis band: a transient dip that recovers **leaks** pressure back to 0
   (reengagement) rather than committing to abort, guarding the premature-abort
   pole (Resulaj failure signature). The dead-band between floor and reengage
   **holds** pressure (the contested phase).

### Config (REEConfig; all default no-op)

| Param | Default | Purpose |
|---|---|---|
| `use_maintenance_release` | False | master switch (bit-identical OFF) |
| `maintenance_release_score_margin_floor` | 0.05 | decisiveness failing at/below |
| `maintenance_release_score_margin_reengage` | 0.10 | decisiveness recovered at/above |
| `maintenance_release_nav_floor` | 0.3 | nav_competence failing at/below |
| `maintenance_release_nav_reengage` | 0.5 | nav_competence recovered at/above |
| `maintenance_release_accumulation_rate` | 0.2 | per-tick drift scale (conflict-scaled) |
| `maintenance_release_leak_rate` | 0.1 | reengagement leak per recovered tick |
| `maintenance_release_bound` | 1.0 | release threshold |
| `maintenance_release_pressure_cap` | 1.5 | accumulator clamp |

All surfaced through `REEConfig.from_dims`. Floors mirror the MECH-090 admission
floors (`commit_readiness_floor`=0.05, `mech090_readiness_floor`=0.3).

### Data flow

```
[e3.last_scores (last completed E3 selection, REE lower-is-better)] -> score_margin (decisiveness axis)
[CommitReadiness EMA (MECH-090 nav signal)]                         -> nav_competence (nav axis)
    -> CommitMaintenanceRelease.tick(score_margin, n_candidates, nav_competence)
    -> [pressure >= release_bound?]
    -> beta_gate.release() + reset _committed_step_idx + clear _committed_anchor_keys + clear e3._committed_trajectory
```

The release branch lives in the `select_action` release block immediately after
the MECH-091 urgency block, reading `self.e3.last_scores` (available every tick,
including between-E3-tick steps; a controlled state-machine probe sets it
directly) and `self.commit_readiness.get_readiness()` (None when CommitReadiness
is not instantiated -- the nav axis is then inert and only decisiveness drives).

## Architecture context — distinctness (falsifiable)

MECH-342 must NOT collapse into any existing mechanism. The falsifiable
distinctions the substrate respects:

- **vs MECH-090 admission predicate:** that gate fires on commit ENTRY and is
  AND-composed; MECH-342 fires during MAINTENANCE and is OR-composed (the De
  Morgan dual). MECH-090's admission axis (V3-EXQ-592d 4-arm validator) is **not
  reopened**.
- **vs MECH-091 urgency-interrupt:** fires on internal decisiveness/nav decay with
  `z_harm_a` BELOW threshold (no harm-stream input).
- **vs ARC-028 / MECH-105 completion:** fires when `completion_signal` is LOW
  (poor options) -- the opposite regime (no completion-signal input).
- **vs MECH-269b / V_s commit-release:** fires with a STABLE world schema (no
  anchor-set input).
- **vs MECH-340 ghost-goal persistence/efficacy gate:** operates on the ACTIVE
  beta-gate commitment at motor-program timescale, not the ghost-goal bank at
  goal-appraisal timescale.

## What this enables

- Closes the V3-EXQ-592f reach gap: the maintenance-time release authority the
  592f probe measured as zero (state-occupancy suppression + decommit transition).
- The 592f manifest's `pending_retest_after_substrate` stays TRUE until this
  substrate lands AND a 592f-style successor probe (V3-EXQ-592g) validates the
  maintenance-time release.

## MECH-094

`tick(simulation_mode=True)` is a no-op (no pressure advance, returns False). A
replay / DMN tick must not abort a committed motor program. Matches the SD-035 /
MECH-279 / MECH-313 / MECH-320 / `commit_readiness` simulation_mode pattern.

## Phased training

Not applicable. Pure-arithmetic regulator; no learned parameters, no gradient
flow, no encoder head. Same class as MECH-313 / MECH-320 / commit_readiness.

## Validation experiment

V3-EXQ-592g (queued via `/queue-experiment`): a 592f-style controlled
state-machine probe with `use_maintenance_release=True`. Forces beta elevated +
E3 committed pointer present + degraded readiness sustained, and verifies the new
coupling now produces state-occupancy suppression + a decommit transition (the
quantities 592f measured as exactly zero), with no false abort under healthy
readiness (the premature-abort guard).

## Related claims

MECH-090 (parent; commit-entry predicate / R-c admission conjunction), MECH-091
(urgency-interrupt; sibling release pathway, threat axis), ARC-028 / MECH-105
(hippocampal-completion release; opposite regime), MECH-269b / MECH-284 (V_s
commit-release; schema axis), SD-034 (closure operator; rule-stability axis),
MECH-340 / ARC-079 / Q-053 (goal-level disengagement; ghost-goal bank timescale),
MECH-094 (simulation-mode call-site scoping).
