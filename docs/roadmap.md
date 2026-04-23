---
title: Roadmap
nav_order: 6
---

# Roadmap

**Claim Type:** implementation_note
**Scope:** Program phases, repository roles, and phase-gate criteria
**Depends On:** IMPL-020, IMPL-021, IMPL-022, MECH-057, MECH-058, MECH-059, MECH-060
**Status:** candidate
**Claim ID:** IMPL-008
<a id="impl-008"></a>

---

## Status Snapshot (2026-04-23 PM — lit-pull + docs sync)

- **Literature pull completed: MECH-074a/c/d (PM session 2026-04-23T11:24Z–11:34Z).**
  Six new entries added to `evidence/literature/targeted_review_connectome_mech_074/`:
  - **MECH-074a** (3 entries): Paré 2003 (connectome_mechanistic_review, conf=0.80);
    Roozendaal et al. 1999 PNAS (behavioral_animal, conf=0.82 — direct beta-adrenergic
    gate evidence); Bass & Manns 2015 (electrophysiology_lfp, conf=0.72 — BLA
    stimulation → CA3-CA1 gamma synchrony → STDP circuit mechanism).
  - **MECH-074c** (2 entries): Ciocchi et al. 2010 Nature (electrophysiology_single_unit,
    conf=0.78 — CeL required for fear acquisition, CeM drives output, GABAergic
    disinhibition); Walker & Davis 2008 (connectome_mechanistic_review, conf=0.75 —
    CeA(M) rapid phasic output vs BNST sustained fear, directly grounds the
    fast_prime vs MECH-046 distinction).
  - **MECH-074d** (1 entry): Redondo et al. 2014 Nature (behavioral_animal, conf=0.62,
    mixed — DG engram can switch valence, BLA engram cannot; supports BLA attribution
    stability but does not directly test PE-triggered partial remap amplitude).
  `claim_evidence.v1.json` updated: MECH-074a lit_conf=0.840, MECH-074c lit_conf=0.782,
  MECH-074d lit_conf=0.560. Index rebuilt: 923 literature entries across 443 experiment
  types.
- **Experiment count:** 844 runs (indexer rebuilt 2026-04-23 PM; prior session spec
  showed stale count of 525 — now corrected in spec and README).
- **Pending review:** 0 indexed pending; 10 runner-only UNKNOWN (V3-EXQ-456, 460,
  462–468, 471, 447 — all from V_s invalidation runtime / SD-032 cluster landings;
  will clear after next indexer rebuild with those results indexed).
- **No new SDs or governance decisions this session** (docs-only sync pass following
  the PM lit-pull).

---

## Status Snapshot (2026-04-23)

- **V_s invalidation runtime substrate wave LANDED 2026-04-22.** Six substrates
  landed in a coordinated 2026-04-22 session implementing the architecture doc
  `REE_assembly/docs/architecture/v_s_invalidation_runtime.md`:
  - **SD-036 GABAergic cross-stream decay regulator**
    (`ree_core/regulators/gabaergic_decay.py`) -- broadly-projecting tonic decay
    applied out-of-place across registered latent streams (z_harm tau=0.05,
    z_harm_a tau=0.02, z_beta tau=0.03 by default; drive accumulator intentionally
    excluded). Global `gaba_tone` multiplier in [0, 2] models benzo-analog (>1)
    and withdrawal / chronic-stress analog (<1). Wired in `agent.sense()` right
    after `LatentStack.encode()` so all downstream consumers see the decayed
    latent on the same tick.
  - **MECH-279 PAG freeze-gate** (`ree_core/pag/freeze_gate.py`) -- committed-
    freeze substrate keyed on `duration_above_threshold * z_harm_a > theta_freeze`
    (default 2.0). Exit threshold scales with SD-036 `gaba_tone`, so the same
    GABAergic system gates BOTH freeze entry AND freeze exit (architectural
    prediction: GABA agonists treat freeze catatonia). Action-class no-op
    injection during freeze; simulation_mode gated.
  - **MECH-269 base / Phase 1 per-stream V_s**
    (`ree_core/hippocampal/module.py::update_per_stream_vs`) -- foundation
    observable: identity-prediction proxy EMA over registered streams
    (`z_world / z_self / z_harm_s / z_harm_a / z_goal / z_beta`); seeds at 1.0
    on first tick, drops on latent change. Forward-predictor routing (SD-007
    reafference for z_world, SD-011 harm forward for z_harm_s) reserved for
    Phase 2 consumer wiring.
  - **MECH-288 event segmenter Phase 2**
    (`ree_core/hippocampal/event_segmenter.py`) -- two-scale boundary detector:
    fast `pe_threshold` on `(z_world, z_self)` (window=200, threshold=0.65) +
    slow BOCPD-Gaussian on `(z_goal,)` (hazard=1/40, posterior_threshold=0.5,
    top-k=20). Emits BoundaryEvents with nested outer.inner segment IDs; slow
    fire forces outer+=1, inner=0 and suppresses same-tick fast; `force_boundary`
    API for scripted injection. BOCPD uses underflow-robust Adams & MacKay 2007
    recursion with Welford online variance.
  - **MECH-287 invalidation trigger Phase 2 iv**
    (`ree_core/regulators/invalidation_trigger.py`) -- BoundaryEvent subscriber
    re-emitting graded BroadcastEvents (`strength = posterior * gain`; NO
    binary thresholding of strength). Phasic/tonic guardrail (Aston-Jones &
    Cohen 2005; Clewett 2025 failure signature 2) via rolling mean over
    `tonic_window=50` past-tick posteriors; suppresses phasic broadcast when
    tonic estimate exceeds `tonic_threshold=0.5`. Verdict-3 architectural
    commitment (V_s foundation lit-pull synthesis): the trigger IS the
    subscriber, not an independent CA1/CA3 mismatch comparator stage -- the
    biological two-stage loop is collapsed to a subscription on the MECH-288
    boundary queue. Dissociation contract C5 verifies: lesioning the segmenter
    silences the trigger regardless of its internal tonic state.
  - **MECH-269 Phase 2 ii AnchorSet** (`ree_core/hippocampal/anchor_set.py`) --
    scale-tagged anchor store keyed on `(scale, segment_id, stream_mixture)`.
    Dual-trace preservation per Bouton 2004: remap on the same
    `(scale, stream_mixture)` marks the outgoing anchor INACTIVE and retains
    it in `all_anchors()`; never erased. k=5 consecutive-below-threshold
    hysteresis on `V_s_anchor = avg(V_s over mixture) - staleness`
    (staleness monotonic in tick - last_accessed). FIFO soft-cap at 128
    active anchors per scale. BoundaryEvent consumer via
    `tick_anchor_set(latent_state, events)`; Phase 2 stream_mixture stand-in is
    `tuple(sorted(per_stream_vs.keys()))` at anchor-creation tick (learned
    attribution-head version reserved for Phase 3 MECH-284).
  - **MECH-269 Phase 2 iii T4 per-region V_s** (extended module.py) -- promotes
    flat `per_stream_vs[stream] -> float` to
    `per_region_vs[(scale, segment_id)][stream] -> float` keyed on active
    AnchorSet regions. Two reset paths: (1) passive hysteresis via
    `tick_anchor_set` marking anchors inactive; (2) explicit via
    `apply_invalidation_broadcasts_to_regions(broadcasts)` dropping region V_s
    and mark_inactive'ing the matching anchor on MECH-287 BroadcastEvents
    (keyed on `source_scale`, `source_segment_id_old`). Peek-not-drain on the
    broadcast queue preserves events for Phase 3 MECH-284 staleness accumulator
    consumer. Idempotent on repeated broadcasts.
  All six landed via 85/85 contracts + 7/7 preflight PASS with flags OFF
  (bit-identical to legacy), plus dedicated contract tests for each phase:
  MECH-269 Phase 1 (5 tests), MECH-288 (7 tests), MECH-287 (5 tests incl.
  verdict-3 dissociation C5), MECH-269 Phase 2 ii (9 tests incl. 2 integration
  smokes for agent-level flag behaviour), MECH-269 Phase 2 iii T4 (6 tests
  incl. 1 integration smoke). Activation smokes confirmed expected signatures:
  CeA synthetic threat -> graded mode_prior/fast_prime; BLA synthetic arousal
  -> inverted-U cap; BLA synthetic PE-spike -> Moita 2004 remap; default agent
  + Phase 1 flag ON seeds `per_stream_vs` at 1.0 and drops on perturbation;
  forced fast boundary installs anchor under segment_id "0.1" and populates
  per-region V_s under the new region key. Design doc:
  `docs/architecture/v_s_invalidation_runtime.md`; anchor-selection doc:
  `docs/architecture/hippocampal_anchor_selection.md`. End-to-end combined-
  cluster validation (V3-EXQ-476: matched re-run of EXQ-475 with the full
  circuit on) is planned; not yet queued as of 2026-04-23.
- **Experiments:** 525 total completions unchanged since 2026-04-22 snapshot
  (runner_status.json last_updated 2026-04-22T01:11Z) -- the V_s invalidation
  runtime wave landed via contract tests + activation smokes only. PASS/FAIL
  breakdown: 108 PASS / 234 FAIL / 62 ERROR / 121 UNKNOWN. Next indexer
  rebuild will refresh after V3-EXQ-476 and the pending SD-032 / SD-003
  successor results land.
- **Pending review:** 10 items as of 2026-04-22T23:12:38Z (down from 46 at the
  2026-04-21T19:54Z snapshot). All 10 are runner-UNKNOWN because the index is
  stale ahead of the next indexer rebuild (`python evidence/experiments/
  scripts/build_experiment_indexes.py` from `REE_assembly/` root clears them).
  Queue IDs: V3-EXQ-456 / 460 / 462 / 463 / 464 / 465 / 466 / 467 / 468 / 471.
- **Current first-paper-gate bottleneck:** SD-032 cluster behavioural follow-
  through remains the primary gate. V3-EXQ-445a (SD-032b dACC full-pipeline
  fix for the EXQ-445 monostrategy collapse + terrain-prior inversion,
  claimed EWIN-PC) is the decisive test still in flight; V3-EXQ-445b / 445c
  have both FAILed and V3-EXQ-325d FAILed on the SD-032c descending-
  modulation falsification signature. V3-EXQ-447 (SD-032d deterministic
  validation, claimed ree-cloud-2) and V3-EXQ-451 (Q-034 hazard/resource
  threshold retest, claimed EWIN-PC) are the remaining two claimed
  experiments. SD-003 successor track (V3-EXQ-433a MECH-256/SD-029 FAIL,
  V3-EXQ-452 MECH-257 dual-function E2 diagnostic FAIL) and ARC-007 path-
  memory track (V3-EXQ-397c) remain alive. Secondary bottleneck: V_s
  invalidation runtime end-to-end validation deferred -- V3-EXQ-476
  (combined-cluster re-run of EXQ-475 with the full circuit on) is planned
  but not yet queued.

---

## Status Snapshot (2026-04-22)

