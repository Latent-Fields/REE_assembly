# Critical-Period Crystallization: Phase-3 Plasticity Injection + EWC Residue Write-Protect

**Implements:** INV-074 (necessity), MECH-333 (open phase, option E subset),
MECH-334 (closure / crystallization), ARC-075 (infant-curriculum plasticity
magnitude asymmetry)
**Subject:** learning.developmental_critical_period_closure_crystallization
**Status:** IMPLEMENTED 2026-05-17
**Registered:** 2026-05-17
**Depends on:** ARC-062 Phase 1 (gated_policy), ARC-046 (infant curriculum
GAP-9 scheduler), ARC-065 (diversity stack), ResidueField (SD-005)
**Blocks / enables:** V3-EXQ-543h (ARC-062 GAP-B falsifier with crystallization
ON); the resolution path for Q-052 (magnitude vs structural)

---

## Problem

V3-EXQ-543g (2026-05-17, FAIL / weakens ARC-062) ran the canonical 543d 2x2
factorial (use_gated_policy x use_dacc) on the SP-CEM substrate with the
GAP-B option-2 first-action one-hot head input. Result:

| Arm | use_gated | use_dacc | mean reef fraction |
|-----|-----------|----------|--------------------|
| ARM_0 | OFF | OFF | 0.278 |
| ARM_1 | OFF | ON  | 0.174 |
| ARM_2 | ON  | OFF | **0.444 (best)** |
| ARM_3 | ON  | ON  | 0.243 (regresses BELOW gated-only) |

D2 (ARM_3 - ARM_2 >= +0.10) FAILED with delta = -0.200. The dACC training
signal, added on top of the gated policy, **destroys** the discrimination
ARM_2 established. This is the experimental signature of shared-parameter
gradient interference: the gated policy is never crystallized before dACC is
introduced, so dACC's gradient overwrites the discrimination (the
heterosynaptic-depression analog, O'Dell 2025, cited in INV-074's literature
anchors -- the dominant pathway actively depresses competitors).

This is the substrate signature of the missing critical-period closure
mechanism (MECH-334). The infant substrate (ARC-046 / GAP-9 scheduler) has
four phases but implements ZERO weight crystallization -- all weights stay
fully plastic through every phase; phase transitions only change scalar
params and env kwargs (ARC-075: temporal scheduling alone is architecturally
incomplete; Bengio 2009).

## Solution

Two coupled mechanisms, both behind one master toggle
(`REEConfig.crystallize_at_phase3`, default False, bit-identical OFF),
fired once at the infant-curriculum Phase 2->3 transition.

### 1. GatedPolicy plasticity injection (Nikishin et al. 2023 NeurIPS)

At Phase-3 entry, `GatedPolicy.crystallize()`:

- Sets `requires_grad=False` on `head_0`, `head_1`, `discriminator` params
  -- the discrimination ARM_2 established during the open window is
  crystallized; routed diversity gradient can no longer overwrite it
  (MECH-334 closure analog for the policy heads).
- Adds a fresh plastic `expansion` MLP with the SAME input contract as the
  scoring heads, **last-Linear zero-initialised** so the module's output is
  bit-identical at the instant of crystallization (the expansion contributes
  exactly 0 until routed gradient grows it -- no transition discontinuity).
- `forward()` becomes `frozen_gated(x) + expansion(x.detach())`. The
  `.detach()` is essential: it blocks the expansion's gradient from flowing
  back into the (frozen) heads' upstream feature producers, in addition to
  the heads themselves being `requires_grad=False`.

`expansion_parameters()` exposes the plastic params for the experiment's
post-Phase-3 optimizer (mirrors the SD-033a GAP-D
`lateral_pfc.bias_head_parameters()` pattern). `crystallize()` is idempotent;
`reset()` does NOT un-crystallize (developmental closure persists across
episodes).

Why option (E) and not (A)-(D) of MECH-333: the EXQ-571 audit showed F
accounts for 88-89% of E3 scoring variance with all diversity bias_fractions
at 0.000. A learning-rate schedule (A) or magnitude rescale (B) does not stop
the *structural* overwrite once F dominates; gradient blocking (C) is the
strongest isolation but plasticity injection (E) achieves the same isolation
(a clean plastic gradient channel that cannot reach the consolidated weights)
while preserving the consolidated knowledge -- and it is the most directly
validated technique for this exact RL failure mode (Nikishin 2023).

### 2. ResidueField EWC write-protect (Kirkpatrick et al. 2017)

`ResidueField.snapshot_ewc_anchor()` captures a detached copy of the
rbf_field centers/weights at Phase 3 plus an established-basin diagonal
Fisher proxy:

```
Fisher_i = |weights_anchor_i| * active_mask_i
```

`ResidueField.ewc_penalty()` returns
`ewc_lambda * sum_i Fisher_i * [ (w_i - w_anchor_i)^2 + sum_d (c_i,d - c_anchor_i,d)^2 ]`,
differentiable w.r.t. the current params (anchor + Fisher detached). The
experiment adds this to its loss.

