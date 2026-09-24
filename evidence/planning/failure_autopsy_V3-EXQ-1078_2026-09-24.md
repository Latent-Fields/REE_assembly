# Failure autopsy -- V3-EXQ-1078 (INV-069 coherence leg, Option C) -- diagnostic PASS, vacuous

- **Status:** `awaiting_human_confirmation` (staging mode). The Step 8 gate is owed by the parent
  `/governance` session `governance-20260924-workset`. Step 9b was drafted only (JSON
  `hypothesis_space_ledger_pending`); the registry was not written.
- **Generated:** 2026-09-24T06:06:53Z; revised 2026-09-24T06:17:41Z after the Step 7c red-team (fable, CONTESTED; all three defects accepted, see Section 10)
- **Run:** `v3_exq_1078_inv069_zself_coherence_unsettled_20260923T182046Z_v3` (ree-worker-3,
  ree-v3 `23bd9cd`, clean, substrate_hash `6eeb6dfb...`, 1772 s, seeds 42/43/45)
- **Tagged:** INV-069 | purpose `diagnostic` | outcome PASS 3/3 | indexer adjudication `vacuous_pass`
- **Self-route:** `arm_a_state_restores_after_burst_untrained_gru_init_contraction__inv069_undetermined|arm_b_sign_locked_gap_above_noise_non_contributory`
- **Open flags in scope:** GFLAG-0414, GFLAG-0428 (both INV-069, both request a what_would_answer amendment)

## 1. Scope and pre-flight

- Single target, the first autopsy ever tagging INV-069 (`granularity_debt_cluster.py INV-069` -> 0
  targets). `check_autopsy_coverage.py` -> AVAILABLE for both the queue_id and the run_id. No cluster.
- **Dry-run gate (2a):** `check_dry_run_citations.py <run_id> V3-EXQ-1078` -> 0 dry, 1 clean;
  `--family v3_exq_1078` -> 0 dry / 1 real. The only cited run is real. `excluded_dry_run_ids: []`.
- **Recording (2b):** `validate_recording.py` -> OK, 0 always-core gaps (`substrate_hash`, `config`,
  `seeds`, `machine_class`, `elapsed_seconds`, `recording_schema` all present;
  `substrate_stable_across_run: true`).
- Premises re-measured against the manifest, the driver and live ree-v3, not taken from the brief:
  every number below was read from the flat manifest or recomputed from its per-seed cells.

## 2. Facts (no interpretation)

The driver pre-registers `evidence_direction: unknown` for INV-069 in every branch. The user chose
this design (Option C) over the recommended Option A, ledger `rec-20260923-061462f2`.

**Arm (a), the scored arm.** A one-tick burst of 0.5 x ||z_self|| goes into the DR-13 recurrent
hidden state at tick 30. It is compared with a deep-copied twin whose RNG is restored. The
control replay was deterministic (max abs diff 0.0).

| seed | dip (peak vs gap) | vs gap at K=30 (A1, <=0.005) | state-div ratio K/burst (A2, <=0.10) |
|---|---|---|---|
| 42 | 0.0339 | 0.00211 | 9.22e-8 |
| 43 | 0.0326 | 0.00194 | 1.107e-7 |
| 45 | 0.0361 | 0.00228 | 1.145e-7 |

The per-event `state_div` traces contract at about 0.46-0.57 per tick over ticks 0-19. After that
they sit at a noisy float32 floor near 1e-7, with late per-tick ratios of 0.5-3.3. The A2 ratio is
therefore floor-limited. `ratio^(1/30)` = 0.583-0.587 is an average over that floor and is not an
init constant (red-team H1). The precondition gate is green:
recurrence live (departure 0.87), dip 0.033 against a 0.015 floor, control vs 0.9985 < 1, 4/4 events
per seed, determinism 0.0.

**The recurrence was not trained.** `gru_param_max_delta` = 0.0 and `latent_stack_tensors_changed`
= 0/53 on every seed. The P0 warmup trained with `compute_prediction_loss() + compute_e2_loss()`
under Adam over `agent.parameters()`. Those are the losses DR-13's doc says train the GRUCell. E1/E2
learned (loss fell by roughly 4-17x) and nothing in the LatentStack moved.

This is narrow, not a V3-wide absolute (red-team D2):

- Seven other `agent.py` losses anchor on `latent_stack` parameters (11611-11916), and SD-070
  trains the world encoder.
