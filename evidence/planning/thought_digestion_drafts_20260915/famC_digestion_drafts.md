# Digestion drafts -- Family C (2026-09-09 convergence/divergence family)

**Date:** 2026-09-15
**Session:** thought-pipeline-20260915
**Scope:** NOT part of the Stage 2 intakes. Drafts only. Nothing here has been written to
`claims.yaml`; the `what_would_answer` drafts for EXISTING claims are proposals to `/governance`, not
edits.

**Extract-before-invent note.** Wherever possible the falsifier language below is lifted from the
thoughts themselves (hub section 11 "Falsifiers and failure modes", dual section 10 "Failure modes",
formal notes sections 8 and 10, diversity section 12, aha section 9) and from the preregistered criteria
of assays 001-006, which are already-executed versions of several of these tests.

**Currency check performed.** Every blocker or run cited below was checked against
`evidence/experiments/`, `ree-v3/experiment_queue.json` and `evidence/planning/substrate_queue.json` as
of 2026-09-15. Two findings are recorded inline: MECH-441's HOLD is stale (its gate resolved in the
negative and the block says a rewrite is owed), and `sd_epistemic_deficit_multitarget_readiness` is
`implemented_pending_validation` after V3-EXQ-964 showed a constant readout in short episodes.

---

## Part 1 -- Proposed new claims

### NEW-MECH-1 -- independence-aware convergence topology

**NON-DEGENERACY PRECONDITION (three parts).**
(P1) At least TWO evaluator routes must be simultaneously LIVE and CONSEQUENTIAL -- actually computed
and actually consumed by a decision -- not present as default-OFF flags or diagnostic-only counters. The
bar is non-trivial: `use_loop_segregation`, `use_loop_local_eligibility_traces`,
`use_model_disagreement_curiosity` and `use_coalition_controller` all default False, and
`curiosity_learning_progress_source` defaults `"broadcast"`.
(P2) The routes must be capable of DISAGREEING in the measured window: a recorded non-zero rate of
`loop_cross_loop_winner_disagreement` (or its equivalent in whatever population is measured). An
evaluator population that never disagrees makes every convergence statistic vacuous.
(P3) The dependency structure must be MANIPULABLE or at least ESTIMABLE without using the outcome label.
A convergence metric validated against a dependency estimate that was itself derived from the answer is
the tautology the E3 commensurability work already caught once.

**CONFIRMING.** In a setting where two states are matched on aggregate weighted confidence but differ in
support topology, an independence-corrected estimator (i) assigns them materially different confidence
in the direction of the true accuracy difference, (ii) remains calibrated at both endpoints within a
preregistered bound, and (iii) is beaten only by exact joint Bayes. Already met in the frozen synthetic
world: assay 001 gave an independent-vs-copied unanimity confidence gap of 0.28420 against a
reliability-only endpoint delta of 0.00037, with endpoint calibration errors of 0.00096 and 0.00139;
assay 002 gave MIXED_3_PLUS_2 Brier of 0.18594 / 0.16697 / 0.15227 / 0.15073 for reliability-only /
global `N_eff` / cluster-aware / exact Bayes. The claim is NOT confirmed for REE until the same
separation is demonstrated over REE's own channels.

**FALSIFYING.** Any of: (a) correct reliability and covariance weighting explains every benefit with no
separate meta-observable needed (hub falsifier 2, stress-test falsifier 1); (b) the benefit disappears
once correlated evaluators are collapsed into one effective source (hub falsifier 3); (c) independence
cannot be estimated cheaply enough for the correction to be affordable (stress-test falsifier 2);
(d) a single dissenting high-reliability channel must routinely override consensus, making aggregate
convergence behaviourally irrelevant (hub falsifier 5); (e) in REE specifically, no evaluator population
exists whose members disagree often enough for a topology to be non-degenerate.

**DISPOSITION: (c) substrate-blocked -- substrate_conditional.** Nothing in `ree_core/` computes any
dependency-corrected quantity; the code is absent, so the signal has never been exercised. With one
qualification the orchestrator should weigh: a SHADOW-ONLY version (log existing agreement diagnostics
against later outcomes, no causal role) is arguably disposition (a) testable now, because
`loop_cross_loop_winner_disagreement`, `_loop_voted`, `model_disagreement_range` and the
epistemic-deficit disagreement input all already exist in V3. Flagged for `/governance` routing; not
decided here.

### NEW-MECH-2 -- evidence dependency vs downstream leverage