- **SD-035 amygdala analogue LANDED 2026-04-21.** BLA + CeA peer modules
  (`ree_core/amygdala/bla.py`, `ree_core/amygdala/cea.py`) non-trainable
  arithmetic. BLA instantiates MECH-074a inverted-U encoding_gain (Roozendaal
  2011), MECH-074b content-selective retrieval_bias (LaBar & Cabeza 2006
  per-trace weight vector, not scalar), and MECH-074d attribution-gated
  PE-spike remap (Moita 2004). CeA instantiates MECH-046 pre-softmax
  mode-prior (LeDoux 1996 "low road" / Pessoa & Adolphs 2010, distinct from
  SD-032c AIC which biases mode-SWITCH threshold rather than mode
  SELECTION) and MECH-074c fast_prime (Mendez-Bertolo 2016 ~75 ms subcortical
  pulse with cortical confirmation window). CeA mode_prior + fast_prime are
  injected into SalienceCoordinator via update_signal each select_action
  tick. BLA retrieval_bias / remap_signal hippocampal consumer wiring is
  deferred until V3-EXQ-474 confirms behavioural signature. Validation:
  V3-EXQ-473 CeA mode-prior PASS (5 acceptance criteria), V3-EXQ-474 BLA
  encoding+remap PASS (5 acceptance criteria), both substrate-readiness
  diagnostics per EXQ-445 lesson. 33/33 preflight+contract tests PASS with
  use_amygdala_analog=False (backward compat preserved). Governance:
  MECH-046 / MECH-074 / MECH-074a/c/d / SD-035 show hold_pending_v3_substrate
  pending completion. Design doc: `docs/architecture/sd_035_amygdala_analog.md`;
  literature synthesis: `evidence/literature/targeted_review_amygdala_analog/
  synthesis.md`.
- **MECH-266 asymmetric per-mode hysteresis LANDED 2026-04-21.** Schmitt-trigger
  per-mode enter_thresholds / exit_thresholds dicts layered atop the MECH-259
  symmetric switch_threshold in
  `ree_core/cingulate/salience_coordinator.py`. Empty-dict default preserves
  legacy behaviour; over-binding/OCD axis reproducible at exit_threshold near 0
  (stuck-in-mode), under-binding/depression axis reproducible with lower
  enter_threshold. Setters: `set_enter_threshold`, `set_exit_threshold`,
  `set_hysteresis_ratio` (uniform exit-rail convenience). Validation:
  V3-EXQ-464 competing-goals 5-arm + V3-EXQ-467 mode-stickiness 5-arm
  parametric sweep both smoke-PASS all sub-tests. Full behavioural
  competing-goals runs deferred pending CausalGridWorldV2 dual simultaneously
  active resource-cue extension.
- **SD-029 curriculum-level balanced hazard-event support LANDED 2026-04-21.**
  `scheduled_external_hazard_enabled` + `scheduled_external_hazard_interval` +
  `scheduled_external_hazard_prob` + `scheduled_external_hazard_adjacent_only`
  flags in CausalGridWorldV2 schedule hazard injection (relocate or spawn) at
  cells adjacent to the agent (or any empty cell when adjacent_only=False).
  Preserves the self- vs externally-caused taxonomy: the agent did not
  initiate the encounter. `info["external_hazard_injected"]` /
  `info["external_hazard_event_count"]` tags always present. Unblocks C3/C4
  event-conditioned SNR measurement for the MECH-256/SD-029 comparator track
  which had been failing on per-seed event-count imbalance. Validation:
  V3-EXQ-470 SCHEDULED vs BASELINE ablation queued.
- **SD-033e frontopolar-analog V4-reserved stub LANDED 2026-04-21.**
  `ree_core/pfc/frontopolar_analog.py` (FrontopolarAnalog +
  FrontopolarConfig) mirrors the SD-033a contract: no-op behind
  `use_frontopolar_analog=False`; raises NotImplementedError when enabled
  (until design doc lands). Last nn.Linear of both heads (MECH-264
  counterfactual-value, MECH-265 relative-importance) zero-initialised.
  `tests/contracts/test_sd_033e_stub.py` 7-contract test added (importable,
  default backward-compat, enabled-raises-NotImplementedError, zero-init,
  reset safety, get_state stub marker). Three V4-reserved experiment
  proposals appended to manual_proposals.v1.json (EXP-0165 / 0166 / 0167).
  Path-clear for the design-doc + dual-active-goal env extension that
  unlocks behavioural testing.
- **Hippocampal anchor-vs-probe cluster REGISTERED 2026-04-21.** MECH-269
  (regional-verisimilitude anchor selection in hippocampal proposer -- per-
  stream V_s gates anchor eligibility; probe channel inverts the gate for
  curiosity-driven seeding; anchored rollouts update ARC-018 viability map,
  probes do not until realized-experience validation); MECH-270 (ephaptic
  field coherence as candidate biological substrate for V_s readout);
  MECH-271 (MECH-094 hypothesis_tag as routing signature: anchored replay
  routes to E1 consolidation / SD-033a PFC, probe replay routes to BLA /
  NAc -- tag is a routing flag, not a source-side marker). MECH-269 lit-pull
  confidence jumped 0.783 -> 0.852 on 2026-04-21 after Pfeiffer & Foster 2013
  (direct evidence: hippocampal sequences start at current location, progress
  to goal, compositional) was added. Design doc:
  `docs/architecture/hippocampal_anchor_selection.md`. MECH-270 future
  directions: standalone-paper candidate.
- **Sleep/waking state-gated routing REGISTERED 2026-04-21.** MECH-272
  (state-gated anchor/probe routing: waking=anchor-dominant decision-support;
  sleep=probe-dominant Bayesian schema restructuring); MECH-273 (sleep-
  dependent aggregation of SD-003 single-episode self-attribution into stable
  self-model); MECH-274 (V4-reserved: other-attribution sleep-dependent
  aggregation via ARC-010 empathy / mirror-modelling;
  implementation_phase: v4). Design doc `hippocampal_anchor_selection.md`
  extended with sleep/waking section and V4 other-attribution reservation.
- **Scientist-agent developmental-ordering cluster REGISTERED 2026-04-21.**
  ARC-059 (three-stage developmental ordering self -> objects -> others
  refining ARC-019), MECH-275 (sleep-phase general Bayesian aggregation
  mechanism -- MECH-273/274 become specialisations of MECH-275), MECH-276
  (scientist-agent principle: waking-phase counterfactual-backed attribution
  via deliberate intervention), MECH-277 (action-space discovery via motor
  experimentation, stage-1 specialisation), MECH-278 (object-schema formation
  via experimental action, stage-2 specialisation). Design doc:
  `docs/architecture/scientist_agent_developmental_ordering.md`.
  MECH-273/274 depends_on updated with MECH-275.
- **Experiment counts: 525 total completions** (runner_status.json last_updated
  2026-04-22T01:11Z): 108 PASS / 234 FAIL / 62 ERROR / 121 UNKNOWN, up from
  495 / 105 PASS / 227 FAIL at the 2026-04-20 snapshot. New PASSes since the
  2026-04-21 snapshot: V3-EXQ-473 SD-035 CeA mode-prior, V3-EXQ-474 SD-035
  BLA encoding+remap, V3-EXQ-455 SD-032a coordinator behavioural, plus
  V3-EXQ-456 SD-033a landing (PASS), V3-EXQ-460/466 SD-034 landings,
  V3-EXQ-462/465 MECH-267, V3-EXQ-463/468 MECH-268, V3-EXQ-464/467 MECH-266.
  New FAILs since the 2026-04-21 snapshot include V3-EXQ-397c (ARC-007 harder
  env, 2 attempts), V3-EXQ-445b/c (SD-032b variants), V3-EXQ-133 (MECH-091),
  V3-EXQ-126 (MECH-104), V3-EXQ-325d (SD-032c AIC), V3-EXQ-452/453/454
  (MECH-257 / MECH-261 landing / ARC-016 adaptive), V3-EXQ-433a (MECH-256/
  SD-029 comparator scripted-eval). Fresh indexer rebuild pending.
- **Pending review count: 46** (as of pending_review.md generation
  2026-04-21T19:54:57Z): 8 PASS / 19 FAIL / 19 ERROR-UNKNOWN-smoke. Governance
  cycle pending to absorb the SD-032 cluster behavioural FAILs, the SD-035
  amygdala landings, the MECH-266 hysteresis extension, and the
  MECH-269/270/271 + MECH-272/273/274 + MECH-275/276/277/278 + ARC-059
  registrations.
- **Queue drained to 3 items -- all claimed.** V3-EXQ-447 (SD-032d
  deterministic validation, ree-cloud-2, claimed 2026-04-19), V3-EXQ-451
  (Q-034 hazard/resource threshold retest, EWIN-PC, claimed 2026-04-20),
  V3-EXQ-445a (SD-032b dACC full-pipeline fix, EWIN-PC, claimed 2026-04-20).
  All other queued entries from the 2026-04-21 snapshot have since landed
  as PASS/FAIL entries in runner_status.json.
- **Current bottleneck.** SD-032 cluster behavioural follow-through remains
  the primary first-paper-gate blocker: V3-EXQ-445a is the decisive test
  after the 445b / 445c monostrategy + terrain-inversion variants FAILed.
  SD-003 successor track (V3-EXQ-433a MECH-256/SD-029 FAIL, V3-EXQ-452
  MECH-257 dual-function diagnostic FAIL) is alive. ARC-007 path-memory
  track remains open (V3-EXQ-397c claimed on DLAPTOP-4.local). SD-035
  first-pass hippocampal consumer wiring for BLA retrieval_bias / remap
  deferred until V3-EXQ-474 behavioural signature confirmed; that work and
  the MECH-266 full behavioural competing-goals arm both depend on the
  CausalGridWorldV2 dual simultaneously active resource-cue extension.

## Immediate Work Queue (This Cycle)

- Land the 3 claimed experiments: V3-EXQ-447 (SD-032d deterministic
  validation, ree-cloud-2), V3-EXQ-451 (Q-034 hazard/resource threshold
  retest, EWIN-PC), V3-EXQ-445a (SD-032b dACC full-pipeline fix, EWIN-PC).
- Queue V3-EXQ-476 (combined V_s invalidation runtime end-to-end validation:
  matched re-run of EXQ-475 with `use_gabaergic_decay=True`,
  `use_pag_freeze_gate=True`, `use_per_stream_vs=True`,
  `use_event_segmenter=True`, `use_invalidation_trigger=True`,
  `use_anchor_sets=True`, `use_per_region_vs=True`). This is the one
  missing piece for the 2026-04-22 substrate wave -- contracts have
  landed but the circuit has not been exercised behaviourally. Test
  MECH-288's falsifiable secondary prediction that z_goal / z_world
  broadcast events preferentially reset their home-region V_s entries
  rather than peer regions.
- Run the next governance cycle once V3-EXQ-445a and V3-EXQ-476 land:
  rebuild `claim_evidence.v1.json`, regenerate `pending_review.md`,
  ingest the SD-032 cluster behavioural FAIL pattern, the SD-035
  landing PASSes, the fresh SD-033 cluster registrations (MECH-266 /
  SD-029 / MECH-269-278 / ARC-059), and the V_s invalidation runtime
  landings (SD-036 / MECH-279 / MECH-269 Phase 1/2 ii/2 iii T4 /
  MECH-288 / MECH-287).
- Assess whether V3-EXQ-445a's outcome vindicates the SD-032b monostrategy
  fix or confirms that the dACC/AIC/ARC-016 behavioural loop needs
  substrate-level redesign; decide whether to queue EXQ-445d or to pivot
  to an SD-035 + MECH-266 behavioural-pair experiment.
- Queue V3-EXQ-470 (SD-029 SCHEDULED vs BASELINE curriculum diagnostic) to
  unblock C3/C4 event-conditioned SNR measurement on the MECH-256
  comparator track.
- First-pass hippocampal consumer wiring for SD-035 BLA retrieval_bias and
  remap_signal once V3-EXQ-474 behavioural signature confirmed (deferred
  from 2026-04-21 landing pass).
