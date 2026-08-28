"""
ARC-004 on the REAL LatentStack: arm A (as-built) vs arm B (serial smoothing).

Closes three stated limits of the two prior probes:
  - canonical observation routing (body_obs_dim=10, world_obs_dim=200), not a half-split
  - the REAL encoders, top-down maps, precision gating and split encoder
  - arm B measured in vivo rather than inferred from a numpy topology toy

Read-only: no substrate file is modified. Both arms are built by calling the
stack's own submodules, so they differ ONLY in where the EMA sits. Arm A is
fidelity-checked against the real stack.encode() before anything is measured.
"""
import sys, numpy as np, torch
sys.path.insert(0, "/Users/dgolden/REE_Working/ree-v3")
from ree_core.latent.stack import LatentStack
from ree_core.utils.config import LatentStackConfig
from ree_core.environment.causal_grid_world import CausalGridWorld

T, WARMUP, SEEDS = 1500, 200, 10
ALPHA = 0.3


def half_life(z):
    z = z - z.mean(axis=0, keepdims=True)
    sd = z.std(axis=0); keep = sd > 1e-9
    if keep.sum() == 0:
        return float("nan")
    z = z[:, keep] / sd[keep]
    prev_k, prev_r = 0, 1.0
    for k in range(1, 200):
        r = float((z[:-k] * z[k:]).mean())
        if r <= 0.5:
            return prev_k + (prev_r - 0.5) / (prev_r - r) * (k - prev_k) if prev_r != r else float(k)
        prev_k, prev_r = k, r
    return 200.0


def shared_path(stack, body_obs, world_obs):
    """Reproduce encode()'s shared-stack computation up to (not including) the EMA."""
    z_self_init, z_world_init, *_ = stack.split_encoder(body_obs, world_obs)
    combined_init = torch.cat([z_self_init, z_world_init], dim=-1)
    zb_init, _ = stack.beta_encoder(combined_init)
    zt_init, _ = stack.theta_encoder(zb_init)
    zd, _ = stack.delta_encoder(zt_init)
    zt, _ = stack.theta_encoder(zb_init, stack.delta_to_theta(zd))
    zb, _ = stack.beta_encoder(combined_init, stack.theta_to_beta(zt))
    return zb, zt, zd, combined_init, zb_init


def rollout(seed, arm, stack, env, obs_seq):
    zb = torch.zeros(1, stack.config.beta_dim)
    zt = torch.zeros(1, stack.config.theta_dim)
    zd = torch.zeros(1, stack.config.delta_dim)
    ZB, ZT, ZD = [], [], []
    for obs in obs_seq:
        body_obs, world_obs = obs[:, :stack.config.body_obs_dim], obs[:, stack.config.body_obs_dim:]
        if arm == "A":
            b, t_, d, _, _ = shared_path(stack, body_obs, world_obs)
            zb = ALPHA * b + (1 - ALPHA) * zb
            zt = ALPHA * t_ + (1 - ALPHA) * zt
            zd = ALPHA * d + (1 - ALPHA) * zd
        else:
            # serial: each depth reads the SMOOTHED value of the one below
            z_self_i, z_world_i, *_ = stack.split_encoder(body_obs, world_obs)
            combined_init = torch.cat([z_self_i, z_world_i], dim=-1)
            b_raw, _ = stack.beta_encoder(combined_init)
            zb = ALPHA * b_raw + (1 - ALPHA) * zb
            t_raw, _ = stack.theta_encoder(zb, stack.delta_to_theta(zd))
            zt = ALPHA * t_raw + (1 - ALPHA) * zt
            d_raw, _ = stack.delta_encoder(zt)
            zd = ALPHA * d_raw + (1 - ALPHA) * zd
        ZB.append(zb.detach().numpy()[0].copy())
        ZT.append(zt.detach().numpy()[0].copy())
        ZD.append(zd.detach().numpy()[0].copy())
    s = slice(WARMUP, None)
    return (half_life(np.array(ZB)[s]), half_life(np.array(ZT)[s]), half_life(np.array(ZD)[s]))


def build(seed):
    torch.manual_seed(seed)
    env = CausalGridWorld(seed=seed)
    cfg = LatentStackConfig(body_obs_dim=env.body_obs_dim,
                            world_obs_dim=env.world_obs_dim,
                            observation_dim=env.body_obs_dim + env.world_obs_dim)
    stack = LatentStack(cfg).eval()
    return env, stack


