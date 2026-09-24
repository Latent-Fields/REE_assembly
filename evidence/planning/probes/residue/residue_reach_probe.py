"""Residue consumer-reach probe (bt0924-residue-reach, chip-20260924-residue-consumer-reach).

Question: at world_dim=32, does the GFLAG-0441 integrate() sampling fix
(use_dim_scaled_integrate_sampling) reach the NATIVE consumers of ResidueField?

Design (one seed per invocation, CPU, 2 threads):
  W1  waking phase (StepHarness, train_mode=False, EXQ-1072 config slice) with
      instrumentation on every ResidueField.evaluate / evaluate_trajectory call
      (query points + caller) and on every E3.select (candidate world_seqs,
      last_scores, last_selected_idx).
  NATIVE  one forced sleep cycle (force_sleep_cycle_at_eval_boundary) on the live
      agent -- confirms WRITEBACK fires integrate() natively, with what budget.
  ARMS  from a deepcopy of the PRE-cycle ResidueField (identical rbf + harm
      history + untrained neural head), train neural_field under matched RNG:
        NONE  untrained (pre-integration pedestal)
        OFF   integrate(train=True), unscaled sampling  (production w/ flags ON)
        ON    integrate(train=True), dim-scaled sampling (GFLAG-0441 fix)
        SCR   ON sampling geometry, targets permuted within each step (control)
        SCRL  ON targets, but trained at MIRRORED locations -h+noise (location control)
        ALT   samples drawn from the E3-queried z_world pool recorded in W1
              (detached), targets rbf(sample)  (the brief's step-4 alternative)
      at budgets B in {10 (one native cycle), 300 (saturated)}.
  W2  post-cycle waking phase on the native agent; every E3.select is scored
      counterfactually under each arm's field on the SAME candidate set:
      argmin flips vs OFF, residue-attributable spread vs total score spread.
  Q2  distances (in harm-kernel bandwidth units) from every consumer query point
      to the nearest harm location in integrate()'s own sampling pool, vs the
      sample-shell radii OFF/ON actually train on.

ASCII-only output. Expects a ree-v3 checkout at ./ree-v3-wt next to this file
(origin/main 00210b5 + the GFLAG-0441 patch in the record's run log). Usage:
  python residue_reach_probe.py --seed 42 --warm 600 [--harm-bw 0.15] --out out.json
Tabulate with: python summarize.py results/
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

WT = Path(__file__).resolve().parent / "ree-v3-wt"
sys.path.insert(0, str(WT))

from ree_core.agent import REEAgent  # noqa: E402
from ree_core.environment.causal_grid_world import CausalGridWorldV2  # noqa: E402
from ree_core.utils.config import REEConfig  # noqa: E402
from experiments._harness import StepHarness  # noqa: E402

torch.set_num_threads(2)

GRID_SIZE, NUM_HAZARDS, NUM_RESOURCES, MAX_EP = 8, 2, 3, 200


def seed_all(s):
    random.seed(s)
    np.random.seed(s)
    torch.manual_seed(s)


def build(seed, harm_bw):
    env = CausalGridWorldV2(size=GRID_SIZE, num_hazards=NUM_HAZARDS,
                            num_resources=NUM_RESOURCES, max_episode_steps=MAX_EP, seed=seed)
    kw = dict(body_obs_dim=env.body_obs_dim, world_obs_dim=env.world_obs_dim,
              action_dim=env.action_dim, use_sleep_aggregation_cluster=True,
              use_cross_module_consolidation=True, use_sleep_residue_integration=True,
              use_offline_integration_gradient_step=True, sleep_loop_episodes_K=10_000_000)
    cfg = REEConfig.from_dims(**kw)
    if harm_bw is not None:
        cfg.residue.harm_field_bandwidth = float(harm_bw)
    agent = REEAgent(cfg).to(torch.device("cpu"))
    agent.eval()
    return env, agent, cfg


class Recorder:
    def __init__(self, agent):
        self.agent = agent
        self.rf = agent.residue_field
        self.queries = []          # (caller, tensor [N, D])
        self.selects = []          # dicts
        self._cur = None
        self.active = True
        rf = self.rf
        orig_eval = rf.evaluate
        orig_traj = rf.evaluate_trajectory
        rec = self

        def ev(z):
            if rec.active:
                rec.queries.append((sys._getframe(1).f_code.co_name,
                                    z.detach().reshape(-1, z.shape[-1]).clone()))
            return orig_eval(z)

        def evt(ws):
            if rec.active:
                caller = sys._getframe(1).f_code.co_name
                rec.queries.append((caller, ws.detach().reshape(-1, ws.shape[-1]).clone()))
                if caller == "_score_trajectory":
                    rec._last_ws = ws.detach().clone()
                if caller == "compute_residue_cost" and rec._cur is not None:
                    rec._cur.append(ws.detach().clone())
            return orig_traj(ws)

        rf.evaluate = ev
        rf.evaluate_trajectory = evt
        e3 = agent.e3
        orig_sel = e3.select

        def sel(candidates, *a, **k):
            rec._cur = []
            out = orig_sel(candidates, *a, **k)
            if rec.active:
                rec.selects.append({
                    "n_cand": len(candidates),
                    "world_seqs": rec._cur,
                    "last_scores": None if e3.last_scores is None else e3.last_scores.detach().clone(),
                    "sel": e3.last_selected_idx,
                    "committed": e3._committed_trajectory is not None,
                })
            rec._cur = None
            return out

        e3.select = sel

        # CEM elite-stage consumer: HippocampalModule._score_trajectory inside
        # propose_trajectories. Record (world_seq passed to evaluate_trajectory,
        # returned score) per call; propose-level grouping.
        hip = agent.hippocampal
        self.cem = []              # list of propose calls: list of (ws, score)
        self._cem_cur = None
        self._last_ws = None
        orig_prop = hip.propose_trajectories
        orig_st = hip._score_trajectory

        def prop(*a, **k):
            rec._cem_cur = []
            out = orig_prop(*a, **k)
            if rec.active and rec._cem_cur:
                rec.cem.append(rec._cem_cur)
            rec._cem_cur = None
            return out

        def st(traj, *a, **k):
            rec._last_ws = None
            out = orig_st(traj, *a, **k)
            if rec.active and rec._cem_cur is not None and rec._last_ws is not None:
                sc = out[0] if isinstance(out, tuple) else out
                rec._cem_cur.append((rec._last_ws, float(torch.as_tensor(sc).detach().sum())))
            return out

        hip.propose_trajectories = prop
        hip._score_trajectory = st


def run_waking(agent, env, obs, steps, seed):
    harness = StepHarness(agent, env, train_mode=False, seed=seed)
    harm = 0
    actions = []
    for _ in range(steps):
        r = harness.step(obs)
        if r.harm_signal < 0:
            harm += 1
        actions.append(int(torch.as_tensor(r.action).argmax().item()))
        obs = r.next_obs_dict
        if r.done:
            _f, obs = env.reset()
            harness.reset()
    return obs, harm, actions


def train_custom(rf, steps, mode, pool=None, seed=0):
    """SCR / ALT arms: same optimiser, lr, batch size and step count as integrate()."""
    torch.manual_seed(seed)
    harm_locations = torch.stack(rf._harm_history[-100:])
    n = harm_locations.shape[0]
    bw = rf.effective_harm_bandwidth / (float(rf.config.world_dim) ** 0.5)
    opt = torch.optim.Adam(list(rf.neural_field.parameters()), lr=float(rf.config.integration_rate))
    losses = []
    for _ in range(steps):
        if mode == "SCR":
            pts = harm_locations + torch.randn_like(harm_locations) * bw
            with torch.no_grad():
                tg = rf.rbf_field(pts)
            tg = tg[torch.randperm(tg.shape[0])]
        elif mode == "SCRL":
            # location scramble: train at MIRRORED harm locations (-h + noise, same norm
            # statistics, wrong place) toward the true ON-shell targets.
            noise = torch.randn_like(harm_locations) * bw
            with torch.no_grad():
                tg = rf.rbf_field(harm_locations + noise)
            pts = -harm_locations + noise
        elif mode == "ALT":
            idx = torch.randint(0, pool.shape[0], (n,))
            pts = pool[idx]
            with torch.no_grad():
                tg = rf.rbf_field(pts)
        else:
            raise ValueError(mode)
        pred = rf.neural_field(pts).squeeze(-1)
        loss = F.mse_loss(pred, tg)
        opt.zero_grad(set_to_none=True)
        loss.backward()
        opt.step()
        losses.append(float(loss.item()))
    return {"loss_first": losses[0], "loss_last": losses[-1]}


def make_arms(rf_pre, pool, budgets, seed):
    arms = {"NONE": copy.deepcopy(rf_pre)}
    meta = {}
    for B in budgets:
        for name in ("OFF", "ON"):
            rf = copy.deepcopy(rf_pre)
            rf.config = copy.deepcopy(rf.config)
            rf.config.use_dim_scaled_integrate_sampling = (name == "ON")
            torch.manual_seed(seed + 1000)
            m = rf.integrate(num_steps=B, train=True)
            arms["%s_%d" % (name, B)] = rf
            meta["%s_%d" % (name, B)] = {k: float(v) for k, v in m.items()}
        for name in ("SCR", "SCRL", "ALT"):
            rf = copy.deepcopy(rf_pre)
            m = train_custom(rf, B, name, pool=pool, seed=seed + 1000)
            arms["%s_%d" % (name, B)] = rf
            meta["%s_%d" % (name, B)] = m
    # rbf-only reference (neural contribution removed): evaluate = rbf + 0.1*0
    return arms, meta


def nn_dist_bw(points, centers, bw, chunk=4096):
    out = []
    for i in range(0, points.shape[0], chunk):
        d = torch.cdist(points[i:i + chunk], centers)
        out.append(d.min(dim=1).values)
    return torch.cat(out) / float(bw)


def pct(x, qs=(0.0, 0.05, 0.5, 0.95, 1.0)):
    x = np.asarray(x, dtype=np.float64)
    if x.size == 0:
        return None
    return {("p%d" % int(q * 100)): float(np.quantile(x, q)) for q in qs}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--harm-bw", type=float, default=None)
    ap.add_argument("--w1", type=int, default=400)
    ap.add_argument("--w2", type=int, default=200)
    ap.add_argument("--warm", type=int, default=0, help="E1+E2 warmup steps (train_mode=True) before W1")
    ap.add_argument("--out", type=str, required=True)
    args = ap.parse_args()
    t0 = time.time()
    seed_all(args.seed)
    env, agent, cfg = build(args.seed, args.harm_bw)
    rf = agent.residue_field
    bw = float(rf.effective_harm_bandwidth)
    rho = float(cfg.e3.rho_residue)
    print("seed=%d world_dim=%d harm_bw=%s rho_residue=%.3f comm=%s" % (
        args.seed, cfg.residue.world_dim, str(args.harm_bw), rho,
        str(getattr(cfg.e3, "use_e3_channel_commensurability", False))), flush=True)
    warm_info = {"warm_steps": args.warm}
    if args.warm > 0:
        opt = torch.optim.Adam(agent.parameters(), lr=1e-3)
        harness = StepHarness(agent, env, train_mode=True, seed=args.seed)
        agent.train()
        _f, obs = env.reset()
        agent.reset()
        harness.reset()
        losses = []
        for i in range(args.warm):
            r = harness.step(obs)
            obs = r.next_obs_dict
            loss = agent.compute_prediction_loss() + agent.compute_e2_loss()
            if loss.requires_grad:
                opt.zero_grad()
                loss.backward()
                opt.step()
            losses.append(float(loss.detach().item()))
            if r.done:
                _f, obs = env.reset()
                agent.reset()
                harness.reset()
        agent.eval()
        warm_info.update({"loss_first50": float(np.mean(losses[:50])), "loss_last50": float(np.mean(losses[-50:]))})
        agent.reset()
        warm_info["harm_history_after_reset"] = len(rf._harm_history)
        warm_info["active_centers_after_reset"] = int(rf.rbf_field.active_mask.sum())
        print("WARM: %s t=%.0fs" % (json.dumps(warm_info), time.time() - t0), flush=True)
    rec = Recorder(agent)
    _f, obs = env.reset()
    obs, harm1, _acts = run_waking(agent, env, obs, args.w1, args.seed)
    n_harm_hist = len(rf._harm_history)
    print("W1 done: harm_ticks=%d harm_history=%d active_centers=%d selects=%d queries=%d t=%.0fs" % (
        harm1, n_harm_hist, int(rf.rbf_field.active_mask.sum()), len(rec.selects),
        len(rec.queries), time.time() - t0), flush=True)
    if n_harm_hist == 0:
        print("NO HARM -- stop")
        return

    # consumer query inventory (W1)
    by_caller = {}
    for c, q in rec.queries:
        by_caller.setdefault(c, []).append(q)
    q_inv = {c: int(sum(x.shape[0] for x in v)) for c, v in by_caller.items()}
    print("query points by caller: %s" % json.dumps(q_inv), flush=True)

    harm_pool = torch.stack(rf._harm_history[-100:]).reshape(-1, cfg.residue.world_dim)
    active = rf.rbf_field.centers[rf.rbf_field.active_mask].detach()
    e3_pool = torch.cat(by_caller.get("compute_residue_cost", [torch.zeros(0, cfg.residue.world_dim)]))

    # Q2: distances in bandwidth units
    q2 = {}
    for c, v in by_caller.items():
        pts = torch.cat(v)
        q2[c] = {"n": int(pts.shape[0]),
                 "to_harm_pool_bw": pct(nn_dist_bw(pts, harm_pool, bw).numpy()),
                 "to_active_center_bw": pct(nn_dist_bw(pts, active, bw).numpy())}
    # manifold scale
    allq = torch.cat([torch.cat(v) for v in by_caller.values()])
    sub = allq[torch.randperm(allq.shape[0])[:2000]]
    pw = torch.pdist(sub)
    q2["_manifold_pairwise_bw"] = pct((pw / bw).numpy())
    q2["_harm_pool_pairwise_bw"] = pct((torch.pdist(harm_pool) / bw).numpy()) if harm_pool.shape[0] > 1 else None
    # sample shells (what integrate trains on), measured with the same formula integrate uses
    g = torch.Generator().manual_seed(7)
    D = cfg.residue.world_dim
    for name, s in (("OFF", bw), ("ON", bw / D ** 0.5)):
        noise = torch.randn(5000, D, generator=g) * s
        q2["_sample_shell_%s_bw" % name] = pct((noise.norm(dim=1) / bw).numpy())
    # fraction of E3 queries inside the ON training shell band (<= 1.25 bw) and at/under 0.5 bw
    if e3_pool.shape[0]:
        d_e3 = nn_dist_bw(e3_pool, harm_pool, bw)
        q2["_e3_frac_le_0p5bw"] = float((d_e3 <= 0.5).float().mean())
        q2["_e3_frac_0p75_to_1p25bw"] = float(((d_e3 >= 0.75) & (d_e3 <= 1.25)).float().mean())
        q2["_e3_frac_le_1p25bw"] = float((d_e3 <= 1.25).float().mean())
    # per-horizon-step profile of E3 candidate world states: distance to harm pool (bw)
    # and z_world norm, vs the visited-state norm (terrain query = current z_world).
    steps_prof = {}
    for sdict in rec.selects:
        for w in sdict["world_seqs"]:
            w2 = w.reshape(-1, w.shape[-2], w.shape[-1]) if w.dim() == 3 else w.unsqueeze(0)
            for t in range(w2.shape[1]):
                pts = w2[:, t, :]
                dd = nn_dist_bw(pts, harm_pool, bw)
                e = steps_prof.setdefault(t, {"d": [], "n": []})
                e["d"].extend(dd.tolist())
                e["n"].extend(pts.norm(dim=-1).tolist())
    q2["_e3_by_step"] = {int(t): {"dist_bw_p50": float(np.median(v["d"])), "dist_bw_p95": float(np.quantile(v["d"], 0.95)),
                                  "znorm_p50": float(np.median(v["n"]))} for t, v in sorted(steps_prof.items())}
    cur = torch.cat(by_caller.get("_get_terrain_action_object_mean", [harm_pool]))
    q2["_visited_znorm_p50"] = float(cur.norm(dim=-1).median())
    print("Q2: %s" % json.dumps(q2), flush=True)

    # fork arms from PRE-cycle field
    rf_pre = copy.deepcopy(rf)
    # restore plain methods on the copy (instance overrides were deep-copied as closures over the live rf)
    for a in ("evaluate", "evaluate_trajectory"):
        if a in rf_pre.__dict__:
            del rf_pre.__dict__[a]
    arms, arm_meta = make_arms(rf_pre, e3_pool if e3_pool.shape[0] else harm_pool, (10, 300), args.seed)
    print("arms trained t=%.0fs" % (time.time() - t0), flush=True)

    # NATIVE cycle on live agent
    rec.active = False
    cyc = agent.force_sleep_cycle_at_eval_boundary() or {}
    native = {k: float(v) for k, v in cyc.items() if k.startswith("mech018_residue")}
    print("NATIVE cycle: %s" % json.dumps(native), flush=True)
    rec.active = True
    rec.queries = []
    rec.selects = []

    # W2 on native post-cycle agent
    seed_all(args.seed + 5)
    obs, harm2, _ = run_waking(agent, env, obs, args.w2, args.seed + 5)
    print("W2 done: harm_ticks=%d selects=%d t=%.0fs" % (harm2, len(rec.selects), time.time() - t0), flush=True)

    # evaluate each arm at W2 consumer queries
    by2 = {}
    for c, q in rec.queries:
        by2.setdefault(c, []).append(q)
    val = {}
    with torch.no_grad():
        for c, v in by2.items():
            pts = torch.cat(v)
            rbf = rf_pre.rbf_field(pts)
            ent = {"rbf_mean": float(rbf.mean()), "rbf_std": float(rbf.std()) if rbf.numel() > 1 else 0.0}
            for an, arf in arms.items():
                nv = arf.neural_field(pts).squeeze(-1) * 0.1
                ent["%s_neural01_mean" % an] = float(nv.mean())
                ent["%s_neural01_std" % an] = float(nv.std()) if nv.numel() > 1 else 0.0
                # correlation of the neural contribution with the rbf core across query points
                if nv.numel() > 2 and float(rbf.std()) > 0 and float(nv.std()) > 0:
                    ent["%s_corr_rbf" % an] = float(np.corrcoef(nv.numpy(), rbf.numpy())[0, 1])
            val[c] = ent
    print("VALUES at W2 queries: %s" % json.dumps(val), flush=True)

    # E3 counterfactual on shared candidates
    ref = "OFF_10"
    flips = {an: 0 for an in list(arms) + ["RBF_ONLY"]}
    usable = 0
    spread_total, spread_phi = [], {an: [] for an in list(arms) + ["RBF_ONLY"]}
    dphi_vs_ref = {an: [] for an in list(arms) + ["RBF_ONLY"]}
    n_mismatch = 0
    committed = 0
    e3_sel_core = {an: [] for an in list(arms) + ["RBF_ONLY"]}
    with torch.no_grad():
        for s in rec.selects:
            if s["last_scores"] is None or s["n_cand"] < 2:
                continue
            ws = s["world_seqs"]
            if len(ws) < s["n_cand"]:
                n_mismatch += 1
                continue
            ws = ws[: s["n_cand"]]
            usable += 1
            committed += int(bool(s["committed"]))
            sc = s["last_scores"].reshape(-1)
            if sc.numel() != s["n_cand"]:
                n_mismatch += 1
                continue
            spread_total.append(float(sc.max() - sc.min()))

            def phi_of(arf):
                if arf is None:
                    return torch.stack([rf_pre.rbf_field(w).sum(-1).mean() for w in ws])
                return torch.stack([(arf.rbf_field(w) + 0.1 * arf.neural_field(w).squeeze(-1)).sum(-1).mean() for w in ws])

            phi_ref = phi_of(arms[ref])
            phi_core = phi_of(None)
            base_arg = int(sc.argmin())
            for an in list(arms) + ["RBF_ONLY"]:
                phi_a = phi_of(None if an == "RBF_ONLY" else arms[an])
                alt = sc + rho * (phi_a - phi_ref)
                if int(alt.argmin()) != base_arg:
                    flips[an] += 1
                e3_sel_core[an].append(float(phi_core[int(alt.argmin())] - phi_core.mean()))
                spread_phi[an].append(float(rho * (phi_a.max() - phi_a.min())))
                dphi_vs_ref[an].append(float((rho * (phi_a - phi_ref)).abs().max()))
    e3cf = {"usable_selects": usable, "mismatch": n_mismatch, "committed_frac": committed / max(1, usable),
            "score_spread_total": pct(spread_total),
            "argmin_flips_vs_OFF_10": flips,
            "selected_minus_pool_rbf_core_phi_mean": {k: (float(np.mean(v)) if v else None) for k, v in e3_sel_core.items()},
            "rho_phi_spread": {k: pct(v) for k, v in spread_phi.items()},
            "max_abs_rho_dphi_vs_OFF_10": {k: pct(v) for k, v in dphi_vs_ref.items()}}
    print("E3 CF: %s" % json.dumps(e3cf), flush=True)

    # CEM elite-set counterfactual: per propose call, chunk scores into CEM
    # iterations of num_candidates; elite = num_elite lowest (module's own rule).
    hc = agent.hippocampal.config
    n_c = int(hc.num_candidates)
    n_el = min(n_c, max(2, max(1, int(n_c * hc.elite_fraction))))
    cem_jacc = {an: [] for an in list(arms) + ["RBF_ONLY"]}
    cem_elite_rbf = {an: [] for an in list(arms) + ["RBF_ONLY"]}
    cem_iters = 0
    with torch.no_grad():
        for call in rec.cem:
            for i0 in range(0, len(call) - n_c + 1, n_c):
                chunk = call[i0:i0 + n_c]
                wss = [c[0] for c in chunk]
                sc = torch.tensor([c[1] for c in chunk])
                cem_iters += 1

                def terr(arf):
                    if arf is None:
                        return torch.tensor([float(rf_pre.rbf_field(w).sum()) for w in wss])
                    return torch.tensor([float((arf.rbf_field(w) + 0.1 * arf.neural_field(w).squeeze(-1)).sum()) for w in wss])

                t_ref = terr(arms[ref])
                t_core = terr(None)
                base = set(torch.argsort(sc)[:n_el].tolist())
                for an in list(arms) + ["RBF_ONLY"]:
                    alt = sc + (terr(None if an == "RBF_ONLY" else arms[an]) - t_ref)
                    e = set(torch.argsort(alt)[:n_el].tolist())
                    cem_jacc[an].append(len(base & e) / float(len(base | e)))
                    cem_elite_rbf[an].append(float(t_core[list(e)].mean() - t_core.mean()))
    cemcf = {"cem_iterations": cem_iters, "num_candidates": n_c, "num_elite": n_el,
             "mean_elite_jaccard_vs_OFF_10": {k: (float(np.mean(v)) if v else None) for k, v in cem_jacc.items()},
             "elite_minus_pool_rbf_core_terrain_mean": {k: (float(np.mean(v)) if v else None) for k, v in cem_elite_rbf.items()},
             "frac_iter_elite_changed_vs_OFF_10": {k: (float(np.mean([x < 1.0 for x in v])) if v else None) for k, v in cem_jacc.items()}}
    print("CEM CF: %s" % json.dumps(cemcf), flush=True)

    out = {"seed": args.seed, "cem_cf": cemcf, "harm_bw": args.harm_bw, "effective_bw": bw, "rho_residue": rho,
           "world_dim": cfg.residue.world_dim, "w1": args.w1, "w2": args.w2,
           "warm": warm_info, "harm_ticks_w1": harm1, "harm_history": n_harm_hist, "harm_ticks_w2": harm2,
           "query_inventory_w1": q_inv, "q2": q2, "arm_meta": arm_meta, "native_cycle": native,
           "values_w2": val, "e3_cf": e3cf, "wall_s": time.time() - t0,
           "worktree_head": "00210b5 + residue_gflag0441_full.patch"}
    Path(args.out).write_text(json.dumps(out, indent=1))
    print("wrote %s wall=%.0fs" % (args.out, time.time() - t0), flush=True)


if __name__ == "__main__":
    main()
