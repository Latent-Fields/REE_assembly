# MECH-165 diagnosis: why EXQ-244a's reverse replay never fired (`reverse_replayed=0`)

**Date:** 2026-08-08
**Claim:** MECH-165 (offline replay must sample trajectory-diverse content -- forward + reverse + random -- to maintain multi-strategy viability)
**Trigger:** `/thought-digestion` pass on MECH-165 flagged that the one config-enabled validation run (V3-EXQ-244a, 2026-04-09) shows `reverse_replayed: 0` in every seed of every condition, and `FORWARD_REPLAY == NO_REPLAY` byte-for-byte, despite `exploration_buffer_size=50`. The claim's own `what_would_answer` NON-DEGENERACY PRECONDITION #1/#2 make diagnosing this a prerequisite before the claim can be tested at all.
**Session:** `metaworker-chip-20260808-mech165-reverse-replay-nonfiring` (headless).

---

## TL;DR

The mechanism is **not broken**. `HippocampalModule.diverse_replay()` / `reverse_replay()` are correct and, when called with valid inputs, reverse replay fires exactly as designed (verified: 11/25 reverse trajectories in `mode="auto"`, 5/5 in `mode="reverse"`).

The `reverse_replayed=0` and the `FORWARD_REPLAY==NO_REPLAY` byte-identity are **both** caused by a single **experiment-driver bug** (task option (c), not (a) a substrate logic bug and not (b) a substrate metrics gap):

> The EXQ-244a driver calls `agent.reset()` as a "final flush" at the end of Phase 1 (`experiments/v3_exq_244a_mech165_replay_diversity_validation.py:140`). `agent.reset()` clears the theta buffer (`agent.py:3060 -> self.theta_buffer.reset()`). The SWS consolidation loop then reads `recent = agent.theta_buffer.recent`, which is now **`None`**, and its `if recent is not None:` gate is False -- so **the entire replay block is skipped in all three conditions**. No forward replay, no reverse replay, no diverse replay is ever invoked.

Consequences, both observed in the manifest and both fully explained:
- **`FORWARD_REPLAY == NO_REPLAY` byte-for-byte:** with `recent is None`, `agent.hippocampal.replay(recent)` is never called in the FORWARD arm, so it does literally nothing that NO_REPLAY doesn't -> identical agent state -> identical Phase 2.
- **`reverse_replayed = 0` in all BALANCED seeds:** `agent.hippocampal.diverse_replay(recent, mode="auto")` is never called, so no `is_reverse` trajectory is ever produced or counted.

There is **also** a secondary, genuine **observability gap in the production replay path** (`_do_replay`), addressed by a narrow logging fix in this session (see §5).

---

## 1. Manifest re-confirmed accurate (2026-08-08)

`REE_assembly/evidence/experiments/v3_exq_244a_mech165_replay_diversity_validation_v3.json`:

| Condition | `exploration_buffer_size` | `reverse_replayed` (all 5 seeds) | Phase 2 vs NO_REPLAY |
|---|---|---|---|
| NO_REPLAY | 0 | 0 | -- |
| FORWARD_REPLAY | 0 | 0 | **byte-identical to NO_REPLAY** |
| BALANCED_REPLAY | 50 | 0 | differs (marginal) |

The manifest's own `evidence_quality_note` already self-flagged this as diagnostic-quality only. Every figure above still reads exactly as described in the trigger. Nothing has changed the manifest since 2026-04-09.

## 2. Substrate re-read (current `ree_core/hippocampal/module.py`)

`diverse_replay()` (module.py:2491), `reverse_replay()` (2408), `record_exploration_trajectory()` (2381), `_sample_exploration_trajectory()` (2466) are all present and correct. The `mode="auto"` branch:

```python
r = self._rng.random()
has_buffer = len(self._exploration_buffer) > 0
if r < self._reverse_fraction and has_buffer:   # 0.3
    step_mode = "reverse"
elif r < self._reverse_fraction + self._random_fraction:  # 0.5
    step_mode = "random"
else:
    step_mode = "forward"
if step_mode == "reverse" and len(self._exploration_buffer) > 0:
    source = self._sample_exploration_trajectory(retrieval_bias=retrieval_bias)
    if source is not None:
        trajectories.append(self.reverse_replay(source))   # is_reverse=True
else:
    trajectories.extend(self.replay(theta_buffer_recent, num_replay_steps=1, ...))
```

