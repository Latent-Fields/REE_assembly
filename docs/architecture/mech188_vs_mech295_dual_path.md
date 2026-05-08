# MECH-188 vs MECH-295 dual-path z_goal: read-site disambiguation

**Created:** 2026-05-08
**Trigger:** EXQ-536b found `inject_observed_fraction=1.0` AND `approach_commit_rate=0.0`
co-existing across 3 seeds. Initial reading "downstream commit chain inert even with active
z_goal" was partially correct but conflated two separate read sites.

## The two paths

There are two write sites for z_goal-derived signals in `select_action()`, with
different read sites and different gating predicates.

| Path | Writer | Stored on | Read by | Gate predicate |
|---|---|---|---|---|
| **MECH-188 inject** (action-time) | `agent.select_action()` line ~2316–2321 | `_goal_state_for_select` (a `GoalState.with_injection()` wrapper, **distinct object** from `self.goal_state`) | `e3.select()` per-candidate scoring via `cand_world_summaries` proximity | `cfg.goal.z_goal_inject > 0.0` |
| **MECH-295 weak bridge** (commit-driving) | `agent._e3_tick()` line ~3608 (`compute_anticipatory_liking_write`) **and** `select_action()` line ~2594–2642 (`compute_approach_cue_score_bias`) | reads `self.goal_state` (the persistent attractor) | composes `m295_bias` into `dacc_score_bias` (the negative score_bias E3 uses to favour approach) | `self.goal_state.is_active()` AND `goal_norm >= mech295_min_z_goal_norm_to_fire (default 0.05)` |

`GoalState.with_injection()` (in `ree_core/goal.py`) creates a **lightweight wrapper** — a
new `GoalState` instance whose `_z_goal` has a norm floor, sharing config and device with
the original. It does not mutate `self.goal_state._z_goal`. The persistent attractor stays
exactly where `update_z_goal()` left it.

`GoalState.is_active()` is `self._z_goal.abs().sum() > 1e-6` — it checks **the persistent
attractor**, not the wrapper.

## Why EXQ-536b reads as "inert"

1. EXQ-536a established that `update_z_goal()` never seeds: the SD-012 drive multiplier
   collapses to ~1.0 at the moment of contact (energy=0.995 → drive=0.005), so
   `effective_benefit = 0.036 < benefit_threshold (0.1)`. Persistent attractor stays zero.
2. `self.goal_state._z_goal` stays at the zero vector for the whole run.
3. `self.goal_state.is_active()` returns `False` for the whole run.
4. The MECH-295 bridge (both write site at `_e3_tick` and read site at `select_action`) is
   gated by `is_active()`. **Both bridge call sites short-circuit.**
5. Meanwhile, `cfg.goal.z_goal_inject = 0.3` ARM_1 builds `_goal_state_for_select` via
   `with_injection(0.3)`. This wrapper has `_z_goal.norm() >= 0.3`. E3.select sees it in
   per-candidate proximity calc → `inject_observed_fraction = 1.0`.
6. But the m295 bias is `0.0` (bridge skipped), so `dacc_score_bias` carries no
   approach pressure. `approach_commit_rate = 0.0`.

The "inert downstream chain" reading was therefore wrong-by-conflation. The chain is not
broken; it is **bypassed**. The bypass is intentional from MECH-188's design intent (the
docstring says "applies to action selection only, does NOT modify the persistent attractor")
but unintentional as a force-arm test of MECH-295.

## What this means for the diagnostic queue

EXQ-536b cannot falsify the MECH-295 weak-bridge reading. It tested the wrong path. Three
follow-ons would discriminate cleanly:

- **EXQ-536c (MECH-295 direct force-arm):** seed `self.goal_state._z_goal` directly to
  norm 0.3 at episode start, bypassing `update_z_goal()`. If `approach_commit_rate` lifts,
  the bridge is intact and the upstream seeding (SD-012 drive-vs-benefit) is the sole
  blocker. If it stays at 0, MECH-295 is also broken.
- **EXQ-536d (lower min_z_goal_norm_to_fire):** drop
  `mech295_min_z_goal_norm_to_fire` from default 0.05 to 0.01. Tests whether the bridge's
  internal threshold is too high for naturalistic z_goal seeding when contacts are sparse.
- **EXQ-536e (combined):** both at once. Cleanest single-shot test.

A fourth option is structural: extend `with_injection()` to **also write the floor into
the persistent attractor**, or have `MECH-188` set both `_goal_state_for_select` and
`self.goal_state._z_goal`. This would make the MECH-188 inject a true upstream
force-arm. Worth considering as a small SD amendment if EXQ-536c/d/e show MECH-295 is
intact.

## Implication for the EXQ-483 catatonic-lock diagnosis

The MECH295LikingBridge constructor docstring at agent.py:628-637 cites EXQ-483 as the
empirical anchor for "drive amplification produces a passive z_goal latent without
behavioural consequence." That diagnosis is unchanged — but the EXQ-483 cohort scripts
also did not seed the persistent attractor in some arms (they relied on the same
benefit-threshold path that EXQ-536a just falsified for sparse contact regimes). Whether
EXQ-483's "approach_commit = 0.0 across all arms" was due to bridge inertness or due to
upstream seeding failure is **not yet disambiguated** by the existing evidence. The
EXQ-536c/d/e cohort would clear this up retroactively.

## Companion claim updates needed

When EXQ-536c/d/e land, add a note to MECH-295's `evidence_quality_note` clarifying that
EXQ-536b is **non_contributory for MECH-295 directly** (it tested MECH-188 path only).
Currently the manifest is correctly tagged `non_contributory` for diagnostic purposes,
but the implication for MECH-295 should be made explicit so the V3-pending note for
MECH-295 doesn't silently absorb 536b as "weakens."

## See also

- `agent.py:2316–2321` — MECH-188 inject site
- `agent.py:2587–2642` — MECH-295 bridge select-time score_bias
- `agent.py:3596–3629` — MECH-295 bridge tick-time anticipatory liking write
- `goal.py:176–214` — `with_injection()` wrapper construction
- `goal.py:215–217` — `is_active()` (reads persistent attractor only)
- `regulators/mech295_liking_bridge.py` — bridge internal gating
- EXQ-536a manifest — H_b benefit-threshold-never-crossed
- EXQ-536b manifest — inject force-arm null
