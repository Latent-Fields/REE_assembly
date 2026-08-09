---
nav_exclude: true
status: implemented
status_asof: 2026-07-10
status_claim: SD-016
---

# SD-016 ContextMemory v3 -- Auxiliary Diversification Loss (Path 1)

Status: PROPOSED 2026-04-25
Supersedes (operational): SD-016 ContextMemory v2 write-path (Part A bias-fix +
  Part B mode routing) for downstream behavioural validity.
  v2 substrate is RETAINED -- diversification adds gradient pressure on top of
  the v2 mechanism, it does not remove key_proj.bias=False or sd016_writepath_mode.
Author: Claude (Opus 4.7) under user direction
Validation: V3-EXQ-418e (4-arm ablation)

## 1. Diagnosis from V3-EXQ-418d

EXQ-418d ran the v2 4-arm comparison (A0_off, A1_train_only, A2_sense_only,
A3_both) under matched seeds [42, 43, 44]. All four arms FAILed acceptance:

  Arm        | attn_entropy_mean | slot_diversity (seeds 42/43/44)
  -----------+-------------------+--------------------------------
  A0_off     | 2.760-2.770       | 0.46 / 0.0 / 0.0 (collapsed)
  A1_train   | 2.760-2.770       | 0.46 / 0.0 / 0.0 (collapsed)
  A2_sense   | 2.760-2.770       | 0.46 / 0.0 / 0.0 (collapsed)
  A3_both    | 2.760-2.770       | 0.46 / 0.0 / 0.0 (collapsed)

Uniform-attention reference is ln(16) = 2.7726. All arms sit on the uniform
rail. Slot diversity is bimodal across seeds: seed 42 escapes to ~0.46, seeds
43 and 44 collapse to numerically zero (<1e-4) on every arm including
A0_off (zero writes).

### 1.1 Why the v2 write-path is insufficient

The v2 write rule (e1_deep.py:76-84) selects the argmin-scoring slot and
EMA-updates it via `0.9*old + 0.1*write_signal.mean(0)`, wrapped in
`torch.no_grad()`. There are TWO observable failure paths:

(a) **No gradient pressure on slot diversification.** Read-side gradient
    through `cue_terrain_loss` + `cue_action_loss` only refines the slot
    vectors that are most-attended (which is all slots equally under the
    uniform attention regime). Differentiating slots requires either an
    init that already breaks symmetry OR an explicit pressure term. EXQ-418d
    A0_off (zero writes, only read-side gradient) confirms read-side alone
    cannot break symmetry: entropy = 2.770 = uniform.

(b) **Writes-only is luck-dependent.** Seed 42 escapes (0.46 diversity)
    only in arm A1; seeds 43/44 collapse in every arm. The argmin-tie path
    in `ContextMemory.write` favours the lowest-index slot deterministically
    when scores are tied, so a single slot accumulates all `write_signal`
    contributions and the others stay near init. Whether this matters
    behaviourally depends on whether the init random vectors happen to
    cluster the argmin into a single slot or oscillate between several --
    pure luck of `torch.randn(num_slots, memory_dim) * 0.01`.

### 1.2 Architecture has implicitly conceded the bottleneck

The EXQ-449a band-aid in `extract_cue_context()` already routes `z_world`
directly into `cue_action_proj` (concatenated with `cue_context`):

```python
action_bias = self.cue_action_proj(torch.cat([cue_context, z_world], dim=-1))
```

This guarantees per-input variation in `action_bias` regardless of whether
`cue_context` is constant. But this is an admission: the SD-016
ContextMemory attention path is currently uninformative for action-bias
differentiation. A working v3 substrate should make `cue_context` itself
informative -- otherwise the SD-016 cluster (MECH-150/151/152, ARC-041)
reduces to a thin shim around the already-existing E1 prior path.

## 2. Path 1: Auxiliary diversification loss

### 2.1 Loss form

For each forward pass that exercises the SD-016 path, add a loss term:

```
slot_norm  = F.normalize(memory, dim=-1)               # [num_slots, memory_dim]
sim        = slot_norm @ slot_norm.T                   # [num_slots, num_slots]
n          = num_slots
mask       = 1 - eye(n)                                 # [n, n]
loss_div   = sd016_diversification_weight *
             (sim * mask).pow(2).sum() / (n * (n - 1))
```

This is the mean squared off-diagonal cosine similarity of the slot vectors,
with the diagonal masked out (cosine self-similarity is 1 by definition).
Minimising it pushes the slot vectors toward mutual orthogonality on the unit
sphere. Implemented as a single new method on `ContextMemory`:

