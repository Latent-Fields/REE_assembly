# DV-range probe -- `waypoint_field_consumer_reach` leg H1

- **Status:** design record. **No experiment was queued by this session** (see "Why nothing
  was queued").
- **Written (UTC):** 2026-09-14T11:35Z by session `metaworker-chip-20260905-waypoint-consumer-reach-portfolio`
  (cloud worker `ree-cloud-4`, dispatched worktree).
- **Campaign:** `chip-20260905-waypoint-consumer-reach-portfolio`, continuing the H2 probe
  sequence (`exq_wpfield_h2_dv_range_probe_20260907.md`, sections 7b/7c). H2 is now
  probe-resolved (REFUSED as queueable, toward ELIMINATED -- see that record's section 7c);
  this record picks up the stated remaining work: **"H1's DV range (visits/ep under the REE
  consumer) is still unmeasured ... it needs a REINFORCE-consumer probe on the 1004 bench."**
- **Registry question:** `waypoint_field_consumer_reach`; hypothesis **`H-wpfield-objective-sparsity`**
  (axis `drive`).
- **Pre-registration source:** confirmed autopsy `failure_autopsy_V3-EXQ-1004_2026-09-05.{md,json}`,
  `fanout_recommendation.suggested_probes[0]` (H1, axis `drive`).
- **Probe script:** `ree-v3/experiments/_scratch/exq_wpfield_h1_probe_dvrange.py` (scratch,
  no manifest, no queue entry -- same `_scratch` convention as the H2 probes).

---

## 1. Why this probe was run

Per the chip's own instruction ("Measure the DV range at probe scale before pre-registering; a
power-bump of the 1004 bench is explicitly refused") and the campaign convention the H2
sequence established (`exq_wpfield_h2_dv_range_probe_20260907.md` section 7b: "queue only with
a criterion the measured range can fail"), H1 needed the same DV-range check H2 already
received before any threshold is written down. H2's own section 8 named this explicitly as the
chip's remaining work.

## 2. What H1 pre-registered

> **Declared null:** visits/ep is flat across training signals, i.e. sparsity is not the
> residual blocker.

DV: waypoints visited per eval episode (`transition_type in {"waypoint", "sequence_complete"}`),
field ON, under a **real REE agent** (z_world -> E1/E2/E3, NOT a behaviour-cloned reader --
required explicitly by the chip and by `fanout_recommendation.live_hypotheses[0]`), comparing
the env's own stock sparse `waypoint_visit_reward` against a driver-side potential-based
shaping bonus.

## 3. Design

**Agent + training substrate: the x724 all-ON recipe, unmodified.** `_make_agent(env,
kind="all_on")` (`experiments/v3_exq_724_competence_localization_diagnostic.py`) -- the exact
agent construction every 724/734/737/742/808/978/1002/1008 driver uses (z_goal, lateral-PFC
bias head, OFC devaluation head, SD-070 z_world warmup, SD-056 e2 world-forward). Trained via
`experiments._lib.allon_training._train_all_on_agent` -- the shared, tested REINFORCE recipe
(lateral-PFC bias head + OFC devaluation head), unmodified. **No new inference-path code was
written**: reusing this exact pipeline is what makes the measurement trustworthy without a
second independent code-review pass on a from-scratch RL loop.

**Env: the V3-EXQ-1004 bench geometry, field ON, identical to both arms**
(`GRID_SIZE=12`, `N_WAYPOINTS=3`, `waypoint_visit_reward=0.2`, hazards/resources/energy zeroed,
`subgoal_arrival_position_check=True`, `hazard_free_contamination_gate=True`,
`waypoint_proximity_field_enabled=True`, `waypoint_field_decay=0.25`). `causal_grid_world.py`
is **never modified**.

**The manipulation (driver-level only, per H1's axis "drive"):** a thin duck-typed wrapper
(`ShapingCountingEnv`) around the env that (a) tallies waypoint arrivals per episode by reading
`info["transition_type"]` -- the same field `V3-EXQ-1004._rollout_counts` reads -- and (b), for
the `ARM_SHAPED` condition only, adds a **potential-based shaping term** to the reward
`_train_all_on_agent` trains on: `bonus = SHAPING_COEF * (phi(s') - phi(s))`, where
`phi(s) = obs_dict["waypoint_proximity_field_view"][2, 2]` (the 5x5 patch's centre cell = the
agent's own position's field value = `1 / (1 + waypoint_field_decay * dist(agent, target))`,
the textbook Ng-et-al. shaping form). This manipulates **only the density of the training
signal**, leaving the arrival/terminal reward, the env dynamics, and the observation channel
(H2's axis, already probe-resolved) untouched -- i.e. it is a clean, single-axis manipulation
of exactly what H1 names.

**Why visits are read off the TRAINING rollout itself, not a separate eval pass.**
`_train_all_on_agent`'s P1 phase already runs true on-policy rollout through the real
inference path (sense -> clock.advance -> e1_tick -> generate_trajectories -> select_action);
re-deriving that ~80-line path outside the shared helper would duplicate untested code for no
reason. The wrapper tallies visits per P1 episode as training proceeds; "visits/ep" is the mean
over the **last `tail_k` P1 episodes** (the "converged" window), read directly off the wrapper,
zero duplicated inference code.

**Probe scale, deliberately small and run in two escalating steps** (not one commitment):
Trial 1 -- `zworld_p0_episodes=15, p0_episodes=10, p1_episodes=20, steps_per_episode=60,
tail_k=8`, 1 seed (42), 2 arms. Trial 2 -- same geometry, `p1_episodes=60, tail_k=15` (3x the
REINFORCE budget), same seed, 2 arms. `SHAPING_COEF=5.0` was chosen deliberately strong (see
section 6) so a probe-scale run has the best chance of surfacing ANY achievable range.

## 4. A substrate/infra bug found and fixed en route (not a scientific finding, record for the
   next session on this box)

On the cloud worker this session ran on, invoking the probe script directly
(`python3 experiments/_scratch/exq_wpfield_h1_probe_dvrange.py`) from a `cwd` reached via the
`/Users/dgolden -> /home/ree` symlink (CLAUDE.md's "Machine-identity note" documents this
symlink exists; it is not specific to this box) produced a **reproducible**
`AttributeError: 'HippocampalModule' object has no attribute 'promote_candidates'` on the very
first `agent.generate_trajectories()` call -- despite `hasattr(agent.hippocampal,
'promote_candidates')` being demonstrably `True` immediately after construction, in-process,
every time it was checked directly. The failure did **not** reproduce when the identical script
was invoked from the real path (`cd /home/ree/REE_Working/ree-v3 && python3 experiments/...`),
nor when the same function was called via `import` from a `python3 -c` snippet with the real
path already on `sys.path`. The most likely mechanism: `Path(__file__).resolve()` (used for the
script's own `sys.path` bootstrap, matching the `REPO_ROOT` idiom every driver in this family
uses) follows the symlink to the real path while Python's automatic `sys.path[0]` insertion
uses the invoked (symlinked) path verbatim, so `ree_core.hippocampal.module` (and possibly
other modules) end up reachable via two distinct `sys.path` entries pointing at the same files
by different name -- plausible grounds for a duplicate-import / duplicate-class-identity defect
of exactly this shape, though this record does not claim to have proven the mechanism further.
**Workaround used for both trials below: always `cd` to the real (`/home/ree/...`) path before
invoking a driver directly on this box, not the `/Users/dgolden/...` symlinked path.** This is
a `cwd`/invocation hazard, not a code defect in this probe or in `HippocampalModule`; flagging
it here (rather than filing a substrate defect) because it costs nothing to read and would
silently confuse a future session that hits it while short-cutting a smoke test with `cd
$(dirname ...)`-style relative invocation from a worktree.

## 5. Results

**Random-policy floor, measured for context** (60-step episodes to match the probe geometry,
n=20 episodes, no agent, uniform-random actions):

| seed | random visits/ep (60-step episodes) |
|---|---|
| 42 | 0.250 |
| 43 | 0.100 |

(For comparison: V3-EXQ-1004's random floor at its native 400-step episodes is 1.29 visits/ep --
consistent with a floor that scales roughly with episode length, as expected for a 3-waypoint
random walk.)

**Trial 1** (`p1_episodes=20`, `tail_k=8`, seed 42):

| arm | visits/ep (tail-8 mean) | visits/ep (all-20 P1 mean) | elapsed |
|---|---|---|---|
| ARM_SPARSE | 0.375 | 0.333 | 229.9s |
| ARM_SHAPED | 0.125 | 0.350 | 409.8s |

lift (shaped - sparse) = **-0.25**.

**Trial 2** (`p1_episodes=60`, `tail_k=15`, seed 42, 3x the REINFORCE budget):

| arm | visits/ep (tail-15 mean) | visits/ep (all-60/70 P1 mean) | elapsed |
|---|---|---|---|
| ARM_SPARSE | 0.400 | 0.241 | 467.0s |
| ARM_SHAPED | 0.400 | 0.350 | 859.7s |

lift (shaped - sparse) = **0.0**.

## 6. Reading

**Both arms, at both budgets tested, sit at or within noise of the measured random floor
(0.1-0.25 visits/ep).** Trial 1's tail values (0.375, 0.125) bracket the floor in both
directions; trial 2's tail values are identical (0.400, 0.400) and only modestly above it.
Given `n=1` seed and an 8-15-episode tail window, none of these differences are distinguishable
from seed/window noise. **Neither arm has yet demonstrated navigation behaviour meaningfully
above chance** -- at this probe scale, the REE agent's REINFORCE-trained bias heads have not
visibly learned to exploit the waypoint signal at all, regardless of whether that signal is
sparse or heavily shaped (`SHAPING_COEF=5.0` was chosen deliberately large -- a per-step bonus
of the same order as, or larger than, the terminal arrival reward -- specifically to give the
shaped arm the best chance of separating from the floor at this budget; even that strong a
signal produced no clear separation).

**This is the SAME finding-class as H2's section 7b/7c: the pre-registered null has no
demonstrated achievable range at this configuration, so a criterion cannot yet be responsibly
written.** It is not evidence for or against H1's substantive claim (that sparsity, not
perceptibility, is the residual blocker) -- it is evidence that **this probe's training budget
is not yet sufficient to produce ANY above-floor navigation, in either arm**, which is a
precondition for discriminating between them at all. The two most likely levers, neither tested
here:

1. **Longer episodes.** 60 steps is 6.7x shorter than V3-EXQ-1004's native 400-step episodes,
   on the same 12x12 / 3-waypoint geometry where the oracle needs the full 400 steps to reach
   ~60 visits/ep. A structurally lower achievable ceiling at 60 steps is expected and was not
   separately quantified here (no oracle/trained-ceiling measurement was run at this episode
   length -- a gap the next session should close before scaling further).
2. **More REINFORCE updates.** 3x the P1 budget (20 -> 60 episodes) did not produce clear
   separation from the floor. The lateral-PFC/OFC bias-head REINFORCE mechanism may simply need
   substantially more on-policy episodes than "probe scale" (order-of-100s) to show any
   learning signal on this sparse-reward task, independent of shaping.

**Disposition: H1 is NOT YET QUEUEABLE, for the same procedural reason H2 was refused --
no achievable DV range has been demonstrated to pre-register a criterion against.** This is
distinct from H2's disposition (probe-resolved toward ELIMINATED): H1 remains genuinely
**untested**, not eliminated -- the probe measured a floor, not an effect. The registry leg
stays `alive` with `adjudicating_runs` empty; a `_scratch` probe cannot and should not
adjudicate a registry hypothesis.

## 7. What the next session inherits

- STOP-CHECK was clean at session start (2026-09-14T10:43Z): not queued, both legs `alive`
  with empty `adjudicating_runs`, no driver in `git log`. H2's disposition (section 7c of the
  H2 record) is unchanged by this session.
- **Remaining work, in priority order:**
  1. Measure the achievable ceiling at the CURRENT 60-step episode length: run one seed of the
     x724 all-ON agent under a much larger REINFORCE budget (order 150-300 P1 episodes) OR
     under the oracle/scripted policy (to get an upper bound comparable to 1004's ~60
     visits/ep-at-400-steps figure, scaled to 60 steps) to determine whether ANY budget
     realistically reachable at "probe scale" can clear the floor.
  2. If (1) suggests episode length is the binding constraint, re-run the SAME probe harness
     (`exq_wpfield_h1_probe_dvrange.py`, already built and validated) with
     `--steps-per-episode` raised toward 200-400 and a correspondingly smaller `--p1-episodes`
     if needed to keep wall-clock bounded (each 60-step/70-P1-episode cell took ~7-14 minutes
     on `ree-cloud-4`'s CPU-only venv; budget accordingly).
  3. Only once an arm demonstrates a clear above-floor navigation ceiling should a
     `dv_headroom`-style criterion be derived from the MEASURED range (never assumed) and the
     portfolio queued, per the shipped convention.
- The probe script is committed and re-runnable:
  `/home/ree/.venv/ree/bin/python3 experiments/_scratch/exq_wpfield_h1_probe_dvrange.py
  --seeds 42 43 --zworld-p0-episodes 15 --p0-episodes 10 --p1-episodes 60
  --steps-per-episode 60 --shaping-coef 5.0 --tail-k 15` (**run from the real `/home/ree/...`
  path on this box, not the `/Users/dgolden/...` symlink -- section 4**). `--dry-run` gives a
  ~15s smoke (2 arms, 1 seed, minimal episodes) to confirm the pipeline still runs before a
  real trial.
- Carry the autopsy's standing caveat forward: the driver docstring's A2C 0.00/0.10 visits/ep
  figure is single-seed, pre-SD-094-gate, on a self-contaminating env -- it MOTIVATES H1, it is
  not evidence, and must not be cited as a baseline (unchanged from the H2 record).
- Claims INV-086 and MECH-428 stay **read-across only**; neither is exercised by this probe.
