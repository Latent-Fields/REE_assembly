"""Probe 1 -- LOSS -> PARAMETERS reach for the z_self recognition path.

For each loss the native agent / production drivers step, which parameters get a
NONZERO gradient, and does any of them sit on the z_self path (self_encoder,
self_topdown, self_precision_logit, self_recurrence GRU)? Also: optimizer-group
membership of the z_self path in the production all-ON recipe (x724 / allon_training).
Seed 42, 40 grad-enabled StepHarness ticks to fill the replay buffers. Writes nothing.
"""
import sys, collections
sys.path.insert(0, "/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/zself")
from zs_common import *
import torch.nn.functional as F


def reach(agent, loss):
    agent.zero_grad(set_to_none=True)
    if not isinstance(loss, torch.Tensor) or not loss.requires_grad:
        return None, []
    loss.backward(retain_graph=True)
    c = collections.Counter(); selfp = []
    sp = set(self_param_names(agent))
    for n, p in agent.named_parameters():
        if p.grad is not None and float(p.grad.abs().sum()) > 0:
            c[n.split(".")[0]] += 1
            if n in sp:
                selfp.append(n)
    return dict(c), selfp


def run(kind, dr13):
    agent, env, cfg = build(kind, 42, dr13=dr13)
    agent.train()
    h = StepHarness(agent, env, train_mode=True, seed=42)
    _, obs = env.reset(); agent.reset(); h.reset()
    last = None
    for t in range(40):
        r = h.step(obs); obs = r.next_obs_dict; last = r
        if r.done:
            _, obs = env.reset(); agent.reset(); h.reset()
    lat = last.latent
    print("==== config", kind, "dr13" if (dr13 or kind == "A") else "dr13-OFF",
          "| self-path params:", len(self_param_names(agent)),
          "| GRU present:", agent.latent_stack.self_recurrence is not None)
    print("  live latent from sense(): z_self.requires_grad=", bool(lat.z_self.requires_grad),
          " _current_latent.z_self.requires_grad=", bool(agent._current_latent.z_self.requires_grad))
    losses = {}
    losses["E1 compute_prediction_loss"] = lambda: agent.compute_prediction_loss()
    losses["E2 compute_e2_loss (self)"] = lambda: agent.compute_e2_loss()
    losses["E2 compute_e2_world_loss"] = lambda: agent.compute_e2_world_loss()
    def _maint():
        old = agent.config.e3.self_maintenance_weight
        agent.config.e3.self_maintenance_weight = 1.0
        try:
            return agent.compute_self_maintenance_loss()
        finally:
            agent.config.e3.self_maintenance_weight = old
    losses["MECH-113 compute_self_maintenance_loss (w=1)"] = _maint
    if lat.z_harm_a is not None:
        losses["SD-011 compute_harm_accum_loss(live latent)"] = lambda: agent.compute_harm_accum_loss(0.5, lat)
    if getattr(lat, "resource_prox_pred", None) is not None:
        losses["SD-018 compute_resource_proximity_loss(live latent)"] = lambda: agent.compute_resource_proximity_loss(0.5, lat)
    losses["E3 harm_eval(live z_world) [undetached world-side probe]"] = lambda: F.mse_loss(agent.e3.harm_eval(lat.z_world), torch.zeros(1, 1))
    losses["E3 harm_eval(z_world.detach())"] = lambda: F.mse_loss(agent.e3.harm_eval(lat.z_world.detach()), torch.zeros(1, 1))
    losses["SYNTHETIC sum(live latent.z_self) [upper bound of reach]"] = lambda: lat.z_self.sum()
    losses["SYNTHETIC sum(_current_latent.z_self)"] = lambda: agent._current_latent.z_self.sum()
    if agent.e2 is not None and hasattr(agent.e2, "world_forward_contrastive_loss"):
        pass  # SD-056 contrastive: e2-only optimizer + clip in allon_training (code-read)
    for name, fn in losses.items():
        try:
            c, sp = reach(agent, fn())
        except Exception as ex:  # report, never hide
            print("  %-58s ERROR %s" % (name, str(ex)[:120])); continue
        if c is None:
            print("  %-58s NO GRAD (no graph)" % name); continue
        print("  %-58s modules=%s" % (name, c))
        print("  %-58s   z_self-path params reached: %d %s" % ("", len(sp), sorted(set(x.split('.')[-2] if x.count('.') > 1 else x for x in sp))))
    return agent


run("A", True)
agB = run("B", False)
run("B", True)

# Production recipe optimizer membership (allon_training._train_all_on_agent + SD-070 + SD-011 P0h)
sp = set(id(p) for n, p in agB.named_parameters() if n in set(self_param_names(agB)))
groups = {"e2_opt (agent.e2)": list(agB.e2.parameters())}
if getattr(agB, "lateral_pfc", None) is not None:
    groups["bias_opt (lpfc bias head)"] = list(agB.lateral_pfc.bias_head_parameters())
if getattr(agB, "ofc", None) is not None:
    groups["ofc_deval_opt"] = list(agB.ofc.devaluation_bias_head_parameters())
from ree_core.latent.zworld_p0 import ZWorldP0Trainer
tr = ZWorldP0Trainer(agB.latent_stack)
groups["SD-070 ZWorldP0Trainer world_path_parameters"] = tr.world_path_parameters()
print("==== production all-ON optimizer groups vs z_self path (config B, DR-13 OFF)")
for g, ps in groups.items():
    print("  %-48s n=%4d  z_self-path members=%d" % (g, len(ps), sum(1 for p in ps if id(p) in sp)))
