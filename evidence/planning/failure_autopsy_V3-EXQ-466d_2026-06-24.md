# Failure Autopsy — V3-EXQ-466d (SD-034 satisficing residue-discharge behavioural)

- **generated_utc:** 2026-06-24T22:08:53Z
- **scope:** single
- **status:** confirmed (interactive gate, user "non_contributory + queue-experiment"; MECH-094 dropped)
- **manifest:** `REE_assembly/evidence/experiments/v3_exq_466d_sd034_satisficing_residue_discharge_behavioural_20260624T094710Z_v3.json`
- **run_id:** `v3_exq_466d_sd034_satisficing_residue_discharge_behavioural_20260624T094710Z_v3`
- **queue_id:** V3-EXQ-466d (supersedes V3-EXQ-466c)
- **claim_ids (manifest):** [SD-034, MECH-094]
- **outcome:** FAIL / self-routed `weakens` (`residual_discharge_open`) — **adjudicated non_contributory**

## 1. Facts (no interpretation)

Three seeds (42/43/44), ARM_CLOSURE_ON vs ARM_CLOSURE_OFF (same trained weights; OFF disables
`use_closure_operator` + `use_closure_env_completion_hook`). Both readiness preconditions PASSED on
3/3 seeds:

- `foraging_contact_guard` measured 1.0 ≥ 0.667
- `commitment_and_completion_engaged` measured 1.0 ≥ 0.667

Per-seed (ARM_CLOSURE_ON): n_closures = 3 / 7 / 5; **discharge_events = 0 / 0 / 0**;
**mean_residue_weight_reduction = 0.0 / 0.0 / 0.0**; n_sequence_completions = 3 / 7 / 5;
n_env_completion_hook_calls = 3 / 7 / 5; total_beta_elevated = 140 / 496 / 116.

Criteria (load-bearing all three): **C1_n_closures PASS** (closures now FORM — the 466c
absent-hook gap is closed), **C2_discharge_events FAIL** (0 < floor 1), **C3_off_no_closure_no_discharge
PASS** (OFF arm: n_closures 0, discharge 0 all seeds). Manifest asserts
`criteria_non_degenerate = {C1: true, C2: true, C3: true}` and self-routed
`route_reason = criteria_unmet_genuine_weakens`, `evidence_direction = weakens`.

**Which criterion failed:** the discrimination criterion C2 (discharge_events). C1 (absolute closure
formation) and C3 (negative control) both pass. "Negative control passes, discrimination fails" is the
substrate-ceiling *fingerprint* — but here the discrimination metric is pinned for a harness reason, not
a substrate one (see §3).

## 2. Code reconstruction — why discharge_events is 0

The discharge leg is the third part of the SD-034 five-part "done" token
(`ResidueField.discharge_domain`, claims.yaml SD-034 (c)). Trace:

1. `_eval_residue_discharge` (script lines 318–432) counts a discharge event only when the closure's
   `ClosureEvent.residue_centers_discharged >= 1` (script line 388).
2. `residue_centers_discharged` is set in `ClosureOperator._fire` (closure_operator.py:743) from
   `discharge_domain(z_world, factor, radius)` (closure_operator.py:698–706). The operator IS wired to
   the field: `ClosureOperator(..., residue=self.residue_field, ...)` (agent.py:1577) — so `self.residue`
   is **not** None and the discharge call is reached on every closure fire.
3. `ResidueField.discharge_domain` (field.py:621) **returns 0 when `self.rbf_field.active_mask.any()` is
   False** (field.py:671) — *before any closure-domain matching*.
4. Active RBF centers are added ONLY by `add_residue`, reached ONLY through `agent.update_residue()`
   (agent.py:7390 → `add_residue`, field.py:123).

**The residue field is empty for the entire run.** Neither the scaffold curriculum
(`scaffolded_sd054_onboarding.py` — zero `update_residue` calls) nor the 466d eval loop
(`_eval_residue_discharge` — sense → generate_trajectories → select_action → env.step →
notify_env_completion, no `update_residue`) ever populates it. And `agent.reset()` explicitly **"Does NOT
reset residue (invariant)"** (agent.py:2354), so the emptiness is not a per-episode wipe — the
accumulation path is simply never exercised.

Net: every closure fires (`_fire` runs, `n_closures` increments, MECH-260 No-Go installs), calls
`discharge_domain` on an empty field, and gets 0 back → `residue_centers_discharged = 0` →
`discharge_events = 0` and `mean_residue_weight_reduction = 0.0` on every closure, every seed. C2 is
pinned at 0 **by construction**, independent of closure behaviour.

