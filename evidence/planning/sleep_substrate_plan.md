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

### Phase 7: Phase 1b (deferred broadcast read-site)

Conditional on Phase 1 PASS. If Option A statistical update produces
measurable precision movement but the agent still does not show
recalibration-driven behavioural recovery, add Option B broadcast
read-site at action selection consuming `precision_at_rem_entry` directly.
Per Q-042 verdict, biology runs both. We add the second arm only if
Phase 1 alone is insufficient.

GAP-5 (arousal-driven entry) is intentionally NOT in this plan. Per the
sleep-aggregation cluster doc C1, SD-037-driven entry is V4 scope and
deferred until V3 entry trigger has matured under empirical pressure.

---

## Status table

The resume primitive. Updated every session that touches sleep-substrate
work. See [Resume ritual](#resume-ritual) below.

| Gap | Phase | Status | Blocking on | Next action | Owner-EXQ | Last updated |
|---|---|---|---|---|---|---|
| GAP-1 | 1 | in-progress | V3-EXQ-541 result | Substrate landed 2026-05-09: `serotonin.compute_recalibration_target`, `E3.recalibrate_precision_to` Option A, WRITEBACK sibling step in `SleepLoopManager._run_cycle`, REEConfig flags `use_rem_precision_recalibration` + `rem_precision_recalibration_step` (default 0.1). 9/9 MECH-204 contracts + 237/237 preflight + contracts PASS. Awaiting V3-EXQ-541 PASS to mark `done`; companion EXP-0171 step-size sweep gated on PASS. | V3-EXQ-541 | 2026-05-09 |
| GAP-2 | 2 | blocked | EXQ-418e (SD-016 div-loss validation) result | Confirm EXQ-418e PASS, then re-queue 265/418/436/500/503 | re-queue ID set TBD | 2026-05-08 |
| GAP-3 | 3, 4 | open | covered by Phase 3 + Phase 4 | tracked under those phases | n/a | 2026-05-08 |
| GAP-4 | 4 | blocked | Phase 3 PASS (cluster must produce real routed events first) | After Phase 3 PASS, replace synthetic batch with replay-derived tuples | EXP-0169 | 2026-05-08 |
| GAP-5 | -- | deferred V4 | per cluster doc C1 | none in V3 | n/a | 2026-05-08 |
| GAP-6 | 5 | open | nothing | Walk write sites in SWS / REM / WRITEBACK paths | substrate audit (no EXQ) | 2026-05-08 |
| GAP-7 | 6 | open | nothing | Update /queue-experiment skill, audit 19 experiments | n/a | 2026-05-08 |
| GAP-8 | 3 | open | nothing | Extend HippocampalRouter to read routing_gate.weights | EXP-0168 | 2026-05-08 |

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
| GAP-8 / Phase 3 | (new entry to add for "downstream wiring") | MECH-272 | sleep_aggregation_cluster.md |

The substrate_queue.json edits to add cross-references and new entries are
made in the same session as this plan registration.

---

## Decision log

Append-only. Every architectural choice + every deviation pause / resume.

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
