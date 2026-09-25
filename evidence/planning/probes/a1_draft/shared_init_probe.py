"""A1 v3 O12 shared-init check (bt0925-a1v3). Construction only -- no env steps, no training.

Question: can INT and NATIVE get the SAME init for their shared modules harness-side, or does a
flag-on module consume the global RNG at construction and shift every later native module's init
(so that a ree_core knob is needed)?

For each flag set F (flags on origin/main that construct extra modules inside REEAgent.__init__):
  (1) naive: seed_all(s); NATIVE = REEAgent(default).  seed_all(s); INT_F = REEAgent(F).
      Count shared state_dict keys (same name, same shape) whose tensors differ -> RNG-shift evidence.
      Record the index of the first INT-only parameter in INT_F's registration order.
  (2) harness copy: seed_all(s); NATIVE.  seed_all(s + INT_ONLY_OFFSET); INT_F.  Copy every shared
      same-shape key from NATIVE's state_dict into INT_F (load_state_dict strict=False).
      Verify every shared key is bit-equal afterwards; list shared-name keys with a SHAPE mismatch
      (those cannot be shared harness-side and would need a ree_core change).
ASCII output only. 2 torch threads.
"""
import random
import sys

import numpy as np
import torch

torch.set_num_threads(2)
sys.path.insert(0, ".")
from ree_core.agent import REEAgent  # noqa: E402
from ree_core.environment.causal_grid_world import CausalGridWorldV2  # noqa: E402
from ree_core.utils.config import REEConfig  # noqa: E402

INT_ONLY_OFFSET = 20_000


def seed_all(s):
    random.seed(s)
    np.random.seed(s)
    torch.manual_seed(s)


def build(env, **latent_flags):
    cfg = REEConfig.from_dims(body_obs_dim=env.body_obs_dim, world_obs_dim=env.world_obs_dim,
                              action_dim=env.action_dim)
    for k, v in latent_flags.items():
        obj, name = (cfg.latent, k[len("latent."):]) if k.startswith("latent.") else (cfg, k)
        setattr(obj, name, v)
    assert cfg.latent.world_dim == 32, cfg.latent.world_dim
    return REEAgent(cfg)


def compare(nat_sd, int_sd):
    shared = [k for k in nat_sd if k in int_sd and nat_sd[k].shape == int_sd[k].shape]
    shape_mismatch = [k for k in nat_sd if k in int_sd and nat_sd[k].shape != int_sd[k].shape]
    differ = [k for k in shared if nat_sd[k].is_floating_point() and not torch.equal(nat_sd[k], int_sd[k])]
    return shared, shape_mismatch, differ


def main():
    s = 2002
    env = CausalGridWorldV2(size=8, num_hazards=2, num_resources=3, max_episode_steps=200,
                            proximity_approach_magnitude_tiebreak=True, seed=s)
    flagsets = {
        "e2_world_uncertainty": {"latent.use_e2_world_uncertainty": True},
        "e2_harm_a": {"use_e2_harm_a": True},
        "e2_harm_s_forward": {"latent.use_e2_harm_s_forward": True},
        "all_three": {"latent.use_e2_world_uncertainty": True, "use_e2_harm_a": True,
                      "latent.use_e2_harm_s_forward": True},
    }
    seed_all(s)
    nat = build(env)
    nat_sd = {k: v.detach().clone() for k, v in nat.state_dict().items()}
    nat_names = [n for n, _ in nat.named_parameters()]
    print("NATIVE: %d params tensors, %d state_dict keys" % (len(nat_names), len(nat_sd)))
    # determinism control: NATIVE twice at the same seed must be bit-identical
    seed_all(s)
    nat2 = build(env)
    _, _, d0 = compare(nat_sd, nat2.state_dict())
    print("control NATIVE vs NATIVE same seed: %d differing shared keys" % len(d0))
    for name, fl in flagsets.items():
        seed_all(s)
        a = build(env, **fl)
        sd = a.state_dict()
        names = [n for n, _ in a.named_parameters()]
        extra = [i for i, n in enumerate(names) if n not in set(nat_names)]
        shared, mism, differ = compare(nat_sd, sd)
        first_extra = extra[0] if extra else None
        later_native = sum(1 for i, n in enumerate(names) if first_extra is not None and i > first_extra
                           and n in set(nat_names))
        print("[%s] naive same-seed: INT-only param tensors=%d first at index %s of %d; native tensors after it=%d;"
              " shared keys=%d, shape-mismatch=%d, DIFFERING shared=%d"
              % (name, len(extra), first_extra, len(names), later_native, len(shared), len(mism), len(differ)))
        if differ:
            print("   first differing shared keys: %s" % ", ".join(differ[:5]))
        if mism:
            print("   shape-mismatch keys: %s" % ", ".join(mism[:8]))
        # harness copy
        seed_all(s + INT_ONLY_OFFSET)
        b = build(env, **fl)
        sdb = b.state_dict()
        shared_b = {k: nat_sd[k] for k in nat_sd if k in sdb and nat_sd[k].shape == sdb[k].shape}
        missing, unexpected = b.load_state_dict(shared_b, strict=False)
        _, _, differ_after = compare(nat_sd, b.state_dict())
        # INT-only tensors must come from the separate generator: equal to a fresh build at s+offset
        seed_all(s + INT_ONLY_OFFSET)
        c = build(env, **fl)
        only = [k for k in sdb if k not in nat_sd]
        same_only = sum(1 for k in only if torch.equal(b.state_dict()[k], c.state_dict()[k]))
        print("   harness copy: copied=%d, differing shared after copy=%d, INT-only keys=%d (from separate gen: %d/%d)"
              % (len(shared_b), len(differ_after), len(only), same_only, len(only)))
    print("DONE")


if __name__ == "__main__":
    main()
