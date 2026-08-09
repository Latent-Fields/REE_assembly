# Knudsen & Wallis (2021) — Hippocampal neurons construct a map of an abstract value space

*Retag entry, 2026-08-09.* This paper was already in the corpus as a Q-020 entry
(`targeted_review_q_020/entries/2026-03-29_q020_abstract_value_map_knudsen2021`). It is MECH-144's
second founding citation but was never tagged to MECH-144, so MECH-144 read as having zero
literature coverage. This record adds that tagging. See the direction-sign note at the bottom for
why it is a separate record rather than an extra id on the existing one.

## What the paper did

Knudsen and Wallis recorded single units in macaque hippocampus during an abstract value-based
decision task in which three options carried different relative reward magnitudes. Rather than
asking whether hippocampal neurons encode value, they asked whether the encoding has the
*structure* of a place map — testing four properties diagnostic of spatial place cells against the
abstract value space.

## Key findings

Hippocampal neurons exhibit "value place fields": tuned responses to positions in the abstract
value space. All four diagnostic properties hold — consistency across repeated experiences,
multidimensional tuning, directional selectivity, and remapping in novel contexts. The fields
generalize across contexts as experience accumulates. The authors' conclusion is constructive
rather than correlational: hippocampus *builds* the value map, it does not merely receive one.

## REE translation

MECH-144 asserts that valence is intrinsic to hippocampal map geometry rather than externally
applied. This paper supplies the constructive half of that claim. The four-property parallelism is
what makes it a *geometry* result rather than a *coding* result — value is represented in the same
representational format as space, so a value-structured prior can be part of the map's own format.
That is precisely the form MECH-144 needs for the MECH-143 / MECH-144 dorsal-ventral dissociation
to hold: a prior encoded in the geometry, not computed during planning.

## Limitations and honest caveats

Two gaps, and the first is load-bearing for this particular tagging.

**Compartment.** MECH-144 is stated as a *ventral* CA1 claim. This is primate hippocampus recorded
without a dorsal/ventral assignment, so the paper supports "hippocampus builds value maps" more
directly than it supports "the ventral compartment does". The compartment specificity that makes
this evidence fit MECH-144 is exactly what the paper does not establish.

**Value type.** The value space is abstract relative reward magnitude in a choice task, not harm or
anxiety geography. Whether value place fields would emerge for aversive residue is untested, and
REE's residue field conflates harm, goal, and spatial salience.

## Confidence reasoning

Confidence 0.70, deliberately set *below* the Q-020 sibling entry's 0.78. Source quality is
identical (0.93 — same paper), but mapping fidelity is lowered to 0.60 from 0.68 and transfer risk
raised to 0.42 from 0.38, both for the compartment mismatch above: MECH-144 names ventral CA1
specifically, which is a tighter mismatch against this recording than the compartment-agnostic
Q-020 was. Jimenez 2018 is the stronger of MECH-144's two legs; this one is the broader-scope,
looser-fit corroboration.

## Note on the direction sign

This record is `evidence_direction: supports`; the Q-020 record on the same paper is `weakens`.
Both are correct, and the difference is the reason this is a separate record rather than an added
id on the existing one. The paper weakens Q-020's ARC-007 "hippocampus is value-free" framing
*precisely by* supporting MECH-144. `evidence_direction` is a single per-record field that the
indexer applies uniformly to every id in `claim_ids_tested` (there is no per-claim direction on the
literature path, unlike experiment manifests), so tagging MECH-144 onto the existing `weakens`
record would have registered this paper as *contradicting* the claim it founds. Splitting the
record is the corpus's own established convention for this — cf. Camille 2004 (`supports` ARC-029 /
`weakens` Q-090) and Mattar & Daw 2018 (`supports` in twelve records, `weakens` in the Q-011 one).
Full reasoning in `evidence/planning/literature_claim_tag_audit.md`.
