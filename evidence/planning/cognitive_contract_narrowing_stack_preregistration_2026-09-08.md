# Pre-registration: emergent cognitive contract under narrowing multi-consumer compression

**Date frozen:** 2026-09-08  
**Amended:** 2026-09-16T14:04:22Z -- Amendment 1 (s.24): capacity/rate added as a second independent factor, new capacity-matched nuisance arm F. Sections 4, 5, 8, 11, 18, 22 must be read subject to s.24; nothing above s.24 is rewritten.  
**Status:** pre-registered experiment design / planning artefact; **not queued, not architecture, not a build instruction**  
**Parent programme:** ARC-142 / GOV-CONTRACT-1 / MECH-545  
**Evidence basis:** `cognitive_contract_literature_pull_2026-09-08.md`, tranche 2, tranche 3  
**Related external positive-control literature:** Webb et al. 2024 relational bottleneck; Campbell & Cohen 2024 dimensional abstraction  
**Target substrate:** `Latent-Fields/ree-v3`, but the first stages are deliberately offline/auxiliary and must not alter the canonical organism.

---

## 1. Question

When representational capacity becomes progressively constrained, do relations that are useful to **multiple heterogeneous cognitive consumers** survive preferentially and converge toward a small, transferable relational basis — without those relations being supplied as labels during training?

The strong REE hypothesis is not merely that a bottleneck compresses.

It is:

> **A sufficiently constrained multi-consumer hierarchy can discover an invariant-preserving cognitive contract because the information useful across heterogeneous prediction, memory, control and valuation operations is preferentially retained as representation-specific detail is discarded.**

This is stronger than the ordinary Information Bottleneck claim and different from an imposed relational bottleneck. The imposed relational-bottleneck literature is therefore used as a **positive control**, not imported as REE architecture.

---

## 2. Why the current V3 substrate makes this testable

The live V3 implementation already contains the relevant structural ingredients, but this pre-registration does **not** assert that the current stack already implements the proposed contract.

`ree_core/latent/stack.py` currently defines:

```text
body_obs  -> z_self
world_obs -> z_world
(z_self + z_world) -> z_beta -> z_theta -> z_delta
```

with top-down projections back toward the split encoders. Its module contract documents heterogeneous consumers: E1 reads `z_self + z_world`; E2 operates primarily over the self/action-prediction domain; E3 and hippocampal/residue machinery consume world/action-relevant representations. The shared stack also maintains separate precision tensors for `self`, `world`, `beta`, `theta`, and `delta`.

This is already enough to define **representation taps and downstream tasks**. It is not enough to claim emergence: the existing dimensions and objectives were not designed as this experiment, and current `beta -> theta -> delta` widths must not be retroactively interpreted as a successful narrowing hierarchy.

A reusable `shared_latent_gradient_probe` also already exists in `ree-v3`; it measures whether multiple module losses are genuinely coupled to a shared latent and whether their gradients are net-conflicting. This should be reused as a preflight/readiness metric rather than reimplemented.

---

## 3. Contamination firewall

The central protection of this experiment is that **candidate cognitive invariants are held out from training**.

### During training, prohibited targets include

- identity / same-token labels;
- same/different or similarity labels;
- temporal-order labels supplied as semantic annotations;
- provenance / perceived-vs-imagined / remembered labels;
- agency / controllability labels;
- candidate/actual/counterfactual/committed labels;
- negation / absence labels;
- linguistic or Natural Semantic Metalanguage labels;
- any hand-written "cognitive contract" vector.

Task losses that naturally require prediction, reconstruction, control, sequence memory, harm/benefit processing, etc. are allowed. Environment state may of course determine ordinary training targets when that target is already part of the task; it may not be repackaged as one of the held-out candidate contract labels solely to make the representation encode it.

### After training

The frozen candidate ledger is opened and independent probes ask whether the candidate relations are recoverable. The post-hoc probe code may see labels; the trained bottleneck may not.

### Language remains sealed until the geometry analysis is frozen

