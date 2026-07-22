# Hypothesis-Space Integrity Audit (anti-Goodhart)

Generated: 2026-07-22T04:02:38Z

GENERATED FILE -- do not edit by hand. Advisory, non-blocking sibling of `check_closure_drift.py`. It audits `hypothesis_space_registry.v1.json` + `hypothesis_space_timeseries.v1.jsonl` for the four ways the Narrow/Decide dashboard could be gamed (design rule 5). Flags are review hints, never a gate. LABELLED GOV-FANOUT-1 growth of an existing question is reported separately as advisory (see the final section) rather than counted as a bucket-(b) violation.

Audited **11** open question(s) across **6** time-series snapshot(s). **0** flag(s) raised, **12** advisory note(s), **7** git-witnessed pre-registration(s), **0** unverifiable, **1** fan-out recurrence overlay(s).

## (a) Un-backed surviving-count drop (0)

_A question's surviving count fell with no adjudicated `weakens`/discrimination behind the elimination._

_None._

## (b) Post-hoc enlargement of a frozen set (0)

_The frozen initial enumeration grew WITHOUT a valid labelled fan-out record, or a hypothesis was pre-registered after its own adjudicating run. Labelled GOV-FANOUT-1 growth is NOT counted here -- see the advisory section below._

_None._

## (c) Confirmed without a passed control (0)

_A `confirmed` hypothesis lacks control_passed == true._

_None._

## (d) Elimination-bar violation (0)

_An `eliminated`/`split` hypothesis is missing part of the bar (met_elimination_bar + control_passed + non_degenerate)._

_None._

## Advisory -- labelled fan-out growth (12, NOT violations)

_An existing question's hypothesis set grew because a GOV-FANOUT-1 discrimination portfolio enumerated new rival explanations as earlier axes were eliminated. This is permitted when the growth satisfies (a) each new leg pre-dates its adjudicating run, (b) it is recorded in `fanout_growth_events[]` naming the autopsy that opened the portfolio, and (c) `initial_frozen_count_at_registration` is preserved. These are LABELLED, not flagged._

**Read these alongside the convergence class, not as an all-clear.** The denominator grows mostly by legs that are then eliminated, which inflates the headline narrowing ratio -- so the dashboard reports surviving/original AND surviving/current-including-fan-out. But growth alone does NOT mean a campaign is failing: the axis-family discriminator (`convergence.convergence_class` in `hypothesis_space.v1.json`) separates **refining** (an axis family was closed out and the survivors sit on fresh territory -- count grows while the KIND of answer narrows) from **circling** (new legs re-enter already-eliminated families, the leg-level analogue of the re-derive brake) and **scattering** (nothing ever closed). Cite the class when you report growth.

- `competence_floor`: +3 leg(s) (H1-drive-schedule, H2-reward-coupling, H3-credit-horizon) added by labelled fan-out from `failure_autopsy_V3-EXQ-769_2026-07-17.json` -- conditions (a)-(c) satisfied, advisory not a violation.
- `competence_floor`: +2 leg(s) (H-bc-prior, H-approach-primitive) added by labelled fan-out from `failure_autopsy_MECH-457-fanout-770-771-772_2026-07-18.json` -- conditions (a)-(c) satisfied, advisory not a violation.
- `competence_floor`: +4 leg(s) (H-retention-critic, H-retention-consolidation, H-retention-auxiliary-decay, H-consummation-binding) added by labelled fan-out from `mech457_retention_portfolio_2026-07-18.md` -- conditions (a)-(c) satisfied, advisory not a violation.
- `competence_floor`: denominator grew 7 -> 16 across 3 labelled portfolio(s). Legitimate; report the reduction ratio BOTH ways. Whether this growth is REFINEMENT (a family closed, survivors on fresh territory) or CIRCLING (re-entry into already-eliminated territory) is decided by the axis-family discriminator -- read `convergence.convergence_class` for this question in hypothesis_space.v1.json rather than assuming either.
- `conversion_ceiling_root`: +1 leg(s) (H-objective-misspecification) added by labelled fan-out from `failure_autopsy_competence-objective-cluster-734-737b-742a_2026-07-22.json` -- conditions (a)-(c) satisfied, advisory not a violation.
- `conversion_ceiling_root`: denominator grew 4 -> 5 across 1 labelled portfolio(s). Legitimate; report the reduction ratio BOTH ways. Whether this growth is REFINEMENT (a family closed, survivors on fresh territory) or CIRCLING (re-entry into already-eliminated territory) is decided by the axis-family discriminator -- read `convergence.convergence_class` for this question in hypothesis_space.v1.json rather than assuming either.
- `arousal-variance-amplifier`: +1 leg(s) (H-arousal-channel-agnostic) added by labelled fan-out from `failure_autopsy_V3-EXQ-785_2026-07-19.json` -- conditions (a)-(c) satisfied, advisory not a violation.
- `arousal-variance-amplifier`: denominator grew 3 -> 4 across 1 labelled portfolio(s). Legitimate; report the reduction ratio BOTH ways. Whether this growth is REFINEMENT (a family closed, survivors on fresh territory) or CIRCLING (re-entry into already-eliminated territory) is decided by the axis-family discriminator -- read `convergence.convergence_class` for this question in hypothesis_space.v1.json rather than assuming either.
- time series 2026-07-17 -> 2026-07-18: total_initial grew by 16, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 16 leg(s)) -- advisory, not a violation.
- time series 2026-07-18 -> 2026-07-19: total_initial grew by 7, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 7 leg(s)) -- advisory, not a violation.
- time series 2026-07-19 -> 2026-07-20: total_initial grew by 4, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 4 leg(s)) -- advisory, not a violation.
- time series 2026-07-21 -> 2026-07-22: total_initial grew by 1, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 1 leg(s)) -- advisory, not a violation.

