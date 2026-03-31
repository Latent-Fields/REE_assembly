# SD-016: Frontal Cue Integration

**Claim ID:** SD-016
**Subject:** `e1.frontal_cue_indexed_integration`
**Status:** PENDING -- not yet implemented
**Registered:** 2026-03-31
**Depends on:** SD-005, SD-010, ARC-035
**Blocks:** MECH-150, MECH-151, MECH-152, ARC-041, INV-040 (cannot be validated until implemented)

---

## Problem

### Current E1 Output Contract

E1 produces a single `terrain_prior` [batch, world_dim] via `generate_prior()`. This is a bulk
associative prior over the world domain, constructed by querying ContextMemory with the full
concatenated latent `[z_self, z_world]` and passing the result through `prior_generator`. The
prior is used by HippocampalModule for terrain-informed rollout search (SD-002).

This is a bulk signal: the same prior structure is produced regardless of whether the agent is in
a hazard-dense or hazard-free region of the environment. There is no mechanism through which
specific z_world cue patterns -- retrieved from ContextMemory -- modulate (a) which action-objects
are prioritised in E2's affordance space, or (b) the precision weights on harm vs. goal scoring
in E3.

### What This Misses

E1's ContextMemory stores 16 association slots. When the agent is in a context with a specific
hazard gradient cue in `world_obs`, the ContextMemory can in principle retrieve hazard-relevant
associations via its softmax attention over slots. But no downstream pathway exists to act on
this retrieval in a cue-specific way.

Two distinct downstream effects are missing:

1. **Action affordance bias (MECH-151):** When z_world retrieves a hazard-associated context
   from ContextMemory, action-objects encoding avoidance manoeuvres should be weighted upward
   in E2's affordance space. Currently, E2's `action_object()` method produces `o_t` from
   `[z_world, action]` with no E1-derived modulation -- the affordance landscape is flat with
   respect to contextual hazard cues.

2. **Terrain precision modulation (MECH-152):** E3 scores trajectories using
   `harm_eval_z_harm_head(z_harm)` and `benefit_eval_head(z_world)` at equal precision
   regardless of whether sensory cues indicate an upcoming hazard or a safe region. The agent
   cannot weight harm scoring more heavily when contextual cues predict elevated danger, nor
   relax harm weighting in clearly safe contexts.

### Concrete Failure Mode

E3's harm scoring is equally precise in all contexts. The agent only begins reacting to harm
after `z_harm_a` accumulates via its EMA (tau ~20 steps). Context-based anticipatory weighting
-- sharpening harm precision before contact, based on exteroceptive cues -- is entirely absent.

This matches the failure mode of vmPFC lesion patients in the Iowa Gambling Task: pre-SCR
(anticipatory skin conductance) is absent. Intact participants show rising SCR several trials
before selecting from a bad deck -- a physiological anticipatory signal driven by contextual
cues, not immediate feedback (Bechara et al. 1997). The lesioned patients respond only to
immediate outcomes, not to predictive context. SD-016 implements the architectural prerequisite
for this pre-SCR analog: E1 cue retrieval feeding forward into E2 affordance and E3 scoring
precision before harm occurs.

### Why SD-005 Is Prerequisite

Cue-indexed retrieval must query ContextMemory with `z_world` only -- not with the full
`[z_self, z_world]` concatenation used by `generate_prior()`. This z_world-only query ensures
that the retrieved context reflects exteroceptive sensory cues, not body state. Without the
z_self/z_world split introduced by SD-005, a z_world-only ContextMemory query is architecturally
impossible -- the latent is a fused `z_gamma` with no clean exteroceptive component.

### Why SD-010 Is Prerequisite

The terrain_weight output of SD-016 scales `harm_eval_z_harm_head`, E3's dedicated nociceptive
scoring head (SD-010). This head operates on `z_harm` -- the clean harm stream separated from
z_world by SD-010. Without SD-010's separation, harm scoring is contaminated by world-structure
content, and terrain_weight modulation would scale an impure signal. SD-010 is the architectural
prerequisite that makes terrain precision modulation interpretable.

### Why ARC-035 Is Prerequisite

