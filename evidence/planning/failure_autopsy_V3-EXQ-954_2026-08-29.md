# Diagnostic-PASS adjudication: V3-EXQ-954 (E1 horizon sweep + action-divergence probe) — 2026-08-29

**Run:** `v3_exq_954_mech135_inv088_e1_horizon_sweep_action_divergence_probe_20260829T093705Z_v3` · PASS · diagnostic · claims [MECH-135, INV-088] (non_contributory per claim, all label branches) · seeds [42,123] · ree-cloud-2 · self-route `action_blindness_confirmed` · qid `inv088_evaluator_degeneracy_cause`
**Status:** confirmed (interactive gate 2026-08-29; session autopsy-batch-20260829)
**Dry-run check:** clean (full run; the queue-note's smoke was a separately-recorded toy check, not cited as evidence here).

## Facts

The lit-pull SYNTHESIS Section 4 "cheap probe before the build": discriminate (a) horizon-compounding from (b) action-blindness as the dominant cause of the 108b evaluator collapse, BEFORE SD-e1-rollout-consistency-training is designed. Pre-registered decision rule (Section 4.3): (a) predicts smooth degradation with depth (healthy at h=1); (b) predicts already-floored at h=1 plus near-zero direct per-action divergence.

**Observed (both seeds, perfect agreement):** cr_ratio(h=1) = 4.76e-07 / 5.39e-07 vs the 0.1 collapse threshold — floored **before any compounding could occur** — with a flat-to-mildly-rising profile to h=30 (6.05e-06 / 8.16e-06, reproducing 108b's regime); horizon-matched denominator healthy at every h (CR_real 0.17–0.24 ≫ 1e-4); one-step per-action probe ratio 1.23e-06 / 8.77e-07. The (b) signature exactly; the (a) signature absent. Non-degeneracy protections all fired (strict `>` encoder comparator fixing 108b's vacuity; per-horizon sample floors — seed123 h=30 clears by exactly 1 sample, affecting only the tail; probe routed through predict_next_self to avoid the identical-input trap). Structural case code-verified: `forward`/`predict_long_horizon` take no action (e1_deep.py:1126/:758), z_self LSTM slot zeroed (:783-784), forward delegates through the zeroed path (no un-zeroed sibling).

**Attribution gap closed by the red-team pass (new measurement, redteam_954.md):** replicating the recipe with the driver's own functions, trained E2 per-action z_self divergence = **2.8e-2** (~5% of ‖z_self‖) vs **5.6e-6** at the E1 output — a **~5,000× attenuation inside E1** (prior_generator ~7×; LSTM+output_proj ~675×, the dominant crush). E2 is exonerated; the label and routing are safe.

ULP caveat recorded: sub-1e-6 fine structure is float32-noise-level; the routed statistics' being 5–6 orders below threshold is robust.

## Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | intact | every branch non_contributory for both claims — explains the 108b collapse, weighs nothing |
| Biological reference | clear | biological forward models are action-conditioned (efference copy); E1's action-free transition is the measured divergence |
| Prerequisites | present | 108b-identical phases; strict comparator |
| Implementation | complete | probe scope; attribution closed by red-team measurement |
| Environment | adequate | CR_real healthy at every horizon |
| Measurement | adequate | 5–6 orders separation; seed123 h=30 floor margin of 1 recorded |
| Integration | coupled | full pipeline, fresh training per the 108b recipe |
| Scale | adequate | qualitative-signature discrimination, cross-seed agreement |

**Failure-location: n/a** — diagnostic PASS adjudicated genuine; the confirmed substrate defect is already SD-e1-rollout-consistency-training's subject.

## Disposition (user-confirmed)

- Self-route **accurate**; per-claim: MECH-135 and INV-088 both non_contributory, `standard`, `pending_retest_after_substrate` unchanged, **`diagnostic_evidence_adjudicated: true`** for both (SD-099 flag; this and 108-lineage diagnostics are the claims' adjudicated-and-expected zeros).
- **Substrate entry amend** (`SD-e1-rollout-consistency-training`, severity **corrupting** — the 108/108a history shows plausible-looking vacuous verdicts; paths `e1_deep.py::forward` / `::predict_long_horizon`): RE-SCOPE the implementation_hint — **action-conditioning E1's transition is work item 1**; the multi-step/rollout-consistency objective is item 2 (all five lit-pull fixes presuppose an action-conditioned transition; and the ~675× LSTM-stage crush means the objective change stays a real second item). Clear the discharged probe-gating (this probe IS the spike the entry's `complex (probe-gated)` classification waited on → `complicated (buildable)`). Append the 954 failure record.
- **Step 9b (applied in this session):** labelled fan-out growth (invariant 3a) on `inv088_evaluator_degeneracy_cause` — add H-horizon-compounding (axis learning-signal) → ELIMINATED by 954, and H-action-blindness (axis intrinsic-architecture) → CONFIRMED by 954. Git witnesses verified: SYNTHESIS.md (fb581f136e, 2026-08-03T14:32:53Z) pre-registers both legs and the exact re-scope branch; the driver (ree-v3, 2026-08-28) pre-dates the run. H-dynamics-collapse's confirmed resolution STANDS; the growth-event rationale states explicitly that the eliminated child (compounding) is the parent's own recorded basis mechanism — the refinement corrects the basis wording, it does not withdraw the leg. `initial_frozen_count_at_registration` preserved.
- **Routing: implement-substrate** (the amend above). No new experiment needed before the build; the unqueued twin v3_exq_953 stays unqueued. Nothing spawned by this session (2026-07-30 rule).

**Re-derive brake: does not fire** (108a's ceiling read leaves MECH-135 at count 1 < 2; this probe is upstream of the brake's own remedy). **Granularity trigger: does not fire** for either claim on the reader's own distributions (MECH-135: weakened=2 but signatures converge on one diagnosed mechanism now routed to a build; INV-088: 7 targets across axes, this run non_contributory).

**7b:** 0 fires. **7c:** CONFIRMED and strengthened (E2 exonerated by measurement; witnesses verified; three hygiene items adopted).

## Learning extracted

1. The "cheap probe before the build" pattern paid off exactly as designed: 49 seconds and 2 seeds re-scoped a substrate build's first work item before any build effort was spent.
2. A confirmed ledger leg can carry a basis wording a later probe corrects WITHIN the confirmed family — the honest move is labelled fan-out growth of pre-enumerated sub-mechanisms, not silent rewriting of the resolved leg.
3. Report ULP-scale robustly: values ≪ threshold by 5–6 orders is the finding; their fine structure is noise.
