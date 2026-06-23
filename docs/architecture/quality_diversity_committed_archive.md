---
title: Behavioral-Descriptor Committed-Selection Archive (conversion-ceiling locus)
parent: "Executive & PFC Control"
grandparent: Architecture
nav_order: 3
---

# Behavioral-Descriptor Committed-Selection Archive (conversion-ceiling locus)

**Status:** architecture stub for candidate claim MECH-442 (candidate / substrate_conditional / implementation_phase v3 / version_relevance v3). Registered 2026-06-18 from a REE_convergence intake (Quality-Diversity / MAP-Elites, demand-queue row CDQ-003). **V3-leaning (on the V3 work surface); off no closure node's build path — registering it blocks no V3 closure node and adds depends_on cross-refs only.** Decide-whether-to-build is a later governance step.

## Problem (the necessity is clear, the mechanism is not)

The committed-action-diversity conversion ceiling is the single most recurrent V3 blocker (this cycle: 460f de-commit authority, 654f CRF gate lockout, 625d monostrategy lock, 687 tonic-noise GAP-C). REE GENERATES per-candidate diversity at the scoring/proposer layer (ARC-065 modulatory channel, MECH-341 within-class preserver, MECH-313 noise floor, rule-bias) that COLLAPSES at the committed argmax. The primary harm/goal score F monopolises ~88-89% of E3 committed-selection variance (V3-EXQ-571, unmoved by the full diversity stack), so every diversity channel drowns at the one selector — the F-dominance diagnosis MECH-439. The **necessity** (diversity must reach committed action, `behavioral_diversity_isolation:GAP-B`) is established. The **mechanism** to preserve diversity through the commit is not.

The only structure that has converted is the **top-k shortlist** (`ree-v3/ree_core/predictors/e3_selector.py`, `modulatory_shortlist_mode='top_k'`, k=3; V3-EXQ-569i PASS): shortlist the k F-best candidates whose membership rotates with state, then arbitrate within by the routed channel. Its margin is THIN (2/3 seeds, ~0.06 nats) and the conversion-ceiling Phase-0 synthesis flags F-dominance as the still-LIVE root for the downstream 625d/654f composites.

## Convergence provenance

Intake thread: **Quality-Diversity / MAP-Elites** (REE_convergence, 2026-06-18; demand-queue row CDQ-003). Promotion packet `CPKT-QUALITY-DIVERSITY-20260618`.

- **MAP-Elites / Quality-Diversity** (Cully et al. 2015, Nature, doi:10.1038/nature14422; Mouret & Clune 2015, arXiv:1504.04909; Pugh/Soros/Stanley 2016) — an explicit **archive** indexed by a **behavioral descriptor**, where each niche keeps its own **elite** (within-niche fitness-best) regardless of global ranking, so a behaviorally-distinct option is not annihilated by a fitter-but-different one. Diversity survives selection by construction.

Comparison artifacts: `REE_convergence/sources/quality-diversity/comparison_table.md`, `REE_convergence/reports/2026-06-18_quality_diversity_conversion_ceiling_synthesis.md`.

## MECH-442 — behavioral-descriptor committed-selection archive (the candidate mechanism)

Partition the eligible E3 candidate set by a **behavioral descriptor** (a behavioral axis — first-action class, committed-action class, or an e2.world_forward strategy signature, NOT F-rank), retain the **F-best candidate within each behavioral niche**, and commit via a **coverage-aware rule**. A behaviorally-distinct action stays selectable through the commit at a **moderate F-gap**, bounded by the per-niche-elite safety envelope (the selected action is still the F-best within its niche; clearly-harmful niches excluded — the same guarantee as top-k's "only the k F-best are eligible"). The validated 569i top-k shortlist is the **degenerate descriptor-free instance** (the niche axis IS F-rank, near-ties only); MECH-442 generalizes it to a behavioral-descriptor-indexed archive predicted to convert per-candidate diversity into committed-action diversity more robustly than the thin near-tie shortlist.

**Falsifier:** if a behavioral-descriptor-indexed committed-selection archive does NOT lift committed-action-class entropy strict-above BOTH collapsed-proposer and matched-noise on ≥2/3 seeds **beyond** the descriptor-free top-k shortlist (V3-EXQ-569i), OR lifts it only by selecting F-dominated/unsafe actions past the per-niche-elite bound (a quality/safety regression), the behavioral-descriptor archive earns no keep over top-k. Pre-registered discriminator: the 2×2 (F-de-collapse) × (behavioral-descriptor archive vs top-k) committed-selection ablation under the C+D composite, with a per-niche F-quality guard.

## Biological grounding (the framing refinement, 2026-06-18 lit-pull)

The `/lit-pull` (`evidence/literature/targeted_review_connectome_mech_442/`, 5 PubMed sources; SYNTHESIS verdict SUPPORTED-with-refinement) grounds the **necessity** and the **existence** of a behavioral-repertoire archive but **relocates the mechanism upstream of the commit gate**:

- A structured behavioral-module **repertoire is a real biological object** — the dorsolateral striatum encodes the identity/ordering of a discrete repertoire of behavioral modules and is required to assemble them (Markowitz et al. 2018, Cell).
- Behavioral diversity is an **actively-maintained, regulated feature**, not noise (Dhawale, Smith & Olveczky 2017, Annu Rev Neurosci).
- Diversity is generated by a **circuit separate from the motor selector** — a basal-ganglia circuit (LMAN/AFP) generates and regulates variability in parallel with the premotor output (Kao & Brainard 2006; Tesileanu, Olveczky & Balasubramanian 2017).
- **Load-bearing weakens:** the basal-ganglia selection gate is a **winner-take-all** that collapses to a single directed action under a strong reward gradient (Ponzi 2007). So **F-dominance at the commit (MECH-439) is biologically faithful** — diversity cannot be preserved by a per-niche structure operating *at* the argmax.

**Refinement carried into the claim:** the archive lives **upstream of / restricts the eligible set *before*** the winner-take-all commit (exactly what the 569i top-k does — an eligible-set restriction), coupled to an **active variability generator** (hence MECH-442 `depends_on` ADDS **MECH-313**). The F-dominated argmax itself is biologically correct; MECH-442 changes the eligible-set structure feeding it, not the argmax.

## Relationship to the cluster

- **MECH-439** — F-dominance, the conversion-ceiling diagnosis this archive circumvents (and which the biology confirms is the faithful behavior of the commit gate).
- **ARC-065** — the behavioural-diversity GENERATION pathway whose output the archive preserves through the commit.
- **MECH-341** — the within-class diversity preserver (the scoring-layer sibling); the archive is the committed-selection-layer complement.
- **MECH-294** — the selection-authority/binding substrate the archive must route around F with.
- **MECH-313** — the active variability-generator analog the biology pairs the repertoire with (added to depends_on per the lit-pull refinement).
- **ARC-062** — the rule-apprehension selector half; its committed reach is gated by the same F-dominance.

The validated V3-EXQ-569i top-k shortlist is the existing point-fix (descriptor-free eligible-set restriction); MECH-442 is the principled, behavioral-descriptor-indexed generalization behind it. The adapter **amends the GAP-B conversion locus** (generalizes the validated top-k selection structure) rather than minting a parallel module.
