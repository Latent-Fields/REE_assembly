"""POST-HOC DIAGNOSTIC (not pre-registered; numbers never replace the pre-registered verdicts).

Worker J (bt0925-decoder-probe). For one seed's saved states (encoder, head A, DEC and DEC-SHUF
decoders from decoder_probe.py), trace what the decoder receives and emits inside the native CEM
loop, per CEM iteration, at 20 states taken from a NATIVE-decoder waking run (same states for every
decoder). Wraps HippocampalModule._decode_action_objects on the live instance to record input norm,
output norm and first-step argmax class of each call; no other behaviour is changed.
ASCII-only output.
"""
import argparse, json, sys
from collections import Counter
from pathlib import Path
import numpy as np
import torch

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "ree-v3-wt")); sys.path.insert(0, str(HERE / "ree-v3-wt" / "experiments")); sys.path.insert(0, str(HERE))
from experiments._harness import StepHarness  # noqa: E402
import rollout_fidelity_probe as R  # noqa: E402
import balanced_replay_probe as BP  # noqa: E402
torch.set_num_threads(2)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--seed", type=int, required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    st = torch.load(HERE / "results" / ("DEC_s%d_states.pt" % a.seed), weights_only=False)
    R.seed_all(a.seed)
    env, agent, cfg = R.build_B(a.seed, False)
    agent.latent_stack.load_state_dict(st["enc"]); BP.set_head(agent, st["headA"]); agent.eval()
    native_dec = {k: v.clone() for k, v in agent.hippocampal.action_object_decoder.state_dict().items()}
    h = StepHarness(agent, env, train_mode=False, seed=a.seed)
    _f, obs = env.reset(); agent.reset(); h.reset(); log = []
    for _ in range(200):
        r = h.step(obs); log.append((r.latent.z_world.detach().clone(), r.latent.z_self.detach().clone())); obs = r.next_obs_dict
        if r.done:
            _f, obs = env.reset(); agent.reset(); h.reset()
    idx = np.linspace(0, len(log) - 1, 20).astype(int).tolist()
    hip = agent.hippocampal; iters = int(hip.config.num_cem_iterations)
    orig = hip._decode_action_objects
    out = {"seed": a.seed, "num_cem_iterations": iters, "decoders": {}}
    for name, sd in (("NATIVE", native_dec), ("DEC", st["dec"]), ("DEC-SHUF", st["shuf"])):
        hip.action_object_decoder.load_state_dict(sd)
        rec = []

        def wrapped(ao, _o=orig):
            y = _o(ao)
            rec.append((float(ao[:, 0, :].norm(dim=-1).mean()), float(y[:, 0, :].norm(dim=-1).mean()), int(y[0, 0, :].argmax())))
            return y
        hip._decode_action_objects = wrapped
        per_it = [{"in": [], "out": [], "cls": Counter()} for _ in range(iters)]
        final_cls = []
        try:
            for j, t in enumerate(idx):
                rec.clear(); torch.manual_seed(a.seed * 1000 + j)
                with torch.no_grad():
                    pool = hip.propose_trajectories(log[t][0], z_self=log[t][1])
                n = len(rec) // iters
                for it in range(iters):
                    for (i_n, o_n, c) in rec[it * n:(it + 1) * n]:
                        per_it[it]["in"].append(i_n); per_it[it]["out"].append(o_n); per_it[it]["cls"][c] += 1
                cc = Counter(hip.candidate_first_action_class(tr) for tr in pool)
                final_cls.append(cc.most_common(1)[0][0])
        finally:
            hip._decode_action_objects = orig
        out["decoders"][name] = {
            "per_iteration": [{"iter": it, "ao_input_norm_median": float(np.median(p["in"])), "decoded_norm_median": float(np.median(p["out"])),
                               "decoded_norm_max": float(np.max(p["out"])),
                               "first_class_counts": {str(k): v for k, v in sorted(p["cls"].items())}} for it, p in enumerate(per_it)],
            "final_pool_majority_class_by_state": {str(k): v for k, v in sorted(Counter(final_cls).items())}}
        print("%-9s %s" % (name, json.dumps(out["decoders"][name])), flush=True)
    json.dump(out, open(a.out, "w"), indent=1)


if __name__ == "__main__":
    main()
