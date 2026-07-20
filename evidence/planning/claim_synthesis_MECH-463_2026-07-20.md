# Claim Synthesis -- MECH-463 (global-scalar arousal as variance amplifier)

- **Generated:** 2026-07-20T16:29:20Z
- **Session:** `festive-lehmann-461cee` -- "MECH-463 claim-synthesis"
- **Status:** PROPOSAL -- nothing registered in `claims.yaml`; awaiting per-child user approval
- **Routed from:** `failure_autopsy_mech463-exogenous-inertness_2026-07-20` (2026-07-20 governance)
- **Inputs read:** `failure_autopsy_mech463-exogenous-inertness_2026-07-20.{json,md}`;
  `failure_autopsy_V3-EXQ-787_2026-07-19.json`; `mech463_channel_agnosticism_scoping_spike_2026-07-19.md`;
  MECH-463 `claims.yaml` entry; `hypothesis_space_registry.v1.json` qid `arousal-variance-amplifier`;
  the 785a manifest `custom_information`; `evidence/literature/targeted_review_connectome_mech_463`
  + `targeted_review_striatal_gain_control_bounding`; `ree-v3/ree_core/predictors/e3_selector.py`;
  the 785a / 785b / 787 driver scripts.

---

## 1. Headline

**The routed decomposition is REFUSED as posed, and a different decomposition is proposed in its place.**

The cluster autopsy routed here on the argument that MECH-463 is coarse because it **fuses
amplification with concentration**. That reading does not survive the Step-3 gate: under exogenous
manipulation *both* premises fail, cleanly, with a passing expressivity control and green
preconditions on every scored arm. Splitting a jointly-falsified pair yields two falsified
children, not two testable ones -- which is precisely what the skill's anti-proliferation rail
exists to prevent.

The granularity debt in MECH-463 is real but sits on **two different axes** the autopsies did not
name:

- **(A) ROUTE fusion.** MECH-463 asserts a single mechanism across **three** global-scalar routes
  that act at **three different stages** of the selection pipeline. Its falsifier -- an
  arousal-conditioned variance decomposition of committed-selection scores -- is **structurally
  blind to two of them**. Evidence from the one tested route is being carried as evidence about
  all three. Worse, the claim's own characterisation of one route is **falsified in code**.
- **(B) REGIME fusion.** MECH-463 asserts two things: arousal changes *variance geometry*, and it
  changes *whether commitment fires*. The first is cleanly falsified. The second was measured only
  in a regime where **the commit gate is saturated open** -- so it is **untested**, not falsified.

---

## 2. Step-3 discrimination gate

| Run | Signature | Class | In cluster signal? |
|---|---|---|---|
| V3-EXQ-785 | endogeneity confound + one vacuous arm (`measurement_test_design_defect`, superseded by 785a) | test-design debt | **EXCLUDE** |
| V3-EXQ-785a | `arousal_causally_inert_on_selection_variance` @ harm_weighted; 6/6 green | genuine, non-degenerate | include |
| V3-EXQ-785b | same signature @ residue_weighted + f; 8/8 green both arms | genuine -- **replication, not a new signature** | include |
| V3-EXQ-787 | `hazard_geometry_inert`; `claim_alignment: intact` | **rival elimination**, not a failure *of* MECH-463 | include (as control) |

**Distinct genuine failure signatures of the claim itself: ONE.** 785a and 785b are the *same*
signature at three incumbent identities -- that is a **replicated single falsification**, which
strengthens it rather than making it circle. 787's own four-layer diagnosis records
`claim_alignment: "intact"` and `biological_reference: "n/a -- instrumentation-axis artifact
hypothesis, not a mechanism import"`: it eliminated a *rival*, it did not fail the claim.

> **Gate verdict on the routed framing: STOP.** On the tested route MECH-463 is a **genuine
> single-point falsification** (skill Step 3, class 3), which routes to `/governance` narrowing or
> demotion -- **not** decomposition. The registry's own ledger agrees in shape: the
> `fanout_growth_note` on qid `arousal-variance-amplifier` records the convergence as
> **CIRCLING within one axis family**, and warns "do not read the 4/4 narrowing ratio as healthy
> breadth."

