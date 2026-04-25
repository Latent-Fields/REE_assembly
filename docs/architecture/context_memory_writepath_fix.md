# ContextMemory write-path + bias-dominance fix (DRAFT v2)

Status: DRAFT v2, 2026-04-25. Revised per user direction: substrate
implements all three Part B options (`train_only`, `sense_only`, `both`)
behind a config flag; V3-EXQ-418d compares them empirically as a 4-arm
study. Pending user sign-off before code lands.

## Problem (V3-EXQ-477 EXP-0155 diagnostic, 2026-04-24)

Two separable failures of the SD-016 cue-indexed integration path were
isolated by V3-EXQ-477 (SD-016 ContextMemory slot-store diagnostic). They
were not the diagnosed root cause of V3-EXQ-449b (committed 2026-04-23 fix
on `cue_action_proj`, which addressed a downstream forward-path concat) --
both sit upstream in `ContextMemory` itself and continue to hold even after
the cue_action_proj fix.

### Issue (a) -- `key_proj.bias` dominates over slot content

In `ree-v3/ree_core/predictors/e1_deep.py::ContextMemory.__init__`:

```python
self.memory    = nn.Parameter(torch.randn(num_slots, memory_dim) * 0.01)  # very small
self.key_proj  = nn.Linear(memory_dim, memory_dim)  # bias=True by default
```

For each slot s, the projected key is `k_s = W_K @ memory_s + b_K`. The
init scale is 0.01 on `memory`, so `||W_K @ memory_s|| << ||b_K||` for
small `b_K` of any default magnitude. The bias term is the same vector
for every slot, so all keys collapse to ~`b_K`. Attention scores
`q . k_s` are then near-identical across slots, softmax is uniform, and
read-out `cue_context` becomes constant across the batch. EXQ-477
measured this directly:

| metric                                | pre-training | post-P0 |
|---------------------------------------|--------------|---------|
| bias_over_content_ratio               | 9.88         | 3.41    |
| attn_entropy_mean                     | 2.773        | 2.773   |
| uniform_reference                     | 2.7726       | 2.7726  |
| keys_pair_sim with bias               | 0.991        | --      |
| keys_pair_sim content_only            | 0.816        | --      |
| cue_context_per_channel_std           | 2.86e-08     | --      |

`attn_entropy_mean ~= ln(num_slots) = 2.7726` confirms uniform softmax.
`cue_context_per_channel_std = 2.86e-08` means cue_context is a constant
function of the input under SD-016's read path -- and therefore so is
`action_bias` (the EXQ-449b concat-with-z_world workaround re-introduces
input variation but does not restore *content-conditioned* attention).

