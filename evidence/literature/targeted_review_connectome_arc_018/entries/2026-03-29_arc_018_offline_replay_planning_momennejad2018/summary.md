# Momennejad, Otto, Daw & Norman (2018) — Offline replay supports planning in human reinforcement learning

**Source:** eLife, 7:e32548. DOI: [10.7554/eLife.32548](https://doi.org/10.7554/eLife.32548)
**PubMed:** PMID 30547886

## What the paper did

Momennejad et al. used fMRI and a two-step sequential decision task to ask whether offline hippocampal replay causally supports human replanning. The paradigm included a reward revaluation phase: after learning the original task, reward values were changed, requiring participants to integrate new information with past knowledge to make optimal decisions. The authors measured multi-voxel pattern (MVPA) evidence for task-state reactivation during off-task rest periods between phases. They also examined whether uncertainty (unsigned prediction error) predicted subsequent replay and replanning.

## Key findings

Three converging results supported the replay-replanning link. First, MVPA evidence for off-task replay during rest predicted subsequent replanning accuracy -- participants who showed more hippocampal reactivation of task states replanned more effectively. Second, neural sensitivity to unsigned prediction error (uncertainty) predicted both subsequent replay probability and replanning success. Third, off-task hippocampus and anterior cingulate cortex showed elevated activity specifically when reward revaluation was required. Together, these results support a Dyna-like architecture in which offline hippocampal replay propagates updated value information backward through the task structure to enable flexible replanning.

## REE translation -- ARC-018

This paper contributes to ARC-018 on two dimensions that the rodent spatial studies do not address. First, the task is abstract -- a two-step sequential decision rather than spatial navigation. This means the hippocampal representations being reactivated are action-sequence states, not place fields. This is directly relevant to ARC-018's V3 framing: if hippocampal replay supports replanning in abstract sequential tasks in humans, the E2 action-object coordinate hypothesis is at least plausible. The viability map need not be limited to spatial coordinates; it may generalise to any action-outcome structure the hippocampus encodes.

Second, the uncertainty-triggers-replay finding is a strong analog to E3 harm/goal error-driven map updating. In REE terms, prediction error (harm/goal discrepancy) is the signal that should trigger viability map updates. Momennejad et al. show that exactly this kind of error signal (unsigned PE, capturing surprise) triggers the hippocampal replay that enables value propagation. The mechanism is imprecise -- unsigned PE conflates positive surprise with negative surprise -- but the directional evidence is supportive.

The anterior cingulate cortex involvement is also worth noting: ACC is a candidate substrate for the E3 harm/goal evaluation function in REE, and its co-activation with hippocampus during revaluation epochs is consistent with an E3-hippocampus signalling pathway.

Where the corrected V3 framing finds support: the abstract sequential task structure is the strongest cross-species evidence that hippocampal viability mapping is not purely spatial. Where it is agnostic: fMRI cannot resolve sequential replay events (temporal resolution too low) -- the MVPA evidence is consistent with replay but does not prove it in the same sense as rodent electrophysiology. The harm/aversive component is again absent from the task.

## Limitations and caveats

fMRI has poor temporal resolution for resolving individual replay sequences. The MVPA measure of replay is correlational -- it captures state reactivation but cannot establish the causal chain from replay to value update to replanning directly. The task uses reward revaluation but not harm signals; whether aversive prediction errors trigger the same hippocampal replay mechanism is unknown. The unsigned PE measure does not distinguish harm from benefit.

## Confidence reasoning

The human data with abstract sequential decisions are a genuine strength -- they extend the viability-map mechanism beyond spatial navigation and towards the action-object level ARC-018 requires. The fMRI limitations prevent a direct mapping to place-cell-level replay mechanisms. Confidence is held at 0.72 to reflect the indirect replay measure and absence of harm-valenced outcomes.
