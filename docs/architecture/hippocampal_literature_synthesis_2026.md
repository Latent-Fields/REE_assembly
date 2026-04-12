---
nav_exclude: true
---

# Hippocampal Literature Synthesis 2026

**Date:** 2026-04-02
**Scope:** Synthesis of targeted literature pull covering 10 hippocampal clusters. Primary purpose: resolve Q-020, ground MECH-074/075 with citation anchors, assess ARC-007's "no value computation" constraint, and identify remaining gaps.
**Total new entries:** 14 papers across 7 literature directories
**Author:** Lit-pull session, 2026-04-02

---

## 1. Q-020 Ruling: Valence in Map Geometry

**Status: RESOLVED — Resolution A adopted.**

### The conflict

Q-020 pits two claims against each other:

- **ARC-007** (hippocampus stores trajectory paths, no value computation) specifies that hippocampus is a relational structure that binds episodes without computing value or encoding valence directly.
- **MECH-073** (valence intrinsic to hippocampal map geometry) claims that place cell over-representation of reward zones, and dedicated reward-coding CA1 neurons, constitute valence as part of the map's geometry — making value intrinsic to the map, not an external label.

### The evidence

The literature pull produced three key papers whose combination resolves Q-020:

**Dupret et al. (2010)** — Place fields reorganise around reward zones after learning. The spatial geometry of CA1 is literally compressed toward reward locations: place fields become denser, smaller, and stronger near reward. This is map deformation in response to value-relevant experience. It strongly supports MECH-073's claim that valence is geometrically encoded.

**Gauthier & Tank (2018)** — A dedicated, anatomically stable population of CA1 and subiculum neurons fires near reward zones *across environments* — not place-specific but reward-zone-specific. These cells are the strongest challenge to ARC-007's "no value computation" claim: they appear to encode something about reward proximity as such, not merely co-occurring spatial context.

**Bittner et al. (2017) — BTSP** — Behavioral time-scale synaptic plasticity is the mechanistic key to the resolution. CA1 plateau potentials — which initiate BTSP and write place fields into the synaptic matrix in single trials — are triggered by behaviorally relevant signals arriving at CA1 dendritic tufts. Crucially, the triggering signal does not originate in CA1 itself; it originates from external inputs (entorhinal cortex, BLA direct projections, VTA inputs) that coincide with reward or salient events. BTSP is a *write operation executed by external agents* using CA1 dendrites as the physical medium. The hippocampus does not decide what to write strongly; external systems (BLA, VTA, EC) determine when to trigger plateau potentials.

### The resolution

**Resolution A is correct:** The hippocampus embodies value-shaped geometry, but this geometry is *written by external systems* (BLA via arousal/NE, VTA via RPE/dopamine, EC via sensory predictions), not computed by hippocampus itself. The distinction is:

| Resolved | Not resolved |
|----------|-------------|
| HPC geometry is warped by value-relevant experience | HPC computes value, encodes RPE, or evaluates outcomes |
| Reward zones produce denser, stronger place fields (Dupret) | Place cells themselves compute reward |
| Dedicated reward-zone cells exist (Gauthier) | These cells perform value computation |
| BTSP writes geometry in response to external triggers (Bittner) | HPC decides write-strength based on internal valuation |

The Gauthier reward-coding cells are consistent with Resolution A if they are interpreted as stable anatomical relay stations for BLA/VTA input rather than value-computing units. Their across-environment stability (they fire near reward regardless of the spatial context) is more consistent with a fixed BLA projection target than with a flexible value-computing population — a value computer should adapt to changing reward contingencies in a way that would disrupt across-environment stability.

### ARC-007 verdict

ARC-007's "no value computation" constraint **survives with a clarification**: hippocampus does not compute value, but it *stores the geometric trace of value-weighted experience*. The map is not value-neutral (MECH-073 is correct that valence is geometrically encoded) but hippocampus is not the agent doing the weighting (ARC-007's core constraint holds). Both claims are simultaneously true via the BTSP mechanism.

**Recommended action:** Update ARC-007's notes field to include: "The 'no value computation' constraint is compatible with hippocampal geometry being value-shaped. The constraint specifies only that the *computation* of value (RPE, utility, outcome prediction) occurs in BG/amygdala/PFC, not in hippocampus. Hippocampus stores the geometrically encoded result of those computations via BTSP-mediated write operations (Bittner 2017). MECH-073 and ARC-007 are co-true under Resolution A (Q-020 closed)."

