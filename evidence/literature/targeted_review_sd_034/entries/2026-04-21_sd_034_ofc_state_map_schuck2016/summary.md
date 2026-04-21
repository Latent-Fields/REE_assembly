# Schuck et al. 2016 -- OFC as cognitive map of state space

## Source
Schuck NW, Cai MB, Wilson RC, Niv Y. Human Orbitofrontal Cortex Represents a Cognitive Map of State Space. Neuron 91(6):1402-1412. DOI: 10.1016/j.neuron.2016.08.019

## Finding
Medial OFC encodes task-relevant state in a multidimensional representation that includes features which are not directly observable but are necessary to determine the correct response. MVPA decoding shows state identity can be read out from OFC voxel patterns; the representation scales with the number of task-relevant dimensions.

## Why it maps to SD-034
SD-034 proposes a closure operator: a detector that fires when a committed rule_state has been satisfied, releasing commitment and imposing a temporary No-Go on re-entry to the just-completed rule. Any such detector needs as its input a representation of task state that goes beyond sensory immediacy -- it has to know where the agent is in the task graph. Schuck et al. demonstrate this prerequisite representation exists in OFC in humans.

The paper is substrate-level evidence: it shows the representation exists; it does not show the specific readout that SD-034 posits. That further step (a completion-state detector that emits a closure token) remains a mechanistic posit.

## Confidence: 0.72 (supports)
- source_quality 0.85 (Neuron, strong MVPA methodology, well-designed task)
- mapping_fidelity 0.65 (substrate present; specific closure-readout not demonstrated)
- transfer_risk 0.35 (OFC in biology has many readout targets; SD-034's posited closure-detector is one of several candidate downstream reads)

## Key limitations
- The task is deterministic and over-trained. If OFC state maps only crystallise under heavy training, the representation may not be available during early rule learning, when SD-034's closure operator would also need to function.
- Decoding is from whole-OFC voxel patterns. A sparse, specialised state-transition-tuned population, if it exists, is not identified here.
- The paper does not test whether OFC state representations predict behaviour on completion transitions specifically; it tests decoding across states generally.

## Failure signatures
- If closure detection turns out to be implemented via a graded continuous signal rather than a discrete token, SD-034's token framing may be too discrete.
- If the relevant readout is a sparse specialised population rather than a distributed OFC pattern, the substrate story here is at the wrong level.
- If OFC state maps require extensive training, SD-034 needs a separate early-learning closure mechanism.
