# Failure autopsy -- V3-EXQ-946 (ContextMemory write-ADDRESS informativeness, real-agent)

**Generated:** 2026-08-25T18:13:06Z
**Scope:** single
**Status:** `confirmed` 2026-08-25T18:30:37Z (Step 8: user confirmed all three recommended
dispositions verbatim -- see Section 11).

**Companion:** `failure_autopsy_V3-EXQ-946_2026-08-25.json`

**Session:** `autopsy-946-serene-yalow`

Claim-free diagnostic PASS, adjudication `vacuous_pass`. Per the skill's 2026-08-07
correction, a clean or flagged diagnostic PASS both require this skill. Central
question, doubled here: (1) did the PASS hold for a real reason or a degenerate one,
and (2) is the mechanical `vacuous_pass` flag itself correct?

`targets[]` covers ONLY
`v3_exq_946_contextmemory_write_address_informativeness_diagnostic_20260823T075019Z_v3`.
This is the direct sibling of the confirmed `failure_autopsy_V3-EXQ-943_2026-08-21`
(occupancy) -- read together, not merged; 943's `targets[]` is not retargeted.

Two prior planning documents already carry substantial analysis of this exact run
and were read in full before this diagnosis: `mech152_measurement_redesign_gated_20260818.md`
(+ its 2026-08-25 amendment) and `mech152_writepath_addressing_probe_20260825.md`. Both
explicitly name this autopsy as the owed next step before the human call on MECH-152's
gate. This artifact **is** that step.

---

## 0. Gates run before any metric was read

| Gate | Result |
|---|---|
| Already-done check (`check_autopsy_coverage.py`, content match) | AVAILABLE YES. 0 artifacts cover this queue_id or run_id. |
| `check_dry_run_citations.py` | **0 dry cited, 0 dry in named families, 0 ambiguous, 1 clean, 0 unknown**, exit 0. Manifest `dry_run` absent/null. |
| `validate_recording.py --paths <manifest>` | **1 complete, 0 always-core gaps.** `recording_schema rec/v1`, `substrate_hash`, `config`, `seeds`, `machine`/`machine_class`, `elapsed_seconds` all present. |
| `validate_experiments.py --checks dry_run_unreachable_criterion` | This driver not in the 11-warning list (all `v3_exq_543` b-l). |
| Re-derive brake | N/A (`claim_ids: []`). Fired false. |
| Granularity-debt trigger | Does not fire (no tagged claim). |
| `autopsy_pre_routing_checks.py` (Step 7b) | 0 fires. C1/C2/C3 inapplicable (claim-free). See Section 7. |

Ran to completion (`outcome: PASS`, `fatal_error_count: 0`). Not a `/diagnose-errors` target.

---

## 1. Facts

`v3_exq_946_contextmemory_write_address_informativeness_diagnostic_20260823T075019Z_v3`
PASS | `experiment_purpose: diagnostic` | `claim_ids: []` |
`ree-worker-1`, `linux-x86_64-py3.10-torch2.12.0+cpu` | 211.72 s |
seeds `[42, 7, 13, 100, 200]` |
`substrate_hash e70ac4d5737cee98...` | `substrate_commit b0840f463bc4` dirty false |
`evidence_direction: non_contributory` (self-stamped) |
self-route `context_informative_address_found_at_operating_point` |
**adjudication: `vacuous_pass`** (see Section 6 -- disputed).

Queue entry absent from live `experiment_queue.json` (completed items removed).
Driver: `ree-v3/experiments/v3_exq_946_contextmemory_write_address_informativeness_diagnostic.py`
(1090 lines).

**Why this run exists.** V3-EXQ-943 (PASS, confirmed autopsy 2026-08-21) validated write
*occupancy* under a real agent for both landed write-address fixes but explicitly did not
test whether the resulting address carries information about *context*. Governance's own
substrate_queue entry `contextmemory-write-path-addressing-degeneracy` records this gap.
946 is purpose-built to close it.

