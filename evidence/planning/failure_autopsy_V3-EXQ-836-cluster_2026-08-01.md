# Failure Autopsy: V3-EXQ-836a + V3-EXQ-836d (MECH-476 redesigned falsifier legs)

Generated: 2026-08-01T10:37:54Z
Status: confirmed (interactive gate completed with user)
Scope: cluster (2 targets, same claim, same shared measurement fix)

## 1. Facts

Both targets are noise-scaled REDESIGNS of legs from the original 3-arm MECH-476 falsifier (V3-EXQ-836 dose / 836b interval / 836c novelty-tagging, all FAILed 2026-07-29 as `non_contributory` / `measurement_test_design_defect` -- the original design used a fixed 0.15 effect-size margin not scaled to observed per-arm noise, per `failure_autopsy_mech476-mech475-cluster_2026-07-29` + `failure_autopsy_v3-exq-836b_2026-07-29`). All three legs were redesigned under an identical noise-scaled convention (`effective_margin = max(EFFECT_SIZE_K=1.5 * sd_delta, EFFECT_SIZE_ABS_FLOOR=0.05)`, seeds 6->10, leave-one-out diagnostics added). Not dry runs (confirmed via `check_dry_run_citations.py`).

### V3-EXQ-836a (dose arm, supersedes V3-EXQ-836)
- Readiness: all 3 dose arms (bc300/bc600/bc900) pass `install_took_strict_majority` at 100%.
- Criterion `resistance_grows_with_dose` (load-bearing): measured `mean_paired_delta = -0.199846` vs `effective_dose_margin = 0.716163` (sd_delta=0.477442). FAIL.
- Dose-axis retained_fraction: `[0.712, 0.430, 0.512]` (bc300/bc600/bc900) -- non-monotone, and the effect magnitude is well inside the noise-scaled margin.
- `non_degenerate: true`, `evidence_direction: weakens`, `interpretation.label: retention_invariant_to_dose_no_process`.

### V3-EXQ-836d (novelty-tagging arm, supersedes V3-EXQ-836c)
- Readiness: both arms (novelty_paired/novelty_unpaired) pass `install_took_strict_majority` at 100%.
- Criterion `paired_retains_more_than_unpaired` (load-bearing): measured `delta = -0.116118` vs `effective_novelty_margin = 0.781809` (sd_delta=0.521206). FAIL.
- paired_retained_fraction_mean=0.8338 vs unpaired=0.9499 -- paired retains LESS, opposite of Moncada & Viola 2007's behavioral-tagging prediction, but well inside the noise-scaled margin (`reversed: false`).
- Leave-one-out: **all 10 folds** (dropping each of seeds 42-51 individually) read `weakened` -- fully robust to single-seed influence.
- `non_degenerate: true`, `evidence_direction: weakens`, `interpretation.label: retention_invariant_to_novelty_no_tagging`.

### The third leg is still pending
V3-EXQ-836e (interval arm, supersedes V3-EXQ-836b) is QUEUED in `ree-v3/experiment_queue.json` under the identical noise-scaled convention but has NOT yet produced a manifest.

## 2. Claim-layer map

**MECH-476** (`competence_retention_dissociable_from_acquisition`, candidate, v3_pending, split_from MECH-457, registered 2026-07-22). depends_on: MECH-457, MECH-459, MECH-460, MECH-475.

The claim's own pre-registered acceptance criteria (`what_would_answer` in claims.yaml) are explicit and were followed faithfully by both redesigned arms: "SUPPORTED if resistance to interference GROWS with install dose and/or with the A->B interval... WEAKENED if retained fraction is INVARIANT to BOTH and tracks only the concurrent constraint coefficient." The claim's own THIRD, separately-falsifiable arm (novelty-tagging, Moncada & Viola 2007) is explicitly framed as "the sharpest available discrimination between 'consolidation process' and 'regulariser.'"

Critically: the pre-registered WEAKENED condition requires invariance to BOTH dose AND interval -- not dose alone. 836e (interval) has not yet reported.

## 3. Biological-reference triage

Strong, multi-citation grounding, all directly on-point:
- Krakauer, Ghez & Ghilardi 2005 -- consolidation-as-resistance-to-retrograde-interference, the source of the dose x interval design.
- Walker et al. 2003 -- dissociable consolidation stages; reactivation returns memory to a labile state.
- Moncada & Viola 2007 -- behavioral tagging: weak training consolidates into long-term memory when paired with novelty exposure close in time.

