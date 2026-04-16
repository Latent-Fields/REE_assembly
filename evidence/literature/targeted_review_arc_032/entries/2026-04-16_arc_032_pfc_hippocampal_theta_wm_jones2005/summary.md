# Jones & Wilson 2005 — Theta Rhythms Coordinate Hippocampal-Prefrontal Interactions

**PLoS Biology | doi: 10.1371/journal.pbio.0030402 | PMID: 16279838**

## What the paper did

Jones and Wilson implanted tetrode arrays targeting hippocampal CA1 and medial prefrontal cortex simultaneously in freely behaving rats performing a continuous spatial alternation task — an operant T-maze that requires the animal to remember its previous choice in order to select the correct next arm. Crucially, the task design allowed them to distinguish epochs that genuinely required working memory (choice epochs, where the animal must recall the last visited arm) from epochs that required similar locomotion but no memory retrieval (forced-turn epochs, where only one arm was open). They measured LFP theta coherence between the two structures and phase-locking of prefrontal unit firing to hippocampal theta across these conditions.

## Key findings relevant to ARC-032

The clearest finding is selectivity: theta-band LFP coherence between CA1 and mPFC was significantly elevated during working-memory-demanding choice epochs (mean coherence ~0.32) compared to non-memory forced-turn epochs (~0.19). Prefrontal neurons showed stronger phase-locking to hippocampal theta during correct choice trials than during error trials. This means that theta coupling between the structures correlates not with movement per se, but with the cognitive demand to retrieve and use goal context for decision-making. The coordination was also predictive: on error trials, the theta coupling was reduced, suggesting that the synchrony failures accompany, and perhaps cause, navigation errors.

## Translation to REE

ARC-032 proposes that the theta-rate ThetaBuffer (MECH-089) is the primary pathway through which E1's goal-context maintenance reaches E3's trajectory scoring. The Jones & Wilson finding maps onto this architecture in two ways. First, the task selectivity (theta coupling tracks goal-context demand) supports the claim that the theta channel is a goal-communication pathway rather than a general locomotion-coupled oscillation. If theta coherence were up during any locomotion, it would be uninformative about goal encoding specifically; the demand-specificity is what makes it architecturally meaningful. Second, the error-trial attenuation finding supports a causal framing: when theta synchrony is degraded, goal-directed navigation fails -- directly consistent with ARC-032's claim that the theta pathway is necessary for E3's trajectory scoring to receive E1's goal context.

## Limitations and caveats

The coherence measure is symmetric -- it cannot distinguish whether mPFC is sending goal context to hippocampus, or hippocampus is sending spatial state to mPFC, or both. The causal direction of information flow remains an inference. The rat prelimbic/infralimbic mPFC is also a less direct analog of primate DLPFC or the E1 LSTM than one would like: rat mPFC working memory content in this task (the previous spatial choice) is narrower and more retrospective than the E1 goal-context described in REE (a maintained goal identity across many steps guiding prospective trajectory selection). Transfer from a binary alternation task to a multi-step goal navigation architecture requires some interpretive latitude.

## Confidence reasoning

Confidence 0.82. This is a well-designed study with a clean behavioural dissociation, simultaneous recordings from both structures, and a finding (task-selective theta coupling) that maps directly onto ARC-032's core prediction. The main deductions are for the symmetric coherence measure (direction of information flow unknown) and the rat-to-REE species and task transfer. Among the three Hyman/Benchenane/Colgin entries already in this directory, Jones & Wilson add the crucial task-selectivity angle: their dissociation between WM and non-WM epochs makes the goal-specificity argument rather than merely documenting oscillatory coupling during navigation.
