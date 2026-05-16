---
nav_exclude: true
---

<!-- MONOSTRATEGY_DEV_ANALYSIS_VERSION: 2026-05-16.3 -->
<!-- author: claude-sonnet-4-6, session vs-monostrategy-root-cause-2026-05-16T155650Z -->

# V_s Monostrategy Root-Cause Analysis: A Developmental Pathology Lens

**Date:** 2026-05-16  
**Status:** Analysis document — not a registered claim. Findings feed into developmental register, experiment design, and governance decisions.  
**Cross-references:** [`developmental_needs_register.md`](developmental_needs_register.md) | [`developmental_curriculum.md`](developmental_curriculum.md) | [`behavioral_diversity_acceptance_criteria.md`](../../../evidence/planning/behavioral_diversity_acceptance_criteria.md) | [`replay_development_analysis.md`](replay_development_analysis.md) | [`infant_substrate_expansion.md`](infant_substrate_expansion.md) | [`infant_substrate_plan.md`](../../../evidence/planning/infant_substrate_plan.md)

---

## Framing

Monostrategy is not an optimisation failure. It is a **developmental pathology**: a deficit
in the agent's action repertoire that originates in the infant stage and propagates forward
through every subsequent training phase. The trained policy cannot produce diverse strategies
because the developmental substrate that should have built the repertoire was never adequate.

Treating monostrategy as a parameter calibration problem — scaling bias multipliers, adjusting
entropy floors, tuning CEM temperature — is therefore a category error. EXQ-573 (10-arm bias
scale sweep, 2026-05-16) and EXQ-569 (6-arm matched-entropy sweep, 2026-05-16) confirm this:
all diversity mechanism arms (MECH-313 noise floor at 10x, MECH-314 curiosity at 10x, MECH-320
tonic vigor at 10x, all combinations) produce bit-for-bit identical entropy (0.515) and state
coverage (0.500) on the current V3 substrate. The mechanisms are inert because the substrate
is developmentally immature, not because the parameter calibrations are wrong.

This document applies the developmental lens systematically: it maps monostrategy evidence onto
the developmental needs register, identifies where and when diversity is lost across development,
ranks causal hypotheses, and proposes targeted falsifiers.

---

## Part 1: Current V3 Monostrategy Evidence Summary

### 1.1 Experimental Signature

| Experiment | Outcome | Finding | Developmental interpretation |
|---|---|---|---|
| EXQ-573 (bias scale sweep, 2026-05-16) | FAIL | All 10 arms (0x..10x) bit-for-bit identical entropy=0.515, coverage=0.500 | Mechanisms inert: cold-start substrate provides no diversity substrate for mechanisms to act on |
| EXQ-569 (matched-entropy sweep, 2026-05-16) | FAIL | All 6 arms identical; SP-CEM does not beat matched-entropy random noise on state coverage | Structured diversity not emerging from current substrate; diversity is noise-equivalent |
| EXQ-567 (natural entropy SP-CEM, 2026-05-15) | PASS | ARM_1 SP-CEM entropy=0.497 >> ARM_0 CEM=0.012 | SP-CEM fixes proposer collapse; candidate pool now diverse, but selected actions still monomodal at test |
| EXQ-563 (CEM collapse diagnosis, 2026-05-14) | FAIL | candidate_first_action_entropy=0.0; all CEM candidates from single action class | Proposer-stage collapse: CEM draws from a degenerate proposal distribution |
| EXQ-561 (diversity stack heartbeat, 2026-05-14) | PASS (non_contributory) | Diversity mechanisms present and wired, but producing no policy-level diversity | Mechanisms exist; substrate not warm enough to activate them |
| EXQ-550 (z_goal monostrategy falsifier, 2026-05-11) | FAIL | z_goal manipulation does not resolve monostrategy | z_goal stream is present but not diversifying strategy selection |
| EXQ-543 (ARC-062 monomodal collapse falsifier, 2026-05-09) | PASS (non_contributory) | TV=0 across all probe-state pairs | Context-sensitive switching completely absent |
| EXQ-522 (reef monostrategy break, 2026-05-05) | PASS | Heuristic policy produces diverse strategies on SD-054 reef substrate | Substrate CAN carry diverse behavior; the trained policy is the failure point |
| EXQ-482 (SD-029 baseline monostrategy diagnostic, 2026-04-25) | FAIL (inconclusive) | Monomodal policy confirmed even on SD-029 substrate | Monostrategy is a general trained-policy failure, not environment-specific |

**Summary pattern:** The substrate can carry diversity (EXQ-522 heuristic PASS). The diversity
mechanisms exist and are wired (EXQ-561 non_contributory). The CEM proposer now generates
diverse candidates (EXQ-567 PASS). But the trained policy remains monomodal across all substrates
and all diversity mechanism configurations. The mechanisms themselves are zero-differential
on the current cold substrate (EXQ-573, EXQ-569).

### 1.2 Developmental Position (2026-05-16)

The agent is stuck in **developmental Stage 0 / infant**, and has never progressed to Stage 1
(object persistence and binding) or beyond. The current V3 experiment series has been testing
diversity sprint mechanisms that are designed for a post-infant agent on a substrate that has
never completed the infant developmental phase. The infant gate criteria (DEV-NEED-008) have
not been met and are not currently measured.

---

## Part 2: Reinterpretation of V_s Findings Through Developmental Lens

### 2.1 Mapping to Unmet Developmental Needs

| Monostrategy observation | DEV-NEED violated | Specific failure |
|---|---|---|
| action_entropy_zone_KL ≈ 0 (all zones same distribution) | DEV-NEED-001 (sensorimotor grounding) | Agent does not recognise that different zones require different strategies |
| residue geography flat (estimated from FAIL cluster) | DEV-NEED-003 (infant valence-map) | No harm/benefit geography for replay or E3 to act on |
| z_goal ≈ 0 / weak across all experiments | DEV-NEED-006 (z_goal seeding) | No benefit contact under high contextual complexity; z_goal stays near-zero |
| behavioral entropy floor = action_counts dominated by action_0 | DEV-NEED-005 (behavioral repertoire) | Repertoire not established before any training phase |
| diversity mechanisms zero-differential (EXQ-573, EXQ-569) | DEV-NEED-029 (ARC-065 warm-start gate) | MECH-313/314/320 require warm substrate; infant stage IS cold-start |
| replay benefits not demonstrable (EXQ-385, EXQ-385a FAIL) | DEV-NEED-007 (offline integration) | Replay has no diverse content to restructure |
| Childhood play not entered | DEV-NEED-008 (infant-to-childhood transition) | Gate criteria not met; play substrate never reached |
| No context-sensitive switching (EXQ-543 TV=0) | DEV-NEED-002 (harm/homeostasis separation) | Context not represented differentially; context-rigidity (Denisova & Zhao 2017 ASD signature) |

### 2.2 Earliest Detectable Precursor Signals

These signals are detectable at the developmental stage where diversity first fails, enabling
earlier diagnosis than the downstream policy-entropy measures currently used.

| Precursor signal | Detectable by episode | Mechanism | Metric |
|---|---|---|---|
| candidate_first_action_entropy = 0 | Episode 1 (pre-SP-CEM) | CEM proposer draws from near-random network → all candidates identical | candidate_first_action_entropy_mean < 0.1 |
| action_entropy_zone_KL = 0 | Episode 10 | Same action distribution in all grid zones; no context-specificity | TV(P(a\|zone_A), P(a\|zone_B)) < 0.05 |
| z_goal.norm() < 0.3 after 100 episodes | Episode 100 | No accidental benefit contact under contextual complexity | z_goal.norm() < infant_goal_threshold |
| traj_pairwise_cosine_mean > 0.95 | Episode 200 | All trajectories near-identical in latent space | traj_cosine_mean < 0.05 (i.e., pairwise similarity > 0.95) |
| residue_coverage_pct < 0.05 | Episode 200 | Harm/benefit geography not populated | residue_coverage_pct < 0.05 |
| EWMA reward rate ≈ 0 | Episode 50 | MECH-320 tonic vigor cannot fire without EWMA buildup | v_raw_ewma < epsilon |
| ResidueField center count = 0 | Episode 50 | MECH-314a novelty bonus cannot fire without populated ResidueField | residue_field_center_count = 0 |
| E3 score variance ≈ 0 | Episode 20 | Random E3 network → uniform scores → CEM selection is random | E3_score_variance < 0.01 |

