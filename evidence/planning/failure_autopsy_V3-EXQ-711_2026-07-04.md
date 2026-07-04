# Failure Autopsy — V3-EXQ-711 (ARC-110 × ARC-108 ascending-spiral gain validation)

- **Generated (UTC):** 2026-07-04T04:08:19Z
- **Run:** `v3_exq_711_ascending_spiral_gain_validation_20260704T021720Z_v3`
- **Queue id:** V3-EXQ-711 · **Purpose:** evidence · **Outcome:** FAIL · **non_degenerate:** True
- **Claims:** MECH-439, ARC-108, ARC-110 (all `candidate` / `implementation_phase: v3` / `pending_retest_after_substrate: true`)
- **Scope:** single (with a load-bearing 709→711 within-lineage pattern)
- **Status:** confirmed (user-approved, interactive gate 2026-07-04)
- **Substrate under test:** ree-v3 main `6b660a6` — no-op-default `config.e3.use_ascending_spiral_gain`; the asymmetric ascending-spiral gain build both the V3-EXQ-709 and V3-EXQ-710 confirmed autopsies routed to.

## Self-route (what is being adjudicated)

The flat manifest self-routed a **DECISIVE** read:

| Claim | Self-routed direction | Reading |
|---|---|---|
| MECH-439 | supports | conversion ceiling is INTRINSIC |
| ARC-108 | weakens | learned gating at the arbitration does not convert |
| ARC-110 | weakens | segregated-loop route does not convert |

Decision rule (pre-registered): `limbic wins ≥3/4` AND `C1 lift` ⇒ MECH-439 weakens / ARC-108+ARC-110 supports (ceiling liftable); `limbic wins but no C1 lift` ⇒ **decisive** MECH-439 supports / ARC-108+ARC-110 weakens (ceiling intrinsic); `limbic can't win ≥3/4` ⇒ substrate_not_ready_requeue (non_contributory). The run landed in the middle branch.

## Facts reconstruction

**Divergent seed set** = {42, 44, 46} (GAP-A divergent on **both** arms; `n_divergent=3`, `MIN_DIVERGENT_SEEDS=3`). Preconditions all recorded MET, including the load-bearing `limbic_loop_can_win` (measured 3.0 ≥ 3.0).

### Concern 2 — C1 seed-count (RESOLVED, not a bug)

C1 (`c1_seeds` loop, script L1327-1332) is scored per-divergent-seed: `learned_ent[s] > static_ent[s] + 0.05`.

| seed | OFF entropy | ON entropy | Δ (ON−OFF) | C1 pass? |
|---|---|---|---|---|
| 42 | 0.880 | 1.033 | +0.153 | ✓ |
| 44 | 1.092 | 1.042 | −0.049 | ✗ |
| 46 | 1.204 | 0.994 | −0.210 | ✗ |

`C1_n_seeds=1` is the **pass-count** (seed 42), scored across all 3 divergent seeds (`C1_n_divergent=3`); needs `max(2, ceil(0.5·3))=2` → 1 < 2 → C1 fails. The `mean_committed_class_entropy_ascending_off 0.877 / _on 0.855` figures are the **all-6-seed** means (a display statistic), not the decision statistic. **No instrumentation / seed-filtering bug.**

### Concern 3 — gain saturation (CONFIRMED, breaks the decisive read)

The `limbic_loop_can_win` gate is a bare `w_eff[limbic] ≥ w_eff[motor]` (script L1283-1292, diag L863-878) with **no upper bound / no parity band**. It was satisfied not by a competitive parity win but by a runaway blow-up of the plastic ascending path (20× forward × 5× maturation gain compounding through the three-factor eligibility update):

| divergent seed | w_motor_eff peak | w_limbic_eff peak | limbic:motor ratio | M_cross range peak | entropy vs OFF |
|---|---|---|---|---|---|
| 42 | 23.3 | **52 988** | ~2274× | 4897.8 | +0.153 (up) |
| 44 | 1.19 | 95.6 | ~80× | 6.96 | −0.049 (down) |
| 46 | 1.05 | 11.4 | ~11× | 0.42 | −0.210 (down) |

(un-gained 709 / OFF arm: M_cross range ~0.02–0.12, limbic never reached motor.)

A 10–2274× limbic dominance is **not a fair arbitration** — it is a **new single-loop monopoly (limbic-pinning)** that has replaced the old one (motor / F-pinning). And it does not convert: on 2 of the 3 divergent seeds the saturated win **reduced** committed-class entropy below the un-gained baseline; only seed 42 (the most extreme blow-up) rose. **The conversion step was tested under a degenerate (saturated) arbitration and was NOT validly measured.**

## Claim-layer mapping

| Claim | claim_type | status | epistemic_category | Did the test let the claim express itself? |
|---|---|---|---|---|
| MECH-439 | mechanism_hypothesis | candidate | substrate_ceiling | No — "ceiling intrinsic" requires a fair parity win; F-dominance was *replaced* by limbic-dominance, not dissolved into competition. |
| ARC-108 | architectural_commitment | candidate | substrate_conditional | No — the learned-gating route was tested with an overshot, saturating gain; a bounded/parity gain was never tested. |
| ARC-110 | architectural_commitment | candidate | substrate_conditional | No — the segregated-loop arbitration was degenerate (monopoly), so the loop route could not deliver diversity. |