**Gate verdict on the route/regime axes: PROCEED.** Findings (A) and (B) below are >= 2 distinct,
genuine, non-degenerate, substrate-ready gaps in what the claim asserts versus what any run has
measured. They clear the granularity-debt bar on an axis the cluster autopsy did not examine.

---

## 3. Finding A -- ROUTE fusion (verified in code, not inferred)

MECH-463's `functional_restatement` names three global scalars and asserts of all three that each
"applies one scalar uniformly across all K candidates and therefore cannot change an argmax."
**All four runs manipulated exactly one of them** -- the harm-urgency threshold shrinkage, via
`e3.config.urgency_weight`. Confirmed by reading the driver scripts: 785a/785b/787 all inject on
`urgency_weight` and nothing else.

The other two are not merely untested. They are **outside the falsifier's causal path**, for
reasons already established in code by the 785b scoping spike and re-verified here:

| Route | Where it acts | Can the falsifier see it? |
|---|---|---|
| Harm-urgency threshold (`e3_selector.py:2679-2686`) | on the commit gate | **Yes** -- this is the tested route |
| D1/D2 dopamine gain (`:1553-1570`, applied `:1728-1729`) | on the loop **accumulator**, *after* channel composition | **No** -- re-gains the aggregate; not an additive component in the decomposition |
| Softmax temperature (`:2682`, `:3102`) | divides the composed score *inside* the softmax | **No** -- strictly downstream of the per-candidate component vectors the shares are computed from |

So the null generalises to the other two routes **only analytically, via the argmax-invariance
argument** -- and that argument is where the claim breaks.

### A.1 The claim's premise is FALSIFIED IN CODE for the D1/D2 route

`_d1_d2_split` (`e3_selector.py:1553-1570`) does **not** apply a uniform scalar. It splits the
accumulator into two opponent populations about zero and gains them **asymmetrically**:

```
go       = relu(-accum)          # promote side
nogo     = relu(+accum)          # suppress side
d1_gain  = 1.0 + d1_da_gain * da       # potentiated by DA
d2_gain  = max(0.0, 1.0 - d2_da_gain * da)   # depressed by DA
net      = d2_gain*nogo - d1_gain*go
```

This is a **piecewise transform, asymmetric about zero**. It therefore *can* reorder any pair of
candidates whose accumulators straddle zero. The docstring says so outright: at `da == 0` the net
is "bit-identical to the additive scalar; **the dissociation is earned only once da != 0**."

**MECH-463 asserts this route cannot change an argmax. The code says it can, whenever `da != 0`.**
That is not a subtle reading -- it is the documented design intent of ARC-109. The claim
mis-classifies one of its own three routes, and the mis-classification is exactly the kind that
route-fusion hides: the D1/D2 route was never going to behave like the threshold route, and no run
has ever tested it.

### A.2 The temperature route -- already contradicted by existing evidence; NO new child proposed

Deliberately **not** proposing a child here, to avoid duplicating registered work. MECH-087 already
maps "dopamine selection-gain = E3 softmax temperature", and V3-EXQ-674 (PASS / supports,
`non_degenerate: true`) measured that **dopamine-temperature modulates decisiveness at 0.93** as a
readiness precondition. Temperature is therefore *already demonstrated non-inert* on selection under
an existing claim.

This still matters to MECH-463: its blanket "all three cannot change an argmax" is contradicted for
the temperature route by evidence **already on file**, under a different claim id. The right fix is
a cross-reference and a narrowing of MECH-463's scope, not a new claim.

---

## 4. Finding B -- REGIME fusion: the commit-gate half was measured against a saturated ceiling

MECH-463 asserts arousal "cannot change an argmax, **but DO change whether commitment fires and how
sharply**." The first half is falsified. The second half was measured **only as C3, explicitly
marked `load_bearing: false`** -- and in a regime with no headroom.

