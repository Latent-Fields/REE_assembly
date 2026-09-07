# DV-range probe + design correction -- `waypoint_field_consumer_reach` leg H2

- **Status:** design record. **No experiment was queued by this session** (see "Why nothing was queued").
- **Written (UTC):** 2026-09-07T17:25Z by session `vigilant-hellman-b2261e` (Mac `DLAPTOP`, worktree; claims `vigilant-hellman-b2261e`, `-a1`, `-a1-doc`).
- **Campaign:** wave-4 S2 item **A1**, `chip-20260905-waypoint-consumer-reach-portfolio`, brief `science_wave_campaign_plan_20260907.md` section 3 S2.
- **Registry question:** `waypoint_field_consumer_reach`; hypothesis **`H-wpfield-zworld-interface`** (axis `representation`).
- **Pre-registration source:** confirmed autopsy `failure_autopsy_V3-EXQ-1004_2026-09-05.{md,json}`, `fanout_recommendation.suggested_probes[1]`.
- **Probe script:** `ree-v3/experiments/_scratch/exq_wpfield_h2_probe_dvrange.py` (scratch, no manifest, no queue entry -- same `_scratch` convention as the V3-EXQ-1005 probes archived at ree-v3 `8132312`).

---

## 1. Why this probe was run

The chip and the campaign brief both require **"measure the DV range at probe scale before pre-registering"**. Item 0 of this same campaign (V3-EXQ-1005) was REFUSED at `/queue-experiment` Step 4.5 for precisely the omission of that measurement: its design floor (0.02) sat above the achievable ceiling (+0.0001..+0.001). This probe is that check, run for H2 before any threshold was written down.

## 2. What H2 pre-registered

> **Declared null:** the `z_world` decodability lift is not distinguishable from zero while the raw-observation lift is large -- which would locate the loss at the encoder, not at the environment.

DV: linear decodability of the **pending waypoint's direction**, field ON vs OFF, measured at `z_world` and compared against the raw-observation reference (V3-EXQ-1004's 0.575 -> 0.841 imitation-accuracy lift).

## 3. Measurement

