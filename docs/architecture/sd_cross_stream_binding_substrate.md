---
title: "SD: cross_stream_binding_substrate"
parent: "Attention, Binding & Objects"
grandparent: Architecture
nav_order: 9
---

# SD: cross_stream_binding_substrate

**Claim ID:** cross_stream_binding_substrate (named substrate; unregistered candidate `entities/selection.coherence_nonreducibility`)
**Subject:** latent.cross_stream_binding
**Status:** IMPLEMENTED -- two modes. FIXED field (2026-07-08; retest V3-EXQ-720 RAN, SPEC 3/6, gate not cleared). LEARNED (plastic) binder (2026-07-09) -- the residual prerequisite the 720 autopsy named. **Learned binder CONVERGENCE REPAIRED 2026-07-09** (failure_autopsy_V3-EXQ-725: first learned build did not converge -- InfoNCE at chance; fix = L2-normalize projections / cosine InfoNCE; now `binder_converged=True`). Retest V3-EXQ-725a pending, HARD-gated on convergence.
**Registered:** 2026-07-08 (fixed); learned mode added 2026-07-09
**Depends on:** E2FastPredictor.rollout_with_world (SD-005 self/world split), MECH-089 (theta-gamma nesting, conceptual), MECH-270 (ephaptic coupling, conceptual). Learned mode adds a P0 binder training curriculum (satisfied by the retest's P0 phase).
**Blocks:** the learned-binder retest (641a harness on the plastic substrate), `entities/selection.coherence_nonreducibility` candidate registration, INV-002 (coherence includes temporal/phase binding), the two 2026-04-23 intakes (binding + path_integral)

## Problem

The failure autopsy `failure_autopsy_V3-EXQ-641a_2026-06-06` (status: confirmed)
adjudicated V3-EXQ-641a as a **substrate ceiling, not a falsification**. With a
fair, contrast-matched control (shuffle-of-real-C), cross-stream phase-alignment
C(tau) over the `world_states` (z_world) and `states` (z_self) rollout streams
carried **no selection information beyond E**: coherence-specificity was 1/6
seeds (need 4), and the shuffle diverged >= the real coherence in 4/6 seeds.

The root cause is structural, and it is in exactly one place. In
`E2FastPredictor.rollout_with_world` (`ree-v3/ree_core/predictors/e2_fast.py`),
each candidate rollout advances the two streams with **two independent forward
models**:

```
z_self  = predict_next_self(z_self, action)   # E2 self transition (self_dim -> self_dim)
z_world = world_forward(z_world, action)       # E2 world transition (world_dim -> world_dim)
```

The **only** shared input is `action`. z_self's evolution never sees z_world and
vice versa; there is no common latent cause. Any co-variation between the two
streams' step-deltas is therefore whatever the shared action already induces --
which is precisely what E (the substrate's own per-candidate cost
`e3.score_trajectory`) already scores. Cross-stream coherence is a
reparameterisation of "these candidates share an action-mode", so it is
functionally redundant with E. This matches the autopsy signature exactly:
"the read has the symbol of cross-stream coherence but the V3 streams need not
carry the functional binding".

For coherence to carry selection information non-reducible to E, the two streams
must be **genuinely bound** -- share a common latent factor that co-drives both
rollouts and is not itself an image of the action/E.

## Solution

Introduce a **shared binding factor** into the candidate rollout, injected into
both stream transitions, gated behind a no-op-default flag.

### Mechanism (`CrossStreamBinder`, `ree_core/latent/cross_stream_binder.py`)

At each rollout step `t`, from the **joint** pre-transition state:

```
g_t = tanh( W_enc . [z_self_t ; z_world_t] )        # [B, bind_dim]  shared factor (joint cause)
b_t = W_out . g_t                                    # [B, bind_out_dim]  common perturbation
```

`bind_out_dim = min(self_dim, world_dim)`. The **same** perturbation `b_t` is
added to the first `bind_out_dim` components of **both** post-transition states,
scaled by a theta-gated strength:

```
gate_t = 0.5 * (1 + cos(2*pi*t / theta_period))      # MECH-089 theta window (gamma nested in theta)
k_t    = strength * gate_t
z_self [.., :bind_out_dim] += k_t * b_t
z_world[.., :bind_out_dim] += k_t * b_t
```

Because `b_t` is derived from the joint `(z_self_t, z_world_t)` state and is
added **identically** into both streams, the two streams' step-deltas now share
an explicit common component. Cross-stream delta-alignment (the harness's read)
now reflects a real shared latent factor whose trajectory is a genuine
per-candidate signature -- and permuting the per-candidate coherence values
(the SPEC shuffle control) destroys the candidate<->value correspondence.

### Two modes: FIXED field (2026-07-08) and LEARNED binder (2026-07-09)

**FIXED field (`learned=False`, default).** `W_enc`, `W_out` are **fixed**
`nn.Linear` maps, initialised deterministically under the caller's seed. This was
the minimal substrate that installs a genuine common cause without a training
curriculum: a fixed, joint-state-dependent shared perturbation both streams feel
(the ephaptic-field analog, MECH-270). It was the right first build -- but
V3-EXQ-720 (strength 0.5) showed it is **symbol-complete but function-partial**:
coherence-specificity lifted 1/6 (641a, unbound) -> 3/6 (720, fixed field) but
did **not** clear the 4/6 SPEC gate, and `n_rebind` stayed 0. A random projection
creates correlation but nothing **shapes** the coupling so real cross-stream
conjunctions are robustly more selection-informative than a contrast-matched
shuffle. `failure_autopsy_V3-EXQ-720_2026-07-09` (confirmed) named the residual
prerequisite: a **learned (plastic)** binder. The fixed path is preserved
byte-identical.

**LEARNED binder (`learned=True`, 2026-07-09).** The residual prerequisite, built
per user direction 2026-07-09 as an active near-term next-step. The projections
are **plastic**, trained by contrastive co-encoding:

```
h_self  = phi_self(z_self)          # plastic self projection  (self_dim -> bind_dim)
h_world = phi_world(z_world)         # plastic world projection (world_dim -> bind_dim)
g_t     = tanh(h_self * h_world)     # MULTIPLICATIVE conjunction (coincidence/AND detector)
b_t     = to_common(g_t)             # -> common perturbation (couple() unchanged, mode-agnostic)
```

Training objective (P0 binder curriculum): **InfoNCE / event-segmented
co-encoding**. Within-tick observed `(z_self_t, z_world_t)` pairs are POSITIVES;
in-batch shuffled pairs are NEGATIVES. Symmetric cross-entropy over the full
pairwise `binding_score(z_self, z_world) = <phi_self(z_self), phi_world(z_world)>`
matrix. This trains `phi_self`/`phi_world` so genuine conjunctions bind (high
score) and a shuffle collapses (low score) -- exactly the structure the SPEC
shuffle control destroys, and the teeth the rebinding falsifier needs. Why this
is the right build:

1. **The load-bearing biology divergence.** Binding-by-synchrony /
   communication-through-coherence (Fries; Singer/Gray; Buzsaki theta-gamma
   code) is **learned and plastic** (Hebbian: fire-together -> wire-together),
   not a fixed field. The fixed-field mode diverged from biology in exactly the
   place the 720 autopsy flagged; the learned binder closes that divergence.
2. **Phased training APPLIES (unlike the fixed mode).** The retest prepends a
   **P0 binder-training phase** (per-step `agent.update_cross_stream_binder`),
   then FREEZES the binder for the P1 641a measurement (`agent.eval()`, no
   further updates). This is the mandatory P0->P1 discipline; joint-training
   collapse is avoided by training the binder P0-only and on **detached**
   `(z_self, z_world)` so no gradient leaks into E1/E2's encoders.
3. **Substrate-level rebinding probe folded in.** `binding_score` +
   `rebinding_probe(z_self, z_world_candidates, anchor_perturbation)` expose the
   binding intake's own falsifier -- does a competing world-config OVERTAKE the
   currently-bound one under an anchor perturbation -- **at the substrate**, not
   as a separate harness instrument. A fixed field cannot express this
   (`binding_score` is identically 0, undiscriminating), which is precisely why
   `n_rebind` stayed 0 across 641/641a/720. The perturbation is applied to the
   shared **anchor** `z_self` (NOT uniformly to the candidates): `binding_score`
   is bilinear, so a uniform candidate perturbation shifts every score by the
   same candidate-independent constant and can never flip the argmax; an anchor
   perturbation gives a per-candidate shift `<W_self . p, phi_world(c)>` that
   varies with `c`, so a competitor can overtake.

### Convergence repair (2026-07-09; `failure_autopsy_V3-EXQ-725`)

The first learned build (above) **did not converge.** V3-EXQ-725 (the 641a harness
with `learned=True`) ran to completion but the binder never trained: the InfoNCE
loss pinned at chance `log(64)=4.16` (observed 3.75-3.96) across 487-1760 steps,
flat and non-monotone, and coherence-specificity **regressed** 3/6 (720 fixed
field) -> 0/6. The 725 autopsy adjudicated this an **untrained-substrate artifact**
(`epistemic_category = untrained_substrate_artifact`), NOT a coherence verdict and
NOT a substrate ceiling: the 720 learned-binder hypothesis remains **UNTESTED**,
and the rebinding PASS (1387 rebinds) was **vacuous** (argmax over near-random
projections).

**Root cause (convergence probe -- `evidence/planning/binder_convergence_probe_2026-07-09.md`).**
The observed `(z_self, z_world)` latents the P0 curriculum buffers are near-collinear
**buffer-wide** (cosine ~0.99; std ~0.007), not just consecutive. The un-normalized
dot-product InfoNCE logit `<phi_self, phi_world>` is therefore dominated by the
near-constant projection **magnitude** and carries essentially no per-pair contrast
-- the positives are not separable from in-batch shuffles, so the objective has no
gradient and sits at chance. This is a **training-signal / geometry** defect, not a
missing architecture and not an environment-adequacy failure (the environment already
carries the conjunction signal; the binder was discarding it).

**Fix -- cosine InfoNCE (L2-normalized projections).** `learn_step` (and
`binding_score`, so the rebinding probe ranks in the trained geometry) now
`F.normalize` `h_self`/`h_world` before the dot:

```
h_self  = normalize(phi_self(z_self))     # unit vector
h_world = normalize(phi_world(z_world))    # unit vector
logits  = (h_self @ h_world.T) / temperature   # cosine InfoNCE
```

Scoring **direction** rather than magnitude exposes the residual conjunction signal.
The loss then drops to **0.65-0.80 of chance** across seeds (SimCLR-standard cosine
InfoNCE; `temperature=0.2` deepens the margin vs the default 0.5). This is
engineering counsel (normalized-embedding contrastive learning), biologically
compatible: binding-by-synchrony is a coincidence read on **direction/phase**
alignment, and the multiplicative-conjunction coupling injected into rollouts
(`factor()`) is unchanged. Delta-binding, variety-filtered negatives, and larger
`bind_dim` were probed and **not adopted** -- zero gain over plain cosine.

**Convergence stat.** The substrate now reports
`binder_converged = loss_ema < conv_frac * log(effective_batch)` (`loss_ema`: EMA
decay 0.9 of the InfoNCE loss; `conv_frac` = `cross_stream_binding_conv_frac`,
default 0.85). This is the **hard gate the retest MUST check**, replacing the
vacuous `learned_binder_trained` (`n_learn_steps > 1`) readiness check that green-lit
the untrained binder in 725. Smoke (real 725 latent stream): `loss_ema` 3.33 < gate
3.54 -> `binder_converged=True` at default temperature; `binding_score` discriminates
a matched conjunction (0.68) from a shuffle (-0.10); an un-normalized control on the
same buffer stays at chance (0.885). Fixed mode is byte-identical.

### Config (E2Config; all no-op default)

| Param | Type | Default | Purpose |
|-------|------|---------|---------|
| `cross_stream_binding_enabled` | bool | `False` | master switch (OFF = byte-identical) |
| `cross_stream_binding_dim` | int | `16` | shared-factor dim (`bind_dim`) |
| `cross_stream_binding_strength` | float | `0.15` | coupling scale `strength` |
| `cross_stream_binding_theta_period` | int | `4` | theta window period in rollout steps (MECH-089) |
| `cross_stream_binding_learned` | bool | `False` | **False = fixed field (720 path); True = learned binder** |
| `cross_stream_binding_lr` | float | `1e-3` | P0 binder optimizer LR (learned only) |
| `cross_stream_binding_temperature` | float | `0.5` | InfoNCE temperature (learned only) |
| `cross_stream_binding_buffer_size` | int | `512` | co-encoding pair buffer (learned only) |
| `cross_stream_binding_batch` | int | `64` | contrastive batch size (learned only) |
| `cross_stream_binding_conv_frac` | float | `0.85` | convergence gate: `binder_converged = loss_ema < conv_frac*log(batch)` (learned only; report-only) |

Mode layering: `enabled=False` -> no binder (pre-substrate, byte-identical).
`enabled=True, learned=False` -> fixed field (V3-EXQ-720 path, byte-identical).
`enabled=True, learned=True` -> learned (plastic) binder.

The `CrossStreamBinder` submodule is constructed on `E2FastPredictor` **only
when the master switch is enabled** -- so with the flag OFF no parameters are
created, no RNG is consumed at construction, and every existing experiment is
bit-identical.

## Architecture Context

- **Blast radius.** `rollout_with_world` is called by the hippocampal proposer
  (`hippocampal/module.py`) and the SD-003 attribution pipeline. With the flag
  ON, all candidate rollouts get the coupling; with the flag OFF (default),
  nothing changes anywhere.
- **No online-model contamination.** The coupling alters only the *imagined*
  rollout states used for candidate scoring/selection. The online E2 self-model
  update (`record_transition`) uses the *observed* z_self from `agent.sense`,
  not rollout states -- so binding never leaks into training targets.
- **MECH-089 (theta-gamma nesting).** The per-step shared code `b_t` is the
  gamma-rate content; the `theta_period` cosine gate is the theta window it
  nests within -- a structural realisation of the cross-frequency temporal
  packaging MECH-089 asserts. This is conceptual grounding, not a claim that
  MECH-089's ThetaBuffer is reused.
- **MECH-270 (ephaptic coupling).** The identical additive perturbation into
  both streams is the field-mediated shared-cause analog.
- **MECH-094 (hypothesis-tag write gate): does NOT newly apply.** The binder
  adds no memory-write surface and does not change `hypothesis_tag` semantics.
  Candidate rollouts keep their existing tags; the retest is a waking
  select-action diagnostic (`simulation_mode=False`). If a future experiment
  enables binding during replay-with-write, the existing `hypothesis_tag`
  machinery already governs that content unchanged.

## What This SD Enables

- **V3-EXQ-720 (RAN, fixed field)** -- the 641a harness with
  `cross_stream_binding_enabled=True, learned=False, strength=0.5`. Result:
  SPEC 3/6 (lifted from 641a's 1/6) but the 4/6 gate NOT cleared; `n_rebind=0`.
  `failure_autopsy_V3-EXQ-720_2026-07-09` routed the learned binder as the
  residual prerequisite.
- **The learned-binder retest (V3-EXQ-725, RAN 2026-07-09) -- untrained-substrate
  artifact.** The 641a harness with `learned=True` ran 18/18 but the binder never
  converged (InfoNCE at chance); SPEC regressed 3/6 -> 0/6 and the rebinding PASS
  was vacuous. `failure_autopsy_V3-EXQ-725_2026-07-09` (confirmed) adjudicated this
  a substrate diagnostic, NOT a coherence verdict: the 720 learned-binder hypothesis
  is UNTESTED, not refuted. Routed `implement-substrate` -> the convergence repair
  above.
- **The GATED retest (V3-EXQ-725a, to be queued once `binder_converged=True`)** --
  the SAME 725 harness on the REPAIRED binder, with a **HARD
  `learned_binder_converged` precondition** (`loss_ema < 0.85*log(batch)`) REPLACING
  the vacuous `learned_binder_trained` (`n_learn_steps>1`) check, and `temperature=0.2`.
  Pass gate (carried verbatim from 720/641a): **`>=4/6` seeds coherence_specific AND
  `n_rebind>0`**. If the repaired binder still cannot converge under the real SP-CEM
  P0, that is an **environment-adequacy** verdict (route back to `/failure-autopsy`),
  not a coherence verdict. A naive 725b (same non-converging curriculum) is REFUSED.
- On registerable PASS: register the candidate
  `entities/selection.coherence_nonreducibility` (governance) and close both
  2026-04-23 intakes positive; INV-002's temporal/phase-binding clause gains
  substrate support.
- On FAIL: the binding hypothesis is falsified *even with a learned binder* --
  route `/failure-autopsy` to decide whether the intakes close.

## Related Claims

INV-002 (coherence includes temporal/phase binding), MECH-089 (theta-gamma
nesting), MECH-094 (hypothesis-tag write gate), MECH-270 (ephaptic coupling),
MECH-269 (per-stream verisimilitude), ARC-006 (entities and binding), ARC-018
(rollout viability), candidate `entities/selection.coherence_nonreducibility`.
