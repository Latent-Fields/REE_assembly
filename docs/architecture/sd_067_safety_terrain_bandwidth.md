---
title: "SD-067: dedicated safety-terrain RBF bandwidth"
nav_exclude: true
status: candidate/v3_pending
status_asof: 2026-07-15
status_claim: SD-067
---

# SD-067: dedicated safety-terrain RBF bandwidth

**Claim ID:** SD-067
**Subject:** safety_prediction.contextual_safety_terrain_read_resolution
**Registered:** 2026-07-15
**Status:** IMPLEMENTED (2026-07-15)
**Depends on:** MECH-303 (contextual passive safety terrain), SD-008 (z_world differentiation -- the deficit this works around)
**Blocks:** MECH-303 promote-to-active behavioural falsifier (V3-EXQ-764)

## Problem

The MECH-303 behavioural promote-to-active gate hits the **same class of substrate
ceiling** SD-066 fixed for the sister claim MECH-304 -- the z_world common-mode
(SD-008) -- but manifesting through a *different* readout. Diagnosed 2026-07-15
(session unruffled-hopper-e33b08) by driving the full teach->test loop with the
real agent.

MECH-303's contextual safety terrain is an **RBF field** over accumulated z_world
centers: `evaluate_safety(z) = sum_i w_i * exp(-||z - center_i||^2 / (2*bw^2))`.
The release gate in `select_action()` fires when `evaluate_safety(z_world).mean() >=
contextual_safety_release_threshold`. The RBF bandwidth is inherited from the
shared `kernel_bandwidth` (**1.0**).

Under SD-008 under-differentiation, safe (`num_hazards=0`) and unsafe
(`num_hazards=8`) contexts produce z_world vectors that are only **~0.065 apart**
(cosine ~0.988; norm ~0.42). A bandwidth of 1.0 is **~15x too wide** for that
residual scale, so `exp(-0.065^2 / (2*1.0^2)) ~ 1` -- the RBF **saturates**: it
reads ~identically at every context (measured `evaluate_safety`: safe **99.7** vs
unsafe **99.7**, ratio 1.00). The fixed release threshold therefore fires
**indiscriminately** -- behaviourally, terrain-ON arms release at 1.0 in *both* a
safe and an unsafe context, so the context-specificity DV fails for a substrate
reason, not a real null.

