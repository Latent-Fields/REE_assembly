"""Probe 3 -- MINIMAL prototypes of candidate z_self training objectives (config A, DR-13 ON).

Probe code only; nothing here is a ree_core change. Every objective is a PHASED trainer
(SD-070 style): it runs its OWN forward passes through the NATIVE encode path
(agent.body_obs_encoder -> LatentStack.encode, incl. top-down, precision and the DR-13
GRU; E1 anchor absent) over RECORDED random-policy observation chunks (B=16 x L=16),
with a fresh detached init state per chunk, so no graph survives an optimizer step
(the retained-graph / in-place hazard is avoided by construction). Optimizer holds ONLY
the z_self path (body_obs_encoder, self_encoder, self_topdown, self_precision_logit,
self_recurrence) + the objective's own head.

Candidates:
  base     no z_self objective (E1/E2 P0 only -- the V3-EXQ-1078 recipe)
  fwd      (i)  body forward model: head([z_self_t, a_t]) -> body_obs_{t+1}   (MSE)
  contr    (ii) temporal InfoNCE between successive stateful z_self (proj, tau 0.1)
  livetap  (iv) E2 motor-sensory loss through LIVE z_self:
                e2.predict_next_self(z_self_t, a_t) vs z_self_{t+1}, both undetached
                (the "let the existing replay loss train through a live tap" route)
  anchor   (iii) match live z_self_{t+1} to the (detached) E1-predicted-next z_self,
                run AFTER E1/E2 P0 so E1 is a trained predictor
Pipeline per candidate: z_self P0 (N_UPD updates) -> E1/E2 P0 (1078 recipe) ; anchor: E1/E2 P0 -> anchor P0.
Readouts: (a) param deltas; (b) held-out info: ridge probe (5-fold by episode) from native
stateful z_self on a HELD-OUT env seed (seed+1000) -> next body core [x,y,health,energy,
footprint]_{t+1}, current body core, and action_{t-2} (memory); collapse stats;
(c) consumer response: one-tick z_self interventions (zero / matched-norm noise / swap)
-> E1 prior rel change (every tick) and committed-action change rate at E3 ticks.
usage: probe3_objectives.py <seed> [n_upd] [cands comma]
"""
import sys, json, time
sys.path.insert(0, "/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/zself")
from zs_common import *
import torch.nn as nn
import torch.nn.functional as F

SEED = int(sys.argv[1]) if __name__ == "__main__" else 0
N_UPD = int(sys.argv[2]) if (__name__ == "__main__" and len(sys.argv) > 2) else 300
CANDS = sys.argv[3].split(",") if (__name__ == "__main__" and len(sys.argv) > 3) else ["base", "fwd", "contr", "livetap", "anchor"]
E1E2_EPS, E1E2_STEPS = int(os.environ.get("ZS_E1E2_EPS", 6)), 100
B, L = 16, 16
ACT_DIM = CausalGridWorldV2(seed=0, **A_ENV).action_dim


def record_random(env, n_eps, T, rs):
    eps = []
    for _ in range(n_eps):
        _, obs = env.reset()
        bod, wor, act = [obs["body_state"].reshape(-1).float()], [obs["world_state"].reshape(-1).float()], []
        for t in range(T):
            a = torch.zeros(ACT_DIM); a[rs.randint(0, ACT_DIM - 1)] = 1.0
            _, _, done, _, obs = env.step(a.unsqueeze(0))
            act.append(a); bod.append(obs["body_state"].reshape(-1).float()); wor.append(obs["world_state"].reshape(-1).float())
            if done:
                break
        if len(act) >= L + 1:
            eps.append((torch.stack(bod), torch.stack(wor), torch.stack(act)))
    return eps


def sample_chunks(eps, rs):
    bs, ws, as_ = [], [], []
    for _ in range(B):
        bb, ww, aa = eps[rs.randrange(len(eps))]
        s = rs.randrange(0, len(aa) - L)
        bs.append(bb[s:s + L + 1]); ws.append(ww[s:s + L + 1]); as_.append(aa[s:s + L])
    return torch.stack(bs), torch.stack(ws), torch.stack(as_)   # [B,L+1,*],[B,L+1,*],[B,L,4]