**NON-DEGENERACY PRECONDITION.** (P1) The query/allocation choice must be REAL -- there must be at least
two competing unresolved targets whose resolution has different consequence, or the allocation policy has
nothing to get right. (P2) The two graphs must be genuinely ANTI-ALIGNED in at least one measured cell:
if evidence independence and downstream leverage happen to covary, a conflated policy scores correctly
for the wrong reason and the experiment tests nothing. Assay 004's forced pair is the template -- five
independent reasons with leverage 1 against five copies with leverage 8. (P3) A pure-noise query channel
must be present so that a selector attracted to irreducible disagreement is visibly punished.

**CONFIRMING.** A policy that represents the two graphs separately achieves materially lower allocation
regret than one that uses either as a proxy for the other, does not select the irreducible-noise channel,
and degrades gracefully when provenance is missing or wrong provided provenance is carried as a
probability rather than a label. Already met synthetically: assay 003 (topology-aware VOI regret 0.00490
vs global-`N_eff` 0.01964; irreducible-noise selection 20.24% by raw disagreement vs 0.005%); assay 004
(forced anti-conflation pair, oracle-following 16.82% conflated vs 100% factorised); assay 005 (93.24%
of oracle utility under 50% missing and 20% wrong provenance; soft beats hard by regret ratio 0.678);
assay 006 (dynamic-both regret 0.01107 vs static 0.04969).

