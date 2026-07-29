# Failure autopsy — V3-EXQ-603e hold-weighted entropy DV (defect form 2)

**Generated** 2026-07-29T16:29Z · **Session** `silly-mayer-a60957`
**Driver** `ree-v3/experiments/v3_exq_603e_q045_mech313_mech260_scaffolded_sd054.py` (ree-v3 `aec93ad`)
**Run** `v3_exq_603e_q045_mech313_mech260_scaffolded_sd054_20260603T040310Z_v3` (FAIL, `non_contributory`, `substrate_ceiling`)
**Lint** `validate_experiments.py::e3_hold_weighted_readout_lint`, site `:575`
**Claims** Q-045, MECH-313, MECH-260 (all three already `pending_retest_after_substrate`)
**Prior autopsy** [`failure_autopsy_V3-EXQ-603e-626a-622_2026-06-03.md`](failure_autopsy_V3-EXQ-603e-626a-622_2026-06-03.md) — predates this finding, does not address it
**Sweep** NOT covered by [`hold_weighted_e3_readout_corpus_sweep_2026-07-20.md`](hold_weighted_e3_readout_corpus_sweep_2026-07-20.md) (zero hits) — genuinely untriaged, not sweep backlog

> **One line.** **DISQUALIFYING.** The primary DV `selected_action_entropy` is a
> distribution-shape statistic accumulated per env step, and the arms are *not*
> symmetric in hold structure: de-weighting moves the DV by **1.8–5.3×** on ARM_0/1/4
> and by **~1%** on ARM_2/3. Acceptance criterion **C3 is decided entirely inside that
> differential** and reverses under de-weighting. **No re-scoring is owed** — the run is
> already `non_contributory` / `substrate_ceiling` with all three claims held for retest.
> The finding is binding on the routed re-issue **603f**.

---

## 1. The accumulation site

`_run_p2_measurement` (`:488`) counts one histogram entry per **env step**:

```python
:575                    action_counts[idx] += 1        # idx = select_action() return
:616    selection_entropy = _entropy(action_counts)
:633        "selected_action_entropy": round(selection_entropy, 6),
```

`agent.select_action` returns the **held** action at `agent.py:5917` on
`not ticks["e3_tick"]`, before `e3.select()` is reached. Cadence is
`heartbeat.e3_steps_per_tick` = 10 by default, driven to **[5, 20]** by
`clock.update_e3_rate_from_beta` (MECH-093), which is called unconditionally every
step (`agent.py:4925`). So ~90–95% of counted steps are replications of a prior
commitment, not fresh selections.

This is the **primary DV**: `_evaluate` reads it as `e0..e4` (`:1027-1031`), and it
carries C1, C2, C3 and the FP2 entropy leg. C2 and FP2 are conjuncts of `overall_pass`.

**Not mitigated by the 2026-07-29 degeneracy self-report** (ree-v3 `55a8fc2`, `:974`):
that block tests whether the five arm entropies are *flat* against a 0.0 floor. The
arms here are anything but flat — they differ by 200×, just for the wrong reason. The
check is orthogonal to replication weight and does not see this.

## 2. Verdict against the rubric — DISQUALIFYING on both exclusions

The lint's rubric bounds the defect at <1% (the V3-EXQ-663 replay) **only** where arm
symmetry cancels it *and* the DV is a continuous magnitude. Both exclusions bind here:

1. **The DV is an entropy** — the explicitly disqualifying category. Replication
   reweights the distribution, which is exactly what the statistic measures.
2. **The arms are not symmetric in hold structure.** `measured_steps` spans
   4060 → 12054, a **~3× spread**, before any consideration of cadence.

## 3. The distortion, computed exactly

`(selected_action_entropy, unique_actions, measured_steps)` over-determines the
histogram for 2–3 symbols, so the landed hold-weighted counts are recoverable exactly
(residuals ~1e-7). Surviving seed-43 cells — **10 of 15 cells aborted on
`p1_survival_gate_failed`, so every arm is n=1**:

| arm | recovered counts | H_hold | position_entropy |
|---|---|---|---|
| ARM_0_both_off | `[11500, 3]` | 0.002413 | 0.996 |
| ARM_1_mech313_only | `[12037, 5]` | 0.003648 | 0.986 |
| ARM_2_mech260_only | `[2034, 2021, 5]` | 0.701770 | **0.0** |
| ARM_3_both_on | `[3430, 3369, 1]` | 0.694450 | **0.0** |
| ARM_4_matched_noise | `[12046, 8]` | 0.005520 | 1.057 |