This is logically sound: with `_reverse_fraction=0.3` and a populated buffer, ~30% of per-step rolls select reverse. Over 5 SWS cycles x 5 steps = 25 rolls, `P(zero reverse) ~= 0.7^25 ~= 1e-4`. A landed run showing `reverse_replayed=0` in **all** seeds is therefore statistically impossible **if `diverse_replay` were actually being called** -- which is the first clue that it is not being called at all.

## 3. Root cause (driver bug), traced end to end

Driver `run_condition()` -> `run_phase1_exploration()` ends at line 139-140:

```python
    # Final flush
    agent.reset()
```

Then:

```python
    sws = run_sws_consolidation(agent, NUM_SWS_CYCLES, condition)
```

`run_sws_consolidation()` (driver line 151):

```python
    for _ in range(num_cycles):
        agent.enter_sws_mode()
        recent = agent.theta_buffer.recent          # <-- None: buffer was just cleared
        if recent is not None:                       # <-- False
            ...  # replay block NEVER entered
        agent.exit_sleep_mode()
```

- `agent.reset()` -> `agent.py:3060` -> `self.theta_buffer.reset()` clears `_z_world_buffer`.
- `ThetaBuffer.recent` (theta_buffer.py:121) returns `None` when `_z_world_buffer` is empty.
- `enter_sws_mode()` (agent.py:10660) does **not** repopulate the theta buffer -- it only gates waking writes, runs SHY normalisation, and sets the serotonin SWS state.

So `recent` is `None` for every SWS cycle in every condition, and the `if recent is not None:` guard skips all replay.

### Why FORWARD == NO_REPLAY byte-for-byte
Because the guard is skipped, the FORWARD arm's only extra work (`agent.hippocampal.replay(recent)`) never runs. FORWARD and NO_REPLAY therefore execute an identical code path from identical seeds, and the untrained-substrate Phase 2 (which collapses to a single action; `phase2_entropy ~= -1e-10` everywhere) is byte-identical.

### Why reverse_replayed == 0 in BALANCED
Same guard: `agent.hippocampal.diverse_replay(recent, mode="auto")` is never called, so no `is_reverse` trajectory is created or counted. The populated `exploration_buffer_size=50` is a red herring -- the buffer is filled during Phase 1 (`_record_exploration_action` / `_flush_exploration_episode`, gated on `replay_diversity_enabled`), but it is only *consumed* by `diverse_replay`, which never runs.

## 4. Empirical confirmation (this session)

Two scratchpad repros against the real substrate (`REEConfig.from_dims` + `REEAgent` + `CausalGridWorldV2`, matching the driver's construction):

**Repro 1 -- reproduce the manifest and isolate the cause.** Running the driver's Phase-1 tail (including the final `agent.reset()`) then its exact SWS loop for BALANCED:
```
[1] after final agent.reset(): exploration_buffer=15  theta_buffer.recent is None -> True
[2] SWS as driver runs it: diverse_replay called 0/5 cycles, reverse_replayed=0
[3] diverse_replay with VALID recent + buffer(15): reverse fired 11 of 25 trajs   <- mechanism works
[4] diverse_replay(mode='reverse'): 5/5 reverse
```
Lines [1]/[2] reproduce the manifest exactly and attribute it to `recent is None`. Lines [3]/[4] prove the mechanism is functional and observable the moment `diverse_replay` receives a valid `recent` tensor.

**Repro 2 -- the BALANCED Phase-1 divergence is an RNG artifact, not the mechanism.** BALANCED's Phase-1 action distribution differs slightly from NO/FORWARD in the manifest. With a **fixed** env seed (removing the unseeded OS-entropy env layout) and identical driver seeds:
```
FORWARD/NO (balanced=False): {0: 51, 1: 44, 2: 113, 3: 92}  buf=0
BALANCED   (balanced=True):  {0: 40, 1: 34, 2: 119, 3: 107} buf=11
identical action dist? False
```
The divergence survives a fixed env seed, so it is an **RNG-stream perturbation** introduced by the exploration-recording path being active only in the BALANCED arm (`replay_diversity_enabled=True` turns on `_record_exploration_action`/`_flush_exploration_episode`), which desyncs the shared RNG stream that `agent.act()` draws from. **This matters for interpretation:** BALANCED's marginal "PASS" (the manifest's own note: only 1/5 seeds a genuine win, 3/5 winning by ~1e-13) is a byproduct of this RNG desync, **not** of the replay-diversity mechanism -- which never fired. The reviewer's `evidence_quality_note` verdict ("diagnostic-quality only") is correct and, if anything, generous.

