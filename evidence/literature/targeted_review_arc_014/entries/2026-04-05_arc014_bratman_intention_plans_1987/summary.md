# Bratman 1987 -- Intention, Plans, and Practical Reason: ARC-014 Mapping

**Source:** Bratman, M.E. (1987). *Intention, Plans, and Practical Reason*. Harvard University Press. Available via: [PhilPapers](https://philpapers.org/rec/BRAIPA)

---

## What the Book Does

Bratman's monograph develops the planning theory of intention, arguing that intentions cannot be reduced to combinations of belief and desire but are a distinct, third category of mental state. The central claim is that future-directed intentions function as elements of partial plans: they commit the agent to a course of action and serve as inputs to further practical reasoning, guiding what means to seek and what side-effects to accept.

The core functional characterisation of intentions is as 'conduct-controlling pro-attitudes': unlike desires, which remain as motivational forces subject to constant comparison with alternatives, intentions are adopted and then treated as settled -- not subject to continuous reconsideration unless there is positive reason to reconsider. This stability function is what makes planning possible: without it, every practical question would revert to first principles and the computational benefits of planning over time would be lost.

The book includes a chapter explicitly titled "Commitment Revisited" that addresses the tension between commitment stability (necessary for planning) and rational revisability (necessary for responsiveness to new information). Bratman's solution is that intentions should not be reconsidered unless there is positive reason to do so -- but the bar for reconsideration is non-zero precisely because that is what makes them commitments rather than tentative preferences.

## Key Arguments Relevant to ARC-014

**1. Prior intentions as planning anchors**: Bratman distinguishes 'prior intentions' (formed in advance of action) from 'intentions in action' (concurrent with execution). Prior intentions function as anchors for multi-step plans: they fix a future-directed commitment that constrains what the agent will deliberate about subsequently. Once a prior intention is formed, subsequent deliberation is about means and schedules, not about whether to pursue the goal. This is the planning theory's account of why committed actions are not simply re-evaluated as options.

**2. Categorical commitment, not graded preference**: Bratman argues that the commitment function of intentions is categorical: the intention either holds or is reconsidered/retracted, but while it holds, it is not simply a very strong preference being outweighed moment to moment. This supports ARC-014's claim that the pre/post-commit boundary is categorical (a route switch) rather than a precision parameter. Graded attenuation of commitment is not a commitment -- it is a preference distribution.

**3. Non-reconsideration as a rational norm**: for Bratman, the rational norm is to not reconsider intentions absent positive reason, because the alternative -- continuous reconsideration -- destroys the value of planning. This is the planning-coherence argument: an agent who re-evaluated every prior intention at every step would derive no computational benefit from having formed the intention. The pre/post-commit boundary in REE instantiates this: once committed, an action is no longer a simulation option, and its consequences must be attributed in a distinct (post-commit) mode.

## REE Mapping to ARC-014

ARC-014's commitment architecture instantiates Bratman's planning theory at the level of neural/computational implementation. The pre-commit channel in REE corresponds to Bratman's deliberative phase: trajectories are hypothetical, evaluation is ongoing, and the agent may update without consequence. The post-commit channel corresponds to Bratman's committed-action phase: the action is executing, re-evaluation is not applicable, and consequences must be attributed in a distinct mode (offline, via phi(z) update).

The categorical character of ARC-014's boundary -- not a precision parameter but a route switch -- is directly supported by Bratman's argument that commitments are categorically distinct from preferences. The hypothesis tag (MECH-094) that gates phi(z) writes in REE implements exactly Bratman's commitment/deliberation distinction: during pre-commit simulation, trajectories are tagged as hypothetical (intention not yet formed); once committed, the tag is removed and the post-commit attribution channel becomes active.

The architectural necessity claim in ARC-014 ("committed actions cannot be unsimulated; their consequences must be attributed offline") corresponds to Bratman's claim that a system without commitment stability loses the computational benefits of planning. REE extends this from rational norms to architectural implementation: for a system that modifies phi(z) (ethical residue) based on experience, maintaining the pre/post-commit boundary is not just rational but necessary to prevent simulation from contaminating the residue field.

## Limitations and Confidence Reasoning

Bratman's framework is normative philosophy of action -- it specifies what rational agents should do, not how neural architectures must be structured. The move from "it is rational to treat committed actions as non-revisable options" to "there must be an architectural boundary with distinct channels and phi(z) write access" requires an additional design argument that Bratman does not provide. The pre-commit/post-commit channel separation is an REE engineering inference from Bratman's philosophical framework. Confidence: 0.74.

*Based on Harvard University Press monograph (1987); also available via Stanford University CSLI Publications reprint (1999).*
