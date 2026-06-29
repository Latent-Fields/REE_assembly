# Failure Autopsy -- V3-EXQ-701b (INV-050 MEL measurability, frozen-probe ablation)

- **Generated (UTC):** 2026-06-29T19:22:13Z
- **Scope:** single
- **Status:** confirmed (user-gated 2026-06-29)
- **Run:** `v3_exq_701b_inv050_mel_measurability_frozen_probe_20260624T043724Z_v3`
- **Queue:** V3-EXQ-701b (supersedes V3-EXQ-701a; diagnostic; PROMOTES NOTHING)
- **Claim:** INV-050 (three-drive sleep regulation / Model Error Load) -- `candidate`, invariant/emergent (emergent_from SD-017), `pending_substrate_reconfirmation: true`
- **Outcome:** FAIL / `evidence_direction: non_contributory` / self-route `substrate_not_ready_requeue`

## 1. Facts (no interpretation)

Failed criterion: **R2 readiness precondition** (`world_model_converged_p0_seed_fraction`), load-bearing -- **0.333 vs 0.667 floor** (1/3 seeds converged on the FIXED frozen-probe battery). R1 (`pe_response_range_to_novelty_shock`) = 0.111 vs 0.25 floor on the single scorable seed; C1 (MEL monotonic) flat (mel_none 0.0017575 ~ mel_high 0.0017945); C2 degenerate (single ready seed -> zero per-arm spread). The MEL-measurability question was never reached on a valid >=2/3 base.

Per-seed frozen-probe convergence (`conv_rel_drop`, >=0.10 = converged):
- recon+contrastive (the deployed P0 recipe): seed 42 = -1.0068, seed 123 = +0.2826, seed 456 = -2.4509 -> **converged_frac 0.333**
- recon-only (matched ablation, identical init + battery, only the SD-056 contrastive term differs): seed 42 = +0.9714, seed 123 = +0.9770, seed 456 = +0.9803 -> **converged_frac 1.000**
- `destabiliser_verdict = sd056_contrastive_is_destabiliser`

`sleep_used: false` (commitment-free probe). The frozen-probe metric (701b's fix) removed the 701a episode-rollout exploration-drift confound, so this R2 failure is a **genuine multi-seed world-forward divergence under the contrastive recipe**, not a metric artifact.

## 2. Claim-layer map

INV-050's testable content (MEL measurability / monotonicity of accumulated prediction error to graded waking novelty) was **not tested** -- the run never produced a valid >=2/3 converged base. INV-050 is **UNWEAKENED** (diagnostic, scoring-excluded). The failure is at the readiness/instrument layer, upstream of the claim.

## 3. Biological-reference triage

Not the core move here -- the claim's mechanism was never exercised. The relevant reference is the SD-056 world-forward / contrastive-representation substrate, which is a formal-import (contrastive auxiliary) layered on a reconstruction-primary world-forward. The ablation shows the **contrastive auxiliary destabilises** the reconstruction-primary world-forward learning (recon-only converges 3/3 cleanly; adding the contrastive term collapses it to 1/3). This is a substrate-recipe defect, not an intrinsic world-forward ceiling.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (untested) | INV-050 content never reached; R2 gate failed upstream |
| Biological reference | n/a (instrument) | mechanism not exercised |
| Prerequisites / dependency | **missing-then-fixable** | the converged base prerequisite was denied by the SD-056 contrastive aux; recon-only supplies it (3/3) |
| Implementation completeness | partial (recipe defect) | P0 recipe `recon_primary + sd056_aux` destabilises; recon-only is stable |
| Environment adequacy | adequate | CausalGridWorldV2 size 12; not the issue |
| Measurement adequacy | **now adequate** | frozen fixed battery (701b fix) removed 701a's exploration-drift confound; the R2 read is now genuine |
| Integration adequacy | n/a | single-module readiness probe |
| Scale / capacity | adequate | recon-only converges to PE ~1.4e-4 |

Dominant diagnosis: **precondition_unmet (642-pattern) -- substrate not validly trained because of a recipe destabiliser**, with the cause cleanly isolated by ablation. NOT `substrate_ceiling`.

## 5. Re-derive brake -- NOT fired (user-confirmed)

Mechanically 701b is the 3rd `non_contributory` INV-050 autopsy (701, 701a, 701b), which would trip the default threshold-2 brake. The brake **does not fire**: (a) every iteration has been a distinct *instrument repair* making genuine progress (P0 divergence -> episode-rollout confound -> frozen-probe fix -> contrastive destabiliser isolated), not re-derivation of one ceiling; (b) a **demonstrably-converging base exists** (recon-only 3/3) -- we are not at a ceiling; (c) the ablation hands a clean mechanical fix. 701a's autopsy set this precedent (mechanical count = 2 = threshold, explicitly not fired because metric-confounded; user-confirmed). The brake LOCKS only if 701c's recon-only base *also* fails to yield a clean MEL read.

## 6. Learning extracted

- The SD-056 contrastive auxiliary destabilises the reconstruction-primary P0 world-forward (recon-only converges 3/3, frac 1.0; recon+contrastive 1/3) -- a real, ablation-confirmed substrate finding worth noting on SD-056.
- The frozen fixed-probe battery is the correct convergence instrument (removes 701a's exploration-drift confound); keep it for 701c.
- INV-050's MEL-measurability question remains genuinely open and untested.

## 7. Routing (user-confirmed)

**`/queue-experiment` -> V3-EXQ-701c**: recon-only P0 warmup (drop the SD-056 contrastive aux from the warmup recipe) -> the same frozen MEL probe (R2 gate -> R1 -> C1 monotonicity). ARM_ABLATION (recon-only) is the valid converged base for the R1/C1 novelty-flatness test. Additionally register the contrastive-destabiliser finding as positive evidence against the SD-056 contrastive auxiliary recipe (note on SD-056). INV-050 stays `non_contributory` / UNWEAKENED.

## Draft evidence_quality_note (for governance; do not write here)

> V3-EXQ-701b (2026-06-24, frozen-probe ablation, supersedes 701a) -> non_contributory. R2 readiness FAILED on the FIXED frozen battery (conv_frac 0.333, 1/3 seeds) -- a GENUINE multi-seed world-forward divergence (exploration-drift confound removed), NOT a metric artifact. Matched ablation: recon-only P0 converges 3/3 (frac 1.0, drops ~0.97-0.98) vs recon+contrastive 1/3 -> destabiliser_verdict = sd056_contrastive_is_destabiliser. Route (autopsy-confirmed 2026-06-29): 701c = recon-only P0 warmup -> frozen MEL probe (the valid converged base). Re-derive brake NOT fired (instrument repair + demonstrably-converging recon-only base, not a ceiling). INV-050 UNWEAKENED (diagnostic, scoring-excluded). Secondary learning: SD-056 contrastive auxiliary is a confirmed P0 world-forward destabiliser.
