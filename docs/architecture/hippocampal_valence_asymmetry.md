# Hippocampal Valence Asymmetry: BLA vs VTA Pathways

> Registered: 2026-04-14
> Claims: MECH-232, MECH-233, ARC-057
> Literature: targeted_review_hippocampal_valence_asymmetry (5 entries)

## The Problem

REE's residue field encodes harm/threat valence directly in hippocampal terrain --
the agent avoids locations with high residue. This maps cleanly to the BLA-hippocampal
pathway (Jimenez 2018: ventral CA1 "anxiety cells"; Redondo 2014: BLA engrams resist
valence reversal). The mechanism is explicit tagging: certain hippocampal cells encode
"this context is dangerous" and drive avoidance via vCA1->LHA projections.

The architectural question: does approach/wanting valence enter hippocampal terrain
the same way? Is there a symmetric "wanting gradient" that mirrors the harm residue
field? The literature says no.

## The Asymmetry

### Threat pathway (BLA -> hippocampus)

- Dedicated valence-coding cells in ventral CA1 (Jimenez 2018)
- Explicit avoidance tags, fast, one-shot (contextual fear conditioning)
- BLA engrams cannot be valence-switched (Redondo 2014)
- Possibly compressed representation (fast detection, not fine spatial detail)
- Maps directly to REE residue field

### Approach pathway (VTA -> hippocampus)

- No equivalent "reward cells" or "wanting cells" found in hippocampus (Jimenez 2018)
- Dopaminergic modulation enhances LTP at reward-associated locations (Lisman & Grace 2005)
- Place cells reorient to represent reward-relevant spatial features; D1 blockade prevents
  reorientation and causes perseveration (Retailleau & Morris 2018)
- Reward-associated items have stronger, more durable memory traces (Wittmann 2005)
- The mechanism is representational expansion, not valence tagging

## MECH-232: DA-Mediated Representational Expansion {#mech-232}

Dopaminergic modulation at reward locations does not write a positive valence tag.
It enhances the fidelity, stability, and associative richness of place representations.
The result: reward-associated locations have more detailed, more durable, more easily
reactivated maps. The approach gradient is implicit in representational quality.

This means the hippocampal terrain at reward locations is effectively "expanded" --
it contains more distinguishable states, more fine-grained spatial features, more
navigable structure in representational space.

## MECH-233: Mechanistic Asymmetry {#mech-233}

The two pathways produce behaviorally similar outputs (avoidance of threat, approach
toward reward) through mechanistically distinct encoding:

| Feature | Threat (BLA) | Approach (VTA-DA) |
|---------|-------------|-------------------|
| Encoding type | Explicit valence tag | Representational expansion |
| Cell type | Dedicated anxiety cells | Enhanced place cells |
| Speed | Fast, one-shot | Gradual, consolidation-dependent |
| Reversibility | BLA engrams resist switching | Expansion decays when DA ceases |
| Map effect | Tags location | Expands representation |
| Curiosity interaction | Wall (avoid) | Open field (explore) |

## ARC-057: Curiosity-Approach Emergence {#arc-057}

The architectural commitment: no explicit wanting gradient is required in hippocampal
terrain. Approach behavior emerges from two interacting mechanisms:

1. **DA-mediated representational expansion** (MECH-232): reward locations have more
   navigable representational structure
2. **Information-seeking drive** (curiosity): the agent explores available structure

The curiosity drive does the same thing everywhere -- it follows available
representational structure. But "available" is asymmetric because dopamine shaped the
map. Reward-associated regions have more structure to explore, so the agent spends
more time there. An observer infers an attractive gradient, but there is no gradient --
there is more map.

### Sub-predictions

1. **Wanting-as-maintenance**: DA re-sharpening on each reward encounter refreshes the
   representational expansion. The map stays expanded as long as the reward contingency
   holds. When rewards stop and DA modulation ceases, expansion decays and approach
   behavior extinguishes.

2. **Wanting-as-sensitivity**: Already-expanded representations encode incoming
   resource/goal gradients at higher fidelity. The agent detects goal signals at
   greater distance because its map of reward-associated areas has higher resolution.

3. **Double dissociation**: Ablating DA modulation degrades approach but not avoidance.
   Ablating explicit valence tags degrades avoidance but not approach. Both components
   are independently necessary for their respective behaviors.

## Substrate Constraint: Environmental Complexity

ARC-057 has a minimum environmental complexity requirement that the current
CausalGridWorld cannot satisfy. The curiosity-approach mechanism depends on
representational expansion capturing genuinely additional information at reward
locations. In the real world, this works: any location has near-fractal complexity
where zooming in reveals more structure (textures, objects, micro-features, social
history). A richer representation at a reward location captures real information
that a coarser one misses.

In a grid world, a cell is a cell. There is nothing more to discover at higher
resolution. Expanding the representation at grid cell (3,4) just encodes the same
sparse features more redundantly. The curiosity drive has nothing additional to
explore, so the approach-emergence mechanism cannot operate.

This does NOT affect the threat/avoidance side. Explicit valence tagging (the BLA
pathway, the harm residue field) works regardless of environmental richness --
tagging a location as dangerous requires no additional spatial detail. The asymmetry
between the two pathways means they have different substrate requirements for testing.

Faithful testing of ARC-057 requires either:
- A richer environment with location-dependent feature complexity
- A conceptual/mind-map space where "locations" have variable information density
- Or acceptance that ARC-057 is a theoretical claim grounded in neuroscience
  literature, testable only when the substrate supports sufficient environmental
  richness

## Implications for REE Architecture

- The **harm residue field** is architecturally correct as-is -- it implements the
  BLA explicit-tagging pathway.
- A symmetric **wanting gradient field** should NOT be added -- it would be
  biologically inaccurate and architecturally redundant.
- Instead, the hippocampal module needs **DA-modulated representational resolution**:
  a mechanism by which reward encounters enhance the spatial detail encoded at those
  locations.
- The **curiosity/exploration drive** (already present or planned) then produces
  approach behavior as an emergent property.
- This resolves the "wanting-in-terrain" question for ARC-007: the approach signal
  IS in the terrain, but as enhanced representational quality, not as a gradient.
