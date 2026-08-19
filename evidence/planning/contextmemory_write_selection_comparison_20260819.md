# ContextMemory write-address selection: landed vs salvaged, independent comparison

**Status: COMPLETE. AWAITING USER REVIEW — no substrate change was made and none is
recommended without a separate decision.**

**Chip:** `chip-20260819-contextmemory-writesel-verify-measurement`
**Probe:** `contextmemory_write_selection_probe_20260819.py` (this directory)
**Raw results:** `contextmemory_write_selection_probe_20260819.results.json`
**Post-hoc check:** `contextmemory_write_selection_blindness_check_20260819.py`
**Environment:** ree-v3 `b956d607`, salvaged `dd4b0a4d`, torch 2.12.0, darwin-arm64, DLAPTOP

The pre-registration below (arms, seeds, metrics, decision rules) was committed in
`REE_assembly` `fcfb311e4b` **before the probe was executed**. Results were appended
afterwards. Nothing in the pre-registered section was edited after the run.

---

## Headline

**The assertion does not survive independent measurement.** The salvaged branch's
numbers reproduce essentially exactly — but the claim that the LANDED implementation is
measured-inferior was never actually measured, and the differentiation column the
salvaged notes reason from cannot discriminate between arms at 5 seeds.

| question | answer |
|---|---|
| Did the salvaged measurement reproduce? | **YES** — 8 of 9 published quantities exact to 4 dp |
| Was the landed implementation in that comparison? | **NO** — the salvaged base `f7a6e9c` predates the landed commit `76cbf844` |
| Is the landed rule the same as the salvaged `usage` rule? | **NO** — different algorithms (below) |
| Is the landed rule worse on the pre-registered rules? | **NO** — R1 pass 5/5, R2 not triggered (0.036 vs a 0.25 margin) |
| Is there any real concern about the landed rule? | **YES, but not the one asserted** — it is 99.9% LRU round-robin on the degenerate stream |
| Does the evidence justify reverting or swapping? | **NO** |

---

## 1. The two "usage" rules are different algorithms

This is the load-bearing correction. The salvaged notes' table has a `usage` row and the
landed commit adds a usage penalty, and the two have been treated as the same thing.
They are not:

```
landed   (ree-v3 76cbf844):  argmin( mean_scores + w * usage_ema * sqrt(memory_dim) )
salvaged (ree-v3 dd4b0a4):   argmax( -z(mean_scores) - w * z(usage_ema) )
```

The landed rule adds the usage penalty on the **raw dot-product scale**, multiplied by
`sqrt(memory_dim)` = 11.31, while the natural across-slot spread of `mean_scores` at this
operating point is only ~0.026 (max−min, measured here over 5 seeds x 200 writes; the
salvaged doc quotes ~0.013, consistent if that is a standard deviation rather than a
range). The usage term is therefore ~2-3 orders of magnitude larger than the content
term it is added to, which is the mechanism behind Section 5. The salvaged rule z-scores
**both** terms, so content and usage carry comparable weight by construction. They behave differently, and they do in
fact measure differently (Section 4).

**The salvaged branch could not have measured the landed rule.** Its base `f7a6e9c`
predates `76cbf844`, and `76cbf844` is the *only* commit touching `e1_deep.py` between
`f7a6e9c` and today's `main` — verified. So the salvaged `argmin` row **is** today's
default path (bit-identical, confirmed by control R0), but no row in that table
corresponds to `write_usage_balancing=True`. **This alone explains the assertion**, which
was the specific alternative the chip asked to be checked.

## 2. Method

Both implementations were driven under **one instrumentation**: the written slot is
recovered by **diffing `memory` across each write** (exactly one row is blended), never
by re-deriving the selection expression. This matters twice. It is the failure mode the
salvaged notes themselves warn about (V3-EXQ-436f's tracker duplicated
`scores.mean(0).argmin()` and so reports the wrong slot the moment the rule changes), and
it is the *same* instrument on both arms — `last_write_index` exists only on the salvaged
copy, so using it would have made the arms non-comparable.

Streams reproduced verbatim from the salvaged contract's `_stream()`: latent 64,
memory_dim 128, num_slots 16, `gated_content_write=True`, state rms 0.078, jitter 0.0078.
Seeds `0, 7, 13, 42, 100`. `n_writes` 1500 and 3000 (the salvaged contract uses 1500; its
published table says 3000 — both were run; conclusions are identical).

