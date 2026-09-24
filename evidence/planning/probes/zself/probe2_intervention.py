"""Probe 2 -- act-time INTERVENTION battery on z_self, with the IDENTICAL battery on z_world
as a canary (and as the CURRENT_FRONT D2-for-z_world row).

Per branched tick: fork (agent, env, harness) by deepcopy, restore the torch/numpy/python
RNG snapshot, and run ONE canonical StepHarness tick in which LatentStack.encode()'s
output stream (z_self or z_world) is replaced -- so EVERY downstream reader in sense(),
_e1_tick, generate_trajectories, select_action (live latent and the detached
_current_latent alike) sees the intervened value. Compared with a matched-RNG control
branch. A control-vs-control replay is recorded as the determinism check.

Interventions (one tick, one stream): zero; matched-norm random direction (dedicated
torch.Generator, so the global RNG stream is untouched); swap with the same stream from a
DIFFERENT episode (bank from an earlier episode of the same agent); coordinate permutation
(batch is 1, so "shuffle across batch" is realised as a fixed per-tick dim permutation that
preserves norm and the value multiset).

Readouts vs control: committed action changed; E3 last_scores relative L2 change; E1 prior
relative change; candidate first-step world state / self state relative change.

usage: probe2_intervention.py <A|B> <untrained|trained> [n_eval_eps] [ticks_per_ep]
"""
import sys, json, time, math
sys.path.insert(0, "/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/zself")
from zs_common import *

KIND = sys.argv[1]; STATE = sys.argv[2]
N_EPS = int(sys.argv[3]) if len(sys.argv) > 3 else 2
T_EP = int(sys.argv[4]) if len(sys.argv) > 4 else 50
SEEDS = [int(s) for s in (sys.argv[5].split(",") if len(sys.argv) > 5 else ["42", "43", "45"])]
WARM = 5
STREAMS = ["z_self", "z_world"]
KINDS = ["zero", "noise", "swap", "permute"]


def train_A(agent, env, seed, n_eps=10, steps=100):
    opt = torch.optim.Adam(agent.parameters(), lr=1e-3)
    h = StepHarness(agent, env, train_mode=True, seed=seed); agent.train()
    for ep in range(n_eps):
        _, obs = env.reset(); agent.reset(); h.reset()
        for _ in range(steps):
            r = h.step(obs); obs = r.next_obs_dict
            loss = agent.compute_prediction_loss() + agent.compute_e2_loss()
            if loss.requires_grad:
                opt.zero_grad(); loss.backward(); opt.step()
            if r.done:
                break


def train_B(agent, env, seed):
    from experiments._lib.allon_training import _train_all_on_agent
    import experiments.v3_exq_724_competence_localization_diagnostic as x724
    return _train_all_on_agent(agent, env, seed, p0_episodes=3, p1_episodes=3,
                               steps_per_episode=100, rung_id="probe", total_denominator=6)


def make_intervention(stream, kind, bank, tick_seed):
    g = torch.Generator().manual_seed(tick_seed)
    def f(z):
        if kind == "zero":
            return torch.zeros_like(z)
        if kind == "noise":
            d = torch.randn(z.shape, generator=g)
            return d / (d.norm() + 1e-12) * z.norm()
        if kind == "swap":
            src = bank[stream][tick_seed % len(bank[stream])]
            return src.clone().reshape(z.shape)
        if kind == "permute":
            perm = torch.randperm(z.shape[-1], generator=g)
            return z[..., perm]
        raise ValueError(kind)
    return f


def install(agent, stream, fn):
    ls = agent.latent_stack
    orig = ls.encode
    def enc(*a, **k):
        out = orig(*a, **k)
        setattr(out, stream, fn(getattr(out, stream)))
        return out
    ls.encode = enc


def instrument(agent):
    rec = {}
    o_e1 = agent._e1_tick
    def e1(latent):
        p = o_e1(latent); rec["e1"] = p.detach().clone().reshape(-1); return p
    agent._e1_tick = e1
    o_gt = agent.generate_trajectories
    def gt(*a, **k):
        c = o_gt(*a, **k); rec["cands"] = c; return c
    agent.generate_trajectories = gt
    return rec


def cand_vecs(cands):
    if not cands:
        return None, None
    w = torch.stack([c.world_states[1].detach().reshape(-1) if c.world_states and len(c.world_states) > 1
                     else torch.zeros(1) for c in cands])
    s = torch.stack([c.states[1].detach().reshape(-1) if c.states and len(c.states) > 1
                     else torch.zeros(1) for c in cands])
    return w, s


def rel(a, b):
    if a is None or b is None or a.shape != b.shape:
        return None
    return float((a - b).norm() / (b.norm() + 1e-9))


def run_branch(agent, env, h, obs, snap, stream=None, fn=None):
    a, e = dcopy(agent), copy.deepcopy(env)
    memo = {id(agent): a, id(env): e}
    rng_mod = getattr(getattr(agent, "hippocampal", None), "_rng", None)
    if rng_mod is not None:
        memo[id(rng_mod)] = rng_mod
    hh = copy.deepcopy(h, memo)
    hh.agent, hh.env = a, e
    rng_restore(snap)
    if stream is not None:
        install(a, stream, fn)
    rec = instrument(a)
    r = hh.step(copy.deepcopy(obs))
    sc = getattr(a.e3, "last_scores", None)
    sc = sc.detach().clone().reshape(-1) if isinstance(sc, torch.Tensor) else None
    w, s = cand_vecs(rec.get("cands"))
    return dict(agent=a, env=e, h=hh, r=r, action=int(r.action.argmax().item()),
                scores=sc, e1=rec.get("e1"), cw=w, cs=s, ticks=dict(r.ticks))


