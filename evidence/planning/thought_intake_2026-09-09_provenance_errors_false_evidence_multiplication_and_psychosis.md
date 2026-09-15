# Thought intake -- Provenance Errors, False Evidence Multiplication, and Psychosis

**Date:** 2026-09-15
**Raw file:** `/Users/dgolden/REE_Working/REE_assembly/docs/thoughts/2026-09-09_provenance_errors_false_evidence_multiplication_and_psychosis.md` (499 lines)
**Session:** thought-pipeline-20260915
**Family:** E (single-file family; no sibling raw thoughts assigned)
**Status:** Stage 2 structured intake. Registers nothing. No claim status, confidence, evidence_direction or queue entry is touched by this pass.

---

## 0. READ THIS FIRST -- the branch is already deep in execution, and the thought is partly superseded by it

This raw thought is NOT an unprocessed idea. Between 2026-09-09 and 2026-09-10 it spawned a
twelve-artifact planning and probe campaign under `REE_assembly/evidence/planning/`, four
executed synthetic probe results, and four probe scripts under `REE_assembly/scripts/`. Two of
those results MATERIALLY REFINE OR CONTRADICT the raw thought's own proposals (section 4b below).

**And none of it is registered.** `grep` over `docs/claims/claims.yaml` for every one of those
artifact filenames, and for `source_thought: docs/thoughts/2026-09-09*`, returns ZERO hits. The
entire branch -- ladder, six assays, corrected evidence map, four run results -- is carried in
planning prose with no claim registry entry anywhere.

| Artifact | Lines | What it is |
|---|---|---|
| `evidence/planning/provenance_false_evidence_multiplication_experiment_ladder.md` | 296 | the P1-P6 assay ladder + shadow stage + stop conditions |
| `evidence/planning/provenance_psychosis_literature_pull_20260909.md` | 591 | clinical source-monitoring baseline |
| `evidence/planning/provenance_false_evidence_multiplication_campaign_supplement_20260910.md` | 241 | hippocampal-campaign audit; the six evidence classes; Breaks A and B; the C3 correction |
| `evidence/planning/provenance_harness_generated_ancestry_design.md` | 570 | the generated-ancestry harness design + genealogy contract |
| `evidence/planning/provenance_p3_replay_amplification_design.md` | 372 | the P3 replay loop design |
| `evidence/planning/provenance_judgment_class_literature_tranche.md` | 229 | judgment-class sweep; the Pilditch 2020 counterweight |
| `evidence/planning/provenance_branch_hippocampal_audit_verification_20260910.md` | 267 | audit verification; controls P1-R5/R6, P3-R4..R7 |
| `evidence/planning/provenance_genealogy_probe_p0_result.md` | 147 | **RUN** -- endogeneity gate PASS |
| `evidence/planning/provenance_p1_result.md` | 167 | **RUN** -- all preregistered criteria pass |
| `evidence/planning/provenance_p1r5_retrieval_attribution_result.md` | 264 | **RUN** -- both routes inflate; `dependent` fix fails on both |
| `evidence/planning/provenance_p3_r2_spike_result.md` | 168 | **RUN** -- healthy-replay arm reachable after harness fix |
| `evidence/planning/provenance_p3_harness_contract_reconciliation.md` | 171 | H1-H8 contract verdicts |

The intake below is therefore written to REGISTER THE BRANCH AS IT NOW STANDS, not as the raw
thought states it.

---

## 1. Verbatim core proposal

The thought's own compact formulation (section 16, quoted in full because it is the claim):

> "An error-tolerant cognitive architecture need not prevent every false representation. It must
> prevent one false representation from reproducing through prediction, memory, replay and
> interpretation and returning as multiple apparently independent reasons to believe itself.
> Provenance errors may therefore be computationally dangerous not only because they misidentify
> the source of an experience, but because they can inflate the apparent cardinality of evidence."

The mechanism chain (section 1):

```text
internal event -> wrong provenance -> false independence
  -> duplicated evidential weight -> premature confidence / closure
```

