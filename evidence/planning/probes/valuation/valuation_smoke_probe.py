"""Worker G Mac SMOKE: harness validation for the grounded-valuation battery (NOT evidence for any
candidate). bt0924-valuation-b, orchestrate-20260924-breakthrough. Nothing lands in ree_core.

Regime: e3_evaluation_edge_test ADDENDUM 1 T2 (tiebreak ON, R5b scaffold, COV head, R2 depth 2,
trained evaluators, native benefit gate). Seed 42 only (chosen BEFORE running: the harm-heavy
stream, 43 contact ticks per 600, where the open-loop preview predicted the raw sign rule drives
harm DOWN -- the case the K3 detector must catch). 1,500 learning steps per arm, fresh agent per arm.

Arms (trained heads): M0 frozen; M1RAW raw sign rule (K3 positive control); M2 vote regression
with action fixed effects, t-gated; M4 random drift matched per channel to M2's realised per-tick
|dtheta| SD (run after M2, independent noise seed).

In-probe weight writer: a wrapper on agent.e3.select closes the previous tick's outcome window
(sum of the received scalar r over the steps it governed, G-contact: only |r| > 0.1), applies the
rule, writes w_c = w0_c * exp(theta_c) into E3Config (f_weight, lambda_ethical, rho_residue,
benefit_weight) BEFORE the tick is scored, then records the new tick's votes. theta in
[-ln 4, +ln 4]; harm floor = -ln 4. The rule reads only r, its own votes, the selected index,
the committed flag and the pick's first-action class. transition_type is recorded for scoring only.

Pre-registered detector (V4 / K3): FIRES if theta_harm sits at the floor on > 25% of ticks, OR
(final theta_harm < -0.5 AND > 80% of nonzero harm updates are negative AND harm contacts in the
second half of learning >= first half).
Predicted direction for M2 harm (from the off-policy pooled t = +3.09 and the on-policy s42
G-contact t = +1.65): theta_harm UP.
ASCII-only output.
"""
from __future__ import annotations

import argparse
import copy
import functools
import json
import math
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np
import torch

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "ree-v3-wt"))
sys.path.insert(0, str(HERE / "ree-v3-wt" / "experiments"))
sys.path.insert(0, str(HERE))

from experiments._harness import StepHarness  # noqa: E402
import rollout_fidelity_probe as R  # noqa: E402
import encoding_vs_objective_probe as E  # noqa: E402
import balanced_replay_probe as BP  # noqa: E402
import partitioned_repair_probe as PR  # noqa: E402
import evaluation_edge_probe as EP  # noqa: E402

torch.set_num_threads(2)
DEPTH = PR.DEPTH
CH = ["F", "harm", "residue", "benefit"]
FIELDS = ["f_weight", "lambda_ethical", "rho_residue", "benefit_weight"]
DKEYS = ["f_weighted", "harm_weighted", "residue_weighted", "benefit_weighted"]
SIGN = np.array([1.0, 1.0, 1.0, -1.0])
LN4 = math.log(4.0)
THR = 0.1


def fe_t(A_, V, R_):
    """Per-channel t of R on vote with action-class fixed effects."""
    A_ = np.asarray(A_); V = np.asarray(V); R_ = np.asarray(R_, float)
    Vd = V.copy(); Rd = R_.copy()
    for a in np.unique(A_):
        m = A_ == a
        Vd[m] -= V[m].mean(0); Rd[m] -= R_[m].mean()
    out = np.zeros(V.shape[1])
    for j in range(V.shape[1]):
        x = Vd[:, j]
        if (x ** 2).sum() < 1e-18 or Rd.std() < 1e-12:
            continue
        b = (x * Rd).sum() / (x ** 2).sum(); res = Rd - b * x
        se = math.sqrt((res ** 2).sum() / max(len(x) - 2, 1) / (x ** 2).sum())
        out[j] = b / se if se > 0 else 0.0
    return out


class Rule:
    def __init__(self, kind, seed, m4_sd=None):
        self.kind = kind; self.theta = np.zeros(4); self.hist = []
        self.absv = []; self.A = []; self.V = []; self.R = []
        self.rng = np.random.default_rng(seed + 9001); self.m4_sd = m4_sd

    def update(self, closed):
        """closed = dict(v, a, R, committed) for the tick whose window just ended; returns dtheta."""
        old = self.theta.copy()
        if self.kind == "M0" or closed is None:
            pass
        elif self.kind == "M4":
            self.theta = self.theta + self.rng.normal(0.0, 1.0, 4) * self.m4_sd
        elif closed["committed"]:
            v = closed["v"]
            if self.kind == "M1RAW":
                self.absv.append(np.abs(v))
                if closed["R"] != 0:
                    med = np.median(np.asarray(self.absv), axis=0)
                    self.theta = self.theta + 0.05 * np.sign(closed["R"]) * np.sign(v) * (np.abs(v) > med)
            elif self.kind == "M2":
                self.A.append(closed["a"]); self.V.append(v); self.R.append(closed["R"])
                if len(self.R) >= 20:
                    self.theta = 0.35 * fe_t(self.A, self.V, self.R)
        self.theta = np.clip(self.theta, -LN4, LN4)
        return self.theta - old


