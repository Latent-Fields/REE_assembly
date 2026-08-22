# ARC-030 / SD-017 "ceiling-may-have-lifted" -- 2026-08-22 assessment

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or any other registry).**

Session: `metaworker-chip-20260822-ceiling-lifted-retests-arc030-sd017` (headless, DLAPTOP)
Chip: `chip-20260822-ceiling-lifted-retests-arc030-sd017`
Date: 2026-08-22T17:22Z

## Summary

`check_substrate_ceiling_audit.py` flags both ARC-030 and SD-017 as
`ceiling-may-have-lifted (ACTIONABLE)` every governance cycle. **Neither retest is
runnable today.** Both are genuine recurrences of prior, already-investigated
findings -- not new information:

| Claim | Owed retest | Runnable today? | Gate |
|---|---|---|---|
| ARC-030 | COMBINED-vs-NOGO_ONLY discriminative pair (Go/NoGo symmetry) | **No** | `complex (probe-gated)` -- MECH-457 competence-floor discrimination, itself stalled |
| SD-017 | 436-family slot-differentiation retest with a write-address fix flag ON | **No** | `puzzle (known rules)` once unblocked, but currently gated on an open `contested_disposition` (GFLAG-0047) plus a pending governance call on V3-EXQ-943 |

Neither was queued. No edits made to `experiment_queue.json`, `experiments/`,
`claims.yaml`, or `pending_retest_after_substrate` on either claim, per this chip's
instructions.

---

## ARC-030

### (a) The owed retest

Per `claims.yaml` `what_would_answer`: the **COMBINED (Go+NoGo, real z_goal via
SD-057) vs NOGO_ONLY (Go channel ablated)** discriminative pair, re-running the
EXQ-138a/226 design on the corrected wiring. Acceptance: `benefit_ratio_COMBINED/
NOGO_ONLY >= 1.2`, `harm_ratio <= 1.3`, `avg_goal_norm >= 0.4` (live-signal floor),
holding on **>=2/3 seeds INDIVIDUALLY** (not aggregate -- the 2026-04-06 illusory-
conflict governance note). Gated behind a **MANDATORY non-degeneracy precondition**:
FULL-arm `resource_visit_rate` must beat RANDOM by `>=0.05` on `>=2/3` seeds.

### (b) Runnable today? -- No. `complex (probe-gated)`, not `complicated (buildable)`

The audit's own trigger (MECH-307 `implemented`) is **correct but insufficient**:
MECH-307 is genuinely implemented and `from_dims`-reachable (confirmed
2026-08-08, `d63f13b7`), but the mandatory G0 non-degeneracy precondition gates
the retest, and that gate has **already been run and failed twice**:

- `v3_exq_899_arc030_mech307_g0_readiness` x2 (2026-08-08): both FAIL /
  `non_contributory`. `g0_on_pass = g0_off_pass = 0.0`. `mech307_perturbs_baseline
  = 0.0` (ON 0.00401 vs OFF 0.00390 -- indistinguishable) while RANDOM scores
  0.01164 -- **the FULL arm forages below a random policy**. Both readiness
  *preconditions* were themselves met (`reached_p2_frac_seeds = 1.0`,
  `p2_window_live_frac_seeds = 0.667`), so this is a genuine gate failure, not a
  dead measurement window.

The failure was traced (`failure_autopsy_V3-EXQ-866a-G0_2026-08-08`, confirmed) to
the **MECH-457 competence-floor phenomenon** (approach-before-avoidance ordering),
reclassified `competence_implementation_gap` -- not itself a `substrate_ceiling` on
ARC-030 -- routed "no new build; cross-ref MECH-457 H1/H2/H3 portfolio". The
`substrate_queue.json` entry for that portfolio,
`mech457_competence_bootstrap_explorer`, is `status: blocked_pending_discrimination`,
`ready: false`, `node_class: complex (probe-gated)` -- **a spike, not a buildable
task**: it is blocked on naming which competence-directed dependency (behavioral
prior vs innate approach drive) to build.

