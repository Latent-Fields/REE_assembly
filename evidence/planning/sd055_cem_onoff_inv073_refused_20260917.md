# SD-055 `use_differentiable_cem` ON/OFF (INV-073 feedback-loop arm): REFUSED -- the gradient route is unreachable on the live agent

**Generated:** 2026-09-16T23:05:39Z
**Session:** `keen-pare-09e5ab` (chip `chip-20260916-sd055-cem-onoff-inv073-queue`, skill `/queue-experiment`)
**Source of the request:** user decision 2026-09-16 (doc-review walk, session `eloquent-jepsen-5f6242`) to queue the
"also proposed" follow-on in `thought_digestion_staged_2026-08-08_trial2_5claims.md` DRAFT 4 (INV-073): an SD-055
`use_differentiable_cem` ON vs OFF cue-conditioned trajectory-divergence experiment on a goal-rich env, the test
V3-EXQ-568's own note names as missing.
**Outcome:** REFUSED at `/queue-experiment` Step 2.5a (empirical doc-vs-runtime probe). No EXQ id reserved, no driver
written, no queue entry. Governance flag **GFLAG-0301** (`evidence_discrepancy`, claims INV-073 / ARC-072 / SD-055).

---

## 1. The premise the design needed

Both INV-073 falsifier texts route the runnable arm through one mechanism:

- staging DRAFT 4, precondition (4): "SD-055's use_differentiable_cem (default False, bit-identical off) restores a
  softmax-weighted CEM so **gradient flows from task reward back to cue_action_proj**; EXQ-568 confirmed the gradient
  flows"; CONFIRMING (a): "with use_differentiable_cem ON, a trained policy produces measurably distinct trajectory
  distributions across distinct goal cues AND higher action-class diversity than the severed (flag-off) baseline";
  FALSIFYING route 1 "LOOP NOT LOAD-BEARING".
- the APPLIED `what_would_answer` (claims.yaml, commits 8b476175070 / 680408eda4f): precondition (iii) "confirm the
  differentiable-CEM gradient is genuinely flowing (grad_max sanity check) so a null result cannot be attributed to the
  flag being silently inert", and the GOVERNANCE/QUEUE FLAG "flip use_differentiable_cem=True, measure option diversity".

So the manipulation is "restore the cue -> trajectory-generation feedback loop"; the flag is only the lever. The design
is meaningful only if flipping the flag actually connects `cue_action_proj` to a task-side gradient on a trained-policy run.

## 2. What the probe measured

Scratch probe (kept verbatim in section 5), run from `ree-v3/` on the Mac, substrate at ree-v3 `origin/main`
`45544c5` (2026-09-16): a live `REEAgent` built with `REEConfig.from_dims(..., sd016_enabled=True,
use_differentiable_cem=True, differentiable_cem_temperature=0.5)` on `CausalGridWorldV2`, driven for 40 ticks through
the production loop `agent.act(flat_obs)` (sense -> E1 tick -> generate_trajectories -> select_action).

```
flag reaches config: True T= 0.5
has cue_action_proj: True
ticks=40 ticks_with_cue_bias=40 ticks_with_candidates=40
live _cue_action_bias (requires_grad, has_grad_fn): (False, False)
live committed-candidate ao_seq (requires_grad, has_grad_fn): (True, True)
cue_action_proj.weight.grad after live ticks: None
568-recipe synthetic action_bias.grad max: 0.29671168327331543
cue_action_proj.weight.grad after 568-recipe backward: None
```

Reading, line by line:

| line | meaning |
|---|---|
| `flag reaches config: True` | The knob is wired at all three `from_dims` sites (`ree_core/utils/config.py` 2823 field, 8212 kwarg, 9616 assignment) -- NOT the `reference-reeconfig-from-dims-silent-kwargs` failure. |
| `_cue_action_bias (False, False)` | On every tick the bias the proposer receives is a leaf with no graph. `ree_core/agent.py` ~5964 calls `extract_cue_context(gated_for_e1.z_world.detach())` and ~5971 stores `self._cue_action_bias = action_bias.detach()`, with the comment "Detached: cue signals are modulation inputs, not part of current-step gradient graph" (SD-016 design). |
| `committed-candidate ao_seq (True, True)` | The SD-055 softmax-refit path IS live downstream: the candidates carry a grad graph. That graph is rooted in the proposer's own parameters and the detached bias, never in `cue_action_proj`. |
| `cue_action_proj.weight.grad: None` | No live loss reaches it. `grep` of `ree_core/` for any loss/backward touching `action_bias` or `cue_action_proj`: zero hits. `propose_trajectories` has exactly one `ree_core` call site (`agent.py:6141`, the waking select path) and no training path backprops through it. |
| `568-recipe ... 0.2967` / `weight.grad: None` | V3-EXQ-568's `grad_max=372` (UC4) and the smoke script's T1 were measured on a **synthetic** `torch.randn(..., requires_grad=True)` tensor passed straight into `propose_trajectories` ("as if NOT detached from cue_action_proj", smoke script line 83). Reproduced here: the synthetic tensor gets a gradient, `cue_action_proj.weight` still does not. 568 proved the CEM-side barrier is gone; it never touched the agent-side one. |

