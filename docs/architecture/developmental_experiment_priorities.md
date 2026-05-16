---
nav_exclude: true
---

<!-- version: 2026-05-16.1 -->
<!-- author: claude-sonnet-4-6, session developmental-experiment-priorities-2026-05-16T144101Z -->

# Developmental Experiment Priorities

**Date:** 2026-05-16  
**Cross-references:** [`developmental_needs_register.md`](developmental_needs_register.md) | [`developmental_curriculum.md`](developmental_curriculum.md) | [`developmental_metrics.md`](developmental_metrics.md) | [`infant_substrate_expansion.md`](infant_substrate_expansion.md) | [`replay_development_analysis.md`](replay_development_analysis.md)  
**Status:** Planning document — not a registered claim. Informs experiment queue decisions and session governance.  
**Governing principle:** Optimise for developmental understanding, not short-term PASS count.

---

## 1. Executive Summary

The dominant bottleneck as of 2026-05-16 is the **cold-start warm-start failure** (DEV-NEED-029): all
ARC-065 diversity mechanisms (MECH-313 noise floor, MECH-314 structured curiosity, MECH-320 tonic vigor)
produce zero differential on a cold-start substrate because the ResidueField, EWMA, and E3 score variance
are all near-zero. EXQ-573 confirmed this: 10x bias scale sweep produced bit-for-bit identical arms.
The same floor blocks INV-049 sleep consolidation tests, Q-043/044/045 behavioral ablations, and every
replay diversity experiment currently proposed.

**The highest-leverage action is not to run more behavioral experiments on the existing substrate.
It is to enrich the infant substrate so the warm-start gate (DEV-NEED-029) becomes passable.**

Once the warm-start gate is established, the experiment sequence becomes:
1. Confirm warm-start via EXQ-ISEF-001/002/003/004 (substrate validation series)
2. Re-run Q-043/044/045 ARC-065 behavioral ablation on warm substrate
3. Run EXQ-IDEV-001 (longitudinal replay quality), EXQ-IDEV-006 (SD-017 functional validation)
4. Queue sleep aggregation cluster (MECH-272/273/275/285) only after SD-017 functional test PASSes

---

## 2. Current State Assessment

### 2.1 FAIL Pattern Analysis

The recent FAIL cluster falls into three mechanistically distinct groups:

| FAIL group | Representative experiments | Root cause | Correct response |
|---|---|---|---|
| **Cold-start warm-start** | EXQ-573 (10x bias sweep), EXQ-549 (MECH-320 discriminative), EXQ-552 (forced warmup), EXQ-553 (orthogonal CEM) | Diversity mechanisms require warm substrate; infant is cold-start by definition | Infant substrate enrichment (EXQ-ISEF-001..005) before any diversity behavioral test |
| **Monostrategy basin** | EXQ-550 (z_goal falsifier), EXQ-554 (decoder collapse), EXQ-555/557 (seed sweep), EXQ-556 (module swap) | CEM proposer collapses to single strategy; seed-dependent (some seeds escape) | SD-055 differentiable CEM (substrate-readiness PASS EXQ-568); ARC-062 Phase 3 wiring; microhabitat zones |
| **Substrate ceiling** | EXQ-530/530c (ARC-016 precision commit), EXQ-532 (SD-005 latent domain), EXQ-537-537d (SD-029 self-attribution) | Claim requires substrate capabilities beyond current V3 baseline | Hold pending substrate enrichment; do not re-queue under same conditions |
| **Methods-valid but function-unproven** | EXQ-265/265a PASS (SD-017 phase infrastructure), EXQ-563c PASS (CEM bias calibration) | Substrate method works; behavioral discriminative test not yet run | Queue functional validation experiments in dependency order |

### 2.2 PASS Pattern Analysis

The recent PASS cluster is concentrated in two categories:

1. **Substrate-readiness probes** (EXQ-540c, EXQ-542, EXQ-544, EXQ-545, EXQ-546, EXQ-547, EXQ-548,
   EXQ-559/559a, EXQ-560, EXQ-561, EXQ-563..563c, EXQ-564, EXQ-565, EXQ-566, EXQ-567, EXQ-568):
   The substrate machinery is landing successfully. This is real progress — infrastructure is in place.
   But infrastructure PASSes do not count as behavioral evidence.

2. **Diagnostic probes** (EXQ-551/551a pipeline entropy, EXQ-555 seed factorization, EXQ-557/558 seed
   sweep): These correctly localise the monostrategy cliff to the CEM proposer stage and establish
   that the basin is large but not universal. This is the right scientific methodology.

**Interpretation:** The substrate is richer than six months ago, but behavioral tests on it remain
consistently blocked by the cold-start problem. The PASSes are building the correct machinery;
the FAILs are correctly diagnosing what machinery is not yet sufficient for discriminative tests.

### 2.3 Monostrategy Characterisation (as of 2026-05-16)

From EXQ-551/551a (pipeline entropy), EXQ-555 (2x2 env/agent seed), EXQ-557 (30-cell agent sweep),
EXQ-558 (seed-pair rank):

- Entropy cliff is at the **CEM proposer stage** (not decoder, not E3 scoring, not environment)
- The collapse is **agent-init-dependent** (some seeds escape with action_class_entropy ~0.68;
  seeds 42/17 collapse to 0.0)
- The collapse is **not attributable to a single submodule** (EXQ-556 module-swap FAIL)
- SD-054 bipartite layout (EXQ-548 PASS) provides 1.27x structural divergence uplift but does not
  fully escape the basin
- SD-055 differentiable CEM (EXQ-568 PASS substrate-readiness) is the next proposer-stage fix

This characterises the monostrategy as a **deep attractor in initialization space** that is too
large to escape via parameter perturbations, but escapes via specific init seeds or substrate
enrichment that creates competing attractors. The infant substrate enrichment proposals
(microhabitat zones, harm gradients, transient benefit patches) are designed to reshape the
attractor landscape during training — creating multiple distinct learned attractor zones that
compete for policy dominance.

---

## 3. Literature Evidence Mapping Table

The following table synthesises all seven required lit-pull topics. Topics 5-7 draw from the
existing synthesis in `infant_substrate_expansion.md` and `replay_development_analysis.md`.
Topics 1-4 are from methodological literature.

### 3.1 Experiment Prioritization Under Uncertainty