Natural Semantic Metalanguage / grammatical comparisons are performed only **after** the latent analyses and candidate decompositions have been committed. Language is an exam paper, not a teacher.

---

## 4. Experimental regimes

Use matched data, seeds, optimiser budget and approximately matched parameter budgets wherever architecture permits.

### A — wide shared-capacity control

A representation with enough width that meaningful compression pressure is minimal.

Purpose: establish the downstream-performance ceiling and determine which held-out relations are present anywhere in the source representation.

### B — width-only narrowing

Progressively reduce latent width while optimising an otherwise generic reconstruction/prediction objective.

Purpose: test the weak claim that narrowing alone is sufficient.

### C — single-consumer narrowing control

Narrow to the same widths as B/E, but optimise the bottleneck for **one downstream consumer at a time**.

Purpose: determine whether any relational structure that appears is simply the sufficient statistic of one task rather than a cross-consumer contract.

### D — imposed relational-bottleneck positive control

Use a relation-selective architecture inspired by Webb et al. (2024): downstream reasoning is restricted primarily to relations between inputs rather than unrestricted object attributes.

Purpose: demonstrate that the assay can detect the expected relational/factorised signature when a relational inductive bias is deliberately imposed.

This arm **must not** be used to infer that REE should adopt the relational bottleneck. It validates the measurement pipeline.

### E — unlabeled multi-consumer narrowing: the REE hypothesis arm

The compressed representation must support several heterogeneous downstream consumers simultaneously, with no candidate-invariant supervision.

At minimum, select consumers from distinct functional families available in V3:

- persistent state / next-state prediction (E1-like requirement);
- action-conditioned forward prediction / counterfactual rollout (E2-like requirement);
- sequence/trajectory retrieval or hippocampal prediction;
- trajectory scoring / selection / commitment-relevant readout (E3-like requirement);
- harm/resource/viability-relevant readout;
- reconstruction into at least two representational spaces rather than one decoder only.

The exact callable losses are frozen during the Stage-0 substrate audit below. If fewer than three genuinely distinct consumers can be constructed without inventing new semantic labels, the E arm is **substrate_not_ready**, not silently weakened.

---

## 5. Width schedule

Use width as an independent variable rather than choosing one bottleneck size after looking at results.

Preferred schedule, expressed as fractions of the unconstrained source width:

`1.00, 0.75, 0.50, 0.25, 0.125`

with integer rounding declared before runs. If the source representation is too small for a meaningful 0.125 arm, replace the last point with the smallest dimension >= 4 and record the deviation before training.

For a genuinely hierarchical version, instantiate monotonically non-increasing stages. Do not assume the live V3 dimensions currently satisfy this condition; the hierarchy belongs to the assay harness until evidence justifies an architectural change.

---

## 6. Stage 0 — substrate and trace audit

Before any new training:

1. freeze the exact `ree-v3` commit SHA;
2. enumerate available latent taps (`z_self`, `z_world`, `z_beta`, `z_theta`, `z_delta`, and any optional harm/resource/goal/status streams actually present in the selected run);
3. enumerate which V3 recordings already persist those taps and the ground-truth/environment variables needed **only for later probes**;
4. enumerate candidate downstream losses that can be reconstructed from current code without adding contract labels;
5. run `shared_latent_gradient_probe` or an equivalent existing readiness readout for the proposed E-arm consumers;
6. report any consumer with zero coupling or net-negative gradient conflict;
7. decide whether the assay can begin offline from recordings, requires a fresh instrumentation run, or is substrate_not_ready.

Missing traces are not back-filled from downstream labels. A missing latent tap triggers fresh recording or omission declared before training.

---

## 7. Stage 1 — retrospective/offline geometry audit (can be done without changing REE)

This stage asks what the current organism already represents before adding any bottleneck.

On frozen trajectories:

- estimate effective rank / participation ratio of each latent tap;
- measure covariance/eigenspectrum and representational drift across episodes/checkpoints;
- train held-out linear probes for the candidate relations where clean labels exist;
- train a controlled nonlinear probe only when linear decodability fails, to distinguish absent information from non-linearly exposed information;
- test cross-environment and cross-schema generalisation of each probe;
- compare absolute-state decoding against relational/transition decoding;
- quantify pairwise representational similarity only as a descriptive metric, not as evidence of shared meaning.

