# SD-008 sibling reset-init build: z_self, shared-latent (z_beta/z_theta/z_delta) and SD-036 z_harm EMAs initialised from the first encode at episode reset (default OFF)

- **Status: BUILT on ree-v3 `main` at `bdfe901b37`, default OFF, OFF bit-identical. 8 new contracts pass; 7/8 fail on the pre-build substrate (the 8th pins the legacy defect and passes on both trees by design). Three flags registered PROBED.** Session `bt0926-emasib` (`orchestrate-20260924-breakthrough-c2`), chip_ref `chip-20260926-sibling-ema-reset-init-build`. Written 2026-09-26.
- **Parent:** `zworld_ema_reset_init_build_20260926.md` (3969d212ba; ree-v3 `298cb8ffd3`, `use_zworld_ema_reset_init`), sec 4 "Sibling EMAs with the same zero-init pattern (reported, NOT fixed)". GFLAG-0559 (SD-008/SD-106, open) covers the defect class; `governance_flag.py` has no note verb (raise / resolve / list only), so no pointer was appended and no second flag raised -- no new registry row is affected (same SD-008 row).
- **Default-ON is a user decision.** Experiments that compare first-tick behaviour of z_self / z_beta / z_theta / z_delta / z_harm across these knobs are confounded.
- **Evidence domain: D0 + D1.** The fix is algebraic and pinned by contract; the PR numbers below are measured on an untrained agent (D1). No consumer intervention -- D2 not reached.

## 1. Premises re-measured (base `298cb8ffd3`)

| # | premise (from the parent record sec 4) | re-measured | verdict |
|---|---|---|---|
| P1 | z_self: `z_self = alpha_self*z_self + (1-alpha_self)*prev.z_self` against init_state's zero z_self | `stack.py` legacy branch (base :1602); `init_state` zeroes z_self (base :1269-1292). Contract C1b: OFF `z_self(t0) == 0.3 * raw_z_self(t0)` elementwise, raw read by forward hook on `split_encoder` (independent of the EMA arithmetic). | holds |
| P2 | z_beta/z_theta/z_delta: same, hard-coded `alpha_shared = 0.3` | base :1551 / :1697-1699. C1b: each OFF reset tick == 0.3 * hooked raw (last `beta_encoder`/`theta_encoder` call, `delta_encoder`). | holds |
| P3 | SD-036 z_harm blends against init_state's zeros "when shapes match", only when the flag is on | `_gaba_state_blend` (base :1295) fails open on `z_prev is None` or a shape mismatch. `init_state` gives `z_harm = zeros(harm_dim)` only when `harm_dim > 0` (the MECH-099 lateral head dim); the SD-010 `harm_encoder` output is `z_harm_dim`. So the zero prior is live iff `gaba_harm_state_recurrence` AND `harm_dim > 0` AND `harm_dim == z_harm_dim` (or no SD-010 override). With `harm_dim = 0` (the default) the blend already fails open at reset and there is no defect. z_harm_a's reset prev is `None` (LatentState default) -> already raw at reset. C1b: with harm_dim = z_harm_dim = 32, OFF `z_harm(t0) == 0.5 * raw`. | holds, **narrower than "whenever the flag is on"**: conditional on harm_dim > 0 with matching dims |

## 2. What was built (ree-v3 `bdfe901b37`)

**Choice: three independent per-family knobs** (not an umbrella + sub-knobs). Simplest shape that keeps OFF bit-identical and lets each family be turned on alone; an umbrella would add a fourth flag with no extra reach. `use_zworld_ema_reset_init` is unchanged and stays a separate switch (C0 checks the knobs do not alias it).

