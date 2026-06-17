# Failure Autopsy -- V3-EXQ-460e (SD-034 commitment-closure-control-plane, Leg C)

- **Generated / confirmed:** 2026-06-17T14:30:51Z
- **Status:** confirmed (interactive gate; user AskUserQuestion 2026-06-17)
- **Scope:** single (one target; tightly-coupled to the SD-034 closure-control-plane lineage)
- **Predecessor:** `failure_autopsy_SD-034-closure-control-plane-d_2026-06-13` (+ `failure_autopsy_SD-034-closure-cluster_2026-06-12`, `..._ext_2026-06-12`)
- **Substrate under test:** `commitment-closure-control-plane` (status `amend_implemented_pending_validation`) -- Legs A (env-completion hook) + B (de-commit refractory) landed 2026-06-12; **Leg C (scaffold_train_rule_bias_head, ree-v3 3ccc48a 2026-06-16) NOW BUILT and WORKING.**
- **Run:** `v3_exq_460e_sd034_closure_control_plane_behavioural_20260617T085103Z_v3` (machine ree-cloud-1, supersedes 460d)

---

## One-line verdict

The Leg-C rule_bias_head **now trains** (rule_bias_trained 1.0 on 3/3 seeds; the 460d flag-set-but-never-optimized bug is fixed) -- but the **MECH-090 bistable beta latch still fails to engage on 2/3 seeds**, so the readiness gate self-routes `substrate_not_ready_requeue` (`beta_engagement_not_met_both_arms`) **before the de-commit DV (C2) ever runs**. This is a **commit-without-beta dissociation**: the closure control-plane installs commitment behaviour (committed_trajectory, closures, No-Go, sequence completions all fire) but the bistable BetaGate never elevates, because E3 never reaches a *decisive natural commit-entry* (`result.committed`) on the 603n foraging substrate on most seeds. The trained rule_bias_head cannot fix this -- it biases per-candidate *scoring*, not the `running_variance` that gates commit-*entry*. This is **exactly the escalation the -d autopsy pre-registered** (line 90). Neither a falsification nor an instrumentation null (seed 44 is the positive existence proof). Route to an `implement-substrate` **amend** of `commitment-closure-control-plane` (beta-engagement deliverable); SD-034 / MECH-260 / MECH-261 stay `non_contributory` + `pending_retest_after_substrate`.

---

## Facts reconstruction

### Readiness gates (the run self-routed on the third)

| Gate | measured | threshold | met |
|---|---|---|---|
| foraging_contact_guard | 1.0 | 0.667 | yes |
| **rule_bias_head_trained** | **1.0** | 0.667 | **yes (Leg C works)** |
| **beta_engagement_both_arms** | **0.333** | 0.667 | **NO (binding failure)** |
| closure_trigger_available_count | 1.0 | 0.667 | yes |

`route_reason = beta_engagement_not_met_both_arms`; `overall_pass = false`; per-seed criteria pass `[false, false, true]`.

### Per-seed dissociation (ARM_CLOSURE_ON)

| seed | committed_steps | total_beta_elevated | n_closures | n_seq_completions | rule_bias_mean_abs |
|---|---|---|---|---|---|
| 42 | 2415 | **0** | 7 | 7 | 0.100 (clamp rail) |
| 43 | 2019 | **0** | 6 | 6 | 0.100 (clamp rail) |
| 44 | 2213 | **176** | 5 | 5 | 0.020 |

ARM_CLOSURE_OFF: seed 42 committed_steps=0 / beta=0; seed 43 committed_steps=0 / beta=0; seed 44 committed_steps=2606 / beta=223. Seed 44 is the only seed that commits (and engages beta) on **either** arm; on the ON arm the closure machinery additionally drives committed_steps on 42/43 without any beta elevation.

### Seed-44 disambiguator (the de-commit DV is real)

On seed 44 both arms engage beta and **C2 passes**: ON `mean_beta_elevated_steps` 11.73 < OFF 14.87 (a non-cap-pinned occupancy drop, OFF having committed above MIN_OFF_OCC). So the instrumentation and the de-commit DV work end-to-end when the agent reaches a decisive commit -- decisive commit-entry is simply fragile (1/3 seeds). This rules out an instrumentation null / vacuous-criterion artifact (cf. V3-EXQ-642): the substrate CAN produce the full signal.

