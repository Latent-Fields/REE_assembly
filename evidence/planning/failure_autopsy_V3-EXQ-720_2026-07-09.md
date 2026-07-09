# Failure Autopsy -- V3-EXQ-720 (coherence non-reducibility RETEST on the bound substrate)

- **Generated (UTC):** 2026-07-09T06:30:24Z
- **Target run_id:** `v3_exq_720_coherence_nonreducibility_bound_substrate_20260709T023441Z_v3`
- **queue_id:** V3-EXQ-720  |  **machine:** ree-cloud-2
- **experiment_purpose:** diagnostic  |  **claim_ids:** [] (non_contributory; excluded from confidence / conflict scoring)
- **Outcome:** FAIL  |  **self-route (majority_label):** `C_changes_selection_specificity_unproven_route_followup`
- **Scope:** single (but the 3rd iteration in one lineage -- 641 -> 641a -> 720)
- **Status:** confirmed (user-adjudicated 2026-07-09)
- **Prior autopsies in lineage:** `failure_autopsy_V3-EXQ-641_2026-06-06`, `failure_autopsy_V3-EXQ-641a_2026-06-06`

---

## 1. The question (unchanged across the lineage)

Is the cross-stream coherence term C(tau) **non-reducible** to the integrated prediction-error cost E(tau)? I.e. does a coherence term in the selection rule change **which** trajectory is selected, in a **coherence-specific** way (not reproducible by a contrast-matched control), independently of prediction-error magnitude?