| Source | Finding | REE relevance | DEV-NEED IDs | Claim IDs | Confidence | Classification |
|---|---|---|---|---|---|---|
| Lindley (1956) Biometrika 43:70 — Bayesian experiment design | Expected information gain (EIG) = expected reduction in posterior entropy. Optimal experiment selection maximises EIG per unit cost | When theory is well-founded but experiments keep failing, EIG of further same-type experiments approaches zero — invest in substrate investigation instead | DEV-NEED-029 | ARC-065, INV-049 | High | suggests experiment (warm-start gate calibration before behavioral tests; EIG near-zero for repeated cold-start diversity tests) |
| Chaloner & Verdinelli (1995) Statistical Science 13:273 — BOED survey | Bayesian Optimal Experimental Design (BOED): prioritise experiments that maximally discriminate between competing hypotheses. When hypotheses make similar predictions under current substrate, discriminative experiments are uninformative | The repeated FAIL pattern (EXQ-385/385a for INV-049, EXQ-537..537d for SD-029) suggests competing hypotheses (theory wrong vs substrate not ready) make identical predictions on current substrate. BOED says: first run the substrate-discrimination experiment | DEV-NEED-029 | INV-049, SD-029 | High | refines existing claim (substrate-validation experiment is the BOED-optimal next step, not theory-test replication) |
| Srinivas et al. (2010) ICML GP-UCB | Upper Confidence Bound (UCB) for sequential experiment selection: balance exploiting known-good conditions (exploit) with testing unexplored substrate regimes (explore). UCB-regret bounds show systematic exploration is required even when exploit looks locally optimal | REE has been in an exploit loop: re-testing claims under conditions known to be substrate-limited. UCB principle: switch to explore (new substrate regime = infant enrichment) when current regime yields zero-information | DEV-NEED-001, DEV-NEED-029 | ARC-065 | 0.85 | suggests experiment (schedule substrate exploration experiments before behavioral exploitation tests) |
| Settles (2012) Active Learning synthesis | Uncertainty sampling: query points where model is most uncertain. Expected model change: query points that would most change the model. In scientific discovery, "model" = theory belief state; "query" = experiment | INV-049 double-FAIL raises genuine uncertainty about whether offline integration matters for this substrate — but the correct query is not "run INV-049 again under same conditions" but "establish whether current substrate can produce the conditions under which INV-049 would be discriminative" | DEV-NEED-007, DEV-NEED-029 | INV-049, ARC-011 | High | suggests experiment (EXQ-IDEV-001 longitudinal replay quality is the active-learning-optimal query for INV-049) |
| Frazier (2018) arXiv:1807.02811 — Bayesian Optimization tutorial | Knowledge gradient: the most valuable next experiment is the one that would most change your decision about which design to deploy. In RL: if you wouldn't change anything after seeing the result, the experiment has zero gradient value | Applied to monostrategy: an experiment that will FAIL regardless of substrate state (because entropy=0 regardless of mechanism state) has zero knowledge gradient. DO NOT queue these until warm-start gate established | DEV-NEED-029 | ARC-065, MECH-313, MECH-314, MECH-320 | High | refines existing claim (blocking constraint: zero KG experiments are waste; warm-start gate is prerequisite for non-zero KG behavioral tests) |

### 3.2 Active Learning for Scientific Discovery

| Source | Finding | REE relevance | DEV-NEED IDs | Claim IDs | Confidence | Classification |
|---|---|---|---|---|---|---|
| Reker et al. (2019) Nature Chemistry 11:895 | Active learning in drug discovery: sequential querying reduces experiments needed 3-5x vs random screening. Key: pool of candidates must be screened for plausibility before querying — uninformative candidates waste the oracle's budget | Analogy: REE oracle = experiment runner (expensive). Uninformative experiments (zero-differential arms on cold-start substrate) consume runner hours with zero evidence gain. Plausibility screening = warm-start gate check before queuing | DEV-NEED-029 | ARC-065 | 0.80 | refines existing claim (warm-start gate IS the plausibility screen for ARC-065 behavioral experiments) |
| Hernandez-Lobato et al. (2017) PMLR 54 — Parallel BOED | Batch query selection under uncertainty: select the most diverse batch of experiments when parallel evaluation is available. Diversity of experiments != diversity of results; need behaviorally-distinct experimental conditions | REE runs experiments in parallel on 5 machines. But recent queued batches have been behaviorally equivalent (all collapse to monostrategy) — the batch is diverse in mechanism flags but not in behavioral regime | DEV-NEED-001, DEV-NEED-005 | ARC-065 | 0.78 | suggests experiment (batch selection criterion: experiments must differ in substrate regime, not just mechanism flag) |

### 3.3 Causal Experiment Design

| Source | Finding | REE relevance | DEV-NEED IDs | Claim IDs | Confidence | Classification |
|---|---|---|---|---|---|---|
| Pearl (2009) Causality Ch.3 — do-calculus | Interventional evidence (do(X)) is strictly stronger than observational evidence. An ablation that removes mechanism X while not controlling for indirect effects of X's removal is confounded — the result cannot be attributed to X specifically | INV-049 ablation (remove sleep = no sleep) also reduces total training steps and removes the offline-integration's indirect effect on E1 update timing. The FAIL may be confounded — need matched-compute control | DEV-NEED-007 | INV-049, SD-017 | High | refines existing claim (INV-049 ablation design must add matched-compute control arm before result is interpretable) |
| Sculley et al. (2015) NIPS — ML Technical Debt | Ablations in large systems accumulate "entanglement debt" — removing feature X changes the effective distribution that feature Y sees, invalidating the ablation's clean interpretation. Multiple ablations accumulated over iterations compound this | REE experiment chains (EXQ-537 -> 537b -> 537c -> 537d SD-029 series) each added a new intervention while inheriting the previous design's substrate assumptions. The FAIL cascade is partly confound accumulation | DEV-NEED-029 | SD-029, ARC-016 | 0.82 | suggests experiment (SD-029 series needs a clean baseline re-run after substrate enrichment, not incremental patch on failed design) |
| Meyes et al. (2019) arXiv:1901.08644 — Ablation Studies survey | Most ablation studies in deep learning fail one or more validity criteria: (a) no random seeds, (b) no comparison to random baseline, (c) ablation evaluated on same data distribution as training. Benchmark: a correct ablation is meaningless unless its discriminative power under the specific substrate is characterised first | DEV-NEED-029 directly addresses criterion (c): ARC-065 mechanisms are evaluated under the same cold-start distribution they were designed to ameliorate — the evaluation domain is the domain where the ablation has zero discriminative power | DEV-NEED-029 | ARC-065, MECH-313, MECH-314, MECH-320 | High | supports existing claim (DEV-NEED-029 warm-start gate IS the Meyes criterion-c check) |
| Imai & Dyk (2004) Political Analysis 12:341 — Causal mechanism identification | Mechanism identification requires both (a) causal identification of the outcome effect and (b) a mediator that correctly represents the proposed mechanism. If the mediator is not operating (e.g. tonic vigor EWMA=0 because substrate is cold), mechanism identification is impossible regardless of experimental design | MECH-320 tonic vigor: substrate-readiness PASS (mechanism instantiated correctly) but discriminative pair FAIL (EXQ-549). The mechanism is not operating during the test because the EWMA hasn't accumulated. This is not a theory failure — it is a mediator-inactivity confound | DEV-NEED-029 | MECH-320, ARC-066 | 0.85 | supports existing claim (mediator-inactivity pattern is the formal causal-inference description of cold-start null results) |

