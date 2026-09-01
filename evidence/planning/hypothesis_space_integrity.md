# Hypothesis-Space Integrity Audit (anti-Goodhart)

Generated: 2026-09-01T15:54:28Z

GENERATED FILE -- do not edit by hand. Advisory, non-blocking sibling of `check_closure_drift.py`. It audits `hypothesis_space_registry.v1.json` + `hypothesis_space_timeseries.v1.jsonl` for the four ways the Narrow/Decide dashboard could be gamed (design rule 5). Flags are review hints, never a gate. LABELLED GOV-FANOUT-1 growth of an existing question is reported separately as advisory (see the final section) rather than counted as a bucket-(b) violation.

Audited **43** open question(s) across **37** time-series snapshot(s). **0** flag(s) raised, **43** advisory note(s), **18** git-witnessed pre-registration(s), **0** unverifiable, **0** fan-out recurrence overlay(s), **3** discovery-growth note(s), **0** discovery-recurrence overlay(s), **1** acknowledged (worked) recurrence(s).

## (a) Un-backed surviving-count drop (0)

_A question's surviving count fell with no adjudicated `weakens`/discrimination behind the elimination._

_None._

## (b) Post-hoc enlargement of a frozen set (0)

_The frozen initial enumeration grew WITHOUT a valid labelled fan-out record, or a hypothesis was pre-registered after its own adjudicating run. Labelled GOV-FANOUT-1 growth is NOT counted here -- see the advisory section below._

_None._

## (c) Confirmed/superseded without a passed control (0)

_A `confirmed` or `superseded` hypothesis lacks control_passed == true._

_None._

## (d) Elimination-bar violation (0)

_An `eliminated`/`split` hypothesis is missing part of the bar (met_elimination_bar + control_passed + non_degenerate)._

_None._

## Advisory -- labelled fan-out growth (43, NOT violations)

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
- `inv088_evaluator_degeneracy_cause`: +2 leg(s) (H-horizon-compounding, H-action-blindness) added by labelled fan-out from `failure_autopsy_V3-EXQ-954_2026-08-29.json` -- conditions (a)-(c) satisfied, advisory not a violation.
- `inv088_evaluator_degeneracy_cause`: denominator grew 2 -> 5 across 2 labelled event(s) (fan-out + discovery). Legitimate; report the reduction ratio BOTH ways. Whether this growth is REFINEMENT (a family closed, survivors on fresh territory) or CIRCLING (re-entry into already-eliminated territory) is decided by the axis-family discriminator -- read `convergence.convergence_class` for this question in hypothesis_space.v1.json rather than assuming either.
- `e3_fdominance_causal_discrimination`: denominator grew 4 -> 6 across 2 labelled event(s) (fan-out + discovery). Legitimate; report the reduction ratio BOTH ways. Whether this growth is REFINEMENT (a family closed, survivors on fresh territory) or CIRCLING (re-entry into already-eliminated territory) is decided by the axis-family discriminator -- read `convergence.convergence_class` for this question in hypothesis_space.v1.json rather than assuming either.
- `mech266_mode_arbitration_saturation`: +1 leg(s) (H4-clip-not-normalisation) added by labelled fan-out from `failure_autopsy_V3-EXQ-935_2026-08-18.json` -- conditions (a)-(c) satisfied, advisory not a violation.
- `mech266_mode_arbitration_saturation`: denominator grew 3 -> 4 across 1 labelled event(s) (fan-out + discovery). Legitimate; report the reduction ratio BOTH ways. Whether this growth is REFINEMENT (a family closed, survivors on fresh territory) or CIRCLING (re-entry into already-eliminated territory) is decided by the axis-family discriminator -- read `convergence.convergence_class` for this question in hypothesis_space.v1.json rather than assuming either.
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
- time series 2026-08-03 -> 2026-08-05: total_initial grew by 6, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 6 leg(s)) -- advisory, not a violation.
- time series 2026-08-07 -> 2026-08-08: total_initial grew by 6, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 6 leg(s)) -- advisory, not a violation.
- time series 2026-08-10 -> 2026-08-11: total_initial grew by 4, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 4 leg(s)) -- advisory, not a violation.
- time series 2026-08-11 -> 2026-08-12: total_initial grew by 5, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 5 leg(s)) -- advisory, not a violation.
- time series 2026-08-12 -> 2026-08-13: total_initial grew by 3, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 3 leg(s)) -- advisory, not a violation.
- time series 2026-08-13 -> 2026-08-16: total_initial grew by 8, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 8 leg(s)) -- advisory, not a violation.
- time series 2026-08-16 -> 2026-08-17: total_initial grew by 4, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 4 leg(s)) -- advisory, not a violation.
- time series 2026-08-17 -> 2026-08-18: total_initial grew by 2, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 2 leg(s)) -- advisory, not a violation.
- time series 2026-08-20 -> 2026-08-21: total_initial grew by 4, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 4 leg(s)) -- advisory, not a violation.
- time series 2026-08-28 -> 2026-08-29: total_initial grew by 9, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 9 leg(s)) -- advisory, not a violation.
- time series 2026-08-29 -> 2026-08-30: total_initial grew by 5, fully attributed to labelled sources landing in this window (new-question registrations + fanout_growth_events, 5 leg(s)) -- advisory, not a violation.

