# Failure autopsy: V3-EXQ-1093 (MECH-428 parent-statistic ESS sweep, diagnostic PASS)

- Run: `v3_exq_1093_mech428_parent_stat_ess_sweep_20260924T180739Z_v3` (ree-worker-3, 78.7 s, substrate 83ca4d44 / bf16cd23, stable)
- Generated: 2026-09-25T01:55:54Z, session orchc0925-autopsyB-1093 (orchestrate-20260924-1707)
- Status: **confirmed** under the user's standing delegation via orchestrate-20260924-1707. The design, including the user's option (b) sub-ceiling C1 (rec-20260924-701216a5), was fixed before data. Every branch is non_contributory for MECH-428 by construction, and every control holds. No claim status or scope moves.
- Indexer adjudication: none flagged. Autopsy owed because `experiment_purpose: diagnostic`.
- Chip: chip-autopsy-v3-exq-1093. Context: GFLAG-0476, GFLAG-0464.

## 1. Facts

**Dry-run gate.** 0 dry, 1 real (run and family). The pilot (seeds 101/102) wrote no manifest. `validate_recording.py` OK.

**What it measures.** One scripted 1600-tick waypoint walk per seed (5 seeds). The walk uses SD-094 env fixes, SD-070 P0 warmup and alpha_world 0.9, and credits pre-arrival z_world through the real `notify_subgoal_attainment`. The parent attractor is then replayed exactly (w @ Z) for 12 (alpha, decay) cells at N = 400 and 1600. The statistic is S = 1 - cos(parent_credited, parent_control). Controls are K=32-averaged and time-local, and the null is a circular time-shift that re-runs parent construction. A seed-cell "separates" when S exceeds its null p95. There is no consumer (parent_goal_weight 0).

| Gate / criterion | Measured | Threshold | Met |
|---|---|---|---|
| PR0 sense_flat == act() on z_world | 0.0 | <= 1e-6 | yes |
| PR1 credits by N=400 (worst seed) | 58 | >= 30 | yes |
| PR2 replay == real GoalState (min cos) | 0.99999982 | >= 0.99999 | yes |
| PR3 uniform-ceiling positive control | 5/5 | >= 3/5 | yes |
| PR4 random-credit negative control, max over 26 cell x N | 0/5 | <= 2/5 | yes |
| **C1** (load-bearing) max over sub-ceiling cells (ESS <= 0.5 n_att) | **0.8** at N=400 cells a0.1_d0 (ESS 18.9) and a0.05_d0.005 (ESS 23.7); 1.0 at the binding a0.025_d0_N1600 (ESS 78.7, near the uniform ceiling at that N) | >= 0.6 | yes |
| C2 (reported) default cell (0.05, 0.005, N=400) | 0.8 (pct 100/86.5/100/99/96.25) | >= 0.6 | yes |
| C3 (reported) Spearman(ESS, pct) | 0.96 | >= 0.5 | yes |

C1 does not rest on its binding high-ESS cell. At N=1600 that cell is close to PR3, because ESS 78.7 exceeds the whole N=400 uniform ceiling of 58-68. The PASS instead holds on two N=400 eligible cells.

**Seed heterogeneity (red-team recompute).** Seeds 42 and 44 separate down to ESS ~7.8. Seed 43 clears only at ESS >= ~36 and fails 15 of 24 cells. The pooled crossover of about 15-24 therefore hides a wide per-seed spread.

**Cell map (sep_frac by ESS):**

| ESS | ~8-9 | 14.5 | 19 | 24 | 33-39 | 41-62 | 79-218 |
|---|---|---|---|---|---|---|---|
| sep_frac | 0.4 | 0.4 | 0.8 (N400) / 0.6 (N1600) | 0.8 (N400) / 0.6 (N1600) | 0.8-1.0 | 0.8-1.0 | 1.0 |

**Effect size.** S is 0.0014-0.0057 everywhere, so the credited and control parents are about 0.998 cosine-similar. Separation is statistical and small.

**Decay caps ESS.** At the default decay 0.005, ESS barely grows with event count for alpha >= 0.05 (a0.05: 23.7 -> 23.8; a0.1: 14.6 -> 14.5). It grows modestly for alpha <= 0.025 (32.9 -> 34.8, 41.2 -> 47.8, 44.4 -> 54.4). At decay 0 it grows (a0.025: 52.2 -> 78.7).

