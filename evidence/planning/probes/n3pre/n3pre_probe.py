"""Probe N3-pre (bt0925-n3pre, orchestrate-20260924-breakthrough, chip-20260925-coupled-n3-preprobe).

Which E3 horizon aggregation makes E3's pick track true consequence, using a PROXY W3 head?
PROVISIONAL for W4: the head here is a harness-trained proxy of the W3 member, not the member.

Pre-registration: REE_assembly/evidence/planning/n3_pre_e3_aggregation_probe_20260925.md
(committed BEFORE any registered seed ran). One invocation = one seed.

Per seed (babbling-probe regime: Phase-0 env CausalGridWorldV2 size 12, native z_world read
path of build_B, world_dim 32, random-init FROZEN encoder):
  1. D_L2  : structured babbling, class uniform over {0..4} (incl. stay=4) held for U{1..4}.
     D_SHUF: D_L2 with action labels permuted across timesteps.
     TE4   : held-out uniform {0..3} (the babbling-probe L2R-bar test set, unchanged).
     TEW   : held-out uniform {0..4} (disc5 and per-depth fidelity weights, H up to 30).
  2. PROXY heads (the W3 recipe = babbling probe's L2R):
       REAL = 3000 updates on D_L2, then 1200 closed-loop steps (fresh agent, native E3, head
              live) with 9000 online updates, each batch 25% D_L2 replay + 75% on-policy.
       SHUF = identical, but every action label it ever trains on is shuffled: D_SHUF for the
              pre-phase and the 25% replay, and on-policy labels resampled independently of
              the transition (label marginal kept, correspondence destroyed).
       INIT = the untrained head (reference for pick-flip).
  3. Probe states: fresh agent, REAL head live, native waking in env episode k=100; every
     EVERY steps at the StepHarness on_action hook: record the native CEM pool (RNG-neutral),
     clone the env per class c for the true next z_world (sense()'s encoder, side-effect-free;
     validated against the next sensed z), and env-Q(c) = mean over NCONT random continuations
     of summed env reward of [c, CLEN random steps] (ADDENDUM 3 estimator).
  4. Re-score. For every head and every candidate, J_L = native E3.score_trajectory with
     SD-081's knob _score_depth_limit = L, L = 2..31 (L=31 == full). Aggregations:
       FULL      J_31 (current)
       D1        J_2  (current state + one step; == the HABIT read at dualsystem_habit_depth 2)
       DISC_g    J_2 + sum_{d=2..30} g^(d-1) (J_{d+1} - J_d), g in {0.5, 0.8}
       FIDW      J_2 + sum_{d=2..30} w_d (J_{d+1} - J_d), w_d = 1 iff this head's median
                 rollout error at depth d beats persistence on TEW, else 0
     Scaffold pool (ADDENDUM 2 Measure 2): pool[0] with step-0 replaced by one-hot c, c=0..4.
     J_true(c) = E3 score of [z0, true z1(c)].
  Gates per aggregation (real minus shuffled, >= 4/5 seeds):
     (a) Spearman(J_pred, J_true) on the scaffold pool, mean over states: diff > 0.15
     (b) P(argmin J_pred in env-Q-best set) on the scaffold pool, informative states: diff > 0.10
     (c) P(argmin over the NATIVE pool differs from INIT head's argmin, same aggregation): diff > 0.15
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

HERE = Path(__file__).resolve().parent
WT = HERE / "ree-v3-wt"
sys.path.insert(0, str(HERE / "probes_src"))
sys.path.insert(0, str(WT / "experiments"))
sys.path.insert(0, str(WT))

import torch  # noqa: E402
import torch.nn.functional as F  # noqa: E402

torch.set_num_threads(2)

from experiments._harness import StepHarness, StepHooks  # noqa: E402
from ree_core.predictors.e2_fast import Trajectory  # noqa: E402
import rollout_fidelity_probe as R  # noqa: E402
import balanced_replay_probe as BP  # noqa: E402
import babble_probe as BB  # noqa: E402

A_ENV = 5
EP_STEPS = BB.EP_STEPS
PRE_UPD = 3000
POST_UPD = 9000
REPLAY_FRAC = 0.25
HMAX = 30
GAMMAS = (0.5, 0.8)
AGGS = ["D1", "DISC_0.5", "DISC_0.8", "FIDW", "FULL"]   # simplicity order (selection rule)
HABIT_LIMIT = 2  # max(2, dualsystem_habit_depth=2), e3_selector.py:2088


def pol_L2_5(seed):
    g = np.random.default_rng(seed * 7 + 2)
    st = {"c": 0, "left": 0}

    def f():
        if st["left"] <= 0:
            st["c"] = int(g.integers(0, 5)); st["left"] = int(g.integers(1, 5))
        st["left"] -= 1
        return st["c"]
    return f


def pol_uniform5(seed):
    g = np.random.default_rng(seed)
    return lambda: int(g.integers(0, 5))


# ------------------------------------------------------------------ post phase (L2R recipe)
def post_phase(seed, ref_enc, head, P, replay, shuffle_onpolicy):
    """babble_probe.post_phase verbatim, plus shuffle_onpolicy (SHUF twin) and the returned
    on-policy buffer (for the descriptive B0' retention baseline)."""
    agent = BB.fresh_agent(seed, ref_enc)
    BP.set_head(agent, head)
    R.seed_all(seed + 500)
    params = BP.head_params(agent)
    opt = torch.optim.Adam(params, lr=3e-4)
    bz0, ba, bz1 = [], [], []
    r0, r1, ra = replay
    roh = F.one_hot(ra, A_ENV).float()
    owed, done_upd, grad_ok = 0, 0, None
    rew, acts, early_flags, t, losses = [], [], [], 0, []
    for ep in range(P // EP_STEPS):
        env = BB.make_env(seed, 50 + ep)
        h = StepHarness(agent, env, train_mode=False, seed=seed * 1000 + 50 + ep)
        _f, od = env.reset(); agent.reset(); h.reset()
        prev = None
        for _s in range(EP_STEPS):
            r = h.step(od)
            z = r.latent.z_world.detach().reshape(1, -1).clone()
            a = int(r.action.detach().reshape(-1).argmax())
            if prev is not None:
                bz0.append(prev[0]); ba.append(prev[1]); bz1.append(z)
            prev = (z, a)
            rew.append(float(r.harm_signal)); acts.append(a); early_flags.append(bool(r.done))
            od = r.next_obs_dict
            if r.done:
                _f, od = env.reset(); agent.reset(); h.reset(); prev = None
            owed += (POST_UPD * (t + 1)) // P - (POST_UPD * t) // P
            t += 1
            if len(bz0) >= 64 and owed > 0:
                Z0 = torch.cat(bz0); Z1 = torch.cat(bz1); OH = F.one_hot(torch.tensor(ba), A_ENV).float()
                n = Z0.shape[0]
                with torch.enable_grad():
                    for _u in range(owed):
                        kr = int(round(32 * REPLAY_FRAC))
                        idx = torch.randint(0, n, (32 - kr,)); ridx = torch.randint(0, r0.shape[0], (kr,))
                        oh_on = OH[torch.randint(0, n, (32 - kr,))] if shuffle_onpolicy else OH[idx]
                        zb = torch.cat([Z0[idx], r0[ridx]]); ab = torch.cat([oh_on, roh[ridx]]); yb = torch.cat([Z1[idx], r1[ridx]])
                        loss = F.mse_loss(agent.e2.world_forward(zb, ab), yb)
                        opt.zero_grad(); loss.backward()
                        if grad_ok is None:
                            grad_ok = all(p.grad is not None and float(p.grad.abs().sum()) > 0 for p in params)
                        torch.nn.utils.clip_grad_norm_(params, 1.0); opt.step()
                        losses.append(float(loss.detach()))
                done_upd += owed
                owed = 0
    rw = np.asarray(rew)
    cc = Counter(acts)
    run = {"updates_done": done_upd, "grad_nonnull_first": grad_ok,
           "loss_last200": float(np.mean(losses[-200:])) if losses else None,
           "reward_per_100": float(rw.sum() * 100.0 / len(rw)),
           "harm_events_per_100": float((rw < 0).sum() * 100.0 / len(rw)),
           "benefit_events_per_100": float((rw > 0).sum() * 100.0 / len(rw)),
           "early_terminations": int(sum(early_flags)), "action_counts": {str(k): v for k, v in sorted(cc.items())},
           "action_entropy": BB.entropy(cc)}
    buf = (torch.cat(bz0), torch.cat(bz1), torch.tensor(ba))
    return BP.get_head(agent), run, buf


# ------------------------------------------------------------------ evaluation on TEW
@torch.no_grad()
def eval_tew(ref, head, te, seed, H=HMAX, max_starts=300):
    """Per-depth fidelity (median ||pred - true|| vs persistence) to H, disc5_h1, rollout norms."""
    BP.set_head(ref, head)
    e2 = ref.e2
    g = np.random.default_rng(seed + 91)
    starts = [(i, t) for i, e in enumerate(te) for t in range(e["a"].shape[0] - H + 1)]
    if len(starts) > max_starts:
        starts = [starts[j] for j in sorted(g.choice(len(starts), max_starts, replace=False))]
    zs = torch.zeros(1, 32)
    err = {h: [] for h in range(1, H + 1)}; pers = {h: [] for h in range(1, H + 1)}
    disc5, n1, n30 = [], [], []
    for i, t in starts:
        x = te[i]["z"]
        acts = F.one_hot(te[i]["a"][t:t + H], A_ENV).float().unsqueeze(0)
        x0 = x[t:t + 1]
        tr = e2.rollout_with_world(zs, x0, acts, compute_action_objects=False)
        for h in range(1, H + 1):
            y = x[t + h:t + h + 1]
            err[h].append(float((tr.world_states[h] - y).norm())); pers[h].append(float((x0 - y).norm()))
        n1.append(float(tr.world_states[1].norm())); n30.append(float(tr.world_states[H].norm()))
        y = x[t + 1:t + 2]
        errs = []
        for c in range(A_ENV):
            a2 = acts[:, :1].clone(); a2[0, 0] = 0.0; a2[0, 0, c] = 1.0
            errs.append(float((e2.rollout_with_world(zs, x0, a2, compute_action_objects=False).world_states[1] - y).norm()))
        disc5.append(int(np.argmin(errs)) == int(te[i]["a"][t]))
    beats = {h: bool(np.median(err[h]) < np.median(pers[h])) for h in range(1, H + 1)}
    k = 0
    for h in range(1, H + 1):
        if beats[h] and k == h - 1:
            k = h
    return {"n_starts": len(starts), "disc5_h1_tew": float(np.mean(disc5)), "k30": k,
            "beats_persistence_by_depth": {str(h): beats[h] for h in range(1, H + 1)},
            "err_over_pers_by_depth": {str(h): float(np.median(err[h]) / np.median(pers[h])) for h in range(1, H + 1)},
            "rollout_norm_t1_p50": float(np.median(n1)), "rollout_norm_t30_p50": float(np.median(n30)),
            "true_norm_p50": float(np.median([float(te[i]["z"][t].norm()) for i, t in starts]))}


# ------------------------------------------------------------------ probe states
def collect_states(agent, env, steps, every, seed, ncont, clen):
    g = np.random.default_rng(seed + 31)
    states, pend = [], {}

    def q_values(e0):
        q = []
        for c in range(A_ENV):
            tot = 0.0
            for _ in range(ncont):
                e = copy.deepcopy(e0)
                _f, h, done, _i, _o = e.step(c)
                s = float(h)
                for _k in range(clen):
                    if done:
                        break
                    _f, h, done, _i, _o = e.step(int(g.integers(0, A_ENV)))
                    s += float(h)
                tot += s
            q.append(tot / ncont)
        return np.asarray(q)

    def on_action(agent, latent, action, obs_dict, ticks, step, **k):
        if step % every != 0:
            return
        lat_s = agent._current_latent
        z0, s0 = latent.z_world.detach().clone(), latent.z_self.detach().clone()
        zt = []
        for c in range(A_ENV):
            e = copy.deepcopy(env)
            zt.append(BP.encode_next(agent, e.step(c)[4], lat_s, BP.onehot(c, A_ENV)))
        rs = torch.get_rng_state()
        with torch.no_grad():
            pool = agent.hippocampal.propose_trajectories(z0, z_self=s0)
        torch.set_rng_state(rs)
        pend["i"] = len(states)
        states.append({"z0": z0, "s0": s0, "z_true": zt, "q": q_values(env),
                       "pool_actions": [p.actions.detach().clone() for p in pool],
                       "executed": int(action.detach().reshape(-1).argmax())})

    h = StepHarness(agent, env, train_mode=False, seed=seed, hooks=StepHooks(on_action=on_action))
    _f, obs = env.reset(); agent.reset(); h.reset()
    harm = []
    for _ in range(steps):
        pend.pop("i", None)
        r = h.step(obs)
        harm.append(float(r.harm_signal))
        i = pend.get("i")
        obs = r.next_obs_dict
        if i is not None and not r.done:
            r2 = h.step(obs)
            harm.append(float(r2.harm_signal))
            states[i]["validation_maxabs"] = float((r2.latent.z_world - states[i]["z_true"][states[i]["executed"]]).abs().max())
            obs = r2.next_obs_dict
            if r2.done:
                _f, obs = env.reset(); agent.reset(); h.reset()
            continue
        if r.done:
            _f, obs = env.reset(); agent.reset(); h.reset()
    return states, harm


# ------------------------------------------------------------------ scoring
def batch_traj(trajs):
    L = len(trajs[0].world_states)
    return Trajectory(states=[torch.cat([t.states[k] for t in trajs]) for k in range(len(trajs[0].states))],
                      actions=torch.cat([t.actions for t in trajs]),
                      world_states=[torch.cat([t.world_states[k] for t in trajs]) for k in range(L)])


@torch.no_grad()
def depth_scores(agent, trajs):
    """J[L] per candidate for L = 2..Lmax (Lmax = full length) plus full (limit None)."""
    e3 = agent.e3
    bt = batch_traj(trajs)
    Lmax = len(trajs[0].world_states)
    prev = e3._score_depth_limit
    out = {}
    try:
        for L in list(range(2, Lmax + 1)) + [None]:
            e3._score_depth_limit = L
            out[L] = e3.score_trajectory(bt).detach().reshape(-1).numpy().astype(np.float64)
    finally:
        e3._score_depth_limit = prev
    return out, Lmax


def aggregate(J, Lmax, fid_beats):
    """J: dict L -> [C]. Increment for depth d (d = 2..Lmax-1 steps): J[d+1] - J[d]."""
    base = J[2]
    inc = {d: J[d + 1] - J[d] for d in range(2, Lmax)}
    out = {"FULL": J[None], "D1": base.copy()}
    for g in GAMMAS:
        out["DISC_%s" % g] = base + sum((g ** (d - 1)) * inc[d] for d in inc)
    w = {d: 1.0 if fid_beats.get(str(d), False) else 0.0 for d in inc}
    out["FIDW"] = base + sum(w[d] * inc[d] for d in inc)
    return out


def spearman(a, b):
    ra, rb = np.argsort(np.argsort(a)), np.argsort(np.argsort(b))
    if np.std(ra) == 0 or np.std(rb) == 0 or np.ptp(a) < 1e-12 or np.ptp(b) < 1e-12:
        return None
    return float(np.corrcoef(ra, rb)[0, 1])


@torch.no_grad()
def score_head(agent, states, fid_beats):
    """Per state: aggregated scores on the native pool and on the scaffold pool, J_true."""
    rows = []
    for st in states:
        s0, z0 = st["s0"], st["z0"]
        pool = [agent.e2.rollout_with_world(s0, z0, a, compute_action_objects=False) for a in st["pool_actions"]]
        Jn, Lmax = depth_scores(agent, pool)
        base = st["pool_actions"][0].clone()
        scaf = []
        for c in range(A_ENV):
            a = base.clone(); a[:, 0, :] = 0.0; a[:, 0, c] = 1.0
            scaf.append(agent.e2.rollout_with_world(s0, z0, a, compute_action_objects=False))
        Js, _ = depth_scores(agent, scaf)
        true_trajs = [Trajectory(states=[s0, s0], actions=BP.onehot(c, A_ENV).unsqueeze(1), world_states=[z0, st["z_true"][c]])
                      for c in range(A_ENV)]
        jt = BP.score(agent, true_trajs, None)
        batch_canary = float(np.abs(BP.score(agent, pool, None) - Jn[None]).max()) if not rows else None
        rows.append({"batch_canary": batch_canary, "native": aggregate(Jn, Lmax, fid_beats), "scaf": aggregate(Js, Lmax, fid_beats), "jtrue": jt,
                     "Lmax": Lmax, "full_eq_Lmax_native": float(np.abs(Jn[Lmax] - Jn[None]).max()),
                     "pool_first_classes": [int(a[0, 0].argmax()) for a in st["pool_actions"]]})
    return rows


def metrics(rows_h, rows_init, states):
    out = {}
    for ag in AGGS:
        rho, hitq, chance, flips, rho_nat, picks = [], [], [], [], [], []
        for r, ri, st in zip(rows_h, rows_init, states):
            js = r["scaf"][ag]
            rho.append(spearman(js, r["jtrue"]))
            q = st["q"]
            p = int(np.argmin(js)); picks.append(p)
            if np.ptp(q) > 1e-9:
                best = set(np.nonzero(q >= q.max() - 1e-9)[0].tolist())
                hitq.append(p in best); chance.append(len(best) / A_ENV)
            flips.append(int(np.argmin(r["native"][ag])) != int(np.argmin(ri["native"][ag])))
            # secondary: native-pool J vs the true one-step J of each candidate's first-action class
            cls = r["pool_first_classes"]
            rho_nat.append(spearman(r["native"][ag], np.asarray([r["jtrue"][c] for c in cls])))
        v = [x for x in rho if x is not None]; vn = [x for x in rho_nat if x is not None]
        out[ag] = {"rho_scaf": float(np.mean(v)) if v else None, "rho_scaf_n": len(v),
                   "pick_in_Qbest": float(np.mean(hitq)) if hitq else None, "q_chance": float(np.mean(chance)) if chance else None,
                   "n_informative": len(hitq), "flip_vs_init": float(np.mean(flips)),
                   "rho_native_secondary": float(np.mean(vn)) if vn else None, "rho_native_n": len(vn),
                   "scaf_pick_counts": {str(k): v for k, v in sorted(Counter(picks).items())}}
    return out


def habit_contrast(rows_h):
    """SD-081 practical contrast: agreement of each aggregation's native-pool pick with the
    habit read (limit 2 == D1) and mean Spearman between them across candidates."""
    out = {}
    for ag in AGGS:
        agree, rho = [], []
        for r in rows_h:
            agree.append(int(np.argmin(r["native"][ag])) == int(np.argmin(r["native"]["D1"])))
            s = spearman(r["native"][ag], r["native"]["D1"])
            if s is not None:
                rho.append(s)
        out[ag] = {"pick_agree_with_habit": float(np.mean(agree)), "rho_with_habit": float(np.mean(rho)) if rho else None}
    return out


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--n-eps", type=int, default=12)       # N = 2400 (babbling probe amendment 1)
    ap.add_argument("--post", type=int, default=1200)
    ap.add_argument("--pre-upd", type=int, default=PRE_UPD)
    ap.add_argument("--probe-steps", type=int, default=320)
    ap.add_argument("--probe-every", type=int, default=8)
    ap.add_argument("--ncont", type=int, default=6)
    ap.add_argument("--clen", type=int, default=4)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    global POST_UPD
    if a.post != 1200:
        POST_UPD = int(9000 * a.post / 1200)   # smoke only
    t0 = time.time()
    S = a.seed
    res = {"args": vars(a), "code_sha": "5f965cff830451e7c4a5b2b237e113990e513b8f", "post_upd": POST_UPD}

    def log(msg):
        print("[s%d t=%4.0fs] %s" % (S, time.time() - t0, msg), flush=True)

    R.seed_all(S)
    _e, ref, _c = R.build_B(S, False)
    ref.eval()
    ref_enc = copy.deepcopy(ref.latent_stack.state_dict())
    init = BP.get_head(ref)

    l2_segs, _ = BB.gen_policy(S, a.n_eps, 0, pol_L2_5(S))
    te4_segs, _ = BB.gen_policy(S, 3000 // EP_STEPS, 120, BB.pol_uniform(S * 7 + 3))
    tew_segs, _ = BB.gen_policy(S, 3000 // EP_STEPS, 160, pol_uniform5(S * 7 + 5))
    res["dose_L2"] = BB.dose_stats(l2_segs)
    E = {"L2": BB.encode_segs(ref, l2_segs), "TE4": BB.encode_segs(ref, te4_segs), "TEW": BB.encode_segs(ref, tew_segs)}
    g = torch.Generator().manual_seed(S + 17)
    allA = torch.cat([e["a"] for e in E["L2"]])
    perm = allA[torch.randperm(allA.shape[0], generator=g)]
    shuf, off = [], 0
    for e in E["L2"]:
        n = e["a"].shape[0]
        shuf.append({"z": e["z"], "raw": e["raw"], "a": perm[off:off + n]}); off += n
    E["SHUF"] = shuf
    log("DATA L2 %s" % json.dumps({k: res["dose_L2"][k] for k in ("n", "class_counts", "entropy_nats", "mean_run_length")}))

    heads, res["heads"] = {"INIT": init}, {}
    pre = {}
    for nm, ds in (("REAL", "L2"), ("SHUF", "SHUF")):
        hd, tinfo = BB.train_head(ref, init, BB.to_trans(E[ds], "z"), a.pre_upd, S)
        pre[nm] = hd
        res["heads"][nm + "_pre"] = {"train": tinfo, "eval4": BB.evaluate(ref, hd, E["TE4"], "z", S)}
        log("PRE %s disc4=%.3f k=%d grad=%s" % (nm, res["heads"][nm + "_pre"]["eval4"]["disc4_h1"],
                                               res["heads"][nm + "_pre"]["eval4"]["k"], tinfo["grad_nonnull_step1"]))
    rep = {"REAL": BB.to_trans(E["L2"], "z"), "SHUF": BB.to_trans(E["SHUF"], "z")}
    bufs = {}
    for nm in ("REAL", "SHUF"):
        hp, run, buf = post_phase(S, ref_enc, pre[nm], a.post, rep[nm], shuffle_onpolicy=(nm == "SHUF"))
        heads[nm] = hp; bufs[nm] = buf
        res["heads"][nm] = {"post_run": run}
        log("POST %s upd=%d grad=%s r/100=%.2f harm/100=%.2f H=%.2f" % (nm, run["updates_done"], run["grad_nonnull_first"],
                                                                       run["reward_per_100"], run["harm_events_per_100"], run["action_entropy"]))
    # descriptive B0': head trained on the REAL arm's own on-policy post-phase transitions
    b0, b0info = BB.train_head(ref, init, bufs["REAL"], a.pre_upd, S)
    heads["B0p"] = b0
    fid = {}
    for nm in ("INIT", "REAL", "SHUF", "B0p"):
        ev4 = BB.evaluate(ref, heads[nm], E["TE4"], "z", S)
        evw = eval_tew(ref, heads[nm], E["TEW"], S)
        fid[nm] = evw["beats_persistence_by_depth"]
        res["heads"].setdefault(nm, {})
        res["heads"][nm]["eval4"] = ev4; res["heads"][nm]["tew"] = evw
        log("EVAL %s disc4=%.3f k=%d disc5(te4)=%.3f disc5(tew)=%.3f k30=%d n_fid_depths=%d norm t1/t30/true=%.2f/%.2f/%.2f" % (
            nm, ev4["disc4_h1"], ev4["k"], ev4["disc5_h1"], evw["disc5_h1_tew"], evw["k30"],
            sum(fid[nm].values()), evw["rollout_norm_t1_p50"], evw["rollout_norm_t30_p50"], evw["true_norm_p50"]))
    d_pre, d_post, d_b0 = res["heads"]["REAL_pre"]["eval4"]["disc4_h1"], res["heads"]["REAL"]["eval4"]["disc4_h1"], res["heads"]["B0p"]["eval4"]["disc4_h1"]
    res["retention_vs_B0p"] = (d_post - d_b0) / (d_pre - d_b0) if abs(d_pre - d_b0) > 1e-9 else None

    # probe states, REAL head live
    pa = BB.fresh_agent(S, ref_enc)
    BP.set_head(pa, heads["REAL"])
    R.seed_all(S + 900)
    env = BB.make_env(S, 100)
    states, harm = collect_states(pa, env, a.probe_steps, a.probe_every, S, a.ncont, a.clen)
    vals = [s["validation_maxabs"] for s in states if "validation_maxabs" in s]
    res["probe"] = {"n_states": len(states), "n_informative_q": int(sum(np.ptp(s["q"]) > 1e-9 for s in states)),
                    "validation_maxabs_max": float(max(vals)) if vals else None, "n_validated": len(vals),
                    "pool_size_p50": float(np.median([len(s["pool_actions"]) for s in states])) if states else None,
                    "pool_first_class_n_distinct_p50": float(np.median([len(set(int(x[0, 0].argmax()) for x in s["pool_actions"])) for s in states])) if states else None,
                    "harm_events_per_100": float((np.asarray(harm) < 0).sum() * 100.0 / max(1, len(harm)))}
    log("PROBE %s" % json.dumps(res["probe"]))

    rows = {}
    for nm in ("INIT", "REAL", "SHUF"):
        BP.set_head(pa, heads[nm])
        rows[nm] = score_head(pa, states, fid[nm])
    res["decomp_canary_full_eq_Lmax_max"] = float(max(r["full_eq_Lmax_native"] for nm in rows for r in rows[nm]))
    res["batch_canary_max"] = float(max(r["batch_canary"] for nm in rows for r in rows[nm] if r["batch_canary"] is not None))
    res["metrics"] = {nm: metrics(rows[nm], rows["INIT"], states) for nm in ("REAL", "SHUF")}
    res["habit_contrast_REAL"] = habit_contrast(rows["REAL"])
    res["fidw_weight_depths"] = {nm: [int(d) for d, b in fid[nm].items() if b and int(d) >= 2] for nm in fid}
    for ag in AGGS:
        mr, ms = res["metrics"]["REAL"][ag], res["metrics"]["SHUF"][ag]
        log("AGG %-8s rho %s/%s  Qbest %s/%s (n_inf=%d chance=%s)  flip %.2f/%.2f  habit_agree=%.2f" % (
            ag, mr["rho_scaf"], ms["rho_scaf"], mr["pick_in_Qbest"], ms["pick_in_Qbest"], mr["n_informative"], mr["q_chance"],
            mr["flip_vs_init"], ms["flip_vs_init"], res["habit_contrast_REAL"][ag]["pick_agree_with_habit"]))
    res["t_total_s"] = round(time.time() - t0, 1)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    json.dump(res, open(a.out, "w"), indent=1, default=str)
    log("wrote %s decomp_canary=%.3g" % (a.out, res["decomp_canary_full_eq_Lmax_max"]))


if __name__ == "__main__":
    main()
