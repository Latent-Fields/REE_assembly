Status: processed

Processed in:
- `docs/architecture/three_loop_learning_channels.md` (ARC-021, MECH-069, MECH-070)
- `docs/claims/claims.yaml` (ARC-021, MECH-069, MECH-070 registered 2026-03-14)

---

## Three BG-like systems, three distinct error signals

Hypothesis: the three cortico-striatal loops that appear to map onto REE are not just structurally distinct — they train on fundamentally different error signals. Each system's learning rule is defined by *what kind of mismatch it cares about*.

### The three systems

**1. Sensorium**
- Trains on: sensory prediction error — predicted sensory state vs. observed sensory state.
- REE mapping: E1 (`compute_prediction_loss`), operating on the latent stream, no action conditioning.
- BG loop: limbic/beta-associated sensorium loop; reticular thalamus; attentional selection of what enters the system.
- Characteristic: slow, continuous, not gated by action. E1's role is to maintain a running "perceived present" — the world as it should appear given current context. Its error signal is purely sensory mismatch.

**2. Action enacting**
- Trains on: expected motor effect error — predicted effect of an action on the *conceptual sensorium* vs. actual effect.
- REE mapping: E2 (`compute_e2_loss`), operating on `z_gamma` — the unified latent space of all sensory modalities, where coherent objects form. NOT on raw sensory streams.
- BG loop: sensorimotor loop; E2 is cerebellum-like — predicts `f(z_t, a_t) → z_{t+1}` and learns from the discrepancy.
- Characteristic: The "conceptual sensorium" (`z_gamma`) is the key distinction from E1. E2 doesn't predict raw sensation — it predicts how actions transform latent sensory *objects*. This is the level where "I grabbed the cup" is represented, not "there is a red patch at coordinates (x, y)." The error signal is motor-sensory: what I expected my action to do vs. what it actually did at the level of coherent objects.
- This means E2's planning horizon should exceed E1's: E1 predicts the perceived present a short way ahead; E2 predicts the full causal chain of a motor act on the object world, which unfolds over a longer interval.

**3. Planning gates**
- Trains on: harm and goal errors — realized harm vs. expected harm, goal achievement vs. goal deviation.
- REE mapping: E3 (REINFORCE on `-(harm_signal)`) and HippocampalModule (terrain-navigated trajectory proposal under residue geometry).
- BG loop: associative/thought loop; mediodorsal thalamus; hippocampal-mPFC episodic future projection.
- Characteristic: The planning system doesn't care about sensory prediction error or motor prediction error directly. It cares about whether trajectories avoid harm and achieve goals. Its error signal is outcome-level: the residue field accumulates harm signal across trajectories; E3 precision modulates how hard the gate closes based on realized vs. anticipated harm.

### Why this matters architecturally

The three systems are not just separated for computational efficiency. Their error signals are *incommensurable* — you cannot derive sensory prediction error from motor prediction error, nor either of those from harm/goal error. Collapsing them into a single prediction error (as a naive JEPA or world-model architecture might) would conflate:
- "I failed to predict the world" (E1)
- "My action had a different effect than expected" (E2)
- "That effect was harmful / failed to achieve the goal" (E3)

These require different credit assignment, different learning rates, and different write boundaries. MECH-058 (E1/E2 timescale separation) and MECH-057 (action loop completion gating) are both downstream of this deeper separation principle.

### Relation to Q-019

Q-019 asks whether the BG implements one gate (evaluate all criteria at once) or three gates (three anatomically distinct loops). This hypothesis presupposes the three-gate model (Q-019 model B) and adds the specific learning signal for each gate. It is not contingent on the anatomical question — even if the gates share substrate, their *training objectives are distinct*.

### Relation to existing REE claims

- **MECH-033** (E2 kernel → hippocampal rollout interface): this hypothesis grounds *why* E2 and the planning system are distinct — different error signals, not just different timescales.
- **MECH-058** (E1/E2 timescale separation): the timescale difference is a *consequence* of the error signal difference. E1 error is continuous and fast to correct (sensory mismatch is small and frequent). E2 error is slower — motor-sensory transitions are sparse and consequences take time to manifest. Planning errors are slowest — harm/goal signal only arrives after full trajectory execution.
- **SD-003** (self-attribution via counterfactual E2): E2's error signal (`z_actual_t+1 - z_predicted_t+1`) is the natural substrate for self-attribution. If `E2(z_t, a_actual) ≈ E2(z_t, a_counterfactual)`, the action was not causally responsible for the outcome. The gap between actual and counterfactual E2 prediction *is* the agent's causal signature on the object world.

### Hypothesis status

Candidate for promotion to a new claim (MECH-06x or ARC-0xx). Suggest registering as either:
- An extension of Q-019 (answering model B's learning rules)
- A new architectural commitment: "The three cortico-striatal learning loops require distinct error signals; conflation degrades all three."

The code already implements this separation (separate `compute_prediction_loss`, `compute_e2_loss`, and REINFORCE return signal). The hypothesis gives it principled grounding.