**The methodological trap this driver is built to avoid**, stated in its own docstring: a
least-recently-used clock or a period-(k+1) cycle can produce non-zero mutual information
purely from period *alignment* with the context-block schedule -- the artifact-as-verdict
error that cost this lineage six generations (V3-EXQ-436..436f) and got both of INV-044's
V3-EXQ-429 entries withdrawn (2026-08-22). The load-bearing gate is therefore not "MI
exceeds chance" but "MI exceeds an **order-only null**": the same write sequence with
context labels permuted *blockwise* (block structure/autocorrelation preserved, only the
safe/dangerous assignment broken). An order-driven address produces identical MI under
this permutation; only a genuinely context-sensitive address shows excess.

**Design.** 4 arms x 5 seeds = 20 cells. BIAS swept over `write_usage_bias_weight` in
{1.0, 0.1, 0.01} (weakening the usage/conscience term relative to the content term, to ask
whether content-dependence survives when unmasked). REFRACTORY run once at k=2 (not
crossed with bias_weight -- the parameter is provably unread on that path; crossing would
have produced bit-identical cells, the same DV-symmetry degeneracy class as V3-EXQ-604c).
Same 436-family CausalGridWorldV2 + REEAgent harness as V3-EXQ-943, `sd016_writepath_mode
= "sense_only"`, no sleep loop.

**P0 (instrument validation, independently recomputed from the manifest's own
`interpretation.preconditions`):**

| Precondition | Measured | Threshold | Direction | Met |
|---|---|---|---|---|
| `mi_null_test_detects_positive_control` | z=40.189 | >=5.0 | lower (floor) | true |
| `mi_null_test_rejects_negative_control` | z=-0.269 | <=2.0 | upper (ceiling) | true |
| `writepath_engaged_every_cell` | 2933 writes | >=200 | lower (floor) | true |

Both instrument controls hold with wide margins (8x and 7x respectively), verified in the
driver's own comments as numerically checked at authoring time, not merely asserted. This
recomputes correctly from the manifest's `interpretation.preconditions[]` array.

**Per-arm load-bearing criterion (recomputed from `metrics.n_seeds_clearing_null_*` and
cross-checked against `arm_results[].z_vs_null`):**

| Arm | bias_weight | seeds clearing (z>=2.0) | z range | observed MI range (bits) |
|---|---|---|---|---|
| BIAS_W1_0 | 1.0 (default) | **5/5 -- PASS** | 2.19 - 7.73 | 0.00022 - 0.00058 |
| BIAS_W0_1 | 0.1 | **3/5 -- PASS** (thin: one seed z=0.39) | -0.29* - 7.97 | 0.00029 - 0.00059 |
| BIAS_W0_01 | 0.01 | 1/5 -- FAIL | -1.83 - 19.52 | 0.00005 - 0.04392 |
| REFRACTORY | n/a (unread) | 2/5 -- FAIL | -1.08 - 4.86 | 0.0000061 - 0.01709 |

*BIAS_W0_1 z-values recomputed: [1.2477, 3.0280, 7.9661, 0.3948, 5.4727] -- 3 of 5 clear
2.0, matching `n_seeds_clearing_null_BIAS_W0_1: 3` exactly.