**Key distinction:** `encoded but not exposed` is not equivalent to absent. Linear failure plus nonlinear success is recorded separately.

This stage can falsify the need for parts of the later experiment if the current stack already shows no information from which a candidate could possibly be recovered.

---

## 8. Stage 2 — frozen-source auxiliary bottlenecks

Use frozen recorded source representations. Train A–E bottleneck/decoder systems **outside** the live REE agent.

Advantages:

- no effect on organism behaviour or learning;
- cheap width sweeps;
- exact same source data for every arm;
- easy multi-seed replication;
- held-out probes remain uncontaminated;
- negative results are interpretable before expensive end-to-end runs.

This is the preferred first direct test of the narrowing-stack hypothesis.

---

## 9. Stage 3 — end-to-end experimental arms

Only if Stage 2 gives a non-degenerate signal should the bottleneck be made trainable with the upstream representation.

Rules:

- isolate in an experiment arm / feature flag; do not replace the canonical latent stack;
- preserve a bit-identical or functionally verified OFF path;
- record all dimensions, consumers, loss weights and seeds in the manifest;
- monitor gradient coupling/conflict throughout training;
- do not tune widths after inspecting held-out invariant probes;
- do not add candidate labels to rescue a negative result.

---

## 10. Held-out probe families

These are frozen **before** E-arm training and are never optimisation targets.

### Tier-1 candidate probes

1. token continuity / identity;
2. equivalence / similarity;
3. transition topology / reachability / successor structure;
4. temporal order / persistence;
5. source / ownership / provenance;
6. branch / obtaining / update status;
7. causal-control relation;
8. epistemic confidence / precision.

### Tier-2 exploratory probes

9. expected absence / non-obtaining;
10. ordered magnitude / comparison;
11. viability/preference relation.

### Composite-vs-factorial comparison probes

Compare recovery/generalisation of coarse labels:

- perception;
- memory;
- imagination;
- prediction;
- agency;
- goal;
- commitment;

against their proposed factorial basis (source + time + branch/update + causal/control + value/viability + confidence).

The factorial account wins only if its components generalise at least as well across contexts and reconstruct the coarse labels without materially worse held-out performance.

---

## 11. Probe construction rules

To reduce probe-induced false positives:

- primary probe = regularised linear model with hyperparameters selected on training/validation only;
- evaluate on held-out episodes **and** a relationally preserved but surface-remapped environment where available;
- report balanced accuracy/AUROC for categorical variables and held-out R2 / rank correlation for continuous variables;
- nonlinear probe is a diagnostic secondary analysis, capacity-matched across representations;
- random-label probes provide a leakage floor;
- dimensionality-matched random projections provide the MECH-545 / INV-105 comparison floor;
- nuisance probes (e.g. surface-specific features not needed by the downstream tasks) test whether compression really discards particulars;
- all probe targets must have an explicit generator from environment/trace state rather than manual annotation after inspecting embeddings.

---

## 12. Relational-topology primary assay

Because tranche 3 yields the strongest cross-domain case for predictive relational topology, pre-register it as the first primary relation.

For pairs/states `i,j`, derive from the environment or trajectory corpus:

- one-step adjacency;
- action-conditional transition likelihood where available;
- short-horizon reachability;
- successor-like occupancy similarity or an empirically estimated analogue.

Ask whether these are recoverable from bottleneck geometry under a surface/schema remap.

A representation does **not** receive credit merely for encoding absolute position if the relation can no longer be recovered when object identity, texture, orientation or another irrelevant surface feature changes.

---

## 13. Multi-consumer emergence outcomes

### Result supporting the strong hypothesis

E preserves cross-context/cross-schema relational probes significantly better than B and C at matched width/downstream utility, and approaches D's relational/factorised signature **without relation labels**.

