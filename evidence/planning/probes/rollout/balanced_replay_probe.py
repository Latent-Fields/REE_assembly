"""ADDENDUM 2 probe: does class-balanced replay (R6) make the agent's OWN E2 world head
action-informative, does that make E3's pick track true consequences (D2), and does
behaviour diversify in a short closed loop (D3-lite)?

bt0924-rollout-c (Worker D, orchestrate-20260924-breakthrough).

Per seed (regime B: CausalGridWorldV2 8x8, world_dim 32):
  0. build_B; SD-070 z_world encoder warmup (run_zworld_p0, 20 eps x 50 steps,
     preservation 1000 = V3-EXQ-1093's setting, RandomPolicy).
  1. REPLAY: waking run (StepHarness, native select, untrained world head) -> the
     agent's own (z_t, executed class, z_{t+1}) transitions.
  2. ARMS, all from the SAME initial world head, 3000 updates, batch 32, Adam 3e-4,
     clip 1.0, single-step MSE, sampling WITH replacement by per-transition weight:
       A NATIVE    uniform weights (the replay as-is)
       B BALANCED  w_i = 1 / n(class(i))  (each class equally likely)
       C CONTROL   B's weight vector randomly permuted across transitions (same weight
                   distribution / effective sample concentration, uncorrelated with action)
  3. PROBE STATES: waking run with head A live; every PROBE_EVERY steps, at the StepHarness
     on_action hook (after select, before env.step), for each action class c: clone the env
     (copy.deepcopy), step c, and encode the true next z_world with the agent's own encoder
     side-effect-free (latent_stack.encode with sense()'s arguments; validated against the
     next tick's sensed z_world for the executed class). Also store a native CEM pool
     (propose_trajectories, torch RNG saved/restored).
  M1 per arm: fidelity k + action discrimination on held-out uniform-random-action episodes;
     on the native pools re-rolled with the arm's head: share of E3 J cross-candidate
     variance from steps > 5, truncation (d=1,3,5) argmin flip rate, deep-step shuffle.
  M2 per arm (D2 choice quality): scaffold pool = one candidate per first-action class c
     (native pool[0]'s action sequence with step 0 replaced by one-hot c), rolled out with
     the arm's head, scored by E3.score_trajectory (FULL and depth-1). TRUE value of c =
     E3.score_trajectory on the 1-step trajectory [z0, z_true(c)]. Report P(E3 pick in
     true-best set) vs chance = mean(|true-best set| / A), and Spearman(J_pred, J_true).
  M3 per arm (closed loop, cheap): fresh env (same seed), arm head live, WAKE steps;
     executed-action entropy / majority share, and P3 proposal majority-class invariance.
     Arms run sequentially on ONE agent (it cannot be deep-copied), order A, B, C; residue
     and other agent state carry over between arms (stated confound).
ASCII-only output.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
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
sys.path.insert(0, str(HERE))

from experiments._harness import StepHarness, StepHooks  # noqa: E402
from ree_core.predictors.e2_fast import Trajectory  # noqa: E402
import rollout_fidelity_probe as R  # noqa: E402
import encoding_vs_objective_probe as E  # noqa: E402

torch.set_num_threads(2)


def head_params(agent):
    return list(agent.e2.world_transition.parameters()) + list(agent.e2.world_action_encoder.parameters())


def get_head(agent):
    return {"t": copy.deepcopy(agent.e2.world_transition.state_dict()),
            "a": copy.deepcopy(agent.e2.world_action_encoder.state_dict())}


def set_head(agent, h):
    agent.e2.world_transition.load_state_dict(h["t"])
    agent.e2.world_action_encoder.load_state_dict(h["a"])


def onehot(c, A):
    v = torch.zeros(1, A)
    v[0, c] = 1.0
    return v


@torch.no_grad()
def encode_next(agent, obs, prev_latent, prev_action):
    """sense()'s encoder call, side-effect-free (agent.py sense -> latent_stack.encode)."""
    ob = torch.as_tensor(obs["body_state"]).float().reshape(1, -1)
    ow = torch.as_tensor(obs["world_state"]).float().reshape(1, -1)
    enc = torch.cat([agent.body_obs_encoder(ob), agent.world_obs_encoder(ow)], dim=-1)
    vol = agent.e3.volatility_estimate if agent.config.latent.volatility_signal_dim > 0 else None
    harm = obs.get("harm_obs")
    if agent.lpb_router is not None and harm is not None:
        harm = agent.lpb_router.mask_external_harm_obs(harm)
    anchor = agent._e1_predicted_next_z_self if getattr(agent.config.latent, "use_self_recurrence", False) else None
    lat = agent.latent_stack.encode(enc, prev_latent, prev_action=prev_action, harm_obs=harm,
                                    harm_obs_a=obs.get("harm_obs_a"), harm_history=obs.get("harm_history"),
                                    volatility_signal=vol, self_e1_anchor=anchor)
    return lat.z_world.detach().clone()


