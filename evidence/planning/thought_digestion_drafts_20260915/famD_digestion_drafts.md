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

### NEW-INV-1 -- a reproduced recipe is not a frozen endpoint

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

### NEW-INV-2 -- the interface-repair adjudication standard

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

### NEW-MECH-1 -- receiver-local self-healing as the standing rival

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

### NEW-Q-1 -- code change versus world change

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
  either NEW-MECH-1's arm F or assay B's Gate 0 drift instrument is built** -- at that point the test
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
  every evaluation boundary (NEW-INV-1). Not satisfiable today for a sender/consumer PAIR -- the
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
  to be plastic and not on the one predicted to be stable. NEW-INV-2's six links apply in full.
- **FALSIFYING, three ways, all registered or newly available.** (i) **S4** -- cross-system similarity
  rises while local competence or task-specific differentiation worsens. The claim's own notes make
  this an explicit FAILURE, not a partial success. (ii) Both interfaces move identically -> nonspecific
  effect. (iii) **NEW-MECH-1's arm F matches the sleep arm at a matched update budget** -- receiver-local
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
- **NEW-INV-2 vs ARC-137** -- **DO NOT MERGE.** ARC-137 partitions offline work by OUTCOME; NEW-INV-2
  partitions by CONFOUND. Distinguished in NEW-INV-2's `depends_on`.
- **NEW-Q-1 vs GOV-EQUIV-1** -- **DO NOT MERGE.** GOV-EQUIV-1 binds SESSIONS and presupposes an outside
  adjudicator; NEW-Q-1 asks whether the ORGANISM can do it with none.
- **NEW-MECH-1 vs MECH-120** -- **DO NOT MERGE.** MECH-120 is nightly synaptic homeostatic
  down-scaling, a magnitude operation on a different timescale; NEW-MECH-1 is correspondence-tracking
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