ARC-035 (vmPFC stored->active transition) specifies the functional circuit within which SD-016
operates: stored value associations in E1's ContextMemory are activated by matching z_world cues
and routed forward to influence ongoing action selection and appraisal. SD-016 provides the
concrete retrieval and projection mechanism that implements this functional specification.

---

## Solution

### New E1 Method: `extract_cue_context()`

A new method is added alongside the existing `generate_prior()`. It does NOT replace
`generate_prior()` -- the terrain prior used by HippocampalModule is unchanged.

```python
def extract_cue_context(
    self,
    z_world: torch.Tensor,   # [batch, world_dim]
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    E1 frontal cue-indexed association retrieval (MECH-150).

    Queries ContextMemory with z_world (exteroceptive cues only),
    producing cue-specific association context without body-state blending.

    Unlike generate_prior() -- which queries with [z_self, z_world] and
    produces a bulk terrain prior for HippocampalModule -- this method
    queries with z_world alone and projects to two downstream signals:

        action_bias:    E1 -> E2 affordance modulation (MECH-151)
        terrain_weight: E1 -> E3 precision modulation  (MECH-152)

    ContextMemory.read() returns [batch, latent_dim=64] (output_proj maps
    memory_dim=128 -> latent_dim=64). The z_world-only query uses a
    dedicated world_query_proj (Linear(world_dim=32, memory_dim=128))
    instead of the main query_proj (which expects latent_dim=64 input).

    Returns:
        action_bias:    [batch, action_object_dim=16]  -- additive to E2.action_object o_t
        terrain_weight: [batch, 2] in (0, 1)           -- [w_harm, w_goal] for E3 scoring
    """
    cue_context = self.context_memory.read(z_world)   # z_world-only query
    action_bias = self.cue_action_proj(cue_context)
    terrain_weight = torch.sigmoid(self.cue_terrain_proj(cue_context))
    return action_bias, terrain_weight
```

### Dimension Note: ContextMemory Output

ContextMemory.read() returns shape `[batch, latent_dim=64]` because:
- `output_proj = nn.Linear(memory_dim=128, latent_dim=64)`
- `latent_dim = self_dim + world_dim = 32 + 32 = 64`

The two new projection heads therefore use `latent_dim=64` as input:
- `cue_action_proj: nn.Linear(latent_dim=64, action_object_dim=16)` (~1040 params)
- `cue_terrain_proj: nn.Linear(latent_dim=64, 2)` (~130 params)

The z_world-only query requires a separate `world_query_proj: nn.Linear(world_dim=32, memory_dim=128)`
because the existing `query_proj` in ContextMemory expects `latent_dim=64` as input. The new
`world_query_proj` bypasses `context_memory.query_proj` to project z_world directly into key-space:

```python
# In extract_cue_context():
# Use world_query_proj to project z_world -> memory_dim, then do the attention manually
q = self.world_query_proj(z_world).unsqueeze(1)  # [batch, 1, memory_dim]
k = self.context_memory.key_proj(self.context_memory.memory).unsqueeze(0).expand(batch, -1, -1)
v = self.context_memory.value_proj(self.context_memory.memory).unsqueeze(0).expand(batch, -1, -1)
scores = torch.bmm(q, k.transpose(1, 2)) / (memory_dim ** 0.5)
weights = F.softmax(scores, dim=-1)
context = torch.bmm(weights, v).squeeze(1)   # [batch, memory_dim]
cue_context = self.context_memory.output_proj(context)  # [batch, latent_dim=64]
```

### New E1 Parameters (conditioned on `sd016_enabled`)

Following the MECH-116 pattern in `E1DeepPredictor.__init__()`, new projections are
instantiated only when the config flag is set:

```python
if getattr(config, 'sd016_enabled', False):
    action_object_dim = getattr(config, 'action_object_dim', 16)
    cue_context_dim = config.self_dim + config.world_dim  # = latent_dim = 64
    self.world_query_proj = nn.Linear(config.world_dim, config.hidden_dim)
    self.cue_action_proj  = nn.Linear(cue_context_dim, action_object_dim)
    self.cue_terrain_proj = nn.Linear(cue_context_dim, 2)
```