def collect_replay(agent, env, steps, seed):
    h = StepHarness(agent, env, train_mode=False, seed=seed)
    _f, obs = env.reset(); agent.reset(); h.reset()
    trans, prev = [], None
    for _ in range(steps):
        r = h.step(obs)
        z = r.latent.z_world.detach().clone()
        if prev is not None:
            trans.append((prev[0], prev[1], z))
        prev = (z, int(r.action.detach().reshape(-1).argmax()))
        obs = r.next_obs_dict
        if r.done:
            _f, obs = env.reset(); agent.reset(); h.reset(); prev = None
    return trans


def train_arm(agent, init, trans, A, weights, steps, seed):
    set_head(agent, init)
    torch.manual_seed(seed)
    x0 = torch.cat([t[0] for t in trans]); x1 = torch.cat([t[2] for t in trans])
    oh = F.one_hot(torch.tensor([t[1] for t in trans]), A).float()
    w = torch.as_tensor(weights, dtype=torch.float64)
    params = head_params(agent)
    opt = torch.optim.Adam(params, lr=3e-4)
    losses = []
    for _ in range(steps):
        idx = torch.multinomial(w, 32, replacement=True)
        loss = F.mse_loss(agent.e2.world_forward(x0[idx], oh[idx]), x1[idx])
        opt.zero_grad(); loss.backward(); torch.nn.utils.clip_grad_norm_(params, 1.0); opt.step()
        losses.append(float(loss.detach()))
    return get_head(agent), {"loss_last200": float(np.mean(losses[-200:])),
                             "identity_mse": float(F.mse_loss(x0, x1))}


def collect_probe_states(agent, env, steps, every, A, seed):
    states = []
    pend = {}

    def on_action(agent, latent, action, obs_dict, ticks, step, **k):
        if step % every != 0:
            return
        lat_s = agent._current_latent
        z0, s0 = latent.z_world.detach().clone(), latent.z_self.detach().clone()
        zt = []
        for c in range(A):
            e = copy.deepcopy(env)
            o2 = e.step(c)[4]
            zt.append(encode_next(agent, o2, lat_s, onehot(c, A)))
        rs = torch.get_rng_state()
        with torch.no_grad():
            pool = agent.hippocampal.propose_trajectories(z0, z_self=s0)
        torch.set_rng_state(rs)
        ex = int(action.detach().reshape(-1).argmax())
        e = copy.deepcopy(env)
        z_exact = encode_next(agent, e.step(action)[4], lat_s, action.detach().reshape(1, -1).float())
        pend["i"] = len(states)
        states.append({"z0": z0, "s0": s0, "z_true": zt, "pool_actions": [p.actions.detach().clone() for p in pool],
                       "executed": ex, "z_exact_exec": z_exact, "exec_is_onehot": bool(float(action.detach().reshape(-1).max()) > 0.99)})

    h = StepHarness(agent, env, train_mode=False, seed=seed, hooks=StepHooks(on_action=on_action))
    _f, obs = env.reset(); agent.reset(); h.reset()
    for _ in range(steps):
        pend.pop("i", None)
        r = h.step(obs)
        i = pend.get("i")
        obs = r.next_obs_dict
        # validation: the NEXT tick's sensed z_world vs encode_next for the executed class
        if i is not None and not r.done:
            r2 = h.step(obs)
            d = float((r2.latent.z_world - states[i]["z_true"][states[i]["executed"]]).abs().max())
            states[i]["validation_maxabs"] = d
            states[i]["validation_exact_action_maxabs"] = float((r2.latent.z_world - states[i]["z_exact_exec"]).abs().max())
            obs = r2.next_obs_dict
            if r2.done:
                _f, obs = env.reset(); agent.reset(); h.reset()
            continue
        if r.done:
            _f, obs = env.reset(); agent.reset(); h.reset()
    return states


