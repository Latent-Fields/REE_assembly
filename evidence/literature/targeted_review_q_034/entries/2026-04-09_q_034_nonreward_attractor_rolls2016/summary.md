# Summary: Rolls (2016) -- A non-reward attractor theory of depression

**Entry:** 2026-04-09_q_034_nonreward_attractor_rolls2016
**Claim tested:** Q-034
**Evidence direction:** supports

## What the study did

Rolls (2016) proposes a computational theory of depression grounded in the circuit architecture of the orbitofrontal cortex (OFC). The theory uses integrate-and-fire neural network modelling of reciprocally inhibiting reward and non-reward attractor populations in the medial and lateral OFC respectively. The key claim is that depression is an attractor state -- a self-sustaining pattern of activity in the lateral OFC non-reward population -- and that the transition into this state depends on the balance between reward and non-reward inputs, not on absolute non-reward magnitude alone.

## Key findings

The model's critical prediction for Q-034 is structural: the non-reward attractor cannot sustain itself when reward input is sufficient to maintain the reciprocally inhibiting reward attractor. This means: (1) the same non-reward input that triggers depression in a reward-depleted context may not trigger it in a reward-rich context, because the reward attractor quashes the non-reward attractor via reciprocal inhibition; (2) therapeutic intervention can target either the non-reward side (reducing harm exposure, standard treatment) or the reward side (increasing reward input / antidepressant facilitation of medial OFC), because both shift the same balance; (3) the transition point between attractors is determined by the ratio of reward to non-reward input strength, not by either in absolute terms. The paper also reviews human and animal neuroimaging evidence for the lateral OFC non-reward system and its role in anhedonia.

## REE translation

Rolls (2016) provides the strongest computational-theoretical grounding for Q-034 among the four entries. The attractor language is directly compatible with REE's attractor state framing for INV-053, and the reciprocal inhibition architecture implements the ratio logic at the neural circuit level. If we map OFC reward input to REE's benefit_exposure and OFC non-reward input to hazard_exposure, the Rolls model predicts exactly what Q-034 asks: the depression attractor engages when non-reward input exceeds what the reward attractor can suppress -- i.e., when the ratio crosses a threshold. Both increasing resources (reward input) and reducing hazards (non-reward input) are valid therapeutic strategies because they operate on the same balance. This bilateral therapeutic implication is explicit in the paper and clinically important.

## Limitations and caveats

The model operates at the OFC circuit level, not at the level of environmental parameters. The mapping from "OFC reward input" to "environmental benefit_exposure density" requires an inferential bridge the paper does not provide. The ratio threshold is not explicitly parameterised -- the model demonstrates that a threshold exists without specifying where it lies or how it scales with environmental parameters. Additionally, the model does not cleanly distinguish between harm exposure and absence of reward -- in REE terms, hazard_harm and num_resources are independent variables, but in the Rolls model they enter as a single net input imbalance. This means the model supports the existence of a ratio threshold but cannot resolve whether the specific operationalisation in CausalGridWorldV2 captures the relevant parameters.

## Confidence reasoning

Confidence 0.65. This is the most conceptually direct paper for Q-034 because it uses attractor state language and explicitly models balance-of-inputs as the determining parameter. Source quality is high (Neuroscience and Biobehavioral Reviews, senior computational neuroscientist, >1000 citations). Mapping fidelity is moderate: the attractor state framing maps well, but the circuit-to-environment inferential gap and the absence of parametric threshold specification limit the fidelity. The paper confirms that the ratio logic has computational precedent in the depression literature, which is strong support for Q-034 as a research question worth pursuing.
