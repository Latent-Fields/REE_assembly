# Thought Intake: Decision-Useful Counterfactual World Models Under Uncertainty

**Date:** 2026-09-03
**Raw thought file:** `docs/thoughts/2026-09-02_decision_useful_counterfactual_world_models_under_uncertainty.md`
**Session:** thought-routing-20260903

**Intake verdict in one line:** three substantive threads, all three already owned in REE coordinates
(SD-056/ARC-002/MECH-033; the MECH-059/SD-063/MECH-385/MECH-510 uncertainty cluster; ARC-130/ARC-131);
**one** genuinely new *measurable* (uncertainty change across rollout horizon absent new evidence), routed
as a proposed `IMPL-022` contract-field addition rather than a claim; **one** genuinely open question
(imagined-trajectory behavioural-access repair under MECH-094 provenance), registered as `Q-102`.
Total new claims this pass: **one**.

## Verbatim prompt (core proposal)

> What must REE preserve about possible futures for action selection to remain causally sensitive,
> uncertainty-aware, and behaviourally effective?

> **Does the organism carry the action-relevant differences and residual uncertainty in its predictive
> state far enough through proposal, comparison, selection, commitment, and enactment to change what it
> actually does?**

The thought reads three 2026 preprints (Chen/Wang/Li *Counterfactual Quotient Models*; Radha/Goktas
*UWM-JEPA*; Nijjer *Dream Rehearsal for Continual Model-Based RL*) and proposes distinguishing three
predictive objects inside REE's existing typed architecture rather than adding a world-model module: an
**absolute predictive context** (what the world is likely to do), a **counterfactual action-effect
representation** (what candidate actions change relative to one another), and a **belief structure**
preserving unresolved alternatives while either is projected forward. It is explicit throughout that this
"does not presently justify a new module," that the three papers' evidential role is "mechanism generation,
boundary sharpening, and experiment design -- not validation of REE," and that "no claim should be
registered or promoted until the novelty and conflict audit is completed."

Per `feedback_lit_exp_decoupled`, this intake treats all three preprints as literature corroboration only.
None of them is substrate evidence, and no existing claim's status, confidence, or evidence record is
touched by this pass. All three are **unverified preprints, not independently checked in this pass** -- a
separate `/lit-pull` agent verifies them (see Next steps).

## What's new vs. existing REE docs/claims (novelty table)

