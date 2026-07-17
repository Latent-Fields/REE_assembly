---
closure_plan:
  id: conversion_ceiling_campaign
  title: "Conversion-Ceiling Campaign (prong-map / parallel multi-face)"
  registered: 2026-06-22
  last_updated: 2026-07-10
  scope_claims: [MECH-439, MECH-309, ARC-062, MECH-445, MECH-446, MECH-448, MECH-449, SD-033b, MECH-263, ARC-107, ARC-108, MECH-450, MECH-458]
  sibling_plans: [behavioral_diversity_isolation, arc_062_rule_apprehension, commitment_closure, sd033_governance]
  pattern: prong_map_pattern.md
  instance_map: conversion_ceiling_prong_map.md
  nodes:
    - id: "conversion_ceiling_campaign:CAMPAIGN"
      title: "Umbrella: assemble the multi-face substrate that converts per-candidate diversity to committed-class diversity"
      status: assembling
      severity: load-bearing
      live:
        as_of: "2026-07-10"
        from: "failure_autopsy_V3-EXQ-732_2026-07-10"
        verdict: "non_contributory/precondition_unmet"
        next: "routing=queue-experiment"
        brake: "fired"
        needs_review: true
        needs_review_reasons: ["newest_forward_predates_later_measurement_event(s)"]
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-439", "MECH-309", "ARC-062", "MECH-445", "MECH-446", "MECH-448", "MECH-449", "SD-033b", "MECH-263", "ARC-107", "ARC-108", "MECH-450"]
      assembly_status: ran_exhausted_for_substrate
    - id: "conversion_ceiling_campaign:P-comp"
      title: "Selection-face composition: does MECH-448 demotion x MECH-449 Go/No-Go compound or cancel at committed-class entropy (C2)?"
      status: assembling
      severity: load-bearing
      live:
        as_of: "2026-07-10"
        from: "failure_autopsy_V3-EXQ-732_2026-07-10"
        verdict: "non_contributory/precondition_unmet"
        next: "routing=queue-experiment"
        brake: "fired"
        needs_review: true
        needs_review_reasons: ["newest_forward_predates_later_measurement_event(s)"]
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-439", "MECH-309", "ARC-062", "MECH-445", "MECH-446", "MECH-448", "MECH-449", "SD-033b", "MECH-263", "ARC-107", "ARC-108", "MECH-450"]
      assembly_status: ran_non_contributory
    - id: "conversion_ceiling_campaign:P2-rootC"
      title: "Commit-duration face (root C, MECH-445/446): de-commit authority on a substrate where natural-commit and closure-de-commit are dissociable"
      status: assembling
      severity: load-bearing
      live:
        as_of: "2026-07-10"
        from: "failure_autopsy_V3-EXQ-732_2026-07-10"
        verdict: "non_contributory/precondition_unmet"
        next: "routing=queue-experiment"
        brake: "fired"
        needs_review: true
        needs_review_reasons: ["newest_forward_predates_later_measurement_event(s)"]
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-439", "MECH-309", "ARC-062", "MECH-445", "MECH-446", "MECH-448", "MECH-449", "SD-033b", "MECH-263", "ARC-107", "ARC-108", "MECH-450"]
      assembly_status: ran_exhausted_for_substrate
    - id: "conversion_ceiling_campaign:P3-ofc"
      title: "Valuation face (SD-033b/MECH-263): decoupled OFC devaluation head feeding F"
      status: assembling
      severity: medium
      live:
        as_of: "2026-07-10"
        from: "failure_autopsy_V3-EXQ-732_2026-07-10"
        verdict: "non_contributory/precondition_unmet"
        next: "routing=queue-experiment"
        brake: "fired"
        needs_review: true
        needs_review_reasons: ["newest_forward_predates_later_measurement_event(s)"]
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-439", "MECH-309", "ARC-062", "MECH-445", "MECH-446", "MECH-448", "MECH-449", "SD-033b", "MECH-263", "ARC-107", "ARC-108", "MECH-450"]
      assembly_status: built
    - id: "conversion_ceiling_campaign:FULLSTACK"
      title: "The real test: co-armed full-stack arm (demotion + Go/No-Go + floor + root-C + OFC ON), sweep use_candidate_rule_field, DV committed-class entropy"
      status: assembling
      severity: load-bearing
      live:
        as_of: "2026-07-10"
        from: "failure_autopsy_V3-EXQ-732_2026-07-10"
        verdict: "non_contributory/precondition_unmet"
        next: "routing=queue-experiment"
        brake: "fired"
        needs_review: true
        needs_review_reasons: ["newest_forward_predates_later_measurement_event(s)"]
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-439", "MECH-309", "ARC-062", "MECH-445", "MECH-446", "MECH-448", "MECH-449", "SD-033b", "MECH-263", "ARC-107", "ARC-108", "MECH-450"]
      assembly_status: ran_exhausted_for_substrate
      cross_plan_link: ["behavioral_diversity_isolation:GAP-I"]
    - id: "conversion_ceiling_campaign:P4-learned-gating"
      title: "Learned-gating face (ARC-108 / MECH-450): make the ARC-107 arithmetic BG arbitration LEARNABLE. The selection face was not 'exhausted lever-by-lever' -- it was never given learned parameters; ARC-108 adds the dopamine-into-gating learning afferent (learned w_chan) + MECH-450 a bounded recurrent settling step replacing the one-shot pallidal argmin."
      status: assembling
      severity: load-bearing
      live:
        as_of: "2026-07-10"
        from: "failure_autopsy_V3-EXQ-732_2026-07-10"
        verdict: "non_contributory/precondition_unmet"
        next: "routing=queue-experiment"
        brake: "fired"
        needs_review: true
        needs_review_reasons: ["newest_forward_predates_later_measurement_event(s)"]
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-439", "MECH-309", "ARC-062", "MECH-445", "MECH-446", "MECH-448", "MECH-449", "SD-033b", "MECH-263", "ARC-107", "ARC-108", "MECH-450"]
      assembly_status: exhausted
      cross_plan_link: ["behavioral_diversity_isolation:GAP-K"]
      reconcile_note_2026_07_06: "ARBITRATION FACE EXHAUSTED (session ecstatic-pare-45f7ad; planning reconciliation only, PROMOTES NOTHING). This 4th campaign face -- the cross-loop-arbitration-REWEIGHTING attack, mirror of behavioral_diversity_isolation:GAP-K -- is retired: 709 (weak) / 711 (runaway) / 713 (fair-bounded parity win) all ran terminal FAIL/non_contributory, and 713 (the first fair non-saturated limbic parity win) still failed C1, exhausting the route. The selection/eligibility face (MECH-448, the SELECTION-face prongs P-comp/P2/P3 composing into FULLSTACK) is confirmed the conversion route of record. status KEPT assembling (NOT flipped to done): the MECH-439 ceiling this face attacked is STILL OPEN (tracked by the in-progress behavioral_diversity_isolation:GAP-I); crediting an exhausted-negative face done=1.0 would inflate the closure %. Marked assembly_status: exhausted, off the % axis."
      build_note_2026_07_01: "The ARC-108xARC-110 LEARNED CROSS-LOOP arbitration coupling -- the 707b-NARROW missing dependency (static-arithmetic cross-loop combine inherits F's dominance so the live limbic loop never wins) -- is BUILT (session learned-crossloop-arbitration-20260701T1840Z, /implement-substrate) behind no-op-default flag config.e3.use_learned_cross_loop_arbitration: a learned [3,3] cross-loop matrix W_cross = I + M_cross updated by the ARC-108 signed-RPE three-factor rule, coupled with MECH-450 settling. PROMOTES NOTHING (annotated on ARC-108 + ARC-110; no new claim per the 2026-06-29 MECH-439 /claim-synthesis DROP-MECH-453). status stays assembling (built substrate, conversion not yet demonstrated). Docs docs/architecture/learned_cross_loop_arbitration.md; ree-v3/CLAUDE.md. Owner build node GAP-K carries the full build_note_2026_07_01."
      reappointment_note_2026_06_24: "ARC-108 depends_on ARC-110 (the segregated-loops sequencing fork). ARC-110 + coupled ARC-109/MECH-452 were REAPPOINTED V4->V3 2026-06-24 (user-directed) because the loop-segregation build attacks MECH-439, this campaign's load-bearing blocker. The 700c-terminal escalation therefore routes to a V3 loop build GATED on V3-EXQ-704 (MECH-451), not a V4 hand-off. See sd_v4_loop_segregation.md (generation flipped V3) + substrate_queue v4_loop_segregation + behavioral_diversity_isolation:GAP-K (the build-owner node)."
      reclassification_note_2026_07_03: "V4->V3 RECLASSIFICATION COMPLETED (user-directed, phase-follows-dependency). The loop-segregation cluster (ARC-108/ARC-109/ARC-110/MECH-439/MECH-450/MECH-451/MECH-452 + MECH-140) is now V3-CLOSURE-REQUIRED, not merely V3-reappointed-but-gated: lifting the F-dominance single-arena conversion ceiling is a V3-closure requirement, and a substrate_ceiling is never grounds to defer to V4. Three structurally-independent conversion mechanisms -- the 700-lineage same-layer-null/exploration, V3-EXQ-709 learned/DA-gated cross-loop arbitration, and V3-EXQ-710 disinhibitory soft-competitive settling -- have ALL self-routed non_contributory/substrate_not_ready on the ONE single-arena F-dominated shared selector; both confirmed autopsies (failure_autopsy_V3-EXQ-709_2026-07-03 + failure_autopsy_V3-EXQ-710_2026-07-03) conclude the ceiling is a SUBSTRATE property and route to implement-substrate v4_loop_segregation. claims.yaml MECH-140 set implementation_phase v3 (all siblings already v3); substrate_queue v4_loop_segregation depends_on_unresolved stripped of the incorrect 'V4 substrate epoch / V4 implementation starts after V3 closeout' deferral gate (the segregated-loop substrate was already BUILT no-op-default in the ree-v3 V3 codebase 2026-06-27 and runs IN the V3 substrate; ARC-109/MECH-452 are V3 built co-requisites), title/status reframed V3-closure-required. sd_id 'v4_loop_segregation' RETAINED verbatim for cross-ref stability. PROMOTES NOTHING (phase reclassification only)."
    - id: "conversion_ceiling_campaign:GENERATION"
      title: "GENERATION face (the missing 6th face, MECH-458): per-candidate strategy diversity may be generation-LIMITED, not merely un-converted. The other five faces are all SELECTION machinery over a candidate set the campaign presumes is already diverse; if the SD-025 curiosity/generation drive is exploitation-dominant (rich-get-richer, 0 proactive pull toward under-represented regions), diversity is never generated and no amount of selection lifts it. Build target: a PROACTIVE rarity-seeking drive (Bellemare-2016 polarity: attraction to low-count / under-represented strategy classes, independent of reward-shaping) on ARC-065/MECH-314 -- NOT a novelty-magnitude sweep of SD-025. ORDERING-GATED on INV-088 z_world differentiation (a rarity term over an under-differentiated map has nothing to range over)."
      status: assembling
      severity: load-bearing
      live:
        as_of: "2026-07-17"
        from: "curiosity_exploitation_amplifier_reframe_2026-07-17 (registered MECH-458)"
        verdict: "generation-limited hypothesis (V3-EXQ-767a exploitation 39.3 vs diversity-ceiling 20.4, 0 at the decision point; V3-EXQ-768a SD-025-alone-on-flat = 0)"
        next: "routing=implement-substrate (rarity-seeking ARC-065/MECH-314), BLOCKED-ON-UPSTREAM INV-088 z_world differentiation"
        brake: "not_fired"
        needs_review: false
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-458", "ARC-065", "MECH-314", "INV-088"]
      assembly_status: blocked_on_upstream
      cross_plan_link: ["behavioral_diversity_isolation:GAP-A", "arc_062_rule_apprehension:GAP-H"]
      rescope_note_2026_07_17: "GENERATION FACE ADDED (session trusting-williams-ac3b1d; metabolizes the curiosity=exploitation-amplifier reframe, registered MECH-458). PROMOTES/DEMOTES NOTHING -- it names a missing build target, not a demonstrated conversion. The campaign's uniform precondition_unmet/non_contributory verdicts across the five SELECTION faces (failure_autopsy_V3-EXQ-732_2026-07-10) are re-read as 'per-candidate diversity was never GENERATED,' not 'selection failed': 767a decomposes the SD-025 curiosity margin as exploitation 39.3 vs a lagging familiarity-discount ceiling 20.4 (0 at the decision point), and 768a shows SD-025-alone on a flat map = 0 directed behaviour (density-attraction is 100% parasitic on prior DA-shaping). The fix is a proactive rarity-seeking drive (Bellemare polarity) on ARC-065/MECH-314, NOT more selection faces and NOT a magnitude sweep of SD-025 (768a: the flat-map arm reads ~0 regardless of weight). status assembling / assembly_status blocked_on_upstream: the build is ORDERING-GATED on INV-088 z_world differentiation (differentiate-first; a rarity term over an AUC-0.83 map chases the sparse corner, not diverse strategies) -- this node is NOT runnable until INV-088 clears, so no experiment is queued here. Off the closure %. See docs/architecture/sd_024_da_modulated_rbf_density.md#curiosity-exploitation-polarity-mech-458 and the PREMISE CHALLENGE blockquote below."