- First-pass Phase 3 wiring for the V_s invalidation runtime: MECH-284
  staleness accumulator consumer on per-region V_s (ticks monotonic in
  (tick - last_accessed) until broadcast or hysteresis reset); MECH-272
  state-gated anchor/probe routing (waking=anchor-dominant,
  sleep=probe-dominant). Both remain v3_pending after the 2026-04-22
  substrate landings -- Phase 2 produces the observables; Phase 3 wires
  them into replay / BG / E3 consumers.
- Move MECH-266 OCD/depression-axis competing-goals behavioural variants
  (EXQ-464b / EXQ-467b) off hold once the CausalGridWorldV2 dual
  simultaneously active resource-cue env extension lands.
- SD-033e design doc + dual-active-goal env extension to unlock the three
  V4-reserved proposals (EXP-0165 / 0166 / 0167).

---

## Status Snapshot (2026-04-21)

- **SD-033a lateral-PFC-analog / MECH-261 primary consumer LANDED 2026-04-20.**
  `ree_core/pfc/lateral_pfc_analog.py` (LateralPFCAnalog, LateralPFCConfig).
  Instantiates MECH-262 rule-selective persistence: gate-modulated EMA
  rule_state ([1, rule_dim]) with eff_eta = update_eta * write_gate("sd_033a"),
  source = delta_proj(z_delta) + world_pool_weight * world_proj(z_world).
  Frozen-random bias head with last nn.Linear zeroed at init -> initial
  bias exactly zero (bit-identical with head untrained; training-dependent
  emergence deferred). Per-mode gate weights from the MECH-261 spec table:
  external_task=1.0, internal_planning=1.0, internal_replay=0.05,
  offline_consolidation=0.3. V3-EXQ-456 landing diagnostic PASS (five
  sub-tests: instantiation, gate-modulated update rate, bias reaches E3
  with zero-init contract, backward compat, reset clears rule_state).
  Design doc: `docs/architecture/sd_033a_lateral_pfc_analog.md`.
- **SD-034 governance closure operator + MECH-268 dACC conflict-saturation +
  MECH-267 mode-conditioned hippocampal proposals LANDED 2026-04-20..2026-04-21.**
  SD-034 closure operator (`ree_core/governance/closure_operator.py`)
  coordinates a five-part "done" token at rule-completion events:
  (a) MECH-090 beta release, (b) MECH-260 No-Go FIFO injection on the
  just-completed action class, (c) ResidueField.discharge_domain(z_world,
  factor, radius) rule-domain multiplicative RBF decay with 1e-6 sign-aware
  floor (invariant: residue cannot be erased), (d) SalienceCoordinator
  closure_event signal re-biasing affinity toward internal_planning,
  (e) dACC PE reset / optional pe_cap install (MECH-268). Completion
  detector: rule_state delta < threshold for N consecutive ticks AND
  beta elevated AND current_mode in allowed_closure_modes AND
  write_gate("sd_033a") >= min. Mode conditioning is the falsifiability
  predicate vs pure MECH-090 + MECH-260 + MECH-094 tuning. MECH-267
  (`ree_core/hippocampal/module.py`) threads operating_mode through
  HippocampalModule.propose_trajectories with per-mode CEM-noise multipliers.
  MECH-268 (`ree_core/cingulate/dacc.py`) adds an outcome-history FIFO +
  f_sat attenuation on the dACC bundle; closure_event resets the buffer.
  Landing smokes all PASS: V3-EXQ-460 SD-034 closure wiring (6 sub-tests),
  V3-EXQ-466 ResidueField.discharge_domain (5 sub-tests: near attenuation,
  far spared, invariant preserved, end-to-end, distant-z spares), V3-EXQ-462
  MECH-267 rule binding, V3-EXQ-465 MECH-267 intrusive-simulation filtering,
  V3-EXQ-463 + V3-EXQ-468 MECH-268 saturation-and-reset. Behavioural
  variants with full E3 task loop + tolerance-band completion env deferred
  (depend on phased rule_state training + env variant not yet on the
  roadmap). Anchor: `evidence/planning/sd033_governance_plan.md`;
  source: `docs/thoughts/2026-04-20_ocd4.md` + GAP MEMO "REE-V3 is not
  missing cognition, it is missing governance."
- **SD-032 cluster behavioural follow-through: FAIL across four first-pass
  behavioural gates.** V3-EXQ-445 FAIL (SD-032b 3-arm ablation hit the
  monostrategy + terrain-inversion fishtank_viz signature under all three
  configs; dACC score_bias entropy delta under the C2 gate); V3-EXQ-325d
  FAIL (SD-032c AIC descending modulation, does_not_support); V3-EXQ-454
  FAIL (ARC-016 adaptive commitment threshold, weakens). V3-EXQ-455 PASS
  (SD-032a salience-network coordinator behavioural: supports SD-032a /
  MECH-259 / MECH-261 on the synthetic high-PE injection path). V3-EXQ-452
  FAIL (MECH-257 dual-function E2 diagnostic), V3-EXQ-453 FAIL (MECH-261
  write-gate landing diagnostic -- SD-032e-relevant). Net reading:
  the salience-coordinator substrate and its write-gate registry are
  structurally sound in isolation, but the end-to-end dACC / AIC / ARC-016
  behavioural loop does not yet clear even the first behavioural gates on
  CausalGridWorldV2. EXQ-445 has three successors queued (a/b/c) targeting
  monostrategy + terrain inversion via MECH-260 suppression, ARC-058
  shared-trunk, and foraging-value wiring respectively. EXQ-325b re-scoped
  as EXQ-325d produced does_not_support; AIC->descending pathway remains
  open under drive-regime contrast.
- **SD-016 forward-path diagnostic: V3-EXQ-449 FAIL confirmed
  cue_action_proj receives exactly 0.0 gradient under the original
  "implicit via E3 trajectory selection" claim** (C1 PASS, 2 seeds, ~1.7k
  steps; CEM argmax non-differentiable + detach at agent.py:694). C2 arm
  added supervised MSE loss against E2.action_object(z_world, a_executed)
  .detach() -- weights trained (grad ~0.013, delta ~0.21) but
  action_bias_divergence stayed at 0.0, indicating a downstream blocker
  between cue_action_proj and E3.select. V3-EXQ-449a queued to instrument
  the full forward path and identify the specific blocker before any
  EXQ-418b successor is written. cue_action_proj is now treated as
  CURRENTLY UNGROUNDED: sd016_enabled=True experiments should expect
  action_bias_divergence ~= 0.0 on the action path; cue_terrain_proj
  remains valid (trained via terrain_loss).
- **Recent landing MECH-267 + MECH-268 substrate smokes all PASS.**
  V3-EXQ-462 (MECH-267 rule binding) supports [MECH-267, SD-033a,
  MECH-262]. V3-EXQ-465 (MECH-267 intrusive-simulation filtering)
  supports [MECH-267, MECH-094, MECH-261]. V3-EXQ-463 + V3-EXQ-468
  (MECH-268 conflict-saturation) supports outcome-history FIFO + f_sat
  attenuation + closure-event buffer reset. V3-EXQ-456 (SD-033a landing)
  supports [SD-033a, MECH-261, MECH-262].
- **~715 V3 runs indexed** (indexer rebuild 2026-04-20T19:49Z wrote
  `claim_evidence.v1.json` with 630 V3 run-dirs + 77 flat V3 manifests =
  707 post-epoch; ~9 further V3 manifests written since rebuild covering
  SD-033a / SD-034 / MECH-267 / MECH-268 landings and the SD-032 cluster
  behavioural follow-through). Fresh claim_evidence.v1.json rebuild
  pending after this cycle's wave of results. Queue at snapshot time:
  14 active items, 4 claimed -- V3-EXQ-447 (SD-032d ree-cloud-2),
  V3-EXQ-451 (Q-034 retest EWIN-PC), V3-EXQ-445a (SD-032b full-pipeline
  fix EWIN-PC), V3-EXQ-397c (ARC-007 harder-env DLAPTOP-4). Pending
  queue: V3-EXQ-445b/c (SD-032b variants), V3-EXQ-456 (SD-033a landing,
  now PASS), V3-EXQ-449a (SD-016 forward-path probe), V3-EXQ-133 /
  V3-EXQ-126 (MECH-091 / MECH-104 discriminative pairs), V3-EXQ-460 /
  463 / 466 / 468 (SD-034 + MECH-268 landing smokes, all PASS).
  runner_status.json last_updated stale at 2026-04-20T14:39:30Z
  (495 completions: 105 PASS / 227 FAIL / 62 ERROR / 101 UNKNOWN);
  the live machine-side completion log is ahead of that snapshot.
- **Pending review count: 6** (as of pending_review.md generation at
  2026-04-20T05:50:27Z; stale -- regeneration pending after this cycle).
  Items: FAIL EXQ-397 (ARC-007/SD-004 path memory), FAIL EXQ-433a
  (MECH-256/SD-029 scripted-eval comparator), FAIL EXQ-445 (SD-032b
  behavioural); PASS EXQ-446 (SD-032a coordinator landing); ERROR
  V3-EXQ-445 + V3-EXQ-325c to clear.
- **Governance cycle 2026-04-19T21 (post-SD-032 landing) carry-forward.**
  Promoted MECH-094 to provisional; applied 12 `hold_pending_v3_substrate`
  decisions for the SD-032 cluster and dependents; reclassified EXQ-395 /
  EXQ-418a / EXQ-430 as non_contributory substrate-gap symptoms. No new
  governance cycle run today -- the SD-032 behavioural FAILs and the
  SD-033a/SD-034/MECH-267/MECH-268 landings are the input set for the
  next cycle.
- **Current bottleneck: SD-032 cluster behavioural escape from
  monostrategy + terrain-inversion, SD-033 governance cluster behavioural
  validation, SD-016 forward-path blocker identification, SD-003
  successor track.** Regression suite PRs 1-5 landed (preflight +
  contracts + deferred changed; `/api/regression/preflight` serve.py
  endpoint; explorer preflight badge; pre-commit contracts hook).

## Immediate Work Queue (This Cycle)

- Land results for the four claimed experiments: V3-EXQ-447 (SD-032d
  deterministic validation, ree-cloud-2), V3-EXQ-451 (Q-034 retest,
  EWIN-PC), V3-EXQ-445a (SD-032b full-pipeline fix, EWIN-PC),
  V3-EXQ-397c (ARC-007 path memory harder-env, DLAPTOP-4).
- Review pending_review.md after its next regeneration -- expected to
  cover EXQ-397 / EXQ-433a / EXQ-445 FAILs plus EXQ-446 PASS and the
  two ERROR clears (V3-EXQ-445, V3-EXQ-325c).
- Queue and land V3-EXQ-449a (SD-016 forward-path instrumentation
  probe) as the prerequisite for any EXQ-418b successor.
- Land V3-EXQ-445b/c (SD-032b monostrategy + terrain-inversion
  variants) once V3-EXQ-445a returns.
- Behavioural variants for SD-034 / MECH-267 / MECH-268 still need a
  tolerance-band completion env + phased rule_state training plan
  before any behavioural EXQ can be written; the landing-diagnostic
  smokes (V3-EXQ-460/462/463/465/466/468) have all PASSed.
- Next governance cycle: ingest the SD-032 behavioural FAILs, the
  SD-033 cluster landings, and the MECH-094 provisional persistence;
  rebuild `claim_evidence.v1.json`; regenerate `pending_review.md`.

---

## Status Snapshot (2026-04-20)

