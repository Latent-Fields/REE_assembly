# Failure Autopsy -- V3-EXQ-641a (coherence-ablation REDESIGN, supersedes V3-EXQ-641)

- **Generated (UTC):** 2026-06-06T09:56:59Z
- **Scope:** single (diagnostic)
- **Status:** confirmed
- **Run:** `v3_exq_641a_coherence_ablation_nonreducibility_20260606T092011Z_v3`
- **Queue:** V3-EXQ-641a
- **experiment_purpose:** diagnostic -- `claim_ids: []`, `evidence_direction: non_contributory` (not weighted in confidence/conflict)
- **Bears on (cited, NOT tagged):** INV-002 (coherence includes temporal/phase binding), ARC-018 (rollout viability mapping), MECH-061 (commitment boundary), MECH-269 (per-stream verisimilitude), MECH-270 (ephaptic coupling)
- **Settles (gated):** `thought_intake_2026-04-23_binding.md`, `thought_intake_2026-04-23_path_integral_constraints_search.md`

## 1. The question (unchanged from 641 / both intakes)

Is the coherence term C(tau) **non-reducible** to the integrated prediction error E(tau)? I.e. does a coherence term in the selection rule change WHICH trajectory/binding is selected, in a **coherence-specific** way (not reproducible by a contrast-matched control), independently of prediction-error magnitude?

## 2. Facts reconstruction (ran to completion -- 18/18 runs, 6 seeds)

This iteration fixed all three confounds the 641 autopsy confirmed (user selected all three levers): **L1** E-orthogonalized cross-stream-only coherence read (641's temporal-smoothness term dropped; it leaked E) + **contrast-matched shuffle-of-real-C control** (replacing 641's high-contrast uniform-random that won SPEC by contrast not structure); **L2** divergence measured on two-mode-active gated P1 steps, 6 seeds; **L3** rebind perturbation mag 0.5 + tie-tick boost.

| Gate | Tests | Threshold | Result |
|---|---|---|---|
| D1 -- gated behavioural divergence | coherence changes selection | >= 0.05 frac, >= 4/6 seeds | **6/6 PASS** |
| D3 -- corr(E, C) < 0.9 | C not a *linear* function of E | abs corr < 0.9, >= 4/6 | **6/6 PASS** (max 0.711) |
| **SPEC -- real C diverges > shuffle** | the *structure* of C carries selection info beyond E | margin >= 0.05, >= 4/6 | **1/6 FAIL** (only seed 46) |
| rebind sub-signal (non-gating) | binding intake's own falsifier | n_rebind > 0 | **0/6** (perturb + tie-tick) |

Per-seed (real_C_clean): in **4 of 6 seeds the contrast-matched shuffle diverged MORE than real C** -- seed 47: real 0.076 vs shuffle 0.651; seed 45: 0.374 vs 0.643; seed 44: 0.115 vs 0.317; seed 43: 0.220 vs 0.518. Only seed 46 (0.871 vs 0.750) was coherence-specific.

**majority_label (self-route):** `C_changes_selection_specificity_unproven_route_followup` -- routes to this autopsy. Confirmed not a crash; correct skill.

## 3. The D3-vs-SPEC nuance (load-bearing)

D3 *passes* -- C is not a linear function of E. But D3 only checks rank-correlation; it is a weak operationalization of "non-reducible." SPEC is the real non-reducibility test ("does the *structure* of C matter for selection?"), and it **fails under a fair control**. Conclusion: in the current V3 substrate, C is statistically non-linear-in-E yet **functionally redundant** with E for selection. The divergence at D1 is driven by the authority-gain *injection*, not by the structure of the coherence signal; real C is, if anything, slightly less perturbative because it tracks E more closely.

## 4. Biological-reference triage