---

# Conversion-Ceiling Campaign

This closure plan is the **assembly-frontier home** for the conversion-ceiling campaign. Its nodes are all `status: assembling` by design — they are required for v3 but actively under construction, so they sit on the assembly frontier (weight `None`, off the closure %) and rest in drift rather than nagging the green-board.

- **The pattern** it instantiates: [`prong_map_pattern.md`](prong_map_pattern.md).
- **The live campaign view** (prong inventory, composition matrix, full-stack spec, critical path): [`conversion_ceiling_prong_map.md`](conversion_ceiling_prong_map.md).
- **The lever inventory + metric trajectory**: the `f_dominance_conversion_ceiling` entry in `substrate_queue.json` (6-rung `fallback_ladder`; rung 6 = root C, tagged PARALLEL to the selection-face rungs).

> **PREMISE CHALLENGE (2026-07-17, hypothesis):** every face here is *selection* machinery, and the umbrella thesis presumes per-candidate diversity already exists and only needs *converting*. The curiosity=exploitation-amplifier reframe ([`curiosity_exploitation_amplifier_reframe_2026-07-17.md`](curiosity_exploitation_amplifier_reframe_2026-07-17.md)) argues per-candidate diversity may be **generation-limited** — the SD-025 drive is exploitation-dominant (V3-EXQ-767a: density-attraction 39.3 vs familiarity-discount ceiling 20.4, 0 at the decision point) and produces zero directed behaviour on an unshaped map (V3-EXQ-768a: SD-025-alone = 0). If so, the uniform `precondition_unmet / non_contributory` verdicts across all five faces (failure_autopsy_V3-EXQ-732_2026-07-10) read as "diversity was never generated," not "selection failed" — and the campaign needs a **generation face** (rarity-seeking `ARC-065 / MECH-314`, ordering-gated on INV-088), not more selection faces. Governance to consider re-scoping `CAMPAIGN`.

