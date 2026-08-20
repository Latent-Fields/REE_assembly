---
title: "Matched-arm causal design: experimenter-triggered sleep vs continued wake in a single continuous life"
registered: 2026-08-14
status: design-staged (NOT queued -- Section 9 constants RESOLVED 2026-08-18; blocked on the
  open `corrupting` substrate defect contextmemory-write-path-addressing-degeneracy per Section
  11; fix LANDED 2026-08-19 but status is implemented_pending_validation, which
  /queue-experiment Step 2.5c treats as still OPEN -- gate remains closed, see Section 12)
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

> **UPDATE 2026-08-18 -- READ SECTION 11 BEFORE SECTION 9.** Section 9's two gated
> constants are now RESOLVED (`T = 400`; DV set fixed from the V3-EXQ-920a N=8
> retrospective). Queuing is nonetheless **blocked**, on a different and unrelated
> gate: an open **`corrupting`** substrate defect
> (`contextmemory-write-path-addressing-degeneracy`) sits on
> `ContextMemory.write()`, which is the target of the SWS schema pass that
> constitutes half of ARM_SLEEP's manipulation. Under that defect a null result
> from this design is **uninterpretable**. Sections 2, 6.1, 6.2, 6.3 and 8 also
> carry corrections in Section 11.4-11.6. Sections 1-10 are left unedited so the
> revision is auditable.

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

---

## 11. Queue attempt 2026-08-18: the two gated constants are RESOLVED, but a DIFFERENT gate now blocks

**Appended by** `chip-20260814-queue-causal-sleep-matched-arm` (session
`metaworker-chip-20260814-queue-causal-sleep-matched-arm`, headless on `ree-cloud-5`),
2026-08-18T18:19Z. Sections 1-10 are left standing so the revision is auditable.

**Status change: `design-staged (two calibration constants gated)` -> `design-staged
(constants RESOLVED; blocked on a substrate defect)`.** Section 9's gate is OPEN. A new,
unrelated one is CLOSED. This run was **not queued**, and no script was written.

### 11.1 Section 9's gate is discharged -- both constants are now fixed

`chip-20260812-exq920-multiseed-degradation-retrospective` resolved `done` 2026-08-14T16:21Z.
Its Section 7 (N=8, V3-EXQ-920a) supplies both missing constants. Section 5 of that document
carries a superseding block dated 2026-08-18; **its revised bullets govern, not the n=1 ones
above them.**

- **Sleep cadence `T` = 400** (`within_life_sleep_step_ceiling=400`), absolute, NOT per-seed.
  The n=1 recommendation to set `T` relative to each seed's own exhaustion point is explicitly
  **withdrawn**: the pre-registered resource-exhaustion boundary fires in **0/8** seeds, and the
  energy ramp is bit-identical across seeds (0.0015/step, reaching 0 at t=666), so "each seed's
  own boundary" is the same absolute step everywhere. At t=400 median energy is 0.398, median
  `z_goal` has already fallen 0.366 -> 0.063, and **8/8 seeds are still alive** (shortest life
  628 steps, ~228 steps of margin).
- **DV set (revised).** Primary: `surprise` (proxy); `z_block` **promoted** to primary, recorded
  with `action_blocked`; mode-run length / mode-switch rate **and** dominant-mode identity.
  Secondary: `liking`; cumulative-distinct-cells + revisit rate (**downgraded** -- new-cell
  acquisition stops mid-life in 5/8 seeds). `z_goal` **manipulation-check only, never an outcome**
  (`r(z_goal, energy) = 0.9235` to 4 dp in 7/8 seeds). Mandatory covariates: `energy`,
  resource count, **and `health`** (health is the only state variable that genuinely diverges
  across seeds: 0.04 .. 0.85 at t=600). Headline organism-level DV: survival time to
  `health_depleted`.
- **Dropped from Section 7's provisional set:** `excite` (`r(surprise, excite) = 0.985 .. 1.0000`
  -- the same signal), `drive` (definitionally `1 - energy`, `ree-v3/ree_core/agent.py:10951`),
  `residue_wanting` (0.0 in 8/8 -- the 916a recording gap, not a measured null),
  `orienting_active` (0 fires in 8/8), `is_committed` (False at all 13718 steps).
  **`vigor` stays excluded** as Section 7 required (0.0 in 7/8, max 0.026 in seed 5).

