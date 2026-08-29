---
title: "V3-EXQ-938 matched-arm causal sleep -- NOT QUEUED: blocked at /queue-experiment Step 2.5c on a corrupting ContextMemory write-path defect"
registered: 2026-08-18
status: queue-blocked (substrate gate); calibration constants RESOLVED and recorded here
chip_ref: chip-20260814-queue-causal-sleep-matched-arm
scope_claims: []
claim_ids: []
related:
  - causal_sleep_deprivation_matched_arm_design_2026-08-14.md (the design this would have executed)
  - within_life_functional_trend_920_lineage_2026-08-14.md (supplied the DV set + cadence guidance)
  - substrate_queue.json :: contextmemory-write-path-addressing-degeneracy (the blocker)
  - chip-20260816-implsub-contextmemory-writepath-degeneracy (the fix, already open)
  - V3-EXQ-920a (the n=8 survival distribution that calibrates T)
---

**Status: AWAITING USER REVIEW. Nothing in this file has been written to
`experiment_queue.json`, `claims.yaml`, the coordinator DB, or any other registry. No
experiment has been queued, and no driver script was written.**

---

## 0. Verdict in one paragraph

The gate this chip waited on (`chip-20260812-exq920-multiseed-degradation-retrospective`) is
**`done`**, and both constants it owed are now resolved (Section 2). But a **different and
later** gate now fires: `/queue-experiment` **Step 2.5c** (substrate-path overlap) finds an
open `severity: corrupting` substrate defect --
`contextmemory-write-path-addressing-degeneracy`, registered **2026-08-16**, two days *after*
the design was written -- squarely on the code path that carries this experiment's primary
manipulation. Step 2.5c's disposition for `corrupting` is a hard stop: do not write the
script, do not add a queue entry. **The stop is not a technicality.** The defect's own
`severity_rationale` describes this experiment's expected result almost verbatim: *"the
resulting null looks like a genuine 'sleep has no effect' finding."* The design (Section 8)
pre-registers exactly that null as informative. Running it now would manufacture the
artefact the defect is registered to prevent, for a third time.

---

## 1. Why the block is real, not incidental overlap

Step 2.5c blocks on module-level overlap. This is tighter than that -- it is function-level,
and it lands on the manipulation itself.

**The defect** (`ree_core/predictors/e1_deep.py`, `ContextMemory.write`, read directly):

```python
with torch.no_grad():
    query = self.query_proj(state)
    scores = torch.mm(query, self.memory.t())
    min_idx = scores.mean(0).argmin()          # <-- hard argmin
    self.memory.data[min_idx] = (0.9 * self.memory.data[min_idx] + 0.1 * write_signal.mean(0))
```

A hard `argmin` under a low-variance query stream is a deterministic single-slot fixed point:
every write lands in the same slot, `write()` returns normally, and thousands of calls are
logged. `read()` on the same class addresses by softmax and is fine -- the asymmetry is the bug.

**The path into it from this experiment.** Per the design Section 3, with the Phase B-E
cluster all OFF, the ARM_SLEEP manipulation reduces to SHY normalisation + serotonin
transitions + `run_sws_schema_pass` + `run_rem_attribution_pass`. The SWS pass **is** the
consolidation content, and it writes straight through the defect:

```
REEAgent.run_sws_schema_pass   (ree_core/agent.py:11225)
  -> self.e1.context_memory.write(e1_input)   (ree_core/agent.py:11440)
     -> ContextMemory.write                   (ree_core/predictors/e1_deep.py:135-147)
```

So the defect does not merely sit somewhere in the import graph. It is on the write path of
the single component whose causal effect this experiment exists to measure.

**Corroboration -- the fingerprint is already visible in this exact lineage.** V3-EXQ-909
(`v3_exq_909_sleep_dv_fishtank_multifiring`, PASS, the same 906b fishtank family, 3 seeds x
15 firings) logged `mean_sws_n_writes = 5.0` per firing -- ~225 writes -- yet:

| metric | value |
|---|---|
| `sws_slot_diversity_min` | 1.1426e-05 |
| `sws_slot_diversity_median` | 7.019e-05 |
| `sws_slot_diversity_max` | 9.2125e-04 |
| `replay_diversity_index` (min=mean=max) | 0.02 (= 1 distinct region / 50 draws) |

Hundreds of writes leaving the slot bank essentially undifferentiated is the single-slot
fixed point, not a small effect. The design's Section 7 read these same numbers as *"expect
small effects ... pre-register a null as informative"*. **That reading is superseded**: the
near-degeneracy now has a named, registered, `corrupting` cause. Note also that the defect's
`unblocks_claims` is `["SD-017", "ARC-045", "MECH-166"]`, and **SD-017 is precisely the sleep
core this experiment tests**.

