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
