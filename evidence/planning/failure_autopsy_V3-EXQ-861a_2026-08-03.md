# Failure Autopsy: V3-EXQ-861a (MECH-180 ecological sleep dose-response / MECH-122 content-packaging validation)

- **Generated:** 2026-08-03T08:24:26Z
- **Scope:** single
- **Status:** confirmed
- **Run ID:** `v3_exq_861a_mech180_mech122_spindle_content_selection_validation_20260802T215005Z_v3`
- **Queue ID:** V3-EXQ-861a (removed from queue on FAIL, per project convention)
- **Claim(s):** MECH-180, MECH-122
- **Supersedes:** none (additive arm-condition test over V3-EXQ-861, not a correction of it — 861's flag-OFF result stands independently)
- **Compares against:** `v3_exq_861_mech180_ecological_novelty_sleep_consolidation_decoupled_diversity_20260801T205600Z_v3` (confirmed `failure_autopsy_V3-EXQ-861_2026-08-01`)
- **dry_run_checked:** true — `scripts/check_dry_run_citations.py` over both this run and its lineage ancestor V3-EXQ-845: "0 dry cited, 0 dry in named families, 0 ambiguous, 2 clean, 0 unknown"
- **Machine:** ree-cloud-4 (per manifest `machine` field on the flat record — 861a itself; 861 ran on ree-cloud-2, 845 on ree-worker-3), `linux-x86_64-py3.10-torch2.12.0+cpu`
- **Recording provenance:** `validate_recording.py --paths <manifest>` → OK, 0 always-core gaps, 0 thin-pack drops, 0 schema warnings. `recording_schema: rec/v1`, `substrate_hash` present, `config`/`seeds` ([42,123,456]) present.

## 1. Facts

**Why this run exists.** V3-EXQ-861 (confirmed autopsy 2026-08-01) traced its `spindle_density` DV's clean 0/3-seed FAIL — under both the confounded (845) and deconfounded (861) touched-slot statistics — to a genuine, previously-undischarged dependency: `ContextMemory`'s SWS-pass writes had no content-selection step, so there was no channel through which higher novelty/MEL could produce more *differentiated* writes (exactly what touched-slot diversity measures). That autopsy mapped the gap to MECH-122's content-packaging half and routed `/implement-substrate` for a new `substrate_queue.json` entry (`MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION`, `complicated (buildable)` — the mechanism already existed as an unwired stub, `ThetaBuffer.consolidation_summary()`/`set_consolidation_mode()`).

**The build** (ree-v3 `a7d36429fd`, IGW-20260801-197, same session that authored 861's autopsy): wired those two `ThetaBuffer` methods into `REEAgent.run_sws_schema_pass()` (`ree_core/agent.py` ~10327–10421), gated by two new `REEConfig` flags: `use_mech122_spindle_content_selection` (default `False`, bit-identical off) and `mech122_spindle_selection_gain` (default `1.0`). When enabled, each schema-installation prototype's `z_world` is blended toward the `ThetaBuffer`'s recency-weighted `consolidation_summary()` in proportion to how *closely* it already matches that reference (`novelty = (1-cos_sim)/2`, `selection_weight = clamp(novelty*gain, 0, 1)`; low-novelty content is homogenised toward the reference, high-novelty content keeps its own direction). New contract probes (`tests/test_flag_inertness.py`) confirm OFF-inertness and ON-differentiation against identical buffered content.

**This run (861a)** is IDENTICAL to 861 in every other design particular (env, arms, seeds, gates, thresholds) except `_make_agent()` sets `use_mech122_spindle_content_selection=True` uniformly across all 5 arms including `ARM_4_HIGH_OFF` (deliberately uniform — the flag is orthogonal to `use_mel_consumer`/`mel_on`, so this stays a single-variable change from 861). `substrate_queue.json`'s own entry (status `implemented_pending_validation`) named this run as the outstanding validation step.

**Result.** `interpretation.label = "mel_control_degenerate"` (FAIL). Both readiness preconditions met (`world_forward_converged_frozen_probe` 1.0/0.667, `ecological_novelty_mel_gradient_present_this_config` 1.0/0.667). `per_dv_seed_pass_fraction`: `sws_power 0.667, spindle_density 0.0, replay_rate 0.667` — **unchanged from 861's flag-OFF result** on the headline pass/fail count. `C2` (non-load-bearing control) improved from 0/3 to 1/3 (seed 123), but that improvement is itself an artifact of measurement degeneracy, not a real effect (see below).

**New instrumentation this run adds, and what it shows.** The driver now reports `mean_spindle_selection_applied` (always `1.0` — the mechanism fired every cycle in every cell, confirming it is not silently inert) and `mean_spindle_selection_weight` (the mean per-prototype `selection_weight`, i.e. how much of each write kept its own direction vs. was pulled toward the theta reference). Read off the manifest directly:

| Seed | Arm (order) | mel | selection_weight | mean_sws_new_slot_diversity |
|---|---|---|---|---|
| 42 | NONE→LOW→HIGH→MED (by measured MEL) | 1.5e-5→2.0e-5→3.0e-5→3.5e-5 | 0.0056 / 0.0101 / 0.0079 / 0.0096 | **0.0227 → 0.0203 → 0.0158 → 0.0112** (strictly decreasing) |
| 456 | LOW→NONE→MED→HIGH | 2.5e-5→2.6e-5→2.9e-5→4.1e-5 | 0.0041–0.0045 (flat) | **0.0111 → 0.0111 → 0.0083 → 0.0081** (non-increasing) |
| 123 | NONE→MED→LOW→HIGH | 2.3e-5→2.6e-5→2.9e-5→3.5e-5 | 0.0039–0.0044 (flat) | 0.0151 / **0.0 (insufficient)** / 0.0151 / 0.0151 — degenerate, see below |

`selection_weight` is uniformly tiny (~0.004–0.01, i.e. 99%+ of every write's magnitude is pulled toward the theta reference) and does **not** track MEL/arm in any of the three seeds — it is closer to flat noise. On the two seeds with well-formed touched-slot data (42, 456), `mean_sws_new_slot_diversity` **decreases monotonically as measured MEL increases** — the opposite of MECH-180's prediction, and a clean, consistent pattern across both seeds, not scatter.

**Seed 123 is separately degenerate**, independent of the above finding: 4–6 of 6 measurement cycles per arm reported `n_touched_slots < 2` (`insufficient`, contributing no data point to the mean per the redesign's own convention — see 861's redesign rationale). The one C2 "pass" this run reports (seed 123, up from 0/3 in 861) is driven entirely by comparing `ARM_3_HIGH_ON`'s single surviving data point (0.0151, from only 2 valid cycles) against `ARM_4_HIGH_OFF`'s `0.0` — which is a **no-data fallback** (all 6 cycles insufficient for that arm/seed), not a genuine zero measurement. This C2 "pass" is not trustworthy and should not be read as an on/off effect.

## 2. Root-cause trace (code-level, not just manifest-level)

Traced `ree_core/latent/theta_buffer.py` and the wiring in `ree_core/agent.py::run_sws_schema_pass()`:

- `ThetaBuffer._z_world_buffer` is a **10-entry** rolling deque (`theta_buffer_size: int = 10`, `ree_core/utils/config.py:2387`, not overridden by this driver), updated once per E1 tick during waking.
- `consolidation_summary()` (the "novelty reference") is a **linear-recency-weighted mean of exactly those last ≤10 E1 ticks** — i.e. the tail end of the *same* short waking window that immediately precedes the SWS pass.
- The schema-installation prototypes being tested for "novelty" are sampled from `self._world_experience_buffer` (`run_sws_schema_pass`'s "diverse sampling: early, mid, recent thirds") — a buffer populated by the **same recent wake window**.
- Consequence: the quantity being compared against the quantity it is *drawn from* is, by construction, self-similar (cosine similarity ≈ 1, novelty ≈ 0) almost regardless of which arm/environment produced it. This is exactly the uniformly-tiny, MEL-insensitive `selection_weight` observed above — an independent confirmation from the instrumentation, not a hypothesis.
- This is a **different novelty axis** from the one the rest of this experiment family already validated as arm-discriminating: `mean_mel` (driven by `world_rule_shift`-induced world-model prediction error over the *whole* wake window, calibrated against a stable-base reference) clears its R2 precondition at 1.0/0.667 in this very run. The content-selection mechanism's "novelty" and MECH-180's "novelty" (MEL) are two different signals; the build correctly wires a *content-selection* mechanism, but the reference it selects against does not correlate with the manipulation this experiment varies.

I did not find a bug in the mechanics of the blend itself (the arithmetic is correct, contract-tested, and fires every cycle) — the defect is in **which signal was chosen as the novelty reference**.

## 3. Claim-layer mapping

**MECH-180** (`docs/claims/claims.yaml`): `status: candidate`, `v3_pending: true`, `epistemic_category: standard` (graduated from `substrate_ceiling` by the 861 autopsy — the ecological run has now scored three times: 845, 861, 861a). `depends_on`: INV-050, MECH-121, MECH-122, MECH-120. Prior evidence: 677 (`substrate_ceiling`, manipulation check failed), 718/718a (`measurement_gap`, producer not exercised), 845 (`mixed/measurement_test_design_defect`, first partial positive), 861 (`mixed/standard`, DV1/DV2 strengthened, DV3 weakened-but-explained). **This run adds nothing new to the MECH-180 direction on DV1/DV2** (unchanged from 861: `sws_power`/`replay_rate` still 2/3) and **does not close DV3** — it tests a specific repair hypothesis for DV3 and that repair did not work as built. Re-derive brake count (R1–R3 convention): 1 confirmed `substrate_ceiling` hit (V3-EXQ-677) — unaffected by this target (this target's category is not `substrate_ceiling`), threshold 2 not reached, brake does not fire.

**MECH-122** (`docs/claims/claims.yaml`): `status: provisional`, `implementation_phase: v3` (correct per 861's autopsy; MECH-122's own registration prose still says "V4 scope" — a separately-flagged stale-prose issue, not corrected by this autopsy). `depends_on`: MECH-030, MECH-089, MECH-121, SD-006. **This is the FIRST claim-tagged autopsy target for MECH-122** (`granularity_debt_cluster.py MECH-122` returns 0 targets prior to this one) — no recurrence signal is possible yet, and the granularity-debt trigger and re-derive brake are both inapplicable by definition (need ≥2 same-claim hits to fire either). MECH-122's own `evidence_direction_per_claim` on this run is `weakens`, computed per the driver's pre-registered per-claim rule (`spindle_density` frac == 0 → weakens) — a single-run, single-mechanism-half (content-packaging only; sensory-gating half untested here) reading, not a claim-level demotion.

## 4. Biological-reference triage

Unchanged from 861's triage, still applicable: the closest mammalian reference for `spindle_density` is thalamocortical sleep spindles' content-packaging function — spindle-coupled hippocampal ripples associated with content transfer to cortex (Yang, Logothetis & Eschenko 2018/2019; Ngo 2020; Staresina 2015 — all already in `evidence/literature/targeted_review_connectome_mech_122/`). No new lit-pull is owed; the biology basis was already established and this run does not touch it.

**What this run adds to the triage**: the failure mode identified here is a **measurement/operationalization gap in the REE proxy**, not a biology-divergence finding. Biologically, spindle-coupled content selection is understood to be driven by hippocampal replay content relative to a *stable* cortical schema, not by comparison against a rolling few-hundred-millisecond self-average of the agent's own immediately-preceding representations — so the REE proxy's choice of a 10-tick recency buffer as the "reference" is arguably a mismatch to the biological analogy on its own terms, independent of the MEL-tracking argument above. Worth folding into the repair spec (Section 6) rather than treated as a separate finding.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment (MECH-180, DV1/DV2) | strengthened (unchanged from 861) | not re-tested by this run's substrate change; still stands from 845/861 |
| Claim alignment (MECH-180, DV3) | weakened-but-explained (unchanged category, new explanation) | still 0/3; the specific repair hypothesis (content-selection wiring) that 861 proposed has now been tried and did not close it |
| Claim alignment (MECH-122, content-packaging half) | weakened (this implementation, this run) | mechanism fired, did not produce the predicted novelty-tracking diversity; single run, does not warrant claim-level demotion |
| Biological reference | partial | content-packaging citations stand (Yang2018/Ngo2020/Staresina2015); this REE proxy's reference source (self-referential recency buffer) is arguably itself a biological mismatch, independent of the MEL-decoupling finding |
| Developmental / dependency prerequisites | present but wrongly sourced | `ThetaBuffer` (MECH-089) is genuinely implemented and available; the defect is which of its outputs was chosen as the selection reference, not a missing prerequisite |
| Implementation completeness | partial — mechanism complete, calibration wrong | the blend/selection arithmetic is correct and contract-tested (OFF-inert, ON-differentiating); the *reference signal* it operates on is the gap |
| Environment adequacy | adequate | unchanged from 845/861/798a; SD-MEL-PRODUCER validated, R1/R2 both clear at 1.0 |
| Measurement adequacy | now BETTER understood, still inadequate for DV3 | new instrumentation (`mean_spindle_selection_applied`/`_weight`) is exactly what let this autopsy distinguish "mechanism didn't fire" from "mechanism fired against the wrong reference" — a genuine methodological improvement even though the DV still fails. Seed 123's measurement is additionally degenerate (touched-slot insufficiency), independent of the reference-source issue |
| Integration adequacy | isolated for DV3 | content-selection operates entirely within the SWS pass; DV1/DV2 (write count, rollout count) are untouched by this substrate change, exactly as designed |
| Scale / capacity | adequate | N/A to this finding — the issue is which signal is read, not insufficient scale |

## 6. Learning extracted and repair pathway

**Learning extracted:**
1. The MECH-122 content-packaging build (`a7d36429fd`) is **not inert** — it fires every cycle in every cell (`mean_spindle_selection_applied = 1.0` throughout) and its blend arithmetic is correct and independently contract-tested. Ruling this in is itself new information 861's autopsy did not have (861 predates the build).
2. The build's **novelty reference is structurally decoupled from the manipulation this experiment family varies.** `ThetaBuffer.consolidation_summary()` averages the same short recent window that also supplies the schema-installation prototypes, so "novelty relative to it" collapses toward ≈0 almost independent of arm — confirmed both by the uniformly tiny/flat `selection_weight` (0.004–0.01, no MEL-tracking) and by code trace (10-tick self-referential buffer). This is a genuine, previously-undiscovered implementation gap, discovered *because* the build was tried, not evidence that content-packaging-by-novelty is biologically wrong.
3. On the two well-formed seeds, touched-slot diversity now moves in the **wrong direction** (monotonically decreasing with MEL) rather than merely failing to move — near-total homogenization (tiny selection weight everywhere) appears to interact with which specific slots get touched more in higher-shift-rate arms. This residual anti-correlation is noted but not fully explained; it does not change the repair recommendation.
4. Seed 123's touched-slot statistic is separately degenerate (4–6/6 cycles insufficient in every arm) — this is a measurement-reliability issue independent of the reference-source finding, and it is what produced this run's one spurious C2 "pass". Future same-family runs should consider flagging/excluding a seed whose insufficiency rate exceeds some threshold (e.g. >50% of cycles) from C1/C2 scoring rather than silently degrading its contribution.
5. MECH-122 now has its first claim-tagged autopsy target (`weakens`, content-packaging half only, this implementation) — not yet a recurrence pattern (n=1), and the sensory-gating half remains entirely untested (separate `substrate_queue.json` entry, `MECH122-SENSORY-GATING-OFFLINE-PROTECTION`).

**Diagnosis**: implementation/operationalization gap (wrong reference signal for "novelty" in the content-selection mechanism), discovered via a correctly-executed validation build. Not a claim falsification for MECH-122 (biology and dependency prerequisites intact; the mechanism-as-specified was simply not implemented with a reference that tracks the intended axis) and not new evidence against MECH-180 beyond what 845/861 already established.

**Node class: `complicated (buildable)`** — the fix is a named, concrete rewiring (change the reference source), not an open question requiring a new spike. Recommended repair, to spec a follow-on build (not built here, per Scope Discipline):

- Re-source `consolidation_ref` in `run_sws_schema_pass()` from a signal that actually correlates with the world_rule_shift-driven novelty axis already validated in this family — candidates: (a) gate `selection_weight` on the same E3/E2 prediction-error signal that drives MEL itself (reusing the validated SD-MEL-PRODUCER/CONSUMER channel rather than inventing a second novelty definition), or (b) widen/stabilize the theta reference to a longer-horizon or calibrated stable-base baseline (analogous to how MEL's own `mel_reference` is calibrated against a stable-base pass in `_run_cell`) rather than a 10-tick self-tracking recency buffer.
- Re-run the V3-EXQ-861/861a driver family (new letter, e.g. 861b) against the repaired reference source once built.
- Separately: consider a per-seed exclusion or flag for touched-slot-insufficiency rates above a stated floor, so a future run's C2 "pass" cannot again be produced by a no-data fallback.

**`recommended_substrate_queue_entry`**: `action: amend` — `MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION` already exists and already names this exact validation step as outstanding; this autopsy adds the specific reason the validation failed and the specific fix direction, rather than opening a new entry.

**Draft `evidence_quality_note` for MECH-180** (governance to apply verbatim, appended alongside the existing 861-sourced note, not replacing it):

> 2026-08-03 (V3-EXQ-861a, autopsy-confirmed): validation of the MECH-122 content-packaging build (ree-v3 a7d36429fd) against the spindle_density DV. The mechanism fires every cycle (mean_spindle_selection_applied=1.0 throughout) but its novelty reference (ThetaBuffer.consolidation_summary(), a 10-tick self-referential recency average) is structurally decoupled from the world_rule_shift-driven MEL axis this experiment family varies — confirmed both by a uniformly tiny/flat selection_weight (~0.004-0.01, no MEL-tracking) and by code trace. On the two well-formed seeds, diversity now moves the WRONG direction (decreasing with MEL) rather than merely failing to move. DV3 remains pending_retest_after_substrate, now against a specifically-diagnosed repair (re-source the novelty reference to something MEL-correlated, e.g. E3/E2 prediction error or a calibrated stable-base baseline). DV1/DV2 evidence is unchanged and stands independently (845/861).

**Draft `evidence_quality_note` for MECH-122** (governance to apply verbatim):

> 2026-08-03 (V3-EXQ-861a, autopsy-confirmed, first claim-tagged target for MECH-122): the content-packaging half's V3 proxy (ThetaBuffer-mediated novelty-gated content selection, ree-v3 a7d36429fd) was built and validated against MECH-180's spindle_density DV. The mechanism fires correctly (contract-tested, confirmed live in this run) but its operationalization of "novelty" (self-referential 10-tick recency buffer) does not correlate with the manipulation this test varies, so it does not produce the predicted novelty-tracking content diversity — weakens the content-packaging half AS IMPLEMENTED, at this specific granularity/reference choice, not the underlying biological hypothesis (dependency prerequisites and lit basis are intact; this is a wrong-reference-signal implementation gap, not a tested-and-falsified mechanism). Routed /implement-substrate (amend MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION) with a specific repair direction. The sensory-gating half (separate substrate_queue entry) remains entirely untested. status stays provisional — a single run does not warrant a status change either direction.

## 7. Re-derive brake / granularity-debt / hypothesis-space

- **Re-derive brake (MECH-180):** 1 confirmed `substrate_ceiling` hit (V3-EXQ-677) under the R1–R3 convention; this target's category is not `substrate_ceiling`, so the count is unaffected. Threshold (2) not reached — brake does not fire.
- **Re-derive brake (MECH-122):** count = 0 prior to this target (no prior `substrate_ceiling`-class hit exists for MECH-122); not applicable.
- **Granularity-debt trigger (MECH-180):** `granularity_debt_cluster.py MECH-180` (re-run this session, 5 targets before this one — 677/718/718a/845/861): alignment distribution `unclear=3, strengthened=2`, no target reads a bare `weakened` (861's DV3 reads `weakened-but-explained`, same shape this target repeats) — trigger does NOT fire. Adding this target (6th) does not change that: it is the same explained-dependency-gap shape as 861, not a new structurally-different failure signature.
- **Granularity-debt trigger (MECH-122):** `granularity_debt_cluster.py MECH-122` returns 0 targets prior to this one — this is the *first* tagging target. A single target cannot trigger a recurrence signal by definition; not applicable until a second, structurally-different MECH-122 failure appears.
- **Fan-out recommendation:** not applicable — this is a single discovered-implementation-gap finding (a specific, named repair), not a discrimination among live rival hypotheses.
- **Hypothesis-space ledger (Step 9b): DEFERRED, not skipped.** This autopsy adjudicates two legs with `recommended_evidence_direction` set (MECH-180 non_contributory, MECH-122 weakens), which would normally trigger a Step 9b append to `hypothesis_space_registry.v1.json`. That file is currently held by an **active TASK_CLAIMS.json claim** from a concurrent session (`lucid-spence-efbee6`, dACC PE/execution-gain cluster autopsy, claimed 2026-08-03T08:12:53Z) — per `task_claim.py`'s exact-file arbitration, editing it now would either collide or require an unclaimed write against a contended shared file. Per the established precedent for this exact situation (`failure_autopsy_V3-EXQ-847a-863_2026-08-02`'s own completion note), the registry append is deferred rather than forced: MECH-180/MECH-122 are not yet tracked in `hypothesis_space_registry.v1.json` as of this writing (confirmed by direct read), so a follow-on session (or the next `/governance` walk) should pre-register/resolve this run's leg once the contention clears. Recorded here so the gap is not silently lost.

## 8. User gate (Step 8)

Presented via `AskUserQuestion` 2026-08-03T08:24Z, two questions (facts reconstruction; routing). User confirmed both as presented, no revisions:

1. **Facts**: confirmed — mechanism fired correctly, novelty reference is self-referential/decoupled from MEL, this is a mechanism-operationalization defect rather than evidence against MECH-122's biology or MECH-180.
2. **Routing**: confirmed — `implement-substrate` amend on `MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION` with the specific novelty-reference-source fix; MECH-180 stays `non_contributory` on DV3 (DV1/DV2 unchanged); MECH-122 reads `weakens` for this specific implementation, not a claim-level demotion.

**Confirmed disposition:** as drafted in Section 6 above, no revisions from the gate.
