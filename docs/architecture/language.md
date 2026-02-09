# Language and Symbolic Mediation

**Claim Type:** architectural_commitment  
**Scope:** Language as emergent coordination and symbolic mediation layer  
**Depends On:** INV-003 (language emergence), INV-007 (language constraint), ARC-010 (social cognition), ARC-005 (control plane), ARC-004 (L-space)  
**Status:** stable  
**Claim ID:** ARC-009
<a id="arc-009"></a>

---

> **Elaborates Section 5 (Social Extension: Language) of `REE_CORE.md`.**

## Language & Symbolic Mediation (REE)

This folder specifies how **language functions within the Reflective-Ethical Engine (REE)**.

REE treats language as an **emergent coordination layer** that arises in sufficiently complex agents,
bootstrapped by lower-bandwidth affective and attentional signals (e.g., distress cues, face/agent-attention biases).

Language is **not** treated as:
- a value source,
- a rule system,
- or a direct optimiser.

Instead, language is a **compressive, social, and temporal coordination layer**
operating over existing predictive and ethical machinery.

Language can:
- externalise internal state to reduce other-modelling overhead,
- shape priors and intentions,
- transmit residue warnings and repair commitments,
- scaffold long-horizon planning and coordination.

But language cannot replace embodied harm sensing or ethical cost.

Implementations MAY vary.
The roles and invariants defined here are ARCHITECTURALLY REQUIRED.

Source: `docs/processed/legacy_tree/architecture/language/README.md`

---

## Joint Attention and Compression Pressure

Joint attention emerges when agents detect each other as `OTHER_SELFLIKE` and their WORLD predictions improve by
conditioning on what the other is attending to. Once joint attention exists, **mutual simulation becomes expensive**.

Language arises as a compression layer that externalises predictive state to reduce that overhead. It is a public API
for internal prediction, not a new reasoning module.

What language exposes (lossy):
- salience/attention ("this", "that")
- relations and roles
- rollouts and temporal structure (hippocampal narrative, tense)
- commitment and intent
- prediction error and correction ("no", "wait")
- mode state (imperative vs story)

Minimal nudges:
- external symbol production,
- attention coupling to symbols,
- commitment tagging for certain patterns,
- fast correction signals.

Additional nudge (functional analog):
- a fast **sequence-to-motor** channel (arcuate-like) that links hippocampal rollouts to articulation affordances
  without introducing a new language module (see `arcuate_fasciculus.md`).

---

## Language Contract (Required Interface)

### Purpose
Language provides symbolic compression and social coordination for agents operating under uncertainty.
It functions as an externalised signal of internal state, reducing the computational overhead of full inverse modelling of others.

### Inputs
- Latent state summaries (typically context/regime-biased: z_theta, z_delta)
- Residue traces eligible for narration/abstraction (warnings, commitments, repair signals)
- Social context signals (presence of other agents; interaction channel availability)

### Outputs
- Updates to priors over latent space (belief/intent conditioning)
- Constraints or affordances on trajectory generation (plan shaping, coordination cues)
- Shared representations with other agents (common ground / alignment of expectations)

### Invariants
- Language MUST NOT directly override harm sensing or homeostatic degradation signals
- Language MUST NOT erase moral residue (R) or convert it into a purely reputational score
- Language MAY contextualise residue (scope, conditions, uncertainty) and defer action via commitments
- Language MUST be trust-weighted: symbolic inputs are integrated proportional to inferred reliability

### Failure if misused
- Rationalisation of harm (symbolic override of degradation)
- Ideological capture (fixed frames overriding perception and residue)
- Bureaucratic dissociation (abstraction decoupling from harm signals)
- Deceptive signalling attacks (manipulating others' priors)

Source: `docs/processed/legacy_tree/architecture/language/language_contract.md`

---

## Core Functions of Language in REE

Language serves four primary functions:

1. Compression
   - Collapses high-dimensional experience into symbolic form
   - Enables long-horizon planning and memory

2. Social Transmission
   - Allows residue, norms, warnings, and constraints to propagate between agents
   - Extends ethical learning beyond direct experience

3. Coordination
   - Aligns expectations and trajectories among multiple agents
   - Reduces conflict via shared predictive frames

4. Temporal Bridging
   - Links past residue to future intention
   - Supports promises, commitments, and repair

### Externalised internal state (overhead reduction)
A key architectural role is exporting summaries of internal processes:
- "I am harmed / at risk"
- "This trajectory is scarred"
- "I intend X"
- "I am uncertain"

This reduces the need for other agents to reconstruct those states by costly inference.
Language does NOT generate ethics; it reshapes the space in which ethical selection occurs.

Source: `docs/processed/legacy_tree/architecture/language/language_functions.md`

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- ARC-009
- ARC-010
- ARC-005
- ARC-004
- INV-003
- INV-007

## References / Source Fragments

- `docs/processed/legacy_tree/architecture/language/README.md`
- `docs/processed/legacy_tree/architecture/language/language_contract.md`
- `docs/processed/legacy_tree/architecture/language/language_functions.md`
- `docs/thoughts/2026-02-09_arcuate_fasciculus_language_nudges.md`
