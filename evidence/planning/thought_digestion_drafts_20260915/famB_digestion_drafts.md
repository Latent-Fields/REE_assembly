# Digestion drafts -- Family B (developmental overcapacity / pruning / sparse interfaces)

Session: thought-pipeline-20260915. **Separate artifact -- NOT part of the intake, and nothing here is
applied to `claims.yaml`.** These are `/thought-digestion` drafts for the orchestrator to route.

Scope rule applied: the four proposed new claims, plus every EXISTING claim this thought materially
bears on that is `status: candidate` and carries **no `what_would_answer` field**. Checked and EXCLUDED
because they already carry one: Q-057, MECH-529, INV-104, INV-074, MECH-333, MECH-334, Q-101, ARC-019.
Checked and excluded as not materially borne on by this thought: MECH-537, INV-105, MECH-547, MECH-548,
ARC-139, MECH-513, ARC-137 (their own intakes deferred hardening deliberately, and this thought adds
nothing to their content).

Extraction discipline: falsifier language is taken from the thought's own sections 7, 8, 9, 11 and 12
where it exists, and from the sibling claims' registered wording where it does not.

---

## A. Proposed new claims

### NEW-ARC-1 -- developmental vs mature capacity envelope

**NON-DEGENERACY PRECONDITION.** At least ONE REE locus must support a declared capacity envelope that
can differ between a developmental phase and the mature phase, with both settings actually instantiable
and behaviourally exercised. Today zero loci do (verified 2026-09-15: no structural pruning, no
sparsification, no capacity schedule in `ree_core/`). Until then any test of this claim is vacuous --
the two envelopes cannot be set to different values, so "do not infer one from the other" has no
observable consequence.

**CONFIRMING.** For at least two structurally different loci (e.g. one representation-side, one
interface-side), a declared developmental envelope LARGER than the mature envelope yields a mature
system that is at least as competent as the same mature envelope trained throughout, at matched final
capacity and matched training compute -- i.e. the design freedom this claim asks for is not merely
permitted but is sometimes used to advantage. One locus is not enough: a single-locus result is a fact
about that locus, not a curriculum-design commitment.

**FALSIFYING.** Across the loci tested, the larger developmental envelope never produces a mature system
better than the mature-throughout baseline, and in at least one case produces a worse one (the thought's
own "irreversible early mistakes" rival: overcapacity increases spurious routes and makes pathological
attractors more likely). That would mean REE SHOULD infer the developmental envelope from the mature
one, which is the current implicit practice and would be vindicated rather than merely unexamined.

**DISPOSITION: (c) substrate-blocked -- `substrate_conditional`.** The code is absent, not
signal-absorbed, so this is the conditional and not the ceiling variant.
*Justification:* the mechanism has never been exercised at any locus because no capacity-schedule
substrate exists anywhere in `ree_core/`, which is the definition the repo's own CLAUDE.md gives for
`substrate_conditional`.

---

### NEW-MECH-1 -- developmental-history irreducibility at matched final capacity

**NON-DEGENERACY PRECONDITION (two independent legs, both currently UNMET).** (1) A capacity-reduction
mechanism must exist that can take an over-capacity locus to an exactly specified final architecture --
otherwise arm B has no defined endpoint and arm D has nothing to reinitialise. (2) Arm D must be
constructible: the sparsity mask / interface structure produced by arm B must be EXPORTABLE and
re-instantiable at initialisation. A design that can prune but cannot export what it pruned to can run
arms A/B/C and still not test this claim -- and A/B/C alone cannot separate it from architecture search,
which is precisely the failure the arm-D control exists to prevent.

**CONFIRMING.** With final capacity(B) = final capacity(D), architecture(B) ~= architecture(D), identical
curriculum, identical seeds and matched training compute: competence(B) > competence(D) by a margin
scaled on the seed-level SD of the B-D difference plus an absolute floor, AND the advantage persists
OUTSIDE the training distribution (held-out layouts, changed action semantics, delayed-consequence
distinctions, cue reassignment) -- the thought's prediction 2, included because a training-distribution-only
advantage is consistent with the memorisation rival.

**FALSIFYING (primary).** competence(B) ~= competence(D) at matched final capacity. The final
architecture reproduces the whole effect; developmental history contributed nothing beyond discovering
a good sparse architecture. The thought states this falsifier itself: "it can be disproved by showing
that matched mature architectures trained from birth perform just as well as systems that develop into
them."