Crucially, the discrimination **exists** -- the raw z_world Euclidean distances
carry it (rank AUC ~0.83, matching V3-EXQ-760's representation-level 0.884) -- but
the wide bandwidth cannot resolve it into an **absolute** gap the fixed-threshold
release can use. This is the RBF analog of the cosine saturation SD-066 diagnosed:
760's AUC (a rank metric, and gated on env ground-truth) sidestepped it; the
behavioural absolute-threshold gate cannot.

**Why centering (the SD-066 lever) does not work here.** SD-066 subtracts a
common-mode baseline before a **cosine** read, which changes the angle so the
residual dominates. The terrain read is a **Euclidean** RBF, and Euclidean
distance is **translation-invariant** -- `||(z - b) - (c - b)|| = ||z - c||` -- so
subtracting any baseline is a no-op for it (confirmed: frozen-accumulation centered
gap 0.0125, nil). The correct lever for a Euclidean RBF is the **bandwidth**, not
a translation.

## Solution

An **opt-in, dedicated bandwidth for the safety-terrain RBF**, tighter than the
shared `kernel_bandwidth`, so `evaluate_safety` resolves the small z_world residual
that discriminates safe from unsafe contexts into an absolute gap the release gate
can use.

- New config `residue.safety_terrain_bandwidth` (`Optional[float]`, default
  **None**). Surfaced through `REEConfig.from_dims(safety_terrain_bandwidth=...)`,
  threaded onto `config.residue` only when `use_contextual_safety_terrain=True`.
- `ResidueField` constructs `safety_terrain_rbf_field` with
  `safety_terrain_bandwidth` when set, else falls back to `kernel_bandwidth`.
- **None -> byte-identical** to the pre-SD-067 behaviour (the safety RBF uses
  `kernel_bandwidth` exactly as before). Only the safety terrain is affected; the
  harm / benefit RBFs keep `kernel_bandwidth`.

This is a **read-resolution workaround for the SD-008 z_world common-mode**, NOT a
representation fix (it does not improve z_world differentiation) and NOT a
replacement for a proper metric-learned terrain (the sharper long-term answer). It
is the direct sibling of SD-066: same SD-008 root cause, same "opt-in, non-
parametric, bit-identical-OFF readout workaround" shape, applied to the Euclidean
RBF terrain instead of the cosine store.

### Calibration + eval control (V3-EXQ-764)

The behavioural falsifier V3-EXQ-764 sets `safety_terrain_bandwidth=0.03`. Real-
field inline validation (6 seeds, `contextual_safety_release_threshold=0.5`):

| arm | context | release_rate | DV |
|-----|---------|--------------|----|
| A terrain-ON  | safe   | **0.748** | -- |
| B terrain-OFF | safe   | **0.000** | terrain-necessity gap **0.748** (>= 0.34) PASS |
| C terrain-ON  | unsafe | **0.457** | context-specificity gap **0.292** (< 0.34) FAIL |
| D store-ON    | cue    | **0.833** | MECH-304 dissociation (>= 0.34) PASS |

**SD-067 works as designed** -- it resolves the saturated read into an absolute
gap the release gate can use: terrain-necessity (previously impossible, the read
was saturated at ~99.7 in every context) is now cleanly demonstrable, and store-
dissociation is clean. **The residual shortfall is upstream, in z_world (SD-008),
not in SD-067.** Context-specificity is directional (5/6 seeds show A > C) but its
mean gap (0.292) sits just under the 0.34 margin because the intrinsic safe-vs-
unsafe z_world separability is only rank AUC ~0.83 -- 1/6 seeds (seed 5) *inverts*
(its unsafe context reads as safer than safe), and a variance-aware paired test
(mean 0.292, sd 0.395 -> t ~1.8, p ~0.13) also does not clear it. No read-side
bandwidth can break an AUC-0.83 input ceiling.

**Disposition (2026-07-15, user decision):** SD-067 lands as a validated read-
resolution fix. The MECH-303 **promote-to-active** behavioural falsifier is
**HELD** (not queued): its context-specificity DV is gated on **z_world
differentiation (SD-008)**, a larger upstream substrate effort than SD-067's
read-side fix. The validated falsifier script
(`ree-v3/experiments/v3_exq_764_mech303_contextual_safety_avoidance_release_behavioural_falsifier.py`)
is committed and ready to queue once z_world can separate safe/unsafe contexts.
MECH-303 stays **provisional** (terrain-necessity + store-dissociation are clean
partial behavioural support; full context-driven promotion awaits SD-008).

The experiment additionally **freezes accumulation during the test window**
(`contextual_safety_harm_threshold` set below the z_harm_a floor after teaching):
the affective-harm encoder z_harm_a does **not** distinguish hazard density
(measured 0.547 safe vs 0.542 unsafe, both below the accumulate gate), an SD-011
harm-encoder fidelity limitation, so live test-time accumulation would pollute the
unsafe read. Freezing isolates the MECH-303 **expression** pathway (contextual
release given accumulated safe terrain) -- the promote-to-active claim -- from the
**accumulation** gate's SD-011 dependency (a separate claim). Mirrors how
V3-EXQ-763 reset the MECH-302 comparator at test to isolate the store gate.

## Implementation

- `ree-v3/ree_core/utils/config.py`: `ResidueConfig.safety_terrain_bandwidth`
  (default None); `from_dims(safety_terrain_bandwidth=None)` threads it onto
  `config.residue` when the terrain is enabled.
- `ree-v3/ree_core/residue/field.py`: `safety_terrain_rbf_field` bandwidth =
  `safety_terrain_bandwidth if not None else kernel_bandwidth`.
- Contracts: `ree-v3/tests/contracts/test_sd067_safety_terrain_bandwidth.py`
  (None->kernel bit-identical / config default None / dedicated bandwidth used +
  others untouched / tight bandwidth resolves a small separation the wide one
  cannot / from_dims wiring).

**Validation:** V3-EXQ-764 (MECH-303 promote-to-active behavioural falsifier).
