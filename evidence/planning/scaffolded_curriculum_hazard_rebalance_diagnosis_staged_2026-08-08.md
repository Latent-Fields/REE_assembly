**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml, substrate_queue.json, or any registry. No substrate code was changed.**

# scaffolded_sd054_onboarding "hazard-rebalance" chip — diagnosis says the scoped fix is misdirected

- **Chip:** `chip-20260808-igw200-scaffolded-curriculum-hazard-rebalance` (IGW-20260808-200)
- **substrate_queue entry:** `scaffolded-curriculum-hazard-rebalance` (`status: pending_implementation`, unblocks Q-021, INV-034, ARC-030)
- **Session:** metaworker-chip-20260808-igw200-scaffolded-curriculum-hazard-rebalance
- **Date:** 2026-08-08T09:45Z
- **Decision chip raised:** `chip-20260808-scaffolded-c6-misdiagnosis-routing` (kind=decision)

## TL;DR

The chip asks: *"Rebalance scaffolded_sd054_onboarding hazard-stage exposure so z_goal survives to the P2 measurement window"* — on the premise (from `substrate_queue.json`) that the *"intervening hazard-only stages appear to starve goal maintenance … z_goal peaks ~0.5 at Stage-0, decays to 0.12 by P2."*

**That premise is empirically false.** An instrumented probe of the real curriculum shows z_goal is **fully preserved through every hazard stage** and **enters the P2 window at ~0.52**. The decay to 0.12 happens **inside the V3-EXQ-866a experiment driver's own P2 measurement loop**, which calls `update_z_goal` unconditionally on every step (a decay-only washout on a near-zero-contact env), **bypassing the scheduler's own contact-gated `run_p2`** that already protects z_goal and reports its *peak*.

**Conclusion:** no substrate change to hazard-stage dosage/ordering can fix C6, because the hazard stages never touch z_goal. The C6 fix is a **`/queue-experiment` re-run** (866c) that measures z_goal through `ScaffoldedSD054OnboardingScheduler.run_p2` (or contact-gates its measurement), not an `/implement-substrate` substrate change. I therefore did **not** build the scoped hazard-stage change — building it would ship a fix that cannot move the metric it targets.

Separately, the 866a run's **actual primary FAIL is G0**, not C6 (see §4): the FULL arm forages *below* the RANDOM baseline (resource_visit_rate 0.0033 vs 0.0103). That is the long-running GAP-2 / Stage-H foraging-competence ceiling, is not what this chip scoped, and is unlikely to be closed by a hazard-stage tweak.

## 1. What 866a measured and why it FAILed

`v3_exq_866a_inv034_q021_goal_maintenance_agency_onboarded_20260803T075813Z_v3.json` (FAIL, non_contributory):

- `degeneracy_reason`: **"G0 non-degeneracy gate failed … FULL arm did not clear random-baseline resource-visit rate by the pre-registered margin on >= 2/3 seeds."**
- `g0_pass = 0`, `c6_pass = 0`. (c1/c2/c3 pass, c4/c5 fail.)
- `zgoal_norm_mean_FULL = 0.1198` (C6 needs `> 0.4`).
- per-seed FULL: `stage0_z_goal_norm_peak` 0.499 / 0.429 / 0.370 (healthy), `stage0b_retention_ratio` ~0.94, but `zgoal_norm_mean` 0.121 / 0.091 / 0.147, and **`hazard_survival_gate_passed = False` on all 3 seeds** (Stage-H median episode length 5.5 / 4.0 / 5.0 vs gate 75), while P1 survival passes.

## 2. The mechanism (code trace)

- **Frozen stages never decay z_goal.** `run_stage0b_consolidation`, `run_p0`, `run_hazard_avoidance` call `_set_goal_pipeline_frozen(frozen=True)` and **do not call `update_z_goal` at all**. Freezing silences the MECH-295/307 *write* pathway; it is orthogonal to the persistent-attractor decay. No `update_z_goal` call ⇒ no `_z_goal *= (1 - decay_goal)` ⇒ z_goal is held flat. (`scaffold_sd054_onboarding.py:1823` `_set_goal_pipeline_frozen`.)
- **`GoalState.update` decays every call** (`ree_core/goal.py:85`, `decay_goal = 0.005`): `self._z_goal = self._z_goal * (1 - decay_goal)` before the benefit-gated pull. So every *unfed* `update_z_goal` step erodes z_goal by 0.5%.
- **The scheduler's own `run_p2` contact-gates the measurement** (`scaffolded_sd054_onboarding.py:2756`): with `scaffold_developmental_window_enabled` + `scaffold_contact_gated_goal_updates` (both set in 866a's config), `_eval_episode` **skips `update_z_goal` on unfed steps** (`n_skipped_protected`), so `n_decay_only = 0`, and it reports **`z_goal_norm_peak_max` / `z_goal_norm_at_contact_peak`** (peaks, captured by a pre-update read), not a decaying mean.
- **The 866a driver does NOT use `run_p2`.** It rolls its own `_measure_866_style` (`v3_exq_866a…py:429`) which, at lines 497–500, calls `update_z_goal(benefit, drive)` **every step unconditionally** and then averages `||z_goal||` over all measurement steps. On the P2 env with `resource_visit_rate ≈ 0.003`, ~all steps are unfed ⇒ pure decay-only washout, averaged into `zgoal_norm_mean`.