- `ree_core/utils/config.py`: `LatentStackConfig.use_zself_ema_reset_init`, `use_shared_ema_reset_init`, `use_zharm_ema_reset_init` (all `False`, :194-196, next to the z_world knob); `REEConfig.from_dims(...)` named params (:8257-8259); assignments in the SD-008 block (:9739-9741). All three sites needed (from_dims swallows unknown kwargs).
- `ree_core/latent/stack.py` `encode()`: one `_reset_tick = (prev_state.timestamp or 0) == 0` and three knob-gated booleans (:1573-1581, the same t==0 test as SD-007's skip and the z_world knob).
  - z_self: `elif zself_reset_init: pass` before the legacy EMA `else:` (:1623) -- z_self(t0) = the instantaneous (post-precision) encode. **The SELF-1 GRU path (`use_self_recurrence`) is not touched**: it is a learned recurrence, not an EMA, and a zero initial hidden state is the GRU's convention; the knob is inert when SELF-1 is on (stated here, not pinned).
  - shared: `if not shared_reset_init:` wraps the three `alpha_shared` blends (:1721).
  - z_harm: the SD-036 block is skipped on the reset tick (`... and not zharm_reset_init`, :1785), so both harm streams start from the instantaneous encode; for z_harm_a this is a no-op on the agent path (prev already None).
  - No RNG touched; no other stream touched; `unified_latent_mode` ordering unchanged.
- `tests/test_flag_inertness.py`: the three flags added to PROBED (:2891-2893); `test_flag_registry_is_current` passes (direct call).
- `tests/contracts/test_sibling_ema_reset_init.py` (8 contracts). "raw" is read by forward hooks on the encoder modules inside the same `encode()` call, never derived from the EMA output:
  - C0 each knob defaults OFF on `LatentStackConfig` and `from_dims`, `from_dims` lands each one, turning one on leaves the others (and the z_world knob) OFF.
  - C1a OFF digest (sha256 of z_world/z_self/z_beta/z_theta/z_delta/z_harm, 24 ticks, 3 resets) == default-config digest at alpha_self 0.3, 0.9, and with the SD-036 harm config.
  - C1b OFF keeps the legacy scaled reset tick for every family (0.3 / 0.3 / 0.5 x hooked raw) -- the defect pin; passes on both trees by design.
  - C2 ON -> `||x(t0)|| == ||raw_x(t0)||` within 1e-6 and elementwise: z_self at 5 agent resets (alpha_self 0.3 and 0.9), shared latents at 5 agent resets, z_harm at 3 stack resets; each also checks another family stays legacy-scaled (independence).
  - C3a all knobs ON: the whole trajectory is `x(0) = raw(0)`, `x(t) = alpha*raw(t) + (1-alpha)*x(t-1)` for z_self, z_harm, z_beta, z_theta, z_delta (t = 1..5).
  - C3b ON == OFF bit-exact from a non-reset prev_state (timestamp 1) for all six streams.
- **Test half** (pre-build tree `298cb8ffd3` + this test file only, direct calls): 1/8 pass. C0 fails AttributeError, C1a/C3b TypeError (knob absent -- reachability failures, as in the parent build); **C2 x3 and C3a fail on the substantive assertion** (knobs set by attribute so the pre-build substrate runs and ignores them); C1b passes on both (defect pin). Post-build 8/8. The parent `test_zworld_ema_reset_init.py` still 8/8 post-build (old guard intact).
- **OFF pre/post bit-identity (native policy, actions included):** `probes/emasib/off_digest.py` -- default config, `act_with_split_obs`, alpha 0.3 and 0.9, 3 episodes each, 51 ticks, sha256 over z_world/z_self/z_beta/z_theta/z_delta/action bytes: pre-build `2615b97a...3d71d` == post-build `2615b97a...3d71d` (same machine).

## 3. Report-only: what ON changes (D1, untrained agent)

**Matched comparison -- identical env trajectories (scripted actions from `np.random.default_rng(seed)`, sense-only), seeds 106-110, 8 ep x 40 ticks, n=614 per arm, self_dim = world_dim = 32 (deployed), alpha_world = alpha_self = 0.3 (deployed defaults), z_world knob OFF** (`probes/emasib/matched_pr_zself.py`):

| arm | per-seed PR of z_self (106..110) | mean | reset enrichment, 0-1st pctile &#124;&#124;z_self&#124;&#124; | per-seed PR of z_beta | mean | reset enrichment, &#124;&#124;z_beta&#124;&#124; |
|---|---|---|---|---|---|---|
| OFF | 1.17 1.13 1.10 1.14 1.16 | 1.14 | 15.35x (7/7 bucket ticks t=0) | 1.00 1.00 1.00 1.00 1.00 | 1.00 | 15.35x |
| zself ON | 2.99 3.56 2.21 4.04 2.92 | **3.14** | 6.58x (3/7 t=0; others t=10,12,19,20) | 1.00 x5 | 1.00 | 15.35x |
| shared ON | 1.17 1.13 1.10 1.14 1.16 | 1.14 | 15.35x | 4.04 4.99 2.68 3.95 4.12 | **3.96** | 0.00x |
| zself + shared ON | 2.99 3.56 2.21 4.04 2.92 | 3.14 | 6.58x | 4.04 4.99 2.68 3.95 4.12 | 3.96 | 0.00x |

- Same pattern as z_world in the parent record: at alpha 0.3 the untrained stream is ~1-D, and that direction is the zero-init norm ramp `1 - 0.7^(t+1)` over the first ~8 ticks of each episode. Removing the ramp lifts per-seed PR ~2.8x for z_self and ~4x for z_beta. The knobs are independent in effect as well as in config (each single-knob arm leaves the other family's numbers unchanged to the printed precision).
- z_self ON still leaves 3 reset ticks in the lowest-percentile bucket. With the knob ON, z_self(t0) is exactly the raw encode (C2), so those are low-norm raw encodes at spawn, not an EMA artefact. Not investigated further.
- These are untrained-weight numbers (D1). Whether the PR gain survives training, and whether any consumer (E2 self-model, E3, beta gate) reads the reset tick differently, is not measured -- D2 not reached.
- z_harm has no PR row: the defect only exists in the non-default `harm_dim > 0`, matching-dims, `use_gabaergic_decay` configuration; C2/C3 pin it algebraically.

## 4. Not done / open

- **Default-ON for any of the four reset-init knobs (z_world + these three) is a user decision** -- flagged, not decided. The four are independent; a combined default flip would be one decision covering four switches.
- No D2 consumer check. The cheapest next check is still the W3 step-1 rollout re-check with the z_world knob ON (parent record sec 3); for these siblings, the analogous check is E2's z_self prediction error on the first tick after reset, ON vs OFF.
- SELF-1 (`use_self_recurrence`) reset behaviour is out of scope (GRU, not EMA).
- Pre-commit contract gate: ran LOCAL under the Mac lock (REE_PRECOMMIT_CONTRACTS_TARGET=local, lock held 04:31-04:56Z): tests/contracts on the staged commit tree, 5849 passed, 25 skipped, 1 xfailed, 0 failed (23m12s); validation-cache record a4b2e0c. The only commit between base 298cb8ffd3 and bdfe901b37 is that cache commit (touches none of this build's files); the four landed files are byte-identical to the tested tree (checked against origin/main).
