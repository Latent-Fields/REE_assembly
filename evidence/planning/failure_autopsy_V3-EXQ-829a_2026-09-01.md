# Failure Autopsy: V3-EXQ-829a (retargeted from a mis-scoped V3-EXQ-829 chip)

**Generated:** 2026-09-01T19:10:15Z
**Status:** awaiting_human_confirmation (staging mode -- headless dispatcher session, no interactive user present at the Step 8 gate)
**Scope:** single target, V3-EXQ-829a
**Chip:** chip-20260901-v3exq829-failure-autopsy

---

## 0. Why this artifact is not named "V3-EXQ-829"

This chip was dispatched on the premise that V3-EXQ-829 (a scored, non-degenerate,
`experiment_purpose: evidence` FAIL) had **never been autopsied** -- verified, per the dispatch
brief, by `find -iname 'failure_autopsy*829*'` returning zero results against 2,576 autopsy
files present in the corpus.

**That premise is false.** `scripts/check_autopsy_coverage.py` -- the skill's own documented,
content-based coverage checker, which matches a candidate's `run_id`/`queue_id` against every
committed autopsy's own structured fields rather than guessing a filename -- returns:

```
CANDIDATE   COVERED_BY                                                           AVAILABLE
V3-EXQ-829  evidence/planning/failure_autopsy_2026-07-28-sweep.json (confirmed)  NO
```

