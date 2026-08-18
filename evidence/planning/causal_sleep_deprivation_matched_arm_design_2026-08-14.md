---
title: "Matched-arm causal design: experimenter-triggered sleep vs continued wake in a single continuous life"
registered: 2026-08-14
status: design-staged (NOT queued -- two calibration constants gated, see Section 9)
chip_ref: chip-20260812-causal-sleep-deprivation-matched-arm-design
scope_claims: []
claim_ids: []
related:
  - sleep_substrate_plan.md (sleep_substrate:GAP-9)
  - organism_lifespan_development_review_906_lineage_2026-08-10.md
  - V3-EXQ-920 (true single-continuous-life base run)
  - V3-EXQ-929 (GAP-9 within-life trigger validation)
  - V3-EXQ-909 (force_cycle() precedent in this driver family)
---

**Status: DESIGN STAGED. Nothing in this file has been written to
`experiment_queue.json`, `claims.yaml`, or any registry. No experiment has been
queued from it.**

---

## 0. One-paragraph summary

V3-EXQ-920 established a TRUE single-continuous-life design (`EVAL_EPISODES=1`, no
segment-boundary respawn) in which **no sleep cycle can fire** -- confirmed
empirically by its own `total_sleep_cycles_fired = 0.0`. That makes 920 and its
successors capable of showing prolonged-wake-*associated* phenomena only, never
that absence of sleep *causes* anything. This document specifies the matched-arm
causal control that closes that gap: two otherwise-identical continuous lives, one
of which receives experimenter-scheduled sleep cycles and one of which does not.
The mechanism is fully resolved and verified against code (Sections 1-4). The
design is **not queued** because two calibration constants -- the sleep cadence and
the primary DV set -- are genuinely gated on
`chip-20260812-exq920-multiseed-degradation-retrospective`, which is still `open`
(Section 9).

---

## 1. Premise correction: GAP-9 closed while this chip was in the queue

The chip that commissioned this design (written 2026-08-12) states that there is
"currently no autonomous within-life sleep trigger", and reasons that
`force_cycle()` lets a causal experiment proceed **without waiting for GAP-9**.

That premise was correct on 2026-08-12 and is **no longer correct**. As of
2026-08-14, `sleep_substrate:GAP-9` is `status: done`:

- `SleepLoopManager.notify_waking_step()` landed on `ree-v3` `origin/main`
  (`ree_core/sleep/phase_manager.py`), called once per waking step from
  `REEAgent.update_residue()` (`ree_core/agent.py` ~line 9779), behind the
  default-False `use_within_life_sleep_trigger` + `within_life_step_ceiling`.
- **V3-EXQ-929 PASSED** the same day
  (`v3_exq_929_sleep_gap9_within_life_trigger_20260814T081606Z_v3`,
  label `within_life_trigger_validated`): OFF fires 0 across 3 seeds, ON fires 4/4/4
  at `step_ceiling=25` over 120 waking steps, ceiling-arm fraction 1.0.