The 2026-04-04 comment block at e1_deep.py:163-167 already acknowledges
this dominance ("key_proj's bias dominates over the small-init memory
slots, so cue_context is constant across batch"). The 449b workaround was
not the architectural fix.

### Issue (b) -- write path inert during waking

EXQ-477 also reported `n_writes = 0` over the entire run despite the write
gate sigmoid sitting at activation = 0.5 throughout pre-training. Tracing
the call graph confirms:

- `ContextMemory.write()` -- the write fn -- is invoked from exactly two
  places in the codebase:
  1. `E1DeepPredictor.update_from_observation()` (e1_deep.py:350-360),
     guarded by `not self._offline_mode`.
  2. `REEAgent.run_sws_schema_pass()` (agent.py:2739) -- offline / SWS-only
     direct write, gate-bypassed by intent.
- `update_from_observation()` is **never called from REEAgent.sense() or
  step()** in the waking loop. The only references in `agent.py` are in
  docstrings (line 2579 mentions it descriptively).

So in any non-sleep experiment, ContextMemory slots are NEVER updated from
waking observations. They drift only via gradient flow through
`memory: nn.Parameter` during training. EXQ-477's `slot_diversity` collapse
from 0.999 (pre-training) to 0.135 (post-P0) is consistent with this:
under the gradient-only path, the encoder learns to ignore the slots and
they collapse toward a single attractor.

These two failures compose: even if (a) is fixed (bias zeroed), (b)
ensures the memory contents themselves never reflect any specific waking
experience -- the read path becomes content-conditioned over content that
was never written.

## Proposed fix

Two-part patch. Part A is uncontroversial. Part B has an architectural
choice that needs user confirmation before code lands.

### Part A: zero `key_proj.bias` (mechanical fix)

Two equivalent options, listed in order of preference.

**Option A1 (preferred): bias=False on key_proj.**

```python
# ree_core/predictors/e1_deep.py, ContextMemory.__init__:
self.key_proj = nn.Linear(memory_dim, memory_dim, bias=False)
```

Rationale: structural -- the bias parameter is not just zeroed at init
but absent entirely, so optimization cannot drift it back. Matches the
implementation contract that key projection should be a pure linear map
of slot content. Same parameter count as zeroing-at-init minus
`memory_dim` (128 fewer params on default config).

**Option A2 (compatibility option): zero at init, leave parameter.**

```python
self.key_proj = nn.Linear(memory_dim, memory_dim)
nn.init.zeros_(self.key_proj.bias)
```

Use only if there is a load-from-checkpoint path that requires the same
state_dict shape as the legacy module (none currently exists in V3, but
flagged for completeness).

Note: `query_proj` and `value_proj` retain their default biases. Their
bias dominance is mitigated because:
- `query_proj` consumes the input cue (`current_state`), which has
  per-batch variation, so a constant bias adds to a per-batch-varying
  signal and does not collapse softmax inputs.
- `value_proj` only affects the read-out value, not the attention
  weights -- a constant bias adds the same vector to every read but does
  not collapse the attention partition.

**Backward compatibility**: this changes the `state_dict` of any model
whose `key_proj` was previously instantiated with `bias=True`. No V3
experiment ships pre-trained weights for ContextMemory, so the backward
compat impact is limited to in-flight experiment runs and to any
checkpoint serialized after this change. The runner does not persist
encoder checkpoints across queue items.

**Smoke check (proposed)**: re-run a single forward pass under
`sd016_enabled=True` on default config and confirm
`attn_entropy_mean < 2.5` (well below `ln(16) = 2.7726`) and
`keys_pair_sim_content_only < 0.95` over a batch of 16 random `z_world`
draws. Add a contract test under `tests/contracts/` that fails if
attention entropy stays at the uniform reference.

### Part B: wire the waking write path (config-flag substrate, all modes empirically tested)

The decision is *where* to call the ContextMemory write from the agent
loop. There are three viable sites with different semantics, and we do
not have priors strong enough to pick one. Per user direction
(2026-04-25): land **all three as a single substrate** keyed on a
config flag, then run V3-EXQ-418d as a multi-arm comparison that
selects empirically.

#### Substrate: `sd016_writepath_mode` config flag

Add a single string flag to `REEAgent`'s config (default `"off"` to
preserve the current observable behaviour for any non-SD-016
experiment):

```python
# config field, REEAgentConfig (or wherever sd016_enabled lives):
sd016_writepath_mode: str = "off"
# valid: "off", "train_only", "sense_only", "both"
```

Semantics:

| value         | train-time write | per-tick sense() write |
|---------------|------------------|------------------------|
| `"off"`       | no               | no                     |
| `"train_only"`| yes (B1)         | no                     |
| `"sense_only"`| no               | yes (B2)               |
| `"both"`      | yes (B1)         | yes (B2)               |

`"off"` is the default and matches the **current** behaviour (no waking
writes ever fire), so no in-flight experiment changes its observable
semantics until it explicitly opts in. SD-016 experiments must set the
flag.

#### Hook B1 -- training-time write (after prediction error computed)

```python
# in compute_e1_prediction_loss (agent.py), AFTER prediction_error is
# computed and BEFORE the optimizer step:
if self.config.sd016_writepath_mode in ("train_only", "both"):
    e1_observation_state = torch.cat([z_self, z_world], dim=-1)
    self.e1.update_from_observation(e1_observation_state, prediction_error)
```

