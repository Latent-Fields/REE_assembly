---
title: ContextMemory write-address selection
parent: "Core Engines & Forward Models"
grandparent: Architecture
nav_order: 1
---

# ContextMemory write-address selection

**substrate_queue id:** `contextmemory-write-path-addressing-degeneracy`
**Severity:** `corrupting`
**Status:** IMPLEMENTED (THREE mechanisms) -- bias/refractory 2026-08-19, gumbel_learned 2026-08-27 -- VALIDATION PENDING for all three
**Substrate:** `ree-v3/ree_core/predictors/e1_deep.py` (`ContextMemory`, `E1DeepPredictor`), `ree_core/utils/config.py`, `ree_core/agent.py` (`REEAgent.compute_prediction_loss`)
**Unblocks:** SD-017, ARC-045, MECH-166 -- *once validated*; see "What this does not unblock"
**Plan of record:** `REE_assembly/evidence/planning/contextmemory_refractory_mode_dataflow_plan_20260819.md`
**Measurement of record:** `REE_assembly/evidence/planning/contextmemory_write_selection_comparison_20260819.md`

> **2026-08-27 update.** HUMAN DECISION 2026-08-26 (via `/metaworker-orchestrate`,
> informed by `failure_autopsy_V3-EXQ-943_2026-08-21`): neither bias nor
> refractory closes the corrupting defect as a matter of addressing POLICY --
> both are mechanical occupancy workarounds, not a learned/content-based
> write-selection mechanism. The substrate_queue entry's own
> `implementation_hint` was directed to be built: annealed Gumbel-softmax,
> matching V3-EXQ-908's confirmed READ-path mechanism. See the new
> **"THIRD mechanism"** section below for what was built, and read it in full
> before assuming this closes the "swapping one corrupting defect for a
> quieter one" concern the ORIGINAL version of this page (2026-08-19, still
> below under "Modes investigated and deliberately NOT landed") raised against
> exactly this route -- it does not close it outright; it answers the specific
> "no gradient at all" critique with a real, verified gradient path, and then
> measures that the resulting mechanism's CONTENT-DISCRIMINATION is still not
> demonstrated. Read both sections; neither supersedes the other.

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

`contextmemory_write_selection` accepts `"argmin"`, `"refractory"`, and
(2026-08-27) `"gumbel_learned"` -- see the THIRD mechanism section below.
Anything else raises at construction. Fail-closed on purpose: a typo that
silently fell back to `"argmin"` would reinstate a `corrupting` defect under a
config claiming to have fixed it. `"usage"` and bare `"gumbel"` are rejected
**by name**, because they existed on the superseded draft (see below) and a
config carrying them over must error rather than degrade. `"gumbel_learned"`
is a deliberately DIFFERENT string from the rejected `"gumbel"`, not a
resurrection of it under the same name -- see below for why they are
different mechanisms.

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

## THIRD mechanism: `contextmemory_write_selection="gumbel_learned"` (2026-08-27)

**Why this exists despite the section above.** HUMAN DECISION 2026-08-26
(substrate_queue `implementation_note`, via `/metaworker-orchestrate`): bias
and refractory are both mechanical occupancy workarounds, not a learned
write-selection policy, and neither closes the corrupting defect as a matter
of POLICY. The build directed: apply the annealed Gumbel-softmax mechanism
V3-EXQ-908 confirmed on the READ path to the WRITE address -- the entry's own
`implementation_hint`, and exactly the route the section above says was
"investigated and deliberately NOT landed."

