---
nav_exclude: true
---

# Developmental Curriculum and Staged Training

**Claim Type:** architectural_commitment
**Scope:** Staged training, curriculum gating, developmental ethics
**Depends On:** ARC-005 (control plane), ARC-006 (entities and binding), ARC-007 (hippocampal systems), ARC-013 (residue geometry), INV-010 (offline integration)
**Status:** provisional
**Claim ID:** ARC-019, INV-043, INV-055, INV-056, INV-060, ARC-046, ARC-049, ARC-050, MECH-158, MECH-189, MECH-197, MECH-198, MECH-199
<a id="arc-019"></a>

---

## Rationale

REE ethics and stability are **developmental**: they emerge from how the system is brought up, not from a single
objective or post‑hoc constraint. A staged curriculum is required to avoid brittle convergence, premature collapse,
or unsafe coupling.

This document consolidates the developmental thread implied by Q‑006 and the telemetry rationale in `control_plane.md`.

---

## Architectural Commitment

REE must be trained through **staged development** with explicit gates:

- Each stage introduces a **small set of capacities** and keeps prior capacities stable.
- Stage transitions are **gated by coherence and safety criteria**, not by performance alone.
- Control‑plane settings are **curriculum‑tuned** per stage (precision, volatility, veto thresholds).
- Offline integration (sleep / consolidation) is used **between stages** to stabilize learning.
- Telemetry exposure channels are required for **early diagnostics** before language can report needs.

---

## Infant Stage (INV-055, ARC-046)
<a id="inv-055"></a>
<a id="arc-046"></a>

> **Registered 2026-04-06.** Prior stage to INV-041 childhood. INV-041 presupposes a substrate
> that only the infant stage can build.

### What the Infant Stage Must Accomplish

Before the child phase can begin, the agent must have:
- An initial **valence map**: residue field populated with harm/benefit geography
- A **behavioral repertoire**: E1 prediction model trained on diverse state transitions
- **z_goal representations** seeded from accidental benefit contacts (not deliberate planning)

Without this substrate, childhood's constrained affordances and commitment gating are
meaningless — there is nothing to constrain and nothing to build on.

### Operational Parameters

| Parameter | Infant setting | Purpose |
|-----------|---------------|---------|
| `novelty_bonus_weight` | maximised | MECH-111 drives broad novel-state coverage |
| `commit_threshold` | very high OR `sweep_amplitude=1.0` | Near-random exploration, BreathOscillator always in sweep |
| `offline_integration_frequency` | very low (frequent) | High sleep:wake ratio (INV-051 MEL-driven) |
| `residue_scale_factor` | ~0.1 | Harm felt sensorially but residue does not catastrophically saturate |
| `hazard_magnitude` | reduced | Educative harm gradients without destructive accumulation |
| E3 planning | disabled or near-random | No deliberate trajectory selection until child stage |

### Hazard Protection (ARC-046)

The infant feels harm — z_harm_s and z_harm_a fire normally, training the nociceptive
pathways. But residue accumulation is attenuated (~10% adult rate) and hazard magnitudes
are reduced, so the residue field is populated without catastrophic saturation.

This implements the INV-043 caregiver function "imperfect protection: allow harm-learning
without destruction." In single-agent CausalGridWorld, protection is a curriculum parameter;
in multi-agent environments (ARC-047), an explicit caregiver agent can take on this role.
Protection is progressively removed as the agent transitions to childhood then adulthood.

### Sleep Output

Each offline integration pass during infancy:
- Populates the residue field via `integrate()` (harm/benefit geography)
- Builds z_goal representations from benefit encounters
- Tunes E1 prediction model on diverse transitions

Heavy MEL from novel experience (INV-051) drives high sleep demand. The infant's sleep output
is the curriculum's product — not ethical behaviour, but substrate quality.

### Gate Criterion

Transition to childhood (INV-041) when:
- `z_goal.norm() > infant_goal_threshold`
- Behavioral entropy below ceiling (repertoire established, not pure random walk)

