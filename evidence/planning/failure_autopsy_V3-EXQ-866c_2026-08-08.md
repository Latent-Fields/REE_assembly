# Failure Autopsy: V3-EXQ-866c (INV-034 / Q-021 goal-maintenance-necessary-for-agency, C6 run_p2 measurement fix)

**Generated:** 2026-08-08T20:53:00Z
**Scope:** single
**Status:** confirmed

## Facts

- **run_id:** `v3_exq_866c_inv034_q021_goal_maintenance_agency_onboarded_20260808T195345Z_v3`
- **queue_id:** V3-EXQ-866c
- **timestamp_utc:** 2026-08-08T19:53:45Z
- **status:** FAIL
- **claim_ids_tested:** INV-034, Q-021
- **experiment_purpose:** evidence
- **evidence_direction (manifest):** non_contributory (per_claim: INV-034=non_contributory, Q-021=non_contributory)
- **supersedes:** V3-EXQ-866a
- **dry_run:** false (checked via `check_dry_run_citations.py`: 0 dry, 1 clean)
- **substrate_hash:** `71b1c363f65ea584298593e590bd2b91264f2239145beb0e3a9e1ea692961d1f` (commit `60993d0e45`, clean)
- **z_goal_stream:** writer_defect=false, active_frac=0.99997 (no dead-stream defect)

### Purpose of this run

V3-EXQ-866c was purpose-queued by the same-day `scaffolded-curriculum-hazard-rebalance`
substrate_queue diagnosis (`evidence/planning/scaffolded_curriculum_hazard_rebalance_diagnosis_staged_2026-08-08.md`,
chip `chip-20260808-igw200-scaffolded-curriculum-hazard-rebalance`, user-confirmed via
`chip-20260808-scaffolded-c6-misdiagnosis-routing`). That diagnosis found the hazard-stage
curriculum was NOT the cause of 866a's C6 z_goal-decay reading: an empirical probe showed
z_goal survives every hazard stage and enters P2 at ~0.52, and 866a's C6 FAIL was a
**measurement artifact** in the driver's own P2 readout (decay-only mean, `zgoal_norm_mean_866a_style`)
which bypasses the scheduler's contact-gated `run_p2` peak (peak 0.52, `n_decay_only=0`).
It routed the finding on two separate threads: **C6 -> V3-EXQ-866c** (fix the readout to use
the contact-gated peak) and **G0 -> a dedicated foraging-competence autopsy** (that autopsy is
`failure_autopsy_V3-EXQ-866a-G0_2026-08-08`, generated the same day at 12:16:25Z, ~7.5h before
this run completed).

### Gates (866c)

| Gate | Frac seeds | Pass |
|---|---|---|
| G0 non-degeneracy (foraging) | 0.00 | **False** |
| C1 harm parity | 1.00 | True |
| C2 survival parity | 1.00 | True |
| C3 quiescence (avoidance-only flat) | 1.00 | True |
| C4 approach restored (FULL > avoidance) | 0.00 | False (unreachable while G0 fails) |
| C5 entropy signature | 0.00 | False (unreachable while G0 fails) |
| **C6 z_goal mechanistic (contact-gated peak)** | **0.67** | **True** |

### C6 readout comparison

| Condition | z_goal_norm_peak_max (866c, corrected) | zgoal_norm_mean (866a-style, decay-only) |
|---|---|---|
| FULL | 0.4610 | 0.1481 |
| AVOIDANCE_ONLY | 0.0000 | 0.0000 |

The corrected FULL-arm reading (0.461) clears the C6 floor (>0.4); the old decay-only reading
(0.148) did not. This confirms the routed diagnosis: the C6 mechanism was never actually
failing — the P2 readout was measuring the wrong quantity.

## Claim-layer map

