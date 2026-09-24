"""Worker G off-policy feasibility probe (M2b): does a channel's VOTE for the executed action
predict the GROUNDED outcome, and does that distinguish trained from shuffled evaluator heads?

Same preamble as valuation_feasibility_probe.py (TB regime: tiebreak ON). Then a uniform-random
action stream (fresh env, seed+41, 1500 steps) through the agent's own encoder. At each state
the 5 one-class scaffold candidates are rolled out ONCE by E2 (COV head D, depth 2 = R2) and
scored per channel (F, harm_eval, residue, benefit_eval) under three evaluator sets: untrained
(T1), trained (T2), label-shuffled (T3). vote_c = -s_c (x_{a,c} - mean_{c'!=a} x_{c'}) for the
executed random action a. Outcome = the received scalar r_t (G-all) and r_t with |r|>0.1
(G-contact). transition_type is recorded for scoring only. Residue accumulates natively via
agent.update_residue(harm_signal) along the stream. Nothing is fed back (open loop, D1/D2-lite).
ASCII-only output.
"""
from __future__ import annotations

import argparse
import copy
import functools
import json
import sys
import time
from pathlib import Path

import numpy as np
import torch

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "ree-v3-wt"))
sys.path.insert(0, str(HERE / "ree-v3-wt" / "experiments"))
sys.path.insert(0, str(HERE))

import rollout_fidelity_probe as R  # noqa: E402
import encoding_vs_objective_probe as E  # noqa: E402
import balanced_replay_probe as BP  # noqa: E402
import partitioned_repair_probe as PR  # noqa: E402
import evaluation_edge_probe as EP  # noqa: E402

torch.set_num_threads(2)
DEPTH = PR.DEPTH


@torch.no_grad()
def channel_terms(agent, trajs):
    e3 = agent.e3
    f = [float(e3.compute_reality_cost(t).mean()) for t in trajs]
    m = [float(e3.compute_harm_cost_fallback(t).mean()) for t in trajs]
    ph = [float(e3.compute_residue_cost(t).mean()) for t in trajs]
    b = [float(e3.compute_benefit_score(t).mean()) for t in trajs]
    return np.asarray([f, m, ph, b]).T  # [A, 4] raw (unweighted)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--steps", type=int, default=1500)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    t0 = time.time()
    R.CausalGridWorldV2 = functools.partial(R.CausalGridWorldV2, proximity_approach_magnitude_tiebreak=True)
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
    init_ev = EP.eval_heads(agent)
    BP.set_head(agent, headA)
    nat = EP.collect_native(agent, R.build_B(a.seed + 21, False)[0], 1500, a.seed + 21)
    ran = EP.collect_random(agent, R.build_B(a.seed + 23, False)[0], 1500, a.seed + 23)
    agent.reset()
    data = nat + ran
    evT, _ = EP.train_evaluators(agent, init_ev, data, 1500, a.seed, False)
    evS, _ = EP.train_evaluators(agent, init_ev, data, 1500, a.seed, True)
    print("PREAMBLE t=%.0fs" % (time.time() - t0), flush=True)
    # ---- off-policy random stream ----
    BP.set_head(agent, headD)
    agent.e3._score_depth_limit = DEPTH
    agent.e3.config.benefit_eval_enabled = True
    sets = {"T1_untrained": init_ev, "T2_trained": evT, "T3_shuffled": evS}
    env2 = R.build_B(a.seed + 41, False)[0]
    g = np.random.default_rng(a.seed + 41)
    _f, obs = env2.reset(); agent.reset()
    lat = agent.sense(obs["body_state"], obs["world_state"], obs_harm=obs.get("harm_obs"),
                      obs_harm_a=obs.get("harm_obs_a"), obs_harm_history=obs.get("harm_history"))
    with torch.no_grad():
        pool = agent.hippocampal.propose_trajectories(lat.z_world.detach(), z_self=lat.z_self.detach())
    base_shape = tuple(pool[0].actions.shape)
    rows = []
    for i in range(a.steps):
        if i > 0:
            lat = agent.sense(obs["body_state"], obs["world_state"], obs_harm=obs.get("harm_obs"),
                              obs_harm_a=obs.get("harm_obs_a"), obs_harm_history=obs.get("harm_history"))
        with torch.no_grad():
            trajs = []
            for c in range(A):
                act = torch.zeros(base_shape); act[:, 0, c] = 1.0
                trajs.append(agent.e2.rollout_with_world(lat.z_self.detach(), lat.z_world.detach(), act,
                                                         compute_action_objects=False))
        terms = {}
        for k, ev in sets.items():
            EP.set_eval(agent, ev)
            terms[k] = channel_terms(agent, trajs).tolist()
        act_i = int(g.integers(0, A))
        _f, hsig, done, info, obs = env2.step(act_i)
        tt = info.get("transition_type", "none") if isinstance(info, dict) else "none"
        agent._last_action = BP.onehot(act_i, A)
        agent.update_residue(harm_signal=float(hsig), world_delta=None, hypothesis_tag=False, owned=True)
        rows.append({"a": act_i, "r": float(hsig), "tt": tt, "terms": terms})
        if done:
            _f, obs = env2.reset(); agent.reset()
        if i % 500 == 0:
            print("step %d t=%.0fs" % (i, time.time() - t0), flush=True)
    json.dump({"args": vars(a), "rows": rows, "t_total_s": round(time.time() - t0, 1)}, open(a.out, "w"))
    print("wrote %s t=%.0fs" % (a.out, time.time() - t0), flush=True)


if __name__ == "__main__":
    main()
