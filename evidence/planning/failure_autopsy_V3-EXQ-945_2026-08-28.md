# Failure Autopsy (diagnostic adjudication): V3-EXQ-945 -- CEM elite authority + throughput readiness

**Generated:** 2026-08-28T17:11:55Z | **Scope:** single | **Status:** confirmed (interactive gate 2026-08-28)
**Session:** failure-autopsy-20260828-diagbatch | **Trigger:** `experiment_purpose: "diagnostic"`, clean unflagged PASS, no prior autopsy coverage.
**Run:** `v3_exq_945_cem_elite_authority_throughput_readiness_20260825T210111Z_v3` (ree-cloud-2, clean substrate 85032d0d, recording complete, dry-run gate clean).

## Facts

Readiness diagnostic for the 2026-08-19 CEM elite-stage modulatory-authority + throughput build. Claim-free by design; its stated purpose is to license flipping substrate_queue `modulatory-bias-selection-authority`'s failure_record (run v3_exq_931) from `resolved: open`. 4 arms x 5 seeds; lever = mode_value (pre-registered substitution for 931's wanting_weight, which is identically zero in the fresh-ResidueField wash-out regime).

- PASS = P1 AND C_AUTH AND C_THROUGHPUT. P1 1.0 vs 0.8. C_AUTH 5/5 seeds (flip_rate > 0, competitive_frac 1.0). C_THROUGHPUT exactly 3/5 = the pre-registered floor: proximity gaps 0.0 / 0.0 / -0.040 / +0.090 / +0.062 -- seeds 42/43 behaviourally bit-identical to ablation despite positive flip rates (the 931 null signature persisting on those seeds).
- ARM_OFF, ARM_AUTH_RANGE, ARM_AUTH_STD behaviourally bit-identical per seed on all 5 seeds -- elite stage confirmed advisory-only without routing.
- OFF-arm flip rate 0.93 with raw modulatory:terrain ratio 19-137: mode_value is naturally dominant; the gain-0.5 rescale NORMALISES it down (scale ~0.004-0.026 per tick, attenuate-only). The amplify-up regime 931's failure exercised was run by zero cells.
- Non-gating NO-HARM readout regressed: +0.065 arm-mean harm rate under routing.
- Instrument defect (reported-only, not a criterion input; verified): `cem_modulatory_throughput_available` is a hippocampal propose-diagnostics key; the driver reads it from `e3.last_score_diagnostics`, so the reported frac is 0.0 in all 20 cells by construction.

## Four-layer diagnosis

| Layer | Status |
|---|---|
| Claim alignment | n/a (claim-free readiness diagnostic) |
| Biological reference | absent (planner-internals engineering) |
| Prerequisites | present |
| Implementation | complete (mechanism); instrument defect on one reported field |
| Environment | adequate |
| Measurement | partially adequate -- C_AUTH strong; C_THROUGHPUT at-floor, direction-agnostic |
| Integration | partially coupled (route reaches behaviour on 3/5 seeds) |
| Scale | adequate |

GOV-FAILLOC-1: not applicable (PASS). Corollary: this PASS licenses "throughput exists" only, never "throughput helps" (harm regressed; gaps direction-mixed).

## 7b / 7c

7b: 0 fires (claim-keyed checks blind on a claim-free target). 7c red team: **CONTESTED (narrowly)** -- every number survived independent recomputation; the one defect (D1) is that the failure_record's own metric line names wanting_weight=0.5 as "the documented operating weight", so "meets the target as written" was wrong -- the target is met under a pre-registered LEVER SUBSTITUTION, in the attenuate-only regime only. Disposed: resolved_note rewritten to state the substitution, the untested amplify-up regime, the at-floor throughput and the harm regression verbatim. Attacks that failed: competitive_frac is not structurally pinned (931 read it false); the OFF-arm counterfactual uses the live selector's own scale; the wrong-dict read is confirmed real and confirmed non-criterion.

## Adjudication (user-confirmed at the gate)

Self-route label CONFIRMED with caveats. `recommended_epistemic_category: standard`; `recommended_evidence_direction: non_contributory` (weights no claim). **User decision: flip the v3_exq_931 failure_record to resolved with the substitution and caveats stated verbatim** (the record's addressed_by schema contemplates "a later build/lever").

## Routing

`queue-experiment` -- the behavioural falsifier the design doc (cem_elite_authority_throughput_design_2026-08-19.md Section 8) gates on exactly this PASS: both gates (build landed; competitive spread ratio) now established. Governance chips it once ratified; this autopsy spawns nothing. Substrate action: `amend` on `modulatory-bias-selection-authority` (resolves_prior_failure_record -- see JSON). Any 945-successor must fix the wrong-dict throughput-available read.