**This is not a contradiction, and here is the distinction.** The section
above is right that the *specific implementation it measured* -- a
Gumbel-perturbed argmax over write()'s own untrained `query_proj(state) @
memory.T` score, no separate training signal -- was, and remains, the wrong
build: it reproduces exactly the read-path's OWN mechanism structurally while
skipping the reason that mechanism works on the read path (a real task loss
shaping the logits). What follows is a build that specifically closes that
gap with a verified gradient path, together with the honest result of testing
whether closing it is *sufficient*.

### What V3-EXQ-908 actually is, precisely

The phrase "the confirmed read-path Gumbel mechanism" is easy to mis-locate.
It is **not** the legacy `query_proj`/`key_proj` q.k attention inside
`ContextMemory.read()` -- that path was independently diagnosed
(V3-EXQ-418i) as pinned at the uniform softmax saddle (`self.memory`'s
`0.01`-scale init leaves near-zero cross-slot score variance) and abandoned
for exactly that reason. The confirmed mechanism is
`E1DeepPredictor._sd016_gumbel_select()` applied to `cue_slot_tagger`'s
output -- a **fresh feedforward MLP** (`world_dim -> hidden -> num_slots`)
that never touches `self.memory`'s scale at all, trained by `terrain_loss`
gradient flowing back through `cue_terrain_proj`. The first build attempt
here scored a `query.memory` dot product (matching write()'s own legacy
expression, not the tagger), and paid for that mismatch exactly as the read
path's own q.k attention did:

```
scores = write_query_proj(state) @ memory.T      # measured: near-zero cross-slot variance
loss = MoE-load-balancing(scores)                # measured: stuck at ~1.0 (its own minimum)
```

50 SGD steps at lr=0.1, batch 16: `compute_write_addressing_loss` sat at
`1.0000` to 4 significant figures, moving nowhere. Replacing the dot product
with a dedicated tagger (`write_addr_tagger`, same shape as
`cue_slot_tagger`) fixed the saddle -- gradient reaches the tagger's
parameters immediately and is nonzero -- but that alone was not the whole
fix; see below.

### The mechanism as landed

| piece | what it does |
|---|---|
| `ContextMemory.write_addr_tagger` | `Linear(latent_dim, hidden) -> ReLU -> Linear(hidden, num_slots)`. Constructed ONLY when `write_selection="gumbel_learned"`. Same shape family as `cue_slot_tagger`, deliberately NOT reusing `query_proj` (that would make this mode's training signal compete with `read()`'s own retrieval-quality objective for the same parameters). |
| `ContextMemory._select_write_slot_gumbel()` | Annealed straight-through Gumbel-max over `write_addr_tagger`'s scores, negated to preserve the "lower score wins" convention `_select_write_slot` already uses for argmin/refractory. Runs entirely inside `write()`'s existing `torch.no_grad()` block -- adds NO gradient of its own. Eval mode is bit-identical to plain `argmin` on the tagger's own scores (no noise, no step-counter advance); train mode samples Gumbel(0,1) noise every call. |
| `ContextMemory.compute_write_addressing_loss(states)` | A SEPARATE, explicit, fresh forward pass the training loop calls -- **not** anything reused from inside `write()`. This is the piece `compute_diversification_loss()` never provided: gradient into write-ADDRESS selection, not just memory content. |
| `REEConfig.contextmemory_write_addressing_loss_weight` | Top-level (not `E1Config`-scoped, mirroring `sd016_diversification_weight`'s own placement and the 2026-08-22 repair note beside it). `0.0` default = no-op. Wired into `REEAgent.compute_prediction_loss()` beside the existing diversification-loss term, gated on `weight > 0.0 AND write_selection == "gumbel_learned"`. |

**Why `compute_write_addressing_loss` is a separate fresh forward pass, not
anything `write()` computes.** `write()`'s content update
(`self.memory.data[idx] = ...`) is a raw `.data` write with no autograd
version tracking (that is deliberate -- see the "Solution" section above). A
soft selection tensor captured *inside* `write()` and consumed by
`.backward()` at some *later* point, after further `write()` calls have
mutated `self.memory.data` in between, would silently differentiate through
the CURRENT memory values rather than the ones actually present at that
forward pass -- wrong gradients, no error raised, because `.data` writes
bypass the version-counter check that would normally catch this.
Recomputing fresh from a caller-supplied batch of already-detached states
(the same convention every `write()` call site in `agent.py` already
follows) avoids the hazard entirely.

### FIRST-attempt loss design, measured, and why it was replaced

The first version of `compute_write_addressing_loss` was the standard MoE
routing-collapse fix (Shazeer et al. 2017, "Outrageously Large Neural
Networks", eq. 8 -- the ML/AI parallel chosen because the *engineering*
problem is analogous, not the theory): minimize the squared deviation of the
BATCH-MEAN selection probability from uniform,
`num_slots * (mean_probs ** 2).sum()`.

Measured, 5 seeds, 300 SGD steps each on a 2-cluster content-conditioning
stream (the same instrument `test_refractory_preserves_content_conditioning`
uses): the loss converged smoothly to its own minimum (~1.0002-1.0003) and
`occupied_slots()` was 16/16 on every seed -- but **2-cluster Jaccard was
EXACTLY 1.000 on 5/5 seeds.** That is the identical failure signature the
superseded draft's rejected `gumbel` mode was measured at. The mechanism:
batch-mean uniformity has a degenerate minimum, satisfied equally by "every
example independently prefers a near-uniform distribution" (content-blind)
and by "different examples prefer different PEAKED distributions that
average out to uniform" (content-conditioned, the wanted outcome) -- and with
annealed Gumbel noise already guaranteeing full occupancy regardless of what
the tagger has learned, nothing in that loss pushed toward the second
solution over the first. A real, verified, nonzero gradient path is not the
same thing as a gradient path that shapes the RIGHT distinction.

**Replaced with a pairwise-diversity form**, deliberately mirroring
`compute_diversification_loss()`'s own structure -- mean squared
off-diagonal cosine similarity, applied to PER-EXAMPLE selection
distributions (`softmax(-write_addr_tagger(state))`) instead of memory rows:

```python
probs = softmax(-write_addr_tagger(states), dim=-1)      # [N, num_slots]
probs_norm = normalize(probs, dim=-1)
sim = probs_norm @ probs_norm.T                            # [N, N]
loss = mean_offdiag((sim) ** 2)                             # minimize
```

Two near-uniform distributions ARE highly cosine-similar to each other (both
close to the constant `1/num_slots` vector), so the degenerate "everyone
converges to near-uniform" solution scores HIGH under this loss, not low --
the gradient pushes explicitly away from it, unlike the load-balancing form.
This is the direct, structural answer to "how does this interact with
`compute_diversification_loss()`" that the substrate_queue
`implementation_hint` asked to be considered: the two losses are the SAME
idea (mean squared off-diagonal cosine similarity, minimized) applied to
complementary objects -- one to memory CONTENT, one to per-example write
ADDRESS SELECTION -- exactly parallel to how the bias/refractory mechanisms
above are one SCORE rule and one ELIGIBILITY rule. They are orthogonal and
can be trained together; no interaction beyond sharing no parameters.

### What is proven, and what is explicitly NOT

**Proven, unit-level, deterministic (contract tests):**

1. Gradient reaches `write_addr_tagger`'s parameters and is nonzero
   (`test_gradient_reaches_write_addr_tagger`) -- the concrete, checkable
   difference from the rejected `gumbel` mode, which had no such path at all.
2. `write()` itself stays entirely `torch.no_grad()` in this mode too -- no
   retained per-call graph (`test_write_itself_stays_fully_no_grad`).
3. Occupancy floor (`>= 2` occupied on `>= 3/5` seeds) is cleared decisively
   -- in fact 16/16 on every one of the 5 measured seeds -- **independent of
   training**, delivered by Gumbel noise alone even for a freshly
   initialised, completely untrained tagger.
4. Eval-mode selection is EXACTLY (not approximately) equal to plain argmin
   on the tagger's own scores, and consumes no RNG; train-mode DOES consume
   RNG (a real, documented behaviour difference from argmin/refractory, which
   remain RNG-free in every mode).
5. Bit-identical default (`write_selection="argmin"`); `write_addr_tagger`
   and its state_dict keys are constructed ONLY in this mode.

**NOT proven, and not claimed:**

1. **Content-discrimination is not demonstrated.** The pairwise-diversity
   loss is the theoretically correct fix for the specific degenerate-minimum
   failure measured in the load-balancing attempt above, not a proven result
   in its own right. A toy training loop (300 steps, small batch, SGD) run
   during this build did not move it off its own near-uniform starting point
   in the time available -- consistent with, and not distinguishable from,
   the SAME symmetry-breaking difficulty `compute_diversification_loss()`
   itself is documented as having (EXQ-418d: "v2 read+write gradients alone
   cannot break slot symmetry"; that loss needed a real experiment,
   V3-EXQ-907, run over a full training schedule, to show effect -- not a
   short synthetic script). Whether `contextmemory_write_addressing_loss_weight`
   at a realistic weight, over a realistic training schedule, actually
   produces content-conditioned addressing is exactly the open question the
   validation experiment below must answer.
2. This build does **not** itself close the substrate_queue entry's
   corrupting defect as a validated fix. Status stays
   `implemented_pending_validation`, for all three mechanisms now, not just
   the two from 2026-08-19.

**Contracts:** `ree-v3/tests/contracts/test_contextmemory_write_gumbel_learned.py`
(26 tests, time-independent, `ContextMemory` constructed directly). Assertion
policy extends the sibling files': no assertion claims content-discrimination
is achieved; assertions are on mechanical correctness (gradient reachability,
RNG consumption exactly where documented, config validation, defaults
untouched) and on the one thing this mode decisively delivers regardless of
training -- occupancy.

**Validation experiment for THIS mechanism needs a real training loop, unlike
the other two.** Bias and refractory need no training to evaluate (both are
deterministic transformations of an untrained score); `gumbel_learned`'s
open question is specifically about what training does to
`write_addr_tagger`, so a driver measuring it must actually run
`contextmemory_write_addressing_loss_weight > 0` through real SGD steps
across an episode/training schedule, not just flip the selection flag on an
untrained agent. This is a new constraint beyond the two the existing
validation chip (`chip-20260819-queueexp-contextmemory-writesel-validation`)
already carries.

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
-- 51 together -- plus (2026-08-27)
`test_contextmemory_write_gumbel_learned.py` (26, see the THIRD mechanism
section above for its own assertion policy). 77 total, time-independent,
constructing `ContextMemory` directly with no environment or runner
dependency. Roughly half of the first two files are negative controls: the
defect pin itself, bit-identity of the default, RNG non-consumption, the
unchanged `state_dict`, the landed knobs untouched, and
`test_landed_usage_balancing_is_a_fixed_cycle_and_refractory_is_not`, which stops
either mechanism being promoted on its occupancy number alone.

**Validation EXPERIMENT: still PENDING, for ALL THREE mechanisms.** The
substrate_queue status stays `implemented_pending_validation`. The contract tests
validate each mechanism at the `ContextMemory` unit level against a synthetic
degenerate stream -- not on a real agent under the 436e/436f harness. Chipped as
`chip-20260819-queueexp-contextmemory-writesel-validation` (bias/refractory;
does not yet cover gumbel_learned -- see the THIRD mechanism section's own
validation note for the additional constraint a gumbel_learned driver needs
that the other two do not: an actual training loop, not just the flag).

Constraints any such experiment must carry:

1. **No flag can be left at its default.** No driver in `ree-v3/experiments/`
   sets any of them; a driver written today runs the unfixed `argmin` path and
   walks straight back into the corrupting defect.
2. **Do not power the comparison on occupied-slot cosine** (see above). Use the
   deterministic DVs: occupancy, self-repeat, entropy, round-robin index.
3. **For `gumbel_learned` specifically**: `contextmemory_write_addressing_loss_weight`
   must be > 0 AND the driver must actually run enough training steps for it to
   matter -- flipping `write_selection="gumbel_learned"` alone (weight at its
   0.0 default) exercises only the Gumbel-noise occupancy effect, not the
   still-unproven content-discrimination question this mechanism exists to
   answer.

### What this does not unblock

Landing default-off knobs changes no driver's behaviour. It therefore does
**not** unblock `chip-20260818-sd017-ceiling-retest-gated` or
`chip-20260818-mech152-redesign-queue-gated`, both of which stay gated: every
flag is off, no driver sets any of them, and the `occ_cos` DV still cannot
discriminate at the powers those experiments were run at. SD-017 / ARC-045 /
MECH-166 are unblocked only once the validation experiment above has run with
a mechanism explicitly enabled AND (for `gumbel_learned`) actually trained.
