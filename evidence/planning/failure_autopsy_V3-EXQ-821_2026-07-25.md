# Failure Autopsy — V3-EXQ-821 (MECH-457, H-consummation-binding, GOV-FANOUT-1 retention leg 4)

**Generated:** 2026-07-25T22:38:43Z · session `clever-antonelli-2e8f4f`
**Scope:** single · **Status:** confirmed (user-adjudicated 2026-07-25)
**Outcome:** FAIL · self-route `consummation_binding_eroded_under_both` · **DIAGNOSTIC** (excluded from scoring; promotes/demotes nothing)
**Run:** `v3_exq_821_mech457_consummation_binding_20260725T222252Z_v3` · substrate_hash `b03e6515…d122b129` · DLAPTOP-5 · darwin-arm64-py3.13-torch2.12.0 · elapsed 5544.8s · seeds [42,43,44]

---

## 1. Facts (no interpretation)

**Hypothesis.** Was V3-EXQ-781's drive-side null an artefact of a *missing consummatory act*? 781 gave the bootstrap an innate non-extinguishing appetitive approach drive and found the drive earned (0.707) while raw-view foraging was suppressed to 0.200 (from a 2.983 control) — approach *without* consummation. H-consummation-binding: 781's terminal drive was non-extinguishing, so there was no mechanism to terminate on arrival and hand off to a distinct act of consuming. The 2026-07-25 builds make contact *afford* rather than *effect* consumption (a distinct CONSUME action, `mech457_consummatory_act`) and let the approach drive *extinguish* on contact (`mech457_approach_extinction`) so it hands off to CONSUME.

**Design.** Single-knob manipulation `approach_extinguishes_on_contact` (OFF control vs ON treatment). Both arms: consummatory env, BC-installed raw_view policy, approach drive (`use_approach_primitive`, `approach_coef=1.0`), reference build (128-wide / 3× budget / z_world detached / credit-replay 3 / topk 32 / bc_aux 0.5). Anti-aliased against the three other retention nodes (value estimator / KL anchor / bc_aux schedule held at defaults). DV = the post-install competence **trajectory** (retention probe every 250 ep, 12 readings/cell), not a terminal scalar. Adjudicated against each arm's own post-BC install (consummatory band ~13, measured live via anchors).

**Preconditions — all met (this is NOT a `substrate_not_ready_requeue`):**
- Install took: post-BC foraging **4.3 / 5.7 / 4.3** on both arms, all > the 1.0 install floor (worst seed 42 = 4.3).
- Consummatory env solvable: `local_view_greedy = 34.2`, `greedy_oracle = 42.8` (both > 1.0).
- Criteria non-degenerate: all five non-degeneracy flags true; both arms green; no vacuous arm.

**Result.** After RL, `retained_fraction = 0.0` on **all 3 seeds in BOTH arms**. Arm margin **0.0** (< 0.15 retention margin). Trajectory peaks: extinct_off [0.4, 0.0, 0.0], extinct_on [0.85, 0.0, 0.0] — **neither arm's peak re-cleared the install floor on any seed**. Half-life 250 (gone by the first probe). Approach reward still earned ~0.8 in *both* arms while forage/CONSUME collapsed to 0.

**Failed criterion:** the load-bearing discrimination criterion `C_extinguishing_drive_retains_installed_competence` (extinguishing arm holds a strict majority of seeds at retained_fraction ≥ 0.5 AND beats the control by ≥ 0.15). The non-load-bearing control criterion (control erodes) *passed* as predicted.

---

## 2. Claim-layer mapping

`MECH-457` (competence floor / conversion ceiling; candidate, v3_pending). This is a **diagnostic** run: `experiment_purpose=diagnostic`, `claim_ids=["MECH-457"]` tags relevance only → excluded from governance confidence/conflict scoring. The test let the *leg* express itself under conditions where it could have succeeded (install took, env solvable), so the elimination is well-founded. MECH-457's parent status is untouched — what is falsified is a specific rival dependency (H-consummation-binding), not the claim.

---

## 3. Biological-reference triage

**Closest mechanism.** The ethological appetitive/consummatory distinction (Craig 1918; Sherrington): appetitive approach/seeking behaviour terminates in a *consummatory act* that resolves the drive, and a satiety signal extinguishes the appetitive signal. In mammals, mesolimbic dopaminergic seeking hands off to consummatory (hypothalamic/brainstem) circuitry. The hypothesis — that a proper CONSUME act plus extinction-on-contact would let the installed forage competence survive — is a **faithful biological translation**, not a formal import, and it is biologically well-motivated.

**Divergence / verdict.** The consummatory binding was *present and functional* (CONSUME wired, extinction active, env solvable, install took) yet the installed foraging **policy** was not protected against the ongoing RL gradient. The failure resembles what would happen biologically if a **different dependency were missing** — protection/consolidation of an acquired policy against continued value updating — rather than "the consummatory binding is the retention mechanism." A **discovered non-dependency**: consummatory binding is *not* the retention lever. This points at the value-estimator / consolidation axis (H-retention-critic), which already carries 780/782 support.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | Diagnostic; eliminates a rival leg, not MECH-457. Neither supported nor weakened. |
| Biological reference | clear | Craig/Sherrington appetitive→consummatory hand-off; cleanly refuted *as the retention lever*. |
| Prerequisites | present | Install took (4.3–5.7 > 1.0); CONSUME wired; extinction active; env floor-achievable. |
| Implementation | complete | 3 substrate builds landed; single-knob anti-aliased; substrate_hash stable across run. |
| Environment | adequate | Consummatory env, resource retained until CONSUME, both anchors clear floor. |
| Measurement | adequate | Retention trajectory (12 readings/cell), peak + terminal, non-perturbing probe, non-degenerate. |
| Integration | coupled but unstable | Composition correct; failure is in the coupled behaviour (RL erodes the BC install). |
| Scale | adequate | 3000 ep / 3 seeds / 128-wide-3× build; half-life 250 → not budget starvation. |

