#!/opt/local/bin/python3
"""Gradient-reach census probe (bt0925-census, chip-20260925-gradient-reach-census).

usage: cd <ree-v3 worktree> && /opt/local/bin/python3 census_probe.py <recipe> [seed]
recipes:
  native   REEConfig.from_dims defaults (world_dim 32). 40 StepHarness ticks (train_mode), then ONE
           backward of every native agent.compute_*_loss that can be called (reach only, no step).
  r1078    V3-EXQ-1078 P0 recipe verbatim: DR-13 config, Adam(agent.parameters()) on
           compute_prediction_loss()+compute_e2_loss() per StepHarness tick (2 eps x 40 steps).
  r1083    V3-EXQ-1083 recipe: mech477 baseline build_arm_agent(ARM_ON) +
           goal_pipeline_tier1.warmup_train (2 eps x 60 steps, one familiar layout).
  allon    all-ON stack (x1002._make_agent, as V3-EXQ-1043b/1002/1008/1010) +
           x734._train_all_on_agent incl. SD-070 run_zworld_p0 (dry_run batch scaling),
           p0=1 p1=1 episodes x 40 steps.
  zselfp0  V3-EXQ-1078 DR-13 config + run_zself_p0 (863d23d, dry_run batch scaling), 2 eps x 40.
Budgets are tiny on purpose: this measures REACH (which tensors a recipe's losses/optimizers can
move), not training quality. Each recipe loop is run long enough that every one of its optimizers
steps at least once (step counts are recorded; a recipe optimizer with 0 steps is reported).
Then: an ACT-TIME READ pass (12 act steps in a fresh env, no_grad) recording which parameters are
touched by any torch function and which submodules' forward is called.
ASCII-only output.
"""
import json
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
WT = os.path.join(HERE, "ree-v3-wt")
sys.path.insert(0, WT)
sys.path.insert(0, os.path.join(WT, "experiments"))
sys.path.insert(0, HERE)
os.chdir(WT)

import torch  # noqa: E402
torch.set_num_threads(2)
import numpy as np  # noqa: E402

import census_instr as CI  # noqa: E402

CI.install()

from ree_core.agent import REEAgent  # noqa: E402
from ree_core.utils.config import REEConfig  # noqa: E402
from ree_core.environment.causal_grid_world import CausalGridWorldV2  # noqa: E402
from experiments._harness import StepHarness  # noqa: E402

RECIPE = sys.argv[1]
SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 42
OUT = os.path.join(HERE, "results")
os.makedirs(OUT, exist_ok=True)


def seed_all(s):
    torch.manual_seed(s)
    random.seed(s)
    np.random.seed(s)


def act_steps(agent, env, n=12):
    """Pure act path (template: arc021_h2_merged_leg_param_reach_probe.py)."""
    wd = agent.config.latent.world_dim
    _, obs = env.reset()
    agent.reset()
    for _ in range(n):
        latent = agent.sense(torch.as_tensor(obs["body_state"], dtype=torch.float32),
                             torch.as_tensor(obs["world_state"], dtype=torch.float32))
        ticks = agent.clock.advance()
        e1p = agent._e1_tick(latent) if ticks["e1_tick"] else torch.zeros(1, wd)
        a = agent.select_action(agent.generate_trajectories(latent, e1p, ticks), ticks)
        _, r, done, info, obs = env.step(a)
        if done:
            _, obs = env.reset()


