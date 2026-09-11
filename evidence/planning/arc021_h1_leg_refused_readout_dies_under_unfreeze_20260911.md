# ARC-021 channel-separation portfolio, H1 (drive axis) leg -- NOT QUEUED, REFUSED at design time: unfreezing the encoder kills the readout in BOTH arms

**Status: NOT QUEUED. No EXQ number consumed, no driver in `experiments/`, no queue entry, no coordinator row.** Refused at `/queue-experiment` Step 4.5's own governing question -- *can the load-bearing criterion actually FAIL?* -- on a measurement, not a judgement. The instrument that produced the refusal is landed at `ree-v3/experiments/_scratch/arc021_h1_encoder_unfrozen_drive_axis_instrument.py`, alongside its five probes, exactly as the H2 leg's reproducer is.

- **Written:** 2026-09-11T15:54Z
- **Session:** `queue-arc021-h1-20260911` (Mac `DLAPTOP`, main checkout), launched by `orchestrate-20260911-fast` under the user's 2026-09-11 authorisation.
- **Chip:** `chip-20260908-arc021-h1-drive-axis-leg`.
- **Sibling records:** H2 leg -- `arc021_h2_leg_blocked_substrate_merged_arm_crash_20260908.md` (blocked on substrate, GFLAG-0229). H3 leg -- ran as V3-EXQ-1011, `submargin_degradation_ruled_out`.

---

## 1. The finding, in one line

**Unfreezing the encoder destroys the `calibration_gap` / `attribution_auc` readout by ~90x, in BOTH arms**, so the registry leg's pre-registered criterion cannot fire in either direction. It is not a bar-calibration problem; it is that the instrument reads nothing once the manipulation is applied.

## 2. What the leg would have been

Registry leg `H-encoder-level-merge-degrades` of `arc021_channel_separation_necessity`; the DRIVE axis of the GOV-FANOUT-1 portfolio in `failure_autopsy_V3-EXQ-993a_2026-09-05` section 6:

> Same two arms with the **encoder unfrozen** and jointly optimised in P1, so a collapsed objective can corrupt the latent itself. Null: both mean paired diffs still > -0.15 with no sign consistency.

The instrument was built from **V3-EXQ-1011, not 993a** -- 1011's paired-CI verdict, its two falsifier DVs (`calibration_gap` AND `attribution_auc`), its `--self-test` grid and its honest `dv_bounds` handling are all strictly better than 993a's threshold-plus-sign-consistency rule, which the 993a autopsy's own repair 5 forbids inheriting. Changes made: P1 no longer freezes the encoder; each arm owns its encoder(s) inside its own optimizer(s); `n=48` seeds sized against a pessimistic SD; a third DIAGNOSTIC arm `SHARED_ENC_SEP_HEADS` merges the ENCODER while leaving heads disjoint, so a positive result could be attributed to the encoder level -- the registry leg's own name -- rather than to the trunk level 993a/1011 already measured as null.

