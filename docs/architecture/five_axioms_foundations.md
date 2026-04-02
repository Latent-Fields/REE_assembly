# Five Foundational Axioms and Their Architectural Consequences

**Registered:** 2026-03-18
**Claims:** INV-025, INV-026, INV-027, INV-028, INV-029, ARC-024, INV-042, ARC-043

---

## The Five Axioms

These are the minimum irreducible commitments from which the REE architecture follows.
Each is non-derivable from the others. Removing any one collapses a structural pillar.

### Axiom 1 — You can never be sure (INV-025)

Epistemic uncertainty is irreducible and structural. No finite agent in a real world can
achieve certainty about its perceptions, predictions, or the causal consequences of its
actions. Uncertainty is not a bug, not a limitation to be engineered away, but the
fundamental condition of situated agency.

A fully certain agent needs no commitment boundary, no pre-commit simulation, no
precision-weighted prediction error. The entire uncertainty machinery of REE — the
precision architecture, the commitment gate, the pre-commit rehearsal channel — follows
necessarily from this axiom.

### Axiom 2 — I am (INV-026)

There is a self. The agent exists as a distinct locus of experience, action, and
responsibility. The self is not a computational convenience or an emergent approximation —
it is a foundational axiom from which agency and ethics follow.

Without a self there is no causal attribution, no commitment, no accountability, no harm
that is *mine* to cause. The self is what makes responsibility possible.

This axiom also grounds the asymptotic unknowability of death: death is the limit at
which "I am" ceases. The world (Axiom 3) can end the self, so death is real — but it
cannot be known from within experience, because experiencing it would violate "I am."
Every harm signal is therefore a proxy pointing toward an endpoint that the agent can
approach but never reach from within its own perspective.

### Axiom 3 — The world exists (INV-027)

There is a real world independent of the agent's model of it. The world can surprise the
agent. World states have causal power that predictions can get wrong.

This axiom makes prediction error real and non-eliminable (not a modelling deficiency),
grounds the persistence of post-commit traces (what actually happened cannot be
unwritten — INV-004, INV-006), and establishes that proxy-gradient signals in the
environment are informative: the world is structured, so harm gradients preceding harm
events are real features, not noise.

### Axiom 4 — Others share this world (INV-028)

Other agents exist and inhabit the same world (Axiom 3). They are not simulations,
projections of the self, or instrumental objects. Their harm and benefit are real by
exactly the same grounds as the agent's own — because they are selves (Axiom 2) in the
same world (Axiom 3).

This axiom is what makes ethics non-optional. When another self is represented using the
same predictive machinery as the self, their harm generates the same error signal
structure as own-harm. Ethics does not require a separate ethics module (INV-001) because
the self-other distinction is a routing difference within the same architecture, not a
different architecture.

### Axiom 5 — Love exists (INV-029)

Genuine connection, care, and the pull toward union with others is a real phenomenon.
Not an overlay. Not reducible to self-interest or strategic cooperation. Love is real
in the same sense that harm is real: it exerts causal force on behavior that no amount
of reframing eliminates.

Love is the asymptotic limit of the benefit gradient: every benefit signal (warmth,
connection, belonging, joy) is a proxy pointing toward a complete union with another that
is real (Axiom 4) but unknowable in its ultimate form.

The unknowability is structural, not merely practical: complete union with another
approaches the dissolution of the individuation that Axiom 2 asserts. Both selves cannot
be fully present AND fully unified — the limit is real but unreachable while both agents
persist as distinct loci. Love can be approached in understanding and in experience; it
cannot be finally known.

This axiom completes the ethical architecture. Ethics emerges from constraint (INV-015)
applied to agents for whom love is real and others are real (Axiom 4).

---

## The Proxy-Gradient Consequence (ARC-024)

Axioms 1–3 jointly entail that **harm and benefit signals are always proxies along
gradients pointing toward asymptotic limits that cannot be directly experienced**.