- None of those losses reaches `self_encoder` or `SelfRecurrenceCell`.
- The one exception is SD-CM-LIVETAP (ree-v3 `30f40ab`). It is default OFF and trains a
  ContextMemory write-addressing objective, not a z_self objective. It shares a detach root with
  V3-EXQ-972a.

**Arm (b), descriptive only and scoped out of scoring.** The freeze starts at tick 2 after reset and
lasts 8 ticks, in the unsettled post-boundary regime. There the live error is 11.5-73x the settled
error.

| seed | frozen-minus-live gap max | / raw settled sd | / detrended settled sd |
|---|---|---|---|
| 42 | 0.0207 | 5.48 | 27.9 |
| 43 | 0.0219 | 4.74 | 22.3 |
| 45 | 0.0235 | 4.60 | 24.3 |

The closed-form identity holds exactly. The frozen vs equals `1-(1-tau)^n(1-vs_onset)` to
1.1e-16, with 0 frozen<live ticks across 12 events.

**Behaviour.** Action divergence was 0.0 in every twin of both arms.

`criteria_non_degenerate` is false for A1, A2 and B, so every criterion that passed is marked
non-discriminating by the driver itself.

## 3. Claim layer

INV-069 is an invariant (universal), status `candidate`. It has no explicit `epistemic_category`
field, so the indexer resolves it to `substrate_coherence`. It `depends_on` INV-067 and INV-068.

The claim says the self is a dynamically sustained process, not a stored state. The
what_would_answer (WWA) requires:

- a trained substrate;
- z_self reaching behaviour (DR-10);
- a coherence readout that sits off its ceiling;
- both arms, sign-consistent across 3 or more seeds.

The current `evidence_quality_note` (GFLAG-0400) states that the WWA amendment is held for this
autopsy and GFLAG-0428.

**Did the test let the claim express itself? No.**

- **Behavioural leg.** It is inert in V3 (GFLAG-0414), and the run confirms this: action
  divergence was 0.0 everywhere.
