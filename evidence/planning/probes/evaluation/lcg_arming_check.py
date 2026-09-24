"""ADDENDUM 3 STEP 0 (empirical half of the producer trace): with use_learned_channel_gating on, in this
harness's regime (tiebreak ON, R5b scaffold + R2 depth 2, trained SD-070 encoder is not needed for arming),
does E3.select ever register a modulatory channel (_lcg_terms non-empty -> eligibility written ->
_lcg_pending armed), and does w_chan ever move? Wraps E3.select to record score_bias presence and the
eligibility trace; counts post_action_update w_chan writes. ASCII-only output."""
import functools, json, sys
from pathlib import Path
import numpy as np
import torch
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "ree-v3-wt")); sys.path.insert(0, str(HERE / "ree-v3-wt" / "experiments")); sys.path.insert(0, str(HERE))
from experiments._harness import StepHarness  # noqa: E402
import rollout_fidelity_probe as R  # noqa: E402
torch.set_num_threads(2)
R.CausalGridWorldV2 = functools.partial(R.CausalGridWorldV2, proximity_approach_magnitude_tiebreak=True)
out = {}
for seed in (42, 43):
    R.seed_all(seed)
    env, agent, cfg = R.build_B(seed, False)
    agent.hippocampal.config.use_action_class_scaffold_candidates = True
    agent.e3._score_depth_limit = 2
    agent.e3.config.use_learned_channel_gating = True
    agent.eval()
    e3 = agent.e3; w0 = e3.w_chan.clone()
    stats = {"selects": 0, "score_bias_not_none": 0, "pending_true_after_select": 0, "elig_nonzero_after_select": 0}
    orig = e3.select
    def wrapped(*a, **k):
        stats["selects"] += 1
        if k.get("score_bias") is not None:
            stats["score_bias_not_none"] += 1
        r = orig(*a, **k)
        stats["pending_true_after_select"] += int(bool(e3._lcg_pending))
        stats["elig_nonzero_after_select"] += int(float(e3._lcg_elig_trace.abs().sum()) > 0)
        return r
    e3.select = wrapped
    h = StepHarness(agent, env, train_mode=False, seed=seed)
    _f, obs = env.reset(); agent.reset(); h.reset()
    for _ in range(300):
        r = h.step(obs); obs = r.next_obs_dict
        if r.done:
            _f, obs = env.reset(); agent.reset(); h.reset()
    stats.update({"w_chan_init": w0.tolist(), "w_chan_end": e3.w_chan.tolist(), "lcg_n_updates": int(e3._lcg_n_updates),
                  "elig_trace_end": e3._lcg_elig_trace.tolist(), "v_hat": float(e3._lcg_value_baseline),
                  "channels": ["score_bias", "mech341", "route"]})
    out[seed] = stats
    print("SEED %d %s" % (seed, json.dumps(stats)), flush=True)
json.dump(out, open(HERE / "results" / "LCG_arming_check.json", "w"), indent=1)
