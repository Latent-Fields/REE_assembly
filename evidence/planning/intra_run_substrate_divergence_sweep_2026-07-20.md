# Intra-run substrate divergence — corpus sweep and triage (defect class D3)

**Generated** 2026-07-20T06:24Z · **Session** `zen-dijkstra-c0fe33`
**Corpus** `REE_assembly/evidence/experiments/**` at REE_assembly `a1559b5160` · substrate ree-v3 `62b3f43`
**Origin** [`failure_autopsy_V3-EXQ-689d_2026-07-20.md`](failure_autopsy_V3-EXQ-689d_2026-07-20.md) sec 4
(REE_assembly `2e6cc2569b`), `targets[0].defects[2]` (D3) + `secondary_routing_recommendation`, which
specified exactly this scan and explicitly deferred it out of scope.
**Companion** [`hold_weighted_e3_readout_corpus_sweep_2026-07-20.md`](hold_weighted_e3_readout_corpus_sweep_2026-07-20.md)
— independent defect; this document follows its shape.

> **SUPERSEDED — read sec 3a first.** The original one-line summary is retained immediately below,
> struck through, because sec 3a exists to catch the reasoning error it makes. **All three SEVERE
> routings were adjudicated and all three were REFUTED, each by a different mechanism; the ladder was
> then applied to all 42 hits and NONE survives as a demonstrated loss of experimental control.**
> The scan detects that a *hash* changed — which, given a deliberately over-inclusive glob and a
> universally single-process corpus, is a poor proxy for a change in *executed code*.
>
> **Corrected one line.** **42 of 164** fingerprinted runs (**25.6%**) changed `substrate_hash`
> mid-run — but that is a base rate of **hash changes, not of defects**. Under the sec-3a ladder
> **11** are glob-scope false positives (the changed files are on no import path the run executes),
> **29** never reached execution (single process, module-scope import binding), **1** is unverifiable
> (driver never committed) and **1** was already excluded as an instrument artefact. **Defect base
> rate: 0 of 42.** The genuine and unchanged finding is the *recording* one: only 164 of 1065 runs
> stamp substrate per cell, so on ~85% of the corpus this class is **unobservable**, and the
> always-core per-run field would have hidden every one of the 42 (sec 8b stands).
>
> ~~**One line.** **42 of 164** runs carrying per-cell fingerprints changed substrate MID-RUN — a
> **25.6% base rate**, far above what 689d alone suggested. **Six carry a live directional verdict**;
> of those, **three are SEVERE** (`V3-EXQ-782` *weakens* MECH-459, `V3-EXQ-604c` *supports* the
> MECH-314 family, `V3-EXQ-778a` *supports* SD-068/INV-047) and are routed to `/failure-autopsy`.
> The defect is **structurally invisible on ~85% of the corpus**: only 164 of 1065 runs stamp
> substrate per cell at all, and the always-core per-run field would have hidden every one of the 42.~~

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

> **Correction (2026-07-20).** Every count in this section is a count of **hash changes** and is
> reproduced exactly by the sec-3a re-derivation. But "genuine substrate change" in the row below
> means only *the bytes under the glob differed* — **not** that the run lost experimental control.
> Under the ladder, **0 of the 41 are confirmed losses of experimental control** (sec 3a-summary).
> Read this table as an instrument-behaviour table, not a defect table.

**Directional exposure.** Within the 164-run scannable population, 37 carry a live directional
verdict (31 `supports`, 6 `weakens`); **6 of those 37 (16.2%) are divergent**. The remaining hits are
24 `non_contributory`, 7 `unknown`, 2 `inconclusive`, 2 `does_not_support`, 1 unset.

**Temporal/host pattern.** Hits concentrate on heavy-development days across the whole fleet, not on
one machine — `ree-cloud-2` (10), `ree-worker-1` (7), `ree-cloud-4` (6), `DLAPTOP-4.local` (6),
`ree-worker-3` (4), `ree-cloud-3` (3), others. **2026-07-18 alone produced 6 divergent runs**
(777a, 779a, 780, 781, 782, 784). So the 689d story — "edited locally while in flight" — is the
*local* instance of a fleet-wide pattern: cloud workers are equally exposed, because a worker's
checkout can move under a long run just as a laptop's can.

## 3a. The triage ladder — apply BEFORE sec 4

> **Added 2026-07-20T07:13Z** (session `musing-einstein-c80816`) after all three SEVERE routings from
> sec 7 were adjudicated and **all three were refuted, each by a different mechanism**. Sec 4 asks
> *where the split falls*. It presupposes that a `substrate_hash` change means the executed code
> changed — and on 3 of 3 adjudicated cases that presupposition was false. The three rungs below each
> test that presupposition directly, are cheap, and can exonerate a hit outright. **Run them first.**
> Sections are numbered `3a` rather than inserted as a new `4` so that the existing cross-references
> from the three autopsies (`sweep sec 4`, `sec 5a`, `sec 7`, `sec 8(a)`) stay valid.

