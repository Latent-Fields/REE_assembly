# Failure Autopsy — V3-EXQ-436c (SD-017 / ARC-045 / MECH-166)

Generated: 2026-08-03T10:16:57Z
Session: night-mode-e39dfd-436c874
Scope: single
Status: confirmed (interactive gate confirmed by user 2026-08-03)

## 1. Target

- `run_id`: `v3_exq_436c_sd017_mech166_repr_confirmer_20260802T221621Z_v3`
- `queue_id`: V3-EXQ-436c (supersedes V3-EXQ-436b)
- `claim_ids`: SD-017, ARC-045, MECH-166
- `outcome`: FAIL, `evidence_direction`: weakens (all three claims)
- `interpretation.label`: `sws_then_rem_does_not_differentiate_slots`
- `dry_run_checked`: true (via `scripts/check_dry_run_citations.py`) — clean, real run.
- `substrate_stable_across_run`: true (no reproducibility caveat).
- Recording: `validate_recording.py` reports complete always-core (no gaps).

## 2. Facts reconstruction

**Lineage**: 436a (noise-floor/input-diversity confound, fixed) → 436b (recording gap:
driver discarded `run_sleep_cycle()`'s entire return value with `_ = ...`, so
`sws_n_writes`/`rem_n_rollouts` were never captured — confirmed `failure_autopsy_V3-EXQ-436b_2026-08-02`,
category `measurement_gap`) → **436c (this run): the recording gap is fixed and a clean
result now stands.**