### 11.2 THE BLOCKER: an open `corrupting` substrate defect on this experiment's own mechanism

`/queue-experiment` **Step 2.5c** (substrate-path overlap gate) fires a mandatory stop:

> `contextmemory-write-path-addressing-degeneracy` -- severity **`corrupting`**,
> `status: pending_implementation`, `ready: true`, `substrate_paths: ["ree_core/predictors/e1_deep.py"]`,
> `unblocks_claims: ["SD-017", "ARC-045", "MECH-166"]`.

**The overlap was verified in code, not taken from the path list.** `ContextMemory` is defined at
`ree_core/predictors/e1_deep.py:36`. Its `read()` addresses by `F.softmax` over projected scores;
its `write()` (lines ~135-147) addresses by a hard `scores.mean(0).argmin()` under `torch.no_grad()`,
which under a near-constant query stream is a deterministic single-slot fixed point.
`agent.run_sws_schema_pass` (`ree_core/agent.py` ~11231) is **the MECH-166 slot-formation phase** and
its own docstring states it writes "directly to ContextMemory bypassing the offline gate".

That pass is **half of this experiment's entire manipulation.** Section 3's table shows Phase B/C/D/E,
MECH-204, MECH-423 and the MEL consumer are ALL OFF in the 906b/920 config, so a forced cycle here is
exactly (1) the SWS schema pass into ContextMemory and (2) the REM attribution rollouts. ARM_SLEEP
therefore drives the defective write path on every fire.

**Why this is disqualifying rather than a caveat -- the defect's own severity rationale describes
this run's most likely result, verbatim:**

> "Every ContextMemory consumer writing under a low-variance query stream silently gets a 1-slot bank
> while write() returns normally and thousands of calls are logged. Nothing errors, the readout is
> well-formed, and **the resulting null looks like a genuine 'sleep has no effect' finding.** That is
> the definition of `corrupting` -- evidence that LOOKS valid but is not -- and it has now produced
> exactly that artefact twice (436e, 436f)."

Section 8 pre-registers a null as informative and expected. Under this defect a null is
**uninterpretable**: "experimenter-scheduled SD-017 sleep has no within-life functional effect" and
"the SWS write path collapsed to one slot" are indistinguishable in the manifest. That would spend the
Section 8 cost estimate (~6-15 h of cloud compute) to produce the third instance of an artefact that
has already been produced twice.

**A retrospective reading this design should also re-examine on its own evidence.** Section 7 cites
V3-EXQ-909's near-degenerate sleep content -- `sws_slot_diversity` between 1.1e-5 and 9.2e-4,
`replay_diversity_index` pinned at exactly 0.02 (= 1 distinct region / 50 draws) -- as grounds to
"expect small effects" and to power accordingly. A near-zero slot diversity is precisely the
1-of-16-slots fixed point this defect predicts. **Section 7's "expect small effects" may therefore be
a readout of the defect rather than a fact about sleep**, which would mean the design is currently
powered against a number the fix could move. Re-derive it after the fix; do not carry it forward
unexamined.

**This is not a lone reading.** `chip-20260818-sd017-ceiling-retest-gated` (open) already gates a
sibling SD-017 retest on the same fix, and the build itself is owned by
`chip-20260816-implsub-contextmemory-writepath-degeneracy` (open, `/implement-substrate`).
**No new chip was spawned for the build** -- it is already owned, and duplicating it is the
documented "spawned then immediately withdrawn" antipattern.

### 11.3 The second overlap, which is NOT a blocker (recorded so it is not re-litigated)

Step 2.5c also matches `SD-SLEEP-ENTRY-PRESSURE` (severity **`degrading`**), whose
`substrate_paths` include `ree_core/sleep/phase_manager.py::notify_waking_step` -- the exact
function Section 4's recommended M2 mechanism uses. It does **not** block, and its own
`severity_reasoning` says why: the defect is "reachable ONLY behind `use_mel_entry`, which is
default-off". This design uses the **ceiling arm with no MEL consumer** (Section 3's table:
`mel_consumer is None`), and `notify_waking_step` computes `need_crossed = self.mel_consumer is not
None and ...`, so the need arm is short-circuited and the broken entry-pressure statistic is never
read. Carry it as a queue-entry `note` when this is eventually queued, per Step 2.5c's degrading rule.