## Node summary

| Node | Face | State | Runnable |
|---|---|---|---|
| `:CAMPAIGN` | umbrella | assembling / **converged on competence gate** (all faces RAN terminal) | **V3-EXQ-724 competence-localization diagnostic (brake-EXEMPT, running)** |
| `:P-comp` | selection (demotion x Go/No-Go) | assembling / RAN (699 non_contributory, precondition_unmet) | diagnostic re-run at most; no build owed |
| `:P2-rootC` | commit-duration | assembling / **de-commit cluster RAN TERMINAL** (715/715a/717 all FAIL; selection-face lift RULED OUT, delta -63; MECH-445 existence proven but sub-2/3 reliable) | **/implement-substrate de-commit-release face, gated behind the 719a competence reframe; no re-queue (brake FIRED)** |
| `:P3-ofc` | valuation | assembling / face-validated (485m RAN, fails-C2-alone) | composed into FULLSTACK (714); ran terminal there |
| `:P4-learned-gating` | arbitration reweighting (GAP-K mirror) | assembling / **EXHAUSTED** (709/711/713 terminal) | — retired; not a full-stack member |
| `:FULLSTACK` | composite (selection-face stack) | assembling / **RAN TERMINAL** (V3-EXQ-714 FAIL/non_contributory, readiness abort -- C2 never scored) | **V3-EXQ-724 competence-localization (719a reframe, running); 714b REFUSED (brake FIRED)** |
| `:GENERATION` | **generation (the missing 6th face, MECH-458)** | assembling / **BLOCKED-ON-UPSTREAM INV-088** (not yet built) | **/implement-substrate rarity-seeking ARC-065/MECH-314 -- ORDERING-GATED on INV-088 z_world differentiation; no experiment queued here until INV-088 clears** |

