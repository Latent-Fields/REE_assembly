# Zhang and Lewis-Peacock (2026) - Working memory constraints on replanning following distraction

**Claim tested:** Q-077 - is SD-046's multi-slot GoalState a set of discrete fixed-capacity slots, a flexible shared resource, or an emergent competition process?

**Primary source:** Zhang, Z. and Lewis-Peacock, J. A. (2026). *Working memory constraints on replanning following distraction*. Communications Psychology. DOI: [10.1038/s44271-026-00497-6](https://doi.org/10.1038/s44271-026-00497-6). The paper reports data and analysis scripts on OSF: <https://osf.io/6ac5m/files/osfstorage>. Secondary trigger was the Medical Xpress article ["Working memory rapidly updates its priorities after distractions, study finds"](https://medicalxpress.com/news/2026-07-memory-rapidly-priorities-distractions.html).

## What the study did

The authors built a Snake-like working-memory task in which human participants briefly encoded 1, 2, or 4 hidden apple locations, then navigated an agent to collect them. Half the trials inserted an unexpected grape-collection phase before apple retrieval, shifting the agent's position and forcing replanning before the hidden targets could be collected. Participants could press a reminder key to reveal remaining apple locations at a point cost, which made resampling from the environment observable rather than inferred.

The design is unusually close to the REE concern that triggered the email: a moving agent must maintain task-relevant targets while a reward-bearing interruption pulls it away from its prior route, then resume a coherent task from a new state. It is not just passive perceptual distraction.

## Main findings

Without distraction, participants showed a proximity policy: they tended to collect the remembered target nearest the agent's current position first. After distraction, participants did not simply reinstate the original route. They reprioritized remembered targets relative to the agent's updated position.

This flexibility was constrained. At memory load 2, proximity-based replanning after distraction was close to intact. At memory load 4, distraction weakened proximity bias, increased errors/reminder use, and made performance more dependent on resampling. Experiment 2 varied distraction duration unpredictably; longer distractions further reduced high-load replanning efficiency, ruling out a simple precomputed-route explanation.

The most important Q-077 detail is the first-item bottleneck: after distraction, memory-based updating was primarily visible for the first target collected. For later targets, participants leaned more on reminder-based resampling. This looks less like four independently durable active slots and more like a small focus-of-attention riding on top of a broader, noisier maintained/resampled set.

## REE interpretation

This entry strengthens the part of Q-077 that says "the acted-on goal draws disproportionate fidelity", but it does not settle slot versus resource. A clean REE translation is:

- The currently actionable goal/target should receive a state-dependent priority boost keyed to the agent's updated position or task state.
- Higher load should degrade replanning gracefully and increase resampling, rather than causing only an all-or-none failure at a fixed slot boundary.
- A multi-goal substrate should distinguish "maintained somewhere" from "currently manipulable for action", because the source study shows participants can remember/resample multiple targets while actively replanning mainly around one immediate target.

For SD-046, this is design pressure against treating all slots as equally active and equally manipulable after a perturbation. The more faithful form is either a resource/precision allocation model or Johnson et al.'s process-level dynamic-field framing: several goal traces may coexist, but the near/actionable trace receives the effective precision and action-control authority.

For the user's "stay on task and return after distraction" framing, the paper supports a concrete failure mode: the agent should not only preserve a goal token through hazard/benefit interruptions; it must re-rank the preserved goals after the interruption according to the new state. Merely keeping `z_goal` alive is insufficient if the post-distraction priority order is stale.

## Boundaries and caveats

The study is behavioral, not neural, and uses undergraduate human participants in a lab game. It does not identify a PFC, hippocampal, or basal-ganglia substrate. It also inserted distractions before memory-guided apple retrieval, leaving open whether the same pattern holds when an already-running memory-guided action is interrupted mid-execution. Trial exclusions were large in distraction trials because participants sometimes collected hidden targets before completing the distraction phase, so the cleanest analysis is conditional on following the task structure.

This therefore should not promote, demote, or directly edit MECH-116, SD-033a, MECH-262, or SD-046. It is a Q-077 literature update and a future SD-046 design constraint: representational capacity, active focus, and environmental resampling must be measured separately.
