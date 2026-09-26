# A1 cost re-measure: INT arm per-seed wall on the branch head with W4 ON (Y5)

- **Status: MEASUREMENT ONLY, timing, no science readout.** Answers `w4_e3_aggregation_build_20260925.md` finding F3 and the v3c addendum's Y5 ("COST is STALE for any A1 run with W4's DISC_0.5 ON... re-measurement specified, not invented"). Session `bt0926-a1cost` (`orchestrate-20260924-breakthrough-c2`), chip_ref `chip-20260926-a1-cost-remeasure-w4on`. Written 2026-09-26T04:33Z.
- **Code:** ree-v3 `origin/integration/coupled-loop-repair` @ `1b013d613b3e00fc7fbf8bd414dca1cb1d388308`, throwaway detached worktree `.scratch/breakthrough-20260924/wt-a1cost` (repo-relative: `.scratch/wt-a1cost`). Already tagged `archive/coupled-loop-repair-1b013d6` and pushed (reused from `bt0926-w3rel`'s prior work on the same sha; no new tag needed). **No `ree_core` edits.**
- **Evidence domain: D1** (wall-clock cost of native code paths under controlled configs). No behaviour or criterion claim.
- Probe: `.scratch/breakthrough-20260924/a1cost/a1cost_probe.py` (kept in `.scratch`, not committed alongside -- small but cites absolute worktree paths; results at `.scratch/breakthrough-20260924/a1cost/results/*.json`).

## 1. Premise re-measured before designing the probe

| # | premise (from the brief / Y5) | re-measured | verdict |
|---|---|---|---|
| P1 | The branch head needs tagging | `git ls-remote --tags origin` already has `archive/coupled-loop-repair-1b013d6` at `1b013d613b3e00fc7fbf8bd414dca1cb1d388308` (from `bt0926-w3rel`, same sha as `origin/integration/coupled-loop-repair` HEAD at fetch time) | **corrected: no new tag needed.** Reused the existing one |
| P2 | The v3b/v3c INT trainer multiplier (1.2/1.3/1.4x NATIVE, "DRAFT, ungrounded") is the thing Y5 flags as stale, and only W4's marginal cost is unmeasured | Measured directly (sec 3): the **INT arm's trainer-ON cost with W4 OFF is already 2.3-4.1x NATIVE** (under matched autograd settings, sec 2 caveat) -- far above the assumed 1.2-1.4x, and unrelated to W4. W4 ON vs OFF on top of that is a much smaller, noisy delta | **corrected.** The multiplier itself (not just its W4 increment) was never grounded against the actual built member roster (E1, E2Self, HarmEval, E2WorldMember/W3, WorldEncoderMember/W6a, CodecMember/W1) at production batch sizes. Y5's framing ("re-measure the W4 increment") undersells the finding: the pre-W4 baseline was already wrong |

## 2. Design and a caveat on the NATIVE baseline

- **Env:** `CausalGridWorldV2(size=8, num_hazards=2, num_resources=3, max_episode_steps=200, proximity_approach_magnitude_tiebreak=True)` -- A1 draft sec 3. `world_dim=self_dim=32` (deployed).
- **Seeds:** 902 (benign) and 901 (hazard_trapped), reusing the A1-stratum classification already measured by `w3_reliability_sweep_20260926.md` (`hazard_stratum_A1` field in its own per-seed JSON, same tag/sha lineage) rather than re-classifying -- cheaply available, per the brief.
- **Configs, each run 300 waking ticks (env resets mid-run; ticks counted, not episodes), `torch.set_num_threads(2)`:**
  - `native`: `REEConfig.from_dims(...)` with no extra flags (`waking_trainer_enabled` defaults `False`) -- matches sec 1 of the v3c addendum ("all flags off" for NATIVE).
  - `int_codec_w4off`: full v3c INT-CODEC member roster ON at **production defaults** (not the contract tests' cheap batch sizes): `waking_trainer_enabled=True, waking_trainer_every_k=1` (+ implicit HarmEvalMember), `waking_trainer_e1_enabled=True`, `waking_trainer_e2_self_enabled=True` (T1), `waking_trainer_e2_world_enabled=True` (W3, batch 32 default), `waking_trainer_world_encoder_enabled=True` (W6a, batch 64 default), `waking_trainer_codec_enabled=True` + `use_codec_bounded_decode=True, use_codec_iter0_image_match=True` (W1). `use_e3_discounted_aggregation=False`.
  - `int_codec_w4on`: same, with `use_e3_discounted_aggregation=True, e3_aggregation_gamma=0.5` (DISC_0.5).
  - **Scope cut, stated plainly:** only **INT-CODEC** was timed, not INT-ACT. The v2 arithmetic (sec 11) assumes ASP costs "at most INT-CODEC's per step" (DRAFT, unmeasured) -- CODEC's measured cost is used here as the conservative (upper-bound) proxy for both variants' non-NATIVE-family arms. This is unverified, not re-measured, and should be closed before a real cost commitment.
- **Caveat on the NATIVE number (found during this measurement, not anticipated):** `StepHarness(..., train_mode=True)` was used for **every** config, including `native`, so the loop timer excludes one-time `REEAgent`/`CausalGridWorldV2` construction (t0 starts after `build()` returns) but runs NATIVE's forward pass under **autograd-enabled** (`nullcontext`), not `torch.no_grad()`. NATIVE has no trainer to consume that graph, so this measures NATIVE's cost **with unused gradient tracking left on** -- higher than the deployed NATIVE arm's true cost. Evidence this happened: my NATIVE numbers (0.086 s/tick benign, 0.149 s/tick trapped; extrapolated to 5,400 ticks: 462s / 806s) sit **above** RT-5's independently measured NATIVE range (123-439s over 5,400 steps, `a1_rt5_native_reseed_probe_20260925.md` `332ab3f7f8`, reproduced in sec 11 of the A1 draft) even on the benign seed. **Consequence for this document:** NATIVE-family arm cost below uses RT-5's own measured figures (123/180/439s), NOT my own NATIVE run, which is reported only to show the size of the train_mode confound (a data point for whoever re-measures this with matched `no_grad`). The INT-arm absolute numbers (below) are NOT affected by this caveat -- they need `train_mode=True` regardless (their trainers require gradients), so they are direct, uncounfounded measurements of the INT arm's actual cost.
- **Mac CPU lock:** one hold, `bt0926-a1cost` 04:22:30Z-04:31:20Z (~8m50s, under the 15 min cap), all 6 timed runs (2 seeds x {native, w4off, w4on}) inside it; released cleanly.

## 3. Measured results (raw)

| config | seed (stratum) | ticks | episodes | wall (s) | s/tick |
|---|---|---|---|---|---|
| native | 902 (benign) | 300 | 2 | 25.7 | 0.0855 |
| native | 901 (hazard_trapped) | 300 | 15 | 44.7 | 0.1492 |
| int_codec, W4 OFF | 902 (benign) | 300 | 3 | 104.5 | 0.3482 |
| int_codec, W4 OFF | 901 (hazard_trapped) | 300 | 6 | 104.4 | 0.3481 |
| int_codec, W4 ON (DISC_0.5) | 902 (benign) | 300 | 4 | 106.2 | 0.3539 |
| int_codec, W4 ON (DISC_0.5) | 901 (hazard_trapped) | 300 | 2 | 70.3 | 0.2343 |

**INT/NATIVE multiplier** (INT s/tick over MY OWN matched-`train_mode=True` NATIVE s/tick -- see sec 2 caveat on why this ratio, not NATIVE's absolute number, is the reusable output):

| seed | W4 OFF | W4 ON |
|---|---|---|
| 902 (benign) | 4.07x | 4.14x |
| 901 (hazard_trapped) | 2.33x | 1.57x |

**W4 ON vs OFF, same seed (the number Y5 actually asked for):** seed 902: **+1.6%** (1.016x). Seed 901: **-32.7%** (0.673x, i.e. W4 ON measured *faster*). **These disagree in direction. Reading: CANNOT_DETERMINE at this N.** Two contributing structural reasons, D0: (i) W4's `Lmax-1` extra scorer calls (`w4_e3_aggregation_build_20260925.md` sec 2, F3) fire only on a **planned** E3 read, which the multi-rate clock (`experiments/_harness.py` step order, comment 3: "multi-rate clock + optional E1 tick") gates to a coarser cadence than one call per env tick -- so its cost is diluted by however many per-tick clock advances in a given 300-tick sample do NOT trigger a planned read, and that count is seed- and episode-length-dependent (seed 901's hazard-trapped resets produced very different episode counts under W4 OFF (6) vs ON (2), which is itself further evidence the two runs are not tick-matched at the sub-episode level); (ii) W4 ON/OFF are **independent constructions** (each its own `REEAgent`, its own RNG stream once flag-dependent modules register in a different order -- Q14/X6 in the A1 draft already found flag-gated modules shift downstream init), not a paired same-agent toggle, so per-seed noise from where episodes happen to reset is not cancelled out. **Recommended fix for a real number:** a paired measurement that toggles `use_e3_discounted_aggregation` on the SAME constructed agent/session (mid-run, matching N3's `_score_depth_limit` restore-in-finally pattern) rather than two independent builds, over more ticks (>=1,200, the W3 dose) so the planned-read count stabilises. Not done here (time budget).

## 4. Extrapolation to the draft's full per-seed schedule (5,400 agent steps, RT-5's measured full-arm length, sec 11 of the A1 draft)

**NATIVE-family arms (4 per seed: NATIVE + NATIVE-R1..R3): unchanged, RT-5's own measured figures** (123s / 180s / 439s low/mid/high; sec 2 caveat explains why my own NATIVE run is not substituted here).

**INT-type arms (all arms other than NATIVE-family: SHUF/FROZEN/R1/NOVAL/babble-attribution variants) -- CODEC proxy, direct measurement, extrapolated linearly (s/tick x 5,400):**

| | benign (s902) | hazard_trapped (s901) |
|---|---|---|
| W4 OFF | 1,879s = 0.522h | 1,879s = 0.522h |
| W4 ON | 1,911s = 0.531h | 1,264s = 0.351h |

Treating all four as samples of "one INT arm's cost" (sec 3's CANNOT_DETERMINE on isolating W4 means they should not be split into a clean on/off table yet): **low 1,264s (0.351h), mid 1,733s (0.481h), high 1,911s (0.531h)** per INT-type arm per seed. This replaces the DRAFT's `1.2/1.3/1.4x NATIVE` multiplier (sec 11), which this measurement shows was **not merely stale for W4 -- it was never grounded against the built roster at all** (sec 1, P2).

**Revised per-seed wall, 16 arms (ABSENT: 4 NATIVE-family + 12 INT-type) / 18 arms (GROUNDED: 4 + 14), per the v3c-current arm count (X16):**

| mode | low | mid | high |
|---|---|---|---|
| ABSENT (12 INT arms) | 4.35h | 5.98h | 6.86h |
| GROUNDED (14 INT arms) | 5.05h | 6.94h | 7.92h |

**24 admitted seeds (12 benign + 12 trapped, before screen/reserves):**

| mode | low | mid | high |
|---|---|---|---|
| ABSENT | **104 CPU-h** | **144 CPU-h** | **165 CPU-h** |
| GROUNDED | **121 CPU-h** | **167 CPU-h** | **190 CPU-h** |

**+ screen** (unchanged by this remeasurement -- NATIVE-only, ~0.7-2.5h per the draft) **+ reserves** (4 extra seeds at the same per-seed rate as above, ~24-32h at mid): **total ABSENT ~169-177 CPU-h mid, GROUNDED ~193-201 CPU-h mid** (low/high bands scale the same way; not spelled out digit-by-digit here given the N=2-seed, single-variant input -- treat the mid figure as the headline, the band as the uncertainty it actually carries).

**Against the draft's current (X16, stale) figure -- 23.5 / 26.6 CPU-h mid for 24 seeds (16/18 arms) -- this re-measurement is about 6x higher at the mid estimate.** The gap is almost entirely the INT-arm multiplier correction (sec 1 P2), not the W4-specific increment, which sec 3 found inconclusive and in any case is small relative to the trainer-roster-vs-NATIVE gap.

## 5. Cloud-worker translation (ratio source stated, not invented)

Per `n2_replay_encoder_probe_20260925.md` "Cost" section: Mac-measured **43 min** per seed at the W3 dose (post=1200) -> **cpx22** (2 vCPU, 1 job) estimated **5-7h** for that item -> **cx43** (8 vCPU, 4 jobs) estimated **2-3h**. Ratio: cpx22/Mac ~= (5-7h)/(43min=0.717h) = **7.0-9.8x**; cx43/Mac ~= (2-3h)/0.717h = **2.8-4.2x**. This is the only ratio measurement on record (V3-EXQ-1108); it was for a different workload (W3-dose replay-encoder item, not an A1 arm), so applying it here is an extrapolation, not a re-measurement, and is stated as such.

**Per-item wall (one seed's full arm set), applying the ratio to sec 4's Mac mid estimate:**

| mode | Mac (2 threads) | cpx22 (7.0-9.8x) | cx43 (2.8-4.2x) |
|---|---|---|---|
| ABSENT mid (5.98h) | 5.98h | 42-59h | 17-25h |
| GROUNDED mid (6.94h) | 6.94h | 49-68h | 19-29h |

**Practical consequence:** at these per-item wall times, a single per-seed queue item (all 16-18 arms) would very likely need the split the draft's sec 11 v2 arithmetic already flagged as **open item O8** ("If an item exceeds the fleet's item budget, split each trapped seed into two items... open item O8 for `/queue-experiment`") -- this re-measurement makes O8 apply to EVERY seed, benign or trapped, not only trapped ones, and probably needs splitting into more than two items per seed given cx43's own 19-29h estimate. Not decided here; named for `/queue-experiment` and the user.

## 6. What this changes, what it doesn't

- **Y5 is closed as originally scoped** (an INT arm was timed with W4 ON and OFF on the pinned branch head) but the number it produces is a small, noisy, direction-inconsistent delta (sec 3), not the multiplier correction that actually matters.
- **The load-bearing correction is P2 (sec 1):** the v3b/v3c cost table's `1.2/1.3/1.4x` INT trainer multiplier is revised to **roughly 2.3-4.1x** measured directly against the full built roster (E1, E2Self, HarmEval, W3, W6a, W1 codec) at production batch sizes, no W4 required to see the gap.
- **Total CPU-h for A1 (24 seeds, before screen/reserves) revises from ~23.5/26.6 CPU-h mid to ~144/167 CPU-h mid (ABSENT/GROUNDED)**, roughly 6x higher, with reserves and screen pushing the ABSENT/GROUNDED mid totals to roughly 170-200 CPU-h.
- **Not done / open for whoever picks this up:** (a) INT-ACT (ASP) was not timed -- CODEC's cost stands in as an unverified upper-bound proxy; (b) the W4 ON/OFF isolation needs a paired same-agent toggle over >=1,200 ticks to resolve the sign disagreement in sec 3; (c) a NATIVE remeasurement under `train_mode=False` (matching the deployed arm) would let this document's INT/NATIVE multiplier be quoted as an independent cross-check of RT-5's own numbers, which it currently cannot be (sec 2 caveat).
- **User-owned decision this surfaces (not decided here):** at ~150-200 CPU-h for 24 seeds before reserves, A1 is a materially larger commitment than previously believed. Whether to proceed at this cost, trim the arm set (O13's reseed-arm saving, ~35-40% per the draft, is still available and now worth more in absolute terms), or wait for a paired W4 remeasurement first, is for the user / `/queue-experiment`.

## 7. Reproduction

- Worktree: `git -C ree-v3 worktree add --detach .scratch/wt-a1cost origin/integration/coupled-loop-repair` (sha `1b013d613b3e00fc7fbf8bd414dca1cb1d388308`, tag `archive/coupled-loop-repair-1b013d6`).
- Probe: `.scratch/breakthrough-20260924/a1cost/a1cost_probe.py --seed <902|901> --wt .scratch/wt-a1cost --out <path> --ticks 300 --config <native|int_codec_w4off|int_codec_w4on>`. ~26-106s per invocation on the Mac at 2 threads.
- Raw JSON: `.scratch/breakthrough-20260924/a1cost/results/{native,int_w4off,int_w4on}_s{902,901}.json`.

## 8. 2026-09-26 addendum: paired same-agent W4 toggle (resolves sec 3's CANNOT_DETERMINE) + INT-ACT (ASP) direct timing

- **Status: MEASUREMENT ONLY, timing, no science readout.** Session `bt0926-a1cost2` (`orchestrate-20260924-breakthrough-c2`), chip_ref `chip-20260926-a1-cost-paired-w4-intact`. Written 2026-09-26T05:52Z. Answers the two "Not done" items sec 6 of this doc left open: (b) the paired W4 isolation, (a) direct INT-ACT timing (previously a CODEC-cost proxy).
- **Code:** same pinned sha as sec 1-7, `ree-v3` `1b013d613b3e00fc7fbf8bd414dca1cb1d388308` (tag `archive/coupled-loop-repair-1b013d6`), fresh throwaway detached worktree `.scratch/breakthrough-20260924/a1cost2/ree-v3-wt` (own copy, not the prior session's). No `ree_core` edits.
- **Evidence domain: D1** (wall-clock cost of native code paths under controlled configs; the paired design additionally reaches D0 on the mechanism -- see below).

### 8.1 Premise re-measured before designing the probe

The prior CANNOT_DETERMINE (sec 3) named two structural causes: (i) W4's extra scorer calls fire only on a gated cadence, diluted by episode-reset variance; (ii) W4 ON/OFF were **independent constructions** (separate `REEAgent`s, separate RNG streams), so per-seed noise was not cancelled. This addendum removes cause (ii) directly (same agent, live toggle) and reduces cause (i)'s sampling noise (2400 ticks vs 300, i.e. 8x the samples per seed).

**Mechanism confirmed by code read (D0), not merely assumed:** `ree_core/predictors/e3_selector.py:1834` reads `getattr(self.config, "use_e3_discounted_aggregation", False)` on **every** `score_trajectory()` planned-read call -- not cached at construction. `ree_core/agent.py:410` constructs `self.e3 = E3TrajectorySelector(config.e3, self.residue_field)` and `agent.py:403` sets `self.config = config` **by reference**, so `agent.config.e3` and `agent.e3.config` are the same `E3Config` object. Consequence: setting `agent.config.e3.use_e3_discounted_aggregation = True/False` between blocks on one constructed `REEAgent` takes effect on the very next tick, with no rebuild and no RNG discontinuity -- verified working, not merely reasoned about (see sec 8.2 results: clean monotone direction on both seeds).

### 8.2 Paired W4 toggle: design and results

One `REEAgent` per seed (`int_codec_w4off`-style config: full trainer roster -- E1, E2Self, E2World/W3, WorldEncoder/W6a, Codec/W1 -- production defaults, same as sec 2), 8 alternating blocks of 300 ticks each (OFF,ON,OFF,ON,OFF,ON,OFF,ON = 1,200 ticks/condition, 2,400 ticks total), same two seeds as sec 2-3 (902 benign, 901 hazard_trapped). Mac CPU lock: two holds, `bt0926-a1cost2` 05:05:48Z-05:19:11Z (seed 902, ~13m23s) and 05:25:06Z-05:39:23Z (seed 901, ~14m17s), both under the 15 min cap, 45s+ pause between (contended by other sessions -- `bt0926-emasib`, `bt0926-gatec3` -- both before and between my holds; `ps` showed no other heavy process running **during** either of my own holds, checked immediately before each run started).

| seed (stratum) | OFF pooled s/tick (1200 ticks) | ON pooled s/tick (1200 ticks) | **W4 multiplier** |
|---|---|---|---|
| 902 (benign) | 0.3044 | 0.3459 | **1.136x** |
| 901 (hazard_trapped) | 0.3245 | 0.3714 | **1.145x** |

**Both seeds now agree in direction and magnitude: W4 ON costs ~13.6-14.5% more than W4 OFF (mean 1.140x), a narrow spread across seeds.** This resolves sec 3's CANNOT_DETERMINE. Per-block s/tick ranged 0.267-0.397 (see raw JSON) -- noisier than the pooled figure, consistent with sec 3's own diagnosis that per-episode/per-block noise is real but now averages out cleanly at N=1,200/condition with the construction confound removed.

Note for calibration: these paired per-tick costs (OFF ~0.30-0.32) run somewhat lower than sec 3's own **unpaired** `int_codec_w4off` measurement on the same seeds/config (0.3482/0.3481, 300 ticks each) -- a ~10-13% difference plausibly reflecting normal run-to-run wall-clock variance (JIT/allocator warmup, episode-count luck at only 300-1200 ticks) rather than a code difference (config is identical). The **ratio** (ON/OFF), not the absolute magnitude, is this section's load-bearing output.

### 8.3 INT-ACT (ASP) direct timing vs INT-CODEC and NATIVE

Config per `coupled_a1_preregistration_draft_20260925.md` line 254 (W6 preset + `use_action_space_proposals=True`; `action_space_first_action_mode` defaults `"stratified"`, `action_space_cem_score_horizon` defaults `None` -> standard CEM window, `use_action_class_scaffold_candidates` defaults `False` -- all exactly the draft's spec, confirmed against `ree_core/utils/config.py:3018-3054` on this pinned sha). Same trainer roster as INT-CODEC minus the codec group (no `waking_trainer_codec_enabled`, no `use_codec_bounded_decode`/`use_codec_iter0_image_match` -- codec and prior members not registered, matching the draft's "INT-ACT keeps `action_object_decoder`/`terrain_prior` constructed but off the act path"). 300 ticks/seed, single Mac CPU lock hold `bt0926-a1cost2` 05:45:04Z-05:48:21Z (~3m17s), no contending process observed.

| seed | INT-ACT s/tick | INT-CODEC (W4 off, sec 3) s/tick | **ACT/CODEC ratio** |
|---|---|---|---|
| 902 (benign) | 0.2588 | 0.3482 | **0.743** |
| 901 (hazard_trapped) | 0.2940 | 0.3481 | **0.845** |

**INT-ACT costs 74-85% of INT-CODEC's per-tick cost -- cheaper, as the draft assumed ("ACT costs at most INT-CODEC's per step"), and now verified rather than assumed.** This means sec 4's use of CODEC's cost as a proxy for *all* non-NATIVE arms was conservative (an overestimate) for the INT-ACT-family arms specifically, not an underestimate -- the opposite direction of risk from the W4 gap.

**INT-ACT was not itself paired-toggle tested for W4** (out of this session's time budget). The W4 multiplier is a generic E3-selector-level effect -- `score_trajectory()`'s discounted-aggregation branch (`e3_selector.py:1834`) fires identically regardless of how the trajectory pool was proposed (codec-decoded vs ASP), and both variants run the same K x I = 96 rollouts per E3 tick (`coupled_a1_preregistration_draft_20260925.md` line 627) -- so sec 8.2's measured multiplier (mean 1.140x) is applied to INT-ACT's own measured OFF cost as a **grounded proxy**, not an invented number, but it is an extrapolation, stated as such, and a direct paired-ACT measurement remains open for whoever picks this up next.

### 8.4 Revised A1 total (deployed setting: W4 DISC_0.5 ON)

Model change from sec 4: instead of one pooled "INT arm" figure mixing CODEC/ACT and W4 on/off indiscriminately, this addendum splits by **family** (CODEC vs ACT -- each is 6 arms/seed in ABSENT mode, 7 in GROUNDED, confirmed by counting `coupled_a1_preregistration_draft_20260925.md`'s per-family arm rows: base + SHUF + FROZEN + R1 + NOBABBLE + BABBLE-DATA = 6, +NOVAL = 7 GROUNDED) and applies the now-resolved W4-ON per-tick cost to each family, extrapolated to RT-5's 5,400-tick full arm length:

| family | per-arm wall, low/mid/high (5,400 ticks) |
|---|---|
| INT-CODEC (W4 ON, directly measured via sec 8.2) | 0.519h / 0.538h / 0.557h |
| INT-ACT (W4 ON, measured-OFF x sec-8.2 multiplier) | 0.441h / 0.473h / 0.505h |

NATIVE-family unchanged (RT-5: 123s/180s/439s low/mid/high per arm, sec 4).

**Revised per-seed wall** (4 NATIVE + 6 CODEC + 6 ACT arms ABSENT; 4 NATIVE + 7 CODEC + 7 ACT arms GROUNDED):

| mode | low | mid | high |
|---|---|---|---|
| ABSENT | 5.90h | 6.27h | 6.86h |
| GROUNDED | 6.86h | 7.28h | 7.92h |

**24 admitted seeds (before screen/reserves):**

| mode | low | mid | high |
|---|---|---|---|
| ABSENT | **141.5 CPU-h** | **150.4 CPU-h** | **164.6 CPU-h** |
| GROUNDED | **164.5 CPU-h** | **174.6 CPU-h** | **190.1 CPU-h** |

**+ screen** (unchanged, ~0.7-2.5h, NATIVE-only) **+ reserves** (4 extra seeds at the mid per-seed rate: +25.1h ABSENT, +29.1h GROUNDED): **total ABSENT ~177 CPU-h mid, GROUNDED ~205 CPU-h mid** (was ~169-177h / ~193-201h in sec 6; the mid figure moves up modestly, ~2-5%, now that it reflects the deployed W4-ON cost cleanly rather than an ambiguous on/off mix -- the **high** band is essentially unchanged (6.86h vs 6.86h ABSENT-per-seed) because sec 4's "high" happened to already sit near a W4-ON value; the **low** band moves up more (~35%) because sec 4's "low" was an artifact of one noisy low-episode-count block, not a real family-level floor).

**What this changes, what it doesn't:**
- **Sec 3's CANNOT_DETERMINE is resolved:** W4 ON costs ~13.6-14.5% more than OFF, consistent direction and magnitude across both seeds (mean 1.140x), via a same-agent paired toggle that removes the independent-construction confound.
- **INT-ACT's cost is now directly measured, not assumed:** it is cheaper than INT-CODEC (74-85% of its per-tick cost), confirming the draft's own upper-bound assumption was directionally safe.
- **The revised mid total (~177h ABSENT / ~205h GROUNDED) is close to sec 6's prior mid estimate** (a few percent higher) -- this addendum sharpens the number and its provenance, it does not overturn A1's cost picture a second time.
- **Not done / open:** (a) a direct paired W4 toggle on the INT-ACT family itself (this addendum's ACT-family W4-ON figure is CODEC's measured multiplier applied to ACT's own measured OFF cost, not a direct paired-ACT measurement); (b) the sec 2 NATIVE `train_mode=False` remeasurement remains open, unaffected by this addendum.
- **User-owned decision (not decided here):** none new -- sec 6's framing (proceed at ~150-200 CPU-h/24 seeds, trim the arm set via O13, or wait) stands, now with a firmer number underneath it.

### 8.5 Reproduction

- Worktree: `git -C ree-v3 worktree add --detach .scratch/breakthrough-20260924/a1cost2/ree-v3-wt archive/coupled-loop-repair-1b013d6` (same sha as sec 7).
- Paired-toggle probe: `.scratch/breakthrough-20260924/a1cost2/paired_w4_probe.py --seed <902|901> --wt .scratch/breakthrough-20260924/a1cost2/ree-v3-wt --out <path> --block-ticks 300 --n-blocks 8`. ~780-840s per seed on the Mac at 2 threads.
- INT-ACT probe: `.scratch/breakthrough-20260924/a1cost2/intact_probe.py --seed <902|901> --wt .scratch/breakthrough-20260924/a1cost2/ree-v3-wt --out <path> --ticks 300 --config <native|int_codec|int_act>`.
- Raw JSON: `.scratch/breakthrough-20260924/a1cost2/results/{paired_w4_s902,paired_w4_s901,int_act_s902,int_act_s901}.json` (kept in `.scratch`, not committed alongside -- small scripts, cite absolute worktree paths, matching sec 7's precedent).
