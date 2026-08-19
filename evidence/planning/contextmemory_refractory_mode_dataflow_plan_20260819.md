# ContextMemory `refractory` write-selection mode -- data-flow plan

**Status: AWAITING USER REVIEW.** The BUILD was authorised by the user on 2026-08-19
(option (c) of `chip-20260819-contextmemory-writesel-disposition-evidenced`: "Landing c
keeping the landed implementation and adding refractory as an additional mode via
/implement-substrate has a go from me"). This document is the `/implement-substrate`
Step 3 data-flow plan, which that skill requires be presented before code is written.
There is no live user in a headless session, so it is landed as a tracked, reviewable
artifact alongside the change rather than shown in a conversation. **The user authorised
the build, not silence about it** -- if any design decision below is wrong, it is wrong
in the tree and can be reverted narrowly.

**Chip:** `chip-20260819-contextmemory-add-refractory-mode`
**Session:** `metaworker-chip-20260819-contextmemory-add-refractory-mode` (DLAPTOP, headless)
**Written:** 2026-08-19T14:20:43Z
**substrate_queue id:** `contextmemory-write-path-addressing-degeneracy` (severity `corrupting`)
**Substrate:** `ree-v3/ree_core/predictors/e1_deep.py`, `ree-v3/ree_core/utils/config.py`
**Base:** ree-v3 `4c66e69` (`origin/main`)
**Salvage source:** ree-v3 tag `stash-archive/20260819-dd4b0a4` (LOCAL-ONLY, DLAPTOP; base `f7a6e9c`)

---

## 0. What this is and is not

This ADDS a second, default-off write-address selection mode. It **does not revert,
replace, weaken or re-scale** the landed conscience-bias implementation
(ree-v3 `76cbf844`, `E1Config.contextmemory_write_usage_balancing`). Both remain
available and, by the composition rule in section 3, both can be enabled together.

It also does **not** unblock `chip-20260818-sd017-ceiling-retest-gated` or
`chip-20260818-mech152-redesign-queue-gated`. Adding a default-OFF knob changes no
driver's behaviour, and the two preconditions those chips carry
(`chip-20260819-contextmemory-gated-exps-driver-preconditions`) are unaffected: no
driver enables either flag, and the `occ_cos` DV still cannot discriminate the arms at
the powers those experiments were run at. Both stay gated.

---

## 1. Justification -- STRUCTURAL, not the differentiation DV

**Read this before quoting any number from the salvaged branch's notes.**

The independent probe (`contextmemory_write_selection_comparison_20260819.md`,
pre-registered `REE_assembly` `fcfb311e4b`, results `b7e072ddf0`) established that the
occupied-slot cosine column **cannot discriminate these arms at 5 seeds**: every
contrast is |dz| <= 0.47, |t(4)| <= 1.04, and sign-inconsistent across seeds. That
verdict applies to the salvaged notes' own headline inference as much as to anything
else -- the +0.6060 -> +0.5919 gap used there to recommend `refractory` over legacy is
dz = -0.06, t(4) = -0.13, i.e. indistinguishable from zero. It is **not** cited here as
evidence of superiority, and it must not be cited that way downstream.

The case for `refractory` is the part of the probe that IS robust -- the deterministic
columns, which reproduce exactly across reruns:

1. **The occupancy guarantee is structural, not empirical.** The `k` most-recently-written
   slots are ineligible, so `n_occupied >= k+1` holds **by construction**, for any stream,
   any seed, any initialisation. Nothing else on offer has that property; the landed rule
   reaches full occupancy *empirically*, on the streams measured.

2. **It is the only arm that does not convert the fixed point into a fixed cycle.**
   Probe section 5, degenerate stream, agreement with a strict LRU round-robin:

   | arm | round-robin agreement | entropy (bits) | HHI | distinct slots per seed |
   |---|---|---|---|---|
   | `argmin` (legacy) | 0.000 | 2.00 | 0.473 | [1, 14, 11, 14, 1] |
   | landed `write_usage_balancing` | **0.999** | **4.00** (exactly) | **0.0625** (exactly 1/16) | [16, 16, 16, 16, 16] |
   | `refractory` k=2 | 0.000 | 2.66 | 0.201 | [3, 14, 11, 14, 3] |

   The landed rule's `sqrt(memory_dim)` = 11.31 scaling makes the usage term ~2-3 orders
   of magnitude larger than the across-slot spread of `mean_scores` (~0.026 at this
   operating point), so after the first pass the address is a function of the write
   COUNTER, not of the query: a fixed period-16 cycle on 99.9% of writes. That is a real
   improvement on every occupancy metric and is **not** the noise-filling failure the
   salvaged notes wrongly ascribed to it -- but it is occupancy without addressing.
   `refractory` masks the last k slots and leaves selection among the rest as the
   **unmodified content argmin**, which is why its distinct-slot counts track legacy's
   exactly on the three non-locking seeds ([_, 14, 11, 14, _]).

3. **Biological grounding.** An absolute refractory period on a recently-active unit is a
   first-order property of real neurons. A global usage-EMA conscience bias is not. Under
   the standing brain-like-construction principle this is a point in `refractory`'s
   favour, and it is why the mode is worth having available even though the landed rule
   already clears the registered acceptance floor.

**Neither mechanism is being declared the winner.** The probe's disposition was "keep the
landed implementation; add `refractory` as an additional mode, through
`/implement-substrate` with its own review, not riding on the probe." That is exactly
this change. Choosing between them is the validation experiment's job (section 8), not
this landing's.

---

## 2. Reconciliation: what is taken from the salvage and what is dropped

The salvage is based on `f7a6e9c`, which **predates** `76cbf844`. `76cbf844` is the only
commit touching either file between `f7a6e9c` and `origin/main` (verified). So this is a
two-way reconciliation of two independent edits to one base, not a clean apply.

| salvaged element | disposition | reason |
|---|---|---|
| `write_selection="refractory"` + `write_refractory_k` | **TAKE** | the authorised subject of this build |
| `write_selection="usage"` | **DROP** | a DIFFERENT algorithm from the landed usage penalty (`argmax(-z(sim) - w*z(usage))` vs `argmin(sim + w*usage*sqrt(d))`). Landing it would put two unrelated things called "usage" in one module. Measured content-blind (Jaccard 0.600 vs refractory 0.364). |
| `write_selection="gumbel"` | **DROP** | measured content-blind at Jaccard **1.000** on 5/5 seeds -- both contexts write the same slot set. The probe's most robust negative result. |
| `slot_usage` buffer, `_zscore`, gumbel tau schedule | **DROP** | state that exists only to serve the two dropped modes |
| `contextmemory_write_usage_weight`, `..._gumbel_tau_{init,min}`, `..._gumbel_anneal_steps` | **DROP** | knobs for the dropped modes |
| `contextmemory_write_usage_decay` | **DROP (already present)** | **NAME COLLISION**: the landed commit already defines this field with different semantics (decay of `write_usage_ema` for the conscience bias). Adding the salvaged one would silently re-purpose a live knob. |
| `slot_write_counts`, `last_write_index`, `occupied_slots()` | **TAKE** | see section 4 |

Net new config surface: **exactly two fields.**

---

## 3. Config changes

| Param | Type | Default | Purpose | Class |
|---|---|---|---|---|
| `contextmemory_write_selection` | `str` | `"argmin"` | write-address ELIGIBILITY rule. `"argmin"` = legacy (all slots eligible); `"refractory"` = exclude the last k written. | `E1Config` |
| `contextmemory_write_refractory_k` | `int` | `2` | refractory horizon. Inert unless `write_selection == "refractory"`. k=2 gives the registered floor of 2 with one slot of margin. | `E1Config` |

Both wired at **all three** `from_dims` sites (dataclass field, `from_dims` signature,
`config.e1.<field> = <arg>` assignment) -- `REEConfig.from_dims` silently swallows unknown
kwargs, so a knob wired at only two sites fails open and silently. Pinned by
`test_config_plumbs_through_from_dims`.

An unrecognised `write_selection` raises `ValueError` at construction. Fail-closed is
correct here: a typo'd mode name that silently fell back to `argmin` would reinstate the
corrupting defect under a config that claims to have fixed it.

### Composition with the landed flag -- the one genuinely new design decision

Neither parent branch had to answer this; it exists only because of the reconciliation.

- `contextmemory_write_usage_balancing` adjusts the **score**.
- `contextmemory_write_selection="refractory"` restricts the **eligible set**.

They are orthogonal and compose:

```
selection_scores = mean_scores + (bias if write_usage_balancing else 0)
min_idx          = argmin over { slots NOT in the last-k window } of selection_scores
```

All four combinations are legal. `(argmin, balancing off)` is the legacy default,
bit-identical. This is a deliberate choice over making them mutually exclusive: mutual
exclusion would need a raise or a silent precedence rule, and the composition is
well-defined and measurable, so it becomes an arm the validation experiment can use
rather than a configuration error.

---

## 4. Data flow

```
E1Config.contextmemory_write_selection        (default "argmin")
E1Config.contextmemory_write_refractory_k     (default 2)
        |
        |  REEConfig.from_dims(...)  -- 3 sites: field, signature, assignment
        v
E1DeepPredictor.__init__   getattr(self.config, "contextmemory_write_selection", "argmin")
        |
        v
ContextMemory.__init__(write_selection=..., write_refractory_k=...)
        |
        v
ContextMemory.write(state):
    write_signal  = write_gate(state) [* write_content(state) if gated_content_write]
    with no_grad:
        scores           = query_proj(state) @ memory.T
        mean_scores      = scores.mean(0)
        selection_scores = mean_scores + usage_bias        # UNCHANGED, landed 76cbf844
        min_idx          = _select_write_slot(selection_scores)   # <-- NEW: eligibility mask
        memory[min_idx]  = 0.9*memory[min_idx] + 0.1*write_signal.mean(0)
        write_usage_ema  update                            # UNCHANGED, landed 76cbf844
        _record_write(min_idx)                             # <-- NEW: instrumentation
        |
        v
Instrumentation consumers (drivers, contracts):
    ContextMemory.last_write_index -> int | None
    ContextMemory.slot_write_counts -> Tensor[num_slots]   (persistent=False)
    ContextMemory.occupied_slots()  -> List[int]
```

No `LatentState` field is added. No new module file. No new environment obs channel. The
change is confined to `ContextMemory` plus its config plumbing.

### Why the instrumentation rides along (it is not scope creep)

V3-EXQ-436f's occupancy tracker learned the written slot by **duplicating** `write()`'s
own `scores.mean(0).argmin()` expression. That re-derivation reports the WRONG slot the
moment the selection rule changes -- which is precisely what this change does, twice over
(the landed bias already changed it once). Landing a second selection mode without an
authoritative record of the slot actually written would leave every future driver one
copy-paste away from mis-measuring every arm. `slot_write_counts` and `last_write_index`
are maintained in **every** mode including the legacy default, so a driver reads the same
field regardless of arm. Pinned by `test_stale_reimplementation_of_the_old_rule_disagrees`.

---

## 5. Backward compatibility

With defaults (`write_selection="argmin"`, `write_usage_balancing=False`):

- `_select_write_slot` returns `selection_scores.argmin()` -- the landed expression
  verbatim, same tensor index type.
- **No RNG is consumed.** `refractory` is fully deterministic; nothing sampled, no
  `torch.rand`. So the global RNG stream is unchanged and every existing experiment's
  seeded trajectory is bit-identical. (This is a substantive difference from the dropped
  `gumbel` mode, which would have perturbed it.)
- `state_dict()` is **unchanged**: `slot_write_counts` is `persistent=False`, so existing
  checkpoints load untouched.
- `named_buffers()` DOES gain `slot_write_counts` (one float32[16], always constructed).
  This is checked against the landed negative control
  `test_off_constructs_no_extra_buffer`, which is scoped to names starting
  `write_usage_ema` and is therefore unaffected. Verified rather than assumed.
- Bit-identity is asserted end-to-end (same slot sequence AND same final memory tensor
  over 5 seeds x 200 writes) by `test_default_is_bit_identical_to_the_legacy_expression`.

**No existing config default is changed.**

---

## 6. Contract tests -- and the negative-control substitution

The salvaged contract (`ree-v3/tests/contracts/test_contextmemory_write_address_selection.py`,
currently UNTRACKED in the shared checkout) is landed WITH this change, adjusted to the
reconciled API. It cannot be landed alone: it calls `write_selection` / `write_refractory_k`
/ `occupied_slots` / `last_write_index`, so on today's `main` it is a red contract for the
whole fleet.

Four of its tests reference the dropped `usage`/`gumbel` modes and are removed. Two of
those were, by the file's own design note, the **load-bearing negative controls** -- the
ones that stop a later session promoting a mode on its occupancy number alone. Deleting
them without replacement would remove the file's main defence. They are replaced by an
equivalent control built on the arm that actually exists:

| removed | replacement | why it is at least as strong |
|---|---|---|
| `test_gumbel_is_not_content_conditioned` (Jaccard ~1.000) | `test_landed_usage_balancing_is_a_fixed_cycle_and_refractory_is_not` -- round-robin agreement: landed ~0.999, refractory 0.000 | Deterministic and exactly reproducible; probe section 5. Jaccard was itself shown to be the WRONG instrument (probe section 6: it aliases against a 2-cluster alternation, giving exactly 0.0 on 3/5 seeds and 1.0 on 2/5). The round-robin index is the metric that should have been pre-registered. |
| `test_recommended_mode_beats_noise_modes_on_context_conditioning` | folded into the same test | same |

Retained unchanged in substance: the defect pin (legacy really locks, on seeds 0 and 100),
the sign discriminator, bit-identity of the default, `state_dict` unchanged, the structural
occupancy guarantee at k in {1,2,4}, the never-write-inside-the-window invariant, the
k >= num_slots non-deadlock case, and the instrumentation tests.

**Assertion policy:** every numeric assertion is on a deterministic quantity (occupancy
count, self-repeat, round-robin agreement, slot identity). **No assertion is placed on
`occ_cos`**, per probe section 6. A test that pinned a quantity with |dz| <= 0.47 at n=5
would be a flake generator masquerading as a contract.

---

## 7. Not applicable, stated explicitly

- **Phased training (Step 3e):** N/A. `write()` runs entirely under `torch.no_grad()`.
  No encoder head is added and no gradient path is created or altered.
- **MECH-094 `hypothesis_tag` (Step 3f):** N/A. No simulation, replay, or non-waking-state
  content is written by this change.
- **ML/AI parallels (Step 3g):** the engineering problem is the "dead unit" / codebook
  collapse pathology in competitive learning and VQ codebooks. Two standard families
  address it: a frequency-sensitive **conscience bias** (DeSieno 1988) -- which is what
  the landed implementation already uses -- and **exclusion of recently-used units**,
  the family this mode belongs to (cf. k-recently-used exclusion in cache replacement,
  and codebook reset/exclusion in VQ-VAE training). The REE adaptation differs from the
  ML versions in that there is no gradient and no learned assignment: `write()` is
  `no_grad`, so this is a pure eligibility mask, not a differentiable relaxation. The
  probe's section 5 result is exactly the standard hazard of the conscience-bias family
  when the penalty is scaled far above the content signal -- it degenerates to
  round-robin -- which is the specific failure the exclusion family avoids by leaving the
  content comparison untouched among eligible units.

---

## 8. Validation experiment -- owed, and an earlier gap repaired

`/implement-substrate` Step 8 requires a validation experiment. Per the standing
chip-everything-else rule, `/queue-experiment` work is chipped rather than done inline,
which is what the previous `/implement-substrate` session for this same entry recorded
doing.

**That chip was never actually recorded.** The `substrate_queue` `implementation_note` and
`validation_experiment` fields both name
`chip-20260819-queueexp-contextmemory-writeusage-validation`; it does not exist in
`TASK_CHIPS.json` (0 hits). So the landed usage-balancing implementation has been sitting
at `implemented_pending_validation` with an owed validation experiment that nothing was
tracking. A single chip is recorded by this session covering **both** arms, which repairs
that gap rather than adding a second unowned one.

Two constraints that chip must carry, both from the probe:

1. **Neither flag can be left at its default.** No driver in `ree-v3/experiments/` sets
   either; a driver written today runs the unfixed `argmin` path and walks back into the
   corrupting defect.
2. **Do not power the comparison on `occ_cos`.** Required n at 80% power (paired t,
   two-sided 0.05, from the probe's own per-seed spreads): 38 for usage-vs-legacy, 58 for
   landed-vs-refractory, 149 for landed-vs-legacy, 2485 for refractory-vs-legacy. Use the
   deterministic DVs -- occupancy, self-repeat, entropy, round-robin index.

Until that experiment runs, the `substrate_queue` status stays
`implemented_pending_validation` for both modes. This landing does not change it.

---

## 9. Preservation

`ree-v3` `stash@{0}` and tag `stash-archive/20260819-dd4b0a4` are **retained**. The user
chose option (c), and the discard half of option (b) was never authorised. The tag is the
only copy of the dropped `usage`/`gumbel` implementations and is LOCAL-ONLY to DLAPTOP
(stash-archive tags are not pushed), so dropping it would destroy them irrecoverably.
