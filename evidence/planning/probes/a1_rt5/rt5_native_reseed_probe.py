"""bt0925-rt5 (orchestrate-20260924-breakthrough), chip chip-20260925-a1-rt5-native-reseed-probe.

A1 RT-5 closer: measure NATIVE vs reseeded-NATIVE closed-loop noise with the env tie-break ON,
env seed FIXED and agent seed VARIED (the split A1 prereg sec 3 / Q6 requires), and compare
2 x RMS(NATIVE - NATIVE-Rk) against the accepted A1 floors. Pre-registration:
REE_assembly/evidence/planning/a1_rt5_native_reseed_probe_20260925.md (committed BEFORE any probe
seed ran). ASCII-only output. Nothing lands in ree_core.

One invocation = one env seed: NATIVE (k=0) through dev epoch + P0a warmup + closed-loop steps
0..599, classify stratum (A1 rule), write the stratum into the output JSON, then -- only if the
driver says that stratum still needs seeds -- NATIVE to 3000 and NATIVE-R1..R3 in full.

Per arm (agent_seed = env_seed + 10000 * k):
  1. env = CausalGridWorldV2(ENV_KW, seed=env_seed)            (constructed BEFORE agent seeding)
  2. seed_all(agent_seed); agent = REEAgent(REEConfig.from_dims(dims))   (NATIVE: every flag default)
  3. dev epoch: DEV native waking steps, StepHarness(train_mode=False, seed=agent_seed), no learning
  4. SD-070 P0a encoder warmup: 20 eps x 50 steps, RandomPolicy(agent_seed), preservation 1000,
     on a DEDICATED env CausalGridWorldV2(ENV_KW, seed=env_seed), recipe seed = agent_seed
  5. closed loop: env.reset(); agent.reset(); CLOSED steps, eval, reset on done.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np
import torch

HERE = Path(__file__).resolve().parent
WT = HERE / "ree-v3-wt"
sys.path.insert(0, str(WT))
sys.path.insert(0, str(WT / "experiments"))

from ree_core.agent import REEAgent  # noqa: E402
from ree_core.environment.causal_grid_world import CausalGridWorldV2  # noqa: E402
from ree_core.utils.config import REEConfig  # noqa: E402
from experiments._harness import StepHarness  # noqa: E402

torch.set_num_threads(2)

ENV_KW = dict(size=8, num_hazards=2, num_resources=3, max_episode_steps=200,
              proximity_approach_magnitude_tiebreak=True)
AGENT_SEED_OFFSET = 10_000
N_RESEED = 3
CONTACT = {"agent_caused_hazard", "env_caused_hazard", "env_caused_multisource"}
CONSUME = {"resource"}
EP_CAP = 200
EARLY_MIN = 10
STRATUM_WINDOW = 600


def seed_all(s):
    random.seed(s)
    np.random.seed(s)
    torch.manual_seed(s)


def classify(ends, window=STRATUM_WINDOW):
    """A1 sec 3 rule: >= 10 episodes that END inside closed-loop steps [0, window) with length < 200."""
    prev = -1
    early = 0
    for s, _c in ends:
        length = s - prev
        prev = s
        if s < window and length < EP_CAP:
            early += 1
    return ("hazard_trapped" if early >= EARLY_MIN else "benign"), early


def window(rew, tts, lo, hi):
    r = np.asarray(rew[lo:hi], float)
    t = tts[lo:hi]
    n = max(hi - lo, 1)
    g = float(sum(x for x, tt in zip(r, t) if tt in CONTACT or tt in CONSUME))
    tc = Counter(t)
    return {"reward_per100": float(r.sum() * 100.0 / n),
            "grounded_per100": g * 100.0 / n,
            "contacts_count": int(sum(v for k, v in tc.items() if k in CONTACT)),
            "contacts_per100": 100.0 * sum(v for k, v in tc.items() if k in CONTACT) / n,
            "consume_count": int(sum(v for k, v in tc.items() if k in CONSUME)),
            "benefit_approach": int(tc.get("benefit_approach", 0)),
            "hazard_approach": int(tc.get("hazard_approach", 0)),
            "tt_counts": dict(tc)}


def run_arm(env_seed, k, dev, closed, stop_at_classify_if, log):
    t0 = time.time()
    agent_seed = env_seed + AGENT_SEED_OFFSET * k
    env = CausalGridWorldV2(seed=env_seed, **ENV_KW)
    seed_all(agent_seed)
    cfg = REEConfig.from_dims(body_obs_dim=env.body_obs_dim, world_obs_dim=env.world_obs_dim,
                              action_dim=env.action_dim)
    assert int(cfg.latent.world_dim) == 32, cfg.latent.world_dim
    agent = REEAgent(cfg).to(torch.device("cpu"))
    agent.eval()
    out = {"env_seed": env_seed, "k": k, "agent_seed": agent_seed, "world_dim": int(cfg.latent.world_dim)}
    # 3. dev epoch
    h = StepHarness(agent, env, train_mode=False, seed=agent_seed)
    _f, obs = env.reset(); agent.reset(); h.reset()
    dev_ends = 0
    for i in range(dev):
        r = h.step(obs)
        obs = r.next_obs_dict
        if r.done:
            dev_ends += 1
            _f, obs = env.reset(); agent.reset(); h.reset()
    out["dev_steps"] = dev; out["dev_episode_ends"] = dev_ends; out["t_dev_s"] = round(time.time() - t0, 1)
    # 4. P0a warmup
    t1 = time.time()
    from experiments._lib.zworld_p0_warmup import run_zworld_p0
    from experiments._lib.capability_eval import RandomPolicy
    from ree_core.latent.zworld_p0 import ZWorldP0Config
    wenv = CausalGridWorldV2(seed=env_seed, **ENV_KW)
    wdiag = run_zworld_p0(agent, wenv, seed=agent_seed, episodes=20, steps_per_episode=50,
                          policy=RandomPolicy(agent_seed), label="rt5", dry_run=False,
                          config=ZWorldP0Config(preservation_weight=1000.0))
    agent.eval()
    out["t_warm_s"] = round(time.time() - t1, 1)
    out["warmup_keys"] = sorted(list(wdiag.keys()))[:20] if isinstance(wdiag, dict) else None
    # 5. closed loop
    t2 = time.time()
    h = StepHarness(agent, env, train_mode=False, seed=agent_seed)
    _f, obs = env.reset(); agent.reset(); h.reset()
    rew, tts, ends, acts = [], [], [], []
    stratum = None
    stopped_early = False
    for i in range(closed):
        r = h.step(obs)
        rew.append(float(r.harm_signal))
        info = r.info if isinstance(r.info, dict) else {}
        tts.append(str(info.get("transition_type", "none")))
        try:
            acts.append(int(r.action.detach().reshape(-1).argmax()))
        except Exception:
            acts.append(-1)
        obs = r.next_obs_dict
        if r.done:
            ends.append([i, str(info.get("done_cause", ""))])
            _f, obs = env.reset(); agent.reset(); h.reset()
        if i == STRATUM_WINDOW - 1:
            stratum, early = classify(ends)
            out["stratum"] = stratum; out["early_terminations_600"] = early
            out["t_to_600_s"] = round(time.time() - t0, 1)
            log("  arm k=%d seed=%d stratum=%s early600=%d t=%.0fs" % (k, env_seed, stratum, early, time.time() - t0))
            if stop_at_classify_if is not None and stop_at_classify_if(stratum):
                stopped_early = True
                break
    n = len(rew)
    out["closed_steps_run"] = n; out["stopped_after_classify"] = stopped_early
    out["FIRST"] = window(rew, tts, 0, min(600, n))
    if n >= 3000:
        out["LAST"] = window(rew, tts, 2400, 3000)
    out["ends"] = ends
    out["action_counts"] = dict(Counter(acts))
    out["t_closed_s"] = round(time.time() - t2, 1); out["t_arm_s"] = round(time.time() - t0, 1)
    out["rew"] = [round(x, 5) for x in rew]
    out["tts"] = tts
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--env-seed", type=int, required=True)
    ap.add_argument("--need", default="benign,hazard_trapped",
                    help="strata still needing seeds; NATIVE of any other stratum stops after classify")
    ap.add_argument("--dev", type=int, default=2400)
    ap.add_argument("--closed", type=int, default=3000)
    ap.add_argument("--n-reseed", type=int, default=N_RESEED)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    need = set(x for x in a.need.split(",") if x)
    t0 = time.time()

    def log(m):
        print(m, flush=True)

    res = {"args": vars(a), "arms": {}}
    nat = run_arm(a.env_seed, 0, a.dev, a.closed, lambda st: st not in need, log)
    res["arms"]["NATIVE"] = nat
    res["stratum"] = nat.get("stratum")
    res["admitted"] = (res["stratum"] in need) and not nat["stopped_after_classify"]
    json.dump(res, open(a.out, "w"))
    if res["admitted"]:
        for k in range(1, a.n_reseed + 1):
            arm = run_arm(a.env_seed, k, a.dev, a.closed, None, log)
            res["arms"]["NATIVE-R%d" % k] = arm
            json.dump(res, open(a.out, "w"))
            log("  ARM R%d seed=%d stratum(own)=%s LAST reward/100 %.3f contacts/100 %.2f t=%.0fs"
                % (k, a.env_seed, arm.get("stratum"), arm["LAST"]["reward_per100"], arm["LAST"]["contacts_per100"],
                   time.time() - t0))
    res["t_total_s"] = round(time.time() - t0, 1)
    json.dump(res, open(a.out, "w"))
    log("DONE seed=%d stratum=%s admitted=%s t=%.0fs" % (a.env_seed, res["stratum"], res["admitted"], time.time() - t0))


if __name__ == "__main__":
    main()