**FALSIFYING (secondary, distinct signature -- do not read as confirmation).** B > A and B > D, but the
advantage disappears once training compute is matched, or is fully reproduced by a plain
teacher-student distillation from arm C at matched compute. Either would relocate the effect to
optimisation mechanics or to distillation, both of which are useful engineering and neither of which
establishes that organismal developmental history matters.

**FALSIFYING (tertiary, the boundary case the thought names).** Arm C strong while every reduced arm
collapses. That is not evidence about history at all; the correct reading is that the proposed mature
bottleneck is simply too narrow, and the claim is untested rather than refuted.

**DISPOSITION: (c) substrate-blocked -- `substrate_conditional`.**
*Justification:* the arm-D export path is not merely unbuilt but unspecified, and the claim is
uninterpretable without it, so this is a build dependency and not a research question about V3.

---

### NEW-MECH-2 -- functional persistence as the retention criterion

**NON-DEGENERACY PRECONDITION.** The magnitude-pruning control arm must be able to REACH the same final
capacity and remain non-collapsed, and the two criteria must actually select DIFFERENT retained sets
(report the overlap). If relevance-guided and magnitude pruning retain the same routes, the comparison
is vacuous regardless of the outcome -- the criterion was never manipulated. This is the same shape as
the V3-EXQ-610a-e cascade's repeated finding that a control which does not degrade makes the treatment
arm uninformative, and it is the most likely way a first attempt here fails.

