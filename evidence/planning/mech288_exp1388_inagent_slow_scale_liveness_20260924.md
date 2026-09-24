# MECH-288 / EXP-1388 -- in-agent slow-scale liveness: measured RED

**Status: FINDINGS RECORD. No registry field, claim status, queue entry or proposal status was
changed by the session that wrote this. EXP-1388 was deliberately left at `status: proposed`
pending the decision chip named below.**

- Session: `metaworker-science-20260924-orchb-mech288-boundary-anchor` (headless, ree-cloud-4)
- Campaign: `science-20260924-orchb-mech288-boundary-anchor`
- Chip: `chip-proposal-exp-1388` (left OPEN, unclaimed -- see "Disposition")
- Written: 2026-09-24T12:36:05Z

## Why this exists

The chip asked `/queue-experiment` to turn proposal EXP-1388 (claim MECH-288) into a driver plus
a queue entry. It arrived with a pre-flight verdict of GREEN. Three of that verdict's premises
were re-measured before any design work, per CLAUDE.md "Working a chip or brief: audit its
premises before building on them". All three are false as of today. The decisive one is
measured below and makes the experiment, as designed, unable to measure its own primary
criterion.

## F1 -- MEASURED: the slow/outer scale is inert on the in-agent observation path

MECH-288's `what_would_answer` NON-DEGENERACY PRECONDITION (1) requires
`use_event_segmenter=True` **and boundary fires > 0 on BOTH scales** in the measurement window on
every measured cell. C1 -- the primary, load-bearing criterion, and the only specificity-bearing
one (precondition (3) makes the fast scale descriptive-only) -- is defined on the slow/outer
scale.

Measured on this box (`ree-cloud-4`, torch 2.12.0+cpu), untrained `REEAgent` in `eval()`,
`CausalGridWorldV2(size=8, num_hazards=3, num_resources=3, background_drift_enabled=True,
n_drift_sources=2)`, `StepHarness(train_mode=False)`, canonical `EventSegmenterConfig` defaults,
counting `BoundaryEvent`s at the agent's own observation call site
(`ree_core/agent.py:5784`, `pe_dict=None`):

| Arm | ticks | z_goal supplied | slow fires | fast fires |
|---|---|---|---|---|
| `REEConfig.from_dims(...)` default | 236 | **0 / 236** (`z_goal` is `None` every tick) | **0** | 2 |
| `+ cfg.goal.z_goal_enabled = True` | 499 | 499 / 499 | **0** | 2 |

In the second arm z_goal is supplied on every tick but is **identically the zero vector for the
whole run**: `zgoal_norm_mean = 0.0`, `zgoal_norm_std = 0.0`, `zgoal_delta_max = 0.0`,
`goal_state.is_active() == False` at the end of all 12 episodes. `GoalState`'s benefit gate
(`benefit_exposure >= goal.benefit_threshold`, default 0.1) never opened, so `update_z_goal()`
was never called -- the `active_frac=0.000` shape the `/queue-experiment` z_goal table describes.
A BOCPD-Gaussian detector over a constant zero stream cannot emit a change point.

Mechanism, from source, not inference:
- `ree_core/goal.py:88` -- `GoalConfig.z_goal_enabled: bool = False`.
- `ree_core/agent.py:3522-3525` -- `self.goal_state` is constructed **only** when
  `goal.z_goal_enabled`; otherwise it stays `None`.
- `ree_core/agent.py:5780-5782` -- the observation-path `latent_dict` sets
  `"z_goal": self.goal_state.z_goal if self.goal_state is not None else None`.
- `ree_core/utils/config.py:2300-2310` -- the canonical slow scale is `bocpd_gaussian` over
  `("z_goal",)` alone, `prior_var=1.0`, `posterior_threshold=0.5`, `min_segment_length=15`.

So on the default in-agent path the slow scale receives no input at all; with `z_goal_enabled=True`
it receives a constant. Either way precondition (1) is RED and C1 is unmeasurable.

### This converges with two already-landed measurements

- **V3-EXQ-830** (2026-07-27, PASS/non_contributory; confirmed autopsy
  `failure_autopsy_V3-EXQ-830_2026-07-29`): with a *live, varying* z_goal stream on 87% of sweeps
  (`zgoal_norm_std 0.070` against a 1e-4 floor) the MECH-288 slow BOCPD scale **fired zero times**
  on the rollout stream. That is the best available evidence about a non-degenerate z_goal stream,
  and it says 0.070 of variation is far below the rail.
- **V3-EXQ-757** needed hand-planted `GOAL_LEVELS` gaps of **>= 10** -- "chosen to hit BOCPD's
  decisive rail, as the driver's own comment says" (D1 cluster autopsy) -- to fire it at all.

