# `_set_goal_pipeline_frozen` silences the goal WRITE paths only -- triage

**Date:** 2026-07-27T21:20Z
**Session:** `elated-shamir-5ef201`
**Surfaced by:** §6 of `frozen_z_goal_scaffold_family_triage_2026-07-27.md`, which
scope-separated it deliberately. That triage (the 28-script measurement-phase family) is
CLOSED and is not revisited here.
**Scope:** the scaffold's own curriculum stages -- so all **78** importers of
`ScaffoldedSD054OnboardingScheduler`, not just the 28.
**Verdict:** **Confirmed by execution, and NOT cosmetic.** No retro-fix, no manifest edit,
no claim change. Closes with a docstring retraction + a contract pin on the deliberate
scope limit. The strict-isolation lever is chipped as opt-in future work.

---

## 1. The finding, restated

`_set_goal_pipeline_frozen(agent, frozen=True)` sets exactly two flags:

```python
agent.config.use_mech295_liking_bridge = False
agent.config.use_mech307_conjunction   = False
```

It does not touch either goal **read** path:

| read path | gate | resolves to |
|---|---|---|
| E3 goal term, `e3_selector.score_trajectory:1179-1190` -- `score -= goal_weight * goal_proximity` | `E3Config.goal_weight > 0.0` **and** `goal_state.is_active()` | `goal_weight = 1.0` -- `REEConfig.from_dims` (`config.py:5258`, `:6329`) overrides the `E3Config` dataclass default of `0.0` |
| E1 goal-conditioning | `GoalConfig.e1_goal_conditioned` | `True` |

The scheduler calls it with `frozen=True` in `run_stage0b_consolidation`, `run_p0` and
`run_hazard_avoidance`. By then Stage-0 has seeded z_goal and Stage-0b has protected it, so
`is_active()` is True and the E3 goal term fires throughout stages the scheduler describes
as having the goal pipeline frozen.

---

## 2. Confirmed by execution, not by reading

Probe: build the V3-EXQ-460c dry-run config, enable `agent.e3.e3_score_decomp_enabled`
(diagnostics-only, does not alter scores), wrap `select_action`, and record
`e3.last_score_decomp["per_candidate"]` plus `e3.last_scores` on every E3 tick of every
stage. 3 seeds (0/1/2), CPU, run on `ree-worker-2` via `scripts/remote_pytest.sh`; base
ree-v3 `f316edae9e`, run_id `DLAPTOP-5-1914-20260727T211636Z-2269119328`.

Config resolution reproduced the §6 claim exactly: `e3.goal_weight = 1.0`,
`goal.e1_goal_conditioned = True`, `goal_state is not None`.

Three quantities per stage. `|mean|` is the candidate-mean **level** of a component -- a
level common to all candidates cancels in the softmax and is NOT evidence of influence.
`spread` is the within-tick max-min **across candidates**, which is what actually
differentiates them. `argmin_flip_rate` is the counterfactual that settles it: the
fraction of ticks on which the cost-argmin candidate changes when the goal term is added
back out of the final per-candidate score vector.

| stage | freeze | n ticks | `goal_active_frac` | goal `spread` | goal/harm spread | goal share of summed spreads | **argmin_flip_rate** |
|---|---|---|---|---|---|---|---|
| `stage0` | UNFROZEN | 129 | 0.977 | 0.0722 | 0.19 | 0.003 | **0.000** |
| `stage0b` | **FROZEN** | 127 | 1.000 | 0.6107 | 2.44 | 0.135 | **0.394** |
| `p0` | **FROZEN** | 360 | 1.000 | 0.1113 | 0.30 | 0.003 | **0.189** |
| `hazard` (Stage-H) | **FROZEN** | 586 | 1.000 | 0.1022 | 0.65 | 0.168 | **0.377** |
| `p1` | unfrozen | 399 | 1.000 | 0.2712 | 1.20 | 0.192 | **0.464** |

`goal_term_nonzero_frac` is **1.000** in all three frozen stages: the term fires on every
single tick, exactly as predicted.

