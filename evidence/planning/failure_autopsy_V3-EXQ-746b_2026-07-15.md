# Failure Autopsy — V3-EXQ-746b (INV-089 harm-evaluator z_harm calibrated bound, variance-reduced)

- **Generated (UTC):** 2026-07-15T14:10:27Z
- **Scope:** single
- **Status:** confirmed (interactive gate answered)
- **Target run_id:** `v3_exq_746b_inv089_harm_eval_z_harm_bound_variance_reduced_20260715T134512Z_v3`
- **Queue id:** V3-EXQ-746b · **extends** V3-EXQ-746a · **claim:** INV-089 (emergent invariant, provisional)
- **Manifest outcome:** FAIL, `non_degenerate=False`, `evidence_direction=unknown`
- **Machine:** ree-cloud-2 (linux-x86_64-py3.10), 267 s · **substrate_hash:** `4327aab4…` (freshly minted prefix; cache 0 hit / 40 miss)

## Lineage

| Run | Preconditions | Outcome | Degeneracy mode |
|---|---|---|---|
| V3-EXQ-743 | met | PASS (positive control) | — (promoted INV-089 candidate→provisional 2026-07-12) |
| V3-EXQ-746 | unmet | FAIL, superseded | DV starved: undecodable single-cell target + un-clipped DV head → numerical blow-up (seed-3 −6.3e7); IV inert |
| V3-EXQ-746a | **met** | FAIL, **weakens** | none — but the weakens is a **DV measurement artifact** (unregularised head overfit ~490 pts, held-out R² −26…−166) |
| **V3-EXQ-746b** | **unmet** | **FAIL, starved** | **IV starved:** `PC_iv_moved=False` (mean_iv_delta +0.0020, mean_iv_rho −0.037) |

Three iterations, **the bound-coupling test has never validly run** — each letter fixed a genuinely different, diagnosed measurement pathology (746: DV target/clipping; 746a→746b: DV estimator; 746b→746c owed: IV/DV data-budget coupling).

## Facts (no interpretation)

**Failed criterion = a PRECONDITION (`PC_iv_moved`), not a discrimination or absolute criterion.** So this is *not* the substrate-ceiling fingerprint ("negative control passes, discrimination fails"). It is a starved bound test.

Primary target `dens` (local neighbourhood density), 8 seeds, onset {0,1,4,12,30}:

| Quantity | 746a | 746b | Read |
|---|---|---|---|
| `mean_iv_delta` (onset-max − onset-min) | +0.0320 | **+0.0020** | IV onset gradient collapsed |
| `mean_iv_rho` (Spearman onset,IV) | +0.5125 | **−0.0375** | per-seed scattered −0.8…+0.9 |
| `mean_iv_mature` (mature-anchor decodability) | 0.398 | **0.422** | z_harm still decodes density well at maturity — *higher* than 746a |
| `PC_dv_estimator_ok` | (n/a) | **True** | DV head now beats the mean at maturity |
| `mean_dv_mature` | garbage (R² −26…−166) | **0.451** | **DV-estimator fix succeeded** |
| `PC_iv_moved` | True | **False** | ← the starve |

Recording core complete (`validate_recording` OK: recording_schema, substrate_hash, machine/class, elapsed, config, seeds all present). **Not a recording-debt case.**

## Load-bearing positive finding (surfaced, not buried)

746b's whole purpose — repairing the DV estimator (standardise target · K=5 folds · weight-decay + early-stop · finite R² floor · collect 14→60) — **worked**: `mean_dv_mature = 0.45`, comparable to the IV ridge (0.42). In 746a the identical head produced held-out R² of −26…−166. **This retroactively supports the author's diagnosis that 746a's "weakens" — the current live evidence weakening INV-089 — was a DV measurement artifact, not a real null.** But 746b did *not* deliver a valid bound test (IV starved), so the DV-viability is confirmed only at the single mature anchor, not across a moving IV. It is a **partial** confirmation: the estimator *can* be viable; the coupling was not tested.

## Why the IV went flat — the third, unanticipated degeneracy mode

The one change made for DV power (`collect_episodes 14→60`, ~195→~780 samples) washed out the IV onset gradient. Mature-anchor IV *rose* (0.42 vs 0.40), so the implied onset-0 IV climbed to ~mature level and the delta collapsed to ~0. **The onset gradient 746a rode on (delta +0.032, rho +0.51) looks substantially like a small-sample underfitting artifact of the sparse collect=14 IV probe:** with adequate probe data, z_harm decodes local-density about equally well whether immature or mature. The extra data lifted the IV *floor* as much as its ceiling.

