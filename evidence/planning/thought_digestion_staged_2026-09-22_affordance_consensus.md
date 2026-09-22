# STAGED (not applied): `/thought-digestion` drafts for ARC-149, MECH-575..579

**Status: AWAITING USER REVIEW. Nothing in this file has been written to `claims.yaml`.**

- **Session:** `compassionate-pike-fe9174-digest` (Mac, umbrella worktree, interactive)
- **Drafted:** 2026-09-22, two grouped agents (Group A = ARC-149/MECH-575/576/577; Group B = MECH-578/579)
- **Scope:** the six claims registered earlier today by this same session's two ingestion passes
  (REE_assembly `66e3fee451` and `8cb8736cb1`).
- **Mode:** interactive grouped. Per the skill, ingestion did NOT draft `what_would_answer`;
  these are the first drafts and the falsification condition and disposition are the user's call.

## Headline: all six are (c) substrate-blocked / `substrate_conditional`, v4 CONFIRMED

Both agents independently agreed with the registered routing and, more usefully, **named the
specific blocking artefact for each claim** rather than restating a generic caveat. The
intake's open question -- whether the raw thoughts' "V3 assays first" steer should override the
v4 default -- is **answered NO**, with evidence, for all six.

## Corrections to claim text written THIS MORNING by the ingestion pass

The agents were instructed to verify, not assume, the cross-references. They found six defects
in text this session wrote hours earlier. All six are verified by the orchestrating session
against live claim text / source before appearing here.

| # | defect | status |
|---|---|---|
| 1 | **GFLAG-0409's premise was FALSE** -- only MECH-548 proposes an eighth rung on INV-105's ladder, and GFLAG-0235 already ruled on it (user-approved 2026-09-10). MECH-555/556's "eighth"/"ninth" are entries in the location doc's **F1-F7 routing table**, a different artifact; GOV-CONTRACT-3 explicitly *declines* a rung; INV-110 cites the ruling. | **ALREADY WITHDRAWN** by the raising session, `7415ab9c29`, status `superseded` |
| 2 | **MECH-578's TITLE cites that false premise** as its reason for carrying no ordinal | proposed fix below -- needs user approval (title edit) |
| 3 | **"MECH-140 is MECH-576's primary falsifier"** reads as a discharged test. MECH-140 has `exp=0` experimental entries, `exp_conf=0`, quadrant `plausible_unproven` -- it is an **unrun specification** | proposed fix below |
| 4 | **MECH-577 omits MECH-225 entirely** (`perception.oscillatory_multiplexing`, also v4): phase-based separation of perception / simulation / action-preparation streams. The v3-vs-v4 argument that separates MECH-561 does **not** transfer | proposed fix below |
| 5 | **MECH-577 `depends_on` MECH-575 is wrong** -- MECH-575 can be false while MECH-577 is true | proposed fix below |
| 6 | **MECH-575 calls ARC-080 "token-indexed"** -- ARC-080 resolved (OBJ-1, 2026-06-14) to three non-reducing facets TYPE/ANCHOR/TOKEN | proposed fix below |

## Cross-cutting findings (true of a whole group, not of any single claim)

**A1. "Matched capacity" is the hinge of all four Group-A falsifiers and is nowhere defined.**
Parameter count? Latent dimensionality? Optimiser budget? FLOPs? Undefined, it makes every one
of those claims unfalsifiable in exactly the direction that matters -- the losing side can always
argue the comparator was under-resourced.

**A2. All four Group-A claims are NEGATIVE EXISTENTIALS** ("no simpler thing suffices"), so a
literal `CONFIRMING:` clause overstates what any single run can deliver. The drafts use
"survives the N pre-registered simpler comparators" with N fixed in advance. ARC-145 has the
same shape; this may warrant a house-structure note rather than four local fixes.

**A3. One shared non-degeneracy gate for all of Group A.** All four are decided by the same
phenotype battery (counterfactual sensitivity, anticipation of consequence, reversibility,
repair, internal accounting for a rejected higher-reward action). **If that battery has no live
variance on the baseline arm, all four claims go vacuous simultaneously.** Written once into
ARC-149; the other three inherit it by explicit reference.

**B1. REE has NO decay-constant estimator anywhere.** Verified: `experiments/_lib/stats.py`
contains only `spearman` and `tost_equivalence`. Everything named `tau`/`decay`/`half_life` in
`ree_core/` is a *hyperparameter*, not a measurement. MECH-578/579's entire content is a
contrast between two decay constants.

**B2. There is already NEGATIVE V3 evidence against the pair's precondition.** `CrossStreamBinder`
is the only genuinely reciprocal coupling in V3. It is **built and was exercised five times**
(V3-EXQ-641/641a/720/725/725a) and its own docstring records `n_rebind` stayed **0** across
641/641a/720 -- the coupling never re-bound; it was **inert**. It is also *symmetric by
construction* (one shared `b_t` added to both streams), so MECH-578's unidirectional ablation
cells are **not constructible** on it, and it is default-OFF and acts only inside imagined CEM
rollouts. This directly refutes the intake's hopeful "may be cheaper on existing V3 substrate".

**B3. A safety gap: INV-108's scope does not reach MECH-578's case.** Both claims' notes lean on
INV-108 to forbid optimising `tau_agree`. INV-108 binds **evaluator populations whose agreement
is consumed as evidence**; MECH-578's A and B are representational subsystems whose agreement is
a *dynamical* property. A system could optimise `tau_agree` between two non-evaluator subsystems
without textually violating INV-108 -- which is exactly the false-consensus / interface-induced-
hallucination failure the source thought warns about. The draft adds MECH-578 its own explicit
do-not-optimise binding rather than relying on a guard that does not reach it.

