# Thought Intake: Epistemic Self-Monitoring, D_eff Gating, and Hippocampal Self-Navigation

**Date:** 2026-03-23
**Session type:** Design conversation (continuation of 2026-03-22 approach/avoidance session)
**Participants:** Daniel Golden, Claude
**Output:** 4 new claims registered (INV-033, MECH-114, MECH-115, ARC-031)
**Related intake:** evidence/planning/thought_intake_2026-03-22_approach_avoidance_drives.md

---

## Conversation Prompts

While implementing EXQ-072..075 (Q-021/MECH-111/MECH-112/MECH-113 experiments), Daniel
raised two observations about the architecture that were not captured in the prior intake:

> "knowing one is not sure may be very important given REE's foundations"

> "And it would also I think work with mapping one's own thoughts hippocampally, hopefully"

Both observations, unpacked below, point to architectural gaps distinct from the
approach/avoidance symmetry gap registered on 2026-03-22.

---

## Analysis

### Observation 1: Knowing One Is Not Sure

REE's entire foundation rests on predictive processing -- the agent acts on its best
model of the world, and prediction error is the signal that drives learning. This is
well-represented in the current architecture:

- **E3 running_variance** (ARC-016): EMA of E3 prediction error over z_world. Low
  variance = confident world predictions = commit permitted.
- **E1 prediction error**: Drives sensory prior updates (sensorium loop).
- **E2 motor-sensory error**: Drives z_self prediction fidelity (motor loop).

But all of these are **first-order** signals: prediction error about the *world* or
about *self-state transitions*.

What is absent is a **second-order** signal: the agent's uncertainty about its OWN
MODEL'S RELIABILITY. This is a qualitatively different epistemic level.

#### The Problem

Consider: E3 running_variance may be low (world predictions confident) while z_self is
dispersed (D_eff high -- self-model incoherent). The current architecture would permit
commitment in this case, because the commit condition only checks world-side confidence.

But an agent with an incoherent self-model should NOT commit to irreversible actions.
The agent does not know what it is doing. This is not a world-prediction problem --
it is a self-model reliability problem.

The distinction matters because:

1. **World confidence and self-confidence are dissociable.** An agent can have accurate
   world predictions (low E3 running_variance) while having a degraded self-model
   (high D_eff). The two signals are independent.

2. **Commitment involves irreversible self-engagement.** ARC-016 permits commitment when
   the agent can reliably predict world consequences. But it does not check whether the
   agent reliably knows *what it is doing* -- whether its own action-selection is
   coherent enough to be entrusted with irreversible actions.

3. **This is REE's ethical foundation, not an optimization detail.** The architecture
   is meant to model the preconditions for moral responsibility. Acting without a
   coherent self-model is acting without full agency -- which should be reflected in
   the commit gate, not just in post-hoc attribution.

#### The Epistemic-Mapping Connection

Daniel had previously begun work on this in the `epistemic-mapping` repo
(`/Users/dgolden/Documents/GitHub/epistemic-mapping/`). The `Epistemic_monitor.py`
module computes three metrics:

1. **D_eff (participation ratio)** = `(sum|h_i|)^2 / sum(h_i^2)` -- effective
   dimensionality of representation. High D_eff = diffuse/uncertain. Low D_eff =
   coherent/focused. Maps directly to z_self coherence.

2. **Hopfield Memory Stability** -- 64-slot LRU modern Hopfield network; stability =
   max(softmax(beta * similarities)). Measures pattern *familiarity*: high stability =
   current state matches stored self-states = "I've been here before." This is a
   second framing of self-coherence: not dispersion but recognisability.

3. **Entropy of representation** -- Shannon entropy of hidden unit activations.

The combined certainty score used in epistemic-mapping:
  `0.4 * (1 - entropy/10) + 0.3 * (1 - D_eff/hidden_size) + 0.3 * stability`

This is exactly the kind of second-order epistemic signal REE needs for its commit gate.
The three metrics capture related but distinct aspects:
- D_eff: Are the active dimensions focused?
- Stability: Is the current state pattern familiar?
- Entropy: Is the information concentrated or diffuse?

The EXQ-075 experiment (MECH-113) implements D_eff monitoring for self-maintenance.
The next architectural step is to **wire D_eff into the commit gate** -- not just
train a maintenance loss, but use D_eff as a gate condition on commitment.

#### The Structural Invariant

This observation points to a new architectural invariant:

REE agents must have explicit SECOND-ORDER EPISTEMIC ACCESS to their own model
confidence -- not just first-order prediction error monitoring. This access must be:
- Structurally represented (not inferred from performance metrics)
- Available at deliberation time (before action selection, not post-hoc)
- Actionable (wired into commit gate, not just logged)

This is distinct from ARC-016 (which is also second-order in a sense, but over the
world model). The new invariant covers the self-model channel.

#### Connection to REE's Ethical Foundations