Independent corroboration already in the repo: the V3-EXQ-922 driver docstring ("HONEST SCOPE CAVEAT") states that its
only validated `cue_action_proj` training recipe (direct MSE supervision on a detached `z_world`, V3-EXQ-907/908
lineage) "never calls agent.hippocampal.propose_trajectories() and never routes gradient through the CEM elite-refit",
so `use_differentiable_cem=True` is "a harmless no-op under this training path", and that a driver which does route
gradient through the refit "would be a materially different, higher-engineering-risk training loop with no existing
validated recipe ... out of scope for a single-session driver build". Also `substrate_queue.json` entry
`exp0155-action-bias-scoring-disconnect` (2026-08-18, closed by GFLAG-0133 decision B): "SD-055's differentiable CEM
restored an action-sequence gradient (V3-EXQ-568 grad_max=372) with no behavioural divergence -- gradient and ranking
authority are different things".

## 3. Why this is a refusal and not a design tweak

An ON/OFF run as specified would compare the softmax-weighted refit (ON; UC5: `mean_abs_diff = 7.0e-4` from the
elite mean) against the argsort-elite refit (OFF) **with the cue -> generation feedback loop detached in both arms**.

- A divergence could not be attributed to a restored loop (there is none); it would be a refit-estimator effect.
- A null could not be read as INV-073's "LOOP NOT LOAD-BEARING" falsification, because the loop was never live.
- The applied falsifier's own guard (iii) -- "so a null result cannot be attributed to the flag being silently inert" --
  is exactly the condition that fails: for the feedback-loop purpose the flag IS silently inert on every trained-policy path.

That is the Step 2.5a gate verbatim ("the feature is not actually reachable/wired despite an IMPLEMENTED/VALIDATED doc
status") and the Step 4.5 family "the manipulation cannot reach the DV". Queueing it would produce a citable artifact
that answers nothing (memory `feedback_precondition_can_dominate_its_criterion`; V3-EXQ-604c class).

Work-graph classification: the node is **not** `complex (probe-gated)` -- the probe above IS the spike and it
converted the node. What remains is `complicated (buildable)` substrate (an agent-side gradient route) **gated on a
design decision** (which loss, and how it survives ARC-007 STRICT value-flat), so it routes to `/governance` then
`/implement-substrate`, not to another `/queue-experiment` letter.

## 4. What is owed, and to whom (all in GFLAG-0301)

1. **Documentation currency** (`/governance`): INV-073 `what_would_answer` precondition (4) / (iii), SD-055
   `implementation_note` ("gradient flows to cue_action_proj.weight when flag=True" -- true only for a synthetic bias
   tensor) and ARC-072 `implementation_note` ("Closes EXP-0155 zero-gradient barrier when use_differentiable_cem=True")
   should say: closes the CEM-side (argsort) barrier; the agent-side detach at `agent.py` ~5964/~5971 still severs the
   route, so no trained-policy run has ever had a live cue -> generation gradient.
2. **Build decision** (`/governance`, then `/implement-substrate` if accepted): ARC-072 gap 2 needs (a) a non-detached
   `action_bias` into `propose_trajectories` on the training path and (b) a loss that backprops through the
   differentiable refit -- the 922 docstring's "materially different training loop". ARC-007 STRICT forbids a value
   head in the proposer, so the loss must come from downstream (E3-selected outcome / task reward), which is the design
   question. **Not chipped by this session**: it depends on this session's own not-yet-reviewed finding and on a design
   choice, so `/governance` is the nexus that ratifies and chips it (CLAUDE.md, the `/failure-autopsy` follow-on rule).
3. **Substrate-queue record**: SD-055's entry should carry this probe as a `failure_record` (target: a trained-policy
   run in which `cue_action_proj.weight.grad` is non-None with the flag ON; measured: None across 40 live ticks).