The engineering rule (section 6):

> "A hypothesis must not be allowed to cite its own descendants as independent witnesses."

The architectural design pressure (section 15):

> "Every representation that can later influence belief, confidence, closure or action should
> preserve enough uncertain causal genealogy to prevent its own descendants from being blindly
> counted as independent evidence."

The thought is explicit that this is NOT a diagnostic model of psychosis (sections 5B, 14, header).

---

## 2. Novelty table

DEFAULT ASSUMPTION APPLIED: REE probably already owns most of it. It owns more than the thought
assumes, and the parts it does not own are narrower than the thought's framing.

| # | Thread in the thought | Existing REE coverage | Verdict |
|---|---|---|---|
| 1 | Internally generated content must be distinguished from real experience; failure = confabulation | **MECH-094** (status `stable`; "simulation content does not accumulate in the viability map as committed experience; failures produce confabulation"), **MECH-248** (source monitoring, Johnson-Raye, as the biological implementation), **MECH-249** (ACh/NA mode-setting), **MECH-037** (Papez-like provenance gating / reality filtering, `provisional`), **INV-011** (imagination without belief update), **INV-019** (rehearsal/durable-write separation), **MECH-319** (categorical replay tag at the rule-arbitration layer) | **already-owned** -- cross-ref only |
| 2 | Provenance must NOT be a decorative immutable label; it is distributed, probabilistic, updated, corruptible | **MECH-094** notes, verbatim: "not a single categorical gate but a distributed set of overlapping mechanisms"; the 2026-04-16 reframe explicitly struck "hypothesis_tag as categorical gate" language | **already-owned** -- the thought's section 3 warning is a warning REE already heeded |
| 3 | Provenance is richer than source identity; several partly-independent dimensions, each with its own confidence | **MECH-430** ("Multi-dimensional provenance source vector ... perceived-vs-imagined, self-generated-vs-other-generated, source identity, temporal source, modality ... each dimension carries its own confidence"), **MECH-365** (provenance-bearing event token with one-way committed gate) | **already-owned** for the per-token dimensions |
| 4 | Soft / uncertainty-bearing provenance degrades more gracefully than hard categorical ancestry | assay 005 result (`convergence_signal_synthetic_assay_005_result_2026-09-09.md`) is the thought's own source; MECH-430 supplies per-dimension confidence | **already-owned AND now partly DISCONFIRMED** -- see 4b(ii). Do NOT register the thought's section-8 recommendation |
| 5 | Source tags degrade while narrative structure is retained | **MECH-544** ("REGISTERED SIGNATURE -- SOURCE-TAG DECAY: source information degrades while narrative structure is retained"), registered 2026-09-08 from the culture package | **already-owned** -- near-exact match |
| 6 | **Provenance error changes evidence CARDINALITY, not only source label** (the core) | Nothing at the agent/epistemic level. Three adjacent-but-different homes: **ARC-115** (socially-supplied agreement must not enter the same accumulator as internally-derived confidence -- the EXTERNAL-ASSERTION channel, not the self-descendant one); **SD-088** (the claims REGISTRY must represent source-dependence between supporting judgements -- the Assembly instrument, not the agent); **MECH-548**(b) SEMANTIC DOUBLE-COUNTING (content already injected is re-amplified -- at ONE translation interface, a gain problem, not an evidence-count problem) | **genuinely new** -> register narrowly, distinguished from all three |
| 7 | A relational GENEALOGY representation: ancestor id, transformation lineage, shared-ancestor probability, already-counted-evidence family, context-conditioned dependency estimate | Nothing. MECH-430's dimensions are PER-TOKEN attributes; none of them is a RELATION between tokens. MECH-365's token schema has `source_status` / `committed_vs_imagined`, no edges. `ree_core` has no ancestry structure at all (section 7) | **genuinely new** -> register, explicitly as an extension of MECH-430 from a vector to a graph |
| 8 | Recursive amplification: confidence rises with replay count at fixed external evidence | **MECH-363** names "runaway resonance" but at the cognifold field-coupling level with signed-coupling as the fix; **MECH-173 / MECH-204 / SD-076** are the existing confidence-inflation family but the mechanism is asymmetric precision EMA and absent REM recalibration, not evidence counting; **MECH-092** is replay itself. Nothing joins replay count to an independence estimate | **genuinely new** -> register as a separate mechanism (the ladder's H2, which its own supplement records as "untested in every class") |
| 9 | Hallucination-like (source readout) and delusion-like (epistemic readout) consequences must not be collapsed | **MECH-094** vs **MECH-244/245/246/247** already separate confabulation from three psychosis pathways from hallucination, and MECH-094's notes carry the Lavalle 2020 tag-loss vs tag-misassignment dissociation. But that is a dissociation between FAILURE KINDS, not between two READOUTS on one manipulation | **adjacent-but-distinct** -> register as an open question, distinguished from the tag-loss/tag-misassignment cut |
| 10 | Error tolerance = containing the "epistemic reproductive number" of an error | Nothing (`grep -iE "error tolerance\|error-tolerant\|reproductive number"` -> no claim). But it is a restatement of thread 6's rule in engineering vocabulary | **fold into thread 6's notes** -- not a separate claim |
| 11 | Clinical: a provenance-error route to psychosis, as distinct from precision failure | **MECH-244** (precision-weighting failure, pathway A), **MECH-246** (signal-degradation pareidolia, B), **MECH-247** (trauma-shaped priors, C), **MECH-088** (four-plane taxonomy, psychosis = NA collapse of E1/E2 constraint + DA aberrant salience), **MECH-245** (hallucination as generative-model dominance) | **deliberately NOT registered** -- see section 6. The campaign supplement's own section 5.2 is DEFLATIONARY for the psychosis framing |
| 12 | Convergence only carries weight if the agreeing signals are independent (the trigger) | The convergence assays 001-006 exist as artifacts; no claim registers the convergence-as-signal programme either (`grep -iE "assay 00[1-6]\|synthetic assay"` -> no hits). **GOV-CONFIRM-1** (evidence-confirmer detector) and **GOV-REUSE-1** are the Assembly-side cousins | out of this thought's scope; flagged to the orchestrator as a separate registration debt |

---

## 3. Key formulations (verbatim)

From the raw thought:

> "The architecture has **manufactured corroboration by losing genealogy**." (section 4)

> "The key pathology would not be that the system predicts. Prediction is necessary. The pathology
> would be that **predictions are allowed to return as evidence without retaining sufficient
> information that they descend from the hypothesis being evaluated**." (section 6)

> "unknown provenance != independent provenance" and "uncertain source != confidently external
> source" (section 8)

> "This resembles a causal genealogy rather than a label." (section 9)

> "A negative result would still separate source attribution from evidence multiplication, which is
> scientifically useful." (section 11)

From the campaign supplement (2026-09-10), which CORRECTS the raw thought and must be read with it:

> "treating one lineage as several independent witnesses is a documented **healthy-human default
> under ancestry ambiguity**, not an unestablished conjecture and not a psychosis signature."

From the judgment-class tranche, restating the engineering rule (this is the form that should be
registered, NOT the raw thought's form):

> "A system must represent the dependency structure among its evidence and condition on it. It must
> not *infer* independence from the absence of a recorded dependency."

From the P1 result (2026-09-10), the finding that relocates the whole hypothesis:

> "the confidence inflation is **not forced by ancestry loss**. It is forced by the readout rule's
> *default for unknown ancestry*, and swapping that default eliminates it completely."

---

## 4a. Affected existing claims -- cross-reference only

No status, confidence, `evidence_direction`, `live_status` or `what_would_answer` field of any
existing claim is touched by this pass. The following are named as `depends_on` or
distinguished-from targets on the proposed entries.

| Claim | Status as read 2026-09-15 | Relation |
|---|---|---|
| MECH-094 | `stable` | parent: the simulation/real distinction the new claims extend from a write-gate to an evidence-weighting question |
| MECH-430 | `candidate` / `substrate_conditional` | generalized-from: the per-token source vector the genealogy graph extends |
| MECH-365 | `candidate` / `substrate_conditional` | the token schema the genealogy edges would attach to |
| MECH-544 | `candidate` / `substrate_conditional` | source-tag decay is the DEGRADATION PROCESS the new claims' corruption arm instantiates |
| MECH-548 | `candidate` / `substrate_conditional` | its mechanism (b) semantic double-counting is the same failure family at a different level |
| MECH-363 | `candidate` / `substrate_conditional` | runaway resonance is the field-coupling cousin |
| ARC-115 | `candidate` / `substrate_conditional` | distinguished-from: external-assertion channel vs self-descendant channel |
| SD-088 | `candidate` | distinguished-from: registry instrument vs agent mechanism |
| INV-077 | `candidate` / `substrate_coherence` | distinguished-from: governance-layer circularity ban vs agent-layer one |
| MECH-244 / MECH-245 / MECH-246 / MECH-247 | all `candidate` | the three existing psychosis pathways the clinical reading would have to be a fourth of -- NOT registered here |
| MECH-088 | `candidate` | the four-plane psychiatric taxonomy; psychosis row = NA collapse + DA aberrant salience. Untouched |
| MECH-092 | (see section 7) | replay itself, whose consumer is missing |
| MECH-275 / MECH-273 | `candidate` / `substrate_conditional`, `v3_pending: true` | the live V3 aggregation path in which the counting defect is instantiated (section 7) |
| SD-076 / MECH-173 / MECH-204 | `candidate` | distinguished-from: the existing confidence-inflation family, by mechanism |
| Q-102 | `open` / `substrate_conditional` | nearest existing open question; asks "what provenance rules make the separation machine-checkable" but about BEHAVIOURAL ACCESS, not evidence counting |
| INV-011 / INV-019 / MECH-319 / MECH-322 | various | the existing write-gate family; unchanged |

**One currency flag, not fixed here.** MECH-094's `what_would_answer` NON-DEGENERACY PRECONDITION
requires the enumerated call-site set to be "re-derived from the CURRENT tree at run time". That
enumeration names `ree_core/residue/field.py` and "the ~30 `getattr(new_latent, "hypothesis_tag",
False)` sites in `ree_core/agent.py`". Measured 2026-09-15: `agent.py` carries 87 occurrences of
`hypothesis_tag` and 24 sites across `ree_core/`. The claim's own drift-test framing anticipates
this; recording it so a later governance pass can re-derive rather than trust the stored figure.

---

## 4b. Where the raw thought is SUPERSEDED by its own branch

Three places. A later session must not re-derive the raw thought's positions as if they still
stood.

**(i) "dependent descendants become independent votes" is NOT an unestablished conjecture.** The
campaign supplement section 5 corrects the branch's own 2026-09-09 literature pull: the cardinality
step is directly established in healthy adults, content-matched, by Yousif, Aboody & Keil 2019
(PMID 31291546), Connor Desai, Xie & Hayes 2022 (PMID 35149359) and Weaver et al. 2007
(PMID 17484607). Consequence recorded in the supplement: "psychosis inflates confidence by losing
ancestry" is the wrong hypothesis shape, because the healthy baseline already does it. The
defensible clinical question becomes whether the independence-discrimination capacity that Connor
Desai 2022 shows is recoverable under explicit cueing is selectively not deployed in psychosis.
**NOT VERIFIED INDEPENDENTLY BY THIS PASS** -- the PMIDs are taken from the supplement, which
records them as located by targeted query.

**(ii) The thought's section-8 recommendation (soft provenance is safer) FAILS as stated.** From
`provenance_p1_result.md`: "The `soft` default is worth its own line, because it is the obvious fix
and it **does not work**: once every binding has fallen below the usable threshold there is nothing
left to interpolate a prior from, so it degenerates to `independent` exactly in the regime where it
was supposed to help. That is structural, not a tuning failure." Measured: `absent_policy=soft`
gave N_eff 1.117 -> 5.000 (inflation +3.883), i.e. WORSE than `independent`'s +3.753.
`absent_policy=dependent` eliminated it (-0.117). And `provenance_p1r5_retrieval_attribution_result.md`
then found the `dependent` fix ALSO fails (criterion A6 "FAIL, on BOTH routes"). So neither of the
two obvious defaults is a fix, which is why the proposed invariant below is stated as a
REPRESENTATION requirement rather than a DISCOUNTING rule.

**(iii) The engineering rule as the thought states it is one-sided and the branch has already
restated it.** Pilditch, Hahn, Fenton & Lagnado 2020 (Cognition 204:104343, PMID 32599310) proves
by construction that where a structural dependency exists but observations are partial or
contradicting, dependent reports support a hypothesis MORE than the independent case would --
so maximal discounting is the larger error. "A hypothesis must not cite its own descendants as
independent witnesses" is correct in its NEGATIVE form and wrong if read as "descendants should be
collapsed to one vote". The registered invariant below carries the corrected form.

---

## 5. Candidate claims -- REGISTERED this pass

Five placeholders. Full blocks in `proposed_claims.yaml`. All `epistemic_category:
substrate_conditional`, all carrying the explicit "DO NOT build in V3. DO NOT queue an experiment
from this entry." caveat, because the governing substrate (a genealogy representation) does not
exist in `ree_core` at all (section 7).

| Id | claim_type | One line |
|---|---|---|
| `INV-107` | invariant (universal) | A system must REPRESENT the dependency structure among its evidence and condition on it, and must not INFER independence from the absence of a recorded dependency. The negative rule ("a hypothesis must not cite its own descendants as independent witnesses") holds; the positive reading ("collapse descendants to one vote") is refused. |
| `MECH-552` | mechanism_hypothesis | Provenance corruption changes evidence CARDINALITY and not only source label: one causal lineage's descendants are counted as several independent witnesses, raising confidence at fixed world evidence. With the P1 locus correction: the operative variable is the READOUT'S DEFAULT FOR UNKNOWN ANCESTRY, not the corruption itself. |
| `MECH-553` | mechanism_hypothesis | A compressed relational GENEALOGY (shared-ancestor probability, external-anchor flag, hypothetical/replay lineage, already-counted-evidence family, context-conditioned dependency estimate) is the representation that discharges INV-107 -- a graph over tokens, extending MECH-430's per-token source VECTOR. |
| `MECH-554` | mechanism_hypothesis | Recursive replay amplification (the ladder's H2): under corrupted or absent genealogy, confidence rises monotonically with replay count while external evidence is fixed, and the belief becomes self-maintaining. Stratified by replay kind; requires matched retrieval quality. |
| `Q-105` | open_question | Are source attribution (P(external \| representation)) and evidence cardinality (effective independent-source count) DISSOCIABLE readouts under one provenance manipulation, or does one always drag the other? |

Recommended priority if the orchestrator wants fewer: `INV-107`, `MECH-552`, `MECH-554` are
load-bearing. `MECH-553` could be merged into `MECH-552` as its substrate half. `Q-105` is
the cheapest to drop.

---

## 6. Deliberately NOT registered

| Not registered | Why |
|---|---|
| **A fourth (provenance-error) psychosis pathway alongside MECH-244/246/247** | The thought forbids it explicitly ("not a claim that psychosis is caused by one provenance mechanism", section 14), AND the campaign supplement section 5.2 is deflationary: if false independence is the healthy default under ambiguity, the psychosis framing has the wrong shape. Registering a fourth pathway now would encode as a REE mechanism claim something the branch's own audit has argued against. If a clinical entry is ever wanted, the right shape is `claim_type: derived_prediction`, `prediction_domain: clinical_psychiatry`, `epistemic_category: out_of_domain` (the INV-106 shape), and its content should be the NARROWED question (is the independence-discrimination capacity deployed?), not the lesion-style account. |
| **"Soft provenance is safer than categorical provenance"** | Refuted as stated by the branch's own P1 run (4b(ii)). Registering it would register a position the evidence already contradicts. |
| **"A hypothesis must not cite its own descendants as independent witnesses", as a discounting rule** | Pilditch 2020 counterweight (4b(iii)). The corrected representation-form is what `INV-107` carries. |
| **The six-rung assay ladder (P1-P6) as claims** | Assay designs are not claims. They already live in `provenance_false_evidence_multiplication_experiment_ladder.md` and its six companions. Registering them would create a second, staler tracker. |
| **Error tolerance as "containing the epistemic reproductive number"** | A restatement of `INV-107` in engineering vocabulary, not a separate assertion. Folded into that claim's notes. |
| **The artificial-model-hallucination engineering analogy (section 7)** | Analogy, labelled as such by the thought. No falsifier. Belongs in notes, not a claim. |
| **Circular-inference equivalence (section 13)** | The thought itself says it "should not be declared equivalent without a dedicated literature comparison". That comparison has not been done. Recorded as a literature debt in section 8. |
| **Convergence-as-signal programme claims** | Out of this thought's scope, but flagged: assays 001-006 are also unregistered. Separate registration debt for the orchestrator. |

---

## 7. Implementation-gap audit (ree-v3)

Method: `grep -rn` over `/Users/dgolden/REE_Working/ree-v3/ree_core/` for `provenance`, `source`,
`origin`, `tag`, `is_imagined`, `hypothesis_tag`, `replay_origin`, `simulation_mode`,
`counterfactual`, `ancestry`, `lineage`, `ancestor`, `genealog`, `parent_id`, `posterior`,
`belief`, `evidence_count`, `n_eff`, `dedup`, `already.count`; plus direct reading of the write
paths and the sleep aggregation chain. Everything below is verified in the tree, not taken from
the thought or from the planning docs.

| # | Mechanism the thought treats as needed | Verified status | Evidence |
|---|---|---|---|
| 1 | Provenance tagging of latent content (perceived vs imagined) | **BUILT** -- a single boolean, strictly enforced | `ree_core/predictors/e2_fast.py:63` `hypothesis_tag: bool = False` on `Trajectory`; 24 files under `ree_core/` reference it (87 occurrences in `agent.py`, 24 in `residue/field.py`, 16 in `hippocampal/module.py`); `ree_core/agent.py:10662` `update_residue(..., hypothesis_tag: bool = False)` -- "hypothesis_tag=True blocks accumulation (MECH-094)" |
| 2 | Replay-origin marking | **BUILT**, narrowly | `ree_core/policy/policy_chunking.py:516` `replay_origin: bool = False`; the MECH-322 sleep-only carve-out behind `use_chunk_replay_origin_path` (default `False`, `ree_core/utils/config.py:5352`); `policy_chunking.py:406` "the shipped default is strict MECH-094" |
| 3 | Simulation-mode marking | **BUILT** -- `simulation_mode` appears across 20 modules (amygdala, hippocampal, pfc, predictors, sleep, goal) | `grep -rln simulation_mode ree_core/` |
| 4 | Per-trajectory provenance METADATA (an ancestor reference) | **PARTIAL, and deliberately stripped at commit** | `e2_fast.py:70` `metadata: Optional[Dict[str, Any]] = None`; populated only for MECH-293 ghost probes with `{"source": "mech293_ghost_probe", "anchor_key": ...}`. `ree_core/hippocampal/module.py:3450-3453` sets `hypothesis_tag=False, metadata=None` on the committed trajectory, with the comment "the executed trajectory IS real, regardless of whether the source proposal was a ghost. Strip the hypothesis tag and metadata". **This is correct under MECH-094 and is exactly the thought's PROVENANCE ABSENT condition**: after commit the architecture cannot know that an executed path descended from an internally generated hypothesis. |
| 5 | Multi-dimensional provenance vector (MECH-430) | **GENUINE GAP** -- one bit, not a vector. MECH-430 is `substrate_conditional` and its own notes say so | searched: no per-dimension confidence, no who-generated-it, no temporal-source field anywhere in `ree_core/` |
| 6 | **Ancestry / lineage / genealogy representation** | **GENUINE GAP -- nothing at all** | `grep -rniE "ancestry\|lineage\|ancestor\|genealog" ree_core/` returns **18 hits, all of them the word "lineage" in COMMENTS referring to EXPERIMENT lineages** (e.g. `config.py:115` "471-lineage env", `e3_selector.py:2361` "the decoupled 700-lineage null"). There is no ancestry data structure, no edge, no parent reference, no shared-ancestor probability. |
| 7 | An "already-counted evidence family" marker | **PARTIAL -- one local precedent, no general mechanism** | `ree_core/policy/policy_chunking.py:91-104` "WHY THE ONCE-PER-OUTCOME DEDUP IS LOAD-BEARING, not a micro-optimisation ... crediting the raw executed-action stream at every position without dedup mints 52-86 'chunks' ... one held action re-counted at five lengths. A readiness criterion would PASS on those for an entirely spurious reason." This is the SAME failure shape as the thought's, caught once, at one site, by hand. It is a dedup within one outcome report, not an ancestry representation. |
| 8 | An evidence-accumulation path where cardinality could inflate | **BUILT AND LIVE -- and it has the defect** | `ree_core/sleep/bayesian_aggregator.py` (MECH-275 Phase D). `update()` at lines 175-237: `tau_post = tau + tau_lik; posterior.n += 1` per routed replay event, keyed on `(domain, region)`. There is **no dependency term and no ancestry check**: N replay draws of the SAME anchor into the same region each add `tau_lik` precision, so posterior variance shrinks with replay COUNT rather than with independent evidence. Per-cycle `decay_factor` defaults to `1.0` (no decay, `bayesian_aggregator.py:102`). |
| 9 | Whether that path can actually be driven by repeats | **YES -- sampling is with replacement** | `ree_core/sleep/replay_sampler.py:128` `draw()` returns one Anchor per call from the frozen snapshot with no exclusion of already-drawn anchors, and the class already tracks `_draw_region_counts` (`replay_sampler.py:158`, exposed as `draw_region_counts`). So per-region replay count is ALREADY INSTRUMENTED. |
| 10 | Whether the inflated posterior is consumed | **PARTIALLY** | `ree_core/sleep/self_model_aggregator.py` (MECH-273 Phase E) uses "the posterior MEAN at each replayed region as the target residual" for offline `E2_harm_s` writeback. It consumes the MEAN, not the variance -- so the understated variance is stored but not read. Repeated dependent draws still pull the mean harder toward the repeated source's value. "place" domain has no V3 consumer beyond metrics (`bayesian_aggregator.py:42-46`). |
| 11 | Is the aggregator reachable in practice? | **YES** | `ree_core/utils/config.py:7050` -- `enable_sleep_aggregation_cluster()` sets `use_mech275_aggregator = True` (Phase D) and `use_mech273_self_model = True` (Phase E). Default is `False` (`config.py:6601`), bit-identical OFF. |
| 12 | Does the CLAIM sanction count-weighted aggregation? | **NO -- claim/implementation semantics mismatch** | MECH-275's title says "sleep phases **aggregate across many episodes**", and its `functional_restatement` warns "Aggregating arbitrary correlations would not produce schema revision -- it would produce noise-fit." The implementation aggregates across **replay draws**, not across episodes, with replacement. Cross-episode independence is the claim's premise; per-draw accumulation is the code's behaviour. Recorded as a finding, not fixed. |
| 13 | Replay descendants reaching memory at all | **GENUINE GAP -- the waking replay path has no consumer** | `ree_core/agent.py:10594-10658` `_do_replay()` computes `replay_trajs` and the function ENDS; the value is never used. `ree_core/hippocampal/module.py:257` comments "PRODUCTION path (agent._do_replay -> diverse_replay, which DISCARDS the ...". Corroborated by `evidence/planning/substrate_queue.json`, entry `mech092-replay-consumer-missing`, status `proposed_REGISTRATION_ONLY_not_a_build_authorisation`: "Replay trajectories are computed and DISCARDED -- `_do_replay` has no consumer anywhere in `ree_core`, an unowned blocker cited by four claims with no queue entry." |
| 14 | Anything in `substrate_queue.json` for provenance/ancestry/cardinality | **GENUINE GAP** | searched all 182 queue entries for `provenance\|ancestry\|genealog\|cardinal\|source.monitor\|double.count`: matches are incidental word uses only (MECH-293 ghost provenance, SD-037, arm-fingerprint). No entry exists for a genealogy substrate. |

### Audit verdict, in one paragraph

REE has built a **one-bit, strictly-enforced, committed-vs-imagined gate** and nothing above it.
The gate is real, live and load-bearing, and MECH-094 is `stable` on the strength of it. What does
not exist anywhere in `ree_core` is a representation of WHERE a piece of content CAME FROM
relative to other pieces -- no ancestor, no edge, no shared-ancestor probability, no
already-counted marker. The architecture therefore cannot in principle distinguish "four
descendants of one hypothesis" from "four independent observations", and the one place it
currently accumulates evidence across repeated internal reinstatements
(`bayesian_aggregator.update()`) does exactly the counting the thought warns about, with the
replay count already instrumented next to it. Two mitigating facts keep this from being an active
harm: the aggregator is default-OFF, and waking replay output is discarded before it reaches any
write path at all. The thought's central assertion that REE lacks the mechanism is therefore
**verified, and narrower than the thought states**: the gap is the genealogy, not the tagging.

### The one V3-observable diagnostic this audit surfaces (named, NOT queued)

Under `enable_sleep_aggregation_cluster()`, `BayesianAggregator` posterior precision per region can
be regressed against `SleepReplaySampler.draw_region_counts()[region]` at fixed waking evidence.
A positive relation is the code's expected arithmetic, so on its own it measures nothing -- it
becomes a result only against the paired arm the substrate cannot currently supply (a veridical
genealogy that suppresses the repeat). **Single-arm, no comparator. This is why the proposed
claims are `substrate_conditional` and not `standard`.** Recorded so a later session does not
mistake the instrumented count for a ready experiment.

---

## 8. Next steps

**Registration debt (the largest finding).** Twelve planning artifacts, four executed probe
results and four probe scripts exist for this branch and NOTHING is in `claims.yaml`. The same is
true of the convergence assays 001-006 that seeded it. Routing this to `/governance` as a
registration-debt item is more valuable than any single claim proposed here.

**Literature to pull.**
1. A dedicated judgment/testimony/redundancy-neglect tranche. The supplement's section 13 debt 3
   says the C3 class "was not exhaustively swept -- this audit located it by targeted query against
   a specific wrong row in the evidence map".
2. Whether the consensus-illusion paradigm has ever been run in psychosis or delusion-proneness.
   The supplement searched and located nothing; it calls this "the most direct empirical test of the
   reframed question".
3. Circular-inference models of schizophrenia, for the section-13 comparison the thought itself
   defers. Not done anywhere in the branch.
4. Replication status of Moritz et al. 2012 (PMID 22683551), the only clinical repetition-belief
   bridge located, which the supplement calls methodologically weak.

**Version routing.** All five proposed entries: `implementation_phase: v4`, `version_relevance:
v4_v5`. None is V3-buildable: the genealogy substrate is absent, and the two candidate V3
observation points are (a) an aggregator that is default-OFF and has no comparator arm, (b) a
waking replay path whose output is discarded.

**Threads pending a closer check by a later session.**
- MECH-094's stored call-site enumeration is stale relative to the current tree (section 4a).
- MECH-275's claim-vs-implementation aggregation-unit mismatch (audit row 12) -- episodes in the
  claim, replay draws in the code.
- `substrate_queue.json` `mech092-replay-consumer-missing` is `proposed_REGISTRATION_ONLY`, is
  cited by four claims, and has no queue entry. It gates the thought's entire section 12.
