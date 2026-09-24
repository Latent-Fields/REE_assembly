"""R5 precheck: does an uninformative CEM initial mean (R5a) un-collapse the proposal? ASCII only."""
import sys, json
from collections import Counter
from pathlib import Path
import numpy as np, torch
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "ree-v3-wt")); sys.path.insert(0, str(HERE / "ree-v3-wt" / "experiments")); sys.path.insert(0, str(HERE))
torch.set_num_threads(2)
import rollout_fidelity_probe as R
from experiments._lib.zworld_p0_warmup import run_zworld_p0
from experiments._lib.capability_eval import RandomPolicy
from ree_core.latent.zworld_p0 import ZWorldP0Config
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 43
R.seed_all(seed)
env, agent, cfg = R.build_B(seed, False)
run_zworld_p0(agent, R.build_B(seed, False)[0], seed=seed, episodes=20, steps_per_episode=50, policy=RandomPolicy(seed),
              label="pre", dry_run=False, config=ZWorldP0Config(preservation_weight=1000.0))
agent.eval()
rec, log, harm = R.waking(agent, env, 150, seed)
hip = agent.hippocampal
orig = hip._get_terrain_action_object_mean
def zero_mean(z_world, e1_prior=None):
    m = orig(z_world, e1_prior=e1_prior)
    return torch.zeros_like(m)
for name, fn in (("native", None), ("R5a_zero", zero_mean)):
    hip._get_terrain_action_object_mean = fn if fn is not None else orig
    m4 = R.m4_proposal(agent, log, 20, [], seed)["native"]
    hip._get_terrain_action_object_mean = orig
    print(name, json.dumps({k: m4[k] for k in ("maj_share_mean", "n_classes_mean", "frac_states_with_modal_majority", "majority_class_counts_across_states")}))
# decoder bias check
with torch.no_grad():
    dec = hip.action_object_decoder
    x = torch.randn(4000, hip.config.action_object_dim)
    print("decoder argmax on N(0,1):", dict(Counter(dec(x).argmax(-1).tolist())), " on 0:", int(dec(torch.zeros(1, hip.config.action_object_dim)).argmax()))
