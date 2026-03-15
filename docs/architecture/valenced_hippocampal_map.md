# Valenced Hippocampal Map, Amygdala Read/Write, and Therapeutic Geometry

**Source thought:** Theoretical development session 2026-03-15 (NC-01 through NC-09)
**Registered:** 2026-03-15

> **CONFLICT NOTICE (for Daniel's judgment):**
> NC-01 and NC-02 (ARC-022, MECH-073) assert that valence is intrinsic to hippocampal map geometry and that rollouts are inherently valenced simulations. This is in direct tension with ARC-007's defining design constraint: "No value computation. Its function is orthogonal to valuation and control."
> Two resolution paths are available:
> **(A) Revise ARC-007** to distinguish "the hippocampus does not *compute* new value" (still denied) from "the hippocampus *embodies* geometrically-encoded value written by the amygdala and shaped by the residue field" (permitted). This preserves INV-014 (representation and regulation are separated) while accepting that the map's topology is itself value-laden through prior write operations.
> **(B) Reject MECH-073** as structurally incompatible with REE's strict commitment to hippocampal value-neutrality, and reclassify NC-01/NC-02 as an external neuroscience model that *inspires* but does not enter the canonical architecture.
> **Neither resolution is taken here. Both ARC-022 and MECH-073 are registered as candidates, flagged for adjudication.**

> **FRAMING NOTE for ARC-022:**
> NC-01 describes a biological hierarchy (E1→Cerebellum→DMN→Goal/Avoid→Hippocampus). In REE terms, the mapping is: Cerebellum = E2's functional role (per Q-019); DMN = the ARC-014 operating *mode*, not a sequential pipeline layer; Goal/Avoid systems = E3 + control-plane valence channels. ARC-022 registers the *abstraction hierarchy* claim (each layer outputs typed objects consumed natively by the next) while the biological labels are treated as approximate functional analogues.

---

<a id="arc-022"></a>
## Hierarchical Effect-Object Abstraction Pipeline (ARC-022)

**Claim Type:** architectural_commitment
**Scope:** Typed-object abstraction hierarchy across REE processing layers
**Depends On:** ARC-001, ARC-002, ARC-007, ARC-014, ARC-021, MECH-070
**Status:** candidate
**Claim ID:** ARC-022
**⚠ Conflict with:** ARC-007 (hippocampal valence constraint — see notice above), ARC-014 (DMN as mode vs. pipeline layer)

The REE architecture implements a hierarchical effect-object pipeline in which each processing layer abstracts the outputs of the layer below into typed objects that the next layer operates on natively. The sequence, mapped to REE components, is:

1. **E1** — produces motor/sensory prediction objects: predicted sensory latents and residuals against the perceived present.
2. **E2 (cerebellar-like motor model)** — consumes E1 latent objects and produces temporally structured self-in-world trajectory predictions: `f(z_gamma_t, a_t) → z_gamma_{t+1}`. Objects at this layer are latent-object transitions, not raw sensory predictions. (In biological terms: cerebellum; in REE terms: E2/MECH-070.)
3. **Default-Mode regime / DMN** — consumes E2 transition kernels chained into multi-step sequences and produces possible strings of effects: narrative simulations and counterfactual trajectory bundles. (In REE terms: the ARC-014 operating regime running over hippocampal rollouts; not a separate processing module.)
4. **Goal/Avoid systems** — consumes narrative simulations and produces a valenced possibility space: which trajectories are approach-relevant vs. avoidance-relevant. (In REE terms: E3 + control-plane valence channels, MECH-035, MECH-054, MECH-055.)
5. **Hippocampus** — consumes the valenced possibility space and provides a valenced cognitive map: a navigable terrain of attractors over which trajectory proposals are generated. (Contested against ARC-007 — see conflict notice.)

**Architectural claim (abstraction-hierarchy):** each layer operates on the output type of the layer below without needing to re-instantiate lower-level computations. This layered typed-object principle explains why E2 operates on z_gamma (not raw sensory streams), why hippocampal rollouts chain E2 kernels rather than re-running E1, and why E3 commits to trajectory proposals that already carry valence signals.

This claim is compatible with ARC-021 (three incommensurable learning channels) because the abstraction hierarchy describes what *each layer operates on*, while ARC-021 describes what *error signal trains each layer*.

---

<a id="mech-073"></a>
## Valence Intrinsic to Hippocampal Map Geometry (MECH-073)

**Claim Type:** mechanism_hypothesis
**Scope:** Joint structure-value encoding in hippocampal map topology
**Depends On:** ARC-007 (conflict), ARC-013, MECH-035, MECH-074
**Status:** candidate
**Claim ID:** MECH-073
**⚠ Conflict with:** ARC-007 ("No value computation. Its function is orthogonal to valuation and control.")

Valence is intrinsic to hippocampal map geometry, not applied downstream by an external evaluator. The hippocampal cognitive map is a joint structure-value representation. Evidence anchors:

- **Place cell over-representation:** rewarded locations are over-represented relative to map area, meaning the metric geometry of the map is warped toward value-relevant zones.
- **Reward and aversive cells within hippocampal circuitry:** distinct cell classes directly encode value-related signals inside hippocampal networks, not only in downstream structures.
- **Map warping around value-relevant zones:** psychological distances between representations are compressed near high-value attractors and expanded elsewhere.

**Consequence for REE:** if this claim is accepted, rollouts (hippocampal trajectory proposals, ARC-018) are inherently valenced simulations rather than neutral trajectories evaluated by an external comparator. The "no value computation" constraint in ARC-007 would need to be reread as "no new value computation by the hippocampus itself" — the hippocampus carries pre-written value structure installed via amygdala write operations (MECH-074) and residue-field shaping (ARC-013).

**Consequence if rejected:** MECH-073 is demoted; ARC-007 stands; NC-01 through NC-09's valence-in-map framing is treated as an external neuroscience model that partially diverges from canonical REE.

---

<a id="mech-074"></a>
## Amygdala as Read/Write Head for the Valenced Hippocampal Map (MECH-074)

**Claim Type:** mechanism_hypothesis
**Scope:** Four functional roles of the amygdala analogue operating on hippocampal map geometry
**Depends On:** MECH-046, MECH-073, ARC-007, ARC-013
**Status:** candidate
**Claim ID:** MECH-074
**Extends:** MECH-046 (amygdala analogue and mode priors)

The amygdala analogue in REE functions as a write and reading head for the valenced hippocampal map. This extends MECH-046 (which characterises the amygdala as a fast salience classifier updating mode priors) with four specific read/write roles:

1. **Modulating encoding (write strength):** BLA→hippocampus projections during consolidation determine what gets written strongly vs. weakly into map geometry. High-arousal events produce deeper attractor basins; low-arousal events produce shallower, more plastic encodings.

2. **Biasing retrieval (read head):** under elevated arousal, the amygdala analogue pulls map activation toward threat-relevant regions, prioritising retrieval of aversive or danger-associated trajectories over neutral ones.

3. **Rapid pre-cortical priming (fast subcortical route):** a fast subcortical pathway provides a crude valence prior before full hippocampal map activation completes. This bootstraps the system's initial response to a stimulus before elaborated trajectory rollout begins. This role is absent from MECH-046's current specification.

4. **Triggering map updating (remapping signal):** when outcomes violate expectation (prediction error spike), the amygdala analogue drives remapping or reweighting of affected hippocampal map regions — initiating reconsolidation of distorted or outdated map geometry.

**Relationship to MECH-046:** MECH-046 remains correct and is not superseded. MECH-074 adds a richer account of the amygdala's operations *on the map itself*, whereas MECH-046 describes its role in mode-prior updating for the control plane. Both are simultaneously active: the amygdala updates mode priors (MECH-046) and modulates hippocampal map read/write (MECH-074).

---

<a id="mech-075"></a>
## Basal Ganglia: Dopaminergic Gain/Threshold Setting on Hippocampal Attractor Dynamics (MECH-075)

**Claim Type:** mechanism_hypothesis
**Scope:** BG role as attractor gain/threshold modulator rather than external value comparator
**Depends On:** Q-019, ARC-021, MECH-043, MECH-073
**Status:** candidate
**Claim ID:** MECH-075
**Extends:** Q-019 (three-gate BG architecture), ARC-021 (three learning channels), MECH-043 (dopamine-like precision)

The basal ganglia perform gain and threshold setting on attractor dynamics in the valenced hippocampal system, rather than performing external value comparison among independently generated rollouts.

**Mechanism:**
- **Dopamine from VTA/SNc sets threshold and urgency:** tonic dopamine sets the baseline attractor depth threshold below which a basin is not activated; phasic dopamine bursts lower the threshold transiently, facilitating entry into reward-relevant attractors.
- **Competitive inhibition in striatum gates basin activation:** direct-pathway neurons disinhibit thalamocortical targets for selected attractor basins; indirect-pathway neurons suppress competing basins. Selection is therefore a property of attractor dynamics modulated by dopaminergic tone, not an explicit comparison operation over externally scored trajectories.

**Relationship to ARC-021 three loops:**
- The sensorium loop BG gate (ARC-021 loop 1) sets attractor thresholds for perceptual representation.
- The action-enacting loop BG gate (ARC-021 loop 2) modulates motor-sensory attractor selection.
- The planning-gates loop (ARC-021 loop 3) is the primary locus of hippocampal attractor gating described here.

**Relationship to MECH-043:** MECH-043 describes dopamine-like modulation of precision-weighting for unsigned prediction errors. MECH-075 extends this to the specific mechanism of attractor-basin threshold setting in the hippocampal planning context — precision-weighting and attractor threshold setting are complementary aspects of dopaminergic function operating at different levels of the hierarchy.

---

<a id="mech-076"></a>
## Residue as Structural Deformation of Hippocampal Map Topology (MECH-076)

**Claim Type:** mechanism_hypothesis
**Scope:** Neural substrate of residue curvature in hippocampal structural geometry
**Depends On:** ARC-013, MECH-056, MECH-073
**Status:** candidate
**Claim ID:** MECH-076
**Extends:** ARC-013 (residue as latent-space curvature)

Residue (previously defined in REE as persistent curvature over latent space, ARC-013) is instantiated, at the hippocampal level, as geometric distortion of map topology rather than as a separate inhibitory filter or scoring layer.

**Mechanisms of structural deformation:**
- **Over-representation:** high-arousal early experiences allocate disproportionate map area to their content, creating zones of compressed psychological distance around aversive or salient attractors.
- **Abnormally deep attractor basins:** stressed or traumatic encoding creates attractor wells that are abnormally hard to leave, biasing rollouts to repeatedly traverse those regions.
- **Reduced neurogenesis in dentate gyrus under chronic stress:** new neurons are required for pattern separation (keeping similar trajectories distinct); stress-impaired neurogenesis reduces map resolution and separation capacity, causing interference between related episodes.
- **Stress-driven dendritic retraction in CA3:** reduces the integration capacity of CA3, compressing the representational space available for complex multi-episode synthesis.
- **Palimpsest traces from incomplete reconsolidation:** failed reconsolidation leaves partially overwritten trajectory encodings that distort subsequent rollouts without cleanly replacing the prior encoding.

**Relationship to MECH-056 (trajectory-first residue placement):** MECH-056 prescribes placing residue pressure in trajectory feasibility and commitment gating before distorting core representations. MECH-076 is compatible: the *terrain itself* is deformed (map topology distortion = the residue field ARC-013 describes), which acts precisely as trajectory-level pressure (rollouts are attracted or repelled by basin geometry) without requiring a separate inhibitory mechanism layered on top of perception.

**Relationship to ARC-013:** MECH-076 provides the specific neural substrate for the curvature field φ(z) posited in ARC-013. The curvature is not merely an abstract quantity — it corresponds to observable structural properties of the hippocampal map.

---

<a id="mech-077"></a>
## Therapeutic Change as Hippocampal Remapping (MECH-077)

**Claim Type:** mechanism_hypothesis
**Scope:** Clinical/therapeutic implications of hippocampal map geometry restructuring
**Depends On:** ARC-013, MECH-076, MECH-018, MECH-073
**Status:** candidate
**Claim ID:** MECH-077
**New domain:** no prior counterpart in REE claim registry

Therapeutic change corresponds to hippocampal remapping — restructuring the geometry of the valenced map — rather than adding corrective propositional content. Different therapeutic modalities operate at different levels of this process:

| Modality | Level of operation | REE analogue |
|---|---|---|
| **CBT** | OFC/vmPFC read of existing map | Updates the *evaluation* of the existing map without restructuring map geometry; changes what trajectories are selected from a largely fixed terrain. |
| **EMDR** | Reconsolidation of distorted map regions under low arousal | Targets MECH-076 palimpsest traces; low-arousal bilateral stimulation enables partial rewriting of map topology during reconsolidation windows. REE analogue: offline consolidation with arousal suppressed (MECH-018). |
| **Psychodynamic therapy** | Gradual geometry restructuring via sustained relational experience | Slow iterative update of map topology through repeated relational episodes; accumulates across many consolidation cycles. REE analogue: slow-rate residue integration (ARC-013 two-rate pipeline, slow cortical consolidation pathway). |
| **Psychedelic-assisted therapy** | Large-scale map restructuring via temporary attractor flattening | Transient reduction in attractor depth across the map (flattening MECH-076 basins), creating a window in which new geometry can be written before basins re-deepen. REE analogue: temporarily reducing κ (commitment stability) across the residue field while new trajectories are encoded. |

**Implication for REE:** this claim grounds the mechanism of ethical learning and self-change in hippocampal map geometry. If an agent's map is severely distorted (MECH-076), behavioral change cannot be achieved by adding propositional content alone — it requires map-level restructuring, which in REE terms means sustained engagement with offline consolidation (MECH-018) or controlled attractor-flattening mechanisms.

**Note:** this claim is clinical/theoretical and not directly testable in current V2 substrate. It is registered as candidate to anchor future therapeutic-analogue experiment design.

---

<a id="mech-078"></a>
## Amygdala Bootstrap Valence for Unmapped Territory (MECH-078)

**Claim Type:** mechanism_hypothesis
**Scope:** Amygdala function for novel/unmapped hippocampal territory; anxiety disorder aetiology
**Depends On:** MECH-046, MECH-074, MECH-073
**Status:** candidate
**Claim ID:** MECH-078
**Extends:** MECH-046, MECH-074

Novel valence assignment for unmapped territory is primarily an amygdala function. The amygdala analogue provides bootstrap valence for representations with no prior hippocampal map entry.

**Mechanism:**
1. A stimulus or context activates a latent representation for which the hippocampal map contains no existing attractor structure (unmapped territory).
2. The amygdala analogue provides a rapid prior-valence estimate (MECH-074 role 3: fast subcortical priming) based on low-dimensional feature similarity to previously encoded threat/reward-relevant content.
3. This initial valence is written into the hippocampal map through consolidation (MECH-074 role 1: encoding modulation), extending the map into new regions with prior-seeded value estimates.
4. Subsequent experience with the novel territory refines the map entry, updating attractor basin depth and position.

**Anxiety disorder aetiology:** anxiety disorders may reflect systematic over-valencing of novel/unmapped territory as aversive. The amygdala analogue applies a prior that strongly weights novel stimuli as threat-relevant, creating large initial aversive basins in unmapped map regions. This biases subsequent experience-based map refinement toward confirming the initial aversive prior, producing stable anxiety-maintaining map geometry.

**Relationship to REE control plane:** this mechanism interacts with MECH-040 (safety baseline and volatility): novel/unmapped territory raises volatility (safety volatility is high when the system lacks a stable map entry), which raises arousal, which strengthens amygdala encoding (MECH-074 role 1) — a positive feedback loop that could produce over-valenced map entries. Control-plane dampening of this loop may be a target for anxiety modelling.

---

<a id="mech-079"></a>
## Phenomenological Selfhood as Stable Hippocampal Map Geometry (MECH-079)

**Claim Type:** mechanism_hypothesis
**Scope:** Continuous subjective selfhood as artefact of stable hippocampal map topology; identity change as map phase transition
**Depends On:** ARC-007, ARC-013, MECH-024, MECH-073
**Status:** candidate
**Claim ID:** MECH-079
**Extends:** MECH-024 (selfhood, personality, ethics converge structurally)

The phenomenological sense of continuous selfhood is partly an artefact of stable hippocampal map geometry.

**Mechanism:** the same map topology produces similar rollouts and similar attractor resolutions across time. Because trajectory proposals arise from the same basin structure, similar starting conditions generate similar candidate trajectories, producing similar commitments and similar experienced outcomes. This structural consistency generates the subjective sense of being the same agent across time — not as a separate "self-module," but as a phenomenological property of map stability.

**Consequences:**
- Gradual character change: slow map restructuring (MECH-077 psychodynamic analogue) produces the experience of gradual character development while preserving phenomenological continuity.
- Profound identity-level change: corresponds to a phase transition in map geometry — a wholesale reorganisation of attractor basin structure such that the system's characteristic rollout profile shifts discontinuously. This is experienced as identity discontinuity or transformation (as in acute psychosis, major depressive episode, or profound spiritual/psychedelic experience).
- Memory: episodic memory (ARC-007 path storage) and prospective simulation both arise from the same map. The feeling that memories "belong to me" arises from the continuity between past-path geometry and current-basin geometry.

**Relationship to MECH-024:** MECH-024 asserts selfhood, personality, and ethics converge structurally. MECH-079 specifies *what* that structure is (hippocampal map geometry) and *why* stable structure produces continuous selfhood (same topology → similar rollouts → similar commitments → subjective identity persistence).

**Relationship to INV-006 (post-commit traces are persistent):** map-level residue from past commitments is structurally encoded (MECH-076), making the ethical history of the agent a permanent component of map geometry. The self that emerges from stable map topology therefore already incorporates its ethical past — selfhood and moral history are co-constituted.

---

<a id="mech-080"></a>
## Rollout Truncation Set-Points as Psychiatric Individual Differences Substrate (MECH-080)

**Claim Type:** mechanism_hypothesis
**Scope:** Individual differences in rollout sampling depth and truncation as substrate for ADHD, anxiety, and OCD
**Depends On:** ARC-018, MECH-027, ARC-014, MECH-075
**Status:** candidate
**Claim ID:** MECH-080
**Extends:** MECH-027 (pathological modes = mis-tuned control-plane regimes), ARC-014 (default mode failure modes), ARC-018 (rollout generation)

Rollout sampling depth and truncation set-points may be a substrate for individual differences in psychiatric conditions. Two signals modulate these parameters:

- **Uncertainty (hippocampal/noradrenergic):** drives *more* rollout sampling — when the map lacks a confident attractor, the system samples more trajectories to find a viable one.
- **Urgency signals (dopaminergic/BG, MECH-075):** truncate sampling — when an attractor is sufficiently dominant or time pressure is high, sampling is cut short and the current basin is committed.

**Differential profile:**

| Condition | Rollout pattern | Mechanism |
|---|---|---|
| **ADHD** | Truncation-biased: sampling ends prematurely; commitment occurs before adequate trajectory exploration | Urgency signal (BG dopaminergic threshold, MECH-075) set too low; any emerging attractor captures commitment before alternatives are explored. Explore/exploit ratio biased toward exploit. |
| **Anxiety** | Extension-biased: sampling continues beyond useful depth; commitment suppressed even when a viable attractor is clearly dominant | Uncertainty signal chronically elevated (from over-valenced unmapped territory, MECH-078); BG threshold set too high; system cannot commit despite adequate trajectory coverage. Explore/exploit ratio biased toward explore. |
| **OCD** | Attractor lock-in: sampling is not extended but loops within a specific attractor region; system cannot exit a dominant aversive basin | Abnormally deep attractor basin (MECH-076) creates escape-proof region; uncertainty and urgency signals are normal in magnitude but basin geometry prevents transition. Characteristic pattern: repeated re-sampling of same trajectory class. |

**Relationship to ARC-014 failure modes:** ARC-014 already identifies ADHD-like dynamics (premature default-mode intrusion into task-engaged operation) and rumination loops (replay within narrow curvature regions). MECH-080 extends these with a unified mechanistic account (rollout truncation set-points) that differentiates ADHD from anxiety from OCD at the parameter level.

**Testable implication in REE:** varying the urgency/uncertainty balance in the rollout sampling algorithm should produce characteristic trajectory-commitment profiles that map onto the three conditions. EXQ experiments targeting rollout-parameter variation could provide model evidence for MECH-080.

---

## Open Questions

**Q-020 — Does ARC-007's "no value computation" constraint survive MECH-073?**
If the hippocampal map is a joint structure-value representation (MECH-073), the constraint in ARC-007 that "its function is orthogonal to valuation and control" must be revised or the valence-in-map claims must be rejected. This is the pivotal question for whether the NC-01 through NC-09 cluster integrates into canonical REE architecture.
Status: open. Pending Daniel's adjudication.

---

## Related Claims (IDs)

- ARC-022
- MECH-073
- MECH-074
- MECH-075
- MECH-076
- MECH-077
- MECH-078
- MECH-079
- MECH-080
- Q-020
- ARC-007 (conflict)
- ARC-013
- ARC-014
- ARC-018
- ARC-021
- MECH-024
- MECH-027
- MECH-043
- MECH-046
- MECH-056
- MECH-073
- Q-019

## References / Source Fragments

- Theoretical development session 2026-03-15 (NC-01 through NC-09)
