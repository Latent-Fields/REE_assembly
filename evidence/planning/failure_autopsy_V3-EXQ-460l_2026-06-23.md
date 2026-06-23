# Failure Autopsy — V3-EXQ-460l (ARC-108 JOB-2 control-plane L0/L1/L2 falsifier)

- **Generated (UTC):** 2026-06-23T04:01:15Z
- **Scope:** single (lineage member 460h..460l)
- **Status:** confirmed (interactive gate, user "Confirm as recommended")
- **Run:** `v3_exq_460l_job2_control_plane_ramp_habenula_falsifier_20260622T221756Z_v3` — terminal FAIL on ree-cloud-4, 2026-06-22T22:17:57Z
- **Supersedes:** V3-EXQ-460k (the rung-6 duration-lever falsifier); this is its biologically-faithful JOB-2 DRIVER-pair successor
- **Claims tagged:** MECH-090, MECH-342, MECH-445, MECH-446, ARC-108
- **Manifest self-route:** `substrate_not_ready_requeue`, `route_reason = closure_exclusive_eval_did_not_arm_hold`, `evidence_direction = non_contributory` (all five claims)

## 1. Facts (no interpretation)

The experiment is the ARC-108 JOB-2 sec-7.2 control-plane falsifier: does giving the
commit/maintain/de-commit machinery its missing dopaminergic DRIVER pair (the rho_t
maintenance ramp that peaks-then-declines + the habenula negative-delta_t de-commit) (a)
self-limit the flat-hold monopoly and (b) supply a content-driven dissociable de-commit
where the hand-tuned arithmetic plumbing could not? Three eval arms on one trained
substrate per seed (driver pair toggled at eval): L0_FLAT_LATCH / L1_RHO_RAMP /
L2_RHO_HABENULA. `closure_exclusive_decommit_eval`, `use_closure_commit_beta_coupling`,
and `use_natural_commit_latch_hold` ON in every arm.

Six readiness/non-vacuity gates must clear before the D1/D2/D3 discriminators score; any
unmet gate self-routes `substrate_not_ready_requeue` (never a false weakens). Observed
(3 seeds 42/43/44, all guard-passing):

| Gate | Result | Evidence |
|---|---|---|
| 1 foraging contact guard | **met** (1.0) | P2 contact_rate 0.11–0.28, z_goal_norm_at_contact_peak 0.41–0.51 |
| 2 rule_bias head trained | **met** (1.0) | mean \|bias\| 0.021–0.100 > floor |
| 3 closure-exclusive eval armed hold | **FAIL** (0.0) | `ncl_hold_closure_armed_total = 0` AND `ncl_hold_reassert_total = 0` on **every** arm/seed |
| 4 L0 monolithic-hold baseline | **FAIL** (0.0) | L0 `mean_per_commit_hold` ≈ 1.1–1.3 vs floor 5.0; `max_consecutive_beta_run` 6–7 |
| 5 rho proximity variance | **FAIL** (0.0) | L1 `rho_peak_max = 0`, `rho_n_releases_total = 0` |
| 6 delta_t negative variance | **met** (1.0) | L2 `n_neg_delta_ticks` 834–1117, `delta_t_min` −0.038 to −0.42, `delta_t_std` 0.012–0.032 |

The script halts at the first unmet gate (3) and reports `route_reason =
closure_exclusive_eval_did_not_arm_hold`. D1/D2/D3 never scored. `n_habenula_aborts = 0`
on every arm (no armed hold to abort), though gate 6 confirms the habenula's input signal
was present.

## 2. Claim-layer mapping

- **MECH-445** (closure→beta coupling engagement), **MECH-446** (de-commit-authority magnitude): candidate / v3_pending / pending_retest_after_substrate. The DV that would test them never ran — no armed hold formed.
- **MECH-090** (BetaGate commit-entry conjunction), **MECH-342** (maintenance-time release coupling): precondition/peripheral here (the latch and its release); not exercised.
- **ARC-108** (JOB-2 control plane): substrate_conditional. The DRIVER pair is built but could not be exercised; ARC-108 is neither supported nor weakened by this run.