This is **not a hard freeze**: residue geometry keeps adapting, but
established basins resist overwriting in proportion to their accumulated
strength -- the biologically faithful MECH-334 reading ("high resistance to
overwriting established basins"), not a uniform L2 pull. Returns a `0.0`
scalar when disabled / lambda 0 / no anchor, so the experiment adds it
unconditionally.

### Phase-3 hook plumbing

`InfantCurriculumScheduler.__init__(on_phase3_entry=...)` takes a zero-arg
callback fired EXACTLY ONCE the first tick the scheduler is in Phase 3
(guarded by `_phase3_hook_fired`). Kept as a caller-supplied callback so the
experiment-harness helper stays ree_core-free; the experiment passes a
closure calling `agent.gated_policy.crystallize()` +
`agent.residue_field.snapshot_ewc_anchor()`.

---

## Pre-check: F-error dependence of routed diversity signals (ICM self-defeat)

Q-052's literature anchor flags the Pathak et al. 2017 ICM self-defeat mode:
an F-prediction-error-based diversity signal collapses to zero as F
consolidates. If a routed signal is F-error-dependent, plasticity injection
cannot rescue it -- the signal is already gone before Phase 3 fires. Audit of
the MECH-313 / MECH-314 / MECH-320 implementations
(`ree-v3/ree_core/policy/{noise_floor,structured_curiosity,tonic_vigor}.py`,
agent feed at `agent.py`):

| Signal | Source | F-error-dependent? | Behaviour by Phase 3 | Route to expansion? |
|--------|--------|--------------------|----------------------|---------------------|
| **MECH-313** noise_floor | `max(baseline_T + alpha, min_T)` constant temperature lift | **No** | constant (no decay) | **Yes -- robust** |
| **MECH-314a** novelty | min RBF distance to active residue centers / mean-norm | **No** (Wittmann 2008: striatal novelty independent of RPE, by design) | tracks residue coverage, not F accuracy | **Yes -- robust** |
| **MECH-314b** uncertainty | reads `e3._running_variance` (per-tick PE-MSE accumulator) | **Yes** | decays toward low/stable as F consolidates | **No -- self-defeated** |
| **MECH-314c** learning-progress | EMA of `|PE_t - PE_{t-K}|`, fed `e3._running_variance` | **Yes -- canonical Pathak 2017** | collapses to ~0 as PE plateaus | **No -- self-defeated** |
| **MECH-320** tonic_vigor | primary = slow EWMA over realised E3-score-receipt (avg reward rate); secondary `gate_pe` reads `_running_variance` | **No** for primary (Niv 2007 avg-reward-rate is reward-rate, not PE); only the non-load-bearing `gate_pe` modulator is F-adjacent | primary robust (a competent agent keeps receiving good scores) | **Yes -- primary robust** |
| **dACC / MECH-260** anti-recency | per-candidate bias from recent action-class frequency | **No** (state-dependent recency, not F-PE) | robust | **Yes -- robust; this is the 543g corrupting signal under test** |

**Implication for the experiment.** Routing MECH-314b/314c to the
post-crystallization expansion layer is pointless: both signals will have
self-defeated to approximately zero before Phase-3 crystallization fires (F
consolidates through Phases 0-2; 314c is the textbook ICM self-defeat case;
314b decays with the same `_running_variance`). They cannot establish
competitive weight on a fresh expansion layer because their gradient
magnitude is already gone. The crystallization hypothesis is therefore tested
with the **F-robust** signals -- dACC/MECH-260 (the exact signal 543g showed
corrupts the gated weights, and it is *not* F-error-dependent, so the
hypothesis is cleanly testable), plus MECH-313 / MECH-314a / MECH-320-primary.
**V3-EXQ-543h holds MECH-314 in novelty-only configuration (314a ON,
314b/314c OFF)** in the routed arms so the test is not diluted by a
confounded null channel. This narrows but does not weaken the 543h test: if
ARM_3 still regresses with crystallization ON and only F-robust signals
routed, the problem is isolated to dACC's own architecture, not gradient
interference.

---

## Architecture context

- **MECH-333 (open phase)** is only *partially* implemented here: option (E)
  plasticity injection provides the post-window plastic channel. The
  *pre*-window F-attenuation (ARC-075 requirement 1: reduce F's gradient
  contribution during Phases 0-1) is NOT implemented in this landing -- it is
  the natural next substrate increment if 543h shows crystallization alone is
  insufficient. This landing is the MECH-334 *closure* half plus the plastic
  channel that closure presupposes.
- **Aton et al. 2013 two-stage gate:** waking dynamics set gate 1
  (consolidation instructions), sleep executes gate 2. Crystallization here
  operates on the waking-side policy weights; it does not replace MECH-120
  (SWY) / MECH-165 (replay diversity), which are post-closure maintenance.
- **Relationship to SD-033a GAP-C/D:** the crystallized discriminator's
  gating_weight still routes to LateralPFCAnalog (GAP-C) unchanged; the
  expansion adds a parallel plastic bias, it does not alter the discriminator
  output contract.

## What this enables

- **V3-EXQ-543h** -- the GAP-B falsifier re-run with crystallization as a
  third factor (2x2x2). Pre-registered prediction: with crystallization ON,
  ARM_3 (gated+dACC) >= ARM_2 (gated alone), i.e. D2 PASSes, because dACC
  gradient is sunk into the expansion layer rather than overwriting the
  crystallized heads.
- **Q-052 resolution path:** 543h discriminates magnitude (A) vs structural
  (B). If crystallization rescues D2, the F-dominance failure is structural
  (B) and MECH-333/334 are the correct architecture. If ARM_3 still regresses
  with crystallization ON and F-robust signals routed, the defect is in
  dACC's own architecture (a narrower diagnostic), not gradient interference.

## Related claims

INV-074 (plasticity crystallization necessity), MECH-333 (critical-period
open phase -- option E subset), MECH-334 (critical-period closure /
crystallization -- primary), ARC-075 (infant curriculum plasticity magnitude
asymmetry), Q-052 (magnitude vs structural), ARC-062 GAP-B (the falsifier
lineage this unblocks), ARC-065 (diversity stack: MECH-313/314/320),
MECH-260 (dACC anti-recency: the 543g corrupting signal under test).
