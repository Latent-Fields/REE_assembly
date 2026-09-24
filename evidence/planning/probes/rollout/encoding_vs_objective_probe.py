"""Discriminator: is the earliest broken edge the observation->z_world ENCODING or E2's OBJECTIVE?

bt0924-rollout-b (Worker D follow-on, orchestrate-20260924-breakthrough).

Regime: Worker B's CausalGridWorldV2 8x8 (2 hazards, 3 resources, max_ep 200), world_dim 32.
All data are UNIFORM-RANDOM one-hot actions (action independent of state by construction).

STEP 1 (ceiling). Per-step change explained by the action taken, in
  RAW   the raw world observation obs["world_state"]
  PCA   a FIXED PCA-32 of RAW (fit on a held-out random-policy batch from a different env
        seed, then frozen), rescaled to the same mean norm as z_world
  Z_d   z_world from agent.sense() for agents warmed at dose d (recipe B/BWF from
        rollout_fidelity_probe.py)
  metrics: eta^2 of the displacement by action class; held-out accuracy of a linear
  (softmax) classifier decoding the action from the displacement (chance = 1/A).

STEP 2. A FRESH E2FastPredictor world head (same architecture: world_transition
  Linear(32+A,128)-ReLU-Linear(128,32) residual + world_action_encoder) trained with the
  dose series' optimiser (Adam 3e-4, batch 32, clip 1.0, single-step MSE) for N steps on
  random-action transitions of each latent (PCA, Z_d), then evaluated on held-out
  random-action episodes: fidelity k (deepest h whose median rollout error < median
  persistence error), err/persistence and cos by h, and action discrimination (swap the
  first action for every class; is the executed one's prediction the closest to the
  outcome? chance 1/A). Native rollout function: E2FastPredictor.rollout_with_world.

ASCII-only output. One invocation = one dose of the z_world encoder (plus the PCA arm).
"""
from __future__ import annotations

import argparse
import copy
import json
import random
import sys
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F

HERE = Path(__file__).resolve().parent
WT = HERE / "ree-v3-wt"
sys.path.insert(0, str(WT))
sys.path.insert(0, str(HERE))

from ree_core.predictors.e2_fast import E2FastPredictor  # noqa: E402
import rollout_fidelity_probe as R  # noqa: E402  (build_B / warm_B reused verbatim)

torch.set_num_threads(2)


def collect(env, agent, n_steps, seed, want_z=True):
    """Uniform-random actions. Returns list of episodes; each = dict(raw [T,Dr], z [T,32], a [T])."""
    g = np.random.default_rng(seed)
    A = env.action_dim
    eps = []
    _f, obs = env.reset()
    if agent is not None:
        agent.reset()
    cur = {"raw": [], "z": [], "a": []}
    for _ in range(n_steps):
        raw = torch.as_tensor(obs["world_state"], dtype=torch.float32).reshape(-1)
        cur["raw"].append(raw)
        if want_z and agent is not None:
            with torch.no_grad():
                lat = agent.sense(obs["body_state"], obs["world_state"], obs_harm=obs.get("harm_obs"),
                                  obs_harm_a=obs.get("harm_obs_a"), obs_harm_history=obs.get("harm_history"))
            cur["z"].append(lat.z_world.detach().reshape(-1).clone())
        a = int(g.integers(0, A))
        cur["a"].append(a)
        _f, _h, done, _i, obs = env.step(a)
        if done:
            eps.append(cur)
            cur = {"raw": [], "z": [], "a": []}
            _f, obs = env.reset()
            if agent is not None:
                agent.reset()
    if len(cur["a"]) > 1:
        eps.append(cur)
    out = []
    for e in eps:
        d = {"raw": torch.stack(e["raw"]), "a": torch.tensor(e["a"])}
        if e["z"]:
            d["z"] = torch.stack(e["z"])
        out.append(d)
    return out


def transitions(eps, key):
    X0, X1, A = [], [], []
    for e in eps:
        x = e[key]
        if x.shape[0] < 2:
            continue
        X0.append(x[:-1]); X1.append(x[1:]); A.append(e["a"][:-1])
    return torch.cat(X0), torch.cat(X1), torch.cat(A)