### 3.4 Ablation Study Design

| Source | Finding | REE relevance | DEV-NEED IDs | Claim IDs | Confidence | Classification |
|---|---|---|---|---|---|---|
| Lipton & Steinhardt (2019) ICML — Troubling Trends in ML | Ablation results without confidence intervals and with insufficient seeds are unreliable. Single-seed ablations on stochastic systems frequently reverse at N=5. Pre-registering the ablation hypotheses before running prevents p-hacking | EXQ-573 ran 10 arms but all bit-for-bit identical — this is actually conclusive evidence of the substrate problem, not ambiguous. Multi-seed, pre-registered ablations that produce identical results across all arms are strong evidence that the ablation's discriminative condition isn't met | DEV-NEED-029 | ARC-065 | High | supports existing claim (EXQ-573 methodology was correct; result is conclusive rather than ambiguous) |
| Kohavi et al. (2020) Trustworthy Online Controlled Experiments | Sequential experimentation: once an experiment shows null result with clear diagnosis (substrate not warm), immediately route to the substrate fix rather than running parametric variations. "Continuing the experiment after a clear negative result wastes resources without adding information" | The 540a/540b/540c/540d/540e/540f MECH-307 iteration chain is a positive example of this principle being followed. The diversity-mechanism chain (EXQ-573 + monostrategy series) should now follow the same principle: substrate fix is the route, not more variation | DEV-NEED-029 | MECH-307, ARC-065 | High | suggests experiment (route to EXQ-ISEF-001..005 immediately; do not queue more ARC-065 behavioral variations on cold substrate) |
| Bouthillier et al. (2021) NeurIPS — Accounting for Variance in ML Benchmarks | Performance differences < 1 std(seed variation) are not meaningful. For developmental AI, the analogous principle is: mechanism effect < substrate noise = the experiment cannot detect the mechanism | ARC-065 diversity mechanisms produce ~0 differential when the substrate baseline variance itself is 0 (monostrategy cold-start). The signal-to-noise ratio for any diversity test is 0/0. The denominator must be non-zero before testing | DEV-NEED-029 | ARC-065, MECH-313, MECH-314, MECH-320 | High | refines existing claim (SNR criterion for DEV-NEED-029 gate: E3 score variance must exceed noise floor before any diversity mechanism test is valid) |

### 3.5 Developmental Robotics Benchmarking

(Synthesised from infant_substrate_expansion.md §3 and replay_development_analysis.md §2 — both 2026-05-16)

| Source | Finding | REE relevance | DEV-NEED IDs | Claim IDs | Confidence | Classification |
|---|---|---|---|---|---|---|
| Garcia-Guzman (2026) Nature family | Infant exploration is not degraded goal-seeking — it is a functionally distinct mode optimising for body-dynamic discovery. Premature goal-activation closes the window | Disabling E3 during Phase 0 (motor babbling) is not an approximation — it IS the biologically-appropriate design | DEV-NEED-001 | INV-055, ARC-065, INV-073 | 0.82 | supports existing claim (Phase 0 reward-free epoch in infant_substrate_expansion.md §6.1 is correct design) |
| Adolph (2017/2019) Psych Learn Mem | Behavioral flexibility requires varied motor experience BEFORE RL narrows repertoire; posture-specific | Infant exploration must cover all action modalities before goal pursuit — impoverished substrate produces narrow option library permanently | DEV-NEED-001, DEV-NEED-004 | INV-073, INV-055, ARC-065 | 0.78 | supports existing claim (7-criterion gate from infant_substrate_expansion.md §8 is necessary) |
| Doupe & Kuhl (1999) Annu Rev Neurosci | BG-driven motor variability necessary for repertoire; pharmacological silencing = permanent monostrategy | If waking exploration is monostrategy (current V3 state), the repertoire deficit is permanent unless substrate is fixed during the developmental window | DEV-NEED-001, DEV-NEED-005 | ARC-065, MECH-309 | 0.78 | supports existing claim; time-urgency argument for prioritising substrate enrichment |

### 3.6 Curriculum Ablation in Reinforcement Learning

(Synthesised from infant_substrate_expansion.md §3.3 and §3.5)

| Source | Finding | REE relevance | DEV-NEED IDs | Claim IDs | Confidence | Classification |
|---|---|---|---|---|---|---|
| Narvekar et al. (2020) JMLR survey | Difficulty-based curricula do NOT prevent monostrategy if all tasks require the same strategy. Diversity-based curricula (by behavioral type) do. Adaptive curricula outperform fixed schedules | REE's Rung 0-4 behavioral curriculum is diversity-based (correct). But the Rung trigger must be behavioral competence plateau, not episode count | DEV-NEED-008 | ARC-065, Q-046 | 0.72 | validates existing design; suggests triggering mechanism |
| Dennis et al. (2020) NeurIPS PAIRED | Fixed bipartite environment produces monostrategy if one attractor is easier. Need difficulty calibrated to agent competence | SD-054 bipartite layout necessary but insufficient. Relative salience must track agent performance — monostrategy sentinel mechanism in infant_substrate_expansion.md §6 Phase 2 | DEV-NEED-005, DEV-NEED-008 | ARC-065, Q-046 | 0.76 | refines existing claim (sentinel mechanism is the PAIRED-analog; implementation required) |
| Oudeyer (2016) IEEE Trans Cog Dev Syst | Learning-progress curiosity produces emergent developmental stage ordering; pure novelty-max does not sequence stages | MECH-314c (learning progress sub-flavour) is the primary infant curiosity signal; needs E1 loss derivative as the progress signal | DEV-NEED-008 | MECH-314, ARC-046 | 0.76 | refines existing claim (MECH-314c priority over 314a during phase 0/1) |