def spearman(a, b):
    ra, rb = np.argsort(np.argsort(a)), np.argsort(np.argsort(b))
    if np.std(ra) == 0 or np.std(rb) == 0:
        return None
    return float(np.corrcoef(ra, rb)[0, 1])


@torch.no_grad()
def score(agent, trajs, depth=None):
    e3 = agent.e3
    prev = e3._score_depth_limit
    e3._score_depth_limit = depth
    try:
        return np.asarray([float(e3.score_trajectory(t).mean()) for t in trajs])
    finally:
        e3._score_depth_limit = prev


@torch.no_grad()
def m1_e3_structure(agent, states, seed):
    g = np.random.default_rng(seed)
    flips = {1: [], 3: [], 5: []}; shuf = []; deep = []
    for st in states:
        acts = st["pool_actions"]
        if len(acts) < 2:
            continue
        trajs = [agent.e2.rollout_with_world(st["s0"], st["z0"], a, compute_action_objects=False) for a in acts]
        full = score(agent, trajs)
        af = int(np.argmin(full))
        for d in flips:
            tr = score(agent, trajs, d + 1)
            flips[d].append(int(np.argmin(tr)) != af)
            if d == 5:
                vf = full.var()
                deep.append(float((full - tr).var() / vf) if vf > 0 else None)
        C = len(trajs); perm = np.roll(np.arange(C), 1 + int(g.integers(0, C - 1)))
        sh = []
        for i in range(C):
            t2 = copy.copy(trajs[i]); ws = list(trajs[i].world_states)
            for j in range(4, len(ws)):
                ws[j] = trajs[perm[i]].world_states[j]
            t2.world_states = ws; sh.append(t2)
        shuf.append(int(np.argmin(score(agent, sh))) != af)
    dd = [x for x in deep if x is not None]
    return {"n_states": len(shuf), "trunc_flip_rate": {d: float(np.mean(v)) for d, v in flips.items()},
            "shuffle_steps_gt3_flip_rate": float(np.mean(shuf)),
            "J_var_share_steps_gt5_p50": float(np.median(dd)) if dd else None}