De-weighting each minority **run** to a single commitment (the most generous
assumption for the landed DV — it is a *lower* bound on the distortion):

| arm | ratio @ cadence 10 | ratio @ cadence 20 |
|---|---|---|
| ARM_0 | **2.90×** | **5.30×** |
| ARM_1 | **1.84×** | **3.37×** |
| ARM_2 | 1.01× | 1.03× |
| ARM_3 | 1.01× | 1.02× |
| ARM_4 | **1.22×** | **2.22×** |

**Why the asymmetry is structural, not incidental.** Entropy is strongly non-linear in
the minority probability as `p → 0`. Hold-weighting multiplies rare-event *counts* by
the hold duration, so it distorts heavily where `p` is tiny (ARM_0/1/4: the minority
action fired 3, 5 and 8 times in ~12,000 steps) and negligibly where `p ≈ 0.5`
(ARM_2/3: a near-exact 50/50 split, preserved under any uniform replication). The arms
differ ~200× in minority rarity, so they sit at opposite ends of that curve. **Any
cross-arm comparison of this DV inherits the differential.**

## 4. C3 is decided inside the distortion band and reverses

```python
:1042    c3_q045_each_alone_beats_off = (e1 > e0) and (e2 > e0)
```

A bare inequality with **no margin** (unlike C1/C2/FP2, which carry
`ENTROPY_MARGIN = 0.05`). The landed verdict is `true`, resting on
`e1 - e0 = 0.003648 - 0.002413 = 0.001235 nats` — arithmetically, **the difference
between 5 and 3 minority steps out of ~12,000**, which de-weight to ~1 fresh selection
each. Under de-weighting at both cadence 10 and cadence 20 the ARM_1/ARM_0 ordering
**reverses** (0.00672 vs 0.00700; 0.01229 vs 0.01279).

The honest statement is not "C3 is false" — the fresh-selection sequence was never
emitted, so it cannot be recomputed. It is that **C3 is undetermined**: its margin is
an order of magnitude smaller than the distortion the accumulation introduces, and the
sign is not stable across the cadence range the substrate actually uses.

**The other criteria are robust and the headline verdict does not move.** C1
(0.694 > 0.052) and C2 (`false`, 0.694 < 0.752) survive de-weighting; FP2 fails on its
*behavioural* leg (`|r3_reef − r4_reef| = 0 > 0.02` is false), so it is not
entropy-decided in this run. `overall_pass` requires C2 ∧ C4, both false. **FAIL stands
on grounds untouched by this defect.**

## 5. The larger finding: the DV is anti-correlated with its own construct

ARM_2 and ARM_3 carry the **highest** action entropy (≈ ln 2 = 0.693) and
`position_entropy = 0.0` — the agent occupied **exactly one grid cell** for the entire
measurement, while ARM_0/1/4, with near-zero action entropy, actually moved
(`position_entropy ≈ 1.0`). C5 fails accordingly (`rolling_h_pos_mean_ARM_3 = 0.0`).

The mechanism is visible in the recovered counts: `[2034, 2021, …]` and
`[3430, 3369, …]` are a near-exact **2-cycle**. MECH-260's dACC penalty is the recent
frequency of a candidate class in an 8-deep ring (`dacc.py:270-287`, weight 0.5), so
selecting A suppresses A, the next selection takes B, which suppresses B, and so on.
The result is an in-place oscillation between two opposing actions with zero
displacement.

So `selected_action_entropy` as constructed **rewards a pathological limit cycle**. It
is not merely contaminated by replication weight — in this very dataset it moves
*opposite* to the behavioural coverage it is supposed to stand in for. Q-045 asks
whether MECH-313 and MECH-260 are jointly load-bearing for *strategy diversity*; a DV
that peaks when the agent is stuck in a corner cannot answer that, hold-weighted or
not.

**Corollary on MECH-313.** The temperature lift the experiment is actually about
produced ARM_0 → ARM_1 = +0.0012 nats, against ARM_4's explicit `T=1.5` at +0.0031.
The arm carrying the NoiseFloor substrate moved *less* than the constant-temperature
control. Temperature enters only at `e3.select()`, i.e. on the ~5–10% fresh steps, and
each fresh choice is then replicated ~10–20×, so any diversity it creates is diluted
before it reaches the histogram. This is suggestive of an inert lever but is **not
adjudicable here** — it is confounded with everything in §3–§5 and rests on n=1.