def action_signal(eps_tr, eps_te, key, A, seed):
    x0, x1, a = transitions(eps_tr, key)
    d = x1 - x0
    tot = float(((d - d.mean(0)) ** 2).sum())
    btw = sum(int((a == c).sum()) * float(((d[a == c].mean(0) - d.mean(0)) ** 2).sum())
              for c in range(A) if int((a == c).sum()) > 0)
    eta2 = btw / tot if tot > 0 else None
    # linear softmax decoder of action from standardized displacement, held-out accuracy
    mu, sd = d.mean(0), d.std(0) + 1e-8
    torch.manual_seed(seed)
    W = torch.zeros(d.shape[1], A, requires_grad=True)
    b = torch.zeros(A, requires_grad=True)
    opt = torch.optim.Adam([W, b], lr=0.05)
    xs = (d - mu) / sd
    for _ in range(300):
        loss = F.cross_entropy(xs @ W + b, a) + 1e-3 * (W ** 2).sum()
        opt.zero_grad(); loss.backward(); opt.step()
    t0, t1, ta = transitions(eps_te, key)
    acc = float((((t1 - t0 - mu) / sd) @ W + b).argmax(-1).eq(ta).float().mean())
    frac_zero = float((d.norm(dim=-1) < 1e-9).float().mean())
    return {"eta2_delta_by_action": eta2, "decode_acc_heldout": acc, "chance": 1.0 / A,
            "n_train": int(d.shape[0]), "n_test": int(ta.shape[0]),
            "delta_norm_p50": float(d.norm(dim=-1).median()), "state_norm_p50": float(x0.norm(dim=-1).median()),
            "frac_zero_delta": frac_zero}


def train_head(eps_tr, key, A, steps, seed, D=32, skew=None):
    """skew=(cls, frac): batches drawn so that `frac` of rows have action `cls` (a
    monostrategy-like training distribution on the SAME transitions), else uniform."""
    torch.manual_seed(seed)
    from ree_core.utils.config import E2Config
    cfg = E2Config()
    cfg.world_dim = D
    cfg.self_dim = 32
    cfg.action_dim = A
    e2 = E2FastPredictor(cfg)
    params = list(e2.world_transition.parameters()) + list(e2.world_action_encoder.parameters())
    opt = torch.optim.Adam(params, lr=3e-4)
    x0, x1, a = transitions(eps_tr, key)
    oh = F.one_hot(a, A).float()
    n = x0.shape[0]
    losses = []
    if skew is not None:
        cls, frac = skew
        pos = torch.nonzero(a == cls).reshape(-1)
        neg = torch.nonzero(a != cls).reshape(-1)
    for i in range(steps):
        if skew is None:
            idx = torch.randint(0, n, (32,))
        else:
            k_pos = int(round(32 * frac))
            idx = torch.cat([pos[torch.randint(0, len(pos), (k_pos,))], neg[torch.randint(0, len(neg), (32 - k_pos,))]])
        loss = F.mse_loss(e2.world_forward(x0[idx], oh[idx]), x1[idx])
        opt.zero_grad(); loss.backward()
        torch.nn.utils.clip_grad_norm_(params, 1.0)
        opt.step()
        losses.append(float(loss.detach()))
    ident = float(F.mse_loss(x0, x1))
    return e2, {"loss_first50": float(np.mean(losses[:50])), "loss_last200": float(np.mean(losses[-200:])),
                "identity_mse": ident}


