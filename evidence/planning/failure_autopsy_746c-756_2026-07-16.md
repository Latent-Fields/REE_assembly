# Failure Autopsy — V3-EXQ-746c (INV-089) + V3-EXQ-756 (MECH-457)

- **Generated (UTC):** 2026-07-16T05:22:38Z
- **Scope:** two independent single-target autopsies bundled (not a cluster — different claims, different failure shapes)
- **Status:** confirmed (interactive gate answered)
- **Regenerated `pending_review.md` first** (3 FAIL; 746b already autopsied 2026-07-15 and is out of scope here)

---

## Target A — V3-EXQ-746c · INV-089 (the load-bearing target)

- **Run:** `v3_exq_746c_inv089_harm_eval_z_harm_bound_target_corrected_20260715T151705Z_v3`
- **Queue:** V3-EXQ-746c · **extends** 743 / supersedes-in-lineage 746b · **claim:** INV-089 `harm_evaluator_bounded_by_z_harm_differentiation` (emergent invariant, **provisional**)
- **Manifest outcome:** FAIL, `non_degenerate=True`, self-routed `evidence_direction=weakens`
- **Machine:** ree-worker-1 (linux-x86_64-py3.10), 418 s · **substrate_hash:** `4327aab4…` (recording core complete; `validate_recording` OK — **not** a recording-debt case)
- **Adjudicated:** **non_contributory** (override of the self-routed weakens) → **/claim-synthesis**

### Lineage

| Run | Preconditions | Outcome | Mode |
|---|---|---|---|
| 743 | met | PASS (positive control) | promoted INV-089 candidate→provisional 2026-07-12 |
| 746 | unmet | FAIL, superseded | DV starved (undecodable single-cell target, un-clipped head blow-up) |
| 746a | met | FAIL, **weakens** | DV measurement artifact (unregularised head, R² −26…−166) — now "measurement-suspect" per 746b autopsy |
| 746b | unmet | FAIL, non_contributory | **IV starved** (`PC_iv_moved=False`); DV-estimator fix validated at maturity |
| **746c** | **met (all 4)** | **FAIL, `non_degenerate=True`** | **first VALID bound test — fails C1/C2/C3 in a NON-BINDING regime** |

### Facts (no interpretation)

746c fixed both 746b defects: corrected the primary target to `prox` (SD-010 harm-proximity label) and **decoupled the IV/DV data budgets** (disjoint pools). All four preconditions met (`PC_iv_moved`, `PC_dv_decodable`, `PC_target_var`, `PC_dv_estimator_ok`), `preconditions_met=True`, `non_degenerate=True`. Primary target `prox`, 8 seeds, onset {0,1,4,12,30}:

| Quantity | Value | Read |
|---|---|---|
| `mean_iv_mature` (z_harm ridge-decode of prox at maturity) | **0.872** | prox already highly decodable |
| `mean_iv_delta` (onset-max − onset-min, full pool) | **+0.054** | IV moves, but a *small* range |
| `mean_iv_rho` (Spearman onset,IV) | **+0.26** | per-seed −0.8…+1.0 — noisy |
| `mean_dv_mature` (fresh harm_eval MLP R² for prox) | **0.891** | harm-eval flat-high |
| `mean_dv_delta` | **−0.004** | DV does not rise with onset |
| `mean_dv_rho` | **−0.11** | → C1 FAIL (threshold 0.80) |
| `mean_couple_rho` (IV↔DV rank coupling) | **0.675** | per-seed [1.0,0.9,0.4,−0.1,0.7,0.9,1.0,0.6] → C2 FAIL (threshold 0.80) |

**Failed criteria = C1 (dv monotone) / C2 (bound coupling) / C3 (dv reliable)** — discrimination criteria, in the *met-precondition* branch, so the script self-routes `weakens`.

### Biological-reference triage — the core move

