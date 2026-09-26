"""Probe N5 (bt0926-n5): does ACh-gated unfreeze revise W3's retained memory only when it should?

2x2 on the W3 E2WorldMember (ree-v3 1b013d6, no ree_core edits):
  {env action-map re-permutation (SD-MEL-PRODUCER effective-map shift) vs none}
  x {g gated by surprise vs g clamped low}
plus one report-only cell on the shift side: `lronly` (g = 1 fixed, unfreeze disabled) --
attributes a re-learn to plasticity gain alone vs to retained-memory revision.

Phases (one process = one seed, all cells):
  0. reference build, held-out test sets TE_orig (the W3/babble-probe test set) and TE_shift
     (same generator, same env seeds, the shifted action map), B0 (N2's recompute recipe).
  1. SHARED developmental phase = the W3 member-gate protocol verbatim (g = 1): W2a babbling
     2400 steps -> FROZEN retained set, 3000 member updates (pre), 1200 native closed-loop
     StepHarness steps x 8 updates at the 25% retained mix. Readout "pre-shift bar" on TE_orig.
  2. snapshot (deepcopy of the agent incl. trainer + member); every cell starts from it.
  3. ADULT phase, N waking steps (8 member updates per step), per cell:
       shift cells: every env built in this phase has its effective action map permuted
       (env._action_map[c] = ACTIONS[SHIFT_P[c]] for the 4 move classes; stay unchanged).
       g rule (harness-side; no ACh / MECH-398 / MECH-207 signal exists in ree_core @ 1b013d6):
         e_t  = log MSE of the member head's one-step prediction on each newly recorded
                transition, computed BEFORE that step's updates (from the record's live z pair)
         z_t  = (e_t - mu_src) / sd_src, per-source baseline (on_policy / babble), initialised
                at the start of the adult phase from the snapshot head's errors on the last 400
                on-policy records / 400 retained records; EMA-updated (alpha_b) only while FROZEN
         s_t  = EMA(z_t, alpha_s)                             (fast surprise)
         a_t  = EMA(1[s_t > Z_THR], alpha_g)                  (slow arousal integrator)
         g_t  = G_LOW + (1 - G_LOW) * a_t   (gated) | G_LOW (clamped) | 1.0 (lronly)
         member lr = BASE_LR * g_t
         UNFREEZE (MECH-207 coincidence) iff s_t > Z_THR AND g_t > G_THR (never in clamped:
         G_LOW < G_THR; disabled in lronly). On unfreeze: the running native episode ends;
         on-policy records recorded before the current surprise onset are dropped (stale
         working memory); a W2a babbling bout of BOUT steps runs, each babble record REPLACING
         the oldest retained entry (FIFO; set size constant). After the bout, another bout if
         the coincidence still holds, else re-FREEZE and resume the native policy.
       Bout steps count toward N (matched env-step and update budget across cells).
  4. readouts: disc4_h1/k on TE_shift (the post-shift bar) and TE_orig; retention (b) vs B0;
     unfreeze/bout counts, replaced/flushed counts, g/s trace, retained-set error, guard, (e).
ASCII output only.
"""
from __future__ import annotations

import argparse, copy, json, sys, time, types
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F

p = argparse.ArgumentParser()
p.add_argument("--seed", type=int, required=True)
p.add_argument("--wt", required=True)
p.add_argument("--out", required=True)
p.add_argument("--cells", default="shift_gated,shift_clamped,noshift_gated,noshift_clamped,shift_oracle")
p.add_argument("--n-adult", type=int, default=1200)
p.add_argument("--post", type=int, default=1200)
p.add_argument("--ups", type=int, default=8)
p.add_argument("--bout", type=int, default=200)
p.add_argument("--gate-signal", choices=["ac", "pe"], default="ac")
p.add_argument("--z-thr-pe", type=float, default=2.0)
p.add_argument("--z-thr-ac", type=float, default=0.75)
p.add_argument("--g-thr", type=float, default=0.5)
p.add_argument("--g-low", type=float, default=0.1)
p.add_argument("--alpha-s-pe", type=float, default=0.2)
p.add_argument("--alpha-s-ac", type=float, default=0.05)
p.add_argument("--alpha-g", type=float, default=0.05)
p.add_argument("--alpha-b", type=float, default=0.005)
p.add_argument("--ckpt-every", type=int, default=0)
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
from ree_core.environment.causal_grid_world import CausalGridWorld  # noqa: E402

