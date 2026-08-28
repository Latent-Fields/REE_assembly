"""
ARC-004 wiring probe: is the depth stack's failure a TRAINING failure or a WIRING failure?

Motivation. ARC-004's own non-degeneracy precondition asserts the differentiation
"must emerge from the recursive top-down architecture (z_delta reads only z_theta's
HISTORY, z_theta reads only z_beta's, so information at each level is progressively
more temporally aggregated)". Source check (ree_core/latent/stack.py) says otherwise:
the beta->theta->delta cascade is entirely WITHIN-TICK on the current observation
(l.1345-1347), and prev_state.z_{beta,theta,delta} appear at exactly three lines --
the terminal EMA (l.1508-1510), applied in PARALLEL with one shared constant.

So as built the three layers are three parallel first-order filters with identical
time constants. This probe asks what would have to change for ARC-004's PASS
prediction to be reachable at all, and whether MECH-523's training-absence reading
is sufficient to explain the null.

ARMS (all share the same input stream and the same random encoders per seed):
  A  as-built     within-tick cascade, parallel EMA           (reproduces the null)
  B  serial       cascade over the SMOOTHED value, ReLU MLP   (the wiring ARC-004 describes)
  C  serial-lin   same, but LINEAR encoders                   (isolates the ReLU's effect)
  D  per-alpha    as-built wiring, per-layer alphas           (built-in rate split; ARC-004
                                                               calls this vacuous-by-construction)

Scored on ARC-004's own criterion: monotone half-life ordering delta > theta > beta
by a margin exceeding 0.8 * SD of the seed-to-seed (delta - beta) delta.

Read-only. No substrate change, no repo writes.
"""
import numpy as np

RHO = 0.95
DIM_IN, DIM_H, DIM_OUT = 32, 64, 32
T, WARMUP, SEEDS = 4000, 500, 5
ALPHA = 0.3
ALPHAS_D = (0.5, 0.3, 0.1)  # arm D: beta fast, delta slow


def mlp(rng, din, dh, dout, linear=False):
    """Untrained encoder, matching SharedDepthEncoder: Linear->ReLU->Linear, x sigmoid(0)=0.5."""
    W1 = rng.normal(0, 1 / np.sqrt(din), (din, dh))
    b1 = np.zeros(dh)
    W2 = rng.normal(0, 1 / np.sqrt(dh), (dh, dout))
    b2 = np.zeros(dout)

    def f(x):
        h = x @ W1 + b1
        if not linear:
            h = np.maximum(h, 0.0)
        return (h @ W2 + b2) * 0.5  # precision gate at init

    return f


def half_life(z):
    """Lag-k autocorrelation half-life, dim-averaged, linear interp at r=0.5."""
    z = z - z.mean(axis=0, keepdims=True)
    sd = z.std(axis=0)
    keep = sd > 1e-9
    if keep.sum() == 0:
        return np.nan
    z = z[:, keep] / sd[keep]
    n = z.shape[0]
    prev_k, prev_r = 0, 1.0
    for k in range(1, 60):
        r = float((z[:-k] * z[k:]).mean())
        if r <= 0.5:
            if prev_r == r:
                return float(k)
            return prev_k + (prev_r - 0.5) / (prev_r - r) * (k - prev_k)
        prev_k, prev_r = k, r
    return 60.0


