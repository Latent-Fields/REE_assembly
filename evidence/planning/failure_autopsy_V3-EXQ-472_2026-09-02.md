# Failure autopsy -- V3-EXQ-472 (SD-011)

- **Run:** `v3_exq_472_sd011_platform_stability_pilot_20260421T183651Z_v3`
- **Generated:** 2026-09-02T16:13:52Z -- **status: confirmed** (Step 8 gate held, user present)
- **Manifest status:** `DIAGNOSTIC` - `experiment_purpose: diagnostic` - no self-route, no indexer adjudication flag
- **In scope because:** every `experiment_purpose: diagnostic` result needs a confirmed autopsy, flagged or not
- **Claims:** SD-011 - **Routing:** `governance-reclassify`
- **Red-team (Step 7c):** cross-model, Fable -- **CONTESTED**, two defects upheld and applied
- **Pre-routing checks (Step 7b):** one C2 fire, dismissed with reason (recorded in the JSON)

## 1. The central fact: there is no criterion

`v3_exq_472_sd011_platform_stability_pilot.py:508`:

```python
print(f"verdict: PASS", flush=True)
```

An **unconditional literal print** inside `run_single`, guarded by no `if`, threshold or comparison. `status` and `outcome` in the manifest are the literal string `DIAGNOSTIC`. No comparison operator appears anywhere in the scoring path. The verdict is structurally decoupled from every number the run computes: `recovery_ratio` could be 0.0, 50.0 or NaN and the line would be byte-identical.

The author qualified this in two places -- the driver docstring ("still prints `verdict: PASS` once per run so the runner progress bar advances correctly") and the queue note ("runner progress only -- diagnostic, not scored") -- **neither of which any downstream consumer reads**.

## 2. How that becomes `supports` for SD-011

`claim_evidence.v1.json` entry 2351 records `status: PASS`, `evidence_direction: supports`, `confidence: 0.75`, `confidence_rationale: "PASS with supporting direction"` -- overriding the pack manifest's own declared `evidence_direction: diagnostic`.

A **three-condition conjunction**, each verified at source. The middle one is an *absence*, not a bad value:

1. **The indexer reads the runner summary, not the run-pack manifest.** No glob reaches `<exp>/<run_id>/manifest.json`; the run's own `INDEX.md` links "manifest" to `v3_exq_472_..._output.json`, whose keys are exactly `claim_ids / experiment_purpose / output_files / run_id / status`. The rich manifest beside it is **invisible to the index**.
2. That file carries **no `evidence_direction` key**, so `_normalize_direction(None)` returns `"unknown"`.
3. `direction_explicitly_set` keys on the presence of an `evidence_direction_note` (`build_experiment_indexes.py:1871`), **not** on `evidence_direction` -- so the guard against auto-inference never engages.

`status: DIAGNOSTIC` is outside `_DERIVED_STATUSES`, so `final_status` collapses to `PASS`; lines 3519-3520 then infer `supports` from that collapsed status.

### Blast radius, measured

Across the runs carrying a non-standard explicit manifest `status`, **69** `claim_evidence` rows are produced and **exactly one -- this one -- reads `supports`**. 65 of 69 are `scoring_excluded`; the 4 that are not all read `mixed`. Every other affected run declares a direction that survives normalisation intact. (The *run* count is scan-dependent, 35-40, because a run can appear in several files with different status keys; the row-level figures are stable across scans.)

### The harm is a mislabel, not a weighting error

The row carries `scoring_excluded: "diagnostic_probe"` and `adjudication: "unverified"`, and it is genuinely **inert on every scored register**: SD-011's `direction_counts`, `pass_runs` and posterior all exclude it; SD-011 is absent from the gap register; it appears nowhere in `promotion_demotion_recommendations`. Its only visible surface is `pending_review.md`, by design.

It is worth fixing because it misleads a human reader, and because it is a landmine if `scoring_excluded` is ever relaxed -- **not** because it is currently weighting a claim.

## 3. A second finding: the headline statistic is a cancellation