**The fix is already owned -- do NOT spawn a duplicate.**
`chip-20260816-implsub-contextmemory-writepath-degeneracy` (`/implement-substrate`) is
**open** in `TASK_CHIPS.json`. The substrate entry is `ready: true`, `priority: 1`,
`node_class: complicated (buildable)` with a concrete implementation hint (apply the annealed
Gumbel-softmax selection V3-EXQ-908 already confirmed works, to the *write* address; or add an
occupancy-balancing term). No spike is owed.

---

## 2. The two gated constants -- RESOLVED (so the next session does not re-derive them)

The chip's substantive work was to fill in the design's two placeholders. Both are now
settled from V3-EXQ-920a. **Recording them here is the point of this document**: they cost
real analysis, and they are independent of the blocker.

### 2a. Sleep cadence T = 250 (`within_life_sleep_step_ceiling`)

**V3-EXQ-920a landed 2026-08-14T22:34Z, outcome PASS, n=8, all 8 uncensored
`health_depleted` deaths** (`v3_exq_920_uncensored_survival_single_life_fishtank_20260814T223432Z_v3`).
This is the survival distribution the design's Section 9 gated on:

| seed | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| life (steps) | 1944 | 1432 | 1846 | 1008 | 2527 | **628** | 2517 | 1816 |

min 628 | median 1831 | mean 1714.75 | max 2527.

**The binding constraint is design Section 8 precondition 3** (`ARM_SLEEP >= 2 cycles per
seed`). With a fixed cadence the fire count is `floor(life / T)`, so `T <= min_life / 2 = 314`.

| T | fires per seed (using the lives above) | verdict |
|---|---|---|
| 400 | 4,3,4,2,6,**1**,6,4 | **FAILS** -- seed 5 fires once |
| 300 | 6,4,6,3,8,**2**,8,6 | passes, but seed 5 needs >=600 of its 628 steps -- ~4% margin |
| **250** | 7,5,7,4,10,**2**,10,7 | **chosen** -- seed 5 needs >=500 of 628 |

T = 250 is the **largest** cadence (so: longest matched-prefix control window, fewest cycles,
most deprivation-like contrast) that still guarantees >=2 fires for the shortest observed life
with real margin. It also places the first fire at t=250, inside the pre-morbid window for
every seed -- earliest `health < 0.5` across the eight seeds is t=403, and energy first
reaches 0 at t=666 in 7 of 8.

**Deviation from the retrospective's stated guidance, and why.** The retrospective proposed
`T ~= 350-450` and said to set T per-seed relative to each seed's **resource-exhaustion**
point. Both parts were premised on its n=1 trajectory (original 920 seed 0: resources 5->0
sustained from t~=555 of 1475). **Neither survives the n=8 data:**

- `T = 350-450` is arithmetically incompatible with precondition 3 (the 400 row above).
- **Resource exhaustion does not occur in 6 of 8 of 920a's seeds.** Measured from the
  920a episode log: seed 0 still holds 1 resource at t=1924 of 1944; seed 2 holds 2 at
  t=1827 of 1846. The regime marker the per-seed rule is defined against is simply absent,
  so "T relative to each seed's own exhaustion point" has no referent for most seeds.

The retrospective itself instructed that T be re-derived against the multi-seed distribution;
that is what this is. A single global T is additionally preferable here because design Section
6.2 requires a fresh arm-independent env stream, so per-seed constants transcribed from a
*different* run's idiosyncratic trajectory would not transfer cleanly anyway.

### 2b. Primary DV set (replaces design Section 7's provisional table)

From the retrospective's Section 5 measure selection, verbatim in content:

| family | measure | note |
|---|---|---|
| prediction error | `surprise` (proxy) | NOT E1/E2/E3 internal uncertainty -- do not relabel |
| affect | `excite` | co-moves with `surprise` |
| acute impairment | `z_block` | the transient/acute marker, not a monotone trend |
| familiarity | cumulative distinct cells visited + revisit rate | exhaustion-robust; **NOT** raw `footprint_at_cell` |
| coherence | mode-run length + mode-switch rate | `is_committed` is False at every step in this design |
| homeostatic (covariate-conditioned) | `z_goal`, `drive` | **only** with resource count + energy recorded alongside as covariates |
| headline (organism) | survival time to `health_depleted` | `realized_steps` + `done_cause` |

**Excluded as structurally dead in this lineage** (not "measured zero"): `residue_wanting`
(the 916a recording gap -- `benefit_exposure` is structurally 0 across the whole
664/906/909/911/912/913 lineage), `vigor`, `orienting_active`. The chip's instruction to keep
`vigor` excluded is correct and is independently confirmed by 920a's own
`chan_max_std_vigor = 0.0023` and `chan_mean_vigor = 2.6e-05`.