- **Arm (b).** The manipulation fixes its own DV. The frozen-minus-live contrast is an arithmetic
  function of the live trace, so it measures nothing about the freeze. The WWA maps a small
  positive delta to both CONFIRMING and FALSIFYING (GFLAG-0428's verdict aliasing).
- **Arm (a).** It ran on an untrained recurrence. That violates the WWA's own "trained substrate"
  precondition. See Section 5 for why the pass is structural.

Claim alignment is therefore **unclear (untested)**, not weakened. The claim tag itself is correct,
and the run was designed for INV-069.

## 4. Biological-reference triage

The closest reference is restoration of a self-state after perturbation by structured recurrent
attractor dynamics. Examples are continuous-attractor restoration (the head-direction ring) and
re-calibration of body schema and interoceptive predictions after rubber-hand or vestibular
perturbation.

The biologically discriminating signature is restoration to a *self-specific* attractor that
exceeds what input re-driving of any fading-memory system provides. Arm (a) has no null for that
generic effect.

INV-069 itself is a formal verisimilitude definition (V_self, D_self EMA), measured through V_s, a
consecutive-difference proxy. The arm-(b) sign-lock comes from that proxy's form. It is an
artefact of the readout, not a biology divergence in the mechanism.

There is no INV-069 literature entry (`lit_status: absent`). A `/lit-pull` commission is a named
secondary follow-on. It is not the primary route, because the failure here is test design, not a
biology mismatch.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | untested; no leg could discriminate |
| Biological reference | partial | attractor restoration; the missing piece is a null for generic fading memory |
| Prerequisites | missing | no z_self training path, so the WWA's "trained substrate" is unmet; DR-10 inert (v4) |
| Implementation | partial | DR-13 is wired and live, but **inert by DEFECT on the training side**. Missing link: **no gradient path** for the losses DR-13 names. The detach loci are `agent.py` ~5721 (`_current_latent`) and the buffer-side detach at ~6155-6160 (`_self_experience_buffer`). This is the same root V3-EXQ-972a measured, and the same detached-z_self family as MECH-113. DR-13's doc claims the GRU trains via the existing E1/E2 losses; measured false. |
| Environment | adequate | contaminated_harm 0.0 lets a settled regime exist; no events skipped |
| Measurement | misleading | A1 is an EMA artefact for any one-tick event. A2 passes by construction for any GRU contraction <= 0.926/tick (driver F1). Measured contraction is about 0.46-0.57/tick down to a float floor, and there is no generic-contraction null. Arm-(b) DV is annihilated by the freeze. |
| Integration | coupled but inert | the recurrence runs, but nothing trains it and z_self reaches no behaviour |
| Scale | adequate | 3 seeds x 4 events, twin-matched |

**Failure-location (GOV-FAILLOC-1).** The classification is **MIXED (MECHANISM + MEASURES), not
chargeable to REE.**

- Mechanism is not established: implementation is partial and the recurrence is untrained.
- Measures are not established.
- Environment is established.

This is a PASS whose criteria cannot discriminate. It reports neither an REE success nor an REE
failure.

**Self-route verdict.** The label is accurate. It already names "untrained GRU init contraction" and
"sign-locked ... non_contributory". The indexer's `vacuous_pass` flag is correct, and the PASS is
**not cleared** as evidence.

## 6. Cluster

Not applicable: this is a single target and the first INV-069 autopsy.

## 7. Learning and repair pathway

**What was learned:**

1. **Measurement gap.** A recovery criterion on a driven recurrent state needs a null for generic
   contraction: the same architecture at random init, plus a recurrence-lesioned or coupling-0
   ablation. "The perturbation recovered" is true of any contractive fading-memory system that
   receives the same input.
2. **Implementation gap.** DR-13's documented training premise is false for the losses it names:
   the E1/E2 losses do not reach `self_encoder` or `SelfRecurrenceCell`. This shares its detach
   root with V3-EXQ-972a. The WWA's "trained substrate" cannot be met for z_self without a z_self
   objective.
3. **Measurement gap, confirmed exactly.** A consecutive-difference coherence DV is annihilated by
   a freeze.
4. **GFLAG-0428's "within noise" half is regime-specific.** In the unsettled window the gap is
   22-28x the detrended settled sd. The sign-lock half is structural.

**Work-graph node:** `complex (probe-gated) / mystery (known data)`. The data is in, and the WWA
frame is wrong on all three legs. The response is to reframe, not to gather more data. The z_self
training path is a separate node, `complicated (buildable)`.

**Routing:**

- **Primary: `governance-reclassify (wwa_amendment)`.** `/governance` applies the WWA amendment
  drafted in Section 9 and the note below.
- **Secondary: `implement-substrate`** via `recommended_substrate_queue_entry` action `create`,
  `sd_zself_training_path`:
  - Priority 1 (fresh failure record).
  - Severity `corrupting` on `ree_core/latent/self_recurrence.py` only. A DR-13 run that trusts the
    doc and does not record the GRU delta reports init contraction as a trained self-recurrence.
    The agent.py detach site is deliberately left off `substrate_paths` so that it does not gate
    every experiment. This call is for the user at the gate; `degrading` is the alternative.
  - It unblocks INV-069 and MECH-113. ARC-081 and MECH-215 are v4-gated, so they are read-across
    only.
  - It is not a duplicate: 7b C2 is silent. It shares its detach root with
    `contextmemory-write-path-addressing-degeneracy` (V3-EXQ-972a, SD-CM-LIVETAP), and governance
    may cross-link the two.
- **Secondary: `/lit-pull`** for `targeted_review_INV-069`: self-state restoration after
  perturbation, structured attractor vs fading memory.

**INV-069 requeue refused until the WWA amendment lands.** Every V3 leg is currently
non-discriminating by construction.

**Re-derive brake.** This target counts as 1 under R3 step 4 (non_contributory, owes a build). The
threshold is 2, so the brake does not fire. The refusal above rests on design grounds, not on the
brake.

**Granularity-debt recurrence trigger does NOT fire.** `granularity_debt_cluster.py INV-069` finds
0 prior tagging targets, and this target reads `unclear`, not `weakened`.

**Draft `evidence_quality_note` (INV-069):**

> [V3-EXQ-1078 autopsy, failure_autopsy_V3-EXQ-1078_2026-09-24] Diagnostic PASS, adjudicated NON-CONTRIBUTORY to INV-069 (vacuous_pass). Arm (a) A1+A2 held on 3/3 seeds, but the z_self recurrence was UNTRAINED: GRU max param delta 0.0 and 0/53 LatentStack tensors changed under the E1/E2 losses DR-13's doc says train it (they do not reach self_encoder or SelfRecurrenceCell; same detach root as V3-EXQ-972a). An untrained contractive GRU passes A2 by construction (any contraction <= 0.926/tick; measured ~0.46-0.57/tick to a float floor) and A1 is an EMA artifact, so the run has no generic-contraction null. Arm (b) is sign-locked exactly (frozen vs == 1-(1-tau)^n(1-vs_onset), dev 1.1e-16): its 22x-detrended-sd gap in the unsettled window is a function of the live trace alone. The behavioural leg is inert in V3 (GFLAG-0414). INV-069 is untested, not weakened. Retest requires the WWA amendment drafted in this autopsy and a z_self training objective.

**Recommended dispositions:**

- `evidence_direction` `non_contributory` for INV-069 (the manifest currently says `unknown`;
  governance writes it).
- `epistemic_category`: **keep the resolved `substrate_coherence`**. INV-069 is a universal
  invariant with no explicit field, and the indexer resolves it to `substrate_coherence`. Do NOT
  stamp `standard`. That was this draft's first recommendation, and it would silently lift
  universal-invariant suppression (red-team D1). The failure mode (vacuous_pass, test-design
  defect, precondition unmet) goes in the note.
- `diagnostic_evidence_adjudicated: true`.
- `pending_retest_after_substrate: true`.
- Status stays `candidate`.

**Alternative for the user.** Use `substrate_conditional` only if governance rules the
dissociation unreachable in V3. That is a deliberate ceiling assertion, which this autopsy does
not make.

## 8. Governance flags GFLAG-0414 / GFLAG-0428

**Can this autopsy resolve either flag? No.** Both flags' ACTION REQUESTED is a `claims.yaml` WWA
amendment, and this skill never edits `claims.yaml`. What this autopsy does is discharge the hold
recorded in INV-069's `evidence_quality_note` ("held for the V3-EXQ-1078 autopsy and GFLAG-0428")
and draft the amendment (Section 9).

**Recommended sequence:**

1. Keep both flags open.
2. `/governance` applies the Section 9 amendment.
3. Resolve both flags in the same pass, citing this artifact.
4. Optionally, append the premise corrections below to BOTH flags now, so neither open record is
   stale.

**Premise corrections, measured in this run:**

- **GFLAG-0414.** "The coherence leg IS fully runnable and non-degenerate" is false on both arms.
  Arm (b) fails per 0428. Arm (a) fails because the recurrence is untrained and A1/A2 pass by
  construction.
- **GFLAG-0428.**
  - The sign-lock is **confirmed and strengthened**: the closed form is exact to 1.1e-16.
  - "Inside the noise band" is **regime-specific**: 4.6-5.5x the raw and 22-28x the detrended
    settled sd in the unsettled window.
  - "ARM (a) IS UNAFFECTED and remains live and non-degenerate" is **corrected**: arm (a) is live,
    but it is not non-degenerate.

**Draft resolution notes:**

- **GFLAG-0414:** "Resolved by the INV-069 WWA amendment applied <date> from
  failure_autopsy_V3-EXQ-1078_2026-09-24 section 9: behavioural leg restated as v4-gated (DR-10
  inert in V3; GatedPolicy rank-invariant at default). The coherence-leg 'fully runnable' premise
  in this flag was corrected by that autopsy (arm (a) non-discriminating on an untrained
  recurrence)."
- **GFLAG-0428:** "Resolved by the INV-069 WWA amendment applied <date> from
  failure_autopsy_V3-EXQ-1078_2026-09-24 section 9: arm (b) DV replaced (must not be a function of
  the frozen stream's own increments), arm (a) given a generic-contraction null and a
  trained-recurrence precondition. V3-EXQ-1078 adjudicated non_contributory (vacuous_pass)."

## 9. Drafted WWA amendment for INV-069 (for /governance to accept, revise or reject)

This is a proposal. The substitute arm-(b) DV below is offered as a candidate, not a decision. The
2026-09-23 decision chip deliberately left the DV choice to the user.

- **Behavioural leg.** Restate it as v4-gated. DR-10 is inert in V3 (no internal self_viability
  producer), and GatedPolicy's z_self bias is rank-invariant at the default operating point
  (GFLAG-0414). V3 evidence can address the coherence leg only, and V3 cannot reach CONFIRMING.
- **Trained-substrate precondition.** Make it explicit and checkable. Record
  `gru_param_max_delta > 0` and a changed self_encoder after warmup, under a documented z_self
  objective. With the current substrate this requires `sd_zself_training_path`.
- **Arm (a).** Add a **generic-contraction null**. Count recovery only if the running process
  restores z_self measurably faster or more completely than both of these:
  - the same architecture at random init;
  - a recurrence-lesioned / coupling-0 ablation.

  Not "anchor-only (1 - coupling)^k": the E1 anchor is predicted from the perturbed z_self, so it
  carries the burst (red-team D3).

  A1 alone never counts, because it is an EMA artefact. A2 is necessary but not sufficient.
- **Arm (b).** The DV must **not be a function of the frozen stream's own consecutive increments**.
  Per GFLAG-0428 and this run, `per_stream_vs['z_self']` is annihilated by the freeze, since
  frozen vs is `1-(1-tau)^n(1-vs_onset)`.

  One candidate is the correspondence between the stored z_self and the current body report
  (`z_self_instant`, or E1's z_self prediction):
  - under a freeze, coherence "drifts" if the stored self stops tracking the body;
  - it is "preserved" if it does not.

  This is still the proxy reading, not INV-067's precision-weighted correspondence.
- **CONFIRMING.** State that "both together, sign-consistent across >=3 seeds" is unreachable in V3
  until arm (b) has a non-annihilated DV **and** arm (a) runs on a trained recurrence against the
  null.

## 9b. Hypothesis-space ledger (drafted only; see JSON `hypothesis_space_ledger_pending`)

No existing registry question carries INV-069, and this autopsy emits no fan-out. The draft
registers a new question, `inv069_process_vs_state_dissociation`, with two legs:

- H-process: the maintenance process restores and sustains z_self beyond generic contraction.
- H-stored: a stored vector suffices.

V3-EXQ-1078 is recorded as a non-discriminating resolving run. Both legs stay `alive`, with
`met_elimination_bar: false` and `non_degenerate: false`. `initial_frozen_count` is 2. The confirming
session applies this and runs `build_hypothesis_space.py` + `check_hypothesis_space_integrity.py`.

## 10. Checks run

- **7b** `autopsy_pre_routing_checks.py`: 0 fires.
  - C7 is inapplicable (single condition).
  - C2 is silent, so `sd_zself_training_path` is not a duplicate.
  - C3 is silent, consistent with lit absent.
- **7c** red-team: **fable** (cross-model; the draft was written on Opus). Verdict **CONTESTED**.
  All three defects were verified by the drafter and ACCEPTED:
  - **D1.** Explicit `standard` would override the resolved `substrate_coherence`.
    `build_experiment_indexes.py` ~4488-4494. The category was changed.
  - **D2.** "No V3 loss reaches the LatentStack" was a false absolute. Seven `agent.py` losses
    anchor on `latent_stack` (11611-11916), and SD-CM-LIVETAP `30f40ab` is a live route. The
    claim was narrowed to the DR-13-named losses and self modules, and the shared root was named.
  - **D3.** The E1 anchor carries the burst (`agent.py` ~5083-5091, ~6155). The anchor-only
    argument was withdrawn, and the WWA arm-(a) null was reworded.
  - **Hygiene accepted:**
    - H1: the contraction figure was a float-floor artefact; corrected to 0.46-0.57/tick,
      re-verified per event.
    - H2: the buffer-side detach at 6155-6160 is now cited.
    - H3: ARC-081/MECH-215 are read-across.
    - H5: resolved by D3.
    - H6: both flags are now offered the append.
  - **Unchanged by the red-team:**
    - the direction, `non_contributory`;
    - the sign-lock;
    - the flag premise corrections;
    - that neither flag can be resolved here;
    - severity `corrupting`, judged defensible.
- **Withdrawn arguments** are recorded in JSON `withdrawn_arguments`: D1, D2, D3 and H1.

## 11. Follow-on named (reported, not spawned; governance chips after ratification)

1. The WWA amendment for INV-069 (governance), then resolve GFLAG-0414 and GFLAG-0428.
2. `/implement-substrate` `sd_zself_training_path`, including correction of the DR-13 doc.
3. `/lit-pull` `targeted_review_INV-069`.
4. Read-across, not adjudicated here:
   - DR-13 consumers (ARC-081, MECH-215; V4-EXQ-002 did not record the GRU delta).
   - The MECH-113 D_eff family (same detach, GFLAG-0400).
