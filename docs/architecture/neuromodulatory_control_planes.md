# Four-Plane Neuromodulatory Control Model

**Source thought:** Theoretical development session 2026-03-15 (NC-11 through NC-16)
**Registered:** 2026-03-15

> **CONFLICT NOTICE (for Daniel's judgment):**
> MECH-085 [Serotonin as Map Geometry Plane] is in partial conflict with MECH-006 [serotonin.md], which explicitly states that serotonin "does NOT select temporal depth (τ)." MECH-085 claims serotonin controls temporal depth of rollouts and aversive attractor basin depth. These are materially different functional accounts.
>
> Resolution options:
> **(A) Reconcile as different levels of description:** MECH-006 describes serotonin's effect at the *representational collapse / exclusivity* level (cognitive-narrative); MECH-085 describes its effect at the *hippocampal terrain* level (map geometry). "Temporal depth of rollouts" (MECH-085) and "learning depth" (MECH-006's `DepthOfRevision ∝ (1-σ)`) may be the same phenomenon described at different levels of the hierarchy.
> **(B) Revise MECH-006:** update it to incorporate hippocampal map geometry framing, removing the "does NOT select temporal depth" prohibition and replacing it with a level-specific account.
> **(C) Restrict MECH-085:** accept MECH-085 only for claims that do not overlap with MECH-006, deferring the temporal-depth and exclusivity claims to further adjudication.
>
> **Neither resolution is taken here. MECH-085 is registered as candidate with explicit conflict flag pending Daniel's adjudication.**

---

<a id="mech-083"></a>
## Acetylcholine as Meta-Level Plasticity Gate (MECH-083)

**Claim Type:** mechanism_hypothesis
**Scope:** ACh as the meta-level control plane governing whether current experience updates the hippocampal map
**Depends On:** ARC-005, ARC-007, ARC-018, INV-019, INV-024
**Status:** candidate
**Claim ID:** MECH-083
**New domain:** no prior counterpart in REE claim registry for ACh-specific function

Acetylcholine functions as the meta-level control plane, gating whether current experience updates the hippocampal map or is interpreted through it — the encoding/retrieval mode switch.

**Mechanism:** ACh switches the hippocampus between two operating modes:
- **High ACh (encoding mode):** new representations are written into the hippocampal map; synaptic plasticity in CA3 and dentate gyrus is enabled; current experience modifies map geometry.
- **Low ACh (retrieval mode):** existing map geometry dominates; pattern completion draws on stored attractors; current experience is interpreted through the prior map rather than modifying it.

**Meta-level position:** ACh sits above the other three neuromodulatory planes (MECH-084 through MECH-086) because it determines whether operations at those planes leave a lasting trace in the map. Dopamine (MECH-086) can set gain on attractor selection, serotonin (MECH-085) can modulate basin depth, and noradrenaline (MECH-084) can alter perceptual sampling — but if ACh signals retrieval mode, none of these operations will be consolidated into durable map updates.

**Relationship to INV-019 and INV-024:** INV-019 states that rehearsal traversal and irreversible durable write must remain separated. INV-024 states offline consolidation and online commitment must remain isolated at responsibility-bearing write loci. ACh is the biological implementation of this separation: encoding mode opens the write path; retrieval mode closes it. ACh gating is therefore the functional instantiation of INV-019/INV-024 at the hippocampal level.