```python
def compute_diversification_loss(self) -> torch.Tensor:
    slot_norm = F.normalize(self.memory, dim=-1)
    sim       = slot_norm @ slot_norm.T
    n         = self.num_slots
    mask      = 1.0 - torch.eye(n, device=sim.device)
    return (sim * mask).pow(2).sum() / (n * (n - 1))
```

The weight is a separate float so the production default is `0.0`
(bit-identical to the v2 substrate when not opted in).

### 2.2 Wiring point

The loss is added inside `REEAgent.compute_prediction_loss()` AFTER the
existing E1 prediction loss is computed and AFTER the v2 train_only write
hook fires:

```python
# SD-016 Path 1: auxiliary diversification loss on ContextMemory slots.
_div_w = getattr(self.config, "sd016_diversification_weight", 0.0)
if _div_w > 0.0 and getattr(self.e1.config, "sd016_enabled", False):
    loss = loss + _div_w * self.e1.context_memory.compute_diversification_loss()
```

Wired into `compute_prediction_loss` (not `sense()`) for the same reason
the v2 train-time hook lives there: it must run inside the gradient pass
so the optimiser can shape `ContextMemory.memory` directly. Gating on
`sd016_enabled` mirrors the existing pattern -- non-SD-016 experiments
see no behaviour change. Gating on `_div_w > 0.0` keeps the no-op cheap
when an SD-016 experiment opts out of diversification.

### 2.3 Initial weight

`sd016_diversification_weight = 0.5` for the validation experiment.
Comparable to `LAMBDA_CUE_ACTION = 0.5` and `LAMBDA_TERRAIN = 0.1` used in
EXQ-418d. The weight is exposed in the experiment script as `LAMBDA_DIVERSIFY`
so future sweeps can vary it without re-implementing the wiring.

## 3. Falsification design (V3-EXQ-418e)

Four-arm ablation, matched seeds [42, 43, 44], same training schedule as
EXQ-418d (P0_EPISODES=20, P1_EPISODES=40, STEPS_PER_EPISODE=150,
LAMBDA_TERRAIN=0.1, LAMBDA_CUE_ACTION=0.5).

  Arm                    | sd016_writepath_mode | sd016_diversification_weight
  -----------------------+----------------------+-----------------------------
  A0_off                 | "off"                | 0.0  (baseline, no writes)
  A1_writes_only         | "sense_only"         | 0.0  (replicates EXQ-418d arm A2)
  A2_div_only            | "off"                | 0.5  (tests if div alone breaks symmetry)
  A3_writes_plus_div     | "sense_only"         | 0.5  (full hypothesis bootstrap)

Acceptance (per-arm, all seeds must satisfy):

  C1 -- attn_entropy_mean < 2.65 in A2_div_only and A3_writes_plus_div.
        Quantifies departure from the uniform rail (uniform = 2.7726;
        cutoff 2.65 means ~5% reduction in attention entropy from uniform).

  C2 -- slot_diversity > 0.10 in A2_div_only and A3_writes_plus_div, all
        three seeds. This is the hard symmetry-breaking criterion: every
        seed must escape collapse, not just the lucky one. EXQ-418d had
        seed 42 escape across multiple arms but 43/44 collapse on all.

  C3 -- action_class_entropy_under_cue_bias differs by >= 0.20 nats
        between A0_off and A3_writes_plus_div. Confirms diversified
        slots produce behaviourally distinguishable cue_action_proj
        outputs (the production target).

  C4 -- A1_writes_only replicates the EXQ-418d FAIL pattern (slot_diversity
        bimodal across seeds, attn_entropy_mean ~ ln(16)). This is a
        sanity check: the new substrate doesn't accidentally fix the v2
        path, which would invalidate the ablation logic.

A PASS on C1+C2+C3 with C4 confirmed reproduces the v2 failure and isolates
the diversification loss as the active mechanism. A1_writes_only failing
to escape collapse while A3 escapes is the strongest evidence that
write-side EMA alone cannot drive slot differentiation.

A FAIL on C1 or C2 with `sd016_diversification_weight = 0.5` invalidates
Path 1 at this weight. The follow-up would be either (a) larger weights
(EXQ-418f sweep at 1.0, 2.0, 5.0) or (b) Path 2 / Path 3 from the original
3-path proposal (VQ-VAE codebook or feedforward tagger).

> **RESOLVED 2026-06-05.** Path (a) was taken: **V3-EXQ-418i** swept the
> diversification weight at 1.0 / 2.0 / 5.0 and FAILed C1 at every weight,
> concluding *"Path 1 alone is insufficient regardless of weight; the
> attention bottleneck is categorically in query selectivity, not slot
> orthogonality."* Path 1 is therefore exhausted. **Path 3 (feedforward
> tagger)** was selected over Path 2 (VQ-VAE codebook, more invasive) and is
> implemented as of 2026-06-05 -- see Section 7 below.

