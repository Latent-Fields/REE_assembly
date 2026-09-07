# ao-decoder proposal-centroid readout: injection contamination -- affected-manifest audit

- **Written:** 2026-09-07T17:22:12Z
- **Session:** `hopeful-solomon-01a60c` (chip `chip-20260907-ao-decoder-stats-injection-contamination-v2`)
- **Substrate fix landed alongside this note:** `ree-v3/ree_core/hippocampal/module.py`
- **Status: LIST ONLY -- NOT adjudicated.** Re-adjudicating these runs is `/failure-autopsy`
  and `/governance` work. This note produces the list and routes it; it deliberately draws
  no verdict on any run.

---

## 1. The contamination, restated

`_inject_support_preserving_candidates` (`module.py`) splices synthetic scaffold
trajectories -- one one-hot action step followed by **exact zeros** -- into the candidate
pool *after* `all_trajectories` is bound and *before* `final_summary` is computed.
`action_object_decoder_raw_output_stats` is derived from that final pool, so every injected
row enters the statistic.

Three properties make this more than a rounding concern:

1. **Magnitude.** Each injected row drags one action dimension's mean by roughly
   `1 / (num_candidates * horizon)`. For a 16-candidate, 4-step pool that is ~0.0156 --
   an order of magnitude above the centroid displacements some drivers read as their DV.
2. **Not arm-independent.** Firing is conditional on the final pool's first-action class
   count. For any design whose arms change elite selection, the injector can fire
   asymmetrically between two arms of a matched pair and **manufacture an apparent
   displacement**.
3. **It replaces real candidates, not merely adds.** `keep_n = total_budget - len(injected)`,
   so an asymmetric firing also changes *which real candidates survive* -- the contamination
   is not confined to the synthetic rows themselves.

The V3-EXQ-1005 red-team record dismissed the injection as "deterministic and
arm-independent". That is correct for 1005's own arms and **does not transfer**.

## 2. Two refinements found during this audit

**(a) The consuming lineage reads `std_by_action_dim`, not `mean_by_action_dim`.**
The chip framed the DV as a centroid (mean). In fact every *recorded* consumer reads the
**spread**. The contamination applies at least as strongly there: a one-hot-then-zeros row
sits far outside the real candidates' distribution, so injection **inflates** the std. The
affected-run list below is therefore driven by `std_by_action_dim` consumption, and the
chip's mean-centred framing under-stated rather than over-stated the exposure.

**(b) `action_class_scaffold` is the same synthetic construct under a different tag.**
`_build_action_class_scaffold_candidates` produces identical one-hot-then-zeros rows, tagged
`action_class_scaffold` instead of `support_preserving_cem_injected`, and **24 experiment
drivers** set `use_action_class_scaffold_candidates`. A readout excluding only the injected
tag is still contaminated whenever that flag is on. The substrate fix therefore emits two
companions rather than one (see section 4).

## 3. Affected recorded runs

Consumers of `action_object_decoder_raw_output_stats` in `ree-v3/experiments/` (excluding
`_scratch/`), and their recorded manifests in `REE_assembly/evidence/experiments/`:

| Run | Manifest | Field read | SP-CEM setting | Injection eligible? |
|---|---|---|---|---|
| V3-EXQ-869 | `v3_exq_869_mech267_mode_conditioning_content_persistence_20260802T035422Z_v3.json` | `std_by_action_dim` | not set -> **default ON** | yes |
| V3-EXQ-869a | `v3_exq_869a_mech267_mode_conditioning_content_persistence_retest_20260802T195943Z_v3.json` | `std_by_action_dim` | not set -> **default ON** | yes |
| V3-EXQ-923 | `v3_exq_923_mech267_gov_fanout1_h1_iteration_count_20260812T045513Z_v3.json` | `std_by_action_dim` | not set -> **default ON** | yes |
| V3-EXQ-927 | `v3_exq_927_mech267_cem_selection_fix_validation_20260814T012404Z_v3.json` | `std_by_action_dim` | not set -> **default ON** | yes |
| V3-EXQ-928 | `v3_exq_928_mech267_cem_selection_fix_validation_20260814T013434Z_v3.json` | `std_by_action_dim` | not set -> **default ON** | yes |

