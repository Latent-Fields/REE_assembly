# Failure Autopsy — V3-EXQ-725a (converged learned-binder coherence-nonreducibility retest)

- **Generated:** 2026-07-10T06:35:17Z
- **Run:** `v3_exq_725a_coherence_nonreducibility_converged_binder_20260709T221114Z_v3`
- **Queue:** V3-EXQ-725a · **supersedes** v3_exq_725 · **machine:** ree-cloud-4
- **Purpose:** diagnostic · **claim_ids:** [] · **evidence_direction:** non_contributory (not weighted)
- **Outcome:** FAIL (load-bearing `SPEC_coherence_specific` not met: 1/6, needs 4/6)
- **Scope:** single (but read against the 641a→720→725→725a lineage; 3rd autopsy in the family)
- **bears_on (untagged):** INV-002, MECH-089, MECH-094, MECH-270, MECH-269
- **Status:** confirmed (interactive gate answered)

---

## 1. The adjudication question

Is 725a a genuine coherence-nonreducibility **NULL** on the converged learned binder, or a
**MEASUREMENT/DIVERSITY gap** (SP-CEM first-action diversity below the gating-adequacy floor →
escalate SP-CEM diversity/steps and re-run, do not read as a coherence verdict)?

**Verdict: NEITHER of the user's two literal branches — and specifically NOT the SP-CEM gap.**
It is a contributory *fair-test negative on coherence-SPECIFICITY*, plus a load-bearing lineage
result: the converged learned binder **refutes** the 720-autopsy's learned-binder-as-residual-
prerequisite hypothesis in the negative.

## 2. Facts (no interpretation)

**Load-bearing criteria (manifest `interpretation.criteria`):**
- `learned_binder_converged` — **PASS** (worst-seed loss_ema 3.266 < gate 3.535; all 6 seeds converged)
- `SPEC_coherence_specific` — **FAIL** (`n_coherence_specific=1`, `n_seed_pass=1`, gate 4/6)
- `rebinding_exercised` — **PASS** (`n_rebind_total=1676` across 6 seeds; 0 in every predecessor)

**Non-load-bearing reads:** D1 behavioural divergence 6/6; D3 c_nonreducible 5/6.
`criteria_non_degenerate`: D1, D3, SPEC, rebinding all TRUE (non-degenerate).

**The SP-CEM measurement caveat did NOT fire this run:**
- `gating_adequacy_warning: false`; `primary_seeds_low_gated: []`
- Every seed `gating_adequate: true`; `n_p1_steps_gated` 238–640 (adequacy floor 20)
- All 3 readiness preconditions MET: learned_binder_active (0.5>0), learned_binder_converged
  (upper-bound gate met), gating_denominator_adequate (238 ≥ 20)

The `review_caveat` the task flagged describes the confound *class* (the 642/719a shape) — it is a
conditional warning, and the per-run instrumentation shows the condition is **absent** here. So
"escalate SP-CEM diversity and re-run" would be re-running to repair a confound that did not occur.

**Per-seed SPEC (real vs shuffle `frac_state_div_gated`, margin 0.05):**

| seed | real | shuffle | interpretable? | specific? |
|---|---|---|---|---|
| 42 | 0.946 | 0.947 | near-ceiling (both) | no (tie) |
| 43 | 0.189 | 0.500 | yes | no (real < shuffle) |
| 44 | 1.000 | 1.000 | **saturated (both)** | no (tie) |
| 45 | 0.242 | 0.859 | yes | no (real << shuffle) |
| 46 | 1.000 | 1.000 | **saturated (both)** | no (tie) |
| 47 | 0.909 | 0.606 | yes | **yes (real > shuffle)** |

Of the 3 cleanly-interpretable (non-saturated) seeds, 2 (43, 45) are anti-specific and 1 (47) is
specific. `majority_label = C_changes_selection_specificity_unproven_route_followup` — the script
self-routes this exact label to `/failure-autopsy` to decide final close vs residual gap.

## 3. Lineage — the load-bearing signal

SPEC (coherence-specificity, seeds passing) across the family, harness held ~identical:

| Iteration | Substrate | SPEC | Rebinding | Autopsy routing |
|---|---|---|---|---|
| 641a | unbound fixed field | 1/6 | 0 (un-exercisable) | learned/bound binder next |
| **720** | **fixed-field bound** | **3/6 (peak)** | 0 | implement-substrate (learned binder = residual prereq) |
| 725 | learned binder, UNCONVERGED | 0/6 | vacuous | implement-substrate (converge the binder) |
| **725a** | **learned binder, CONVERGED + rebinding exercised** | **1/6** | **1676** | (this autopsy) |

