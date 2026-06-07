# Failure Autopsy -- V3-EXQ-624b (MECH-320 / ARC-068 Niv-vs-Salamone dissociation, authority ON)

- **Generated (UTC):** 2026-06-07T07:55:01Z
- **Scope:** single
- **Status:** confirmed (user-adjudicated 2026-06-07)
- **Run ID:** `v3_exq_624b_arc068_mech320_niv_salamone_dissociation_20260607T051206Z_v3`
- **Queue ID:** V3-EXQ-624b (supersedes V3-EXQ-624a, the zeroed-lever FAIL)
- **Claims:** MECH-320 (`tonic_vigor_coupling_score_bias` / w_passive), ARC-068 (`opportunity_cost_no_op_penalty`)
- **Routed from:** /governance 2026-06-07
- **Verdict:** non_contributory overall, **with `narrow_supports_flag=true`** -- the C2 dissociation is narrow positive support for ARC-068/MECH-320. Route: /queue-experiment re-spec (no substrate gap). **Neither claim weakened.**

## 1. Facts (no interpretation)

| Criterion | Per-seed [42, 43, 44] | All-seeds | Read |
|---|---|---|---|
| C1 Niv lift (ARM_1 - ARM_0) >= 0.03 | [0.000, 0.259, 0.045] -> [F, T, T] | **False** | seed 42 zero lift |
| C2 dissociation \|d_arm2 - d_arm1\|/max < 0.5 | [0.000, 0.103, 0.023] -> [T, T, T] | **True** | dissociation holds every seed |
| C3 gate_product (vigor fired) | [T, T, T] | True | forced-vigor probe fired |
| C4 no-op penalty observable | [F, T, T] | False | seed 42 no no-op opportunity |
| C5 authority active+ranged | [F, T, T] | **False** | seed 42 authority inert (range 0) |

Mean action_density by arm: ARM_0 0.8649, ARM_1 (vigor/Niv) 0.9663, ARM_2 (vigor/Salamone) 0.9739, ARM_3 (baseline/Salamone) 0.8818. ARM_1 authority: active_frac 0.629, authority_range 6.29e-03, raw_score_range 5.87, scale 173.5 (no explosion). 3 seeds x 4 arms x (P0 100ep warmup + P1 30ep x 200 steps). `use_modulatory_selection_authority=True`, gain=0.5.

**Expected vs observed.** Expected: vigor raises action density (C1) AND the no-op penalty bias has authority over the argmin (C5) on every seed, while the w_passive cost stays insensitive to parametric movement cost (C2 dissociation). Observed: C2 dissociation clean on all seeds; C1/C5 fail on seed 42 only. Failed criterion = **negative_control / non-vacuity conjunction** (C1+C5), not the discrimination criterion (C2 passed).

## 2. The load-bearing observation

The actual scientific content -- the **Niv-vs-Salamone dissociation (C2)** -- **passed on all 3 seeds**, including the env-degenerate seed 42. The FAIL is entirely in the positive-control/non-vacuity conjunction, which failed on a single seed where the well-fed-safe-familiar regime presented no no-op opportunity (action_density headroom near-saturated), so the w_passive bias was exactly zero -> authority inert -> Niv lift 0.0. Seeds 43/44 show clear vigor lift and operative authority -- positive evidence the 643a authority fix works.

## 3. Claim-layer mapping

- **MECH-320 / ARC-068** (collapsed per ARC-068 R3: w_passive IS the ARC-068 implementation). The R4 verdict under test: w_passive must remain **insensitive to parametric movement cost** (Niv opportunity-cost-on-time), distinct from MECH-258/SD-032b dACC effort cost (Salamone). C2 is the direct test of that and it PASSED at all seeds -> narrow positive support. The experiment let the dissociation claim express itself.
- The positive control (does vigor lift action density at all, with the bias reaching the argmin) is what failed -- on one seed, for env-adequacy reasons. That does not bear on the dissociation claim's truth.

## 4. Biological-reference triage

- Closest mechanism: mesolimbic-DA average-reward-rate vigor (Niv 2007 opportunity-cost-on-time), dissociated from dACC effort cost (Salamone & Correa 2003). Lit status: present (ARC-066 lit-pull R3/R4).
- Not a formal-definition import. The dissociation confirmed IS the biologically-motivated separation. The failure resembles what happens biologically if the agent is in a context with no waiting/no-op option to penalise -- the opportunity-cost mechanism has nothing to act on. That is a missing-opportunity (environment) signature, not a falsification.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | strengthened (narrow) | C2 dissociation PASS all seeds; positive control failed on seed 42 only |
| Biological reference | clear | Niv-vs-Salamone separation is the lit-grounded target |
| Dependency prerequisites | present | 643a authority operative; vigor fired (C3 all seeds) |
| Implementation completeness | complete | authority reached argmin on 2/3 seeds, no score explosion |
| Environment adequacy | **too sparse (1 seed)** | well-fed-safe-familiar regime no-op-opportunity-poor; seed 42 no headroom |
| Measurement adequacy | brittle guard | all-seeds non-vacuity conjunction poisoned by one env-degenerate seed |
| Integration adequacy | coupled+stable | on seeds with a no-op opportunity |
| Scale / capacity | adequate | -- |

**Dominant diagnosis:** environment-adequacy / seed-robustness gap (descriptive `epistemic_category=environment_adequacy_defect`; NOT substrate_ceiling, NOT falsification).

## 6. Learning extracted

- 643a authority substrate is proven operative for the vigor/no-op-penalty lever (vigor lift on 2/3 seeds) -- positive contrast to 614e where the bottleneck is upstream (GAP-A).
- The Niv-vs-Salamone dissociation is robust (C2 PASS all seeds) -> narrow support for ARC-068/MECH-320 movement-cost insensitivity.
- The well-fed-safe-familiar regime is no-op-opportunity-poor; the opportunity-cost mechanism needs a regime that reliably presents stationary/no-op candidates.
- All-seeds non-vacuity conjunctions are brittle for sparse-opportunity mechanisms; prefer >= 5 seeds or a majority gate on the positive control while keeping the dissociation gate strict.

## 7. Repair pathway (routing = queue-experiment; substrate action = none)

No substrate gap -- the modulatory-bias-selection-authority substrate is implemented + ready and proven operative here. Owed work via /queue-experiment: a successor (e.g. V3-EXQ-624c) on a **no-op-opportunity-rich regime** (lower baseline action density / forced-wait pressure) and/or **>= 5 seeds**, so the Niv positive control + authority express on every seed. Keep the C2 dissociation gate strict. ARC-068/MECH-320 stay candidate / v3_pending=true with the narrow-supports note; no confidence move, not weakened.

### Draft evidence_quality_note (governance to write -- do not write here)

See `recommended_evidence_quality_note` in the JSON sibling.

## 8. Routing decision (user-confirmed)

`non_contributory + narrow-supports note` -- record C2 dissociation as narrow positive support; re-queue with no-op-rich regime + more seeds; neither claim weakened. Confirmed via AskUserQuestion 2026-06-07.