### 3.7 Information Gain in Experimental Design

(Synthesised from replay_development_analysis.md §1.3, §4)

| Source | Finding | REE relevance | DEV-NEED IDs | Claim IDs | Confidence | Classification |
|---|---|---|---|---|---|---|
| Parker-Holder et al. (2020) NeurIPS DvD | Apparent diversity (pairwise distance) != effective diversity (volume). Population can be spread but degenerate | Current V3 entropy metrics measure apparent diversity. Need volumetric trajectory coverage — traj_volume_estimate (DvD-style log-det). Zero pairwise distance means zero information gain from diversity experiments | DEV-NEED-005, DEV-NEED-007 | Q-046, ARC-065 | 0.78 | refines existing claim (traj_volume_estimate is the correct info-gain metric; current entropy metrics are insufficient) |
| Schapiro et al. (2017) Phil Trans R Soc B | Dense, diverse replay required for cross-episode generalisation. Biased or sparse replay fails to extract transferable principles | Replay info-gain is bounded by waking diversity. Sleep cannot restructure content that was never created | DEV-NEED-007, DEV-NEED-011 | ARC-011, MECH-194 | High | supports existing claim; confirms infant substrate enrichment is upstream prerequisite for replay info-gain |
| Joo & Frank (2024) Science | SWR incidence increases with novelty and harm salience. Salient trials over-represented in offline replay | Harm salience is the natural SWR-gating factor. High-harm episodes MUST exist in waking experience for replay to exploit them. Current infant phase (binary hazard, near-zero residue accumulation) does not generate these | DEV-NEED-007 | MECH-285, MECH-205 | High | supports existing claim; confirms harm gradient feature (EXQ-ISEF-001) is prerequisite for replay quality |

---

## 4. Ranked Experiment Proposals

Ranking criteria: expected information gain × developmental leverage × bottleneck reduction × future unblocking. Cost and misleading-success risk are tiebreakers.

### RANK 1 — EXQ-ISEF-001: Harm Gradient Baseline

**Status:** Script not yet written — must go through /queue-experiment skill  
**DEV-NEED IDs:** DEV-NEED-002, DEV-NEED-003, DEV-NEED-004  
**Claim IDs:** ARC-013, ARC-046, INV-055  
**Priority:** Highest. This is the most direct substrate fix for content poverty (§4.1/B1 of replay_development_analysis.md).

**Why first:**
- Residue field geography (DEV-NEED-004) is the single structural prerequisite for: (a) sleep
  consolidation experiments, (b) MECH-285 staleness-priority replay, (c) DEV-NEED-029 warm-start
  gate calibration, (d) the harm-benefit separation gate (DEV-NEED-002). Without residue geography,
  everything downstream is substrate-limited.
- Binary hazard contact (current default) means the residue field never accumulates geography
  during normal episodes — agent either avoids hazards entirely (no residue) or contacts them
  terminally (brief residue spike, then episode ends).
- Harm gradients are an environment-level change only — no ree_core architecture change required.
  Low implementation cost, high downstream leverage.

**Design:** Control (binary contact) vs Treatment (harm_gradient_enabled=True, scale=0.30).
N=5 seeds each, 2000 episodes. Compare residue_coverage_pct at ep 500/1000/2000.

**Expected observations:**
- Treatment: residue_coverage_pct 0.15+ by episode 1000; harm zones show graded approach/retreat
  trajectories in replay buffer; traj_pairwise_cosine_mean higher than control.
- Control: residue_coverage_pct near-zero unless terminal contact; replay dominated by termination-adjacent
  sequences only.

**Interpretation grid:**

| Outcome | Interpretation | Next action |
|---|---|---|
| Treatment residue_coverage > 2x control at ep 1000 | Harm gradients are the bottleneck; binary contact is the root cause | Enable harm gradients as infant default; proceed to EXQ-ISEF-002 |
| Both conditions show low residue_coverage | Harm gradient alone is insufficient; likely also needs microhabitat zones for spatial differentiation | Run EXQ-ISEF-003 in parallel or serially |
| Treatment shows higher coverage but still below 0.15 | Partial fix; need higher harm_gradient_scale or larger outer radius | Re-queue as EXQ-ISEF-001a with parameter sweep |
| Treatment produces catastrophic residue saturation | harm_gradient_scale=0.30 is too high; residue_saturation_pct > 0.15 | Reduce harm_gradient_scale to 0.15; re-queue |

**Failure interpretation:** A Treatment FAIL where coverage remains near-zero despite gradients is
strong evidence that the spatial homogeneity compression (§2.3 of infant_substrate_expansion.md) is
the root cause, not the binary-contact compression — route immediately to EXQ-ISEF-003.

**Downstream decision:** PASS enables queuing EXQ-ISEF-002 and EXQ-ISEF-003 simultaneously. Also
enables the DEV-NEED-029 warm-start gate calibration experiment (EXQ-ISEF-004 needs warm residue field
to have a meaningful stochastic-attractor audit).

---

### RANK 2 — EXQ-ISEF-002: Transient Benefit Patches (z_goal Seeding Rate)

**Status:** Script not yet written — must go through /queue-experiment skill  
**DEV-NEED IDs:** DEV-NEED-006, DEV-NEED-008  
**Claim IDs:** MECH-189, INV-055  
**Priority:** High. The infant-to-childhood gate (DEV-NEED-008) is blocked by z_goal norm remaining near-zero. This directly unblocks the transition gate.

**Why second:**
- z_goal.norm() > 0.4 is the #1 blocking criterion for the infant gate. It cannot be met if resource
  contacts are sparse and uniform. Transient benefit patches create the high-salience accidental contact
  events that MECH-189 requires.
- Berridge & Robinson (1998) / Keren-Portnoy (2021) ground the wanting-before-liking pathway:
  accidental benefit contact creates approach motivation (z_goal seeding) before consummatory calibration.
  The mechanism is fast (minutes in infants) and environment-driven.