## Advisory -- surviving-count drop backed by confirmation/supersession (2 backed, 3 unverifiable, NOT violations)

_A `confirmed` resolution (supports + control_passed) or a `superseded` resolution (ratified moot, added 2026-08-19) also legitimately removes a hypothesis from `surviving`, exactly like an elimination does -- `surviving` counts alive legs, so an alive -> confirmed/superseded transition drops the total with no elimination behind it. `total_confirmed` (build_hypothesis_space.py, added 2026-08-02) and `total_superseded` (added 2026-08-19) let this check credit either instead of reading the drop as unbacked. A snapshot pair predating either field is UNVERIFIABLE, not a violation -- same quiet-on-insufficient-data design as the git-witness provenance check below._

**Backed (drop fully explained by a confirmation/supersession):**

- time series 2026-08-19 -> 2026-08-20: surviving fell by 1, backed by 1 newly-confirmed/superseded hypothesis(es) (an adjudicated resolution, not an elimination) -- advisory, not a violation.
- time series 2026-08-23 -> 2026-08-25: surviving fell by 1, backed by 1 newly-confirmed/superseded hypothesis(es) (an adjudicated resolution, not an elimination) -- advisory, not a violation.

**Unverifiable (quiet -- total_confirmed and/or total_superseded absent from one or both snapshots):**

- time series 2026-07-29 -> 2026-07-30: surviving fell by 1 with no rise in resolved_out, but total_confirmed and/or total_superseded is absent from one or both snapshots (predates the field) so a confirmation/supersession-explained drop cannot be ruled out -- unverifiable, not a violation.
- time series 2026-08-05 -> 2026-08-07: surviving fell by 1 with no rise in resolved_out, but total_confirmed and/or total_superseded is absent from one or both snapshots (predates the field) so a confirmation/supersession-explained drop cannot be ruled out -- unverifiable, not a violation.
- time series 2026-08-18 -> 2026-08-19: surviving fell by 1 with no rise in resolved_out, but total_confirmed and/or total_superseded is absent from one or both snapshots (predates the field) so a confirmation/supersession-explained drop cannot be ruled out -- unverifiable, not a violation.

## Fan-out recurrence (ACTIONABLE, 0) -- N >= 3 portfolios on one question

_GOV-FROZEN-1 escalation clause. Conditions (a)-(c) license an INDIVIDUAL growth event, so they say nothing about recurrence: a question can fan out indefinitely, clearing every check every time, while its denominator outruns its eliminations. Every portfolio counted below was individually legitimate -- **the recurrence is the signal**, and the reading is that the question may be MIS-POSED rather than under-enumerated._

_Complementary to GOV-DIAG-1, not redundant with it: that rule counts pure-diagnostic NO-VERDICT chains, whereas fan-out recurrence is the opposite signature -- every run reached a verdict and eliminated a leg. A campaign can hold perfect GOV-DIAG-1 hygiene and still never converge._

**Response is routing, not demotion.** These are questions, not claims; nothing is promoted or demoted. Re-pose the operationalization before opening another portfolio -- enumerating a further round of rivals on an unchanged framing is the denominator-side twin of re-running a braked experiment harder. Warn-only: this never gates a cycle.

**A count of 0 here is NOT the same as 'no recurrence'.** 1 recurrence(s) are ACKNOWLEDGED this cycle and listed in the next section rather than here -- read both before concluding the ledger is quiet.

_None._

## Recurrence acknowledged (1, advisory) -- worked, not live

