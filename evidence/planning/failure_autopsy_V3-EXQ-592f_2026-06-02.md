# Failure Autopsy: V3-EXQ-592f (MECH-090 commitment-state transition authority probe)

**Generated:** 2026-06-02T05:51:20Z
**Scope:** single
**Status:** confirmed (interactive gate cleared 2026-06-02)
**Autopsy session:** failure-autopsy-v3-exq-592f-20260602T055130Z
**Predecessor autopsy:** [failure_autopsy_V3-EXQ-592e_2026-06-01.md](failure_autopsy_V3-EXQ-592e_2026-06-01.md)

## 1. Target and facts

| Field | Value |
|---|---|
| Queue id | V3-EXQ-592f |
| Run id | `v3_exq_592f_mech090_commitment_state_transition_probe_20260601T194325Z_v3` |
| Manifest | `REE_assembly/evidence/experiments/v3_exq_592f_mech090_commitment_state_transition_probe_20260601T194325Z_v3.json` |
| Script | `ree-v3/experiments/v3_exq_592f_mech090_commitment_state_transition_probe.py` |
| Claim ids | `["MECH-090"]` |
| Experiment purpose | `diagnostic` (controlled state-machine probe, not ecological) |
| Supersedes | V3-EXQ-592e |
| Outcome | FAIL |
| Diagnostic outcome | `FAIL_NO_RELEASE_AUTHORITY` |
| Manifest evidence_direction | `does_not_support` |
| Machine | DLAPTOP-4.local |

592f was designed at the close of the 592e autopsy as a controlled state-machine probe.
It forces beta elevated + an E3 committed pointer + rv-low BEFORE perturbation, then
varies score_margin and nav_readiness while the real `REEAgent.select_action`,
real `BetaGate`, and real `CommitReadiness` run on top of a stubbed
`E3TrajectorySelector.select` that returns controlled `SelectionResult` objects.
The harness exercises whether failed readiness can SUPPRESS or RELEASE an
already-held committed state -- the autopsy-named bit 592e could not resolve.

### Per-stage observations (6 ticks per stage, single seed=42)

| Stage | forced score_margin | forced nav_readiness | beta_elev fraction | e3_pointer fraction | score_blocks delta | nav_blocks delta | release transitions |
|---|---:|---:|---:|---:|---:|---:|---:|
| A baseline | 0.10 | 1.00 | 1.00 | 1.00 | 0 | 0 | 0 |
| B score_fail | 0.01 | 1.00 | 1.00 | 1.00 | **0** | 0 | 0 |
| C nav_fail | 0.10 | 0.00 | 1.00 | 1.00 | 0 | **6** | 0 |
| D both_fail | 0.01 | 0.00 | 1.00 | 1.00 | **0** | **6** | 0 |
| E recovery | 0.10 | 1.00 | 1.00 | 1.00 | 0 | 0 | 0 |

Acceptance flags:

- **C1 forced baseline:** PASS (baseline beta_elev=1.0, pointer=1.0).
- **C2 score_margin release authority:** **FAIL.** Direct ticks below score_margin
  floor=6/6 in stage B, but suppression of beta/e3 occupancy is 0.0 and zero
  decommit transitions.
- **C3 nav_competence release authority:** **FAIL.** nav_blocks=6/6 in stage C
  (predicate IS firing), but suppression of beta/e3 occupancy is 0.0 and zero
  decommit transitions.
- **C4 conjunction authority:** **PASS, but vacuously.** The criterion is
  `d_supp.max_drop >= max(b_supp.max_drop, c_supp.max_drop)`. Since every
  suppression value is 0.0, the inequality holds at 0 >= max(0, 0). This is a
  no-suppression-equals-no-suppression PASS; the diagnostic_outcome correctly
  ignores it because C2 AND C3 AND C5 are all FALSE. **Flag for script-design
  fix:** C4 should require d_supp.max_drop strictly POSITIVE (or at minimum
  greater than zero) so it cannot pass under a globally zero-suppression regime.
- **C5 recovery:** FAIL with `note: "not_evaluable_no_prior_suppression"`.
- **C6 no-vacuity:** PASS (forced inputs actually crossed thresholds where intended).

The decisive cell-level facts:

- Stage B: forced score_margin=0.01 (below floor 0.05). Direct readout shows
  6/6 ticks below floor. Yet `BetaGate.mech090_n_elevation_blocked` did NOT advance.
- Stage C/D: nav_blocks DID advance 6 per stage. The CommitReadiness predicate
  is being consulted -- it just has no release authority.
- All five stages end with `final_beta_elevated=true` and
  `final_e3_committed_pointer_present=true`. No transition counter ever ticked.