- Can run in parallel with EXQ-ISEF-001 (independent environment features).

**Design:** Control (uniform resource placement) vs Treatment (transient_benefit_enabled=True,
multiplier=3.0). N=5 seeds, 1000 episodes. Primary: episode at which z_goal.norm() > 0.4 first achieved.
Secondary: accidental_benefit_contacts, z_goal_identity_count.

**Expected observations:**
- Treatment: z_goal first-crossing before episode 300 in median; z_goal_identity_count > 1 (multiple
  resource type seeding) by episode 500.
- Control: z_goal first-crossing after episode 700 or never within 1000 episodes for some seeds.

**Interpretation grid:**

| Outcome | Interpretation | Next action |
|---|---|---|
| Treatment median first-crossing < 0.7x control | Transient patches are effective; z_goal seeding unblocked | Enable as infant default; include in 7-criterion gate |
| Both conditions show similar first-crossing times | Sparse resource contacts are not the bottleneck; likely the goal encoder or MECH-189 write path is the issue | Run goal-seeding pipeline diagnostic (similar to EXQ-536a instrumentation) |
| Treatment shows z_goal seeding but z_goal_identity_count stays at 1 | Single resource type is dominating; SD-049 multi-resource heterogeneity needed alongside | Queue EXQ testing SD-049 multi-resource + transient patches combined |

**Failure interpretation:** If z_goal seeding occurs but does not improve the transition gate, the
gate metric (z_goal.norm() threshold) may need recalibration — or the childhood-readiness issue is
not z_goal seeding but behavioral entropy.

**Downstream decision:** PASS enables: (a) enabling transient patches as infant default, (b) re-testing
the infant-to-childhood gate as a meaningful developmental transition rather than a trivially-blocked one.

---

### RANK 3 — EXQ-ISEF-003: Microhabitat Zones (Latent State Diversity)

**Status:** Script not yet written (requires microhabitat_enabled feature implementation first)  
**DEV-NEED IDs:** DEV-NEED-001, DEV-NEED-003, DEV-NEED-007  
**Claim IDs:** ARC-065, ARC-007, INV-055  
**Priority:** High. Directly addresses spatial homogeneity compression (§2.3), which prevents z_world coverage and replay geography.

**Why third:**
- Ventura et al. (2024) CA3 flexibility: environment structure during infant exploration determines
  downstream hippocampal representational flexibility. Flat environment → flat z_world → flat replay.
- Without spatially distinct zones, the warm-start gate criteria for MECH-314a (novelty bias needs
  distinct RBF centers) cannot be met — the ResidueField will not populate distinct zones.
- Implementation requires environment extension (Voronoi zone boundaries, per-zone resource/hazard
  modulation), which is a moderate-cost change.

**Design:** Control (SD-054 reef bipartite, two-zone) vs Treatment (microhabitat_enabled=True,
n_microhabitats=3). N=5 seeds, 2000 episodes. Primary: PCA variance in z_world (top 5 components)
at ep 500/1000/2000. Secondary: traj_pairwise_cosine_mean, zone_coverage.

**Expected observations:**
- Treatment: z_world PC-1 through PC-3 all > 1.2x control at ep 1000; zone-specific action
  distributions differ (H(action|zone_A) vs H(action|zone_B) KL > 0.05).
- Control: z_world PC structure dominated by single geography; zone-specific entropy near-identical.

**Interpretation grid:**

| Outcome | Interpretation | Next action |
|---|---|---|
| Treatment PCs > 1.2x and zone entropy differs | Microhabitat zones create the structural diversity needed for warm-start gate | Enable microhabitats as infant default; proceed to warm-start calibration |
| Treatment PCs higher but zone entropy identical | Zones create distinct z_world representations but agent hasn't learned zone-conditional behavior | Check whether E3 planning weight is too low for zone-specific learning; may need minimal E3 in Phase 2 |
| Both conditions similar PCA structure | CausalGridWorldV2 spatial structure doesn't propagate to z_world; the encoding is geography-blind | Investigate z_world encoder's sensitivity to spatial position; may need positional encoding |

**Failure interpretation:** A FAIL here would be important: it would mean the z_world encoder
is not sensitive to spatial geography even when the environment has structured geography. This
would be evidence for a representation quality issue upstream of the diversity mechanisms.

**Downstream decision:** PASS enables DEV-NEED-029 warm-start gate calibration (ResidueField needs
populated zones before the zone-center-count threshold can be measured).

---

### RANK 4 — EXQ-ISEF-004: Stochastic Attractor Audit + Curiosity Bonus Calibration

**Status:** Script not yet written  
**DEV-NEED IDs:** DEV-NEED-003  
**Claim IDs:** MECH-314, ARC-065  
**Priority:** High. This is a PREREQUISITE for turning up novelty_bonus_weight to its intended operating level — without this audit, increasing MECH-314a risks permanent noisy-TV capture.

**Why fourth:**
- Burda et al. (2018) ICLR: large-scale curiosity; noisy-TV problem is real and blocks permanent
  novelty trap if environment has irreducible random elements.
- Pathak et al. (2017) ICML: forward-model PE in learned feature space — fails with stochastic
  attractors. CausalGridWorldV2 has: (a) hazard drift (SD-047 stochastic), (b) resource respawn
  (random), (c) SD-048 interoceptive noise.
- These elements capture the MECH-314c learning-progress signal permanently if not controlled.

**Design:** Grid search novelty_bonus_weight in {0.1, 0.3, 0.5, 0.7, 1.0} with structured environment
(microhabitat_enabled=True). Primary: residue_coverage_pct and H_pos as functions of weight. Success:
identify Goldilocks point where both metrics maximise.

**Interpretation grid:**

| Outcome | Interpretation | Next action |
|---|---|---|
| Clear Goldilocks maximum (both metrics peak at same weight) | Noisy-TV capture visible at high weights; structured env protects at mid-range | Set novelty_bonus_weight to optimal point; include in infant defaults |
| Both metrics monotone increasing with weight | Stochastic elements not capturing novelty signal; environment is well-structured | Can safely use high novelty_bonus_weight; simplifies infant curriculum |
| residue_coverage peaks at low weight, H_pos flat | Noisy-TV capture dominant even at low weight | Audit SD-047/SD-048 for irreducible stochasticity; Markovianise or exclude from novelty signal |

