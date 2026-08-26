# Thought-digestion wave 1 — DRAFTS FOR REVIEW (nothing applied)

**Date:** 2026-08-26 · **Session:** `insights-7fd98a-digestion`
**Status:** STAGED ONLY. No `claims.yaml` write has been made. Dispositions are the user's call.
**Claims in wave:** ARC-133, MECH-516, MECH-517, MECH-518, MECH-521
**Method:** 5 parallel read-only drafting agents; orchestrator sole writer.

---

## 0. Cross-cutting findings (verified by the orchestrator in code, not taken on trust)

### 0.1 CORRECTION: the O-space decoder is NOT on 817a's behavioural path

The development doc §3.3c explained 817a's null as "the grounding was applied to the
encoder while the **decoder** exit from the bottleneck remained a collapsing interface
whose argmax pins to one constant class."

**That mechanism is wrong.** Verified: `experiments/v3_exq_817a_sd080_worldeffect_grounding_falsifier.py`
lines 480/486, 581/585, 748/751 run `hippocampal.propose_trajectories(...)` ->
`agent.e3.select(candidates, temperature=1.5)` -> `result.selected_action`. It never calls
`_decode_action_objects` or `get_action_object_sequence`. `module.py`'s own docstring
confirms `select_action` "routes through E3's J(zeta) and returns the action directly
**without consulting the decoder at all**", and the decoder's sanctioned CEM use
"consumes the full real-valued vector, so candidates differ continuously even when their
argmaxes coincide". The argmax-pins effect belongs to a **forbidden driver idiom** used as
a diagnostic. Two agents found this independently.

### 0.2 ...but MECH-518's core assertion SURVIVES, via a different and better site

`ree_core/hippocampal/module.py:2293-2302`: after CEM iteration 0, `ao_mean`/`ao_std` are
refit from `elite_ao_tensor` = the elites' `get_action_object_sequence()`, i.e.
**E2.action_object_head's output**. From iteration 1 the CEM's proposal distribution
literally IS a mean/std over O. Sampling at `:2102`. So O really is both the semantic
compression and the search geometry — and this site IS on 817a's path (it calls
`propose_trajectories`). **The claim is right; the mechanism I stated for it was wrong.**

### 0.3 Evidence nobody in this thread had cited

- **V3-EXQ-948** (2026-08-25, PASS, `claim_ids: []`, diagnostic) — verified present. Fixed
  the objective at `W3_survival_zeroed`, removing the exact confound behind the
  734/737b/742a "objective not representation" verdict, and varied ONLY the observation
  vector: z_world 0.5; z_world + 25-dim resource field **2.233** (clears the 1.0 floor
  3/3); field alone 1.217; raw obs 9.033. `H-observation-interface` moved
  `alive -> confirmed`. Landed ONE DAY before this thought was registered and is cited by
  none of MECH-516/517/518.
- **V3-EXQ-514u** (2026-06-20, PASS/supports MECH-436) — verified present. Already measured
  MECH-516 instance 1 at the interface: flip-gated `mean_wl_drive_delta` -0.133 (sd 0.119),
  sign-unstable, FAILED its 0.15 margin; continuous `mean_cont_amplitude_shift` +0.164
  (sd 0.022) cleared 5/5 against a hard 0.0 OFF floor.
- **V3-EXQ-108b** (2026-08-03, user-gated) — scored **INV-088 `weakens`**: z_world's
  real-state differentiation is healthy (CR_real 0.19-0.20) while the evaluator built on
  its rollout is degenerate by ~11 orders of magnitude (CR_rollout/CR_real ~3e-6). So
  MECH-517's "rival to a healthy standing prediction" framing is stale — and 108b is
  arguably MECH-517's strongest existing support, cited nowhere.

### 0.4 Re-derive brake status (checked)

SD-004 and SD-080 carry **0** `substrate_ceiling` hits; MECH-516/517/518 at 0. The brake
does **not** fire on this lineage — it is queueable. Brakes ARE live on neighbours
(689/485/445/625 conversion-ceiling families; MECH-457 at 7; SD-017 fired at 3), so any
falsifier must be tagged to SD-004/SD-080/MECH-516/517/518 and must NOT be posed as
another conversion-ceiling or f-dominance re-test. **No `substrate_queue.json` entry
exists for the 817a open link** — still unowned.