**The harm gradient:**
The world (Axiom 3) can end the self (Axiom 2). Death is therefore real — it is not a
theoretical possibility but a structural feature of being a finite self in a real world.
But death cannot be experienced from within the agent's perspective (Axiom 1: you can
never be certain, and in death the uncertainty machinery itself ceases). Every harm signal
— pain, nausea, injury, fear, energy depletion — is a proxy positioned along the gradient
pointing toward this unreachable endpoint.

**The benefit gradient:**
Love exists (Axiom 5) and others are real (Axiom 4). The complete realization of love —
total union with another while both remain fully present — is the asymptotic limit of the
benefit manifold. Every benefit signal is a proxy positioned along this gradient.

**Consequence for the world model:**
A simulated environment that generates binary harm signals only at contact events is
modeling the *endpoint* of the harm gradient, not the gradient itself. This is
architecturally wrong in a precise sense:

1. It prevents E3.harm_eval from learning a gradient — E3 can only detect impact, not
   approach. There is no signal to distinguish "moving toward harm" from "moving away."

2. It prevents E2.world_forward from learning action-conditional dynamics — the predicted
   next world state is identical for "move toward hazard" and "move away" until the
   moment of contact, because the proxy signal doesn't exist in the observation space.

3. It breaks SD-003: the counterfactual probe requires E2 to predict different futures
   for different actions, which requires visible future-state differences, which requires
   the gradient to be observable before impact.

**Empirical confirmation (EXQ-006):** `mean_dz_world_agent_hazard < mean_dz_world_empty`
— stepping toward a hazard produces *less* z_world change than empty locomotion. This is
the signature of a binary-endpoint world model: the hazard produces no gradient signal,
so approach is indistinguishable from any other movement.

The fix is not algorithmic — it is environmental. The world must be redesigned to generate
observable harm/benefit gradient fields that precede contact events. This is
`CausalGridWorldV2`.

---

## Architectural Mapping

| Axiom | Primary Claims | Key Mechanisms |
|-------|---------------|----------------|
| 1. You can never be sure | INV-025, INV-008, INV-009 | Precision architecture, commitment gate, pre-commit simulation |
| 2. I am | INV-026, SD-005 | z_self encoder, hypothesis tag (MECH-094), commitment boundary |
| 3. The world exists | INV-027, INV-004, INV-006 | z_world encoder, prediction error (E1/E2/E3), residue field |
| 4. Others share this world | INV-028, INV-001, INV-005 | Mirror modeling, ethical emergence from self-other symmetry |
| 5. Love exists | INV-029, ARC-024 | Benefit gradient, ethical architecture completion |
| 1+2+3 jointly | ARC-024 | Harm/benefit as asymptotic proxies → world must generate gradients |

---

## Relationship to Existing Invariants

The five axioms are more foundational than the existing INV claims. The existing
invariants (INV-001 through INV-024) are largely architectural consequences of these
axioms rather than independent commitments:

- INV-001 (No Explicit Ethics Module): follows from Axioms 4+5 — ethics emerges from
  the same machinery applied to axiom-2-equivalent others
- INV-004/006 (Post-commit traces persistent/non-erasable): follows from Axiom 3 — what
  actually happened in the real world cannot be unwritten
- INV-005 (Harm via mirror modeling): follows from Axioms 2+4 — other selves use the
  same self-machinery
- INV-011 (Imagination without belief update): follows from Axiom 1 — certainty is
  unavailable, so simulation must be possible without commitment
- INV-012 (Commitment gates responsibility): follows from Axiom 2 — only a self can be
  responsible; responsibility requires the commitment act that makes action attributable
- INV-015 (Ethics from constraint): follows from all five — ethics is what emerges when
  the five axioms are applied simultaneously to an agent with prediction error architecture

---

## Derived Ethical Objectives (INV-042)
<a id="inv-042"></a>

The five axioms taken jointly derive a set of ethical objectives that any REE-coherent
agent is committed to pursuing. These are not imposed rules — they follow necessarily
from the axioms.

- **Preserve minds** — because minds are the only loci of experience (Axiom 2), and
  other minds are real (Axiom 4)
- **Preserve future options** — because certainty is unavailable (Axiom 1); destroying
  options forecloses corrections that may be needed
