# Yaghoubi et al. 2026 -- Predictive coding of reward in the hippocampus

## What the paper did

Yaghoubi and colleagues (2026) tracked the evolution of hippocampal neural representations over weeks as mice learned to solve a cognitively demanding reward-based navigation task. Using in-vivo electrophysiology and calcium imaging in CA1, they monitored how individual neurons' temporal firing profiles changed across the learning arc. They also constructed a temporal difference computational model of place field dynamics to test whether TD learning principles could explain the observed representational shifts.

## Key findings

As mice learned the task, hippocampal neurons systematically shifted their activity backward in time: cells that initially fired at the reward location gradually began firing earlier in the trajectory, eventually encoding events that preceded the reward rather than the reward itself. The representation of reward in hippocampal neurons decreased over training while representation of reward-predicting environmental events increased. Individual neurons showed this temporal displacement, not just population averages. A TD model of place field evolution replicated the observed pattern, suggesting the hippocampus operates as an evolving predictive map that continually updates its representation to encode the earliest reliable predictor of upcoming outcomes.

## REE translation

SD-023 and MECH-216 together argue that Landmark B provides E1 with a distal predictive signal that should fire BEFORE resource proximity rises. Yaghoubi et al. (2026) provides the strongest contemporary biological evidence for this principle: hippocampal neurons (the biological analogue of E1's world model) develop temporally shifted predictive representations given appropriate environmental structure. Critically, this shift requires that distal predictive cues exist in the environment -- without Landmark B (or its biological equivalent), there is nothing for the representation to shift backward to. The paper directly implies that environmental richness enabling distal-cue representation is necessary for hippocampal predictive coding to develop. This is the functional argument for SD-023: Landmark B creates the environmental condition under which E1's LSTM can develop anticipatory predictive states analogous to the hippocampal shift observed here.

## Limitations

The temporal shift in Yaghoubi et al. (2026) depends on repeated, consistent trajectories approaching the reward site. In CausalGridWorldV2, if the agent does not develop consistent routes via Landmark B's gradient zone, the analogous temporal prediction shift may not emerge. The paper addresses reward-linked place cells specifically; SD-023's Landmark B is a non-reward landmark near resources -- if the agent does not strongly couple goal states to resource proximity, the predictive shift may be attenuated. The paper is very recent (January 2026) and independent replication is pending.

## Confidence reasoning

High source quality (Nature, multi-lab, computational model validation). Mapping fidelity is high for the MECH-216 component of SD-023: the specific claim that hippocampus-as-predictive-map develops distal-cue representations given structured environments is directly what SD-023 requires architecturally. Transfer risk is moderate due to biological hippocampus vs. LSTM and reward vs. resource-proximity prediction.
