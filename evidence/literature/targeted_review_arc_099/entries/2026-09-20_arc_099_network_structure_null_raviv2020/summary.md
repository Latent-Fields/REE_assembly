# The Role of Social Network Structure in the Emergence of Linguistic Structure (Raviv, Meyer & Lev-Ari, Cognitive Science, 2020)

## Why a null is in this pull

The chip that commissioned this pull asked, among other things, whether there are null results in the primary human group-size literature. There is one, and it is not a null on group size -- it is a null on the variable that most people assumed was group size's real mechanism.

## What the paper did

Same lab, same paradigm, same artificial-language group communication task as the 2019 Proceedings B study. This time community size was held fixed at eight and the *shape* of the interaction graph was manipulated: fully connected (everyone meets everyone), small-world (mostly local connections with a few long-range ones), and scale-free (a hub who talks to nearly everyone, with peripheral members who talk to almost no one). 168 adults, 21 groups, seven per condition.

The prediction being tested was not speculative. Computational models of language change, the Linguistic Niche Hypothesis literature, and the esoteric-versus-exoteric distinction in sociolinguistics all converge on the claim that sparsely connected communities develop more systematic languages while tightly knit ones maintain complexity and variability. As the authors put it, the role of social network structure in the cultural evolution of languages had never been tested experimentally. They tested it.

## What it found

Nothing. "Results did not reveal any effect of network structure for any measure, with all languages becoming similarly more systematic, more accurate, more stable, and more shared over time." The one residue is a variance effect: small-world networks showed the greatest variation across groups in convergence, stabilisation and structure, which the authors interpret as differential susceptibility to drift rather than a directional influence.

## What this does to ARC-099

It does two opposite things, which is why the direction here is `mixed` rather than `weakens`.

**It relieves the contract of a parameter.** If ARC-099 is to be a machine-checkable V6-entry gate, the most expensive kind of item is one that requires specifying the ecology's interaction graph -- because a graph is a large object and getting it wrong is invisible. This experiment says that at constant community size, the graph did not change what emerged along any of the four measured dimensions. The gate can leave it unspecified. That is a real economy, and it is the kind of thing only a null can tell you.

**And it is a cautionary case about how to amend the inventory.** Read alongside the 2019 group-size result, the pair says something sharper than either alone: the amount of distinct input an agent receives matters, and the topology by which that input arrives does not. The 2019 mediation analysis had already relocated the mechanism to input variability; this null is what you would expect if that relocation is correct, because all three topologies at n = 8 deliver broadly comparable input variability to a given participant even though they differ wildly in who-meets-whom.

The cautionary part concerns Galke et al. 2022, the entry that prompted this pull. Their argument is that ARC-099 omits two constraints that are load-bearing in humans, one of which -- speaker/listener role alternation -- is a property of the ecology's interaction protocol. This paper is the only direct experimental test of an interaction-protocol property in this literature, the prediction it tested had at least as much theoretical backing as the role-alternation proposal has, and it came back null. That is not an argument that role alternation does not matter. It is an argument that strong theoretical motivation about interaction protocols has, in the one case where it was checked in humans, not survived the check -- and that ARC-099 should therefore not absorb role alternation as a *human*-warranted item. As the Rita 2022 and Galke & Raviv 2024 entries in this directory show, the actual evidence for role coupling comes from the artificial-agent side, not the human side. That matters for how the item, if added, should be justified.

## Limitations

Seven groups per condition is the number to keep in mind. This detects a reasonably large effect and would miss a small one, so "network structure does not matter" means "no effect detectable at this scale in this task". The elevated variance in small-world groups is itself a hint that topology may be doing something the means cannot see -- and if topology modulates drift rather than direction, sixteen rounds is probably too short for drift to accumulate into a directional difference. A V6 ecology run for very many more interaction rounds than a human afternoon is precisely the regime where an effect this experiment could not detect might appear.

## Confidence

0.66, `mixed`. Source quality 0.82, mapping fidelity 0.64, transfer risk 0.45. I have deliberately not treated this null as strong evidence of absence; it is evidence that one plausible refinement of ARC-099's partner-variation item is not worth adding, and a warning about the evidential standard that should be applied to the other refinements currently on the table.
