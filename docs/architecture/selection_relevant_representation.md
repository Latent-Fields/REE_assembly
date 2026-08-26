---
title: "Selection-Relevant Representation (ARC-133/134, MECH-516..521)"
parent: "Attention, Binding & Objects"
grandparent: Architecture
nav_order: 10
status: candidate
status_asof: 2026-08-26
status_claim: ARC-133
---

# Selection-Relevant Representation

**Registered:** 2026-08-26
**Source thought:** [`docs/thoughts/2026-08-26_representation_authority_selection.md`](../thoughts/2026-08-26_representation_authority_selection.md)
**Intake:** [`evidence/planning/thought_intake_2026-08-26_representation_authority_selection.md`](../../evidence/planning/thought_intake_2026-08-26_representation_authority_selection.md)
**Session development (code-verified, with the SD-080 / V3-EXQ-817a correction):**
[`evidence/planning/representation_authority_selection_bottleneck_20260826.md`](../../evidence/planning/representation_authority_selection_bottleneck_20260826.md)

> **DOC + GOVERNANCE ONLY.** No substrate, no experiments, no V3 behaviour change.
> Every claim here is `candidate`. Several are deliberately **mutually exclusive
> with existing claims** and registered anyway, so that experiment and literature
> can adjudicate rather than the registering session (user instruction, 2026-08-26).

---

## The thesis

Representation, authority and selection are one bottleneck rather than three. REE
currently carves its world along three axes -- objects by **causal coherence under
intervention** (MECH-278), episodes by **prediction error / changepoint**
(MECH-288), latent depths by **timescale** (ARC-004) -- and computes value *on top
of* all three, at E3. None of the three carvings is indexed by *why the thing
matters*. These claims propose that selection-relevance is itself a legitimate
individuation criterion, name the interface failure that would hide it, and supply
the anti-collapse constraint without which the proposal degenerates.

---

## ARC-133 -- selection-relevance as an object-individuation criterion {#arc-133}

An object may be individuated by what it is FOR. Explicitly **rival to MECH-278**
(causal feature-bundle under intervention), and the two disagree on real cases:
causally-identical-but-functionally-distinct items (two berries, different
nutritional axes) are one object under MECH-278 and two under ARC-133;
causally-distinct-but-functionally-identical items (a hazard that bites, a hazard
that falls) are two under MECH-278 and one under ARC-133. The sharpest divergence is
**drive-relative re-individuation**: under ARC-133 the same world carves differently
when hungry vs thirsty vs injured, which a causal criterion cannot deliver and which
is exactly what MECH-359 says selection needs.

The conservative reading makes it a **fourth facet** coregistered under ARC-080's
OBJ-1 resolution (type / anchor / token / **use**); the radical reading makes it
primary and demotes causal coherence to evidence for it. Not resolved here.

## ARC-134 -- dynamic regranularisation of PERCEPTUAL grain {#arc-134}

ARC-069 already commits REE to dynamic granularity **for policy** -- "the unit-of-policy
... is itself a dynamic representation, not a fixed primitive", because a fixed
grain "may be too fine (combinatorial explosion in rollout) or too coarse (chunks
fail to map onto the actual state)". ARC-134 asserts the identical argument for
**perception**: the unit-of-percept is dynamic, not fixed. The rationale transfers
axis-independently; REE simply never made the commitment on this axis. The
perceptual cell is empty -- a part-whole search over `claims.yaml` returns zero
claims, and ARC-080 defines what an object *is* without saying at what grain objects
are individuated or that the grain moves.

## MECH-516 -- graded value, categorical interface {#mech-516}

The recurring structural failure: value structure is computed **gradedly** and
delivered to its consumer **categorically**, so the gradient dies at the interface.
Instances: `wanting[k]` over all objects collapsed by `most_wanted()`'s **argmax**
into one z_goal (code-verified); MECH-319's **binary** replay WHETHER-gate, which
"says nothing about ordering among the replayed transitions it admits"; MECH-294's
`ThetaPacket` **fixed-arity dataclass**; and the O-space **decoder** whose "argmax
pins to one constant class". Distinct from MECH-359 (the *signal* must carry
per-candidate range) and MECH-463 (a *global scalar* amplifies the incumbent):
MECH-516 is about range that **existed upstream and was destroyed at the boundary**.

## MECH-517 -- interface before representation (ordering) {#mech-517}

**Rival to the standing differentiate-first ordering** (INV-088 / MECH-458's
"ordering-gated on INV-088 z_world differentiation"). A representation improvement is
**undetectable through a collapsing interface**, so representation-side experiments
run before the interface is fixed return uninterpretable nulls. V3-EXQ-817a is the
worked instance: grounding verifiably took (r^2 0.995 -> 0.721, shuffled control
clean) and behaviour did not move. Differentiate-first reads that as "consequence
structure does not help"; MECH-517 reads it as "the measurement could not have
detected help". Discriminating test: re-run an 817a-shaped grounding contrast
*through* a non-collapsing interface.

