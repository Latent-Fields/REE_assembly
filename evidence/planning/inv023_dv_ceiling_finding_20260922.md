# INV-023 / V3-EXQ-1076 -- Step 2.5d STOP (falsifier-runnability, INERT shape)
Session inv023-science-20260922, campaign science-20260922-inv023-offline-protection.

## Gates cleared before the stop
- ID V3-EXQ-1076 free on origin/main (queue, runner_status, git log -S, experiments/ tree). Reserved.
- No completed run for INV-023 (absent from claim_evidence.v1.json); no implementation_phase.
- 2.5b re-derive brake: 0 hits for INV-023, MECH-018, MECH-204.
- 2.5c substrate-path gate: no open `corrupting` entry in the module set the design names.
  Noted-not-blocking: `contextmemory-write-path-addressing-degeneracy` (corrupting, fix default-OFF
  via E1Config.contextmemory_write_usage_balancing so the legacy argmin path is live) and
  `f_dominance_conversion_ceiling` (severity corrupting but implementation_status=wontfix -> CLOSED
  by the exact-match test; names e3_selector.py::score_trajectory + residue/field.py). Both are
  arm-invariant here.
- 2.4 GOV-REUSE-1: `mech204_running_variance_*` recorded in only 4 pre-standard manifests
  (541/541a/541b + 1), all substrate_hash UNVERIFIABLE -> not recoverable. `mech018_residue_trains`
  and `broadcast_precision` -> 0 manifests in the whole 1060-manifest corpus. Not recoverable -> run.
- GAP-9 CLOSED (both arms, 2026-08-14 + SD-SLEEP-ENTRY-PRESSURE 2026-08-26): the WWA's parenthetical
  "a true single-continuous-life driver is structurally unable to sleep" is STALE.

## The API trap -- resolved, with a source-exact assertion
`REEAgent.run_sleep_cycle()` (agent.py:13080) drives only enter_sws->run_sws_schema_pass->exit and
enter_rem->run_rem_attribution_pass->exit. It never touches SleepLoopManager.state.phase, so it
NEVER reaches SleepPhase.WRITEBACK. Only force_sleep_cycle_at_eval_boundary() (agent.py:13117)
-> sleep_loop.force_cycle -> _run_cycle does.
`agent.sleep_loop.state.phase` is USELESS post-hoc: phase_manager.py:831 resets it to WAKING at the
end of every cycle, before the return.
Correct assertion, from phase_manager.py:639-659 -- the phase is assigned at :639 BEFORE the
`target > 0.0` test, so:
  * WRITEBACK ENTERED  <=> key "mech204_recalibration_fired" PRESENT in the returned/cycle_history dict
  * recalibration APPLIED <=> that key == 1.0
Residue arm equivalent: mech018_residue_integration_fired == 1.0 (phase_manager.py:689) AND
mech018_residue_trains -- `_fired` alone witnesses the CALL, not the work (field.py:1175 early-returns
on empty _harm_history).

## THE STOP -- INV-023's primary DV is measured non-discriminative
Arm A `recalibrate_precision_to` (e3_selector.py:1128) and arm B `broadcast_precision_pull`
(e3_selector.py:1158) are ARITHMETICALLY IDENTICAL: new_var = (1-k)*old + k*(1/target), same target
source (serotonin.compute_recalibration_target -> _persistent_zero_point). They differ ONLY in WHEN
they fire. That is the right contrast for INV-023 -- but it lands on a DV that cannot hold it:

`_running_variance` is a SYMMETRIC EMA over realised error (e3_selector.py:1056-1058):
    rv <- (1 - alpha) * rv + alpha * error_var,  alpha = precision_ema_alpha = 0.05
config.py:1076 states the effective window: ~20 ticks. So an injected offset from EITHER arm decays
back to realised error on a ~20-tick horizon. Arm A injects once per sleep cycle (hundreds of waking
ticks apart); arm B at N budget-matched waking ticks. At eval, rv has re-equilibrated in BOTH arms
-- the calibration DV is approximately INVARIANT under the manipulation (which is the timing), by
construction. This is the DV-symmetry-invariance class.

