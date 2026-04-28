# Bradfield, Hart & Balleine 2018 -- Anterior mOFC and inference of action-dependent outcomes

## What the paper does

The Balleine lab has spent two decades using selective lesion + structured behavioural paradigms to dissect goal-directed action in rats. This paper extends that programme into the heterogeneity of medial OFC itself: prior work established that mOFC (broadly) is necessary for inferring outcomes that cannot be observed from the current sensory state, and this paper asks whether that function is uniformly distributed across mOFC or localised within an anteroposterior gradient.

Two converging methods. First, retrograde tracing from five regions known to participate in goal-directed action (mediodorsal thalamus, basolateral amygdala, posterior dorsomedial striatum, nucleus accumbens core, VTA) showed that anterior mOFC has substantially denser projections to nucleus accumbens core than posterior mOFC. Second, excitotoxic lesions targeted to anterior versus posterior mOFC were tested across three behavioural paradigms that probe outcome-specific knowledge: Pavlovian-instrumental transfer, instrumental outcome devaluation, and outcome-specific reinstatement. The pattern was clean: anterior mOFC lesions disrupted outcome-specific behaviour on all three; posterior mOFC lesions were largely spared.

## Findings relevant to SD-033b

SD-033b framing (i) -- specific-outcome prediction, the Rudebeck/Murray oracle function -- is the substrate's role in answering "given this state and this candidate action, what particular outcome do I expect?" Bradfield 2018 is direct behavioural evidence that this function is real, localisable, and dissociable: rats with anterior mOFC lesions cannot infer the specific outcomes their actions will produce when those outcomes are not observable in the current environment. They retain general goal-directed motivation but lose the outcome-specific structure that lets them weight options against expected particular consequences.

This complements Wilson/Niv 2014 (theoretical framing) and Schuck 2016 (human fMRI cognitive-map decoding) by adding mechanistic causality: it is not just that OFC encodes structured outcome representations, but that lesioning the relevant OFC subregion produces the predicted behavioural deficit. For an architectural substrate claim like SD-033b, this is the right kind of evidence -- functional necessity of the substrate, demonstrated by selective ablation, with the deficit pattern matching what the architecture requires.

The retrograde tracing component also matters. Anterior mOFC's denser projection to nucleus accumbens core is consistent with the substrate sending outcome predictions into action-selection circuitry, which is broadly the right shape for an OFC-analog feeding E2-style specific-outcome predictions to downstream modules. It is suggestive rather than decisive about the directionality and computational role of those projections, but the anatomical pattern lines up with the functional hypothesis.

## Mapping to REE -- caveats

The biggest caveat is well-known in the OFC literature and applies here: rat mOFC does not cleanly map onto primate or human OFC. The functional homology has been argued both ways for decades, and rat mOFC is sometimes more vmPFC-like functionally. So this paper supports SD-033b's framing (i) by showing that the specific-outcome-prediction function is real and lesion-dissociable in rat, but it does not directly speak to the OFC-vs-vmPFC dissociation that SD-033b vs SD-033c rests on -- the dissociation here is within mOFC (anterior vs posterior), not between OFC and adjacent vmPFC.

Second-order: the paper is about goal-directed action with reward outcomes; SD-033b's natural use case in REE is harm-predictive rollouts. The functional analogy is good (predicting specific outcomes of candidate actions under partial observability) but the valence dimension is different. REE should not assume that an anterior-mOFC-like substrate handles harm prediction by the same computational route as appetitive outcome prediction without further evidence.

## Limitations

Rat lesion work, ~8-12 animals per group, well-validated behavioural paradigms but inevitably species-specific. The anteroposterior dissociation is robust within this paper but the deeper question of how the anatomical gradient maps to functional architecture remains open. The paper does not directly compare OFC to vmPFC, which is the dissociation SD-033b vs SD-033c most needs. None of these undercut the central claim that a specific-outcome-prediction function exists and is substrate-localisable; they bound the strength of the inference about which exact substrate hosts that function in REE's terms.

## Confidence reasoning

Confidence 0.78. Source quality solid (Balleine lab, careful lesion methodology, multi-paradigm behaviour, anatomical confirmation). Mapping fidelity reasonable: the lesion-induced deficit is exactly the deficit SD-033b framing (i) predicts. Transfer risk moderate-to-high: rat mOFC vs primate OFC alignment is the well-known problem, and this paper is rat-specific. The 0.78 reflects strong methodology and good functional mapping pulled down by genuine cross-species transfer concerns. Together with Wilson 2014 (theory), Schuck 2016 (human fMRI), and the Rudebeck/Murray 2014 review already in this directory, the SD-033b framing (i) substrate function has converging evidence across theoretical, human-imaging, and rodent-lesion sources -- with the strongest single piece being Rudebeck/Murray's primate selective-lesion review.
