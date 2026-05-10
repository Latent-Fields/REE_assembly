# Westgate & Wilson 2018 — Boring Thoughts and Bored Minds: The MAC Model

[DOI](https://doi.org/10.1037/rev0000097) · PMID 29963873 · *Psychological Review* 125(5):689-713

## What the paper argues

A Psychological Review theoretical paper proposing the Meaning-and-Attentional-Components (MAC) model of boredom. The model decomposes boredom into two semi-independent components: (a) an **attentional component** — mismatches between cognitive demands and available mental resources, with both under-stimulation (resources exceed demands) and over-stimulation (demands exceed resources) yielding the boredom signature; and (b) a **meaning component** — mismatches between activities and valued goals, including the limit case of absent valued goals altogether. The two components produce *different profiles* of boredom: someone bored from a too-easy task differs from someone bored from a meaningless task, even though both label the experience "boredom" and behave similarly in some respects. MAC is the modern dominant citation for the attentional account and the most-cited contemporary mechanism paper.

## Why this matters for ARC-067

This is a load-bearing R1 paper that complicates the pre-registered ARC-067 single-component shape. The user's registration framing is essentially the attentional-component half of MAC: an engagement-rate accumulator (commit transitions per episode, novel-observation count, E3 deliberation depth, residue-write rate). MAC argues that this captures only one of two semi-independent inputs to the boredom-aversive. The meaning-component half — which fires when the agent has *no z_goal* or when the *current z_goal does not match the task* — is mechanistically different and would not be detected by the engagement-rate proxy alone.

For child-MECH design this means the cleanest implementation is a two-input convergence on the ARC-067 valence accumulator. The attentional channel takes the engagement-rate scalar (this is the primary mechanism per R1). The meaning channel reuses the existing REE z_goal substrate (SD-012 homeostatic drive, MECH-308 ghost-goal arbitration): when z_goal is empty *or* when the current z_goal does not match what the agent is doing, a meaning-misfit signal contributes to the aversive. This is architecturally cheap because the z_goal substrate already exists; it does not require a new estimator.

There is an important boundary against ARC-068 (opportunity cost) here. MAC's meaning component is *teleological* (about goal-task fit), whereas ARC-068's opportunity cost is *value-driven* (about expected reward foregone by passivity). The two are conceptually adjacent but mechanistically distinct: meaning-misfit can fire when the agent is busy but mis-aligned, regardless of opportunity cost; opportunity cost can fire when meaning is fine but a higher-value alternative is available. The R3 verdict on routing channel keeps these on different layers (meaning-misfit feeds the z_harm_a aversive accumulator; opportunity cost stays on the E3 score axis).

## Limitations and confidence

MAC was developed on human task-engagement experiments, primarily laboratory tasks varying boringness and meaning. The cross-domain transfer to embodied open-ended REE foraging is theoretically clean but not directly tested. The two-component decomposition may also be coarser than the underlying mechanism — post-2018 proposals (notably Eastwood-lab reformulations and FEP-flavoured learning-progress accounts) collapse both into a single information-gain failure signal, with the two components being two routes to that failure. Confidence aggregate 0.82 — Psychological Review venue puts source quality near ceiling; mapping fidelity moderately high (the two-component shape forces a compositional reading); transfer risk somewhat elevated because the experimental base is human laboratory tasks.

## Failure signature it would falsify

Two failure signatures fall out of MAC for an ARC-067 substrate. First: a single-component implementation (engagement-rate only) will fail to discriminate over- vs under-stimulation profiles when MAC predicts both should produce boredom but through opposite routes through the cognitive-demand-vs-resources gap. Second: a discriminative test pair should hold for the two-component decomposition — under-stimulation arms (low cognitive demand, low novelty) and meaning-violation arms (high engagement but goal-incongruent task) should both produce boredom-like behaviour with separable internal signatures. An ARC-067 substrate that lacks the meaning channel will fail the meaning-violation arm.