Both redesigned arms are FAIR, well-instrumented tests of the biological prediction, not translation gaps. The claim's own KNOWN DIVERGENCE note (already recorded, not smoothed by this autopsy) is that REE's two demonstrated protection pathways (distributional critic V3-EXQ-788, KL anchor V3-EXQ-792) are awake/online/undifferentiated, while the biological mechanisms are sleep/replay-dependent and trace-selective -- SD-083's offline EWC-anchor consolidation window (landed 2026-07-29) is the substrate built specifically to close that gap, and both 836a/836d exercise it.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | Both arms tested fairly under the claim's own pre-registered design and acceptance criteria; the noise-scaled redesign specifically fixed the prior cycle's measurement defect. |
| Biological reference | clear | Krakauer 2005, Walker 2003, Moncada & Viola 2007 -- strong, directly on-point grounding for both dose and novelty-tagging predictions. |
| Developmental / dependency prerequisites | present | SD-083 offline EWC-anchor consolidation window landed 2026-07-29; distributional critic (788) and KL anchor (792) protection pathways already validated; RND novelty drive landed (exercised by 836d). |
| Implementation completeness | complete | Both arms correctly implement the pre-registered design; readiness gates (install_took_strict_majority) both pass at 100%. |
| Environment adequacy | adequate | Dose and novelty-pairing are cleanly manipulable parameters; no environment gap identified. |
| Measurement adequacy | **now adequate** (prior cycle's defect fixed) | The noise-scaled effect-size gate (replacing the fixed 0.15 margin) is the correct fix per the project's effect-size-gate convention; leave-one-out robustness (836d: 10/10 folds agree) confirms this isn't seed-driven noise. |
| Integration adequacy | coupled | Offline consolidation window operates correctly between BC install and RL refinement. |
| Scale / capacity | adequate | n=10 seeds per arm (up from 6), matching the redesign convention. |

## 5. Cluster pattern

**Shape**: both legs independently, robustly find retention INVARIANT to their respective manipulated variable (dose; novelty-pairing), using the SAME measurement fix (noise-scaled margin) applied to two structurally different comparisons (a 3-level dose ladder; a paired-vs-unpaired novelty contrast). This is not two independent bugs -- it is the same underlying finding (no detectable dose/novelty-dependent consolidation PROCESS) surfacing consistently across two different experimental designs, now that the measurement artifact that obscured it in the prior cycle (836/836b/836c) has been fixed.

**Reading**: this is `test_design_ceiling` resolved -> now producing a coherent, cross-design-consistent NULL finding, not a `substrate_enrichment` gap. The prior cycle's non_contributory reads were correctly diagnosed as measurement_test_design_defect (not evidence either way); this cycle's weakens reads are the first genuine evidence this falsifier has produced.

## 6. Learning extracted

1. The noise-scaled effect-size-gate redesign (replacing 836/836b/836c's fixed 0.15 margin) works as intended -- both redesigned legs now produce well-powered, leave-one-out-robust verdicts instead of the prior cycle's noise-driven non_contributory reads.
2. Two of the claim's three falsifier arms (dose, novelty-tagging -- including the "sharpest discrimination" arm) now independently and robustly find retention invariant to the manipulated variable, consistent with the claim's own pre-registered "intended failure mode" (no consolidation process, only a regulariser).
3. The claim's pre-registered SUPPORTED/WEAKENED logic requires BOTH dose and interval invariance before the core verdict is warranted -- the third leg (V3-EXQ-836e, interval) is still queued and has not yet run. A claim-level disposition should wait for it.

## 7. Recommended routing

**Recommended `epistemic_category`**: `standard` for both targets (clean, well-powered falsifier results; NOT `substrate_ceiling`, NOT `measurement_test_design_defect` -- that category correctly described the PRIOR cycle, not this one).

**Recommended `evidence_direction`**: `weakens` for both (concur with self-route on both targets).

**Recommended `evidence_quality_note`** (draft text for governance, to be appended alongside the existing 2026-07-29 note rather than replacing it):
> [2026-08-01 failure-autopsy, V3-EXQ-836a + V3-EXQ-836d, confirmed failure_autopsy_V3-EXQ-836-cluster_2026-08-01]: both redesigned legs (noise-scaled effect-size gate, replacing the 2026-07-29 cycle's fixed-0.15-margin defect) now cleanly self-route `weakens`. 836a (dose): retained_fraction actually DECREASES with more BC install dose (0.712->0.430->0.512, non-monotone), effect (-0.1998) well inside the noise-scaled margin (0.7162) for "grows." 836d (novelty-tagging, the claim's own "sharpest discrimination" arm): paired retention is LOWER than unpaired (0.8338 vs 0.9499), opposite Moncada & Viola's prediction, effect (-0.1161) well inside the noise-scaled margin (0.7818); robust across all 10 leave-one-out folds. Both readiness-gated 100% (`install_took_strict_majority`), both `non_degenerate: true`. This is the first genuine (not measurement-artifact) evidence this falsifier has produced, and it points toward the claim's own pre-registered "intended failure mode" -- BUT the claim's WEAKENED condition requires invariance to dose AND interval, and the third leg (V3-EXQ-836e, interval, supersedes 836b) is still queued and has not yet run. **DO NOT change MECH-476's claim-level status until 836e reports** -- record these two `weakens` findings individually, synthesize all three legs together once 836e completes. v3_pending STAYS. PROMOTES/DEMOTES NOTHING at the claim level pending 836e.

**routing**: no further routing action needed from THIS autopsy -- both experiments are complete, well-powered, individually confirmed `weakens`. The one open action is procedural: governance should NOT synthesize a claim-level verdict until V3-EXQ-836e (already queued) reports.

User-confirmed at the interactive gate (2026-08-01): "Record both, hold claim verdict" -- do not treat 2-of-3 legs as sufficient for demotion consideration; wait for 836e.
