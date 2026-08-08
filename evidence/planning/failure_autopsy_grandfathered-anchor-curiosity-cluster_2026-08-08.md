# Failure Autopsy (cluster, closure pass): MECH-309/ARC-062/ARC-065 origin runs (11 runs, already covered)

**Generated:** 2026-08-08T17:10:36Z
**Scope:** cluster (11 runs, 2026-05-10 to 2026-05-22)
**Status:** confirmed (Step 8 interactive gate: user confirmed closure + report the detection-script gap)

## Governing fact -- read this first

**This is not un-autopsied backlog.** All 11 runs are already covered by CONFIRMED prior `/failure-autopsy` artifacts -- either as a dedicated target or as a named `cluster_pattern.members` entry -- and the claims they tag have each moved to much later, higher-quality evidence chains. The output here is a consolidation/closure note, not a fresh four-layer diagnosis.

## Dry-run gate

`check_dry_run_citations.py` on all 11: 0 dry, 11 clean. The `dry_run_unreachable_criterion` lint fires on 6 of the batch's driver scripts (543c/d/e/g/j/k -- the documented v3_exq_543 lineage trap), but does not affect these runs since all are full-budget real executions, not smokes.

## Per-run coverage table

| run_id (short) | claim_ids | outcome | evidence_direction | already autopsied via |
|---|---|---|---|---|
| 543c (05-11) | ARC-062, MECH-309 | FAIL | non_contributory | `failure_autopsy_EXQ-543e_2026-05-17` (narrative: "whole 543b/c/d/e lineage is non-contributory") |
| 543d (05-12) | ARC-062, MECH-309 | FAIL | non_contributory (per-claim: ARC-062=weakens) | `failure_autopsy_EXQ-543e_2026-05-17` (dACC axis root cause: dacc_weight=0.0 master-gate) |
| 543e (05-17) | ARC-062, MECH-309 | FAIL | non_contributory | own dedicated confirmed autopsy, `failure_autopsy_EXQ-543e_2026-05-17` |
| 543g (05-17) | ARC-062, MECH-309, INV-074, MECH-334 | FAIL | non_contributory | `cluster_pattern.members` of `failure_autopsy_V3-EXQ-543h_2026-05-18` (cross-machine proof: 1/3 minority-basin artifact) |
| 543j (05-19) | ARC-062, MECH-309, INV-074, MECH-334 | FAIL | non_contributory (all 4) | manifest's own note cites `failure_autopsy_543i_2026-05-19` as operative (basin RNG/init nondeterminism) |
| 543k (05-22) | ARC-062, MECH-309, INV-074, MECH-334 | FAIL | mixed (ARC-062 weakens, MECH-309 supports) | own dedicated confirmed autopsy, `failure_autopsy_V3-EXQ-543k_2026-05-21` |
| 569 (05-16) | ARC-065 | FAIL | non_contributory | manifest cites "EXQ-571 diagnostic"; root-caused in `evidence/planning/v3_exq_571_root_cause_2026-05-25.md` |
| 572 ×3 (05-16) | ARC-065 | FAIL | non_contributory | directly named as the broken predecessor runs in confirmed `failure_autopsy_EXQ-572-573_2026-05-17`: "earlier 3 runs had n=0, correctly reclassified" -- verified independently: `metrics.json.values` literally `{}` |
| 605 (05-21) | Q-043, ARC-065, MECH-313, MECH-314 | FAIL | non_contributory | Cluster B of confirmed `failure_autopsy_V3-EXQ-603a-b-c-604-605_2026-05-29` |

All 11 manifests: `substrate_hash` absent, environment hashes `"unknown"` -- universal recording gap (pre-dates the 2026-07-12 Experimental Recording Standard). Not actionable now (all already-adjudicated), noted so nobody re-derives a fresh `substrate_ceiling` verdict off these manifests directly.

## Claim status (current)

**MECH-309** -- `candidate/v3_pending/substrate_ceiling`. Live evidence anchor `failure_autopsy_V3-EXQ-732_2026-07-10`. Evidence history runs continuously 05-17 -> 08-01 through 719a, 714, 654i/j, 654g, 690, 851 -- all months after this batch.

**ARC-062** -- same posture, same evidence chain (`v3_pending/substrate_ceiling`, `pending_retest_after_substrate: true`, `ceiling_decision: deferred`). `narrow_supports_flag` set.

**ARC-065** -- `status: stable`, **`epistemic_category: standard`** -- ceiling LIFTED 2026-06-17 by V3-EXQ-569i PASS. The evidence_quality_note explicitly closes the loop: the 569/572/605-era `substrate_ceiling` reading was correct at the time, superseded once the GAP-A top-k shortlist fix landed.

## Biological-reference triage

MECH-309/ARC-062 (rule-apprehension, GAP-B): lit-pulls A+B both discharged 2026-05-09 (`targeted_review_arc_062_rule_apprehension/`, `targeted_review_arc_062_refuge_forage_ecology/`). Three biologically-real gating-site candidates (BG cortico-striatal, hippocampal, PFC top-down) confirmed present -- biology divergence is NOT the failure mode; the confirmed read is a missing-prerequisite/implementation-instability signature.