_A recurrence overlay whose question has since been RE-POSED and formally closed. The portfolio count never decreases (GOV-FROZEN-1 has no shrinkage operation, correctly), so a question that crossed N goes on firing forever -- including long after every leg was resolved and the qid was closed to further growth. Listing those alongside live ones is a duplicate-work generator that fires once per governance cycle per closed campaign, which is the alarm-fatigue Goodhart vector GOV-FROZEN-1 warns about turned on the rule itself. Confirmed: `competence_floor` closed 2026-08-08 and a governance cycle routed a re-pose chip for it on 2026-08-12, four days later._

**Acknowledgement is not suppression.** The line is still emitted, the restriction is quoted verbatim, and the count appears in the summary above and in both ACTIONABLE section headers. Nothing here clears itself silently -- what is withdrawn is the routing, not the record. **Two conditions, both required:** the question carries a non-empty top-level `growth_restriction` (the same field `/failure-autopsy` Step 9b reads before attaching a leg), AND it has zero `alive` legs. Zero-alive alone is deliberately NOT sufficient: a campaign between portfolios legitimately has no live legs, and `competence_floor` sat at 0 alive twice while still live -- twelve hours before it opened portfolio 4 (2026-07-26) and five days before a leg went back alive (2026-08-02).

**Re-read the restriction before treating any new growth on these questions as sanctioned.** A restriction names its own exception conditions; an acknowledged recurrence that starts growing again is a real finding, not a resolved one.