## 5. Fixes

### 5a. Substrate: NO logic change needed -- mechanism is correct
`diverse_replay` / `reverse_replay` are left unchanged. There is no probability check that is always false, no dead mode-selection branch, no config-wiring gap. The one config-enabled run simply never called the method.

### 5b. Substrate: narrow LOGGING fix (applied this session)
The claim's `what_would_answer` NON-DEGENERACY PRECONDITION **#4** requires the corrected re-run to drive consolidation through the **production** path (`agent.act[_with_split_obs] -> _do_replay -> hippocampal.diverse_replay`), not a hand-rolled in-episode proxy. But `_do_replay` (agent.py:9207) **invokes `diverse_replay` and discards the returned trajectories** -- it records no metric. So a production-path re-run currently has **no way to observe whether reverse replay fired**, which would leave PRECONDITION #1 (`reverse_replayed > 0` observable) unsatisfiable through the sanctioned path.

Fix (module.py, additive and RNG-neutral -- `diverse_replay` stays bit-identical; consumes no RNG, no control-flow change):
- `diverse_replay` now records a per-call tally `self._last_diverse_replay_diagnostics` (`{reverse, forward, random, total}`) and increments cumulative counters `self._diverse_replay_mode_counts` (`{reverse, forward, random, calls}`).
- Because the counter lives inside `diverse_replay`, it is updated **regardless of caller** -- a re-run routed through `_do_replay` can read `agent.hippocampal._diverse_replay_mode_counts["reverse"]` after the SWS phase without the driver having to hand-count `is_reverse`.

### 5c. Driver: NOT fixed here (belongs to `/queue-experiment`)
Per CLAUDE.md, any new/modified experiment script + queue entry must go through `/queue-experiment`. This session deliberately does **not** edit `experiments/v3_exq_244a_mech165_replay_diversity_validation.py`. The corrected driver (a new lettered iteration, e.g. EXQ-244b) must, at minimum:

1. **Not clear the theta buffer before SWS.** Either drop the "final flush" `agent.reset()` at end of Phase 1, or run the SWS/consolidation pass while the theta buffer still holds waking Phase-1 content, or explicitly re-populate `theta_buffer` before reading `recent`.
2. **Route through the production path** (`_do_replay`) per PRECONDITION #4, and read reverse-firing from `agent.hippocampal._diverse_replay_mode_counts["reverse"]` (now available -- see §5b) rather than a bespoke `is_reverse` count on directly-returned trajectories.
3. **Assert non-degeneracy in-run:** fail loudly if `reverse_replayed == 0` in every BALANCED seed, or if FORWARD == NO_REPLAY byte-for-byte -- the two conditions this run silently produced.
4. **Give FORWARD and BALANCED a genuine consolidation signal to differentiate on.** With an untrained substrate whose Phase 2 collapses to a single action (`phase2_entropy ~= 0` in 14/15 cells here), the entropy-retention readout has almost no dynamic range; the corrected design should ensure replay content can actually move Phase-2 behaviour (PRECONDITION #3: exploration-generated source material, not the dominant trajectory alone).

## 6. Status for a future `/queue-experiment` re-run

- **Mechanism believed fixed/observable:** YES. `diverse_replay`/`reverse_replay` were never broken; they are verified functional (§4) and now **observable through the production path** via the §5b counter.
- **What blocked the claim was the test harness, not the substrate** -- exactly what the claim's PRECONDITION #1/#2 anticipated ("a prerequisite defect to diagnose and fix before this claim can be tested at all").
- **This session does NOT re-queue.** A `/queue-experiment` session should author EXQ-244b per the §5c requirements. The claim's existing `what_would_answer` CONFIRMING/FALSIFYING criteria stand unchanged.
- **Note (separate, pre-existing):** `replay_diversity_enabled` still defaults `False` (config.py:2594). That is expected (backward-compat master switch); the corrected experiment sets it `True` for the BALANCED arm exactly as EXQ-244a already did.

---

*Repro scripts used for §4 are session-local (scratchpad) and not committed; the assertions above are reproducible by constructing a BALANCED-config `REEAgent`, running any short exploration phase, and comparing `theta_buffer.recent is None` before/after the driver's final `agent.reset()`.*
