# ContextMemory write-address selection: landed vs salvaged, independent comparison

**Status: PRE-REGISTRATION COMMITTED, RESULTS NOT YET RUN.**
**Chip:** `chip-20260819-contextmemory-writesel-verify-measurement`
**Probe:** `REE_assembly/evidence/planning/contextmemory_write_selection_probe_20260819.py`

This section is committed BEFORE the probe is executed. Metrics, arms, seeds
and decision rules below are fixed at this commit; the results section is
appended in a later commit on the same branch.

## Question

Is the LANDED usage-penalty write-selection (ree-v3 `76cbf844`,
`E1Config.contextmemory_write_usage_balancing`) actually WORSE on write-address
degeneracy / content-conditioning than the SALVAGED four-mode implementation
(ree-v3 stash `dd4b0a4`, tag `stash-archive/20260819-dd4b0a4`), as the salvaged
branch's own notes assert?

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
num_slots 16, `gated_content_write=True`; stream reproduced verbatim from the
salvaged contract's `_stream()` (state rms 0.078, jitter 0.0078).

## Pre-registered metrics

Degenerate stream (clusters=1): `n_distinct`, `entropy_bits`, `self_repeat`
(collision rate), `herfindahl`. 2-context stream (clusters=2): `jaccard`
(lower = more context-conditioned), `occ_cos` (mean pairwise cosine among
occupied slots, lower = more differentiated).

## Pre-registered decision rules

- **R4** validity gate: `argmin_legacy` must reproduce the documented lock at
  exactly 3/5 seeds. Otherwise the operating point has drifted and all rows void.
- **R0** base-identity: `argmin_legacy` and `salvaged_argmin` must give an
  identical slot sequence and final memory. Otherwise the two copies are not
  the same base and the comparison is void.
- **R1** does the landed fix work: `landed_usage_balancing` must reach >= 2
  occupied slots on >= 4/5 seeds. FAIL => reconciliation justified.
- **R2** is the landed fix content-blind: `mean_jaccard(landed) -
  mean_jaccard(refractory) > 0.25` => reconciliation justified. The 0.25 margin
  is the salvaged contract's own pre-existing materiality margin, not one
  chosen here.
- **R3** secondary, descriptive, no threshold: `occ_cos` across arms with
  Cohen's d over the 5 seeds.

Disposition mapping: R1 pass AND R2 not triggered => landed implementation
adequate. R1 fail OR R2 triggered => reconciliation justified.

## Full instrumentation and rationale

See the probe script's module docstring. In particular, the written slot is
recovered by DIFFING `memory` across the write rather than by re-deriving the
selection expression -- the same instrument on both implementations, which is
what makes the arms comparable at all (`last_write_index` exists only on the
salvaged copy).