S = a.seed
t0 = time.time()
BASE_LR = 3e-4
SHIFT_P = [2, 3, 1, 0]          # move class c now displaces like canonical class SHIFT_P[c]
ON = WT.SOURCE_ON_POLICY if hasattr(WT, "SOURCE_ON_POLICY") else "on_policy"


def log(m):
    print("[n5 s%d t=%5.0fs] %s" % (S, time.time() - t0, m), flush=True)


assert str(Path(WT.__file__).resolve()).startswith(str(Path(a.wt).resolve())), WT.__file__
BASE_ACTIONS = dict(CausalGridWorld.ACTIONS)
SHIFTED = dict(BASE_ACTIONS)
for c in range(4):
    SHIFTED[c] = BASE_ACTIONS[SHIFT_P[c]]
assert all(SHIFTED[c] != BASE_ACTIONS[c] for c in range(4)) and SHIFTED[4] == BASE_ACTIONS[4]
_make_env_orig = BB.make_env


def make_env_shift(seed, k):
    env = _make_env_orig(seed, k)
    env._action_map = dict(SHIFTED)
    return env


def check_shift_live(mk, seed, k, n=400):
    """Empirical displacement tally: which (dx,dy) each class actually produced."""
    env = mk(seed, k)
    env.reset()
    g = np.random.default_rng(seed + 991)
    tally = {c: {} for c in range(5)}
    for _ in range(n):
        c = int(g.integers(0, 5))
        x0, y0 = int(env.agent_x), int(env.agent_y)
        _o, _h, done, _i, _od = env.step(c)
        d = (int(env.agent_x) - x0, int(env.agent_y) - y0)
        if d != (0, 0) or c == 4:
            tally[c][str(d)] = tally[c].get(str(d), 0) + 1
        if done:
            env.reset()
    modal = {c: (max(v, key=v.get) if v else None) for c, v in tally.items()}
    return modal, tally


