"""Probe N3 PROPER (bt0925-n3, orchestrate-20260924-breakthrough-c2, chip-20260925-coupled-n3-proper).

Which E3 horizon aggregation makes E3's ranking track true consequence, with the REAL W3
member head (ree_core E2WorldMember on integration/coupled-loop-repair @ 042895a), trained
natively by the W3 member-gate protocol (probes/w3/w3_l2r_member_probe.py), NOT a proxy.

Pre-registration: REE_assembly/evidence/planning/n3_e3_aggregation_probe_20260925.md
(committed BEFORE any registered seed ran). One invocation = one seed.

Design = N3-pre (probes/n3pre/n3pre_probe.py, d4bb6449b3) with the proxy head REPLACED:
  heads  REAL   = W3 member, W2a babbling (5 classes incl. stay) -> FROZEN retained set,
                  3000 member updates, 1200 native closed-loop steps x 8 member updates
                  (25% retained replay, re-encoded), MSE objective (the W3 defaults).
         SHUF   = identical; retained babbling actions relabelled by the FIXED class
                  permutation [1,2,3,4,0] (plan decision log 14:19Z item 3; W3 gate (c) twin).
         BLIND  = identical recipe with the action input ZEROED (e2.world_forward called with
                  a zero action everywhere during the member run); scored exactly action-blind
                  (world_action_encoder.weight := 0, so W a + b == b for every action).
         BLINDR = the same trained BLIND head scored with its action encoder weight left as
                  trained (== init: a zero input gives it no gradient) -- the pre-registered
                  fallback reference for gate (c) if BLIND is degenerate (all-tied).
         INIT   = untrained head (descriptive; N3-pre's old (c) reference).
  aggregations over E3's own depth-limited scores J_L (SD-081 knob), L = 2..31:
         D1 = J_2 (habit read; reference only), DISC_g = J_2 + sum g^(d-1)(J_{d+1}-J_d),
         g in {0.5, 0.8}, FIDW (per-depth fidelity-vs-persistence weights on TEW), FULL = J_31.
  gates  (a) Spearman(J_pred, J_true) on the scaffold pool, REAL - SHUF > 0.15
         (c) native-pool pick-flip vs the action-blind reference, REAL - SHUF > 0.15
         (b) pick in env-Q-best (scaffold), REAL - SHUF > 0.10 -- REPORTED ONLY
Instruments: ree-v3 experiments/_lib/coupled_acceptance.py (I1) for probe states, env-Q,
cloned-env validation, Spearman / pick-in-best, and its pinned canaries.
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

WT = Path("/Users/dgolden/REE_Working/.scratch/wt-w4")
PROBES = Path("/Users/dgolden/REE_Working/REE_assembly/evidence/planning/probes")
sys.path.insert(0, str(PROBES / "babble"))
sys.path.insert(0, str(PROBES / "rollout"))
sys.path.insert(0, str(WT / "experiments"))
sys.path.insert(0, str(WT))

import torch  # noqa: E402
import torch.nn.functional as F  # noqa: E402

torch.set_num_threads(2)

import babble_probe as BB  # noqa: E402
import rollout_fidelity_probe as R  # noqa: E402
import balanced_replay_probe as BP  # noqa: E402
from experiments._harness import StepHarness  # noqa: E402
from experiments._lib import coupled_acceptance as CA  # noqa: E402
from ree_core.predictors.e2_fast import Trajectory  # noqa: E402
from ree_core.utils import waking_trainer as WTR  # noqa: E402
from ree_core.developmental.structured_babbling import StructuredBabbler  # noqa: E402

A_ENV = 5
EP_STEPS = BB.EP_STEPS
HMAX = 30
GAMMAS = (0.5, 0.8)
AGGS = ["D1", "DISC_0.5", "DISC_0.8", "FIDW", "FULL"]
PERM = [1, 2, 3, 4, 0]
TIE_REL = 1e-6
CODE_SHA = "042895a3a2be3a54e5a74199e8e3950cc058cb31"

assert str(Path(WTR.__file__).resolve()).startswith(str(WT.resolve())), WTR.__file__
assert str(Path(CA.__file__).resolve()).startswith(str(WT.resolve())), CA.__file__
assert hasattr(WTR, "E2WorldMember")


# ------------------------------------------------------------------ member training (W3 protocol)
def train_member(S, ref, ref_enc, arm, post, ups, log):
    """W3 member-gate protocol verbatim (w3_l2r_member_probe.py), arm in {real, shuf, blind}."""
    agent = BB.fresh_agent(S, ref_enc)
    cfg = agent.config
    cfg.waking_trainer_guard_min_steps = 8
    if arm == "blind":
        # the zeroed action input leaves world_action_encoder.weight DEAD by construction, and the
        # guard RAISES on a dead tensor (waking_trainer.py:821); 0 disarms it (config.py:8110).
        cfg.waking_trainer_guard_min_steps = 0
        _orig = agent.e2.world_forward
        agent.e2.world_forward = lambda z, a, _o=_orig: _o(z, torch.zeros_like(a))
    member = WTR.E2WorldMember(agent, lr=3e-4, batch_size=32, buffer_max=2000, retained_max=5000,
                               replay_frac=0.25, reencode_window=0, replay_latent="reencode",
                               objective="mse", grad_clip=1.0, updates_per_step=1)
    tr = WTR.WakingTrainer(agent, cfg, members=[member])
    agent.waking_trainer = tr
    bab = StructuredBabbler(n_classes=5, max_run=4, seed=S * 13 + 1)
    tr.set_e2_world_source("babble")
    tr.every_k = 10 ** 9
    counts = [0] * 5
    with torch.no_grad():
        for k in range(12):
            env = BB.make_env(S, k)
            _f, od = env.reset(); agent.reset(); bab.reset()
            for _s in range(EP_STEPS):
                agent.sense(od["body_state"], od["world_state"], obs_harm=od.get("harm_obs"),
                            obs_harm_a=od.get("harm_obs_a"), obs_harm_history=od.get("harm_history"))
                act = bab.next_action()
                c = int(act.argmax()); counts[c] += 1
                agent.record_executed_action(act)
                _f, h, done, _i, od = env.step(c)
                tr.on_waking_step(float(h))
                if done:
                    _f, od = env.reset(); agent.reset(); bab.reset()
    retained_n = len(member._retained)
    if arm == "shuf":
        for r in member._retained:
            r["a"] = F.one_hot(torch.tensor([PERM[int(r["a"].argmax())]]), 5).float()
    for _u in range(3000):
        tr._update("e2_world", member)
    head_pre = BP.get_head(agent)
    tr.set_e2_world_source("on_policy")
    tr.every_k = 1
    member.updates_per_step = ups
    agent.reset()
    R.seed_all(S + 500)
    rew, acts_all, early = [], [], 0
    for ep in range(post // EP_STEPS):
        env = BB.make_env(S, 50 + ep)
        hh = StepHarness(agent, env, train_mode=False, seed=S * 1000 + 50 + ep)
        _f, od = env.reset(); agent.reset(); hh.reset()
        for _s in range(EP_STEPS):
            r = hh.step(od)
            rew.append(float(r.harm_signal)); acts_all.append(int(r.action.detach().reshape(-1).argmax()))
            od = r.next_obs_dict
            if r.done:
                early += 1
                _f, od = env.reset(); agent.reset(); hh.reset()
    head = BP.get_head(agent)
    rw = np.asarray(rew)
    info = {"retained_n": retained_n, "babble_class_counts": counts,
            "guard": {k: v.status for k, v in tr.guard_results.items()},
            "updates": dict(tr.steps), "drawn_retained": member.n_drawn_retained,
            "drawn_on_policy": member.n_drawn_on_policy,
            "post_reward_per_100": float(rw.sum() * 100.0 / len(rw)),
            "post_harm_events_per_100": float((rw < 0).sum() * 100.0 / len(rw)),
            "post_early_terminations": early,
            "post_action_counts": {str(c): acts_all.count(c) for c in range(5)}}
    log("MEMBER %s retained %d guard %s post_actions %s r/100 %.2f" % (
        arm, retained_n, info["guard"], info["post_action_counts"], info["post_reward_per_100"]))
    return head_pre, head, info


def blind_exact(head):
    h = copy.deepcopy(head)
    h["a"]["weight"] = torch.zeros_like(h["a"]["weight"])
    return h


# ------------------------------------------------------------------ TEW evaluation (N3-pre verbatim)
@torch.no_grad()
def eval_tew(ref, head, te, seed, H=HMAX, max_starts=300):
    BP.set_head(ref, head)
    e2 = ref.e2
    g = np.random.default_rng(seed + 91)
    starts = [(i, t) for i, e in enumerate(te) for t in range(e["a"].shape[0] - H + 1)]
    if len(starts) > max_starts:
        starts = [starts[j] for j in sorted(g.choice(len(starts), max_starts, replace=False))]
    zs = torch.zeros(1, 32)
    err = {h: [] for h in range(1, H + 1)}; pers = {h: [] for h in range(1, H + 1)}
    disc5, disc5_fair, n1, n30 = [], [], [], []
    for i, t in starts:
        x = te[i]["z"]
        acts = F.one_hot(te[i]["a"][t:t + H], A_ENV).float().unsqueeze(0)
        x0 = x[t:t + 1]
        trj = e2.rollout_with_world(zs, x0, acts, compute_action_objects=False)
        for h in range(1, H + 1):
            y = x[t + h:t + h + 1]
            err[h].append(float((trj.world_states[h] - y).norm())); pers[h].append(float((x0 - y).norm()))
        n1.append(float(trj.world_states[1].norm())); n30.append(float(trj.world_states[H].norm()))
        y = x[t + 1:t + 2]
        errs = []
        for c in range(A_ENV):
            a2 = acts[:, :1].clone(); a2[0, 0] = 0.0; a2[0, 0, c] = 1.0
            errs.append(float((e2.rollout_with_world(zs, x0, a2, compute_action_objects=False).world_states[1] - y).norm()))
        disc5.append(int(np.argmin(errs)) == int(te[i]["a"][t]))
        disc5_fair.append(CA._tie_fair_hit(errs, int(te[i]["a"][t]))[0])
    beats = {h: bool(np.median(err[h]) < np.median(pers[h])) for h in range(1, H + 1)}
    k = 0
    for h in range(1, H + 1):
        if beats[h] and k == h - 1:
            k = h
    return {"n_starts": len(starts), "disc5_h1_tew": float(np.mean(disc5)),
            "disc5_h1_tew_tiefair": float(np.mean(disc5_fair)), "k30": k,
            "beats_persistence_by_depth": {str(h): beats[h] for h in range(1, H + 1)},
            "err_over_pers_by_depth": {str(h): float(np.median(err[h]) / np.median(pers[h])) for h in range(1, H + 1)},
            "rollout_norm_t1_p50": float(np.median(n1)), "rollout_norm_t30_p50": float(np.median(n30)),
            "true_norm_p50": float(np.median([float(te[i]["z"][t].norm()) for i, t in starts]))}


# ------------------------------------------------------------------ scoring
def batch_traj(trajs):
    L = len(trajs[0].world_states)
    return Trajectory(states=[torch.cat([t.states[k] for t in trajs]) for k in range(len(trajs[0].states))],
                      actions=torch.cat([t.actions for t in trajs]),
                      world_states=[torch.cat([t.world_states[k] for t in trajs]) for k in range(L)])


@torch.no_grad()
def depth_scores(agent, trajs):
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
    base = J[2]
    inc = {d: J[d + 1] - J[d] for d in range(2, Lmax)}
    out = {"FULL": J[None], "D1": base.copy()}
    for g in GAMMAS:
        out["DISC_%s" % g] = base + sum((g ** (d - 1)) * inc[d] for d in inc)
    w = {d: 1.0 if fid_beats.get(str(d), False) else 0.0 for d in inc}
    out["FIDW"] = base + sum(w[d] * inc[d] for d in inc)
    return out


@torch.no_grad()
def score_head(agent, states, fid_beats, canary_fn):
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
        true_trajs = [Trajectory(states=[s0, s0], actions=CA.onehot(c, A_ENV).unsqueeze(1),
                                 world_states=[z0, st["z_true"][c]]) for c in range(A_ENV)]
        jt = canary_fn(true_trajs, None)
        bc = None
        if not rows:
            single = canary_fn(pool, None)
            bc = float(np.abs(single - Jn[None]).max() / max(1.0, float(np.abs(single).max())))
        rows.append({"batch_canary_rel": bc, "native": aggregate(Jn, Lmax, fid_beats),
                     "scaf": aggregate(Js, Lmax, fid_beats), "jtrue": np.asarray(jt),
                     "Lmax": Lmax, "full_eq_Lmax_native": float(np.abs(Jn[Lmax] - Jn[None]).max()),
                     "pool_first_classes": [int(a[0, 0].argmax()) for a in st["pool_actions"]]})
    return rows


def tie_set(J):
    J = np.asarray(J, dtype=float)
    m = float(J.min())
    return set(np.nonzero(J <= m + TIE_REL * max(1.0, abs(m)))[0].tolist())


def flip_vs_ref(J_h, J_ref):
    """Expected P(pick differs) under uniform tie-breaks on both sides; plus ref-degenerate flag."""
    P, T = tie_set(J_h), tie_set(J_ref)
    return 1.0 - len(P & T) / (len(P) * len(T)), len(T) == len(J_ref)


def spearman_n3pre(a, b):
    a, b = np.asarray(a), np.asarray(b)
    if np.ptp(a) < 1e-12 or np.ptp(b) < 1e-12:
        return None
    return CA.spearman(a, b)


def metrics(rows_h, refs, states):
    """refs: {name: rows} for pick-flip references. (a)/(b) via I1 e3_choice_quality."""
    out = {}
    for ag in AGGS:
        preds = [r["scaf"][ag] for r in rows_h]
        qa = CA.e3_choice_quality({ag: preds}, [r["jtrue"] for r in rows_h], truth_lower_is_better=True)
        qb = CA.e3_choice_quality({ag: preds}, [st["q"] for st in states], truth_lower_is_better=False)
        rho_alt = [spearman_n3pre(r["scaf"][ag], r["jtrue"]) for r in rows_h]
        rho_alt = [x for x in rho_alt if x is not None]
        m = {"rho_scaf": qa["arms"][ag]["spearman_mean"] if "arms" in qa else None,
             "rho_scaf_n": qa.get("n_informative", 0),
             "rho_scaf_n3pre_form": float(np.mean(rho_alt)) if rho_alt else None,
             "pick_in_Qbest": qb["arms"][ag]["pick_in_best"] if "arms" in qb else None,
             "q_chance": qb.get("chance"), "n_informative_q": qb.get("n_informative", 0),
             "scaf_pick_counts": qa["arms"][ag]["pick_counts"] if "arms" in qa else None}
        for rn, rrows in refs.items():
            fl, deg = [], []
            for r, rr in zip(rows_h, rrows):
                f, d = flip_vs_ref(r["native"][ag], rr["native"][ag])
                fl.append(f); deg.append(d)
            m["flip_vs_" + rn] = float(np.mean(fl))
            m["flip_vs_" + rn + "_plain_argmin"] = float(np.mean(
                [int(np.argmin(r["native"][ag])) != int(np.argmin(rr["native"][ag])) for r, rr in zip(rows_h, rrows)]))
            m["ref_" + rn + "_degenerate_frac"] = float(np.mean(deg))
            # (c3) descriptive: does the pick's first-action class have a better TRUE one-step J
            # than the reference pick's class? (+1 better, -1 worse, 0 same), tie-broken by argmin
            tb = []
            for r, rr in zip(rows_h, rrows):
                ch = r["pool_first_classes"][int(np.argmin(r["native"][ag]))]
                cr = rr["pool_first_classes"][int(np.argmin(rr["native"][ag]))]
                jt = r["jtrue"]
                tb.append(0 if abs(jt[ch] - jt[cr]) < 1e-12 else (1 if jt[ch] < jt[cr] else -1))
            m["toward_better_vs_" + rn] = float(np.mean(tb))
        out[ag] = m
    return out


def habit_contrast(rows_h):
    out = {}
    for ag in AGGS:
        agree, rho = [], []
        for r in rows_h:
            agree.append(int(np.argmin(r["native"][ag])) == int(np.argmin(r["native"]["D1"])))
            s = spearman_n3pre(r["native"][ag], r["native"]["D1"])
            if s is not None:
                rho.append(s)
        out[ag] = {"pick_agree_with_habit": float(np.mean(agree)), "rho_with_habit": float(np.mean(rho)) if rho else None}
    return out


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--post", type=int, default=1200)
    ap.add_argument("--ups", type=int, default=8)
    ap.add_argument("--probe-steps", type=int, default=320)
    ap.add_argument("--probe-every", type=int, default=8)
    ap.add_argument("--ncont", type=int, default=6)
    ap.add_argument("--clen", type=int, default=4)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    t0 = time.time()
    S = a.seed
    res = {"args": vars(a), "code_sha": CODE_SHA}

    def log(msg):
        print("[n3 s%d t=%4.0fs] %s" % (S, time.time() - t0, msg), flush=True)

    # I1 pinned canaries (instrument health)
    ce = CA.canary_e3_structure(seed=S)
    cd = CA.canary_action_discrimination(seed=S)
    res["canary_e3_structure"] = bool(ce["reproduced"])
    res["canary_action_discrimination"] = bool(cd.get("reproduced", False))
    log("I1 canaries e3_structure=%s action_discrimination=%s" % (res["canary_e3_structure"], res["canary_action_discrimination"]))

    R.seed_all(S)
    _e, ref, _c = R.build_B(S, False)
    ref.eval()
    ref_enc = copy.deepcopy(ref.latent_stack.state_dict())
    init = BP.get_head(ref)
    te4_segs, _ = BB.gen_policy(S, 3000 // EP_STEPS, 120, BB.pol_uniform(S * 7 + 3))
    g5 = np.random.default_rng(S * 7 + 5)
    tew_segs, _ = BB.gen_policy(S, 3000 // EP_STEPS, 160, lambda: int(g5.integers(0, 5)))
    TE4 = BB.encode_segs(ref, te4_segs)
    TEW = BB.encode_segs(ref, tew_segs)

    heads, res["heads"] = {"INIT": init}, {}
    for arm in ("real", "shuf", "blind"):
        hp, hd, info = train_member(S, ref, ref_enc, arm, a.post, a.ups, log)
        nm = arm.upper()
        heads[nm] = hd
        res["heads"][nm] = {"member": info, "pre_eval4": BB.evaluate(ref, hp, TE4, "z", S)}
    heads["BLINDR"] = heads["BLIND"]
    heads["BLIND"] = blind_exact(heads["BLINDR"])
    res["blind_action_weight_unchanged_from_init"] = bool(torch.equal(heads["BLINDR"]["a"]["weight"], init["a"]["weight"]))
    res["heads"]["BLINDR"] = {}
    fid = {}
    for nm in ("INIT", "REAL", "SHUF", "BLIND", "BLINDR"):
        ev4 = BB.evaluate(ref, heads[nm], TE4, "z", S)
        evw = eval_tew(ref, heads[nm], TEW, S)
        fid[nm] = evw["beats_persistence_by_depth"]
        res["heads"].setdefault(nm, {})
        res["heads"][nm]["eval4"] = ev4; res["heads"][nm]["tew"] = evw
        log("EVAL %-6s disc4=%.3f k=%d disc5(tew)=%.3f fair=%.3f k30=%d norm t1/t30/true=%.2f/%.2f/%.2f" % (
            nm, ev4["disc4_h1"], ev4["k"], evw["disc5_h1_tew"], evw["disc5_h1_tew_tiefair"], evw["k30"],
            evw["rollout_norm_t1_p50"], evw["rollout_norm_t30_p50"], evw["true_norm_p50"]))
    res["l2r_bar_real"] = bool(res["heads"]["REAL"]["eval4"]["disc4_h1"] >= 0.47 and res["heads"]["REAL"]["eval4"]["k"] == 10)
    res["twin_at_chance"] = bool(res["heads"]["SHUF"]["eval4"]["disc4_h1"] <= 0.32 and res["heads"]["SHUF"]["tew"]["disc5_h1_tew"] <= 0.27)

    # probe states, REAL head live (I1 collect_probe_states)
    def collect(steps):
        pa = BB.fresh_agent(S, ref_enc)
        BP.set_head(pa, heads["REAL"])
        R.seed_all(S + 900)
        env = BB.make_env(S, 100)
        return pa, CA.collect_probe_states(pa, env, steps, a.probe_every, S, action_dim=A_ENV,
                                           n_cont=a.ncont, cont_len=a.clen)
    pa, states = collect(a.probe_steps)
    res["probe_rerun_640"] = False
    if len(states) < 20:
        pa, states = collect(640)
        res["probe_rerun_640"] = True
    val = CA.probe_state_validation(states)
    res["probe"] = {"n_states": len(states), "validation": val,
                    "n_informative_q": int(sum(np.ptp(s["q"]) > 1e-9 for s in states)),
                    "pool_size_p50": float(np.median([len(s["pool_actions"]) for s in states])),
                    "pool_first_class_n_distinct_p50": float(np.median([len(set(int(x[0, 0].argmax()) for x in s["pool_actions"])) for s in states])),
                    "exec_class_counts": dict(Counter(str(s["executed"]) for s in states))}
    log("PROBE n=%d validation=%s maxdiff=%s" % (len(states), val.get("verdict"), val.get("max_abs_diff")))

    score_fn = CA.e3_score_fn(pa)
    rows = {}
    for nm in ("INIT", "REAL", "SHUF", "BLIND", "BLINDR"):
        BP.set_head(pa, heads[nm])
        rows[nm] = score_head(pa, states, fid[nm], score_fn)
    res["decomp_canary_full_eq_Lmax_max"] = float(max(r["full_eq_Lmax_native"] for nm in rows for r in rows[nm]))
    res["batch_canary_rel_max"] = float(max(r["batch_canary_rel"] for nm in rows for r in rows[nm] if r["batch_canary_rel"] is not None))
    refs = {"BLIND": rows["BLIND"], "BLINDR": rows["BLINDR"], "INIT": rows["INIT"]}
    res["metrics"] = {nm: metrics(rows[nm], refs, states) for nm in ("REAL", "SHUF")}
    res["habit_contrast_REAL"] = habit_contrast(rows["REAL"])
    res["fidw_weight_depths"] = {nm: [int(d) for d, b in fid[nm].items() if b and int(d) >= 2] for nm in fid}
    for ag in AGGS:
        mr, ms = res["metrics"]["REAL"][ag], res["metrics"]["SHUF"][ag]
        log("AGG %-8s rho %s/%s  Qbest %s/%s  flipBLIND %.2f/%.2f (deg %.2f) flipBLINDR %.2f/%.2f (deg %.2f) habit_agree=%.2f" % (
            ag, mr["rho_scaf"], ms["rho_scaf"], mr["pick_in_Qbest"], ms["pick_in_Qbest"],
            mr["flip_vs_BLIND"], ms["flip_vs_BLIND"], mr["ref_BLIND_degenerate_frac"],
            mr["flip_vs_BLINDR"], ms["flip_vs_BLINDR"], mr["ref_BLINDR_degenerate_frac"],
            res["habit_contrast_REAL"][ag]["pick_agree_with_habit"]))
    res["t_total_s"] = round(time.time() - t0, 1)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    json.dump(res, open(a.out, "w"), indent=1, default=str)
    log("wrote %s decomp=%.3g batch_rel=%.3g" % (a.out, res["decomp_canary_full_eq_Lmax_max"], res["batch_canary_rel_max"]))


if __name__ == "__main__":
    main()