---

## 2. MECH-074: Amygdala Write Interface — Citation Anchors

MECH-074 now has two literature entries providing its biological foundation:

**McGaugh (2004) — Ann Rev Neurosci** [animals, pharmacology]
Canonical demonstration that BLA modulates consolidation strength via NE/cortisol/direct projections. Establishes the write-head architecture: BLA is a modulator, not a storage site. Grounds MECH-074's role 1 (write-strength modulation) and role 2 (retrieval bias).

**Dolcos, LaBar & Cabeza (2004) — Neuron** [human, fMRI]
Human fMRI evidence that amygdala-MTL functional connectivity at encoding predicts emotional memory enhancement. Arousal-dependence confirms that the write-head activates for both harm and benefit events (both high-arousal). Grounds MECH-074 in human data, closing the species transfer gap.

The mechanistic chain is now complete: emotional event → BLA activation (McGaugh) → BLA-MTL connectivity predicts encoding depth (Dolcos) → BTSP plateau potential triggered in CA1 (Bittner 2017) → place/trajectory field written into viability map with enhanced depth. Each link has a citation anchor.

---

## 3. MECH-075: Dopaminergic Gain — Required Reframing

**Important finding from Kempadoo et al. (2016, PNAS):** VTA dopaminergic axons are sparse in dorsal hippocampus. Dopamine in dorsal hippocampus comes primarily from locus coeruleus (LC), which co-releases dopamine and norepinephrine. LC stimulation in dorsal HPC enhances spatial memory.

**Implication for MECH-075:** The claim that "BG dopaminergic signals set gain on hippocampal attractor basins" is anatomically incomplete. A subdivision is required:

| HPC Axis | Gain Modulator | Functional Trigger | REE Role |
|----------|---------------|-------------------|---------|
| Dorsal (spatial/planning) | LC catecholamines (DA/NE co-release) | Novelty, arousal, prediction error | Sets encoding depth for new trajectory segments |
| Ventral (affective/motivational) | VTA dopamine | Reward prediction error, BG signal | Sets value-weighting of harm/benefit trajectories |

The Lisman & Grace (2005) VTA-HPC loop (already in `targeted_review_v3_hippocampal_rollout`) primarily describes VTA→ventral HPC coupling via the novelty detection circuit. This is real and important for REE's motivational weighting. But the planning/spatial circuit in dorsal HPC is modulated by LC, not VTA.

**Recommended action:** Add an `anatomical_note` to MECH-075's claims.yaml entry: "BG/VTA dopamine primarily modulates ventral HPC (motivational/affective weighting). Dorsal HPC (spatial/planning substrate, E3 viability map) is primarily modulated by LC catecholamines responding to novelty/arousal (Kempadoo 2016). MECH-075's gain mechanism bifurcates by HPC axis."

---

## 4. ARC-007: Challenges and Defenses Summary

### Challenges identified by the literature pull

**Gauthier & Tank (2018)** — Dedicated stable CA1/subiculum reward-zone cells. These fire near reward across environments and resist the pure-indexer characterisation. If these cells represent reward proximity as such (not merely co-occurring spatial context), ARC-007's "no value computation" claim faces genuine pressure. This is the strongest challenge in the evidence set.

**Dupret et al. (2010)** — Geometric compression of place fields near reward. This is a map deformation driven by value, which MECH-073 correctly characterises as valence intrinsic to geometry. ARC-007 survives only because the *computation* of this value (which locations are worth compressing around) happens externally.

### Defenses that hold

**Teyler & Rudy (2007)** — Indexing theory. HPC stores sparse cortical indices, not content. The indexer role is fundamentally neutral: the hippocampus records "what happened together," not "what it was worth." The value-weighting is in the write operation, not the storage operation.

**Bittner 2017 (BTSP)** — The plateau potential mechanism shows that hippocampus is a write *recipient*, not a write *agent*. The cellular mechanism of value-geometry writing is initiated by external signals (BLA, EC, VTA), not by intrahippocampal value computation.

**McGaugh 2004 + Dolcos 2004** — Both confirm that amygdala modulates HPC encoding strength without being a storage site. The modulator/storage-site distinction is exactly ARC-007's architecture: external systems write valence into HPC geometry; hippocampus stores the result.

### Verdict

