# Design-decision / diagnostic-purpose evidence-credit gap -- 20260821

chip-20260821-sd099-diagnostic-purpose-evidence-credit, following on from
IGW-20260821-229 / EVB-0622's gating_reason (which surfaced this rather than
fixing it -- "governance / experiment-design calls deliberately NOT taken
unilaterally by this session"). This doc records the two decisions requested
by that chip brief, with the code citations that back them, and is the
durable artifact a future session or a `/governance` cycle should read before
re-opening either question.

## Decision A -- is `EXPERIMENT_PURPOSE = "diagnostic"` correct for the
V3-EXQ-910/910a/910b (MECH-489/SD-099) lineage?

**Conclusion: yes, retained as-is. Do not change V3-EXQ-910b (still pending)
to `"evidence"`.**

`.claude/skills/queue-experiment/SKILL.md` Step 3 defines `"diagnostic"` as
for "probes, root-cause discrimination, substrate readiness tests," excluded
from governance confidence/conflict scoring, "appear[ing] in the evidence
record as context only." All three drivers explicitly self-declare this
framing (`v3_exq_910_..._validation.py:49-50`, `v3_exq_910a_..._retest.py:70`,
verbatim: "first test of a freshly-built mechanism, substrate-readiness
validation for MECH-489/SD-099, not a governance evidence run"). This is a
deliberate, consistent author choice across the lineage, not an oversight in
one script -- and it fits the definition: three iterations (910 -> 910a ->
910b) have been needed just to get the *instrument* (the decision_counts
readout) correct, each surfacing a NEW substrate/driver defect
(910: norm-vs-value scale mismatch; 910a: decision-logging persistence bug;
910b: env-step vs E3-tick counting mismatch) rather than delivering a stable
verdict. That is exactly what "diagnostic" is for.

The apparent tension -- that `/failure-autopsy` sessions DID use 910/910a's
findings to update MECH-489's `evidence_quality_note` narrative (weakens
direction on falsifying signature #1, "MIXED, not a clean weakens") even
though the purpose tag marks them "context only" -- is not a bug. Read
literally, "context only" means excluded from the AUTOMATED
confidence/conflict number, not excluded from the human-read evidence record.
A diagnostic run informing a governance session's qualitative read of a claim,
while never feeding the auto-computed `overall_confidence` / `genuine_exp_count`
scalar, is the system working as designed. The defect is downstream, in
Decision B.

## Correction to EVB-0622's gating_reason -- only ONE of the two claimed
exclusion mechanisms is actually active

EVB-0622 (`REE_assembly/evidence/planning/experiment_proposals.v1.json`)
states MECH-489's two 2026-08-10 entries are excluded from scoring "once as
`scoring_excluded='stale_substrate'` (claims.yaml MECH-489
`pending_retest_after_substrate: true`) and once as
`scoring_excluded='diagnostic_probe'`." Verified directly against
`build_experiment_indexes.py` and the two manifests: **only the
`diagnostic_probe` branch is actually firing.**

- `build_experiment_indexes.py:3384-3391` reads `run.pending_retest_after_substrate`
  from **the manifest** (`manifest.get("pending_retest_after_substrate", False)`,
  line 1740-1741) -- a per-RUN flag, not the claim-level one.
- `_load_claim_registry` (`build_experiment_indexes.py:3555` on) parses
  claims.yaml's claim-level fields into `registry_meta` and does **not**
  extract `pending_retest_after_substrate` at all -- grep confirms zero
  references to it in that function. The claim-level flag in claims.yaml
  (MECH-489, line 80385) has **no code path** into `scoring_excluded` at all.
- Both manifests
  (`v3_exq_910_mech489_defensive_orienting_validation_20260810T004433Z_v3.json`,
  `v3_exq_910a_mech489_defensive_orienting_decision_retest_20260810T213616Z_v3.json`)
  confirmed by direct read: `pending_retest_after_substrate` key is absent
  (defaults False). So the `stale_substrate` branch (line 3384) does not match
  for either entry; execution falls through to line 3391
  (`run.experiment_purpose in ("diagnostic", "baseline")`), which **does**
  match (`experiment_purpose: "diagnostic"` confirmed in both manifests) and
  is the sole active exclusion.

Practical consequence: fixing (or not fixing) the claim-level
`pending_retest_after_substrate` handling would have made **no difference**
to MECH-489's `genuine_exp_count`. Any future work on this claim should not
assume the stale-substrate branch is contributing to the zero -- it is not.

## Decision B -- should the auto-proposal generator's why_now signals
account for diagnostic-adjudicated evidence and `design_decision` ->
instantiating-child routing?

**Conclusion: yes, this is a real, confirmed gap, generalizing beyond
MECH-489/SD-099 -- but the fix is a shared-scoring-code change with broad
blast radius, and is NOT implemented in this session. It is escalated via a
`kind: decision` chip for `/governance` review (see chip_ledger entry
referenced at the end of this doc), per CLAUDE.md's standing rule that a
governance/indexer design call is not taken unilaterally, and per
GOV-HELDOUT-1's discipline that a standing-scoring-code change should be
checked against held-out cases before shipping -- which a `/governance`
session, with the fuller claim-registry context, is better placed to run than
a single narrow chip.**

### The gap, confirmed in code

`build_experiment_indexes.py`'s `_write_planning_outputs` (the function
containing the `missing_experimental_evidence` / `lit_only_above_cap` /
`insufficient_experimental_replication` signal computation,
`build_experiment_indexes.py:5941-6007`) reasons **purely on numeric evidence
counts** (`exp_count`, i.e. `source_counts.experimental`, itself built from
`genuine_exp_count`) with:

