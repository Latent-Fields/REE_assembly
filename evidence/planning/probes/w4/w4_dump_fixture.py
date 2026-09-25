"""W4 fixture dump (bt0925-w4): re-run N3 proper's seed-532 REAL/SHUF member training and
probe-state collection VERBATIM (n3_probe_w4copy.py == probes/n3/n3_probe.py @ 9608f3117a with
only the worktree path changed; W4 knob OFF == ree-v3 042895a behaviour), then:

  1. reproduction check: DISC_0.5 / FULL gate-(a) Spearman for REAL/SHUF vs N3_s532.json;
  2. in-situ parity: ree_core W4 ON score_trajectory == probe aggregate(DISC_0.5) on every
     native pool, with the probe agent's own E3 (residue field included);
  3. writes a compact fixture (heads + states + harm_eval_head) for
     tests/contracts/test_w4_e3_aggregation.py, and checks the standalone reconstruction
     (fresh E2FastPredictor/E3TrajectorySelector from REEConfig.from_dims defaults) rolls out
     bit-identically and reports the reduced gate (a) on it.
ASCII-only output.
"""
from __future__ import annotations

import copy
import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import n3_probe_w4copy as N  # noqa: E402  (sets sys.path to wt-w4 + probes)

import torch  # noqa: E402

from ree_core.utils.config import REEConfig  # noqa: E402
from ree_core.predictors.e2_fast import E2FastPredictor, Trajectory  # noqa: E402
from ree_core.predictors.e3_selector import E3TrajectorySelector  # noqa: E402

CA, BB, R, BP = N.CA, N.BB, N.R, N.BP
S = 532
OUT = HERE / "fixture_w4_n3_s532.pt"
REP = HERE / "dump_report.json"
t0 = time.time()


def log(m):
    print("[w4dump t=%4.0fs] %s" % (time.time() - t0, m), flush=True)


