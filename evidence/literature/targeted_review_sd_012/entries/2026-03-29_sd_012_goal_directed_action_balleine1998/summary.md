# Balleine and Dickinson (1998) -- Goal-directed instrumental action: contingency and incentive learning and their cortical substrates

**Claim tested:** SD-012 (z_goal seeding requires drive-scaled benefit signals)

## What the paper did

Balleine and Dickinson addressed one of the central puzzles in animal learning: why does knowing that an action produces a reward not guarantee that the animal will perform that action? Their answer is that goal-directed action requires two separable forms of learning: contingency learning (the action causes this outcome) and incentive learning (this outcome has this current value given my current motivational state). The paper uses a combination of specific satiety devaluation experiments and insular cortex lesion studies to dissect these two learning processes. In the key experiments, rats trained on two actions for distinct food outcomes are sated on one food before a choice test in extinction. Sated animals preferentially avoid the action that earned the now-devalued food -- demonstrating that current motivational state modulates performance even when both actions are known. Insular cortex lesions selectively impair this incentive learning component, leaving contingency learning intact.

## Key findings relevant to SD-012

The incentive learning mechanism is the critical finding for SD-012. Balleine and Dickinson demonstrate that the motivational value of an outcome is not stored as a fixed property learned during training -- it must be retrieved and updated based on current homeostatic state at the time of performance. The insular cortex is required for this updating: without it, animals cannot integrate current drive state with remembered cue-outcome associations to produce a current incentive value. They continue to pursue outcomes that they would avoid if their insular cortex were intact and able to compute: "I am sated; this outcome is currently not valuable; I will not pursue the action that leads to it."

For SD-012, the lesson is that benefit signals must be computed relative to current drive state, not stored as fixed values. An agent that learned during training when it was hungry and never updates those values to reflect current satiety would be incorrectly motivated -- it would pursue resources when sated (too much motivation) and might not correctly weight resource encounters during training (too little amplification). SD-012's drive-scaling formula is architecturally equivalent to the incentive learning mechanism: effective_benefit at time t = benefit_exposure * (1.0 + drive_weight * drive_level_t). This is the agent computing its current incentive value for the resource outcome by multiplying nominal value by current motivational state.

## REE translation

SD-012's design decision translates directly from Balleine and Dickinson's incentive learning framework. The insular cortex's role in Balleine and Dickinson -- integrating drive state with learned cue-outcome value to produce current incentive value -- is implemented in SD-012 as the drive_level scaling term. Without this integration, the agent learns that resources are beneficial but cannot scale that benefit signal by current need, leading to benefit_exposure that accumulates too slowly during high-drive states (when the agent most needs to form goal representations) and too quickly during low-drive states (when goal formation is less relevant). The SD-012 formula ensures that z_goal formation is most likely when drive is high -- when the agent is most in need of goal direction -- which is the adaptive property that Balleine and Dickinson's incentive learning mechanism provides biologically.

## Limitations and caveats

The insular cortex lesion model is a radical intervention that removes a specific brain region involved in interoceptive processing and taste learning. There is no architectural equivalent of the insular cortex in REE -- SD-012 implements drive scaling as an explicit formula in GoalState.update(), not as an emergent property of a distinct module. The Balleine and Dickinson paradigm uses specific satiety (consuming one food to the point of aversion) as its drive manipulation, which is a more drastic state change than the gradual energy decay in CausalGridWorld. The paper's primary contribution is demonstrating the dissociability of contingency learning and incentive learning, not directly demonstrating drive-level scaling of benefit signals -- that inference requires the additional step of recognising that incentive learning is the mechanism by which drive state modulates outcome value.

## Confidence reasoning

Confidence is 0.80. Landmark paper with rigorous behavioral and lesion data. The incentive learning concept provides direct theoretical grounding for SD-012's drive-scaling mechanism. Mapping is good but requires one inferential step (from incentive learning as drive-state updating to linear drive-level scaling formula).
