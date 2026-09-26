# H3 probe pre-registration: does ending babbling on the organism's own learning progress
develop the E2 world head as well as a fixed 2,400-step epoch, and does the timing carry
information?

- **Written:** 2026-09-26T15:4X Z. Session `bt0926-dch3` (Worker DCH3,
  `orchestrate-20260924-breakthrough-c2`), chip_ref `chip-20260926-dcd2-h3-babble-end`.
- **Spec:** H3 in `evidence/planning/dynamic_control_audit_20260926.md` (e3cafebab3), sec B.
  DRAFT-DCD-2 (`/governance` candidate) names the same unowned decision.
- **Scope:** a Mac probe only. Harness-side. No `ree_core` edit, no queue entry, no chip
  spawned, no `claims.yaml` edit. Pre-registered **before** the 5 registered seeds run
  (COMMON rule; this file is committed before `--dry-run` is dropped and the real seeds
  start).
- **Code:** `ree-v3` `archive/coupled-loop-repair-4070b0e`
  (`4070b0efa4e51a0a837228bb4f3b4564c19185ca`), checked out as a private detached worktree
  at `/Users/dgolden/REE_Working/.scratch/wt-dch3`. This commit carries the current W3
  contract: member gate (a) is `disc4_h1 >= 0.47` **alone** (the `k == 10` conjunct was
  dropped 2026-09-26, `tests/contracts/test_w3_e2_world_member.py` W3-10/W3-10b). The
  source switch is `waking_trainer.py:771` `WakingTrainer.set_e2_world_source`.
- **Probe script:** `.scratch/breakthrough-20260924/dch3/h3_probe.py` (this repo's copy at
  `evidence/planning/probes/dch3/h3_probe.py` if landed alongside this record; otherwise
  cited by path only, per the worker brief's "otherwise leave them in `.scratch` and cite
  them").

## 1. Hypothesis and arms (verbatim from the audit spec)

**Hypothesis.** A babbling epoch ended by the organism's own learning progress develops the
E2 world head at least as reliably as a fixed epoch, and the information comes from the
*timing*, not from the *duration*.

**Trigger information available to REE.** The E2WorldMember's own training loss on its
babble stream (no held-out labels). Learning progress LP is the slope of a slow EMA of that
loss. Babbling ends when LP falls below a pre-registered fraction of its early value for a
pre-registered dwell.

**Controlled variable.** The babbling source switch (`set_e2_world_source("babble" ->
"on_policy")`), and so the epoch length (how many raw babble ticks land in the FROZEN
retained set before the switch).

- **A (imposed):** a fixed 2,400 steps (12 episodes) -- the campaign's ungrounded constant
  (A1 open item O9).
- **B (endogenous):** end at the LP plateau (rule in sec 3 below).
- **C (wrong-reason):** each seed's duration equals **another** seed's arm-B duration -- a
  fixed cyclic derangement across the 5 registered seeds (seed `i` gets seed `(i+1) mod 5`'s
  arm-B stop tick). Information about *that* seed's own learning trajectory is absent;
  only the duration distribution is matched (ARC-156 F2 logic: information vs duration).
- **D (oracle ceiling):** end at the first checkpoint where a held-out disc4 read of the
  **online, continuously-trained** head first crosses the bar (sec 3).

## 2. Deviations from the audit's literal design, and why (state them, don't bury them)

The audit's B.0 design rules ask for these arms **as a three/four-arm comparison of babble
duration only**, everything else held fixed. Two engineering decisions were needed to make
that runnable on the Mac at probe scale; both are stated here rather than discovered later.

1. **Two-phase design: "monitor" (decide the stop tick) then "score" (consolidate and
   evaluate), per seed.** A single online run cannot use a fixed post-babble consolidation
   dose (needed so arms differ only in retained-buffer *contents*, not in *how much total
   training* they received) while also being the thing whose loss stream decides when to
   stop. So:
   - **Monitor** (once per seed): babble **with** continuous training (`tr.every_k = 1`,
     one update per tick once the retained buffer reaches batch size 32), logging the
     member's own loss and, at each 200-tick (episode) checkpoint, a cheap held-out disc4
     read of the *current, online-trained* head. This determines stop_A (fixed), stop_B
     (LP rule) and stop_D (oracle) and nothing else -- its trained head and buffer are
     discarded afterward.
   - **Score** (once per seed x arm): re-run the **same** babbling stream **without**
     training (`tr.every_k = 10**9`, exactly the vendored N2 babble-phase behaviour) for
     that arm's stop-tick number of ticks, building the retained buffer that a run which
     really stopped there would hold. Then a **fixed** consolidation dose from the INIT
     head (`C_DOSE` offline updates, mirroring the vendored `PRE_UPDATES` step) and a
     **fixed** post on-policy phase, identical across arms.
   - **Why the monitor and score retained buffers are bit-identical up to a shared tick,
     so this substitution is not a confound:** `E2WorldMember.observe()` records raw
     observations from `agent._current_latent` / `agent._last_action`, both produced by
     `agent.sense()` / the babbler -- neither reads `agent.e2.world_transition` or
     `world_action_encoder` (the only tensors the member trains). Training the head during
     monitor therefore has zero causal reach into what gets recorded. `WakingTrainer._update`
     draws its replay-batch randomness from a **private, forked** torch RNG
     (`torch.random.fork_rng`, initialised from `config.waking_trainer_seed`, never set
     here so it is always seed 0 for every fresh `WakingTrainer`) -- so per-step training
     draws never perturb the global RNG the env/babbler/encoder use. Given the same
     `seed_all(seed)` at the top of both phases, the env (`CausalGridWorldV2(seed=seed*160+k)`)
     and `StructuredBabbler(seed=seed*13+1)` reproduce an identical action/observation
     stream in both phases. This was **not measured** on this probe (a code read, D0); if a
     future check needed to verify it, the mechanical test is: run monitor and score to the
     same tick and assert their retained buffers are byte-identical (not done here for time;
     flagged as a limit in sec 6).
   - **Consequence for interpretation:** this probe measures the effect of retained-buffer
     *duration and content* on the post-consolidation head, using each seed's own babble
     trajectory as ground truth for what the organism's LP signal would have observed
     online. It does **not** measure a single online run that both decides its own stop
     point and is scored on that same partially-trained head -- that is a harder, closer-
     to-deployment design and is named as a follow-on in sec 6.
2. **Probe-scale doses, smaller than the campaign's canonical W3 protocol** (N2's
   `PRE_UPDATES=3000`, `UPS=8`, `post=1200`): here `C_DOSE=1000`, `UPS_POST=4`,
   `POST_STEPS=400`. This trades absolute disc4 magnitude fidelity to the campaign's
   published numbers for probe-budget speed (COMMON rule 4: smallest config that answers
   the question). **Absolute pass rates from this probe are therefore not directly
   comparable to N2/W3's own published numbers**; only the **within-probe, across-arm**
   comparison is load-bearing, since every arm gets the identical dose.