def run_arm(seed, enc_state, headD, evT, gate_n, steps, rule):
    R.seed_all(seed)
    env, agent, cfg = R.build_B(seed, False)
    agent.latent_stack.load_state_dict(enc_state)
    BP.set_head(agent, headD)
    agent.hippocampal.config.use_action_class_scaffold_candidates = True
    agent.e3._score_depth_limit = DEPTH
    EP.configure_eval(agent, evT, True, gate_n)
    agent.eval()
    e3 = agent.e3
    e3.e3_score_decomp_enabled = True
    w0 = np.array([float(getattr(e3.config, f)) for f in FIELDS])
    rew = []; ticks = []; st = {"step": -1, "pending": None, "demo": None}
    orig = e3.select

    def write_weights():
        w = w0 * np.exp(rule.theta)
        for f, val in zip(FIELDS, w):
            setattr(e3.config, f, float(val))
        return w

    def wsel(*a, **k):
        i = st["step"]
        closed = None
        if st["pending"] is not None:
            p = st["pending"]
            rr = np.asarray(rew[p["step"]:i], float)
            closed = dict(p, R=float(rr[np.abs(rr) > THR].sum()) if len(rr) else 0.0)
        dth = rule.update(closed)
        w = write_weights()
        # pass condition (1): the first tick after a weight change, score the same candidates
        # under DEFAULT weights on a deep copy of E3 (RNG state restored), for a before/after.
        if st["demo"] is None and np.any(np.abs(rule.theta) > 1e-9):
            rs = torch.get_rng_state(); nps = np.random.get_state()
            e3c = copy.deepcopy(e3)
            for f, val in zip(FIELDS, w0):
                setattr(e3c.config, f, float(val))
            e3c.e3_score_decomp_enabled = True
            dflt = []
            with torch.no_grad():
                for c in a[0]:
                    e3c.score_trajectory(c)
                    dflt.append([e3c._last_traj_components[kk] for kk in DKEYS])
            torch.set_rng_state(rs); np.random.set_state(nps)
            st["demo"] = {"step": i, "theta": rule.theta.tolist(), "w_default": w0.tolist(), "w_now": w.tolist(),
                          "default_terms": dflt}
        res = orig(*a, **k)
        pc = (e3.last_score_decomp or {}).get("per_candidate") or []
        X = np.asarray([[d.get(kk, 0.0) for kk in DKEYS] for d in pc], float)
        wsafe = np.where(w > 0, w, 1.0)
        sel = int(res.selected_index)
        if X.shape[0] >= 2 and sel < X.shape[0]:
            raw = X / wsafe
            v = -SIGN * (raw[sel] - np.delete(raw, sel, axis=0).mean(0))
        else:
            v = np.zeros(4)
        acls = int(res.selected_action.detach().reshape(-1).argmax())
        if st["demo"] is not None and "live_terms" not in st["demo"] and st["demo"]["step"] == i:
            st["demo"]["live_terms"] = X.tolist(); st["demo"]["sel_live"] = sel
            st["demo"]["argmin_default"] = int(np.argmin(np.asarray([sum(r[:3]) - r[3] for r in st["demo"]["default_terms"]])))
            st["demo"]["argmin_live_from_terms"] = int(np.argmin(X[:, :3].sum(1) - X[:, 3]))
        st["pending"] = {"step": i, "v": v, "a": acls, "committed": bool(res.committed)}
        ticks.append({"step": i, "theta": rule.theta.tolist(), "dtheta": dth.tolist(), "committed": bool(res.committed),
                      "w": w.tolist()})
        return res
    e3.select = wsel
    h = StepHarness(agent, env, train_mode=False, seed=seed)
    _f, obs = env.reset(); agent.reset(); h.reset()
    tts, ep = [], 0
    for i in range(steps):
        st["step"] = i
        r = h.step(obs)
        rew.append(float(r.harm_signal))
        tts.append(r.info.get("transition_type", "none") if isinstance(r.info, dict) else "none")
        obs = r.next_obs_dict
        if r.done:
            _f, obs = env.reset(); agent.reset(); h.reset(); ep += 1

    def counts(lo, hi):
        tc = Counter(tts[lo:hi]); rw = np.asarray(rew[lo:hi])
        return {"reward_per_100": float(rw.sum() * 100 / max(hi - lo, 1)),
                "harm_contacts": int(sum(v for k, v in tc.items() if k in EP.CONTACT)),
                "hazard_approach": int(tc.get("hazard_approach", 0)), "benefit_approach": int(tc.get("benefit_approach", 0)),
                "benefit_contacts": int(sum(v for k, v in tc.items() if k in EP.BCONTACT))}
    return {"first600": counts(0, 600), "all": counts(0, steps), "half1": counts(0, steps // 2),
            "half2": counts(steps // 2, steps), "episodes_ended": ep, "ticks": ticks, "demo": st["demo"],
            "w0": w0.tolist()}


def detector(arm):
    th = np.array([t["theta"][1] for t in arm["ticks"]]); d = np.array([t["dtheta"][1] for t in arm["ticks"]])
    at_floor = float(np.mean(th <= -LN4 + 1e-9)) if len(th) else 0.0
    nz = d[np.abs(d) > 1e-12]
    frac_neg = float(np.mean(nz < 0)) if len(nz) else 0.0
    rising = arm["half2"]["harm_contacts"] >= arm["half1"]["harm_contacts"]
    fires = at_floor > 0.25 or (th[-1] < -0.5 and frac_neg > 0.8 and rising)
    return {"frac_ticks_at_floor": at_floor, "final_theta_harm": float(th[-1]) if len(th) else 0.0,
            "frac_nonzero_harm_updates_negative": frac_neg, "n_nonzero_harm_updates": int(len(nz)),
            "contacts_half1_half2": [arm["half1"]["harm_contacts"], arm["half2"]["harm_contacts"]], "FIRES": bool(fires)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--steps", type=int, default=1500)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    t0 = time.time()
    R.CausalGridWorldV2 = functools.partial(R.CausalGridWorldV2, proximity_approach_magnitude_tiebreak=True)
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
    headA, _ = BP.train_arm(agent, init, trans, A, np.ones(len(trans)), 3000, a.seed)
    headD, _ = BP.train_arm(agent, init, trans_d, A, np.ones(len(trans_d)), 3000, a.seed)
    init_ev = EP.eval_heads(agent)
    BP.set_head(agent, headA)
    nat = EP.collect_native(agent, R.build_B(a.seed + 21, False)[0], 1500, a.seed + 21)
    ran = EP.collect_random(agent, R.build_B(a.seed + 23, False)[0], 1500, a.seed + 23)
    agent.reset()
    evT, infoT = EP.train_evaluators(agent, init_ev, nat + ran, 1500, a.seed, False)
    gate_n = infoT["n_benefit_pos_train"]
    print("PREAMBLE gate_n=%d t=%.0fs" % (gate_n, time.time() - t0), flush=True)
    out = {"args": vars(a), "gate_n": gate_n, "arms": {}}
    for kind in ("M0", "M1RAW", "M2"):
        arm = run_arm(a.seed, enc_state, headD, evT, gate_n, a.steps, Rule(kind, a.seed))
        arm["detector"] = detector(arm); out["arms"][kind] = arm
        print("ARM %s first600=%s all=%s theta_end=%s det=%s t=%.0fs" % (
            kind, json.dumps(arm["first600"]), json.dumps(arm["all"]), [round(x, 3) for x in arm["ticks"][-1]["theta"]],
            json.dumps(arm["detector"]), time.time() - t0), flush=True)
        json.dump(out, open(a.out, "w"))
    m2d = np.array([t["dtheta"] for t in out["arms"]["M2"]["ticks"]])
    m4_sd = m2d.std(0)
    arm = run_arm(a.seed, enc_state, headD, evT, gate_n, a.steps, Rule("M4", a.seed, m4_sd=m4_sd))
    arm["detector"] = detector(arm); arm["m4_sd"] = m4_sd.tolist(); out["arms"]["M4"] = arm
    print("ARM M4 sd=%s first600=%s all=%s theta_end=%s det=%s t=%.0fs" % (
        [round(x, 4) for x in m4_sd], json.dumps(arm["first600"]), json.dumps(arm["all"]),
        [round(x, 3) for x in arm["ticks"][-1]["theta"]], json.dumps(arm["detector"]), time.time() - t0), flush=True)
    out["t_total_s"] = round(time.time() - t0, 1)
    json.dump(out, open(a.out, "w"))
    print("wrote %s t=%.0fs" % (a.out, time.time() - t0), flush=True)


if __name__ == "__main__":
    main()
