# SD-063 online head training -- the MECH-314b per-candidate keystone (ARC-065 GAP-A follow-on 1)

**Status: substrate landed (code), DEFAULT OFF. No claims.yaml status / `v3_pending` /
`pending_retest_after_substrate` flag was flipped -- flag flips remain governance work per
`mech314bc_percandidate_extension_staged_2026-08-08.md` section 7.**

Session: `elated-jackson-f12eae`. Chip: `chip-20260822-sd063-head-training-keystone`
(user-authorised 2026-08-22, AskUserQuestion "Keystone build" -> "Chip it now").
Parent design record: `mech314bc_percandidate_extension_staged_2026-08-08.md` section 6 item 1.

---

## 1. What was asked, and what the gap actually was

The 2026-08-08 landing (ree-v3 `c0e0ce8`) gave MECH-314b a per-candidate **slot**:
`agent._curiosity_per_candidate_uncertainty` builds
`head.predictive_variance(z0_K, actions_K) -> [K]` and passes it to
`StructuredCuriosity.compute_score_bias` as `per_candidate_uncertainty`, where its deviation
lands in the argmin-relevant term. `use_e2_world_uncertainty` instantiates the SD-063
`E2WorldUncertaintyHead` on the agent.

**Nothing ever trained that head.** It sat at its random init for the whole of any run, so its
`predictive_variance` was a near-uniform vector and 314b's "per-candidate" contribution was a
vacuous channel -- the 604a / 624a / 614d / 640a failure class. Per-candidate-**capable**, not
**live**. This session builds the training loop.

## 2. What landed

All changes are **bit-identical OFF** (`use_e2_world_uncertainty_online_training=False` by default:
no optimizer is built, no replay buffer is allocated, the agent hook returns immediately).

### 2a. `ree-v3/ree_core/predictors/e2_world_uncertainty.py`
- `E2WorldUncertaintyConfig` gains `train_online` (default `False`), `warmup_steps` (200),
  `replay_capacity` (2048), `batch_size` (32), `ready_min_train_steps` (50).
- `train_step(z_world_prev, action, z_world_next, simulation_mode=False)` -- one P1 pinball
  update. Detaches inputs **and** target internally, so a caller that forgets cannot leak
  gradient into the encoder (the SD-031 agency-residual guard, previously only a
  by-hand convention in the documented external-optimizer recipe). Mirrors
  `ModelDisagreementEnsemble.train_step`. Refuses a mismatched batch rather than broadcasting.
- `observe_transition(...)` -- the per-tick online entry point. Buffers every observed
  transition; takes **no** head update until `warmup_steps` have been seen (P0: the z_world
  encoder is still becoming discriminative); thereafter samples a minibatch from the bounded
  replay and calls `train_step`. This is the V3-EXQ-716 driver's schedule, made a method.
  Minibatch rather than the single current transition because the pinball loss estimates 9
  quantile levels per z_world dim -- a batch of one is a near-useless gradient.
- The optimizer is built **lazily** on first `train_step`, so the existing callers that build
  their own (`test_sd063_conditional_uncertainty_head.py`, the V3-EXQ-716/716a drivers) are
  untouched. Documented: do not mix the two.
- `n_train_steps` / `n_observed_transitions` / `training_ready` / `get_state()` diagnostics,
  plus the per-read `_last_pvar_mean` / `_last_pvar_range` / `_last_pvar_relative_spread`
  recorded by `predictive_variance` (see section 4 -- the relative spread is the load-bearing
  one).
- `training_ready` is **diagnostic only** and is deliberately NOT consulted by
  `predictive_variance` or by the agent's 314b read: filtering the read on it would convert a
  vacuous channel into a *silent* fallback to the Phase-1 broadcast, which is exactly what the
  readiness gate exists to catch in the open.

### 2b. `ree-v3/ree_core/utils/config.py`
`LatentStackConfig` gains `use_e2_world_uncertainty_online_training` (default `False`) plus
`e2_world_uncertainty_{warmup_steps,replay_capacity,batch_size,ready_min_train_steps}`.
Following the existing SD-063 convention, these are not `from_dims` parameters -- set them on
`config.latent`.