INV-089 is a **bound / ceiling** (lit_conf 0.793: Bastuji2016 parallel nociceptive routing; Verriotis-Fitzgerald2016 distinct nociceptive maturation; Beggs2015 postnatal separation). A ceiling says `harm_eval ≤ f(z_harm differentiation)`. It predicts the DV **tracks** the IV **only in the binding regime** — i.e. when differentiation is low enough to *limit* evaluation. Here prox z_harm differentiation is **already ~0.82 at onset 0** and grows only to ~0.87: **non-binding at every tested onset.** In a non-binding regime a ceiling predicts DV = flat-high and decoupled from small IV fluctuations — **exactly what 746c observed** (DV mature ~0.89; couple_rho 0.675 with 6/8 seeds strongly positive is, if anything, weak *positive* evidence).

This is **not a substrate ceiling** and **not a recording gap**. It is a **test-in-wrong-regime / wrong-instrument** problem, biology-supported (the bound is real and simply not binding here).

### The wrong-instrument mechanism (why weakens is a misclassification)

The `PC_iv_moved` gate only checks `mean_iv_delta > 0 ∧ mean_iv_rho > 0` — it does **not** verify the IV enters a *binding* (low-differentiation) regime, nor a minimum dynamic range. The script operationalizes the bound as a **monotone driver** (`couple_rho ≥ 0.80`). A met-precondition C1/C2 FAIL is a trustworthy weakens of a **driver** reading (harm_eval *rises with* differentiation) but **not** of a **ceiling** reading (harm_eval *cannot exceed* differentiation). INV-089's text asserts the ceiling ("strictly bounded by… Productive harm-evaluator training cannot precede sufficient z_harm differentiation"); the 746 lineage keeps testing the *driver*.

Across 746a/b/c, **no available harm target has a binding maturation gradient in this substrate**: `dens` = small-sample underfitting artifact (washes out at adequate n); realized-harm `Y` = flat; `prox` = already-high at onset 0. So the driver test can never enter the regime where the bound is expressible with the current curriculum.

### Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (untested) | bound could not express itself in a non-binding regime; no claim pressure either way |
| Biological reference | clear | ceiling is lit-supported (0.793) and simply non-binding here; no biology/formal-import divergence |
| Prerequisites / substrate | present | SD-010 HarmEncoder + harm_eval_z_harm IMPLEMENTED |
| Implementation (DV estimator) | complete | 746b DV-estimator fix retained + validated (dv_mature 0.89) |
| Environment / curriculum | **inadequate** | maturation curriculum never drives harm-target z_harm differentiation into the binding regime |
| Measurement (regime) | **inadequate** | `PC_iv_moved` does not gate on a binding regime; test measures a driver, not a ceiling |
| Integration | n/a | single-stream measurement |
| Scale / capacity | adequate | not a data-volume problem |

**Node classification:** `complex (probe-gated) / mystery (known data)`. We already **have** the data (746a/b/c) showing no harm target has a binding gradient here — the frame ("test the bound as a monotone driver") is the thing that is wrong. More same-shape runs won't settle it → **reframe**, don't gather.

### Recurrence / re-derive brake / granularity-debt trigger

- **4th autopsy circling INV-089** (742-746a, 746b, 746c). This is the **2nd** with a non_contributory-family reading (746b = 1st).
- **Re-derive brake FIRES** (threshold 2). A naive same-regime 746-letter is **REFUSED** — re-testing the driver reading in the same non-binding regime is exactly the loop the brake exists to stop.
- **Granularity-debt trigger FIRES (`fires=true`).** The 746b autopsy set it false ("measurement-instrument iterations of one bound test"). 746c changes that: a *valid* test now fails for a **claim-semantics** reason (ceiling vs driver conflation), not another measurement bug. That is granularity debt surfacing → route to **/claim-synthesis** (not implement-substrate). The user confirmed this route at the gate.

### Learning extracted

1. **INV-089 conflates two claims:** a **ceiling** (`harm_eval ≤ f(differentiation)`) and a **growth-coupling / driver** (`harm_eval rises with differentiation during maturation`). The 746 lineage tests the driver; the driver is unfalsifiable whenever differentiation is non-binding.
2. **The substrate has no harm target with a binding maturation gradient** — dens (artifact), Y (flat), prox (already-high). Any future *driver* test needs a curriculum that starts harm-target z_harm differentiation genuinely low; that is the substrate fallback if /claim-synthesis keeps the driver sub-claim.
3. **746c is a clean non_contributory, not a weakens** — surface it as such; do not let a well-built experiment's self-route pressure a lit-supported provisional invariant.

