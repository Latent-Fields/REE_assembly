# Failure autopsy — V3-EXQ-782 (re-adjudication for intra-run substrate divergence, D3)

**Generated** 2026-07-20T06:44:10Z · **Session** `stoic-wescoff-cac81f`
**Target** `v3_exq_782_mech459_advantage_composition_probe_20260718T111818Z_v3` · `V3-EXQ-782` · `MECH-459`
**Scope** single · **Status** confirmed (user-adjudicated at the Step 8 gate)

**Trigger** [`intra_run_substrate_divergence_sweep_2026-07-20.md`](intra_run_substrate_divergence_sweep_2026-07-20.md)
sec 5a — routed as *"SEVERE, highest structural severity in the corpus"*, defect class D3.
**Origin of the class** [`failure_autopsy_V3-EXQ-689d_2026-07-20.md`](failure_autopsy_V3-EXQ-689d_2026-07-20.md)
sec 4, `targets[0].defects[2]`.

**Prior adjudication (affirmed, not superseded on the merits)**
[`failure_autopsy_MECH-457-gov-fanout-1-cluster-780-781-782_2026-07-18.json`](failure_autopsy_MECH-457-gov-fanout-1-cluster-780-781-782_2026-07-18.json).

> **One line.** The D3 hit on V3-EXQ-782 is a **FALSE POSITIVE**. All four `substrate_hash` values
> reconstruct from clean committed trees, but the fingerprint's globs are **wider than the code 782
> executes**: the closure-restricted fingerprint is byte-identical (`3b33ab7f515e21ac...`) across all
> four bands, and the three files that moved are on no import path of this run. Independently, the
> load-bearing verdict is a **within-cell** quantity that replicates on all 6 probe cells across all
> 4 builds at >=2.07x margin. **`evidence_direction: weakens` on MECH-459 STANDS, unchanged.**
> The sweep's method carries an unruled-out false-positive channel that also bears on its two other
> SEVERE routings (604c, 778a) — routed onward, see sec 7.

---

## 1. Facts reconstructed

`FAIL` · `experiment_purpose: diagnostic` · `ree-worker-1` · `linux-x86_64-py3.10` · 10831.7 s
· seeds 42/43/44 · `non_degenerate: true` · `recording_schema: rec/v1`.

The always-core recording set is **complete** — `recording_schema`, top-level `substrate_hash`,
`machine`, `machine_class`, `elapsed_seconds`, full `config`, explicit `seeds`. No recording gap.
(Note the top-level `substrate_hash` is the first-arm hoist from
`manifest_core.py:117 _hoist_multi_arm_substrate_hash()` and is therefore *not* evidence of
homogeneity — the sweep is right about that in general; it is simply not load-bearing here.)

Self-route: `forage_mass_already_concentrated__critic_flat_uninformed`.
Criteria: `R_a_forage_adv_mass_parity_rescaled_post_standardisation` (**load_bearing**) FAILED;
`R_b_critic_separates_pre_from_post_reward_states` (load_bearing **false**) FAILED.
Failed criterion class: **absolute** (a pre-declared conditional on an intermediate quantity, not a
discrimination between arms — there is no treatment arm by design, per Decision 2b).

All four readiness preconditions met: `local_view_greedy` 48.05 and `greedy_oracle` 57.2 against the
1.0 competence floor; 273 forage-contact steps against a 30 floor; demonstrator return std 0.302689
against a 0.25 floor.

### The divergence, as reported

| substrate | `n_files` | cells |
|---|---|---|
| `098473b9` | 131 | `local_view_greedy` 42/43/44, `greedy_oracle` 42/43/44, `random_walk` 42/43/44, `probeR_ctrl_zworld` **42** |
| `765ce9d2` | 132 | `probeR_ctrl_zworld` **43** |
| `a652aa3d` | 133 | `probeR_ctrl_zworld` **44**, `probeR_ctrl_raw` 42/43 |
| `7f856703` | 133 | `probeR_ctrl_raw` **44** |

`driver_script_hash` (`af4a62f9`) and `machine_class` constant across all 15 cells.

---

## 2. Line 1 — the divergence does not touch the executed code

### 2a. All four hashes are clean committed trees

