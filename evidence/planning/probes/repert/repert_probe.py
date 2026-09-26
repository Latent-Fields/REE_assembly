"""Probe R (bt0926-repert): where is E3 candidate / action-class diversity lost?

DCD2 follow-on to probe C (REE_assembly 6f45386213 sec 2.4 item 5: forced sampling executed one
class on 81-99% of ticks on 4/5 seeds). One process = one seed. Code under test: ree-v3
4070b0efa4 (archive/coupled-loop-repair-4070b0e, has W1-alt ASP), private detached worktree.
NO ree_core edits: every readout is harness-side (StepHarness hooks, an instance-level wrapper
around agent.e3.select that only records, an env proxy that pins health and records the executed
action). Config knobs are set on the probe's own deep copies only.

Per E3 tick (the tick the proposer and E3 actually ran) it records:
  PROPOSALS  final pool handed to E3: K, first-action continuous vectors (class via argmax, as the
             env decodes it), their spread, sources; for the native codec CEM also the
             iteration-0 pre-refit class counts (the raw decoder cloud before any score refit).
  DECODE     the same first-action cloud after removing its pool mean (centred argmax) -- the
             class spread the continuous cloud would express without a common offset; agreement of
             each candidate's class with the argmax of the pool-mean vector.
  SCORING    E3's post-bias scores, the deployed (effective) temperature, the softmax over
             candidates (e3.last_precommit_probs), and its mass per first-action class; a
             score-shuffle control (probs permuted over candidates, 64 draws).
  SELECTION  the selected candidate's class and E3's committed flag.
Every tick: EXECUTION = the class the env actually received (after the beta gate / hold / freeze).

Arms per seed: training {U untrained, T W3-trained at S1} x proposer {NAT codec CEM, ASPE
stratified, ASP0 stratified_uniform} x commitment {NATc native gate, OFF forced uncommitted}.
Mac CPU lock: mkdir lock BEFORE compute, owner file after mkdir, <= max-hold s per hold (rotated at
life / dose-episode boundaries), >= gap s after each release before re-acquiring, never broken.
ASCII output only.
"""
from __future__ import annotations

import argparse, copy, json, math, os, select, subprocess, sys, time, types

import numpy as np
import torch

p = argparse.ArgumentParser()
p.add_argument("--seed", type=int, required=True)
p.add_argument("--wt", required=True)
p.add_argument("--out", required=True)
p.add_argument("--s1", type=int, default=1200)
p.add_argument("--ups", type=int, default=8)
p.add_argument("--life", type=int, default=400)
p.add_argument("--n-shuf", type=int, default=64)
p.add_argument("--max-hold", type=float, default=720.0)
p.add_argument("--gap", type=float, default=180.0)
p.add_argument("--no-lock", action="store_true")
p.add_argument("--smoke", action="store_true")
a = p.parse_args()

PROBES = "/Users/dgolden/REE_Working/REE_assembly/evidence/planning/probes"
sys.path.insert(0, PROBES + "/babble")
sys.path.insert(0, PROBES + "/rollout")
sys.path.insert(0, a.wt + "/experiments")
sys.path.insert(0, a.wt)
torch.set_num_threads(2)

import babble_probe as BB  # noqa: E402
import rollout_fidelity_probe as R  # noqa: E402
import balanced_replay_probe as BP  # noqa: E402
from experiments._harness import StepHarness, StepHooks  # noqa: E402
from ree_core.utils import waking_trainer as WT  # noqa: E402
from ree_core.developmental.structured_babbling import StructuredBabbler  # noqa: E402
from ree_core.environment.causal_grid_world import CausalGridWorldV2  # noqa: E402
from ree_core.hippocampal.module import HippocampalModule  # noqa: E402

S = a.seed
t0 = time.time()
BASE_LR = 3e-4
LOCK = "/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/mac_probe.lock"
LAST_REL = "/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/repert/results/.last_release"
KNOBS = ("use_zworld_ema_reset_init", "use_zself_ema_reset_init",
         "use_shared_ema_reset_init", "use_zharm_ema_reset_init")