4. **When (2) lands**, the ON/OFF cue-conditioned-divergence experiment becomes runnable as originally designed: arms
   ON vs OFF, >= 5 seeds, goal-rich multi-cue env, DV = cross-cue trajectory divergence + action-class entropy (MECH-269
   readout), with a per-arm `cue_action_proj.weight.grad` readiness precondition (same statistic as the routed
   criterion) so the inert-flag failure can never recur silently. Nothing about that design changes; only its
   precondition is currently false.

## 5. Reproduction (scratch probe, verbatim)

Run from `ree-v3/` with `/opt/local/bin/python3`. Not an experiment; never write it under `evidence/experiments/`.

```python
"""Step 2.5a one-tick probe: does use_differentiable_cem=True make the cue_action_proj
gradient reachable on the LIVE agent path (agent.select_action), as opposed to a direct
propose_trajectories call with a synthetic requires_grad tensor (V3-EXQ-568's recipe)?"""
import sys, inspect, torch
sys.path.insert(0, "/Users/dgolden/REE_Working/ree-v3")
from ree_core.agent import REEAgent
from ree_core.environment.causal_grid_world import CausalGridWorldV2
from ree_core.utils.config import REEConfig

torch.manual_seed(0)
env = CausalGridWorldV2(seed=0) if "seed" in inspect.signature(CausalGridWorldV2).parameters else CausalGridWorldV2()
cfg = REEConfig.from_dims(
    body_obs_dim=env.body_obs_dim, world_obs_dim=env.world_obs_dim, action_dim=env.action_dim,
    alpha_world=0.9, sd016_enabled=True, sws_enabled=False, rem_enabled=False, shy_enabled=False,
    use_differentiable_cem=True, differentiable_cem_temperature=0.5,
)
cfg.hippocampal.num_candidates = 8; cfg.hippocampal.num_cem_iterations = 2; cfg.hippocampal.rollout_horizon = 3
agent = REEAgent(cfg); agent.train()
print("flag reaches config:", agent.hippocampal.config.use_differentiable_cem, "T=", agent.hippocampal.config.differentiable_cem_temperature)
print("has cue_action_proj:", hasattr(agent.e1, "cue_action_proj"))
_, obs = env.reset(); agent.reset()
dev = agent.device
def T(x):
    x = x.to(dev) if torch.is_tensor(x) else torch.tensor(x, dtype=torch.float32, device=dev)
    return x.unsqueeze(0) if x.dim()==1 else x
seen_bias = seen_cands = 0; bias_rg = cand_rg = None; n_ticks = 40; latent = None
for t in range(n_ticks):
    flat = torch.cat([T(obs["body_state"]), T(obs["world_state"])], dim=-1)
    action = agent.act(flat)
    latent = agent._current_latent
    b = getattr(agent, "_cue_action_bias", None)
    if b is not None:
        seen_bias += 1; bias_rg = (bool(b.requires_grad), b.grad_fn is not None)
    c = getattr(agent, "_committed_candidates", None)
    if c:
        seen_cands += 1
        ao = c[0].get_action_object_sequence() if hasattr(c[0], "get_action_object_sequence") else None
        if ao is not None: cand_rg = (bool(ao.requires_grad), ao.grad_fn is not None)
    if torch.is_tensor(action) and action.dim()>1: action = action[0]
    if torch.is_tensor(action) and action.numel()==1:
        a = torch.zeros(env.action_dim); a[int(action.item())] = 1.0; action = a
    _, _h, done, _i, obs = env.step(action)
    if done: _, obs = env.reset(); agent.reset()
print(f"ticks={n_ticks} ticks_with_cue_bias={seen_bias} ticks_with_candidates={seen_cands}")
print("live _cue_action_bias (requires_grad, has_grad_fn):", bias_rg)
print("live committed-candidate ao_seq (requires_grad, has_grad_fn):", cand_rg)
w = agent.e1.cue_action_proj.weight
print("cue_action_proj.weight.grad after live ticks:", None if w.grad is None else float(w.grad.abs().max()))
# Now the 568 recipe for contrast: direct call with a synthetic requires_grad bias.
ab = torch.randn(1, cfg.hippocampal.action_object_dim, requires_grad=True)
trajs = agent.hippocampal.propose_trajectories(z_world=latent.z_world.detach(), z_self=latent.z_self.detach(), e1_prior=None, action_bias=ab)
aos = [t_.get_action_object_sequence() for t_ in trajs if t_.get_action_object_sequence() is not None]
loss = torch.stack(aos).pow(2).mean(); loss.backward()
print("568-recipe synthetic action_bias.grad max:", None if ab.grad is None else float(ab.grad.abs().max()))
print("cue_action_proj.weight.grad after 568-recipe backward:", None if w.grad is None else float(w.grad.abs().max()))
```