This is the **460c shape repeated one leg downstream**: 460c was `n_closures = 0` because env completions
were never routed into `emit_closure` (a wiring/harness gap, fixed by the Leg-A hook → 466d C1 now PASS).
466d is `discharge_events = 0` because the residue-accumulation INPUT to the discharge leg is never
exercised by the harness. Both are missing-call harness gaps, not falsifications.

**Manifest `criteria_non_degenerate` correction:** C2 is **degenerate** (CLAUDE.md sense — a discriminative
metric pinned by test construction so it can never fire regardless of behaviour). `discharge_domain` on an
empty field can only return 0. The script's two non-vacuity gates (contact, commitment+completion) do NOT
include a *residue-field-populated* gate — that is the unmet precondition that makes the self-routed
`weakens` untrustworthy (V3-EXQ-642 invalid-precondition pattern). Recommended
`non_degenerate_per_claim: {SD-034: false, MECH-094: false}` with the degeneracy reason below.

## 3. Claim-layer mapping

**SD-034** (design_decision, provisional, implementation_phase v3, v3_pending false,
pending_retest_after_substrate true; umbrella narrowed 2026-06-19 — de-commit/latch sub-property → MECH-445/446).
The 466d residue-discharge leg (part c) is **structurally distinct** from the MECH-445/446 latch/beta-coupling
de-commit lineage (the 460e..460l / 468e/468f autopsies). Did the test let SD-034's discharge leg express
itself? **No** — discharge cannot fire on an empty field. Implementation gap is at the **harness**, not the
claim. Reading: **intact / non_contributory**, NOT weakened.

**MECH-094** (mechanism_hypothesis, **stable**, conf 0.868, 23 supports vs 1 weakens — heavily
literature-grounded simulation/real write distinction). 466d exercises **no** simulation/replay path; the
discharge is waking-only. MECH-094 yields no signal here either way. Tag is inherited from the SD-034 cluster.
Per `claim_ids` accuracy rule (err toward fewer tags) and to protect a stable claim from a spurious weakens:
**drop MECH-094 from the scored tags** on the 466e retest (re-add only with an explicit simulation-tagged
discharge control). Reading: **non_contributory (not exercised)**.

## 4. Biological-reference triage

Closest reference: closure-triggered, domain-scoped relaxation of just-completed rule-episode residue —
sleep-style contextualisation (Rich & Shapiro 2009 sequence-completion cells; Collins & Frank 2014 task-set
disengagement). The REE `discharge_domain` is a **faithful translation** (multiplicative decay within a
bandwidth-scoped domain, hard 1e-6 floor preserving the "residue cannot be erased" invariant; valence_vecs
untouched). It is NOT a formal-definition import. The failure does NOT resemble a missing biological
dependency of the discharge mechanism — it resembles "the experiment never put any residue on the table to
discharge." `lit_status: present` (the discharge mechanism is biologically anchored and built).

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | discharge could not express — empty field; not a fair test of SD-034's discharge leg |
| Biological reference | clear | closure→residue relaxation faithfully translated (discharge_domain); not a formal import |
| Prerequisites / dependency | **missing** | residue-accumulation path (`update_residue → add_residue`) never exercised by the scaffold curriculum or the eval |
| Implementation completeness | complete | `discharge_domain` implemented + correctly wired (`closure_operator.residue = residue_field`, agent.py:1577); fires every closure |
| Environment adequacy | adequate | 603n foraging substrate, contact guard 1.0 |
| Measurement adequacy | **under-instrumented** | no residue-field-populated non-vacuity gate; instruments weight-reduction but never ensures there is residue to reduce → C2 degenerate |
| Integration | isolated | discharge leg decoupled from the residue-accumulation path in this harness |
| Scale / capacity | adequate | not a budget/depth issue |

**Recommended epistemic_category:** NOT `substrate_ceiling` (the substrate works; nothing to enrich). This is
a degenerate/non-contributory run from an unmet harness precondition → **non_contributory**, `pending_retest`.

## 6. Re-derive brake (MOVE-3)

SD-034 prior `substrate_ceiling`/`non_contributory` autopsies tagging the claim: **9**
(SD-034-closure-cluster, -ext, -control-plane-d; V3-EXQ-460b/461b/464b/466b; 460e/460f/460g; 468e/468f) —
threshold (2) far exceeded. MECH-094: 2.

