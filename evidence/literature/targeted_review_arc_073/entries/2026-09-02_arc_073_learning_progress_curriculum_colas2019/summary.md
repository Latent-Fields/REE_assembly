# Colas et al. (2019) -- CURIOUS: Intrinsically Motivated Modular Multi-Goal Reinforcement Learning

*Entry for ARC-073: play-to-real transition is triggered by competence saturation or drive pressure, not by scheduled duration.*

## What the paper did

CURIOUS is an autotelic agent for a modular multi-goal setting (a simulated Fetch arm with several kinds of goal). It combines a modular Universal Value Function Approximator with hindsight learning, so one policy can pursue heterogeneous goals, and an automatic curriculum that biases goal selection toward the module with the highest *absolute* learning progress, estimated over a sliding window and sampled epsilon-greedily. The reported behaviour is that the agent focuses on achievable goals first, ignores goal spaces it cannot make progress on -- including deliberately inserted impossible and distracting modules -- and returns to goals whose competence has decayed.

This is the closest computational instantiation available of the signal ARC-073 proposes to use, and it comes from the Oudeyer line the claim's own notes cite.

## The half this supports

ARC-073 needs learning progress to be a *usable* quantity: computable online, discriminative between "mastered", "unlearnable", and "still yielding", and robust enough to steer behaviour on. CURIOUS demonstrates all three. LP over a sliding window separates the three regimes well enough that the agent avoids the classic failure of naive curiosity -- being captured by a high-entropy region it can never predict -- and outperforms a uniform curriculum. That is direct support for the implementation note in ARC-073's claim text: monitoring a rolling LP estimate during play, parameterised in GoalConfig, is a real design that works in a real system.

## The half this complicates, which I think is the more important finding

CURIOUS uses *absolute* learning progress, and the choice is deliberate. A module whose performance is decaying has negative signed LP and high absolute LP, and the agent re-selects it. Saturation in this architecture is a local, reversible, per-region state -- not a terminal one. The agent that has stopped learning about a goal region has not finished with that region; it will come back when forgetting makes the region productive again.

ARC-073 reads |d(PE)/dt| < threshold across all reachable regions as an exit condition. If saturation is reversible in the way CURIOUS shows it to be, that test can fire on a transient plateau and close a play episode that would shortly have resumed producing world-model learning. And because LP is estimated over a finite window, the test is a statistical decision with a false-positive rate the claim does not currently specify. Setting `play_lp_saturation_threshold` is therefore not choosing a number; it is choosing an operating point on a detection curve, and the Baarendse entry in this directory argues the two error directions are not equally cheap.

There is also a plain absence to record. CURIOUS never exits exploration. There is no non-exploratory mode to transition into, and the paper contains no mechanism for terminating the curriculum. The half of ARC-073 that says "and then the agent leaves play" has no instantiation in the work it is most naturally read as resting on. That is not evidence against it -- it is a gap, and it is why this entry is `mixed` rather than `supports`.

## Limitations

Simulation only, in a robotic manipulation environment with a small hand-specified module set. Nothing here about embodiment, homeostatic drive, or an agent with a real task waiting for it. The "reachable PE regions" quantifier in ARC-073 has no counterpart: CURIOUS's goal modules are given by the designer, whereas REE would have to define what the reachable set *is* at the moment the exit test is applied, and a test quantified over a set the agent computes is a different and harder proposition than a test over a set the designer wrote down.

## Confidence

0.62. High relevance and low transfer risk -- this is an artificial agent transferring to another artificial agent, so the usual animal-to-machine hazard does not apply. The binding constraint is mapping fidelity: the paper gives ARC-073 the signal it wants and is silent-to-negative on the decision ARC-073 makes with that signal. Anyone citing Forestier/Oudeyer-lineage work as settling ARC-073's transition criterion is citing support for the wrong half.
