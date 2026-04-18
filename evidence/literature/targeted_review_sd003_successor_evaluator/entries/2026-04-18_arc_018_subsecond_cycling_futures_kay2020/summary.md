# Kay, Chung, Sosa, Schor, Karlsson, Larkin, Liu, Frank (2020). Constant Sub-second Cycling between Representations of Possible Futures in the Hippocampus. *Cell*.

## What the paper does

Kay and colleagues recorded from large CA1 populations in rats running a T-maze and asked a very specific question: when an animal is approaching a choice point, is the hippocampus already representing the possible futures -- and if so, how? Earlier work (Johnson & Redish 2007, vicarious trial-and-error; Pfeiffer & Foster 2013, preplay) had established that CA1 *could* represent future trajectories at decision points. The Kay paper tightens this into something quantitative. Using Bayesian decoding, they ask, cycle by cycle, which future is being represented, and they do it across the entire approach, not just at the explicit choice.

## Findings

The answer is sharper than the prior literature had suggested. CA1 alternates between coherent representations of the two mutually exclusive future arms on successive theta cycles -- roughly 8 Hz, so about 125 ms per future. The alternation is constant: it happens throughout the approach, not only at the choice point, and it does not require the animal to stop or show behavioural hesitation. Each theta cycle, CA1 is running one rollout of one candidate future; on the next cycle, it is running the other. This is, in the authors' phrasing, a deliberative process running at sub-second resolution, continuously, as the default mode of the hippocampus during goal-directed approach.

A second observation matters for our question. The fidelity of the represented trajectory -- how cleanly CA1 decodes to the arm being represented -- predicts the eventual choice on the fly. That is, the representation is not just existing; it is scaled or weighted in a way that correlates with what the animal will do next. The authors are careful not to overclaim that this *is* the value signal. But the signal behaves the way a rollout feeding an evaluator should behave.

## REE mapping

For ARC-018 and MECH-033, this is close to the best single piece of empirical evidence available. ARC-018 commits REE to hippocampal rollout generation; the Kay paper shows CA1 is doing exactly that, at sub-second cadence, on every traversal. MECH-033 commits REE to E2-forward-prediction kernels being chained into rollouts; the theta-cycle rollouts here are effectively the neural implementation of that chaining, each cycle constituting one kernel application. For the SD-003-successor question -- is evaluator architecture the same as comparator architecture? -- this paper is pointing firmly toward "different": the Kay cycling is pre-action forward-model use, and it is plainly a different operation from post-action attribution (the subtraction of actual vs counterfactual outcomes that Frith-family comparator models propose).

## Where the mapping is imperfect

The Kay paper measures the rollouts; it does not measure their scoring. The inference that CA1 cycling constitutes an evaluator depends on readout circuitry (mPFC, OFC, vStriatum) that is not recorded here. It is also worth naming that the trajectories at issue are spatial, not moral. The REE claim (ARC-033) is that the harm stream needs its own E2_harm_s forward model separate from E2.world_forward. Kay et al. do not speak to whether the biological rollout circuit is single-stream or multi-stream; they demonstrate only that CA1 cycles through spatial futures. If REE's stream separation holds, the Kay result tells us what the world-forward rollout half looks like but is silent about the harm-forward half.

## Confidence reasoning

Source quality is very high -- Cell, Frank lab, methodologically strong. Mapping fidelity to ARC-018 is about as direct as literature-to-architecture ever gets; to MECH-033 it is slightly softer (the paper does not label cycles as E2-kernel applications -- that framing is REE's). Transfer risk is real but moderate: spatial navigation is not harm proximity, and the measured signal is the rollout not its evaluation. Confidence 0.80. Together with Pezzulo et al. 2014, this is the strongest pair of biological anchors for the evaluator mode of the SD-003 successor.
