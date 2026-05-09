# Pfeiffer and Foster 2013 — Hippocampal place-cell sequences depict future paths to remembered goals

**Source:** Pfeiffer BE, Foster DJ. *Nature* 497(7447):74-9 (2013). [DOI: 10.1038/nature12112](https://doi.org/10.1038/nature12112). PMID: 23594744. PMC: PMC3990408.

## What the paper did

Pfeiffer and Foster recorded large ensembles of CA1 place cells (149-273 cells simultaneously per session) from male Long-Evans rats foraging in a 2x2 m open arena with two reward sites. The task structure required the rat to alternate between a daily-novel home well and a randomly chosen reward well; on each trial, the home well changed location, so the rat was repeatedly faced with the problem of constructing a goal-directed route through a familiar arena. The authors decoded the rat's hippocampal representation of position from millisecond-scale place-cell activity and asked: at the moment the rat is about to start a goal-directed run, what does the hippocampus represent?

The answer was a brief, coherent forward-sweep sequence — 40-200 ms long — encoding a spatial trajectory from the rat's current location to the remembered goal. Crucially, these sequences appeared *before* the rat moved; they predicted the upcoming path, not the path just taken. They occurred even when the specific start-goal combination was novel (the rat had never made *this* trip before, but had to assemble it from familiar pieces). And they happened at moments when memory retrieval was needed, not as a constant background.

## Key findings relevant to MECH-307 Gap 4

MECH-307 Gap 4 says: MECH-216 schema readout should write VALENCE_WANTING (and partial anticipatory VALENCE_LIKING and a z_beta arousal pulse) to E1's *predicted* future z_world, not to the agent's current z_world. The architectural commitment is that the conjunction-state — the affective signature of "good thing imminent at that location over there" — must be deposited in the right spatial slot of the residue field, namely the slot that corresponds to where the agent is about to be.

Pfeiffer and Foster supply the canonical biological precedent for this commitment. The rat hippocampus does not just represent where the animal is; at the moment goal retrieval matters, it constructs a representation of where the animal is going to be. That forward representation is what downstream targets (in the rat: navigational motor systems; in REE: the residue field's valence buffer at z_world_predicted) need in order to do anything goal-directed at all. Without it, the only addressable slot would be the current location, and the affective annotation would land on stale geometry.

## How the findings translate to REE

The translation is architectural rather than mechanistic. REE's z_world is a learned latent state, not a metric place code; E1's forward rollout produces a predicted z_world at horizon h=1 (or further), not a place-cell sequence. But the functional role is the same: write at the projected target, not at the current state. Once that primitive is in place, MECH-205 (surprise-gated sleep-replay write path) and MECH-292 (ghost-goal priority bank) can consume the conjunction-state at the right z_world locations, and the Adcock 2006 prediction (anticipation-marked locations get >=1.5x replay priority) becomes testable.

A subtle point: Pfeiffer-Foster sweeps construct a *trajectory* (a sequence of intermediate places connecting current to goal), whereas MECH-307 Gap 4 only requires a single write at the predicted target. REE could in principle implement the simpler version — single-target write — and capture the Adcock-replay tie-in without the full trajectory shape. Whether the trajectory-shaped version is needed for MECH-292 ghost-goal bank ranking is an open architectural question and probably worth deferring until the simpler write-at-target version produces measurable behaviour in EXQ-540's successor.

## Limitations and caveats

The paradigm is spatial navigation in well-trained rats. The forward-sweep mechanism is only known to fire reliably when the rat already knows the goal location and is committed to retrieving it. MECH-307's analog will need to handle the case where E1's forward prediction is uncertain (early learning, novel z_world neighbourhoods). Writing the conjunction-state at a low-confidence predicted location would scatter wanting/liking annotations across noise, which would degrade rather than enhance MECH-205 replay-priority signal. The straightforward fix is to gate the write on prediction certainty — but that gate is not in the current MECH-307 substrate, so it needs to be added when Gap 4 is implemented past the consumer-side proof-of-concept (V3-EXQ-540 currently exercises a Gap-1+Gap-2+Gap-3 ARM_2; Gap 4 is the remaining un-touched piece).

A second caveat: hippocampal place-cell forward sweeps are themselves a small literature with active debates about whether they are "preplay" (constructed prior to experience) or "replay" of generalised templates. Pfeiffer and Foster argue strongly for the constructive reading — sequences appear for novel start-goal combinations — but the broader question of how much of the trajectory is built from learned components vs. assembled de novo is not fully settled.

## Confidence reasoning

I assign confidence 0.86 — strong but not maximal. Source quality is very high (Nature, foundational, well-cited, replicated in independent labs). Mapping fidelity to MECH-307 Gap 4 is direct in architectural form (forward-projection at recall is exactly what Gap 4 asks for) but loose in detail (the rat constructs a full trajectory; MECH-307 needs only a single-target write). Transfer risk is moderate because the substrates are conceptually adjacent — both build a representation of where the agent is going — but mechanistically distinct (place code vs learned latent). The paper does not falsify any other plausible reading of MECH-307; its role is to establish that "write at predicted location, not current location" is a real architectural primitive in biology, not a REE-specific stipulation.

This is the load-bearing entry for Gap 4 of MECH-307. Together with Johnson and Redish 2007 (forward sweeps at decision points specifically), it grounds the predicted-location-write commitment in two independent paradigms within the same lab tradition.
