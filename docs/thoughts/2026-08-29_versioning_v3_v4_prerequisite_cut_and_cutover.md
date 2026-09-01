Status: processed
Intake: evidence/planning/thought_intake_2026-08-29_versioning_v3_v4_prerequisite_cut_and_cutover.md
Claims registered: GOV-V4CUT-1

Original status line: raw thought intake

Date: 2026-08-29
Scope: REE version ontology; V3 qualification; V3→V4 transition governance
Authority: exploratory programme thought; does not itself alter version routing, claim status, closure requirements, or release policy
Processing note: preserve the distinction between organism/design generation and evidential closure. The proposed V4 prerequisite cut is an action to derive from the live claim/capability graph, not something asserted as already complete.

# Versioning, the V3→V4 prerequisite cut, and the cutover problem

## Originating problem

A fence-post ambiguity has emerged in the way REE version numbers are being used.

Two different concepts have been allowed to share the same labels:

1. **the organism/design generation** — what REE-v3 or REE-v4 is architecturally intended to instantiate; and
2. **the evidential closure state** — how well the claims associated with that generation have been causally, behaviourally and experimentally validated.

These are related, but they are not the same thing and should not be forced to finish at the same moment.

A version number should primarily name an **organism/design generation**. Closure should describe **how well that generation has been validated**.

This resolves an otherwise unstable pair of interpretations:

- "V4 starts when the V3 closure map reaches 100%."
- "V4 is only complete when the V4 closure map reaches 100%."

If both are allowed, the version boundary moves depending on whether the label is being used prospectively for architecture or retrospectively for proof.

## V3 now appears to have at least two distinct milestones

The current programme state suggests that REE-v3 should not be treated as having a single all-or-nothing completion event.

### Milestone 1 — the V3 design objective

> **Viable minimal working intelligence achieved; causal/ablative validation of the responsible architecture remains incomplete.**

This marks the point at which the V3 organism has achieved its defining design objective: a minimally viable artificial intelligence with enough learned, integrated and behaviourally expressed competence to be treated as an experimental organism rather than merely an unfinished candidate architecture.

It does **not** mean every V3 claim is closed.

### Milestone 2 — V3 qualified as the prerequisite substrate for V4

A second milestone is required before V4 can be trusted as an informative next organism generation:

> **The V3 instantiation has become sufficiently solid in the specific capabilities that V4 assumes that V4 development can begin without routinely confounding inherited V3 defects with genuinely new V4 phenomena.**

This milestone should not be defined by total V3 closure.

Instead it should be defined by the subset of V3 capabilities and claims that are genuinely **load-bearing prerequisites for V4**.

## The V4 prerequisite cut

The transition problem can be formalised as a dependency-cut problem.

The **V4 prerequisite cut** is the smallest transitive set of V3 capabilities/claims whose truth or functional adequacy is assumed by V4.

The current V3 closure map contains several different kinds of work that should not automatically be treated as equally blocking for V4:

- **inherited capabilities** that V4 genuinely needs;
- **validation of inherited capabilities**, where the capability carries forward but the exact V3 assay does not;
- **V3-specific experimental harnesses, calibration and diagnostic campaigns**;
- **scientific characterisation debt** that remains worth studying in V3 but is not load-bearing for V4;
- **superseded or ecology-limited questions** that may become better posed in V4;
- **work already better understood as V4-leaning or later-version architecture**;
- **orphaned prerequisites or dependency-routing defects** that require explicit ownership rather than being silently absorbed into a version boundary.

Therefore:

> **Version membership is not the same thing as inheritance, and inheritance is not the same thing as closure membership.**

A V3-aligned node can remain scientifically open without preventing V4, provided V4 does not depend on it or its failure mode is sufficiently bounded and observable.

Conversely, a apparently small V3 uncertainty may need to block V4 if it sits on a load-bearing causal path and would make later behaviour uninterpretable.

## Proposed cutover criterion

V4 should become **developmentally admissible** when every load-bearing V3 prerequisite is in one of two states:

1. **sufficiently demonstrated** to be trusted as a substrate for richer development; or
2. **bounded and instrumented**, such that its known failure mode can be detected and distinguished from V4-specific effects.

A second condition should also hold:

> **Remaining V3 uncertainty is unlikely to reveal a missing architectural foundation that would invalidate the interpretation of V4.**

This is deliberately stronger than "V3 works" and deliberately weaker than "V3 is completely proven."

The qualification milestone is therefore not a percentage threshold. It is a statement about the **location and nature of residual uncertainty**.

## The cutover has symmetric risks

There is a real risk in moving both too early and too late.

