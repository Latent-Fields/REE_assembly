# Badre & Nee 2018 — Frontal Cortex and the Hierarchical Control of Behavior

## What the paper does

Badre and Nee synthesise two decades of fMRI and lesion evidence for a caudal-to-rostral gradient within lateral PFC. Posterior regions near premotor cortex handle concrete stimulus-response mappings; mid-lateral PFC (roughly middle frontal gyrus, BA 46/9) represents the current task rule or cognitive set; rostrolateral PFC and frontopolar cortex (BA 10) handle abstract, temporally extended, contextually embedded policies — the kind of representation that lets you nest one task inside another, hold a pending sub-goal while executing a current sub-goal, or reason about alternative policies before committing. The review is careful to distinguish the "policy abstraction" framing from rival "domain" and "temporal integration" accounts, and concludes that the abstraction framing best fits the converging data.

## Key findings relevant to MECH-261 and the PFC cluster

The architectural implication for REE is that there is not a single lateral-PFC write target; there is a gradient. An implementation that writes rules into "the PFC analogue" without specifying which level along the abstraction gradient it is writing into will blur functions that biology separates. Concretely:

- Concrete stimulus-response updates (when a habitual routine needs refinement) belong in a posterior / premotor-SMA-adjacent substrate.
- Current-rule / current-set updates (when the active task demand changes) belong in mid-lateral PFC.
- Policy-selection / branching / meta-control updates (when the agent is choosing between candidate policies rather than refining within a policy) belong in frontopolar cortex.

Each of these write targets may have different mode-gating profiles under MECH-261. In particular, frontopolar-analog writes are probably only licensed during internal_planning (explicit counterfactual branching) and strongly suppressed during external_task (too abstract, would destabilise committed execution).

## How this translates into REE

This is the cleanest biological argument I have seen for not lumping "PFC analogue" into one module. The V3 minimum should implement the mid-lateral rule level. The frontopolar branching level is V4 scope — it is the substrate where explicit counterfactual policy comparison happens, and REE's internal_planning mode is the natural home for it. The premotor/SMA level overlaps with what ARC-035 and existing E3 sequence-selection machinery are already doing and may not need a new substrate.

## Limitations and caveats

The strict caudal-rostral ordering has been contested. Some authors (e.g., Christoff & colleagues) argue for a domain-based rather than abstraction-based organisation; others argue the gradient is driven by temporal integration depth rather than policy abstraction per se. REE should implement the gradient as a soft ordering rather than a rigid stack: multiple abstraction levels exist as separable write targets, but the specific correspondence between anatomical position and abstraction depth should be treated as a working hypothesis. The review is also fMRI-heavy, so spatial resolution claims should be read with the usual BOLD caveats.

## Confidence reasoning

Source quality high (Trends review, thorough synthesis, well-cited). Mapping fidelity is strong because the paper's "abstraction gradient" vocabulary translates almost directly into REE's multi-level control vocabulary. Transfer risk moderate — the claim that multiple levels of abstraction are separable write targets is robust, but the strict ordering is not. Net confidence: 0.80.
