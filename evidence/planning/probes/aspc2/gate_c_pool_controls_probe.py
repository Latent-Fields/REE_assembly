"""Gate (c) pool-controls probe (bt0925-aspc2, orchestrate-20260924-breakthrough-c2,
chip_ref chip-20260925-gate-c-pool-controls).

Diagnostic: is the gate-(c) per-step growth failure found in
asp_gate_c_readout_20260925.md (cbf0f87173) a property of the W3 head's rollout
at H=30 (ANY pool of candidate action sequences), or specific to the ASP/codec
proposal mechanisms? Reads gate (c) EXACTLY as that record did (same statistic,
same bound, same held-out-state protocol, same training recipe, H=30), on FOUR
pools sharing the SAME trained world head and the SAME held-out states:

  (1) native codec pool, W1 codec parts ON: waking_trainer_codec_enabled (a
      CodecMember trained jointly with the world head) + use_codec_bounded_decode
      + use_codec_iter0_image_match. use_action_space_proposals stays False (the
      codec IS the native/default proposer's decode path once trained).
  (2) native default pool: ASP off, codec knobs off, codec weights left UNTRAINED
      (today's actual deployed default -- nothing in this campaign has landed on
      by default yet).
  (3) control: K=num_candidates random one-hot action sequences, uniform class
      PER STEP (independent draws), rolled out directly through
      e2.rollout_with_world -- bypasses propose_trajectories/CEM/codec entirely.
  (4) control: K constant-action sequences, one per class, cycled to fill K --
      also a direct e2.rollout_with_world call, no proposer involved.

Because e2.rollout_with_world steps world_forward(z_world, action) on the RAW
one-hot action (rollout_with_world's compute_action_objects branch feeds
action_object() only for traj.action_objects, a side channel E3's cue-bias term
and the codec read -- it does not feed world_forward; w1_codec_build_20260925.md
sec 1 "the encoder does not feed E2's world prediction"), pools (3)/(4) need no
codec state at all: compute_action_objects=False.

Training recipe for the world head: probes/w3/w3_l2r_member_probe.py's exact
recipe, IDENTICAL to gate_c_probe.py (E2WorldMember, babble pre-phase + on-policy
post-phase). Training recipe for the codec: CodecMember (ree_core/utils/
waking_trainer_codec.py), registered on the SAME WakingTrainer alongside the
world member so both read the SAME agent/tick stream; codec.updates_per_step is
pinned to 0 so on_waking_step() never auto-trains it (only observe()/buffer-fill
happens automatically), then exactly 1000 manual tr._update("codec", codec)
calls after the babble pre-phase -- matching test_w1_codec.py's GB gate recipe
("1000 member updates" on recorded z_world). Additional babble-phase states are
fed to the codec buffer via CodecMember.add_states() (its own documented manual
path for drivers/contracts), since the pre-phase babble loop does not call
on_waking_step() (mirrors gate_c_probe.py, which reserves on_waking_step for the
post-phase only).

Held-out states, gate (c) computation, and the [0.5,2] / 1.05 bound: identical
to gate_c_probe.py / asp_gate_c_readout_20260925.md sec 2. Additionally computes,
per candidate in every pool, the two alternative readings the aspc record's sec 4
named but did not measure: a late-window (steps 21-30 of H=30) MEAN growth like
W3 gate (e), and a max-growth restricted to the first D in {1,3,5} steps.

REPORT ONLY: this script does not decide which reading is authoritative (U1 in
the aspc record) -- it prints the literal (all-step max) reading as the primary
gate-c pass/fail column, and the alternative readings alongside it, for every
pool.

ASCII-only output.
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F

p = argparse.ArgumentParser()
p.add_argument("--seed", type=int, required=True)
p.add_argument("--wt", required=True)
p.add_argument("--out", required=True)
p.add_argument("--n-states", type=int, default=20)
p.add_argument("--quick", action="store_true",
                help="shrink all update counts for a fast correctness smoke test")
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
from ree_core.utils.waking_trainer_codec import CodecMember  # noqa: E402
from ree_core.developmental.structured_babbling import StructuredBabbler  # noqa: E402

S = a.seed
t0 = time.time()

PRE_UPDATES = 30 if a.quick else 3000
CODEC_UPDATES = 20 if a.quick else 1000
N_BABBLE_EP = 2 if a.quick else 12
POST_STEPS = 200 if a.quick else 1200


def log(m):
    print("[aspc2 s%d t=%4.0fs] %s" % (S, time.time() - t0, m), flush=True)


assert WT.E2WorldMember.__module__ == "ree_core.utils.waking_trainer"
assert str(Path(WT.__file__).resolve()).startswith(str(Path(a.wt).resolve())), WT.__file__

R.seed_all(S)
_e, ref, _c = R.build_B(S, False)
ref.eval()
ref_enc = copy.deepcopy(ref.latent_stack.state_dict())
orig_codec = {
    "enc": copy.deepcopy(ref.e2.action_object_head.state_dict()),
    "dec": copy.deepcopy(ref.hippocampal.action_object_decoder.state_dict()),
}

# ------------------------------------------------- train world head + codec ----
agent = BB.fresh_agent(S, ref_enc)
cfg = agent.config
cfg.waking_trainer_guard_min_steps = 8
member = WT.E2WorldMember(
    agent, lr=3e-4, batch_size=32, buffer_max=2000, retained_max=5000,
    replay_frac=0.25, reencode_window=0, replay_latent="reencode",
    objective="mse", grad_clip=1.0, updates_per_step=1,
)
codec = CodecMember(agent, lr=1e-3, batch_size=16, buffer_max=2000, code_l2=1e-3)
codec.updates_per_step = 0  # manual-only: no auto-update inside on_waking_step
tr = WT.WakingTrainer(agent, cfg, members=[member, codec])
agent.waking_trainer = tr

bab = StructuredBabbler(n_classes=5, max_run=4, seed=S * 13 + 1)
tr.set_e2_world_source("babble")
tr.every_k = 10 ** 9
counts = [0] * 5
with torch.no_grad():
    for k in range(N_BABBLE_EP):
        env = BB.make_env(S, k)
        _f, od = env.reset(); agent.reset(); bab.reset()
        for _s in range(BB.EP_STEPS):
            lat = agent.sense(od["body_state"], od["world_state"], obs_harm=od.get("harm_obs"),
                               obs_harm_a=od.get("harm_obs_a"), obs_harm_history=od.get("harm_history"))
            codec.add_states([lat.z_world])
            act = bab.next_action()
            c = int(act.argmax()); counts[c] += 1
            agent.record_executed_action(act)
            _f, h, done, _i, od = env.step(c)
            tr.on_waking_step(float(h))
            if done:
                _f, od = env.reset(); agent.reset(); bab.reset()
retained_n = len(member._retained)
for _u in range(PRE_UPDATES):
    tr._update("e2_world", member)
for _u in range(CODEC_UPDATES):
    tr._update("codec", codec)
log("pre-phase done: retained %d classes %s, codec buf %d, codec updates %d"
    % (retained_n, counts, len(codec._buf), CODEC_UPDATES))

tr.set_e2_world_source("on_policy")
tr.every_k = 1
member.updates_per_step = 8
agent.reset()
R.seed_all(S + 500)
for ep in range(POST_STEPS // BB.EP_STEPS):
    env = BB.make_env(S, 50 + ep)
    hh = StepHarness(agent, env, train_mode=False, seed=S * 1000 + 50 + ep)
    _f, od = env.reset(); agent.reset(); hh.reset()
    for _s in range(BB.EP_STEPS):
        r = hh.step(od)
        od = r.next_obs_dict
        if r.done:
            _f, od = env.reset(); agent.reset(); hh.reset()
head_post = BP.get_head(agent)
codec_post = {
    "enc": copy.deepcopy(agent.e2.action_object_head.state_dict()),
    "dec": copy.deepcopy(agent.hippocampal.action_object_decoder.state_dict()),
}
log("post-phase done (%d steps, 8 upd/step world; codec frozen after pre-phase)" % POST_STEPS)

# ---------------------------------------------------------------- load head ----
BP.set_head(ref, head_post)
Hh = int(ref.hippocampal.config.horizon)
K = int(ref.hippocampal.config.num_candidates)
WD = int(ref.hippocampal.config.world_dim)
A = int(ref.hippocampal.config.action_dim)
I = int(ref.hippocampal.config.num_cem_iterations)
log("ref.hippocampal deployed dims: H=%d K=%d WD=%d A=%d I=%d" % (Hh, K, WD, A, I))

# ------------------------------------------------------- held-out states ----
ref.eval()
te_segs, _ = BB.gen_policy(S, a.n_states, 300, BB.pol_uniform(S * 11 + 17))
g = np.random.default_rng(S * 97 + 5)
states = []
for seg in te_segs:
    if len(seg["a"]) < 1:
        continue
    ref.reset()
    t_pick = int(g.integers(0, len(seg["obs"])))
    lat = None
    with torch.no_grad():
        for ti, o in enumerate(seg["obs"]):
            lat = ref.sense(o["body_state"], o["world_state"], obs_harm=o.get("harm_obs"),
                             obs_harm_a=o.get("harm_obs_a"), obs_harm_history=o.get("harm_history"))
            if ti == t_pick:
                states.append((lat.z_world.detach().clone(), lat.z_self.detach().clone()))
                break
log("collected %d held-out (z_world, z_self) states (k0=300, disjoint from training k-ranges)"
    % len(states))


# ------------------------------------------------------------- growth stats ----
def growth_stats(norms_1d):
    """norms_1d: 1D array length H+1 (t=0..H). Returns per-candidate stat dict."""
    v = np.asarray(norms_1d, dtype=float)
    n0 = float(v[0])
    ratio = float(v[-1] / n0) if n0 > 0 else None
    g = v[1:] / np.clip(v[:-1], 1e-12, None)
    Hn = len(g)
    out = {"ratio": ratio, "max_growth_all": float(g.max()) if Hn else None}
    if Hn >= 30:
        late = g[20:30]
    else:
        late = g[max(0, Hn - 10):Hn]
    out["late_window_mean_growth"] = float(late.mean()) if len(late) else None
    for D in (1, 3, 5):
        d = min(D, Hn)
        out["first%d_max_growth" % D] = float(g[:d].max()) if d > 0 else None
    return out


def pool_and_gate(per_cand):
    ratios = [c["ratio"] for c in per_cand if c["ratio"] is not None]
    out = {"n_candidates_pooled": len(per_cand)}
    out["pooled_ratio_median"] = float(np.median(ratios)) if ratios else None
    out["gate_ratio_ok"] = (out["pooled_ratio_median"] is not None
                             and 0.5 <= out["pooled_ratio_median"] <= 2.0)
    for key in ("max_growth_all", "first1_max_growth", "first3_max_growth", "first5_max_growth"):
        vals = [c[key] for c in per_cand if c.get(key) is not None]
        out["pooled_max_%s" % key] = float(np.max(vals)) if vals else None
    lw = [c["late_window_mean_growth"] for c in per_cand if c.get("late_window_mean_growth") is not None]
    out["pooled_median_late_window_mean_growth"] = float(np.median(lw)) if lw else None
    out["pooled_max_late_window_mean_growth"] = float(np.max(lw)) if lw else None
    out["gate_growth_ok_literal"] = (out["pooled_max_max_growth_all"] is not None
                                      and out["pooled_max_max_growth_all"] <= 1.05)
    out["gate_c_pass_literal"] = bool(out["gate_ratio_ok"] and out["gate_growth_ok_literal"])
    return out


results = {}

# ---- Pool 2: native default (ASP off, codec knobs off, codec UNTRAINED) ------
ref.hippocampal.config.use_action_space_proposals = False
ref.hippocampal.config.use_codec_bounded_decode = False
ref.hippocampal.config.use_codec_iter0_image_match = False
ref.e2.action_object_head.load_state_dict(orig_codec["enc"])
ref.hippocampal.action_object_decoder.load_state_dict(orig_codec["dec"])
per_cand = []
for si, (zw, zs) in enumerate(states):
    torch.manual_seed(S * 30000 + si * 13 + 1)
    with torch.no_grad():
        pool = ref.hippocampal.propose_trajectories(zw, z_self=zs)
    for tr_ in pool:
        seq = tr_.get_world_state_sequence()
        if seq is None:
            continue
        norms = seq.detach().norm(dim=-1).mean(dim=0).numpy()
        per_cand.append(growth_stats(norms))
results["native_default"] = pool_and_gate(per_cand)
results["native_default"]["n_states"] = len(states)
log("native_default: ratio_med=%.4f max_growth=%.4f pass=%s (n_cand=%d)" % (
    results["native_default"]["pooled_ratio_median"] or -1.0,
    results["native_default"]["pooled_max_max_growth_all"] or -1.0,
    results["native_default"]["gate_c_pass_literal"], results["native_default"]["n_candidates_pooled"]))

# ---- Pool 1: native codec, W1 parts ON, codec TRAINED -------------------------
ref.hippocampal.config.use_action_space_proposals = False
ref.hippocampal.config.use_codec_bounded_decode = True
ref.hippocampal.config.use_codec_iter0_image_match = True
ref.e2.action_object_head.load_state_dict(codec_post["enc"])
ref.hippocampal.action_object_decoder.load_state_dict(codec_post["dec"])
per_cand = []
for si, (zw, zs) in enumerate(states):
    torch.manual_seed(S * 30000 + si * 13 + 2)
    with torch.no_grad():
        pool = ref.hippocampal.propose_trajectories(zw, z_self=zs)
    for tr_ in pool:
        seq = tr_.get_world_state_sequence()
        if seq is None:
            continue
        norms = seq.detach().norm(dim=-1).mean(dim=0).numpy()
        per_cand.append(growth_stats(norms))
results["native_codec_w1_on"] = pool_and_gate(per_cand)
results["native_codec_w1_on"]["n_states"] = len(states)
log("native_codec_w1_on: ratio_med=%.4f max_growth=%.4f pass=%s (n_cand=%d)" % (
    results["native_codec_w1_on"]["pooled_ratio_median"] or -1.0,
    results["native_codec_w1_on"]["pooled_max_max_growth_all"] or -1.0,
    results["native_codec_w1_on"]["gate_c_pass_literal"], results["native_codec_w1_on"]["n_candidates_pooled"]))

# reset knobs to OFF (hygiene; controls below bypass hippocampal entirely anyway)
ref.hippocampal.config.use_codec_bounded_decode = False
ref.hippocampal.config.use_codec_iter0_image_match = False

# ---- Pool 3: control, K random one-hot sequences, uniform class PER STEP -----
per_cand = []
for si, (zw, zs) in enumerate(states):
    torch.manual_seed(S * 30000 + si * 13 + 3)
    idx = torch.randint(0, A, (K, Hh))
    act_seq = F.one_hot(idx, num_classes=A).float()
    zw_b = zw.repeat(K, 1)
    zs_b = zs.repeat(K, 1)
    with torch.no_grad():
        traj = ref.e2.rollout_with_world(zs_b, zw_b, act_seq, compute_action_objects=False)
    seq = traj.get_world_state_sequence()
    norms_all = seq.detach().norm(dim=-1).numpy()
    for k in range(K):
        per_cand.append(growth_stats(norms_all[k]))
results["control_random_per_step"] = pool_and_gate(per_cand)
results["control_random_per_step"]["n_states"] = len(states)
log("control_random_per_step: ratio_med=%.4f max_growth=%.4f pass=%s (n_cand=%d)" % (
    results["control_random_per_step"]["pooled_ratio_median"] or -1.0,
    results["control_random_per_step"]["pooled_max_max_growth_all"] or -1.0,
    results["control_random_per_step"]["gate_c_pass_literal"],
    results["control_random_per_step"]["n_candidates_pooled"]))

# ---- Pool 4: control, K constant-action sequences, one per class, cycled ----
per_cand = []
classes = torch.tensor([i % A for i in range(K)])
idx_const = classes.unsqueeze(1).expand(K, Hh)
act_seq_const = F.one_hot(idx_const, num_classes=A).float()
for si, (zw, zs) in enumerate(states):
    torch.manual_seed(S * 30000 + si * 13 + 4)  # no randomness used; kept for parity
    zw_b = zw.repeat(K, 1)
    zs_b = zs.repeat(K, 1)
    with torch.no_grad():
        traj = ref.e2.rollout_with_world(zs_b, zw_b, act_seq_const, compute_action_objects=False)
    seq = traj.get_world_state_sequence()
    norms_all = seq.detach().norm(dim=-1).numpy()
    for k in range(K):
        per_cand.append(growth_stats(norms_all[k]))
results["control_constant_per_class"] = pool_and_gate(per_cand)
results["control_constant_per_class"]["n_states"] = len(states)
log("control_constant_per_class: ratio_med=%.4f max_growth=%.4f pass=%s (n_cand=%d)" % (
    results["control_constant_per_class"]["pooled_ratio_median"] or -1.0,
    results["control_constant_per_class"]["pooled_max_max_growth_all"] or -1.0,
    results["control_constant_per_class"]["gate_c_pass_literal"],
    results["control_constant_per_class"]["n_candidates_pooled"]))

out = {
    "seed": S, "horizon": Hh, "num_candidates": K, "world_dim": WD, "action_dim": A,
    "num_cem_iterations": I, "n_states": a.n_states, "retained_n": retained_n,
    "quick": bool(a.quick), "pre_updates": PRE_UPDATES, "codec_updates": CODEC_UPDATES,
    "results": results, "t_total_s": time.time() - t0,
}
json.dump(out, open(a.out, "w"), indent=1, default=str)
log("DONE -> %s" % a.out)