- **SD-032 cingulate integration cluster fully IMPLEMENTED 2026-04-19 (a/b/c/d/e).**
  In order of landing: SD-032b dACC/aMCC-analog adaptive control (Croxson/Shenhav/Kolling
  bundle -> DACCtoE3Adapter shim -> E3.select score_bias; ARC-033 vs ARC-058 shared-trunk
  as constructor-switch alternative), then SD-032a salience-network coordinator (soft
  operating_mode vector + MECH-259 Schmitt-trigger switch threshold + MECH-261 dict-keyed
  write-gate registry, 8 default targets, V4 register_target() extensibility), then
  SD-032c AIC-analog (drive- and mode-aware harm_s_gain subsumes SD-021 descending
  modulation; EXQ-325a bit-identical DESCENDING==CONTROL signature resolved), then
  SD-032d PCC-analog metastability scalar (modulates MECH-259 effective_threshold by
  drive_level / success EMA / time-since-offline; single integration point for MECH-092
  within-session quiescence and INV-049 cross-session sleep via enter_offline_mode), then
  SD-032e pACC-analog slow-EMA autonomic coupling (drive_bias write-back from z_harm_a,
  MECH-094 hypothesis_tag gated, alpha=0.002 default ~347-step half-life inside Guo 2018
  ACC mGluR5 LTP envelope). All modules under ree_core/cingulate/, backward-compatible
  master switches default False.
- **MECH-094 promoted candidate -> provisional (governance-2026-04-19T21).** First
  concrete write-gate wiring established by V3-EXQ-448 pACC hypothesis_tag skip PASS;
  12 supports / 0 opposing, confidence 0.856. Feeds the MECH-261 mode-conditioned
  generalisation.
- **SD-033 PFC subdivision cluster registered 2026-04-19.** SD-033 parent + SD-033a-e
  (lateral-PFC / premotor-analog / vmPFC-analog / OFC-analog / frontopolar parallel-goal
  deliberation) + MECH-262/263 + MECH-264/265 (frontopolar counterfactual-value and
  relative-importance monitoring). V3-pending; primary write target for MECH-261
  operating-mode-conditioned writes. Prong D frontopolar lit-pull (6 entries, mean conf
  0.81, Boorman 2009 / Mansouri 2017 load-bearing) broadened SD-033e from Koechlin
  branching to parallel-goal deliberation; reserved V4 operating-mode renamed
  deliberative_branching -> parallel_goal_deliberation (zero schema cost — mode names
  are dict keys). Design docs: `docs/architecture/sd_032_cingulate_integration_substrate.md`,
  `docs/architecture/sd_033_pfc_subdivision_architecture.md`.
- **Regression suite PRs 1-3 landed (ree-v3).** Three-layer architecture:
  (1) preflight (tests/preflight/, runner imports + queue integrity + machine boot; wired
  into experiment_runner.py startup with `--skip-preflight` escape hatch);
  (2) contracts (tests/contracts/ with C1 agent boot, C2 8-flag boot matrix, C3 seed
  determinism, C4 BG gating MECH-090/091, C5 imagined/acted isolation MECH-094, C6/C7/C8
  SD-032 dACC/AIC/PCC/pACC wiring; 24/24 pass in ~14s);
  (3) deferred changed layer stubbed via scripts/run_regression_suite.py. Serve.py
  `/api/regression/preflight` endpoint with 60s memoisation added (REE_assembly commit
  2cb1c9559). Contracts test wiring only, never thresholds from EXQ evidence.
- **EXQ-433 reclassified non_contributory; EXQ-433a scripted-eval successor queued**
  (2026-04-19). Root cause of EXQ-433 FAIL: event-distribution collapse in 3/4 seeds
  (seed 91: 303/0 agent/env, seeds 13/42: ~100/1-2). MECH-256 C1 forward_r2=0.983-0.9998
  unaffected. EXQ-433a uses CausalGridWorldV2.reset_to() for deterministic placement +
  30-trial scripted harness per event type; balanced 3/3/3/3 event counts in smoke;
  supersedes EXQ-433.
- **Governance cycle 2026-04-19T21 (post-SD-032 landing).** Promoted MECH-094 to
  provisional; held SD-020 at provisional; applied 12 `hold_pending_v3_substrate` batch
  (MECH-256/258/259/260/261/264/265, SD-029/032a/b/d/e); reclassified 3 FAIL manifests
  as non_contributory substrate-gap (EXQ-395 MECH-220, EXQ-418a SD-017, EXQ-430 INV-010
  — all addressable by SD-032 cluster); marked 7 experiments reviewed. Retest
  eligibility post-cluster: V3-EXQ-325b (SD-032c falsification signature); V3-EXQ-430a
  (MECH-261 offline-write-gating); V3-EXQ-418b pending diagnostic of SD-016
  cue_action_proj wiring. 5 SD-032 entries added to substrate_queue.json as implemented;
  EXP-0121 and EXP-0132 marked executed.
- **MECH-261 mode-gating lit-pull (2026-04-20T06:30Z).** 5 entries
  (Latchoumane 2017 SO-spindle-ripple triple coupling; Maingret 2016 hippocampo-cortical
  coupling reorganises mPFC; Helfrich 2018 MFC atrophy disperses SO-spindle coupling;
  Klinzing/Niethard/Born 2019 review; Boyce 2016 REM theta optogenetic). V4-staging
  findings: per-mode gate weights load-bearing; carrier rhythm is biological realisation
  of gate in SWS and REM; gate locus and write target may overlap in mPFC; within-REM
  target selection remains open. 795 literature entries, 805 runs indexed at lit-pull
  rebuild.
- **704 runs indexed (630 dirs + 74 flat); 831 queue-level completions across
  five machines** (252 PASS / 480 FAIL / 88 ERROR / 11 UNKNOWN). Queue: 2 items, both
  claimed — V3-EXQ-445 (SD-032b 3-arm ablation OFF / ON-independent / ON-shared-trunk,
  DLAPTOP-4.local) and V3-EXQ-447 (SD-032d deterministic validation, ree-cloud-2).
- **Current bottleneck: SD-032 cluster behavioural validation + SD-003 successor
  follow-through.** V3-EXQ-445 is the first behavioural gate on SD-032b (C2 dACC
  score_bias produces >=0.1 nats entropy delta in either ON arm). V3-EXQ-433a supersedes
  EXQ-433 as the MECH-256/SD-029 comparator test on scripted balanced events. 3 pending
  review (EXQ-397 FAIL ARC-007/SD-004 path memory, EXQ-433a FAIL MECH-256/SD-029
  scripted-eval comparator, V3-EXQ-325c ERROR).

## Immediate Work Queue (This Cycle)

- Land results for V3-EXQ-445 (SD-032b behavioural) and V3-EXQ-447 (SD-032d deterministic);
  both are the first post-landing validation gates for the cingulate cluster.
- Review EXQ-397 (ARC-007/SD-004 path memory) and EXQ-433a (MECH-256/SD-029 scripted
  comparator) in the next governance pass; clear V3-EXQ-325c ERROR.
- Queue SD-032 cluster retests now unblocked by substrate arrival: V3-EXQ-325b (SD-032c
  falsification signature), V3-EXQ-430a (MECH-261 offline-write-gating), and V3-EXQ-418b
  (gated on SD-016 cue_action_proj wiring diagnostic).
- MECH-261 V4 staging decisions tracked against the 2026-04-20 mode-gating lit-pull
  (carrier-rhythm gate implementation, within-REM target selection).

---

## Status Snapshot (2026-04-18)

- **SD-003 superseded.** After 28 accumulated FAILs across the two-pass counterfactual
  architecture, SD-003 was flipped to `superseded` with `superseded_by: [MECH-256, SD-029]`.
  New claims registered: MECH-256 (general single-pass forward-model comparator,
  stream-agnostic; Frith/Shergill/Haggard/Blakemore biology), MECH-257 (dual-function
  single-substrate E2: comparator vs evaluator, controller-gated), SD-029 (concrete
  z_harm_s instantiation of MECH-256), SD-030 (z_self stream, V4-deferred), SD-031
  (z_world stream, V4-deferred). Architecture doc:
  `docs/architecture/self_attribution_per_stream.md`. claims.yaml: 491 claims (+5).
- **V3-EXQ-433 queued (SD-003 successor test, next-up).** Event-conditioned single-pass
  comparator test on z_harm_s: residual = z_harm_s_observed − E2_harm_s(z_harm_s_{t−1},
  a_actual). SD-013 interventional training (fraction=0.5) during P1; P2 uses event-density
  controller that extends up to 200 episodes until ≥20 env-caused and ≥20 agent-caused
  hazards per seed (fixes EXQ-431 sample starvation). Criteria: C1 forward_r2 ≥ 0.9, C2
  self/ext attenuation ratio ∈ [0.3, 0.7] (Shergill), C3 approach SNR > 3, C4 density
  floor; PASS needs 3/4 seeds. Substrate prerequisites (ARC-033, SD-013, SD-011) all
  implemented — SD-029 is a read-mode claim over existing substrate.
- **Governance cycle 2026-04-18 (governance-2026-04-18-15z).** 2 `pending_user`
  recommendations applied as `hold_pending_v3_substrate`: SD-014 (implementation_phase=v3,
  4 supports/0 weakens lit-only) and SD-023 (override of indexer's promote_to_provisional
  to hold, with EXQ-332a indexed non_contributory). Pipeline clean (validator OK 68/68,
  772 runs indexed). **Pending review cleared: 0.**
- **New lit-pulls (wave 1):** LIT-0092 (MECH-104 LC-NE volatility; Sara 2009 Nat Rev
  Neurosci filled triangulation), LIT-0097 (INV-053 depression attractor; Huys/Daw/Dayan
  2015 added as HDD contrast class — HDD and INV-053 are complementary not identical).
  Plus three lit-pulls informing SD-003 successor design (comparator, evaluator, mode
  distinction modes). Literature entries: 741 (+14).
- **New experiments queued (wave 2):** V3-EXQ-434 (INV-053 depression attractor replication,
  5-seed LONG_HORIZON), V3-EXQ-435 (INV-054 phase-transition recovery, sustained-crossing
  criterion, supersedes EXQ-278), V3-EXQ-436 (SD-017 sleep phase ablation redesign with
  context-conditioned harm threshold, supersedes EXQ-242).
- **ree-cloud-2 onboarded.** Second Hetzner cloud worker (CX22 nbg1, IPv4 116.203.216.181)
  brought online. Parameterised systemd service template; cloud-scaler.yml extended to a
  two-server loop (ree-worker-1/ree-cloud-1 + ree-worker-2/ree-cloud-2); validator
  whitelist extended; contributor JSON registered. First real claim was V3-EXQ-355b
  (ARC-038 schema assimilation) rather than the dedicated smoke, because the runner's
  iteration order put the smoke behind any-affinity items — de facto pipeline verification.
- **772 runs indexed; 517 queue-level completions in runner_status.json**
  (102 PASS / 238 FAIL / 63 ERROR / 114 UNKNOWN).
- **Current bottleneck: SD-003 successor architecture validation + first-paper gate.**
  Active queue (17 items): V3-ONBOARD-smoke-ree-cloud-2, V3-EXQ-433 (SD-029 event-conditioned
  comparator, next-up), V3-EXQ-326, V3-EXQ-330a, V3-EXQ-328b, V3-EXQ-326a, V3-EXQ-407,
  V3-EXQ-332, V3-EXQ-321c, V3-EXQ-325b, V3-EXQ-355b, V3-EXQ-418b, V3-EXQ-434, V3-EXQ-435,
  V3-EXQ-436, V3-EXQ-406b, V3-EXQ-429b.

---

## Status Snapshot (2026-04-17)

