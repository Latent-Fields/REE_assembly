"""Worker F split probe: is the evaluator's failure in the EVALUATION or in the PREDICTION it reads?

Rebuilds evaluation_edge_probe.py's preamble for one seed (same RNG order -> same encoder,
heads A/D and trained / shuffled evaluators), then at probe states along a native waking run
(head A) clones the env and, for every action class c, records the TRUE immediate reward r_c
and the TRUE encoded arrival state z1_c (encode_next, validated in ADDENDUM 2). Per state:
  harm head on TRUE z1_c vs on E2-PREDICTED z1_c (COV head D, world_forward(z0, onehot c)):
    Spearman(head, -r_c) over classes, on states where r_c varies.
  benefit head likewise, on states where some class yields r_c > 0 (rare).
  agreement: Spearman(head(pred z1_c), head(true z1_c)).
ASCII-only output.
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
import time
from pathlib import Path

import numpy as np
import torch

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import evaluation_edge_probe as EV  # noqa: E402  (sets sys.path for the worktree)
from experiments._harness import StepHarness, StepHooks  # noqa: E402

R, E, BP, PR = EV.R, EV.E, EV.BP, EV.PR
torch.set_num_threads(2)


def spear(a, b):
    a = np.asarray(a, float); b = np.asarray(b, float)
    if a.std() < 1e-12 or b.std() < 1e-12:
        return None
    return float(np.corrcoef(avg_rank(a), avg_rank(b))[0, 1])


def avg_rank(x):
    """Average ranks: ties (e.g. four zero-harm classes) must not be given an arbitrary order."""
    x = np.asarray(x, float); r = np.empty(len(x))
    for v in np.unique(x):
        idx = np.nonzero(x == v)[0]
        r[idx] = np.mean(np.nonzero(np.sort(x) == v)[0])
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--steps", type=int, default=600)
    ap.add_argument("--every", type=int, default=3)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    t0 = time.time()
    R.seed_all(a.seed)
    env, agent, cfg = R.build_B(a.seed, False)
    A = env.action_dim
    PR.p0(agent, a.seed)
    agent.eval()
    init = BP.get_head(agent)
    trans = BP.collect_replay(agent, env, 1500, a.seed)
    rnd = E.collect(R.build_B(a.seed + 11, False)[0], agent, len(trans) + 200, a.seed + 3)
    trans_d = []
    for e in rnd:
        for t in range(e["a"].shape[0] - 1):
            trans_d.append((e["z"][t:t + 1], int(e["a"][t]), e["z"][t + 1:t + 2]))
    trans_d = trans_d[:len(trans)]
    headA, _ = BP.train_arm(agent, init, trans, A, np.ones(len(trans)), 3000, a.seed)
    headD, _ = BP.train_arm(agent, init, trans_d, A, np.ones(len(trans_d)), 3000, a.seed)
    init_ev = EV.eval_heads(agent)
    BP.set_head(agent, headA)
    nat = EV.collect_native(agent, R.build_B(a.seed + 21, False)[0], 1500, a.seed + 21)
    ran = EV.collect_random(agent, R.build_B(a.seed + 23, False)[0], 1500, a.seed + 23)
    agent.reset()
    evT, infoT = EV.train_evaluators(agent, init_ev, nat + ran, 1500, a.seed, False)
    evS, _ = EV.train_evaluators(agent, init_ev, nat + ran, 1500, a.seed, True)
    print("PREAMBLE harm_auc=%.3f benefit_auc=%s t=%.0fs" % (infoT["harm"]["heldout_auc"], infoT["benefit"]["heldout_auc"], time.time() - t0), flush=True)
    EV.set_eval(agent, init_ev)
    BP.set_head(agent, headA)
    states = []

    def on_action(agent, latent, action, obs_dict, ticks, step, **k):
        if step % a.every:
            return
        lat_s = agent._current_latent
        zt, rr = [], []
        for c in range(A):
            e = copy.deepcopy(env)
            _f, h, _d, _i, o2 = e.step(c)
            rr.append(float(h)); zt.append(BP.encode_next(agent, o2, lat_s, BP.onehot(c, A)))
        states.append({"z0": latent.z_world.detach().clone(), "zt": torch.cat(zt), "r": np.asarray(rr)})

    h = StepHarness(agent, env, train_mode=False, seed=a.seed, hooks=StepHooks(on_action=on_action))
    _f, obs = env.reset(); agent.reset(); h.reset()
    for _ in range(a.steps):
        r = h.step(obs); obs = r.next_obs_dict
        if r.done:
            _f, obs = env.reset(); agent.reset(); h.reset()
    BP.set_head(agent, headD)
    oh = torch.eye(A)
    res = {}
    with torch.no_grad():
        for tag, ev in (("trained", evT), ("shuffled", evS), ("untrained", init_ev)):
            EV.set_eval(agent, ev)
            acc = {k: [] for k in ("harm_true", "harm_pred", "harm_agree", "ben_true", "ben_pred", "ben_agree",
                                   "harm_true_pick_best", "harm_pred_pick_best", "ben_true_pick_best", "ben_pred_pick_best")}
            n_h = n_b = 0
            for st in states:
                zp = agent.e2.world_forward(st["z0"].expand(A, -1), oh)
                ht = agent.e3.harm_eval_head(st["zt"]).reshape(-1).numpy(); hp = agent.e3.harm_eval_head(zp).reshape(-1).numpy()
                bt = agent.e3.benefit_eval_head(st["zt"]).reshape(-1).numpy(); bp = agent.e3.benefit_eval_head(zp).reshape(-1).numpy()
                rr = st["r"]
                if np.ptp(np.minimum(rr, 0)) > 1e-9:
                    n_h += 1
                    harm = -np.minimum(rr, 0)
                    for k, v in (("harm_true", spear(ht, harm)), ("harm_pred", spear(hp, harm)), ("harm_agree", spear(hp, ht))):
                        if v is not None:
                            acc[k].append(v)
                    best = set(np.nonzero(harm <= harm.min() + 1e-9)[0].tolist())
                    acc["harm_true_pick_best"].append(int(np.argmin(ht)) in best)
                    acc["harm_pred_pick_best"].append(int(np.argmin(hp)) in best)
                if rr.max() > 0:
                    n_b += 1
                    ben = np.maximum(rr, 0)
                    for k, v in (("ben_true", spear(bt, ben)), ("ben_pred", spear(bp, ben)), ("ben_agree", spear(bp, bt))):
                        if v is not None:
                            acc[k].append(v)
                    best = set(np.nonzero(ben >= ben.max() - 1e-9)[0].tolist())
                    acc["ben_true_pick_best"].append(int(np.argmax(bt)) in best)
                    acc["ben_pred_pick_best"].append(int(np.argmax(bp)) in best)
            res[tag] = {"n_states": len(states), "n_harm_informative": n_h, "n_benefit_available": n_b,
                        **{k: (float(np.mean(v)) if v else None) for k, v in acc.items()},
                        "n_" + "harm_agree": len(acc["harm_agree"])}
            print("SPLIT %s %s" % (tag, json.dumps(res[tag])), flush=True)
    z_disp_true = float(np.mean([float((st["zt"] - st["zt"].mean(0)).norm(dim=-1).mean()) for st in states]))
    with torch.no_grad():
        z_disp_pred = float(np.mean([float((lambda zp: (zp - zp.mean(0)).norm(dim=-1).mean())(
            agent.e2.world_forward(st["z0"].expand(A, -1), oh))) for st in states]))
    n_distinct = len({tuple(np.round(st["z0"].reshape(-1).numpy(), 5)) for st in states})
    out = {"args": vars(a), "split": res, "n_distinct_z0": n_distinct, "xclass_z1_spread_true": z_disp_true, "xclass_z1_spread_pred": z_disp_pred,
           "z0_norm_mean": float(np.mean([float(st["z0"].norm()) for st in states])), "t_total_s": round(time.time() - t0, 1)}
    json.dump(out, open(a.out, "w"), indent=1)
    print("wrote %s z1 spread true=%.4f pred=%.4f t=%.0fs" % (a.out, z_disp_true, z_disp_pred, time.time() - t0), flush=True)


if __name__ == "__main__":
    main()
