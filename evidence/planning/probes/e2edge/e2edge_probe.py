"""DCD2 probe E (bt0926-e2edge): why does the W3-trained E2 world head only tie persistence
away from resets? Locate the earliest rung where action-conditional information is lost:
  (i)   ENV   -- obs_{t+1} barely depends on a_t (persistence near-optimal in obs space);
  (ii)  REP   -- obs carries it, z_world does not;
  (iii) PRED  -- z_world carries it (a fitted oracle on (z_t, a_t) beats persistence), E2 does not;
  (iv)  PROV  -- E2 is fed a continuous candidate vector in the native loop, env executes its class.

One process = one seed. Code under test: ree-v3 4070b0efa4 (archive/coupled-loop-repair-4070b0e),
private detached worktree. NO ree_core edits. Pre-registration:
REE_assembly/evidence/planning/e2_offreset_edge_probe_20260926.md.

Phases:
  0. reference build (build_B(S), world_dim 32, reset-init knobs ON) + an untrained second-init
     reference encoder (build_B(S+1000)). TEST set = the W3 held-out generator
     (gen_policy(S, 15, 120, pol_uniform(S*7+3))), augmented with COUNTERFACTUAL next observations
     (deepcopy(env).step(c) for c = 0..4 at every tick, all RNG restored). TRAIN set for the fitted
     oracles = same generator, env k 300.., policy seed S*7+5. Canaries: CF(executed) == actual
     next obs; TEST obs sequence == BB.gen_policy's; encode_next(CF(executed)) == sense().z_world.
  1. W3 member protocol verbatim (cg_probe phase 1): babble 2400 -> FROZEN retained, 3000 updates
     (head_pre), 1200 native steps x 8 updates (head_post). Encoder-unchanged check.
  2. native on-policy lives (frozen trainer), recording fed vector and executed class (PROV).
  3. scoring (all in-process, CPU numpy/torch): see sec 2 of the pre-registration.
ASCII-only output.
"""
from __future__ import annotations

import argparse, copy, json, math, os, random, select, subprocess, sys, time, types
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F

p = argparse.ArgumentParser()
p.add_argument("--seed", type=int, required=True)
p.add_argument("--wt", required=True)
p.add_argument("--out", required=True)
p.add_argument("--s1", type=int, default=1200)
p.add_argument("--ups", type=int, default=8)
p.add_argument("--n-test-eps", type=int, default=15)
p.add_argument("--n-train-eps", type=int, default=15)
p.add_argument("--n-onpol", type=int, default=800)
p.add_argument("--tmin", type=int, default=8)
p.add_argument("--max-hold", type=float, default=600.0)
p.add_argument("--regap", type=float, default=180.0)
p.add_argument("--no-lock", action="store_true")
p.add_argument("--smoke", action="store_true")
a = p.parse_args()

PROBES = Path("/Users/dgolden/REE_Working/REE_assembly/evidence/planning/probes")
sys.path.insert(0, str(PROBES / "babble"))
sys.path.insert(0, str(PROBES / "rollout"))
sys.path.insert(0, str(Path(a.wt) / "experiments"))
sys.path.insert(0, a.wt)
torch.set_num_threads(2)

import babble_probe as BB  # noqa: E402
import rollout_fidelity_probe as R  # noqa: E402
import balanced_replay_probe as BP  # noqa: E402
from experiments._harness import StepHarness  # noqa: E402
from ree_core.utils import waking_trainer as WT  # noqa: E402
from ree_core.developmental.structured_babbling import StructuredBabbler  # noqa: E402

S = a.seed
t0 = time.time()
BASE_LR = 3e-4
A_ENV = 5
CL = [0, 1, 2, 3]
LOCK = "/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/mac_probe.lock"
KNOBS = ("use_zworld_ema_reset_init", "use_zself_ema_reset_init",
         "use_shared_ema_reset_init", "use_zharm_ema_reset_init")


def log(m):
    print("[e2edge s%d t=%5.0fs] %s" % (S, time.time() - t0, m), flush=True)


assert str(Path(WT.__file__).resolve()).startswith(str(Path(a.wt).resolve())), WT.__file__


# ------------------------------------------------------------------ Mac CPU lock
def _freemb():
    out = subprocess.run(["vm_stat"], capture_output=True, text=True).stdout
    ps = int(out.split("page size of")[1].split()[0]); f = i = 0
    for ln in out.splitlines():
        if ln.startswith("Pages free"): f = int(ln.split()[-1].rstrip("."))
        if ln.startswith("Pages inactive"): i = int(ln.split()[-1].rstrip("."))
    return (f + i) * ps // 1048576


HELD = {"label": None, "t": None, "released_at": None}
HOLDS = []