## Fan-out recurrence (ACTIONABLE, 1) -- N >= 3 portfolios on one question

_GOV-FROZEN-1 escalation clause. Conditions (a)-(c) license an INDIVIDUAL growth event, so they say nothing about recurrence: a question can fan out indefinitely, clearing every check every time, while its denominator outruns its eliminations. Every portfolio counted below was individually legitimate -- **the recurrence is the signal**, and the reading is that the question may be MIS-POSED rather than under-enumerated._

_Complementary to GOV-DIAG-1, not redundant with it: that rule counts pure-diagnostic NO-VERDICT chains, whereas fan-out recurrence is the opposite signature -- every run reached a verdict and eliminated a leg. A campaign can hold perfect GOV-DIAG-1 hygiene and still never converge._

**Response is routing, not demotion.** These are questions, not claims; nothing is promoted or demoted. Re-pose the operationalization before opening another portfolio -- enumerating a further round of rivals on an unchanged framing is the denominator-side twin of re-running a braked experiment harder. Warn-only: this never gates a cycle.

- `competence_floor`: 3 distinct labelled fan-out portfolios (>= N=3); denominator 7 -> 16, 3 leg(s) still alive. Each portfolio cleared conditions (a)-(c) individually -- the RECURRENCE is the signal. Reading: the question may be MIS-POSED rather than under-enumerated. Re-pose the operationalization before opening portfolio 4; enumerating another round of rivals on an unchanged framing is the denominator-side twin of re-running a braked experiment harder. Sources: `failure_autopsy_MECH-457-fanout-770-771-772_2026-07-18.json`, `failure_autopsy_V3-EXQ-769_2026-07-17.json`, `mech457_retention_portfolio_2026-07-18.md`

## Pre-registration provenance (7 witnessed, 0 unverifiable)

_`pre_registered_utc` is SELF-REPORTED and written into the registry after the fact, so the pre <= resolved invariant is trivially satisfiable by back-dating -- no audit reading only the registry can detect that. A fan-out leg whose adjudicating run had ALREADY RESOLVED when it was added therefore clears only on **git-witnessed** provenance: its `pre_registration_source` artifact (or its own registry entry) must have been durably committed before the run resolved. The honest case self-clears with no human adjudication; a back-dated one cannot manufacture a commit._

**Witnessed (cleared on evidence):**

- `competence_floor`/`H1-drive-schedule`: `failure_autopsy_V3-EXQ-769_2026-07-17.json` committed 2026-07-17 <= resolution 2026-07-17
- `competence_floor`/`H2-reward-coupling`: `failure_autopsy_V3-EXQ-769_2026-07-17.json` committed 2026-07-17 <= resolution 2026-07-18
- `competence_floor`/`H3-credit-horizon`: `failure_autopsy_V3-EXQ-769_2026-07-17.json` committed 2026-07-17 <= resolution 2026-07-17
- `competence_floor`/`H-bc-prior`: `failure_autopsy_MECH-457-fanout-770-771-772_2026-07-18.json` committed 2026-07-18 <= resolution 2026-07-18
- `competence_floor`/`H-approach-primitive`: `failure_autopsy_MECH-457-fanout-770-771-772_2026-07-18.json` committed 2026-07-18 <= resolution 2026-07-18
- `competence_floor`/`H-retention-auxiliary-decay`: `mech457_retention_portfolio_2026-07-18.md` committed 2026-07-18 <= resolution 2026-07-20
- `arousal-variance-amplifier`/`H-arousal-channel-agnostic`: `failure_autopsy_V3-EXQ-785_2026-07-19.json` committed 2026-07-19 <= resolution 2026-07-19

---

This audit promotes/demotes nothing. Response to any flag is a human decision at governance (the same handling as `check_closure_drift.py`). Advisory labelled-growth notes need no action -- but a question accumulating them is one whose campaign has not converged.