**Downstream decision:** Sets the safe operating range for novelty_bonus_weight in infant Phase 1/2,
which directly determines how effectively MECH-314a/314c can drive exploration coverage.

---

### RANK 5 — EXQ-ISEF-005: Full Infant Curriculum vs Flat Parameters

**Status:** Script not yet written (requires curriculum scheduler hook implementation)  
**DEV-NEED IDs:** DEV-NEED-008  
**Claim IDs:** ARC-046, INV-055  
**Priority:** Medium-High. This is the integration test that checks whether the four-phase curriculum (§6 of infant_substrate_expansion.md) produces better gate-criterion satisfaction than flat parameter settings.

**Prerequisite:** EXQ-ISEF-001, 002, 003, 004 must all PASS to validate individual features before
the combined curriculum is tested. This avoids confounded interpretation if the curriculum test fails.

**Design:** Three-arm: (A) flat novelty_bonus=0.7 with all features on from ep 0, (B) flat with
standard infant params, (C) 4-phase curriculum. N=5 seeds, 2000 episodes. Primary: fraction of
7 gate criteria passing at ep 2000.

**Interpretation grid:**

| Outcome | Interpretation | Next action |
|---|---|---|
| Curriculum > 5/7 criteria; controls < 5/7 | Staging is necessary; features cause harm if introduced without sequencing | Adopt curriculum as infant default; proceed to warm-start calibration |
| All conditions > 5/7 at ep 2000 | Gate criteria are too easy; need harder thresholds or longer runs | Recalibrate thresholds; may indicate curriculum is not differentiating enough |
| Curriculum fails specific criteria that flat passes | Early-phase feature suppression hurts specific gates | Investigate specific phase boundaries; adjust Phase 0 exit criterion |

---

### RANK 6 — DEV-NEED-029 Warm-Start Gate Calibration (EXQ-ISEF-006, to be designed)

**Status:** Not yet designed — depends on EXQ-ISEF-001/003 PASS  
**DEV-NEED IDs:** DEV-NEED-029  
**Claim IDs:** ARC-065, MECH-313, MECH-314, MECH-320  
**Priority:** Medium-High. This experiment establishes the empirical thresholds for the three DEV-NEED-029 criteria:
- ResidueField center count > N_min (threshold TBD)
- MECH-320 EWMA > epsilon (threshold TBD)
- E3 score variance > noise floor (threshold TBD)

**Design:** Two-phase within a single run: (Phase 1) allow substrate to warm naturally until
residue_coverage_pct > 0.15 and z_goal.norm() > 0.4 (infant gate criteria met); (Phase 2) run
diversity mechanism sweep on the now-warm substrate. Observe at what substrate state each diversity
mechanism first produces non-zero differential. That state becomes the gate threshold.

**Interpretation grid:**

| Outcome | Interpretation | Next action |
|---|---|---|
| All mechanisms produce non-zero differential once residue_coverage > 0.15 | Gate criterion is residue coverage; this is the single warm-start proxy | Adopt residue_coverage > 0.15 as DEV-NEED-029 gate; unblocks Q-043/044/045 queuing |
| MECH-320 needs EWMA > specific value independent of residue | Gate criterion is EWMA-based; both thresholds needed | Register both thresholds; update DEV-NEED-029 with dual criteria |
| E3 score variance is the limiting factor | Gate criterion is E3 training depth, not substrate coverage | Gate criterion needs episode count + E3 training metric |

**Downstream decision:** PASS establishes the empirical thresholds for DEV-NEED-029, converting
it from a PROPOSED gap into a blocking gate with measurable criteria. This is the meta-experiment
that makes all subsequent ARC-065 behavioral experiments scientifically valid.

---

### RANK 7 — Q-043 / Q-044 / Q-045 ARC-065 Behavioral Ablation Cohort

**Status:** Designed; blocked on warm-start gate confirmation  
**DEV-NEED IDs:** DEV-NEED-003, DEV-NEED-005, DEV-NEED-029  
**Claim IDs:** MECH-313, MECH-314, MECH-320, Q-043, Q-044, Q-045  
**Priority:** Medium (becomes Highest once DEV-NEED-029 gate is passed)

**Why seventh (not first):**
- These experiments have substrate-readiness PASSes (EXQ-544, EXQ-545, EXQ-547).
- But behavioral discriminative tests require warm substrate (DEV-NEED-029 gate).
- Running now = zero information (EXQ-573 demonstrated this).
- Running after EXQ-ISEF-006 warm-start calibration = maximum information.

**Q-043 design:** Relative weight calibration (MECH-313 vs MECH-314 vs MECH-320 contribution weight sweep). 4-arm factorial. Run AFTER DEV-NEED-029 gate established.

**Q-044 design:** MECH-314 sub-flavour independence test (314a alone, 314b alone, 314c alone, all three). Establishes whether any single sub-flavour drives the diversity benefit.

**Q-045 design:** MECH-313 vs MECH-260 collapse falsifier with extended 8-cell design (per R4 verdict from Q-045 lit-pull). Requires SD-054 multi-trial temporal horizon precondition (R5 precondition from Kennerley 2006).

---

### RANK 8 — EXQ-IDEV-006: SD-017 Functional Validation (Context Discrimination)

**Status:** Partially designed in replay_development_analysis.md §7.6  
**DEV-NEED IDs:** DEV-NEED-007  
**Claim IDs:** SD-017, MECH-166, INV-044  
**Priority:** Medium. This is the functional test that EXQ-265/265a methods PASSes built toward.

**Design:** Two conditions over 3 waking+sleep cycles: (A) 3 sessions + 3 sleep cycles, (B) 3 sessions + no sleep. Measure context cosine_sim before and after each cycle. Target: sleep condition context_cosine_sim < 0.95 by cycle 3; no-sleep stays > 0.95.

**Prerequisite:** SD-017 SWS/REM phase infrastructure is confirmed working (EXQ-265a PASS — confirmed). Residue geography must exist for context differentiation to be meaningful — needs EXQ-ISEF-001/003 PASS.

**Why this matters:** INV-049 (offline phases mathematical necessity) has FAILed twice. The functional SD-017 test would provide direct positive evidence for the consolidation mechanism rather than trying to ablate it. If this PASSes, it strongly supports INV-049 despite its ablation failures, and confirms the content-poverty interpretation of those FAILs.

---

### RANK 9 — EXQ-IDEV-001: Longitudinal Infant Replay Quality

