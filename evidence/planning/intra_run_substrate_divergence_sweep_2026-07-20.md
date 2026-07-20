# Intra-run substrate divergence — corpus sweep and triage (defect class D3)

**Generated** 2026-07-20T06:24Z · **Session** `zen-dijkstra-c0fe33`
**Corpus** `REE_assembly/evidence/experiments/**` at REE_assembly `a1559b5160` · substrate ree-v3 `62b3f43`
**Origin** [`failure_autopsy_V3-EXQ-689d_2026-07-20.md`](failure_autopsy_V3-EXQ-689d_2026-07-20.md) sec 4
(REE_assembly `2e6cc2569b`), `targets[0].defects[2]` (D3) + `secondary_routing_recommendation`, which
specified exactly this scan and explicitly deferred it out of scope.
**Companion** [`hold_weighted_e3_readout_corpus_sweep_2026-07-20.md`](hold_weighted_e3_readout_corpus_sweep_2026-07-20.md)
— independent defect; this document follows its shape.

> **One line.** **42 of 164** runs carrying per-cell fingerprints changed substrate MID-RUN — a
> **25.6% base rate**, far above what 689d alone suggested. **Six carry a live directional verdict**;
> of those, **three are SEVERE** (`V3-EXQ-782` *weakens* MECH-459, `V3-EXQ-604c` *supports* the
> MECH-314 family, `V3-EXQ-778a` *supports* SD-068/INV-047) and are routed to `/failure-autopsy`.
> The defect is **structurally invisible on ~85% of the corpus**: only 164 of 1065 runs stamp
> substrate per cell at all, and the always-core per-run field would have hidden every one of the 42.

---

## 1. The defect, and why nothing catches it

A multi-arm experiment is a controlled comparison **only if every cell ran against the same substrate
build**. `arm_fingerprint.substrate_hash` is a sha256 over the *content* of `ree_core/**/*.py`,
`experiments/_harness.py`, `experiments/_metrics.py`, `experiments/_lib/**/*.py` and (optionally) the
driver script — a content hash, not a git SHA, precisely because "this workflow runs dirty trees
constantly" (`experiments/_lib/arm_fingerprint.py:20-27`). So if the checkout changes while a run is
in flight, cells executed after the change carry a different hash.

On **V3-EXQ-689d** that happened between `ARM_ON` seed 42 and seed 43 on `DLAPTOP-4.local`, and it was
decisive: the only seed whose treatment arm shared a substrate with its own controls was the one seed
that **failed** the primary criterion, leaving `C_PRIMARY` with **zero validly-controlled surviving
seeds**.

**Why no existing gate sees it.** It is a *confound*, not noise, so no margin arithmetic bounds it,
and it survives any DV repair:

| Gate | Blind because |
|---|---|
| `e3_diagnostics_staleness_lint` (form 1) | static AST scan of driver source; substrate identity is a runtime property |
| `e3_hold_weighted_readout_lint` (form 2) | same — and hold-weighting is an orthogonal defect |
| `validate_recording.py` | checks fields are *present*, never that per-cell values *agree* |
| always-core per-run `substrate_hash` | **actively hides it** — see below |

**The per-run field is the trap.** `experiments/_lib/manifest_core.py:117`
`_hoist_multi_arm_substrate_hash()` fills the top-level `substrate_hash` from **the first arm's**
fingerprint. A divergent run therefore records one hash and looks clean. The Experimental Recording
Standard specifies that per-run field as always-core — so on a manifest without per-cell
fingerprints this defect is not merely undetected, it is **unrecordable**. Confirmed on 689d, whose
top-level `substrate_hash` is in fact absent entirely.

## 2. Method, and the false-positive channels ruled out

For every JSON under `evidence/experiments/**` (7758 files; flat manifests and `<run>/manifest.json`
packs, deduped by `run_id`, preferring the record with more fingerprinted cells), collect the set of
`arm_results[].arm_fingerprint.substrate_hash` and report cardinality > 1. Sanity-checked against
689d: reproduces its 10/2 split and both hashes exactly.