Numbering note: rung (d) is the pre-existing sec-4 test, unchanged.

| rung | question | clears the hit when | cost | worked case |
|---|---|---|---|---|
| **(a) glob scope** | is the changed file on any import path the run *executes*? | closure-restricted fingerprint is constant across bands | one import trace + rehash | `V3-EXQ-782` |
| **(b) process topology** | did the change *reach execution* at all? | single process + module-scope import binding | one `grep` + a consistency check | `V3-EXQ-778a` |
| **(c) DV inertness** | do the recorded numbers actually differ across the boundary? | cross-boundary matched cell-pairs bit-identical on trajectory quantities | manifest arithmetic only | `V3-EXQ-604c` |
| **(d) comparison structure** | does the split cross the finding-bearing contrast? | *see sec 4* | manifest reading | `V3-EXQ-716a` |

### (a) Glob scope — is the changed file even on the executed path?

`_SUBSTRATE_GLOBS` (`arm_fingerprint.py:65-70`) hashes **all** of `ree_core/**/*.py`,
`experiments/_harness.py`, `experiments/_metrics.py`, `experiments/_lib/**/*.py`. The module documents
this over-inclusion at `:14-17` as "over-inclusion -> false misses only" — correct for its **designed**
purpose (arm-reuse cache validity, where a false miss is free), and **wrong** when the same field is
repurposed as a divergence detector, where over-inclusion converts directly into false positives.
**The defect is in the reuse, not the field.**

Test: build the transitive **static** import closure of the run's driver, intersect it with the globs,
and recompute the fingerprint byte protocol (`arm_fingerprint.py:216-232`) restricted to that closure,
**deriving the closure per tree, not from the tip**. Constant across bands -> the executed code was
byte-identical -> **glob-scope false positive**.

Soundness condition: the closure is *static*. Scan it for `importlib`, `__import__`, `exec(`,
`pkgutil`, `entry_points` before relying on it — **per run, never assumed** (782 returned zero, so its
static trace was sound; beware `harm_eval(` / `.eval()` substring false positives on `eval(`).

Generating mechanism, which is why this rung clears so much: **parallel development in globbed
directories**. All three files that moved under 782 belonged to other sessions' concurrent work
(SD-070, EXQ-783, SD-068) and were on no import path of 782. This predicts that the sweep's
"2026-07-18 alone produced 6 divergent runs" clustering is largely an artefact of **development
volume**, not of experimental fragility — and sec 3a-summary below confirms it.

### (b) Process topology — did the change reach execution?

CPython caches modules in `sys.modules` at first import. A file edited on disk *after* a driver has
bound it is not re-read; the process keeps executing the bytecode frozen at import time. So a disk
change during a run may never reach execution at all.

| topology | reaches execution? |
|---|---|
| single process, imports bound at **module scope** before the seed/arm loop | **NO** — bytecode frozen at first import |
| subprocess or runner restart **per cell** | **YES** — each cell re-imports from the current disk |
| **lazy** import first touched *after* the change | **PARTIALLY** — cells before the first touch are clean |

Two cheap checks, both required:

1. **`grep` the driver at its run-time revision for module-scope imports** of the changed file (e.g.
   `from experiments._lib import consolidation_lesion_harness as H` at line 72). Confirm no
   `importlib` / `reload(` / `__import__` in driver or the imported module, and that any deferred
   import is either in an untouched tree or `sys.modules`-cached after the first cell.
2. **Distinguish one process from N** by an elapsed/arm-count consistency check. The single-process
   signature is: the hash split is a **contiguous prefix** in cell-execution order, exactly **one**
   monotone transition, **each seed present exactly once**, within **one coherent elapsed window**.
   A restart shows the opposite tell — it would **re-run** the cell it died on against the new
   substrate. Corroborate by timing: the landing commit's committer date should fall at the observed
   boundary given `elapsed / n_cells`.

**Precondition, and it bites:** this rung needs per-cell `elapsed_seconds`. Where that always-core
field is missing, check 2 cannot be run from the manifest and the rung degrades to check 1 alone.

### (c) DV inertness — do the recorded numbers differ across the boundary?

The strongest rung when it is available, because it is **indifferent to what changed** — it does not
need the commit identified, and so it survives the dirty-tree case where hash archaeology fails.

Find any two cells on **opposite sides** of the boundary whose *intended* difference is separable
from the substrate difference — most cleanly, matched by seed — and compare **all** recorded per-cell
fields. Bit-identity on the **trajectory-determined** quantities (discrete histograms such as
`selected_class_counts` and `candidate_first_action_counts`, plus `n_p1_ticks`, `n_buffer_appends`,
entropies, pairwise distances) exonerates the boundary. Fields that differ are fine **iff** every one
is bookkeeping the arm's own treatment is defined to change.