**The master switch is deliberately named `use_*` rather than grouped under the
`e2_world_uncertainty_*` prefix of its siblings.** `tests/test_flag_inertness.py`'s dead-flag
recurrence guard (`test_flag_registry_is_current`) enumerates config-dataclass fields by
`startswith("use_") or endswith("_enabled")`, so a switch named outside that convention is
invisible to it -- it is neither required to carry a probe nor reported if it becomes inert.
Given that this entire chip exists because `use_e2_world_uncertainty` constructed a head that
nothing ever exercised, the new switch is named so the inertness guard can see it, and is
registered in `PROBED` against the ON/OFF agent-rollout pair in section 2d. (First attempt used
the prefix-grouped name and added it to `PROBED` anyway; that would have failed the registry's
*staleness* half -- an entry for a flag the scanner cannot see. Caught by the full suite.)

### 2c. `ree-v3/ree_core/agent.py`
- The new config is threaded into `E2WorldUncertaintyConfig` at instantiation.
- `_e2u_prev_z_world` one-tick-lag cache (mirrors `_sci_prev_z_world` / `_ba_prev_z_world`),
  cleared in `reset()` so the first tick of an episode never trains on a cross-episode
  "transition". The **head itself persists** across episodes -- learning is cumulative.
- `_train_e2_world_uncertainty(new_latent)`, called in `sense()` immediately after the MECH-276
  `_update_scientist_attribution` sibling, so it reads the same freshly-encoded latent and runs
  *after* this tick's selection has consumed the head (the MECH-074d second-pass rule: the gate
  never sees a head updated on the very transition it is about to be evaluated against).
  No-op when the head is absent, when `train_online` is off, in `eval()` mode (the P1-train /
  P2-eval split), and under simulation (`hypothesis_tag`) -- an imagined tick has no *observed*
  next z_world, so training on it would fit the head to the proposer's own rollout rather than
  to the world. That last gate is a schedule-correctness point, **not** a MECH-094 claim: the
  SD-063 head is a waking online read and MECH-094 does not apply to it.
- The action one-hot is reconstructed exactly as `_update_scientist_attribution` does, so both
  comparators read one action encoding.

### 2d. `ree-v3/tests/contracts/test_sd063_online_head_training.py` (new, 18 tests)
Inert-OFF surface, the P0/P1 schedule, bounded replay, loss reduction, conditional variance
monotone in the true per-action noise scale, the relative-spread discriminator **and its
negative control**, the SD-031 gradient guard, the simulation gate, and agent-level wiring
(OFF never trains; ON trains across a real `CausalGridWorldV2` rollout; `eval()` freezes).

---

## 3. Evidence that it trains

Synthetic heteroscedastic world (per-action next-state noise scales 0.01 / 0.05 / 0.20 / 0.60),
3000 transitions, `warmup_steps=50`, `batch_size=32`:

- pinball loss **0.18900 -> 0.06939** (mean of first / last 50 updates)
- `predictive_variance` over the 4 action classes:
  **[0.007303, 0.008071, 0.037735, 0.358951]** -- strictly monotone in the true noise scale,
  max/min **49x**.

Real agent rollouts (`CausalGridWorldV2`, `world_dim=32`, 4 episodes x 80 steps, seeds
71/101/202, `warmup_steps=100`): 216 P1 updates per run, terminal pinball loss ~1.9e-03.

---

## 4. THE BINDING FINDING: the section-5 readiness gate does not discriminate

**The ARC-065 section-5 gate `last_uncertainty_dev_range > 0` is NECESSARY BUT NOT SUFFICIENT.
An UNTRAINED head passes it -- on 320/320 ticks, in all 3 seeds -- and passes it with a LARGER
absolute range than a trained head.**

Measured on real agent rollouts, trained vs untrained, identical seeds and schedules. The
"max/min" column evaluates the head on all 5 action classes at one z_world; `rel_spread` is
`(max-min)/mean` from `get_state()`:

| seed | train | P1 steps | rel_spread | max/min | **absolute** range | `dev_range>0` ticks |
|------|-------|---------:|-----------:|--------:|-------------------:|--------------------:|
| 71   | ON    | 216 | 2.374 | **11.80x** | 5.75e-04 | 320/320 |
| 71   | OFF   |   0 | 0.179 | **1.19x**  | 8.62e-04 | 320/320 |
| 101  | ON    | 216 | 1.807 | **10.38x** | 4.01e-04 | 320/320 |
| 101  | OFF   |   0 | 0.256 | **1.28x**  | 1.27e-03 | 320/320 |
| 202  | ON    | 216 | 2.335 | **10.19x** | 4.27e-04 | 320/320 |
| 202  | OFF   |   0 | 0.142 | **1.15x**  | 6.82e-04 | 320/320 |

**Mechanism.** Training *lowers* the overall predicted spread -- the world is more predictable
than a random init assumes -- while *raising* the relative differentiation. A random-init MLP
evaluated on distinct action one-hots produces distinct outputs, so its cross-candidate range is
strictly positive; it is simply near-**uniform** (1.15-1.28x), which is the definition of the
vacuous channel. The absolute range is therefore the wrong statistic and, worse, points the
wrong way: in 3 of 3 seeds the untrained head's absolute range is the larger one.

**Consequence for the gate.** Before scoring any curiosity-dependent DV with 314b per-candidate
ON, the three section-5 assertions should be read as:
1. `last_bias_range > 0` -- unchanged (channel not flat);
2. `last_clamp_saturated_frac` strictly below `(K-1)/K` -- unchanged (ranking not compressed);
3. `last_uncertainty_dev_range > 0` -- **keep, but it is not sufficient**. Add
   `e2_world_uncertainty_last_pvar_relative_spread` well above the random-init band. Measured
   separation is clean and non-overlapping: untrained **0.14-0.26**, trained **1.81-2.37**. A
   threshold of **>= 1.0** sits an order of magnitude above the observed untrained ceiling and
   an order of magnitude below the trained floor; it is proposed, not yet validated on an
   independent run, and should be re-measured before being pinned.

This correction has **not** been written into
`mech314bc_percandidate_extension_staged_2026-08-08.md` section 5 -- that file was under an
active TASK_CLAIMS claim by `serene-yalow-3dd4b0-xref` (the section-4 budget-split
cross-reference) at the time, and the arbitration verdict was deferral. Handing it over here.

---

## 5. SECOND FINDING: the candidate pool, not the head, is now the binding constraint

Across all 6 runs the candidate pool carried **~2.0-2.4 distinct first-actions out of K=32
candidates** (seed 71: 2.32 / 2.41; seed 101: 2.03 / 2.06; seed 202: 2.25 / 2.19 for ON / OFF).
The figure is essentially identical trained and untrained, so it is a **proposer** property and
wholly independent of the head.

The head is evaluated at exactly those first actions, so a head carrying ~10-12x per-action
differentiation can express at most a **2-valued** vector across 32 candidates. This is the
V3-EXQ-614e monostrategy / proposer-collapse finding -- the same one that motivated ARC-065
GAP-A -- resurfacing one layer down, at 314b's consumption point rather than at
`cand_world_summaries`.

**So: training the head was necessary and is now done, but it is not sufficient for 314b to
carry meaningful argmin-relevant span.** Whatever the head learns is throttled by first-action
diversity in the candidate pool. The validation experiment (follow-on 3) should record
distinct-first-action count as a covariate, or it risks reading a proposer-diversity null as a
314b null. This is a `complex (probe-gated)` unknown, not a `complicated (buildable)` one: the
right next move is a spike measuring whether first-action diversity can be raised at all in
this substrate, not a build.

---

## 6. Scope held

