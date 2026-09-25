"""Probe N2 (bt0925-n2): does W3's retained replay keep the L2R bar while W6a trains the
world encoder through the read path? (coupled_loop_repair_campaign_plan.md sec 4 N2, P8, Q4c)

Pre-registration: REE_assembly/evidence/planning/n2_replay_encoder_probe_20260925.md
(committed BEFORE any registered seed ran). One invocation = one (seed, arm, twin) run.

Protocol = the W3 member-gate probe (probes/w3/w3_l2r_member_probe.py, f82cb986c5), reused
verbatim for env / agent build / babbling / pre phase / post phase / test set / evaluate(),
pinned to ree-v3 9b322d5 (tag archive/coupled-loop-repair-9b322d5). Arms (config only):
  frozen   : W6a OFF                                   (= the W3 member-gate configuration)
  reencode : W6a ON  + W3 replay_latent "reencode"     (raw obs re-encoded at replay)
  stored   : W6a ON  + W3 replay_latent "stored"       (the z sensed at record time)
W6a = WorldEncoderMember at its from_dims defaults (lr 1e-3, batch 64, window auto = 26 at
alpha_world 0.3, grad_clip 1.0, 1 update per waking step), registered AFTER the W3 member.
It records every sensed tick (babble + post) and trains ONLY in the post phase (the waking
run: every_k = 1), so babble + pre phase are identical across arms.
Twin: shuf = retained babbling actions relabelled by the FIXED class permutation (W3's).

Readouts at the END of the post phase (gates are pre-registered in the record):
  PRIMARY  : evaluate() of the post head on the held-out test set encoded through the
             CURRENT (end-of-run) encoder -- disc4_h1, k, disc5; rollout (e) from those starts.
  retention: (post_cur - B0) / (pre - B0); B0 + pre are in the (frozen) reference space,
             B0 recomputed here with the babbling probe's own recipe (--b0-only).
  SECONDARY (not gating): (i) per-dimension standardised error variant of disc4/k in the
             current space; (ii) the post head read in the REFERENCE space; (iii) latent
             scale / PR / encoder drift; (iv) stored-vs-current latent staleness.
ASCII output only.
"""
from __future__ import annotations

import argparse, copy, json, sys, time
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F

p = argparse.ArgumentParser()
p.add_argument("--seed", type=int, required=True)
p.add_argument("--wt", required=True)
p.add_argument("--arm", choices=["frozen", "reencode", "stored"])
p.add_argument("--twin", choices=["real", "shuf"], default="real")
p.add_argument("--out", required=True)
p.add_argument("--b0-only", action="store_true")
p.add_argument("--b0-cache", default=None)
p.add_argument("--post", type=int, default=1200)
p.add_argument("--ups", type=int, default=8)
p.add_argument("--w6a-ups", type=int, default=1)
p.add_argument("--w6a-batch", type=int, default=64)
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
from ree_core.utils import waking_trainer_world_encoder as WE  # noqa: E402
from ree_core.developmental.structured_babbling import StructuredBabbler  # noqa: E402

S = a.seed
t0 = time.time()
PERM = [1, 2, 3, 4, 0]
A_ENV, CLASSES = BB.A_ENV, BB.CLASSES


def log(m):
    print("[n2 s%d %s/%s t=%4.0fs] %s" % (S, a.arm, a.twin, time.time() - t0, m), flush=True)


for mod in (WT, WE):
    assert str(Path(mod.__file__).resolve()).startswith(str(Path(a.wt).resolve())), mod.__file__