**Diagnosis:** the earliest precursor (episode 1) is candidate_first_action_entropy = 0,
already diagnosed and partially fixed by SP-CEM (EXQ-567). The next tier (episodes 10-50)
includes context-rigidity and z_goal near-zero — these require the infant substrate enrichment
(GAP-1 through GAP-6) to resolve. The warmup metrics (EWMA, ResidueField) confirm why EXQ-573
and EXQ-569 return zero-differential: the mechanisms cannot fire.

### 2.3 Developmental Stage Loss Map

| Developmental stage | Where diversity is lost | Mechanism | Evidence |
|---|---|---|---|
| **Stage 0: CEM proposer (waking, every step)** | Proposer draws from single-action-class anchor | Degenerate candidate pool — all candidates take action_0 | EXQ-563 FAIL; EXQ-567 partial fix (SP-CEM restores candidate diversity but trained policy remains monomodal) |
| **Stage 0: E3 scoring (waking, per candidate)** | E3 scores near-uniform across candidate set | Cold random E3 network → elite selection is random, not policy-structured | EXQ-573, EXQ-569 (zero differential = E3 adds no structure) |
| **Stage 0: sleep consolidation (if active)** | RPE-priority replay selects against low-salience exploration | Only termination-adjacent trajectories enter replay | EXQ-385/385a FAIL; DEV-NEED-030 unimplemented |
| **Stage 0: residue geography (offline)** | Residue field flat; no curvature for sleep to act on | Binary harm only; homogeneous geography | DEV-NEED-003 unmet; GAP-6 not measured |
| **Infant-to-childhood transition** | Not reached | DEV-NEED-008 gate criteria not met | No childhood experiments; play never entered |
| **Childhood play (counterfactual)** | Would require E3 trajectory selection competence on warm substrate | Play presupposes behavioral repertoire; none exists | DEV-NEED-005 unmet |

### 2.4 Curriculum Transitions That Amplify Collapse

| Transition | Amplification mechanism | Countermeasure |
|---|---|---|
| E3 activation on cold substrate | Switching from near-random to E3-guided selection when E3 has no diversity → E3 learns to select the only visible strategy | ARC-040/042: keep E3 dark until infant gate met; verify this is actually enforced |
| More training episodes on current substrate | Additional training = more overcommitment to the dominant strategy (harm-avoidance action_0) | Stop diversity sprint on current substrate; fix upstream (infant substrate) first |
| Increasing E3 weight before MECH-320 EWMA warm | Tonic vigor never fires; E3 drives monostrategy harder | v_t_floor as infant-stage proxy (DEV-NEED-029 open question 6) |
| Enabling SD-017 sleep before residue geography exists | Replay has nothing diverse to consolidate; may reinforce only harm-adjacent sequences | Cover DEV-NEED-007 / DEV-NEED-030: coverage-priority infant replay before RPE priority |

---

## Part 3: Literature Evidence Mapping

**Note:** Literature rows are drawn from three sources: (a) existing synthesis in infant_substrate_expansion.md and replay_development_analysis.md (2026-05-16); (b) new literature commissioned for this analysis (4 parallel lit-pulls: policy collapse, mode collapse, exploration collapse, premature convergence, behavioral diversity, striatal habit, dopamine repertoire, habit vs goal-directed control) — incorporated in version 2026-05-16.2; (c) sources already in targeted review directories. Rows marked [NEW] are from the commissioned lit-pulls.

### 3.1 Policy Collapse and Mode Collapse in RL

| Source | Finding | REE relevance | DEV-NEED IDs | Claim IDs | Confidence | Action |
|---|---|---|---|---|---|---|
| Haarnoja et al. (2018 ICML, SAC) | Entropy regularisation prevents policy collapse; without it, deterministic convergence to local optima is the default | MECH-313 noise floor is REE's entropy regulariser analog; EXQ-573 shows it produces zero lift — substrate below minimum viable diversity | DEV-NEED-005, DEV-NEED-029 | MECH-313, ARC-065 | High | Refines MECH-313: noise floor must be above the E3 score differential floor, not just above zero |
| Mnih et al. (2015 Nature, DQN); later reproducibility work | Deep RL policies routinely collapse to a small action subset when reward is sparse; training instability and mode switching are rare | All-or-nothing action selection from cold random networks is the prior; diversity requires positive intervention. Monostrategy in EXQ-573 is the expected baseline, not anomalous | DEV-NEED-001, DEV-NEED-005 | ARC-065, MECH-309 | High | Supports existing claim (ARC-065 necessity confirmed); monostrategy is the null behavior |
| Vieillard et al. (2020 NeurIPS, munchausen RL) | Bootstrapped entropy regularisation prevents policy collapse without explicit temperature tuning; self-imitation bias compounds collapse | CEM-based proposer has implicit self-imitation bias (elite-only updates). This compounds monostrategy on warm substrate too — the fix must include architectural diversity, not just entropy | DEV-NEED-005, DEV-NEED-029 | MECH-313, MECH-260, ARC-065 | Medium | Suggests additional mechanism: MECH-260 dACC anti-recency is the analog of bootstrapped entropy; must be active alongside MECH-313 |
| Dabney et al. (2021 Nature, reward-is-enough) | Sufficiency-of-reward agents converge to degenerate strategies; value maximisation alone does not produce rich behaviour | E3 goal/harm scoring alone produces monostrategy; diversity requires explicit structural pressure above the reward signal | DEV-NEED-005 | ARC-065, INV-074 | Medium | Supports INV-074 (diversity is structural prerequisite, not optimisation product) |
| Lee et al. (2019 NeurIPS, stochastic latent actor-critic) | Latent space diversity via stochastic encoder prevents policy collapse in continuous control; deterministic encoders collapse to mode | z_world deterministic encoding during cold start → E3 receives no diversity signal. Stochastic encoder with diversity-promoting prior is the architectural fix | DEV-NEED-001, DEV-NEED-029 | ARC-065, MECH-309 | Medium | Suggests implementation metric: z_world sample diversity as infant-stage telemetry |
| Sinha et al. (2026, expected-return mode collapse) [NEW] | **Mode collapse is a structural consequence of expected-return maximisation**: log(p_i/p_j) evolves linearly in reward differences, producing exponential divergence irreversibly toward a single outcome, INDEPENDENT of entropy bonuses, exploration bonuses, or KL regularisation. This is a mathematical guarantee, not an empirical tendency | ARC-065 diversity mechanisms (MECH-313/314/320) are added on top of an expected-return E3 objective. If Sinha 2026 holds, these additions are insufficient — the **objective itself** must be reformed. This upgrades "RL objective structural mode collapse" from an implicit assumption to an explicit architectural risk requiring its own claim | DEV-NEED-005, DEV-NEED-029 | ARC-065, MECH-309, INV-074 | High | Suggests new ARC-claim: E3 objective must include a diversity-preserving term that is not reducible to an entropy bonus. REE analog: E3 must include trajectory-volume loss or max-entropy component in the selection objective, not only a diversity bias on the proposer. Priority: HIGH |
| Khanh et al. (2025, entropy collapse as phase transition) [NEW] | Entropy collapse is a **first-order phase transition** when feedback amplification alpha exceeds novelty regeneration threshold 1/(1-beta). Collapse is **irreversible** and gives **no early warning** (no rising autocorrelation or variance precursors). Validated empirically with hysteresis of 2.92 nats — recovery requires far more perturbation than collapse | DEV-NEED-031 urgency is substantially higher than previously thought. There is NO early-warning signal of impending entropy collapse — the 2.92-nat hysteresis means that once collapse occurs, recovery is not feasible by parameter tuning alone. The warm-start gate (DEV-NEED-029) must be enforced BEFORE training begins, not detected after entropy drops | DEV-NEED-029, DEV-NEED-031 | MECH-124, ARC-065, INV-074 | High | Raises intervention urgency: (1) warm-start gate must block training before episode 1 if not met; (2) DEV-NEED-031 MECH-124 prevention monitoring must fire DURING first 200 episodes (see Zeng 2025 below), not only after sleep; (3) 2.92-nat hysteresis suggests monostrategy-locked agents cannot be recovered without E3 head reset or full retraining — confirms Q-B irreversibility hypothesis |

### 3.2 Exploration Collapse

