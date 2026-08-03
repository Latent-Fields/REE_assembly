# Failure Autopsy — V3-EXQ-874 (MECH-467)

Generated: 2026-08-03T10:16:57Z
Session: night-mode-e39dfd-436c874
Scope: single
Status: confirmed (interactive gate confirmed by user 2026-08-03)

## 1. Target

- `run_id`: `v3_exq_874_mech467_distractor_resistance_20260802T222132Z_v3`
- `queue_id`: V3-EXQ-874 (EXP-0398)
- `claim_ids`: MECH-467
- `outcome`: FAIL, manifest `evidence_direction`: does_not_support (self-routed)
- `interpretation.label`: `legs_covary_no_dissociation`
- `dry_run_checked`: true (via `scripts/check_dry_run_citations.py`) — clean, real run
  (`smoke: false`).
- `substrate_stable_across_run`: true.
- Recording: `validate_recording.py` reports complete always-core (no gaps).

## 2. Facts reconstruction

**Design**: three-leg distractor battery over existing substrate (diagnostic, explicitly
NOT a new attention module per the 2026-06-04 containment rule). Two arms:
`ARM_PRECOMMIT` (`internal_planning`) and `ARM_REPLAY` (`internal_replay`); the
during-commitment arm is deliberately excluded because "the substrate cannot currently
sustain multi-step commitment yet" (memory note `feedback_dont_queue_commitment_dependent_behavioural`).
3 seeds (42, 43, 44), 150 real environment ticks per (seed, arm) cell in a single
continuous episode (no mid-run reset, by design — resets zero `lateral_pfc.rule_state`).

**Three legs**, each read off existing telemetry (no new instrumentation):
(a) sensory capture — `resource_field_view_distractor`; (b) rule-state drift —
`agent.lateral_pfc.rule_state.norm()`; (c) wrong-target selection —
`info["sd049_consumed_type_tag_this_tick"]`, conditioned on rule verified intact.
PASS requires, in ≥1 arm: rule drift at floor (<0.05) **while** conditioned
wrong-target rate is elevated (≥0.10) — "behavioural capture with the rule intact."

**Pooled/per-seed results:**

| seed | arm | sensory capture | rule drift | n_intact | wrong_cond | n_wrong | n_correct |
|---|---|---|---|---|---|---|---|
| 42 | PRECOMMIT | 1.00 | 0.225 | 27  | 0.000 | 0 | 0 |
| 42 | REPLAY    | 1.00 | 0.015 | 150 | 0.000 | 0 | 0 |
| 43 | PRECOMMIT | 0.00 | 0.208 | 21  | 0.000 | 0 | 0 |
| 43 | REPLAY    | 1.00 | 0.015 | 150 | 0.000 | 0 | 0 |
| 44 | PRECOMMIT | 1.00 | 0.241 | 23  | 0.000 | 0 | 0 |
| 44 | REPLAY    | 0.00 | 0.017 | 150 | 0.000 | 0 | 0 |

**The tell**: `n_wrong_target_total == 0` **and** `n_correct_target_total == 0` in
**every one of the 6 cells** — 900 real navigation ticks (`_env_step` genuinely calls
`agent.select_action()` → `env.step()` every tick), zero target-consumption events of
either kind, anywhere. `wrong_target_rate_conditioned = 0.000` is not "zero errors out of
many successes" — it is a 0/0 denominator silently rendered as `0.0`
(`n_wrong_target_intact / n_intact if n_intact > 0 else 0.0` guards only the *conditioned*
denominator against zero *intact* ticks, not against the underlying consumption count
being zero). **The decisive leg (c) never had a chance to move in either direction.**

ARM_REPLAY shows rule intact (drift at floor, ~0.015–0.017 < 0.05 threshold) with zero
wrong-target selection — consistent with either genuine protection or (per the tell
above) simply no consumption events to select wrongly. ARM_PRECOMMIT shows rule *not*
intact (drift 0.21–0.24, above floor) yet **still zero wrong-target selections** — i.e.
the agent's target-selection behaviour is identically inert (zero events) regardless of
whether its rule representation itself is degrading. That is the opposite of what a
"legs covary" reading implies (legs covarying would mean both track together in a
meaningful way); here leg (c) simply never fires.