ARC-007 holds under Resolution A. The "no value computation" constraint means hippocampus does not evaluate outcomes, does not compute RPE, does not assign utility. It does store geometry that has been shaped by those computations via BLA/VTA/EC write operations. The Gauthier cells are the only genuine threat — if future work establishes that those cells update their reward-zone tuning in response to value changes (not just spatial context changes), this would require further revision.

---

## 5. New Claims Warranted by This Evidence Pull

One finding requires a claim update; no new claims need registration:

**MECH-075 anatomical subdivision** — The LC→dorsal HPC / VTA→ventral HPC distinction should be captured in MECH-075's notes but does not warrant a new claim. The functional principle (catecholaminergic gain on hippocampal attractor basins) is unchanged; only the anatomy is more specific.

---

## 6. Evidence Grounding Summary by Claim

| Claim | Before pull | After pull | Key new entries |
|-------|------------|-----------|----------------|
| Q-020 | Open conflict | Resolved → Resolution A | Dupret 2010, Gauthier 2018, Bittner 2017 |
| ARC-007 | 3 entries, v3_pending | Strengthened + clarified | Teyler 2007 (indexing theory) |
| ARC-018 | 2 entries, v3_pending | Strengthened | Johnson & Redish 2007 (VTE sweeps) |
| MECH-074 | 0 entries | Founded | McGaugh 2004, Dolcos 2004 |
| MECH-075 | 0 entries (Lisman 2005 in v3_rollout) | 1 entry; requires reframing | Kempadoo 2016 |
| MECH-077 | 1 entry | Strengthened + anatomically constrained | Leutgeb 2005, Fanselow & Dong 2010 |
| MECH-092 | 0 direct entries | Founded | Karlsson & Frank 2009 |
| MECH-163 | 1 entry | Strengthened + division of labor | Benchenane 2010, Preston & Eichenbaum 2013 |
| MECH-022 | 3 entries | Strengthened | Karlsson & Frank 2009 (awake remote replay) |

---

## 7. Remaining Gaps After This Pull

### Gaps not addressed in this pull

**Cluster 1 (subfield architecture)** — Neunuebel & Knierim (2014) direct recording of DG pattern separation vs. CA3 completion, and MacDonald et al. (2011) hippocampal time cells, remain unpulled. These would ground MECH-033's E2→HPC interface at the subfield level. Low urgency given existing CLS theory coverage.

**Cluster 8 (dopamine gain — VTA→ventral HPC)** — The Kempadoo paper grounds dorsal HPC catecholaminergic gain but the VTA→ventral HPC story (Lisman & Grace 2005, already in evidence set) needs a dedicated ventral HPC entry to complete the MECH-075 subdivision. This is a medium-priority gap.

**Cluster 10 (event segmentation)** — Brunec & Moscovitch's prediction error drives hippocampal event segmentation paper remains unpulled. This would strengthen the ARC-007 segmentation specification's "sharp prediction error" trigger criterion. Low urgency given Baldassano 2017 already provides direct neural evidence.

**ARC-035 specific grounding** — vmPFC→CA1 direct projection evidence (anatomical tract tracing or optogenetics) is missing. The Preston/Eichenbaum review establishes the functional principle but direct anatomical grounding for the vmPFC→HPC node interface claimed by ARC-035 requires dedicated search (Tierney et al., or vmPFC-CA1 connectivity literature).

**MECH-076 therapeutic rate remapping** — Fear extinction + hippocampal remapping (Hainmueller or Bhattacharya) remains unpulled. The Leutgeb 2005 entry grounds the theoretical framework; experimental evidence in fear/trauma context is needed to close this gap.

### What the pull closed

The critical P1 gap (Q-020 valence conflict) is resolved. MECH-074 is now grounded with two citation anchors (McGaugh animal pharmacology, Dolcos human fMRI). MECH-092's quiescent remote replay is grounded by Karlsson/Frank. ARC-007's indexing theory foundation is explicit. The dorsal/ventral anatomical constraint on therapeutic remapping is established. The LC/VTA dopamine dissociation has been captured and requires a MECH-075 note update.

---

## 8. Recommended Immediate Actions

1. **Update claims.yaml** — ARC-007: add Q-020 resolution note. MECH-075: add LC/VTA anatomical subdivision note.
2. **Close Q-020** — Formally close the question as "resolved_resolution_a" with BTSP as the mechanistic key.
3. **Run governance.sh** — The new literature entries will update literature_confidence for all affected claims.