def native_chain(agent, bb, ww, aa):
    """Own forward pass through the native encode path over a chunk. Returns stateful
    z_self [B,L+1,sd] and z_world [B,L+1,wd] (live graph, chunk-local)."""
    ls = agent.latent_stack
    prev = ls.init_state(bb.shape[0], bb.device)
    zs, zw = [], []
    for t in range(bb.shape[1]):
        enc = torch.cat([agent.body_obs_encoder(bb[:, t]), agent.world_obs_encoder(ww[:, t])], dim=-1)
        pa = aa[:, t - 1] if t > 0 else None
        st = ls.encode(enc, prev, prev_action=pa)
        zs.append(st.z_self); zw.append(st.z_world)
        prev = st
    return torch.stack(zs, 1), torch.stack(zw, 1)


def self_path_params(agent):
    names = set(self_param_names(agent)) - {n for n in self_param_names(agent) if "self_predictor" in n}
    ps = [p for n, p in agent.named_parameters() if n in names]
    ps += list(agent.body_obs_encoder.parameters())
    return ps


def zself_p0(agent, kind, eps, rs):
    sd = agent.config.latent.self_dim
    bd = eps[0][0].shape[-1]
    heads = nn.ModuleList()
    if kind == "fwd":
        head = nn.Sequential(nn.Linear(sd + ACT_DIM, 64), nn.ReLU(), nn.Linear(64, bd)); heads.append(head)
    elif kind == "contr":
        head = nn.Linear(sd, sd); heads.append(head)
    params = self_path_params(agent) + list(heads.parameters())
    if kind == "livetap":
        params += list(agent.e2.parameters())
    opt = torch.optim.Adam(params, lr=1e-3)
    losses = []
    for u in range(N_UPD):
        bb, ww, aa = sample_chunks(eps, rs)
        zs, zw = native_chain(agent, bb, ww, aa)
        if kind == "fwd":
            pred = head(torch.cat([zs[:, :-1], aa], -1))
            loss = F.mse_loss(pred, bb[:, 1:])
        elif kind == "contr":
            p = F.normalize(head(zs), dim=-1)
            q = p[:, :-1].reshape(-1, sd); k = p[:, 1:].reshape(-1, sd)
            logits = q @ k.t() / 0.1
            loss = F.cross_entropy(logits, torch.arange(q.shape[0]))
        elif kind == "livetap":
            pred = agent.e2.predict_next_self(zs[:, :-1].reshape(-1, sd), aa.reshape(-1, ACT_DIM))
            loss = F.mse_loss(pred, zs[:, 1:].reshape(-1, sd))
        elif kind == "anchor":
            saved = agent.e1._hidden_state; agent.e1.reset_hidden_state()
            tgts = []
            with torch.no_grad():
                for t in range(L):
                    preds, _ = agent.e1(torch.cat([zs[:, t], zw[:, t]], -1).detach())
                    tgts.append(agent.e1.split_prediction(preds[:, 0, :])[0])
            agent.e1._hidden_state = saved
            loss = F.mse_loss(zs[:, 1:], torch.stack(tgts, 1))
        opt.zero_grad(); loss.backward(); opt.step()
        losses.append(float(loss.detach()))
    return {"loss_first10": float(np.mean(losses[:10])), "loss_last10": float(np.mean(losses[-10:]))}


def e1e2_p0(agent, env, seed):
    opt = torch.optim.Adam(agent.parameters(), lr=1e-3)
    h = StepHarness(agent, env, train_mode=True, seed=seed); agent.train()
    for ep in range(E1E2_EPS):
        _, obs = env.reset(); agent.reset(); h.reset()
        for _ in range(E1E2_STEPS):
            r = h.step(obs); obs = r.next_obs_dict
            loss = agent.compute_prediction_loss() + agent.compute_e2_loss()
            if loss.requires_grad:
                opt.zero_grad(); loss.backward(); opt.step()
            if r.done:
                break