- `competence_floor`: 5 distinct labelled fan-out portfolios (>= N=3); denominator 7 -> 20, 0 leg(s) still alive. **ACKNOWLEDGED (fan-out).** The qid carries a `growth_restriction` closing it to further growth AND no leg is still alive, so this recurrence has been WORKED -- it needs no re-pose routing this cycle. Reported, never suppressed: the count does not decrease and the overlay does not clear itself. Re-read the restriction before treating any new portfolio on this qid as sanctioned. Sources: `failure_autopsy_MECH-457-fanout-770-771-772_2026-07-18.json`, `failure_autopsy_V3-EXQ-769_2026-07-17.json`, `failure_autopsy_batch-793a-817-819_2026-07-26.json`, `failure_autopsy_mech476-mech475-cluster_2026-07-29.json`, `mech457_retention_portfolio_2026-07-18.md`

  Restriction, verbatim:

  > CLOSED TO FURTHER FAN-OUT (2026-08-08, competence_floor_recurrence_repose_2026-08-08.md, chip-20260808-competence-floor-refpose). This qid accumulated 5 labelled GOV-FANOUT-1 portfolios (denominator 7 -> 20) before its own standing rule -- set by competence_floor_reposing_2026-07-19.md section 7, 'if a fifth portfolio is proposed on the retention operationalization, treat the recurrence flag as BLOCKING' -- was checked against a real case. Portfolio 5 (failure_autopsy_mech476-mech475-cluster_2026-07-29) opened three legs squarely in the already-decided 'process' family (MECH-475's own registration text names the SAME uninformative-baseline mechanism the retention decision had just confirmed a fix for) and nothing checked the 07-19 rule against it, because the rule lived only as prose in a planning document, not as anything a future /failure-autopsy Step 9b invocation would read. It converged decisively anyway (both MECH-475 and MECH-476 fully retired within days, on their own pre-registered falsifiers) -- that was the outcome, not a property of the process that produced it. RULE, stated here so the next session finds it in the qid it applies to, not in a fourth separate document: a claim whose depends_on includes MECH-457, MECH-459, MECH-460, MECH-475, or MECH-476, and whose first /failure-autopsy would otherwise grow competence_floor by Step 9b's claims+theme matching, should instead pre-register its OWN qid -- UNLESS the specific mechanism under test targets an axis family this qid's decision block still lists as undecided (there is currently none; every family -- process, constitution, instrumentation, representation, world -- carries a resolved answer). This qid's 20 hypotheses and their resolutions are UNCHANGED by this note (GOV-FROZEN-1 has no shrinkage operation and none is invoked); what changes is that this qid should not receive hypothesis #21 onward. The one still-alive leg, H-consummation-binding, is not an exception -- it is complicated (buildable) work (a probe-function fix + one calibrated re-run; see decision.observation_bottleneck), not a discrimination, so it does not need or license a sixth portfolio. Recommended follow-on (not started by this session, per scope discipline): teach /failure-autopsy Step 9b to read a target qid's growth_restriction before Mode A/B registration and surface it to the user at the Step 8 gate rather than silently growing the qid.

## Advisory -- labelled discovery growth (3, NOT violations)

_An existing question's hypothesis set grew because a genuinely serendipitous explanation was found DURING the same analysis that resolves it -- discovered while explaining away already-pre-registered rivals, never anticipated beforehand. This is DIFFERENT from labelled fan-out growth above: by construction no artifact can pre-date a discovery made by the very run that reveals it, so this path does not require (and cannot honestly satisfy) the pre-dates-the-run witness fan-out growth needs. It is permitted instead when (i) the hypothesis is born already resolved in the same edit (never left `alive`), (ii) it is recorded in `discovery_growth_events[]` naming the discovering-and-resolving autopsy plus a `rationale` grounding why this is principled abduction and not motivated post-hoc reasoning, and (iii) `initial_frozen_count_at_registration` is preserved. These are LABELLED, not flagged._

**A hypothesis left `alive` never qualifies here.** If a leg is not resolved in the same edit, it needed Mode A pre-registration BEFORE its adjudicating run instead -- back-dating `pre_registered_utc` to make an actually-anticipated rival look like a discovery is exactly the (b) violation this ledger polices, whichever door it is walked through.

- `inv088_evaluator_degeneracy_cause`: +1 leg(s) (H-dynamics-collapse) added by labelled discovery from `failure_autopsy_V3-EXQ-108b_2026-08-03.json` -- conditions (i)-(iii) satisfied, advisory not a violation. Rationale: H-dynamics-collapse draws on an independent, established mechanism -- the classic model-based-RL compounding-error/mode-collapse failure mode, where a dynamics model trained only on single-step transitions is rolled out autoregressively far beyond its training horizon and converges toward a training-distribution-average attractor -- not intuition applied after the fact. It was genuinely unconsidered before 108b ran: the two hypotheses pre-registered on 2026-08-02 (H-undertrained-instrument, H-dimension-ceiling) both concerned z_world's REPRESENTATION (bespoke-loss adequacy, dimension=32 capacity); neither anticipated a DYNAMICS-training-objective explanation. 108b's own instrumentation is what surfaces it: separately measuring the antecedent (CR_real, healthy at 0.19-0.20) from the coupling-leg (CR_rollout, collapsed to ~3e-6 of CR_real) is what let the run's own decision tree eliminate both pre-registered rivals (branch 1 and branch 2) and land on branch 3 (downstream_dynamics_collapse) -- a mechanism the pre-registration could not have named because the CR_real/CR_rollout dissociation that reveals it did not exist as a finding until this run produced it. Re-filed from fanout_growth_events (2026-08-03T12:15:04Z integrity audit, bucket (b)): that path requires pre-registration to precede its adjudicating run, evidenced by a commit that pre-dates the run's resolution -- but failure_autopsy_V3-EXQ-108b_2026-08-03.json (the only artifact naming this hypothesis) was committed 2026-08-03T09:47:09+01:00 (ree-v3 commit 9c48f834231ca20f3476112ad151808e1352986e), AFTER the run's resolved_utc of 2026-08-02T12:16:43Z -- unwitnessed by construction, since the hypothesis was discovered BY that run's own analysis, not anticipated before it. Discovery growth is the honest path: pre_registered_utc is set to the same instant as resolved_utc (2026-08-02T12:16:43Z) because that is genuinely when the hypothesis was learned to exist, not a claim of prior knowledge.
- `e3_fdominance_causal_discrimination`: +1 leg(s) (H0-selector-regime-confound) added by labelled discovery from `failure_autopsy_V3-EXQ-925_2026-08-12.json` -- conditions (i)-(iii) satisfied, advisory not a violation. Rationale: H0 draws on an independent, established mechanism -- accumulator/drift-diffusion decision models, where near-uniform choice under a low signal-to-noise ratio (small score range relative to decision temperature/noise) is a textbook signature of weak evidence, not intuition applied after the fact. It was genuinely unconsidered when H1-H4 were pre-registered (ree-v3 commit dcd4b6639a, 2026-08-12T06:44:40Z): all four concern WHICH channel has causal authority, none anticipated that NO channel would have meaningful absolute authority at this scale regardless of identity. The run's own instrumentation is what surfaces it -- fixing the counterfactual-replay reconstruction bug (previously reproducing the live selection only ~2.5% of the time, chance at K=32) exposed committed=False on every observed tick and normalised entropy 0.998, a finding that did not exist as such before the replay arithmetic was corrected during this session's authoring.
- `e3_fdominance_causal_discrimination`: +1 leg(s) (H5-score-scale-uncontrolled) added by labelled discovery from `failure_autopsy_V3-EXQ-936_2026-08-18.json` -- conditions (i)-(iii) satisfied, advisory not a violation. Rationale: H5 draws on an independent, established property of the substrate's own numerics rather than on intuition applied after the fact: F is a squared latent-transition norm and the modulatory channels are piecewise-linear head outputs, so the quadratic-vs-linear scaling relation is derivable a priori -- and V3-EXQ-936's data confirms it at slope 2.020, R^2 0.978, over 54 orders of magnitude. It was genuinely unconsidered when H1-H4 were pre-registered (2026-08-12T06:44:40Z) and when H0 was discovered later that day: every one of those five asks WHICH channel has causal authority, or whether any does at the observed scale; none asks whether the scale is a controlled quantity at all. The run's OWN data is what surfaces it -- V3-EXQ-936 is the first experiment in this lineage to record the E3 score COMPONENT MAGNITUDES rather than a rank/entropy statistic (rank statistics are invariant under monotone transforms and structurally cannot see a scale change, which the driver's own docstring notes as a plausible reason the lineage kept reading 'no conversion'). It is born resolved because the evidence that reveals it is the same arithmetic that settles it; there is no future adjudicating run to await for the hypothesis as stated. The separate CAUSAL question -- whether the unbounded rollout is due to the unarmed SD-056 clamp -- is a distinct proposition and is NOT claimed here; it is the V3-EXQ-936a A/B.