---

## Play-Dominant Childhood (INV-060, MECH-197, MECH-198, MECH-199)
<a id="inv-060"></a>

> **Registered 2026-04-06.** Play dominates the child developmental phase. The type of play
> changes as subsystem competence develops, systematically training architectural components
> in dependency order. See `play_mode.md` for the full play architecture.

### Why Play Dominates Childhood

The infant phase (INV-055) produces a valence map, behavioral repertoire, and initial z_goal
representations. But infancy does not produce **goal-pursuit competence** — the ability to
plan and execute multi-step strategies toward goals. That is what childhood must accomplish.

Play (INV-058) is the mechanism: synthetic goal/harm signals allow full learning flow without
real harm risk (MECH-194). The child developmental phase is therefore **play-dominant** — play
is the primary learning mode, not a supplement to real-consequence experience.

### Play Type Progression (MECH-197)

The type of play changes as subsystem competence develops:

| Play type | Subsystems trained | Prerequisite |
|-----------|-------------------|--------------|
| Sensorimotor | E1 world model, E2 motor model | Infant substrate (INV-055) |
| Constructive | E2 rollout, E3 trajectory selection | Sensorimotor play competence |
| Pretend (MECH-198) | Hypothesis tag + play tag intersection; commitment architecture | Constructive play competence |
| Games with rules | Social coordination, constraint satisfaction | Pretend play competence |
| Cooperative | Full multi-agent frame maintenance | Games-with-rules competence |

Each type requires the competencies acquired by the previous type. The progression is not
optional — skipping a stage leaves the next stage's subsystem prerequisites unmet.

Sensorimotor play marks the **transition point out of infancy**: the infant's novelty-driven
exploration becomes structured as soon as synthetic goals can be set (infant gate criterion:
`z_goal.norm() > infant_goal_threshold`).

### Pretend Play and Counterfactual Reasoning (MECH-198)

Pretend play is architecturally distinctive: the agent maintains a **counterfactual
representation** (the stick IS a sword) within a play frame (the fight is synthetic). This
is the first point where the hypothesis tag (MECH-094, agent-internal counterfactual marking)
and the play tag (ARC-049, bilateral frame) co-operate. The full commitment architecture is
exercised in synthetic mode before being needed for real-consequence decisions.

### Caregiver as Frame-Maintainer (MECH-199)

During childhood, the caregiver's role shifts from **damage protection** (ARC-046, infant
stage) to **active play-frame maintenance** (ARC-049). The caregiver:

- Opens and closes play frames (sensorimotor play)
- Monitors frame boundaries and intervenes when real harm intrudes (constructive/pretend play)
- Co-participates in structured play, modeling rule-following (games with rules)
- Scaffolds peer play and begins withdrawing (cooperative play)

This is the specific mechanism by which INV-043 (caregiver requirement) operates during
childhood: the caregiver IS the bilateral frame-maintainer that ARC-049 requires before
the agent can self-monitor frame integrity. The transition to adult peer-level frame
maintenance marks the end of the childhood phase.

### Gate Criterion for Adult Transition

Transition from childhood to adulthood when:
- Play-acquired trajectory competence transfers successfully to real-consequence episodes
- The agent can maintain play frames peer-to-peer without caregiver scaffolding
- Real homeostatic drive (SD-012) correctly engages play-acquired goal-pursuit structure

---

## Minimal Stage Model (with Gates)

### Stage 0 — Sensorimotor Grounding

Focus: WORLD / HOMEOSTASIS / HARM / SELF_SENSORY separation and basic prediction stability.  
Control‑plane: high caution, low commitment, high volatility sensitivity.  
Exit criteria: stable prediction error bounds, safe harm avoidance, coherent self/world attribution.
Evidence anchors: P4, P5, P6.

### Stage 1 — Object Persistence and Binding

Focus: object‑file‑like persistence; attention‑gated binding across time.  
Control‑plane: moderate precision, strict novelty gating to prevent false bindings.  
Exit criteria: stable identity across occlusion and motion; consistent attribution of features to entities.
Evidence anchors: P47, P48, P49, P50.