| seed | swap | recovery_ratio |
|---|---|---|
| 42 | L3 -> L5 | **1.0987** |
| 7 | L3 -> L5 | **1.0702** |
| 42 | L5 -> L3 | **0.7919** |
| 7 | L5 -> L3 | **0.9285** |

`recovery_ratio_median = 0.999379` reads as textbook stability and is the midpoint of two clean opposite-direction pairs -- both L3->L5 above 1, both L5->L3 below 1. `stream_corr` moves oppositely by direction too (L3->L5 falls; L5->L3 rises 4-6x).

**With n=2 per direction this is a pattern worth testing, not an established asymmetry.** The point that survives regardless is procedural: a pilot whose declared job is to *anchor a recovery threshold* should report the per-direction pairs, because the pooled statistic destroys exactly the structure an anchor would need.

The anchor never propagated. `EXP-0090` is recorded `status: executed`, `executed_by: V3-EXQ-198` -- a run 20 days *before* this pilot, carrying no C7 threshold. Risk is latent, not realised. (The bookkeeping oddity -- a proposal closed by a run predating its own anchoring pilot -- is flagged for a governance eye.)

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a for scoring | An unscored pilot cannot support or weaken SD-011. Non-contributory as claim evidence. |
| Biological reference | not engaged | Instrument-calibration pilot, not a mechanism test. |
| Prerequisites | partially unmet | SD-011's `what_would_answer` names three preconditions; (i) is satisfied, (ii) and (iii) are unmet/unstated. Even a scored version would not have addressed the claim. |
| Implementation | adequate for the pilot | Not exercised as a claim test. |
| Environment | adequate | L3/L5 swapped both directions, 2 seeds each. |
| Measurement | **under-instrumented** | The pooled median hides the directional split (section 3). |
| Integration | n/a | Actions uniformly random in every phase; no selection pathway exercised. |
| Scale | under-powered | n=2 per direction. |

**Failure-location: n/a** -- no bucket established and none asserted. The finding is an evidence-*recording* defect downstream of the run, not a failure of REE, mechanism or environment.

## 5. Recording provenance

Seven always-core fields absent: `recording_schema`, `substrate_hash`, `substrate_commit`, `machine`, `machine_class`, `elapsed_seconds`, `config`. Seeds are present. The manifest is hand-written inline rather than via `pack_writer`; `output_files` are Windows paths, so this ran on Daniel-PC. The run predates the 2026-07-12 Experimental Recording Standard.

**Why it surfaced only now:** the indexer's discovery glob could not reach this pack's shape, so the run was invisible for 4.5 months until `76921a56ce` (GFLAG-0111, 2026-09-01). It was never grandfathered and never marked reviewed -- the machinery could not see it. Worth remembering when a backlog looks ignored: check whether the detector could reach it.

## 6. Routing (ratified at the Step 8 gate)

**(1) Per-claim.** Record as an unscored diagnostic pilot with no criterion -- `non_contributory` for SD-011 -- and set `diagnostic_evidence_adjudicated: true`. SD-011's `status` (stable) and `epistemic_category` (standard) do not move.

**(2) Tooling -- RECORDED for `/governance` to chip, deliberately not chipped here** (CLAUDE.md Session Land Protocol step 6). Recommended fix: **gate the direction inference at `build_experiment_indexes.py:3519-3520` on `experiment_purpose != "diagnostic"`**. That key IS present in the file the indexer actually reads, so the information already exists at the point of the defect.

Three alternatives are inadequate, recorded so they are not re-proposed:
- extending `_normalize_direction` cannot see a key that is **absent**;
- hand-correcting `claim_evidence.v1.json` entry 2351 edits a **derived** artifact the next `governance.sh` regenerates;
- widening `_DERIVED_STATUSES` alone would flip this row from `supports` to **`weakens`**, not correct it.

This also settles the decision deferred by the 2026-08-08 `_display_status` fix, which declined to touch `final_status` because reclassifying evidence direction was "a governance change, not a display fix": the measurement it was waiting on is that exactly **1 of 69** affected rows reads `supports`.

**This skill recommends; `/governance` applies.**
