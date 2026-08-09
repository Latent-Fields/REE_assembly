# Failure Autopsy — V3-EXQ-228b (ARC-032 theta-bypass ablation, onboarded substrate)

**Generated:** 2026-08-09T05:43:28Z
**Scope:** single
**Status:** confirmed (interactive gate run 2026-08-09 — presented as low-controversy, no reversal of a strong filed verdict; manifest's own `decision: inconclusive` refined, not overturned)

## 1. Facts

Manifest `v3_exq_228b_arc032_theta_bypass_onboarded_20260809T030541Z_v3`, `supersedes: V3-EXQ-228a`, `claim_ids: ['ARC-032']`, `evidence_direction: does_not_support` (filed), `decision: inconclusive` (filed). Real run (13,292s elapsed, `ree-worker-3`, 3 seeds, full `scaffolded_sd054_onboarding` FULL curriculum).

This is the **first time ARC-032's theta-bypass ablation has ever been fairly tested** — predecessors V3-EXQ-228a (goal_norm ~0.031) and V3-EXQ-247 (goal_norm=0.0) both failed their own non-degeneracy precondition on the old `causal_grid_world` substrate + simplified warmup.

| Gate | Frac seeds | Pass |
|---|---|---|
| Precondition (goal_norm >= 0.05) | **1.00** | **True** — first time ever |
| C1 (main): resource_visit_rate lift >= 0.05 | 0.00 | False |
| C2 (info): harm ratio <= 1.5x | 1.00 | True |

Per-seed lift (ACTIVE - ZEROED), all three seeds same sign: seed 42 -0.00236 (2.25x ratio), seed 43 -0.00116 (1.64x), seed 45 -0.00283 (2.70x) — small in absolute terms but consistently reversed from ARC-032's prediction. Patch confirmed non-inert (smoke-test harm_rate divergence, plus the full run's own confirmed non-degeneracy).

