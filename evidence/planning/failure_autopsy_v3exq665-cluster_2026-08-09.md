# Failure Autopsy — V3-EXQ-665 cluster (Curriculum Affective Fishtank Showcase, `vacuous_pass` flag, 2 runs)

**Generated:** 2026-08-09T07:09:13Z
**Scope:** cluster
**Status:** confirmed (interactive gate run 2026-08-09 — low controversy; identical mechanism to the just-confirmed V3-EXQ-906 autopsy, zero claim impact)

## Executive summary

Both `v3_exq_665_curriculum_affective_fishtank_showcase` runs (2026-06-10T15:51:23Z and 2026-06-10T23:30:54Z) carry a confirmed **false positive** on the indexer's `vacuous_pass` adjudication flag — the identical join-mismatch mechanism `failure_autopsy_V3-EXQ-906_2026-08-09` just diagnosed for a different (but structurally identical) driver family. Both runs' actual load-bearing gates (`core_channels_non_degenerate`, `harm_pathway_trained`) are real, non-degenerate, and correctly computed; both genuinely PASS. The flag fires because the indexer's legacy `criteria_non_degenerate{}` &harr; `criteria[]` join cannot find a matching `criteria[]` entry for several individually-reported channels (`channel_z_block`, `channel_excite`, `channel_dread`, and — in the earlier run only — `channel_vigor`), because this driver rolls up to 10-12 reported channels into one aggregate `core_channels_non_degenerate` criterion covering only 4 of them by design. Under the indexer's "ambiguity resolves toward flagging" convention, the unmatched `False` values trip `vacuous_pass` on an otherwise-real PASS. These two runs were the ones V3-EXQ-906's autopsy explicitly flagged as "confirmed recurring, not one-off" and recommended be closed out without independent re-discovery — this artifact is that closure.

## 1. Facts

Both runs: `experiment_purpose: diagnostic`, `claim_ids: []`, `evidence_direction: non_contributory`, `outcome: PASS`. Neither is a dry run (`check_dry_run_citations.py`: 0 dry, both clean, checked alongside V3-EXQ-904 in this session). Both carry `adjudication: "vacuous_pass"` in `claim_evidence.v1.json`.

`interpretation.criteria[]` (identical shape, both runs — 3 gating entries):

| name | load_bearing | passed (both runs) |
|---|---|---|
| core_channels_non_degenerate | true | true |
| harm_pathway_trained | true | true |
| freeze_not_locked | false | true |

`interpretation.criteria_non_degenerate{}` (informational, 12 keys) — run `20260610T233054Z`: all true except `channel_z_block: false`, `channel_excite: false`, `channel_dread: false`. Run `20260610T155123Z`: all true except `channel_vigor: false`, `channel_z_block: false`, `channel_excite: false`, `channel_dread: false`. None of `channel_z_block` / `channel_excite` / `channel_dread` / `channel_vigor` has a matching `criteria[]` entry by name — the driver only ever declared the single aggregate `core_channels_non_degenerate` criterion, scoped (per the same pattern V3-EXQ-906 diagnosed) to a named core-channel subset that does not include these four.

