# `_write_planning_outputs` exp_count vs `scoring_excluded` -- read-only investigation, 2026-08-26

Session `metaworker-chip-20260826-scoring-excluded-expcount-investigation`, spawned from
`chip-20260826-scoring-excluded-expcount-investigation`, following on from the
"Fix shape 1 implemented, 2026-08-26" addendum in
`evidence/planning/design_decision_evidence_credit_gap_20260821.md`. That addendum found that
`_write_planning_outputs` builds its own `entries_by_claim` straight from `matrix["entries"]`
(the full audit log), filtered only by `is_applicable()` (epoch staleness) -- **not** by
`scoring_excluded` -- and confirmed this on MECH-489 (3 diagnostic-probe entries counted as
`exp_count=3` in `evidence_backlog.v1.json`, vs `genuine_exp_count=0` in the correctly-filtered
`claim_evidence.v1.json`). This is a **read-only investigation** per the chip brief -- no code,
`claims.yaml`, `epistemic_category`, or `evidence_direction` changes were made.

## TL;DR

**Recommend (a): fix it.** The bug is real, confirmed to generalize far beyond MECH-489 (112
claims fleet-wide as of this writing), and is **not just a cosmetic `exp_count` display issue** --
it also corrupts `conflict_ratio`, `overall_confidence`, `experimental_confidence`, and
`entries_total` for every affected claim, because `_write_planning_outputs` recomputes its own
`claim_meta` via `_summarize_claim_entries()` on the unfiltered entry list rather than reusing the
already-correct `matrix["claims"][claim_id]` object. On the held-out cases checked below, this
produces both **false negatives** (a real "zero genuine experimental evidence" condition silently
masked) and, in at least one case (MECH-171), an outright **priority-level misclassification**
(shown `medium`, should be `high`) that keeps the claim out of the explorer's "Backlog (High
Priority)" governance table entirely. No downstream consumer was found that depends on or needs
the current (unfiltered) definition for `exp_count`/`overall_confidence`/`conflict_ratio`
specifically. One adjacent computation (recurring failure-signature counting) plausibly *does*
want to include diagnostic-probe entries deliberately -- see the scoping note in the
Recommendation section; the fix should not be a blind wholesale swap.

---

## 1. Downstream consumers of `evidence_backlog.v1.json`'s `source_counts`

Grepped for `evidence_backlog` and `source_counts` across `REE_assembly`, `ree-v3`, and
`REE_Working/scripts`. Hits:

- `REE_assembly/explorer.html` -- the live consumer that matters. `refreshGovernanceData()`
  fetches `evidence/planning/evidence_backlog.v1.json` into `governanceBacklog`, and the
  Governance tab's **"Backlog (High Priority)" table** renders
  `backlogItems.filter(item => item.priority === 'high').slice(0, 15)` with columns
  `backlog_id`, `claim`, `evidence_needed`, `reasons` (explorer.html:5647-5651, 5843-5858). This
  is a direct, unfiltered pass-through of the buggy `priority`/`reasons` fields to whoever is
  running a `/governance` cycle and reading the dashboard. There is **no** medium/low-priority
  table anywhere in the file (`grep -n "priority === 'medium'"` -> no hits) -- a claim
  misclassified as `medium` by this bug is invisible in the governance UI, not merely
  mis-labeled in a visible row.
- `REE_assembly/evidence/planning/scripts/run_governance_cycle.py` -- loads the same file
  (line 634), derives `high_backlog = [item for item in backlog_items if item.get("priority") ==
  "high"]` (line 730) which feeds `governance_agenda.v1.json`'s summary counts (consumed by the
  explorer's priority pane and `updateGovConflictBadge()`), plus `backlog_saturation_holds` /
  `backlog_escalation_required` derived from `item.get("reasons", [])`. Same exposure: a reason
  token corrupted by this bug propagates into the agenda.
- `REE_assembly/dual_insights_report.html`, `REE_assembly/insights_report.html` -- static,
  narrative snapshots generated *from* `evidence_backlog.v1.json` at report-generation time
  (e.g. "417 items, 123 of them high priority"). They reflect whatever the backlog says,
  correct or not; not an independent code path with its own reliance on the broader definition.
- `REE_assembly/serve.py` -- **zero** references to `evidence_backlog` or `source_counts`. The
  explorer fetches the JSON file directly as a static asset; no API endpoint mediates or
  recomputes it.