**P0 readiness gate** (new in 436c, the direct fix for 436b's recording gap): pooled
`sws_n_writes` = 800, `rem_n_rollouts` = 600 across all 5 SWS_THEN_REM seeds — both clear
their floor (>0) by a wide margin. `ContextMemory.write()` and the REM-equivalent replay
demonstrably fired. **This is not a recording gap.**

**C1 (sole PASS/FAIL gate)**: `slot_cosine_sim(SWS_THEN_REM) < slot_cosine_sim(WAKING_ONLY)`
required in ≥3/5 seeds. Actual result — **0/5 seeds pass, and the effect runs in the
opposite direction**:

| seed | waking cos-sim | SWS_THEN_REM cos-sim | signed diff | waking entropy | SWS_THEN_REM entropy | slot_sep | C4 |
|---|---|---|---|---|---|---|---|
| 42  | 0.6734 | 0.7387 | +0.065 | 1.214 | 1.202 | 0.634 | pass |
| 7   | 0.0197 | 0.99997 | +0.980 | 1.194 | 1.204 | 0.193 | fail |
| 13  | 0.4816 | 0.99999 | +0.518 | 1.241 | 1.244 | 0.176 | fail |
| 100 | 0.0618 | 0.99999 | +0.938 | 1.225 | 1.225 | 0.589 | pass |
| 200 | 0.2820 | 0.99997 | +0.718 | 1.208 | 1.215 | 0.188 | fail |

Waking-phase action-class entropy is healthy and stable (~1.19–1.24) in **every** seed
and **every** condition — ruling out the "monomodal collapse, nothing for sleep to
refine" explanation that blocked the 436-family for GAP-2 (see §3 below). In 4 of 5
seeds, SWS_THEN_REM drives whole-bank slot cosine similarity to **within
3×10⁻⁵ of total collapse (1.0)** — not "no effect," but a strong, consistent
**homogenization** of context-memory content across the manipulation the claim predicts
should *differentiate* it.

**Script** (`ree-v3/experiments/v3_exq_436c_sd017_mech166_repr_confirmer.py`): pre-registers
exactly this branch in its own interpretation grid — "if waking-phase entropy is healthy
but slot_cosine_sim still does not differentiate, that is a genuine (b) weakens reading
for all three claims... with P0 met, this is real evidence... not a wiring failure." The
driver's own pre-registered logic and this autopsy's independent read agree.

**Failed criterion**: discrimination (C1), not an absolute/negative-control criterion —
and the failure is a clean reversal, not a null.

## 3. Claim-layer mapping

- **SD-017** (`sleep_phase.minimal_sleep_infrastructure_v3`, status stable): predicts
  context representations stay globally undifferentiated (cos_sim → 1.0) *without*
  SWS/REM. Status `stable` is unaffected by a `weakens` evidence tag on the same rule
  applied to a downstream implementation detail (per its own evidence_quality_note
  history — SD-017's genuine support remains V3-EXQ-691, a different mechanism claim).
- **ARC-045** (`hippocampus.bidirectional_information_flow`, candidate): predicts
  cos_sim < 0.95 (differentiated) *after* sleep phases specifically via bidirectional
  offline flow. This run's own gate is the paired directional comparison (pre-registered
  as primary over the absolute 0.95 threshold), and it is what fails.
- **MECH-166** (`hippocampus.slot_formation_filling_temporal_separation`, candidate):
  "slot structure must be consolidated during an SWS-analog phase." This run IS the
  direct test its own notes call for (EXQ-239/MECH-153 only provided an indirect one).

**Did the test let the claims express themselves?** Yes — P0 confirms the write/replay
machinery fired at real volume (800/600 pooled events), waking-phase behavioural
diversity is healthy, and the DV is wall-independent (read under `torch.no_grad()` off
`agent.e1.context_memory.memory`, no confound from the behavioural readouts). This is a
fair test.

**GAP-2 process note (flag, not a verdict on this run's validity):** `sleep_substrate_plan.md`'s
GAP-2 node states the 436-family successors (418m/436b) are deferred/unqueued pending the
`arc_062_rule_apprehension:GAP-B` rule-creator/discriminator substrate — yet 436b ran
2026-08-02T03:53Z and this run (436c) ran 2026-08-02T22:16Z, neither gated on GAP-B
landing. The 2026-08-02 governance entry for this node already flagged the discrepancy
("worth a look next time this node is touched — not investigated further this cycle").
This autopsy is that look: **the specific concern GAP-2's resume_condition targets
(zero waking-phase behavioural diversity, diagnosed in 418l/436a) is empirically absent
here** — entropy is healthy in every seed of this run. That does not resolve whether
GAP-B is relevant for some *other* reason this autopsy did not investigate, but it means
436c's own result is not invalidated by the stated GAP-2 concern. Recommend governance
reconcile the plan doc's resume_condition against this run rather than treat the
discrepancy as a reason to discount the result.

## 4. Biological-reference triage

Systems-consolidation theory (hippocampal-cortical dialogue, sharp-wave-ripple-mediated
replay) predicts SWS/REM should **selectively strengthen and differentiate specific
engrams** via targeted replay — not homogenize all memory content toward a shared
attractor. The measured direction (homogenization) is the opposite of what the biological
reference predicts, which is itself informative: it points to a **specific, structural,
content-blind write mechanism** rather than "sleep does nothing" or "sleep does the wrong
thing for some emergent-property reason."

**Root-cause trace (code-level).** `ContextMemory.write()` (`ree_core/predictors/e1_deep.py:77`):

```python
def write(self, state):
    write_signal = self.write_gate(state)
    with torch.no_grad():
        query = self.query_proj(state)
        scores = torch.mm(query, self.memory.t())
        min_idx = scores.mean(0).argmin()
        self.memory.data[min_idx] = 0.9 * self.memory.data[min_idx] + 0.1 * write_signal.mean(0)
```

`write_gate` is a plain `nn.Linear(latent_dim, memory_dim)` + `Sigmoid`, **with its
default bias still in place**. This is the *exact* failure class already diagnosed and
fixed on the **read** path: SD-016 Part A / EXQ-477 (EXP-0155) found `key_proj`'s bias
dominated its weight-times-content term (`bias_over_content_ratio` 9.88 pre-train / 3.41
post-P0), collapsing `read()`'s attention to near-uniform regardless of query content —
fixed by removing `key_proj`'s bias entirely (`context_memory_writepath_fix.md`).

That fix-and-measurement exercise **never touched `write_gate`**, because `write_gate`
plays no role in `read()` — it is the content-generation step for `write()`, an entirely
separate code path. The same doc explicitly reasons about why `query_proj`'s default
bias is safe *for the read path* ("consumes the input cue, which has per-batch
variation... does not collapse softmax inputs") but says nothing about whether
`write_gate`'s bias could dominate its own output, or about `query_proj`'s role in
`write()`'s `argmin` slot-selection (a different computation from `read()`'s softmax).
**If `write_gate`'s bias dominates, every write — regardless of which slot the argmin
picks or what state produced it — pushes toward nearly the same vector.** Applied
repeatedly (160 writes across 20 SWS cycles per seed in this run's design), that would
mechanically produce exactly the observed near-total collapse toward a shared attractor,
independent of any MEL/novelty signal.

**This is not yet a measured fact — it is a specific, testable hypothesis**, analogous in
method to EXQ-477's own diagnostic (measure `bias_over_content_ratio` for `write_gate`,
the same way it was measured for `key_proj`). It has not been directly instrumented in
this run.

**Convergent cross-experiment signal.** `failure_autopsy_V3-EXQ-861a_2026-08-03.json`
(confirmed, different session, same day) independently root-caused a **different**
DV (`mean_sws_new_slot_diversity`, touched-slot cosine *distance*) on the **same**
write path (`run_sws_schema_pass()` → `ContextMemory.write()`) to a structurally
self-referential novelty reference (`ThetaBuffer.consolidation_summary()`), producing a
uniformly tiny/flat content-selection weight regardless of arm — and found that even with
the MECH-122 content-selection fix applied and firing every cycle, the touched-slot
statistic still failed to track novelty and in two well-formed seeds moved in the *wrong*
direction (decreasing with MEL). **Two unrelated claim families (MECH-180/MECH-122 dose-
response vs. SD-017/ARC-045/MECH-166 slot differentiation), two different DVs (touched-
slot diversity vs. whole-bank cosine similarity), same substrate (`ContextMemory` write
path), same qualitative shape: writes are not differentiating content the way either
claim family predicts.** This run does not even have `use_mech122_spindle_content_selection`
enabled (436c's `_make_agent` never sets it — plain baseline `write()` path), so its
result cannot be explained by 861a's specific reference-source bug; it is evidence of a
**more upstream** defect in the un-augmented write path itself, for which `write_gate`
bias-dominance is the leading hypothesis.

**Literature**: `evidence/literature/targeted_review_{mech_166,arc_045,sd_017}` already
exist and are unaffected by this finding — the biological prediction (selective,
differentiated consolidation) is not in question; the REE implementation's fidelity to it
is.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened | fair test: P0 met, waking diversity healthy, DV wall-independent |
| Biological reference | clear | systems consolidation predicts differentiation, not homogenization; divergence is informative |
| Developmental / dependency prerequisites | present | `depends_on` (MECH-092, ARC-038, ARC-007/SD-014, MECH-166 for ARC-045) all V3-implemented; not a missing-prerequisite story |
| Implementation completeness | partial — hypothesized gap | `write_gate` bias-dominance (untested this run) as leading candidate; `write()`'s argmin slot-selection also unverified for genuine content-sensitivity |
| Environment adequacy | adequate | context-conditioned harm-threshold env; SAFE/DANGEROUS structure present; unchanged from validated 436a/436b design |
| Measurement adequacy | adequate | wall-independent DV, P0 gate closes 436b's recording gap, non-degenerate |
| Integration adequacy | isolated | write path failure is local to `ContextMemory.write()`/`write_gate`; doesn't implicate encoder, E2, or downstream consumers |
| Scale / capacity | adequate | 20 sleep cycles / 5 seeds is ample volume to detect differentiation if the write path supported it |

## 6. Cluster pattern (informal — not a formal cluster-scope autopsy)

Not run as a formal cluster (different claim families, different DVs), but the shared
substrate + shared failure shape with `failure_autopsy_V3-EXQ-861a_2026-08-03` is
load-bearing and stated above (§4). Both autopsies point at the same code region
(`ContextMemory`/`run_sws_schema_pass` write path) and should be triaged together at
`/governance` and by whichever `/implement-substrate` session next touches
`MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION`.

## 7. Learning extracted

1. The recording-gap fix (P0 gate) worked: 436c is genuinely non-degenerate, unlike 436a/436b.
2. SD-017/ARC-045/MECH-166's decisive DV moves in the *opposite* direction from
   prediction, with a strong, consistent effect size (4/5 seeds within 3×10⁻⁵ of total
   collapse) — not a null.
3. The write path's `write_gate` has never been audited for the bias-over-content defect
   class that was found and fixed on the sibling `key_proj` (read path) — a concrete,
   cheap, unaddressed gap.
4. This converges structurally with `failure_autopsy_V3-EXQ-861a_2026-08-03`'s finding on
   a different DV/claim family, reinforcing that the underlying gap is in REE's SWS write
   mechanism generally, not specific to either experiment's design.
5. `sleep_substrate_plan.md`'s GAP-2 gate (arc_062 GAP-B) predates and does not account
   for this run; its stated concern (waking monomodal collapse) is empirically absent
   here. Flagged for governance/plan reconciliation, not resolved by this autopsy.
6. Granularity-debt recurrence check (`scripts/granularity_debt_cluster.py MECH-166`):
   1 prior target (436b, `unclear`/`measurement_gap`) + this one (`weakened`). **Trigger
   does NOT fire** — 436b's shape was an instrumentation dead-end (recording gap), not a
   structurally distinct failure mode; this is implementation debt on one identified
   mechanism, not evidence the claim needs splitting.
7. Re-derive brake (`substrate_ceiling`-only count, R1–R3 convention): 0 prior hits for
   MECH-166 before this run. **Does not fire** (threshold 2) regardless of which category
   is finally recorded.

## 8. Repair pathway (user-confirmed 2026-08-03)

**Routing: `implement-substrate`, amending the existing `MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION`
substrate_queue.json entry** (the same entry `failure_autopsy_V3-EXQ-861a_2026-08-03` just
touched) rather than opening a new one — the two autopsies converge on the same write
path and governance should triage them together.

**Recommended `evidence_quality_note`** (SD-017, ARC-045, MECH-166, verbatim for governance
to apply):

> 2026-08-03 (governance, V3-EXQ-436c, confirmed `failure_autopsy_V3-EXQ-436c_2026-08-03`,
> successor to V3-EXQ-436b): recording gap fixed (P0 gate: pooled sws_n_writes=800,
> rem_n_rollouts=600, both floor-clearing). Waking-phase action-class entropy healthy in
> every seed (~1.2), ruling out the monomodal-collapse confound that blocked this lineage
> under sleep_substrate_plan.md GAP-2. C1 (slot_cosine_sim differentiation) fails 0/5
> seeds — not a null: SWS_THEN_REM collapses whole-bank cosine similarity to ~0.9999–1.0
> in 4/5 seeds (homogenization), opposite the predicted direction. Root-cause hypothesis
> (untested this run): `ContextMemory.write_gate` (Linear+Sigmoid, default bias) may carry
> the same bias-over-content collapse already found and fixed on `key_proj`'s read path
> (SD-016 Part A / EXQ-477); has never been audited. Converges with
> `failure_autopsy_V3-EXQ-861a_2026-08-03`'s independent finding on a different DV
> (touched-slot diversity, MECH-180/MECH-122) via the same write path. weakens SD-017,
> ARC-045, MECH-166 (all: pending_retest_after_substrate=true). Routing: implement-substrate,
> amend MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION.

**`recommended_substrate_queue_entry`** — see JSON. Adds SD-017/ARC-045/MECH-166 to
`unblocks_claims`, and a new `failure_record_entry` naming this run plus a concrete
diagnostic step (measure `write_gate`'s bias-over-content ratio per the EXQ-477 method
before committing to a specific fix).

**pending_retest_after_substrate**: true for all three claims. A same-question re-queue
(new letter, e.g. V3-EXQ-436d) against the repaired write path is the correct next step
once the substrate build lands — not before.

**Step 9b (hypothesis-space ledger)**: skipped. This target adjudicates a leg
(`recommended_evidence_direction` present) but is a lone, non-fan-out FAIL — it does not
resolve a previously pre-registered rival hypothesis, nor does it open a discrimination
portfolio requiring tracking. `hypothesis_space_registry.v1.json` has no existing
question referencing SD-017/ARC-045/MECH-166 (checked: 0/22 questions). Nothing to
register.