**Mechanical trace** (identical to `failure_autopsy_V3-EXQ-906_2026-08-09`'s Section 1, reproduced here rather than re-derived): the indexer's legacy fallback join builds `by_name` from `criteria[].name -> load_bearing`, then for every key in `criteria_non_degenerate{}` tries to match a `criteria[]` name. For the unmatched `channel_*` keys, zero candidates match (no `channel_*`-prefixed `criteria[]` entry exists). Per the documented design, unmatched `False` values are not excluded, and `any(v is False for v in degeneracy_assertions)` while `status=="PASS"` returns `vacuous_pass`.

**Recurrence**: this is the same root cause as V3-EXQ-906 (a broad-report/narrow-gate driver declaration shape with no per-excess-channel `criteria[]` entry), on a different but structurally analogous driver (`v3_exq_665_curriculum_affective_fishtank_showcase.py` vs. `v3_exq_906_full_stack_observational_fishtank.py`). Confirmed **3 total instances** of this join-mismatch sub-case across the corpus (906 + both 665 runs), all `experiment_purpose: diagnostic`, all `claim_ids: []`.

## 2. Claim-layer mapping — not applicable

`claim_ids: []` on both runs. No claim is under test, tagged, or at risk of mis-weighted demotion/promotion.

## 3. Biological-reference triage — not applicable

No mechanism is under test as a claim (showcase/diagnostic driver, curriculum-affective observational sweep). No bio triage owed.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | N/A | no claim under test by design |
| Biological reference | N/A | — |
| Dependency prerequisites | N/A | — |
| Implementation completeness | complete (for what's gated) | `core_channels_non_degenerate` and `harm_pathway_trained` correctly implemented and scoped on both runs |
| Environment adequacy | adequate for stated purpose | curriculum-affective fishtank showcase sweep, matches driver's own breadth goal |
| Measurement adequacy | adequate for the runs; the ADJUDICATION TOOLING is under-instrumented | both runs' own metrics are complete and honestly reported; the defect is in the indexer's join heuristic, shared with V3-EXQ-906, not in either experiment |
| Integration adequacy | N/A | — |
| Scale/capacity | N/A | — |

## 5. Cluster pattern (tooling recurrence, not a claim cluster)

Not a claim-bearing cluster. The recurrence is a tooling pattern: 3 confirmed instances of the identical false-positive mechanism (V3-EXQ-906 + both V3-EXQ-665 runs), all `experiment_purpose: diagnostic`, all `claim_ids: []`, all `vacuous_pass`. One structural property of a driver-declaration shape (broad-report/narrow-gate split with no per-excess-channel `criteria[]` entry) shared across at least two independently-authored driver families, not three independent bugs, and not specific to either driver.

## 6. Learning extracted / routing (confirmed)

**Diagnosis class**: `complicated (buildable)` — same fix class as V3-EXQ-906 (driver-side: emit an explicit `criteria[]` entry per reported-but-non-gating channel; or indexer-side: recognize an aggregate `criteria[]` entry's own channel scope and exclude out-of-scope `criteria_non_degenerate{}` keys from the vacuity check by default). This autopsy does not re-open that fix decision — it was already surfaced as out-of-scope maintenance by V3-EXQ-906's autopsy, and is not re-surfaced here to avoid duplicating that recommendation across artifacts.

**User-confirmed routing (2026-08-09 interactive gate): confirm known false positive, no action.** Both runs' `outcome: PASS` and `evidence_direction: non_contributory` are genuine and correctly recorded. `claim_ids: []` means no governance demotion/promotion, no `/lit-pull`, no `/queue-experiment` re-test is owed. Recommend to governance: treat both adjudications as known false positives; clear them from any flagged-diagnostic `pending_review.md` section without further action. These are now formally closed — no longer orphaned/un-autopsied (they had sat unadjudicated for ~2 months, since 2026-06-10, until V3-EXQ-906's investigation on 2026-08-09 surfaced them).

`recommended_substrate_queue_entry.action: none` — not a substrate gap.

**Step 9b**: not applicable — no claim under test, no `fanout_recommendation`, matching the V3-EXQ-906 precedent exactly.

## 7. Evidence quality note (informational — no claim to attach it to; offered for the manifest/governance record)

> [2026-08-09 failure-autopsy, confirmed]: both V3-EXQ-665 runs' vacuous_pass flags (2026-06-10) are false positives, mechanism identical to failure_autopsy_V3-EXQ-906_2026-08-09 (indexer's criteria_non_degenerate{} <-> criteria[] join has no matching criteria[] entry for several individually-reported channels this driver intentionally rolls into one aggregate gating criterion). Both runs' actual gates (core_channels_non_degenerate, harm_pathway_trained) are real and correctly computed. No claim is affected (claim_ids: []); no governance action required beyond clearing the flagged-diagnostic pending_review entries. ~2-month-old orphaned flags, now formally closed.
