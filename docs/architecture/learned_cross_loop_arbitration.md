---
title: "Learned (dopamine-gated) cross-loop arbitration -- ARC-108 x ARC-110 coupling (V3)"
nav_exclude: true
---

# Learned (dopamine-gated) cross-loop arbitration -- ARC-108 x ARC-110 coupling

**Substrate id:** `learned_cross_loop_arbitration`
**Owning claims:** ARC-108 (learned dopamine-gated gating) x ARC-110 (segregated loops) -- this is the
IMPLEMENTATION of their coupling; it is NOT a new claim (see "Claim handling" below).
**Subject:** `selection.cross_loop_arbitration_plasticity`
**Status:** IMPLEMENTED 2026-07-01. PROMOTES NOTHING. Behind a no-op-default flag, byte-identical OFF.
**Generation:** V3 (attacks the V3 closure blocker MECH-439; `run_id` ends `_v3`,
`architecture_epoch: ree_hybrid_guardrails_v1`).
**Depends on (built, V3-frozen):** ARC-110 (`use_loop_segregation`), ARC-108 (`use_learned_channel_gating`
three-factor machinery), MECH-450 (recurrent settling `W_lat`), MECH-448/449 + ARC-107 (the F-bounded
Go/No-Go eligible set the arbitration runs within).
**Config flag:** `E3Config.use_learned_cross_loop_arbitration` (default `False`) + `learned_cross_loop_eta`
(default 0.01). Requires `use_loop_segregation` on to act.
**Regression guard:** `ree-v3/tests/contracts/test_learned_cross_loop_arbitration.py`.

---

## Problem

V3-EXQ-707b built ARC-110 loop segregation **fully live** -- all six non-degeneracy gates passed, the
limbic loop carried genuine per-candidate range (`named_channel_routing_live` 1.414 >> 0.001, and
`C2_drop_differs_from_a1 = True` on 3/3 seeds). Yet the committed-class entropy conversion DV did not lift:
**A1_LOOPS 0.838 ~ A0_SINGLE_ARENA 0.914** (below), C1 0/3 seeds. Per ARC-110's own pre-registered grid
this narrowed ARC-110 (not demoted): **loop segregation is necessary-but-not-sufficient**.

The autopsy (`evidence/planning/failure_autopsy_V3-EXQ-707b_2026-06-29.md`, section 6) traced the missing
dependency precisely: the cross-loop combine in `_segregated_loop_arbitrate` is **static arithmetic** --
the per-loop normalised preferences are summed with **fixed** spiral gains
(`loop_segregation_spiral_gain_assoc/limbic`, `loop_segregation_motor_authority`, all 1.0). Even after the
per-loop zscore strips F's raw magnitude, the *combine weights themselves cannot LEARN*, so the arbitration
still inherits F's static dominance: the limbic "is this worth committing to" value carries real range but
**never wins**, because nothing lets its influence grow through experience.

Biological BG action selection does not have a fixed cross-loop combine. The segregated
cortico-basal-ganglia-thalamic loops (Alexander / DeLong / Strick 1986) coexist with **dopamine-gated
striatal plasticity**: D1/D2 pathways LEARN the arbitration, and Haber's ascending striato-nigro-striatal
dopamine spiral (limbic -> associative -> motor) is the *plastic* medium through which the limbic value
loop comes to modulate the motor loop. The BG-assembly map (`basal_ganglia_assembly_map_2026-06-22.md`)
names this exactly: "learning is at valuation, not arbitration -- and that IS the conversion-ceiling root."
The next attack it registers is "dopamine-into-gating + recurrent-settling-step (coupled)."

