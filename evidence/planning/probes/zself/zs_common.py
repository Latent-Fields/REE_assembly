"""Shared builders for the z_self causal-reach probes (bt0924-zself-trace).

Run with cwd = the throwaway ree-v3 worktree (so ree_core / experiments resolve there).
Two configs:
  A  = V3-EXQ-1078 config (DR-13 ON, per-stream V_s), CausalGridWorldV2 size 10.
  B  = V3-EXQ-724 all-ON production stack (x724 _base_config_kwargs + _all_on_extra_kwargs),
       x724 ENV_KWARGS (size 12 reef world). DR-13 OFF as in production unless dr13=True.
Dims: self_dim=32, world_dim=32 in both (the deployed values).
"""
import os, sys, copy, random
from pathlib import Path
WT = Path(os.environ.get("ZS_WT", "/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/zself/ree-v3-wt"))
sys.path.insert(0, str(WT))
import numpy as np
import torch
torch.set_num_threads(2)
from ree_core.agent import REEAgent
from ree_core.utils.config import REEConfig
from ree_core.environment.causal_grid_world import CausalGridWorldV2
from experiments._harness import StepHarness

A_ENV = dict(size=10, num_hazards=2, num_resources=5, hazard_harm=0.1, contaminated_harm=0.0)
A_CFG = dict(self_dim=32, world_dim=32, alpha_world=0.9,
             use_self_recurrence=True, self_recurrence_e1_coupling=0.15,
             use_per_stream_vs=True)


def build(kind, seed, dr13=False):
    torch.manual_seed(seed); random.seed(seed); np.random.seed(seed)
    if kind == "A":
        env = CausalGridWorldV2(seed=seed, **A_ENV)
        kw = dict(A_CFG, body_obs_dim=env.body_obs_dim, world_obs_dim=env.world_obs_dim,
                  action_dim=env.action_dim)
        cfg = REEConfig.from_dims(**kw)
    elif kind == "B":
        import experiments.v3_exq_724_competence_localization_diagnostic as x724
        env = x724._make_env(seed)
        kw = x724._base_config_kwargs(env)
        kw.update(x724._all_on_extra_kwargs())
        if dr13:
            kw.update(use_self_recurrence=True, self_recurrence_e1_coupling=0.15)
        cfg = REEConfig.from_dims(**kw)
    else:
        raise ValueError(kind)
    agent = REEAgent(cfg)
    return agent, env, cfg


def dcopy(obj):
    memo = {}
    hip = getattr(obj, "hippocampal", None)
    rng = getattr(hip, "_rng", None)
    if rng is not None:
        memo[id(rng)] = rng
    return copy.deepcopy(obj, memo)


def rng_snap():
    return (torch.get_rng_state(), np.random.get_state(), random.getstate())


def rng_restore(s):
    torch.set_rng_state(s[0]); np.random.set_state(s[1]); random.setstate(s[2])


def self_param_names(agent):
    """Parameter names on the z_self recognition path (the build's targets)."""
    out = []
    for n, _ in agent.named_parameters():
        if (".self_encoder." in n or ".self_recurrence." in n or ".self_topdown." in n
                or n.endswith("self_precision_logit") or ".self_predictor." in n):
            out.append(n)
    return out