**Failed criterion**: none of the load-bearing legs failed in the sense of measuring a
genuine null — leg (a) varies (0.00/1.00 across seeds), leg (b) varies clearly (0.015 vs
0.22+), leg (c) is flat at 0.000 with a zero-event denominator throughout.

## 3. Claim-layer mapping

**MECH-467** (`attention.distractor_failure_mode_dissociation`, candidate): asserts three
dissociable distractor-failure modes — sensory capture, rule corruption, behavioural
capture (rule survives, action doesn't) — and that REE's existing evidence covers rule
corruption only. This run is the pre-registered falsifier for legs 1 and 3 specifically.

The claim's own pre-registered **non-degeneracy guard** (claims.yaml notes, verbatim):
"the distractor must actually be REGISTERED by the system — non-zero sensory-capture rate
in at least one arm. A distractor the agent never encodes tests nothing, and an all-floor
battery self-routes substrate_not_ready rather than returning a verdict." This guard
checks leg (a) only. **There is no equivalent floor requiring that leg (c)'s underlying
event (a target-consumption tick, correct or incorrect) actually occur at least once.**
The run's own `criteria_non_degenerate` block (`sensory_capture_registered`,
`any_leg_moves`, `conditioning_non_vacuous`) checks that *some* leg varies across
seeds/arms and that rule-intact conditioning discriminates ticks — neither check catches
a leg whose own numerator-and-denominator are both zero throughout.

**Did the test let the claim express itself?** No, not for leg (c) specifically. Legs (a)
and (b) were fairly tested (both are richly informative: sensory capture varies across
seeds, rule drift clearly discriminates PRECOMMIT from REPLAY). Leg (c) — the leg the
claim's own author notes call "the one that matters most, because it is precisely the
failure rule-state protection cannot catch by construction" — never had a chance to
express anything.

## 4. Biological-reference triage

The predicted phenomenon (behavioural capture despite intact rule representation) has
real precedent in attention/action-selection literature: goal-directed reaching/foraging
tasks routinely show "looking is not choosing" dissociations where gaze/salience capture
by a task-irrelevant but physically salient cue does not always translate into an
erroneous motor commitment, and the reverse (behavioural capture despite verified correct
task-set) is the classic signature the claim is chasing. Nothing in the biological
reference predicts *zero* completed approach-and-consume events over 900 real ticks in a
10×10 grid with 4–5 resources and no hazards — that is a testbed/behavioural-completion
problem, not a biological question.

**Root cause (structural, not a discovered biological mismatch)**: both included arms are
explicitly *internal, non-committed* cognitive states (`internal_planning`,
`internal_replay`) — chosen specifically because "the substrate cannot currently sustain
multi-step commitment yet," the same reasoning that excluded the third (committed) arm.
That same substrate limitation plausibly starves the *included* arms of any completed
approach-and-consume sequence: without sustained multi-step commitment, 150 ticks of
internal deliberation/replay-flavoured action selection may simply never complete a
full approach to either resource. This is the design's own excluded-arm rationale
re-appearing, unacknowledged, inside the two arms that were supposed to be safe from it.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (leg c only) | legs (a)/(b) fairly tested and informative; leg (c) never exercised |
| Biological reference | clear | behavioural-capture-despite-intact-rule is a real, well-motivated phenomenon; the gap is testbed completion, not biology |
| Developmental / dependency prerequisites | present | MECH-262, SD-033a, MECH-261, MECH-254 all V3-implemented; not a missing-prerequisite story |
| Implementation completeness | adequate for legs (a)/(b) | telemetry reused correctly (SD-049 field view, SD-033a rule_state, SD-049 consumed-tag) |
| Environment adequacy | inadequate for leg (c) specifically | 10x10 grid / 150-tick eval window under internal-only operating modes produces zero consumption events in every one of 6 cells |
| Measurement adequacy | inadequate for leg (c) | 0/0 denominator rendered as a clean 0.000 rate; the claim's own non-degeneracy guard checks leg (a) but not leg (c)'s event floor |
| Integration adequacy | isolated | the gap is specific to whether committed approach-and-consume completes; sensory/rule telemetry is unaffected |
| Scale / capacity | likely insufficient | 150 ticks in two non-committed operating modes appears to be below the volume needed for even one full approach-and-consume; untested whether a longer budget or larger resource density would clear it |

