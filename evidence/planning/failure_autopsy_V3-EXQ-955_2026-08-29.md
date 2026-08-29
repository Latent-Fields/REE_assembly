# Failure Autopsy: V3-EXQ-955 (MECH-440 armed-stack falsifier at the raised class floor)

Generated: 2026-08-29T13:57:37Z · Scope: single · Status: **confirmed** (user gate 2026-08-29, "Accept override")
Run: `v3_exq_955_mech440_armed_stack_raised_class_floor_falsifier_20260829T120510Z_v3` · outcome FAIL · `experiment_purpose: evidence` · claim_ids [MECH-440]

## 1. Facts

- 3 arms x 6 seeds (42-47), 13.1h on `ree-worker-1` (hub), machine_class linux-x86_64 torch 2.12.0+cpu.
- **Dry-run gate:** `check_dry_run_citations.py` -- 1 clean, 0 dry cited. `dry_run: false` on the manifest.
- **Recording always-core:** `validate_recording.py` -- complete (rec/v1, substrate_hash, config, seeds, elapsed).
- Design: V3-EXQ-708b's three-arm design with ONE integer changed -- `support_preserving_min_first_action_classes = action_dim (5)` instead of the default 2 -- plus the V3-EXQ-949 yoked-pair / private-RNG-stream instruments (per-tick committed-action divergence; authority_rel_deviation; fraction-of-ceiling DV).
- **All armed-conversion preconditions on the lever arms MET and MEASURED** (first time in the lineage): P1 candidate diversity 4.78-4.89/5 (thr 4.5), P2 authority engaged 0.85-0.87 (thr 0.05), fresh selects 1030-2129 genuine fires per cell, noise bias supra-floor, dACC live, self-yoke bit-identical (paired_control_divergence_max = 0.0).
- **C1 -- the ONLY load-bearing criterion -- PASSED**: `n_noise_above_temp = 5/6`, `n_noise_reaches_committed = 6/6`, bar = 4 (2/3 of 6). Red-team independently recomputed both from the per-seed cells.
- **The FAIL came from the arm gate alone**: A0_OFF failed `ceiling_headroom_below_saturation` -- `max()` across seeds = 0.9732 (seed 44) vs threshold 0.90. Second-max is 0.886; arm mean 0.833.

Per-seed (fraction-of-ceiling; yoked divergence):

| seed | OFF frac | TEMP frac | NOISE frac | TEMP yokdiv | NOISE yokdiv | noise>temp |
|---|---|---|---|---|---|---|
| 42 | 0.8754 | 0.8754 | 0.9193 | 0.0 | 0.786 | yes |
| 43 | 0.6291 | 0.6291 | 0.9799 | 0.0 | 0.685 | yes |
| 44 | **0.9732** | 0.9115 | 0.8675 | **0.686** | 0.777 | **no** |
| 45 | 0.8678 | 0.8678 | 0.9376 | 0.0 | 0.880 | yes |
| 46 | 0.8862 | 0.8862 | 0.9812 | 0.0 | 0.718 | yes |
| 47 | 0.7681 | 0.7681 | 0.9227 | 0.0 | 0.718 | yes |

## 2. The defect: a null-protection gate vacated a positive

The driver's pre-registered docstring scopes the headroom check to the null branch: "CEILING-HEADROOM CHECK (**precondition on the falsifying branch specifically**): A0_OFF's fraction-of-ceiling must be materially below 1.0 -- a null in the OFF arm is uninformative (nothing to lift)", and FAIL class (a) is "valid ONLY once the ceiling-headroom check passes". The VACUITY RULE's enumerated requeue triggers (P1/P2 unmet, insufficient fresh selects, noise non-vacuity, dACC flat) do NOT include it.

The code instead folds the check into `armed_ok` (driver ~1414-1418) and orders it ahead of C1 (~1443-1450), so a run with a POSITIVE C1 self-routes `substrate_not_ready_requeue` / direction `unknown`. Two compounding choices:

1. **Aggregation**: `max(r["committed_class_entropy_fraction_of_ceiling"] for r in rows)` (line 1372) -- one seed reds the arm. C1 itself already absorbs seed heterogeneity with a 2/3 majority.
2. **Branch ordering**: the gate fires before the supports branch, contradicting the docstring's stated scope. (The dedicated `elif "A0_OFF" not in green` branch is unreachable given `armed_ok`'s definition -- hygiene, not load-bearing.)

The manifest's own `degeneracy_reason` states the correct rule: "a red arm does NOT vacate a green one ... Read the red arm(s) as unscored, NOT as a refutation."

**Strictest reanalysis (red-team):** dropping seed 44 entirely -- the only seed whose OFF exceeds the 0.90 headroom threshold -- C1 is 5/5 on both sub-conditions against a bar of 4. The supports read survives per-seed application of the gate's own logic.

## 3. Seed 44: a coupled anomaly, recorded not hidden

Seed 44 is anomalous in three coupled ways: OFF near saturation (0.973); the "non-propagating" temperature control diverging massively (yoked 0.686 -- every other seed exactly 0.0, the pre-registered DV-symmetry expectation); and the one seed where noise < temp. One coherent explanation: near-uniform committed behaviour makes score vectors near-tie, so any perturbation flips argmins and lift comparisons compress. This is exactly the state the headroom precondition exists to detect -- per-seed. It is evidence for per-seed gating, not for vacating the run.

## 4. Claim layer (Step 3) and biological triage (Step 4)