- **zero references to `instantiates`** anywhere in the file (grepped), so a
  `design_decision` claim's own instantiating-child relationship is
  completely invisible to this signal computation;
- **zero references to `design_decision`** as a claim_type anywhere in the
  file, so nothing exempts or special-cases this claim_type the way
  `_is_experiment_ineligible_claim` (`build_experiment_indexes.py:3794`)
  exempts `architectural_commitment`/`invariant`/`open_question` types via
  `epistemic_category` resolution -- `design_decision` resolves to
  `epistemic_category = "standard"` by default (the `_resolve_epistemic_category`
  mapping at `build_experiment_indexes.py:3852` on lists only
  `architectural_commitment`, `invariant`+`universal`, `open_question`;
  everything else, including `design_decision`, falls through to
  `"standard"`), so it is fully subject to the same why_now signals as an
  ordinary `mechanism_hypothesis` claim unless an explicit
  `epistemic_category:` override is added per-claim;
- **no awareness of `evidence_quality_note` content** -- a claim with an
  extensively narrated, governance-adjudicated diagnostic history (MECH-489's
  is ~2,500 words across two dated governance entries) is treated identically
  to a claim with literally zero touchpoints, so long as `genuine_exp_count`
  reads 0.

### Confirmed to generalize -- not a MECH-489/SD-099 one-off

| claim | claim_type | relationship | `genuine_exp_count` |
|---|---|---|---|
| MECH-489 | mechanism_hypothesis | (itself; 2 diagnostic-purpose runs, no scoring credit) | 0 |
| SD-099 | design_decision | `instantiated_by` MECH-489 ("Validation experiment: see MECH-489 what_would_answer" -- `docs/claims/claims.yaml:80362`) | 0 |
| SD-032 | design_decision | instantiated by 5 children (`instantiates: SD-032` x5) | not in `claim_evidence.v1.json` at all (`claim_meta is None`) |
| SD-033 | design_decision | instantiated by 5 children (`instantiates: SD-033` x5, one of them SD-033c) | not in `claim_evidence.v1.json` at all |
| SD-033c | design_decision | `instantiates: SD-033` | (child; not itself checked here) |

