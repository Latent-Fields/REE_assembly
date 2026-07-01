---
closure_plan:
  id: conversion_ceiling_campaign
  title: "Conversion-Ceiling Campaign (prong-map / parallel multi-face)"
  registered: 2026-06-22
  last_updated: 2026-07-01
  scope_claims: [MECH-439, MECH-309, ARC-062, MECH-445, MECH-446, MECH-448, MECH-449, SD-033b, MECH-263, ARC-107, ARC-108, MECH-450]
  sibling_plans: [behavioral_diversity_isolation, arc_062_rule_apprehension, commitment_closure, sd033_governance]
  pattern: prong_map_pattern.md
  instance_map: conversion_ceiling_prong_map.md
  nodes:
    - id: "conversion_ceiling_campaign:CAMPAIGN"
      title: "Umbrella: assemble the multi-face substrate that converts per-candidate diversity to committed-class diversity"
      phase: "Selection face exhausted lever-by-lever (Factor A inert 689a; Factor B REFUTED 689c; demotion 654i and Go/No-Go 654j each fail C2 alone). Per assembly-vs-closure, the real test is the co-armed FULL-STACK arm, not another isolated falsifier. Three live prongs assembling in parallel (P-comp selection composition, P2 root-C commit-duration, P3 OFC valuation); full-stack arm assembled once all three are composition-ready."
      status: assembling
      severity: load-bearing
      awaiting: "P-comp + P2 + P3 composition-readiness"
      assembly_status: in_progress
      owner_exq: "null -- umbrella; owned via child prong nodes"
    - id: "conversion_ceiling_campaign:P-comp"
      title: "Selection-face composition: does MECH-448 demotion x MECH-449 Go/No-Go compound or cancel at committed-class entropy (C2)?"
      phase: "The within-selection-face interaction-characterization gate (own experiment, user-decided 2026-06-22). Both levers face-validated alone (689d, 689g) but each fails C2 alone (654i, 654j). Factor A x Factor B cancelled (689a) -- demotion x Go/No-Go interaction is UNKNOWN and must be measured before co-arming the full stack. Runnable NOW (uses only built + face-validated levers). NOT another GAP-B same-lever letter -- it tests the composition, a different question."
      status: assembling
      severity: load-bearing
      awaiting: "demotion x Go/No-Go composition falsifier (to queue via /queue-experiment)"
      assembly_status: queued
      owner_exq: "V3-EXQ-699 (queued 2026-06-22; awaiting run)"
    - id: "conversion_ceiling_campaign:P2-rootC"
      title: "Commit-duration face (root C, MECH-445/446): de-commit authority on a substrate where natural-commit and closure-de-commit are dissociable"
      phase: "The live V3 critical path post-689c. Rung-6 de-commit lever PARKED 2026-06-22 (460h/i/j; the F-driven natural-commit latch ~2400-2600 steps swamps the SD-034 closure de-commit, and natural-commit/closure-de-commit were non-dissociable so the lever was untestable). The closure-exclusive de-commit eval mode was BUILT ree-v3 main e52158d 2026-06-22. BUT both successors RAN terminal FAIL/non_contributory: V3-EXQ-460k (rung-6 duration lever; concurrent failure-autopsy-460k 2026-06-22) and its JOB-2 control-plane successor V3-EXQ-460l (rho_t maintenance ramp + habenula de-commit DRIVER pair; confirmed failure_autopsy_V3-EXQ-460l_2026-06-23) BOTH self-routed substrate_not_ready_requeue at the same gate: the closure-exclusive eval mode does NOT arm the closure-coupled latch-hold in a real eval (ncl_hold_closure_armed_total=0 on every arm/seed) because _closure_commit_active is structurally gated on the F-driven e3._committed_trajectory. On the 603n foraging substrate no sustained monolithic hold forms at all -- so the commit-DURATION face is not even the exercisable constraint here; the binding constraint is upstream at commit-ENTRY / sustained-occupancy formation (the F-dominance selection face, MECH-439). Re-derive brake FIRED (5th lineage autopsy 460h..460l) -> the next step is /implement-substrate (amend f_dominance_conversion_ceiling: decouple closure-coupled hold-arming from the F-driven natural commit), NOT another 460-letter. The duration face remains downstream of, and gated by, the selection face."
      status: assembling
      severity: load-bearing
      awaiting: "/implement-substrate amend f_dominance_conversion_ceiling -- F-independent closure-coupled-hold arming (so a hold arms+sustains independently of the F-driven natural commit; the prerequisite 460k/460l both lacked). Until then the commit-duration face is untestable and is subordinate to the upstream commit-entry F-dominance face."
      assembly_status: queued
      revisit_after: 2026-07-15
      owner_exq: "V3-EXQ-460l (SUPERSEDES 460k; RAN terminal FAIL/non_contributory 2026-06-22T22:17:57Z; confirmed failure_autopsy_V3-EXQ-460l_2026-06-23 -- substrate_not_ready_requeue, closure-coupled hold never armed; re-derive brake FIRED -> implement-substrate amend f_dominance_conversion_ceiling, REFUSE a 460m re-queue). Build the F-independent closure-coupled-hold arming substrate next; the validation re-test follows the build."
    - id: "conversion_ceiling_campaign:P3-ofc"
      title: "Valuation face (SD-033b/MECH-263): decoupled OFC devaluation head feeding F"
      phase: "FACE-VALIDATED -> composition-ready for the full-stack arm. V3-EXQ-485m RAN terminal FAIL/non_contributory 2026-06-22T14:33Z (run_id v3_exq_485m_sd033b_devaluation_decoupled_head_behavioural; applied via the CONFIRMED failure_autopsy_V3-EXQ-485m_2026-06-22, governance master f8a55e4525). On the BUILT decoupled devaluation_bias_head (ree-v3 758956f) the 485l clamp-starvation is FIXED -- C1 devaluation shift 3/3, MECH-449 No-Go 2/3, devalued bias range supra-floor 3/3 (the OFC valuation mechanism is EXERCISED, not falsified) -- but the behavioural C1b vector-inversion (1/3) and C2 committed-class separation (1/3) still fail standalone. That is exactly the conversion-ceiling signature the full-stack arm exists to break: the OFC face is validated for inclusion in FULLSTACK with use_ofc_devaluation_head ON. PROMOTES NOTHING."
      status: assembling
      severity: medium
      awaiting: "composition into the full-stack arm (with P-comp + P2-rootC composition-ready)"
      assembly_status: built
      owner_exq: "V3-EXQ-485m (RAN terminal FAIL/non_contributory 2026-06-22; OFC face FACE-VALIDATED -> composition-ready for FULLSTACK with use_ofc_devaluation_head ON)"
    - id: "conversion_ceiling_campaign:FULLSTACK"
      title: "The real test: co-armed full-stack arm (demotion + Go/No-Go + floor + root-C + OFC ON), sweep use_candidate_rule_field, DV committed-class entropy"
      phase: "Assembled once P-comp + P2 + P3 are composition-ready (each lever no-op-default + own-face-validated + interaction-characterized). Factor B EXCLUDED (refuted 689c). Per-prong baseline discipline: composite carries its own dedicated all-stack-ON / swept-var-OFF control (no shared frozen baseline). PASS -> assembled substrate converts -> supports MECH-309/ARC-062, closes behavioral_diversity_isolation:GAP-I. FAIL -> leave-one-out ablation to localize the blocking face."
      status: assembling
      severity: load-bearing
      awaiting: "P-comp + P2 + P3 composition-ready"
      assembly_status: queued
      owner_exq: "null -- composite, gated on child prongs"
      cross_plan_link: ["behavioral_diversity_isolation:GAP-I"]
    - id: "conversion_ceiling_campaign:P4-learned-gating"
      title: "Learned-gating face (ARC-108 / MECH-450): make the ARC-107 arithmetic BG arbitration LEARNABLE. The selection face was not 'exhausted lever-by-lever' -- it was never given learned parameters; ARC-108 adds the dopamine-into-gating learning afferent (learned w_chan) + MECH-450 a bounded recurrent settling step replacing the one-shot pallidal argmin."
      phase: "Registered 2026-06-23 as the 4th live campaign face. The selection-face prongs (P-comp, demotion 654i, Go/No-Go 654j) all act on a FIXED arithmetic arbitration; ARC-108's thesis is that the arbitration layer has NO learned parameters, so MECH-439's F-monopoly was never made adaptable. Falsifiers V3-EXQ-700 (sec-7 learned-gating 2x2: does ARC-108+MECH-450 resolve MECH-439 on the COLLAPSED arena?) + V3-EXQ-700a (C3 signed-vs-unsigned-RPE ablation); live letter is now the TERMINAL V3-EXQ-700c (CLAIMED/running 2026-06-24, supersedes the 700 -> 700a -> 700b lineage; failure_autopsy_V3-EXQ-700b_2026-06-24 is the routing record). MIRROR node: the build front is OWNED by behavioral_diversity_isolation:GAP-K (the GAP-J-successor build node) -- this prong gives the campaign prong-map its 4th face without duplicating ownership, exactly as biology_grounding_convergence_v4:BG-2 mirrors GAP-I/GAP-J. ARC-108 depends_on ARC-110 (segregated-loops sequencing fork; 700 is the explicit test of whether loop segregation is required)."
      status: assembling
      severity: load-bearing
      awaiting: "UPDATED 2026-07-01: the learned-gating stack is now BUILT end-to-end -- ARC-108 (learned w_chan) + MECH-450 (settling W_lat) + ARC-110 (segregated loops, 707b-validated live) + the ARC-108xARC-110 LEARNED CROSS-LOOP arbitration coupling (built 2026-07-01; config.e3.use_learned_cross_loop_arbitration). 707b confirmed the conversion ceiling INTRINSIC (not a single-arena artefact) and NARROWED the front to 'the cross-loop arbitration must be LEARNED, not static arithmetic'; that coupling is now built. Now awaiting the SEPARATE new-EXQ validation falsifier (A1_LOOPS + learned cross-loop arbitration STRICT-ABOVE A1_LOOPS + static arbitration; different claim_ids), queued via /queue-experiment as V3-EXQ-709 (2026-07-01, ree-v3 main 2a5e8a6, live in the coordinator DB pending a runner claim). Build owned by the mirror node behavioral_diversity_isolation:GAP-K."
      assembly_status: in_progress
      owner_exq: "null -- mirror prong; build owned by behavioral_diversity_isolation:GAP-K. The 700-lineage single-arena attack + the ARC-110 707b segregation validation both landed; the front advanced to the DA-gated cross-loop arbitration coupling, BUILT 2026-07-01. Validation owner (on the mirror node GAP-K) = V3-EXQ-709, the learned-cross-loop-arbitration validation falsifier (queued 2026-07-01, ree-v3 main 2a5e8a6, live in the coordinator DB pending a runner claim)."
      cross_plan_link: ["behavioral_diversity_isolation:GAP-K"]
      build_note_2026_07_01: "The ARC-108xARC-110 LEARNED CROSS-LOOP arbitration coupling -- the 707b-NARROW missing dependency (static-arithmetic cross-loop combine inherits F's dominance so the live limbic loop never wins) -- is BUILT (session learned-crossloop-arbitration-20260701T1840Z, /implement-substrate) behind no-op-default flag config.e3.use_learned_cross_loop_arbitration: a learned [3,3] cross-loop matrix W_cross = I + M_cross updated by the ARC-108 signed-RPE three-factor rule, coupled with MECH-450 settling. PROMOTES NOTHING (annotated on ARC-108 + ARC-110; no new claim per the 2026-06-29 MECH-439 /claim-synthesis DROP-MECH-453). status stays assembling (built substrate, conversion not yet demonstrated). Docs docs/architecture/learned_cross_loop_arbitration.md; ree-v3/CLAUDE.md. Owner build node GAP-K carries the full build_note_2026_07_01."
      reappointment_note_2026_06_24: "ARC-108 depends_on ARC-110 (the segregated-loops sequencing fork). ARC-110 + coupled ARC-109/MECH-452 were REAPPOINTED V4->V3 2026-06-24 (user-directed) because the loop-segregation build attacks MECH-439, this campaign's load-bearing blocker. The 700c-terminal escalation therefore routes to a V3 loop build GATED on V3-EXQ-704 (MECH-451), not a V4 hand-off. See sd_v4_loop_segregation.md (generation flipped V3) + substrate_queue v4_loop_segregation + behavioral_diversity_isolation:GAP-K (the build-owner node)."