A hash can differ for reasons *other* than a code edit. All were checked and **all are clean**:

| Benign channel | Check | Result |
|---|---|---|
| differing `scope`/`globs` per cell (author-declared narrowing) | `globs` set per run | **0 of 42 vary** |
| `scoped` flag differing per cell | `scoped` set per run | **0 of 42 vary** |
| cross-machine-class execution | `machine_class` set per run | **0 of 42 vary** |
| driver-script inclusion toggled per cell | `driver_script_in_substrate_hash` set per run | **1 of 42 varies — V3-EXQ-788 only** |
| `__pycache__` / build artefacts | globs are `*.py` only (`arm_fingerprint.py:65`) | not reachable |

So **41 of 42 are genuine mid-run substrate changes.** `V3-EXQ-788` is excluded as an artefact: its
two hashes correspond exactly to `driver_script_in_substrate_hash` `False` vs `True`, i.e. the
fingerprint *call signature* changed mid-run, not necessarily the substrate.

**Two corroborating signals, neither used to define a hit.** `driver_script_hash` is constant in 37
of 42 — so the edit was in `ree_core`/`_lib`, not the driver (exceptions: 705, 705b, 706, 706b,
785b, where the driver was edited mid-run too). And in **19 of 42** `substrate_n_files` *changes*
within the run — files were literally added or removed mid-flight (V3-EXQ-655 spans 94→100 files
across **9** distinct substrates).

## 3. Sweep result

| | count |
|---|---|
| distinct run directories in corpus | 1065 |
| runs carrying per-cell `arm_fingerprint` (**the scannable population**) | **164** |
| — **divergent (cardinality > 1)** | **42 (25.6%)** |
| — of which genuine substrate change (788 excluded as instrument artefact) | **41** |
| runs with **no** per-cell stamping — defect undetectable | **901 (84.6%)** |

Divergence depth: 20 runs at 2 hashes, 13 at 3, 6 at 4, and one each at 6 (`780`), 8 (`784`), 9 (`655`).

**Directional exposure.** Within the 164-run scannable population, 37 carry a live directional
verdict (31 `supports`, 6 `weakens`); **6 of those 37 (16.2%) are divergent**. The remaining hits are
24 `non_contributory`, 7 `unknown`, 2 `inconclusive`, 2 `does_not_support`, 1 unset.

**Temporal/host pattern.** Hits concentrate on heavy-development days across the whole fleet, not on
one machine — `ree-cloud-2` (10), `ree-worker-1` (7), `ree-cloud-4` (6), `DLAPTOP-4.local` (6),
`ree-worker-3` (4), `ree-cloud-3` (3), others. **2026-07-18 alone produced 6 divergent runs**
(777a, 779a, 780, 781, 782, 784). So the 689d story — "edited locally while in flight" — is the
*local* instance of a fleet-wide pattern: cloud workers are equally exposed, because a worker's
checkout can move under a long run just as a laptop's can.

## 4. The triage test

A hit is **not automatically fatal**. Severity depends on whether the split crosses the comparison
that carries the finding.

| Class | Test |
|---|---|
| **SEVERE** | the split separates a treatment arm from its controls, **or** splits seeds within an arm such that the finding-bearing seeds are the divergent ones, **or** the finding is itself a statement about between-seed variance while the seed pool is substrate-heterogeneous |
| **LESS SEVERE** | the split falls wholly inside a non-finding-bearing arm; or is symmetric across all arms (all changed together between seeds); or every comparison is *within* a cell, so no contrast crosses the boundary and the split only affects pooling homogeneity |

## 5. Verified verdicts — the six live directional hits

### 5a. V3-EXQ-782 — SEVERE, highest structural severity in the corpus

`evidence_direction: **weakens**` MECH-459 · FAIL · `ree-worker-1` · 2026-07-18 · **4 substrates**

The finding-bearing arms are the ones fragmented, and maximally:

| substrate | cells |
|---|---|
| `098473b9` | `local_view_greedy` 42/43/44, `greedy_oracle` 42/43/44, `random_walk` 42/43/44, `probeR_ctrl_zworld` **42** |
| `765ce9d2` | `probeR_ctrl_zworld` **43** |
| `a652aa3d` | `probeR_ctrl_zworld` **44**, `probeR_ctrl_raw` 42/43 |
| `7f856703` | `probeR_ctrl_raw` **44** |

Every baseline/anchor arm sits on one substrate; **both probe arms — which carry the entire finding —
are split, and `probeR_ctrl_zworld`'s three seeds ran on three different builds.** The headline is a
`z_world` vs `raw_view` per-representation contrast
(`forage_mass_already_concentrated` / `critic_flat_uninformed`); that contrast is **wholly
cross-substrate**, and the per-seed spreads it reports
(`separation_ratio_per_seed [0.000251, 0.032429, 0.015187]`) are confounded with build identity.
`substrate_n_files` moves 131→132→133 within the run.

This matters beyond 782: per the standing conversion-ceiling map, MECH-459's **strong form is
recorded as refuted**, and 782 is the `weakens` carrying that. **Route first.**

### 5b. V3-EXQ-604c — SEVERE, the exact 689d signature

`evidence_direction: **supports**` MECH-314 / 314a / 314b / 314c / Q-044 · PASS · `ree-cloud-2` · **2 substrates**

| substrate | cells |
|---|---|
| `f80bc236` | `ARM_OFF` 42/43/44, `ARM_ALL_ON` **42** |
| `0bedd600` | `ARM_ALL_ON` **43/44**, `ARM_NOVELTY_OFF` ×3, `ARM_UNCERTAINTY_OFF` ×3, `ARM_LP_OFF` ×3 |

**This is 689d's signature reproduced exactly**: the whole control arm on one build, the treatment
arm split 1/2 across the boundary. The load-bearing `C1` is
`c1_parent_delta_on_vs_off = 0.402505` — `ARM_ALL_ON` vs `ARM_OFF` — so **two of the three treatment
seeds are compared against controls built from different code**. `C2`'s sub-flavour deltas are
measured against `ARM_ALL_ON`, so they inherit the same split. `substrate_n_files` 90→91: a file was
**added** mid-run.

**Note a second, independent observation** (not a divergence finding, and not adjudicated here):
`selected_entropy` is *exactly* equal for `ARM_OFF` and `ARM_NOVELTY_OFF` (0.649722), and exactly
equal across `ARM_ALL_ON`, `ARM_UNCERTAINTY_OFF`, `ARM_LP_OFF` (0.247217). Here that is plausibly
**substantive** rather than the companion sweep's sec-6 vacuity tell — it is the literal content of
`c2_sub_flavour_deltas` (novelty 0.402505; uncertainty and LP both **0.0**), i.e. novelty is the only
active sub-flavour. But it does mean `C1` and the novelty leg of `C2` are the **same comparison**, so
they do not independently corroborate. Worth the autopsy's attention.

### 5c. V3-EXQ-778a — SEVERE *for its specific claim*

`evidence_direction: **supports**` SD-068 / MECH-168 / MECH-169 / INV-047 · PASS · `ree-worker-1` · **2 substrates**

| substrate | seeds |
|---|---|
| `e9a22a91` | 42, 7 |
| `c8d6d0e2` | 123, 2024, 99, 7777, 314, 1000 |

Structurally this looks mild — the sigma-sweep comparison behind load-bearing
`C1_monotone_degradation_all_phases` is *within* a seed, so no single comparison crosses the
boundary. **But the finding is `staging_seed_variable_underpowered`** — a claim *about between-seed
variability* (`modal_order_seed_count: 4`, `n_seeds_matching_prediction: 4` of 8). Two of the eight
seeds ran on different code, so an unknown share of the reported seed-to-seed variability is
**substrate variability, not seed variability**. The defect lands squarely on the quantity the
conclusion is made of. This is the third severity limb of the sec-4 test.