**That discrimination itself is not close to unblocking ARC-030.** Cross-checked
against `hypothesis_space_registry.v1.json` (qid tracking MECH-457): the GOV-FANOUT-1
portfolio meant to answer this (H-bc-prior vs H-approach-primitive, opened
2026-07-18) already ran and resolved **without naming a build path** -- V3-EXQ-780
inconclusive (re-routed), V3-EXQ-781 non_contributory (H-approach-primitive
eliminated). The registry's own `growth_restriction` note says the campaign's
"discrimination phase is complete" and directs any further MECH-457-lineage claim to
register its **own** qid rather than grow this one further. In other words: the
substrate_queue entry's `blocked_note` ("gated on the NEW GOV-FANOUT-1 discrimination
portfolio... do NOT build blind") names a portfolio that has since run and come back
empty-handed, and nothing has re-opened the question since. ARC-030's actual blocker
is therefore doubly stale-labeled: `claims.yaml` still names MECH-307 (lifted);
`substrate_queue` names a discrimination portfolio that already concluded without a
build target.

### (c) Has an equivalent run already happened since the substrate landed?

**Yes -- twice, and it FAILED both times** (`v3_exq_899_...`, both 2026-08-08, see
above). This is not merely absence-of-evidence from an unrun queue; the readiness
gate was tested and did not clear.

### Recurrence history (queue-absence is not evidence this was never checked)

This is the **fourth** time the audit has mechanically re-flagged ARC-030, and the
fourth independent chip session to reach the identical DID-NOT-QUEUE verdict after a
full re-verification:

- `chip-20260807-arc030-mech307-retest` (2026-08-07) -- initial correction; found
  MECH-307 unreachable via `from_dims` at the time; routed to
  `/implement-substrate`.
- `chip-20260808-arc030-mech307-readiness` (2026-08-08) -- queued the G0 readiness
  diagnostic (V3-EXQ-899).
- `chip-20260808-g0-foraging-competence-autopsy` (2026-08-08) -- autopsied the FAIL,
  reclassified to MECH-457 competence-floor.
- `chip-20260812-arc030-ceiling-lifted-retest` (done 2026-08-14) -- re-flagged by the
  audit, re-verified, DID NOT QUEUE.
- `chip-20260813-queueexp-arc030-retest` (withdrawn 2026-08-14) -- duplicate of the
  above.
- `chip-20260816-arc030-ceiling-lifted-retest` (done 2026-08-19) -- third
  investigation, re-verified nothing had changed, staged a governance
  recommendation (`arc030_ceiling_recurrence_staged_2026-08-19.md`, still
  AWAITING USER REVIEW, unapplied).
- **This chip (2026-08-22) -- fourth investigation. Re-checked `evidence/experiments/`
  for any ARC-030- or MECH-457-tagged manifest newer than the 2026-08-19 staged doc:
  none found. Nothing has moved.**

### Recommendation (not applied by this session -- governance's call)

The 2026-08-19 staged recommendation still stands and has not been actioned:

1. Set `ceiling_decision: deferred` on ARC-030 with a `ceiling_routing_note` naming
   MECH-457 (competence floor) as the operative blocker, not MECH-307. This is the
   audit's own purpose-built park mechanism (23 claims already use it) and would
   stop the mechanical re-flagging every cycle without losing the owed retest.
2. Leave `pending_retest_after_substrate: true`.
3. Append the V3-EXQ-899 FAIL (x2) to ARC-030's `evidence_quality_note`, which
   currently stops at the 2026-08-08 "readiness chipped" line and does not record
   that the gate then ran and failed.
4. **New this session**: also record that the MECH-457 GOV-FANOUT-1 discrimination
   the `substrate_queue` blocker names has itself already concluded
   (`H-approach-primitive` eliminated, `H-bc-prior` inconclusive/re-routed,
   2026-07-18) without producing a build target -- so re-checking "has MECH-457's
   discrimination portfolio landed yet" will not by itself surface a next step;
   MECH-457 needs its own fresh disposition before ARC-030 can move.

**Not queued.**

