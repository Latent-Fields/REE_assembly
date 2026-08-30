# Diagnostic-PASS adjudication: V3-EXQ-965 (SD-e1 ITEM 1 action-conditioning validation) -- 2026-08-30

**Run:** `v3_exq_965_sd_e1_item1_action_conditioning_validation_20260830T145908Z_v3` - PASS - diagnostic - `claim_ids: []` (deliberate) - seeds [42,123] - arms [A_off, B_action, C_both] - ree-worker-3 - 209s - self-route `action_conditioning_converts_both_arms` - manifest `evidence_direction: non_contributory` - qid stamp `inv088_evaluator_degeneracy_cause`
**Status:** confirmed (interactive Step 8 gate 2026-08-30T16:19:45Z; session autopsy-exq965-20260830)
**Dry-run check:** clean -- family `v3_exq_965` is 0 dry / 1 real; no top-level or config `dry_run`; the `--dry-run` smoke described in the queue note wrote to a scratch dir, not to `evidence/`. The queue note's smoke text is cited below ONLY as documentation of author intent, never as measurement.
**Recording:** `validate_recording.py` -> complete, 0 always-core gaps. `substrate_hash` present, so a substrate-attributed reading here is falsifiable.

**Verdict in one line: the substantive finding is GENUINE; the criterion that produced the PASS label is UNSOUND.** (User-confirmed disposition at the Step 8 gate.)

## Facts

**Provenance verified, not assumed.** The ITEM 1 build `ree-v3 26557a3758` is a git ancestor of the run's `substrate_commit` `072d9b0b33b5`; `dirty: false`, `substrate_stable_across_run: true`, `drifted_since_resolved: false`. `e1_deep.py` at the run commit carries `actions=`, `_action_conditioned`, `_action_cond_unzero_self_slot` and `_action_cond_missing_calls`. The code change reached the running process.

**What ITEM 1 actually did (the load-bearing positive result).** On the direct Phase-4c probe -- `(z_self_0, z_world_0)` held bitwise fixed, hidden state reset per call, only the `actions=` one-hot varying -- the ON arms produce genuine per-action structure at the E1 output:

| cell | mean pairwise L2 | min | max | `action_cr` |
|---|---|---|---|---|
| A_off s42 / s123 | **0.0 / 0.0** | 0.0 | 0.0 | 1.03e-08 / 2.69e-08 |
| B_action s42 / s123 | 1.71e-03 / 2.19e-03 | 2.82e-04 / 1.74e-04 | 3.17e-03 / 4.16e-03 | 7.30e-04 / 7.69e-04 |
| C_both s42 / s123 | 1.65e-03 / 1.46e-03 | 1.53e-04 / 2.58e-04 | 2.90e-03 / 2.57e-03 | 7.25e-04 / 5.35e-04 |

**On the NON-GATING rollout statistic -- the one that matters for the consumer** -- ITEM 1 moves `cr_ratio(h=1)` from `4.14e-07 / 4.05e-07` (A_off, which reproduces V3-EXQ-954's own `4.76e-07 / 5.39e-07` to within ~15-25%) to `2.67e-03 - 3.96e-03`: a **6455x - 9775x lift that is still 25-37x short of the 0.1 bar**. `e1coe_score_var(h=1)` moves from ~1e-15 to 6.9e-09 - 1.5e-07, still **5-7 orders below** its 0.002 bar. Denominator health is fine throughout (`CR_real` 0.17-0.26, n=40 at h=1; seed123 h=30 clears the n>=10 floor by exactly 1, the same marginal tail 954 carried, and it does not touch h=1).

**Vacuity traps genuinely closed.** `missing_action_calls == 0` on every ON cell (the counter is reachable and increments on the real `actions=None` fallback path, so it would fire on the exact 954-lineage failure); `direct_action_supply_fraction == 1.0`, computed at the call site off the literal tensors passed. Four of the five preconditions -- `encoder_trained`, `real_zworld_nondegenerate_h1`, `no_missing_action_calls`, `direct_action_supply_fraction` -- were swept and all genuinely discriminate.

## The defect: C1 is decided by float32 rounding, in both directions

**A_off's DV is analytically pinned to zero.** All ten pairwise distances are *exactly* 0.0 in both seeds. This is correct by construction: the OFF branch of `predict_long_horizon` never reads `actions`, and Phase 4c holds `total_curr` bitwise fixed with `reset_hidden_state()` before each of the K calls, so the K predictions are bitwise identical. (That exact zero is simultaneously *excellent evidence the probe's isolation is clean* -- it proves the hidden-state reset works -- and *a useless denominator for a ratio criterion*. Both are true.)