### 5d. V3-EXQ-784 — un-adjudicated; most fragmented run, but no registered claim

`evidence_direction: **supports**` · PASS · `claim_ids: null` (SD-074) · `ree-worker-1` · **8 substrates over 56 cells**

The most fragmented run in the corpus. Grouping is broadly seed-ordered — the bulk (35 cells,
seeds 3–83) sits on `849de508` — but the early seeds are badly split: **seed 11 spans four different
substrates**, and seeds 17, 23, 29, 37, 3 each straddle a boundary. Since the informative-vs-saturated
read is a *within-seed across-budget* comparison, those early seeds' comparisons **are**
cross-substrate. Load-bearing `C1` (0.7857 vs 0.5 threshold) aggregates 14 seeds, so the majority of
its mass is substrate-clean and the margin is wide.

**Ranked below 782/604c/778a because `claim_ids` is null — it weights no claim today.** Flagged, not
routed. If SD-074 is later given registered claim_ids, re-examine before citing.

### 5e. V3-EXQ-716a — LESS SEVERE, finding survives on matched seeds

`evidence_direction: **supports**` SD-063 · PASS · `ree-cloud-2` · **2 substrates** (seeds 42, 43 | seed 44)

All three load-bearing criteria (`C1_crps_quantile_beats_point`, `C2_precision_error_corr_over_ema_null`,
`C3_sd031_agency_residual_preserved`) won on **3 of 3 seeds** against a pre-registered
`majority_needed: 2`. The divergent seed is 44; **seeds 42 and 43 are mutually substrate-matched and
by themselves satisfy the pre-registered majority on all three criteria.** Each criterion is also an
internal per-seed comparison, so nothing contrasts across the boundary. **No action owed** — the
verdict stands on a substrate-homogeneous subset that independently clears the bar.

### 5f. V3-EXQ-689d — already routed

`supports` MECH-448 · the origin case. Autopsy complete
(`failure_autopsy_V3-EXQ-689d_2026-07-20`); D3 is recorded there as
`sufficient_alone_to_withdraw: true`. No new routing owed. Listed for completeness.

## 6. Cross-reference with the hold-weighted E3 sweep

Runs hit by **both** defects are priority re-adjudication candidates. Against the ~30 runs verified
in depth in the companion document, the intersection is **three**:

- **V3-EXQ-689d** — both defects, already routed; D3 alone forces withdrawal.
- **V3-EXQ-689e** — companion verdict "verified SAFE"; divergent here but `non_contributory`. No action.
- **V3-EXQ-662** — `non_contributory`, so no direct exposure, **but worth one line**: 662/663 is the
  driver whose matched replay *calibrated* the hold-weighting cost at −0.87%…+0.64%. The calibration
  instrument is itself intra-run divergent (2 substrates, `n_files` 97→98). That does not invalidate
  the calibration — it was a matched replay on a fixed checkout, not a re-use of the original cells —
  but the original 662 manifest should not be treated as a clean reference run.

**This intersection is a lower bound**, not a complete join: the companion sweep names ~30 of its 150
fires explicitly, and the full fire list was not re-derived here.

## 7. Recommended routing

1. **`/failure-autopsy` V3-EXQ-782** — `weakens` MECH-459; finding-bearing probe arms split across
   three substrates. Highest structural severity.
2. **`/failure-autopsy` V3-EXQ-604c** — `supports` MECH-314/314a/314b/314c/Q-044; exact 689d
   signature. Note the C1/C2-novelty non-independence (sec 5b).
3. **`/failure-autopsy` V3-EXQ-778a** — `supports` SD-068/MECH-168/MECH-169/INV-047; the
   seed-variance conclusion is confounded with substrate variance.
4. **V3-EXQ-784** — flagged, not routed (no registered claim_ids). Re-examine before any citation.
5. **The 36 non-directional hits** — no routing owed while `non_contributory` / `unknown` /
   `inconclusive` / `does_not_support`. But **any one of them promoted to a directional verdict must
   be triaged against sec 4 first.** The list is machine-derivable by re-running the sec-2 scan.

