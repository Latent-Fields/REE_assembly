# Aston-Jones & Cohen 2005 -- LC-NE adaptive gain (re-anchored against ARC-066)

**Citation:** Aston-Jones G, Cohen JD. An integrative theory of locus coeruleus-norepinephrine function: adaptive gain and optimal performance. *Annual Review of Neuroscience*. 2005;28:403-450. PMID: 16022602. DOI: 10.1146/annurev.neuro.28.061604.135709.

## What the paper does

Aston-Jones & Cohen 2005 is the foundational integrative theory of LC-NE function. It proposes that LC neurons have two modes -- phasic (bursting locked to decision outcomes, facilitates exploitation of the current task) and tonic (sustained elevated firing, associated with task disengagement and search for alternative behaviours). Adaptive gain through ACC + OFC monitoring of task utility gates the tonic-phasic mode switch. The paper has been the standard reference for explore-exploit neural circuitry for two decades and is cited >5000 times.

This same paper appears as an entry in the ARC-065 (behavioural diversity generation pathway) lit-pull, where its mapping was to MECH-313 (LC-NE tonic NOISE FLOOR). The current ARC-066 entry tags the same paper to a DIFFERENT mapping: the user-pre-registered claim that LC-NE tonic mode also provides a *directional* action-bias function distinct from MECH-313. The same paper supporting two different REE claims via two different readings is allowed because the conceptual content of the 2005 review is consistent with both readings -- the empirical disambiguation is what determines which mapping survives.

## Why the mapping for ARC-066 is mixed-direction

The R2 verdict (noise-vs-direction LC-NE disambiguation) is the central question for this entry. At the theoretical level, Aston-Jones & Cohen 2005 is consistent with EITHER reading:

- **Noise reading:** high tonic LC firing increases neural gain uniformly, which raises the variance of the decision distribution, which produces patch-leaving / disengagement / exploration via random-walk effects. This is the MECH-313 mapping.
- **Direction reading:** high tonic LC firing biases the system toward action / disengagement via a systematic shift of decision thresholds, separate from any noise effect. This is the pre-registered ARC-066 mapping.

The 2005 theoretical paper does not run a model comparison to disambiguate. The empirical resolution is Kane et al. 2017 (separate entry, by the same authorship group), which used DREADDs to selectively elevate LC tonic firing in rats and ran a formal model comparison: the resulting earlier patch-leaving was best explained by an INCREASE IN DECISION NOISE rather than a SYSTEMATIC BIAS. The noise reading was supported; the direction reading was not.

Under the R2 verdict, this paper is therefore a MIXED entry for ARC-066:

- Supports the broader architectural commitment (there is a tonic substrate that biases toward action / disengagement under appropriate utility conditions).
- Does NOT support the specific disambiguation that the LC-NE substrate provides this function as direction-rather-than-noise.

The mapping to ARC-066 should therefore be that this paper motivated the slot's ORIGINAL anchor cluster but the empirical follow-up rejected the LC-NE attribution. The 2005 paper remains useful as a *boundary* anchor (clarifying what ARC-066 is NOT and what mechanisms exist nearby) but is no longer a load-bearing positive-direction anchor for ARC-066's substrate attribution. The DA-vigor substrate (Niv 2007 / Salamone & Correa 2012 / Beierholm 2013) replaces it in the substrate-attribution role.

## What this means for the architecture family doc

The synthesis recommends governance update the family doc (`docs/architecture/non_deficit_action_drives.md`) anchor cluster:

- REMOVE: Aston-Jones & Cohen 2005 from the primary ARC-066 anchor cluster.
- ADD: Aston-Jones & Cohen 2005 + Kane 2017 in a "what ARC-066 is NOT" section, clarifying that LC-NE tonic mode is one mechanism (noise = MECH-313), not two.
- KEEP: Niv 2007, Salamone & Correa 2012, Beierholm 2013, Walton 2003, Depue & Collins 1999 as substrate / formal / empirical / ACC / abstract anchors respectively.

This is a reframe of the slot's biological substrate attribution. It does NOT split the slot (the architectural function ARC-066 names is still real -- the substrate attribution is just different than the registration assumed). Slot-splitting is governance-level work, not lit-pull work.

## Confidence reasoning

Source quality is high (foundational review, top venue, decades of citation use). Mapping fidelity is materially lower than the ARC-065 entry (0.55 vs 0.80) because the empirical follow-up disconfirmed the direction-over-noise reading the ARC-066 mapping depended on. Transfer risk is elevated for the same reason. Aggregate 0.62, mixed direction. The downgrade from 0.84 (ARC-065 mapping) to 0.62 (ARC-066 mapping) reflects: same paper, different REE claim, the second reading is empirically weaker.

According to PubMed, this paper appears under PMID 16022602; this is the same paper indexed in the ARC-065 lit-pull entry, intentionally re-indexed here against a different REE claim and with a different evidence direction.