Note `benefit_exposure` is **not** in the per-step episode-log schema; the retrospective's
"`benefit_exposure`-proxy (or resource count)" is the usable form -- resource count and
energy are both logged per step.

---

## 3. Three implementation findings that outlive the block

These were established while preparing the driver and are recorded so the eventual session
does not rediscover them.

**(a) The design doc names the wrong config field. This one would have silently no-opped.**
Design Section 6.1 gives the ARM_SLEEP delta as `within_life_step_ceiling=T`. The actual
`REEConfig` attribute is **`within_life_sleep_step_ceiling`**:

```python
# ree_core/agent.py:2829-2834
within_life_trigger  = bool(getattr(config, "use_within_life_sleep_trigger", False)),
within_life_step_ceiling = int(getattr(config, "within_life_sleep_step_ceiling", 1000)),
```

`within_life_step_ceiling` is only the `SleepLoopManager` **constructor kwarg**. Setting the
doc's name on the config is read by nothing and falls back to the default **1000** -- at which,
against the 920a lives, seed 5 fires **zero** cycles and three more seeds fire one. The run
would have looked green while testing nothing, which is the precise hazard design Section 9
warns about. (This is the `from_dims`-swallows-unknown-kwargs failure mode; V3-EXQ-929 guards
it by asserting `agent.sleep_loop.within_life_trigger` / `.within_life_step_ceiling` after
construction, and the eventual driver should do the same for both arms.)

**(b) Design 6.2's "hard requirement" is already satisfied by the substrate.** The requirement
is an arm-independent env RNG stream. `CausalGridWorldV2` already owns its randomness --
`self._rng = np.random.default_rng(seed)` (line 1383) and `self._traj_pair_rng` (1217) -- and
a scan of the module finds **no** global `random.` / `np.random.` and **no** torch RNG use in
the env at all. The sleep passes consume torch/global RNG and therefore cannot perturb env
draws. No 921-style `_spawn_order_for_segment` shim is needed. Two residuals worth recording:
`_observational_run` has one global `random.randint` fallback (906b line 576) when
`select_action` returns None, whose firing count should be recorded; and post-first-cycle
policy divergence is inherent to the manipulation, as 6.2 itself states.

**(c) The matched-prefix control is stronger than "statistically indistinguishable".** Before
t=T the ARM_SLEEP agent's only extra work is `notify_waking_step` incrementing a counter and
returning `None` -- no RNG, no state change. With shared training and per-arm re-seeding the
arms should be **bit-identical** over `0..T-1`, so the negative control can be an
action-agreement assertion rather than a distributional test. Two prerequisites: the global
RNG (`torch`/`random`/`numpy`) **must** be re-seeded identically immediately before each arm's
eval, or the prefix will not match at all; and `sleep_loop_episodes_K` should be set huge on
**both** arms, because `agent.reset()` calls `notify_episode_end()` at `ep_idx == 0` and
ARM_WAKE's zero-cycle precondition should be structural rather than lucky.

Also: `_observational_run`'s own `sleep_cycles_fired` counter compares `_cycle_history` length
only at segment boundaries, so with `num_episodes=1` it **cannot see within-life fires**. The
driver must count them itself from `agent.sleep_loop._cycle_history` around the call, and read
`within_life_trigger_arm_ceiling`, `sws_n_writes`, `rem_n_rollouts` per fire for design Section
8 preconditions 3 and 4.

---

## 4. What was NOT done, explicitly

- No driver script written (Step 2.5c stops before Step 3).
- No queue entry appended; `experiment_queue.json` untouched. V3-EXQ-938 is **not** minted --
  the next available id at the time of writing was 938 (max in history: V3-EXQ-937a), and it
  should be re-derived at queue time, not assumed from this document.
- No `POST /queue/add`; nothing in the coordinator DB.
- No `substrate_queue.json` / `claims.yaml` / design-doc edits. In particular the design
  doc's wrong config field (Section 3a above) is **reported, not patched** -- amending a
  landed design artifact is governance's call, not this chip's.

## 5. Resume condition

Queue this experiment when `contextmemory-write-path-addressing-degeneracy` reaches
`implemented` / `validated` (tracked by `chip-20260816-implsub-contextmemory-writepath-degeneracy`).
At that point Sections 2 and 3 above are directly consumable: T = 250, the DV set as listed,
the corrected config field name, and the three implementation findings. Re-run Step 2.5c
first -- the substrate may have moved again -- and re-derive the queue id.

A reviewer who disagrees that the block should hold has one coherent alternative: run it as an
explicitly **instrument-limited** diagnostic whose pre-registration states that a null is
**uninterpretable** (rather than informative) until the write-path defect is fixed. That is a
real option, but it forfeits the design's headline result and should be a deliberate user
decision, not a default.

---