SD-032 and SD-033 do not even appear in `claim_meta` (no run or literature
entry has ever tagged the parent id directly -- only children are tagged).
**Verified via a second, independent read of the code (Explore agent,
2026-08-21T21:05Z): this is a DIFFERENT failure mode from MECH-489/SD-099, not
a worse version of the same one.** `_write_planning_outputs`'s per-claim loop
(`build_experiment_indexes.py:5776` on) hits `if claim_meta is None: ... else:
continue` at line 5928/5939-5940 for any non-`open_question` claim with zero
matrix entries -- so SD-032/SD-033 are **silently skipped entirely**: zero
`why_now` reasons, no backlog/proposal entry, confirmed by zero matches for
either id in `evidence_backlog.v1.json` and `experiment_proposals.v1.json` as
of this writing. That is arguably a WORSE failure mode than MECH-489/SD-099's
(which at least surfaces and gets a human look each cycle) -- these two are
invisible to the entire auto-proposal pipeline, with no run that could ever be
queued against the *parent* id to clear it even if someone noticed. Do not
conflate the two shapes when scoping a fix: MECH-489/SD-099 need signal
SUPPRESSION on an already-populated backlog entry; SD-032/SD-033 would need
the loop to stop `continue`-ing past a `design_decision` parent with
instantiating children in the first place before any suppression logic could
even apply.

SD-099 already has a hold applied the same day this doc was written
(`docs/claims/claims.yaml` SD-099 `evidence_quality_note`,
`gov-20260821-0203`: `hold_pending_v3_substrate APPLIED ... Status stays
candidate. No promotion or demotion until a V3 experiment completes.`) --
that protects SD-099's own status/confidence disposition from today's
governance cycle, but it is a per-claim, per-cycle manual disposition, not a
fix to the why_now signal computation. Absent a code fix, SD-099 will need
the same manual hold re-applied (or a fresh `EVB-*` gated the way EVB-0622
was) every cycle the signal keeps firing, and SD-032/SD-033 have no
equivalent hold at all as of this writing.

### Two candidate fix shapes (for `/governance` to pick between or combine --
not decided here)

