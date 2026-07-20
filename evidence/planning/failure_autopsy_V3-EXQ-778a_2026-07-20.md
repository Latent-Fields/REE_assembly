# Failure autopsy — V3-EXQ-778a (intra-run substrate divergence, defect class D3)

**Generated** 2026-07-20T06:43:37Z · **Session** `funny-kilby-e4dd87`
**Target** `v3_exq_sd068_consolidation_staging_power_diagnostic_20260717T163507Z_v3` · `V3-EXQ-778a`
**Outcome** PASS · `evidence_direction: supports` · `ree-worker-1` · 2026-07-17 · 418s · 8 seeds
**Referred by** [`intra_run_substrate_divergence_sweep_2026-07-20.md`](intra_run_substrate_divergence_sweep_2026-07-20.md) sec 5c
(REE_assembly `3427fe852a`), which classed it **SEVERE**
**D3 origin** [`failure_autopsy_V3-EXQ-689d_2026-07-20.md`](failure_autopsy_V3-EXQ-689d_2026-07-20.md) sec 4,
`targets[0].defects[2]`

> **One line.** The mid-run substrate change is **real on disk but never reached execution** — the one
> changed file was import-bound before the seed loop, so all 8 seeds ran identical bytecode. And even
> setting that aside, the observed variability **does not partition** along the substrate boundary: the
> six-seed homogeneous partition alone reproduces the entire reported spread. D3 is **REFUTED** for this
> run; `supports` on SD-068 **stands**. The load-bearing output is a *different* defect the investigation
> exposed — the fingerprint stamped 6 cells with code they never executed, a **false-HIT channel** in
> arm-reuse.

---

## 1. Facts

Per-cell `arm_fingerprint.substrate_hash` splits the seed pool:

| substrate | seeds | n cells |
|---|---|---|
| `e9a22a91` | 42, 7 | 2 |
| `c8d6d0e2` | 123, 2024, 99, 7777, 314, 1000 | 6 |

Constant within the run: `substrate_n_files` = 129 (no files added/removed), `machine_class`
`linux-x86_64-py3.10`, `driver_script_hash` `edc944ae`, `driver_script_in_substrate_hash` `true`,
`scope`/`globs` unset, `reuse_eligible` true on all 8. Top-level hoisted `substrate_hash` = `e9a22a91`.

The split is a **contiguous prefix** (arms 1-2, then 3-8) — one monotone transition, each seed present
exactly once, one coherent 418s window. That is the signature of a single process whose *disk* moved
underneath it, not of a restart (a restart would have re-run seed 42 on the new substrate).

### The finding at stake

`interpretation.label: staging_seed_variable_underpowered`. Load-bearing criterion
`C1_monotone_degradation_all_phases` PASSed on 8/8. The staging verdict is **reported, never gated**:
`modal_observed_order` = `(rem, nrem, sws)` = the predicted reverse-dependency order,
`modal_order_seed_count: 4`, `n_seeds_matching_prediction: 4` of 8, mean Spearman rho 0.375
(95% CI -0.247 to 0.997), sign test p = 0.727.

The sweep's severity call rests on the third limb of its sec-4 test: *the finding is itself a statement
about between-seed variance while the seed pool is substrate-heterogeneous.* That reasoning is correct
in form — this autopsy tests whether it holds in fact.

### Correction to the referral's scope

The referral describes "a live directional verdict across four claims." The manifest's
`evidence_direction_per_claim` is:

| claim | direction |
|---|---|
| SD-068 | **supports** |
| MECH-168 | unknown |
| MECH-169 | unknown |
| INV-047 | unknown |