---

## The load-bearing finding (code-confirmed)

The 460e config sets only `cfg.heartbeat.beta_gate_bistable = True`; the MECH-090 R-c readiness gates (`use_commit_readiness_gate`, `use_mech090_readiness_conjunction`) are **OFF**. So the bistable elevate path (`ree_core/agent.py:5847-5855`) reduces to:

```python
if result.committed and not self.beta_gate.is_elevated:
    self.beta_gate.elevate()
```

Beta elevates **iff E3 returns `result.committed`** -- i.e. `running_variance < commit_threshold`, a decisive natural commit-entry. But the manifest's `total_committed_steps` counts a *different* state: `e3._committed_trajectory is not None`, which the closure machinery / env-completion hook populates independently. The two states are **decoupled** on seeds 42/43: the closure control-plane sets the committed_trajectory (2415 / 2019 steps) and fires closures (7 / 6), but `result.committed` essentially never fires, so `beta_gate.elevate()` is never reached and `total_beta_elevated = 0`.

**Why the trained head does not rescue it:** `rule_bias_head` biases per-candidate *score* (which mechanically fixed the 460d C2/C4 de-commit-authority gap). It does **not** touch the `running_variance` that gates commit-*entry* decisiveness. Beta-engagement lives one layer up from the de-commit authority the head trains. The inverse tell confirms it: seeds 42/43 saturated the head at the 0.10 `bias_scale` clamp rail (uniform across candidates, no cross-candidate gradient -- the SD-033a/b clamp-saturation note) yet beta fails on exactly those seeds, while seed 44 (smaller 0.020 bias) is the one that engages. rule_bias magnitude does **not** predict beta engagement.

This is the literal **commit-without-beta fragility** the -d autopsy named (Section "load-bearing finding"; cluster pattern reading `beta_engagement_fragility`) and **pre-registered as the escalation trigger** (routing line 90): *"Escalate to a MECH-090 R-c-gate / scaffolded-curriculum substrate amend only if beta still fails to elevate on >=2/3 seeds after the head is trained."* Head trained; beta still fails on 2/3 -> trigger met.

---

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | SD-034 / MECH-260 / MECH-261 NOT exercised -- the readiness gate self-routed before the C2 de-commit DV ran. Do not weaken. |
| Biological reference | clear | BG beta-band commitment latch (STN/GPe); elevation requires a decisive commit-entry (Hanes & Schall accumulator-to-threshold). Beta fails to engage = the agent never enters a stably-committed motor program on most seeds despite a nominally-set committed_trajectory. |
| Prerequisites | **missing** | Robust **commit-with-beta engagement** (decisive `result.committed` that elevates the bistable latch) on the 603n foraging substrate. This is the binding gap. |
| Implementation | partial | Leg A (hook), Leg B (refractory), Leg C (trained head) all built and working; beta-engagement is the residual. |
| Environment | adequate | guard 3/3; closures + sequence completions fire on all seeds. |
| Measurement | adequate-but-gated | C2 is non-cap-pinned (sound; seed 44 proves it). Its precondition (beta occupancy > 0 both arms) is the binding constraint, correctly caught by the readiness gate -- not a measurement defect. |
| Integration | isolated | Closure fires its proximal events but the installed commitment is decoupled from the bistable beta latch on 2/3 seeds (commit-without-beta). |
| Scale / capacity | possibly insufficient (secondary) | closure_eval=15 / P1=50; more decisive policy might raise the commit-entry rate, but the -d autopsy already deprioritized budget vs the substrate amend. |

**Recommended epistemic_category:** the manifest's self-route `substrate_not_ready_requeue` is **confirmed** (precondition genuinely unmet: beta engagement). Not a substrate_ceiling (seed 44 proves the distinction is deliverable); not a vacuous_pass. The claims stay candidate/provisional.

---

## Recurrence check (granularity-debt / `/claim-synthesis` trigger)

Third autopsy in the lineage (*c cluster 2026-06-12 -> *d 2026-06-13 -> 460e). But the signatures **advance one structural property link-by-link** -- `n_closures=0` (Leg A) -> de-commit authority absent (Leg C unbuilt) -> beta-engagement fragility (Leg C built) -- each closing one prerequisite and surfacing the next, **not** structurally different signatures circling one coarse claim. The commit-without-beta fragility was explicitly named and pre-registered by the -d autopsy. Therefore this is **NOT** granularity debt; `/claim-synthesis` is not the route. It is a clean, pre-registered substrate escalation.

