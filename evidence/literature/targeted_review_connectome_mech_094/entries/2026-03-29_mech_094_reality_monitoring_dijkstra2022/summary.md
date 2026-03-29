# Dijkstra, Kok & Fleming (2022) -- Perceptual Reality Monitoring: Neural Mechanisms Dissociating Imagination from Reality

## What the paper did

Dijkstra and colleagues at UCL's Wellcome Centre for Human Neuroimaging wrote a comprehensive review synthesising research on how the brain distinguishes internally generated imagination from externally triggered perception. The review draws on cognitive neuroscience, clinical psychiatry, and computational modelling. It asks a deceptively simple question: given that imagination and perception use overlapping neural machinery, how does the brain know which is which? The answer turns out to be non-trivial and has significant implications for understanding hallucinations, PTSD, and other disorders of reality monitoring.

## Key findings relevant to MECH-094

Three findings from this review bear directly on MECH-094.

First: no single low-level signal unambiguously marks an experience as internally versus externally generated. Imagination tends to produce weaker, less precise sensory representations than perception, but these differences are graded, not categorical. The brain cannot simply look at signal amplitude or precision and read off "imagined" vs "real."

Second: reality monitoring is implemented by higher-level cortical circuits -- primarily prefrontal -- that evaluate a collection of first-order sensory and cognitive factors to make an inference about source. The review frames this as sharing core computations with metacognition: reality monitoring is the brain's judgment about the origin of its own content. The anterior prefrontal cortex is identified as a key implementation site.

Third: when this monitoring mechanism fails, the result is source confusion at various levels of severity. Mild failures produce everyday experiences like uncertainty about whether one did something (e.g., locked the door). More severe failures include hallucinations (internally generated content experienced as externally real) and the PTSD flashback (a memory experienced as a current percept). The review explicitly links the PTSD flashback to failure of the reality monitoring mechanism rather than to excessive vividness of the memory.

## Translation to MECH-094

MECH-094 proposes that the hypothesis tag is a categorical write gate that separates simulation/DMN signals from committed-outcome signals. During simulation, only the pre-commit error channel is active; the post-commit channel -- which drives residue accumulation -- is suppressed. This is an architectural implementation of reality monitoring at the mechanism level: the hypothesis tag is the gate that the prefrontal reality-monitoring circuit implements.

The parallel between the biological and computational architectures is close. In the biology: prefrontal circuits evaluate first-order sensory factors to determine whether a signal is internal or external, then route downstream processing accordingly. In REE: E3 maintains the hypothesis tag as part of its commitment-state representation, and the tag routes simulation signals away from the residue write pathway. The key difference is that MECH-094's tag is categorical (in/out of simulation mode) while the biological mechanism is more graded. But the functional purpose -- preventing internally generated content from being mistaken for committed outcomes -- is identical.

The review's clinical failure modes map precisely onto MECH-094's predicted failure modes. Hallucinations = internally generated content treated as externally real = tag loss causing simulation to write to the committed channel. PTSD flashback = a memory treated as a current percept = tag loss causing a replayed event to drive residue accumulation as if it were a new committed event. Psychosis = systematic tag-loss across domains. MECH-094 describes this as "the damage in rumination is tag loss, not excessive vividness" -- which is exactly the conclusion Dijkstra et al. reach about hallucinations: the problem is source attribution failure, not signal strength.

## Limitations and caveats

The review identifies a multi-factor graded inference as the biological mechanism; MECH-094 proposes a categorical tag. This is a deliberate architectural simplification in REE rather than a misrepresentation of the biology, but it means MECH-094 cannot reproduce the full range of graded reality-monitoring failures. The review also focusses on perceptual reality monitoring (distinguishing sensory imagery from sensory input), whereas MECH-094's tag operates on a somewhat different axis (distinguishing planning/simulation from committed action). These are functionally related but not identical: a vivid visual image in imagination is different from a planned action in DMN. The overlap is strong enough to make the mapping compelling, but the distinction should be kept in mind when interpreting the clinical failure modes.

## Confidence reasoning

The source is a comprehensive, recent review from one of the best labs working on this topic, published in a high-impact review journal. The mapping to MECH-094 is the most direct of any paper found for this claim: the biological function described (distinguishing internally generated from externally generated signals) is precisely the function MECH-094's tag implements. Transfer risk is low. Overall confidence 0.82.

Based on articles retrieved from PubMed. DOI: https://doi.org/10.1016/j.neubiorev.2022.104557