Corroborated by landed, completed evidence (independently verified from the manifests):
- v3_exq_794a ...20260724T063301Z_v3 (the REPAIRED successor; per_arm_gate all six arms green,
  dose_levels_separable true, non_degenerate true) -- BOTH load-bearing criteria FAILED:
    C1_inflation_creates_absolute_overconfidence: n_seeds_overconfident=0 (min_required 2),
      per_level {LO:0, HI:0}, operative_level=null
    C2_broadcast_corrects_under_drift: evaluated_at_level=null, mean_delta=0.0, sd=0.0
      -- and criteria_non_degenerate marks C2 FALSE: it never discriminated at all.
  interpretation.label = "drift_source_insufficient_dv_still_tautological"
  thresholds ABS_FLOOR=0.10, K_SD=1.0; measured broadcast delta on overconfidence_score under drift
  = -0.055 (sd 0.034) at LO and -0.039 (sd 0.020) at HI -- BELOW the floor on both.
  C4_off_off_reproduces_774_ceiling PASSED (-0.192): the 774 ceiling reproduces.
- v3_exq_794 (predecessor): same label; four inflation arms saturated at rv_final EXACTLY 0.01 and
  overconfidence bit-identical across broadcast on/off (delta exactly 0.0 at HI).
- failure_autopsy_V3-EXQ-774_2026-07-17 (confirmed) already adjudicated this substrate_ceiling.

The other two DVs have NEVER been instrumented anywhere: residue specificity and identity
persistence (per_stream_vs/z_self) appear in ZERO of the 1060 manifests. So they are genuinely
UNKNOWN -- not established live, not established inert.

INV-023's CONFIRMING clause requires arm A to beat arm B on calibration AND residue specificity.
Calibration is one of the two required conjuncts and it is the inert one, so the pre-registered
CONFIRMING test cannot be satisfied as written.

## GAP-2 floor -- data-grounded, ready to use whichever way the decision goes
`committed_class_entropy_nats`: 53 manifests, 830 cell values, range 0.0 .. 1.598.
Healthy recent band (707c/955/959) medians 0.99-1.40. Floor 0.3 nats is already pre-registered in
30+ landed manifests across four families (entropy_floor / selected_entropy_floor /
c3_selected_entropy_floor / rung1_entropy_threshold all = 0.3). Gate additionally on
committed_class_entropy_n_classes >= 2 (it is 1 in all 168 cells of 8 manifests -> entropy trivially 0).

---

# PART 2 -- LIVENESS PILOT under user RULING option B (2026-09-22)

Ruling: option B (residue specificity + identity persistence LOAD-BEARING, calibration a
ceiling-declared reported secondary), WITH a mandatory liveness pilot on both load-bearing DVs
before authoring. "If either is inert or pinned, STOP and report -- that is a valid outcome and
converts this to a substrate item rather than a run."

## WRITEBACK assertion -- CONFIRMED AT RUNTIME (2.5a), not inferred
.scratch/probe_writeback_assert.py, one agent, 120 harness steps, intended operating point:
  run_sleep_cycle()                     -> 12 metrics; mech204_recalibration_fired ABSENT;
                                           mech018_residue_integration_fired ABSENT
  force_sleep_cycle_at_eval_boundary()  -> 48 metrics; mech204_recalibration_fired PRESENT = 1.0;
                                           mech018_residue_integration_fired = 1.0;
                                           mech018_residue_trains = 1.0; cycle_history len 1;
                                           state.phase back to WAKING (hence useless post-hoc)
  mech204_recalibration_target = 183.41330460263993
  rv before -> after = 0.005451167181472869 -> 0.005451417174041337   (delta 2.5e-7)
NOTE: 1/183.413 = 0.0054521. rv was ALREADY at the target variance before the recalibration --
the EMA had put it there. The tautology is visible in a single cycle.

## DV-1 residue specificity -- PINNED. Cause isolated to z_world, NOT the residue field.
Warmed (alpha_world=0.9, P0 12 ep + P1 8 ep + SD-070 z_world P0 20 ep, 240 waking steps, 2 seeds):
  seed 0: total_residue 37.41, num_harm_events 666, active_centers 32/32
          natural     harm_mean 36.80416488647461  safe_mean 36.560142517089844  ratio 1.0066745
          after-burst harm_mean 49.39703369140625  safe_mean 48.9774284362793    ratio 1.0085673
          -> harm +12.59, safe +12.42. The field moves; it moves EVERYWHERE AT ONCE.
  seed 1: ratio 1.0004540 -> 1.0014257 (harm +12.62, safe +12.56)

DISCRIMINATOR (.scratch/probe_residue_geometry.py, pure field, no training, no agent stepping):
  two maximally separated synthetic points, |A-B| = 20.0, rbf bandwidth = 1.0
  before: phi(A)=0.066936 phi(B)=0.073535
  after 32 accumulations AT A ONLY: phi(A)=12.866936  phi(B)=0.073535 (UNCHANGED)  ratio 175.0
  => THE RESIDUE FIELD IS SHARPLY SPECIFIC. It is NOT the ceiling. The 32/32 active_centers
     reading is a red herring (centers activate; the field still resolves).