The philosophical foundation of REE (Synthese paper, /Users/dgolden/Documents/GitHub/Philosophy/)
frames ethical agency around five axioms and three functional constraints. Constraint 3
(hypothesis tag / MECH-094) already encodes the simulation/real-action distinction.

Knowing-one-is-not-sure is the PRECONDITION for that constraint to be meaningful:
if the agent does not have reliable access to its own epistemic state, the hypothesis
tag itself cannot be reliably issued. A dispersed self-model is one that cannot
clearly distinguish "I am simulating X" from "I am doing X."

This connects MECH-113 (self-maintenance) to MECH-094 (hypothesis tag) in a way
not previously captured: the reliability of the tag depends on z_self coherence.
High D_eff = unreliable tag = PTSD-adjacent state where simulation bleeds into
real-action marking.

---

### Observation 2: Mapping One's Own Thoughts Hippocampally

The current HippocampalModule (SD-004, Q-020 resolved) navigates ACTION-OBJECT space O
-- it generates trajectory proposals through the external world's residue-shaped z_world.
It maps ENVIRONMENT, not SELF.

But the hippocampus does not only navigate spatial environments. The cognitive map
literature (Tolman 1948, O'Keefe & Nadel 1978, Buzsaki & Moser 2013) has progressively
expanded from spatial maps to abstract conceptual maps. Entorhinal grid cells and
hippocampal place cells appear to represent not just spatial location but position in
any continuous abstract space -- including mental/conceptual spaces.

Daniel's observation: the same hippocampal machinery could navigate Z_SELF TRAJECTORY
SPACE -- sequences of self-states constituting deliberation, planning, or rumination.

In REE terms:
- Current: HippocampalModule proposes trajectories through z_world (external action sequences)
- Extended: HippocampalModule could also propose trajectories through z_self (deliberation sequences)

A z_self trajectory = a planned sequence of internal state transitions: "I will first
resolve uncertainty about X (shift from high D_eff to low D_eff in domain X), then
attend to Y, then commit." This is the hippocampal substrate of DELIBERATION PLANNING,
not just action planning.

The E3 evaluation pipeline would then evaluate z_self trajectories for:
- Self-coherence cost (does the deliberation sequence maintain low D_eff throughout?)
- Hypothesis tag integrity cost (does the deliberation not confuse simulation and real?)
- Self-maintenance cost (does the deliberation respect allostatic setpoints?)

This is a V4+ claim: it requires the waking architecture (EXQ-072..075 results) plus
a consolidation mechanism (SWR-equivalent replay of z_self trajectories during offline
integration -- already gestured at in MECH-092 but currently only for z_world).

The connection to ARC-028 (hippocampal→BG completion coupling) is direct: if the
hippocampus generates both external AND internal trajectory proposals, the BG completion
signal fires on BOTH action completion and deliberation completion. The commit threshold
would then govern both kinds of commitment.

#### Biological Basis

Schapiro et al. 2017 (J Cogn Neurosci, DOI 10.1162/jocn_a_01111): hippocampal
representations encode temporal sequences in abstract domains, not just spatial ones.

Milivojevic et al. 2015 (J Neurosci, DOI 10.1523/JNEUROSCI.3603-14.2015): fMRI
evidence for hippocampal coding of narrative/temporal structure in abstract event space.

Behrens et al. 2018 (Neuron, DOI 10.1016/j.neuron.2018.09.040): "What is a cognitive
map? Organizing knowledge for flexible behaviour." Grid/place cell mapping extends to
social cognition and conceptual structure -- the same navigation algorithms map
abstract "thought space."

This would make MECH-113 (self-maintenance) not just a homeostatic signal but a
NAVIGATION PREREQUISITE: you cannot reliably navigate z_self trajectory space if the
self-model is incoherent (high D_eff). The D_eff monitoring is the precondition for
hippocampal self-navigation to be meaningful.

---

## Claims Registered

### INV-033: `epistemic.second_order_self_monitoring`

REE agents require second-order epistemic access to their own model confidence --
explicit structural representation of "how much to trust this self-model" -- available
at deliberation time and wired into commit gating.

**Why this is an invariant and not a mechanism:**
- It is not a specific implementation (D_eff, Hopfield, entropy -- all are candidate
  mechanisms, see MECH-114)
- It is a functional requirement: any REE-conforming architecture must have SOME
  mechanism for second-order self-confidence access
- It is constitutive of the ethical architecture: agents cannot be held responsible
  for actions taken without coherent self-knowledge

### MECH-114: `commit_gate.z_self_d_eff_gate`

D_eff (z_self participation ratio) as a necessary co-condition for commitment, alongside
ARC-016 world-side running_variance.

Current commit condition (ARC-016): `running_variance < commit_threshold`
Extended commit condition (MECH-114): `running_variance < commit_threshold AND d_eff < d_eff_threshold`

Mechanistically: the commit gate AND's two independent signals -- world-side confidence
and self-side coherence. Both must be in range. This prevents commitment when the agent
knows the world well but does not know what it is doing internally.

### MECH-115: `hypothesis_tag.z_self_coherence_dependency`

MECH-094 (hypothesis tag as φ(z) write gate separating simulation from real action)
depends on z_self coherence for its reliability. When z_self is dispersed (high D_eff),
the tag signal becomes unreliable: the distinction between "I am simulating X" and
"I am doing X" blurs at the self-model level.

This is distinct from MECH-094 tag LOSS (the full loss of the gate, modeled as
PTSD/psychosis mechanism). MECH-115 is tag DEGRADATION through self-model incoherence
-- a milder, graded failure mode where the tag does not disappear but becomes unreliable.

### ARC-031: `hippocampal.z_self_trajectory_navigation`

V4 scoped. The HippocampalModule extends to navigate z_self trajectory space (deliberation
sequences -- planned transitions through self-states) in addition to z_world action-object
space O (SD-004). This enables the agent to plan its own deliberation, not just its
actions -- hippocampal mapping of thought rather than environment.

ARC-031 depends on: MECH-113 (D_eff monitoring as navigation precondition), MECH-114
(D_eff commit gate), SD-004 (action-object space already implemented), MECH-092
(offline replay mechanism extended to z_self trajectories).

---

## Architectural Shape

The four claims produce the following additions to the REE wiring diagram:

```
z_self → D_eff monitor (MECH-113)
                  |
                  ├── Self-maintenance loss (existing)
                  |
                  ├── Commit gate co-condition (MECH-114):
                  |     [ARC-016 world_variance < threshold] AND [D_eff < d_eff_threshold]
                  |
                  └── Tag reliability signal (MECH-115):
                        When D_eff high → degrade φ(z) write gate reliability
                        [Implementation: reduce gate confidence, not zero it]

HippocampalModule (V4 extension -- ARC-031):
  Current:  propose_trajectories(z_world, z_self) → action-object space O
  Extended: propose_self_trajectories(z_self) → deliberation space Z_self
                  ↓
  E3 evaluates z_self trajectories for coherence + tag integrity + maintenance costs

INV-033 (invariant -- no specific implementation):
  Any REE-conforming architecture must expose second-order self-confidence
  in a form usable by the commit gate. D_eff is the current candidate mechanism.
  Hopfield stability is a complementary framing (familiarity vs. coherence).
  Combined certainty score from epistemic-mapping (entropy + D_eff + stability)
  is the richer multi-framing implementation.
```

---

## Relation to Prior Claims

| Prior claim | Relation |
|-------------|----------|
| MECH-094 (hypothesis tag) | MECH-115 adds: tag reliability depends on z_self coherence |
| ARC-016 (dynamic precision) | MECH-114 adds: commit gate requires BOTH world_variance AND D_eff |
| MECH-113 (self-maintenance) | MECH-114 wires D_eff monitoring into commit gate (not just loss) |
| SD-004 (action-object space) | ARC-031 extends: z_self trajectory space navigated analogously |
| MECH-092 (offline replay) | ARC-031 extends: offline replay of z_self trajectories |
| INV-032 (approach/avoidance) | INV-033 adds: self-confidence access is also constitutive |
| ARC-028 (hippocampal→BG coupling) | ARC-031: BG completion fires on deliberation completion too |

---

## Implementation Priority

| Claim | Phase | Priority |
|-------|-------|----------|
| MECH-114 (D_eff commit gate) | V3 | Medium -- EXQ-075 is prerequisite |
| MECH-115 (tag coherence dependency) | V3 | Low -- design question, no experiment yet |
| INV-033 (second-order access invariant) | V3 | High (conceptual) -- shapes all above |
| ARC-031 (z_self hippocampal navigation) | V4 | Future -- waking architecture first |

EXQ-075 (MECH-113 D_eff homeostasis) is the immediate prerequisite for MECH-114.
If EXQ-075 PASSes, the next step is to wire the D_eff signal into the commit gate
condition rather than only using it as a training loss.

---

## Open Questions

1. **MECH-114 threshold**: What is the appropriate D_eff commit threshold? EXQ-075
   will provide baseline D_eff values (pre-perturbation) that can calibrate this.

2. **MECH-115 implementation**: How should tag reliability be graded by D_eff?
   Options: (a) smooth gate confidence = sigmoid(-D_eff + target); (b) hard gate:
   tag disabled when D_eff > threshold; (c) precision-weighted tag: tag carries
   a reliability score used downstream.

3. **INV-033 multi-framing**: D_eff (coherence), Hopfield stability (familiarity),
   entropy (concentration) are three candidate implementations of INV-033. Should
   all three be combined (epistemic-mapping combined certainty score) or is one
   sufficient? EXQ-075 tests D_eff alone -- future experiments could add the others.

4. **ARC-031 boundary with SD-004**: SD-004 action-object space maps external
   action-consequence pairs. Z_self trajectory space maps internal state transitions.
   The mathematical structure may be similar (both are sequences over a latent space)
   but the training signal differs: z_self trajectories should be evaluated by
   self-maintenance cost, not harm cost. Need to specify which E3 head evaluates them.