Three gaps in 1011 were also closed on the way: a `dv_headroom` check for `attribution_auc` (1011's own code comment promises one -- "see its own check below" -- but none was ever written, so its AUC criterion ran ungated); per-criterion **re-derivable** `measured`/`threshold` records; and a flat top-level `readout` block (without one the runpack harvests `values={}` and no stop threshold can fire). Those improvements live in the instrument and should be carried into the successor.

## 3. The measurement

Five probes, all run **through the instrument's own `_run_cell`** -- never a probe subclass (993a red-team F3: its design probe consumed the torch RNG differently before head construction, and the whole control-arm measurement had to be redone).

### 3a. The leg is NOT substrate-blocked (probe 1)

All three arms run, and **the encoder demonstrably receives gradient** in each. The H2 leg's `ContextMemory` crash does not reproduce, exactly as the 2026-09-10 pre-flight predicted: this driver family imports only `ree_core.environment.causal_grid_world`.

```
arm                    runnable  encoder_grad  pre_clip_norm  harm_loss
SEPARATED              True      True                0.63098  0.68890
MERGED                 True      True                0.65222  0.64711
SHARED_ENC_SEP_HEADS   True      True                0.63153  0.68920
```

This also confirms the pre-flight's warning that the unfreeze is **not a one-line flip**: deleting 993a's `requires_grad_(False)` loop alone changes nothing, because the encoder calls sat inside a *separate* `torch.no_grad()` block and no optimizer held `encoder.parameters()`. All three had to go.

### 3b. The control arm produces no signal (probe 3)

Production schedule (P0=80, P1=80, 120 steps), 32 cells, 8 seeds **disjoint from any scored seed set**, both conditions, both criterion arms:

| condition | control mean gap | control max gap | control AUC | above chance |
|---|---|---|---|---|
| DENSE | +0.02144 | +0.06268 | 0.5322 | 0.032 |
| SPARSE | +0.01421 | +0.04400 | 0.5409 | 0.041 |

Frozen-encoder reference (V3-EXQ-1011, n=96): **0.4147 / 0.4071** on the gap, **~0.69** on the AUC. **0 of 16 control cells reach `SEPARATED_SIGNAL_FLOOR = 0.20`**; the largest is 0.0627.

### 3c. The decisive control -- it is not a plumbing bug (probe 4)

The alternative hypothesis is that the collapse is a defect introduced while unfreezing. Ruled out by running **this same driver** with the encoder RE-FROZEN at `_encode`, leaving every other line (heads, optimizers, clip, probes, verdict) on the shipped path:

| regime | arm | mean gap | mean AUC |
|---|---|---|---|
| FROZEN | SEPARATED | **+0.21685** | 0.652 |
| FROZEN | MERGED | +0.33038 | 0.725 |
| UNFROZEN | SEPARATED | **+0.00242** | 0.513 |
| UNFROZEN | MERGED | +0.02604 | 0.533 |

The frozen arm reproduces the reference regime and clears the 0.20 floor. **Ratio unfrozen/frozen = 0.011.** The plumbing is sound; the unfreeze is the cause.

### 3d. Why it is a REFUSAL and not a threshold to lower

Three of the five preconditions fail deterministically, on every seed, in both conditions, **before a single treatment cell is trained** -- computed exactly as the driver computes them:

| precondition | statistic | measured | required | verdict |
|---|---|---|---|---|
| `dv_headroom_margin_room_below_control` | range | 0.09262 | 0.30000 | UNMET, 3.2x short |
| `dv_headroom_control_signal_floor_reachable` | max_abs | 0.06268 | 0.40000 | UNMET, 6.4x short |
| `dv_headroom_auc_room_below_control` | floor_headroom | **-0.01857** | 0.10500 | UNMET, negative |
| non-degeneracy DENSE | control mean gap | +0.02144 | 0.20 | UNMET, 9x short |
| non-degeneracy SPARSE | control mean gap | +0.01421 | 0.20 | UNMET, 14x short |

The run would self-route `substrate_not_ready_requeue` / `non_contributory` every time.

**The pre-registered MARGIN of 0.15 is 1.6x the ENTIRE observed control range** -- a bar wider than the instrument's whole dynamic range. That is the V3-EXQ-936a failure shape (a bar ~7,900x above the maximum attainable effect, logged clean for three governance cycles).

Lowering the floor or shrinking MARGIN to fit is refused on the standing rule: *a pre-registered value that provably fails a gate is a design-time proof, never a threshold to lower.* And the deeper point is that it is **not a threshold problem at all** -- BOTH arms read within noise of zero, so their contrast measures the death of the readout, not channel separation.

For the record, the sign is the same "wrong direction" 993a and 1011 both saw: MERGED > SEPARATED by +0.037 DENSE / +0.125 SPARSE. At this scale that is uninterpretable and must not be cited as evidence in either direction.

### 3e. Two design facts the successor inherits

**The MSE targets must be detached, and the reason is asymmetric (probe 2).** With the encoder unfrozen, both MSE terms admit the trivial global optimum "encoder emits a constant". Measured: undetached targets collapse ARM_MERGED's latent dispersion 0.327 -> 0.048 (6.9x) while leaving ARM_SEPARATED untouched (ratio 0.999). That is a collapse in the **treatment arm alone**, which would have manufactured a result for a reason unrelated to channel incommensurability. The instrument therefore detaches: sensory target `sg(z)`, forward target under `no_grad`, harm BCE fully differentiable into the encoder. Detaching is the best available option **and the readout still dies**, so the refusal does not rest on this choice.

**The union grad-clip binds asymmetrically once the encoder is unfrozen.** 18.6% of steps in ARM_SEPARATED vs **44.2%** in ARM_MERGED (mean pre-clip norms 1.71 vs 1.84). Under 993a the encoders were outside the clip entirely, so this is new, and it is a second independent reason the leg as specified is not clean.

## 4. What is actually owed

**`complex (probe-gated)`, not `complicated (buildable)`.** The signal loss is **cumulative drift over ~9,600 encoder updates**, not an instantaneous property of unfreezing. Probe 5, control arm, DENSE, full schedule, 3 seeds:

| mode | mean gap | mean AUC | |
|---|---|---|---|
| unfrozen (the leg as specified) | +0.00178 | 0.499 | BELOW FLOOR |
| anchored (P0 reconstruction continued through P1) | +0.02456 | 0.563 | BELOW FLOOR |
| short (unfrozen for the LAST 10 of 80 episodes) | **+0.21158** | **0.675** | **CLEARS FLOOR** |

Anchoring the encoder with a maintained reconstruction term does **not** rescue it. Shortening the unfreeze does.

So the live question is an **unfreeze-DOSE spike**: *is there a dose at which the encoder receives materially channel-shaped gradient AND the readout survives -- and at that dose, is a merge-vs-separate contrast still a test of ARC-021 rather than a test of the dose?* Probe 5 shows only the two ends; nothing in between has been measured.

**The answer may well be NO**, and that would itself be the finding: H1 would be unanswerable in this surrogate, and the honest route to ARC-021's necessity half would be **H2** -- the leg ARC-021's `what_would_answer` literally names, currently substrate-blocked on the `ContextMemory` in-place write (`e1_deep.py:127`, `:272-273`; GFLAG-0229). That would be a real prioritisation finding for the substrate queue, not a null.

Note the trap to avoid in that spike: a dose chosen *because* it keeps the control arm above its own floor is a tuned knob, and pre-registering a criterion at such a dose is tuning the design toward a pass. The dose must be characterised first and fixed on its own grounds, with the control-arm signal reported at each dose.

## 5. Registry and claim state -- deliberately UNCHANGED

- Leg `H-encoder-level-merge-degrades` stays **`alive`** with `adjudicating_runs: []`. It has not been falsified and it has not been tested; it has been shown **un-attemptable with this instrument**. Nothing in `hypothesis_space_registry.v1.json` was edited (a concurrent session, `jolly-neumann-a8857e`, holds a claim on that file, and a narrow edit is not owed by a refusal).
- **ARC-021 and MECH-069 are untouched.** No evidence was produced in either direction; no manifest was written; nothing entered the evidence record.
- A governance flag (`evidence_discrepancy`, ARC-021 / MECH-069) carries the follow-on.

## 6. Artifacts

All under `ree-v3/experiments/_scratch/`:

| file | what it is |
|---|---|
| `arc021_h1_encoder_unfrozen_drive_axis_instrument.py` | the driver. `--self-test` (0 failures) and `--dry-run` work; a SCORED run is refused at `main()` so it can never enter the evidence record unpre-registered |
| `arc021_h1_runnability_probe.py` | probe 1 -- three arms run, encoder gradient live |
| `arc021_h1_detach_probe.py` | probe 2 -- the detach decision, measured |
| `arc021_h1_calibration_probe.py` (+ `.result.json`) | probe 3 -- the 32-cell production-schedule measurement |
| `arc021_h1_frozen_control_probe.py` | probe 4 -- the decisive frozen-vs-unfrozen control |
| `arc021_h1_anchor_probe.py` | probe 5 -- anchored / short-unfreeze repair candidates |