@torch.no_grad()
def evaluate_sd(ref, head, te, key, seed, sd=None, H=10, max_starts=300):
    """BB.evaluate with an optional per-dimension standardisation of the error metric
    (pred and target both divided by sd).  sd=None reproduces BB.evaluate exactly."""
    BP.set_head(ref, head)
    e2 = ref.e2
    g = np.random.default_rng(seed + 77)
    starts = [(i, t) for i, e in enumerate(te) for t in range(e["a"].shape[0] - H + 1)]
    if len(starts) > max_starts:
        starts = [starts[j] for j in sorted(g.choice(len(starts), max_starts, replace=False))]
    zs = torch.zeros(1, 32)
    w = torch.ones(1, 32) if sd is None else (1.0 / sd.clamp_min(1e-6)).reshape(1, -1)
    rows = {h: {"err": [], "pers": []} for h in range(1, H + 1)}
    disc4, disc5 = {1: [], 3: [], 5: []}, {1: []}
    for i, t in starts:
        x = te[i][key]
        acts = F.one_hot(te[i]["a"][t:t + H], A_ENV).float().unsqueeze(0)
        x0 = x[t:t + 1]
        tr = e2.rollout_with_world(zs, x0, acts, compute_action_objects=False)
        for h in range(1, H + 1):
            y = x[t + h:t + h + 1]
            rows[h]["err"].append(float(((tr.world_states[h] - y) * w).norm()))
            rows[h]["pers"].append(float(((x0 - y) * w).norm()))
        ex = int(te[i]["a"][t])
        for h in (1, 3, 5):
            y = x[t + h:t + h + 1]
            errs = []
            for c in range(A_ENV):
                a2 = acts[:, :h].clone(); a2[0, 0] = 0.0; a2[0, 0, c] = 1.0
                errs.append(float(((e2.rollout_with_world(zs, x0, a2, compute_action_objects=False)
                                    .world_states[h] - y) * w).norm()))
            e4 = [errs[c] for c in CLASSES]
            disc4[h].append(int(np.argmin(e4)) == CLASSES.index(ex))
            if h == 1:
                disc5[1].append(int(np.argmin(errs)) == ex)
    k, eop = 0, {}
    for h in range(1, H + 1):
        me, mp = float(np.median(rows[h]["err"])), float(np.median(rows[h]["pers"]))
        eop[h] = me / mp if mp > 0 else None
        if mp > 0 and me < mp and k == h - 1:
            k = h
    return {"n_starts": len(starts), "disc4_h1": float(np.mean(disc4[1])), "disc4_h3": float(np.mean(disc4[3])),
            "disc4_h5": float(np.mean(disc4[5])), "disc5_h1": float(np.mean(disc5[1])), "k": k,
            "err_over_pers_h1": eop[1], "err_over_pers_h5": eop[5]}


def rollout_e(ref, head, TE, seed):
    BP.set_head(ref, head)
    g = np.random.default_rng(seed + 31)
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
    return {"t30_over_t0_median": float(np.median(t30)), "late_growth_median": float(np.median(late)),
            "late_growth_max": float(np.max(late)),
            "gate_e": bool(float(np.max(late)) < 1.2 and float(np.median(t30)) < 5.0)}


def pr_and_norm(TE):
    Z = torch.cat([e["z"] for e in TE])
    Zc = Z - Z.mean(0)
    ev = torch.linalg.eigvalsh(Zc.T @ Zc / max(1, Z.shape[0] - 1)).clamp_min(0)
    return {"pr": float(ev.sum() ** 2 / (ev ** 2).sum().clamp_min(1e-30)),
            "norm_median": float(Z.norm(dim=-1).median()), "sd": Z.std(0)}