**The load-bearing numbers.** In Stage-H the goal term's candidate spread is **0.65x the
harm term's** and ~17% of the summed component spread, and removing it moves the selected
candidate on **38% of ticks**. Stage-H's whole point is that "the agent's E3 harm
evaluation drives survival"; the goal term is nearly two-thirds as discriminative as the
harm term it is supposed to be isolated from. Stage-H's profile is close to **P1's**
(flip 0.464, share 0.192) -- the stage where the goal is deliberately live. That is the
sharpest way to put it: on the E3 score decomposition, the "isolated" stage is not far
from the un-isolated one.

**Why P0 looks mild and Stage-H does not.** In P0 the E1 viability term `f` has a mean
level of 1328 and a spread of 36.7 -- the world model is still untrained and `f` swamps
everything, so the goal term's share is 0.003. By Stage-H `f` has collapsed to a level of
4.7 and a spread of 0.34. The goal term barely changes in absolute terms; it simply stops
being swamped. So the effect grows as the curriculum works, and it is largest exactly where
the curriculum's isolation claim is strongest.

**Direction of the bias in the estimate.** In this dry-run configuration Stage-0 reached
`z_goal_peak` 0.352 / 0.259 / 0.422 -- two of three seeds **below** the 0.4 formation gate a
real run must clear. A production run holds a **larger** z_goal, so the goal term is larger
than measured. These numbers under-state.

**Caveats, stated plainly.** One config (460c dry-run: 5 episodes/stage), 3 seeds, CPU. The
argmin flip is a deterministic proxy -- selection is a multinomial over
`softmax(-score/T)`, so a flip at a near-tie tick carries less behavioural weight than the
rate alone suggests. It is not proof that any measured DV moved; it is proof that the
isolation claim is false as written, which is what was asked.

---

## 3. Scope -- whose recorded conclusion rests on strict isolation? **None.**

79 files import the scheduler (78 experiment scripts + the module itself). **73** enable
`scaffold_stage0_enabled=True`; **64** enable `scaffold_hazard_stage_enabled=True`.

**The five exceptions where the term is genuinely inert.** `v3_exq_603d`, `v3_exq_603e`,
`v3_exq_621`, `v3_exq_621a`, `v3_exq_625c` leave Stage-0 disabled. For 603d / 621 / 621a
(zero `update_z_goal` calls of their own) z_goal is zero-init when `run_p0` runs,
`is_active()` is False and the E3 goal term is skipped outright. 603e and 625c call
`update_z_goal` themselves (9 and 2 sites) so their P0 state needs a per-script read;
neither enables Stage-H.

**Landed manifests.** Across all 78, evidence directions are: `non_contributory` 54,
`superseded` 6, none 7, `unknown` 2, `supports` 5, `mixed` 2, `weakens` 1, no manifest 1.
The ten governance-weighting runs:

| run | direction | claims |
|---|---|---|
| 460d | mixed (FAIL) | SD-034, MECH-260, MECH-261 |
| 466e | **supports** (PASS) | SD-034 |
| 514m | mixed (FAIL) | MECH-229, MECH-230 |
| 514o | **supports** (PASS) | MECH-229 |
| 514u | **supports** (PASS) | MECH-436 |
| 603q | **supports** (PASS) | SD-059, MECH-358 |
| 652 | **supports** (PASS) | SD-057, MECH-346, MECH-347 |
| 715 | unknown (FAIL) | MECH-445, MECH-446 |
| 717 | weakens (FAIL) | MECH-445 |
| 721 | unknown (PASS) | -- |

None of these has a conclusion of the form "avoidance/survival was learned WITHOUT goal
influence". Their DVs are closure/commitment behaviour, wanting-liking dissociation, cue
authority, and bridge survival-lift; Stage-H is curriculum for them, not the estimand. In
particular **603q**, the one `supports` run that is *about* Stage-H, is a 4-arm
**between-arm survival lift** (bridge ON vs `ARM_BASE_IA_ONLY`) -- the goal term is present
in every arm, so it does not manufacture the lift.

The experiments that ARE about Stage-H isolation are exactly the readiness/validation
series, and **every one of them is already non-weighting**: 603g FAIL/`non_contributory`,
603h FAIL/`non_contributory`, 603k PASS/`non_contributory`, 603m FAIL/`superseded`, 603n
PASS/`non_contributory`, 603p FAIL/`non_contributory` -- all with empty `claim_ids`. So the
overclaim never reached governance.

