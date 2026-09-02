# Developmental Ecology Assays — Incubator

**Status:** incubator / pre-claim research programme  
**Created:** 2026-09-02  
**Relationship to REE:** adjacent programme; not part of the canonical REE architecture or V3 closure path

## Boundary

This directory develops the **Developmental Ecology Assays** idea while it is still being tested for scientific usefulness.

The core inversion is:

> **Hold a developing probe organism and protocol sufficiently stable, then characterise an information environment by the distribution and causal history of phenotypes it produces.**

This is deliberately different from asking only how well an agent performs in a benchmark or from changing environments in order to make an agent better.

Nothing in this directory is an REE architecture claim, V3 requirement, green-board blocker, experiment-queue item, or evidence-bearing result unless it later passes through the normal REE thought/claim/experiment/governance machinery.

The incubator exists to prevent an attractive adjacent programme from silently expanding V3 scope.

## Provenance

The programme emerged from the 2026-09-02 discussion of retained REE versions and their practical niches.

Source material:

- [Programme seed](../../thoughts/2026-09-02_developmental_ecology_assays_programme_seed.md)
- [Preliminary novelty and neighbour scan](../../thoughts/2026-09-02_developmental_ecology_novelty_scan.md)
- [Versioned organisms / retained lineages](../../thoughts/2026-09-02_versioned_organisms_capacity_boundaries_and_retained_lineages.md)
- [Ecological succession as developmental curriculum](../../thoughts/2026-08-11_ecological_succession_as_developmental_curriculum.md)
- [Longitudinal artificial-organism neuroscience](../../thoughts/2026-08-13_behaviour_linked_substrate_imaging_longitudinal_artificial_organism_neuroscience.md)

The earlier ecological-succession thought already established **environment as an experimental instrument** for revealing what REE can and cannot learn. This incubator adds a different inversion: the developing organism itself becomes a standardised instrument for measuring what an environment teaches.

## Current artefacts

1. [`ecology_adapter_v0_1.md`](ecology_adapter_v0_1.md) — architecture-neutral adapter contract with an initial REE-V3 compatibility profile.
2. [`assay_001_yoked_controllability_prereg.md`](assay_001_yoked_controllability_prereg.md) — pre-registration-style design for the first matched-adulthood / different-childhood assay.

## Programme discipline

The programme should earn complexity rather than inherit it from REE.

Before creating a standalone repository or product layer it should demonstrate, at minimum, that a developmental assay can provide useful information about an environment that is not captured as cheaply by conventional agent score, coverage, static inspection, or a standard reinforcement-learning test agent.

A negative result is informative. If conventional methods provide the same diagnosis more cheaply, or if developmental phenotype adds no explanatory information, the programme should contract rather than protect itself by adding machinery.

## Immediate gate

The next gate is not commercialisation and not a large platform build.

It is:

> **Can one tiny, well-controlled ecology produce a reproducible developmental phenotype under a causal manipulation, and can that phenotype be measured without leaking the manipulation to the organism?**

Assay 001 is designed to answer that question.