- **New substrate: SD-016 (frontal cue-indexed integration) implemented 2026-04-16.** E1 queries ContextMemory via z_world using world_query_proj; cue_action_proj provides affordance bias to E2; cue_terrain_proj provides (w_harm, w_goal) terrain precision weights to E3. Config: E1Config.sd016_enabled (default False, backward compatible). Design doc: `REE_assembly/docs/architecture/sd_016_frontal_cue_integration.md`. Validation experiment V3-EXQ-418a queued with terrain_loss fix.
- **Governance 2026-04-16 completed: 16 experiments reviewed.** 5 PASS: EXQ-049a (MECH-090 bistable concordance, Layer 1+2 regression), EXQ-365 (MECH-104 surprise gate, 5-seed), EXQ-353 (ARC-033/SD-003/SD-013 interventional vs observational counterfactual), EXQ-323a (SD-019 affective nonredundancy on SD-022 substrate), EXQ-328a (MECH-090 bistable + SD-012). 11 FAIL/non_contributory/inconclusive including EXQ-385/418 (INV-049/SD-017, identical per-seed data — SHY collapse root cause identified), EXQ-355 (ARC-038 optimizer contamination), EXQ-330a (SD-013, later PASS in EXQ-330a — already confirmed 2026-04-15), EXQ-324a (SD-020 inconclusive, eval termination bug). 9 manifest reclassifications. 4 fix scripts written and queued (EXQ-418a, EXQ-385a, EXQ-355a, EXQ-324b).
- **EXQ-321a FAIL (2026-04-17):** MECH-090 bistable gate still failing. Root causes: 4-bug chain (shared training deepcopy on autograd tensors, spike timing vs E3-tick alignment, bistable config silently dropped via **kwargs). EXQ-321b queued with all 4 fixes; dry-run 3/3 seeds PASS.
- **766 runs indexed** (per morning digest 2026-04-17). **2 pending review** (EXQ-321a FAIL + UNKNOWN runner entry).
- **SD-016 lit-pull (2026-04-17):** Additional 3 entries added to targeted_review_sd_019 (wind-up/central sensitization, Craig 2003 interoception/insula, pain asymbolia). SD-022 lit-pull added 2 entries. Index now 706 lit entries total.
- **Deployment gating note added (2026-04-17):** V3 is treated as a sandbox-only scientific substrate. High-capability or externally connected REE deployment is gated on V4 social/developmental completion. See `docs/governance/deployment_gating.md`.
- **Current bottleneck: first-paper gate.** Active queue (18 items): EXQ-326 (SD-015/MECH-216/SD-012 wanting nav fix), EXQ-330a (SD-013 claimed), EXQ-321b (MECH-090 bistable fix), EXQ-325a (SD-021 descending modulation claimed), EXQ-395 (MECH-220), EXQ-375 (MECH-073), EXQ-328b (MECH-230 claimed), EXQ-326a (SD-015/MECH-229 nav), EXQ-406 (INV-053), EXQ-407 (MECH-231), EXQ-396 (ARC-016), EXQ-397 (ARC-007), EXQ-429 (INV-044), EXQ-430 (INV-010), EXQ-418a (SD-016+SD-017 fix), EXQ-385a (INV-049 SHY fix), EXQ-355a (ARC-038 optimizer fix), EXQ-324b (SD-020 eval fix).

---

## Status Snapshot (2026-04-15)

- **New substrate today: MECH-090 Layer 1 (trajectory stepping) + MECH-091 Layer 2 (urgency interrupt) implemented.** REEAgent now steps through committed_trajectory.actions[idx] via _committed_step_idx counter (Layer 1). Layer 2: when beta elevated and z_harm_a.norm() > urgency_interrupt_threshold (default 0.8), gate releases and step counter resets. Both wired in agent.py + E3Config.urgency_interrupt_threshold in config.py (2026-04-15).
- **New claims registered 2026-04-14: MECH-232 (DA representational expansion as approach mechanism), MECH-233 (asymmetric valence encoding: BLA tags vs VTA expands), ARC-057 (curiosity-approach emergence from DA-expanded map).** Architecture doc: hippocampal_valence_asymmetry.md. MECH-231 promoted candidate->provisional (conf from EXQ-407 PASS, 164x E2/E1 slope ratio).
- **EXQ-330a PASS (2026-04-15):** SD-013 contrastive counterfactual at interventional_fraction=0.5. forward_r2=0.999, cf_gap confirmed. Advances SD-013 evidence (already provisional conf=0.788).
- **EXQ-327 PASS (2026-04-14):** MECH-163 goal-conditioned navigation paper gate confirmed.
- **EXQ-365 PASS (2026-04-14):** MECH-104 surprise gate (5-seed) confirmed.
- **494 experiments completed.** 100 PASS, 236 FAIL, 51 ERROR, 107 UNKNOWN.
- **0 pending review** (as of 2026-04-15).
- **Current bottleneck: first-paper gate.** Active queue (16 items): EXQ-323a (SD-019 nonredundancy), EXQ-326 (SD-015 wanting gradient nav), EXQ-330a (claimed), EXQ-353 (SD-003 interventional vs observational), EXQ-321a (MECH-090 bistable gate retest), EXQ-325a (SD-021 descending modulation retest), EXQ-395 (MECH-220), EXQ-375 (MECH-073), EXQ-328b (claimed), EXQ-326a, EXQ-406 (INV-053), EXQ-407 (MECH-231), EXQ-396a (ARC-016 dual-bug fix), EXQ-396 (ARC-016 sweep), EXQ-397 (ARC-007 path memory), EXQ-418 (SD-017 + SD-016 context action).

---

## Status Snapshot (2026-04-14)

- **Key governance outcome: SD-013 promoted candidate->provisional (2026-04-13b governance).** conf=0.788, 5 supports/1 weakens. SD-013 (interventional training bias) now provisional. 7 experiments reclassified non_contributory.
- **New claim class registered: EXT-001 through EXT-007.** External AI/LLM failure mode catalogue with REE mechanism mappings (sycophancy, hallucination, reward hacking, goal misgeneralization, causal attribution gap, other-model collapse, context amnesia). claims.yaml: 454 claims total.
- **MECH-231 registered** (E2 short-horizon discriminative pair, cowork-2026-04-13-e). EXQ-407 queued.
- **EXQ-406 queued** (INV-053 depression attractor replication, 5-seed LONG_HORIZON characterisation, ~240 min).
- **~481 experiments completed.** 96 PASS, 235 FAIL, 51 ERROR, 99 UNKNOWN.
- **2 pending review** (as of 2026-04-14T04:18:29Z): v3_exq_326_wanting_gradient_nav_fix FAIL (MECH-216/SD-012/SD-015); V3-EXQ-326 UNKNOWN.
- **Current bottleneck: first-paper gate.** Active queue (17 items): EXQ-326, EXQ-332, EXQ-330a, EXQ-353, EXQ-322a, EXQ-328a, EXQ-321a, EXQ-325a, EXQ-365, EXQ-355, EXQ-395, EXQ-375, EXQ-385, EXQ-328b, EXQ-326a, EXQ-406 (INV-053 depression attractor), EXQ-407 (MECH-231 E2 short-horizon).

---

## Status Snapshot (2026-04-13)

- **Key governance outcome: EXQ-354 PASS (2026-04-13).** MECH-112 behavioral wanting/liking
  dissociation confirmed with SD-015 wiring (3/3 seeds). MECH-112 split into MECH-229
  (behavioral wanting/liking dissociation, active) and MECH-230 (latent z_goal structure,
  candidate). 7 dry-run FAILs from earlier sessions reclassified as non_contributory. SD-012
  design doc updated to IMPLEMENTED.
- **Five new experiments queued (2026-04-13):** V3-EXQ-355 (ARC-038 schema assimilation),
  V3-EXQ-365 (MECH-104 surprise gate, 5-seed), V3-EXQ-375 (MECH-073 valence geometry),
  V3-EXQ-385 (INV-049 offline consolidation necessity / sleep ablation), V3-EXQ-395
  (MECH-220 harm hub behavioral probe). Plus EXQ-328b (MECH-230 full run) and EXQ-326a
  (SD-015 + MECH-229 nav fix).
- **SDs moved pending->implemented since last snapshot:** SD-013 (interventional training),
  SD-015 (ResourceEncoder), SD-017 (minimal sleep infrastructure), SD-018 (resource proximity
  supervision), SD-019 (affective nonredundancy constraint), SD-020 (affective harm surprise PE),
  SD-021 (descending pain modulation), SD-022 (directional limb damage), SD-023 (environmental
  gradient texture). Also: ARC-033, MECH-090 bistable gate, MECH-120 SHY wiring, MECH-203/204
  serotonin substrate, MECH-205 surprise-gated replay fix, MECH-216 E1 predictive wanting.
- **481 experiments completed.** 96 PASS, 235 FAIL, 51 ERROR, 99 UNKNOWN.
- **0 pending review** (as of 2026-04-13T07:19:18Z).
- **Current bottleneck: first-paper gate.** Active queue (16 items): EXQ-327 (MECH-163
  goal-conditioned nav paper gate), EXQ-326a (SD-015 + MECH-229 nav fix), EXQ-353 (ARC-033/
  SD-003/SD-013 interventional vs observational counterfactual), EXQ-321a (MECH-090 bistable
  gate retest), EXQ-325a (SD-021 descending modulation retest), EXQ-365 (MECH-104 surprise
  gate), EXQ-355 (ARC-038), EXQ-395 (MECH-220), EXQ-375 (MECH-073), EXQ-385 (INV-049 sleep
  ablation), and fix iterations EXQ-322a/328a/330a/332/328b/326a.

---

## Status Snapshot (2026-04-06)

- **SD-011/SD-012 Full E3 Integration (2026-04-05).** z_harm_a now flows through the complete
  agent loop: agent.sense() -> LatentStack.encode() -> E3.select(). New E3Config parameters:
  urgency_weight (z_harm_a.norm() lowers commit threshold, D2 avoidance escape, capped by
  urgency_max=0.5) and affective_harm_scale (amplifies lambda_ethical by accumulated threat).
  E3.compute_harm_forward_cost() replaces deprecated HarmBridge path, rolling z_harm_s step-by-step
  through trajectory actions via ResidualHarmForward. Agent.compute_drive_level(obs_body) added
  as canonical SD-012 static method. All new parameters default to 0.0/None for full backward
  compatibility.
- **EXQ-247 queued:** 4-arm ablation validating full SD-011/SD-012 E3 integration. Tests
  urgency_weight and affective_harm_scale jointly with drive_weight across ablation conditions
  (FULL vs NO_URGENCY vs NO_AFFECT vs BASELINE). 3 seeds x 200 train + 50 eval x 200 steps.
- **New claims registered (2026-04-06 thought-intake sessions):** INV-049 (Offline Update
  Necessity Principle -- offline phases are a mathematical necessity for model-building agents),
  INV-050 (three-drive sleep regulation), INV-051 (optimal novelty range), MECH-178
  (noradrenergic REM suppression pathway), MECH-179 (MEL type-specificity), MECH-180
  (novelty-driven adaptive sleep), MECH-181 (cognitive reserve as update-loop maintenance),
  Q-033 (actigraphy MEL forecasting).
- **~198 experiments run.** 51 PASS, 123 FAIL, 22 ERROR, 2 UNKNOWN. 22 experiments
  currently queued (EXQ-223 through EXQ-247 series plus EWIN-PC onboarding smoke).