## 3. Exact pre-registered rule and constants

- **Env / agent:** `CausalGridWorldV2` size 12, Phase-0 kwargs
  (`InfantCurriculumScheduler(grid_size=12).env_kwargs(0)`); `REEConfig.from_dims` with
  `world_dim=32` (deployed), `alpha_world=0.3` (default), and **all four EMA reset-init
  knobs ON** (`use_zworld_ema_reset_init`, `use_zself_ema_reset_init`,
  `use_shared_ema_reset_init`, `use_zharm_ema_reset_init` = True; brief line 9, campaign
  convention GFLAG-0559).
- **Held-out test set:** 3,000 uniform-random `{0,1,2,3}` steps (15 episodes, `k0=120`),
  encoded once per seed through the frozen encoder (`ref`).
- **Babbler:** `StructuredBabbler(n_classes=5, max_run=4, seed=seed*13+1)`.
- **E2WorldMember:** `lr=3e-4, batch_size=32, buffer_max=2000, retained_max=3500,
  replay_frac=0.25, reencode_window=0 (auto), replay_latent="reencode", objective="mse",
  grad_clip=1.0`.
- **Gate (a) (current W3 contract):** `disc4_h1 >= 0.47`, no `k` conjunct.
- **Monitor phase:** `MAX_STEPS=3200` (16 episodes, 1.33x arm A), checkpoint every 200
  ticks (episode boundary), cheap disc4 read at each checkpoint (`max_starts=100`).
  - **Slow EMA of the training loss:** `S_t = 0.01*L_t + 0.99*S_{t-1}` (`SLOW_ALPHA=0.01`,
    half-life ~69 ticks), updated only on ticks where a loss is available (`ready()` first
    true once the retained buffer reaches batch size 32, i.e. tick ~32).
  - **LP at checkpoint i** = `S` at checkpoint `i-1` minus `S` at checkpoint `i` (positive =
    loss falling = progress).
  - **LP_early** = LP at checkpoint index 1 (between ticks 200 and 400) -- the earliest LP
    value available with one full prior checkpoint behind it.
  - **Non-degeneracy precondition (checked, not assumed):** if `LP_early` is `None` or
    `<= 0`, arm B is **degenerate** for that seed -- report it explicitly and do not
    interpret arm B for that seed (COMMON stop rule 10); it is censored at `MAX_STEPS`.
  - **Stop rule (arm B):** the first checkpoint `i >= 2` such that `LP_i < 0.25 * LP_early`
    for **2 consecutive checkpoints** (`LP_FRAC=0.25`, `LP_DWELL=2`, i.e. a 400-tick
    plateau). If never met by `MAX_STEPS`, censored at `MAX_STEPS` (flagged).
  - **Stop rule (arm D, oracle):** the first checkpoint whose *online* head's disc4 read
    crosses `0.47`. If never met by `MAX_STEPS`, censored at `MAX_STEPS` (flagged).