| Thread in the raw thought | Existing REE coverage (claim id + what it already says) | Verdict |
|---|---|---|
| Typed ownership split -- E1 persistent absolute context, E2 short-horizon action-conditioned kernel, hippocampus chains, E3 selects but does not generate, control plane grants authority | **ARC-001** (E1 persistent predictive substrate), **ARC-002** (E2 fast forward predictor of affordances), **ARC-018** (hippocampus generates explicit rollouts + viability mapping), **MECH-033** (E2 kernels seed hippocampal rollouts), **ARC-005** (control-plane precision routing), **ARC-004**. The thought restates this split accurately and says so itself. | **Already owned.** The thought's own "Existing REE ownership boundaries must remain intact" section is a correct summary of the registry, not an addition to it. |
| Centred action-effect / counterfactual "quotient" as a decision-facing derived view alongside absolute prediction | **SD-056** is this problem already stated in REE coordinates: it was born from the V3-EXQ-571 root-cause finding that with `world_dim=32`/`action_dim=4` "reconstruction-shaped training collapses to the state-dominated local minimum where **action effect is fitted to zero**" (`cand_world_pairwise_dist = 0.0000` across K=8 candidates differing only in first action), and its fix is an auxiliary InfoNCE-style contrastive loss that *preserves action-conditional divergence* in `E2.world_forward`. **ARC-002**'s own `what_would_answer` already names `cand_world_pairwise_dist` / `world_forward_contrastive_loss` as a confirming signature. **MECH-033** owns the E2->hippocampus kernel handoff the derived view would ride. **IMPL-022** (JEPA contract) already requires the metric `action_conditioned_delta_error`. | **Already owned -- SD-056/ARC-002/MECH-033 refinement, not a new engine.** The CQM framing supplies vocabulary ("quotient", "signed successor measure with zero total mass", "decision-equivalent up to a shared component") and an external precedent for a *lever* REE already chose on other grounds. See `refinements_proposed.md`. |
| "Predict the action effect directly rather than predict several absolute futures and subtract them after approximation" (change of learned target) | **SD-056** already changes the training *objective* rather than post-hoc subtracting; its own notes already record two rejected alternative levers (PLSM-style MI factorisation = lever A; SWIRL-style MI maximisation = lever C) with lever B (contrastive next-state) chosen 2026-05-28. A direct signed-successor-measure regression target is a **fourth** lever of the same family, not registered anywhere. | **Adjacent but too thin to register.** Folded into the SD-056 `notes` addendum as a named alternative lever alongside A/C, so a future `/implement-substrate` sees it without a claim that asserts it works. |
| Derive-at-comparison-time vs learn-directly: `effect(s,a) = future_features(s,a) - sum_b rho(b|s) future_features(s,b)` | **SD-003 (SUPERSEDED)** is the derive-at-comparison-time form, already tried and retired: `causal_signature = E2(z_t, a_actual) - E2(z_t, a_counterfactual)`. Superseded 2026-04-18 by **MECH-256** (general single-pass forward-model comparator) + **SD-029**, after 28 FAILs and a 14-entry literature synthesis found the single-pass comparator (Frith 2000, Shergill 2003, Blakemore 1998) to be the biologically-evidenced mechanism. | **Already owned, with a decided history the thought does not know about.** Important boundary: SD-003's retirement was scoped to **self-attribution**, on biological-precedent grounds -- it is *not* a verdict against a centred action-effect view for **decision comparison**, which is a different consumer. Recorded so a future session neither resurrects SD-003 nor mistakes its supersession for a general refutation. |
| "Synchronized counterfactual branches with common random numbers are privileged supervision -- treat as oracle/ceiling, not endogenous competence" | **GOV-INTERVENE-1** (oracle/non-oracle x silky/oddly-composed intervention taxonomy) and **GOV-PATHVALID-1** (a positive control that injects the state downstream of a suspected causal edge certifies the *consumer*, never that the *production organism* reaches that state endogenously) are exactly this doctrine, already registered. **INV-103** (non-oracular evidence ingestion). **SD-013** already carries the Scholkopf-2021 observational-vs-interventional training requirement for the attribution pipeline. | **Already owned -- and REE's coverage is sharper than the thought's.** The thought's caution is correct and needs no new claim; it should cite GOV-PATHVALID-1/GOV-INTERVENE-1 by name. |
| Uncertainty must not silently collapse into a point estimate under partial observability; a belief structure carries unresolved modes forward | **INV-025** (irreducible uncertainty is structural, not engineerable away), **MECH-059** ACTIVE (confidence channel must remain distinct from residual error -- this *is* the thought's "does confidence have declared provenance rather than being an alias for residual magnitude" check, already an active claim), **SD-063** PROVISIONAL/v3 (E2 world-forward carries a conditional predictive-uncertainty head in distribution-free quantile form, because E3's running-variance EMA has near-zero per-point error correlation), **MECH-385 / ARC-091** v4 (bounded belief-state hypothesis set; "E3 evaluates candidate trajectories over the hypothesis set rather than over a single collapsed state"), **MECH-510** (generative vs error precision), **IMPL-022** (`latent_uncertainty_calibration_error`, `latent_rollout_consistency_rate`, `uncertainty_estimator` knob with `dispersion`/`ensemble`/`head`, and a required *uncertainty provenance check*). | **Already owned across the cluster.** Every individual check the thought's REE-interpretation section lists maps onto a live claim or an existing contract requirement. |
| The specific measurable: **change in uncertainty across rollout horizon in the absence of new evidence** | Searched: zero registry hits for "blind rollout", "absent new evidence", any uncertainty-monotonicity-over-horizon formulation. The nearest, **MECH-231**, is about predictive *accuracy* degrading with horizon, not about the predictor's own uncertainty estimate failing to widen. `latent_rollout_consistency_rate` measures rollout self-consistency, not uncertainty dissipation; `latent_uncertainty_calibration_error` measures calibration at a point, not its trajectory across a blind horizon. | **Genuinely new -- but as a METRIC, not a claim.** Routed as a proposed `IMPL-022` contract-field addition (diff snippet below), not registered as a MECH. Registering a mechanism claim here would assert a substrate proposal the thought does not make; the thought says only that the check should exist. Flagged for `/governance` if it disagrees. |
| Density-matrix / unitary-dynamics latent parameterisation | The thought itself: "The density-matrix implementation should not be imported merely because it preserves a mathematical invariant" and "The density-matrix construction has no privileged status." | **Correctly left unclaimed by the thought.** Not registered. |
| Teacher forcing lets the learned action term collapse while training loss stays low; counterfactual targets restore action sensitivity | This is a *training-protocol* diagnosis of the same failure **SD-056** already owns (action effect fitted to zero at low reconstruction loss). SD-056's registered diagnosis is dimensional/objective-shaped (action is ~11% of `world_forward` input dimensionality); the teacher-forcing account is a second, independent route to the same collapse and is not recorded anywhere. | **Already owned as the failure; adjacent as the mechanism.** Folded into the SD-056 `notes` addendum as a second candidate route to the same collapse, plus a concrete negative control (does the action term survive when the target encoder has not seen the future). No new claim. |
| Three-way validation: representation quality, decision usefulness, and behavioural reach measured separately in the same experiment | **ARC-130** (8-stage causal-reach ladder: existence, representation, endogenous recruitment, local operation, competitive authority, committed throughput, ecological consequence, retention/generalisation -- "the furthest stage actually demonstrated ... is the correct unit"), **ARC-131** (installability as a competence dissociable from component-level validation), **ARC-120** (competence before authority), **GOV-FAILLOC-1**. The thought's own chain (`representation -> endogenous recruitment -> local prediction/proposal -> competitive authority -> selection -> fresh commitment -> execution -> ecological consequence -> retention/generalisation`) is ARC-130's ladder, reached independently and stated almost stage-for-stage. | **Already owned -- an ARC-130/ARC-131 APPLICATION, not a claim.** Independent convergence is worth recording in ARC-130's notes; it is not new content. |
| "Retained representation is not retained behavioural competence" (the Nijjer component-level dissociation) | **ARC-130/ARC-131** as above. Also **MECH-476 (RETIRED)**: REE's own general acquisition-vs-retention claim was retired after its falsifier (V3-EXQ-836a/d/e) found retention invariant to dose/interval/novelty and explained by **MECH-459**'s return-scale-invariance normaliser rather than a dedicated consolidation process. | **Already owned -- with a standing caution.** The external preprint must NOT be used to resurrect MECH-476: it is a component-level dissociation *within one replay-maintained Dreamer regime at 17M parameters and three seeds*, which the paper itself scopes narrowly. Recorded in the ARC-130/131 refinement. |
| Dream self-imitation / offline rehearsal to repair behavioural access, in tension with simulation-write governance | **MECH-094** STABLE (simulation content must not accumulate as committed experience), **INV-011** (imagination without belief update), **INV-019** (rehearsal traversal separated from irreversible durable write), **ARC-020** (offline consolidation protected by typed authority/write boundaries), and critically **MECH-322** -- REE's *existing* narrow carve-out permitting ARC-071 chunk formation from replayed sequences in designated sleep phase, gated on a value-tag from prior real-executed episodes, sleep-phase-only, with a `replay_origin=True` audit flag and accelerated dissolution absent real waking corroboration. | **Strongly adjacent, partly owned -- but the residual question is genuinely open.** MECH-322 is REE's answer-shape for *policy chunk* formation from replay; it does not answer whether *behavioural access / readout / eligibility mappings* can be repaired from **model-generated** (not previously-realized) trajectories. That residue is what `Q-102` registers. |
| Social action effects: "unchanged by me" must not collapse into "irrelevant" (V5 social attribution) | Adjacent to **MECH-274** (other-model sleep-dependent aggregation, V4-reserved), **MECH-222/MECH-223** (self-attribution overflow; agency-attribution bias). The thought states this as a version-routing caution for V5, not as a mechanism. | **Left out deliberately.** Registering it now would invent precision the thought does not supply. Carried as a next-step flag only. |
| Quotient discards action-independent information needed for hazard detection, anomaly, other agents, later objectives | **ARC-001** already owns E1 as the preserver of absolute/causal context; the thought's own asymmetric reading ("E1 preserves the richer absolute and causal context") restates it. | **Already owned.** Recorded as a caveat inside the SD-056 refinement (a decision-facing derived view must never replace the absolute channel), not as a claim. |

