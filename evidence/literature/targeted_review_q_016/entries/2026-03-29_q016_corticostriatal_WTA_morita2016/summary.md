# Corticostriatal circuit mechanisms of value-based action selection: Implementation of reinforcement learning algorithms and beyond

**Morita, Jitsev & Morrison (2016) — Behavioural Brain Research**
DOI: [10.1016/j.bbr.2016.05.017](https://doi.org/10.1016/j.bbr.2016.05.017)
*Based on articles retrieved from PubMed*

## What the paper did

Morita and colleagues provided a systematic theoretical review asking how corticostriatal local circuits implement reinforcement learning algorithms. They organised the literature around two questions: (1) what selection operation does the striatum perform -- winner-take-all (WTA, max) or something softer? -- and (2) how does the cortical circuit contribute to the same selection problem? The review synthesised experimental data on lateral inhibition in striatum, recurrent excitation in cortex, and dopamine-mediated plasticity to propose a dual-mechanism model.

## Key findings

The striatal circuit -- despite having weaker and sparser lateral inhibition than classical WTA models assume -- can still generate WTA-like behaviour on short timescales through the dynamics of D1/D2 pathway competition. The cortical circuit, with its recurrent excitation, implements a softer probabilistic selection (soft-max) and can sustain activity representing the chosen action long enough for dopamine neurons to receive the credit-assignment signal they need to compute reward prediction error. The paper argues these two mechanisms are complementary: striatal max selects the current best action; cortical soft-max provides temporal integration and probabilistic exploration. The sequence dynamics of striatal circuits on longer timescales remain an open question -- the paper proposes that sequences of WTA fragments may implement replay, action representation, or probabilistic sampling.

## REE translation

Q-016 asks what arbitration policy avoids coupling collapse when REE's three cortico-striatal loops disagree. Morita et al. offer a principled framing: there is not one arbitration policy but two operating at different timescales and anatomical levels. The motor loop's BG circuit naturally tends toward WTA (fast, categorical commitment); the planning loop's prefrontal-striatal circuit naturally tends toward soft-max (slower, exploratory). Coupling collapse becomes a risk when a WTA outcome from one loop is treated as a hard constraint by the others -- for example, if the motor loop commits and its WTA signal is fed back as a hard prior to the planning loop, the planning loop's probabilistic exploration is foreclosed. The arbitration policy that prevents this must preserve loop independence: the motor loop's WTA commitment should update the planning loop's priors, not replace them. In REE terms, committing at the motor gate should not close the E3 simulation channel -- E3 should continue sampling counterfactuals even after E1/E2 have committed to execution.

## Limitations

This is a review of computational models rather than direct empirical evidence of multi-loop conflict resolution. The WTA/soft-max distinction is framed around a single loop's dynamics, not the interaction between loops with incommensurable error signals. REE's three loops differ in what they optimise (sensory prediction accuracy, motor efficiency, harm avoidance), not merely in timescale -- the Morita et al. framework does not address incommensurability. The paper predates much of the circuit-level optogenetic work (e.g., Lee & Sabatini 2021) that provides direct causal evidence.

## Confidence reasoning

I rate this 0.68. The WTA/soft-max dual-mechanism framework is the most precisely articulated computational account of the action selection problem that Q-016 needs to address, and it directly raises the question of which regime is appropriate for which loop. The mixed evidence direction reflects that the paper describes the tradeoffs without resolving which policy prevents coupling collapse in a multi-loop conflict -- that resolution is what REE still needs to work out.
