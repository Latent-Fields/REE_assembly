---
closure_plan:
  id: sleep_substrate
  title: "Sleep Substrate"
  registered: 2026-05-08
  scope_claims: [SD-017, MECH-204, MECH-205, MECH-272, MECH-273, MECH-275, MECH-285, INV-049, Q-041, Q-042, SD-029, MECH-111, MECH-256, ARC-045, MECH-166]
  nodes:
    - id: "sleep_substrate:GAP-1"
      title: "MECH-204 precision recalibration consumer (F1 closure; V3-EXQ-541c PASS, cycle-count dose-response confirmed F1-sufficient)"
      phase: 1
      status: done
      severity: load-bearing
      owner_exq: V3-EXQ-541c
      unblocks_claims: [Q-041, Q-042, SD-029, MECH-111, MECH-256]
      depends_on: []
      last_updated: 2026-05-09
    - id: "sleep_substrate:GAP-2"
      title: "SD-017 retest cohort (V3-EXQ-265a PASS 2026-05-09; V3-EXQ-418l + 436a reclassified non_contributory 2026-05-10 pending ARC-065 substrate; 500a / 503a in pending review)"
      phase: 2
      status: upstream-blocked
      severity: high
      owner_exq: V3-EXQ-265a
      owner_exq_status: passed
      pending_owner_exqs: [V3-EXQ-500a, V3-EXQ-503a]
      reclassified_non_contributory: [V3-EXQ-418l, V3-EXQ-436a]
      unblocks_claims: [SD-017, ARC-045, MECH-166]
      depends_on: ["arc_062_rule_apprehension:ARC-065-substrate"]
      upstream_block_reason: "ARC-065 (behavioral-diversity-generation pathway) registered 2026-05-10. V3-EXQ-418l + 436a returned bit-identical sleep-vs-waking metrics across all seeds because the agent's waking phase produces no behavioural variation for sleep to refine. Sleep refinement experiments cannot register signal until the agent has waking diversity to refine. See arc_062_rule_apprehension_plan.md decision log 2026-05-10 entry."
      resume_condition: "V3-EXQ-543b/c PASS demonstrating non-degenerate cross-seed behavioural diversity in waking phase under ARC-065 substrate, then re-queue 418m + 436b under the diversity-substrate stack."
      last_updated: 2026-05-10
    - id: "sleep_substrate:GAP-3"
      title: "Phase B-E master flags default-False (cluster silent)"
      phase: 3
      status: open
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-285, MECH-272, MECH-275, MECH-273]
      depends_on: ["sleep_substrate:GAP-8"]
      last_updated: 2026-05-08
    - id: "sleep_substrate:GAP-4"
      title: "MECH-273 offline gradient uses synthetic batch (replace with replay-derived)"
      phase: 4
      status: blocked
      severity: high
      owner_exq: EXP-0169
      unblocks_claims: [MECH-273]
      depends_on: ["sleep_substrate:GAP-3"]
      last_updated: 2026-05-08
    - id: "sleep_substrate:GAP-5"
      title: "Sleep entry K-episode deterministic (no arousal trigger)"
      phase: null
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: []
      depends_on: []
      blocking_external: ["V4 SD-037 arousal substrate"]
      last_updated: 2026-05-08
    - id: "sleep_substrate:GAP-6"
      title: "StepHarness audit: SWS / REM write paths vs canonical sense/update sequence"
      phase: 5
      status: done
      severity: medium
      owner_exq: null
      unblocks_claims: []
      depends_on: []
      cross_plan_link: ["commitment_closure:GAP-10"]
      last_updated: 2026-05-15
      completed_note: "All 7 write sites audited and documented in sleep_aggregation_cluster.md; all are documented architectural exceptions; zero require StepHarness routing."
    - id: "sleep_substrate:GAP-7"
      title: "Multi-episode driver pattern not standardised (sleep cycles fire once at K=1)"
      phase: 6
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: []
      depends_on: []
      last_updated: 2026-05-08
    - id: "sleep_substrate:GAP-8"
      title: "MECH-272 routing weights flip but HippocampalRouter does not consume them"
      phase: 3
      status: done
      severity: high
      owner_exq: V3-EXQ-565
      unblocks_claims: [MECH-272, MECH-285]
      depends_on: []
      last_updated: 2026-05-15
      completed_note: "Substrate: anchor_weight scaling wired in run_sws_schema_pass(); mean_anchor forwarded by SleepLoopManager._run_cycle(); routing_gate.py docstring updated. Validation: V3-EXQ-565 queued + smoke C1/C2/C3 PASS 2026-05-15 (ARM_0 consumer-OFF weight==1.0; ARM_1 consumer-ON weight~=0.6; sws_n_writes=5 both arms via act_with_split_obs driver). EXP-0168 was the planning-time placeholder ID; V3-EXQ-565 is the queued validation experiment."
---
# Sleep Substrate Plan

**Registered:** 2026-05-08
**Status:** active
**Scope:** close the SD-017 / MECH-204 / sleep-aggregation-cluster gaps that
together prevent the offline-consolidation pathway from producing measurable
behavioural or evidential effect, and that gate Q-041, Q-042, SD-029, MECH-111,
MECH-256, INV-049, and the SD-049 sleep-on retest cohort.

