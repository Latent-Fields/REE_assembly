# Morning Agenda -- 2026-05-12

Generated: 2026-05-12T04:22:43Z

---

## Queue Status
- Total pending: **0** (Mac: 0 | PC: 0 | EWIN: 0 | any: 0)
- **ALERT: Queue empty -- no pending experiments.** Runners on all machines will idle. Queue new experiments via `/queue-experiment` before starting any runner.

---

## Experiments Awaiting Review (5 indexed / 1 runner-only)

### V3-EXQ-549 -- `arc066_tonic_vigor_discriminative_pair` -- FAIL
- **Claims tested:**
  - **ARC-066** (candidate, exp_conf=0.324, lit_conf=0.789, quadrant=plausible_unproven; prior 0 supports / 1 weakens after this run)
  - **MECH-320** (candidate_substrate_landed, exp_conf=0.324, lit_conf=0.000, quadrant=speculative; 0 supports / 1 weakens)
- **Key metrics:** C1 fail (lift=0.0 both seeds), C2 fail, C3 pass (gates not clamping). ARM_OFF action_density=1.0 (saturated noop-free policy) -> v_t window empty (n_windows=0) so pearson_r=0, gate_product_mean=0.
- **Classification:** evidence (discriminative pair, pre-registered C1/C2/C3 thresholds).
- **Governance impact if confirmed:** ARC-066 / MECH-320 first FAIL -- would push toward `weakens` for capacity-keyed target-firing-rate vigor scaling. Note: ARM_OFF saturated; this may be a substrate-readiness issue, not a true falsification. Consider `/diagnose-errors` before accepting as weakens evidence.

### V3-EXQ-550 -- `zgoal_monostrategy_falsifier` -- FAIL
- **Claims tested:** **MECH-269** (candidate, exp_conf=0.000, lit_conf=0.873, quadrant=plausible_unproven; no prior exp entries)
- **Key metrics:** outcome=FAIL but evidence_direction=`supports` -- the experiment is a falsifier; the FAIL of the falsifier criterion supports MECH-269 V_s monostrategy claim.
- **Classification:** evidence (falsifier -- inverted interpretation).
- **Governance impact if confirmed:** First experimental support for MECH-269 (currently 0.000 exp_conf). Substantial lift toward leaving plausible_unproven quadrant.

### V3-EXQ-543d -- `arc062_mech260_factorial_falsifier` -- FAIL
- **Claims tested:**
  - **ARC-062** (candidate, exp_conf=0.325, lit_conf=0.865, quadrant=plausible_unproven; 0 supports / 1 weakens)
  - **MECH-309** (candidate, exp_conf=0.000, lit_conf=0.889, quadrant=plausible_unproven; flagged non_contributory by this run)
- **Key metrics:** Per-claim split -- ARC-062 weakens, MECH-309 non_contributory. ARM_0 mean_reef_fraction=0.29, abs_rho mostly below threshold (1/3 seeds above). Pre-registered D2 + D3 cross-arm attributions did not pass.
- **Classification:** evidence (2x2 factorial monomodal-collapse falsifier).
- **Supersedes:** V3-EXQ-543c (this is the iteration adding dACC arm).
- **Governance impact if confirmed:** ARC-062 second weakens (would tip exp_conf below 0.3); plan-of-record decision-log entry 2026-05-11 indicates next-step routing depends on D-pattern (FAIL all-D-null -> option-2 head-input augmentation; FAIL D1-only -> substrate-rationale review).

### V3-EXQ-540a -- `mech307_optionb_3arm_conjunction_decomposition` -- FAIL
- **Claims tested (per-claim direction):**
  - **MECH-307** (candidate_substrate_landed, exp_conf=0.473) -- mixed
  - **MECH-216** (provisional, exp_conf=0.583) -- supports
  - **MECH-205** (stable, exp_conf=0.861) -- supports
  - **MECH-093** (provisional, exp_conf=0.758) -- non_contributory
  - **SD-014** (candidate, exp_conf=0.000) -- non_contributory
  - **MECH-295** (candidate, exp_conf=0.000) -- weakens
- **Key metrics:** ARM_0_off n_conjunction_fire_ticks_total=0 / read_opportunities=8000 (rate=0). Schema_wanting_writes_mean=2711 in ARM_0. Approach_commit_rate=1.0. Per-claim direction overrides correctly applied.
- **Classification:** evidence (3-arm decomposition of MECH-307 conjunction gate).
- **Supersedes:** V3-EXQ-540 (initial version).
- **Governance impact if confirmed:** MECH-205/MECH-216 each pick up another supports entry (MECH-205 already confirmed_established); MECH-295 first exp entry is weakens (would still leave it in plausible_unproven given high lit_conf); MECH-307 picks up mixed (currently 1 mixed only).