- **Closest mechanism:** binding-by-synchrony / communication-through-coherence (Fries), theta-gamma binding. Already instantiated in REE via MECH-089 (theta-gamma nesting packages E1 for E3), MECH-094 (hypothesis-tag write gate), MECH-270 (ephaptic coupling).
- **Existence proof for the CLASS, not this implementation.** REE already performs coherence-gated selection through E-based scoring. The candidate Q-claim asserts coherence as a **separable, non-reducible** factor -- which is exactly what SPEC tested and (under a fair control) rejected.
- **Missing-dependency signature?** Yes. In real brains, binding-by-synchrony operates on streams that are *genuinely bound* (theta-gamma nesting actually carries co-varying information). The V3 cross-streams (`world_states`, `states`) need not carry bound information at the granularity the coherence read assumes. The SPEC failure matches what would happen biologically if the **bound-representation prerequisite were absent**: the read has the *symbol* of cross-stream coherence but the streams do not carry the *functional* binding.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a (diagnostic, no tagged claim) | candidate Q `entities/selection.coherence_nonreducibility` does NOT gain support -> do not register |
| Biological reference | clear (for the class) | REE already owns coherence-gated selection; *separable-factor* version is structural-analogy in this substrate |
| Prerequisites / dependency | **missing** | `world_states`<->`states` streams not demonstrated to carry genuinely bound info; depends_on MECH-089 / MECH-094 / MECH-270 binding mechanisms |
| Implementation completeness | complete & fair | harness ablation, no ree_core mod; redesign correctly closed 641's confounds -- the FAIL is trustworthy |
| Environment adequacy | possibly inadequate | CausalGridWorldV2 may not generate the binding pressure that would make cross-stream coherence informative |
| Measurement adequacy | divergence axis OK; **rebinding axis UNDER-instrumented** | n_rebind=0 on all 6 seeds despite mag 0.5 + tie-boost |
| Integration / scale | n/a | harness-level read |

**Recommended epistemic_category:** `substrate_ceiling`.

## 6. Adjudication (user scientific judgment, 2026-06-06)

The autopsy presented two live readings of the fair-control SPEC failure: (1) CLOSE both intakes as structural-analogy-no-mechanism; (2) substrate-ceiling + retest. **User selected (2) substrate-ceiling + retest** for the divergence axis, and **queue a substrate-level rebind probe** for the rebinding axis.

Rationale (brain-as-existence-proof default): the mechanism class is real; the SPEC failure is most parsimoniously read as the V3 streams not carrying genuinely bound information, so the test could not let cross-stream coherence express itself. This is a translation/prerequisite gap, not a falsification.

### Routing

- **Divergence axis -> `implement-substrate`.** Both intakes stay **OPEN**, gated on a new **bound-multi-stream representation substrate** (recommended_substrate_queue_entry, action=create). The candidate Q-claim is NOT registered (no fair-control specificity yet). Pair with `pending_retest_after_substrate`. The 641a retest (same harness, fair control) is gated on that substrate landing.
- **Rebinding axis -> `/queue-experiment`.** n_rebind=0 on all 6 seeds despite mag 0.5 + tie-boost means the binding intake's own falsifier was never exercised. The binding intake stays open on the rebinding axis; route a **substrate-level rebind probe** (escalated perturbation and/or a probe that directly forces a cross-stream rebinding event), itself gated on the bound-stream substrate so the probe is meaningful.

### Learning extracted

1. D3 (rank-correlation < 0.9) is a weak non-reducibility test; SPEC (contrast-matched structure) is the load-bearing one. Statistical non-linearity in E != functional non-reducibility.
2. With a fair control, a coherence *read* over unbound streams is functionally redundant with E -- "coherence changes selection" (D1) is an authority-gain artifact, not evidence of a separable factor.
3. The binding question is **substrate-gated**: it cannot be decided until the substrate carries genuinely bound multi-stream representations. Both 2026-04-23 intakes are blocked on that, not on test design.
4. The rebinding falsifier remains un-exercised (n_rebind=0); the binding intake's strongest discriminator needs a substrate-level instrument.

## 7. Draft `evidence_quality_note` (governance to apply to the two intake docs / candidate Q entry -- NOT written here)

> V3-EXQ-641a (diagnostic, supersedes 641) ran the redesigned best-chance test (E-orthogonalized cross-stream-only coherence read, contrast-matched shuffle-of-real-C control, two-mode-gated divergence, 6 seeds, gap-relative authority). D1 (coherence changes selection) 6/6 and D3 (corr(E,C)<0.9) 6/6, but coherence-SPECIFICITY 1/6 (need 4): with a fair control the shuffle diverged >= real in 4/6 seeds, so C's structure is functionally redundant with E for selection in the current V3 substrate. Adjudicated (failure_autopsy_V3-EXQ-641a_2026-06-06) as substrate-ceiling, not falsification: the world_states<->states streams do not carry genuinely bound information, so the test could not let cross-stream coherence express itself. Both intakes (binding, path_integral) stay OPEN, gated on a bound-multi-stream substrate (recommended_substrate_queue_entry: create). Candidate Q entities/selection.coherence_nonreducibility NOT registered. Rebinding axis under-instrumented (n_rebind=0 on all 6 seeds despite mag 0.5 + tie-boost) -> binding intake stays open on the rebinding axis; route a substrate-level rebind probe. pending_retest_after_substrate.