Two orders of magnitude separate the variation a live z_goal stream has been measured to carry
(0.070) from the jump the detector has been measured to need (>= 10).

**Caveat, stated rather than papered over:** the probe used an UNTRAINED agent. A warmed or
trained agent may open the benefit gate and produce a live z_goal stream. What that would NOT
change is the rail: V3-EXQ-830 already had a live varying stream and still got zero slow fires.
So warming plausibly moves the first arm's failure mode (`z_goal` constant) onto 830's
(`z_goal` live but sub-rail); it does not obviously reach precondition (1) green. Establishing
that is exactly the probe the decision chip proposes.

## F2 -- the pre-flight's DV-liveness citation is a fast-scale, rollout-path counter

The pre-flight's item 5 cited V3-EXQ-938's `boundary_fires_mean_pe_arm=276.95` /
`boundary_fires_mean_yoked_arm=287.325` as showing MECH-288 "firing on both scales". It does not.
That statistic is `decomp_n_boundary_fires`, produced by `ree_core/policy/policy_decomposition.py:866`
on the MECH-321 **rollout** stream, whose own source comment (`:870-873`) reads:

> `decomp_n_boundary_fires_slow` stays 0 unless the slow BOCPD scale has its z_goal stream on the
> rollout side, which is what `decomposition_scale_resolved_probe` switches on -- so on the
> default path these read `(n_boundary_fires, 0, 0)`.

V3-EXQ-938 did not run that probe, so its 277-287 figure is fast-scale-only. There is no landed
measurement of slow-scale firing on the observation path. There is now: zero (F1).

## F3 -- C2's only pre-registered anchor was invalidated 51 minutes before the pre-flight ran

EXP-1388's acceptance check 4 (C2, bounded false-positive rate) and MECH-288's own
`what_would_answer` CONFIRMING (b) both anchor the ceiling on V3-EXQ-757's `C288_silence`
("there it was 27 A-slow vs 0 B-slow"). The pre-flight's item 4 restated that anchor as
"genuinely measurable, not floor-pinned by construction".

The confirmed D1 cluster autopsy (`evidence/planning/failure_autopsy_gflag0452-D1-cluster_2026-09-24.md`),
applied to `origin/master` in REE_assembly `2e6fe97c4b` at 2026-09-24T10:23:06Z -- **51 minutes
before the pre-flight was written at 11:14:55Z** -- finds the opposite: "Smooth-arm silence
follows from 0.02 noise far below the rail." Verified against the driver:
`experiments/v3_exq_757_mech288_mech287_event_boundary_trigger_functional.py:148` sets
`GOAL_NOISE = 0.02` on the smooth arm, against planted gaps of >= 10 on the boundary arm. The
0-fire result is by construction.

The same commit moved MECH-288 `provisional -> candidate` and V3-EXQ-757
`supports -> non_contributory`, leaving MECH-288 at `genuine_exp_count 0`. MECH-288's
`what_would_answer` was **not** amended and still cites the invalidated number as the ceiling
precedent -- recorded separately as a `stale_note` governance flag.

## F4 -- precondition (3)'s "~15% construction floor" does not hold in-agent either

Precondition (3) asserts the fast/inner scale "fires ~15% on ANY stationary z-score stream by
construction" and requires that 15% be the chance baseline C3 compares the fast scale against.
Measured in-agent: 2 fast fires in 499 ticks (0.4%) and 2 in 236 ticks (0.8%) -- roughly 20-40x
below the asserted floor. The 15% figure is a property of V3-EXQ-757's synthetic stream, not of
the in-agent observation stream, so C3's chance baseline would have to be measured rather than
imported.

## Disposition

Three premises the item rests on are stale, two of them the pre-flight's own. Per the dispatch
brief's own rule ("Two unspecified choices in one item means the item's premises are stale and
the pre-flight missed it -- say so; that finding is worth more than a third question"), this
session did **not** redesign around them and did **not** author a driver or a queue entry.

- `chip-proposal-exp-1388`: left OPEN and unclaimed, note pointing here.
- EXP-1388: left at `status: proposed`. Whether it becomes `blocked_substrate` or is re-scoped
  is the open decision, not this session's to take.
- Decision chip raised with the options; `stale_note` governance flag raised on MECH-288.

## Reproducing

The two probes are `.scratch/` throwaways and are reproduced inline here rather than committed;
both are ~60 lines and consist of building env + `REEConfig.from_dims` + `REEAgent`, wrapping
`agent.hippocampal.event_segmenter.step` to tally `BoundaryEvent.scale` and the z_goal norm
series, and stepping `StepHarness(train_mode=False)`. Interpreter on this box:
`/home/ree/.venv/ree/bin/python3` (torch 2.12.0+cpu); `/opt/local/bin/python3` has no torch on
a metaworker box.
