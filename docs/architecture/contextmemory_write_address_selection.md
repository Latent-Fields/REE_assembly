---
title: ContextMemory write-address selection
parent: "Core Engines & Forward Models"
grandparent: Architecture
nav_order: 1
---

# ContextMemory write-address selection

**substrate_queue id:** `contextmemory-write-path-addressing-degeneracy`
**Severity:** `corrupting`
**Status:** IMPLEMENTED (two mechanisms) 2026-08-19 -- VALIDATION PENDING for both
**Substrate:** `ree-v3/ree_core/predictors/e1_deep.py` (`ContextMemory`), `ree_core/utils/config.py`
**Unblocks:** SD-017, ARC-045, MECH-166 -- *once validated*; see "What this does not unblock"
**Plan of record:** `REE_assembly/evidence/planning/contextmemory_refractory_mode_dataflow_plan_20260819.md`
**Measurement of record:** `REE_assembly/evidence/planning/contextmemory_write_selection_comparison_20260819.md`

This is the WRITE-side sibling of `SD-016`, which is scoped to cue-indexed
RETRIEVAL and is already `implemented`. It is deliberately a separate entry: the
read path and the write path fail for different reasons and are fixed by
different mechanisms.

> **Provenance note.** An earlier draft of this document existed untracked in the
> working tree from 2026-08-18. It described a four-mode implementation
> (`argmin`/`refractory`/`usage`/`gumbel`) that was never landed, and it drew its
> recommendation partly from an occupied-slot cosine column that a subsequent
> independent probe showed **cannot discriminate the arms at 5 seeds**. This
> version supersedes it: two modes exist, and the recommendation now rests only
> on the deterministic measurements. The superseded draft's implementation
> survives in ree-v3 tag `stash-archive/20260819-dd4b0a4` (LOCAL-ONLY to DLAPTOP).

---

## Problem

`ContextMemory.read()` addresses by softmax over `query_proj(query) . key_proj(memory)`.
`ContextMemory.write()` addressed by a hard `scores.mean(0).argmin()`.

Under a near-constant query stream that hard argmin is a **deterministic
single-slot fixed point**. The mechanism is an addressing-space misalignment,
not bad luck in the initialisation:

- the ADDRESS is computed in `query_proj(x)` space;
- the PAYLOAD written is `write_gate(x) * write_content(x)`, an **unrelated**
  linear map of the same state;
- so blending the payload into the argmin slot can push that slot **further
  from** the query, which re-selects it on the next write, permanently.

V3-EXQ-436e established the closed-form sign discriminator

```
q . (write_signal - memory[argmin])      negative -> LOCK,  positive -> ROTATE
```

which predicted lock-vs-rotate 5/5, and is re-confirmed 5/5 independently by
`test_sign_discriminator_predicts_lock_versus_rotate`.

### Why `corrupting` rather than merely wrong

`write()` returns normally, thousands of calls are logged, and the readout is
well-formed. The resulting 1-slot bank yields a clean null that reads as a
genuine "sleep has no effect" finding. It has produced exactly that artefact
twice:

| run | observation |
|---|---|
| V3-EXQ-436e | single-slot occupancy; discriminator predicted it 5/5 |
| V3-EXQ-436f | `n_occupied_slots = 1 of 16` in BOTH arms on 3/5 seeds (7, 13, 100) despite 2,837-4,903 `write()` calls per arm, giving `n_scoreable_seeds = 2` against a registered floor of 3 |

436f had the full SD-016 production combination ARMED and confirmed engaged
(pooled applied ctxdiv loss 25,796.28 against a 1e-9 floor). **The read-path fix
changes write-path occupancy by ZERO seeds.** `compute_diversification_loss()`
acts on `self.memory`, but the write update runs under `torch.no_grad()` and is
therefore unaffected by it -- it is not a mitigation for this.

---

## Solution: two orthogonal mechanisms, both default-off

| mechanism | config | what it changes | landed |
|---|---|---|---|
| conscience bias | `contextmemory_write_usage_balancing` (bool, `False`) | the **score**: `argmin(mean_scores + w * usage_ema * sqrt(memory_dim))` | ree-v3 `76cbf844`, 2026-08-19 |
| refractory | `contextmemory_write_selection` (str, `"argmin"`) | the **eligible set**: argmin over slots outside the last-`k` window | ree-v3, 2026-08-19 |

Supporting params: `contextmemory_write_usage_bias_weight` (1.0),
`contextmemory_write_usage_decay` (0.99), `contextmemory_write_refractory_k` (2).
All threaded through `REEConfig.from_dims` at **all three** sites -- `from_dims`
silently swallows unknown kwargs, so a knob wired at two of three fails open and
silently.

