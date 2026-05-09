# Targeted lit-pull synthesis: ARC-062 / MECH-309 / ARC-063 — refuge-vs-forage behavioural ecology

**Pulled** 2026-05-09 (6 entries).
**Target claims** MECH-309 (monomodal collapse without rule-apprehension), ARC-062 (weak reading, V3 architectural slot), ARC-063 (strong reading, V4 deferred), SD-054 (reef enrichment substrate — directly relevant to several entries).
**Author** lit-pull session `lit-pull-arc062-refuge-forage-ecology-2026-05-09T1924Z`.
**Sister pull** Pull A `targeted_review_arc_062_rule_apprehension/` (8 entries; PFC / BG / hippocampal architectural anchors). Pull B is the behavioural-ecology / R4 calibration counterpart.
**Plan-of-record** to be drafted from these two pulls together: `evidence/planning/arc_062_rule_apprehension_plan.md`.

---

## Verdict — R4 (Phase 2 falsifier acceptance threshold calibration)

**The acceptance threshold should be a tolerance window with multiple convergent signatures, not a single fixed allocation ratio.** Six anchors converge on this verdict from different directions:

| Source | Direction of constraint |
|---|---|
| Lima & Bednekoff 1999 *Am Nat* ([DOI 10.1086/303202](https://doi.org/10.1086/303202)) | Canonical theory: allocation is a *function* of temporal risk pattern; chronic-high-risk should REDUCE refuge-use, not increase it; pulsed-risk paradigms overestimate antipredator behaviour |
| Beauchamp & Ruxton 2010 *Am Nat* ([DOI 10.1086/657437](https://doi.org/10.1086/657437)) | Theoretical reassessment: even canonical-theory's specific quantitative predictions have caveats; field has retained the *spirit* but weakened specific predictions |
| Sundell et al. 2004 *Oecologia* ([DOI 10.1007/s00442-004-1490-x](https://doi.org/10.1007/s00442-004-1490-x)) | Empirical field test in voles: 1/5 Lima-Bednekoff predictions replicated; partial replication is the realistic empirical baseline |
| Balaban-Feld et al. 2019 *Oecologia* ([DOI 10.1007/s00442-019-04395-z](https://doi.org/10.1007/s00442-019-04395-z)) | Direct fish-refuge data: state-dependent allocation (underfed forage more, well-fed refuge more); within-population spread driven by internal-state variable |
| Eccard et al. 2020 *Oecologia* ([DOI 10.1007/s00442-020-04773-y](https://doi.org/10.1007/s00442-020-04773-y)) | Individual variation in voles: consistent across-individual differences ("foraging personalities"); risk-type dissociation (feeding-risk vs transit-risk) |
| Crowell et al. 2016 *Ecol Evol* ([DOI 10.1002/ece3.1940](https://doi.org/10.1002/ece3.1940)) | Species-difference data: closely-related rabbits with different body sizes / refuge dependencies adopt different policies in the same environment |

### Architectural commitment for the plan-doc

R4 default = **multi-signature tolerance window**, not single-ratio:

- **Acceptance criterion 1 (density tracking)**: ARM_1 ARC-062 should produce monotone refuge-use response across SD-054 hazard density (more hazards → more refuge-use, but with the chronic-high-risk reduction kicking in at the high-density end per Lima-Bednekoff). Exact slopes are species-specific and not pre-registerable; require *positive* monotone relationship with at least one significant manipulation.
- **Acceptance criterion 2 (state-dependence)**: ARM_1 should produce monotone refuge-use response across agent `drive_level` (underfed → less refuge-use, well-fed → more refuge-use) per Balaban-Feld 2019. Single-stream `z_world`-only discriminator is predicted to FAIL this; multi-stream default per Pull A's R1 verdict is required to PASS it.
- **Acceptance criterion 3 (risk-type dissociation)**: ARM_1 should produce *different* response patterns to risk-during-feeding (food-attracted hazards in forage zone) vs risk-during-transit (transitions between reef and forage zone) per Eccard 2020. If the two manipulations move the same metric in lock-step, the discriminator is collapsing across distinct risk-type cues.
- **Acceptance criterion 4 (cross-seed variation)**: ARM_1 should produce non-zero across-seed coefficient of variation in `reef_visit_fraction`. Real animals show consistent inter-individual differences (Eccard 2020) and inter-species differences (Crowell 2016) in the same environment; seed-convergence to a single allocation is biologically anomalous.
- **PASS rule**: at least 2 of 4 acceptance criteria hold with p<0.05 across seeds, with no contradictory signal (e.g. invariant allocation OR perfect convergence). Consistent with Sundell's empirical 1/5 partial replication and Beauchamp-Ruxton's theoretical-caveat reading.

**Sharper FAIL signatures** (any one is unambiguous):
- Total invariance across all four criteria — the unambiguous monomodal-collapse signature MECH-309 predicts for an architecture without rule-apprehension layer.
- Refuge-use *increases* monotonically with chronic high-risk regimes — biologically inverted; would indicate the agent is implementing a naive "always-flee-when-hazard-present" policy rather than the relative-risk-pattern-dependent policy biology actually exhibits.

### Why a tolerance window rather than a sharp ratio

Three converging arguments:

1. **Theoretical caveats** (Beauchamp & Ruxton 2010): even the canonical theory's specific quantitative predictions have caveats; the field has retained the spirit while weakening specifics.
2. **Empirical noise** (Sundell 2004): real animals tested against a 5-prediction theoretical battery delivered 1/5 replication. Narrow acceptance criteria would falsely reject biologically plausible behaviour.
3. **Individual / species variation** (Eccard 2020, Crowell 2016): even within a single environment, biology produces inter-individual and inter-species variation in allocation. The Phase 2 falsifier should expect cross-seed variation in ARM_1 rather than convergence.

### Numerical calibration target — best available

For the specific case of fish-with-refuge-and-active-predator (closest direct analog to SD-054), Balaban-Feld 2019 is the load-bearing entry. Its quantitative pattern: state-dependent allocation difference between underfed and well-fed individuals in the same group. Specific numerical ratios are sample-specific (n=12 paired groups, goldfish-egret system); the *shape* (monotone state-dependence) generalises. The Phase 2 falsifier's state-dependence acceptance criterion should specify a slope direction (negative `reef_visit_fraction` vs `drive_level`) rather than a specific numerical slope.

---

## Cross-claim implications

### MECH-309 (monomodal collapse without rule-apprehension)

The pull *supports* MECH-309's logical-necessity claim with three convergent strands:

1. **Lima & Bednekoff 1999 + Beauchamp & Ruxton 2010** — biology has a real allocation rule (modulate antipredator effort by relative risk pattern) that requires the agent to *represent* the relative-risk variable. Strict gradient descent on raw policy-loss without a discriminator that gates on this variable would not extract it from the input stream.

2. **Sundell 2004** — even when the architecture is biologically present, perception failures can produce monomodal-looking behaviour. Real voles cannot accurately assess outdoor risk-pattern changes; the architecture-vs-perception ambiguity in their data maps directly to a similar ambiguity for ARC-062. The discriminator may have the architecture but lack adequate input signal — a relevant diagnostic when interpreting Phase 2 falsifier results.

3. **Eccard 2020 + Crowell 2016** — even *with* the architecture and adequate perception, biology produces multiple coexisting valid policies rather than a single optimum. MECH-309's monomodal collapse is therefore a *more severe* form of failure than what biology exhibits; ARC-062's success criterion is producing context-dependent allocation with substantial variation, not converging to a single optimum.

### ARC-062 (V3 architectural slot, weak reading)

The pull *qualifies* ARC-062's empirical expectations:

- The Phase 2 falsifier should not pre-register acceptance criteria that match a strict reading of Lima-Bednekoff (Beauchamp & Ruxton 2010 caveat).
- ARM_1 should be tested across multiple manipulations (hazard density, attack ratio, internal state, risk-type) rather than a single binary comparison; partial replication is the biologically expected signature (Sundell 2004).
- Across-seed variation in ARM_1 is a *positive* prediction of the architecture (Eccard 2020, Crowell 2016), not a noise concern.

### ARC-063 (V4 strong reading, deferred)

The pull *strengthens* the case that V4 strong reading will be needed at scale:

- Crowell 2016 species-difference data shows multiple coexisting valid policies in the same environment. ARC-063's distributed `CandidateRule` field is the architecture that explicitly accommodates this; ARC-062 weak reading at the score_bias level can produce one policy but not multiple coexisting ones.
- Eccard 2020 risk-type dissociation requires the agent to maintain separate policy components for different risk types. ARC-062's two-head architecture handles binary cuts; ARC-063's `CandidateRule` field handles the multi-rule structure that Crowell + Eccard together imply biology exhibits.

### SD-054 (reef enrichment substrate)

Several entries explicitly tag SD-054. The substrate has the right *structural* shape (refuge area + forage zone + active hazards + spatial gradient) but quantitative calibration of its constants — `n_reef_patches`, `reef_patch_radius`, `hazard_food_attraction` — is empirical rather than biology-anchored. Pull B's verdict is that calibration via biology requires a *system match* (ideally fish-with-coral-refuge); Balaban-Feld's goldfish-and-egret is the closest available analog but is not coral-reef-specific. Future SD-054 calibration may benefit from a coral-reef-fish-specific empirical search; that is out of Pull B's scope.

---

## Discharged debt

The MECH-309 `evidence_quality_note` (updated 2026-05-09 after Pull A) listed remaining debts; Pull B addresses one but not all:

- ✓ Pull A discharged hippocampal rollout selection, basal ganglia commitment, PFC rule-coding (8 entries).
- ✓ Pull B discharges behavioural ecology refuge-vs-forage allocation as a quantitative calibration anchor for the Phase 2 falsifier (6 entries).
- ✗ Sleep-vs-waking refinement remains outstanding, scoped to ARC-063 V4 work.

**Action**: update MECH-309 `evidence_quality_note` to mark Pull B discharged, point at this directory, with the sleep-vs-waking-refinement debt remaining as the only future-pull recommendation.

---

## Next steps post-pull

1. Rebuild the evidence index. Lit_conf on MECH-309 / ARC-062 / ARC-063 will rise modestly from 0.894 (Pull A baseline) as 6 more entries land; entries_total per claim should go from 8 → 14.
2. Update MECH-309 `evidence_quality_note` per the "Discharged debt" action above.
3. Draft `evidence/planning/arc_062_rule_apprehension_plan.md` — with R1, R2, R3 (Pull A) + R4 (Pull B) all biology-anchored, the plan's Open Questions section can be written with resolved-default values for all four.
4. Update `commitment_closure_plan.md` GAP-1 row with the cross-plan link to the new plan-doc, per the parent session's sketch.

---

## Entries summary

| entry_id | source | direction | confidence | primary R-question coverage |
|---|---|---|---|---|
| `..._risk_allocation_canonical_lima1999` | Lima & Bednekoff 1999 *Am Nat* | supports | 0.88 | R4 theory foundation |
| `..._state_dependent_fish_refuge_balabanfeld2019` | Balaban-Feld et al. 2019 *Oecologia* | supports | 0.81 | R4 fish-refuge state-dependence (highest mapping fidelity to SD-054) |
| `..._risk_allocation_vole_test_sundell2004` | Sundell et al. 2004 *Oecologia* | mixed | 0.71 | R4 empirical partial replication; tolerance-window calibration |
| `..._individual_foraging_personalities_eccard2020` | Eccard et al. 2020 *Oecologia* | supports | 0.79 | R4 individual variation + risk-type dissociation |
| `..._rabbit_refuge_distance_crowell2016` | Crowell et al. 2016 *Ecol Evol* | supports | 0.74 | R4 refuge-distance gradient + species variation |
| `..._risk_allocation_critique_beauchamp2010` | Beauchamp & Ruxton 2010 *Am Nat* | mixed | 0.68 | R4 theoretical caveat for tolerance window |