`update_from_observation` is already gated internally by
`not self._offline_mode`, so SHY semantics hold automatically.

#### Hook B2 -- per-tick sense() write

```python
# in REEAgent.sense(), AFTER LatentStack.encode() and BEFORE MECH-269
# per_stream_vs update:
if self.config.sd016_writepath_mode in ("sense_only", "both") and not self.e1._offline_mode:
    obs_state = torch.cat([new_latent.z_self, new_latent.z_world], dim=-1)
    self.e1.context_memory.write(obs_state)
```

Note the explicit `_offline_mode` guard: `ContextMemory.write` is not
internally gated (only `update_from_observation` is), so the gate must
be added at the call site to preserve MECH-120 SHY semantics.

#### Mode trade-offs (to be settled empirically by EXQ-418d)

- **`train_only` (B1)**: writes fire only when prediction error is being
  computed, so the slot store reflects content the encoder is also
  training on. Lowest risk for diagnostic probes that run pure-inference
  -- they see no writes and read back whatever was trained in.
- **`sense_only` (B2)**: writes fire from raw observation every step,
  decoupled from training. Higher write density, but contaminates
  diagnostic probes that intentionally compare pre/post-training slot
  state.
- **`both`**: maximum write density, double-writes for any tick that
  involves both sense() and training. Useful as a ceiling for slot-
  differentiation behaviour; not necessarily the right production
  default.

### What this does NOT fix

- `cue_action_proj` training surface remains unresolved. EXP-0155
  identified that cue_action_proj.weight gets exactly 0.0 gradient under
  the current path because the CEM argmax in HippocampalModule is
  non-differentiable and `agent.py` detaches `action_bias` before
  rollouts. The 449b "concat z_world" workaround makes the *output* of
  cue_action_proj input-varying but does not give cue_action_proj's
  *weights* a training signal. The fix above gives ContextMemory slots
  real content; whether cue_action_proj can extract anything useful
  from the now-content-rich slots is a separate question (EXP-0155
  follow-up).
- ContextMemory.write() uses the no-grad min-score-slot replacement
  rule. This may or may not be the right write policy for a content-
  addressable memory under SD-016. A separate question, not in scope.
- Slot diversity collapse from 0.999 -> 0.135 post-P0 may persist
  even after both Part A and Part B if the gradient through the now-
  written slots still pulls them together. A regularization term
  (e.g. orthogonality loss on the slot matrix) would be the next-step
  remedy if this signature recurs in EXQ-418d.

## Validation experiment

Once Part A and the Part B substrate land, queue **V3-EXQ-418d**
(supersedes V3-EXQ-418c) as a 4-arm comparison testing all three
write-path modes against an OFF baseline, with Part A applied
uniformly across arms.

### Arm matrix

| arm | `sd016_enabled` | `key_proj.bias` | `sd016_writepath_mode` | purpose |
|-----|-----------------|-----------------|------------------------|---------|
| A0 (baseline) | `True` | `False` (Part A) | `"off"`        | isolates Part A effect alone -- read-path fix without write-path |
| A1 (B1)       | `True` | `False` (Part A) | `"train_only"` | training-time writes only |
| A2 (B2)       | `True` | `False` (Part A) | `"sense_only"` | per-tick observation writes only |
| A3 (both)     | `True` | `False` (Part A) | `"both"`       | maximum write density |

3 seeds per arm = 12 runs. Part A is applied uniformly (all arms have
`bias=False`) so the comparison is purely about write-path mode, not
about whether bias zeroing matters. Whether bias zeroing matters is
already settled by EXQ-477 metrics + the proposed contract test --
416 lines of measured `attn_entropy_mean = 2.773` (uniform reference)
under the legacy code is the negative control for that question.

If the user wants an explicit pre-fix negative control included, add:

| arm | `sd016_enabled` | `key_proj.bias` | `sd016_writepath_mode` | purpose |
|-----|-----------------|-----------------|------------------------|---------|
| A_neg (legacy) | `True` | `True` (legacy) | `"off"` | reproduces EXQ-418c FAIL signature, sanity-check |