## Biological-reference triage (the core move)

Closest mechanism: **BG striato-nigro-striatal ascending spiral** (Haber 2000) — limbic → associative → motor ascending DA projection that **graded-biases** downstream loop competition. Its surrounding dependencies in real brains: tonic-DA homeostasis (bounds ascending drive) and striatal lateral inhibition / normalization (prevents single-loop runaway); the coupling is **graded, not winner-take-all**.

REE has the **symbol** (asymmetric upper-triangular gain on the ascending M_cross entries) but not the **functional role**: an unbounded raw scalar gain on a positive-feedback plastic loop → exponential runaway into limbic monopoly. **This divergence is load-bearing** — the mechanism is missing the homeostatic/normalization dependency that keeps the biological spiral in a parity regime. Classic missing-dependency signature, **not** a falsification.

## Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | unclear | conversion evaluated under a degenerate (saturated) arbitration; self-routed decisive weakens not warranted |
| Biological reference | partial | Haber 2000 graded, bounded spiral; REE has symbol not functional role (raw scalar → runaway) |
| Prerequisites | missing | gain-control / column-normalization / target-parity law bounding w_eff |
| Implementation | partial | `_ascending_gain_matrix` + M_cross maturation update unbounded; win-gate has no parity band / w_eff ceiling |
| Environment | adequate | GAP-A reef-bipartite carries divergence (3 divergent seeds) |
| Measurement | misleading | win-gate cannot distinguish a 1.01× fair win from a 2274× blow-up |
| Integration | unstable | gained cross-loop interaction numerically unstable (M_cross range 0.42 → 4897.8 across seeds) |
| Scale | adequate | 6 seeds, phased P0/P1/P2; not a capacity issue |

**Recommended `epistemic_category`: `substrate_ceiling`** → **evidence_direction `non_contributory` for all three claims** (substrate_not_ready_requeue — the win-gate simply lacked the saturation guard that would have fired its own non-vacuity branch).

## 709 → 711 pattern (load-bearing)

- **709:** ascending coupling ~0.03 — limbic loop **too weak**, never wins (1/4).
- **711:** ascending coupling at 20×/5× — limbic loop **runs away**, monopolizes (10–2274×).

The raw-scalar ascending gain has **no stable operating regime that yields a parity win** — sub-threshold or runaway. This is a genuine **new** substrate finding (the gain mechanism is missing a controller/normalization), not evidence that MECH-439's ceiling is intrinsic.

## Re-derive brake (MOVE-3) — FIRES

This autopsy makes the substrate_ceiling / non_contributory count **MECH-439 = 10th, ARC-108 = 7th, ARC-110 = 2nd** (threshold 2). Brake fires:

- **Route:** `/implement-substrate` — amend `v4_loop_segregation`.
- **Refuse** a blind same-claim gain-magnitude re-queue (e.g. 711b at 5×/10×) — a bare magnitude sweep is the same-claim / same-substrate re-test the brake exists to stop. A *controller* redesign (bounded/normalized gain) is a substrate BUILD and is the allowed path.
- Upstream substrate: `v4_loop_segregation`.

## Learning extracted

1. The raw-scalar ascending gain has no stable parity regime (709 sub-threshold, 711 runaway); the mechanism is **missing a controller** (gain-normalization / target-parity law) — a new substrate finding, not an intrinsic ceiling.
2. A bare `w_eff[limbic] ≥ w_eff[motor]` win-gate cannot distinguish a fair parity win from a saturated blow-up; a **saturation guard** (parity band + w_eff/M_cross ceiling) is required.
3. Saturated limbic dominance **reduces** committed-action diversity (entropy fell on 2/3 divergent seeds) — it is a mirror-image of F-dominance, not its dissolution.
4. `C1_n_seeds=1` is the correct per-divergent-seed pass-count; concern 2 (instrumentation/seed-filtering bug) is resolved as no-bug.

## Routing (user-confirmed, interactive gate 2026-07-04)

- **Adjudication:** `non_contributory` (gain overshoot) for all three — **the self-routed decisive `weakens` on ARC-108/ARC-110 and `supports` on MECH-439 must NOT be stamped by governance.**
- **Repair route:** `/implement-substrate` — amend `v4_loop_segregation`: bounded/normalized ascending gain (target-parity controller) + a saturation guard on the `limbic_loop_can_win` gate. Blind same-claim gain-magnitude re-queue refused until the controller is built.
- PROMOTES NOTHING; all three stay `candidate` + `pending_retest_after_substrate`.

## Draft `evidence_quality_note` for /governance

See `recommended_evidence_quality_note` in the companion `.json` (identical text to be appended per-claim to MECH-439 / ARC-108 / ARC-110, PROMOTES NOTHING).