No `claim_ids` inheritance error: the tags reflect what the run attempted to test. The run produced no interpretable signal *for any tagged claim's mechanism* — but it produced a load-bearing **substrate** signal (Section 3).

## 3. Biological-reference triage — the core move

Closest reference: the **lateral habenula (LHb)** fires on worse-than-expected (negative-RPE)
outcomes and, via RMTg, suppresses dopaminergic drive to abort an ongoing commitment; the
BG maintains the commitment hold the de-commit interrupts, with a DA-ramp-like maintenance
signal (the rho_t proximity ramp analog) that peaks then declines so the hold self-limits.

This is **not a formal-definition import** — it is a faithful translation. The divergence
is a **wiring/translation gap**: in REE the closure-coupled commit that should arm the hold
(`_closure_commit_active`) is structurally gated on `e3._committed_trajectory`, which is set
*only* under the F-driven natural commit (`e3_selector.py:1926`, per the confirmed 460k
autopsy). So the hold cannot arm independently of the F-dominated natural commit, and the
"dissociable" closure-exclusive eval is illusory outside the contract harness that injects
`e3._committed_trajectory` directly.

Does the failure resemble a missing biological dependency? **Yes** — it is exactly what you
would see if the BG never established a sustained commitment hold: the habenula's negative-RPE
input is live, but there is nothing to abort. The de-commit reference mechanism is intact;
its **prerequisite** (a sustained, F-independent hold) is absent.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | test vacuous; no claim exercised; nothing weakened |
| Biological reference | partial | LHb de-commit input live (signed-RPE delta_t); the BG hold it acts on never arms |
| Prerequisites | missing | closure-coupled commit gated on F-driven `e3._committed_trajectory`; hold never arms in a real eval |
| Implementation | partial | JOB-2 DRIVER pair built + OFF-correct, but has nothing to drive |
| Environment | wrong pressures | 603n foraging substrate produces no sustained monolithic hold (max run 5–7); binding constraint is upstream at commit-entry |
| Measurement | adequate | six gates correctly caught the vacuity and self-routed |
| Integration | isolated | closure plane / latch-hold / DRIVER pair don't couple in a real eval |
| Scale | unknown | not reached |

**Recommended `epistemic_category`: `substrate_ceiling`.** **Direction: `non_contributory`** (all five claims). `pending_retest_after_substrate = true`.

## 5. Learning extracted

1. 460l independently confirms the 460k wiring diagnosis from a *clean* foraging eval (no harness injection): the closure-exclusive de-commit eval substrate (e52158d) does **not** arm the closure-coupled latch-hold in a real run — `ncl_hold_closure_armed_total = 0` everywhere.
2. The biologically-faithful JOB-2 DRIVER pair (rho ramp + habenula, the B6 structural fix) is **unexercisable** here: the ramp has no monolithic hold to self-limit (L0 ≈ 1.2 vs floor 5.0); the habenula has no armed hold to abort.
3. **Load-bearing reframe:** the maintenance-RELEASE face (P2-rootC) is not even the exercisable constraint — no sustained hold forms, so maintenance cannot be the bottleneck. The binding constraint is upstream at commit-ENTRY / sustained-occupancy formation, i.e. the **F-dominance selection face (MECH-439)**. The commit-duration face is downstream of, and gated by, the same F-dominance that monopolises commit-entry.
4. **Narrow positive:** the JOB-1 signed-RPE `delta_t = R_t − V̂_t` (reused by the habenula) is live and produces genuine negative-RPE variance in a real eval. The habenula's *input* works; only the hold it would act on is absent. This is positive evidence for the JOB-1 RPE machinery, **not** for the JOB-2 control plane.

