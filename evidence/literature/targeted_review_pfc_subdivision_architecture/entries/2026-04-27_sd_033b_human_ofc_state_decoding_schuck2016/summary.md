# Schuck, Cai, Wilson & Niv 2016 -- Human OFC represents a cognitive map of state space

## What the paper does

This is the direct human-fMRI test of the Wilson/Niv 2014 OFC-as-cognitive-map hypothesis. Subjects performed a structured decision-making task with 16 task states arranged so that several state distinctions could only be made by integrating prior context with current observations -- the states were unobservable from immediate sensory input. The authors applied multivariate pattern classification (MVPA) to BOLD signal in medial OFC and asked: can we decode the current task state from the OFC activity pattern, even when sensory input alone underdetermines the state?

The headline result: yes. State decoding from OFC was reliable, including for the unobservable distinctions, and decoding accuracy correlated with behavioural performance -- subjects whose OFC patterns more cleanly distinguished states made fewer errors. They went further: similarity between OFC patterns for consecutive states correlated with the agent's behavioural accuracy on the corresponding state transition. This last result is the methodological strongest move, because it ties the geometric structure of the OFC representation to the structure of the agent's behavioural map of the task.

## Findings relevant to SD-033b

SD-033b's functional restatement requires the OFC-analog to hold a structured representation of "what states the agent can be in, what transitions are possible, and what outcome structure each state predicts." Schuck 2016 is the cleanest single-experiment confirmation of that claim in humans. The decoded entity is exactly what SD-033b calls the task-structure cognitive map: a labelling of the current state that is computed from sensory input plus stored context, and that downstream prediction machinery can read.

The behavioural correlation matters more than the decoding alone. A pure decodability finding could be explained by OFC reflecting downstream computation -- a readout of what some other region computed. The performance correlation goes the other way: better OFC representation predicts better behaviour, which is the right shape of evidence for OFC being the substrate the behaviour depends on rather than a downstream artefact. This is the operational link that SD-033b needs.

## Mapping to REE -- caveats

The mapping is unusually clean for an fMRI paper. SD-033b says the OFC-analog holds a task-structure representation; Schuck 2016 demonstrates exactly that in human OFC, with the right behavioural correlates. ree-v3's E2 reads from this substrate to do specific-outcome rollouts; in Schuck's paradigm the analog operation is using the decoded state to look up the correct prediction for the next observation. The structural correspondence is direct.

What the mapping does not establish: whether human OFC represents continuous state spaces or open-ended task structures the same way. The 16-state task is discrete, structured, and well-defined; agents in ree-v3 face latent spaces with much richer dynamics. So Schuck 2016 confirms the substrate exists and behaves as predicted in a structured paradigm, but the question of how naturally this generalises to less constrained settings is empirically open. I would not over-extend the mapping to claim that human OFC implements the same continuous-latent rollout machinery REE postulates -- only that the structured-state-labelling function it performs is the right one.

## Limitations

fMRI MVPA infers representational content from BOLD pattern similarity, not from direct neural code -- the substrate could be implementing the function via mechanisms quite different from REE's E2 architecture. The behavioural correlation strengthens the inference but does not eliminate it. Sample size (~30s) is reasonable for fMRI but not large. The task is structured-discrete; richer state spaces are not directly tested. None of these are fatal to the central claim, but they bound the inference.

## Confidence reasoning

Confidence 0.84. Source quality high (Neuron, methodologically careful, multiple confirmation analyses). Mapping fidelity strong because the decoded entity is what SD-033b describes as framing (ii). Transfer risk low -- this is human data on a cognitively rich task, the direction REE most needs to anchor its architectural claims. The 0.84 rather than 0.90 reflects the inferential gap between MVPA decodability and direct neural code, plus the open question of generalisation beyond structured discrete tasks. Together with Wilson 2014 (theory) and the Zhou/Stalnaker rodent entries (single-unit confirmation), this paper completes a strong cross-species evidence triangle for SD-033b framing (ii).
