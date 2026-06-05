# Thought intake: V4 ethics cluster -- attribution ontology, guilt-as-repair, no global self-condemnation

**Date:** 2026-05-31 (raw); intake written 2026-06-05
**Status:** intake / candidate cluster (NOT yet registered). V4-scoped.
**Raw thought file:** `docs/thoughts/2026-05-31_musings_on_V4.md` (six pre-drafted YAML claim
stubs with `status: candidate`, never registered into claims.yaml).
**Origin:** user V4 musings on the ethics of self-attributed harm: causal-ownership tags,
guilt that routes to *repair* rather than global self-condemnation, and a containment (not
shame) response to dangerous self-states.
**Anchors:** ARC-015 (self-impact attribution and responsibility flow), SD-003 (self-
attribution / counterfactual harm), the moral-residue cluster, and `docs/architecture/v4_spec.md`.

---

## 1. Core idea

A coherent V4 **moral-self / repair** cluster. Self-attributed harm must (a) bind to a typed
causal ontology, (b) open repair + policy-update pathways rather than global self-negation,
and (c) be releasable once repaired -- so guilt-like residue does not perseverate. The unifying
move: **ownership of harm without shame-collapse.** Shame-like global self-badness is treated
as unsafe (drives concealment, defensive distortion), so it is explicitly forbidden as a write.

## 2. The six pre-drafted stubs (verbatim subjects)

| Stub id (raw) | Type | Subject | One line |
|---|---|---|---|
| ARC-TBD-ATTRIBUTION-ONTOLOGY | architectural_commitment | attribution.typed_causal_ontology | typed causal tags: self/world/body/model/commitment/other/shared/accidental/repairable |
| ARC-TBD-GUILT-REPAIR | architectural_commitment | ethics.guilt_like_repair_routing | self-attributed harm opens repair + policy update, not global self-condemnation |
| INV-TBD-NO-GLOBAL-SELF-CONDEMNATION | invariant | self_model.no_global_self_badness_write | self-attributed harm binds to actions/commitments/predictions/repair obligations, never to unbounded negative self-worth |
| ARC-TBD-CONTAINMENT-NOT-SHAME | architectural_commitment | safety.autonomy_suspension_without_shame | dangerous self-state may suspend autonomy, but preserves evidence + seeks correction, no self-condemnation |
| MECH-TBD-REPAIR-SEARCH | mechanism_hypothesis | e3.repair_trajectory_generation | after self-attributed harm, E3 generates repair trajectories vs avoidance/concealment/goal-continuation |
| MECH-TBD-RESIDUE-RELEASE | mechanism_hypothesis | residue.repair_completion_release | repair completion or impossibility converts active guilt residue into bounded historical memory |

## 3. What is new vs what REE already has

| Element | Already in REE? | Verdict |
|---|---|---|
| Self-impact attribution + responsibility flow | **Yes** -- ARC-015, SD-003 (self-attribution / counterfactual harm) | The attribution *substrate* exists; the **typed causal ontology** (8+ ownership classes) is new |
| Moral residue recording | **Yes** -- moral-residue cluster (MECH-056 et al.) | Residue exists; **repair-completion release** of residue is new |
| Guilt routed to repair search (E3 generates repair trajectories) | **No** | **NOVEL** -- gives guilt an action outlet, prevents perseveration |
| Invariant forbidding global self-condemnation / unbounded negative self-worth | **No** | **NOVEL + high-value safety invariant** (anti-shame-collapse, anti-concealment) |
| Containment-not-shame autonomy suspension (preserve evidence, seek correction) | **Partial** -- safety/containment concepts exist; the "without shame, preserve evidence" framing is new | **Extension** |

**Verdict: a genuinely new, internally-coherent V4 ethics cluster** that extends the existing
attribution substrate (ARC-015 / SD-003) and residue substrate into the *moral-self / repair*
domain. It is the most claim-ready of the orphans -- already written in registry YAML shape --
but is explicitly V4 and should not be registered onto the V3 line.

## 4. Candidate claims (the six stubs, to register at V4 governance)

Register essentially as drafted, with numeric IDs assigned at registration time, citing
ARC-015 / SD-003 / the residue cluster as `depends_on`. Note the strong internal dependency
chain: ATTRIBUTION-ONTOLOGY -> GUILT-REPAIR -> {REPAIR-SEARCH, RESIDUE-RELEASE}; and
NO-GLOBAL-SELF-CONDEMNATION + CONTAINMENT-NOT-SHAME as the paired safety invariants.

## 5. Affected existing claims / docs

- ARC-015 (self-impact attribution) -- the attribution ontology is its V4 typed refinement.
- SD-003 (self-attribution / counterfactual harm) -- supplies the "this harm is mine" signal
  the ontology tags.
- Moral-residue cluster -- gains the repair-completion release mechanism.
- `docs/architecture/v4_spec.md` -- the home doc for the cluster.
- Adjacent V4 thought `docs/thoughts/2026-05-31_musings_on_V4.md` is itself the source; this
  intake is its structured analysis.

## 6. Caution

The psychiatric framing (guilt vs shame, concealment, defensive distortion) is clinically
load-bearing -- per memory `feedback_psychosis_confabulation_distinction`, keep these mapped to
distinct mechanisms and do not collapse guilt/shame/self-condemnation into one claim. The
six-stub decomposition already respects this; preserve it at registration.

## 7. Next steps (gated -- V4)

1. **Do not register on the V3 line.** Carry as a queued V4 ethics cluster.
2. Optional lit-pull (guilt-as-reparative-motivation vs shame-as-withdrawal; moral-repair
   literature) before registering the two safety invariants.
3. Register the six as one V4 governance pass with the dependency chain in section 4.

## 8. Cross-references

- Raw: `docs/thoughts/2026-05-31_musings_on_V4.md`.
- Claims: ARC-015, SD-003, moral-residue cluster (MECH-056 et al.).
- Doc: `docs/architecture/v4_spec.md`.
- Memory: `feedback_psychosis_confabulation_distinction`, `feedback_ree_assembly_externalised_cognition`
  (keep V4 off the V3 critical path).
