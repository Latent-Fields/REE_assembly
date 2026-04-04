# Summary: High-Level Prediction Signals in a Low-Level Area — Schwiedrzik & Freiwald (2017)

**Claim tested:** ARC-022 (Hierarchical effect-object abstraction pipeline)
**Evidence direction:** supports
**Confidence:** 0.70

Here is a more uncomfortable question for ARC-022 than the computational papers raise: if higher areas send typed prediction signals to lower areas, and if those signals carry the abstraction properties of the higher level rather than the lower level, then what is actually flowing between layers? Schwiedrzik and Freiwald give an empirical answer in the macaque face-processing hierarchy. After training monkeys on face sequences, they recorded from the low-level face area ML and found prediction error signals that carried identity specificity and view invariance -- properties of the higher-level face area AL, not ML's own tuning. The lower area was comparing incoming input against predictions that had been typed at the higher level.

This is the physiological correlate of ARC-022's typed-object abstraction principle. In REE terms, when E1 computes a prediction error, it is not comparing raw sensory signal against a raw sensory prediction; it is comparing against a prediction that has been typed and abstracted by E2's transition model. The error signal is already typed. The Schwiedrzik and Freiwald finding makes this concrete: you can see it in single-unit responses in a well-characterised biological hierarchy. Lower areas test predictions at abstraction levels that exceed their own typical processing level, which is exactly what ARC-022 predicts about E1 receiving E2-abstracted prediction objects.

The view-invariance property is particularly relevant. ARC-022 claims E2 produces temporally structured self-in-world trajectory predictions (z_gamma transitions), not raw sensory predictions. View invariance is the visual-domain analogue of motion-invariance or context-invariance: the prediction survives transformation, which means it is a higher-order typed object, not a point in sensory space. This directly supports the claim that the output type at each level has properties that the level below cannot generate from its own computations alone.

The main limitation is domain specificity. The face-processing cascade (ML -> AL -> anterior face patches) is a highly specialised visual recognition hierarchy in a primate with unusually dense face-processing infrastructure. The inference to the E1->E2 junction in an action/planning hierarchy requires treating this specialised result as a general principle of cortical hierarchy. This is not unreasonable -- predictive coding theorists do exactly this -- but it is inference by analogy. The study cannot directly address the DMN->Goal/Avoid->Hippocampus stages that sit above E2 in ARC-022's pipeline.

---
*Source:* Schwiedrzik CM, Freiwald WA (2017). High-Level Prediction Signals in a Low-Level Area of the Macaque Face-Processing Hierarchy. *Neuron* 96(1):89-97.e4. doi:10.1016/j.neuron.2017.09.007
