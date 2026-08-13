# Failure Autopsy: V3-EXQ-228d (ARC-032)

**Generated:** 2026-08-13T05:24:45Z
**Scope:** single
**Status:** confirmed
**Dry-run check:** clean

## 1. Facts

- **Run:** `v3_exq_228d_arc032_theta_phase_weighted_readout_20260811T234236Z_v3`, queue_id V3-EXQ-228d, claim_ids `["ARC-032"]`, `supersedes: "V3-EXQ-228c"`. Machine `ree-worker-3`, elapsed ~3.8h, seeds [42,43,45] (44 deliberately excluded, known per-seed instability per EXQ-539/540). Recording provenance clean.
- **Precondition** (`goal_norm >= 0.05`): **met**, 1.00 frac seeds.
- **C1 persistence** (`active-zeroed cos >= 0.02`): **FAIL** 0/3. `persist_delta_mean = -2.72e-07` (std_effect -0.12) — essentially zero both arms.
- **C2 prox-noise** (`zeroed-active >= 0.005`): **FAIL** 0/3. `noise_delta_mean = -0.1095` (std_effect **-6.10**) — large, consistently REVERSED. `reversed_noise_frac_seeds = 1.00`.
- `persistence_cos_mean` is ~0.999997 in **both** conditions across **all** seeds — near the numerical ceiling of cosine similarity, raising a genuine measurement-adequacy question for C1 specifically, newly flagged by this autopsy.
- `e3_tick_ratio ≈ 0.066–0.081` confirms the ablation only bites on the E3-tick-restricted window as designed; ablation confirmed non-inert via arm fingerprints.

## 2. Lineage — the load-bearing narrative

228/228a: precondition never cleared (`non_contributory`). **228b** (2026-08-09, first to clear precondition): measured a downstream behavioral proxy, FAILED 0/3, autopsy diagnosed two measurement defects (E3-tick cache-gating dilutes ~89% of readout; wrong DV — claim names persistence/proximity-noise, not resource-lift). Routed `/queue-experiment` → **228c**. **228c** (2026-08-09/10): first fair, E3-tick-restricted, direct-DV test — FAILED 0/3 with a REVERSED trend (theta ACTIVE noisier 3/3, less persistent 1/3). Autopsy diagnosed a biology-divergence implementation gap: `ThetaBuffer.summary()` was a flat unweighted mean (permutation-invariant), unable to represent the phase/sequence-order structure the literature attributes theta's function to. Routed `/implement-substrate` → **SD-100** (landed 2026-08-10): a literature-grounded von-Mises-style forward-sweep phase kernel replacing the flat mean, gated behind `use_theta_phase_weighted_summary` (default off, bit-identical). **228d (this run):** retest with SD-100's kernel enabled — **everything else held bit-identical to 228c's mechanism** (THETA_ZEROED unchanged, bypasses `ThetaBuffer.summary()` via monkeypatch).

**The driver script's own docstring explicitly pre-registered this exact outcome and its governance implication before the run executed**: "if 228d again shows a consistent reversed direction even under the phase-weighted summary, that is a STRONGER finding than 228c's... the reversal is not attributable to the flat-mean's permutation-invariance specifically... flag this explicitly for governance rather than silently re-routing to another /implement-substrate cycle." **This is exactly what happened.**

## 3. Claim-layer mapping — ARC-032

"The theta-rate packaging of E1 output (MECH-089 ThetaBuffer) is the primary pathway through which E1's goal-context maintenance reaches E3's trajectory scoring — the computational analog of frontal-hippocampal theta synchronisation." `claim_type: architecture_hypothesis`, `status: candidate`, `epistemic_category: substrate_conditional` (pre-existing). `depends_on`: MECH-089 (implemented/active), MECH-116 (candidate but functionally wired). This is the **second** fair, direct-DV, precondition-cleared test (228c and 228d) using the claim's own pre-registered confirming readouts, after the specific implementation gap the prior autopsy diagnosed was fixed and re-verified non-inert.

## 4. Biological-reference triage

Frontal (mPFC)–hippocampal theta phase synchrony supporting goal-directed navigation (Benchenane 2010, Hyman 2010, Sigurdsson 2010 disruption model), with phase/order-coding specifics from theta-sequence compression (Dragoi & Buzsaki 2006) and theta-gamma phase nesting (Colgin 2016). A dedicated 4-entry lit-pull directory exists — this is a well-lit-supported claim. **228c flagged the original flat-mean summary as a formal/engineering simplification with no phase-coding content** — a genuine biology-divergence gap. SD-100's replacement is a deliberate, literature-grounded translation attempt (citing Dragoi/Colgin directly, degrades gracefully to the old flat-mean at κ=0). **228d tests a genuinely improved translation, not a repeat of the same formal-import defect** — and the reversal persisted anyway.

