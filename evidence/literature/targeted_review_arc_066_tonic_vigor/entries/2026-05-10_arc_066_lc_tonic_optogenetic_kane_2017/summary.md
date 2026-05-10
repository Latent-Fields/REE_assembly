# Kane, Vazey, Wilson, Shenhav, Daw, Aston-Jones & Cohen 2017 -- LC-NE tonic stimulation = noise, not direction

**Citation:** Kane GA, Vazey EM, Wilson RC, Shenhav A, Daw ND, Aston-Jones G, Cohen JD. Increased locus coeruleus tonic activity causes disengagement from a patch-foraging task. *Cognitive, Affective, & Behavioral Neuroscience*. 2017;17(6):1073-1083. PMID: 28900892. DOI: 10.3758/s13415-017-0531-y.

## What the paper does

This is the most informative single empirical test on the noise-vs-direction question for LC-NE tonic mode. Kane et al. used DREADDs (designer-receptor chemogenetic stimulation) to selectively elevate LC tonic firing in Long-Evans rats performing a patch-foraging task. The task required repeated decisions to either exploit a depleting reward patch or pay a time cost to travel to a new full patch. The Aston-Jones & Cohen 2005 adaptive-gain theory predicts that elevated LC tonic activity should cause earlier disengagement (= more exploration, more patch-leaving). The empirical question Kane et al. addressed -- via formal model comparison -- was *how*: does the disengagement come from a directional shift of the leave threshold (consistent earlier leaves), or from increased decision noise (more variable leaves around the same threshold)?

The result is unambiguous in the abstract: "This effect is best explained by an increase in decision noise rather than a systematic bias to leave earlier (i.e., at higher values)." The behaviour pattern under elevated LC tonic activity is *noisier*, not *biased*.

## Why this is the load-bearing R2 paper for ARC-066

The user-registered ARC-066 anchors include Aston-Jones & Cohen 2005 with the explicit gloss that LC-NE tonic mode provides a "directional bias TOWARD action, not noise on choice", distinct from MECH-313's already-substrate-landed noise-floor function. The R2 verdict the synthesis must produce is whether this is correct -- whether LC-NE tonic mode is one mechanism with two faces (noise + direction) or two mechanistically separable functions.

Kane et al. 2017 is the direct causal test. The authorship matters: Aston-Jones (original theory) and Cohen (theory co-author) are co-authors on this paper. These are the people most motivated to find a directional-bias component if one existed. They ran a clean DREADD manipulation, fit a formal model comparison, and reported noise-best-explanation. The implication for ARC-066 is direct and substantive:

- LC-NE tonic mode is fully covered by MECH-313 (noise floor / softmax temperature lift).
- There is no remaining LC-NE function for ARC-066 to claim.
- ARC-066's substrate attribution must lean on mesolimbic DA-vigor (Niv 2007, Salamone & Correa 2012) and the BAS abstract level (Depue & Collins 1999), not on LC-NE.

This is a substantive correction of the slot's pre-registered anchor cluster. The architecture family doc (`docs/architecture/non_deficit_action_drives.md`) currently lists Aston-Jones as a primary anchor for ARC-066. The synthesis recommends governance update that anchor downward: Aston-Jones should be cited as evidence for what ARC-066 is NOT (i.e. it is not LC-NE-direction; LC-NE tonic mode is noise, which is MECH-313 territory). Slot-splitting is not warranted -- the architectural function ARC-066 names is real (capacity-keyed positive bias toward action), it just has a different substrate than the registration assumed.

## Caveats

The patch-leaving readout in Kane et al. is closer to ARC-068 (opportunity cost / when to disengage) than to ARC-066 (when to engage). The strict relevance for ARC-066 is via the general substrate-level claim that LC-NE tonic effects are noise-mediated, which transfers to any task readout. A subtle caveat: the abstract says noise BETTER explains the data, not that a directional component is fully ruled out. A small directional contribution might be undetectable in this design. However, under current evidence the default attribution should be noise-only, and the burden is on any LC-NE-direction account to produce its own causal evidence.

A second concern: DREADDs activation produces a non-physiologically uniform LC firing pattern compared to natural tonic-mode firing. If natural LC tonic firing has spatial / temporal heterogeneity that DREADDs miss, a directional-bias function might be present in natural firing but lost under DREADDs. This is a plausible but speculative caveat -- the absence of a positive empirical anchor for LC-NE-direction means it cannot serve as a load-bearing substrate for ARC-066 even if the door is left ajar.

## Confidence reasoning

Source quality is high: causal optogenetic-equivalent manipulation, formal model comparison, top-tier authorship including the original LC-NE theory team. Mapping fidelity is moderate-high -- the patch-leaving readout is not exactly the act-vs-not-act selection ARC-066 names, but the noise-vs-direction disambiguation is the same architectural question. Transfer risk is moderate: rat patch foraging maps onto REE foraging-style environments reasonably well, and the mechanistic claim is at the substrate level. Aggregate 0.82 -- the load-bearing R2 paper for the synthesis with weakens-direction (specifically: weakens the LC-NE attribution of ARC-066).

According to PubMed, this paper appears under PMID 28900892 with DOI 10.3758/s13415-017-0531-y.