`contextmemory_write_selection` accepts only `"argmin"` and `"refractory"`.
Anything else raises at construction. Fail-closed on purpose: a typo that
silently fell back to `"argmin"` would reinstate a `corrupting` defect under a
config claiming to have fixed it. `"usage"` and `"gumbel"` are rejected **by
name**, because they existed on the superseded draft (see below) and a config
carrying them over must error rather than degrade.

**They compose.** The bias decides how good each slot looks; the mask decides
which slots may be looked at. All four combinations are legal. This is
deliberate rather than a missing mutual exclusion -- mutual exclusion would
require a raise or a silent precedence rule, whereas the composition is well
defined and measurable, so it becomes an available arm instead of a
configuration error. **Measured caveat:** at the default bias weight the usage
term dominates content by 2-3 orders of magnitude, so the composed arm is
byte-identical to the bias alone -- the mask never binds. Enabling both is legal
but buys nothing today. Pinned by
`test_the_conscience_bias_subsumes_the_refractory_mask_at_default_weight`, which
will go red if that relative scaling ever changes.

Backward compatible: with defaults the write path is **bit-identical** to the
pre-change code -- verified as an identical slot sequence AND an identical final
memory tensor over 5 seeds x 200 writes. `refractory` consumes **no RNG** in any
mode (it is fully deterministic), so no existing seeded trajectory shifts.
`slot_write_counts` is `persistent=False`, so `state_dict()` is unchanged and
existing checkpoints load untouched.

---

## Measurement, and the trap it exposes

The measurement of record is the independently pre-registered probe
(pre-registration `REE_assembly` `fcfb311e4b`, committed **before** execution;
results `b7e072ddf0`). It reproduced the superseded draft's published table to
4 dp on 8 of 9 quantities, using **independent instrumentation** (the written
slot recovered by diffing `memory` across each write, never by re-deriving the
selection expression).

### The robust, deterministic columns

Degenerate stream, 5 seeds. Lower `self_repeat` is better; round-robin agreement
is the fraction of writes landing on the strict least-recently-used slot.

| arm | seeds with >= 2 slots | distinct slots per seed | entropy (bits) | HHI | round-robin agreement |
|---|---|---|---|---|---|
| `argmin` (legacy) | 3/5 (**LOCKS**) | [1, 14, 11, 14, 1] | 2.00 | 0.473 | 0.000 |
| + `write_usage_balancing` | **5/5** | [16, 16, 16, 16, 16] | **4.00** exactly | **0.0625** exactly (1/16) | **0.991** |
| `refractory` k=2 | **5/5** | [3, 13, 11, 14, 3] | 2.67 | 0.201 | 0.000 |

Both mechanisms clear the registered acceptance floor (`>= 2` occupied slots on
`>= 3/5` seeds), decisively. **So occupancy cannot choose between them.**

The conscience bias's `sqrt(memory_dim)` = 11.31 scaling puts the usage term
2-3 orders of magnitude above the ~0.026 across-slot spread of `mean_scores`, so
after the first pass the write address is a function of the write **counter**
rather than of the query: a fixed period-16 LRU cycle on ~99% of writes. That is
a real improvement on every occupancy metric, and it is **not** globally
content-blind -- the cycle's *ordering* is content-determined once (agreement
across different content streams is only 0.113), then frozen. But "16 slots
visited in a fixed order regardless of query" is **occupancy without
addressing**, and it is worth naming plainly rather than reading 5/5 off a table.

`refractory` masks only the last `k` slots and leaves selection among the rest
as the **unmodified content argmin**. Consequently its occupancy varies with the
stream and tracks legacy's exactly on the three seeds where legacy does not lock
([_, 13-14, 11, 14, _]), while the bias returns 16 on every seed regardless.

### The column that does NOT discriminate -- do not quote it

The superseded draft recommended `refractory` partly on an occupied-slot cosine
gap of +0.6060 -> +0.5919. **That gap is dz = -0.06, t(4) = -0.13.** Across all
contrasts the column is |dz| <= 0.47, |t(4)| <= 1.04, and sign-inconsistent
across seeds. Required n at 80% power is 38 (usage vs legacy), 58
(landed vs refractory), 149 (landed vs legacy), 2485 (refractory vs legacy).

The draft's cluster-Jaccard detector was also the **wrong instrument**: a
period-16 cycle aliases against a 2-cluster alternation, giving Jaccard exactly
0.0 on 3/5 seeds and exactly 1.0 on 2/5 -- a bimodal artifact whose mean (0.400)
looks moderate and which therefore failed to flag the round-robin behaviour at
all. The round-robin index above is the metric that should have been
pre-registered, and it is what the contract now asserts on.