- **0 pending review** (as of 2026-04-04T18:45:00Z).
- **Current bottleneck: first-paper gate.** Active queue: EXQ-074e/234 (wanting/liking),
  EXQ-076e/235 (goal conditioning), EXQ-195 (SD-003 z_harm_s counterfactual), EXQ-247
  (SD-011/012 full integration), and sleep-architecture experiments (EXQ-242--246).

---

## Status Snapshot (2026-04-04)

- **SD-014 implemented (2026-04-04): hippocampal valence vector node recording.** 4-component
  valence vector V=[wanting, liking, harm_discriminative, surprise] added to RBFLayer and
  ResidueField (ree_core/residue/field.py). Each RBF center stores a valence_vecs buffer
  [num_centers, 4] updated incrementally per visit. MECH-094 gate applies: hypothesis_tag=True
  blocks valence updates. Prerequisite for ARC-036 and replay prioritisation via drive state.
- **ARC-028 + MECH-105 implemented (2026-04-04): hippocampal-BetaGate completion coupling.**
  HippocampalModule.compute_completion_signal() maps best trajectory score to a sigmoid
  dopamine-analog value. BetaGate.receive_hippocampal_completion() releases beta when signal
  >= threshold (0.75). Implements the Lisman & Grace 2005 subiculum->NAc->VP->VTA loop.
- **~292 experiment scripts authored.** EXQ-001 through EXQ-223 series. 0 pending review
  as of 2026-04-03 (all discussed). EXQ-125 currently running on DLAPTOP-4.local (ARC-029).
- **Governance clean.** 0 pending review items (generated 2026-04-03T21:39:23Z).
  Last governance cycle: 2026-04-03 (cowork-2026-04-03-b, 14 experiments reviewed;
  ARC-022 promoted to provisional).
- **Current bottleneck: first-paper gate experiments.** EXQ-223 PASS confirmed the minimal
  E1+E2+hippocampus core loop. Active queue: EXQ-074e (MECH-112/117 wanting/liking),
  EXQ-076e (MECH-116 E1 goal conditioning), EXQ-195 (SD-003 z_harm_s counterfactual),
  EXQ-125 (ARC-029 committed mode, running). SD-015 resource indicator in progress.

---

## Status Snapshot (2026-04-03)

- **EXQ-223 PASS: Minimal mind confirmed (2026-04-03).** The REE core loop —
  E1 (associative world model) + E2 (fast transition model) + HippocampalModule
  (trajectory proposal) + multinomial go/no-go + raw harm/reward signals — is sufficient
  for stable navigation, harm avoidance, and resource acquisition. 3/3 criteria met across
  all 3 seeds (harm_ratio 0.29–0.39; REE takes ~4.5× as much reward as random). The
  ablation strips the deliberative architecture entirely: commitment_threshold=−1.0 (always
  uncommitted), z_goal disabled, benefit_eval disabled. What remains is the predictive
  associative core alone — and it works. This is the first experimental confirmation that
  the E1+E2+hippocampus triad constitutes a minimal functional mind. **The circuit topology
  is a named-structure match to the zebrafish larva (5–7 dpf)**: dorsal pallium (E1) →
  cerebellum (E2) → lateral pallium (hippocampal module) → optic tectum + reticulospinal
  neurons (go/no-go) → lateral habenula (harm signal). The larva has no mature prefrontal
  cortex — no commitment architecture — matching the ablation exactly. It is the only
  vertebrate whose entire ~100,000-neuron CNS has been functionally imaged during free
  behaviour (Ahrens et al., 2013, *Nature Methods*; Portugues et al., 2014, *Neuron*).
  This match was derived from functional-architecture arguments, not from biology.
  Episode visualiser (`episode_viewer.html`) added to the explorer for trajectory playback.
  Full circuit table and references: see changelog 2026-04-03.
- **SD-011 and SD-012 both implemented.** SD-011 (dual nociceptive streams: z_harm_s +
  z_harm_a) validated at EXQ-178b PASS (2026-03-30). SD-012 (homeostatic drive modulation)
  implemented 2026-04-02: drive_weight default raised from 0.0 to 2.0, enabling
  effective_benefit = benefit_exposure * (1.0 + drive_weight * drive_level). Step 3.1
  substrate debt now substantially resolved (SD-008/009/010/011/012 all done).
- **~198 experiments run.** EXQ-001 through EXQ-212+ series. 51 PASS, 123 FAIL, 22 ERROR
  as of 2026-04-03. Breadth of FAIL reflects aggressive experimentation on a developing
  substrate -- each FAIL cluster was analyzed and resolved before the next iteration.
- **Breath oscillator and z_beta pathway wired (2026-04-02).** BreathOscillator integrated
  into core commitment decision (MECH-108). rv -> z_beta volatility pathway wired for Q-007.
  14 substrate-limited experiments marked scoring_excluded. EXQ-199--203 queued to re-run
  MECH-025/Q-007/MECH-029/MECH-026/MECH-057a on corrected substrate.
- **ARC-033 ResidualHarmForward promoted to ree_core (2026-04-02).** E2_harm_s forward model
  now in `ree_core/latent/stack.py`, enabling EXQ-195 (SD-003 z_harm_s counterfactual).
  EXQ-195 queued; this is the critical SD-003 re-validation step on the new harm pipeline.
- **Governance cycle active.** 36 experiments pending review (2026-04-03). PASS cluster
  includes SD-011 validation (EXQ-178b), terrain work (SD-015), and several MECH-1xx claims;
  FAIL cluster being classified (evidence vs diagnostic). Governance session in progress.
- **Current bottleneck: first-paper gate experiments.** SD-011/012 substrates cleared; next
  priority is EXQ-074e (MECH-112/117 wanting/liking), EXQ-076e (MECH-116 E1 goal
  conditioning), EXQ-195 (SD-003 z_harm_s counterfactual), and EXQ-182a (oracle ceiling
  for habit-system goal lift).

---

## Status Snapshot (2026-03-31)

- **V3 first-paper gate clarified.** `ree-v3` completion for the first paper is now
  explicitly scoped to the **waking, single-agent substrate**. Sleep, social extension,
  language/communication, nth-order ethics, and full psychiatric modelling are **not**
  blockers for V3 completion.
- **Immediate focus is the approach/goal side.** Harm/attribution substrate has advanced
  materially (SD-003 architecture, SD-005, SD-010, SD-011, ARC-033), but the main remaining
  V3 risk is still positive attractor behavior rather than harm avoidance.
- **Hard V3 completion gates for paper 1:** (1) post-SD-011 SD-003 works on `z_harm_s`,
  not only the legacy `z_world` form; (2) harm/attribution substrate is stable enough to
  treat as platform rather than ongoing rescue work; (3) SD-012 + MECH-112 yield genuine
  behavioral goal lift, not only `z_goal` activation; (4) ARC-030 is demonstrated as
  dual evaluation of the same trajectories by harm and goal channels inside one selector;
  (5) matched-seed reruns and at least one task variant confirm robustness; (6) governance
  state remains clean enough that review/index/claim status are aligned.
- **First-paper claim remains narrow.** Target claim is: REE architectural separation yields
  attributable, harm-avoiding, goal-directed agency in a waking single-agent substrate.
- **Deferred to V4/V5:** consolidation/sleep mechanisms, integrated self/other modelling,
  structured communication, and emergent ethical behavior in multi-agent settings.
  *(Note 2026-04-02:* The V4 deferral of social work reflects a precise architectural
  constraint: INV-043 establishes that testing whether ethical capacity is
  *developmentally activated* — not merely architecturally present — requires a
  multi-agent substrate with modelled caregiving. V3 tests the machinery (ARC-043
  Layer 6); INV-043 testing requires Layers 2-4 to be exercised socially.
  See `docs/architecture/developmental_curriculum.md#inv-043`.*)*

---

## Status Snapshot (2026-03-26)

- **V2 complete.** Series closed after EXQ-028 (2026-03-19). Governance cycle applied 7
  decisions, V3-pending gate lifted.
- **V3 active.** ~96 experiments run (through EXQ-096a). SDs 004–010 implemented.
  SD-010 (harm stream separation) unblocked the prior FAIL cluster: EXQ-056c/058b/059c all PASS.
- **SD-011 is the current bottleneck.** Dual nociceptive streams (z_harm_s + z_harm_a) are
  required for the SD-003 counterfactual redesign. EXQ-093/094 confirmed that
  `HarmBridge(z_world → z_harm)` has bridge_r2=0 (architectural impossibility by SD-010 design).
  ~10 experiments are blocked pending SD-011. Design doc: `sd_011_dual_nociceptive_streams.md`.
- **SD-012 registered.** Homeostatic drive modulation for z_goal seeding — required for
  EXQ-085+ (wanting/liking experiments) and for any goal-directed behavior validation.
  Design doc: `sd_012_homeostatic_drive.md`.
- **New claims registered (2026-03-24/25):** INV-032–038 (approach/avoidance symmetry,
  epistemic self-monitoring, goal maintenance, state definition, stored/active distinction,
  EVR pattern). ARC-030–035. SD-011/012. MECH-112–134.
- **Currently queued:** EXQ-074b (MECH-112/117 wanting/liking, supersedes EXQ-074) and
  EXQ-076b (MECH-116/ARC-032 goal conditioning, supersedes EXQ-076).
- **MECH-124 diagnostic:** When reviewing EXQ-074b/076b results, check whether z_goal
  salience is competitive with harm salience — if not, this is a V4 early risk indicator
  (consolidation-mediated option-space contraction).
- **0 pending review** as of 2026-03-25 (all experiments discussed and marked in
  review_tracker.json).
- **Phase gate:** SD-011 implementation → re-run blocked experiments → governance cycle.
- **Step 3.1 (Substrate Debt Resolution)** is the current active step; SD-008/009/010 are
  done; SD-011/012 remain.

---

## Status Snapshot (2026-03-20) — archived

- **V2 complete.** All three hard-stop criteria triggered after EXQ-028. Governance cycle
  run 2026-03-19: 7 decisions applied, V3-pending gate lifted, ARC-024 and SD-010
  registered.
- **V3 active.** 73 experiments run (through EXQ-059). Substrate SDs 004/005/006/007
  implemented. EXQ-030b PASS validated V3-form SD-003 attribution pipeline
  (attribution_gap=0.035, world_forward_r2=0.947). Current focus: SD-010 implementation
  (harm stream separation) to unblock ~10 pending FAILs.
- **Q-020 adjudicated:** ARC-007 strict (2026-03-16). HippocampalModule generates
  value-flat proposals; terrain sensitivity is a consequence of navigating
  residue-shaped z_world, not a separate hippocampal value signal.
- **17 pending FAILs** awaiting review (generated 2026-03-20). Root cause cluster:
  fused z_world containing harm signal → SD-010 substrate debt.
- `REE_assembly` is the canonical governance + specification repo. Current V3 roadmap
  is in §REE-v3 below; `v2_v3_transition_roadmap.md` is now historical.

---

## Status Snapshot (2026-02-28) — archived

- `REE_assembly` is the canonical governance + specification repo.
- `ree-v1-minimal` has served as the qualification harness: 8 genuine experiments
  completed (EXQ-000 through EXQ-007), 4 PASS, 4 informative FAIL (substrate-limited).
- Substrate debt items SD-001, SD-002, SD-003 registered. V1 has reached saturation
  for the claims it was designed to test. Further V1 runs (EXQ-008/009) complete the
  current evidence cycle; extended-seed reruns (EXQ-010–013) are low-priority confidence
  accumulation.
- V2 cutover gates passed 2026-02-18 but cutover was deferred. Correct decision: V2
  specification needs redesigning (Step 2.0, below) before implementation begins.