## 5. Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | weakened | Two consecutive fair tests both reverse on the noise criterion |
| Biological reference | clear, translation improved but still diverges empirically | Well-grounded; SD-100 addressed the diagnosed gap without flipping the direction |
| Prerequisites | present | MECH-089, MECH-116 both exercised |
| Implementation completeness | complete | SD-100 fully built, validated, non-inert |
| Environment adequacy | adequate | Same validated curriculum/scaffold recipe as 228b/228c |
| Measurement adequacy | mixed — C2 adequate, C1 possibly ceiling-saturated | C1's persistence_cos sits at ~0.999997 in both arms — may lack dynamic range, independent of ARC-032's truth |
| Integration adequacy | coupled, confirmed non-inert | Ablation demonstrably changes trajectory-candidate generation |
| Scale/capacity | adequate | Not implicated |

**Failure-location (GOV-FAILLOC-1):** MECHANISM FAILED as the sole explanation is now RULED OUT (SD-100 is complete and correctly targeted) — leaving a partial REE-FAILED signal specifically on C2 (the noise readout, robust and twice-replicated across two structurally-independent implementations), while C1 stays genuinely ambiguous (ceiling effect, not evidence either way).

## 6. Re-derive brake & granularity-debt checks

- **Re-derive brake (literal):** 0 — no prior autopsy in this lineage used the exact `substrate_ceiling` string (categories used: `measurement_test_design_defect` x5, `precondition_unmet` x1, `substrate_conditional` x1). **De facto trigger, treated as fired:** this is a **third distinct build-fix-retest cycle** (precondition-fail → measurement-defect fix → implementation-gap fix) with no resolution, which is the qualitative pattern the brake exists to catch even though no prior artifact used the literal enum value. A same-claim `/implement-substrate` re-queue is **not** recommended without a concrete new hypothesis.
- **Granularity-debt:** 6 targets across 4 files, alignment distribution `other=4, weakened=2` (228b, 228c). 228d would be a 7th target, a 3rd `weakened`-type reading, and its failure signature (reversal under a *different* summary mechanism) is structurally different from 228c's — a genuinely new, independent confirmation, not duplicate noise. Does not fire `/claim-synthesis` routing on its own.

## 7. Recommended epistemic_category

`standard` — down from the pre-existing `substrate_conditional`. The substrate gate that justified `substrate_conditional` (SD-100) has now been built and tested; carrying the conditional forward without a concrete, scoped next hypothesis would leave the claim in permanent-pending limbo. If governance wants one more probe, `substrate_conditional` could be re-asserted with a narrower, explicitly-scoped gate (e.g. a `theta_phase_concentration` sweep) — but that should be a deliberate governance decision, not a default carry-forward.

## 8. Learning extracted

- Two structurally independent theta-summary implementations (flat mean, phase-weighted von-Mises kernel) both show the same reversed effect on the noise criterion — ruling out the specific implementation-gap explanation as the sole cause.
- C1 (persistence) may be measurement-inadequate due to ceiling saturation, independent of ARC-032's truth — a genuinely new nuance.
- The driver script's own docstring correctly pre-registered this exact outcome shape and its governance-escalation implication before the run executed — a model of good pre-registration practice worth noting for future lettered-lineage drivers.

## 9. Routing — CONFIRMED

**Flag for governance re-examination of ARC-032's disposition** (user confirmed the recommended option at the Step 8 gate, 2026-08-13) — **not** a further automatic `/implement-substrate` cycle. `epistemic_category` recommended down to `standard`. A narrowly-scoped `theta_phase_concentration` sweep remains available as a deliberate governance choice if one more probe is wanted.

Draft `evidence_quality_note`: see JSON companion `failure_autopsy_V3-EXQ-228d_2026-08-13.json`.

## 10. Governance apply checklist

- [ ] Append `evidence_quality_note` to ARC-032 in `claims.yaml`
- [ ] Change `epistemic_category`: `substrate_conditional` → `standard`
- [ ] No substrate_queue entry recommended (`action: none`) — governance to decide whether a narrow kappa-sweep probe is worth a future queue entry
- [ ] Re-examine ARC-032's `status`/disposition given the twice-replicated reversed effect
