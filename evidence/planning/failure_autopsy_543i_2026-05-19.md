# Failure Autopsy — V3-EXQ-543i (ARC-062 differential-heads falsifier)

- **Generated (UTC):** 2026-05-19T07:06:52Z
- **Scope:** cluster (543f -> 543g -> 543h -> **543i**; extended family 433e/433f, 522, 523/523a/523b)
- **Status:** confirmed (interactive gate, user-confirmed 2026-05-19)
- **Targets:** `v3_exq_543i_arc062_differential_heads_falsifier_20260518T063711Z_v3` (branch c) and `..._20260518T191052Z_v3` (branch e); queue_id V3-EXQ-543i; claims ARC-062, MECH-309, INV-074, MECH-334
- **Not a crash.** Both runs ran to completion with `outcome: FAIL`. Autopsy, not `/diagnose-errors`.

## 1. Facts (no interpretation)

Two byte-identical 543i runs (12-arm pruned design; only varied factor across matched
diff-OFF/diff-ON gated pairs is `use_differential_heads`; P1 outcome-coupled REINFORCE
loss byte-identical across all arms) produced **opposite basins**:

| Run | `diff_off_reproduced_collapse` | `diff_on_escape` | self-branch | manifest `evidence_direction` | baseline reef_fraction |
|---|---|---|---|---|---|
| 20260518T063711Z | **false** — diff-OFF gated arms 0/3 inert | true — diff-ON arms 0/3 inert | (c) | `non_contributory` ×4 | ARM_0 ≈ 0.278 |
| 20260518T191052Z | **true** — diff-OFF gated arms 3/3 inert | **false** — diff-ON arms 3/3 inert | (e) | mixed: ARC-062 **weakens**, MECH-309 **supports**, INV-074/MECH-334 non_c | ARM_0 ≈ 0.692 |