---

## SD-017

### (a) The owed retest

Per `claims.yaml` (evidence_quality_note, 2026-08-16, V3-EXQ-436f, the current
authoritative disposition): a **436-family slot-differentiation retest, run with a
non-degenerate write-address selection mechanism ON** (either
`contextmemory_write_usage_balancing=True` or
`contextmemory_write_selection="refractory"`), scored on the corrected,
occupancy-aware DV machinery 436e/436f already established (never the whole-bank
`slot_cosine_sim` product-of-similarity-and-occupancy metric 436b/436c/436d
falsified). SD-017/ARC-045/MECH-166 share this gate.

### (b) Runnable today? -- No. Two independent, currently-open gates.

**The audit's trigger substring-matches on the wrong substrate_queue entry.** It
flags SD-017 via the `SD-016` entry (`status: implemented`) in `unblocks_claims` --
correct that SD-016 (cue-indexed retrieval) is implemented, but **stale**: SD-017's
own evidence_quality_note re-scoped its gate away from SD-016 three times since
(after-DV-repair -> after-SD-016-armed -> **after-WRITE-PATH-ADDRESSING-BUILD**, as
of 436f 2026-08-16). SD-017 carries no `ceiling_retest_binding_substrate` field, so
the audit's own binding-substrate refinement (built for exactly this MECH-314-style
false-positive pattern) does not engage here -- this is a second instance of the
same known gap, not a new bug to fix in this chip.

The **binding** substrate is `contextmemory-write-path-addressing-degeneracy`
(`unblocks_claims: [SD-017, ARC-045, MECH-166]`), status **`implemented_pending_
validation`** -- not `implemented`. Both fix mechanisms (conscience-bias write
selection, refractory write selection) are code-landed
(ree-v3 `76cbf844`, `692f8526d0`) but validation was, until this week, still owed.

**That validation has now run** (`V3-EXQ-943`, queued 2026-08-20, executed and
autopsied 2026-08-21, `failure_autopsy_V3-EXQ-943_2026-08-21.json`): occupancy floor
MET under a real REEAgent loop -- BIAS reaches 16/16 slots occupied on 5/5 seeds
(round-robin agreement 0.993-0.996, real but counter-driven, not content-addressed);
REFRACTORY hits its structural `k+1` floor on the three legacy-lock seeds. **But the
substrate_queue entry's own `validation_record_943` explicitly instructs: do NOT
flip status `implemented_pending_validation -> implemented_validated` in this
finding.** Two things remain open per that same note:

1. **A human/governance decision** on whether this occupancy-without-addressing
   result (BIAS is a counter-driven LRU cycle; REFRACTORY is a structural `k+1`
   guarantee) actually closes the "corrupting" 1-slot-bank defect the 436e/436f
   autopsies diagnosed, or whether genuine content-addressed write selection is
   still owed before the claim-level retest means anything.
2. **A flag-on 436-family retest itself** -- V3-EXQ-943 tested the write-path FIX
   mechanism (occupancy, on deterministic DVs), not the SD-017/ARC-045/MECH-166
   differentiation CLAIM. No such retest has been queued.

**GFLAG-0047 (open, `contested_disposition`) directly gates step 2, per this chip's
own instruction to stop if so.** It names SD-017 explicitly (with MECH-495,
ARC-045, MECH-166, MECH-147) and asks: should the write-selection validation run's
DV be a **differentiation** statistic (as SD-017/ARC-045/MECH-166's own
`what_would_answer` implicitly assumes) or a **relational-topology** one (per
MECH-495's 2026-08-19 hippocampal-episodic-organisation thought -- related
experiences should overlap appropriately; maximal separation may be the wrong
objective entirely)? The flag's own text is explicit that the deterministic DVs
already chosen for the write-path validation (round-robin index, entropy,
self-repeat) are **still differentiation statistics** -- dropping `occ_cos` for
power reasons (n=38-2485 needed to discriminate arms) does **not** answer the
objective question MECH-495 raises. **Consequence: even once the write-path
substrate status question (point 1) is settled, a flag-on 436-family retest cannot
be correctly designed until GFLAG-0047 resolves** -- the DV choice it disputes is
exactly what such a retest would need to fix first.