**No manifest was edited.** Completed runs are re-adjudicated via `/failure-autopsy`, never
rewritten. This document records findings only.

## 8. Recommendations (proposed, not implemented)

**(a) A lint / `manifest_core` assertion that a run's cells share one `substrate_hash`.**
Recommended, with one design caution. The natural home is `manifest_core.py:117`
`_hoist_multi_arm_substrate_hash()` — it *already iterates every arm's fingerprint* and returns the
first hash, so the check costs nothing and sits exactly where the information is currently discarded.
Emit `substrate_divergent: true` plus the partition map into the manifest rather than only warning,
so the fact is recorded at write time and this sweep never has to be re-derived.

Caution: it must **not** be a hard failure at manifest-write time. By then the compute is spent, and
refusing to write the manifest would destroy an expensive run over a defect that is sometimes
survivable (`716a`). The correct shape is **record-and-WARN at write, gate at adjudication** — the
same posture both E3 lints take. It should also key on the `driver_script_in_substrate_hash`
discriminator so it does not fire on the 788 artefact class.

A cheap complement: have the runner stamp the substrate hash at run **start** and **end** and warn on
mismatch. That catches single-arm runs too, which per-cell fingerprints cannot reach today.

**(b) Should the Recording Standard specify per-CELL substrate stamping?** **Yes** — and this is the
generalisable lesson from 689d. The current standard makes `substrate_hash` always-core **per run**;
the hoist then reduces a heterogeneous run to one hash and reports it as if homogeneous. That is
worse than absent, because it looks like positive evidence of homogeneity.

The principle: **provenance granularity must follow the unit of COMPARISON, not the unit of
execution.** A run is the unit of execution; the *cell* is the unit of comparison, because that is
what arms and seeds are contrasted at. Any provenance field recorded coarser than the comparison it
must license can only mislead. `arm_fingerprint` already gets this right — which is the only reason
this defect class is visible at all — so the change is to *promote the existing per-cell field to
core for multi-arm runs* and demote the per-run hoist to a derived convenience explicitly marked as
first-arm-only.

Concrete consequence of not doing it: **901 of 1065 runs (84.6%) cannot be scanned for this defect at
all, retroactively or otherwise.** That number is the cost of the current granularity.

## 9. Coverage and limits

- **The scan covers 164 of 1065 runs (15.4%).** The other 901 carry no per-cell substrate stamp, so
  they are not "clean" — they are **unobservable**. The 25.6% base rate is measured on the
  fingerprinted population and should not be extrapolated to the whole corpus without stating that
  the fingerprinted population skews recent (fingerprints post-date the Phase-0 arm-reuse work) and
  therefore toward the fleet's most active development period.
- **41 of 42 hits are confirmed genuine** substrate changes; V3-EXQ-788 is excluded as a
  fingerprint-API artefact (sec 2). Both figures are stated separately throughout.
- **6 of 42 hits were triaged in depth** (sec 5) — the complete set carrying a live directional
  verdict. The other 36 are enumerated but **not adjudicated**; their directions are
  `non_contributory` / `unknown` / `inconclusive` / `does_not_support`, which is why they were
  deprioritised, not a judgement that they are sound.
- **The scan detects divergence, never its content.** Two hashes tell you the code changed, not what
  changed or whether the change could affect the DV. Establishing that requires the autopsy — which
  is exactly why hits are routed rather than adjudicated here. A hit is a **loss of experimental
  control**, not a demonstration that the result is wrong.
- **The intersection with the hold-weighted sweep (sec 6) is a lower bound** — matched against that
  document's ~30 verified runs, not its full 150-fire list.
- **`substrate_n_files` deltas under-report file edits**: a modified-in-place file changes the hash
  without changing the count, so 19 of 42 is a floor on how many runs saw structural change.