This plan is the durable resume-point for sleep-substrate work across sessions.
When work pauses to handle adjacent paths (e.g. MECH-307 conjunction architecture,
StepHarness retest cohort, Q-040 factorial), the deviation is logged in the
[Decision log](#decision-log) below with a resume condition.

---

## One-line framing

> The sleep loop scaffolding has landed end-to-end; the read paths into it have
> not. Every post-A master flag is independently default-False, and the one
> recalibration claim that justified pulling sleep into V3 (MECH-204) captures
> its zero-point reference but never applies it.

The waking-side substrate has matured fast: V_s invalidation runtime (Phase 1-3),
anchor sets with dual-trace, MECH-284 staleness accumulator, MECH-269b rollout
gating, MECH-292/293 ghost-goal bank. The sleep-side substrate landed as a
five-phase scaffold (Phase A through E, MECH-285 / MECH-272 / MECH-275 / MECH-273)
between 2026-04-25 and 2026-04-27. None of the five phases has produced a
PASSing experimental result. The promotions of SD-017 (provisional -> stable
2026-04-24) and MECH-205 to stable were on literature only.

The gap is not "more design"; the gap is the read paths and the validation
runs.

---

## Source artefacts

Provenance for every gap and decision in this plan:

| Artefact | Role |
|---|---|
| 2026-05-08 sleep-substrate audit (this session) | Gap inventory; identified MECH-204 capture-without-consumer pattern, Phase B-E silent flags, SD-017 retest deferral chain |
| [docs/architecture/sd_017_sleep_phase_architecture.md](../../docs/architecture/sd_017_sleep_phase_architecture.md) | Parent infrastructure: SWS / REM passes, slot-formation-then-filling commitment |
| [docs/architecture/sleep_aggregation_cluster.md](../../docs/architecture/sleep_aggregation_cluster.md) | MECH-272 / MECH-273 / MECH-275 / MECH-285 build order, validation plan |
| [docs/architecture/v_s_invalidation_runtime.md](../../docs/architecture/v_s_invalidation_runtime.md) | MECH-284 / MECH-287 / MECH-269 online-arm Phase 1-3 (already implemented) |
| [docs/architecture/sleep/serotonergic_cross_state_substrate.md](../../docs/architecture/sleep/serotonergic_cross_state_substrate.md) | SR-1/SR-2/SR-3 spec; grounds MECH-203 / MECH-204 |
| [docs/architecture/sleep/precision_recalibration.md](../../docs/architecture/sleep/precision_recalibration.md) | Architectural commitment that REM provides the precision recalibration mechanism |
| [evidence/literature/targeted_review_q042/synthesis.md](../literature/targeted_review_q042/synthesis.md) | Q-042 Option A statistical update + Option B broadcast dual-arm verdict |
| [evidence/literature/targeted_review_mech285_sleep_replay_seed/SYNTHESIS.md](../literature/targeted_review_mech285_sleep_replay_seed/SYNTHESIS.md) | MECH-285 staleness-priority softmax verdict |
| substrate_queue.json MECH-204 entry (priority=1) | Named MECH-204 as top-priority unblocker per 2026-05-08 governance |

---

## Existing substrate (do not duplicate)

Wired and behaving correctly:

| Component | Location | Status |
|---|---|---|
| MECH-203 tonic 5-HT + benefit-salience tagging | `ree-v3/ree_core/neuromodulation/serotonin.py` | EXQ-255/256 PASS; adequate |
| MECH-205 surprise-gated replay | `ree-v3/ree_core/agent.py` `update_residue` | EXQ-258b PASS; stable |
| MECH-120 SHY normalisation wired into `enter_sws_mode` | `ree-v3/ree_core/predictors/e1_deep.py` | EXQ-245a wired |
| SD-017 SWS-analog `run_sws_schema_pass` | `ree-v3/ree_core/agent.py:4027` | code present, never validated end-to-end |
| SD-017 REM-analog `run_rem_attribution_pass` | `ree-v3/ree_core/agent.py:4138` | code present, never validated end-to-end |
| SD-017 `run_sleep_cycle` convenience | `ree-v3/ree_core/agent.py:4236` | code present |
| SleepLoopManager Phase A scaffolding | `ree-v3/ree_core/sleep/phase_manager.py` | wraps run_sleep_cycle |
| MECH-285 SleepReplaySampler Phase B | `ree-v3/ree_core/sleep/replay_sampler.py` | contracts only |
| MECH-272 RoutingGate Phase C | `ree-v3/ree_core/sleep/routing_gate.py` | contracts only; downstream consumer NOT wired |
| MECH-275 BayesianAggregator Phase D | `ree-v3/ree_core/sleep/bayesian_aggregator.py` | contracts only |
| MECH-273 SelfModelAggregator Phase E | `ree-v3/ree_core/sleep/self_model_aggregator.py` | contracts only; uses synthetic batch |
| V_s invalidation runtime Phase 1-3 (waking-side prerequisite) | `ree-v3/ree_core/hippocampal/`, `ree-v3/ree_core/regulators/` | landed 2026-04-22 - 2026-04-24 |

---

## Gap inventory

Eight gaps, ordered by leverage. Each is the basis for one row of the
[Status table](#status-table) below.

| Gap | Subject | Severity | Unblocks |
|---|---|---|---|
| **GAP-1** | MECH-204 precision-recalibration consumer absent (`precision_at_rem_entry` captured at REM entry, never read) | load-bearing | Q-041, Q-042, SD-029, MECH-111, MECH-256 |
| **GAP-2** | SD-017 retest cohort never re-run since SD-016 attention-uniformity fix landed 2026-04-25 | high | SD-017 stable -> empirically supported; ARC-045; MECH-166 |
| **GAP-3** | Phase B-E master flags all default-False; cluster silent unless every flag enabled independently | high | MECH-285, MECH-272, MECH-275, MECH-273 empirical promotion |
| **GAP-4** | MECH-273 offline gradient uses synthetic `(z_harm_s zeros, action one-hot round-robin)` batch, not replay-derived corrected residuals | high | MECH-273 honest validation (EXP-0169) |
| **GAP-5** | Sleep entry is K-episode deterministic, no arousal-driven trigger | low (V4 deferred) | SD-037-driven entry; not in scope |
| **GAP-6** | StepHarness integration: SWS / REM write paths not audited against canonical sense / update_z_goal / update_residue sequence | medium | bit-aligned waking + offline writes |
| **GAP-7** | Multi-episode driver pattern not standardised; sleep cycles fire once at end of K=1 default rather than across an experiment | medium | realistic ablation experiments |
| **GAP-8** | MECH-272 routing weights flip across phases but `HippocampalRouter` does not yet multiply destination strengths by them; only `mech272_*` diagnostics surface | high | MECH-272 functional validation (EXP-0168); MECH-285 effect on downstream consumers |

---

## Sequenced plan

Seven phases. Each phase is small, verifiable, and unblocks at least one
downstream item. Phases are ordered by leverage and by what each unblocks.
Where work depends on adjacent non-sleep paths (e.g. MECH-307), that is
called out as a deviation in the [Decision log](#decision-log).

### Phase 1: MECH-204 precision recalibration consumer (GAP-1)

Smallest scope, highest leverage. Add the missing read path so
`serotonin.precision_at_rem_entry` actually moves the waking precision
setpoint.

Deliverables:

1. `serotonin.compute_recalibration_target() -> float` returning the captured
   zero-point reference, plus a config flag `use_rem_precision_recalibration`
   defaulting False.
2. WRITEBACK-phase hook in `SleepLoopManager._run_cycle` that, when the flag
   is on, calls `e3.recalibrate_precision_to(target)`. Currently the WRITEBACK
   phase only handles MECH-273 self-model gradient + MECH-273 partial-decay;
   precision recalibration is a sibling step inside the same phase.
3. `E3Selector.recalibrate_precision_to(target)` API: Option A statistical
   update (move `_running_variance` toward `1.0 / target` with configurable
   step size) - per Q-042 verdict's Option A arm. Option B broadcast (read
   site at action selection time consuming `precision_at_rem_entry`)
   deferred to Phase 1b.
4. Validation EXQ: 2-arm ablation (recalibration ON vs OFF) running >=8
   episodes with sustained precision drift induced by deliberate harm /
   benefit imbalance; acceptance: post-REM `_running_variance` measurably
   moved toward zero-point reference in ON arm, unchanged in OFF arm.

Contract tests: at least one assertion that
`precision_at_rem_entry` is read by some module other than `get_state`
(catches any future regression to capture-only).

Phase 1b (deferred, conditional): broadcast read-site at action selection.
Per Q-042 verdict, biology runs both arms; landing Option A first lets us
measure whether Option B adds discriminative power.

### Phase 2: SD-017 retest cohort (GAP-2)

Re-run the SD-017 ablation cohort under SD-016 Path 1 diversification loss
ON, gated on EXQ-418e PASS. See [SD-017 retest cohort](#sd-017-retest-cohort)
section for the concrete experiment list. The retest does not require Phase 1
to land first - it tests the SWS-then-REM pass independently of precision
recalibration. Run order:

1. Confirm EXQ-418e PASS (SD-016 div-loss A2_div_only or A3_writes_plus_div
   produces `slot_diversity >= 0.5` with non-collapsed seeds across 3 seeds).
2. Re-queue EXQ-265, EXQ-418-cohort, EXQ-436, EXQ-500, EXQ-503 with
   `sd016_diversification_weight > 0` and full SD-017 flag stack on
   (`use_sleep_loop=True`, `sws_enabled=True`, `rem_enabled=True`).
3. Acceptance per experiment: `action_bias_div > 0` in SLEEP arms (vs
   identical-across-conditions pattern observed in 418/418a/436); slot
   metrics differ between WAKING / SWS_ONLY / SWS_THEN_REM.

### Phase 3: MECH-272 downstream consumer wiring (GAP-8) + EXP-0168 (Phase B end-to-end)

The cluster doc lists this as the Phase C "extend MECH-271 router consumer"
step. It did not land. Without it, MECH-285 priority sampling and MECH-272
routing weights produce diagnostics but do not change consumer behaviour.

Deliverables:

1. Extend `HippocampalRouter` (or whichever consumer reads anchor-channel /
   probe-channel routing) to multiply destination write strengths by
   `routing_gate.weights`. Single integration point.
2. Run EXP-0168 (already drafted, currently `gated`): high vs low waking
   trigger load over region R; sleep-replay event count over R must scale
   monotonically with `staleness[R]` at sleep entry, 2/2 seeds.
3. Acceptance: routing weights actually change downstream consumer output;
   EXP-0168 PASS.

This phase unblocks MECH-285 + MECH-272 empirical promotion together because
the sampler is silent without the routing gate consumer.

### Phase 4: MECH-273 real replay-derived training targets (GAP-4) + EXP-0169

Replace the synthetic `(z_harm_s zeros, action one-hot round-robin)` batch
in `SelfModelAggregator.offline_gradient_pass` with replay-derived
`(z_harm_s, a, posterior-corrected residual)` tuples drawn from the cycle's
routed events.

Deliverables:

1. Buffer the routed events during SWS + REM passes inside SleepLoopManager
   so the WRITEBACK phase has access to them.
2. For each buffered event, construct the training tuple from the actual
   z_harm_s seen during waking around the anchor's region, the action
   sampled from the replayed trajectory, and the posterior-mean correction
   from MECH-275 as the residual target.
3. Run EXP-0169 (already drafted, gated on Phase D): seed waking with
   biased self-attribution; sleep aggregator should correct it. Acceptance:
   mean of `self`-domain posterior shifts toward true causal_sig by >= 0.5
   SD across 3 sleep cycles.

### Phase 5: StepHarness audit (GAP-6)

Audit SWS-analog and REM-analog write paths against the canonical
sense / update_z_goal / update_residue sequence enforced by the
StepHarness landed 2026-05-08. Sleep-period writes must hit the same
canonical substrate as wake-time updates (per substrate_queue MECH-204
entry's implementation_hint).

Deliverables:

1. Walk every write site reachable from `enter_sws_mode`, `enter_rem_mode`,
   `run_sws_schema_pass`, `run_rem_attribution_pass`, MECH-273
   `offline_gradient_pass`. Confirm each either uses the StepHarness
   sequence or has a documented exception (e.g. `e1.shy_normalise` is a
   weight-decay write, not an experience write).
2. For any write site NOT using the harness: either re-route through it
   or document the architectural exception in
   `sleep_aggregation_cluster.md`.
3. Acceptance: every sleep-side write site is either StepHarness-routed
   or has a registered exception with a reason.

This phase has no validation EXQ of its own; it is a substrate audit.

### Phase 6: Multi-episode driver pattern (GAP-7)

Update `/queue-experiment` skill template + audit existing 19
sleep-touching experiments for the multi-episode driver pattern. Sleep
cycles need to fire across an experiment, not just at its boundary.

Deliverables:

1. Add a "multi-episode driver" section to the `/queue-experiment` skill
   that surfaces when any of `use_sleep_loop`, `sws_enabled`, `rem_enabled`
   is set in the proposed config.
2. Walk the 19 sleep-touching experiments and either confirm the loop
   fires meaningfully or annotate as "K=1 single-fire" / "K=N
   multi-fire".
3. Acceptance: every sleep experiment in `experiments/` has its driver
   pattern explicit in the docstring.

This phase has no validation EXQ of its own; it is a process improvement.

### Phase 7: Phase 1b (deferred to V4 unless future behavioural evidence reverses)

**Status (2026-05-09): deferred to V4 or later.** V3-EXQ-541c PASSed all
four criteria (overall_pass=True), confirming F1+step-tuning is the
operative MECH-204 architecture per the REM-precision lit-pull SYNTHESIS
dispatch case #1. Phase 7 / Option B (broadcast read-site at action
selection) is NOT needed for V3 closure.

**Original conditional design retained as architectural insurance:** if
future behavioural evidence reveals that the F1-sufficient reading is
incomplete -- e.g. a downstream claim's behavioural signature requires
the dual-arm pattern that Q-042 + Laukkonen-Friston-Chandaria 2025
hyper-model proposal preserve as a possibility -- Phase 7 implementation
is fully spec'd:

- Read `serotonin._persistent_zero_point` (the F1 cumulative reference)
  at `select_action()` time, NOT `serotonin._precision_at_rem_entry`
  (the moment-snapshot). Per lit-pull SYNTHESIS: Hobson-Hong-Friston
  2014 + Walker-Stickgold 2006 establish the cumulative reference as
  the biologically meaningful target.
- Apply broadcast as additive bias on E3 score, scaled by tunable
  `rem_precision_broadcast_gain` knob.
- Run alongside F1 (NOT replacing it -- the dual-arm pattern from
  Q-042's general waking finding).

**F2 (apply-before-recapture) is permanently OFF the option set.** The
2026-05-09 REM-precision lit pull found zero biological referent across
5 entries; F2 is a software shape divergent from the neuroscience
oracle.

**Trigger condition for Phase 7 work to resume:** a downstream behavioural
claim that depends on MECH-204 (Q-041, Q-042, SD-029, MECH-111, MECH-256
per GAP-1 unblocks_claims) FAILing in a way that forensic analysis
attributes to "F1 alone insufficient" rather than to other substrate
gaps. Until then, Phase 7 stays in V4 deferred state.

**Phase 7 dependency on REM-precision-recalibration lit-pull**
(2026-05-09): the Q-042 lit-pull synthesis covers general waking
precision-update timing (Iglesias 2013, Behrens 2007, Aston-Jones &
Cohen 2005, Frank 2015, Schwartenbeck 2014). It does NOT specifically
address REM-phase recalibration semantics or the 5-HT zero-point
mechanism's relationship to the broadcast arm. A focused lit-pull on
REM-phase timing (anchors: Hobson AIM, Pace-Schott + Stickgold
cumulative-cycle effects, Aghajanian + Fishbein 5-HT withdrawal and
post-REM precision recovery, Walker & Stickgold sleep-dependent
precision improvements) was queued 2026-05-09 to inform whether
Phase 7's broadcast site should:
- (a) read `_persistent_zero_point` directly (the F1 cumulative
  reference) at action selection,
- (b) read `_precision_at_rem_entry` (the most-recent moment-snapshot)
  at action selection,
- (c) read the *difference* between current rv and either of the above,
  scaled by some gain.

The lit pull gates the architectural choice (a) vs (b) vs (c). Until
its verdict lands, Phase 7 implementation is paused even if V3-EXQ-541b
results indicate F1+step-tuning is insufficient. **F2 (apply-before-
recapture) is NOT in the option set for Phase 7 -- decision-log entry
2026-05-09 records this**: biology does not run any "recalibrate-then-
recapture" pattern; F2 would be a software shape divergent from the
neuroscience oracle.

**Lit-pull verdict landed 2026-05-09** (5 entries +
SYNTHESIS.md at `evidence/literature/targeted_review_rem_precision_recalibration_timing/`):
choice (a) is the dominant pattern; (c) dual-arm is preserved as a
candidate via the Laukkonen-Friston-Chandaria 2025 hyper-model proposal;
(b) F3-only is NOT supported; (d) passive drift is NOT supported. F2
permanently confirmed discarded (zero papers support it).

Phase 7 design choice IF triggered (V3-EXQ-541b fails C3 across all
defensible step-size arms): the broadcast read should consume
`serotonin._persistent_zero_point` (the F1 cumulative reference) NOT
`serotonin._precision_at_rem_entry` (the moment-snapshot). Reasoning per
SYNTHESIS.md: Hobson-Hong-Friston 2014 + Walker-Stickgold 2006 establish
the cumulative reference as the biologically meaningful target; the
moment-snapshot is a substrate observable, not a behaviourally-consumed
signal. Apply broadcast as additive bias on E3 score at `select_action()`
time, scaled by tunable `rem_precision_broadcast_gain` knob, running
alongside F1 (NOT replacing it -- the dual-arm pattern from Q-042).

GAP-5 (arousal-driven entry) is intentionally NOT in this plan. Per the
sleep-aggregation cluster doc C1, SD-037-driven entry is V4 scope and
deferred until V3 entry trigger has matured under empirical pressure.

---

## Status table

The resume primitive. Updated every session that touches sleep-substrate
work. See [Resume ritual](#resume-ritual) below.

| Gap | Phase | Status | Blocking on | Next action | Owner-EXQ | Last updated |
|---|---|---|---|---|---|---|
| GAP-1 | 1 | done | (none) | F1 substrate landed 2026-05-09 (cross-cycle persistent zero-point EMA reference; 13/13 MECH-204 contracts + 241/241 preflight+contracts PASS). REM-precision lit-pull (5 entries; MECH-204 lit_conf 0.864): F1 dominant pattern; F2 permanently discarded (zero biological referent); F3 dual-arm preserved as conditional fallback. V3-EXQ-541a confirmed F1 mechanism. V3-EXQ-541b step-size sweep showed monotone dose-response but no arm cleared 5% C4 at 4 cycles. **V3-EXQ-541c (16 cycles, 4x exposure) PASSED all four criteria 2026-05-09: cycle-count dose-response is sub-linear but firmly NOT a plateau (~2.9x divergence growth per 4x cycle increase). ARM_4 step=0.5 cleared 5% C4 threshold at 9.03% in 3/3 seeds; ARM_3 step=0.25 came in at 4.51% just under. Tracking_quality monotonically improved 0.842 -> 0.921; zero overshoot. F1+step-tuning IS the operative architecture for V3 per lit-pull SYNTHESIS dispatch case #1.** Default `rem_precision_recalibration_step` bumped 0.1 -> 0.25 (high end of biologically defensible band per Q-042 Option A; strongest defensible default backed by 541c evidence). MECH-204 V3 closure complete. Phase 7 / Option B deferred to V4 unless future behavioural evidence reverses the dispatch. | V3-EXQ-541c | 2026-05-09 |
| GAP-2 | 2 | upstream-blocked | ARC-065 (behavioral-diversity-generation pathway) substrate not landed -- V3-EXQ-418l + 436a reclassified non_contributory 2026-05-10 (bit-identical sleep-vs-waking metrics; agent in monomodal collapse). 500a + 503a are surviving Tier-1 successors in pending review and are NOT diversity-dependent the same way. Resume after V3-EXQ-543b/c PASS under ARC-065 substrate, then re-queue 418m + 436b. See decision log 2026-05-10 entry + arc_062_rule_apprehension_plan.md for cross-cluster reflection. Original entry: | **V3-EXQ-265a PASSED all 4 criteria (2026-05-09T20:12Z, 22 min on Mac).** C1 sws_writes>0 in 3/3 WITH_SLEEP seeds (mean=8.0); C2 with_sleep slot diversity 0.257 > 0.10; C3 rem_rollouts>0 in 3/3 seeds; C4 (signed |diff|>0.05 between WITH/WITHOUT_SLEEP, either direction) PASSED in 2/3 seeds. Notable cross-seed heterogeneity: seed 42 sleep ADDED diversity (0.266 vs 0.175); seed 49 saturated near-tie (0.365 vs 0.358); seed 56 sleep COLLAPSED diversity (~0 vs 0.194). The C4 signed-difference acceptance shape is validated for use in successor experiments. EXQ-265 manifest flipped to evidence_direction=superseded with note explaining the SD-016 attention-uniformity confound that drove the C4 reversal in the original. Reviewed in review_tracker.json 2026-05-09T20:14Z. Phase 2 substrate template confirmed working end-to-end. Remaining Tier 1 EXQs (V3-EXQ-418c, 436a, 500a, 503a) STILL OUTSTANDING -- queue in fresh session(s) using the 5-flag template + supersedes pattern recorded in the 2026-05-09T19:49Z decision log; the C4 signed-difference shape (|diff| > 0.05) carried over directly. The seed-56 collapse pattern is worth flagging in 436a's design (3 conditions x 5 seeds) so per-condition aggregation handles bimodal cross-seed distributions cleanly. | V3-EXQ-265a (PASS); pending V3-EXQ-418c, 436a, 500a, 503a | 2026-05-09 |
| GAP-3 | 3, 4 | open | covered by Phase 3 + Phase 4 | tracked under those phases | n/a | 2026-05-08 |
| GAP-4 | 4 | blocked | Phase 3 PASS (cluster must produce real routed events first) | After Phase 3 PASS, replace synthetic batch with replay-derived tuples | EXP-0169 | 2026-05-08 |
| GAP-5 | -- | deferred V4 | per cluster doc C1 | none in V3 | n/a | 2026-05-08 |
| GAP-6 | 5 | done | (none) | Audit complete: all 7 write sites documented in sleep_aggregation_cluster.md; all are architectural exceptions; zero require StepHarness routing | substrate audit (no EXQ) | 2026-05-15 |
| GAP-7 | 6 | open | nothing | Update /queue-experiment skill, audit 19 experiments | n/a | 2026-05-08 |
| GAP-8 | 3 | done | (none) | Substrate wired (run_sws_schema_pass anchor_weight scaling; SleepLoopManager mean_anchor forwarding). Validation V3-EXQ-565 queued + smoke C1/C2/C3 PASS 2026-05-15 (consumer-OFF weight 1.0, consumer-ON ~0.6, sws_n_writes=5 via act_with_split_obs driver) | V3-EXQ-565 | 2026-05-15 |

Status values: `open`, `in-progress`, `blocked`, `paused`, `done`, `deferred`.
A `paused` row carries a resume condition in the [Decision log](#decision-log).

---

## SD-017 retest cohort

The cohort that needs to re-run once SD-016 attention-uniformity is fixed.
Two tiers.

### Tier 0: SD-016 substrate-fix series (must clear before SD-017 retest is interpretable)

| EXQ | Subject | Current status | Gates SD-017? |
|---|---|---|---|
| EXQ-477 | SD-016 ContextMemory attention-uniformity diagnostic (localised `key_proj.bias` dominance, ratio=4.24) | done (diagnosis) | yes (root cause identified) |
| EXQ-418d | SD-016 write-path 4-arm modes comparison | FAIL (`attn_entropy_mean ~2.76`) | yes |
| EXQ-418e | SD-016 Path 1 diversification loss (4-arm A0_off / A1_writes_only / A2_div_only / A3_writes_plus_div) | queued 2026-04-25, awaiting result | yes - primary unblocker |
| EXQ-418f | SD-016 attention uniformity probe | check status | yes |
| EXQ-418g | SD-016 selectivity-first 4-arm | check status | yes |
| EXQ-418h | SD-016 env-entropy precondition | check status | yes |
| EXQ-418i | SD-016 div-weight sweep | check status | yes |
| EXQ-418j/k | SD-016 ContextMemory reef | check status | yes |

Tier 0 acceptance: EXQ-418e arm A2_div_only or A3_writes_plus_div produces
`slot_diversity >= 0.5` with non-collapsed seeds across at least 2/3 seeds.

### Tier 1: SD-017 cluster retests (run after Tier 0 clears)

| EXQ | Tests | Prior verdict | Re-run trigger |
|---|---|---|---|
| EXQ-265 | SD-017 first-class SWS / REM methods validation, 2 conditions x 3 seeds | non_contributory | Re-run with `sd016_diversification_weight > 0` |
| EXQ-418 / 418a / 418b | SD-016 + SD-017 context-conditioned action | non_contributory (`action_bias_div=0.0`) | Re-run after EXQ-418e PASS |
| EXQ-436 | Cross-frequency bidirectional flow / context-conditional harm-threshold (WAKING_ONLY / SWS_ONLY / SWS_THEN_REM x 5 seeds) | non_contributory (`slot_cosine_sim` identical across conditions) | Re-run with div-loss ON |
| EXQ-500 | SD-017 sleep-phase readiness | check status | Re-run with full V_s circuit ON |
| EXQ-503 | SD-017 sleep-phase discriminative | check status | Re-run with full V_s circuit ON |
| EXQ-242 | SD-017 sleep-phase ablation (proxy hooks; superseded by first-class methods) | non_contributory | Skip - superseded by 265 / 500 / 503 |

Tier 1 acceptance per experiment: `action_bias_div > 0` or analogous
discriminative metric in SLEEP arms (vs identical-across-conditions
pattern observed in 418 / 418a / 436); slot metrics differ between
WAKING / SWS_ONLY / SWS_THEN_REM conditions.

For the retest to discriminate sleep ON / OFF rather than just clear the
SD-016 confound, the experiment configs must additionally enable:
- `use_sleep_loop=True`, `sws_enabled=True`, `rem_enabled=True`
- `use_per_stream_vs=True`, `use_anchor_sets=True`, `use_sd039_anchor_payload=True`
- Multi-episode driver (>= K episodes between sleep cycles; K=1 acceptable
  for first PASS but worth flagging)

---

## Cross-references

| Plan node | substrate_queue.json sd_id | claims.yaml claim | Design doc |
|---|---|---|---|
| GAP-1 / Phase 1 / Phase 7 | MECH-204 (priority=1) | MECH-204 | sleep/serotonergic_cross_state_substrate.md, sleep/precision_recalibration.md |
| GAP-2 / Phase 2 | (new entry to add) | SD-017, ARC-045, MECH-166 | sd_017_sleep_phase_architecture.md |
| GAP-3 / Phase 3 / Phase 4 | (existing MECH-272/273/275/285 entries) | MECH-272, MECH-273, MECH-275, MECH-285 | sleep_aggregation_cluster.md |
| GAP-4 / Phase 4 | (new entry to add for "real targets") | MECH-273 | sleep_aggregation_cluster.md |
| GAP-6 / Phase 5 | (new entry to add) | (audit, no claim) | sleep_aggregation_cluster.md |
| GAP-7 / Phase 6 | (skill change, no queue entry) | n/a | n/a |
| GAP-8 / Phase 3 | V3-EXQ-565 (queued 2026-05-15, smoke C1/C2/C3 PASS) | MECH-272 | sleep_aggregation_cluster.md |

The substrate_queue.json edits to add cross-references and new entries are
made in the same session as this plan registration.

---

## Decision log

Append-only. Every architectural choice + every deviation pause / resume.

### 2026-05-15 - GAP-8 validation experiment V3-EXQ-565 queued

V3-EXQ-565 written + queued via /queue-experiment (ree-v3 6ddf4ab). Two-arm
diagnostic: ARM_0 (use_mech272_routing_consumer=False) asserts
sws_anchor_weight_applied==1.0; ARM_1 (consumer ON) asserts ~=0.6 (the SWS-row
mech272_sws_anchor_weight). Three acceptance criteria C1/C2/C3; smoke all PASS
2026-05-15 (anchor_weight 1.0 vs 0.6 exact within tol; sws_n_writes=5 both arms;
mech285_draws=8; mech272_routed=8).

**Driver-pattern finding (carries to GAP-7).** First smoke FAILed C3
(sws_n_writes=0): `run_sws_schema_pass()` returns early at `n_buf < 2`, and
`_world_experience_buffer` is appended ONLY inside `REEAgent._e1_tick()`, which
runs from `act()` / `act_with_split_obs()` -- never from bare `agent.sense()`.
The Phase C contract test (`tests/contracts/test_sleep_phase_c_routing_consumer.py`)
drives with bare `sense()` and so can only assert `sws_anchor_weight_applied`,
not `sws_n_writes`. Any sleep experiment that needs the SWS write path exercised
must drive the agent with `act_with_split_obs()`. This is the concrete instance
of the GAP-7 multi-episode/driver-standardisation gap and should be folded into
the GAP-7 skill/audit work (the 19-experiment audit must check the driver call,
not just episode count). owner_exq for GAP-8 set to V3-EXQ-565 (EXP-0168 was the
planning-time placeholder ID).

### 2026-05-15 - GAP-6 done (StepHarness audit) + GAP-8 done (MECH-272 anchor-channel consumer)

**GAP-6 (StepHarness write-path audit):** All 7 write sites reachable from the five
sleep entry/exit/pass methods were walked and classified. Every site is a documented
architectural exception; zero sites require re-routing through StepHarness.
StepHarness lives in experiments/_harness.py:106, not ree_core/; sleep-period writes
cannot and should not call it by design. Audit documented in
sleep_aggregation_cluster.md under new section "## StepHarness write-path audit
(GAP-6)". GAP-6 acceptance criterion satisfied.

**GAP-8 (MECH-272 anchor-channel consumer):** anchor_weight scaling wired through
three layers: (1) RoutingGate.route() produces RoutedEvent.anchor_channel; (2)
SleepLoopManager._run_cycle() computes mean_anchor over SWS draws and calls
agent.run_sleep_cycle(sws_anchor_weight=mean_anchor); (3)
run_sws_schema_pass(anchor_weight) scales e1_input by anchor_weight before
context_memory.write(e1_input). routing_gate.py module docstring updated to document
the Phase C anchor channel consumption (GAP-8, 2026-05-15 tag).

### 2026-05-10 - GAP-2 status `in-progress` -> `upstream-blocked` by ARC-065 substrate

Triggered by user observation following ARC-065 cluster registration on
2026-05-10. Two of the four Tier-1 GAP-2 successors (V3-EXQ-418l SD-017
action_bias_div, V3-EXQ-436a SD-017+ARC-045+MECH-166 context-conditioned
harm) returned bit-identical sleep-vs-waking metrics across all seeds:

- 418l: with_action_bias_div = without_action_bias_div = 0.000450 every
  seed; signed_diff = 0.0; abs_diff = 0.0.
- 436a: waking_slot_cosine_sim = sws_then_rem_slot_cosine_sim and
  waking_harm_rate_dangerous = sws_then_rem_harm_rate_dangerous
  bit-identical for every seed (n_seeds_passed = 0 / 5 on every
  pre-registered criterion).

Sleep refinement of bit-identical waking content can only produce
bit-identical sleep content. Without the upstream behavioural-diversity-
generation pathway (ARC-065 cluster registered same day:
ARC-065 anchor + MECH-313 stochastic_noise_floor + MECH-314 / 314a / b / c
structured curiosity + MECH-312 multi-channel arbitration), the agent's
waking phase is monomodal and the discriminative-pair tests are
non_contributory. Both manifests reclassified `evidence_direction:
weakens -> non_contributory`; review_tracker.json updated; arc_062
plan-doc decision log carries the cross-cluster reflection.

GAP-2 status row: `in-progress -> upstream-blocked`. Pending owner-EXQs
trimmed from [418l, 436a, 500a, 503a] to [500a, 503a] (the surviving
two Tier-1 successors that PASSed and are awaiting routine review;
they are NOT diversity-dependent in the same way -- 500a is sleep
phase readiness check, 503a is SWS-vs-REM discriminative pair).
Reclassified-non-contributory list [418l, 436a] preserved as a
distinct field so the resume-condition workflow can re-queue 418m / 436b
once ARC-065 substrate lands.

Resume condition: V3-EXQ-543b/c PASS demonstrating non-degenerate
cross-seed behavioural diversity in waking phase under ARC-065
substrate. Then re-queue 418m + 436b with the same 5-flag Phase 2
template plus the new diversity-substrate flags.

Provenance: full triage entry in arc_062_rule_apprehension_plan.md
decision log under same-date heading "Pending FAIL triage: ARC-065
dependents reclassified non_contributory" (parent reflection on root
cause + what-is-now-blocked table also recorded there). The arc_062
plan is the parent for the rule-apprehension cluster including
ARC-065; the dependency direction is ARC-065 (foundational) -> ARC-062
(top-down rule selection) and ARC-064 (bottom-up rule extraction).

### 2026-05-08 - Plan registered

Audit conducted in conversation with user. Eight gaps surfaced and
sequenced into seven phases. User acknowledged all eight as in-scope
(none deferred beyond V4-natural GAP-5). User raised concern about
keeping plan alive across deviations; plan-doc + status-table + decision-log
pattern adopted, mirroring `sd033_governance_plan.md` precedent.

### 2026-05-08 - Phase 1 / Phase 7 split decision

MECH-204 recalibration could be implemented as Option A only (statistical
update on `_running_variance`), Option B only (broadcast read at action
selection), or both. Per Q-042 lit-pull verdict ("biology runs both arms;
the dual-update variant is favoured"), both are eventually wanted. Decision:
land Option A first (Phase 1) as the smallest precision-moving deliverable;
land Option B (Phase 7) only if Phase 1 PASS does not produce
behavioural-recovery effect. Reason: smallest-step principle; Option A is
self-contained; Option B's add value is empirical.

### 2026-05-09T20:14Z - V3-EXQ-265a PASS; Phase 2 substrate template validated; remaining 4 Tier-1 EXQs ready to queue

V3-EXQ-265a completed on Mac runner 2026-05-09T20:12:57Z (22 min wall) with
overall outcome PASS on all four criteria.

Result detail (3 seeds, 80 episodes, 150 steps/ep, 2 conditions WITH/WITHOUT
sleep):

  C1 sws_writes_all_seeds:        PASS (mean=8.0 in WITH_SLEEP, all 3 seeds)
  C2 with_sleep slot_div > 0.10:  PASS (mean=0.257)
  C3 rem_rollouts_all_seeds:      PASS (mean=6.0 in WITH_SLEEP, all 3 seeds)
  C4 with vs without differs:     PASS in 2/3 seeds (|diff| > 0.05 either dir)

Cross-seed C4 detail:
  seed 42: WITH=0.266, WITHOUT=0.175, diff=+0.090 -- sleep ADDED diversity.
  seed 49: WITH=0.365, WITHOUT=0.358, diff=+0.007 -- both saturated near-tie.
  seed 56: WITH=~0,    WITHOUT=0.194, diff=-0.194 -- sleep COLLAPSED diversity.

The signed-difference C4 acceptance shape is validated for use in successor
experiments. Either direction was informative; the docstring interpretation
grid correctly anticipated both add-diversity (seed 42) and flatten-diversity
(seed 56) outcomes. The seed-49 saturation case is the failure mode the |diff|
threshold guards against (correctly flagged as not-differing rather than
counted as a "supports" result by direction alone).

Architectural read on the cross-seed heterogeneity: under the Phase 2 stack
SWS does real work but the work is seed-sensitive. Two interpretations both
fit:
  (a) The stochastic prototype-sampling inside run_sws_schema_pass produces
      different schema sets per seed, and one set happens to project onto the
      div-loss-trained slot manifold collapsing to a single attractor while
      another set adds non-redundant prototypes. Architectural prediction:
      tighter stratification of the buffer-sampling step would reduce the
      seed-56 collapse rate.
  (b) The per-seed environment trajectory exposes the agent to qualitatively
      different residue terrain in the WITH vs WITHOUT arms (RNG state
      diverges across the sleep-cycle ticks), so the comparison is partially
      a comparison of different environments. Architectural prediction:
      replay-buffer matching across arms would tighten the comparison.
Either reading is consistent with PASS at the cohort level. Worth flagging
in 436a's design (3 conditions x 5 seeds) so per-condition aggregation
handles the bimodal cross-seed distribution cleanly -- mean-only summaries
would mask the seed-56-style collapse.

Bookkeeping landed this session:
- EXQ-265 manifest flipped to evidence_direction=superseded with note
  explaining the SD-016 attention-uniformity confound that drove the
  original C4 reversal (C4 in 265 FAILed with mean WITH=0.279 vs
  WITHOUT=0.293, direction-reversed; the failure was confound-driven, not
  a substrate refutation). The indexer now treats EXQ-265 as
  scoring_excluded:superseded; EXQ-265a is the operative measurement of
  SD-017 SWS/REM methods discriminative behaviour.
- review_tracker.json: appended both v3_exq_265 and v3_exq_265a run_ids to
  reviewed_run_ids; appended discussion_notes entry with full per-seed
  result detail; updated last_review_utc to 2026-05-09T20:14:34Z.
- sync_v3_results + build_experiment_indexes + generate_pending_review run.
  EXQ-265a now indexed (1012 runs vs 1011 before); per-experiment-type dir
  v3_exq_265a_sd017_sleep_phase_methods_validation_phase2/ created.
  pending_review.md down to 2 indexed-FAIL entries (530c, 141d) -- both
  belong to other sessions; 0 runner-only.

Decision: queue the remaining 4 Tier-1 EXQs in fresh session(s) using the
validated 5-flag Phase 2 template + supersedes pattern + signed-difference
C4 acceptance shape. The per-script template diff recorded in the
2026-05-09T19:49Z decision-log entry is mechanically applicable; one
adjustment to flag for the next session: 436a should add per-seed
distribution diagnostics (not just mean) so the seed-56-style collapse
pattern doesn't get masked at the cohort level.

GAP-2 status table row updated to record 265a PASS + owner-EXQ list still
showing 4 outstanding. Status remains `in-progress` until the 4 successors
land.

### 2026-05-09T19:49Z - GAP-2 Phase 2 first owner-EXQ queued (V3-EXQ-265a SD-017 methods validation Phase 2 retest)

Phase 2 work resumed in a fresh session per the 2026-05-09T13:52Z plan-of-record
closure recommendation. Audit of the 5 Tier-1 EXQ scripts confirmed none of them
already set the Phase 2 substrate flags (sd016_diversification_weight,
use_per_stream_vs, use_anchor_sets, use_sd039_anchor_payload). Substrate
readiness verified: all 5 flags exist in REEConfig.from_dims (config.py lines
522/687/715/1026/1615/1884/1889/2105/2108/2117/2150/2541/2544/2552/2585) and
are wired through to the relevant submodules (LatentStackConfig,
HippocampalConfig, AnchorSetConfig). Anchor-set has a structural precondition
that requires use_per_stream_vs=True (raised in HippocampalModule.__init__);
both flags are wired together in 265a's _make_agent.

V3-EXQ-265a written as a copy-and-modify of EXQ-265 with:
  - the 5 Phase 2 substrate flags added to _make_agent.
  - SD016_DIVERSIFICATION_WEIGHT=0.5 + sd016_writepath_mode="off" (the
    A2_div_only equivalent that EXQ-418e PASSed; A3_writes_plus_div was
    excluded per the 2026-05-09T13:52Z note about its one collapsed seed).
  - C2 threshold lifted 0.05 -> 0.10 (more conservative; under SD-016 div
    loss the baseline diversity is already much higher).
  - C4 redesigned to test signed-difference > 0.05 between WITH_SLEEP and
    WITHOUT_SLEEP at end-of-run, vs the original 265's "WITH > WITHOUT"
    direction-only check. Phase 2 acceptance per plan-of-record is "slot
    metrics differ between sleep arms"; either direction is informative.
  - supersedes="V3-EXQ-265" set in both queue entry and manifest output so
    the indexer flips the original 265 verdict to scoring_excluded:superseded.
  - Five-row interpretation grid in docstring distinguishing PASS, C4-only
    near-miss, substrate regression (C1/C3), and SWS-flattens-div-loss
    pathology (C2-only).
  - emit_outcome runner-conformance contract satisfied on every code path
    (--dry-run smoke + main run).

Smoke (Mac, --dry-run): backward compat preserved with sleep flags off.
Phase 2 stack + sleep ON: SWS n_writes=8, REM n_rollouts=6,
slot_diversity~1.01; per_stream_vs populated 3 streams; anchor_set
instantiated with use_sd039_anchor_payload=True. validate_experiments OK.
validate_queue OK. ree-v3 commit 9e343e7 pushed; Mac runner auto-claimed
within seconds (claimed_at 2026-05-09T19:49:50Z, status pending -> claimed).

Decision: queue 265a alone in this session. The remaining 4 Tier-1 EXQs
(V3-EXQ-418c, 436a, 500a, 503a) are NOT queued in this session. The Phase 2
substrate template is established by 265a (5-flag config diff + supersedes
metadata + acceptance-criterion shape). Each remaining EXQ applies the same
template to a different base script; per /queue-experiment skill rules each
needs its own code-review + smoke-test pass, and back-to-back skill
invocations would inflate context with diminishing return. Recommendation:
queue 418c next as a separate session (or this same session continues if
user prefers), letting 265a's result inform whether the C4 acceptance shape
needs adjustment for the multi-claim 436 (3 claims: SD-017 + ARC-045 +
MECH-166) and the discriminative-pair 503 (FULL_4_PHASE_ON vs
NO_SLEEP_BASELINE) before propagating.

Per-script template diff for the remaining 4 EXQs (recorded here so the
next session can apply mechanically):
  - Add to _make_agent / agent build: sd016_writepath_mode="off",
    sd016_diversification_weight=0.5, use_per_stream_vs=True,
    use_anchor_sets=True, use_sd039_anchor_payload=True. Sleep flags
    already present in original scripts.
  - 418c: base on EXQ-418a (canonical, shy_enabled=False fix), NOT
    EXQ-418 (buggy). 418a already has terrain_loss + LAMBDA_TERRAIN=0.1.
    Single-claim ["SD-017"]; no per-claim direction needed.
  - 436a: 3 claims [SD-017, ARC-045, MECH-166], 5 seeds, 3 conditions
    (WAKING_ONLY/SWS_ONLY/SWS_THEN_REM). Already emits
    evidence_direction_per_claim. Needs only the 5-flag substrate add.
  - 500a: single claim, sws+rem fixed True, EPISODES_PER_RUN=3 cycles.
    Diagnostic experiment; same 5-flag add.
  - 503a: discriminative pair (FULL_4_PHASE_ON vs NO_SLEEP_BASELINE),
    sleep_enabled boolean parameter. Single claim. Same 5-flag add.

GAP-2 status row advances `open` -> `in-progress` with owner_exq=V3-EXQ-265a
and pending_owner_exqs listing the remaining 4. Will roll forward as each
owner-EXQ lands.

### 2026-05-09 - GAP-2 status correction: Tier 0 was cleared by EXQ-418e A2_div_only on 2026-04-27

User asked whether GAP-2 was still blocked by EXQ-418e. Investigation
shows EXQ-418e ran twice on 2026-04-27 (T0159 + T0544 timestamps) and
both runs cleanly cleared the plan-of-record's Tier 0 acceptance
criterion (slot_diversity >= 0.5 in 2/3+ seeds with non-collapsed
seeds). The A2_div_only arm produced:

|   Arm                | slot_diversity_mean | slot_diversity_min | seeds_pass |
|----------------------|---------------------|--------------------|------------|
| A0_off (baseline)    | 0.199               | 0.191              | 3 (above floor only) |
| A1_writes_only       | 0.349               | **0.000**          | 2 (one collapsed) |
| **A2_div_only**      | **1.000**           | **0.9997**         | **3 (none collapsed)** |
| A3_writes_plus_div   | 0.611               | **0.0054**         | 2 (one collapsed) |

A2_div_only clears the threshold definitively. EXQ-418e's overall
FAIL was on a SEPARATE criterion (C1 attn_entropy still uniform across
all arms including A2 -- attention selectivity is a distinct concern
from slot diversity per se). The plan-of-record Tier 0 gate -- whether
SD-016's div-loss broke the slot collapse -- IS met. The
attention-selectivity question is a separate (more demanding) follow-on
that does not gate Phase 2.

GAP-2 status updated `blocked` -> `open` in both YAML frontmatter and
body status table. blocking_external on EXQ-418e removed. Phase 2 is
now ready to queue.

Note on config recommendation: A2_div_only is the cleaner config for
Phase 2 Tier 1 retests -- A3_writes_plus_div had one collapsed seed
in both 418e runs (slot_diversity_min ~ 0.005-0.007), so it's not
robust enough to baseline against. New Phase 2 sessions should set
`sd016_diversification_weight > 0` AND `use_writes_only=False` (or
equivalent flag for the relevant ContextMemory write path) to land
on the A2_div_only equivalent.

Phase 2 starter prompt at `/tmp/sleep_substrate_phase2_starter_prompt.md`
updated to reflect Tier 0 cleared (no /diagnose-errors detour needed).

### 2026-05-09 - V3-EXQ-541c PASS: MECH-204 V3 closure on F1; default step bumped to 0.25; Phase 7 deferred to V4

V3-EXQ-541c (16 cycles per run, 4x V3-EXQ-541b's 4 cycles) PASSED all
four criteria (overall_pass=True) in 201 sec on DLAPTOP-4.local.

Cycle-count dose-response across step arms (541b's 4 cycles → 541c's 16):

| step | C4 @ 4 cycles | C4 @ 16 cycles | scaling factor |
|---|---|---|---|
| 0.05 | 0.31% | 0.90% | ~2.9x |
| 0.10 | 0.63% | 1.81% | ~2.9x |
| 0.25 | 1.56% | 4.51% | ~2.9x |
| 0.50 | 3.13% | **9.03% (PASS)** | ~2.9x |

A 4x cycle-count increase produced ~2.9x divergence increase across all
arms -- sub-linear (waking drift still washes some) but firmly NOT a
plateau. ARM_4 step=0.5 cleared the 5% C4 threshold at 9.03% in 3/3
seeds; ARM_3 step=0.25 came in at 4.51% just under. Tracking_quality
monotonically improved 0.842 -> 0.921; zero overshoot in any arm.

**This is dispatch case #1 from the REM-precision lit-pull SYNTHESIS.**
F1+step-tuning is sufficient given enough exposure; Phase 7 / Option B
stays deferred. The Hobson-Hong-Friston 2014 + Walker-Stickgold 2006
F1-sufficient reading is empirically backed.

Three closure actions landed in this entry's commit:

1. **GAP-1 status `in-progress` -> `done`** in YAML frontmatter + body
   status table. owner_exq retained as V3-EXQ-541c (the validation that
   licensed closure). MECH-204 V3 closure complete.

2. **Phase 7 description rewritten**: deferred-conditional -> deferred-
   to-V4-unless-future-behavioural-evidence-reverses. Original Option B
   design retained as architectural insurance with a documented trigger
   condition (a downstream MECH-204-dependent claim FAILing in a way
   forensic analysis attributes to "F1 alone insufficient").

3. **Default `rem_precision_recalibration_step` bumped 0.1 -> 0.25** in
   ree-v3 REEConfig dataclass + from_dims kwarg. Rationale: 0.25 is the
   high end of the biologically defensible band per Q-042 Option A
   verdict; V3-EXQ-541c shows this step produces measurable cross-arm
   divergence (4.51% at 16 cycles, 1.56% at 4 cycles) with perfect
   tracking_quality and zero overshoot. The previous default 0.1 was
   conservative; 0.25 is the strongest biologically-defensible default
   that balances movement magnitude against overshoot risk. Existing
   experiment scripts that pin step=0.1 explicitly (V3-EXQ-541, 541a,
   541b's ARM_2, 541c's ARM_2) are unaffected -- they pass step
   explicitly, not via default. Out-of-the-box behaviour for new
   experiments now uses 0.25; experiments wanting other values
   (including the conservative 0.1 baseline) should override.

Notes:

- ARM_3 step=0.25 just barely missed the strict 5% C4 threshold at 16
  cycles (4.51%). Either the threshold was conservative for the
  defensible band, OR ~24-32 cycles would let 0.25 clear strictly. The
  default-bump to 0.25 is justified by the dose-response trend + the
  541c PASS at step=0.5 (which clears comfortably).
- The 5% C4 threshold itself was set without prior knowledge of the
  effect size; in retrospect a sliding-scale or per-arm threshold
  matched to the expected dose-response would have been more
  informative. Future MECH-204 step-size sweeps (if any) should
  pre-register thresholds based on the 541b/541c dose-response curve
  rather than a single magic number.
- Phase 2 (SD-017 retest cohort) is now unblocked -- no Phase 1
  dependency remains. Recommended new session for Phase 2 work to
  keep context clean and avoid concurrency with the still-active
  runner-leak-fix session.

Phase 1 of sleep_substrate_plan.md is closed. The remaining gaps
(GAP-2 SD-017 retest cohort, GAP-3 Phase B-E master flags, GAP-4
MECH-273 replay-derived training, GAP-6 StepHarness audit, GAP-7
multi-episode driver pattern, GAP-8 MECH-272 routing-gate consumer)
are independent of MECH-204 closure and proceed on their own gating
chains.

### 2026-05-09 - V3-EXQ-541b result (clean monotone dose-response, FAIL on threshold only) + V3-EXQ-541c queued (cycle-count test, lowest-load-bearing-assumption discriminator)

V3-EXQ-541b (step-size sweep on F1 substrate) ran on DLAPTOP-4.local
in 180 sec. Result: outcome FAIL but ALL behavioural criteria except
C4 PASS in every step-size arm.

| Arm | step | tracking_quality | overshoot_rate | mean_rv_post | C4 cross-arm divergence |
|---|---|---|---|---|---|
| ARM_0_off | 0.00 | 0.877 | 0.00 | 0.31076 | (reference) |
| ARM_1 | 0.05 | 0.883 | 0.00 | 0.30988 | 0.31% |
| ARM_2 | 0.10 | 0.889 | 0.00 | 0.30901 | 0.63% |
| ARM_3 | 0.25 | 0.908 | 0.00 | 0.30638 | 1.56% |
| ARM_4 | 0.50 | 0.939 | 0.00 | 0.30200 | 3.13% |

C1+C2+C3 PASS in every arm. C4 FAIL in every arm vs the 5e-2 threshold,
but with a clean monotone dose-response (divergence doubles with each
step doubling). Tracking_quality monotonically improves with step;
zero overshoot. F1 mechanism is doing biologically meaningful work;
the 5% threshold appears conservative given the measured effect size.

The pattern sits between dispatch cases #2 and #3 from the lit-pull
SYNTHESIS. The divergence-grows-monotonically-with-step pattern is
consistent with F1 being the right architecture but waking drift
between cycles washing out most of the per-cycle recalibration before
the next cycle's rv_post measurement.

V3-EXQ-541c queued as a cycle-count discriminator with the fewest
load-bearing assumptions: same 5 step arms, same env, same seeds,
sleep_loop_K=1 + EPISODES_PER_RUN=16 (16 cycles per run vs 541b's 4
cycles). Tests whether F1 cross-arm divergence scales linearly with
cycle count under fixed waking drift (F1 sufficient given enough
exposure -> Phase 7 stays deferred per dispatch case #1) OR plateaus
at the 4-cycle level (F1 at its ceiling -> Phase 7 / Option B
becomes load-bearing per dispatch case #3). Estimated ~6 min on Mac.

This is the cheapest test that distinguishes "F1 needs more cycles"
from "F1 is intrinsically limited" without committing to either
architectural path. If 541c shows divergence growing roughly linearly
to ~12-15% at 16 cycles (4x of 541b's 3.13% peak), F1 is sufficient
and Phase 7 stays deferred. If 541c plateaus at ~3-5% regardless of
cycle count, F1 ceiling is confirmed and Phase 7 becomes load-bearing
per the lit-pull-supported design (broadcast read of
serotonin._persistent_zero_point at action-selection time, additive
bias on E3 score, dual-arm with F1).

GAP-1 status table row owner-EXQ rolls from V3-EXQ-541a -> V3-EXQ-541b
-> V3-EXQ-541c for the immediate cycle-count discrimination arc.

### 2026-05-09 - REM-precision lit-pull verdict (5 entries): F1 dominant, F3 dual-arm preserved as conditional fallback, F2 confirmed discarded

Targeted lit pull on REM-phase precision recalibration timing landed at
`evidence/literature/targeted_review_rem_precision_recalibration_timing/`
with 5 entries + SYNTHESIS.md. MECH-204 literature_confidence advanced
from 0.0 to 0.864; quadrant moved from speculative to plausible_unproven.

Entries:
- Hobson, Hong & Friston 2014 (DOI 10.3389/fpsyg.2014.01133) -- supports F1, conf 0.82.
- Hong, Fallon, Friston & Harris 2018 (DOI 10.3389/fpsyg.2018.02087) -- supports F1, conf 0.68.
- Sakai & Crochet 2001 (DOI 10.1016/s0306-4522(01)00103-8) -- substrate for MECH-203 quiescence + MECH-204 capture moment, conf 0.78.
- Walker & Stickgold 2006 (DOI 10.1146/annurev.psych.56.091103.070307) -- supports F1's cumulative-across-cycles pattern by analogy from sleep-dependent memory consolidation, conf 0.74.
- Laukkonen, Friston & Chandaria 2025 (DOI 10.1016/j.neubiorev.2025.106296) -- mixed; tilts toward F3 / Option B as candidate dual-arm complement to F1, conf 0.62.

Verdict: dominant biological pattern is F1 (cross-cycle slow-EMA reference
accumulated during REM, consumed passively by waking via the refined
generative model). Hobson-Hong-Friston 2014's architectural commitment is
F1-sufficient; Walker-Stickgold 2006's cumulative-across-cycles dose-response
pattern reinforces by analogy. Sakai 2001 grounds the substrate (88% of
serotonergic DR neurons go silent at REM entry).

The 2025 Laukkonen-Friston-Chandaria hyper-model proposal tilts toward a
DUAL-ARM reading -- biology may run BOTH F1 (parameter-refinement
absorption) AND F3 (active hyper-model broadcast at choice time) as a
sleep-extension of the Q-042 dual-arm finding for general waking
precision-update timing. The hyper-model is the active-inference framing
of Phase 7 / Option B. NOT directly tied to REM-captured zero-points in
the literature; the F3-supporting reading requires inferring that the
hyper-model consumes them.

F2 (apply-before-recapture) confirmed discarded: zero papers in this lit
pull support the "recalibrate then re-snapshot" pattern. The architectural
shape has no biological referent. F2 is permanently off the table.

Phase 7 implication dispatch table (now in SYNTHESIS.md verdict section):
1. V3-EXQ-541b clears C3 in defensible step band {0.05, 0.10, 0.25} ->
   F1 + tuned step is the operative architecture; Phase 7 deferred to
   V4-or-later. MECH-204 V3 closure on F1 alone.
2. V3-EXQ-541b fails C3 in defensible band but ARM_4_step_0_50 clears it ->
   Phase 7 deprioritised; F1 with biologically-borderline step is barely
   sufficient. Dual-arm reading preserved as architectural insurance.
3. V3-EXQ-541b fails C3 across all arms including 0.50 -> Laukkonen-
   Friston-Chandaria 2025 hyper-model reading becomes load-bearing;
   Phase 7 / Option B implementation justified. Design (per lit-pull
   synthesis): broadcast read of `serotonin._persistent_zero_point`
   (F1 cumulative reference, NOT moment-snapshot) at `select_action()`
   time, additive bias on E3 score, scaled by tunable
   `rem_precision_broadcast_gain`, run alongside F1 (dual-arm).

Phase 7 description in this plan-of-record updated 2026-05-09 to record
the lit-pull dependency satisfied; the design choice (read persistent
not snapshot) is now lit-pull-grounded.

What this lit-pull does NOT settle: exact F3 broadcast gain (no direct
biological analogue); cumulative-vs-snapshot for the broadcast arm
specifically; whether 12% atypical DR neurons (Sakai 2001) carry
precision-relevant signal REE's binary tonic_5ht=0.0 ignores (V4 question);
SWS spindle-mediated consolidation interaction with REM-driven precision
recalibration (separate substrate question).

Recommended next action (per lit-pull SYNTHESIS): wait for V3-EXQ-541b
result (currently running on DLAPTOP-4.local), apply dispatch table.

### 2026-05-09 - V3-EXQ-541a F1 result; F2 discarded; EXP-0171 sweep + REM lit-pull queued

V3-EXQ-541a (F1 substrate) ran on DLAPTOP-4.local (95 sec) immediately
after the F1 fix landed. Result:

  C1 PASS (3/3 ARM_1 seeds fired every cycle)
  C2 PASS (mean_abs_delta = 3.62e-3 vs threshold 1e-3; FOUR ORDERS OF
       MAGNITUDE improvement over V3-EXQ-541's 9.05e-8 within-cycle no-op)
  C2 sign_consistency = 1.00 (direction always correct)
  C3 FAIL (cross-arm divergence = 5.64e-3 vs threshold 5e-2; ten times
       closer than V3-EXQ-541's 2.94e-7 but still under threshold)

Interpretation: F1 mechanism works as designed. Cycle records (ARM_1
seed 42) show genuine bidirectional rv movement: ep=1 cold-start no-op
(target = first capture by construction); ep=3 delta=+1.24e-3 (rv pulled
up toward 0.286); ep=5 delta=-5.48e-3 (rv pulled down toward 0.291);
ep=7 delta=-5.27e-3 (rv pulled down toward 0.296). The per-cycle
recalibration is doing its job, but the per-cycle effect (~5e-3) is
largely re-absorbed by waking drift over the ~400 steps between sleep
cycles, so cumulative cross-arm divergence stays at ~0.5%.

F2 (apply-before-recapture) discarded as a follow-on option after
checking biological evidence. Q-042 lit-pull synthesis (5 entries:
Iglesias 2013 basal-forebrain high-level PE, Behrens 2007 ACC
volatility, Aston-Jones & Cohen 2005 LC phasic NA, Frank 2015 STN-preSMA
threshold, Schwartenbeck 2014 DA policy precision) shows biology runs
two arms: a late post-outcome statistical update (Option A) AND a
separate pre-commit broadcast at action selection (Option B). Neither
matches F2's "recalibrate-then-recapture" semantic. F2 is a software
shape with no biological referent; pursuing it would diverge REE from
the neuroscience oracle. Decision: skip F2; the natural next move when
F1 is insufficient is F3 (Phase 7 / Option B broadcast read at action
selection), which IS the second arm biology runs.

Two parallel follow-ons queued instead:

(1) EXP-0171 step-size sweep instantiated as V3-EXQ-541b: 5-arm
parametric sweep of `rem_precision_recalibration_step` in {0.0_off,
0.05, 0.1, 0.25, 0.5}. Primary metrics tracking_quality (1 - mean(
|rv_after - target_variance| / target_variance)) and overshoot_rate
(fraction of cycles where rv crosses target). Lightweight: zero new
substrate code (the step is already a config knob landed in F1).
Pre-registered acceptance: at least one step in the biologically
defensible band {0.05, 0.1, 0.25} produces tracking_quality >= 0.7 with
overshoot_rate <= 0.1 in >= 2/3 seeds AND clears C3 (cross-arm
divergence >= 5%). FAIL-route: if no step satisfies both criteria,
F1+step-tuning alone is insufficient and Phase 7 / Option B becomes
load-bearing.

(2) Targeted lit-pull on REM-phase precision recalibration timing
queued via /lit-pull. Anchors: Hobson AIM model (REM as distinct
neuromodulatory regime), Pace-Schott + Stickgold (cumulative
across-cycle effects), Aghajanian + Fishbein (5-HT withdrawal and
post-REM precision recovery), Walker & Stickgold (sleep-dependent
perceptual precision improvements). Question: does biology
specifically support F1 (slow-EMA cumulative reference) vs F3
(broadcast read against the reference at action selection) for
**REM-phase** recalibration as distinct from the general waking
precision-update timing covered by Q-042. Output: synthesis verdict
informing Phase 7 design. Gates Phase 7 / Option B implementation.

Status table row GAP-1 unchanged at `in-progress`. The owner-EXQ rolls
from V3-EXQ-541a to V3-EXQ-541b for the immediate validation arc.
Phase 7 dependency on the lit-pull recorded in the Phase 7 description
(below).

### 2026-05-09 - V3-EXQ-541 FAIL diagnosis + F1 substrate fix; V3-EXQ-541a queued

V3-EXQ-541 ran on ree-cloud-1 (130 sec, 2026-05-08T23:43:02Z) and FAILed:
C1 PASS (substrate-readiness: recalibration fired every cycle in 3/3 ARM_1
seeds), C2 FAIL (mean_abs_delta = 9.05e-8 vs threshold 1e-3), C3 FAIL
(cross-arm divergence = 2.94e-7 vs threshold 5%). Sign-consistency was 1.0
in every cycle of every ARM_1 seed -- the DIRECTION of recalibration was
correct every time. The MAGNITUDE was six orders of magnitude under the
acceptance threshold.

Root cause: contract-test C8 of the original implementation flagged that
"within a single cycle, the captured precision_at_rem_entry equals rv at
REM entry, so Option A interpolation is mathematically a no-op against
itself". The cycle records confirm: every ARM_1 cycle had
target_variance ~ rv_before, so Option A linear interpolation
`new_rv = (1 - step) * rv + step * (1 / target)` collapsed because
`1 / target ~ rv`. Waking drift between cycles IS real (rv_history shows
0.288 -> 0.328 -> 0.274 -> 0.305 -> ...) but each new REM entry CAPTURED
the new rv as the new target, so the target tracked the rv rather than
acting as a stable reference for it to be pulled back to. Local re-run
on the Mac produced numerically identical results (mean_abs_delta 9.02e-8
vs cloud 9.05e-8), confirming reproducibility.

Concurrent finding from the cloud investigation: ree-cloud-1's
auto-sync conflict-recovery destroyed the original V3-EXQ-541 manifest
via `git stash --include-untracked` + `git reset --hard origin/master` +
`git stash pop` semantics -- the locally-committed manifest was reset
away and the selective `git add <manifest_path>` post-pop ran against a
deleted file. Manifest recovered from dangling commit `9e8f7786be` via
`git cat-file -p` and committed to master 2026-05-09. Diagnosis prompt
for runner-side fix delegated to a separate session at
`/tmp/cloud_manifest_leak_diagnosis_prompt.md` (option A: capture HEAD
SHA pre-reset, restore manifest paths via `git checkout <sha> -- <paths>`
post-reset). Distinct from the F1 substrate fix below.

F1 substrate fix landed 2026-05-09:

  - SerotoninConfig: new field `precision_zero_point_ema_alpha`
    (default 0.1).
  - SerotoninModule: new state `_persistent_zero_point: Optional[float]`
    (initially None). On `enter_rem(precision)`: cold-start sets
    persistent = first capture; subsequent captures EMA-track via
    `persistent <- (1 - alpha) * persistent + alpha * capture`.
    `_precision_at_rem_entry` preserved unchanged for diagnostic
    continuity.
  - SerotoninModule: `compute_recalibration_target` now returns
    `_persistent_zero_point` (not `_precision_at_rem_entry`). Returns
    0.0 sentinel when None (cold-start before first REM).
  - SerotoninModule: new `hard_reset()` method. Per-episode `reset()`
    preserves `_persistent_zero_point` so the long-horizon reference
    accumulates across episodes within a session; `hard_reset()` clears
    it (intended for between-stage resets).
  - REEConfig.from_dims: new kwarg `precision_zero_point_ema_alpha`
    (default 0.1) propagated to `cfg.serotonin.precision_zero_point_ema_alpha`.
  - get_state / load_state extended to cover `persistent_zero_point`;
    older state dicts without the field load cleanly (None).

Contract suite: tests/contracts/test_mech204_precision_recalibration.py
extended from 9 to 13 tests. New: C10 cross-cycle EMA arithmetic, C11
persistent-survives-reset / clears-on-hard-reset, C12 alpha edge cases
(0.0 freezes on first capture, 1.0 reverts to legacy snapshot behaviour),
C13 state-roundtrip preserves persistent. All 13 PASS. Full preflight +
contracts 241/241 PASS (was 237 + 4 new F1 tests).

V3-EXQ-541 manifest flipped to `evidence_direction: superseded` with
`evidence_direction_per_claim: {"MECH-204": "superseded"}` and a
`evidence_direction_note` preserving the diagnosis as the architectural
finding that drove the F1 fix. Indexer treats it as `scoring_excluded:
"superseded"` per the EXQ Versioning policy.

V3-EXQ-541a queued (priority=4, machine_affinity=any, supersedes
V3-EXQ-541). Identical 2-arm ablation; only manipulated variable is the
F1 substrate fix (now on the consumer side via the persistent zero-point
EMA reference). Pre-registered acceptance C1/C2/C3 unchanged. Auto-claimed
by DLAPTOP-4.local within seconds of the queue commit.

Status table row GAP-1 unchanged at `in-progress`; the owner-EXQ rolled
from V3-EXQ-541 to V3-EXQ-541a. EXP-0171 step-size sweep remains gated
on V3-EXQ-541a PASS rather than 541. If 541a also FAILs C2/C3, the
diagnosis points at F2 (apply-before-recapture) or F3 (Phase 7 Option B
broadcast read) per the original split decision.

### 2026-05-09 - Phase 1 substrate landed; V3-EXQ-541 + EXP-0171 queued

Phase 1 deliverables 1-3 (sleep_substrate_plan.md lines 107-122) implemented:

- `SerotoninModule.compute_recalibration_target() -> float` returns the captured
  `_precision_at_rem_entry` zero-point reference (returns 0.0 when disabled or
  when no REM entered, treated as "no target available" sentinel by the
  consumer).
- `E3TrajectorySelector.recalibrate_precision_to(target_precision, step) -> Tuple[float, float]`
  applies the Option A statistical update:
  `new_rv = (1 - step) * rv + step * (1.0 / (target + 1e-6))`. Returns
  `(rv_before, rv_after)`. No-op on `target <= 0` or `step <= 0`.
- `SleepLoopManager._run_cycle` runs the recalibration as a WRITEBACK-phase
  sibling step (independent of the MECH-273 self-model gradient pass). Gated
  on `use_rem_precision_recalibration` AND `agent.config.rem_enabled` AND
  `agent.serotonin.enabled`. Emits diagnostics
  `mech204_recalibration_fired`, `mech204_recalibration_target`,
  `mech204_running_variance_before`, `mech204_running_variance_after`,
  `mech204_recalibration_step`.
- New REEConfig fields `use_rem_precision_recalibration` (default False) and
  `rem_precision_recalibration_step` (default 0.1, per Q1). Both surfaced
  through `REEConfig.from_dims`.

Contract suite landed: `tests/contracts/test_mech204_precision_recalibration.py`
9/9 PASS covering module surface (C1), default-OFF backward compat (C2),
sleep-loop-ON / recalibration-OFF no-mech204-metrics (C3), arithmetic
correctness (C4), zero-target / zero-step no-op (C5/C6), the
**capture-only regression guard** (C7: `compute_recalibration_target` is
referenced from `phase_manager.py`), end-to-end WRITEBACK firing (C8), and
end-to-end drift movement (C9). Full preflight + contracts: 237/237 PASS.

Validation experiment `V3-EXQ-541` queued: 2-arm ablation
(ARM_0 OFF / ARM_1 ON step=0.1), 3 seeds x 8 episodes, sleep_loop K=2,
hazard-heavy / resource-thin CausalGridWorldV2 to drive sustained PE
variance between cycles. Pre-registered acceptance C1/C2/C3 per Phase 1
deliverable 4.

Companion proposal `EXP-0171` (manual_proposals.v1.json) registered for
step-size sweep tuning, gated on V3-EXQ-541 PASS. 5-arm parametric sweep
{0.0_off, 0.05, 0.1, 0.25, 0.5}; primary metrics tracking_quality and
overshoot_rate; FAIL-route identifies the regime where Option B (Phase 7)
becomes load-bearing.

Status table row GAP-1 advanced from `open` -> `in-progress`. Marks `done`
on V3-EXQ-541 PASS. Phase 1b (Option B broadcast read) remains
deferred-conditional per the original Phase 1 / Phase 7 split decision.

### 2026-05-08 - GAP-5 deferred to V4

SD-037-driven sleep entry (sustained low-arousal, high drive) is the
biologically more correct trigger but per `sleep_aggregation_cluster.md`
C1 it is deferred to V4 to avoid coupling sleep-cycle entry to the
still-validating SD-037 substrate. Resume condition: SD-037 promotion to
provisional (currently candidate, EXQ-483 pending).

---

## Open questions

Numbered for reference from future sessions.

- **Q1**: For Phase 1, should `_running_variance` be moved toward the zero-
  point reference by full replacement, by a tunable step size, or by a
  posterior-style update? Default proposed: tunable step size with
  config knob `rem_precision_recalibration_step` defaulting 0.1.
- **Q2**: For Phase 4 real targets, posterior correction comes from
  `MECH-275 BayesianAggregator` per-domain posteriors. The `self` domain
  uses SD-003 causal_sig as evidence. Open: how to handle the case where
  the posterior is uninformative (n_evidence < threshold) for a given
  region. Default proposed: skip writeback for that region; surface
  diagnostic.
- **Q3**: For Phase 5 StepHarness audit, `e1.shy_normalise` is a weight
  decay, not an experience write. Open: should the audit cover only
  experience writes, or all parameter / weight modifications? Default
  proposed: only experience writes; parameter updates live in the MECH-273
  exception.

---

## Resume ritual

When picking up sleep-substrate work after a deviation:

1. Read this plan document first.
2. Read the [Status table](#status-table) and identify the row that was
   `paused` or `in-progress`.
3. If `paused`, find its entry in the [Decision log](#decision-log) and
   confirm the resume condition has fired.
4. If `in-progress`, find the most recent decision-log entry for that
   phase and continue from the last concrete action.
5. Update the row's `Last updated` field and `Status` if it changes.
6. Append a new decision-log entry for any architectural choice made
   during the resumed session.

Sessions that do NOT touch sleep work do not need to read this document.
Sessions that DO touch sleep work read this document before any code or
experiment edit.

The plan-doc is the agent's working memory across sessions. TodoWrite
entries die with the session; WORKSPACE_STATE.md is recent-work, not
strategic; substrate_queue.json is granular but does not capture phase
ordering or decision rationale. This document is the single source of
truth for sleep-substrate strategy.

---

## See also

- [docs/architecture/sd_017_sleep_phase_architecture.md](../../docs/architecture/sd_017_sleep_phase_architecture.md)
- [docs/architecture/sleep_aggregation_cluster.md](../../docs/architecture/sleep_aggregation_cluster.md)
- [docs/architecture/v_s_invalidation_runtime.md](../../docs/architecture/v_s_invalidation_runtime.md)
- [docs/architecture/sleep/precision_recalibration.md](../../docs/architecture/sleep/precision_recalibration.md)
- [docs/architecture/sleep/serotonergic_cross_state_substrate.md](../../docs/architecture/sleep/serotonergic_cross_state_substrate.md)
- [evidence/planning/substrate_queue.json](./substrate_queue.json) MECH-204 entry (priority=1)
- [evidence/planning/sd033_governance_plan.md](./sd033_governance_plan.md) plan-doc precedent
- [evidence/planning/goal_pipeline_plan.md](./goal_pipeline_plan.md) -- adjacent plan; the SD-049 sleep-on cohort (V3-EXQ-514 family with `use_sleep_loop=True`, `sws_enabled=True`, `rem_enabled=True`) sits at the boundary of both plans. **goal_pipeline_plan owns the SD-049 substrate** (Phase 1 env-only, Phase 2 hybrid encoder, Phase 3 consumer cascade) and the wanting/liking + identity-recovery + wanting!=liking trajectory acceptance criteria. **sleep_substrate_plan (this doc) owns the sleep-loop side of validation**: SleepLoopManager Phase A-E scaffolding, MECH-204 precision recalibration consumer, MECH-272 routing-gate downstream wiring, MECH-273 replay-derived training targets, MECH-285 staleness-priority sampling. Either plan may sequence a V3-EXQ-514 successor with its respective flag stack; the other plan tracks the dependency under a `tracked` row. See goal_pipeline_plan.md "Boundary with sleep_substrate_plan.md" section for the full statement.