Overall `outcome = PASS` because the driver's own semantics is `any(per_arm_pass.values())`
-- an explicit, deliberate OR across the four arms ("this run found SOME operating point
with a context-informative address"). Read literally, the manifest's own docstring states:
*"FAIL means no operating point tested shows an address exceeding the order-only null
anywhere -- itself the informative, falsifiable answer... not an experiment failure."* The
symmetric statement holds for PASS: it means *some* operating point does, not that the
write-address mechanism *in general* is now context-informative.

**z_goal_stream:** `ticks_total 0`, `writer_calls 0`, `writer_defect null`,
`goal_state_present false`, `n_agents 20`. Expected -- no goal-using agent, no criterion
depends on z_goal.

**Recomputed cross-check (independent of the manifest's own arithmetic):** BIAS_W1_0's
`z_vs_null` for seed 42 = (0.0005837 - 0.0001321) / 0.0000794 = 5.687 -- manifest reports
5.689 (rounding only). Positive control: (1.0 - 0.016767) / 0.024465 = 40.188 -- manifest
reports 40.189. Both spot-checks reproduce the manifest's own arithmetic to 3-4 significant
figures; no computation-layer defect found.

---

## 2. Claim layer

`claim_ids: []` by design. The driver states this is a readiness/instrument diagnostic for
EVB-0628/INV-044, not evidence for or against any registered claim, and diagnostic runs
with `claim_ids: []` are excluded from governance confidence scoring by construction. No
claim is tested here; Section 8 covers read-across only.

---

## 3. Biological-reference triage

Same grounding as V3-EXQ-943 (identical mechanism, different DV): DeSieno 1988
frequency-sensitive competitive-learning conscience bias (BIAS arms) and a neuronal
absolute refractory period (REFRACTORY). Architecture doc
(`contextmemory_write_address_selection.md`) names both explicitly. Not a formal-definition
import. `lit_status: present`; no `/lit-pull` owed. The divergence already documented for
943 (occupancy-without-addressing at default BIAS weight is a global usage-EMA, not a
first-order neural property) carries forward and is sharpened here: even where BIAS *does*
carry a detectable context signal (W1_0, W0_1), the signal is a thin residual riding on top
of the dominant order-driven mechanism, not a redesigned context-sensitive addressing rule.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | claim-free |
| Biological reference | clear | DeSieno conscience bias; neuronal refractory. Divergence named, not a missing lit entry. |
| Developmental / dependency prerequisites | present | Both write-address fixes landed and engaged; P0 writepath-engaged met at 2933-3187 writes/cell. |
| Implementation completeness | partial | BIAS_W1_0/W0_1 carry a real-but-minute context signal (~0.02-0.06% of the instrument's own positive-control range). BIAS_W0_01 partially re-degenerates occupancy (4-14/16 slots vs 16/16, up to 7% self-repeat) -- moving back toward the original corrupting fixed point. REFRACTORY (pure content-argmin among eligible slots, no usage term) underperforms BIAS on this instrument. No tested operating point is a genuinely redesigned context-sensitive address rule; all are order/eligibility-dominated with a thin content residual. |
| Environment adequacy | adequate | 436-family harness, real agent, real z_world-derived state, writepath genuinely engaged. |
| Measurement adequacy | adequate | The strongest layer. Order-only blockwise-permutation null purpose-built against the exact six-generation artifact-as-verdict trap; instrument itself independently validated on synthetic controls with wide margins (8x, 7x), reproduced here to 3-4 sig figs. |
| Integration adequacy | isolated | Writes are a `sense()` side-effect; action selection never reads ContextMemory (write-call counts identical across arms per seed, as in 943). Not this diagnostic's question. |
| Scale / capacity | adequate | 16 slots, ~2933-3187 writes/cell, 40 blocks, 5 seeds/arm. |

**Failure-location (GOV-FAILLOC-1).** This is not primarily a "REE failed" narrative (the
run PASSed), but the triage still applies to avoid the mirror-image over-read ("REE
succeeded at context-sensitive write addressing"). Mechanism: `partial` (thin, non-monotone,
partially unstable signal). Measures: `established`/adequate. Environment: `established`.
Net classification: **MIXED** -- a real, instrument-validated, order-only-null-exceeding
signal exists at some operating points, but it is neither the magnitude nor the uniformity
that would license "REE succeeded" language, and the mechanism layer alone (not measurement
or environment) is why. Do not write that write addressing is fixed, and do not write that
it has failed -- both would overclaim past what this table supports.

---

## 5. Is the PASS real or vacuous, substantively?

**Real at two operating points, vanishingly small in magnitude, and not uniform or
monotone across the swept parameter.**

Real:

1. The instrument is genuinely well-built. Both synthetic controls hold with wide margins,
   independently recomputed here, and the order-only null construction is specifically
   designed against (and avoids) the exact artifact that produced false positives six times
   before in this lineage.
2. BIAS_W1_0 clears on 5/5 seeds with a z range (2.19-7.73) well clear of the 2.0 threshold
   -- not a borderline result.
3. The write-call counts and occupancy figures at BIAS_W1_0 (16/16, entropy ~4.0) match
   V3-EXQ-943's own BIAS finding exactly, confirming this is the same wiring under the
   same harness, not a different regime.

Vanishing / not uniform:

1. Observed MI at the two clearing arms is 0.0002-0.0006 bits against the same instrument's
   own 1.0-bit positive control -- roughly 0.02-0.06% of the detectable range. "Exceeds an
   order-only null with p<0.023" is a real statistical statement; "carries context usable by
   a downstream mechanism" is a different, much stronger claim this magnitude does not
   support on its own.
2. BIAS_W0_1 clears at *exactly* the required floor (3/5), with one seed (z=0.395)
   indistinguishable from the null. A single seed's outcome away from being 2/5 (a FAIL).
3. The seeds-clearing-null count is strictly monotonic *opposite* the driver's own
   hypothesis as bias_weight falls -- 5/5 (W1_0) -> 3/5 (W0_1) -> 1/5 (W0_01) -- with sharply
   increased per-seed variance at the lowest weight (z range -1.83 to 19.52, vs the tight
   2.19-7.73 at W1_0). BIAS_W0_01 -- the arm where the driver's own hypothesis predicts the
   *strongest* content signal (usage term weakest, content least masked) -- instead FAILS
   the 3/5 bar, and its
   occupancy partially collapses (4-14 of 16 slots, self-repeat up to 7.5%) toward the
   original single-slot corrupting regime. The one large z at this arm (seed 200, z=19.52,
   MI=0.044 bits) sits on a bank with only 14 occupied slots and highly uneven per-slot
   counts (from 0 to 261) -- consistent with a low-occupancy artifact rather than a clean
   content signal, though this instrument's own construction (blockwise permutation,
   40 blocks) should in principle be robust to occupancy skew. Flagged as a fragility, not
   resolved here.
4. REFRACTORY -- content-only addressing among eligible slots, with NO usage term at all --
   underperforms BIAS_W1_0 (2/5 vs 5/5) on this specific instrument. This is the opposite
   ranking from a separate synthetic depth-based probe run the same week
   (`mech152_writepath_addressing_probe_20260825.md`, which favours REFRACTORY on raw
   modulation depth). The two instruments disagree; per that probe's own explicit
   preference (real agent + validated order-only null beats a synthetic harness + the very
   MI-against-chance instrument this null was built to replace), 946's ranking should be
   weighted over the synthetic one, but the disagreement itself is evidence the addressing
   question is not settled by either alone.

**Net read:** the PASS establishes that *an* operating point clears a genuinely
well-validated statistical bar -- a first for this lineage -- but does not establish that
write addressing is now context-informative in any practically useful sense. Treating 946
as closing the write-path gate (as opposed to informing it) would repeat the category error
the V3-EXQ-922a autopsy caught for MECH-152's earlier FAILs: a scale-sensitive claim
adjudicated on a scale-invariant or magnitude-blind readout.

---

## 6. Is the `vacuous_pass` FLAG itself correct? -- disputed, and likely a false positive

The indexer's diagnostic-adjudication gate (`build_experiment_indexes.py`,
`_diagnostic_adjudication`) fires `vacuous_pass` under rule (3b) whenever an overall PASS
carries ANY criterion tagged `load_bearing: true` with `passed: false`. This run's
`interpretation.criteria[]` has exactly four entries, one per arm, **each individually
tagged `load_bearing: true`**:

```
C_BIAS_W1_0_exceeds_order_only_null   load_bearing=true  passed=true
C_BIAS_W0_1_exceeds_order_only_null   load_bearing=true  passed=true
C_BIAS_W0_01_exceeds_order_only_null  load_bearing=true  passed=false   <- fires (3b)
C_REFRACTORY_exceeds_order_only_null  load_bearing=true  passed=false   <- fires (3b)
```

Rule (3b) exists to catch a genuine failure mode -- the V3-EXQ-621a "aggregation-vacuity"
pattern, where an overall PASS rests on an unmet gate that was supposed to be necessary.
That is an **AND**-semantics failure mode: if a load-bearing criterion is the thing that
makes the PASS non-vacuous, and it fails, the PASS is indeed vacuous.

But this driver's own semantics, stated explicitly in its docstring and confirmed by
reading the source (`overall_pass = any(per_arm_pass.values())`), is a deliberate **OR**:
"Overall `outcome` is PASS iff AT LEAST ONE arm clears its bar (i.e. this run found SOME
operating point with a context-informative address)." Under OR-semantics, each individual
per-arm criterion IS meaningfully load-bearing *for its own arm's own conclusion*
("does BIAS_W0_01 show a context-informative address? -- no") without being load-bearing
*for the overall run's PASS/FAIL* the way an AND-combined criterion would be. The author's
`load_bearing: true` tag is doing double duty here -- marking "this is a genuine,
pre-registered, meaningful per-arm criterion" -- and the indexer's (3b) rule cannot
distinguish that from "this criterion's failure alone invalidates the overall PASS."