def native_loss_reach(agent, env):
    """One backward per callable native loss. Reach only; no optimizer step."""
    out = {}
    harness = StepHarness(agent, env, train_mode=True, seed=SEED)
    _, obs = env.reset()
    agent.reset()
    harness.reset()
    agent.train()
    last = None
    for _ in range(40):
        r = harness.step(obs)
        last = r
        obs = r.next_obs_dict
        if r.done:
            _, obs = env.reset()
    # a LIVE (undetached) latent for the latent-taking auxiliaries
    live = agent.sense(torch.as_tensor(obs["body_state"], dtype=torch.float32),
                       torch.as_tensor(obs["world_state"], dtype=torch.float32))
    calls = {
        "compute_prediction_loss": lambda: agent.compute_prediction_loss(),
        "compute_e2_loss": lambda: agent.compute_e2_loss(),
        "compute_e2_world_loss": lambda: agent.compute_e2_world_loss(),
        "compute_self_maintenance_loss": lambda: agent.compute_self_maintenance_loss(),
        "compute_benefit_eval_loss": lambda: agent.compute_benefit_eval_loss(torch.tensor([[0.5]])),
        "compute_event_contrastive_loss": lambda: agent.compute_event_contrastive_loss("none", live),
        "compute_resource_proximity_loss": lambda: agent.compute_resource_proximity_loss(0.5, live),
        "compute_resource_field_loss": lambda: agent.compute_resource_field_loss(
            torch.zeros(1, 4), live),
        "compute_resource_encoder_loss": lambda: agent.compute_resource_encoder_loss(0.5, live),
        "compute_resource_identity_loss": lambda: agent.compute_resource_identity_loss(0, live),
        "compute_harm_nonredundancy_loss": lambda: agent.compute_harm_nonredundancy_loss(live),
        "compute_harm_accum_loss": lambda: agent.compute_harm_accum_loss(0.5, live),
        "compute_schema_readout_loss": lambda: agent.compute_schema_readout_loss(0.5),
    }
    name_of = {id(p): n for n, p in agent.named_parameters()}
    for nm, fn in calls.items():
        try:
            loss = fn()
        except Exception as exc:  # cannot-determine category, recorded, not silenced
            out[nm] = {"status": "CANNOT_CALL", "reason": ("%s: %s" % (type(exc).__name__, exc))[:200]}
            continue
        if loss is None or not isinstance(loss, torch.Tensor):
            out[nm] = {"status": "RETURNED_NONE"}
            continue
        if not loss.requires_grad:
            out[nm] = {"status": "NO_GRAD", "value": float(loss.detach().sum())}
            continue
        agent.zero_grad(set_to_none=True)
        try:
            loss.backward(retain_graph=True)
        except Exception as exc:
            out[nm] = {"status": "BACKWARD_FAILED", "reason": str(exc)[:200]}
            continue
        hit = {}
        for n, p in agent.named_parameters():
            if p.grad is not None and float(p.grad.abs().sum()) > 0:
                top = ".".join(n.split(".")[:2])
                hit[top] = hit.get(top, 0) + 1
        out[nm] = {"status": "REACH", "value": float(loss.detach().sum()), "modules": hit}
    agent.zero_grad(set_to_none=True)
    return out


def build_and_train():
    meta = {}
    if RECIPE == "native":
        env = CausalGridWorldV2(seed=SEED)
        cfg = REEConfig.from_dims(body_obs_dim=env.body_obs_dim, world_obs_dim=env.world_obs_dim,
                                  action_dim=env.action_dim)
        agent = REEAgent(cfg)
        CI.track(agent)
        snap = CI.snapshot(agent)
        meta["native_loss_reach"] = native_loss_reach(agent, env)
        return agent, env, snap, meta
    if RECIPE in ("r1078", "zselfp0"):
        import importlib
        x = importlib.import_module("experiments.v3_exq_1078_inv069_zself_coherence_unsettled")
        env = x._make_env(SEED)
        _, obs = env.reset()
        cfg = REEConfig.from_dims(**dict(x.CFG_KW, body_obs_dim=env.body_obs_dim,
                                          world_obs_dim=env.world_obs_dim, action_dim=env.action_dim))
        agent = REEAgent(cfg)
        assert agent.latent_stack.self_recurrence is not None
        CI.track(agent)
        snap = CI.snapshot(agent)
        if RECIPE == "r1078":
            opt = torch.optim.Adam(agent.parameters(), lr=x.LR)
            harness = StepHarness(agent, env, train_mode=True, seed=SEED)
            agent.train()
            nstep = 0
            for ep in range(2):
                _, obs = env.reset(); agent.reset(); harness.reset()
                for _t in range(40):
                    r = harness.step(obs); obs = r.next_obs_dict
                    loss = agent.compute_prediction_loss() + agent.compute_e2_loss()
                    if loss.requires_grad:
                        opt.zero_grad(); loss.backward(); opt.step(); nstep += 1
                    if r.done:
                        break
            meta["opt_steps"] = nstep
        else:
            from experiments._lib.zself_p0_warmup import run_zself_p0
            from experiments._lib.capability_eval import RandomPolicy
            wenv = x._make_env(SEED)
            meta["zself_p0"] = run_zself_p0(agent, wenv, SEED, 2, 40, policy=RandomPolicy(SEED),
                                            label="census", dry_run=True)
        return agent, env, snap, meta
    if RECIPE == "r1083":
        from experiments._lib.baselines import mech477_dualsystem_arbitration as LIN
        from experiments._lib.goal_pipeline_tier1 import warmup_train
        agent, cfg = LIN.build_arm_agent(LIN.ARM_ON)
        CI.track(agent)
        snap = CI.snapshot(agent)
        env = CausalGridWorldV2(seed=LIN.FAMILIAR_ENV_SEEDS[0], **LIN.FAMILIAR_ENV_KWARGS)
        meta["warmup"] = {k: (float(v) if isinstance(v, (int, float)) else str(v)) for k, v in
                          (warmup_train(agent, env, num_episodes=2, steps_per_episode=60,
                                        label="census") or {}).items()}
        return agent, env, snap, meta
    if RECIPE == "allon":
        import importlib
        x1002 = importlib.import_module("experiments.v3_exq_1002_zworld_actor_adequacy_oracle_adapter")
        x734 = importlib.import_module("experiments.v3_exq_734_env_difficulty_competence_recovery_sweep")
        env_kwargs = x734._env_kwargs_for_rung(x1002.RUNG)
        env = x734._make_env(SEED, env_kwargs)
        agent = x1002._make_agent(env)
        CI.track(agent)
        snap = CI.snapshot(agent)
        res = x734._train_all_on_agent(
            agent, env, seed=SEED, p0_episodes=1, p1_episodes=int(os.environ.get("CENSUS_ALLON_P1", "1")), steps_per_episode=int(os.environ.get("CENSUS_ALLON_STEPS", "40")),
            rung_id="census", total_denominator=2, zworld_p0_episodes=2,
            zworld_p0_env=x734._make_env(SEED, env_kwargs), zworld_p0_dry_run=True,
            zworld_p0_resource_field_weight=0.0)
        meta["allon_keys"] = sorted(list(res.keys()))[:80] if isinstance(res, dict) else str(type(res))
        for k in ("n_e2_train_steps", "zworld_p0"):
            if isinstance(res, dict) and k in res:
                meta[k] = str(res[k])[:400]
        return agent, env, snap, meta
    raise SystemExit("unknown recipe %s" % RECIPE)


