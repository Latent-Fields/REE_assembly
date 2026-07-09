# Failure Autopsy -- V3-EXQ-725 (coherence non-reducibility RETEST on the LEARNED binder)

- **Generated (UTC):** 2026-07-09T18:49:02Z
- **Target run_id:** `v3_exq_725_coherence_nonreducibility_learned_binder_20260709T095128Z_v3`
- **queue_id:** V3-EXQ-725  |  **machine:** ree-cloud-2
- **experiment_purpose:** diagnostic  |  **claim_ids:** [] (non_contributory; excluded from confidence / conflict scoring)
- **Outcome:** FAIL  |  **self-route (majority_label):** `C_changes_selection_specificity_unproven_route_followup`
- **Scope:** single (but the **4th** iteration in one lineage -- 641 -> 641a -> 720 -> 725)
- **Status:** confirmed (user-adjudicated 2026-07-09)
- **Prior autopsies in lineage:** `failure_autopsy_V3-EXQ-641_2026-06-06`, `failure_autopsy_V3-EXQ-641a_2026-06-06`, `failure_autopsy_V3-EXQ-720_2026-07-09`

---

## 1. The question (unchanged across the lineage)

Is the cross-stream coherence term C(tau) **non-reducible** to the integrated prediction-error cost E(tau)? I.e. does a coherence term in the selection rule change **which** trajectory is selected, in a **coherence-specific** way (not reproducible by a contrast-matched shuffle), independently of prediction-error magnitude?

725 is a **retest of the 641a/720 harness verbatim** (E-orthogonalized cross-stream-only phase-alignment read + shuffle-of-real-C contrast-matched control + two-mode-active gating + 6 seeds + substrate-level rebinding probe). The **only** change vs 720: the agent is built with `cross_stream_binding_learned=True, strength=0.5` -- the LEARNED (plastic) binder that the 720 autopsy routed as the residual prerequisite (built 2026-07-09, session bold-payne-7587d5). It does **not** supersede 641a/720 (their findings on the unbound / fixed-field substrates stand).

## 2. Facts reconstruction (ran to completion -- 18/18 runs, 6 seeds [42-47], 3 conditions)

Preconditions all report **met**; `criteria_non_degenerate` all True; `gating_adequacy_warning=false`.

| Gate | Tests | Threshold | 641a | 720 | **725** |
|---|---|---|---|---|---|
| D1 -- gated behavioural divergence | coherence changes selection | >= 0.05, >= 4/6 | 6/6 | 4/6 | **6/6** |
| D3 -- abs corr(E, rawC) < 0.9 | C not a linear fn of E | < 0.9, >= 4/6 | 6/6 | 6/6 | **6/6** |
| **SPEC -- real C diverges > shuffle** | *structure* of C carries info beyond E | margin >= 0.05, **>= 4/6** | 1/6 | 3/6 | **0/6 FAIL** |
| rebinding exercisable (PASS-relevant here) | binding intake's own falsifier | n_rebind > 0 | 0/6 | 0/6 | **6/6 (1387 total)** |

**Per-seed SPEC (real_frac_state_div_gated vs shuffle):**
- seed 42: 1.00 vs 1.00 -> not (tie, both saturated)
- seed 43: 0.192 vs 0.568 -> not (**shuffle higher**)
- seed 44: 1.00 vs 1.00 -> not (tie)
- seed 45: 0.742 vs 0.800 -> not (shuffle higher)
- seed 46: 0.250 vs 0.942 -> not (**shuffle much higher**)
- seed 47: 0.220 vs 0.782 -> not (shuffle higher)

`n_coherence_specific = 0`, `n_seed_pass = 0`, `min_seeds_for_pass = 4`. **Failed criterion: SPEC (load-bearing, discrimination).** SPEC did not merely fail to clear -- it **regressed** below the fixed-field 720 (3/6) and even below the unbound 641a (1/6), with the shuffle control driving >= as much behavioural divergence as real coherence in every seed.

