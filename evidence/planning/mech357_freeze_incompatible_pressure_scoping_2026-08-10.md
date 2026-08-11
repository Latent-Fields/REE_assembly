# MECH-357 pressure scoping spike -- config-only lever exhaustion, and what to build next

**Date:** 2026-08-10 (spike run 2026-08-11)
**Session:** `mech357-pressure-scoping-11e9c9`
**Owns:** the scoping question raised in
[`failure_autopsy_V3-EXQ-603s_2026-08-10.md`](failure_autopsy_V3-EXQ-603s_2026-08-10.md) §6
Routing -- which of (a) genuine agent-directed predator pursuit, or (b) an episode-length /
event-timing environment-mechanics redesign, to build before spending another MECH-357 run.
**Debt class:** `complex (probe-gated)` on entry -- resolved to `complicated (buildable)` on
both halves below, with a specific build recommendation and a cheaper third option neither
original framing named.

**Changes no claim status, confidence, `live_status` or `v3_pending`. Scoping/recommendation
only -- neither candidate is built in this session, per the autopsy's routing.**

---

## Verdict in one paragraph

Re-reading `_drift_hazards` (`causal_grid_world.py:4945`) confirms what 603s's own driver
docstring already scoped: hazard mobility under `env_drift_interval`/`env_drift_prob` is
**undirected** -- hazards move randomly, or biased toward food, never toward the agent. Reading
the actual per-seed 603s data against that mechanism explains the exact tie the autopsy found:
episode outcomes are strictly **bimodal** (every cell in the corpus lands at the 200-step cap or
at ~5.5-6 steps -- nothing in between), and the ~6-step failures cluster with a collapsed
PAG-release rate matching the driver script's own documented self-contamination death clock for
a near-pure-freeze policy. That pattern is what an undirected random walk produces: whether a
hazard happens to wander onto the agent in the first few steps is a **spawn-position lottery**,
largely independent of whether the ilPFC gate is on. This is a *third* answer beyond the two the
autopsy posed: the literal **episode-length** hypothesis is not supported by the data (failures
are near-instant, not length-starved), but a **cheaper, already-built, currently-unused**
config-only mechanism -- `scheduled_external_hazard_*` (SD-029), which deterministically places
a hazard *adjacent to the agent's current position* on a schedule -- matches the "sudden,
discrete, agent-relative threat" half of the user's hypothesis far better than continuous drift,
and removes the spawn-lottery confound without writing a line of pursuit AI. **Recommendation:
run that first** (cheap, ~1 experiment), and reserve genuine agent-directed pursuit -- which
*is* buildable, scoped in §3 below, as a small extension of the existing `hazard_food_attraction`
code path -- as the fallback if the discrete-threat mechanism still doesn't separate LESION from
INTACT.

---

## 1. What the 603s mobility lever actually does

603s's own docstring (lines 30-42) already correctly audited this before the run: pursuit
(agent-directed hazard motion) is *not* in the environment. Confirmed independently this
session by reading `_drift_hazards` (`ree-v3/ree_core/environment/causal_grid_world.py:4945-
5020`): for each hazard, with probability `env_drift_prob`, it either (a) sorts candidate move
directions by distance to the *nearest food resource* (if `hazard_food_attraction > 0`, which
603s left at 0.0 -- see `HAZARD_STAGE_HFA = 0.0` in the driver), or (b) shuffles directions
uniformly at random. **Neither branch ever references the agent's position.** A grep for
pursuit/chase/seek-agent/hunt/stalk primitives across `ree_core/` (this session) turns up
nothing but unrelated "goal pursuit" language in the motivation/salience code -- there is no
agent-directed hazard-motion primitive anywhere in the substrate.