**Measurement-adequacy finding**: `generate_trajectories()` only regenerates candidates from a fresh theta summary at `e3_tick` rate — MECH-089's own EXQ-052b measurement puts that at `e3_tick_ratio ~= 0.109`, i.e. ~1 in 9 steps. The remaining ~89% of a 200-step episode reuses cached candidates unaffected by the ablation, diluting any theta-specific behavioral signal roughly 9x in a full-episode aggregate. The driver also measures only a downstream behavioral proxy (resource_visit_rate/harm_rate); it never computes the readouts claims.yaml's own CONFIRMING criterion names as decisive (z_goal persistence, goal-proximity-score noise in E3's trajectory candidates).

Dry-run check: clean.

## 2. Claim-layer mapping

ARC-032 (`candidate`, `substrate_conditional`, `depends_on: [MECH-089, MECH-116]`). Claims.yaml's `what_would_answer` (updated 2026-08-08, same day 228b was authored) pre-registers almost exactly this test — CONFIRMING names three readouts (z_goal persistence, trajectory-scoring noise, behavioral lift); FALSIFYING is "lift ~ 0, no separation across seeds," which 228b's C1 result (lift_mean=-0.0021, all seeds near zero) near-verbatim matches. **228b operationalizes only the behavioral-lift readout (c) of the three CONFIRMING criteria** — this is the crux of the measurement-adequacy finding below.

## 3. Biological-reference triage

Strong, dedicated lit base: `evidence/literature/targeted_review_arc_032/` (7 entries, mean confidence high-0.7s: Benchenane 2010, Hyman 2010, Sigurdsson 2010, Jones & Wilson 2005, Colgin 2016, Dragoi 2006, Pfeiffer 2013). Not a formal-definition import; no `/lit-pull` owed.

Sigurdsson et al. 2010 (disruption of hippocampal-prefrontal theta coherence causally impairs goal-directed navigation) predicts degradation, not a null/reversed effect, on ablation. **Where REE diverges**: `ThetaBuffer.summary()` is a flat, unweighted mean over a fixed 10-step window — a rate-reduction filter carrying no phase/sequence-order information, whereas the deeper literature (Dragoi 2006 theta-sequence compression, Colgin 2016 theta-gamma nesting) attributes theta's functional payload specifically to sequence-order encoding, not temporal averaging. MECH-089's own `what_would_answer` states this translation choice explicitly. **This null result independently converges with MECH-089's own already-confirmed, adverse finding**: "uniform static-k theta batching is CONFIRMED HARMFUL for harm attribution (EXQ-066: batched error 2.28x worse than raw; EXQ-122: harm_auc delta=-0.135 adverse direction)." Not a novel anomaly — a second line of evidence for the same static-averaging limitation.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened, with a measurement caveat | claim's own pre-registered FALSIFYING criterion literally matched, but only 1 of 3 named CONFIRMING readouts was measured |
| Biological reference | clear, implementation diverges | Sigurdsson's disruption analog predicts degradation; REE's flat-mean implementation captures theta's rate-reduction role, not its phase/sequence-order role |
| Dependency prerequisites | present | precondition cleared for the first time (1.00 frac seeds, mean 0.469) |
| Implementation completeness | partial — symbol vs functional role | rate-reduction/batching analog complete; sequence/order-encoding analog absent by design |
| Environment adequacy | adequate | 866a-validated P2 env, reasonable window for an aggregate readout in isolation |
| Measurement adequacy | under-instrumented — the central finding | E3-tick cache-gating dilutes any theta-specific signal ~9x in a full-episode aggregate; the claim's own named CONFIRMING readouts (persistence, scoring-noise) were never directly measured |
| Integration adequacy | coupled, confirmed non-inert | theta summary genuinely threaded into `hippocampal.propose_trajectories`; smoke + full-run confirm the patch is live |
| Scale/capacity | adequate | full curriculum budgets, 3 seeds, standard P2 measurement volume |

## 5. Learning extracted

1. 228b is the first ARC-032-tagged run to clear the non-degeneracy precondition — confirms `scaffolded_sd054_onboarding` is a viable substrate for this claim family going forward.
2. Theta-patch confirmed genuinely wired into trajectory candidate generation and confirmed non-inert at both smoke and full scale.
3. C1 shows no positive effect and a small but seed-consistent reversed-direction trend.
4. `generate_trajectories()` only regenerates candidates from a fresh theta summary at E3-tick rate (~11% of steps) — a structural dilution factor for any full-episode aggregate readout, worth citing whenever this substrate's theta pathway is behaviorally tested.
5. MECH-089's own EXQ-066/EXQ-122 findings independently converge with this null — the likely locus of the gap is the flat-mean implementation of "theta packaging," not the frontal-hippocampal-synchrony hypothesis itself.
6. claims.yaml's ARC-032 CONFIRMING criterion names z_goal persistence and goal-proximity-score noise as decisive readouts; the driver measures neither directly.

## 6. Routing (confirmed)

`epistemic_category: measurement_test_design_defect` (not `substrate_ceiling` — nothing suggests the substrate can't express the effect; not `precondition_unmet` — the precondition passed cleanly for the first time). `evidence_direction: does_not_support` (confirmed as filed, refined with the measurement caveat above — not accepted as a stable terminal read). Routing: `/queue-experiment`, same-question redesign (alphabetic suffix, V3-EXQ-228c) — measure at E3-tick granularity (or restrict to ticks where `e3_tick` actually fired), add direct persistence/proximity-noise readouts, register the consistent reversed-direction trend as a finding to investigate rather than dismiss, cite MECH-089's EXQ-066/EXQ-122 explicitly in the redesign note. `recommended_substrate_queue_entry.action: none` — ThetaBuffer, E3-tick gating, and the propose_trajectories wiring are already fully built and functioning as designed; this is a measurement-design gap on top of complete substrate.

**Step 9b**: no existing hypothesis-space qid names ARC-032; no `fanout_recommendation` emitted. Registration deferred.

## 7. Evidence quality note (for governance to apply)

> V3-EXQ-228b FAIL/does_not_support (2026-08-09): first genuine test of ARC-032 with the non-degeneracy precondition met (goal_norm 1.00 frac seeds, mean 0.469 -- cleared for the first time across the whole 076/228/247/228a/228b lineage). C1 (resource-collection lift) failed 0/3 seeds; lift_mean=-0.0021 (~0 in absolute terms, but consistently negative -- i.e. reversed from prediction -- across all 3 seeds, ZEROED collecting 1.6-2.7x ACTIVE's resource-visit rate). C2 (harm parity) passed cleanly. Patch confirmed non-inert (smoke + full-run harm_rate divergence). NOT treated as falsifying: (a) the E3-tick cache-gating this substrate already documents (MECH-089 EXQ-052b: e3_tick_ratio ~0.109) means ~89% of the measured episode steps reuse cached trajectory candidates unaffected by the ablation, diluting any theta-specific effect in a full-episode aggregate; (b) the driver measures only a downstream behavioral proxy, never the z_goal-persistence / goal-proximity-score-noise readouts ARC-032's own CONFIRMING criterion names. Converges with MECH-089's own already-confirmed finding that static/uniform theta-averaging measurably hurts (not helps) E3's fine-grained discrimination (EXQ-066, EXQ-122) -- consistent reading, not a novel anomaly. Routed to /queue-experiment for a tick-granularity, persistence/noise-metric redesign (V3-EXQ-228c), not to demotion. epistemic_category: measurement_test_design_defect.