**No contract in this area asserts on occupied-slot cosine.** A test pinning a
quantity with that spread at n=5 is a flake generator wearing a contract's
clothes.

### Why `refractory` is available anyway

Three reasons, none of which is the cosine column:

1. **Structural guarantee.** `n_occupied >= k+1` holds **by construction**, for
   any stream, seed or initialisation. The conscience bias reaches full
   occupancy *empirically*, on the streams measured.
2. **It is the only arm that does not become counter-driven** (round-robin
   0.000 vs 0.991).
3. **Biological grounding.** An absolute refractory period on a recently-active
   unit is a first-order property of real neurons. A global usage-EMA conscience
   bias is not.

**Neither mechanism is declared the winner.** That is the validation
experiment's job.

---

## Modes investigated and deliberately NOT landed

| mode | rule | why not |
|---|---|---|
| `usage` | `argmax(-z(sim) - w * z(usage_ema))` | measured content-blind (cluster Jaccard 0.600). Also a **different algorithm** from the landed conscience bias despite the shared name -- they must not be conflated. |
| `gumbel` | annealed Gumbel over that availability score | measured content-blind at Jaccard **exactly 1.000 on 5/5 seeds** -- both contexts write the same slot set. The probe's most robust negative result. Also would consume RNG, shifting every seeded trajectory. |

The substrate_queue `implementation_hint` proposed exactly the `gumbel` route
("apply the annealed Gumbel-softmax selection that V3-EXQ-908 confirmed works on
the READ path to the WRITE address"). **Following it would have satisfied the
registered acceptance criterion while swapping one corrupting defect for a
quieter one.** The read-path result does not transfer, because there Gumbel
sparsification is applied to *learned, gradient-shaped* slot logits, whereas the
write path has no gradient at all: the same operator that sharpens a trained
distribution merely randomises an untrained one. This is the single most
important thing on this page for anyone re-reading the hint.

Relatedly, the gumbel implementation carried no straight-through estimator, and
that was correct: `write()` runs entirely under `torch.no_grad()`, so the ST
algebra would have been dead code falsely implying a learning signal.

---

## Instrumentation change (read this before writing a driver)

`ContextMemory` records the slot it actually wrote: `last_write_index`,
`slot_write_counts`, `occupied_slots()`. These are maintained in **every** mode
including the legacy default.

V3-EXQ-436f's `_install_write_tracker` learned the written slot by
**duplicating** `write()`'s own `scores.mean(0).argmin()` expression. That
re-derivation silently reports the WRONG slot the moment the selection rule
changes -- and it has now changed twice. Any new driver must read these fields
instead of re-deriving. Pinned by
`test_stale_reimplementation_of_the_old_rule_disagrees`.

---

## Validation

**Contract tests:** `ree-v3/tests/contracts/test_contextmemory_write_address_selection.py`
(refractory) and `test_contextmemory_write_usage_balancing.py` (conscience bias)
-- 51 together, time-independent, constructing `ContextMemory` directly with no
environment or runner dependency. Roughly half are negative controls: the defect
pin itself, bit-identity of the default, RNG non-consumption, the unchanged
`state_dict`, the landed knobs untouched, and
`test_landed_usage_balancing_is_a_fixed_cycle_and_refractory_is_not`, which stops
either mechanism being promoted on its occupancy number alone.

**Validation EXPERIMENT: still PENDING, for BOTH mechanisms.** The
substrate_queue status stays `implemented_pending_validation`. The contract tests
validate the mechanism at the `ContextMemory` unit level against a synthetic
degenerate stream -- not on a real agent under the 436e/436f harness. Chipped as
`chip-20260819-queueexp-contextmemory-writesel-validation`.

Two constraints that experiment must carry:

1. **Neither flag can be left at its default.** No driver in `ree-v3/experiments/`
   sets either; a driver written today runs the unfixed `argmin` path and walks
   straight back into the corrupting defect.
2. **Do not power the comparison on occupied-slot cosine** (see above). Use the
   deterministic DVs: occupancy, self-repeat, entropy, round-robin index.

### What this does not unblock

Landing two default-off knobs changes no driver's behaviour. It therefore does
**not** unblock `chip-20260818-sd017-ceiling-retest-gated` or
`chip-20260818-mech152-redesign-queue-gated`, both of which stay gated: the
flags are off, no driver sets them, and the `occ_cos` DV still cannot
discriminate at the powers those experiments were run at. SD-017 / ARC-045 /
MECH-166 are unblocked only once the validation experiment above has run with a
flag explicitly enabled.