def heldout_collect(agent, seed):
    env = CausalGridWorldV2(seed=seed + 1000, **A_ENV)
    rs = random.Random(seed + 7)
    agent.eval(); rows = []
    with torch.no_grad():
        for ep in range(10):
            _, obs = env.reset(); agent.reset()
            acts = []
            for t in range(60):
                lat = agent.sense(obs["body_state"], obs["world_state"])
                agent._e1_tick(lat)
                a = torch.zeros(1, ACT_DIM); a[0, rs.randint(0, ACT_DIM - 1)] = 1.0
                agent._last_action = a
                b_now = obs["body_state"].reshape(-1).float().clone()
                _, _, done, _, obs = env.step(a)
                b_next = obs["body_state"].reshape(-1).float().clone()
                acts.append(a.reshape(-1))
                rows.append(dict(ep=ep, t=t, z=lat.z_self.reshape(-1).clone(), b=b_now, bn=b_next,
                                 am2=(acts[-3] if len(acts) >= 3 else None)))
                if done:
                    break
    return rows


def ridge_cv(X, Y, groups, lam=1e-2):
    X = torch.cat([X, torch.ones(X.shape[0], 1)], 1)
    ug = sorted(set(groups)); folds = [ug[i::5] for i in range(5)]
    ss_res = torch.zeros(Y.shape[1]); ss_tot = torch.zeros(Y.shape[1])
    g = torch.tensor(groups)
    for f in folds:
        te = torch.isin(g, torch.tensor(f)); tr = ~te
        if te.sum() == 0 or tr.sum() < 5:
            continue
        Xt, Yt = X[tr].double(), Y[tr].double()
        W = torch.linalg.solve(Xt.t() @ Xt + lam * torch.eye(X.shape[1], dtype=torch.float64), Xt.t() @ Yt)
        P = X[te].double() @ W
        ss_res += ((Y[te].double() - P) ** 2).sum(0).float()
        ss_tot += ((Y[te].double() - Yt.mean(0)) ** 2).sum(0).float()
    keep = ss_tot > 1e-8
    return float((1 - ss_res[keep] / ss_tot[keep]).mean()) if keep.any() else None


def info_readout(rows):
    Z = torch.stack([r["z"] for r in rows]); Bn = torch.stack([r["b"] for r in rows])
    BN = torch.stack([r["bn"] for r in rows]); g = [r["ep"] for r in rows]
    core = [0, 1, 2, 3, 4]
    m = [i for i, r in enumerate(rows) if r["am2"] is not None]
    AM2 = torch.stack([rows[i]["am2"] for i in m])
    zc = Z - Z.mean(0)
    out = {
        "z_rel_spread": float(torch.cdist(Z, Z).mean() / (Z.norm(dim=1).mean() + 1e-9)),
        "z_dim_std_mean": float(Z.std(0).mean()), "z_norm_mean": float(Z.norm(dim=1).mean()),
        "z_eff_rank": float(torch.linalg.svdvals(zc).pow(2).sum() ** 2 / (torch.linalg.svdvals(zc).pow(4).sum() + 1e-12)),
        "R2_next_body_core": ridge_cv(Z, BN[:, core], g),
        "R2_cur_body_core": ridge_cv(Z, Bn[:, core], g),
        "R2_action_tminus2": ridge_cv(Z[m], AM2, [g[i] for i in m]),
        "ceiling_R2_next_body_core_from_raw_body_t": ridge_cv(Bn, BN[:, core], g),
        "ceiling_R2_action_tminus2_from_raw_body_t": ridge_cv(Bn[m], AM2, [g[i] for i in m]),
    }
    return out