**CONFIRMING.** At matched final capacity and matched update count, a retention criterion built from the
thought's list (predictive contribution, persistent-PE reduction, harm/benefit relevance, controllability
discrimination, counterfactual usefulness, action-selection contribution, replay recurrence, cross-context
transfer, cross-stage stability, multi-consumer utility, uncertainty maintenance) produces better
downstream competence AND better transfer than magnitude pruning, with a non-trivial retained-set
difference. Additionally diagnostic (the thought's Stage 5): the surviving routes correspond to stable
regulatory distinctions, task-relevant communication subspaces or repeated transformation motifs, rather
than to large parameter magnitude.

**FALSIFYING.** Magnitude pruning matches or beats the relevance-guided criterion at matched capacity and
matched updates. Then functional selection is not what the reduction is doing: the developmental benefit,
if any, is capacity annealing, and the elaborate criterion is decoration.

**FALSIFYING (second signature, INV-104-facing).** The relevance-guided criterion wins on aggregate
competence but selectively destroys distinctions from INV-104's protected preservation set whose
relevance had not yet been revealed. That is a FAILURE of this claim as stated (the criterion list
includes "maintenance of uncertainty where premature collapse would be dangerous" precisely to forbid
this outcome), not a partial success.

**DISPOSITION: (c) substrate-blocked -- `substrate_conditional`.**
*Justification:* nothing in `ree_core/` scores any connection, route or mapping for retention, so neither
arm of the comparison can be instantiated.

---

### NEW-MECH-3 -- replay-coupled capacity reduction as the coordination site

**NON-DEGENERACY PRECONDITION (three legs).** (1) A reduction mechanism must exist. (2) The
representation must actually be CHANGING during the reduction window -- if the representation is
frozen, the coordination hazard the claim is about does not arise and the comparison degenerates into
"does replay help pruning in general". (3) Update count must be matched between arms, not merely
wall-clock or episode count; an unmatched comparison measures extra gradient steps.

**CONFIRMING.** At equal reduction aggressiveness and matched update count, replay-coupled reduction
preserves more transfer and more causal structure (held-out layouts, counterfactual discrimination,
delayed-consequence distinctions) than online-only reduction. Strong form, and the one worth pre-registering
because it is harder to get by accident: replay permits GREATER compression at equal or better transfer.

**FALSIFYING.** Online-only reduction matches replay-coupled reduction at matched updates. Offline
reorganisation is not doing the coordination work; the reduction decision is reliable enough online, and
the coordination hazard is either absent or self-correcting.

**FALSIFYING (second signature, inherited from MECH-540's S4 and MECH-548's sleep corollary).** The
replay-coupled arm improves a static retention/reconstruction probe while the next waking trajectory is
measurably worse. That is a failure, not consolidation, and it must be measured rather than assumed away.

**DISPOSITION: (c) substrate-blocked -- `substrate_conditional`; ALTERNATIVELY (g) merge with MECH-540.**
*Justification:* substrate-blocked because there is nothing to reduce; flagged for a possible merge
because a capacity-reducing offline job could be MECH-540's fifth job rather than a separate claim --
if merged, MECH-540 is the survivor, NEW-MECH-3 is absorbed, and NEW-ARC-1 / NEW-MECH-2's reverse-deps
on it re-point to MECH-540. The decision needs MECH-540's own registration reasoning and is a governance
call, not a digestion one.

---

## B. Existing claims this thought materially bears on, candidate, with NO `what_would_answer`

### MECH-362 -- subtractive developmental sparsification (the parent claim)

Currency checked: its stated blocker ("a developmental pruning/sparsification substrate not yet built")
is STILL TRUE as of 2026-09-15 -- verified against `ree_core/` and against `substrate_queue.json` (182
entries, no matching `sd_id`). No run and no substrate entry has since appeared. Nothing to correct.

**NON-DEGENERACY PRECONDITION.** Both regimes must be instantiable: an over-connected / near-random
early substrate AND a sparse/structured mature one, with the trajectory between them actually traversed
by the system rather than configured at two fixed settings. A two-config A/B comparison tests the
ENDPOINTS, which ARC-006 already asserts; it does not test the TRAJECTORY, which is what MECH-362 claims.

**CONFIRMING.** A memory substrate that begins over-connected, dense and near-random and is reduced by
experience-dependent pruning / down-weighting reaches a sparse, structured organisation that an
additively-grown sparse substrate does not reach under the same curriculum; and the recall corollary
holds -- mature recall requires convergent summation of several weak inputs, with a single strong cue no
longer sufficient to release action (measured as the shift from single-cue release to multi-cue
convergence, which is the one strand with present-day V3 diagnostic relevance).

**FALSIFYING.** An additively-grown sparse substrate reaches the same mature organisation and the same
recall behaviour under the same curriculum -- the tabula-plena route is one path among several and not a
necessary one; OR the reduced substrate keeps single-strong-cue release throughout, which would falsify
the recall corollary specifically while leaving the connectivity trajectory untouched (these two legs can
fail independently and must be reported separately).

**DISPOSITION: (c) substrate-blocked -- `substrate_conditional`.** Unchanged from its registration.
*Justification:* three months after registration the substrate is still absent and no substrate-queue
entry has been opened for it; that is the situation `substrate_conditional` names, and the correct
response remains "wait for the upstream substrate", not "run something".

---

### MECH-538 -- minimum bridge complexity as the measure of mutual legibility

**CURRENCY FINDING -- the orchestrator should look at this, and a later session should fix it; DO NOT
fix it here.** MECH-538's notes (registered 2026-09-08) state that its orthogonal-Procrustes rung "is
independently owed elsewhere: V3-EXQ-1002's autopsy names an 'information-preserving rotation
corroborator' as an open obligation, and a flat result there WEAKENS the confirmed H-C leg." The
2026-09-11 governance note on the `zworld_actor_adequacy_locus` gate (claims.yaml lines ~32310 and
~84105) records that **BOTH** of the two parallel tests the 1002 autopsy owed have since been run:
"not a width bound (an optimal linear 32-dim compression of the same 250-dim input reaches 0.868
against a 0.80 bar) and **not a geometry bound (three information-preserving re-bases flat**; closed-form
linear-content witness degrades to ~0.59 against a ~0.57 trivial baseline) -- the encoding DISCARDS the
decision-relevant content." If those re-bases are the owed corroborator, MECH-538's "open obligation"
sentence is stale by three days, and -- per the 1002 autopsy's own pre-registered reading -- the flat
result WEAKENS the H-C leg rather than leaving it open. Governance should adjudicate whether the 1008
re-bases discharge the obligation; this pass only reports the collision.

**NON-DEGENERACY PRECONDITION.** The bridge ladder must be able to SEPARATE its rungs on the endpoints
being measured: if the native readout already clears the criterion, or if nothing up to the high-capacity
upper bound clears it, L is not measurable and the developmental trajectory cannot be tracked. The
V3-EXQ-1002/1008/1010 lineage at the observation -> z_world locus is currently in the second of those
states, which is informative about that locus and disqualifying as an instrument-validation site.

