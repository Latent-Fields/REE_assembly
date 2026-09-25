"""A1 v3 O12 env-only stratum classifier pilot (bt0925-a1v3). Env steps only -- no agent, no torch model.

Rule under test (user decision rec-20260925-a6132a2d): hazard_trapped is classified from a FIXED-SEED
RandomPolicy rollout on the env seed, so agent init cannot move it.
  env = CausalGridWorldV2(A1 ENV_KW, seed=s); policy = RandomPolicy(seed=s) (a function of s only).
  Roll CLS_STEPS steps, reset on done; count episodes that END inside the window with length < 200.
Pilot seeds 2001-2040 (RT-5's range; 2001-2008 have NATIVE strata from RT-5 332ab3f7f8). Also reports the
same count under 4 other policy seeds (s+1..s+4) to show how much policy randomness moves it, and a
3000-step count. ASCII output.
"""
import json
import sys

sys.path.insert(0, ".")
from ree_core.environment.causal_grid_world import CausalGridWorldV2  # noqa: E402
from experiments._lib.capability_eval import RandomPolicy  # noqa: E402

ENV_KW = dict(size=8, num_hazards=2, num_resources=3, max_episode_steps=200,
              proximity_approach_magnitude_tiebreak=True)
EP_CAP = 200
RT5_NATIVE = {2001: ("t", 58), 2002: ("b", None), 2003: ("b", None), 2004: ("b", None), 2005: ("b", None),
              2006: ("b", None), 2007: ("t", 22), 2008: ("t", 40)}


def early_count(env_seed, policy_seed, steps):
    env = CausalGridWorldV2(seed=env_seed, **ENV_KW)
    pol = RandomPolicy(policy_seed)
    _f, obs = env.reset()
    prev, early, causes = -1, 0, {}
    for i in range(steps):
        _flat, _h, done, info, obs = env.step(pol.act(env, obs))
        if done:
            if i - prev < EP_CAP:
                early += 1
                c = str(info.get("done_cause", "")) if isinstance(info, dict) else ""
                causes[c] = causes.get(c, 0) + 1
            prev = i
            _f, obs = env.reset()
    return early, causes


def main():
    rows = []
    for s in range(2001, 2041):
        e600, causes = early_count(s, s, 600)
        alt = [early_count(s, s + j, 600)[0] for j in range(1, 5)]
        e3000, _ = early_count(s, s, 3000)
        rows.append(dict(seed=s, early600=e600, early600_alt_policy_seeds=alt, early3000=e3000, causes600=causes,
                         rt5_native=RT5_NATIVE.get(s)))
        print("seed %d early600=%3d alt=%s early3000=%4d rt5=%s causes=%s"
              % (s, e600, alt, e3000, RT5_NATIVE.get(s), causes))
    json.dump(rows, open("../env_only_classifier_pilot.json", "w"), indent=1)
    print("DONE")


if __name__ == "__main__":
    main()