## Key formulations (verbatim, load-bearing)

> Does the organism carry the action-relevant differences and residual uncertainty in its predictive state
> far enough through proposal, comparison, selection, commitment, and enactment to change what it actually
> does?

> Predict the action effect directly, rather than predict several absolute futures and subtract them only
> after approximation.

> A system can model environmental evolution accurately while remaining poor at estimating its own causal
> contribution. Conversely, an action-effect representation can support choice while being an impoverished
> world model.

> A predictive state used for counterfactual action comparison should not become more certain merely
> because it has been rolled forward without new evidence.

> Retained representation is not retained behavioural competence.

> Without those links, an efficient quotient could become epistemically dangerous. It might rank the
> current actions accurately while becoming blind to shared hazards, anomalous environmental changes,
> another agent's independently evolving state, or a later change in objectives.

> Social action effects must not subtract away another agent's independent evolution merely because it is
> shared across the current action set. V5 social attribution will need an explicit distinction between
> "unchanged by me" and "irrelevant."

> A useful REE predictor must preserve more than an expected future and less than an exhaustive simulation.

## Affected existing claims

Cross-references and `depends_on` additions only. **No status, confidence, evidence-direction, or
`what_would_answer` field on any existing claim is amended by this pass.** Proposed one-paragraph `notes`
addenda are in `refinements_proposed.md` and are proposals for the parent, not applied edits.