Decide A_neg vs no-A_neg at script-writing time -- not load-bearing for
the B-mode comparison.

### Per-arm acceptance criteria

For arms A1, A2, A3:
- `attn_entropy_mean < 2.5` in 2/3 seeds during eval (read-path
  content-conditioning intact -- driven by Part A, expected to hold
  in A0 too).
- `n_writes > 0` over the run (write path firing -- A0 should have 0,
  arms A1/A2/A3 should be non-zero).
- `slot_diversity` post-eval > 0.5 (slot differentiation preserved --
  breaks the 0.999 -> 0.135 collapse signature seen in EXQ-477).
- Behavioural arm ablation (WITH_SLEEP vs WITHOUT_SLEEP) produces
  measurably different `action_class_entropy` in at least one of
  A1/A2/A3 (EXQ-418c saw bit-identical because cue_action_proj output
  was constant -- if all of A1/A2/A3 are still bit-identical, the
  bottleneck is not the write path and EXP-0155 follow-up is the next
  step).

### Cross-arm comparison

Report side-by-side:
- `n_writes`, `slot_diversity`, `attn_entropy_mean` per arm.
- `action_class_entropy` ablation delta (WITH_SLEEP minus
  WITHOUT_SLEEP) per arm.
- Wall-clock training cost per arm (B2/both will write per tick, may
  add measurable overhead; relevant for the production-default
  choice).

### Decision rule

The arm with the **smallest** `slot_diversity` collapse and the
**largest** `action_class_entropy` ablation delta becomes the
recommended production default for `sd016_writepath_mode`. If A0
already meets criteria (Part A alone restores SD-016), the B-modes
become an enhancement question rather than a correctness question and
the recommendation is `"off"` until a stronger SD-016 experiment
demands otherwise. If multiple modes are statistically
indistinguishable, prefer `train_only` (lowest write overhead, cleanest
diagnostic semantics).

## Files touched (proposed)

| File                                                           | Change                                                                            |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------|
| `ree-v3/ree_core/predictors/e1_deep.py`                        | Part A (`bias=False` on `key_proj`)                                               |
| `ree-v3/ree_core/agent.py`                                     | Add `sd016_writepath_mode` config; wire B1 hook in `compute_e1_prediction_loss`; wire B2 hook in `sense()` |
| `ree-v3/ree_core/config.py` (or wherever REEAgentConfig lives) | Add `sd016_writepath_mode: str = "off"` field with validator `{off, train_only, sense_only, both}` |
| `ree-v3/tests/contracts/test_sd_016_context_memory.py` (NEW)   | Contract test asserting non-uniform attention entropy under Part A; mode-routing asserts |
| `ree-v3/experiments/v3_exq_418d_sd016_writepath_modes_comparison.py` (NEW) | 4-arm validation script (A0/A1/A2/A3 [+ optional A_neg])              |

No claims.yaml edits in this pass -- if 418d PASSes, the SD-016 entry
gains a new evidence note rather than a new claim. The chosen
production default for `sd016_writepath_mode` (per the decision rule
above) becomes a follow-up edit to whichever experiment script first
ships SD-016 in production configuration.

## References

- V3-EXQ-477 manifest: `REE_assembly/evidence/experiments/v3_exq_477_sd016_context_memory_slot_store_diagnostic_20260424T080649Z_v3.json`
- V3-EXQ-418a manifest (run actually under EXQ-418c queue ID, reused 418a script): `REE_assembly/evidence/experiments/v3_exq_418a_sd016_sd017_context_conditioned_action_20260424T021932Z_v3.json`
- ContextMemory definition: `ree-v3/ree_core/predictors/e1_deep.py:35-73`
- `update_from_observation` definition: `ree-v3/ree_core/predictors/e1_deep.py:350-360`
- SD-016 design doc: `REE_assembly/docs/architecture/sd_016_frontal_cue_integration.md`
- 449b prior fix (downstream concat): `ree-v3/experiments/v3_exq_449b_sd016_cue_action_proj_consumer_fix.py`