def main():
    rep = {"seed": S}
    R.seed_all(S)
    _e, ref, _c = R.build_B(S, False)
    ref.eval()
    ref_enc = copy.deepcopy(ref.latent_stack.state_dict())
    heads = {}
    for arm in ("real", "shuf"):
        _hp, hd, info = N.train_member(S, ref, ref_enc, arm, 1200, 8, log)
        heads[arm.upper()] = hd
    ev = {nm: BB.evaluate(ref, heads[nm], BB.encode_segs(ref, BB.gen_policy(S, 3000 // N.EP_STEPS, 120, BB.pol_uniform(S * 7 + 3))[0]), "z", S)
          for nm in ("REAL", "SHUF")}
    rep["disc4"] = {k: v["disc4_h1"] for k, v in ev.items()}
    log("disc4 REAL %.3f SHUF %.3f (N3: 0.467 / 0.163)" % (rep["disc4"]["REAL"], rep["disc4"]["SHUF"]))

    pa = BB.fresh_agent(S, ref_enc)
    BP.set_head(pa, heads["REAL"])
    R.seed_all(S + 900)
    env = BB.make_env(S, 100)
    states = CA.collect_probe_states(pa, env, 320, 8, S, action_dim=5, n_cont=6, cont_len=4)
    log("states %d" % len(states))
    score_fn = CA.e3_score_fn(pa)
    fid = {str(d): False for d in range(1, 31)}
    rows = {}
    for nm in ("REAL", "SHUF"):
        BP.set_head(pa, heads[nm])
        rows[nm] = N.score_head(pa, states, fid, score_fn)
    rep["repro"] = {}
    for ag in ("DISC_0.5", "FULL", "D1"):
        r = {}
        for nm in ("REAL", "SHUF"):
            q = CA.e3_choice_quality({ag: [x["scaf"][ag] for x in rows[nm]]}, [x["jtrue"] for x in rows[nm]])
            r[nm] = q["arms"][ag]["spearman_mean"]
        rep["repro"][ag] = r
        log("repro %-8s REAL %.3f SHUF %.3f diff %+.3f" % (ag, r["REAL"], r["SHUF"], r["REAL"] - r["SHUF"]))

    # 2. in-situ parity on native pools, probe agent's own E3 (residue included)
    e3 = pa.e3
    BP.set_head(pa, heads["REAL"])
    maxrel = 0.0
    for st, row in zip(states, rows["REAL"]):
        pool = [pa.e2.rollout_with_world(st["s0"], st["z0"], a, compute_action_objects=False) for a in st["pool_actions"]]
        bt = N.batch_traj(pool)
        e3.config.use_e3_discounted_aggregation = True
        e3.config.e3_aggregation_gamma = 0.5
        try:
            with torch.no_grad():
                on = e3.score_trajectory(bt).reshape(-1).double().numpy()
        finally:
            e3.config.use_e3_discounted_aggregation = False
        ref_v = row["native"]["DISC_0.5"]
        maxrel = max(maxrel, float(np.abs(on - ref_v).max() / max(1.0, float(np.abs(ref_v).max()))))
    rep["insitu_parity_max_rel"] = maxrel
    log("in-situ parity ON vs probe DISC_0.5 max rel %.3g over %d native pools" % (maxrel, len(states)))

    # 3. fixture
    self_dim = int(states[0]["s0"].shape[-1])
    fx = {
        "meta": {"seed": S, "source": "N3 proper n3_probe.py 9608f3117a protocol, W3 member @ 042895a",
                 "body_obs_dim": int(BB.make_env(S, 0).body_obs_dim), "world_obs_dim": int(BB.make_env(S, 0).world_obs_dim),
                 "world_dim": int(states[0]["z0"].shape[-1]), "self_dim": self_dim, "action_dim": 5,
                 "n_states": len(states)},
        "heads": {nm: {"t": {k: v.clone() for k, v in heads[nm]["t"].items()},
                       "a": {k: v.clone() for k, v in heads[nm]["a"].items()}} for nm in ("REAL", "SHUF")},
        "harm_eval_head": {k: v.clone() for k, v in pa.e3.harm_eval_head.state_dict().items()},
        "z0": torch.cat([st["z0"] for st in states]),
        "base_actions": torch.cat([st["pool_actions"][0] for st in states]),
        "z_true": torch.stack([torch.cat([st["z_true"][c] for c in range(5)]) for st in states]),
        "native_pool_actions_state0": torch.cat(list(states[0]["pool_actions"])),
    }
    torch.save(fx, OUT)
    log("wrote %s (%d bytes)" % (OUT, OUT.stat().st_size))
    # e3 config diffs vs from_dims defaults (what the test builds)
    env8 = BB.make_env(S, 0)
    cfg_t = REEConfig.from_dims(body_obs_dim=env8.body_obs_dim, world_obs_dim=env8.world_obs_dim, action_dim=5)
    d_e3 = {k: (str(getattr(pa.e3.config, k)), str(getattr(cfg_t.e3, k))) for k in vars(cfg_t.e3)
            if str(getattr(pa.e3.config, k, None)) != str(getattr(cfg_t.e3, k))}
    d_e2 = {k: (str(getattr(pa.e2.config, k)), str(getattr(cfg_t.e2, k))) for k in vars(cfg_t.e2)
            if str(getattr(pa.e2.config, k, None)) != str(getattr(cfg_t.e2, k))}
    rep["e3_cfg_diff"] = d_e3
    rep["e2_cfg_diff"] = d_e2
    rep["dims"] = {"body_obs_dim": env8.body_obs_dim, "world_obs_dim": env8.world_obs_dim}
    log("cfg diffs e3 %s e2 %s" % (d_e3, d_e2))
    # standalone reconstruction as the test does it
    e2s = E2FastPredictor(cfg_t.e2)
    e3s = E3TrajectorySelector(cfg_t.e3)
    e3s.harm_eval_head.load_state_dict(fx["harm_eval_head"])
    e2s.eval(); e3s.eval()
    roll_diff, j_diff = 0.0, 0.0
    res_std = {}
    for nm in ("REAL", "SHUF"):
        e2s.world_transition.load_state_dict(fx["heads"][nm]["t"])
        e2s.world_action_encoder.load_state_dict(fx["heads"][nm]["a"])
        BP.set_head(pa, heads[nm])
        preds = {"DISC_0.5": [], "FULL": []}
        truths = []
        for i, st in enumerate(states):
            base = fx["base_actions"][i:i + 1]
            scaf = []
            for c in range(5):
                a = base.clone(); a[:, 0, :] = 0.0; a[:, 0, c] = 1.0
                tr_s = e2s.rollout_with_world(torch.zeros(1, self_dim), fx["z0"][i:i + 1], a, compute_action_objects=False)
                tr_p = pa.e2.rollout_with_world(st["s0"], st["z0"], a, compute_action_objects=False)
                roll_diff = max(roll_diff, max(float((x - y).abs().max()) for x, y in zip(tr_s.world_states, tr_p.world_states)))
                scaf.append(tr_s)
            bt = N.batch_traj(scaf)
            with torch.no_grad():
                full = e3s.score_trajectory(bt).reshape(-1).double().numpy()
                e3s.config.use_e3_discounted_aggregation = True
                disc = e3s.score_trajectory(bt).reshape(-1).double().numpy()
                e3s.config.use_e3_discounted_aggregation = False
                tt = [Trajectory(states=[torch.zeros(1, self_dim)] * 2, actions=CA.onehot(c, 5).unsqueeze(1),
                                 world_states=[fx["z0"][i:i + 1], fx["z_true"][i:i + 1, c]]) for c in range(5)]
                jt = e3s.score_trajectory(N.batch_traj(tt)).reshape(-1).double().numpy()
            preds["DISC_0.5"].append(disc); preds["FULL"].append(full); truths.append(jt)
            j_diff = max(j_diff, float(np.abs(full - rows[nm][i]["scaf"]["FULL"]).max()))
        res_std[nm] = {ag: CA.e3_choice_quality({ag: preds[ag]}, truths)["arms"][ag]["spearman_mean"] for ag in preds}
    rep["standalone_rollout_max_abs_diff"] = roll_diff
    rep["standalone_vs_probe_FULL_J_max_abs_diff"] = j_diff
    rep["standalone_gate_a"] = res_std
    log("standalone rollout diff %.3g ; FULL J diff vs probe agent E3 %.3g" % (roll_diff, j_diff))
    for ag in ("DISC_0.5", "FULL"):
        log("standalone gate(a) %-8s REAL %.3f SHUF %.3f diff %+.3f" % (
            ag, res_std["REAL"][ag], res_std["SHUF"][ag], res_std["REAL"][ag] - res_std["SHUF"][ag]))
    json.dump(rep, open(REP, "w"), indent=1, default=str)
    log("done")


if __name__ == "__main__":
    main()
