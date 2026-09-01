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

> **FORK RESOLVED 2026-08-26** (thought-digestion wave 1, user-gated). The
> "fourth facet" reading is **withdrawn as a type error**: OBJ-1's facets
> (TYPE / ANCHOR / TOKEN) are coordinate descriptors *of a persisting particular* --
> properties the object HAS -- while USE is a *relation* between object and current
> internal state. The facets are stable under drive change; ARC-133's whole content is
> that drive change alters **how many object-files there are**, and a facet cannot
> determine how many bearers-of-facets exist. The tell: the fourth-facet reading is
> **already instantiated** as SD-057's `wanting[k]`, and instantiating it changed no
> carving. ARC-133 stands as the **primary-criterion** rival. A conservative landing
> zone already exists without inventing a facet -- OBJ-1 defers a
> "token-vs-type **individuation-strength** sub-fork" to the first OBJ-2 build step, and
> drive-modulated individuation strength is a third option there, at the right level.

**Substrate note (verified 2026-08-26):** `ree-v3/ree_core/entities/object_file_buffer.py`
**exists** (landed 2026-06-09, *after* ARC-080 was written -- so ARC-080's "the entire
layer is orphaned" text is stale) and **hard-codes MECH-278**: the association cost is
`w_motion * d_pos + w_feat * feat_term`, with `resource_tag` stored as `type_hint` but
never an input to the decision ("the key is continuity, not type"). ARC-133 is a rival to
**running code**, not to a design doc.

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

## MECH-521 -- settling-derived slot occupancy (mechanism-agnostic core) {#mech-521}

> **SPLIT 2026-08-26** (thought-digestion wave 1, user-gated). MECH-521 is now the
> mechanism-agnostic settling core; the ephaptic specialisation moved to **MECH-522**
> below and is ordered strictly after it. The split is load-bearing: fused, a
> 725a-shaped negative on the ephaptic leg would read as refuting the settling core,
> which it would not -- the exact function-vs-substrate conflation MECH-499/500's own
> scoping doc exists to prevent. Two further corrections applied: the
> `disinhibitory_soft_competitive_settling` machinery is the **structurally wrong site**
> (its elements are candidate *trajectories*, its kernel a discrete first-action-class
> surround, its readout a single argmin with no domain-count output, and its own
> divergence ledger records "no convergence guarantee", so "count the surviving
> attractors" is not well-defined on it -- what transfers is the algorithm *template*);
> and the **"third answer to Q-077" framing does not hold**, since Q-077 already names a
> hybrid third answer and is scoped to *goal* slots rather than perceptual grain.

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

## MECH-522 -- ephaptic field strength as the coupling constant {#mech-522}

Split out of MECH-521 on 2026-08-26. The field is **not the thing counted** -- it is the
**coupling constant** of the settling dynamic. A physical field does not enumerate
domains; it sets the interaction strength from which the domain count emerges, and
because coherence is a property of *each population separately*, a field-derived setter is
natively **heterogeneous** rather than imposing the single ordered abstraction axis that
Badre & Nee 2018 reports the evidence does not support. A **third** ephaptic function,
distinct from MECH-499 (what the now *contains*) and MECH-500 (*when* it is ready to
commit): at what **grain** the now is carved.

**The 725a caution is two-sided and must be carried whole.** V3-EXQ-725a failed its
coherence-specificity gate (1/6 seeds vs a 4/6 bar; 2 of 3 interpretable seeds
anti-specific) -- *but* the same `cross_stream_binder` substrate then had **MECH-456
promoted candidate -> provisional** on 2026-07-12 (V3-EXQ-733b PASS 6/6 + 733c replication
on disjoint seeds). So "the ephaptic-analog binder does no functional work" is false; what
725a killed is coherence-*specificity as a selection factor*, a different function on a
different readout from grain regulation.

## MECH-523 -- the compression sites are untrained {#mech-523}

Registered 2026-08-26 from digestion wave 2, after three independent agents each surfaced
one site. **Verified in source:** (a) `E2.action_object_head` receives **zero gradient** from
every REE path (SD-080) -- a frozen random projection, ~99.5% of its variance the action label;
(b) `beta_encoder` / `theta_encoder` / `delta_encoder` appear **zero times** in `agent.py`, have
no loss, no optimiser and no predictive head at any horizon, and are an untrained
random-projection cascade smoothed by one hardcoded `alpha_shared = 0.3`; (c) **no value-shaped
objective reaches any encoder** -- `compute_benefit_eval_loss` reads `z_world.detach()`.

**The corollary is methodological:** a null measured at an untrained compression site is
evidence about the absence of a training signal, not about the representation's capacity. SD-070
is the one worked instance and it went that way -- collapse measured at participation ratio
~1.06, a training recipe built, and V3-EXQ-783 then measuring trained PR 5.261 against a 0.50
retained-fraction floor.

**This reframes the thought this whole document came from.** The diagnosis was "abstract but not
funnelled". The measured situation is simpler: the funnels exist -- a bottleneck at O, a depth
cascade at z_beta/theta/delta -- and none is trained toward anything. There is no learning
pressure on the abstraction in the first place.

**Immediate consequence for ARC-004:** depth-equals-timescale has **never been measured**, and
ARC-004's own falsifier warns it could fail as MECH-058 did. With three untrained encoders
sharing one EMA constant, "one timescale wearing three labels" is the outcome to *expect*. A
per-layer autocorrelation half-life check (z_delta > z_theta > z_beta) is cheap and owed before
anything leans on the temporal spread.

## MECH-531 -- the P0 grain operator, minimal and v3-testable {#mech-531}

Split off ARC-134 2026-09-01 (GOV-V4CUT-1 F1, GFLAG-0101). ARC-134's own preconditions name a
**P0 gap**: no merge or split of `EntityObservation` tokens exists anywhere in
`ree_core/entities/object_file_buffer.py`, and matching is strict 1:1 greedy. MECH-531 asserts
only that a **corrigible** merge/split operator exists at **fixed capacity** -- no dynamic
per-population regulation, no settling competition -- responding to MECH-126's overmerge/
oversplit consequence-divergence evidence against a yoked random-regrain control. ARC-134's
richer demand-sensitivity claim (grain rescales with circumstance, the full L1-L3 ladder) and
MECH-521/522's settling-competition dynamics are unaffected and stay v4.

## MECH-532 -- pairing a compression site with a trained decompression stage {#mech-532}

Split off MECH-507 2026-09-01 (GOV-V4CUT-1 F2, GFLAG-0102). MECH-507's full E1/ContextMemory
reciprocal-bridge reframing stays v4 -- but the underlying pattern (a compression site paired
with a trained decompression/readout stage before ceiling-nulls measured there are
interpretable) is already partially built and separately registered as v3 work: SD-056 (E2's
trained world-forward decompression head, coded and default-off) pairs with SD-070's anti-
collapse encoder recipe at the z_world site, and the independent P4 training-debt cluster at
`E2.action_object_head`/O (SD-080, MECH-518, MECH-517) names the same repair owed at a second
site. MECH-532 states the general pairing requirement, satisfied by confirming it at either
site.

---

## Sequencing (nothing here authorises V3 work except MECH-518)

0. **MECH-521's derivational toy comes first and needs no REE substrate.** The
   "graceful degradation then whole-domain loss" signature is *asserted, not derived* --
   pattern formation gives domain count and size as functions of the control parameter,
   but the mapping from domain size to per-item *fidelity* is unargued. A ~20-line 1-D
   lateral-inhibition settling model can kill or confirm it before anything is built.
1. **MECH-518** is cheaply V3-testable now and settles how V3-EXQ-817a should be read.
   Proposal **EXP-0589** minted 2026-08-26; hand off to `/queue-experiment`.
   **Note the corrected instrument** -- `cand_world_pairwise_dist` routes through
   `world_forward` and cannot respond to this manipulation; use
   `pre_refit_first_action_entropy` + `cem_iteration_diagnostics[i].ao_std_*`, and add a
   matched `support_preserving_ao_std_floor=0.0` arm.
2. Grain-arbitration can be probed with **no ephaptic content**: MECH-288 already runs
   two segmentation scales in parallel with nothing arbitrating which is operative,
   and MECH-126's overmerge/oversplit supplies the DV.
3. Only then is the field-coupling question (MECH-521) worth commissioning, and only
   there does 725a bite.
