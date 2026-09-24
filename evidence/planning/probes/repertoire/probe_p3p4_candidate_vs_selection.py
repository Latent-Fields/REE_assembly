"""Probe (bt0924-repertoire-ab): decompose the V3-EXQ-1061 monostrategy.

QUESTION. V3-EXQ-1061 addendum 4 measured E3 committing the SAME first action at
39-40/40 probe states. That number alone cannot tell Type A (the candidate pool
itself holds only one first-action class -- nothing else is ever proposed) from a
selection-stage collapse (the pool holds several classes, E3 always picks one).
This probe re-creates ONE 1061 cell (intact arm, production ao_std floor 0.2) and,
at each probe state, records:
  - first-action class of every candidate (argmax of actions[:, 0, :])
  - n distinct classes in the pool, pool class entropy
  - E3 per-candidate scores (bare e3.select, exactly 1061's path) -> spread,
    per-class best score, best-vs-second-best CLASS gap, score std
  - which class E3 selected, and whether it is the pool-majority class
  - the same through the FULL agent path (agent.generate_trajectories +
    agent.select_action) with ticks forced so E3 re-selects each probe state.
Read-only on substrate; imports 1061's builders from a throwaway detached ree-v3
worktree expected at ./ree-v3-wt next to this file (run @ ree-v3 00210b5).
Usage: python3 probe_p3p4_candidate_vs_selection.py <seed>  (seeds run: 11 23 37).
ASCII-only output.
"""
import json
import math
import os
import sys
import time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
WT = os.path.join(HERE, "ree-v3-wt")
sys.path.insert(0, WT)
sys.path.insert(0, os.path.join(WT, "experiments"))

import torch  # noqa: E402

torch.set_num_threads(2)

import v3_exq_1061_mech131_anticipatory_residue_lesion as X  # noqa: E402


def ent(counts):
    n = sum(counts.values())
    if n == 0:
        return 0.0
    return -sum((c / n) * math.log(c / n) for c in counts.values() if c > 0)


def first_class(t):
    a = t.actions
    return int(torch.argmax(a[0, 0, :]).item())


