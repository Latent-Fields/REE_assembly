# Computational Models of Interoception and Body Regulation

**Petzschner et al. (2021) -- Trends in Neurosciences -- DOI: 10.1016/j.tins.2020.09.012 -- PMID: 33378658**

## What the paper did

Petzschner and colleagues review the landscape of computational models applied to interoception and body regulation. The paper is organized around a sensory-control loop framework: models of interoceptive perception describe how the brain estimates the current state of the body from ascending interoceptive signals; models of body regulation describe how actions are selected to maintain or restore desired bodily states; models of forecasting describe how the brain predicts future bodily states as a consequence of planned actions. The review covers Bayesian perceptual models, active inference frameworks, control-theoretic models, and reinforcement learning approaches. Clinical implications are addressed throughout: disruption of perceptual models maps to somatic symptom disorders; disruption of regulatory models maps to failure of adaptive behavior under physiological challenge; disruption of forecasting maps to anticipatory anxiety and allostatic overload.

## Key findings relevant to MECH-113

The structurally important contribution for MECH-113 is the demonstration that three computationally distinct problems must be solved to achieve adequate interoceptive self-regulation. These are not redundant framings of the same problem -- they have different information requirements, different failure modes, and different timescales. Perceptual models operate on current evidence. Regulatory models select actions. Forecasting models look ahead. This tripartite structure is directly instantiated in MECH-113's three-level design. A system that only monitors current coherence (Level 1) cannot anticipate future coherence failures (Level 2) and cannot model its own capacity to prevent them (Level 3). The review confirms that all three are needed and that collapsing them produces characteristic pathologies at the collapsed boundary.

The review also explicitly notes that interoceptive active inference -- in which actions are chosen to bring actual bodily states into alignment with predicted states -- requires a forward model of how actions affect bodily state. This is the Level 2 mechanism in MECH-113: E2 as forward model of z_self dynamics, monitoring predicted D_eff over rollout horizon. The biological analog is the anticipatory regulation system that adjusts metabolic setpoints before exertion, not only after deviation is detected.

## REE translation

The three-part taxonomy (perceive, regulate, forecast) provides independent computational motivation for MECH-113's architecture that is not dependent on any particular biological substrate. The argument is that the computational problems are real -- they arise from the structure of the agent-environment interface -- and any agent that must maintain its own functional integrity over time will encounter them. REE's z_self coherence monitoring is the perceptual component; the allostatic anticipatory monitoring (Level 2, not yet implemented) is the regulatory/forecasting component; metacognitive self-efficacy monitoring (Level 3, V4 scope) is the capacity-monitoring component. The architecture is not borrowed from biology for its prestige -- it reflects the actual computational requirements.

## Limitations and caveats

The review covers computational models of biological interoception exclusively. The empirical evidence it synthesises is from human interoceptive experiments, autonomic regulation studies, and clinical neuroscience. There is no evidence presented for artificial agents, and none of the reviewed models resembles REE's architecture. The transfer therefore requires an argument by structure rather than by direct evidence: the claim is that the same three computational problems arise in REE as in biological interoception, and so the same three-level architecture is warranted. This argument is plausible but not demonstrated. A further caveat: the review was published in 2021 and the field has moved quickly; some of the specific computational models reviewed may have been superseded.

## Confidence reasoning

Confidence is set at 0.75. Trends in Neurosciences is a high-impact venue and Petzschner is a leading authority in this literature. The three-level taxonomy is well-established and the mapping to MECH-113's design is direct. The limitation is that the paper provides architectural grounding, not experimental validation, and the transfer to an artificial agent context remains the untested step. This is one supporting entry in a cluster -- its value is in confirming that the three-level design reflects genuine computational structure rather than arbitrary complexity.
