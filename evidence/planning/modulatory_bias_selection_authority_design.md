# modulatory-bias-selection-authority — Substrate Design Document

**Date:** 2026-06-03
**Status:** Implemented
**Claims:** MECH-314, MECH-314a, MECH-314b, MECH-314c, Q-044, MECH-320, MECH-341
**Master flag:** `use_modulatory_selection_authority` (default `False`)

---

## Problem Statement

**Root cause (604a/624a/614d failure cluster):**
Modulatory/secondary score-bias channels (MECH-314 curiosity bonus, MECH-320 vigor no-op penalty, MECH-341 within-class entropy bonus, plus dACC/lateral_pfc/ofc/MECH-295 cortical biases) are additive contributors to E3 candidate scores but are **dominated by primary F+M+phi terms**. Fixed small bias magnitudes (~0.05-0.1) added to primary scores whose raw_score_range is much larger (e.g., 2.0-5.0) never change the argmin.

**Failure signatures:**
- V3-EXQ-604a (MECH-314a per-candidate curiosity): `curiosity_bias_abs_mean = 0.0` across all arms → no curiosity-driven exploration observed
- V3-EXQ-624a (MECH-320 vigor): `v_t = 0.05` fires but `action_density` identical across ON/OFF arms → vigor penalty not affecting selection
- V3-EXQ-614d (MECH-341 within-class temperature): `committed_class_entropy` identical across T=0.5/1.0/2.0 arms → temperature not affecting class diversity

**Biological anchor:**
Basal ganglia Go/NoGo arbitration operates at a different gain stage than cortical value estimation (Frank 2006, Hikosaka 2000). The striatum doesn't just add tiny biases to cortical signals—it applies gain modulation and competitive selection at its own scale.

---

## Solution: Gap-Relative Rescaling

### Core mechanism

1. **Compute primary scores** `F(ζ) + λ·M(ζ) + ρ·Φ_R(ζ)` as usual (unchanged)
2. **Compute modulatory contribution** = sum of all secondary biases (dACC + lateral_pfc + ofc + MECH-295 + MECH-314 curiosity + MECH-320 vigor + MECH-341 entropy bonus)
3. **Rescale modulatory contribution** so its range equals `modulatory_authority_gain * raw_score_range`
4. **Apply rescaled contribution** to primary scores before selection

### Mathematical formulation

```
scores_raw = F(ζ) + λ·M(ζ) + ρ·Φ_R(ζ)
modulatory_total = score_bias + mech341_bonus
modulatory_range = max(modulatory_total) - min(modulatory_total)
target_range = modulatory_authority_gain * (max(scores_raw) - min(scores_raw))
scale_factor = target_range / modulatory_range
scores_final = scores_raw + scale_factor * modulatory_total
```

### Key properties

- **Bit-identical when OFF:** Master flag `use_modulatory_selection_authority=False` (default) → zero code path overhead, all modulatory biases applied as-is
- **Bounded authority:** gain < 1.0 keeps modulatory signals competitive in near-tie regimes but subdominant when primary harm/goal gaps exceed `gain * raw_range` → clearly harmful candidates stay rejected
- **Degenerate-case guard:** When `modulatory_range < modulatory_authority_min_range_floor` (default 1e-6), rescaling does not fire (avoids divide-by-near-zero)

---

## Config Parameters

### E3Config additions (already present in config, implementation added 2026-06-03)

```python
use_modulatory_selection_authority: bool = False
modulatory_authority_gain: float = 0.5
modulatory_authority_min_range_floor: float = 1e-6
```

### Diagnostic telemetry

Added to `E3TrajectorySelector.last_score_diagnostics`:
```python
{
    "modulatory_authority_active": bool,  # True if rescaling fired this tick
    "modulatory_authority_scale_factor": float,  # actual scale_factor applied
}
```

---

## Implementation Location

**File:** `ree-v3/ree_core/predictors/e3_selector.py:764-794`
**Contract tests:** `ree-v3/tests/contracts/test_e3_score_bias_candidate_support.py:172-254`

Rescaling block runs:
1. **After** all modulatory biases are composed (dACC, lateral_pfc, ofc, MECH-295, MECH-314, MECH-320, MECH-341)
2. **Before** `last_scores` cache and softmax

This ensures:
- All modulatory signals are rescaled together (preserves relative proportions)
- Diagnostics capture post-rescale scores
- Commitment / running_variance / urgency semantics unchanged (all operate on final scores)

---

## Validation Plan

### Falsification experiment (to be queued)

**Design:** Copy V3-EXQ-604a (MECH-314a per-candidate curiosity ablation) with authority ON vs OFF:

- **Arm A:** `use_modulatory_selection_authority=False` (baseline, expect FAIL replication)
- **Arm B:** `use_modulatory_selection_authority=True, modulatory_authority_gain=0.5`
- **Arm C:** `use_modulatory_selection_authority=True, modulatory_authority_gain=0.8`

**Acceptance criteria:**
1. Arm A: `curiosity_bias_abs_mean ≈ 0.0` → FAIL (bit-identical to 604a)
2. Arm B/C: `curiosity_bias_abs_mean > 0.05` **AND** `modulatory_authority_scale_factor > 1.0` → mechanism active
3. Arm B/C: observable action-distribution difference vs Arm A (e.g., visited_cells increase, mean_episode_length change)
4. Arm C (higher gain): larger behavioral deviation from Arm A than Arm B

**Success verdict:** If Arm B/C show both mechanism-active telemetry AND behavioral change, the substrate has given modulatory signals genuine authority.

---

## Related Work

**Supersedes (never landed):**
- normalize_score_bias_to_e3_range (V3-EXQ-563c, 2026-05-22): blunt gain=1.0 rescaling of `score_bias` alone (does not compose MECH-341, does not bound authority). Config flag present but mechanism was always a stand-in for this substrate.

**Complements:**
- MECH-314 structured curiosity (per-candidate + broadcast + learning-progress flavours)
- MECH-320 tonic vigor (capacity-keyed no-op penalty)
- MECH-341 behavioral diversity (entropy bonus + class-stratified selection)
- SD-032b dACC adaptive control (harm-PE-driven payoff/effort bias)
- SD-033a lateral-PFC rule persistence (rule-state-derived bias)

All of these mechanisms now have bounded authority at selection via this substrate.

---

## Commit Log

**2026-06-03:**
- Added implementation in `e3_selector.py:764-794` (rescaling block + diagnostics)
- Added three contract tests (bit-identical OFF, rescaling ON, degenerate-case guard)
- Config flags already present in `E3Config` (lines 395-412), implementation was missing

**Next:** Queue validation experiment via `/queue-experiment` to falsify authority mechanism.