PROPS = {"NAT": None, "ASPE": "stratified", "ASP0": "stratified_uniform"}
COMMITS = ("NATc", "OFF")
A_DIM = 5


def log(m):
    print("[rp s%d t=%5.0fs] %s" % (S, time.time() - t0, m), flush=True)


import os.path as _op  # noqa: E402
assert _op.realpath(WT.__file__).startswith(_op.realpath(a.wt)), WT.__file__


# ------------------------------------------------------------------ lock (never broken)
def _freemb():
    out = subprocess.run(["vm_stat"], capture_output=True, text=True).stdout
    ps = int(out.split("page size of")[1].split()[0]); f = i = 0
    for ln in out.splitlines():
        if ln.startswith("Pages free"): f = int(ln.split()[-1].rstrip("."))
        if ln.startswith("Pages inactive"): i = int(ln.split()[-1].rstrip("."))
    return (f + i) * ps // 1048576


HELD = {"label": None, "t": None, "released_at": None}


def lock_acquire(label):
    if a.no_lock:
        return
    last = HELD["released_at"]
    try:                                            # gap also spans this worker's other processes
        last = max(last or 0.0, float(open(LAST_REL).read().strip()))
    except (OSError, ValueError):
        pass
    if last:                                        # fairness gap after our own release
        w = a.gap - (time.time() - last)
        if w > 0:
            log("fairness gap: sleeping %.0fs before re-acquire" % w)
            time.sleep(w)
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
        fh.write("bt0926-repert %s %s pid %d\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                                                   label, os.getpid()))
    HELD["label"] = label
    HELD["t"] = time.time()
    log("LOCK ACQUIRED %s (waited %.0fs)" % (label, time.time() - tw))


def lock_release(label):
    if a.no_lock or HELD["label"] is None:
        return
    try:
        os.remove(os.path.join(LOCK, "owner"))
    except FileNotFoundError:
        pass
    os.rmdir(LOCK)
    HELD["label"] = None
    HELD["released_at"] = time.time()
    with open(LAST_REL, "w") as fh:
        fh.write("%.3f\n" % HELD["released_at"])
    assert not os.path.exists(LOCK), "lock still present after release"
    log("LOCK RELEASED %s (verified gone)" % label)


def maybe_rehold(label):
    if a.no_lock or HELD["label"] is None:
        return
    if time.time() - HELD["t"] > a.max_hold:
        lock_release(HELD["label"])
        lock_acquire(label)


def _release_at_exit(*_x):
    if HELD["label"] is not None:
        lock_release(HELD["label"])
    if _x:
        sys.exit(143)


import atexit, signal  # noqa: E402
atexit.register(_release_at_exit)
signal.signal(signal.SIGTERM, _release_at_exit)


# ------------------------------------------------------------------ helpers
class EnvProxy:
    """Delegates to the real env; pins health at 1.0 around every step (continuous life, as probe C)
    and records the action the env actually received."""

    def __init__(self, env):
        self.__dict__["_env"] = env
        self.__dict__["last_exec"] = None

    def __getattr__(self, k):
        return getattr(self._env, k)

    def __setattr__(self, k, v):
        if k in ("last_exec", "last_moved", "last_harm", "_env"):
            self.__dict__[k] = v
        else:
            setattr(self._env, k, v)

    def step(self, action):
        self.__dict__["last_exec"] = action.detach().clone().reshape(1, -1)
        pos0 = (int(self._env.agent_x), int(self._env.agent_y))
        self._env.agent_health = 1.0
        res = self._env.step(action)
        self._env.agent_health = 1.0
        self.__dict__["last_moved"] = (int(self._env.agent_x), int(self._env.agent_y)) != pos0
        self.__dict__["last_harm"] = float(res[1])
        return res


def make_life_env(k):
    return CausalGridWorldV2(size=BB.GRID, seed=S * BB.SEED_STRIDE + k, resource_respawn_on_consume=True,
                             pos_telemetry_enabled=True, traj_telemetry_enabled=True,
                             max_episode_steps=a.life + 100, **BB.PH0_KW)


def set_knobs(agent):
    for k in KNOBS:
        setattr(agent.config.latent, k, True)
        if hasattr(agent, "latent_stack") and hasattr(agent.latent_stack, "config"):
            setattr(agent.latent_stack.config, k, True)
    assert all(getattr(agent.latent_stack.config, k) for k in KNOBS)


def hbits(counts):
    c = np.asarray(counts, dtype=float)
    s = c.sum()
    if s <= 0:
        return float("nan")
    q = c[c > 0] / s
    return float(-(q * np.log2(q)).sum())


# ------------------------------------------------------------------ life runner
def run_life(snap, stage, prop, commit):
    name = "%s-%s-%s" % (stage, prop, commit)
    ag = copy.deepcopy(snap)
    tr = getattr(ag, "waking_trainer", None)
    if tr is not None:
        tr.every_k = 10 ** 9                     # frozen: no member updates in a test life
    hc = ag.hippocampal.config
    if PROPS[prop] is not None:
        hc.use_action_space_proposals = True
        hc.action_space_first_action_mode = PROPS[prop]
        HippocampalModule._validate_action_space_proposal_config(hc)   # raises on a conflict
    e3cfg = ag.e3.config
    base_thr = float(e3cfg.commitment_threshold)
    cap = []
    orig_select = ag.e3.select

    def wsel(*args, **kw):                        # record-only wrapper (instance attribute)
        res = orig_select(*args, **kw)
        cand = args[0] if args else kw.get("candidates")
        temp = args[1] if len(args) > 1 else kw.get("temperature", 1.0)
        cap.append((cand, float(temp), res, bool(kw.get("simulation_mode", False))))
        return res

    ag.e3.select = wsel
    R.seed_all(S + 900)
    env = EnvProxy(make_life_env(150))
    srng = np.random.default_rng(S + 6161)
    ticks_rec = []
    e3_rec = []

    def on_sense(agent, latent, step, **kw):
        cap.clear()
        e3cfg.commitment_threshold = -1.0 if commit == "OFF" else base_thr

    def on_action(agent, action, step, ticks, **kw):
        if not ticks.get("e3_tick", False):
            return
        live = [c for c in cap if c[0] is agent._committed_candidates and not c[3]]
        ident = bool(live)
        if not live:
            live = [c for c in cap if not c[3]]
        if not live:
            e3_rec.append({"t": step, "missing": True, "n_cap": len(cap)})
            return
        cand, temp, res, _sim = live[-1]
        first = torch.stack([c.actions[:, 0, :].detach().reshape(-1).float() for c in cand])  # [K, A]
        K = int(first.shape[0])
        cls = first.argmax(dim=1)
        cen = first - first.mean(dim=0, keepdim=True)
        cls_c = cen.argmax(dim=1)
        mean_cls = int(first.mean(dim=0).argmax().item())
        d = torch.cdist(first, first)
        pair = float(d.sum().item() / max(1, K * (K - 1)))
        sc = res.scores.detach().reshape(-1).double()
        assert sc.numel() == K, (sc.numel(), K)
        probs = torch.softmax(-sc / max(temp, 1e-12), dim=0)
        lpp = getattr(agent.e3, "last_precommit_probs", None)
        pchk = float((lpp.detach().reshape(-1).double() - probs).abs().max().item()) if lpp is not None and lpp.numel() == K else None
        cls_np = cls.numpy()
        mass = np.bincount(cls_np, weights=probs.numpy(), minlength=A_DIM)
        pn = probs.numpy()
        sh = np.zeros(A_DIM)
        for _ in range(a.n_shuf):
            sh += np.bincount(cls_np, weights=pn[srng.permutation(K)], minlength=A_DIM)
        sh /= a.n_shuf
        hp = float(-(pn[pn > 0] * np.log2(pn[pn > 0])).sum())
        srcs = {}
        for c in cand:
            s_ = (c.metadata or {}).get("source", "none") if isinstance(getattr(c, "metadata", None), dict) else "none"
            srcs[s_] = srcs.get(s_, 0) + 1
        pdg = getattr(agent.hippocampal, "_last_propose_diagnostics", {}) or {}
        it = pdg.get("cem_iteration_diagnostics") or []
        it0 = None
        if it and isinstance(it[0], dict):
            it0 = it[0].get("pre_refit_first_action_counts")
        sel_idx = int(res.selected_index)
        e3_rec.append({
            "t": step, "K": K, "ident": ident, "pchk": pchk, "n_cap": len(cap),
            "pool": np.bincount(cls_np, minlength=A_DIM).tolist(),
            "pool_c": np.bincount(cls_c.numpy(), minlength=A_DIM).tolist(),
            "mean_cls": mean_cls, "agree_mean": float((cls == mean_cls).float().mean().item()),
            "dim_mean": first.mean(dim=0).tolist(), "dim_std": first.std(dim=0).tolist(),
            "pair": pair, "norm_med": float(first.norm(dim=1).median().item()),
            "it0": {str(k): int(v) for k, v in it0.items()} if isinstance(it0, dict) else None,
            "sp_inj": int(pdg.get("support_preserving_injected_candidates", 0) or 0),
            "srcs": srcs,
            "T": temp, "sc_std": float(sc.std().item()), "sc_rng": float((sc.max() - sc.min()).item()),
            "hp": hp, "mass": mass.tolist(), "mass_shuf": sh.tolist(),
            "argmin_cls": int(cls_np[int(sc.argmin().item())]),
            "sel_idx": sel_idx, "sel_cls": int(cls_np[sel_idx]), "committed": bool(res.committed),
            "exec_cls": int(action.detach().reshape(-1).argmax().item()),
        })

    def on_post_step(agent, ticks, **kw):
        ticks_rec.append((int(env.last_exec.reshape(-1).argmax().item()), bool(ticks.get("e3_tick", False)),
                          bool(agent.beta_gate.is_elevated), bool(env.last_moved), float(env.last_harm)))

    hh = StepHarness(ag, env, train_mode=False, seed=S * 1000 + 777,
                     hooks=StepHooks(on_sense=on_sense, on_action=on_action, on_post_step=on_post_step))
    _f, od = env.reset(); ag.reset(); hh.reset()
    tl = time.time()
    resets = []
    for t in range(a.life):
        r = hh.step(od)
        od = r.next_obs_dict
        if r.done:
            resets.append(t)
            _f, od = env.reset(); ag.reset(); hh.reset()
    e3cfg.commitment_threshold = base_thr
    ex = np.bincount([x[0] for x in ticks_rec], minlength=A_DIM)
    good = [e for e in e3_rec if not e.get("missing")]
    pool_tot = np.sum([e["pool"] for e in good], axis=0) if good else np.zeros(A_DIM)
    out = {"name": name, "secs": time.time() - tl, "resets": resets, "ticks": ticks_rec, "e3": e3_rec,
           "base_thr": base_thr, "asp": PROPS[prop]}
    log("LIFE %-14s %4.0fs e3 %d (miss %d) pool %s exec %s H_pool %.2f H_exec %.2f beta %.2f" % (
        name, out["secs"], len(e3_rec), len(e3_rec) - len(good), pool_tot.astype(int).tolist(), ex.tolist(),
        hbits(pool_tot), hbits(ex), float(np.mean([x[2] for x in ticks_rec]))))
    return out


# ------------------------------------------------------------------ main
out = {"seed": S, "args": vars(a), "wt": a.wt, "stages": {}}


def dump():
    json.dump(out, open(a.out, "w"), default=lambda o: None if isinstance(o, float) and not math.isfinite(o) else str(o))


copy._deepcopy_dispatch[types.ModuleType] = lambda x, memo: x
lock_acquire("seed%d-A" % S)                    # BEFORE any heavy compute
R.seed_all(S)
_e, ref, _c = R.build_B(S, False)
set_knobs(ref)
ref.eval()
ref_enc = copy.deepcopy(ref.latent_stack.state_dict())
te_segs, _ = BB.gen_policy(S, 1 if a.smoke else 3000 // BB.EP_STEPS, 120, BB.pol_uniform(S * 7 + 3))
TE = BB.encode_segs(ref, te_segs)

agent = BB.fresh_agent(S, ref_enc)
set_knobs(agent)
hcfg = agent.hippocampal.config
out["config"] = {k: getattr(hcfg, k, None) for k in (
    "num_candidates", "num_cem_iterations", "elite_fraction", "horizon", "use_support_preserving_cem",
    "support_preserving_min_first_action_classes", "use_action_space_proposals", "action_space_first_action_mode",
    "use_differentiable_cem", "use_orthogonal_cem_seeding", "mode_conditioning_enabled",
    "use_mech293_ghost_probes", "use_cem_modulatory_authority", "use_chunk_proposal_injection",
    "use_action_class_scaffold_candidates")}
out["config"]["commitment_threshold"] = float(agent.e3.config.commitment_threshold)
out["config"]["use_pag_freeze_gate"] = bool(getattr(agent.config, "use_pag_freeze_gate", False))
log("config %s" % out["config"])
SNAP_U = copy.deepcopy(agent)
out["stages"]["U"] = {"disc4": BB.evaluate(ref, BP.get_head(agent), TE, "z", S), "lives": {}}
dump()
for prop in PROPS:
    for commit in COMMITS:
        maybe_rehold("seed%d-U-%s-%s" % (S, prop, commit))
        out["stages"]["U"]["lives"]["%s-%s" % (prop, commit)] = run_life(SNAP_U, "U", prop, commit)
        dump()
del SNAP_U

# W3 member protocol exactly as probe C / N5 phase 1 (native codec proposer during the dose)
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
        maybe_rehold("seed%d-babble-%d" % (S, k))
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
tr.set_e2_world_source("on_policy")
tr.every_k = 1
member.updates_per_step = a.ups
agent.reset()
R.seed_all(S + 500)
s1 = 200 if a.smoke else a.s1
for ep in range(max(1, s1 // BB.EP_STEPS)):
    maybe_rehold("seed%d-dose-%d" % (S, ep))
    env = BB.make_env(S, 50 + ep)
    hh = StepHarness(agent, env, train_mode=False, seed=S * 1000 + 50 + ep)
    _f, od = env.reset(); agent.reset(); hh.reset()
    for _s in range(min(BB.EP_STEPS, s1)):
        r = hh.step(od)
        od = r.next_obs_dict
        if r.done:
            _f, od = env.reset(); agent.reset(); hh.reset()
ev_s1 = BB.evaluate(ref, BP.get_head(agent), TE, "z", S)
agent.reset()
SNAP_T = copy.deepcopy(agent)
out["stages"]["T"] = {"disc4": ev_s1, "screen_pass": bool(ev_s1["disc4_h1"] >= 0.47), "lives": {}}
log("T disc4 %.4f k %d (bar 0.47 %s)" % (ev_s1["disc4_h1"], ev_s1["k"], ev_s1["disc4_h1"] >= 0.47))
dump()
for prop in PROPS:
    for commit in COMMITS:
        maybe_rehold("seed%d-T-%s-%s" % (S, prop, commit))
        out["stages"]["T"]["lives"]["%s-%s" % (prop, commit)] = run_life(SNAP_T, "T", prop, commit)
        dump()
lock_release(HELD["label"] or "seed%d" % S)
out["t_total_s"] = time.time() - t0
dump()
log("DONE %.0fs" % out["t_total_s"])