A FAIL on C3 with C1+C2 PASS would mean diversification works at the
slot level but doesn't propagate to behaviour -- the cue_action_proj path
is still uninformative even with non-uniform attention. That would
indicate the bottleneck is downstream of ContextMemory.

## 4. Default policy

After EXQ-418e validates Path 1, production defaults are set so SD-016
experiments running with `sd016_enabled=True` AND
`sd016_writepath_mode in {"sense_only", "train_only", "both"}` ALSO opt
into `sd016_diversification_weight=0.5`. Documented but not auto-coupled --
the explicit opt-in keeps the substrate auditable and lets ablation
experiments (e.g. A1_writes_only-style) run cleanly.

## 5. Out of scope

- Trained read-side projection of slots (would couple slot identity to
  task gradients more tightly than diversification alone, but adds a new
  trainable head and changes the latent geometry; deferred to a v4 if
  Path 1 PASS still leaves cue_context behavioural impact too small).
- Discrete slot codebook (VQ-VAE-style; original Path 2). More invasive
  substrate change; reserved if Path 1 fails.
- Removal of the v2 substrate (key_proj.bias=False, sd016_writepath_mode).
  Both Part A and Part B are kept -- diversification is additive.
- The EXQ-449a band-aid (z_world concat into cue_action_proj). Retained --
  removing it is a separate experiment after Path 1 lands and proves
  cue_context is informative.

## 6. References

- v2 design doc: REE_assembly/docs/architecture/context_memory_writepath_fix.md
- SD-016 cluster doc: REE_assembly/docs/architecture/sd_016_frontal_cue_integration.md
- EXQ-418d manifest: REE_assembly/evidence/experiments/v3_exq_418d_sd016_writepath_modes_comparison_20260425T141932Z_v3.json
- Substrate queue entry: REE_assembly/evidence/planning/substrate_queue.json (SD-016 implemented_but_failing_validation, priority 1)

## 7. Path 3: Feedforward cue->slot tagger (implemented 2026-06-05)

**Why Path 1 and Path 4 were not enough.** Path 1 (auxiliary slot
diversification loss) was swept across weights 1.0/2.0/5.0 by **V3-EXQ-418i**
and FAILed C1 at every weight: *the attention bottleneck is categorically in
query selectivity, not slot orthogonality.* Path 4 (learnable attention
temperature) gives the optimiser a selectivity knob but still routes through
the same `world_query_proj -> key_proj(memory)` scoring, which is the
saddle: with `memory` init 0.01 the slot keys are near-identical, the softmax
over them is near-uniform, and the softmax Jacobian at uniform is flat, so
`terrain_loss` gradient cannot push the attention off the `ln(num_slots)`
rail.

**Mechanism.** Path 3 replaces ONLY the slot-**selection** scoring inside
`extract_cue_context`. A fresh feedforward MLP

```
cue_slot_tagger:  z_world [world_dim]
                  -> Linear(world_dim, hidden) -> ReLU
                  -> Linear(hidden, num_slots)
                  -> slot_logits [num_slots]
selection_weights = softmax(slot_logits / temperature)
context = selection_weights @ value_proj(memory)
```

produces non-uniform logits from random init, so it sits **off** the saddle.
The slot-**content** path (`value_proj` -> `output_proj` -> `cue_context`) and
both downstream projections (`cue_action_proj`, retaining the EXQ-449a
`z_world` concat band-aid; `cue_terrain_proj`) are unchanged. The tagger is
trained by the **existing** `terrain_loss` gradient that already supervises
`cue_terrain_proj` -- no new supervised target is invented. Because the
tagger is not stuck at a flat saddle, that gradient now shapes contextual
selectivity (which it could not do through the attention scoring).

**Config (E1Config + REEConfig.from_dims; all no-op defaults):**

| Param | Default | Purpose |
|-------|---------|---------|
| `sd016_cue_slot_tagger` | `False` | master switch (requires `sd016_enabled=True`) |
| `sd016_cue_slot_tagger_hidden` | `32` | tagger MLP hidden width |
| `sd016_cue_slot_tagger_temperature` | `1.0` | softmax temp on tagger logits |

When `sd016_cue_slot_tagger=False` the legacy q.k attention branch runs
verbatim (bit-identical; verified OFF selection entropy == `ln(16)` exactly).
`extract_cue_context` caches the last selection distribution on
`E1DeepPredictor._last_cue_slot_weights` as a read-only diagnostic for the
validation experiment's selection-entropy metric.