Recomputing the `arm_fingerprint` byte protocol (`arm_fingerprint.py:222-225`: sorted repo-relative
path + `\0` + per-file sha256 hex + `\n`) over every `ree-v3` tree in the window reproduces all four
values **exactly**. No dirty-tree edit is implicated:

| hash | `n_files` | tree band (committer dates UTC) |
|---|---|---|
| `098473b9` | 131 | `16fd4eff7d19` 08:16:27Z .. `375476e35c88` 09:30:46Z |
| `765ce9d2` | 132 | `8b467007c22f` 09:54:26Z .. `ff7b8ca9775e` 10:40:41Z |
| `a652aa3d` | 133 | `f418400f4583` 10:46:06Z .. `4607c4133940` 10:52:34Z |
| `7f856703` | 133 | `8b183383dfc9` 10:57:13Z .. `18e8336067d0` 11:10:09Z |

The run *started* at 11:18:18Z — after all four trees already existed. The hub's checkout was lagging
and pulled forward through them mid-run. (It skipped the intermediate tree `3d4dd77e`, so band A->B
spans two commits' worth of change.)

### 2b. Exactly three files moved, and none is on 782's import path

| band | change |
|---|---|
| A -> B | **+** `experiments/_lib/baselines/exq783_zworld_granularity.py` (new); `experiments/_lib/consolidation_lesion_harness.py` +269 |
| B -> C | **+** `ree_core/latent/zworld_p0.py` (new, 539 lines); `exq783_zworld_granularity.py` 36 lines changed |
| C -> D | `experiments/_lib/consolidation_lesion_harness.py` +191/-13 |

Transitive static import closure of
[`v3_exq_782_mech459_advantage_composition_probe.py`](../../../ree-v3/experiments/v3_exq_782_mech459_advantage_composition_probe.py)
(driver lines 196-208; `mech459_probe_r.py:70-72`) = **110 files**, of which **103** are globbed.
None of the three changed files is in it:

- `ree_core/latent/zworld_p0.py` — referenced repo-wide only by
  `v3_exq_783_zworld_granularity_training_crossing.py:177` and `tests/contracts/test_sd070_zworld_p0.py:17`.
  `ree_core/latent/__init__.py` is the **empty blob** (`e69de29bb2`) in all four trees, so there is
  no package-import side channel.
- `experiments/_lib/baselines/exq783_zworld_granularity.py` — referenced only by `v3_exq_783_...:174`.
- `experiments/_lib/consolidation_lesion_harness.py` — referenced only by the seven `v3_exq_sd068_*`
  drivers and three SD-068 contract tests.

### 2c. The closure-restricted fingerprint is identical — the decisive check

Recomputing the same byte protocol restricted to the 103 globbed closure files, with the closure
derived **per tree** (not imported from the tip), at a representative commit in each band:

| band | commit | globbed closure | closure-restricted FP |
|---|---|---|---|
| `098473b9` | `375476e35c88` | 103 | `3b33ab7f515e21ac...` |
| `765ce9d2` | `ff7b8ca9775e` | 103 | `3b33ab7f515e21ac...` |
| `a652aa3d` | `4607c4133940` | 103 | `3b33ab7f515e21ac...` |
| `7f856703` | `18e8336067d0` | 103 | `3b33ab7f515e21ac...` |

Full digest `3b33ab7f515e21aca40eae800273fd61698c3fd53f1c55e2bbd6c76f3daa6c41`. The closure **file
set** is identical too, so this is not one file dropping out as another appears — every one of the
103 has the same blob OID across all four trees.

Corroborating, on the three modules that carry the instrumentation and the mechanism under test —
single blob OID each across all four trees:

| module | OID |
|---|---|
| `experiments/_lib/mech457_explorer_classes.py` (normaliser under test, `:688`/`:697`) | `c2bf26f8a030` |
| `experiments/_lib/mech457_bootstrap_explorer.py` | `5fc49688123b` |
| `experiments/_lib/mech459_probe_r.py` | `641cc3c730e4` |

A dynamic-import scan over the closure returns **zero** hits for `importlib`, `__import__`, `exec(`,
`pkgutil`, `entry_points` (the 23 `eval(` matches are all substring false positives — `harm_eval(`,
`policy_net.eval()`, `def run_eval(`). So the static closure is not an under-approximation.

**The code V3-EXQ-782 executed was byte-identical in all 15 cells.**

---

## 3. Line 2 — independently, the verdict is within-cell and replicates on every build

`_classify_composition(c_pre, c_post)` (driver `:337-342`) routes first on `c_pre >= CONC_TINY_PRE`
(0.5). `C_pre = f_pre / s` is computed **inside a single cell's** late measurement window
(`_forage_conc`, `:328-334`). The load-bearing criterion is `passed = any_parity` (`:575-576`) — an
**OR across representations of a within-representation classification**, not a difference between
them. So no comparison in R-(a) crosses a cell, an arm, or a substrate boundary.

The sweep's framing — *"the headline is a z_world vs raw_view per-representation contrast ... that
contrast is wholly cross-substrate"* — does not match the criterion's construction. Both
representations return the **same** verdict independently; the headline reports them side by side
rather than contrasting them.

And every individual cell clears the threshold, so the verdict is invariant to pooling seeds that
sit on different builds:

| substrate | cell | `C_pre` | margin vs 0.5 | verdict |
|---|---|---|---|---|
| `098473b9` | zworld s42 | 1.641 | 3.28x | already_concentrated |
| `765ce9d2` | zworld s43 | 1.654 | 3.31x | already_concentrated |
| `a652aa3d` | zworld s44 | 2.458 | 4.92x | already_concentrated |
| `a652aa3d` | raw s42 | 1.317 | 2.63x | already_concentrated |
| `a652aa3d` | raw s43 | 1.257 | 2.51x | already_concentrated |
| `7f856703` | raw s44 | 1.035 | **2.07x** (min) | already_concentrated |

All four builds carry at least one probe cell, and each independently yields the verdict. Given
sec 2c the four builds are the *same* executed code, so this is not a true replication across
substrates — but it does mean that **even under the sweep's own (incorrect) assumption that the
builds differed, the finding would survive**, because a substrate-homogeneous per-cell read returns
the identical verdict on every partition. The finding is robust to the defect on two independent
grounds.

The non-load-bearing R-(b) reading is equally margin-safe per cell: `std(V)/std(G)` 0.041 (z_world)
/ 0.065 (raw) against a 0.25 collapse threshold, separation ratios 0.016 / 0.014 against a 0.25
floor. The sweep flagged `separation_ratio_per_seed [0.000251, 0.032429, 0.015187]` as confounded
with build identity; all three are an order of magnitude below the floor, and per sec 2c the build
identity is not a code difference.

### One residual observation, recorded and not routed

The `demo_state_return_spread_supra_floor` precondition is a **min over cells** = 0.302689, sourced
from `raw_view` seed 44 — the singleton cell on `7f856703` — clearing its 0.25 floor by only 1.21x,
against `return_std` of 31.95 and 42.15 on raw seeds 42/43 (a ~100x spread). This is the one place
in the run where the divergence would have had any bite. It does not: the C->D change is
`consolidation_lesion_harness.py`, definitively off-path, so the anomaly is not substrate-caused —
raw seed 44 also differs behaviourally (`n_forage_steps` 4928, step fraction 0.161 vs 2095/736 and
0.085/0.048), which is the more likely account. It gates only R-(b), which is declared
`load_bearing: false`. **Recorded for the record; no routing owed.**

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **weakened (weak form only)** — unchanged from the prior autopsy | The weak form's PREMISE fails, not its consequent: `C_pre` 1.92 (z_world) / 1.20 (raw) against the 0.5 "tiny" threshold, so forage-contact steps already carry disproportionate `abs(adv)` mass BEFORE the standardiser. No tiny forage signal exists for novelty noise to swamp. The STRONG form is not restated — already refuted by Finding V2 of the sanctioning decision. |
| Biological reference | partial | Formal/algorithmic import (DreamerV3, Hafner 2023 App. E), not a biological translation. Critic half has a dopaminergic-RPE analogue; normaliser half does not. Lit present on the claim — no `/lit-pull` owed. |
| Prerequisites | present | All four readiness preconditions met with margin. |
| Implementation completeness | complete | Instrumentation mirror module; live 780/781 scripts and `mech457_*` `_lib` modules byte-unchanged — now **independently verified by blob OID across all four trees** (sec 2c). |
| Environment adequacy | adequate | Same CausalGridWorld D3 configuration as the portfolio it instruments. |
| Measurement adequacy | adequate and decisive on R-(a) | Measured exactly the intermediate quantity no manifest records, so correctly run rather than reanalysed (GOV-REUSE-1). |
| Integration adequacy | coupled | CTRL arms behaviourally equivalent to the portfolio's. |
| Scale / capacity | adequate | 3 seeds x 2 representations on the reference 128-wide/3x/detached build. |
| **Experimental control (D3)** | **intact — defect REFUTED** | Four `substrate_hash` values, one executed closure. Closure-restricted FP identical across all four bands; no changed file on the import path; no dynamic-import escape. |

**Recommended `epistemic_category`: `standard`** (unchanged).
**Recommended `evidence_direction`: `weakens`** (unchanged).

**Re-derive brake:** MECH-459 ceiling count **0** under the R1-R3 convention. Does not fire. This
re-adjudication **retains** both direction and category, so per shape (c) of the counting convention
it is one superseding adjudication of the same run, not a second hit — the count stays 0.

---

## 5. Learning extracted

1. **A `substrate_hash` change is not evidence that the executed code changed.** The fingerprint
   globs (`ree_core/**/*.py`, `experiments/_harness.py`, `experiments/_metrics.py`,
   `experiments/_lib/**/*.py` — `arm_fingerprint.py:65-70`) are deliberately over-inclusive, an
   asymmetry the module documents at `:14-17` as "over-inclusion -> false misses only". That
   asymmetry is exactly right for its **designed** purpose (arm-reuse cache validity, where a false
   miss is free). It is **wrong** when the same field is repurposed as a *divergence detector*, where
   over-inclusion converts directly into false positives. The defect is in the reuse, not the field.
2. **The D3 triage test needs a fourth question.** Sec 4 of the sweep asks only *where the split
   falls* relative to the finding. Before that, it must ask **whether the split reflects a change on
   the executed path at all** — recoverable cheaply by recomputing the fingerprint over the driver's
   import closure. On 782 that single question answers the whole autopsy.
3. **The five benign channels the sweep ruled out are all *within-run* variation** (`globs`,
   `scoped`, `machine_class`, `driver_script_in_substrate_hash`, `__pycache__`). The channel that
   actually explains 782 is a *between-run* property of the instrument — the glob's scope relative to
   the closure — which no within-run constancy check can see.
4. **Parallel development in globbed directories is the generating mechanism.** All three moved files
   belong to *other sessions'* work (SD-070 z_world P0, EXQ-783, SD-068). On a heavy-development day
   this fires against every long run on the fleet regardless of what that run touches — which
   predicts that the sweep's "2026-07-18 alone produced 6 divergent runs" clustering is largely an
   artefact of development volume, not of experimental fragility.
5. **The prior 2026-07-18 cluster autopsy's substrate-equivalence reasoning was correct** and is now
   independently verified at blob-OID granularity.

---

## 6. Routing — V3-EXQ-782

**`routing: governance-affirm`** (no re-queue, no substrate entry, no claim change).

- `evidence_direction: weakens` on MECH-459 **stands**, `epistemic_category: standard` **stands**.
- **No manifest edit.** Completed runs are re-adjudicated via autopsy, never rewritten.
- **No re-run.** A confirmatory run would reproduce a result already shown to be substrate-invariant
  on four partitions and executed against byte-identical code.
- **No substrate_queue entry** (`action: none`). The prior autopsy's rationale stands: probe R is a
  diagnostic on intermediate quantities and the sanctioning decision licenses no build.
- **No hypothesis-registry write.** 782 appears in `hypothesis_space_registry.v1.json` only as a
  `fanout_sources` entry on `competence_floor` and as `motivating_evidence` for `H-retention-critic`
  (`hypotheses[12]`, state `alive`). The verdict is unchanged, so no field moves. The R-(b) evidence
  motivating that leg is now substrate-verified, which strengthens it without altering its content
  or state.
- **`pending_retest_after_substrate: false`.**

**Draft `evidence_quality_note` addendum for `/governance`** (append to the existing note, which
stands in full):

> D3 RE-ADJUDICATION 2026-07-20 (`failure_autopsy_V3-EXQ-782_2026-07-20`): the intra-run
> substrate-divergence hit recorded against this run by
> `intra_run_substrate_divergence_sweep_2026-07-20.md` sec 5a is a FALSE POSITIVE and is WITHDRAWN.
> The run's four `arm_fingerprint.substrate_hash` values all reconstruct from clean committed trees,
> but the fingerprint globs (`ree_core/**`, `experiments/_lib/**`) are wider than this run's executed
> code: the fingerprint recomputed over the driver's 103-file globbed import closure is BYTE-IDENTICAL
> (`3b33ab7f515e21ac...`) at every band, every closure file shares one blob OID across all four trees,
> and the three files that did move (`ree_core/latent/zworld_p0.py`,
> `_lib/baselines/exq783_zworld_granularity.py`, `_lib/consolidation_lesion_harness.py`) are imported
> by no module on this run's path, statically or dynamically. `mech457_explorer_classes.py` — which
> carries the normaliser under test at `:688`/`:697` — is a single blob OID throughout. Independently,
> the load-bearing R-(a) criterion routes on a WITHIN-CELL quantity (`C_pre >= 0.5`,
> driver `:337`) OR-ed across representations, not on a cross-representation contrast, and every one
> of the 6 probe cells clears the threshold on its own build at >=2.07x margin (min: raw seed 44,
> `C_pre` 1.035). Experimental control is INTACT; `evidence_direction: weakens` and
> `epistemic_category: standard` stand unchanged.

---

## 7. Secondary routing — the sweep's method (user-confirmed at the Step 8 gate)

**Confirmed route: re-scan the 41 hits with a closure-restricted recomputation FIRST, then fix the
instrument.** Rationale: **V3-EXQ-604c and V3-EXQ-778a are queued for autopsy (sweep sec 7 items 2
and 3) on the same premise that just failed on 782.** Establishing the true base rate is cheap, is
pure analysis over existing artefacts (no compute, no fleet), and re-prioritises those two before
autopsy effort is spent on them.

Node class: **`complex (probe-gated) / puzzle (known rules)`** — the frame is well-posed and the
method is known; a specific fact (how many of the 41 survive a closure-restricted recomputation) is
missing.

Sketch, so the follow-on is self-contained:

1. For each of the 41 genuine hits, resolve the driver from `experiment_type`, build its transitive
   static import closure **per tree**, intersect with `_SUBSTRATE_GLOBS`, recompute the
   `arm_fingerprint` byte protocol per band, and report whether the closure-restricted hash is
   constant.
2. Partition into **true D3** (closure-restricted hash varies — a real loss of control) vs
   **glob-scope false positive** (constant). Re-rank the SEVERE routings on the true set only.
3. Caveat to carry: a hit whose four hashes do **not** all reconstruct from committed trees (782's
   did) needs the dirty-tree case handled explicitly — report it as `unverifiable`, not as clean.

Then, informed by that base rate, the durable instrument fix — which should be **closure-restricted**,
not the whole-glob check proposed in sweep sec 8(a). Emitting `substrate_divergent: true` keyed on
the current whole-tree hash would have fired on 782 and on every other run co-resident with unrelated
parallel development, i.e. it would institutionalise this false positive as a standing warning.
Sweep sec 8(b) — per-cell stamping, "provenance granularity must follow the unit of COMPARISON" —
is **correct and unaffected** by this finding; it is the *scope* of the hashed set, not its
granularity, that failed here. The two recommendations are orthogonal and both survive.

---

## 8. Scope and limits

- This autopsy adjudicates **V3-EXQ-782 only**. The other 41 hits are **not** adjudicated here; the
  finding that 782's hit is a glob-scope artefact is a *reason to check* them, not a demonstration
  that they are clean. Several may be genuine — a modification to an on-path file would be.
- The import closure is **static**. A dynamic-import scan (sec 2c) returned zero constructs on this
  run's closure, so the static trace is sound here; that check must be repeated per run, not assumed.
- Hub-side pull times were inferred from the cell-to-hash assignment, not from the hub's git reflog,
  which was not queried. This affects only the *narrative* of when each tree arrived, not the
  closure-equivalence result, which is tree-to-tree.
- The prior autopsy's substantive scientific adjudication (weak-form premise failure; the R-(b)
  flat-critic reading; the separation of MECH-459's two halves) is **affirmed and not re-derived**
  here. This document adds only the D3 adjudication.