## Discovery-growth recurrence (ACTIONABLE, 0) -- N >= 3 discovery events on one question

_Mirrors the fan-out recurrence overlay above, for the discovery-growth path. Every event counted below was individually legitimate -- **the recurrence is the signal**: a question racking up repeated 'discoveries' may be using this path as a substitute for pre-registration discipline (an actually-anticipated rival hypothesis being called a discovery each time to dodge Mode A) rather than genuine one-off serendipity. Response is routing -- check whether the next candidate explanation was really unforeseeable before treating it as another discovery. Warn-only: this never gates a cycle._

**Same acknowledgement rule as the fan-out overlay above** -- a closed question with no alive legs is listed under 'Recurrence acknowledged', not here, because `growth_restriction` governs the discovery path too (Step 9b applies it to Mode C in every case). A count of 0 here is not by itself evidence of no recurrence.

_None._

## Pre-registration provenance (18 witnessed, 0 unverifiable)

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
- `competence_floor`/`H-consummation-binding`: `mech457_retention_portfolio_2026-07-18.md` committed 2026-07-18 <= resolution 2026-08-08
- `competence_floor`/`H-zworld-trained-instrument`: `failure_autopsy_batch-793a-817-819_2026-07-26.json` committed 2026-07-26 <= resolution 2026-07-27
- `competence_floor`/`H-mech475-baseline-reversal`: `failure_autopsy_mech476-mech475-cluster_2026-07-29.json` committed 2026-07-29 <= resolution 2026-07-29
- `competence_floor`/`H-mech476-dose-response`: `failure_autopsy_mech476-mech475-cluster_2026-07-29.json` committed 2026-07-29 <= resolution 2026-08-01
- `competence_floor`/`H-mech476-novelty-tagging`: `failure_autopsy_mech476-mech475-cluster_2026-07-29.json` committed 2026-07-29 <= resolution 2026-08-01
- `conversion_ceiling_root`/`H-objective-misspecification`: `failure_autopsy_competence-objective-cluster-734-737b-742a_2026-07-22.json` committed 2026-07-22 <= resolution 2026-07-24
- `conversion_ceiling_root`/`H-observation-interface`: `failure_autopsy_backlog_2026-07-24.json` committed 2026-07-24 <= resolution 2026-08-25
- `arousal-variance-amplifier`/`H-arousal-channel-agnostic`: `failure_autopsy_V3-EXQ-785_2026-07-19.json` committed 2026-07-19 <= resolution 2026-07-19
- `inv088_evaluator_degeneracy_cause`/`H-horizon-compounding`: entered the registry 2026-08-29 <= resolution 2026-08-29
- `inv088_evaluator_degeneracy_cause`/`H-action-blindness`: entered the registry 2026-08-29 <= resolution 2026-08-29

---

This audit promotes/demotes nothing. Response to any flag is a human decision at governance (the same handling as `check_closure_drift.py`). Advisory labelled-growth notes need no action -- but a question accumulating them is one whose campaign has not converged.

