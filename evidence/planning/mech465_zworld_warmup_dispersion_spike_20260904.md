# MECH-465 spike: does a TRAINED z_world change commit-gate dispersion?

**Kind:** scratch SPIKE (diagnostic probe). **Not** an experiment: no queue entry, no manifest,
no `run_id`, no claim status change. **A spike licenses nothing by itself** -- see section 6.

- **Date:** 2026-09-04
- **Session:** `campaign-c1b-20260904`, chip `chip-20260902-mech465-zworld-warmup-spike`
  (user-consented redirect approved 2026-09-03 in an `/metaworker-orchestrate` session)
- **Harness:** `evidence/planning/mech465_zworld_warmup_dispersion_probe_20260904.py`
  (this directory) -- the 2026-08-27 boundary-regime probe verbatim plus a warmup arm
- **Registry:** `MECH465-COMMIT-GATE-HEADROOM` corrected in `evidence/planning/substrate_queue.json`
  (REE_assembly `0abb9f0006`) -- gate-rescale route retired, `ready` -> false, node_class ->
  `complex (probe-gated)`

## 1. The question

MECH-465's substrate entry proposed a commit-gate rescale. Three probes had already measured
and declined that route:

| probe | gated quantity | verdict |
|---|---|---|
| stage-1 spike, 2026-07-20 | `_running_variance` EMA | dispersion 1.024-1.069x vs the 1.455x urgency bar -- FAILS |
| stage-2 probe, 2026-07-21 | SD-063 `predictive_variance`, deployment CEM | 1.2473x -- FAILS |
| boundary-regime probe, 2026-08-27 | rv at a calibrated boundary threshold | P1 fails 3/3; P2 fails 3/3 by 11-19x |

**All three ran on an untrained z_world** -- a frozen random projection. Their shared release
condition `sd_zworld_warmup_optimizer_group` was read as `implemented_pending_validation` when
it had in fact been `status: validated` since 2026-07-22. A validated standalone warmup
(`ree-v3/experiments/_lib/zworld_p0_warmup.py::run_zworld_p0`) was available and unused.

**Confound confirmed directly, not assumed:** `mech465_boundary_regime_probe_20260827.py` has
ZERO zworld/P0/warmup references. Its only z_world contact is reading `lat.z_world` as an
observation (line 51).

So: **is "the rv distribution is a point mass" a property of the GATE, or of an untrained encoder?**

## 2. Design

The 2026-08-27 harness unchanged -- same `REEConfig`, same urgency grid
`URG = [0.04, 0.10, 0.16, 0.22, 0.28, 0.34]`, same exogenous-urgency idiom, same 600 ticks/seed,
same post-warmup window `tick >= 90`, same per-seed thresholds it calibrated -- plus one arm that
calls `run_zworld_p0(agent, warmup_env, seed, episodes, steps_per_episode, RandomPolicy(seed))`
before measuring. Three arms per seed: COLD (no warmup), WARM60, WARM200 (P0a episodes).
Seeds 0, 1, 3 at thresholds 0.00517 / 0.00570 / 0.00283. Warmup env is a dedicated instance, and
`run_zworld_p0` is RNG-neutral by construction, so the arms differ only in whether the encoder
was trained.

**Non-vacuity control (the point of the spike, so it is measured rather than assumed):** the
world-encoder parameter L2 delta is recorded per arm. `V3-EXQ-737a` is the documented failure
mode -- 0 of 4 `world_encoder` tensors changed. Here **4/4 tensors changed on 3/3 seeds in both
warm arms**, `p0a_ran=True`, `n_buffered` 1141-1174 (WARM60) / 3741-3812 (WARM200),
`p0a_holdout_mean_lift` 0.546-0.554 against SD-070's own +0.23..+0.47 target band. The warmup
really trained.

## 3. Result

Pre-registered P2 metric = within-seed `IQR(rv)/median(rv)`, floor **0.51**.

| seed | arm | n_post | rv median | **IQR/med** (floor 0.51) | vs COLD | p99/p1 | commit rate by urgency level |
|---|---|---|---|---|---|---|---|
| 0 | COLD    | 52 | 0.003597 | **0.0276** | -- | 1.820 | 1.00 0.89 0.86 1.00 1.00 1.00 |
| 0 | WARM60  | 63 | 0.010528 | **0.0456** | 1.65x | 1.347 | 0 0 0 0 0 0 |
| 0 | WARM200 | 57 | 0.007706 | **0.0881** | **3.19x** | 1.556 | 0 0 0 0 0 0 |
| 1 | COLD    | 114 | 0.005922 | **0.0230** | -- | 1.306 | 0.58 1.00 0.94 1.00 0.84 0.96 |
| 1 | WARM60  | 64 | 0.007447 | **0.1705** | 7.41x | 1.780 | 0 0 0 0.07 0.38 0.50 |
| 1 | WARM200 | 73 | 0.013432 | **0.1899** | **8.26x** | 1.508 | 0 0 0 0 0 0 |
| 3 | COLD    | 57 | 0.005671 | **0.0357** | -- | 1.821 | 0 0 0 0 0 0 |
| 3 | WARM60  | 63 | 0.013226 | **0.1291** | 3.62x | 1.515 | 0 0 0 0 0 0 |
| 3 | WARM200 | 66 | 0.017737 | **0.1729** | **4.84x** | 1.555 | 0 0 0 0 0 0 |