### Result supporting only generic compression

B ~= E on held-out relational retention and transfer.

Interpretation: narrowing explains the result; multi-consumer pressure is unnecessary.

### Result supporting imposed relational bias but not spontaneous emergence

D shows the expected signal but E does not.

Interpretation: relations are useful, but the proposed objective pressure is insufficient; a relational inductive bias may be needed.

### Assay failure / invalidity

D fails to produce the expected relational signature.

Interpretation: measurement pipeline is not sensitive enough; do not interpret E's null.

### Result against the current hypothesis

E preferentially preserves task-specific particulars, fails to converge across seeds/environments, or relational retention is no better than matched random/nuisance baselines once downstream utility is controlled.

Interpretation: the upper-stack emergent-contract hypothesis is not supported in its present form.

---

## 14. Cross-seed and cross-schema convergence

The claim concerns relations, not neuron identities.

Therefore do **not** require corresponding latent dimensions across seeds.

Instead test whether independently trained representations support equivalent relational structure up to a learned invertible/low-complexity mapping:

- held-out cross-decoding;
- orthogonal Procrustes / linear alignment as descriptive controls;
- relation-distance correlation;
- subspace principal angles for probe-relevant directions;
- bridge complexity needed to transfer a probe or decoder between seeds.

A genuine candidate contract should survive surface/schema remapping more reliably than low-level particulars.

---

## 15. Factorisation and "representation of the representational system"

The user's stronger hypothesis predicts that as capacity falls, upper representations increasingly encode **how a state is represented** rather than only what particular state is present.

Operational test:

- train probes for CONTENT-specific variables and for META-RELATIONAL variables (source, time, branch/update status, controllability, confidence);
- track their normalised retained decodability as width decreases;
- test whether meta-relational variables become relatively enriched at narrow widths in E more than B/C;
- determine whether coarse modes (memory/perception/imagination/prediction) become reconstructible as combinations of those meta-relational axes.

Evidence for "representation of the representation system" requires relative enrichment **plus cross-content generalisation**. A source-status probe that works only for one stimulus class does not qualify.

---

## 16. Value versus viability fork

Do not train a held-out `VALUE` axis.

Compare two post-hoc models:

### H1 — signed-value basis

A compact signed evaluative coordinate survives narrowing and predicts harm/benefit and action tradeoffs across contexts.

### H2 — viability/preference basis

The narrow representation preserves distance/direction relative to viable/preferred state regions or homeostatic constraints, from which signed value can be reconstructed as change in drive/preference satisfaction.

Evidence favouring H2: viability/homeostatic relational probes transfer better across resource/harm rescalings than a scalar value probe while still reconstructing behavioural preference.

This test is especially important because REE's ethical harm/benefit machinery can remain operationally indispensable even if scalar `VALUE` is not a substrate-neutral contract primitive.

---

## 17. Acute lesion versus compensation-aware lesion

A relation that is currently load-bearing may be recoverable after adaptation through a different internal route. Therefore every important lesion has two phases.

### Acute boundary lesion

Remove/scramble the probe-defined relation at translation time with weights frozen.

Question: **does the present solution depend on this relation?**

### Adaptation / compensation phase

Permit a predeclared amount of retraining while keeping the lesion in place.

Question: **can the organism realise the same function through another representation/pathway?**

Record:

- target deficit;
- collateral deficits in all other consumers;
- whether another latent/subspace increases its representation of the missing relation;
- recovery trajectory and final residual deficit;
- whether recovery preserves downstream behaviour but changes internal strategy.

A recovered function is not evidence that the original relation was irrelevant. It is evidence of **multiple realizability / compensation** and must be reported separately from the acute necessity result.

Matched controls:

- same-dimensional random subspace lesion;
- magnitude-matched noise lesion;
- shuffled-label targeted erasure;
- sham lesion.

This is the operational extension of MECH-545: lesion the boundary relation, not the underlying content, while measuring the lesion's other impacts rather than assuming a one-function-one-mechanism mapping.

---

## 18. Pre-registered primary comparisons