The residual-objection is answerable by arithmetic, not judgement: for the substrate change to have
had an effect that the treatment exactly cancelled, the cancellation would have to hold simultaneously
across several arms, several seeds, and 20+ independent continuous **and discrete-count** quantities
to full recorded precision. That is not a credible confound.

### The general lesson: reconstruct both hashes from git

On any hit whose verdict is load-bearing, **reconstruct the manifest's hashes from committed trees**:
detached worktrees at each candidate commit, hashed with **that commit's own**
`experiments/_lib/arm_fingerprint.compute_substrate_hash` (folding the driver in iff
`driver_script_in_substrate_hash`). This converts *"the code changed, we don't know how"* into a named
commit and a **file-level diff** — which is what makes rungs (a) and (b) evaluable at all.

Two disciplines on the result:

- **A reconstruction that does not match is itself a finding, not a failure.** 604c's tree was dirty
  (recomputation yields a constant +1 file offset against the manifest, and no hash matches), so its
  commit archaeology is **corroboration only** and rung (c) carried the warrant. Report such a hit as
  **`unverifiable`**, never as clean.
- **Order matters.** Prefer rung (c) where matched cross-boundary cells exist, because it is
  indifferent to attribution; use (a)/(b) where they do not.

## 3a-summary. The ladder applied to all 42 hits — **the base rate of real defects is 0**

> **Added 2026-07-20T07:46Z** (session `musing-einstein-c80816`). Method: the sec-2 scan was
> re-derived from scratch (**reproduces 164 fingerprinted / 42 divergent exactly**); every manifest
> hash was reconstructed against every `ree-v3` tree since 2026-05-20 (1861 commits, 1844 distinct
> trees) by replaying the `arm_fingerprint.py:216-232` byte protocol; band diffs were intersected
> with each driver's transitive static import closure; and driver topology was scanned for
> process-spawning and dynamic-import constructs. **The tool was validated against all four
> hand-adjudicated cases before use** — it independently reproduces 782 CLEARS at (a) with the same
> three off-path files, 778a and 689d *not* clearing (a), and 604c `unverifiable` with the same
> dirty-tree signature.

| disposition | runs |
|---|---|
| **REFUTED at rung (a)** — changed files on **no** import path the run executes | **11** |
| **REFUTED at rung (b)** — single process, module-scope binding; change never reached execution | **20** |
| **REFUTED at rung (b)**, attribution `unverifiable` (dirty tree, so *what* changed is unknown) | **9** |
| `unverifiable` — driver script was never committed (`V3-EXQ-645`) | **1** |
| excluded as instrument artefact (`V3-EXQ-788`, per sec 2) | **1** |
| **SURVIVING as a demonstrated loss of experimental control** | **0** |

**The headline 25.6% is a base rate of *hash changes*, not of defects. The defect base rate on this
corpus is 0 of 42.** The 25.6% figure should not be cited as a corpus-wide quality signal; sec 3 and
sec 9 are corrected accordingly.

**Why it collapses so completely.** Two structural facts, each independently sufficient for most hits:

1. **The glob is wider than any run's closure** (rung a). `_SUBSTRATE_GLOBS` hashes *all* of
   `ree_core/**` and `experiments/_lib/**`, while a given driver imports ~95-116 of those files. In a
   fleet where several sessions develop in those directories concurrently, the hash moves constantly
   for reasons no single run executes.
