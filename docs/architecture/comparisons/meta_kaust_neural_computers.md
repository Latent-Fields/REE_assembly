---
nav_exclude: true
---

# REE versus Neural Computers: A Technical Comparison
<!-- IMPL-027 -->

**Status:** candidate
**Registered:** 2026-04-12
**Depends on:** INV-025, INV-026, INV-027, INV-028, INV-029, MECH-069, ARC-021, INV-049, IMPL-024

---

## 1. The Neural Computers Programme

Schmidhuber et al. (2025) — a 19-person collaboration from Meta AI and KAUST — propose that the
next fundamental computing platform is the *Neural Computer* (NC): a system in which computation,
memory, and I/O are unified as a single learned runtime state within a neural network. The core
claim is that "the model itself" becomes the executable computer; there is no separation between
the AI system and the operating environment it runs in.

Their four requirements for a *Completely Neural Computer* (CNC):

| # | Requirement | What it means |
|---|-------------|----------------|
| 1 | Turing completeness | Express arbitrary computations |
| 2 | Universal programmability | Install routines via instruction or demonstration — no explicit code |
| 3 | Behavior consistency | Prevent silent drift during multi-step execution |
| 4 | Machine-native semantics | Develop genuine machine semantics, not just imitation of observed I/O |

Their current prototypes — trained on screen-recording I/O traces (CLIGen: 1,100 hours; GUIWorld:
1,510 hours) — demonstrate basic interactions but fail on all four requirements under any
non-trivial load. Acknowledged failures include: inability to reliably perform two-digit
arithmetic, no long-horizon behavioral stability, no routine reuse across contexts, and
catastrophic forgetting when acquiring new capabilities.

Their roadmap calls for: unbounded effective memory, composable reusable programs, architectural
separation of inference from parameter updates, and eventual hardware evolution toward sparser,
addressable, circuit-like architectures.

---

## 2. REE's Architectural Answers to the Four CNC Requirements

REE is a research programme that derives agent architecture from first principles rather than
designing it (see [five_axioms_foundations.md](five_axioms_foundations.md)). The current
canonical foundation is an eight-axiom chain plus two first derivations. The older five-axiom
formulation remains a compact mnemonic: uncertainty, self, world, others, love. The expanded
chain makes explicit that existence has value, agency requires both causal power and
vulnerability, responsibility for others is existentially necessary, and language helps repair
the self-other similarity model. The required architecture follows by logical necessity from
that chain. The comparison below shows that REE's derived structures address each CNC
requirement not by engineering toward it, but because the requirement is an instance of a more
general architectural necessity.

### 2.1 Behavior Consistency

**NC's failure:** Behavior drifts silently over multi-step tasks. The model cannot maintain a
consistent execution context without active retraining.

**REE's answer:** Commitment gating. E3 maintains a typed commit boundary — a specific
architectural transition point at which action becomes irreversible and fully attributable (INV-021,
MECH-061). Before this boundary, E3 runs multi-step trajectory simulation through the hippocampal
rollout mechanism (ARC-007). The beta-gate (MECH-090) suppresses premature policy output to the
action selection system while E3 is internally updating; the control plane releases the gate only
at commit time. This is not a mechanism added to prevent drift — it is the necessary consequence
of distinguishing rehearsal from realization (INV-019: rehearsal traversal and irreversible
durable write must remain separated).

Behavioral consistency is therefore a structural invariant in REE, not a training target. NC's
failure on this requirement arises because they have no equivalent of the commit boundary — the
model produces output continuously from the same parameter state that is also being used for
context simulation. These cannot be safely simultaneous.

**Key claims:** INV-019, INV-021, MECH-061, MECH-090, ARC-016

### 2.2 Long-Horizon Stability

**NC's failure:** Behavior degrades over extended multi-step sequences. There is no mechanism
for stable reference-frame maintenance across long episodes.

**REE's answer:** E3 operates via explicit hippocampal trajectory planning — multi-step rollout
on a latent map, not implicit hidden-state continuation (ARC-007, ARC-018). The hippocampal
module maintains a valenced viability map that E3 traverses during planning. Trajectories are
evaluated against harm and goal gradients before commit. This is architecturally different from
recurrent hidden-state propagation: the map is a persistent structure that does not degrade with
sequence length.

Long-horizon stability also requires the multi-timescale latent stack. REE's L-space stratifies
latent representation across four frequency bands (gamma, beta, theta, delta), with slower bands
carrying increasingly persistent structure. The delta band functions as cross-session persistent
context — the REE equivalent of "unbounded effective memory" in the NC roadmap — while the
gamma band handles step-level working state. This stratification prevents the accumulation of
fast noise into slow representations.