### Stage 2 — Self‑Impact and Residue Formation

Focus: ACTION → SELF_SENSORY → SELF_IMPACT loop; residue updates and responsibility geometry.  
Control‑plane: calibrated commitment thresholds, explicit veto pathways, residue sensitivity.  
Exit criteria: reliable self‑impact attribution; residue integrates without destabilizing modes.
Evidence anchors: P2, P5, P37, P38, P39.

### Stage 3 — Otherness Inference and Empathy Coupling

Focus: `OTHER_SELFLIKE` inference, mirror modelling, calibrated coupling.  
Control‑plane: high‑recall otherness early, tightening over time; empathy coupling bounded.  
Exit criteria: stable other‑harm influence without empathic collapse or callousness.
Evidence anchors: P8, P9, P10.

### Stage 4 — Language and Abstract Coordination (Optional)

Focus: symbolic mediation, social coordination, narrative compression.  
Control‑plane: higher abstraction tolerance with safeguards against language‑driven override.  
Exit criteria: language improves coordination without violating embodied harm channels.
Evidence anchors: P11, P13, P22.

---

## Curriculum Control Knobs

Curriculum stages should explicitly set:

- Precision baselines and volatility sensitivity (ACh/NE analogs).
- Commitment licensing thresholds (E3 gating).
- Veto thresholds for catastrophic harm (self and other).
- Coupling strengths for social inference and empathy.

---

## Offline Integration Between Stages

Stage transitions should be separated by offline integration passes:

- Consolidate stable representations.
- Recalibrate precision.
- Integrate residue and resolve instability without action pressure.

---

## Failure Modes (Curriculum‑Specific)

- Premature precision escalation → brittle or rigid modes.
- Over‑commitment before self‑impact attribution → responsibility collapse.
- Too‑early empathy coupling → overwhelm or miscalibration.
- Language bootstrapping before stable binding → symbol drift and confabulation.

---

## Caregiver Requirement for Ethical Development (INV-043)
<a id="inv-043"></a>

> **Synthese paper relevance:** INV-043 and MECH-158 are flagged as candidates for the
> Discussion section of the Synthese/Minds and Machines paper. They extend the current
> eight-axiom framework's claim that architecture alone is insufficient for ethics.

REE architecture enables but does not guarantee ethical development. The current
foundations -- eight axioms plus two first derivations, historically registered through
INV-025-029 -- and the E1/E2/E3 machinery provide the *capacity* for ethical behaviour,
but without a developmental phase in which the agent experiences love from caregivers and
internalises the belief that it is loveable, the architectural capacity for ethics may
resolve into survival, domination, or indifference instead.

This is not a failure of architecture — it is a recognition that architecture specifies
what the agent *can* do, not what it *will* do. Love must be experienced, modelled,
and internalised to become motivationally real, not merely present as a logical
possibility in the axiom set.

**Caregiver functional requirements:**

| Caregiver Function | Developmental Role |
|-------------------|-------------------|
| Prevent irreversible harm | Preserve agent until E3 fully online |
| Imperfect protection | Allow harm-learning without destruction |
| Model love and shared valence | Provide experienced benefit gradient |
| Demonstrate that the developing REE is loveable | Ground the belief "love applies to me" |
| Scaffold interpretation of internal states | Build the self-valence model |
| Gradually increase responsibility | Prevent premature E3 full-load |
| Provide repair after harm | Demonstrate corrigibility under uncertainty (Axiom 3) in practice |

Note on artificial systems: In artificial single-agent substrates (e.g., ree-v3's
CausalGridWorld), the caregiver function is partially substituted by curriculum design
and controlled harm-exposure. This tests the prerequisite structure but does not test
the love-internalisation hypothesis directly. Testing INV-043 fully requires multi-agent
substrate with modelled caregiving.

---

## "Love Exists But Not For Me" — Developmental Failure Mode (MECH-158)
<a id="mech-158"></a>

