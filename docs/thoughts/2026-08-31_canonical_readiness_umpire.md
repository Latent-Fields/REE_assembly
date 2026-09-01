---
title: Canonical Readiness Umpire — Detecting When a Reference Organism Has Emerged
date: 2026-08-31
scope: full REE lineage
status: processed
---

Status: processed
Intake: evidence/planning/thought_intake_2026-08-31_canonical_readiness_umpire.md
Claims registered: GOV-UMPIRE-1


# Canonical Readiness Umpire — Detecting When a Reference Organism Has Emerged

## Core thought

REE needs a mechanism that can recognise when the accumulated evidence has reached the point where a canonical organism should be considered, without giving that mechanism the authority to declare an organism canonical.

The system should be able to recognise when the evidence warrants asking whether a canonical organism has emerged, while remaining structurally unable to answer that question by itself.

This is an umpire function rather than a ruler function.

The umpire does not decide what REE ought to become. It does not choose preferred architecture by optimisation score, promote mechanisms because they are fashionable, or declare that some arbitrary quantity of cognition is “enough.” It observes whether previously agreed evidential conditions have become true and, when they have, calls for the appropriate review.

The immediate motivation is REE-v3, where the mechanism for freezing a canonical profile already exists but the baseline remains an empty placeholder. The deeper principle applies to the entire REE lineage.

A future REE could become a coherent and increasingly competent organism through the accumulation and integration of mechanisms while its formal canonical record remained stale simply because nobody noticed that the threshold for an admission review had been crossed.

That should not be possible.

---

# 1. The problem

REE increasingly has two different kinds of progress.

The first is **mechanism progress**: a memory mechanism works, an avoidance mechanism bites, an action-conditioned prediction pathway becomes active, sleep modifies something useful, a control signal gains causal authority.

The second is **organism progress**: the same identifiable agent possesses multiple such faculties simultaneously and uses them together successfully over its life.

Those are not equivalent.

A collection of individually validated mechanisms distributed across many experiment-specific configurations is not yet a canonical organism.

Likewise, the existence of a canonical-profile mechanism does not mean there is yet a configuration worth canonising.

The transition we need to recognise is therefore not:

> enough mechanisms have been implemented.

It is closer to:

> enough mutually compatible, adequately evidenced mechanisms now coexist in an identifiable organism, and that organism has demonstrated sufficient integrated function that formal canonical-profile review has become scientifically meaningful.

The current governance machinery already contains much of what is needed to judge this once someone asks the question.

What is missing is the machinery that notices **it is now time to ask**.

---

# 2. Canonicality must not be a score

Canonical readiness should not be represented primarily as a percentage.

A single scalar such as:

> canonical readiness = 83%

would allow strengths in one subsystem to numerically compensate for absence of another essential faculty.

A sophisticated memory system cannot compensate for an organism that cannot perceive useful features of its environment.

Excellent prediction cannot compensate for an action pathway that never reaches behaviour.

A rich control plane cannot compensate for a policy that is not plastic.

Canonical readiness is therefore better represented as a set of explicit predicates or gates.

The detector should answer:

- what conditions are satisfied;
- what conditions are not satisfied;
- what evidence supports each judgement;
- what changed since the previous judgement;
- and whether that change warrants escalation.

This creates inspectable scientific state rather than a psychologically attractive progress number.

---

# 3. Proposed readiness states

The umpire should expose a small state machine.

## `NO_WARRANT`

There is not yet sufficient evidence to justify a canonical-profile admission pass.

This is not failure. It is simply the normal developmental state before the relevant conditions have converged.

The output should state why no warrant exists.

Examples:

- no identifiable recurring organism;
- relevant mechanisms have not been tested together;
- whole-organism behaviour is degenerate;
- learning pathways required by the evidence are not demonstrably plastic;
- integrated competence has not been demonstrated.

## `ADMISSION_PASS_WARRANTED`

A sufficiently coherent candidate organism or profile-shaped configuration now exists that running the existing canonical-profile admission procedure is scientifically worthwhile.

This does **not** mean that the candidate is canonical.

It means:

> there is now enough here to perform the formal admission work.

## `REFERENCE_ORGANISM_REVIEW_WARRANTED`

A reproducibly identifiable organism has demonstrated meaningful integrated organism-level competence.

At this point the question is no longer merely which mechanisms should enter a profile.

The repository should explicitly ask whether this organism should become the reference REE for its developmental stage or version.

## `USER_DECISION_REQUIRED`

The admission and qualification process has produced a draft profile, constitution, evidence dossier and caveats.

Canonical declaration now requires explicit human adjudication.

## `CANONICAL_OBSERVED`

A non-empty canonical profile has actually been approved and frozen through the authorised process.

The umpire may observe this state.

It must not create it.