# ------------------------------------------------------------------ phase 0: reference, test sets, B0
R.seed_all(S)
_e, ref, _c = R.build_B(S, False)
ref.eval()
ref_enc = copy.deepcopy(ref.latent_stack.state_dict())
init = BP.get_head(ref)
te_segs, _ = BB.gen_policy(S, 3000 // BB.EP_STEPS, 120, BB.pol_uniform(S * 7 + 3))
TE = BB.encode_segs(ref, te_segs)
BB.make_env = make_env_shift
try:
    te_segs_s, _ = BB.gen_policy(S, 3000 // BB.EP_STEPS, 120, BB.pol_uniform(S * 7 + 3))
finally:
    BB.make_env = _make_env_orig
TE_S = BB.encode_segs(ref, te_segs_s)
modal_orig, _ = check_shift_live(_make_env_orig, S, 999)
modal_shift, tally_shift = check_shift_live(make_env_shift, S, 999)
log("displacement modal orig %s | shift %s" % (modal_orig, modal_shift))
ev_init = BB.evaluate(ref, init, TE, "z", S)
ev_init_s = BB.evaluate(ref, init, TE_S, "z", S)

pol_agent = BB.fresh_agent(S, ref_enc)
R.seed_all(S + 300)
pol_segs, pol_info = BB.gen_POL(pol_agent, S, 12, 25)
trapped = bool(pol_info["early_per_1000"] >= 3.0 or pol_info["harm_events_per_100"] >= 10.0)
E_POL = BB.encode_segs(ref, pol_segs)
hd_b0, _tinfo = BB.train_head(ref, init, BB.to_trans(E_POL, "z"), BB.PRE_UPD, S)
ev_b0 = BB.evaluate(ref, hd_b0, TE, "z", S)
B0 = ev_b0["disc4_h1"]
del pol_agent, pol_segs, E_POL
log("INIT disc4 orig %.4f shift %.4f | B0 %.4f k %d (%s)" % (
    ev_init["disc4_h1"], ev_init_s["disc4_h1"], B0, ev_b0["k"], "trapped" if trapped else "benign"))

# ------------------------------------------------------------------ phase 1: shared W3 protocol (g = 1)
agent = BB.fresh_agent(S, ref_enc)
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
    for k in range(12):
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
for _u in range(3000):
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
head_ps = BP.get_head(agent)
ev_ps = BB.evaluate(ref, head_ps, TE, "z", S)
ev_ps_s = BB.evaluate(ref, head_ps, TE_S, "z", S)
pre_bar = bool(ev_ps["disc4_h1"] >= 0.47 and ev_ps["k"] == 10)
ret_ps = (ev_ps["disc4_h1"] - B0) / (ev_pre["disc4_h1"] - B0) if ev_pre["disc4_h1"] != B0 else None
log("retained %d | pre disc4 %.4f k %d | PRE-SHIFT (end W3 protocol) orig %.4f k %d bar %s ret %s | on shifted map %.4f k %d" % (
    retained_n0, ev_pre["disc4_h1"], ev_pre["k"], ev_ps["disc4_h1"], ev_ps["k"], pre_bar,
    None if ret_ps is None else round(ret_ps, 3), ev_ps_s["disc4_h1"], ev_ps_s["k"]))
agent.reset()
copy._deepcopy_dispatch[types.ModuleType] = lambda x, memo: x   # modules are shared, not copied
SNAP = copy.deepcopy(agent)
log("snapshot ok (on-policy %d, retained %d)" % (len(member._on_policy), len(member._retained)))


def rollout_e(head):
    BP.set_head(ref, head)
    g = np.random.default_rng(S + 31)
    t30, late = [], []
    with torch.no_grad():
        for _i in range(40):
            ep = TE[int(g.integers(0, len(TE)))]
            t = int(g.integers(0, ep["z"].shape[0]))
            x0 = ep["z"][t:t + 1]
            acts = F.one_hot(torch.tensor(g.integers(0, 5, 30)), 5).float().unsqueeze(0)
            ws = ref.e2.rollout_with_world(torch.zeros(1, 32), x0, acts, compute_action_objects=False).world_states
            n = [float(w.norm()) for w in ws]
            t30.append(n[30] / max(n[0], 1e-9))
            late.append(float(np.mean([n[j] / max(n[j - 1], 1e-9) for j in range(21, 31)])))
    return {"t30_over_t0_median": float(np.median(t30)), "late_growth_max": float(np.max(late)),
            "gate_e": bool(float(np.max(late)) < 1.2 and float(np.median(t30)) < 5.0)}


# ------------------------------------------------------------------ phase 3: adult phase, one cell
def run_cell(cell):
    shift = cell.startswith("shift_")
    mode = cell.split("_", 1)[1]
    mk = make_env_shift if shift else _make_env_orig
    ag = copy.deepcopy(SNAP)
    trc = ag.waking_trainer
    mem = trc.members["e2_world"]
    opt = trc.optimizers["e2_world"]
    assert mem._agent is ag and trc._agent is ag
    R.seed_all(S + 700)

    @torch.no_grad()
    def rec_stats(rec):
        """(pe, ac): pe = log one-step MSE under the executed action; ac = pe minus the log MSE
        of the BEST alternative action class (>0: another action explains the transition better)."""
        z0, z1 = rec["z_live"]
        aex = int(rec["a"].reshape(-1).argmax())
        acts = torch.eye(5, dtype=z0.dtype)
        pred = ag.e2.world_forward(z0.expand(5, -1), acts)
        le = torch.log(((pred - z1) ** 2).mean(dim=-1) + 1e-12)
        pe = float(le[aex])
        alt = torch.cat([le[:aex], le[aex + 1:]])
        return pe, pe - float(alt.min())

    def rec_err(rec):
        return rec_stats(rec)[0]

    # per-source baselines from the snapshot head, for both detectors
    st_on = [rec_stats(r) for r in list(mem._on_policy)[-400:]]
    gg = np.random.default_rng(S + 4242)
    idx = gg.choice(len(mem._retained), min(400, len(mem._retained)), replace=False)
    st_bb = [rec_stats(mem._retained[int(i)]) for i in idx]
    base = {}
    for j, det in ((0, "pe"), (1, "ac")):
        von = [x[j] for x in st_on]; vbb = [x[j] for x in st_bb]
        base[det] = {"on": [float(np.mean(von)), float(np.var(von))], "bab": [float(np.mean(vbb)), float(np.var(vbb))]}
    base0 = copy.deepcopy(base)
    ret_probe_idx = gg.choice(len(mem._retained), 256, replace=False)
    DET = {"pe": {"alpha": a.alpha_s_pe, "thr": a.z_thr_pe}, "ac": {"alpha": a.alpha_s_ac, "thr": a.z_thr_ac}}
    GATE = a.gate_signal
    st = {"s": {"pe": 0.0, "ac": 0.0}, "a": {"pe": 0.0, "ac": 0.0},
          "g": {"gated": a.g_low, "clamped": a.g_low, "lronly": 1.0, "oracle": 1.0, "oraclefull": 1.0}[mode],
          "unfrozen": False, "onset": None, "coinc": mode in ("oracle", "oraclefull"), "n_rec": 0}
    tr_log = {"s_ac": [], "s_pe": [], "g": [], "z_ac": [], "z_pe": [], "src": []}
    cnt = {"replaced": 0, "flushed": 0, "bouts": 0, "bout_steps": 0, "unfreeze_events": 0,
           "coinc_steps": 0, "first_unfreeze_step": None, "first_coinc_step": None,
           "would_coinc_steps": {"pe": 0, "ac": 0}, "first_would_coinc": {"pe": None, "ac": None}}
    steps = {"n": 0}

    def store(rec):
        src = "on" if rec["source"] == ON else "bab"
        vals = dict(zip(("pe", "ac"), rec_stats(rec)))
        zs = {}
        for det, v in vals.items():
            mu, var = base[det][src]
            z = (v - mu) / max(np.sqrt(var), 1e-6)
            zs[det] = z
            prev_s = st["s"][det]
            st["s"][det] += DET[det]["alpha"] * (z - st["s"][det])
            st["a"][det] += a.alpha_g * (float(st["s"][det] > DET[det]["thr"]) - st["a"][det])
            if not st["unfrozen"]:
                mu2 = mu + a.alpha_b * (v - mu)
                base[det][src] = [mu2, var + a.alpha_b * ((v - mu) * (v - mu2) - var)]
            # report-only: would this detector's own coincidence (s > thr AND its g > G_THR) fire?
            g_would = a.g_low + (1.0 - a.g_low) * st["a"][det]
            if st["s"][det] > DET[det]["thr"] and g_would > a.g_thr:
                cnt["would_coinc_steps"][det] += 1
                if cnt["first_would_coinc"][det] is None:
                    cnt["first_would_coinc"][det] = steps["n"]
            if det == GATE and st["s"][det] > DET[det]["thr"] and prev_s <= DET[det]["thr"]:
                st["onset"] = rec["step"]
        if mode == "gated":
            st["g"] = a.g_low + (1.0 - a.g_low) * st["a"][GATE]
        if mode in ("oracle", "oraclefull"):
            st["coinc"] = True
        else:
            st["coinc"] = bool(mode != "lronly" and st["s"][GATE] > DET[GATE]["thr"] and st["g"] > a.g_thr)
        cnt["coinc_steps"] += int(st["coinc"])
        if st["coinc"] and cnt["first_coinc_step"] is None:
            cnt["first_coinc_step"] = steps["n"]
        st["n_rec"] += 1
        if st["n_rec"] % 5 == 0:
            tr_log["s_ac"].append(round(st["s"]["ac"], 3)); tr_log["s_pe"].append(round(st["s"]["pe"], 3))
            tr_log["g"].append(round(st["g"], 3)); tr_log["z_ac"].append(round(zs["ac"], 3))
            tr_log["z_pe"].append(round(zs["pe"], 3)); tr_log["src"].append(src)
        if src == "on":
            mem._on_policy.append(rec)
        elif st["unfrozen"] and not (mode == "oraclefull"):
            mem._retained.pop(0)
            mem._retained.append(rec)
            cnt["replaced"] += 1
        else:
            mem._retain(rec)

    mem._store = store
    bab_c = StructuredBabbler(n_classes=5, max_run=4, seed=S * 17 + 5)
    ckpts = []
    if mode in ("oracle", "oraclefull"):
        pending_init = True
    else:
        pending_init = False
    k_env = [60]
    pending = pending_init

    def set_lr():
        for pg in opt.param_groups:
            pg["lr"] = BASE_LR * st["g"]

    def ckpt():
        if a.ckpt_every and steps["n"] % a.ckpt_every == 0 and steps["n"] > 0:
            hd = BP.get_head(ag)
            e_s = BB.evaluate(ref, hd, TE_S, "z", S) if shift else None
            e_o = BB.evaluate(ref, hd, TE, "z", S)
            ckpts.append({"step": steps["n"], "orig_disc4": e_o["disc4_h1"], "orig_k": e_o["k"],
                          "shift_disc4": None if e_s is None else e_s["disc4_h1"],
                          "shift_k": None if e_s is None else e_s["k"], "g": st["g"], "s": st["s"],
                          "bouts": cnt["bouts"], "replaced": cnt["replaced"]})

    while steps["n"] < a.n_adult:
        k_env[0] += 1
        env = mk(S, k_env[0])
        if pending:
            if not st["unfrozen"]:
                cnt["unfreeze_events"] += 1
                if cnt["first_unfreeze_step"] is None:
                    cnt["first_unfreeze_step"] = steps["n"]
            st["unfrozen"] = True
            cnt["bouts"] += 1
            onset = st["onset"]
            if mode in ("oracle", "oraclefull") and cnt["bouts"] == 1:
                onset = 10 ** 12          # oracle: every pre-shift on-policy record is stale
            if mode == "oraclefull" and cnt["bouts"] == 1:
                cnt["quarantined"] = len(mem._retained)
                mem._retained.clear()      # oraclefull: the whole pre-shift retained set is quarantined
            if onset is not None:
                keep = [r for r in mem._on_policy if r["step"] >= onset]
                cnt["flushed"] += len(mem._on_policy) - len(keep)
                mem._on_policy.clear(); mem._on_policy.extend(keep)
            trc.set_e2_world_source("babble")
            _f, od = env.reset(); ag.reset(); bab_c.reset()
            for _s in range(a.bout):
                if steps["n"] >= a.n_adult:
                    break
                set_lr()
                with torch.no_grad():
                    ag.sense(od["body_state"], od["world_state"], obs_harm=od.get("harm_obs"),
                             obs_harm_a=od.get("harm_obs_a"), obs_harm_history=od.get("harm_history"))
                    act = bab_c.next_action()
                    ag.record_executed_action(act)
                    _f, h, done, _i, od = env.step(int(act.argmax()))
                trc.on_waking_step(float(h))
                steps["n"] += 1; cnt["bout_steps"] += 1
                ckpt()
                if done:
                    _f, od = env.reset(); ag.reset(); bab_c.reset()
            trc.set_e2_world_source("on_policy")
            ag.reset()
            pending = st["coinc"]
            if not pending:
                st["unfrozen"] = False
            continue
        hh = StepHarness(ag, env, train_mode=False, seed=S * 1000 + k_env[0])
        _f, od = env.reset(); ag.reset(); hh.reset()
        for _s in range(BB.EP_STEPS):
            if steps["n"] >= a.n_adult:
                break
            set_lr()
            r = hh.step(od)
            steps["n"] += 1
            ckpt()
            od = r.next_obs_dict
            if st["coinc"]:
                pending = True
                break
            if r.done:
                _f, od = env.reset(); ag.reset(); hh.reset()
        ag.reset()

    hd = BP.get_head(ag)
    ev_o = BB.evaluate(ref, hd, TE, "z", S)
    ev_s = BB.evaluate(ref, hd, TE_S, "z", S)
    with torch.no_grad():
        ret_err = float(np.mean([np.exp(rec_err(mem._retained[int(i)])) for i in ret_probe_idx if int(i) < len(mem._retained)]))
    n_orig_left = sum(1 for r in mem._retained if r["source"] != ON and r["step"] <= SNAP.waking_trainer.members["e2_world"].n_observed)
    res = {
        "cell": cell, "shift": shift, "mode": mode, "n_adult": steps["n"],
        "orig": ev_o, "shift_map": ev_s,
        "bar_shift": bool(ev_s["disc4_h1"] >= 0.47 and ev_s["k"] == 10),
        "bar_orig": bool(ev_o["disc4_h1"] >= 0.47 and ev_o["k"] == 10),
        "retention_orig": (ev_o["disc4_h1"] - B0) / (ev_pre["disc4_h1"] - B0) if ev_pre["disc4_h1"] != B0 else None,
        "counts": cnt, "retained_n": len(mem._retained), "retained_original_left": n_orig_left,
        "retained_err_mse_mean": ret_err, "baseline_start": base0, "baseline_end": base,
        "g_end": st["g"], "g_mean": float(np.mean(tr_log["g"])) if tr_log["g"] else None,
        "frac_g_gt_thr": float(np.mean([x > a.g_thr for x in tr_log["g"]])) if tr_log["g"] else None,
        "s_max": float(np.max(tr_log["s_" + GATE])) if tr_log["g"] else None,
        "z_ac_on_mean": float(np.mean([z for z, sr in zip(tr_log["z_ac"], tr_log["src"]) if sr == "on"] or [np.nan])),
        "z_pe_on_mean": float(np.mean([z for z, sr in zip(tr_log["z_pe"], tr_log["src"]) if sr == "on"] or [np.nan])),
        "p_s_ac_gt_thr": float(np.mean([x > a.z_thr_ac for x in tr_log["s_ac"]])) if tr_log["g"] else None,
        "p_s_pe_gt_thr": float(np.mean([x > a.z_thr_pe for x in tr_log["s_pe"]])) if tr_log["g"] else None,
        "ckpts": ckpts, "guard": {k: v.status for k, v in trc.guard_results.items()},
        "rollout": rollout_e(hd), "updates": dict(trc.steps),
        "trace_every5": tr_log,
    }
    log("CELL %-16s shift-map %.4f k %2d bar %s | orig %.4f k %2d bar %s ret %s | bouts %d (steps %d) events %d first %s replaced %d flushed %d orig_left %d | g_mean %s s_max %s coinc %d first %s | would pe %d ac %d | zon ac %.2f pe %.2f | ret_err %.4g" % (
        cell, ev_s["disc4_h1"], ev_s["k"], res["bar_shift"], ev_o["disc4_h1"], ev_o["k"], res["bar_orig"],
        None if res["retention_orig"] is None else round(res["retention_orig"], 3), cnt["bouts"], cnt["bout_steps"],
        cnt["unfreeze_events"], cnt["first_unfreeze_step"], cnt["replaced"], cnt["flushed"], n_orig_left,
        None if res["g_mean"] is None else round(res["g_mean"], 3),
        None if res["s_max"] is None else round(res["s_max"], 2), cnt["coinc_steps"], cnt["first_coinc_step"],
        cnt["would_coinc_steps"]["pe"], cnt["would_coinc_steps"]["ac"], res["z_ac_on_mean"], res["z_pe_on_mean"], ret_err))
    return res


out = {"seed": S, "args": vars(a), "code_sha_wt": a.wt, "hazard_class": "hazard-trapped" if trapped else "benign",
       "displacement_modal_orig": modal_orig, "displacement_modal_shift": modal_shift,
       "init_orig": ev_init, "init_shift": ev_init_s, "B0": ev_b0, "pre": ev_pre,
       "pre_shift_orig": ev_ps, "pre_shift_on_shifted_map": ev_ps_s, "pre_shift_bar": pre_bar,
       "pre_shift_retention": ret_ps, "retained_n0": retained_n0, "cells": {}}
for cell in [c for c in a.cells.split(",") if c]:
    out["cells"][cell] = run_cell(cell)
    json.dump(out, open(a.out, "w"), indent=1, default=str)
out["t_total_s"] = time.time() - t0
json.dump(out, open(a.out, "w"), indent=1, default=str)
log("DONE %.0fs" % out["t_total_s"])