No manifest anywhere in `evidence/experiments/` asserts goal-free isolation in its own
text (grepped for "without the goal" / "goal-free" / "goal pipeline FROZEN" / "survival
learned alone"; the hits are unrelated uses of "in isolation" in non-scaffold runs).

**Where the overclaim DID propagate:** the phrase is copied into 8 experiment-script
comments -- 603g (twice, incl. "survival learned alone"), 603m, 603n, 634, 634b, 687, plus
`run_p0`-frozen mentions. These are landed scripts; they are **not** edited (see §5).

---

## 4. Recommendation: **(b), leave the code and correct the docstrings** -- with the
strict lever chipped as opt-in

Reasoning, against option (a) "widen the helper to zero `e3.goal_weight`":

1. **It is not free and not bit-identical.** It changes E3 selection in three stages for
   all 78 importers, so no future run is comparable to any landed scaffold run. That is a
   large comparability cost.
2. **Nothing is bought with it right now.** §3 establishes that no landed conclusion rests
   on strict isolation, and the six runs that *are* about Stage-H isolation are all
   already `non_contributory` / `superseded` with no claim ids.
3. **The helper is not lying about itself.** Its own docstring says it freezes "the goal
   pipeline **write paths**", and MECH-295/307 are write paths. The false statement is in
   the *stage* docstrings -- `run_hazard_avoidance`'s "the agent's E3 harm evaluation
   drives survival **without the goal pipeline**". Fixing the false statement is the
   proportionate repair.
4. **But the lever should exist.** A future experiment that genuinely needs goal-free
   Stage-H currently cannot get it. That wants an opt-in, default-off knob (bit-identical
   when unset, per this repo's standing convention), not a silent widening. Chipped, not
   built here.

### Landed with this triage

- `experiments/scaffolded_sd054_onboarding.py` -- **docstrings/comments only, zero logic
  change**:
  - `_set_goal_pipeline_frozen`: a SCOPE block naming both read paths, their independent
    gates, the `from_dims`-vs-dataclass `goal_weight` trap, the measured numbers, and why
    widening was declined.
  - `run_hazard_avoidance`: the "without the goal pipeline" sentence **retracted
    explicitly** and replaced with what freezing does and does not buy, plus the Stage-H
    measurements. The inline `# Goal pipeline FROZEN (isolation)` comment likewise.
  - `run_p0`: the same scope note, including the five-script inert exception.
- `tests/contracts/test_frozen_z_goal_scaffold_family.py`:
  - module docstring: the "the held goal cannot drive behaviour" claim corrected, with the
    measured flip rates.
  - `test_goal_pipeline_freeze_helper_silences_the_consumers`: docstring corrected (it
    asserted this pairing was "a genuine isolation"). **The assertions are unchanged** --
    the existing freeze/unfreeze call-site pins and the both-flags-written pin still hold,
    as required.
  - NEW `test_goal_pipeline_freeze_does_not_touch_the_read_paths`: pins the write set as
    *exactly* the two MECH flags, so a future widening has to be a deliberate,
    test-updating act rather than an unremarked "fix" -- and re-asserts that the read paths
    are live, so the scope limit actually bites.

### Not done, on purpose

- No landed experiment script edited (the 8 carrying the propagated phrasing). They are
  historical, the phrasing is in comments only, and touching `experiments/v3_exq_*.py`
  goes through `/queue-experiment`.
- No manifest edited. No claim status, confidence, `live_status` or `v3_pending` touched.
- The opt-in strict-isolation knob is **not** built -- chipped as `/implement-substrate`
  work.

---

## 5. Reproduction

```bash
scripts/remote_pytest.sh tests/contracts/test_frozen_z_goal_scaffold_family.py -q
```

The measurement probe itself was temporary and is not retained (it monkeypatches
`select_action` and takes ~3.5 min for 3 seeds, which does not belong in the contract
suite). To re-derive: build `_make_config` / `_make_scaffold_cfg` from
`experiments/v3_exq_460c_sd034_verified_but_not_released_behavioural.py` with
`dry_run=True`, set `agent.e3.e3_score_decomp_enabled = True`, wrap `agent.select_action`
to capture `agent.e3.last_score_decomp["per_candidate"]` (index-aligned with
`agent.e3.last_scores`), and run the stages in order. The goal term is recovered per
candidate as `goal_weighted`; the counterfactual score is `last_scores + goal_weighted`
because the term entered the cost as a subtraction.