The experiment should avoid one opaque "cognitive contract score" as the sole endpoint.

Primary comparisons:

1. **E vs B:** cross-schema relational-topology retention at matched width and downstream utility;
2. **E vs C:** relation retention and number of consumers supported at matched width;
3. **E vs D:** degree to which unlabeled multi-consumer pressure approaches the imposed relational positive-control signature;
4. **meta-relational vs content retention slope:** change in normalised held-out decodability across width, E vs B/C;
5. **factorial vs coarse-mode generalisation:** source/time/branch/control basis versus PERCEPTION/MEMORY/IMAGINATION/PREDICTION labels;
6. **acute targeted lesion vs matched random lesion:** invariant-specific behavioural/consumer dissociation;
7. **acute vs adapted lesion:** necessity versus compensability.

All other analyses are secondary/exploratory unless frozen by an amendment **before** results are inspected.

---

## 19. Minimum seed and replication posture

This pre-registration does not fix a power number before Stage 0 exposes variance and compute cost.

It does fix the rule:

- no single-seed architectural conclusion;
- Stage 2 must include enough independent seeds to estimate between-seed variance before any end-to-end Stage-3 claim;
- seed count is frozen from a variance/power estimate using only training/validation metrics or a pilot dataset separated from the final held-out test;
- final held-out environments are not used to choose seed count, widths, loss weights or probe classes.

---

## 20. Stop/go gates

### Gate G0 — trace readiness

Required taps and >=3 distinct consumers are available; otherwise substrate_not_ready.

### Gate G1 — positive-control validity

D exhibits a detectable relational/factorised signature; otherwise measurement_not_ready.

### Gate G2 — offline signal

E shows a non-trivial E-vs-B/C relation-retention difference on frozen-source data. If absent, do not spend compute on Stage 3 unless a specific assay defect is identified and amended blind to final held-out results.

### Gate G3 — end-to-end reproducibility

E's signal replicates across seeds and a schema/surface remap.

### Gate G4 — causal necessity

Targeted acute relation lesions produce predicted, relation-specific deficits exceeding matched random lesions.

### Gate G5 — compensation classification

Recovered versus non-recovered functions are classified separately; neither overwrites the acute result.

---

## 21. What is deliberately not decided here

- whether REE should adopt a relational bottleneck;
- the final cognitive-contract primitive set;
- whether `z_delta` or any existing named latent is "the" contract;
- whether current V3 stack widths should be changed;
- whether value is primitive or derived;
- whether confidence should be a content field or control-plane quantity;
- whether this belongs permanently in V3, V4 or a later substrate.

Those are outputs of evidence/governance, not assumptions of the assay.

---

## 22. Pre-results prediction table

| Observation | Interpretation |
|---|---|
| E > B and E > C; E approaches D | supports emergent multi-consumer contract |
| E ~= B | generic narrowing sufficient; reject special multi-consumer claim |
| D > E, D valid | relation bias useful but not spontaneously discovered under present pressure |
| D invalid/null | assay not sensitive; no conclusion about E |
| narrow E retains nuisance particulars over transferable relations | evidence against current contract-emergence hypothesis |
| factorial status axes transfer better than coarse mode labels | supports representation-of-representation-system account |
| coarse labels outperform factorial basis cross-context | weakens proposed decomposition |
| viability basis transfers better than signed value | supports value-as-derived H2 |
| signed value survives more invariantly than viability basis | supports H1 |
| targeted acute lesion deficit but adapted recovery | relation load-bearing but compensable / multiply realisable |
| no acute deficit beyond random lesion | strike/demote candidate relation for that boundary |

---

## 23. Freeze statement

The hypotheses, held-out candidate families, A–E arm logic, primary comparisons and interpretation table above are frozen **before** a cognitive-contract-specific narrowing experiment is run. Amendments are allowed only if timestamped and justified before the affected result is inspected.

The experiment is explicitly permitted to tell us that the attractive idea is wrong.

---

## 24. Amendment 1 — capacity is a second independent factor, and a capacity-matched nuisance arm