**Reading:** the 720 autopsy hypothesised a *learned* (plastic) binder was the missing prerequisite
to clear the 4/6 gate. That prerequisite has now been built, converged, and tested — and it gives
**1/6, below the fixed-field peak of 3/6 and back at the unbound floor.** Plasticity did not lift
coherence-specificity; it regressed it (consistent with the 725 finding that a plastic coupling
injects divergence-amplifying noise that *destroys* the partial specificity a deterministic joint-
state field provided; even converged, both real and shuffle arms are driven toward saturation).
**SPEC tracks the binder architecture (3/6 fixed vs 1/6 learned), not the competence floor** — this
is why the competence-floor tie is a secondary caveat here, not the dominant cause.

## 4. Claim-layer mapping

No tagged `claim_ids` (diagnostic). The target is the **candidate Q**
`entities/selection.coherence_nonreducibility` (unregistered), shared by two OPEN intakes:
- `thought_intake_2026-04-23_binding.md`
- `thought_intake_2026-04-23_path_integral_constraints_search.md`

Both were pre-registered as **gated on the learned-binder substrate** and to be settled by this run.
The intakes' own registered falsifiers:
- "unsupported if C adds nothing beyond E" → **NOT triggered** (D3 5/6: C is non-reducible to E)
- "unsupported if removing C produces no behavioural difference" → **NOT triggered** (D1 6/6)
- "unsupported if no dynamic rebinding under perturbation" → **NOT triggered** (rebinding exercised)

So on the intakes' *literal* falsifiers C survives — but that is the weak bar (any orthogonal signal
that breaks ties passes it). The redesign correctly imposed the *stronger* specificity bar (real vs
contrast-matched shuffle), which is exactly what the registerable-novel-claim status requires, and
that is what fails. The candidate Q therefore does **not** clear the bar to register.

## 5. Biological / formal-import triage

The coherence term `C(τ)` is a **formal-physics import** (path-integral / least-action / cross-stream
phase alignment). The `path_integral` intake itself pre-registered the caution (per
`feedback_biology_before_formal_definitions`): a path-integral/least-action import is the canonical
"philosophy-right, mechanism-wrong" risk class; do not register on the strength of the analogy alone.

The closest biological reference (binding-by-synchrony / cross-region coherence gating action
selection) is **partial**: the fixed-field binder is symbol-complete/function-partial (MECH-270
ephaptic analog), and the learned binder is a faithful "trained, not fixed random field" translation
— yet the trained translation did not deliver coherence-*specific* selection. This is **not** a
missing-dependency signature (the dependency — a converged, rebinding-capable binder — is now
present and still yields the null). The operative reading is the formal-import caution vindicated:
`C(τ)` behaves as *any orthogonal tie-breaking bias*, reproduced by a contrast-matched shuffle.

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear→settle | candidate Q; test let it express itself under the fairest substrate to date; SPEC not cleared |
| Biological reference | partial | binding-by-synchrony; trained-binder translation present, still non-specific → formal-import caution operative |
| Prerequisites | present | converged binder + exercised rebinding + adequate gating all satisfied (the 720/725 residuals are cleared) |
| Implementation | complete | learned binder built, converged (loss_ema 0.65–0.80 of chance), P0→P1 discipline honoured |
| Environment | adequate (caveat) | CausalGridWorldV2 slow-drift; gating adequate (238–640 gated steps); competence-floor tie is secondary |
| Measurement | under-instrumented (secondary) | `frac_state_div` **saturates** on 3/6 seeds → SPEC unmeasurable there; NOT the flagged SP-CEM low-gating gap |
| Integration | coupled | binder ↔ selection coupled; rebinds under perturbation |
| Scale | adequate | 6 seeds, 40/25 P0/P1 episodes, converged binder |

