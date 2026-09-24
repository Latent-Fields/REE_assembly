#!/opt/local/bin/python3
"""Act-time CALL-SITE probe for key modules (bt0925-census). Untrained agents (call sites are
structural, not training-dependent). usage: callsite_probe.py native|allon|r1078. ASCII only."""
import collections
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WT = os.path.join(HERE, "ree-v3-wt")
sys.path.insert(0, WT)
sys.path.insert(0, os.path.join(WT, "experiments"))
sys.path.insert(0, HERE)
os.chdir(WT)
import torch  # noqa: E402
torch.set_num_threads(2)
torch.manual_seed(42)
import census_instr as CI  # noqa: E402
from ree_core.agent import REEAgent  # noqa: E402
from ree_core.utils.config import REEConfig  # noqa: E402
from ree_core.environment.causal_grid_world import CausalGridWorldV2  # noqa: E402

KEYS = ["hippocampal.action_object_decoder", "hippocampal.terrain_prior", "e3.harm_eval_head",
        "e2.world_transition", "e2.self_transition", "e2.action_object_head",
        "residue_field.neural_field", "latent_stack.self_recurrence", "latent_stack.beta_encoder",
        "latent_stack.split_encoder.world_topdown", "world_obs_encoder", "body_obs_encoder",
        "gated_policy.head_0", "gated_policy.discriminator", "ofc.state_bias_head",
        "lateral_pfc.rule_bias_head", "e1.prior_generator", "e1.transition_rnn"]

rec = sys.argv[1]
if rec == "native":
    env = CausalGridWorldV2(seed=42)
    agent = REEAgent(REEConfig.from_dims(body_obs_dim=env.body_obs_dim,
                                         world_obs_dim=env.world_obs_dim, action_dim=env.action_dim))
elif rec == "r1078":
    x = importlib.import_module("experiments.v3_exq_1078_inv069_zself_coherence_unsettled")
    env = x._make_env(42)
    agent = REEAgent(REEConfig.from_dims(**dict(x.CFG_KW, body_obs_dim=env.body_obs_dim,
                                                world_obs_dim=env.world_obs_dim,
                                                action_dim=env.action_dim)))
else:
    x1002 = importlib.import_module("experiments.v3_exq_1002_zworld_actor_adequacy_oracle_adapter")
    x734 = importlib.import_module("experiments.v3_exq_734_env_difficulty_competence_recovery_sweep")
    env = x734._make_env(42, x734._env_kwargs_for_rung(x1002.RUNG))
    agent = x1002._make_agent(env)

mods = dict(agent.named_modules())
sites = collections.defaultdict(collections.Counter)


def mk(n):
    def h(m, i, o):
        sites[n][CI._site_chain(3)] += 1
    return h


for k in KEYS:
    if k in mods and mods[k] is not None:
        mods[k].register_forward_hook(mk(k))
wd = agent.config.latent.world_dim
_, obs = env.reset()
agent.reset()
with torch.no_grad():
    for _ in range(12):
        latent = agent.sense(torch.as_tensor(obs["body_state"], dtype=torch.float32),
                             torch.as_tensor(obs["world_state"], dtype=torch.float32))
        ticks = agent.clock.advance()
        e1p = agent._e1_tick(latent) if ticks["e1_tick"] else torch.zeros(1, wd)
        a = agent.select_action(agent.generate_trajectories(latent, e1p, ticks), ticks)
        _, r, done, info, obs = env.step(a)
        if done:
            _, obs = env.reset()
print("recipe=%s" % rec)
for k in KEYS:
    if k not in mods or mods[k] is None:
        print("  %-42s ABSENT" % k)
        continue
    top = sites[k].most_common(3)
    print("  %-42s calls=%d" % (k, sum(sites[k].values())))
    for s, c in top:
        print("      %4d  %s" % (c, s))
