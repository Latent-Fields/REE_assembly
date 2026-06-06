# Failure autopsy — V3-EXQ-641 (coherence-ablation: is C(τ) non-reducible to E(τ)?)

- **Generated (UTC):** 2026-06-06T04:13:20Z
- **Scope:** single
- **Status:** confirmed (interactive gate answered 2026-06-06)
- **Run:** `v3_exq_641_coherence_ablation_nonreducibility_20260606T021359Z_v3`
- **Queue id:** V3-EXQ-641 (removed from queue on completion)
- **Outcome:** FAIL · `evidence_direction: non_contributory` (diagnostic, `claim_ids: []`)
- **`majority_label`:** `C_changes_selection_specificity_unproven_route_followup`
- **Machine:** DLAPTOP-4.local
- **Settles (gated):** `thought_intake_2026-04-23_binding.md` + `thought_intake_2026-04-23_path_integral_constraints_search.md` — both kept **OPEN** by this autopsy.

This is a **FAIL** (ran to completion, scientific criteria not met), correctly routed here and not to `/diagnose-errors`: all 9 runs completed (`n_runs_completed: 9/9`, every `error_note: null`).

---

## 1. What the experiment tested

A claim-free diagnostic ablation built to settle two 2026-04-23 intakes at once via one shared discriminator:

> Is the coherence term `C(τ)` **non-reducible** to integrated prediction error `E(τ)`, and does varying `C` change **behaviour** in a **coherence-specific** way (not reproducible by a range-matched random tie-breaker)?

