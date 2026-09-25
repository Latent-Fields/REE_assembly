"""Probe (bt0925-spcem2): repeat the SP-CEM zero-continuation check at the DEPLOYED
world_dim/self_dim = 32 with the FULL V3-EXQ-1061 warmup schedule (trained agent),
before any default change.

This is bt0925-spcem's probe_spcem_zero_continuation.py (see
REE_assembly/evidence/planning/spcem_zero_continuation_check_20260925.md), changed
ONLY in:
  (i)  self_dim = world_dim = 32 (deployed) instead of 16 (toy) -- monkeypatched on
       the imported driver module BEFORE build_agent() is called; no file edits to
       the driver or ree_core.
  (ii) warmup = the full V3-EXQ-1061 schedule (600 episodes x 200 steps = 120000
       steps) instead of 20 x 100 -- or the largest warmup that fits ~25 min Mac
       wall per seed, sized from a short calibration run and recorded.

All arms, readouts, fidelity checks (control_rebuilt drift check), and the 40-state
random-walk probe design are UNCHANGED from the first probe. Read-only on substrate.
Imports V3-EXQ-1061's builders from ./ree-v3-wt (a detached throwaway worktree off
origin/main). ASCII-only output.

Usage: python3 probe_spcem_wd32_trained.py <seed> <warm_eps> [n_states]
"""
import json
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

# (i) deployed dims -- monkeypatch only, no file edit.
DEPLOYED_DIM = 32
X.SELF_DIM = DEPLOYED_DIM
X.WORLD_DIM = DEPLOYED_DIM

STEPS_PER_EPISODE = X.STEPS_PER_EPISODE  # 200, 1061's own number
FULL_WARMUP_EPISODES = X.WARMUP_EPISODES  # 600, 1061's own number

ARMS = ["control", "hold", "sampled", "oh_bt", "pm_z", "pm_bt", "maj_oh_z", "maj_oh_bt"]


def first_class(t):
    return int(torch.argmax(t.actions[0, 0, :]).item())


def src(t):
    return (t.metadata or {}).get("source")


def main(seed=11, warm_eps=FULL_WARMUP_EPISODES, steps=STEPS_PER_EPISODE, n_states=40):
    t0 = time.time()
    agent, env, cfg = X.build_agent(True, True, seed, X.PRODUCTION_FLOOR)
    assert cfg.hippocampal.self_dim == DEPLOYED_DIM if hasattr(cfg.hippocampal, "self_dim") else True
    t_build = time.time() - t0
    hc = agent.hippocampal.config
    warm = X.warmup_train(agent, env, seed, warm_eps, steps)
    obs_dict = warm.pop("final_obs")
    warm.pop("_harm_pos", None)
    warm.pop("_harm_neg", None)
    t_warm = time.time() - t0 - t_build
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
            "token_step0_norm": float(acts[0, 0].norm().item()),
            "token_tail_abs_max": float(acts[0, 1:].abs().max().item()),
            "real_step0_abs_mean": float(real_acts[:, 0].abs().mean().item()),
            "real_step0_norm_mean": float(real_acts[:, 0].norm(dim=-1).mean().item()),
            "real_tail_abs_mean": float(real_acts[:, 1:].abs().mean().item()),
            "real_tail_norm_mean": float(real_acts[:, 1:].norm(dim=-1).mean().item()),
            "real_step0_max_mean": float(real_acts[:, 0].max(dim=-1).values.mean().item()),
        })
        g = torch.Generator().manual_seed(seed * 7919 + s)
        rand_real = real_idx[int(torch.randint(0, len(real_idx), (1,), generator=g).item())]
        e3c = agent.e3
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
        bm = pool[best_maj].actions.detach().clone()
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
        ref_bm = roll(z_self, theta_z, bm)
        row["ref_bm_reality_cost"] = float(agent.e3.compute_reality_cost(ref_bm).item())
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
            "build_seconds": round(t_build, 1),
            "warm_seconds": round(t_warm, 1),
            "full_1061_warmup_episodes": FULL_WARMUP_EPISODES,
            "warmup_shrunk": bool(warm_eps < FULL_WARMUP_EPISODES)}
    if ok:
        summ["token_step0_norm_mean"] = sum(r["token_step0_norm"] for r in ok) / len(ok)
        summ["real_step0_norm_mean"] = sum(r["real_step0_norm_mean"] for r in ok) / len(ok)
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
    summ["warmup_stats"] = warm
    summ["total_seconds"] = round(time.time() - t0, 1)
    out = os.path.join(HERE, "probe_spcem2_seed%d.json" % seed)
    with open(out, "w") as f:
        json.dump({"summary": summ, "rows": rows}, f, indent=1)
    print(json.dumps(summ, indent=1))
    print("wrote", out)


if __name__ == "__main__":
    sd = int(sys.argv[1]) if len(sys.argv) > 1 else 11
    we = int(sys.argv[2]) if len(sys.argv) > 2 else FULL_WARMUP_EPISODES
    ns = int(sys.argv[3]) if len(sys.argv) > 3 else 40
    main(seed=sd, warm_eps=we, n_states=ns)