**Status:** Designed in replay_development_analysis.md §7.1  
**DEV-NEED IDs:** DEV-NEED-007, DEV-NEED-008  
**Claim IDs:** INV-055, ARC-011, INV-049  
**Priority:** Medium. This is the active-learning-optimal query for INV-049 (Settles 2012 criterion).

**Design:** Track replay metrics longitudinally across the infant phase. If replay quality metrics (replay_zone_coverage_fraction, replay_residue_coverage_delta, post_sleep_z_goal_retention) improve monotonically and converge with gate criteria at the same episode count, this confirms that replay is driving developmental progress, not just measuring noise.

**Critical failure interpretation:** If replay quality metrics improve but gate criteria do NOT improve, replay is reorganizing impoverished content rather than creating new developmental capacity — the substrate fix is the correct intervention, confirming the content-poverty theory of INV-049 FAILs.

**Prerequisite:** Requires warm infant substrate (EXQ-ISEF-001..004 PASS).

---

### RANK 10 — ARC-062 Phase 3 Wiring Redesign

**Status:** V3-EXQ-543d FAIL; redesign needed  
**DEV-NEED IDs:** DEV-NEED-019 (gradual responsibility expansion)  
**Claim IDs:** ARC-062, SD-033a, MECH-260  
**Priority:** Medium. This is the next architectural wiring pass on a separate (non-monostrategy-dependent) thread.

ARC-062 Phase 3 (discriminator → SD-033a LateralPFCAnalog.update() + bias-head parameters to E3 optimizer) has FAILed in three iterations (543b, 543c, 543d). The 2x2 factorial (gated_policy x dACC) with MECH-260 anti-recency=0.5 did not isolate the wiring issue. The next iteration needs to: (a) verify the discriminator output is reaching its consumer with non-trivial signal, (b) instrument the LateralPFCAnalog.update() path for signal through-flow before the full training run.

**Downstream decision:** Phase 3 PASS closes commitment_closure_plan.md GAP-1 and unblocks the SD-033a/SD-034 consumer cascade (goal_pipeline_plan.md GAP-2/GAP-5).

---

## 5. Dependency-Aware Scheduling

```
EXQ-ISEF-001 (harm gradient)
    │
    ├──> EXQ-ISEF-002 (transient benefit patches) [parallel safe]
    │        │
    │        └──> Infant gate criteria become testable
    │
    ├──> EXQ-ISEF-003 (microhabitat zones) [parallel safe after env feature lands]
    │        │
    │        └──> z_world coverage testable
    │
    └──> EXQ-ISEF-004 (curiosity bonus calibration) [needs EXQ-ISEF-003 warm substrate]
             │
             ├──> novelty_bonus_weight calibrated for Phase 1/2
             │
             └──> EXQ-ISEF-006 (DEV-NEED-029 warm-start gate calibration)
                      │
                      ├──> Q-043 / Q-044 / Q-045 ARC-065 behavioral ablation [UNBLOCKED]
                      │
                      ├──> EXQ-IDEV-006 (SD-017 functional validation) [UNBLOCKED]
                      │        │
                      │        └──> EXQ-IDEV-001 (longitudinal replay quality)
                      │
                      └──> EXQ-IDEV-003 (coverage vs RPE replay policy) [UNBLOCKED]

EXQ-ISEF-005 (full curriculum vs flat) [after EXQ-ISEF-001..004 all PASS]

ARC-062 Phase 3 wiring [independent thread, no dependency on infant substrate]
    │
    └──> SD-033a consumer cascade (goal_pipeline GAP-2/5)
             │
             └──> SD-049 Phase 2 behavioral validation (after GAP-3 env extensions)
```

**Critical path:** EXQ-ISEF-001 → EXQ-ISEF-003 → EXQ-ISEF-006 → Q-043/044/045

**Parallel-safe pairs:**
- EXQ-ISEF-001 ‖ EXQ-ISEF-002 (independent environment features)
- ARC-062 Phase 3 redesign ‖ any EXQ-ISEF experiment (different code paths)
- EXQ-IDEV-006 ‖ Q-043/044/045 (once warm-start gate established)

**Serial dependencies:**
- EXQ-ISEF-004 must follow EXQ-ISEF-003 (needs warm microhabitat substrate for meaningful attractor audit)
- EXQ-ISEF-006 must follow EXQ-ISEF-001 + EXQ-ISEF-003 (needs populated ResidueField and z_world zones)
- Q-043/044/045 must follow DEV-NEED-029 gate establishment (EXQ-ISEF-006)

---

## 6. Experiments to Defer

The following experiments should NOT be queued until the specified prerequisite conditions are met.
Queuing them now would produce zero-information results at non-trivial runner cost.

| Experiment type | Prerequisite not met | Approximate prerequisite experiment | Deferral rationale |
|---|---|---|---|
| Any ARC-065 behavioral discriminative pair | DEV-NEED-029 warm-start gate not established | EXQ-ISEF-006 | Zero KG / zero SNR on cold substrate (EXQ-573 demonstrated) |
| INV-049 retest (offline consolidation necessity ablation) | Infant substrate content poverty not fixed | EXQ-ISEF-001, EXQ-ISEF-003 | INV-049 FAILs are most plausibly content-poverty failures, not theory failures; retesting under same conditions wastes oracle budget |
| SD-029 self-attribution retest | V_s monostrategy not resolved | ARC-065 behavioral validation + SD-055 differentiable CEM | SD-029 requires agent-vs-environment event distributions; monomodal policy cannot generate balanced C2/C3 distributions |
| ARC-016 precision commitment retest | Substrate-ceiling determination pending | V4 spec or major substrate enrichment | EXQ-530/530c FAIL pattern is consistent with substrate ceiling; more experiments on same substrate will not advance this |
| EXQ-IDEV-002 (play+real interleaved replay) | Play substrate not implemented | V4 developmental harness spec | Requires bilateral play frame + caregiver scaffold; full V4 play substrate needed |
| EXQ-IDEV-003 (coverage vs RPE replay policy) | Warm-start gate not established AND MECH-285 staleness priority not implemented | DEV-NEED-029 gate + MECH-285 implementation | Replay policy comparison is only meaningful on warm substrate with staleness mechanism present |
| EXQ-IDEV-004 (sleep prevents residue saturation) | Warm-start gate not established | EXQ-ISEF-006 | Residue saturation prevention requires populated residue field; cold substrate has nothing to saturate |
| Q-043/044/045 before warm-start gate | DEV-NEED-029 gate not met | EXQ-ISEF-006 | See EXQ-573; mechanism ABs produce identical arms on cold substrate |
| SD-032b dACC arbitration behavioral test | ARC-062 Phase 3 wiring not complete | commitment_closure_plan GAP-1 | Consumer of Phase 3 wiring; premature test cannot route arbitration signal |
| Any V4 social/language experiment | V4 multi-agent substrate not built | V4 spec and implementation | INV-043, MECH-158, ARC-047, ARC-048 require genuine caregiver + peer agents; no V3 proxy is valid |