This **strengthens** the case for the experiment and **changes the recommended
implementation mechanism** (Section 4). It does not make the chip moot: 929
validated *structural reachability only*, on an **untrained agent by design**
("the DV is structural reachability of a sleep cycle from within a single
continuous life, independent of learning"). Nothing yet tests whether within-life
sleep has any *functional* consequence. That is exactly what this design is for.

Two further points a later reader needs:

- The v1 ceiling arm hardcodes `need_crossed = False`. The MEL/need-crossing arm
  (design (b), the intended PRIMARY trigger per the 2026-08-14 lit synthesis) is
  **not wired**. So the landed trigger is a **pure step counter** -- experimenter-
  configured sleep wearing autonomous clothing. Section 5's labelling discipline
  therefore applies to it just as much as to `force_cycle()`.
- `chip-20260814-sleep-gap9-trigger-focused` is still `open` in `TASK_CHIPS.json`
  even though the build has landed; the ledger row is stale, not the substrate.

---

## 2. `force_cycle()` -- verified mechanics (chip item 1)

Read directly from `ree_core/sleep/phase_manager.py`, not from documentation.

```python
def force_cycle(self, agent: "REEAgent") -> Dict[str, float]:
    """Diagnostic / experiment hook: run a sleep cycle immediately,
    regardless of the K-episode counter. ..."""
    return self._run_cycle(agent)
```

It is a thin pass-through to the **same** `_run_cycle()` that
`notify_episode_end()` reaches. There is no separate code path and no
episode-boundary-specific setup.

### 2.1 Preconditions

| # | Precondition | Consequence if unmet | Status in the 906b/920 family |
|---|---|---|---|
| 1 | `agent.sleep_loop` exists (`use_sleep_loop=True`) | `AttributeError` | **Met** (`use_sleep_loop=True`) |
| 2 | `config.sws_enabled or config.rem_enabled`, when `require_sleep_passes_enabled=True` (the default) | **silent no-op**: resets counter, returns `None` | **Met** (both `True`) |
| 3 | `use_mech286_sleep_onset_gate` OFF, or the gate permits | cycle **blocked**; returns gate metrics only | **Met** (flag absent from the run's `enabled_default_off_flags`, i.e. default-False) |

Verified against the V3-EXQ-920 manifest's own
`enabled_default_off_flags`: `use_sleep_loop=True`, `sws_enabled=True`,
`rem_enabled=True`. So `force_cycle()` fires a real cycle in this family. This is
the single most load-bearing fact in the design and it checks out.

> **Gotcha worth pinning.** `force_cycle()`'s return annotation is `Dict[str, float]`
> but `_run_cycle()` can return `None` (precondition 2) or a *blocked-gate* dict
> (precondition 3). **A driver must check the return value**, not assume a dict.
> An unchecked `None` here is exactly how a "sleep arm" silently becomes a second
> wake arm -- which would invalidate the whole experiment while every criterion
> still reported green.

### 2.2 No episode-boundary state is required

`_run_cycle()` reads only live agent state that exists mid-life: `agent.config`,
`agent.hippocampal`, `agent._harm_replay_buffer`, `agent.e2_harm_s`, `agent.e3`,
`agent.serotonin`, `agent.goal_state`, `agent.e1`/`agent.e2`. It **never** calls
`agent.reset()` and **never** touches the environment. Nothing in it assumes an
episode just ended.

**Confirmed by precedent, not just by reading:** V3-EXQ-909
(`v3_exq_909_sleep_dv_fishtank_multifiring`) called `force_cycle()` at every eval
boundary in this exact 906b fishtank family across 3 seeds x 15 firings and
**PASSED** (`sleep_dv_nonnull_detected`), with `mean_sws_n_writes = 5.0` and
`mean_rem_n_rollouts = 10.0` -- i.e. the write paths genuinely engaged.

---

## 3. What a forced cycle actually does *in this config* (chip item 5)

This is narrower than the chip anticipated, and the precision matters for what a
positive result would license.

`_run_cycle()` is heavily config-gated. In the 906b/920 config the sleep-cluster
components are **absent**, so the following are all **skipped**:

| Component | Gate | State in 906b/920 |
|---|---|---|
| Phase B replay sampler (draws, frozen snapshot) | `replay_sampler is not None` | **OFF** (None) |
| Phase C routing gate (MECH-272) | `routing_gate is not None` | **OFF** |
| Phase D Bayesian aggregator (MECH-285) | `bayesian_aggregator is not None` | **OFF** |
| Phase E self-model writeback on `E2_harm_s` (MECH-273) | `self_model_aggregator is not None` | **OFF** |
| MECH-284 partial staleness decay | rides Phase E | **OFF** |
| MECH-204 precision recalibration of `E3._running_variance` | `use_rem_precision_recalibration` | **OFF** |
| MECH-423 cross-module consolidation | `cross_module_consolidator is not None` | **OFF** |
| SD-MEL-CONSUMER duration scaling (GAP-5b) | `mel_consumer is not None` | **OFF** |

*(Cross-checked against V3-EXQ-909's own chip note, which recorded that
`use_anchor_sets + use_mech285_sampler + use_mech272_routing` had to be **added**
to 906b's config to make `replay_diversity_index` reachable at all -- i.e. 906b
unmodified does not have them.)*

**What therefore actually runs** is exactly `agent.run_sleep_cycle()`:

1. `enter_sws_mode()` = `enter_offline_mode()` (gates `E1.context_memory` writes;
   also resets the SD-032d PCC `steps_since_offline` "rest clock" -- **inert here**,
   the PCC analog is not enabled in this family) + **MECH-120 SHY normalisation**
   on E1 (`shy_enabled=True` in 906b -- a real E1 decay applied on *every* sleep
   entry) + `serotonin.enter_sws()`.
2. `run_sws_schema_pass(anchor_weight=1.0)` -- writes compressed `z_world`
   prototypes into `E1.ContextMemory` (MECH-166 slot formation; ~5 writes).
3. `exit_sleep_mode()` = `exit_offline_mode()` + `serotonin.exit_sleep()`.
4. `enter_rem_mode()` = `enter_offline_mode()` + `serotonin.enter_rem(current_precision=...)`
   (SR-3 zero-point capture -- captured but, with MECH-204 off, **never applied**).
5. `run_rem_attribution_pass()` -- REM terrain rollouts (~10).
6. `exit_sleep_mode()`.

### 3.1 The confound, stated plainly (NOT resolved here)

A positive result from the design below establishes that **the SWS+REM offline
pass causally affects the measured DV**. It does **not** establish:

- **"unconsciousness" or "rest" as such.** The manipulation bundles the *mode
  transitions* (offline gating, serotonin enter/exit, SHY normalisation) with the
  *offline consolidation content* (schema installation, attribution rollouts).
  These are inseparable in a single `force_cycle()` call.
- **"sleep" in the full-cluster sense.** Everything in the table above is OFF, so
  this tests a deliberately narrow SD-017 core, not the Phase B-E aggregation
  cluster. A result here does not transfer to a cluster-enabled config.
- **anything about naturalistic sleep onset.** See Section 5.

**Optional dissociation (design extension, not required for v1).** Because the
components are separable at the API level, a third **ARM_SHAM** could call
`enter_sws_mode()` / `exit_sleep_mode()` / `enter_rem_mode()` / `exit_sleep_mode()`
**without** the two passes. Then:

- ARM_SHAM vs ARM_WAKE isolates the mode-transition / SHY / serotonin component.
- ARM_SLEEP vs ARM_SHAM isolates the offline consolidation content.

This is worth doing, but it is **not a clean "rest" control either**: SHY
normalisation lives inside `enter_sws_mode()`, so a sham arm still applies an E1
decay. A genuinely minimal rest control would call `enter_offline_mode()` /
`exit_offline_mode()` directly. Flagged, not resolved.

---

## 4. Recommended mechanism: the config flag, not a driver-level `force_cycle()`

The chip specifies `force_cycle()`. Having read both paths I recommend the
**newly-landed config flag** instead, and the reasoning is worth recording because
it is not the obvious answer.

| | **M1: driver calls `force_cycle()`** | **M2: `use_within_life_sleep_trigger=True`** |
|---|---|---|
| Driver change | **Requires forking `_observational_run()`** | **None** |
| Arms differ by | driver control flow | **exactly one config flag** |
| Schedule | arbitrary (incl. one-shot) | fixed cadence, every `within_life_step_ceiling` steps |
| Validated | V3-EXQ-909 (PASS, this family) | V3-EXQ-929 (PASS, structural) |

The decisive point is the first row. The 906-lineage deliberately imports
`_observational_run()` **UNCHANGED** (920's docstring stresses this), and there is
no injection hook in its `for step_idx in range(steps_per_episode)` loop. M1 would
require a driver-local fork of a ~200-line shared function whose continuity
semantics the whole lineage depends on -- a real regression risk for a
manipulation M2 delivers by flipping one flag. M2 also gives **maximal arm
matching**: the OFF arm makes no new call at all, which is precisely what 929's
`c1_off_silent` criterion pinned.

**Both are experimenter-triggered.** M2's ceiling arm hardcodes
`need_crossed = False`, so it is a step counter, not a need signal. Choosing M2
buys implementation safety, **not** ecological validity, and must not be written
up as if it did.

**Use M1 if and only if** the design needs a *one-shot* or irregular schedule
(e.g. "one night of sleep at step T"), which M2 cannot express -- its trigger
re-arms every `within_life_step_ceiling` steps. For the deprivation question
(Section 6) a repeated cadence is the *scientifically correct* contrast anyway, so
M2 is preferred on the merits and not merely on cost.

---

## 5. Labelling discipline (chip item 4) -- binding on any write-up

Whichever mechanism is used, the manipulation is an **EXPERIMENTER-TRIGGERED
CAUSAL CONTROL**, not endogenous sleep onset.

**Required wording**, in the driver docstring, the manifest `interpretation.note`,
and any downstream synthesis:

> Sleep cycles in ARM_SLEEP are inserted on a fixed experimenter-configured
> schedule. REE does not detect fatigue, accumulate a sleep need, or select sleep.
> The v1 GAP-9 trigger is a step counter (`need_crossed` is hardcoded `False`); the
> MEL/need-crossing arm is not wired.

**Forbidden**: any phrasing in which REE "chose", "decided", "needed", "wanted",
or "became tired enough" to sleep; any use of "sleep deprivation" without the
qualifier "experimenter-scheduled"; any claim that this run bears on *when* an
organism should sleep. The title of this document says "sleep deprivation" as
shorthand for the contrast; the experiment tests **absence of a scheduled offline
pass**, which is a strictly narrower thing.

---

## 6. The design

### 6.1 Structure

Base: a new driver in the 920 lineage, reusing `_make_config`,
`_env_config_snapshot`, `_observational_run`, `TRAIN_TOTAL_EPS`, `CORE_CHANNELS`,
`STD_FLOOR` from `v3_exq_906b_full_stack_observational_fishtank` and 920's
`EVAL_EPISODES=1` + `max_episode_steps=EVAL_STEPS` single-life eval, **all
unmodified**.

Per seed, **two complete lives** from an identical starting point:

| Arm | Config delta | Expected sleep cycles |
|---|---|---|
| `ARM_WAKE` | none (baseline 906b/920 config) | **0** |
| `ARM_SLEEP` | `use_within_life_sleep_trigger=True`, `within_life_sleep_step_ceiling=T` [^cfgfield] | `floor(life_length / T)` |

[^cfgfield]: The **config** field carries the `sleep_` infix; bare
`within_life_step_ceiling` is only the `SleepLoopManager` **constructor kwarg** it is
read into (`ree-v3/ree_core/agent.py:2832-2834`:
`within_life_step_ceiling=int(getattr(config, "within_life_sleep_step_ceiling", 1000))`).
`REEConfig` swallows unknown kwargs, so the constructor spelling silently no-ops back to
the default ceiling of 1000 -- against 920a's measured life lengths that is zero or one
cycle on half the seeds, i.e. a green run testing nothing (Section 9's hazard).
V3-EXQ-929 sets `within_life_sleep_step_ceiling=STEP_CEILING`.

Training is **shared**: run the curriculum once per seed, then deep-copy (or
re-instantiate from an identical seeded state) so both arms enter their life with
**bit-identical weights**. Do not train twice -- that introduces a divergence the
manipulation does not control.

### 6.2 Matching requirements (the part most likely to be got wrong)

1. **Identical seed, identical env kwargs, identical training.** Arms differ by
   the one flag and nothing else.
2. **Arm-independent environment RNG.** After the first sleep cycle the arms' RNG
   streams necessarily diverge (the sleep passes consume RNG). That is inherent to
   the manipulation, but it means env-side stochasticity (spawn position, drift,
   scheduled hazards) would *also* diverge, mixing a nuisance factor into the
   contrast. **Mitigation, with precedent in this lineage:** V3-EXQ-921 solved the
   identical problem with a shared arm-independent `_spawn_order_for_segment(seed,
   segment_index)` stream. Do the same here -- drive env stochasticity from a
   dedicated `random.Random(seed)` / `np.random.Generator` that the sleep passes
   cannot touch. **This is a hard requirement, not a nicety.**
3. **Pin the machine.** `torch.multinomial` returns different categories on
   `linux-x86_64` vs `darwin-arm64` from bit-identical inputs (CLAUDE.md, "Running
   the test suite"). Both arms must run in the same process on the same box;
   record `machine_class` in the manifest (920's `write_flat_manifest` already
   does).
4. **Assert the manipulation actually happened.** Record
   `total_sleep_cycles_fired` per arm and make it a **load-bearing precondition**:
   `ARM_WAKE == 0` and `ARM_SLEEP >= 2`. This is the direct guard against the
   silent-no-op failure in Section 2.1 -- and it is cheap, since 920 already
   computes `sleep_cycles_fired` from `sleep_loop._cycle_history` length.

### 6.3 Analysis window

Both arms run to the same total step budget or to `health_depleted`, whichever
first. Compare on:

- **matched-prefix window** (steps `0..T`): must be statistically indistinguishable
  -- a *negative control* confirming the arms really were matched before the first
  cycle. If they differ here, the matching is broken and the run is void.
- **post-first-cycle window** (steps `T..end`): where the causal contrast lives.

---

## 7. Dependent variables -- **PROVISIONAL** (chip item 3)

**This section is explicitly a placeholder.** The chip specifies that the DV set
should be inherited from
`chip-20260812-exq920-multiseed-degradation-retrospective`'s measure selection.
That chip is **still `open`** (verified in `TASK_CHIPS.json`, `resolution_note:
None`), so the measures below are proposed **from V3-EXQ-920's own logged
channels** and are to be **replaced, not merely supplemented**, once the
retrospective lands. This is a follow-on to that analysis's measure selection, not
an independent invention of new metrics.

Available per-step from `_observational_run`'s `ep_steps` record: `harm_signal`,
`z_harm_s/un/a`, `z_world_norm`, `z_self_norm`, `z_beta_val`,
`world_change_norm`, `drive`, `z_goal`, `vigor`, `override`, `z_block`, `freeze`,
`excite`, `dread`, `surprise`, `residue_wanting`, `liking`, `mode`,
`transition_type`, `health`, `pos`, `action`.

Provisional DVs, mapped to the chip's four named families:

| Family | Provisional measure | Source |
|---|---|---|
| Prediction / model error | mean `surprise`; `world_change_norm` drift over the life | per-step log |
| Action-run coherence | mode-run-length distribution; **waking mode entropy (bits)** | `mode`; 909 used `mean_waking_mode_entropy_bits` |
| Hippocampal familiarity growth | residue `active_centers` / `total_residue` trajectory | 920 logs `seed0_residue_active_centers_final`, `..._total_residue_final` |
| `z_goal` / `residue_wanting` trajectory | mean and slope of `z_goal`, `residue_wanting` over the life | per-step log |
| **Organism-level (headline)** | **survival time to `health_depleted`** | 920's `realized_steps` + `done_cause` |

**Do NOT use `vigor`.** It is degenerate in this family: V3-EXQ-920 measured
`chan_max_std_vigor = 0.0` and its own `channel_vigor` criterion **failed**. Any
DV built on it is guaranteed null for reasons unrelated to sleep.

**Expect small effects.** V3-EXQ-909, the only run to characterise sleep-cycle
*content* here, found it near-degenerate: `replay_diversity_index` pinned at
exactly `0.02` (= 1 distinct region / 50 draws) and `sws_slot_diversity` between
`1.1e-5` and `9.2e-4`. It passed a deliberately weak "non-null" bar. A design
powered for a large behavioural effect will be disappointed; power accordingly
(Section 8) and pre-register a null as informative.

---

## 8. Pre-registration sketch

**Preconditions (load-bearing, all must hold or the run is void):**

1. `harm_pathway_trained` >= 1 optimizer step (inherit 920's).
2. `ARM_WAKE` `total_sleep_cycles_fired == 0`.
3. `ARM_SLEEP` `total_sleep_cycles_fired >= 2` per seed.
4. `sws_n_writes >= 1` and `rem_n_rollouts >= 1` on every ARM_SLEEP firing
   (inherit 909's mechanism-engaged checks -- guards a *nominal* cycle that wrote
   nothing).
5. Matched-prefix negative control: no DV differs between arms over steps `0..T`.
6. Both arms complete for every seed (no silent `n` shrinkage -- 920's own
   `all_seeds_completed`).

**Primary criterion:** a pre-registered directional difference on the DV set
adopted from the retrospective, over the post-first-cycle window, across seeds.

**Seeds:** >= 8, paired (each seed contributes one ARM_WAKE and one ARM_SLEEP
life). Paired analysis, since the arms share training and seed. **Note the base
run's own weakness here: V3-EXQ-920 FAILED with `n_seeds = 1`** (one life, 1475
steps, genuine `health_depleted`) -- it never reached its own
`MIN_UNCENSORED_DEATHS_TOTAL = 4`. Building on an unreplicated base is precisely
what Section 9 gates on.

**A null is publishable and expected to be informative**: given Section 7's
effect-size evidence, "experimenter-scheduled SD-017 sleep has no detectable
within-life functional effect in this config" is a real result and would route
straight to the question of whether the Phase B-E cluster (all OFF here) is what
carries the effect.

**Cost estimate:** V3-EXQ-920 took **929 s** for a single 1475-step life on
`ree-worker-1`. Two arms x 8 seeds, at a longer per-life budget, is plausibly
6-15 h of cloud compute. Not free -- another reason not to queue it uncalibrated.

---

## 9. Why this is NOT queued (chip item 6)

The chip instructs: queue if concrete enough, otherwise leave a scoped design doc
and name the dependency. **Two constants are genuinely gated**, and both are
`puzzle (known rules)` -- a missing fact, obtainable, not requiring a reframe.

1. **The sleep cadence `T` (`within_life_step_ceiling`) is uncalibrated.** It must
   be short enough that several cycles fire within a life and long enough that the
   contrast is a *deprivation* contrast rather than a near-continuous-sleep one.
   Setting it requires the within-life survival distribution. The only true
   single-life datum in existence is **n = 1**: V3-EXQ-920 seed 0, dead at 1475
   steps. With n = 1 there is no distribution, and a `T` chosen from it could
   trivially land past the median death time -- producing an ARM_SLEEP that never
   sleeps and an experiment that looks green while testing nothing.
2. **The DV set is, by the chip's own construction, inherited from the
   retrospective** (Section 7), which is `open`.

**Both unblock on the same artifact:**
`chip-20260812-exq920-multiseed-degradation-retrospective` (multi-seed 920
successor + within-life degradation retrospective). It supplies the survival
distribution that calibrates `T` *and* the measure selection that fixes the DVs.

Everything else is settled: mechanism verified (Section 2), confound scoped
(Section 3), implementation route chosen (Section 4), matching requirements
specified (Section 6.2), pre-registration drafted (Section 8). Once the
retrospective lands, this should be queueable via `/queue-experiment` mechanically
-- fill in `T` and the DV list, write the driver, smoke-test, queue.

**Explicitly NOT a reason to delay:** GAP-9. It is closed and validated. The
original chip's "we don't need to wait for GAP-9" reasoning has been overtaken by
GAP-9 simply landing.

---

## 10. Follow-on this design surfaces (not actioned here)

- **The need-arm successor.** Once GAP-9's MEL/need-crossing arm is wired, the
  identical design becomes a genuinely *endogenous* sleep test, and the Section 5
  labelling restriction relaxes. That is the scientifically more interesting
  version and it is one substrate step away.
- **ARM_SHAM** (Section 3.1) to dissociate rest from consolidation.
- **Cluster-enabled replication.** Everything in Section 3's table is OFF here;
  909 showed the cluster is reachable in this family with three added flags. A
  cluster-on arm asks whether the aggregation machinery is what carries any effect.
