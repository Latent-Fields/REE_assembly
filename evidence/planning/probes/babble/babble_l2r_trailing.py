"""Trailing L2R block (bt0925-babble). Restored after the orchestrator raised the cap (L2R had been
dropped for seeds 108-110 under the pre-registered drop rule, for resources alone, not results).
IDENTICAL pre-registered configuration: it regenerates D_L2 and the test set deterministically,
retrains L2_pre (checked bit-for-bit against the main run's L2_pre disc), and runs the L2R post
phase (L2_pre head, 25% D_L2 replay, P=1200, 9000 updates), using the functions of babble_probe.py
unchanged. It writes results/BAB_L2R_s<seed>.json. ASCII only.
"""
import argparse
import copy
import json
import time
from pathlib import Path

import babble_probe as B
import torch


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--n-eps", type=int, default=12)
    ap.add_argument("--post", type=int, default=1200)
    ap.add_argument("--test-steps", type=int, default=3000)
    a = ap.parse_args()
    S = a.seed
    t0 = time.time()
    main_res = json.load(open(B.HERE / "results" / ("BAB_s%d.json" % S)))
    B.R.seed_all(S)
    _e, ref, _c = B.R.build_B(S, False)
    ref.eval()
    ref_enc = copy.deepcopy(ref.latent_stack.state_dict())
    init = B.BP.get_head(ref)
    l2_segs, _ = B.gen_policy(S, a.n_eps, 0, B.pol_L2(S))
    te_segs, _ = B.gen_policy(S, a.test_steps // B.EP_STEPS, 120, B.pol_uniform(S * 7 + 3))
    E = {"L2": B.encode_segs(ref, l2_segs), "TE": B.encode_segs(ref, te_segs)}
    hd, tinfo = B.train_head(ref, init, B.to_trans(E["L2"], "z"), B.PRE_UPD, S)
    ev_pre = B.evaluate(ref, hd, E["TE"], "z", S)
    main_pre = main_res["open_loop"]["L2_pre|z"]["eval"]["disc4_h1"]
    consistent = abs(ev_pre["disc4_h1"] - main_pre) < 1e-9
    print("[s%d] L2_pre recomputed disc4_h1=%.4f main=%.4f consistent=%s" % (S, ev_pre["disc4_h1"], main_pre, consistent), flush=True)
    hpost, beh, full = B.post_phase(S, ref_enc, hd, a.post, replay=B.to_trans(E["L2"], "z"))
    ev = B.evaluate(ref, hpost, E["TE"], "z", S)
    out = {"seed": S, "L2_pre_recomputed": ev_pre, "L2_pre_main_disc4_h1": main_pre, "consistent_with_main": consistent,
           "L2R": {"eval": ev, "beh_last50": beh, "run": full}, "t_total_s": round(time.time() - t0, 1),
           "note": "trailing block, restored after cap change; identical pre-registered config"}
    json.dump(out, open(B.HERE / "results" / ("BAB_L2R_s%d.json" % S), "w"), indent=1, default=str)
    print("[s%d] L2R disc4_h1=%.3f k=%d beh r/100=%.3f harm=%.2f upd=%d grad=%s t=%.0fs" % (
        S, ev["disc4_h1"], ev["k"], beh["reward_per_100"], beh["harm_events_per_100"], full["updates_done"],
        full["grad_nonnull_first"], time.time() - t0), flush=True)


if __name__ == "__main__":
    main()