def obs_stream(env, seed, n):
    rng = np.random.default_rng(seed)
    _, parts = env.reset()
    out = []
    for _ in range(n):
        v = np.concatenate([np.asarray(parts["body_state"], dtype=np.float32).ravel(),
                            np.asarray(parts["world_state"], dtype=np.float32).ravel()])
        out.append(torch.tensor(v, dtype=torch.float32).unsqueeze(0))
        _, _, done, _, parts = env.step(int(rng.integers(0, env.action_dim)))
        if done:
            _, parts = env.reset()
    return out


# ---- fidelity check: does shared_path + parallel EMA match the real encode()? ----
env, stack = build(1000)
seq = obs_stream(env, 1000, 40)
with torch.no_grad():
    prev = None
    devs = []
    zb = torch.zeros(1, stack.config.beta_dim)
    zt = torch.zeros(1, stack.config.theta_dim)
    zd = torch.zeros(1, stack.config.delta_dim)
    for obs in seq:
        prev = stack.encode(obs, prev)
        b, t_, d, _, _ = shared_path(stack, obs[:, :stack.config.body_obs_dim],
                                     obs[:, stack.config.body_obs_dim:])
        zb = ALPHA * b + (1 - ALPHA) * zb
        zt = ALPHA * t_ + (1 - ALPHA) * zt
        zd = ALPHA * d + (1 - ALPHA) * zd
        devs.append(max(float((prev.z_beta - zb).abs().max()),
                        float((prev.z_theta - zt).abs().max()),
                        float((prev.z_delta - zd).abs().max())))
print(f"FIDELITY: max |arm-A manual - real stack.encode()| over 40 ticks = {max(devs):.3e}")
print(f"          (arm A is a faithful reimplementation iff this is ~0)\n")

print(f"ARC-004 on the REAL LatentStack -- canonical routing "
      f"(body={stack.config.body_obs_dim}, world={stack.config.world_obs_dim}), "
      f"{SEEDS} seeds, T={T}, random policy")
print(f"{'arm':<4} {'beta':>7} {'theta':>7} {'delta':>7} {'d-b':>8} {'0.8SD':>7} {'mono':>5}  verdict")
with torch.no_grad():
    for arm in ("A", "B"):
        rows = []
        for s in range(SEEDS):
            env, stack = build(1000 + s)
            rows.append(rollout(1000 + s, arm, stack, env, obs_stream(env, 1000 + s, T)))
        res = np.array(rows)
        b, t_, d = res[:, 0], res[:, 1], res[:, 2]
        delta = d - b; bar = 0.8 * delta.std(ddof=1)
        mono = int(sum(res[i, 2] > res[i, 1] > res[i, 0] for i in range(SEEDS)))
        v = "PASS" if (delta.mean() > bar and mono >= SEEDS - 1) else "FAIL"
        print(f"{arm:<4} {b.mean():7.2f} {t_.mean():7.2f} {d.mean():7.2f} "
              f"{delta.mean():8.3f} {bar:7.3f} {mono:>3}/{SEEDS}  {v}")

# ---------------------------------------------------------------------------
# RESULTS (2026-08-28, ree-v3 as checked out; 10 seeds, T=1500, random policy).
#
#   FIDELITY: max |arm-A manual - real stack.encode()| = 0.000e+00 over 40 ticks.
#             Arm A is a bit-identical reimplementation of the shared-stack path.
#
#   arm   beta   theta  delta   d-b     0.8*SD  mono    verdict
#   A     5.00   5.05   5.10    +0.102  0.354   4/10    FAIL
#   B     5.00   7.71   9.34    +4.342  0.510  10/10    PASS
#
# METHOD-SENSITIVITY of arm A (routing x estimator x action count x env seeding,
# 8 variants, 10 seeds each): mean(delta - beta) spans -0.037 .. +0.102, every
# value far below its own 0.8*SD bar (0.33 .. 0.56), monotone-ordering count
# 2..4 of 10 throughout. The as-built effect is indistinguishable from zero and
# its SIGN is not stable across incidental methodological choices. Arm B's
# +4.342 is an order of magnitude outside that band.
#
# The 2026-08-26 probe's "-0.159, 0/5 seeds, the margin points the wrong way" is
# a 5-seed reading inside this zero-centred band; that script uses an UNSEEDED
# CausalGridWorld() and is not deterministic -- re-running it as recovered gives
# -0.125 and -0.097 on successive runs. Its FAIL verdict reproduces under every
# variant tested; its DIRECTION claim does not.
# ---------------------------------------------------------------------------