## 2. Mapping to the 592e autopsy hypothesis

The 592e autopsy (Section 2) named the precise mechanism:

- `BetaGate.should_admit_elevation()` is the score-margin block counter site,
  and in bistable mode `REEAgent.select_action()` only calls it under
  `result.committed and not beta_gate.is_elevated`. With beta forced ALREADY
  elevated in 592f stages B/D, the admission path is bypassed, so score_blocks
  never advances even though the input crosses the floor. **Exact match.**
- `CommitReadiness.is_above_floor()` is AND-composed into the elevation call.
  When below the floor it increments `n_blocks_emitted`, but it never calls
  `beta_gate.release()` and never clears `e3._committed_trajectory`. With beta
  forced ALREADY elevated in 592f stages C/D, the block counter rises 6 per
  stage but state occupancy is untouched. **Exact match.**

592f's controlled probe is therefore the structural confirmation 592e called for.
The hypothesis "predicates fire, but lack causal authority over already-held
commitment state" is no longer indirectly inferred from a degenerate behavioural
manifest; it is directly observed under forced state.

## 3. Claim-layer mapping -- what was tested vs what the claim asserts

| Claim | Status | Notes |
|---|---|---|
| MECH-090 base claim ("BG-level beta gates E3->action-selection propagation, not E3 internal updating") | INTACT | Not tested by 592f and not weakened. EXQ-049e remains the canonical PASS (MECH-090 fully confirmed). 592f did not exercise the propagation gate semantic. |
| MECH-090 bistable latch implementation_note (2026-04-10) | INTACT | Bistable gate elevated correctly; release on completion / urgency interrupt / V_s anchor remain the live release paths and were not exercised here. |
| MECH-090 R-c commit-entry readiness conjunction implementation_note (2026-05-28 / 2026-05-29) | **PARTIALLY FALSIFIED at the reach claim, INTACT at the substrate claim.** The substrate IS wired (score_margin gate + nav_competence EMA both produce diagnostic deltas under controlled forcing). The implicit reach -- that the same R-c gates can govern MAINTENANCE / RELEASE of an already-held committed state -- is NOT supported by the 592f probe. The 592e autopsy already flagged this; 592f converts the inference to a controlled measurement. |
| commitment_closure_plan.md GAP-4 substrate readiness | INTACT for admission side; OPEN for maintenance/release coupling. The substrate_queue entry sd_id=MECH-090 (status=substrate_landed_validation_v3_exq_592d_queued) correctly notes the admission-axis scope. |

`claim_ids=["MECH-090"]` on the manifest is accurate: 592f directly exercised
the MECH-090 R-c integration path. No tag drift from a predecessor.

## 4. Biological-reference triage

Closest reference systems: BG / STN beta gating (Cisek & Kalaska 2010,
Hanes & Schall 1996, Roesch / Calu / Schoenbaum 2007 -- the R-c lit-pull
anchors); descending inhibitory release paths (hippocampal completion via
ARC-028 / MECH-105 = Lisman & Grace 2005 subiculum->NAc->VP->VTA loop;
STN burst urgency interrupt MECH-091; V_s anchor invalidation as a
contextual-reset analog).

The biology is unambiguous on one architectural point: **action initiation
gates and motor-program maintenance/cessation gates are distinct neural
substrates in real brains.** D1/D2 direct/indirect-pathway BG circuits
initiate; STN beta sustains; sequence-end signals from hippocampal
completion + cortical PE-spike + STN urgency-burst drive cessation. The
admission predicate is not expected biologically to perform the release
function. So an admission-only R-c integration is not biologically wrong;
it is biologically faithful but architecturally incomplete -- the
expected release substrates (some of which ARE already wired) need
either (a) explicit coupling to readiness-failure-while-elevated, or
(b) the user-facing acceptance that release lives only in
hippocampal-completion / urgency / V_s anchor / SD-034 closure paths
and readiness predicates are deliberately admission-only.