**The load-bearing fact -- the binder never converged.** The InfoNCE loss (`cross_stream_binder.learn_step`) is symmetric cross-entropy, `0.5*(CE(logits,targets)+CE(logits.T,targets))`, whose **chance floor is `log(batch)`**. The binder's default `batch=64` -> chance ~= **4.16 nats**. Observed `binder_last_loss` across seeds: 3.75 / 3.89 / 3.95 / 3.90 / 3.89 / 3.96 -- **flat at ~90-95% of chance**, and NOT monotone in `binder_learn_steps` (seed 42 ran 1760 steps -> 3.75; seed 43 ran 487 steps -> 3.89; i.e. 3.6x more training bought ~0.14 nats). The plastic `phi_self`/`phi_world` projections barely moved off random init. The P0 contrastive task -- separate within-tick observed (z_self, z_world) pairs from in-batch shuffles -- is **unlearnable as configured**: in the slow-drift 12x12 CausalGridWorldV2 consecutive latents are near-collinear, so positives are not separable from negatives and InfoNCE sits at chance.

## 3. Claim-layer mapping

Diagnostic, `claim_ids=[]` -> no tagged claim is weakened or strengthened. **Bears on** (cited, not tagged): INV-002 (coherence includes temporal/phase binding), MECH-089 (theta-cycle temporal packaging), MECH-094 (simulation/real write distinction -- does not newly apply), MECH-270 (ephaptic-field verisimilitude readout -- the binder is a MECH-270 instantiation), MECH-269 (per-stream verisimilitude / anchor selection). The candidate Q `entities/selection.coherence_nonreducibility` remains **unregistered** in claims.yaml and does **not** reach the register threshold (needs 4/6 SPEC AND n_rebind>0). It is **not** weakened -- see Section 6: this run did not fairly test the learned binder, so it carries no evidence for OR against the coherence-non-reducibility question.

## 4. Biological-reference triage (the core move)

- **Closest mechanism:** binding-by-synchrony / communication-through-coherence (Fries), theta-gamma binding (Singer/Gray; Buzsaki theta-gamma code). Partially instantiated in REE via MECH-089 / MECH-270.
- **Existence proof for the CLASS, not this implementation.** In brains, binding-by-synchrony operates on streams whose coupling is **learned / plastic** -- genuine cross-stream coherence carries conjunction-specific information *because the coupling was shaped by experience to make it informative*. The 720 autopsy correctly identified plasticity as the residual prerequisite.
- **Faithful translation vs formal import:** the learned binder installs the **right class** of mechanism (plastic multiplicative coincidence detector trained by contrastive co-encoding) -- so this is NOT a formal-definition-import divergence. The failure is one level down: the mechanism is wired but **does not train** in this environment. Symbol of the mechanism (plastic projections + InfoNCE optimizer + P0 curriculum) present; functional role (a converged binder that makes real coherence conjunction-specific) **absent**.
- **Missing-dependency signature?** Yes -- and it is a *training-signal* dependency, not an architecture dependency. Biologically, a coincidence detector only becomes informative if the environment presents separable conjunctions to learn from. A near-collinear slow-drift gridworld presents none, so the contrastive objective has no gradient signal -- exactly what an unlearnable-positives regime looks like. The regression 3/6 -> 0/6 is the tell: a *structured* fixed field (deterministic joint-state common cause) gave partial specificity; a *near-random* plastic coupling injects noise that destroys even that.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a (diagnostic, claim_ids=[]) | candidate Q coherence_nonreducibility unregistered; NOT weakened -- run did not fairly test the learned binder |
| Biological reference | clear (for the class) | correct mechanism class (learned binding-by-synchrony); the gap is training-signal, not architecture |
| Prerequisites / dependency | **missing (training signal)** | the P0 contrastive curriculum needs separable positives; CausalGridWorldV2 slow-drift collinearity provides none |
| Implementation completeness | **partial (symbol not function)** | plastic binder + InfoNCE + P0 curriculum WIRED but **does not converge** (loss ~= chance log(64)) |
| Environment adequacy | **inadequate** | near-collinear consecutive latents -> InfoNCE positives not separable from negatives (carried + sharpened from 641a/720 "no binding pressure" note) |
| Measurement adequacy | **VACUOUS readiness gate** | precondition `learned_binder_trained` checks `n_learn_steps > 1` (curriculum FIRED) not loss convergence -> passes on an untrained binder |
| Integration / scale | n/a | harness-level read; no ree_core selection wiring |