**B4. MECH-579's falsifier is silent on the ALL-ZERO case, which is the LIKELY case.** If there
is no separation at any point, leg 1 (present at init) does not fire and leg 2 (grows uniformly)
does not fire. The notes cover it with "vacuous rather than false", which is not a reportable
outcome in this registry's vocabulary. The fix is already on MECH-579's own cited sibling:
MECH-549 carries an explicit `BOUNDARY (not refutation)` leg. The draft adopts that device.

**B5. MECH-579's dependency on MECH-578 is overstated.** It needs only that an agreement-dependent
tau contrast EXISTS AND IS MEASURABLE -- not MECH-578's *attribution* of it to reciprocal
reconciliation. If MECH-578 falls to its own falsifier (b), MECH-579 remains fully testable. As
written, a future session would wrongly retire MECH-579 on a MECH-578 refutation.

**B6. No further rung on INV-105 is warranted -- name it, do not number it.** INV-105's seven rungs
are each a property of *a single variable's status in a latent space*, monotone (rung n entails
1..n-1). "Reciprocally reconciled" has the wrong subject (a coupled pair's joint dynamics) and is
orthogonal rather than above: generic recurrence can give `tau_agree > tau_disagree` with nothing
at rung 4 bridgeable (MECH-578's own falsifier 2 concedes this), and a feedforward bridge can
reach rung 7 with no reciprocal reconciliation. Two properties dissociating in both directions are
not adjacent rungs. GOV-CONTRACT-3's "rather than as an eighth rung, to avoid a second ladder that
would invite collapse with the first" is the live precedent; GFLAG-0235 is the governing ruling.
The blank ordinal should be **removed, not filled**.

---

# GROUP A -- full drafted text

## ARC-149 -- `architecture.affordance_valuation_bridge`

**Recommended disposition: (c) substrate-blocked, `substrate_conditional`** (not
`substrate_ceiling`: never built or exercised, zero evidence either way, nothing downstream
absorbing a signal). *The falsifier is decided by a phenotype battery whose "repair" and
"internal accounting" columns have no V3 instrument at all, so the claim cannot be run rather
than merely has not been.*

```
NON-DEGENERACY PRECONDITION (this is the SHARED gate for the whole 2026-09-18
affordance-bridge group -- MECH-575 / MECH-576 / MECH-577 reference this paragraph
and deliberately do not re-derive it): the PHENOTYPE BATTERY that decides the
verdict must be LIVE and differentiating BEFORE either arm is run. This claim's
own title rules a reward comparison inadmissible in both directions, so the
deciding metric is the battery, not reward, and a battery with no variance makes
every falsifier in this group vacuous at once.
  (a) Each battery measure -- counterfactual sensitivity, anticipation of
      consequence, reversibility, repair, and internal accounting for a rejected
      higher-reward action -- must show non-zero cross-seed variance on the
      BASELINE arm alone, established before any bridge arm is run. A measure
      pinned at floor or ceiling on the baseline cannot discriminate, and a run
      scored on such a battery is vacuous regardless of which arm wins.
  (b) At least one battery measure must be demonstrably DISSOCIABLE FROM TASK
      REWARD on the baseline arm. A battery that is a monotone function of reward
      silently reduces this test to the reward-only comparison the title
      explicitly rules out.
  (c) The "repair" and "internal accounting" columns require behavioural events
      that actually occur: a non-zero count of trajectories in which a
      higher-reward action was available and NOT committed, and a non-zero count
      of recoverable failures. Zero of either makes those columns UNSCOREABLE --
      they are reported as unscoreable, never as ties.
  (d) MATCHED CAPACITY must be DEFINED AND PRE-REGISTERED before the run, not
      argued after it: parameter count, latent dimensionality and optimiser budget
      each separately matched, or the mismatch stated. The entire content of this
      commitment is a matched-capacity contrast, so an unpinned capacity
      definition makes the result unfalsifiable in exactly the direction that
      matters -- the losing side can always claim the comparator was
      under-resourced.
NAMED INERT-INSTRUMENT RISK, recorded because this group's deciding metrics run
through machinery that is known not to carry them: V3's action-object space
o_t = E2.action_object(z_world, action) (ree-v3
ree_core/predictors/e2_fast.py:571) takes no self-state argument, so any battery
column whose variation runs through body state is pinned at zero BY CONSTRUCTION
on V3 substrate. See MECH-575's precondition (i) for the full consequence. A null
produced that way measures the instrument, not the mechanism.

CONFIRMING: at matched, pre-registered capacity, the bridge arm exceeds the direct
z_world -> policy arm on the battery above, on at least TWO battery measures whose
baseline variance was established under (a), with the advantage surviving a
capacity-matched control that adds the bridge's parameters as undifferentiated
depth rather than as an action-conditioned intermediate. Because this commitment
is a NEGATIVE EXISTENTIAL ("no direct map suffices"), a single win can never
confirm it: the admissible confirming statement is "survives the N pre-registered
direct-map comparators", with N and the comparator family fixed in advance.

FALSIFYING: a direct z_world -> policy mapping at matched capacity and compute
reproduces the FULL battery -- not merely task reward -- at which point this
commitment is WITHDRAWN, not weakened, in favour of ARC-002 plus MECH-125 alone,
exactly as the title states.
Two outcomes that are explicitly NOT falsifying and must not be recorded as such:
  - a reward-only win for the direct map (the title rules it out, in terms);
  - a bridge-arm loss on a battery whose precondition (a)-(c) was unmet -- that is
    substrate_not_ready / measurement_test_design_defect, not a verdict on this
    claim.

SUBSTRATE NOTE (why this is substrate-blocked rather than merely unqueued): the
battery's own instruments do not exist. "Repair" and "internal accounting for a
rejected higher-reward action" have no V3 readout; retention of rejected
candidates past their rejection tick is MECH-487, registered and unbuilt. The
"DO NOT build in V3 / DO NOT queue an experiment" note on this claim is therefore
correct for a nameable reason, not as a generic caution.

Disposition 2026-09-22: (c) substrate-blocked, substrate_conditional. Version
routing (v4 as registered vs the source thought's "V3 assays first") remains an
OPEN /governance decision and is not resolved here.
```

---

## MECH-575 -- `representation.action_conditioned_affordance_geometry`

**Recommended disposition: (c) substrate-blocked, `substrate_conditional`.** *The affordance
representation V3 actually has (`action_object(z_world, action)`) is architecturally insensitive
to the very factors the deformation signature intervenes on, so both halves of the signature are
unsatisfiable by construction.*

```
NON-DEGENERACY PRECONDITION: inherits ARC-149's phenotype-battery and
matched-capacity gate in full -- see ARC-149's own what_would_answer, do not
re-derive it -- and adds three of its own. All three FAIL on V3 substrate as
built, which is the specific reason this claim is substrate_conditional rather
than merely unqueued.

  (i) THE REPRESENTATION UNDER TEST MUST BE SENSITIVE TO THE INTERVENED FACTOR AT
      ALL. V3's action-object space is o_t = E2.action_object(z_world, action)
      plus an optional cue bias (ree-v3 ree_core/predictors/e2_fast.py:571-605):
      it takes NO self-state argument. Interventions (ii) agent energy or body
      state and (iv) availability of a motor primitive therefore cannot move it,
      and a null on those arms would measure the instrument rather than the
      mechanism -- the failure mode the residue-bandwidth incident recorded, where
      the deciding readout returned 84 action divergences at bandwidth 8.0 AND at
      0.02, in opposite directions. REQUIRED, per factor and before any scoring: a
      factor-to-representation sensitivity check demonstrating non-zero effect on
      the ON arm. A factor failing it is reported UNSCOREABLE, never as "no
      deformation".

 (ii) THE TWO HALVES OF THE SIGNATURE MUST BE SIMULTANEOUSLY SATISFIABLE. The
      pre-registered deformation signature requires the geometry to move WHILE a
      world-identity decoder stays accurate. On V3 substrate the four factors that
      CAN move o_t -- (i) position, (iii) obstacle or route, (v) presence of a
      threatened or beneficial other, (vi) observation uncertainty -- all enter
      THROUGH z_world, so moving them moves world identity too and the SECOND
      FALSIFIER below fires trivially, by construction rather than by finding. A
      run in which no intervention can be shown to move the geometry WITHOUT
      moving z_world does not test this claim and self-routes
      substrate_not_ready_requeue. The assay presupposes an
      A_t = F(z_world, z_self, C, K) signature that V3 does not instantiate; this,
      not a generic substrate caveat, is why the claim's "DO NOT build in V3" note
      is correct.

(iii) NEIGHBOURHOOD STRUCTURE MUST BE MEASURABLE INDEPENDENTLY OF THE RANKING. The
      PRIMARY FALSIFIER turns entirely on separating "a permutation of scores"
      from "a change in neighbourhood structure", so the run must carry a metric
      on the representation that is INVARIANT TO ANY MONOTONE RE-SCORING --
      pairwise distances or local neighbour sets among action trajectories,
      computed before any score is applied. If the only available readout is the
      score vector, the primary falsifier is unreachable and the claim is
      untestable on that substrate whatever the outcome.

Also required, from the title: the world-identity decoder is trained BEFORE the
intervention and FROZEN. It is never refit on post-intervention data -- a refit
decoder can absorb the deformation and silently convert a SECOND-falsifier result
into an apparent confirmation.

CONFIRMING: for at least TWO interventions passing (i) and (ii), the
representation's post-intervention neighbourhood structure changes in a direction
that PREDICTS, held out, which trajectories became reachable or unavailable -- a
reachability decoder trained on the deformation generalises to held-out
interventions of the same factor -- while the frozen world-identity decoder's
accuracy is statistically unchanged. The deformation must additionally beat a
MAGNITUDE-MATCHED RANDOM-PERTURBATION NULL injected at the same layer, so that
"the geometry moved" cannot be satisfied by any perturbation of the right size.

FALSIFYING -- two routes, both pre-registered in the title:
  PRIMARY: the response to every intervention passing (i) is fully explained by a
  monotone re-ranking of a fixed candidate set -- pairwise distances and local
  neighbour sets among trajectories unchanged within the random-perturbation null,
  while only the score order moves. The bridge is an action-value table and this
  claim is refuted. GUARD: V3's E3 arbitrates over a list of K Trajectory objects
  carrying a scalar score, so on V3 substrate this outcome is the ARCHITECTURAL
  DEFAULT, not a discovery -- a V3 run returning it is uninformative and must not
  be scored against this claim.
  SECOND: world identity degrades whenever the geometry deforms -- the frozen
  decoder loses accuracy in proportion to the deformation -- so the bridge is not
  separable from z_world and ARC-149's intermediate object collapses into the
  world model. GUARD: per precondition (ii), this is admissible only on a
  substrate where a non-z_world route into the geometry EXISTS. Where it does not,
  the outcome is guaranteed and is not evidence.

A NULL RESULT -- the learned bridge becomes an opaque map with no usable structure
(the source thought's affordance-collapse failure mode) -- IS THIS CLAIM FAILING,
not the assay failing, PROVIDED (i)-(iii) were met. Under unmet preconditions the
same null is substrate_not_ready. The distinction is the whole difference between
a finding and a wasted run.

RELATION TO MECH-576, so the two are not read as fighting: MECH-576 asserts
DISCRETE alternating tendency states while this claim asserts a CONTINUOUS metric
field. They are at different grains -- the field is the terrain, tendency states
are coarse regimes over it -- and a discreteness result at the tendency level is
not evidence against metric structure at the trajectory level, nor the converse.

Disposition 2026-09-22: (c) substrate-blocked, substrate_conditional.
```

**Also proposed for MECH-575 (defect 6):** in `notes`, replace "ARC-080 / ARC-082's object-file
binding, which is token-indexed rather than geometric" with **"facet-indexed (TYPE / ANCHOR /
TOKEN per ARC-080's OBJ-1 resolution), not metric"**.

---
## MECH-576 -- `commitment.precommitment_tendency_alternation`

**Recommended disposition: (c) substrate-blocked, `substrate_conditional`.** *V3's E3 resolves a
decision in a single pass per tick, so the pre-commitment interval over which dwell time and
switching rate are even defined does not exist -- and the comparator the primary falsifier needs
(MECH-140) is itself an unrun specification, not a baseline.*

```
NON-DEGENERACY PRECONDITION: inherits ARC-149's phenotype-battery and
matched-capacity gate -- see ARC-149's own what_would_answer, do not re-derive it
-- and adds four.

  (i) GENUINE CONFLICT MUST OCCUR AT A NON-TRIVIAL RATE. Telemetry "recorded per
      genuine conflict" is vacuous when conflicts are rare or absent. This is the
      MECH-138 lesson verbatim: V3-EXQ-162 (2026-03-29) ran that claim's exact
      THREE_PHASE design under a random action policy and produced
      n_cancel_events = 0 in all four cells -- PARTIAL_NO_CANCEL, neither
      confirming nor falsifying. REQUIRED: a pre-declared conflict-rate floor; a
      conflict definition that is NOT "near-tie in score" alone (a score-defined
      conflict pre-supposes the scalar this claim says is insufficient); and a
      policy that is neither random nor undertrained.

 (ii) THERE MUST BE PRE-COMMITMENT TIME TO ALTERNATE IN. Dwell time and switching
      rate are undefined if the decision resolves in a single pass. V3's E3 makes
      ONE selection per E3 tick over a candidate bank; the only intra-decision
      iteration available is the HippocampalModule CEM refit loop, which is an
      OPTIMISER OVER PROPOSALS, not a competition between tendency states.
      Reading CEM refit iterations as "alternation" would be an instrument
      artefact and is INADMISSIBLE. REQUIRED: a pre-commitment interval supplying
      at least a declared minimum number of independently-resolvable deliberation
      steps, with the substrate that supplies them named.

(iii) THE TENDENCY-STATE LABEL MUST EXIST AND BE NON-DEGENERATE. The telemetry
      enumerates approach / avoid / pause / investigate / affiliate / protect /
      repair. V3 carries partial machinery for a subset (an infralimbic avoidance
      gate; a five-class action-class embedding in the escape-affordance linker)
      and MECH-483's orient/survey regime is registered but explicitly not built;
      affiliate / protect / repair have NO substrate. REQUIRED: at least THREE
      labels observed with non-zero occupancy; labels assigned by a rule fixed
      before the run; and the label NOT derived from the score. A tendency state
      read off the score vector cannot subsequently carry information the score
      does not -- that is circular and would manufacture a false confirmation of
      the very point at issue.

 (iv) THE F-DOMINANCE GATE, INHERITED FROM THE COMPARATOR. The primary falsifier's
      comparator is MECH-140's concurrent soft-competitive model, and MECH-140
      carries its own unmet precondition: the settling must operate over a field
      that is not F-collapsed, against MECH-439's measured ~88-89 percent
      F-variance monopoly. Over an F-collapsed field both arms are simply the
      F-winner and the contrast cannot discriminate. This claim therefore inherits
      MECH-439's clearance and MECH-488's gates (gap_norm regaining genuine
      cross-seed spread, gap_spread_seeds >= 2). Do not run before they hold.

Additionally: DECISION DIFFICULTY must be measured and available as a covariate,
because the SECOND FALSIFIER below is explicitly conditional on controlling for it.

CONFIRMING: with (i)-(iv) met --
  (a) the pre-commitment record shows discrete state occupancy whose dwell-time
      distribution is distinguishable from the continuous-mixture null generated by
      the SAME substrate under a concurrent-summation model at matched capacity;
  (b) dwell time and switching rate predict the three-regime distinction --
      productive deliberation, pathological flicker, perseveration -- OUT OF SAMPLE
      and AFTER decision difficulty is partialled out; and
  (c) final dominance is better predicted by a candidate's stability, duration or
      constraint-survival than by its peak instantaneous score, on held-out
      conflicts.
Per the group's shared structure (ARC-149), the admissible confirming statement is
"survives the N pre-registered concurrent comparators", not "confirmed".

FALSIFYING -- two routes, both pre-registered in the title:
  PRIMARY: a concurrent soft-competitive model with no alternation -- tendencies
  co-active and summed, as MECH-140's soft-competitive disinhibition already
  permits -- reproduces BOTH the commitment outcomes AND the conflict-resolution
  latencies at matched capacity. The alternation is epiphenomenal and this claim is
  refuted. TWO GUARDS, both load-bearing: (1) THE COMPARATOR MUST BE BUILT AND RUN,
  NOT ASSERTED. MECH-140 has ZERO valid experimental rows -- the V3-EXQ-710 finding
  was withdrawn on instrument-validity grounds 2026-07-20 and its own falsifier is
  still unmet -- so "MECH-140 covers this" is a SPECIFICATION, not a baseline, and
  citing MECH-140's existence does not discharge this falsifier. (2) Latencies must
  be matched as a SCORED OUTCOME, not incidentally; outcome-only matching is
  insufficient because the claim's content is that the dynamics, not the verdict,
  carry the distinction.
  SECOND: dwell time and switching rate carry no information about the
  deliberation-versus-pathology distinction once decision difficulty is controlled
  for -- the telemetry is descriptive only and the claim's discriminating content is
  unreachable. This is the likelier of the two outcomes and is a FINDING, not a
  failed run.

DIRECTIONAL NOTE, so a result is not mis-filed: MECH-488's gap_norm is precisely
the instantaneous scalar compression this claim predicts is insufficient. A run in
which gap_norm ALONE matches the alternation telemetry's predictive power on (b)
is the SECOND FALSIFIER firing and is recorded AGAINST this claim -- not as
support for MECH-488, whose own falsifier is a different contrast entirely.

Disposition 2026-09-22: (c) substrate-blocked, substrate_conditional.
```

**Also proposed for MECH-576 (defect 3):** reword its `notes` line "MECH-140 is in fact
MECH-576's primary falsifier" to **"MECH-140 LICENSES the comparator model that is MECH-576's
primary falsifier; that comparator has NEVER BEEN RUN (MECH-140 carries exp=0 entries,
exp_conf=0, quadrant plausible_unproven)"**. As written it can be read as already-discharged.
**(defect: MECH-432 edge)** add a disambiguating note: MECH-432 is about WHERE the comparison
lives (across two substrates); MECH-576 is about its TEMPORAL FORM. Neither entails the other.

---

## MECH-577 -- `representation.sensorimotor_phase_subspace_gradient`

**Recommended disposition: (c) substrate-blocked, `substrate_conditional`.** *The four-phase
partition does not exist in V3 (SD-032a's `operating_mode` is a different partition and
substituting it would yield evidence about MECH-261 instead), and the load-bearing
alternative-preservation column needs MECH-487, registered and unbuilt.*

```
NON-DEGENERACY PRECONDITION: inherits ARC-149's phenotype-battery and
matched-capacity gate -- see ARC-149's own what_would_answer, do not re-derive it
-- and adds four.

  (i) THE FOUR PHASES MUST EXIST AS AN INDEPENDENTLY-ESTABLISHED PARTITION.
      Orienting, prospective rollout, commitment preparation, and execution /
      feedback control must be segmentable by a rule FIXED BEFORE THE RUN and NOT
      derived from the latent under test. Segmenting phases BY the latent and then
      measuring phase-exclusive dimensions IN that latent is circular and is the
      single most likely route to a false positive here. Each phase needs a
      declared minimum number of scored ticks; a phase with near-zero occupancy
      makes its exclusive dimensions unestimable and is reported UNSCOREABLE.
      TWO SUBSTITUTIONS ARE EXPLICITLY INADMISSIBLE:
        - DO NOT substitute SD-032a's operating_mode ({external_task,
          internal_replay, internal_planning, offline_consolidation}). That is a
          different partition -- engagement regime, not position within an action
          -- and is what MECH-261 gates writes on. A result obtained over it is
          evidence about SD-032a / MECH-261, not about this claim.
        - DO NOT substitute MECH-561's phi. MECH-561's phase is an ENDOGENOUS
          CYCLIC coordinate indexing an inter-engine communication subspace and is
          implementation_phase v3; this claim's phase is a NON-CYCLIC task /
          processing coordinate at v4. A V3 phase-as-address result is not evidence
          here in either direction. This claim's notes already say so; this
          precondition makes it operative at run time.

 (ii) DIMENSIONALITY ESTIMATES MUST BE SAMPLE- AND CAPACITY-MATCHED ACROSS PHASES.
      The shared-versus-exclusive split is trivially driven by per-phase row count.
      REQUIRED: equal (or explicitly resampled) rows per phase, plus a BIN-COUNT
      SWEEP demonstrating the split is not a function of the count -- the same
      guard MECH-561's own precondition (c) carries for its principal angles.

(iii) THE ALTERNATIVE-TRAJECTORY READOUT MUST BE LIVE. The load-bearing
      measurement, named as such in the title, is whether execution-specific
      dimensions improve closed-loop control WITHOUT erasing alternative-trajectory
      information earlier than commitment requires. That requires an
      alternative-trajectory readout with DEMONSTRATED NON-ZERO INFORMATION during
      the rollout and preparation phases on the baseline arm. If alternatives are
      already uninformative pre-commitment, "erased too early" is unmeasurable and
      the load-bearing column is dead before the run starts. This is where the
      claim most concretely blocks on V3: retention of rejected candidates past
      their rejection tick is MECH-487, registered and unbuilt.

 (iv) CLOSED-LOOP CONTROL PERFORMANCE MUST HAVE HEADROOM IN BOTH DIRECTIONS on the
      baseline arm. Both falsifiers are of the form "a simpler representation
      MATCHES it at matched capacity", so floor or ceiling saturation makes both
      unreachable simultaneously and the run returns no verdict in either
      direction.

Per the title: a binary test for decodability, or for the presence of an
attractor, discriminates none of these outcomes and is NOT ADMISSIBLE EVIDENCE
here -- it satisfies no precondition above and decides no falsifier below.

CONFIRMING: with (i)-(iv) met --
  (a) a shared component exists whose decision-relevant world variables remain
      stably decodable across all four phases, measured with a FROZEN decoder;
  (b) phase-exclusive components are recoverable above a PHASE-LABEL-PERMUTATION
      null;
  (c) the degree of overlap VARIES SYSTEMATICALLY ALONG THE PATH rather than being
      constant -- this is the claim's own differentiator, and a constant-overlap
      result is NOT confirming even when (a) and (b) both hold;
  (d) execution-specific dimensions measurably improve closed-loop control; AND
  (e) they do so WITHOUT reducing alternative-trajectory information before the
      commitment boundary, relative to the matched control.
  (e) is load-bearing: (a)-(d) holding while (e) fails is the source thought's
  "premature narrowing" failure mode and is a finding AGAINST this claim's value,
  not for it.

FALSIFYING -- two directions, both pre-registered in the title:
  PRIMARY: a fully shared representation -- a single undifferentiated latent
  serving every phase -- matches closed-loop control performance at matched
  capacity, in which case phase-exclusive structure is unnecessary.
  SECOND, in the opposite direction: a fully serial pipeline -- perception
  completes, then planning completes, then execution begins, with no shared
  component -- matches it, in which case the shared world-anchored component is
  unnecessary.
  Both inherit ARC-149's matched-capacity definition requirement (its precondition
  (d)); an unpinned capacity definition makes both routes unfalsifiable in exactly
  the direction that matters. A run in which NEITHER comparator is actually built
  and run returns NO VERDICT -- asserting either comparator from architecture is
  not a result.

Disposition 2026-09-22: (c) substrate-blocked, substrate_conditional. Of the four
claims in this group this is the most separable from ARC-149 -- the four
processing phases are properties of the sensorimotor path and exist whether or not
the bridge does -- and is therefore the likeliest candidate for a /governance V3
re-route. The two V3 gaps that would have to close first are named in (i) and
(iii): a phase partition that is not SD-032a's operating_mode, and a live
alternative-trajectory readout (MECH-487).
```

**Also proposed for MECH-577 (defects 4 and 5):**
- **`depends_on: MECH-575` -> move to `related`.** MECH-575 can be false while MECH-577 is
  true: if the affordance representation is a ranked candidate list with no neighbourhood
  structure (MECH-575 refuted), one can still measure shared-vs-phase-exclusive dimensionality
  across the four phases on that list's latent and find exactly the gradient MECH-577 predicts.
  None of MECH-577's four measurements requires metric structure over action trajectories. The
  edge as written would let a MECH-575 refutation be read as pre-empting MECH-577.
- **Add a MECH-225 disambiguation** (and probably a `related` edge). MECH-225
  (`perception.oscillatory_multiplexing`, also **v4**) asserts phase-based separation of
  perception / simulation / action-preparation streams -- nearly isomorphic to MECH-577's
  orienting / rollout / preparation. The v3-vs-v4 argument that separates MECH-561 **does not
  transfer**. Proposed distinction: MECH-225 partitions by STREAM TYPE using an OSCILLATORY
  FREQUENCY BAND; MECH-577 partitions by POSITION WITHIN AN ACTION using a non-cyclic task
  coordinate, and MECH-577's two load-bearing predictions (overlap varies systematically along
  the path; execution dimensions must not erase alternatives early) are absent from MECH-225.

---
# GROUP B -- full drafted text

## MECH-578 -- `representation.agreement_dependent_timescale_separation`

**Recommended disposition: (c) substrate-blocked, `substrate_conditional`, v4 CONFIRMED.**
*Three required instruments absent, and the one candidate coupling is symmetric-by-construction,
default-off, imagined-rollout-only, and already measured inert.* Explicitly **not** (e) excrete
and **not** (g) merge -- both were checked: the assays are disjoint from MECH-548's and the
readouts are different shapes, so a merge would lose a real experiment.

```
NON-DEGENERACY PRECONDITION (six parts; this claim's entire content is a comparison of two
decay constants, so an unmet precondition makes the comparison uninterpretable rather than
null). (P1) RECIPROCAL AND PER-DIRECTION ABLATABLE: influence must be measured to flow in BOTH
directions between A and B within the loop under test, and each direction must be separately
removable. Verified absent 2026-09-22: V3 has no such coupling. CrossStreamBinder
(ree-v3 ree_core/latent/cross_stream_binder.py:205,225-230) is SYMMETRIC BY CONSTRUCTION --
one shared b_t added to both streams, no A->B weight distinct from B->A -- so falsifier (1)'s
unidirectional cells are NOT CONSTRUCTIBLE on it; it is default-OFF
(cross_stream_binding_enabled, utils/config.py:928) and acts only inside imagined CEM rollouts,
not the online loop (:70-73). E1<->E2 is one-directional (E1->E2 action_bias only,
agent.py:6128,6306). ARC-110's M_cross (e3_selector.py:770,2602-2614) is the only per-direction
addressable coupling but carries no persistent joint state to perturb.
(P2) THE COUPLING MUST BE MEASURABLY LIVE, NOT MERELY ENABLED -- a non-zero measured effect in
each direction separately, reported before any tau is read. STANDING NEGATIVE RESULT: across
V3-EXQ-641/641a/720 the binder recorded n_rebind = 0 and cross-stream coherence carried no
selection information beyond prediction error (cross_stream_binder.py:11-32). An inert coupling
makes both decay constants properties of the UNCOUPLED substrate, and the comparison is vacuous
whatever it returns.
(P3) PERTURBATION MAGNITUDE MATCHED AT DELIVERY, in the metric the decay is read in -- not a
matched nominal sigma. Use the rms_ref discipline of consolidation_lesion_harness.diffuse_perturb
(experiments/_lib/consolidation_lesion_harness.py:294-300) so delivered magnitude is numerically
identical across the agree and disagree arms, and REPORT the delivered norms. An unmatched pair
measures the perturbation, not the coupling.
(P4) tau RESOLVABLE ABOVE NOISE AND WITH DEMONSTRATED RANGE: a fitted decay constant with
seed-level CIs that do not span the agree/disagree difference, PLUS a positive control -- a
manipulation known to move tau -- so a null is distinguishable from a flat instrument. A readout
that returns the same value across a wide sweep of the quantity it is supposed to track is
measuring itself (the residue-bandwidth precedent: 84 action divergences at bandwidth 8.0 AND
0.02, in opposite directions).
(P5) ON-MANIFOLD PERTURBATION (interface_probe.manifold_guard, experiments/_lib/
interface_probe.py:1366): a perturbation landing off-distribution decays at the rate of the
return-to-manifold dynamics, which is not the quantity claimed.
(P6) NON-TAUTOLOGY (MECH-558's third binding, applied here): agreement and disagreement must be
labelled WITHOUT reference to the decay being measured and without reference to the outcome. A
tau contrast validated against an agreement label derived from persistence is circular.

BINDING (INV-108 part (i), stated here because INV-108's own scope may not reach this case --
see the governance note on its evaluator-only wording): tau_agree is a DIAGNOSTIC READOUT and
must NEVER become an optimisation target, a reward term, or a teacher signal. A system trained
to maximise the separation manufactures the observation and falsifies nothing. Falsifier (3) is
the operational guard.

CONFIRMING: tau_agree > tau_disagree at matched DELIVERED perturbation magnitude, by a margin
scaled on the seed-level SD of the per-seed (tau_agree - tau_disagree) difference plus a
pre-registered absolute floor -- AND all three pre-registered ablations abolish it.
(1) COUPLING-DIRECTION: the separation is present under intact bidirectional coupling and ABSENT
in EVERY other cell -- A->B only, B->A only, and both removed.
(2) CORRESPONDENCE SCRAMBLE: the separation does NOT survive permuting which dimensions are
connected at preserved total coupling magnitude (report the preserved magnitude, not just the
intent to preserve it).
(3) FALSE-CONSENSUS CHALLENGE: a shared-but-incorrect injected latent does not acquire agree-mode
persistence; or if it does, an independent environmental error signal still destabilises it
within the horizon the system actually uses the interface.
Report the four coupling cells and the scramble as ONE grid. A partial result -- separation
abolished by the scramble but reproduced by a unidirectional cell -- routes to persistence, and
is NOT a weakened version of this claim.

FALSIFYING (four, which fail independently and must be reported separately):
(a) tau_agree ~= tau_disagree at matched delivered magnitude on a coupling measured live in both
directions -- no agreement-dependent separation exists.
(b) ANY unidirectional condition reproduces the separation -- what is measured is persistence,
not reciprocal reconciliation; the reciprocal attribution is wrong and the claim is REFUTED, not
narrowed. (Note for MECH-579: this leg does not take MECH-579 with it -- see its scope note.)
(c) the separation survives a correspondence scramble at matched coupling magnitude -- generic
recurrence rather than learned like-to-like correspondence.
(d) the false-consensus challenge shows agreement alone stabilising an incorrect shared signal
that independent environmental error cannot destabilise -- the mechanism manufactures coherence
without correctness and MUST NOT BE BUILT. This refutes the claim's architectural value even if
(a)-(c) all pass, and is the one leg whose failure is a build prohibition rather than a scientific
null.

BOUNDARY (not refutation): no coupling in the substrate is simultaneously reciprocal,
per-direction ablatable, and measurably live. The claim is then UNTESTED. Reporting that
situation as a null (a) is the specific error this precondition exists to prevent, and given P1
and P2 it is currently the expected outcome of any V3 attempt.

SEPARATION FROM NEIGHBOURS, so a result routes correctly: vs MECH-548 -- the discriminator is
whether the SENDER's own state is updated by the receiver within the loop (MECH-548: no, A is
exogenous and the loop is B->B through a receiver-conditioned T; here: yes). MECH-548's assay is
clean-base vs cumulative over N consumer steps and its signature is monotone degradation of ONE
quantity; this claim's assay is the four-cell grid and its signature is a CONTRAST between two
constants. Neither run yields the other's readout. vs MECH-539 -- a property of the MAP, checkable
with both endpoints frozen, vs a property of the CLOSED LOOP. vs ARC-139 -- ARC-139 says
representational sameness is not required; this says what replaces it dynamically.

Disposition 2026-09-22: (c) substrate-blocked, substrate_conditional -- three required instruments
absent (per-direction-ablatable reciprocal coupling; ANY decay-constant estimator, none exists in
ree_core/ or experiments/; a magnitude-preserving dimension-correspondence scramble). All four are
complicated (buildable). LAYERED FINDING, recorded because it changes what a future build must do
FIRST: the coupling half is not merely unbuilt -- CrossStreamBinder is built, was exercised across
V3-EXQ-641/641a/720/725/725a, and was measured INERT (n_rebind = 0), which is a substrate_ceiling
signature sitting beneath the substrate_conditional block on the measurement. Establishing that
the coupling actually binds is complex (probe-gated) and is UPSTREAM of building any tau
estimator. v4 CONFIRMED against the intake's open routing question: assay 1 is NOT cheaper on
existing V3 substrate. The proposed further rung should be NAMED, NOT NUMBERED, and the blank
ordinal REMOVED rather than filled -- it is a property of a coupled pair's dynamics, not of a
variable's status in a latent space, and it dissociates from INV-105's ladder in both directions
(GOV-CONTRACT-3's "rather than as an eighth rung" is the governing precedent; GFLAG-0235 is the
governing ruling).
```

**Also proposed for MECH-578 (defect 2):** its TITLE currently justifies carrying no ordinal by
citing the now-withdrawn GFLAG-0409 premise ("because four claims ... already each describe
themselves as adding an eighth rung"). That sentence is **false** and is in a registered claim
title. Replace with the orthogonal-axis reason (finding B6), citing GOV-CONTRACT-3's precedent
and GFLAG-0235's ruling, and **remove** the blank ordinal rather than leaving it pending.

---

## MECH-579 -- `development.consensus_topology_carved_by_pruning`

**Recommended disposition: (c) substrate-blocked, `substrate_conditional`, v4 CONFIRMED** --
blocked FOUR times independently: it inherits MECH-578's entire block, and adds MECH-549's arm-D
export path (**unspecified**, not merely unbuilt), MECH-550's retention criterion (nothing in
`ree_core/` scores any route for retention) and MECH-362's capacity-schedule substrate (no
matching `sd_id`) -- all three verified 2026-09-15 and re-confirmed unchanged 2026-09-22.

```
NON-DEGENERACY PRECONDITION: inherits ALL of MECH-578's P1-P6 UNCHANGED (reciprocal and
per-direction-ablatable coupling; coupling measurably live; matched delivered perturbation
magnitude; tau resolvable above noise with demonstrated range; on-manifold perturbation;
non-tautological agreement labelling). Four further parts:
(P7) A measurable NON-ZERO agreement-dependent tau contrast must exist at SOME point in the
developmental window. This is the inherited gate and it is what makes the all-zero case
reportable -- see BOUNDARY.
(P8) A developmental TRAJECTORY must actually be TRAVERSED, not two fixed configurations compared
(MECH-362's own precondition, adopted verbatim): a dense early coupling progressively reduced,
with the INTERMEDIATE states measured. A dense-config vs sparse-config A/B tests the endpoints,
not the trajectory this claim asserts.
(P9) Agreement modes must be separable into BEHAVIOURALLY USEFUL and not, by an organism-level
readout computed INDEPENDENTLY of the tau measurement. The selectivity half is this claim's whole
novelty over ordinary subtractive sparsification; without an independent usefulness label it
cannot be assessed, and the claim collapses into MECH-362.
(P10) For the SECOND FALSIFIER only -- MECH-549's arm-D export path: the mature connectivity,
sparsity mask and interface structure produced by the dense-then-pruned arm must be EXPORTABLE and
re-instantiable at initialisation at matched final capacity. Verified on MECH-549 2026-09-15 and
unchanged: UNSPECIFIED, not merely unbuilt. Also unmet: MECH-362's capacity-schedule substrate
(verified 2026-09-15, no matching sd_id in substrate_queue.json) and MECH-550's retention
criterion (verified 2026-09-15, nothing in ree_core/ scores any route for retention).

CONFIRMING (three legs, ALL required):
(i) EMERGENCE -- the agreement-dependent tau contrast is ABSENT OR AT NOISE at initialisation and
grows over learning, measured on the traversed trajectory of P8, not inferred from two endpoints.
(ii) SELECTIVITY -- at maturity the contrast is materially larger for agreement modes independently
scored BEHAVIOURALLY USEFUL than for agreement modes that are not, with a selectivity index
exceeding a pre-registered floor and the difference scaled on the seed-level SD. This is the leg
that separates a consensus TOPOLOGY from a sparse weight matrix.
(iii) HISTORY IRREDUCIBILITY -- the mature selective topology is NOT reachable by training directly
at the mature connectivity at matched final capacity and matched compute (MECH-549 arm D).
(i) and (ii) WITHOUT (iii) is fully consistent with "pruning found a good architecture"; (iii) is
what makes this a developmental claim rather than an architecture-search result.

FALSIFYING (four, failing independently, reported separately):
(a) the separation is present at initialisation at full mature magnitude -- a property of the
coupling ARCHITECTURE, not a learned topology. This claim is refuted while MECH-578 may still stand.
(b) the separation grows but UNIFORMLY across all agreement modes, irrespective of which cash out
in adaptive behaviour -- this is subtractive sparsification of the coupling, already owned by
MECH-362, and this claim adds nothing beyond it.
(c) arm D matches arm B at matched final capacity and matched compute -- the developmental ordering
claimed here is unnecessary (MECH-549's own primary falsifier, applied to the interface).
(d) the retained structure is fully predicted by coupling-weight MAGNITUDE at the point of pruning,
with the retained-set overlap against a magnitude-pruning control at or near total -- the retained
object is a sparse weight matrix, not a map of where agreement is worth having, and MECH-550's
magnitude-pruning rival owns the result. Report the retained-set overlap; identical retained sets
make the comparison vacuous whatever the competence outcome (MECH-550's own precondition).

BOUNDARY (not refutation) -- AND THIS IS THE LIKELY CASE, NOT AN EXOTIC ONE, WHICH IS WHY IT IS
NAMED HERE RATHER THAN LEFT TO PROSE: no agreement-dependent tau contrast is measurable at ANY
point in the developmental window. There is then no topology for development to carve and this
claim is UNTESTED -- neither confirmed nor refuted. It MUST be reported in that category and MUST
NOT be recorded as a null, because the all-zero case fires NEITHER falsifier (a) (nothing is
present at initialisation) NOR falsifier (b) (nothing grows). Same device as MECH-549's own
BOUNDARY leg, which this claim's second falsifier already borrows.

SCOPE NOTE ON THE DEPENDENCY (correcting the strong reading in this claim's notes): this claim
requires only that an agreement-dependent tau contrast EXISTS AND IS MEASURABLE -- not that
MECH-578's attribution of it to RECIPROCAL RECONCILIATION is correct. If MECH-578 is refuted by
its falsifier (b) -- a unidirectional condition reproduces the separation, so the quantity is
persistence rather than reconciliation -- this claim remains FULLY TESTABLE about whether that
persistence becomes developmentally selective and behaviourally targeted. Do NOT read a MECH-578
refutation as retiring this claim. The genuine vacuity condition is the BOUNDARY above (no
contrast at all), not a MECH-578 refutation.

SEPARATION FROM NEIGHBOURS: vs MECH-362 -- within-system memory connectivity (CA3 tabula plena)
vs a cross-system interface, and what the retained structure MEANS rather than how sparse it is.
vs MECH-550 -- MECH-550 supplies the retention CRITERION this claim assumes; this claim says what
is retained in the cross-system case. vs MECH-549 -- MECH-549 supplies falsifier (c) directly and
is why that falsifier is stated in its terms rather than reinvented.

Disposition 2026-09-22: (c) substrate-blocked, substrate_conditional, and blocked FOUR TIMES
INDEPENDENTLY. v4 CONFIRMED; this is the better-routed of the pair and its version placement was
never in doubt. The falsifier hole (the all-zero case fires neither stated falsifier) is a
claim-text defect routed to /governance, not a reason to re-categorise.
```

---

# What needs your decision

1. **Apply the six `what_would_answer` blocks as drafted?** (All six disposition (c),
   `substrate_conditional` unchanged, v4 unchanged. No proposals minted -- correct, since all
   six carry DO-NOT-QUEUE notes.)
2. **Apply the six claim-text corrections** (defects 2-6 above, plus the MECH-579 BOUNDARY leg
   and scope note, which are inside the drafted blocks)?
3. **The MECH-578 do-not-optimise binding** -- accept it inside MECH-578, or widen INV-108's
   scope instead? (Finding B3. The agent recommends the former as narrower and cheaper.)
4. **Anything to send to `/governance` rather than apply here?** My read: nothing -- GFLAG-0409
   is withdrawn, GFLAG-0235 already settled the rung question, and the rest are corrections to
   text this session wrote today.
