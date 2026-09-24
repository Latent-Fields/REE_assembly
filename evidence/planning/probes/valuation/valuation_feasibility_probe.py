"""Worker G feasibility probe: grounded main-channel valuation (DESIGN + FEASIBILITY only).

bt0924-valuation (Worker G, orchestrate-20260924-breakthrough). Nothing lands in ree_core.
Reuses e3_evaluation_edge_test ADDENDUM 1's harness verbatim (evaluation_edge_probe.py with
--tiebreak 1 --force-gate 0): same preamble (encoder P0, heads A/D, labelled own experience,
trained / shuffled evaluators), same closed-loop arms T1 (FULL), T2 (FULL+EVAL), T3 (FULL+SHUF).

The ONLY addition is a READ-ONLY tap:
  * E3.e3_score_decomp_enabled = True (diagnostics-only per-candidate channel terms,
    e3_selector.py:1821-1834 / :3953-3957), and a wrapper on agent.e3.select that copies
    selected_index, committed, scores and the per-candidate weighted channel terms per tick.
  * per env step: reward (StepResult.harm_signal), transition_type (SCORING ONLY -- env
    internal, never available to a candidate mechanism), and whether E3 selected this step.
Canary: T1/T2/T3 counts must reproduce TB_s{seed}.json bit-for-bit (proves the tap is inert).
ASCII-only output.
"""
from __future__ import annotations

import argparse
import copy
import functools
import json
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np
import torch

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "ree-v3-wt"))
sys.path.insert(0, str(HERE / "ree-v3-wt" / "experiments"))
sys.path.insert(0, str(HERE))

from experiments._harness import StepHarness  # noqa: E402
import rollout_fidelity_probe as R  # noqa: E402
import encoding_vs_objective_probe as E  # noqa: E402
import balanced_replay_probe as BP  # noqa: E402
import partitioned_repair_probe as PR  # noqa: E402
import evaluation_edge_probe as EP  # noqa: E402

torch.set_num_threads(2)
DEPTH = PR.DEPTH
CH = ("f_weighted", "harm_weighted", "residue_weighted", "benefit_weighted", "goal_weighted")


