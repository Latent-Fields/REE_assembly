# Thought intake -- Convergence Signal: Formal Notes

**Date processed:** 2026-09-15
**Raw thought:** `docs/thoughts/2026-09-09_convergence_signal_formal_notes.md` (478 lines)
**Session:** thought-pipeline-20260915
**Parent:** `docs/thoughts/2026-09-09_convergence_as_general_computational_signal.md`
**Family HUB intake (full novelty table lives there):**
`thought_intake_2026-09-09_convergence_as_general_computational_signal.md`

**Character of this file.** It is exploratory mathematics and measurement notes, self-described as "no
architectural commitment" and "define candidate measurements, not choose one prematurely". Almost
nothing in it is claim-shaped. Its value to this intake is (a) it supplies the precise wording for the
two bindings that keep MECH-558 honest, and (b) it is the design source for assays 001-006, so the
question the brief asks -- does it propose measurements something already computes? -- has an unusually
exact answer.

## 1. Verbatim core proposal

> A usable quantity must separate at least: **preference strength**, **reliability**, **relevance**,
> **dependence**, **alignment**, **diversity**.

> `P` answers: what does the weighted coalition currently favour? whereas convergence should answer
> something like: how independently and robustly is that direction supported?

> The attractive idea is not one magic formula. The likely useful object is a small **diagnostic
> bundle**.

## 2. Novelty table (short -- see hub for the family-wide table)

| Thread unique to this file | Existing REE coverage | Verdict |
|---|---|---|
| Six quantities that must be kept separate (s.1) | -- | The decomposition MECH-558 registers as "a topology, not a scalar" |
| `P` (aggregate pull) is not `C` (convergence); a single high-weight evaluator makes `P` large while every other evaluator disagrees (s.3) | **MECH-439** measures exactly this in REE: F holds 88-89% of committed-selection variance; **MECH-463** names global scalar routes as variance amplifiers | **Already owned as a measured REE fact**; the general statement goes into MECH-558 |
| `C_dir`, and its stated limitation that it counts clones as independent (s.4) | none | **Instrument, not built** |
| `C_pair` and the coalition graph (node = evaluator, edge = agreement, node weight = reliability) (s.5) | **SD-091 / MECH-481** coalition/topology control -- a temporary functional interaction graph over subsystems | **Adjacent vocabulary, different object**: SD-091's graph is a RECRUITMENT topology the control plane emits; this is an AGREEMENT topology read off evaluator outputs. Cross-referenced in MECH-558's depends_on |
| Error covariance `Sigma_ij`, inverse-covariance weighting, dependence-adjusted `N_eff`, causal ancestry annotation (s.6) | none | **NEW** -> MECH-558 ("preserve topology; a single `N_eff` is not enough") |
| The sublinear term: ten weak independent votes should not overwhelm one protected veto (s.7, s.12) | **MECH-125** veto-level error signals; **MECH-449** eligibility constitution | **Already owned** -- restated as a binding inside MECH-558 and clause (iv) of INV-108 |
| Convergence vs confidence: matched aggregate confidence, different SUPPORT TOPOLOGY, and robustness as the discriminating consequence (s.8) | **MECH-059** keeps confidence distinct from residual error but says nothing about support topology | **NEW** -> MECH-558's non-tautology binding |
| Cross-model epistemic leverage `L(q)` and the interaction term `X(q)` (s.9) | **MECH-482** formula; **MECH-314c** learning progress | **NEW** -> MECH-559 |
| Aha metrics: `delta K` complexity, `delta E` held-out error, cross-view integration count `I` with EFFECTIVE independence, change-point `S_t`; and the explicit warning that a degenerate constant representation is maximally simple and useless (s.10) | **MECH-423** measures joint held-out gain across two views; **INV-104** guards against compression that deletes consequential distinctions | **Adjacent** -> the deferred insight-candidate claim (NOT registered 2026-09-15; see the aha intake section 5) |
| Separability of the computational insight event from the phenomenological Aha (s.10.4) | nothing | **NEW** -> the deferred insight-candidate claim (NOT registered 2026-09-15; see the aha intake section 5) binding (4) |
| Six diversity diagnostics and the explicit "do NOT maximise diversity" (s.11) | ARC-065 family; **INV-076**; **ARC-139** | **Already owned** -> the wording feeds INV-108 clause (v) |
| `Authority(a) = VetoGate(a) x F(P_a, C_a, uncertainty, ...)` (s.12) | **MECH-125**, **MECH-449** | **Already owned** |
| Dropout robustness `R_drop` as the practical proxy, and the clean reading "high convergence + low dropout robustness = apparent consensus hiding a dominant source" (s.13) | none, anywhere | **Instrument, UNBUILT** -- the highest-value unimplemented measurement in the family |
| The experimental-mathematics target (s.14): manipulate accuracy, pairwise error correlation, number of evaluators, one protected veto, context relevance, one high-reliability minority expert, distribution shift | -- | **Already executed** as assays 001-006 preregistrations |
| "a small diagnostic bundle ... the control system can then ask different questions of the same bundle" (s.15) | -- | The family's own best summary; it is the shape MECH-558 registers |