So 603s's fix (`env_drift_interval` 5->1, `env_drift_prob` 0.3->0.6) makes hazards drift *faster
and more often*, but the direction of that drift stays statistically independent of the agent.
On the 10x10 grid (`causal_grid_world.py:132`, default `size=10`) with 4 hazards
(`HAZARD_STAGE_NUM_HAZARDS=4`) each attempting an independent random step with p=0.6 on *every*
tick, this converts "hazards eventually wander somewhere" into "hazards very quickly explore
their local neighbourhood" -- which raises the *chance* that a hazard starts or ends up adjacent
to the agent early, without making that chance depend on the agent's behaviour at all.

## 2. Re-reading the 603s per-seed data: bimodal, not length-starved

Pulled `arm_results`/`per_seed` from
`REE_assembly/evidence/experiments/v3_exq_603s_instrumental_avoidance_freeze_incompatible_hazard_20260809T161324Z_v3.json`
directly (no new run needed -- this was answerable from already-collected logs, per the task
brief).

| Arm | seed 42 | seed 43 | seed 44 |
|---|---|---|---|
| LESION `median_last_window` | 200.0 | **5.5** | 200.0 |
| LESION `pag_commits`/`releases` | 176/32 (18%) | 154/5 (**3%**) | 189/45 (24%) |
| INTACT `median_last_window` | 200.0 | **6.0** | 200.0 |
| INTACT `mean_ep_len` (all 40 eps) | 144.25 | **5.975** | 144.5 |
| INTACT `pag_commits`/`releases` | 180/39 (22%) | 165/10 (**6%**) | 185/41 (22%) |
| POSCTRL `median_last_window` | 200.0 | 200.0 | **6.0** |
| POSCTRL `mean_ep_len` (all 40 eps) | 146.3 | 62.3 | **5.975** |
| POSCTRL `pag_commits`/`releases` | 175/32 (18%) | 152/8 (5%) | 198/45 (23%) |

`scaffold_steps_per_episode=200` is a hard cap (`scaffolded_sd054_onboarding.py:99`,
`causal_grid_world.py:3071-3073`: episode ends on `agent_health <= 0` OR step-cap, nothing
else). `scaffold_hazard_stage_survival_gate_steps=75` over a `stability_window=10`
(`scaffolded_sd054_onboarding.py:403-404`).

Three observations, in order of how load-bearing they are for the scoping question:

1. **There is no intermediate outcome anywhere in the corpus.** Every one of the 9 (arm, seed)
   cells lands at the 200-step cap or at 5.5-6.0 steps. If episode length were the binding
   constraint (agents surviving to, say, step 120 of a 200-step episode and needing more runway
   to fully evade), that would show up as clustering somewhere below 200 but well above 6. It
   doesn't. **Extending the episode cap would not move a 6-step death, because that death isn't
   running out of episode -- it's dying almost immediately.** This is evidence against the
   literal form of the user's hypothesis.
2. **The catastrophic cells (INTACT seed 43, POSCTRL seed 44) have `mean_ep_len` ~= `median_
   last_window` ~= 6** -- i.e. the failure is stable across *all 40* Stage-H training episodes
   for that (arm, seed), not something that emerges only late in training. Combined with a
   collapsed release-to-commit ratio (3-6% vs 18-24% in the surviving cells), this matches the
   603s driver docstring's own documented finding almost exactly: *"a PURE freeze dies in ~6
   steps in EVERY regime... due to self-contamination_spread=0.5/step -> threshold 2.0 ->
   contaminated -> health drain"* (603s docstring, lines 53-58). That mechanism is contact-
   independent of hazard motion -- it fires from the agent staying in one cell, which is
   consistent with a policy caught in a freeze it can't escape from in time, not with a graded
   avoidance failure.