MECH-440 (`candidate`, v3_pending, no explicit epistemic_category): LC-NE tonic floor as learned per-parameter (factorised-Gaussian) weight noise in the E3 selection pathway, asserting (i) PROPAGATION to committed action, (ii) STATE-CONDITIONING, (iii) SELF-ANNEALING. This run tests **leg (i) only** and the claim could express itself (preconditions armed and measured) -- alignment **strengthened**, narrowly. Legs (ii)/(iii): `secondary_checks_measured=false`, the driver's declared honest gap.

Lineage: 708 (measurement_test_design_defect -- cadence pseudo-replication), 708a (measurement_gap -- no injected variance), 708b (measurement_test_design_defect -- class-floor ceiling; `precommit_shape_headroom_unexplained`, GFLAG-0072). 955 is the fourth consecutive MECH-440 adjudication locating the problem in the instrument, but the first where the DV is sound and positive -- only the self-route label logic misfired. The raised floor confirmed 708b's third unenumerated reading: OFF fraction-of-ceiling fell 0.978 -> 0.833 mean.

Biology: NoisyNet is a formal import; the biological analog (LC-NE) is carried by legs (ii)/(iii), untested here. lit_status partial -- no lit-pull commissioned (the divergence question only becomes decidable when legs ii/iii are measured).

## 5. Four-layer diagnosis + failure location (GOV-FAILLOC-1)

| Layer | Status |
|---|---|
| Claim alignment | strengthened (narrow -- leg i) |
| Biological reference | clear (propagation leg upstream-neutral to the biology) |
| Prerequisites | present (ARC-065 stack armed as matched constant) |
| Implementation | complete for leg (i); legs (ii)/(iii) unmeasured |
| Environment | adequate (raised floor opened real headroom) |
| Measurement | under-instrumented at the ADJUDICATION layer only |
| Integration | coupled and stable (5/6 seeds match the pre-registered signature exactly) |
| Scale | adequate (6 seeds, 1030-2129 fresh fires/cell) |

**Failure-location: MEASURES FAILED (adjudication-branch logic only).** Mechanism not_established-as-failed (it performed); environment adequate; `ree: false`. Not chargeable to REE.

## 6. Brake, granularity, checks

- **Re-derive brake: NOT fired** -- 0 `substrate_ceiling` hits for MECH-440 under R1-R3 (708's old ceiling read superseded 2026-07-19 to measurement_test_design_defect).
- **Granularity-debt trigger: does not fire** -- `granularity_debt_cluster.py MECH-440`: 4 targets, alignment distribution unclear=2 / intact=1 / untested=1, NO `weakened` target -- measurement debt, not granularity debt.
- **Step 7b pre-routing checks: 0 fires** (C1/C2/C3 keyed on MECH-440, quiet; C5 inapplicable pre-.md).
- **Step 7c red-team: CONFIRMED** (`redteam_V3-EXQ-955` scratch record) -- independently recomputed C1 from cells; confirmed max-aggregation, A0_OFF-only scope, seed-44-only failure; confirmed the docstring/code divergence with exact quotes; found the supports read SURVIVES the strictest per-seed reanalysis (5/5). Hygiene findings folded into the JSON's learning_extracted.

## 7. Learning extracted and repair pathway (Step 7)

Node classification: `complex (probe-gated) / mystery (known data)` for the propagation question -- the data is in hand; the frame (self-route logic) was wrong; **reanalysis resolves it, no re-run**. The untested legs (ii)/(iii) are `complex (probe-gated) / puzzle (known rules)` -- a fact is missing, get it with a new probe.

**Routing: `/queue-experiment`, NEW EXQ** for state-conditioning + self-annealing (per-state noise-magnitude covariance with state; per-parameter sigma trajectory vs policy confidence), on the same armed raised-floor stack. Explicitly NOT a 955a same-question re-run. Driver-fix note for any design reuse: headroom gate per-seed (or mean), falsifying-branch only. Substrate queue: action **none** (the defect is a driver adjudication branch, not ree_core substrate; no severity classification owed -- nothing here corrupts other experiments' evidence).

Per the 2026-07-30 rule this session spawns NO chip for its own routing; `/governance` chips it once Step 2b ratifies.

## 8. Recommended governance writes (drafted, not applied)

- Manifest `evidence_direction`: unknown -> **supports** + `evidence_direction_note` (fallback workaround; rebuild index after).
- MECH-440 `evidence_quality_note`: the drafted note in the JSON (`recommended_evidence_quality_note`).
- MECH-440 gains explicit `epistemic_category: standard` (currently absent; behaviour-preserving). Status stays `candidate`. `pending_retest_after_substrate` cleared -- the retest has now happened, armed and measured. `v3_pending` disposition is governance's call (this IS v3 evidence for leg i; legs ii/iii still open).
- `recommended_diagnostic_evidence_adjudicated`: not set -- `experiment_purpose: evidence`, the flag is for diagnostic/baseline targets only.

## 9. Hypothesis-space ledger (Step 9b)

New question `mech440_noise_propagation_to_committed_diversity` registered and resolved same-cycle (Mode B new-question shortcut; pre-registration git-witnessed by the driver commit `ree-v3 6d07074`, 2026-08-28, which enumerates the PASS/FAIL classes): **H-propagates confirmed** (control passed, non-degenerate); **H-washout-at-argmax eliminated** (divergence 0.68-0.88 on 6/6 seeds vs 0.02 floor); **H-thrash-not-carve eliminated** (divergence co-occurs with sustained committed-class entropy lift). No growth restriction applies (new question). Full bar met on both eliminations.