### Routing (user-confirmed at gate)

- **746c → non_contributory** (override the self-routed weakens; no weight on INV-089's bound).
- **INV-089 → /claim-synthesis** — split the ceiling sub-claim from the growth-coupling/driver sub-claim (proposal-first, lit-grounded). Re-derive brake fired → **refuse** a naive same-regime 746-letter. If the split retains a driver sub-claim, the substrate fallback is a binding-regime maturation curriculum (a *new* substrate_queue entry at that point — not created here).
- **746a re-read (user-added):** recommend governance **re-read the still-active 746a weakens** in light of 746c. 746a is already flagged "measurement-suspect" (746b autopsy); 746c now shows the *driver* test cannot validly run in the available regime, which means the current claim note's "the 'strictly bounded by' reading is now actively pressured" language over-states a driver-test result. Governance should re-weigh whether 746a's weakens should stay active or be reclassified alongside the ceiling/driver split. **Analysis-only — governance decides.**
- **NARROW-SUPPORTS WARNING (`narrow_supports_flag=true`):** with 746c set aside and 746a measurement-suspect, INV-089's only undisturbed support is **743's single-pathway decodability positive control**. INV-089 must **not** advance toward stable until the ceiling/driver split lands and a valid ceiling-form (or binding-regime driver) test exists. Stays provisional.

### Draft `evidence_quality_note` for governance

**On the 746c manifest (bound-test leg — inactive / non-weighting):**
> V3-EXQ-746c FAIL, self-routed `weakens` but **ADJUDICATED non_contributory** (`failure_autopsy_746c-756_2026-07-16`). First VALID met-precondition bound test (all 4 PC met, `non_degenerate=True`) after the 746/746a/746b measurement fixes. It fails C1/C2/C3, but in a **non-binding regime**: primary target `prox` has z_harm differentiation already ~0.82 at onset 0 rising only to ~0.87 (IV delta +0.054, rho +0.26 noisy), so differentiation is never the binding constraint at any tested onset. A ceiling bound predicts harm_eval flat-high and decoupled from small IV wiggles in the non-binding regime — exactly observed (DV mature ~0.89, couple_rho 0.675, 6/8 seeds strongly positive). `PC_iv_moved` (delta>0 ∧ rho>0) does not verify a binding regime; the test operationalizes the bound as a monotone **driver** (couple≥0.80), a trustworthy weakens of the driver reading but NOT of the ceiling reading INV-089 asserts. **No weight on INV-089's bound.** Root: no available harm target has a binding maturation gradient in this substrate (dens=small-sample artifact, realized-harm Y=flat, prox=already-high). Route: /claim-synthesis to split 'bounded by' (ceiling) from 'grows with' (driver). Re-derive brake fired (2nd non_contributory on INV-089); a naive same-regime 746-letter is REFUSED.

**Appended to INV-089 claim context (narrow-supports + 746a re-read):**
> 2026-07-16 (V3-EXQ-746c autopsy — `failure_autopsy_746c-756_2026-07-16`): the first VALID met-precondition bound test does **not** weaken INV-089 — it ran in a non-binding regime (prox z_harm differentiation already ~0.82+ at onset 0, so the ceiling is never the binding constraint) and its flat-high decoupled harm_eval is CONSISTENT with a ceiling bound. Adjudicated **non_contributory**, not weakens. This surfaces **granularity debt**: INV-089 conflates 'bounded by z_harm differentiation' (ceiling) with 'harm_eval grows with differentiation during maturation' (driver); the 746 lineage (4 autopsies) keeps testing the driver and keeps hitting the non-binding regime. Routed to **/claim-synthesis** to split the ceiling and driver sub-claims. **746a re-read:** the still-active 746a weakens (already 'measurement-suspect' per the 746b autopsy) should be re-weighed — 746c shows the driver test cannot validly run in the available regime, so the prior note's 'the strictly-bounded reading is now actively pressured' over-states a driver-test result; governance to decide whether 746a stays active or reclassifies with the split. **NARROW-SUPPORTS:** with 746c set aside and 746a measurement-suspect, INV-089's only undisturbed support is 743's single-pathway decodability positive control; it must NOT advance toward stable until the split lands and a valid ceiling-form (or binding-regime driver) test exists. Stays provisional.

---

## Target B — V3-EXQ-756 · MECH-457 (diagnostic, non-scoring)

- **Run:** `v3_exq_756_mech457_hcredit_x_hreturn_pair_20260715T170212Z_v3`
- **Queue:** V3-EXQ-756 · **claim:** MECH-457 (candidate / v3_pending) · also bears on INV-088
- **Manifest outcome:** FAIL, `evidence_direction=unknown`, `experiment_purpose=diagnostic`, `non_degenerate=True`, `interpretation_label=pair_subfloor_does_not_clear_floor`
- **Machine:** ree-worker-3 (linux-x86_64-py3.10), 53871 s · **substrate_hash:** `dd3db615…`
- **Adjudicated:** non_contributory / `competence_implementation_gap` → **implement-substrate (amend)**

### Facts

The **H-credit × H-return pair** (additivity cell of the GOV-FANOUT-1 portfolio):

| Arm | z_world forage | raw forage | supra-floor? |
|---|---|---|---|
| pair | **0.20** | **0.32** | no (0/3 seeds) |
| H-credit | 0.23 | 0.33 | no |
| H-return | 0.25 | 0.30 | no |
| sparse baseline | 0.35 | 0.38 | no |

- `pair_gain_over_best_single`: **−0.05 (z_world) / −0.017 (raw)** → `any_rep_pair_additive=false`. The pair is **below even the sparse baseline** — combining the two mechanisms *slightly degrades*.
- Readiness **met** (local-view greedy 48.05, oracle 57.2 vs 1.0 floor — env solvable from the local view). `criteria_non_degenerate` all true.

### Read (continuation of a settled wall)

This closes the last leg of the GOV-FANOUT-1 combination-aware discrimination. Per the 752-754 and 755 autopsies, **no single mechanism** (backward credit sweep / Go-Explore archive-return / AMIGo goal-frontier / critic-utility explore-exploit gate) clears the 1.0 competence floor; only 751's unsupervised RND explorer cleared it (5.22, ~11% of the 48 local-view ceiling). 756 adds: **no pairwise combination** of the two most-promising mechanisms clears the floor or shows super-additivity either. The bottleneck is not "the right exploration mechanism (or combination) has not been found" — it is a **missing competence-bootstrap primitive**.

### Four-layer diagnosis (abbreviated — precedented)

Claim alignment intact (diagnostic, MECH-457 stays candidate/v3_pending); implementation = **competence_implementation_gap** (the action-learning stack collapses to sub-sparse-baseline despite a solvable env); environment adequate (readiness met); measurement adequate. Node: `complicated (buildable)` — the fix is the named `mech457_competence_bootstrap_explorer` build, no open question → implement-substrate.

### Routing (user-confirmed)

- **756 → implement-substrate, `amend`** the existing `mech457_competence_bootstrap_explorer` substrate_queue entry (`pending_implementation`, priority 1, unblocks MECH-457 + INV-088) with 756's non-additivity failure record.
- **Re-derive brake:** continues to fire (already fired at 752-754 / 755). A further same-claim MECH-457 explorer-mechanism test is refused until the bootstrap substrate is built.
- MECH-457 stays candidate/v3_pending; INV-088 candidate/pending_substrate_reconfirmation. Diagnostic → **no governance scoring weight** regardless.

### Draft `evidence_quality_note` (756 manifest — diagnostic, non-scoring)

> V3-EXQ-756 FAIL (diagnostic, non-scoring). H-credit × H-return pair forages 0.20 z_world / 0.32 raw — sub-floor, below even the sparse baseline (0.35/0.38); `pair_gain_over_best_single` −0.05/−0.017, no super-additivity (`any_rep_pair_additive=false`). Readiness met (local-view greedy 48.05, oracle 57.2). Closes the GOV-FANOUT-1 combination-aware discrimination: no single mechanism (752-755) and no pairwise combination of the two most-promising clears the 1.0 competence floor. `competence_implementation_gap`; route implement-substrate (amend `mech457_competence_bootstrap_explorer`). MECH-457 stays candidate/v3_pending; INV-088 candidate/pending_substrate_reconfirmation. Re-derive brake continues to fire.