From the 785a manifest, per urgency level:

| assigned urgency | commit_rate | commit_variance_mean | effective_threshold_mean | gate margin |
|---|---|---|---|---|
| 0.04 | 0.9968 | 0.00785 | 0.3761 | **48x** |
| 0.10 | 0.9965 | 0.00983 | 0.3467 | 35x |
| 0.16 | 0.9901 | 0.01193 | 0.3294 | 28x |
| 0.22 | 0.9965 | 0.00646 | 0.3052 | **47x** |
| 0.28 | 1.0000 | 0.00710 | 0.2800 | 39x |
| 0.34 | 0.9932 | 0.01037 | 0.2570 | 25x |

The gate is `committed = variance < effective_threshold`. **The gated quantity sits 25-48x below
its own bound at every level.** Commit rate is pinned at 0.9901-1.0 (span 0.0099).

The 32% threshold reduction (0.3761 -> 0.2570) that the autopsies correctly cite as proof the
manipulation *landed* is, for this DV, **moving a ceiling that was never within an order of
magnitude of binding**. A flat commit rate here carries essentially no information about whether
arousal changes whether commitment fires -- it is a ceiling effect, not a null.

This does **not** disturb the variance-geometry nulls: those are computed on committed ticks with
green preconditions and a passing expressivity control, and they stand. It means the claim's
*other* registered prediction has never been tested.

**Independent corroboration from the lit already on file.** The `targeted_review_connectome_mech_463`
entry on Jepma et al. (2010) -- the reboxetine/citalopram/placebo null, the closest human causal
test -- reaches the same place by a different road: it notes the null is equally consistent with
MECH-359 (the scalar is too weak to steer) and with MECH-463, and names the discriminating
measurement explicitly as **"the commit gate itself: does raising the scalar change *whether* and
*how sharply* commitment fires, holding the winner fixed?"** That measurement has not been made in
a regime where it could return a signal.

**Honest risk statement.** Adding a headroom precondition to a falsified claim is exactly the move
that manufactures epicycles, and it should be resisted on reflex. The defence here is that this is
**not a new precondition invented to rescue the claim** -- "changes whether commitment fires" is in
MECH-463's registered text, was assigned its own criterion (C3), and that criterion was marked
non-load-bearing precisely *because* its author saw the mechanism was mis-signed. The unmeasured
half is original, not retrofitted. Child B2 below is nonetheless proposed as **probe-gated**, not
as a queued experiment, for the reason in its `what_would_answer`.

---

## 5. Answers to the three questions this synthesis was asked to resolve

**Q1: The ledger has all four hypotheses eliminated. What survives?**
Nothing survives *within qid `arousal-variance-amplifier` as posed* -- the frozen set is genuinely
exhausted 4/4, and the `fanout_growth_note` correctly reads the shape as circling. What survives is
outside that question's frame: the two untested routes (A) and the untested commit-gate regime (B).
Both are new questions, not surviving legs of the old one. The residual 14.1x endogenous profile is
a `mystery (known data)` node -- see §7.

**Q2: Is there a narrower still-interesting claim, or does MECH-463 retire?**
**Narrow and retain, then split.** MECH-463 should be narrowed to what was actually tested and
falsified -- *the harm-urgency threshold route's effect on committed-selection variance geometry* --
and carried to `/governance` for a status decision on that narrowed scope. The two children below
carry the parts that were never tested. Retiring the whole claim would discard finding A.1, which is
a real, code-verified defect worth registering rather than deleting.

**Q3: Are the D1/D2 and softmax-temperature routes a live remainder, or out of scope?**
**Explicitly LIVE, and asymmetrically so -- this is the load-bearing scope decision.**
- **D1/D2: live, and the claim is wrong about it.** Not merely untested: the argmax-invariance
  premise that would have let the threshold-route null generalise to it is **false in code** (§A.1).
  This is the strongest remainder. -> child A1.
