"""W3 member gate: the L2R bar re-measured on E2WorldMember (bt0925-w3).

Protocol = babbling_e2_action_coverage_probe_20260925.md (0ac69c87446) L2R arm, with the
babbling source and the replay done by the BUILT member (ree_core/utils/waking_trainer.py
E2WorldMember) instead of the probe's hand-rolled loop:
  * env / agent / test set / evaluate(): the babble probe's own functions (babble_probe.py,
    rollout_fidelity_probe.build_B); test set = 3000 uniform-random {0..3} steps, k=120..134.
  * babbling: W2a StructuredBabbler (5 classes incl. stay, runs {1..4}, own seed), 2400
    transitions over Phase-0 episodes k=0..11 through agent.sense + the member (source
    'babble' -> FROZEN retained set, raw obs); then 3000 member updates (probe: 3000).
  * post: 1200 native closed-loop StepHarness steps (k=50..55), member source 'on_policy',
    8 member updates per step once 32 on-policy transitions exist (~9300; probe 9000),
    batches 24 on-policy + 8 retained (25%), re-encoded at replay.
  * SHUF twin: retained babbling actions relabelled by a FIXED class permutation
    (plan Decision log 14:19Z item 3), everything else identical.
Gates (plan sec 3 W3): (a) disc4_h1 >= 0.47 and k == 10; (b) retention (post-B0)/(pre-B0)
>= 0.5 with B0 from the probe's own results (valid only if this run's INIT disc equals the
probe's INIT disc exactly -- same encoder, same test set); (c) SHUF does not reach (a);
(d) guard PASS; (e) rollout t30 bounded, no x1.2/step growth. ASCII output.
"""
from __future__ import annotations

import argparse, copy, json, sys, time
from pathlib import Path

import numpy as np
import torch

p = argparse.ArgumentParser()
p.add_argument("--seed", type=int, required=True)
p.add_argument("--wt", required=True)
p.add_argument("--arm", choices=["real", "shuf"], required=True)
p.add_argument("--out", required=True)
p.add_argument("--post", type=int, default=1200)
p.add_argument("--ups", type=int, default=8)
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
PERM = [1, 2, 3, 4, 0]


def log(m):
    print("[w3 s%d %s t=%4.0fs] %s" % (S, a.arm, time.time() - t0, m), flush=True)