**CONFIRMING.** Across developmental checkpoints at a locus where L is measurable, minimum bridge rank
FALLS while both endpoints' local competence RISES and global representational similarity stays flat or
falls -- coordination without homogenisation, on both axes simultaneously.

**FALSIFYING.** L stays flat or rises while competence rises (the "overcapacity crutch" outcome the
thought names in section 4); OR L falls together with rising cross-system similarity and falling local
specialisation, which is the degenerate homogenisation case the two-axis requirement exists to catch and
which must be reported as a failure rather than as the prediction confirmed on one axis.

**DISPOSITION: (f) defer, with reason.** Its own registration sequences the developmental sweep after
ML-20 has shown range and stability at one waking locus; running it earlier measures the instrument.
*Justification:* the sequencing is part of the claim, and the only locus with a bridge ladder attempted
so far is one where no rung clears the bar.

---

### MECH-540 -- sleep as selective interface maintenance

**NON-DEGENERACY PRECONDITION.** At least TWO interfaces with DIFFERENT predicted plasticity must be
measurable pre- and post-sleep, and at least one must be predicted stable. The claim's own content is a
plasticity/stability DIVISION OF LABOUR, so a single-interface measurement cannot confirm it however it
comes out.

**CONFIRMING.** S2 or S3 at the predicted-plastic interface (communication subspace or bridge complexity
improves with local competence stable; or representations move while the mapping holds) WITH the
predicted-stable interface not moving in the same direction over the same sleep episode.

**FALSIFYING.** S4 -- cross-system similarity rises while local competence or task-specific
differentiation falls (maladaptive homogenisation); OR all measured interfaces move together, which is
global alignment and is exactly what the claim predicts against; OR S1 alone at every interface (metrics
move only because the senders moved), which means sleep is doing representation work and no interface
work.

**Proposed but not applied (carried from MECH-548's registration, restated here because this thought
bears on it):** a fifth signature S5 -- a static probe improves while the next waking trajectory
destabilises -- and, from this thought, a possible SIXTH offline job (capacity reduction, NEW-MECH-3).
Both are governance decisions.

**DISPOSITION: (f) defer, with reason.** Same sequencing gate as MECH-538 and for the same reason; its
own notes name the cheapness of `force_sleep_cycle_at_eval_boundary` as the trap.

---

### INV-056 -- selective neoteny / substrate-specific developmental hardening

The thought's section 10 ("graceful freezing": most structure stabilises while limited plasticity remains
for genuinely novel environments) is a restatement of this claim, so it is worth hardening while the
wording is in front of us.

**NON-DEGENERACY PRECONDITION.** Hardening rates must be SETTABLE PER SUBSTRATE, and at least one
substrate must be set to harden while another is set to retain plasticity in the same run. A uniform
hardening schedule cannot test a claim whose content is the non-uniformity. `DEV-NEED-025`'s own open
question records that the representation of hardening rates in substrate configs does not exist
("Claimed as design principle; implementation contract absent"), so this precondition is UNMET today.

**CONFIRMING.** After a late-stage environmental or ethical-context change, an agent whose procedural /
motor substrates hardened but whose social-cognition, goal-representation and epistemic-ethical
substrates retained elevated plasticity updates the latter measurably (new goal structure, revised
other-model, revised valuation) while the former stay stable -- and outperforms both a uniformly-hardened
and a uniformly-plastic control.

**FALSIFYING.** The uniformly-hardened control matches it (selectivity buys nothing), OR the
uniformly-plastic control matches it (hardening buys nothing and the cost is only stability that was
never needed), OR the selectively-plastic agent's retained plasticity destabilises the hardened
substrates through shared parameters -- which would mean the selectivity is not architecturally
realisable as stated.

**DISPOSITION: (c) substrate-blocked -- `substrate_conditional`, and its `implementation_phase` should
be checked.** *Justification:* no per-substrate hardening-rate representation exists, so the
non-uniformity cannot be configured; the right response is the implementation contract `DEV-NEED-025`
names, not an experiment.

---

## C. Nothing here is an excretion or a merge, with one exception

No (e) excrete verdicts: none of the four proposed claims duplicates an existing one, and the three
threads that DID duplicate existing claims (the tabula-plena trajectory, the falling-L developmental
prediction, prediction 7) were caught in the novelty table and never drafted. The one merge candidate is
NEW-MECH-3 -> MECH-540, recorded above with the survivor, the absorbed entry and the reverse-deps named.
