# Summary: Schultze-Kraft et al. (2016) — The Point of No Return

**Source:** Schultze-Kraft M, Birman D, Rusconi M, et al. The point of no return in vetoing self-initiated movements. *PNAS*, 113(4), 1080-1085.

## The Question They Were Asking

The readiness potential (RP) begins to rise up to a second or more before a voluntary movement is executed. The question Schultze-Kraft and colleagues posed was not simply whether this preparatory signal exists, but whether — once it is underway — the agent can still cancel the action. Is the RP a passive indicator of an already-determined trajectory, or does it represent a process that remains genuinely interruptible up until some point? To probe this, they built a brain-computer interface that decoded the RP in real-time from EEG and delivered a visual stop signal to participants who were trying to earn points by pressing a button before the BCI could detect them. The design is elegant in a slightly vertiginous way: the BCI is essentially converting the agent's own preparatory brain signal into a challenge that the agent then tries to overcome.

## What They Found

Participants could veto the movement — but only if the stop signal arrived before approximately 200 milliseconds prior to movement onset. Earlier signals were catchable; later signals were not. The 200 ms boundary is empirically measured, not assumed: it is the point at which the probability of successful cancellation drops to chance. Crucially, this boundary falls well after the onset of the RP itself — preparation can be underway for hundreds of milliseconds and still be reversible. But there is a specific, temporally sharp moment after which the motor command is no longer subject to voluntary interruption.

## Why This Matters for MECH-061

MECH-061 claims that a commit-boundary token reclassifies which error channel is operative: before the boundary, errors are pre-commit predictions subject to deliberative updating; after it, errors are realized post-commit outcomes that update policy rather than revise the current plan. Schultze-Kraft et al. provide what is perhaps the cleanest behavioral demonstration that this boundary is real, temporally measurable, and genuinely discrete in character — not simply a gradual fade from revisability to irreversibility. The point of no return is sharp. That sharpness is load-bearing for the MECH-061 architecture: a token semantics requires a transition, and this paper demonstrates the transition exists.

The limitation worth acknowledging is that the paper identifies *when* the boundary lies without characterizing *what* the boundary does to error signals downstream. We observe that veto becomes impossible after the point of no return; we do not observe what the nervous system does differently with outcome information in the post-boundary regime compared with the pre-boundary regime. MECH-061 requires both: the boundary event itself, and the reclassification of error channels that follows it. Schultze-Kraft et al. supply strong evidence for the first and leave the second as a standing question.

## Honest Uncertainty

There is a reasonable concern about generalization. The action here is a wrist movement; the commitment is motor and happens in under a second. REE's commit boundary is intended to operate over harm-attribution decisions that may unfold across many seconds, involve complex counterfactual reasoning, and culminate in social or ethical consequences rather than a button press. Whether the same sharp-boundary topology holds at that level of abstraction is not demonstrated. One could imagine that for complex high-stakes decisions, the point of no return is not a single moment but a gradual narrowing of the option space — in which case the token metaphor is approximate rather than literal. That said, the existence of any sharp boundary in any voluntary action system is encouraging: it shows that the nervous system is capable of implementing commitment as a categorical event, not merely as a continuous shift in probability.