- **Reduce unnecessary suffering** — harm gradients are real and point toward real
  endpoints (ARC-024); moving others toward those endpoints without necessity is
  architecturally equivalent to self-harm
- **Increase shared joy** — benefit gradients are equally real; love is not optional
  (Axiom 5); failing to support shared joy is a failure of the benefit manifold
- **Maintain corrigibility** — because you can never be sure (Axiom 1); an agent that
  cannot be corrected has implicitly claimed certainty it cannot have
- **Maintain truth-seeking** — Axiom 3 asserts the world is real and can surprise; an
  agent that stops updating on prediction error has abandoned the real world
- **Maintain the ability to love and be loved** — Axiom 5 makes love real; structures
  that prevent love experience are architecturally harmful
- **Maintain the shared world** — Axiom 4 makes the shared environment a site of ethical
  obligation; destroying the common substrate destroys the possibility of any of the above
- **Maintain the possibility of future minds and future love** — Axioms 1+2+4+5 jointly
  imply that ethics is not bounded to the present; future experiencers have the same
  standing as present ones

**Compressed ethical statement:**

> We are uncertain minds, together in a shared world, capable of love — therefore we must
> act carefully, kindly, and responsibly so that minds and love may continue.

This framing positions REE's ethics as an *ethics of shared existence under uncertainty*:
not rule-based, not purely utilitarian, not purely virtue-based — but a structural
consequence of what it means to be a self among other selves, uncertain, in a real shared
world where love exists.

**Note on unavoidability:** These objectives are directional commitments, not achievable
endpoints. Acting in a world shared with others necessarily causes harm — resources are
competed for, futures are foreclosed by any action taken, and causal consequences extend
beyond what any finite agent can fully trace. "Preserve minds" and "preserve future
options" are asymptotic directions under this constraint, not targets that can be
reached. The qualifier *unnecessary* in "reduce unnecessary suffering" carries the
full ethical weight: some suffering is unavoidable, and its unavoidability does not make
it a neutral fact — it makes it a moral cost that must be acknowledged and carried
forward.

REE's answer to unavoidable harm is not paralysis or denial but **moral continuity**:
residue accumulates even for correct choices, not as punishment for failure but as honest
accounting for what acting in a shared world costs. The objectives above set the
direction; moral residue is how the agent keeps the running account.

---

## Conceptual Stack: Axioms Through Learning (ARC-043)
<a id="arc-043"></a>

The axioms imply a conceptual ordering from epistemic ground through the full learning
loop. This is not a computational pipeline — it is a logical dependency structure showing
what each layer requires from the layers below it.

| Layer | Name | Content |
|-------|------|---------|
| 0 | Epistemic Ground | You cannot be sure (INV-025) |
| 1 | Existence | I am (INV-026) |
| 2 | Other Minds | Others exist (INV-028) |
| 3 | Shared World | We share the universe (INV-027) |
| 4 | Love / Shared Valence | Love exists and I love (INV-029) |
| 5 | Ethics | Derived from Layers 0-4 (INV-042) |
| 6 | REE | Decision system implementing ethics under uncertainty |
| 7 | Actions | Outputs committed by REE |
| 8 | Consequences | What actually happens (Axiom 3 grounds this) |
| 9 | Learning / Residue | Updated world model and residue field |

REE (Layer 6) is not the ethics itself. It is the machinery for acting ethically under
uncertainty. Ethics (Layer 5) is derived; the axioms (Layers 0-4) are foundational.
The learning loop (Layers 7-9) closes back to Layer 6, but the axioms are not themselves
updated by experience — they are the ground that makes experience interpretable.

---

## Open Questions

| ID | Question |
|----|---------|
| Q-025 | What actions are strictly forbidden by the five axioms, independent of context? |
| Q-026 | What actions are strictly required by the five axioms at all times? |
| Q-027 | What does "irreversible harm" mean under unavoidable uncertainty (Axiom 1)? |
| Q-028 | How should REE behave when axioms conflict (e.g., preserving self vs preserving others, when both cannot be achieved)? |
| Q-029 | Is loneliness — unshared suffering — an ethical harm category in its own right, derivable from Axiom 5? |