**But C1 does not divide by the pairwise distance; it divides by `contrast_ratio`,** which is `spread / ||centroid||` over the five identical vectors. `spread` is then nothing but float32 rounding residue in the mean-and-subtract: `1.67e-08 / 5.37e-08`. Reproduced independently here -- five bitwise-identical float32 vectors of the observed norm through the same function give `cr ~ 1.8e-08`, matching the manifest's order.

Three consequences, each verified by execution rather than inspection:

1. **The headline number is meaningless.** `measured: 57809.12` against `threshold: 6.101` is ON divided by rounding residue. It is not an effect size; in float64 it would move by orders of magnitude.
2. **The threshold derivation is circular on noise.** `LIFT_FACTOR = max(3.0, 2.0 x (1.4966e-07 / 4.906e-08)) = 6.101`. The "measured OFF-arm cross-seed noise ratio" -- the run's explicit defence against inherited constants ("never an inherited historical constant") -- is **the ratio of two rounding errors**. The smoke recorded in the queue note makes this visible from the other side: at one seed the ratio is trivially 1.0 and LIFT_FACTOR simply floors at 3.0.
3. **The verdict is unstable in BOTH directions.** Had the mean rounded exactly, `off_ratio == 0.0` -> `rel_lift = NaN` (driver line ~1088 guards on `off_ratio > 0`) -> `rel_ok = False` -> all four cells fail -> label `action_conditioning_no_lift`, **status FAIL** on a substrate that demonstrably works. Confirmed by running the driver's own expression on both values. So the PASS/FAIL boundary here is decided by float32 jitter.

