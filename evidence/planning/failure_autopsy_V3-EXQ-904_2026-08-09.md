# Failure Autopsy — V3-EXQ-904 (ARC-070 decomposition trigger selectivity, manifest-schema defect)

**Generated:** 2026-08-09T07:09:13Z
**Scope:** single
**Status:** confirmed (interactive gate run 2026-08-09 — schema/documentation finding, zero claim impact on this run)

## Executive summary

V3-EXQ-904 is a genuine PASS supporting ARC-070's narrow mechanism-fires claim (already applied to `claims.yaml` in the 2026-08-09 governance reconciliation, separately from this autopsy). This autopsy addresses a distinct finding surfaced by that cycle's mandatory non-outcome-findings skim of the driver: the manifest's top-level `outcome` is computed as an AND of all 5 criteria, but the `interpretation.criteria[]` list marks only 1 of the 5 (`C_BOUNDARY_LIVE_real_mech288_drives_decomp`) `load_bearing: true`. No `combination_rule` field documents this discrepancy, unlike sibling drivers (e.g. `v3_exq_868_mech292_ghost_priority_relevance_confirmer.py`), which declare one explicitly. The discrepancy did not corrupt this run — all 5 criteria passed — but it misrepresents which criterion actually decides PASS/FAIL for any future reuse of this driver.

**User-confirmed fix direction (interactive gate, 2026-08-09): document only.** Add an explicit `combination_rule` field to `interpretation` on any future reuse of this driver; do not change the AND-gating behavior.

## 1. Facts

Manifest `v3_exq_904_arc070_decomposition_trigger_selectivity_20260808T201150Z_v3`, `experiment_purpose: evidence`, `claim_ids: [ARC-070]`, `evidence_direction: supports`, `outcome: PASS`. Not a dry run (`check_dry_run_citations.py`: 0 dry, 3 clean across all three targets checked in this session). `non_degenerate: true`, `degeneracy_reason: null`. Recording core present (`recording_schema`, `substrate_hash`, `machine_class`, `elapsed_seconds`, `config`, `seeds` all populated).

`interpretation.preconditions`: one precondition, `highvs_boundary_path_engaged` (the real, non-forced load-bearing measurement — MECH-288 detector firing on genuine rollout latents), measured=180.0 vs threshold=1.0, met=true.

`interpretation.criteria[]` (5 entries, all `passed: true`):

| name | load_bearing | passed |
|---|---|---|
| C_BOUNDARY_LIVE_real_mech288_drives_decomp | **true** | true |
| C_DECOMP_FIRES_vs_trigger_drives_decomp | false | true |
| C_GRAIN_decompose_yields_finer_tiles | false | true |
| C_DEPTHCAP_at_cap_marked_unreliable | false | true |
| C_OFF_structural_zero | false | true |

`interpretation.criteria_non_degenerate`: all 5 keys `true` (or forced `true` for `C_OFF`, a structural-inertness assertion).

**Driver source** (`ree-v3/experiments/v3_exq_904_arc070_decomposition_trigger_selectivity.py`):

```python
overall_pass = (non_degenerate and c_boundary_live and c_decomp_fires
                and c_grain and c_depthcap and c_off)
```

`outcome = "PASS" if overall_pass else "FAIL"`. This ANDs all 5 booleans unconditionally — the `load_bearing` flags on `criteria[]` are purely descriptive metadata that the outcome computation never reads. No `combination_rule` field exists anywhere in the driver or manifest.

**Sibling convention** (confirmed by grep across `ree-v3/experiments/`): `v3_exq_868_mech292_ghost_priority_relevance_confirmer.py` declares an explicit `combination_rule` string in its `interpretation` block spelling out exactly which criterion gates outcome and which is "reported alongside as a secondary, non-gating corroboration." V3-EXQ-904's driver has no equivalent field, despite having the identical shape (one load-bearing criterion, several non-gating ones).

**Why this matters going forward, not now**: this run's PASS is correct under either reading (AND-of-5, or load-bearing-only), because all 5 happened to pass. A future reuse of this same driver (e.g. a `904b` testing a different configuration) where `C_GRAIN`, `C_DEPTHCAP`, or `C_OFF` fails for a reason unrelated to the falsifiable prediction (e.g. an unrelated tiling bug) would report `outcome: FAIL` and, per the driver's own branch logic, `evidence_direction: weakens` against ARC-070 — even though the one criterion the claim's own `what_would_answer` FALSIFYING clause actually tests (`C_BOUNDARY_LIVE`) passed. That would be a false weakening read.

## 2. Claim-layer mapping

`claim_ids: [ARC-070]`. Read in full from `claims.yaml`: `status: candidate`, `v3_pending: true`, `claim_type: architectural_commitment`, `epistemic_category: standard`. The claim's `what_would_answer` FALSIFYING clause is precisely "the WITH-ARC-070 agent nonetheless commits blind... even though its own trigger condition... is genuinely met" — i.e. exactly what `C_BOUNDARY_LIVE` tests (180 real MECH-288 boundary fires drove 180 decompositions). The other 4 criteria (fires-on-injected-signal tautology-adjacent check, finer-tile yield, depth-cap respect, OFF-arm structural zero) are engineering-correctness checks on the surrounding machinery, not tests of the claim's own falsifiable prediction — which is exactly why the driver author already marked them `load_bearing: false`.