**This is a distinct failure mode from the join-mismatch class the indexer's own comments
already document four instances of** (branch-selector exclusion, V3-EXQ-783's criteria-tag
join, V3-EXQ-906's aggregate `_non_degenerate` licence, V3-EXQ-908's `arm::check`
convention) -- those four are all about a NAME/KEY-MATCHING mismatch between
`criteria_non_degenerate{}` and `criteria[]` in the indexer's legacy fallback path; this one
fires at rule (3b) itself, before the legacy path (and hence all four exclusions) is ever
reached, because (3b) has no representation of run-level AND-vs-OR combination semantics at
all. Confirmed by control-flow trace: (3b)'s `return label, "vacuous_pass"`
(`build_experiment_indexes.py:539`) is the only exit before the legacy path begins at line
543, so none of the four exclusions is even evaluated here. None of the four existing
exclusions cover "N independently load-bearing criteria combined by OR, no aggregate
criterion declared" -- and structurally cannot, since they never run. A hypothetical aggregate criterion
(`C_any_arm_exceeds_order_only_null`, `load_bearing: true`, `passed: true`) with the four
per-arm entries re-tagged `load_bearing: false` would have licensed exactly the same PASS
under the existing `_aggregate_cleared` mechanism (Section 5's `_non_degenerate`-suffix
licence is the closest existing analogue but does not literally match this driver's naming
or its non-`_non_degenerate` criterion names) -- but this driver did not author it that way,
because each per-arm criterion IS independently a real finding worth surfacing as
`load_bearing: true` in its own right (informative if it fails, per Section 5 above:
BIAS_W0_01 and REFRACTORY failing is itself informative about which operating points do
NOT carry a context signal).

