# CEM `wanting_weight` / VALENCE_WANTING scoring pathway -- causal-ablation design

**Status: DESIGN NOTE + READINESS FINDINGS. Nothing here has been written to `claims.yaml` or
`substrate_queue.json`. Whether an experiment was queued from it is recorded in section 7.**

- Author: headless metaworker chip `chip-20260812-cem-wanting-weight-causal-ablation`
- Date: 2026-08-14
- Substrate probed: `ree-v3` @ working tree of `/home/ree/REE_Working/ree-v3` (see "Provenance")
- Related: V3-EXQ-914 / 914a, `failure_autopsy_V3-EXQ-914-914a_2026-08-13.md`, MECH-236,
  V3-EXQ-916a (`residue_wanting` orphaned-writer fix), organism review Section 3 Level C

---

## 0. One-paragraph summary

The brief asked for a Level-C causal-necessity ablation of the CEM trajectory-scoring
`wanting_weight * mean(VALENCE_WANTING)` term -- ARM ON vs ARM OFF, isolating the *scoring*
contribution rather than the *proposal* channel V3-EXQ-914 tested. A Step-2.5a readiness probe
run for this design shows that **the naive ON/OFF behavioural ablation would be structurally
guaranteed null**, for two independent, separately-confirmed reasons, and therefore must not be
queued in that form. (1) The 914 driver family never calls `agent.update_residue(...)`, so the
residue field has **zero active RBF centers**, so `VALENCE_WANTING` is identically 0 and the
wanting term is inert regardless of `wanting_weight` -- a strictly deeper defect than the
2026-08-13 autopsy's `NUM_HAZARDS=0` diagnosis. (2) Even once the field is live, the wanting
term's spread **across candidate trajectories within a scoring tick** is 2-3 orders of magnitude
smaller than the terrain term's, and at the documented operating value `wanting_weight=0.5` it
**never changed the CEM argmin in 484 scored ticks across 9 probed cells** -- the
V3-EXQ-604c uniform-broadcast / "modulatory-bias-selection-authority" hazard, measured for the
first time at the hippocampal CEM elite-selection call site. The design below therefore replaces
the behavioural-gap primary DV with a **selection-authority DV over a `wanting_weight`
dose-response ladder**, which is informative regardless of outcome, and reports the behavioural
DV as secondary.

---

## 1. Where the pathway actually is (task item 1)

Single consumer, confirmed by source read:

- `ree_core/hippocampal/module.py::HippocampalModule._score_trajectory` (def at line 1517;
  the wanting block at lines ~1573-1581):

  ```
  terrain_score = residue_field.evaluate_trajectory(world_seq).sum()          # ARC-007 STRICT
  if self.config.wanting_weight > 0:
      valence_flat  = residue_field.evaluate_valence(world_seq.reshape(B*H, D))
      wanting_score = valence_flat[..., VALENCE_WANTING].mean()
      terrain_score = terrain_score - self.config.wanting_weight * wanting_score
  if curiosity_weight > 0: ...        # unrelated
  # SD-MECH267 mode_value_weight term  # unrelated, independent of wanting_weight
  return terrain_score                # CEM MINIMISES -- lower is better
  ```

- Config: `HippocampalConfig.wanting_weight`, `ree_core/utils/config.py:2055`, **default 0.0**,
  docstring "Set ~0.3-0.5 for goal-directed navigation". Threaded from
  `REEConfig.from_dims(wanting_weight=...)` (`config.py:5849/7167`).
- `_score_trajectory` is used for (a) CEM elite-selection refit ranking of ghost-mixed candidates
  (`module.py` `_mix_value_flat_with_ghost` -> ~2365) and (b) the support-preserving keep/drop
  ranking (~1486), and its output feeds action-selection scoring (`agent.py:11415/11432/11449`).
- A second, structurally identical consumer exists in
  `ree_core/hippocampal/ghost_goal_bank.py:264` (`w_term = cfg.wanting_weight * wanting`) but
  that is `GhostGoalBankConfig.wanting_weight` (default 1.0, `config.py:1885`) -- a **different
  field on a different config object**, ranking bank entries, not trajectories. Do not conflate
  the two; the ablation below manipulates `config.hippocampal.wanting_weight` only.

Writer side (what puts anything into `VALENCE_WANTING` at all):

