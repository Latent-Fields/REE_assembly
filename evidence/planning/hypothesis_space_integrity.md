# Hypothesis-Space Integrity Audit (anti-Goodhart)

Generated: 2026-08-03T12:15:04Z

GENERATED FILE -- do not edit by hand. Advisory, non-blocking sibling of `check_closure_drift.py`. It audits `hypothesis_space_registry.v1.json` + `hypothesis_space_timeseries.v1.jsonl` for the four ways the Narrow/Decide dashboard could be gamed (design rule 5). Flags are review hints, never a gate. LABELLED GOV-FANOUT-1 growth of an existing question is reported separately as advisory (see the final section) rather than counted as a bucket-(b) violation.

Audited **24** open question(s) across **16** time-series snapshot(s). **2** flag(s) raised, **27** advisory note(s), **16** git-witnessed pre-registration(s), **0** unverifiable, **1** fan-out recurrence overlay(s), **0** discovery-growth note(s), **0** discovery-recurrence overlay(s).

## (a) Un-backed surviving-count drop (0)

_A question's surviving count fell with no adjudicated `weakens`/discrimination behind the elimination._

_None._

## (b) Post-hoc enlargement of a frozen set (2)

_The frozen initial enumeration grew WITHOUT a valid labelled fan-out record, or a hypothesis was pre-registered after its own adjudicating run. Labelled GOV-FANOUT-1 growth is NOT counted here -- see the advisory section below._

- `inv088_evaluator_degeneracy_cause` fan-out failure_autopsy_V3-EXQ-108b_2026-08-03.json: condition (a) unmet for H-dynamics-collapse (adjudicating run already RESOLVED when the leg was added; `failure_autopsy_V3-EXQ-108b_2026-08-03.json` was committed 2026-08-03, AFTER resolution 2026-08-02 -- self-reported pre_registered_utc 2026-08-02 is unwitnessed) -- a leg added by fan-out must pre-date the run that adjudicates it.
- `inv088_evaluator_degeneracy_cause`: grew 2 -> 3 (+1) but only 0 leg(s) are covered by a valid fanout_growth_events/discovery_growth_events entry -- 1 unaccounted, which is post-hoc enlargement.

## (c) Confirmed without a passed control (0)

_A `confirmed` hypothesis lacks control_passed == true._

_None._

## (d) Elimination-bar violation (0)

_An `eliminated`/`split` hypothesis is missing part of the bar (met_elimination_bar + control_passed + non_degenerate)._

_None._

## Advisory -- labelled fan-out growth (27, NOT violations)

_An existing question's hypothesis set grew because a GOV-FANOUT-1 discrimination portfolio enumerated new rival explanations as earlier axes were eliminated. This is permitted when the growth satisfies (a) each new leg pre-dates its adjudicating run, (b) it is recorded in `fanout_growth_events[]` naming the autopsy that opened the portfolio, and (c) `initial_frozen_count_at_registration` is preserved. These are LABELLED, not flagged._

**Read these alongside the convergence class, not as an all-clear.** The denominator grows mostly by legs that are then eliminated, which inflates the headline narrowing ratio -- so the dashboard reports surviving/original AND surviving/current-including-fan-out. But growth alone does NOT mean a campaign is failing: the axis-family discriminator (`convergence.convergence_class` in `hypothesis_space.v1.json`) separates **refining** (an axis family was closed out and the survivors sit on fresh territory -- count grows while the KIND of answer narrows) from **circling** (new legs re-enter already-eliminated families, the leg-level analogue of the re-derive brake) and **scattering** (nothing ever closed). Cite the class when you report growth.

