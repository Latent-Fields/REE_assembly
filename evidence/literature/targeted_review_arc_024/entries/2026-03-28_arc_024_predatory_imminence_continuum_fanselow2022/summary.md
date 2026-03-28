# Fanselow 2022 — Negative Valence Systems: Sustained Threat and the Predatory Imminence Continuum

**Source:** Fanselow MS (2022). Negative valence systems: sustained threat and the predatory imminence continuum. *Emerging Topics in Life Sciences* 6(5):467–477. [DOI: 10.1042/ETLS20220003](https://doi.org/10.1042/ETLS20220003)

---

## What the paper did

This is a theoretical review by Michael Fanselow, the originator of predatory imminence continuum (PIC) theory, revisiting the relationship between PIC and the NIMH Research Domain Criteria (RDoC) negative valence constructs. The review traces the history of PIC from Bolles' species-specific defence reactions through the three-mode PIC model (pre-encounter, post-encounter, circa-strike) and then examines whether the RDoC construct of "Sustained Threat" maps cleanly onto the PIC. Along the way, it provides a rich synthesis of the neural circuits underlying each PIC mode and the evidence for continuous vs. threshold-like transitions along the gradient.

## Key findings relevant to ARC-024

The central theoretical claim of PIC is that defensive behaviour is not binary — it is not simply "threat present/absent." Defensive response *topography* (what kind of behaviour) and *vigour* (how intensely) are both determined by the psychological distance of the threat from the prey, which Fanselow & Lester originally called "predatory imminence." The three PIC modes represent regions along this continuum: pre-encounter (distant/uncertain threat: foraging modification, vigilance), post-encounter (detected threat: freezing, analgesia), and circa-strike (near-contact: explosive escape, fight, tonic immobility). Each mode increases in vigour up to a threshold that flips the system into the next mode — but this flip is driven by continuous accumulation of threat-proximity signal, not by a discrete event detector.

Crucially, even pre-encounter defence — the lowest level, corresponding to "there might be a predator somewhere in this environment" — constitutes a positive harm signal before any threat detection occurs. The gradient begins at the moment the agent leaves a position of safety, not at the moment of detected threat or contact. This is precisely the structure ARC-024 claims for the world-latent space: harm signal is non-zero in environments that contain hazards, proportional to proximity and likelihood, approaching asymptotic maximum at contact.

The review also documents the neural circuits: pre-encounter involves medial prefrontal cortex and ventral hippocampus; post-encounter involves the BLA-CeA-PAG circuit; circa-strike shifts toward the dorsal PAG. This maps onto the REE architecture: E3 (vmPFC/hippocampal analog) for distant planning, subcortical circuits (PAG analog) for proximate reflexive response.

## Translation to REE / ARC-024

The predatory imminence continuum is the ethological formalisation of what ARC-024 states in computational terms: the world generates continuous, graded harm signals that increase with proximity to harm sources, approaching an asymptotic limit at the contact event. The three PIC modes are operational definitions of gradient levels: low-gradient (pre-encounter), mid-gradient (post-encounter), and near-asymptote (circa-strike). CausalGridWorldV2's hazard_field, which generates a continuous proximity-proportional harm signal, implements this structure. EXQ-028 (gradient dominance confirmed: mean_dz_world_hazard_approach >> none) and EXQ-029 (E3.harm_eval: none=0.373, approach=0.612, contact=0.666) replicate the PIC gradient structure in the simulated environment.

The PIC also provides a theoretical account of *why* the gradient must exist: evolution selected for defensive behaviour calibrated to threat distance because binary at-contact detection fails to protect organisms that need to begin defensive preparation before the predator strikes. An agent whose harm signal activates only at contact cannot act in time. This evolutionary argument maps directly onto REE's architectural claim that E2/E3 require a gradient world to learn meaningful harm evaluation and attribution.

## Limitations and caveats

The PIC describes three discrete modes rather than a fully continuous mathematical gradient. The transitions are threshold-like — there is a point at which pre-encounter flips to post-encounter — which could be interpreted as evidence for partial discretisation rather than the pure continuous gradient ARC-024 posits. However, within each mode the vigour of the response is continuous, and the mode-switching itself is driven by continuous threat-distance accumulation, so the overall structure is better described as a piecewise-continuous gradient than a binary signal.

The review is primarily grounded in rodent literature, with human data referenced but not the primary evidence base. This introduces animal-to-human transfer risk, though this risk is significantly mitigated by Mobbs et al. 2007, which demonstrates that the same continuum structure holds in human fMRI with virtual threat. The review's main focus is on the sustained threat construct and the role of BST/hippocampus, rather than the gradient structure per se, which is treated as established background.

## Confidence reasoning

Confidence assigned 0.78. Mapping fidelity is the strongest in this batch: the PIC directly defines the gradient structure ARC-024 claims at the level of both behaviour and neural circuit, providing an independent theoretical derivation of the same architectural necessity. Source quality is solid — this is the field originator writing an authoritative review — though the journal (Emerging Topics in Life Sciences) is lower-tier than Science or Nature. Transfer risk is moderate because the animal-to-human inference is required, but it is well-supported by the broader PIC-in-humans literature.

*According to PubMed, this article is available at PMID 36286244. [DOI: 10.1042/ETLS20220003](https://doi.org/10.1042/ETLS20220003)*
