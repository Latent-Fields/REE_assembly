"""Probe DCH2 / N5b (bt0926-dch2): does an unexpected-uncertainty (change-point) statistic, fed by
regime-surviving probe bouts, detect the action-map shift that N5's magnitude gate missed?

Audit H2 stage 1 (dynamic_control_audit_20260926.md sec B H2), a detector-only test on N5's CLAMPED
pair: {probe bouts OFF / ON} x {change-point statistic CP / N5 magnitude statistic MAG}, under shift
and no shift, no unfreeze. The statistic factor is computed on the SAME record stream of each cell,
so one cell serves both statistics. Report-only: a 25% probe-budget pair (F3), a per-source magnitude
variant (attribution), and a rate-matched random trigger (computed post hoc by the analyser).

Code under test: ree-v3 4070b0efa4 (archive/coupled-loop-repair-4070b0e), private detached worktree.
NO ree_core edits: shift, probes, statistics and g are harness-side.

One process = one seed:
  0. reference build (build_B, world_dim 32), reset-init knobs ON (4), held-out TE_orig (W3 set).
  1. W3 member protocol verbatim (N5 phase 1): babble 2400 -> FROZEN retained set, 3000 updates,
     1200 native StepHarness steps x 8 updates. P-a pre-screen: disc4_h1 on TE_orig >= 0.47
     (the 4070b0e W3 gate (a)). A failing seed stops here (unless --force).
  2. snapshot; BASELINE-CALIBRATION life on a deepcopy (original map, trainer frozen, 8% probe
     schedule, env seeds k = 40..): per-source (on_policy / probe) mean and variance of the
     action-contrastive one-step error `ac` from the snapshot head, out of sample. Identical for
     every cell (the expected-uncertainty model's initial state).
  3. cells (each from the snapshot, R.seed_all(S+700)): N adult steps, clamped g = 0.1 (member lr
     3e-5, 8 updates / step, retained set FROZEN, probe records scored only, never trained on),
     native 200-step episodes, env seeds k = 61..; SHIFT applied mid-episode at adult step T_S
     (the running env's _action_map is overwritten; later envs are built shifted).
     Probe schedule: steps with (t mod 100) >= 100 - B are probe steps: the agent still selects,
     the env executes a StructuredBabbler action instead (EnvProxy override) and the record is
     tagged source 'babble' (= probe). No reset, same env.
  Per record: z = (ac - mu_src) / sd_src; baselines EMA-updated (alpha_b) per source.
     MAG (N5 verbatim): s = EMA(z, 0.05) over the merged stream, a = EMA(1[s > 0.75], 0.05),
       g_would = 0.1 + 0.9 a; alarm = rising edge of (s > 0.75 AND g_would > 0.5).
     MAGps (report-only): the same rule run separately per source; alarm if either source.
     CP: per-source one-sided CUSUM C = max(0, C + z - K), alarm when C > H, then C = 0;
       Cnr = the same CUSUM never reset (threshold-free window score).
  Per step: executed class, source, informative (orig vs shifted map give different displacement
     from this cell), moved.
ASCII output only.
"""
from __future__ import annotations

import argparse, atexit, copy, json, os, select, signal, subprocess, sys, time, types
from pathlib import Path

import numpy as np
import torch

p = argparse.ArgumentParser()
p.add_argument("--seed", type=int, required=True)
p.add_argument("--wt", required=True)
p.add_argument("--out", required=True)
p.add_argument("--cells", default="shift_off,noshift_off,shift_on8,noshift_on8,shift_on25,noshift_on25")
p.add_argument("--n-adult", type=int, default=1200)
p.add_argument("--t-shift", type=int, default=700)
p.add_argument("--calib-steps", type=int, default=600)
p.add_argument("--post", type=int, default=1200)
p.add_argument("--ups", type=int, default=8)
p.add_argument("--g-low", type=float, default=0.1)
p.add_argument("--alpha-b", type=float, default=0.005)
p.add_argument("--mag-alpha", type=float, default=0.05)
p.add_argument("--mag-thr", type=float, default=0.75)
p.add_argument("--mag-alpha-g", type=float, default=0.05)
p.add_argument("--mag-g-thr", type=float, default=0.5)
p.add_argument("--cp-k", type=float, default=0.5)
p.add_argument("--cp-h", type=float, default=5.0)
p.add_argument("--force", action="store_true")
p.add_argument("--max-hold", type=float, default=720.0)
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
from ree_core.environment.causal_grid_world import CausalGridWorld  # noqa: E402