## 6. Re-derive brake — FIRED

Prior `substrate_ceiling` / `non_contributory` autopsies tagging MECH-445/446:
`failure_autopsy_V3-EXQ-460h/460i/460j/460k` (4 each). With 460l this is the **5th**.
Threshold 2 → **brake fires**. (MECH-090: 9 prior; MECH-342: 2 with this.)

- **Routing: `implement-substrate`**, amend the existing `f_dominance_conversion_ceiling` substrate_queue entry (which already owns root-C / the commit-release-duration face and lists MECH-445/446 in `unblocks_claims`). Consolidate with the 460k autopsy's `amend` recommendation — **no new substrate entry**.
- **Substrate work:** decouple closure-coupled hold-arming from the F-driven `e3._committed_trajectory` so a closure-coupled commit can arm and sustain a hold independently of the F-dominated natural commit. Until then, natural-commit occupancy is not dissociable from closure-de-commit and the de-commit face is untestable.
- **REFUSE a V3-EXQ-460m same-claim re-queue.** Another lettered de-commit falsifier circling the same un-arming substrate is exactly the loop the brake exists to stop. A redesign of a *different* mechanism (new EXQ number, different `claim_ids`) or a commitment-free read remains allowed.

## 7. Cluster pattern (460h..460l)

- **Shape:** readiness gates self-route `substrate_not_ready_requeue`; the closure-coupled hold never arms / never sustains, so every discrimination criterion is unscorable — the substrate-ceiling fingerprint across the whole lineage.
- **Independent bugs?** No — one structural property.
- **Structural property:** the commitment-maintenance substrate does not produce a sustained, F-independent commitment hold on the foraging substrate; the closure-coupled commit that should arm it is structurally entangled with the F-driven natural commit. Neither a duration lever (460k) nor a dopaminergic DRIVER pair (460l) can act on a hold that does not form.
- **Two readings (both live):** (a) substrate enrichment — build F-independent closure-coupled hold-arming; (b) the upstream binding constraint is commit-entry F-dominance (MECH-439), not maintenance-release. They are complementary, not competing: (a) is the local fix that makes the face testable; (b) is why the face is subdominant.

## 8. Draft `evidence_quality_note` (governance writes; not written here)

> V3-EXQ-460l (ARC-108 JOB-2 control-plane L0/L1/L2 falsifier, supersedes V3-EXQ-460k) RAN terminal FAIL/non_contributory 2026-06-22T22:17:57Z: clean substrate_not_ready_requeue at readiness gate 3 (closure_exclusive_eval_did_not_arm_hold) — `ncl_hold_closure_armed_total=0` AND `ncl_hold_reassert_total=0` on every arm/seed. Independently confirms the 460k wiring diagnosis: `_closure_commit_active` is structurally gated on the F-driven `e3._committed_trajectory`, so the closure-coupled hold does not arm in a real eval; L0 also fails to monopolise (mean per-commit hold ~1.2 vs floor 5.0) and rho never peaks. The biologically-faithful JOB-2 DRIVER pair (rho ramp + habenula) is unexercisable on this substrate. NOT a falsification (no claim exercised). The habenula INPUT signal (JOB-1 signed-RPE delta_t) is live (n_neg_delta_ticks 834-1117) — a narrow positive for the JOB-1 RPE machinery, not for the JOB-2 control plane. pending_retest_after_substrate. PROMOTES NOTHING.

## 9. Routing decision (confirmed)

`implement-substrate` — amend `f_dominance_conversion_ceiling` (closure-coupled-hold arming,
F-independent). Re-derive brake fired → **refuse** a 460m re-queue. `commitment_closure:GAP-4`
stays in-progress; `conversion_ceiling_campaign:P2-rootC` stays `assembling` (substrate build
owed). PROMOTES NOTHING (MECH-445/446 candidate/v3_pending; ARC-108 substrate_conditional;
MECH-090/342 candidate).