A hypothetical retagging (per-arm criteria set to `load_bearing: false`, plus a new aggregate
`C_any_arm_exceeds_order_only_null` criterion tagged `load_bearing: true, passed: true`)
would license the same PASS -- but the mechanism that would license it is rule (3b) itself
(no `load_bearing:true`+`passed:false` entry remains to fire it), **not** the `_aggregate_cleared`/
`_non_degenerate`-suffix licence (`build_experiment_indexes.py:651-667`), which lives in the
legacy fallback path and is never reached once (3b) returns cleanly. Stated precisely because
it matters for how the follow-on fix (Section 9, item 3) gets scoped: the actual gap is that
(3b), at `build_experiment_indexes.py:532-539`, has no representation of run-level
combination semantics (AND vs OR) at all -- it is not a join-key mismatch like the four
documented sub-cases, so a fix modelled on those (another name/key-matching heuristic) would
likely miss it. The fix needs either an explicit aggregation-mode declaration the driver can
set, or (3b) itself needs to stop treating "some load_bearing criterion failed" as sufficient
without checking whether an aggregate criterion already accounts for it.

**Disposition: the flag is very likely a false positive for the run-level trust question**
(does this PASS clear a genuine gate on genuine evidence, at BIAS_W1_0/W0_1) but is
**directionally correct as a caution** in the coarser sense that it correctly signals "do
not treat this PASS as an unqualified, uniform success" -- which Section 5's magnitude
finding independently confirms is the right caution to attach, just for a different
(substantive, not mechanical) reason. Recommend: (a) governance treat this PASS's
BIAS_W1_0/W0_1 clearance as real for the addressing-informativeness question, subject to
the magnitude caveat in Section 5 -- do not let the mechanical flag alone block using this
evidence; (b) flag the indexer gap as follow-on engineering work -- **not** a join-mismatch
sub-case like the four documented ones (see above), and **not** performed by this autopsy,
which does not edit indexer code.