All five are **MECH-267 lineage**. Each has both a flat manifest and a
`runs/<run_id>/manifest.json` pack.

Not in the table, and why:
- **V3-EXQ-1005** -- the consuming script lives in `experiments/_scratch/`; no recorded
  manifest in the evidence tree.
- **V3-EXQ-1009** -- queued, not yet run. Its driver already handles this contamination
  **locally**, filtering by source tag in its own `_propose`, and records
  `mean_by_action_dim_substrate_incl_injected` alongside the filtered value. It is the
  worked reference for the substrate fix, not an affected run.

### 3a. The runs cannot be self-audited for whether injection actually FIRED

`use_support_preserving_cem` has been the main-path **default `True`** since 2026-05-17
(ARC-065, `cb1c6da`), and none of the five drivers sets the legacy opt-out. So injection was
**eligible** in every one of them.

Whether it *fired* is a different question, and **none of the five manifests records it**:
`support_preserving_injected_candidates` and `support_preserving_active` are absent from all
four grep-visible manifest files. The diagnostic exists at the top level of the propose
diagnostics at runtime -- the drivers simply never persisted it.

**Consequence for whoever adjudicates these:** "eligible" is the strongest statement the
recorded evidence supports. Establishing fired-vs-not-fired requires a re-run, not a
re-read. That is a genuine limit on what a desk review of these five can conclude.

### 3b. An injection-free readout already existed per-CEM-iteration -- but none of the five recorded it

`cem_iteration_diagnostics[i]["action_object_decoder_raw_output_stats"]` is computed from
`decoded_summary` **inside** the CEM loop, which completes *before*
`_inject_support_preserving_candidates` is called. That per-iteration copy has therefore
always been injection-free.

It is not a rescue for these five runs: **none of the five manifests records
`cem_iteration_diagnostics` at all.** But it is worth knowing for two reasons -- it is a
second uncontaminated readout a future driver can persist cheaply, and it means the
contamination was confined to the final-pool summary rather than being pervasive in the
diagnostics.

## 4. What landed in the substrate (for the adjudicator's reference)

Additive only -- `action_object_decoder_raw_output_stats` keeps its exact meaning, because
landed manifests depend on it. New top-level keys in the propose diagnostics:

- `action_object_decoder_raw_output_stats_excluding_injected` -- same statistic over the pool
  with `support_preserving_cem_injected` rows removed. Differs from the headline field
  **exactly when** `support_preserving_injected_candidates > 0`.
- `action_object_decoder_raw_output_stats_excluding_synthetic` -- also removes
  `action_class_scaffold`. **This is the field to read when
  `use_action_class_scaffold_candidates` may be on**; `_excluding_injected` does not filter
  that source.
- `candidate_samples_excluding_injected` / `candidate_samples_excluding_synthetic` --
  denominators, so a consumer need not recount.

`support_preserving_injected_candidates` was already top-level reachable (spread via
`**support_preserving_diag`) and needed no change; chip item 2 was already satisfied.

Contract: `ree-v3/tests/contracts/test_ao_decoder_injection_free_stats.py` (8 tests). All
assertions are on continuous statistics, metadata tags, or counts from the returned pool --
never an exact committed action sequence, per the cross-machine-class `torch.multinomial`
divergence. Fault-injection checked: neutralising the exclusion filter turns 5 of the 8 red,
so the oracle is not vacuous.

## 5. Routing

- **Owed to `/failure-autopsy` / `/governance`:** decide whether any of the five recorded
  MECH-267 runs needs its `evidence_direction` revisited, given (a) the DV read a
  contaminated spread statistic and (b) fired-vs-not-fired is unrecoverable from the
  manifests.
- **Owed to future drivers in this lineage:** read `_excluding_synthetic` (or
  `_excluding_injected` when the scaffold is provably off) and **persist
  `support_preserving_injected_candidates` into the manifest**, so the next audit of this
  kind is a re-read rather than a re-run.