1. **Structured-flag-aware suppression (NOT narrative-parsing).** Confirmed
   (Explore agent, 2026-08-21): `evidence_quality_note` is parsed from
   claims.yaml and carried into claim metadata, but `_write_planning_outputs`'s
   `_add_reason` decision logic (`build_experiment_indexes.py:5941-6098`)
   never reads it -- it is display-only (surfaced verbatim, truncated, into
   the promotion/demotion markdown at `build_experiment_indexes.py:4812-4816`).
   Do NOT fix this by grepping `evidence_quality_note` prose for
   `"confirmed failure_autopsy"` or similar -- fragile, and exactly the kind
   of string-matching heuristic this repo's own contracts warn against
   elsewhere. Instead add a small **structured** claims.yaml field (e.g.
   `diagnostic_evidence_adjudicated: true`), set explicitly by `/failure-autopsy`
   at the point it confirms a diagnostic-purpose run's finding into a claim's
   narrative (exactly the moment MECH-489's 910/910a entries were adjudicated),
   and have `_add_reason` suppress `missing_experimental_evidence` /
   `lit_only_above_cap` when it is set and `exp_count == 0`. Covers MECH-489
   directly; requires a `/failure-autopsy` SKILL.md change to set the flag
   going forward (retrofitting it onto MECH-489's own past adjudications is a
   one-line backfill).
2. **`design_decision` -> instantiating-child evidence-visibility.** Two
   sub-cases, confirmed to need DIFFERENT code paths (see the SD-032/SD-033
   correction above -- do not design one fix assuming both hit the same
   branch):
   - **SD-099-shaped** (parent DOES have a `claim_meta` entry, reads
     `genuine_exp_count=0`): before adding `missing_experimental_evidence` /
     `lit_only_above_cap` / `synthetic_signals_only`, check whether the
     validating claim (found via `instantiated_by` reverse-lookup, or SD-099's
     prose form) itself carries real, non-superseded experimental evidence,
     and suppress if so.
   - **SD-032/SD-033-shaped** (parent has NO `claim_meta` entry at all, hits
     the `continue` at line 5939-5940 before any signal is even computed):
     the loop must first recognize a `design_decision` parent with
     instantiating children as a claim that legitimately has no direct
     `claim_meta` BY DESIGN, and either synthesize a `why_now`-relevant view
     from the children's aggregate evidence, or explicitly and visibly mark it
     "not applicable, validated via children" rather than the current silent
     `continue` (which is indistinguishable from "not yet looked at").

Neither shape changes `overall_confidence` / `genuine_exp_count` themselves --
both are scoped to the why_now / auto-proposal signal layer only, so a claim's
promotion/demotion math is untouched. Do not widen either fix to also affect
scoring -- that is a different, larger change this doc does not evaluate.

## Do not re-run GOV-REUSE-1 for this claim pair

Per the chip brief: EVB-0622 already ran GOV-REUSE-1 for SD-099 on 2026-08-21
and both halves of its `what_would_answer` are accounted for (trigger-alignment,
already in 910/910a; decision-alignment, already queued as V3-EXQ-910b). No
new SD-099 or MECH-489 experiment should be queued as a result of this doc.

---
Session: metaworker-chip-20260821-sd099-diagnostic-purpose-evidence-credit.
Decision-chip raised for `/governance` ratification of Decision B:
see `TASK_CHIPS.json` chip-ref cited in the closing WORKSPACE_STATE.md line
for this session.

---

## GOV-HELDOUT-1 check, 2026-08-26 -- sub-case A of Decision B's fix shape 2
## is a MEASURED NO-OP. Do not implement it as written.

Run by session `rc-mac-designdecision-heldout-finding` (Mac, DLAPTOP) against
`claim_evidence.v1.json` + `docs/claims/claims.yaml` as of 2026-08-26T06:40Z,
before writing any code, per CLAUDE.md General Rules. **The check changed the
design**, which is the outcome that discipline exists to produce -- recording it
here so the eventual implementer does not rebuild the dead branch.

### The finding

Fix shape 2's **SD-099-shaped sub-case** proposes: for a `design_decision`
parent that HAS a `claim_meta` entry reading `genuine_exp_count = 0`, suppress
`missing_experimental_evidence` / `lit_only_above_cap` / `synthetic_signals_only`
*if the instantiating child itself carries real, non-superseded experimental
evidence*.

**On every real instance in the registry, the child carries none, so the
suppression can never fire.** There are exactly three such parents:

| parent | child | child exp / genuine_exp / lit | suppression fires? |
|---|---|---|---|
| SD-099 (motivating case) | MECH-489 | 0 / **0** / 5 | no |
| SD-091 (**held-out**) | MECH-481 | 0 / **0** / 4 | no |
| SD-101 (**held-out**) | MECH-503 | 0 / **0** / 4 | no |

SD-091, SD-101, MECH-481 and MECH-503 appear **nowhere** in this document
(verified by grep: 0 mentions each), so they are genuine held-out cases, not
the motivating ones re-read. They independently reproduce the pattern, so this
is structural rather than an SD-099 quirk.

The mechanism is already stated in this doc's own "Correction to EVB-0622"
section and simply was not carried forward into the fix shape: MECH-489's two
runs are `scoring_excluded='diagnostic_probe'`, which is exactly what drives
`genuine_exp_count` to 0. The child is therefore **as evidence-less as the
parent by the same mechanism**. A parent-suppression rule keyed on child
evidence is asking a question whose answer is structurally always "no".

Shipping it would add a dead branch to a shared scoring path used by all 1052
claims -- cost with no behaviour change, and a future reader would reasonably
assume it was doing something.

### What IS real -- sub-case B, unchanged and worth building

The **SD-032/SD-033-shaped** sub-case survives the check intact. Those parents
have no `claim_meta` entry at all, hit the `continue` at
`build_experiment_indexes.py:5939-5940`, and are invisible to the entire
auto-proposal pipeline -- while their children carry genuine evidence:

| parent | claim_meta | children (exp/genuine/lit) |
|---|---|---|
| SD-032 | NONE | SD-032a 1/**1**/20, SD-032b 0/0/14, SD-032c 0/0/3, SD-032d 0/0/4, SD-032e 0/0/4 |
| SD-033 | NONE | SD-033a 3/**3**/19, SD-033b 0/0/5, SD-033c NONE, SD-033d NONE, SD-033e 0/0/9 |
| SD-033c | NONE | ARC-035 0/0/13, MECH-133 NONE, MECH-151 0/0/4, MECH-152 1/**1**/2, MECH-235 NONE |

So the recommended scope is **sub-case B only**: stop silently `continue`-ing
past a `design_decision` parent that has instantiating children; emit a visible
entry with a dedicated reason (e.g. `validated_via_instantiating_children`)
carrying the children's aggregate evidence, instead of either silence or a
spurious `missing_experimental_evidence`.

Implementation note for whoever picks this up: `_load_claim_registry`
(`build_experiment_indexes.py:3605` on) does **not** currently extract
`instantiates` -- grep confirms zero references to it in the whole file -- so the
reverse parent -> children map has to be built from a new field added to that
hand-rolled line parser. `instantiates` is a **scalar** in claims.yaml (e.g.
`instantiates: SD-033c    # comment`), not a list, in all 23 occurrences; it
needs the same `_strip_inline_yaml_comment` treatment the sibling fields get.
Blast radius of the reverse map is small and auditable: only 9 distinct parents
are referenced by any `instantiates`, of which 6 are `design_decision`
(SD-032, SD-033, SD-033c, SD-091, SD-099, SD-101) and 3 are
`mechanism_hypothesis` with a `claim_meta` entry already (MECH-059, MECH-256,
MECH-269) and so are untouched by a `claim_meta is None` branch.

### SD-099 still needs fix shape 1, and this check does not weaken that

Dropping sub-case A leaves SD-099/MECH-489 **unfixed** -- that is the honest
consequence, not an oversight. The only shape that addresses it is fix shape 1
(the structured `diagnostic_evidence_adjudicated` flag), which needs a
claims.yaml schema field plus a `/failure-autopsy` SKILL.md change to set it at
adjudication time, and is a materially larger decision than an indexer-local
edit. It is deliberately left open here rather than folded in.

### Status

**Not implemented in this session.** `build_experiment_indexes.py` was under an
active TASK_CLAIMS claim by `metaworker-chip-20260825-indexer-vacuous-pass-or-semantics-gap`
(opened 2026-08-26T05:45:30Z) for an unrelated vacuous_pass OR-semantics fix;
`task_claim.py open` arbitrated this session as NOT the owner, so per CLAUDE.md
"Conflict resolution" the code was left untouched and only this finding was
recorded. Decision chip
`chip-20260821-governance-design-decision-evidence-credit-fix` stays open with
its scope now narrowed to sub-case B.

---

## Fix shape 1 implemented, 2026-08-26 -- with a confirmed pre-existing gap that
## limits it on the MOTIVATING case itself (chip-20260826-sd099-diagnostic-adjudicated-flag)

Session `metaworker-chip-20260826-sd099-diagnostic-adjudicated-flag`. Shipped:
`diagnostic_evidence_adjudicated` claims.yaml field (parsed in
`_load_claim_registry`, same hand-rolled-parser idiom as `instantiates`),
`validate_claims.py` warn-only schema check, `_write_planning_outputs` suppression
of `missing_experimental_evidence` / `lit_only_above_cap` (and the `evidence_needed`
catch-all default) when the flag is set and `exp_count == 0`, and the
`/failure-autopsy` SKILL.md recommendation field (`per_claim_recommendation.
recommended_diagnostic_evidence_adjudicated`, both `.claude/` and `.agents/`
copies) so future adjudications populate it. MECH-489 backfilled
`diagnostic_evidence_adjudicated: true`.

### GOV-HELDOUT-1 check, run before landing, per CLAUDE.md General Rules

Checked the suppression condition (`exp_count == 0` -- deliberately mirroring
the EXISTING `missing_experimental_evidence`/`lit_only_above_cap` guard's own
condition, so the suppression is symmetric with what it counteracts) against 3
real claims from the live `evidence_backlog.v1.json` / `claim_evidence.v1.json`
snapshots (2026-08-25T18:02Z / 23:08Z), none of which this doc's fix-shape-1
recipe text was written from. Non-degeneracy: a case counts only if old vs. new
wording actually differ, i.e. the claim currently shows `exp_count == 0` with
`missing_experimental_evidence`/`lit_only_above_cap` firing.

| claim | `_write_planning_outputs` `exp_count` (backlog, unfiltered) | `genuine_exp_count` (claim_evidence.v1.json, filtered) | old vs new differ? |
|---|---|---|---|
| **MECH-489** (motivating case) | **3** | 0 | **NO** -- see finding below |
| MECH-481 (held-out) | 0 | 0 | YES -- suppression engages correctly |
| SD-091 (held-out) | 0 | 0 | YES -- suppression engages correctly |

**Finding: `_write_planning_outputs` re-derives its OWN `entries_by_claim` directly
from `matrix["entries"]` (the full, unfiltered audit log), filtered only by
`is_applicable()` (epoch staleness) -- NOT by `scoring_excluded`.** This is
different from `claim_evidence.v1.json`'s own `matrix["claims"][id]` sub-object,
which is built in `_write_claim_evidence_matrix` from the separately,
correctly-filtered `claim_to_entries` (scoring_excluded entries `continue`d out
before being appended, `build_experiment_indexes.py:3413-3461`).
`_write_planning_outputs` does not reuse that already-correct `matrix["claims"]`
result -- it rebuilds its own from the raw log instead
(`build_experiment_indexes.py:5829-5840`), and that rebuild has no
`scoring_excluded` check at all.

Confirmed directly against `claim_evidence.v1.json`'s own `entries` array: MECH-489
carries 8 total entries for its claim_id, 3 of them `source_type: "experimental"`
(`v3_exq_910`, `v3_exq_910a`, `v3_exq_910b`), **all three** `scoring_excluded:
"diagnostic_probe"`. All three are epoch-applicable (`architecture_epoch:
"ree_hybrid_guardrails_v1"`, matching the current cutoff), so all three land in
`_write_planning_outputs`'s own `entries_by_claim["MECH-489"]` and count toward
`exp_count` -- giving 3, not 0, even though every one of them is
`scoring_excluded` and `genuine_exp_count` (which DOES filter on
`_is_genuine_experimental_entry`) correctly reads 0. This is why the live
`evidence_backlog.v1.json` (`EVB-0610`, snapshot 18:02Z) shows MECH-489's actual
current reason as `directional_conflict_alert` (from a real literature/experimental
conflict_ratio computation) -- not `missing_experimental_evidence` /
`lit_only_above_cap` at all.

**Consequence: fix shape 1, exactly as scoped and shipped, does NOT change
MECH-489's own current backlog entry.** Its `exp_count` never reads 0 via this
function's own (buggy) count, so `missing_experimental_evidence`/
`lit_only_above_cap` were never firing on it in the first place -- there is
nothing for the new flag to suppress. The flag's suppression mechanism is
correctly built and verified to work on genuinely-zero-`exp_count` claims (see
MECH-481 / SD-091 above), and the MECH-489 backfill is still correct and required
(the flag is meant to describe the claim's adjudication state, independent of
whether today's `exp_count` bug happens to mask its effect) -- but readers should
not expect MECH-489's own backlog priority/reasons to visibly change from this
fix alone. **MECH-489's actual live churn (`directional_conflict_alert` ->
`synthetic_signals_only` downgrade) is a different mechanism, out of scope for
fix shape 1, and not decided here.**

**Not fixed in this session, and not decided here -- a further, larger design
call:** whether `_write_planning_outputs`'s `entries_by_claim` should instead
reuse `matrix["claims"]` (or otherwise filter on `scoring_excluded` itself). That
is a shared-scoring-code change touching every claim's `evidence_needed`/`reasons`
computation fleet-wide (not scoped to diagnostic-adjudicated claims), well beyond
this chip's mandate -- flagged here for a future `/governance`-reviewed chip,
per CLAUDE.md's standing rule against unilateral shared-scoring-code changes.