1004 bench geometry (`GRID_SIZE=12`, `N_WAYPOINTS=3`, `waypoint_visit_reward=0.2`, hazards/resources/energy_decay zeroed, `subgoal_arrival_position_check=True`, `hazard_free_contamination_gate=True`, `waypoint_field_decay=0.25`), all five 1004 seeds, 40 episodes x 200 steps per seed (n = 8000 states/seed), random-policy rollouts, 70/30 train/held-out split, multinomial logistic (LINEAR -- H2's claim is about what `z_world` linearly carries) over a 4-class direction label read from env ground truth.

**Ablation is by ZEROING the trailing 25 dims, not by turning the env flag off.** Turning the flag off shrinks `world_obs_dim` 275 -> 250 (`causal_grid_world.py::world_obs_dim`), which changes the encoder's first `Linear` and therefore its init RNG draw, so the ON/OFF pair would not be matched. Zeroing keeps the encoder byte-identical at init and makes the manipulation purely the CONTENT of the trailing 25 dims -- the same repair V3-EXQ-1004 applied to its own readers (its F7 zero-padding note).

| seed | majority | raw ON | raw OFF | **raw lift** | **randproj lift** | **z_world (untrained) lift** |
|---|---|---|---|---|---|---|
| 42 | 0.330 | 0.835 | 0.570 | +0.265 | +0.188 | +0.185 |
| 43 | 0.298 | 0.835 | 0.567 | +0.267 | +0.220 | +0.155 |
| 44 | 0.403 | 0.839 | 0.611 | +0.228 | +0.186 | +0.145 |
| 45 | 0.278 | 0.841 | 0.532 | +0.310 | +0.258 | +0.173 |
| 46 | 0.357 | 0.853 | 0.575 | +0.277 | +0.202 | +0.177 |
| **mean** | 0.333 | 0.841 | 0.571 | **+0.269** | **+0.211** | **+0.167** |

`randproj` = a random LINEAR projection 275 -> 32 (no ReLU, no encoder, no training). `z_world (untrained)` = `SplitEncoder.world_encoder` at init (275 -> 128 -> ReLU -> 32), the architectural floor.

## 4. The finding, and the design correction it forces

**H2's declared null is refuted by linear algebra alone, before any REE-specific fact is in play.**

A random 32-dim linear projection retains **78%** of the raw lift (+0.211 of +0.269); the untrained `SplitEncoder` retains **62%** (+0.167). On no seed is either near zero. This is Johnson-Lindenstrauss, not a property of REE's encoder: a 32-dim compression of a 275-dim vector is a near-isometry for linearly decodable structure, so "the field survives compression into `z_world`" is ~80% guaranteed by construction.

So a run pre-registered against "lift indistinguishable from zero" would resolve to **H2 eliminated** at the architectural floor, carrying zero information about REE. That is the same defect class that refused V3-EXQ-1005 -- a design decided by construction rather than by measurement -- caught this time before queueing rather than after.

**This does NOT refuse the leg.** It relocates the verdict. The corrected design:

| | pre-registered | corrected |
|---|---|---|
| verdict arm | `z_world`, encoder unspecified | **TRAINED** `z_world` (lineage-warmed on this geometry) |
| bar | lift indistinguishable from **zero** | lift materially **below the random-projection floor** (+0.211) |
| control | (none named) | `randproj` (isometry floor) **and** untrained `SplitEncoder` (architectural floor) |
| upstream reference | 1004's 0.575 -> 0.841 | reproduced in-probe as raw lift +0.269 |

**H2 CONFIRMED** iff the trained `z_world` lift falls materially below the random floor -- i.e. training *actively discards* the field, spending capacity elsewhere. **H2 ELIMINATED** iff the trained lift is at or above the random floor. The interesting outcome is now a *loss relative to a random baseline*, which is a real and falsifiable claim about learned capacity allocation, rather than the un-losable "is the field still in there".

## 5. Mechanistic support for the corrected form

`SplitEncoder` carries a dedicated auxiliary decode head for the **resource** field (`use_resource_field_head` -> `resource_field_head`, SD-018 AMEND, `latent/stack.py:921-927`) and `zworld_p0.RESOURCE_FIELD_SLICE = slice(225, 250)` is contract-pinned to it. There is **no waypoint-field head anywhere in `ree_core/latent/`** (grep: zero hits for `waypoint`). So the resource field has a standing supervised pressure keeping it in `z_world` and the waypoint field has only whatever the main objective incidentally preserves -- which is exactly the asymmetry that makes "training discards it" a live, non-trivial hypothesis, and the corrected verdict arm the one that tests it.

## 6. Convergence with V3-EXQ-1008 (in flight)

V3-EXQ-1008 LEG 1 carries `ws250_randproj` -- a random-projection control of the same family, on the same substrate. The two are on **disjoint slices**: 1008's `world_state` is exactly 250 dims (`local_view[0:175]` + `contamination[175:200]` + `hazard_field[200:225]` + `resource_field[225:250]`; the driver contains zero `waypoint` references, so the field is OFF there), while H2 is the trailing `[250:275]` that only exists when the flag is ON. So this is **not** duplication.

**But do not read 1008's number as directly comparable, and do not treat it as confirmation of the +0.211 floor.** The two controls measure different quantities: 1008 scores *absolute* agreement with an oracle action policy against a 0.80 bar (its own text anticipates the 250 -> 32 random projection may fail that bar), whereas this probe scores an *ON-minus-OFF differential* in direction decodability. A random projection can preserve a differential while failing an absolute bar, so a 1008 randproj miss would not contradict the +0.211 retention measured here. The useful transfer is methodological -- that a random-projection floor is the right control against which to read a `z_world` compression result at all -- not numerical. 1008 was `claimed` and running at the time of writing.

## 7. Why nothing was queued

The campaign's **pacing rule** (`science_wave_campaign_plan_20260907.md` section 5) allows up to **three** un-adjudicated results on origin. At 2026-09-07T17:15Z there were **five**, all unreviewed in `review_tracker.json`:

`v3_exq_1006_sd_e1_var_bar_portfolio_fidelity_anchor_20260906T195135Z_v3`, `v3_exq_1007_mech536_eval_persistence_discriminator_20260907T072349Z_v3`, `v3_exq_970a_contextmemory_write_content_h1_mi_instrument_20260907T152212Z_v3`, `v3_exq_972a_sd070_write_stream_heldout_linear_probe_20260907T162343Z_v3`, `v3_exq_1009_mech267_elite_channel_ceiling_spike_20260907T171115Z_v3`

(plus V3-EXQ-1008 claimed and running). `pending_review.md` reads 1 because it was generated 04:20Z and predates four of them. The chip's own instruction for this state is to spend the wait on design and red-team work and queue once the backlog clears -- which is what this record is.

## 8. What the queueing session inherits

- STOP-CHECK was clean at 17:15Z: not queued, both legs `alive` with empty `adjudicating_runs`, no driver in `git log`.
- The registry was **NOT** edited. No run has adjudicated anything, so `adjudicating_runs` stays empty -- writing it now would be a false record.
- H1 (`H-wpfield-objective-sparsity`) was **not** probed here; the chip's order queues H2 first as the cheaper leg. H1's DV range is still unmeasured and needs the same treatment before pre-registration.
- The probe script is committed and re-runnable: `/opt/local/bin/python3 experiments/_scratch/exq_wpfield_h2_probe_dvrange.py --seeds 42 43 44 45 46 --episodes 40 --steps 200` (~2 min on the Mac).
- Carry the autopsy's standing caveat: the driver docstring's A2C 0.00/0.10 visits/ep figure is single-seed, pre-SD-094-gate, self-contaminating-env -- it MOTIVATES H1, it is not evidence, and must not be cited as a baseline.
- Claims INV-086 and MECH-428 stay **read-across only**; neither is exercised by a decodability probe.