When `sd016_enabled=False` (all existing experiments), these attributes do not exist and the
extract_cue_context() call is never made -- full backward compatibility.

### E2 Integration: Biased Action-Object (MECH-151)

`E2FastPredictor.action_object()` accepts an optional `action_bias` argument. When provided,
it is added to the raw action-object output before returning:

```python
def action_object(
    self,
    z_world: torch.Tensor,
    action: torch.Tensor,
    action_bias: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    z_a = torch.cat([z_world, action], dim=-1)
    o_t = self.action_object_head(z_a)
    if action_bias is not None:
        o_t = o_t + action_bias
    return o_t
```

The additive formulation preserves the existing `action_object_head` computation as the base
affordance signal; the E1-derived bias shifts this without overriding it. When `action_bias` is
None (all existing callers), behaviour is identical to the current implementation.

### E3 Integration: Terrain-Weighted Scoring (MECH-152)

In `E3TrajectorySelector.score_trajectory()` (or the equivalent inline scoring path), an
optional `terrain_weight` argument modulates harm and goal score magnitudes:

```python
def score_trajectory(self, trajectory, terrain_weight=None, ...):
    # ... existing latent construction and harm/benefit eval ...
    harm_score = self.harm_eval_z_harm_head(z_harm)
    goal_score = self.benefit_eval_head(z_world)
    if terrain_weight is not None:
        w_harm = terrain_weight[:, 0:1]
        w_goal = terrain_weight[:, 1:2]
        harm_score = harm_score * w_harm
        goal_score = goal_score * w_goal
    # ... aggregate into total score ...
```

Crucially, both `harm_eval_z_harm_head` and `benefit_eval_head` still receive their proper
latent inputs (`z_harm` and `z_world` respectively) -- terrain_weight rescales the scores after
evaluation, not the inputs. This preserves the SD-010 harm stream separation: z_harm is not
touched, only the weight applied to the resulting score.

### agent.py Wiring

In `_e1_tick()`, after E1 runs and produces the terrain prior, the cue context extraction is
performed and cached on the agent:

```python
if hasattr(self.e1, 'cue_action_proj'):
    action_bias, terrain_weight = self.e1.extract_cue_context(latent_state.z_world)
    self._cue_action_bias    = action_bias.detach()
    self._cue_terrain_weight = terrain_weight.detach()
else:
    self._cue_action_bias    = None
    self._cue_terrain_weight = None
```

The cached tensors are passed forward at the appropriate points in the step loop:
- `action_bias` is passed into all E2 `action_object()` calls within HippocampalModule's
  candidate generation loop.
- `terrain_weight` is passed into E3 trajectory scoring at the E3 tick.

Detaching the cached tensors prevents stale computational graphs from accumulating between
ticks. The cue signals are treated as contextual modulation inputs, not as part of the
current-step gradient graph.

---

## Tensor Shapes and Contracts

| Signal | Source | Destination | Shape | Notes |
|---|---|---|---|---|
| `cue_context` | `E1.context_memory.output_proj(attention_out)` | E1 internal | [batch, latent_dim=64] | z_world-only query via world_query_proj; ContextMemory output_proj maps memory_dim=128 -> latent_dim=64 |
| `action_bias` | `E1.cue_action_proj(cue_context)` | `E2.action_object()` | [batch, action_object_dim=16] | Additive to `o_t`; None when sd016_enabled=False |
| `terrain_weight` | `E1.cue_terrain_proj(cue_context)` + sigmoid | `E3.score_trajectory()` | [batch, 2] in (0, 1) | [w_harm, w_goal]; sigmoid ensures weights are bounded |

**Invariant:** `action_bias` and `terrain_weight` are derived from `z_world` ONLY -- not from
`z_self` or the full `[z_self, z_world]` concatenation. This ensures action biasing and terrain
weighting reflect exteroceptive sensory context rather than body state, preserving the SD-004/
SD-005 contract: E2 action-object space is z_world-domain; E3 operates on z_world and z_harm.

---

## Training Signals

### `cue_action_proj` Training

