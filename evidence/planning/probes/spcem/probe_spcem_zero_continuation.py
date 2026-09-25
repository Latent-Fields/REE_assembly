"""Probe (bt0925-spcem): do default-ON SP-CEM tokens lose E3 on their ZERO continuations?

Context. Worker C (monostrategy_type_a_vs_b_discrimination_20260924.md sec 2.3)
found in the V3-EXQ-1061 intact regime that the SP-CEM floor token "never beats the
best of ~31" majority candidates (0/40 states, 3/3 seeds) and read it as an
order-statistic effect of a 31:1 pool imbalance. Code-read (D0): the token is built
by _build_action_class_scaffold_candidates = one-hot at step 0 then EXACT ZEROS for
steps 1..H-1, rolled through E2, and E3 scores the full horizon.

This probe re-creates Worker C's cell (1061 intact arm, production ao_std floor 0.2,
20 warm eps x 100 steps, 40 probe states along a random walk) and at every state:
  D1  records the token's actions (zeros after step 0?) and its E3 rank.
  D2  swaps ONLY the token's construction, holding the rest of the pool fixed, and
      re-runs bare e3.select on the live E3 (deepcopy is impossible: non-leaf
      tensors in its state). Cross-call state drift is checked: the control arm
      is scored FIRST and an identical rebuilt control LAST; equal scores = no drift.
        Arms are listed (and defined) at ARMS below: a 2x2 HEAD {one-hot, on-
        manifold permuted} x TAIL {zeros, best-majority tail} on the token class,
        plus hold / sampled-tail, plus same-CLASS construction controls on the
        majority class (if a majority-class one-hot token also loses, the loss
        is the construction, not the class).
Metrics per arm: token rank (0 = best, lower score = better), token beats majority
BEST, token beats majority MEAN, E3 argmin is token, E3 selected_index is token.
Read-only on substrate. Imports 1061's builders from ./ree-v3-wt (a detached
worktree next to this file or passed via REE_V3_WT). ASCII-only output.
Usage: python3 probe_spcem_zero_continuation.py <seed>
"""
import json
import math
import os
import sys
import time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
WT = os.environ.get("REE_V3_WT", os.path.join(HERE, "ree-v3-wt"))
sys.path.insert(0, WT)
sys.path.insert(0, os.path.join(WT, "experiments"))

import torch  # noqa: E402

torch.set_num_threads(2)

import v3_exq_1061_mech131_anticipatory_residue_lesion as X  # noqa: E402

# 2x2 on the class-c token: HEAD {oh = exact one-hot(c), pm = the E3-best majority
# candidate's own step-0 vector with its majority and c entries SWAPPED (argmax
# becomes c, magnitude stays on the decoder's manifold)} x TAIL {z = zeros,
# bt = the E3-best majority candidate's own steps 1..H-1}. oh_z is the native token.
# Plus: hold (one-hot(c) every step), sampled (oh + a random real candidate's tail),
# and same-CLASS construction controls on the majority class:
# maj_oh_z (one-hot(maj)+zeros), maj_oh_bt (best-majority candidate with only its
# step 0 replaced by one-hot(maj)).
ARMS = ["control", "hold", "sampled", "oh_bt", "pm_z", "pm_bt", "maj_oh_z", "maj_oh_bt"]


def first_class(t):
    return int(torch.argmax(t.actions[0, 0, :]).item())


def src(t):
    return (t.metadata or {}).get("source")


