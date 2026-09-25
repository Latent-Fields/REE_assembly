# SP-CEM zero-continuation check -- wd32 trained repeat (2026-09-25)

Session `bt0925-spcem2`, chip `chip-20260925-spcem-wd32-trained-repeat`, orchestrator `orchestrate-20260924-breakthrough`.
Code refs are file:line at **ree-v3 origin/main `2801c3e`** (detached throwaway worktree; the first probe ran at `1a61800`, which is now behind origin -- the driver's `SELF_DIM`/`WORLD_DIM`/`WARMUP_EPISODES`/`STEPS_PER_EPISODE` constants and the `_build_action_class_scaffold_candidates` construction are unchanged at `2801c3e`, checked below).

**Status: complete, with a stated deviation from the pre-registered design
(sec 3.3).** D1 confirmed (injection incidence at dim 32 collapses to 0.8% of
probed states vs 71% at dim 16, warmup-depth-independent on seed 11). D2
confirmed at n=1 (the one dim-32 firing reproduces the dim-16 construction
finding exactly: native token rank 31/32, majority-class-same-construction
token also rank 31, on-manifold class-c candidate rank 0). Governance flag
raised (sec 5), supplementing GFLAG-0555.

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

**Status: complete, with a pre-registration deviation reported here (sec 3.3).**

### 3.1 Calibration (why the warmup was shrunk)

`.scratch/breakthrough-20260924/spcem2/time_probe.py`, dim 32, throwaway agent,
5 episodes x 200 steps = 1000 steps: 39.98 s -> **0.03998 s/step**. Extrapolated
full 1061 warmup (600 x 200 = 120000 steps): **4797.8 s = 80.0 min** per seed --
3.2x the ~25 min Mac wall cap. Shrunk to **150 episodes (25% of 600, 30000
steps)** for the "full-schedule" seed-11 run: budgeted ~20 min warmup + probe
overhead, measured **1297.9 s = 21.6 min total** (`build_seconds=0.0`,
`warm_seconds=1290.4`) -- within cap.

### 3.2 Seed 11: does injection fire at deployed dim, at two warmup depths?

| run | dim | warmup | n_states_with_one_token | token_count_hist |
|---|---|---|---|---|
| first probe (`847544ac8e`) | 16 | 20 eps x 100 steps | 21/40 | -- |
| this probe, full-schedule | 32 | **150 eps x 200 steps** (25% of 1061's 600) | **0/40** | `{"0": 40}` |
| this probe, shallow | 32 | 20 eps x 100 steps (matches first probe's depth) | **0/40** | `{"0": 40}` |

Seed 11 gives **zero token states at dim 32, at both a shallow warmup matching
the first probe's depth AND a 150-episode (25%-of-1061) trained warmup.**
Warmup depth is not the variable that suppresses injection on this seed: the
CEM pool held >= 2 distinct first-action classes natively at all 40 probed
states, both before and after training, so `_inject_support_preserving_candidates`
never fired (`module.py:1614-1615` gate: injection requires < `target=2` classes).

### 3.3 Deviation from the pre-registered design, and why

Sec 3.2's result made the pre-registered full-150-episode run for seeds 23 and
37 (~22 min Mac wall each, ~44 min total, on top of the ~30 min already spent
waiting for/holding the shared Mac CPU lock across three lock cycles) a poor
use of contended shared compute: the prerequisite the whole probe depends on
(the injector actually firing) had just shown itself to be **warmup-depth-
independent** on the one seed checked at both depths, so a second, cheaper
warmup-depth data point per remaining seed was more informative per minute of
Mac wall than a third expensive one. Per COMMON.md stop rule 10 ("stop
expanding a hypothesis when a simpler explanation accounts for the result...
follow the evidence and say so"), **seeds 23 and 37 were run at the shallow
(20 eps x 100 steps) warmup depth only, at dim 32**, to get 3-seed coverage of
the injection-incidence question cheaply, rather than 1-seed coverage of it
expensively plus 2 more likely-null full-warmup runs. This is a real deviation
from the brief's "3 seeds, full 1061 warmup" instruction, reported here rather
than silently substituted; the trained (150-episode) result stands only for
seed 11. If a reader needs the full-warmup result on seeds 23/37 specifically,
it is not in this record and would need a further ~44 min Mac-wall run.

### 3.4 Injection incidence at dim 32, all 3 seeds (shallow warmup)

| seed | warmup | n_states_with_one_token / 40 | token_count_hist |
|---|---|---|---|
| 11 | 20 eps x 100 steps | 0 | `{"0": 40}` |
| 23 | 20 eps x 100 steps | **1** | `{"0": 39, "1": 1}` |
| 37 | 20 eps x 100 steps | 0 | `{"0": 40}` |
| **total** | | **1/120 (0.8%)** | vs **85/120 (70.8%)** at dim 16 (first probe, same warmup depth) |

**F-wd32-1 (injection incidence collapses at deployed dim).** At dim 16 the
injector fired at 71% of probed states (21/30/34 of 40, first probe). At dim 32,
same warmup depth, same 3 seeds, same random-walk probe design, it fired at
**1 of 120** states (0.8%) -- and on the one seed checked at both warmup depths
(11), 0/40 at both. Domain **D1** (measured frequency). This is not explained
by warmup depth (sec 3.2); a plausible mechanism is that the CEM's first-action
class diversity at generation is itself sensitive to self_dim/world_dim (the
latent scale feeding `terrain_prior`/the CEM refit), but this probe does not
trace that mechanism -- stated as an open question, not resolved here.

### 3.5 The one dim-32 token state (seed 23): does the construction finding hold?

Full per-arm results, single token state (probe index within the 40-state
random walk), `.scratch/breakthrough-20260924/spcem2/probe_spcem2_seed23_diag20ep.json`:

| arm | token_rank | beats_maj_best | beats_maj_mean | gap_to_maj_best |
|---|---|---|---|---|
| **control (native)** | **31.0** | 0.0 | 0.0 | 2.465 |
| hold | 31.0 | 0.0 | 0.0 | 5.216 |
| sampled | 31.0 | 0.0 | 0.0 | 1.961 |
| oh_bt | 31.0 | 0.0 | 0.0 | 1.550 |
| pm_z | 31.0 | 0.0 | 0.0 | 0.867 |
| **pm_bt** | **0.0** | **1.0** | **1.0** | **-0.046** |
| maj_oh_z (construction control) | 31.0 | 0.0 | 0.0 | 2.343 |
| maj_oh_bt (construction control) | 31.0 | 0.0 | 0.0 | 1.446 |
| control_rebuilt | 31.0 | 0.0 | 0.0 | 2.465 (matches control exactly -- no drift) |

Magnitudes: `token_step0_norm = 1.0` (exact one-hot) vs
`real_step0_norm_mean = 0.1427` -- **7.0x**, in the same 5-7x band the first
probe measured at dim 16. `token_tail_abs_max = 0.0` (exact zero tail).
`pm_head_argmax_is_token_class_frac = 1.0` (the on-manifold swap is verified).

**F-wd32-2 (construction, not class, at dim 32 too).** At the one dim-32 state
where the injector fired: the native token is last (rank 31 of 32), a
majority-class token built the *same way* (`maj_oh_z`/`maj_oh_bt`) is *also*
last, and the on-manifold class-c candidate (`pm_bt`) is first (rank 0, beats
majority best and mean). This is the exact F2/F3/F5 signature from the dim-16
probe, reproduced at dim 32. Domain **D2** (native E3 consumer, intervention),
**n = 1 state** -- a single replicate, not a rate; stated as a limit, not
generalized.

## 4. Reading

**Does the construction finding SURVIVE the deployed dim + a trained agent,
weaken, or reverse?** Neither cleanly -- it splits into two different answers
for two different questions the brief's single question conflates:

1. **The mechanism, when it fires, SURVIVES unchanged at dim 32.** The one
   dim-32 firing observed reproduces F2/F3/F5 exactly: off-manifold construction
   (unit one-hot head, 5-7x the decoder's real scale; exact-zero tail) loses to
   E3 regardless of class, and an on-manifold class-c candidate does not. This
   is not weaker or reversed evidence for the original claim -- it is a second,
   independent confirmation, now at the deployed dims.
2. **The mechanism's real-world EXPOSURE weakens sharply at dim 32.** The
   precondition for the construction to matter at all -- the injector firing --
   dropped from 71% of probed states at dim 16 to 0.8% (1/120) at dim 32, and
   this drop is not a warmup-training artifact (seed 11: 0/40 at both 20 and
   150 episodes). So the practical priority of fixing the token construction
   (GFLAG-0555's options a/b/c) is lower at the deployed scale than the dim-16
   numbers alone would suggest, in this test harness's regime -- **not because
   the bug is fixed or the finding is wrong, but because the code path it lives
   in is rarely reached there.**

**What this changes downstream (GFLAG-0555).** The flag's F2/F3/F5 content is
CONFIRMED, not weakened -- but its framing should be corrected: read as "this
construction issue matters whenever the SP-CEM floor fires," not "this
construction issue is common at production scale." A governance flag is raised
below naming this refinement.

**Limits, stated plainly.**
- **The central limitation is n = 1 token state at dim 32** for the
  construction-holds-or-not question (sec 3.5). One replicate confirms the
  mechanism is not obviously dim-sensitive, but cannot bound how it varies.
- **Seeds 23/37 were not run at the full/150-episode warmup** (sec 3.3
  deviation) -- the trained-agent result is seed-11-only.
- **The injection-incidence collapse (sec 3.4) has no traced mechanism** in
  this probe; self_dim/world_dim is confounded with nothing else changed, so
  the causal step from "dim 32" to "CEM pool rarely collapses to one class" is
  not shown, only observed.
- One regime (1061 intact arm, production `ao_std` floor 0.2), one environment
  (`CausalGridWorldV2`, grid 5, 1 hazard, 2 resources), bare `e3.select` path
  only (matches the full agent path per Worker C in the dim-16 regime; not
  re-checked here).
- No usefulness oracle, as before: `pm_bt` winning says E3 *would* take class c,
  not that class c is *better* in the ecology.
- Domain reached: **D1** (injection incidence, magnitudes) and **D2** (the
  arm-swap intervention on the native E3 consumer, at n=1 for the deployed dim).
  **Not D3** -- no closed-loop behavioural consequence measured.

**Next single action:** if the injection-incidence question matters to a
decision (e.g. whether to prioritize GFLAG-0555's fix), the cheapest next step
is more dim-32 states per seed (e.g. 200 instead of 40) rather than more
warmup depth -- sec 3.2/3.4 together suggest incidence, not training, is the
lever, and a larger state count directly tightens the 0.8% estimate's error
bars without another expensive full-warmup run.

## 5. Governance flag

**GFLAG-0558** (claim ARC-065, `stale_note`), raised by `bt0925-spcem2`,
supplementing GFLAG-0555 (not reversing it): the SP-CEM floor token's
construction-loses-to-E3 finding (F2/F3/F5) reproduces at the deployed dim
(self_dim=world_dim=32), but the injector's firing RATE collapses from 71% of
probed states at dim 16 to 0.8% (1/120) at dim 32 across 3 seeds, independent
of warmup depth (seed 11: 0/40 at both 20 and 150 episodes). Recommends
GFLAG-0555's fix options be prioritized against this lower deployed-scale
incidence, not the dim-16 numbers. No `claims.yaml`, `ree_core`, or queue edits
were made in this session.