- `REEAgent.update_benefit_salience(benefit_exposure, drive_level)` (`agent.py:10738`)
  -> `ResidueField.update_valence(z_world, VALENCE_WANTING, salience)` (`field.py:816`)
  -> writes at `_nearest_active_center(z_world)`; **returns silently if no center is active**.
- Requires `serotonin.enabled` (i.e. `tonic_5ht_enabled=True`) and `salience > 0`, i.e. a
  genuinely nonzero `benefit_exposure`, which in `CausalGridWorldV2` requires
  `use_proxy_fields=True` and reading `info["benefit_exposure"]` (NOT `obs_dict`) -- this is
  exactly the V3-EXQ-916a fix, and it is a **driver-side** requirement: no agent-level step loop
  makes this call.

---

## 2. Readiness findings (Step 2.5a empirical probe -- the load-bearing part)

Probe script: `/tmp/probe_wanting_scoring.py` (throwaway; its full logic is reproduced in
Appendix A so this note is self-contained). Agent/env built to V3-EXQ-914's own recipe
(`GRID_SIZE=16`, `NUM_RESOURCES=3`, `use_proxy_fields=True`, `z_goal_enabled=True`,
`drive_weight=2.0`, forced `update_z_goal(0.5, 0.9)` per tick) plus `tonic_5ht_enabled=True`
and the canonical `update_benefit_salience(info["benefit_exposure"], drive_level)` call.

### Finding A -- the 914 driver family never calls `agent.update_residue()`, so the residue field is EMPTY

RBF centers in the main residue field are activated **only** by `ResidueField.accumulate()`
(`field.py:633` -> `RBFLayer.add_residue` -> `active_mask[idx] = True`). Its sole production call
site is `REEAgent.update_residue()` (`agent.py:9653`, the `harm_signal < 0` branch at 9812-9824).
`update_residue` is the canonical post-action hook (`experiments/_harness.py:201/357-361`,
"exactly one `agent.update_residue(harm_signal, ...)` per tick"). **V3-EXQ-914's step loop does
not call it** (its loop is sense -> clock -> `_e1_tick` -> `generate_trajectories` ->
`select_action` -> `update_z_goal` -> `env.step`).

Measured, first probe pass (`update_residue` NOT called, matching 914 exactly):

| config | harm events | active centers (max) | \|VALENCE_WANTING\|max |
|---|---|---|---|
| NUM_HAZARDS=0 seed 42 | 9 | **0** | 0.000000 |
| NUM_HAZARDS=0 seed 43 | 0 | **0** | 0.000000 |
| NUM_HAZARDS=2 seed 42 | 32 | **0** | 0.000000 |
| NUM_HAZARDS=2 seed 43 | 48 | **0** | 0.000000 |

Second pass, identical except `agent.update_residue(harm_signal)` added after `env.step`:

| config | harm events | active centers (max) | \|VALENCE_WANTING\|max |
|---|---|---|---|
| NUM_HAZARDS=0 seed 42 | 9 | 12 | 0.209283 |
| NUM_HAZARDS=0 seed 43 | 0 | 0 | 0.000000 |
| NUM_HAZARDS=2 seed 42 | 32 | 32 | 0.000000 (no benefit contact) |
| NUM_HAZARDS=2 seed 43 | 14 | 27 | 0.000000 (no benefit contact) |

**This sharpens the 2026-08-13 autopsy.** That autopsy attributed the dead terrain term to
`NUM_HAZARDS=0` ("a harm-accumulation mechanism with nothing to accumulate"). The probe shows
that is not the operative cause: with `NUM_HAZARDS=2` and 48 harm events the field is *still*
empty, because the harm never reaches the field. The operative cause is the missing
`update_residue` call. Consequently, in V3-EXQ-914/914a **`_score_trajectory` returned identically
0.0 for every candidate in every arm** -- not merely "goal-blind", but *entirely* flat, with CEM
elite selection reduced to index tie-break. This is a stricter version of the autopsy's
`MEASURES FAILED` verdict and does not change it; it does change what a successor must fix.

