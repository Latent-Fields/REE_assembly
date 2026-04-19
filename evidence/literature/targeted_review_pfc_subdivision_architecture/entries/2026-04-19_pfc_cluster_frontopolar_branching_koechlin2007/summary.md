# Koechlin & Summerfield 2007 — An Information-Theoretic Approach to PFC Executive Function

## What the paper does

Koechlin and Summerfield propose a formal information-theoretic framing of lateral PFC function in which progressively more rostral regions handle progressively more abstract forms of control. At the apex sits frontopolar cortex (BA 10), which the authors argue is the substrate for branching and nested cognitive control — the specific capability of holding a pending cognitive operation in abeyance while executing a current one, then returning to the suspended operation. This capability is what lets humans interleave multiple ongoing tasks, handle unexpected interruptions, and reason about parallel policies before committing. The review is built on human fMRI and patient-lesion evidence (Burgess, Shallice, Koechlin lab).

## Key findings relevant to the PFC cluster

Frontopolar function matters specifically for REE's V3-vs-V4 scoping decision. In the operating_mode_vector framework, internal_planning is currently treated as a single mode in which the agent runs counterfactual rollouts and evaluates outcomes. But the Koechlin framing implies that more sophisticated internal_planning — explicit branching between candidate policies, maintaining multiple options in parallel, returning to a suspended line of reasoning after a distraction — sits at a distinct computational level that requires its own substrate.

This lines up cleanly with what I have been treating as V4 capability: the kind of explicit deliberative architecture that supports ethical reasoning under conflict, genuine counterfactual weighing of futures, and the Frankfurt-style "reflective endorsement" of one's own first-order motivations. V3 provides the hooks (MECH-261, operating_mode_vector with internal_planning) but implements only the mid-lateral rule-holding level. V4 adds the frontopolar-analogue substrate for branching.

## How this translates into REE

The scoping recommendation is:

- **V3 implementation of lateral-PFC-analogue:** stop at the mid-lateral level — a substrate that holds the currently active rule/goal, supports rule-selective persistence across delays, and is written into under MECH-261 gating.
- **V4 scope:** add frontopolar-analogue — explicit branching, parallel policy maintenance, return-from-suspension capability. This is where REE's long-horizon ethical reasoning will eventually live.
- **Design-forward note on MECH-261:** the operating_mode_vector should already accommodate a future "deliberative_branching" mode even if V3 doesn't implement it. Getting the mode vocabulary right now saves a disruptive schema change later.

## Limitations and caveats

Frontopolar cortex is the least-well-mapped region in the PFC hierarchy. It is phylogenetically newest, has the sparsest single-unit recording coverage, and its precise functional role is still actively debated (branching vs prospective memory vs meta-cognition vs relational integration are competing accounts, not all mutually exclusive). The Koechlin information-theoretic framing is one influential account but not the only one. REE should treat frontopolar-analogue as a well-motivated V4 design target without over-committing to a specific computational implementation. When V4 design work begins, this should be followed up with a more thorough lit-pull (Burgess, Mansouri, Boorman, perhaps Christoff on meta-cognition).

## Confidence reasoning

Source quality solid (TiCS, Koechlin lab) but not Nature Reviews level. Mapping fidelity moderate — the function matches what V4 needs, but the computational specifics are still contested. Transfer risk higher than other entries because frontopolar is the most humanised / least cross-species substrate. Net confidence: 0.72.