---

## 7. Step 7b -- mechanical pre-routing checks

`autopsy_pre_routing_checks.py --json` against the draft artifact: **0 fires.** C1/C2/C3
report `inapplicable` (claim-keyed, `claim_ids: []` -- structurally blind here, per the
skill's own caveat that `inapplicable` is not `no fire`). C5 (prose-vs-scored-run) and C6
(seed-dissent-vs-absolute) found nothing to flag against this artifact's own content. Given
the claim-free blindness of C1-C3, Section 6 above and the read of two full prior planning
documents (`mech152_measurement_redesign_gated_20260818.md`,
`mech152_writepath_addressing_probe_20260825.md`) carry the load C1-C3 would otherwise
carry -- both documents were read in full, not skimmed, before this diagnosis, per the
2026-08-18 standing instruction on full-artifact reads.

---

## 8. Re-derive brake

Fired **false**. `claim_ids: []`, recommended category `standard`, not `substrate_ceiling`.
No claim's autopsy count applies -- identical disposition to V3-EXQ-943 (Section 6 there).

---

## 9. Learning and routing

**Node class:** the write-address-informativeness question is now `mystery (known data)` at
these four operating points -- more BIAS-weight sweeps or REFRACTORY-k sweeps would not
change the substantive picture (magnitude is the binding constraint, not sample coverage).
Whether the human call closes the write-path gate is a governance decision, not a further
experiment.

**Learning** (mirrored in the companion JSON `learning_extracted`):

1. Write-address informativeness is statistically detectable at 2 of 4 operating points
   against a purpose-built, independently-validated order-only null on a real agent -- a
   first for this six-generation lineage.
2. The detectable signal is of minute magnitude (~0.02-0.06% of the instrument's own
   positive-control range) -- statistically real, practically negligible until shown
   otherwise.
3. Weakening the usage/conscience term does NOT monotonically increase addressing
   informativeness (BIAS_W0_01 fails where the driver's own hypothesis predicted the
   strongest signal) and additionally partially re-degenerates occupancy -- the
   bias_weight/informativeness relationship is non-monotone in this data.
4. REFRACTORY underperforms BIAS_W1_0 on this instrument, the opposite ranking from a
   separate synthetic depth-based probe -- the two instruments disagree, and per the
   synthetic probe's own stated preference, this real-agent result should be weighted more
   heavily, but neither alone settles which mode to ship as default.
5. The indexer's `vacuous_pass` flag has a structural blind spot for deliberate
   OR-aggregated, individually load-bearing per-arm criteria -- distinct in kind from the
   four already-documented join-mismatch sub-cases (those are key-matching mismatches in a
   legacy fallback path; this fires at the primary rule itself, upstream of that path).

**Routing: `governance`.** Amend substrate_queue `contextmemory-write-path-addressing-
degeneracy`: append V3-EXQ-946 as a second validation record (addressing, alongside 943's
occupancy record). Do **not** flip `implemented_pending_validation` to
`implemented_validated` on this evidence alone -- see Section 5's magnitude finding and
Section 10's human call below. Leave the 436f `failure_record` item `resolved: open`.

**Not routed:** `/lit-pull` (lit_status present); `/queue-experiment` for a 946b letter
(node class is `mystery`, not `puzzle` -- more runs at more weights would not change the
picture); `/implement-substrate` (the write-address build already landed; what remains is a
human disposition on the validation evidence, not a new build); `/claim-synthesis`
(claim-free); governance-demotion (no claim); indexer code fix (out of this skill's scope
-- reported as follow-on, not performed here).

**Follow-ons (reported, not chipped per the `/failure-autopsy` CLAUDE.md exception -- this
IS `/failure-autopsy` work, reported inline):**

1. The substrate_queue amend above -- this autopsy's own recommendation, for governance to
   apply.
2. The human call on MECH-152's gate (Section 10) -- already the explicitly stated owed
   step in both prior planning documents; this autopsy supplies the confirmed numbers.
3. The indexer join-mismatch gap (Section 6) is genuine follow-on engineering work outside
   this skill's writ (fixing `build_experiment_indexes.py` is not a claims/substrate/
   experiment action). **This is reported here and will be surfaced as a spawn_task chip at
   session close**, since it is not `/governance` or `/failure-autopsy` work by the
   CLAUDE.md exception's own definition -- it is an infrastructure defect nothing else
   audits.