def main():
    out = {"kind": KIND, "state": STATE, "seeds": SEEDS, "n_eps": N_EPS, "t_ep": T_EP, "rows": []}
    t0 = time.time()
    for seed in SEEDS:
        agent, env, cfg = build(KIND, seed)
        if STATE == "trained":
            (train_A if KIND == "A" else train_B)(agent, env, seed)
        elif STATE in ("fwdtrained", "e1e2only"):
            import probe3_objectives as P3
            if STATE == "fwdtrained":
                eps3 = P3.record_random(CausalGridWorldV2(seed=seed, **A_ENV), 20, 100, random.Random(seed))
                agent.train(); P3.zself_p0(agent, "fwd", eps3, random.Random(seed + 1))
            P3.e1e2_p0(agent, CausalGridWorldV2(seed=seed, **A_ENV), seed)
            env = CausalGridWorldV2(seed=seed + 2000, **A_ENV)
        agent.eval()
        h = StepHarness(agent, env, train_mode=False, seed=seed)
        # bank: z_self / z_world from a separate episode of this agent (swap source)
        bank = {"z_self": [], "z_world": []}
        _, obs = env.reset(); agent.reset(); h.reset()
        for t in range(40):
            r = h.step(obs); obs = r.next_obs_dict
            bank["z_self"].append(r.latent.z_self.detach().clone())
            bank["z_world"].append(r.latent.z_world.detach().clone())
            if r.done:
                break
        for st in STREAMS:
            B = torch.stack([b.reshape(-1) for b in bank[st]])
            mn = float(B.norm(dim=1).mean())
            pd = float(torch.cdist(B, B).mean())
            out.setdefault("bank_spread", []).append({"seed": seed, "stream": st, "mean_norm": round(mn, 5),
                                                      "mean_pairwise_dist": round(pd, 5),
                                                      "rel_spread": round(pd / (mn + 1e-9), 5)})
        for ep in range(N_EPS):
            _, obs = env.reset(); agent.reset(); h.reset()
            for t in range(T_EP):
                if t < WARM:
                    r = h.step(obs); obs = r.next_obs_dict
                    if r.done: break
                    continue
                snap = rng_snap()
                ctl = run_branch(agent, env, h, obs, snap)
                post = rng_snap()
                if os.environ.get("ZS_E3_ONLY") and not ctl["ticks"].get("e3_tick"):
                    agent, env, h = ctl["agent"], ctl["env"], ctl["h"]
                    rng_restore(post); obs = ctl["r"].next_obs_dict
                    if ctl["r"].done:
                        break
                    continue
                ctl2 = run_branch(agent, env, h, obs, snap)
                row = {"seed": seed, "ep": ep, "t": t, "e3_tick": bool(ctl["ticks"].get("e3_tick")),
                       "e1_tick": bool(ctl["ticks"].get("e1_tick")),
                       "det_action_same": ctl2["action"] == ctl["action"],
                       "det_score_rel": rel(ctl2["scores"], ctl["scores"])}
                for st in STREAMS:
                    for k in KINDS:
                        fn = make_intervention(st, k, bank, seed * 100000 + ep * 1000 + t)
                        br = run_branch(agent, env, h, obs, snap, st, fn)
                        row[f"{st}.{k}.act"] = br["action"] != ctl["action"]
                        row[f"{st}.{k}.score"] = rel(br["scores"], ctl["scores"])
                        row[f"{st}.{k}.e1"] = rel(br["e1"], ctl["e1"])
                        row[f"{st}.{k}.cw"] = rel(br["cw"], ctl["cw"])
                        row[f"{st}.{k}.cs"] = rel(br["cs"], ctl["cs"])
                out["rows"].append(row)
                agent, env, h = ctl["agent"], ctl["env"], ctl["h"]
                rng_restore(post)
                obs = ctl["r"].next_obs_dict
                if ctl["r"].done:
                    break
        print("seed %d done, %d rows, %.0fs" % (seed, len(out["rows"]), time.time() - t0), flush=True)
    # summary
    rows = out["rows"]
    def agg(key, sub=None):
        vals = [r[key] for r in rows if (sub is None or sub(r)) and r.get(key) is not None]
        if not vals: return None
        if isinstance(vals[0], bool): return round(sum(vals) / len(vals), 4)
        vals = sorted(vals); return {"mean": round(sum(vals) / len(vals), 5), "max": round(vals[-1], 5)}
    summ = {"n_rows": len(rows), "n_e3_tick_rows": sum(r["e3_tick"] for r in rows),
            "determinism_action_same": agg("det_action_same"), "determinism_score_rel": agg("det_score_rel")}
    for st in STREAMS:
        for k in KINDS:
            p = f"{st}.{k}"
            summ[p] = {"act_changed_all": agg(p + ".act"),
                       "act_changed_e3tick": agg(p + ".act", lambda r: r["e3_tick"]),
                       "score_rel": agg(p + ".score", lambda r: r["e3_tick"]),
                       "e1_rel": agg(p + ".e1", lambda r: r["e1_tick"]),
                       "cand_world_rel": agg(p + ".cw", lambda r: r["e3_tick"]),
                       "cand_self_rel": agg(p + ".cs", lambda r: r["e3_tick"])}
    summ["bank_spread"] = out.get("bank_spread")
    out["summary"] = summ
    fn = "/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/zself/probe2_%s_%s%s.json" % (KIND, STATE, os.environ.get("ZS_TAG", ""))
    json.dump(out, open(fn, "w"), indent=1)
    print(json.dumps(summ, indent=1))
    print("elapsed %.0fs -> %s" % (time.time() - t0, fn))


main()