In 06:37Z *nothing* collapsed (the diff-OFF controls that "MUST reproduce the
cross-machine inert collapse" did not). In 19:10Z *everything* collapsed, including the
differential-head arms whose `delta_hat` candidate-axis L2 is pinned to
`differential_bias_scale=0.1` (designed to make `delta==0` a structural
non-equilibrium). `n_inert_gating_seeds = 3` on every gated arm (2,3,6,7,8,9,10,11) in
19:10Z; `= 0` on every gated arm in 06:37Z. Both manifests are
`experiment_purpose: "evidence"` — the 19:10Z per-claim directions weigh into governance
as recorded.

Failed criterion: **discrimination** — and, more diagnostically, the negative-control /
collapse baseline (`diff_off_reproduced_collapse`) is itself **run-nondeterministic**
(present 19:10Z, absent 06:37Z under identical code).

Script interpretation grid (canonical, lines 100-117): (a) collapse + escape + c2c3 ->
ARC-062 supports / MECH-309 weakens; (e) collapse + NOT escape -> MECH-309 strong /
ARC-062 weakens, INV-074/MECH-334 non_c; (c) NOT collapse -> all non_contributory
(substrate/seed drift). 06:37Z = (c); 19:10Z = (e).

## 2. Claim-layer mapping

- **ARC-062** (architectural_commitment, candidate, v3_pending; depends MECH-309/SD-054/MECH-269/SD-029): the weak-reading rule-apprehension slot. 543i is its falsifier. The claim **could not express itself**: the basin swing (all-escape vs all-collapse, baseline reef 0.28 vs 0.69) dominates the `use_differential_heads` effect; 19:10Z "weakens" is a single-basin landing, not attributable to the manipulation.
- **MECH-309** (mechanism_hypothesis, candidate, v3_pending): monomodal collapse is the equilibrium without a rule-apprehender; ARC-062 is its falsifying condition. 19:10Z "supports (STRONG)" relies on the collapse baseline as ground truth — but that baseline vanished 12 h earlier (06:37Z). A **narrow / single-basin** support, exactly the illusory-conflict-resolution risk.
- **INV-074** (invariant, `invariant_type: universal`, lit_conf 0.82 — Fagiolini & Hensch, BCM/Clothiaux) and **MECH-334** (mechanism_hypothesis, lit_conf 0.78 — Pizzorusso PNN/ChABC, Morishita Lynx1): crystallization froze a collapsed / basin-dependent policy, so the closure mechanism was never exercised. **Untested, not weakened.** An implementation/substrate gap must not demote a universal invariant.

## 3. Biological-reference triage

Established by the 543h autopsy and unchanged: closest mechanisms are the PNN/Lynx1/NgR1
critical-period three-brake (MECH-334) and PFC-like contextual policy arbitration
(ARC-062/MECH-309). **Not a formal-definition import.** Biology lit is present
(`targeted_review` anchors on the claims), and there is **no biology divergence**. The
failure matches a missing-prerequisite / unstable-substrate signature (a brake with a
non-differentiated policy to lock; an arbitration layer whose modal split is not a strong
attractor), not claim falsification and not a formal-import divergence. `/lit-pull` is
**not** the route.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | could-not-express | basin swing > manipulation effect; 19:10Z "weakens" is one basin of a bistable pair |
| Biological reference | clear | PNN/Lynx1/NgR1 + PFC arbitration; lit present; no divergence; missing-prerequisite shape |
| Prerequisites | missing | strong differentiation attractor (MECH-333/INV-074 functional GatedPolicy) absent |
| Implementation | partial | `use_differential_heads` delta_hat norm-pin is the symbol; does not stabilise basin selection |
| Environment | not the driver | same SD-054 bipartite env where 543g activated |
| Measurement | misleading + gap | per-claim direction emitted from a single basin landing; **manifests record no hostname** for a bistability under cross-machine investigation |
| Integration | unstable | basin selection RNG/init + cross-run + cross-machine nondeterministic |
| Scale | possibly insufficient | P1=60 ep without head_div force; unknown |

Recommended `epistemic_category`: **substrate_ceiling** (unstable-activation variant; cluster continuity with 543h).

## 5. Cluster pattern

| Experiment | Claim(s) | Negative-control / collapse baseline | Discrimination | Read |
|---|---|---|---|---|
| 543f | ARC-062/MECH-309 | inert | fails | substrate-ceiling (autopsied) |
| 543g | ARC-062/MECH-309 | ACTIVE host-A / INERT cloud-3+cloud-4 | 1/3 minority-basin "weakens" | cross-machine bistability |
| 543h | ARC-062/MECH-309/INV-074/MECH-334 | inert all gated arms | fails; sign-only repro misfired grid | substrate-ceiling, non_c (autopsied) |
| **543i 06:37Z** | all 4 | **absent** (diff-OFF 0/3 inert) | branch (c) | basin A (all-escape) |
| **543i 19:10Z** | all 4 | present (diff-OFF 3/3 inert) | branch (e), diff-ON 3/3 inert | basin B (all-collapse) |

**Not N independent bugs — one structural property.** The gated/rule-apprehension
substrate has the asserted wiring but does not reliably carry differentiated policy
behaviour under a trained policy; basin selection (ACTIVE/differentiated vs INERT/
collapsed) is governed by uncontrolled nondeterminism (init RNG + cross-run + cross-
machine), not by `use_differential_heads`. 543i upgrades the 543h evidence from
**cross-machine** to **cross-run on a single host**: the structural fix under test did
not convert differentiation into a strong attractor. Continuous with MECH-309's
documented V_s-monostrategy substrate-ceiling.

## 6. Learning extracted

1. The `use_differential_heads` reparameterization (base ± delta_hat, candidate-axis L2 pinned to 0.1) is **insufficient** to make head differentiation a strong attractor under outcome-coupled REINFORCE — differentiation remains basin-nondeterministic.
2. Bistability is now demonstrated **cross-run on one host**, not merely cross-machine — a >=2-machine confirmation (543j) is necessary but **not sufficient**; basin-determinism must be characterised over K repeated identical runs.
3. Per-claim `evidence_direction` must not be emitted from a single run when the script's own documented failure mode is run-level basin nondeterminism. A determinism guard (basin stability across repeated runs) must gate any directional reading.
4. Manifests do not record the executing hostname — a measurement gap that blocks attributing basin to machine in exactly the cluster where it matters.
5. MECH-309 "support" derived from a collapse baseline that is itself non-deterministic is a narrow/single-basin signal, not confirmation (illusory-conflict-resolution guard).

## 7. Repair pathway (routing) — user-confirmed

**Routing: `/implement-substrate`**, extending the existing 543h `substrate_queue` entry
("GatedPolicy head-differentiation under outcome-coupled REINFORCE"):

- Mark the 543h entry's fix attempt (`use_differential_heads`) **insufficient** (543i evidence).
- Update `threshold_a_working_impl_must_exceed`: differentiation must be a strong
  attractor — `n_inert_gating_seeds == 0` on all gated arms reproducibly across **K (>=3)
  repeated same-machine runs** AND **>=2 machines**; behavioural-divergence probe
  `mean_tv_distance >= 0.05` sustained at end of P1.
- Secondary (measurement / test-design, fold into the next falsifier or 543j successor):
  manifests must record `hostname`; no per-claim `evidence_direction` until basin
  stability is established across repeated runs.
- **543j caveat:** the in-flight V3-EXQ-543j (cross-machine confirmation, claimed by
  ree-cloud-4) inherits the single-basin attribution flaw. Its branch result must be
  interpreted **under this autopsy** — a 543j branch-e does NOT confirm "ARC-062 weakens",
  a branch-a does NOT confirm "supports"; only a basin-determinism characterisation
  resolves the chain. Do not block 543j; do not let its raw branch weigh on governance.

**Not** governance-demotion: ARC-062 was not tested fairly. **Not** `/lit-pull`: biology
present, no divergence. **Not** `/diagnose-errors`: ran to completion.

## 8. Draft `evidence_quality_note` (governance to write — NOT written here)

**ARC-062 / MECH-309 (both 543i runs):**
> V3-EXQ-543i non_contributory all claims, both runs (failure autopsy 2026-05-19,
> user-confirmed). Two byte-identical runs landed opposite basins: 20260518T063711Z
> branch (c) — diff-OFF gated arms 0/3 inert (no collapse baseline), all escape, baseline
> reef 0.28; 20260518T191052Z branch (e) — diff-OFF 3/3 inert, diff-ON 3/3 inert, baseline
> reef 0.69. Basin selection is RNG/init + cross-run + cross-machine nondeterministic
> (continuous with 543g ACTIVE host-A / INERT cloud-3+cloud-4 and the 543h substrate-
> ceiling autopsy); it is NOT controlled by use_differential_heads, so ARC-062 could not
> express itself and the 19:10Z "weakens" is a single-basin artifact. MECH-309's 19:10Z
> "supports" rests on a collapse baseline that is itself non-deterministic — recorded as a
> flagged narrow/single-basin signal, not confirmation (narrow_supports_flag).
> ARC-062/MECH-309 have zero reliable contributory trained-policy evidence;
> pending_retest_after_substrate. Do NOT honor the 19:10Z per-claim weakens/supports in
> confidence or conflict scoring.

**INV-074 / MECH-334 (both 543i runs):**
> V3-EXQ-543i does NOT weaken INV-074 or MECH-334 (failure autopsy 2026-05-19). The
> crystallization closure froze a collapsed / basin-dependent GatedPolicy; the
> PNN/Lynx1/NgR1-analog mechanism was never exercised. Missing prerequisite (functional
> differentiated GatedPolicy = MECH-333/INV-074), not claim pressure. INV-074 is a
> universal invariant with independent biological support (lit_conf 0.82) and must not be
> demoted by a substrate-instability FAIL. evidence_direction non_contributory;
> pending_retest_after_substrate.

**Supersession / indexer:**
> 543i carries `supersedes: V3-EXQ-543h`. Both 543i runs are non_contributory (basin
> nondeterminism); the supersession is bookkeeping continuity only — 543i provides no
> contributory evidence that displaces any prior contributory result. The 543g/543h
> non_contributory dispositions stand.

## 9. Routing decision (confirmed at interactive gate)

- Evidence: **non_contributory for ARC-062, MECH-309, INV-074, MECH-334 on BOTH 543i runs**; `pending_retest_after_substrate: true`; `narrow_supports_flag: true` (MECH-309 single-basin).
- `epistemic_category`: **substrate_ceiling**.
- Routing: **`/implement-substrate`** — extend the 543h substrate_queue entry (use_differential_heads insufficient; add basin-determinism + cross-run threshold; manifest hostname + determinism-gate measurement fixes; 543j-interpretation caveat).
- `/governance` applies the writes; this skill does not edit claims.yaml, manifests, review_tracker, or substrate_queue.
