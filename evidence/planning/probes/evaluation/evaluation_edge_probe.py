"""Worker F probe: is EVALUATION the next broken edge? (probe-only, nothing lands in ree_core)

bt0924-evaluation (Worker F, orchestrate-20260924-breakthrough), follow-on to Worker D ADDENDUM 3.
Reuses ADDENDUM 3's harness verbatim (partitioned_repair_probe.py: encoder P0, own-replay head A,
COV head D, probe_states, choice_quality) and adds trained E3 evaluators.

EVALUATORS (agent's own experience only; labels = the env reward stream the agent receives,
StepResult.harm_signal / env.step's harm return: <0 harm, >0 benefit; no env internals):
  harm_eval_head    BCE, V3-EXQ-1061's recipe (v3_exq_1061_...py:520-575): class-balanced
                    batches k=min(16,npos,nneg) per class, Adam lr 1e-3, clip 1.0, min 8 per class.
  benefit_eval_head the same recipe on benefit labels (analogue; no landed driver trains it on
                    the reward stream -- V3-EXQ-183 uses privileged env distance, not used here).
  Label state = the ENCODED ARRIVAL state z_{t+1} of the labelled transition (what E3 scores:
  world_states[1] under the depth-2 limit). DEVIATION from 1061, which labels the pre-step state.
  Data = two own-experience runs through the agent's SD-070 encoder: a native waking run (head A,
  E3 selecting) and a uniform-random-action run (the COV head's kind of data), pooled.
  E4 SHUFFLED: the same z's, harm and benefit labels independently permuted across timesteps.
  Benefit channel: E3Config.benefit_eval_enabled=True, benefit_weight=1.0 (default), warmup gate
  _benefit_samples_seen := number of positive benefit samples in the training buffer (the
  docstring's semantic, e3_selector.py:1209-1216); if < 50 the native gate stays SHUT and the
  arm is reported both ways (--force-gate opens it, labelled).
ARMS (600 closed-loop steps, fresh agent per arm from the same seed, as ADDENDUM 3):
  E0 NATIVE (head A, no R5/R2, untrained evaluators)  -- canary vs PART_s*.json NATIVE
  E1 FULL (R5b + COV + R2, untrained evaluators)      -- canary vs PART_s*.json FULL
  E2 FULL+EVAL   E3 EVAL-only (NATIVE + trained evaluators)   E4 FULL+SHUF
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
import torch
import torch.nn.functional as F

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "ree-v3-wt"))
sys.path.insert(0, str(HERE / "ree-v3-wt" / "experiments"))
sys.path.insert(0, str(HERE))

from experiments._harness import StepHarness  # noqa: E402
import rollout_fidelity_probe as R  # noqa: E402
import encoding_vs_objective_probe as E  # noqa: E402
import balanced_replay_probe as BP  # noqa: E402
import partitioned_repair_probe as PR  # noqa: E402

torch.set_num_threads(2)
DEPTH = PR.DEPTH
CONTACT = {"agent_caused_hazard", "env_caused_hazard", "env_caused_multisource"}
BCONTACT = {"resource", "resource_contact", "sequence_complete", "waypoint"}
COMM = False  # ADDENDUM 2 factor: E3Config.use_e3_channel_commensurability (set per arm, as its docs say)


def eval_heads(agent):
    return {"h": copy.deepcopy(agent.e3.harm_eval_head.state_dict()),
            "b": copy.deepcopy(agent.e3.benefit_eval_head.state_dict())}


def set_eval(agent, ev):
    agent.e3.harm_eval_head.load_state_dict(ev["h"])
    agent.e3.benefit_eval_head.load_state_dict(ev["b"])


def exposure(obs):
    """benefit_exposure exactly as the harness derives it (_harness.py:248-256)."""
    v = obs.get("benefit_exposure", None)
    if v is None:
        b = torch.as_tensor(obs["body_state"]).reshape(-1)
        v = b[11] if b.shape[0] > 11 else None
    return 0.0 if v is None else max(0.0, float(v))


def collect_native(agent, env, steps, seed):
    """Native waking run; returns list of (z_post[1,D], reward, ttype)."""
    h = StepHarness(agent, env, train_mode=False, seed=seed)
    _f, obs = env.reset(); agent.reset(); h.reset()
    out = []
    for _ in range(steps):
        r = h.step(obs)
        with torch.no_grad():
            zp = BP.encode_next(agent, r.next_obs_dict, r.latent, r.action.detach().reshape(1, -1).float())
        tt = r.info.get("transition_type", "none") if isinstance(r.info, dict) else "none"
        out.append((zp, float(r.harm_signal), tt, exposure(r.next_obs_dict)))
        obs = r.next_obs_dict
        if r.done:
            _f, obs = env.reset(); agent.reset(); h.reset()
    return out


@torch.no_grad()
def collect_random(agent, env, steps, seed):
    g = np.random.default_rng(seed)
    A = env.action_dim
    out = []
    _f, obs = env.reset(); agent.reset()
    for _ in range(steps):
        lat = agent.sense(obs["body_state"], obs["world_state"], obs_harm=obs.get("harm_obs"),
                          obs_harm_a=obs.get("harm_obs_a"), obs_harm_history=obs.get("harm_history"))
        a = int(g.integers(0, A))
        _f, hsig, done, info, obs = env.step(a)
        zp = BP.encode_next(agent, obs, lat, BP.onehot(a, A))
        tt = info.get("transition_type", "none") if isinstance(info, dict) else "none"
        out.append((zp, float(hsig), tt, exposure(obs)))
        if done:
            _f, obs = env.reset(); agent.reset()
    return out


def auc(scores, labels):
    s = np.asarray(scores, float); y = np.asarray(labels, bool)
    if y.sum() == 0 or (~y).sum() == 0:
        return None
    order = np.argsort(s); ranks = np.empty(len(s)); ranks[order] = np.arange(1, len(s) + 1)
    return float((ranks[y].sum() - y.sum() * (y.sum() + 1) / 2) / (y.sum() * (~y).sum()))


def train_bce(head, Z, y, steps, seed):
    """V3-EXQ-1061 recipe, offline: balanced k=min(16,npos,nneg) per class, Adam 1e-3, clip 1.0."""
    pos = np.nonzero(y)[0]; neg = np.nonzero(~y)[0]
    if len(pos) < 8 or len(neg) < 8:
        return {"trained": False, "npos": int(len(pos)), "nneg": int(len(neg))}
    g = torch.Generator().manual_seed(seed)
    opt = torch.optim.Adam(head.parameters(), lr=1e-3)
    k = min(16, len(pos), len(neg)); losses = []
    pos_t = torch.as_tensor(pos); neg_t = torch.as_tensor(neg)
    for _ in range(steps):
        pi = pos_t[torch.randperm(len(pos), generator=g)[:k]]; ni = neg_t[torch.randperm(len(neg), generator=g)[:k]]
        zb = torch.cat([Z[pi], Z[ni]]); lb = torch.cat([torch.ones(k, 1), torch.zeros(k, 1)])
        loss = F.binary_cross_entropy(head(zb), lb)
        opt.zero_grad(); loss.backward(); torch.nn.utils.clip_grad_norm_(head.parameters(), 1.0); opt.step()
        losses.append(float(loss.detach()))
    return {"trained": True, "npos": int(len(pos)), "nneg": int(len(neg)), "k": k, "steps": steps,
            "loss_last100": float(np.mean(losses[-100:]))}


def train_mse(head, Z, y, steps, seed):
    """Native benefit recipe (agent.py:11701 compute_benefit_eval_loss: MSE of benefit_eval(z_world)
    on benefit_exposure; driver cadence e.g. v3_exq_074c:258-265), offline: batch 32, Adam 1e-3, clip 1.0."""
    g = torch.Generator().manual_seed(seed)
    opt = torch.optim.Adam(head.parameters(), lr=1e-3)
    yt = torch.as_tensor(y, dtype=torch.float32).reshape(-1, 1); losses = []
    for _ in range(steps):
        idx = torch.randint(0, len(yt), (32,), generator=g)
        loss = F.mse_loss(head(Z[idx]), yt[idx])
        opt.zero_grad(); loss.backward(); torch.nn.utils.clip_grad_norm_(head.parameters(), 1.0); opt.step()
        losses.append(float(loss.detach()))
    return {"trained": True, "n": int(len(yt)), "n_exposure_pos": int((yt > 0).sum()), "steps": steps,
            "loss_last100": float(np.mean(losses[-100:])), "target_var": float(yt.var())}


def train_evaluators_native_b(agent, ev_harm, data, steps, seed, shuffle):
    """Harm head taken from ev_harm (the contact-BCE one); benefit head by the native MSE recipe."""
    Z = torch.cat([d[0] for d in data]).detach()
    ex = np.asarray([d[3] for d in data]); rw = np.asarray([d[1] for d in data])
    g = np.random.default_rng(seed + 991)
    n = len(ex); tr = np.zeros(n, bool); tr[g.permutation(n)[: int(0.8 * n)]] = True
    y = ex.copy()
    if shuffle:
        idx = np.nonzero(tr)[0]; y[idx] = ex[idx][g.permutation(len(idx))]
    set_eval(agent, ev_harm)
    init_b = copy.deepcopy(agent.e3.benefit_eval_head.state_dict())
    ib = train_mse(agent.e3.benefit_eval_head, Z[torch.as_tensor(np.nonzero(tr)[0])], y[tr], steps, seed + 2)
    te = torch.as_tensor(np.nonzero(~tr)[0])
    with torch.no_grad():
        pb = agent.e3.benefit_eval_head(Z[te]).reshape(-1).numpy()
    ib["heldout_corr_exposure"] = float(np.corrcoef(pb, ex[~tr])[0, 1]) if ex[~tr].std() > 0 else None
    ib["heldout_auc_benefit_contact"] = auc(pb, rw[~tr] > 0)
    ev = eval_heads(agent)
    agent.e3.benefit_eval_head.load_state_dict(init_b)
    return ev, ib


def train_evaluators(agent, init_ev, data, steps, seed, shuffle):
    Z = torch.cat([d[0] for d in data]).detach()
    rw = np.asarray([d[1] for d in data])
    yh = rw < 0; yb = rw > 0
    g = np.random.default_rng(seed + 777)
    n = len(rw); tr = np.zeros(n, bool); tr[g.permutation(n)[: int(0.8 * n)]] = True
    if shuffle:
        yh_tr = yh.copy(); yb_tr = yb.copy()
        idx = np.nonzero(tr)[0]
        yh_tr[idx] = yh[idx][g.permutation(len(idx))]; yb_tr[idx] = yb[idx][g.permutation(len(idx))]
    else:
        yh_tr, yb_tr = yh, yb
    set_eval(agent, init_ev)
    Ztr = Z[torch.as_tensor(np.nonzero(tr)[0])]
    ih = train_bce(agent.e3.harm_eval_head, Ztr, yh_tr[tr], steps, seed)
    ib = train_bce(agent.e3.benefit_eval_head, Ztr, yb_tr[tr], steps, seed + 1)
    te = torch.as_tensor(np.nonzero(~tr)[0])
    with torch.no_grad():
        ph = agent.e3.harm_eval_head(Z[te]).reshape(-1).numpy(); pb = agent.e3.benefit_eval_head(Z[te]).reshape(-1).numpy()
    ih["heldout_auc"] = auc(ph, yh[~tr]); ib["heldout_auc"] = auc(pb, yb[~tr])
    ih["heldout_npos"] = int(yh[~tr].sum()); ib["heldout_npos"] = int(yb[~tr].sum())
    ih["out_mean_pos_neg"] = [float(ph[yh[~tr]].mean()) if yh[~tr].any() else None, float(ph[~yh[~tr]].mean())]
    ib["out_mean_pos_neg"] = [float(pb[yb[~tr]].mean()) if yb[~tr].any() else None, float(pb[~yb[~tr]].mean())]
    return eval_heads(agent), {"harm": ih, "benefit": ib, "n_benefit_pos_train": int(yb_tr[tr].sum())}


@torch.no_grad()
def term_spread(agent, states, A, depth):
    """Per probe state: the 5 one-class scaffold candidates (as choice_quality), each J term's
    cross-candidate std (weighted as in score_trajectory), and whether dropping the evaluator
    terms (harm + benefit) changes E3's argmin."""
    e3 = agent.e3; prev = e3._score_depth_limit; e3._score_depth_limit = depth
    sd = {"F": [], "harm": [], "residue": [], "benefit": [], "J": []}; flips = []
    sdn = {"F": [], "harm": [], "residue": [], "benefit": []}
    on = bool(getattr(e3.config, "use_e3_channel_commensurability", False))
    sc = {k: (e3._commensurability_scale(n) if on else 1.0) for k, n in
          (("F", "f_weighted"), ("harm", "harm_weighted"), ("residue", "residue_weighted"), ("benefit", "benefit_weighted"))}
    try:
        for st in states:
            trajs = []
            for c in range(A):
                a = st["base"].clone(); a[:, 0, :] = 0.0; a[:, 0, c] = 1.0
                trajs.append(agent.e2.rollout_with_world(st["s0"], st["z0"], a, compute_action_objects=False))
            f = np.asarray([float(e3.config.f_weight * e3.compute_reality_cost(t).mean()) for t in trajs])
            m = np.asarray([float(e3.config.lambda_ethical * e3.compute_harm_cost_fallback(t).mean()) for t in trajs])
            ph = np.asarray([float(e3.config.rho_residue * e3.compute_residue_cost(t).mean()) for t in trajs])
            bon = (e3.config.benefit_eval_enabled and e3._benefit_samples_seen >= e3._BENEFIT_WARMUP_SAMPLES)
            b = np.asarray([float(e3.config.benefit_weight * e3.compute_benefit_score(t).mean()) for t in trajs]) if bon else np.zeros(A)
            j = np.asarray([float(e3.score_trajectory(t).mean()) for t in trajs])
            for k, v in (("F", f), ("harm", m), ("residue", ph), ("benefit", b), ("J", j)):
                sd[k].append(float(v.std()))
            for k, v in (("F", f), ("harm", m), ("residue", ph), ("benefit", b)):
                sdn[k].append(float(v.std() / sc[k]))
            flips.append(int(np.argmin(j) != np.argmin(j - m / sc["harm"] + b / sc["benefit"])))
    finally:
        e3._score_depth_limit = prev
    return {"xcand_std_mean": {k: float(np.mean(v)) for k, v in sd.items()},
            "xcand_std_normalised_mean": {k: float(np.mean(v)) for k, v in sdn.items()},
            "scales_used": sc, "commensurability_on": on,
            "drop_eval_flip_rate": float(np.mean(flips)) if flips else None}


