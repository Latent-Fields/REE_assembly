"""Probe C (bt0926-cgdisc): commit-gate discrimination -- signal validity (C0), operating point
(C1), escape evidence (C2). DCD2 plan sec 2 Family C / sec 3 rows C0-C2 / sec 4.1.

One process = one seed. Code under test: ree-v3 4070b0efa4 (archive/coupled-loop-repair-4070b0e),
private detached worktree. NO ree_core edits: every signal, bar, clamp, probe action and world
change is probe-side (StepHarness hooks + an env proxy).

Phases:
  0. reference build (build_B, W3 member-probe protocol, world_dim 32), held-out TE (W3 test set).
  1. W3 member protocol verbatim (N5 phase 1): babble 2400 -> FROZEN retained set, 3000 updates,
     then S1 native closed-loop dose (--s1 steps x 8 updates). Readout disc4_h1 on TE (pre-screen).
     Snapshot SNAP_S1.
  2. S1 test lives: one continuous life each (LIFE ticks, max_episode_steps LIFE+100, no episode
     boundary), frozen trainer (no member updates), identical env seed / RNG across lives of a
     stage. Hidden change at tick TC (action-map derangement SHIFT_P, or a layout redraw), used only
     for scoring. Policy clamps: NAT (native gate), FC (forced committed), FS (forced sampling), CP
     (forced committed + probe actions at rate PROBE_RATE), OWN (closed loop: ARC-029(D) own-scale
     bar on the REALISED-error EMA drives the gate).
  3. continue native training to S2 (--s2-extra more steps x 8 updates), disc4 readout, snapshot,
     S2 lives.
Per tick logged: raw_mix (rv's raw input = e3 prediction_error), rv, raw_real (realised one-step
error of the previous tick's executed action, ||z_{t+1} - E2.world_forward(z_t, a_t)||^2 mean,
logged at the tick it becomes available), ema_real (EMA alpha = precision_ema_alpha), committed
(gate state), e3_tick, executed action, probe flag, harm, env reset.
Mac CPU lock: acquired per segment (S1 part, S2 part), <= 15 min per hold, verified release.
ASCII output only.
"""
from __future__ import annotations

import argparse, copy, json, math, os, select, subprocess, sys, time, types
from collections import deque
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F

p = argparse.ArgumentParser()
p.add_argument("--seed", type=int, required=True)
p.add_argument("--wt", required=True)
p.add_argument("--out", required=True)
p.add_argument("--s1", type=int, default=1200)          # W3 standard native dose
p.add_argument("--s2-extra", type=int, default=1200)    # S2 = 2x the native dose
p.add_argument("--ups", type=int, default=8)
p.add_argument("--life", type=int, default=330)
p.add_argument("--tc", type=int, default=200)
p.add_argument("--probe-rate", type=float, default=0.05)
p.add_argument("--own-q", type=float, default=0.90)
p.add_argument("--own-window", type=int, default=60)
p.add_argument("--lives-s1", default="RND-perm,RND-none,FS-perm,FS-none,NAT-perm,NAT-none,CP-perm,CP-none,OWN-perm,OWN-none")
p.add_argument("--lives-s2", default="RND-perm,RND-none,NAT-perm,NAT-none")
p.add_argument("--max-hold", type=float, default=720.0)
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
from experiments._harness import StepHarness, StepHooks  # noqa: E402
from ree_core.utils import waking_trainer as WT  # noqa: E402
from ree_core.developmental.structured_babbling import StructuredBabbler  # noqa: E402
from ree_core.environment.causal_grid_world import CausalGridWorld, CausalGridWorldV2  # noqa: E402
from ree_core.predictors.e3_selector import E3TrajectorySelector  # noqa: E402

S = a.seed
t0 = time.time()
BASE_LR = 3e-4
SHIFT_P = [2, 3, 1, 0]
LOCK = "/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/mac_probe.lock"
KNOBS = ("use_zworld_ema_reset_init", "use_zself_ema_reset_init",
         "use_shared_ema_reset_init", "use_zharm_ema_reset_init")


def log(m):
    print("[cg s%d t=%5.0fs] %s" % (S, time.time() - t0, m), flush=True)


assert str(Path(WT.__file__).resolve()).startswith(str(Path(a.wt).resolve())), WT.__file__