## 3. Key formulations (verbatim)

- "'Several things agree' is too vague to implement safely."
- "This is **not** the convergence signal. A single high-weight evaluator can make `P_a` large even when
  every other evaluator disagrees."
- "### Limitation -- This counts correlated clones as independent supporters. It is therefore not
  sufficient."
- "This makes disagreement topology inspectable rather than hiding it in one resultant vector."
- "Highly correlated residual errors imply duplicated evidence."
- "REE has an advantage over a biological observer: its computation graph is partly known."
- "The sublinear term matters: ten weak independent votes should not necessarily overwhelm one protected
  veto simply because ten is larger than one."
- "A valid convergence metric should add value in regimes where two candidate states have equal
  aggregate confidence but different **support topology**."
- "interesting because uncertain" versus "interesting because resolving it may reorganise several models
  at once."
- "A computational Aha candidate should not be triggered by compression alone. A degenerate constant
  representation is maximally simple and useless."
- "restructuring may occur without strong Aha; strong confidence/reward may feel Aha-like without deep
  restructuring."
- "A simple target should **not** be `maximize diversity`."
- "This directly tests whether 'agreement' reflects distributed support or one hidden monarch."
- "Action selection may care about `P` plus vetoes. Information hunger may care about disagreement and
  cross-model leverage. Closure may care about convergence plus expected value of more computation.
  Insight detection may care about sudden cross-model restructuring."

## 4. Affected existing claims

Cross-reference only; **no field of any existing claim is touched**. One observation worth surfacing
without acting on it: this file's section 8 rival ("convergence adds nothing beyond ordinary posterior
confidence") and REE's own E3 commensurability warning recorded in
`evidence/planning/convergence_signal_ree_archaeology.md` section 8 (normalising each channel by its own
variance makes equalised variance shares partly tautological) are the same methodological hazard reached
from two directions. That hazard is registered as MECH-558's non-tautology binding rather than as a
governance rule; if `/governance` prefers it as a standing admissibility rule it is closer to a
one-clause extension of **GOV-MATCHAUX-1** (matched-auxiliary-control admissibility) than to a new claim.

## 5. Candidate claims -- REGISTERED this pass

**No new claim is registered from this file alone.** Its content is distributed into claims registered
from its siblings:

- sections 1-8 -> **MECH-558** (the six-quantity decomposition, the `P` vs `C` distinction, the
  topology-beats-`N_eff` assertion, the ceiling binding, the non-tautology binding);
- section 9 -> **MECH-559** (cross-model leverage and its separation from evidence dependency);
- section 10 -> **the deferred insight-candidate claim (NOT registered 2026-09-15; see the aha intake section 5)** (the four-part aha signature and the event/phenomenology separation);
- sections 11-12 -> **INV-108** (competent non-redundant routes, not maximum diversity; veto asymmetry).

This is the correct disposition for a measurement-notes document: it earns bindings inside claims, not a
claim of its own.

## 6. Deliberately NOT registered

- **Every named formula** (`C_dir`, `C_pair`, `Sigma^-1 w`, `N_eff`, `C_ind`, `L(q)`, `X(q)`,
  `R_drop(a)`, `S_t`). Instruments. Six of them already exist as code in
  `REE_assembly/scripts/convergence_signal_synthetic_assay_00*.py`; registering a formula as a claim
  would be the over-splitting GOV-SHARPEN-1 guards against.
- **Any choice among them.** The file explicitly refuses to choose, and assays 001-006 have since shown
  the scalar candidates to be the weaker ones.