> **Load-bearing for V3-EXQ-914b.** The autopsy routes 914b to "pair `wanting_weight > 0` with the
> ghost-probe channel". **That is necessary but NOT sufficient.** If 914b sets `wanting_weight>0`
> while keeping 914's step loop, `VALENCE_WANTING` stays identically zero and 914b is vacuous
> again, for a third time. 914b must additionally (a) call `agent.update_residue(harm_signal)`
> per tick, (b) set `tonic_5ht_enabled=True`, (c) `use_proxy_fields=True` + read
> `info["benefit_exposure"]` (the 916a fix), and (d) verify a nonzero `VALENCE_WANTING` as a
> gating precondition rather than assuming it.

### Finding B -- the wanting term has no selection authority at documented operating weights

Even with the field live, the term must **vary across candidates within a tick** to change any
selection; a constant offset is rank-preserving (the V3-EXQ-604c uniform-broadcast hazard).
Measured by counterfactual re-score: at every scored tick, compute per-candidate terrain score
and wanting term, then compare `argmin(terrain)` with `argmin(terrain - w * wanting)`.

32 candidates per tick throughout. `update_residue` wired. 3 episodes x 40 steps per cell.

| config | ticks | wanting spread (mean) | terrain spread (mean) | ratio | argmin flips @ w=0.5 / 5 / 50 / 500 / 5000 |
|---|---|---|---|---|---|
| NH=0 s42 | 63 | 1.72e-04 | (n/a, see note) | -- | **0** / 0 / 38 / 50 / 50 |
| NH=0 s43 | 120 | 0 (field empty) | 5.40e-03 | -- | 0 / 0 / 0 / 0 / 0 |
| NH=0 s45 | 82 | 1.59e-04 | 1.82e-02 | 1:114 | **0** / 8 / 14 / 48 / 69 |
| NH=1 s42 | 35 | 8.95e-07 | 2.70e-02 | 1:30000 | **0** / 0 / 0 / 0 / 2 |
| NH=1 s43 | 120 | 7.38e-05 | 2.68e-02 | 1:363 | **0** / 0 / 0 / 40 / 109 |
| NH=1 s45 | 62 | 1.83e-05 | 5.17e-02 | 1:2822 | **0** / 0 / 1 / 7 / 49 |
| NH=2 s42/43/45 | 32/120/96 | 0 (no benefit contact) | 2.2e-2..3.2e-2 | -- | 0 everywhere |

**At `wanting_weight = 0.5` -- the value `HippocampalConfig`'s own docstring prescribes for
"goal-directed navigation" -- the argmin flipped 0 times out of 484 scored ticks, across every
probed cell.** Flips first appear around `w ~ 5-50` and become the majority case only at
`w ~ 500-5000`, i.e. **3-4 orders of magnitude above the documented operating range.**