**Validity controls, both passed.** R0: `argmin_legacy` (main) and `salvaged_argmin`
produced identical slot sequences and identical final memory on every seed — the two
module copies really are the same base. R4: legacy reproduced the documented lock at
exactly 3/5 seeds (locking on 0 and 100), so the operating point has not drifted.

## 3. Reproduction of the salvaged table

| quantity | salvaged notes | this probe | |
|---|---|---|---|
| `argmin` seeds with >= 2 slots | 3/5 | 3/5 | exact |
| `argmin` occupied-slot cosine | +0.6060 | +0.6060 | exact |
| `argmin` cluster Jaccard | 0.329 | 0.329 | exact |
| `refractory` seeds with >= 2 slots | 5/5 | 5/5 | exact |
| `refractory` occupied-slot cosine | +0.5919 | +0.5919 | exact |
| `refractory` cluster Jaccard | 0.364 | 0.364 | exact |
| `usage` cluster Jaccard | 0.600 | 0.600 | exact |
| `gumbel` cluster Jaccard | 1.000 | 1.000 | exact |
| degenerate-stream cosine, gumbel / argmin | +0.9995 / +0.9792 | +0.9995 / +0.9792 | exact |
| `gumbel` occupied-slot cosine | +0.7525 | **+0.7325** | **−0.020** |

**REPRODUCED.** The single discrepancy is the `gumbel` cosine, the only stochastic arm;
its qualitative claim (worse than the legacy path it replaces) holds either way. Given
independent instrumentation, exact agreement on eight quantities is strong evidence the
salvaged probe was executed as described.

## 4. Full comparison (n_writes = 3000, 5 seeds)

Degenerate stream (`clusters=1`) on the left; 2-context stream (`clusters=2`) on the right.
Lower Jaccard = more context-conditioned. Lower `occ_cos` = more differentiated.

| arm | >=2 slots | distinct slots per seed | entropy (bits) | self-repeat | HHI | Jaccard | `occ_cos` |
|---|---|---|---|---|---|---|---|
| `argmin_legacy` | 3/5 | [1, 14, 11, 14, 1] | 2.00 | 0.912 | 0.473 | **0.329** | 0.6060 |
| `landed_usage_balancing` | **5/5** | [16, 16, 16, 16, 16] | **4.00** | 0.000 | **0.0625** | 0.400 | 0.6867 |
| `salvaged_refractory_k2` | **5/5** | [3, 14, 11, 14, 3] | 2.66 | 0.000 | 0.201 | 0.364 | **0.5919** |
| `salvaged_usage` | 5/5 | [15, 15, 15, 15, 14] | 3.89 | 0.000 | 0.068 | 0.600 | 0.7348 |
| `salvaged_gumbel` | 5/5 | [16, 16, 16, 16, 16] | 3.99 | 0.045 | 0.0625 | 1.000 | 0.7325 |

### Pre-registered verdicts

- **R1 — does the landed fix work? PASS.** `landed_usage_balancing` reaches 16 of 16
  slots on **5/5** seeds, against a required 4/5 and a registered acceptance floor of
  >= 2 slots on >= 3/5. Self-repeat falls 0.912 -> 0.000. The landed fix does fix the
  registered defect, on the registered criterion, decisively.