def run(seed, arm):
    rng = np.random.default_rng(seed)
    lin = (arm == "C")
    fb = mlp(rng, DIM_IN, DIM_H, DIM_OUT, lin)
    ft = mlp(rng, DIM_OUT, DIM_H, DIM_OUT, lin)
    fd = mlp(rng, DIM_OUT, DIM_H, DIM_OUT, lin)

    # AR(1) input stream
    x = np.zeros((T, DIM_IN))
    for t in range(1, T):
        x[t] = RHO * x[t - 1] + np.sqrt(1 - RHO ** 2) * rng.normal(size=DIM_IN)

    ab, at, ad = (ALPHAS_D if arm == "D" else (ALPHA, ALPHA, ALPHA))
    zb = np.zeros(DIM_OUT); zt = np.zeros(DIM_OUT); zd = np.zeros(DIM_OUT)
    ZB, ZT, ZD = [], [], []
    for t in range(T):
        if arm in ("A", "D"):
            # within-tick cascade on the RAW value, then three parallel EMAs
            b_raw = fb(x[t]); t_raw = ft(b_raw); d_raw = fd(t_raw)
            zb = ab * b_raw + (1 - ab) * zb
            zt = at * t_raw + (1 - at) * zt
            zd = ad * d_raw + (1 - ad) * zd
        else:
            # serial: each layer reads the SMOOTHED value of the one below
            b_raw = fb(x[t]);  zb = ab * b_raw + (1 - ab) * zb
            t_raw = ft(zb);    zt = at * t_raw + (1 - at) * zt
            d_raw = fd(zt);    zd = ad * d_raw + (1 - ad) * zd
        ZB.append(zb.copy()); ZT.append(zt.copy()); ZD.append(zd.copy())
    s = slice(WARMUP, None)
    return (half_life(np.array(ZB)[s]), half_life(np.array(ZT)[s]), half_life(np.array(ZD)[s]))


NAMES = {"A": "as-built (parallel EMA, within-tick cascade)",
         "B": "serial cascade, ReLU encoders",
         "C": "serial cascade, LINEAR encoders",
         "D": "as-built wiring, per-layer alphas 0.5/0.3/0.1"}

print(f"ARC-004 wiring probe -- AR(1) rho={RHO}, {SEEDS} seeds, T={T}, alpha={ALPHA}")
print(f"single-EMA analytic half-life = ln(0.5)/ln(1-alpha) = "
      f"{np.log(0.5)/np.log(1-ALPHA):.2f} ticks\n")
print(f"{'arm':<4} {'beta':>7} {'theta':>7} {'delta':>7} {'d-b':>8} {'0.8*SD':>8} "
      f"{'mono':>5}  verdict")
for arm in ("A", "B", "C", "D"):
    res = np.array([run(1000 + s, arm) for s in range(SEEDS)])
    b, t_, d = res[:, 0], res[:, 1], res[:, 2]
    delta = d - b
    bar = 0.8 * delta.std(ddof=1)
    mono = int(sum((res[i, 2] > res[i, 1] > res[i, 0]) for i in range(SEEDS)))
    verdict = "PASS" if (delta.mean() > bar and mono >= 4) else "FAIL"
    print(f"{arm:<4} {b.mean():7.2f} {t_.mean():7.2f} {d.mean():7.2f} "
          f"{delta.mean():8.3f} {bar:8.3f} {mono:>3}/5  {verdict}   {NAMES[arm]}")

# ---------------------------------------------------------------------------
# ROBUSTNESS SWEEP (as run 2026-08-28). Set RHO and SEEDS above, or run this
# block, to reproduce the rho sweep reported in the accompanying .md:
#
#   rho    A (as-built)          B (serial, ReLU)      C (serial, linear)
#   0.00   -0.008  2/8  FAIL     +4.241  8/8  PASS     +4.467  8/8  PASS
#   0.50   -0.210  0/8  FAIL     +3.370  8/8  PASS     +3.596  8/8  PASS
#   0.90   -1.078  0/8  FAIL     +2.057  8/8  PASS     +3.101  8/8  PASS
#   0.95   -2.212  0/8  FAIL     +0.873  7/8  PASS     +3.074  8/8  PASS
#   0.99  -10.757  0/8  FAIL     -8.012  0/8  FAIL     +0.166  0/8  FAIL
#
# Arm A is inverted at every rho > 0 and matches the EMA-alone analytic value
# (1.94) on all three layers at rho = 0. Arm B clears ARC-004's bar across the
# operationally relevant band and fails only as the input approaches a random
# walk, where per-stage nonlinear decorrelation outruns the cascade gain.
# ---------------------------------------------------------------------------
