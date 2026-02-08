# Daniel README — How This Project Is Sharpened Without Breaking It

This document exists to prevent a recurring failure mode:
rewriting the REE repository wholesale whenever a new insight emerges.

It is written for **me**, not for contributors or reviewers.

If you are reading this while feeling the urge to:
- restructure the repo again,
- rewrite the README to reflect a new insight,
- “clean up” architecture that suddenly feels wrong,

pause and read this first.

---

## The Core Problem This Solves

REE requires **architectural refinement under uncertainty**.

That means:
- insights arrive unevenly,
- biological inspiration precedes formalisation,
- correctness is more important than neatness,
- and premature coherence destroys novelty.

Historically, this has led to:
- repeated repo redrafts,
- loss of earlier good structure,
- flattening of speculative but valuable ideas,
- and exhaustion.

This document defines a **non-lossy refinement process**.

---

## The Three-Layer Rule (Non-Negotiable)

All work on REE must belong to **exactly one** of the following layers.

Confusion between layers is the source of almost all damage.

---

### Layer 1 — Invariant Claims (Very Slow)

These are the commitments that define what REE *is*.

Examples:
- Cognition is predictive, iterative, and multi-timescale
- There is a strict separation between representation (content) and regulation (control)
- Ethics emerges from constraint, not optimisation and this includes constraints on learning dynamics plus self other representational symmetry
- Stability, not maximal performance, is the primary viability criterion
- Runaway behaviour is a control failure, not a representational one
- Coherence includes temporal / phase binding, not just static metrics.
- Language is functional self-representation and joint attention, not a bolted-on module.

**Where these live**
- `README.md`
- `REE_CORE.md`

**Rules**
- These change rarely.
- Changing one invalidates large parts of the project.
- Do not update these impulsively.

If an insight threatens an invariant, treat it as a **major event**, not a tweak.

---

### Layer 2 — Mechanism Hypotheses (Fast, Allowed to Be Wrong)

This is where most thinking belongs.

Examples:
- Phase compatibility as an implementation of L-space coherence.
- Hippocampal rollouts as temporally structured binding traffic.
- Astrocyte-mediated regulation as slow spatial control.
- Language emergence via shared predictive control states.

**Where these live**
docs/hypotheses/
H_temporal_coherence.md
H_self_other_symmetry.md
H_language_emergence.md
H_mode_control.md

**What each hypothesis document must contain**
- What function this hypothesis is trying to explain.
- What biological inspiration motivates it.
- Which architectural components it would affect *if true*.
- What would falsify or weaken it.

**Rules**
- Hypotheses may overlap or conflict.
- Hypotheses may be wrong.
- Hypotheses do *not* require repo-wide changes.
- New insights go here first. Always.

If an idea feels exciting but disruptive, it belongs here.

---

### Layer 3 — Architectural Commitments (Medium Speed)

This is the “buildable” layer.

Examples:
- E1 / E2 / E3 interfaces.
- Control plane knobs and modes.
- Folder structure under `architecture/`
- Minimum spec in `REE_MIN_SPEC.md`.

1.	E1 is a predictive field, not a deep network
	•	Shallow, recurrent, multi-rate
	•	Iterative refinement over a shared latent space
	•	Columns as local predictive kernels
	2.	Explicit separation of planes
	•	Content plane (L-space, entities, errors)
	•	Control plane (precision, gain, clocks, plasticity)
This is now an architectural boundary, not just a conceptual one.
	3.	Entities as emergent but real variables
	•	Sparse, persistent, bindable structures
	•	Not forced symbols, but not denied either
	•	Error ownership is entity-linked
	4.	Control plane is first-class
	•	Not “attention layers”
	•	Not scalar “reward”
	•	Vector-valued knobs with partial locality

**Where these live**
- `architecture/`
- `docs/REE_MIN_SPEC.md`

**Rules**
- Architecture is updated only when a hypothesis has stabilised.
- Changes should be surgical, not sweeping.
- Prefer additive clarification over deletion.
- Always be able to point to *which hypothesis justified the change*.

If you can’t name the hypothesis you’re promoting, don’t change the architecture.

---

## The Sharpening Loop (Do This, Not Repo Rewrites)

When a new insight occurs:

### Step 1 — Capture Without Damage
Write a hypothesis document.
Do **not** touch architecture yet.

### Step 2 — Interrogate the Hypothesis
Ask:
- What does this replace, if anything?
- Is this necessary or one possible implementation?
- Does this change interfaces or only internals?
- Could REE survive without this?

AI agents are useful *here* — for interrogation, not rewriting.

### Step 3 — Promote Sparingly
If the hypothesis survives reflection:
- add **one or two sentences** to an architecture doc,
- add a reference to the hypothesis file,
- avoid global rewrites.

### Step 4 — Periodic Reconciliation
Only occasionally:
- review which hypotheses have been promoted,
- tidy architecture accordingly,
- delete nothing unless clearly superseded.

This prevents loss while allowing progress.

---

## Rules for Using AI on This Project

AI is a tool, not a co-author.

**Allowed uses**
- Stress-testing a hypothesis.
- Mapping a hypothesis to biology or computation.
- Identifying hidden assumptions.
- Proposing minimal interface changes.

**Disallowed uses**
- “Improve the architecture.”
- “Refactor the repo.”
- “Make this more conventional.”
- Any request that invites re-introduction of:
  - explicit moral scoring layers,
  - static coherence metrics,
  - LLM-on-top designs.

If AI output conflicts with REE invariants, the output is wrong.

---

## If You Feel Stuck or Discouraged

REE is not a content project.
It is a **constraint-driven architecture**.

Progress looks like:
- fewer but sharper commitments,
- hypotheses that survive longer,
- structure that resists erosion.

Do not optimise for visibility.
Optimise for correctness and falsifiability.

---

## Final Reminder (Read This Twice)

Do not rewrite the blade to sharpen it.

Preserve structure.
Protect speculation.
Promote slowly.
Delete reluctantly.

The architecture is allowed to be unfinished.
It is not allowed to be incoherent.