- **Arm C:** the cyclic derangement of arm B's per-seed stop ticks (sec 1), computed only
  after all 5 seeds' monitor phases complete.
- **Score phase (all arms):** babble-replay without training for the arm's stop-tick number
  of ticks; `C_DOSE=1000` offline consolidation updates from the INIT head (`get_head`
  before any babbling); a fixed `POST_STEPS=400` (2 episodes) on-policy phase
  (`UPS_POST=4`, native `StepHarness`, `seed_all(seed+500)` before it, matching the
  vendored N2 convention) using env indices `k=50,51`, distinct from babble (`k=0..15`),
  the on-policy B0 baseline (`k=25..36`) and the held-out set (`k=120..134`).
- **B0 baseline (per seed, shared across arms):** 12 native on-policy episodes (2,400
  steps, `k0=25`, no babbling at all), then the **same** `C_DOSE=1000` consolidation from
  the INIT head, then a disc4 read -- exactly the vendored N2 B0 recipe, at the probe's
  reduced dose.
- **Seeds:** 5 fresh -- `901, 902, 903, 904, 905` (not overlapping any prior campaign seed
  set: 106-110, 531-535, 611-615, 721-725, 811-815).

## 4. DVs and falsifier (verbatim from the audit spec, operationalised above)

- **DVs:**
  - W3 gate (a) pass count per arm (`disc4_h1 >= 0.47`, evaluated on the **post**-phase
    head, matching N2's `gate_a` definition on `post_current`, not `pre`);
  - disc4 (pre and post);
  - retention (b): `(post_disc4 - B0_disc4) / (pre_disc4 - B0_disc4)`, guarded for a
    non-positive denominator (reported, not concealed, per the N2 red-team note F3);
  - `corr(arm-B duration, post-hoc time-to-bar)` -- Pearson r over the 5 seeds between each
    seed's arm-B stop tick and that seed's arm-D (oracle) stop tick, both from the monitor
    phase. **n=5 is too small for a reliable correlation estimate**; reported as a
    descriptive number with that caveat, not as a statistical test.
- **Falsifier.** B is no better than C at matched mean duration **and** B's durations are
  uncorrelated with post-hoc time-to-bar. Then the organism's own LP signal carries no
  readiness information in this regime, and stage length is a timer question here.
  **If A already passes gate (a) on every seed, that is a NULL for the question, not a
  falsification** (per the spec) -- report it as such, do not force a verdict either way.

## 5. What this probe does NOT do

No `ree_core` edit. No queue entry, no experiment_queue.json touch, no chip spawned, no
`claims.yaml` edit (worker brief line 13). Not a claim -- a probe, reported to the
orchestrator for a user/governance decision on whether and how to build on it. Evidence
domain: **D1** (a member-trained head's discrimination in the space it is evaluated in; no
E3 consumer, no behaviour reading) -- matching the audit's own domain call for H3.

## 6. Limits, stated up front

- The monitor/score bit-identity claim (sec 2.1) is a D0 code-read inference, not directly
  verified by a byte-comparison in this run (time budget). If this probe's result is
  surprising, that is the first thing to check.
- Probe-scale doses (sec 2.2) mean this probe's absolute disc4 numbers are not comparable
  to the campaign's own published W3/N2 figures; only the within-probe arm comparison is
  load-bearing.
- n=5 seeds is the audit's own registered size; the correlation DV is descriptive only.
- This probe answers "does timing beat duration-matched randomness, holding total
  consolidation training fixed" -- it does not test a single online run that decides its
  own stop point AND is scored on the head that decision produced (a harder, more
  deployment-realistic design named here as a follow-on, not built).

## 7. Results

*(filled in after the registered seeds run; this section is appended, not
retro-fitted into secs 1-6 above)*