S = a.seed
t0 = time.time()
BASE_LR = 3e-4
SHIFT_P = [2, 3, 1, 0]
PERIOD = 100
LOCK = "/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/mac_probe.lock"
KNOBS = ("use_zworld_ema_reset_init", "use_zself_ema_reset_init",
         "use_shared_ema_reset_init", "use_zharm_ema_reset_init")
ON, BAB = WT.SOURCE_ON_POLICY, WT.SOURCE_BABBLE


def log(m):
    print("[dch2 s%d t=%5.0fs] %s" % (S, time.time() - t0, m), flush=True)


assert str(Path(WT.__file__).resolve()).startswith(str(Path(a.wt).resolve())), WT.__file__


# ------------------------------------------------------------------ Mac probe lock
def _freemb():
    out = subprocess.run(["vm_stat"], capture_output=True, text=True).stdout
    ps = int(out.split("page size of")[1].split()[0]); f = i = 0
    for ln in out.splitlines():
        if ln.startswith("Pages free"): f = int(ln.split()[-1].rstrip("."))
        if ln.startswith("Pages inactive"): i = int(ln.split()[-1].rstrip("."))
    return (f + i) * ps // 1048576


HELD = {"label": None, "t": 0.0}


def lock_acquire(label):
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
    with open(os.path.join(LOCK, "owner"), "w") as fh:     # owner file ONLY after our mkdir
        fh.write("bt0926-dch2 %s %s pid %d\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                                                 label, os.getpid()))
    HELD["label"] = label
    HELD["t"] = time.time()
    log("LOCK ACQUIRED %s (waited %.0fs)" % (label, time.time() - tw))


def lock_release():
    if HELD["label"] is None:
        return
    try:
        os.remove(os.path.join(LOCK, "owner"))
    except FileNotFoundError:
        pass
    try:
        os.rmdir(LOCK)
    except FileNotFoundError:
        pass
    lab = HELD["label"]
    HELD["label"] = None
    mine = False
    try:
        mine = "bt0926-dch2" in open(os.path.join(LOCK, "owner")).read() and str(os.getpid()) in open(os.path.join(LOCK, "owner")).read()
    except Exception:
        pass
    log("LOCK RELEASED %s (verified: our owner file gone=%s, held %.0fs)" % (lab, not mine, time.time() - HELD["t"]))


def maybe_rehold(label):
    if HELD["label"] is not None and time.time() - HELD["t"] > a.max_hold:
        lock_release()
        time.sleep(45)
        lock_acquire(label)


def _atexit(*_x):
    lock_release()
    if _x:
        sys.exit(143)


atexit.register(_atexit)
signal.signal(signal.SIGTERM, _atexit)

# ------------------------------------------------------------------ env helpers
BASE_ACTIONS = dict(CausalGridWorld.ACTIONS)
SHIFTED = dict(BASE_ACTIONS)
for c in range(4):
    SHIFTED[c] = BASE_ACTIONS[SHIFT_P[c]]
assert all(SHIFTED[c] != BASE_ACTIONS[c] for c in range(4)) and SHIFTED[4] == BASE_ACTIONS[4]


def set_knobs(agent):
    for k in KNOBS:
        setattr(agent.config.latent, k, True)
        if hasattr(agent, "latent_stack") and hasattr(agent.latent_stack, "config"):
            setattr(agent.latent_stack.config, k, True)
    assert all(getattr(agent.latent_stack.config, k) for k in KNOBS)


def disp(env, c, amap):
    dx, dy = amap[c]
    nx, ny = env.agent_x + dx, env.agent_y + dy
    if not (0 <= nx < env.size and 0 <= ny < env.size):
        return (0, 0)
    if env.grid[nx, ny] == env.ENTITY_TYPES["wall"]:
        return (0, 0)
    return (dx, dy)


class EnvProxy:
    """Delegates to the real env; when .override is set the env executes that class instead and
    the agent's _last_action (what the E2 member records) is set to the executed one-hot."""

    def __init__(self, env, agent, steplog):
        self.__dict__.update(_env=env, _agent=agent, override=None, _log=steplog)

    def __getattr__(self, k):
        return getattr(self._env, k)

    def __setattr__(self, k, v):
        if k in ("override", "_env", "_agent", "_log"):
            self.__dict__[k] = v
        else:
            setattr(self._env, k, v)

    def step(self, action):
        env = self._env
        if self.override is not None:
            act = self.override
            self._agent._last_action = act.clone()
            src = "probe"
        else:
            act = action
            src = "on"
        c = int(act.reshape(-1).argmax())
        d_o, d_s = disp(env, c, BASE_ACTIONS), disp(env, c, SHIFTED)
        x0, y0 = env.agent_x, env.agent_y
        self.__dict__["override"] = None
        res = env.step(act)
        self._log.append((src, c, int(d_o != d_s), int((env.agent_x, env.agent_y) != (x0, y0))))
        return res


# ------------------------------------------------------------------ phase 0: reference + TE
lock_acquire("seed%d-A" % S)
R.seed_all(S)
_e, ref, _c = R.build_B(S, False)
set_knobs(ref)
ref.eval()
ref_enc = copy.deepcopy(ref.latent_stack.state_dict())
init = BP.get_head(ref)
te_segs, _ = BB.gen_policy(S, (3000 if not a.smoke else 400) // BB.EP_STEPS, 120, BB.pol_uniform(S * 7 + 3))
TE = BB.encode_segs(ref, te_segs)
ev_init = BB.evaluate(ref, init, TE, "z", S)
log("INIT disc4 %.4f k %d" % (ev_init["disc4_h1"], ev_init["k"]))

# ------------------------------------------------------------------ phase 1: W3 member protocol (g = 1)
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
    for k in range(12 if not a.smoke else 2):
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
retained_n0 = len(member._retained)
for _u in range(3000 if not a.smoke else 200):
    tr._update("e2_world", member)
ev_pre = BB.evaluate(ref, BP.get_head(agent), TE, "z", S)
tr.set_e2_world_source("on_policy")
tr.every_k = 1
member.updates_per_step = a.ups
agent.reset()
R.seed_all(S + 500)
for ep in range(a.post // BB.EP_STEPS):
    env = BB.make_env(S, 50 + ep)
    hh = StepHarness(agent, env, train_mode=False, seed=S * 1000 + 50 + ep)
    _f, od = env.reset(); agent.reset(); hh.reset()
    for _s in range(BB.EP_STEPS):
        r = hh.step(od)
        od = r.next_obs_dict
        if r.done:
            _f, od = env.reset(); agent.reset(); hh.reset()
ev_ps = BB.evaluate(ref, BP.get_head(agent), TE, "z", S)
pre_bar = bool(ev_ps["disc4_h1"] >= 0.47)
log("retained %d | pre(babble) disc4 %.4f | PRE-SHIFT (end W3 protocol) disc4 %.4f k %d -> P-a bar %s" % (
    retained_n0, ev_pre["disc4_h1"], ev_ps["disc4_h1"], ev_ps["k"], pre_bar))
out = {"seed": S, "args": vars(a), "code_sha": "4070b0efa4", "wt": a.wt, "knobs_on": list(KNOBS),
       "init": ev_init, "pre_babble": ev_pre, "pre_shift": ev_ps, "pa_pass": pre_bar,
       "retained_n0": retained_n0, "cells": {}}
json.dump(out, open(a.out, "w"), indent=1, default=str)
if not pre_bar and not a.force:
    out["t_total_s"] = time.time() - t0
    json.dump(out, open(a.out, "w"), indent=1, default=str)
    log("P-a FAIL: seed rejected by the pre-screen; no cells run. DONE %.0fs" % out["t_total_s"])
    sys.exit(0)

agent.reset()
copy._deepcopy_dispatch[types.ModuleType] = lambda x, memo: x   # modules shared, not copied
SNAP = copy.deepcopy(agent)
log("snapshot ok (on-policy %d, retained %d)" % (len(member._on_policy), len(member._retained)))


# ------------------------------------------------------------------ life runner
def run_life(shift, probe_b, n_steps, train, k0, stats_base=None, rseed=700):
    """One adult life from SNAP. probe_b = probe steps per PERIOD (0 = OFF). Returns dict."""
    ag = copy.deepcopy(SNAP)
    trc = ag.waking_trainer
    mem = trc.members["e2_world"]
    opt = trc.optimizers["e2_world"]
    assert mem._agent is ag and trc._agent is ag
    retained_before = len(mem._retained)
    if train:
        trc.every_k = 1
        for pg in opt.param_groups:
            pg["lr"] = BASE_LR * a.g_low
    else:
        trc.every_k = 10 ** 9
    R.seed_all(S + rseed)
    bab_c = StructuredBabbler(n_classes=5, max_run=4, seed=S * 17 + 5 + rseed)
    steplog = []
    recs = []          # per record: (gstep, src, pe, ac, z, s_mag, g_would, C_on, C_bab, Cnr_on, Cnr_bab, sps_on, sps_bab)
    G = {"n": 0}
    base = None if stats_base is None else copy.deepcopy(stats_base)
    st = {"s": 0.0, "ar": 0.0, "coinc": False, "C": {"on": 0.0, "bab": 0.0}, "Cnr": {"on": 0.0, "bab": 0.0},
          "sps": {"on": 0.0, "bab": 0.0}, "arps": {"on": 0.0, "bab": 0.0}, "coincps": False}
    alarms = {"MAG": [], "MAGps": [], "CP": [], "CP_on": [], "CP_bab": []}

    @torch.no_grad()
    def rec_stats(rec):
        z0, z1 = rec["z_live"]
        aex = int(rec["a"].reshape(-1).argmax())
        pred = ag.e2.world_forward(z0.expand(5, -1), torch.eye(5, dtype=z0.dtype))
        le = torch.log(((pred - z1) ** 2).mean(dim=-1) + 1e-12)
        pe = float(le[aex])
        alt = torch.cat([le[:aex], le[aex + 1:]])
        return pe, pe - float(alt.min())

    def store(rec):
        src = "on" if rec["source"] == ON else "bab"
        pe, ac = rec_stats(rec)
        gs = G["n"]
        row = [gs, src, pe, ac]
        if base is not None:
            mu, var = base[src]
            z = (ac - mu) / max(np.sqrt(var), 1e-6)
            mu2 = mu + a.alpha_b * (ac - mu)
            base[src] = [mu2, var + a.alpha_b * ((ac - mu) * (ac - mu2) - var)]
            # MAG (N5 verbatim, merged stream)
            st["s"] += a.mag_alpha * (z - st["s"])
            st["ar"] += a.mag_alpha_g * (float(st["s"] > a.mag_thr) - st["ar"])
            gw = a.g_low + (1.0 - a.g_low) * st["ar"]
            c_now = bool(st["s"] > a.mag_thr and gw > a.mag_g_thr)
            if c_now and not st["coinc"]:
                alarms["MAG"].append(gs)
            st["coinc"] = c_now
            # MAGps (report-only): same rule per source
            st["sps"][src] += a.mag_alpha * (z - st["sps"][src])
            st["arps"][src] += a.mag_alpha_g * (float(st["sps"][src] > a.mag_thr) - st["arps"][src])
            cps = any(st["sps"][q] > a.mag_thr and a.g_low + (1 - a.g_low) * st["arps"][q] > a.mag_g_thr
                      for q in ("on", "bab"))
            if cps and not st["coincps"]:
                alarms["MAGps"].append(gs)
            st["coincps"] = cps
            # CP: per-source one-sided CUSUM
            st["Cnr"][src] = max(0.0, st["Cnr"][src] + z - a.cp_k)
            st["C"][src] = max(0.0, st["C"][src] + z - a.cp_k)
            if st["C"][src] > a.cp_h:
                alarms["CP"].append(gs)
                alarms["CP_" + src].append(gs)
                st["C"][src] = 0.0
            row += [z, st["s"], gw, st["C"]["on"], st["C"]["bab"], st["Cnr"]["on"], st["Cnr"]["bab"],
                    st["sps"]["on"], st["sps"]["bab"]]
        recs.append(row)
        if src == "on":
            mem._on_policy.append(rec)      # clamped pair: on-policy trained at g = G_LOW
        # probe records: scored only; retained set stays FROZEN, never trained on

    mem._store = store
    k_env = k0
    shifted = {"on": False}
    while G["n"] < n_steps:
        k_env += 1
        env_real = BB.make_env(S, k_env)
        if shifted["on"]:
            env_real._action_map = dict(SHIFTED)
        env = EnvProxy(env_real, ag, steplog)

        def on_action(agent, latent, action, obs_dict, ticks, step, **kw):
            t = G["n"]
            if probe_b and (t % PERIOD) >= PERIOD - probe_b:
                if (t % PERIOD) == PERIOD - probe_b:
                    bab_c.reset()
                env.override = bab_c.next_action()
                mem.source = BAB
            else:
                mem.source = ON

        hh = StepHarness(ag, env, train_mode=False, seed=S * 1000 + k_env, hooks=StepHooks(on_action=on_action))
        _f, od = env.reset(); ag.reset(); hh.reset()
        for _s in range(BB.EP_STEPS):
            if G["n"] >= n_steps:
                break
            if shift and G["n"] == a.t_shift and not shifted["on"]:
                env_real._action_map = dict(SHIFTED)
                shifted["on"] = True
            r = hh.step(od)
            G["n"] += 1
            od = r.next_obs_dict
            if r.done:
                _f, od = env.reset(); ag.reset(); hh.reset()
        ag.reset()
        mem.source = ON
    return {"recs": recs, "steplog": steplog, "alarms": alarms, "base_end": base,
            "retained_unchanged": len(mem._retained) == retained_before, "shifted": shifted["on"],
            "updates": dict(trc.steps)}


# ------------------------------------------------------------------ phase 2: baseline calibration life
maybe_rehold("seed%d-B" % S)
cal = run_life(False, 8, a.calib_steps, False, 39, stats_base=None, rseed=650)
BASE0 = {}
for src in ("on", "bab"):
    v = [r[3] for r in cal["recs"] if r[1] == src]
    BASE0[src] = [float(np.mean(v)), float(np.var(v))]
cal_pe = {src: float(np.mean([r[2] for r in cal["recs"] if r[1] == src])) for src in ("on", "bab")}
sl = cal["steplog"]
log("CALIB n_rec on %d probe %d | ac mu/var on %.3f/%.3f probe %.3f/%.3f | pe on %.2f probe %.2f" % (
    sum(1 for r in cal["recs"] if r[1] == "on"), sum(1 for r in cal["recs"] if r[1] == "bab"),
    BASE0["on"][0], BASE0["on"][1], BASE0["bab"][0], BASE0["bab"][1], cal_pe["on"], cal_pe["bab"]))
out["baseline0"] = BASE0
out["calib_pe_mean"] = cal_pe
out["calib_steplog_summary"] = {
    src: {"n": sum(1 for x in sl if x[0] == src),
          "informative": float(np.mean([x[2] for x in sl if x[0] == src] or [np.nan])),
          "moved": float(np.mean([x[3] for x in sl if x[0] == src] or [np.nan])),
          "class_frac": [float(np.mean([x[1] == c for x in sl if x[0] == src] or [np.nan])) for c in range(5)]}
    for src in ("on", "probe")}
json.dump(out, open(a.out, "w"), indent=1, default=str)

PB = {"off": 0, "on8": 8, "on25": 25}
for cell in [c for c in a.cells.split(",") if c]:
    maybe_rehold("seed%d-%s" % (S, cell))
    shift = cell.startswith("shift_")
    pb = PB[cell.split("_", 1)[1]]
    tc = time.time()
    res = run_life(shift, pb, a.n_adult, True, 60, stats_base=BASE0, rseed=700)
    sl = res["steplog"]
    summ = {}
    for src in ("on", "probe"):
        for per, lo, hi in (("pre", 0, a.t_shift), ("post", a.t_shift, a.n_adult)):
            rows = [x for i, x in enumerate(sl) if x[0] == src and lo <= i < hi]
            summ["%s_%s" % (src, per)] = {
                "n": len(rows),
                "informative": float(np.mean([x[2] for x in rows])) if rows else None,
                "moved": float(np.mean([x[3] for x in rows])) if rows else None,
                "class_frac": [float(np.mean([x[1] == c for x in rows])) if rows else None for c in range(5)]}
    zs = {}
    for src in ("on", "bab"):
        for per, lo, hi in (("pre", 0, a.t_shift), ("post", a.t_shift, a.n_adult)):
            v = [r[4] for r in res["recs"] if r[1] == src and lo <= r[0] < hi]
            zs["%s_%s" % (src, per)] = [len(v), float(np.mean(v)) if v else None]
    al = res["alarms"]
    log("CELL %-13s %.0fs | alarms MAG %d CP %d (on %d bab %d) MAGps %d | post-shift-window MAG %d CP %d | z %s | inf on-post %s probe-post %s | retained_unchanged %s" % (
        cell, time.time() - tc, len(al["MAG"]), len(al["CP"]), len(al["CP_on"]), len(al["CP_bab"]), len(al["MAGps"]),
        sum(1 for x in al["MAG"] if x >= a.t_shift), sum(1 for x in al["CP"] if x >= a.t_shift),
        {k: (v[0], None if v[1] is None else round(v[1], 2)) for k, v in zs.items()},
        summ["on_post"]["informative"], summ["probe_post"]["informative"], res["retained_unchanged"]))
    out["cells"][cell] = {"shift": shift, "probe_b": pb, "alarms": al, "z_summary": zs, "steplog_summary": summ,
                          "retained_unchanged": res["retained_unchanged"], "shifted": res["shifted"],
                          "base_end": res["base_end"], "updates": res["updates"],
                          "recs": [[round(x, 4) if isinstance(x, float) else x for x in r] for r in res["recs"]],
                          "steplog": sl}
    json.dump(out, open(a.out, "w"), indent=1, default=str)

out["t_total_s"] = time.time() - t0
json.dump(out, open(a.out, "w"), indent=1, default=str)
log("DONE %.0fs" % out["t_total_s"])
