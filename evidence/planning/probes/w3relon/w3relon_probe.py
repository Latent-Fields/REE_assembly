"""Probe (bt0926-w3relon): paired re-run of the W3 reliability sweep with
use_zworld_ema_reset_init ON, for the same 15 seeds (901-915) that bt0926-w3rel
registered OFF.

Pre-registration: chip-20260926-w3-reliability-with-ema-fix (Z_w3relon.md).
Recipe reused BYTE-IDENTICALLY from probes/w3rel/w3rel_probe.py (bt0926-w3rel),
which itself reused byte-identically from probes/w3/w3_l2r_member_probe.py
(bt0925-w3): babbling 2400 steps (StructuredBabbler, 5 classes incl. stay,
k=0..11) -> FROZEN retained set -> 3000 member updates (pre) -> 1200 native
closed-loop StepHarness steps (k=50.., 8 member updates/step, 25% retained mix,
re-encoded) -> evaluate() on the held-out disc4/disc5 test set (3000 uniform
{0..3}, k=120..134). SHUF twin: retained babbling actions relabelled by the
fixed permutation [1,2,3,4,0].

The ONLY change from w3rel_probe.py: an optional --knob flag that, when set,
turns on LatentStackConfig.use_zworld_ema_reset_init for the WHOLE pipeline --
set on BOTH `ref`'s config (before held-out-state generation / INIT / B0) and
each arm's training `agent`'s config (before babbling starts) -- exactly the
pattern gate_c_ema_reset_init_probe.py (bt0926-gatec3) used. --knob false
(default) reproduces w3rel_probe.py's own code path bit-for-bit (used here as
the canary against the committed OFF results).

Runs MULTIPLE seeds in one process (amortised imports), one JSON per seed,
checking a wall-time budget between seeds so a batch can be stopped cleanly
before the Mac-lock hold's ~15 min cap.

ASCII output only.
"""
from __future__ import annotations

import argparse, copy, json, sys, time
from pathlib import Path

import numpy as np
import torch

p = argparse.ArgumentParser()
p.add_argument("--seeds", required=True, help="comma-separated seed list")
p.add_argument("--wt", required=True)
p.add_argument("--out-dir", required=True)
p.add_argument("--tag", required=True, help="output filename prefix, e.g. ON or CANARY")
p.add_argument("--knob", choices=["true", "false"], required=True)
p.add_argument("--post", type=int, default=1200)
p.add_argument("--ups", type=int, default=8)
p.add_argument("--budget-s", type=float, default=900.0, help="stop starting new seeds once this much wall time has elapsed")
a = p.parse_args()

KNOB = (a.knob == "true")
SEEDS = [int(s) for s in a.seeds.split(",") if s.strip()]

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

assert WT.E2WorldMember.__module__ == "ree_core.utils.waking_trainer"
assert str(Path(WT.__file__).resolve()).startswith(str(Path(a.wt).resolve())), WT.__file__

t_batch0 = time.time()
PERM = [1, 2, 3, 4, 0]
completed = []


def log(S, m):
    print("[w3relon %s s%d t=%4.0fs] %s" % (a.tag, S, time.time() - t_batch0, m), flush=True)


def run_seed(S):
    t0 = time.time()
    R.seed_all(S)
    _e, ref, _c = R.build_B(S, False)
    ref.eval()
    ref.latent_stack.config.use_zworld_ema_reset_init = bool(KNOB)
    ref_enc = copy.deepcopy(ref.latent_stack.state_dict())
    init = BP.get_head(ref)
    te_segs, _ = BB.gen_policy(S, 3000 // BB.EP_STEPS, 120, BB.pol_uniform(S * 7 + 3))
    TE = BB.encode_segs(ref, te_segs)
    ev_init = BB.evaluate(ref, init, TE, "z", S)
    log(S, "INIT disc4 %.4f k %d knob=%s" % (ev_init["disc4_h1"], ev_init["k"], KNOB))

    # B0 = babble_probe's own on-policy-data head (POL + train_head), n_eps=12
    pol_agent = BB.fresh_agent(S, ref_enc)
    pol_agent.latent_stack.config.use_zworld_ema_reset_init = bool(KNOB)
    R.seed_all(S + 300)
    pol_segs, pol_info = BB.gen_POL(pol_agent, S, 12, 25)
    trapped_b = bool(pol_info["early_per_1000"] >= 3.0 or pol_info["harm_events_per_100"] >= 10.0)
    del pol_agent
    E_POL = BB.encode_segs(ref, pol_segs)
    hd, tinfo = BB.train_head(ref, init, BB.to_trans(E_POL, "z"), BB.PRE_UPD, S)
    ev_b0 = BB.evaluate(ref, hd, TE, "z", S)
    B0 = ev_b0["disc4_h1"]
    hazard_babble = "hazard-trapped" if trapped_b else "benign"
    log(S, "B0 disc4 %.4f k %d class(babble-POL)=%s pol=%s" % (
        ev_b0["disc4_h1"], ev_b0["k"], hazard_babble, json.dumps(pol_info)))

    results = {}
    for arm in ("real", "shuf"):
        log(S, "== arm %s ==" % arm)
        agent = BB.fresh_agent(S, ref_enc)
        agent.latent_stack.config.use_zworld_ema_reset_init = bool(KNOB)
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
        log(S, "pre disc4 %.4f k %d babble_entropy %.3f stay_share %.3f wall_share(of moves) %.3f" % (
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
            "seed": S, "arm": arm, "post_n": a.post, "knob": KNOB,
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
        log(S, "RESULT arm=%s post disc4 %.4f k %d gate_a %s ret %s stratum=%s t30/t0 %.2f late %.3f" % (
            arm, ev_post["disc4_h1"], ev_post["k"], res["gate_a"],
            None if res["retention"] is None else round(res["retention"], 3),
            stratum.get("stratum", stratum.get("reason")), res["rollout_t30_over_t0_median"],
            res["rollout_late_step_growth_median"]))

    out = {"seed": S, "post": a.post, "knob": KNOB, "arms": results,
           "init": ev_init, "B0": B0, "hazard_class_babble": hazard_babble,
           "t_total_s": time.time() - t0}
    outp = Path(a.out_dir) / ("%s_s%d.json" % (a.tag, S))
    json.dump(out, open(outp, "w"), indent=1, default=str)
    log(S, "DONE t_seed=%.0fs -> %s" % (time.time() - t0, outp))
    return out


for S in SEEDS:
    if time.time() - t_batch0 > a.budget_s:
        print("[w3relon %s BUDGET] stopping before seed %d, elapsed %.0fs > budget %.0fs" % (
            a.tag, S, time.time() - t_batch0, a.budget_s), flush=True)
        break
    out = run_seed(S)
    completed.append(S)

print("[w3relon %s BATCH DONE] completed=%s t_total=%.0fs" % (
    a.tag, completed, time.time() - t_batch0), flush=True)
