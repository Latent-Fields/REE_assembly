# Cortical substrates for exploratory decisions in humans

**Class surveyed:** EXPLORE-EXPLOIT MODE | **Evidence direction:** supports | **Confidence:** 0.68

**Source:** Nathaniel D. Daw, John P. O'Doherty, Peter Dayan et al. (2006). *Cortical substrates for exploratory decisions in humans.* Nature 441(7095):876-879 DOI: 10.1038/nature04766

Daw et al. fit human choices in a four-armed restless bandit with an explore-exploit model, classified trials as exploratory vs exploitative, and found frontopolar cortex and intraparietal sulcus preferentially active on exploratory choices while striatum and vmPFC tracked value-based exploitative choice. They frame the result as switching between exploratory and exploitative behavioural modes -- a dedicated cortical system that flips regime, anatomically separate from the valuation system.

For the class-choice this is the strongest biological evidence that exploration is implemented as a *separable mode* with its own substrate (frontopolar/IPS) distinct from the value/exploitation substrate (striatum/vmPFC) -- consistent with a mode variable being a distinct mechanism, not a term folded into value. A mode gate selects which policy regime runs, whereas a novelty bonus only reshapes the reward a single policy optimises.

The honest caveat: the *computational* model they fit was a softmax exploration parameter (random exploration), not an explicit committed-mode latent. So the paper's neural finding argues for the existence and separability of a mode substrate, while its behavioural model is closer to a temperature/bonus. It supports mode-as-distinct-mechanism more than it proves a mode outperforms a bonus at closing a competence gap.

Buildable as a two-headed/gated policy: a mode head (frontopolar analog) emits an explore-exploit signal that arbitrates between an exploratory sub-policy and the value-greedy critic-exploiting sub-policy. Note the frontopolar locus is the same one REE's SD-033e de-commit lever targets. Confidence 0.68.