def main():
    t0 = time.time()
    seed_all(SEED)
    agent, env, snap, meta = build_and_train()
    t_train = time.time() - t0
    # ---- act-time read pass (fresh env instance of the same kind, no_grad) -------------
    pids = {id(p) for p in agent.parameters()}
    called, handles = CI.module_forward_hooks(agent)
    mode = CI.ParamReadMode(pids)
    act_err = None
    try:
        env2 = type(env)(**{}) if False else env
        with torch.no_grad():
            with mode:
                act_steps(agent, env2, n=12)
    except Exception as exc:
        act_err = "%s: %s" % (type(exc).__name__, str(exc)[:300])
    for h in handles:
        h.remove()
    rows = CI.classify(agent, snap, read_pids=mode.hit)
    out = {
        "recipe": RECIPE, "seed": SEED,
        "ree_v3_sha": os.popen("git -C %s rev-parse --short=10 HEAD" % WT).read().strip(),
        "world_dim": int(agent.config.latent.world_dim),
        "self_dim": int(agent.config.latent.self_dim),
        "use_self_recurrence": bool(getattr(agent.config.latent, "use_self_recurrence", False)),
        "train_seconds": round(t_train, 1),
        "act_error": act_err,
        "meta": meta,
        "optimizers": [dict(site=v["site"], cls=v["cls"], n_params=len(v["param_ids"]))
                       for v in CI.STATE["optimizers"].values()],
        "backward_sites": dict(CI.STATE["backward_sites"]),
        "act_module_calls": dict(called),
        "rows": rows,
    }
    path = os.path.join(OUT, "census_%s%s_s%d.json" % (RECIPE, os.environ.get("CENSUS_TAG", ""), SEED))
    with open(path, "w") as f:
        json.dump(out, f, indent=1, default=str)
    n = len(rows)
    n_moved = sum(1 for r in rows if (r["param_delta_max"] or 0) > 0)
    n_read = sum(1 for r in rows if r["read_at_act"])
    print("recipe=%s tensors=%d moved=%d read_at_act=%d optimizers=%d backward_sites=%d "
          "train_s=%.1f act_err=%s -> %s" % (RECIPE, n, n_moved, n_read, len(out["optimizers"]),
                                             len(out["backward_sites"]), t_train, act_err, path))


if __name__ == "__main__":
    main()
