# Thought-digestion staged review -- session thought-pipeline-20260915

WHAT THIS IS: the /thought-digestion skill's unattended-mode staging file. Drafted
`what_would_answer` falsification conditions and recommended dispositions for the claims
registered (or materially touched) by the 2026-09-15 ingestion of the 17-thought backlog.
NOTHING here has been written to claims.yaml. Per the skill, the falsification condition
and disposition are the user's call; review each entry, then a session applies the
approved ones (re-reading each block fresh) and checkpoint-commits.

HOW TO USE: read section 0 (governance flags) first. Then per claim: accept / edit / defer.
Dispositions: (a) testable now on V3, (b) derivational, (c) substrate-blocked
[substrate_conditional | substrate_ceiling], (c2) out-of-domain, (e) excrete, (f) defer
with digestion_note, (g) merge proposal -> governance_flag.py.

## 0. Governance flags / currency findings surfaced during research

Raised via governance_flag.py on 2026-09-15 (all pushed; /governance reads them):
- GFLAG-0280 MECH-540 contested_disposition -- amendment proposal: add 'replay maintains the causal ACCESS
  correspondence' as a MECH-540 signature (same shape as MECH-548 S5 and MECH-551); the drafted claim was
  deliberately NOT registered.
- GFLAG-0281 GOV-CONTRACT-1 / ARC-142 stale_note -- 'ledger NOT BUILT' is stale (14 records since
  2026-09-08); the tranche-3 ledger amendment (7 edits) was never applied and this ingestion is its trigger.
- GFLAG-0282 MECH-537 / MECH-538 stale_note -- both notes overtaken by V3-EXQ-1010 H-F confirmed;
  SD-080 unblocks_claims omits MECH-537.
- GFLAG-0283 MECH-441 stale_note -- what_would_answer HOLD self-contradicting (V3-EXQ-707 negative;
  REWRITE OWED).
- GFLAG-0284 MECH-275 / MECH-554 evidence_discrepancy -- claim says aggregate across EPISODES; code
  aggregates per replay DRAW with replacement and no dependency term.
- GFLAG-0285 MECH-094 / MECH-227 stale_note -- call-site count stale (87 vs ~30); MECH-227 still lacks
  epistemic_category / implementation_phase.
- GFLAG-0286 (expected id) SD-106 / SD-018 contested_disposition -- the exq1010 sample-saturation
  objection (row-sampled sub-split; all half-to-full deltas positive) was never adjudicated at the Step 8
  gate; _best_over_rungs does not exclude diverged rows and SD-106's acceptance target is a 1010 re-run.

Not flagged (planning docs, not claims) but recorded in WORKSPACE_STATE: hippocampal assay spec section
0.2 'instrument does not exist' is stale (interface_probe.py landed 2026-09-10 21:15Z); replay_sampler.py
docstring 'Phase B is a NO-OP CONSUMER' is stale; docs/CURRENT_FRONT.md still says 1010 is running;
hypothesis_space decision block reads H-F ALIVE while the leg is confirmed; hippocampal_systems.md has no
heading for ARC-007.

Registry deltas this session: 1126 -> 1152 claims (+26). Validator: 0 errors; warnings 18 -> 21 (the
three new open_question entries Q-105, Q-106, Q-107 lack what_would_answer -- supplied by the drafts
below once approved). Stance tally shown=90 unchanged (digestion is not promotion).


## Family B -- developmental overcapacity, pruning, sparse interfaces (registered ARC-143, MECH-549, MECH-550, MECH-551)

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

### ARC-143 -- developmental vs mature capacity envelope

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

### MECH-549 -- developmental-history irreducibility at matched final capacity

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

### MECH-550 -- functional persistence as the retention criterion

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

### MECH-551 -- replay-coupled capacity reduction as the coordination site

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
if merged, MECH-540 is the survivor, MECH-551 is absorbed, and ARC-143 / MECH-550's reverse-deps
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
destabilises -- and, from this thought, a possible SIXTH offline job (capacity reduction, MECH-551).
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
MECH-551 -> MECH-540, recorded above with the survivor, the absorbed entry and the reverse-deps named.

## Family E -- provenance errors, false evidence multiplication (registered INV-107, MECH-552, MECH-553, MECH-554, Q-105)

# Digestion drafts -- Family E (provenance / false evidence multiplication)

**Date:** 2026-09-15
**Session:** thought-pipeline-20260915
**Scope:** the five proposed claims in `proposed_claims.yaml`, plus the existing `candidate` claims
this thought materially bears on that carry NO `what_would_answer` field.
**Status:** drafts only. Nothing is applied to `claims.yaml`. Disposition recommendations are
recommendations.

Method note: falsifier language is EXTRACTED wherever possible -- from the raw thought's section 11,
from the ladder's stop conditions, from the campaign supplement's section 11 falsifier list, and
from the four executed probe results -- rather than invented. Where a probe has already fired a
falsifier or changed its meaning, that is recorded under CURRENCY.

---

## A. Proposed new claims

### INV-107 -- dependency must be represented; independence must not be inferred

**NON-DEGENERACY PRECONDITION.** Two things must both be live before any test reads on this. (1) The
architecture must actually generate more than one evidence-bearing descendant of a single item in
the run -- an architecture in which each belief update sees exactly one input cannot violate or
satisfy the invariant, and a descendant count of one is a vacuity signal, not a pass. (2) The
confidence or commit-readiness readout being audited must have non-zero cross-arm variance; a
readout pinned at a floor cannot show a dependency-driven shift.

**CONFIRMING.** An audit-shaped, not performance-shaped, test, in the ARC-115 / INV-077 style: every
path by which an item can enter a belief, confidence, closure or action computation either carries a
readable dependency record for that item, or explicitly refuses to treat it as independent. The
architecture nowhere has a branch whose behaviour on "no dependency recorded" equals its behaviour
on "dependency recorded as absent".