---

# 4. Structural prohibition on self-canonisation

The most important safety and epistemic property is negative:

**the umpire must have no pathway that directly modifies or declares the canonical profile.**

It can:

- detect;
- derive;
- report;
- assemble evidence;
- recommend that an admission pass be run;
- generate a draft admission dossier;
- escalate a state transition.

It cannot:

- write admitted members into the canonical profile;
- declare a new canonical version;
- bypass the qualification battery;
- convert its own readiness state into canonical status;
- reinterpret failed gates as optional in order to cross the threshold.

The final transition to canonical status remains an adjudicated governance act.

This preserves an important distinction:

> the organism may eventually become capable of supplying evidence about itself, but it should not acquire authority to declare that evidence sufficient.

---

# 5. Gate A — Identifiable organism

Before asking whether an organism is canonical, the system must be able to say which organism it means.

A candidate should therefore be reconstructable.

Relevant information may include:

- substrate commit and hash;
- configuration values;
- default-off overrides;
- canonical-profile or candidate-profile fingerprint;
- developmental curriculum;
- initial conditions where scientifically relevant;
- architecture epoch;
- provenance of major learned state where persistence matters.

The umpire should determine whether successful experiments repeatedly involve:

1. an exact recurring configuration;
2. a fingerprintable configuration;
3. or configurations demonstrably equivalent with respect to the mechanisms under consideration.

If mechanism A succeeded in one animal, mechanism B in another and mechanism C in a third, this gate remains unsatisfied.

The current problem of experiment-specific REEs should become machine-visible rather than an interpretive caveat discovered during retrospective review.

A useful failure state would therefore be:

`NO_WARRANT: NO_IDENTIFIABLE_ORGANISM`

---

# 6. Gate B — Canonical-profile candidate substrate

The umpire should reuse the existing canonical-profile admission doctrine rather than creating a new definition of admissibility.

Candidate mechanisms should be assessed against the established dimensions, including:

- the substrate actually exists;
- it is genuinely exercised in the experimental corpus;
- supporting evidence traverses the real production pathway;
- enabling it does not catastrophically disrupt unrelated core function;
- known interactions with other candidate mechanisms have been examined;
- the underlying claim has reached the required epistemic status;
- bounded governance debt is tolerated rather than requiring artificial perfection.

Candidates may then be sorted into the already useful conceptual categories:

- canonical core;
- canonical but context-dependent;
- experimental substrate;
- diagnostic-only;
- deprecated or superseded;
- version-deferred.

The umpire does not itself admit the first two categories.

It detects whether there is now a sufficiently substantial and coherent set of plausible members that performing the admission pass is warranted.

---

# 7. Gate C — Coexistence

This may be the most important new detector.

Mechanisms should not be treated as composable merely because each works alone.

The system should explicitly ask:

> Have these faculties actually coexisted in the same organism?

A derived coexistence representation could record:

- mechanisms exercised together;
- mechanisms never yet combined;
- exact configuration overlap;
- approximate configuration overlap;
- known antagonistic interactions;
- unresolved interaction risk;
- combinations that have repeatedly produced non-degenerate behaviour.

A coexistence matrix or graph could make visible when experimental practice itself has begun converging on a recurring organism.

This creates the possibility of detecting a **proto-canonical organism** before anyone manually names it.

The important transition is:

> we are no longer repeatedly assembling different experimental animals; essentially the same animal keeps reappearing and surviving increasingly broad tests.

That should be recognised as evidence.

---

# 8. Gate D — Whole-organism non-degeneracy

A candidate reference organism should pass a cheap but meaningful whole-organism qualification.

At minimum the detector should be able to establish facts such as:

- the agent moves;
- observations contain meaningful variation;
- action selection has not collapsed to one trivial behaviour;
- required learning paths are actually plastic;
- expected memory systems are writable;
- relevant predictive streams vary meaningfully;
- candidate generation occurs;
- commitment pathways are reachable;
- actions can produce ecological consequences;
- no catastrophic numerical collapse or NaN state dominates;
- environmental anchors show that the world itself remains solvable.

This should integrate naturally with the developing capability/plasticity contract.

A long run is not developmental opportunity if nothing capable of changing is allowed to change.

The umpire should therefore distinguish:

> the organism failed to acquire the faculty

from:

> the instantiated organism could not possibly have acquired the faculty.

Canonical review should not be triggered by impressive-looking duration over a structurally non-plastic organism.

---

# 9. Gate E — Behavioural evidence

The existing Behavioural Evidence Ladder provides much of the conceptual structure required here.

A canonical admission pass need not wait until REE is finished.

Indeed, waiting for completion would defeat the value of having a reference organism during development.

The threshold for `ADMISSION_PASS_WARRANTED` could therefore occur while organism-level competence remains modest, provided that:

- the organism is identifiable;
- meaningful mechanisms are genuinely active;
- the combined organism is non-degenerate;
- at least some behavioural competence is attributable to that same organism;
- and the candidate configuration is scientifically worth qualifying.

A more consequential threshold exists when **integrated organism competence** is demonstrated.

When a single identifiable organism reaches the equivalent of Behavioural Evidence Ladder Rung 6 — several faculties demonstrably working together — this should trigger:

`REFERENCE_ORGANISM_REVIEW_WARRANTED`

That does not force canonisation.

It says:

> something qualitatively important has happened. A coherent organism now exists that deserves explicit consideration as the reference animal.

---

# 10. Gate F — Reproducibility

A lucky run should not define the species.

Canonical readiness should therefore require some form of replication.

For relatively fixed systems this may mean reproducing the same frozen configuration across:

- multiple seeds;
- repeated runs;
- different machines;
- equivalent environments.

As REE becomes genuinely developmental, exact mature internal states may cease to be the appropriate unit of replication.

The more biologically natural identity may instead become:

> the same constitution, starting architecture and developmental process reliably produce organisms with the relevant family of competencies.

This distinction should be preserved early.

A developmental REE should not eventually be forced into a concept of identity that assumes all mature learned weights must be identical.

The reproducible object may be the **developmental recipe and constitution**, not the adult state.

---

# 11. Derived artifact rather than new authority

The first implementation should probably be deliberately simple.

A deterministic tool could derive something like:

`canonical_readiness.v1.json`

alongside a human-readable:

`canonical_readiness.md`

The machine-readable artifact might expose:

- current readiness state;
- identifiable candidate organism(s);
- candidate canonical members;
- coexistence evidence;
- whole-organism qualification status;
- highest behavioural rung demonstrated by the same organism;
- plasticity/capability preflight status;
- reproducibility status;
- blocking reasons;
- newly changed predicates;
- previous readiness state.

The human-readable artifact should explain the verdict in ordinary scientific language.

For example:

> NO_WARRANT  
> The project contains multiple validated mechanisms but no recurring fingerprinted organism in which the relevant faculties have jointly demonstrated integrated competence. The strongest current behavioural evidence remains distributed across script-specific configurations.

Later this might become:

> ADMISSION_PASS_WARRANTED  
> A recurring fingerprinted configuration now contains 27 individually admissible or context-dependent mechanisms, has survived the whole-organism qualification battery across three seeds, and has demonstrated behavioural competence in two independent task families. Formal canonical admission review is warranted.

---

# 12. Escalate transitions, not persistent states

The detector should borrow the strongest property of REE's Steward architecture:

**persistent known conditions should not repeatedly consume attention.**

If the state remains:

`NO_WARRANT`

for fifty governance cycles, the system does not need to keep announcing that fact.

The interesting information is a transition.

Examples:

`NO_WARRANT → ADMISSION_PASS_WARRANTED`

should generate a prominent escalation.

Likewise:

`ADMISSION_PASS_WARRANTED → NO_WARRANT`

after an autopsy invalidates important evidence should generate:

**CANONICAL ADMISSION WARRANT WITHDRAWN**

This reversibility is essential.

Canonical readiness should remain scientific evidence state, not a milestone that becomes politically difficult for the system to retract.

The detector should therefore maintain enough prior derived state to distinguish:

- unchanged;
- newly satisfied;
- newly blocked;
- withdrawn;
- restored.

---

# 13. Admission dossier generation

When `ADMISSION_PASS_WARRANTED` fires, the system can reduce the cost of human adjudication without prejudging it.

It should assemble a candidate admission dossier containing:

- candidate organism fingerprint;
- complete proposed configuration;
- proposed canonical-core mechanisms;
- proposed context-dependent mechanisms;
- evidence lineage for each;
- production-path validity;
- coexistence evidence;
- interaction risks;
- qualification results;
- whole-organism behaviour;
- developmental and plasticity evidence;
- reproducibility evidence;
- unresolved governance debt;
- explicit limitations;
- failed or excluded candidate members.

The dossier then enters the existing canonical-profile admission process.

The process remains:

candidate detected  
→ admission pass  
→ qualification battery  
→ draft profile  
→ constitution  
→ explicit adjudication  
→ freeze if approved.

The umpire therefore becomes a **front door to the existing canonical system**, not a competing system.

---

# 14. Distinguish profile readiness from reference-organism readiness

Two thresholds should deliberately remain separate.

## Profile admission readiness

The project has accumulated enough stable, mutually compatible and evidenced substrate that it is useful to define a canonical reference configuration.

This can happen relatively early.

The resulting profile may contain substantial caveats and context-dependent mechanisms.

That is acceptable.

A canonical organism need not be a finished organism.