- **Softmax temperature: live, but already owned.** Contradicts MECH-463's blanket premise, but the
  contradiction is already evidenced under MECH-087 / V3-EXQ-674. -> cross-reference, no new claim.
- **Threshold route: closed.** Cleanly falsified for variance geometry (§2); its commit-gate half is
  finding B.

---

## 6. Proposed children (ids are "next free at registration time", NOT reserved here)

### Child A1 -- D1/D2 opponent gain is order-changing, not uniform

| Field | Value |
|---|---|
| Proposed id | next free `MECH-4xx` |
| `claim_type` | `mechanism_hypothesis` |
| `subject` | `selection.d1_d2_opponent_gain_is_order_changing` |
| `polarity` | `asserts` (and **contradicts** MECH-463's premise for this route) |
| `status` | `candidate` |
| `epistemic_category` | `standard` |
| `depends_on` | ARC-109, MECH-463, SD-011 |
| Lit grounding | `targeted_review_striatal_gain_control_bounding` -- kohnomi2016 (DA graded lateral inhibition), chen2020 (D2 autoreceptor homeostat). **Present; no `/lit-pull` owed.** |

**Claim.** The D1/D2 dopamine gain is *not* a global scalar in MECH-463's sense. Because it gains
`relu(-accum)` and `relu(+accum)` asymmetrically about zero, a non-zero `da` reorders any candidate
pair whose accumulators straddle zero. It is therefore capable of changing an argmax and of
producing behavioural differentiation -- the opposite of what MECH-463 asserts of it.

**`what_would_answer`.** Sweep `da` exogenously (as 785a swept urgency) with `d1_da_gain` /
`d2_da_gain` at their configured values, recording per-candidate accumulators and the committed
argmin. **Supports** if the committed-candidate identity changes with `da` at a rate exceeding the
`da == 0` baseline, and if the reordering rate scales with the fraction of candidate pairs whose
accumulators straddle zero. **Refutes** if the committed identity is invariant to `da` across the
sweep -- which would mean the straddling fraction is ~0 in practice and the asymmetry, though real
in code, is behaviourally inert. **Mandatory precondition:** report the straddle fraction; if it is
~0 the run is vacuous and must be scored `precondition_unmet`, not as a null.

**Why registrable now:** the mechanism is verified in source, the instrument (per-candidate
accumulators) is the same one 785a/785b already persisted, and the falsifier has a declared
non-vacuity gate.

---

### Child B2 -- arousal's commit-gate effect is only expressible near the gate boundary

| Field | Value |
|---|---|
| Proposed id | next free `MECH-4xx` (after A1) |
| `claim_type` | `mechanism_hypothesis` |
| `subject` | `selection.commit_gate_arousal_effect_requires_boundary_regime` |
| `polarity` | `asserts` |
| `status` | **`substrate_conditional`** (not `candidate` -- see below) |
| `epistemic_category` | `standard` |
| `depends_on` | SD-011, MECH-463, MECH-359 |
| Lit grounding | `targeted_review_connectome_mech_463` -- jepma2010 (the reboxetine null, which names this exact measurement as the MECH-463/MECH-359 discriminator), astonjones2005. **Present; no `/lit-pull` owed.** |

**Claim.** MECH-463's "arousal changes whether commitment fires" is untested rather than false: it
can only express itself where the gated quantity is within the same order of magnitude as the
threshold. In every run to date the z_world running variance sits 25-48x below `effective_threshold`
and commit rate is pinned at 0.99-1.00, so the DV had no headroom.

**`what_would_answer`.** First a **scoping spike** (this is why the child is `substrate_conditional`
and probe-gated, not queued): establish whether a boundary regime -- `commit_variance` within ~2x of
`effective_threshold` -- is reachable *by configuration*, by lowering `commit_threshold`, or whether
it requires raising z_world variance. **If reachable by config:** re-run the 785a exogenous-urgency
design in that regime with commit rate as the load-bearing DV. Supports if commit rate varies
monotonically with urgency and the span exceeds an effect floor; refutes if commit rate stays flat
*with demonstrated headroom* (a mandatory precondition: median gate margin < 2x, commit rate away
from both 0 and 1). **If NOT reachable by config,** the child is substrate-gated and routes to
`/implement-substrate`, not to `/queue-experiment`.

**This is NOT re-running the decided null.** Different DV (commit rate, not variance geometry),
different regime (gate near boundary, not saturated), different precondition (headroom, which no
prior run reports). The variance-geometry framing stays closed.

> **The z_world caution applies here and is respected.** The spike may find the boundary regime
> needs higher z_world variance, which would collide with V3-EXQ-737's finding that z_world is never
> prediction-trained in the x734/737 driver family (0 of 61 `latent_stack` tensors move;
> `sd_zworld_warmup_optimizer_group` pending). **This proposal does not lean on "z_world cannot
> express it" as an established ceiling** -- it treats reachability as the open question the spike
> exists to answer, which is the correct posture while that substrate entry is unlanded. Note this
> is a live tension with both autopsies' `recommended_substrate_queue_entry.action: none`: that
> verdict is correct for the *variance-geometry* framing and may not hold for this one.

---

### Declined: a third child for the softmax-temperature route

Rejected to avoid inflating the believed tail. The route is live and does contradict MECH-463's
blanket premise, but MECH-087 already owns the temperature-as-selection-gain mapping and
V3-EXQ-674 already evidenced it (`decisiveness 0.93`). Recorded as a cross-reference in §7 instead.

---

## 7. Proposed non-claim dispositions

1. **Narrow MECH-463** to: *the harm-urgency threshold route's effect on committed-selection variance
   geometry*. On that narrowed scope it is falsified (replicated at three incumbent identities,
   expressivity control passed, leading rival independently eliminated) and is ready for a
   `/governance` status decision. The `evidence_quality_note` should record that the blanket
   three-route premise is **withdrawn**, with the reason (§A.1) and the cross-reference (§A.2).
2. **The unexplained 14.1x endogenous profile -> an open QUESTION, not a claim.** 787 eliminated
   hazard geometry *and* falsified its premise at the first stage (corr(assigned proximity, realized
   urgency) = 0.164, below the 0.2 threshold) -- so endogenous urgency does not even track hazard
   proximity, and what it *does* track is unknown. Per the autopsy this is a `mystery (known data)`
   node: the data are in hand and the frame is wrong. Recommend a **new qid** in
   `hypothesis_space_registry.v1.json` -- *"what does endogenous urgency co-vary with?"* -- rather
   than a claim, since there is no pre-registered candidate left to freeze.
   **Not written by this session** -- `commit-push-ordering-fae508` holds an active claim on that
   registry file (see §9).
3. **No `/queue-experiment` and no further lettered arousal decomposition on the 785 axis.** Both
   autopsies' refusal stands and this synthesis endorses it.

---

## 8. What this does NOT conclude

- It does **not** rescue MECH-463 as registered. The variance-amplification mechanism is falsified
  on the one route where it was testable, and this proposal leaves that falsification intact.
- It does **not** claim the substrate is the blocker. Finding A is a claim-text defect; finding B is
  an unresolved reachability question, deliberately posed as a spike rather than asserted either way.
- It does **not** treat z_world under-differentiation as a ceiling (per the standing caution).

---

## 9. Concurrency note

Two active `TASK_CLAIMS` entries touch adjacent files; neither conflicts with this proposal doc
(a new file), and **no `claims.yaml` or registry edit has been made**:

- `igw-auto-igw-189-...` (2026-07-19T12:22:08Z, staged awaiting human launch) lists
  `docs/claims/claims.yaml`. **Re-check before any registration** in Step 7.
- `commit-push-ordering-fae508` (2026-07-20T16:29:05Z) lists
  `evidence/planning/hypothesis_space_registry.v1.json`. This session therefore **did not touch the
  registry**; disposition 7.2 is left as a recommendation for whoever holds that file.

---

*Proposal only. Per the `/claim-synthesis` contract, no child is registered without explicit
per-child user approval.*
