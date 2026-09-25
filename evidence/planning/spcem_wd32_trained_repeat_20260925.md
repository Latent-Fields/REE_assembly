# SP-CEM zero-continuation check -- wd32 trained repeat (2026-09-25)

Session `bt0925-spcem2`, chip `chip-20260925-spcem-wd32-trained-repeat`, orchestrator `orchestrate-20260924-breakthrough`.
Code refs are file:line at **ree-v3 origin/main `2801c3e`** (detached throwaway worktree; the first probe ran at `1a61800`, which is now behind origin -- the driver's `SELF_DIM`/`WORLD_DIM`/`WARMUP_EPISODES`/`STEPS_PER_EPISODE` constants and the `_build_action_class_scaffold_candidates` construction are unchanged at `2801c3e`, checked below).

**Status: PRE-REGISTERED, run pending.**

## 0. Purpose and premise re-measurement

`spcem_zero_continuation_check_20260925.md` (`847544ac8e`) found, at toy dims
(self_dim = world_dim = 16, 20 warmup episodes x 100 steps), that the default-ON
SP-CEM floor token loses E3's ranking by **construction** (unit one-hot step-0 +
exact-zero tail, 5-7x the decoder's real scale), not by pool-imbalance order
statistics: native token rank 31.00/31.00/31.00 (3/3 seeds, 85/85 token states),
majority-class tokens built the same way also rank last, and an on-manifold
class-c candidate (`pm_bt`) ranks 0.00/7.53/2.06. Its own "Next single action"
names this exact follow-up: repeat at world_dim 32 (deployed) with the full
V3-EXQ-1061 warmup (trained agent) before any default change.

**Premise re-measured against `2801c3e` (this worktree, not `1a61800`):**
- `_build_action_class_scaffold_candidates` (one-hot(cls) at step 0, zeros at
  steps 1..H-1) -- present, same construction. `grep -n "actions\[:, 0, cls\] = 1.0"
  ree_core/hippocampal/module.py` -> one hit.
- `SELF_DIM = WORLD_DIM = 16` in `experiments/v3_exq_1061_mech131_anticipatory_residue_lesion.py`
  (module-level constants, read directly by `build_agent`) -- **confirmed still 16**,
  i.e. the deployed dim (32) has never been the dim this driver actually runs at;
  this probe monkeypatches them to 32 in-process (no file edit) per the brief.
- `WARMUP_EPISODES = 600`, `STEPS_PER_EPISODE = 200` (1061's own numbers, "042's
  own numbers, not new ones", driver comment) -- confirmed. The first probe used
  20 x 100 (1/60th of 1061's own warmup by step count), which is the gap this
  repeat closes.
- GFLAG-0555 (claim ARC-065, `stale_note`) carries F2/F3/F5 from the first probe
  and is still open; this record's result is additional evidence for that flag,
  not a new one, unless the result reverses the finding (sec 4).
- W1 codec build (`w1_codec_build_20260925.md` F2): the fixed SP-CEM `ao_std`
  floor (0.2, absolute, per-dim) sets the sample scale on CEM iterations 1-2.
  Relevant context (the token's one-hot magnitude is compared against that same
  floor-governed real-candidate scale) but **the codec branch is explicitly NOT
  under test here** -- this run is on `origin/main`, no codec knobs exist there.

## 1. Design (unchanged from the first probe except dims + warmup)

**Changed, ONLY:**
1. `self_dim = world_dim = 32` (deployed), monkeypatched on the imported driver
   module (`X.SELF_DIM = X.WORLD_DIM = 32`) before `build_agent()` is called --
   no edit to the driver file or `ree_core`.
2. Warmup = the full 1061 schedule, **600 episodes x 200 steps**, per seed --
   or the largest warmup that fits ~25 min Mac wall for that seed, sized from a
   short calibration run at the deployed dims and recorded per seed if shrunk
   (contingency stated up front per the brief; actual episode counts used are
   reported in sec 3, not assumed here).

**Unchanged:** 3 seeds (11/23/37), the 8-arm design (control / hold / sampled /
oh_bt / pm_z / pm_bt / maj_oh_z / maj_oh_bt -- see the first probe's sec 2 ARMS
table for definitions), 40 probe states along a random walk per seed, the bare
`e3.select` path (matches the full agent path per Worker C, not re-checked here),
the `control_rebuilt_matches_native` drift check, `torch.set_num_threads(2)`,
one process. Script: `probes/spcem2/probe_spcem_wd32_trained.py` (reuses the
first probe's `probe_spcem_zero_continuation.py` structure verbatim except for
the two changes above; both scripts import 1061's `build_agent`/`warmup_train`
from the same throwaway-worktree pattern).

**Readouts (as before, plus one addition named in the brief):**
- Token E3 rank vs the 31 fixed candidates, per arm (mean, frac beats majority
  best/mean, frac argmin/selected is token).
- Native selection rate of the token's class (via `selected_class`, arms
  `control` vs `hold`).
- **Added:** the token's first-step norm vs the real candidates' decoded step-0
  norm (`token_step0_norm` vs `real_step0_norm_mean`) -- the deployed-dim analogue
  of the first probe's "5-7x the decoder scale" finding, measured at dim 32
  rather than inferred from the dim-16 numbers.

**Decision question:** does the construction finding (the token loses by
construction -- off-manifold one-hot head + zero tail -- not by order statistic
over an exchangeable pool) SURVIVE the deployed dim + a fully warmed-up agent,
weaken, or reverse? Domain assigned per finding (D1 for rank/construction facts,
D2 for the arm-swap interventions on the native E3 consumer).

## 2. Mac CPU lock protocol

One seed per lock hold (`mkdir .scratch/breakthrough-20260924/mac_probe.lock`,
owner file, retry 30 s, never break a lock < 45 min old or with a live owner).
A short calibration run (5 episodes x 200 steps at dim 32, throwaway agent, same
lock discipline) precedes seed 11's hold to size the warmup budget empirically
rather than by extrapolation from the dim-16 timing (76-106 s for 2000 steps in
the first probe; dim-32 per-step cost is not assumed equal).

## 3. Results

*(filled in after the runs; this section is committed as a placeholder so the
design above is pre-registered before any seed executes)*

## 4. Reading

*(filled in after the runs)*