- `competence_floor`: +3 leg(s) (H1-drive-schedule, H2-reward-coupling, H3-credit-horizon) added by labelled fan-out from `failure_autopsy_V3-EXQ-769_2026-07-17.json` -- conditions (a)-(c) satisfied, advisory not a violation.
- `competence_floor`: +2 leg(s) (H-bc-prior, H-approach-primitive) added by labelled fan-out from `failure_autopsy_MECH-457-fanout-770-771-772_2026-07-18.json` -- conditions (a)-(c) satisfied, advisory not a violation.
- `competence_floor`: +4 leg(s) (H-retention-critic, H-retention-consolidation, H-retention-auxiliary-decay, H-consummation-binding) added by labelled fan-out from `mech457_retention_portfolio_2026-07-18.md` -- conditions (a)-(c) satisfied, advisory not a violation.
- `competence_floor`: +1 leg(s) (H-zworld-trained-instrument) added by labelled fan-out from `failure_autopsy_batch-793a-817-819_2026-07-26.json` -- conditions (a)-(c) satisfied, advisory not a violation.
- `competence_floor`: +1 leg(s) (H-mech475-baseline-reversal) added by labelled fan-out from `failure_autopsy_mech476-mech475-cluster_2026-07-29.json` -- conditions (a)-(c) satisfied, advisory not a violation.
- `competence_floor`: +1 leg(s) (H-mech476-dose-response) added by labelled fan-out from `failure_autopsy_mech476-mech475-cluster_2026-07-29.json` -- conditions (a)-(c) satisfied, advisory not a violation.
- `competence_floor`: +1 leg(s) (H-mech476-novelty-tagging) added by labelled fan-out from `failure_autopsy_mech476-mech475-cluster_2026-07-29.json` -- conditions (a)-(c) satisfied, advisory not a violation.
- `competence_floor`: denominator grew 7 -> 20 across 5 labelled event(s) (fan-out + discovery). Legitimate; report the reduction ratio BOTH ways. Whether this growth is REFINEMENT (a family closed, survivors on fresh territory) or CIRCLING (re-entry into already-eliminated territory) is decided by the axis-family discriminator -- read `convergence.convergence_class` for this question in hypothesis_space.v1.json rather than assuming either.
- `conversion_ceiling_root`: +1 leg(s) (H-objective-misspecification) added by labelled fan-out from `failure_autopsy_competence-objective-cluster-734-737b-742a_2026-07-22.json` -- conditions (a)-(c) satisfied, advisory not a violation.
- `conversion_ceiling_root`: +1 leg(s) (H-observation-interface) added by labelled fan-out from `failure_autopsy_backlog_2026-07-24.json` -- conditions (a)-(c) satisfied, advisory not a violation.
- `conversion_ceiling_root`: denominator grew 4 -> 6 across 2 labelled event(s) (fan-out + discovery). Legitimate; report the reduction ratio BOTH ways. Whether this growth is REFINEMENT (a family closed, survivors on fresh territory) or CIRCLING (re-entry into already-eliminated territory) is decided by the axis-family discriminator -- read `convergence.convergence_class` for this question in hypothesis_space.v1.json rather than assuming either.
- `arousal-variance-amplifier`: +1 leg(s) (H-arousal-channel-agnostic) added by labelled fan-out from `failure_autopsy_V3-EXQ-785_2026-07-19.json` -- conditions (a)-(c) satisfied, advisory not a violation.
- `arousal-variance-amplifier`: denominator grew 3 -> 4 across 1 labelled event(s) (fan-out + discovery). Legitimate; report the reduction ratio BOTH ways. Whether this growth is REFINEMENT (a family closed, survivors on fresh territory) or CIRCLING (re-entry into already-eliminated territory) is decided by the axis-family discriminator -- read `convergence.convergence_class` for this question in hypothesis_space.v1.json rather than assuming either.
- `policy_decomposition_discrimination`: +2 leg(s) (H-representation-axis, H-algorithm-axis) added by labelled fan-out from `failure_autopsy_2026-07-28-sweep.json` -- conditions (a)-(c) satisfied, advisory not a violation.
- `policy_decomposition_discrimination`: denominator grew 4 -> 6 across 1 labelled event(s) (fan-out + discovery). Legitimate; report the reduction ratio BOTH ways. Whether this growth is REFINEMENT (a family closed, survivors on fresh territory) or CIRCLING (re-entry into already-eliminated territory) is decided by the axis-family discriminator -- read `convergence.convergence_class` for this question in hypothesis_space.v1.json rather than assuming either.
- time series 2026-07-17 -> 2026-07-18: total_initial grew by 16, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 16 leg(s)) -- advisory, not a violation.
- time series 2026-07-18 -> 2026-07-19: total_initial grew by 7, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 7 leg(s)) -- advisory, not a violation.
- time series 2026-07-19 -> 2026-07-20: total_initial grew by 4, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 4 leg(s)) -- advisory, not a violation.
- time series 2026-07-21 -> 2026-07-22: total_initial grew by 1, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 1 leg(s)) -- advisory, not a violation.
- time series 2026-07-22 -> 2026-07-24: total_initial grew by 1, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 1 leg(s)) -- advisory, not a violation.
- time series 2026-07-25 -> 2026-07-26: total_initial grew by 5, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 5 leg(s)) -- advisory, not a violation.
- time series 2026-07-26 -> 2026-07-28: total_initial grew by 2, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 2 leg(s)) -- advisory, not a violation.
- time series 2026-07-28 -> 2026-07-29: total_initial grew by 9, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 9 leg(s)) -- advisory, not a violation.
- time series 2026-07-30 -> 2026-07-31: total_initial grew by 2, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 2 leg(s)) -- advisory, not a violation.
- time series 2026-07-31 -> 2026-08-01: total_initial grew by 3, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 3 leg(s)) -- advisory, not a violation.
- time series 2026-08-01 -> 2026-08-02: total_initial grew by 6, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 6 leg(s)) -- advisory, not a violation.
- time series 2026-08-02 -> 2026-08-03: total_initial grew by 10, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 10 leg(s)) -- advisory, not a violation.