## Reference-organism readiness

A specific reproducible organism has demonstrated sufficiently integrated competence that the project should consider it the actual reference animal for that stage of REE.

This is a stronger event.

It is probably associated with genuine integrated organism competence rather than merely the existence of many admissible mechanisms.

Keeping the thresholds separate avoids two opposite errors:

- waiting far too long to create any useful canonical profile;
- prematurely interpreting a configuration file as evidence that a competent organism exists.

---

# 15. Full-lineage principle

Although the first implementation belongs naturally around REE-v3, this is not fundamentally a V3 mechanism.

Future versions may have:

- different faculties;
- different environments;
- social development;
- language;
- different embodiment;
- substantially more learned rather than architecturally supplied structure.

The specific readiness predicates will evolve.

The invariant should remain:

> REE should maintain an explicit, inspectable process for recognising when a reproducible organism has become sufficiently coherent and competent that formal reference-organism review is warranted.

The detector should therefore be version-aware but conceptually lineage-level.

---

# 16. What the umpire must not become

Several failure modes should be excluded from the design from the beginning.

It must not become:

### A progress optimiser

Its purpose is not to push the system toward whatever improves canonical-readiness fastest.

That would turn an observational measure into a target.

### A canonicality leaderboard

Competing configurations should not be reduced to one scalar and ranked as if canonical identity were a benchmark competition.

### A mechanism popularity detector

Frequent enablement is evidence of corpus practice, not evidence of scientific necessity.

### A self-certification loop

Evidence produced by the candidate organism must not automatically authorise the candidate organism.

### A completion detector

Canonical does not mean complete.

A canonical infant, juvenile or intermediate developmental organism may be scientifically useful and entirely legitimate if its limitations are explicit.

### An irreversible milestone

Readiness warrants may be withdrawn when new evidence invalidates their basis.

---

# 17. Likely implementation route

This thought should initially produce a small programme rather than a proliferation of architectural claims.

Likely components include:

1. a lineage-level governance principle covering canonical-readiness detection without canonical authority;
2. a deterministic readiness detector;
3. a machine-readable readiness artifact;
4. a human-readable report;
5. configuration/fingerprint coexistence analysis across experimental manifests;
6. integration with capability/plasticity preflight as that machinery matures;
7. a transition detector using the existing Steward-like “new information only” escalation principle;
8. an admission-dossier generator;
9. eventual integration into ordinary governance cycles.

The initial implementation should be conservative.

It is better for the first detector to say:

> I cannot yet determine this predicate.

than to infer green state from missing instrumentation.

Unknown, false and unmeasured should remain separate states.

---

# 18. Present expectation for REE-v3

At the time of this thought, REE-v3 has many causally active and individually evidenced mechanisms but does not yet possess a populated canonical baseline.

The behavioural record also does not yet establish robust integrated organism-level competence.

The expected immediate output of a Canonical Readiness Umpire would therefore be `NO_WARRANT`.

That is useful.

Unlike an empty canonical profile, the detector would explain *why* no warrant currently exists and would make changes in those reasons visible over time.

The value of the umpire is therefore not that it should soon announce success.

The value is that when the scientific state eventually changes, the project will not depend on somebody remembering to notice.

---

# 19. Core formulations

> **The system must be able to recognise when the evidence warrants asking whether a canonical organism has emerged, while remaining structurally unable to answer that question by itself.**

> **Canonical readiness is a set of gates, not a progress percentage.**

> **Mechanisms demonstrated in different experimental animals do not compose into a competent organism merely because they share a repository.**

> **The first important transition is not “the architecture is finished,” but “essentially the same animal keeps reappearing and surviving broader tests.”**

> **A canonical profile may legitimately precede a fully competent reference organism.**

> **A reference-organism review becomes warranted when an identifiable, reproducible REE demonstrates integrated organism-level competence.**

> **Readiness detection should escalate transitions, not repeatedly announce persistent known states.**

> **The umpire may call for adjudication. It may never adjudicate its own call.**

---

# 20. Summary

REE already contains increasingly sophisticated machinery for deciding whether individual claims and mechanisms deserve confidence.

It is beginning to contain machinery for defining a canonical organism.

What it lacks is the connective governance layer that notices when the evidence base itself has changed category.

The Canonical Readiness Umpire fills that gap.

It watches for convergence from distributed mechanisms toward one identifiable, reproducible organism. It checks whether the existing admission criteria have become meaningfully satisfiable, whether candidate faculties coexist without degeneration, whether developmental and learning pathways are genuinely available, whether behaviour belongs to the same organism, and whether integrated competence has appeared.

When those predicates change, it raises the flag.

Then it stops.

The scientific and constitutional decision remains outside the umpire.

We never needed a ruler.

For this problem, we need an umpire.
