# SD-008 reset-init build: z_world EMA initialised from the first observation at episode reset (default OFF) -- and the zero-init transient is ~8 ticks, not 1, which corrects U4 sec 4

- **Status: BUILT on ree-v3 `main` at `298cb8ffd3`, default OFF, OFF bit-identical. 8/8 new contracts pass (all 8 fail on the pre-build substrate). Flag registered PROBED.** Session `bt0926-emainit` (`orchestrate-20260924-breakthrough-c2`), chip_ref `chip-20260926-zworld-ema-reset-init-fix`. Written 2026-09-26.
- **Defect closed:** U4, `zworld_near_collapse_rootcause_20260926.md` (1294f6edf5c): `LatentStack.init_state()` zeroes z_world at reset (`ree_core/latent/stack.py:1278`, base `e72e963`), SD-007 reafference is skipped at t=0 (`:1528`), so the EMA blend (`:1675`) degenerates on the first tick after every reset to `z(t0) = alpha_world * raw(t0)`.
- **Default-ON is a user decision; experiments that compare first-tick behaviour across the fix are confounded.**
- **Evidence domain: D0 + D1.** The fix is an algebraic change verified by contract; the PR/enrichment effects below are measured (D1). No consumer (E1/E2/E3) intervention here -- D2 not reached.

## 1. Premises re-measured

| # | premise | re-measured | verdict |
|---|---|---|---|
| P1 | reset identity &#124;&#124;z(t0)&#124;&#124; = alpha * &#124;&#124;raw(t0)&#124;&#124; (U4 sec 3) | Re-ran the U4 probe unchanged (native policy, 5 seeds 106-110, 8 ep x 40 ticks, alpha 0.3, deployed dims 32/32) on the base commit with the knob OFF: n=875 ticks, p1 0.1346, median 0.4519, collapse bucket 9/9 reset, enrichment 21.88x -- identical to U4's table. | holds, reproduced exactly |
| P2 | "reafference correction is skipped at t=0" | `stack.py:1528` `(prev_state.timestamp or 0) > 0`; the fix keys on the same predicate (`== 0`), so on the reset tick the post-SD-007 z_world IS `z_world_raw` and `z(t0) = raw(t0)` needs no change to the SD-007 skip. | holds; SD-007 skip left untouched |
| P3 | U4 sec 4: low PR at alpha 0.3 is "MOSTLY a separate general-smoothing effect" because excluding the t=0 ticks did not close the PR gap | **Stale / incorrect.** With a near-constant untrained raw encode, the zero-init transient is &#124;&#124;z(t)&#124;&#124; / &#124;&#124;raw(t)&#124;&#124; = 1 - (1-alpha)^(t+1): measured mean ratio by tick (U4 probe rerun, OFF, alpha 0.3) t0 0.300, t1 0.509, t2 0.658, t3 0.760, t4 0.831, t5 0.882, t6 0.917, t7 0.942 (theory: 0.300 0.510 0.657 0.760 0.832 0.882 0.918 0.942). The artefact spans ~8 ticks, not one; U4 excluded only t=0. See sec 3. | **corrected** -- the reset-init mechanism is the MAJORITY of the alpha-0.3 PR gap in a matched comparison |

## 2. What was built (ree-v3 `298cb8ffd3`)

- `ree_core/utils/config.py`: `LatentStackConfig.use_zworld_ema_reset_init: bool = False` (field, next to `alpha_world`/`alpha_self`); `REEConfig.from_dims(..., use_zworld_ema_reset_init=False)` named param; assignment `config.latent.use_zworld_ema_reset_init = bool(...)` in the SD-008 block. (The three config sites; from_dims silently drops unknown kwargs, so all three are needed.)
- `ree_core/latent/stack.py` `encode()`: `zworld_reset_init = flag and (prev_state.timestamp or 0) == 0`. Legacy branch: `elif zworld_reset_init: pass` (z_world(t0) = the instantaneous post-SD-007 encode) before the unchanged legacy `else:` blend. MECH-157 mode-routing branch: `alpha_eff = 1.0` on the reset tick (the E2 anchor pull, if any, still applies after it). No RNG touched; no other stream touched.
- `tests/test_flag_inertness.py`: `use_zworld_ema_reset_init` added to PROBED; `test_flag_registry_is_current` passes.
- `tests/contracts/test_zworld_ema_reset_init.py` (8 contracts): C0 default OFF + from_dims lands the knob; C1 OFF digest (sha256 of z_world/z_self/z_beta/z_theta/z_delta over 24 ticks with 3 resets) == default-config digest at alpha 0.3 and 0.9, and OFF keeps the legacy 0.3 reset ratio; C2 ON -> `||z(t0)|| == ||z_world_raw(t0)||` within 1e-6 (and elementwise) at every one of 5 agent resets, alpha 0.3 and 0.9; C3 ON t>=1 equals `alpha*raw(t) + (1-alpha)*z(t-1)` within 1e-6, ON == OFF bit-exact from a non-reset prev_state, ON covers the MECH-157 branch (`alpha_eff == 1.0`); C4 reduced U4 readout (sense-only, scripted actions from a local generator, seed 106, 10 ep x 30 ticks, alpha 0.3): OFF enrichment >= 3x (readout sensitivity) and ON < 3x.
- **Test half:** on the pre-build tree (`e72e963`, test file only) 0/8 pass. C0/C1/C3 fail because the knob does not exist (AttributeError/TypeError -- a reachability failure, not a behavioural one); C2 fails on the norm assertion; C4 fails on the substantive readout (ON enrichment 17.60x, the flag silently swallowed by from_dims). Post-build 8/8 (direct calls, Mac, `.scratch/breakthrough-20260924/emainit/run_contracts.py`).
- **OFF pre/post bit-identity (native policy, actions included):** `probes/emainit/off_digest.py` (committed alongside) -- default config, `act_with_split_obs`, alpha 0.3 and 0.9, 3 episodes each, 51 ticks, sha256 over z_world/z_self/action bytes: pre-build `733e14e9...cd60` == post-build `733e14e9...cd60` (same machine).