def lock_acquire(label):
    if a.no_lock:
        return
    if HELD["released_at"] is not None:            # fairness gap after our own release
        gap = a.regap - (time.time() - HELD["released_at"])
        if gap > 0:
            time.sleep(gap)
    fd = os.open(os.path.dirname(LOCK), os.O_RDONLY)
    kq = select.kqueue()
    ev = select.kevent(fd, filter=select.KQ_FILTER_VNODE, flags=select.KQ_EV_ADD | select.KQ_EV_CLEAR,
                       fflags=select.KQ_NOTE_WRITE | select.KQ_NOTE_LINK)
    kq.control([ev], 0, 0)
    tw = time.time()
    while True:
        if _freemb() >= 800:
            try:
                os.mkdir(LOCK)
                break
            except FileExistsError:
                pass
        kq.control(None, 1, 30.0)
    os.close(fd)
    with open(os.path.join(LOCK, "owner"), "w") as fh:     # owner file only after mkdir succeeded
        fh.write("bt0926-e2edge %s %s pid %d\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), label, os.getpid()))
    HELD["label"] = label
    HELD["t"] = time.time()
    log("LOCK ACQUIRED %s (waited %.0fs)" % (label, time.time() - tw))


def lock_release(label=None):
    if a.no_lock or HELD["label"] is None:
        return
    try:
        os.remove(os.path.join(LOCK, "owner"))
    except FileNotFoundError:
        pass
    os.rmdir(LOCK)
    assert not os.path.exists(LOCK), "lock still present after release"
    HOLDS.append([HELD["label"], round(time.time() - HELD["t"], 1)])
    log("LOCK RELEASED %s after %.0fs (verified gone)" % (HELD["label"], time.time() - HELD["t"]))
    HELD["label"] = None
    HELD["released_at"] = time.time()


def maybe_rehold(label):
    if a.no_lock or HELD["label"] is None:
        return
    if time.time() - HELD["t"] > a.max_hold:
        lock_release()
        lock_acquire(label)


def _release_at_exit(*_x):
    if HELD["label"] is not None:
        lock_release()
    if _x:
        sys.exit(143)


import atexit, signal  # noqa: E402
atexit.register(_release_at_exit)
signal.signal(signal.SIGTERM, _release_at_exit)


def set_knobs(agent):
    for k in KNOBS:
        setattr(agent.config.latent, k, True)
        if hasattr(agent, "latent_stack") and hasattr(agent.latent_stack, "config"):
            setattr(agent.latent_stack.config, k, True)
    assert all(getattr(agent.latent_stack.config, k) for k in KNOBS)


# ------------------------------------------------------------------ data generation
def _rng_state():
    return (random.getstate(), np.random.get_state(), torch.get_rng_state())


def _rng_restore(st):
    random.setstate(st[0]); np.random.set_state(st[1]); torch.set_rng_state(st[2])


def gen_cf(seed, n_eps, k0, policy, cf=True):
    """BB.gen_policy verbatim, plus counterfactual next obs for c = 0..4 at every tick."""
    segs, early = [], 0
    nbad = 0
    for ep in range(n_eps):
        env = BB.make_env(seed, k0 + ep)
        _f, od = env.reset()
        seg = {"obs": [BB.snap_obs(od)], "a": [], "cf": []}
        for _s in range(BB.EP_STEPS):
            ai = policy()
            if cf:
                st = _rng_state()
                cfo = []
                for c in range(A_ENV):
                    e2 = copy.deepcopy(env)
                    _o, _h, _d, _i, od2 = e2.step(c)
                    cfo.append(BB.snap_obs(od2))
                _rng_restore(st)
                seg["cf"].append(cfo)
            _o, harm, done, info, od = env.step(ai)
            if cf and not torch.equal(seg["cf"][-1][ai]["world_state"], torch.as_tensor(od["world_state"]).float()):
                nbad += 1
            seg["a"].append(ai); seg["obs"].append(BB.snap_obs(od))
            if done:
                early += 1
                segs.append(seg)
                _f, od = env.reset()
                seg = {"obs": [BB.snap_obs(od)], "a": [], "cf": []}
        segs.append(seg)
    return segs, {"early_terminations": early, "cf_exec_mismatch": nbad}


@torch.no_grad()
def encode_lat(agent, obs, prev_latent):
    ob = torch.as_tensor(obs["body_state"]).float().reshape(1, -1)
    ow = torch.as_tensor(obs["world_state"]).float().reshape(1, -1)
    enc = torch.cat([agent.body_obs_encoder(ob), agent.world_obs_encoder(ow)], dim=-1)
    vol = agent.e3.volatility_estimate if agent.config.latent.volatility_signal_dim > 0 else None
    harm = obs.get("harm_obs")
    if agent.lpb_router is not None and harm is not None:
        harm = agent.lpb_router.mask_external_harm_obs(harm)
    anchor = agent._e1_predicted_next_z_self if getattr(agent.config.latent, "use_self_recurrence", False) else None
    lat = agent.latent_stack.encode(enc, prev_latent, prev_action=None, harm_obs=harm,
                                    harm_obs_a=obs.get("harm_obs_a"), harm_history=obs.get("harm_history"),
                                    volatility_signal=vol, self_e1_anchor=anchor)
    zr = getattr(lat, "z_world_raw", None)
    return lat.z_world.detach().reshape(-1).clone(), (zr.detach().reshape(-1).clone() if zr is not None else None)


@torch.no_grad()
def encode_cf(agent, segs, canary):
    """Native read path (ref.sense over each segment after ref.reset(), as BB.encode_segs), plus
    counterfactual z^c / z_raw^c of each CF next obs from the SAME pre-sense latent."""
    out = []
    for s in segs:
        if len(s["a"]) < 1:
            continue
        agent.reset()
        zs, zr, cz, czr = [], [], [], []
        for t, o in enumerate(s["obs"]):
            if t >= 1 and s.get("cf"):
                prev = agent._current_latent
                row, rowr = [], []
                for c in range(A_ENV):
                    z1, r1 = encode_lat(agent, s["cf"][t - 1][c], prev)
                    row.append(z1); rowr.append(r1 if r1 is not None else z1)
                cz.append(torch.stack(row)); czr.append(torch.stack(rowr))
            lat = agent.sense(o["body_state"], o["world_state"], obs_harm=o.get("harm_obs"),
                              obs_harm_a=o.get("harm_obs_a"), obs_harm_history=o.get("harm_history"))
            z = lat.z_world.detach().reshape(-1).clone()
            r_ = getattr(lat, "z_world_raw", None)
            zs.append(z); zr.append(r_.detach().reshape(-1).clone() if r_ is not None else z)
            if t >= 1 and s.get("cf"):
                ex = int(s["a"][t - 1])
                d = float((cz[-1][ex] - z).abs().max())
                canary["enc_max_absdiff"] = max(canary.get("enc_max_absdiff", 0.0), d)
        e = {"z": torch.stack(zs), "zr": torch.stack(zr), "a": torch.tensor(s["a"]),
             "raw": torch.stack([o["world_state"].reshape(-1) for o in s["obs"]])}
        if s.get("cf"):
            e["cz"] = torch.stack(cz); e["czr"] = torch.stack(czr)
            e["craw"] = torch.stack([torch.stack([c["world_state"].reshape(-1) for c in row]) for row in s["cf"]])
        out.append(e)
    return out


# ------------------------------------------------------------------ phase 0
premise = {}
lock_acquire("seed%d-p0" % S)
R.seed_all(S)
_e, ref, _c = R.build_B(S, False)
set_knobs(ref)
ref.eval()
ref_enc = copy.deepcopy(ref.latent_stack.state_dict())
init_head = BP.get_head(ref)
premise["reafference_predictor_is_none"] = ref.latent_stack.reafference_predictor is None
premise["alpha_world"] = float(getattr(ref.latent_stack.config, "alpha_world", float("nan")))
premise["observation_reliability_is_none"] = getattr(ref, "observation_reliability", None) is None
premise["world_dim"] = int(ref.e2.config.world_dim)
R.seed_all(S + 1000)
_e2, ref2, _c2 = R.build_B(S + 1000, False)
set_knobs(ref2)
ref2.eval()

n_te = 2 if a.smoke else a.n_test_eps
n_tr = 2 if a.smoke else a.n_train_eps
tg = time.time()
te_segs, te_info = gen_cf(S, n_te, 120, BB.pol_uniform(S * 7 + 3), cf=True)
tr_segs, tr_info = gen_cf(S, n_tr, 300, BB.pol_uniform(S * 7 + 5), cf=False)
# canary: TEST obs sequence identical to BB.gen_policy (the W3 held-out generator)
chk_segs, _ = BB.gen_policy(S, n_te, 120, BB.pol_uniform(S * 7 + 3))
same = len(chk_segs) == len(te_segs) and all(
    len(x["obs"]) == len(y["obs"]) and all(torch.equal(u["world_state"], v["world_state"]) for u, v in zip(x["obs"], y["obs"]))
    and x["a"] == y["a"] for x, y in zip(chk_segs, te_segs))
premise["canary_test_equals_W3_generator"] = bool(same)
premise["canary_cf_exec_mismatch"] = te_info["cf_exec_mismatch"]
log("data gen %.0fs: test segs %d (early %d, cf mismatch %d), train segs %d, W3-generator identical %s" % (
    time.time() - tg, len(te_segs), te_info["early_terminations"], te_info["cf_exec_mismatch"], len(tr_segs), same))
canary = {}
TE = encode_cf(ref, te_segs, canary)
TR = encode_cf(ref, tr_segs, {})
canary2 = {}
TE2 = encode_cf(ref2, te_segs, canary2)
TR2 = encode_cf(ref2, tr_segs, {})
premise["canary_encode_next_vs_sense_maxabs"] = canary.get("enc_max_absdiff")
premise["canary2_encode_next_vs_sense_maxabs"] = canary2.get("enc_max_absdiff")
log("encode done %.0fs | encode canary maxabs %.2e / %.2e" % (time.time() - tg, canary.get("enc_max_absdiff", -1),
                                                             canary2.get("enc_max_absdiff", -1)))
ev_init_std = BB.evaluate(ref, init_head, TE, "z", S)

# ------------------------------------------------------------------ phase 1: W3 protocol
agent = BB.fresh_agent(S, ref_enc)
set_knobs(agent)
cfg = agent.config
cfg.waking_trainer_guard_min_steps = 8
member = WT.E2WorldMember(agent, lr=BASE_LR, batch_size=32, buffer_max=2000, retained_max=5000,
                          replay_frac=0.25, reencode_window=0, replay_latent="reencode",
                          objective="mse", grad_clip=1.0, updates_per_step=1)
tr = WT.WakingTrainer(agent, cfg, members=[member])
agent.waking_trainer = tr
bab = StructuredBabbler(n_classes=5, max_run=4, seed=S * 13 + 1)
tr.set_e2_world_source("babble")
tr.every_k = 10 ** 9
with torch.no_grad():
    for k in range(1 if a.smoke else 12):
        maybe_rehold("seed%d-bab-%d" % (S, k))
        env = BB.make_env(S, k)
        _f, od = env.reset(); agent.reset(); bab.reset()
        for _s in range(BB.EP_STEPS):
            agent.sense(od["body_state"], od["world_state"], obs_harm=od.get("harm_obs"),
                        obs_harm_a=od.get("harm_obs_a"), obs_harm_history=od.get("harm_history"))
            act = bab.next_action()
            agent.record_executed_action(act)
            _f, h, done, _i, od = env.step(int(act.argmax()))
            tr.on_waking_step(float(h))
            if done:
                _f, od = env.reset(); agent.reset(); bab.reset()
for _u in range(300 if a.smoke else 3000):
    tr._update("e2_world", member)
head_pre = BP.get_head(agent)
tr.set_e2_world_source("on_policy")
tr.every_k = 1
member.updates_per_step = a.ups
agent.reset()
R.seed_all(S + 500)


def native_dose(n_steps, k0):
    n_eps = max(1, n_steps // BB.EP_STEPS)
    for ep in range(n_eps):
        maybe_rehold("seed%d-dose-%d" % (S, k0 + ep))
        env = BB.make_env(S, k0 + ep)
        hh = StepHarness(agent, env, train_mode=False, seed=S * 1000 + k0 + ep)
        _f, od = env.reset(); agent.reset(); hh.reset()
        for _s in range(min(BB.EP_STEPS, n_steps)):
            r = hh.step(od)
            od = r.next_obs_dict
            if r.done:
                _f, od = env.reset(); agent.reset(); hh.reset()


tdose = time.time()
native_dose(200 if a.smoke else a.s1, 50)
head_post = BP.get_head(agent)
enc_now = agent.latent_stack.state_dict()
premise["encoder_unchanged_after_W3"] = bool(all(torch.equal(enc_now[k], v) for k, v in ref_enc.items()))
ev_pre_std = BB.evaluate(ref, head_pre, TE, "z", S)
ev_post_std = BB.evaluate(ref, head_post, TE, "z", S)
log("W3 dose %.0fs | std evaluate disc4/k/eop: init %.3f/%d/%.3f pre %.3f/%d/%.3f post %.3f/%d/%.3f | enc unchanged %s" % (
    time.time() - tdose, ev_init_std["disc4_h1"], ev_init_std["k"], ev_init_std["err_over_pers_h1"],
    ev_pre_std["disc4_h1"], ev_pre_std["k"], ev_pre_std["err_over_pers_h1"],
    ev_post_std["disc4_h1"], ev_post_std["k"], ev_post_std["err_over_pers_h1"], premise["encoder_unchanged_after_W3"]))

# member buffer (the data E2 learned from)
buf = {"retained": [], "on_policy": []}
for name, lst in (("retained", list(member._retained)), ("on_policy", list(member._on_policy))):
    for rec in lst:
        zl = rec.get("z_live")
        if zl is None or zl[0] is None or zl[1] is None:
            continue
        av = rec["a"].reshape(-1).float()
        buf[name].append((zl[0].reshape(-1), zl[1].reshape(-1), av))


def onehot_frac(lst):
    if not lst:
        return None
    n = 0
    for _z0, _z1, av in lst:
        if float(av.max()) == 1.0 and float(av.sum()) == 1.0 and int((av != 0).sum()) == 1:
            n += 1
    return n / len(lst)


premise["buffer_n"] = {k: len(v) for k, v in buf.items()}
premise["buffer_onehot_frac"] = {k: onehot_frac(v) for k, v in buf.items()}
if buf["on_policy"]:
    av = torch.stack([x[2] for x in buf["on_policy"]])
    premise["onpol_action_vec_norm_median"] = float(av.norm(dim=1).median())
    premise["onpol_action_class_hist"] = torch.bincount(av.argmax(1), minlength=5).tolist()
log("member buffer n %s one-hot frac %s" % (premise["buffer_n"], premise["buffer_onehot_frac"]))

# ------------------------------------------------------------------ phase 2: native on-policy (PROV)
copy._deepcopy_dispatch[types.ModuleType] = lambda x, memo: x
agC = copy.deepcopy(agent)
agC.waking_trainer.every_k = 10 ** 9


class Rec:
    def __init__(self, env):
        self.__dict__["_env"] = env
        self.__dict__["last"] = None

    def __getattr__(self, k):
        return getattr(self._env, k)

    def __setattr__(self, k, v):
        if k in ("_env", "last"):
            self.__dict__[k] = v
        else:
            setattr(self._env, k, v)

    def step(self, action):
        self.__dict__["last"] = action.detach().clone().reshape(-1) if torch.is_tensor(action) else action
        return self._env.step(action)


R.seed_all(S + 600)
on_segs, on_fed, on_ex = [], [], []
n_on = 200 if a.smoke else a.n_onpol
kk = 0
done_steps = 0
while done_steps < n_on:
    maybe_rehold("seed%d-onpol-%d" % (S, kk))
    env = Rec(BB.make_env(S, 170 + kk))
    hh = StepHarness(agC, env, train_mode=False, seed=S * 1000 + 170 + kk)
    _f, od = env.reset(); agC.reset(); hh.reset()
    seg = {"obs": [BB.snap_obs(od)], "a": []}; fed = []; ex = []
    for _s in range(BB.EP_STEPS):
        r = hh.step(od)
        la = agC._last_action
        fed.append(la.detach().reshape(-1).float().clone() if la is not None else torch.zeros(A_ENV))
        exv = env.last
        exc = int(exv.argmax()) if torch.is_tensor(exv) else int(exv)
        ex.append(exc)
        od = r.next_obs_dict
        seg["a"].append(exc); seg["obs"].append(BB.snap_obs(od))
        done_steps += 1
        if r.done or done_steps >= n_on:
            break
    on_segs.append(seg); on_fed.append(fed); on_ex.append(ex)
    kk += 1
ON = encode_cf(ref, on_segs, {})
fed_all = torch.stack([v for f in on_fed for v in f])
premise["onpol_live_fed_onehot_frac"] = float(np.mean([
    float(v.max()) == 1.0 and float(v.sum()) == 1.0 and int((v != 0).sum()) == 1 for v in fed_all]))
premise["onpol_live_fed_argmax_eq_exec_frac"] = float(np.mean([
    int(v.argmax()) == e for f, ee in zip(on_fed, on_ex) for v, e in zip(f, ee)]))
log("on-policy %d steps in %d segs | fed one-hot frac %.3f | fed argmax==exec %.3f | exec hist %s" % (
    done_steps, len(on_segs), premise["onpol_live_fed_onehot_frac"], premise["onpol_live_fed_argmax_eq_exec_frac"],
    np.bincount(np.array([e for ee in on_ex for e in ee]), minlength=5).tolist()))
lock_release()
del agC

# ------------------------------------------------------------------ phase 3: scoring (no lock: light CPU,
# but stays 2 threads; the fitted MLPs are small). Re-take the lock for the MLP fits to be safe.
lock_acquire("seed%d-score" % S)


def trans(eps, key, tmin=None, tmax=None, cfkey=None):
    X0, X1, A, T, CF = [], [], [], [], []
    for e in eps:
        x = e[key].double()
        n = e["a"].shape[0]
        for t in range(n):
            if tmin is not None and t < tmin:
                continue
            if tmax is not None and t >= tmax:
                continue
            X0.append(x[t]); X1.append(x[t + 1]); A.append(int(e["a"][t])); T.append(t)
            if cfkey is not None:
                CF.append(e[cfkey][t].double())
    out = {"X0": torch.stack(X0), "X1": torch.stack(X1), "A": torch.tensor(A), "T": torch.tensor(T)}
    if cfkey is not None:
        out["CF"] = torch.stack(CF)
    return out


def ridge_fit(Xf, Y, lam):
    d = Xf.shape[1]
    reg = lam * torch.eye(d, dtype=Xf.dtype); reg[-1, -1] = 0.0
    return torch.linalg.solve(Xf.T @ Xf + reg, Xf.T @ Y)


def aug(X):
    return torch.cat([X, torch.ones(X.shape[0], 1, dtype=X.dtype)], 1)


LAMS = [1e-3, 1e-2, 1e-1, 1.0, 10.0, 100.0, 1000.0]


def fit_ridge_model(trd, mode, rng):
    """mode: 'act' per-class maps; 'blind' pooled; 'shuf' per-class on permuted labels.
    Predicts delta = X1 - X0. lambda chosen on a 20% validation split (median L2 error)."""
    X0, D, A = trd["X0"], trd["X1"] - trd["X0"], trd["A"].clone()
    if mode == "shuf":
        A = A[torch.as_tensor(rng.permutation(A.shape[0]))]
    n = X0.shape[0]
    perm = torch.as_tensor(rng.permutation(n)); nv = max(1, n // 5)
    iv, it = perm[:nv], perm[nv:]

    def fit(idx, lam):
        if mode == "blind":
            return {"all": ridge_fit(aug(X0[idx]), D[idx], lam)}
        W = {}
        for c in range(A_ENV):
            m = idx[A[idx] == c]
            if m.numel() >= 5:
                W[c] = ridge_fit(aug(X0[m]), D[m], lam)
        return W

    def pred(W, X, c):
        key = "all" if mode == "blind" else c
        if key not in W:
            return X.clone()
        return X + aug(X) @ W[key]

    best = None
    for lam in LAMS:
        W = fit(it, lam)
        P = torch.stack([pred(W, X0[iv[j:j + 1]], int(A[iv[j]]))[0] for j in range(nv)])
        e = float((P - trd["X1"][iv]).norm(dim=1).median())
        if best is None or e < best[0]:
            best = (e, lam)
    W = fit(torch.arange(n), best[1])
    return (lambda X, c: pred(W, X, c)), best[1]


def fit_mlp_model(trd, mode, seed, steps=2500):
    X0, D, A = trd["X0"].float(), (trd["X1"] - trd["X0"]).float(), trd["A"].clone()
    g = np.random.default_rng(seed)
    if mode == "shuf":
        A = A[torch.as_tensor(g.permutation(A.shape[0]))]
    torch.manual_seed(seed)
    d = X0.shape[1]
    mu, sd = X0.mean(0), X0.std(0) + 1e-6
    dsd = D.std(0) + 1e-6
    net = torch.nn.Sequential(torch.nn.Linear(d + A_ENV, 128), torch.nn.ReLU(), torch.nn.Linear(128, 128),
                              torch.nn.ReLU(), torch.nn.Linear(128, d))
    opt = torch.optim.Adam(net.parameters(), lr=1e-3, weight_decay=1e-5)
    n = X0.shape[0]
    perm = torch.as_tensor(g.permutation(n)); nv = max(1, n // 5)
    iv, it = perm[:nv], perm[nv:]
    oh = F.one_hot(A, A_ENV).float()
    inp = torch.cat([(X0 - mu) / sd, oh], 1)
    best = (float("inf"), None)
    with torch.enable_grad():
        for s in range(steps):
            idx = it[torch.randint(0, it.numel(), (128,))]
            loss = F.mse_loss(net(inp[idx]), D[idx] / dsd)
            opt.zero_grad(); loss.backward(); opt.step()
            if s % 100 == 99:
                with torch.no_grad():
                    vl = float(F.mse_loss(net(inp[iv]), D[iv] / dsd))
                if vl < best[0]:
                    best = (vl, copy.deepcopy(net.state_dict()))
    net.load_state_dict(best[1])
    net.eval()

    def pred(X, c):
        with torch.no_grad():
            Xf = X.float()
            o = F.one_hot(torch.full((X.shape[0],), int(c), dtype=torch.long), A_ENV).float()
            return (Xf + net(torch.cat([(Xf - mu) / sd, o], 1)) * dsd).double()
    return pred


def _e2_batch(X, V):
    """E2 one-step world prediction, batched; the evaluate() call form (zero z_self, h=1)."""
    e2 = ref.e2
    with torch.no_grad():
        zs = torch.zeros(X.shape[0], int(ref.e2.config.self_dim))
        tr_ = e2.rollout_with_world(zs, X.float(), V.reshape(X.shape[0], 1, -1).float(), compute_action_objects=False)
        return tr_.world_states[1].double()


def e2_model(head):
    def pred(X, c):
        BP.set_head(ref, head)
        return _e2_batch(X, F.one_hot(torch.full((X.shape[0],), int(c), dtype=torch.long), A_ENV).float())
    return pred


def e2_vec(head, X, V):
    BP.set_head(ref, head)
    return _e2_batch(X, V)


def score(model, d, rng, per_class=True):
    """model(X, c) -> predicted X1 for class c. Metrics on d (X0, X1, A[, CF]):
    R = median ||pred(a) - y|| / median ||x0 - y|| (the W3 err_over_pers_h1 form);
    disc4 = argmin_c in 0..3 ||pred(c) - y|| == a (ties broken at random);
    R_blind = the same model averaged over classes 0..3 (its own action-blind twin);
    ES = median ||pred(a) - mean_c pred(c)|| / median ||x^a - mean_c x^c|| (needs CF)."""
    X0, X1, A = d["X0"], d["X1"], d["A"]
    P = {c: model(X0, c) for c in CL}
    Pa = torch.stack([P[int(A[i])][i] for i in range(A.shape[0])])
    E = torch.stack([(P[c] - X1).norm(dim=1) for c in CL], 1)
    pers = (X0 - X1).norm(dim=1)
    mp = float(pers.median())
    err = (Pa - X1).norm(dim=1)
    Pm = torch.stack([P[c] for c in CL]).mean(0)
    jit = torch.as_tensor(rng.random(E.shape)) * 1e-12 * (E.abs().max() + 1e-12)
    hit = ((E + jit).argmin(1) == A).double()
    out = {"n": int(A.shape[0]), "R": float(err.median()) / mp, "disc4": float(hit.mean()),
           "R_blind": float((Pm - X1).norm(dim=1).median()) / mp, "pers_med": mp}
    if "CF" in d:
        CFm = d["CF"][:, CL].mean(1)
        Xa = torch.stack([d["CF"][i, int(A[i])] for i in range(A.shape[0])])
        den = float((Xa - CFm).norm(dim=1).median())
        out["ES"] = float((Pa - Pm).norm(dim=1).median()) / den if den > 0 else None
    if per_class:
        pc = {}
        for c in CL:
            m = A == c
            if int(m.sum()) >= 5:
                pc[str(c)] = {"n": int(m.sum()), "R": float(err[m].median()) / float(pers[m].median()) if float(pers[m].median()) > 0 else None,
                              "disc4": float(hit[m].mean())}
        out["per_class"] = pc
    return out


def exact_env(d, rng):
    """Exact counterfactual indices (no fitting): ID = disc4 of the exact next-state oracle with
    random tie-breaking (identifiability of a_t from x_{t+1} given the true dynamics);
    AC = median ||x^a - mean_c x^c|| / median ||x^a - x_t|| (share of the step that depends on
    the action); R_cfblind = median ||mean_c x^c - y|| / pers (best action-blind prediction under
    a uniform action prior); R_cfact = exact oracle (canary: 0 when CF(exec) == actual)."""
    X0, X1, A, CF = d["X0"], d["X1"], d["A"], d["CF"]
    Xa = torch.stack([CF[i, int(A[i])] for i in range(A.shape[0])])
    CFm = CF[:, CL].mean(1)
    pers = (X0 - X1).norm(dim=1)
    mp = float(pers.median())
    E = torch.stack([(CF[:, c] - X1).norm(dim=1) for c in CL], 1)
    jit = torch.as_tensor(rng.random(E.shape))
    tie_min = (E <= E.min(1, keepdim=True).values + 1e-9)
    hits = []
    for i in range(A.shape[0]):
        cands = [c for c in CL if bool(tie_min[i, c])]
        hits.append(1.0 / len(cands) if int(A[i]) in cands else 0.0)
    moved = float(((X1 - X0).norm(dim=1) > 1e-9).double().mean())
    return {"n": int(A.shape[0]), "ID": float(np.mean(hits)),
            "AC": float((Xa - CFm).norm(dim=1).median()) / float((Xa - X0).norm(dim=1).median()) if float((Xa - X0).norm(dim=1).median()) > 0 else None,
            "R_cfblind": float((CFm - X1).norm(dim=1).median()) / mp if mp > 0 else None,
            "R_cfact": float((Xa - X1).norm(dim=1).median()) / mp if mp > 0 else None,
            "frac_step_nonzero": moved, "pers_med": mp,
            "frac_all4_distinct": float(np.mean([len({tuple(CF[i, c].tolist()) for c in CL}) == 4 for i in range(A.shape[0])]))}


rng = np.random.default_rng(S + 31)
res = {"seed": S, "args": vars(a), "premise": premise,
       "std_evaluate": {"init": ev_init_std, "pre": ev_pre_std, "post": ev_post_std}}
ts = time.time()
# PCA-32 of raw obs (fitted on TRAIN obs), a linear, information-preserving 32-d reference
Xraw_tr = torch.cat([e["raw"] for e in TR]).double()
mu_raw = Xraw_tr.mean(0)
U, Sv, Vt = torch.linalg.svd(Xraw_tr - mu_raw, full_matrices=False)
Wp = Vt[:32].T
for eps in (TE, TR, ON):
    for e in eps:
        e["pca"] = (e["raw"].double() - mu_raw) @ Wp
        if "craw" in e:
            e["cpca"] = (e["craw"].double() - mu_raw) @ Wp
for e, e2_ in zip(TE, TE2):
    e["zu"] = e2_["z"]; e["czu"] = e2_["cz"]
for e, e2_ in zip(TR, TR2):
    e["zu"] = e2_["z"]

SPACES = [("OBS", "raw", "craw"), ("ZW", "z", "cz"), ("ZR", "zr", "czr"), ("ZU", "zu", "czu"), ("PCA", "pca", "cpca")]
windows = {"off": (a.tmin, None), "near": (0, a.tmin), "all": (None, None)}
res["spaces"] = {}
for sp, key, ck in SPACES:
    R_sp = {}
    trd = trans(TR, key, tmin=a.tmin)
    models = {}
    f_act, lam_act = fit_ridge_model(trd, "act", rng)
    f_bl, lam_bl = fit_ridge_model(trd, "blind", rng)
    f_sh, lam_sh = fit_ridge_model(trd, "shuf", rng)
    models["RIDGE_ACT"] = f_act; models["RIDGE_BLIND"] = f_bl; models["RIDGE_SHUF"] = f_sh
    R_sp["lambda"] = {"act": lam_act, "blind": lam_bl, "shuf": lam_sh}
    if sp != "OBS":
        models["MLP_ACT"] = fit_mlp_model(trd, "act", S + 71)
        models["MLP_SHUF"] = fit_mlp_model(trd, "shuf", S + 72)
    models["PERS"] = lambda X, c: X.clone()
    for wn, (lo, hi) in windows.items():
        d = trans(TE, key, tmin=lo, tmax=hi, cfkey=ck)
        R_sp[wn] = {"exact": exact_env(d, rng)}
        for mn, f in models.items():
            R_sp[wn][mn] = score(f, d, rng, per_class=(wn == "off"))
    res["spaces"][sp] = R_sp
    ex = R_sp["off"]["exact"]
    log("%-3s off: exact ID %.3f AC %.3f Rcfblind %.3f Rcfact %.3f | RIDGE_ACT R %.3f d4 %.3f | BLIND R %.3f | SHUF R %.3f d4 %.3f%s" % (
        sp, ex["ID"], -1 if ex["AC"] is None else ex["AC"], -1 if ex["R_cfblind"] is None else ex["R_cfblind"], -1 if ex["R_cfact"] is None else ex["R_cfact"],
        R_sp["off"]["RIDGE_ACT"]["R"], R_sp["off"]["RIDGE_ACT"]["disc4"], R_sp["off"]["RIDGE_BLIND"]["R"],
        R_sp["off"]["RIDGE_SHUF"]["R"], R_sp["off"]["RIDGE_SHUF"]["disc4"],
        "" if sp == "OBS" else " | MLP_ACT R %.3f d4 %.3f SHUF R %.3f" % (
            R_sp["off"]["MLP_ACT"]["R"], R_sp["off"]["MLP_ACT"]["disc4"], R_sp["off"]["MLP_SHUF"]["R"])))

# report-only: z_{t+1} from [z_t, obs_t] per class (does z_t lack the current-view detail?)
def zo_trans(eps, lo, hi):
    X0, O0, X1, A = [], [], [], []
    for e in eps:
        for t in range(e["a"].shape[0]):
            if (lo is not None and t < lo) or (hi is not None and t >= hi):
                continue
            X0.append(e["z"][t].double()); O0.append(e["raw"][t].double()); X1.append(e["z"][t + 1].double()); A.append(int(e["a"][t]))
    return torch.stack(X0), torch.stack(O0), torch.stack(X1), torch.tensor(A)


try:
    zx0, zo0, zx1, za = zo_trans(TR, a.tmin, None)
    feat_tr = aug(torch.cat([zx0, zo0], 1)); D_tr = zx1 - zx0
    n_ = feat_tr.shape[0]; pv = torch.as_tensor(rng.permutation(n_)); nv_ = n_ // 5
    best_ = None
    for lam in LAMS:
        Wc = {c: ridge_fit(feat_tr[pv[nv_:]][za[pv[nv_:]] == c], D_tr[pv[nv_:]][za[pv[nv_:]] == c], lam) for c in range(A_ENV)
              if int((za[pv[nv_:]] == c).sum()) >= 5}
        iv_ = pv[:nv_]
        P_ = torch.stack([zx0[i] + feat_tr[i] @ Wc[int(za[i])] if int(za[i]) in Wc else zx0[i] for i in iv_.tolist()])
        e_ = float((P_ - zx1[iv_]).norm(dim=1).median())
        if best_ is None or e_ < best_[0]:
            best_ = (e_, lam)
    Wc = {c: ridge_fit(feat_tr[za == c], D_tr[za == c], best_[1]) for c in range(A_ENV) if int((za == c).sum()) >= 5}
    tx0, to0, tx1, ta = zo_trans(TE, a.tmin, None)
    ft = aug(torch.cat([tx0, to0], 1))
    Pc = {c: tx0 + ft @ Wc[c] for c in CL}
    E_ = torch.stack([(Pc[c] - tx1).norm(dim=1) for c in CL], 1)
    Pa_ = torch.stack([Pc[int(ta[i])][i] for i in range(ta.shape[0])])
    mp_ = float((tx0 - tx1).norm(dim=1).median())
    res["ZW_FROM_Z_OBS"] = {"R": float((Pa_ - tx1).norm(dim=1).median()) / mp_, "disc4": float((E_.argmin(1) == ta).double().mean()),
                            "lambda": best_[1]}
    log("ZW_FROM_Z_OBS (report-only) off R %.3f d4 %.3f" % (res["ZW_FROM_Z_OBS"]["R"], res["ZW_FROM_Z_OBS"]["disc4"]))
except Exception as ex_:
    res["ZW_FROM_Z_OBS"] = {"error": repr(ex_)}
    log("ZW_FROM_Z_OBS error %r" % ex_)

# E2 heads on ZW (the deployed read path; E2 is trained on it)
E2R = {}
for hn, h in (("E2_INIT", init_head), ("E2_PRE", head_pre), ("E2_POST", head_post)):
    f = e2_model(h)
    E2R[hn] = {wn: score(f, trans(TE, "z", tmin=lo, tmax=hi, cfkey="cz"), rng, per_class=(wn == "off"))
               for wn, (lo, hi) in windows.items()}
    log("%s off R %.3f d4 %.3f Rblind %.3f ES %.3f | near R %.3f | all R %.3f d4 %.3f" % (
        hn, E2R[hn]["off"]["R"], E2R[hn]["off"]["disc4"], E2R[hn]["off"]["R_blind"], E2R[hn]["off"]["ES"] or -1,
        E2R[hn]["near"]["R"], E2R[hn]["all"]["R"], E2R[hn]["all"]["disc4"]))
res["E2"] = E2R

# canary: my disc4 on evaluate()'s own 300 starts == evaluate()'s disc4_h1 for head_post
g = np.random.default_rng(S + 77)
starts = [(i, t) for i, e in enumerate(TE) for t in range(e["a"].shape[0] - 10 + 1)]
if len(starts) > 300:
    starts = [starts[j] for j in sorted(g.choice(len(starts), 300, replace=False))]
fpost = e2_model(head_post)
hits = []
for i, t in starts:
    x0 = TE[i]["z"][t:t + 1].double(); y = TE[i]["z"][t + 1:t + 2].double()
    errs = [float((fpost(x0, c) - y).norm()) for c in CL]
    hits.append(int(np.argmin(errs)) == int(TE[i]["a"][t]))
res["premise"]["canary_disc4_vs_evaluate"] = [float(np.mean(hits)), ev_post_std["disc4_h1"]]

# ORACLE-BUF: per-class ridge + MLP fitted on the member's own buffer (z_live pairs, argmax action)
allbuf = buf["retained"] + buf["on_policy"]
if len(allbuf) >= 100:
    bd = {"X0": torch.stack([x[0] for x in allbuf]).double(), "X1": torch.stack([x[1] for x in allbuf]).double(),
          "A": torch.tensor([int(x[2].argmax()) for x in allbuf])}
    fb, lamb = fit_ridge_model(bd, "act", rng)
    fbm = fit_mlp_model(bd, "act", S + 73)
    dz = trans(TE, "z", tmin=a.tmin, cfkey="cz")
    res["ORACLE_BUF"] = {"lambda": lamb, "n_buf": len(allbuf), "RIDGE": score(fb, dz, rng), "MLP": score(fbm, dz, rng)}
    log("ORACLE_BUF (n %d) off: RIDGE R %.3f d4 %.3f | MLP R %.3f d4 %.3f" % (
        len(allbuf), res["ORACLE_BUF"]["RIDGE"]["R"], res["ORACLE_BUF"]["RIDGE"]["disc4"],
        res["ORACLE_BUF"]["MLP"]["R"], res["ORACLE_BUF"]["MLP"]["disc4"]))

# PROV: native on-policy off-reset transitions, E2_POST with the fed continuous vector vs the executed one-hot
X0l, X1l, Vl, Al, Tl = [], [], [], [], []
for e, fed in zip(ON, on_fed):
    for t in range(e["a"].shape[0]):
        if t < a.tmin:
            continue
        X0l.append(e["z"][t].double()); X1l.append(e["z"][t + 1].double()); Vl.append(fed[t]); Al.append(int(e["a"][t])); Tl.append(t)
prov = {"n": len(Al)}
if len(Al) >= 20:
    X0p, X1p, Vp, Ap = torch.stack(X0l), torch.stack(X1l), torch.stack(Vl), torch.tensor(Al)
    pers = (X0p - X1p).norm(dim=1); mp = float(pers.median())
    for hn, h in (("E2_POST", head_post), ("E2_PRE", head_pre)):
        Pc = e2_vec(h, X0p, Vp)
        Po = e2_vec(h, X0p, F.one_hot(Ap, A_ENV).float())
        prov[hn] = {"R_cont": float((Pc - X1p).norm(dim=1).median()) / mp if mp > 0 else None,
                    "R_onehot": float((Po - X1p).norm(dim=1).median()) / mp if mp > 0 else None,
                    "pred_gap_med": float((Pc - Po).norm(dim=1).median()), "pers_med": mp}
    prov["exec_hist"] = torch.bincount(Ap, minlength=5).tolist()
    prov["frac_step_nonzero_raw"] = None
    # oracle on-policy (ZW RIDGE_ACT fitted on uniform TRAIN), same transitions, executed class
    f_act_zw, _ = fit_ridge_model(trans(TR, "z", tmin=a.tmin), "act", rng)
    Pr = torch.stack([f_act_zw(X0p[i:i + 1], int(Ap[i]))[0] for i in range(Ap.shape[0])])
    prov["RIDGE_ACT_R"] = float((Pr - X1p).norm(dim=1).median()) / mp if mp > 0 else None
    log("PROV on-policy n %d exec hist %s | E2_POST R cont %.3f onehot %.3f | E2_PRE R cont %.3f onehot %.3f | ridge %.3f" % (
        prov["n"], prov["exec_hist"], prov["E2_POST"]["R_cont"], prov["E2_POST"]["R_onehot"],
        prov["E2_PRE"]["R_cont"], prov["E2_PRE"]["R_onehot"], prov["RIDGE_ACT_R"]))
res["PROV"] = prov


# ------------------------------------------------------------------ Q-113 P1 add-on (report-only)
def cue_labels(eps, tmin):
    Y = []
    for e in eps:
        for t in range(e["raw"].shape[0]):
            if t < tmin:
                continue
            lv = e["raw"][t][:175].reshape(5, 5, 7)
            Y.append((int(lv[:, :, 3].sum() > 0), int(lv[:, :, 2].sum() > 0)))
    return torch.tensor(Y)


def feats(eps, key, tmin):
    return torch.cat([e[key][tmin:].double() for e in eps])


def logreg_bal(Xtr, ytr, Xte, yte, seed, n_cls=2):
    torch.manual_seed(seed)
    mu, sd = Xtr.mean(0), Xtr.std(0) + 1e-6
    Xtr_, Xte_ = ((Xtr - mu) / sd).float(), ((Xte - mu) / sd).float()
    W = torch.zeros(Xtr.shape[1], n_cls, requires_grad=True); b = torch.zeros(n_cls, requires_grad=True)
    cnt = torch.bincount(ytr, minlength=n_cls).float().clamp(min=1)
    wts = (cnt.sum() / (n_cls * cnt))
    opt = torch.optim.LBFGS([W, b], max_iter=200)

    def closure():
        opt.zero_grad()
        l = F.cross_entropy(Xtr_ @ W + b, ytr, weight=wts) + 1e-3 * (W ** 2).sum()
        l.backward()
        return l
    with torch.enable_grad():
        opt.step(closure)
    with torch.no_grad():
        pr = (Xte_ @ W + b).argmax(1)
    rec = [float((pr[yte == c] == c).float().mean()) for c in range(n_cls) if int((yte == c).sum()) > 0]
    return float(np.mean(rec))


try:
    ytr = cue_labels(TR, a.tmin); yte = cue_labels(TE, a.tmin)
    Rproj = torch.as_tensor(np.random.default_rng(S + 99).normal(size=(250, 32)) / math.sqrt(250.0))
    reps = {"ZW (frozen deployed z_world)": ("z", None), "ZU (second untrained init)": ("zu", None),
            "RANDPROJ (untrained linear projection of world_state)": ("raw", Rproj), "PCA32": ("pca", None)}
    q = {"prevalence_test": {"hazard": float(yte[:, 0].float().mean()), "resource": float(yte[:, 1].float().mean()),
                             "both": float((yte[:, 0] * yte[:, 1]).float().mean())}}
    joint_tr = ytr[:, 0] * 2 + ytr[:, 1]; joint_te = yte[:, 0] * 2 + yte[:, 1]
    for rn, (key, P) in reps.items():
        Xtr = feats(TR, key, a.tmin); Xte = feats(TE, key, a.tmin)
        if P is not None:
            Xtr = Xtr @ P; Xte = Xte @ P
        q[rn] = {"hazard_bacc": logreg_bal(Xtr, ytr[:, 0], Xte, yte[:, 0], S),
                 "resource_bacc": logreg_bal(Xtr, ytr[:, 1], Xte, yte[:, 1], S),
                 "joint4_bacc": logreg_bal(Xtr, joint_tr, Xte, joint_te, S, n_cls=4)}
    res["Q113_P1"] = q
    log("Q113 P1: %s" % json.dumps({k: v for k, v in q.items()}, default=lambda o: round(o, 3)))
except Exception as ex:  # report-only add-on; never kill the run
    res["Q113_P1"] = {"error": repr(ex)}
    log("Q113 P1 error %r" % ex)

lock_release()
res["holds"] = HOLDS
res["t_total_s"] = time.time() - t0
json.dump(res, open(a.out, "w"), indent=1,
          default=lambda o: None if isinstance(o, float) and not math.isfinite(o) else str(o))
log("DONE %.0fs (scoring %.0fs)" % (res["t_total_s"], time.time() - ts))
