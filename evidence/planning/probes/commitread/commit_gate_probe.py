"""Pre-A1 H1-lite probe (chip-20260926-commit-gate-read-int-vs-native): rv trace and
commit occupancy under NATIVE vs INT-CODEC vs NATIVE-NOKNOBS; plus a cheap D1 check of
GFLAG-0486 (is rv E2's realised one-step error, or its predicted displacement?).

Report-only. Does NOT change the 0.40 commit bar. No ree_core edits.

Usage: commit_gate_probe.py <tree> <steps> <seed> [<seed>...]
"""
import sys, os, time, json
import numpy as np
import torch

tree, steps = sys.argv[1], int(sys.argv[2])
seeds = [int(s) for s in sys.argv[3:]]
sys.path.insert(0, tree)
sys.path.insert(0, os.path.join(tree, "experiments"))
torch.set_num_threads(2)

from ree_core.agent import REEAgent
from ree_core.environment.causal_grid_world import CausalGridWorldV2
from ree_core.utils.config import REEConfig
from _harness import StepHarness

MAX_EP_STEPS = 200


def make_env(seed):
    return CausalGridWorldV2(
        size=8, num_hazards=3, num_resources=2, hazard_harm=0.5,
        seed=seed, max_episode_steps=MAX_EP_STEPS,
    )


KNOBS_ON = dict(
    use_zworld_ema_reset_init=True, use_zself_ema_reset_init=True,
    use_shared_ema_reset_init=True, use_zharm_ema_reset_init=True,
)
KNOBS_OFF = dict(
    use_zworld_ema_reset_init=False, use_zself_ema_reset_init=False,
    use_shared_ema_reset_init=False, use_zharm_ema_reset_init=False,
)

ARM_FLAGS = {
    # NATIVE per orchestrator 13:40Z provisional decision: reset-init knobs ON,
    # no waking trainer (no members).
    "NATIVE": dict(KNOBS_ON),
    # Reference: NATIVE with knobs OFF too (the literal "all flags off" row).
    "NATIVE_NOKNOBS": dict(KNOBS_OFF),
    # INT-CODEC per v3c member roster sec 1: HarmEvalMember (always-on member
    # of the trainer), E1Member, E2SelfMember, CodecMember (+ bounded decode +
    # iter0 image match), E2WorldMember (W3), WorldEncoderMember (W6a), E3
    # discounted aggregation (W4). Knobs ON (same asymmetry as NATIVE row
    # above -- P8/C.4 obs 2: as written the branch has knobs ON in INT arms).
    "INT_CODEC": dict(
        KNOBS_ON,
        waking_trainer_enabled=True,
        waking_trainer_e1_enabled=True,
        waking_trainer_e2_self_enabled=True,
        waking_trainer_codec_enabled=True,
        waking_trainer_e2_world_enabled=True,
        waking_trainer_world_encoder_enabled=True,
        use_e3_discounted_aggregation=True,
        use_codec_bounded_decode=True,
        use_codec_iter0_image_match=True,
    ),
}


def run_arm(arm, seed, steps):
    env0 = make_env(seed)
    flags = ARM_FLAGS[arm]
    cfg = REEConfig.from_dims(
        body_obs_dim=env0.body_obs_dim, world_obs_dim=env0.world_obs_dim,
        action_dim=env0.action_dim, self_dim=32, world_dim=32, alpha_world=0.05,
        **flags,
    )
    bar = cfg.e3.commitment_threshold
    torch.manual_seed(seed)
    np.random.seed(seed)
    agent = REEAgent(cfg)
    harness = StepHarness(agent, env0, train_mode=True, seed=seed)

    _flat, obs = env0.reset()
    agent.reset()
    harness.reset()

    rows = []
    t0 = time.time()
    for i in range(steps):
        result = harness.step(obs)
        obs = result.next_obs_dict
        cs = agent.e3.get_commitment_state()
        pe = result.residue_metrics.get("e3_prediction_error")
        pe_val = float(pe.detach().item()) if torch.is_tensor(pe) else (
            float(pe) if pe is not None else None)
        rows.append(dict(
            i=i,
            e3_tick=bool(result.ticks.get("e3_tick", False)),
            rv=float(cs["running_variance"]),
            committed=bool(cs["committed_now"]),
            pred_err=pe_val,
            z_world_norm=float(result.latent.z_world.detach().norm()),
        ))
        if result.done:
            _flat, obs = env0.reset()
            agent.reset()
            harness.reset()
            if agent.waking_trainer is not None:
                agent.waking_trainer.on_env_reset()
    secs = time.time() - t0
    return dict(arm=arm, seed=seed, bar=float(bar), steps=steps, secs=secs, rows=rows)


