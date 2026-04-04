# Bengio, Louradour, Collobert & Weston (2009) — Curriculum Learning (ARC-042 entry)

**Venue:** ICML 2009
**DOI:** 10.1145/1553374.1553380
**Citations:** ~17,000

## Relevance to ARC-042

ARC-042 proposes a three-phase staged development for ContextMemory:
- Phase 0: Bootstrap world model (no context discrimination)
- Phase 1: Supervised context training with terrain labels (Phase 1 gate must be crossed)
- Phase 2: Context-gated evaluation with frozen ContextMemory

This staging is a curriculum strategy. Bengio et al. (2009) provide the foundational ML theory and evidence that staged training is not merely convenient but necessary for non-convex representation learning objectives.

## Core Argument

Curriculum learning acts as a continuation method for non-convex optimization:
1. Simpler objectives (Phase 0: world model prediction) define loss landscapes with fewer bad local minima
2. Training on the simpler objective first guides parameters toward regions from which harder objectives (Phase 1: context discrimination) can be successfully learned
3. Initializing on the hard objective from scratch risks convergence to degenerate solutions

The EXQ-187a result (cosine_sim=1.0 after 150 warmup episodes) is precisely this: the label signal (lambda=0.1) was too weak to escape the trivial attractor without prior Phase 0 world-model grounding to shape the representation space.

## Implication for Phase 1 Gate

The curriculum learning framework predicts that the Phase 1 gate is qualitative, not merely quantitative. It is not that Phase 0 representations are "nearly good enough" and just need more training. Rather, Phase 0 representations (world-model-only) occupy a different region of representation space than what Phase 1 requires. The Phase 1 gate marks the transition from a world-model-shaped representation (useful for prediction) to a context-discriminating representation (useful for gating). Without explicitly crossing this gate (intensive supervised context training), the representation cannot reorganize spontaneously.

## Important Caveat

Bengio et al. demonstrate curriculum learning for example ordering within a fixed objective. ARC-042 proposes objective staging (different loss functions in different phases), which is a stronger claim. The curriculum learning framework provides conceptual support but does not formally prove that objective staging is necessary. The complementary evidence from Sanders et al. (2020) and Law et al. (2016) provides the mechanistic grounding: the context prior must be learned before inference is possible (Sanders), and this learning requires repeated contrastive multi-context exposure (Law).