## 6. Unit mismatch in the run's own FIFO guard (same defect family)

`dacc.record_action` (`agent.py:8138`) sits **after** the held-action early return
(`:5917`) and is therefore unreachable on held steps — dACC's memory is in units of
**fresh selections**, not env steps. But the guard is written in env steps:

```python
:220    FIFO_WARMUP_STEPS = 75            # env steps
:244    DACC_SUPPRESSION_MEMORY = 8       # fresh selections ~= 80-160 env steps
        fifo_gate_ok = (fifo_warmup_steps >= 2 * DACC_SUPPRESSION_MEMORY and ...)
```

`75 >= 16` passes numerically while comparing incommensurable units. Filling the 8-deep
FIFO twice needs ~160 env steps at cadence 10 and ~320 at cadence 20; a 75-step warmup
does not fill it **once**. The run's own guard against "dACC not warmed up" certifies a
FIFO that never warmed. (`fifo_temporal_gate_ok_all` is `false` in the manifest, but it
failed on the *other* conjunct — the steps-measured leg — so this leg passed vacuously.)

## 7. Disposition

**No re-scoring, no manifest edit.** The landed run is `outcome: FAIL`,
`evidence_direction: non_contributory`, `epistemic_category: substrate_ceiling`, with
no `load_bearing` field and all three claims already `pending_retest_after_substrate`.
Nothing in the claim graph is scored on this DV, so the contamination has **no
retrospective consequence**. The 2026-06-03 cluster autopsy's diagnosis (z_goal = 0.0
on all 15 cells; survival-competence and benefit-starvation prerequisites) stands
unchanged and is independent of this finding.

**No `E3_HOLD_WEIGHTED_READOUT_EXEMPT`.** The finding is not safe; the marker would be
false.

**Binding on 603f**, the re-issue the prior autopsy already routed behind a
`scaffolded_sd054_onboarding` substrate AMEND. 603f is **not queued by this session**:
its stated prerequisite (P0/P1 scaffold reaching ≥2/3 foraging-competent seeds, plus a
forced-benefit Stage-0 z_goal warmup) is not evidenced as done, and re-issuing now
would abort on the same `p1_survival_gate_failed` that took 10/15 cells. Requirements
carried forward, to be discharged **in `/queue-experiment`**:

1. **Gate the accumulation on a fresh selection** — `ticks["e3_tick"]`, or
   clear-before-select. Emit `n_fresh_select`, `n_latched`, `fresh_select_yield`.
   Reference: `experiments/v3_exq_785a_mech463_arousal_exogenous_urgency_decomp.py`.
2. **Emit both readouts kept distinct** if the hold-weighted quantity is still wanted
   (it is a legitimate *occupancy* measure — just not a selection-diversity one).
3. **Give C3 a margin.** A bare `>` on a continuous DV is unsound independently of this
   defect.
4. **Replace or supplement the DV so it is not maximised by an in-place 2-cycle** —
   §5 is the load-bearing objection and survives the fix in (1). Pair it with the
   existing behavioural coverage term (`rolling_h_pos_mean`) as a conjunct rather than
   a separate criterion, so a stuck-oscillation arm cannot score as diverse.
5. **Re-express the FIFO warmup in fresh selections**, per §6.

## 8. Incidental: HEAD/worktree skew found and repaired

The first validator run in this session was against **stale working-tree content**: the
Mac checkout's `603e` and `622` were byte-identical to `55a8fc2^` while HEAD carried
`55a8fc2`, so the two blocking findings that commit had just cleared appeared to still
fire. This is the documented ` M` adoption-lag variant (CLAUDE.md, "Deletions are not
the only skew"). Verified against the pre-move base and repaired narrowly with
`git checkout HEAD -- <two paths>`; re-validation then reported **0 non-conforming**,
with the hold-weighted warning still firing at `:575`.

`ree-v3 stash@{0}` (autostash, 2026-07-29 17:13) holds the same two files at blobs
**identical to HEAD** — fully contained — but its `validate_experiments.py` blob
**differs from HEAD** and is therefore unlanded. **The stash was left in place**; it
needs its own containment triage per
[`ree_v3_orphaned_autostash_triage.md`](ree_v3_orphaned_autostash_triage.md).