- **SD-056** -- the primary refinement target. Receives the counterfactual-quotient framing as external
  precedent for its already-chosen lever, a named fourth lever (direct signed-successor-measure target), a
  second candidate route to the same action-effect collapse (teacher forcing), and the "must not replace
  the absolute channel" caveat. **Not** amended in status; SD-056 remains `candidate` / `v3_pending`, and
  its outstanding 569e-equivalent re-run debt (recorded in its own `digestion_note`, 2026-08-07) is
  untouched by this intake.
- **ARC-002** -- cross-referenced. Its existing `what_would_answer` already names the weaker confirming
  form (`cand_world_pairwise_dist` tracking true viability differences); the thought's absolute-vs-effect
  distinction sharpens *why* that form is the weaker one. Proposed note addendum only.
- **MECH-033** -- cross-referenced as the owner of the E2->hippocampus handoff any derived centred view
  would ride. Proposed note addendum only.
- **MECH-510** -- cross-referenced. The thought explicitly says its uncertainty thread "supports MECH-510's
  separation between generative precision and prediction-error precision"; the proposed addendum records
  the independent external arrival and the horizon-dissipation measurable that sits beside it.
- **ARC-130 / ARC-131** -- cross-referenced. The thought's `representation -> ... -> retention` chain is an
  independent re-derivation of ARC-130's ladder; the Nijjer preprint is a candidate external corroborant
  for ARC-130's authority-vs-throughput dissociation and is routed to the existing
  `evidence/literature/targeted_review_arc_130/` directory. Proposed addendum records both, plus the
  standing caution against reading it as reviving MECH-476.
- **SD-063** -- cross-referenced (not amended). REE's live v3 vehicle for per-prediction predictive spread;
  the natural home for the UWM-JEPA preprint's transferable requirement and for the proposed contract
  field's producer side.
