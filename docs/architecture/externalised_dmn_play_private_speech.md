# Externalised Default Mode Operation; Private Speech as Developmental Cognitive-Control Scaffold

**Status:** V4+ developmental-architecture cluster (candidate). Off the REE-v3 critical
path. Registered as the home doc for the externalised-DMN / private-speech intake.

**Source thought:** [`docs/thoughts/2026-06-08_play_private_speech_externalised_dmn.md`](../thoughts/2026-06-08_play_private_speech_externalised_dmn.md)
(Training-Data Confidence 0.82, Epistemic Confidence 0.74 -- the psychology/neuroscience
anchors are solid; the REE mapping is a strong architectural analogy, not an established
empirical claim).

**Scope guardrail (from the thought, preserved verbatim in intent):**

> Use this to improve the developmental interpretation of REE.
> Do not use it to expand REE-v3 unless the implementation is small, testable, and
> directly green-board relevant.

The REE-v3 strict green-board target (Sunday 19 July 2026; optimistic 28 June 2026) takes
precedence. The developmental machinery below is V4+ and must not enter the V3 critical path.
The single V3-compatible reduced form is the **self-narration trace/debug scaffold**
(MECH-384), and even that is a post-green-board observability surface, not a committed work
item.

---

## Core intuition

**Play resembles externalised Default Mode Network (DMN) operation.** The DMN is associated
with internally-generated modelling: self-reference, autobiographical memory, social
imagination, future simulation, counterfactual thought, and narrative construction. In play,
these functions are not kept wholly internal -- they are pushed *outward* into objects, roles,
movement, spoken narration, social interaction, and temporary "as-if" worlds ("this block is a
house"; "I am the doctor"; "the dragon is coming"). Play lets the organism say: *let this be
true temporarily; act inside it; observe what follows; exit without catastrophe.* That may be
a developmental root of safe counterfactual cognition.

**Private speech (Vygotsky) is the external phase of a cognitive-control system that later
becomes silent inner speech.** Children narrate, instruct, correct, rehearse, and regulate
themselves out loud. The internalisation ladder: (1) others speak to the child; (2) the child
speaks to others; (3) the child speaks to itself out loud; (4) this internalises into inner
speech; (5) inner speech becomes compressed cognition -- planning, inhibition, self-instruction,
self-regulation. Private speech is a *temporary control surface* that makes cognition
inspectable before it becomes compressed.

**Play and private speech are two faces of one developmental scaffold:** play externalises
possible-world simulation; private speech externalises control of attention, action, affect,
and task sequence. Together they form an intermediate layer between raw perception/action and
mature internal cognition.

A developmental ladder:

1. Raw sensorimotor exploration -- action-consequence learning.
2. Play -- rehearse possible worlds/actions without full real-world commitment.
3. Private speech / self-narration -- narrate, label, and guide one's own action and attention.
4. Inner speech / internal simulation -- the external scaffold compresses into internal control.
5. Mature REE arbitration -- simulate, evaluate, inhibit, reframe, and commit without
   externalising every step.

---

## What REE already owns (depends_on cross-refs, NOT re-registered)

This intake is fertile but most of its surface is already covered. The genuinely-new content
is narrow; the rest is cross-reference.

| Already-owned | Claims | Relation to this intake |
|---|---|---|
| Internal DMN: safe imagination without commitment | ARC-014 | The *internal* end-state this cluster's externalised form develops INTO |
| DMN reflective/moral evaluation of replay | MECH-029 | Evaluative arm of internal DMN; the developmental target of externalised narration |
| Play as bounded low-stakes learning mode | INV-058, INV-059, INV-060 | Play's structural necessity / frame maintenance / developmental dominance |
| Synthetic-signal play substitution + frame tag | MECH-194..MECH-199, ARC-049, ARC-050 | The play-frame mechanism; "play/simulation mode" is THIS, not new |
| Pretend-play tag intersection ("stick is a sword") | MECH-198 | The hypothesis-tag x play-frame-tag co-operation |
| Play-type progression (sensorimotor->cooperative) | INV-060, MECH-197 | Progression WITHIN play; distinct from the externalise->internalise compression axis |
| Simulation vs commitment write profile / hypothesis tag | MECH-094 | Already distinguishes simulated from committed writes |
| Commit-boundary token | MECH-061 | Already reclassifies pre/post-commit error routing |
| Socially-scaffolded rule population (Vygotsky ZPD) | ARC-077, MECH-337 | Other->self scaffolding for RULE content; distinct from self-CONTROL internalisation |
| Control plane routes precision and modes | ARC-005 | Substrate the label-as-control and distancing operators would act through |
| Attention as distributed precision-selection | MECH-251, MECH-254, MECH-255, MECH-261 | The precision-tuning the label-feedback mechanism rides on |
| Frame-confusion psychiatric etiology | INV-061 | Failure side of under-developed real/synthetic frame distinction |
| Goal maintenance necessary for ethical agency | INV-034 | The control target private speech regulates |

"Play/simulation mode" as a module implication is therefore **not** a new claim -- it is the
existing play cluster (MECH-194/198, ARC-049) plus the MECH-094 simulation write-profile. It
appears here only as a cross-ref.

---

## Genuinely-new claims registered (this cluster)

All V4 developmental claims are `status: candidate`, `epistemic_category:
substrate_conditional`, `implementation_phase: v4`, `version_relevance: v4_v5` -- they depend on
developmental substrate (staged curriculum, multi-agent frame maintenance, a self-narration
control surface) that V3 does not have, so they are correctly invisible to the inter-governance
workset (IGW) proposal lane and do not generate vacuous V3 probes.

- **ARC-090** -- *Externalised Default Mode Operation (umbrella).* Play instantiates DMN
  functions (self-reference, autobiographical memory, social imagination, future simulation,
  counterfactual thought, narrative construction) **externally** -- pushed outward into objects,
  roles, movement, spoken narration, and temporary as-if worlds -- as the developmental
  precursor to the internal DMN (ARC-014/MECH-029). The developmental arc compresses
  externalised modelling into internal generative modelling. Bridges the internal-DMN claims
  to the play cluster, neither of which currently frames play as externalised DMN.
  depends_on: ARC-014, MECH-029, ARC-049, MECH-198, INV-058, INV-060.

- **MECH-380** -- *Private speech as externalised cognitive-control scaffold.* Overt
  self-narration is the external phase of a control loop over attention, action, affect, and
  task sequence; the Vygotskian internalisation ladder (other-regulation -> overt
  self-regulation -> inner speech -> compressed control) is the developmental route by which
  external control surfaces become internal. Distinct from ARC-077/MECH-337 (scaffolding of
  rule CONTENT) -- this is scaffolding of self-directed CONTROL. depends_on: ARC-090, INV-034,
  MECH-029, ARC-077, MECH-337.

- **MECH-381** -- *Developmental compression ladder.* sensorimotor exploration -> play/simulation
  -> self-narration -> compressed internal control -> mature arbitration: external scaffolds
  compress into internal control over development. Distinct from INV-060/MECH-197 (progression
  of play TYPES) -- this is the externalise->internalise compression axis that runs across the
  whole ladder. depends_on: ARC-090, INV-060, MECH-197, MECH-380.

- **MECH-382** -- *Distancing operator.* Reframing a sticky, high-conflict, self-referential
  state from first-person ("I am failing") into a model-like system-state / third-person frame
  ("REE is encountering unresolved prediction-error pressure under current constraints")
  reduces self-referential collapse and increases model-based inspection during arbitration.
  Not cosmetic -- a low-effort self-distancing operator on arbitration (Kross and Moser
  third-person self-talk). depends_on: ARC-090, ARC-005, INV-061.

- **MECH-383** -- *Labels as active top-down perceptual-control signals.* A self-directed label
  ("food-gradient", "danger-gradient", "novelty-gradient", "blocked-goal", "return-to-baseline")
  is not merely a post-perceptual report -- it is a top-down tuning signal that biases perceptual
  search and detection (Lupyan and Swingley visual-search work). It is a perceptual-control
  intervention riding on the ARC-005 control plane / MECH-251/261 precision-selection
  machinery. depends_on: ARC-090, MECH-029, ARC-005, MECH-251, MECH-261.

- **Q-068** -- *Graded action-status vocabulary.* Does REE need an explicit graded action-status
  annotation -- `simulated != rehearsed != intended != committed != acted` (and a parallel
  `self_reference_frame`: first_person / system_state / third_person_model) -- as a first-class
  field, or do MECH-094's simulation/commit write-profiles plus MECH-061's commit-boundary token
  already suffice? `epistemic_category: substrate_conditional` set explicitly so
  `narrow_open_question` does not fire. depends_on: MECH-094, MECH-061, ARC-090.

### Separate, narrowly-scoped V3 reduced form

- **MECH-384** -- *Lightweight self-narration trace/debug scaffold.* The one V3-compatible
  instantiation in the thought: an optional traceable self-narration field set that exposes
  REE's working state for inspection -- `state_label`, `goal_label`, `sensed_gradient`,
  `active_prediction`, `uncertainty_level`, `candidate_action`, `candidate_action_reason`,
  `expected_consequence`, `affective_pressure`, `conflict_flag`, `commitment_threshold`,
  `stop_condition`, `simulation_or_commitment`, `self_reference_frame`. This is REE's early
  "private speech" surface BEFORE it is compressed -- a debug/observability surface, not new
  substrate machinery. Registered as `claim_type: design_decision`, `epistemic_category:
  substrate_coherence` (a design/observability choice, not a falsifiable mechanism needing a
  probe -- this keeps it out of the IGW proposal lane), `status: candidate`,
  `implementation_phase: v3`, `version_relevance: v3_v4`. **Post-green-board and off the V3
  critical path:** build only if it helps REE-v3 pass existing tests more cleanly. The fields
  largely re-expose state REE already computes; the claim is the decision to surface them as a
  coherent trace. depends_on: ARC-090, MECH-094.

---

## The key architectural distinction this cluster makes explicit

> Not every possible action is an intended action.
> Not every intended action is a committed action.
> Not every simulated state is a believed state.
> Not every affective pressure should collapse into behaviour.

`simulation != intention != commitment != action`. REE already enforces the simulation/commitment
boundary (MECH-094) and the commit-boundary reclassification (MECH-061); Q-068 asks whether the
finer graded vocabulary is worth making first-class.

---

## V3 vs V4 boundary

- **V3 (post-green-board, optional):** MECH-384 self-narration trace surface only, and only if
  it helps pass existing tests. Nothing else from this cluster touches V3.
- **V4+:** the developmental machinery -- externalised-DMN play scaffold (ARC-090), private-speech
  control internalisation (MECH-380), the compression ladder (MECH-381), the distancing operator
  (MECH-382), label-as-control (MECH-383). These need a staged developmental curriculum, a
  self-narration control surface that can actually drive arbitration, and (for the bilateral
  play frame) the multi-agent substrate ARC-049 already flags as a V4 requirement.

## Evidence anchors (architectural analogy, not citable mechanism evidence)

- Vygotskian private speech: widely treated as a developmental route into inner speech and
  self-regulation.
- Lupyan and Swingley (visual search): self-directed labels can alter perceptual search.
- Kross and Moser (third-person self-talk): low-effort self-distancing reduces emotional
  reactivity.
- DMN literature: links the network with self-reflection, memory, future simulation, and
  internally-generated cognition.

These are textbook-level psychology/neuroscience anchors supporting a strong architectural
analogy. They are not a single citable out-of-domain dataset and are recorded as anchors here
rather than as a separate research_anchor claim.
