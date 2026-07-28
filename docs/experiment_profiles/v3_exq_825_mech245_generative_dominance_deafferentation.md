# Experiment Profile: V3-EXQ-825 / MECH-245

Generated for external laboratory legibility from existing repository sources only. This page is a legibility artifact, not a scientific claim edit, evidence edit, or governance decision. Sources: `REE_assembly/scripts/generate_experiment_profile.py`; `REE_assembly/templates/experiment_profile.md`.

## Scientific Question

This experiment asks whether the MECH-245 hallucination pathway is reproduced when bottom-up grounding is absent and the system's own top-down prediction is substituted as the observation at E3's bottom-up mismatch-check call site. The driver states that PRIMARY keeps the mismatch check intact by feeding the last genuinely grounded observation, while ABLATION substitutes the model prediction as if it were received sensory input. Sources: `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:9-19`; `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:20-41`; `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:42-69`.

## Claim Under Test

Authoritative claim wording: "Hallucination is a generative-model dominance failure where top-down predictions produce percepts without corresponding bottom-up sensory grounding." The claim notes specify that hallucination is a perceptual generation failure in which E1 top-down predictions propagate forward as if they were received sensory signals, bypassing or overwhelming the bottom-up mismatch check. Sources: `REE_assembly/docs/claims/claims.yaml:23855-23896`.

## Competing Explanations

- MECH-094 is documented as confabulation, a memory write-gate or source-monitoring failure, not the percept-generation pathway tested here. Sources: `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:9-19`; `REE_assembly/docs/claims/claims.yaml:6566-6601`.
- MECH-244 is documented as a precision-weighting or belief-updating failure where bottom-up evidence is present but resisted. Sources: `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:9-19`; `REE_assembly/docs/claims/claims.yaml:23855-23896`.
- MECH-246 is documented as signal-degradation or pareidolia: bottom-up input is present but too degraded, sparse, or ambiguous to constrain inference. Sources: `REE_assembly/docs/claims/claims.yaml:23897-23932`.
- MECH-247 is documented as trauma-shaped hypervigilant priors: pathological prior structure generates strong top-down predictions from minimal threat-relevant signals. Sources: `REE_assembly/docs/claims/claims.yaml:23933-23969`.

## Experimental Design

- Manipulation: after a shared grounding phase, the deafferentation window removes sensory input; PRIMARY feeds E3 the last genuinely grounded observation, while ABLATION feeds E3 the model's own rolled-forward prediction. Sources: `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:42-69`.
- Controls: both arms use the same seed, same trained forward model, same true trajectory continuation, and identical grounding phase, so they enter the manipulation window from the same confidence state. Sources: `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:42-69`.
- Dependent variables: grounded operating variance, final running variance, current precision, deafferentation mean absolute prediction error, would-commit fraction, and ground-truth drift at the end of the rollout. Sources: `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:90-103`.
- Discriminative logic: support requires PRIMARY uncertainty to rise under honest sensory absence while ABLATION sustains low variance and high confidence when top-down content is substituted for bottom-up input. Sources: `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:104-131`; `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3.json:1`.

## What Would Falsify The Claim?

- C1 would fail if fewer than 2 of 3 seeds show PRIMARY final variance / grounded variance >= 1.3 and ABLATION final variance / grounded variance <= 1.05. Sources: `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:104-131`; `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3.json:1`.
- C2 would fail if fewer than 2 of 3 seeds show (primary_final_var - ablation_final_var) / grounded variance >= 0.3. Sources: `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:104-131`; `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3.json:1`.
- C3 would fail if fewer than 2 of 3 seeds show PRIMARY/ABLATION deafferentation prediction-error ratio >= 20.0 and PRIMARY deafferentation prediction error / grounded mean absolute prediction error >= 1.2. Sources: `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:104-131`; `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3.json:1`.
- Overall PASS requires C1, C2, and C3 in at least ceil(n_seeds * 0.6666666666666666) seeds; otherwise the manifest direction would be `weakens` rather than `supports`. Sources: `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:104-131`; `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:532-560`.

## What Actually Happened?

The archived run records `outcome=PASS`, `result=PASS`, `evidence_direction=supports`, and all three criteria passing in 3/3 seeds with 2 seeds required. Sources: `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3.json:1`; `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/metrics.json:1-18`. 