ROOT CAUSE, measured: z_world does not separate harm from non-harm contexts.
  seed 0: harm/non-harm centroid_dist = 0.187763 vs rbf bandwidth 1.000  (ratio 0.188)
          within-cluster spread: harm 0.131291, safe 0.052448
  seed 1: harm/non-harm centroid_dist = 0.080564 vs rbf bandwidth 1.000  (ratio 0.081)
          within-cluster spread: harm 0.120749, safe 0.085289
  => the two classes sit 5-12x CLOSER than the field's own resolution, and on seed 1 the centroid
     separation (0.0806) is SMALLER than the within-cluster spread of BOTH clusters (0.1207,
     0.0853) -- the classes overlap almost completely.
  => residue specificity (harm-residue / non-harm-residue) is STRUCTURALLY PINNED at ~1.0 and
     cannot carry a four-arm contrast. This is the Step 2.5d INERT shape.
  This is the observation-interface binding constraint (z_world), not a residue-geometry ceiling.

## DV-2 identity persistence per_stream_vs['z_self'] -- LIVE (untrained pass)
POST-INIT ticks only (update_per_stream_vs sets V_s := 1.0 definitionally on first observation,
hippocampal/module.py:3810-3813):
  seed 0: n=259 mean 0.9618968 sd 0.0105905 min 0.9244028 max 0.9840844
  seed 1: n=259 mean 0.9774733 sd 0.0090279 min 0.9305623 max 0.9851720
  injected perturbation (corrupt the cached previous z_self, then let it re-converge):
  seed 0: pre 0.9742676 -> departed 0.8946191 -> recovered 0.9612034
  seed 1: pre 0.9807453 -> departed 0.9000210 -> recovered 0.9790575
  => departs ~0.08 and RECOVERS on both seeds: real dynamic range, not a static mean.
  CAVEAT being closed separately: this pass ran on an UNTRAINED agent, so the range could be a
  warm-up transient. Trained re-measurement: .scratch/pilot_dv2_trained.py.

## VERDICT
DV-1 is pinned => the ruling's stated stop condition is met. One of the two load-bearing DVs
cannot move, so option B's load-bearing pair cannot be instantiated as specified. Nothing authored,
nothing queued; V3-EXQ-1076 remains reserved and unused.

## DV-2 TRAINED confirmation -- LIVE, not a warm-up transient
.scratch/pilot_dv2_trained.py, same P0/P1 + SD-070 z_world warm-up as the DV-1 pass,
POST-INIT ticks only:
  seed 0: n=239 mean 0.971355 sd 0.012493 min 0.936900 max 0.996629
          perturb pre 0.9907653 -> departed 0.9119510 -> recovered 0.9959362
  seed 1: n=239 mean 0.978183 sd 0.004847 min 0.950186 max 0.987222
          perturb pre 0.9780289 -> departed 0.8961585 -> recovered 0.9788252
  => departs ~0.079-0.082 and FULLY recovers on both seeds AFTER training. The dynamic range
     survives the warm-up, so the untrained reading was not a transient. DV-2 is LIVE.

## OUTCOME
GFLAG-0415 raised and VERIFIED ON ORIGIN (REE_assembly 918cfb0e38, origin/master;
evidence/planning/governance_flags.v1.json, ree_commit delta items: +1 (GFLAG-0415), no sweep).
Claims INV-023 + MECH-018, type evidence_discrepancy, status open.
V3-EXQ-1076 RELEASED UNUSED -- no script authored, no queue entry, no queue commit.
Score: 1 of the 2 load-bearing DVs under option B is live (identity persistence); the other
(residue specificity) is structurally pinned upstream in z_world. Option B's load-bearing PAIR
cannot be instantiated as specified.


---

## Provenance note (added by orchestrate-20260922-subagent-wave)

This file was produced by session `inv023-science-20260922` under `/Users/dgolden/REE_Working/.scratch/`, which is not version-controlled and is garbage-collected. **GFLAG-0415 cites it as its full trace**, so it was landed here verbatim to keep that citation resolvable. Content is unchanged apart from this note.

Companion records: GFLAG-0415 (`REE_assembly 918cfb0e38`) requests the z_world harm-separability substrate entry and `pending_retest_after_substrate` on INV-023. The separation measurement here is one of two independent 2026-09-22 measurements of the same constraint family; the other is in GFLAG-0414 (INV-069, cross-candidate z_world spread 0.0). Chip `chip-20260922-zworld-separation-quantified-join` owns the question of whether they are ONE constraint -- which must be established, not assumed.
