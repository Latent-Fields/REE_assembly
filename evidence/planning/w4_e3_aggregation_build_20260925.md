# W4 build: E3 discounted aggregation (DISC_0.5) on `integration/coupled-loop-repair` (default-OFF)

- **Status: BUILT on the branch (`1b013d6`), DISC_0.5, default OFF, OFF bit-identical.** Member gate (a) PASSes 4/5 in N3 proper (`9608f3117a`). **Gate (c) re-spec is HELD FOR THE USER** (options (i)/(ii)/(iii) in the N3 record), so **W4 does not yet count as gate-passed**, and the campaign rule "no D2 reading counts until W4's gate passes" still stands.
- Session `bt0925-w4` (orchestrate-20260924-breakthrough-c2), chip_ref `chip-20260925-coupled-w4-e3-aggregation-build`. Written 2026-09-25/26.
- **Code:** ree-v3 `integration/coupled-loop-repair`. The W4 commit `1b013d6` sits on top of W6a `9b322d5`; the branch was rebased by W6a, so W3 is now `7428da3`. Nothing on `main` changed.
- **Plan of record:** `coupled_loop_repair_campaign_plan.md` sec 3 W4. Selection comes from `n3_e3_aggregation_probe_20260925.md` (pre-registration `78820b45c7`, results `9608f3117a`); its design is N3-pre (`d4bb6449b3`).
- **Evidence domain: D1 on recorded data.** The native scorer's ranking of recorded rollouts. The D2 reading (head swap changes E3's ranking against cloned-env consequence) is N3's, reproduced here for s532. Nothing here reaches D3.

## 1. Premises re-measured

| # | premise (source) | re-measured | verdict |
|---|---|---|---|
| P1 | W6a is landing on the branch; wait for it to pass `042895a` (brief) | W6a pushed `9b322d5` at ~22:40Z. It rebased the branch, so W3 is `7428da3`, not `042895a` | holds. The W4 diff was re-applied on `9b322d5`. One conflict in `tests/test_flag_inertness.py` PROBED was resolved keeping both entries. `config.py` and `e3_selector.py` applied cleanly |
| P2 | "per-step terms" aggregated with a discount (brief) | E3's F is a MEAN over transitions (`compute_reality_cost`), so J is not a sum of per-step terms. N3's DISC is defined over whole depth-limited reads J_L | **corrected.** Built exactly as N3 did it: J_disc = J_2 + sum_{d=2}^{Lmax-1} gamma^(d-1) (J_{d+1} - J_d), where J_L is the same scorer at `_score_depth_limit = L`. This keeps one scorer, which is SD-081's discipline |
| P3 | the habit read is `max(2, habit_depth)` at `e3_selector.py:2088` (plan) | holds at `9b322d5` (`_arbitrate_dual_system`) | the habit loop sets `_score_depth_limit` before calling `score_trajectory`, so any depth-limited call bypasses the aggregation by construction |
| P4 | the N3 s532 result is reproducible on the rebased branch | fixture dump (below) re-ran N3's s532 REAL/SHUF protocol verbatim on `9b322d5` + W4 (OFF): disc4 0.467 / 0.163; DISC_0.5 (a) 0.307 / -0.259 (diff +0.566); FULL -0.400 / 0.507 (-0.907) | **holds exactly** (N3: +0.57 / -0.91). This also shows that the W3 rebase `042895a -> 7428da3` and W6a (OFF) do not change behaviour on this protocol |

## 2. What was built (branch only)

- **`E3TrajectorySelector.score_trajectory`**: when `use_e3_discounted_aggregation` is on and `_score_depth_limit is None` (the PLANNED read), it dispatches to `_score_trajectory_discounted`.
  - That method reads the same scorer at every depth L = 2..Lmax (Lmax = z_world sequence length), passing all kwargs through, and restores the depth limit in a try/finally.
  - It combines the reads in float64 in N3's own order and casts back.
  - gamma = 1 telescopes exactly to the full read. gamma outside (0, 1] raises (gamma 0 would collapse onto the habit read).
  - The result stays differentiable.
  - Cost: Lmax - 1 scorer calls per planned score (30 at horizon 30).
- **Unchanged:** the HABIT read, the commit gate (ARC-016), channel weighting and the hippocampal CEM scorer (`hippocampal._score_trajectory` is a separate scorer).
- **Documented side effect:** `_last_traj_components` / `_last_commensurability_raw` come from the last per-depth call (J_Lmax), i.e. they describe the full-horizon channels, not the discounted combination.
- **Knobs (3 sites + PROBED):** `use_e3_discounted_aggregation` (False) and `e3_aggregation_gamma` (0.5), on `E3Config`, plus the `REEConfig.from_dims` signature and assignment.

## 3. Contracts (`tests/contracts/test_w4_e3_aggregation.py`, 11) and the test half