### 11.4 Substrate facts verified empirically this session (carry these into the driver)

Probed directly against the live substrate on `ree-cloud-5` (`linux-x86_64`, py3.10), scratch
scripts not committed. These supersede or sharpen several of Sections 2, 6.1 and 6.2.

1. **Config threading works, and the Section 6.1 footnote's hazard is real but avoidable.**
   Setting `cfg.use_within_life_sleep_trigger = True` and `cfg.within_life_sleep_step_ceiling = 400`
   post-construction on a `_make_config(env)` config reaches the manager:
   `agent.sleep_loop.within_life_trigger == True`, `.within_life_step_ceiling == 400`. `_make_config`'s
   `from_dims` path already exposes the attribute (default ceiling **1000**), so the footnote's
   silent-no-op-to-1000 failure is exactly what happens if the constructor spelling
   `within_life_step_ceiling` is used on the config instead of `within_life_sleep_step_ceiling`.
2. **`force_cycle()` returns a dict here, not `None`** -- Section 2.1's preconditions 1-3 hold in this
   config. **But on an untrained agent it returned `sws_n_writes = 0.0` and `rem_n_rollouts = 0.0`**,
   which confirms Section 8's precondition 4 (`sws_n_writes >= 1`, `rem_n_rollouts >= 1` on every
   firing) is a **live, non-vacuous guard**, not boilerplate. Keep it load-bearing.
3. **Section 6.2 requirement 2 (arm-independent env RNG) is satisfied STRUCTURALLY -- verified, not
   assumed.** `CausalGridWorldV2` draws from a dedicated per-env `self._rng =
   np.random.default_rng(seed)` (`causal_grid_world.py:1383`), and a `force_cycle()` left the env's
   `bit_generator.state` **bit-identical** across the call. So the manipulation itself cannot perturb
   env stochasticity, and the V3-EXQ-921 `_spawn_order_for_segment` retrofit Section 6.2 proposes is
   **not needed**: with `EVAL_EPISODES=1` there is exactly ONE spawn, at step 0, before any cycle can
   fire, so the spawn is identical across arms by construction. What remains is *behaviour-mediated*
   env divergence after the first cycle -- and that is the causal pathway under test, not a nuisance
   factor to engineer away.
4. **`copy.deepcopy(agent)` FAILS as Section 6.1 literally specifies it** --
   `TypeError: cannot pickle 'module' object`. Cause is a single attribute:
   `agent.hippocampal._rng` **is the stdlib `random` module itself**. Detaching that one attribute,
   deep-copying, and restoring it on both copies works and yields **bit-identical parameters AND
   buffers** with a distinct `sleep_loop` object. Because it is a shared global module, detach/restore
   loses nothing. **Prefer this to Section 6.1's "re-instantiate from an identical seeded state"
   alternative**: it halves the compute (one curriculum per seed, not two) and makes bit-identity a
   property of the copy rather than of training determinism. Train with the trigger **OFF in both
   arms**, deep-copy, then flip `use_within_life_sleep_trigger` / `within_life_sleep_step_ceiling` /
   `sleep_loop.state.steps_since_sleep = 0` on the ARM_SLEEP copy only -- so training is not merely
   matched but *untouched* relative to the 920 lineage.
5. **TRAP -- `_observational_run`'s `sleep_cycles_fired` does NOT count within-life cycles.** It
   diffs `sleep_loop._cycle_history` **once per episode, before the step loop**
   (`v3_exq_906b_...py` ~line 519). With `num_episodes=1` that check runs exactly once, at `ep_idx=0`,
   before any step executes. Every cycle `notify_waking_step` fires **inside** the step loop is
   therefore invisible to `ree["sleep_cycles_fired"]`, which will read **0 for ARM_SLEEP**. A driver
   that wires Section 6.2's requirement 4 to that field would fail its own load-bearing precondition
   on a correctly-working manipulation. **Count `len(agent.sleep_loop._cycle_history)` directly,
   before and after the eval life.**

