# Parallel processing streams in the hippocampus
**Lee, GoodSmith & Knierim (2020) | Current Opinion in Neurobiology | doi:10.1016/j.conb.2020.03.004**

## What the paper did

Lee, GoodSmith, and Knierim synthesise rodent electrophysiology, lesion studies, and human neuroimaging evidence to argue that the hippocampus is not a single-pathway structure but a set of parallel processing circuits. The central claim is that two anatomically distinct entorhinal input streams carry qualitatively different information into the hippocampus: the lateral entorhinal cortex (LEC) carries object-centered, non-spatial information about individual items and their egocentric relational geometry, while the medial entorhinal cortex (MEC) carries allocentric spatial information via grid cells and border cells. These streams remain partially segregated through dentate gyrus and CA3 before converging in CA1, which receives direct input from both and serves as an integration zone.

## Key findings relevant to SD-015

The most direct relevance is the anatomical dissociation: object identity does not reach the hippocampus through the same channel as spatial location. The LEC projects preferentially to proximal CA1 and distal CA3; the MEC projects to distal CA1 and proximal CA3. This means the hippocampal module must explicitly bind two separately encoded representations -- "what" from LEC and "where" from MEC -- to form an object-place conjunctive memory. The authors are explicit that "the DG and proximal CA3 work as a functional unit for pattern separation" on the LEC stream, while distal CA3 performs pattern completion on the MEC stream. CA1 synthesises these into the episodic representation.

This is precisely the architectural logic behind SD-015. If z_world already encoded everything needed for goal-directed approach, the brain would not maintain a dedicated non-spatial input channel. It does. The LEC stream exists specifically because the "what" information cannot be adequately extracted from the spatial map.

## The REE translation and its limits

In REE terms: z_resource (ResourceEncoder) is the LEC analogue, and z_world is the MEC analogue. Both feed into the hippocampal module, which binds them into goal-relevant object-place representations. The motivation for a dedicated ResourceEncoder is structurally homologous to the brain's motivation for a dedicated LEC stream.

The mapping is directionally strong but has a precision limit worth stating plainly. The LEC in rodents encodes egocentric relational information -- the object's relationship to the animal's current perspective -- rather than purely abstract categorical object-type features. A food pellet at the animal's left is represented differently from the same pellet at its right. This is weaker than the full spatial invariance that SD-015's ResourceEncoder aims for, where world_obs[250] extracts object-type features regardless of position in the scene. IT cortex (covered by DiCarlo 2007 in this same review) achieves the stronger invariance. LEC appears to be an intermediate stage: more spatially invariant than raw sensory input, but not fully position-invariant. The SD-015 ResourceEncoder is closer to the IT cortex end of this spectrum.

## Limitations and caveats

Most of the supporting evidence comes from rodent navigation in mazes or open fields. The extent to which the LEC/MEC segregation translates to more complex, high-dimensional object environments is not fully established. Human fMRI evidence is cited but has lower spatial resolution. The review also notes that LEC is not a pure object-identity module -- it integrates object information with temporal and contextual signals -- so calling it a "what" stream is a useful simplification rather than a precise characterisation.

## Confidence reasoning

This is a high-quality review synthesising a mature literature. The parallel-streams architecture is not controversial -- it is well replicated and consistent with the broader medial temporal lobe organisation. The mapping to SD-015's z_resource/z_world split is structurally compelling. Confidence is set at 0.82: the directional support is strong, but the LEC-to-z_resource analogy has the precision caveat noted above, and the REE ResourceEncoder targets a stronger invariance than LEC alone achieves.
