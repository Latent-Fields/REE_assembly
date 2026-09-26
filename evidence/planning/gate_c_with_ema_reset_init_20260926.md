[chip_ref: chip-20260926-gate-c-with-ema-reset-init]

# Gate (c) with z_world EMA reset-init: MOSTLY ARTEFACT-EXPLAINED (84% of the excess closed), quantified RESIDUAL matches the already-characterized non-reset ratio floor (bt0926-gatec3)

- **Status: MEASURED, 5/5 seeds x 4 pools (20 cells). Verdict: MOSTLY ARTEFACT-EXPLAINED, with a small quantified RESIDUAL that this record's own second route shows is NOT new.** Session `bt0926-gatec3` (`orchestrate-20260924-breakthrough-c2`), chip_ref `chip-20260926-gate-c-with-ema-reset-init`. Written 2026-09-26.
- **Question being closed:** `zworld_ema_reset_init_build_20260926.md` (3969d212ba) sec 3's own named cheap next check: "the gate-(c) step-1 growth-leg FAIL is the same reset artefact, correctly predicted by E2 ... not re-run with the knob ON."
- **Code:** `ree-v3` tag `archive/coupled-loop-repair-042895a` (`042895a3a2be3a54e5a74199e8e3950cc058cb31`, the SAME base `gate_c_pool_controls_20260925.md` used) in a detached throwaway worktree `/Users/dgolden/REE_Working/.scratch/wt-gatec3/ree-v3-wt`, with `main`'s `298cb8ffd3` (the SD-008 reset-init build) cherry-picked on top. **The cherry-pick applied CLEANLY, no conflicts** (`git cherry-pick 298cb8ffd3` -> `4e7328b9c9`, 4 files changed, 260 insertions, 0 deletions -- `ree_core/latent/stack.py`, `ree_core/utils/config.py`, `tests/contracts/test_zworld_ema_reset_init.py`, `tests/test_flag_inertness.py`). Worktree removed at the end (`git worktree remove --force` + `git worktree prune`). No `ree_core` edits beyond the cherry-pick. No queue, no chips beyond the one closed here, no `claims.yaml` edits.
- **Evidence domain: D1.** The quantity (per-candidate `||z_world||` growth from `E2.world_forward`/`rollout_with_world`, decoded from the trained W3 head) exists, moves, and is read directly; no consumer-mediated (E3) intervention performed here.

## 1. Premises re-measured