---

## 1. ARC-133 — recommended (c) `substrate_conditional`, KEEP as registered

Full three-arm draft (ARM_CAUSAL / ARM_USE / ARM_SHUFFLE over one recorded observation
stream replayed under two internal states), with readouts R1 partition-ARI, R2
re-individuation events on an unchanged world, R3 selection utility (the actual
discriminator). Non-degeneracy: (a) an individuation path must exist at all — it does not
today; (b) the attention gate must be non-vacuous; (c) foraging-contact / MECH-520
anti-collapse control.

**The key architectural finding: the fourth-facet framing is a TYPE ERROR.** OBJ-1's
facets (TYPE / ANCHOR / TOKEN) are coordinate descriptors *of a persisting particular* —
properties the object HAS. USE is a *relation* between object and current internal state.
The facets are stable under drive change; ARC-133's whole content is that drive change
alters **how many object-files there are**. A facet cannot determine how many
bearers-of-facets exist. And the tell: the conservative reading is *already instantiated*
(SD-057's `wanting[k]`) and instantiating it changed no carving.
**Better landing zone:** OBJ-1 already defers a "token-vs-type **individuation-strength**
sub-fork" to the first OBJ-2 build step. Drive-modulated individuation strength is a third
option in that live fork, at the right level, needing no OBJ-1 amendment.

**Substrate finding:** `ree_core/entities/object_file_buffer.py` (landed 2026-06-09, after
ARC-080 was written) HARD-CODES MECH-278 — association cost is
`w_motion * d_pos + w_feat * feat_term`, `resource_tag` stored as `type_hint` but never an
input to the decision; docstring: the key is "continuity, not type". ARC-133 is a rival to
running code, not to a design doc. Also: the C4 attention gate has NEVER fired
(V3-EXQ-658 hardcodes `salience=1.0`; `obf_min_birth_salience` defaults 0.0).

---

## 2. MECH-516 — recommended (e) RETIRE/MERGE, or narrow to instance 1 -> (a)

**Two of four instances are factually wrong as registered:**
- **Instance 4 (O-space decoder): FALSE.** See §0.1.
- **Instance 3 (ThetaPacket fixed arity): mis-stated.** Every content slot carries a full
  continuous tensor; the typing exists precisely to PREVENT collapse. Fixed arity
  constrains how many *streams*, not value resolution. (A real instance in the same module
  was missed: `_apply_vs_gate` thresholds continuous `V_s` to binary `is_current`;
  `coherence_weights` is 3-valued.)
- **Instance 2: is MECH-443 restated**, registered 2026-06-19 with a better
  (matched-total-write-mass) falsifier. MECH-443 is not even in `depends_on`.
- **Instance 1 (`most_wanted` argmax): real, and already PASS-confirmed at the interface
  by V3-EXQ-514u** (§0.3).

**Internal inconsistency introduced at registration:** the notes say "MECH-464 disputes the
**affect instance**" — but there IS no affect instance among the four. That is drift from
the development doc's §2.3 list (where instance 3 WAS the affect scalar). So the claim is
LESS contested and MORE thinly instanced than its own notes say.

**Also:** all four sites are behind default-OFF flags, so the headline prediction is
trivially true in the default config for reasons unrelated to the claim.

Full drafted falsifier for instance 1 (ARM_ARGMAX / ARM_GRADED norm-matched /
ARM_SHUFFLE, dose-swept on `incentive_drive_kappa_scale`, with P1-P4 preconditions) is
available and is (a)-shaped if the claim is narrowed.

**On "one habit vs several local decisions":** that is a claim about design PROVENANCE, not
substrate behaviour — two systems with identical dynamics can differ on it. Only a
transfer test (pre-registered site-agnostic remedy template applied unchanged at a second
site) makes it partly empirical, and at n=2 heterogeneous sites it is illustrative, not a
powered discrimination.

---

## 3. MECH-517 — recommended (f) DEFER with a durable note

Full 3x2 factorial draft (R = frozen / grounded / shuffled x I = stock consumer /
non-collapsing consumer), with "non-collapsing" defined operationally (soft wanting-weighted
bank read routed as an additive modulatory channel) rather than by adjective, and seven
non-degeneracy preconditions including P6 = **MECH-518 must clear first** (if proposal
diversity drops under grounding, 817a's null is variance contention and MECH-517 loses its
flagship instance) and P7 = a power requirement 817a's own 21x seed spread shows is not
affordable now.

**The structural problem:** MECH-517's empirical content is a **strict subset of
MECH-516's**. MECH-517 = MECH-516's last sentence + a research-strategy inference. The
inference is a cost argument, not an empirical proposition. The only real falsifier is an
interaction test whose confirming outcome is identical to a confirming outcome for
MECH-516. **Danger F2:** an ordering heuristic naturally absorbs a main-effect result as
vindication, which would make it unfalsifiable; holding it to the interaction keeps it
honest but then it is testing MECH-516.

**Flagship instance misattributed** — see §0.1; the 817a-decoder instance should be
withdrawn from MECH-517's support.

**Counter-evidence weaker than the claim's own notes concede, and the concession is stale:**
V3-EXQ-948 removed the survival confound behind 734/737b/742a (§0.3), so that autopsy is
itself an instance of the MECH-517 *shape* one layer up. **But that rescue costs MECH-517
its specificity**: 948's mechanism is *under-exposure* (content absent from the reader's
input), not *categorical collapse*. Broaden to "any consumer-side defect" and it is
near-unfalsifiable; hold it to MECH-516's mechanism and its flagship instance is
misattributed. **That tension is unresolved.**

