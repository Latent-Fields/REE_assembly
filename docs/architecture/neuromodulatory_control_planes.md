---
nav_exclude: true
---

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
## Acetylcholine as Meta-Level Plasticity Gain (MECH-083)

**Claim Type:** mechanism_hypothesis
**Scope:** ACh as the meta-level control plane governing the plasticity gain on bottom-up input — how much current experience modifies the hippocampal map
**Depends On:** ARC-005, ARC-007, ARC-018, INV-019, INV-024
**Status:** candidate
**Claim ID:** MECH-083
**New domain:** no prior counterpart in REE claim registry for ACh-specific function

> **Framing note (2026-03-15):** The encoding/retrieval binary switch framing (high ACh = write; low ACh = retrieve) is likely too discrete. A more accurate characterisation is that ACh modulates the *plasticity gain* on bottom-up input: a continuous parameter controlling how strongly incoming sensory evidence modifies map geometry vs. how strongly existing map attractors dominate the interpretation. This preserves the core claim (ACh governs durable write vs. read-through) while capturing the graded nature of the mechanism. The distinction between ACh (plasticity gain: how much this experience updates the map) and NA (attentional snap: whether the system orients to bottom-up surprise right now) is noted below.

Acetylcholine functions as the meta-level control plane, governing the plasticity gain on bottom-up data — specifically, how strongly current sensory experience modifies the hippocampal map geometry rather than being interpreted through existing attractors.

**Mechanism:** ACh modulates a continuous plasticity gain parameter:
- **High ACh (high plasticity gain):** bottom-up input has high weight in updating map geometry; synaptic plasticity in CA3 and dentate gyrus is facilitated; current experience can reshape attractor basin structure. Corresponds approximately to "encoding mode."
- **Low ACh (low plasticity gain):** existing attractor structure dominates; bottom-up input is interpreted through prior map geometry rather than modifying it; pattern completion from stored attractors suppresses novel encoding. Corresponds approximately to "retrieval mode."

The key characterisation is *gain on bottom-up data for learning purposes*, not a discrete mode switch. This is distinct from NA's role (MECH-084): NA controls whether the system *attends* to bottom-up surprise (orienting, moment-to-moment sampling); ACh controls whether that attended input *leaves a lasting trace* in the map.

**ACh vs NA — the key distinction:**
- **ACh (plasticity gain):** *does this input modify the map?* Slow-moving; relevant for the consolidation timescale. High ACh = experience teaches the system.
- **NA (attentional snap):** *does the system snap to this input right now?* Fast-moving; relevant for the moment-to-moment sampling timescale. High NA = system orients toward unexpected bottom-up signals.
- Both increase the *influence* of bottom-up data, but at different timescales and via different mechanisms. High NA + low ACh = attentional snap to surprise without map update (aroused but not learning). High ACh + low NA = steady map updating from the ambient sensory stream without strong orienting responses.

**Meta-level position:** ACh sits above the other three neuromodulatory planes (MECH-084 through MECH-086) because it determines whether operations at those planes leave a lasting trace in the map. Dopamine (MECH-086) can set gain on attractor selection, serotonin (MECH-085) can modulate basin depth, and noradrenaline (MECH-084) can snap attention to bottom-up signals — but if ACh is low, none of these operations will produce durable map updates.

**Relationship to INV-019 and INV-024:** INV-019 states that rehearsal traversal and irreversible durable write must remain separated. INV-024 states offline consolidation and online commitment must remain isolated at responsibility-bearing write loci. ACh modulates the plasticity gain that governs this separation: low ACh = traversal without durable write; high ACh = traversal with write. ACh is the functional instantiation of the durable-write gate at the hippocampal level.

**Failure modes:**
- **Insufficient ACh gating:** plasticity gain inappropriately elevated during retrieval. The map updates from a stuck rollout each time it is traversed — potentially relevant to **OCD** (complements MECH-080) and to certain rumination patterns where replaying a memory reinforces rather than integrates it.
- **Chronically high ACh:** map instability — every traversal re-encodes, preventing stable geometry from forming.
- **Chronically low ACh:** learning failure — bottom-up input never updates the map; new experience is always routed through existing attractors, producing chronic confirmation bias (related to MECH-082).

**Relationship to existing claims:** MECH-083 instantiates one specific axis of ARC-005's control plane — the plasticity gain — with ACh as its neuromodulatory carrier, complementing the dopamine (MECH-043), noradrenaline (MECH-005/MECH-084), and serotonin (MECH-006) analogues already registered.

---

<a id="mech-084"></a>
## Noradrenaline as Attentional Snap and E1/E2 Sampling Ratio Modulator (MECH-084)

