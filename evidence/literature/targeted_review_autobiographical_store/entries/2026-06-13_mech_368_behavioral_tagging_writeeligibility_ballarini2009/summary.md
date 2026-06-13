# Behavioral tagging as the biology of write-eligibility (MECH-368)

**Ballarini, Moncada, Martinez, Alen & Viola (2009), *PNAS* 106(34):14599-14604. [DOI](https://doi.org/10.1073/pnas.0907078106)** (PMID 19706547).
Claims grounded: **MECH-368** (primary), **MECH-361** (secondary). *According to PubMed.*

## What the paper does

Ballarini et al. take the synaptic **tag-and-capture** idea — that a weakly stimulated synapse sets a transient tag which, if it captures plasticity-related proteins made elsewhere, becomes durably potentiated — and demonstrate its behavioural analogue across three learning tasks in rats (spatial object recognition, contextual fear conditioning, conditioned taste aversion). The key result: weak training that normally produces only **short-term** memory is converted into **long-term** memory if it occurs within a critical time window of a *separate novel experience*. The conversion depends on newly synthesized proteins induced by the novelty (blocked by a protein-synthesis inhibitor). So a weak event sets an input-specific, protein-synthesis-*independent* "learning tag," and durability requires a second factor — the plasticity-related products that the tag captures.

## Why it grounds MECH-368

MECH-368 is the **event-level write-authority gate**: an explicit per-event transition from "observed/represented" to "write-eligible" over the durable model-update path, so that not every prediction error in an open channel writes. The conceptually load-bearing structure is a *separation between being eligible to write and actually consummating a durable write*. Behavioral tagging is the cleanest biological instance of exactly that separation. Setting the tag = becoming write-eligible; capturing the PRPs = consummating the durable write. The experiment shows this is not an engineering abstraction but how durable memory formation is actually gated: weak events sit in a transient eligible state and only some are converted, contingent on a salience/novelty signal arriving in time. That directly grounds MECH-368's `plasticity_eligibility` term as a real gated state, and its core motivation — durable write is licensed, not automatic.

It also reinforces MECH-361: which traces survive to long-term storage is *gated by salience/novelty*, consistent with affect/salience acting as a write-weight rather than every encoded event being written equally.

## Where the mapping strains (honest boundary)

Two divergences, both `failure_signatures`. First, the gated path here is **hippocampus-dependent episodic/behavioural memory** — and MECH-368's own notes concede the episodic write path is *already* substantially covered in REE. MECH-368's genuinely under-covered target is the **online world-model / policy weight-update** path. Behavioral tagging does not touch that; the analogy from episodic consolidation to E1/E2/policy weight-writes is structural, not demonstrated. Second, the "second factor" that licenses durable write is **novelty-induced protein availability** — a narrower, more passive trigger than MECH-368's posited active arbitration over `f(prediction_error, salience, pathway_state, residue_status, goal_relevance, plasticity_eligibility)`. Tagging shows *that* an eligibility-then-capture gate exists; it does not show the rich multi-input gate MECH-368 specifies.

So this entry grounds the **two-factor gating structure** that is MECH-368's backbone, while leaving the *path generalisation* and the *multi-input conditioning* as the parts still owed evidence. That is the right shape for a V4 candidate.

## Confidence

0.70, `supports`. Well-controlled PNAS study generalising a respected cellular mechanism to behaviour across three tasks. Mapping fidelity is moderate: the eligibility/consummation structure transfers cleanly; the path and the conditioning set diverge. Transfer risk is real (rat episodic memory → synthetic durable-write gate). Raises literature_confidence only; promotes nothing.