# ADDENDUM 2026-08-29T17:52Z -- gate re-checked, STILL BLOCKED (user-ratified hold)

Chip `chip-20260814-queue-causal-sleep-matched-arm` was picked up again on 2026-08-29 and
Section 5's resume condition re-tested. **The block holds. Nothing was queued; no driver was
written.** Recording the re-check so the next session does not re-derive it a third time.

## Verdict

`contextmemory-write-path-addressing-degeneracy` is **still OPEN**: `status:
implemented_pending_validation`, `severity: corrupting`. `/queue-experiment` Step 2.5c is
explicit that this status is open, not closed -- *"A status of the form
`implemented_pending_validation` (or any status containing `pending`) is still OPEN, never
closed"* -- precisely because `implemented` is a text prefix of it. The entry now also
declares `substrate_paths`, which it did not on 2026-08-18, and the overlap is mechanical
rather than argued:

```
ree_core/predictors/e1_deep.py::ContextMemory.write          <-- the ARM_SLEEP write path
ree_core/predictors/e1_deep.py::ContextMemory.compute_write_addressing_loss
ree_core/agent.py::compute_prediction_loss
```

Section 1's call chain (`run_sws_schema_pass -> e1.context_memory.write ->
ContextMemory.write`) is unchanged, so the defect is still on the write path of the single
component whose causal effect this experiment exists to measure.

## What changed since 2026-08-18 (none of it releases the gate)

Three write-address mechanisms have landed, all **DEFAULT-OFF**:

| mechanism | landed | knob |
|---|---|---|
| usage/conscience bias | ree-v3 `76cbf844` (2026-08-19) | `contextmemory_write_usage_balancing` |
| refractory mask | ree-v3 `692f8526d0` (2026-08-19) | `contextmemory_write_selection=refractory` |
| gumbel_learned tagger | ree-v3 `636d0e4fb2` (2026-08-27) | `contextmemory_write_addressing_loss_weight` |

Each build's own resolution note states it does **not** unblock this chip. Validation
experiments V3-EXQ-943 / 946 / 956 were queued; V3-EXQ-956 ran and **failed** the C2
content-discrimination criterion (confirmed autopsy `failure_autopsy_V3-EXQ-956_2026-08-29`).

**The still-live driver precondition** (from
`chip-20260819-contextmemory-gated-exps-driver-preconditions`, and it is the trap): both
flags default `False` and **no driver in `ree-v3/experiments/` sets any of them**, so a
driver written today runs the **unfixed argmin path** regardless of what has landed. Any
eventual driver must set one explicitly and assert it after construction -- the same
`from_dims`-swallows-unknown-kwargs hazard as Section 3(a).

## The new disposition question, and how it was resolved

`contextmemory_write_c2_criterion_reposed_20260829.md` (chip
`chip-20260829-contextmemory-c2-criterion-repose`, resolved 2026-08-29T17:13Z) found the C2
criterion **mis-posed** -- 2-cluster occupied-slot-set Jaccard at n=5 is a known-aliasing,
near-Bernoulli statistic -- and argued in its Section 4 that what actually blocked the
436e/436f retest was **occupancy**, not addressing quality, and that occupancy is now met by
all three mechanisms. Its recommendation 2 is to proceed with the SD-017/ARC-045/MECH-166
retest on the occupancy floor, treating content-discrimination as a *descriptive* readout
rather than a precondition gate.

That recommendation is **not applied**. The spike says so itself: it is *"a disposition call
for governance/a human, not something this spike unilaterally applies"*, and it left
`unblocks_claims` and `status` untouched.

**User decision 2026-08-29: HOLD THE BLOCK.** Put to the user as a three-way choice (hold /
adopt recommendation 2 / queue as an explicitly instrument-limited diagnostic); the user
chose to hold. Logged in `REE_assembly/evidence/decisions/RECOMMENDATION_LOG.jsonl`. The
governing reason is unchanged from Section 0: the defect's own `severity_rationale` predicts
this experiment's null almost verbatim, and running it now would manufacture that artefact a
third time.

## Resume condition (supersedes Section 5)

Either of these, whichever comes first:

1. `contextmemory-write-path-addressing-degeneracy` reaches a genuinely closed status
   (`implemented` / `validated` -- **not** anything containing `pending`); **or**
2. **governance ratifies the 2026-08-29 spike's recommendation 2**, i.e. records that
   SD-017/ARC-045/MECH-166 are gated on the occupancy floor only, and amends the substrate
   entry's `unblocks_claims` / disposition accordingly.

Sections 2 and 3 remain directly consumable either way -- T = 250, the DV set, the corrected
config field `within_life_sleep_step_ceiling`, and the three implementation findings. Re-run
Step 2.5c first, re-derive the queue id, and set one write-address flag explicitly.