assert WT.E2WorldMember.__module__ == "ree_core.utils.waking_trainer"
assert str(Path(WT.__file__).resolve()).startswith(str(Path(a.wt).resolve())), WT.__file__
pub = json.load(open(PROBES / "babble" / "results" / ("BAB_s%d.json" % S)))
R.seed_all(S)
_e, ref, _c = R.build_B(S, False)
ref.eval()
ref_enc = copy.deepcopy(ref.latent_stack.state_dict())
init = BP.get_head(ref)
te_segs, _ = BB.gen_policy(S, 3000 // BB.EP_STEPS, 120, BB.pol_uniform(S * 7 + 3))
TE = BB.encode_segs(ref, te_segs)
ev_init = BB.evaluate(ref, init, TE, "z", S)
init_ok = abs(ev_init["disc4_h1"] - pub["open_loop"]["INIT|z"]["eval"]["disc4_h1"]) < 1e-12 and \
    ev_init["k"] == pub["open_loop"]["INIT|z"]["eval"]["k"]
B0 = pub["open_loop"]["B0|z"]["eval"]["disc4_h1"]
log("INIT disc4 %.4f (published %.4f) init_match=%s B0(pub)=%.4f" % (
    ev_init["disc4_h1"], pub["open_loop"]["INIT|z"]["eval"]["disc4_h1"], init_ok, B0))

# member agent: fresh build (same encoder), trainer with ONLY the E2-world member
agent = BB.fresh_agent(S, ref_enc)
cfg = agent.config
cfg.waking_trainer_guard_min_steps = 8
member = WT.E2WorldMember(agent, lr=3e-4, batch_size=32, buffer_max=2000, retained_max=5000,
                          replay_frac=0.25, reencode_window=0, replay_latent="reencode",
                          objective="mse", grad_clip=1.0, updates_per_step=1)
tr = WT.WakingTrainer(agent, cfg, members=[member])
agent.waking_trainer = tr
log("member W=%d alpha_world=%.2f" % (member.reencode_window, cfg.latent.alpha_world))

# babbling epoch (sense + member only; updates deferred to match the probe's pre phase)
bab = StructuredBabbler(n_classes=5, max_run=4, seed=S * 13 + 1)
tr.set_e2_world_source("babble")
tr.every_k = 10 ** 9
counts = [0] * 5
with torch.no_grad():
    for k in range(12):   # the probe's gen_policy: 12 episodes x 200 steps, env reset on done
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
    # (the unsensed final obs of each 200-step episode drops its last pair: ~2388 retained)
    
retained_n = len(member._retained)
if a.arm == "shuf":
    for r in member._retained:
        r["a"] = torch.nn.functional.one_hot(torch.tensor([PERM[int(r["a"].argmax())]]), 5).float()
log("babble done: retained %d classes %s" % (retained_n, counts))
snap = [(r["step"], r["a"].clone(), r["obs"][-1][1].clone()) for r in member._retained]
for _u in range(3000):
    tr._update("e2_world", member)
ev_pre = BB.evaluate(ref, BP.get_head(agent), TE, "z", S)
log("pre disc4 %.4f k %d" % (ev_pre["disc4_h1"], ev_pre["k"]))

# post phase: native closed loop, member on-policy + 25% retained replay
tr.set_e2_world_source("on_policy")
tr.every_k = 1
member.updates_per_step = a.ups
agent.reset()
R.seed_all(S + 500)
rew, acts_all, commits = [], [], []
for ep in range(a.post // BB.EP_STEPS):
    env = BB.make_env(S, 50 + ep)
    hh = StepHarness(agent, env, train_mode=False, seed=S * 1000 + 50 + ep)
    _f, od = env.reset(); agent.reset(); hh.reset()
    for _s in range(BB.EP_STEPS):
        r = hh.step(od)
        rew.append(float(r.harm_signal)); acts_all.append(int(r.action.detach().reshape(-1).argmax()))
        commits.append(getattr(agent.e3, "_committed_trajectory", None) is not None)
        od = r.next_obs_dict
        if r.done:
            _f, od = env.reset(); agent.reset(); hh.reset()
head_post = BP.get_head(agent)
ev_post = BB.evaluate(ref, head_post, TE, "z", S)
frozen_ok = len(snap) == len(member._retained) and all(
    s == r["step"] and torch.equal(aa, r["a"]) and torch.equal(o, r["obs"][-1][1])
    for (s, aa, o), r in zip(snap, member._retained))

# (e) rollout norm growth from test starts, 30 random actions
BP.set_head(ref, head_post)
g = np.random.default_rng(S + 31)
ratios_t30, late_growth = [], []
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
res = {
    "seed": S, "arm": a.arm, "hazard_class": pub.get("hazard_class"),
    "init": ev_init, "init_match_published": init_ok, "B0_published": B0,
    "pre": ev_pre, "post": ev_post,
    "retention": ((ev_post["disc4_h1"] - B0) / (ev_pre["disc4_h1"] - B0)
                  if init_ok and ev_pre["disc4_h1"] != B0 else None),
    "gate_a": bool(ev_post["disc4_h1"] >= 0.47 and ev_post["k"] == 10),
    "guard": {k: v.status for k, v in tr.guard_results.items()},
    "frozen_retained_unchanged_after_post": frozen_ok,
    "retained_n": retained_n, "retained_dropped": member.retained_dropped,
    "babble_class_counts": counts, "onpol_n": len(member._on_policy),
    "updates": dict(tr.steps), "drawn_retained": member.n_drawn_retained,
    "drawn_on_policy": member.n_drawn_on_policy,
    "n_reencoded": member.n_reencoded, "n_cache_hits": member.n_cache_hits,
    "reencode_window": member.reencode_window,
    "rollout_t30_over_t0_median": float(np.median(ratios_t30)),
    "rollout_late_step_growth_median": float(np.median(late_growth)),
    "rollout_late_step_growth_max": float(np.max(late_growth)),
    "post_reward_per_100": float(np.sum(rew) * 100.0 / len(rew)),
    "post_action_counts": {str(c): acts_all.count(c) for c in range(5)},
    "e3_running_variance_end": float(getattr(agent.e3, "_running_variance", float("nan"))),
    "commit_rate": float(np.mean(commits)),
    "t_total_s": time.time() - t0,
}
json.dump(res, open(a.out, "w"), indent=1, default=str)
log("RESULT post disc4 %.4f disc5 %.4f k %d gate_a %s ret %s guard %s frozen_ok %s t30/t0 %.2f late %.3f commit %.2f rv %.4g" % (
    ev_post["disc4_h1"], ev_post["disc5_h1"], ev_post["k"], res["gate_a"],
    None if res["retention"] is None else round(res["retention"], 3), res["guard"], frozen_ok,
    res["rollout_t30_over_t0_median"], res["rollout_late_step_growth_median"], res["commit_rate"],
    res["e3_running_variance_end"]))