| Field | Value | Source |
|---|---:|---|
| Outcome | `PASS` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3.json:1` |
| C1 confidence collapse | `3/3 seeds` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/metrics.json:1-18` |
| C2 divergence magnitude | `3/3 seeds` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/metrics.json:1-18` |
| C3 manipulation validity | `3/3 seeds` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/metrics.json:1-18` |
| Primary mean final variance | `6.82256` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/metrics.json:1-18` |
| Ablation mean final variance | `0.0111604` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/metrics.json:1-18` |
| Variance delta primary minus ablation | `6.8114` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/metrics.json:1-18` |
| Ablation-primary would-commit fraction delta | `0.644444` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/metrics.json:1-18` |
| Ground-truth drift at end | `primary=25.6893; ablation=25.6893` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/metrics.json:1-18` |

## Interpretation

The manifest summary states that PASS maps to `evidence_direction=supports`: PRIMARY sensory absence raised variance from the grounded operating point, while ABLATION sustained false confidence when the generative prediction was substituted for missing bottom-up input. This profile does not mark the run reviewed; `pending_review.md` still lists the run under PASS verify-and-close. Sources: `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3.json:1`; `REE_assembly/evidence/experiments/pending_review.md:29-34`.

## Limitations

- The ABLATION arm's per-tick prediction error is a definitional self-comparison; the driver identifies the falsifiable content as PRIMARY's deprivation-driven prediction-error magnitude, the C1/C2 confidence-collapse margins, and ground-truth drift. Sources: `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:70-89`.
- `would_commit_fraction` is reported for interpretation but is not a gating criterion because the commit threshold is calibrated to real RL z_world scale, not this synthetic scale. Sources: `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:90-103`.
- The forward model is a synthetic GRU stand-in for the top-down generative pathway; the driver states no head is trained on real z_world, z_harm, or encoder output. Sources: `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:132-136`.
- Embedded run-pack provenance is incomplete: `source_repo.commit` is empty and the environment dynamics, reward, observation, and config hashes are recorded as `unknown`; Git-history and content-hash fallbacks are listed below. Sources: `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/manifest.json:1-49`.

## Reproduction

Run from `/Users/dgolden/REE_Working/ree-v3` with the exact command below. A fresh run writes a new timestamped flat manifest under `REE_assembly/evidence/experiments/`; the archived reference run is the `v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3` output listed in Expected outputs. Sources: `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:137-140`; `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:532-560`.

```bash
/opt/local/bin/python3 experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py
```

Dry-run smoke command, documented by the same source, is available for path validation. Sources: `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:137-140`.

```bash
/opt/local/bin/python3 experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py --dry-run
```

## Expected Outputs

- Archived flat manifest: `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3.json` with `outcome=PASS` and `evidence_direction=supports`. Sources: `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3.json:1`.
- Archived run pack: `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3` with `manifest.json`, `metrics.json`, and `summary.md`. Sources: `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/manifest.json:1-49`; `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/metrics.json:1-18`; `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/summary.md:1-3`.
- Expected criteria shape for a fresh reproduction: C1, C2, and C3 all pass with the configured matched seeds `[0, 1, 2]`. Sources: `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3.json:1`; `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/metrics.json:1-18`.

## Provenance

The experiment proposal records backlog EVB-0122 as executed by V3-EXQ-825, with objective `Reduce uncertainty for MECH-245 via targeted experiment runs.` Sources: `REE_assembly/evidence/planning/experiment_proposals.v1.json:13679-13705`.

| Item | Value | Source |
|---|---|---|
| Required repo | `ree-v3` | `ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:137-140` |
| Required repo | `REE_assembly` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/manifest.json:1-49` |
| Driver source commit | `0130028a457f45bdfd7951968395336bbbbb3fb1` | `REE_assembly/scripts/generate_experiment_profile.py` |
| Result-pack commit | `4710a1a128df2118a3a6473860ba1f059490bd4a` | `REE_assembly/scripts/generate_experiment_profile.py` |
| Driver git blob | `21b3a191274b8cb74bf8d38f5686fc0b36a7c637` | `REE_assembly/scripts/generate_experiment_profile.py` |
| Flat manifest git blob | `043ba33502aab81e592497b73822363c9cf695af` | `REE_assembly/scripts/generate_experiment_profile.py` |
| Driver SHA-256 | `102ffecc0c89c7030a4d7b63e0148ee3a78ef31b8f5f9d8f9eb720be74bc0977` | `REE_assembly/scripts/generate_experiment_profile.py` |
| Flat manifest SHA-256 | `adb365044f4b9c4765592fed35299665f9485477772528aa18bb74ef9809e734` | `REE_assembly/scripts/generate_experiment_profile.py` |
| Run-pack manifest SHA-256 | `098d8598654e6c1193bc3f18f300d1ca50349ba294fc1505eb5dd97165dec301` | `REE_assembly/scripts/generate_experiment_profile.py` |
| Substrate hash | `ef7f39e80d28715ce215d9af3c473cbf09c2ea2fa64161fcee8e8da23fbf339f` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3.json:1` |

Population-gap report: `v3_exq_825_mech245_generative_dominance_deafferentation.population_report.md`. Sources: `REE_assembly/scripts/generate_experiment_profile.py`; `REE_assembly/templates/experiment_profile.md`.