3. **The same seed (43) fails identically for LESION and INTACT** (5.5 vs 6.0 -- i.e. the ilPFC
   gate being on or off made essentially no difference to that seed's outcome), while POSCTRL
   fails on a *different* seed (44) with the same ~6-step signature. That is exactly the
   "exact tie" the autopsy flagged (`G_H_LESION_frac == G_H_INTACT_frac == 0.6667`), and it is
   what an undirected process predicts: whether a given seed's random hazard walk happens to
   converge on the agent early is close to independent of whether the gate suppresses freeze,
   because with 4 fast-drifting hazards on a 10x10 grid the agent can be caught before the
   policy has had time to act on the gate's signal at all.

**Reading:** the mobility increase didn't create a gradable Pavlovian-instrumental conflict the
gate can resolve. It created a coin-flip -- unlucky spawn-adjacency kills almost instantly
regardless of policy, lucky spawn-adjacency is safe for the whole episode regardless of policy.
That is consistent with, and explains, the exact tie without needing to invoke measurement
noise.

## 3. Candidate (a) -- agent-directed pursuit: buildable, and cheaply so

Confirmed no pursuit primitive exists (§1). But the code shape to add one already exists and is
directly reusable: `hazard_food_attraction`'s branch in `_drift_hazards`
(`causal_grid_world.py:4959-4972`) already implements "sort candidate directions by Manhattan
distance to a target" for the food case:

```python
if (self.reef_enabled and self.hazard_food_attraction > 0.0
        and self.resources and self._rng.random() < self.hazard_food_attraction):
    ...
    dirs_ordered = sorted(available_dirs,
                           key=lambda d: abs(hx + d[0] - fx) + abs(hy + d[1] - fy))
```

A `hazard_agent_pursuit: float` parameter following the identical pattern -- sort toward
`(self.agent_x, self.agent_y)` instead of the nearest resource, with the same per-drift-tick
probability gate -- is a direct sibling of code that already exists, tested, and shipped. Rough
scope: one new constructor param + default, one new branch (or a shared helper parameterised on
target-cell rather than duplicated), a `machine_class`/config-slice entry, and a contract test
mirroring whatever covers `hazard_food_attraction` today. This is a **`complicated (buildable)`**
env-code change, not a `complex (probe-gated)` one -- the uncertainty in "not config-buildable"
(603s's own framing, correctly) was about whether it existed as a *config knob*, not about
implementation difficulty once real code is on the table. Estimate: small, well-bounded, on the
order of the `hazard_food_attraction` feature itself.

What it buys that continuous undirected drift cannot: a pursuing hazard's threat to the agent is
*continuous and behaviour-contingent* rather than a one-time spawn-position lottery -- an
undirected freeze/release cycle stays reachable indefinitely, while directed escape-to-reef
actually increases distance. That is the genuine, sustained Pavlovian-instrumental conflict the
paradigm needs, and it is the only one of the three candidates in this note that removes the
spawn-lottery confound *and* forces a sustained (not one-shot) response.

## 4. Candidate (b), reframed -- SD-029 `scheduled_external_hazard` is already built and unused

The literal "make episodes longer" reading of (b) is not supported (§2.1). But the *mechanism*
half of the user's hypothesis -- "sudden, discrete novel-threat events... as opposed to smooth
continuous drift" -- names something that already exists in the substrate and was **not** used
by either 603r or 603s: `scheduled_external_hazard_enabled` / `_interval` / `_prob` /
`_adjacent_only` (SD-029 balanced-hazard-event curriculum, `causal_grid_world.py:260-270`,
implemented at `_inject_external_hazard`, `causal_grid_world.py:4774-4843`).

Mechanically, on a schedule (every `scheduled_external_hazard_interval` steps, with probability
`scheduled_external_hazard_prob`), it **moves an existing hazard to a cell adjacent to the
agent's current position** (or spawns one there if none exist) -- not to a random cell, not
biased toward food, but to the agent's *neighbourhood specifically*, wherever the agent currently
is. This is qualitatively different from `_drift_hazards`'s ambient random walk in exactly the
way that matters here:

- It is **agent-relative by construction** (unlike `_drift_hazards`, which is symmetric with
  respect to the agent and only *coincidentally* threatens it).
- It is **discrete and scheduled**, not continuous -- a genuine "threat-onset event" rather than
  ambient risk, closer to the active-avoidance paradigms the 603r/603s autopsies both cited as
  the biological reference (discrete, sudden threat onset).
- It removes the **spawn-position lottery** identified in §2: because the injection targets the
  agent's *current* cell at the scheduled tick (which happens after the episode -- and the
  trained policy -- is already underway), the outcome is no longer dominated by where the agent
  happened to start relative to a random walk's early trajectory.
- It requires **zero new environment code** -- the four parameters already exist on
  `CausalGridWorldV2.__init__`, default `enabled=False`, and would need only to be threaded
  through `ScaffoldedSD054OnboardingConfig`/the Stage-H `_build_env` call the way
  `HAZARD_STAGE_ENV_DRIFT_INTERVAL`/`_PROB` already are in the 603s driver (`v3_exq_603s_
  instrumental_avoidance_freeze_incompatible_hazard.py:296-298`). This is a **config-only**
  successor experiment, not an `/implement-substrate` build.

This is genuinely a third option the autopsy's routing didn't name (it posed (a) full pursuit AI
vs (b) episode-length -- SD-029 is neither). It is the cheapest thing to try next: it directly
tests the "does a forced, discrete proximity event -- rather than ambient drift -- force the
freeze/escape conflict" question, at zero code cost, and if it works, MECH-357 gets its evidence
without ever needing pursuit AI.

## 5. Recommendation

**Try SD-029 (`scheduled_external_hazard`) first, as a config-only successor experiment.**
Suggested calibration starting point: `scheduled_external_hazard_enabled=True`,
`_interval` in the 15-25 range (several discrete events across a 200-step / 40-episode Stage-H
budget), `_prob` 0.8-1.0 (near-guaranteed on schedule, so all three arms see comparable event
counts), `_adjacent_only=True` (matches "adjacent predator appears" rather than "somewhere in
the grid"). Keep background `_drift_hazards` at its default-adjacent low mobility (`interval=5,
prob=0.3`, i.e. revert 603s's aggressive `(1, 0.6)`) so the *discrete* injection is the isolated
new pressure rather than stacking on top of the spawn-lottery-prone continuous drift this note
diagnosed in §2. Keep the existing two-sided discriminative-headroom guard (R4/R5, LESION-must-
fail / POSCTRL-must-clear) unchanged -- it is exactly the right instrument for this too and
worked as designed in 603s.

**Reserve genuine agent-directed pursuit (§3) as the fallback**, to be scoped into a real
`/implement-substrate` build only if the SD-029 successor *also* fails to separate LESION from
INTACT. If a single discrete forced-proximity event still isn't enough to force the conflict
(plausible: one adjacency event might still be survivable by luck or by a single reactive move,
without requiring *sustained* directed evasion), that would be reasonably strong evidence that
sustained, behaviour-contingent pursuit is the actual missing ingredient, and the pursuit build
scoped in §3 is a small, well-bounded addition to reach for at that point -- not a large lift,
contrary to how "not config-buildable" reads if taken as "hard to build."

## 6. Follow-on work surfaced (not spawned in this session)

Per this repo's chip-following-autopsy convention, this scoping session does not itself spawn a
chip (it is not a `/failure-autopsy` or `/governance` session, but the recommendation here is
downstream of one and should go through the normal `/queue-experiment` / `/implement-substrate`
routing rather than being started here):

- **`/queue-experiment`**: a V3-EXQ-603t-style successor to 603s using
  `scheduled_external_hazard_*` per §5's calibration, claim-tagged `MECH-357`, keeping the two-
  sided headroom guard from 603s's design.
- **`/implement-substrate`** (fallback only, contingent on the above): `hazard_agent_pursuit`
  parameter on `CausalGridWorldV2._drift_hazards`, mirroring the existing
  `hazard_food_attraction` sort-by-distance pattern, per §3.

Both are named here per the routing convention; neither is chipped by this session.
