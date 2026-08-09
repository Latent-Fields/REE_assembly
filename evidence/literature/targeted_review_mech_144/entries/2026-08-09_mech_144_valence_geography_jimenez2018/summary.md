# Jimenez et al. (2018) — Anxiety Cells in a Hippocampal-Hypothalamic Circuit

*Retag entry, 2026-08-09.* This paper was already in the corpus as a Q-020 entry
(`targeted_review_q_020/entries/2026-03-29_q020_valence_geography_jimenez2018`). It is MECH-144's
founding citation but was never tagged to MECH-144, so MECH-144 read as having zero literature
coverage. This record adds that tagging. See the direction-sign note at the bottom for why it is a
separate record rather than an extra id on the existing one.

## What the paper did

Jimenez and colleagues used GCaMP6f calcium imaging in freely moving mice to record ventral CA1
during standard anxiety assays (open field, elevated plus maze), then used channelrhodopsin and
halorhodopsin to test whether the population they found was causally involved rather than merely
correlated. They asked whether vCA1 activity is organized by the *aversiveness* of a location, not
just by position.

## Key findings

A distinct population of vCA1 neurons — "anxiety cells" — fires selectively in anxiogenic zones,
scaling with proximity to open/exposed space. The tuning is stable across sessions rather than a
transient state signal, and it is spatially organized: the population tiles the environment by
affective value. Optogenetic activation drove avoidance; silencing reduced it, establishing
necessity rather than correlation. The circuit runs vCA1 → lateral hypothalamus, anatomically
distinct from the basal amygdala pathway that carries fear memory.

## REE translation

MECH-144 claims that ventral CA1 contains spatially organized valence encoding — that valence is
intrinsic to hippocampal map geometry in the ventral compartment, rather than computed elsewhere
and tagged on afterwards. This paper is the direct empirical instantiation of exactly that: the
affective sign is carried by the geometry of the map itself.

Its architectural significance is the dissociation it enables. MECH-143 (dorsal CA1 value-free,
from Duvelle 2019) and MECH-144 (ventral CA1 valence-encoding) are co-true because they concern
different compartments. That is the mechanism by which ARC-007's no-new-value-computation
constraint survives for the trajectory-proposal module while a ventral valence prior still shapes
R(x,t) — the prior is *encoded in* the geometry, not *computed during* planning.

## Limitations and honest caveats

The finding is ventral CA1, in mouse. MECH-144's second leg (primate abstract value maps, Knudsen
& Wallis 2021) is a different compartment and species, so neither paper alone covers the claim's
full stated scope. The optogenetics establish that the anxiety-cell population is necessary for
avoidance but do not resolve the representational geometry — whether valence is a smoothly tiled
gradient over space or a thresholded tag on certain zones is not distinguished, and MECH-144's
"geometrically embedded" wording is the stronger of those two readings. Transfer from open-field
and elevated-plus-maze mouse anxiety to an agent's harm-residue navigation is a substantial
abstraction step.

## Confidence reasoning

Confidence 0.72, carried over unchanged from the Q-020 sibling entry rather than raised. Mapping
fidelity is a little better here (0.68 vs 0.62) because MECH-144 is stated at the ventral-compartment
level the paper actually measures, so the dorsal/ventral abstraction gap that penalised the Q-020
mapping does not apply. But transfer risk is identical (0.42), and that is what holds the overall
figure where it was.

## Note on the direction sign

This record is `evidence_direction: supports`; the Q-020 record on the same paper is `weakens`.
Both are correct, and the difference is the reason this is a separate record rather than an added
id on the existing one. The paper weakens Q-020's ARC-007 "hippocampus is value-free" framing
*precisely by* supporting MECH-144's ventral-valence-encoding claim — one finding, opposite signs
against two different propositions. `evidence_direction` is a single per-record field that the
indexer applies uniformly to every id in `claim_ids_tested` (there is no per-claim direction on the
literature path, unlike experiment manifests), so tagging MECH-144 onto the existing `weakens`
record would have registered this paper as *contradicting* the claim it founds. Splitting the
record is the corpus's own established convention for this — cf. Camille 2004 (`supports` ARC-029 /
`weakens` Q-090) and Mattar & Daw 2018 (`supports` in twelve records, `weakens` in the Q-011 one).
Full reasoning in `evidence/planning/literature_claim_tag_audit.md`.