## Advisory -- surviving-count drop backed by confirmation (0 backed, 1 unverifiable, NOT violations)

_A `confirmed` resolution (supports + control_passed) also legitimately removes a hypothesis from `surviving`, exactly like an elimination does -- `surviving` counts alive legs, so an alive -> confirmed transition drops the total with no elimination behind it. `total_confirmed` (build_hypothesis_space.py, added 2026-08-02) lets this check credit that instead of reading the drop as unbacked. A snapshot pair predating the field is UNVERIFIABLE, not a violation -- same quiet-on-insufficient-data design as the git-witness provenance check below._

**Unverifiable (quiet -- total_confirmed absent from one or both snapshots):**

- time series 2026-07-29 -> 2026-07-30: surviving fell by 1 with no rise in resolved_out, but total_confirmed is absent from one or both snapshots (predates the field) so a confirmation-explained drop cannot be ruled out -- unverifiable, not a violation.

## Fan-out recurrence (ACTIONABLE, 1) -- N >= 3 portfolios on one question

_GOV-FROZEN-1 escalation clause. Conditions (a)-(c) license an INDIVIDUAL growth event, so they say nothing about recurrence: a question can fan out indefinitely, clearing every check every time, while its denominator outruns its eliminations. Every portfolio counted below was individually legitimate -- **the recurrence is the signal**, and the reading is that the question may be MIS-POSED rather than under-enumerated._

_Complementary to GOV-DIAG-1, not redundant with it: that rule counts pure-diagnostic NO-VERDICT chains, whereas fan-out recurrence is the opposite signature -- every run reached a verdict and eliminated a leg. A campaign can hold perfect GOV-DIAG-1 hygiene and still never converge._

**Response is routing, not demotion.** These are questions, not claims; nothing is promoted or demoted. Re-pose the operationalization before opening another portfolio -- enumerating a further round of rivals on an unchanged framing is the denominator-side twin of re-running a braked experiment harder. Warn-only: this never gates a cycle.

- `competence_floor`: 5 distinct labelled fan-out portfolios (>= N=3); denominator 7 -> 20, 0 leg(s) still alive. Each portfolio cleared conditions (a)-(c) individually -- the RECURRENCE is the signal. Reading: the question may be MIS-POSED rather than under-enumerated. Re-pose the operationalization before opening portfolio 6; enumerating another round of rivals on an unchanged framing is the denominator-side twin of re-running a braked experiment harder. Sources: `failure_autopsy_MECH-457-fanout-770-771-772_2026-07-18.json`, `failure_autopsy_V3-EXQ-769_2026-07-17.json`, `failure_autopsy_batch-793a-817-819_2026-07-26.json`, `failure_autopsy_mech476-mech475-cluster_2026-07-29.json`, `mech457_retention_portfolio_2026-07-18.md`

## Advisory -- labelled discovery growth (0, NOT violations)

_An existing question's hypothesis set grew because a genuinely serendipitous explanation was found DURING the same analysis that resolves it -- discovered while explaining away already-pre-registered rivals, never anticipated beforehand. This is DIFFERENT from labelled fan-out growth above: by construction no artifact can pre-date a discovery made by the very run that reveals it, so this path does not require (and cannot honestly satisfy) the pre-dates-the-run witness fan-out growth needs. It is permitted instead when (i) the hypothesis is born already resolved in the same edit (never left `alive`), (ii) it is recorded in `discovery_growth_events[]` naming the discovering-and-resolving autopsy plus a `rationale` grounding why this is principled abduction and not motivated post-hoc reasoning, and (iii) `initial_frozen_count_at_registration` is preserved. These are LABELLED, not flagged._

**A hypothesis left `alive` never qualifies here.** If a leg is not resolved in the same edit, it needed Mode A pre-registration BEFORE its adjudicating run instead -- back-dating `pre_registered_utc` to make an actually-anticipated rival look like a discovery is exactly the (b) violation this ledger polices, whichever door it is walked through.