**Unmatched 884c form (reported only).** At the default cell the true arm separates 1/5 and the negative control reaches 2/5 on some cells. Under the matched form these are 4/5 and 0.

**The driver's own pre-data predictions (scorecard):**
- P1 ("every sub-ceiling cell with ESS >= 14 separates >= 4/5"): **failed** as stated. a0.1_d0.005 (ESS 14.5) is 2/5; two N=1600 cells at ESS 19 and 24 are 3/5.
- P2 ("crossover in ESS 8-15"): **failed** on the range. The measured crossover is about 15-24.
- P3 (default cell separates on a majority): **held** (4/5).
- P4 (negative control never separates on a majority): **held**.

The two-seed pilot was optimistic.

## 2. Hypotheses (pre-registered in the queue entry, ree-v3 e942c9b)

- **H1** (ESS-bound; the default cell at chance): the specific prediction is **refuted** (4/5). Its ESS-ordering half survives (rho 0.96).
- **H2** (884c's at-chance reading was a single-draw, confounded-null instrument limitation): **supported** on its main point (matched 4/5 vs unmatched 1/5). Its crossover band is too low.
- **H3** (no content even at the ceiling): **refuted** (PR3 5/5).

## 3. Claim layer

MECH-428 (candidate, standard, diagnostic_evidence_adjudicated true, pending_retest_after_substrate true). Its WWA NON-DEGENERACY PRECONDITION has three clauses: attainment, a 626b forced-seed control, and an achievable range that separates from a re-constructed null. 1093 satisfies **attainment** and **achievable range**. It does not address the forced-seed clause or the CONFIRMING clause's live consumer. There is no consumer, the policy is scripted, and there is no NO-SUBGOAL arm. Those parts are owed by EXP-0710 / GFLAG-0464 (the SD-092 E3 consumer landed default-off at ree-v3 52096b7) and by the never-run V3-EXQ-884a.

The run rules out the FALSIFYING shape at the instrument level: "no sweep point yields separation". It cannot confirm the claim.

**The what_would_answer text is partly wrong, in two places (red-team F1).**

1. The DISPOSITION head clause says: "The parent statistic is degenerate at registered defaults (... correctly-nulled form at chance because the EMA effective sample size is ~20)".
2. The Stale-falsifier correction says: "the correctly-nulled form reads at chance at parent_goal_alpha=0.05".

Under the matched instrument, the default operating point separates on 4/5 seeds, so the at-chance reading was mainly instrument. Separation is still ESS-ordered, however, and seed-dependent, and the default (ESS ~24) sits on the crossover (0.6 at N=1600). Both replacements, with the head clause softened to "two of the three forms", are in JSON `recommended_wwa_disposition_correction`. Applying only one would leave the WWA self-contradictory.

Bears-on, not adjudicated: the same DISPOSITION's "_z_goal_parent has NO downstream consumer" has been stale since ree-v3 52096b7. GFLAG-0464 owns that correction.

## 4. Biological reference

The closest reference is recency-weighted accumulation of subgoal-completion credit onto a superordinate goal representation: the PFC abstraction hierarchy and hippocampal-prefrontal schema building. The EMA-with-decay form is an engineering choice. The biology does not fix its effective sample size, so this is an instrument/parameterisation question, not a translation failure. Lit coverage is partial on the accumulation window. No lit-pull is owed for this diagnostic.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact / not exercised | non-degeneracy diagnostic; 2 of 3 precondition clauses satisfied |
| Biological reference | partial | EMA window is an engineering form |
| Prerequisites | partial | P0 ran. z_world is read through the untrained world_obs_encoder pre-projection (SD-ZWORLD-SENSE-PATH-PARITY) and has no waking objective (GFLAG-0491), so the run shows separability, not semantic content |
| Implementation | complete (for what is measured) | PR2 exact replay; PR0 exact sense path |
| Environment | adequate | 58-68 credits by N=400 |
| Measurement | adequate | matched controls and time-shift null; negative control 0 everywhere; positive control 5/5. C1 can fail with PR3 met. Conservative bump bias (red-team pass 1 F2) |
| Integration | coupled but inert BY DESIGN | nothing reads the parent (parent_goal_weight 0); owed by EXP-0710 / GFLAG-0464 |
| Scale | adequate | 5 seeds, 400 perms per seed-cell; the absolute margin is small |

**Failure-location:** n/a. This is a PASS on an instrument question, and no REE failure is asserted.

## 6. Learning extracted

- **Measurement gap closed:** 884c's at-chance reading at the default operating point was mainly an instrument artefact.
- **Parameterisation dependency surfaced:** separation is ESS-ordered with a crossover near ESS 15-24, and the crossover is strongly seed-dependent (one seed in five needs ESS >= ~36). At the default alpha 0.05, SD-092's default decay 0.005 caps ESS near 24 however many events accrue, so the default sits on the crossover.
- **Scope:** the separation is small (parents ~0.998 cosine) and is measured in a largely untrained z_world. It shows no semantic content and no behavioural effect.
- **Prediction audit:** pilot-derived crossover bands (2 seeds) were optimistic on held-out seeds. Treat such bands as leads.

## 7. Routing

**queue-experiment**, with no same-question re-run. The instrument question is answered. Governance:

1. Apply the MECH-428 evidence_quality_note and BOTH what_would_answer replacements (JSON exact text). Advance live_status.evidence.from to this artifact.
2. Resolve GFLAG-0476 with the correction. Its "more likely instrument than ESS ceiling" is right on the default cell but overstated: ESS still orders separation and the default is marginal.
3. When EXP-0710 (behavioural consumer leg) and V3-EXQ-884a are queued, carry the operating-point guidance: ESS >= ~36 (e.g. decay 0, alpha <= 0.05), which the weakest seed needs, and report ESS per seed.
4. Apply `hypothesis_space_ledger_pending`: register the new qid `mech428_parent_statistic_achievable_range`. H1 is eliminated, H2 confirmed, H3 eliminated. Each is pre-registered at the queue commit e942c9b (2026-09-24T17:33:14Z, per-leg `pre_registration_source`) and resolved at the run (18:07:39Z). All three axis families already exist. Step 9b was not written directly because the registry is held by orchc0925-autopsyA-1083.
5. `chip-20260917-mech428-parent-goal-alpha-sweep`: already resolved done (2026-09-24T17:36:13Z). Nothing owed.

No substrate entry is owed (`action: none`).

**Re-derive brake:** not fired. This is an explicit producer release: an instrumentation PASS that owes no build. MECH-428's prior count is 1 (884).

**Granularity-debt trigger:** does not fire. No MECH-428 target reads weakened.

Follow-on is not chipped (autopsy rule).

## 8. Step 7b / 7c

- 7b: on the first draft, 1 fire: C2 `waypoint-proximity-field-observable`. It does not fire on the final draft (0 fires). **Dismissed** anyway: this run scripts the walk, so the field is not on its path. The entry belongs to the behavioural leg, where SD-WAYPOINT-FIELD is built and reader-validated (V3-EXQ-1004); qid `waypoint_field_consumer_reach` owns that question. C5 and C7 were inapplicable.
- 7c: fable, CONTESTED, 1 finding accepted plus hygiene (section 9).

## 9. Red-team (7c)

Model: **fable** (cross-model; this session runs Opus 5.5). Verdict: **CONTESTED** at the recommendation level, on one defect. The science, the PASS, the direction, the routing, the brake release and the ledger states all stand. Recomputed from per-seed cells, everything matches: C1 set 15 (5 + 10); max 1.0 at a0.025_d0_N1600 (ESS 78.67); min separating ESS 18.95; N=400 eligible cells 0.8 / 0.8; Spearman 0.9613; default cell 0.8 / 0.6; per-seed s_obs/p95 0.82-2.35. The brake snippet gives 1 prior hit (884). e942c9b is 17:33:14Z, before the 18:07:39Z run.

- **F1 (CONTESTED, accepted):** MECH-428's what_would_answer says "at chance" twice, and its head clause asserts degeneracy for all three forms. Correcting only the DISPOSITION sub-clause would leave the WWA self-contradictory. Confirmer: `what_would_answer.count('at chance') == 2`. Disposition: the correction now carries both replacements and softens the head clause.
- **Hygiene (all applied):**
  - decay-caps-ESS scoped to alpha >= 0.05;
  - seed heterogeneity stated (seed 43 needs ESS >= ~36);
  - stale 7b block corrected (0 fires on the final draft);
  - per-leg `pre_registration_source` added;
  - C1 lead reordered to the N=400 cells;
  - alpha-sweep chip already done;
  - axis families present.

Record: `.scratch/orch-20260924-1707/autopsy/redteam_1093.md` (scratch, not committed).