def closed_loop_tapped(seed, enc_state, head, ev, benefit_on, gate_n, steps):
    R.seed_all(seed)
    env, agent, cfg = R.build_B(seed, False)
    agent.latent_stack.load_state_dict(enc_state)
    BP.set_head(agent, head)
    agent.hippocampal.config.use_action_class_scaffold_candidates = True
    agent.e3._score_depth_limit = DEPTH
    EP.configure_eval(agent, ev, benefit_on, gate_n)
    agent.e3.config.use_e3_channel_commensurability = False
    agent.eval()
    e3 = agent.e3
    e3.e3_score_decomp_enabled = True
    ticks = []
    cur = {"step": -1}
    orig = e3.select

    def wsel(*a, **k):
        res = orig(*a, **k)
        pc = (e3.last_score_decomp or {}).get("per_candidate") or []
        ticks.append({"step": cur["step"], "sel": int(res.selected_index), "committed": bool(res.committed),
                      "scores": [float(x) for x in res.scores.detach().reshape(-1).tolist()],
                      "terms": [[float(d.get(c, 0.0)) for c in CH] for d in pc]})
        return res
    e3.select = wsel
    weights = {"f_weight": float(e3.config.f_weight), "lambda_ethical": float(e3.config.lambda_ethical),
               "rho_residue": float(e3.config.rho_residue), "benefit_weight": float(e3.config.benefit_weight),
               "goal_weight": float(e3.config.goal_weight)}
    h = StepHarness(agent, env, train_mode=False, seed=seed)
    _f, obs = env.reset(); agent.reset(); h.reset()
    rew, tts, acts, ep = [], [], [], 0
    for i in range(steps):
        cur["step"] = i
        r = h.step(obs)
        rew.append(float(r.harm_signal)); acts.append(int(r.action.detach().reshape(-1).argmax()))
        tts.append(r.info.get("transition_type", "none") if isinstance(r.info, dict) else "none")
        obs = r.next_obs_dict
        if r.done:
            _f, obs = env.reset(); agent.reset(); h.reset(); ep += 1
    rw = np.asarray(rew); tc = Counter(tts)
    summ = {"reward_per_100": float(rw.sum() * 100 / steps),
            "harm_contacts": int(sum(v for k, v in tc.items() if k in EP.CONTACT)),
            "hazard_approach": int(tc.get("hazard_approach", 0)), "benefit_approach": int(tc.get("benefit_approach", 0)),
            "benefit_contacts": int(sum(v for k, v in tc.items() if k in EP.BCONTACT)), "episodes_ended": ep}
    return {"summary": summ, "weights": weights, "rewards": rew, "ttypes": tts, "actions": acts, "ticks": ticks}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--wake", type=int, default=600)
    ap.add_argument("--label-steps", type=int, default=1500)
    ap.add_argument("--eval-steps", type=int, default=1500)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    t0 = time.time()
    R.CausalGridWorldV2 = functools.partial(R.CausalGridWorldV2, proximity_approach_magnitude_tiebreak=True)
    assert R.build_B(a.seed, False)[0].proximity_approach_magnitude_tiebreak is True
    # ---- ADDENDUM 1 (TB) preamble, same RNG order ----
    R.seed_all(a.seed)
    env, agent, cfg = R.build_B(a.seed, False)
    A = env.action_dim
    PR.p0(agent, a.seed)
    agent.eval()
    enc_state = copy.deepcopy(agent.latent_stack.state_dict())
    init = BP.get_head(agent)
    trans = BP.collect_replay(agent, env, 1500, a.seed)
    rnd = E.collect(R.build_B(a.seed + 11, False)[0], agent, len(trans) + 200, a.seed + 3)
    trans_d = []
    for e in rnd:
        for t in range(e["a"].shape[0] - 1):
            trans_d.append((e["z"][t:t + 1], int(e["a"][t]), e["z"][t + 1:t + 2]))
    trans_d = trans_d[:len(trans)]
    headA, infoA = BP.train_arm(agent, init, trans, A, np.ones(len(trans)), 3000, a.seed)
    headD, infoD = BP.train_arm(agent, init, trans_d, A, np.ones(len(trans_d)), 3000, a.seed)
    init_ev = EP.eval_heads(agent)
    BP.set_head(agent, headA)
    nat = EP.collect_native(agent, R.build_B(a.seed + 21, False)[0], a.label_steps, a.seed + 21)
    ran = EP.collect_random(agent, R.build_B(a.seed + 23, False)[0], a.label_steps, a.seed + 23)
    agent.reset()
    data = nat + ran
    # reward magnitude by transition type in the labelled own experience (is contact vs
    # proximity separable from the scalar the agent receives?)
    mag = {}
    for d in data:
        mag.setdefault(d[2], []).append(d[1])
    mag = {k: {"n": len(v), "min": float(np.min(v)), "max": float(np.max(v)), "mean": float(np.mean(v))}
           for k, v in mag.items()}
    evT, infoT = EP.train_evaluators(agent, init_ev, data, a.eval_steps, a.seed, False)
    evS, infoS = EP.train_evaluators(agent, init_ev, data, a.eval_steps, a.seed, True)
    gate_n = infoT["n_benefit_pos_train"]
    print("PREAMBLE gate_n=%d t=%.0fs" % (gate_n, time.time() - t0), flush=True)
    out = {"args": vars(a), "gate_n": gate_n, "reward_by_ttype": mag,
           "evaluators": {"trained": infoT, "shuffled": infoS}, "arms": {}}
    for name, ev, bon in (("T1_FULL", init_ev, False), ("T2_FULL_EVAL", evT, True), ("T3_FULL_SHUF", evS, True)):
        res = closed_loop_tapped(a.seed, enc_state, headD, ev, bon, gate_n, a.wake)
        out["arms"][name] = res
        print("ARM %s %s ticks=%d t=%.0fs" % (name, json.dumps(res["summary"]), len(res["ticks"]), time.time() - t0),
              flush=True)
        json.dump(out, open(a.out, "w"))
    out["t_total_s"] = round(time.time() - t0, 1)
    json.dump(out, open(a.out, "w"))
    print("wrote %s t=%.0fs" % (a.out, time.time() - t0), flush=True)


if __name__ == "__main__":
    main()