**Brake adjudicated NOT FIRED (user-confirmed at gate).** Rationale (V3-EXQ-642 exemption): the brake exists
to stop re-testing a claim *at the same granularity against the same substrate ceiling*. This FAIL is NOT a
substrate ceiling — it is a harness/invalid-precondition artefact (empty residue field). The discharge
substrate is built, wired, and fires; firing the brake would route to `/implement-substrate` on a substrate
that needs **no enrichment**. The correct route is a harness-fix re-queue (populate the field) — exempt from
the brake. Additionally, the 9 priors are almost all the MECH-445/446 latch/beta de-commit lineage (a
*different* leg than residue discharge); 466d is the first proper test of the discharge leg with closures
actually forming, and it found a harness gap. `re_derive_brake.fired = false`.

## 7. Learning extracted

- A "negative-control-passes / discrimination-fails" fingerprint is the substrate-ceiling tell **only after**
  confirming the discrimination metric *could* fire. Here C2 (`discharge_events`) is pinned at 0 by an empty
  residue field, so the fingerprint is a false positive — the V3-EXQ-642 invalid-precondition pattern one leg
  past the 460c hook gap.
- The closure five-part "done" token's leg (c) residue-discharge requires a **populated residue field** as a
  precondition; the 466 harness lineage instruments the discharge effect but never exercised
  `update_residue → add_residue`, so leg (c) was never on a fair test bed.
- Future closure-leg behavioural arms MUST add a residue-field-populated non-vacuity gate (active_mask count
  > 0 at closure time) alongside the contact + commitment+completion gates, so an empty-field run self-routes
  `substrate_not_ready_requeue` instead of self-routing a false `weakens`.

## 8. Routing (user-confirmed)

**`queue-experiment`** — a 466e successor (NEW letter, supersedes 466d) that:
- calls `agent.update_residue(harm_signal, world_delta)` each step in the scaffold P1/P2 training AND in the
  `_eval_residue_discharge` loop so the residue field accumulates active centers reflecting the trajectory
  BEFORE a closure fires;
- adds a residue-field-populated non-vacuity gate (`active_mask.sum() > 0` on ≥2/3 seeds at closure time) that
  self-routes `substrate_not_ready_requeue` when unmet (never a false weakens);
- keeps the load-bearing C2 discharge gate + C1/C3, with `claim_ids = [SD-034]` (MECH-094 dropped; re-add only
  with an explicit simulation-tagged discharge control).

`recommended_substrate_queue_entry.action = none` — the discharge substrate (`discharge_domain`) is built and
wired; nothing to create/amend. `pending_retest_after_substrate` on SD-034 is already `true` and unchanged
(this is a harness retest, not a substrate build).

## 9. Draft evidence_quality_note (governance to write; do NOT write here)

> V3-EXQ-466d (satisficing residue-discharge behavioural) → SD-034 + MECH-094 **non_contributory**
> (confirmed failure_autopsy_V3-EXQ-466d_2026-06-24, interactive gate). Closures now FORM (C1 PASS — the
> 466c Leg-A env-completion hook is fixed) but C2_discharge_events = 0 on 3/3 seeds because the residue
> field is **empty for the whole run**: `discharge_domain` is implemented and correctly wired
> (`closure_operator.residue = residue_field`, agent.py:1577) and fires on every closure, but neither the
> scaffold curriculum nor the eval ever calls `agent.update_residue()` (the only path to `add_residue` →
> active centers), so `discharge_domain` returns 0 from an empty `active_mask` (field.py:671) regardless of
> closure behaviour. C2 is therefore **degenerate** (pinned by test construction, not behaviour) — the
> V3-EXQ-642 invalid-precondition pattern, NOT a falsification and NOT a substrate ceiling (the discharge
> mechanism needs no enrichment). MECH-094 is not exercised (waking-only discharge; no simulation path) and
> is dropped from the scored tags to protect its stable status. Re-derive brake NOT fired (642 exemption:
> harness gap, harness-fix re-queue is exempt). Routed `/queue-experiment` V3-EXQ-466e: wire
> `update_residue` into the scaffold P1/P2 + eval so the field accumulates centers before closure, add a
> residue-field-populated non-vacuity gate, `claim_ids=[SD-034]`. `pending_retest_after_substrate` stays
> true; no claims.yaml status change.
