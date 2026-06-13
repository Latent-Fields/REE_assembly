# Pure vs contextual time cells (Omer, Las & Ulanovsky 2022) — MECH-148

**Claim:** MECH-148 — hippocampal pure time cells provide a temporal scaffold for E3 credit assignment: a context-independent elapsed-time encoding must be present so trajectory outcomes are weighted by temporal distance, not evaluated step-locally.

## What the paper did

Omer, Las, and Ulanovsky recorded single units in hippocampal area CA1 of freely-behaving fruit bats. Time cells — neurons that fire at circumscribed moments within a delay — were already known, but it was unresolved whether they encode *context-dependent experience* or *time per se*. By recording while a bat hung at different locations, the authors could separate the two. They found two distinct populations. **Contextual time cells** generated different temporal sequences at different locations — time conjoined with place. **Pure time cells** showed similar preferred times across spatial contexts — they encoded elapsed time independent of where the animal was. A third population fired in register with *another* bat's landing moment during a social imitation task, encoding time relative to a conspecific's action.

## Why it matters for REE

This is almost a verbatim grounding of MECH-148. The claim's load-bearing construct is a "context-independent elapsed-time encoding," and the pure-time population is exactly that — a temporal tag that is not bound to the spatial/contextual content of the rollout. That is what lets E3 discount a harm at rollout step 15 differently from one at step 3 along otherwise-identical z_world paths, instead of being myopic to temporal distance. The dissociation from contextual time cells is the important part: it shows the brain *does* maintain a content-free time axis as a separable signal, which is precisely the design MECH-148 reserves.

The social time-cell population is an unexpected bonus that the HPL-9 node explicitly flags as a forward bridge. Cells coding time relative to another agent's action are the biological analogue of MECH-127's multi-agent temporal credit — the V5 social tier's requirement to attribute outcomes to another agent's events over time. So this single paper grounds both the V4 mechanism (pure elapsed-time scaffold) and the V5 extension (other-aligned time coding), which is exactly the kind of "same-system" completeness the assembly sweep is meant to catch.

## Caveats and confidence

The limit is the usual representation-versus-use gap. The paper establishes that pure elapsed-time cells exist and are dissociable; it does not show that feeding such a tag into a planner improves long-horizon credit assignment — that is REE's forward inference. The substrate is bat CA1 during hanging and landing, not a multi-step deliberative rollout. With those caveats, the mapping fidelity is unusually high (the construct matches the data almost one-to-one) and the source is a Nature Neuroscience primary single-unit study. Confidence 0.83 (supports).

*According to PubMed.* Source: Omer DB, Las L, Ulanovsky N (2022), *Nature Neuroscience* 26(2):285–294. [DOI](https://doi.org/10.1038/s41593-022-01226-y)