720 is a **retest of the 641a harness verbatim** (E-orthogonalized cross-stream-only phase-alignment read + shuffle-of-real-C contrast-matched control + two-mode-active gating + 6 seeds + L3 boosted rebind perturbation). The **only** change vs 641a: the agent is built with `cross_stream_binding_enabled=True, strength=0.5` -- the newly-landed `cross_stream_binding_substrate` (built 2026-07-08, session reverent-clarke-16000f). It does **not** supersede 641a (641a's substrate-ceiling finding on the *unbound* substrate stands).

## 2. Facts reconstruction (ran to completion -- 18/18 runs, 6 seeds [42-47], 3 conditions)

Substrate active and fair: `cross_stream_binding_active` precondition met (measured 0.5 > 0.0); `gating_denominator_adequate` met (min 504 gated steps > 20 floor); `gating_adequacy_warning=false`; all three criteria non-degenerate.

| Gate | Tests | Threshold | 641a | **720** |
|---|---|---|---|---|
| D1 -- gated behavioural divergence | coherence changes selection | >= 0.05 frac, >= 4/6 | 6/6 | **4/6** (seeds 44/47 low-flip: frac 0.005/0.021) |
| D3 -- abs corr(E, rawC) < 0.9 | C not a *linear* fn of E | < 0.9, >= 4/6 | 6/6 | **6/6** (max 0.68) |
| **SPEC -- real C diverges > shuffle** | *structure* of C carries info beyond E | margin >= 0.05, **>= 4/6** | **1/6** | **3/6 FAIL** |
| rebind sub-signal (non-gating) | binding intake's own falsifier | n_rebind > 0 | 0/6 | **0/6** (despite L3 mag 0.5 + tie-boost 1.0) |

**Per-seed SPEC (real_frac_state_div_gated vs shuffle):**
- seed 42: 0.913 vs 0.846 -> **specific**
- seed 43: 0.829 vs 0.968 -> not (shuffle higher)
- seed 44: **0.005** vs 0.727 -> not (real near-zero; shuffle high)
- seed 45: 0.923 vs 0.795 -> **specific**
- seed 46: 0.880 vs 0.788 -> **specific**
- seed 47: **0.021** vs 0.206 -> not (real near-zero)

`n_coherence_specific = 3`, `n_seed_pass = 3`, `min_seeds_for_pass = 4`. **Failed criterion: SPEC (load-bearing, discrimination).**

**The load-bearing signal (partial lift):** the fixed-field binder moved coherence-specificity **from 1/6 (641a, unbound) to 3/6 (720, bound)**. The substrate ceiling did not vanish -- it **moved**. Half the seeds now show real cross-stream coherence carrying selection information a shuffle destroys; the other half (notably 44/47, where real divergence collapses to ~0) do not.

## 3. Claim-layer mapping

Diagnostic, `claim_ids=[]` -> no tagged claim is weakened or strengthened. **Bears on** (cited, not tagged): INV-002 (coherence includes temporal/phase binding), MECH-089 (theta-gamma nesting), MECH-094 (write gate -- does not newly apply here), MECH-270 (ephaptic coupling -- the fixed-field binder is a MECH-270 instantiation), MECH-269 (per-stream verisimilitude). The candidate Q `entities/selection.coherence_nonreducibility` **does not reach the register threshold** (needs 4/6 SPEC) -> stays candidate/unregistered; **not** weakened (partial lift is directional support, not a null).

## 4. Biological-reference triage (the core move)

- **Closest mechanism:** binding-by-synchrony / communication-through-coherence (Fries), theta-gamma binding (Singer/Gray, Buzsaki theta-gamma code). Already partially instantiated in REE via MECH-089 / MECH-270.
- **Existence proof for the CLASS, not this implementation.** In brains, binding-by-synchrony operates on streams whose coupling is **learned / plastic** -- genuine cross-stream coherence carries conjunction-specific information *because the coupling was shaped by experience to make it informative*, which is exactly what a shuffle destroys.
- **Faithful translation vs formal/structural import:** the V3 binder (`ree_core/latent/cross_stream_binder.py`) installs a **FIXED (untrained) random-projection shared field** -- theta-gated, joint-state-derived, injected identically into both streams. Its own docstring (lines 25-31): *"A fixed, joint-state-dependent shared field is the minimal substrate that installs a genuine common cause -- the ephaptic-field analog (MECH-270)... A learned binder is a V4 extension, out of scope here."* So the substrate has the **symbol** of the mechanism (shared theta-gated field) but only the **partial functional role** (an unlearned field couples the streams, but nothing shapes the coupling so that *real* coherence is robustly more selection-informative than a contrast-matched shuffle).
- **Missing-dependency signature?** Yes, and it is now *sharper* than at 641a. At 641a the missing prerequisite was "bound representation" (absent -> SPEC 1/6). 720 supplied a fixed bound representation and lifted SPEC to 3/6. The **residual** missing prerequisite is **plasticity of the binder** -- exactly what would be missing biologically if you installed an unlearned ephaptic field: it creates correlation but does not make real coherence conjunction-specific. **This biology divergence is load-bearing, not a caveat to tune.**

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a (diagnostic, claim_ids=[]) | candidate Q coherence_nonreducibility does NOT reach register (needs 4/6); not weakened |
| Biological reference | clear (for the class) | binding-by-synchrony is **learned**; fixed random field is symbol-complete, function-partial |
| Prerequisites / dependency | **partially present** | bound representation now installed (SPEC 1/6->3/6); residual missing prerequisite = **plasticity / learned binder (V4)** |
| Implementation completeness | complete & fair | pre-registered strength 0.5, byte-identical OFF, smoke PASS; the FAIL is trustworthy |
| Environment adequacy | possibly inadequate | CausalGridWorldV2 may still not generate binding pressure (carried from 641a; seeds 44/47 zero-contact) |
| Measurement adequacy | divergence axis OK; **rebinding axis STILL under-instrumented** | n_rebind=0 on all seeds despite L3 boost -- 3rd run running; a fixed field cannot be perturbed *into* a rebind |
| Integration / scale | n/a | harness-level read; no ree_core selection wiring |

**Recommended epistemic_category:** `substrate_ceiling` -- a **partial-lift ceiling** (the ceiling moved from unbound to fixed-field-bound; the residual is the plasticity prerequisite).

## 6. Adjudication (user scientific judgment, 2026-07-09)

Presented: the partial-lift positive (1/6->3/6), the fixed->learned biology divergence, the four-layer table, and the routing options. **User selected:**
- **Routing: `implement-substrate` NOW** (active near-term V4 learned-binder build; **not** parked off the V3 critical path).
- **Rebinding axis: fold into the V4 learned-binder build** (a fixed field cannot be perturbed into a rebind; the rebinding instrument is a substrate-level probe to build alongside the learned binder -- do NOT spin a separate V3 instrument iteration).

Rationale (brain-as-existence-proof default): the mechanism class is real and the binding direction is now **directionally validated** by the partial lift; the residual SPEC gap is most parsimoniously a **plasticity prerequisite** (learned binder), not a falsification of separable coherence. Both 2026-04-23 intakes stay **OPEN** (the ambiguous partial-lift routes a followup; neither a clean register nor an F1/F2 close).

## 7. Learning extracted

1. **Positive / directional:** installing a genuine shared common cause between z_self and z_world lifted coherence-specificity from 1/6 (641a) to 3/6 (720). The cross-stream-binding hypothesis is directionally validated -- a partial lift, not a null.
2. **Fixed-field (untrained) binding is functionally insufficient** to clear the 4/6 SPEC gate. The missing prerequisite is a **learned (plastic) binder = V4**. Load-bearing biology divergence: binding-by-synchrony in brains is trained, not a fixed random field; the fixed ephaptic-field analog (MECH-270) is symbol-complete, function-partial.
3. **Rebinding falsifier still un-exercised** (`n_rebind=0` across 641/641a/720, now even at L3 boosted perturbation 0.5 / tie-tick 1.0). A fixed field cannot be perturbed *into* a competing-config overtake; the rebinding instrument is a substrate-level probe that belongs with the learned binder.

## 8. Repair pathway / routing

**Routing: `implement-substrate` -> amend `cross_stream_binding_substrate`** (V4 learned-binder enrichment; active near-term per user). See the JSON `recommended_substrate_queue_entry` for the structured hand-off (action=amend, +720 failure record, +learned-binder + rebinding-instrument next-step).

**REFUSED:** re-queuing the 641a harness on the **fixed-field** substrate (a strength-sweep "720b" would circle the same fixed-field ceiling -- the loop the re-derive brake exists to stop). A learned-binder build + retest is a genuine substrate enrichment and is allowed. The re-derive brake does **not** formally fire (claim_ids=[]; and the substrate was genuinely enriched between 641a->720, the brake's explicit exemption), but the fixed-field re-queue refusal is applied on its own merits.

**Not `/claim-synthesis`:** the failure signature is *consistent* (SPEC fails) across a *progressing* substrate (unbound 1/6 -> fixed 3/6). This is substrate-progression, not granularity debt (a claim too coarse would show *structurally different* failure signatures per iteration).

**Intakes:** `thought_intake_2026-04-23_binding.md` and `thought_intake_2026-04-23_path_integral_constraints_search.md` stay **OPEN**, gated on the learned-binder substrate. The binding intake's rebinding axis stays open on the instrument gap.

## 9. Draft governance writes (do NOT apply here; /governance owns them)

- **substrate_queue.json:** amend `cross_stream_binding_substrate` per the JSON `recommended_substrate_queue_entry` (fixed-field V3 build stays `implemented`; add the learned-binder V4 next-step + rebinding instrument; +720 failure record; pending_retest_after_substrate stays true).
- **manifest evidence_direction:** leave `non_contributory` (correct for a diagnostic; no supersede -- 720 does not supersede 641a).
- **review_tracker.json:** mark run reviewed; regenerate pending_review -> 0.
- **Optional light bears-on note (non-status-changing) for MECH-270** (draft): *"V3-EXQ-720 (2026-07-09, diagnostic, non_contributory): a FIXED-field ephaptic-analog cross-stream binder (cross_stream_binder.py, strength 0.5) lifted coherence-specificity from 1/6 (641a, unbound) to 3/6 seeds but did not clear the 4/6 SPEC gate. Directional support for the ephaptic-coupling class; refines the translation -- a fixed field is symbol-complete but function-partial, a LEARNED/plastic binder (V4) is the residual prerequisite for coherence-non-reducibility. Not a status change."* Apply only if governance wants the refinement recorded on MECH-270; the primary landing is the substrate_queue amend.
