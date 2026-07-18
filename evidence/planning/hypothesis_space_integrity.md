# Hypothesis-Space Integrity Audit (anti-Goodhart)

Generated: 2026-07-18T07:11:30Z

GENERATED FILE -- do not edit by hand. Advisory, non-blocking sibling of `check_closure_drift.py`. It audits `hypothesis_space_registry.v1.json` + `hypothesis_space_timeseries.v1.jsonl` for the four ways the Narrow/Decide dashboard could be gamed (design rule 5). Flags are review hints, never a gate. LABELLED GOV-FANOUT-1 growth of an existing question is reported separately as advisory (see the final section) rather than counted as a bucket-(b) violation.

Audited **6** open question(s) across **2** time-series snapshot(s). **0** flag(s) raised, **4** advisory note(s).

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

## Advisory -- labelled fan-out growth (4, NOT violations)

_An existing question's hypothesis set grew because a GOV-FANOUT-1 discrimination portfolio enumerated new rival explanations as earlier axes were eliminated. This is permitted when the growth satisfies (a) each new leg pre-dates its adjudicating run, (b) it is recorded in `fanout_growth_events[]` naming the autopsy that opened the portfolio, and (c) `initial_frozen_count_at_registration` is preserved. These are LABELLED, not flagged._

**Read these as a convergence signal, not an all-clear.** The denominator grows mostly by legs that are then eliminated, which makes the headline narrowing ratio look strongest exactly when a campaign is failing to converge and having to invent new candidate explanations. The dashboard reports surviving/original AND surviving/current-including-fan-out for this reason.

- `competence_floor`: +3 leg(s) (H1-drive-schedule, H2-reward-coupling, H3-credit-horizon) added by labelled fan-out from `failure_autopsy_V3-EXQ-769_2026-07-17.json` -- conditions (a)-(c) satisfied, advisory not a violation.
- `competence_floor`: +2 leg(s) (H-bc-prior, H-approach-primitive) added by labelled fan-out from `failure_autopsy_MECH-457-fanout-770-771-772_2026-07-18.json` -- conditions (a)-(c) satisfied, advisory not a violation.
- `competence_floor`: denominator grew 7 -> 12 across 2 labelled portfolio(s). Legitimate, but report the reduction ratio BOTH ways -- a campaign enumerating new rivals as it eliminates old ones has not converged.
- time series 2026-07-17 -> 2026-07-18: total_initial grew by 5, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 5 leg(s)) -- advisory, not a violation.

---

This audit promotes/demotes nothing. Response to any flag is a human decision at governance (the same handling as `check_closure_drift.py`). Advisory labelled-growth notes need no action -- but a question accumulating them is one whose campaign has not converged.

