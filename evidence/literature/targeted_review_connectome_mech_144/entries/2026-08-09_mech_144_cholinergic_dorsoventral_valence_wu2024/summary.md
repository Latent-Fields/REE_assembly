# Septo-hippocampal cholinergic projections and the dorsoventral valence split (Wu et al., 2024, Science Advances)

## What the paper did

Wu and colleagues identified two distinct basal forebrain cholinergic subpopulations in mice -- one projecting to dorsal hippocampus, one to ventral -- and characterised them across four levels: input organisation, electrophysiological properties, transcriptomics, and responses to positively and negatively valenced stimuli. They then asked what each contributes behaviourally under chronic stress, and whether the contributions can be dissociated pharmacologically.

## Key findings relevant to the claim

The two populations are distinct on every measure taken, including their responses to stimulus valence. Functionally they dissociate cleanly: the ventral-projecting population is critical for emotional modulation, the dorsal-projecting one for cognitive modulation. Chronic stress produced elevated anxiety and cognitive deficits alongside *enhanced* ventral and *suppressed* dorsal cholinergic projections. Chemogenetic activation of the dorsal projection, or inhibition of the ventral one, alleviated the stress-induced behavioural phenotype -- and donepezil combined with M1 muscarinic blockade in ventral hippocampus rescued both symptom domains.

## How this translates to REE

MECH-143 and MECH-144 jointly presuppose that the hippocampal dorsoventral axis is functionally partitioned along something like a spatial/cognitive versus emotional line. This paper corroborates that presupposition from an entirely independent direction -- neuromodulatory input organisation rather than hippocampal recording -- which is worth something precisely because it does not share the methodological assumptions of the place-cell literature.

The more interesting contribution is that the partition turns out to be *reweightable*. Chronic stress shifts the balance toward the ventral pole, and rebalancing it chemogenetically reverses the behavioural phenotype. If REE takes anything architecturally useful from this, it is that a dorsal/ventral weighting over R(x,t) should be a state-dependent parameter under something like a stress or arousal variable, not a constant fixed at design time. That is a modest but concrete suggestion, and it is not something the place-cell literature would have surfaced.

## Limitations and caveats

I want to be blunt about this entry's standing, because its source quality could otherwise carry more weight than its relevance deserves. It measures cholinergic *input* and no spatial coding whatsoever. It therefore cannot discriminate between valence that is intrinsic to the ventral map -- MECH-144's actual assertion -- and valence that is tagged onto a ventral structure from outside. Since that distinction is the entire content of the claim, this paper corroborates the *frame* around MECH-144 rather than MECH-144 itself, and if the ventral valence signal turned out to be wholly input-driven this evidence would look exactly the same.

There is also a further transfer step: this is a chronic stress model, and MECH-144 is not a claim about stressed animals. The dorsoventral asymmetry reported here may be partly a stress phenomenon rather than a baseline architectural fact.

## Confidence reasoning

0.45, deliberately below the moderate band despite source quality of 0.80. Mapping fidelity (0.35) is weighted heavily because MECH-144 is an architectural claim about where valence *lives*, and this design cannot address that; transfer risk (0.45) reflects both the rodent-to-architecture step and the stress-model confound. Direction is **supports**, but supports-the-frame -- it should not be counted as evidence that valence is geometrically embedded in the ventral map.