**The "both-tails" guard did not close this.** The driver invokes the V3-EXQ-936a both-tails-need-floors lesson, but the `abs_lift` tail is itself denominated on the OFF arm (`on_abs >= 2.0 * off_abs`, i.e. 2x the residue). Only `ABS_ACTION_CR_FLOOR = 1e-7` is genuinely absolute, and it sits ~10x above the residue rather than at any level tied to the E2 2.8e-2 reference or the 5.6e-6 prior. All three tails therefore collapse to one effective question: **"is the ON arm's per-action contrast ratio above 1e-7?"** -- a wiring check. That question is real and was not guaranteed to pass (954's red-team localised a ~675x LSTM+output_proj crush that could plausibly have swallowed the direct channel too), so C1 is *not* unfailable-by-construction. What it cannot do is measure the magnitude its own `statement` claims -- "material lift toward E2's trained per-action reference" -- because no tail references that reference at all.

**Provenance of the criterion does not check out.** The driver attributes both its Phase-4c protocol and "ITEM 1's OWN acceptance criterion" to the SD doc. `docs/architecture/sd_e1_rollout_consistency_training.md` contains **no numeric acceptance criterion and no "Reference measurement" protocol at any revision**, including the exact commit the queue note cites (`1f8870d290`). The quoted protocol text traces to the **V3-EXQ-954 driver's own docstring**; the quoted "smoke measurement" traces to `substrate_queue.json`'s `implementation_hint`. These are misattributions, not fabrications -- but they are what let a criterion authored by the same session that then passed it read as inherited and pre-registered.

**The positive control is keyed to the wrong statistic.** `off_arm_reproduces_954` is a one-sided ceiling (`OFF ratio < 1e-3`) on the Phase-4c statistic, which is structurally zero -- so an exactly-zero arm and 954's attenuated-but-real 4.76e-07 both pass, and the check cannot verify the "faithfully reproduces the known action-blindness signature" claim its own description makes. The scientific intent *is* independently satisfied, but by a different, non-gating number in the same manifest: `cr_ratio(h=1)` at `4.14e-07 / 4.05e-07`. A two-sided band on **that** statistic is the control this run should have carried, and it would have passed.

## Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | n/a | `claim_ids: []` by deliberate, and correct, design -- tagging MECH-135/INV-088 here would have been the speculative tagging the claim_ids accuracy rule forbids |
| Biological reference | clear | action-conditioned forward models (efference copy); ITEM 1 brings E1 to the interface standard SD-056 already set for E2 |
| Prerequisites | present | SD-070 warmup, 954-identical phases; substrate provenance verified by ancestry |
| Implementation | complete | the `actions=` channel exists, is exercised, and carries signal; vacuity traps reachable and closed |
| Environment | adequate | `CR_real` 0.17-0.26 at every horizon, n=40 at h=1 |
| Measurement | **MIXED** | recording complete and cells correct; the **gating criterion** denominates on an analytically-zero control and its stored `statement` carries a provenance claim that does not trace |
| Integration | coupled | real REEAgent pipeline, fresh training per the 954 recipe |
| Scale | adequate / inadequate | adequate for the qualitative wiring verdict; inadequate for the magnitude claim C1 asserts |

**Failure-location (GOV-FAILLOC-1): n/a** -- diagnostic PASS, and no observation here is described as evidence REE itself failed. The residual evaluator degeneracy is already SD-e1-rollout-consistency-training ITEM 2's subject. Recorded per the 954 precedent rather than forced into a bucket.

## Read-across (verified, NOT adjudicated here)

1. **The 954 substrate handoff was only partly applied.** `substrate_queue.json`'s `SD-e1-rollout-consistency-training` entry carries `severity: null`, `substrate_paths: null`, and a `failure_record` containing only the 108b run -- the 954 autopsy's recommended `severity: corrupting`, its two `substrate_paths`, and its `failure_record_entry` were all dropped. The `implementation_hint` re-scope and the `complicated (buildable)` reclassification did land. **Practical cost:** `/queue-experiment` Step 2.5c reads exactly `severity` + `substrate_paths` to gate unrelated experiments against a corrupting substrate, so that gate is currently **inert** on an entry an autopsy classified corrupting. GOV-APPLY-1 reads `per_claim_recommendation` only, so there is no standing scan on the substrate side and this was invisible.
2. **An already-true `change` tail cleared a row whose disposition was dropped.** 954 recommended `epistemic_category: standard` for both claims. MECH-135 carries it; **INV-088 still carries none** -- yet INV-088's GOV-APPLY-1 row self-cleared, because its `change` string ends `-> diagnostic_evidence_adjudicated`, which *did* land. This is the already-true-tail hazard the skill documents, observed live in this corpus.
3. **The sub-flag ablation returns a null, and the flag defaults ON.** `action_cond_unzero_self_slot` is the reason the design doc gave for keeping the two defects separately ablatable -- and un-zeroing contributes nothing measurable: C_both <= B_action on 3 of 4 h=1 comparisons (s123: 5.35e-04 vs 7.69e-04). With n=2 seeds this is a null, not a refutation. It matters because `E1Config` defaults `action_cond_unzero_self_slot` to **True**, so enabling the master switch in production silently selects the arm this run gives no evidence for.

## Learning extracted

1. **A control arm pinned analytically to zero is excellent probe hygiene and a useless ratio denominator.** The same design property that proves the isolation is clean (bitwise-identical inputs -> bitwise-identical outputs) destroys the denominator of any ratio criterion built on it. When a control is zero *by construction*, gate on an absolute reference, never on ON/OFF.
2. **"Derived from this run's own measured baseline" is only a defence when the baseline measures something.** The idiom is a genuine guard against inherited constants and was applied in good faith here -- but applied to a quantity that is float32 residue, it launders noise into a threshold. Check that the derived-from quantity has a physical interpretation before crediting the derivation.
3. **A criterion whose verdict flips on rounding is unsound even when it happens to give the right answer.** This run would have reported FAIL had the residue rounded to zero. Sound-in-substance is not sound-in-mechanism, and only the second survives being re-run on another machine or dtype.
4. **Attribution launders authorship.** Citing a criterion to a design doc that does not contain it makes a self-authored bar read as pre-registered -- which is precisely what stops the next reader from auditing it. Quote-check provenance claims in driver docstrings against the cited artifact.
5. **A partially-applied autopsy handoff is invisible to the standing scans.** GOV-APPLY-1 covers the claim side only; nothing audits whether `recommended_substrate_queue_entry` was applied, and an already-true `change` tail can clear a claim row whose other recommendations were dropped.

## Disposition (user-confirmed)

- **Adjudication:** GENUINE finding, UNSOUND criterion. The self-route label `action_conditioning_converts_both_arms` is **accurate**; the number behind it is not interpretable. ITEM 1 is validated as delivering a real per-action signal on a trained model -- established by the recorded pairwise distances and the non-gating `cr_ratio(h)` sweep, **not** by C1.
- **`epistemic_category: standard`**, `evidence_direction: non_contributory`, no `per_claim_recommendation` (claim-free target; MECH-135/INV-088 keep `pending_retest_after_substrate: true` and were already flagged `diagnostic_evidence_adjudicated` by the 954 cycle).
- **Do NOT unblock the MECH-135 / INV-088 retest yet.** ITEM 1 landing is necessary but not sufficient: a retest run today would still meet a `cr_ratio(h=1)` 25-37x short of 0.1 and an `e1coe_score_var` 5-7 orders short of 0.002.
- **Routing: implement-substrate** -- amend `SD-e1-rollout-consistency-training` per `recommended_substrate_queue_entry`: record ITEM 1 validated (with the scope caveat), append the 965 failure record as ITEM 2's baseline, **restore the dropped `severity: corrupting` and `substrate_paths`**, and fire the design doc's own pre-registered branch. The 954 failure record stays **open**: its stated target (`cr_ratio(h=1) >= 0.1`) is unmet.
- **The design doc's pre-registered branch FIRES.** It says: "If the item-1 ON arm still shows crushed per-action divergence at the E1 output, that [`output_proj` absolute-vs-residual] parameterisation is the next thing to test." The ON arm *is* still crushed relative to the evaluator bar. That branch is now live, and it is emitted as a two-leg `fanout_recommendation` (GOV-FANOUT-1) rather than a single build, following the 954 lineage's own recorded lesson that a cheap probe before the build re-scoped ITEM 1 for 49 seconds of compute.
- **Nothing spawned by this session** (2026-07-30 rule): the routing above is a proposal for `/governance` Step 2b to ratify before any chip.

**Re-derive brake: not applicable** -- claim-free target, so there is no claim to count ceiling hits against; and this validates a substrate that did not exist before 2026-08-29. **Granularity trigger: not applicable** -- no claim_ids to run the cluster reader on.

**Step 7b:** 0 fires -- but C1/C2/C3 structurally inapplicable (claim-free target) and C5 inapplicable (no sibling `.md` at draft time), so only C6-narrow could look. Step 7c carried the load, as the skill requires when the mechanical checks are blind.

**Step 7c (adversarial red-team, cross-model -- Fable, not the drafting model): CONFIRMED.** It recomputed the 25-37x shortfall, all four `relative_lift` values, and the LIFT_FACTOR derivation bit-for-bit from the manifest's own cells; independently reached the NaN-FAIL instability (which the draft had understated); source-verified the fan-out premises (`output_proj` absolute in `e1_deep.py`, residual in `e2_fast.py`); verified substrate ancestry; swept all five preconditions and found only C1 defective. It added the dropped-954-`failure_record` finding (F6), the sub-flag null (H3), and a lift-range correction (6455x, not 6476x) -- all three verified here independently before adoption.
