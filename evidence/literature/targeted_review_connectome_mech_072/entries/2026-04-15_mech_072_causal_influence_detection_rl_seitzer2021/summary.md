# Causal influence detection: a forward-model-based primitive for the discriminator gate

**Source:** Seitzer, Scholkopf & Martius (2021), NeurIPS 2021. arXiv: 2106.03443

## The question this paper answers

MECH-072 requires a discriminator that asks, at the moment harm occurs, whether the agent's action actually had causal influence over that outcome. This is not a single scalar threshold but a situation-dependent question: in some states the agent can affect certain aspects of the world, and in others it cannot. A discriminator gate that operates regardless of situation would either suppress too much residue (overblocking harmless situations) or too little (failing to gate in cases where the agent had no real influence). Seitzer and colleagues provide the computational primitive for situation-dependent causal influence detection.

## The approach

The core measure is conditional mutual information: I(action; next_state | current_state). This asks, given the current state, how much does the choice of action predict the resulting next state? When this is high, the agent has real causal influence; when it is near zero, what happens next is largely independent of what the agent does. Crucially, this measure is situation-dependent: the same agent has high influence in some states (reaching distance from an object) and near-zero influence in others (object out of reach entirely).

The authors estimate this quantity using a learned forward model of environment dynamics. The forward model predicts next states from (state, action) pairs; the conditional mutual information is estimated from the spread of predictions across actions in a given state. They show this measure reliably detects influence states and integrate it into RL algorithms to improve exploration efficiency and off-policy learning on robotic manipulation tasks.

## The relevance to MECH-072's discriminator design

MECH-072's foreseeable-harm gate is described as a discriminator on (z_world_delta, is_agent_caused) pairs. The 'is_agent_caused' component is exactly a causal influence detection problem. Seitzer et al. provide a principled method: compute conditional mutual information between the agent's action and the world-state change (z_world_delta in REE terms), conditioned on the current world state. When this is high, the agent had influence and residue accumulation is appropriate. When this is near zero, the harm was environmentally determined and the gate should suppress residue.

This suggests that MECH-072's discriminator need not be a separately trained classification network. Instead, the E2 forward model can provide the causal influence estimate directly: the spread of E2's z_world predictions across counterfactual actions in the current state gives the conditional mutual information approximation. The gate threshold is then a setting on this information measure rather than a learned binary classifier.

## Situation-dependence and the false attribution problem

The EXQ-213 result -- 48% false attribution rate without gating -- is consistent with Seitzer et al.'s observation about situation-independent RL. Without detecting whether actions had causal influence in specific situations, reward signals (or harm signals) are assigned to actions regardless of whether those actions actually mattered. Seitzer et al. show that detecting and exploiting this influence structure substantially improves learning. MECH-072's gating achieves the same gain, but on the harm residue channel specifically.

## Caveats

The paper's application domain is exploration efficiency, not harm attribution. Causal influence ('could I have affected this?') and causal attribution ('did I actually cause this?') are related but distinct. The mutual information measure supports the former; the latter requires a counterfactual comparison (see Mesnard et al. 2021 for the complementary credit assignment literature). The full MECH-072 discriminator likely needs both: Seitzer's influence detection to establish whether the agent was in a position to cause harm, and Mesnard's counterfactual logic to estimate how much of the harm was actually agent-caused.
