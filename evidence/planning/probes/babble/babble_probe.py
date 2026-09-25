"""Pre-registered probe: is Phase-0 babbling a sufficient and DURABLE source of action
coverage for E2's world head? (bt0925-babble, Worker Q, orchestrate-20260924-breakthrough)

Pre-registration: REE_assembly/evidence/planning/babbling_e2_action_coverage_probe_20260925.md
(committed a9f323c92b1 BEFORE any registered seed ran). One invocation = one seed.

Env: the real Phase-0 env (CausalGridWorldV2 size 12, resource_respawn_on_consume, Phase-0
env_kwargs, new env per 200-step episode, seed = seed*160 + k). Latent: the native z_world
read path (sense()) of the addendum-1 build (rollout_fidelity_probe.build_B, world_dim 32),
random-init encoder; secondary fixed PCA-32 of the raw world obs.

Datasets (N transitions each): L1 = D_BAB (591c agent, native act, 591h loop), L0 (p=0.8 one
class, rest uniform over 0..3), L2 (uniform class over 0..3 held for U{1..4} steps), BAB_SHUF
(L1 actions permuted), POL (build_B native waking, init head).
Open-loop heads (3000 updates): B0 (POL), B1=L1_pre, B1S, L0_pre, L2_pre (+ PCA twins).
Post phase (P closed-loop steps, fresh build_B agent, native E3, head in place and training
online on on-policy transitions, 9000 updates): L0_post, L1_post(=B2), L2_post, B3 (L1 + 25%
D_L1 replay), L2R (L2 + 25% D_L2 replay), NB (init head, on-policy only).
Metric: executed-action-closest at h=1 over classes 0..3 on held-out uniform-random test.
ASCII-only output.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
WT = HERE / "ree-v3-wt"
sys.path.insert(0, str(WT))
sys.path.insert(0, str(WT / "experiments"))
sys.path.insert(0, str(HERE / "probes_src"))

import torch  # noqa: E402
import torch.nn.functional as F  # noqa: E402

torch.set_num_threads(2)

from ree_core.environment.causal_grid_world import CausalGridWorldV2  # noqa: E402
from experiments._harness import StepHarness  # noqa: E402
from infant_curriculum import InfantCurriculumScheduler  # noqa: E402
import v3_exq_591h_isef005_phase01_gate_live_v3 as X  # noqa: E402
import v3_exq_591_isef005_curriculum_vs_flat_v3 as X0  # noqa: E402
import rollout_fidelity_probe as R  # noqa: E402
import balanced_replay_probe as BP  # noqa: E402

GRID = X0.GRID_SIZE          # 12
EP_STEPS = 200
SEED_STRIDE = 160            # 591h: env seed = seed * n_episodes(160) + ep
A_ENV = 5
CLASSES = [0, 1, 2, 3]       # the Phase-0 generator's action space (argmax % 4)
PRE_UPD = 3000
POST_UPD = 9000
REPLAY_FRAC = 0.25
PH0_KW = InfantCurriculumScheduler(grid_size=GRID).env_kwargs(0)


def make_env(seed, k):
    return CausalGridWorldV2(size=GRID, seed=seed * SEED_STRIDE + k, resource_respawn_on_consume=True,
                             pos_telemetry_enabled=True, traj_telemetry_enabled=True, **PH0_KW)


def snap_obs(od):
    keep = {}
    for key in ("body_state", "world_state", "harm_obs", "harm_obs_a", "harm_history"):
        v = od.get(key)
        if v is not None:
            keep[key] = torch.as_tensor(v).detach().clone().float()
    return keep


def entropy(counts):
    tot = sum(counts.values())
    p = np.asarray([v / tot for v in counts.values() if v > 0])
    return float(-(p * np.log(p)).sum()) if tot else 0.0


def run_lengths(segs):
    rl = []
    for s in segs:
        a = s["a"]
        if not a:
            continue
        cur = 1
        for i in range(1, len(a)):
            if a[i] == a[i - 1]:
                cur += 1
            else:
                rl.append(cur); cur = 1
        rl.append(cur)
    return float(np.mean(rl)) if rl else 0.0


def dose_stats(segs):
    c = Counter(a for s in segs for a in s["a"])
    return {"n": sum(c.values()), "class_counts": {str(k): v for k, v in sorted(c.items())},
            "entropy_nats": entropy(c), "majority_share": max(c.values()) / max(1, sum(c.values())),
            "mean_run_length": run_lengths(segs)}


# ------------------------------------------------------------------ generators
def gen_L1(seed, n_eps):
    """The REAL Phase-0 generator: 591c diversity-armed agent, native act, 591h loop verbatim
    (no agent.reset between episodes, as 591h; update_residue + update_z_goal; novelty override)."""
    torch.manual_seed(seed)
    agent = X._build_diversity_agent()
    sched = InfantCurriculumScheduler(grid_size=GRID)
    segs, h_pos, early = [], [], 0
    for ep in range(n_eps):
        sched.env_kwargs()
        agent.config.e3.novelty_bonus_weight = float(sched.config_overrides().get("novelty_bonus_weight", 0.5))
        env = make_env(seed, ep)
        _f, od = env.reset()
        ob, ow = X0._extract_obs(od)
        seg = {"obs": [snap_obs(od)], "a": []}
        ep_h = -1.0
        for _s in range(EP_STEPS):
            with torch.no_grad():
                action = agent.act_with_split_obs(obs_body=ob, obs_world=ow)
            ai = int(action.argmax().item()) % X0.ACTION_DIM
            _o, harm, done, info, od = env.step(ai)
            agent.update_residue(float(harm))
            ob, ow = X0._extract_obs(od)
            benefit = float(ob[11].item()) if ob.shape[0] > 11 else 0.0
            energy = float(ob[3].item()) if ob.shape[0] > 3 else 0.5
            agent.update_z_goal(benefit_exposure=benefit, drive_level=max(0.0, min(1.0, 1.0 - energy)))
            ep_h = float(info.get("pos_entropy", -1.0))
            seg["a"].append(ai); seg["obs"].append(snap_obs(od))
            if done:
                early += 1
                segs.append(seg)
                _f, od = env.reset()
                ob, ow = X0._extract_obs(od)
                seg = {"obs": [snap_obs(od)], "a": []}
        segs.append(seg)
        h_pos.append(ep_h)
        sched.update(ep, h_pos=ep_h if ep_h >= 0 else None)
    return segs, {"h_pos_mean": float(np.mean(h_pos)), "h_pos_max": float(np.max(h_pos)),
                  "early_terminations": early, "phase_after": sched.current_phase}


def gen_policy(seed, n_eps, k0, policy):
    segs, early, rew = [], 0, []
    for ep in range(n_eps):
        env = make_env(seed, k0 + ep)
        _f, od = env.reset()
        seg = {"obs": [snap_obs(od)], "a": []}
        for _s in range(EP_STEPS):
            ai = policy()
            _o, harm, done, info, od = env.step(ai)
            rew.append(float(harm))
            seg["a"].append(ai); seg["obs"].append(snap_obs(od))
            if done:
                early += 1
                segs.append(seg)
                _f, od = env.reset()
                seg = {"obs": [snap_obs(od)], "a": []}
        segs.append(seg)
    return segs, {"early_terminations": early}


def pol_L0(seed):
    g = np.random.default_rng(seed * 7 + 1)
    c0 = int(g.integers(0, 4))
    others = [c for c in CLASSES if c != c0]

    def f():
        return c0 if g.random() < 0.8 else int(others[int(g.integers(0, 3))])
    return f, c0


def pol_L2(seed):
    g = np.random.default_rng(seed * 7 + 2)
    st = {"c": 0, "left": 0}

    def f():
        if st["left"] <= 0:
            st["c"] = int(g.integers(0, 4)); st["left"] = int(g.integers(1, 5))
        st["left"] -= 1
        return st["c"]
    return f


def pol_uniform(seed):
    g = np.random.default_rng(seed)
    return lambda: int(g.integers(0, 4))


def gen_POL(agent, seed, n_eps, k0):
    """Native on-policy (build_B agent, native waking, init head). Also the hazard classifier."""
    segs, early, rew = [], 0, []
    for ep in range(n_eps):
        env = make_env(seed, k0 + ep)
        h = StepHarness(agent, env, train_mode=False, seed=seed * 1000 + k0 + ep)
        _f, od = env.reset(); agent.reset(); h.reset()
        seg = {"obs": [snap_obs(od)], "a": [], "z": []}
        for _s in range(EP_STEPS):
            r = h.step(od)
            rew.append(float(r.harm_signal))
            seg["a"].append(int(r.action.detach().reshape(-1).argmax()))
            od = r.next_obs_dict
            seg["obs"].append(snap_obs(od))
            if r.done:
                early += 1
                segs.append(seg)
                _f, od = env.reset(); agent.reset(); h.reset()
                seg = {"obs": [snap_obs(od)], "a": [], "z": []}
        segs.append(seg)
    rew = np.asarray(rew)
    n = len(rew)
    return segs, {"early_terminations": early, "early_per_1000": early * 1000.0 / n,
                  "harm_events_per_100": float((rew < 0).sum() * 100.0 / n),
                  "benefit_events_per_100": float((rew > 0).sum() * 100.0 / n),
                  "reward_per_100": float(rew.sum() * 100.0 / n)}


# ------------------------------------------------------------------ encoding
@torch.no_grad()
def encode_segs(ref, segs):
    """Native read path: ref.sense() over each episode stream, ref.reset() at boundaries."""
    out = []
    for s in segs:
        if len(s["a"]) < 1:
            continue
        ref.reset()
        zs = []
        for o in s["obs"]:
            lat = ref.sense(o["body_state"], o["world_state"], obs_harm=o.get("harm_obs"),
                            obs_harm_a=o.get("harm_obs_a"), obs_harm_history=o.get("harm_history"))
            zs.append(lat.z_world.detach().reshape(-1).clone())
        raw = torch.stack([o["world_state"].reshape(-1) for o in s["obs"]])
        out.append({"z": torch.stack(zs), "raw": raw, "a": torch.tensor(s["a"])})
    return out


def to_trans(eps, key):
    X0_, X1_, A_ = [], [], []
    for e in eps:
        x = e[key]
        X0_.append(x[:-1]); X1_.append(x[1:]); A_.append(e["a"])
    return torch.cat(X0_), torch.cat(X1_), torch.cat(A_)


# ------------------------------------------------------------------ training
def train_head(ref, init, trans, steps, seed, replay=None):
    BP.set_head(ref, init)
    torch.manual_seed(seed)
    x0, x1, a = trans
    oh = F.one_hot(a, A_ENV).float()
    params = BP.head_params(ref)
    opt = torch.optim.Adam(params, lr=3e-4)
    before = [p.detach().clone() for p in params]
    losses, grad_ok = [], None
    n = x0.shape[0]
    if replay is not None:
        r0, r1, ra = replay
        roh = F.one_hot(ra, A_ENV).float()
    with torch.enable_grad():
        for i in range(steps):
            idx = torch.randint(0, n, (32,))
            zb, ab, yb = x0[idx], oh[idx], x1[idx]
            loss = F.mse_loss(ref.e2.world_forward(zb, ab), yb)
            opt.zero_grad(); loss.backward()
            if i == 0:
                grad_ok = all(p.grad is not None and float(p.grad.abs().sum()) > 0 for p in params)
            torch.nn.utils.clip_grad_norm_(params, 1.0); opt.step()
            losses.append(float(loss.detach()))
    delta = float(torch.sqrt(sum(((p.detach() - b) ** 2).sum() for p, b in zip(params, before))))
    return BP.get_head(ref), {"loss_first50": float(np.mean(losses[:50])), "loss_last200": float(np.mean(losses[-200:])),
                              "identity_mse": float(F.mse_loss(x0, x1)), "grad_nonnull_step1": grad_ok,
                              "param_delta": delta, "n_trans": int(n)}


# ------------------------------------------------------------------ evaluation
@torch.no_grad()
def evaluate(ref, head, te, key, seed, H=10, max_starts=300):
    BP.set_head(ref, head)
    e2 = ref.e2
    g = np.random.default_rng(seed + 77)
    starts = [(i, t) for i, e in enumerate(te) for t in range(e["a"].shape[0] - H + 1)]
    if len(starts) > max_starts:
        starts = [starts[j] for j in sorted(g.choice(len(starts), max_starts, replace=False))]
    zs = torch.zeros(1, 32)
    rows = {h: {"err": [], "pers": []} for h in range(1, H + 1)}
    disc4 = {1: [], 3: [], 5: []}
    disc5 = {1: []}
    for i, t in starts:
        x = te[i][key]
        acts = F.one_hot(te[i]["a"][t:t + H], A_ENV).float().unsqueeze(0)
        x0 = x[t:t + 1]
        tr = e2.rollout_with_world(zs, x0, acts, compute_action_objects=False)
        for h in range(1, H + 1):
            y = x[t + h:t + h + 1]
            rows[h]["err"].append(float((tr.world_states[h] - y).norm()))
            rows[h]["pers"].append(float((x0 - y).norm()))
        ex = int(te[i]["a"][t])
        for h in (1, 3, 5):
            y = x[t + h:t + h + 1]
            errs = []
            for c in range(A_ENV):
                a2 = acts[:, :h].clone(); a2[0, 0] = 0.0; a2[0, 0, c] = 1.0
                errs.append(float((e2.rollout_with_world(zs, x0, a2, compute_action_objects=False).world_states[h] - y).norm()))
            e4 = [errs[c] for c in CLASSES]
            disc4[h].append(int(np.argmin(e4)) == CLASSES.index(ex))
            if h == 1:
                disc5[1].append(int(np.argmin(errs)) == ex)
    k = 0
    eop = {}
    for h in range(1, H + 1):
        me, mp = float(np.median(rows[h]["err"])), float(np.median(rows[h]["pers"]))
        eop[h] = me / mp if mp > 0 else None
        if mp > 0 and me < mp and k == h - 1:
            k = h
    return {"n_starts": len(starts), "disc4_h1": float(np.mean(disc4[1])), "disc4_h3": float(np.mean(disc4[3])),
            "disc4_h5": float(np.mean(disc4[5])), "disc5_h1": float(np.mean(disc5[1])), "k": k,
            "err_over_pers_h1": eop[1], "err_over_pers_h5": eop[5]}


# ------------------------------------------------------------------ post-babbling phase
def fresh_agent(seed, ref_enc):
    R.seed_all(seed)
    _e, agent, _c = R.build_B(seed, False)
    enc = agent.latent_stack.state_dict()
    for kk, v in ref_enc.items():
        assert torch.equal(enc[kk], v), "encoder mismatch vs reference"
    agent.eval()
    return agent


def post_phase(seed, ref_enc, head, P, replay=None):
    agent = fresh_agent(seed, ref_enc)
    BP.set_head(agent, head)
    R.seed_all(seed + 500)
    params = BP.head_params(agent)
    opt = torch.optim.Adam(params, lr=3e-4)
    bz0, ba, bz1 = [], [], []
    if replay is not None:
        r0, r1, ra = replay
        roh = F.one_hot(ra, A_ENV).float()
    owed, done_upd, grad_ok = 0, 0, None
    rew, acts, early_flags, t = [], [], [], 0
    losses = []
    n_eps = P // EP_STEPS
    for ep in range(n_eps):
        env = make_env(seed, 50 + ep)
        h = StepHarness(agent, env, train_mode=False, seed=seed * 1000 + 50 + ep)
        _f, od = env.reset(); agent.reset(); h.reset()
        prev = None
        for _s in range(EP_STEPS):
            r = h.step(od)
            z = r.latent.z_world.detach().reshape(1, -1).clone()
            a = int(r.action.detach().reshape(-1).argmax())
            if prev is not None:
                bz0.append(prev[0]); ba.append(prev[1]); bz1.append(z)
            prev = (z, a)
            rew.append(float(r.harm_signal)); acts.append(a); early_flags.append(bool(r.done))
            od = r.next_obs_dict
            if r.done:
                _f, od = env.reset(); agent.reset(); h.reset(); prev = None
            owed += (POST_UPD * (t + 1)) // P - (POST_UPD * t) // P
            t += 1
            if len(bz0) >= 64 and owed > 0:
                Z0 = torch.cat(bz0); Z1 = torch.cat(bz1); OH = F.one_hot(torch.tensor(ba), A_ENV).float()
                n = Z0.shape[0]
                with torch.enable_grad():
                    for _u in range(owed):
                        if replay is None:
                            idx = torch.randint(0, n, (32,))
                            zb, ab, yb = Z0[idx], OH[idx], Z1[idx]
                        else:
                            kr = int(round(32 * REPLAY_FRAC))
                            idx = torch.randint(0, n, (32 - kr,)); ridx = torch.randint(0, r0.shape[0], (kr,))
                            zb = torch.cat([Z0[idx], r0[ridx]]); ab = torch.cat([OH[idx], roh[ridx]]); yb = torch.cat([Z1[idx], r1[ridx]])
                        loss = F.mse_loss(agent.e2.world_forward(zb, ab), yb)
                        opt.zero_grad(); loss.backward()
                        if grad_ok is None:
                            grad_ok = all(p.grad is not None and float(p.grad.abs().sum()) > 0 for p in params)
                        torch.nn.utils.clip_grad_norm_(params, 1.0); opt.step()
                        losses.append(float(loss.detach()))
                done_upd += owed
                owed = 0
    half = len(rew) // 2
    rw, ac, ef = np.asarray(rew[half:]), acts[half:], early_flags[half:]
    cc = Counter(ac)
    beh = {"steps": len(rw), "reward_per_100": float(rw.sum() * 100.0 / len(rw)),
           "harm_events_per_100": float((rw < 0).sum() * 100.0 / len(rw)),
           "benefit_events_per_100": float((rw > 0).sum() * 100.0 / len(rw)),
           "action_entropy": entropy(cc), "majority_share": max(cc.values()) / len(ac),
           "action_counts": {str(k): v for k, v in sorted(cc.items())}, "early_terminations": int(sum(ef))}
    full = {"early_terminations_all": int(sum(early_flags)), "action_counts_all": {str(k): v for k, v in sorted(Counter(acts).items())},
            "updates_done": done_upd, "grad_nonnull_first": grad_ok,
            "loss_last200": float(np.mean(losses[-200:])) if losses else None}
    return BP.get_head(agent), beh, full


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--n-eps", type=int, default=25)       # N = 25 x 200 = 5000
    ap.add_argument("--post", type=int, default=1200)       # P
    ap.add_argument("--test-steps", type=int, default=3000)
    ap.add_argument("--probe-steps", type=int, default=200)
    ap.add_argument("--skip", default="", help="comma list of post arms to drop (pre-registered drop order)")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    t0 = time.time()
    S = a.seed
    skip = set(x for x in a.skip.split(",") if x)
    res = {"args": vars(a), "code_sha": "6de633cea57c64da500712ede9061475336ef954", "classes": CLASSES}

    def log(msg):
        print("[s%d t=%4.0fs] %s" % (S, time.time() - t0, msg), flush=True)

    # reference agent (native read path) + init head
    ref = fresh_agent_ref = None
    R.seed_all(S)
    _e, ref, _c = R.build_B(S, False)
    ref.eval()
    ref_enc = copy.deepcopy(ref.latent_stack.state_dict())
    init = BP.get_head(ref)

    # POL first: the NATIVE on-policy arm classifies the seed before anything else is looked at
    pol_agent = fresh_agent(S, ref_enc)
    R.seed_all(S + 300)
    pol_segs, pol_info = gen_POL(pol_agent, S, a.n_eps, 25)
    trapped = bool(pol_info["early_per_1000"] >= 3.0 or pol_info["harm_events_per_100"] >= 10.0)
    res["hazard_class"] = "hazard-trapped" if trapped else "benign"
    res["pol_run"] = pol_info
    log("POL %s %s" % (res["hazard_class"], json.dumps(pol_info)))
    del pol_agent

    l1_segs, l1_info = gen_L1(S, a.n_eps)
    log("L1 generated %s" % json.dumps(l1_info))
    f0, c0 = pol_L0(S)
    l0_segs, l0_info = gen_policy(S, a.n_eps, 0, f0)
    l2_segs, l2_info = gen_policy(S, a.n_eps, 0, pol_L2(S))
    te_segs, _ = gen_policy(S, a.test_steps // EP_STEPS, 120, pol_uniform(S * 7 + 3))
    fit_segs, _ = gen_policy(S, 15, 140, pol_uniform(S * 7 + 4))
    res["doses"] = {"L0": dict(dose_stats(l0_segs), c0=c0, **l0_info), "L1": dict(dose_stats(l1_segs), **l1_info),
                    "L2": dict(dose_stats(l2_segs), **l2_info), "POL": dose_stats(pol_segs)}
    log("DOSES %s" % json.dumps({k: (round(v["entropy_nats"], 3), round(v["mean_run_length"], 2), v["class_counts"]) for k, v in res["doses"].items()}))

    E = {nm: encode_segs(ref, sg) for nm, sg in (("L0", l0_segs), ("L1", l1_segs), ("L2", l2_segs), ("POL", pol_segs),
                                                  ("TE", te_segs), ("FIT", fit_segs))}
    # shuffled babbling: permute L1's action labels across all timesteps
    g = torch.Generator().manual_seed(S + 17)
    allA = torch.cat([e["a"] for e in E["L1"]])
    perm = allA[torch.randperm(allA.shape[0], generator=g)]
    shuf, off = [], 0
    for e in E["L1"]:
        n = e["a"].shape[0]
        shuf.append({"z": e["z"], "raw": e["raw"], "a": perm[off:off + n]}); off += n
    E["SHUF"] = shuf
    # fixed PCA-32
    rawfit = torch.cat([e["raw"] for e in E["FIT"]])
    mu = rawfit.mean(0)
    _U, Sv, V = torch.linalg.svd(rawfit - mu, full_matrices=False)
    Pm = V[:32].T
    znorm = float(torch.cat([e["z"] for e in E["TE"]]).norm(dim=-1).mean())
    pnorm = float(((torch.cat([e["raw"] for e in E["TE"]]) - mu) @ Pm).norm(dim=-1).mean())
    for nm in E:
        for e in E[nm]:
            e["pca"] = ((e["raw"] - mu) @ Pm) * (znorm / pnorm)
    res["pca_evr"] = float((Sv[:32] ** 2).sum() / (Sv ** 2).sum())
    log("ENCODED n_trans %s" % {k: int(sum(e["a"].shape[0] for e in v)) for k, v in E.items()})

    # open-loop heads
    arms = {"B0": "POL", "B1": "L1", "B1S": "SHUF", "L0_pre": "L0", "L2_pre": "L2"}
    heads, res["open_loop"] = {}, {}
    for nm, ds in arms.items():
        for key in ("z", "pca"):
            hd, tinfo = train_head(ref, init, to_trans(E[ds], key), PRE_UPD, S)
            ev = evaluate(ref, hd, E["TE"], key, S)
            res["open_loop"]["%s|%s" % (nm, key)] = {"train": tinfo, "eval": ev}
            if key == "z":
                heads[nm] = hd
            log("HEAD %s|%s disc4_h1=%.3f h3=%.3f h5=%.3f disc5=%.3f k=%d fit %.2e/%.2e grad=%s" % (
                nm, key, ev["disc4_h1"], ev["disc4_h3"], ev["disc4_h5"], ev["disc5_h1"], ev["k"],
                tinfo["loss_last200"], tinfo["identity_mse"], tinfo["grad_nonnull_step1"]))
            if nm == "B1" and key == "z" and (not tinfo["grad_nonnull_step1"] or tinfo["param_delta"] <= 0):
                res["HARNESS_FAILURE"] = "B1 head received no gradient"
                json.dump(res, open(a.out, "w"), indent=1, default=str)
                raise SystemExit("HARNESS FAILURE: B1 no gradient")
    ev0 = evaluate(ref, init, E["TE"], "z", S)
    res["open_loop"]["INIT|z"] = {"eval": ev0}
    log("HEAD INIT disc4_h1=%.3f k=%d" % (ev0["disc4_h1"], ev0["k"]))

    # post-babbling phase
    rep_L1 = to_trans(E["L1"], "z")
    rep_L2 = to_trans(E["L2"], "z")
    post_arms = [("L0_post", heads["L0_pre"], None), ("L1_post", heads["B1"], None), ("L2_post", heads["L2_pre"], None),
                 ("B3", heads["B1"], rep_L1), ("L2R", heads["L2_pre"], rep_L2), ("NB", init, None)]
    res["post"] = {}
    for nm, hd, rep in post_arms:
        if nm in skip:
            res["post"][nm] = {"skipped": True}
            log("POST %s SKIPPED (pre-registered drop order)" % nm)
            continue
        hpost, beh, full = post_phase(S, ref_enc, hd, a.post, replay=rep)
        ev = evaluate(ref, hpost, E["TE"], "z", S)
        heads[nm] = hpost
        res["post"][nm] = {"eval": ev, "beh_last50": beh, "run": full}
        log("POST %s disc4_h1=%.3f k=%d | beh r/100=%.3f harm=%.2f ben=%.2f H=%.2f early=%d | upd=%d grad=%s" % (
            nm, ev["disc4_h1"], ev["k"], beh["reward_per_100"], beh["harm_events_per_100"],
            beh["benefit_events_per_100"], beh["action_entropy"], beh["early_terminations"], full["updates_done"],
            full["grad_nonnull_first"]))

    # D2 reach + depth-1 diagnostic at probe states (native waking, init head)
    if "D2" not in skip:
        pa = fresh_agent(S, ref_enc)
        BP.set_head(pa, init)
        R.seed_all(S + 900)
        env = make_env(S, 100)
        states = BP.collect_probe_states(pa, env, a.probe_steps, 10, A_ENV, S)
        states = states[:20]
        res["n_probe_states"] = len(states)
        res["probe_validation_maxabs"] = float(max([s.get("validation_maxabs", 0.0) for s in states] + [0.0]))
        with torch.no_grad():
            def picks(hd):
                BP.set_head(pa, hd)
                out = []
                for st in states:
                    trajs = [pa.e2.rollout_with_world(st["s0"], st["z0"], acts, compute_action_objects=False)
                             for acts in st["pool_actions"]]
                    out.append(int(np.argmin(BP.score(pa, trajs, None))))
                return out
            base = picks(init)
            res["D2_pick_change_vs_native"] = {}
            for nm in ("B1", "B1S", "L0_pre", "L2_pre", "L1_post", "L2_post", "L0_post"):
                if nm in heads:
                    p = picks(heads[nm])
                    res["D2_pick_change_vs_native"][nm] = float(np.mean([x != y for x, y in zip(p, base)]))
            res["depth1_diag"] = {}
            for nm in ("NB", "L0_post", "L1_post", "L2_post", "B1", "L2_pre"):
                if nm in heads:
                    BP.set_head(pa, heads[nm])
                    res["depth1_diag"][nm] = BP.m2_choice(pa, states, A_ENV)
        log("D2 %s" % json.dumps(res["D2_pick_change_vs_native"]))
        log("DEPTH1 %s" % json.dumps({k: (v["spearman_Jpred_Jtrue_FULL"], v["spearman_Jpred_Jtrue_DEPTH1"]) for k, v in res["depth1_diag"].items()}))
    res["t_total_s"] = round(time.time() - t0, 1)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    json.dump(res, open(a.out, "w"), indent=1, default=str)
    log("wrote %s" % a.out)


if __name__ == "__main__":
    main()
