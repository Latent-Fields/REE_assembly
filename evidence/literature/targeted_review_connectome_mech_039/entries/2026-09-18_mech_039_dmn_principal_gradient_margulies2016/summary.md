# Margulies et al. (2016) -- Situating the default-mode network along a principal gradient of macroscale cortical organization

*PNAS 113(44):12574-12579 -- doi:10.1073/pnas.1608282113 -- PMID 27791099*

## What the paper did

Decomposing connectivity data in humans and in the macaque, the authors extract a principal gradient of cortical organisation anchored at one end by regions serving primary sensory and motor functions and at the other by transmodal regions -- in humans, the default-mode network. The DMN regions turn out to lie at the greatest geodesic distance along the cortical surface from primary sensory and motor landmarks, and to be *precisely equidistant* from them. The gradient also organises other large-scale networks spatially and, in a functional meta-analysis, characterises "a spectrum from unimodal to heteromodal activity". The conclusion the paper draws is the one it is famous for: the DMN's cognitive role "might arise from its position at one extreme of a hierarchy", rather than from its being a discrete system with a dedicated job.

## Why it belongs in a MECH-039 pull

MECH-039's headline is *not separate modules*, and this is the canonical demonstration that the most module-like object in systems neuroscience is better described by where it sits on a graded axis than by being a bounded thing. It licenses the general architectural stance behind the claim: a named regime can be fully specified by coordinates, without needing a module to own it. And it gives the default-mode-like mode in particular a principled non-modular description, which is useful because that is the mode REE is most at risk of reifying.

## Why I have recorded it at low confidence anyway

Because the continuum this paper establishes is **spatial**, and MECH-039's is **temporal**. That is not a quibble; it is an equivocation waiting to happen, and I would rather it sat in the record than be rediscovered by a future session reading the title.

The gradient is a property of the connectivity *architecture* -- how regions are laid out with respect to one another on the cortical sheet. MECH-039 is a claim about the trajectory of control state *over time*. A system whose components are continuously graded in anatomical space can still switch between a small number of discrete operating regimes from moment to moment; the two properties are close to orthogonal. Put concretely: the claim's falsifying signature -- transitions that are instantaneous and simultaneous across all channels -- could obtain in full, and everything in this paper would remain exactly as reported. So the paper neither confirms nor falsifies what MECH-039 actually asserts, and citing it as support for the dynamics claim would be trading on an ambiguity in the word "continuous".

Two further limits are worth naming. A single principal gradient is a one-dimensional object; MECH-039's confirming signature requires clustering structure in a *joint* space spanned by six channels, which a one-dimensional embedding cannot exhibit. And gradient decomposition of a connectivity matrix returns continuous components by construction -- diffusion-map and PCA-style embeddings have no mechanism for emitting discrete cluster labels -- so "the DMN lies on a continuum" is partly a statement about the method's output space. The paper's evidence *against* modularity is a little weaker than it reads.

## Calibration

Confidence 0.58, which is deliberately low for a paper of this stature, and the components say why. Source quality 0.88: PNAS, human and macaque convergence, extensively replicated and extended in the decade since. Mapping fidelity 0.45 is what holds the entry down -- the paper's "continuous" and the claim's "continuous" refer to different axes, and the overlap is largely one of vocabulary. Transfer risk 0.55, the highest in this pull, for the same reason. Per the guidance for architectural claims I have weighted mapping fidelity heavily rather than taking a mean of the components, which would have put this near 0.6 and overstated it.

The entry is included so that the corpus carries the caveat *alongside* the citation. The DMN-is-not-a-module literature is genuinely relevant to how REE talks about modes, and genuinely does not settle the dynamics question; both of those should be findable in the same place.