| # | premise | re-measured | verdict |
|---|---|---|---|
| P1 | brief: "must reproduce aspc2 within noise -- canary" (knob OFF) | Ran the full `gate_c_pool_controls_probe.py` pipeline byte-for-byte (same training recipe, same RNG seeding, same held-out-state protocol) inside THIS worktree with `use_zworld_ema_reset_init=False`, all 5 seeds x 4 pools (20 cells). Compared `pooled_max_max_growth_all` and `pooled_ratio_median` against the committed `gatec2_s{106..110}.json` (fc8340fb87). | **Exceeded the ask: BIT-EXACT match (abs diff < 1e-6) on all 20/20 cells**, not merely "within noise" -- confirms the cherry-picked worktree, the RNG streams, and this script's refactor introduce zero behavioural change with the knob OFF. |
| P2 | "the fix is z_world-scoped and touches only the reset tick's blend" (build record sec 2) | Re-read the cherry-picked diff directly (`git show 4e7328b9c9 -- ree_core/latent/stack.py`): `zworld_reset_init = bool(getattr(self.config, "use_zworld_ema_reset_init", False)) and (prev_state.timestamp or 0) == 0` (stack.py ~1555, right after the `alpha_world`/`alpha_shared` reads) and `if zworld_reset_init: alpha_eff = 1.0` inside the MECH-157 mode-routing blend (~1635), immediately before `z_world = alpha_eff * z_world + (1 - alpha_eff) * prev_state.z_world`. | **holds** -- exactly the diff the build record describes, nothing else touched. |
| P3 (new, this probe's own instrument) | whether `BB.gen_policy`'s per-segment tick index `ti` (used to label held-out states) equals "ticks since that episode's own reset" | Re-read `babble_probe.py:gen_policy` (154-166, unchanged in this campaign): each segment's `obs` list is seeded with `snap_obs(od)` from the `env.reset()` that starts it (or from a mid-episode re-`reset()` on early termination), and the held-out-state loop calls `ref.reset()` immediately before replaying a segment's own `obs` list in order -- so `ti=0` is always the FIRST `ref.sense()` call after `ref.reset()` (`prev_state.timestamp==0`), i.e. exactly the reset-init knob's trigger tick. `t_pick` (the state actually kept) is therefore ticks-since-reset directly, with no separate derivation needed. | **holds** -- confirmed by code read, not assumed; this is what licenses sec 3's "fraction within 8 ticks" and the restricted-subset reading below. |

## 2. Method

- **Pipeline: run TWICE per seed, in one process, sharing nothing but the RNG-seeding calls** (`R.seed_all(S)` at the top of each arm) -- once `use_zworld_ema_reset_init=False` (the P1 canary), once `=True` (the test). The knob is set on BOTH the training agent's config (`agent.latent_stack.config.use_zworld_ema_reset_init`, immediately after `BB.fresh_agent` constructs it, before babbling starts) and `ref`'s config (immediately after `R.build_B`, before held-out-state generation) -- so the fix is live for the WHOLE pipeline (world-head + codec training AND readout), not spliced in only at readout as a spot check. Setting the flag is a pure attribute write (no RNG consumed), so it does not perturb the OFF arm's bit-identity to aspc2.
- **Everything else byte-identical to `gate_c_pool_controls_probe.py` (aspc2):** `E2WorldMember` (babble pre-phase 12 eps -> 3000 updates, then 1200 on-policy post-phase steps at 8 updates/step) + `CodecMember` (1000 manual updates after babbling) on the same `WakingTrainer`; held-out states via `BB.gen_policy(S, 20, 300, BB.pol_uniform(S*11+17))`, `t_pick` from `default_rng(S*97+5)`; same 4 pools (`native_default`, `native_codec_w1_on`, `control_random_per_step`, `control_constant_per_class`); same `growth_stats`/`pool_and_gate`, same [0.5,2]/1.05 bound, same late-window(21-30)/first-D alternative readings. Seeds 106-110.
- **New instrumentation, added without any extra rollout or RNG draw:** (a) `t_pick` (== ticks-since-reset, P3) recorded per held-out state; (b) each per-candidate growth-stat dict tagged with its source `state_idx`, so a SUBSET of already-computed candidates can be re-pooled after the fact with no extra compute; (c) using (b), for the OFF arm only, the SAME 4-pool `pool_and_gate` computation re-run restricted to states with `t_pick >= 8` (the build record's own measured ~8-tick transient window) -- a second, orthogonal route to the same question that needs no fix at all: if excluding early-tick states alone closes most of the gap, that independently implicates the reset transient.
- Script: `probes/gatec3/gate_c_ema_reset_init_probe.py` (committed alongside this record). Raw per-seed JSON (both arms): `probes/gatec3/gatec3_s{106,107,108,109,110}.json`.
- **MAC CPU LOCK discipline followed throughout**: one seed's full run (OFF+ON, ~90-480s wall) per lock hold, `rmdir` released immediately after each, 45s pause, re-poll. Per-seed wall time 122s-472s (both arms); total probe wall time ~28 min across 5 lock holds.

## 3. Results

**Literal reading (pooled max growth over all 30 steps), 5 seeds x 4 pools, OFF vs ON:**

| seed | pool | OFF max_growth | ON max_growth | OFF ratio_med | ON ratio_med |
|---|---|---|---|---|---|
| 106 | native_default | 1.7162 | 1.1571 | 1.5830 | 1.9641 |
| 106 | native_codec_w1_on | 1.7238 | 1.1372 | 1.4466 | 1.1896 |
| 106 | control_random_per_step | 1.7254 | 1.1445 | 1.5150 | 1.1809 |
| 106 | control_constant_per_class | 1.7254 | 1.1620 | 1.9480 | 1.4009 |
| 107 | native_default | 1.7566 | 1.1897 | 4.7189 | 4.4252 |
| 107 | native_codec_w1_on | 1.7940 | 1.2137 | 2.8831 | 5.7372 |
| 107 | control_random_per_step | 1.7942 | 1.2091 | 2.0275 | 3.2061 |
| 107 | control_constant_per_class | 1.7942 | 1.2052 | 4.3894 | 5.8799 |
| 108 | native_default | 1.7327 | 1.1608 | 1.9827 | 2.8338 |
| 108 | native_codec_w1_on | 1.7372 | 1.1699 | 1.6707 | 2.5326 |
| 108 | control_random_per_step | 1.7372 | 1.1662 | 1.7488 | 2.1419 |
| 108 | control_constant_per_class | 1.7372 | 1.1734 | 2.7729 | 2.4291 |
| 109 | native_default | 1.7098 | **1.0915** | 1.5626 | 1.1511 |
| 109 | native_codec_w1_on | 1.7243 | 1.1006 | 1.5058 | 1.0830 |
| 109 | control_random_per_step | 1.7243 | **1.0820** | 1.4780 | 1.1142 |
| 109 | control_constant_per_class | 1.7243 | 1.1220 | 1.7070 | 1.3111 |
| 110 | native_default | 1.6964 | 1.1750 | 2.6867 | 8.3843 |
| 110 | native_codec_w1_on | 1.7384 | 1.1609 | 1.1518 | 1.1501 |
| 110 | control_random_per_step | 1.7384 | 1.1571 | 1.1097 | 1.1317 |
| 110 | control_constant_per_class | 1.7384 | 1.1710 | 1.2495 | 1.2958 |

**Every OFF cell matches `gate_c_pool_controls_20260925.md`'s stored `gatec2_s{106..110}.json` exactly** (abs diff < 1e-6, both `pooled_max_max_growth_all` and `pooled_ratio_median`, all 20 cells) -- P1's canary, confirmed at the strongest level (bit-exact, not "within noise"). **`gate_c_pass_literal` is FALSE in all 20 OFF cells and all 20 ON cells** -- the fix does not make gate (c)'s literal reading PASS anywhere. Ratio-leg medians drift under ON (expected: the fix changes early trajectories, so this is a KNOWN confound the build record already names -- "experiments that compare first-tick behaviour across the fix are confounded" -- and the ratio leg was never the gate-deciding leg in any prior record in this line).

**Aggregate, across all 20 cells:**

| | min | max | mean | mean excess over 1.05 bound |
|---|---|---|---|---|
| OFF max_growth | 1.6964 | 1.7942 | 1.7384 | 0.6884 |
| ON max_growth | 1.0820 | 1.2137 | 1.1574 | 0.1074 |

**The knob closes 84.4% of the mean excess-over-bound** ((0.6884-0.1074)/0.6884). Cells failing the literal bound: OFF 20/20, ON 20/20 -- no cell flips to PASS, but the margin collapses from ~1.62-1.79x the 1.0 baseline (or 61-71% over the 1.05 bound) to ~1.03-1.16x (3-16% over the bound).

**Late-window (steps 21-30) mean-growth reading:** unaffected by the finding either way -- OFF max 1.066-1.142, ON max 1.052-1.161, both comfortably under gate (e)'s own 1.2 bound in every cell, matching every prior record in this line (aspc/aspc2/u3).

**Fraction of held-out states within 8 ticks of a reset (P3, tick-index == ticks-since-reset):** 38.6%-49.2% across seeds (mean 42.9%) -- large, not a rare edge case, because segments frequently terminate early (hazard hits) well before `EP_STEPS=200`, so a `t_pick` drawn uniformly over a SHORT segment lands in the first 8 ticks disproportionately often. This fraction is identical between the OFF and ON arms (t_pick is drawn from the held-out-state RNG stream, independent of the knob).

**Second route -- OFF arm, `native_default` pool, restricted to states with `t_pick >= 8` (no fix, just excluding early-tick states):**

| seed | n kept / total | restricted max_growth (OFF, no fix) |
|---|---|---|
| 106 | 102/166 | 1.1495 |
| 107 | 102/173 | 1.1529 |
| 108 | 93/183 | 1.1424 |
| 109 | 106/177 | 1.0999 |
| 110 | 97/179 | 1.1199 |

Mean 1.1329, range 1.0999-1.1529 -- **this lands in the SAME range as the ON arm's full-state-set max_growth (mean 1.1574, range 1.0820-1.2137)**, via a completely independent mechanism (excluding early ticks vs. correcting the encode at early ticks). Two orthogonal routes to the same conclusion agree to within ~0.02-0.04 on the residual's magnitude.

## 4. Verdict: MOSTLY ARTEFACT-EXPLAINED; the residual is quantified and is NOT new

Per the brief's two options, this is not a clean binary -- the honest read uses the brief's own escape clause ("ON ... fails only by a margin you quantify"):

- **ARTEFACT-EXPLAINED, majority.** The reset-init fix closes 84.4% of the mean excess over the literal bound, across all 4 pools and all 5 seeds uniformly (no pool or seed is an outlier in either direction). This is a real, large, uniform effect -- not noise.
- **The remaining margin is small and precisely quantified**, not an open-ended "real growth remains": ON max_growth spans 1.082-1.214 (mean 1.157), i.e. the literal bound is exceeded by 3-16% (mean 10%), versus 61-79% (mean 66%) with the fix OFF.
- **The residual is NOT new, and is NOT reset-related.** The independent (t_pick>=8, knob OFF) restricted reading -- which involves no fix, only excluding reset-adjacent states -- lands in the SAME numeric range (1.100-1.153) as the ON arm's full-state reading (1.082-1.214). This matches `w3_step1_spike_attribution_20260925.md`'s (d5f3bdc2fd) own verdict on the (state, not action-class)-driven, largely-CORRECT-PREDICTION + RATIO-ARTEFACT growth spike that persists even on the environment's own TRUE dynamics, independent of E2 or of resets specifically -- that record's own U4 ("is the SD-008 EMA's occasional near-collapsed single-tick ||z_world|| itself worth investigating") is exactly the mechanism this fix targets for the RESET case, but u3 already showed the SAME ratio-floor phenomenon recurs at non-reset ticks too (small-||z0|| states can occur without a reset, just less densely). **So: the reset-init fix correctly and fully explains the RESET-attributable share of the growth-leg failure; the remainder is the pre-existing, already-characterized non-reset small-||z0|| ratio floor, not a new or separate defect.**

**This does not decide U1** (`asp_gate_c_readout_20260925.md`/`gate_c_pool_controls_20260925.md`/`w3_step1_spike_attribution_20260925.md`, unchanged, per the brief). It does sharpen U1's option-space: with the reset-init fix ON, the literal all-step-max/1.05 bound would need to move only ~3-16% (vs ~61-79% OFF) to accommodate the residual, a much smaller ask than before -- but whether to fix the bound, fix the residual ratio-floor, or accept the residual as within measurement noise of a re-calibrated bound remains the user's/orchestrator's call.

## 5. Decisions the user/orchestrator owns (none taken here)

| id | decision | options |
|---|---|---|
| U1 (inherited, unchanged) | Which growth-leg reading is authoritative for gate (c) | Unchanged from prior records; this record adds that WITH the reset-init fix ON, the literal bound's residual violation shrinks to 3-16% (mean 10%) instead of 61-79%, and that residual is the SAME magnitude as the already-characterized non-reset small-||z0|| floor (u3), not a new phenomenon. |
| U5 (new) | Default-ON for `use_zworld_ema_reset_init` (already flagged as a user decision in the build record) | This record adds evidence FOR: at deployed dims/alpha, ON uniformly reduces gate-(c) literal-reading violation by 84% with no case made worse, across every pool and seed tested. Still not decided here; z_self/shared-latent siblings remain unfixed (build record sec 4) and no D2/consumer-reach check has been done with ON (sec 6). |

## 6. Not done

- No D2 (consumer-mediated, E3-reach) check with the knob ON -- unchanged from every prior record in this line; out of scope per the brief.
- Did not extend the fix or this readout to `alpha_world >= 0.9` (SD-008's own recommended floor) -- all runs here use the deployed default `alpha_world=0.3`, matching aspc2/u3 exactly, per the brief's REUSE instruction.
- Did not investigate the residual small-||z0|| ratio floor itself (would need u3's own per-state/per-class attribution machinery re-run under the ON arm) -- flagged as a possible follow-on, not attempted here (brief scope was gate (c) re-readout only).
- Did not test the sibling EMAs (z_self, z_beta/theta/delta) that the build record's sec 4 reports share the same zero-init pattern but are NOT covered by this knob.