- `scripts/audit_coordination_plane_dirt.py`, `scripts/audit_stashes.py` -- path-string matches
  only (coordination-plane hygiene / stash-safety allowlists), not consumers of the field
  contents.
- `test_build_experiment_indexes.py` -- see Section 2; the existing test suite already pins the
  current (buggy) behavior with an explicit note that it is a known gap, not a specification.

**No consumer was found that relies on, needs, or was designed around the current unfiltered
definition.** Every live consumer (explorer governance tab, `run_governance_cycle.py`'s agenda)
treats `exp_count`/`priority`/`reasons` as if they already reflect scored, non-excluded evidence
-- which is exactly what they do NOT currently do for a claim whose only experimental entries are
`scoring_excluded`.

## 2. Is `matrix["entries"]` meant to be pre-filtered before feeding `entries_by_claim`?

`_write_claim_evidence_matrix`'s own docstring (`build_experiment_indexes.py:3214-3220`) is
explicit and states the intended contract directly:

> All entries are included in `matrix["entries"]` for audit purposes.
> Only *applicable* and *non-excluded* entries feed into claim confidence scores.

This is not an oversight to read into the code -- it is the stated design. `matrix["entries"]`
(the full audit log, `scoring_excluded` and all) is explicitly scoped to **audit visibility**,
and the docstring explicitly says only applicable-and-non-excluded entries should feed
**"claim confidence scores"**.

`_write_planning_outputs`'s local `claim_meta` -- built via
`_summarize_claim_entries(claim_entries, generated_at_dt)` on the unfiltered `entries_by_claim`
(`build_experiment_indexes.py:5921-5922`) -- computes exactly a claim confidence score
(`overall_confidence`, `experimental_confidence`, `genuine_exp_count`, `source_counts`,
`conflict_ratio`) from that unfiltered population. This is a **second, independent**
confidence-score computation that does not reuse the already-correct
`matrix["claims"][claim_id]` object `_write_claim_evidence_matrix` already built (via
`claim_to_entries`, which never receives a `scoring_excluded` entry in the first place --
`build_experiment_indexes.py:3413-3461`). Confirmed by direct inspection: `_summarize_claim_entries`
and `_compute_claim_confidence` themselves have **no `scoring_excluded` check at all** -- they
score whatever entries they are handed, unconditionally.

**Conclusion for item 2: this is an oversight, not a deliberate second design.** The docstring's
own stated policy ("only applicable and non-excluded entries feed into claim confidence scores")
is violated by `_write_planning_outputs`'s local recomputation. There is no comment, test, or
design doc anywhere in the file suggesting `entries_by_claim` was deliberately left unfiltered by
`scoring_excluded` for a reason -- the epoch (`is_applicable`) filter is applied explicitly and
carefully (with a documented literature exemption, `build_experiment_indexes.py:5835-5839`), and
`scoring_excluded` was simply never added alongside it.

## 3. GOV-HELDOUT-1 check -- held-out cases beyond MECH-489

**Non-degeneracy scope**: a claim counts as a held-out case only if the current (buggy,
unfiltered) computation and the proposed fix (filter by `scoring_excluded`, matching
`claim_evidence.v1.json`) give a **different** governance-visible outcome for it. Cases were
found by scanning the live `claim_evidence.v1.json` (`entries` + `claims`, snapshot as of this
session) for every claim whose experimental entries are **all** `scoring_excluded` (excluding
`stale_epoch`, since that reason is already caught by the shared `is_applicable()` filter both
paths apply, so it produces no discrepancy) **and** whose correctly-filtered `genuine_exp_count`
is 0. **112 such claims exist fleet-wide** (script and full list retained in this session's tool
transcript; not reproduced in full here for length). Of the 112, 22 are already `priority: high`
in the live backlog (for other reasons, so the bug is currently reason-token-cosmetic for them),
**63 are currently `priority: medium`**, and 27 do not currently appear in the backlog at all
(status/pinning reasons not further audited here). Three representative, non-degenerate cases,
plus the motivating MECH-489, are detailed below.

| claim | claim_type / status | excluded reasons | buggy `exp_count` (backlog) | `genuine_exp_count` (claim_evidence, correct) | current priority / reasons | verdict under current (buggy) code | verdict under fix (filter `scoring_excluded`) | old vs new differ? |
|---|---|---|---|---|---|---|---|---|
| **MECH-489** (motivating) | mechanism_hypothesis / candidate | `diagnostic_probe` x3 | 3 | 0 | high / `directional_conflict_alert` | conflict flagged, driven partly by 3 non-scored diagnostic entries folded into `genuine_exp_direction_counts` | conflict_ratio computed from literature alone -> **0.0**, `directional_conflict_alert` would NOT fire; `missing_experimental_evidence` suppressed instead by the already-shipped `diagnostic_evidence_adjudicated` flag | **YES** -- current reason (`directional_conflict_alert`) is a false positive entirely manufactured by the bug (see detail below) |
| **ARC-071** (held-out) | architectural_commitment / candidate, `v3_pending: true` | `diagnostic_probe` x6 | 6 | 0 | high / `active_conflict` only | claim's own `implementation_note` says verbatim "NO EXPERIMENTAL EVIDENCE YET" -- but the backlog signal shows 6 experimental entries and never fires `missing_experimental_evidence` | `exp_count` -> 0, `missing_experimental_evidence` (a **high**-priority marker) newly fires, matching the claim author's own stated evidentiary state | YES -- `reasons`/`evidence_needed` gain a correct, currently-absent signal (priority stays high here only because `active_conflict` already forced it) |
| **INV-047** (held-out) | derived_prediction / candidate | `degenerate`, `diagnostic_probe`, `superseded` x10 | 10 | 0 | high / `active_conflict`, `directional_conflict_alert` | 10 disqualified entries (degenerate + diagnostic + superseded) presented as if they were live evidence; `directional_conflict_alert` already fires today too (0.667 >= 0.40), so that specific token is degenerate for this claim | `exp_count` -> 0, adds `missing_experimental_evidence`; conflict_ratio recomputed from literature alone (`supports=1, weakens=1, mixed=2`) -> **1.0**, still fires `directional_conflict_alert` (stronger, not weaker) | YES for `missing_experimental_evidence` / `evidence_needed`; NO for the conflict-alert token specifically (both fire) -- a mixed case, included to show the fix does not uniformly relax signals |
| **MECH-171** (held-out) | derived_prediction / candidate | `degenerate` x7 | 7 | 0 | **medium** / `low_exp_conf` only | claim absent from the explorer's "Backlog (High Priority)" table entirely -- 7 fully-disqualified entries hide a genuinely zero-evidence claim behind a merely-medium signal | `exp_count` -> 0, `missing_experimental_evidence` (**high** marker) newly fires alongside `lit_only_above_cap` -- **priority flips medium -> high** | **YES, most consequential case**: a genuine priority-level misclassification, not just a reason-token difference -- this claim is currently invisible to a governance session reading the dashboard, and under the fix it would surface as a top-15 high-priority item |

**MECH-489 detail (the false-conflict mechanism, confirmed by direct arithmetic against the live
data):** the three `diagnostic_probe` entries carry directions `weakens, weakens, supports`.
Because `_is_genuine_experimental_entry()` checks only V1/V2/V3 substrate genuineness -- **not**
`scoring_excluded` -- all three are folded into `genuine_exp_direction_counts` at
`build_experiment_indexes.py:6142-6148`, combined with the 5 literature entries
(`supports=3, mixed=2`) into `_combined_dirs = {supports: 4, weakens: 2, mixed: 2}`. Feeding
`_direction_conflict_ratio`: `2*min(4,2)/6 = 0.667`, exactly matching the live
`evidence_backlog.v1.json` value and clearing the 0.40 alert threshold. With the three excluded
entries correctly removed, `_combined_dirs` reduces to the literature-only
`{supports: 3, mixed: 2, weakens: 0}`; `directional_total = 3`, `2*min(3,0)/3 = 0.0` -- no
conflict at all. **MECH-489's current live `directional_conflict_alert` / high-priority status is
itself a direct artifact of this bug**, not an independent, separately-confirmed conflict signal.
(This is a stronger and more specific finding than the design-decision doc's own framing, which
treated `exp_count` in isolation; `conflict_ratio` is corrupted by the identical root cause.)

MECH-450 and Q-005 (not tabulated above, checked as additional sanity spot-checks) show the same
medium->high flip shape as MECH-171: both currently `priority: medium` / `reasons: [low_exp_conf]`
with `genuine_exp_count: 0` and buggy `exp_count` of 6 and 1 respectively, both `candidate`
status, neither `diagnostic_evidence_adjudicated`. Fleet-wide, **all 111 non-MECH-489 candidates
would newly gain the `missing_experimental_evidence` high-priority marker under the fix**, since
`diagnostic_evidence_adjudicated` has only ever been backfilled for MECH-489 (per the "Fix shape
1" addendum) -- so none of the other 111 have the suppression flag that would keep them off the
high-priority list the way MECH-489 now would.

**Existing test contract already anticipates this exact investigation.**
`test_build_experiment_indexes.py`'s
`test_diagnostic_evidence_adjudicated_does_not_suppress_when_exp_count_nonzero` (added alongside
fix shape 1) pins the current buggy behavior *by name*, with a docstring stating verbatim: "this
test exists so a future reader who 'fixes' `entries_by_claim` to filter `scoring_excluded` does
not silently change this flag's behaviour without re-running GOV-HELDOUT-1." That test's expected
outcome (`missing_experimental_evidence not in reasons`, because `exp_count != 0` bypasses the
gate) is exactly the artifact this investigation confirms is wrong, and it is a load-bearing
pointer for whoever implements the fix: that test's assertion will need to flip once
`entries_by_claim` correctly filters `scoring_excluded`.

## 4. Recommendation

**(a) Fix it.** The evidence is unambiguous:

- No consumer anywhere in the codebase (explorer, `run_governance_cycle.py`, `serve.py`, or the
  narrative report generators) depends on or was designed around the current unfiltered
  definition; every live consumer treats the fields as if they were already correctly filtered.
- The producing function's own docstring states the intended contract ("only applicable and
  non-excluded entries feed into claim confidence scores"), and the current code violates it --
  this reads as an oversight (a second, independently-written scoring pass that never got the
  `scoring_excluded` check the first pass has), not a deliberate second design.
- The bug generalizes far beyond the motivating MECH-489 case: 112 claims fleet-wide currently
  carry a `genuine_exp_count` of 0 masked by a nonzero unfiltered `exp_count`, of which 63 are
  currently misclassified as `medium` priority (invisible in the explorer's governance table)
  and would very likely become `high` under a fix, and MECH-489's own current `high` / active
  `directional_conflict_alert` status is itself a manufactured artifact of the bug rather than an
  independently-real conflict.

**Scoping note for whoever implements the fix (do not treat this as "make `entries_by_claim`
identical to `claim_to_entries`" without checking one adjacent computation first):**
`_write_planning_outputs` also uses `claim_entries` (the same unfiltered list) to build
`signature_counts` / `recurring_signatures` (`build_experiment_indexes.py:5976-5993`), filtered
only by `_is_genuine_experimental_entry` (substrate genuineness), not `scoring_excluded`. Unlike
`exp_count`/`conflict_ratio`/`overall_confidence`, there is a *plausible* deliberate reason to
keep diagnostic-probe entries in the failure-signature aggregation specifically: diagnostic
probes exist precisely to surface recurring root-cause signatures (`queue-experiment` SKILL.md's
own definition -- "probes, root-cause discrimination, substrate readiness tests"), and a claim
that keeps hitting the same failure signature across several disqualified probes is exactly the
kind of `consider_new_structure`/escalation signal governance would want visible. This was not
independently confirmed as intentional (no comment says so explicitly), but it is different in
kind from the confidence-score fields the docstring explicitly scopes, so the fix should reuse
`matrix["claims"][claim_id]` (or equivalently filter `entries_by_claim` on `scoring_excluded`) for
the confidence-score fields specifically (`overall_confidence`, `experimental_confidence`,
`genuine_exp_count`, `source_counts`, `conflict_ratio`, `entries_total`), and treat the
signature/batch/saturation computations as a separate decision requiring their own check rather
than folding them in by default.

Per CLAUDE.md's standing rule against unilateral shared-scoring-code changes and this repo's own
`/governance`-review convention for this exact gap (see the design-decision doc's Decision B /
"Status: Not implemented" precedent), **this fix is not implemented here** -- it is scoped,
evidenced, and left for a `/governance`-reviewed chip to pick up, which should re-run
GOV-HELDOUT-1 against the pinned test above and against a fresh snapshot of the 63
medium-priority candidates (composition will have shifted by the time it is picked up) before
shipping.

---
Investigation only. No code, `claims.yaml`, `epistemic_category`, or `evidence_direction` changes
made in this session.