**Recommended epistemic_category:** `untrained_substrate_artifact` (a precondition-unmet-in-substance) -- **NOT `substrate_ceiling`**. The 725 result is uninterpretable as a verdict on learned binding because the binder never learned. This is the 642 / 719a family: a substrate self-routes a scientific verdict on a substrate that was never actually trained, because the readiness gate that should have caught it is vacuous.

## 6. Adjudication (user scientific judgment, 2026-07-09)

Presented: the SPEC 3/6 -> 0/6 regression, the InfoNCE-at-chance evidence (`binder_last_loss` 3.75-3.96 vs chance ~4.16), the vacuous `learned_binder_trained` precondition, the contamination of the rebinding PASS, and the routing options. **User selected:**

- **Diagnosis: "Accept -- untrained-binder artifact."** The SPEC 0/6 AND the rebinding PASS are a vacuous-precondition artifact: the learned binder never converged, so 725 did **not** actually test a learned binder. `epistemic_category = untrained_substrate_artifact` (not substrate_ceiling). Nothing weakened; both 2026-04-23 intakes stay OPEN.
- **Routing: `implement-substrate` NOW + a GATED 725a retest.** Repair the learned-binder convergence first; only then re-test, with a hard convergence precondition. Refuse a naive 725b that reruns the same non-converging curriculum.

**Consequence for the lineage (governance MUST record this):** the 720 "learned binder is the residual prerequisite" hypothesis is **UNTESTED, not refuted.** 725 must NOT be read as falsifying learned binding or as a further substrate ceiling. The lineage's open question is unchanged; what 725 discovered is that the learned-binder substrate is *built but non-functional*.

**The rebinding PASS is also vacuous.** `rebinding_probe` argmaxes a bilinear form `<phi_self, phi_world>` over near-random (untrained) projections, so a large anchor perturbation flips the argmax trivially (1387 rebinds). It demonstrates the probe *mechanically fires* -- a genuine advance in instrument availability vs the fixed field -- but NOT that *meaningful bindings rebind*. Rebinding is only interpretable once the binder converges; the binding intake stays OPEN on the rebinding axis.

## 7. Learning extracted

1. **The learned-binder substrate is built but non-functional.** InfoNCE loss sits at chance (~log(64)=4.16; observed 3.75-3.96) after 487-1760 steps, flat and non-monotone in step count. The P0 contrastive task is unlearnable in the slow-drift gridworld (positives not separable from negatives). This is the actionable finding -- the run is contributory as a *substrate diagnostic*, not as a coherence verdict.
2. **The `learned_binder_trained` precondition is vacuous.** It gates on `n_learn_steps > 1` (curriculum fired), not on loss convergence, so it green-lit a scientific verdict on an untrained binder -- the 642/719a signature. Any learned-binder retest MUST gate on convergence (loss < k*log(batch)).
3. **A near-random plastic coupling is *worse* than a structured fixed field** for coherence-specificity (SPEC 3/6 -> 0/6): an unconverged binder injects noise that destroys the partial specificity the deterministic joint-state field provided. Plasticity only helps once it has trained.
4. **The 720 learned-binder hypothesis remains open.** It has been neither confirmed nor refuted; the substrate that was supposed to test it did not train.

## 8. Repair pathway / routing