def consumer_interventions(agent, seed, bank):
    import copy as _c
    env = CausalGridWorldV2(seed=seed + 2000, **A_ENV)
    agent.eval(); h = StepHarness(agent, env, train_mode=False, seed=seed)
    _, obs = env.reset(); agent.reset(); h.reset()
    res = {k: {"e1": [], "act_e3": []} for k in ["zero", "noise", "swap"]}
    for t in range(60):
        if t < 5:
            r = h.step(obs); obs = r.next_obs_dict
            if r.done: break
            continue
        snap = rng_snap()
        outs = {}
        for k in [None, "zero", "noise", "swap"]:
            a = dcopy(agent); e = _c.deepcopy(env)
            memo = {id(agent): a, id(env): e}
            rm = getattr(agent.hippocampal, "_rng", None)
            if rm is not None: memo[id(rm)] = rm
            hh = _c.deepcopy(h, memo); hh.agent, hh.env = a, e
            rng_restore(snap)
            if k is not None:
                gen = torch.Generator().manual_seed(seed * 1000 + t)
                def fn(z, k=k, gen=gen):
                    if k == "zero": return torch.zeros_like(z)
                    if k == "noise":
                        d = torch.randn(z.shape, generator=gen); return d / (d.norm() + 1e-12) * z.norm()
                    return bank[(seed * 1000 + t) % len(bank)].clone().reshape(z.shape)
                ls = a.latent_stack; orig = ls.encode
                def enc(*aa, _o=orig, _f=fn, **kk):
                    o = _o(*aa, **kk); o.z_self = _f(o.z_self); return o
                ls.encode = enc
            rec = {}
            o1 = a._e1_tick
            def e1w(lat, _o=o1, _r=rec):
                p = _o(lat); _r["e1"] = p.detach().reshape(-1).clone(); return p
            a._e1_tick = e1w
            r = hh.step(_c.deepcopy(obs))
            outs[k] = (a, e, hh, r, rec.get("e1"), int(r.action.argmax()), bool(r.ticks.get("e3_tick")))
            if k is None:
                post = rng_snap()
        c = outs[None]
        for k in ["zero", "noise", "swap"]:
            o = outs[k]
            if c[4] is not None and o[4] is not None:
                res[k]["e1"].append(float((o[4] - c[4]).norm() / (c[4].norm() + 1e-9)))
            if c[6]:
                res[k]["act_e3"].append(o[5] != c[5])
        agent, env, h = c[0], c[1], c[2]
        rng_restore(post); obs = c[3].next_obs_dict
        if c[3].done:
            break
    return {k: {"e1_rel_mean": (float(np.mean(v["e1"])) if v["e1"] else None),
                "act_change_rate_e3": (float(np.mean(v["act_e3"])) if v["act_e3"] else None),
                "n_e3": len(v["act_e3"])} for k, v in res.items()}


def snapshot(agent):
    return {n: p.detach().clone() for n, p in agent.named_parameters()}


def deltas(agent, s0):
    groups = {"self_encoder": ".self_encoder.", "self_recurrence_GRU": ".self_recurrence.",
              "self_topdown": ".self_topdown.", "self_precision_logit": "self_precision_logit",
              "body_obs_encoder": "body_obs_encoder."}
    out = {}
    for g, key in groups.items():
        v = [float((p.detach() - s0[n]).abs().max()) for n, p in agent.named_parameters() if key in n]
        out[g] = max(v) if v else None
    return out


def main():
    t0 = time.time()
    base_agent, env, cfg = build("A", SEED)
    rs = random.Random(SEED)
    rec_env = CausalGridWorldV2(seed=SEED, **A_ENV)
    train_eps = record_random(rec_env, 20, 100, rs)
    res = {"seed": SEED, "n_upd": N_UPD, "n_rec_eps": len(train_eps), "cands": {}}
    for cand in CANDS:
        torch.manual_seed(SEED); random.seed(SEED); np.random.seed(SEED)
        agent = dcopy(base_agent); env_c = CausalGridWorldV2(seed=SEED, **A_ENV)
        s0 = snapshot(agent); crs = random.Random(SEED + 1)
        p0 = None
        agent.train()
        if cand in ("fwd", "contr", "livetap"):
            p0 = zself_p0(agent, cand, train_eps, crs)
            d_after_p0 = deltas(agent, s0)
            e1e2_p0(agent, env_c, SEED)
        elif cand == "anchor":
            e1e2_p0(agent, env_c, SEED)
            s1 = snapshot(agent)
            p0 = zself_p0(agent, cand, train_eps, crs)
            d_after_p0 = deltas(agent, s1)
        else:
            e1e2_p0(agent, env_c, SEED)
            d_after_p0 = None
        rows = heldout_collect(agent, SEED)
        info = info_readout(rows)
        bank = [r["z"] for r in rows[:40]]
        cons = consumer_interventions(agent, SEED, bank)
        res["cands"][cand] = {"p0_loss": p0, "param_delta_after_zself_p0": d_after_p0,
                              "param_delta_total": deltas(agent, s0), "heldout_info": info,
                              "consumer": cons}
        print("[%s] seed %d done %.0fs" % (cand, SEED, time.time() - t0), flush=True)
        print(json.dumps(res["cands"][cand]), flush=True)
    fn = "/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/zself/probe3_seed%d.json" % SEED
    json.dump(res, open(fn, "w"), indent=1)
    print("wrote", fn, "%.0fs" % (time.time() - t0))


if __name__ == "__main__":
    main()