No new loss term is required. `action_bias` enters the computation graph via E2's biased
action-object outputs, which feed HippocampalModule's trajectory proposals (SD-004), which feed
E3 trajectory scoring. Gradient flows back from E3's trajectory selection loss through the biased
action-objects, through `cue_action_proj`, and into ContextMemory's slot contents.

The implicit training signal: when a hazard-avoidance trajectory is selected and the episode
confirms low harm realised, the action-objects that were upweighted (via action_bias) reinforce
the z_world cue pattern that retrieved them. This is credit assignment through the existing
trajectory scoring path -- no new loss path required.

### `cue_terrain_proj` Training: Supervised Proxy (V3)

For initial V3 validation, `cue_terrain_proj` is trained with a direct supervised signal using
`hazard_field_view.max()` as a context label. CausalGridWorldV2 already emits `harm_obs`
(proximity-weighted hazard density in the agent's field of view); the maximum across the field
serves as a proxy for whether the current context is hazard-dense.

```python
# Compute targets from environment observation
# hazard_field_view: [batch] scalar from harm_obs[..., :25].max()
w_harm_target = torch.where(
    hazard_field_view > 0.3,
    torch.full_like(hazard_field_view, 0.8),
    torch.full_like(hazard_field_view, 0.2),
)
w_goal_target = torch.where(
    hazard_field_view < 0.1,
    torch.full_like(hazard_field_view, 0.8),
    torch.full_like(hazard_field_view, 0.3),
)

terrain_loss = (
    F.mse_loss(terrain_weight[:, 0], w_harm_target)
    + F.mse_loss(terrain_weight[:, 1], w_goal_target)
)
```

The thresholds (0.3 hazard-dense; 0.1 hazard-free) and target values (0.8 / 0.2) are calibration
parameters exposed via config. This supervised signal is intentionally coarse -- the goal is to
confirm that E1's cue context can be projected into a meaningful terrain weighting before
implementing learned context embeddings (V4 extension).

### Loss Integration

`terrain_loss` is added to the E1 training objective (alongside the existing prediction error
loss). It should be weighted to avoid overwhelming the primary prediction objective:

```python
e1_total_loss = e1_prediction_loss + lambda_terrain * terrain_loss
```

where `lambda_terrain` is a config parameter (suggested default: 0.1 for V3 calibration).

---

## Prerequisites, V3/V4 Scope, Downstream Claims

### Prerequisites (Hard Gates)

- **SD-005** (z_self/z_world split): z_world must be architecturally distinct from z_self for the
  z_world-only ContextMemory query to be meaningful. Without SD-005, no clean exteroceptive
  channel exists to query.
- **SD-010** (harm stream separation): `terrain_weight` modulates `harm_eval_z_harm_head`, which
  operates on the dedicated z_harm stream. This head is only architecturally isolated and
  interpretable after SD-010 separates z_harm from z_world.
- **ARC-035** (vmPFC stored->active transition): SD-016 provides the concrete retrieval mechanism
  for the stored->active transition specified by ARC-035. SD-016 cannot be validated in isolation
  from the functional claim it implements.

### V3 Scope (all of SD-016)

| Component | Change | Parameter count |
|---|---|---|
| `E1DeepPredictor.extract_cue_context()` | New method | 0 (logic only) |
| `E1.world_query_proj` | `nn.Linear(world_dim=32, memory_dim=128)` | ~4224 params |
| `E1.cue_action_proj` | `nn.Linear(latent_dim=64, action_object_dim=16)` | ~1040 params |
| `E1.cue_terrain_proj` | `nn.Linear(latent_dim=64, 2)` | ~130 params |
| `E2.action_object()` | Optional `action_bias` arg | 0 (interface change) |
| `E3.score_trajectory()` | Optional `terrain_weight` arg | 0 (interface change) |
| `agent._e1_tick()` | Cache + forward cue signals | ~20 lines |
| Training: `terrain_loss` | Supervised proxy on hazard_field_view | 0 (loss logic) |

Total new parameters: ~5394 (negligible relative to existing architecture). Backward-compat
flag `sd016_enabled=False` ensures all existing experiments are unaffected.

### V4 Scope (Extensions)

- **Learned context embeddings:** Replace the `hazard_field_view.max()` proxy with unsupervised
  clustering of z_world patterns. Context labels derived from offline clustering of the z_world
  manifold; terrain_weight trained to predict cluster-specific harm/goal priors rather than
  scalar hazard density.
- **Social observation channels:** Extend ContextMemory query to include social-observation
  components of z_world (MECH-131/132: social and identity constraint content classes). Cue
  retrieval then modulates action affordances and terrain precision in response to social
  context, not only physical hazard context.
- **Allostatic terrain_weight modulation:** Couple `terrain_weight` to `drive_level` from
  SD-012 (homeostatic drive). When energy is depleted, upweight `w_goal` modulation from
  cue context regardless of hazard cues -- approach drive overrides risk sensitivity in the
  terrain weighting. This is the frontal/hypothalamic coupling analog.

---

## What SD-016 Enables

- **MECH-150 (E1 cue-indexed association retrieval):** The z_world-only ContextMemory query
  is the substrate for this mechanism. Can be validated once SD-016 is implemented by measuring
  whether cue_context retrieval correlates with the current hazard context independently of body
  state.
- **MECH-151 (E1->E2 action affordance modulation):** The biased `action_object()` output
  can be validated by measuring whether hazard-context cues shift candidate trajectory
  distributions toward avoidance action-objects before harm contact occurs.
- **MECH-152 (E1->E3 terrain precision modulation):** The terrain_weight modulation can be
  validated by measuring whether harm/goal scoring precision shifts in response to contextual
  cues in advance of the harm stream accumulating (z_harm_a EMA lag).
- **ARC-041 (frontal cue-weighting circuit):** The full E1->E2 and E1->E3 circuit together
  constitute the frontal cue-weighting architecture described in ARC-035 (vmPFC stored->active
  transition).
- **INV-040 (sensory cue sufficiency):** The claim that sensory cues alone are sufficient to
  activate terrain-appropriate precision weighting -- without requiring harm contact -- can be
  tested directly by measuring terrain_weight outputs in novel hazard-cue contexts before any
  harm accumulates in z_harm_a.

---

## Registered Claims

| Claim ID | Status | Subject | Depends on |
|---|---|---|---|
| SD-016 | PENDING | `e1.frontal_cue_indexed_integration` | SD-005, SD-010, ARC-035 |
| MECH-150 | candidate | `e1.cue_indexed_association_retrieval` | SD-016, ARC-001, SD-005 |
| MECH-151 | candidate | `e1_e2.cue_indexed_action_affordance_modulation` | MECH-150, SD-004 |
| MECH-152 | candidate | `e1_e3.cue_indexed_terrain_precision_modulation` | MECH-150, ARC-016, SD-010 |
| ARC-041 | candidate | `architecture.frontal_cue_weighting_circuit` | MECH-150, MECH-151, MECH-152, ARC-035 |
| INV-040 | candidate | `ethics.sensory_cue_sufficiency_for_terrain_activation` | ARC-041, MECH-150 |

---

## References

- Bechara et al. (1997, *Science*): vmPFC patients lack anticipatory SCR before choosing from
  bad decks in the Iowa Gambling Task -- pre-outcome physiological preparation absent even when
  immediate feedback is intact. Motivates the cue-indexed anticipatory precision mechanism.
- Damasio (1994): Somatic marker hypothesis -- stored value associations modulate prospective
  decision-making via re-activation from contextual cues (the vmPFC stored->active transition
  formalised in ARC-035).
- ARC-035: vmPFC stored->active transition (architectural requirement that SD-016 implements).
- SD-005: z_self/z_world split (prerequisite -- z_world-only query requires architecturally
  distinct exteroceptive channel).
- SD-010: harm stream separation (prerequisite -- terrain_weight modulates z_harm-based scoring,
  which requires the clean nociceptive stream).
- SD-011: dual nociceptive streams (co-constraint -- z_harm_a EMA lag motivates the need for
  cue-indexed anticipatory weighting; SD-016 provides the pre-emptive signal that z_harm_a
  cannot).
- SD-012: homeostatic drive (V4 coupling target -- allostatic modulation of terrain_weight
  by drive_level deferred to V4 scope).
