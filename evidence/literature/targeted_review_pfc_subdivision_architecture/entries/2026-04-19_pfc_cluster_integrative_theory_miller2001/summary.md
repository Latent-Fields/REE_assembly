# Miller & Cohen 2001 — An Integrative Theory of Prefrontal Cortex Function

## What the paper does

This is the canonical integrative review that cemented the "PFC as active maintenance of task-relevant representations" framing. Miller and Cohen argue that PFC neurons sustain activity across delays to represent current rules, goals, and context, and that this sustained activity projects back into posterior sensory, motor, and limbic cortices to bias processing toward task-appropriate responses. The paper synthesises primate single-unit recording (delayed-match-to-sample, Wisconsin Card Sort analogues, delayed-response tasks) with human lesion and fMRI evidence showing that dorsolateral PFC damage selectively impairs rule-guided behaviour while sparing stimulus-driven responses.

## Key findings relevant to MECH-261 and the PFC cluster

The load-bearing finding for REE is that PFC sustains rule representations over delays in a way that biases processing elsewhere. That gives REE a biological substrate for what MECH-261 is implicitly writing into during internal_planning and external_task modes — a rule/policy-level representation that holds current task demands and shapes action selection in downstream modules. Miller and Cohen are also careful to frame this as *biasing* rather than *commanding*: PFC doesn't directly execute the rule, it makes rule-consistent responses more probable in posterior circuits. That biasing-not-commanding distinction matters for REE because it means the lateral-PFC analogue does not need to sit in the action-execution path; it can sit upstream in the trajectory-proposal or value-weighting stages.

## How this translates into REE

The PFC of Miller & Cohen 2001 maps onto what REE needs as the write target for policy/rule-level updates — distinct from vmPFC value-map writes (ARC-035), distinct from viability-map writes in hippocampus, and distinct from sensory-cortical predictive updates (Rothschild 2017). In the operating-mode vector:

- **external_task:** lateral-PFC analogue actively holds the current rule; MECH-261 allows refinement writes.
- **internal_planning:** the analogue holds the rule for counterfactual rollout; MECH-261 allows speculative writes that are reversible.
- **internal_replay:** MECH-261 suppresses writes to this substrate so that imagined trajectories don't clobber the currently held rule.
- **offline_consolidation:** MECH-261 permits slow consolidation writes that stabilise rules learned during waking task performance.

## Limitations and caveats

The 2001 framing predates the PFC-subdivision literature that has since become load-bearing for any careful implementation. Badre & Nee 2018 (hierarchical control), Rudebeck & Murray 2014 (OFC as credit/value oracle distinct from vmPFC), and Mansouri 2020 (lateral-PFC for abstract rules specifically) all refine what the 2001 paper left as an undifferentiated "PFC." REE must not inherit the unified-PFC framing; it must import the rule-maintenance function specifically into the lateral-PFC analogue, and route value, credit, effort, and planning-depth functions into the appropriate subdivisions (vmPFC, OFC, dACC, frontopolar). The 2001 paper is the entry point, not the finished map.

## Confidence reasoning

Source quality is very high — this is a foundational review with two decades of corroboration. Mapping fidelity is moderate rather than high because REE has to treat "PFC" in the 2001 sense as "lateral PFC specifically." Transfer risk is low for the rule-maintenance claim itself but climbs sharply if the unified framing is imported uncritically. Net confidence: 0.82.