`lit_status: present` for the R-c reading (Pull at
`evidence/literature/targeted_review_connectome_mech_090/synthesis.md`,
commit 9e68c5ca8a 2026-05-28; verdict R-c strongest). No anchor in that
synthesis claims the SAME readiness predicates serve release authority --
release-side anchors are different (Lisman & Grace 2005, Foster & Wilson
2006). The current substrate is biologically consistent at the admission
axis; the gap is not biology divergence but architectural completeness.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | strengthened (substrate axis) / partial (reach axis) | MECH-090 R-c is correctly admission-only per implementation. The "could readiness drive release too?" question is now resolved negative under controlled forcing. |
| Biological reference | clear | Admission gates and release gates are biologically distinct. Admission-only R-c is biologically faithful; current release paths cover sequence completion / urgency / context invalidation. |
| Prerequisites / dependencies | present at admission; not exercised for maintenance | All R-c admission machinery wired (BetaGate.should_admit_elevation + CommitReadiness.is_above_floor + AND composition in agent.py). |
| Implementation completeness | partial | Readiness-failure-while-elevated has no release-side consumer. nav_blocks counter rises and is wasted (no action taken on a positive block count). |
| Environment adequacy | adequate by construction | Controlled state-machine probe; ecological env not required. |
| Measurement adequacy | adequate at most cells; C4 vacuous-PASS noted | Direct gate inputs, official counters, state-occupancy, and transition counts all surfaced. C4 acceptance criterion should require strictly positive d_supp.max_drop. |
| Integration adequacy | admission-coupled, maintenance-not-coupled | The interface between readiness predicates, BetaGate latch state, and E3 committed-pointer state is precisely where the gap lives. |
| Scale / capacity | adequate | 5 stages x 6 ticks is the right granularity for a state-machine probe. |

Recommended `epistemic_category`: **substrate_ceiling** at the reach axis (the
current substrate cannot deliver readiness-driven release; this is a
substrate-enrichment matter, not a claim demotion); the substrate at the
admission axis remains `standard` and continues to ride the
V3-EXQ-592d 4-arm validation cycle.

## 6. Cluster pattern (none required)

592f is a single-target controlled probe authored as the 592e autopsy's
next step. No cluster scope. The wider 490g / 591 / 603 family operate on
different claims (Q-045 / MECH-313 / MECH-260 / INV-074 / ARC-046 / MECH-307
goal-pipeline; see those autopsies). The 592 lineage (592 -> 592b -> 592c
-> 592d (queued) and 592e -> 592f) is structurally insulated from those.

## 7. Learning extracted

**Architectural finding (load-bearing):** MECH-090's current R-c integration is
admission-side only. The two readiness predicates (score_margin via
`BetaGate.should_admit_elevation` and nav_competence via
`CommitReadiness.is_above_floor`) both fire and produce diagnostic counter
movement, but neither has been wired to call `beta_gate.release()` or
`agent.e3._committed_trajectory = None` when failure occurs WHILE the agent
is already in a committed state. The 592e autopsy's read is correct, and is
now backed by direct controlled measurement.