**Scope honesty.** Path 3 restores RETRIEVAL (`cue_context`) selectivity.
Full behavioural `action_bias_div >= 0.05` propagation additionally depends on
`cue_action_proj`, whose gradient path is the separate **SD-055**
differentiable-CEM concern; the validation measures `action_bias_div` as a
secondary diagnostic, gated on SD-055.

**Validation.** Substrate-readiness diagnostic (`claim_ids=[]`), OFF vs ON
ablation. PRIMARY acceptance: mean selection entropy `< 2.5` (vs the pinned
`ln(16)=2.773`) with the tagger ON, on the real env where V3-EXQ-418i measured
the legacy attention stuck at ~2.76. SECONDARY: `cue_context` per-channel std +
safe-vs-dangerous `action_bias_div`. Implementation entry +
contracts (`tests/contracts/test_sd016_cue_slot_tagger.py`) recorded in
`ree-v3/CLAUDE.md`.

## 8. H3: Hard/competitive selection operator (implemented 2026-08-09)

**Why Path 3 alone was not enough.** **V3-EXQ-898**'s failure autopsy
(2026-08-08) found that even the Path 3 soft tagger, correctly rewarded by
`terrain_loss`, reproduced the exact uniform `ln(16)` attractor under its C2
control -- the same saddle Path 3 was built to escape. This raises hypothesis
**H3** (one leg of the **GOV-FANOUT-1** discrimination portfolio, alongside
H1/drive and H2/representation): a soft, end-to-end differentiable softmax
gate may not be able to **hold** a sparse, context-selective optimum even
when correctly rewarded -- gradient descent relaxes it back toward the
uniform attractor regardless of what the loss demands. H3 tests whether a
structurally competitive selector, independent of the downstream loss,
breaks the saddle where the soft gate could not.

**Mechanism.** A selection-mode knob on Path 3's slot-**selection** scores
only (the slot-content and downstream-projection paths remain untouched,
same discipline as Path 3):

```
sd016_cue_slot_tagger_selection: "soft" | "gumbel" | "topk"
  "soft"   -> softmax(slot_logits / temperature)              [Path 3, default]
  "gumbel" -> straight-through Gumbel-softmax, annealed temperature
  "topk"   -> straight-through top-k (k of num_slots)
```

Both `gumbel` and `topk` are straight-through estimators: the **forward**
pass is structurally sparse (one-hot for gumbel, exactly k nonzero slots for
topk) independent of what `terrain_loss` rewards; the **backward** pass
flows through the soft relaxation, so the tagger remains trainable by the
same gradient source as Path 3. `soft` is bit-identical to Path 3 by
construction (the original softmax line is unmoved, just reached through the
new mode dispatch's default branch).

**Config (E1Config + REEConfig.from_dims; all no-op defaults):**

| Param | Default | Purpose |
|-------|---------|---------|
| `sd016_cue_slot_tagger_selection` | `"soft"` | `"soft"` \| `"gumbel"` \| `"topk"` |
| `sd016_cue_slot_tagger_topk_k` | `1` | topk: slots kept active |
| `sd016_cue_slot_tagger_gumbel_tau_init` | `1.0` | gumbel: starting temperature |
| `sd016_cue_slot_tagger_gumbel_tau_min` | `0.1` | gumbel: floor temperature |
| `sd016_cue_slot_tagger_gumbel_anneal_steps` | `2000` | gumbel: linear anneal horizon (training-mode forward calls) |

**Null declaration.** If `gumbel`/`topk` fail C1 (entropy `< 2.5`) / C1b
(context-divergence `> 0.1`) with readiness met, hard selection alone does
not break the saddle -- implicating the drive (H1) or the representation
(H2), not the softness of the gate. A C1-pass/C1b-fail `topk` run (a fixed
slot selected regardless of context) is the "constant-peaky" degeneracy C1b
exists to catch.

**Validation.** H3 leg of the GOV-FANOUT-1 portfolio (arms `A0_OFF` /
`A1_tagger_soft` / `A2_tagger_gumbel` / `A3_tagger_topk`, inheriting the
V3-EXQ-898 scaffold), to be queued via `/queue-experiment`. Implementation
entry + contracts (`tests/contracts/test_sd016_h3_hard_selection.py`)
recorded in `ree-v3/CLAUDE.md`. Full portfolio design:
`REE_assembly/evidence/planning/sd016_selection_fanout_portfolio_scope_staged_20260809.md`
(section 3, "Leg H3").