- **MECH-059** -- cross-referenced. Already answers the thought's confidence-provenance check as an ACTIVE
  claim; recorded so a later reader does not treat that check as an open gap.
- **MECH-094, MECH-322, INV-011, INV-019, ARC-020** -- cross-referenced by `Q-102`. MECH-094's strict
  gating is the constraint the question is posed *against*; MECH-322 is the existing narrow, sleep-only,
  real-value-tagged carve-out that shows the answer-shape REE already accepts. Neither is relaxed,
  amended, or challenged here.
- **SD-003 (superseded) / MECH-256 / SD-029 / SD-013 / ARC-033** -- cited as historical record for the
  derive-at-comparison-time form and the interventional-training requirement. Not reactivated.
- **MECH-476 (retired)** -- cited only as a caution. Not reactivated.
- **GOV-INTERVENE-1 / GOV-PATHVALID-1 / INV-103** -- cited as already owning the oracle/ceiling doctrine
  the thought's synchronized-branch caution reaches independently.
- **IMPL-022** (`docs/architecture/jepa_e1e2_integration_contract.md`) -- the one artifact this intake
  proposes to *change*, by adding one required metric and one required check (diff snippet below). Proposal
  only; the parent lands it.

## Candidate claims -- REGISTERED this pass

**One.** Registered into `docs/claims/claims.yaml` in this pass (draft prepared by an Opus subagent, reviewed and landed by the session; `status: open` per the corpus convention for open questions). The five notes addenda in Affected existing claims were applied as notes-only cross-references (SD-056, MECH-510, ARC-002, MECH-033, ARC-130, plus a one-line pointer on ARC-131). The IMPL-022 contract-field addition was NOT applied; it is chipped as follow-on work.