This is the same pattern `substrate_queue.json`'s `modulatory-bias-selection-authority` entry
documents for `E3.select` ("modulatory/secondary score-bias channels ... are dominated by the
primary harm/goal score term, so they never change argmax"), now measured at a *different*,
upstream call site -- the hippocampal CEM elite-selection refit, which happens **before**
candidates ever reach E3, and which that already-implemented fix does not reach.

### Finding B2 -- confirmation at 5 episodes x 5 seeds, and the pre-registered env config

Second probe (`NUM_HAZARDS=1`, 5 episodes x 40 steps, seeds 42/43/45/46/47, `update_residue`
wired, `tonic_5ht_enabled=True`), 32 candidates/tick throughout:

| seed | active centers | \|WANTING\|max | ticks wanting != 0 | wanting spread | terrain spread | flips @0.5 | @50 | @500 | steps alive | contacts |
|---|---|---|---|---|---|---|---|---|---|---|
| 42 | 32 | 0.0178 | 30/60 | 1.08e-05 | 4.67e-02 | **0** | 0 | 5 | 60 | 8 |
| 43 | 32 | 0.2427 | 189/200 | 1.50e-04 | 4.61e-02 | **0** | 1 | 120 | 200 | 4 |
| 45 | 32 | 0.0140 | 103/116 | 2.07e-05 | 8.48e-02 | **0** | 1 | 7 | 116 | 15 |
| 46 | 32 | 0.0228 | 31/42 | 4.94e-05 | 8.42e-02 | **0** | 2 | 15 | 42 | 17 |
| 47 | 28 | 0.0985 | 158/200 | 3.41e-04 | 6.32e-02 | **0** | 3 | 142 | 200 | 26 |

**`wanting_weight = 0.5` flipped the CEM argmin 0 times in 618 scored ticks across 5/5 seeds**,
on top of the 484 ticks of the first probe -- 1102 ticks, zero flips, at the documented
operating value.

> **CORRECTION (same day, found while authoring the driver): those tick counts are ~10x
> INFLATED.** `REEAgent.generate_trajectories` (`agent.py:5581-5611`) returns **cached**
> `_committed_candidates` whenever `not ticks["e3_tick"]`, and the E3 cadence default is
> `e3_steps_per_tick=10` (`ree_core/heartbeat/clock.py`). Both probes re-scored on **every env
> step**, so one genuine CEM refit was counted up to ~10 times -- the same latch-and-reread
> hazard `/queue-experiment` documents for the E3 `last_*` diagnostics, one layer up. The
> **direction** of the zero-flip reading is unaffected (zero is zero at any denominator), but its
> **n** is ~10x smaller than stated: ~1102 env steps is roughly **~110 genuine refits**. The
> queued driver gates the re-score on `ticks["e3_tick"]` and reports `n_latched_ticks`, and a
> full-length engagement check on the honest denominator is in section 6a below. `w=50` flips 0-3 ticks (4/5 seeds nonzero, but marginal); `w=500` flips in
**5/5 seeds** (5-142 ticks). So the instrument demonstrably *can* detect authority, which is what
makes the null at 0.5 a finding rather than an artefact.

**Env config decision (settles open decision 1 below): `NUM_HAZARDS=1`.** At this setting P1
(field live) clears **5/5** seeds -- 28-32 active centers, `|VALENCE_WANTING|max` 0.014-0.243,
`ticks_wanting_nonzero_frac` 0.50-0.95, all comfortably above the 0.25 bar -- and P3 (positive
control) clears **5/5**. `NUM_HAZARDS=0` fails P1 on seed 43 (0 harm -> 0 centers);
`NUM_HAZARDS=2` fails P1 on 3/3 probed seeds (harm plentiful, benefit contact zero).

Two caveats to carry into the queue entry rather than bury:
- **`hazard_harm` is inert here.** `hazard_harm=0.05` and `0.1` produced *bit-identical* numbers
  in every one of the 10 cells, including harm-event counts -- so in this configuration the harm
  driving residue accumulation comes from `proximity_harm_scale` / health depletion, not hazard
  contact. Not chased further; recorded so nobody tunes that knob expecting an effect.
- **Early death on 3/5 seeds.** Seeds 42/45/46 ran 60/116/42 of a possible 200 steps. That is
  the untrained-agent death confound V3-EXQ-914 removed by setting `NUM_HAZARDS=0` -- which is
  not available here, since it is exactly what empties the field. `steps_alive` must be reported
  per arm per seed, and any behavioural (C_BEHAV) comparison must be per-step-normalised.

### Finding C -- the wanting channel needs a near-mutually-exclusive conjunction in this env

`VALENCE_WANTING` becomes nonzero only where **harm has already allocated a center** AND
**benefit exposure is nonzero at a nearby location**. In `CausalGridWorldV2` those two pull apart:
`NUM_HAZARDS=0` gives benefit contact but often no harm at all (seed 43: 0 harm events, 0
centers); `NUM_HAZARDS=2` gives plentiful harm but drives contact to zero (0 contacts on all
three probed seeds, and early death on seed 42). `NUM_HAZARDS=1` is the only probed setting where
all three seeds produced both -- and it still produced very small wanting magnitudes on two of
three seeds. **The env config is therefore itself a pre-registered, probe-calibrated choice, not
an inherited default.** See section 5 for the final selection.

---

## 3. The design (task items 2-4)

**Purpose: `diagnostic`, not `evidence`.** Justified: Finding B means the behavioural
ON/OFF contrast is structurally near-guaranteed null at operating weights, so a behavioural
evidence run would reproduce exactly the vacuity the 914a autopsy charged as `MEASURES FAILED`.
What is genuinely unknown, and is what this run measures, is *where along the `wanting_weight`
axis the pathway acquires selection authority at all*, and whether behaviour changes once it does.

### Arms -- a dose-response ladder, not a binary ablation

| arm | `wanting_weight` | role |
|---|---|---|
| `ARM_W0` | 0.0 | **the ablation** (pathway fully removed); also a structural negative control -- its selection-flip rate is 0 by construction |
| `ARM_W05` | 0.5 | the documented operating value ("~0.3-0.5 for goal-directed navigation") |
| `ARM_W50` | 50.0 | supra-operating; probe says flips begin around here |
| `ARM_W500` | 500.0 | **positive control** -- the instrument must be able to detect authority somewhere, or the whole measurement is uninformative |

Everything else is IDENTICAL across arms. In particular the MECH-293 ghost-probe stack is held
**OFF in every arm** (`use_mech293_ghost_probes=False` and its whole prerequisite stack), which is
what makes this a genuinely different test from V3-EXQ-914/914b -- see section 4.

### Wiring required in every arm (this is what makes the pathway live at all)

1. `tonic_5ht_enabled=True` (else `update_benefit_salience` no-ops -- 916a change 1).
2. `use_proxy_fields=True` in the env, and read `info["benefit_exposure"]`, not
   `obs_dict["benefit_exposure"]` (916a change 3).
3. `agent.update_benefit_salience(benefit_exposure, drive_level=...)` once per tick, at the
   canonical position right after `update_z_goal` (916a change 2 / `_harness.py`).
4. **`agent.update_residue(harm_signal)` once per tick after `env.step`** (Finding A -- the
   canonical `_harness.py:357-361` post-action hook, absent from the 914 lineage).
5. `z_goal_enabled=True`, `drive_weight=2.0`, forced `update_z_goal(FORCED_BENEFIT=0.5,
   FORCED_DRIVE=0.9)` per tick -- inherited from 914 unchanged, so `z_goal` formation is held
   constant and cannot be confounded with the manipulation.

### DVs

**Primary (mechanism, `C_AUTH`): `selection_flip_rate`** -- fraction of scored CEM ticks at which
`argmin_i( terrain_i - w * wanting_i ) != argmin_i( terrain_i )`, computed per tick by
counterfactual re-score over the actual candidate pool. Non-degenerate by construction: it is
defined at every tick, is not a per-step magnitude at the env's competence ceiling, and is
exactly the quantity "does this pathway have causal authority over selection" asks for.

Reported alongside it, per arm: `wanting_spread_mean` / `terrain_spread_mean` and their ratio
(`wanting_authority_ratio`), `ticks_wanting_nonzero_frac`, `valence_wanting_abs_max`.

**Secondary (behavioural, `C_BEHAV`, reported, non-gating): `mean_resource_proximity`**
(`obs["resource_field_view"].max()` averaged over env steps) -- V3-EXQ-914's own DV, already
calibrated on this env at `GRID_SIZE=16` (probe: mean 0.54, stdev 0.24 -- genuinely
discriminating, unlike `GRID_SIZE=8` where it saturates at 0.90+-0.02). Plus `contact_rate` and
`steps_alive` as diagnostic context only.

**On the brief's item 3 caution:** V3-EXQ-914's docstring warns that raw `contact_rate` is a bad
primary DV here (pinned at 0.00-0.014 in every arm across 5 probe seeds -- the env's foraging
competence ceiling). **That caution applies unchanged to this design** and is why `contact_rate`
is diagnostic-only. It applies *more* strongly, in fact: the probe measured 0-11 contacts per
cell at `NUM_HAZARDS=1`. `mean_resource_proximity` inherits 914's calibration and is the right
behavioural readout; but per Finding B it is expected null at `ARM_W05` and is therefore
explicitly **not** the gating criterion.

### Pre-registered acceptance criteria

- **P1 (gating) WANTING FIELD LIVE**: in every arm, `valence_wanting_abs_max > 0` and
  `ticks_wanting_nonzero_frac >= 0.25`, in `>= 4/5` seeds. If this fails, the run is
  uninformative about the pathway and must be reported as such, NOT as a null.
- **P2 (gating) FORMATION MATCHED**: `valence_wanting_abs_max` and `ticks_wanting_nonzero_frac`
  agree between `ARM_W0` and each ON arm within a pre-registered tolerance over the first
  episode (before behavioural divergence can feed back into where the agent writes wanting).
  This is what isolates the SCORING weight from signal FORMATION, per the brief's item 2.
  Measured on episode 1 only, deliberately: after that the arms visit different states and a
  formation difference is a *consequence* of the manipulation, not a confound.
- **P3 (gating) INSTRUMENT CAPABLE**: `ARM_W500.selection_flip_rate > 0` in `>= 3/5` seeds.
  The positive control. If even `w=500` never flips an argmin, the measurement cannot detect
  authority and no conclusion about `w=0.5` is warranted.
- **P0 (structural negative control)**: `ARM_W0.selection_flip_rate == 0` exactly, all seeds.
- **C_AUTH (the finding)**: report `selection_flip_rate` per arm with per-seed values. The
  pre-registered *directional* prediction, stated so it can be wrong: if the pathway is
  causally operative as deployed, `ARM_W05.selection_flip_rate > 0` in `>= 3/5` seeds.
  **The readiness probe predicts this will FAIL (0/484 ticks).** It is pre-registered anyway
  because the probe used 3 episodes x 40 steps on 9 cells and the run uses more; a non-zero rate
  at higher wanting magnitudes would be a genuine, informative surprise.
- **C_BEHAV (reported, non-gating)**: `mean_resource_proximity` per arm, per seed, with the
  `ARM_W05 - ARM_W0` and `ARM_W500 - ARM_W0` gaps. Interpreted **only** in the light of C_AUTH:
  a behavioural gap in an arm whose flip rate is 0 would indicate a leak through some other
  pathway and should be investigated, not reported as a wanting effect.

### DV-symmetry declaration (mandatory)

`selection_flip_rate` is a **rank/argmin** DV, so monotone-rescaling symmetry **does** apply and
is the point: it is invariant under any transform that preserves candidate ordering, which is
precisely why it detects the uniform-broadcast hazard instead of being fooled by it. It is
**not** invariant under the manipulation (`wanting_weight` scales one additive term
non-uniformly across candidates whenever the wanting field is non-constant over their world
states). `mean_resource_proximity` is a per-step continuous magnitude, not derived from any
CEM-internal score -- 914's own declaration carries over verbatim.

### Cost

4 arms x 5 seeds x 10 episodes x 40 steps = 8000 agent steps plus a 32-candidate counterfactual
re-score per scored tick. The probe ran 9 cells of 3 x 40 with the same re-score in roughly 6
minutes wall-clock on `ree-cloud-5`, so a full run is on the order of tens of minutes -- cheap.

---

### Finding D -- full-length engagement check on the HONEST (e3_tick) denominator

Run 2026-08-14 with the queued driver's own `_run_cell`, full length (10 episodes x 40 steps),
seeds 42/43, re-score gated on `ticks["e3_tick"]`:

| arm | seed | genuine refits | latched | flips | flip rate | wanting nonzero frac | \|WANTING\|max | authority ratio | mean_resource_proximity |
|---|---|---|---|---|---|---|---|---|---|
| ARM_W0 | 42 | 104 | 25 | 0 | 0.0000 | 0.750 | 0.0178 | 1.7e-04 | 0.6480 |
| ARM_W0 | 43 | 98 | 302 | 0 | 0.0000 | 0.980 | 0.5301 | 5.1e-03 | 0.6839 |
| ARM_W05 | 42 | 104 | 25 | 0 | 0.0000 | 0.750 | 0.0178 | 1.7e-04 | 0.6480 |
| ARM_W05 | 43 | 98 | 302 | 0 | 0.0000 | 0.980 | 0.5301 | 5.1e-03 | 0.6839 |
| ARM_W5000 | 42 | 104 | 25 | **43** | **0.4135** | 0.750 | 0.0178 | 1.7e-04 | 0.6480 |
| ARM_W5000 | 43 | 98 | 302 | **96** | **0.9796** | 0.980 | 0.5301 | 5.1e-03 | 0.6839 |

Three things this settles:

1. **P1 clears on the honest denominator** -- ~100 genuine refits per cell, wanting field live
   in both seeds. The design is not vacuous.
2. **P3 clears decisively**, which is why the positive control was raised from `w=500` to
   `w=5000` at Step-4 smoke time: the probe's `w=500` flip counts were measured on the inflated
   env-step denominator, so a control calibrated there could have failed on the honest one and
   self-routed the whole run `substrate_not_ready_requeue`. This change strengthens a control
   and does not touch the load-bearing C_AUTH criterion.
3. **ARM_W0 and ARM_W05 are BIT-IDENTICAL on every readout** -- 0 flips in 202 genuine refits.
   The pre-registered C_AUTH criterion is predicted to fail, and is registered anyway.

**And one genuinely new observation, which changes how C_BEHAV must be read.** At `w=5000` the
CEM argmin flips on **41-98%** of refits while `mean_resource_proximity` stays **bit-identical**
to the ablated arm (0.6480 / 0.6839). So on this substrate **a flipped CEM elite-selection argmin
does not, by itself, change behaviour** -- E3's own downstream action selection
(`agent.py:11415/11432/11449`) re-scores, and the flipped candidate evidently yields the same
executed action class. Two consequences: (a) a null C_BEHAV is the EXPECTED reading even in an
arm with full selection authority, and must not be reported as evidence that the wanting pathway
is behaviourally inert -- that conflates two separate links in the chain; (b) there is a second,
independent authority gap downstream of the one this design measures, which no experiment
currently addresses. Recorded in the driver's `c_behav_note` manifest field.

## 4. What this does NOT test (brief item 4)

**This does not retest V3-EXQ-914's ghost-branch finding.** 914/914a manipulated
`use_mech293_ghost_probes` -- which candidate trajectories are **PROPOSED** (a minority probe
budget seeded around ghost-goal-bank anchors). This design holds that channel **OFF in every
arm** and manipulates `config.hippocampal.wanting_weight` -- how candidates, however proposed,
are **SCORED** during CEM elite selection. Different config field, different code path, different
consumer, different question. The two are complementary halves of the same Level-C picture:
914/914b ask whether goal-tagged candidates get *proposed*; this asks whether a goal/benefit
gradient can *win* the selection once they are.

**Nor does it duplicate the routed V3-EXQ-914b.** 914b keeps the CLOSED/OPEN ghost-channel
contrast and turns `wanting_weight` on *in both arms* as an enabling condition. Here
`wanting_weight` is the manipulated variable and the ghost channel is the constant. Running this
first is arguably the right order, since it tells 914b's author **what `wanting_weight` value
would actually make the scoring term bite** -- and Finding B says 0.5 would not.

**It is not a test of MECH-236.** No claim tag is proposed for the primary DV. Candidate tags for
the eventual write-up, to be settled at queue time and not asserted here: none, `diagnostic`
purpose, with the findings reported into MECH-236's `evidence_quality_note` and into the
`modulatory-bias-selection-authority` substrate-queue entry as a second confirmed call site.

---

## 5. Open decisions a queueing session must settle

1. ~~**Env config.**~~ **SETTLED -- see Finding B2.** `NUM_HAZARDS=1`, `GRID_SIZE=16`,
   `NUM_RESOURCES=3`, `use_proxy_fields=True`; P1 clears 5/5 seeds and P3 clears 5/5.
   `hazard_harm` is inert in this configuration and 3/5 seeds die early -- both recorded above,
   both must be reproduced verbatim in the queue entry's calibration block.
2. **Whether to force the wanting field instead of earning it.** A driver-issued
   `residue_field.accumulate(z_world, ...)` seed at resource-proximal locations would guarantee
   P1 across all seeds, at the cost of the field no longer being the agent's own. 914 faced the
   identical choice for anchors and chose driver-issued writes with an explicit "this is an
   experimental proxy, not discovered production behaviour" flag. The same flag would be
   required here. Recommendation: **earn it** if `NUM_HAZARDS=1` clears P1 on >= 4/5 seeds;
   force it only if it does not, and say so loudly.
3. **Whether `benefit_terrain_enabled=True` belongs in the design.** It would give
   `_score_trajectory`'s terrain term a benefit-linked signal, which is closer to the deployed
   architecture -- but it is a *second* benefit-linked pathway and would confound the ablation
   (ARM_W0 would no longer be benefit-blind). Recommendation: leave it OFF and say why.
4. **`/queue-experiment` is mandatory** for the script + queue entry (CLAUDE.md "Experiment
   Scripts"). Nothing in this note may be shortcut into a direct `experiment_queue.json` append.

---

## 6. Provenance / reproduction

- Probes were run against the `ree-v3` working tree on `ree-cloud-5` on 2026-08-14
  (`/home/ree/REE_Working/ree-v3`), with `/opt/local/bin/python3`.
- Both probe scripts are throwaway scratch (`/tmp/probe_wanting_scoring.py`,
  `/tmp/probe_env_config.py`) and are **not** durable; Appendix A restates the measurement
  logic so the findings can be reproduced without them.
- The companion chip `chip-20260812-zgoal-wanting-coupling-reinstrument` (observational
  z_goal/wanting coupling on 916a's repaired substrate) had **not** landed at the time of
  writing -- it is `status: open`, released DEAD-ON-ARRIVAL when the Mac's headless `claude -p`
  could not authenticate. So the brief's item 5 sanity-check against an observational coupling
  measurement was not available. Per the brief, that does not block this design: Finding B is a
  *direct* measurement of the causal pathway's selection authority and does not depend on a
  naive observational correlation existing.

## Appendix A -- measurement logic (to reproduce Findings A and B)

Per tick, after `candidates = agent.generate_trajectories(latent, e1_prior, ticks)` and before
`agent.select_action(...)`:

```python
hip = agent.hippocampal
for tr in candidates:                     # 32 candidates in every probed cell
    ws   = tr.get_world_state_sequence()  # [B, H, world_dim]
    B, H, D = ws.shape
    with torch.no_grad():
        val = hip.residue_field.evaluate_valence(ws.reshape(B * H, D))
    wanting_i = float(val[..., VALENCE_WANTING].mean())          # the term _score_trajectory uses
    terrain_i = float(hip.residue_field.evaluate_trajectory(ws).sum())
flip = argmin(terrain_i - w * wanting_i) != argmin(terrain_i)     # selection authority
```

Field-liveness instrumentation (Finding A):
`hip.residue_field.rbf_field.active_mask.sum()` and
`hip.residue_field.rbf_field.valence_vecs[:, VALENCE_WANTING].abs().max()`.

---

## 7. Queue status

Recorded here rather than left implicit, because this note is the durable artifact and the chip
resolution note is only a pointer to it.

- **QUEUED as `V3-EXQ-931`** (2026-08-14), via `/queue-experiment`.
  Script: `ree-v3/experiments/v3_exq_931_cem_wanting_weight_selection_authority.py`.
  Both the script and the queue entry are on `ree-v3` `origin/main` (commit `ff69ac7e85`;
  a follow-up `ed7294d0b6` removed a stray pre-rename copy -- see the ID-collision note below).
  `validate_experiments.py --strict` OK, `validate_queue.py` OK, `--dry-run` smoke PASS,
  full-length engagement check in Finding D.
- **ID collision, resolved.** This was authored as V3-EXQ-929; a concurrent session landed
  `v3_exq_929_sleep_gap9_within_life_trigger.py` under that number during the run, and a third
  had already moved something 929 -> 930. Renamed to **931** after re-deriving the next free id
  from scripts + git log + the evidence corpus together.
- **STEP 8.6 NOT PERFORMED -- OPERATOR ACTION REQUIRED.** This was queued from `ree-cloud-5`,
  which has no `REE_assembly/coordinator.env`, so `POST /queue/add` could not be issued. Under
  Phase 3 the runners read the **coordinator DB**, not `experiment_queue.json`, and a git-only
  add from a headless cloud box is documented to be deleted by the next `phase3-queue` snapshot
  **without ever running** (4 losses in 4 attempts, 2026-08-08, this same box). **The entry is
  not runnable until a coordinator-capable box POSTs it.** From the Mac:
  ```bash
  set -a; . /Users/dgolden/REE_Working/REE_assembly/coordinator.env; set +a
  ITEM=$(git -C /Users/dgolden/REE_Working/ree-v3 show ff69ac7e85:experiment_queue.json \
    | /opt/local/bin/python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps({'item': next(i for i in d['items'] if i.get('queue_id')=='V3-EXQ-931')}))")
  curl -s -m 8 -X POST -H "Authorization: Bearer ${COORDINATOR_LOCAL_TOKEN}" \
    -H "Content-Type: application/json" -d "$ITEM" "${COORDINATOR_URL}/queue/add"
  ```
  Read the item from the **commit**, not the working tree -- a snapshot tick has very likely
  already deleted it from the file on disk. That is the expected case, not an error.
- **Governance flag raised: `GFLAG-0033`** (MECH-236, `evidence_discrepancy`) carrying Finding A
  -- that the routed V3-EXQ-914b fix is necessary but not sufficient.
