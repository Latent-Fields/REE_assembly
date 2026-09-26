"""Probe (bt0926-w3rel): how reliably does the W3 L2R-bar recipe pass on fresh seeds, and
what predicts a miss?

Pre-registration: REE_assembly/evidence/planning/w3_reliability_sweep_20260926.md (committed
BEFORE any registered seed ran). One invocation = one seed. Recipe reused BYTE-IDENTICALLY
from probes/w3/w3_l2r_member_probe.py (bt0925-w3, gate (a) disc4_h1 >= 0.47 and k == 10):
babbling 2400 steps (StructuredBabbler, 5 classes incl. stay, k=0..11) -> FROZEN retained set
-> 3000 member updates (pre) -> --post native closed-loop StepHarness steps (default 1200,
k=50.., 8 member updates/step, 25% retained mix, re-encoded) -> evaluate() on the held-out
disc4/disc5 test set (3000 uniform {0..3}, k=120..134). SHUF twin: retained babbling actions
relabelled by the FIXED permutation [1,2,3,4,0] (same as W3/N2/N3/N5).

Predictors recorded BEFORE the training outcome is known (pre-registered list, w3rel doc sec
2): B0 disc4 (babble_probe's own POL + train_head recipe, --n-eps 12, 3000 updates -- same
recipe N2 used), INIT disc (untrained head), babble-phase action-class distribution (entropy
+ share of class 4 "stay" + share of wall-push/no-displacement steps among classes 0-3),
post-phase action-class distribution (same three stats over the post-phase's native actions),
and the A1 hazard-trapped/benign stratum (coupled_acceptance.classify_stratum over this run's
OWN post-phase `done` flags, window=600 -- cheap: no extra rollout).

--dose N reruns ONLY the real arm with --post N instead of 1200 (report-only DOSE probe on
seeds that missed gate (a) at the registered dose); it skips B0/INIT/shuf (already have them
from the --post 1200 run, passed via --b0-cache).

ASCII output only.
"""
from __future__ import annotations

import argparse, copy, json, sys, time
from pathlib import Path

import numpy as np
import torch

p = argparse.ArgumentParser()
p.add_argument("--seed", type=int, required=True)
p.add_argument("--wt", required=True)
p.add_argument("--out", required=True)
p.add_argument("--post", type=int, default=1200)
p.add_argument("--ups", type=int, default=8)
p.add_argument("--dose", action="store_true", help="report-only: real arm only, reuse --b0-cache")
p.add_argument("--b0-cache", default=None)
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
from experiments._lib import coupled_acceptance as CA  # noqa: E402
from ree_core.utils import waking_trainer as WT  # noqa: E402
from ree_core.developmental.structured_babbling import StructuredBabbler  # noqa: E402

S = a.seed
t0 = time.time()
PERM = [1, 2, 3, 4, 0]


def log(m):
    print("[w3rel s%d %s t=%4.0fs] %s" % (S, ("dose%d" % a.post if a.dose else "real"),
                                           time.time() - t0, m), flush=True)


assert WT.E2WorldMember.__module__ == "ree_core.utils.waking_trainer"
assert str(Path(WT.__file__).resolve()).startswith(str(Path(a.wt).resolve())), WT.__file__

