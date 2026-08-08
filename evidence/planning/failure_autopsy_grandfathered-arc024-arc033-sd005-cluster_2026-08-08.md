# Failure Autopsy: SD-005 thread + ARC-024/ARC-033 thread (21 nominal / 19 deduped)

**Generated:** 2026-08-08T17:37:36Z
**Scope:** cluster (19 deduped runs, two independent threads, 2026-03-17 to 2026-05-06)
**Status:** confirmed (Step 8 interactive gate: user confirmed SD-005 formalization + Step 9b registration, ARC-024 redesign+env-fix routing)

## Dry-run gate and deduplication

One dry-run miss caught manually (pre-2026-07 manifests lack the `dry_run` boolean the automated checker relies on): `v3_exq_330a_..._frac05_dry_20260412T102042Z_v3` is a genuine smoke by content (`evidence_direction_note`: "Smoke/dry-run invocation... insufficient training depth... Classified non_contributory 2026-04-13"), already correctly excluded by governance. Two exact-timestamp duplicate pairs found (`045` and `047`, both prefix/suffix naming). **21 nominal -> 19 distinct runs** (Thread 1 SD-005: 12 distinct; Thread 2 ARC-024/ARC-033: 7 distinct).

## Thread 1 -- SD-005 (+ MECH-095/MECH-069 satellites)

**Claim state**: `implemented`, `epistemic_category: standard` (never flagged `substrate_ceiling`). Re-derive brake: 0 confirmed `substrate_ceiling` hits anywhere in the corpus -- this is, in effect, the first formal autopsy SD-005 has received despite ~12 experimental iterations.

**Governance already substantially pre-diagnosed this cluster.** A 2026-08-06 thought-digestion `heterogeneity_note` narrates most of this thread in detail: EXQ-047d/e/f are ruled DESIGN FAILURES, not disconfirmation (frozen probe with no separation objective; unstable adversarial GRL race; geometrically-orthogonal-but-functionally-unspecialised "wrong test"). **EXQ-047g/113/532 (all in this batch) are ruled "the corrected designs"** and all three converge on the same specific asymmetric pattern: **z_self reliably specializes for self/action information; z_world does NOT show reciprocal world-specific specialization** (047g: split-vs-unified action advantage negative; 113: `Decision: retire_ree_claim`; 532: `world_obs_advantage=-0.032`, negative).

**Runs the existing note does NOT individually narrate (real content this autopsy adds):**
- **011** (MECH-095 TPJ proxy, RANDOM policy): mixed. Pre-dates the one MECH-095 PASS by 8 days.
- **013** (SD-005 strict, event-conditional, **RANDOM policy**): weakens, but `body_selectivity_margin=-0.0234` -- backwards. **RANDOM-policy caveat applies -- the exact V3-EXQ-642 trap shape** (untrained-substrate artifact); flag rather than read as an independent ceiling data point.
- **047 (original)**: 4/5, matches the note's own citation.
- **047b (SD-005+SD-010 joint)**: 3/5. Split does NOT improve world-forward R2 over unified (0.9480 vs 0.9648) even after SD-010 removed nociceptive contamination -- **directly contradicts the original 047 note's own stated expectation**; not currently narrated.
- **090 (adversarial split drift)**: manually corrected to `supports` (2026-03-24: "z_self naturally excludes harm... no drift occurred even without adversarial defense"). **Reading tension flagged**: a genuinely null R2(z_self->harm)=0.0000 in both conditions is consistent with either "z_self is clean by construction" (the note's reading) or "z_self simply carries very little of anything reliably" (given 013's low absolute delta-z values). Surfaced at Step 8; user confirmed proceeding with the existing `supports` reading but flagging the tension explicitly in the note.
- **047i/047j (TPJ routing satellites)**: already implicitly folded into MECH-095's extensively-documented substrate-ceiling chain (brake already fired, repointed to `multi_agent_ecology_v5:MAE-3` via V3-EXQ-741). No new MECH-095 action owed.