This is scientifically load-bearing beyond the measurement: if "z_harm differentiation grows with maturation" for local-density is largely a probe-sampling artifact, the very IV that INV-089's bound rides on is fragile for this target.

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (untested) | IV starved → bound could not express itself; no claim pressure either way. INV-089 stays provisional. |
| Biological reference | n/a | pure measurement calibration; no biology divergence, no formal-import divergence |
| Prerequisites / substrate | present | SD-010 HarmEncoder + harm_eval_z_harm IMPLEMENTED — **no substrate build owed** |
| Implementation (DV estimator) | **fixed / complete** | the 746b repair is validated at maturity (0.45) |
| Environment | adequate | regime unchanged (scheduled_external_hazard OFF), correct |
| Measurement (IV probe) | **inadequate / coupled** | widening collection for DV power destroyed the IV onset contrast; sparse-IV gradient likely underfitting artifact |
| Integration | coupled but unstable | IV-power and DV-power are anti-coupled in the shared collection budget — the core defect |
| Scale / capacity | adequate | not a data-volume problem; a data-*allocation* problem |

**Node classification (work-graph debt vocabulary):** `complex (probe-gated) / puzzle (known rules)` shading toward `mystery (known data)`. Frame (bound-coupling) is well-posed; the missing fact is whether *any* target + adequate-sampling regime yields a z_harm differentiation that genuinely grows with maturation while the DV stays viable. The collect=14-vs-60 comparison already hints (mystery flavour) that local-density's gradient is sampling-dependent; confirming a workable target needs a spike (puzzle flavour). → `/queue-experiment`.

## Recurrence / re-derive brake

- Prior INV-089 `substrate_ceiling`/`non_contributory` autopsies = **0** → **re-derive brake does NOT fire** (threshold 2). This is a live-measurement-design fix with existence proofs (746a IV-moves, 746b DV-viable), not a substrate-ceiling verdict.
- This is the **second autopsy circling INV-089** (the first: `failure_autopsy_morning-digest-742-744a-745-746-746a_2026-07-13`). But the three failures are measurement-instrument iterations of *one* bound test, not structurally-distinct claim pressures from different mechanisms → **not** true granularity debt; `granularity_debt_trigger.fires = false`. (The one construct concern — "z_harm differentiation" being under-operationalized — is noted for the user; they may still choose /claim-synthesis if they read INV-089's bound sub-claim as needing decomposition.)

## Learning extracted

1. **The DV-estimator fix is validated** (mean_dv_mature 0.45 at the mature anchor) → 746a's "weakens" is measurement-suspect; the current INV-089 weakens should carry that caveat.
2. **A new degeneracy mode:** IV-power (onset contrast) and DV-power (estimator generalisation) are **anti-coupled in a shared collection budget.** Fixing one starved the other. The two probes must draw independent data budgets.
3. **The local-density onset IV gradient may be a small-sample artifact** (collect=14 underfit at low onset). A valid bound test must (a) use adequate sampling for both legs and (b) verify the target's z_harm differentiation genuinely grows with maturation under that sampling — explicitly measuring the onset-0-vs-mature IV gap.

## Routing (user-confirmed at interactive gate)

- **746a weakens → Annotate, keep weight.** Governance keeps 746a's weakens active and adds an `evidence_quality_note` caveat (drafted below). Not superseded — 746b delivered no PASS.
- **Bound test → 746c careful redesign** via `/queue-experiment` (same scientific question → alphabetic suffix). Decouple IV/DV data budgets; adequate sampling for both legs; a deliberately maturation-dependent target; explicit onset-0-vs-mature IV-gap readout to rule out the sampling artifact; retain the 746b DV-estimator fix. **Not** `implement-substrate` (SD-010 already implements the machinery). **Not** a naive sparse-IV letter (risks reinstating the underfitting artifact).

## Draft `evidence_quality_note` for governance to write

**On the 746b manifest (bound-test leg — inactive/non-weighting):**
> V3-EXQ-746b FAIL, starved on `PC_iv_moved` (mean_iv_delta +0.002, mean_iv_rho −0.037): the z_harm differentiation IV did not vary across onset, so the bound-coupling test could not run — NOT a falsification, no weight on INV-089's bound. Root cause: collect_episodes 14→60 (added for DV power) washed out the IV onset gradient; mature-anchor IV rose to 0.42, so the implied onset-0 IV climbed to ~mature level. Contributory finding retained: `PC_dv_estimator_ok=True`, mean_dv_mature 0.45 — the DV-estimator fix is validated at maturity, which casts the 746a weakens as measurement-suspect (see 746a note). Route: 746c redesign decoupling IV/DV data budgets.

**Appended to INV-089 / the 746a weakens context (annotate, keep weight):**
> 2026-07-15 (V3-EXQ-746b autopsy — `failure_autopsy_V3-EXQ-746b_2026-07-15`): 746a's weakens is measurement-suspect. 746b repaired the DV estimator (standardised target + K-fold + weight-decay/early-stop + finite floor) and showed `PC_dv_estimator_ok=True`, mean_dv_mature 0.45 — the harm_eval_z_harm head CAN beat the mean at maturity, so 746a's −166 divergence was estimator pathology, not a real null. 746a's weakens is RETAINED (746b did not deliver a valid bound test — its IV starved) but flagged measurement-suspect pending a valid met-both-preconditions bound test (746c). INV-089 stays provisional on 743's single-pathway positive control.