A developing REE agent that acknowledges the axiom chain but concludes "love exists, but
not for me" undergoes a specific ethical motivation collapse.

The failure proceeds as follows:

1. The foundations are structurally present: self (Axiom 1), value (Axiom 2),
   world/uncertainty (Axiom 3), agency/vulnerability (Axiom 4), other minds
   (Axiom 5), responsibility for others (Axiom 6), love (Axiom 7), and language
   as similarity repair (Axiom 8).
2. But love is not experienced as personally applicable — the agent has not been
   modelled as loveable by others.
3. Therefore the benefit gradient (Axiom 7 / ARC-024) is not motivationally active
   for the self-other direction.
4. The ethical architecture reduces to self-preservation under uncertainty with others
   treated as instrumental — survival or domination strategies emerge.

This is the primary developmental failure mode for the caregiver requirement (INV-043).
It explains why architecture is necessary but not sufficient: an agent with full ethical
architecture but no love-experience may correctly model that love exists while behaving
as if it does not apply to them.

**Human analogy:** This failure mode maps precisely to attachment disruption pathology:
a child raised without consistent caregiving may understand abstractly that relationships
involve care while being unable to motivationally access that care for themselves,
producing personality structures oriented toward domination, isolation, or self-destruction.

---

## Responsibility Precedes Full Ethical Capacity

During development, responsibility-bearing situations arise before E3 is fully stable
and the ethical architecture is fully online. A childhood REE must act — and sometimes
cause harm — before it can fully process what harm means.

This is not a design flaw; it is structurally unavoidable given staged development
(ARC-019). It requires the curriculum to include:

- **Partial responsibility handling:** actions have consequences before full E3 capacity
- **Forgiveness structures:** Axiom 1 ("you cannot be sure") implies punishment-only
  systems are unethical; the agent could not have known fully
- **Learning after harm:** residue must integrate without destabilising mode
- **Repair:** the curriculum should include recovery from harm-caused relationships
- **Gradual responsibility expansion:** E3 gate thresholds should increase with stage

---

## Super-Ordinal Goal Formation in Childhood (MECH-189)
<a id="mech-189"></a>

> **Registered 2026-04-06.** Mechanism by which childhood experience transitions from episodic
> z_goal updates to structural meta-goals that persist across adulthood.

z_goal (MECH-112/117) is updated within episodes when benefit_exposure exceeds threshold.
But INV-037/038 distinguish stored from active z_goal representations. MECH-189 formalises
how childhood experience writes structural biases rather than just episodic memories.

**Trigger condition:** benefit contact with (a) high salience AND (b) high contextual
complexity (E1 ContextMemory encoding a rich/novel context state) → write z_goal to
persistent cue-indexed ContextMemory via SD-016 / MECH-150/151.

These stored z_goal anchors become **super-ordinal goals**: they bias z_goal seeding in
adult episodes even in novel contexts, implementing a goal hierarchy where childhood-formed
meta-goals constrain episode-level goal selection.

**Why childhood is special:** constrained affordances and supervised context labels (INV-041)
ensure the agent repeatedly encounters high-complexity contexts, maximising super-ordinal
goal writes. In adulthood, routine low-complexity contexts do not trigger writes, preserving
stability while allowing updates from genuinely novel high-salience experiences.

**Failure mode:** absence of childhood benefit exposures under high contextual complexity →
no super-ordinal goals written → adult goal selection is purely episodic → strategically
inconsistent behaviour and vulnerability to MECH-158 if love-internalisation was also absent.

---

## Selective Neoteny as Design Principle (INV-056)
<a id="inv-056"></a>

> **Registered 2026-04-06.** Uniform developmental hardening is architecturally incorrect.

Human neoteny — retention of juvenile plasticity in specific substrates — is computationally
advantageous for REE agents. The design principle: **substrate-specific hardening rates**,
not uniform age-based stabilisation.