## 3. Results: what ON changes (D1)

**U4 readout, native policy, U4 probe rerun (5 seeds, alpha 0.3, deployed dims):**

| knob | n ticks | p1 &#124;&#124;z&#124;&#124; | median &#124;&#124;z&#124;&#124; | 0-1st pctile bucket | reset enrichment | reset-tick &#124;&#124;z&#124;&#124;/&#124;&#124;raw&#124;&#124; |
|---|---|---|---|---|---|---|
| OFF | 875 | 0.1346 | 0.4519 | 9 reset | 21.88x | 0.30000 |
| ON | 956 | 0.4323 | 0.4845 | 1 reset, 2 hazard, 7 wallpush | 2.39x | 1.00000 |

(Native-policy trajectories diverge once z_world changes, so n differs; the matched comparison is below.)

**Matched comparison -- identical env trajectories (scripted actions from `np.random.default_rng(seed)`, sense-only), seeds 106-110, 8 ep x 40 ticks, n=614 per arm** (`probes/emainit/matched_pr.py` (committed alongside)):

| arm | per-seed PR of z_world (106..110) | reset enrichment in 0-1st pctile |
|---|---|---|
| OFF alpha 0.3 | 1.35 1.36 1.15 1.40 1.25 | 15.35x (7/7 bucket ticks are t=0) |
| **ON alpha 0.3** | **3.97 4.06 3.49 4.32 3.31** | 0.00x (bucket ticks at t=2..8) |
| OFF alpha 0.9 | 5.94 6.44 5.29 7.15 5.32 | 15.35x |
| ON alpha 0.9 | 5.70 6.04 4.96 6.83 4.87 | 0.00x |

- At the deployed alpha 0.3 the fix alone lifts per-seed PR ~3x (mean 1.30 -> 3.83), closing ~53% of the gap to alpha 0.9 OFF (mean 6.03). The remaining gap (3.83 vs 5.68 ON / 6.03 OFF at alpha 0.9) is the general low-alpha smoothing SD-008 already names. **This reverses U4 sec 4's weighting** ("MOSTLY a separate general-smoothing effect"): the ~1-D untrained z_world at alpha 0.3 is mostly the zero-init norm ramp (a single direction -- the mean raw direction -- scaled 0.30 -> 0.94 over the first 8 ticks of every episode) dominating the covariance.
- Even at alpha 0.9 the reset tick is the collapse bucket (OFF 15.35x): the 0.9 shrink still puts t=0 in the lowest percentile of a tight norm distribution. SD-008's `alpha_world >= 0.9` does not by itself remove the reset spike; this knob does, at either alpha.
- **Adjacent corroboration (D0, not measured here):** W3/U3's step-1 rollout-norm spike (`w3_step1_spike_attribution_20260925.md`, d5f3bdc2fd: max g1 1.71-1.74 predicted, 1.73-1.77 true, concentrated at the smallest-||z0|| states) matches the zero-init ramp's t0 -> t1 ratio `(1-(1-alpha)^2)/alpha = 0.51/0.30 = 1.70` at the implicit alpha 0.3 those probes ran (`probes/rollout/rollout_fidelity_probe.py` build_B passes no alpha_world). If so, the gate-(c) step-1 growth-leg FAIL is the same reset artefact, correctly predicted by E2. Not re-run with the knob ON -- that is the cheap next check.

## 4. Sibling EMAs with the same zero-init pattern (reported, NOT fixed)

- **z_self**: identical mechanism -- `z_self = alpha_self*z_self + (1-alpha_self)*prev_state.z_self` (`stack.py` legacy branch, alpha_self default 0.3) against init_state's zero z_self. Not covered: the knob is z_world-scoped by name and brief, and z_self has its own SELF-1 recurrence path (`use_self_recurrence`) whose GRU also reads a zero prev at reset. A sibling knob would be the same 3-line change.
- **z_beta / z_theta / z_delta**: identical mechanism at the hard-coded `alpha_shared = 0.3`. Not covered.
- **z_harm (SD-036 `gaba_harm_state_recurrence`, default OFF)**: `_gaba_state_blend` fails open when prev is None (z_harm_a at reset), but init_state gives z_harm `zeros(harm_dim)` when harm_dim > 0, so the MECH-099 z_harm blends against zeros at reset when shapes match. Only live when that flag is ON. Not covered.

## 5. Not done / open

- Default-ON (and whether to extend to z_self / shared latents) is a user decision -- flagged, not decided.
- No D2 check (does E1/E2/E3 consume the reset tick differently with ON). The W3 step-1 re-check with ON is the cheapest D2-adjacent follow-on.
- Pre-commit contract gate ran the full suite remotely (Mac lock busy > 30 min, held by bt0926-w3rel): 5812 passed, 54 skipped, 1 xfailed, 0 failed (run_id DLAPTOP-4-2869-20260926T033926Z-205618554). The only commit between base e72e963 and 298cb8ffd3 is the validation-cache commit e63f809eae, which touches none of this build's files.