@torch.no_grad()
def evaluate(e2, eps_te, key, A, H, seed, max_starts=300):
    g = np.random.default_rng(seed)
    starts = [(i, t) for i, e in enumerate(eps_te) for t in range(e["a"].shape[0] - H)]
    if not starts:
        return None
    if len(starts) > max_starts:
        starts = [starts[j] for j in sorted(g.choice(len(starts), max_starts, replace=False))]
    allx = torch.cat([e[key] for e in eps_te])
    rows = {h: {"err": [], "pers": [], "chance": [], "cos": []} for h in range(1, H + 1)}
    disc = {h: [] for h in (1, 3, 5) if h <= H}
    zs = torch.zeros(1, 32)
    for i, t in starts:
        x = eps_te[i][key]
        acts = F.one_hot(eps_te[i]["a"][t:t + H], A).float().unsqueeze(0)
        x0 = x[t:t + 1]
        tr = e2.rollout_with_world(zs, x0, acts, compute_action_objects=False)
        for h in range(1, H + 1):
            p, y = tr.world_states[h], x[t + h:t + h + 1]
            rows[h]["err"].append(float((p - y).norm()))
            rows[h]["pers"].append(float((x0 - y).norm()))
            rows[h]["chance"].append(float((allx[int(g.integers(0, allx.shape[0]))] - y).norm()))
            dp, dy = (p - x0).reshape(-1), (y - x0).reshape(-1)
            if dp.norm() > 1e-9 and dy.norm() > 1e-9:
                rows[h]["cos"].append(float(F.cosine_similarity(dp, dy, dim=0)))
        for h in disc:
            ex = int(eps_te[i]["a"][t])
            errs = []
            for c in range(A):
                a2 = acts[:, :h].clone(); a2[0, 0] = 0.0; a2[0, 0, c] = 1.0
                tr2 = e2.rollout_with_world(zs, x0, a2, compute_action_objects=False)
                errs.append(float((tr2.world_states[h] - x[t + h:t + h + 1]).norm()))
            disc[h].append(int(np.argmin(errs)) == ex)
    out = {}
    k = 0
    for h in range(1, H + 1):
        r = rows[h]
        me, mp, mc = float(np.median(r["err"])), float(np.median(r["pers"])), float(np.median(r["chance"]))
        out[h] = {"err_over_pers": me / mp if mp > 0 else None, "err_over_chance": me / mc if mc > 0 else None,
                  "frac_beats_pers": float(np.mean(np.asarray(r["err"]) < np.asarray(r["pers"]))),
                  "cos_p50": float(np.median(r["cos"])) if r["cos"] else None}
        if mp > 0 and me < mp and k == h - 1:
            k = h
    return {"n_starts": len(starts), "k_beats_persistence": k, "by_h": out,
            "action_disc": {h: {"executed_closest": float(np.mean(v)), "chance": 1.0 / A, "n": len(v)}
                            for h, v in disc.items()}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dose", type=int, required=True, help="encoder warm steps (B/BWF recipe) for the Z arm")
    ap.add_argument("--recipe", default="BWF")
    ap.add_argument("--seed", type=int, default=43)
    ap.add_argument("--n-train", type=int, default=8000)
    ap.add_argument("--n-test", type=int, default=3000)
    ap.add_argument("--budgets", default="3000,10000")
    ap.add_argument("--H", type=int, default=10)
    ap.add_argument("--skip-pca", action="store_true")
    ap.add_argument("--p0-episodes", type=int, default=0, help="SD-070 z_world encoder warmup (run_zworld_p0) episodes")
    ap.add_argument("--p0-steps", type=int, default=50)
    ap.add_argument("--p0-preservation", type=float, default=-1.0, help="ZWorldP0Config.preservation_weight (-1 = default config)")
    ap.add_argument("--skew-budget", type=int, default=3000, help="monostrategy-skewed training control (0=off)")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    t0 = time.time()
    R.seed_all(a.seed)
    env, agent, cfg = R.build_B(a.seed, False)
    A = env.action_dim
    enc0 = [q.detach().clone() for q in agent.latent_stack.parameters()]
    winfo = R.warm_B(agent, env, a.seed, a.dose, a.recipe == "BWF") if a.dose > 0 else {"warm_steps": 0}
    if a.p0_episodes > 0:
        from experiments._lib.zworld_p0_warmup import run_zworld_p0
        from experiments._lib.capability_eval import RandomPolicy
        from ree_core.latent.zworld_p0 import ZWorldP0Config
        warm_env, _ag2, _c2 = R.build_B(a.seed, False)
        pcfg = ZWorldP0Config(preservation_weight=a.p0_preservation) if a.p0_preservation >= 0 else None
        p0 = run_zworld_p0(agent, warm_env, seed=a.seed, episodes=a.p0_episodes, steps_per_episode=a.p0_steps,
                           policy=RandomPolicy(a.seed), label="bt0924", dry_run=False, config=pcfg)
        winfo["p0"] = {k: v for k, v in p0.items() if isinstance(v, (int, float, str, bool))}
        agent.eval()
    winfo["encoder_param_delta_l2"] = float(torch.sqrt(sum(((q.detach() - q0) ** 2).sum()
                                                          for q, q0 in zip(agent.latent_stack.parameters(), enc0))))
    winfo["encoder_param_norm"] = float(torch.sqrt(sum((q0 ** 2).sum() for q0 in enc0)))
    agent.eval()
    print("WARM %s t=%.0fs" % (json.dumps(winfo, default=str)[:900], time.time() - t0), flush=True)
    # PCA fit batch: different env seed, raw only
    env_fit, _ag, _c = R.build_B(a.seed + 1000, False)
    fit = collect(env_fit, None, 3000, a.seed + 1000, want_z=False)
    rawfit = torch.cat([e["raw"] for e in fit])
    mu = rawfit.mean(0)
    U, S, V = torch.linalg.svd(rawfit - mu, full_matrices=False)
    P = V[:32].T  # [Dr, 32]
    evr = float((S[:32] ** 2).sum() / (S ** 2).sum())
    tr_eps = collect(env, agent, a.n_train, a.seed + 1)
    te_eps = collect(env, agent, a.n_test, a.seed + 2)
    znorm = float(torch.cat([e["z"] for e in tr_eps]).norm(dim=-1).mean())
    pnorm = float(((torch.cat([e["raw"] for e in tr_eps]) - mu) @ P).norm(dim=-1).mean())
    scale = znorm / pnorm
    for e in tr_eps + te_eps:
        e["pca"] = ((e["raw"] - mu) @ P) * scale
    print("DATA train_eps=%d test_eps=%d pca_evr=%.3f scale=%.4f t=%.0fs" % (len(tr_eps), len(te_eps), evr, scale, time.time() - t0), flush=True)
    res = {"args": vars(a), "warm": winfo, "pca_explained_var": evr, "pca_scale": scale,
           "raw_dim": int(rawfit.shape[1]), "ep_len_p50_train": float(np.median([e["a"].shape[0] for e in tr_eps])),
           "ceiling": {}, "heads": {}}
    for key in ("raw", "pca", "z"):
        res["ceiling"][key] = action_signal(tr_eps, te_eps, key, A, a.seed)
        print("CEIL %s %s" % (key, json.dumps(res["ceiling"][key])), flush=True)
    for key in (("z",) if a.skip_pca else ("pca", "z")):
        for n in [int(x) for x in a.budgets.split(",")]:
            e2, tinfo = train_head(tr_eps, key, A, n, a.seed)
            ev = evaluate(e2, te_eps, key, A, a.H, a.seed)
            res["heads"]["%s_%d" % (key, n)] = {"train": tinfo, "eval": ev}
            print("HEAD %s_%d train=%s k=%s disc=%s h1=%s t=%.0fs" % (
                key, n, json.dumps(tinfo), ev and ev["k_beats_persistence"], ev and json.dumps(ev["action_disc"]),
                ev and json.dumps(ev["by_h"][1]), time.time() - t0), flush=True)
    if a.skew_budget > 0:
        for key in (("z",) if a.skip_pca else ("pca", "z")):
          for fr in (0.95, 0.99):
            e2, tinfo = train_head(tr_eps, key, A, a.skew_budget, a.seed, skew=(1, fr))
            ev = evaluate(e2, te_eps, key, A, a.H, a.seed)
            tag = "%s_%d_skew%d" % (key, a.skew_budget, int(round(fr * 100)))
            res["heads"][tag] = {"train": tinfo, "eval": ev}
            print("HEAD %s k=%s disc=%s h1=%s t=%.0fs" % (
                tag, ev and ev["k_beats_persistence"], ev and json.dumps(ev["action_disc"]),
                ev and json.dumps(ev["by_h"][1]), time.time() - t0), flush=True)
    res["t_total_s"] = round(time.time() - t0, 1)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    json.dump(res, open(a.out, "w"), indent=1, default=str)
    print("wrote %s t=%.0fs" % (a.out, time.time() - t0), flush=True)


if __name__ == "__main__":
    main()
