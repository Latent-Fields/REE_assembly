"""Harness-sizing pilot (seed 99, NOT a registered seed): step cost + obs dims only."""
import sys, time
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "ree-v3-wt")); sys.path.insert(0, str(HERE / "ree-v3-wt" / "experiments")); sys.path.insert(0, str(HERE / "probes_src"))
import torch
torch.set_num_threads(2)
from ree_core.agent import REEAgent
from ree_core.utils.config import REEConfig
from ree_core.environment.causal_grid_world import CausalGridWorldV2
from infant_curriculum import InfantCurriculumScheduler
import v3_exq_591h_isef005_phase01_gate_live_v3 as X
import v3_exq_591_isef005_curriculum_vs_flat_v3 as X0
from experiments._harness import StepHarness
import rollout_fidelity_probe as R
S = 99
torch.manual_seed(S)
ag = X._build_diversity_agent()
print("591c world_dim", ag.config.latent.world_dim, "action_dim", ag.config.e2.action_dim)
sched = InfantCurriculumScheduler(grid_size=X0.GRID_SIZE)
env = CausalGridWorldV2(size=X0.GRID_SIZE, seed=S * 160, resource_respawn_on_consume=True, pos_telemetry_enabled=True, traj_telemetry_enabled=True, **sched.env_kwargs())
print("grid", X0.GRID_SIZE, "env body/world/action", env.body_obs_dim, env.world_obs_dim, env.action_dim, "max_ep", env.max_episode_steps)
_f, od = env.reset(); ob, ow = X0._extract_obs(od)
t = time.time(); acts = []
for i in range(300):
    with torch.no_grad():
        a = ag.act_with_split_obs(obs_body=ob, obs_world=ow)
    ai = int(a.argmax().item()) % 4; acts.append(ai)
    _o, h, done, info, od = env.step(ai); ag.update_residue(float(h)); ob, ow = X0._extract_obs(od)
    if done:
        _f, od = env.reset(); ob, ow = X0._extract_obs(od)
print("591c act s/step %.4f" % ((time.time() - t) / 300), "counts", dict(Counter(acts)), "h_pos", info.get("pos_entropy"))
envB, agB, cfgB = R.build_B(S, False)
print("B env body/world/action", envB.body_obs_dim, envB.world_obs_dim, envB.action_dim)
h = StepHarness(agB, envB, train_mode=False, seed=S)
_f, obs = envB.reset(); agB.reset(); h.reset()
t = time.time(); acts = []
for i in range(300):
    r = h.step(obs); obs = r.next_obs_dict; acts.append(int(r.action.reshape(-1).argmax()))
    if r.done:
        _f, obs = envB.reset(); agB.reset(); h.reset()
print("B waking s/step %.4f" % ((time.time() - t) / 300), "counts", dict(Counter(acts)))
t = time.time()
for i in range(300):
    with torch.no_grad():
        agB.sense(obs["body_state"], obs["world_state"])
print("B sense s/step %.4f" % ((time.time() - t) / 300))
