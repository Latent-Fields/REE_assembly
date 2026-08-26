# The representation -> authority -> selection bottleneck

**Date opened:** 2026-08-26
**Session:** `insights-7fd98a` (Remote Control; exploratory)
**Status:** EXPLORATORY DEVELOPMENT OF A USER THOUGHT. **Registers nothing.** No
`claims.yaml` entry, no queue entry, no substrate change, no promotion. The
synthesis below is offered for the user to accept, revise or reject.


## TL;DR (the four things worth your time)

1. **Your principle is already registered** as MECH-359 ("for proto-affect to
   carve behaviour it must carry per-candidate range, not merely per-tick
   magnitude") -- parked as `substrate_conditional`, do-not-build-in-V3. What is
   NOT registered is your *criterion*: that an object is individuated by **what
   it is useful for**. MECH-278 currently individuates objects **causally**;
   MECH-288 carves episodes by **prediction error**; ARC-004 stratifies latents
   by **timescale**. None of the three is indexed by why it matters. (S1, S3)

2. **Code-verified finding.** REE holds two ranked, revaluable, drive-conditioned
   multi-item value stores -- `IncentiveTokenBank` (per object) and
   `GhostGoalBank` (per anchor) -- and **neither delivers a multi-item comparison
   to the E3 committed selector.** One is collapsed by `most_wanted()`'s argmax
   into a single z_goal; the other feeds proposal, not scoring. The value index
   you are asking for **exists today, one layer deep, wired to something other
   than the selector.** (S2, S2.1)

3. **The pattern I think is the real finding, and the one I am least sure of.**
   The same move happens three times independently: graded value computed, then
   delivered categorically -- objects via argmax, episodes via MECH-319's binary
   write gate, affect via one uniform scalar (measured cross-candidate spread
   **0.0** across ~3182 ticks). If that reading holds, three months of authority
   work has been trying to *manufacture* downstream a differentiation that was
   *discarded at the interface*. That makes it plumbing
   (`complicated (buildable)`), not tuning. (S2.3 -- with its own post-diction
   checks and their limits)

4. **One cheap probe would settle a lot**, and needs no new representation: replace
   the argmax with a soft, wanting-weighted read over the whole bank --
   "per-candidate value = how close this brings me to each thing I have stored,
   weighted by how much I want it given my current interoceptive state". ~10
   lines over tensors that already exist, dimensionally verified, bit-identical
   when off, does not touch z_goal or MECH-346. DV is *spread*, not behaviour.
   **A null kills the object framing cheaply.** (S5.1)

Open questions are in S6; nothing is registered or queued.

---

## 0. The thought, verbatim

> "The convergence of the representation to authority to selection bottleneck
> that is emerging is indeed a difficult bottleneck to crack. And clearly the
> correct bottleneck as I have not already imagined exactly how that will work
> more than what we have. How things are represented seems very important.
> Representation itself must relate to why something might be selected. Object
> representation systems where decisions for what make an object relate to the
> why of selection. That is to say relating to usefulness which would relate to
> goals, harm, and things like metabolic or interoceptive state (hunger and
> thirst etc) and possibly other basic drives like information need. Objects and
> episodes then hold useful information, indeed very compressed information which
> could help with selection etc. The previous idea I had of higher order
> representations in the latent field may not quite be all the story especially
> since higher level latents may be more abstract but without there being a
> funnel they are not necessarily compressed to extract useful representative
> values. A combination of the higher level representation and objects and
> episodes is likely to be useful."
>
> -- user, 2026-08-26, in conversation

---

## 1. Where this lands in existing REE work

The thought is not arriving on empty ground. Three separate REE threads have
independently converged on the same bottleneck, and one of them states the
thought's core principle almost word for word at claim level. What the thought
adds is **a criterion the existing threads do not supply** (section 3).

### 1.1 The authority/selection side is exhaustively characterised

The `conversion_ceiling_campaign` has spent roughly three months on precisely the
"authority -> selection" link. Its findings, in order of discovery, form a clean
ladder (source: `docs/architecture/modulatory_bias_selection_authority.md`,
`conversion_ceiling_prong_map.md`, `conversion_ceiling_phase0_synthesis_2026-06-18.md`):

| Link | Established by | Finding |
|---|---|---|
| **Reach** | V3-EXQ-643 / 643a | A modulatory channel with no cross-candidate *range* has no authority. "Rescaling a zero range is still zero." |
| **Routing** | 569f / 661 / 654a -> 663 | Range must be *routed into the per-candidate bias*, not merely exist in the representation. Range present in a representation is flattened by the consuming head. |
| **Conversion** | 569g / 682 / 684 / 569h | Even routed, the channel is subdominant to F (the primary harm/goal score), which monopolises **88-89%** of E3 committed-selection variance (MECH-439, V3-EXQ-571). |
| **Structural bound beats rebalancing** | 569i, 689d | Top-k / eligibility-demotion (MECH-448, BG-faithful) lifts committed entropy where gain-tuning does not. |
| **But it does not generalise** | 654h / 485i / 445h / 625e | The lift was demonstrated on the GAP-A foraging substrate ONLY. A re-derive brake is live; further lettered re-tests of those lineages are REFUSED. |

The campaign is now **parked** behind two upstream blocks, and `CURRENT_FRONT.md`
states outright that the live front is not "attack f_dominance". The two blocks
are the competence floor (MECH-457) and **INV-088 -- `world_goal_evaluator_bounded_by_z_world_differentiation`**.

INV-088 is, in REE's own registry, the "representation bounds authority bounds
selection" claim. The user's bottleneck is already half-registered.

### 1.2 The most recent measurement says the modulatory layer is not merely weak -- it is flat

`authority_to_action_stage_trace_probe_2026-08-22.md` is four days old and is the
sharpest datum available. Measured, not asserted:

- At the bare default operating point, `E3.select()`'s post-modulation `scores`
  tensor is **bit-identical** to its pre-modulation `raw_scores` on every tick.
  `scores == raw_scores` in **12** distinct configurations tested.
- **Eleven default-ON flags moved nothing at any of 8 real operating points,
  across ~3182 matched-state ticks** -- including both harm analogs
  (`use_bla_analog`, `use_cea_analog`), all three curiosity flavours, both
  diversity levers, and both escape-credit channels.
- When the dACC bias *does* run (98 of 1361 drivers satisfy its precondition
  conjunction), `_dacc_last_bias` is a real tensor with cross-candidate spread
  **0.0** -- "a uniform scalar added to every candidate, invariant under
  argmin/softmax however large."

The probe's own conclusion is the one-line version:

> **Nothing asserts that the production path ever produces a non-degenerate
> `score_bias`.** ... "Spread, not magnitude."

MECH-463 makes the same point in claim form from the affect side: global-scalar
arousal channels (D1/D2 gain, urgency threshold shrinkage, LC-NE temperature)
each apply **one scalar uniformly across all K candidates**, so they cannot
reorder an argmax -- but they *do* sharpen commitment, which under F-dominance
means affect **entrenches F** rather than converting diversity.

### 1.3 The principle the user states is already MECH-359

`MECH-359` (candidate, `substrate_conditional`, `implementation_phase: v4`,
registered 2026-06-09, from the user's own 2026-06-06 thought):

> "for proto-affect to carve behaviour it must carry per-candidate
> (cross-candidate) range, not merely per-tick magnitude. Each E3 candidate
> trajectory carries a multi-channel affect vector (curiosity / safety /
> harm-sensory / harm-affective / effort / relief / blocked-agency) **so the same
> world-state can support different candidate rankings** (approach / inspect /
> retreat / persist / retry / rest / reorient) **under different internal
> pressures**."

With `MECH-360` (expression as action geometry) and `MECH-361` (candidate-gradient
episode schema: `state -> candidates -> affective gradients -> selected ->
outcome -> residue`, the gradient used as memory write-weight and retrieval
query). All three are `substrate_conditional`, deliberately suppressed from IGW,
marked **DO NOT build in V3**.

So the "usefulness must be per-candidate" half of the thought is registered and
parked. That is worth saying plainly: **the thought is not new to REE at the
level of the principle.** What is new is the *criterion* -- section 3.

### 1.4 The object spine exists, with a resolved fork

`ARC-080` (candidate, v3_pending, v4) is the adopted spine: object identity as a
cross-cutting primitive, with `ARC-081/082/083` as self / tools / others pillars
and permanence as an unregistered future child. Its **OBJ-1 resolution**
(2026-06-14, user decision) is directly relevant here: an object is **not** one
of {type, token, anchor} crowned over the others -- it is the **coregistration**
that holds all three facets bound. `MECH-278` supplies the definition currently
in force: *an object is the stable bundle of features that behave causally
together under interventional perturbation.*

And SD-057 is **live** (default-OFF flags): `IncentiveTokenBank` holds, per
resource-type tag k, a revaluable `base_value[k]` and a stored identity
embedding `z_object[k]`, with drive-conditioned recall
`wanting[k] = base_value[k] * (1 + kappa * drive_axis[k])`
(`ree-v3/ree_core/goal.py:659-770`, verified in code this session).

**That formula is already the user's "usefulness".** It is object identity x
interoceptive/metabolic state -> value. The machinery the thought asks for
exists, one layer deep, today.

---

## 2. The code-level finding: the funnel exists, and it funnels to ONE

This is the most concrete thing this session found, and it was not previously
written down anywhere I could locate.

Trace the object-indexed value from the bank to the selector:

```
IncentiveTokenBank                      per-object, drive-conditioned
  base_value[k], z_object[k]            k in {1..n_resource_types}
  wanting[k] = base_value[k]*(1+kappa*drive_axis[k])
        |
        |  most_wanted()  ->  argmax over k          <-- ARGMAX COLLAPSE
        v
  (k*, z_object[k*], wanting[k*])       ONE object survives
        |
        |  MECH-346: z_goal seeded FROM z_object[k*]
        v
  z_goal                                ONE attractor vector
        |
        |  goal_proximity(cand) = 1/(1+MSE(z_world_cand, z_goal))
        v
  per-candidate scalar, folded INTO F   (e3_selector.py:1121, ONE call)
```

Verified: `most_wanted()` is consumed at `ree_core/agent.py:10897` for z_goal
seeding, and `e3_selector.py` calls `goal_state.goal_proximity(flat)` exactly
once, against the single z_goal.

**The consequence.** The bank knows the drive-conditioned worth of *every* stored
object. Exactly one of them reaches selection. A candidate trajectory heading
toward object 2 is scored **only by its distance to object 1's embedding**. The
comparative structure -- the very thing that would make candidates differ from
each other for a value-relevant reason -- is discarded by `max()` before the
selector ever sees it.

So there IS a funnel from objects to selection, and it is a funnel **to one
winner**, not a funnel **to a differentiated per-candidate value structure**.
This is a different failure from the ones the conversion-ceiling campaign
catalogued: not "the channel is drowned by F" (MECH-439) and not "the channel is
a uniform scalar" (MECH-463), but **"the channel's cross-candidate structure was
destroyed upstream, by an argmax, before routing."**

It also explains a puzzle in the campaign record. `project_channel_range()` in
`e3_selector.py` routes a channel's per-candidate representation into a bias by
projecting onto the leading right-singular vector of the centred `[K, D]` matrix
-- a **generic** direction of maximal variance. It has no way to know which
direction of variation *matters*. If the object-indexed value structure had
survived to that point, no singular-vector projection would be needed: the
per-candidate differences would already be in value units.

### 2.1 Correction: there are TWO multi-item value stores, and neither reaches the selector

The "funnel to one" above is accurate for the SD-057 path but is too strong as a
blanket statement, and the correction makes the finding sharper rather than
weaker. REE has **two** ranked multi-item value stores:

| Store | Key | Per-item value | Consumer |
|---|---|---|---|
| `IncentiveTokenBank` (SD-057) | resource **type** tag k | `base_value[k]`, drive-conditioned `wanting[k]` | `most_wanted()` -> **argmax** -> z_goal seed (MECH-346) |
| `GhostGoalBank` (MECH-292) | spatial **anchor** | `wanting_strength`, `arousal_tag`, `ghost_priority` -- a genuine **ranked** list (`bank.rank()`) | MECH-293 waking ghost-goal **probe search** (seeds candidate trajectories) |

The ghost bank does *not* collapse -- it ranks. But its consumer is **trajectory
proposal**, not candidate **scoring**: it seeds probes into the candidate pool,
tagged `hypothesis_tag` / `metadata["ghost_priority"]`. It never supplies a
per-candidate value at the committed argmin.

So the accurate statement is stronger than the one above:

> **REE maintains two ranked, revaluable, multi-item value stores, and neither
> delivers a multi-item comparison to the E3 committed selector.** One is
> collapsed by `max()` into a single attractor; the other feeds proposal rather
> than selection.

This sharpens ARC-080's "three disconnected per-item stores" observation with a
consumer-side fact ARC-080 does not state: the stores are not merely
uncoordinated with each other -- **none of them is a selection-time input.** The
selector sees one z_goal vector, plus whatever the modulatory channels supply
(measured spread: 0.0).

**Caveat, stated rather than buried.** SD-057 is default-OFF, and the argmax
collapse is by design -- MECH-346 exists specifically to make z_goal's *seed
source* object-bound so wanting could dissociate from liking. Collapsing to one
pointer was the point of L4, and it solved the L9 dissociation problem it was
built for. The observation here is not that MECH-346 is wrong; it is that
**nothing downstream of it carries the multi-object comparison**, and that gap
was never anyone's assignment. The same holds for MECH-292: ranking anchors for
probe search is what it was built for, and nothing asked it to also score
candidates.

### 2.2 The same move happens on the EPISODE side -- and it is the same shape

The user's thought names "objects **and** episodes". Running the identical trace
on the episode side produces a structurally identical result, which is what makes
this worth stating as a pattern rather than a bug.

| | **Objects** | **Episodes** |
|---|---|---|
| Carved by | causal feature-coherence under intervention (MECH-278) | prediction error / Bayesian changepoint (MECH-288: PE threshold on `z_world`/`z_self`; BOCPD on `z_goal`) |
| Value index exists? | **yes, live** -- `wanting[k] = base_value[k]*(1+kappa*drive_axis[k])` (SD-057, default-OFF) | **proposed** -- MECH-443 priority-weighted replay write selection |
| Ranked multi-item store? | `IncentiveTokenBank` | `GhostGoalBank` (MECH-292, `bank.rank()`) |
| Reaches the selector? | **No** -- `most_wanted()` argmax -> one z_goal | **No** -- MECH-319 is a **binary** WHETHER gate; MECH-443's graded WHICH is unbuilt |

MECH-443 is worth dwelling on, because it is the episode-side statement of
exactly the criterion the user is proposing, **already registered**, and it came
in through the MuZero lane (CDQ-005, `REE_convergence/sources/muzero/`):

> the priority is the value of the **update** (gain x need, Mattar & Daw 2018),
> **NOT reward magnitude** -- with the Carey et al. 2019 refinement that replay
> can be biased *away* from the currently-most-valuable outcome.

"Gain x need" is a decision-theoretic quantity: *how much would knowing this
change what I would choose*, times *how likely am I to face that choice*. That is
"usefulness for selection" used as an **indexing criterion for episodes**, which
is precisely the user's move applied to the episode half. Its status is
`candidate / substrate_ceiling / v3_pending` -- explicitly "the current gate is
too coarse to carry the signal". Off the V3 critical path; nothing has decided
whether to build it.

### 2.3 The pattern: graded value, categorical interface

Three independent places in REE compute a **graded** value structure and then
hand the consumer a **categorical** summary of it. In each case the consumer is
the selector or a write gate, and in each case the gradient dies at the boundary:

1. **Objects.** `wanting[k]` over all k -> `most_wanted()` **argmax** -> one
   z_goal -> one `goal_proximity` call. *(verified in code, section 2)*
2. **Episodes.** Replay priority is graded in principle (MECH-443, Mattar & Daw)
   -> MECH-319 is an **all-or-nothing** `caller_sim` gate: "It is all-or-nothing.
   It says nothing about *ordering* among the replayed transitions it admits."
   *(quoted from `prioritized_replay_write_gating.md`)*
3. **Affect.** A graded affective state -> **one scalar** broadcast uniformly
   across all K candidates (MECH-463: D1/D2 gain, urgency threshold shrinkage,
   LC-NE temperature), measured spread **0.0** across ~3182 matched-state ticks.

I do not think this is three coincidences. It is one architectural habit:
**value is computed gradedly and delivered categorically.** And a categorical
delivery is, definitionally, a delivery with no cross-candidate structure -- which
is exactly the F-C2 defect the authority campaign has been trying to repair from
downstream for three months, with gain rescaling, std-basis normalisation, margin
shortlists and top-k shortlists.

If this reading is right, it reframes the campaign's whole ladder. Those levers
are all attempts to **manufacture** cross-candidate differentiation at the
selector. The pattern above says the differentiation **existed upstream and was
thrown away at the interface**. Recovering it is then not a tuning problem but a
plumbing one -- and plumbing is `complicated (buildable)`, not
`complex (probe-gated)`.

**Held-out check against the record, since this is a strong claim.** The reading
must not be over-fitted, so: does it predict anything the campaign already found
independently?

- It predicts **structural bounding beats variance rebalancing** -- because
  rebalancing amplifies a signal that has no structure, while bounding (top-k)
  lets whatever residual structure exists decide. That is exactly the
  2026-06-18 Phase-1 verdict ("STRUCTURAL BOUNDING wins, NOT F-variance
  rebalancing"; 569h rebalance FAILed 1/3, 569i top-k PASSed 2/3). **Qualified:**
  569i's margin is explicitly recorded as **thin** (ARM_1 0.711 vs proposer
  0.650, ~0.06 nats), and the synthesis notes that if it does not survive the
  full composite the real target is F's monopoly itself. So this post-diction is
  directional, not decisive.
- It predicts the **margin shortlist collapses to a global favourite** -- because
  `argmin` over a near-whole eligible set of a structureless channel picks that
  channel's state-invariant preference. That is exactly the recorded 569h
  diagnosis (`modulatory_shortlist_size_mean` 6.25-8.54 of ~8; "collapses to the
  modulatory channel's **global favourite** (monostrategy)").
- It predicts **Go/No-Go is standalone-inert** -- a relabeller inside another
  lever's envelope adds nothing when the thing being relabelled carries no
  gradient. Recorded: 689h `gng_inert_standalone=True`, ARM_GNG bit-identical to
  ARM_OFF.

Three post-dictions on findings this reading was not built from. That is
encouraging but **it is post-diction, not prediction** -- the findings were all in
front of me when I wrote this. The honest test is 5.1, which is a forward
measurement with a pre-registered null.

---

## 3. What the thought adds that REE does not already have

REE currently carves its world along **three** axes. None of them is usefulness.

| Structure | Carving criterion | Where |
|---|---|---|
| **Objects** | causal feature-coherence under intervention | MECH-278 |
| **Episodes** | prediction error / Bayesian changepoint | MECH-288 event segmenter: fast = normalised PE threshold on `z_world`/`z_self`; slow = BOCPD on `z_goal` |
| **Latent depths** | *timescale* (gamma / beta / theta / delta) | ARC-004 L-space |

Value (F) is then computed **on top of** all three, at E3.

The user's thought proposes a fourth criterion and asserts it should be
constitutive rather than downstream:

> **An object/episode is individuated by what it is useful for.**

This is a real fork, not a rewording, and it is *unregistered*. MECH-278 and the
user's criterion can disagree:

- **Causally identical, functionally distinct.** Two berries with identical
  intervention dynamics but different nutritional axes are ONE object under
  MECH-278 and TWO under the usefulness criterion.
- **Causally distinct, functionally identical.** A hazard that bites and a hazard
  that falls are two causal bundles and ONE "avoid" unit. This is how biological
  *predator* categories work -- they unify causally dissimilar things by their
  relation to the organism.
- **Drive-relative re-individuation.** Under the usefulness criterion the same
  world can carve differently when hungry vs thirsty vs injured. Under MECH-278
  it cannot -- causal structure does not move with interoceptive state.

That third one is the sharpest, because it is exactly what MECH-359 says
selection needs ("the same world-state can support different candidate rankings
under different internal pressures") and exactly what a causal or predictive
carving cannot deliver.

### 3.1 The "funnel" point, made precise

The user's diagnosis of his own earlier idea is, I think, correct and worth
stating in REE's terms.

`ARC-004` L-space is stratified **by timescale**: z_gamma (sensory binding) ->
z_beta (affordance/action-set) -> z_theta (sequence context) -> z_delta (regime,
motivational set, long-horizon context, "biases selection but does not overwrite
perception"). Depth = prediction horizon. **Deeper is more abstract in the
temporal sense, and nothing in the design makes it more compressed toward what
selection needs.** There is no objective anywhere in the stack of the form
"preserve what distinguishes options by their worth."

That is the funnel the user says is missing, and its absence is architectural,
not a tuning failure.

The same point holds for the two carvings above: PE-carved episodes preserve what
was *surprising*; intervention-carved objects preserve what *coheres causally*.
Neither preserves what *matters*, except by the accident that surprising and
causally-coherent things are often also important.

### 3.1b "Information need" as a drive axis

The user lists "information need" alongside hunger and thirst as a **basic
drive**. That is a stronger claim than "curiosity exists", and it interacts with
a currently-stuck REE result in a way worth spelling out.

`MECH-458` (candidate) established, from two cloud PASSes re-analysed on a common
scale, that SD-025 curiosity is a **reward-conditional exploitation amplifier**,
not a diversity generator: density-attraction 39.3 vs familiarity-discount
ceiling 20.4 (~1.9x), with the diversity term contributing **0 at the decision
point**, and **0 directed behaviour** on a map reward has not already sculpted.
Its corollary is that proactive diversity needs a *separate rarity-seeking drive*
(Bellemare polarity) -- "ordering-gated on INV-088 z_world differentiation".

That owed build is currently framed as **a bonus over states** -- attraction to
low-count/under-represented regions of a map. Note what shape that is: a
*state-indexed scalar*, which is the section-2.3 pattern again, and which is why
it is gated on having a differentiated map to range over.

The user's framing suggests a different shape. If information need is a **drive
axis on the same footing as the metabolic axes**, then it plugs into machinery
that already exists rather than needing new machinery:

- SD-049 supplies **per-axis drive**; SD-057's `_drive_axis_for(k, ...)` already
  maps object tag k to drive axis k-1.
- `wanting[k] = base_value[k] * (1 + kappa * drive_axis[k])` would then make
  **epistemic value object-bound and drive-conditioned** -- "this object is worth
  approaching *because I need to know about it*, scaled by how much I currently
  need to know anything at all."

That is a materially different mechanism from a novelty bonus over states. It is
per-**object**, revaluable, persists when the object is out of view, and competes
in the same currency as hunger and thirst -- so an epistemic goal and a metabolic
goal can be *traded off* rather than summed as unrelated terms. It also inherits
the section-2.3 problem for free (it would be collapsed by the same argmax), and
the section-5.1 fix for free (a soft bank read makes epistemic and metabolic
wanting differentiate candidates jointly).

**The honest objection, which I do not think is settled.** Epistemic value may be
a category error in this slot. Hunger is a property of the **agent's body**;
information need is a property of the **agent's model** -- specifically of where
the model is uncertain. A per-object `base_value` learned from *benefit pulses at
contact* has no obvious epistemic analogue, because the "benefit" of an epistemic
interaction is a reduction in model uncertainty, which is not a pulse the
environment delivers. Making this work would need `base_value[k]` for the
epistemic axis to be written from something like E1/E2 prediction error *about
object k*, which is a real build, not a re-wiring.

So: plausible, cheap to *state*, and not cheap to build. Flagged as question 3
in section 6 rather than proposed.

### 3.2 The formal shape, and the external precedent

Stated as an objective, the difference is standard information-bottleneck
geometry:

- **What REE trains now:** compress X subject to preserving `I(Z; X_{t+1})`
  (E1 sensory prediction, E2 motor-sensory, SD-056 action-conditional
  contrastive). Reconstruction/prediction-shaped.
- **What the thought proposes:** compress X subject to preserving what is
  sufficient to *rank options* -- `I(Z; V)`, or more precisely, sufficiency for
  the selection ordering.

This is a known and empirically consequential distinction outside REE:
value-equivalent models (Grimm et al. 2020), bisimulation metrics (Ferns et al.;
DeepMDP), and **MuZero**, which trains its latent purely on reward/value/policy
targets with *no observation-reconstruction loss at all* and outperforms
reconstruction-trained model-based agents. REE_convergence already holds a MuZero
intake lane, so this is a translation question, not a new import.

I want to flag one honest tension with REE's own design rationale before this is
taken as settled. `efficiency_dimensionality_hypothesis.md` argues the multi-stack
exists **precisely so** each module trains on a *clean, separated* error signal
(E1 sensory, E2 motor-sensory, E3 harm/goal), avoiding gradient interference. A
joint representation-and-value objective deliberately re-entangles what SD-004/
SD-005 separated. That is not necessarily wrong -- but it is a reversal of a
stated architectural commitment and should be argued, not slipped in.

### 3.3 REE already has one worked example of the thesis, and it PASSED

`SD-004` (status: **implemented**) -- "action objects as hippocampal map
backbone". E2 produces compressed **action-object** representations; the
hippocampus navigates action-object space O (16-dim) rather than raw z_world
(32-dim). `EXQ-003` PASS: terrain-guided planning in O-space achieved a **6x
survival improvement** over random trajectory selection in z_world.

`efficiency_dimensionality_hypothesis.md` calls this "the strongest current piece
of evidence for the efficiency hypothesis" and notes the benefit is *structural*
and does not depend on SD-005 holding.

And it is already **per-candidate**: `Trajectory.action_objects` carries the
`o_t` sequence on every candidate trajectory (`ree_core/predictors/e2_fast.py:53`).
The compressed, consumer-defined unit is present at the selection site today --
it simply carries no value index.

**This is the user's thesis, already built, already validated, at one narrow
scope.** O-space is a funnel: a compression whose target is defined by *what the
planner needs to choose between*, not by what reconstructs the world. The
proposal in section 4 is essentially: generalise the SD-004 move from
action-effects to objects-and-episodes, with drive/harm as the value index.

---

## 4. Does the object/episode distinction survive scrutiny, or collapse into "just a latent"?

The launch question. I think it survives, but only on **three checkable
properties** -- and if none holds, the distinction genuinely does collapse and
should be dropped.

**(a) Addressability and persistence across gaps.** An object is a *slot* with an
identity you can point at when it is not being perceived; a latent is a vector
recomputed each tick with no identity. The operational test: **can you revalue it
without re-perceiving it?** `IncentiveTokenBank` can (revaluable `base_value`,
Balleine/Dickinson). z_delta cannot. This is ARC-080's OBJ-1 coregistration and
it is a real structural difference, not a framing one.

**(b) Per-candidate differentiation comes for free.** This is the mechanical link
to the authority problem and, I think, the strongest argument. A latent-derived
modulatory signal is computed **per tick** -> one vector -> one scalar bias ->
**spread 0.0**, which is the F-C2 defect measured 2026-08-22 across ~3182 ticks.
An object-indexed value is computed **per object**; candidates that engage
different objects therefore differ *by construction*. Spread stops being
something the authority layer has to manufacture downstream (gain rescaling,
top-k shortlists, std-basis normalisation -- all of which were tried) and becomes
a property of the representational format.

If that is right, then the entire conversion-ceiling ladder has been trying to
recover downstream a differentiation that was destroyed upstream. The section-2
argmax finding is one concrete instance of exactly that destruction.

**(c) The decoder IS the selector.** An object's value token is a sufficient
statistic for selection *with respect to that object*. The funnel's target is
defined by the consumer. A latent's compression target is defined by a predictive
loss that has no consumer in the selection path.

**Falsifier for the whole distinction:** if an object-indexed bias channel and a
latent-projection bias channel produce statistically indistinguishable
cross-candidate spread at matched operating point, then (b) is false, and the
object framing is decoration over a latent. That is cheap to measure -- see 5.1.

---

## 5. What would make this buildable rather than conceptual

In `work_graph_debt_vocabulary.md` terms:

- The general claim "representation should be carved by selection-relevance" is
  **`complex (probe-gated)`** -- it needs a spike, not a build.
- The specific question "does object-indexing produce cross-candidate spread
  where latent-projection does not" is **`complicated (buildable)`** and cheap.
- "What is the right individuation criterion for an object" is currently a
  **`mystery (known data)`** -- more data will not settle it; it needs the
  reframe the user is proposing.

### 5.1 The cheapest decisive probe (proposed, NOT queued)

My first draft of this section proposed adding an `object_incentive` source to
`modulatory_channel_route_source` and claimed "the machinery exists at both
ends". **I then checked the code and that claim was wrong in one respect and
understated in another.** The corrected version is simpler and stronger.

**What is NOT there:** `E3TrajectorySelector.select()` receives
`candidates: List[Trajectory]` and has **no** per-candidate resource-type or
object-identity argument. `resource_prox_pred` is a `[batch, 1]` **scalar** head
(peak resource proximity), so it cannot attribute a candidate to an object type.
There is no existing per-candidate object-attribution step.

**What IS there, and makes the attribution step unnecessary:**

- `Trajectory.world_states` -- `[batch, horizon+1, world_dim]`, already used by
  `compute_goal_score()`.
- `IncentiveTokenBank._z_object[k]` -- `[1, goal_dim]` per stored object.
- **Dimensions are already compatible.** `config.goal.goal_dim` is wired to
  `config.latent.world_dim` by default (`utils/config.py:7747`), and
  `z_resource_dim` "must match GoalConfig.goal_dim for direct seeding"
  (`utils/config.py:350`). **No new projection is needed.**

So the candidate does not need to be *labelled* with an object. Its proximity to
**every** stored object can be read directly. The probe is therefore not a new
channel source -- it is **replacing an argmax with a soft, wanting-weighted read
over the whole bank**, using only tensors that already exist:

```
current (compute_goal_score, e3_selector.py:1111-1123):
    prox   = goal_proximity(flat)                       # vs ONE z_goal
    score  = prox.reshape(B, H+1).sum(-1)               # [B]

proposed (additive modulatory channel, default OFF):
    w = bank.wanting(per_axis_drive, scalar_drive)      # {k: float}
    bias = sum_k  w[k] * ( 1 / (1 + MSE(flat, z_object[k])) )
    bias = bias.reshape(B, H+1).sum(-1)                 # [B]
```

In words: **per-candidate value = how close this candidate brings me to each
thing I have stored, weighted by how much I currently want that thing given my
interoceptive state.** That is the user's sentence -- "objects and episodes then
hold useful information, indeed very compressed information which could help with
selection" -- expressed in ~10 lines over existing tensors.

Properties that make this the right first probe:

1. **Spread is non-degenerate by construction**, whenever >= 2 objects are stored
   with differing `wanting[k]` and candidates differ in which they approach. This
   attacks the measured F-C2 defect (`score_bias` spread 0.0 across ~3182 ticks)
   at its source rather than rescaling it downstream.
2. **It does not touch z_goal or MECH-346.** It is an *additive modulatory
   channel*, so the L9 wanting != liking machinery, the argmax seed, and the
   commit-threshold semantics are all untouched. Bit-identical when OFF.
3. **It reuses the existing authority plumbing.** The routed bias folds into
   `_modulatory_accum`, so `modulatory_channel_route_range` reports its raw
   cross-candidate range *before* rescaling -- the P0 readiness gate the 663 work
   already built exists to measure exactly this.
4. **It is pre-registered falsifiable at the cheapest point.** DV is *spread*,
   not behaviour: `modulatory_channel_route_range` for the object-field read vs
   the existing `cand_world_summary` singular-vector projection, at matched
   operating point. No competence claim, no committed-entropy claim, no
   promotion, no `claim_ids`.
5. **A null is informative.** If the object-indexed read carries no more
   cross-candidate range than the generic latent projection, property (b) of
   section 4 is false, the object framing does not earn its place at the
   selector, and the thought should be narrowed to representation-learning only.

**Mandatory guards, inherited from the existing record and not optional:**

- The **V3-EXQ-643 non-vacuity gate**. The 643 harness drove primary scores to
  ~1e32 and float32 cancellation returned a spurious zero range. Any run here
  must keep `raw_score_range` bounded and assert it, or a null is uninterpretable.
- The **604a degeneracy guard**: assert the bank is non-empty with >= 2 stored
  objects and non-uniform `wanting`, else the arm tests a degenerate upstream
  signal rather than the mechanism. "Scaling a zero range is still zero."
- SD-057 is **default-OFF**, so the operating point must arm
  `use_incentive_token_bank` -- and per the 2026-08-22 probe, most drivers do not
  satisfy such preconditions, which is precisely how a false INERT arises.

**A second, independent route worth noting.** `Trajectory.action_objects` carries
the SD-004 `o_t` sequence per candidate -- the *already-validated* funnel of
section 3.3 (EXQ-003 PASS, 6x survival). An object-field read in **O-space**
rather than z_world space is the more faithful expression of the thesis, since
O-space is already a consumer-defined compression. It is second, not first,
because it needs the bank's embeddings mapped into O-space, which the z_world
route does not.

### 5.2 Ordering caution against the existing record

Two live constraints argue against jumping to a representation build:

1. The **differentiate-first** prediction (`monostrategy_representation_ceiling_root`)
   already says differentiate z_world *before* applying diversity pressure. The
   user's thought sharpens this into a question that ordering does not answer:
   **differentiated along which axis?** Raising the effective dimensionality of a
   *prediction-trained* latent differentiates along prediction-relevant axes,
   which need not align with value-relevant axes at all. If the user's criterion
   is right, generic differentiation is the wrong lever and would produce a
   plausible null.
2. The `734/737b/742a` autopsy is a **caution against the representation reading**
   and I want to record it against my own argument. It found `ppo_ree_latent`
   0.233 and `ppo_raw_obs` 0.567 *both* sub-random, and concluded: "a failure
   invariant across learner AND representation is a property of neither -- it is
   a property of the **objective** they share." It explicitly rejects
   `substrate_ceiling` on the representation.

   The honest reading: that autopsy is evidence **against** "the representation
   lacks capacity" and **for** "the objective is mis-specified". Which is
   congruent with the thought -- the thought is an *objective-level* proposal
   (train the representation for selection-relevance), not a capacity proposal.
   But it must not be cited as evidence that representation is the ceiling. It
   says the opposite.

---

## 6. Open questions for the user

Ordered by how much they change what gets built. Questions 1-3 are about the
*idea*; 4-6 are decisions that could be taken independently of it.

1. **Is the usefulness criterion meant to REPLACE MECH-278's causal-coherence
   definition, or to sit ALONGSIDE it as a second facet?** ARC-080's OBJ-1
   resolution already made the object a *coregistration* of three facets
   (type / anchor / token) rather than crowning one. The conservative move is a
   **fourth facet -- a value/affordance facet** -- coregistered with the others.
   The radical move is that usefulness is the *primary* individuation criterion
   and causal coherence is merely evidence for it. Different builds; I do not
   want to assume which you mean.

2. **Does the funnel run THROUGH objects, or do objects and the funnel do
   different jobs?** Your closing sentence ("a combination ... is likely to be
   useful") suggests both. One reading: higher-order latents supply *generality*
   (what kind of situation is this), objects/episodes supply *addressability and
   revaluability* (what specific things are at stake, worth what to me now). On
   that reading the architecture is not "objects instead of deep latents" but
   **"deep latents index; objects carry value"** -- which is a much smaller change
   than replacing the latent stack, and is roughly what section 5.1 would test.

3. **"Information need" as a drive axis (3.1b) -- same mechanism as hunger, or a
   category error?** The plumbing is nearly free (SD-049 per-axis drive x SD-057
   per-object token). The hard part is what writes `base_value` for an epistemic
   axis, since there is no environmental "benefit pulse" for learning something.
   If you want this, it is a real build; if you want it *only* as a
   trade-off-in-one-currency argument, it may be enough to say so and let the
   rarity-seeking build MECH-458 already owes inherit the object-bound shape.

4. **Is the categorical-collapse pattern (2.3) a real finding, or am I pattern-
   matching three unrelated design choices?** This is the claim I am least sure
   of and the one that would matter most if true. Each of the three instances has
   a perfectly good local justification (MECH-346 needed a single seed; MECH-319
   needed a clean simulation/real boundary; global neuromodulators really are
   broadcast in biology). The question is whether "graded value, categorical
   interface" is a genuine architectural habit or three defensible decisions I
   have strung together with hindsight. Your judgement here decides whether
   section 5.1 is a probe of a pattern or a one-off plumbing test.

5. **The argmax collapse (section 2) as a standalone item.** Independent of
   everything above: the multi-object comparison is destroyed by `most_wanted()`
   before selection, and nothing downstream carries it. That is small, concrete,
   V3-scoped and code-verified. It could be raised as a governance flag on its own
   merits. **I have not raised one** -- per the standing rule that governance
   findings route via `governance_flag.py`, and per your instruction that nothing
   here gets registered without you. Say the word and it becomes a flag.

6. **Does the re-entanglement worry (3.2) matter to you?** A joint
   representation-and-value objective reverses the multi-stack separation
   rationale SD-004/SD-005 were built on. I think the SD-004 precedent (3.3)
   shows the separation was never absolute -- O-space is already a
   consumer-defined compression, and it is the single best-evidenced efficiency
   result in the project. But this is an architectural-commitment question and
   it is yours, not mine.

### What I would do next, if you want a recommendation

Section 5.1, and nothing else. It is the only step here that is cheap, forward-
looking, pre-registered falsifiable, and informative in **both** directions --
and it does not require settling questions 1-4 first. A null there narrows the
whole thought to representation-learning and saves a lot of downstream design; a
positive result makes questions 1-4 worth the argument.

## 7. What this document deliberately does not do

- Registers no claim. MECH-359/360/361 already carry the per-candidate principle
  and are `substrate_conditional` **by design**; nothing here unparks them.
- Queues no experiment. The 5.1 probe is a proposal awaiting your decision.
- Proposes no change to MECH-278, ARC-080, or the OBJ-1 resolution.
- Does not treat the conversion-ceiling re-derive brake as liftable. If anything
  in section 5 became a build, it would need to be routed as a *representation*
  question, not another lettered re-test of the 689/485/445/625 lineages.

## 8. Sources read for this synthesis

`docs/CURRENT_FRONT.md`; `docs/architecture/arc_080_object_representation_primitive.md`;
`docs/architecture/modulatory_bias_selection_authority.md`;
`docs/architecture/candidate_differentiated_affective_gradients.md`;
`docs/architecture/efficiency_dimensionality_hypothesis.md`;
`docs/architecture/l_space.md`; `docs/architecture/event_segmenter.md`;
`evidence/planning/authority_to_action_stage_trace_probe_2026-08-22.md`;
`evidence/planning/conversion_ceiling_prong_map.md`;
`evidence/planning/failure_autopsy_competence-objective-cluster-734-737b-742a_2026-07-22.md`;
`docs/claims/claims.yaml` (SD-004, MECH-278, MECH-359/360/361, ARC-080, ARC-006,
MECH-045, SD-057, MECH-344/346, MECH-439, MECH-448, MECH-457, MECH-458, MECH-463,
INV-088, ARC-062, MECH-309, ARC-065, SD-055, SD-056, SD-016);
`ree-v3/ree_core/goal.py` (IncentiveTokenBank, verified in code);
`ree-v3/ree_core/agent.py:10897`; `ree-v3/ree_core/predictors/e3_selector.py`
(channel registry, `compute_goal_score` / `goal_proximity` call site,
`select()` signature); `ree-v3/ree_core/predictors/e2_fast.py:42-70`
(`Trajectory` fields); `ree-v3/ree_core/hippocampal/ghost_goal_bank.py`;
`ree-v3/ree_core/hippocampal/anchor_set.py:60-90` (`AnchorGoalPayload`);
`ree-v3/ree_core/utils/config.py:350,7747` (goal_dim/world_dim/z_resource_dim
wiring).

**Provenance note.** Every code-level statement in sections 2, 2.1, 3.3 and 5.1
was read from `ree-v3` at `main` during this session, not inferred from the
design docs. Section 5.1 records where my own first draft was wrong, because the
wrong version was more optimistic about existing machinery than the code
supports.
