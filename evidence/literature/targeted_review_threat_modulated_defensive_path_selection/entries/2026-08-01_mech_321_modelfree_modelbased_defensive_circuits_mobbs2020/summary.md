# Mobbs, Headley, Ding & Dayan 2020 -- Space, Time, and Fear: Survival Computations along Defensive Circuits

**Source**: Mobbs D, Headley DB, Ding W, Dayan P (2020). *Trends in Cognitive Sciences* 24(3):228-241. [DOI 10.1016/j.tics.2019.12.016](https://doi.org/10.1016/j.tics.2019.12.016). PMID 32029360.

## What the paper did

This is a theoretical/computational review recasting the threat-imminence literature (Fanselow's PIC, Mobbs' own 2007 fMRI work, and the broader defensive-circuit neuroscience) explicitly in the model-free (MF) versus model-based (MB) reinforcement-learning vocabulary, co-authored by Peter Dayan, one of the originators of that computational distinction. It asks how decisions to avoid or escape threats at different spatiotemporal scales map onto different classes of computation and different neural circuits.

## Key findings relevant to the claim

The paper's central claim: at the extreme of proximal (spatially/temporally close) threat, defense is handled by a limited repertoire of fast, reflexive, myopic actions — reflecting a REDUCED decision and state space and a model-free computational architecture (cached, habitual, cheap). At the extreme of distal threat, more information processing is possible and is handled by model-based operations — affective prospection, mental replay, and planning against a fuller world model. The two modes are not strictly separate; under conditions of safety, model-based computation can lay down the foundations for effective future model-free reaction (planning now so reacting can be fast and cheap later). All of this is proposed to be realized by distinct, distributed population codes across the defensive circuit, whose overall function is to determine and execute the best policy.

## How this translates to REE

Of everything gathered in this pull, this is the highest-fidelity mapping onto REE's own architecture, because it is written in essentially the same computational vocabulary REE already uses. REE's hippocampal policy-decomposition/redecomposition step is itself a model-based operation — it re-plans using a world model when a committed (cached, model-free-like) macro-action becomes unreliable, which is precisely MECH-321's own trigger condition. This paper's central proposal gives SD-hazard-aware-policy-decomposition a concrete, REE-native functional-form candidate that goes beyond a simple reweighting: as `z_harm_a`/imminence rises, the redecomposition step should not just reweight scores across an unchanged candidate set, it should PRUNE the candidate re-tiling set — narrowing toward a small, fast, low-deliberation choice near the high-harm end (mirroring MF-like reflexive narrowing), while permitting fuller, more exploratory scoring among many candidates when harm is low (mirroring MB-like deliberation). This operationalizes Mobbs 2007's categorical-shift finding (elsewhere in this pull) in concrete computational terms: the "regime change" is a change in effective SEARCH-SPACE SIZE, not merely a change in which score wins.

## Limitations and caveats

This is a theoretical review proposing an interpretive framework, not new empirical measurements — its force depends on how well the underlying primary literature (Mobbs 2007, the Fanselow PIC papers, and others cited elsewhere in this pull) actually supports the MF/MB dissociation, and other reasonable computational framings of the same data exist. Worth flagging honestly: because the MF/MB vocabulary was built for exactly the kind of system REE is (Dayan is a co-originator of that RL distinction), part of why this paper "fits" REE so well is that the terms were designed to describe systems like it, not that biology has been independently shown to literally implement MF/MB RL. That does not make the mapping wrong, but it means the apparent fit should not be read as stronger evidence than it is.

## Confidence reasoning

High mapping fidelity (0.88) given the shared computational vocabulary, tempered confidence overall (0.83) because it is a synthesis rather than primary data and because some of its apparent REE-relevance is an artifact of the authors' own framework choice rather than independent biological confirmation — both points made explicit in the mapping_caveat above.