**FALSIFYING.** Either direction falsifies, and both must be scored:
(i) a live path is found where an item with no recorded dependency is weighted as independent, with
no refusal and no uncertainty carried -- the under-representation failure;
(ii) the architecture applies a FIXED discount to any item merely because a dependency is recorded,
without conditioning on the observations across that dependency -- the over-discounting failure the
Pilditch 2020 counterweight identifies, which the raw thought's wording would have licensed.
Also falsifying: ordinary covariance or dependency estimation over content, with no genealogy
representation at all, is shown to satisfy (i) and (ii) equally well (this is the ladder's own P6
stop condition and retires the invariant's representational requirement rather than the invariant).

**DISPOSITION: (c) substrate-blocked [substrate_conditional].** No dependency representation exists
in `ree_core` to audit -- a tree-wide grep for ancestry/lineage/ancestor/genealogy returns only
comments about experiment lineages -- so the audit has nothing to trace and would report
`definition_not_ready` rather than a verdict.

---

### MECH-552 -- false evidence multiplication

**NON-DEGENERACY PRECONDITION.** Extracted from the ladder's P1 critical criterion and the
supplement's P1-R1/R4. All four must hold: (1) informational content and the external evidence set
are IDENTICAL across provenance conditions -- a hard assertion, not a design intention; (2) the
descendants are GENERATED by the architecture's own processes and the ancestry record is corrupted
INSIDE it, not handed to a reader as a fixed evidence graph (a stipulated-graph version reproduces
published human work and adds nothing); (3) a genuinely-independent-new-observation arm raises both
count and confidence with calibration preserved, so the count readout is shown to have dynamic range
in the correct direction; (4) the effective-source-count instrument reports its own calibration --
it is known to drift away from its endpoints, so it must not be read as ground truth, and confidence
must be measured separately rather than derived from the count.

**CONFIRMING.** With content and world evidence fixed, the corrupted / absent-ancestry condition
raises the effective independent-source count AND degrades calibration against world truth AND
reduces further information-seeking, while a matched legitimate-computation arm (further computation
on a fixed observation set that demonstrably improves the estimate) shows calibration IMPROVING with
the effective source count UNCHANGED. The separation of those two signatures is the confirmation;
either alone is not.

**FALSIFYING.** Extracted from the thought's section 11 and the supplement's section 11:
content-matched provenance corruption changes source attribution and association strength but leaves
effective source count and calibration intact (the H0 source-label-only outcome, and still the most
likely single result); OR the inflation appears only when ancestry is PRESENTED as split and never
when a genealogy representation is corrupted internally; OR contradictory external evidence is
handled normally despite corruption; OR the effect requires an explicit hand-coded
provenance-error-to-confidence bonus rather than emerging from the inference rule; OR the
legitimate-computation control cannot be distinguished from the false-independence signature under
the chosen instruments, in which case the hypothesis is untestable as posed and the instruments must
be rebuilt before any result is reported.

**CURRENCY -- this claim's headline has already moved.** `evidence/planning/provenance_p1_result.md`
(2026-09-10, synthetic, three seed-pairs) reports every preregistered criterion passing, and then
locates the effect in the READOUT DEFAULT rather than in the corruption: `absent_policy=independent`
gave N_eff 1.117 -> 4.869, `soft` gave 1.117 -> 5.000, `dependent` gave 1.117 -> 1.000, at identical
corruption. `evidence/planning/provenance_p1r5_retrieval_attribution_result.md` then found the
`dependent` fix ALSO fails its absent-policy crossing criterion on both routes. The claim as drafted
carries that correction; a version that asserts corruption as the cause would be registering a
position its own branch has already refined. These are synthetic-harness results and are NOT claim
evidence.

**DISPOSITION: (c) substrate-blocked [substrate_conditional].** The VERIDICAL comparator arm cannot
be built -- there is no genealogy in `ree_core` to leave intact -- and the architecture sits
permanently in the ABSENT condition, with the one ancestry reference that does exist deleted at
commit (`ree_core/hippocampal/module.py:3450-3453`).

---

### MECH-553 -- compressed causal genealogy

**NON-DEGENERACY PRECONDITION.** The comparison must be at MATCHED INFORMATION, and the genealogy
must be exercised: at least one pair of items in the run must genuinely share an ancestor and at
least one pair must genuinely not, with both cases reaching a belief update. A run in which every
item is independent, or every item shares one ancestor, tests nothing. The bounded structure must
also be genuinely bounded -- if the implementation stores full history, it is a different and weaker
claim and must be reported as such rather than scored against this one.

**CONFIRMING.** Explicit compressed genealogy beats both lineage-free inference and no genealogy on
calibration and duplicate-evidence resistance at matched information, AND the already-counted-family
marker demonstrably prevents a re-presented item from contributing twice to the same belief update,
AND edge confidence is load-bearing (an uncertain edge produces an intermediate weighting rather
than collapsing to present-or-absent).

**FALSIFYING.** Lineage-free dependency estimation -- from residual or error covariance, shared
latent provenance, temporal co-reactivation, common prediction ancestry, ablation/dropout response,
or a context-conditioned dependency estimate -- matches explicit genealogy on calibration and
duplicate resistance at matched information. Rule & O'Leary 2022 (PMID 35145024) is the named
concrete competitor. Also falsifying: the per-token source vector of MECH-430 alone, with no
relational edges, is sufficient -- in which case this claim earns no keep over MECH-430.

**DISPOSITION: (c) substrate-blocked [substrate_conditional], and (g) merge is a live option.** If
the orchestrator wants a smaller set, this is the claim to fold into MECH-552 as its substrate
half; it survives separately only because MECH-430's own falsifier would pass unchanged in an
architecture that counted one lineage four times, so the representational requirement is not tested
by anything currently registered.

---

### MECH-554 -- recursive replay amplification

**NON-DEGENERACY PRECONDITION.** Four, all extracted from the supplement's P3-R1/R2/R3. (1) External
evidence must be genuinely fixed after the replay phase begins, asserted rather than assumed.
(2) Replay must be stratified by kind -- single-episode content rehearsal, cross-episode relational
linking, prediction-generated descendants -- because a replay-count main effect pooled across kinds
is not a result. (3) Retrieval quality must be matched across ancestry conditions, or the
ancestry-by-count interaction is a retrieval effect wearing a provenance label. (4) The healthy-replay
arm must be ABLE TO PASS: an arm in which replay improves retrieval fidelity while the effective
source count stays flat must be reachable. If every replay arm inflates the count, the instrument is
measuring replay exposure, not genealogy, and the run reports instrument failure rather than a
result.

**CONFIRMING.** A significant ancestry-by-replay-count INTERACTION at fixed external evidence and
matched retrieval quality: confidence rises monotonically with replay count in the corrupted /
absent-ancestry conditions and does not in the veridical condition, with the healthy-replay arm
simultaneously showing fidelity improvement at flat source count.

**FALSIFYING.** No ancestry-by-replay-count interaction survives matched retrieval quality (the
supplement's own restatement of the thought's section 12 falsifier); OR replay improves
representation without any change in the independence estimate under every ancestry condition; OR
the interaction appears only under an explicitly programmed confidence bonus.

**CURRENCY.** `evidence/planning/provenance_p3_r2_spike_result.md` (2026-09-10) reports the
healthy-replay arm was UNREACHABLE as the harness was built (fidelity rise exactly 0.000000000) and
became reachable only after a harness capability was added. In the work-graph debt vocabulary the
spike routes the rung from `complex (probe-gated)` through `puzzle (known rules)` to
`complicated (buildable)`. The confirmatory grid has not been run; seeds were pilot and discarded.

**DISPOSITION: (c) substrate-blocked [substrate_conditional] in REE, with a named and deliberately
unqueued V3 observation point.** `ree_core/sleep/bayesian_aggregator.py` adds likelihood precision
per routed replay event with no dependency term, and `ree_core/sleep/replay_sampler.py` draws with
replacement while already tracking `draw_region_counts` -- so precision against per-region draw count
at fixed waking evidence is instrumentable today with no code change. It is NOT a test: a positive
relation is the code's own arithmetic, and the veridical comparator arm does not exist. Separately
the waking replay path is discarded entirely (`ree_core/agent.py:10594`), gated behind
`substrate_queue.json` entry `mech092-replay-consumer-missing`.

---

### Q-105 -- source attribution versus evidence cardinality

**NON-DEGENERACY PRECONDITION.** Both readouts must be independently instrumented and both must move
somewhere in the design -- a source readout pinned at chance, or a cardinality readout with no
dynamic range, makes a null uninterpretable. The four readouts (association strength, source
attribution, effective independent-source count, calibration against world truth) must be reported
separately, with none derived from another, because the count instrument is itself miscalibrated
away from its endpoints.

**ANSWERED-BY (this is an open_question, so CONFIRMING/FALSIFYING is stated as resolution).**
Resolved AFFIRMATIVE by a 2x2 in which provenance and self-generation prediction are manipulated
separately and at least one cell moves source attribution without moving the count, and at least one
cell moves the count and calibration without moving source attribution. Resolved NEGATIVE by the two
readouts covarying across every cell at matched instrument sensitivity -- which would mean the
architecture has one underlying provenance variable with two faces, and would collapse MECH-552's
epistemic branch back into the source-monitoring account.

**DISPOSITION: (c) substrate-blocked [substrate_conditional].** The epistemic readout
(P(H | evidence graph)) has no referent in `ree_core`: there is no evidence graph. Partial synthetic
evidence exists (`provenance_p1r5_retrieval_attribution_result.md` criteria A9a FAIL / A9b PASS) and
is recorded on the claim so the question is not treated as untouched, but it is not claim evidence.

---

## B. Existing candidate claims with NO `what_would_answer`, that this thought materially bears on

Drafts for a later `/governance` or `/claim-synthesis` pass. **Not applied here.**

### MECH-244 -- psychosis as precision-weighting failure (`candidate`, no `what_would_answer`, no `falsifier` field)

This is the claim the thought's clinical half would have to be a fourth pathway of, and it currently
has no structured decision rule at all -- only an `evidence_quality_note` recording two
`non_contributory` runs (V3-EXQ-826, V3-EXQ-826a).

**NON-DEGENERACY PRECONDITION (draft).** The two readiness gates the 826a note already names must
both clear before any arm is interpretable: phase-A convergence ratio at or above its 0.25 floor
(measured 0.152), and regime-change disconfirmation at or above 1.15 (measured 0.966). The note
records `pe_precision_manipulation_took` as passing at 2.06 against a 1.5 floor, so E1 does train;
the outstanding gates are convergence and disconfirmation, not gradient flow.

**CONFIRMING (draft).** Downweighting sensory prediction-error precision relative to prior precision
produces beliefs that persist against incoming percepts, with a dose-response on the precision ratio,
and the persistence is NOT reproduced by the two registered alternative pathways at matched input
(MECH-246 signal degradation, MECH-247 pathological priors).

**FALSIFYING (draft).** Belief persistence tracks input noise or prior structure rather than the
precision ratio; or the self-sealing signature appears at every precision setting, including the
intact one, which would make the precision ratio non-load-bearing.

**DISPOSITION: (c) substrate-blocked [substrate_conditional] on its own readiness gates, and
separately (c2) out-of-domain for its clinical content.** The thought bears on it only by NOT being
registered as a fourth pathway; no field changes.

### MECH-248 -- source monitoring as the biological implementation of MECH-094 (`candidate`, no `what_would_answer`)

**NON-DEGENERACY PRECONDITION (draft).** A source-monitoring readout distinct from the write gate
must exist -- i.e. the architecture must be able to report P(external | representation) separately
from whether the item was allowed to write. In the current tree it cannot: `hypothesis_tag` is the
same bit for both.

**CONFIRMING (draft).** A distinct attribution stage, operating at retrieval rather than at encoding,
reproduces the functional separation MECH-094 asserts, and its ablation degrades attribution while
leaving the encoding-side mode-setting (MECH-249) intact.

**FALSIFYING (draft).** Encoding-side neuromodulatory mode-setting alone reproduces the whole of
MECH-094's functional separation, with no retrieval-side attribution stage needed -- in which case
MECH-248 earns no keep over MECH-249.

**DISPOSITION: (c) substrate-blocked [substrate_conditional].** Bears on Q-105 directly: the
source readout Q-105 needs is MECH-248's readout, and neither exists.

### MECH-430 -- multi-dimensional provenance source vector (`candidate`, falsifier in `notes` prose, no structured field)

Its prose falsifier ("if a single committed_vs_imagined bit is sufficient to prevent all
safety-relevant confabulation ... MECH-430 earns no keep over MECH-365") is sound for what it tests
and is **silent about cardinality**: an architecture that passes it can still count one lineage four
times, because every dimension it lists is a per-token attribute.

**RECOMMENDED ADDITION (not applied).** Promote the prose falsifier to a structured
`what_would_answer` and add an explicit scope line saying the claim covers per-token source
attributes only, with relational ancestry routed to MECH-553. That is a `/governance` edit, not an
intake edit.

**DISPOSITION: (c) substrate-blocked [substrate_conditional] (unchanged), plus a
documentation-currency item.**

### MECH-363 -- diffuse long-range competitive coupling (`candidate`, no `what_would_answer`)

Named here only to record the distinction, since "runaway resonance" and "self-confirming evidence
loop" read alike. MECH-363's own notes already distinguish two non-equivalent failure axes (runaway
positive coupling versus monostrategy collapse); MECH-554 is a THIRD axis that neither covers --
an evidence-count failure with correctly damped fields.

**DISPOSITION: (f) defer.** No change proposed; the `depends_on` edge from MECH-554 carries the
distinction.

### MECH-544 and MECH-548 -- source-tag decay; semantic double-counting (`candidate`, falsifiers in `notes` prose)

Both registered 2026-09-08, both carry prose falsifiers, both are cross-referenced by the proposed
entries. MECH-544 supplies the degradation PROCESS that MECH-552's corruption arm instantiates;
MECH-548's mechanism (b) is the same failure family at one translation interface.

**DISPOSITION: (f) defer -- too recently registered to digest, and neither is stale.** Cross-ref
only.

---

## C. Things this pass deliberately did NOT draft a falsifier for

| Item | Why |
|---|---|
| A clinical provenance-error psychosis pathway | (c2) out-of-domain. The thought forbids it; the branch's own supplement argues the framing has the wrong shape because the cardinality error is a healthy-human default under ambiguity. If ever registered, the INV-106 shape (`derived_prediction` + `prediction_domain: clinical_psychiatry` + `epistemic_category: out_of_domain`) is correct, and the content should be the narrowed question (is the discrimination capacity deployed?), not a lesion account. |
| "Soft provenance is safer than categorical provenance" | (e) excrete -- the surviving position is INV-107's representation requirement. The branch's own P1 run measured `soft` degenerating to `independent` exactly in the regime where it was meant to help. |
| The P1-P6 assay rungs | (f) defer -- assay designs, already owned by the ladder and its six companions. Registering them would create a second, staler tracker. |
| "Epistemic reproductive number" as a claim | (e) excrete into INV-107's notes -- an engineering restatement of the same rule, with no independent falsifier. |
| Circular-inference equivalence | (f) defer, with a literature debt. The thought itself says it "should not be declared equivalent without a dedicated literature comparison", and that comparison has not been done anywhere in the branch. |

## Family F -- shared reference frames and temporal gates (registered MECH-555, MECH-556)

# Digestion drafts -- FAMILY F

**Source thought:** `docs/thoughts/2026-09-09_shared_reference_frames_and_temporal_gates.md`
**Date:** 2026-09-15 -- **NOT part of the intake.** These are `/thought-digestion` drafts
(`what_would_answer` candidates + disposition recommendations), offered for a later hardening pass.
Nothing here was written into `claims.yaml`.

Method note: falsifier language is EXTRACTED from the thought (sections 7, 8, 11) and from the
already-written assay specification
(`evidence/planning/hippocampal_campaign_assay_specifications_20260910.md`) wherever it exists, rather
than invented. Where an existing sibling's wording covers a condition, it is reused verbatim.

**Currency check performed (2026-09-15):** V3-EXQ-1010 has RUN and RESOLVED -- manifest
`v3_exq_1010_zworld_overcapacity_decoder_sweep_20260909T195348Z_v3.json`, outcome PASS,
`hypothesis_verdict: H-F-confirmed`, "the decision-relevant content is DESTROYED AT ENCODE TIME: no
decoder in the capacity ladder recovers the oracle above the bar from the frozen latent ... The repair
is at the ENCODER'S OBJECTIVE, not at the consumer", with the `rawfield_ceiling` positive control at
0.9735 worst-seed. It is `evidence_direction: non_contributory`, `claim_ids: []`, and already in
`review_tracker.json`. **This bounds the whole family and every draft below is written against it.**
`docs/CURRENT_FRONT.md` (generated 2026-09-14 from a 2026-09-08 insights report) still describes 1010
as "queued and running" -- a generated-doc staleness, not a claim error.

---

## D1. MECH-555 -- reference-frame mediation

**NON-DEGENERACY PRECONDITION (this is the gate; check it before anything else).** Three conditions,
all failing today:

1. **An adequate source.** V3-EXQ-1010 CONFIRMED H-F at `observation -> z_world`: the decision-relevant
   content is destroyed at encode, so at THAT locus there is nothing mis-framed to detect and a frame
   permutation would measure noise. A frame assay is only interpretable at an interface whose source
   passes an adequacy check first -- `rawfield25` (0.9735 worst-seed) or a post-SD-106 encoder, not
   the shipped P0 latent. Running RF-1..RF-4 on an inadequate source cannot distinguish RF-F from F1
   (target absent from sender) and would produce a false RF-F-eliminated.
2. **At least two candidate frames that are distinguishable in V3.** Zero matches in `ree_core/` for
   `egocentric`, `allocentric`, `reference_frame`, `ref_frame`, `frame_id`, so the frames must be
   supplied by the experiment layer. The assay spec already does this (five frame levels, assay A
   section 2.2) -- but note level (ii), the invertible 90/180/270 rotation, is a CONSTRUCTED frame,
   not one REE learned, so it tests the instrument's sensitivity, not whether REE spontaneously
   preserves a shared index.
3. **The G4 instrument gate.** "Known invertible frame transform with its exact inverse. If this does
   not restore the consumer, the instrument cannot detect any transformation effect and the run is
   refused." Reused verbatim from the assay spec.

**CONFIRMING.** On a source that passed adequacy, at frozen endpoints and matched capacity, data,
optimisation and conditioning-channel width: held-out consumer use under the intact frame is
**substantially greater** than under a within-stratum frame permutation, **while the task target
remains decodable at the same level in both** (the permutation preserved content and marginal
difficulty), AND `A3_frame_cond` clears `A1_source_only` on the compositional holdout cells (frame
level x query level unseen in fitting). A frame permutation that disrupts **only one** downstream
consumer confirms the weaker, consumer-specific reading and MUST be reported as such rather than as
a shared global frame.

**FALSIFYING.** Any of: (a) intact ~= frame-permuted at matched decodability -- the frame is
incidental at this interface; (b) `A3_frame_cond ~= A1_source_only` on the holdout cells, i.e.
conditioning on the frame label buys nothing over an unconditional low-rank bridge; (c) the frame
effect disappears once marginal difficulty is equalised, i.e. the permutation was off-distribution
rather than frame-destroying (assay spec guard 6); (d) frame alignment does NOT lower the minimum
bridge rung `L(A -> B)` in any tested pair -- this falsifies the claim's second non-redundant
prediction specifically while leaving the first open, and should motivate a narrower successor rather
than a flat fail.

**Recommended disposition: (f) DEFER, with reason** -- and the reason is sequencing, not doubt.
Everything the claim needs exists except an adequate source at a named locus, and 1010 just
established that the primary locus does not have one. The claim should sit `candidate` until either
SD-106 validates or the assay runs on `rawfield25`. Secondary disposition if governance disagrees on
2.1: **(g) MERGE into ARC-142**, naming MECH-555 absorbed, RF-F and the frame-permutation control
lifted into ARC-142's notes, reverse-deps = none (nothing yet depends on it).

---

## D2. MECH-556 -- temporal-gate adequacy

**NON-DEGENERACY PRECONDITION.** The manipulated phase must be one the receiver's plasticity or read
actually tracks, and the comparison must hold quantity fixed. Extracted from the thought
("preserve total communication energy/updates so that timing, not quantity, is the manipulated
variable") and from Gate B2 verbatim: "Match event count, phase occupancy, activity magnitude and
total absolute weight change. Do **not** interpret a timing interaction if the shifted condition
changes data exposure or update magnitude." Additional precondition specific to REE: the interface
under test must have a receiver whose state can change as a result of the read at all -- note
`mech092-replay-consumer-missing` (substrate_queue, `proposed_REGISTRATION_ONLY`): `_do_replay`
computes replay trajectories and discards them, so the replay -> consumer interface has **no
consumer**, and a timing manipulation there is unfalsifiable by construction.

**CONFIRMING.** Correctly paired content delivered at the target phase produces a downstream change
(receiver parameter/state change, consumer-use gain, or post-sleep retention) that early-shifted,
late-shifted and phase-shuffled delivery do not, at matched event count, phase occupancy, activity
magnitude and total absolute weight change -- and the effect survives the pairing controls that
already bind (correct vs mismatched vs zero vs moment-matched random, INV-105). Per MECH-540's
two-interface requirement, the timing effect must be measured on **at least two interfaces with
different predicted plasticity**; a timing effect identical on both is generic plasticity scheduling,
not interface-specific gating.

**FALSIFYING.** Any of: (a) target-phase ~= shifted at matched energy -- timing is not a factor at
this interface, and TG-F may not be invoked to excuse its nulls; (b) the apparent timing effect
tracks total update magnitude or exposure rather than phase (the Gate B2 disqualifier); (c) the
effect appears at every phase offset, i.e. what varied was not phase; (d) **the strong falsifier for
the claim's evidential rule specifically:** a systematic re-measurement of interface nulls under a
phase-controlled protocol recovers none of them -- the phase control adds cost and changes no verdict,
which would make TG-F a distinction without a difference and argue for retiring it to a
documentation note rather than a claim.

**Recommended disposition: (a) TESTABLE NOW ON V3 SUBSTRATE, with one caveat** -- the levers are
built (MECH-089 `ThetaBuffer`, MECH-272 `routing_gate.py`, MECH-091 `phase_reset`, `MultiRateClock`,
`force_sleep_cycle_at_eval_boundary`), the instrument is built (`interface_probe.py`, whose
`CaptureRecord` already carries `phase`), and the manipulation is specified (Gate B2). The caveat is
that Gate B2 is explicitly staged "only after content specificity is established" at Gate B1, so this
is testable-but-sequenced, not testable-now-in-practice. Governance should consider routing
MECH-556 `implementation_phase: v3` on this basis -- the same reasoning that put MECH-537 and
INV-105 at v3 while their siblings defaulted to v4.

---

## D3. MECH-537 (candidate, substrate_conditional, no `what_would_answer`)

The thought materially bears on this claim: it argues the communication subspace is under-specified
without saying what its directions are indexed against, and that a fixed-subspace estimate can
under-read an interface that is healthy but differently framed (MECH-547 already makes the parallel
point for receiver state).

**NON-DEGENERACY PRECONDITION.** A source that passes adequacy (see D1.1 -- 1010's H-F-confirmed
verdict means the primary locus does not), and a `receiver_input` tensor that is the signal the LIVE
consumer actually reads, not a neighbouring tensor (the assay doc's own "critical rule", which
`interface_probe.CaptureRecord` explicitly cannot enforce).

**CONFIRMING.** `target decodable from X` AND `poorly decodable from P_comm X` on held-out data, with
the orthogonal complement carrying the decodability, cross-validated RRR rank selected on a held-out
block, and the consumer demonstrably insensitive to the complement.

**FALSIFYING.** The target is as decodable inside the estimated communication subspace as in the full
sender (no routing failure -- route to F3, consumer insensitivity, or F1), OR the subspace estimate is
unstable across frame or receiver-state strata, in which case the single-subspace premise fails and
the question belongs to MECH-547 / MECH-555 rather than here.

**Recommended disposition: (a) testable now**, unchanged from the parent intake's routing -- the RRR
estimator exists in `interface_probe.communication_subspace`. This draft adds only the stratification
caveat.

---

## D4. MECH-539 (candidate, substrate_conditional, no `what_would_answer`)

Bearing: the thought's section 10.3 asks the dynamic-compatibility assay to "report whether sender and
receiver transitions are being compared in the same action/time frame" -- a precondition MECH-539
does not currently state.

**NON-DEGENERACY PRECONDITION (the thought's addition).** Sender and receiver transitions must be
compared in the SAME action and horizon frame before any `good static + bad dynamic` reading is taken.
A transition-geometry null measured across a frame mismatch (one indexed at observation time, one at
predicted action time) is uninterpretable, and would be scored as F4 when it is F8/RF-F.

**CONFIRMING.** Map-initial-only (receiver evolves natively) preserves one-step and multi-step
compatibility while repeated re-mapping of sender rollout states does not -- or the reverse, each
routing differently -- with the frame correspondence asserted rather than assumed, and horizons
matched to those used to judge predictive competence (MECH-548's requirement).

**FALSIFYING.** Pointwise and transition compatibility move together across every bridge rung, i.e.
transition geometry adds no separable failure mode; or the `good static + bad dynamic` signature
disappears once the action/time frame correspondence is fixed, which would reassign the phenomenon to
MECH-555.

**Recommended disposition: (f) defer** -- MECH-539's own notes already say the diagnostic does not
yet exist; `interface_probe.dynamic_compatibility` now supplies the primitive, so the reason to defer
is the same adequacy-of-source gate as D1, not absence of an instrument.

---

## D5. MECH-540 (candidate, substrate_conditional, no `what_would_answer`)

Bearing: the thought's section 10.5 says the sleep programme "should no longer ask only whether an
interface changed before versus after sleep" but which replay event was active, what frame it
instantiated, which consumer was receptive, at what phase, which interface changed, and whether waking
recurrent stability improved.

**NON-DEGENERACY PRECONDITION.** Two interfaces with DIFFERENT predicted plasticity measured
simultaneously (MECH-540's own requirement, operationalised in the assay spec as `I_drift` and
`I_stable`), plus the parent package's sequencing bar: a waking interface metric must have
demonstrated range and stability at one locus first. `force_sleep_cycle_at_eval_boundary` exists,
which is exactly why the sequencing bar is stated -- cheapness is the trap.

**CONFIRMING.** S2 (interface recalibration): local competence stable at both endpoints by equivalence
test, communication-subspace rotation or bridge complexity improves on the plastic interface and not
on the stable one, and -- per MECH-548's corollary and this thought's section 10.5 -- closed-loop
waking stability is preserved or improved after the change.

**FALSIFYING.** S4 (maladaptive homogenisation): cross-system similarity rises while local competence
or task-specific differentiation falls -- registered as a FAILURE, not a partial success. Or both
interfaces move identically, which is generic plasticity. Or a static probe improves while the next
waking trajectory destabilises (MECH-548's S5, which GFLAG-0235 left on MECH-548).

**Recommended disposition: (c) substrate-blocked -- `substrate_conditional` (unchanged)**, plus a
note that the phase/event identifiers section 10.5 asks for are the SAME fields Gate B2 already
specifies, so no new instrument is owed.

---

## D6. MECH-547 (candidate, substrate_conditional, no `what_would_answer`)

Bearing: the thought's temporal-gate thread makes explicit an item MECH-547 lists in passing
("temporal phase" among receiver-state conditioners).

**Draft addition only** (the sibling intake deferred the full hardening): a `what_would_answer` for
MECH-547 should state that **the temporal-phase item in its conditioner list is NOT tested by the
receiver-state permutation control**, because permuting receiver state within a phase stratum leaves
phase intact. If a future result attributes a `T(A,B)` gain to "temporal phase", it is a MECH-556
result, not a MECH-547 result, and the two must be scored separately.

**Recommended disposition: (f) defer** the full draft to `/thought-digestion` per the sibling intake;
register only the separation note above so the ambiguity is not inherited.

---

## D7. MECH-096 (candidate, no `what_would_answer`, no `epistemic_category`)

Bearing: MECH-096's notes carry REE's ONLY registered reference-frame commitment -- "Dorsal-equivalent
head: egocentric, action-relevant, high temporal resolution -> z_self. Ventral-equivalent head:
allocentric, object-identity, sustained representation -> z_world" -- and it has never been
implemented (zero `egocentric`/`allocentric` matches in `ree_core/`).

**NON-DEGENERACY PRECONDITION.** Two structurally distinct encoder heads must exist with a testable
frame difference. V3 has a z_self/z_world split (SD-005 SplitEncoder) but nothing that makes one
egocentric and the other allocentric, and nothing that measures which frame either occupies. The
claim is currently untestable in the vacuous sense ARC-087 records for its own substrate gate.

**CONFIRMING.** With both heads live, a frame-diagnostic probe recovers self-relative coordinates from
z_self and agent-position-invariant coordinates from z_world at above-chance separation, AND removing
the architectural distinction (a single encoder with a learned routing gate, the alternative
MECH-096 explicitly rejects) degrades the separation and the downstream split -- the claim's own
stated failure mode, "the z_self/z_world split degrades back toward z_gamma conflation".

**FALSIFYING.** A single encoder with a learned routing gate produces the same downstream behaviour
and the same stream separation, i.e. the two-head architectural requirement is not load-bearing; or
the two heads exist and neither occupies a recoverable frame, in which case the egocentric/allocentric
language should be retired from the claim as biological motivation rather than architectural content.

**Recommended disposition: (c) substrate-blocked -- `substrate_conditional`, and a currency note that
the frame half was never built.** NOT (e) excrete: it is the only place REE records a frame
commitment, and MECH-555 now depends on it. A `/governance` pass should set
`epistemic_category: substrate_conditional` (currently absent) rather than leave the claim
surfaceable as ready experiment work.

---

## Summary of recommended dispositions

| Claim | Disposition | One-sentence justification |
|---|---|---|
| MECH-555 | (f) defer, secondary (g) merge into ARC-142 | Everything needed exists except an adequate source at a named locus, which V3-EXQ-1010 just showed the primary locus does not have. |
| MECH-556 | (a) testable now, sequenced behind Gate B1 | The levers, the instrument and the manipulation spec are all built; only the staging bar is unmet, which argues for a v3 routing. |
| MECH-537 | (a) testable now | `interface_probe.communication_subspace` supplies the RRR estimator the claim is operationalised on. |
| MECH-539 | (f) defer | The instrument now exists; the source-adequacy gate does not. |
| MECH-540 | (c) substrate-blocked, `substrate_conditional` unchanged | Two-interface plasticity comparison plus the waking-metric sequencing bar are both unmet. |
| MECH-547 | (f) defer full draft; record the phase/state separation note | A temporal-phase gain is a MECH-556 result and must not be scored as receiver conditioning. |
| MECH-096 | (c) substrate-blocked + currency note | Its egocentric/allocentric frame requirement is asserted and unimplemented, and it carries no `epistemic_category` to suppress surfacing. |

## Family A -- candidate cognitive invariants (registered ARC-144, GOV-CONTRACT-2, GOV-CONTRACT-3, MECH-557; the 14 ledger candidates stay ledger-only)

# Digestion drafts -- family A (candidate cognitive invariants)

**NOT part of the intake.** Drafts for `/thought-digestion` / `/governance` to consider; nothing here is
proposed for direct application, and no existing claim field is touched.

**Source thought:** `docs/thoughts/2026-09-08_candidate_cognitive_invariants.md`
**Date drafted:** 2026-09-15 | **Session:** thought-pipeline-20260915

**Extraction-before-invention note.** Almost every falsifier below is the thought's own language (its
section 16 lists ten programme falsifiers, section 14 the crossed design, section 15 the failure
signatures) or is already present in
`evidence/planning/cognitive_contract_narrowing_stack_preregistration_2026-09-08.md` (arms A-E, gates
G0-G5, the pre-results prediction table) or in the ledger's per-record `lesion_prediction` and
`alternative_explanation` fields. Where a falsifier is invented rather than extracted it is marked
**[drafted]**.

**Currency check performed.** For every cited blocker or run: `ree-v3/experiment_queue.json` holds 1 item
and none is a cognitive-contract entry; `REE_assembly/evidence/experiments/` contains no matching run; and
`evidence/planning/substrate_queue.json` contains zero occurrences of `cognitive_contract`, `ARC-142` or
`MECH-545`. Nothing in this programme has been run, queued or given a substrate owner. No cited blocker
has resolved since 2026-09-08 except the three "missing planned artefacts" (see intake s.7.2), all of
which had in fact landed before the thought was written.

---

## Part 1 -- proposed new claims

### ARC-144 -- boundary-indexed contract obligations

- **NON-DEGENERACY PRECONDITION.** At least two heterogeneous interfaces have been instrumented with the
  SAME candidate relation and the SAME receiver-accessible recoverability measure, and the relation is
  measurably present at at least one of them. If one boundary is instrumented, or the relation is absent
  everywhere, the claim is untestable rather than false: a single-boundary programme cannot distinguish
  "boundary-indexed" from "universal".
- **CONFIRMING.** A relation is shown obligatory at one boundary (nuisance-controlled lesion produces the
  predicted deficit, MECH-545) and NOT obligatory at another -- the receiver at the second boundary
  reconstructs it locally within its own compute/latency budget with no behavioural cost -- with the
  dissociation replicating across seeds. Plus, over several boundaries, a measured OVERLAP set that is
  non-empty and smaller than the union: obligations differ, and a core exists.
- **FALSIFYING.** Two outcomes, in opposite directions, both count. (i) **Universality**: every
  instrumented boundary requires the same obligation set, with no relation ever locally reconstructable --
  the flat ARC-142 reading was right and the indexing is bookkeeping. (ii) **Falsifier 10** (the thought's
  own): useful obligations exist per boundary but their OVERLAP across the cognitive graph is negligible
  -- there is no shared core, and the contract is a set of interface specifications rather than an
  architecture of cognition. ARC-144 survives only the middle.
- **DISPOSITION: (c) substrate-blocked -- `substrate_conditional`.** Never exercised: multi-boundary
  instrumentation does not exist, and MECH-545's lesion pattern is itself unbuilt. Not a ceiling -- the
  code is absent, not absorbing signal.
- **Justification.** The claim is about a comparison across boundaries, and REE currently has no
  instrument that measures the same thing at two of them.

### GOV-CONTRACT-2 -- promotion ladder

- **NON-DEGENERACY PRECONDITION.** At least one candidate has reached a stage above 1, so the ladder has
  discriminated something. Until then the rule is a refusal rule only, and "no candidate has been
  registered" is consistent with both the rule working and the programme being stalled.
- **CONFIRMING.** [drafted] The ladder gives a DIFFERENT answer from the prior wording on a real case,
  and the different answer turns out to be the right one in hindsight -- e.g. a candidate registered under
  the old "ledger record + lesion prediction" test is later shown reducible or boundary-local, and would
  have been held at Stage 1-3 by this ladder. Evidence of use, not of formalisation (same promotion
  discipline as GOV-PATHVALID-1 / GOV-INTERVENE-1).
- **FALSIFYING.** The ladder is applied and every candidate either passes all six stages trivially (the
  stages do not discriminate) or none ever passes Stage 2 over a long programme while the candidates are
  nevertheless independently shown load-bearing by other routes (the ladder is measuring instrument
  availability rather than candidate quality). Either outcome says the stages are the wrong cuts.
- **DISPOSITION: (b) derivational**, with a use-gated promotion condition. It is a governance rule with no
  substrate dependency; its status should not move to `provisional` until it has been *applied* in a live
  `/governance` pass, per the GOV-INTERVENE-1 / GOV-PATHVALID-1 precedent ("promote only after live use,
  not merely after formalisation").
- **Justification.** Nothing in V3 bears on whether the ladder is the right ladder; only governance
  practice does.

### GOV-CONTRACT-3 -- reduction admissibility

- **NON-DEGENERACY PRECONDITION.** A concrete merge proposal exists with an explicit before/after basis,
  and the cost terms are at least coarsely estimable for both. MECH-557 is that proposal; without it the
  rule has nothing to score.
- **CONFIRMING.** [drafted] A proposed merge that looks compelling on relabelling grounds is REFUSED by
  the relocation checklist -- the lost distinction is found in the decoder, a context tag or a side
  channel -- and the refusal is later vindicated (the merged basis fails a discriminating-prediction test
  the unmerged basis passes). One such case establishes the rule catches something the naive criterion
  does not.
- **FALSIFYING.** Every merge proposal fails the cost test for reasons that turn out to be measurement
  artefacts (cost terms not estimable at the available precision), so the rule blocks all reduction and
  the basis grows monotonically -- the thought's own falsifier 8 ("The basis continually expands ... total
  description cost fails to fall"). Alternatively, the symmetry clause is never exercised -- no retention
  is ever argued for, only reductions policed -- in which case the rule is one-sided in practice whatever
  its text says.
- **DISPOSITION: (b) derivational.**
- **Justification.** Same as GOV-CONTRACT-2; the rule's correctness is a question about governance practice
  and cost-accounting, not about V3.

### MECH-557 -- the 3 + 2 reduction hypothesis

- **NON-DEGENERACY PRECONDITION.** The crossed design of the thought's section 14 can actually be
  instantiated: structure and weighting must be independently manipulable. Concretely, there must exist a
  manipulation that changes confidence at FIXED structural content, and one that changes structural
  content at FIXED confidence -- and a positive control showing each manipulation moves its own target.
  If the two cannot be varied independently at all, the experiment cannot test the model and returns
  "assay invalid", not "model wrong" (prereg gate G1's role).
- **CONFIRMING.** All five crossed contrasts dissociate along the structure/field boundary: structural
  families (correspondence, event/trajectory, lineage) survive object/world remapping when the world
  relation is preserved despite altered surface features, while epistemic and regulatory weights vary
  strongly with uncertainty, need, goal, physiology and task regime at fixed structure. Plus: the absorbed
  candidates' failure signatures collapse onto the five reduced signatures of section 15 rather than
  remaining fourteen-way distinct, AND the merge passes GOV-CONTRACT-3's three collapse requirements (lower
  total cost, discriminating predictions preserved, transfer improved).
- **FALSIFYING.** Four distinct routes, all extracted: (i) structural and weighting variables **cannot be
  dissociated** by the crossed design -- the thought's own stated refutation ("the 3 + 2 model is wrong or
  too simple"); (ii) a held-out residue survives -- intervention/control residue (passive prediction
  preserved with selective loss of action-effect learning and controllability attribution) or
  expected-absence residue (inability to represent omitted expected events despite intact raw surprise) --
  showing the families do not absorb CCI-004 or CCI-011; (iii) the reduction succeeds only by decoder
  inflation (falsifier 9), caught by GOV-CONTRACT-3; (iv) the fourteen candidates' failure signatures remain
  mutually distinguishable under nuisance-controlled perturbation, i.e. the merges destroy discriminating
  predictions.
- **DISPOSITION: (c) substrate-blocked -- `substrate_conditional`**, and specifically
  **substrate_conditional, NOT substrate_ceiling**: the mechanisms are absent, not built-and-absorbed.
  Family C's V3 analogue is a binary `Trajectory.hypothesis_tag` with injector-only source metadata
  (`ree-v3/ree_core/predictors/e2_fast.py:41-70`, `ree_core/hippocampal/module.py:833-843`) rather than a
  lineage structure; field D's translation-confidence subcase has zero substrate representation
  (`grep -rln "translation_confidence\|bridge_confidence" ree_core experiments` -> 0).
- **Justification.** Testing it needs a rate-constrained multi-consumer bottleneck that does not exist
  (no KL/variational, quantisation, noise-injection, sparsity or rate-regularisation machinery anywhere in
  `ree_core`) plus generative-lineage structure that does not exist.
- **Additional routing note.** The prereg's pre-results prediction table already contains two rows that
  bear on this claim ("factorial status axes transfer better than coarse mode labels" -> supports the
  representation-of-representation-system account; "viability basis transfers better than signed value" ->
  supports value-as-derived H2). Those are MECH-557's family-C and field-E predictions written a week
  early; whoever digests this claim should reuse that wording rather than redraft it.

---

## Part 2 -- existing claims this thought materially bears on

All five contract claims and two of their neighbours were checked: **none has a `what_would_answer`
field** (verified by loading `claims.yaml`; `GOV-INTERVENE-1` is the only claim in this neighbourhood that
does). Drafts follow for the five the thought bears on most directly.

### ARC-142 (candidate, `substrate_conditional`, v4) -- the cognitive contract

- **NON-DEGENERACY PRECONDITION.** At least one inter-engine boundary is instrumented well enough that a
  relation can be shown recoverable at it by the RECEIVER (INV-105 rung 3), not merely by an external
  probe. Without that, both "contract preserved" and "contract failed" are unobservable and every result
  is about the probe.
- **CONFIRMING.** Engines maintain measurably DIFFERENT representational geometries (global similarity
  flat or falling) while a small, stable set of relations remains receiver-recoverable across their
  boundaries, and behavioural coherence tracks the relations rather than the geometry -- the thought's
  falsifiable claims 4-5, and the non-redundant developmental prediction MECH-538 already registers
  (specialisation and legibility rising together).
- **FALSIFYING.** The thought's section 16 supplies ten; four falsify ARC-142 rather than the method.
  (1) **No reusable compact structure exists** -- different consumers repeatedly require unrelated
  task-specific exchange variables, with no set recurring across boundaries. (2) **Ordinary latent
  geometry is operationally enough** -- actual receiving modules cheaply reconstruct every required
  distinction locally, so nothing must be preserved. (3) **Probe-only invariants dominate** -- candidate
  information is externally decodable but unavailable to or unused by receivers (INV-105 rungs 2 but not
  3/6). (10) **Boundary-specificity defeats a shared core** -- see ARC-144.
- **DISPOSITION: (c) substrate-blocked, `substrate_conditional`.** Unchanged from registration.
- **Justification.** No boundary in V3 is instrumented for receiver-side recoverability; the mutual-
  legibility instruments (ML-10..ML-15) that would supply it are themselves owed.

### GOV-CONTRACT-1 (candidate, `governance_rule`, v3) -- admissibility

- **NON-DEGENERACY PRECONDITION.** The ledger has entries whose classification the rule actually
  determines. Satisfied since 2026-09-08 -- which is itself the point: the rule's own notes still say
  "THE TWELVE-FIELD LEDGER IS NOT BUILT ... until it exists the rule is warn-only". **That note is stale
  and should be corrected before any `what_would_answer` is attached**, or the precondition will be read
  as unmet.
- **CONFIRMING.** [drafted] The four-way classification and the >= 2-of-6 quorum give a different answer
  from an unclassified reading on a real candidate, and the different answer survives a later independent
  pull. The 2026-09-14 Session-B reconciliation is the first live instance: CCI-003's linguistic cell was
  graded `supports` by Session A and `s` (areal/cultural-leaning) by Session B, and the rule is what forces
  that disagreement to be recorded per-record rather than silently averaged.
- **FALSIFYING.** (5) **Cross-domain convergence evaporates** -- linguistic, developmental, neural,
  comparative and artificial-system evidence support mutually incompatible structures, so the quorum is
  aggregating noise. Or: the quorum is met by every candidate ever proposed, making it non-discriminating
  (a bar nothing fails is not a bar). Currently 4 of 14 records are `admitted` and 0 are `not_required`,
  which is closer to discriminating than not -- but **zero `not_required` records after three literature
  tranches is worth watching**, because the rule's most valuable clause is the one that preserves negative
  findings, and it has never once fired.
- **DISPOSITION: (b) derivational**, use-gated promotion as for GOV-CONTRACT-2.

### MECH-545 (candidate, `substrate_conditional`, v4) -- contract-lesion assays

- **NON-DEGENERACY PRECONDITION.** A within-boundary content-preserving CONTROL exists and works -- the
  lesion must be shown to delete the relation while leaving content intact, distinguished from MECH-537's
  encoded-but-not-exposed phenotype (INV-105 rung 3 vs rung 2). Without that control every lesion result
  is generic information loss.
- **CONFIRMING.** Each of the five lesions, applied at ONE inter-engine boundary, produces a signature
  distinct from the other four AND from a dimensionality-matched random-projection floor, replicating
  across seeds, with acute-frozen-weights and adapted phases separated per ARC-140.
- **FALSIFYING.** (4) **Lesion specificity disappears** -- controlled corruption produces only generic
  information loss, no five-way dissociation. Also, per the thought's section 12, two asymmetric failure
  routes that must be excluded before either verdict: an **off-manifold** lesion damaging unrelated
  computations (false positive: the candidate looks necessary) and **compensation** through an alternative
  pathway (false negative: the mechanism looks unnecessary if only post-adaptation behaviour is examined).
- **MERGE / DEPENDENCY PROPOSAL, not a merge of claims.** MECH-545's `depends_on` should gain **ARC-140**
  and **GOV-INTERVENE-1**. The thought's section 12 causal standard is almost entirely those two claims
  (ARC-140: acute vs adapted, altered causal-importance distribution, selective re-ablation, restoration,
  four-arm design; GOV-INTERVENE-1: the explicit on-/near-/off-manifold construction axis and the
  intervention-attribution rule). No survivor, no absorption -- two edges. Reverse-deps unaffected.
- **DISPOSITION: (c) substrate-blocked, `substrate_conditional`.** The reality-status lesion remains the
  cheapest V3-buildable cousin, but see the currency note below.
- **Currency correction on that cousin.** Both the parent intake and MECH-545's own notes say
  "force-dropping `committed_vs_imagined` at the replay -> consolidation boundary is a small edit". Verified
  2026-09-15: `grep -rn "committed_vs_imagined\|source_status" ree_core experiments` -> **0 hits**. The
  MECH-365 token structure is unbuilt; what exists is `hypothesis_tag` used as a boolean **write gate** at
  that boundary (`ree_core/sleep/mel_consumer.py:46,178`, `ree_core/sleep/phase_manager.py:255`). The
  lesion is still cheap -- forcing the gate open is a small edit -- but it perturbs a *gate*, not a
  *status carried across the boundary*, which is a weaker instance of the assay pattern than the notes
  imply. Whoever routes this should say which of the two they mean.

### MECH-546 (candidate, `substrate_conditional`, v6) -- grammar inherits the contract

- **NON-DEGENERACY PRECONDITION.** The two directions can disagree. If the set of "invariants derived from
  cognition" is read off grammar in the first place, direction (a) is guaranteed and the test is circular
  -- which is exactly the contamination GOV-CONTRACT-1 and the prereg's language firewall exist to
  prevent, so the precondition is: the candidate set was frozen BEFORE the typological comparison.
- **CONFIRMING.** Agreement across both directions: contract-derived invariants over-represented among
  recurrently grammaticalised distinctions, AND recurrently grammaticalised distinctions lacking
  developmental/comparative/computational support classifying as embodied or cultural. Plus the
  emergent-communication prediction: agents transmitting invariant-rich states over a low-cost channel
  develop grammar-like structure for contract relations and not for schema content.
- **FALSIFYING.** Either direction alone (the claim says agreement is the evidence). Concretely: the
  grammaticalised set and the contract set are statistically independent; or agents develop grammar-like
  structure for schema content as readily as for relations. **Existing contrary evidence already in the
  corpus:** `evidence/literature/targeted_review_cognitive_contract_invariants/entries/` carries
  `2026-09-08_mech_546_compositionality_not_required_for_generalization_chaabouni2020` -- compositionality
  is not required for generalisation in emergent communication, which weakens the channel-converges-on-
  relational-structure half. That entry should be read before any confirming citation is attached.
- **DISPOSITION: (f) defer.** v6 per ARC-100's language phase; nothing in V3 or V4 exercises it, and the
  typological work is a `/lit-pull`, not an experiment.

### Q-104 (open, `substrate_conditional`, v4) -- cognifold vs braidling

- **NON-DEGENERACY PRECONDITION.** A severance is actually performable and reversible on both candidate
  configurations -- within-agent (E1/E2/E3/hippocampus) and between-agent -- and a coherence measure
  exists that is not simply task performance. Otherwise the criterion cannot be applied to either side.
- **CONFIRMING.** The severance assay places E1/E2/E3/hippocampus on the cognifold side (severance
  degrades coherence on BOTH sides, not merely coordination) and two communicating REE agents on the
  braidling side (each remains independently coherent), with the placement tracking a measurable
  contract-dimension dependency or MECH-538 bridge complexity rather than being stipulated.
- **FALSIFYING.** The criterion does not separate the two configurations -- either everything severs
  gracefully (no cognifold anywhere in REE) or nothing does (the distinction is not doing work). Also
  falsified if placement tracks task coupling strength alone, with no contract-dimension dependency
  signal: the question would then be answered by ordinary coupling measures and not need the contract.
- **NEW ROUTING FROM THIS THOUGHT.** Section 18 sharpens the cognifold side to "unity could be a property
  of the transformation NETWORK rather than of any one representation". Under ARC-144 that is directly
  operationalisable: the cognifold is the region of the interface graph whose boundary obligations
  OVERLAP, and the braidling boundary is where overlap goes to zero. If ARC-144 is registered, Q-104
  should gain it as a `depends_on` -- the overlap measurement ARC-144 demands is a candidate severance
  criterion.
- **DISPOSITION: (c) substrate-blocked, `substrate_conditional`**, with the severance assay
  `complex (probe-gated)`: a spike measuring obligation overlap at two boundaries would convert it to
  `puzzle (known rules)`.

---

## Part 3 -- dispositions summary

| Claim | Disposition | One-sentence justification |
|---|---|---|
| ARC-144 | (c) substrate-blocked, `substrate_conditional` | Requires the same recoverability measure at two boundaries; no boundary is instrumented. |
| GOV-CONTRACT-2 | (b) derivational, use-gated promotion | A governance rule with no substrate dependency; promote only after live application. |
| GOV-CONTRACT-3 | (b) derivational, use-gated promotion | Same; its correctness is a question about cost-accounting practice, not about V3. |
| MECH-557 | (c) substrate-blocked, `substrate_conditional` | Needs rate-constrained multi-consumer compression and a lineage structure; neither exists in `ree_core`. |
| ARC-142 | (c) substrate-blocked, `substrate_conditional` | No boundary instrumented for receiver-side recoverability. |
| GOV-CONTRACT-1 | (b) derivational | Applies now; stale "ledger not built" note should be corrected first. |
| MECH-545 | (c) substrate-blocked + two `depends_on` edges owed (ARC-140, GOV-INTERVENE-1) | Assay pattern unbuilt; its causal standard is already owned by two uncited claims. |
| MECH-546 | (f) defer | v6 language phase; the owed work is a typology `/lit-pull`, and contrary evidence is already filed. |
| Q-104 | (c) substrate-blocked; severance assay `complex (probe-gated)` | No severance is performable; an overlap spike would convert it to `puzzle (known rules)`. |

**No `(e) excrete` and no claim merge is proposed.** The only merge-shaped item is the MECH-545
`depends_on` addition, which is an edge, not an absorption. **No candidate cognitive invariant appears
anywhere in this file as a claim**, per the intake's section 0.

## Family C -- convergence signal cluster (registered MECH-558, MECH-559, INV-108; the aha/insight claim NOT registered -- deferred, see aha intake section 5)

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

### MECH-558 -- independence-aware convergence topology

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

### MECH-559 -- evidence dependency vs downstream leverage

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
qualification as MECH-558. The leverage half is the harder gap: nothing in `ree_core/` represents which
consumers an unresolved uncertainty would update.

### INV-108 -- convergence detected, not trained

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

### NEW-MECH-3 (NOT REGISTERED -- deferred) -- cross-model restructuring as an insight-candidate event

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
carried as a sentence in MECH-558's notes instead. A (g) MERGE proposal is also defensible: make it a
child of MECH-423 (survivor MECH-423, absorbed NEW-MECH-3 (NOT REGISTERED -- deferred), reverse-deps none since nothing depends on a
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
> "abstraction is wrong" axis. (Relevance to this family: NEW-MECH-3 (NOT REGISTERED -- deferred)'s impostor (1) -- compression that
> deletes organism-relevant distinctions -- IS overmerge, and inherits whatever discriminability
> MECH-126 can establish.)

---

## Part 3 -- dispositions summary

| Item | Disposition | One-sentence justification |
|---|---|---|
| MECH-558 | (c) substrate_conditional; shadow-only variant may be (a) | No dependency-corrected quantity exists in `ree_core/` at all, but every input a shadow diagnostic would read already exists in V3. |
| MECH-559 | (c) substrate_conditional | The dependency half has partial V3 substrate (MECH-441, MECH-482) but nothing represents downstream consumers, so the leverage half cannot be measured. |
| INV-108 | (c) substrate_conditional + (f) defer on V3 | V3 has no agreement objective to prohibit; the invariant guards a future architecture and its falsifier is synthetic. |
| NEW-MECH-3 (NOT REGISTERED -- deferred) | (c) substrate_conditional, strong (f) defer candidate, (g) merge-into-MECH-423 defensible | Externally pre-empted, nearest REE claim already evidenced, and the revision mechanism it would detect events over is itself unbuilt (MECH-531). |
| Hub "convergence is a general computational signal" | (e) excrete -- survivor MECH-558 | The family's own stress test retracted the broad form; registering it would re-mint a retracted claim. |
| Aha = restructuring + model reduction | (c2)/(e) out-of-domain and pre-empted -- survivor: external literature | Friston et al. 2017 and Kounios & Beeman 2014 occupy it; REE should cite, not claim. |
| Diversity file sections 1,2,3,5,6,9,10,11 | (e) excrete -- survivors ARC-065, MECH-309, INV-074, INV-076, MECH-333/334, MECH-496, ARC-128, MECH-165, MECH-529, SD-091, ARC-139 | Re-derivation of owned claims with no new falsifier. |
| Diversity section 10 sleep hypothesis | (g) merge into **Q-055** | Q-055 already asks exactly this; the thought's "replay rare dissenting episodes" is `what_would_answer` material for it. |
| Formal notes: every named formula | instrument, not a claim | GOV-SHARPEN-1's over-splitting guard; six of them already exist as assay code. |
| `R_drop`, `delta K`, `S_t`, `C_pair` | (a) buildable now, synthetic | Four unimplemented measurements the family's own notes call for; `R_drop` is the highest value and the cheapest. |
| Assays 001-006 with empty `claim_ids` | `/governance` decision | Six passing preregistered runs attach to no claim; whether they may cite a newly registered id, and under what evidence class, is not an ingestion decision. |

## Family G -- dynamic information governance (registered ARC-145, MECH-560, MECH-561, Q-106; propagation and replay-access claims NOT registered -- deferred, see hub intake section 5)

# Digestion drafts -- FAMILY G (2026-09-10 dynamic information governance / routing / phase)

**Date drafted:** 2026-09-15
**Session:** thought-pipeline-20260915
**Status: INPUT TO `/thought-digestion`, NOT A REGISTRATION.** None of these triads was written into
any `claims.yaml` block. `what_would_answer` hardening is digestion's job, not ingestion's; these
drafts exist so digestion does not have to re-derive them from 1,832 lines of source.

**Method note.** Extraction before invention: every falsifier below is the source family's own
language where the family supplied one (hub F1-F9, routing note s.11, phase note s.13), or an
existing sibling's registered control where one applied (INV-105's mismatched/zero/moment-matched-random
controls, GOV-MATCHAUX-1's matched capacity, MECH-538's high-capacity-bridge warning, Q-081's
constrained-realisation surrogate, MECH-547's receiver-state permutation).

**Currency verified for every blocker cited below** (2026-09-15): V3-EXQ-1010 has landed
(PASS / `H-F-confirmed`, run `20260909T195348Z`) and still disqualifies trained `z_world`; the P0
interface instrument HAS landed (`ree-v3 experiments/_lib/interface_probe.py`, commit `a83f2fb`), so
"instrument-blocked" is no longer true at the P0 level; `ree-v3/experiment_queue.json` holds one
unrelated item, so nothing in this family is in flight.

---

# Part A -- the six proposed new claims

## ARC-145 (dynamic information governance: three-level interface completeness)

**NON-DEGENERACY PRECONDITION.** At least one interface must exist at which levels 1 and 2 are
*already satisfied and measured*: a sender demonstrated to contain the decision-relevant content
(rung 1-2 of INV-105, on a measured-adequate source -- `rawfield25` primary), a frozen receiver
demonstrated not to use it natively (rung 3 fails), AND a constrained bridge demonstrated to restore
receiver use with both endpoints continuously available (rung 4 succeeds). Without all three, a
"jurisdiction" reading is unavailable by construction: content absence (V3-EXQ-1010's H-F) and
consumer collapse (MECH-517) both produce the same downstream null. **Verified absent as of
2026-09-15:** no such locus has been measured -- the instrument now exists but no assay has run.

**CONFIRMING.** At a locus satisfying the precondition, the SAME bridge with the SAME parameters
restores held-out behavioural competence when the message is delivered under one organism state and
fails to when delivered under another, at matched message count, matched transmitted norm, matched
receiver-local competence and matched episode phase -- and the state variable that separates the two
is not a property of either endpoint.

**FALSIFYING.** A static bridge between frozen endpoints restores the full behavioural phenotype
irrespective of delivery timing or organism state (the family's own F2). Then levels 1-2 plus
MECH-539 exhaust interface completeness and this commitment should be withdrawn, not weakened.

**DISPOSITION: (f) defer with reason.** Architectural commitments should not be hardened before the
mechanism claims beneath them have a single measurement. Defer until MECH-560's observational leg
or MECH-561's diagnostic has produced any result at any locus.

---

## MECH-560 (governed selectivity beats transfer volume)

**NON-DEGENERACY PRECONDITION.** (a) A measurable, non-constant directed-influence statistic over at
least three real producer-consumer interfaces, showing live variance across arms and seeds; (b) a
constrained-realisation surrogate null per Q-081 -- preserving each stream's tick grid, marginal
distribution and within-stream autocorrelation, destroying only the between-stream relation --
**validated before it adjudicates anything** by killing a deliberately-artefactual statistic and
sparing a deliberately-injected real one; (c) a demonstrated ability to vary total transfer and
selectivity independently, since the whole claim is a dissociation and is vacuous if the two cannot
be dissociated in this substrate. **Verified absent 2026-09-15:** no directed-influence estimator
exists anywhere in `ree-v3` (hub audit row 5), and Q-081's own telemetry-audit precondition is
unanswered.

**CONFIRMING.** High-competence episodes show more selective and more stable sequences of directed
influence than matched low-competence episodes at matched total activity and matched traffic; AND a
matched-traffic lesion (gain flattening, edge permutation, or timing permutation at preserved gain
marginals) degrades integrated behaviour while endpoint-local decodability and endpoint-local
competence are unchanged and total inter-module transfer is matched or higher. The three degradation
modes produce distinguishable signatures rather than one.

**FALSIFYING.** Any of: performance is fully explained by total transmitted activity or message count
once matched (F1); a one-dimensional global arousal/gain scalar explains the whole effect (F3 --
note SD-037's `override_signal` is exactly such a scalar and already exists, so this rival is not
hypothetical); total transfer always falls whenever behaviour falls, so the high-traffic/low-tuning
regime does not occur in REE at all; or the apparent directional structure survives only estimators
that are functions of the configured update rates (Q-081's a-priori filter).

**DISPOSITION: (b) derivational for the lesion leg / (a) testable-now for the observational leg --
SPLIT RECOMMENDED.** The observational leg is runnable read-only over recorded trajectories once a
directed-influence estimator is written (`complicated (buildable)`, no `ree_core` change, no unknown).
The matched-traffic lesion leg needs an experiment-layer inter-engine gain overlay that does not
exist, and should stay `substrate_conditional`. Digestion should propose the split to `/governance`
rather than assigning one version to both.

---

## NEW-MECH-2 (NOT REGISTERED -- deferred: propagation) (propagating routing state)

**NON-DEGENERACY PRECONDITION.** A routing state must first be shown to EXIST and to be
load-bearing -- MECH-560 confirming, or an equivalent -- and a *declared functional adjacency
graph* over REE's interfaces must be committed in advance, because "adjacent interfaces open in
order" is unfalsifiable if adjacency is chosen after seeing the sequence. **Verified absent
2026-09-15:** no routing state, no adjacency declaration, no propagation machinery anywhere
(`routing_state` / `g_ij` / `travelling` -> 0 hits across `ree-v3`).

**CONFIRMING.** With the adjacency graph pre-declared, a low-rank routing overlay whose loadings
respect it outperforms an otherwise identical overlay whose loadings are permuted across the graph,
at matched gain marginals, matched temporal autocorrelation, matched parameter count and matched
compute -- and the advantage grows with the number of sequential hops a task requires.

**FALSIFYING.** The propagation-break lesion (local routing state retained, the neighbour dependency
removed) performs equivalently at matched gain marginals and autocorrelation -- isolated gates
suffice. **Or** the best-fitting model is abrupt switching between a small number of global routing
modes, in which case the source's own disposal clause applies: keep ARC-145 and MECH-560, discard
the propagation claim. **Or** the routing overlay's advantage survives a content-poverty audit
failure -- i.e. the overlay is found to carry semantic information -- in which case it is performing
cognition, not governing flow (F4).

**DISPOSITION: (c) substrate-blocked, `substrate_conditional`** -- the mechanism has never been
exercised because the code is absent. Explicitly NOT `substrate_ceiling`. Secondary recommendation:
digestion should record the disposal clause as a first-class stop condition so a later session does
not quietly retain the wave framing after the governance result survives without it.

---

## NEW-MECH-3 (NOT REGISTERED -- deferred: proposed as MECH-540 signature) (causal access correspondence maintained by replay)

**NON-DEGENERACY PRECONDITION.** Four things, all currently absent: (a) a controlled task-relevant
DRIFT that provably creates an interface lesion rather than a content loss (the replay-maintenance
supplement's own Gate 0); (b) `(sender_episode, receiver_episode)` pairing expressible at the
experiment layer -- **verified absent in `ree_core` 2026-09-15**, no `sender_episode` /
`receiver_episode` / `paired_replay` anywhere, and `cross_module_consolidation.py` schedules module
losses with no pairing; (c) a replay path whose content reaches a consumer -- the MECH-285 sampler's
draws now do (`phase_manager.py:435-525`), MECH-092's `_do_replay` still does not
(`mech092-replay-consumer-missing`); (d) a *routing/timing* variable distinct from the representational
pairing, which presupposes MECH-561's `phi` or an equivalent.

**CONFIRMING.** In the 2x2, `correct-representation + correct-routing` beats
`correct-representation + shuffled-routing` on held-out receiver causal use and behaviour, at matched
marginals, matched event count, matched inter-event intervals, matched activation magnitude and
matched total weight change, while endpoint-local recall and endpoint-local competence are equal
across all four cells.

**FALSIFYING.** `correct-representation + shuffled-routing` is indistinguishable from
`correct-representation + correct-routing` -- routing correspondence is not separately maintained and
MECH-540 alone suffices. **Or** a timing main effect appears with NO pair specificity, which the
replay-maintenance supplement already rules supports plasticity gating or consolidation rather than
interface repair -- this is the failure mode most likely to be misread as confirmation.

**DISPOSITION: (c) substrate-blocked (`substrate_conditional`), and (g) MERGE CANDIDATE.** Digestion
should put to `/governance` whether this is better landed as a **fifth signature on MECH-540** (S5:
the maintained object includes the access state) than as a separate claim -- MECH-548's sleep
corollary already has a proposed S5 pending, so MECH-540's signature list is already open for
amendment and adding two at once is cheaper than two claims. If kept separate, survivor is this
claim, absorbed is nothing, and MECH-540 gains a reverse-dependency.

---

## MECH-561 (phase as an addressing coordinate)

**NON-DEGENERACY PRECONDITION.** (a) The chosen `phi` must have live variance and must not be a
deterministic function of the configured update rates (Q-081's a-priori filter) -- `_e3_phase_step`
qualifies because MECH-091's salient-event reset makes it event-driven rather than purely periodic,
whereas a raw multi-rate tick index does NOT and should be excluded; (b) `breath_period > 0` if the
BreathOscillator is the chosen `phi`, since it defaults OFF and historical trajectories recorded
under the default contain no breath phase; (c) enough rows per phase bin to fit a rank-selected RRR
without the bin count itself driving the principal angles -- a bin-count sweep is required, not
optional; (d) a sender measured to contain the content (`rawfield25`; trained `z_world` inadmissible
per V3-EXQ-1010). **All four are satisfiable today** -- this is the one claim in the family whose
diagnostic is not blocked.

**CONFIRMING.** Principal angles between phase-conditioned subspaces exceed the surrogate null; a
phase-conditioned model beats a static subspace on held-out receiver prediction **at matched
complexity**; the downstream causal effect of a fixed sender direction varies with `phi` while the
sender's decodability does not; and a **receiver-state permutation run alongside the phase
permutation** shows the phase permutation independently destroys the gain (otherwise MECH-547 owns
the result).

**FALSIFYING.** Any of the phase note's own eight: a static subspace explains receiver activity and
behaviour as well at matched complexity; a global scalar gain explains it without receiver-specific
temporal structure; **random temporal labels perform as well** as the endogenous coordinate; phase
predicts correlation but not causal susceptibility; the effect disappears after controlling for task
context, action identity or arousal; the periodicity is traceable to environment sampling; the
conditioned model wins only by added capacity; or disrupting the hypothesised read window leaves
behaviour unchanged. Add one not on that list: **MECH-466's event-relative index outperforms any
cyclic `phi`**, which would relocate the finding to MECH-466 rather than refute the governance idea.

**DISPOSITION: (a) TESTABLE NOW on the V3 substrate -- observationally.** The estimator
(`interface_probe.py`) and the coordinates (`clock.py`) both exist as of 2026-09-15. One strong
caveat digestion must carry to `/governance`: the 2026-09-07 sequencing rule ("do not queue the
developmental or sleep assays until a single waking interface metric has demonstrated range and
stability at one locus; otherwise the assay measures the instrument") applies, and the assay being
*cheap* is precisely the trap that rule names. The causal lesion ladder remains
`substrate_conditional`.

---

## Q-106 (endogenous vs scheduled routing generation)

**NON-DEGENERACY PRECONDITION.** A routing state that is load-bearing (MECH-560 or NEW-MECH-2 (NOT REGISTERED -- deferred: propagation)
confirming) AND two generators whose OUTPUT statistics can be matched to a declared tolerance --
gain distribution, temporal autocorrelation, motif dwell, transition entropy -- because an unmatched
comparison measures the statistics, not the loop. **Verified absent 2026-09-15:** neither generator
exists; nothing in `substrate_queue.json` plans either.

**CONFIRMING.** At matched output statistics, matched parameters and matched compute, the
closed-loop generator beats the open-loop schedule on at least two of: robustness to perturbation,
reconfiguration speed after a context change, adaptive routing in unseen contexts, recovery after a
transient lesion. Raw task score is explicitly excluded as a readout.

**FALSIFYING.** Identical performance on all four -- endogenous field feedback is unnecessary and the
simpler scheduled field is kept. Also falsifying-by-invalidation: the closed-loop generator's
advantage disappears against a *random recurrent control field* of the same capacity, which would
show the gain came from recurrence rather than from the specific coupling.

**DISPOSITION: (f) defer with reason.** Last stage of the family's own programme. Opening it before
the earlier stages have results would test a field nothing has shown to be load-bearing, which is the
error the family explicitly warns against.

---

# Part B -- existing candidate claims this family materially bears on, with NO `what_would_answer`

Confirmed by inspection 2026-09-15: MECH-534, Q-103, MECH-537, MECH-540 and MECH-547 all carry
`status: candidate`/`open` and **no `what_would_answer` field**. (MECH-225, SD-091, MECH-481, Q-081
and MECH-271 DO have one and are not drafted here.)

## MECH-534 -- authority field

**NON-DEGENERACY PRECONDITION.** Two matched runs must be constructible that differ in "field state"
while content state is held materially similar -- which requires a field to exist. Digestion must
FIRST discharge MECH-534's own registered instruction: ask whether it reduces, under another name, to
one of `MECH-359` + ARC-065 GAP-A (candidate-conditioned transform, built), SD-032a's
`SalienceCoordinator` operating-mode vector, MECH-254's top-k boundary, or SD-037's broadcast
regulator. **This pass adds two candidates that instruction predates and that must join the list:**
**`VsRolloutGate` (MECH-269b)** -- a per-stream, verisimilitude-thresholded, hysteretic hold/substitute
gate at the E1 sensory-predictor and E2 forward-model call sites, i.e. a state-conditioned gate on
inter-engine input, default OFF -- and **`RoutingGate` (MECH-272)**, a state-conditioned per-phase
destination-weight table. Neither is MECH-534, but neither was on the list, and a reduction check that
misses them is incomplete.

**CONFIRMING.** Two runs with materially similar content state but different field state differ
systematically in retrieval, commitment and distractor recovery, and an equally-parameterised static
scalar or global gate cannot reproduce the same context-sensitivity across matched tasks and seeds.

**FALSIFYING.** (From MECH-534's own notes, unchanged.) A static scalar control plane matches or beats
the field; the field improves internal separability with no causal downstream effect; the gain comes
only from extra parameters under matched capacity and exposure; field state is exogenously injected
rather than recruited; the system becomes brittle or oscillatory without improving ecological tasks.

**DISPOSITION: (c) substrate-blocked, `substrate_conditional`** -- code absent, never exercised.

## Q-103 -- routing-only or representational field

**NON-DEGENERACY PRECONDITION.** MECH-534 must have some instantiation whose state trajectory can be
recorded; and the instantaneous and trajectory decoders must be matched on parameter count and
training exposure, or the trajectory decoder wins by capacity.

**CONFIRMING (representational branch).** The trajectory decoder over `r(t-k:t)` plus the authority
variables predicts current global structure, the appropriate retrieved path, or the next committed
action better than the matched instantaneous decoder over `r(t)` on the SAME stored representations.

**FALSIFYING (routing-only branch).** The trajectory decoder adds nothing at matched capacity -- the
field sets eligibility and topology over content stored elsewhere.

**DISPOSITION: (c) substrate-blocked.** Note for digestion: Q-106 is the orthogonal fork (how the
field is GENERATED, not what it CARRIES) and the two share a precondition, so they should be
sequenced together once a field exists.

## MECH-537 -- communication-subspace routing failure

**NON-DEGENERACY PRECONDITION.** A locus where an external probe succeeds on the full sender latent
and native behaviour fails, on a source measured to contain the content (`rawfield25`; trained
`z_world` excluded by V3-EXQ-1010), with MECH-517 (decoder collapse) and MECH-532 (missing
decompression stage) independently excluded -- routing failure requires neither.

**CONFIRMING.** Cross-validated RRR from sender activity to the ACTUAL consumer input tensor shows
task decodability in the full sender latent that is materially absent from the selected-rank
consumer-facing subspace, with mismatched / zero / moment-matched-random controls per INV-105.

**FALSIFYING.** The consumer-facing subspace carries the distinction as well as the full latent, so
the null is a consumer or downstream-valuation problem, not an exposure problem.

**DISPOSITION: (a) testable now.** **CURRENCY CORRECTION for digestion:** MECH-537 has been treated
as instrument-blocked since registration, and that is **no longer true** -- the RRR estimator, the
principal-angle metric, the bridge ladder, the causal-replacement harness and the manifold guard all
landed in `ree-v3 experiments/_lib/interface_probe.py` (commit `a83f2fb`, 2026-09-10, on
`origin/main`). The 2026-09-10 assay spec's section 0.2 ("the instrument does not exist") predates
that commit by fourteen hours and should be annotated.

## MECH-540 -- sleep as selective interface maintenance

**NON-DEGENERACY PRECONDITION.** At least TWO interfaces with *different predicted plasticity* (the
claim's own design requirement -- the strongest test compares two interfaces, not whether all systems
become more similar), plus a sleep cycle whose replay content reaches a consumer. The latter is now
**partially satisfied**: the MECH-285 sampler's draws are consumed through the MECH-272 routing gate
into the Bayesian aggregator, the self-model aggregator and the SWS anchor weight
(`phase_manager.py:435-525`) -- note that `replay_sampler.py`'s "Phase B is a NO-OP CONSUMER"
docstring is **stale** and should not be cited as evidence of a gap. MECH-092's `_do_replay` still
has no consumer.

**CONFIRMING.** Post-sleep, at least two interfaces show *divergent* change -- one reconfigured, one
held stable -- with the direction predicted in advance from which had recent learning pressure, and
the change is in the interface (subspace / bridge complexity) rather than only in the endpoint
representations.

**FALSIFYING.** All interfaces move together (global alignment), or none moves while endpoint
representations do (S1 only) -- in either case there is no third offline job, only MECH-529's two.

**DISPOSITION: (a) testable now for the static signatures S1-S4** (the instrument exists; `ree-v3
de26949aa` `force_sleep_cycle_at_eval_boundary` makes the sleep assay cheap -- **which the 2026-09-07
intake explicitly names as the trap**, since sequencing requires a single waking interface metric to
show range and stability first). **Two amendments are pending on this claim and should be decided
together rather than piecemeal:** MECH-548's proposed S5 (static probe improves, next waking
trajectory destabilises) and this pass's NEW-MECH-3 (NOT REGISTERED -- deferred: proposed as MECH-540 signature) (the maintained object includes the access state).

## MECH-547 -- receiver-conditioned translation

**NON-DEGENERACY PRECONDITION.** A locus where the same sender plausibly supports more than one read
surface, and a receiver-state variable with live variance; matched capacity with the unconditional
arm receiving the conditioning input as a constant zero vector of the same width, so the arms differ
in the *information* on that channel and not its dimensionality.

**CONFIRMING.** `T(A,B) > T(A)` on held-out data at matched capacity AND receiver-state permutation
destroys the gain.

**FALSIFYING.** Permutation barely matters -- the gain is extra capacity, and the result is evidence
about the bridge (MECH-538), not about the endpoints.

**DISPOSITION: (a) testable now** (instrument landed). **(g) MERGE-ADJACENT, flagged:** MECH-547's
title already lists "temporal phase" among candidate conditioners, so MECH-561 narrows MECH-547's
disjunction to one conditioner class that belongs to neither endpoint, plus a claim MECH-547 does not
make (geometric/temporal substitution). Digestion should decide whether to keep them separate or fold
MECH-561 in as a MECH-547 amendment. If separate, the shared experiment MUST run the receiver-state
permutation and the phase permutation together, or the result cannot be attributed.

---

# Part C -- disposition summary

| Claim | Disposition | One-sentence justification |
|---|---|---|
| ARC-145 | (f) defer | An architectural commitment should not harden before a single measurement exists beneath it. |
| MECH-560 | **split**: (a) observational / (c) lesion | The observational leg needs only a directed-influence estimator (buildable); the lesion leg needs an inter-engine gain overlay that does not exist. |
| NEW-MECH-2 (NOT REGISTERED -- deferred: propagation) | (c) substrate-blocked, `substrate_conditional` | No routing state and no propagation machinery exist anywhere in `ree-v3`; the mechanism has never been exercised. |
| NEW-MECH-3 (NOT REGISTERED -- deferred: proposed as MECH-540 signature) | (c) substrate-blocked + (g) merge candidate with MECH-540 | No `(sender_episode, receiver_episode)` pairing exists, and MECH-540's signature list is already open for one amendment. |
| MECH-561 | (a) testable now, observationally | Both the estimator and three endogenous phase coordinates exist today; only the causal lesion ladder is blocked. |
| Q-106 | (f) defer | Last stage of the programme; asking it early tests a field nothing has shown to be load-bearing. |
| MECH-534 | (c) substrate-blocked | Code absent; digestion's reduction check must add `VsRolloutGate` and `RoutingGate` to its candidate list. |
| Q-103 | (c) substrate-blocked | Shares MECH-534's precondition; sequence with Q-106. |
| MECH-537 | (a) testable now -- **currency correction** | The instrument landed 2026-09-10; the "instrument-blocked" reading is stale. |
| MECH-540 | (a) testable now for S1-S4, with a sequencing caveat | The cheap sleep hook is the trap the 2026-09-07 intake named; two amendments are pending and should be decided together. |
| MECH-547 | (a) testable now + (g) merge-adjacent to MECH-561 | Instrument landed; the two conditioners overlap and must be permuted in the same experiment. |

**Nothing above excretes a claim.** No duplicate, pun or redundant entry was found in the family that
warranted disposition (e), and no existing claim was found to be superseded by anything here.

## Family D -- hippocampal campaign cluster (registered INV-109, INV-110, MECH-562, Q-107)

# Digestion drafts -- FAMILY D (hippocampal translation-maps campaign)

**Date:** 2026-09-15 | **Session:** thought-pipeline-20260915
**Scope:** (a) the four proposed new claims in `proposed_claims.yaml`; (b) the EIGHT existing claims
this family materially bears on that are `status: candidate` with **no `what_would_answer` field** --
verified absent on all eight.

**This is a SEPARATE ARTIFACT, not part of any intake.** Nothing here is applied.

**Extract-before-invent was applied.** Wherever the raw thoughts or the assay specifications state a
falsifier, it is reused verbatim rather than re-invented, and the source is named. Where a sibling
claim already carries a `what_would_answer` in the same shape (MECH-269, ARC-007, ARC-018, Q-057 all
do), its shape is copied.

**Currency verified for every cited blocker** against `ree-v3` HEAD, `REE_assembly/evidence/`, and
`ree-v3/experiment_queue.json` on 2026-09-15. Two blockers cited in the source documents have RESOLVED
since they were written, and both are marked.

---

## PART A -- the four proposed new claims

### INV-109 -- a reproduced recipe is not a frozen endpoint

- **NON-DEGENERACY PRECONDITION.** At least two runs in the same lineage must claim to measure "the
  same" endpoint, and at least one must have re-derived it rather than loaded it. Degenerate if every
  run persists and loads its endpoints (the invariant is then vacuously satisfied) or if no two runs
  reference a shared endpoint at all.
- **CONFIRMING.** Two runs reproducing one documented recipe under matched seeds, on different machine
  classes or at different times, produce endpoints whose `hash_tensor_state` differs while their
  regime-level readouts agree within the declared band. The prediction is already half-witnessed:
  V3-EXQ-1010 reproduced 1008's recipe and reports matching participation ratios and in-band
  consumer-width values alongside differing example weight deltas (seed 42: 0.2929618 vs 0.2930078)
  and `substrate_stable_across_run: false`. What is missing is a direct hash comparison, which nothing
  in that lineage recorded.
- **FALSIFYING.** Recipe reproduction under a pinned substrate commit yields bit-identical endpoint
  weights across machine classes and repeated runs -- i.e. the commit pin already delivers endpoint
  identity and the distinction has no operational content. **Note this is a live possibility and worth
  the cheap test**: `[memory] reference-cross-machine-class-contract-divergence` records that
  `rand`/`randint`/`randperm`/`bernoulli` ARE bit-identical across `darwin-arm64` and `linux-x86_64`,
  and only `torch.multinomial` diverges. If the encoder path touches no multinomial, the endpoints may
  be closer than the invariant assumes.
- **DISPOSITION: (a) testable now on V3 substrate.** The test is `hash_tensor_state` on two reproductions
  of one recipe -- minutes of work with the instrument that already exists at
  `ree-v3/experiments/_lib/interface_probe.py:119`. Justification: a universal evidential invariant does
  not normally get a falsification experiment, but this one makes an empirical prediction about the
  substrate that is cheap to check and would materially narrow it.

### INV-110 -- the interface-repair adjudication standard

- **NON-DEGENERACY PRECONDITION.** A maintenance/repair claim must exist that the standard could
  refuse. Degenerate if no REE experiment has yet attempted a repair claim -- which is the case today,
  so the standard is currently prospective and cannot be exercised.
- **CONFIRMING.** The standard earns its keep the way INV-105 did: a REE result is produced that would
  have been read as interface repair, and applying the six links plus the `D > max(E,F,G)` estimand
  changes the reading. Concretely: an assay B run in which `D > B` (correct pairing beats no
  maintenance) but `D` does not exceed arm F (receiver-local self-healing) or arm G (local rehearsal),
  and the standard converts what would have been reported as repair into "access maintained by local
  adaptation; pair-specific replay not necessary."
- **FALSIFYING.** The standard's central empirical premise is that the four outcomes are genuinely
  confounded in practice. It is falsified if arms E, F and G are shown to be reliably separable by a
  cheaper signature than the full six-link design -- for instance if local-memory equivalence turns out
  to hold automatically whenever drift is confined to the receiver-potent subspace, making prospective
  titration unnecessary. It would also be falsified as OVER-BROAD if Gate 0 proves unreachable in
  practice: if no drift model can be found that degrades `U` while leaving both endpoints locally
  intact AND is restored by a known oracle inverse, the standard forbids every possible experiment,
  which is a defect in the standard rather than a finding about the world.
- **DISPOSITION: (b) derivational, shading to (f) defer.** It is an interpretive standard and should
  not be given a falsification experiment (same treatment as INV-105, whose own notes say so). Its
  exercise is a governance decision about whether to make it a pre-registration gate. **Defer the
  gate decision until one assay B design is actually staged**, so the over-broad risk above can be
  judged against a real design rather than in the abstract.
- **Open governance question, flagged rather than resolved:** should this be a second consequence-set
  on INV-105 instead of a standalone invariant? The governing precedent is the 2026-09-10 GFLAG-0235
  ruling on MECH-548's eighth rung, which chose **forward reference over amendment** on the stated
  ground that a testable mechanism's specific framing should not be baked into a definitional
  universal invariant. That reasoning applies here in reverse -- this IS definitional -- so it argues
  for standing alone rather than amending. Recorded, not decided.

### MECH-562 -- receiver-local self-healing as the standing rival

- **NON-DEGENERACY PRECONDITION.** The sender representation must actually drift in directions the
  receiver reads, and the receiver must have plasticity enabled at its afferents. Degenerate under
  either of two conditions, both live in REE today: (i) drift confined to the receiver-null subspace,
  where a fixed readout works and no adaptation is exercised; (ii) a frozen consumer -- and **every
  adapter in the 978->1023 lineage is fitted-then-frozen**, so on that lineage this mechanism has never
  been exercised even once.
- **CONFIRMING.** A receiver running only the label-free local rule -- presynaptic sender activity,
  its own postsynaptic output, homeostatic error against fixed pre-drift output mean and variance,
  error-gated decay -- recovers held-out receiver-dependent use after a verified interface lesion, at a
  matched update budget, with no episodic pair identity available to it. Stronger: the recovery tracks
  the drift-rate-to-maintenance-interval ratio as predicted, degrading when maintenance is made
  infrequent relative to drift.
- **FALSIFYING.** The local rule fails to recover use under conditions its own preconditions declare
  favourable -- smooth redundant tuning, incremental drift, plasticity faster than drift, ample
  sampling -- while a correctly-paired arm at the same update budget recovers. That is simultaneously
  the confirming result for MECH-540's interface-repair reading, which is why the two claims must be
  run as arms of one design and not separately.
- **DISPOSITION: (c) substrate-blocked, subtype `substrate_conditional`.** The code is absent: `grep`
  over `ree_core/` finds no readout-adaptation rule of this shape, and `interface_probe` is pure and
  stateless by design so it cannot host one. Zero non-degenerate attempts are possible today. This is
  the **correct** subtype and not `substrate_ceiling`: nothing has been exercised and no evidence has
  been banked either way.
- **Build note, because it changes the cost estimate:** arm F is specified to implementation level
  already, in the supplement's section 6.4 (six numbered implementation points) and in the assay
  specification's section 3.3. It is `complicated (buildable)` at the EXPERIMENT layer -- the assay
  spec's section 4.4 forbids putting it in `ree_core`.

### Q-107 -- code change versus world change

- **NON-DEGENERACY PRECONDITION.** A maintenance mechanism must exist whose behaviour could differ
  between the two cases. Degenerate if no REE component adapts to upstream change at all -- currently
  true, which is why this is deferred rather than testable.
- **CONFIRMING** (that the ambiguity is real and consequential in REE): run identical maintenance arms
  under two conditions constructed to be indistinguishable from the receiver's vantage -- a pure code
  rotation with the task unchanged, and a genuine task change of matched magnitude at the sender --
  and find that no REE mechanism behaves differently. The consequence is then that every REE
  maintenance claim must state an external anchor in its design.
- **FALSIFYING.** Some REE mechanism *does* distinguish them without an externally supplied label --
  for instance because a residual prediction error, a provenance tag, or a `z_goal`-side signal
  carries the information implicitly. That would be a substantive positive finding about REE's
  architecture, not merely a null.
- **DISPOSITION: (f) defer, with a named trigger.** The discriminating manipulation requires the
  controlled-drift INTERVENTION that does not exist (`per_code_drift` at
  `ree-v3/experiments/_lib/interface_probe.py:1012` measures; nothing imposes). **Trigger: revisit when
  either MECH-562's arm F or assay B's Gate 0 drift instrument is built** -- at that point the test
  is nearly free, because both already construct a known code rotation, and the only addition is a
  matched-magnitude genuine task change.
- Set `epistemic_category: substrate_conditional` explicitly so `narrow_open_question` does not fire.

---

## PART B -- the eight existing claims with NO `what_would_answer`

All eight are `status: candidate`, all registered 2026-09-08, all carry "DO NOT queue an experiment
from this entry", and **`what_would_answer` is absent on every one** (verified individually). The
combination -- no falsification handle plus a standing do-not-queue -- means the family currently has
no registered way to be wrong. Drafting these does not lift the do-not-queue: a `what_would_answer`
says what WOULD answer the claim, and the sequencing in each claim's own notes still governs when.

Two shared preconditions bind all eight and are stated once rather than repeated:

- **P-COMMON-1 (endpoint identity).** Both endpoints frozen, loaded from persisted weights, hashed at
  every evaluation boundary (INV-109). Not satisfiable today for a sender/consumer PAIR -- the
  pieces exist (`interface_probe.hash_tensor_state:119`; `probe_warmup.AgentSurface:254`,
  `capture_agent_surface:367`, `restore_agent_surface:395`) but their composition does not.
- **P-COMMON-2 (adequate source).** The sender must carry the content. **This precondition has
  RESOLVED since these claims were registered, and resolved against the obvious source.** V3-EXQ-1010
  confirmed H-F at the user gate 2026-09-11: the trained `z_world` is not an admissible source. The
  two measured-adequate replacements are `rawfield25` (0.9735 worst-seed held-out oracle agreement)
  and `ws250_pca32` (0.868 mean, 3/3 above bar). Any `what_would_answer` on these eight that named
  `z_world` as the sender would have been stale on arrival; none do, because none exists.

### ARC-139 -- selective mutual legibility without representational convergence

- **NON-DEGENERACY.** At least two REE subsystems must be separately competent and separately
  measurable, with an identifiable narrow interface between them. Degenerate if one subsystem's local
  competence is at floor -- an incompetent endpoint makes both axes uninformative.
- **CONFIRMING.** Across a developmental sweep, local competence rises in E1/E2/hippocampus/E3 **while
  global representational similarity between them stays flat or falls**, and cross-system legibility
  (falling `L(A->B)` at fixed held-out criterion) rises over the same interval. The divergence of the
  two axes is the whole content; either alone is uninformative.
- **FALSIFYING.** Rising local competence is accompanied by rising global similarity, i.e. maturation
  IS convergence -- which is ARC-121's reading, deliberately kept alive as the rival. Or: `L(A->B)`
  falls only because one subsystem lost its specialisation, which the two-axis guard (MECH-538) is
  designed to catch and which would falsify the "at the same time" clause specifically.
- **DISPOSITION: (c) substrate-blocked (`substrate_conditional`)**, and the blocker is now named
  precisely: no measurement of `L` exists at any REE interface. **Partially resolved since
  registration** -- the ladder itself now exists (`interface_probe.bridge_ladder:629`), so this has
  moved from "no instrument" to "instrument built, never run at a live locus". The work programme's
  ML-20 names the first locus.

### MECH-537 -- communication-subspace routing failure

- **NON-DEGENERACY.** The target variable must be decodable from the FULL sender at above the
  random-projection floor (INV-105 consequence 2), and the consumer-facing subspace must be estimable
  at a stable rank. Degenerate if the target is not in the sender at all -- **and that is the live
  case for `z_world`**, per H-F.
- **CONFIRMING.** The registered signature verbatim: `target decodable from X` but `poorly decodable
  from P_comm X`, where `P_comm` is the cross-validated RRR projection onto the actual consumer input
  tensor -- with the complement projection carrying the distinction. And, discriminating it from
  MECH-517: the consumer's readout is NOT rank-deficient or collapsed.
- **FALSIFYING.** Task decodability inside the estimated communication subspace matches decodability
  in the full sender, i.e. nothing is being withheld by routing; or the phenotype is fully explained
  by a collapsing decoder (MECH-517) or a missing decompression stage (MECH-532). The registered
  discriminator is failure class F2 vs F3 on the location doc.
- **DISPOSITION: (c) substrate-blocked, and RE-ROUTED by new evidence.** It is
  `implementation_phase: v3` and its instrument now exists
  (`interface_probe.communication_subspace:361`), so it is closer to testable than any other claim in
  the family. **But its motivating locus is gone**: H-F says the content is not in the trained
  `z_world` to be withheld. The claim survives -- routing failure remains a real third category -- and
  needs a NEW locus. Candidates from its own `depends_on`: SD-080's frozen action-object projection,
  which is `pending_implementation` in `substrate_queue.json` and whose `unblocks_claims` list
  **omits MECH-537** (a currency fix in its own right).
- **Recommended disposition to `/governance`: re-word the notes, do not demote.**

### MECH-538 -- minimum bridge complexity as the legibility measure

- **NON-DEGENERACY.** The ladder must span a real range on the locus: the high-capacity rung must
  succeed (so the criterion is reachable) and the native rung must fail (so there is something to
  measure). If L0 already clears the criterion, `L` is 0 and the quantity is uninformative.
- **CONFIRMING.** `L(A->B)` is measurable and stable across seeds at one locus, AND its developmental
  prediction holds: sender and receiver each improve local competence while global similarity stays
  flat or falls, task information concentrates in the consumer-facing subspace, and minimum bridge
  rank falls.
- **FALSIFYING.** `L` does not fall across development in ANY arm -- which the assay C specification
  already names as its falsifier F7 and flags as the **cheap check that can void the rest**. Or `L`
  is unstable across seeds at a fixed developmental point, in which case it is not a measure.
- **DISPOSITION: (c) substrate-blocked -> now (a) testable at instrument level, (f) deferred at claim
  level.** The ladder exists and its self-test passes (5 cells, 0.071 s). The developmental prediction
  needs a developmental substrate that does not exist. **Sequencing from the claim's own notes binds:
  ML-20 then ML-50 -- a developmental sweep on an unvalidated instrument measures the instrument.**

### MECH-539 -- dynamic interface compatibility

- **NON-DEGENERACY.** The receiver must have non-trivial action-conditioned transition structure to
  destroy. Degenerate if the receiver's transitions are near-identity or if cross-candidate divergence
  at the source is ~0 -- the latter is a measured REE failure mode (`cand_world_pairwise_dist` = 0.0 at
  V3-EXQ-571, recorded in MECH-033's own notes).
- **CONFIRMING.** A bridge with good pointwise fit shows `receiver_transition(T(x_t), a_t)`
  incompatible with `T(x_{t+1})`, and the registered separation reproduces: map-initial-only succeeds
  while re-map-each-step degrades, or vice versa.
- **FALSIFYING.** Pointwise-good bridges are also dynamically compatible at every locus tested, i.e.
  the additional criterion never bites and pointwise fit suffices between predictive systems.
- **DISPOSITION: (a) testable now, at instrument level.** `interface_probe.dynamic_compatibility:953`
  implements exactly the registered criterion, one-step and multi-step with a `compounding` flag. The
  remaining gap is a live locus and an adequate source, both now identified.

### MECH-540 -- sleep as selective interface maintenance

- **NON-DEGENERACY.** Two interfaces with DIFFERENT predicted plasticity, both with adequate native
  consumers and both measurable pre/post -- the claim's own two-interface requirement. Degenerate on
  one interface, because a nonspecific plasticity or arousal effect is then invisible.
- **CONFIRMING.** Signature S2 specifically: local competence stable across the sleep boundary while
  the communication subspace or bridge complexity improves -- and improves on the interface predicted
  to be plastic and not on the one predicted to be stable. INV-110's six links apply in full.
- **FALSIFYING, three ways, all registered or newly available.** (i) **S4** -- cross-system similarity
  rises while local competence or task-specific differentiation worsens. The claim's own notes make
  this an explicit FAILURE, not a partial success. (ii) Both interfaces move identically -> nonspecific
  effect. (iii) **MECH-562's arm F matches the sleep arm at a matched update budget** -- receiver-local
  self-healing does the work, and no offline interface maintenance is needed. The supplement's own
  strongest-falsifier formulation is the best available wording and should be reused verbatim.
- **DISPOSITION: (c) substrate-blocked (`substrate_conditional`), with a SEQUENCING gate that is part
  of the claim.** The sleep trigger exists (`ree_core/agent.py:12759
  force_sleep_cycle_at_eval_boundary`) but the pairing does not: `SleepReplaySampler` is a declared
  no-op consumer and `CrossModuleConsolidator` carries no `(sender_episode, receiver_episode)` pairing.
  Additionally `substrate_queue.json`'s `mech092-replay-consumer-missing` records that replay
  trajectories are computed and DISCARDED with no consumer anywhere in `ree_core`. And the claim's own
  sequencing forbids a sleep assay before a waking interface metric shows range and stability.
- **Note addition proposed** (not applied): cite the 2026-09-09 supplement in MECH-540's
  evidence-status paragraph -- it is the systematic version of the honest sentence already there.

### INV-105 -- the latent-access evidence ladder

- **NON-DEGENERACY.** n/a in the usual sense. It is a definitional universal invariant and its own
  notes say it "should not be given a falsification experiment".
- **CONFIRMING** (that it does work, which is the only admissible evidence for a standard):
  documented instances where applying the ladder changed a reading that would otherwise have been made.
  **One such instance now exists and should be recorded**: the 2026-09-10 EXQ-1010 readiness audit
  applied rungs 1-2 to refuse the manifest's "DESTROYED AT ENCODE TIME" paraphrase as established
  science, substituting "finite-ladder non-recovery on a reproduced OFF regime". That is INV-105 doing
  its job on a live run.
- **FALSIFYING** (as a standard, not as a fact): the two binding consequences prove unnecessary in
  practice -- e.g. the zero floor and the dimensionality-matched random-projection floor never differ
  materially on real REE nulls, making consequence (2) ceremonial. Cheap to check retrospectively
  across banked manifests.
- **DISPOSITION: (b) derivational.** Convert to a pre-registration gate or leave as an interpretive
  standard; `/governance` owns it, as the claim itself says. The `what_would_answer` should record the
  ladder-did-work instance rather than propose an experiment.

### MECH-547 -- receiver-conditioned translation

- **NON-DEGENERACY.** Matched capacity between `T(A)` and `T(A,B)` must be genuinely enforced and
  reported, and the receiver state must carry information the sender does not. Degenerate if `T(A,B)`
  has more parameters -- the gain is then capacity, which is the exact confound the claim names.
- **CONFIRMING.** The registered signature verbatim: `T(A,B) > T(A)` on held-out data at MATCHED
  capacity, **and** receiver-state permutation destroys the gain. Plus the exposure-not-solving
  constraint: the bridge must be shown to expose existing sender content rather than learn the task,
  which requires the sender-only matched-capacity baseline and INV-105's correct/mismatched controls.
- **FALSIFYING.** Receiver permutation barely matters -> the gain is extra capacity, and the result is
  evidence about the bridge (MECH-538), not about conditioning. Or a receiver-only predictor accounts
  for the gain -> the receiver supplied the information and the sender never had it, which the campaign
  adjudication flags as the interpretive trap ("a receiver-conditioned bridge can recover performance
  by introducing missing information from the receiver ... does **not** prove the sender retained it").
- **DISPOSITION: (c) substrate-blocked (`substrate_conditional`), and this is the family's SHARPEST
  instrument gap.** `interface_probe.bridge_ladder:629` fits `X -> Y` unconditionally across L0-L5;
  **there is no receiver-conditioned rung.** The work programme's ML-13 addendum ("Added 2026-09-08",
  the `T(A,B)` rung with mandatory `T(A)`, `T(A,B_perm)` and ML-14 arms) is the one ML-13 item the
  2026-09-10 P0 build did not deliver. Until it lands, MECH-547 has no instrument and assay A can run
  every arm except the discriminating one. `complicated (buildable)`.

### MECH-548 -- recurrent interface stability

- **NON-DEGENERACY.** The interface must be traversed repeatedly over a horizon the system actually
  uses, and the one-step result must be positive -- there is nothing to destabilise otherwise.
  Degenerate if one-step utility is at or below floor.
- **CONFIRMING.** The registered signature verbatim: **one-step rescue + cumulative collapse +
  clean-base stability**. Recomputing each step against the unmodified native receiver state restores
  stability while cumulative application degrades -- which is simultaneously the separating arm against
  MECH-539 (dynamics incompatibility), since MECH-539's failure persists under clean-base and
  MECH-548's does not.
- **FALSIFYING.** Cumulative and clean-base application are indistinguishable over the horizons the
  system uses, i.e. the bridge's own output re-entering as input costs nothing. Or the degradation is
  fully explained by native-dynamics incompatibility (MECH-539) and clean-base does not rescue it.
- **DISPOSITION: (c) substrate-blocked -> PARTIAL.** `manifold_guard:847` covers the off-manifold half
  (mechanism (a)). **The cumulative-re-application half is NOT built**: `dynamic_compatibility:953`
  measures compounding across ONE rollout, not `N` re-applications of `T`; no `cumulative_drift` /
  `repeated_use` / `recurrent_interface` symbol exists anywhere in `ree-v3`. The assay specification's
  section 1.8 specifies exactly what is needed (N=20 consecutive closed-loop consumer steps, agreement
  at step 1 and step N, fitted decay slope, first-crossing index) and defines the reporting category
  **one-step-only, never a rescue**. `complicated (buildable)`.
- **Also unresolved and already ruled on:** the eighth-rung proposal (`recurrently stable`) stays on
  MECH-548 rather than amending INV-105, per the 2026-09-10 GFLAG-0235 ruling, **revisit when MECH-548
  acquires evidence**. That is a live trigger, not a closed item.

---

## PART C -- merge proposals and excretions

**None of either.** Checked explicitly, because an archaeology pass is exactly where duplicates
surface:

- **ARC-139 vs ARC-121** (federation vs shared epistemic-state object) -- **DO NOT MERGE.** Both
  claims' own notes keep the other alive deliberately as a rival reading of the same convergence
  evidence, and ARC-139's notes say ARC-121 "must not be used to prejudge the question".
- **MECH-539 vs MECH-548** -- **DO NOT MERGE.** Both produce "good one-step + degrading long-horizon"
  and MECH-548's notes distinguish them at length: MECH-539 is incompatibility with the receiver's
  native dynamics; MECH-548 is the bridge's own output re-entering as its own input. The separating arm
  is clean-base translation. A future session merging them would lose a real distinction, and both
  claims say so.
- **MECH-539 / MECH-548 vs INV-088** -- **DO NOT MERGE.** INV-088 is E1's own multi-step fidelity; both
  MECH claims are about a mapping BETWEEN systems. Stated on both.
- **INV-110 vs ARC-137** -- **DO NOT MERGE.** ARC-137 partitions offline work by OUTCOME; INV-110
  partitions by CONFOUND. Distinguished in INV-110's `depends_on`.
- **Q-107 vs GOV-EQUIV-1** -- **DO NOT MERGE.** GOV-EQUIV-1 binds SESSIONS and presupposes an outside
  adjudicator; Q-107 asks whether the ORGANISM can do it with none.
- **MECH-562 vs MECH-120** -- **DO NOT MERGE.** MECH-120 is nightly synaptic homeostatic
  down-scaling, a magnitude operation on a different timescale; MECH-562 is correspondence-tracking
  at a readout.
- **The two archaeologies** (`..._translation_interface_archaeology.md` and
  `..._translation_maps_ree_archaeology.md`) -- **RECOMMEND RETAIN BOTH, cross-link, do not merge.**
  Full reasoning in
  `thought_intake_2026-09-09_hippocampal_translation_interface_archaeology.md` section 4a. This is a
  document-level judgement call for `/governance`, not a claim-level merge.

---

## PART D -- currency corrections found while drafting

Every blocker cited by the five raw thoughts was re-checked. Five have changed state; **all five make
the claims LESS blocked, not more**, which is why drafting these falsifiers is worth doing now.

| Cited blocker | State on 2026-09-15 |
|---|---|
| "No communication-subspace estimator, bridge ladder, principal-angle metric, causal-replacement harness, receiver-manifold guard or dynamic-compatibility scorer exists in `ree-v3`" | **RESOLVED 2026-09-10**, `ree-v3` `a83f2fb` -- `experiments/_lib/interface_probe.py` (1,202 lines) plus `stats.tost_equivalence`, with contract tests at `tests/contracts/test_interface_probe.py` |
| "No equivalence test exists anywhere in `experiments/`" | **RESOLVED**, same commit -- `experiments/_lib/stats.py:202 tost_equivalence` |
| "The governance registry still records H-F as `alive`, with no evidence runs" | **RESOLVED 2026-09-11** -- `hypothesis_space_registry.v1.json` now `state: confirmed`, `resolving_runs: [V3-EXQ-1010]`, synthesis refreshed. **BUT the `decision` block in the same object still reads "(H-F, ALIVE)" and "NOT YET QUEUED"** -- stale relative to its own leg state. A currency fix for `/governance` |
| "1010 is not yet queued" / the encoder-objective branch is hypothetical | **RESOLVED** -- 1010 ran, was autopsied CONFIRMED 2026-09-11; **SD-106** landed `ree-v3` `616e713`; **V3-EXQ-1023** ran 2026-09-12 and was autopsied CONFIRMED at the `/governance` gate 2026-09-15 (weakened partial: 0/3 clear the 0.85 bar, but ON beats paired OFF on 3/3 by +0.037 to +0.072) |
| Assay C's G-LIFE gate "unowned" (readiness investigation section 19 item 1) | **RESOLVED and decided AGAINST the branch assay C needs**, 2026-08-12 -- and the readiness investigation still reads as though it is unowned. The assay C spec records this as its own debt 7 |
| **NOT resolved, and the family's one live methodological debt** | The EXQ-1010 audit's section 2.4 objection -- all three half-to-full sample deltas are POSITIVE and the sub-split is by ROWS not EPISODES -- was **not adopted** into the confirmed H-F basis, which reads the same three numbers as reassurance. Its named remedy (refit `mlp512` on nested WHOLE-EPISODE subsets) was **never offered at the Step 8 gate**. See `thought_intake_2026-09-09_exq1010_substrate_readiness_audit.md` section 7.3 row C3 |