# ------------------------------------------------------------------ lock
def _freemb():
    out = subprocess.run(["vm_stat"], capture_output=True, text=True).stdout
    ps = int(out.split("page size of")[1].split()[0]); f = i = 0
    for ln in out.splitlines():
        if ln.startswith("Pages free"): f = int(ln.split()[-1].rstrip("."))
        if ln.startswith("Pages inactive"): i = int(ln.split()[-1].rstrip("."))
    return (f + i) * ps // 1048576


HELD = {"label": None}


def _release_at_exit(*_x):
    if HELD["label"] is not None:
        lock_release(HELD["label"])
    if _x:
        sys.exit(143)


def lock_acquire(label):
    if a.no_lock:
        return
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
    with open(os.path.join(LOCK, "owner"), "w") as fh:
        fh.write("bt0926-cgdisc %s %s pid %d\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), label, os.getpid()))
    HELD["label"] = label
    HELD["t"] = time.time()
    log("LOCK ACQUIRED %s (waited %.0fs)" % (label, time.time() - tw))


def lock_release(label):
    if a.no_lock:
        return
    try:
        os.remove(os.path.join(LOCK, "owner"))
    except FileNotFoundError:
        pass
    os.rmdir(LOCK)
    HELD["label"] = None
    assert not os.path.exists(LOCK), "lock still present after release"
    log("LOCK RELEASED %s (verified gone)" % label)


def maybe_rehold(label):
    """At a life boundary: if this hold is older than --max-hold s, release, wait 45 s, re-acquire."""
    if a.no_lock or HELD["label"] is None:
        return
    if time.time() - HELD.get("t", time.time()) > a.max_hold:
        lab = HELD["label"]
        lock_release(lab)
        time.sleep(45)
        lock_acquire(label)


import atexit, signal  # noqa: E402
atexit.register(_release_at_exit)
signal.signal(signal.SIGTERM, _release_at_exit)

# ------------------------------------------------------------------ env helpers
BASE_ACTIONS = dict(CausalGridWorld.ACTIONS)
SHIFTED = dict(BASE_ACTIONS)
for c in range(4):
    SHIFTED[c] = BASE_ACTIONS[SHIFT_P[c]]
assert all(SHIFTED[c] != BASE_ACTIONS[c] for c in range(4)) and SHIFTED[4] == BASE_ACTIONS[4]


def make_life_env(k):
    return CausalGridWorldV2(size=BB.GRID, seed=S * BB.SEED_STRIDE + k, resource_respawn_on_consume=True,
                             pos_telemetry_enabled=True, traj_telemetry_enabled=True,
                             max_episode_steps=a.life + 100, **BB.PH0_KW)


def relayout(env, rng):
    """Layout redraw WITHOUT reset: move every hazard and resource to a fresh random empty
    interior cell (agent, walls, health, step counter untouched)."""
    E = env.ENTITY_TYPES
    for lst, et in ((env.hazards, E["hazard"]), (env.resources, E["resource"])):
        for obj in lst:
            if env.grid[obj[0], obj[1]] == et:
                env.grid[obj[0], obj[1]] = E["empty"]
    moved = 0
    for lst, et in ((env.hazards, E["hazard"]), (env.resources, E["resource"])):
        for obj in lst:
            for _try in range(200):
                x, y = int(rng.integers(1, env.size - 1)), int(rng.integers(1, env.size - 1))
                if env.grid[x, y] == E["empty"]:
                    env.grid[x, y] = et; obj[0], obj[1] = x, y; moved += 1
                    break
    if getattr(env, "use_proxy_fields", False) and hasattr(env, "_compute_proximity_fields"):
        env._compute_proximity_fields()
    return moved


class EnvProxy:
    """Delegates to the real env; substitutes the executed action when .override is set."""

    def __init__(self, env):
        self.__dict__["_env"] = env
        self.__dict__["override"] = None
        self.__dict__["last_exec"] = None

    def __getattr__(self, k):
        return getattr(self._env, k)

    def __setattr__(self, k, v):
        if k in ("override", "last_exec", "_env"):
            self.__dict__[k] = v
        else:
            setattr(self._env, k, v)

    def step(self, action):
        if self.override is not None:
            act = torch.zeros(1, self._env.action_dim)
            act[0, int(self.override)] = 1.0
        else:
            act = action
        self.__dict__["last_exec"] = act.detach().clone().reshape(1, -1)
        self.__dict__["override"] = None
        # continuous life: health pinned at 1.0 around every step (harm is still delivered as the
        # step's harm signal; only the death -> reset path is removed). Same in every life.
        self._env.agent_health = 1.0
        res = self._env.step(act)
        self._env.agent_health = 1.0
        return res


def set_knobs(agent):
    for k in KNOBS:
        setattr(agent.config.latent, k, True)
        if hasattr(agent, "latent_stack") and hasattr(agent.latent_stack, "config"):
            setattr(agent.latent_stack.config, k, True)
    assert all(getattr(agent.latent_stack.config, k) for k in KNOBS)


class _BarStub:
    """Carries exactly what E3TrajectorySelector._variance_tracking_commit_bar reads, so the
    NATIVE ARC-029(D) estimator is used verbatim on a probe-side series."""

    def __init__(self, q, w):
        self._commit_gate_variance_window = deque(maxlen=w)
        self.config = types.SimpleNamespace(commit_threshold_quantile=q)

    def bar(self):
        return E3TrajectorySelector._variance_tracking_commit_bar(self)


# ------------------------------------------------------------------ premise audits (cheap, D0/D1)
premise = {}
try:
    from ree_core.utils.config import REEConfig
    env_tmp = CausalGridWorldV2(size=8, seed=1)
    cfg_tmp = REEConfig.from_dims(body_obs_dim=env_tmp.body_obs_dim, world_obs_dim=env_tmp.world_obs_dim,
                                  action_dim=env_tmp.action_dim)
    premise["d_defaults"] = {"commit_threshold_quantile": cfg_tmp.e3.commit_threshold_quantile,
                             "commit_threshold_quantile_window": cfg_tmp.e3.commit_threshold_quantile_window,
                             "commitment_threshold": cfg_tmp.e3.commitment_threshold,
                             "precision_init": cfg_tmp.e3.precision_init,
                             "precision_ema_alpha": cfg_tmp.e3.precision_ema_alpha}
    cfg_tmp.e3.use_variance_tracking_commit_threshold = True
    try:
        E3TrajectorySelector._build_commit_gate_window(types.SimpleNamespace(config=cfg_tmp.e3))
        premise["d_raises_if_unset"] = False
    except ValueError as ex:
        premise["d_raises_if_unset"] = True
        premise["d_raise_msg_head"] = str(ex)[:120]
except Exception as ex:  # report, never crash on an audit
    premise["d_error"] = repr(ex)

# ------------------------------------------------------------------ phase 0: reference + TE
lock_acquire("seed%d-S1" % S)      # BEFORE any heavy compute
R.seed_all(S)
_e, ref, _c = R.build_B(S, False)
set_knobs(ref)
ref.eval()
ref_enc = copy.deepcopy(ref.latent_stack.state_dict())
init = BP.get_head(ref)
if not a.smoke:
    te_segs, _ = BB.gen_policy(S, 3000 // BB.EP_STEPS, 120, BB.pol_uniform(S * 7 + 3))
else:
    te_segs, _ = BB.gen_policy(S, 1, 120, BB.pol_uniform(S * 7 + 3))
TE = BB.encode_segs(ref, te_segs)
ev_init = BB.evaluate(ref, init, TE, "z", S)
log("INIT disc4 %.4f k %d | premise %s" % (ev_init["disc4_h1"], ev_init["k"], premise))


# ------------------------------------------------------------------ life runner
def run_life(snap, name, stage):
    pol, kind = name.split("-")
    change = kind != "none"
    ag = copy.deepcopy(snap)
    tr = ag.waking_trainer
    tr.every_k = 10 ** 9            # frozen: no member updates during a test life
    e3cfg = ag.e3.config
    base_thr = float(e3cfg.commitment_threshold)
    R.seed_all(S + 900 + (0 if stage == "S1" else 50))
    env_real = make_life_env(150 if stage == "S1" else 151)
    env = EnvProxy(env_real)
    prng = np.random.default_rng(S + 4242)
    lrng = np.random.default_rng(S + 5151)
    own = _BarStub(a.own_q, a.own_window)
    alpha = float(e3cfg.precision_ema_alpha)
    st = {"prev_pred": None, "ema": None, "raw_real": float("nan")}
    rec = {k: [] for k in ("raw_mix", "rv", "raw_real", "ema_real", "committed", "e3_tick", "act", "sel",
                           "probe", "harm", "reset", "own_bar", "own_dec")}
    ev = {"resets": [], "changed_at": None, "relayout_moved": None}

    def on_sense(agent, latent, step, **kw):
        t = step
        if st["prev_pred"] is not None:
            e = float(((latent.z_world.detach() - st["prev_pred"]) ** 2).mean())
            st["raw_real"] = e
            st["ema"] = e if st["ema"] is None else (1 - alpha) * st["ema"] + alpha * e
        else:
            st["raw_real"] = float("nan")
        if change and t == a.tc:
            if kind == "perm":
                env_real._action_map = dict(SHIFTED)
            elif kind == "layout":
                ev["relayout_moved"] = relayout(env_real, lrng)
            ev["changed_at"] = t
        bar = None
        dec = None
        if pol == "FC" or pol == "CP" or pol == "RND":
            e3cfg.commitment_threshold = 1e9
        elif pol == "FS":
            e3cfg.commitment_threshold = -1.0
        elif pol == "OWN":
            bar = own.bar()
            x = st["ema"]
            if bar is None or x is None:
                dec = True               # warmup -> native fallback (absolute bar; rv << 0.40 -> committed)
            else:
                dec = bool(x < bar)
            e3cfg.commitment_threshold = 1e9 if dec else -1.0
            if x is not None and math.isfinite(x):
                own._commit_gate_variance_window.append(x)   # AFTER the decision (strictly causal)
        else:
            e3cfg.commitment_threshold = base_thr
        rec["own_bar"].append(bar); rec["own_dec"].append(dec)
        rec["raw_real"].append(st["raw_real"]); rec["ema_real"].append(st["ema"])

    def on_action(agent, action, step, **kw):
        probe = False
        u = prng.random(); c = int(prng.integers(0, 4))
        if (pol == "CP" and u < a.probe_rate) or pol == "RND":
            env.override = c
            probe = True
        rec["probe"].append(probe)
        rec["sel"].append(int(action.reshape(-1).argmax()))

    def on_post_step(agent, latent, residue_metrics, harm_signal, ticks, **kw):
        aex = env.last_exec
        with torch.no_grad():
            st["prev_pred"] = agent.e2.world_forward(latent.z_world.detach(), aex.to(latent.z_world.dtype)).detach()
        pe = residue_metrics.get("e3_prediction_error")
        rec["raw_mix"].append(float(pe.detach().item()) if torch.is_tensor(pe) else (float(pe) if pe is not None else None))
        cs = agent.e3.get_commitment_state()
        rec["rv"].append(float(cs["running_variance"]))
        rec["committed"].append(bool(cs["committed_now"]))
        rec["e3_tick"].append(bool(ticks.get("e3_tick", False)))
        rec["act"].append(int(aex.reshape(-1).argmax()))
        rec["harm"].append(float(harm_signal))

    hh = StepHarness(ag, env, train_mode=False, seed=S * 1000 + 777,
                     hooks=StepHooks(on_sense=on_sense, on_action=on_action, on_post_step=on_post_step))
    _f, od = env.reset(); ag.reset(); hh.reset()
    rv_before_reset = None
    tl = time.time()
    for t in range(a.life):
        r = hh.step(od)
        od = r.next_obs_dict
        rec["reset"].append(bool(r.done))
        if r.done:
            ev["resets"].append(t)
            rv_before_reset = ag.e3._running_variance
            _f, od = env.reset(); ag.reset(); hh.reset()
            ev.setdefault("rv_persist_check", []).append([rv_before_reset, ag.e3._running_variance])
            st["prev_pred"] = None
    e3cfg.commitment_threshold = base_thr
    out = {"name": name, "stage": stage, "policy": pol, "kind": kind, "secs": time.time() - tl,
           "events": ev, "rec": rec}
    ex = np.array(rec["act"])
    log("LIFE %s %-10s %.0fs resets %s commit %.3f probes %d act-hist %s" % (
        stage, name, out["secs"], ev["resets"], float(np.mean(rec["committed"])), int(np.sum(rec["probe"])),
        np.bincount(ex, minlength=5).tolist()))
    return out


# ------------------------------------------------------------------ phase 1: W3 protocol + S1 dose
out = {"seed": S, "args": vars(a), "wt": a.wt, "premise": premise, "init": ev_init, "stages": {}}


def dump():
    json.dump(out, open(a.out, "w"), default=lambda o: None if isinstance(o, float) and not math.isfinite(o) else str(o))


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
n_bab_eps = 1 if a.smoke else 12
with torch.no_grad():
    for k in range(n_bab_eps):
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
ev_pre = BB.evaluate(ref, BP.get_head(agent), TE, "z", S)
tr.set_e2_world_source("on_policy")
tr.every_k = 1
member.updates_per_step = a.ups
agent.reset()
R.seed_all(S + 500)
rv_first = []


def native_dose(n_steps, k0):
    n_eps = max(1, n_steps // BB.EP_STEPS)
    for ep in range(n_eps):
        env = BB.make_env(S, k0 + ep)
        hh = StepHarness(agent, env, train_mode=False, seed=S * 1000 + k0 + ep)
        _f, od = env.reset(); agent.reset(); hh.reset()
        for _s in range(min(BB.EP_STEPS, n_steps)):
            r = hh.step(od)
            if len(rv_first) < 12:
                rv_first.append(float(agent.e3._running_variance))
            od = r.next_obs_dict
            if r.done:
                _f, od = env.reset(); agent.reset(); hh.reset()


tdose = time.time()
native_dose(a.s1, 50)
ev_s1 = BB.evaluate(ref, BP.get_head(agent), TE, "z", S)
cross = next((i for i, v in enumerate(rv_first) if v < 0.40), None)
out["premise"]["c_rv_first12_native"] = rv_first
out["premise"]["c_first_index_below_0p40"] = cross
log("W3 pre disc4 %.4f | S1 disc4 %.4f k %d (bar 0.47 %s) | dose %.0fs | rv first %s cross@%s" % (
    ev_pre["disc4_h1"], ev_s1["disc4_h1"], ev_s1["k"], ev_s1["disc4_h1"] >= 0.47, time.time() - tdose,
    [round(v, 4) for v in rv_first[:7]], cross))
rv_b = float(agent.e3._running_variance)
agent.reset()
out["premise"]["b_rv_before_after_agent_reset"] = [rv_b, float(agent.e3._running_variance)]
copy._deepcopy_dispatch[types.ModuleType] = lambda x, memo: x
SNAP = copy.deepcopy(agent)
out["stages"]["S1"] = {"disc4": ev_s1, "pre_disc4": ev_pre, "screen_pass": bool(ev_s1["disc4_h1"] >= 0.47),
                       "rv_at_snapshot": float(agent.e3._running_variance), "lives": {}}
dump()
for j, nm in enumerate([x for x in a.lives_s1.split(",") if x]):
    maybe_rehold("seed%d-S1-%d" % (S, j))
    out["stages"]["S1"]["lives"][nm] = run_life(SNAP, nm, "S1")
    dump()
lock_release(HELD["label"] or "seed%d-S1" % S)
if a.s2_extra <= 0 or not a.lives_s2:
    out["t_total_s"] = time.time() - t0
    dump(); log("DONE (no S2) %.0fs" % out["t_total_s"]); sys.exit(0)
time.sleep(0 if a.no_lock else 45)

# ------------------------------------------------------------------ phase 3: S2 dose + lives
lock_acquire("seed%d-S2" % S)
del SNAP
tdose = time.time()
native_dose(a.s2_extra, 56)
ev_s2 = BB.evaluate(ref, BP.get_head(agent), TE, "z", S)
log("S2 disc4 %.4f k %d | dose %.0fs" % (ev_s2["disc4_h1"], ev_s2["k"], time.time() - tdose))
agent.reset()
SNAP2 = copy.deepcopy(agent)
out["stages"]["S2"] = {"disc4": ev_s2, "rv_at_snapshot": float(agent.e3._running_variance), "lives": {}}
dump()
for j, nm in enumerate([x for x in a.lives_s2.split(",") if x]):
    maybe_rehold("seed%d-S2-%d" % (S, j))
    out["stages"]["S2"]["lives"][nm] = run_life(SNAP2, nm, "S2")
    dump()
lock_release(HELD["label"] or "seed%d-S2" % S)
out["t_total_s"] = time.time() - t0
dump()
log("DONE %.0fs" % out["t_total_s"])