- **Q-021** (`open_question`, subject `drive.behavioral_flatness_under_pure_avoidance`,
  status `open`): tests Pathway A (drive absence, ARC-030 route). `what_would_answer` states
  a MANDATORY non-degeneracy precondition (G0-equivalent) — a run failing it self-routes
  `substrate_not_ready`, not a "yes"/"no" answer. 866c's G0 FAIL is exactly this precondition
  path; the question remains untested, not answered "no."
- **INV-034** (`invariant`, `emergent_from: [ARC-030]`, status `candidate`,
  `pending_substrate_reconfirmation: true`): needs the fuller C1-C6 battery on top of Q-021's
  G0+C3. `what_would_answer` explicitly names the SAME G0 mandatory precondition and states a
  FAIL there "self-routes non_contributory/substrate_not_ready_requeue -- a competence-floor
  failure, not evidence against INV-034/Q-021." 866c's own C6 note (already present in the
  claim text as of the 2026-08-08 CORRECTION entry) anticipated exactly this run and reads:
  "C6 failing under 866a is itself downstream of the same z_goal-survival-to-P2 gap ...
  not a fresh mechanistic problem" — 866c is the confirmation that C6 was never a real
  mechanistic failure once measured correctly.

Neither claim could express itself in this run: G0 (foraging competence) gates the whole
battery, and G0 is a substrate/curriculum competence question, not a goal-maintenance
question. The experiment tested the wrong layer for a verdict on INV-034/Q-021 themselves,
exactly as diagnosed for 866 and 866a before it.

## Biological-reference triage

Unchanged from 866/866a: the closest mammalian reference is prospective/persistent approach
motivation (wanting, mesolimbic dopamine) sustaining goal pursuit independent of moment-to-moment
hedonic response (liking) — the schizophrenia avolition / anhedonic-depression dissociation
INV-034's `notes` already cites (Culbreth et al. 2023). That reference is not in question here;
what is in question is whether the REE Stage-H hazard-avoidance curriculum's agent can forage
above a chance floor at all before the approach/avoidance dissociation can even be probed. That
is an implementation/curriculum-competence question, not a biological-fidelity question — no new
lit-pull is warranted by this run.

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (untested) | G0 precondition unmet; claim could not express itself |
| Biological reference | clear | wanting/liking dissociation; unaffected by this run |
| Developmental / dependency prerequisites | immature | Stage-H foraging competence not yet established on this curriculum (G0) |
| Implementation completeness | partial | C6 readout bug now FIXED (confirmed this run); G0 foraging-competence gap remains, already routed to `failure_autopsy_V3-EXQ-866a-G0` |
| Environment adequacy | adequate | scaffolded_sd054_onboarding confirmed substrate-sound (V3-EXQ-866b); not an environment gap |
| Measurement adequacy | **corrected this run** | C6's prior decay-only P2 mean was a washout artifact; contact-gated `run_p2` peak is the mechanistically correct readout and now passes |
| Integration adequacy | isolated (untestable) | cannot assess FULL-vs-avoidance interaction while G0 blocks foraging |
| Scale / capacity | likely insufficient (per 866a-G0) | foraging-competence gap shared with MECH-457's GOV-FANOUT-1 portfolio dependency, per 866a-G0's routing |

## Learning extracted

1. **C6 measurement fix CONFIRMED.** The contact-gated `run_p2` peak readout (vs the old
   decay-only P2 mean) is the correct z_goal mechanistic-check methodology going forward for
   this experiment family. `zgoal_norm_mean_*_866a_style` metrics should not be read as the C6
   criterion in any future run of this lineage.
2. **G0 foraging-competence gap reconfirmed, third occurrence (866, 866a, 866c).** No new
   diagnostic content beyond what `failure_autopsy_V3-EXQ-866a-G0_2026-08-08` already
   established (category `competence_implementation_gap`, shared dependency with MECH-457's
   GOV-FANOUT-1 portfolio, awaiting V3-EXQ-899). This run does not add a new G0 finding; it
   confirms the gap is stable/reproducible under the corrected-C6 harness too.
