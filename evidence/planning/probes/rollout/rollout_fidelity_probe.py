"""E2 rollout fidelity + consumer reach + proposal state-dependence probe.

bt0924-rollout (Worker D, orchestrate-20260924-breakthrough),
chip_ref chip-20260924-e2-rollout-divergence-remeasure.

One cell per invocation (one regime, one recipe, one dose, one seed). CPU, 2 threads.

REGIMES
  B   Worker B's residue-probe regime verbatim (CausalGridWorldV2 8x8, 2 hazards,
      3 resources, max_ep 200, REEConfig.from_dims defaults world_dim=32, B's
      sleep/residue flags, sleep never fires). Recipes:
        B    B's own warmup: Adam(agent.parameters()) on compute_prediction_loss()
             + compute_e2_loss()  (the CANARY: reproduces B's measurement)
        BWF  B's warmup PLUS the canonical single-step world_forward MSE step
             (experiments/_lib/goal_pipeline_tier1.warmup_train: Adam lr 3e-4 over
             e2.world_transition + e2.world_action_encoder, batch 32, buffer 2000)
  C   V3-EXQ-1061's builder + its own warmup_train (terrain_prior BC + world_forward
      single-step MSE + main params), intact arm, production ao_std floor 0.2, with
      WORLD_DIM = SELF_DIM = 32 patched in (deployed dims; C ran 16).

MEASUREMENTS (after warmup; agent.eval(); StepHarness train_mode=False waking run)
  M0  parameter reach of the warmup on e2.world_transition (L2 delta).
  M1  per-rollout-step z_world norm of the candidate world_states E3 actually scores
      (hook on E3.score_trajectory inside E3.select = the production consumer path).
  M2  open-loop fidelity: from each visited z_world_t, native E2.rollout_with_world
      with the EXECUTED action sequence; error vs the actual encoded z_world_{t+h},
      against persistence (z_t) and chance (random visited state) baselines, and
      cosine(pred delta, actual delta). k = deepest h at which the rollout still
      beats persistence on median.
  M3  consumer reach (D2): re-score each recorded E3 candidate set with E3's own
      score_trajectory under FULL / TRUNC_d (native SD-081 _score_depth_limit = d+1)
      / SHUF_d (world steps > d replaced by a deranged other candidate's steps).
      argmin agreement vs FULL, Spearman rho, share of J spread from steps > d.
  M4  proposal state-dependence: hippocampal.propose_trajectories at probe states
      (C's P3 measure: first-action class share, majority class across states),
      native vs CEM scoring window restricted to max_horizon = d.

ASCII-only output.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import random
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F

HERE = Path(__file__).resolve().parent
WT = HERE / "ree-v3-wt"
sys.path.insert(0, str(WT))
sys.path.insert(0, str(WT / "experiments"))

from ree_core.agent import REEAgent  # noqa: E402
from ree_core.environment.causal_grid_world import CausalGridWorldV2  # noqa: E402
from ree_core.utils.config import REEConfig  # noqa: E402
from experiments._harness import StepHarness  # noqa: E402

torch.set_num_threads(2)


def seed_all(s):
    random.seed(s)
    np.random.seed(s)
    torch.manual_seed(s)


def wt_norm(agent):
    return float(torch.sqrt(sum((p.detach() ** 2).sum() for p in
                                list(agent.e2.world_transition.parameters())
                                + list(agent.e2.world_action_encoder.parameters()))))


def wt_snapshot(agent):
    return [p.detach().clone() for p in list(agent.e2.world_transition.parameters())
            + list(agent.e2.world_action_encoder.parameters())]


def wt_delta(agent, snap):
    cur = list(agent.e2.world_transition.parameters()) + list(agent.e2.world_action_encoder.parameters())
    return float(torch.sqrt(sum(((a.detach() - b) ** 2).sum() for a, b in zip(cur, snap))))


# ----------------------------------------------------------------- regime B
def build_B(seed, clamp):
    env = CausalGridWorldV2(size=8, num_hazards=2, num_resources=3, max_episode_steps=200, seed=seed)
    kw = dict(body_obs_dim=env.body_obs_dim, world_obs_dim=env.world_obs_dim,
              action_dim=env.action_dim, use_sleep_aggregation_cluster=True,
              use_cross_module_consolidation=True, use_sleep_residue_integration=True,
              use_offline_integration_gradient_step=True, sleep_loop_episodes_K=10_000_000)
    if clamp:
        kw["e2_rollout_output_norm_clamp_enabled"] = True
        kw["e2_rollout_output_norm_clamp_ratio"] = 2.0
    cfg = REEConfig.from_dims(**kw)
    if clamp:
        assert cfg.e2.e2_rollout_output_norm_clamp_enabled is True
    agent = REEAgent(cfg).to(torch.device("cpu"))
    agent.eval()
    return env, agent, cfg


def warm_B(agent, env, seed, steps, train_wf):
    info = {"warm_steps": steps, "train_wf": bool(train_wf)}
    snap = wt_snapshot(agent)
    info["wt_norm_before"] = wt_norm(agent)
    if steps <= 0:
        info["wt_delta"] = 0.0
        return info
    opt = torch.optim.Adam(agent.parameters(), lr=1e-3)
    wf_params = list(agent.e2.world_transition.parameters()) + list(agent.e2.world_action_encoder.parameters())
    wf_opt = torch.optim.Adam(wf_params, lr=3e-4)
    harness = StepHarness(agent, env, train_mode=True, seed=seed)
    agent.train()
    _f, obs = env.reset()
    agent.reset()
    harness.reset()
    losses, wf_losses = [], []
    wf_buf = []
    z_prev, a_prev = None, None
    for i in range(steps):
        r = harness.step(obs)
        obs = r.next_obs_dict
        loss = agent.compute_prediction_loss() + agent.compute_e2_loss()
        if loss.requires_grad:
            opt.zero_grad()
            loss.backward()
            opt.step()
        losses.append(float(loss.detach().item()))
        if train_wf:
            z_cur = r.latent.z_world.detach()
            if z_prev is not None:
                wf_buf.append((z_prev, a_prev, z_cur))
                if len(wf_buf) > 2000:
                    wf_buf = wf_buf[-2000:]
            z_prev, a_prev = z_cur, r.action.detach().reshape(1, -1).float()
            if len(wf_buf) >= 32:
                idx = torch.randperm(len(wf_buf))[:32].tolist()
                zb = torch.cat([wf_buf[j][0] for j in idx])
                ab = torch.cat([wf_buf[j][1] for j in idx])
                z1 = torch.cat([wf_buf[j][2] for j in idx])
                wl = F.mse_loss(agent.e2.world_forward(zb, ab), z1)
                wf_opt.zero_grad()
                wl.backward()
                torch.nn.utils.clip_grad_norm_(wf_params, 1.0)
                wf_opt.step()
                wf_losses.append(float(wl.item()))
        if r.done:
            _f, obs = env.reset()
            agent.reset()
            harness.reset()
            z_prev, a_prev = None, None
    agent.eval()
    agent.reset()
    info["loss_first50"] = float(np.mean(losses[:50]))
    info["loss_last50"] = float(np.mean(losses[-50:]))
    if wf_losses:
        info["wf_loss_first50"] = float(np.mean(wf_losses[:50]))
        info["wf_loss_last50"] = float(np.mean(wf_losses[-50:]))
        info["wf_train_steps"] = len(wf_losses)
    info["wt_delta"] = wt_delta(agent, snap)
    info["wt_norm_after"] = wt_norm(agent)
    return info


# ----------------------------------------------------------------- regime C
def build_warm_C(seed, eps, clamp):
    import v3_exq_1061_mech131_anticipatory_residue_lesion as X
    X.WORLD_DIM = 32
    X.SELF_DIM = 32
    agent, env, cfg = X.build_agent(True, True, seed, X.PRODUCTION_FLOOR)
    if clamp:
        agent.e2.config.e2_rollout_output_norm_clamp_enabled = True
        agent.e2.config.e2_rollout_output_norm_clamp_ratio = 2.0
    assert agent.e2.config.world_dim == 32 and cfg.latent.world_dim == 32
    snap = wt_snapshot(agent)
    info = {"warm_eps": eps, "steps_per_ep": 100, "wt_norm_before": wt_norm(agent)}
    if eps > 0:
        w = X.warmup_train(agent, env, seed, eps, 100)
        for k in ("final_obs", "_harm_pos", "_harm_neg"):
            w.pop(k, None)
        info["warm"] = {k: v for k, v in w.items() if isinstance(v, (int, float, str, bool))}
    info["wt_delta"] = wt_delta(agent, snap)
    info["wt_norm_after"] = wt_norm(agent)
    agent.eval()
    agent.reset()
    return env, agent, cfg, info


# ----------------------------------------------------------------- waking + hooks
class Rec:
    def __init__(self, agent):
        self.agent = agent
        self.selects = []
        self._cur = None
        self.active = True
        e3 = agent.e3
        orig_sel = e3.select
        orig_st = e3.score_trajectory
        rec = self

        def st(traj, *a, **k):
            if rec.active and rec._cur is not None:
                rec._cur.append((traj, dict(k)))
            return orig_st(traj, *a, **k)

        def sel(candidates, *a, **k):
            rec._cur = []
            out = orig_sel(candidates, *a, **k)
            if rec.active and rec._cur:
                rec.selects.append({"calls": rec._cur, "sel": e3.last_selected_idx})
            rec._cur = None
            return out

        e3.score_trajectory = st
        e3.select = sel


def waking(agent, env, steps, seed):
    rec = Rec(agent)
    harness = StepHarness(agent, env, train_mode=False, seed=seed)
    _f, obs = env.reset()
    agent.reset()
    harness.reset()
    traj_log = []   # per step: (episode_id, z_world [1,D], z_self [1,S], action [1,A])
    ep = 0
    harm = 0
    for _ in range(steps):
        r = harness.step(obs)
        traj_log.append((ep, r.latent.z_world.detach().clone(), r.latent.z_self.detach().clone(),
                         r.action.detach().reshape(1, -1).float().clone()))
        if r.harm_signal < 0:
            harm += 1
        obs = r.next_obs_dict
        if r.done:
            _f, obs = env.reset()
            agent.reset()
            harness.reset()
            ep += 1
    rec.active = False
    return rec, traj_log, harm


def pct(x):
    x = np.asarray(x, dtype=float)
    if x.size == 0:
        return None
    return {"p05": float(np.quantile(x, 0.05)), "p50": float(np.median(x)), "p95": float(np.quantile(x, 0.95))}


# M1
def m1_candidate_norms(rec, cfg_h):
    per = {}
    spread = {}
    for s in rec.selects:
        wss = []
        for traj, _k in s["calls"]:
            ws = traj.get_world_state_sequence()
            if ws is None:
                continue
            wss.append(ws.reshape(-1, ws.shape[-2], ws.shape[-1])[0])
        if not wss:
            continue
        W = torch.stack(wss)  # [C, T, D]
        for t in range(W.shape[1]):
            per.setdefault(t, []).extend(W[:, t, :].norm(dim=-1).tolist())
            if W.shape[0] > 1:
                d = torch.pdist(W[:, t, :])
                spread.setdefault(t, []).append(float(d.mean() / (W[:, t, :].norm(dim=-1).mean() + 1e-12)))
    out = {}
    for t in sorted(per):
        v = np.asarray(per[t])
        out[t] = {"norm_p50": float(np.median(v)), "norm_p95": float(np.quantile(v, 0.95)),
                  "rel_pairwise_spread_p50": float(np.median(spread[t])) if t in spread else None}
    ratios = []
    ts = sorted(out)
    for a, b in zip(ts[:-1], ts[1:]):
        if out[a]["norm_p50"] > 0:
            ratios.append(out[b]["norm_p50"] / out[a]["norm_p50"])
    return out, (float(np.median(ratios[-10:])) if ratios else None)


# M2
@torch.no_grad()
def m2_fidelity(agent, traj_log, H, n_starts, seed):
    g = np.random.default_rng(seed)
    n = len(traj_log)
    zs = torch.cat([t[1] for t in traj_log])  # [N, D]
    starts = []
    for t0 in range(n):
        if t0 + H < n and traj_log[t0][0] == traj_log[t0 + H][0]:
            starts.append(t0)
    if not starts:
        return None
    if len(starts) > n_starts:
        starts = sorted(g.choice(starts, n_starts, replace=False).tolist())
    rows = {h: {"err": [], "pers": [], "chance": [], "cos": [], "pnorm": [], "anorm": []} for h in range(1, H + 1)}
    for t0 in starts:
        z0 = traj_log[t0][1]
        s0 = traj_log[t0][2]
        acts = torch.cat([traj_log[t0 + j][3] for j in range(H)]).unsqueeze(0)  # [1,H,A]
        tr = agent.e2.rollout_with_world(s0, z0, acts, compute_action_objects=False)
        for h in range(1, H + 1):
            pred = tr.world_states[h]
            act = traj_log[t0 + h][1]
            rnd = zs[int(g.integers(0, n))].unsqueeze(0)
            e = float((pred - act).norm())
            rows[h]["err"].append(e)
            rows[h]["pers"].append(float((z0 - act).norm()))
            rows[h]["chance"].append(float((rnd - act).norm()))
            dp = (pred - z0).reshape(-1)
            da = (act - z0).reshape(-1)
            if dp.norm() > 1e-9 and da.norm() > 1e-9:
                rows[h]["cos"].append(float(F.cosine_similarity(dp, da, dim=0)))
            rows[h]["pnorm"].append(float(pred.norm()))
            rows[h]["anorm"].append(float(act.norm()))
    out = {}
    k_pers = 0
    k_chance = 0
    for h in range(1, H + 1):
        r = rows[h]
        me, mp, mc = float(np.median(r["err"])), float(np.median(r["pers"])), float(np.median(r["chance"]))
        out[h] = {"err_p50": me, "pers_p50": mp, "chance_p50": mc,
                  "err_over_pers": me / mp if mp > 0 else None,
                  "err_over_chance": me / mc if mc > 0 else None,
                  "frac_beats_pers": float(np.mean(np.asarray(r["err"]) < np.asarray(r["pers"]))),
                  "cos_delta_p50": float(np.median(r["cos"])) if r["cos"] else None,
                  "pred_norm_p50": float(np.median(r["pnorm"])), "actual_norm_p50": float(np.median(r["anorm"]))}
        if me < mp and k_pers == h - 1:
            k_pers = h
        if me < mc and k_chance == h - 1:
            k_chance = h
    # M2b action discrimination: swap the FIRST action for each one-hot class (rest executed);
    # is the executed action's prediction the closest to what actually happened? chance = 1/A.
    A = traj_log[0][3].shape[-1]
    disc = {}
    for h in (1, 3, 5):
        top1 = []
        rank = []
        for t0 in starts:
            if t0 + h >= n or traj_log[t0][0] != traj_log[t0 + h][0]:
                continue
            z0, s0 = traj_log[t0][1], traj_log[t0][2]
            acts = torch.cat([traj_log[t0 + j][3] for j in range(h)]).unsqueeze(0)
            ex = int(acts[0, 0].argmax())
            if float(acts[0, 0].max()) < 0.5:
                continue
            errs = []
            for c in range(A):
                a2 = acts.clone()
                a2[0, 0] = 0.0
                a2[0, 0, c] = 1.0
                tr = agent.e2.rollout_with_world(s0, z0, a2, compute_action_objects=False)
                errs.append(float((tr.world_states[h] - traj_log[t0 + h][1]).norm()))
            order = np.argsort(errs)
            top1.append(int(order[0]) == ex)
            rank.append(int(np.where(order == ex)[0][0]))
        if top1:
            disc[h] = {"n": len(top1), "executed_is_closest": float(np.mean(top1)), "chance": 1.0 / A,
                       "mean_rank": float(np.mean(rank))}
    # M2c: does the ACTUAL encoded z_world step carry the executed action at all? eta^2 of
    # delta-z_world by executed action class over all logged within-episode transitions.
    dz, lab = [], []
    for t in range(n - 1):
        if traj_log[t][0] == traj_log[t + 1][0]:
            dz.append((traj_log[t + 1][1] - traj_log[t][1]).reshape(-1))
            lab.append(int(traj_log[t][3].argmax()))
    eta = None
    if len(dz) > 10:
        D = torch.stack(dz)
        tot = float(((D - D.mean(0)) ** 2).sum())
        btw = 0.0
        for c in set(lab):
            m = [i for i, x in enumerate(lab) if x == c]
            btw += len(m) * float(((D[m].mean(0) - D.mean(0)) ** 2).sum())
        eta = {"eta2_delta_by_action": btw / tot if tot > 0 else None, "n": len(dz),
               "delta_norm_p50": float(D.norm(dim=-1).median()),
               "action_counts": {str(k): v for k, v in sorted(Counter(lab).items())}}
    return {"n_starts": len(starts), "by_h": out, "k_beats_persistence": k_pers, "k_beats_chance": k_chance,
            "visited_norm_p50": float(zs.norm(dim=-1).median()), "action_discrimination": disc,
            "actual_delta_action_eta2": eta}


# M3
def _spearman(a, b):
    ra = np.argsort(np.argsort(a))
    rb = np.argsort(np.argsort(b))
    if np.std(ra) == 0 or np.std(rb) == 0:
        return None
    return float(np.corrcoef(ra, rb)[0, 1])


def _shuffled_traj(traj, donor, d):
    t2 = copy.copy(traj)
    ws = list(traj.world_states)
    dws = donor.world_states
    for i in range(d + 1, len(ws)):
        ws[i] = dws[i]
    t2.world_states = ws
    return t2


@torch.no_grad()
def m3_consumer(agent, rec, depths, max_selects, seed):
    e3 = agent.e3
    g = np.random.default_rng(seed + 7)
    sels = [s for s in rec.selects if len(s["calls"]) >= 2]
    if len(sels) > max_selects:
        idx = sorted(g.choice(len(sels), max_selects, replace=False).tolist())
        sels = [sels[i] for i in idx]
    prev_decomp = e3.e3_score_decomp_enabled
    prev_depth = e3._score_depth_limit
    e3.e3_score_decomp_enabled = True
    res = {d: {"trunc_same": [], "shuf_same": [], "trunc_rho": [], "shuf_rho": [], "deep_share": []} for d in depths}
    comp_full = {"f_weighted": [], "harm_weighted": [], "residue_weighted": [], "benefit_weighted": []}
    spreads = []
    native_same = []
    try:
        for s in sels:
            calls = s["calls"]
            e3._score_depth_limit = None
            full = []
            comps = []
            for traj, kw in calls:
                full.append(float(e3.score_trajectory(traj, **kw).mean()))
                comps.append(dict(e3._last_traj_components))
            full = np.asarray(full)
            spreads.append(float(full.std()))
            for key in comp_full:
                v = np.asarray([c.get(key, 0.0) for c in comps])
                comp_full[key].append(float(v.std()))
            a_full = int(np.argmin(full))
            if s["sel"] is not None:
                native_same.append(int(s["sel"]) == a_full)
            C = len(calls)
            perm = np.roll(np.arange(C), 1 + int(g.integers(0, C - 1)))  # derangement
            for d in depths:
                e3._score_depth_limit = d + 1
                tr = np.asarray([float(e3.score_trajectory(traj, **kw).mean()) for traj, kw in calls])
                e3._score_depth_limit = None
                sh = np.asarray([float(e3.score_trajectory(_shuffled_traj(calls[i][0], calls[perm[i]][0], d),
                                                           **calls[i][1]).mean()) for i in range(C)])
                res[d]["trunc_same"].append(int(np.argmin(tr)) == a_full)
                res[d]["shuf_same"].append(int(np.argmin(sh)) == a_full)
                res[d]["trunc_rho"].append(_spearman(full, tr))
                res[d]["shuf_rho"].append(_spearman(full, sh))
                # share of full-J cross-candidate variance NOT reproduced by the first d steps
                resid = full - tr
                vf = float(full.var())
                res[d]["deep_share"].append(float(resid.var() / vf) if vf > 0 else None)
    finally:
        e3._score_depth_limit = prev_depth
        e3.e3_score_decomp_enabled = prev_decomp

    def mean(v):
        v = [x for x in v if x is not None]
        return float(np.mean(v)) if v else None
    out = {"n_selects": len(sels), "J_spread_std_p50": float(np.median(spreads)) if spreads else None,
           "native_selected_eq_Jargmin": mean(native_same),
           "component_spread_std_p50": {k: float(np.median(v)) if v else None for k, v in comp_full.items()},
           "by_depth": {}}
    for d in depths:
        r = res[d]
        out["by_depth"][d] = {"trunc_argmin_same": mean(r["trunc_same"]), "shuf_argmin_same": mean(r["shuf_same"]),
                              "trunc_spearman": mean(r["trunc_rho"]), "shuf_spearman": mean(r["shuf_rho"]),
                              "deep_var_share_p50": (float(np.median([x for x in r["deep_share"] if x is not None]))
                                                     if any(x is not None for x in r["deep_share"]) else None)}
    return out


# M4
@torch.no_grad()
def m4_proposal(agent, traj_log, n_states, depths, seed):
    hip = agent.hippocampal
    orig_st = hip._score_trajectory
    idx = np.linspace(0, len(traj_log) - 1, n_states).astype(int).tolist()
    arms = [None] + list(depths)
    out = {}
    for arm in arms:
        rows = []
        if arm is not None:
            def st(traj, max_horizon=None, _o=orig_st, _d=arm, **k):
                mh = _d if max_horizon is None else min(max_horizon, _d)
                return _o(traj, max_horizon=mh, **k)
            hip._score_trajectory = st
        try:
            for j, t in enumerate(idx):
                z_world = traj_log[t][1]
                z_self = traj_log[t][2]
                torch.manual_seed(seed * 1000 + j)
                trajs = hip.propose_trajectories(z_world, z_self=z_self)
                cls = [hip.candidate_first_action_class(tr) for tr in trajs]
                cls = [c for c in cls if c is not None]
                cc = Counter(cls)
                maj, nmaj = cc.most_common(1)[0]
                p = np.asarray(list(cc.values()), dtype=float) / len(cls)
                rows.append({"n": len(cls), "maj": int(maj), "maj_share": nmaj / len(cls),
                             "n_classes": len(cc), "entropy": float(-(p * np.log(p)).sum()),
                             "counts": {str(k): v for k, v in sorted(cc.items())}})
        finally:
            hip._score_trajectory = orig_st
        majs = Counter(r["maj"] for r in rows)
        out["native" if arm is None else "cem_window_%d" % arm] = {
            "n_states": len(rows),
            "maj_share_mean": float(np.mean([r["maj_share"] for r in rows])),
            "n_classes_mean": float(np.mean([r["n_classes"] for r in rows])),
            "entropy_mean": float(np.mean([r["entropy"] for r in rows])),
            "majority_class_counts_across_states": {str(k): v for k, v in sorted(majs.items())},
            "frac_states_with_modal_majority": majs.most_common(1)[0][1] / len(rows),
            "first_rows": rows[:3],
        }
    # decomposition of where state-invariance lives: terrain_prior output variation
    with torch.no_grad():
        zw = torch.cat([traj_log[t][1] for t in idx])
        aom = hip._get_terrain_action_object_mean(zw)          # [N, H, ao]
        acts0 = hip._decode_action_objects(aom[:, :1, :])[:, 0, :]  # [N, A]
        cls0 = acts0.argmax(-1).tolist()
        out["terrain_prior_mean_first_action"] = {
            "class_counts": {str(k): v for k, v in sorted(Counter(cls0).items())},
            "ao_mean_state_std_over_mean_abs": float(aom[:, 0, :].std(0).mean() / (aom[:, 0, :].abs().mean() + 1e-12)),
            "z_world_state_std_over_mean_abs": float(zw.std(0).mean() / (zw.abs().mean() + 1e-12)),
        }
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--regime", choices=["B", "C"], required=True)
    ap.add_argument("--recipe", default="B", help="B|BWF (regime B only)")
    ap.add_argument("--dose", type=int, required=True, help="warm steps (B) or warm episodes (C)")
    ap.add_argument("--seed", type=int, default=43)
    ap.add_argument("--clamp", action="store_true", help="SD-056 lever (b) rollout norm clamp ON (ratio 2.0)")
    ap.add_argument("--wake", type=int, default=300)
    ap.add_argument("--H", type=int, default=30)
    ap.add_argument("--n-starts", type=int, default=150)
    ap.add_argument("--max-selects", type=int, default=60)
    ap.add_argument("--n-states", type=int, default=30)
    ap.add_argument("--depths", type=str, default="1,2,3,5,10")
    ap.add_argument("--skip-m4", action="store_true")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    depths = [int(x) for x in a.depths.split(",")]
    t0 = time.time()
    seed_all(a.seed)
    if a.regime == "B":
        env, agent, cfg = build_B(a.seed, a.clamp)
        winfo = warm_B(agent, env, a.seed, a.dose, a.recipe == "BWF")
    else:
        env, agent, cfg, winfo = build_warm_C(a.seed, a.dose, a.clamp)
    winfo["t_warm_s"] = round(time.time() - t0, 1)
    print("WARM %s" % json.dumps(winfo), flush=True)
    rec, traj_log, harm = waking(agent, env, a.wake, a.seed)
    t_wake = time.time() - t0
    print("WAKE selects=%d steps=%d harm=%d t=%.0fs" % (len(rec.selects), len(traj_log), harm, t_wake), flush=True)
    m1, growth = m1_candidate_norms(rec, a.H)
    print("M1 growth/step(last10 median)=%s t0=%.3f t30=%s" % (
        growth, m1[0]["norm_p50"], m1.get(max(m1))["norm_p50"]), flush=True)
    m2 = m2_fidelity(agent, traj_log, a.H, a.n_starts, a.seed)
    if m2:
        print("M2 k_pers=%d k_chance=%d n=%d" % (m2["k_beats_persistence"], m2["k_beats_chance"], m2["n_starts"]), flush=True)
    m3 = m3_consumer(agent, rec, depths, a.max_selects, a.seed)
    print("M3 %s" % json.dumps({d: m3["by_depth"][d] for d in depths}), flush=True)
    m4 = None if a.skip_m4 else m4_proposal(agent, traj_log, a.n_states, depths, a.seed)
    if m4:
        print("M4 %s" % json.dumps({k: (v.get("maj_share_mean"), v.get("frac_states_with_modal_majority"))
                                    for k, v in m4.items() if isinstance(v, dict) and "maj_share_mean" in v}), flush=True)
    out = {"args": vars(a), "world_dim": int(agent.e2.config.world_dim), "self_dim": int(agent.e2.config.self_dim),
           "rollout_horizon_cfg": int(agent.e2.config.rollout_horizon),
           "hip_horizon_cfg": int(agent.hippocampal.config.horizon),
           "clamp": bool(agent.e2.config.e2_rollout_output_norm_clamp_enabled),
           "warm": winfo, "harm_ticks_wake": harm, "n_selects": len(rec.selects),
           "M1_by_step": m1, "M1_growth_per_step_late": growth, "M2": m2, "M3": m3, "M4": m4,
           "t_total_s": round(time.time() - t0, 1)}
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    with open(a.out, "w") as f:
        json.dump(out, f, indent=1, default=str)
    print("wrote %s t=%.0fs" % (a.out, time.time() - t0), flush=True)


if __name__ == "__main__":
    main()