Fixture `tests/fixtures/w4_n3_s532.pt` (163 KB):
- the N3 s532 REAL and SHUF W3 heads (`world_transition` + `world_action_encoder`);
- the probe agent's `harm_eval_head`;
- for 41 probe states: z0, the pool[0] actions and the true next z_world per class;
- state 0's native pool actions.

It was dumped by `probes/w4/w4_dump_fixture.py`, which runs the N3 protocol verbatim (`n3_probe_w4copy.py` = `probes/n3/n3_probe.py` with only the worktree path changed). The tests re-roll the fixture with ree_core's own `E2FastPredictor` (0.0 max abs diff to the probe agent's rollouts) and score with ree_core's own E3 (`residue_field` None; config identical to the probe agent's).

| contract | what | pre-build (`9b322d5`) |
|---|---|---|
| W4-01 defaults | False / 0.5 on E3Config and from_dims | FAIL |
| W4-01 OFF read | planned read == explicit full-depth read, gamma unread (torch.equal) | pass (OFF is pre-build behaviour) |
| W4-01 OFF agent | a default agent and an explicit-OFF agent with gamma 0.7 act identically over 12 steps | FAIL (knob absent) |
| W4-02 parity | ON == N3's `depth_scores` + `aggregate` (copied verbatim) DISC_0.5 on the recorded 32-candidate native pool, rel < 1e-6; not vacuous (differs from FULL) | FAIL |
| W4-02 gamma | gamma 1 == full read exactly; 0 / -0.5 / 1.5 raise; limit restored | FAIL |
| W4-02 grad | differentiable; limit restored | pass |
| W4-03 habit | inside `select()` with SD-081 arbitration, the 8 habit-read scores are byte-identical ON vs OFF, and the planned range changes | FAIL |
| W4-03 reach | perturbing world step 5 moves the ON planned score of that candidate only; the habit read does not move | pass (FULL also reaches) |
| W4-03 ranking | Spearman(ON, habit) < 0.99 on the native pool, and closer to habit than FULL is | FAIL |
| W4-04 reduced gate (a) | on the 41 recorded states, REAL minus SHUF Spearman(J_pred, J_true) > 0.15 with ON (**+1.029**: 0.759 vs -0.271), while the full read FAILS the same bar (**-0.037**: 0.080 vs 0.117; dataset canary). I1 `e3_choice_quality` | FAIL |
| W4-05 plumb | from_dims -> agent.e3.config; an ON agent acts 12 steps | FAIL |

Results: **11/11 pass on the build and 8/11 fail on the pre-build tree.** The three pre-build passes are properties the pre-build code already has. There is no gate (c) contract.

**In-situ parity** (probe agent's own E3, residue field included): ON vs N3's DISC_0.5 on all 41 native pools gives max relative difference **4.4e-8**.

**Commit gate:** the full contracts run locally (`REE_PRECOMMIT_CONTRACTS_TARGET=local`) under the Mac probe lock: 5921 passed, 25 skipped, 3 xfailed (24m55s); `git show --stat 1b013d6` = the 5 W4 files only.

## 4. Findings

- **F1: the planned/habit contrast is thin when there is no residue field.** In the standalone E3 (residue_field None):
  - DISC_0.5 ranks the recorded native pool at Spearman 0.94 against the habit read, with the same argmin (FULL: 0.62).
  - On the scaffold pool (candidates differ in the first action only), the DISC_0.5 pick differs from the habit pick at 2/41 states.
  - N3's 40-65% disagreement was measured with the probe agent's residue field. That term is large: the standalone and probe-agent FULL J differ by up to **39.3**, the Phi_R contribution. So most of the deep planned/habit contrast lives in the residue term.
  - gamma 0.5 has effective depth ~2 by design. SD-081 P1 holds nominally (the planned read reads to Lmax and W4-03 reach shows it), but the size of the contrast depends on gamma and residue. The W4-03 ranking contract pins it as "not identical", not as large.
- **F2: gate (a) is stronger standalone than in N3 at s532** (+1.03 vs +0.57). The residue term, a head-independent common term, dilutes the head's effect on the ranking. This is a descriptive reading of one seed, not a new gate.
- **F3: the scorer cost is Lmax - 1 times per planned score.** No runtime was measured on a full agent loop here. A1's CPU-h estimate should re-measure it with W4 ON.

## 5. Decisions held for the user (none taken here)

- **Gate (c) re-spec** (N3 record options): (i) choice quality vs the blind head; (ii) gate W4 on (a) alone (N3's analysis recommends this; under (ii) W4 would be gate-passed on DISC_0.5 4/5); (iii) blind twin (moves the defect). This changes the campaign rule that no D2 reading counts until W4's gate passes, which is why it is held.

## 6. Reproduction

- Branch commit `1b013d6`: `pytest tests/contracts/test_w4_e3_aggregation.py` (~3 s).
- Fixture: `probes/w4/w4_dump_fixture.py` (seed 532, ~3 min on the Mac; it expects a ree-v3 worktree at `.scratch/wt-w4`). Report: `probes/w4/dump_report.json`.