def main(seed=11, warm_eps=20, steps=100, n_states=40):
    t0 = time.time()
    agent, env, cfg = X.build_agent(True, True, seed, X.PRODUCTION_FLOOR)
    warm = X.warmup_train(agent, env, seed, warm_eps, steps)
    obs_dict = warm.pop("final_obs")
    warm.pop("_harm_pos", None)
    warm.pop("_harm_neg", None)
    t_warm = time.time() - t0

    rows = []
    bare_sel = Counter()
    full_sel = Counter()
    for s in range(n_states):
        body, world = X._obs(obs_dict)
        latent = agent.sense(body, world)
        theta_z = agent.theta_buffer.summary()
        z_self = latent.z_self.detach()
        torch.manual_seed(seed * 1000 + s)
        trajs = agent.hippocampal.propose_trajectories(theta_z, z_self=z_self)
        row = {"probe_index": s, "n_candidates": len(trajs)}
        if trajs:
            classes = [first_class(t) for t in trajs]
            cc = Counter(classes)
            row["pool_class_counts"] = dict(sorted(cc.items()))
            row["pool_n_classes"] = len(cc)
            row["pool_class_entropy"] = ent(cc)
            with torch.no_grad():
                sel = agent.e3.select(trajs, temperature=1.0)
            sc = [float(x) for x in sel.scores.detach().reshape(-1).tolist()]
            sel_cls = int(torch.argmax(sel.selected_action.detach()).item())
            bare_sel[sel_cls] += 1
            per_cls_best = {}
            per_cls_vals = {}
            for c, v in zip(classes, sc):
                per_cls_best[c] = min(v, per_cls_best.get(c, float("inf")))
                per_cls_vals.setdefault(c, []).append(v)
            maj = cc.most_common(1)[0][0]
            maj_mean = sum(per_cls_vals[maj]) / len(per_cls_vals[maj])
            minority = [v for c, vs in per_cls_vals.items() if c != maj for v in vs]
            row["per_class_mean_score"] = {str(k): sum(v) / len(v) for k, v in per_cls_vals.items()}
            row["minority_beats_majority_mean_frac"] = (
                sum(v < maj_mean for v in minority) / len(minority)) if minority else None
            row["minority_beats_majority_best"] = (
                min(minority) < per_cls_best[maj]) if minority else None
            ordered = sorted(per_cls_best.values())
            row.update({
                "bare_selected_class": sel_cls,
                "bare_selected_is_pool_majority": sel_cls == cc.most_common(1)[0][0],
                "score_min": min(sc), "score_max": max(sc),
                "score_spread": max(sc) - min(sc),
                "score_std": float(torch.tensor(sc).std().item()) if len(sc) > 1 else 0.0,
                "per_class_best_score": {str(k): v for k, v in sorted(per_cls_best.items())},
                "class_gap_best_vs_second": (ordered[1] - ordered[0]) if len(ordered) > 1 else None,
                "committed_flag": bool(sel.committed),
            })
        # FULL agent path at this state (fresh E3 tick forced).
        try:
            ticks = {"e1_tick": True, "e2_tick": True, "e3_tick": True,
                     "e3_quiescent": False}
            e1_prior = agent._e1_tick(latent)
            agent._committed_candidates = None
            cands = agent.generate_trajectories(latent, e1_prior, ticks)
            fc = Counter(first_class(t) for t in cands)
            act = agent.select_action(cands, ticks, 1.0)
            fa = int(torch.argmax(act.detach().reshape(-1)).item())
            full_sel[fa] += 1
            row["full_pool_class_counts"] = dict(sorted(fc.items()))
            row["full_pool_n_classes"] = len(fc)
            row["full_selected_class"] = fa
        except Exception as e:  # report, do not hide
            row["full_path_error"] = repr(e)[:200]
        rows.append(row)
        _f, _h, done, _i, obs_dict = env.step(int(torch.randint(0, X.ACTION_DIM, (1,)).item()))
        if done:
            _f, obs_dict = env.reset()

    ok = [r for r in rows if "pool_n_classes" in r]
    summ = {
        "seed": seed, "warm_eps": warm_eps, "steps": steps, "n_states": n_states,
        "grid_size": X.GRID_SIZE, "world_dim": X.WORLD_DIM, "self_dim": X.SELF_DIM,
        "ao_std_floor": X.PRODUCTION_FLOOR,
        "warm_seconds": round(t_warm, 1), "total_seconds": round(time.time() - t0, 1),
        "mean_n_candidates": sum(r["n_candidates"] for r in ok) / max(1, len(ok)),
        "frac_states_pool_ge2_classes": sum(r["pool_n_classes"] >= 2 for r in ok) / max(1, len(ok)),
        "mean_pool_n_classes": sum(r["pool_n_classes"] for r in ok) / max(1, len(ok)),
        "mean_pool_class_entropy": sum(r["pool_class_entropy"] for r in ok) / max(1, len(ok)),
        "bare_selected_counts": dict(sorted(bare_sel.items())),
        "bare_selected_entropy": ent(bare_sel),
        "frac_bare_selected_is_pool_majority": sum(r["bare_selected_is_pool_majority"] for r in ok) / max(1, len(ok)),
        "mean_score_spread": sum(r["score_spread"] for r in ok) / max(1, len(ok)),
        "mean_score_std": sum(r["score_std"] for r in ok) / max(1, len(ok)),
        "mean_abs_score": sum(abs(r["score_min"]) for r in ok) / max(1, len(ok)),
        "mean_class_gap": (lambda g: sum(g) / len(g) if g else None)(
            [r["class_gap_best_vs_second"] for r in ok if r["class_gap_best_vs_second"] is not None]),
        "mean_minority_beats_majority_mean_frac": (lambda v: sum(v) / len(v) if v else None)(
            [r["minority_beats_majority_mean_frac"] for r in ok if r.get("minority_beats_majority_mean_frac") is not None]),
        "frac_states_minority_beats_majority_best": (lambda v: sum(v) / len(v) if v else None)(
            [r["minority_beats_majority_best"] for r in ok if r.get("minority_beats_majority_best") is not None]),
        "full_selected_counts": dict(sorted(full_sel.items())),
        "full_selected_entropy": ent(full_sel),
        "frac_full_pool_ge2_classes": (lambda v: sum(v) / len(v) if v else None)(
            [r["full_pool_n_classes"] >= 2 for r in rows if "full_pool_n_classes" in r]),
        "full_path_errors": sum("full_path_error" in r for r in rows),
    }
    out = os.path.join(HERE, "probe_p3p4_seed%d.json" % seed)
    with open(out, "w") as f:
        json.dump({"summary": summ, "rows": rows}, f, indent=1)
    print(json.dumps(summ, indent=1))
    print("wrote", out)


if __name__ == "__main__":
    sd = int(sys.argv[1]) if len(sys.argv) > 1 else 11
    main(seed=sd)
