---
closure_plan:
  id: goal_pipeline
  title: "Goal Pipeline (wanting / liking / drive cascade)"
  registered: 2026-05-08
  scope_claims: [SD-012, SD-014, SD-015, SD-018, SD-049, MECH-117, MECH-216, MECH-229, MECH-230, MECH-295, MECH-307, ARC-030, ARC-032, ARC-036, ARC-051]
  nodes:
    - id: "goal_pipeline:GAP-1"
      title: "MECH-307 anticipatory-affect conjunction architecture"
      phase: 1
      status: done
      severity: load-bearing
      owner_exq: TBD (4-arm discriminative pair pending)
      unblocks_claims: [MECH-307, SD-014]
      depends_on: []
      last_updated: 2026-05-11
      completion_note: "Substrate landed 2026-05-11. Gap 1 implemented as Option-b (split channels VALENCE_POSITIVE_SURPRISE + VALENCE_NEGATIVE_SURPRISE) per user override; Gaps 2/3/4 substrate-landed 2026-05-08. Master flag use_mech307_conjunction propagates to three sub-flags. 309/309 contracts + 7/7 preflight PASS with master OFF. 4-arm discriminative validation deferred to a /queue-experiment session per the 'substrate only first' directive."
    - id: "goal_pipeline:GAP-2"
      title: "SD-049 Phase 2 hybrid encoder behavioural validation (V3-EXQ-514 successor)"
      phase: 2
      status: blocked
      severity: high
      owner_exq: V3-EXQ-514g
      unblocks_claims: [SD-049, SD-015, MECH-229, MECH-230, MECH-117, MECH-216, ARC-030, ARC-032, Q-030]
      depends_on: ["goal_pipeline:GAP-1"]
      last_updated: 2026-05-16
      resume_condition: "Monostrategy root cause has a validated substrate fix (V3-EXQ-567 PASS, supports ARC-065: SP-CEM lifts natural action entropy 0.012->0.497, candidate support 1.007->2.810). V3-EXQ-550 settled that the blocker is NOT z_goal wiring. Retest unblockable once SP-CEM lands in the main agent action path; re-issue the SD-049 Phase 2 behavioural validation via /queue-experiment then. See 2026-05-16 decision-log entry."
    - id: "goal_pipeline:GAP-3"
      title: "SD-012 sustained-drive EMA amendment"
      phase: 3
      status: in-progress
      severity: high
      owner_exq: V3-EXQ-582a
      unblocks_claims: [SD-012, MECH-216, ARC-051]
      depends_on: []
      last_updated: 2026-05-17
      resume_condition: "Option 1 substrate landed 2026-05-17 (drive_ema_alpha). V3-EXQ-582 FAILED: diagnostic grid row 'No arm clears A1 (incl. 0.01)' -> Escalate to Option 2. Root cause: drive_level near-zero throughout episodes (agent well-fed); EMA cannot help when input is consistently low. Post_warmup_cut=100 masked the contacts (all contacts before step 100). Option 2 substrate landed 2026-05-17T13:03Z: GoalConfig.drive_floor (default 0.0 bit-identical); GoalState.update() drive_level_floored=max(drive_level,drive_floor) fed into EMA; contract test_drive_floor_gap3_opt2.py 7/7; full suite 484/484. V3-EXQ-582a queued 2026-05-17T13:03Z (priority 1, any machine): sweeps drive_floor {0.0,0.3,0.6,0.9,1.2} x 3 seeds, drive_ema_alpha=1.0 (Option 1 OFF), no post_warmup_cut. Dry-run confirms floor scaling: mean_eff_benefit_on_contact 0.035->0.098->0.119 across floors. GAP-3 done when V3-EXQ-582a PASSes (A1-A4); on PASS register MECH-306 + mark GAP-3 done. On FAIL follow 582a diagnostic grid (see script docstring)."
    - id: "goal_pipeline:GAP-4"
      title: "MECH-295 drive->liking->approach cascade Tier-1 retest cohort"
      phase: 4
      status: blocked
      severity: high
      owner_exq: V3-EXQ-490g
      unblocks_claims: [MECH-295, ARC-030, MECH-117, Q-040]
      depends_on: ["goal_pipeline:GAP-1", "goal_pipeline:GAP-3"]
      last_updated: 2026-05-16
      resume_condition: "Same monostrategy gate as GAP-2 -- validated substrate fix is V3-EXQ-567 (ARC-065 SP-CEM). Also depends on GAP-3: as of 2026-05-17 the GAP-3 Q2 EMA decision is RESOLVED and the SD-012 sustained-drive EMA substrate has landed; GAP-3 is now in-progress with V3-EXQ-582 (discriminative sweep) queued. GAP-4 retest unblockable once SP-CEM lands AND V3-EXQ-582 PASSes (GAP-3 done). See 2026-05-16 and 2026-05-17 decision-log entries."
    - id: "goal_pipeline:GAP-5"
      title: "SD-049 Phase 3 consumer cascade migration (read-side fidelity)"
      phase: 5
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: []
      depends_on: ["goal_pipeline:GAP-4"]
      last_updated: 2026-05-08
    - id: "goal_pipeline:GAP-6"
      title: "MECH-269b V_s staleness-corrected consumer migration"
      phase: 6
      status: done
      severity: medium
      owner_exq: V3-EXQ-490b
      unblocks_claims: [MECH-269b]
      depends_on: []
      blocking_external: ["external V_s invalidation runtime evolution"]
      last_updated: 2026-05-17
      completion_note: "Substrate fully implemented: HippocampalConfig.use_vs_gate_staleness_lookup, VsRolloutGate.gate() per_stream_staleness path, agent.py end-to-end wiring, HippocampalModule.compute_per_stream_staleness(). V3-EXQ-490b C1 PASS (gate fires); V3-EXQ-490c/e/f completed Q-040 factorial (MECH-295 dominant cause of catatonic-lock, not MECH-269b alone). Monostrategy confound resolved at substrate level by ARC-065 SP-CEM landing as default 2026-05-17. Q-040b behavioral sufficiency of staleness correction alone is a claims-level question continuing under v_s_invalidation_runtime.md; GAP-6 goal_pipeline dependency is satisfied."
---
# Goal Pipeline Plan (wanting / liking / goal-seeding)

**Registered:** 2026-05-08
**Status:** active
**Scope:** close the substrate gaps that prevent the
drive -> wanting -> liking-bridge -> approach-cue loop from producing measurable
behavioural effect. The cohort SD-012, SD-014, SD-015, SD-018, SD-049 (Phase 1 +
Phase 2 + deferred Phase 3), MECH-216, MECH-229, MECH-230, MECH-117, MECH-295,
MECH-307, ARC-030, ARC-032, ARC-036, ARC-051 is wired end-to-end at the module
level but the integration produces the wired-but-inert pattern recurring across
EXQ-471 / EXQ-483 / EXQ-490 / EXQ-514 / EXQ-536 / EXQ-538.