`failure_autopsy_2026-07-28-sweep.json` is a **confirmed** cluster autopsy (9 targets) whose
target for `run_id: v3_exq_829_mech324_rapid_reacquisition_falsifier_20260727T170539Z_v3`
recommends `evidence_direction_per_claim: {MECH-324: mixed, MECH-323: supports}`. Governance
**applied** this on 2026-07-29 (session `sweet-williams-f30676`): MECH-323's `evidence_quality_note`
carries a `[2026-07-29 governance, V3-EXQ-829 supports (MECH-323 only...)]` block (claims.yaml
~line 59379) and MECH-324's carries a `[2026-07-29 governance, V3-EXQ-829 weakens;
failure_autopsy_2026-07-28-sweep, confirmed]` block (claims.yaml ~line 60413). The substrate
entry the sweep autopsy recommended (`MECH324-REACQ-WINDOW-GATING-DECOUPLE`) was created the same
governance cycle and, per its own `status: "implemented"`, is done.

An independent foreground agent re-verified all of this from raw files (exact line numbers, exact
quoted JSON) before this artifact was drafted, and a second, cross-model (fable) red-team pass
re-verified it again after drafting. Both confirm.

**Why the false premise recurred.** This is not a one-off. The identical filename-grep-based
"829 has no autopsy" belief appears independently in at least three other places, spanning four
days:

- **GFLAG-0084** (raised 2026-08-28, session `thought-digestion-v3closure-20260828`): "V3-EXQ-829
  (a FAIL) has no failure_autopsy artifact -- verified 2026-08-28."
- **`docs/architecture/mech_317_absorption_check.md`**, "Separable, and better lifted out than
  cycled with the merge" section (written 2026-09-01, the same day as this chip): "V3-EXQ-829's
  missing autopsy -- a `/failure-autopsy` routing question... the autopsy is largely
  transcription."
- **`evidence/planning/substrate_queue.json`**'s `mech324-reacquisition-window-isolation` entry
  (renamed from the colliding `SD-083` today, session `sd083-collision-20260901`): "The V3-EXQ-829
  failure autopsy the old gate named is still genuinely owed and is now chipped as
  chip-20260901-v3exq829-failure-autopsy" -- literally the dispatch instruction behind this
  session.

None of these four artifacts (the three above, plus this chip's own dispatch brief) ran
`check_autopsy_coverage.py`. All four independently reconstructed the same false negative by
grepping filenames instead.

**What is actually owed**, and what this artifact adjudicates instead: **V3-EXQ-829a** --
the successor run that validates the substrate fix -- has never been autopsied, and its own
manifest carries a genuine, previously-uncaught anomaly (Section 2 below). The
`governance_flag_triage_20260901.md` Part 2 "MECH-317 absorption" cluster brief and the
`mech324-reacquisition-window-isolation` substrate entry's own 2026-09-01 status note both
already *name* this anomaly correctly (829a's `criteria_non_degenerate.C2 = False`) -- but
neither is a confirmed `/failure-autopsy` adjudication, and neither corrects the repeated false
"829 has no autopsy" belief. This artifact is that adjudication, retargeted to the run that
needs it, plus the correction.

---

## 1. Facts -- V3-EXQ-829a

- **Run:** `v3_exq_829a_mech324_rapid_reacquisition_window_isolation_fix_20260801T062510Z_v3`,
  ran 2026-08-01 on `ree-cloud-2` (per its manifest), `experiment_purpose: evidence`,
  `outcome: PASS`, top-level `non_degenerate: true`, `dry_run: null` (confirmed via
  `scripts/check_dry_run_citations.py`, 0 dry hits across both 829 and 829a).
- **Script:** `ree-v3/experiments/v3_exq_829_mech324_rapid_reacquisition_falsifier.py`, reused
  as-is per the substrate entry's own recommendation, with `use_reacquisition_window_isolation`
  now toggled ON in the ON arms.
- **Queue entry:** `V3-EXQ-829a`, `supersedes: V3-EXQ-829` (per claims.yaml's "Validation
  experiment V3-EXQ-829a queued (supersedes V3-EXQ-829)" note).
- **Self-route label:** `reacquisition_window_isolation_fix_confirmed`. Per the skill's own
  standing rule, this is a hypothesis, not a verdict -- it is exactly what this autopsy exists
  to check.

### Six criteria, and the one that breaks

| Criterion | Load-bearing | `passed` | `criteria_non_degenerate` | Read |
|---|---|---|---|---|
| C1 reacquisition faster than acquisition | yes | true | **true** (per manifest) | Manifest says clean, but see below -- **this autopsy's own finding**: partially tautological, same class as C2. |
| C2 reacquisition scales with f_reacq | yes | true | **false** | **DEGENERATE.** Arithmetic identity. |
| C3 retention discriminates erasure | yes | true | true | Genuine, unaffected by the fix. |
| C4 short-window scaling | no | true | true | Genuine, non-load-bearing. |
| C5 isolation-on faster than isolation-off (paired) | no | true | true | **Genuine, the real signal.** |
| C6 isolation-off reproduces 829's flat signature | no | true | true | Genuine internal-consistency check. |

**C2, independently recomputed from raw `arm_results`** (not trusted from the manifest's own
summary): across all 24 isolation-ON W=100 cells and all 24 isolation-ON W=30 cells (6 seeds x 4
f_reacq values x 2 windows), `r_reacq` equals `ceil(R_min * f_reacq)` **exactly, with zero
variance, in every single cell**:

| f_reacq | r_reacq (isolation ON, every seed) | forced_bar = ceil(20 * f_reacq) |
|---|---|---|
| 1.0 | 20 | 20 |
| 0.5 | 10 | 10 |
| 0.25 | 5 | 5 |
| 0.1 | 2 | 2 |

`scaling_rho_iso_on_w100 = scaling_rho_iso_on_w30 = 0.9999999999999998`, and the manifest's own
`all_iso_on_cells_sit_on_forced_bar: true` confirms this is not a coincidence of the summary
statistic. **This is why the criterion is degenerate**: once the dissolution-scoped counter
(the fix) is reading the right window, and the variance/mean gates on that window clear well
before the repetition count does (true in this synthetic harness), the counter necessarily fires
the instant it reaches its own threshold. Spearman rho against a value that is *by construction*
a deterministic function of its own predictor is 1.0 whatever the true underlying process is --
the test cannot discriminate "the counter correctly counts to threshold" (guaranteed) from "the
biological rate this threshold models is validated" (the actual open question).

**Control that this reading is real, not an artifact of a bad summary function**: the isolation-OFF
arms in the *same* run read `median_r_reacq = 90` at every f_reacq (reproducing 829's own flat
signature, C6) -- i.e. they do **not** sit on the forced bar. The isolation-ON tautology is
specific to the fixed read path, not a property of how the metric is computed in general.

**C1's own tautology, found only by this autopsy's cross-model red-team pass, not by the
manifest's own degeneracy check**: `r_acq_form` (median repetitions to first acquisition) reads
exactly `20` (= `R_min`) with **zero variance across all 108 arms in the manifest**. So "r_reacq
(2/5/10/20) < r_acq_form (20)" is true purely because `r_acq_form` is pinned at `R_min` by the
same harness convention that pins C2's forced bar -- not an independent finding that
reacquisition is faster than acquisition in any sense beyond arithmetic. The manifest's own
`criteria_non_degenerate.C1 = true` does **not** catch this; it is this autopsy's own addition,
surfaced rather than silently deferred. C1's only genuinely informative content (gates clear
before the count binds) duplicates C5.

**C5 is therefore the load-bearing genuine signal in this run**: a paired within-cell comparison,
isolation ON (r_reacq=5 at f=0.25) vs isolation OFF (r_reacq=90 at the same f, same seed) --
this is a real measurement, not a tautology, and it is what actually demonstrates the substrate
fix changes behaviour in the direction the fix was designed to produce.

---

## 2. Claim-layer mapping

Both claims were already fully mapped by V3-EXQ-829's own confirmed autopsy
(`failure_autopsy_2026-07-28-sweep.json`) -- see its target for `run_id: v3_exq_829_...` for the
full claim text, `claim_type`, `depends_on`, prior counts, and the pre-829 lit basis. Not
re-derived here; 829a adds no new claim-layer information, only a new (partial) evidence data
point.

- **MECH-323** (formation operator): unaffected by 829a beyond a reconfirmation of C3. 829's own
  `supports` disposition stands.
- **MECH-324** (maintenance/dissolution operator, rapid-reacquisition prediction): 829's own
  `weakens`-on-the-specific-rate-claim disposition (per-claim, see Section 4 below) is **not
  overturned** by 829a -- 829a does not re-test the rate-scaling prediction with a real
  measurement, it only confirms the counter-level fix works (C5) and reconfirms retention (C3).

---

## 3. Biological-reference triage

Unchanged from V3-EXQ-829's own autopsy. Closest reference mechanisms: striatal ensemble
re-emergence on reacquisition (Barnes 2005) and renewal/resurgence/rapid-reacquisition as
retention-not-erasure signatures (Bouton 2012). Both sources ground the *direction* (faster than
acquisition) but neither quantifies a rate, and both come from paradigms with sleep *between*
real trials -- a transfer-limit caveat already registered on MECH-324, load-bearing, and not
touched by this run. No new literature engaged by 829a; it is a pure instrument-validation run,
not a biology-facing one.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (fix) / unclear (MECH-324's own rate prediction) | The fix is confirmed correct; the claim's own quantitative sub-prediction remains untested. |
| Biological reference | clear, same transfer-limit caveat as 829 | No new lit engaged. |
| Prerequisites | unchanged | Offline sleep-replay consolidation (MECH-322) remains a candidate missing prerequisite, deliberately unexercised. |
| Implementation | complete for the fix itself | `use_reacquisition_window_isolation` (ree-v3 7747a01) confirmed correct via C5. |
| Environment | adequate | n/a -- isolated operator-level test, same design class as 829. |
| Measurement | **under-instrumented for C2 specifically** | C2 cannot discriminate a tautology from real evidence; needs a redesigned criterion. |
| Integration | isolated by design | Correctly so, matching 829's own justification. |
| Scale | adequate | 6 seeds, both windows, both isolation settings. |

**Failure-location summary (GOV-FAILLOC-1), applied to the C2 anomaly specifically:**

- Mechanism: **established** (the substrate fix is genuinely correct, per C5).
- Measures: **not established** (C2 cannot discriminate tautology from evidence).
- Environment: **established** (isolated test design is appropriate for what it's testing).
- REE FAILED: **false** -- only the Measures bucket is implicated. This is a test-design gap on
  one criterion inside an otherwise-successful instrument-validation run, not a REE-level failure
  on any axis.

---

## 5. Review-tracker discrepancy -- resolved

**The question, as posed to this autopsy:** review_tracker.json's 2026-07-29T23:24:03Z
review_log note reads "MECH-324 weakens" (`V3-EXQ-829, mixed, split per-claim`), while the
manifest's own `evidence_direction` / `evidence_direction_per_claim.MECH-324`, and the sweep
autopsy's `recommended_evidence_direction_per_claim.MECH-324`, all read `"mixed"`. Which is
right?

**Resolution: both are correct at different granularities, and "weakens" is the more precise
value for MECH-324 specifically** -- it is what governance actually wrote into MECH-324's own
`evidence_quality_note` in claims.yaml: *"Weakens the specific rate claim; does not weaken the
retention-vs-erasure structure (see MECH-323, supports)."*

**Why the manifest's per-claim field reads differently:** the manifest's
`evidence_direction_per_claim` is a labeling artifact, not a true per-claim split. MECH-323
correctly gets its own distinct value (`supports`), but MECH-324's slot simply echoes the
run-level `"mixed"` value rather than reading `"weakens"`. `"mixed"` is an accurate description
of the *run as a whole* (support for one tagged claim, falsification for the other), but it is
not the correct per-claim characterization of MECH-324's own evidence. The sweep autopsy's own
JSON `recommended_evidence_direction_per_claim` inherited this same imprecision (copied the
manifest's map verbatim) even though its own *prose* is precise throughout ("falsifies
MECH-324's specific rapid-reacquisition rate prediction... in the wrong direction"). Governance
applied the prose reading, not the JSON field, when writing MECH-324's claims.yaml note --
review_tracker's "MECH-324 weakens" shorthand mirrors what was actually applied.

**No claims.yaml change owed from this finding** -- already correctly applied. Flagged as a minor
process note: an autopsy's per-claim JSON field should carry that claim's *own* direction, not an
echo of the run-level value, when they differ.

---

## 6. What 829a changes, and what it doesn't

**Confirmed genuine (non-degenerate) by this run:**
- The `use_reacquisition_window_isolation` substrate fix works as designed (C5).
- MECH-323's retention-with-dormancy structure reconfirmed (C3).

**NOT confirmed by this run, despite `outcome: PASS` and a clean-reading self-route label:**
- MECH-324's own quantitative rate-scaling prediction (`r_reacq` scales measurably with
  `f_reacq`) -- C2 is uninterpretable by construction.
- claims.yaml's current 2026-08-01 governance note on MECH-324 -- *"the queued validation
  experiment ran and confirms the use_reacquisition_window_isolation fix works as designed --
  clean PASS, no anomalies"* -- is **not accurate**. The fix-works-as-designed half is right
  (and reconfirmed here via C5); "no anomalies" is not.

**Net effect on MECH-324's disposition:** none. The claim's quantitative rate prediction remains
exactly where V3-EXQ-829 left it -- neither newly weakened (829a's isolation-ON arms do not
reproduce 829's flat-signature defect) nor genuinely supported quantitatively (C2 cannot bear
that weight). What changes is that the record should say so explicitly, rather than reading
"clean PASS, no anomalies."

---

## 7. Recommended routing

**`/queue-experiment`**, for a redesigned MECH-324 rate-scaling validation (new EXQ number, or
829b at the drafting session's discretion) whose C2-equivalent criterion measures something the
fixed counter's own threshold does not mechanically determine. Two sketched options:

1. An independent downstream signal (behavioural latency, rollout cost) that should improve in
   proportion to `f_reacq` once the repetition threshold is reached.
2. A prediction compared against an *externally derived* rate rather than against the counter's
   own defining formula.

**Caveat, surfaced by this autopsy's cross-model red-team pass:** option 1 may itself be
instrument-gated. `substrate_queue.json`'s `mech317-action-chunk-boundary-instrument` entry
(registered 2026-09-01, `status: proposed_REGISTRATION_ONLY_not_a_build_authorisation`, unblocks
MECH-317/ARC-071) records that **no behavioural/action-stream DV currently exists anywhere in the
ARC-071/MECH-323/MECH-324 family** -- chunks form under agent control but nothing downstream
measures behaviour yet. The `/queue-experiment` drafting session should check whether that
instrument (or an equivalent) exists before committing to option 1; option 2 needs no new
instrument and is a viable first hop regardless.

**Re-derive brake:** does not fire. Mechanically checked over the full confirmed-autopsy corpus
via the R1-R3 counting convention: MECH-324 has exactly 1 ceiling-counting hit (an unrelated
V3-EXQ-810 readiness target), below the threshold of 2. Not that it would apply here regardless
-- this routes to a *redesigned* criterion, not a same-design retest.

**Granularity-debt recurrence trigger:** does not fire. `scripts/granularity_debt_cluster.py
MECH-324` reports 3 targets, alignment distribution `strengthened=2, unclear=1`, **no target
reads `weakened`** -- per the skill's own rule, this is measurement/implementation debt, not
granularity debt, regardless of the count.

**Per CLAUDE.md's failure-autopsy chip-reporting rule**, this artifact REPORTS the routing above
rather than spawning it; `/governance` chips the follow-on once it ratifies the recommendation
at its own Step 2b/4/6a walk.

---

## 8. GFLAG-0084 -- recommended resolution

**Recommend: resolved.** V3-EXQ-829 already has a confirmed, applied autopsy (Section 0). The
flag's premise ("no failure_autopsy artifact") was a filename-search false negative. The SD-083
collision half is independently resolved (renamed to `mech324-reacquisition-window-isolation`,
session `sd083-collision-20260901`, 2026-09-01) and its `DO_NOT_BUILD_YET` gate is confirmed
obsolete (the build landed 2026-07-31). The genuine open item the flag was gesturing at --
829a's degenerate C2 -- is now adjudicated here; see Section 7 for routing. V3-EXQ-834's
unmeasured growable-ceiling prediction (the flag's third bundled item) is out of scope for this
artifact and remains open; `mech_317_absorption_check.md`'s own "Separable" section already
recommends lifting it out independently.

This skill never edits `governance_flags.v1.json` -- recommendation only, for `/governance` to
apply.

---

## 9. Per-claim recommendation summary

| Claim | Direction | Category | Change |
|---|---|---|---|
| MECH-324 | supports (qualitative, via C5 -- not C1, see Section 1) on the direction; rate-scaling sub-prediction remains untested, per Section 6 | standard (unchanged) | STANDS on status/category/direction; append an evidence_quality_note addendum documenting 829a's genuine instrument validation (C5) and C2's degeneracy -- note-only |
| MECH-323 | supports (unchanged, reconfirmed by C3) | standard (unchanged) | STANDS; optional brief addendum, not required |

---

## 10. Adversarial verification record

Two independent verification passes were run against this artifact, both by agents that did not
share this session's reasoning:

1. **Pre-draft fact-check** (same model, foreground): independently recomputed CLAIM 1 (829's
   coverage), CLAIM 2 (829a's C2 arithmetic), and CLAIM 3 (no other autopsy targets 829/829a) from
   raw files. All three CONFIRMED.
2. **Post-draft red-team pass** (cross-model, `fable`, foreground): attacked the drafted routing
   and per-claim conclusions specifically. **Verdict: CONFIRMED, with 2 CONTESTED sub-points**,
   both incorporated into this artifact before finalisation:
   - C1 shares C2's tautology class (Section 1) -- the artifact originally read C1 as
     uncritically genuine; revised to lean on C5 instead.
   - The `/queue-experiment` routing may be partially instrument-gated on
     `mech317-action-chunk-boundary-instrument` (Section 7) -- routing note revised to name this
     dependency.

Neither contested point overturns the central finding (829 already autopsied; 829a's C2 is
genuinely degenerate; no claims.yaml disposition change is owed beyond a clarifying note).

---

## 11. Learning extracted

1. The `use_reacquisition_window_isolation` substrate fix (ree-v3 7747a01) is confirmed correct
   via a genuinely non-forced paired comparison (C5).
2. V3-EXQ-829a's own C2 criterion is degenerate by construction, in a way invisible to the
   manifest's top-level `non_degenerate` flag and to its own `adjudication` field (unset, since
   `experiment_purpose: evidence` PASSes are not routinely flagged) -- a new instance of the
   general class GOV-FAILLOC-1/GOV-DRY-1 guard against elsewhere, on the PASS side, for an
   unflagged evidence-purpose run, which is a shape the skill's own scoping rule (Step
   "before starting" 3) does not currently catch as a *mandatory* autopsy trigger.
3. The "V3-EXQ-829 has no failure_autopsy artifact" belief was independently reconstructed by at
   least three separate sessions/artifacts across 2026-08-28 through 2026-09-01, all via
   filename-based search rather than `scripts/check_autopsy_coverage.py`. This is a durable
   process-hygiene finding worth a governance mention: filename-grep is not a reliable
   "has this been autopsied" check.

---

## Session close

Staging mode -- this artifact is a draft. Per the skill, the Step 8 interactive gate and Step 9b
(hypothesis ledger) are both skipped (no `fanout_recommendation` is emitted; this is a
re-adjudication clarifying existing findings, not opening new live hypotheses to pre-register).
An interactive session or the next `/governance` walk should confirm the routing and the
GFLAG-0084 resolution above before either is applied.