### V3-EXQ-540b -- `mech307_conjunction_threshold_sweep` -- FAIL
- **Claims tested:**
  - **MECH-307** (candidate_substrate_landed, exp_conf=0.473) -- mixed
  - **MECH-295** (candidate, exp_conf=0.000) -- weakens
- **Key metrics:** ARM_default schema_wanting_writes_mean=2711, conjunction_fire_rate_mean=0.0 across all threshold settings; z_beta_excursion_mean=0.151; harm_paired_surprise_writes=232; nonharm_surprise_writes=3114; surprise centers populated (59 pos, 82 neg, 82 split). Threshold sweep did not yield conjunction firing.
- **Classification:** evidence (threshold sweep follow-up).
- **Supersedes:** V3-EXQ-540a (sweep variant).
- **Governance impact if confirmed:** Reinforces MECH-307 mixed signal and MECH-295 weakens; pattern with EXQ-540a suggests conjunction-gate substrate may be unreachable under current monostrategy regime -- pairs with MECH-269 V_s landing.

---

## Errors to Diagnose (10)

The unique-base undiagnosed ERRORs in `runner_status.json` with no queued fix and no lettered successor:

| Queue ID | Completed | Claim | Title | Reason |
|---|---|---|---|---|
| `V3-EXQ-544` | 2026-05-10 | MECH-313 | MECH-313 (ARC-065) stochastic_noise_floor substrate-readiness diagnostic (UC1-UC5) | No runner sentinel emitted; exit=0; secs=2.8 |
| `V3-EXQ-542` | 2026-05-09 | ARC-062 | ARC-062 Phase 1 gated-policy substrate-readiness diagnostic | No runner sentinel emitted; exit=0; secs=2.2 |
| `V3-EXQ-538` | 2026-05-08 | -- | SD-049 Phase 2 reef behavioural validation, sleep-on ablation (paired) | Non-zero exit code -15 (killed) |
| `V3-EXQ-244a` | 2026-05-06 | -- | MECH-165 reverse replay diversity scheduler validation (redesign) | Non-zero exit code -15 (killed) |
| `V3-EXQ-495` | 2026-04-28 | MECH-163 | MECH-163 V3 full-completion gate -- VTA / hippocampally-planned arm | Non-zero exit code -15 (killed) |
| `V3-EXQ-449c` | 2026-04-24 | -- | MECH-074b BLA retrieval bias on action selection -- V_s-gated | Non-zero exit code 1 |
| `V3-EXQ-455a` | 2026-04-23 | -- | SD-032a salience coordinator behavioural -- V_s-enabled re-run | Non-zero exit code 1 |
| `V3-ONBOARD-smoke-ree-cloud-1` | 2026-04-06 | -- | Onboarding smoke test -- ree-cloud-1 (Hetzner CX22) | Non-zero exit code 1 |
| `V3-ONBOARD-smoke-EWIN-PC` | 2026-04-05 | -- | Onboarding smoke test -- EWIN-PC (Eoin) | Non-zero exit code 1 |
| `V3-EXQ-008` | 2026-03-17 | SD-003 | SD-003 Larger World + 3x3 Observation (V2-era) | Non-zero exit code 1 |

Top of list: **V3-EXQ-544 / V3-EXQ-542 / V3-EXQ-538** are the freshest and most actionable -- likely need `/diagnose-errors`. Note: `pending_review.md` also lists **V3-EXQ-552** (FAIL, index stale) -- re-run `build_experiment_indexes.py` to clear or escalate.

---

## Governance Agenda (9 recommendations)

| Claim | Status | Recommendation | Supports/Weakens/Mixed | exp_conf |
|---|---|---|---|---|
| **ARC-066** | candidate | `hold_pending_v3_substrate` | 0 / 1 / 0 | 0.324 |
| **ARC-067** | candidate | `hold_pending_v3_substrate` | 0 / 0 / 0 | 0.000 |
| **ARC-068** | candidate | `hold_pending_v3_substrate` | 0 / 0 / 0 | 0.000 |
| **ARC-070** | candidate | `hold_pending_v3_substrate` | 0 / 0 / 0 | 0.000 |
| **ARC-071** | candidate | `hold_pending_v3_substrate` | 0 / 0 / 0 | 0.000 |
| **MECH-320** | candidate_substrate_landed | `hold_pending_v3_substrate` | 0 / 1 / 0 | 0.324 |
| **Q-043** | open | `hold_pending_v3_substrate` | 0 / 0 / 0 | 0.000 |
| **Q-044** | open | `hold_pending_v3_substrate` | 0 / 0 / 0 | 0.000 |
| **Q-045** | open | `hold_pending_v3_substrate` | 0 / 0 / 0 | 0.000 |

