# Mobbs et al. 2007 — When Fear Is Near: Threat Imminence Elicits Prefrontal-Periaqueductal Gray Shifts in Humans

**Source:** Mobbs D, Petrovic P, Marchant JL, Hassabis D, Weiskopf N, Seymour B, Dolan RJ, Frith CD (2007). *Science* 317(5841):1079–83. [DOI: 10.1126/science.1144298](https://doi.org/10.1126/science.1144298)

---

## What the paper did

Fourteen healthy human participants navigated a virtual maze while being pursued by a digital predator that could deliver an electric shock upon capture. The paradigm was designed so that the spatial distance between participant and predator varied continuously, and the shock magnitude was either low or high. Whole-brain fMRI was recorded throughout. The authors asked whether there was a systematic shift in brain-region activation as a function of threat proximity — not just whether the brain responds to threat, but how the *pattern* of response changes as the threat draws closer.

## Key findings relevant to ARC-024

The central result was a continuous, distance-graded shift in neural activity from the ventromedial prefrontal cortex (vmPFC) toward the periaqueductal gray (PAG) as the virtual predator approached. At distal threat distances, vmPFC activation dominated — a region associated with complex planning, cost-benefit appraisal, and flexible avoidance strategy. As the predator closed the distance, PAG activation increased and PAG activity correlated directly with subjective dread ratings and reduced confidence in escape. At near-contact distances, the defensive response reorganised around PAG-mediated reflexive behaviour.

This is not a binary switch but a gradient: the transition occurs across a range of threat distances, and the intermediate distances produce mixed activation profiles. The implication is that the brain does not simply detect "harm" as a binary signal at the moment of contact — it represents harm as a graded, distance-dependent quantity that begins influencing neural processing and behaviour well before any aversive contact occurs.

## Translation to REE / ARC-024

ARC-024 asserts that harm signals in world-latent space have asymptotic proxy structure: they are graded, continuous, and approach an asymptotic limit at the contact event (death) rather than being binary. The Mobbs et al. finding provides the neural instantiation of exactly this structure. The vmPFC-to-PAG gradient maps directly onto what CausalGridWorldV2's hazard_field implements computationally: a continuously varying harm-proximity signal that increases in magnitude as the agent approaches the hazard source. The experimental result that E3.harm_eval learns to distinguish approach from contact (EXQ-029: none=0.373, approach=0.612, contact=0.666) mirrors the behavioural gradient observed in human participants — harm signal magnitude increases along the approach trajectory before any contact occurs.

The paper also supports the architectural motivation for why REE must use a gradient world rather than a contact-only world: if the brain uses graded harm signals for flexible avoidance planning (vmPFC at distance, PAG at contact), then any computational test of harm evaluation must expose the system to the gradient, not only to binary contact events.

## Limitations and caveats

The study uses a virtual predator with known shock magnitudes, which produces unusually predictable gradient structure. Real-world harm sources vary in speed, trajectory, and magnitude, meaning that the gradient is typically noisier. Additionally, the sample is small (n=14) and all healthy adults, which limits generalisability to pathological gradient distortions (anxiety disorders, PTSD) or developmental stages. The inference that neural gradient = world-latent gradient representation requires an additional step: this paper shows the brain *uses* graded threat signals, not directly that the brain represents them in a structured latent space of the kind REE proposes.

## Confidence reasoning

Confidence assigned 0.78. Source quality is high (Science journal, first-author work by Mobbs who went on to lead the predatory imminence neuroscience literature). Mapping fidelity is strong: the spatial proximity gradient in this paradigm directly corresponds to the hazard_field proximity structure in CausalGridWorldV2. Transfer risk is modest: the virtual-threat paradigm is unusually clean compared to naturalistic harm sources, but the gradient mechanism appears robust across replications.

*According to PubMed, this article is available at PMID 17717184. [DOI: 10.1126/science.1144298](https://doi.org/10.1126/science.1144298)*