def summarize(run):
    rows = run["rows"]
    rv = np.array([r["rv"] for r in rows])
    committed = np.array([r["committed"] for r in rows])
    znorm = np.array([r["z_world_norm"] for r in rows])
    e3_ticks = np.array([r["e3_tick"] for r in rows])
    qs = np.quantile(rv, [0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0])
    # first tick (if any) where committed goes permanently True and never
    # flips back to False again.
    perm_idx = None
    for k in range(len(committed) - 1, -1, -1):
        if not committed[k]:
            break
    else:
        k = -1
    if k + 1 < len(committed) and committed[k + 1:].all() and len(committed) - (k + 1) >= 20:
        perm_idx = k + 1
    return dict(
        arm=run["arm"], seed=run["seed"], bar=run["bar"], n=len(rows), secs=run["secs"],
        rv_quantiles=dict(zip(["min", "p10", "p25", "p50", "p75", "p90", "max"], qs.tolist())),
        commit_frac=float(committed.mean()),
        commit_frac_first_half=float(committed[: len(committed) // 2].mean()),
        commit_frac_second_half=float(committed[len(committed) // 2:].mean()),
        goes_permanent_at=perm_idx,
        z_world_norm_mean=float(znorm.mean()),
        n_e3_ticks=int(e3_ticks.sum()),
    )


def d1_check(run, n_examples=8):
    """GFLAG-0486 D1 check: is pred_err (rv's raw input, error_var) the
    self-referential displacement computed ON an E3 tick, a genuine one-step
    error the tick right AFTER an E3 tick, or drift-against-a-stale-prediction
    on later ticks? Classify each row by ticks-since-last-e3-tick and report
    the mean pred_err per class -- the P6 premise correction predicts these
    differ systematically (small/self-consistent at k=0, a real jump at k=1,
    then drifting upward for k>=2 until the next E3 tick)."""
    rows = run["rows"]
    since = None
    classes = {}
    for r in rows:
        if r["e3_tick"]:
            since = 0
        elif since is not None:
            since += 1
        if r["pred_err"] is None or since is None:
            continue
        k = min(since, 5)  # bucket 5+ together
        classes.setdefault(k, []).append(r["pred_err"])
    return {k: (float(np.mean(v)), len(v)) for k, v in sorted(classes.items())}


if __name__ == "__main__":
    all_summaries = []
    all_d1 = []
    out_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(out_dir, exist_ok=True)
    for seed in seeds:
        for arm in ("NATIVE", "INT_CODEC", "NATIVE_NOKNOBS"):
            run = run_arm(arm, seed, steps)
            s = summarize(run)
            d1 = d1_check(run)
            all_summaries.append(s)
            all_d1.append(dict(arm=arm, seed=seed, d1=d1))
            print(json.dumps(s), flush=True)
            print("D1[%s seed %d]: %s" % (arm, seed, d1), flush=True)
            with open(os.path.join(out_dir, "%s_seed%d.json" % (arm, seed)), "w") as f:
                json.dump(run, f)
    with open(os.path.join(out_dir, "summary.json"), "w") as f:
        json.dump(dict(summaries=all_summaries, d1=all_d1), f, indent=2)
    print("DONE. wrote %s" % out_dir, flush=True)
