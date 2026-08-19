---
nav_exclude: true
---

# Q-093 Discussion: Dimensionality and Dynamics for Neural Network Efficiency

**Source email:** `REE: email i found I sent myself a while ago`  
**Primary source:** Wang G, Fan F-L (2025). *Dimensionality and dynamics for next-generation artificial neural networks*. Patterns, 6(8): 101231. DOI: `10.1016/j.patter.2025.101231`; PMID: `40843340`; PMCID: `PMC12365495`.  
**News source that triggered intake:** TechXplore / RPI, "Rethinking AI: Researchers propose a more effective, human-like approach" (2025-06-13).  
**Related REE claim:** `Q-093` -- cognitive efficiency / control-machinery scaling.

## Why This Was Not Filed As Strong Evidence

This paper is a perspective, not an empirical demonstration. It argues that next-generation neural networks may benefit from two families of structure:

- **Dimensionality expansion:** not just width and depth, but "height" or additional intra-layer/inter-network structure, implemented through intra-layer links, hypernetwork-like dependencies, or higher-dimensional organization.
- **Dynamics through feedback:** feedback loops, Hopfield-like associative memory, diffusion/noising-denoising loops, state-space compression/recovery, and phase-transition-like behavior.

That is conceptually relevant to REE, but it does not test REE, does not compare systems at matched competence, and does not establish that the proposed structures actually reduce lifetime compute. It should therefore inform discussion around `Q-093`, not alter any claim status.

## Does It Help REE?

Yes, but mostly by sharpening questions REE already had.

The paper supports the idea that efficiency is not only about making a network smaller. It can come from using the right **organization of state and recurrence**: persistent structure, feedback loops, higher-dimensional factorization, and selective dynamics. That is close to the intuition behind `Q-093`: perhaps REE's organizing machinery can remain comparatively compact while the representational spaces it organizes become richer.

The useful REE translation is:

> REE efficiency, if it exists, will probably not come from "small model beats large model." It would come from structured state plus selective recurrent control reducing the need to recompute cognition from scratch.

That is the same core idea already in `docs/thoughts/2026-08-10_REE_efficiency.md`, but Wang and Fan give it an external vocabulary: height, dimensional augmentation, feedback loops, attractor/phase-transition dynamics, and reservoir-like high-dimensional dynamic embeddings.

## What It Adds To Q-093

`Q-093` currently asks whether REE's control/organizing machinery scales sublinearly relative to representational richness, measured at matched behavioral competence and across total lifetime cost.

This source suggests several more precise sub-questions:

1. **Dimensional decomposition:** Does adding structured latent axes or intra-module links let a REE substrate represent more without scaling every control module proportionally?
2. **Recurrent state dividend:** Does persistent recurrent state reduce repeated context reconstruction cost compared with repeatedly invoking a large model over long context?
3. **Loop topology:** Are REE's feedback loops merely implementation details, or do specific loop topologies produce qualitatively different competence regimes?
4. **Phase transitions:** Are there threshold transitions in competence, stability, or failure when recurrence, dimensionality, or coupling crosses some regime boundary?
5. **Reservoir-like strategy:** Could some REE components use high-dimensional dynamic state with a comparatively cheap readout, while preserving inspectability better than opaque reservoir computing normally does?

These are useful for the future evaluation-methodology document flagged in the original `REE_efficiency` intake.

## What It Challenges

The paper also warns against a weak version of the REE efficiency story.

If REE merely says "we have compact explicit modules, therefore we are efficient," that is not enough. Wang and Fan's argument points the other way: useful efficiency may require **more internal structure**, not less. A richer REE may need higher-dimensional latent spaces, recurrent loops, and complicated cross-module dependencies. That could still be efficient if the structure gives better separability, reuse, memory, and selective computation. But it could also become expensive or unstable.

So the right pressure on REE is:

- Do not equate compactness with efficiency.
- Do not equate dimensionality with waste.
- Do not add recurrence or higher-dimensional links unless they buy measurable competence, stability, or adaptation.
- Count training/raising, inference, replay, memory, adaptation, and planning cost together.

## What It Does Not Prove

- It does not show that "3D neural networks" are generally better.
- It does not show that intra-layer links outperform existing architectures on REE-relevant tasks.
- It does not show that feedback loops yield safe or inspectable cognition.
- It does not show that phase transitions are desirable; REE has many places where abrupt transitions are hazards.
- It does not answer `Q-093`, because no matched-competence lifetime-cost comparison is supplied.

## REE Discussion Verdict

This helps as a **conceptual design prompt** for `Q-093`, not as a claim update.

The most useful idea is to separate three scaling axes:

1. **Representational richness:** how much the system can encode.
2. **Organizing/control machinery:** how much machinery is needed to use those representations.
3. **Dynamic state and loop topology:** how much competence is carried by persistent state, recurrence, and attractor structure rather than by recomputation.

Future REE efficiency tests should measure these separately. A convincing REE efficiency result would show that representational richness can increase while the organizing machinery and per-cycle cost grow more slowly, without hiding costs in replay, memory, or developmental experience.

No claim status change. No new claim registered. This is a discussion note attached to the `Q-093` research thread.