This plan is the durable resume-point for goal-pipeline work across sessions.
When work pauses for adjacent paths (sleep substrate, V_s monostrategy, Tier-1
StepHarness retests), the deviation is logged in the [Decision log](#decision-log)
with a resume condition.

---

## One-line framing

> The drive-to-approach pipeline has all its modules. Drive amplification,
> wanting EMA, schema readout, ResourceEncoder identity, liking-bridge,
> per-axis homeostatic drive, ghost-goal bank, dACC bias, BG action selection
> -- each component passes its unit tests and its substrate-readiness
> diagnostic in isolation. End-to-end the loop produces approach_commit_rate=0
> across every diagnostic that probes it. The fault is at the seams, not in
> the components.

The pattern is named in the substrate_queue.json failure records: cue-side gain
fires on direct injection (EXQ-493 UC4), liking-bridge collapses correctly when
severed (EXQ-493 UC5), the encoder's identity head trains
(SD-049 Phase 2 hybrid encoder PASS smoke), but the conjunction of (a) signed
anticipatory affect, (b) drive-modulated cue salience, (c) per-axis goal-identity
disambiguation, and (d) anticipatory write-at-predicted-location does not
produce a behaviourally distinguishable approach signal.

The gap is not "more design". It is the integration audit + the four-gap
conjunction fix + the sustained-drive amendment + the behavioural validations
that have been deferred behind each successive substrate landing.

---

## Source artefacts

Provenance for every gap and decision in this plan:

| Artefact | Role |
|---|---|
| 2026-05-08 governance-cycle-friday-pm session | Strategic redirect: MECH-307 + MECH-295 added to substrate_queue priority=1; SD-049 / SD-029 / SD-032b / MECH-269b-followup-A failure records updated with EXQ-490f / EXQ-514f / EXQ-536b confounds |
| 2026-05-08 register-mech307-and-sd014-amendment session | MECH-307 registered as candidate / v3_pending; SD-014 evidence_quality_note records both proposals (conjunction fix vs 6-channel amendment) |
| [docs/architecture/anticipatory_affect_conjunction_vs_dual_channel.md](../../docs/architecture/anticipatory_affect_conjunction_vs_dual_channel.md) | MECH-307 four-gap conjunction architecture; comparative analysis vs SD-014 6-channel amendment fallback |
| [docs/architecture/sustained_drive_anticipatory_wanting.md](../../docs/architecture/sustained_drive_anticipatory_wanting.md) | SD-012 amendment scoping (drive collapse at contact); three options (sustained-drive EMA, decoupled wanting, insatiability floor) |
| [docs/architecture/goal_wanting_signal_chain.md](../../docs/architecture/goal_wanting_signal_chain.md) | Provenance map: world_obs -> ResourceEncoder -> z_resource -> z_goal seeding -> VALENCE_WANTING -> E3 score -> action |
| [docs/architecture/mech_295_drive_liking_approach_bridge.md](../../docs/architecture/mech_295_drive_liking_approach_bridge.md) | MECH-295 weak-reading bridge: cue-side gain = f(drive * goal_proximity); severed-bridge falsifier |
| [docs/architecture/sd_049_multi_resource_heterogeneity.md](../../docs/architecture/sd_049_multi_resource_heterogeneity.md) | SD-049 Phase 1 / Phase 2 / Phase 3 implementation note; 4-arm validation grid + Woo/Spelke falsifier branch |
| [docs/architecture/sd_015_z_resource_encoder.md](../../docs/architecture/sd_015_z_resource_encoder.md) | z_resource encoder identity head + magnitude head (Phase 2 hybrid Option C verdict) |
| substrate_queue.json MECH-307 (priority=1) + MECH-295 (priority=1) entries | Names MECH-307 four-gap conjunction as the top-priority unblocker for the goal pipeline per 2026-05-08 governance |
| EXQ-493 MECH-295 weak-bridge validation (6/6 PASS, 2026-04-27/28) | Cue-side bias produces monotone-negative score_bias; severed-bridge collapses to 0; UC1-UC6 pass. Confirms the bridge is wired correctly in isolation |
| EXQ-490f / EXQ-514f / EXQ-536b failure records | Cascade-broken-beyond-rv pattern; force-arm probe with z_goal_inject=0.3 + action-time fraction=1.0 -> approach_commit_rate=0.0 |

---

## Existing substrate (do not duplicate)

Wired and behaving correctly in isolation:

| Component | Location | Status |
|---|---|---|
| SD-012 homeostatic drive (single-axis collapse) | `ree-v3/ree_core/goal/goal_state.py` GoalState.update() | implemented; drive_weight=2.0 default |
| SD-014 4-component valence vector (w/l/h/s) | `ree-v3/ree_core/residue/` ResidueField | candidate; channels written |
| SD-015 z_resource encoder (magnitude head) | `ree-v3/ree_core/latent/stack.py` ResourceEncoder | implemented Phase 1; identity head landed Phase 2 |
| SD-018 resource proximity supervision | `ree-v3/ree_core/latent/stack.py` SplitEncoder.resource_proximity_head | implemented |
| SD-049 Phase 1 multi-resource env-only substrate | `ree-v3/ree_core/environment/causal_grid_world.py` flat-kwargs | phase_1_implemented 2026-05-03 (V3-EXQ-513 PASS 13/13) |
| SD-049 Phase 2 hybrid encoder (identity + magnitude) | `ree-v3/ree_core/latent/stack.py` ResourceEncoder identity_head + LatentState.identity_logits | phase_2_implemented 2026-05-04; V3-EXQ-514 behavioural validation pending |
| MECH-216 E1 schema readout / predictive wanting | `ree-v3/ree_core/predictors/e1_deep.py` schema_readout_head + agent.update_schema_wanting() | implemented; schema_wanting_enabled flag default False |
| MECH-229 wanting/liking behavioural dissociation | E3 + VALENCE_WANTING + VALENCE_LIKING residue channels | active (10 seeds, 3 experiments PASS); evidence is z_world fallback seeding (degenerate per SD-049 failure record) |
| MECH-230 z_goal latent structure | GoalState.update() + z_resource seeding | provisional; v3_pending |
| MECH-295 drive -> liking-bridge -> approach cue | `ree-v3/ree_core/regulators/mech295_liking_bridge.py` | implemented 2026-04-26; V3-EXQ-493 6/6 PASS isolation; cascade behavioural validation deferred |
| MECH-117 wanting/liking dissociation in benefit_eval_head vs z_goal_latent | `ree-v3/ree_core/agent.py` benefit_eval_head + GoalState.update() | candidate; pending_retest_after_substrate (gate: SD-015 + sleep substrate) |
| ARC-030 BG approach-avoidance symmetry (Go + NoGo) | E3 + BG action selection | candidate; ARC-030's path forward is held under SD-012 / sustained-drive resolution |
| ARC-032 hippocampal theta-frequency goal communication | MECH-089 ThetaBuffer + agent goal context | candidate; theta-bypass ablation never run |
| ARC-036 multidimensional valence map | hippocampus + ResidueField 4-channel structure | candidate |
| ARC-051 multi-level wanting hierarchy (contact + schema + replay) | residue field VALENCE_WANTING field | candidate; depends on MECH-216 + MECH-217 + SD-018 firing in concert |

---

## Gap inventory

Six gaps, ordered by leverage. Each is the basis for one row of the
[Status table](#status-table) below.

| Gap | Subject | Severity | Unblocks |
|---|---|---|---|
| **GAP-1** | MECH-307 four-gap conjunction architecture not landed: VALENCE_SURPRISE unsigned, MECH-216 writes only VALENCE_WANTING (no z_beta arousal coupling, no anticipatory liking), MECH-216 writes at current rather than predicted z_world | load-bearing | Q-040, SD-049 Phase 2 behavioural acceptance, SD-015 unblock chain, MECH-111, SD-032b, SD-018, MECH-112, MECH-295 cascade behavioural validation |
| **GAP-2** | SD-049 Phase 2 V3-EXQ-514 behavioural validation never PASSed: 514f reclassified non_contributory as pre-MECH-307 affect-stream confound; identity-recovery + wanting!=liking dissociation acceptance criteria untested under MECH-307-fixed substrate | load-bearing | SD-015, MECH-229 (non-degenerate retest), MECH-230, MECH-117 retest, MECH-216 retest, ARC-030, ARC-032, Q-030 |
| **GAP-3** | SD-012 sustained-drive amendment: drive_level collapses to ~0.005 at exact step the agent contacts a resource (energy resets toward 1.0); multiplier (1 + 2*0.005) cancels almost all benefit amplification SD-012 was intended to provide | high | MECH-295 cascade non-collapse, MECH-216 schema wanting threshold crossing, SD-014 wanting EMA non-degeneration, ARC-030 approach drive |
| **GAP-4** | MECH-295 cascade behavioural validation deferred: V3-EXQ-493 isolation 6/6 PASS confirms substrate, but EXQ-490f / EXQ-536a/b force-arm probe shows downstream cascade inert under realistic policy state (cue_fires=0 at relaxed activation floors; approach_commit_rate=0 even at z_goal_inject=0.3 + action-time fraction=1.0) | high | EXQ-471 catatonic-lock factorial diagnosis (Q-040), MECH-295 promotion, SD-029 substrate retest |
| **GAP-5** | SD-049 Phase 3 SD-032 consumer cascade reading per_axis_drive directly: AIC, PCC, pACC, dACC adaptive control, salience-coordinator, override-regulator, MECH-295 liking-bridge currently read goal_state._last_drive_level (collapsed scalar) | medium | SD-032b cascade fidelity, MECH-258 + MECH-260 calibration; refactor not on acceptance-criterion path for any current claim |
| **GAP-6** | MECH-269b-followup-A staleness-corrected V_s in VsRolloutGate.gate: lower-priority follow-on after V3-EXQ-490b clears; gates the V_s monostrategy resolution that interacts with goal-pipeline behavioural tests | medium | SD-029 retest cohort (cross-plan with sleep_substrate_plan via V_s invalidation runtime) |

GAP-3 (sustained-drive amendment) is intentionally separated from GAP-1 even
though both touch SD-012 / MECH-216. Reason: GAP-1 is the four-gap conjunction
fix at the affect-write site; GAP-3 is the drive-multiplier fix at the
goal-seeding site. They interact (the same EXQ-536b force-arm probe documents
both confounds) but the fixes are independently small and independently
falsifiable. Sequencing them serially keeps each PASS interpretable.

---

## Sequenced plan

Six phases. Each phase is small, verifiable, and unblocks at least one
downstream item. Phases are ordered by leverage and by what each unblocks.
Where work depends on adjacent paths (sleep substrate, V_s monostrategy,
StepHarness retest cohort), that is called out as a deviation in the
[Decision log](#decision-log).

### Phase 1: MECH-307 four-gap conjunction architecture (GAP-1)

Top priority per substrate_queue priority=1. Without this, every downstream
behavioural test of the goal pipeline confounds the conjunction-architecture
fault with the test's own claim.

Deliverables:

1. Gap 1: signed VALENCE_SURPRISE. Either (a) store signed PE in VALENCE_SURPRISE
   (negative for negative PE, positive for positive PE), with consumers reading
   sign or magnitude as needed; or (b) split into VALENCE_POSITIVE_SURPRISE and
   VALENCE_NEGATIVE_SURPRISE as separate channels. Default: (a) behind config
   flag `surprise_signed` (~5 lines, one field semantics change).
2. Gap 2: MECH-216 schema readout writes partial VALENCE_LIKING amplitude in
   addition to VALENCE_WANTING, AND raises z_beta arousal proportional to
   schema_salience. Two write sites added next to existing VALENCE_WANTING write
   in `agent.py:3753-3757`.
3. Gap 3: subsumed by Gap 2 architecturally (z_beta arousal write is the same
   line as the schema_salience-driven liking write); named separately because
   the z_beta path has a distinct downstream consumer (MECH-093 E3 heartbeat).
4. Gap 4: MECH-216 writes at the predicted z_world (E1's forward prediction),
   not the current z_world. Replace `self._current_latent.z_world` at
   `agent.py:3754` with the cached `e1_prior` predicted next-state z_world.
5. ~40 lines of code total per the 2026-05-08 design doc estimate.
6. Validation EXQ: 4-arm discriminative-pair experiment per the design doc
   Validation Experiment section. Acceptance: arm with all four gaps fixed
   produces non-zero `cue_fires + dacc_bias + approach_commit` in the relaxed
   floors arm relative to baseline; arm with any one gap re-disabled
   collapses to baseline (the conjunction-architecture falsifier).

Fallback (per docs/architecture/anticipatory_affect_conjunction_vs_dual_channel.md):
if MECH-307 conjunction fix does not produce the expected derived states, the
SD-014 6-channel amendment (add VALENCE_EXCITEMENT + VALENCE_DREAD as discrete
channels) is the architectural fallback. The amendment is registered in
SD-014's evidence_quality_note but not yet applied to the registry pending
MECH-307 outcome.

Phase 1 is the gate for everything else in this plan. Phases 2-6 do not start
until Phase 1's discriminative validation arm PASSes.

### Phase 2: SD-049 Phase 2 V3-EXQ-514 behavioural validation under MECH-307-fixed substrate (GAP-2)

V3-EXQ-514f reclassified non_contributory 2026-05-08 because the affect-stream
mixed harm + benefit surprise (classifier_loss 0.015-0.023 vs target <0.005;
probe_acc 0.48-0.53 vs target >0.70). The retest under signed VALENCE_SURPRISE
is the discriminative evidence on whether SD-049 Phase 2 hybrid encoder
delivers the goal_resource_r lift / identity-recovery / wanting!=liking
trajectory dissociation acceptance criteria.

Deliverables:

1. V3-EXQ-514g (or successor letter): re-queue V3-EXQ-514's 4-arm sweep with
   MECH-307 four-gap conjunction landed. Phased training preserved per Phase 2
   verdict (P0 joint -> P1 freeze classifier -> P2 evaluate). Pre-registered
   acceptance per design doc Validation Experiment section: ARM_2 -> ARM_0
   `goal_resource_r` lift >= 0.4 (target 0.066 -> >= 0.5); identity-recovery
   linear-probe accuracy > 0.6 in ARM_2; wanting_target != liking_target
   trajectory fraction >= 0.6 in ARM_2 (near zero in ARM_0 / ARM_1); per-axis
   drive ANOVA on z_goal cluster IDs p < 0.01 in ARM_2. Five-row interpretation
   grid + Woo/Spelke-style falsifier branch routing MECH-229 to
   substrate_conditional with V4-1 multi-agent ecology dependency on flat-failure.
2. Acceptance gates promotion of MECH-229 (non-degenerate retest, per SD-049
   failure record), MECH-230 (z_goal latent structure), MECH-117 (wanting /
   liking dissociation in benefit_eval_head vs z_goal_latent), MECH-216 (E1
   schema-conditioned wanting), and the SD-049 v3_pending clearance.
3. Row-6 falsifier branch (joint ARM_2 + ARM_3 failure): routes MECH-229 to
   substrate_conditional with V4-1 multi-agent ecology dependency. This is
   not a Phase 3 trigger (Phase 3 is the consumer-cascade refactor; the row-6
   branch is a substrate-ceiling escalation).

### Phase 3: SD-012 sustained-drive amendment (GAP-3)

Per `sustained_drive_anticipatory_wanting.md`, the multiplier
`(1 + drive_weight * drive_level)` cancels at contact because energy resets
toward 1.0 the moment a resource is consumed. Three substrate options listed
in increasing order of architectural change.

Deliverables:

1. Option 1 (cheapest): sustained-drive EMA. Replace instantaneous `drive_level`
   in the multiplier with a slow EMA (`drive_ema_alpha` config knob, default
   0.05; first PASS arm). Bit-identical OFF when alpha=1.0.
2. Option 2 (decoupled wanting): wanting amplitude as separate state from
   drive_level, updated at schema-cue events (MECH-216 fires) and at contact,
   decaying on a slow timescale independent of energy reset. Tracks the
   Berridge / Robinson sustained motivational state account.
3. Option 3 (insatiability floors): chronic homeostatic deficits maintain a
   baseline wanting tone independent of recent consumption. Most disruptive;
   requires a per-axis "deficit-history" buffer.
4. Validation: discriminative experiment landing Option 1 first; Options 2-3
   gated on Option 1 outcome.
5. Acceptance: max_effective_benefit > benefit_threshold (currently 0.1) at
   contact under realistic policy state, with the persistent attractor seeding
   on the Phase 1 corrected substrate. Falsifier: drive_ema_alpha sweep
   producing monotone seeding-rate vs alpha curve.

The lit-pull anchored in `sustained_drive_anticipatory_wanting.md` is a
companion task; the substrate amendment lands first, the lit-pull cites
biology in parallel.

### Phase 4: MECH-295 cascade behavioural validation (GAP-4)

V3-EXQ-493 confirms MECH-295 substrate is wired correctly in isolation (UC1-UC6
PASS). The cascade (drive amplification -> liking-stream gain -> approach cue)
fails in realistic experiments because the upstream wiring (Phase 1) and the
drive multiplier (Phase 3) prevent the bridge's input from ever firing.

Deliverables:

1. V3-EXQ-490g (or successor letter): re-queue Q-040 cascade test with Phase 1
   + Phase 3 landed. Acceptance: non-zero cue_fires + dacc_bias +
   approach_commit in relaxed-floor arm relative to baseline (the explicit
   target documented in MECH-295 failure record for EXQ-490f).
2. EXQ-471a / EXQ-475a / EXQ-483c / EXQ-490g / EXQ-524a Tier-1 retest cohort
   under StepHarness: re-queue the cohort with the canonical
   sense / update_z_goal / update_residue sequence + Phase 1 + Phase 3
   landed. The StepHarness migration was landed 2026-05-08 in
   `ree-v3/experiments/_harness.py`; the retest cohort consumes that
   migration. Tier-1 PASS gates Tier-2 (514f-style retest) and Tier-3
   (490e/f, 524, 536-cluster) per the 2026-05-08 governance redirect.
3. Acceptance gates promotion of MECH-295 to provisional and clears the
   EXQ-471 catatonic-lock factorial diagnosis (Q-040).

### Phase 5: SD-049 Phase 3 SD-032 consumer cascade (GAP-5)

Cleanup-of-substrate-coverage refactor. Migrate AIC, PCC, pACC, dACC adaptive
control, salience-coordinator, override-regulator, MECH-295 liking-bridge from
reading `goal_state._last_drive_level` (collapsed scalar) to optionally reading
`obs_dict['per_axis_drive']` directly when SD-049 per-axis is on.

Deliverables:

1. Per-consumer migration order: start with MECH-295 liking-bridge (simplest);
   then salience-coordinator; then dACC; then AIC / PCC / pACC. Each consumer
   preserves bit-identical OFF when `per_axis_drive` is None or SD-049 per-axis
   is OFF.
2. Each consumer's `tick()` function gains an optional
   `per_axis_drive: Optional[Sequence[float]]` kwarg.
3. Test suite run after each consumer.
4. Trigger pending_substrate_reconfirmation flag on SD-012-emergent invariants
   per the invariant-types governance rule (the cascade changes how SD-012's
   drive_level interface is consumed across the cluster).
5. No new validation experiment required if Phase 5 is purely a refactor (no
   behavioural change); a regression run on the V3-EXQ-514 successor may be
   sufficient to confirm bit-identical OFF and activation correctness.

Phase 5 is intentionally low-priority. Per the queue entry's `ready_blocked_by`
field, "Cascade is a cleanup-of-substrate-coverage refinement, not an
acceptance-criterion prerequisite." None of the goal-pipeline acceptance
criteria require Phase 5 to land; Phases 1-4 are sufficient. Phase 5 is the
right next step if and only if Phase 4 PASSes a Tier-3 retest and reveals a
remaining drive-cascade fidelity issue.

### Phase 6: MECH-269b-followup-A staleness-corrected V_s in VsRolloutGate (GAP-6)

Lower-priority follow-on per substrate_queue. Tracked here because
goal-pipeline behavioural tests (Phase 4 Tier-3 cohort, SD-029 retest) interact
with V_s monostrategy: a monomodal policy cannot generate balanced
agent-vs-env event distributions for C2/C3 measurement, and reef enrichment
(SD-050) did not break monostrategy at this scale.

Deliverables:

1. Wire `MECH-284 StalenessAccumulator.snapshot()` correction into
   `VsRolloutGate.gate(...)` so the gate's V_s reading is staleness-corrected
   at use time, not just snapshot time. Implementation hint already in
   substrate_queue.json MECH-269b-followup-A entry.
2. Validation: V3-EXQ-490b (already pending in queue) is the primary
   diagnostic. Acceptance: Q-040 factorial cleanly distinguishes MECH-269b
   vs MECH-295 as dominant cause of the EXQ-471 catatonic-lock signature.
3. Phase 6 is independently scheduled by the V_s invalidation runtime work in
   sleep_substrate_plan / sd033_governance_plan; this plan tracks its
   dependency rather than owning the implementation.

---

## Status table

The resume primitive. Updated every session that touches goal-pipeline work.
See [Resume ritual](#resume-ritual) below.

| Gap | Phase | Status | Blocking on | Next action | Owner-EXQ | Last updated |
|---|---|---|---|---|---|---|
| GAP-1 | 1 | done | (substrate landed 2026-05-11; 4-arm validation pending separate session) | Queue 4-arm discriminative pair via /queue-experiment under master flag use_mech307_conjunction=True. **NOTE 2026-05-11 (EXQ-550 review):** V3-EXQ-550 FAIL sustains MECH-269 V_s monostrategy substrate-level reading at no-training depth; same run surfaced wired-but-inert z_goal pipeline (1200/1200 update_z_goal calls, z_goal_norm_peak=0.0) -- see decision-log 2026-05-11 entry. V3-EXQ-551 (pipeline-entropy diagnostic) + V3-EXQ-552 (forced-exploration warmup) queued by parallel sessions to narrow mechanism before trained-z_goal follow-up. | TBD (4-arm discriminative pair) | 2026-05-11 |
| GAP-2 | 2 | blocked | Phase 1 PASS | Re-queue V3-EXQ-514 successor with phased training under MECH-307-fixed substrate | V3-EXQ-514g (TBD) | 2026-05-08 |
| GAP-3 | 3 | in-progress | V3-EXQ-582a result | Option 1 (EMA) substrate landed + EXQ-582 FAILED 2026-05-17 (no arm cleared A1; drive near-zero all episode). Option 2 (drive_floor) substrate landed 2026-05-17T13:03Z (GoalConfig.drive_floor, 7/7 contracts, 484/484 suite). EXQ-582a queued (priority 1, floor sweep {0.0,0.3,0.6,0.9,1.2} x 3 seeds, no warmup_cut). On 582a PASS: GAP-3 done + register MECH-306. On FAIL: follow 582a diagnostic grid. | V3-EXQ-582a | 2026-05-17 |
| GAP-4 | 4 | blocked | Phase 1 + Phase 3 PASS | Re-queue Tier-1 cohort under StepHarness with Phase 1 + Phase 3 landed | V3-EXQ-490g, V3-EXQ-471a, V3-EXQ-475a, V3-EXQ-483c, V3-EXQ-524a | 2026-05-08 |
| GAP-5 | 5 | deferred | Phase 4 Tier-3 outcome | Migrate consumer cascade only if Phase 4 reveals drive-cascade fidelity gap | n/a (refactor) | 2026-05-08 |
| GAP-6 | 6 | done | (none) | Substrate implemented (use_vs_gate_staleness_lookup wired end-to-end). V3-EXQ-490b C1 PASS; 490c/e/f factorial shows MECH-295 dominant cause. Monostrategy resolved by ARC-065 SP-CEM default 2026-05-17. Q-040b behavioral sufficiency continues under v_s_invalidation_runtime.md. | V3-EXQ-490b | 2026-05-17 |

Status values: `open`, `in-progress`, `blocked`, `paused`, `done`, `deferred`,
`tracked`. A `paused` row carries a resume condition in the
[Decision log](#decision-log). A `tracked` row indicates the implementation is
owned by another plan; this plan only consumes the result.

---

## Test cohort

The discriminative experiments by phase. EXQ IDs are pre-registered where
landed; "TBD" indicates the queue-experiment skill must allocate the next
letter at write time.

### Phase 1 cohort (MECH-307 conjunction)

| EXQ | Subject | Acceptance | Status |
|---|---|---|---|
| TBD | MECH-307 4-arm conjunction discriminative pair (all-four-gaps-fixed vs each-gap-removed) | non-zero cue_fires + dacc_bias + approach_commit in all-fixed arm; collapse to baseline in each lesioned arm | not queued |

### Phase 2 cohort (SD-049 Phase 2 behavioural under MECH-307)

| EXQ | Subject | Acceptance | Status |
|---|---|---|---|
| V3-EXQ-514g (TBD letter) | SD-049 Phase 2 reef behavioural validation under MECH-307-fixed substrate | classifier_loss < 0.005; probe_acc > 0.70; goal_resource_r lift ARM_2-ARM_0 >= 0.4; wanting!=liking trajectory fraction >= 0.6 in ARM_2; per-axis-drive ANOVA p < 0.01 | gated on Phase 1 PASS |

### Phase 3 cohort (SD-012 sustained-drive amendment)

| EXQ | Subject | Acceptance | Status |
|---|---|---|---|
| TBD | SD-012 drive_ema_alpha sweep discriminative pair | max_effective_benefit > benefit_threshold at contact; persistent attractor seeds on corrected substrate; monotone seeding-rate vs alpha | not queued |

### Phase 4 cohort (Tier-1 StepHarness + Q-040 cascade retest)

| EXQ | Subject | Prior verdict | Re-run trigger |
|---|---|---|---|
| V3-EXQ-490g | Q-040 cascade test under MECH-307 + SD-012 amendment + StepHarness | EXQ-490f non_contributory (pre-MECH-307 confound) | Phase 1 + Phase 3 PASS |
| V3-EXQ-471a | EXQ-471 catatonic-lock factorial under StepHarness | EXQ-471 non_contributory (pre-MECH-307 + drive collapse confound) | Phase 1 + Phase 3 PASS |
| V3-EXQ-475a | EXQ-475 retest under StepHarness | EXQ-475 superseded (update_z_goal TypeError) | Phase 1 + Phase 3 PASS |
| V3-EXQ-483c | EXQ-483 SD-037 retest under StepHarness | EXQ-483 superseded (update_z_goal TypeError) | Phase 1 + Phase 3 PASS |
| V3-EXQ-524a | EXQ-524 retest under StepHarness | EXQ-524 superseded (update_z_goal TypeError) | Phase 1 + Phase 3 PASS |

Tier-1 acceptance per experiment: non-zero approach_commit_rate in the relaxed-floor
arm relative to baseline; cue_fires > 0; dacc_bias non-zero. Tier-2
(514f-style retest) and Tier-3 (490e/f, 524, 536-cluster) gated on Tier-1
PASS, per the 2026-05-08 governance redirect.

### Phase 5 cohort (SD-049 Phase 3 consumer cascade)

| EXQ | Subject | Acceptance | Status |
|---|---|---|---|
| (regression on V3-EXQ-514 successor) | bit-identical OFF + activation correctness for per-axis drive consumer migration | identical metrics with per_axis_drive=None vs SD-049-OFF | not queued (Phase 5 deferred) |

### Phase 6 cohort (MECH-269b-followup-A)

| EXQ | Subject | Acceptance | Status |
|---|---|---|---|
| V3-EXQ-490b | Q-040 factorial distinguishing MECH-269b vs MECH-295 as dominant cause of EXQ-471 catatonic-lock | clean factorial separation in 2x2 design | already pending in queue |

---

## Cross-references

| Plan node | substrate_queue.json sd_id | claims.yaml claim | Design doc |
|---|---|---|---|
| GAP-1 / Phase 1 | MECH-307 (priority=1) | MECH-307; SD-014 (fallback amendment) | anticipatory_affect_conjunction_vs_dual_channel.md |
| GAP-2 / Phase 2 | SD-049-PHASE-2 | SD-049, SD-015, MECH-229, MECH-230, MECH-117, MECH-216, ARC-030, ARC-032, Q-030 | sd_049_multi_resource_heterogeneity.md |
| GAP-3 / Phase 3 | SD-012 (registry-only; no queue entry yet) | SD-012, MECH-216, ARC-051 | sustained_drive_anticipatory_wanting.md |
| GAP-4 / Phase 4 | MECH-295 (priority=1) | MECH-295, ARC-030, MECH-117, Q-040 | mech_295_drive_liking_approach_bridge.md |
| GAP-5 / Phase 5 | SD-049-PHASE-3 (priority=3, deferred) | SD-032b (read-side fidelity); no acceptance gate | sd_049_multi_resource_heterogeneity.md |
| GAP-6 / Phase 6 | MECH-269b-followup-A (priority=1) | MECH-269b | v_s_invalidation_runtime.md |

The substrate_queue.json design_doc field updates are made in the same session
as this plan registration: MECH-307, MECH-295, SD-049 (Phase 1 main), SD-049-PHASE-2,
SD-049-PHASE-3, MECH-269b-followup-A all updated to point to this plan as the
canonical sequencing reference, in addition to their existing mechanism-specific
design docs (those remain the authoritative single-claim references; the plan
is the umbrella).

### Boundary with sleep_substrate_plan.md

The SD-049 sleep-on cohort (V3-EXQ-514 family configured with `use_sleep_loop=True`,
`sws_enabled=True`, `rem_enabled=True`) sits at the boundary of both plans:

- **goal_pipeline_plan.md owns the SD-049 substrate** (Phase 1 env-only,
  Phase 2 hybrid encoder, Phase 3 consumer cascade), the wanting/liking
  behavioural acceptance criteria, and the wanting != liking trajectory
  fraction validation.
- **sleep_substrate_plan.md owns the sleep-loop side of validation**: the
  SleepLoopManager Phase A/B/C/D/E scaffolding, MECH-204 precision
  recalibration consumer, MECH-272 routing-gate downstream consumer wiring,
  MECH-273 replay-derived training targets, MECH-285 staleness-priority
  sampling.

When V3-EXQ-514 successors are configured with sleep flags ON, both plans'
acceptance criteria apply. The sleep flags are not part of the Phase 1 / Phase 2
goal-pipeline validation acceptance (which can run with `use_sleep_loop=False`);
they are part of the V3 full-stack validation that gates SD-049's promotion
beyond v3_pending and the SD-017 + MECH-204 + sleep cluster's full
end-to-end validation. Either plan may sequence a V3-EXQ-514 successor with
its respective flag stack; the other plan's status table tracks the dependency
under a `tracked` row.

---

## Decision log

Append-only. Every architectural choice + every deviation pause / resume.

### 2026-05-17 - GAP-6 DONE: MECH-269b staleness-corrected V_s consumer migration closed

**GAP-6 closure.**

The MECH-269b-followup-A substrate (staleness-corrected V_s in `VsRolloutGate.gate()`) is
fully implemented end-to-end:

- `HippocampalConfig.use_vs_gate_staleness_lookup` flag (False default; also exposed via
  `REEConfig.use_vs_gate_staleness_lookup` and wired through `from_dims`)
- `VsRolloutGate.gate()` and `gate_stream()` accept `per_stream_staleness` dict; when
  `use_staleness_lookup=True`, compute `effective_vs = raw_vs - staleness[stream]` before
  threshold comparison
- `REEAgent` passes `self.hippocampal.compute_per_stream_staleness()` to `gate()` calls
  when the flag is on (agent.py lines ~2271 / ~2307 / ~3501)
- `HippocampalModule.compute_per_stream_staleness()` exists and draws from the
  `StalenessAccumulator` (MECH-284 Phase-3, implemented 2026-04-24)

**Experimental lineage (Q-040 factorial):**

| EXQ | Outcome | Finding |
|-----|---------|---------|
| V3-EXQ-490b | FAIL / superseded | C1 PASS (gate fires at override thresholds); C2+C3 FAIL (zero approach_commit, zero dACC score-bias -- MECH-295 dominant, not MECH-269b alone) |
| V3-EXQ-490c | FAIL / superseded | Added MECH-295 liking-bridge ON arm; still catatonic-lock |
| V3-EXQ-490e | FAIL / non_contributory | Strengthened bridge seeding; cue fires confirmed but approach_commit=0 |
| V3-EXQ-490f | FAIL / superseded | Further parametric sweep; monostrategy confound identified as primary block |

**Q-040 factorial verdict:** MECH-295 (liking-bridge) is the dominant cause of the EXQ-471
catatonic-lock, not MECH-269b alone. The staleness gate fires (C1), but behavioral
sufficiency (Q-040b) is blocked by the monostrategy confound, not by missing staleness
wiring.

**Monostrategy resolved:** ARC-065 SP-CEM landed as main-path default 2026-05-17
(WORKSPACE_STATE.md entry). The candidate-generation monostrategy that was confounding
all goal-pipeline behavioural tests (EXQ-471 / 490 / 514 / 536 lineage) is now removed at
the substrate level. This satisfies the "V_s monostrategy resolution" condition that GAP-6
was blocking on.

**Scope boundary:** Q-040b behavioral sufficiency of the staleness correction *alone*
remains a claims-level open question under MECH-269b. It continues under
`v_s_invalidation_runtime.md` (Phase 2 T2 forward-predictor path or the
combined-cluster combined-arm path). The goal_pipeline infrastructure dependency -- that
the monostrategy confound not interfere with Tier-3 behavioural tests -- is satisfied.

**Status transition:** GAP-6 open/tracked -> done.

### 2026-05-17T13:03Z - GAP-3 Option 2 escalation: drive_floor substrate + V3-EXQ-582a queued

V3-EXQ-582 FAILED (all 5 alphas incl. 0.01; diagnostic grid row "No arm clears A1"
-> escalate to Option 2). Root cause: drive_level near-zero throughout the episode
(agent well-fed); EMA cannot help when the EMA INPUT is consistently low. Additionally
POST_WARMUP_CUT=100 masked all contacts (every contact occurred before step 100 in
the 200-step episodes). Option 2 proceeds per the pre-registered diagnostic grid.

**Substrate landed** (ree-v3 466e7db):
- `GoalConfig.drive_floor: float = 0.0` (default, bit-identical OFF)
- `GoalState.update()`: `drive_level_floored = max(drive_level, drive_floor)` applied
  before the EMA -- guarantees trace >= drive_floor in steady state, giving
  `effective_benefit >= benefit * (1 + drive_weight * drive_floor)` at every contact.
- `config.py from_dims()` wired with `drive_floor` kwarg.
- Contract `test_drive_floor_gap3_opt2.py` 7/7 PASS; full suite 484/484 PASS.

**V3-EXQ-582a queued** (priority 1, any machine, supersedes V3-EXQ-582):
- Sweeps `drive_floor` in {0.0, 0.3, 0.6, 0.9, 1.2} x 3 seeds.
- `drive_ema_alpha=1.0` (Option 1 OFF; testing Option 2 in isolation).
- No POST_WARMUP_CUT: floor applies from step 0, no cold-start transient.
- First-PASS arm: floor=0.9 (predicted: effective_benefit ~ 0.03 * 2.8 = 0.084 at
  first contact; accumulates to > 0.1 by the 2nd-3rd contact within an episode).
- Dry-run confirms floor scaling: mean_eff_benefit_on_contact = 0.035 / 0.056 /
  0.077 / 0.098 / 0.119 across floors 0.0 -> 1.2.
- On PASS (A1-A4): GAP-3 done, register MECH-306 via governance.
- On FAIL: follow 582a diagnostic grid (see script docstring). If no floor clears A1
  (incl. 1.2), escalate to Option 3 (MECH-216 schema-driven wanting).

Note: prior session `resume_condition` recommended waiting for V3-EXQ-587/588
(infant substrate contact density gate). User explicitly chose to proceed with
Option 2 now per the EXQ-582 diagnostic grid. The 582a dry-run confirms contacts
DO occur without the warm-start gate (n_contacts > 0 in 40-step eval for 2/3
seeds). The warm-start prerequisite may have been overstated; 582a will resolve it.

**Status:** GAP-3 remains in-progress; owner_exq updated to V3-EXQ-582a.

---

### 2026-05-17 - GAP-3 Q2 RESOLVED + SD-012 sustained-drive EMA (Option 1) substrate landed; V3-EXQ-582 queued

User invoked goal-pipeline GAP-3. GAP-3 was `open`/unstarted (no EMA knob in
goal.py; the design memo's reserved EXQ-539-541 had been reused for MECH-204
work). Surfaced the registered open question **Q2** (the EMA timescale) plus a
plan-of-record inconsistency: the plan body/Q2 proposed knob `drive_ema_alpha`
default 0.05; the design memo used `alpha_drive_trace` operating value 0.02;
the lit synthesis `wanting_liking_sleep_consolidation_synthesis.md` endorses a
30-60 step half-life window and flags 0.05 (~14-step) as too fast.

**User decisions:** (Q2) canonical knob `drive_ema_alpha`, config default 1.0
(bit-identical OFF, non-negotiable), first-PASS arm **alpha=0.02** (lit-
anchored ~35-step half-life), discriminative sweep {0.01, 0.02, 0.2, 1.0};
(implementation sub-choice) **zero-init** the trace rather than first-obs init,
explicitly accepting the ~1/alpha-step per-episode cold-start transient as a
documented confound the validation EXQ accounts for.

**Landed (via /implement-substrate):** `GoalConfig.drive_ema_alpha` (goal.py,
default 1.0); `GoalState.update()` EMA recursion
`_drive_trace = (1-alpha)*_drive_trace + alpha*drive_level` then the SD-012
multiplier uses `_drive_trace`; `GoalState.reset()` zeroes `_drive_trace` (the
Q2 cold-start is per-episode -- caught during code review when tracing the
eval-loop reset() semantics, a substrate gap fixed before queuing);
`REEConfig.from_dims` passthrough mirroring `drive_weight`. Backward compat is
load-bearing and verified: alpha=1.0 -> trace==drive_level regardless of init
(contract C1/C2), full contract+preflight suite 426/426 green, an existing
drive-modulated goal experiment runs unchanged under default config. New
contract `tests/contracts/test_sustained_drive_ema_gap3.py` 7/7 (C1 default,
C2 bit-identical-to-instantaneous, C3 no contact-collapse, C4 ~35-step
half-life, C5 monotone falsifier curve = trace-at-contact post-warmup, C6
zero-init cold-start bound, C7 reset() re-zeroes). Docs reconciled: SD-012 doc
gained a "Sustained-drive amendment" section; the design memo's
`alpha_drive_trace` name marked superseded; ree-v3/CLAUDE.md SD section entry.

**Scope discipline:** `claims.yaml` deliberately NOT modified. Registering
**MECH-306 sustained_drive_trace** (mechanism_hypothesis; EXQ-536a empirical
anchor; lit anchors per the wanting/liking synthesis) is the governance
follow-on, gated on V3-EXQ-582 PASS -- consistent with the recent GAP-closure
convention ("GAP unblocks but does not itself promote").

**Validation:** V3-EXQ-582 (`v3_exq_582_gap3_sustained_drive_ema_sweep`,
diagnostic, claim_ids=[], priority 2) queued -- 4 alpha arms x 3 seeds on the
EXQ-536a goal-seeding regime, ungated per-step `update_z_goal` (substrate-
faithful time-EMA; diverges from 536a's benefit-gate by design), trace read
from `goal_state._drive_trace` post-update, metrics over an all + fixed
post-warmup (cut=100) window. PASS = A1 drive-trace@contact(0.02)>0.10
(vs 536a 0.005) & A2 >=2/3 seeds clear benefit_threshold & A3
z_goal_active_fraction>0.20 & A4 monotone alpha curve with the OFF arm at the
536a value. Script carries the mandatory diagnostic interpretation grid
(Option-2 escalation / regime-drift / downstream-bottleneck routings).

**Status:** GAP-3 open -> in-progress (NOT done -- the EXQ has not run; per
the never-mark-complete-before-artifact rule). On 582 PASS: GAP-3 -> done,
MECH-306 to governance, GAP-4's GAP-3 prerequisite satisfied (GAP-4 still
separately gated on the ARC-065 SP-CEM monostrategy fix). GAP-4
resume_condition updated to reflect Q2 resolved + EMA landed. ree-v3 and
REE_assembly committed.

### 2026-05-16 - Closure-map reconciliation: GAP-2 / GAP-4 monostrategy blocker has a validated substrate fix (ARC-065 SP-CEM)

Staleness pass (status tables 5-8 days behind runner, now V3-EXQ-581).

GAP-2 (SD-049 Phase 2 behavioural) and GAP-4 (MECH-295 cascade Tier-1
retest) have been `blocked` since 2026-05-08 on the z_goal /
monostrategy root cause. Reconciled evidence:
- V3-EXQ-550 FAIL (supports MECH-269): wired z_goal alone does NOT
  break monostrategy (entropy delta ~0 at no-training depth). Settles
  that the blocker is NOT missing z_goal wiring.
- V3-EXQ-551 / 551a / 570 PASS (diagnostic): bottleneck localised to
  E2-rollout / CEM-candidate collapse, not the goal pipeline.
- V3-EXQ-560 / 561 / 562 non_contributory: the diversity stack
  (ARC-065 / MECH-313/314/320 arms) does not break monostrategy under
  the OLD collapsed CEM.
- V3-EXQ-567 PASS (supports ARC-065): SP-CEM lifts natural action
  entropy 0.012 -> 0.497, candidate support 1.007 -> 2.810 -- the
  validated substrate fix for exactly this root cause.

GAP-2 / GAP-4 stay `blocked` (behavioural retest not yet run) but the
resume condition is now precise: gated on SP-CEM landing in the main
agent action path + retest re-issue via /queue-experiment, NOT on
further z_goal wiring (V3-EXQ-550 closed that question). last_updated
bumped on both nodes.

### 2026-05-11 - V3-EXQ-550 FAIL: MECH-269 V_s monostrategy substrate-level reading sustained at no-training depth; new "wired-but-inert z_goal" gap surfaced

V3-EXQ-550 ran 2026-05-11T19:01Z (DLAPTOP-4.local) and registered FAIL on the
pre-registered pass rule `action_class_entropy(ON) - action_class_entropy(OFF)
>= 0.10 in >= 2/3 seeds`. All 3 seeds returned `action_class_entropy = 0.0` in
BOTH arms and per-seed action distributions bit-identical between ARM_OFF and
ARM_ON (seed 42 class "1" 1200/1200 both arms; seed 7 class "2" 1200/1200 both
arms; seed 17 class "2" 1200/1200 both arms). Per the pre-registered
interpretation grid in the manifest's `evidence_direction_note`:
**FAIL supports the substrate-level reading of MECH-269 V_s monostrategy at
no-training depth.** Does NOT rule out that a trained z_goal pipeline would
change the picture; the test was a no-training random-init probe by design.
MECH-269's hold on SD-029 stands at this depth.

**Additional finding NOT in the pre-registered grid (separate substrate gap):**
the diagnostic incidentally surfaced a wired-but-inert pattern in the z_goal
activation path. ARM_ON recorded `z_goal_update_calls = 1200` (every tick of
every seed; the per-step `update_z_goal(info['benefit_exposure'])` plumbed in
the experiment script fired correctly) but `z_goal_norm_peak = 0.0` on every
seed. The goal pipeline is wired and called but functionally inert: GoalState
mutates without ever producing a non-zero `z_goal` norm under this probe's
benefit-exposure feed. Mechanism is unconfirmed (candidates: GoalState
internal threshold gating, benefit_exposure scale mismatch, drive-weight
multiplier zeroing through, missing seeding step). This is distinct from the
action-class-collapse signature MECH-269 captures -- the agent's downstream
selection is still single-action-deterministic, but EVEN IF V_s monostrategy
were broken upstream, the goal pipeline at this no-training depth would not
seed a non-zero z_goal to bias action selection. This is a recurrence of the
wired-but-inert pattern named in the One-line framing section (and previously
seen on EXQ-471 / EXQ-483 / EXQ-490 / EXQ-514 / EXQ-536 / EXQ-538).

**Recommended next moves:**

1. **Trained-z_goal follow-up** (the natural successor to V3-EXQ-550). Same
   ARM_OFF / ARM_ON structure but with P0 + P1 training prior to the action-
   class entropy measurement, so the z_goal pipeline has had a chance to
   accumulate state and the goal-modulated policy has gradient pressure.
   PASS at training depth = z_goal pipeline biases action selection materially
   once trained -> weakens MECH-269 substrate-level reading. FAIL at training
   depth = substrate-level reading survives the strongest available probe
   short of architectural redesign. Deferred to a separate `/queue-experiment`
   session; not authored here.

2. **Diagnostic-first ordering** (concurrent sessions, parallel to this one):
   - **V3-EXQ-551 pipeline-entropy diagnostic** -- characterise what the
     `update_z_goal` -> GoalState -> z_goal-bias-into-action_selection chain
     actually does at no-training-depth: log z_goal norm trajectory, GoalState
     drive trajectory, per-step contribution to action logits, identify where
     in the chain the signal collapses to zero. Owned by a parallel session
     in `ree-v3/`.
   - **V3-EXQ-552 forced-exploration warmup** -- inject epsilon-greedy
     exploration during a warmup phase to escape the random-init action-class
     collapse, then re-measure z_goal ON/OFF entropy delta. Test whether the
     no-training monostrategy is the bottleneck for the z_goal diagnostic
     (orthogonal to whether trained z_goal helps). Owned by a parallel
     session in `ree-v3/`.

   These two diagnostics are queued by parallel sessions concurrent with
   this review (no resource overlap with REE_assembly/ planning docs); their
   outputs route back into this plan via separate decision-log entries.

**Status table impact:** This plan does NOT carry a GAP explicitly named
"z_goal wired-but-inert at no-training depth" -- the pattern was implicit in
GAP-2 / GAP-3 / GAP-4 prerequisites. EXQ-550's incidental finding tightens
the substrate description: any Phase 2/3/4 EXQ that does NOT actively warm
up the goal pipeline (e.g. through training or forced exploration) will
inherit the inert-z_goal signature regardless of substrate quality. Recorded
here rather than as a new GAP row because (a) the candidates EXQ-551 / EXQ-552
will narrow what the actual mechanism is, and (b) the fix path (trained
follow-up + diagnostic-driven mechanism identification) is already covered
by Phase 2 + Phase 3 + Phase 4 cohort triggers. If EXQ-551 / EXQ-552 surface
a distinct architectural gap (e.g. a missing GoalState seeding hook), a new
GAP row will be added in the resolving session.

**Substrate-readiness implications for in-flight work:**
- MECH-269 V_s monostrategy hold on SD-029 is sustained at no-training depth.
  Previous reclassifications of EXQ-433* / EXQ-470 / EXQ-476* / EXQ-537 as
  non_contributory under V_s monostrategy remain correct.
- Other plans' interpretations of "wired but inert" recur (most recently in
  the 2026-05-11 self_attribution_plan GAP-1 inversion: floating-point-
  identical metrics between ARM_INDEPENDENT and ARM_SHARED under
  action_class_entropy=0.0) read the SAME substrate-ceiling signal from a
  different observable.

**Files touched in this session:** `goal_pipeline_plan.md` (this decision-log
entry; status-table GAP-1 row "Next action" notes EXQ-550 finding); review
tracker; WORKSPACE_STATE.md. No claims.yaml edits; no MECH-269 status
change (already candidate / v3_pending under MECH-269b followup). No
`evidence_direction_per_claim` overrides needed -- the manifest's flat
`MECH-269: supports` correctly carries the substrate-level reading. No
script written; concurrent sessions B + C own the diagnostic queue-ups
(V3-EXQ-551 + V3-EXQ-552).

### 2026-05-11 - GAP-1 substrate landed (Option-b for Gap 1 per user override)

Phase 1 substrate (MECH-307 four-gap conjunction architecture) landed end-to-end
in ree-v3. Gap 1 implemented as Option-b (split into VALENCE_POSITIVE_SURPRISE +
VALENCE_NEGATIVE_SURPRISE as separate channels in the residue valence buffer)
per user override 2026-05-11 of the design-doc default Option-a (signed single
channel). Gaps 2, 3, 4 substrate-landed 2026-05-08 unchanged (no rewrite this
session). New REEConfig field `use_mech307_conjunction` is a master convenience
flag whose `__post_init__` resolver propagates to the three substrate-side
sub-flags (`use_mech307_split_surprise`, `use_mech307_schema_multichannel`,
`use_mech307_predicted_location_write`). Path B / consumer-side
`use_mech307_consumer_conjunction_read` NOT auto-set (out of session scope per
"substrate only first" directive).

Modules touched:
- ree-v3/ree_core/residue/field.py (VALENCE_DIM 4 -> 6; new constants
  VALENCE_POSITIVE_SURPRISE=4 and VALENCE_NEGATIVE_SURPRISE=5;
  evaluate_valence return shape [batch, 6]).
- ree-v3/ree_core/utils/config.py (two new REEConfig fields +
  `__post_init__` resolver).
- ree-v3/ree_core/agent.py (MECH-205 PE write site dispatches three paths:
  split / signed / true-legacy; new VALENCE_POSITIVE_SURPRISE /
  VALENCE_NEGATIVE_SURPRISE imports).
- ree-v3/CLAUDE.md ("MECH-307 Anticipatory Affect Conjunction Architecture
  (2026-05-11)" SD-Implemented entry appended).
- REE_assembly/docs/claims/claims.yaml (MECH-307 status candidate ->
  candidate_substrate_landed; evidence_quality_note extended with 2026-05-11
  implementation_note paragraph; v3_pending remains True pending behavioural
  validation).
- REE_assembly/docs/architecture/anticipatory_affect_conjunction_vs_dual_channel.md
  (Status block flipped PENDING -> SUBSTRATE LANDED 2026-05-11; Option-b
  paragraph added).

Regression: 309/309 contracts + 7/7 preflight PASS with master OFF
(bit-identical OFF guarantee). The existing
tests/contracts/test_mech307_conjunction_contract.py (12 contracts covering
Gaps 1-4 under their individual flags) PASSed unmodified -- the Option-a
Gap-1 path is preserved behind `use_mech307_signed_pe`.

Direct field-level smoke (2026-05-11):
- VALENCE_DIM=6 buffer allocation verified.
- Split-channel write routing verified: harm_signal < 0 -> NEGATIVE channel;
  harm_signal >= 0 -> POSITIVE channel; magnitude preserved on legacy
  VALENCE_SURPRISE for backward-compat consumers.
- MECH-094 hypothesis_tag=True gate respected (write skipped).

GAP-2 (SD-049 Phase 2 V3-EXQ-514 behavioural validation under MECH-307-fixed
substrate) now unblocked. Phase 2 trigger condition (Phase 1 PASS on the 4-arm
discriminative validation) is the next gate; the 4-arm validation EXQ is the
canonical Phase 1 PASS / fallback adjudicator between MECH-307 conjunction
architecture (first-line) and the SD-014 6-channel amendment (registered
fallback).

Reason for Option-b override: user-directed; rationale not recorded by the
user beyond preference for the architecturally cleaner channel-separation
form. The Option-a path is preserved behind `use_mech307_signed_pe`, so
the 4-arm validation can include an Option-a arm if discriminative testing
between Option-a and Option-b becomes load-bearing for governance.

### 2026-05-08 - Plan registered

Audit conducted in conversation with user as a follow-on to the
2026-05-08 governance-cycle-friday-pm and register-mech307-and-sd014-amendment
sessions. User flagged the goal pipeline as a load-bearing umbrella loop
parallel to sleep_substrate_plan.md, with MECH-307 conjunction architecture
already at substrate_queue priority=1. Six gaps surfaced and sequenced into
six phases. User acknowledged Phase 1 (MECH-307) as the gate for the rest;
GAP-5 / Phase 5 deferred as cleanup-of-substrate-coverage refactor not on
acceptance-criterion path. Plan-doc + status-table + decision-log pattern
adopted, mirroring sleep_substrate_plan.md / sd033_governance_plan.md
precedent.

### 2026-05-08 - Boundary with sleep_substrate_plan.md established

SD-049 sleep-on cohort (V3-EXQ-514 family with use_sleep_loop=True) sits at the
boundary of both plans. Decision: goal_pipeline_plan.md owns the SD-049
substrate + behavioural acceptance criteria; sleep_substrate_plan.md owns the
sleep-loop side of validation. Both plans' "See also" sections cross-reference
each other; either plan may sequence a V3-EXQ-514 successor with its flag stack.
Reason: avoid plan-doc drift where two plans claim ownership of the same EXQ
without explicit boundary.

### 2026-05-08 - MECH-307 vs SD-014 6-channel amendment

MECH-307 four-gap conjunction architecture is the first-line proposal (~40 lines
of code per the 2026-05-08 design doc); SD-014 6-channel amendment (add
VALENCE_EXCITEMENT + VALENCE_DREAD as discrete channels) is the architectural
fallback if MECH-307 conjunction does not produce the expected derived states.
Decision: land MECH-307 first; only escalate to SD-014 6-channel amendment on
Phase 1 falsification (all-four-gaps-fixed arm fails to produce non-zero
cue_fires + dacc_bias + approach_commit relative to baseline). Reason:
biology does not have a "VALENCE_EXCITEMENT neuron type"; the excitement
signal measured in NAcc fMRI is the anatomical convergence of DA RPE +
hippocampal preplay + ANS arousal at one structure -- the conjunction reading is
more biologically faithful than adding a new channel.

### 2026-05-08 - SD-012 sustained-drive amendment scoped as Phase 3, not Phase 1

The sustained-drive amendment (drive_level collapse at contact, per
sustained_drive_anticipatory_wanting.md) overlaps with MECH-307 Gap 4
(MECH-216 writes at current rather than predicted z_world). Both touch SD-012 /
MECH-216. Decision: keep them as separate phases (Phase 1 = affect-write site
fix; Phase 3 = drive-multiplier site fix). Reason: independently small and
independently falsifiable; sequencing serially keeps each PASS interpretable.
EXQ-536b force-arm probe documents both confounds simultaneously; separating
them lets the Phase 1 retest disambiguate.

### 2026-05-08 - Phase 5 deferred as refactor not on acceptance-criterion path

SD-049 Phase 3 SD-032 consumer cascade (GAP-5) is a cleanup-of-substrate-coverage
refactor: migrating AIC, PCC, pACC, dACC, salience-coordinator,
override-regulator, MECH-295 liking-bridge from reading collapsed scalar to
per_axis_drive vector. None of the goal-pipeline acceptance criteria require
Phase 5 to land; Phases 1-4 are sufficient. Decision: defer Phase 5 to "Phase
4 Tier-3 outcome" trigger -- only land if Phase 4 reveals a remaining
drive-cascade fidelity gap. Reason: smallest-step principle; Phase 5 has no
load-bearing dependent claim.

---

## Open questions

Numbered for reference from future sessions.

- **Q1**: For Phase 1 Gap 1, prefer signed VALENCE_SURPRISE (single channel,
  preserves backward compat under `abs()`) or split into VALENCE_POSITIVE_SURPRISE
  + VALENCE_NEGATIVE_SURPRISE (cleaner separation, more disruptive). Default
  proposed: signed single channel behind `surprise_signed` config flag. Open:
  whether any downstream consumer needs the channel-level separation rather
  than reading sign-magnitude.
- **Q2**: ~~For Phase 3 Option 1 (sustained-drive EMA), what is the right
  `drive_ema_alpha` default?~~ **RESOLVED 2026-05-17 (user decision).**
  Config *default* = **1.0** (non-negotiable: alpha=1.0 -> trace == drive_level
  every step regardless of init -> bit-identical OFF / backward-compat).
  Canonical knob name = **`drive_ema_alpha`** (the design memo's
  `alpha_drive_trace` is superseded; identical semantics). First-PASS /
  acceptance operating arm = **alpha=0.02** (~35-step half-life), chosen over
  the originally-proposed 0.05 (~14-step) because the lit synthesis
  `wanting_liking_sleep_consolidation_synthesis.md` endorses a 30-60 step
  post-consummatory wanting window and explicitly flags 0.05 as risking the
  documented "trace too fast -> resembles OFF" failure mode. Discriminative
  sweep = **{0.01, 0.02, 0.2, 1.0}** (0.02 first-PASS, 0.01 slow bracket, 0.2
  fast-end falsifier, 1.0 OFF parity). Trace is **zero-initialised**
  (user-chosen over first-obs init): for alpha<1.0 this carries a deliberate
  ~1/alpha-step per-episode cold-start transient -- an accepted, documented
  confound that V3-EXQ-582 accounts for by reporting metrics over a fixed
  post-warmup window. Landed: GoalConfig.drive_ema_alpha; GoalState.update
  EMA recursion; GoalState.reset() zeroes the trace (per-episode cold-start);
  REEConfig.from_dims passthrough; contract test_sustained_drive_ema_gap3.py
  (7/7). Validation: V3-EXQ-582 (queued).
- **Q3**: For Phase 4 Tier-1 cohort, should V3-EXQ-471a / V3-EXQ-475a / V3-EXQ-483c /
  V3-EXQ-490g / V3-EXQ-524a all run together as a Tier-1 batch, or sequentially?
  Default proposed: batch, since they share substrate (MECH-307 + SD-012
  amendment + StepHarness) and discriminate on different downstream pathways.
- **Q4**: For Phase 2 row-6 falsifier branch, MECH-229 routing to
  substrate_conditional with V4-1 multi-agent ecology dependency requires
  V4 substrate work. Open: should goal_pipeline_plan track the V4-1
  escalation path, or is that V4 spec territory? Default proposed: track here
  with a `tracked` row pointing at v4_spec.md, escalate ownership only on
  row-6 hit.
- **Q5**: For Phase 5 (deferred), the Phase 5 trigger is "Phase 4 Tier-3
  outcome reveals a remaining drive-cascade fidelity gap." Open: what is the
  precise diagnostic that would identify the cascade as the residual issue
  rather than (e.g.) E3 / BG selection thresholds? Default proposed: per-axis
  drive ANOVA on z_goal cluster IDs producing p > 0.05 in Phase 4 Tier-3
  ARM_2 (the SD-049 acceptance criterion fails specifically on the per-axis
  drive read-site path).

---

## Resume ritual

When picking up goal-pipeline work after a deviation:

1. Read this plan document first.
2. Read the [Status table](#status-table) and identify the row that was
   `paused`, `in-progress`, or `blocked` whose blocker has cleared.
3. If `paused`, find its entry in the [Decision log](#decision-log) and
   confirm the resume condition has fired.
4. If `blocked` and the blocking phase has PASSed, transition to `in-progress`
   and continue from the most recent decision-log entry for that phase.
5. If `in-progress`, find the most recent decision-log entry for that phase
   and continue from the last concrete action.
6. Update the row's `Last updated` field and `Status` if it changes.
7. Append a new decision-log entry for any architectural choice made during
   the resumed session.

Sessions that do NOT touch goal-pipeline work do not need to read this
document. Sessions that DO touch goal-pipeline work read this document before
any code or experiment edit.

The plan-doc is the agent's working memory across sessions. TodoWrite entries
die with the session; WORKSPACE_STATE.md is recent-work, not strategic;
substrate_queue.json is granular but does not capture phase ordering or
decision rationale. This document is the single source of truth for
goal-pipeline strategy.

---

## See also

- [docs/architecture/anticipatory_affect_conjunction_vs_dual_channel.md](../../docs/architecture/anticipatory_affect_conjunction_vs_dual_channel.md)
- [docs/architecture/sustained_drive_anticipatory_wanting.md](../../docs/architecture/sustained_drive_anticipatory_wanting.md)
- [docs/architecture/goal_wanting_signal_chain.md](../../docs/architecture/goal_wanting_signal_chain.md)
- [docs/architecture/mech_295_drive_liking_approach_bridge.md](../../docs/architecture/mech_295_drive_liking_approach_bridge.md)
- [docs/architecture/sd_049_multi_resource_heterogeneity.md](../../docs/architecture/sd_049_multi_resource_heterogeneity.md)
- [docs/architecture/sd_015_z_resource_encoder.md](../../docs/architecture/sd_015_z_resource_encoder.md)
- [docs/architecture/approach_avoidance_symmetry.md](../../docs/architecture/approach_avoidance_symmetry.md) (ARC-030, MECH-117, MECH-229, MECH-230 location)
- [evidence/planning/sleep_substrate_plan.md](./sleep_substrate_plan.md) -- adjacent plan; SD-049 sleep-on cohort sits at the boundary (see [Boundary with sleep_substrate_plan.md](#boundary-with-sleep_substrate_planmd))
- [evidence/planning/sd033_governance_plan.md](./sd033_governance_plan.md) plan-doc precedent
- [evidence/planning/substrate_queue.json](./substrate_queue.json) -- MECH-307 / MECH-295 / SD-049-* / MECH-269b-followup-A entries
