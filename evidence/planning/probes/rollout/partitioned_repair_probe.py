"""ADDENDUM 3 probe: partitioned closed-loop test of three repairs (probe-only, nothing lands).

bt0924-rollout-d (Worker D, orchestrate-20260924-breakthrough).

REPAIRS
  R5   proposal. R5a (uninformative CEM initial mean) was pre-checked with r5_precheck.py and
       is bit-identical to native on 2 seeds, so R5 here = R5b: the EXISTING hippocampal knob
       use_action_class_scaffold_candidates (config.py; module.py _build_action_class_scaffold_
       candidates), set on the live agent's HippocampalConfig. It prepends one one-hot
       first-action candidate per class. NOT state-conditioned: it bypasses the untrained
       decoder, and any state dependence must come from E3's choice among the scaffolds.
  COV  E2 world head trained on uniform-random-action transitions through the agent's own
       SD-070 encoder (ADDENDUM 2 arm D). Without COV: head trained on the agent's own replay
       (ADDENDUM 2 arm A). Same budget (3000 updates, batch 32, Adam 3e-4, clip 1.0).
  R2   E3 depth limit via SD-081's live knob e3._score_depth_limit = 2 (initial state + 1 step).
ARMS (closed loop): FULL, FULL-R5, FULL-COV, FULL-R2, NATIVE. Each arm = a FRESH agent from the
  same seed (no carry-over), the master's trained encoder + chosen head loaded, fresh env with
  the same seed, WAKE waking steps.
OUTCOMES
  1 env-grounded: the env's own reward stream (StepResult.harm_signal: negative = harm,
    positive = benefit), summed per 100 steps; harm-event and benefit-event counts.
  2 behaviour: executed-action entropy, majority share; P3 proposal majority invariance.
  3 choice quality (env deepcopy): at probe states, Q(c) = mean over NCONT random
    continuations of the summed env reward of [step c, then CONT_LEN random steps]. E3's pick
    on the one-candidate-per-class scaffold (arm head + arm depth) vs the Q-best set; only
    states where Q is not constant across classes count. R5 does not enter this measure.
ASCII-only output.
"""
from __future__ import annotations

import argparse
import copy
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

from experiments._harness import StepHarness, StepHooks  # noqa: E402
import rollout_fidelity_probe as R  # noqa: E402
import encoding_vs_objective_probe as E  # noqa: E402
import balanced_replay_probe as BP  # noqa: E402

torch.set_num_threads(2)
DEPTH = 2
ARMS = {"FULL": (1, 1, 1), "FULL-R5": (0, 1, 1), "FULL-COV": (1, 0, 1), "FULL-R2": (1, 1, 0), "NATIVE": (0, 0, 0)}


def p0(agent, seed):
    from experiments._lib.zworld_p0_warmup import run_zworld_p0
    from experiments._lib.capability_eval import RandomPolicy
    from ree_core.latent.zworld_p0 import ZWorldP0Config
    return run_zworld_p0(agent, R.build_B(seed, False)[0], seed=seed, episodes=20, steps_per_episode=50,
                         policy=RandomPolicy(seed), label="bt0924d", dry_run=False,
                         config=ZWorldP0Config(preservation_weight=1000.0))


def q_values(env, A, g, ncont, clen):
    q = []
    for c in range(A):
        tot = 0.0
        for _ in range(ncont):
            e = copy.deepcopy(env)
            _f, h, done, _i, _o = e.step(c)
            s = float(h)
            for _k in range(clen):
                if done:
                    break
                _f, h, done, _i, _o = e.step(int(g.integers(0, A)))
                s += float(h)
            tot += s
        q.append(tot / ncont)
    return np.asarray(q)


def probe_states(agent, env, steps, every, A, seed, ncont, clen):
    g = np.random.default_rng(seed + 31)
    states = []

    def on_action(agent, latent, action, obs_dict, ticks, step, **k):
        if step % every:
            return
        rs = torch.get_rng_state()
        with torch.no_grad():
            pool = agent.hippocampal.propose_trajectories(latent.z_world.detach(), z_self=latent.z_self.detach())
        torch.set_rng_state(rs)
        states.append({"z0": latent.z_world.detach().clone(), "s0": latent.z_self.detach().clone(),
                       "base": pool[0].actions.detach().clone(), "q": q_values(env, A, g, ncont, clen)})

    h = StepHarness(agent, env, train_mode=False, seed=seed, hooks=StepHooks(on_action=on_action))
    _f, obs = env.reset(); agent.reset(); h.reset()
    for _ in range(steps):
        r = h.step(obs); obs = r.next_obs_dict
        if r.done:
            _f, obs = env.reset(); agent.reset(); h.reset()
    return states


