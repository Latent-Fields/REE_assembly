Status: unprocessed

# MECH-071: Why All Goal-Persist Experiments Are Non-Contributory

Date: 2026-03-24

## The Core Problem

EXQ-085 through EXQ-085d have all failed at the same bottleneck: z_goal_norm < 0.1 (often ~0.013
or 0.000). The goal latent is never seeded. This is not a falsification of MECH-071 (harm eval
calibration gradient asymmetry / benefit signal encoding). It means the experimental apparatus
cannot produce valid evidence either way.

The reason: random-walk warmup does not generate the conditions under which goal representations
form. A goal is a persistent, drive-modulated representation of a future state that has been
repeatedly paired with drive-reduction (reward/benefit). Without:
  (1) A homeostatic drive that accumulates between satisfactions
  (2) Repeated cycles of drive-buildup -> goal-proximity -> drive-reduction
  (3) Sufficient temporal spacing to allow z_goal to form through gradient accumulation

...the z_goal latent simply has no signal to latch onto. Random walk with no hunger means food
resources are encountered but carry no motivational salience differential.

## All Prior Experiments Are Non-Contributory

This means EXQ-085 through EXQ-085d should be treated as infrastructure-failure runs, not
as weak evidence against MECH-071. They cannot support OR falsify MECH-071 because the
mechanism was never instantiated.

The governance evidence record should reflect this: these experiments have outcome=FAIL but
the fail reason is "mechanism not instantiated" not "mechanism tested and found absent."

Suggested action: mark all v3_exq_085* manifests with evidence_direction_note explaining
non-contributory status. Do not let them weight MECH-071's confidence score.

## What Is Actually Required

### 1. Homeostatic Drive (Hunger)

The environment needs an energy level that depletes over time. Resources restore energy.
Drive = max_energy - current_energy. This creates a real motivational signal that scales
benefit salience.

Without drive, encountering a food resource is always equally rewarding (or not rewarding
at all if the benefit signal is weak). With drive, hungry agents find food highly salient;
sated agents find it less salient. This is Hull's drive-reduction theory (1943) and
directly motivates Berridge's incentive salience / "wanting" vs "liking" dissociation
(Berridge & Robinson 1998; Berridge 2007, Nature Reviews Neuroscience).

### 2. Oscillatory Exposure Schedule

Goals form through repeated cycles. A single encounter with food is not enough to form
a persistent goal representation. The agent needs:
  - Episode 1: hungry -> finds food -> satisfied -> goal representation begins
  - Episode 2-N: hunger returns -> food memory activates -> z_goal strengthens
  - Eventually: z_goal is a stable predictor of benefit-restoration

This is consistent with:
  - Balleine & Dickinson (1998) goal-directed vs habitual action -- goal representations
    require outcome-devaluation sensitivity, which takes multiple learning cycles
  - Schultz et al. (1997) dopamine prediction errors -- reward-predictive representations
    form over many trials of pairing
  - Oudeyer & Kaplan (2007) intrinsic motivation -- goal salience emerges from learning
    progress, not single exposures

### 3. Curriculum / Developmental Schedule

Early in training, goals should be simple and obvious:
  - Phase 1: large energy depletion, resources placed near spawn -> guaranteed encounters
  - Phase 2: moderate depletion, resources at medium distance
  - Phase 3: natural exploration with full drive dynamics

This is standard curriculum learning (Bengio et al. 2009 ICML). Without it, the agent
spends most of warmup in a low-drive state where goal learning signals are weak.

### 4. Goal Seeding via Drive-Modulated Reward

The loss for z_goal must be:
  loss_goal = -drive_level * benefit_signal * z_goal_norm

When drive is high and benefit is encountered, z_goal gets a strong gradient.
When drive is low, z_goal gets a weak gradient even if benefit is encountered.

This is the mechanistic link between homeostatic drive and goal representation formation.

## Architectural Changes Required

Before MECH-071 can be tested experimentally:

A. **CausalGridWorldV2 extension (or new V3WorldWithDrive)**:
   - Add energy: float state variable (starts at max_energy)
   - Energy depletes at rate `depletion_rate` per step
   - Resource encounter restores energy by `resource_value`
   - Emit drive_level = (max_energy - energy) / max_energy in body_obs
   - Benefit signal = drive_level * resource_collected (drive-modulated reward)

B. **REEAgent z_goal latent**:
   - GoalState should receive benefit_signal * drive_level as its update signal
   - Not a simple count of benefit events -- needs drive weighting

C. **Warmup curriculum**:
   - First N episodes: forced resource placement within 3 cells of spawn
   - After N: normal random placement
   - This guarantees early drive-reduction cycles without biasing eval policy

## Literature Pulls Needed

Priority literature to process before designing EXQ-085e:

1. Berridge & Robinson (1998) "What is the role of dopamine in reward: hedonic impact,
   reward learning, or incentive salience?" -- incentive salience/wanting mechanism.
   Directly maps to drive-modulated z_goal.

2. Balleine & Dickinson (1998) "Goal-directed instrumental action: contingency and
   incentive learning and their cortical substrates." -- how goal representations
   distinguish from habits; devaluation sensitivity test.

3. Bengio et al. (2009) "Curriculum Learning" ICML -- formal justification for
   ordered training schedule.

4. Sutton & Barto (2018) Ch. 17 "Frontiers" -- options framework and temporal
   abstraction; z_goal as a temporally extended option initiation condition.

5. O'Keefe & Nadel (1978) / Moser et al. (2008) -- place cells as goal representations;
   z_goal analogy as a "goal place field" in latent space.

6. Dayan & Daw (2008) "Decision theory, reinforcement learning, and the brain" --
   model-based vs model-free; goal-directed requires a model (consistent with REE's
   E2 forward model as goal-prediction mechanism).

7. Hull (1943) "Principles of Behavior" -- drive reduction theory; hunger as motivating
   condition for goal learning. Historical grounding for the drive-modulated architecture.

## Conclusion

MECH-071 is on hold pending architectural redesign. The claim itself (that harm signals
produce stronger gradient asymmetry than benefit signals, and that benefit salience
requires drive-modulation to match harm salience) is plausible and has neuroscientific
grounding. It simply cannot be tested in the current substrate.

The right framing: MECH-071 is a prediction about what will happen AFTER the drive
architecture is in place. It is a claim about differential calibration gradient magnitude
under homeostatic conditions, not about random-walk benefit encounter rates.

Next experiment (EXQ-085e) should not be designed until:
  (a) CausalGridWorldV2 has energy/drive dynamics
  (b) GoalState update is drive-weighted
  (c) Warmup curriculum guarantees early drive-reduction cycles
  (d) Literature pulls 1-4 above are processed
