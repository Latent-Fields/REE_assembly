# Bengio, Louradour, Collobert & Weston (2009) — Curriculum Learning

**Venue:** ICML 2009
**DOI:** 10.1145/1553374.1553380
**Citations:** ~17,000 (foundational reference)

## Relevance to MECH-153 and ARC-042

This paper establishes the theoretical and empirical basis for staged/ordered training strategies. It is relevant to both claims:

- **MECH-153**: The EXQ-187a failure (cosine_sim=1.0 with lambda=0.1, 150 warmup episodes) is a curriculum-without-curriculum failure: the label-supervised discrimination objective is the "hard task" that was introduced at full complexity from the start with insufficient signal strength.

- **ARC-042**: The Phase 0/1/2 developmental structure is explicitly a curriculum strategy -- Phase 0 establishes an easier world-model objective, Phase 1 introduces the hard context-discrimination objective, Phase 2 evaluates the frozen result.

## Core Contribution

Bengio et al. formalize the observation that humans and animals learn better when examples are organized from easy to hard. The formal argument is that curriculum learning is a continuation method for non-convex optimization:

1. Simple tasks/examples define loss landscapes with fewer bad local minima
2. Training on simple tasks first guides parameters toward a region of the loss surface from which the hard task can be successfully learned
3. Training on the hard task from scratch risks convergence to degenerate solutions

The paper provides empirical evidence in:
- Text chunking (NLP)
- Language modeling
- Shape recognition (vision)

## Key Mapping

The ARC-042 Phase 0/1/2 structure instantiates a two-stage curriculum:

| Curriculum Stage | ARC-042 Phase | Objective |
|-----------------|---------------|-----------|
| Easy task warm-up | Phase 0 | World model prediction (self-supervised) |
| Hard task introduction | Phase 1 | Supervised context discrimination (terrain labels) |
| Evaluation | Phase 2 | Frozen context representations used for gating |

Bengio et al.'s theory predicts that Phase 0 is not optional: without it, the joint Phase 0+1 objective may converge to the degenerate solution (all representations identical) because the self-supervised prediction signal dominates and the label signal is too weak (lambda=0.1) to escape.

## Important Caveat

Bengio et al. demonstrate curriculum ordering of examples within a fixed objective. ARC-042 proposes objective staging (different loss functions in different phases). This is a stronger version of the curriculum hypothesis. The curriculum learning framework supports the intuition but does not formally prove objective-staging necessity. The additional justification comes from the Law et al. (2016) hippocampal evidence: the biological system also requires a staged process -- first forming context representations through repeated exposure, then consolidating discriminating structure.

## Limitations

- Empirical demonstrations in NLP/vision, not LSTM context memory
- Complete collapse (cosine_sim=1.0) is more extreme than typical curriculum failures
- Does not address label signal strength (lambda) as a separate dimension from ordering