**Amendment timestamp (UTC):** 2026-09-16T14:04:22Z
**Amendment status:** made under the s.23 freeze clause, **before any arm has been run and before any result of this pre-registration has been inspected**. Verified at amendment time: `ree-v3/experiment_queue.json` contains no cognitive-contract / narrowing / `CCI-*` entry, and `REE_assembly/evidence/experiments/` contains no run against this pre-registration (the only `*narrow*` hit, `v3_exq_810b_arc071_mech323_seed202_narrow_repertoire_probe`, belongs to ARC-071 / MECH-323 and is unrelated).
**Justification source:** `REE_assembly/evidence/planning/thought_intake_2026-09-08_candidate_cognitive_invariants.md` s.8 (implementation-gap audit, row 2) and s.9.1, ingesting `REE_assembly/docs/thoughts/2026-09-08_candidate_cognitive_invariants.md` s.13 and s.20.6.
**Substrate SHAs:** gap audit verified against `ree-v3` `9d3a7a4` (2026-09-15); independently re-confirmed against `ree-v3` `c7ba953` (2026-09-16). Stage-0 audit pinned at `8e57e473` (2026-09-08).

**Nothing above is rewritten.** Sections 4, 5, 8, 11, 18 and 22 remain as frozen on 2026-09-08 and are to be read **subject to** this section.

### 24.1 The defect this amendment corrects

The frozen design makes **width** the sole independent capacity variable (s.5; regime B is literally titled "width-only narrowing"). That is not an information bottleneck. As the source thought puts it at s.13:

> fewer nodes is not by itself an information bottleneck

A small number of *unconstrained continuous* variables can carry arbitrarily much information. A width-only narrowing stack therefore cannot, on its own, test the ARC-142 / MECH-545 hypothesis that *capacity pressure* preferentially retains cross-consumer-useful relations: a null result would be uninterpretable (no pressure was applied) and a positive result would not be attributable to compression.

This is a defect in the **pre-registration**, not only in the substrate. It is corrected here rather than at analysis time precisely because the window is still open.

### 24.2 Capacity (rate) is added as a SECOND independent factor, orthogonal to width

Width is retained exactly as frozen in s.5 and is **not** replaced. A new factor is added:

**R — achieved rate**, an explicit, measured, per-step information budget at the bottleneck, reported in **nats per step**.

**Primary operationalisation (declared before any run):** a Gaussian channel at the bottleneck with a variational rate term; the achieved rate is the measured KL of the posterior to the prior, and the target rate is held at a declared budget by dual ascent on the rate constraint (a Lagrangian rate-targeting controller), not by a hand-tuned fixed beta.

**Pre-declared fallbacks, in this order, to be used only if the primary is unstable and only with the substitution recorded before held-out probes are inspected:**

1. uniform scalar quantisation of the bottleneck at declared bit depths (exact rate ceiling, no controller);
2. additive Gaussian channel noise at declared SNR with the rate computed analytically per dimension.

Entropy/sparsity/activity-budget penalties are **diagnostics only** under this amendment: they constrain rate only indirectly and their achieved rate is not directly measurable, so they may not serve as the matching variable in s.24.3.

**Rate ladder**, expressed — as s.5 does for width — as fractions of an unconstrained source rate `R0`:

`1.00, 0.50, 0.25, 0.125, 0.0625` x `R0`

`R0` is the achieved rate of the unconstrained arm-A bottleneck at width fraction 1.00, measured during Stage 0 / Stage 2 **before any held-out invariant probe is inspected**. If the primary controller cannot hold a ladder rung within the tolerance of s.24.3, that rung is recorded as **not attained** and its comparisons are declared invalid rather than reported at the nominal budget.

**Reporting rule:** every arm reports its **achieved** rate, never only its nominal budget. Arms are compared on achieved rate.

### 24.3 Design: the (width x rate) grid is deliberately NOT run on the diagonal

Sweeping width and rate together is the confound this amendment exists to remove. The pre-declared fractional design is:

1. **Rate sweep at fixed width** (width fraction 1.00, the full rate ladder) — isolates rate.
2. **Width sweep at fixed rate** (rate unconstrained, the full s.5 width ladder) — this is the existing frozen s.5 schedule, now explicitly re-read as the *width-only* factor rather than as "the capacity variable".
3. **Interaction cells:** width fractions {1.00, 0.25} x rate fractions {1.00, 0.125}, four cells, for the width x rate interaction test.

The full cross-product is **not** pre-registered; extending beyond these cells requires a further timestamped amendment before the affected result is inspected.

**Capacity-matching tolerance:** two arms are "capacity-matched" only if their achieved rates agree within **+/-5% in nats** and their widths are identical. A comparison whose arms fall outside that tolerance is reported as **matching_failed** and does not contribute to any primary comparison.

### 24.4 New arm F — capacity-matched nuisance / random-relation control

The frozen design has nuisance *probes* (s.11) but no nuisance *arm*. Thought s.13 condition F is added here as a sixth arm. **Arm letters A-E are NOT re-lettered** (see s.24.5); F is a new letter in this pre-registration's own letter-space.

**F — capacity-matched nuisance/random-relation control.** Identical to arm E in width, achieved rate (within the s.24.3 tolerance), data, seeds and optimiser budget, differing **only** in its downstream consumer targets, which are replaced by:

- surface-specific nuisance features not required by any real downstream task (the same generator family as the s.11 nuisance probes), and
- randomly generated but fixed-per-seed relational targets over the same pair/state index set used by the s.12 relational-topology assay.

**Purpose:** F asks whether the *assay pipeline plus capacity pressure* manufactures a relational signature regardless of what the consumers actually need. It is a control on the measurement, in the same sense that D is a positive control on the measurement.

**Falsifier this arm supplies:** if **F reproduces E's relation-retention signature at matched capacity and width**, then the E-vs-B and E-vs-C results do **not** support emergent multi-consumer contract formation — the signature is attributable to rate pressure plus probe pipeline, not to cross-consumer utility. This outcome **strikes** the primary interpretation of comparisons 1 and 2 in s.18, and no amount of E > B margin rescues it.

### 24.5 Letter-collision warning (must be read before citing either document)

The source thought's condition letters at s.13 do **not** match this pre-registration's arm letters, and two of them are transposed. This mapping is authoritative:

| Thought s.13 condition | This pre-registration's arm | Note |
|---|---|---|
| A wide / weakly constrained control | **A** wide shared-capacity control | same |
| B width-narrowed only | **B** width-only narrowing | same |
| C true rate-constrained single-consumer bottleneck | **C** single-consumer narrowing control | this prereg's C becomes rate-constrained under s.24.2 |
| D true rate-constrained multi-consumer, unlabeled | **E** unlabeled multi-consumer (the REE hypothesis arm) | **TRANSPOSED** |
| E relation-supervised bottleneck, positive control | **D** imposed relational-bottleneck positive control | **TRANSPOSED** |
| F capacity-matched nuisance/random-relation control | **F** (new, s.24.4) | same |

The s.18 primary comparisons and the s.22 prediction table are written in **this pre-registration's** letters and are unchanged. A citation that reads "condition D is the important one" (thought s.13) refers to **arm E** here.

### 24.6 Arms B and C are re-scoped by the new factor; A, D, E are not

- **B (width-only)** keeps its frozen meaning and becomes the *rate-unconstrained* level of the new factor. Its purpose is unchanged: test whether narrowing alone suffices. Under this amendment, B is no longer a candidate bottleneck arm — it is the **negative control for rate**.
- **C (single-consumer)** and **E (multi-consumer)** are run **rate-constrained** per s.24.2 in the rate sweep and interaction cells, and rate-unconstrained in the width sweep. The frozen E-vs-C comparison (s.18 item 2) is now evaluated at matched achieved rate as well as matched width.
- **A, D** are unchanged; D's imposed relational bias is orthogonal to the rate factor and D is run at the same declared cells as E.

