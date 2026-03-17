# Literature Summary: 2026-03-17_mech097_parietal_cortex_sight_action_rizzolatti1997

## Claims Tested

- `MECH-097`

## Source

- Rizzolatti G, Fogassi L, Gallese V (1997). *Parietal cortex: from sight to action*. Current Opinion in Neurobiology, 7(4), 562–567.
- DOI: `10.1016/s0959-4388(97)80037-2`
- URL: `https://pubmed.ncbi.nlm.nih.gov/9287198/`

## Source Wording

Premotor area F4 and parietal areas 7b/VIP contain neurons that respond to visual, tactile, and somatosensory stimuli within a dynamically defined near-body region — peripersonal space (PPS). These neurons encode stimulus positions in body-part-centered (egocentric) coordinates: head-centered, arm-centered, trunk-centered. The PPS boundary is not anatomically fixed: it extends to the tip of a held tool, scales with motor reach, and shifts with attentional focus. Objects entering PPS trigger qualitatively different neural processing than objects outside it. PPS is the spatial zone in which motor commands produce world-directed sensory consequences — where the body's action-execution machinery intersects with the external world.

## REE Translation

**MECH-097 (peripersonal space as commit locus)**: PPS defines the spatial boundary at which z_self (body-state, motor-sensory, E2's domain) and z_world (allocentric environment, E3's domain) first interact. In REE:

- **Inside PPS**: body-relative space, z_self coordinates, action consequences are immediate and proprioceptively direct
- **PPS boundary crossing**: the moment at which a motor action produces a world-directed effect — contamination, contact, object displacement
- **Outside PPS**: world space, z_world coordinates, consequences are causal chains extending beyond immediate body contact

In CausalGridWorld, contamination occurs exactly at the PPS boundary: the agent's positional state (z_self) contacts the cell state (z_world). This is not a fixed threshold — PPS scales dynamically with motor context and attentional state. In REE terms, z_beta modulates the effective PPS boundary: high harm salience → contracted PPS boundary (more conservative commit locus); routine operation → extended PPS (broader action reach). This connects MECH-097 to ARC-016 (z_beta-gated commitment precision) and MECH-093 (z_beta modulates E3 heartbeat rate).

**Architectural implication for SD-005**: SD-005's z_self/z_world split requires an architectural representation of where self ends and world begins in spatial terms. Without a PPS-equivalent structure, the encoder has no principled basis for routing observations to z_self vs z_world — the routing decision degenerates to a fixed threshold or a learned heuristic. MECH-097 grounds the routing mechanism in a dynamically updated body-centered spatial frame.

## Caveat

PPS is characterised in macaque premotor/parietal cortex. The mapping to a latent-space commit boundary requires two inferential steps (PPS → commit boundary, commit boundary → residue trigger) that are REE-specific. CausalGridWorld's discrete grid is a simplified proxy for the continuous PPS boundary. The moral-residue application is not in the source.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.72`