**Routing: `implement-substrate` -> amend `cross_stream_binding_substrate`** (repair the learned-binder P0 convergence). See the JSON `recommended_substrate_queue_entry` (action=amend). The build work:
1. **Diagnose the InfoNCE degeneracy** (why positives aren't separable): most likely near-collinear z_self/z_world across ticks. Candidate fixes -- construct positives from *causally-linked* self/world conjunctions rather than raw within-tick pairs; add environment binding-pressure (multi-object / bipartite-reef conjunctions the reef layout already supports); raise `bind_dim` / `lr`, lower `temperature`, lengthen the P0 budget; or add hard-negative mining. Feasibility of separability should be checked with a tiny convergence probe before committing the full build.
2. **Expose a convergence statistic** the substrate reports (e.g. `binder_converged = last_loss < CONV_FRAC * log(batch)`) so a retest can gate on it.
3. Flip the substrate_queue status from `implemented` to reflect *implemented-but-non-functional* (learned binder does not converge); keep `pending_retest_after_substrate` true.

**Then queue 725a via `/queue-experiment`** (same 641a harness on the repaired binder) with a **HARD `learned_binder_converged` precondition** (loss < k*log(batch)) *replacing* the vacuous `learned_binder_trained` steps-check. If the repaired binder still cannot converge, that itself becomes an environment-adequacy verdict (route back to autopsy), not a coherence verdict.

**REFUSED:** a naive **725b** that reruns the *same* non-converging P0 curriculum on the *same* substrate (would circle the same untrained-binder artifact). The re-derive brake does **not** formally fire (`claim_ids=[]`; and the substrate is genuinely being enriched -- unbound -> fixed -> learned, now learned-that-actually-trains), but the naive-rerun refusal is applied on its own merits: do not re-measure until the binder demonstrably converges. `/queue-experiment` Step 2.5 (consumer half) should refuse 725a until the substrate exposes `binder_converged=True`.

**Not `/claim-synthesis`:** the failure signature is *consistent* (SPEC fails) across a *progressing* substrate; this is substrate-progression, not granularity debt (a coarse claim would show *structurally different* signatures per iteration). Same reasoning as 720.

**Intakes:** `thought_intake_2026-04-23_binding.md` and `thought_intake_2026-04-23_path_integral_constraints_search.md` stay **OPEN** -- gated on a learned binder that actually converges. The binding intake's rebinding axis stays open (the rebinding PASS is instrument-mechanical, not a meaningful-binding verdict).

## 9. Draft governance writes (do NOT apply here; /governance owns them)

- **substrate_queue.json:** amend `cross_stream_binding_substrate` per the JSON `recommended_substrate_queue_entry` (action=amend): add the 725 failure record; add the convergence-repair next-step + `binder_converged` stat requirement; note status is *implemented-but-non-functional* (learned binder does not train); `pending_retest_after_substrate` stays true; retest gated on convergence.
- **manifest evidence_direction:** leave `non_contributory` (correct for a diagnostic; no supersede -- 725 does not supersede 641a/720).
- **review_tracker.json:** mark run reviewed; regenerate pending_review -> 0.
- **Optional light bears-on note (non-status-changing) for MECH-270** (draft): *"V3-EXQ-725 (2026-07-09, diagnostic, non_contributory): the LEARNED (plastic) cross-stream binder built to test the 720 residual-prerequisite hypothesis did NOT converge -- InfoNCE loss stayed at chance (~log(64)=4.16; observed 3.75-3.96) in CausalGridWorldV2 (slow-drift latents -> non-separable contrastive positives). Coherence-specificity regressed 3/6 (720 fixed field) -> 0/6, an untrained-binder artifact, NOT a verdict on learned binding-by-synchrony. The learned-binder-as-prerequisite hypothesis remains UNTESTED. Not a status change."* Apply only if governance wants the refinement recorded on MECH-270; the primary landing is the substrate_queue amend.