This run's evidence (`supports`) was **already applied** to ARC-070's `live_status`/`implementation_note` in the separate 2026-08-09 governance reconciliation (see claim's implementation_note, "mechanism-fires evidence line" block) — that application is correct and unaffected by this autopsy's finding, since all 5 criteria held. This autopsy closes the standing `evidence_quality_note` flag: "the V3-EXQ-904 combination_rule / load_bearing manifest discrepancy noted above remains routed to /failure-autopsy."

## 3. Biological-reference triage — not applicable to the defect

ARC-070's biological grounding (Badre & D'Esposito 2009, Zacks 2007, Koechlin & Summerfield 2007, Pfeiffer & Foster 2013, Schapiro et al. 2017) is already established in the claim's `evidence_quality_note` from its 2026-05-10 lit-pull. This autopsy's finding is a manifest-schema/documentation gap in the experiment driver, not a translation or biological-dependency question — no new bio triage is owed.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | this run's PASS correctly supports the narrow mechanism-fires claim under either reading of the combination rule |
| Biological reference | clear (pre-existing) | not implicated by this defect |
| Dependency prerequisites | present | MECH-288 substrate landed, real detector fired 180 times |
| Implementation completeness | complete (substrate); **incomplete (manifest schema)** | the substrate mechanism is correctly implemented and measured; the manifest's own self-description of how outcome is derived from its criteria is incomplete/inconsistent with its own `load_bearing` metadata |
| Environment adequacy | adequate | ARM_ON_HIGHVS/LOWVS/OFF design correctly isolates the boundary-triggered path |
| Measurement adequacy | **under-instrumented (documentation)** | the measurement itself is fine; the manifest fails to document which of the 5 measured criteria the claim's falsifiable prediction actually rests on |
| Integration adequacy | N/A | — |
| Scale/capacity | N/A | — |

## 5. Cluster pattern — not applicable

Single-target autopsy; no other pending FAIL/flagged-diagnostic shares this shape at time of writing.

## 6. Learning extracted / routing (confirmed)

**Diagnosis class**: `complicated (buildable)` — the fix is a named build with no open scientific question (the interactive gate resolved the one open design choice: document vs. re-gate).

**User-confirmed routing (2026-08-09 interactive gate): document only.** On any future reuse of this driver (a new lettered experiment against the same `experiment_type`, or a copy for a related test), add an explicit `combination_rule` field to `interpretation` stating: *"outcome = AND of all 5 criteria (engineering-correctness gate); only C_BOUNDARY_LIVE_real_mech288_drives_decomp is scientifically load-bearing for ARC-070's falsifiable prediction — the other 4 are structural/engineering-correctness checks (decomposition fires as designed on the injected trigger, yields finer tiles, respects the depth cap, and the OFF arm is a structural zero) whose failure would indicate an implementation bug in the surrounding machinery, not evidence against ARC-070 itself."* No change to the AND-gating behavior — this is a documentation fix only, applied via `/queue-experiment`'s normal script-modification rails the next time this driver is touched, not a standalone re-queue of V3-EXQ-904 itself.

**No retro-edit of the landed V3-EXQ-904 manifest** — the run is complete and its outcome/evidence_direction are correct as recorded.

`recommended_substrate_queue_entry.action: none` — not a substrate gap; this is a driver-script documentation gap, out of `substrate_queue.json`'s scope.

**Severity classification**: `degrading` — a known limitation that could weaken confidence in a *future* run's evidence_direction if a non-load-bearing criterion fails, but does not invalidate anything already collected (this run's PASS is genuine under either reading). Not `corrupting`: nothing has yet produced evidence that looks valid but isn't.

**`substrate_paths`**: `experiments/v3_exq_904_arc070_decomposition_trigger_selectivity.py` (relative to `ree-v3/`).

**Step 9b**: not applicable. This autopsy does not emit a `fanout_recommendation` and does not adjudicate a fresh leg of any pre-registered question in `hypothesis_space_registry.v1.json` — ARC-070's two tracked questions there (`policy_decomposition_discrimination`, `decomposition_scale_heterogeneity`) concern the R1-vs-R5 trigger-mode and MECH-288 dual-scale dissociations, neither of which this manifest-schema finding bears on. The evidence-line application itself was a separate governance action (2026-08-09 reconciliation), not this autopsy's output.

## 7. Draft evidence_quality_note (informational — no change owed to ARC-070's existing note)

> [2026-08-09 failure-autopsy, V3-EXQ-904 manifest-schema defect, confirmed]: the driver's undocumented AND-of-5-criteria outcome computation (only 1 of 5 marked load_bearing) did not affect this run's PASS (all 5 held). User-confirmed fix: document only — add a `combination_rule` field on next reuse of this driver; no change to this run's recorded evidence. Closes the standing autopsy flag on this claim's evidence_quality_note.