def configure_eval(agent, ev, benefit_on, gate_n):
    if ev is not None:
        set_eval(agent, ev)
    agent.e3.config.benefit_eval_enabled = bool(benefit_on)
    agent.e3._benefit_samples_seen = int(gate_n) if benefit_on else 0


def closed_loop(seed, enc_state, head, r5, r2, ev, benefit_on, gate_n, steps):
    R.seed_all(seed)
    env, agent, cfg = R.build_B(seed, False)
    agent.latent_stack.load_state_dict(enc_state)
    BP.set_head(agent, head)
    agent.hippocampal.config.use_action_class_scaffold_candidates = bool(r5)
    agent.e3._score_depth_limit = DEPTH if r2 else None
    configure_eval(agent, ev, benefit_on, gate_n)
    agent.e3.config.use_e3_channel_commensurability = bool(COMM)
    agent.eval()
    calls = Counter()
    e3 = agent.e3
    oh, ob = e3.compute_harm_cost_fallback, e3.compute_benefit_score

    def wh(t):
        calls["harm_fallback"] += 1; return oh(t)

    def wb(t):
        calls["benefit"] += 1; return ob(t)
    e3.compute_harm_cost_fallback = wh; e3.compute_benefit_score = wb
    h = StepHarness(agent, env, train_mode=False, seed=seed)
    _f, obs = env.reset(); agent.reset(); h.reset()
    rew, acts, tts, ep = [], [], Counter(), 0
    for _ in range(steps):
        r = h.step(obs)
        rew.append(float(r.harm_signal)); acts.append(int(r.action.detach().reshape(-1).argmax()))
        tts[r.info.get("transition_type", "none") if isinstance(r.info, dict) else "none"] += 1
        obs = r.next_obs_dict
        if r.done:
            _f, obs = env.reset(); agent.reset(); h.reset(); ep += 1
    assert agent.e3._score_depth_limit == (DEPTH if r2 else None)
    rew = np.asarray(rew); cc = Counter(acts); p = np.asarray(list(cc.values()), float) / len(acts)
    return {"steps": steps, "episodes_ended": ep, "reward_per_100": float(rew.sum() * 100 / steps),
            "harm_events_per_100": float((rew < 0).sum() * 100 / steps),
            "benefit_events_per_100": float((rew > 0).sum() * 100 / steps),
            "harm_sum_per_100": float(rew[rew < 0].sum() * 100 / steps),
            "benefit_sum_per_100": float(rew[rew > 0].sum() * 100 / steps),
            "harm_contacts": int(sum(v for k, v in tts.items() if k in CONTACT)),
            "hazard_approach": int(tts.get("hazard_approach", 0)), "benefit_approach": int(tts.get("benefit_approach", 0)),
            "benefit_contacts": int(sum(v for k, v in tts.items() if k in BCONTACT)),
            "transition_types": dict(tts), "action_counts": {str(k): v for k, v in sorted(cc.items())},
            "action_entropy": float(-(p * np.log(p)).sum()), "majority_share": max(cc.values()) / len(acts),
            "scorer_calls": dict(calls),
            "comm_state": {"on": bool(agent.e3.config.use_e3_channel_commensurability),
                           "ema": dict(agent.e3._chan_scale_ema), "n": int(agent.e3._chan_scale_n),
                           "last": dict(agent.e3.last_channel_scale_estimates)}, "benefit_gate_open": bool(benefit_on and gate_n >= e3._BENEFIT_WARMUP_SAMPLES)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--wake", type=int, default=600)
    ap.add_argument("--probe-steps", type=int, default=200)
    ap.add_argument("--label-steps", type=int, default=1500)
    ap.add_argument("--eval-steps", type=int, default=1500)
    ap.add_argument("--force-gate", type=int, default=1)
    ap.add_argument("--tiebreak", type=int, default=0)
    ap.add_argument("--comm", type=int, default=0)
    ap.add_argument("--arms", default="")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    t0 = time.time()
    if a.tiebreak:
        # ADDENDUM single factor: every env this probe builds goes through R.build_B ->
        # R.CausalGridWorldV2 (rollout_fidelity_probe.py:93), so patching that name covers
        # the encoder P0, replay, label runs, probe states and every closed-loop arm.
        import functools
        R.CausalGridWorldV2 = functools.partial(R.CausalGridWorldV2, proximity_approach_magnitude_tiebreak=True)
        _e = R.build_B(a.seed, False)[0]
        assert _e.proximity_approach_magnitude_tiebreak is True
    keep = set(x for x in a.arms.split(",") if x)
    global COMM
    COMM = bool(a.comm)
    # ---- ADDENDUM 3's exact preamble (same RNG order -> same encoder and heads) ----
    R.seed_all(a.seed)
    env, agent, cfg = R.build_B(a.seed, False)
    A = env.action_dim
    PR.p0(agent, a.seed)
    agent.eval()
    enc_state = copy.deepcopy(agent.latent_stack.state_dict())
    init = BP.get_head(agent)
    trans = BP.collect_replay(agent, env, 1500, a.seed)
    rnd = E.collect(R.build_B(a.seed + 11, False)[0], agent, len(trans) + 200, a.seed + 3)
    trans_d = []
    for e in rnd:
        for t in range(e["a"].shape[0] - 1):
            trans_d.append((e["z"][t:t + 1], int(e["a"][t]), e["z"][t + 1:t + 2]))
    trans_d = trans_d[:len(trans)]
    headA, infoA = BP.train_arm(agent, init, trans, A, np.ones(len(trans)), 3000, a.seed)
    headD, infoD = BP.train_arm(agent, init, trans_d, A, np.ones(len(trans_d)), 3000, a.seed)
    print("HEADS A=%s D=%s t=%.0fs" % (json.dumps(infoA), json.dumps(infoD), time.time() - t0), flush=True)
    init_ev = eval_heads(agent)
    # ---- labelled own experience ----
    BP.set_head(agent, headA)
    nat = collect_native(agent, R.build_B(a.seed + 21, False)[0], a.label_steps, a.seed + 21)
    ran = collect_random(agent, R.build_B(a.seed + 23, False)[0], a.label_steps, a.seed + 23)
    agent.reset()

    def cnt(d):
        rw = np.asarray([x[1] for x in d]); tt = Counter(x[2] for x in d)
        return {"n": len(d), "harm_neg_reward": int((rw < 0).sum()), "benefit_pos_reward": int((rw > 0).sum()),
                "harm_contacts": int(sum(v for k, v in tt.items() if k in CONTACT)),
                "benefit_contacts": int(sum(v for k, v in tt.items() if k in BCONTACT)),
                "benefit_approach": int(tt.get("benefit_approach", 0)), "hazard_approach": int(tt.get("hazard_approach", 0)),
                "transition_types": dict(tt)}
    counts = {"native": cnt(nat), "random": cnt(ran)}
    print("LABELS %s t=%.0fs" % (json.dumps(counts), time.time() - t0), flush=True)
    data = nat + ran
    evT, infoT = train_evaluators(agent, init_ev, data, a.eval_steps, a.seed, False)
    evS, infoS = train_evaluators(agent, init_ev, data, a.eval_steps, a.seed, True)
    evN, infoN = train_evaluators_native_b(agent, evT, data, a.eval_steps, a.seed, False)
    evNS, infoNS = train_evaluators_native_b(agent, evS, data, a.eval_steps, a.seed, True)
    gate_nat = infoN["n_exposure_pos"]
    print("NATB trained=%s shuffled=%s t=%.0fs" % (json.dumps(infoN), json.dumps(infoNS), time.time() - t0), flush=True)
    gate_n = infoT["n_benefit_pos_train"]
    native_gate_open = gate_n >= agent.e3._BENEFIT_WARMUP_SAMPLES
    gate_used = max(gate_n, agent.e3._BENEFIT_WARMUP_SAMPLES) if a.force_gate else gate_n
    print("EVAL trained=%s shuffled=%s native_gate_open=%s gate_used=%d t=%.0fs" % (
        json.dumps(infoT), json.dumps(infoS), native_gate_open, gate_used, time.time() - t0), flush=True)
    # ---- choice quality vs env-grounded Q (ADDENDUM 3 measure) ----
    set_eval(agent, init_ev); configure_eval(agent, None, False, 0)
    BP.set_head(agent, headA)
    states = PR.probe_states(agent, env, a.probe_steps, 5, A, a.seed, 6, 4)
    cq = {}
    for name, head, depth, ev, bon in (("E1_FULL", headD, DEPTH, init_ev, False),
                                       ("E2_FULL_EVAL", headD, DEPTH, evT, True),
                                       ("E3_EVAL_only", headA, None, evT, True),
                                       ("E4_FULL_SHUF", headD, DEPTH, evS, True),
                                       ("E0_NATIVE", headA, None, init_ev, False),
                                       ("E5_FULL_EVALnb", headD, DEPTH, evN, True),
                                       ("E6_FULL_SHUFnb", headD, DEPTH, evNS, True)):
        if keep and name not in keep:
            continue
        BP.set_head(agent, head); configure_eval(agent, ev, bon, gate_nat if name.endswith("nb") else gate_used)
        cq[name] = PR.choice_quality(agent, states, A, depth)
        cq[name]["terms"] = term_spread(agent, states, A, depth)
    configure_eval(agent, init_ev, False, 0)
    print("CHOICE %s t=%.0fs" % (json.dumps(cq), time.time() - t0), flush=True)
    out = {"args": vars(a), "heads": {"A": infoA, "D": infoD}, "label_counts": counts,
           "evaluators": {"trained": infoT, "shuffled": infoS}, "native_gate_open": native_gate_open,
           "gate_used": gate_used, "native_b": {"trained": infoN, "shuffled": infoNS, "gate": gate_nat}, "choice_quality": cq, "arms": {}}
    arms = {"E0_NATIVE": (headA, 0, 0, init_ev, False), "E1_FULL": (headD, 1, 1, init_ev, False),
            "E2_FULL_EVAL": (headD, 1, 1, evT, True), "E3_EVAL_only": (headA, 0, 0, evT, True),
            "E4_FULL_SHUF": (headD, 1, 1, evS, True),
            "E5_FULL_EVALnb": (headD, 1, 1, evN, True), "E6_FULL_SHUFnb": (headD, 1, 1, evNS, True)}
    for name, (head, r5, r2, ev, bon) in arms.items():
        if keep and name not in keep:
            continue
        res = closed_loop(a.seed, enc_state, head, r5, r2, ev, bon, gate_nat if name.endswith("nb") else gate_used, a.wake)
        res["choice_quality"] = cq[name]
        if COMM:
            # choice quality / term spread WITH the flag: the master agent's E3 gets this arm's
            # own running scale state (built over its 600 closed-loop ticks), then re-scores.
            cs = res["comm_state"]
            BP.set_head(agent, head); configure_eval(agent, ev, bon, gate_nat if name.endswith("nb") else gate_used)
            agent.e3.config.use_e3_channel_commensurability = True
            agent.e3._chan_scale_ema = dict(cs["ema"]); agent.e3._chan_scale_n = int(cs["n"])
            cqc = PR.choice_quality(agent, states, A, DEPTH if r2 else None)
            cqc["terms"] = term_spread(agent, states, A, DEPTH if r2 else None)
            res["choice_quality_comm"] = cqc
            agent.e3.config.use_e3_channel_commensurability = False
            agent.e3._chan_scale_ema = {}; agent.e3._chan_scale_n = 0
            configure_eval(agent, init_ev, False, 0)
        out["arms"][name] = res
        print("ARM %-13s %s t=%.0fs" % (name, json.dumps({k: v for k, v in res.items()
                                                          if k not in ("choice_quality", "transition_types")}),
                                        time.time() - t0), flush=True)
        json.dump(out, open(a.out, "w"), indent=1, default=str)
    out["t_total_s"] = round(time.time() - t0, 1)
    json.dump(out, open(a.out, "w"), indent=1, default=str)
    print("wrote %s t=%.0fs" % (a.out, time.time() - t0), flush=True)


if __name__ == "__main__":
    main()