### Deferral Principle

**Do not queue an experiment where the pre-registered interpretation grid contains no row that would
produce a theory-informative result.** If every plausible experimental outcome routes to "substrate
not ready, fix substrate first," the experiment has zero developmental information value.

For INV-049 specifically: a third FAIL under current substrate would not change the current
interpretation (content poverty, not theory failure). The correct response is EXQ-IDEV-001
(longitudinal replay quality), which tests whether replay IS improving within-stage even if the
between-condition ablation is not yet discriminative.

---

## 7. Governing Principles for This Priority List

### 7.1 Substrate First, Mechanisms Second

The ARC-065 mechanism cluster (MECH-313, MECH-314, MECH-320) is implemented and has substrate-readiness
PASSes. The infant substrate expansion (EXQ-ISEF series) is the prerequisite for these mechanisms to
produce non-zero differential. Queuing behavioral validation before the substrate produces warm states
is equivalent to testing whether a car engine works by testing it with no fuel — the negative result
tells you nothing about the engine.

### 7.2 The Warm-Start Gate Is the Science Gate

DEV-NEED-029 is not just a technical prerequisite. It is the scientific gate that determines whether
ARC-065 behavioral experiments can produce theory-informative results. Until DEV-NEED-029 thresholds
are empirically calibrated (EXQ-ISEF-006), every ARC-065 behavioral test has unknown interpretability.

### 7.3 FAILs Are Information — Use Them

The recent FAIL cluster (EXQ-573, EXQ-549, EXQ-552, EXQ-553) is extremely informative:
- They confirm the cold-start warm-start failure theory.
- They localise the monostrategy cliff to the CEM proposer.
- They establish that the basin is agent-init-dependent (not universal).
The correct response is to use this information to design better experiments, not to add more
parameters or retry under near-identical conditions.

### 7.4 PASS Infrastructure Counts — Build On It

The recent PASS cluster (substrate-readiness probes, SD-055 differentiable CEM, SD-054 bipartite layout)
represents real capability gains. The SD-055 differentiable CEM (EXQ-568 PASS) is particularly valuable
as it directly targets the CEM proposer-stage monostrategy cliff. This should be integrated into the
infant substrate alongside the environment enrichment features.

### 7.5 Distinguish Curriculum Failure from Substrate Failure

A substrate failure is when the experimental conditions cannot produce the theoretical outcome
regardless of curriculum (e.g., no residue geography, no z_world diversity). A curriculum failure
is when the conditions are present but the staging is wrong (e.g., E3 activated too early,
suppressing the Phase 0 babbling window). The EXQ-ISEF series tests for substrate failures.
EXQ-ISEF-005 tests for curriculum failures. These must not be conflated.

### 7.6 The Monostrategy Is Developmental, Not Mechanical

The seed-dependent escape from monostrategy (EXQ-555/557) suggests the monostrategy basin is not a
mathematical certainty for any given architecture. Some initializations escape. The infant substrate
enrichment is designed to reshape the attractor landscape during the developmental window — creating
competing benefit/harm attractors before the policy can converge to a single basin. This is a
developmental intervention, not a parameter fix. Getting it right requires the sequenced curriculum
(Phase 0 protected babbling, Phase 1 benefit discovery, Phase 2 competing attractors) specified in
infant_substrate_expansion.md.

---

## 8. Open Questions for Governance

1. **DEV-NEED-029 thresholds:** The three threshold values (N_min for ResidueField centers,
   epsilon for MECH-320 EWMA, noise floor for E3 score variance) are TBD. EXQ-ISEF-006 must
   be designed and PASSed before these can become blocking gate criteria. Who decides the minimum
   acceptable thresholds?

2. **Phase 0 reward-free epoch:** Griffin et al. (2026) + Garcia-Guzman (2026) ground the
   mechanistic necessity of a reward-free Phase 0. Currently ARC-046 mentions the infant stage
   but does not explicitly mandate a Phase 0 epoch. Should this be registered as an ARC-046
   amendment or as a new candidate ARC-claim?

3. **Wanting-before-liking sequencing (candidate MECH):** The Berridge/Keren-Portnoy finding
   (wanting = approach motivation, seeded before liking is calibrated) is not currently a registered
   MECH. It would be a child of MECH-189. Governance decision needed before EXQ-ISEF-002 results
   can be properly tagged.

4. **INV-049 status:** Two FAILs (EXQ-385, EXQ-385a) but strong literature grounding. The
   content-poverty interpretation is now well-supported. Should INV-049 be flagged
   pending_substrate_reconfirmation while EXQ-ISEF series is in progress? This would prevent
   the two FAILs from continuing to weigh against INV-049 in governance scoring.

5. **ARC-070/071 R6 SAFETY-CRITICAL:** The governance decision on MECH-094 hypothesis_tag
   strict-vs-relaxed for chunking writes (ARC-071) is gated and should not be held up by the
   infant substrate work. These are independent threads.

---

## Related Documents

- [`infant_substrate_expansion.md`](infant_substrate_expansion.md) — substrate feature proposals (EXQ-ISEF series scripts + gate criteria)
- [`replay_development_analysis.md`](replay_development_analysis.md) — replay bottleneck analysis + candidate experiments (EXQ-IDEV series)
- [`developmental_needs_register.md`](developmental_needs_register.md) — full DEV-NEED traceability table
- [`developmental_metrics.md`](developmental_metrics.md) — quantitative gate thresholds
- [`behavioral_diversity_acceptance_criteria.md`](../../../evidence/planning/behavioral_diversity_acceptance_criteria.md) — Rung 0-4 diversity ladder
- `evidence/planning/infant_substrate_expansion_plan.md` — when created, this will be the plan-of-record for EXQ-ISEF series