The 2026-06-29 MECH-439 claim-synthesis (`claim_synthesis_MECH-439_2026-06-29.md`, section 7) named the same
gap as the **intersection of ARC-108 and ARC-110** ("DA-gated three-factor plasticity operating AT the
cross-loop arbitration") and recommended routing it to `/implement-substrate` rather than minting a child.
This document is that build.

### Failure record (defines acceptance criteria)

| run | conversion DV | reading |
|---|---|---|
| V3-EXQ-707b | committed-class entropy A1_LOOPS **0.838** ~ A0 0.914 (below); C1 0/3 | segregation alone, with STATIC arbitration, does not convert |

**Acceptance target** (for the SEPARATE validation falsifier, queued after this build lands): A1_LOOPS
**coupled with learned/DA-gated cross-loop arbitration** strict-above A1_LOOPS + static-arithmetic
arbitration on a strict majority of divergent seeds, on the same GAP-A reef-bipartite foraging substrate,
with the learned cross-loop weights demonstrably moving off init and the limbic effective column weight able
to exceed the motor loop's.

---

## Solution

Replace the static cross-loop combine with a **learned [3x3] cross-loop matrix** `W_cross = I + M_cross`
(loop order motor / associative / limbic), learned by the SAME ARC-108 signed-RPE three-factor rule that
already trains `w_chan` and `W_lat`, sharing one dopaminergic teaching signal.

### Forward

Let `Z = [motor_z, assoc_z, limbic_z]` be the three per-loop preferences AFTER the existing per-loop
settling (MECH-450) and per-loop zscore normalisation (each a length-`n_elig` COST vector, lower == better).
Then:

```
W_cross = I + M_cross                       # [3,3], M_cross a register_buffer init 0
eff     = W_cross @ Z                        # [3, n_elig]  (Haber ascending spiral, now PLASTIC)
final   = m_a*eff_motor + g_a*eff_assoc + g_l*eff_limbic
commit  = argmin(final)                      # (softmax sample when uncommitted)
```

At init `M_cross == 0` so `W_cross == I`, `eff == Z`, and `final` is **bit-identical** to the static
combine. With the flag off, the static combine runs untouched. `M_cross[i, j]` is the learned directed
influence of loop `j` on loop `i`'s effective preference: the diagonal is per-loop self-gain and the
off-diagonal is the ascending spiral -- in particular **`M_cross[motor, limbic]` is the learnable path by
which the limbic value loop comes to drive the motor commit.**

### Learning (three-factor, shared dopamine)

`M_cross` is updated by the standard three-factor Hebbian rule already used for `W_lat`, via an
**outer-product co-activation trace** at the committed candidate:

```
pre_j  = -Z_j[committed]          # SIGNED: > 0 when loop j PREFERRED the committed candidate (low cost)
post_i = -eff_i[committed]        # SIGNED effective preference of loop i for the committed candidate
coact[i, j] = post_i * pre_j                          # outer product, decayed into _clg_coact_trace
Delta M_cross = eta_c * delta_t * asym(delta_t) * coact_trace
```

`delta_t = R_t - V-hat_t` is the **SAME** signed dopaminergic RPE that trains `w_chan` and `W_lat`
(`R_t = benefit_eval - harm_eval` at the realised state from the already-trained valuation heads; `V-hat_t`
a slow EMA baseline) -- Haber's single ascending dopamine broadcast, one signal for all learned objects.
`asym` is the shared D1-LTP / D2-LTD asymmetry (potentiation on `delta_t >= 0` faster than depression).

The **signed** eligibility (`pre_j = -Z_j[committed]`, user-chosen 2026-07-01) gives directionally-correct
cross-loop credit: a loop that was FOR the committed candidate and got a good outcome is up-weighted; a loop
that was AGAINST it and it worked anyway is down-weighted -- exactly the credit structure needed for the
limbic loop to LEARN TO WIN, and sharper than the unsigned `|.|` eligibility used for `w_chan` (whose bias
sign convention differs). Waking-only: a replay/DMN simulation tick records no trace, forms no `delta_t`,
and writes no `M_cross` (MECH-094). Learned state persists across episodes; only the within-episode trace +
pending flag are cleared at episode boundaries (`clear_learned_channel_eligibility`).

### Coupling with MECH-450 (settling)

The per-loop settling step (`_lateral_settle`, MECH-450 `W_lat`) runs BEFORE the normalise/arbitrate,
shaping each loop's *within-loop* competition. The learned cross-loop weights arbitrate ACROSS the settled
loops. Both learned objects ride the same shared `delta_t` in one `post_action_update`. This is the coupled
"dopamine-into-gating + recurrent-settling-step" the BG-assembly map names -- settling shapes the within-loop
attractor, cross-loop plasticity shapes the across-loop authority, one dopamine system.

### Safety (unchanged)

The arbitration runs **strictly within** the F + MECH-448/449 Go/No-Go eligible set (a No-Go-suppressed
candidate is never a candidate here), so a learned cross-loop weight can reorder within-eligible candidates
but can **never re-admit a suppressed one** -- the orthogonal-to-F safety guarantee is inherited from the
envelope regardless of the weights, including if the motor weight shrinks toward zero. No autograd
(`register_buffer` + `no_grad` local update); the plasticity is never an optimizer target.

---

## Biological Grounding (ARC-106)

**Grounding ladder.** L1-L2: functional translation of dopamine-gated striatal plasticity operating on the
Alexander/DeLong/Strick segregated loops, integrated by Haber's ascending striato-nigro-striatal dopamine
spiral. The claim is FUNCTIONAL (learned cross-loop credit assignment under a single dopamine broadcast),
not anatomical mimicry.

**Load-bearing-vs-decorative.** The mechanism is load-bearing by construction: its whole purpose is to
change the pre-registered conversion metric (committed-class entropy) that the static combine could not
move. The SEPARATE validation falsifier is the ablation test (learned cross-loop arbitration ON vs the
707b static-arbitration control); if learned arbitration also fails to lift, the coupling hypothesis is
refuted (route back per the autopsy).

**Divergence ledger (logged, not silent):**

| # | Divergence from biology | Why acceptable (function over homology) |
|---|---|---|
| CLA-1 | The cross-loop influence is a single scalar matrix `M_cross[i,j]`, not the anatomically-distributed striato-nigro-striatal projection. | ARC-106 G1 function-not-homology: the FUNCTION (learned directed cross-loop credit) is preserved; the anatomical substrate is abstracted, as everywhere else in REE. |
| CLA-2 | The credit is a decayed eligibility/co-activation trace, not sub-second dopamine transients. | Standard RL eligibility-trace abstraction (as `w_chan` / `W_lat` already do); the trace carries the locality, the shared `delta_t` the teaching. |
| CLA-3 | The forward map is **linear**, so the committed selection depends only on the effective column weights `w_eff[j] = sum_i gain_i * W_cross[i,j]`; the [3x3] is rank-collapsible in the forward pass. | Honest simplification. The [3x3] matrix's value is the DIRECTED credit-assignment STRUCTURE it learns (who influences whom, via the outer-product post_i x pre_j), not forward expressivity. A future nonlinearity (per-row renorm between mix and combine) would make it non-collapsing but breaks bit-identical-at-init; deferred. |
| CLA-4 | `M_cross` is signed (a loop may invert another's preference). | Mirrors the existing signed `W_lat` (MECH-450) precedent; expressive and safe (arbitration stays within the eligible set). |

**Psychiatric-failure-mode mapping (ARC-106 EARNS -- required column).** A mis-learned cross-loop matrix is
the computational signature of the conversion ceiling AS a disorder axis, localised by loop:

- **Motor-loop dominance that cannot be re-weighted** (`w_eff[limbic]` stuck low, `M_cross[motor, limbic]`
  never grows) = the limbic "is this worth it" value fails to override habitual/F-driven motor selection ->
  **avolition / anhedonic inertia** (the value loop can't win arbitration); the depressive/negative-symptom
  pole.
- **Runaway limbic-to-motor drive** (`M_cross[motor, limbic]` over-potentiated) = the limbic loop
  compulsively overrides motor selection -> **OCD-like / impulsive over-valuation** (limbic-loop dominance
  of the final common path); the compulsive pole.
- **Failure of dopaminergic credit** (`delta_t` uninformative, so `M_cross` never adapts) = the arbitration
  stays frozen regardless of outcome -> the **apathy / cognitive-inflexibility** signature of degraded
  striatal dopamine (the "learning is at valuation, not arbitration" root, now made a controllable axis).

This is the loop-specific CSTC disorder axis the ARC-110 SD doc names, now with a *plastic* arbitration knob
that can be lesioned to model each pole.

---

## ML/AI Engineering Notes (Layer 7 -- counsel, not authority)

- **Three-factor plasticity on a weight matrix.** The outer-product co-activation trace (`post_i * pre_j`)
  gated by a global scalar (`delta_t`) is the standard neo-Hebbian / three-factor learning rule; the REE
  adaptation is that the global scalar is a signed dopaminergic RPE (not a reward) and the update is a LOCAL
  buffer write, never autograd -- identical in shape to the already-shipped `W_lat` update, so it inherits
  that code's numerical behaviour.
- **Router collapse / dead-expert hazard** (mixture-of-experts parallel). A learned cross-loop arbiter can
  collapse all authority onto one loop (here: the motor/F loop -- exactly the pathology this exists to
  break). Mitigations already in place: the arbitration runs on the per-loop-normalised (magnitude-stripped)
  preferences, the within-loop competition is preserved independent of the cross-loop weights, and the
  validation falsifier's non-vacuity gate requires the learned weights to move off init AND the limbic
  effective weight to be able to exceed motor. Do NOT import MoE architecture (top-k gating nets) -- these
  are 3 functionally-specified loops, not anonymous experts.
- **Learning-rate / stability.** `eta_c` default 0.01 matches the `w_chan` / `W_lat` rate; the signed RPE
  and the D1/D2 asymmetry are shared, so the three learned objects stay on one consistent dopamine scale.

---

## MECH-094

Selection + waking-learning only. The learned update runs on the waking committed-selection path; a
simulation/replay tick arms no trace and writes no `M_cross`. Nothing is written to memory by this
mechanism, so the `hypothesis_tag` requirement does not engage at this layer (inherited from the ARC-108
waking gate).

---

## Claim handling (no new child)

Per the 2026-06-29 MECH-439 claim-synthesis discrimination gate (section 7), the borderline candidate child
**MECH-453 (cross-loop arbitration plasticity)** was recommended **DROP**: it is the intersection of two
already-registered architectural commitments (ARC-108 learned gating o ARC-110 segregated loops), and
**ARC-108 already `depends_on` ARC-110**. This build therefore mints **no new claim**; instead it annotates
the existing ARC-108 and ARC-110 `implementation_note`s and records the coupling via their `depends_on` /
`related_claims`. The validation falsifier (queued separately, new EXQ, different `claim_ids`) tests
**ARC-108-coupled-to-ARC-110**; it does not need a fresh claim to be runnable.

---

## What This Substrate Enables

- **MECH-439** -- the named next attack on the F-dominance conversion ceiling after 707b: does learned
  cross-loop arbitration convert committed-action diversity where static arbitration plateaued?
- **ARC-108 / ARC-110** -- the first substrate on which their coupling (learned gating AT the cross-loop
  arbitration) is testable; resolves whether the 707b narrowing's "requires coupling with learned/DA-gated
  cross-loop arbitration" release condition holds.
- The loop-specific CSTC disorder axis with a *plastic* arbitration knob (the psychiatric mapping above).

---

## Addendum: ascending-spiral gain (V3-EXQ-709/710 loop-effective-weight repair, 2026-07-03)

**Status:** IMPLEMENTED 2026-07-03. PROMOTES NOTHING. No-op-default flag, byte-identical OFF.
**Config:** `E3Config.use_ascending_spiral_gain` (default `False`) + `loop_segregation_ascending_spiral_gain`
(default `1.0`, forward) + `loop_segregation_ascending_plasticity_gain` (default `1.0`, maturation). Requires
`use_learned_cross_loop_arbitration` (hence `use_loop_segregation`) on to act.
**Regression guard:** `ree-v3/tests/contracts/test_ascending_spiral_gain.py` (8 contracts).

### Problem (the deeper sub-gate 709/710 exposed)

The learned cross-loop matrix above ENGAGES -- V3-EXQ-709 confirmed 6/7 readiness gates met (`M_cross`
moved off init, range 0.116; limbic routing live 1.414; 4 divergent seeds; learning engaged). But the ONE
unmet gate is the load-bearing one: `limbic_loop_can_win` -- on the GAP-A-divergent seeds the limbic loop
reached the motor loop's **effective column weight** `w_eff[j] = sum_i gain_i * W_cross[i,j]` on only **1/4**
(threshold 2). The plastic ascending path `M_cross[motor,limbic]` peaked at only ~0.03 -- the arbitration
LEARNS and the limbic channel CARRIES signal, but the ascending coupling is functionally **too weak** to lift
a non-motor loop above the F-pinned motor loop. Three structurally-different conversion mechanisms (709
learned arbitration, 710 disinhibitory settling, the 700-lineage same-layer null) now fail on this one
substrate with the same signature -> the ceiling is a **loop-effective-weight property** (autopsies
`failure_autopsy_V3-EXQ-709_2026-07-03` and `_710_`).

### Failure record (defines acceptance criteria)

| run | gate | reading |
|---|---|---|
| V3-EXQ-709 | `limbic_loop_can_win` 1/4 divergent (thr 2); `M_cross[motor,limbic]` peak ~0.03; C1 learned==static | learned arbitration engages but the ascending coupling is too weak for a non-motor loop to win |

**Acceptance target** (for the SEPARATE new-EXQ validation falsifier): under an appropriate ascending-spiral
gain, the limbic loop reaches/exceeds the motor loop's effective column weight on a strict-majority (>=3/4) of
divergent seeds, so C1 (learned strict-above static) becomes validly evaluable -- on the same GAP-A
reef-bipartite substrate, matched seeds, with the same non-vacuity self-route
(`substrate_not_ready_requeue` when `limbic_loop_can_win` is still unmet; never a false weakens).

### Solution

Biology (Haber 2000): the striato-nigro-striatal spiral is anatomically **asymmetric** -- ascending
(limbic -> associative -> motor) influence is the developmentally-strengthened, load-bearing direction. In the
motor(0)/associative(1)/limbic(2) ordering the forward map `eff_i = sum_j W_cross[i,j] z_j` makes the
ascending entries exactly the **strict upper triangle** (row `i` < col `j`): `W_cross[0,2]` (limbic->motor),
`W_cross[0,1]` (assoc->motor), `W_cross[1,2]` (limbic->assoc). Two knobs scale ONLY those entries:

1. **Forward gain** (`_ascending_gain_matrix` in the `W_cross` assembly): `W_cross = I + (G_fwd .* M_cross)`,
   `G_fwd` upper-tri = `spiral_gain`, else 1.0. This is the **anatomical ascending-projection strength** (an
   untuned implicit 1.0 in the 709 substrate). It raises `w_eff[limbic]`/`w_eff[assoc]` (their columns'
   ascending entries) **without touching `w_eff[motor]`** (the motor column is diagonal + descending,
   never scaled) -- so it simultaneously strengthens the ascending coupling AND implicitly **de-pins** the
   motor(F) default. The map stays **linear** (a constant elementwise scaling of `M_cross`), preserving the
   `w_eff`-collapsibility of divergence **CLA-3** and bit-identical-at-init (at init `M_cross==0` ->
   `gain*0==0` -> `W_cross==I` for any gain).
2. **Plasticity maturation gain** (in `post_action_update`): the ascending entries of the three-factor
   `M_cross` update are scaled by `plasticity_gain` -- the ascending **spiral-maturation rate** (ascending
   credit accrues faster than descending). `eta` stays the base rate; this is the directional multiplier on
   ascending plasticity only.

`F` still fully owns the MOTOR loop (`motor_pref` unchanged); the gain only stops F from drowning the limbic
"is this worth committing to" value. **Safety unchanged:** the arbitration stays STRICTLY within the
F+MECH-448/449 eligible set -- the gain reorders within-eligible candidates and can never re-admit a
No-Go-suppressed one. The `w_eff`/`limbic_ge_motor` diagnostics are computed from the **same gained**
`W_cross` (so `limbic_loop_can_win` reads true effective weights), while `clg_limbic_to_motor` stays the RAW
`M_cross[0,2]` (it measures learning, not effective weight). `eta` and P2 length remain independently
sweepable complementary levers (already exposed). Default False / gains 1.0 -> bit-identical OFF.

### ARC-106 divergence-ledger row (this addendum)

| id | divergence from biology | justification |
|---|---|---|
| ASG-1 | The ascending-spiral strength is a single scalar `spiral_gain` on the upper triangle, not an anatomically-distributed, per-projection maturational gradient. | ARC-106 G1 function-not-homology: the FUNCTION (asymmetric ascending-dominant cross-loop influence that lets a matured limbic loop override a motor default) is preserved; the anatomical gradient is abstracted, as everywhere in REE. |
| ASG-2 | Forward gain and maturation gain are decoupled knobs; in biology anatomical projection density and plasticity co-vary. | Honest simplification for a cleanly-isolable falsifier -- forward gain keeps `M_cross` trajectories controllable; the two can be co-swept if the biology demands it. |

## Related Claims

ARC-108 (learned dopamine-gated gating), ARC-110 (segregated loops), MECH-439 (conversion-ceiling umbrella),
MECH-448 / MECH-449 (F-bounded Go/No-Go eligible set), ARC-107 (BG selector constitution), MECH-450
(recurrent settling), MECH-452 (loop-local traces), ARC-109 (D1/D2 split), ARC-106 (biology grounding).
See `sd_v4_loop_segregation.md` (ARC-110 build-of-record) and
`evidence/planning/failure_autopsy_V3-EXQ-707b_2026-06-29.md` (the escalation source).