### 11.5 Correction to Section 8's precondition 3, forced by the now-known survival distribution

Section 8 requires `ARM_SLEEP total_sleep_cycles_fired >= 2` **per seed**. Against 920a's measured
lives (628, 1008, 1432, 1816, 1846, 1944, 2517, 2527) at `T=400`, `floor(life/T)` gives
**1, 2, 3, 4, 4, 4, 6, 6** -- so **7/8 seeds reach >= 2 and seed 5 (628 steps) reaches only 1.**
The blanket per-seed `>= 2` is therefore unsatisfiable at the cadence the same gating artifact
selected. This is exactly the kind of design-time arithmetic `/queue-experiment` Step 3.5 requires be
done on paper before compute is spent. Replace with:

- **load-bearing:** `ARM_WAKE` cycles `== 0` in 8/8 seeds (the Section 2.1 silent-no-op guard);
- **load-bearing:** `ARM_SLEEP` cycles `>= 1` in **8/8** seeds (the manipulation genuinely happened);
- **load-bearing:** `ARM_SLEEP` cycles `>= 2` in **>= 6/8** seeds (the repeated-cadence contrast;
  920a predicts 7/8).

Do **not** resolve this by lowering `T`: `T` was selected on liveness and on `z_goal` having already
moved, and shortening it converts the design from a deprivation contrast toward a
near-continuous-sleep one (Section 9's own criterion).

### 11.6 A strengthening of Section 6.3's negative control, available for free

Section 6.3 asks that the matched-prefix window (`0..T`) be "statistically indistinguishable"
between arms. Given 11.4 items 3 and 4, it can be **bit-identical**, which is a far sharper control:
the agents are bit-identical copies, the env RNG is arm-independent, and `notify_waking_step` returns
`None` before consuming any randomness on every step until the ceiling is reached
(`need_crossed` short-circuits on `mel_consumer is None`). So steps `0..T-1` should agree exactly.
Assert exact per-step equality over the prefix as the load-bearing matching control and report the
statistical comparison alongside it; any divergence before step `T` is then a positive detection of
broken matching rather than a judgement call.

### 11.7 Resume condition

Queue this when `contextmemory-write-path-addressing-degeneracy` reaches
`implemented` / `implemented_validated` in `substrate_queue.json` (tracked by
`chip-20260816-implsub-contextmemory-writepath-degeneracy`). At that point Sections 1-8 plus 11.1
and 11.4-11.6 are sufficient to write the driver and queue it via `/queue-experiment` mechanically --
**and re-derive Section 7's "expect small effects" power expectation first (11.2), rather than
inheriting it.** No constants remain gated.

**Note for whoever queues it:** `/queue-experiment` **Step 8.6** (`POST /queue/add` to the
coordinator) **cannot be completed from a headless cloud box** -- `ree-cloud-5` has no
`REE_assembly/coordinator.env`, so no bearer token is obtainable and a git commit alone is NOT a
durable add. Queue this from the Mac, or hand off the `queue_id` + commit sha explicitly.

---

## 12. Queue attempt 2026-08-20: the fix landed, but the resume condition is STILL not met

**Appended by** `chip-20260814-queue-causal-sleep-matched-arm` (session
`metaworker-chip-20260814-queue-causal-sleep-matched-arm`, headless on `ree-cloud-4`),
2026-08-20T11:38Z. Sections 1-11 left standing so the revision is auditable. **Status change:
`blocked (defect open)` -> `blocked (defect fixed, validation owed)`. Still not queued.**

### 12.1 The fix landed

`chip-20260816-implsub-contextmemory-writepath-degeneracy` resolved `done` 2026-08-19T04:10:28Z.
`ree-v3` `76cbf844` ("e1: repair ContextMemory.write() deterministic single-slot fixed point") is
confirmed on `origin/main` (`git merge-base --is-ancestor` checked live this session). A second
mechanism, `692f8526d0` ("add default-off 'refractory' ContextMemory write-selection mode"),
landed the same window.

### 12.2 Why this does NOT satisfy Section 11.7's resume condition

Section 11.7 says: queue when the `substrate_queue.json` entry reaches `implemented` /
`implemented_validated`. Read live this session: the entry's `status` is
**`implemented_pending_validation`** -- a third state Section 11.7 did not anticipate. This is
not a technicality. `/queue-experiment` Step 2.5c states the rule explicitly and by name:

> A status of the form `implemented_pending_validation` (or any status containing `pending`) is
> still OPEN, never closed -- ... the substrate has landed and NOT yet been confirmed correct,
> which is exactly the window a corrupting defect is most likely to still be live in.

This design's own Section 4 mechanism (`use_within_life_sleep_trigger=True`) routes through
`agent.run_sws_schema_pass()` -> `ContextMemory.write()` in `ree_core/predictors/e1_deep.py` on
every ARM_SLEEP fire (Section 3 step 2) -- an exact match against the entry's
`substrate_paths: ["ree_core/predictors/e1_deep.py"]`. Re-ran Step 2.5c's overlap gate live this
session: the entry is still `corrupting` severity and still reads OPEN under the `pending`
override. **The mandatory stop-gate shape still applies: do not write the script, do not add a
queue entry.**

### 12.3 Both fix mechanisms are also DEFAULT-OFF -- opting in is not free either

Even setting the resume-condition question aside, neither fix self-applies. Both
`E1Config.contextmemory_write_usage_balancing` (bool, default `False`) and
`E1Config.contextmemory_write_selection` (default `"argmin"`, the legacy path) preserve
bit-identical legacy behaviour unless a driver explicitly opts in. The substrate_queue entry's
own `validation_experiment` field states plainly: "no driver in `ree-v3/experiments/` sets
either, so a driver written today runs the unfixed argmin path." A driver for this design
that did not explicitly set one of these flags would silently re-run into the exact corrupting
defect Section 11 stopped this design for -- opting in is not automatic and must be a deliberate,
documented choice in whichever future session writes the driver.

**Why this session does not just opt in unilaterally and proceed anyway.** The fix's own
system-level validation is not yet in evidence: `implementation_note` on the substrate_queue
entry states the two mechanisms are validated only at the `ContextMemory` unit level against a
*synthetic* degenerate query stream, "not yet with a queued EXQ measuring `n_occupied_slots` on
a real agent under the 436e/436f harness's own instrumentation." A dedicated chip for exactly
that validation experiment, `chip-20260819-queueexp-contextmemory-writesel-validation`, is
itself still `open` (and actively claimed by a concurrent session as of this check) -- i.e. the
question "does the fix actually work on a real agent" has an owner and is in flight, but has not
answered yet. Queuing this design's 6-15h compute run on an informal, self-supplied opt-in
(rather than on a fix the ecosystem has separately confirmed) would repeat the exact "looks
green, tests nothing" failure mode Section 11.2 quoted the defect's own severity rationale
about -- just one layer up, on the fix instead of the defect.

### 12.4 Resume condition, corrected

Section 11.7's condition is superseded by this one, which accounts for the pending/default-off
distinction Section 11.7 did not anticipate:

Queue this when **either**:
- (a) `contextmemory-write-path-addressing-degeneracy` reaches `implemented_validated` (not
  merely `implemented_pending_validation`) in `substrate_queue.json` -- i.e.
  `chip-20260819-queueexp-contextmemory-writesel-validation` lands and confirms the fix on a
  real agent, which also settles which of the two mechanisms (or their composition) to use and
  at what parameters; **or**
- (b) a future session makes a deliberate, documented decision to opt in early (citing this
  section), explicitly setting `contextmemory_write_selection="refractory"` (or the usage-
  balancing flag) in BOTH arms of the driver, and adds a load-bearing precondition asserting
  non-degenerate write-path behaviour in ARM_SLEEP (`n_occupied_slots >= 2` on `>= 3/5` seeds,
  matching the defect's own `failure_record` acceptance criterion, measured directly rather than
  assumed) -- so a collapsed write path self-routes to `substrate_not_ready_requeue` rather than
  masquerading as a null "sleep has no effect" finding.

Route (a) is preferred: it is order-independent of this design and reuses work already in
flight rather than duplicating it. Nothing else in Sections 1-11 changes; once either condition
is met, Sections 1-8 plus 11.1 and 11.4-11.6 remain sufficient to write the driver mechanically.