- **R2 — is the landed fix content-blind? NOT TRIGGERED.**
  `mean_jaccard(landed) − mean_jaccard(refractory)` = **+0.036**, against a
  pre-registered materiality margin of 0.25 (the salvaged contract's own margin). By
  contrast the salvaged `usage` and `gumbel` modes sit at +0.236 and +0.636 on the same
  contrast — i.e. **the two modes the salvaged notes call content-blind are, and the
  landed one is not.**
- **R3 — differentiation DV, descriptive.** `occ_cos`: refractory 0.5919 < legacy 0.6060
  < landed 0.6867 < gumbel 0.7325 < salvaged usage 0.7348. Landed is +0.095 worse than
  refractory and +0.081 worse than legacy. **But see Section 6 — this column does not
  discriminate at n=5.**

**By the pre-registered decision rules, reconciliation is NOT justified.**

## 5. The real concern, which is a different one (post-hoc, not pre-registered)

The landed arm's entropy is *exactly* 4.00 bits and its HHI *exactly* 1/16 — a perfectly
uniform write distribution, which is not what a content-driven selector produces. A
follow-up check (`..._blindness_check_20260819.py`) confirms the mechanism:

| arm | agreement with a strict LRU round-robin | slot sequence, seed 0, first 20 writes |
|---|---|---|
| `argmin_legacy` | 0.000 | `15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15` |
| `landed_usage_balancing` | **0.999** | `15 6 10 9 14 1 5 11 8 0 4 13 12 7 3 2 | 15 6 10 9` |
| `salvaged_refractory_k2` | 0.000 | `15 6 10 | 15 6 10 | 15 6 10 | 15 6 10 | 15 6 10 | 15 6` |
| `salvaged_usage` | 0.000 | `15 6 10 9 14 1 5 11 8 0 4 6 15 10 9 14 5 1 13 11` |
| `salvaged_gumbel` | 0.083 | `3 8 1 6 10 14 12 4 5 11 13 15 9 5 9 7 0 9 10 1` |

On the degenerate stream the landed rule is a **fixed period-16 cycle, 99.9% of writes**:
the `sqrt(memory_dim)` scaling makes the usage term dominate content, so after the first
pass the address is a function of the write counter, not of the query. The *ordering* of
that cycle is content-determined once (agreement across different content streams is only
0.113, so it is not globally content-blind), then frozen.

So the landed rule converts a **1-slot fixed point** into a **16-slot fixed cycle**. That
is a genuine improvement on every occupancy metric and is not the noise-filling failure
the salvaged notes describe — but "16 slots visited in a fixed order regardless of query"
is occupancy without addressing, and it is worth naming plainly rather than reading 5/5
off the table. `refractory` is the only arm that does not do this: it breaks the fixed
point structurally (>= k+1 slots by construction) and leaves selection among the
remaining slots as the unmodified content argmin, which is why its distinct-slot counts
track legacy's exactly on the three non-locking seeds ([_, 14, 11, 14, _]).

## 6. The differentiation column does not discriminate at 5 seeds

Paired across the same 5 seeds, `occ_cos` differences (lower = better):

| contrast | mean Δ | sd | dz | t(4) | per-seed |
|---|---|---|---|---|---|
| landed − refractory | +0.095 | 0.253 | +0.38 | +0.84 | [+.15, +.33, **−.33**, +.21, +.12] |
| landed − legacy | +0.081 | 0.350 | +0.23 | +0.52 | [+.53, +.19, **−.36**, +.21, **−.17**] |
| refractory − legacy | −0.014 | 0.249 | −0.06 | −0.13 | [+.38, −.14, −.03, +.00, −.29] |
| usage − legacy | +0.129 | 0.276 | +0.47 | +1.04 | [+.53, +.20, −.08, +.17, −.17] |
| gumbel − legacy | +0.127 | 0.287 | +0.44 | +0.99 | [+.53, +.20, −.13, +.21, −.17] |

Every contrast is small (|dz| <= 0.47), non-significant (|t(4)| <= 1.04), and
**sign-inconsistent across seeds**. This applies to the salvaged notes' own headline
inference as much as to the landed arm: the +0.6060 -> +0.5919 gap used to recommend
`refractory` over legacy is dz = −0.06, t(4) = −0.13 — indistinguishable from zero.

**What IS robust** is everything deterministic: occupancy counts (identical across
reruns), self-repeat rate, entropy, the round-robin index, and gumbel's Jaccard of
exactly 1.000 on 5/5 seeds. The recommendation for `refractory` is well-founded on its
*structural* guarantee; it is not founded on the cosine column, and that column should
stop being quoted to four decimals as though it were.

**This is also a limitation of my own pre-registration**, stated rather than buried: R2
used Jaccard, which failed to flag the landed rule's round-robin behaviour because a
period-16 cycle aliases against a 2-cluster alternation — giving Jaccard exactly 0.0 on
3/5 seeds and exactly 1.0 on the other 2, a bimodal artifact whose mean (0.400) looks
moderate. The round-robin index in Section 5 is the metric that should have been
pre-registered.

## 7. Disposition

**Recommended: keep the landed implementation. Do not revert it, and do not swap it for
the salvaged branch on the strength of the salvaged notes.** The inferiority claim rests
on a row that is a different algorithm and on a column that cannot resolve the arms.

**Also recommended, as separate work rather than as a consequence of this probe:** add
`refractory` as an *additional* mode alongside the landed flag. Its case is independent
of the noisy DV — the occupancy guarantee is structural, and it is the only arm that does
not degenerate into a content-independent cycle. This is closest to option (c) "land only
refractory", except that nothing needs removing: the two are not mutually exclusive. It
should go through `/implement-substrate` with its own review, not ride on this probe.

The salvaged contract file
(`ree-v3/tests/contracts/test_contextmemory_write_address_selection.py`, untracked) and
the salvaged architecture doc
(`REE_assembly/docs/architecture/contextmemory_write_address_selection.md`, untracked)
were both left untouched, as were ree-v3 `stash@{0}` and tag
`stash-archive/20260819-dd4b0a4`. Both dispositions remain open.

### Actionable for the two gated experiment chips

`chip-20260818-sd017-ceiling-retest-gated` and `chip-20260818-mech152-redesign-queue-gated`
were held behind this probe. Two findings bear on them directly, and the second is the
more important:

1. **Both flags default to `False`.** `contextmemory_write_usage_balancing` is referenced
   by nothing outside its own contract, `config.py` and `e1_deep.py` — no driver enables
   it. A driver written today runs the **unfixed** `argmin` path and walks straight back
   into the corrupting defect. Whichever mode is chosen, it must be set explicitly.
2. **`occ_cos` at 5 seeds cannot discriminate these arms** (Section 6). An experiment
   powered as 436e/436f were, using this DV, will produce another well-formed
   uninterpretable result — the same trap in a new guise, arrived at from the other
   direction. Either raise n substantially, or select a DV with a deterministic signal
   (occupancy, self-repeat, round-robin index), before queuing either.

## 8. Reproducing this

```bash
/opt/local/bin/python3 \
  REE_assembly/evidence/planning/contextmemory_write_selection_probe_20260819.py
```

~99 s on DLAPTOP. Requires the salvaged object `dd4b0a4` to be reachable in the ree-v3
checkout. **That object is LOCAL-ONLY** — it is a stash archive tag, and stash archive
tags are not pushed, so this probe is reproducible on DLAPTOP and nowhere else until the
salvaged branch is landed or pushed somewhere. The raw results JSON is committed
alongside so the numbers survive the object.

---

# PRE-REGISTRATION (committed `fcfb311e4b`, before the run)

## Arms (all on today's `main` base)

| arm | implementation | selection rule |
|---|---|---|
| `argmin_legacy` | main | `mean_scores.argmin()` |
| `landed_usage_balancing` | main `76cbf844` | `argmin(mean_scores + w * usage_ema * sqrt(memory_dim))` |
| `salvaged_argmin` | stash `dd4b0a4` | identical to legacy (base-identity control) |
| `salvaged_refractory_k2` | stash `dd4b0a4` | content argmin over slots outside the last-k window |
| `salvaged_usage` | stash `dd4b0a4` | `argmax(-z(mean_scores) - w * z(usage_ema))` |
| `salvaged_gumbel` | stash `dd4b0a4` | annealed Gumbel over that availability score |

Seeds `0, 7, 13, 42, 100`; `n_writes` 1500 and 3000; latent 64, memory_dim 128,
num_slots 16, `gated_content_write=True`; stream reproduced verbatim from the salvaged
contract's `_stream()` (state rms 0.078, jitter 0.0078).

## Pre-registered metrics

Degenerate stream (clusters=1): `n_distinct`, `entropy_bits`, `self_repeat` (collision
rate), `herfindahl`. 2-context stream (clusters=2): `jaccard` (lower = more
context-conditioned), `occ_cos` (mean pairwise cosine among occupied slots, lower = more
differentiated).

## Pre-registered decision rules

- **R4** validity gate: `argmin_legacy` must reproduce the documented lock at exactly 3/5
  seeds. Otherwise the operating point has drifted and all rows void.
- **R0** base-identity: `argmin_legacy` and `salvaged_argmin` must give an identical slot
  sequence and final memory. Otherwise the two copies are not the same base and the
  comparison is void.
- **R1** does the landed fix work: `landed_usage_balancing` must reach >= 2 occupied
  slots on >= 4/5 seeds. FAIL => reconciliation justified.
- **R2** is the landed fix content-blind: `mean_jaccard(landed) −
  mean_jaccard(refractory) > 0.25` => reconciliation justified. The 0.25 margin is the
  salvaged contract's own pre-existing materiality margin, not one chosen here.
- **R3** secondary, descriptive, no threshold: `occ_cos` across arms with Cohen's d over
  the 5 seeds.

Disposition mapping: R1 pass AND R2 not triggered => landed implementation adequate.
R1 fail OR R2 triggered => reconciliation justified.