**FALSIFYING.** (a) structured disagreement fails to predict information value above ordinary
uncertainty, expected information gain or learning progress (hub falsifier 6, stress-test falsifier 3) --
note that MECH-314b, MECH-314c and MECH-482 are the REE-native versions of those baselines and are the
ones to beat; (b) the factorisation's advantage disappears as soon as provenance or leverage is imperfect
(assay 005's explicit test, which it survived synthetically and may not survive in REE); (c) estimating
the dependency and impact relations costs more compute than the decisions they improve (dual failure mode
"meta-control explosion"); (d) in REE, cross-model leverage turns out to be unmeasurable because no
representation of downstream consumers exists.

**DISPOSITION: (c) substrate-blocked -- substrate_conditional**, with the same shadow-diagnostic
qualification as NEW-MECH-1. The leverage half is the harder gap: nothing in `ree_core/` represents which
consumers an unresolved uncertainty would update.

### NEW-INV-1 -- convergence detected, not trained

**NON-DEGENERACY PRECONDITION.** The evaluator population must be TRAINABLE toward agreement for the
prohibition to have content. An ensemble of frozen or arithmetic evaluators cannot co-adapt, so a test
run on one measures nothing. There must also be a measurable independence quantity (pairwise residual
correlation or unique-failure coverage) whose COLLAPSE is the predicted harm.

**CONFIRMING.** Ladder Stage 7 / diversity section 12: three arms -- (A) performance only, (B) agreement
explicitly rewarded, (C) local competence plus unique-coverage reward with convergence observed
externally. C preserves more robust cross-view evidence than B under distribution shift, shared upstream
perturbation, specialist-only regime and evaluator ablation, EVEN THOUGH B has higher raw agreement. The
thought states this prediction itself and states the consequence of its failure: "If not, the strong
diversity-preservation claim weakens."

**FALSIFYING.** (a) B matches or beats C on every robustness readout, i.e. rewarding agreement is free;
(b) preserving evaluator diversity costs more competence than it saves (stress-test falsifier 4);
(c) error correlation does not actually rise under an agreement objective, i.e. the incentive coupling
the claim asserts does not exist.

**DISPOSITION: (c) substrate-blocked -- substrate_conditional**, and additionally **(f) defer** on the
V3 question specifically: V3 has no agreement objective to prohibit, so the invariant guards a future
architecture. Its falsifier is synthetic-ensemble work that needs no REE substrate and could be run at
any time; that is an argument for keeping the claim rather than excreting it.

### NEW-MECH-3 -- cross-model restructuring as an insight-candidate event

**NON-DEGENERACY PRECONDITION.** (P1) There must be a representation-revision MECHANISM for the detector
to fire over. Today there is not: MECH-531 states that
`ree_core/entities/object_file_buffer.py` has no merge/split path, and MECH-529 is a v4 claim. (P2) The
views must be EFFECTIVELY independent before the restructuring -- otherwise "several views improved" is
one view counted several times, which is the family's own core error. (P3) There must be a held-out
transfer set generated by the shared structure but not seen during the restructuring, or predictive
"gain" is unfalsifiable.

**CONFIRMING.** Ladder Stage 6 / aha section 9: over several superficially different tasks with one
hidden common structure, the correct-common-abstraction arm shows simultaneously reduced joint
complexity, preserved or improved held-out prediction, increased transfer to a novel member of the task
family, and reduced cross-view disagreement -- while the three control arms fail at least one: the
incorrect-but-highly-compressive arm fails held-out prediction, the one-domain arm fails cross-view
breadth, and the confidence/reward-manipulation-without-restructuring arm fails complexity and transfer.

**FALSIFYING.** (a) candidate insight metrics fail to distinguish genuine cross-model restructuring from
ordinary confidence, fluency or reward (hub falsifier 7); (b) apparent cross-view compression does not
predict held-out generalization or future problem solving (stress-test falsifier 5); (c) the cross-view
breadth criterion adds nothing over single-view restructuring plus model reduction, i.e. Friston et al.
2017's account already suffices.

**DISPOSITION: (c) substrate-blocked -- substrate_conditional, AND a live (f) defer candidate.** The
orchestrator should consider deferring this one. Reasons in order: the general form is externally
pre-empted; the nearest REE claim (MECH-423) already exists WITH evidence; impostor (1) is already
covered by INV-104 + MECH-126; the event has no substrate to fire over (P1 fails today); and no assay has
been run. The one thing that would be lost by deferring is the self-confirmation impostor, which can be
carried as a sentence in NEW-MECH-1's notes instead. A (g) MERGE proposal is also defensible: make it a
child of MECH-423 (survivor MECH-423, absorbed NEW-MECH-3, reverse-deps none since nothing depends on a
claim that does not yet exist).

---

## Part 2 -- `what_would_answer` drafts for EXISTING adjacent claims that lack one

Six candidate claims that this family materially bears on carry no `what_would_answer`. Drafts below are
proposals to `/governance`. **None is applied.** (ARC-142 also lacks one but this family bears on it too
weakly to draft responsibly -- the contract's own MECH-545 lesion-assay claim is the right source.)

### MECH-125 -- `coherence.multiconstraint_viability`

> NON-DEGENERACY PRECONDITION: at least two evaluation systems must be LIVE and capable of emitting a
> veto-level error signal in the measured window, and at least one candidate must actually receive one;
> a run in which no veto ever fires tests nothing, and a run in which only one system is live trivially
> satisfies "no major system vetoes". CONFIRMING: committed trajectories are those on which no
> evaluation system exceeds its veto threshold, and this predicts commitment better than the argmin of
> the aggregate score -- specifically, there exist committed actions that are NOT the aggregate-score
> winner because a higher-scoring candidate carried a veto, at a rate above chance. FALSIFYING: the
> committed action is the aggregate-score argmin on essentially every tick, i.e. "multi-constraint
> viability" is an alternative description of scalar maximisation with no separable veto structure --
> which is what MECH-439's 88-89% F variance monopoly currently predicts and is why this claim needs its
> own falsifier rather than inheriting one.

### ARC-128 -- `control_plane.termination_taxonomy_generality`

> NON-DEGENERACY PRECONDITION: at least two DIFFERENT families of persistent process must be
> instrumented, and each must actually terminate more than once in the measured window under at least
> two different terminal states. CONFIRMING: the same taxonomy (completion / satiety / closure /
> disengagement / suspension / switching / interruption / reopening) classifies terminations in two or
> more process families without family-specific additions, AND the recorded reason is consequential --
> a process terminated as `suspension` is reopened at a measurably higher rate than one terminated as
> `completion`. FALSIFYING: either the taxonomy requires family-specific terminal states (it is not
> general), or the recorded reason has no downstream effect on reopening, resource release or credit
> (it is bookkeeping, not architecture).

### MECH-434 -- `inference.epistemic_commitment_timing`

> NON-DEGENERACY PRECONDITION: the commitment threshold must be reachable in both directions within the
> measured range -- both epistemic-freezing and premature-commit poles must be producible by the
> available parameter sweep -- or the asserted inverted-U cannot be distinguished from a monotone.
> CONFIRMING: performance as a function of the urgency/threshold parameter is non-monotone with an
> interior optimum, and the two failure poles are behaviourally DISSOCIABLE (freezing shows sampling
> without commitment; panic shows commitment at measurably lower evidence), and the collapse of the
> epistemic term under threat is demonstrated rather than assumed. FALSIFYING: performance is monotone
> in the parameter (no inverted-U), or the two poles cannot be dissociated, or the axis reduces to
> MECH-126's uncertainty-collapse failure mode, which the claim explicitly denies.

### MECH-498 -- `control_plane.progress_gated_disengagement`

> NON-DEGENERACY PRECONDITION: RATE of progress and ABSOLUTE level of uncertainty/goal-distance must be
> DECORRELATED in the measured window -- the claim's whole content is that rate adds something level
> does not, so a regime where they covary tests nothing. CONFIRMING: disengagement gated jointly on
> marginal expected return and observed progress RATE outperforms a level-only gate specifically in the
> cell where absolute value remains high while marginal progress has collapsed; and it is dissociable
> from MECH-343's widening response, i.e. there exist cases where widening also fails and only
> disengagement recovers. FALSIFYING: a level-only gate matches it everywhere, or the rate term's
> apparent benefit disappears once the level term is correctly scaled.

### ARC-139 -- `architecture.mutual_legibility_without_representational_convergence`

> NON-DEGENERACY PRECONDITION: local competence must actually RISE over the measured developmental
> window in at least two subsystems -- a flat-competence window cannot test "specialisation and
> legibility rise together" -- and the cross-system similarity measure must have demonstrated range
> (an unrepresentative measure pinned near zero or one passes vacuously). CONFIRMING: over maturation,
> local competence in E1/E2/hippocampus/E3 rises while GLOBAL representational similarity between them
> stays flat or falls, AND mutual legibility measured as minimum bridge complexity (MECH-538) falls over
> the same window. Both halves are required: rising competence with falling similarity and no legibility
> measure is compatible with fragmentation. FALSIFYING: legibility improves only when representational
> similarity also rises, which would support ARC-121's shared-object reading instead; or competence and
> legibility trade off rather than rising together.

### MECH-126 -- `state_abstraction.failure_modes_psychiatric_analogs`

> NON-DEGENERACY PRECONDITION: each named failure mode must be independently INDUCIBLE in the substrate
> -- a taxonomy whose members cannot be produced separately is a vocabulary, not a set of mechanisms --
> and the behavioural signature must be measured on a substrate with demonstrated headroom to express
> the alternative. CONFIRMING: at least three of the six modes (overmerge, oversplit, temporal context
> loss, valence mis-tagging, uncertainty collapse, narrow representational capacity) are separately
> inducible and produce DISSOCIABLE behavioural signatures -- an intervention producing overmerge does
> not produce the oversplit signature and vice versa. FALSIFYING: the modes are not separately
> inducible, or their behavioural signatures are indistinguishable, collapsing the taxonomy to a single
> "abstraction is wrong" axis. (Relevance to this family: NEW-MECH-3's impostor (1) -- compression that
> deletes organism-relevant distinctions -- IS overmerge, and inherits whatever discriminability
> MECH-126 can establish.)

---

## Part 3 -- dispositions summary

| Item | Disposition | One-sentence justification |
|---|---|---|
| NEW-MECH-1 | (c) substrate_conditional; shadow-only variant may be (a) | No dependency-corrected quantity exists in `ree_core/` at all, but every input a shadow diagnostic would read already exists in V3. |
| NEW-MECH-2 | (c) substrate_conditional | The dependency half has partial V3 substrate (MECH-441, MECH-482) but nothing represents downstream consumers, so the leverage half cannot be measured. |
| NEW-INV-1 | (c) substrate_conditional + (f) defer on V3 | V3 has no agreement objective to prohibit; the invariant guards a future architecture and its falsifier is synthetic. |
| NEW-MECH-3 | (c) substrate_conditional, strong (f) defer candidate, (g) merge-into-MECH-423 defensible | Externally pre-empted, nearest REE claim already evidenced, and the revision mechanism it would detect events over is itself unbuilt (MECH-531). |
| Hub "convergence is a general computational signal" | (e) excrete -- survivor NEW-MECH-1 | The family's own stress test retracted the broad form; registering it would re-mint a retracted claim. |
| Aha = restructuring + model reduction | (c2)/(e) out-of-domain and pre-empted -- survivor: external literature | Friston et al. 2017 and Kounios & Beeman 2014 occupy it; REE should cite, not claim. |
| Diversity file sections 1,2,3,5,6,9,10,11 | (e) excrete -- survivors ARC-065, MECH-309, INV-074, INV-076, MECH-333/334, MECH-496, ARC-128, MECH-165, MECH-529, SD-091, ARC-139 | Re-derivation of owned claims with no new falsifier. |
| Diversity section 10 sleep hypothesis | (g) merge into **Q-055** | Q-055 already asks exactly this; the thought's "replay rare dissenting episodes" is `what_would_answer` material for it. |
| Formal notes: every named formula | instrument, not a claim | GOV-SHARPEN-1's over-splitting guard; six of them already exist as assay code. |
| `R_drop`, `delta K`, `S_t`, `C_pair` | (a) buildable now, synthetic | Four unimplemented measurements the family's own notes call for; `R_drop` is the highest value and the cheapest. |
| Assays 001-006 with empty `claim_ids` | `/governance` decision | Six passing preregistered runs attach to no claim; whether they may cite a newly registered id, and under what evidence class, is not an ingestion decision. |