---

## 4. MECH-518 — recommended (a) TESTABLE NOW, with two mandatory changes

**DEFECT IN THE CLAIM AS REGISTERED (verified):** the pre-registered check names
`cand_world_pairwise_dist`, which computes `world_forward(z0, candidate_actions)` and has
**zero references to `action_object`**. The 817a manipulation trains ONLY
`action_object_head` (`wf_M5` flat across arms; `M0` 0 -> ~17). So the named instrument is
guaranteed UNCHANGED by construction — and the notes say "if UNCHANGED the claim is
refuted and 817a bites much harder against SD-004 and ARC-133." **As written the check
auto-refutes the claim and auto-escalates against two others.**

**Correct instruments, all already emitted today** by
`HippocampalModule.get_last_propose_diagnostics()`:
`cem_iteration_diagnostics[i].{ao_std_mean,min,max}`, `pre_refit_first_action_entropy`,
`post_elite_refit_first_action_entropy`, `action_object_roundtrip_recovery`. The 817a
driver simply discards them (zero occurrences of `get_last_propose_diagnostics`), so this
is a re-run with a capture, not a re-read.

**MANDATORY CONTROL ARM:** `use_support_preserving_cem=True` with
`support_preserving_ao_std_floor=0.2` are the `from_dims` defaults 817a itself used, and
were MEASURED live clamping `ao_std` fully at CEM iteration 2 and partly at iteration 1 —
against ARM_0's own O spread of `mean_per_dim_action_std` 0.0296, an order of magnitude
BELOW the floor. At defaults the search WIDTH is a constant, not O's variance, so the
channel the claim is about cannot express itself. Needs a matched
`support_preserving_ao_std_floor=0.0` arm.

Full four-precondition draft (P1 budget-not-floor-set, P2 ARM_0 has diversity to lose,
P3 float32 guard, P4 grounding reproduces) with CONFIRMING/FALSIFYING on paired within-seed
drops in `ao_std_mean` (above-floor iterations only) and `pre_refit_first_action_entropy`.

**Residual to state in any FALSIFYING write-up:** `ao_std` is floored but `ao_mean` is NOT,
so a null on the variance channel with movement in `ao_mean` geometry falsifies the
"shared fixed budget = O's VARIANCE" formulation specifically, not the weaker
shared-geometry claim.

---

## 5. MECH-521 — recommended SPLIT two-way, both (c) `substrate_conditional`

**Leg structure is two, not three:**
- **L1a** (circularity / nesting / type-token) is an ARGUMENT, already recorded as
  REFUTED-BY-ARGUMENT — motivation, not assertion. **(b) derivational**; give it no
  falsifier.
- **CORE = L1b + L2** — inseparable: "occupancy is an order parameter" is contentless
  without a distinct bound to be an order parameter relative to, and "capacity != occupancy"
  is a definition unless a dynamic fills it. One claim, two regulators.
