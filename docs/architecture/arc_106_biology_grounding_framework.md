---
title: Biology-Grounding Framework
parent: "Foundations & Rationale"
grandparent: Architecture
nav_order: 2
status: candidate
status_asof: 2026-07-10
status_claim: ARC-106
---

# Biology-Grounding Framework

**Claim Type:** architectural_commitment &nbsp;|&nbsp; **Status:** candidate (adopted as a standing design constraint by user decision 2026-06-20) &nbsp;|&nbsp; **Claim ID:** ARC-106

<a id="arc-106"></a>

**Subject:** `architecture.biology_grounding_constraint`
**Depends On:** MECH-439 (first worked example), SD-011 (canonical grounding success), SD-033 (region-grounded substrate family), ARC-035 (vmPFC)
**Registered:** 2026-06-20
**Location:** this document

---

## 1. Purpose

This is a standing constraint on how **REE the agent** is constructed, plus the method that operationalises it. It is *not* a claim about REE_assembly governance, and it does not assert a mechanism. It says: wherever feasible, build REE so that each functional component maps to an identifiable neural substrate **at the level of function** (not homology), and track every place the design has diverged from biology in a living ledger.

Two reasons, both load-bearing:

1. **Biology is a known-working reference architecture.** When a design fork is genuinely underdetermined by REE's own evidence, "what does the brain do here, and why" is the strongest available prior. The brain is the one existence-proof that multiple competing upstream signals can be granted lawful access to action without one crude scalar permanently owning the final gate. Designing against that reference is cheaper than rediscovering its constraints by failure.
2. **REE_assembly is intended as a model of psychiatric failure modes.** That status is *earned*, not assumed: a component is only psychiatrically interpretable if its breakage maps to a recognisable disorder analog. A parameter chosen for engineering convenience, with no neural referent, cannot model a disorder when it fails — it just produces a bug. Grounding is the precondition for the clinical-modelling goal (cross-ref [REE for Psychiatrists](../ree_for_psychiatrists.md), [psychiatric_failure_modes.md](psychiatric_failure_modes.md)).