ARC-065 (diversity generation): lit anchors present (Wilson 2014, Aston-Jones & Cohen 2005, Daw 2006, Wittmann 2008, Haarnoja 2018, Friston, Schmidhuber/Pathak, Kidd & Hayden). A formal-import concern was flagged in the 572-573 autopsy (REE implements MECH-313/314/320 as additive scalar score-biases, not the biological LC-NE gain-modulation mechanism) but noted as untestable until the propagation ceiling was resolved -- not adjudicated as falsification.

## Cluster convergent pattern

| Experiment | Claim(s) | Read |
|---|---|---|
| 543c/d/e | ARC-062, MECH-309 | measurement/config confound (dACC axis dead), precursor to the real ceiling |
| 543g (cluster w/543f/h) | + INV-074, MECH-334 | substrate instability confirmed cross-machine (ACTIVE host-A only, INERT elsewhere, bit-identical) |
| 543j (confirms 543i) | + INV-074, MECH-334 | basin selection nondeterministic across runs/machines |
| 543k (extends 543i) | + INV-074, MECH-334 | ARC-062 weakens/MECH-309 supports -- first contributory MECH-309 support, single-pathway |
| 569, 572×3, 605 | ARC-065 (+Q-043, MECH-313/314) | bias-channel propagation dead upstream of E3 selection -- same structural fingerprint as the 543 line, one generation earlier |

**Structural verdict: one structural property, shared across BOTH lineages.** Both the 543 (ARC-062/MECH-309, GAP-B) and 569/572/605 (ARC-065, GAP-A) lines hit an identical shape: a differentiating signal is genuinely present upstream but does not survive to change the committed E3 selection -- later formally named MECH-439 F-dominance/selection-authority conversion ceiling. This batch is the early, still-locally-diagnosed instance of what became the corpus-wide dominant failure mode (74% of all autopsies conclude `substrate_ceiling`, per the skill's own text).

## Re-derive brake state (R1-R3, confirmed corpus)

MECH-309: **17** confirmed `substrate_ceiling` hits. ARC-062: **18**. ARC-065: **4** (historical -- category since lifted to `standard`). All three far past `RE_DERIVE_BRAKE_THRESHOLD=2`; MECH-309/ARC-062 have been firing continuously since well before this batch's own 543k autopsy landed (claims.yaml text logs "17th/18th/19th/20th/21st readings"). **The brake fired long ago and stayed fired** -- no new build recommendation from this batch; the correct disposition is to confirm subsumption and close.

**Note (infrastructure finding, not fixed here):** the mechanical R1-R3 recipe under-counts because several of this batch's own run_ids (543c/d/g/j) never got their own `targets[]` row -- they were folded into an anchoring run's row via `cluster_pattern.members` instead. This is a real gap in the counting recipe, not just this batch's grandfather-detection issue (see below).

## Recommended routing

- **543c/d/e/g/j/k, 569, 605**: no new routing -- all already closed out through `/implement-substrate` (GatedPolicy attractor stability -> MECH-448/449 -> F-dominance work) and `/lit-pull` (both discharged) in the confirmed chain. `routing: governance-note-only`.
- **572×3**: recommend `evidence_direction: superseded` pointing at `v3_exq_572_intervention_a_dual_attractor_20260516T095117Z_v3` (the same-day real run; confirmed by `failure_autopsy_EXQ-572-573_2026-05-17` as "systematic data collection failure," `metrics.json.values: {}`). Trivial housekeeping fix, not new experimental or substrate work.

## Infrastructure finding to report (not fixed by this skill -- report only)

**The grandfathered-backlog detection mechanism (`fail_autopsy_grandfather.json` / whatever seeded it) checks for coverage via a literal `targets[].run_id` match and misses coverage recorded via `cluster_pattern.members` or narrative supersession chains.** All 11 runs in this batch were flagged as "reviewed, never autopsied" despite being fully covered by existing confirmed autopsies for months. This suggests the 480-run V3 grandfathered list is likely significantly over-inclusive, and future backlog-clearing sessions should cross-check both `targets[].run_id` AND `cluster_pattern.members` (plus narrative citation, where mechanically detectable) before assuming a run is genuinely un-autopsied. Recommend surfacing this to governance/the grandfather-file maintainer as a detection-script improvement -- out of scope for this skill to fix directly (analysis + handoff only).

## Learning extracted

1. A "reviewed but never autopsied" flag can be stale relative to claims.yaml's own evidence history and the confirmed-autopsy corpus. All 11 runs here read as an open backlog by manifest timestamp alone, but were fully processed and superseded by 2026-05-29 at the latest (ARC-065 by 06-17; ARC-062/MECH-309 continuously through 08-01).
2. Cluster-member coverage lives in `cluster_pattern.members`/narrative supersession chains, not always in a per-run `targets[]` row -- check both before concluding a run is unautopsied.
3. Empty-metrics duplicate runs (572×3) are a distinct, cheap-to-spot failure signature (`metrics.json.values == {}`) worth a mechanical check before investing analysis time.
4. Both GAP-A (ARC-065) and GAP-B (ARC-062/MECH-309) independently hit the identical "signal reaches but doesn't route to committed selection" fingerprint in May 2026, months before it was named MECH-439 F-dominance.
