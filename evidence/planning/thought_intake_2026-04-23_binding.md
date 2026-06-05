# Thought intake: binding as dynamic coherence under uncertainty

**Date:** 2026-04-23 (raw); intake written 2026-06-05
**Status:** intake / candidate refinement (NOT yet registered)
**Raw thought file:** `docs/thoughts/2026-04-23_binding.md`
**Origin:** user reframing of the binding problem -- binding is not a fixed assignment of
features to entities but a dynamically maintained coherence that persists only while
mutually consistent across prediction, perception, and time. "What belongs together is what
continues to make sense together."
**Anchors:** ARC-006 (entities.binding), Q-001 (entities.emergence_mechanism), MECH-044
(hippocampal relational binding), INV-002 (coherence includes temporal/phase binding),
INV-012 (coherence), MECH-269 (verisimilitude / regional anchor) -- all already in the
registry; this thought *refines the mechanism* rather than opening new territory.

---

## 1. Core idea

Binding = the persistence of a configuration under ongoing cross-system constraint checking
(E1 prediction x E2 transition x sensory input), with selection probability
`P(tau) ~ exp(-beta E(tau)) * C(tau)` where `E` is integrated prediction error and `C` is
cross-system coherence. Identity is *maintained, not intrinsic*: an entity persists as long
as its coherence persists. Misbinding is expected and useful (drives exploration/rebinding).

## 2. What is new vs what REE already has

| Element | Already in REE? | Verdict |
|---|---|---|
| Binding is coherence-based, not slot-assignment | **Yes** -- INV-002 ("coherence includes temporal/phase binding, not just static metrics"), ARC-006 (entities.binding, `entities_and_binding.md`) | Confirms / restates existing position in cleaner form |
| Hippocampal rollout generates competing binding hypotheses; verisimilitude filters them | **Yes** -- MECH-044 (hippocampal relational binding), MECH-269 (verisimilitude anchor), ARC-018 (rollout) | Confirms; thought sequences them into one pipeline |
| Offline/sleep defines "what tends to belong together" (clusters co-occurring features) | **Partial** -- sleep consolidation exists (SD-017); "binding-prior formation during replay" is not separately stated | Minor extension |
| Continuous rebinding under perturbation as a *requirement* (not just a capability) | **Implicit** | Sharpening worth a test |
| Identity-as-persistence-of-coherence (no hard binding) | **Yes** -- consistent with object-file persistence (MECH "object_file_persistence") and the object-representation thread | Confirms |

**Verdict: this is mostly a clean restatement + sequencing of REE's existing coherence-based
binding stance, not a new mechanism.** Its incremental value is (a) the explicit five-stage
decomposition (offline structuring -> E1 representation -> hippocampal candidate generation
-> verisimilitude filtering -> E3 commitment) and (b) the falsifiable predictions.

## 3. Falsifiable content (the part worth keeping)

The thought states its own failure conditions, which is unusually testable:
- Unsupported if binding is fully explained by static assignment.
- Unsupported if coherence reduces to prediction-error weighting alone (i.e. `C(tau)` adds
  nothing beyond `E(tau)`).
- Unsupported if no dynamic rebinding is observed under perturbation.

This connects directly to the path-integral thought of the same day
(`thought_intake_2026-04-23_path_integral_constraints_search.md`): **both hinge on whether
`C(tau)` is non-reducible to `E(tau)`.** They should be tested by one experiment, not two.

## 4. Candidate claims / refinements

- **Refine ARC-006** with the coherence-persistence formulation and the "identity = maintained,
  not intrinsic" framing (likely an evidence/wording update, not a new claim).
- **Candidate Q** (entities.coherence_nonreducibility): does a coherence term `C(tau)` alter
  binding selection independently of prediction-error magnitude? -- shared discriminator with
  the path-integral intake.
- **Candidate MECH** (rebinding-under-perturbation): the system must monitor coherence and
  rebind when a competing configuration overtakes the current one in `exp(-beta E) * C`.

## 5. Affected existing claims / docs

- ARC-006, Q-001, MECH-044 (`docs/architecture/entities_and_binding.md`) -- primary home.
- INV-002 / INV-012 (coherence definition).
- Object-representation thread (memory `project_object_representation_thread`): this binding
  framing is one of the three object lineages that thread proposes to spine together; note the
  cross-link there rather than registering a competing lineage.

## 6. Next steps (gated)

1. Fold the coherence-persistence wording into ARC-006's evidence note (low risk; no new claim).
2. Decide whether the `C(tau)` non-reducibility question is worth a discriminative experiment
   -- if so, design it *jointly* with the path-integral intake (single coherence-ablation run).
3. Route through the object-representation-thread decision rather than as a standalone claim.

## 7. Cross-references

- Raw: `docs/thoughts/2026-04-23_binding.md`; same-day sibling
  `docs/thoughts/2026-04-23_path_integral_constraints_search.md`.
- Claims: ARC-006, Q-001, MECH-044, INV-002, INV-012, MECH-269, ARC-018.
- Memory: `project_object_representation_thread`.