## 6. Learning extracted

1. Leg (c) (wrong-target selection) has a **0/0 event denominator in all 6 cells** — the
   decisive leg for MECH-467's core prediction never fired, in either direction.
2. This is the same substrate limitation (no sustained multi-step commitment) that
   justified excluding the third arm, re-appearing inside the two *included* arms: without
   commitment, target-consumption events may not complete at all within budget.
3. The claim's own pre-registered non-degeneracy guard checks leg (a) (distractor
   registered) but has no equivalent floor for leg (c) (at least one consumption event,
   correct or incorrect, must occur) — a genuine gap in the falsifier's own design, not
   just an unlucky run.
4. Legs (a) and (b) were fairly and informatively tested and should not be discarded —
   sensory capture and rule-drift dissociate cleanly between arms exactly as the
   substrate's existing rule-corruption evidence would predict.
5. No prior autopsy target exists for MECH-467 (checked via
   `granularity_debt_cluster.py`-equivalent grep of `claim_ids`) — this is its first, so
   no recurrence/granularity signal to report yet.
6. Re-derive brake: 0 prior `substrate_ceiling` hits for MECH-467. Does not fire.

## 7. Repair pathway (user-confirmed 2026-08-03)

**Reclassify away from `does_not_support`.** The manifest's self-routed label
(`legs_covary_no_dissociation`) presumes all three legs were genuinely measured; leg (c)
was not. Recommend `non_contributory` (per-claim), specifically for the reason "leg (c)
structurally unmeasurable under the two included operating-mode arms at this budget/grid
size" — not a real null result against MECH-467.

**Recommended `evidence_quality_note`** (MECH-467, verbatim for governance to apply):

> 2026-08-03 (governance, V3-EXQ-874, confirmed `failure_autopsy_V3-EXQ-874_2026-08-03`):
> legs (a) sensory-capture and (b) rule-drift were fairly and informatively tested (clear
> dissociation between ARM_PRECOMMIT drift ~0.22 and ARM_REPLAY drift ~0.015). Leg (c)
> (conditioned wrong-target selection) has a 0/0 event denominator in all 6 cells (3
> seeds x 2 arms) — zero target-consumption events of either kind occurred across 900
> real navigation ticks. This is not a measured null; it is the decisive leg never firing,
> plausibly because both included operating modes (internal_planning, internal_replay)
> are the same non-committed cognitive states whose lack of sustained multi-step
> commitment already justified excluding the third arm. Reclassified `non_contributory`
> (not `does_not_support`) pending a redesign that can actually produce consumption
> events. MECH-467 stays `candidate`, unresolved on leg (c); legs (a)/(b) results stand as
> reported. Routing: `/queue-experiment` for a redesign (larger eval budget and/or denser
> resource placement, or a short bounded-commitment sub-arm within existing substrate
> limits) that clears a consumption-event floor before scoring leg (c).

**Routing: `/queue-experiment`**, a redesign (new letter, e.g. V3-EXQ-874b) — not
`/implement-substrate` (no missing mechanism is implicated; the existing telemetry and
mechanisms are adequate, the *task parameters* under-power leg (c)) and not a straight
re-run (a same-parameter re-run would very likely reproduce the same zero-event outcome).
Concretely: either (i) lengthen `N_EVAL_STEPS` and/or shrink the grid so approach-and-
consume reliably completes within budget under internal-only operating modes, or (ii) add
a short, tightly bounded "commit-then-immediately-release" sub-window that does not
require *sustained* multi-step commitment (only a single completed approach) — consistent
with the existing containment rule (no new attention module, no dependence on stable
multi-step commitment).

**Also recommend**: add a non-degeneracy guard to MECH-467's own claims.yaml notes (or the
next redesign's pre-registration) requiring `n_wrong_target_total + n_correct_target_total
> 0` in at least one arm before leg (c) is scored — closing the gap the existing guard
(leg (a) only) left open.

**Step 9b (hypothesis-space ledger)**: skipped. Lone non-fan-out FAIL; no existing
question in `hypothesis_space_registry.v1.json` references MECH-467 (checked: 0/22
questions).