The doc exists because **the design has diverged** in places (the action selector is the worked example below), and because "be more brain-like" is not actionable on its own — it needs a method that separates a *load-bearing neural primitive* from *decorative mimicry*, or the grounding mandate just trades one failure mode (arbitrary engineering) for another (cargo-culting structure the brain has but REE doesn't need).

## 2. The standing constraint (ARC-106)

> Construct REE the agent so that each functional component has an identified neural analog at the function level, and so that biology serves as the reference of first resort for underdetermined design forks. Grounding must be **load-bearing** — a named neural primitive whose defining constraint is validated on a REE falsifier — not decorative naming. Divergences from biology are **expected and legitimate**, but must be made explicit and tracked, never silent. This is the **construction-time** complement to the **registration-time** rule "biology before formal definitions" (restated in [sd_047_multi_source_dynamics.md](sd_047_multi_source_dynamics.md):365-372; canonical failures SD-003, SD-010/SD-011).

ARC-106 is a **thin umbrella / standing design constraint + method**, not new mechanism. Like [ARC-080](arc_080_object_representation_primitive.md) it carries a coherence map, not a substrate. Its epistemic category resolves to `substrate_coherence` (promotion/demotion suppressed; it is a design choice, not an experiment-gated hypothesis). Adopted by user decision 2026-06-20; registered `candidate` pending its first governance walk.

## 3. Relationship to existing scaffolding (do not duplicate)

This framework sits on top of work that already exists. It does **not** re-derive any of it.

| Existing asset | What it provides | What ARC-106 adds |
|---|---|---|
| [founder_ontology.md](founder_ontology.md) | The canonical E1/E2/E3 -> biology mapping ("functional, not homology"): E1 = cerebrum/deep cortex, E2 = cortical-edge + cerebellar forward model, E3 = **basal ganglia + thalamic routing**. | A *method* for grounding the components *below* the engine level, and a divergence ledger. |
| [brain_region_map.yaml](brain_region_map.yaml) / [brain_map.md](brain_map.md) | Machine-readable atlas of mapped components (hippocampus, amygdala, pfc, cingulate, basal_ganglia, dmn, thalamus, pag, harm_stream, ...). Explicitly "functional analogy, not homology". | Fills the **`non_anatomy_prefixes`** gap — the components *deliberately left unmapped* (ethics, love, play, language, goal, commitment, attention, self, drive). Those are the convergence backlog (S9). |
| [invariant_types.md](invariant_types.md) | universal / emergent / grey_zone taxonomy for invariants. | Orthogonal: ARC-106 governs *construction*, invariant_types governs *which invariants survive substrate change*. |
| "biology before formal definitions" (memory + [sd_047](sd_047_multi_source_dynamics.md):365-372; failures SD-003, SD-010/SD-011) | A **registration-time** gate: commission a biology lit-pull before registering any claim that instantiates a formal concept. | The **construction-time** complement: ground the *build*, not just the claim text. The two are a pair — lit-pull tells you the biological mechanism; this framework tells you how much of it to import and how to know if it mattered. |

**Stance: function, not homology.** Following founder_ontology and brain_map.md, every mapping here is a *functional* analogy. We do not claim REE's `e3_selector.py` *is* a striatum; we claim it occupies the basal-ganglia **role** (which candidate gets access to execution) and should therefore be checked against how that role is solved biologically.

## 4. The grounding method

### 4.1 Grounding levels (the ladder)

Every component gets a grounding level. The level is descriptive, not a quality score — an L1 component is not "bad", it is "not yet audited against biology".

- **L0 — Ungrounded.** Structure/parameters chosen for engineering convenience; no neural referent. *Example: a bare `argmin` over a scalar cost.*
- **L1 — Functional analogy named.** The component is mapped to a brain function/region at the function level (founder_ontology / brain_region_map style). The minimum bar.
- **L2 — Literature-anchored.** The mechanism's defining constraint is sourced to specific literature (the biology-before-formal-definitions lit-pull), and the divergences from the biological mechanism are *identified* (not yet tested).
- **L3 — Divergence-audited and validated.** Divergences are explicit, and the load-bearing biological constraint has been **tested on a REE falsifier** with the result recorded. Full grounding.

### 4.2 The load-bearing vs decorative test

A grounding is **load-bearing** iff the biological primitive's defining constraint changes REE's behaviour in a way a falsifier can detect. Operationally:

> Ablate (or gap-blind) the biologically-motivated constraint while holding everything else fixed. If a pre-registered behavioural metric is unchanged, the grounding is **decorative** — the biological name is cosmetic and should be dropped or the mechanism redesigned.

This test is the antidote to cargo-culting. It is exactly the structure of the keystone selector experiment (V3-EXQ-689a): a "conflict-graded hold" is only a real import of the basal-ganglia hyperdirect motif if the committed-diversity lift is **gap-concentrated** (`C_GAPBLIND`), i.e. strictly above a fixed-k shortlist and a flat-hot softmax. A uniform lift means we built a hotter softmax and *called* it conflict-grading — decorative.

### 4.3 Anti-cargo-cult guardrails

These are the standing rules that keep "be brain-like" from becoming over-fitting (see also S8 risks):

- **G1 — Function, not homology.** Map the role, not the anatomy. Never import a structure because the brain has that region; import it because the *function* is needed and biology shows how the function is realised.
- **G2 — Reuse before duplicate.** Do not add a module that duplicates a function REE already implements differently. (E.g. an explicit D1/D2 Go/No-Go module when the harm cost `M` already *is* the No-Go channel — cf. the open "escape-forward reuse-vs-duplicate" bet.)
- **G3 — Minimal primitive first, validate, then escalate.** Import the single smallest neural primitive that could resolve the live failure; validate it on a REE falsifier before importing the surrounding stack. Do not build the full competitive-selection architecture when one constraint might suffice.
- **G4 — Preserve auditability.** Prefer the construction whose behavioural effect can be attributed by a clean arm-contrast. Reject biological complexity (e.g. opaque recurrent dynamics) that destroys the ability to attribute a result — the brain's selector is hard to debug; importing its complexity imports its opacity.

### 4.4 Divergence is data, not failure

REE faces constraints biology does not (no embodiment energetics, different timing, differentiability requirements) and vice versa. A divergence from biology is therefore often *correct*. The mandate is not zero divergence — it is **zero silent divergence**. Every entry in the ledger states where REE departs, whether the departure is principled, and whether it has been validated. The MECH-439 lit-pull is the model: it registered, as load-bearing, that canonical divisive normalisation is *pooled-symmetric and order-preserving* whereas REE's proposed `F -> eligibility` demotion is *rank-altering and single-target* — a deliberate, documented departure that *exceeds* the canonical computation, flagged so it carries its own separate justification.

## 5. The divergence ledger (living)

Schema per row: **component | REE construction | neural analog (function) | grounding level | key divergence | load-bearing? | psychiatric failure mode (on breakage) | convergence action / status.**

The ledger is seeded below. Rows other than the action selector reference their existing per-component docs rather than re-deriving them; the action selector (the live case) is worked in full in S6. The intended growth path is the `non_anatomy_prefixes` backlog (S9).

| Component | REE construction | Neural analog (function) | Level | Key divergence | Load-bearing? | Psychiatric failure mode | Convergence action / status |
|---|---|---|---|---|---|---|---|
| **Action selector (E3)** | Deterministic `argmin` over scalar `J(zeta)`; `F` ~88-89% of committed-selection variance ([e3_selector.py:683,1361](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/predictors/e3_selector.py)) | Basal-ganglia action selection: disinhibition/competition, hyperdirect (STN) conflict-graded hold, D1/D2 Go-NoGo, tonic-DA gain (founder_ontology E3=BG) | **L2** (lit-anchored: Frank, Cavanagh, Bogacz MSPRT, Aron; falsifier 689a pending) | A single scalar permanently owns the committed gate via `argmin`; biology has no such monopoly (winner emerges by disinhibition, not scalar comparison) | **Under test** (689a: load-bearing iff lift is gap-concentrated) | Perseveration; behavioural-repertoire narrowing; psychomotor/anhedonic action-collapse; set-shifting deficit | F -> eligibility-set + stochastic commit (tier-1 = 689a); rank-preserving whole-vector F-renorm (tier-2). See S6. |
| Harm valuation / drive-coupled gain | `lambda_eff` amplified by accumulated `z_harm_a` ([e3_selector.py:673-676](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/predictors/e3_selector.py)); commit threshold lowered by harm urgency (`:1161`) | Amygdala/PAG threat gain; descending pain modulation | L2 | gain is a scalar multiplier on one cost term | partially | Anxiety / threat-overweighting; avoidance-dominant policy; panic (urgency lowers commit threshold -> impulsive escape) | cross-ref [sd_035_amygdala_analog.md](sd_035_amygdala_analog.md), [sd_021_descending_pain_modulation.md](sd_021_descending_pain_modulation.md) |
| Harm streams (nociceptive split) | z_self / z_world / z_harm_s separated | Separate spinothalamic / ACC / insular nociceptive pathways | **L3** (grounding *success*: Melzack & Casey, Craig, Rainville) | minimal — modelled on the biology directly | yes | Chronic pain dissociation; alexithymia (interoceptive) | [sd_011_dual_nociceptive_streams.md](sd_011_dual_nociceptive_streams.md) — exemplar |
| OFC valuation head | `harm_eval_head` / SD-033b bias on candidate bank | OFC outcome-value / devaluation sensitivity | L2 | reaches authority but does not convert (485h) | under test | Goal-devaluation insensitivity; compulsion | [sd_033b_ofc_analog.md](sd_033b_ofc_analog.md); blocked behind selector (S6) |
| Commitment latch | beta-gate bistable latch + refractory ([beta_gate.py](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/heartbeat/beta_gate.py)) | BG/thalamic commit + maintenance | L1->L2 | refractory dynamics tuned, not bio-sourced | partially | Rigidity/perseveration (refractory too long); distractibility/disorganisation (too short) | [mech_090_commit_entry_predicate.md](mech_090_commit_entry_predicate.md), [mech_342_commit_maintenance_release.md](mech_342_commit_maintenance_release.md) |
| Drive / incentive salience | `wanting = base_value*(1+kappa*per_axis_drive)` | Mesolimbic incentive salience (wanting != liking) | **L3** (intensity face; validated on 514u) | scalar-gain FLIP falsified (514t), but continuous-amplitude reading VALIDATED (514u PASS/supports, ceiling lifted 2026-06-21); residual: natural drive re-weights intensity yet does not re-select the argmax target without overshoot | residual (secondary flip disjunct; magnitude artifact, not a falsification) | Addiction (wanting-liking dissociation); apathy | [sd_057_object_bound_incentive_salience.md](sd_057_object_bound_incentive_salience.md); L3 via BG-4 / V3-EXQ-514u |
| **Goal / wanting layer** | single compact `z_goal` handle (GoalState) on slow EMA + SD-039 ghost-goal-bank rank; goal maintenance/abandon as threshold / one-shot flag | Frontal goal-directed control: vmPFC/dlPFC/dACC goal encoding+routing, ventral-striatal / mesolimbic-DA effort-based initiation, the current-concern commit->pursue->disengage lifecycle | **L1->L2** (lit-anchored 2026-07-07 by assembling on-file reviews; falsifier deferred to v4) | (D1) static-threshold/one-shot abandon vs biology's obstruction-appraisal-gated current-concern *state* (offset not keyed on value-drop/cost-tally); (D2) one `z_goal` channel collapses biology's rich-write (Spellman) / compact-retrieval (Ito) / thalamic-gate (Hallock) / task-graph-store (Baram) split | under test (deferred) -- the obstruction-appraisal abandon falsifier | Apathy / anhedonia / avolition (over-disengagement: Husain & Roiser 2018) vs perseverative striving / rumination + arrested-depression (under-disengagement: Klinger 1975, Brandstaetter 2013) | BG-5 / [goal_deliberation_v4_plan.md](../../evidence/planning/goal_deliberation_v4_plan.md); L2->L3 gated on the v4 substrate (GDL-1 multi-slot + GDL-5 interrupt/resume) |
| Ethics / commitment / attention / drive (policy layer) | distributed; no unifying region map | (deliberately unmapped — `non_anatomy_prefixes`) | **L0/L1** | n/a | n/a | various | **convergence backlog — S9** |
| **Go/No-Go combination** | benefit (Go) + harm (No-Go) pre-summed into one additive scalar `J = f + λ·m + ρ·Φ − β·b` ([e3_selector.py:683](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/predictors/e3_selector.py)) | D1/direct vs D2/indirect **parallel opponent** pathways (dissociable; different routing, DA sign, timing) | **L1** | opponent pathways collapsed into one cost: high-Go+high-NoGo is indistinguishable from low-Go+low-NoGo | **load-bearing** (blocks the conflict failure mode) | Anxiety; approach-avoidance conflict; OCD CSTC over-binding | D1/D2 population split — `basal_ganglia_assembly_map` A.2/B4 |
| **Dopaminergic RPE / teaching signal** | unsigned E3 prediction-error **variance** (ARC-016) used for precision / commit threshold; no signed RPE; gating layer has no learned parameters | **signed** dopaminergic RPE driving D1-LTP / D2-LTD three-factor plasticity | **L1** | unsigned magnitude substituted for a signed signal — cannot drive directional plasticity | **load-bearing** (blocks any learned gating; the conversion-ceiling root) | Reward-learning / anhedonia signatures if mis-signed | signed RPE in a unified dopamine substrate — `basal_ganglia_assembly_map` A.4/B5 |
| **Anti-perseveration / No-Go recency** | `count(action in history)/len(history)` ([dacc.py](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/cingulate/dacc.py), MECH-260) | dACC value-gated suppression of recently-**rewarded** choices when exploration is warranted (Scholl/Kolling) | **L1→L2** | raw recency count, not outcome-gated — suppresses a repeatedly-**correct** action just for repetition; now reused as the MECH-449 perseveration No-Go axis | partially | Pathological switching vs perseveration; inhibition-of-return artefacts | value-gated suppression (V3-tractable) — `basal_ganglia_assembly_map` B7 |
| **BG neuromodulator pair** | 5-HT built (MECH-203/204); **dopamine absent** (only biological-basis comments) | DA = principal for action-selection/learning; 5-HT = opponent (Cools/Dayan) | n/a (sequencing) | opponent neuromodulator built before the principal | n/a | n/a | build the dopamine substrate — `basal_ganglia_assembly_map` A.4/B8 |
| **Tonic exploration noise (MECH-440)** | factorised-Gaussian per-parameter WEIGHT NOISE at the E3 selection head (NoisyNet; [noisy_selection_head.py](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/policy/noisy_selection_head.py)); propagates into the committed argmin; sigma self-anneals via a LOCAL confidence EMA | LC-NE tonic exploration: a **systems-level tonic/phasic mode gate** that raises baseline decision noise, annealed by controllability (Aston-Jones & Cohen 2005; Tervo 2014 causal LC->ACC) | **L2** (lit-anchored; falsifier queued) | **(1)** per-parameter sigma is one description-level *below* biology's systems-level mode gate; **(2)** sigma self-anneals via REE's LOCAL confidence EMA, **not** NoisyNet's RL gradient — REE does not backprop through E3 selection | under test (falsifier: committed entropy > matched temperature control, not thrash) | over-exploration / disorganised action if sigma fails to anneal; rigidity if it over-anneals | falsifier on the 569i top-k + MECH-448 stack (loop-seg OFF vs ON); `state_conditioned_exploration_noise_floor.md` #mech-440 |
| **Directed curiosity (MECH-441)** | K-head E2 forward-model ensemble; per-candidate cross-head VARIANCE -> propagating curiosity bonus into E3 selection ([model_disagreement.py](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/policy/model_disagreement.py)) | frontopolar directed exploration; epistemic-uncertainty-driven curiosity (Daw 2006; RND/Plan2Explore) | **L2** (substrate-existence anchor only — the disagreement *computation* is the engineering import; weakest of the cluster) | the model-disagreement computation is an ML import (RND/Plan2Explore), not derived from the frontopolar substrate; bonus arbitrates only WITHIN the F-eligible set (safety bound) | **likely gated on ARC-110** (706b: the channel works; the single arena is the bottleneck) | impaired directed exploration / failure to seek informative states | falsifier HELD gated on ARC-110 validation V3-EXQ-707; `state_conditioned_exploration_noise_floor.md` #mech-441 |

> **Consolidated BG ledger + missing-pieces map + top-three disposition note:**
> [`evidence/planning/basal_ganglia_assembly_map_2026-06-22.md`](../../evidence/planning/basal_ganglia_assembly_map_2026-06-22.md).
> The four rows above were SILENT divergences until 2026-06-22 (ARC-106
> zero-silent-divergence violation, now closed). That doc also carries the
> afferent/efferent/learning missing-pieces map and the
> defensible-simplification-vs-repair-target disposition for the top three
> (recurrent settling, F-deletion, disinhibition/surround inhibition).

## 6. Worked example: the E3 action selector

This is the live case that motivated the framework, and the template for how a ledger row gets worked from L2 to L3.

### 6.1 Current construction (REE the agent)

The committed action is chosen by a **deterministic `argmin` over a single additive scalar** `J(zeta) = F + lambda*M + rho*Phi_R - beta*B - goal ...` ([e3_selector.py:683](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/predictors/e3_selector.py); final pick [e3_selector.py:1361](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/predictors/e3_selector.py)), where `F = coherence_cost - viability` carries **88-89% of committed-selection variance** (V3-EXQ-571: 0.886 baseline, 0.894 *with the full diversity stack*). The richer competition machinery (top-k shortlist, divisive-norm authority, conflict-graded width, gap-scaled commit temperature, class-stratified select) exists in code but is **gated off by default**.

This is the L0/L1 state: an `argmin` over a scalar is an engineering-convenient selector, named "E3 / basal ganglia" (L1) but not built like one.

### 6.2 Neural analog (the reference)

Basal-ganglia action selection is **not** an argmax over a value scalar. The winner emerges by **disinhibition** within a competition: a **hyperdirect (cortico-STN) pathway** transiently raises the decision threshold under choice-conflict (a global "hold / widen the field"), a **D1/D2 Go-NoGo** balance gates candidates, and **tonic dopamine** sets exploration gain. (founder_ontology E3=BG; lit-anchored by the MECH-439 targeted review: Frank 2006 "hold-your-horses", Cavanagh/Cohen/Frank 2011 mediofrontal-theta-raises-threshold, Bogacz & Gurney 2007 MSPRT, Aron & Poldrack 2006 hyperdirect stop.)

### 6.3 The divergence (made explicit)

REE's `argmin` over a near-monopolised scalar is the divergence: **one crude scalar permanently owns the final gate.** An argmin over a scalar that is ~89% one component cannot express upstream diversity at the committed layer except at exact ties, regardless of how the modulators are weighted. This is not a tuning state; it is a structural property of the selection *rule*. (Confirmed by the diagnosis: gain-calibration is falsified by 514t's regression; candidate-pool is falsified by 569h's diverse-input-flat-output; the only positive lever was structural bounding, 569i.)

The MECH-439 lit-pull registered two **load-bearing divergences** from the biology:
- canonical divisive normalisation is **order-preserving** -> alone it keeps F the argmax; the diversity lift requires a downstream **stochastic** commit (a build precondition E3 must possess, currently off-by-default).
- canonical normalisation is **pooled-symmetric** (every score divided by a shared field) whereas REE's proposed lever demotes **only F** -> a faithful lever renormalises the whole vector; REE's stronger "F removed from the argmin" is rank-altering and *exceeds* the canonical computation (needs its own justification, e.g. QD/MAP-Elites).

### 6.4 Convergence (the v3-bounded redesign)

Mostly **promoting existing-but-off machinery to load-bearing**, not new modules (guardrail G3):
- **tier-1 (minimal):** F defines an *eligibility set* (conflict-graded near-tie shortlist, `k = f(F-gap)`) and commit is **stochastic within the set** (gap-scaled temperature) so the modulator field owns the within-set order. This is V3-EXQ-689a.
- **tier-2 (fallback):** rank-preserving whole-vector F-renormalisation / `F -> eligibility-only` demotion if tier-1's lift is uniform.

### 6.5 L2 -> L3 transition

The row moves to L3 when 689a returns a verdict under the load-bearing test (S4.2): **PASS with gap-concentrated lift** => the BG-hyperdirect import is load-bearing and validated; **uniform lift** => decorative conflict-grading, escalate to tier-2; **no lift** => the blocker is downstream (commit latch) — re-ground that row instead. (689a is currently the keystone and was stalled on a stale Mac claim as of 2026-06-20; the experiment, not the design, is the bottleneck.)

## 7. Psychiatric failure-mode mapping (structural axis)

Because grounding is the precondition for clinical modelling (S1.2), **every ledger row carries the disorder analog of its breakage** — this is a required column, not an afterthought. The discipline: a component's failure mode is read off the *biological* function it occupies, and a REE failure that matches it becomes a candidate computational model of that disorder. Cross-ref [psychiatric_failure_modes.md](psychiatric_failure_modes.md), [psychiatric_failure_axes.md](psychiatric_failure_axes.md), [depressive_network_regimes.md](depressive_network_regimes.md), [slow_modulatory_state_and_compulsive_loops.md](slow_modulatory_state_and_compulsive_loops.md).

The selector is the proof of concept of the *value* of grounding: the same computational fact — **one value dimension monopolising committed selection with no conflict/competition layer** — is the shared signature of *perseveration*, *behavioural-repertoire narrowing in depression*, *set-shifting deficits* (OFC/vmPFC), and at the extreme *catatonic action-collapse / stereotypy*. Ungrounded, "committed-action entropy stays flat" is just a failed experiment; grounded, it is a testable model of psychomotor narrowing. Adjacent rows: harm-gain runaway -> anxiety/threat-locking and panic; over-strong No-Go -> akinesia / OCD-like doubt loops; incentive wanting-liking dissociation -> addiction vs apathy.

**Guardrail:** do not force a disorder label where the analogy is weak (G1-adjacent). A row may carry "no clean analog" — that is honest and better than a speculative mapping that would mislead a clinician reading the model.

## 8. Risks of over-fitting to the brain analogy

The grounding mandate has its own failure modes; the guardrails (S4.3) exist to bound them.

- **Cargo-culting structure** the brain has but the live failure does not require (mitigated by the load-bearing test S4.2 + G3).
- **Duplicating a function** REE already implements differently (G2; the reuse-vs-duplicate bet).
- **Mechanism-wrong instantiation** of a biological concept — the recurring "philosophy-right / mechanism-wrong" failure (SD-003's 28 FAILs; the SD-010/011 harm split). A "conflict signal" in BG is STN/dopaminergic and timing-specific; REE's `conflict_gap_norm` is a static score-gap. The lit-pull-before-registration gate is the primary defence.
- **Auditability collapse** from importing opaque dynamics (G4). More moving parts -> harder autopsies -> the exact failure-treadmill the framework is meant to shorten.
- **Constraint mismatch** — the argmin may be wrong for REE for a *different* reason than it is wrong for brains, so the brain fix may not be the REE fix. Use biology as a source of **candidate primitives validated on REE's own falsifiers**, never as a stack to import wholesale.

## 9. Convergence roadmap (resume primitive)

**Tracked as:** [biology_grounding_convergence_v4_plan.md](../../evidence/planning/biology_grounding_convergence_v4_plan.md) — a `generation: v4` forward-roadmap in the closure pipeline (nodes BG-1..BG-7, no `owner_exq`, excluded from the V3 closure %). Each node's `readiness_gate` is the V3-era prerequisite that defers it; the selector node (BG-2) mirrors the V3-owned `behavioral_diversity_isolation:GAP-I` rather than duplicating it. The table below is the human-readable mirror of that plan.

The backlog is the `non_anatomy_prefixes` set from [brain_region_map.yaml](brain_region_map.yaml) — components with per-claim docs but no systematic function-grounding row. Work each from its current level toward L3, one component per session, lit-pull-gated.

| # | Component cluster | Current level | Next action | Status |
|---|---|---|---|---|
| C1 | Action selector (E3) | L2 | Land 689a verdict under the load-bearing test (S6.5) | in-progress (689a keystone) |
| C2 | Commitment / de-commit | L1->L2 | Lit-pull commit/maintenance dynamics; ground refractory | open (cf. SD-034 cluster) |
| C3 | Drive / incentive salience | **L3** (intensity face) | DONE -- 514u measurement-redesign LANDED PASS/supports (applied 2026-06-21); scalar-flip falsified, continuous-amplitude validated | done (BG-4; owner V3-EXQ-514u) |
| C4 | Goal / wanting | **L1->L2** | DONE -- lit-anchored 2026-07-07 by assembling on-file reviews (frontal_goal_grounding + goal_disengagement + proxy_progress + wanting_liking); divergence + two-poled psychiatric column stated. L2->L3 = obstruction-appraisal abandon falsifier, gated on v4 goal-deliberation substrate | in-progress (BG-5) |
| C5 | Attention (distributed) | L1 | unifying map, not a module (per attention=precision-selection note) | open |
| C6 | Ethics / commitment policy | L0/L1 | function-ground or mark "no clean analog" | open |

Sequencing rule: do not open a downstream row's convergence while the selector (C1) gates it — the same plan-of-record gate that holds the channel retests behind 689a ([behavioral_diversity_isolation_plan.md](../../evidence/planning/behavioral_diversity_isolation_plan.md) GAP-I).

## 10. Governance wiring

ARC-106 is enforced through three existing channels, not a new pipeline:

1. **The `biology_grounding_note` field** (as on ARC-080): any new substrate claim should carry one, naming its grounding level and any divergence. Absence on an L2+ component is a drift signal.
2. **The biology-before-formal-definitions gate** (registration-time): unchanged; this framework is its construction-time partner.
3. **The divergence ledger (S5)**: updated in the same pass as any substrate change that moves a component's level. The ledger is the resume primitive for the convergence roadmap.

No promotion machinery acts on ARC-106 (epistemic_category = substrate_coherence). It is a constraint future design is checked against, surfaced as drift when violated, not an experiment-gated hypothesis.

## 11. Related claims and docs

- **Engines:** [founder_ontology.md](founder_ontology.md) (E1/E2/E3 -> biology), [brain_map.md](brain_map.md), [brain_region_map.yaml](brain_region_map.yaml)
- **Grounding exemplars:** [sd_011_dual_nociceptive_streams.md](sd_011_dual_nociceptive_streams.md) (L3 success), [sd_033_pfc_subdivision_architecture.md](sd_033_pfc_subdivision_architecture.md), [vmPFC.md](vmPFC.md)
- **Selector worked example:** MECH-439; [behavioral_diversity_isolation_plan.md](../../evidence/planning/behavioral_diversity_isolation_plan.md) GAP-I; [conversion_ceiling_phase0_synthesis_2026-06-18.md](../../evidence/planning/conversion_ceiling_phase0_synthesis_2026-06-18.md)
- **Method partner:** "biology before formal definitions" ([sd_047_multi_source_dynamics.md](sd_047_multi_source_dynamics.md):365-372); failures SD-003, SD-010/SD-011
- **Clinical:** [REE for Psychiatrists](../ree_for_psychiatrists.md), [psychiatric_failure_modes.md](psychiatric_failure_modes.md), [psychiatric_failure_axes.md](psychiatric_failure_axes.md)
- **Taxonomy (orthogonal):** [invariant_types.md](invariant_types.md)