Only **SD-068** carries a directional verdict. MECH-168/169 and INV-047 are tagged but explicitly
`unknown` — consistent with the manifest note ("MECH-121 NOT tagged for promotion; glymphatic half of
MECH-169 out of scope"). Directional exposure is **one claim, not four**.

---

## 2. The divergence did not reach execution

### 2a. Both hashes reconstructed exactly from git

Detached worktrees at each candidate commit, hashed with that commit's own
`experiments/_lib/arm_fingerprint.compute_substrate_hash`, driver folded in (matching
`driver_script_in_substrate_hash: true`):

| reconstruction | substrate_hash | n_files | matches |
|---|---|---|---|
| ree-v3 @ `6614a2e` | `e9a22a91` | 129 | seeds 42, 7 |
| ree-v3 @ `da873a1` | `c8d6d0e2` | 129 | seeds 123, 2024, 99, 7777, 314, 1000 |

Byte-exact on both. The run-time driver blob `edc944ae` is the version committed in `6614a2e`
(`queue: V3-EXQ-778a SD-068 staged-damage power-up`, 2026-07-17T16:25:48Z) — 2.4 minutes before the
run started. `6614a2e` is an ancestor of `da873a1`.

### 2b. The delta is one file, and it is import-bound

`da873a1` (2026-07-17T16:29:34Z, *"SD-068: replace REM terrain-variance proxy with rollout-seed
generative-fidelity readout"*) changed **exactly one file**:

```
 experiments/_lib/consolidation_lesion_harness.py | 254 +++++++++++++++++++++--
 1 file changed, 232 insertions(+), 22 deletions(-)
```

It landed ~85s into a 418s run (~52s/seed), i.e. between seed 7 and seed 123 — exactly the observed
boundary. Superficially this is the worst case: the edit rewrites the **REM readout**, the very quantity
whose spread carries the finding.

But the driver binds that module at **module scope, before the seed loop**:

```python
# ree-v3/experiments/v3_exq_sd068_consolidation_staging_power_diagnostic.py:72
from experiments._lib import consolidation_lesion_harness as H
```

CPython caches modules in `sys.modules` at first import; the seed loop calls `H.run_staged_sweep(...)`
against the object bound at process start. Verified on the exact run-time source (`6614a2e`):

- no `importlib`, `reload(`, or `__import__` anywhere in the driver or the harness;
- the harness's only deferred import (`ree_core.sleep.cross_module_consolidation`, harness line 560)
  is (a) in `ree_core`, which `da873a1` did not touch, and (b) `sys.modules`-cached after seed 42;
- no runtime file reads in the harness.

**Therefore all 8 seeds executed the `6614a2e` (`e9a22a91`) harness.** The disk changed; the executing
bytecode did not. The hoisted top-level `substrate_hash` (`e9a22a91`, taken from arm 0) is in fact the
**correct** identity for all 8 cells.

Residual uncertainty, stated honestly: this argument establishes that the *changed file* could not
reach execution. It does not exclude an unrecorded non-`.py` runtime input — but `substrate_n_files`
is constant at 129, the globs are `*.py` only, and the harness performs no file reads.

---

## 3. The variability does not partition along the boundary

This is the referral's key question, and it is answered independently of section 2 — i.e. it would hold
even if the code change *had* reached execution.

| | A `e9a22a91` (n=2) | B `c8d6d0e2` (n=6) | pooled (n=8) |
|---|---|---|---|
| seeds | 42, 7 | 123, 2024, 99, 7777, 314, 1000 | — |
| matches predicted order | 1/2 = **50%** | 3/6 = **50%** | 4/8 = 50% |
| distinct observed orders | 2 | **3** | 3 |
| per-seed Spearman rho | 1.0, -0.5 | 0.5, 1.0, 1.0, 1.0, -0.5, -0.5 | — |
| REM tolerance range | [0.846, 1.350] | **[0.433, 1.500]** | [0.433, 1.500] |
| REM tolerance sd | 0.357 | **0.435** | 0.396 |
| NREM tolerance sd | 0.0023 | 0.0013 | 0.0014 |
| SWS tolerance sd | 0.0 | 0.0 | ~8.6e-09 |

Four things follow, none of which favour a partition reading:

1. **The match rate is identical** — 50% in each partition, and equal to the pooled rate. The
   `n_seeds_matching_prediction: 4 / 8` headline is not produced by the split.
2. **A's range lies entirely inside B's.** B contributes both the minimum (0.433, seed 99) and the
   maximum (1.500, seed 1000) of the whole run.
3. **B's REM sd (0.435) exceeds the pooled sd (0.396)** and A's (0.357). The homogeneous six-seed
   partition alone reproduces — indeed slightly *exceeds* — the full reported spread.
4. **Both observed orders present in A are also present in B**, and B carries a third
   (`nrem, rem, sws`) that A does not. A's two seeds are one exact match plus one inversion: the pooled
   pattern in miniature, not a distinct group.

NREM and SWS are near-degenerate in variance in **both** partitions (sd ~1e-03 and ~0 respectively), so
no phase shows a partition-aligned shift.

**Reading.** The `staging_seed_variable_underpowered` finding is **strengthened**, not undermined. Six
seeds on a single substrate produce three distinct staging orders and the entire REM tolerance range.
Seed-to-seed variability is genuinely seed variability. Per the referral's own framing — *"If they
don't, the finding is more robust than the split suggests"* — that is the outcome.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | SD-068 tested under conditions where it could express itself; C1 PASS 8/8; staging reported not gated |
| Biological reference | clear (not at issue) | consolidation staging / reverse-dependency order; the autopsy turns on instrumentation, not biology |
| Prerequisites | present | P0 positive control `intact_readouts_nondegenerate` met (0.4999999 vs 1e-09 threshold) |
| Implementation completeness | **complete for the run**; **defective in the fingerprint instrument** | the experiment executed one coherent substrate; `arm_fingerprint` mislabelled 6 of 8 cells |
| Environment adequacy | adequate | sigma grid 0/0.25/0.5/1.0/2.0, warm_steps 40 |
| Measurement adequacy | adequate | per-phase tolerance distribution + Spearman/sign/Kendall's W as designed |
| Integration adequacy | coupled | — |
| Scale / capacity | **adequate for the gated claim; underpowered for the reported staging verdict** | n=8, sign test p=0.727 — which is exactly what the run reports and does not gate |

**Recommended `epistemic_category`: `instrument_repair_validated`** — the defect referred for
adjudication was tested and refuted; the instrument's controlled comparison held.
**Recommended `evidence_direction`: `supports` (SD-068) — UNCHANGED.**

---

## 5. The load-bearing output: a false-HIT channel in arm-reuse

The investigation exposed a defect more consequential than the one it was sent to adjudicate.

`arm_cell` computes `substrate_hash` by hashing source files **from disk at cell entry**. The cell then
executes **in-memory** bytecode frozen at process start. When the checkout moves mid-run, those two
diverge, and the manifest records the *disk* state. Here, 6 of 8 cells are stamped `c8d6d0e2` while
executing `e9a22a91`.

`experiments/_lib/arm_fingerprint.py:20-27` states the governing asymmetry:

> a false cache-HIT corrupts a scientific conclusion; a false cache-MISS only wastes compute. So the
> fingerprint is deliberately OVER-inclusive.

Over-inclusion is supposed to buy false **misses** only. This is a false **label**, and it runs in the
dangerous direction: a future consumer matching on `c8d6d0e2` would be served a cell that actually ran
`e9a22a91`. All 8 cells here carry `reuse_eligible: true`. The safety argument the whole reuse design
rests on does not hold across a mid-run checkout move.

**Fix shape** (see `recommended_substrate_queue_entry`): resolve substrate identity **once at process
start** and reuse it for every cell, and/or derive it from the *loaded modules*
(`sys.modules[...].__file__` content as imported) rather than a fresh disk read. Either makes the
recorded identity the executed identity. A cheap adjunct: re-hash at process exit and stamp a
`substrate_stable_across_run` boolean, so the divergence is recorded as the *instrument* event it is
rather than as per-cell substrate identity.

---

## 6. D3's triage model needs a process-topology qualifier

The sweep's sec-4 severity test asks *where the split falls relative to the finding-bearing comparison*.
It does not ask **whether the change reached execution at all** — and that is a prior question, because
where the boundary falls is irrelevant if no boundary existed in the executed code.

Whether a mid-run hash change reaches execution depends on process topology:

| topology | does the change reach execution? |
|---|---|
| single process, module-scope imports (**778a**) | **No** — bytecode frozen at first import; recording artifact only |
| subprocess or runner restart per cell | **Yes** — each cell imports fresh; genuine confound |
| lazy import first touched *after* the change | **Partially** — only the deferred module |

Recommendation: add this as a **gate ahead of** the sec-4 severity table, applied per run — cheap to
evaluate (one `grep` for module-scope imports plus the elapsed/arm-count consistency check that
distinguishes one process from N).

**This bears on 689d's own D3.** `failure_autopsy_V3-EXQ-689d_2026-07-20.json`
`targets[0].defects[2]` asserts *"ree_core was edited on DLAPTOP-4.local between ARM_ON seed 42 and
ARM_ON seed 43, while the run was in flight"* and draws the decisive conclusion that `C_PRIMARY` had
zero validly-controlled surviving seeds. That inference carries the same unstated premise. It is
**not re-adjudicated here** — 689d's D1 (`hold_weighted_dv`, DISQUALIFYING) and D2
(`vacuous_matched_noise_control`) stand independently of D3, so its conclusion is not obviously at
risk — but the premise should be checked, along with the other 40 corpus hits. Routed as a follow-on,
per the user's Step 8 decision.

---

## 7. Learning extracted

1. **A per-cell substrate hash records the DISK, not the EXECUTED code.** For a single-process run with
   module-scope imports, a mid-run checkout move produces cells labelled with bytecode they never ran.
   The recorded divergence is an instrument event, not necessarily an experimental one.
2. **This is a false-HIT channel in the arm-reuse fingerprint** — the one failure mode the design's
   governing asymmetry says must never occur. It is not covered by over-inclusion, which buys false
   misses only.
3. **D3 severity must be gated on process topology before the sec-4 comparison test is applied.**
4. **A between-seed-variance finding under a heterogeneous seed pool is testable, not merely suspect.**
   Partition the seeds by substrate and compare match rate, order diversity, and per-phase spread. Here
   the homogeneous six-seed partition reproduced the full spread, which converts a "SEVERE" structural
   flag into a *strengthened* finding. The test is cheap and should precede any downgrade.
5. **Check `evidence_direction_per_claim`, not just the top-level `evidence_direction`,** when scoping
   directional exposure. 778a's exposure is one claim (SD-068), not the four it is tagged with.
6. **Reconstructing a substrate hash from git is tractable and decisive** — detached worktrees plus the
   commit's own `compute_substrate_hash` reproduced both hashes byte-exact, converting "the code
   changed, we don't know how" into a named commit and a one-file diff. Worth doing on any D3 hit whose
   verdict is load-bearing.

---

## 8. Routing (confirmed by the user at the Step 8 gate)

| # | Route | Content |
|---|---|---|
| 1 | **governance-ratification-no-write** | 778a: `supports` on SD-068 **stands**. D3 refuted as an execution confound. No re-queue, no re-run, no substrate build *for 778a*. Governance writes the `evidence_quality_note` below. |
| 2 | **implement-substrate** | Fix `arm_fingerprint` so recorded substrate identity equals executed substrate identity (sec 5). `recommended_substrate_queue_entry.action: create`. |
| 3 | **doc correction** | Add the process-topology gate (sec 6) ahead of the sec-4 severity table in `intra_run_substrate_divergence_sweep_2026-07-20.md`; correct sec 5c's verdict and its "four claims" scope. |
| 4 | **follow-on chip** | Topology re-check of 689d's D3 and the other 40 corpus hits. Not re-adjudicated here. |

**Re-derive brake:** does not fire — 0 `substrate_ceiling` autopsies under the R1-R3 convention on each
of SD-068, MECH-168, MECH-169, INV-047.

**Granularity-debt recurrence:** four prior autopsies touch these claims
(`SD-068-rem-fanout-cluster`, `778c`, `778g`, `778h`), so the trigger is technically live. It is
**recorded but not routed to `/claim-synthesis`**: those adjudicate SD-068's *readout content-fidelity*
(all `measurement_gap` / `instrument_repair_validated`), a coherent single instrument-validation line
against one substrate — not structurally different failure signatures circling a coarse claim. This
autopsy adjudicates an *experimental-control* defect and is a fifth instance of the same
instrument-validation theme, which is evidence of a well-scoped claim under active instrument repair,
not of granularity debt.

**Hypothesis-space ledger (Step 9b): skipped cleanly, deliberately.** This autopsy emits no
`fanout_recommendation` and resolves no pre-registered leg. The registry's SD-068 question
`consolidation_readout_validity` (6 hypotheses, all resolved by 778c-778h) asks whether the per-phase
readouts measure content fidelity or raw noise sensitivity — a different question from 778a's staging
order, and 778a appears in none of its `adjudicating_runs`. Nothing to pre-register or resolve.

### Draft `evidence_quality_note` for governance to write (SD-068)

> Referred to `/failure-autopsy` by the 2026-07-20 intra-run substrate divergence corpus sweep (sec 5c,
> defect class D3) as SEVERE: cells carry two `arm_fingerprint.substrate_hash` values (`e9a22a91` seeds
> 42/7; `c8d6d0e2` the other six), and the finding
> (`staging_seed_variable_underpowered`) is a claim about between-seed variance. **Adjudicated
> 2026-07-20 (`failure_autopsy_V3-EXQ-778a_2026-07-20`): D3 REFUTED for this run; direction unchanged.**
> Both hashes were reconstructed byte-exact from git — `e9a22a91` = ree-v3 `6614a2e`, `c8d6d0e2` =
> `da873a1` — and `da873a1` changed exactly one file, `experiments/_lib/consolidation_lesion_harness.py`,
> which the driver binds at module scope (line 72) before the seed loop. With no `importlib`/`reload` in
> the execution path, all 8 seeds executed the `e9a22a91` harness; only the disk moved. Independently,
> the variability does not partition along the boundary: both partitions match the predicted order at
> 50% (1/2 and 3/6), the 2-seed partition's REM tolerance range [0.846, 1.350] lies entirely inside the
> 6-seed partition's [0.433, 1.500], and the 6-seed homogeneous partition's REM sd (0.435) exceeds the
> pooled sd (0.396) — i.e. the full reported spread is reproduced within one substrate. The finding is
> strengthened, not weakened. Note directional exposure is SD-068 only; MECH-168/MECH-169/INV-047 are
> tagged `unknown` in `evidence_direction_per_claim`. Separately, the run exposed a false-HIT channel in
> the arm-reuse fingerprint (6 cells stamped with code they did not execute) — routed to
> `/implement-substrate`; those cells must not be served as reuse hits under `c8d6d0e2`.
