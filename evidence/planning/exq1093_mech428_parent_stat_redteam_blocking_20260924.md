# V3-EXQ-1093 (MECH-428 parent-statistic ESS sweep): red-team BLOCKING, parked pending a decision

**Status: NOT QUEUED. BLOCKED pending decision chip `chip-20260924-decision-exq1093-c1-pr3-identity`.**
No queue entry, no coordinator row, no manifest. V3-EXQ-1093 stays reserved for this driver.

- **Written:** 2026-09-24
- **Session:** `metaworker-science-20260924-mech428-alpha-diag`, a headless science worker in campaign
  `science-20260924-mech428-alpha-diag` (orchestrator `orchestrate-20260924-0808`).
- **Chip:** `chip-20260917-mech428-parent-goal-alpha-sweep`. Unclaimed and left open, with a note
  pointing here.
- **Driver (parked):** `ree-v3/experiments/_scratch/v3_exq_1093_mech428_parent_stat_ess_sweep.py`.
  Its module docstring carries the full design, the pilot and the pre-registered prediction.
- **Pilot raw data:** `ree-v3/experiments/_scratch/v3_exq_1093_pilot_seeds101_102.json`
- **Authority carried forward:** `exq884c_mech428_c1_ema_self_overlap_redteam_blocking_20260916.md`

---

## 1. What was built, per the orchestrator's decisions (Q-MECH428 -> A)

- The run is an instrument / non-degeneracy diagnostic for the achievable-range clause of MECH-428's
  WWA precondition. `evidence_direction` is `non_contributory` on every branch, and no consumer is armed.
- Sweep: `parent_goal_alpha` {0.20, 0.10, 0.05, 0.025, 0.01, 0.005} x `parent_goal_decay`
  {0.005, 0} x N_STEPS {400, 1600} (event count ~60 -> ~245). 5 seeds (42-46).
- Statistic: S = 1 - cos(parent_credited, parent_control). s_obs is averaged over K=32 control
  draws, and each null sample carries the same K-average.
- Carried forward from 884c: pre-arrival crediting via the real `notify_subgoal_attainment`,
  `alpha_world` 0.9, SD-094 env flags, and the 884c driver-bug fixes (crc32 seeding, a real
  random-credit negative control scored on its own partition).
- Controls:
  - PR0: sense-path equivalence
  - PR1: attainment
  - PR2: replay fidelity against a real GoalState per cell
  - PR3: uniform-weight ESS-ceiling positive control
  - PR4: random-credit negative control
- Load-bearing criterion: C1.

## 2. Instrument corrections this session MEASURED (they survive the refusal)

1. **The 884c control/null form is confounded by temporal structure.** Recency weighting concentrates
   the parent on the latest credits. A control drawn from anywhere in the run therefore differs from
   the credited parent by whatever z_world content persists in time. Measured: under that unmatched
   form (K-averaged), the RANDOM-CREDIT negative control reached pct 98.2-99.8 at N=400 on held-out
   seed 102. So controls must be time-local. The driver uses the ticks between each credit's
   previous and next credit, which is parameter-free.
2. **A within-window null is biased too.** The credited tick sits in the window interior, while a
   null pseudo-credit drawn uniformly inside the window does not. Measured: the negative control
   reached pct 94-98 on seed 102 at N=1600. The fix is a **circular time-shift null**: shift the
   whole credited set by a random delta, keep the credit order and weights, and apply the same
   window rule. With it, the negative control separated in 0 of 52 cell x N combos on both
   held-out seeds (max pct 92.5).
3. **Sense path.** `agent.act()` costs ~1.7 s per tick on a contended 2-core box, and `sense_flat()`
   costs ~9 ms. A twin carrying the FULL agent state_dict and running `act()` for 30 ticks matches
   `sense_flat()` z_world exactly (max |diff| 0.0). The twin has to copy the full state, because
   `sense()` also runs the agent-level random `world_obs_encoder` / `body_obs_encoder` outside
   `latent_stack`. That is the open cosmetic item SD-ZWORLD-SENSE-PATH-PARITY. A latent_stack-only
   twin differs by up to 0.26 per element.

## 3. The pilot, and a premise it contradicts

Held-out seeds 101/102, full budgets, instrument as in section 2:

| | seed 101 | seed 102 |
|---|---|---|
| credits by N=400 / 1600 | 59 / 248 | 66 / 245 |
| uniform ceiling S vs p95, N=1600 | 0.00283 vs 0.00016 (pct 100) | 0.00303 vs 0.00029 (pct 100) |
| **default cell (0.05, 0.005, N=400)** | **pct 100, ESS 23.9** | **pct 100, ESS 24.9** |
| alpha=0.2 cells (ESS 7.7-9.0) | 3 of 4 separate | 1 of 4 separate |
| real cells with ESS >= 14 | all separate (pct 97.8-100) | all separate |
| negative control, max pct over 26 combos | 71.8 | 92.5 |

**The premise this contradicts.** The chip, its pre-flight ("headroom is bounded by event count"),
and claims.yaml MECH-428's DISPOSITION ("correctly-nulled form at chance because the EMA effective
sample size is ~20") all attribute 884c's at-chance S at the default operating point (pct
78.0 / 63.0 / 86.5, K=1) to an ESS ceiling. On two held-out seeds, the default cell separates at
pct 100 once s_obs is K-averaged and the null is time-matched. The unmatched K=32 form also
separates the true arm there, at pct 99.8 / 99.2. The at-chance reading is therefore more likely a
single-control-draw limitation than an ESS ceiling. This is n=2 with a changed instrument, so it is
a lead, not a verdict. It is raised to /governance as a `stale_note` flag rather than written into
the claim.

## 4. Red-team (fable, one pass, foreground): BLOCKING. Findings and dispositions

Each finding was checked against the source and the pilot data before being accepted.

- **F1 BLOCKING, confirmed, NOT fixed.** C1 is implied by PR3 by construction.
  - The real cell (alpha 0.005, decay 0) has near-flat weights, so it effectively *is* the uniform
    ceiling: ESS 58.6 vs 59 at N=400, S 0.002414 vs 0.002422, p95 0.000744 vs 0.000749.
  - PR3 is evaluated before C1. So C1 can never fail on its own.
  - The genuine negative ("no achievable range even at the ceiling") routes to
    `substrate_not_ready_requeue`. That is a harness-defect label, and it would re-queue an
    identical run. `parent_statistic_no_achievable_range_at_registered_settings` is unreachable.
  - Secondary: the PR3 reachability anchor, built on two pilot (s_obs, p95) pairs, certifies
    little.
  - Left unfixed because the campaign's consent rule forbids re-designing around a red-team refusal
    unilaterally. See section 5.
- **F2 CONTESTED, accepted as conservative.** In the shift null, the bump rule puts ~15% of
  pseudo-credits on the arrival tick after a credited one, and bumped pseudo-credits lose their
  nearest control neighbour. Both push the null up, so they can bias where the crossover lands but
  never flip a separation. The random-credit control shares the effect, so PR4 cannot see it. The
  confirmer is now recorded per seed x N (`null_bump_frac`): 0.08-0.16 in the smoke run, matching
  the reviewer's 14.5-15.3% estimate.
- **F3 CONTESTED, fixed.** The reported-only unmatched null drew controls from a pool that still
  contained its own pseudo-credited ticks, which is null-side self-overlap. They are now excluded.

## 5. The decision owed (chip `chip-20260924-decision-exq1093-c1-pr3-identity`)

How C1 and PR3 should relate. Each option changes what a PASS or FAIL is allowed to mean:

- **(a) Re-route only.** PR3-unmet becomes the scientific FAIL
  `parent_statistic_no_achievable_range_at_registered_settings`, and
  `substrate_not_ready_requeue` stays for PR0/PR1/PR2 only. C1 and PR3 remain near-identical, so
  the diagnostic effectively asks one question: can S separate at the ESS ceiling?
- **(b) Sub-ceiling C1.** C1 ranges only over real cells with ESS <= 0.5 x n_att. It then asks
  whether S separates at a setting that is not the ceiling, and PR3 stays as the readiness control.
- **(c) Map as product.** C1 is demoted to reported-only. PR3 plus the per-cell separation map
  (crossover ESS) becomes the output, and the verdict rides on PR3.
- **(d) Shrink.** Given section 3, drop the sweep to the default cell + ceiling + negative control
  on 5 seeds, asking whether 884c's at-chance S replicates.

**Recommendation: (b) plus the section-3 question recorded as a pre-registered reported readout.**
(b) is the only option in which C1 asks something PR3 does not. The pilot predicts it passes,
which is informative, because it corrects the ESS-ceiling premise. Each option is a one- or
two-line edit to the parked driver, followed by a fresh red-team pass, since the change touches the
criterion.