Per the chip, this session did **not**: queue the ON-vs-OFF validation experiment (follow-on 3
-- goes via `/queue-experiment` once readiness is judged); build MECH-482's `epistemic_deficit`
accumulator (follow-on 2 -- `curiosity_learning_progress_source="epistemic_deficit"` remains
guarded to `None`); flip any claims.yaml flag; or touch the section-4 budget-split resolution
(unratified, owned by `chip-20260822-curiosity-budget-split-eligibility`). The work here is
independent of how the budget is eventually split.

## 7. Follow-on

1. **Correct section 5** of the staged design doc with the finding in section 4 above, once
   `serene-yalow-3dd4b0-xref` releases its claim. (Deferred by arbitration, not dropped.)
2. **Spike: first-action diversity in the candidate pool** (section 5). Gates how much 314b can
   ever contribute; blocks a clean read of the validation experiment.
3. **Validation experiment** for the 314b live path -- follow-on 3 of the parent doc, now
   additionally requiring the relative-spread assertion and the distinct-first-action covariate.
4. **Verification status (final).** Landed as ree-v3 `88287f11c6` on `origin/main`.
   The pre-commit contract gate ran on a clean idle hub: **4145 passed / 21 skipped /
   1 xfailed / 43 subtests**, 22m03s.

   **The gate caught a real defect in this change on its first clean run, and it is worth
   recording WHY it was missed.** `use_e2_world_uncertainty_online_training` failed
   `tests/contracts/test_from_dims_flag_reachability.py::
   test_every_unreachable_bool_flag_is_registered`. There are **TWO** independent bool-flag
   registries in this tree, not one, and they filter differently:
     - `tests/test_flag_inertness.py` -- the dead-flag guard; enumerates `use_*` / `*_enabled`
       only. Registered here in `PROBED` from the outset.
     - `tests/contracts/test_from_dims_flag_reachability.py` -- sweeps **every** bool on the
       config tree (deliberately NOT name-filtered, because 13 of its 37 unreachable flags
       match neither convention) and pins whether `from_dims` silently drops it. This is the
       `reference-reeconfig-from-dims-silent-kwargs` hazard, the one that once left 84 drivers
       running an ablation that was a complete no-op. Missed on the first pass.
   Registered in `REACHABLE_BY_ALTERNATIVE_IDIOM` (set by attribute assignment on
   `config.latent`, exactly like the rest of the SD-063 knob family) and deliberately **not**
   given a `from_dims` signature entry -- that file is explicit that adding one is a convention
   change, not a repair. A sweep for a third such registry found none: exactly two files in the
   tree enumerate config dataclass fields, and both are now satisfied.

   Earlier runs, for the record: 18 new contracts green (ree-worker-2); a targeted 132-test run
   green (ree-worker-4); a full suite at 4885 passed / 26 skipped / 215 subtests
   (ree-worker-3). **That full-suite run predates the flag under its final name and did not
   include the reachability contract, so it did not cover the defect above** -- recorded
   because it would otherwise read as stronger evidence than it was. Its single failure,
   `coordinator/test_cloud_scaler_orchestrator_veto.py::
   test_box_with_idle_metaworker_and_empty_ledger_IS_shut_down`, is **not** from this change:
   the diff touches no `coordinator/` path, the file passes 24/24 on clean `origin/main`
   locally, and it passed on a cloud worker with this working tree staged -- a cross-test
   interaction inside the shared pytest process. It also passed in the final green gate run.
   Not investigated further (out of scope).

   **Tooling note, observed twice and not repaired here.** The gate's own validation-cache
   writer commits `.contract_validation_cache.json` to `main` from inside the pre-commit hook,
   which moves the branch out from under the outer commit's compare-and-swap -- so a first
   green run reliably ends in `CAS failed` and must be re-run (the re-run then hits cache and
   is fast). Working as each piece intends; the interaction is the wart. Recorded, not filed.

5. `ModelDisagreementEnsemble.train_step` (MECH-441) has **no caller anywhere in the tree** --
   noticed in passing while surveying training hooks; the same untrained-head shape this chip
   fixed for SD-063. Not investigated, not in scope, recorded so it is not lost.