4. If the human call favours a specific mode (BIAS vs REFRACTORY) as the shipped default:
   the 436-family sleep retest that 943's autopsy already named as unblocked-for-occupancy
   remains open and would additionally need the chosen addressing mode wired in.

**Draft `evidence_quality_note`:** see companion JSON
`recommended_evidence_quality_note` (manifest-level; no claim to write, `claim_ids: []`).

---

## 10. Read-across (not adjudicated)

This artifact does not supersede `failure_autopsy_V3-EXQ-943_2026-08-21`,
`failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16`, or
`failure_autopsy_slot_cosine_sim_fanout_sweep_2026-08-13`.

**MECH-152 (GFLAG-0044, HOLD demote_to_candidate, cycle gov-20260821-0203).** The HOLD's
stated condition was that the write-path substrate entry stays
`implemented_pending_validation` and V3-EXQ-943's occupancy PASS is not addressing
validation. 946 supplies the addressing validation that was missing, but per Section 5's
magnitude finding, does not on its own license flipping the substrate entry to
`implemented_validated`, and per the mech152_measurement_redesign_gated_20260818.md
Section 5/6.3 finding (bank-content-ablation control, Element 6, not yet queued), the
measurement redesign itself remains gated regardless of this run's addressing result. MECH-
152's `provisional` status and `pending_retest_after_substrate: true` are unaffected by this
claim-free run; this section is read-across, not a claim disposition.