## MECH-518 -- one tensor, two masters {#mech-518}

`E2.action_object_head`'s output O is simultaneously the **semantic compression**
(what `o_t` means) and the **search coordinate system** the hippocampal CEM samples
in (`ao_mean + ao_std*noise`, decoded to actions). An objective that improves the
first can degrade the second by reallocating a shared, fixed budget -- O's variance.
Measured in V3-EXQ-817a: `ao_M5_r2_explained_by_action_alone` fell 0.995 -> 0.721,
i.e. ~28% of O's variance moved out of action-coding, while the consequence-ordering
metric M6 stayed weak and sign-unstable (mean ~+0.12, negative on 2/5 seeds). Cheap
decisive check: record per-candidate proposal diversity (`cand_world_pairwise_dist`)
under ARM_0 vs ARM_1. **This claim is V3-testable today.**

## MECH-519 -- epistemic value is episode-borne, not object-borne {#mech-519}

Consummatory and harm value attach to **objects** (SD-057's
`base_value[k] * (1 + kappa * drive_axis[k])`); epistemic value attaches to
**episodes**, as **gain x need** (MECH-443, Mattar & Daw 2018), because a model is
wrong about *transitions*, not about *things*. This predicts there is no epistemic
"benefit pulse" to bind to an object identity, and explains why adding an epistemic
axis to SD-049's per-axis drive has no natural write rule. Distinguished from
MECH-388 (epistemic pressure on *actions* under partial observability), MECH-314b (a
reward *bonus* over states) and MECH-443 itself (the write-priority *mechanism*);
MECH-519 is a **carrier** claim about which structure holds the quantity. Rival
reading -- that epistemic value is object-borne like nutritive value -- is live and
deliberately not suppressed.

## MECH-520 -- predictive obligation as representational anti-collapse {#mech-520}

A representation compressed toward selection-relevance ALONE degenerates: value is a
near-scalar projection, so a pure value-carving objective admits a solution that
discards everything not currently useful. Requiring the higher-order latents to
remain **predictive across the ARC-004 temporal spread** is an anti-collapse
constraint that a value-only objective lacks -- cross-horizon prediction demands
retained state structure that value alone does not. Distinct from **ARC-088**
(anti-collapse at the *behavioural/evaluator* level, plural evaluators preventing
behavioural monostrategy) and from **SD-070** (a specific VICReg-style
variance/covariance *training recipe* for z_world). REE precedent that the risk is
real: SD-070 exists because z_world was measured collapsing to participation ratio
~1.06 at world_dim=128. Related: **INV-091**'s viable band (too little shared
organisation is fragmentation; too much is representational collapse) -- MECH-520
proposes a mechanism for staying below the upper wall.

## MECH-521 -- settling-derived slot occupancy; the field as coupling constant {#mech-521}

Perceptual slot count is **not** read off coherence by counting "related
coherencies" -- that is circular, since the relatedness criterion IS the grain
decision, and coherence nests rather than partitions. Instead: occupancy is an
**emergent order parameter** of a settling competition (coupling vs lateral
inhibition), bounded above by the **carrier ratio** (Lisman & Jensen theta/gamma
capacity ~ slots x phase-bins). **Capacity and occupancy are distinct regulators**
and must not be collapsed. Ephaptic field strength enters as the **coupling
constant** of that settling dynamic, not as a quantity that is measured and counted
-- which is what a physical field natively supplies, and which is heterogeneous by
population rather than imposing the single ordered abstraction axis Badre & Nee 2018
says the evidence does not support.

**Third answer to Q-077** (slot-vs-resource for SD-046's multi-slot GoalState):
coupling is a continuous *resource*, settling turns it into discrete *attractors*,
so discreteness is emergent from a resource and neither is primitive. Discriminating
signature: capacity degrades gracefully (resource-like) up to a point, then loses a
whole domain (slot-like). REE already has the settling machinery --
`disinhibitory_soft_competitive_settling` (MECH-140 x MECH-450, implemented
2026-07-02) -- built for **selection**, not perception.

**Standing caution:** V3-EXQ-725a, REE's one ephaptic-analog test, FAILED its
coherence-specificity gate (1/6 seeds vs a 4/6 bar; 2 of 3 cleanly-interpretable
seeds anti-specific). It tested coherence as a *binding* signal, not as a *grain*
regulator, but anyone proposing ephaptic work carries it.

---

## Sequencing (nothing here authorises V3 work except MECH-518)

1. **MECH-518** is cheaply V3-testable now and settles how V3-EXQ-817a should be read.
2. Grain-arbitration can be probed with **no ephaptic content**: MECH-288 already runs
   two segmentation scales in parallel with nothing arbitrating which is operative,
   and MECH-126's overmerge/oversplit supplies the DV.
3. Only then is the field-coupling question (MECH-521) worth commissioning, and only
   there does 725a bite.
