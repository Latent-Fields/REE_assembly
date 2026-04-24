# Lewis & Durrant 2011 -- Overlapping memory replay during sleep builds cognitive schemata

## What the paper did

Lewis and Durrant write a synthesis paper in *Trends in Cognitive Sciences* that proposes a mechanism by which sleep produces cognitive schemata. Their proposal: during NREM slow-wave sleep, the hippocampus replays recent episodic traces; when traces share elements (a place, an event-type, a sensory regularity), those shared elements occur in the cortex more often than the episode-specific details. Cortical Hebbian learning then strengthens the invariants and lets the episode-specific details fade. The output is a schema -- a generalised representation of what is common across the replayed episodes -- stored in cortex and increasingly independent of the hippocampus that originally indexed it.

The paper draws together rodent place-cell replay literature, human declarative consolidation behaviour, and computational modelling of overlapping reactivation. It does not run a new empirical study; it argues that the existing pieces fit a single coherent mechanism.

## Key findings relevant to MECH-275 and MECH-273

The mechanism Lewis & Durrant describe is structurally what MECH-275 asserts. Both claim that sleep aggregates across many recent traces, that the aggregation is over the regularities common to the traces (not the episode-specific surface), and that the output is a stable cortical representation that survives loss of the original hippocampal index. MECH-275 calls the output "schema revision"; Lewis & Durrant call it "schema construction". The functional shape is the same.

For MECH-273 specifically, the mapping is the self-attribution specialisation: many SD-003 outputs across many episodes are the "shared traces", the regularities that survive replay are the stable self-attributions (which actions are reliably self-initiated, which biases are systematic), and the cortical schema that emerges is the stable self-model. Without the sleep aggregation step, MECH-273 predicts -- and Lewis & Durrant's framework predicts -- an episode-local representation rather than a durable model.

## How the findings translate to REE

The translation is direct at the cognitive-mechanism level: overlapping replay → invariant extraction → cortical schema. REE inherits this and specifies the routing: the aggregated output is delivered to E1 (world-model consolidation) and SD-033a (viability-map revision) via MECH-271/MECH-272 anchored channel.

## Limitations and caveats

The mapping has one important gap. Lewis & Durrant treat the replayed episodes as the input -- they do not require the input to be counterfactual-backed. MECH-275 explicitly requires this: aggregation over arbitrary correlation would produce noise-fit, not schema revision. The paper would, on its face, also aggregate noise. REE adds MECH-276 (counterfactual-backed waking-phase intervention) as the precondition that makes the aggregation meaningful. A strict reading of Lewis & Durrant supports the aggregation mechanism but not the input requirement.

Two further caveats. First, Lewis & Durrant route the output to cortex only; MECH-273 routes to two consumers (E1 and SD-033a) via the anchored channel. The paper does not motivate or rule out the dual-target routing. Second, the paper's mechanism is monotonic statistical extraction; MECH-273 includes a correction sub-mechanism (overturning previously-held spurious self-attributions when post-hoc evidence accumulates against them) that needs non-monotonic Bayesian revision, not just Hebbian averaging.

## Confidence reasoning

Confidence 0.78 -- supports both claims. The aggregation mechanism is the right shape and the paper is widely cited and influential (foundational TICS review). It is held below 0.8 because the input-requirement gap (counterfactual-backed feedstock) is a load-bearing piece of MECH-275 that this paper does not motivate, and the correction-not-just-averaging gap is load-bearing for MECH-273. Source quality is high; mapping fidelity is moderate; transfer risk is low because the mechanism is described at the cognitive-computational level.