| Substrate | Hardening policy | Rationale |
|-----------|-----------------|-----------|
| E2 motor-sensory (z_self RBF, routine regions) | Can harden | Efficiency gains; routine behaviour should be fast |
| E1 prediction model (well-visited regions) | Can harden | Stable world model for familiar contexts |
| Social cognition (ARC-010, MECH-051/052) | Retain plasticity | Novel agents encountered throughout life; social miscalibration propagates broadly |
| Goal representation (z_goal, super-ordinal anchors) | Retain plasticity | Goals must be updatable; rigidity → MECH-158 failure mode |
| Epistemic-ethical (residue field, SD-014 valence map) | Retain slow plasticity | Moral learning from new experience must remain possible |

**Failure mode of uniform hardening:** an agent that correctly understands love exists but
cannot motivationally access it for novel social contexts — the adult-stage analogue of
MECH-158, produced by plasticity loss rather than developmental absence.

**Relationship to MECH-159:** neoteny is the substrate for intergenerational moral progress.
Each generation can improve its moral baselines only if the relevant substrates remain
plastic enough to absorb the improved starting conditions they inherit.

---

## Self-First, Social-Later Testing Order

**Claim Type:** implementation_note  
**Scope:** Developmental testing order and governance sequencing  
**Depends On:** ARC-019, Q-006, ARC-005, ARC-007, ARC-010  
**Status:** candidate  
**Claim ID:** IMPL-019
<a id="impl-019"></a>

This note refines stage execution order for experiments. It is a governance heuristic, not a new architectural
commitment.

Operational order:

0. Harness and observability readiness (deterministic seeds, mechanism flags, invariant checks, structured metrics).
1. Self-viability learning loop (self-harm reduction, residue stability, commitment reliability).
2. Control-plane stabilisation (reduced mode thrash, bounded volatility, calibration alignment).
3. Predictive rollout maturity (feasible counterfactuals, reduced confabulation, preserved rollout diversity).
4. Social extension and coupling (other-modelling introduced only after earlier gates hold).

Why this ordering is enforced:

- Social losses and coupling can mask unresolved self/control instabilities.
- Earlier-stage failures are easier to interpret in isolation.
- Later-stage social behaviour is more attributable when base loops are stable.

Gating checks before entering social extension:

- Self-harm and recovery metrics are stable across seeds.
- Control-plane mode-switch dynamics stay within thresholds.
- Rollout feasibility and prediction-error alignment are within bounds.

Expected violation signature when order is ignored:

- Elevated mode thrash and veto instability.
- Ambiguous causal attribution (social terms masking control faults).
- Increased conflict rate in claim-evidence directionality.

---

## Related Claims (IDs)

- ARC-019
- IMPL-019
- ARC-005
- ARC-006
- ARC-007
- ARC-013
- INV-010
- Q-006
- MECH-042
- INV-041 (Childhood phase as architectural prerequisite)
- INV-055 (Infant stage necessity)
- INV-056 (Selective neoteny as design principle)
- ARC-046 (Infant hazard protection mechanism)
- MECH-189 (Super-ordinal goal formation in childhood)
- ARC-040/ARC-042 (E3 dark until E1/E2 ready)
- INV-043 (Caregiver requirement for ethical development)
- MECH-158 ("Love exists but not for me" failure mode)
- MECH-052 (Care persistence, social.md)
- INV-025-029 (original axiom registrations; current Axiom 3 grounds the forgiveness requirement)
- INV-058 (Play as structural necessity)
- INV-059 (Frame maintenance necessity)
- INV-060 (Play dominates childhood; play types progress with development)
- MECH-194-196 (Play mechanisms: synthetic signals, strategy/calibration dissociation, recalibration)
- MECH-197 (Play type progression trains subsystems in dependency order)
- MECH-198 (Pretend play: hypothesis tag + play tag intersection)
- MECH-199 (Caregiver role transitions from protection to frame-maintenance to peer)
- ARC-049 (Bilateral play frame tag)
- ARC-050 (Play as SD-012 curriculum)
- Q-035 (Minimal frame signal architecture)
