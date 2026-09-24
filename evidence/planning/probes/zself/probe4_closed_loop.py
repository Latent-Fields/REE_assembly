"""Probe 4 -- CLOSED-LOOP persistent intervention (D3 check).

From the same episode start (agent, env and RNG snapshot matched), run a whole eval
episode twice: control, and with the stream (z_self or z_world) replaced on EVERY
encode() call (zero, or matched-norm fixed random direction). Readouts: first tick at
which the committed action differs, fraction of ticks with a different action, episode
length, summed harm signal (env reward), resources consumed (info key if present).
usage: probe4_closed_loop.py <A|B> <untrained|fwdtrained|e1e2only> <seeds> <n_eps> <T>
"""
import sys, json, time
sys.path.insert(0, "/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/zself")
from zs_common import *

KIND, STATE = sys.argv[1], sys.argv[2]
SEEDS = [int(s) for s in sys.argv[3].split(",")]
N_EPS, T = int(sys.argv[4]), int(sys.argv[5])


def prep(seed):
    agent, env, cfg = build(KIND, seed)
    if STATE in ("fwdtrained", "e1e2only"):
        import probe3_objectives as P3
        if STATE == "fwdtrained":
            eps3 = P3.record_random(CausalGridWorldV2(seed=seed, **A_ENV), 20, 100, random.Random(seed))
            agent.train(); P3.zself_p0(agent, "fwd", eps3, random.Random(seed + 1))
        P3.e1e2_p0(agent, CausalGridWorldV2(seed=seed, **A_ENV), seed)
        env = CausalGridWorldV2(seed=seed + 3000, **A_ENV)
    agent.eval()
    # flush training-time graph-carrying buffer entries (as probe 2's bank phase does)
    h = StepHarness(agent, env, train_mode=False, seed=seed)
    _, o = env.reset(); agent.reset(); h.reset()
    for _ in range(40):
        r = h.step(o); o = r.next_obs_dict
        if r.done:
            break
    return agent, env


def episode(agent, env, obs, snap, stream=None, kind=None, seed=0):
    import copy as _c
    a = dcopy(agent); e = _c.deepcopy(env)
    rng_restore(snap)
    if stream is not None:
        g = torch.Generator().manual_seed(seed)
        d = torch.randn(1, 32, generator=g); d = d / d.norm()
        ls = a.latent_stack; orig = ls.encode
        def enc(*aa, **kk):
            o = orig(*aa, **kk); z = getattr(o, stream)
            setattr(o, stream, torch.zeros_like(z) if kind == "zero" else (d.reshape(z.shape) * z.norm()))
            return o
        ls.encode = enc
    h = StepHarness(a, e, train_mode=False, seed=seed)
    acts, harm, n_res = [], 0.0, 0
    o = _c.deepcopy(obs)
    for t in range(T):
        r = h.step(o); o = r.next_obs_dict
        acts.append(int(r.action.argmax())); harm += float(r.harm_signal)
        n_res += int(isinstance(r.info, dict) and r.info.get("transition_type") == "resource")
        if r.done:
            break
    return acts, harm, n_res


def main():
    t0 = time.time(); rows = []
    for seed in SEEDS:
        agent, env = prep(seed)
        for ep in range(N_EPS):
            _, obs = env.reset(); agent.reset()
            snap = rng_snap()
            base = episode(agent, env, obs, snap, seed=seed)
            base2 = episode(agent, env, obs, snap, seed=seed)
            row = {"seed": seed, "ep": ep, "len": len(base[0]), "harm": base[1], "res": base[2],
                   "det_identical": base2[0] == base[0]}
            for st in ["z_self", "z_world"]:
                for k in ["zero", "noise"]:
                    x = episode(agent, env, obs, snap, st, k, seed=seed * 100 + ep)
                    n = min(len(x[0]), len(base[0]))
                    diff = [x[0][i] != base[0][i] for i in range(n)]
                    row[f"{st}.{k}"] = {"first_div": (diff.index(True) if any(diff) else None),
                                        "frac_diff": round(sum(diff) / max(1, n), 4),
                                        "len": len(x[0]), "harm": round(x[1], 4), "res": x[2]}
            rows.append(row)
            env.reset()
        print("seed", seed, "done %.0fs" % (time.time() - t0), flush=True)
    fn = "/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/zself/probe4_%s_%s.json" % (KIND, STATE)
    json.dump(rows, open(fn, "w"), indent=1)
    for r in rows:
        print(json.dumps(r))
    print("elapsed %.0fs" % (time.time() - t0))


main()