---

# Conversion-Ceiling Campaign

This closure plan is the **assembly-frontier home** for the conversion-ceiling campaign. Its nodes are all `status: assembling` by design — they are required for v3 but actively under construction, so they sit on the assembly frontier (weight `None`, off the closure %) and rest in drift rather than nagging the green-board.

- **The pattern** it instantiates: [`prong_map_pattern.md`](prong_map_pattern.md).
- **The live campaign view** (prong inventory, composition matrix, full-stack spec, critical path): [`conversion_ceiling_prong_map.md`](conversion_ceiling_prong_map.md).
- **The lever inventory + metric trajectory**: the `f_dominance_conversion_ceiling` entry in `substrate_queue.json` (6-rung `fallback_ladder`; rung 6 = root C, tagged PARALLEL to the selection-face rungs).

## Node summary

| Node | Face | State | Runnable |
|---|---|---|---|
| `:CAMPAIGN` | umbrella | assembling | — |
| `:P-comp` | selection (demotion x Go/No-Go) | assembling / queued | **now** |
| `:P2-rootC` | commit-duration | assembling / build owed | needs substrate build |
| `:P3-ofc` | valuation | assembling / in_progress | 485m running |
| `:FULLSTACK` | composite | assembling / gated | after P-comp + P2 + P3 |

Factor B (gap-scaled commit-T) is **refuted** at the selection face (V3-EXQ-689c FAIL, 2026-06-21) and is **not** represented as a live node — it is dropped from the full-stack arm. See the prong map for the full rationale.
