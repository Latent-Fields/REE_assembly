---
nav_exclude: true
---

# ContextMemory.write_gate bias-over-content audit (V3-EXQ-436c / V3-EXQ-861a follow-up)

Status: COMPLETE, 2026-08-03. Substrate fix landed behind a default-OFF config
flag (`contextmemory_gated_content_write`). Awaiting a 436-family re-run under a
new letter (e.g. V3-EXQ-436d) with the flag ON.

Scope: the audit requested by the `failure_record` entry of
`substrate_queue.json` -> `MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION`, added by
`failure_autopsy_V3-EXQ-436c_2026-08-03` and cross-referenced by
`failure_autopsy_V3-EXQ-861a_2026-08-03`.

## Headline

**The write path is broken, the autopsy pointed at the right module, and the fix
it proposed does not work.**

The autopsy hypothesised that `ContextMemory.write_gate` carries the same
bias-over-content collapse found and fixed on `key_proj`'s read path (SD-016
Part A / V3-EXQ-477 EXP-0155), and recommended the analogous remedy: remove or
zero-init the bias. Measured directly:

- The bias premise **holds**: `bias_over_content_ratio = 1.60` at the live
  operating point (`||b|| = 0.847` vs mean `||W x|| = 0.528`), i.e. the bias term
  does exceed the content term. Compare key_proj's 9.88 (pre-train) / 3.41 (post-P0).
- Removing the bias **changes nothing**. A/B on the same load:
  `const_over_varying` 44.87 -> 44.78, post-800-write slot cosine similarity
  0.999910 -> 0.999914.

Had the recommended fix been applied on the strength of the ratio alone, it would
have looked justified, changed no observable, and burned a V3-EXQ-436d re-run.

## What is actually wrong

`ContextMemory.write()` uses `write_gate`'s **post-sigmoid output as the write
payload**:

```python
write_signal = self.write_gate(state)          # Sequential(Linear, Sigmoid)
self.memory.data[min_idx] = (
    0.9 * self.memory.data[min_idx] + 0.1 * write_signal.mean(0)
)
```

A sigmoid output is confined to `(0, 1)`. At this module's operating point every
channel sits within +-0.02 of 0.5, so every write blends the selected slot toward
the **same** vector `0.5 * ones(memory_dim)`. Repeated writes therefore drag the
whole bank onto one point -- homogenization, which is exactly the direction
V3-EXQ-436c measured and the opposite of what SD-017 / ARC-045 / MECH-166 predict.

The constant is **sigmoid's own midpoint, not the bias**, which is why the bias
fix cannot touch it:

| quantity | measured | `\|\|0.5*ones(128)\|\|` |
|---|---|---|
| `\|\|mean write_signal\|\|`, bias present | 5.6589 | 5.6569 |
| `\|\|mean write_signal\|\|`, bias zeroed | 5.6568 | 5.6569 |

It agrees to four significant figures with the sigmoid midpoint in both cases.
No change to `b` can move a constant that `b` does not produce.

### Live operating point

Measured by instrumenting `ContextMemory.write` on a real agent built by
`experiments/v3_exq_436c_sd017_mech166_repr_confirmer.py::_make_agent`, over the
writes issued by `REEAgent.run_sws_schema_pass()`:

```
state ||x||       mean 0.6266   min 0.4118   max 0.7041
state rms         mean 0.0783   min 0.0515   max 0.0880
content ||W x||   mean 0.5279   min 0.3377   max 0.6017
bias ||b||             0.8468
bias_over_content_ratio = 1.6040

write_gate output (the vector actually blended into the slot):
  elementwise mean 0.4998   std 0.0223   min 0.4481   max 0.5550
  ||mean gate vector||        = 5.6604
  mean ||gate - mean gate||   = 0.0293
  const_over_varying_ratio    = 193.2
  mean pairwise cos sim of WRITTEN vectors = 0.999961
```

Replaying 436c's pooled write load (800 writes, batch=1 per write, the real
`write()`) drives whole-bank slot cosine similarity from ~0.001 to
**{0.9999, 0.9999, 1.0000, -0.0120, 0.2776}** over seeds 0-4 -- 3/5 fully
collapsed, closely matching 436c's reported ~0.9999-1.0 in 4/5 seeds.

## The fix

The defect is semantic: a *gate* should **modulate** content, not **be** content.
`write_gate` is named a gate but there is no content term for it to gate.

`contextmemory_gated_content_write=True` restores the namesake role:

```python
write_signal = sigmoid(write_gate_pre(x)) * write_content(x)
```

`write_content` is `nn.Linear(latent_dim, memory_dim, bias=False)`.

**`bias=False` is load-bearing, and it is where SD-016 Part A's insight genuinely
applies.** With a default-init bias on `write_content` the payload collapses back
onto a constant `sigmoid(.) * b_c` and the repair only half-works:

| `write_content` | bias/content | const/vary | written pairwise cos sim | slot cos sim after 800 writes |
|---|---|---|---|---|
| `bias=True` | 1.56 | 1.56 | 0.707 | 0.968 |
| `bias=False` | -- | 0.07 | 0.00023 | 0.006 - 0.049 |

So the autopsy's mechanism was real and its remedy was right -- for the wrong
projection. It belongs on the content path, which did not exist until this fix
created it.

### Result

| | legacy (`False`) | gated (`True`) |
|---|---|---|
| `const_over_varying_ratio` | 44.9 | 0.07 |
| written-vector pairwise cos sim | 0.99950 | 0.00023 |
| slot cos sim after 800 writes, seeds 0-4 | 0.9999, 0.9999, 1.0000, -0.0120, 0.2776 | 0.0062, 0.0491, 0.0434, 0.0288, 0.0319 |

## Backward compatibility

Default `False`. The `write_content` parameter is **not constructed** when the
flag is off, so the module is bit-identical to the legacy path -- parameter set,
`state_dict`, and per-write arithmetic all unchanged. No in-flight experiment
changes semantics until it opts in via
`REEConfig.from_dims(contextmemory_gated_content_write=True)`.

## Relationship to the V3-EXQ-861a finding

Both autopsies converge on this write path, but they name **two independent
defects**, and this audit closes only one of them:

- **This one (436c)** -- the write *payload* is a near-constant sigmoid output.
  Fixed here.
- **861a** -- `run_sws_schema_pass()`'s novelty reference,
  `ThetaBuffer.consolidation_summary()`, is a 10-tick self-referential recency
  average, structurally decoupled from the world_rule_shift / MEL axis. **Still
  open**; it sits upstream of `write()` in the SWS pass and is untouched by this
  change.

Fixing the payload does not repair 861a's `selection_weight`, and vice versa. A
re-run of the 861 family should wait for the 861a repair; a re-run of the 436
family can proceed on this fix alone.

## Files

- `ree-v3/ree_core/predictors/e1_deep.py` -- `ContextMemory.__init__` / `.write`
- `ree-v3/ree_core/utils/config.py` -- `E1Config.contextmemory_gated_content_write`,
  plumbed through `REEConfig.from_dims`
- `ree-v3/tests/contracts/test_contextmemory_gated_content_write.py` -- 18 tests,
  time-independent, CPU-only. Pins OFF-inertness, ON-differentiation, a paired
  same-seed OFF-vs-ON comparison, a regression pin on the defect itself, and
  `test_legacy_constant_is_the_sigmoid_midpoint_not_the_bias`, which fails if a
  later session re-derives the autopsy's hypothesis and "fixes" it by removing
  the bias.