R.seed_all(S)
_e, ref, _c = R.build_B(S, False)
ref.eval()
ref_enc = copy.deepcopy(ref.latent_stack.state_dict())
init = BP.get_head(ref)
te_segs, _ = BB.gen_policy(S, 3000 // BB.EP_STEPS, 120, BB.pol_uniform(S * 7 + 3))
TE = BB.encode_segs(ref, te_segs)
ev_init = BB.evaluate(ref, init, TE, "z", S)
log("INIT disc4 %.4f k %d" % (ev_init["disc4_h1"], ev_init["k"]))

if a.b0_cache:
    b0c = json.load(open(a.b0_cache))
    assert abs(b0c["init"]["disc4_h1"] - ev_init["disc4_h1"]) < 1e-12, "INIT mismatch vs B0 cache"
    B0 = b0c["B0"]
    hazard_babble = b0c["hazard_class_babble"]
else:
    # B0 = babble_probe's own on-policy-data head (POL + train_head), --n-eps 12 (N2's recipe)
    pol_agent = BB.fresh_agent(S, ref_enc)
    R.seed_all(S + 300)
    pol_segs, pol_info = BB.gen_POL(pol_agent, S, 12, 25)
    trapped_b = bool(pol_info["early_per_1000"] >= 3.0 or pol_info["harm_events_per_100"] >= 10.0)
    del pol_agent
    E_POL = BB.encode_segs(ref, pol_segs)
    hd, tinfo = BB.train_head(ref, init, BB.to_trans(E_POL, "z"), BB.PRE_UPD, S)
    ev_b0 = BB.evaluate(ref, hd, TE, "z", S)
    B0 = ev_b0["disc4_h1"]
    hazard_babble = "hazard-trapped" if trapped_b else "benign"
    log("B0 disc4 %.4f k %d class(babble-POL)=%s pol=%s" % (
        ev_b0["disc4_h1"], ev_b0["k"], hazard_babble, json.dumps(pol_info)))

results = {}
for arm in (["real"] if a.dose else ["real", "shuf"]):
    log("== arm %s ==" % arm)
    agent = BB.fresh_agent(S, ref_enc)
    cfg = agent.config
    cfg.waking_trainer_guard_min_steps = 8
    member = WT.E2WorldMember(agent, lr=3e-4, batch_size=32, buffer_max=2000, retained_max=5000,
                              replay_frac=0.25, reencode_window=0, replay_latent="reencode",
                              objective="mse", grad_clip=1.0, updates_per_step=1)
    tr = WT.WakingTrainer(agent, cfg, members=[member])
    agent.waking_trainer = tr

    bab = StructuredBabbler(n_classes=5, max_run=4, seed=S * 13 + 1)
    tr.set_e2_world_source("babble")
    tr.every_k = 10 ** 9
    counts_bab = [0] * 5
    wall_bab = 0
    n_move_bab = 0
    with torch.no_grad():
        for k in range(12):
            env = BB.make_env(S, k)
            _f, od = env.reset(); agent.reset(); bab.reset()
            for _s in range(BB.EP_STEPS):
                agent.sense(od["body_state"], od["world_state"], obs_harm=od.get("harm_obs"),
                            obs_harm_a=od.get("harm_obs_a"), obs_harm_history=od.get("harm_history"))
                act = bab.next_action()
                c = int(act.argmax()); counts_bab[c] += 1
                px, py = env.agent_x, env.agent_y
                agent.record_executed_action(act)
                _f, h, done, _i, od = env.step(c)
                if c != 4:
                    n_move_bab += 1
                    if env.agent_x == px and env.agent_y == py:
                        wall_bab += 1
                tr.on_waking_step(float(h))
                if done:
                    _f, od = env.reset(); agent.reset(); bab.reset()
    retained_n = len(member._retained)
    if arm == "shuf":
        for r in member._retained:
            r["a"] = torch.nn.functional.one_hot(torch.tensor([PERM[int(r["a"].argmax())]]), 5).float()
    snap = [(r["step"], r["a"].clone(), r["obs"][-1][1].clone()) for r in member._retained]
    for _u in range(3000):
        tr._update("e2_world", member)
    ev_pre = BB.evaluate(ref, BP.get_head(agent), TE, "z", S)
    log("pre disc4 %.4f k %d babble_entropy %.3f stay_share %.3f wall_share(of moves) %.3f" % (
        ev_pre["disc4_h1"], ev_pre["k"], BB.entropy({str(i): c for i, c in enumerate(counts_bab)}),
        counts_bab[4] / sum(counts_bab), wall_bab / max(n_move_bab, 1)))

    tr.set_e2_world_source("on_policy")
    tr.every_k = 1
    member.updates_per_step = a.ups
    agent.reset()
    R.seed_all(S + 500)
    rew, acts_all, dones_all = [], [], []
    wall_post, n_move_post = 0, 0
    for ep in range(a.post // BB.EP_STEPS):
        env = BB.make_env(S, 50 + ep)
        hh = StepHarness(agent, env, train_mode=False, seed=S * 1000 + 50 + ep)
        _f, od = env.reset(); agent.reset(); hh.reset()
        for _s in range(BB.EP_STEPS):
            px, py = env.agent_x, env.agent_y
            r = hh.step(od)
            c = int(r.action.detach().reshape(-1).argmax())
            rew.append(float(r.harm_signal)); acts_all.append(c); dones_all.append(bool(r.done))
            if c != 4:
                n_move_post += 1
                if env.agent_x == px and env.agent_y == py:
                    wall_post += 1
            od = r.next_obs_dict
            if r.done:
                _f, od = env.reset(); agent.reset(); hh.reset()
    head_post = BP.get_head(agent)
    ev_post = BB.evaluate(ref, head_post, TE, "z", S)
    frozen_ok = len(snap) == len(member._retained) and all(
        s == rr["step"] and torch.equal(aa, rr["a"]) and torch.equal(o, rr["obs"][-1][1])
        for (s, aa, o), rr in zip(snap, member._retained))
    counts_post = [acts_all.count(i) for i in range(5)]

    ratios_t30, late_growth = [], []
    BP.set_head(ref, head_post)
    g = np.random.default_rng(S + 31)
    with torch.no_grad():
        for i in range(40):
            ep = TE[int(g.integers(0, len(TE)))]
            t = int(g.integers(0, ep["z"].shape[0]))
            x0 = ep["z"][t:t + 1]
            acts = torch.nn.functional.one_hot(torch.tensor(g.integers(0, 5, 30)), 5).float().unsqueeze(0)
            ws = ref.e2.rollout_with_world(torch.zeros(1, 32), x0, acts, compute_action_objects=False).world_states
            n = [float(w.norm()) for w in ws]
            ratios_t30.append(n[30] / max(n[0], 1e-9))
            late_growth.append(float(np.mean([n[j] / max(n[j - 1], 1e-9) for j in range(21, 31)])))

    stratum = CA.classify_stratum(dones_all, window=min(600, len(dones_all)))

    res = {
        "seed": S, "arm": arm, "post_n": a.post,
        "init": ev_init, "B0": B0, "hazard_class_babble": hazard_babble,
        "pre": ev_pre, "post": ev_post,
        "retention": ((ev_post["disc4_h1"] - B0) / (ev_pre["disc4_h1"] - B0)
                      if ev_pre["disc4_h1"] != B0 else None),
        "gate_a": bool(ev_post["disc4_h1"] >= 0.47 and ev_post["k"] == 10),
        "guard": {k: v.status for k, v in tr.guard_results.items()},
        "frozen_retained_unchanged_after_post": frozen_ok,
        "retained_n": retained_n,
        "babble_action_counts": counts_bab,
        "babble_entropy": BB.entropy({str(i): c for i, c in enumerate(counts_bab)}),
        "babble_stay_share": counts_bab[4] / sum(counts_bab),
        "babble_wallpush_share_of_moves": wall_bab / max(n_move_bab, 1),
        "post_action_counts": counts_post,
        "post_entropy": BB.entropy({str(i): c for i, c in enumerate(counts_post)}),
        "post_stay_share": counts_post[4] / sum(counts_post),
        "post_wallpush_share_of_moves": wall_post / max(n_move_post, 1),
        "hazard_stratum_A1": stratum,
        "rollout_t30_over_t0_median": float(np.median(ratios_t30)),
        "rollout_late_step_growth_median": float(np.median(late_growth)),
        "rollout_late_step_growth_max": float(np.max(late_growth)),
        "t_arm_s": time.time() - t0,
    }
    results[arm] = res
    log("RESULT arm=%s post disc4 %.4f k %d gate_a %s ret %s stratum=%s t30/t0 %.2f late %.3f" % (
        arm, ev_post["disc4_h1"], ev_post["k"], res["gate_a"],
        None if res["retention"] is None else round(res["retention"], 3),
        stratum.get("stratum", stratum.get("reason")), res["rollout_t30_over_t0_median"],
        res["rollout_late_step_growth_median"]))

out = {"seed": S, "post": a.post, "dose_run": a.dose, "arms": results,
       "init": ev_init, "B0": B0, "hazard_class_babble": hazard_babble,
       "t_total_s": time.time() - t0}
json.dump(out, open(a.out, "w"), indent=1, default=str)
log("DONE t_total=%.0fs" % (time.time() - t0))