All 9 are `hold_pending_v3_substrate`. ARC-066 and MECH-320 now have first exp evidence from EXQ-549 (weakens) -- substrate is "landed" for MECH-320, so the hold may be reviewable once EXQ-549 is interpreted (saturation issue noted above).

---

## Active Plans Heartbeat (6 plans)

| Plan | Phases in-flight | Blocked | Paused | Stale rows | Last decision |
|---|---|---|---|---|---|
| arc_062_rule_apprehension_plan | 2 | 1 | 0 | 0 | 2026-05-11 |
| commitment_closure_plan | 4 | 2 | 0 | 0 | 2026-05-09 |
| goal_pipeline_plan | 2 | 2 | 0 | 0 | 2026-05-11 |
| sd033_governance_plan | 0 | 0 | 0 | 0 | -- (8/8 nodes done) |
| self_attribution_plan | 1 | 3 | 0 | 0 | 2026-05-11 |
| sleep_substrate_plan | 4 | 2 | 0 | 0 | 2026-05-10 |

No stale rows (>7 days untouched). No plan-staling flag triggered (no plans with > 14 days since last decision AND phases in-flight). `sd033_governance_plan` is effectively complete (8/8 nodes done) -- candidate for status flip to `done` at front-matter level.

Notable cross-plan signal: **`self_attribution_plan` has 3 of 5 nodes blocked**, all on MECH-269 V_s monostrategy landing and MECH-307 conjunction architecture (same upstream as `sleep_substrate_plan` GAP-1 and EXQ-540a/b results just queued for review). MECH-269 V_s monostrategy is the central bottleneck across self_attribution, sleep_substrate, and the SD-029 retest gate.

---

## Literature Pull Candidates (Top 5)

Only 2 backlog items explicitly carry `evidence_needed: literature`:

| # | Backlog ID | Claim | Subject | Priority | Existing entries |
|---|---|---|---|---|---|
| 1 | EVB-PINNED-Q019 | Q-019 | Three-Gate BG Architecture lit extraction (O'Reilly/Frank 2006, Hazy/Frank/O'Reilly 2007, Aron 2007, Brittain/Brown 2014, Buckner 2008, Crick 1984/Zikopoulos) | (pinned) | 1 |
| 2 | (untagged) | MECH-320 | Tonic vigor capacity-keyed firing-rate gain (pairs with EXQ-549 review) | -- | 0 |

All 224 other high/medium priority backlog items request `experimental` evidence rather than literature. MECH-320 has 0 existing targeted_review_* dirs -- the substrate-landed claim has zero literature backing; consider a `/lit-pull` before interpreting the EXQ-549 weakens entry.

---

## Serve.py Status
- **RUNNING on port 8000** (PID 38826, Python listener).

---

## Blocked Items

- **`pending_review.md` lists V3-EXQ-552 as FAIL with stale index** -- script flagged `?` (index stale). Re-run `python evidence/experiments/scripts/build_experiment_indexes.py` to refresh, or treat as a runner-only entry needing manual discussion.
- **Indexer warnings** during governance.sh: 5 SD-029 / MECH-256 runs (EXQ-433c, EXQ-523b, EXQ-537 x2) and several legacy multi-claim runs (EXQ-074e/f, EXQ-076e/f, EXQ-243, EXQ-038, EXQ-046, EXQ-242, EXQ-247, EXQ-397, EXQ-397c) are missing `evidence_direction_per_claim` -- blanket direction applied. Non-blocking but contaminates per-claim evidence ledger. Schedule a backfill pass.
- **Canonical-bridge timestamp drift** flagged for `jepa_uncertainty_channels`, `v3_exq_074f`, `v3_exq_133`, `v3_exq_223`, `v3_exq_484`, `v3_exq_523b`, `v3_exq_537` -- multiple manifest variants for the same experiment_type. Investigate when next touching the index.
- **No active TASK_CLAIMS collisions** -- pipeline ran fully.
