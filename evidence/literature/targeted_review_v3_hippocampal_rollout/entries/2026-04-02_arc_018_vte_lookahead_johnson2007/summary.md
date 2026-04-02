# Johnson & Redish (2007) — CA3 Sweeps Forward at Decision Points: The Neural Substrate of ARC-018 Rollout

**Claims tested:** ARC-018, MECH-033
**Evidence direction:** supports | **Confidence:** 0.82

---

## What the paper did

Johnson and Redish recorded from CA3 tetrode arrays in rats navigating a multiple-T-maze with rewards at both ends. The key innovation was Bayesian position reconstruction from neural ensemble firing, applied to short time windows (250ms) coinciding with the periods when rats paused at choice points and looked alternately down each arm — the behavioral signature of vicarious trial and error (VTE). The question: what does the CA3 ensemble encode during these pauses?

The answer was striking: the reconstructed position swept ahead, down one arm of the maze and then the other, representing positions 10-30cm forward of the animal's actual location. These forward sweeps were transient, occurring specifically at choice points rather than during continuous running, and they preferentially represented future trajectories rather than recently-visited paths. This is the neural substrate of the planning behavior Tolman observed decades earlier and termed VTE.

## Key findings relevant to ARC-018

ARC-018 claims that hippocampus performs counterfactual trajectory construction at commitment boundaries. Johnson & Redish provide the cellular-level evidence for this at choice points — the biological analogue of REE's commitment boundary. At the moment the animal must choose, CA3 activity sweeps through the possible future trajectories in sequence, representing each one briefly before the commitment is resolved. This is not a memory retrieval event; it is a prospective simulation.

Several details strengthen the REE mapping:

- The sweeps occur specifically during **pausing behavior at choice points** — matching ARC-018's claim that rollout is triggered at commitment boundaries, not during ongoing execution.
- The sweeps represent **paths forward, not backward** — prospective, not retrospective, consistent with ARC-018's trajectory proposal function.
- The sweeps are **transient and sequential** — first one arm, then the other — which is consistent with the serial evaluation of candidate trajectories in MECH-033's rollout architecture.
- The frequency and organization of sweeps correlates with VTE behavior, which in turn correlates with task performance — suggesting the sweeps are functional (used for decision-making) not epiphenomenal.

## REE translation and MECH-033

For MECH-033 (E2 kernel → hippocampal rollout interface), the forward sweeps in CA3 show trajectory chaining in real time during theta. Each theta cycle compresses a segment of future path into a sequential replay — the chaining is implemented by CA3's autoassociative dynamics, seeded by entorhinal cortex inputs that encode the available transitions from the current state. In REE, the EC inputs are the E2 forward-prediction kernels (`f(z_t, a) → z_{t+1}`), and the CA3 autoassociative chain produces the multi-step trajectory rollout that MECH-033 describes. The distinction in REE is that E2 kernels operate on action-consequence objects (z_world coordinates), not raw spatial positions — but the chaining mechanism is the same.

## Limitations

Spatial T-maze; the forward sweeps encode locations, not abstract action consequences. The mapping to ARC-018's z_world action-consequence rollout requires inference about what the non-spatial analogue of the CA3 trajectory sweep would look like. The sweeps are sometimes incomplete or ambiguous, and the algorithm for resolving competitive trajectories (how the animal chooses between the two arm-representations) is not specified — this is the gap that E3's commitment mechanism fills in REE. More recent work (Pfeiffer 2020, Dragoi & Tonegawa 2011, already in this evidence set) has extended and replicated the basic finding.
