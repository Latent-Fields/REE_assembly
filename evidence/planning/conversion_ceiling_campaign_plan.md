---
closure_plan:
  id: conversion_ceiling_campaign
  title: "Conversion-Ceiling Campaign (prong-map / parallel multi-face)"
  registered: 2026-06-22
  last_updated: 2026-06-22
  scope_claims: [MECH-439, MECH-309, ARC-062, MECH-445, MECH-446, MECH-448, MECH-449, SD-033b, MECH-263, ARC-107]
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
      phase: "The live V3 critical path post-689c, and the most likely true bottleneck (commit-duration, not selection). Rung-6 de-commit lever PARKED 2026-06-22 (460h/i/j; the F-driven natural-commit latch ~2400-2600 steps swamps the SD-034 closure de-commit, and natural-commit/closure-de-commit were non-dissociable so the lever was untestable). The named upstream substrate is now BUILT: the closure-exclusive de-commit eval mode (beta elevates only via _closure_commit_active during the eval, so occupancy forms independently of the closure plane) landed ree-v3 main e52158d 2026-06-22 (substrate_queue rung-6 PARKED -> BUILT). The validation successor V3-EXQ-460k was queued + ingested 2026-06-22 (ree-v3 main 979a943; supersedes 460j) and awaits run."
      status: assembling
      severity: load-bearing
      awaiting: "V3-EXQ-460k run result (on the BUILT closure-exclusive de-commit eval substrate)"
      assembly_status: queued
      revisit_after: 2026-07-15
      owner_exq: "V3-EXQ-460k (queued 2026-06-22; awaiting run on the BUILT closure-exclusive de-commit eval substrate)"
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