**Quantitative check.** `0.995^200 ≈ 0.37` retention per 200-step episode; z_goal persists across episodes (`REEAgent.reset()` does not reset `goal_state`), so after ~2–3 P2 episodes it is near zero and the 30-episode mean lands at ~0.12 — exactly the observed value.

## 3. Empirical probe (real curriculum, reduced budget, seed 42)

`scratchpad/probe_zgoal_decay.py` runs the real `ScaffoldedSD054OnboardingScheduler` (866a's exact config, budgets Stage0=4/Stage0b=2/P0=8/H=6/P1=6/P2=6, 40 steps/ep) and snapshots `||z_goal||` after each stage, then measures P2 two ways from the *same* post-P1 state:

```
after Stage-0   (peak=0.4829)              ||z_goal|| = 0.4737
after Stage-0b  (retention=0.981)          ||z_goal|| = 0.4737   <- consolidation preserves
after P0        (frozen)                   ||z_goal|| = 0.4737   <- hazard-adjacent, preserved
after Stage-H   (gate=False, median=8)     ||z_goal|| = 0.4737   <- HAZARD STAGE: z_goal FLAT
after P1        (contact-gated)            ||z_goal|| = 0.5261   <- ecological contact GROWS it
=== z_goal ENTERING P2 = 0.5154–0.5261 ===
(a) 866a-style unconditional-update P2:  zgoal_norm_MEAN = 0.437   (decays step-by-step)
    first-ep per-step ||z_goal||: 0.5235, 0.5225, …, 0.4805  (monotone decay)
(b) scheduler run_p2 (contact-gated):    peak_max = 0.5172, contact_peak = 0.5129,
                                         n_decay_only = 0, n_skipped_protected = 164
```

The two P2 rows are the whole story: **same agent, same z_goal entering P2 (~0.52); the 866a-style measurement decays it, `run_p2` does not.** The reduced-budget mean (0.44) vs the full-budget mean (0.12) differ only by episode length (40 vs 200 steps) — the mechanism (per-step decay-only) is identical and seed-independent.

## 4. The real primary blocker is G0 (foraging competence), not C6

866a FAILs at **G0 first** (FULL forages *below* RANDOM). Even a perfect C6 fix leaves G0 failing, so the experiment would still FAIL. G0 is the GAP-2 / Stage-H foraging-competence ceiling this lineage has fought since ~2026-06 (Stage-H survival gate has failed across 603g/603i/…; here it fails again, median 4–5.5/200). "Rebalancing hazard-stage exposure" is the substrate_queue's instinct for *this* leg, but:
- it is a **foraging/survival** problem, not a **z_goal-maintenance** problem (the chip's stated metric);
- it is the SAME ceiling that survived months of dedicated Stage-H work (harm-pathway training, cue-authority, etc.), so a dosage tweak is unlikely to be the fix and deserves its own diagnosis/autopsy, not a hasty rebalance under a mis-scoped chip.

## 5. Recommended routing (for user / governance review)

1. **C6 / z_goal maintenance — NO substrate change.** The substrate already achieves the stated goal (z_goal survives to P2 at ~0.52; `run_p2` reports peak 0.52 with `n_decay_only=0`). Fix the *measurement*: a **`/queue-experiment` 866c re-run** whose P2 z_goal readout uses `run_p2`'s `z_goal_norm_peak_max` / `z_goal_norm_at_contact_peak` (or contact-gates `_measure_866_style`). This is a driver change, not a scheduler change.
2. **G0 / foraging competence — the real substrate blocker.** Route to the GAP-2 / Stage-H foraging-competence thread (its own `/failure-autopsy` or `/implement-substrate` diagnosis). Do not fold it into the z_goal chip.
3. **substrate_queue entry `scaffolded-curriculum-hazard-rebalance`:** leave `pending_implementation` **or** re-title/re-scope to the G0 foraging leg. Its current title/premise (hazard-stage exposure starves z_goal) should be corrected — it conflates the measurement-harness C6 bug with the G0 foraging ceiling. (Not edited here: `substrate_queue.json` is under an active claim by another session as of this writing.)

## 6. What this session did and did not do

- **Did:** diagnosed the C6 failure to the 866a measurement harness (code trace + two-way empirical probe); confirmed the substrate preserves z_goal through the curriculum; identified G0 as the real primary FAIL.
- **Did NOT:** change `scaffolded_sd054_onboarding.py` or its contracts (no substrate change is warranted for the stated z_goal goal); did NOT flip the substrate_queue status; did NOT queue the 866c re-run (that is a separate `/queue-experiment` session) or touch claims.yaml.