2. **Every experiment in the corpus is single-process** (rung b). Across all 30 drivers whose source
   is recoverable, there are **zero** `multiprocessing` / `Popen(` / `os.fork(` /
   `ProcessPoolExecutor` / `joblib` constructs, **zero** `importlib` / `__import__` / `reload(`, and
   — critically — **zero function-scope imports of `ree_core` or `experiments`**. So the import graph
   is frozen at first use in every case. Since a divergence boundary by construction falls **after**
   the first cell, any module the experiment exercises is already `sys.modules`-cached before the
   disk moves. *(One earlier candidate exception, `V3-EXQ-753`, was a false positive: the matched
   token `spawn` is prose about the grid-world agent's spawn point.)*

Together these mean the defect requires a topology this corpus does not contain. **D3 is real as a
mechanism and correctly specified — it is simply never realised here.** It would be realised by a
subprocess-per-cell runner or an arm-conditional lazy import, and either could appear later, so the
class should be retained as a check rather than retired.

**The nine dirty-tree cases are the weakest limb, and are honestly labelled.** For
`604b, 604c, 648a, 655, 657a, 705, 705b, 706, 706b` no hash reconstructs from committed trees, so
*what* changed is unknown and rung (a) cannot run. Their refutation rests on topology alone (rung b),
which does not depend on the change's content. **`V3-EXQ-604c` is the reassuring case here**: its
authoritative refutation is rung (c) — empirical bit-identity across five matched cross-boundary
pairs, which is indifferent to attribution — and the topological argument agrees independently. That
is two mechanisms converging on one verdict in exactly the case where attribution failed.

**Per-claim directional exposure was also re-derived**, since the sweep counted the run-level
`evidence_direction` roll-up. Six runs carry a live directional verdict, the same six as sec 5 — but
`V3-EXQ-778a` exposes **one** claim, not four (sec 5c), so live-claim exposure across the whole hit
set is **7 claim-run pairs**, not the 10 the run-level count implies. All are now refuted.



| Class | Test |
|---|---|
| **SEVERE** | the split separates a treatment arm from its controls, **or** splits seeds within an arm such that the finding-bearing seeds are the divergent ones, **or** the finding is itself a statement about between-seed variance while the seed pool is substrate-heterogeneous |
| **LESS SEVERE** | the split falls wholly inside a non-finding-bearing arm; or is symmetric across all arms (all changed together between seeds); or every comparison is *within* a cell, so no contrast crosses the boundary and the split only affects pooling homogeneity |

## 5. Verified verdicts — the six live directional hits

### 5a. V3-EXQ-782 — ~~SEVERE, highest structural severity in the corpus~~ **REFUTED (rung a)**

> **Verdict corrected 2026-07-20.** [`failure_autopsy_V3-EXQ-782_2026-07-20.md`](failure_autopsy_V3-EXQ-782_2026-07-20.md)
> (REE_assembly `2c6826d3e3`) finds this hit a **FALSE POSITIVE** and **withdraws** it. All four
> hashes reconstruct byte-exact from committed trees, but the **closure-restricted** fingerprint is
> `3b33ab7f515e21ac...` — **identical in all four bands**, over an identical 103-file set with
> identical blob OIDs. The three files that moved
> (`ree_core/latent/zworld_p0.py`, `experiments/_lib/baselines/exq783_zworld_granularity.py`,
> `experiments/_lib/consolidation_lesion_harness.py`) are on **no import path** of this run — they
> belong to other sessions' parallel SD-070 / EXQ-783 / SD-068 work. `ree_core/latent/__init__.py` is
> the empty blob in all four trees, so there is no package-import side channel.
> **The code V3-EXQ-782 executed was byte-identical in all 15 cells.** Independently, the load-bearing
> criterion is `passed = any_parity` — an OR across representations of a **within**-representation
> threshold classification — so no comparison crosses a cell boundary, and all 6 probe cells clear the
> 0.5 threshold by >=2.07x. `weakens` on MECH-459 **stands**; `epistemic_category: standard` stands;
> routing `governance-affirm`. **MECH-459's strong-form refutation is unaffected.**
>
> The section below is the **original, now-superseded** analysis, retained because sec 3a(a) exists
> precisely to catch the reasoning error it contains. Its structural description of the hash split is
> accurate; its inference from that split to a loss of experimental control is not.

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

### 5b. V3-EXQ-604c — ~~SEVERE, the exact 689d signature~~ **D3 EXONERATED (rung c)**

> **Verdict corrected 2026-07-20.** [`failure_autopsy_V3-EXQ-604c_2026-07-20.md`](failure_autopsy_V3-EXQ-604c_2026-07-20.md)
> (REE_assembly `75726ecb4c`) finds the divergence **real but DV-inert**, and **withdraws** the D3
> defect: `sufficient_alone_to_withdraw: false`. Five seed-matched cell-pairs straddle the boundary
> and are **bit-identical on every trajectory-determined quantity** — `selected_class_counts`,
> `candidate_first_action_counts`, `selected_action_class_entropy`, `n_p1_ticks`, `n_buffer_appends`,
> `n_contrastive_steps`, the `cand_world_pairwise_dist_*` and `raw_score_range_*` family. Every field
> that differs is curiosity-bias bookkeeping the arm's own treatment is *defined* to change. The
> load-bearing `C1` additionally stands on a **substrate-homogeneous** pair (`ARM_OFF` 42 vs
> `ARM_ALL_ON` 42, both on `f80bc236`) at delta **0.732** against `DISTINCT_MARGIN = 0.03` — the
> largest of the three seeds. **This is 689d inverted**: there the only substrate-matched seed was the
> one that *failed*; here it is the strongest pass.
>
> Note the tree was **dirty** — recomputation gives 89/90 files against the manifest's 90/91, a
> constant +1, and neither hash reconstructs. Commit archaeology is therefore corroboration only
> (`ree-v3 6bba8cf`, adding `ree_core/pfc/infralimbic_avoidance_gate.py` behind a config flag 604c
> never sets); the empirical bit-identity is the warrant. This is the `unverifiable`-attribution case
> of sec 3a.
>
> **Unrelated to D3, the autopsy upheld a larger defect** and this is what governance must act on:
> C2 is **structurally vacuous** for MECH-314b/314c. Uncertainty and learning-progress are Phase-1
> **global scalars broadcast across all K candidates** (`structured_curiosity.py:40-41,101`), and a
> constant added uniformly to every candidate cannot change an argmax (nor a softmax sample). So
> `delta == 0.0` is an **arithmetic identity fixed before the run**, independent of whether 314b/314c
> are true. Recommended: MECH-314 and MECH-314a `supports` **STAND**; MECH-314b, MECH-314c and Q-044
> move `mixed` -> **`non_contributory`** under `substrate_ceiling`. The re-derive brake **fires** (3
> vs threshold 2) and a further same-claim ablation is **REFUSED**. See sec 7 item 2.

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

### 5c. V3-EXQ-778a — ~~SEVERE *for its specific claim*~~ **REFUTED (rung b)**

> **Verdict corrected 2026-07-20.** [`failure_autopsy_V3-EXQ-778a_2026-07-20.md`](failure_autopsy_V3-EXQ-778a_2026-07-20.md)
> (REE_assembly `77cd4cc013`) finds the divergence **real on disk but never reached execution**, and
> **refutes** D3. Both hashes reconstruct **byte-exact** from git (`6614a2e` -> `e9a22a91`,
> `da873a1` -> `c8d6d0e2`, 129 files each). `da873a1` changed **exactly one file**,
> `experiments/_lib/consolidation_lesion_harness.py` — superficially worst-case, since it rewrites the
> REM readout that carries the finding. But the driver binds it at **module scope**
> (`v3_exq_sd068_consolidation_staging_power_diagnostic.py:72`,
> `from experiments._lib import consolidation_lesion_harness as H`) **before** the seed loop, and
> CPython caches modules in `sys.modules` at first import. No `importlib` / `reload(` / `__import__`
> anywhere in driver or harness; the harness's one deferred import is in `ree_core`, which `da873a1`
> did not touch. **All 8 seeds executed the `6614a2e` harness.** The topology is single-process: the
> split is a contiguous prefix, one monotone transition, each seed present exactly once, in one
> coherent 418s window — a restart would have re-run seed 42 on the new substrate, and did not. The
> timing agrees: `da873a1` landed ~85s into a 418s run at ~52s/seed, i.e. exactly the observed
> boundary. `supports` on SD-068 **stands**; recommended `epistemic_category:
> `instrument_repair_validated`.
>
> Second, independent limb: even had the change reached execution, the variability **does not
> partition** along the boundary — the 6-seed homogeneous partition alone reproduces the entire
> reported spread (its REM sd 0.435 **exceeds** the pooled 0.396, and its tolerance range contains the
> 2-seed partition's). The finding is *strengthened*, not undermined.
>
> **Factual correction to the section below.** It describes "a live directional verdict across four
> claims". The manifest's `evidence_direction_per_claim` carries `supports` on **SD-068 only**;
> **MECH-168, MECH-169 and INV-047 are all `unknown`**. The run-level `evidence_direction: supports`
> is what the sweep read, and it over-states per-claim exposure by a factor of four. Any future
> severity ranking must read `evidence_direction_per_claim`, not the run-level roll-up.
>
> The autopsy's own load-bearing output is a **different** defect this investigation exposed: the
> fingerprint stamped 6 cells with code they never executed — a **false-HIT channel in arm-reuse**,
> since all 8 cells carried `reuse_eligible: true`. That is now fixed upstream
> (`resolve_substrate_identity`, `arm_fingerprint.py`, "executed-substrate fix, 2026-07-20").

`evidence_direction: **supports**` SD-068 / MECH-168 / MECH-169 / INV-047 (**per-claim: `supports` on SD-068 only; the other three `unknown`**) · PASS · `ree-worker-1` · **2 substrates**

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

> **Closed 2026-07-20 — REFUTED at rung (b).** Both `V3-EXQ-784`'s driver and every other in the
> corpus are single-process with module-scope import binding and no dynamic imports, so the eight
> substrates on disk correspond to **one** executed build. The "seed 11 spans four different
> substrates" structure is real as a stamping artefact and inert as a confound. The `claim_ids: null`
> caveat is unchanged and still applies for other reasons.

### 5e. V3-EXQ-716a — LESS SEVERE, finding survives on matched seeds

`evidence_direction: **supports**` SD-063 · PASS · `ree-cloud-2` · **2 substrates** (seeds 42, 43 | seed 44)

All three load-bearing criteria (`C1_crps_quantile_beats_point`, `C2_precision_error_corr_over_ema_null`,
`C3_sd031_agency_residual_preserved`) won on **3 of 3 seeds** against a pre-registered
`majority_needed: 2`. The divergent seed is 44; **seeds 42 and 43 are mutually substrate-matched and
by themselves satisfy the pre-registered majority on all three criteria.** Each criterion is also an
internal per-seed comparison, so nothing contrasts across the boundary. **No action owed** — the
verdict stands on a substrate-homogeneous subset that independently clears the bar.

> **Strengthened 2026-07-20 — now REFUTED outright at rung (b), not merely survived at rung (d).**
> 716a's driver is single-process with module-scope binding and no dynamic imports, so seed 44 ran
> the same executed build as seeds 42 and 43. The finding no longer needs the matched-subset
> argument, though that argument remains valid. `supports` SD-063 stands. This is the one sec-5 entry
> whose original disposition was already correct; the ladder only makes it unconditional.

### 5f. V3-EXQ-689d — already routed

`supports` MECH-448 · the origin case. Autopsy complete
(`failure_autopsy_V3-EXQ-689d_2026-07-20`); D3 is recorded there as
`sufficient_alone_to_withdraw: true`.

> **Re-adjudicated 2026-07-20 — D3 REFUTED and WITHDRAWN.** See
> [`failure_autopsy_V3-EXQ-689d-D3_2026-07-20.md`](failure_autopsy_V3-EXQ-689d-D3_2026-07-20.md),
> which supersedes the D3 defect only. Rung (a) does **not** clear it — `ree_core/agent.py` (+95) and
> `ree_core/utils/config.py` (+33) genuinely changed between the bands (`f53c28123eff` ->
> `c15f84ee494f`) and both are on the executed closure. **Rung (b) clears it decisively**: the driver
> binds `REEAgent` at `:128` and `REEConfig` at `:130`, **937 lines before** the arm loop opens at
> `:1065`, in a single process with no dynamic imports. All 12 cells executed the `19b4073c`
> substrate. `sufficient_alone_to_withdraw` becomes **false**.
>
> **689d's conclusion is unaffected.** D1 (`hold_weighted_dv`, DISQUALIFYING) and D2
> (`vacuous_matched_noise_control`) stand independently, and D2 was re-verified here: 26 of 27 fields
> bit-identical between `ARM_PROPOSER_CTRL` and `ARM_MATCHED_NOISE` on all three seeds, differing
> only in the inert `temperature` knob, with identical `n_p1_ticks` (387/3616/224) — identical
> trajectories, i.e. the same arm. The withdrawal of `C_PRIMARY` stands on D1+D2; only the "zero
> validly-controlled surviving seeds" *formulation* is lost. **Cite D1+D2, not D3.**
>
> Consequence for this document: **D3's class-origin case is withdrawn.** The defect class was
> generalised from a run where it did not in fact occur.

## 6. Cross-reference with the hold-weighted E3 sweep

Runs hit by **both** defects are priority re-adjudication candidates. Against the ~30 runs verified
in depth in the companion document, the intersection is **three**:

- **V3-EXQ-689d** — both defects, already routed. ~~D3 alone forces withdrawal.~~ **Corrected
  2026-07-20: D3 is refuted (sec 5f); the withdrawal rests on the hold-weighted DV and the vacuous
  matched-noise control.** The companion sweep's defect is the one that survives on this run.
- **V3-EXQ-689e** — companion verdict "verified SAFE"; divergent here but `non_contributory`. No action.
- **V3-EXQ-662** — `non_contributory`, so no direct exposure, **but worth one line**: 662/663 is the
  driver whose matched replay *calibrated* the hold-weighting cost at −0.87%…+0.64%. The calibration
  instrument is itself intra-run divergent (2 substrates, `n_files` 97→98). That does not invalidate
  the calibration — it was a matched replay on a fixed checkout, not a re-use of the original cells —
  but the original 662 manifest should not be treated as a clean reference run.

**This intersection is a lower bound**, not a complete join: the companion sweep names ~30 of its 150
fires explicitly, and the full fire list was not re-derived here.

## 7. Recommended routing — **ALL ITEMS CLOSED, 2026-07-20**

Items 1-3 were routed, adjudicated, and **all three refuted**. Item 4 is closed by the corpus pass.
The live recommendations that remain are governance items, listed after the closed table.

| was | now |
|---|---|
| 1. `/failure-autopsy` **V3-EXQ-782** | **DONE — REFUTED** (rung a). `weakens` MECH-459 stands. `governance-affirm`. |
| 2. `/failure-autopsy` **V3-EXQ-604c** | **DONE — D3 EXONERATED** (rung c). But a *larger* defect was upheld: see below. |
| 3. `/failure-autopsy` **V3-EXQ-778a** | **DONE — REFUTED** (rung b). `supports` SD-068 stands. |
| 4. **V3-EXQ-784** flagged, not routed | **CLOSED — REFUTED** (rung b), single process, module-scope binding. `claim_ids` still null, so it weights no claim regardless. |
| 5. the 36 non-directional hits | **CLOSED — all triaged** under the sec-3a ladder (sec 3a-summary). None survives. The former instruction to "triage against sec 4 first" on promotion is superseded: triage against **sec 3a** first. |

**Live recommendations for `/governance`** (this document changes no registry; `claims.yaml`,
`review_tracker.json` and `substrate_queue.json` are untouched):

1. **MECH-314b, MECH-314c, Q-044: `mixed` -> `non_contributory`** under `epistemic_category:
   substrate_ceiling` — from the 604c autopsy, and **unrelated to D3**. C2 is structurally vacuous
   for these three: Phase-1 uncertainty and learning-progress are global scalars broadcast across all
   K candidates, and a uniform additive constant cannot change an argmax, so `delta == 0.0` was an
   arithmetic identity fixed before the run. MECH-314 and MECH-314a `supports` **stand**. The
   re-derive brake **fires** (3 vs threshold 2) and a further same-claim ablation is **REFUSED**;
   the build route is to make both terms per-candidate (`amend` on ARC-065).
2. **MECH-459, SD-068, MECH-448, SD-063: no change.** All four readings stand; the D3 hits recorded
   against 782, 778a, 689d and 716a are withdrawn.
3. **Withdraw the D3 defect from V3-EXQ-689d** per
   [`failure_autopsy_V3-EXQ-689d-D3_2026-07-20`](failure_autopsy_V3-EXQ-689d-D3_2026-07-20.md).
   689d's overall withdrawal of `C_PRIMARY` **stands unchanged** on D1 + D2 — D2 was independently
   re-verified (26 of 27 fields bit-identical between `ARM_PROPOSER_CTRL` and `ARM_MATCHED_NOISE`,
   identical tick counts on all three seeds). Reading and category retained, so per R1-R3 shape (c)
   the re-adjudication **supersedes** rather than adds: MECH-448 stays **0**.
4. **Add `evidence_quality_note` addenda** to 782, 604c, 778a, 689d and 716a recording that the
   intra-run substrate-divergence hit against each is **withdrawn**, so the flag does not resurface
   as unexplained doubt in a later sweep.
5. **Prefer the new `inert_arm_knob` lint over a whole-glob divergence lint** — see sec 8(a)
   correction.

**No manifest was edited.** Completed runs are re-adjudicated via `/failure-autopsy`, never
rewritten. This document records findings only.

## 8. Recommendations (proposed, not implemented)

> **Correction (2026-07-20) to (a): a whole-glob check is the WRONG shape and should not be built.**
> With a defect base rate of 0 of 42 (sec 3a-summary), a lint that fires on whole-glob hash
> divergence would have fired **42 times with 42 false positives** — it would institutionalise this
> sweep's own error as a standing warning, and warnings that are almost always wrong get ignored,
> taking the real case with them. If a divergence check is built, it must be **closure-restricted**
> (rung a) and should additionally suppress on the single-process/module-scope-binding condition
> (rung b). Two cheaper and higher-yield alternatives, in priority order:
> 1. **`inert_arm_knob`** (from 689d's D2, the defect that actually survived): compare every pair of
>    arms declared distinct; WARN if bit-identical on all recorded per-cell fields except the knob
>    naming their difference. Manifest-local, no substrate dependency, and it catches a defect class
>    that *silently degrades conjunctive acceptance criteria*.
> 2. **The executed-substrate stamp**, which has **already landed** — `resolve_substrate_identity()`
>    in `arm_fingerprint.py` ("executed-substrate fix, 2026-07-20") resolves substrate identity once
>    per process, so cells are stamped with the code they *executed* rather than whatever is on disk
>    when the cell finishes. That closes the false-HIT arm-reuse channel 778a exposed, and it removes
>    the generating cause of this entire hit set going forward.
>
> Sec 8(b) — per-cell stamping — is **unaffected and stands**; it is what made every adjudication in
> this document possible.

**(a) A lint / `manifest_core` assertion that a run's cells share one `substrate_hash`.**
~~Recommended~~ **superseded — see the correction box above**, with one design caution. The natural home is `manifest_core.py:117`
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
- ~~**6 of 42 hits were triaged in depth** (sec 5) ... The other 36 are enumerated but **not
  adjudicated**~~ — **superseded 2026-07-20: all 42 have now been triaged** under the sec-3a ladder
  and none survives (sec 3a-summary).
- **The scan detects divergence, never its content.** Two hashes tell you the code changed, not what
  changed or whether the change could affect the DV. ~~A hit is a **loss of experimental control**~~
  — **corrected: a hit is NOT a loss of experimental control.** It is a hash change, which is a
  *weak* proxy for a change in executed code, because (i) the glob is deliberately over-inclusive of
  the executed closure and (ii) a single-process run freezes its import graph at first use. On this
  corpus the proxy was wrong **42 times out of 42**. Treat a hit as a prompt to run the ladder, never
  as a finding in itself.
- **The corpus is uniformly single-process, and that is load-bearing.** Across all 30 examinable
  drivers: zero process-spawning constructs, zero dynamic imports, zero function-scope `ree_core` /
  `experiments` imports. If that ever changes — a subprocess-per-cell runner, or an arm-conditional
  lazy import — rung (b) stops clearing and this defect class becomes live. **The class is retained
  as a check, not retired.**
- **Nine hits are refuted on topology alone** (dirty tree, so attribution is `unverifiable`). That is
  the weakest limb of the corpus result. It is not weak in the one case where it could be
  cross-checked: `604c` is independently refuted at rung (c) by empirical bit-identity, which needs
  no attribution at all.
- **The intersection with the hold-weighted sweep (sec 6) is a lower bound** — matched against that
  document's ~30 verified runs, not its full 150-fire list.
- **`substrate_n_files` deltas under-report file edits**: a modified-in-place file changes the hash
  without changing the count, so 19 of 42 is a floor on how many runs saw structural change.

## 10. A discovery gap this document CANNOT fix by being written in

> **Recorded 2026-07-20T10:15Z** (session `musing-einstein-c80816`). This section is a **record of a
> defect in the governance cycle**, not a mechanism. Writing a recommendation down — here or
> anywhere else off the cycle's input list — does **not** cause it to be applied. That claim is not
> a prediction; it is the observed behaviour of this very document, three times over.

**The gap.** `/governance` discovers autopsy recommendations by walking
`evidence/experiments/pending_review.md` and then, for each surfaced `run_id`, looking up a confirmed
`failure_autopsy_*.json` and reading its `recommended_evidence_direction` /
`recommended_epistemic_category` / `recommended_substrate_queue_entry` (governance SKILL.md Step 2
item 5). A run that is already in `review_tracker.json:reviewed_run_ids` is **absent from
`pending_review.md`**, so that lookup never runs for it.

**Therefore: a re-adjudication landing against an ALREADY-REVIEWED run is structurally invisible to
governance.** The cycle assumes adjudication precedes review. That assumption is false for the entire
class of work this document represents — a corpus sweep re-opens completed, reviewed runs by
construction.

**Confirmed instance.** `failure_autopsy_V3-EXQ-604c_2026-07-20` is `confirmed` and recommends
demoting **MECH-314b, MECH-314c and Q-044** (`mixed` -> `non_contributory` under `substrate_ceiling`,
on structural vacuity — see sec 5b and sec 7). Its run
`v3_exq_604c_q044_mech314_subflavour_ablation_gapa_ready_20260607T193029Z_v3` is in
`reviewed_run_ids` and returns **0 hits** in `pending_review.md`. As of 2026-07-20T10:15Z the
demotion is **still unapplied**: MECH-314b/314c remain `candidate_substrate_landed` and Q-044 remains
`status: open` with `live_status.evidence` still citing the **superseded** predecessor autopsy
`failure_autopsy_gapA-cluster-604b-648a-649_2026-06-07#V3-EXQ-604b`.

It has now survived **three** independent attempts to route it: two `spawn_task` chips (neither
produced a worktree or a claim) and one completed 604c application pass that landed the
`substrate_queue` entry but never reached the claim layer. Three failures with three different
proximate causes is the signature of a **structural** gap, not of three unlucky sessions.

**Why this document is not the fix.** `/governance`'s inputs are `claims.yaml`,
`hypothesis_space_integrity.md`, `pending_review.md`, `promotion_demotion_recommendations.md`,
`review_tracker.json`, `experiment_proposals.v1.json`, `convergence_demand_queue.v1.json`,
`closure_drift.md`, `substrate_queue.json`, `substrate_dependencies.json`. **This sweep is on none of
them**, and neither is the IGW workset (a downstream *consumer*: governance -> `substrate_queue` ->
workset). Sec 7's "Live recommendations for `/governance`" has been landed on `origin/master` since
2026-07-20T07:51Z and was **not** picked up — which is the direct evidence that documenting a
recommendation does not surface it.

**A second-order harm, already present.** Stale text keeps asserting the pre-autopsy reading.
`inter_governance_workset.md` `IGW-20260720-020` still says *"Q-044/MECH-314-family leg is satisfied
by V3-EXQ-604c PASS on validated GAP-A"*. Post-autopsy that is wrong in the consequential direction:
C2 was **structurally vacuous** for 314b/314c, so the leg was never tested, and a planner reading
that line concludes a closed question that is in fact open. **An unapplied demotion does not stay
neutral — it decays into a positive claim.**

**The fix (proposed, not implemented — chipped).** A **generic re-surfacing rule**: scan
`evidence/planning/failure_autopsy_*.json` for `confirmed` artifacts whose `recommended_*` fields are
not yet reflected in `claims.yaml`, and surface that set **independently of review status**. Emit it
into `promotion_demotion_recommendations.md`, which is already a governance input and already
generated by `scripts/governance.sh` — so the change belongs in the generator, not in any hand-written
file. Two narrower alternatives were considered and are **worse**: un-reviewing 604c in
`review_tracker.json` fixes one item and asserts something false (the run *was* reviewed), and
hand-writing into `promotion_demotion_recommendations.md` is overwritten on the next regeneration.

**Until that lands, the only reliable route is to NAME these items explicitly when starting a
`/governance` run.** They will not be raised for you.