**Recommended epistemic reading:** genuine fair-test negative on coherence-SPECIFICITY (formal-import
unsupported) — NOT `substrate_ceiling` (720's category; the substrate is now mature) and NOT
`untrained_substrate_artifact` (725's category; the binder converged). Direction stays
`non_contributory` (diagnostic, claim_ids=[]).

## 7. Learning extracted

1. **The learned-binder-as-residual-prerequisite hypothesis (720 autopsy) is REFUTED in the negative.**
   A converged, rebinding-capable learned binder gives SPEC 1/6 — below the fixed-field peak (3/6) and
   at the unbound floor. Plasticity did not lift coherence-specificity.
2. **The best coherence-specificity result in the entire lineage came from the FIXED-FIELD binder
   (720, 3/6)** — a structured deterministic joint-state field — and even that plateaued below gate.
3. **The SP-CEM measurement gap did NOT fire** (gating adequate on all seeds); the flagged confound
   class is absent, so an SP-CEM-diversity re-run is unwarranted.
4. **Residual measurement note:** `frac_state_div` saturates on 3/6 seeds; any *future different-
   mechanism* test of coherence must use a **graded / non-saturating divergence metric** so both arms
   can separate. This is a spec note for a redesign, not a mandate to re-run 725a.
5. **Rebinding-under-perturbation is now positively exercised** (1676 events; 0 in all predecessors).
   The binding intake's candidate MECH (monitor coherence and rebind when a competing configuration
   overtakes the current one in `exp(-βE)·C`) is the one salvageable positive — decoupled from the
   coherence-nonreducibility Q that closes.

## 8. Routing (confirmed at interactive gate)

**Intake disposition — settle NO-CLAIM, salvage rebinding MECH (user-selected):**
- **Settle both intakes** (`thought_intake_2026-04-23_binding.md`,
  `thought_intake_2026-04-23_path_integral_constraints_search.md`) as **RESOLVED — do NOT register**
  the candidate Q `entities/selection.coherence_nonreducibility`. Under the fairest, most-mature
  substrate (converged learned binder, exercised rebinding, adequate gating), coherence changes
  selection (D1) non-reducibly (D3) but NOT coherence-specifically (SPEC 1/6; contrast-matched
  shuffle reproduces the divergence). The formal-import caution is the operative reading.
- **Salvage** the rebinding-under-perturbation candidate MECH as a **separate `/claim-synthesis`**
  handoff (proposal-first, lit-grounded), *decoupled* from the closing coherence-nonreducibility Q.
  This is the one load-bearing positive (rebinding now exercisable + observed at the substrate).

**Re-queue gate — refuse the SP-CEM re-run only (user-selected):**
- **REFUSE** the specific "escalate SP-CEM diversity / steps and re-run" re-queue — that confound is
  absent (gating adequate), so it would repair nothing.
- A **redesigned test of a DIFFERENT coherence mechanism** (new EXQ number, different `claim_ids`,
  and a **graded non-saturating divergence metric** replacing `frac_state_div`) is **allowed** — it
  is not another letter circling the same ceiling.
- The substrate-enrichment exemption that protected 720/725 from the re-derive brake is **spent**
  (unbound → fixed → learned-unconverged → learned-converged; the terminal enrichment underperformed).
  A same-question `725b` on this substrate lineage is not sanctioned.

**Not routed:** implement-substrate on the binder (already built + converged); lit-pull (biology is
not the identified gap; the formal-import caution is already registered in the intake);
governance-demotion (no tagged claim to demote).

## 9. Draft `evidence_quality_note` (for governance — do not write from this skill)

> V3-EXQ-725a (diagnostic, claim_ids=[], non_contributory): converged learned-binder retest of the
> 641a/720/725 coherence-nonreducibility harness. Gating adequate (all 6 seeds, 238–640 gated steps;
> SP-CEM measurement gap did NOT fire — `primary_seeds_low_gated=[]`, `gating_adequacy_warning=false`).
> Load-bearing SPEC 1/6 (gate 4/6): coherence changes selection (D1 6/6) non-reducibly to E (D3 5/6)
> but NOT coherence-specifically vs a contrast-matched shuffle (F3). Lineage SPEC 641a 1/6 → 720
> fixed-field 3/6 (peak) → 725 unconverged 0/6 → 725a converged 1/6: the converged learned binder
> REFUTES the 720 learned-binder-prerequisite hypothesis in the negative and underperforms the fixed
> field. Rebinding now positively exercised (1676 events). Settles both 2026-04-23 intakes NO-CLAIM
> (candidate Q coherence_nonreducibility not registered; formal-import caution vindicated); rebinding-
> under-perturbation MECH salvaged to /claim-synthesis. Refuse SP-CEM re-run; a different-mechanism
> redesign with a non-saturating divergence metric is the only sanctioned continuation.
