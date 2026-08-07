# Methodology check — V3-EXQ-436d `slot_cosine_sim` (C1 primary DV)

**Status:** `awaiting_human_confirmation` (headless / staging mode)
**Generated:** 2026-08-07T20:32:48Z
**Session:** `metaworker-chip-20260807-436d-slotcosinesim-methodology-check`
**Machine-readable companion:** `failure_autopsy_V3-EXQ-436d-methodology-check_2026-08-07.json`

**Target:** `v3_exq_436d_sd017_mech166_writepath_retest_20260804T071541Z_v3` (V3-EXQ-436d), claims SD-017 / ARC-045 / MECH-166.
**Held by:** the 2026-08-07 `/governance` cycle, pending exactly this check (`failure_autopsy_2026-08-05_pending_review_batch.json` target #5).

---

## Verdict

**The C1 FAIL is not an interpretable null. The metric is confounded, and the confound is fatal to the criterion as registered.** Confidence: **high**.

The held caveat resolves *against* the metric. The concern that prompted the hold — a WAKING_ONLY baseline ranging 0.0009–0.47 instead of clustering near 1.0, plus one seed showing sleep *increasing* similarity — is not noise. Both are surface manifestations of a single measurement defect.

**What survives intact:** P0 clearance. `sws_n_writes_total = 160` per sleep seed is real, and V3-EXQ-436d genuinely is the first run of the 436a→d lineage with a working write path and no known instrumentation defect. Governance recorded that correctly and this check does not disturb it.

**What does not survive:** C1's status as evidence. Recommended `evidence_direction: weakens → non_contributory`, `epistemic_category: measurement_test_design_defect`. **This session did not apply that** — it is a disposition change, and therefore governance's call. It is also physically blocked: `claims.yaml` is under an active foreign claim (see *Contention* below).

---

## The single sentence version

`slot_cosine_sim` averages pairwise cosine over **all 16 memory slots including never-written ones**, and the WAKING_ONLY arm it is compared against **performs zero ContextMemory writes** — so C1 compares a bank holding 160 content vectors against a bank holding no context at all, on a statistic whose baseline value is set by optimiser drift.

---

## Findings

### F1 — The WAKING_ONLY arm performs ZERO ContextMemory writes *(fatal)*

`ContextMemory.write()` has exactly three reachable call sites, and 436d's config closes all three for the waking arm:

| Site | Gate | 436d value |
|---|---|---|
| `agent.py:4605` (in `sense()`) | `sd016_writepath_mode ∈ {sense_only, both}` | `"off"` |
| `e1_deep.py:552` (`update_from_observation`, reached from `agent.py:9426`) | `sd016_writepath_mode ∈ {train_only, both}` | `"off"` |
| `agent.py:10780` (`run_sws_schema_pass`) | sleep-only | WAKING_ONLY has `sleep_passes = 0` |

The manifest corroborates independently: `sleep_cycle_sws_n_writes_total = 0.0` for all five WAKING_ONLY arms, `160.0` for all five SWS_THEN_REM arms.

So C1 is not *"sleep-differentiated context vs waking-undifferentiated context"*. It is *"a bank with 160 content writes vs a bank with none"*. The two arms have no shared referent.

### F2 — The metric includes unwritten slots, so an untouched bank reads ~0, not ~1.0 *(fatal)*

`_compute_slot_cosine_sim` (driver:435) masks only the diagonal — no occupancy mask. Slots initialise as `nn.Parameter(torch.randn(16,128) * 0.01)` (`e1_deep.py:47`), i.e. mutually near-orthogonal.

Measured null over **2000 random inits**: mean `+0.000145`, sd `0.008121`, range `[-0.0229, +0.0294]`, **P(metric > 0.20) = 0.0000**.

ARC-045's prediction that an undifferentiated bank reads near 1.0 requires *all 16 slots to hold near-identical content*. That state was reachable only under the legacy `write_gate`-as-payload defect (every write blended the slot toward `0.5*ones(128)`; 436c measured 0.9999–1.0 in 4/5 seeds) — **the very defect V3-EXQ-436d repaired** via `contextmemory_gated_content_write=true`.

> The near-1.0 baseline C1 was calibrated against was an artifact of the broken substrate. C1 was inherited from a substrate that no longer exists.

### F3 — The metric is a *product* of similarity and occupancy *(fatal)*

With `k` slots written at mutual cosine `c` and the rest at init, the whole-bank statistic tracks `c·k(k−1)/(n(n−1))`:

| c | k=8 | k=12 | k=16 |
|---|---|---|---|
| 0.90 | 0.2487 *(pred 0.2100)* | 0.5199 *(0.4950)* | 0.9017 *(0.9000)* |
| 0.50 | 0.1475 *(0.1167)* | 0.3003 *(0.2750)* | 0.5049 *(0.5000)* |

**Control:** with written content held mutually *orthogonal*, the metric stays at ~0 (|value| ≤ 0.013) for every k from 0 to 16 — confirming occupancy alone does not move it; only occupancy × similarity does.

### F4 — C1 *penalises* sleep for recruiting slots — the exact predicted behaviour *(direction-reversing)*

Manifest `slot_visit_safe_count` shows WAKING_ONLY activating **exactly one slot in all five seeds** (seed 7→slot 1, 13→8, 42→8, 100→7, 200→14); SWS_THEN_REM activates 2–6.

Simulated on the real metric:

| arm | occupied-only cosine (true differentiation) | whole-bank metric (C1's DV) | C1 says |
|---|---|---|---|
| WAKING_ONLY, k=1 | — | **+0.0092** | — |
| SWS_THEN_REM, k=4 | +0.321 | +0.0305 | FAIL |
| SWS_THEN_REM, k=6 | +0.207 | +0.0432 | FAIL |
| SWS_THEN_REM, k=8 | +0.173 | +0.0542 | FAIL |
| SWS_THEN_REM, k=12 | **+0.113** *(near-orthogonal — excellent)* | **+0.0763** | **FAIL** |

An arm spreading context across 12 slots at near-orthogonal separation scores **8× worse** than one using a single slot. The criterion is anti-correlated with the mechanism it was written to detect.

### F5 — The baseline is set by an uncontrolled nuisance term: Adam drift *(fatal)*

`context_memory.memory` is an `nn.Parameter`, and the driver's optimiser is `standard_params = [p for n,p in agent.named_parameters() if 'harm_eval_head' not in n]` at `lr=1e-3` (driver:697–700) — **which includes it**. Gradient reaches it through `read()`'s shared softmax attention.

Reproduced on the real `ContextMemory(gated_content_write=True)`, Adam lr=1e-3, **zero `write()` calls**, at the five experiment seeds:

| seed | init | @200 | @1000 | @5000 | @30000 |
|---|---|---|---|---|---|
| 42 | −0.0015 | 0.3074 | 0.3039 | 0.1337 | 0.1118 |
| 7 | −0.0018 | 0.3631 | 0.2480 | 0.0531 | 0.0650 |
| 13 | −0.0100 | 0.2459 | 0.3119 | 0.0916 | 0.0701 |
| 100 | −0.0073 | 0.2575 | 0.1854 | 0.1067 | 0.1954 |
| 200 | +0.0153 | 0.2827 | 0.3696 | 0.1335 | 0.1141 |

This reproduces **the entire observed WAKING_ONLY range (0.000878–0.470201) with no context writes at all**, and it is non-monotone in training time — so the baseline's value at readout is an arbitrary function of seed and of where training stopped.

> **This is the direct answer to the question that triggered the hold.** The 0.0009–0.47 spread is optimiser drift, not context content.

### F6 — C1 is unsatisfiable on 2 of 5 seeds, so the "2/5 vs 3/5" arithmetic is not a null *(invalidates denominator)*

| seed | WAKING_ONLY | z vs untouched-bank null | SWS_THEN_REM | C1 |
|---|---|---|---|---|
| 7 | 0.470201 | 57.9 | 0.156510 | PASS |
| 42 | 0.390728 | 48.1 | 0.432449 | FAIL |
| 100 | 0.208183 | 25.6 | 0.107311 | PASS |
| 13 | 0.009946 | **+1.21** | 0.085408 | FAIL *(unsatisfiable)* |
| 200 | 0.000878 | **+0.09** | 0.487948 | FAIL *(unsatisfiable)* |

Seeds 13 and 200 sit **inside** the untouched-bank null. For those seeds C1 asks whether sleep can push the statistic below the metric's own zero-point *while writing 160 content vectors into the bank* — which by F3 can only raise it. **C1 cannot pass there regardless of what sleep does.**

Effective denominator ≤ 3, of which 2 passed — against a threshold registered as 3/5.

This also disposes of the "reversed direction" concern: seed 200's `0.000878 → 0.487948` is not sleep making things worse. It is the sleep arm writing content into a bank that started at exactly zero.

### F7 — Two secondary reporting defects *(no differential effect)*

**(a)** The manifest advertises `sd016_diversification_weight: 0.5`, but the loss is gated on `_div_w > 0.0 AND self.e1.config.sd016_enabled` (`agent.py:9437–9439`). `sd016_enabled` defaults `False` (`config.py:384`) and the 436d driver never sets it — **the advertised orthogonality pressure was inactive for the whole run.** Do not cite that config field as a substrate condition.

**(b)** `sleep_cycle_sws_slot_diversity_last` is **not** an independent readout. `run_sws_schema_pass` computes `mean(1 − off_diag_cosine)` over the same bank with the same mask, so it is exactly `1 − slot_cosine_sim`. Verified to 6 dp on all five sleep arms (seed 42: `1 − 0.5676 = 0.4324 = 0.432449`). These two fields must not be read as mutually corroborating — they are one number reported twice.

---

## What this check did *not* establish

- **Whether the SD-017/ARC-045/MECH-166 slot-differentiation prediction is true.** This invalidates the instrument, not the hypothesis.
- **What a corrected DV would have reported for 436d.** No per-slot memory snapshot is persisted, so the occupied-only statistic is not recomputable from the manifest. That is why the finding is *"the metric is confounded"* and not *"the corrected metric would have said X"*.
- **Whether C2–C4 are affected.** Only C1's DV was examined; P0 was spot-checked and is sound.

Also worth recording: the manifest carries **no write-target occupancy**. `slot_visit_*_count` are read-side *argmax* counts, whereas `write()` selects by *argmin* of `query·memory` — a different index. Occupancy figures above are indicative, not exact.

---

## Recommendation to `/governance` (proposed — not applied)

1. **`evidence_direction`: `weakens` → `non_contributory`**; `epistemic_category`: `measurement_test_design_defect`. Apply consistently across SD-017, ARC-045 and MECH-166 — all three reference the same held result.
2. **Release the hold, but not into demotion weighting.** The FAIL should stop weighting these claims rather than start doing so.
3. **Re-scope the retest gate** from `pending_retest_after_substrate` to *pending DV repair*. The substrate is not the blocker — the write path already works. The instrument is.
4. **Queue V3-EXQ-436e.** Required changes (full list in the JSON):
   - statistic over **occupied slots only**, tracking `write()`'s `min_idx` directly;
   - pre-register on similarity `c`, reporting occupancy `k` separately — never on the `c·k(k−1)/(n(n−1))` product;
   - give WAKING_ONLY a real write path (e.g. `sd016_writepath_mode='sense_only'`) so it is a control rather than an empty bank, and equalise or report per-arm write counts;
   - neutralise Adam drift (exclude `memory` from the optimiser for this measurement, or report it as a covariate, or snapshot at a fixed step);
   - **re-derive the predicted baseline against the repaired write path** — do not reuse ARC-045's near-1.0 figure;
   - add a writes-disabled negative control, which should be indistinguishable from the untouched-bank null (~0.0001 ± 0.008).

### Fan-out worth governance's attention

The defective statistic is **not local to this driver**:

- `run_sws_schema_pass`'s `sws_slot_diversity` is the same whole-bank formula (F7b) and is emitted by *every* driver that calls a sleep pass — any criterion elsewhere pre-registered on it inherits the same occupancy confound.
- The same `_compute_slot_cosine_sim` shape appears in `v3_exq_242`, `v3_exq_243`, `v3_exq_245/245a/245b`, `v3_exq_246` and the earlier 436-family drivers. A grep-level sweep for other criteria pre-registered on a whole-bank cosine is warranted.

---

## Contention

`task_claim.py open --resources REE_assembly/docs/claims/claims.yaml` returned **exit 3**:

- **OWNER:** `metaworker-chip-20260807-sd014-decouple-wanting-liking` (2026-08-07T20:02:46Z)
- plus a governance-pause hold by `cool-torvalds-a82359` (2026-08-07T20:16:26Z)

This session is **not** the owner, so it did not edit `claims.yaml` and routed its finding here instead — the alternative output path the chip prompt explicitly sanctions. The recommended `evidence_quality_note` text for all three claims is in the JSON under `recommended_evidence_quality_note`, ready to paste.

The coordination-plane autopsy-pause claim was also **not** opened: a governance pause is already in force, and this check is read-only apart from writing this artifact pair — it queues and runs nothing on the plane.

---

## Reproduction

Code sites and probe definitions are listed in the JSON under `provenance`. All four probes run against the real substrate (`ree_core.predictors.e1_deep.ContextMemory`), not a reimplementation:

1. untouched-bank null (2000 random inits);
2. occupancy sweep at orthogonal content (control) and at fixed `c ∈ {0.90, 0.50}`;
3. direction-reversal demonstration (k=1 vs k ∈ {4,6,8,12});
4. Adam-drift reproduction — real `ContextMemory`, zero `write()` calls, 30 000 steps, five experiment seeds.