**Biological-reference triage**: `targeted_review_connectome_sd_005/` (Friston 2016, Keysers 2009, Wolpert 1998, Farrer 2002) and `targeted_review_reafference_streams/` (Blakemore 2002, Gu 2008, Haak & Beckmann 2018, Rolls 2023) both present, pulled essentially concurrently with the batch's earliest runs. Genuine biological mechanism, not a bare formal import -- default "translation gap, not falsification" applies strongly. SD-005's own note already identifies the likely correct next architectural move: use E2 prediction as the primary reafference signal (a predictive-coding comparator) rather than static geometric separation.

**Four-layer diagnosis (SD-005 cluster)**:

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened (world side specifically) | z_self specializes reliably; z_world does not, consistently across 3 corrected designs |
| Biological reference | clear, partially formal-imported | efference-copy biology strong; tested mechanism (static geometric separation) a weaker translation than a predictive-coding comparator would be |
| Prerequisites | present (SD-010 landed, didn't fix world-side calibration per 047b) | |
| Implementation | partial | E2.world_forward reafference-signal redesign not yet built |
| Environment | partial | 113 flags scale/warmup confound at 6x6 |
| Measurement | adequate in corrected trio; degenerate in 013/011 (RANDOM policy) | |
| Recording | universal gap (no substrate_hash/config/seeds, pre-dates Recording Standard) -- no ceiling read here is falsifiable against a specific substrate commit |

**Recommended routing**: the corrected trio (047g/113/532) -- **formalize the existing claims.yaml reasoning and register the "z_self specializes / z_world doesn't" hypothesis in `hypothesis_space_registry.v1.json` via Step 9b** (see below). 013/011 -> `measurement_gap`/`precondition_unmet` (RANDOM-policy trap), not fresh weakens data. 090 -> keep `supports` but the tension is explicitly recorded. 047b -> record as a genuine new weakens data point against SD-010's predicted fix. The E2-prediction-as-reafference-signal redesign the claim's own note names is the natural next `/queue-experiment`/`/implement-substrate` candidate -- surfaced, not chipped.

### Step 9b -- hypothesis-space ledger

No existing `qid` in `hypothesis_space_registry.v1.json` names SD-005. This autopsy resolves a genuinely new question in the same edit it registers it (Mode B, new-question shortcut): the "z_self specializes for self/action information; z_world does not show reciprocal specialization" finding, adjudicated by the corrected trio (047g/113/532), `pre_registered_utc` set to `<=` the earliest of the three runs' completion dates. See registry diff landed alongside this artifact.

## Thread 2 -- ARC-024 / ARC-033 (+ SD-011/SD-013/MECH-102 satellites)

**Claim states**: ARC-024 `provisional` (0 confirmed ceiling hits). ARC-033 `stable` (promoted 2026-08-07 via V3-EXQ-525, not in this batch; 2 ceiling hits exist but on a different, earlier non-batch run, superseded by the stable promotion). SD-011 `stable`. SD-013 `provisional`. MECH-102 `active/substrate_conditional` (deliberately NOT substrate_ceiling, V5-bound).

**095b (ARC-033/SD-011) -- already fully diagnosed, already resolved.** The FAIL (R2=0 on harm forward models despite loss decreasing) is explicitly diagnosed in ARC-033's evidence_quality_note as a measurement-target problem: `harm_obs_s` variance near-zero at single-step resolution, so any model converges to the conditional mean trivially. Fix (harm-delta target, EXQ-166e) subsequently built, validated, and drove ARC-033's stable promotion via 166e->353->525. `measurement_gap`, no new routing -- fix already shipped.

**330a (SD-013) -- already fully diagnosed, already resolved.** Explicitly narrated: "threshold calibration issue, not mechanism failure." The full-budget 330a's raw-Euclidean 2.0x threshold is too strict relative to the normalized-gap 1.2x threshold the contemporaneous EXQ-353 cleared. `measurement_gap`, already closed.

**107 / 117 (ARC-024) -- genuinely fresh, real new finding, this autopsy's main contribution.** Neither appears in ARC-024's evidence_quality_note. Both test the claim's core architectural prediction (continuous pre-contact harm/benefit gradients in z_world) via cross-decoding probes on the learned latent -- a higher bar than EXQ-028/029's raw-observation test.
- **107** (5 seeds): pre-contact gradient FAILs at 0.0030, over 25x below threshold (0.08). AUC discriminability passes (0.6477); some signal present, just not the specific gradient structure.
- **117** (2 seeds, redesigned after 107, doubled warmup): harm gradient still fails. **`n_benefit_approach=0` in both seeds -- the benefit arm is currently untestable, not merely unconfirmed** (a genuine environment/labeling gap: resource-proximity "approach" events apparently never fire the way hazard-proximity ones do).

**Biological triage (ARC-024/ARC-033)**: `targeted_review_arc_024/` (Fanselow 2022, Seymour 2004, Mobbs 2007, pulled 2026-03-28 -- the same day as 107/117, plausibly a direct response). `targeted_review_arc_033/` (Bursztyn 2006, Case 2016, Chen 2023, Geuter 2017, Song 2021, Treede 1999). Biology strongly supports proximity/imminence gradients as a real phenomenon -- 107/117 read as an encoder/training-scale translation gap, not claim falsification.

**045 (MECH-102/ARC-024)** -- already loosely absorbed into MECH-102's aggregate 8+-operationalization substrate-conditional note ("ethical" operationalization); recommend citing 045 explicitly by number (documentation completeness), no new routing.

**Four-layer diagnosis (thread 2)**:

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact for ARC-033/SD-011/SD-013 (resolved); weakened for ARC-024 specifically on pre-contact-gradient-in-latent-geometry | |
| Biological reference | clear for both | Strong, contemporaneous literature pulls |
| Prerequisites | present | SD-010/SD-011 landed before 095b/117 |
| Implementation | complete for ARC-033; partial for ARC-024 (gradient-geometry encoder objective not built) | |
| Environment | inadequate specifically for ARC-024's benefit arm | 117: n_benefit_approach=0, event-labeling gap |
| Measurement | root cause for 095b/330a (both now fixed); adequate for 107/117 | |
| Recording | same universal gap as Thread 1 | |

## Recommended routing summary

**Thread 1**: 047g/113/532 -> formalize + Step 9b register. 013/011 -> RANDOM-policy caveat, not a fresh data point. 090 -> keep `supports`, tension recorded. 047b -> new weakens data point. `governance-note-only` for the whole thread; the redesign direction (E2-prediction reafference signal) surfaced, not chipped.

**Thread 2**: 095b/330a -> `measurement_gap`, `governance-note-only` (already resolved downstream). **107/117 -> `/queue-experiment` redesign** (larger warmup budget and/or an explicit gradient-propagation training objective for z_world -- `complex (probe-gated)/puzzle`) **plus a prerequisite environment fix** (benefit-approach event labeling in `CausalGridWorldV2` -- `complicated (buildable)`) before the benefit arm is testable at all. Not a claim-layer demotion for ARC-024. 045 -> cite explicitly, no new routing.

## Re-derive brake state (R1-R3)

SD-005: 0 hits. ARC-024: 0 hits. ARC-033: 2 hits (pre-batch, different run, superseded by stable promotion). SD-011: 2 hits (same pair, double-counted across tags; claim already stable). SD-013: 0 hits. MECH-102: 0 hits. No brake fires for this batch on any thread-2 claim.

## Learning extracted

1. SD-005's corrected trio (047g/113/532) is a clean example of governance prose already containing autopsy-grade diagnosis -- this artifact's job was largely formalization + Step 9b registration, not fresh derivation.
2. 013/011 (RANDOM-policy runs) are the batch's clearest instance of the V3-EXQ-642 self-route trap -- a manifest reading `weakens` that is actually an untrained-substrate artifact.
3. 107/117 are the batch's genuinely fresh content -- ARC-024's core architectural prediction has never been cleanly tested at the latent-geometry level, and 117 additionally surfaces a real environment-labeling gap (benefit-approach events never fire).
4. Both threads have strong, contemporaneous biological literature support -- neither shows the SD-003-style "formal import with no biology" failure mode.