def main(seed=11, warm_eps=20, steps=100, n_states=40):
    t0 = time.time()
    agent, env, cfg = X.build_agent(True, True, seed, X.PRODUCTION_FLOOR)
    hc = agent.hippocampal.config
    warm = X.warmup_train(agent, env, seed, warm_eps, steps)
    obs_dict = warm.pop("final_obs")
    t_warm = time.time() - t0
    H = int(hc.horizon)
    A = int(hc.action_dim)
    e2 = agent.hippocampal.e2

    def roll(z_self, z_world, actions):
        with torch.no_grad():
            return e2.rollout_with_world(z_self, z_world, actions,
                                         compute_action_objects=True,
                                         action_bias=None)

    rows = []
    for s in range(n_states):
        body, world = X._obs(obs_dict)
        latent = agent.sense(body, world)
        theta_z = agent.theta_buffer.summary()
        z_self = latent.z_self.detach()
        torch.manual_seed(seed * 1000 + s)
        with torch.no_grad():
            pool = agent.hippocampal.propose_trajectories(theta_z, z_self=z_self)
        row = {"probe_index": s, "n_candidates": len(pool)}
        tok_idx = [i for i, t in enumerate(pool)
                   if src(t) == "support_preserving_cem_injected"]
        classes = [first_class(t) for t in pool]
        cc = Counter(classes)
        row["pool_class_counts"] = dict(sorted(cc.items()))
        row["n_tokens"] = len(tok_idx)
        if len(tok_idx) != 1:
            rows.append(row)
            _f, _h, done, _i, obs_dict = env.step(int(torch.randint(0, A, (1,)).item()))
            if done:
                _f, obs_dict = env.reset()
            continue
        ti = tok_idx[0]
        tok = pool[ti]
        c = first_class(tok)
        maj = cc.most_common(1)[0][0]
        acts = tok.actions.detach()
        real_idx = [i for i in range(len(pool)) if i != ti]
        real_acts = torch.stack([pool[i].actions.detach()[0] for i in real_idx])  # [n,H,A]
        row.update({
            "token_class": c, "majority_class": maj,
            "token_step0": [round(float(x), 4) for x in acts[0, 0].tolist()],
            "token_tail_abs_max": float(acts[0, 1:].abs().max().item()),
            "real_step0_abs_mean": float(real_acts[:, 0].abs().mean().item()),
            "real_tail_abs_mean": float(real_acts[:, 1:].abs().mean().item()),
            "real_tail_norm_mean": float(real_acts[:, 1:].norm(dim=-1).mean().item()),
            "real_step0_max_mean": float(real_acts[:, 0].max(dim=-1).values.mean().item()),
        })
        # Build variants for the SAME slot ti.
        # Need the z_world the pool was rolled from: theta_z (bare path, as Worker C).
        g = torch.Generator().manual_seed(seed * 7919 + s)
        rand_real = real_idx[int(torch.randint(0, len(real_idx), (1,), generator=g).item())]
        # E3-best majority candidate (on control pool) needed for maj_best_swap.
        e3c = agent.e3  # deepcopy fails (non-leaf tensors in E3 state); drift checked via control_rebuilt
        with torch.no_grad():
            torch.manual_seed(seed * 100003 + s)
            sel_c = e3c.select(pool, temperature=1.0)
        sc_c = [float(x) for x in sel_c.scores.detach().reshape(-1).tolist()]
        maj_real = [i for i in real_idx if classes[i] == maj]
        best_maj = min(maj_real, key=lambda i: sc_c[i])

        def onehot_at0(base_tail, cls):
            a = torch.zeros(1, H, A)
            if base_tail is not None:
                a[:, 1:, :] = base_tail
            a[:, 0, cls] = 1.0
            return a

        variants = {}
        variants["control"] = tok
        hold = torch.zeros(1, H, A)
        hold[:, :, c] = 1.0
        variants["hold"] = roll(z_self, theta_z, hold)
        variants["sampled"] = roll(z_self, theta_z,
                                   onehot_at0(pool[rand_real].actions.detach()[:, 1:, :], c))
        bm = pool[best_maj].actions.detach().clone()          # [1,H,A]
        bt = bm[:, 1:, :]
        pm_head = bm[:, 0, :].clone()
        pm_head[:, maj], pm_head[:, c] = bm[:, 0, c].clone(), bm[:, 0, maj].clone()
        row["pm_head_argmax"] = int(torch.argmax(pm_head[0]).item())
        variants["oh_bt"] = roll(z_self, theta_z, onehot_at0(bt, c))
        a = torch.zeros(1, H, A); a[:, 0, :] = pm_head
        variants["pm_z"] = roll(z_self, theta_z, a)
        a = bm.clone(); a[:, 0, :] = pm_head
        variants["pm_bt"] = roll(z_self, theta_z, a)
        variants["maj_oh_z"] = roll(z_self, theta_z, onehot_at0(None, maj))
        variants["maj_oh_bt"] = roll(z_self, theta_z, onehot_at0(bt, maj))
        # Reference: best-majority candidate re-rolled here (same z as variants).
        ref_bm = roll(z_self, theta_z, bm)
        row["ref_bm_reality_cost"] = float(agent.e3.compute_reality_cost(ref_bm).item())
        # Sanity: control rebuilt through roll() must reproduce the native token score.
        variants_check = roll(z_self, theta_z, onehot_at0(None, c))

        arm_out = {}
        for arm in ARMS + ["control_rebuilt"]:
            v = variants_check if arm == "control_rebuilt" else variants[arm]
            p2 = list(pool)
            p2[ti] = v
            e3a = agent.e3
            with torch.no_grad():
                torch.manual_seed(seed * 100003 + s)
                sel = e3a.select(p2, temperature=1.0)
            sc = [float(x) for x in sel.scores.detach().reshape(-1).tolist()]
            tsc = sc[ti]
            maj_sc = [sc[i] for i in maj_real]
            order = sorted(range(len(sc)), key=lambda i: sc[i])
            arm_out[arm] = {
                "token_score": tsc,
                "token_rank": order.index(ti),
                "beats_majority_best": bool(tsc < min(maj_sc)),
                "beats_majority_mean": bool(tsc < sum(maj_sc) / len(maj_sc)),
                "gap_to_majority_best": tsc - min(maj_sc),
                "argmin_is_token": bool(order[0] == ti),
                "selected_is_token": bool(int(sel.selected_index) == ti),
                "selected_class": first_class(p2[int(sel.selected_index)]),
                "score_std": float(torch.tensor(sc).std().item()),
                "token_reality_cost": float(agent.e3.compute_reality_cost(v).item()),
            }
        row["arms"] = arm_out
        rows.append(row)
        _f, _h, done, _i, obs_dict = env.step(int(torch.randint(0, A, (1,)).item()))
        if done:
            _f, obs_dict = env.reset()

    ok = [r for r in rows if "arms" in r]
    summ = {"seed": seed, "warm_eps": warm_eps, "steps": steps, "n_states": n_states,
            "n_states_with_one_token": len(ok),
            "token_count_hist": dict(Counter(r["n_tokens"] for r in rows)),
            "horizon": H, "action_dim": A, "num_candidates": int(hc.num_candidates),
            "world_dim": X.WORLD_DIM, "self_dim": X.SELF_DIM, "grid": X.GRID_SIZE,
            "ao_std_floor": X.PRODUCTION_FLOOR,
            "use_support_preserving_cem": bool(hc.use_support_preserving_cem),
            "warm_seconds": round(t_warm, 1)}
    if ok:
        summ["token_tail_abs_max_max"] = max(r["token_tail_abs_max"] for r in ok)
        summ["real_tail_norm_mean"] = sum(r["real_tail_norm_mean"] for r in ok) / len(ok)
        summ["real_step0_max_mean"] = sum(r["real_step0_max_mean"] for r in ok) / len(ok)
        for arm in ARMS + ["control_rebuilt"]:
            a = [r["arms"][arm] for r in ok]
            n = len(a)
            summ[arm] = {
                "mean_token_rank": sum(x["token_rank"] for x in a) / n,
                "frac_beats_majority_best": sum(x["beats_majority_best"] for x in a) / n,
                "frac_beats_majority_mean": sum(x["beats_majority_mean"] for x in a) / n,
                "mean_gap_to_majority_best": sum(x["gap_to_majority_best"] for x in a) / n,
                "frac_argmin_is_token": sum(x["argmin_is_token"] for x in a) / n,
                "frac_selected_is_token": sum(x["selected_is_token"] for x in a) / n,
                "mean_score_std": sum(x["score_std"] for x in a) / n,
                "mean_token_reality_cost": sum(x["token_reality_cost"] for x in a) / n,
            }
        summ["ref_best_majority_reality_cost_mean"] = sum(r["ref_bm_reality_cost"] for r in ok) / len(ok)
        summ["pm_head_argmax_is_token_class_frac"] = sum(r["pm_head_argmax"] == r["token_class"] for r in ok) / len(ok)
        summ["control_rebuilt_matches_native"] = all(
            abs(r["arms"]["control"]["token_score"] - r["arms"]["control_rebuilt"]["token_score"]) < 1e-5
            for r in ok)
    summ["total_seconds"] = round(time.time() - t0, 1)
    out = os.path.join(HERE, "probe_spcem_seed%d.json" % seed)
    with open(out, "w") as f:
        json.dump({"summary": summ, "rows": rows}, f, indent=1)
    print(json.dumps(summ, indent=1))
    print("wrote", out)


if __name__ == "__main__":
    sd = int(sys.argv[1]) if len(sys.argv) > 1 else 11
    ns = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    main(seed=sd, n_states=ns)