**Key claims:** ARC-007, ARC-018, MECH-089 (theta-gamma nesting), MECH-093 (z_beta modulation)

### 2.3 Universal Programmability

**NC's requirement:** Install routines via instruction or demonstration without explicit code.
Their prototypes cannot do this — learned routines do not transfer across contexts and are lost
under new learning.

**REE's answer:** The residue field. Past actions leave persistent consequence traces that shape
future policy without retraining (INV-004: irreversible harm creates moral residue; INV-012:
responsibility-bearing state changes occur only at typed commit boundaries). The residue field is
REE's architectural substitute for "installing a routine" — a prior action's world-consequence
footprint remains as a weighted influence on E3's future trajectory selection. This is not
memory in the sense of stored weights; it is a structural trace in the latent world-state that
E3 reads during future planning.

For routine transfer across contexts, REE relies on E3's hippocampal module. A trajectory that
was successful in one context is stored as a candidate in the viability map; E3 can propose it in
a structurally similar context by map-navigation rather than by re-learning. This directly
addresses NC's context-transfer failure.

NC's "programmability from demonstration" has a narrower parallel in REE: the commitment
architecture means that a witnessed action sequence (in REE's social model — see [social.md](social.md))
can be stored as a trajectory proposal in E3 and replayed in the agent's own context. The
mechanism differs from NC's I/O-trace approach but addresses the same functional gap.

**Key claims:** INV-004, INV-012, ARC-007, ARC-018

### 2.4 Machine-Native Semantics

**NC's requirement:** Develop genuine machine semantics — not imitation of observed I/O streams.
Their prototypes are trained entirely on I/O traces, which means they can replicate the *form*
of machine behavior without the *structure* that generates it.

**REE's answer:** REE's semantics are not learned from I/O — they are derived from the
foundational axiom chain. INV-025 through INV-029 registered the original five-axiom
formulation; the current foundations document expands and refines that into eight axioms plus
two first derivations. The architectural structures that follow (persistent world model, fast
transition predictor, harm accumulator, commit gate, multi-step planner) are necessary
consequences of those commitments, not pattern-matches to observed machine behavior. This is
what REE means by "a derivation, not a design."

The practical implication: REE components have a fixed semantic role (E1 = persistent world
model, E2 = fast motor-sensory transition model, E3 = trajectory planner with ethical commitment
gating) that cannot be displaced by training. Their semantics are structural, not emergent.
NC's semantics are fully emergent from I/O statistics — which is why they fail to transfer and
cannot perform arithmetic reliably. Arithmetic requires a structural account of number; I/O
statistics of screen-recordings provide only surface correlations.

**Key claims:** INV-025, INV-026, INV-027, INV-028, INV-029, ARC-001 (E-space three-loop
architecture)

---

## 3. REE's Additional Structures Not in the NC Roadmap

Several REE architectural features address deeper requirements that the NC roadmap does not yet
formulate:

**Ethical structure derived from axioms.** NC makes no claim about how a neural computer should
handle harm to others. REE derives ethical structure as an architectural necessity from INV-028
(others share the same consequence space as the self). The harm accumulator, residue field, and
commit gate are ethical mechanisms in the engineering sense — not policy add-ons but necessary
consequences of recognizing others.

**Incommensurable error streams.** REE's three-loop architecture routes three structurally
different learning signals through separate channels: sensory prediction error (E1), motor-sensory
error (E2), and harm/goal error (E3) (MECH-069, ARC-021). These cannot be collapsed into a
single loss — doing so misattributes credit and destroys the information content of each signal.
NC uses a single I/O prediction loss. This is the deepest architectural difference: NC has one
error signal; REE requires three incommensurable ones.

**Offline consolidation as mathematical necessity.** REE derives the requirement for periodic
offline phases (sleep-analog) from the fundamental incompatibility of model-use and model-update
(INV-049). A system that must use its world model to navigate the environment cannot safely update
that model during online operation — each update destabilizes the predictions the system is
depending on. This is a general computational necessity, not a biological contingency. NC's
roadmap calls for "architectural separation of inference from parameter updates" — this is exactly
the NC-language description of REE's offline/online phase separation.

**Clinical failure-mode mapping.** When REE components are removed, the resulting failure modes
match specific psychiatric syndromes (see [psychiatric_failure_modes.md](psychiatric_failure_modes.md)).
Absent harm accumulator: features of anhedonia. Closed attribution loop: passivity phenomena.
Precision dysregulation: psychosis-like states. This provides an external validation path that
NC does not have.

**Control-plane authority.** REE has a centralized control plane that routes precision signals
and manages transitions between operating modes (waking, sleep, committed sequence) (ARC-016).
This is architecturally different from NC's implicit mode handling via context window state. In
REE, modes are explicit architectural transitions; in NC, they are statistical regularities in
the I/O trace.

---

## 4. What the NC Roadmap Addresses That REE Does Not

REE does not currently specify:

**I/O interface layer.** NC's core contribution is the idea that the model itself can become
the I/O interface — reading and writing to screens, terminals, and GUIs directly. REE is
agnostic about the perceptual front-end; it specifies internal architecture, not I/O modality.

**Programmability from natural-language instruction.** NC aims for agents that can be programmed
by telling them what to do, in natural language, without code. REE specifies how a trajectory
can be proposed and committed but does not specify how natural-language instructions parse into
E3 trajectory proposals. This is an open interface.

**Hardware evolution roadmap.** NC includes a roadmap for hardware architectures supporting
sparser, addressable, circuit-like neural systems at 10T-1000T parameter scale. REE makes no
hardware claims.

---

## 5. Translation Table

| Neural Computers term | REE canonical term |
|------------------------|-------------------|
| Neural Computer (model-as-runtime) | Agent instantiating L-space + three-loop architecture |
| Behavior consistency | Commitment gating / beta-gate (MECH-061, MECH-090) |
| Long-horizon stability | Hippocampal trajectory planning (ARC-007) + multi-timescale L-space |
| Catastrophic forgetting | Solved by offline consolidation (INV-049) + timescale separation |
| Unbounded effective memory | Multi-timescale latent stack: delta-band persistent, theta-band episodic |
| Universal programmability | Residue field + hippocampal viability map (INV-004, ARC-018) |
| Machine-native semantics | Axiomatic derivation (current eight-axiom chain; INV-025-029 historical registrations) — structure, not imitation |
| Inference/parameter-update separation | Online/offline phase separation (INV-049) |
| Composable reusable programs | Hippocampal trajectory reuse across contexts (ARC-018) |
| Single I/O prediction loss | Three incommensurable error channels (MECH-069, ARC-021) |

---

## 6. The Relationship Between the Two Frameworks

NC and REE are not in competition. They operate at different architectural levels:

- **NC is an interface architecture.** It asks: how can a neural network become the computational
  substrate through which a user interacts with a computer? Its target is the boundary between
  user and machine.

- **REE is an internal architecture.** It asks: what structures must an agent have in order to
  act responsibly in a world? Its target is the internal organization of the agent that sits
  behind any external interface.

A fully realized NC would need to solve the internal problems that REE addresses — behavior
consistency, long-horizon stability, routine reuse without forgetting, genuine semantics — or it
would remain a high-fidelity I/O imitation engine. NC's own roadmap acknowledges this: their
four CNC requirements are internal-architecture problems, not interface problems. They are asking
for what REE has derived.

The convergence is significant. NC arrives at these requirements from the direction of systems
engineering (what would a neural computer need to be a real computer?). REE arrives at the same
structures from the direction of first principles (what must any responsible agent have?). That
both programmes converge on commitment boundaries, memory stratification, offline consolidation,
and incommensurable learning channels — from entirely different starting points — suggests these
are genuinely necessary structures, not design choices.

---

## References

- Schmidhuber, J. et al. (2025). *An Engineering Roadmap Toward Completely Neural Computers.*
  Meta AI / KAUST. Coverage: https://semiengineering.com/an-engineering-roadmap-toward-completely-neural-computers-meta-ai-kaust/
- REE foundational axioms: [docs/architecture/five_axioms_foundations.md](five_axioms_foundations.md)
- REE architecture overview: [docs/architecture/overview.md](overview.md)
- Commitment gating: [docs/architecture/e3.md](e3.md), [docs/architecture/control_plane.md](control_plane.md)
- Hippocampal systems: [docs/architecture/hippocampal_systems.md](hippocampal_systems.md)
- Offline consolidation necessity: claims.yaml INV-049
- Incommensurable error channels: claims.yaml MECH-069, ARC-021
- Clinical failure modes: [docs/architecture/psychiatric_failure_modes.md](psychiatric_failure_modes.md)