**Failure modes:**
- **Insufficient ACh gating:** failure to switch appropriately between encoding and retrieval. The map keeps updating from a stuck rollout — each retrieval re-encodes the retrieved pattern, strengthening existing attractors. This may be relevant to **OCD** (complements MECH-080's attractor-lock description) and to certain memory consolidation failures where novel experience overwrites rather than enriches existing map structure.
- **Chronic encoding mode:** map instability — every retrieval triggers re-encoding, preventing stable map geometry from forming.
- **Chronic retrieval mode:** learning failure — new experience consistently routed through existing attractors, producing perceptual confirmation bias (related to MECH-082's account of E1 perceptual bias).

**Relationship to existing claims:** ARC-005 (control plane) and MECH-019 (control plane shapes modes) describe the general control-plane architecture. MECH-083 instantiates one specific axis of that architecture (the encoding/retrieval switch) with ACh as its neuromodulatory carrier, complementing the dopamine (MECH-043), noradrenaline (MECH-005), and serotonin (MECH-006) analogues already registered.

---

<a id="mech-084"></a>
## Noradrenaline as E1/E2 Bottom-Up/Top-Down Ratio Modulator (MECH-084)

**Claim Type:** mechanism_hypothesis
**Scope:** NA as the perceptual-sampling control plane modulating the bottom-up/top-down weight ratio at the E1/E2 interface
**Depends On:** ARC-001, ARC-002, MECH-005, MECH-081, ARC-005
**Status:** candidate
**Claim ID:** MECH-084
**Extends:** MECH-005 (noradrenaline path authority and interruptibility)

Noradrenaline modulates the bottom-up / top-down ratio at the E1/E2 prediction interface. This extends MECH-005 (which covers NA's role in path authority and commitment pressure) with the specific E1/E2 interface mechanism.

**Mechanism:**
- **High NA:** reduces E2's constraining influence on E1 (the sufficiency constraint, MECH-081). E1 is forced to engage in broader, less-directed sensory sampling — attending to the full sensory stream regardless of E2's prediction space. This is the *explore signal at the perceptual level*, upstream of the planning/rollout system.
- **Low NA:** E2's constraint dominates; E1 samples selectively for dimensions that are discriminative for E2's current predictions. Perceptual processing is more efficient but also more confirmatory.

**Relationship to MECH-005:** MECH-005 defines NA's role as modulating path authority and commitment pressure. MECH-084 adds the upstream account: before commitment is even on the table, NA is determining how much E1's sensory processing is shaped by E2's current model vs. driven by raw bottom-up signals.

**Clinical anchors:**
- **Too little NA:** perceptual confirmation bias — the world confirms existing maps (E2 dominates E1 sampling). Related to MECH-082 (perceptual bias as downstream of E2 distortion).
- **Too much NA:** sensory flooding — E2 constraint collapses; E1 samples broadly without coherent object formation. Incoherent sensory input overwhelms hippocampal map coherence.
- **PTSD hypervigilance:** tonic NA elevation broadly expands bottom-up sampling, reducing E2's ability to filter the sensory stream. This makes the system sensitive to all unexpected signals, consistent with the hyperarousal phenotype.
- **Dissociation:** complex NA dysregulation may produce episodic failure of E1/E2 integration, with perceptual experience temporarily de-coupled from E2 predictions.

**Complementarity with MECH-083 (ACh):** ACh determines whether E1/E2 processing leaves a map update; NA determines *how much bottom-up input reaches the system in the first place*. Both are necessary: high NA without ACh encoding mode = sensory flooding without map update; low NA with ACh encoding mode = efficient confirmation-biased processing leaves a deep (but distorted) map imprint.

---

<a id="mech-085"></a>
## Serotonin as Hippocampal Map Geometry Parameter (MECH-085)

**Claim Type:** mechanism_hypothesis
**Scope:** Serotonin as map geometry parameter governing rollout depth, distal value weighting, and aversive basin depth
**Depends On:** MECH-006, MECH-073, MECH-076, ARC-013
**Status:** candidate
**Claim ID:** MECH-085
**⚠ Conflict with:** MECH-006 (serotonin.md). MECH-006 explicitly states serotonin "does NOT select temporal depth (τ)." MECH-085 asserts serotonin controls temporal depth of rollouts. See conflict notice above.
**Extends:** MECH-006, MECH-076

Serotonin operates on the geometry of the hippocampal landscape over which rollouts run. Rather than being a mood neuromodulator, serotonin is a map geometry parameter with three specific effects:

1. **Temporal depth of rollouts:** serotonin modulates how far forward simulation extends before truncating. High serotonin = longer rollout depth (more distal futures considered); low serotonin = shallower rollouts (near-term biased).

2. **Distal/proximal value weighting:** high serotonin may flatten the temporal distance penalty on far attractors, making long-term consequences more legible to the trajectory selection system. Low serotonin increases temporal discounting, making distal rewards and costs less influential in trajectory selection.

3. **Aversive attractor basin depth:** serotonin modulates the steepness of threat-related attractor walls in the hippocampal map. This directly explains anxiolytic effects of SSRIs: increased serotonergic tone reduces the gravitational pull of aversive representations, making the system less trapped by fear-consistent rollout loops.

**Relationship to MECH-006 (serotonin as representational collapse control):** MECH-006 frames serotonin as controlling representational exclusivity and collapse pressure across representational depths (ρ). MECH-085 frames it as map geometry parameter operating at the hippocampal terrain level. A possible reconciliation: MECH-006's "learning depth" (DepthOfRevision ∝ (1-σ)) is related to MECH-085's "temporal depth of rollouts" — both concern how far forward/deep the system's representations extend and update. However, MECH-006 contains an explicit prohibition ("serotonin does not select temporal depth τ") that is in direct tension with MECH-085's first claim. **Pending Daniel's adjudication.**

**Relationship to MECH-076 (residue as map deformation):** MECH-085 and MECH-076 are complementary accounts of map geometry. MECH-076 describes how structural damage (stress, trauma) creates persistent deformation. MECH-085 describes how serotonin dynamically modulates the functional parameters of that geometry (basin steepness, rollout depth). Both operate on the same substrate.

**Clinical anchors:**
- **SSRI anxiolytic effect:** increased serotonergic tone flattens aversive attractor walls (MECH-085 claim 3), reducing the pull of threat-consistent rollouts.
- **SSRI delay-of-onset effect:** map geometry is slow-changing; structural changes to attractor depth require multiple consolidation cycles, explaining the 2–4 week SSRI onset delay.
- **Psilocybin:** acute serotonin agonism may produce rapid large-scale flattening of attractor depth across the map (consistent with MECH-077's psychedelic-assisted therapeutic remapping account).

---

<a id="mech-086"></a>
## Dopamine as Trajectory Selection Gain Plane (MECH-086)

**Claim Type:** mechanism_hypothesis
**Scope:** Dopamine as the selection gain plane operating over the already-valenced hippocampal landscape
**Depends On:** MECH-043, MECH-075, MECH-085, ARC-005
**Status:** candidate
**Claim ID:** MECH-086
**Extends:** MECH-043 (dopamine-like precision-weighting), MECH-075 (BG attractor threshold setting)

Dopamine sets gain on trajectory selection — which rollout wins and how quickly — by modulating attractor dynamics in the already-valenced hippocampal system. This is the *exploitation signal at the planning level*.

**Mechanism:** dopamine's effect is downstream of all three upstream planes (ACh gating, NA sampling, serotonin geometry):
- Tonic dopamine sets the baseline gain on attractor entry — how strongly any basin pulls commitment toward it.
- Phasic dopamine bursts signal positive prediction error and lower the commitment threshold, facilitating rapid entry into reward-consistent attractors.
- Dopamine depletion flattens the attractor landscape — all basins become equally shallow; no trajectory wins.

**The hierarchical constraint:** dopamine optimises selection over whatever landscape (serotonin, MECH-085) and state representation (noradrenaline, MECH-084) and encoding mode (ACh, MECH-083) it receives. It *cannot compensate* for upstream plane failures:
- Distorted map geometry (MECH-076) + high dopamine → rapid, confident commitment to distorted trajectories.
- Sensory flooding (high NA) → dopamine cannot stabilise selection because state representation is incoherent.
- Encoding mode failure (ACh) → dopamine-modulated selection occurs normally but leaves no consolidated map update.

**Relationship to MECH-043 and MECH-075:** MECH-043 covers dopamine-like unsigned prediction error precision-weighting. MECH-075 covers BG attractor threshold setting in the hippocampal context. MECH-086 synthesises both into the explicit "selection gain plane" framing and adds the hierarchical-constraint claim: dopamine's effectiveness is bounded by the quality of upstream plane outputs.

**Failure modes:**
- **Too little:** indecision, flattened landscape, anhedonia (no trajectory dominates; system cannot commit even when viable options exist).
- **Too much:** premature commitment, inflexibility, aberrant salience (noise attractors inappropriately capture commitment).

---

<a id="mech-087"></a>
## Hierarchical Ordering of Four Neuromodulatory Control Planes (MECH-087)

**Claim Type:** mechanism_hypothesis
**Scope:** Hierarchical ordering of ACh, NA, serotonin, dopamine planes by upstream position in the processing hierarchy
**Depends On:** MECH-083, MECH-084, MECH-085, MECH-086, ARC-005, MECH-063
**Status:** candidate
**Claim ID:** MECH-087
**Extends:** MECH-063 (orthogonal tonic/phasic control axes), ARC-005 (control plane)

The four neuromodulatory control planes are hierarchically ordered by how upstream their effects are:

```
ACh         → does this moment update the map at all?        [meta-level gate]
Noradrenaline → what gets encoded as the current state?      [perceptual sampling]
Serotonin   → what does the landscape look like?             [map geometry]
Dopamine    → which trajectory wins?                         [selection gain]
```

Each downstream plane operates over the outputs of all upstream planes. The hierarchy is not merely descriptive — it generates specific predictions:

1. **Cascade failure:** dysfunction at any level cascades downward but produces *qualitatively distinct* failure modes (see MECH-088). A serotonin failure produces different pathology than a dopamine failure, even if both ultimately manifest as abnormal trajectory selection.

2. **Intervention order:** single-neuromodulator interventions will be partially effective at best when the primary dysfunction is at a different plane. Upstream planes should be stabilised before downstream optimisation is attempted (e.g., treating NA dysregulation before attempting dopaminergic augmentation in PTSD with comorbid ADHD-like symptoms).

3. **Epistatic effects:** dopamine augmentation on a distorted serotonergic landscape produces rapid, confident commitment to distorted trajectories — potentially worsening outcomes compared to dopamine augmentation on a healthy landscape.

**Relationship to MECH-063 (orthogonal control axes):** MECH-063 specifies that control-plane axes should remain orthogonal (no single global arousal scalar). MECH-087 adds hierarchical ordering to the orthogonality requirement: the axes are not only orthogonal but ordered by upstream position, meaning their interactions are asymmetric (upstream planes constrain downstream plane effectiveness; downstream planes do not propagate effects upward).

**Testable prediction:** in a REE model with all four control axes, selectively degrading the serotonin axis (map geometry) should produce characteristic trajectory pathology that is not rescued by increasing dopamine gain. Conversely, degrading only the dopamine axis should produce a different failure mode that is rescued by dopamine augmentation, not by serotonin adjustment.

---

<a id="mech-088"></a>
## Psychiatric Conditions as Four-Plane Neuromodulatory Control Failures (MECH-088)

**Claim Type:** mechanism_hypothesis
**Scope:** Mapping of psychiatric conditions to specific control-plane level failures
**Depends On:** MECH-083, MECH-084, MECH-085, MECH-086, MECH-087, MECH-080, MECH-027
**Status:** candidate
**Claim ID:** MECH-088
**Extends:** MECH-027 (pathological modes = mis-tuned control-plane regimes), MECH-080 (rollout truncation psychiatric differences)

The four-plane model maps onto psychiatric conditions as specific control-plane failures, extending MECH-027 and MECH-080 with a comprehensive taxonomy:

| Condition | Primary plane failure | Secondary effects | REE mechanisms |
|---|---|---|---|
| **PTSD** | Serotonin (map geometry): deep aversive attractor basins, distorted temporal weighting (MECH-085) | Secondary NA hyperactivity collapses E1/E2 constraint (MECH-084), amplifying bottom-up sensory flooding | MECH-076 (map deformation), MECH-082 (perceptual bias), MECH-084, MECH-085 |
| **Depression** | Serotonin (distal attractor inaccessibility: nothing distant feels reachable) + Dopamine (selection failure: nothing wins) | Combined effect: viable attractors exist but are inaccessible (serotonin) and cannot capture commitment (dopamine) | MECH-085, MECH-086, MECH-076 |
| **ADHD** | Noradrenaline (inconsistent perceptual sampling: state representation unstable) + Dopamine (unstable attractor commitment) | Inconsistent E1/E2 constraint (MECH-084) produces variable state encoding; dopamine-mediated BG threshold set too low (MECH-075, MECH-080) | MECH-084, MECH-086, MECH-080 |
| **OCD** | Dopamine (selection stuck in local attractor) + ACh gating failure (map keeps updating from stuck rollout) | Deep attractor basin (MECH-076) + ACh failure means each stuck-rollout retrieval re-encodes the pattern, deepening the basin | MECH-083, MECH-086, MECH-076, MECH-080 |
| **Psychosis** | NA collapse of E1/E2 constraint (sensory flooding overwhelms map coherence) + dopamine aberrant salience (spurious attractor selection on noisy input) | Map coherence fails when NA-driven sensory flooding overwhelms E2's ability to form stable predictions; dopamine then stamps selection onto noise | MECH-084, MECH-086, MECH-073, ARC-007 |

**Relationship to MECH-080 (rollout truncation substrate):** MECH-080 provides rollout-parameter profiles for ADHD, anxiety, and OCD. MECH-088 extends this with PTSD, depression, and psychosis, and grounds all profiles in the four-plane hierarchy. The rollout parameters in MECH-080 (truncation/extension set-points) are downstream consequences of the plane-level failures described here — e.g., ADHD truncation arises because unstable state representation (NA plane, MECH-084) plus low BG threshold (dopamine plane, MECH-086) jointly reduce rollout sampling depth.

**Relationship to MECH-027 (pathological modes):** MECH-027 frames pathological modes as mis-tuned control-plane regimes. MECH-088 specifies *which* planes are mis-tuned in each condition and predicts characteristic interaction patterns.

**Note on intervention predictions:** following MECH-087's hierarchical ordering, MECH-088 predicts:
- PTSD: address serotonin (map geometry) and NA (sampling) before dopaminergic augmentation.
- Depression: combined serotonin/dopamine intervention may be necessary; addressing either alone produces partial response.
- ADHD: NA and dopamine co-intervention; ACh stabilisation may reduce inconsistency.
- OCD: ACh gating normalisation and dopamine de-locking; deep-basin restructuring (MECH-077) may be required for refractory cases.
- Psychosis: NA containment (stabilise sensory sampling) before dopamine modulation; otherwise aberrant salience is stamped onto incoherent state representations.

---

## Open Questions

None currently registered specific to this file. Conflict notice for MECH-085 vs MECH-006 is the primary open issue requiring Daniel's adjudication.

---

## Related Claims (IDs)

- MECH-083
- MECH-084
- MECH-085
- MECH-086
- MECH-087
- MECH-088
- MECH-005 (noradrenaline — path authority, extends to MECH-084)
- MECH-006 (serotonin — conflict with MECH-085)
- MECH-043 (dopamine-like precision-weighting — extends to MECH-086)
- MECH-063 (orthogonal control axes — extends to MECH-087)
- MECH-075 (BG attractor threshold — extends to MECH-086)
- MECH-080 (rollout truncation — extends to MECH-088)
- MECH-027 (pathological modes — extends to MECH-088)
- ARC-005 (control plane)
- ARC-007
- INV-019
- INV-024
- Q-020

## References / Source Fragments

- Theoretical development session 2026-03-15 (NC-11 through NC-16)