@torch.no_grad()
def m2_choice(agent, states, A):
    hits_full, hits_d1, chance, rho_full, rho_d1, picks_full, best_cls = [], [], [], [], [], [], []
    for st in states:
        base = st["pool_actions"][0].clone()
        trajs, true_trajs = [], []
        for c in range(A):
            a = base.clone(); a[:, 0, :] = 0.0; a[:, 0, c] = 1.0
            trajs.append(agent.e2.rollout_with_world(st["s0"], st["z0"], a, compute_action_objects=False))
            true_trajs.append(Trajectory(states=[st["s0"], st["s0"]], actions=onehot(c, A).unsqueeze(1),
                                         world_states=[st["z0"], st["z_true"][c]]))
        jt = score(agent, true_trajs)
        best = set(np.nonzero(jt <= jt.min() + 1e-9 * max(1.0, abs(jt.min())))[0].tolist())
        jf = score(agent, trajs); j1 = score(agent, trajs, 2)
        pf, p1 = int(np.argmin(jf)), int(np.argmin(j1))
        hits_full.append(pf in best); hits_d1.append(p1 in best); chance.append(len(best) / A)
        rho_full.append(spearman(jf, jt)); rho_d1.append(spearman(j1, jt))
        picks_full.append(pf); best_cls.extend(sorted(best))

    def m(v):
        v = [x for x in v if x is not None]
        return float(np.mean(v)) if v else None
    return {"n_states": len(hits_full), "pick_is_true_best_FULL": m(hits_full), "pick_is_true_best_DEPTH1": m(hits_d1),
            "chance": m(chance), "spearman_Jpred_Jtrue_FULL": m(rho_full), "spearman_Jpred_Jtrue_DEPTH1": m(rho_d1),
            "FULL_pick_counts": {str(k): v for k, v in sorted(Counter(picks_full).items())},
            "true_best_class_counts": {str(k): v for k, v in sorted(Counter(best_cls).items())}}