- JEPA integration guidance remains convergence-first: source-method details live in
  `REE_convergence`; `REE_assembly` keeps REE-first canonical contracts and adjudication
  outputs.

---

## Roadmap Discipline

**Each step must be completed in sequence. Before starting the next step:**

1. Record what was learned (update GOVERNANCE_STATE.md, substrate debt register, any
   affected claims).
2. Update this roadmap to reflect that learning — revise subsequent steps if the
   evidence changes what they should be.
3. Make the update-roadmap action explicit in the exit criteria of every step.

The roadmap is not a fixed plan; it is a living document that is deliberately updated at
each step boundary. Steps may be added, split, or reordered as understanding grows.

## V3 Completion Gate For First Paper (2026-03-31 clarification)

This section records the current planning boundary for when `ree-v3` should be considered
"complete enough" for the first real paper.

**Paper-1 target claim**

REE should support a narrow, defensible claim:

- A waking, single-agent REE substrate can learn stable self/world attribution, harm avoidance,
  and genuine goal-directed behavior from architectural separation rather than a monolithic
  reward objective.

**Must-pass gates**

- **Post-SD-011 SD-003 works in the current architecture.** Counterfactual attribution must
  succeed on the sensory-discriminative harm stream (`z_harm_s`), not only on the older
  `z_world` formulation.
- **Harm/attribution substrate is stable.** SD-005, SD-010, SD-011, and ARC-033 must be
  reliable enough to function as substrate rather than as active rescue work.
- **Goal-directed behavior is behaviorally real.** SD-012 and MECH-112 must produce a genuine
  GOAL_PRESENT vs GOAL_ABSENT behavioral lift, not just `z_goal` seeding.
- **Approach and avoidance compete in one selector.** ARC-030 must be demonstrated as dual
  evaluation of the same candidate trajectories by harm and goal channels inside a shared
  commitment process.
- **Results survive reruns.** Matched-seed reruns and at least one task variant must confirm
  the core behavior is not a one-task artifact.
- **Governance state is clean.** Review tracking, claim status, and experiment indexing must
  remain aligned enough for the evidence story to be legible to an external reader.

**Two-tier V3 completion (2026-04-02 clarification)**

V3 completion has two levels with distinct gates:

*V3 first-paper gate* (sufficient for Paper 1 claim):
- Habit-system goal-directed behavior demonstrated: SD-012 activates approach drive;
  EXQ-182a oracle confirms the environment is near-optimal for habit-level policy;
  goal-lift experiment (EXQ-074e successor) shows GOAL_PRESENT > GOAL_ABSENT behavioral
  lift with ARC-030 harm/goal competition in one selector.

*V3 full completion gate* (required before V4 entry):
- **HippocampalModule multi-step trajectory planning validated.** This is a V4
  prerequisite, not merely a V4 feature. V4's social extension ("sharing joys and
  sorrows", INV-029 benefit gradient) requires planning trajectories that affect
  another agent's z_harm_a accumulation and benefit_exposure over time. One-step
  greedy cannot reach this: it can approach its own resources but cannot plan paths
  that sustain another's joy or reduce another's sorrow over multi-step trajectories.
  The VTA/hippocampal system (MECH-163) must be validated in V3 to provide the
  planning substrate that V4 social cognition will depend on.
- All V3 first-paper gates passed.

See MECH-163 (dual goal-directed systems: habit vs hippocampally-planned).

**Explicit non-blockers for V3 *first-paper* completion**

- Sleep/offline consolidation mechanisms.
- Integrated self/other social modelling.
- Full language integration; simple future communication primitives are enough.
- nth-order multi-agent ethics tests.
- Full computational-psychiatry coverage.

**Deferred to V4/V5 / later papers** *(requires V3 full completion gates first)*

- Sleep-like consolidation as a load-bearing mechanism.
- Social coupling and other-modelling inside core substrate — **specifically requires
  hippocampal multi-step planning (MECH-163 VTA/planned system) from V3 full gate**.
- Structured communication between agents.
- Emergent ethical behavior in multi-agent settings.
- Stronger psychiatric modelling beyond single-agent perturbation analogs.
- **INV-043 (caregiver requirement)** — requires multi-agent substrate with modelled
  caregiving. V3 cannot test whether ethical capacity is *motivationally activated*
  (vs merely architecturally present). This is a first-class V4 research question.
- **MECH-158 (love-exclusion failure mode)** — requires developmental multi-agent
  substrate to test whether absence of love-experience collapses ethical motivation.
- **MECH-159 (intergenerational moral progress)** — requires multi-generation agent
  infrastructure. V5 scope or later.

*The distinction between V3 and V4 is not only scope but epistemological level:
V3 tests whether the machinery works. V4 tests whether the machinery develops correctly.
The ARC-043 stack makes this precise: V3 exercises Layers 6-9; V4 must exercise Layers
2-5 dynamically, with caregiving, developmental phases, and social residue.*

**Deployment constraint:** V3 may be used as a sandboxed scientific substrate, but
serious capability scale-up or external-world connectivity is deferred until V4
social/developmental completion. Language alone is not treated as sufficient
safety. See `docs/governance/deployment_gating.md`.

---

## Phase Definitions

### REE-v1 ✓ (completed purpose: qualification baseline)

**Primary role:** validate whether proposed mechanisms produce expected directional
effects under controlled conditions.

**Outcome:** useful for signal discovery and contract hardening. Not sufficient as final
architecture target due to stress-lane conflicts, limited environment breadth, and
accumulated substrate debt (SD-001, SD-002, SD-003). Four genuine PASSes confirm core
signal structure; four informative FAILs confirm substrate resolution limits, not
architecture failures.

**Post-V1 learning incorporated into roadmap:**
- E2/hippocampus conflation (SD-001) prevents clean mechanistic isolation
- E1/E2 mutual constitution (SD-002) reframes timescale-separation interpretation
- E2 self-attribution substrate (SD-003) is an unmet V2 design requirement
- V1 stateless grid cannot surface persistent agent causal footprint
- MECH-057 (control completion) requires multi-step environment with genuine commitment
  pressure; needs richer substrate before further testing

---

### REE-v2 ✓ (completed purpose: V2 qualification)

**V2 series closed after EXQ-028 (2026-03-19).** All three hard-stop criteria met.
Governance cycle completed 2026-03-19.

#### Step 2.0 — V2 Redesign ✓

**Primary role:** Produce an updated V2 specification that incorporates V1 learning.
The original V2 spec (representation-interface contract) remains in scope, but the
design must now account for SD-001/002/003 and explicitly address what V2 must deliver
to make future self-attribution and self-modelling experiments possible.

**In-scope:**
- Redesign V2 architecture to resolve SD-001: E2 separated as pure transition MLP,
  HippocampalModule created as distinct component of E3 complex
- Revise V2 entry criteria to include SD-003 requirements (see below)
- Produce first-pass V2 implementation spec: subsystem boundaries, required metrics,
  failure gates
- Define the persistent-causal-footprint environment requirement (SD-003)
- Capture mutual constitution (SD-002) in architecture documents

**Out-of-scope:**
- Implementation (code changes happen in Step 2.1 onward)
- New V1 experiments beyond EXQ-008/009

**Exit criteria:**
- Updated V2 implementation spec document exists with SD-001/002/003 addressed
- V2 entry criteria revised (see below)
- This roadmap updated with Step 2.1–2.5 refined based on redesign output
- GOVERNANCE_STATE.md SD-003 entry complete ✓ (done 2026-02-28)

**Outcome:** ✓ Complete. V2 spec produced (`docs/architecture/ree_v2_spec.md`). SD-001/002/003
addressed in design. Steps 2.1–2.5 scoped.

---

#### Step 2.1 — E2 Separation (SD-001 resolution) ✓

**Primary role:** Refactor E2 into a pure fast transition model. Create HippocampalModule
as a distinct component of the E3 complex. Close SD-001.

**In-scope:**
- `E2FastPredictor` → pure forward predictor: `forward(z, a) → z_next` (cerebellum-like)
- `HippocampalModule` (new) → trajectory proposal by navigating affective terrain; not
  by running transition predictions
- Counterfactual E2 querying made architecturally possible: `e2.forward(z, a_cf)`
- SD-001 closed in GOVERNANCE_STATE.md

**Out-of-scope:**
- Full E3 complex redesign (Step 2.2+)
- Self-attribution experiments (Step 2.4)

**Exit criteria:**
- E2 callable independently with arbitrary action input
- HippocampalModule exists as separate class
- Existing EXQ PASS results replicated on refactored substrate (parity check)
- Roadmap updated with any discoveries

**Outcome:** ✓ Complete. E2 is a pure fast transition MLP on z_self. HippocampalModule
created as distinct E3 component. SD-001 closed.

---

#### Step 2.2 — Representation Interface Contract ✓

**Primary role:** Lock stable representation-interface contract for sensing adapters
and E1/E2 latent prediction. This is the original primary V2 role, now sequenced after
E2 separation.

**In-scope:**
- Sensor adapters mapped to JEPA-like context/target latent interfaces
- E1/E2 representation-reference integration contract (`IMPL-022`)
- Stable output streams for latent prediction error and uncertainty
- Run-pack/adapter-signal compliance and calibration metrics

**Out-of-scope:**
- Full control-plane completion
- Hippocampal/E3 commitment architecture
- Full ethical arbitration dynamics

**Exit criteria:**
- Representation-interface contract stable across qualification and stress lanes
- Uncertainty/error streams calibrated and non-gamed across distribution shifts
- No unresolved adapter contract drift
- Roadmap updated with any discoveries

**Outcome:** ✓ Complete. MECH-059 PASS confirmed E1 precision and E3 confidence are
structurally independent. Representation interface stable.

---

#### Step 2.3 — Persistent Causal Environment ✓

**Primary role:** Upgrade the environment substrate so that persistent agent causal
footprint is present — actions at step N affect the landscape at step N+k in ways
that require disambiguation from independent environment change. This is the
prerequisite for SD-003 experiments.

**In-scope:**
- Environment design where agent-caused and environment-caused transitions are
  structurally distinct and must be separated for correct attribution
- Validation that E2 (now pure transition model from Step 2.1) can be queried
  counterfactually against this environment

**Out-of-scope:**
- Full self-attribution claim testing (Step 2.4)

**Exit criteria:**
- Environment exists with persistent agent causal footprint
- Baseline experiments confirm agent-caused / environment-caused distinguishability
- Roadmap updated with any discoveries

**Outcome:** ✓ Complete. CausalGridWorld implemented with persistent agent causal
footprint. EXQ-018 PASS confirmed agent-caused/environment-caused distinguishability.

---

#### Step 2.4 — Self-Attribution Substrate ✓ (V2 partial; V3 form validated)

**Primary role:** Implement and test counterfactual E2 querying for self-modelling.
First genuine experiments on self-attribution claims. Close SD-003.

**In-scope:**
- Counterfactual E2 queries integrated into agent decision loop
- First genuine experiments isolating agent-caused vs environment-caused harm
- Self-attribution claim coverage (claims to be identified during Step 2.0 redesign)
- SD-003 closed in GOVERNANCE_STATE.md

**Exit criteria:**
- At least one genuine PASS on a self-attribution claim
- E2 counterfactual querying demonstrated experimentally
- Roadmap updated with any discoveries

**Outcome:** ✓ Partial / hard stop. EXQ-027 FAIL triggered V2 hard stop: E2 cannot
discriminate agent-caused harm in z_gamma; SD-005 substrate required. V2
self-attribution experiments concluded. V3-form SD-003 validated at EXQ-030b PASS
(2026-03-18): attribution_gap=0.035, world_forward_r2=0.947. Full SD-003 achieved on
V3 substrate with z_world separation.