_None._

## Discovery-growth recurrence (ACTIONABLE, 0) -- N >= 3 discovery events on one question

_Mirrors the fan-out recurrence overlay above, for the discovery-growth path. Every event counted below was individually legitimate -- **the recurrence is the signal**: a question racking up repeated 'discoveries' may be using this path as a substitute for pre-registration discipline (an actually-anticipated rival hypothesis being called a discovery each time to dodge Mode A) rather than genuine one-off serendipity. Response is routing -- check whether the next candidate explanation was really unforeseeable before treating it as another discovery. Warn-only: this never gates a cycle._

_None._

## Pre-registration provenance (16 witnessed, 0 unverifiable)

_`pre_registered_utc` is SELF-REPORTED and written into the registry after the fact, so the pre <= resolved invariant is trivially satisfiable by back-dating -- no audit reading only the registry can detect that. A fan-out leg whose adjudicating run had ALREADY RESOLVED when it was added therefore clears only on **git-witnessed** provenance: its `pre_registration_source` artifact (or its own registry entry) must have been durably committed before the run resolved. The honest case self-clears with no human adjudication; a back-dated one cannot manufacture a commit._

**Witnessed (cleared on evidence):**

- `competence_floor`/`H1-drive-schedule`: `failure_autopsy_V3-EXQ-769_2026-07-17.json` committed 2026-07-17 <= resolution 2026-07-17
- `competence_floor`/`H2-reward-coupling`: `failure_autopsy_V3-EXQ-769_2026-07-17.json` committed 2026-07-17 <= resolution 2026-07-18
- `competence_floor`/`H3-credit-horizon`: `failure_autopsy_V3-EXQ-769_2026-07-17.json` committed 2026-07-17 <= resolution 2026-07-17
- `competence_floor`/`H-bc-prior`: `failure_autopsy_MECH-457-fanout-770-771-772_2026-07-18.json` committed 2026-07-18 <= resolution 2026-07-18
- `competence_floor`/`H-approach-primitive`: `failure_autopsy_MECH-457-fanout-770-771-772_2026-07-18.json` committed 2026-07-18 <= resolution 2026-07-18
- `competence_floor`/`H-retention-critic`: `mech457_retention_portfolio_2026-07-18.md` committed 2026-07-18 <= resolution 2026-07-19
- `competence_floor`/`H-retention-consolidation`: `mech457_retention_portfolio_2026-07-18.md` committed 2026-07-18 <= resolution 2026-07-22
- `competence_floor`/`H-retention-auxiliary-decay`: `mech457_retention_portfolio_2026-07-18.md` committed 2026-07-18 <= resolution 2026-07-20
- `competence_floor`/`H-consummation-binding`: `mech457_retention_portfolio_2026-07-18.md` committed 2026-07-18 <= resolution 2026-07-25
- `competence_floor`/`H-zworld-trained-instrument`: `failure_autopsy_batch-793a-817-819_2026-07-26.json` committed 2026-07-26 <= resolution 2026-07-27
- `competence_floor`/`H-mech475-baseline-reversal`: `failure_autopsy_mech476-mech475-cluster_2026-07-29.json` committed 2026-07-29 <= resolution 2026-07-29
- `competence_floor`/`H-mech476-dose-response`: `failure_autopsy_mech476-mech475-cluster_2026-07-29.json` committed 2026-07-29 <= resolution 2026-08-01
- `competence_floor`/`H-mech476-novelty-tagging`: `failure_autopsy_mech476-mech475-cluster_2026-07-29.json` committed 2026-07-29 <= resolution 2026-08-01
- `conversion_ceiling_root`/`H-objective-misspecification`: `failure_autopsy_competence-objective-cluster-734-737b-742a_2026-07-22.json` committed 2026-07-22 <= resolution 2026-07-24
- `conversion_ceiling_root`/`H-observation-interface`: `failure_autopsy_backlog_2026-07-24.json` committed 2026-07-24 <= resolution 2026-07-24
- `arousal-variance-amplifier`/`H-arousal-channel-agnostic`: `failure_autopsy_V3-EXQ-785_2026-07-19.json` committed 2026-07-19 <= resolution 2026-07-19

---

This audit promotes/demotes nothing. Response to any flag is a human decision at governance (the same handling as `check_closure_drift.py`). Advisory labelled-growth notes need no action -- but a question accumulating them is one whose campaign has not converged.