### Cut over too early

If V4 begins before the load-bearing V3 prerequisite substrate is sufficiently understood:

- hidden V3 defects can become embedded in richer V4 behaviour;
- increased ecological and architectural complexity can make those defects much harder to localise;
- inherited failures may masquerade as novel V4 phenomena;
- later experiments may become uninterpretable because a prerequisite faculty was never actually stable;
- development may accumulate compensatory machinery around an avoidable V3 defect.

The result can be apparent progress with degraded scientific legibility.

### Cut over too late

If V4 is held until every V3-aligned node is closed:

- V3 can become an endless validation sink;
- increasingly narrow calibration and harness-specific questions can dominate programme time despite having little bearing on the next organism generation;
- questions requiring richer objects, affordances, ecologies, agents or developmental demands may be impossible to pose properly in V3;
- the simple V3 environment may itself become the limiting instrument;
- effort can be spent proving properties of a test vehicle rather than learning about the architecture.

The result can be apparent rigour with declining scientific return.

The optimal cutover is therefore likely to be a **window**, not a point defined by arbitrary percentage closure.

## Consequence for parallel version work

Once the V3 qualification milestone is crossed, the programme can legitimately occupy two states at once:

- **V3 remains the validated/simple experimental reference organism**, with continuing ablation, characterisation and mechanism-isolation science where useful;
- **V4 becomes the active development organism**, introducing the richer ecology and capacities needed for the next scientific questions.

This is not inconsistent versioning. It follows naturally once architecture generation and validation state are represented separately.

The programme sequence becomes:

**V3 design objective achieved**  
→ **V3 prerequisite substrate qualified for V4**  
→ **V4 architectural development begins**  
→ **V3 validation continues independently where scientifically useful**.

V3 need not disappear when V4 starts. Its comparative simplicity may make it permanently useful as an experimental animal for regressions, lesions, mechanistic isolation, and reproducing earlier findings.

## Proposed classification for unresolved version-aligned work

To make the cutover machine-auditable rather than intuitive, unresolved nodes should eventually gain a derived classification such as:

- `inherited_prerequisite`
- `validation_of_inherited_capability`
- `v3_only_characterisation`
- `v3_harness_or_calibration`
- `diagnostic_debt`
- `superseded_or_reposed_by_v4`
- `v4_or_later_architecture`
- `orphan_or_dependency_defect`

These labels should preferably be a **derived projection over existing claims/plans**, not a second hand-maintained source of truth.

The important generated view would answer:

> **Which unresolved V3 nodes are actually on a transitive dependency path to V4, and which are not?**

That set — not the entire V3 closure map — should define the hard scientific gate for the V3→V4 qualification milestone.

## Required follow-on work

### 1. Derive the V4 prerequisite cut

Traverse the live claims, plans, developmental requirements and architecture assumptions to identify the smallest set of V3 capabilities that V4 genuinely presupposes.

Do not infer this merely from `phase: v3` / `phase: v4` labels. The investigation should distinguish architectural dependence from historical placement in the work graph.

### 2. Classify current residual V3 work against the cut

For each unresolved V3 node, determine whether it is:

- genuinely load-bearing for V4;
- evidence needed to qualify a load-bearing capability;
- useful but non-blocking V3 science;
- a V3-specific assay/harness/calibration;
- better reposed in V4;
- superseded;
- or an orphan/dependency defect.

### 3. Define qualification evidence per prerequisite capability

For every load-bearing capability, specify what is enough to carry it across the boundary. This need not always mean complete causal closure.

Possible qualification states should include:

- robustly demonstrated;
- causally localised sufficiently for inheritance;
- known limitation with reliable detection;
- unresolved and therefore blocking.

### 4. Add a cutover review rather than a percentage gate

The V3→V4 transition should be adjudicated by a dedicated review of the prerequisite cut and the residual-risk structure, not automatically by reaching an arbitrary global closure percentage.

The review should explicitly ask:

- What V3 failures could still make V4 behaviour uninterpretable?
- Are those failures detectable in V4 if they occur?
- Is any remaining V3 question more likely to be answered by richer V4 ecology than by further V3 work?
- Is V3 still exposing foundational architecture defects, or mostly calibration, characterisation and known ceilings?

## Working principle

The central principle is:

> **Do not require V3 to be fully closed before V4 begins. Require V3 to be sufficiently qualified in exactly the things V4 needs.**

Or, equivalently:

> **The version boundary should follow architectural generation; the scientific cutover should follow prerequisite qualification.**

This preserves both forms of rigour: it avoids building V4 on unknown foundations without turning V3 into a permanently unfinished validation programme.