- **Q-102** (placeholder id; parent assigns the next free `Q-0NN`) --
  `simulation.imagined_trajectory_behavioural_access_repair`. `claim_type: open_question`,
  `polarity: open`, `status: candidate`, `epistemic_category: substrate_conditional`,
  `implementation_phase: v4`, `version_relevance: v4_v5`, `registered_utc: 2026-09-03`.
  `depends_on: [MECH-094, ARC-020, ARC-130, ARC-131]`.
  Location anchor: `docs/architecture/sleep.md#arc-020` (a real existing anchor at `sleep.md:76`; the
  alternative `docs/architecture/default_mode.md#mech-094` is MECH-094's own recorded location but has no
  literal `<a id="mech-094">` in that file). `sleep.md`'s "Related Claims (IDs)" list (line 159) needs the
  new id appended. No stub doc required.

  **DEDUPE REQUIRED, and this is the point of drafting it here.** The sibling raw thought
  `docs/thoughts/2026-09-02_sleep_as_deferred_reorganisation_and_behavioural_access_repair.md` reaches the
  same question independently, at its "Candidate provenance question": *"Can hypothesis-tagged simulated
  trajectories update retrieval, readout, or eligibility mappings strongly enough to preserve competence
  while remaining categorically barred from experienced residue, autobiographical fact, realized reward,
  and direct authority?"* A separate agent is drafting that intake concurrently. **This must be registered
  ONCE.** The wording proposed here is deliberately drawn to cover both framings (this thought's
  behavioural-access-repair framing and the sleep thought's four-provenance-class framing) so the parent can
  keep whichever draft is better and drop the other without losing coverage. If the sleep intake's version
  lands first, drop this one and add this thought's file to the surviving claim's `source_documents`.

**No `MECH-NEW-1` was minted, deliberately.** The one genuinely new item (uncertainty non-dissipation
across a blind rollout horizon) is a *measurable*, and the thought asks only that the check exist -- it
proposes no mechanism for producing the property, explicitly denies the density-matrix construction any
privileged status, and says the thread "may already be substantially covered." Minting a MECH here would
assert a substrate proposal the source does not make. It is routed as the `IMPL-022` field addition below.
Flagged for `/governance` rather than decided unilaterally: if governance judges the *requirement* (not
just the metric) claim-worthy, the natural shape is a `mechanism_hypothesis` at
`docs/architecture/precision_control.md` with `depends_on: [MECH-510, MECH-059, SD-063, MECH-385]` -- but
it is not registered here.

## Next steps

### 1. Literature entries to bank (three preprints; verified and banked by a literature subagent in the same routing session under evidence/literature/targeted_review_decision_useful_world_models/ and targeted_review_arc_130/)

All three are arXiv preprints reported by the thought and **not independently verified in this pass** --
neither citation-checked nor content-checked. A dedicated `/lit-pull` agent must verify each before any
`notes` field cites it as verified support rather than as an ingestion-time cross-reference. Proposed
routing:

| Preprint | Tag to claim(s) | Proposed `evidence/literature/` directory |
|---|---|---|
| Chen J, Wang R, Li J. *Counterfactual Quotient Models: Learning What Actions Change, Not What the World Does*. arXiv:2608.22092, 2026. | **SD-056** (primary); ARC-002, MECH-033 (secondary) | `targeted_review_sd_056_action_effect_quotient/` (new) |
| Radha SK, Goktas O. *UWM-JEPA: Predictive World Models That Imagine in Belief Space*. arXiv:2605.25313, 2026. | **SD-063** (primary); MECH-510, MECH-385, IMPL-022 (secondary) | `targeted_review_uncertainty_preserving_rollout/` (new) |
| Nijjer G. *The World Model Remembers, the Actor Forgets: Dream Rehearsal for Continual Model-Based Reinforcement Learning*. arXiv:2607.19749, 2026. | **ARC-130** (primary); ARC-131, Q-102, MECH-094 (secondary) | `targeted_review_arc_130/` (**existing** directory -- add an entry, do not create a new one) |

Scope constraints the lit-pull must carry into each `record.json`: Walker is a **stress result**, not a
supporting one (quotient targeting did not compensate for inadequate representational capacity); UWM-JEPA
does **not** establish durable long-horizon belief preservation (both families degraded at longer horizons)
and does **not** claim calibrated Bayesian posteriors; Nijjer is 17M parameters, MiniGrid, three seeds, one
replay-maintained regime, and reports latent drift despite head-level preservation. `confidence` on all
three should reflect preprint status. Per `feedback_lit_exp_decoupled` none of these may raise any claim's
`experimental_confidence`.

### 2. Proposed `IMPL-022` contract-field addition (diff snippet -- proposal, not applied)

Target: `REE_assembly/docs/architecture/jepa_e1e2_integration_contract.md`, "Evaluation Contract" section
(required metrics list at lines 190-196; required checks list at lines 207-213).

```diff
--- a/docs/architecture/jepa_e1e2_integration_contract.md
+++ b/docs/architecture/jepa_e1e2_integration_contract.md
@@ ## Evaluation Contract / ### Required metrics (stable keys)
 - `latent_rollout_consistency_rate`
 - `latent_uncertainty_calibration_error` (if uncertainty head present)
+- `latent_uncertainty_horizon_dissipation_rate` (if uncertainty head present) --
+  signed change in the predictor's own uncertainty estimate per rollout step during a
+  BLIND rollout (no new observation ingested after step 0), reported over the declared
+  `prediction_horizon`. A negative value means the predictor became more certain purely
+  by being rolled forward. Report the per-step series, not only its mean.
 - `action_conditioned_delta_error` (if action-conditioned enabled)
@@ ### Required checks
 - uncertainty provenance check: every uncertainty value must declare estimator type (`dispersion`/`ensemble`/`head`);
+- uncertainty non-dissipation check: under blind rollout, `latent_uncertainty_horizon_dissipation_rate`
+  must not be negative beyond a declared tolerance. A predictive state used for counterfactual action
+  comparison must not become more certain merely because it was rolled forward without new evidence.
+  NON-DEGENERACY: the check is vacuous unless the environment supplies genuinely ambiguous histories
+  (one observation history compatible with several hidden continuations); a fully observable domain
+  self-routes `substrate_not_ready` rather than reporting a PASS.
```

Producer-side note for whoever lands this: **SD-063** (E2 conditional predictive-uncertainty head,
provisional/v3) is the existing REE component that could emit the per-step series; nothing else currently
does. The `uncertainty_estimator` knob already contract-required by IMPL-022 (`dispersion` | `ensemble` |
`head`) is what makes the metric well-defined across profiles. **This is a documentation/contract change,
not a build authorisation** -- do not queue an experiment against the new field until a `/governance` cycle
routes it.

### 3. Experiment families A/B/C -- do NOT queue from this intake

The thought's Experiments A (absolute vs action-effect targeting), B (point vs uncertainty-preserving
prediction), and C (retained predictive competence vs behavioural access) are well-specified but every one
of them is gated:

- **A** is an SD-056 experiment, and SD-056 already carries undischarged validation debt -- its own
  `digestion_note` records that the 569e-equivalent Pathway-A-vs-B re-run was never queued (~7 weeks, as of
  2026-08-07) despite its numerical precondition (V3-EXQ-617) passing the same day, and that ARC-065 GAP-A
  closed via a different lever. **The correct next move on this thread is to discharge SD-056's existing
  debt, not to queue a new arm on top of it.** Any Experiment-A design must also declare its DELTA-DIRECT
  arm an oracle/ceiling condition per GOV-INTERVENE-1 and carry a GOV-PATHVALID-1 production-path arm.
- **B** requires the proposed contract field (item 2) to exist, plus a partially-observable environment with
  verified multi-modal hidden continuations. Its own falsifier as the thought states it ("weakened if a
  simpler calibrated ensemble or mixture performs as well") should be a *pre-registered* arm, not a caveat.
- **C** is an ARC-130/ARC-131 audit, and per the standing rule its rehearsal intervention would touch
  MECH-094 -- which is precisely what `Q-102` says is unresolved. Do not run a rehearsal arm before that
  question has a governance-ratified answer shape.

All three go through `/queue-experiment` if and when routed. Nothing here authorises a build or a queue
entry.

### 4. Version routing (the thought's own note, carried forward unchanged)

The thought states: this concerns the full lineage and "should not silently pull a new representation into
V3"; if current V3 closure already requires a discriminative action-effect signal or uncertainty-preserving
rollout, "the relevant minimum follows the dependency into V3"; rich learned quotient representations,
belief-structured latent dynamics, changed action sets, multi-object consequences, and dream-based
behavioural rehearsal "appear more naturally aligned with later substrate unless a current gate proves them
necessary."

Applied here: `Q-102` is parked `v4` / `v4_v5` per standing thought-intake practice. Note the tension a
governance cycle should resolve rather than this intake: the *action-effect minimum* already IS in V3 --
SD-056 is `implementation_phase: v3` / `v3_pending: true`, and MECH-532 (registered 2026-09-01,
`implementation_phase: v3`) explicitly names SD-056 as the decompression half at the `z_world` compression
site. So the phase-follows-dependency rule points the first thread at V3, not v4, and this intake does not
change that -- it only declines to add new v3 scope on top of it.

The thought's V5 social caution ("unchanged by me" vs "irrelevant") is recorded here and deliberately not
registered; a future intake should sharpen it against MECH-274/MECH-222/MECH-223 before it earns a claim.

### 5. Marker

Raw thought file `docs/thoughts/2026-09-02_decision_useful_counterfactual_world_models_under_uncertainty.md`
to be marked `Status: processed` with this intake linked, per the Stage 1/2 linking convention. Exact header
lines in `marker.txt` -- note that the raw file's existing `**Status:** Raw evidence-backed thought...` line
must be relabelled rather than deleted.

### 6. GOV-HELDOUT-1

Not applicable to this pass -- this intake changes no standing rule, workflow, or skill. The one proposed
change to a governing artifact (the IMPL-022 contract-field addition) is a *contract metric*, not a
standing-rule wording change, and is routed as a proposal for the parent rather than landed here.