def closed_loop(agent, seed, steps, A):
    env = R.build_B(seed, False)[0]
    rec, log, harm = R.waking(agent, env, steps, seed)
    acts = [int(t[3].argmax()) for t in log]
    cc = Counter(acts)
    p = np.asarray(list(cc.values()), dtype=float) / len(acts)
    m4 = R.m4_proposal(agent, log, 20, [], seed)
    nat = m4["native"]
    return {"exec_action_counts": {str(k): v for k, v in sorted(cc.items())},
            "exec_action_entropy_nats": float(-(p * np.log(p)).sum()), "exec_majority_share": max(cc.values()) / len(acts),
            "harm_ticks": harm, "P3_maj_share": nat["maj_share_mean"], "P3_modal_majority_frac": nat["frac_states_with_modal_majority"],
            "P3_majority_counts": nat["majority_class_counts_across_states"],
            "terrain_prior_first_action": m4["terrain_prior_mean_first_action"]["class_counts"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=43)
    ap.add_argument("--replay", type=int, default=1500)
    ap.add_argument("--updates", type=int, default=3000)
    ap.add_argument("--probe-steps", type=int, default=200)
    ap.add_argument("--probe-every", type=int, default=5)
    ap.add_argument("--wake", type=int, default=300)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    t0 = time.time()
    R.seed_all(a.seed)
    env, agent, cfg = R.build_B(a.seed, False)
    A = env.action_dim
    from experiments._lib.zworld_p0_warmup import run_zworld_p0
    from experiments._lib.capability_eval import RandomPolicy
    from ree_core.latent.zworld_p0 import ZWorldP0Config
    p0 = run_zworld_p0(agent, R.build_B(a.seed, False)[0], seed=a.seed, episodes=20, steps_per_episode=50,
                       policy=RandomPolicy(a.seed), label="bt0924c", dry_run=False,
                       config=ZWorldP0Config(preservation_weight=1000.0))
    agent.eval()
    init = get_head(agent)
    trans = collect_replay(agent, env, a.replay, a.seed)
    cls = [t[1] for t in trans]; cnt = Counter(cls)
    print("REPLAY n=%d class_counts=%s p0_ran=%s t=%.0fs" % (len(trans), dict(sorted(cnt.items())), p0.get("p0a_ran"), time.time() - t0), flush=True)
    # D EXPLORE (positive control, added after A/B/C): same count of transitions, same
    # updates, but collected under a UNIFORM-RANDOM action policy with the agent's own
    # encoder (agent.sense) -- action COVERAGE rather than reweighting of the own replay.
    rnd = E.collect(R.build_B(a.seed + 11, False)[0], agent, len(trans) + 200, a.seed + 3)
    trans_d = []
    for e in rnd:
        for t in range(e["a"].shape[0] - 1):
            trans_d.append((e["z"][t:t + 1], int(e["a"][t]), e["z"][t + 1:t + 2]))
    trans_d = trans_d[:len(trans)]
    wB = np.asarray([1.0 / cnt[c] for c in cls])
    rng = np.random.default_rng(a.seed + 5)
    wC = wB[rng.permutation(len(wB))]
    arms = {}
    for name, w, tr in (("A_native", np.ones(len(cls)), trans), ("B_balanced", wB, trans), ("C_shuffled", wC, trans),
                        ("D_explore", np.ones(len(trans_d)), trans_d)):
        head, info = train_arm(agent, init, tr, A, w, a.updates, a.seed)
        cl_ = [t[1] for t in tr]
        info["effective_class_share"] = {str(c): float(sum(w[i] for i in range(len(cl_)) if cl_[i] == c) / w.sum()) for c in sorted(set(cl_))}
        info["ess"] = float(w.sum() ** 2 / (w ** 2).sum())
        arms[name] = {"head": head, "train": info}
        print("TRAIN %s %s" % (name, json.dumps(info)), flush=True)
    # probe states under head A
    set_head(agent, arms["A_native"]["head"])
    states = collect_probe_states(agent, env, a.probe_steps, a.probe_every, A, a.seed)
    vals = [s.get("validation_maxabs") for s in states if s.get("validation_maxabs") is not None]
    vals2 = [s.get("validation_exact_action_maxabs") for s in states if s.get("validation_exact_action_maxabs") is not None]
    print("PROBE states=%d val_onehot p50=%s max=%s val_exact_action max=%s exec_onehot_frac=%.2f t=%.0fs" % (
        len(states), np.median(vals) if vals else None, max(vals) if vals else None, max(vals2) if vals2 else None,
        float(np.mean([s["exec_is_onehot"] for s in states])) if states else -1, time.time() - t0), flush=True)
    # held-out random-action data for fidelity (sense mutates agent state -> after probe states)
    te = E.collect(R.build_B(a.seed + 7, False)[0], agent, 2500, a.seed + 2)
    out = {"args": vars(a), "p0": {k: v for k, v in p0.items() if isinstance(v, (int, float, str, bool))},
           "replay_n": len(trans), "replay_class_counts": {str(k): v for k, v in sorted(cnt.items())},
           "probe_states": len(states), "validation_maxabs": vals, "arms": {}}
    for name, arm in arms.items():
        set_head(agent, arm["head"])
        fid = E.evaluate(agent.e2, te, "z", A, 10, a.seed)
        m1 = m1_e3_structure(agent, states, a.seed)
        m2 = m2_choice(agent, states, A)
        out["arms"][name] = {"train": arm["train"], "fidelity": {"k": fid["k_beats_persistence"], "action_disc": fid["action_disc"],
                                                                 "err_over_pers_h1": fid["by_h"][1]["err_over_pers"],
                                                                 "err_over_pers_h5": fid["by_h"][5]["err_over_pers"],
                                                                 "cos_h1": fid["by_h"][1]["cos_p50"]},
                             "M1_e3": m1, "M2_choice": m2}
        print("M12 %s k=%s disc1=%.2f | %s | %s t=%.0fs" % (name, fid["k_beats_persistence"], fid["action_disc"][1]["executed_closest"],
                                                         json.dumps(m1), json.dumps(m2), time.time() - t0), flush=True)
    for name in ("A_native", "B_balanced", "C_shuffled", "D_explore"):
        set_head(agent, arms[name]["head"])
        cl = closed_loop(agent, a.seed, a.wake, A)
        out["arms"][name]["M3_closed_loop"] = cl
        print("M3 %s %s t=%.0fs" % (name, json.dumps(cl), time.time() - t0), flush=True)
    out["t_total_s"] = round(time.time() - t0, 1)
    json.dump(out, open(a.out, "w"), indent=1, default=str)
    print("wrote %s t=%.0fs" % (a.out, time.time() - t0), flush=True)


if __name__ == "__main__":
    main()