**Claim Type:** mechanism_hypothesis
**Scope:** NA as the perceptual-sampling control plane — fast attentional orienting to bottom-up surprise and modulation of the bottom-up/top-down weight ratio at the E1/E2 interface
**Depends On:** ARC-001, ARC-002, MECH-005, MECH-081, ARC-005
**Status:** candidate
**Claim ID:** MECH-084
**Extends:** MECH-005 (noradrenaline path authority and interruptibility)

Noradrenaline provides the *attentional snap* — the fast, moment-to-moment orienting signal that determines whether the system turns toward unexpected bottom-up input. This is distinct from ACh (MECH-083), which governs whether that input then updates the map. Together they control two separable aspects of how bottom-up data is handled: NA determines *whether and how strongly the system orients*; ACh determines *whether that orientation leaves a trace*.

**Mechanism:**
- **High NA (orienting / surprise signal):** reduces E2's constraining influence on E1 (MECH-081 sufficiency constraint). E1 is driven by the bottom-up stream rather than by E2's predictions — the system snaps to unexpected sensory signals regardless of what E2 predicted. This is the *perceptual-level explore signal*, upstream of the planning/rollout system.
- **Low NA:** E2's top-down constraint dominates; E1 samples selectively for dimensions discriminative for E2's current predictions. Processing is efficient but confirmatory — the system does not easily snap to bottom-up surprises that fall outside E2's prediction space.

**The NA/ACh distinction in practice:**
- High NA snaps the system's *current attention* to a bottom-up signal. Whether that signal then rewires the map depends on ACh.
- High NA + low ACh: strong orienting to surprise, no durable map update. Aroused, vigilant, not learning.
- High NA + high ACh: strong orienting to surprise, and the surprise is written into the map. Maximum new learning from unexpected input.
- Low NA + high ACh: steady ambient updating of the map without strong orienting — gradual learning from the background stream.
- Low NA + low ACh: processing dominated by prior predictions and existing map; neither orienting nor learning from bottom-up data.

**Relationship to MECH-005:** MECH-005 defines NA's role in path authority and commitment pressure (downstream effects). MECH-084 adds the upstream account: before commitment, NA is determining how much E1's sensory processing is shaped by E2's model vs. driven by raw bottom-up signals.

**Clinical anchors:**
- **Too little NA:** perceptual confirmation bias — E2 dominates E1; the world confirms existing maps (related to MECH-082).
- **Too much NA (tonic):** pervasive attentional snap to all bottom-up signals, including noise — reduces E2's filtering capacity. PTSD hypervigilance is the archetypal presentation.
- **Too much NA (phasic, dysregulated):** episodic decoupling of E1 from E2 predictions — perceptual experience temporarily runs on bottom-up noise without E2 scaffolding. Candidate mechanism for certain dissociative episodes.

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

**Relationship to MECH-006 (serotonin as representational collapse control):** MECH-006 frames serotonin as controlling representational exclusivity and collapse pressure across representational depths (ρ). MECH-085 frames it as map geometry parameter operating at the hippocampal terrain level. A possible reconciliation: MECH-006's "learning depth" (DepthOfRevision ∝ (1-σ)) is related to MECH-085's "temporal depth of rollouts" — both concern how far forward/deep the system's representations extend and update. However, MECH-006 contains an explicit prohibition ("serotonin does not select temporal depth τ") that is in direct tension with MECH-085's first claim.

**Raphe nucleus / receptor-subtype framing (candidate reconciliation path, 2026-03-15):** The multiple raphe nuclei and the diversity of serotonin receptor subtypes (5-HT1A, 2A, 2C, 3, 4, 6, 7, etc.) mean serotonin likely re-uses the same motif — *modulating resolution pressure / exclusivity* — at different hierarchical levels via different receptor populations and projection targets. Under this framing, MECH-006 and MECH-085 describe the *same serotonergic motif applied at different levels*:
- MECH-006 (dorsal raphe → prefrontal/cortical): serotonin modulates representational collapse/exclusivity at the cognitive-narrative level (ρ-depth exclusivity).
- MECH-085 (median raphe → hippocampal CA1/DG): the same motif applied to hippocampal terrain — modulating how exclusive and deep attractor basins are, and how far rollouts extend before collapsing.

If this reconciliation is adopted, MECH-006's "does NOT select temporal depth τ" should be read as "does not select global τ at the E-stack level" (which remains correct), while MECH-085's rollout-depth claim refers to hippocampal-terrain-level depth — a different construct. This would resolve the apparent conflict without requiring either claim to be retracted, only annotated with level specificity. **Literature pull required to confirm raphe projection specificity and receptor-subtype distribution before this reconciliation can be accepted. Pending adjudication.**

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