# ------------------------------------------------------------------ reference build + test set
R.seed_all(S)
_e, ref, _c = R.build_B(S, False)
ref.eval()
ref_enc = copy.deepcopy(ref.latent_stack.state_dict())
init = BP.get_head(ref)
te_segs, _ = BB.gen_policy(S, 3000 // BB.EP_STEPS, 120, BB.pol_uniform(S * 7 + 3))
TE = BB.encode_segs(ref, te_segs)
ev_init = BB.evaluate(ref, init, TE, "z", S)

if a.b0_only:
    # B0 = the babbling probe's on-policy-data head (babble_probe.main POL + train_head).
    pol_agent = BB.fresh_agent(S, ref_enc)
    R.seed_all(S + 300)
    pol_segs, pol_info = BB.gen_POL(pol_agent, S, 12, 25)   # published runs: --n-eps 12
    trapped = bool(pol_info["early_per_1000"] >= 3.0 or pol_info["harm_events_per_100"] >= 10.0)
    E_POL = BB.encode_segs(ref, pol_segs)
    hd, tinfo = BB.train_head(ref, init, BB.to_trans(E_POL, "z"), BB.PRE_UPD, S)
    ev_b0 = BB.evaluate(ref, hd, TE, "z", S)
    out = {"seed": S, "hazard_class": "hazard-trapped" if trapped else "benign", "pol_run": pol_info,
           "B0": ev_b0, "B0_train": tinfo, "init": ev_init, "t_s": time.time() - t0}
    json.dump(out, open(a.out, "w"), indent=1, default=str)
    log("B0 disc4 %.4f k %d INIT %.4f class %s pol %s" % (ev_b0["disc4_h1"], ev_b0["k"], ev_init["disc4_h1"],
                                                          out["hazard_class"], json.dumps(pol_info)))
    raise SystemExit(0)

b0 = json.load(open(a.b0_cache))
assert abs(b0["init"]["disc4_h1"] - ev_init["disc4_h1"]) < 1e-12, "INIT mismatch vs B0 cache"
B0 = b0["B0"]["disc4_h1"]
log("INIT disc4 %.4f B0 %.4f (%s)" % (ev_init["disc4_h1"], B0, b0["hazard_class"]))

# ------------------------------------------------------------------ member agent
agent = BB.fresh_agent(S, ref_enc)
cfg = agent.config
cfg.waking_trainer_guard_min_steps = 8
latent_mode = "stored" if a.arm == "stored" else "reencode"
member = WT.E2WorldMember(agent, lr=3e-4, batch_size=32, buffer_max=2000, retained_max=5000,
                          replay_frac=0.25, reencode_window=0, replay_latent=latent_mode,
                          objective="mse", grad_clip=1.0, updates_per_step=1)
members = [member]
wem = None
if a.arm in ("reencode", "stored"):
    wem = WE.WorldEncoderMember(agent, lr=1e-3, batch_size=a.w6a_batch, buffer_max=2000, window=0,
                                grad_clip=1.0, updates_per_step=a.w6a_ups, seed=S)
    members.append(wem)
tr = WT.WakingTrainer(agent, cfg, members=members)
agent.waking_trainer = tr
woe0 = agent.world_obs_encoder[0].weight.detach().clone()
log("members %s W3 W=%d alpha_world=%.2f latent=%s" % (list(tr.members), member.reencode_window,
                                                      cfg.latent.alpha_world, member.replay_latent))

# babbling epoch (identical to the W3 probe; W6a only records here)
bab = StructuredBabbler(n_classes=5, max_run=4, seed=S * 13 + 1)
tr.set_e2_world_source("babble")
tr.every_k = 10 ** 9
counts = [0] * 5
with torch.no_grad():
    for k in range(12):
        env = BB.make_env(S, k)
        _f, od = env.reset(); agent.reset(); bab.reset()
        for _s in range(BB.EP_STEPS):
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
if a.twin == "shuf":
    for r in member._retained:
        r["a"] = F.one_hot(torch.tensor([PERM[int(r["a"].argmax())]]), 5).float()
log("babble done: retained %d classes %s" % (retained_n, counts))
snap = [(r["step"], r["a"].clone(), r["obs"][-1][1].clone()) for r in member._retained]
for _u in range(3000):
    tr._update("e2_world", member)
assert torch.equal(agent.world_obs_encoder[0].weight, woe0), "encoder moved before the post phase"
ev_pre = BB.evaluate(ref, BP.get_head(agent), TE, "z", S)
log("pre disc4 %.4f k %d" % (ev_pre["disc4_h1"], ev_pre["k"]))

# post phase: native closed loop; W3 on-policy + 25% retained; W6a trains the encoder (arms 2/3)
tr.set_e2_world_source("on_policy")
tr.every_k = 1
member.updates_per_step = a.ups
agent.reset()
R.seed_all(S + 500)
rew, acts_all = [], []
tpost = time.time()
for ep in range(a.post // BB.EP_STEPS):
    env = BB.make_env(S, 50 + ep)
    hh = StepHarness(agent, env, train_mode=False, seed=S * 1000 + 50 + ep)
    _f, od = env.reset(); agent.reset(); hh.reset()
    for _s in range(BB.EP_STEPS):
        r = hh.step(od)
        rew.append(float(r.harm_signal)); acts_all.append(int(r.action.detach().reshape(-1).argmax()))
        od = r.next_obs_dict
        if r.done:
            _f, od = env.reset(); agent.reset(); hh.reset()
    log("post ep %d done (%.0fs) steps %s" % (ep, time.time() - tpost, dict(tr.steps)))
head_post = BP.get_head(agent)
frozen_ok = len(snap) == len(member._retained) and all(
    s == r["step"] and torch.equal(aa, r["a"]) and torch.equal(o, r["obs"][-1][1])
    for (s, aa, o), r in zip(snap, member._retained))

# ------------------------------------------------------------------ readouts
# the run is over: detach the trainer (sense would record into its buffers) and encode the
# test streams through the agent's own end-of-run read path (encode_segs resets per episode).
saved_tr = agent.waking_trainer
agent.waking_trainer = None
TE_cur = BB.encode_segs(agent, te_segs)
agent.waking_trainer = saved_tr
st_ref, st_cur = pr_and_norm(TE), pr_and_norm(TE_cur)
ev_cur = evaluate_sd(ref, head_post, TE_cur, "z", S)             # PRIMARY
ev_cur_std = evaluate_sd(ref, head_post, TE_cur, "z", S, sd=st_cur["sd"])   # secondary (i)
ev_refspace = evaluate_sd(ref, head_post, TE, "z", S)             # secondary (ii)
ev_refspace_bb = BB.evaluate(ref, head_post, TE, "z", S)
assert ev_refspace_bb == ev_refspace, "evaluate_sd(sd=None) does not reproduce BB.evaluate"
roll_cur = rollout_e(ref, head_post, TE_cur, S)
roll_ref = rollout_e(ref, head_post, TE, S)

# staleness: stored z (record time) vs the current read path, on retained + on-policy samples
g = torch.Generator().manual_seed(S + 5)
stale = {}
for nm, buf in (("retained", member._retained), ("on_policy", list(member._on_policy))):
    idx = torch.randperm(len(buf), generator=g)[:256].tolist()
    recs = [buf[i] for i in idx if buf[i].get("z_live") is not None]
    if not recs:
        continue
    zs0 = torch.cat([r["z_live"][0] for r in recs])
    zr0, _zr1 = member._reencode(recs)
    stale[nm] = {"n": len(recs),
                 "rel_diff_median": float(((zs0 - zr0).norm(dim=-1) / zr0.norm(dim=-1).clamp_min(1e-9)).median()),
                 "norm_ratio_current_over_stored_median": float((zr0.norm(dim=-1) / zs0.norm(dim=-1).clamp_min(1e-9)).median())}

woe_rel = float((agent.world_obs_encoder[0].weight.detach() - woe0).norm() / woe0.norm())
res = {
    "seed": S, "arm": a.arm, "twin": a.twin, "hazard_class": b0["hazard_class"],
    "config": {"post": a.post, "ups": a.ups, "w6a_ups": a.w6a_ups, "w6a_batch": a.w6a_batch,
               "replay_latent": member.replay_latent, "w3_window": member.reencode_window,
               "w6a_window": None if wem is None else wem.window, "wt": a.wt},
    "init": ev_init, "B0": B0, "pre": ev_pre,
    "post_current": ev_cur, "post_current_std": ev_cur_std, "post_refspace": ev_refspace,
    "retention": (ev_cur["disc4_h1"] - B0) / (ev_pre["disc4_h1"] - B0) if ev_pre["disc4_h1"] != B0 else None,
    "gate_a": bool(ev_cur["disc4_h1"] >= 0.47 and ev_cur["k"] == 10),
    "gate_a_std_secondary": bool(ev_cur_std["disc4_h1"] >= 0.47 and ev_cur_std["k"] == 10),
    "gate_a_refspace_secondary": bool(ev_refspace["disc4_h1"] >= 0.47 and ev_refspace["k"] == 10),
    "rollout_current": roll_cur, "rollout_refspace": roll_ref,
    "guard": {k: v.status for k, v in tr.guard_results.items()},
    "frozen_retained_unchanged_after_post": frozen_ok,
    "retained_n": retained_n, "babble_class_counts": counts, "onpol_n": len(member._on_policy),
    "updates": dict(tr.steps), "drawn_retained": member.n_drawn_retained,
    "drawn_on_policy": member.n_drawn_on_policy, "n_reencoded": member.n_reencoded,
    "n_cache_hits": member.n_cache_hits,
    "latent_ref": {"pr": st_ref["pr"], "norm_median": st_ref["norm_median"]},
    "latent_current": {"pr": st_cur["pr"], "norm_median": st_cur["norm_median"]},
    "norm_ratio_current_over_ref": st_cur["norm_median"] / max(st_ref["norm_median"], 1e-9),
    "world_obs_encoder_rel_change": woe_rel,
    "w6a_last_terms": None if wem is None else wem.last_terms,
    "staleness": stale,
    "post_reward_per_100": float(np.sum(rew) * 100.0 / len(rew)),
    "post_action_counts": {str(c): acts_all.count(c) for c in range(5)},
    "t_post_s": time.time() - tpost, "t_total_s": time.time() - t0,
}
json.dump(res, open(a.out, "w"), indent=1, default=str)
log("RESULT cur disc4 %.4f k %d disc5 %.4f gate_a %s ret %s | std %.4f k %d | refspace %.4f k %d | "
    "e %s t30 %.2f late %.3f/%.3f | norm x%.2f PR %.2f->%.2f woe %.3f | guard %s frozen %s | stale %s" % (
        ev_cur["disc4_h1"], ev_cur["k"], ev_cur["disc5_h1"], res["gate_a"],
        None if res["retention"] is None else round(res["retention"], 3),
        ev_cur_std["disc4_h1"], ev_cur_std["k"], ev_refspace["disc4_h1"], ev_refspace["k"],
        roll_cur["gate_e"], roll_cur["t30_over_t0_median"], roll_cur["late_growth_median"],
        roll_cur["late_growth_max"], res["norm_ratio_current_over_ref"], st_ref["pr"], st_cur["pr"],
        woe_rel, res["guard"], frozen_ok,
        {k: round(v["rel_diff_median"], 3) for k, v in stale.items()}))