- `E(τ)` = the substrate's own per-candidate cost `e3.score_trajectory(...)` (identical call for both arms → E identical by construction).
- `C(τ)` = harness-computed cross-system temporal/phase consistency over the rollout window: geometric mean of (a) per-stream temporal-consistency `1 − ‖z_{t+1}−z_t‖/‖z_t‖` over `world_states`/`states`/`action_objects` and (b) a `world_states↔states` cross-stream delta-alignment term (weight 0.5).
- Arm A = `argmin E` (pure error-minimiser); Arm B = `argmin(E + λ·(−log C))` with λ **gap-relative** so the coherence-term range = `0.5·range(E)` (the substrate's modulatory-authority pattern).
- Three conditions × 3 seeds: `real_C_clean` (PRIMARY), `rand_C_control` (range-matched random C, SPECIFICITY), `real_C_perturb` (perturb 0.20 on z_world, REBINDING).

Acceptance per primary seed: **D1** `frac_state_div ≥ 0.05`, **D3** `|Spearman corr(E,C)| < 0.90`, **SPEC** `real_div ≥ rand_div + 0.05`. Run PASS = D1∧D3∧SPEC on ≥2/3 seeds.

`bears_on_not_tagged`: INV-002, ARC-018, MECH-061, MECH-269, MECH-270 — cited only; **none tagged**, so this run carries **zero** confidence/conflict weight on any claim.

## 2. Facts — which criterion failed

`n_D1=2`, `n_D3=3`, `n_coherence_specific=1`, `n_seed_pass=1` (need ≥2). The failed criterion is the **SPEC discrimination criterion**, not an absolute/negative-control criterion.

| seed | D1 `frac_state_div` | D3 `\|corr(E,C)\|` | real_div vs rand_div (SPEC) | SPEC | contacts a/b | P1 steps | `tie_higher_c_frac` real / rand |
|---|---|---|---|---|---|---|---|
| 42 | ✓ 0.906 | ✓ 0.089 | 0.906 vs 0.845 = **+0.061** | ✓ | 257/223 | 512 | 0.435 / 0.557 |
| 43 | ✓ 0.224 | ✓ **0.701** | 0.224 vs 0.655 = **−0.431** | ✗ | 0/0 | 2673 | 0.344 / 0.589 |
| 44 | ✗ 0.000 | ✓ 0.139 | 0.000 vs 0.253 = **−0.253** | ✗ | 0/0 | 177 | 0.400 / 0.583 |

`n_rebind_under_perturb = 0` on **all three** seeds.

## 3. The load-bearing signal — this is NOT a clean falsification

Three concrete confounds make the SPEC failure a **measurement/test-design gap**, not evidence that coherence is reducible to E:

1. **Real coherence is a *weaker* tie-breaker than random noise.** On seeds 43/44 `real_div ≪ rand_div`. At matched-E ties the higher-C candidate is chosen **below chance** under real C (`tie_higher_c_frac` 0.34–0.44) but **above chance** under random C (0.56–0.59). The harness coherence read is **low-contrast**: the pre-flight noted `−log C` spreads ~O(0.004); gap-relative rescaling normalizes the *range* but leaves a near-flat distribution with a couple of outliers, so most candidates get near-identical bias and ties break essentially arbitrarily (or on E), whereas uniform-random in (0.5,1.0] gives every candidate a decisive distinct bias. **Random wins SPEC by being higher-contrast, not by lacking the structure C has.**
2. **The proxy leaks E.** Seed 43 `|corr(E,C)| = 0.70` — temporal-smoothness is partly a reparameterisation of the score's reality-cost term (the F2 reducibility risk leaking in below the 0.90 D3 threshold). D3 "passing" at 0.70 understates how much E-information the proxy carries.
3. **The binding intake's own prediction was never exercised.** `n_rebind_under_perturb = 0` across all seeds — perturb=0.20·rms on z_world never changed B's committed pick vs its clean-rank pick. And **2/3 seeds reached zero benefit contacts**, so the SD-054 reef-vs-forage two-mode tie distribution only materialised in seed 42. `n_seed_pass=1` vs 2 is within the enormous per-seed variance (177 ↔ 2673 P1 steps).

## 4. Biological-reference triage

- **Closest mechanism class:** binding-by-coherence / phase-synchrony in cortical assemblies and hippocampal sequence coherence (INV-002 "coherence includes temporal/phase binding"; MECH-269 verisimilitude; MECH-270 ephaptic carrier). This is a real biological class — an existence proof for *the class*, not for the current harness proxy.
- **Formal-import flag:** the path-integral / least-action framing is an explicit **formal import**, exactly the "philosophy-right / mechanism-wrong" risk class (`feedback_biology_before_formal_definitions`). Both intakes already commit (correctly) to registering a claim **only** on behavioural divergence that a pure error-minimiser cannot reproduce **and** that is coherence-specific.
- **Translation verdict:** the harness `C` (temporal-smoothness geometric mean) is **not a faithful translation** of phase/binding coherence — it is a smoothness statistic that partly reduces to E (seed 43) and is too low-contrast to drive specific selection. The SPEC failure indicts **the proxy**, not the mechanism class.
- **Missing-dependency signature?** No — this is not "a known dependency of the reference mechanism is absent." It is "the measurement of the mechanism is crude and partly co-linear with the thing it must be shown independent of."

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | candidate Q `selection.coherence_nonreducibility` **not registerable** (SPEC gate uncleared) **and not falsified** (measurement gap). No registered claim touched. |
| Biological reference | partial / formal-import | binding-by-coherence is a real class; path-integral is a formal import; temporal-smoothness proxy is not a faithful translation and partly reduces to E. |
| Developmental / prerequisites | degenerate | 2/3 seeds zero benefit contacts → degenerate tie distribution; SD-054 bipartite two-mode partition only realised in 1/3. |
| Implementation completeness | symbol-not-role | C has the *symbol* of coherence but at matched-E ties selects higher-C below chance; rebinding instrument produced flat-zero. |
| Environment adequacy | too sparse (as executed) | reef-vs-forage two-mode pressure present by design but only realised in seed 42's contact-rich rollout. |
| Measurement adequacy | under-instrumented / misleading | low-contrast + E-correlated C; random out-performs it as a tie-breaker; `n_rebind=0` everywhere. |
| Integration adequacy | n/a | selection re-implemented in harness; no module-interaction failure. |
| Scale / capacity | insufficient | 3 seeds, variance 177↔2673 P1 steps; pass-count within seed-noise. |

**Recommended epistemic category:** measurement / test-design gap (N/A for governance — no claim; manifest `evidence_direction: non_contributory` is already correct and is **not** changed).

## 6. Learning extracted

1. **Do not register** the candidate Q `selection.coherence_nonreducibility` — the intakes' own SPEC gate is uncleared. Firm regardless of follow-up.
2. **Do not close the intakes yet** — the SPEC failure is confounded by (a) a low-contrast / E-leaking coherence proxy that loses to random noise as a tie-breaker, (b) 2/3 degenerate zero-contact seeds, and (c) a flat-zero rebinding axis. A clean close would require SPEC to fail with an **adequate** coherence read on contact-rich seeds with a working rebinding instrument.
3. **A range-matched random control is only a fair SPEC baseline if the real signal is matched on *contrast/distribution-shape*, not just range.** Gap-relative range normalization alone lets a high-contrast random control beat a near-flat real signal — a generalisable test-design lesson for any "is X-specific beyond a random tie-break?" ablation.
4. **`cand_world_pairwise_dist`-style low per-candidate spread recurs** as the upstream reason a harness-level read goes near-flat (cf. the SD-056 / V3-EXQ-571 E2-collapse lineage). The coherence read inherits whatever per-candidate spread the candidate pool carries; sparse-contact seeds shrink it further.

## 7. Repair pathway + routing (user-confirmed 2026-06-06)

**Routing: `/queue-experiment` → V3-EXQ-641a** (same scientific question, redesigned instrumentation → alphabetic suffix). **Not** implement-substrate (no `ree_core` gap — the coherence read is harness-level), **not** lit-pull (binding/coherence biology already anchored in INV-002/MECH-269/MECH-270), **not** governance-demotion (no claim).

Both intakes stay **OPEN** (gated), annotated with this result.

Redesign levers for V3-EXQ-641a (user selected **all three**):

- **(L1) E-orthogonalized coherence read.** Residualize/whiten `C` against `E` per candidate-pool (or drop the temporal-smoothness term and keep only the cross-stream phase-alignment term, or whiten C against E per-pool) so SPEC tests coherence *structure* rather than smoothness-that-correlates-with-E. Targets the seed-43 `corr=0.70` leak and the low-contrast distribution. Also fix the SPEC control to match the real signal on **contrast/distribution-shape**, not just range (e.g. a shuffle-of-real-C control rather than uniform-random), so the baseline is not unfairly high-contrast.
- **(L2) Contact-gated window + more seeds.** Restrict the measurement window to contact-rich / two-mode-active steps and raise to 5–7 seeds, so the SD-054 reef-vs-forage tie distribution is actually present and the pass-count is above seed-noise (was 1 vs 2 on 3 high-variance seeds).
- **(L3) Stronger rebinding instrument.** Raise the perturbation magnitude and/or apply it at detected tie-ticks; `n_rebind_under_perturb=0` across all seeds means the binding intake's own falsifiable prediction was never tested. Decisive for the **binding** intake specifically.

There is no `evidence_quality_note` for governance to write (no claim, no manifest field change). The only governance-adjacent action is the intake annotation, captured by this artifact.

## 8. Cross-references

- Manifest: `REE_assembly/evidence/experiments/v3_exq_641_coherence_ablation_nonreducibility_20260606T021359Z_v3.json`
- Script: `ree-v3/experiments/v3_exq_641_coherence_ablation_nonreducibility.py`
- Intakes: `REE_assembly/evidence/planning/thought_intake_2026-04-23_binding.md`, `..._path_integral_constraints_search.md`
- Memory: `feedback_biology_before_formal_definitions` (formal-import caution), `project_object_representation_thread` (binding lineage)
- Claims cited (untagged): INV-002, ARC-018, MECH-061, MECH-269, MECH-270