- **L3** (ephaptic = the coupling constant) — a substrate specialisation, the only leg 725a
  touches.

**Split is load-bearing, not tidiness:** fused, a 725a-shaped negative on the ephaptic
specialisation would read as a refutation of the settling core, which it would not be —
exactly the conflation MECH-499/500's own scoping doc says it exists to prevent.

**THREE PRECONDITIONS ALL CURRENTLY FALSE**, which is why `substrate_conditional` is right:
P0 unit count must be endogenous (today `ObjectFileBuffer.update()` consumes a
caller-built `List[EntityObservation]` — occupancy measures the ENVIRONMENT, not the
agent); P1 the resource horn must be expressible (today `tok.precision` has no
cross-token normalisation and capacity is a hard truncation `max_tokens=5`, so a load
sweep returns a step function BY CONSTRUCTION = vacuous PASS for the slot horn); P2
capacity and occupancy must be independently manipulable.

**A DERIVATIONAL GAP UPSTREAM OF THE SUBSTRATE ONE:** "graceful degradation then
whole-domain loss" is **asserted, not derived**. Pattern formation gives domain count and
size as functions of the control parameter; the mapping from domain size to per-item
representational FIDELITY is unargued. Checkable in a ~20-line 1-D lateral-inhibition toy
with **no REE substrate at all** — it can kill or confirm the signature before anything is
built. Nothing in the record names this probe; it is the cheapest thing available and
should precede everything else.

**Two corrections to the claim as registered:**
1. **`soft_competitive_disinhibition_settling` is the structurally WRONG SITE**, and the
   development doc's "REE has this machinery, built, one layer over" overstates it. Its
   elements are candidate TRAJECTORIES; the kernel is a discrete first-action-class
   surround (1.0 within / 0.25 across), not feature similarity; the readout returns a cost
   field to a **single argmin** — no domain-count readout and nowhere to put one; and
   divergence-ledger SCS-4 states "bounded rounds (R~3), **no convergence guarantee**", so
   "count the attractors that survive" is not well-defined on it. What transfers is the
   algorithm TEMPLATE, not a flag flip.
2. **The 725a caution is one-sided and six weeks stale.** The SAME `cross_stream_binder`
   substrate then had **MECH-456 promoted candidate -> provisional** on 2026-07-12
   (V3-EXQ-733b PASS, DV1 6/6 DV2 6/6; replicated by 733c on disjoint seeds 101-106). So
   "the ephaptic-analog binder does no functional work" is FALSE; what 725a killed is
   specifically coherence-SPECIFICITY as a selection factor.

**"THIRD ANSWER to Q-077" does not hold as written:** Q-077's own notes already say
"Hybrid 'slots+averaging' models exist in the source literature and are a third possible
answer" — so this is a *mechanism for* the already-named third, not a new third. And Q-077
is scoped to GOAL slots (SD-046/dACC) while MECH-521 is PERCEPTUAL; treating one as an
answer to the other needs an unstated substrate-generality claim.

**Binding instrument requirement inherited from 725a §8:** the fidelity DV must be GRADED
and NON-SATURATING. A raw occupancy count saturates at the capacity ceiling — the exact
failure that made 2/6 seeds uninterpretable in 725a.

---

## 6. Summary of recommended dispositions

| claim | agent recommendation | orchestrator note |
|---|---|---|
| ARC-133 | **(c)** keep, `substrate_conditional` v4 | drop the fourth-facet framing (type error); prefer OBJ-1's open individuation-strength sub-fork |
| MECH-516 | **(e)** retire/merge, OR narrow to instance 1 -> **(a)** | 2 of 4 instances wrong; notes internally inconsistent |
| MECH-517 | **(f)** defer with durable note | empirical content is a subset of MECH-516's |
| MECH-518 | **(a)** testable now | instrument must change; needs a `floor=0.0` arm |
| MECH-521 | **split**; core (c), L3 (c) as a new sibling; L1a (b) | derivational toy owed FIRST |

**Note the reciprocal collision:** MECH-516's agent recommends merging 516 INTO 517;
MECH-517's agent recommends merging 517 INTO 516. They agree the two overlap and should
not both stand as registered. That is the single decision with the largest downstream
effect.