**Harness fidelity check.** The COLD arm reproduces the 2026-08-27 readings closely on the same
seeds (0.0276 vs 0.0279 seed 0; 0.0230 vs 0.0266 seed 1; 0.0357 vs 0.0450 seed 3), so the WARM
deltas below are attributable to the warmup and not to a harness difference.

### The finding, in one line

**Warming z_world raises within-seed rv dispersion monotonically with warmup budget, on 3/3
seeds, by 3.2x-8.3x -- and P2 still fails on 3/3 seeds, now by 2.7x-5.8x instead of 11-19x.**

## 4. What this licenses

1. **The confound was real and material, not merely plausible.** The 2026-08-27 "P2 fails by
   11-19x" figure was measured on an untrained encoder and **overstates the failure by roughly
   3-4x**. That correction should be carried wherever the 11-19x number is cited.
2. **The gate-rescale route is NOT "fully exhausted".** The chip's step 3 offered exactly two
   write-ups -- clears the bar (mint the build) or still fails (mark the route exhausted). The
   measured result is neither: it still fails, but the failure is monotone-decreasing in warmup
   budget on every seed, and most of the gap has closed on a log scale. Declaring exhaustion from
   3 seeds at a warmup budget the trend has not yet plateaued at would be the same error the
   2026-08-27 probe made in the other direction -- concluding about the gate from a measurement
   the encoder was confounding.
3. **P1 is not readable in the WARM arms at all, and this is a measurement gap, not a P1 result.**
   Warming shifts the rv *location* 1.4-3.1x above the COLD-calibrated per-seed threshold, so
   commitment never fires and every WARM commit rate is degenerate. Reading P1 under warmup needs
   per-seed recalibration to the WARM median. The 2026-08-27 probe found that recalibration does
   not converge (target moves 35-165%, graded band 2.7-4.5% wide) -- but **that finding is itself
   confounded by the same untrained encoder** and should not be carried forward as settled.
4. **Do not use the p99/p1 column against the 1.455x bar.** At n_post 52-114 the 1st/99th
   percentiles are effectively tail order statistics; the column shows no consistent direction
   (COLD 1.31-1.82, WARM 1.35-1.78) and is reported only for continuity with the earlier probes'
   metric. The pre-registered within-seed P2 metric is IQR/median and is what section 3 turns on.

## 5. What this does NOT license

- **No build.** Not the gate rescale (retired on the three prior probes' verdicts, unchanged by
  this spike), and not a new substrate entry minted by this session. The registry entry stays
  `complex (probe-gated)` with `ready: false`.
- **No claim status, confidence, or evidence change** on MECH-465 or anything else. A spike is
  not evidence for a claim; nothing here was pre-registered as a falsifier.
- **No conclusion about MECH-465's own assertion** (that arousal's effect on WHETHER commitment
  fires is expressible near the gate boundary). The DV is still saturated; this spike only moves
  the estimate of how far from expressible it is.

## 6. Recommended next step -- for GOVERNANCE to route, not for this session to mint

The natural next probe is a **warmup-budget sweep** (WARM200 -> WARM400/800, plus the full phased
P0a -> P0b warmup rather than P0a alone) on the same three seeds, with per-seed thresholds
recalibrated to each arm's own WARM median so P1 becomes readable. Two pre-registrable outcomes:
IQR/median plateaus below 0.51 -> the route IS exhausted, with the confound genuinely addressed;
it keeps climbing -> the "gate has no headroom" premise under this whole entry was an artefact of
an untrained encoder and MECH-465's gap needs restating.

Raised to governance as an `evidence_discrepancy` flag rather than actioned here.

## 7. Reproduce

```bash
cd /Users/dgolden/REE_Working/REE_assembly/evidence/planning
# COLD / WARM60 / WARM200 for seed 0 (thr from the 2026-08-27 calibration)
/opt/local/bin/python3 mech465_zworld_warmup_dispersion_probe_20260904.py 0.00517 0 600
/opt/local/bin/python3 mech465_zworld_warmup_dispersion_probe_20260904.py 0.00517 0 600 warm
/opt/local/bin/python3 mech465_zworld_warmup_dispersion_probe_20260904.py 0.00517 0 600 warm 200
# seed 1 thr 0.00570, seed 3 thr 0.00283
```

Ran on the Mac (`DLAPTOP`, `darwin-arm64`, torch 2.10.0). Total cost ~6 minutes for all nine
cells: 19-37 s per COLD/WARM60 cell, ~60 s per WARM200 cell. Machine-class caveat: these are
continuous dispersion statistics, not sampled discrete actions, so they are not exposed to the
`torch.multinomial` cross-machine-class divergence -- but the absolute rv values are still
Mac-class and a cloud replication should re-measure rather than compare against this table.

**Warmup variant actually exercised:** `p0a_used_reconstruction_head=True`,
`used_proximity_head=False`, `resource_field_weight=0.0` (the SD-018 directional-field leg OFF,
the default). A sweep that turns the field leg on is a different manipulation and would need its
own COLD baseline.
