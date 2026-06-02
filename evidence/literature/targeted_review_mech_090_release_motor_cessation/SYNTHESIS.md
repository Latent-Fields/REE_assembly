# SYNTHESIS — MECH-090 release-path disambiguation (motor-program cessation)

**Generated:** 2026-06-02T15:35:42Z
**Routed by:** failure_autopsy_V3-EXQ-592f_2026-06-02 Section 9.1 (B3 branch) via
`evidence/planning/mech090_release_path_audit_2026-06-02.md` (user-confirmed B3, 2026-06-02)
**Scope:** the disambiguating question — when a committed motor program's
execution readiness (R-c nav_competence + score_margin) degrades mid-execution,
absent threat spike / positive completion / schema invalidation, which biological
substrate aborts it? Three candidates: (i) a distinct lower-level motor-cancellation
circuit; (ii) a commitment-latch readout of goal-level disengagement (already
surveyed in `targeted_review_goal_disengagement`); (iii) admission-only is correct
and the reach axis is substrate_ceiling / V4.
**Did NOT re-survey** goal-level disengagement biology (Wrosch/Brandstaetter/Klinger/Husain)
— that pull (2026-05-19) is the comparison baseline, not re-run.

## Entries

| Entry | Source | Direction | Conf | Contribution |
|---|---|---|---|---|
| changes_of_mind_resulaj2009 | Resulaj/Kiani/Wolpert/Shadlen 2009, Nature | supports | 0.82 | TRIGGER: an already-initiated action is reversed by continued internal evidence/decisiveness. Commitment is NOT locked irreversibly. |
| stn_decision_threshold_cavanagh2011 | Cavanagh/Frank et al. 2011, Nat Neurosci | supports | 0.78 | CIRCUIT: the STN (= beta-gate substrate) dynamically + bidirectionally modulates commitment threshold; STN-DBS removes the brake -> impulsivity. Admission-only is a lesioned STN. |
| bg_output_suppression_falasconi2025 | Falasconi/Kanodia/Arber 2025, Nature | supports | 0.74 | EFFECTOR/LEVEL: BG output (SNr) bidirectionally + movement-specifically licenses/suppresses ongoing motor programs in real time; a distinct, faster substrate than slow goal-level disengagement. |
| nonselective_stopping_wessel2022 | Wessel/Diesburg et al. 2022, Curr Biol | mixed | 0.70 | DELIMITER: the canonical stop-signal STN brake is real + causal but EXTERNAL-cue-triggered + NON-SELECTIVE — the wrong trigger/scope; rules out "it's just the stop-signal reflex." |

## Verdict — route to B3b (new substrate, R-c/beta-gate level, graded online)

The biology answers the disambiguating question cleanly and against two of the three candidates:

- **Candidate (iii) — admission-only is correct / substrate_ceiling+V4 — REFUTED.**
  Cavanagh/Frank show the STN (REE's beta-gate substrate) is a continuously-modulated
  bidirectional commitment regulator, and that disabling it produces *impulsive
  under-commitment*, not stable holding. Resulaj shows an already-initiated action is
  reversible by continued internal evidence. Biological commitment is not an
  irreversible latch; an admission-only beta gate is a lesioned STN. The 592f reach gap
  is a real architectural incompleteness, not a mis-routed expectation.

- **Candidate (ii) — it's just a readout of goal-level disengagement (B2) — INSUFFICIENT.**
  Falasconi shows motor-program maintenance/cessation is a continuous, granular,
  movement-specific basal-ganglia-OUTPUT function operating moment-to-moment — a
  distinct and faster substrate than the slow, appraisal-driven, goal-level
  disengagement (Wrosch/Klinger, instantiated as MECH-340 on the ghost-goal bank).
  These are two levels; the 592f gap is at the lower (motor-latch) one. A pure readout
  of MECH-340 goal disengagement does not capture the fast, decisiveness-driven,
  targeted motor-latch revision.

- **Candidate (i) — a distinct motor-cancellation substrate — SUPPORTED, with a precise shape.**
  The release REE is missing is: an **internally-driven** (continued evidence /
  decisiveness, not external cue — Resulaj), **graded/online** (bounded-accumulation
  and conflict-scaled threshold, NOT a one-shot Schmitt flag — Resulaj + Cavanagh),
  **targeted** (movement-specific, not the global non-selective stop reflex —
  Falasconi vs Wessel), release **sited at the R-c / beta-gate level itself**
  (because the STN that admits the commitment is the same circuit that dynamically
  regulates holding it — Cavanagh). The canonical external-cue, non-selective
  stop-signal pathway (Wessel) is the WRONG model and is already covered in REE by
  MECH-091 (the threat/surprise analog).

**Routing: B3b** — open a NEW substrate_queue entry for a maintenance-time,
readiness-driven commitment-release coupling at the R-c / beta-gate level, distinct
from (a) the MECH-090 admission predicate, (b) MECH-091 urgency-interrupt (external
threat/surprise), and (c) MECH-340 goal-level disengagement (ghost-goal bank). This
is autopsy **option (a) resurfacing under B3b** — but the biology adds two binding
design constraints that the naive option-(a) sketch lacked:

1. **Graded online, not a Schmitt flag.** The trigger should be a continued
   accumulation of low decisiveness / nav_competence (drift-to-a-release-bound or
   conflict-scaled hold/release tendency), NOT "below floor for K consecutive ticks."
   This converges with the goal-disengagement pull's contested-phase warning
   (Brandstaetter/Klinger) and the changes-of-mind bounded-accumulation model.
2. **Targeted + hysteretic, with reengagement coupling.** Release the specific
   committed program, not a global brake (Falasconi vs Wessel); guard against the
   premature-abort pole (reversing a correct-but-hard commitment — Resulaj failure
   signature) with hysteresis and a reengagement path.

**Falsifiable distinctions** this substrate must respect (so it does not collapse
into existing claims): (a) vs MECH-091 — fires on internal decisiveness decay with
z_harm_a BELOW threshold; (b) vs ARC-028 completion — fires when completion_signal is
LOW (poor options), the opposite regime; (c) vs MECH-269b/V_s — fires with a STABLE
world schema (no anchor invalidation); (d) vs MECH-340 — operates on the active
beta-gate commitment at motor-program timescale, not on ghost-goal-bank re-probe
persistence at goal-appraisal timescale.

## What this does NOT license

- It does NOT re-open the MECH-090 admission axis (V3-EXQ-592d 4-arm validator stays
  live; admission integration intact).
- The 592f manifest stays `pending_retest_after_substrate=TRUE` until the B3b
  substrate lands and a successor probe validates the maintenance-time release.
- This is a literature verdict, not a substrate landing. The B3b substrate_queue
  entry + design doc + implementation are a separate `/implement-substrate` session.
- lit_conf here is a parallel signal (sanity-check + biology harvest); it does NOT
  promote MECH-090 or weight experimental confidence (Phase-3 lit/exp decoupling).