### (c) Has an equivalent run already happened since the substrate landed?

**V3-EXQ-943 (2026-08-20/21) is the closest existing run, and it is not the owed
retest.** It validates the write-path FIX mechanism's occupancy behaviour under
deterministic DVs; it does not test the SD-017/ARC-045/MECH-166 slot-differentiation
claim itself, and per the substrate_queue entry's own note was never intended to.
No 436-family successor to 436f (i.e. a "V3-EXQ-436g"-shaped run, flag ON) has been
queued or run. `experiment_queue.json` currently holds 0 items; no manifest newer
than V3-EXQ-943 tags SD-017 as a claim_id.

### Prior investigation, and what changed since

A dedicated prior chip (`chip-20260818-sd017-ceiling-retest-gated`, resolved
2026-08-20T11:57Z, **before** V3-EXQ-943 ran) reached the same structural finding:
gate not cleared, GFLAG-0047 open and directly on-point, resolved `done` rather than
left open (the audit re-derives the finding every cycle regardless, so nothing is
lost). **What is new since that chip**: V3-EXQ-943 has since run and been autopsied
(2026-08-21), closing the "is the validation even queued" half of the gate but
explicitly leaving open the two items above (human call on occupancy-sufficiency;
GFLAG-0047). The net effect on runnability is unchanged -- still not runnable --
but the specific open items have narrowed from "validation not yet run" to "validation
ran; two adjudications still owed."

### Recommendation (not applied by this session -- governance's call)

1. Resolve GFLAG-0047 (differentiation vs relational-topology DV) -- this is squarely
   a `/governance` contested-disposition adjudication, in scope for the next
   governance cycle, not something this chip should pre-empt.
2. Alongside it, decide whether V3-EXQ-943's occupancy result (real occupancy,
   structurally guaranteed for REFRACTORY, counter-driven for BIAS -- neither is
   content-addressed) is sufficient to call the write-path substrate genuinely
   fixed for SD-017's purposes, or whether occupancy-without-addressing still
   under-serves the differentiation question -- and update
   `contextmemory-write-path-addressing-degeneracy`'s status accordingly
   (`implemented` / `implemented_validated`, or leave as-is with the reasoning
   recorded).
3. Only once both are settled, design and queue the flag-on 436-family retest
   (`/queue-experiment`), using whichever DV GFLAG-0047's resolution licenses.

**Not queued. This chip did not attempt to adjudicate either open question --** both
are governance dispositions, not build or measurement gaps this session can close,
and the chip's own brief says to stop and say so if the GFLAG-0047 fork applies.
It does.

---

## IGW-20260822-206 (not duplicated)

`inter_governance_workset.v1.json` carries a `plan reconcile` item for SD-017
(`sleep_substrate:GAP-2`), `status: upstream_blocked`, `blocked_by:
arc_062_rule_apprehension:GAP-B [in_progress]`. This is a **different, older**
tracking thread (the deferred `V3-EXQ-418m`/`436b` successors under the
`scaffolded_sd054_onboarding` / ARC-065 lineage) than the 436c-436f /
write-path-addressing lineage this assessment covers, and its `resume_condition`
text is stale (references the dead `V3-EXQ-543l` gate, superseded 2026-05-30, and
does not mention the write-path-addressing build or GFLAG-0047 at all). The plan doc
(`sleep_substrate_plan.md`, node `GAP-2`) itself already flags this inconsistency as
an open, unresolved TODO from two prior governance cycles (2026-08-02, 2026-08-10):
whether the 436b/436c/436d/436e/436f runs, which happened despite being nominally
"deferred pending GAP-B", reflect a pre-existing queue entry never withdrawn or a
gate that was never actually enforced at queue time. Not investigated further here
-- out of scope for this chip, and already an acknowledged open item elsewhere. This
assessment does not touch IGW-20260822-206 or the plan doc.