---

## Learning extracted

- Training the Leg-C rule_bias_head was **necessary but not sufficient**: it fixed the 460d de-commit-*authority* mechanics (per-candidate scoring) but does nothing for beta-*engagement*, which is gated upstream by commit-entry decisiveness (`running_variance < commit_threshold`).
- The closure control-plane's proximal events (committed_trajectory, closures, No-Go, sequence completions) are **decoupled from the bistable MECH-090 latch** on the foraging substrate when `result.committed` never fires -- the "commit-without-beta" dissociation.
- The de-commit DV (non-cap-pinned ON<OFF occupancy drop) is **sound and readable** when beta engages (seed 44, C2 PASS) -- the gap is engagement, not measurement.
- `rule_bias_mean_abs` saturating at the `bias_scale` clamp rail (0.10) is a uniform, no-gradient signal -- a watch item for any rule_bias-magnitude readiness gate (magnitude != differentiation).

## Repair pathway (user-confirmed: list both mechanisms)

`implement-substrate` **amend** on the existing `commitment-closure-control-plane` substrate_queue entry (do NOT duplicate). Beta-engagement deliverable; both candidate mechanisms recorded, implement-substrate to choose/sequence:

- **(a) couple closure -> beta elevation** -- make the env-hook / closure-installed commitment also elevate the bistable BetaGate, decoupling the de-commit DV from the fragile natural `running_variance` crossing so it is readable on every seed where closure fires;
- **(b) commit-entry decisiveness** -- address why `running_variance` rarely crosses `commit_threshold` on the 603n foraging substrate (adapt the threshold for the substrate, or scaffold a more decisive P1 policy) so `result.committed` fires on >=2/3 seeds;
- **(c) budget escalation** (eval 15 / P1 50) -- deprioritized secondary, per the -d autopsy.

Retest gate (after amend): beta_engagement_both_arms met on >=2/3 guard seeds, THEN the C2 non-cap-pinned de-commit DV ON<OFF on >=2/3 seeds. Re-issue as 460f. The **468e** successor (MECH-090 commit-entry conjunction under the trained head) is separately owed.

## Draft evidence_quality_note (governance applies; this skill does not write it)

> V3-EXQ-460e (supersedes 460d): Leg-C rule_bias_head now trains (rule_bias_trained 1.0 3/3) but the MECH-090 bistable beta latch engaged on only 1/3 seeds (beta_engagement_both_arms 0.333 < 0.667), so the readiness gate self-routed substrate_not_ready_requeue before the C2 de-commit DV ran. Code-confirmed commit-without-beta dissociation: with both MECH-090 R-c gates OFF, beta elevates only on E3 result.committed (running_variance < commit_threshold), which fails on 2/3 seeds on the 603n foraging substrate; the closure control-plane sets committed_trajectory + fires closures regardless. Trained head biases scoring, not commit-entry decisiveness. Seed 44 (beta engaged both arms; C2 ON 11.7 < OFF 14.9) is the positive existence proof that the de-commit DV is sound. SD-034 / MECH-260 / MECH-261 stay non_contributory + pending_retest_after_substrate (never fairly tested). Escalation pre-registered by failure_autopsy_SD-034-closure-control-plane-d_2026-06-13 line 90.

---

## Routing decision (user-confirmed)

1. **substrate_queue `action=amend`** on `commitment-closure-control-plane`: append the 460e failure record + the beta-engagement deliverable (mechanisms a + b; budget secondary). Status stays `amend_implemented_pending_validation`; `ready` stays false.
2. **Evidence disposition:** SD-034 / MECH-260 / MECH-261 -> `non_contributory` + `pending_retest_after_substrate` (no status/confidence change; no narrow_supports flag). Seed-44 ON<OFF recorded as a narrow, non-scoring positive observation.
3. **Owed successor:** 468e (MECH-090 commit-entry conjunction under the trained head) -- separate `/queue-experiment` session, gated on the beta-engagement amend.

commitment_closure:GAP-4 stays in-progress; closes when the post-amend 460f re-queue returns a contributory PASS (beta engaged + ON<OFF de-commit on a non-cap-pinned DV on >=2/3 seeds).