**Two architectural responses are coherent (decision is the user's):**

(a) **Add an explicit readiness-failure-while-elevated release coupling.**
When `beta_gate.is_elevated` AND readiness predicates fail for K consecutive
ticks (Schmitt hysteresis to avoid chatter), call
`beta_gate.release()` and clear the E3 committed pointer. This makes R-c a
two-sided gate (admission AND maintenance), at the cost of adding a new
release pathway in parallel to hippocampal-completion / urgency-interrupt /
V_s anchor / SD-034 closure. Smallest substrate change to address the gap
directly.

(b) **Accept admission-only R-c as the architectural commitment.** Document
that readiness-failure-while-elevated is by design NOT a release trigger;
release authority lives only in the four existing pathways above. Audit
those pathways to ensure they cover the scenarios where readiness failure
mid-commitment matters (in particular: does hippocampal-completion fire
when the agent is stuck mid-program with degraded readiness? does V_s
anchor invalidation activate when nav_competence has been low for many
ticks?). If yes, the architecture is complete and the apparent gap is
mis-routed expectation. If no, sub-pathway gaps are flagged for separate
substrate work.

**Script-design tweak (script-design level, not architectural):** the
C4 conjunction-authority criterion as written admits a vacuous PASS on
identically-zero suppression. Successor scripts (if any) should require
`d_supp.max_drop > 0` AND `d_supp.max_drop >= max(b_supp, c_supp)`.

**No new lit-pull commission required.** The R-c lit synthesis is fresh
(2026-05-28) and the architectural distinction between admission and
release gates is well-anchored in the BG / STN / hippocampal literature
that synthesis already cited. The architectural choice (a vs b above) is
a REE-internal design decision, not a literature-pending question.

## 8. Recommended routing

`implement-substrate` AMEND on the existing MECH-090 substrate_queue entry
(`sd_id: MECH-090`, line 3407 of substrate_queue.json, status
`substrate_landed_validation_v3_exq_592d_queued`). Add a 592f
failure_record entry confirming admission-only integration. Update the
implementation_hint to surface the (a)/(b) architectural choice noted in
Section 7. Do NOT change `status` -- the existing V3-EXQ-592d behavioural
validation chain remains live for the admission axis; the
release-coupling decision is a separate workstream.

The recommended structured handoff entry (governance to materialise):

- action: `amend`
- target_sd_id: `MECH-090`
- new failure_record entry pointing at V3-EXQ-592f with metric
  "predicates fire under forced beta-elevated state but produce zero
  state-occupancy suppression (b/c/d_supp.max_drop = 0.0); diagnostic
  outcome FAIL_NO_RELEASE_AUTHORITY" and target "either add release
  coupling on readiness failure (option a) OR document admission-only
  scope and confirm existing release pathways cover degraded-readiness
  scenarios (option b)".

**`pending_retest_after_substrate`:** TRUE for the implicit reach claim
that R-c readiness predicates govern maintenance / release. FALSE for the
admission axis (V3-EXQ-592d remains the active validator there).

**Recommended evidence_quality_note draft** (governance to apply if accepted):

> V3-EXQ-592f (2026-06-01, controlled state-machine probe; supersedes
> V3-EXQ-592e; FAIL_NO_RELEASE_AUTHORITY): with beta forced already
> elevated and E3 committed pointer forced present, forced
> score_margin=0.01 (below floor 0.05) and forced
> nav_readiness=0.0 (below floor 0.3) produce zero state-occupancy
> suppression and zero decommit transitions across stages B/C/D. nav
> readiness predicate IS consulted (n_blocks_emitted advances 6 per
> stage in C/D); score_margin admission gate is bypassed because beta is
> already elevated (this is the current bistable-branch design). C4
> conjunction-authority returns PASS vacuously (0 >= max(0, 0));
> diagnostic outcome correctly ignores it because C2 AND C3 AND C5 FAIL.
> NOT a falsification of MECH-090 base claim (beta-gates-propagation-not-
> internal-updating remains intact, EXQ-049e PASS preserved). NOT a
> falsification of the R-c admission integration (V3-EXQ-592d retains
> its 4-arm validation scope on the admission axis). IS a controlled-
> measurement confirmation of the 592e autopsy's read that current R-c
> integration is admission-only -- the same readiness predicates that
> guard entry do not currently couple to beta_gate.release() or
> e3._committed_trajectory clearing when failure occurs while the agent
> is already committed. Architectural choice routed to implement-
> substrate AMEND on the MECH-090 substrate_queue entry: option (a) add
> a readiness-failure-while-elevated release coupling, or option (b)
> document admission-only as the architectural commitment and audit
> hippocampal-completion / urgency-interrupt / V_s anchor / SD-034
> closure pathways for coverage of degraded-readiness scenarios.

## 9. Interactive gate (Step 8) -- user decisions captured

The user cleared Step 8 via AskUserQuestion 2026-06-02. Confirmed decisions:

1. **Architectural response: option (b) admission-only + audit.** Document
   admission-only as the architectural commitment for MECH-090 R-c. Hand off
   to `/implement-substrate` an AMEND on the existing MECH-090 substrate_queue
   entry whose implementation_hint surfaces a follow-on audit of the four
   existing release pathways (ARC-028/MECH-105 hippocampal-completion,
   MECH-091 urgency-interrupt, V_s anchor invalidation, SD-034 closure
   operator) for coverage of degraded-readiness scenarios. Option (a) -- a
   new R-c-level release coupling -- is explicitly NOT taken; if the audit
   surfaces a coverage gap, that gap is registered as separate substrate
   work on the relevant pathway's entry, not on MECH-090's.
2. **Evidence direction: `non_contributory` + `pending_retest_after_substrate=true`.**
   Governance to re-tag the 592f manifest from `does_not_support` to
   `non_contributory` with epistemic_category `substrate_ceiling` at the
   reach axis. Substrate context (a/b above) is what determines whether
   the reach question becomes retestable; the manifest's current
   `does_not_support` tag understates the substrate-ceiling read.
3. **C4 vacuous-PASS tweak: in-place script patch via `/queue-experiment`.**
   The user chose to harden the C4 criterion on the existing 592f script
   (`require d_supp.max_drop > 0 AND d_supp.max_drop >= max(b_supp.max_drop,
   c_supp.max_drop)`) so the script is correct for any future re-run.
   The mandatory-skill-path rule in REE_Working/CLAUDE.md requires that
   experiment-script edits go through `/queue-experiment` (or
   `/diagnose-errors`); this autopsy does NOT edit the script. Routed
   as a `/queue-experiment` follow-on (no behavioural EXQ-592g currently
   planned; the patch lands either standalone as a script-hardening
   follow-on or bundled with any future state-machine probe in this
   lineage if one is ever queued).