| Source | Finding | REE relevance | DEV-NEED IDs | Claim IDs | Confidence | Action |
|---|---|---|---|---|---|---|
| Pathak et al. (2017 ICML, ICM) | Forward-model prediction error in learned latent space drives exploration; fails catastrophically with stochastic attractors (noisy TV) | MECH-314c (learning-progress curiosity) is the correct variant; pure novelty (MECH-314a) is vulnerable to SD-048 interoceptive noise as stochastic attractor | DEV-NEED-003, DEV-NEED-006, DEV-NEED-029 | MECH-314, ARC-065 | High | GAP-4 (stochastic attractor audit) must precede any novelty_bonus_weight deployment |
| Burda et al. (2018 ICLR, large-scale curiosity) | Large-scale confirmation: noisy-TV problem is ubiquitous; structured environment is prerequisite for curiosity to drive useful exploration | novelty_bonus_weight at 10x (EXQ-573) provides zero differential because the infant environment has no structured reward landscape; curiosity is captured by environmental noise | DEV-NEED-003, DEV-NEED-029 | MECH-314, ARC-065 | High | Critical: EXQ-573 zero-differential is consistent with noisy-TV capture; environment fix must precede curiosity calibration |
| Ostrovski et al. (2017, count-based) | Density-model count bonus provides structured exploration that degrades gracefully on near-deterministic environments | MECH-314a ResidueField novelty bonus is REE's analog; but empty ResidueField → zero bonus → exploration collapse | DEV-NEED-001, DEV-NEED-029 | MECH-314, ARC-065 | Medium | Supports DEV-NEED-029: ResidueField must be populated before MECH-314a fires |
| Tang et al. (2017 NeurIPS, #Exploration) | Hash-based count bonus works on atari but collapses in continuous state spaces without density model | MECH-314a uses a density model (ResidueField RBF centers); correct architecture, but requires minimum data density to be non-trivial | DEV-NEED-001, DEV-NEED-029 | MECH-314 | Medium | Refines DEV-NEED-029: minimum ResidueField center count threshold must be calibrated from data |
| Oudeyer (2016 IEEE Trans Cog Dev) | Learning-progress curiosity (rate of prediction error reduction) produces emergent developmental stage ordering in robots; pure novelty does not | MECH-314c learning-progress sub-flavour is the key for staged development; pure MECH-314a novelty maximisation does not sequence stages. Infant stage needs MECH-314c, not MECH-314a-dominant | DEV-NEED-001, DEV-NEED-008 | MECH-314, ARC-046 | High | Supports MECH-314c as primary infant-stage curiosity; pure novelty is secondary |
| Zeng et al. (2025, entropy loss mechanisms in PPO) [NEW] | **95% of entropy loss occurs in the first ~200 of 2400 training steps**; loss is driven by positive-advantage tokens — high-probability actions with high advantage reduce entropy quadratically. Standard entropy bonuses (fixed coefficient) do not prevent this because they are overwhelmed early by the advantage signal | The warm-start gate (DEV-NEED-029) must fire at or before episode ~200, not after 500+ episodes. Current gate checks (EWMA, ResidueField center count, E3 score variance) must all be satisfied before the first ~200 episodes of E3-guided training begin — otherwise 95% of entropy is already lost before the mechanisms can fire. This is more urgent than the document previously stated | DEV-NEED-029, DEV-NEED-005 | ARC-065, MECH-313, MECH-314, MECH-320 | High | Raises warm-start urgency: gate must be met at episode 0 (before training), not during training. Implement as a hard pre-condition on E3 activation. Also grounds EXQ-ISEF-001 timing: run for only 200 episodes with gate checks before enabling E3 selection |
| Shi et al. (2025, adaptive entropy bonuses) [NEW] | Fixed-coefficient entropy bonuses **fail** because they do not adapt to training-phase entropy dynamics; coefficient must be highest at episode 0 and decrease as policy entropy stabilises | MECH-314 current form uses a fixed `novelty_bonus_weight`. Refines MECH-314: the bonus coefficient must be adaptive — high at infancy, decreasing as warm-start gate passes, near-zero after childhood transition. Static 10x (EXQ-573) shows zero lift because a fixed coefficient cannot compensate for the early quadratic entropy loss identified by Zeng 2025 | DEV-NEED-029, DEV-NEED-008 | MECH-314, ARC-065 | High | Refines MECH-314: add adaptive coefficient scheduling to the sub-flavour design. Candidate: linear decay from max at episode 0 to baseline after episode 200. This is a new sub-flavour (MECH-314d) or a parameter update to existing sub-flavours |
| Guo et al. (2024, reverse KL in PPO) [NEW] | **Reverse KL-divergence in PPO-style training structurally accelerates policy narrowing**; reverse KL is mode-seeking (concentrates on dominant mode), while forward KL is mean-seeking (spreads mass). Standard PPO uses reverse KL implicitly via the importance ratio — this is not a tuning choice, it is an architectural property | E3 training uses PPO-style updates with a KL penalty. If the KL term is reverse, this provides an additional structural accelerator for monostrategy beyond the expected-return objective. Requires: (1) audit the ree-v3 E3 update to determine KL direction; (2) if reverse, evaluate switching to forward KL or symmetric KL penalty | DEV-NEED-005, DEV-NEED-029 | MECH-309, ARC-065 | High | Urgent audit: check `ree-v3/ree_core/` E3 training objective. If using importance ratio clip (PPO-clip) or explicit reverse KL, this is a compounding structural accelerator for monostrategy. New open question: Q-G (KL direction audit — see Part 8) |

### 3.3 Premature Convergence in RL

| Source | Finding | REE relevance | DEV-NEED IDs | Claim IDs | Confidence | Action |
|---|---|---|---|---|---|---|
| Garcia & Thomas (2019 ICML, meta-learning of step sizes) | Premature convergence in RL is caused by adaptive step sizes collapsing variance; standard Adam compounds policy collapse under sparse reward | CEM elite-only updates with E3 scoring act like aggressive adaptive step sizes; diversity must be maintained at the proposal stage (SP-CEM) not only the selection stage | DEV-NEED-005, DEV-NEED-029 | ARC-065, MECH-309 | Medium | Supports SP-CEM as first-order fix; additional variance must come from proposal diversity (DEV-NEED-005) |
| Andrychowicz et al. (2021 OpenAI, what matters in RL) | Network initialisation, reward scaling, and gradient clipping interact with premature convergence; environment structure is the dominant predictor of whether diversity is maintained | Environment structure > hyperparameters for long-run diversity; consistent with EXQ-573 showing parameter scaling (10x) produces zero benefit | DEV-NEED-001, DEV-NEED-003 | ARC-065, MECH-309 | High | Strongly supports prioritising environmental enrichment (GAP-1..4) over parameter tuning |
| Nikishin et al. (2022 ICML, primacy bias) | Early training experiences have disproportionate weight on the learned policy; erasing early experiences and resetting the head periodically helps | Primacy bias: the monostrategy learned in cold infant stage persists because E3/E1 learning weights early experiences disproportionately. Infancy is the highest-risk window for primacy | DEV-NEED-001, DEV-NEED-007 | MECH-120, ARC-065, INV-055 | High | Suggests missing claim: **primacy bias during infant training compounds monostrategy** — candidate MECH extension; sleep-replay coverage priority is a mitigation |
| Sharma et al. (2021, ICLR, periodic resets) | Periodic parameter resets during RL prevent premature convergence in locomotion tasks; reset frequency is curriculum-dependent | E3 scoring reset as a curriculum parameter for infant stage: if E3 is locked to monostrategy before infant gate passes, a periodic E3 reset may recover diversity | DEV-NEED-001, DEV-NEED-029 | ARC-065, MECH-309 | Medium | Suggests experiment: periodic E3 head reset during infant stage as a structural diversity intervention |

### 3.4 Behavioral Diversity in RL

| Source | Finding | REE relevance | DEV-NEED IDs | Claim Iids | Confidence | Action |
|---|---|---|---|---|---|---|
| Eysenbach et al. (2018 ICLR, DIAYN) | Diverse skills emerge from maximising I(S;Z) — mutual information between skill discriminator and state; works without reward; produces behaviourally distinct strategies | DIAYN analog for REE: ARC-062 context discriminator must have positive I(context; action) to learn a reliable cut. EXQ-543 TV=0 = I=0 = discriminator cannot learn. Fix is upstream diversity | DEV-NEED-005, DEV-NEED-008 | ARC-062, ARC-065, MECH-269 | High | Refines ARC-062: minimum I(context; action) threshold required before discriminator training can succeed |
| Parker-Holder et al. (2020 NeurIPS, DvD) | Diversity via Determinants (DvD): volumetric (kernel matrix det) diversity exceeds pairwise distance diversity; population can be spread but lie on a degenerate manifold | V3 trajectory diversity metrics (traj_pairwise_cosine_mean) may be measuring apparent diversity; need log-det volumetric metric (DEV-NEED-029 / replay_development_analysis.md §5.1) | DEV-NEED-005, DEV-NEED-007 | Q-046, ARC-065 | High | Supports replay_volumetric_coverage metric (log-det of trajectory kernel) as the correct diversity measure |
| Cully & Demiris (2017 nature machine intelligence, MAP-Elites quality diversity) | MAP-Elites: structured archival of diverse high-quality solutions; requires environmental structure to define meaningful behaviour descriptors | ARC-064 (bottom-up rule discovery) is REE's MAP-Elites analog; requires diverse behavioral stream. EXQ-573 confirms no diverse stream exists yet | DEV-NEED-005, DEV-NEED-008 | ARC-064, ARC-065 | High | Supports existing claim (ARC-064 blocked on diversity); confirms environment structure is prerequisite |
| Zha et al. (2024 arXiv, DBER) | Diversity-based replay (DBER) outperforms prioritised replay (PER) in sparse-reward environments; diverse trajectory sampling yields better policy coverage | Infant-phase replay should use coverage priority, not RPE priority. DEV-NEED-030 (stage-aware replay scheduling) is the implementation gap | DEV-NEED-005, DEV-NEED-007 | ARC-065, MECH-285 | High | Grounds DEV-NEED-030: stage-indexed scheduler with coverage_priority for infant phase |
| Florensa et al. (2017 CoRL, reverse curriculum) | Starting from near-goal states and expanding outward produces more diverse final policies than forward curriculum; avoids premature convergence | Infant substrate is always at far-from-goal state (sparse accidental benefit = DEV-NEED-006 unmet); reverse curriculum (transient_benefit_enabled) could seed z_goal more reliably | DEV-NEED-006, DEV-NEED-003 | MECH-189, ARC-046 | Medium | Grounds GAP-3 (transient benefit patches) as a reverse-curriculum mechanism for z_goal seeding |

### 3.5 Striatal Value Learning and Habit Overconsolidation

| Source | Finding | REE relevance | DEV-NEED IDs | Claim IDs | Confidence | Action |
|---|---|---|---|---|---|---|
| Balleine & O'Doherty (2010 Neuron review) | DMS (dorsomedial striatum) supports goal-directed control; DLS (dorsolateral striatum) supports habits. Overtraining systematically shifts control from DMS to DLS; shift is irreversible under identical training after a critical period | MECH-120 (Hebbian winner-take-all) is REE's DLS habitisation mechanism. If infant training overtakes E3 goal-directed control before behavioral repertoire is established, the monostrategy habit is DLS-encoded and resistant to later diversification | DEV-NEED-005, DEV-NEED-007 | MECH-120, MECH-124, INV-056 | High | Supports MECH-120 as the neural substrate of monostrategy; suggests irreversibility if infant stage is not fixed |
| Dickinson (1985 Philos Trans R Soc) | Sensitivity to outcome devaluation dissociates goal-directed (DMS) from habitual (DLS) responding; overtraining abolishes devaluation sensitivity | E3 outcome sensitivity (devaluation of harmful trajectories) requires DMS-equivalent goal-directed substrate intact. Monostrategy = devaluation insensitivity = E3 harm evaluation not influencing selection | DEV-NEED-005, DEV-NEED-019 | MECH-120, MECH-124, SD-003 | High | Refines SD-003: counterfactual evaluation is only possible if devaluation sensitivity intact (DMS); DLS monostrategy bypasses E3 evaluation entirely |
| Corbit & Janak (2007 J Neurosci) | DLS inactivation restores goal-directed control in overtrained rats; DMS inactivation accelerates habit formation; both systems compete | MECH-120 (DLS-like) must not overwhelm E3 (DMS-like) during infant training. Disabling or attenuating MECH-120 during infancy may prevent monostrategy habitisation | DEV-NEED-005, DEV-NEED-029 | MECH-120, ARC-065 | High | Suggests falsifier: attenuate MECH-120 Hebbian reinforcement weight during infant stage; measure post-infant diversity |
| Adams et al. (2022 eLife) | Human habitual responding correlates with reduced OFC engagement; OFC lesion accelerates habit formation in healthy subjects | V_s schema-staleness accumulator (MECH-284 / OFC analog) must be active during infant stage to resist habit lock-in; if staleness accumulation fails during infancy, monostrategy is consolidation-driven | DEV-NEED-005, DEV-NEED-029 | MECH-124, MECH-284, MECH-269 | Medium | Refines MECH-284: staleness accumulator must run during infant stage to prevent early monostrategy via habit |
| Lu et al. (2019 Nat Commun) | Without MEC inputs, CA1 replay becomes rigid/stereotyped (less diverse, same sequences repeatedly). MEC lesion blocks reversal learning. Diversity loss = flexibility loss | Direct mechanistic evidence: replay diversity is upstream of behavioral flexibility. Homogenised replay (MECH-124 risk) = monostrategy-locked agent. Grounds monostrategy_prevention_score as mandatory metric | DEV-NEED-005, DEV-NEED-007 | MECH-124, MECH-285, MECH-165 | High | Supports MECH-124 as mandatory gate; monostrategy_prevention_score must be monitored per sleep cycle (DEV-NEED-031) |
| Halbout et al. (2025, mGluR5 desensitization in DLS) [NEW] | **Overtraining desensitizes mGluR5 receptors in DLS via homotypic desensitization**, blocking contingency-sensitivity. This is the cellular mechanism for MECH-124 irreversibility: mGluR5 desensitization prevents the agent from updating its DLS-encoded habit even when outcome contingencies change. The desensitization is time-locked to training duration — not to performance level | Provides a cellular grounding for MECH-124 that was previously inferred only from behavioral analogy (PTSD). Key implication: irreversibility is **time-locked, not performance-locked** — meaning the intervention window (DEV-NEED-031) closes based on number of training steps, not on whether the policy has converged. The warm-start gate must therefore be enforced at episode 0, regardless of apparent policy stability | DEV-NEED-031, DEV-NEED-029 | MECH-124, MECH-120, ARC-065 | High | Refines MECH-124: add evidence_quality_note citing Halbout 2025 as cellular mechanism. Updates the irreversibility model: the critical period is training-step-bounded (estimated <200 steps from Zeng 2025), not contingency-bounded. Raises urgency of DEV-NEED-031 monitoring to pre-training |
| Gremel & Costa (2019, DMS/DLS co-option) [NEW] | With extended training, **DMS and DLS activity patterns converge to chance-level decodability** — not simple DMS withdrawal. Both systems are co-activated after training; the DLS pattern dominates behavioral output. DMS decodability drops from >70% (early training) to chance after extended training | Refines MECH-120 description. The current MECH-120 framing (Hebbian winner-take-all → monostrategy) correctly identifies DLS as the monostrategy substrate but implies DMS withdrawal. The actual mechanism is convergence: DMS encodes a version of the same pattern but has lost its independent discriminative signal. This means goal-directed (E3) and habitual (MECH-120) systems are not opposing — they co-represent the monostrategy. Ablating MECH-120 alone will not restore diversity if E3 has also converged | DEV-NEED-005, DEV-NEED-019 | MECH-120, MECH-124, ARC-065 | High | Refines MECH-120: update evidence_quality_note to reflect co-option mechanism, not pure winner-take-all. Also refines Falsifier 2 (E3 disabling): if both DLS and E3 have converged, disabling E3 may not produce diversity (predicted FAIL is even more likely). The fix must come from the proposer and the environment (ranks 1-3), not from E3 architecture |

### 3.6 Dopamine and Action Repertoire Narrowing

| Source | Finding | REE relevance | DEV-NEED IDs | Claim IDs | Confidence | Action |
|---|---|---|---|---|---|---|
| Doupe & Kuhl (1999 Annu Rev Neurosci) | BG-driven motor variability (dopamine-dependent) is necessary for repertoire formation in songbirds; pharmacological silencing of BG output = monostrategy. Critical period is partly self-closing | MECH-320 (tonic vigor, dopamine analog) is REE's BG motor variability mechanism. EXQ-573: MECH-320 at 10x produces zero differential because EWMA is not built up. BG must fire before replay consolidates monostrategy | DEV-NEED-001, DEV-NEED-005, DEV-NEED-029 | MECH-320, ARC-065, INV-055 | High | Grounds MECH-320 biological necessity; v_t_floor as cold-start proxy for MECH-320 before EWMA (DEV-NEED-029 Q6) |
| Dhawale et al. (2017 Nat Neurosci) | Dopamine suppression (DMS) during practice reduces motor variability; dopamine restoration restores it; trial-by-trial dopamine signal scales with action variability | Dopamine variability signal must be active DURING infant practice, not only after. MECH-320 EWMA-based vigor requires prior episodes to compute EWMA — bootstrapping gap | DEV-NEED-001, DEV-NEED-029 | MECH-320, ARC-065 | High | Confirms v_t_floor as bootstrapping mechanism: provide floor tonic vigor before EWMA accumulates |
| Salamone & Correa (2012 Neuron review) | Dopamine modulates EFFORT for reward, not reward itself; dopamine depletion reduces willingness to exert effort but not hedonic value of obtained reward | MECH-320 tonic vigor is the REE analog of dopamine-effort coupling; effort bias (action vs noop) is the operationalisation; vigor deficit → noop dominance → monostrategy of inaction | DEV-NEED-001, DEV-NEED-006 | MECH-320, ARC-065, SD-012 | High | Refines MECH-320: vigor must be above noop threshold for any action repertoire to form; test: action_fraction vs noop_fraction metric |
| Beeler et al. (2012 Front Psychol) | Dopamine D2 receptor variation predicts individual differences in habit formation rate; high D2 = slower habitisation = more goal-directed residual | MECH-320 (tonic dopamine analog) modulates the rate at which monostrategy habits form; tuning MECH-320 gain can delay habitisation | DEV-NEED-005, DEV-NEED-019 | MECH-320, MECH-120 | Medium | Suggests MECH-320 gain as a curriculum parameter for habit-resistance during infant stage |
| Olveczky (2011 Curr Opin Neurobiol) | BG-thalamo-cortical pathway generates motor variability specifically during learning; variability is not noise but structured random exploration in motor latent space | MECH-313 (noise floor) + MECH-320 (vigor) together implement BG motor variability; but both are zero-differential on cold substrate; need warm E3 scores for structured randomness | DEV-NEED-001, DEV-NEED-029 | MECH-313, MECH-320, ARC-065 | Medium | Confirms pair (MECH-313 + MECH-320) as the correct mechanism; cold substrate is the block |

### 3.7 Habit Formation vs Goal-Directed Control — Developmental Transitions

| Source | Finding | REE relevance | DEV-NEED IDs | Claim IDs | Confidence | Action |
|---|---|---|---|---|---|---|
| Decker et al. (2016 Neuron) | Adolescents use more model-based (goal-directed) control than adults on two-step task; adult life leads to progressive shift toward model-free (habit). Early childhood = maximally model-based | E3 trajectory planning is REE's model-based system; MECH-120 Hebbian consolidation is model-free. Infancy must be protected as model-based dominant phase; overtraining in infancy accelerates model-free takeover | DEV-NEED-001, DEV-NEED-019, DEV-NEED-025 | MECH-120, INV-056, ARC-019 | High | Supports DEV-NEED-019 (gradual responsibility expansion) and DEV-NEED-025 (selective neoteny); E3 planning should dominate until habit substrate is ready |
| Gillan et al. (2016 eLife) | Compulsive behavior in humans = excessive habit; arises from DLS overweighting + failure of goal-directed OFC/DMS circuit; substrate is trainable but requires intact early goal-directed experience | Monostrategy in REE is the compulsive-habit analog. Intact infant goal-directed experience (E3 guidance over diverse repertoire) is the protective factor; cold-start E3 on impoverished substrate installs compulsive monostrategy | DEV-NEED-005, DEV-NEED-007 | MECH-120, MECH-124, ARC-065 | High | Confirms developmental pathology framing: monostrategy = compulsive habit from impoverished early experience |
| Otto et al. (2013 Psychol Sci) | Cognitive load degrades goal-directed control in favour of habit; under high cognitive demand, humans revert to model-free | If E3 is computationally loaded during infant training (cold network, full episode length), it defaults to model-free monostrategy; E3 load must be reduced during infancy | DEV-NEED-001, DEV-NEED-019 | ARC-019, MECH-120 | Medium | Supports E3 near-random / disabled during infant stage (ARC-019 operational parameters); confirm this is enforced in V3 |
| Smittenaar et al. (2013 Neuron) | Disrupting DLPFC (goal-directed) with TMS increases habitual responding; model-based control requires frontal resources | E3 load reduction during infant stage is not just an efficiency choice — it is a developmental protection against early model-free lock-in | DEV-NEED-001, DEV-NEED-019 | ARC-019, MECH-120, INV-055 | Medium | Supports E3 planning disabled or near-random during infant stage; ARC-019 infant operational parameter confirmed biologically |
| Noonan et al. (2010 J Neurosci) | OFC is necessary for value updating on goal-directed representations; OFC lesion = insensitivity to outcome devaluation = habit even with intact DMS | MECH-284 (staleness accumulator, OFC analog) must be active during infant training to support outcome devaluation and prevent early monostrategy habitisation | DEV-NEED-005, DEV-NEED-029 | MECH-284, MECH-124, MECH-120 | Medium | Refines: MECH-284 staleness accumulator must be active from episode 1 (not only during sleep) to prevent monostrategy habitisation |
| Daw, Niv & Dayan (2005, uncertainty arbitration) [NEW] | **Model-free (habit) control wins by default when model uncertainty is high**; the arbitration system assigns control to the system with lower prediction uncertainty. When the model-based system (E3) has not yet built a reliable world model, model-free takes over. This is not a failure — it is adaptive given the agent's epistemic state | E3's model uncertainty during cold-start infancy is maximal (cold random network). The arbitration rule therefore assigns full control to the model-free system (MECH-120) by default. This is a structural source of infant monostrategy that is entirely separate from the objective structure (Sinha 2026) or entropy dynamics (Khanh 2025). The fix is to build E3's world model BEFORE activating arbitration — which requires warm-start gating (DEV-NEED-029) | DEV-NEED-001, DEV-NEED-005, DEV-NEED-029 | MECH-120, ARC-019, ARC-065 | High | Adds a third structural source of monostrategy: uncertainty-arbitrated model-free dominance during cold start. All three interact: (1) expected-return objective causes mode collapse (Sinha 2026); (2) arbitration assigns control to model-free when model-based is uncertain (Daw 2005); (3) entropy collapse is irreversible without early intervention (Khanh 2025). All three point to the same fix: warm-start gate must be passed before E3 guidance begins |
| Hartley et al. (2016, developmental model-based control) [NEW] | **Goal-directed (model-based) control is absent in children aged 8-12**; it is emergent in adolescence and maximal in adults aged 18-25. Children's two-step task performance is statistically indistinguishable from model-free in this age window | Grounds the infant-stage necessity (INV-055): the agent cannot be expected to exhibit model-based (E3) control during developmental infancy. The infant stage is the window where model-free (MECH-120) dominance is biologically normal. Attempting to elicit E3-guided behavioral diversity during infancy is developmentally premature — consistent with the observation that E3 disabling does not worsen monostrategy (EXQ-482) | DEV-NEED-001, DEV-NEED-019, DEV-NEED-025 | INV-055, ARC-019, MECH-120, ARC-065 | High | Supports and refines INV-055 (infant stage necessity): the infant stage must be model-free dominant by design. The developmental curriculum (ARC-019) already specifies near-random E3; this source confirms the necessity is not just a warmup hack but a developmental law. Cite in INV-055 evidence_quality_note |

---

## Part 4: Causal Hypothesis Ranking

Rankings are scored on four dimensions: (E) explanatory power for the current experimental evidence, (F) falsifiability with a tractable V3 experiment, (D) developmental relevance (does this occur early enough to be upstream?), (T) implementation tractability.

| Rank | Hypothesis | E | F | D | T | Primary evidence | Next action |
|------|-----------|---|---|---|---|-----------------|-------------|
| **1** | **Environmental compressiveness (6 infant compressions in CausalGridWorldV2)** | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★★ | EXQ-573/569 zero-differential; EXQ-522 heuristic PASS (substrate CAN carry diversity); Li 2007 permanent monostrategy from isolation; Ventura 2024 flat env → flat CA3 | infant_substrate_plan.md GAP-1 through GAP-4 |
| **2** | **Cold-start / warm-start gate failure (DEV-NEED-029)** | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★ | EXQ-573: 10x bias scaling produces zero differential; EWMA not built up; ResidueField empty; E3 score variance zero; Zeng 2025: 95% entropy loss occurs in first ~200 steps | EXQ-ISEF-001 (warm-start calibration after env enrichment); gate must be enforced at episode 0 |
| **3** | **RL objective structural mode collapse (Sinha 2026)** [NEW] | ★★★★★ | ★★★ | ★★★★★ | ★★★ | Sinha 2026: expected-return maximisation mathematically guarantees mode collapse regardless of entropy bonuses, exploration, or KL regularisation; Khanh 2025: collapse is a first-order phase transition with no early warning and 2.92-nat recovery hysteresis; Guo 2024: reverse KL (PPO implicit) accelerates narrowing | Audit E3 objective in ree-v3/ree_core/: (1) verify KL direction; (2) evaluate adding trajectory-volume loss to E3 selection objective; (3) design ARC-level claim for diversity-preserving E3 objective |
| **4** | **CEM proposer-stage collapse (partially fixed)** | ★★★★ | ★★★★★ | ★★★ | ★★★★★ | EXQ-563 FAIL (candidate_first_action_entropy=0); EXQ-567 PASS (SP-CEM fixes proposer); EXQ-569 FAIL (structured mechanisms still zero) | Proposer fix done (SP-CEM); upstream causes remain |
| **5** | **E3 score variance collapse on cold substrate** | ★★★★ | ★★★★ | ★★★ | ★★★ | EXQ-573/569 zero-differential (most parsimonious cause: E3 scores uniform → CEM selection random); EXQ-561 non_contributory; Daw 2005: uncertainty arbitration assigns control to model-free (MECH-120) by default when E3 model uncertainty is maximal | E3 score variance telemetry; compare warm vs cold |
| **6** | **Replay homogenisation / MECH-124 risk** | ★★★ | ★★★★ | ★★★★ | ★★★ | EXQ-385/385a FAIL (INV-049 offline necessity); Lu 2019 MEC lesion → rigid replay; Halbout 2025: mGluR5 desensitization = cellular mechanism for MECH-124 irreversibility; content poverty confirmed | EXQ-IDEV-003 (coverage-priority vs RPE-priority replay); first requires env enrichment (rank 1) |
| **7** | **z_goal insufficiency / weak goal seeding** | ★★★ | ★★★★ | ★★★★ | ★★★★ | EXQ-550 FAIL (z_goal monostrategy falsifier); DEV-NEED-006 unmet; MECH-189 requires benefit contact under high contextual complexity | GAP-3 (transient benefit patches); EXQ-ISEF-002 |
| **8** | **Developmental replay asymmetry (no stage-aware scheduler)** | ★★★ | ★★★★ | ★★★★ | ★★★ | DEV-NEED-030 unimplemented; adult RPE-priority replay running during infancy selects against exploration; Zha 2024 DBER shows coverage > RPE in sparse reward | Implement stage-aware replay scheduler (DEV-NEED-030) |
| **9** | **Poor valence-map coverage (DEV-NEED-003)** | ★★★ | ★★★ | ★★★★ | ★★★★ | residue_coverage_pct not measured (GAP-6); DEV-NEED-004 protected harm exposure without gradients; binary harm = no geographic residue | GAP-1 harm gradient + GAP-6 telemetry |
| **10** | **Primacy bias — infant experiences disproportionately weighted** | ★★ | ★★★ | ★★★★ | ★★★ | Nikishin 2022 primacy bias; Zeng 2025: 95% entropy loss in first ~200 steps = primacy window is narrower than expected; early cold monostrategy persists because early training is over-weighted | Periodic E3 head reset during infant stage (Sharma 2021); novel experiment |
| **11** | **E3 premature activation / ARC-040 violation** | ★★ | ★★★★ | ★★★ | ★★★★★ | EXQ-482 FAIL on E3-ablated baseline = monostrategy exists even without E3; E3 not the initiator; but E3 activation may compound it; Gremel & Costa 2019: DMS/DLS co-option means disabling E3 alone cannot restore diversity | Verify E3 is disabled during infant stage per ARC-019 parameters |
| **12** | **Insufficient developmental asymmetry (uniform curriculum)** | ★★ | ★★★ | ★★★ | ★★★ | No 4-phase infant curriculum scheduler (GAP-9); all parameters flat across infant stage; Shi 2025: fixed-coefficient bonuses fail at all training phases | Implement GAP-9 curriculum scheduler; adaptive bonus scheduling |
| **13** | **Metric-induced collapse (FP-5)** | ★ | ★★★ | ★ | ★★★★ | EXQ-567 ARM_0 entropy=0.012 → argmax policy without diversity substrates; this is a symptom | Rung 0 metric (entropy without substrate) is the symptom, not the cause |
| **14** | **Play substrate absence** | ★ | N/A | ★★★★★ | ★ | Not yet entered childhood; downstream gap | Unblocked by ranks 1-9; requires V4 multi-agent |

### 4.1 Causal Chain Summary

```
THREE STRUCTURAL ACCELERATORS (independent, all converge on monostrategy)
│
├── [Rank 1] Environmental compressiveness (6 infant compressions)
│     └── Cold-start / warm-start failure (diversity mechanisms inert)
│           ├── E3 score variance collapse (cold E3 → uniform scores)
│           │     ├── CEM elite selection → random (no policy structure)
│           │     └── Uncertainty arbitration → model-free (MECH-120) by default [Daw 2005]
│           ├── Proposer-stage collapse (resolved by SP-CEM; underlying cause remains)
│           ├── z_goal near-zero (no accidental benefit contact)
│           │     └── No super-ordinal goal seeds (MECH-189 never fires)
│           ├── Replay content poverty (nothing diverse to replay)
│           │     ├── RPE-priority replay reinforces only termination-adjacent sequences
│           │     └── MECH-124 risk: mGluR5 desensitization → option-space contraction [Halbout 2025]
│           └── Poor valence-map geography (binary harm → flat residue field)
│
├── [Rank 3] RL objective structural mode collapse [Sinha 2026; Khanh 2025; Guo 2024]
│     ├── Expected-return maximisation log-diverges toward single mode regardless of entropy bonus
│     ├── PPO reverse-KL accelerates narrowing
│     └── Entropy collapse = first-order phase transition; 2.92-nat recovery hysteresis
│           └── 95% entropy lost in first ~200 training steps [Zeng 2025]
│
└── [Rank 5/combined with Rank 2] Model uncertainty → model-free arbitration [Daw 2005]
      └── Cold E3 uncertainty → MECH-120 controls behavioral output during infancy
            └── DMS/DLS co-option after extended training [Gremel & Costa 2019]:
                  both systems represent the same monostrategy; E3 disabling alone insufficient

Result: trained policy = monostrategy (action_0 dominant, context-insensitive)
        EXQ-522 heuristic PASS confirms substrate COULD carry diversity
        EXQ-573/569 confirm: mechanisms exist AND substrate is the bottleneck
        Sinha 2026 / Khanh 2025 confirm: the RL objective is a THIRD independent bottleneck
```

---

## Part 5: Targeted Falsifiers

### 5.1 Falsifier 1: Infant Substrate Insufficiency (Primary)

**Claim being tested:** Environmental compressiveness is the primary cause; enriching the infant substrate will allow diversity mechanisms to fire.

**Design:**
- Phase 1: Implement GAP-1 (harm gradient) + GAP-2 (microhabitat zones) + GAP-3 (transient benefit patches)
- Phase 2: Two-arm experiment: (A) default CausalGridWorldV2 + ARC-065 mechanisms at 5x; (B) enriched infant substrate + ARC-065 mechanisms at 5x
- Measure at episode 500: MECH-313 entropy lift, MECH-314a ResidueField center count, MECH-320 EWMA, E3_score_variance, traj_pairwise_cosine_mean, action_entropy_zone_KL

**PASS criterion:** ARM_B shows nonzero MECH-313/314/320 differential (any mechanism_entropy_lift > 0.05) AND ARM_A remains zero-differential (confirming it is the substrate, not the mechanism)

**FAIL interpretation:** If ARM_B also zero-differential, the bottleneck is deeper (candidates E3 score collapse or proposer architecture); if ARM_A shows differential, something else changed between EXQ-573 and the new run (commit hygiene issue)

**EXQ label:** EXQ-ISEF-001 (after GAP-1/2/3 implementation)

---

### 5.2 Falsifier 2: E3 Premature Commitment

**Claim being tested:** E3 is contributing to monostrategy by activating before the repertoire is established.

**Design:**
- Three arms: (A) E3 fully disabled for 500 infant episodes, then enabled; (B) E3 near-random (weight 0.01) for 500 episodes, then enabled; (C) E3 normal (current)
- Measure: policy_entropy_after_500_episodes, traj_volume_estimate, action_class_coverage at episode 500 and episode 1000

**PASS criterion:** ARM_A/B show higher policy diversity at episode 500 than ARM_C; diversity maintained through episode 1000 (i.e., delayed E3 activation produces lasting repertoire improvement)

**FAIL interpretation:** No difference between arms → E3 activation timing is not the cause; EXQ-482 FAIL (monostrategy even without E3) supports this interpretation

**PREDICTED OUTCOME:** FAIL — EXQ-482 already shows E3 is not the initiator. But this test quantifies whether E3 compounds monostrategy after initiation.

---

### 5.3 Falsifier 3: Replay Homogenisation (MECH-124)

**Claim being tested:** RPE-priority replay during infancy is accelerating monostrategy by reinforcing termination-adjacent sequences.

**Design:** Requires enriched infant substrate (Falsifier 1 must PASS first)
- Two arms post-enrichment: (A) RPE-priority replay (current); (B) coverage-priority replay (replay_zone_coverage_fraction >= 0.6, RPE_weight=0.2)
- Measure: traj_volume_estimate, monostrategy_prevention_score, action_class_coverage across 1000 episodes

**PASS criterion:** ARM_B shows monostrategy_prevention_score >= 1.0 (option space non-contracting) AND ARM_A shows monostrategy_prevention_score < 1.0 (option space contracting)

**EXQ label:** EXQ-IDEV-003

---

### 5.4 Falsifier 4: z_goal Seeding Insufficiency

**Claim being tested:** The infant environment fails to deliver accidental benefit contacts of sufficient salience and contextual complexity for z_goal seeding.

**Design:**
- Implement GAP-3 (transient_benefit_enabled, transient_benefit_prob=0.02, transient_benefit_duration=10, transient_benefit_multiplier=3.0)
- Two arms: (A) current sparse benefit; (B) transient benefit patches added
- Measure: median episodes to first z_goal.norm() > 0.4, z_goal_identity_count at episode 500, action_class_coverage at episode 500

**PASS criterion:** ARM_B reaches z_goal.norm() > 0.4 in < 50% fewer episodes than ARM_A, AND arm_B shows higher action_class_coverage (z_goal diversification leads to policy diversification)

**EXQ label:** EXQ-ISEF-002

---

### 5.5 Falsifier 5: Metric-Induced Collapse (FP-5)

**Claim being tested:** Policy diversity is present during training but collapses before evaluation (training-phase artefact, FP-5 from behavioral_diversity_acceptance_criteria.md).

**Design:** Already partially tested. EXQ-567 ARM_0 shows selected_entropy=0.012 at evaluation time; this is post-convergence entropy, not exploration-phase entropy.

**PASS criterion for FP-5:** If diversity is present during episode 1-50 but absent by episode 200 → FP-5 confirmed. Current evidence: ARM_0 shows argmax policy at convergence → FP-5 is present but is a symptom of the deeper cold-start issue.

**PREDICTED OUTCOME:** FP-5 is PRESENT but is not a CAUSE; it is the measurable end-state of the cold-start → E3 score collapse → monostrategy cascade.

---

### 5.6 Falsifier 6: Play Substrate Absence

**Claim being tested:** The absence of play substrate is a significant contributor to adult monostrategy.

**Current status:** Cannot be falsified at V3 level — childhood play is not implemented. Blocked on Falsifiers 1-4 (infant substrate must be fixed first, childhood entered, play substrate built).

**Developmental prediction:** If Falsifiers 1-4 PASS (infant substrate enriched, warm-start gate cleared, replay fixed, z_goal seeded), but the agent still shows monomodal policy after transitioning to childhood without play, then the play absence is confirmed as a downstream contributor. This is the planned V3 test sequence for DEV-NEED-009 through DEV-NEED-011.

---

## Part 6: Telemetry Additions

The following metrics are currently absent and required to monitor monostrategy onset and progression. All are flagged as `TelemetryRequired` in the developmental register.

### 6.1 Cold-Start / Warm-Start Gate Metrics

| Metric | Formula | Gate threshold | Claim IDs | Priority |
|---|---|---|---|---|
| `mech320_ewma` | Rolling EWMA of step reward; MECH-320 vigor proxy | > 0.05 before diversity sprint | MECH-320, DEV-NEED-029 | Immediate |
| `residue_field_center_count` | Count of populated RBF centers in ResidueField | > 10 before MECH-314a fires | MECH-314, DEV-NEED-029 | Immediate |
| `e3_score_variance` | Variance of E3 scores across CEM candidate set | > 0.01 before E3 selection is non-random | ARC-065, DEV-NEED-029 | Immediate |
| `warm_start_gate_all_green` | Boolean: all three criteria met | True = diversity sprint can be meaningful | DEV-NEED-029 | Immediate |

### 6.2 Monostrategy Onset Metrics

| Metric | Formula | Alarm threshold | Claim IDs | Priority |
|---|---|---|---|---|
| `action_entropy_zone_KL` | KL divergence between action distributions in different zones | < 0.05 = context-rigidity alarm | ARC-062, DEV-NEED-001 | Immediate |
| `action_class_coverage` | Count of distinct action classes used in last 100 episodes | < 2 = monostrategy alarm | ARC-065, DEV-NEED-005 | Immediate |
| `action_0_dominance` | Fraction of steps where action_0 is taken | > 0.70 = action_class_collapse alarm | MECH-309, DEV-NEED-005 | Immediate |
| `traj_pairwise_cosine_mean` | Mean pairwise cosine similarity across stored trajectories | > 0.95 = trajectory collapse | ARC-065, DEV-NEED-005 | After GAP-7 |

### 6.3 Infant Developmental Stage Metrics

| Metric | Formula | Blocking gate? | Claim IDs | Priority |
|---|---|---|---|---|
| `residue_coverage_pct` | Fraction of grid cells with |residue| > threshold | Yes: > 0.15 for infancy-to-childhood | DEV-NEED-003, DEV-NEED-004 | After GAP-6 |
| `z_goal_norm` | z_goal.norm() | Yes: > 0.4 for infancy-to-childhood | DEV-NEED-006, MECH-189 | Now |
| `h_pos` | Shannon entropy of position histogram | Advisory: > 0.65 × ln(N_cells) | DEV-NEED-001 | After GAP-5 |
| `harm_benefit_ratio` | ratio of harm vs benefit residue contacts | Advisory: [0.2, 5.0] | DEV-NEED-002, DEV-NEED-003 | After GAP-6 |
| `accidental_benefit_contacts` | Count of benefit contacts without explicit goal | Advisory: >= 5 in last 100 episodes | DEV-NEED-006 | After GAP-3 |

### 6.4 MECH-124 Prevention Metrics

| Metric | Formula | Gate threshold | Claim IDs | Priority |
|---|---|---|---|---|
| `monostrategy_prevention_score` | traj_volume_estimate post-sleep / pre-sleep | >= 1.0 per sleep cycle | MECH-124, DEV-NEED-031 | With sleep substrate |
| `option_space_contraction_rate` | Rate of decline in action_class_coverage across sleep cycles | <= 0 (non-declining) | MECH-124, DEV-NEED-031 | With sleep substrate |
| `replay_zone_coverage_fraction` | Fraction of grid zones sampled in last sleep cycle | > 0.6 in infant stage | DEV-NEED-030, DEV-NEED-007 | With sleep substrate |

---

## Part 7: Action Sequencing

The following sequencing is derived from the causal hierarchy. Earlier items are prerequisites for later items.

### Immediate (unblocked now)

1. **Warm-start gate telemetry** (GAP-5/6/7/8 from infant_substrate_plan.md): add mech320_ewma, residue_field_center_count, e3_score_variance, action_entropy_zone_KL, action_class_coverage to experiment output. These are analysis metrics only; they precede any further diversity sprint. **Revise gate timing per Zeng 2025: all criteria must be met at episode 0, not during training.**

2. **Stochastic attractor audit** (GAP-4): enumerate all random.* calls in CausalGridWorldV2 step() and reset(); classify SD-048 interoceptive noise as a potential novelty signal attractor. Block any further novelty_bonus_weight increase until audit is complete.

3. **Verify E3 is disabled during infant stage** (ARC-019 parameter check): confirm near_random=True or E3 weight < 0.05 during infant-stage runs. If not, this is an ARC-019 violation that independently compounds monostrategy.

4. **E3 objective audit** (Q-G / Q-H from Part 8): read `ree-v3/ree_core/` E3 update logic to determine KL direction (reverse vs forward) and whether the selection objective includes any trajectory-volume or diversity-preserving term. This is a code-read-only task and is unblocked now. Finding: if reverse KL confirmed, flag as structural architectural risk at governance level.

### Phase 1 (env feature implementation — unblocked, parallel)

4. **GAP-1**: Implement harm gradient parameter in CausalGridWorldV2.
5. **GAP-2**: Implement microhabitat zone parameter (Voronoi seed).
6. **GAP-3**: Implement transient benefit patches parameter.

### Phase 2 (telemetry — after GAP-1/2/3 or in parallel)

7. **GAP-5/6**: Add H_pos, zone_coverage, residue_coverage_pct telemetry.
8. **GAP-7**: Add traj_pairwise_cosine_mean at episode end.
9. **GAP-8**: Add z_goal_before/after_sleep and z_goal_retention.

### Phase 3 (validation experiments — after Phases 1+2)

10. **EXQ-ISEF-001**: Harm gradient vs binary-contact residue geography.
11. **EXQ-ISEF-002**: Transient benefit z_goal seeding rate.
12. **EXQ-ISEF-003**: Microhabitat latent diversity.
13. **EXQ-ISEF-004**: Novelty bonus Goldilocks calibration.

### Phase 4 (warm-start diversity sprint — after ISEF-001..003 PASS)

14. **Warm-start bias sweep**: Re-run EXQ-573 equivalent on enriched substrate. Expect nonzero differential for MECH-313/314/320.
15. **Warm-start matched-entropy sweep**: Re-run EXQ-569 equivalent on enriched substrate. Expect SP-CEM to beat matched-entropy on state coverage.

### Phase 5 (replay + curriculum — after Phase 4 shows warmth)

16. **Stage-aware replay scheduler** (DEV-NEED-030): implement and run EXQ-IDEV-003.
17. **MECH-124 prevention gate monitoring** (DEV-NEED-031): add monostrategy_prevention_score telemetry.
18. **4-phase curriculum scheduler** (GAP-9): implement infant-phase parameter gating.

---

## Part 8: Open Questions for Future Governance

These questions are not yet Q-claims but arise directly from this analysis. Each could become a Q-claim or ARC-claim in a future registration session.

| Question | Why it matters | Suggested resolution path |
|---|---|---|
| Q-A: Does periodic E3 head reset during infant stage prevent monostrategy lock-in? (Nikishin 2022 primacy bias) | Primacy bias may compound monostrategy even after env enrichment | Novel experiment: 3-arm (no reset / reset-100 / reset-200) on enriched substrate |
| Q-B: Is the monostrategy habit irreversible after critical period? (Li 2007, Balleine 2010) | If monostrategy is irreversible after a critical period, the ordering constraint (fix infant FIRST) is not just efficiency — it is mandatory | Experiment: train on impoverished substrate for 1000 episodes, then switch to enriched; measure diversity recovery vs train on enriched from episode 1 |
| Q-C: Should MECH-320 v_t_floor serve as a developmental bootstrapping parameter separate from adult MECH-320? | v_t_floor bypasses EWMA warmup; provides immediate action/noop bias in infant stage before EWMA accumulates | Add v_t_floor to infant curriculum parameter set; evaluate action_fraction vs noop_fraction |
| Q-D: Does MECH-284 staleness accumulator need to be active during infancy (not only sleep)? (Noonan 2010 OFC lesion → habit acceleration) | Staleness accumulator may need to resist monostrategy habitisation in real-time during waking exploration | Ablation: MECH-284 ON vs OFF during infant stage; measure post-infant strategy switching |
| Q-E: What is the minimum ResidueField center count required for MECH-314a to produce non-zero novelty signal? | DEV-NEED-029 requires a gate criterion; the threshold must be calibrated | EXQ-ISEF-001 will provide data; extract from residue_field_center_count vs entropy_lift curve |
| Q-F: Is context-rigidity (Denisova & Zhao 2017) the correct measurable signature of developmental monostrategy, rather than entropy collapse? | action_entropy_zone_KL may be a more sensitive early biomarker than global entropy | Add action_entropy_zone_KL telemetry; compare sensitivity to global H(a|s) across runs |
| Q-G: Is the ree-v3 E3 training objective using reverse KL or forward KL? (Guo 2024) — **ANSWERED 2026-05-16** | **RESOLVED: Guo 2024 reverse-KL concern does not apply to E3.** E3 is not a policy-gradient module. It is a trajectory evaluator with a fixed cost function `J(ζ) = F(ζ) + λ·M(ζ) + ρ·Φ_R(ζ) - β·B(ζ) - η·novelty` and softmax selection (e3_selector.py:544, 772). No PPO, no importance ratio clipping, no KL term of any kind. **Residual concern:** softmax temperature is fixed at 1.0 (non-adaptive). This is the Shi 2025 problem: a fixed-coefficient entropy parameter cannot adapt to training-phase entropy dynamics. The temperature should be treated as a curriculum parameter, highest at infant stage and decreasing as the warm-start gate passes. Check E1/E2 separately for PPO-style updates if monostrategy persists post-env-enrichment. | Closed for E3. Recommend: add softmax_temperature to infant curriculum parameter set (DEV-NEED-029 / GAP-9) |
| Q-H: Does the E3 selection objective need a trajectory-volume term to be monostrategy-resistant? (Sinha 2026) | If mode collapse is mathematically guaranteed from expected-return maximisation, no amount of diversity mechanism tuning (MECH-313/314/320) will prevent it — the objective must be reformed | Design a trajectory-volume or max-entropy term for the E3 selection objective; propose as a new ARC-level claim for governance |
| Q-I: What is the precise first-episode warm-start gate? (Zeng 2025 — 95% entropy loss in first ~200 steps) | If 95% of entropy is lost in the first 200 training steps, the warm-start gate must be satisfied at episode 0, not during training. The current gate criteria (DEV-NEED-029) are specified as "before diversity sprint" without a step-count anchor | Revise DEV-NEED-029 gate: all criteria (EWMA, ResidueField center count, E3 score variance) must be met before episode 1 of E3-guided training. Add step-count monitoring to warm-start gate dashboard |

---

## Related Claims

- **ARC-065** (behavioral diversity generation pathway — architectural commitment)
- **ARC-062** (rule apprehension via gated policy — blocked on Rung 2 clearance)
- **ARC-064** (bottom-up rule discovery — blocked on diverse behavioral stream)
- **ARC-019** (developmental curriculum — infant operational parameters)
- **ARC-046** (infant hazard protection mechanism)
- **MECH-120** (Hebbian winner-take-all → monostrategy risk)
- **MECH-124** (consolidation-mediated option-space contraction — PTSD analog)
- **MECH-260** (dACC anti-recency suppression)
- **MECH-309** (V_s monostrategy — the mechanism under test)
- **MECH-313** (stochastic noise floor / LC-NE tonic analog)
- **MECH-314** (structured curiosity bonus / a/b/c sub-flavours)
- **MECH-320** (tonic vigor / dopamine effort-motivation analog)
- **MECH-189** (super-ordinal goal formation in childhood)
- **INV-049** (offline phases mathematical necessity)
- **INV-055** (infant stage necessity)
- **INV-074** (behavioral diversity structural prerequisite for ethical counterfactual evaluation)
- **SD-017** (sleep phase architecture)
- **DEV-NEED-001 through DEV-NEED-008** (infant stage developmental needs)
- **DEV-NEED-029** (ARC-065 warm-start gate)
- **DEV-NEED-030** (stage-aware replay scheduling)
- **DEV-NEED-031** (MECH-124 prevention gate)
- **Q-046** (minimum trajectory-class diversity floor for ARC-062)
- **Q-047** (sleep consolidation: diversity-preserving or diversity-eroding?)