- **The experimental-mathematics target (s.14).** Executed.

## 7. Implementation-gap audit -- which proposed measurements already exist

This is the question the brief asks specifically of this file. Method: grep each proposed metric across
`REE_assembly/scripts/convergence_signal_synthetic_assay_00*.py`, `ree-v3/experiments/`,
`ree-v3/ree_core/` and `REE_assembly/evidence/experiments/`.

| Proposed measurement | Status | Where it exists (or what was searched) |
|---|---|---|
| `N_eff` effective source count (s.6.2) | **BUILT (synthetic)** | assay drivers 001, 002, 003 |
| Cluster / provenance-aware dependency topology (s.6.3, s.7) | **BUILT (synthetic)** | assays 002-006 as methods M2/M3 |
| Calibration and Brier against an exact-Bayes ceiling (s.8) | **BUILT (synthetic)** | assays 001, 002; the banked 002 manifest carries an `in_distribution_brier` block |
| Cross-model leverage `L(q)`, factorised from evidence dependency (s.9) | **BUILT (synthetic)** | assays 004, 005, 006 |
| Uncertain / soft dependency estimates (implicit in s.6) | **BUILT (synthetic)** | assay 005 (soft provenance beat hard labels, regret ratio 0.678 under harsh corruption) |
| State-conditioned dependency and impact graphs (not in this file; added by assay 006) | **BUILT (synthetic)** | assay 006 |
| `C_dir` directional alignment (s.4) | **NOT BUILT** | zero hits for cosine / directional-alignment in the assay drivers |
| `C_pair` pairwise alignment and the coalition graph (s.5) | **NOT BUILT** | zero hits; SD-091's `CoalitionController` is a different object (recruitment, not agreement) and defaults off |
| Inverse-covariance source weighting (s.6.1) | **NOT BUILT** | approximated by cluster membership in the assays; never as `Sigma^-1` |
| Dropout robustness `R_drop` (s.13) | **NOT BUILT ANYWHERE** | zero hits for dropout / leave-one-evaluator-out across all six assay drivers; the nearest thing in the whole repo is module ablation in `v3_exq_680c_mech423_superadditivity_ablation.py`, which ablates a training path, not an evaluator at decision time |
| Complexity reduction `delta K` / MDL (s.10.1) | **NOT BUILT ANYWHERE** | zero hits for `description_length` or `mdl` in `ree_core/`, `ree-v3/experiments/`, `REE_assembly/evidence/experiments/` |
| Held-out predictive preservation `delta E` (s.10.2) | **BUILT for n=2 views** | `v3_exq_680c/d/e_mech423_superadditivity_ablation.py` (world R2 + affordance R2, held-out, param- and compute-matched arms) |
| Cross-view integration count `I` with effective independence (s.10.3) | **PARTIAL, n=2, no independence correction** | same experiment family |
| Change-point magnitude `S_t` (s.10.4) | **NOT BUILT** | -- |
| Six diversity diagnostics (s.11) | **PARTIAL** | REE measures policy/behavioural diversity heavily (`first_action_entropy`, `committed_class_entropy`, participation ratio); residual-error covariance ACROSS EVALUATORS is not measured anywhere |
| `VetoGate` asymmetry (s.12) | **NOT BUILT** | MECH-125 asserts veto-level error signals; the live E3 path sums channel biases into `_modulatory_accum` with no unbuyable gate |

**Bottom line for this file:** roughly half the proposed measurement bundle was implemented and exercised
by the 2026-09-09 assays; the unimplemented half is precisely the half the aha branch and the
robustness-proxy branch need -- `R_drop`, `delta K`, `S_t`, `C_pair`.

## 8. Next steps

1. **Cheapest high-value instrument to build next:** `R_drop` (evaluator-dropout robustness) inside the
   existing assay harness. The file argues it "may also be easier to interpret than a sophisticated
   independence scalar", and it is the one measurement that directly separates "broad support" from
   "apparent consensus hiding a dominant source" -- which is the REE-native question MECH-439 already
   poses about F.
2. **Literature.** Nothing in this file is a literature claim; the DOIs supporting the bindings live in
   `evidence/planning/convergence_signal_literature_review.md` and are unverified in this pass.
3. **Version routing.** No claim is registered from this file, so no routing is owed.