**Dominant diagnosis:** clean pre-registered discrimination → `epistemic_category = standard` (consistent with 781, same axis/shape). Not a ceiling, not a measurement fault, not an implementation gap in the tested mechanism.

---

## 5. Counters

**Re-derive brake (R1–R3): does NOT fire.** MECH-457 has **0** prior `substrate_ceiling` autopsies (24 targets across 14 files; category distribution: competence_implementation_gap ×15, measurement_test_design_defect ×4, standard ×3, substrate_starved_precondition_unmet ×1). This is a GOV-FANOUT-1 sufficiency-dependency search, not a ceiling loop. The confirmed follow-on (H-retention-critic) tests a different mechanism (value estimator) and is brake-exempt regardless.

**Granularity-debt recurrence trigger: does NOT fire (as a new routing).** Alignment distribution over the cluster: intact=12, strengthened=4, unclear=2, unstamped=2, **weakened=2**, untested=1. The two `weakened` targets (789 retention-auxiliary-decay; 742 sufficiency-refuted) are consistent-*sufficiency* refutations (MECH-457 necessary-but-not-sufficient), not structurally-distinct falsifications of one coarse claim. Critically, a `/claim-synthesis` **proposal already exists** — `claim_synthesis_MECH-457_2026-07-22.md` (awaiting per-child user approval) — so the granularity handoff was **not** dropped. No new claim-synthesis routing.

**CIRCLING context (GOV-FROZEN-1).** `competence_floor` is flagged `convergence_class: CIRCLING` (families_fresh empty). H-consummation-binding's axis `intrinsic-architecture` = **constitution** family, the same axis as the already-eliminated H-approach-primitive — so this leg was arguably a circling leg. With it eliminated, the retention sub-portfolio stands at **3 of 4 named mechanisms resolved**:

| Retention leg | axis / family | state | run |
|---|---|---|---|
| H-retention-auxiliary-decay | learning-signal / constitution | eliminated (weakens) | V3-EXQ-789 |
| H-consummation-binding | intrinsic-architecture / constitution | **eliminated (this autopsy)** | V3-EXQ-821 |
| H-retention-consolidation | policy / process | alive (inconclusive) | V3-EXQ-792 |
| H-retention-critic | algorithm / process | **alive, un-run** | — |

The remaining discrimination (critic value-estimator vs consolidation) is already pre-registered, so **no new `fanout_recommendation`** is emitted.

---

## 6. Learning extracted

1. **H-consummation-binding ELIMINATED**: the extinguish-and-hand-off binding is not the retention mechanism — BC-installed competence erodes identically with and without extinction (margin 0.0).
2. **781's "approach without consummation" replicates even in the extinguishing arm** (drive earned ~0.8 / forage 0.0) → the deficit is *upstream* of the consummatory act. The RL objective out-competes the BC-installed forage/CONSUME policy regardless of drive extinction.
3. **The retention question converges** on H-retention-critic (flat value estimator), corroborated by 780 (raw_view 20.933→11.667) and 782 (std(V)/std(G)=0.041, separation 0.016).
4. Diagnostic value confirmed: a clean pre-registered null narrowing the frozen hypothesis space by one constitution-family leg without touching MECH-457's status.

---

## 7. Routing (user-confirmed 2026-07-25)

- **Adjudication:** confirm as diagnostic null. `H-consummation-binding → eliminated`; MECH-457 `non_contributory` / unaffected, stays candidate·v3_pending; `epistemic_category = standard`.
- **Ledger (Step 9b Mode B):** resolve H-consummation-binding under `competence_floor` (resolving_runs [V3-EXQ-821], resolved_utc 2026-07-25T22:22:52Z). Pure resolve of an already-pre-registered leg; `initial_frozen_count` unchanged (16).
- **Routing:** `governance` — the diagnostic result flows to the next `/governance` walk via the ledger. **No substrate build** (brake=0). **No same-claim re-queue** of consummation-binding.
- **Follow-on (chip):** `/queue-experiment` **H-retention-critic (leg 5)** — value-estimator retention probe (flat / distributional critic, `mech457_distributional_critic` node) in the retention framing. Convergent target with 780/782 support; a different mechanism → brake-exempt; not a re-open of the eliminated consummatory/constitution axis.

## 8. Draft `evidence_quality_note` (governance writes; this skill does not touch claims.yaml)

> V3-EXQ-821 (H-consummation-binding, GOV-FANOUT-1 retention leg 4, DIAGNOSTIC, non_contributory): the consummatory-act binding (approach_extinguishes_on_contact hand-off to a distinct CONSUME) is NOT the retention mechanism. BC-installed foraging competence (post-BC 4.3–5.7 > 1.0 floor on both arms) eroded to retained_fraction 0.0 on all 3 seeds in BOTH the extinguishing treatment and the non-extinguishing control (arm margin 0.0 < 0.15 floor); neither arm's trajectory peak re-cleared the install floor. Consummatory env solvable (anchors local_view_greedy 34.2 / greedy_oracle 42.8), criteria non-degenerate. H-consummation-binding ELIMINATED; MECH-457 neither supported nor weakened, stays candidate/v3_pending. Converges with 780/782 on H-retention-critic (flat value estimator) as the leading remaining retention candidate.