### 24.7 The substrate supplies no rate machinery — an auxiliary-harness implementation is MANDATORY

Recorded per intake s.8 row 2, verified by direct code read at `ree-v3` `9d3a7a4` and re-confirmed at `c7ba953`: searching `ree_core/` for `kl_div`, `KL(`, `variational`, `logvar`, `quantiz`/`quantis`, `vector_quant`, `sparsity`, `l1_penalty`, `activity_budget`, `rate_penalty`, `entropy_reg`, `add_noise`, `noise_std`, `gaussian_noise` yields **zero latent-capacity hits**. The two incidental hits are a fixed unlearned region-code discretisation of `z_world` for policy decomposition (`ree_core/policy/policy_decomposition.py`) and comments in the amygdala attribution head recording that a sparsity penalty was **removed** for outweighing its objective (`ree_core/amygdala/attribution_head.py`) — neither is a representational-capacity term.

Consequences, binding on any session that executes this design:

1. The rate machinery of s.24.2 **must** be built in the Stage-2 auxiliary harness (s.8), outside the live agent. This is not optional and not a deficiency to be worked around by reporting width as capacity.
2. `ree_core/**` **must not** be modified to satisfy this pre-registration. s.9's rules (feature-flagged arm, bit-identical OFF path) continue to govern any eventual Stage-3 work, and Stage 3 remains gated on a non-degenerate Stage-2 signal.
3. Because there is no existing rate term to reuse, the harness's rate measurement **must** be validated against a known-rate synthetic source before any arm is trained — a channel whose true rate is analytically known, recovered to within the s.24.3 tolerance. A harness that cannot recover a known rate cannot capacity-match, and therefore cannot run arm F.

### 24.8 Amendment to s.18 — additional pre-registered primary comparisons

Added, frozen as of this amendment's timestamp and before any result is inspected:

8. **E vs F:** relation retention at matched width **and** matched achieved rate. This is the load-bearing control on comparisons 1 and 2 (s.24.4).
9. **rate slope vs width slope:** change in normalised held-out relational decodability per nat of achieved rate removed, versus per unit of width removed, arms E and B. Tests whether the retention effect tracks *information* or merely *dimension*.
10. **width x rate interaction** over the four s.24.3 interaction cells: whether width reduction adds retention pressure beyond the rate it removes.

### 24.9 Amendment to s.22 — additional pre-results prediction rows

| Observation | Interpretation |
|---|---|
| E > B and E > F at matched achieved rate and width | supports emergent multi-consumer contract; the signature is not a pipeline artefact |
| **F ~= E at matched capacity** | **strikes the primary interpretation of s.18 comparisons 1 and 2**: signature attributable to rate pressure + probe pipeline, not cross-consumer utility |
| retention tracks achieved rate but not width, at fixed rate | capacity pressure is the operative variable; the frozen width-only framing was the defect this amendment corrects |
| retention tracks width but not achieved rate, at fixed width | unexpected; dimension per se matters and the information-bottleneck framing of ARC-142 / MECH-545 is wrong as stated |
| no rung of the rate ladder attained within tolerance | **matching_failed**: no conclusion about capacity; report the controller failure, do not fall back to reporting width as capacity |
| harness cannot recover a known synthetic rate (s.24.7 item 3) | assay invalid; arm F may not be run and no capacity claim may be made |

### 24.10 What this amendment does NOT change

- The contamination firewall (s.3) and the language seal are unchanged and apply to arm F exactly as to arm E. F's random relational targets are generated from environment/trace state or from a seeded RNG, never from the held-out candidate ledger.
- The s.10 held-out probe families, the s.12 relational-topology primary assay, s.14-s.17, s.19 replication posture and s.20 stop/go gates are unchanged.
- s.21 ("what is deliberately not decided here") is unchanged: this amendment does **not** decide that REE should acquire a rate term. It decides only that the *assay* must apply measurable capacity pressure in order to bear on the question at all.
- No claim in `claims.yaml` is altered by this amendment; routing of ARC-142 / MECH-545 dispositions remains `/governance`'s.