3. **The claims.yaml `epistemic_category: substrate_ceiling` on both INV-034 and Q-021 is
   stale** — `failure_autopsy_V3-EXQ-866a-G0_2026-08-08` recommended `competence_implementation_gap`
   over six hours before this run even completed, and that correction was never applied.
   Independently flagged by this cycle's own GOV-APPLY-1 scan (`check_unapplied_autopsy_recommendations.py`,
   "superseded live_status citation" bucket) as citing the superseded `V3-EXQ-866a` autopsy
   rather than its superseding `V3-EXQ-866a-G0`. 866c's own read is consistent with the
   `competence_implementation_gap` category, not `substrate_ceiling` (the substrate itself is
   confirmed sound per V3-EXQ-866b; the gap is in curriculum/competence-training, which is a
   ceiling on the *harness*, not on what the substrate can represent).

## Repair pathway

**Node class:** `complex (probe-gated) / puzzle (known rules)` for the G0 foraging-competence
gap — already correctly framed and being probed by the MECH-457 GOV-FANOUT-1 portfolio and
V3-EXQ-899; no new spike needed from this autopsy. The C6 measurement thread is now
`complicated (buildable)` and CLOSED (the fix shipped in this run's own driver).

**Routing: `governance-note-only`.** No new `/queue-experiment` or `/implement-substrate`
action from this autopsy — G0 already has its own dedicated routing via
`failure_autopsy_V3-EXQ-866a-G0_2026-08-08` (await V3-EXQ-899 + cross-reference the MECH-457
portfolio), and re-opening a parallel routing here would duplicate that. This autopsy's sole
governance action is applying the overdue `epistemic_category` correction (below) and recording
the C6 fix as confirmed.

**Re-derive brake:** does NOT fire. This was the planned confirmation run for a specific,
already-diagnosed measurement fix (C6), not a blind same-claim re-test. Under the R1-R3
convention, `competence_implementation_gap` is not a `substrate_ceiling` hit, so this run adds
0 to the ceiling-hit count for INV-034/Q-021 (consistent with `866a-G0` already reclassifying
away from the ceiling reading).

### Draft `evidence_quality_note` (governance to apply, both claims)

> [2026-08-08 governance, V3-EXQ-866c, confirmed failure_autopsy_V3-EXQ-866c_2026-08-08,
> supersedes V3-EXQ-866a]: G0 non-degeneracy gate FAILED again (foraging-competence), as
> already diagnosed by failure_autopsy_V3-EXQ-866a-G0_2026-08-08 -- non_contributory,
> precondition_unmet, not evidence against INV-034/Q-021. 866c's own contribution: the C6
> z_goal mechanistic-check readout is CORRECTED (contact-gated run_p2 peak, FULL=0.461 clears
> the 0.4 floor) and CONFIRMED PASSING -- 866a's C6 FAIL (zgoal_norm_mean=0.148) was a
> decay-only measurement washout artifact, not a real mechanistic gap, exactly as the
> scaffolded-curriculum-hazard-rebalance diagnosis routed. epistemic_category corrected from
> the stale substrate_ceiling (866a's original, since superseded) to competence_implementation_gap
> (866a-G0's reading, now applied). Remaining blocker is G0 foraging-competence alone, shared
> with MECH-457's GOV-FANOUT-1 portfolio dependency; awaiting V3-EXQ-899. pending_retest_after_substrate
> stays true.

## Governance disposition (user-confirmed, Step 8 gate)

User selected "Agree (Recommended)": apply as proposed. C6 fix recorded as confirmed;
`epistemic_category` corrected `substrate_ceiling -> competence_implementation_gap` on both
INV-034 and Q-021 (the overdue 866a-G0 correction, applied via this autopsy rather than a
separate GOV-APPLY-1 walk item); `pending_retest_after_substrate` unchanged (true); no new
substrate_queue entry; no re-derive-brake fire.