**Route of record (2026-07-09 — every face RAN terminal; campaign converged on the behavioural-competence gate):** all four campaign faces have now run to terminal against the current substrate, and none cleared the conversion ceiling. (1) The cross-loop-**arbitration-reweighting** face (`:P4-learned-gating` / `behavioral_diversity_isolation:GAP-K`) is **EXHAUSTED** — V3-EXQ-709/711/713 all terminal FAIL; 713's first validly-measured fair non-saturated limbic parity win **still** failed C1 (`failure_autopsy_V3-EXQ-713_2026-07-05`, governance-applied `65940b83b5`). (2) The **selection+valuation FULLSTACK arm** V3-EXQ-714 **RAN terminal FAIL/non_contributory** (self-routed `substrate_not_ready_requeue` — the C2 committed-class-entropy falsifier was **never scored**: readiness gates C1b GAP-A divergence `0.004<0.05` and C1g OFC devalued-range `0.0007<0.05` failed even at full P0=200; `failure_autopsy_V3-EXQ-714_2026-07-07`, 20th ARC-062 / 19th MECH-309, **brake FIRED**, fullstack re-queue REFUSED). (3) The **P2 root-C de-commit cluster** V3-EXQ-715/715a/717 **RAN terminal FAIL** (`failure_autopsy_MECH-445-cluster-715a-717_2026-07-07`): the moderate-F selection-face lift is **RULED OUT** as the de-commit-release lever (715a `moderate_f_delta -63`, arming 1/3), MECH-445 F-independent commit-intent existence is proven but **sub-2/3-reliable** (717 narrow weakens, 2/9 in-regime); both route to `/implement-substrate` on the `f_dominance_conversion_ceiling` **de-commit-release face** (brake FIRED, same-claim de-commit re-queue REFUSED). (4) The **valuation** face (`:P3-ofc` / 485m) is face-validated but fails-C2-alone, and composed into 714. **Convergence** (`failure_autopsy_V3-EXQ-719a_2026-07-08`, governance-applied `REE_assembly` master `07acd6ad29`): the 714 readiness abort and the whole 654h/485i/625e/460h/460i downstream-behavioural-retest wall are **one root** — the integrated all-ON agent is not behaviourally **competent** enough to produce meaningful committed behaviour to measure (forages `0.065/0.0/0.455` resources/ep, below the `1.0` floor on 0/3 seeds; MI above the shuffle null 3/3 yet marginal committed entropy moderate-to-high = diffuse state-blind commitment, **not** literal monomodal collapse). The missing substrate is **not** another selection/valuation/arbitration/de-commit lever — it is whatever makes the fully-integrated agent competently commit. The campaign now converges on the **competence-localization gate**: the brake-EXEMPT **V3-EXQ-724 competence-localization diagnostic** (a *different* question — thin P1 budget vs frozen encoder vs all-ON mechanism interference; queued + running as of 2026-07-08) localizes the lever **before** any `/implement-substrate` build. **Do NOT re-queue any conversion or de-commit falsifier** — both re-derive brakes REFUSE it.

Factor B (gap-scaled commit-T) is **refuted** at the selection face (V3-EXQ-689c FAIL, 2026-06-21) and is **not** represented as a live node — it is dropped from the full-stack arm. See the prong map for the full rationale.