**EVB-0628 / INV-044.** Marked `blocked_substrate` 2026-08-23 (REE_assembly `54e114c5de`)
on exactly this write-address-informativeness gap. This run supplies a first data point
(informativeness exists, magnitude minute) but the SNR implied by Section 5 (a signal
~0.02-0.06% of the instrument's detectable range) is a caution against unblocking a
differentiation DV on this evidence alone: a downstream attribution/differentiation
mechanism built on a channel this thin risks reproducing exactly the "evidence that looks
valid but is not" (`corrupting`) failure mode the substrate_queue entry's own severity
stamp warns against. Not adjudicated here (claim-free, INV-044/EVB-0628 disposition is
governance's to make); named for the human call in Section 10 below.

**mech152_writepath_addressing_probe_20260825.md.** That document's own Section 2
recommendation ("regen the evidence index, then autopsy V3-EXQ-946, then put the human call
to the user with 946's numbers in front of them") is what this artifact executes. Its
Section 6.4 mode-ranking disagreement (REFRACTORY favoured on synthetic depth vs BIAS
favoured on 946's real-agent addressing) is read across in Section 5 above, not
re-adjudicated -- that document already states, and this autopsy agrees, that 946's reading
should be weighted over the synthetic probe's where they conflict.

---

## 11. Human call (Step 8 gate) -- CONFIRMED 2026-08-25T18:30:37Z

Both prior planning documents name this as the owed next step. Three questions were put to
the user (`AskUserQuestion`), each carrying a `(Recommended)` option per this autopsy's own
Section 5/9/10 analysis. **The user selected the recommended option on all three, verbatim,
with no dissent or amendment.**

1. **Does 946's evidence close the `contextmemory-write-path-addressing-degeneracy`
   substrate entry** (flip to `implemented_validated`)? **-> NO, do not close it yet.**
   Disposition: record 946 as a second validation datapoint (addressing, alongside 943's
   occupancy) but keep the entry `implemented_pending_validation` pending the still-unqueued
   measurement redesign (Element 6 bank-content-ablation control). Magnitude is too small to
   be practically load-bearing for EVB-0628/INV-044 on this evidence alone.
2. **Which mode ships as the write-address default** (BIAS vs REFRACTORY)? **-> DEFER.**
   Neither instrument alone settles it: this run and the synthetic depth-based probe
   conflict on ranking, and both surface real weaknesses in their favoured mode (BIAS:
   occupancy-without-addressing, non-monotone/fragile weight-response, minute magnitude;
   REFRACTORY: worse occupancy than BIAS in this run, addressing loser on this instrument).
   Mode selection stays open pending the measurement redesign or a run that can resolve the
   disagreement directly.
3. **Does 946 change the MECH-152 measurement redesign's scope** (Element 6, still
   unqueued)? **-> NO, unchanged.** 946's result doesn't touch the Element-6 finding (the
   redesign's own DV clears its band even on a random-content bank under the production
   tagger config, regardless of write-path addressing quality) -- the redesign stays gated
   on that separately, exactly as `mech152_measurement_redesign_gated_20260818.md` Section 6
   already specifies.

**Consequence for governance:** the amend to substrate_queue `contextmemory-write-path-
addressing-degeneracy` in Section 9 stands as originally recommended (add V3-EXQ-946 as a
validation record, `resolved: open`, do NOT flip status). No claims.yaml write is triggered
(claim-free). GFLAG-0044's HOLD (MECH-152 stays `provisional`) is unaffected and remains
correct. The MECH-152 redesign (Element 6 + the five originally-specified elements) remains
designed-but-not-queued, per its own gate, unchanged by this run.

---

## 12. Constraints observed

Interactive session (not staging mode). Claim opened via `task_claim.py` on the two
artifact paths only -- the shared `hypothesis_space_registry.v1.json` and the
coordination-plane pause paths were both contended by concurrent sessions
(`failure-autopsy-cluster-c-3c01c6` on V3-EXQ-948, and the standing
`f-dominance-regime-retest-ddbe10` governance-pause) and are not needed here: this target
is claim-free with no `fanout_recommendation`, so no live registry append is owed (same
disposition as V3-EXQ-943 Section 10), and the coordination plane is already paused by the
standing governance session. No `claims.yaml` / manifest / `review_tracker.json` /
`substrate_queue.json` / `hypothesis_space_registry.v1.json` edit performed by this skill --
governance applies the recommendations above.