---

#### Step 2.5 — V2 Qualification ✓

**Primary role:** Genuine experiment coverage across core V2 claims. Sufficient evidence
to make V3 entry decision.

**Exit criteria:**
- Representation interface stable across qualification and stress lanes (from Step 2.2)
- Self-attribution substrate tested (from Step 2.4)
- Governance confidence above provisional thresholds for core V2 claims
- **Roadmap updated with V1+V2 learnings before V3 begins**
- V3 entry decision made explicitly

**Outcome:** ✓ Complete. V2 series closed after EXQ-028. 15 genuine V2 experiments
(EXQ-014–028): 5 structural-separation PASSes, 9 FAILs (all substrate-limited by
z_gamma conflation or SD-004 absence). Governance cycle 2026-03-19: 7 decisions
applied. V3 entry formally made.

---

### REE-v3 ← **current phase** (control completion + full attribution)

**Primary role:** Implement full attribution pipeline, control-plane heartbeat architecture,
and E3 commitment/accountability on the z_self/z_world split substrate (SD-004/005).

#### Step 3.0 — V3 Substrate Implementation ✓

SD-004 (E2 action objects; HippocampalModule navigates action-object space O), SD-005
(z_gamma → z_self + z_world split), SD-006 (asynchronous multi-rate heartbeat,
time-multiplexed phase 1), SD-007 (ReafferencePredictor for perspective-corrected
z_world). Q-020 adjudicated: ARC-007 strict (2026-03-16). CausalGridWorld extended
to V3 environment. EXQ-030b PASS: SD-003 attribution pipeline validated.

#### Step 3.1 — Substrate Debt Resolution ← **current step**

**In-scope:**
- SD-008: alpha_world ≥ 0.9 in LatentStackConfig ✓ (validated EXQ-040)
- SD-009: event-contrastive CE auxiliary loss for z_world encoder ✓ (EXQ-020 PASS)
- SD-010: harm stream separation ✓ (EXQ-056c/058b/059c PASS)
- SD-011: dual nociceptive streams (z_harm_s + z_harm_a) ← **current focus**
- SD-012: homeostatic drive modulation for z_goal seeding ← **next**

**Exit criteria:**
- SD-011 implemented and EXQ-093/094 successors run on dual-stream substrate
- SD-003 counterfactual redesigned for z_harm_s pipeline and validated
- SD-012 implemented; EXQ-085 successors (wanting/liking) runnable with functional z_goal
- Pending FAIL cluster (~10 experiments) reviewed after SD-011 implementation

#### Step 3.2 — V3 Claim Qualification

**In-scope:**
- ARC-016: E3-derived dynamic precision + end-to-end commitment→behavior behavioral distinction
- MECH-025: action-doing mode probe on V3 substrate
- MECH-057b: completion gate retest
- Q-007: valence-precision interaction
- SD-006: multi-rate loop validation at scale (ARC-023, MECH-089–093)
- MECH-090: beta-gated policy propagation
- ARC-024: harm attribution with SD-010 substrate
- Full V3-EXQ series (V3-EXQ-001 through V3-EXQ-010 as designed in transition roadmap)

**Exit criteria:**
- Governance confidence above provisional thresholds for core V3 control claims
- V3-pending claims adjudicated (ARC-007, ARC-016, ARC-018, MECH-025, MECH-033, Q-007)
- **Roadmap updated with V1+V2+V3 learnings before V4 begins**

#### Step 3.3 — V3 Governance Cycle and V4 Entry Decision

**Exit criteria to start V4:**
- Robust separation of exploratory simulation vs committed learning
- Stable behaviour under adversarial trajectory pressure
- Governance confidence above provisional thresholds for core control claims
- V4 entry decision made explicitly

---

### REE-v4 (later: social and institutional complexity)

**Primary role:** Scale to richer multi-agent coupling, language-mediated coordination,
and institutional constraints.

**Exit criteria:** To be defined during V3, informed by what V3 delivers.

---

## V2 Entry Criteria (revised 2026-02-28)

Original criteria (all still required):
- Representation-interface contract stable across qualification and stress lanes
- Uncertainty/error streams calibrated and non-gamed across distribution shifts
- No unresolved adapter contract drift

Added from V1 learning:
- **SD-001 resolved**: E2 implemented as pure isolatable transition model; HippocampalModule
  exists as separate component of E3 complex
- **SD-003 requirement**: Counterfactual E2 querying architecturally possible
  (`e2.forward(z, a_counterfactual)` callable independently)
- **Persistent causal environment**: environment substrate provides persistent agent
  causal footprint, enabling agent-caused vs environment-caused transition disambiguation

---

## Repository Roles

- `REE_assembly`: canonical claims, architecture docs, evidence matrix, governance outputs.
- `ree-v3`: **primary qualification lane** for V3 experiments and claim coverage. Default
  branch: `main`. Results go to `REE_assembly/evidence/experiments/`.
- `ree-v2`: transitional reference. V2 series complete (EXQ-014–028). No new experiments.
- `ree-v1-minimal`: legacy baseline/reference harness. No new mechanism development.
- `ree-experiments-lab`: **ARCHIVED** 2026-02-26. Synthetic scaffolding only; do not use.

---

## Immediate Work Queue (This Cycle)

**Current step: SD-003 Successor Validation + First-Paper Gate (as of 2026-04-18)**

SD-004 through SD-023 all implemented. ARC-033, MECH-090 (bistable + Layer 1 trajectory
stepping), MECH-091 Layer 2 urgency interrupt, MECH-120, MECH-203/204, MECH-205, MECH-216
implemented. **SD-003 superseded 2026-04-18** by MECH-256 + SD-029 + MECH-257. Governance
cycle 2026-04-18 applied 2 hold_pending_v3_substrate (SD-014, SD-023). 0 pending review.
Second Hetzner worker (ree-cloud-2) onboarded.

1. **V3-EXQ-433** (SD-029 event-conditioned single-pass comparator on z_harm_s — decisive
   test of the new self-attribution topology after SD-003 supersession; next-up priority=60).
2. **V3-ONBOARD-smoke-ree-cloud-2** (second Hetzner worker calibration smoke).
3. **V3-EXQ-321c** (MECH-090 bistable vs legacy gate hold rate, spike-aligned E3-tick fix).
4. **V3-EXQ-325b** (SD-021 descending pain modulation retest, E2 world-forward training fix).
5. **V3-EXQ-330a** (SD-013 contrastive counterfactual retest).
6. **V3-EXQ-418b** (SD-016+SD-017 context-conditioned action: SHY fix + terrain_loss).
7. **V3-EXQ-326 / V3-EXQ-326a** (SD-015 wanting-gradient nav and MECH-229 behavioral
   dissociation fix).
8. **V3-EXQ-434 / V3-EXQ-406b** (INV-053 depression attractor replication; 5-seed
   LONG_HORIZON characterisation).
9. **V3-EXQ-435** (INV-054 phase-transition recovery, sustained-crossing criterion,
   supersedes EXQ-278).
10. **V3-EXQ-436** (SD-017 sleep phase ablation redesign with context-conditioned harm
    threshold, supersedes EXQ-242).
11. **V3-EXQ-429b** (INV-044 Bayesian prior-before-posterior; SWS-ordered vs REM-only).
12. **V3-EXQ-407** (MECH-231 E2 short-horizon efference-copy discriminative pair).

---

## ARC-057 Environment-Complexity Gate (2026-04-14)

**Status: PARKED.** ARC-057 (curiosity-approach emergence) cannot be faithfully tested
in the current CausalGridWorld. The mechanism requires an environment where
representational expansion at a location captures genuinely additional information --
near-fractal complexity where zooming in reveals more structure. Grid cells are
informationally flat: a cell is a cell. See `docs/architecture/hippocampal_valence_asymmetry.md`.

**What this blocks:** Faithful testing of approach-via-representational-expansion (MECH-232),
the valence encoding asymmetry (MECH-233), and the curiosity-approach emergence (ARC-057).

**What this does NOT block:** The threat/avoidance side (harm residue field, BLA-pathway
logic) remains fully testable. All existing V3 architecture work continues. The claims
are registered and constrain future design even without experiments.

### Proxy mechanism policy

Any experiment testing approach behavior in the grid world will necessarily use a **proxy
mechanism** for the approach signal (e.g., explicit wanting gradient, DA-modulated place
priority, or direct goal-location bias). This is acceptable for testing downstream
architecture (commitment gating, trajectory selection, E3 evaluation) but carries a
contamination risk:

**Results obtained with a proxy approach mechanism may not generalize to an ARC-057-enabled
agent.** The proxy is a commanded gradient; ARC-057 is emergent from representational
expansion + curiosity. The downstream architecture may develop implicit dependencies on
proxy properties (e.g., gradient smoothness, signal strength, spatial extent) that the
real mechanism would not provide.

### Tagging requirements

1. **Any experiment that tests approach behavior** must declare in its docstring and
   manifest notes which proxy mechanism it uses for the approach signal.
2. **Tag**: experiments using a proxy approach mechanism should include `approach_proxy`
   in their tags. This enables future filtering when ARC-057 becomes testable.
3. **Evidence interpretation**: PASS results for claims that depend on approach behavior
   should carry an `evidence_quality_note` stating the proxy was used and results may not
   transfer to ARC-057-enabled substrate.
4. **Re-validation queue**: when a richer environment becomes available, all `approach_proxy`
   tagged experiments form the re-validation backlog.

### What "richer environment" requires

- More sensory input channels (visual texture, object features, spatial micro-structure)
- Larger latent spaces to encode location-dependent detail
- Significantly more compute for training
- Location-dependent information density (some areas genuinely have more to discover)

This is a V5+ concern. V3 and V4 proceed with proxy mechanisms and honest tagging.

---

## Open Questions

- **SD-010 HarmEncoder architecture**: should z_harm be a separate stream alongside
  z_world and z_self, or should it route through z_world after SD-010? The `l_space.md`
  architecture suggests a four-stream model (z_self, z_world, z_beta, z_harm).
- **ARC-016 E3-derived precision**: EXQ-038 FAIL — root cause (precision invariance)
  needs analysis before designing the next precision-regime experiment.
- **SD-006 phase 2**: time-multiplexed multi-rate is phase 1; true asynchronous
  execution (thread-based or event-loop) is still open. HTA (hierarchical temporal
  abstraction) is the recommended direction but not yet designed.
- **ARC-057 environment substrate**: what is the minimum environment complexity that
  would enable faithful testing of curiosity-approach emergence? Is a continuous 2D
  world with procedural texture sufficient, or does it require full 3D/visual input?
  See ARC-057 gate section above.

---

## Related Claims

- IMPL-008, IMPL-020, IMPL-021, IMPL-022
- MECH-057, MECH-058, MECH-059, MECH-060, MECH-063
- ARC-024, MECH-069, MECH-070, MECH-089, MECH-090, MECH-100, MECH-101, MECH-102
- SD-010 (harm stream separation)

## References

- `docs/architecture/jepa_ree_hybrid_diagram_spec.md`
- `docs/architecture/jepa_e1e2_integration_contract.md`
- `evidence/GOVERNANCE_STATE.md` (substrate debt register: SD-001, SD-002, SD-003)
- `evidence/experiments/claim_evidence.v1.json`
- `evidence/experiments/promotion_demotion_recommendations.md`
- `evidence/planning/CUTOVER_REE_V2_READINESS.md`