@torch.no_grad()
def choice_quality(agent, states, A, depth):
    hits, chance, n_inf, picks = [], [], 0, []
    for st in states:
        q = st["q"]
        if np.ptp(q) < 1e-9:
            continue
        n_inf += 1
        trajs = []
        for c in range(A):
            a = st["base"].clone(); a[:, 0, :] = 0.0; a[:, 0, c] = 1.0
            trajs.append(agent.e2.rollout_with_world(st["s0"], st["z0"], a, compute_action_objects=False))
        j = BP.score(agent, trajs, depth)
        best = set(np.nonzero(q >= q.max() - 1e-9)[0].tolist())
        p = int(np.argmin(j)); picks.append(p)
        hits.append(p in best); chance.append(len(best) / A)
    return {"n_states": len(states), "n_informative": n_inf,
            "pick_is_Qbest": float(np.mean(hits)) if hits else None, "chance": float(np.mean(chance)) if chance else None,
            "pick_counts": {str(k): v for k, v in sorted(Counter(picks).items())}}


def closed_loop_rewards(seed, enc_state, head, r5, r2, steps):
    R.seed_all(seed)
    env, agent, cfg = R.build_B(seed, False)
    agent.latent_stack.load_state_dict(enc_state)
    BP.set_head(agent, head)
    agent.hippocampal.config.use_action_class_scaffold_candidates = bool(r5)
    agent.e3._score_depth_limit = DEPTH if r2 else None
    agent.eval()
    h = StepHarness(agent, env, train_mode=False, seed=seed)
    _f, obs = env.reset(); agent.reset(); h.reset()
    rew, acts, log, ep = [], [], [], 0
    for _ in range(steps):
        r = h.step(obs)
        rew.append(float(r.harm_signal))
        a = int(r.action.detach().reshape(-1).argmax()); acts.append(a)
        log.append((ep, r.latent.z_world.detach().clone(), r.latent.z_self.detach().clone(),
                    r.action.detach().reshape(1, -1).float().clone()))
        obs = r.next_obs_dict
        if r.done:
            _f, obs = env.reset(); agent.reset(); h.reset(); ep += 1
    rew = np.asarray(rew)
    cc = Counter(acts); p = np.asarray(list(cc.values()), float) / len(acts)
    m4 = R.m4_proposal(agent, log, 20, [], seed)["native"]
    assert agent.e3._score_depth_limit == (DEPTH if r2 else None)
    return {"steps": steps, "episodes_ended": ep, "reward_per_100": float(rew.sum() * 100 / steps),
            "harm_events_per_100": float((rew < 0).sum() * 100 / steps), "benefit_events_per_100": float((rew > 0).sum() * 100 / steps),
            "harm_sum_per_100": float(rew[rew < 0].sum() * 100 / steps), "benefit_sum_per_100": float(rew[rew > 0].sum() * 100 / steps),
            "action_counts": {str(k): v for k, v in sorted(cc.items())}, "action_entropy": float(-(p * np.log(p)).sum()),
            "majority_share": max(cc.values()) / len(acts),
            "P3_maj_share": m4["maj_share_mean"], "P3_modal_frac": m4["frac_states_with_modal_majority"],
            "P3_majority_counts": m4["majority_class_counts_across_states"], "P3_n_classes": m4["n_classes_mean"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=43)
    ap.add_argument("--wake", type=int, default=600)
    ap.add_argument("--probe-steps", type=int, default=200)
    ap.add_argument("--ncont", type=int, default=6)
    ap.add_argument("--clen", type=int, default=4)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    t0 = time.time()
    R.seed_all(a.seed)
    env, agent, cfg = R.build_B(a.seed, False)
    A = env.action_dim
    p0info = p0(agent, a.seed)
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
    print("HEADS replay_classes=%s A=%s D=%s t=%.0fs" % (dict(sorted(Counter(t[1] for t in trans).items())),
                                                        json.dumps(infoA), json.dumps(infoD), time.time() - t0), flush=True)
    BP.set_head(agent, headA)
    states = probe_states(agent, env, a.probe_steps, 5, A, a.seed, a.ncont, a.clen)
    cq = {}
    for cov in (0, 1):
        BP.set_head(agent, headD if cov else headA)
        for r2 in (0, 1):
            cq["COV%d_R2%d" % (cov, r2)] = choice_quality(agent, states, A, DEPTH if r2 else None)
    print("CHOICE %s t=%.0fs" % (json.dumps(cq), time.time() - t0), flush=True)
    out = {"args": vars(a), "p0_ran": p0info.get("p0a_ran"), "heads": {"A_native": infoA, "D_cov": infoD},
           "replay_class_counts": {str(k): v for k, v in sorted(Counter(t[1] for t in trans).items())},
           "choice_quality": cq, "arms": {}, "depth_limit": DEPTH}
    for name, (r5, cov, r2) in ARMS.items():
        res = closed_loop_rewards(a.seed, enc_state, headD if cov else headA, r5, r2, a.wake)
        res["choice_quality"] = cq["COV%d_R2%d" % (cov, r2)]
        out["arms"][name] = res
        print("ARM %-9s %s t=%.0fs" % (name, json.dumps({k: v for k, v in res.items() if k != "choice_quality"}), time.time() - t0), flush=True)
    out["t_total_s"] = round(time.time() - t0, 1)
    json.dump(out, open(a.out, "w"), indent=1, default=str)
    print("wrote %s t=%.0fs" % (a.out, time.time() - t0), flush=True)


if __name__ == "__main__":
    main()
