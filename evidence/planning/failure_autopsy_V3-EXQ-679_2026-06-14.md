# Failure / Diagnostic Autopsy -- V3-EXQ-679 (MECH-423 super-additivity readiness diagnostic)

- **Generated (UTC):** 2026-06-14T18:37:00Z
- **Scope:** single -- diagnostic **gate-clear adjudication**
- **Target run:** `v3_exq_679_mech423_readiness_validation_diagnostic_20260614T102515Z_v3`
- **Queue id:** V3-EXQ-679 | **purpose:** diagnostic | **claim_ids:** [] (tags nothing, weighs nothing)
- **Outcome adjudicated:** PASS / `interpretation.label = readiness_validated`
- **Status:** confirmed (user-accepted gate-clear, 2026-06-14)
- **Routing:** gate cleared -> EXP-0380 (already built+queued; see Concurrency note)

## Why this autopsy at all (a clean PASS)

This is a *verified / unflagged* PASS with `claim_ids: []`. Under the standard rule a
clean PASS clears at the `/governance` walk and needs no autopsy. The user explicitly
routed it to `/diagnostic-autopsy` anyway -- the correct defensive move, because a
**PASS that clears a gate** is the under-adjudicated case (memory:
*diagnostic self-route is a hypothesis, not a verdict* -- "PASS-clears-gate currently
under-adjudicated vs FAIL"). The question this autopsy answers is therefore:

> Did the EXP-0380 readiness gate clear for a **real** reason, or a **degenerate** one?

V3-EXQ-679 is a **readiness gate** for EXP-0380 (the MECH-423 3-arm super-additivity
ablation). It validates that the three substrate readouts EXP-0380's arms depend on are
*live and non-vacuous on a trained substrate* -- it does **not** itself provide evidence
for MECH-423.

## 1. Facts (no interpretation)

Three pre-registered, load-bearing readiness criteria, each measured on the trained
substrate (a known-positive control) across seeds 42 / 123 / 456:

| Criterion | What it asserts | Reading (per-seed) | Threshold | Margin |
|---|---|---|---|---|
| **R1** shared-latent gradient coupling | trained shared latent carries non-zero grad to each module; cosine >= 0; n_modules == 2 | min_grad_norm 1.4e-3 / 2.1e-3 / 8.4e-4; cosine 0.223 / 0.129 / 0.259; n_modules 2 | grad floor 1e-6 | comfortably above floor |
| **R2** iterative-inference convergence | settling loop iterates (>=2) and converges below tol | final_rel_delta 0.0086 / 0.047 / 0.045; n_iters 3 / 2 / 2 | rel_tol 0.05 | **thin on seeds 123/456** |
| **R3** interleaved cross-module consolidation | interleaved share > 0, blocked share == 0, E1 and E2 both updated | interleaved_share 1.0 vs blocked 0.0; updates_e1 8, updates_e2 8; 8 cross-module traces (all seeds) | share>0 & blocked==0 | clean contrast |

- `aggregate.all_preconditions_met = true`; `all_seeds_pass = true`.
- `interpretation.criteria_non_degenerate = {R1: true, R2: true, R3: true}`.
- Buffers populated: world 1000, e2 1000 (all seeds). Warmup 24 ep (p0_end 16).
- Config: grid 6, 4 hazards, 3 resources. Machine ree-cloud-1.
- Pack manifest (`runs/.../manifest.json`, what the indexer scores) agrees with the flat
  manifest: `evidence_direction = supports`, `claim_ids_tested = []`, label
  `readiness_validated`. No flat-vs-pack divergence.

## 2. Adjudication -- the gate-clear is genuine, not vacuous

The script implements the **anti-vacuity precondition pattern** (the V3-EXQ-643 lesson):
each load-bearing criterion has a paired `kind: readiness` precondition that asserts the
*same statistic the criterion routes on*, measured on the known-positive control. All
three preconditions fire independently:

- `r1_shared_latent_grad_coupled` -- min_grad_norm 8.4e-4 > floor 1e-6. **met.**
- `r2_iterative_loop_iterated` -- n_iters >= 2 (the loop actually iterated). **met.**
- `r3_e2_touchable_under_interleaved` -- updates_e2 = 8 >= 1 (the module the cross-module
  share depends on was actually touched -- directly rules out the "starved E2 buffer
  masquerading as the blocked control" mode the script names). **met.**

This is precisely the `non_degenerate` self-check: a starved/untrained substrate would
self-route `substrate_not_ready_requeue`, not masquerade as a falsification or a vacuous
PASS. None of the degenerate failure modes (V3-EXQ-514m valence-channel-never-written,
V3-EXQ-642 untrained-encoder z_block==0) apply here: R2's delta is genuinely below
tolerance (not pinned at 0), R3 shows a real interleaved-vs-blocked contrast with E2
demonstrably touched.

**Conclusion: the EXP-0380 gate clears for a real reason.** The three readouts are live
and discriminative on the trained substrate; EXP-0380's arms will receive a meaningful
reading.

## 3. Biological-reference triage

Light, by design -- this is an instrumentation/readiness diagnostic, not a mechanism test.
- `is_formal_import`: **no.** R1/R2/R3 are substrate-instrumentation preconditions
  (gradient coupling, loop convergence, consolidation touch-counts), not a
  formal-definition import. No biology divergence to register.
- The super-additivity biology (multisensory enhancement / inverse-effectiveness; cortical
  multisensory neurons exceeding the unimodal sum) bears on **EXP-0380 / MECH-423**, not on
  this readiness gate. No `/lit-pull` commission arises from 679.

## 4. Layer diagnosis (adapted for a PASS gate-clear)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | diagnostic tags no claim; it gates EXP-0380. Gate scope is correct (validates the 3 readiness substrates the 3 arms depend on). |
| Biological reference | n/a (for the gate) | super-additivity biology bears on EXP-0380, not on the instrumentation check. |
| Prerequisites | present | trained substrate, warmup 24 ep, buffers 1000/1000. |
| Implementation | complete | 3 readouts on positive control + anti-vacuity preconditions (V3-EXQ-643 lesson applied). |
| Environment | adequate | grid 6 / 4 hazards / 3 resources. |
| Measurement | adequate / non-degenerate | `criteria_non_degenerate` all true; preconditions confirm non-vacuity. |
| Integration | coupled | R3 shows interleaved consolidation actually touches both E1 (8x) and E2 (8x). |
| Scale | adequate | sufficient for a readiness gate. |

`recommended_epistemic_category`: **n/a** (diagnostic, no claim -- nothing to categorise).

## 5. Learning extracted

1. The EXP-0380 readiness substrate (R1 shared-latent gradient coupling, R2
   iterative-inference convergence, R3 interleaved cross-module consolidation) is validated
   **non-vacuously** on a trained substrate across 3 seeds. EXP-0380's 3 arms will read
   meaningfully.
2. The PASS is non-degenerate **by construction** -- the anti-vacuity preconditions all
   fire, ruling out the starved-E2 / untrained-encoder masquerade modes. This is the
   V3-EXQ-643 lesson working as intended.
3. **Watch-item (informational, not a blocker):** R2 `final_rel_delta` on seeds 123/456
   (0.045-0.047) sits just under the 0.05 tolerance with only 2 iterations. The gate
   passes, but EXP-0380's integrated arms should not over-read iterative-inference settling
   *headroom*; if tighter convergence matters there, raise `settle_iters` (>10) or tighten
   `rel_tol`.

## 6. Concurrency note -- EXP-0380 already built + queued

The "then queue EXP-0380" follow-up is **already complete**, by the active parallel session
`queue-exp0380-mech423-superadditivity-20260614T1805Z` (TASK_CLAIMS claim at 2026-06-14T18:05Z):

- `ree-v3/experiments/v3_exq_680_mech423_superadditivity_ablation.py` -- tracked + committed.
- `V3-EXQ-680` -- in `experiment_queue.json`, landed on `origin/main` (commit `121a188`;
  priority 200, machine_affinity any, status pending).

Per the concurrency rule (never silently overwrite/duplicate another session's claimed
work), this autopsy session does **not** re-queue EXP-0380. User-confirmed 2026-06-14:
"Leave it -- don't duplicate."

## Routing decision (user-confirmed)

- **V3-EXQ-679:** gate-clear **confirmed** (genuine, non-vacuous). No claim weighting, no
  substrate gap, no lit-pull, no demotion. Remains a diagnostic; stays pending in
  `review_tracker` by design (no claim to clear at the walk).
- **EXP-0380 / V3-EXQ-680:** already queued by the parallel session -- not touched here.
