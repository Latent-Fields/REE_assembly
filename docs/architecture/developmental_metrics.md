---
nav_exclude: true
---

# Developmental Metrics

<!-- version: 2026-05-16.1 -->
<!-- author: claude-sonnet-4-6, session dev-metrics-design-2026-05-16T123718Z -->

**Cross-references:** [`developmental_needs_register.md`](developmental_needs_register.md) | [`developmental_curriculum.md`](developmental_curriculum.md) | [`infant_substrate_expansion.md`](infant_substrate_expansion.md) | [`control_plane.md`](control_plane.md)

---

## Purpose

This document converts the narrative developmental gates in `developmental_needs_register.md`
into measurable, non-Goodharted metrics. For each DEV-NEED it specifies:
- Quantitative metrics and their thresholds
- Qualitative governance checks
- Telemetry signals and MECH-042 channels
- Maturation indicators (trajectory over time, not just crossing)
- Failure signatures (what bad looks like, not just what good looks like)
- Substrate-readiness / behavioural-readiness / governance-readiness distinctions

**Design principle throughout:** metrics diagnose development, they do not optimise behaviour.
A metric that can be Goodharted into a high score without developmental progress is a wrong metric.
Single-scalar collapse is explicitly prohibited — every gate requires a family of signals.

---

## Anti-Goodhart Taxonomy

Before the DEV-NEED metrics, this taxonomy identifies the failure modes that metric design must avoid.

| Anti-pattern | Description | Example of the mistake | Correction |
|---|---|---|---|
| **Monostrategy masquerade** | High aggregate metric via single behavioural mode repeated at scale | Action entropy computed globally: agent moves right 100% of time in zone A, left 100% in zone B → global H is ln(2) but each zone has H=0 | Always compute entropy per context-zone, not globally |
| **Action-frequency confusion** | Treating how often an action is used as evidence of how richly it is used | z_harm fires on every hazard contact; high fire rate ≠ calibrated harm geometry | Measure activation profile shape, not incidence count |
| **Short-term reward priority** | Metrics that reward fast reward accumulation at the expense of developmental breadth | Sum-of-rewards as childhood readiness gate: agent that collects adjacent resource every step gets high score without building multi-step competence | Use competence-progress (learning-rate) not level; use transfer-test, not in-training reward |
| **Synthetic calibration leak** | Policy trained in synthetic mode with magnitude imprint passing as real-domain competence | High play-task success transferring into inflated harm/goal weights in real episodes | Test with rank-correlation metrics (SCC) not absolute magnitude metrics |
| **Saturation misread** | Metric at ceiling misread as developmental readiness when it may indicate monostrategy lock-in | action_entropy = ln(5) throughout — could mean rich repertoire or random walk | Pair entropy with coherence metric: does entropy come from multi-modal policy or noise? |
| **Implicit-explicit collapse** | Using one number for what are two architecturally distinct capacities | "ToM score" combining reactive belief-tracking and planning-gated attribution | Always report reactive (implicit) and planning-gated (explicit) components separately |

---

## Metric Readiness Vocabulary

Each metric is tagged with the substrate context in which it becomes meaningful:

- **SubstrateReady:** can be computed from current V3 instrumentation with no new features
- **TelemetryRequired:** V3 with added telemetry hooks (training loop or per-step logging)
- **EnvExtension:** requires environment feature not yet implemented (from `infant_substrate_expansion.md`)
- **V4Required:** requires multi-agent substrate; V3 can only proxy
- **GovernanceOnly:** not a runtime metric; checked in governance review or experiment audit

---

## Consolidated Literature Evidence Table

Literature sources from four parallel pulls (2026-05-16) and `infant_substrate_expansion.md`.

| Source | Key finding | REE relevance | DEV-NEED IDs | Claim IDs | Confidence | Classification |
|---|---|---|---|---|---|---|
| Diamond (2013, Ann Rev Psych) | Inhibitory control detectable from 6 months (A-not-B); cognitive flexibility (DCCS) detectable 3–4 years; perseveration rate is the canonical failed-gate signature | Perseveration rate on rule-switch = REE failure signature for stage-exit gate | DEV-NEED-001, DEV-NEED-026 | INV-055, INV-060 | High | suggests implementation metric |
| Blankenship et al. (2019, Dev Sci; PMC6722030) | EF trajectory is continuous not step-change; single attention metric at 5 months predicts WM at 10 months and academics at 6 years | Stage gates must be thresholds on continuous curves, not binary presence/absence | DEV-NEED-008, DEV-NEED-026 | ARC-019, INV-060 | High | refines existing claim |
| Zelazo (DCCS literature, 3–5yr) | ~50% pass rate at age 3–4, 80% at 5, 92% at 6; failure = perseveration on prior rule despite instruction; multi-rule integration required for abstract goal maintenance | DCCS perseveration ↔ REE E3 failure to update trajectory when rules change | DEV-NEED-008, DEV-NEED-019 | ARC-019, INV-055 | High | suggests implementation metric |
| Reilly et al. (2022, Dev Sci; PMC9296695) | 60% of EF growth at ages 3–4; nonlinear; single-factor best fit for young ages | Single-factor gate metric may suffice early; multi-criterion needed after differentiation | DEV-NEED-008 | ARC-019 | High | refines existing claim |
| Howard et al. (2024, Children; PMC11275069) | Three EF batteries compared (n=846); inhibitory control and set-switching are dissociable failure modes; composite passes can mask component failures | Need sub-scores not composites at transition boundaries | DEV-NEED-008, DEV-NEED-026 | IMPL-019 | High | suggests implementation metric |
| Zelazo & Carlson (hot/cool EF) | Cool EF (inhibition, WM, planning) vs hot EF (delay of gratification, affective commitment); 2-year dissociation observable | Separate gate criteria: cool EF for E3 planning chain, hot EF for harm-weighted commitment | DEV-NEED-019, DEV-NEED-020 | INV-055, ARC-019 | Medium-high | suggests missing claim |
| Sadozai et al. (2024, Nature Human Behaviour) | EF delay transdiagnostic meta-analysis (g=0.56, 180 studies); ADHD=inhibition; ASD=set-switching | Failed-gate signatures are disorder-specific and dissociable; separate sub-scores needed | DEV-NEED-008 | ARC-019, INV-055 | High | suggests implementation metric |
| Forestier et al. (JMLR 2022, IMGEP) | Competence-progress (d(success_rate)/dt) drives self-organized developmental stage ordering in robots; LP near zero = stage complete | LP-based gating for DEV-NEED-008/010/011 is theoretically correct and empirically validated | DEV-NEED-008, DEV-NEED-010 | ARC-019, IMPL-019 | High | suggests implementation metric |
| Baillargeon et al. (Cognition 2019; PMID 31445431) | Meta-analysis: implicit false-belief success does NOT correlate with explicit false-belief success; two paradigms dissociate | Otherness inference needs implicit (reactive) + explicit (planning-gated) components; single ToM score is invalid | DEV-NEED-021 | ARC-010, MECH-031 | High | suggests missing claim |
| Hyde et al. (J Neurosci 2018; PMID 29593053) | TPJ fNIRS: belief-tracking onset at 7 months, pre-linguistic | TPJ belief-tracking is pre-linguistic; MECH-031 should document this; otherness gate precedes language gate | DEV-NEED-021 | MECH-031, MECH-032 | High | refines existing claim |
| McDonald & Messinger (2020, ScienceDirect) | Optimal empathic response requires intermediate vicarious arousal; too-low = callousness, too-high = egoistic drift | Empathy coupling has mandatory gain bounds; out-of-range = self/other signal swap | DEV-NEED-022 | MECH-036, INV-043 | High | suggests implementation metric |
| Salles et al. (PsyCh Journal 2024) | Moderate similarity → empathic concern; high similarity → personal distress; continuous graded effect | Loveability coupling must have upper bound; above threshold, coupling inverts | DEV-NEED-017, DEV-NEED-022 | MECH-036, ARC-047 | Moderate | suggests implementation metric |
| Martin, Martin & McAuliffe (2021; PMID 34424010) | Direct punishment feedback increases cooperative sharing; reputation alone does not; outcome-driven before intent-modelled | Early cooperative norm compliance is punishment-prediction-driven; MECH-032 needs outcome + intent channels | DEV-NEED-013, DEV-NEED-014 | MECH-032, ARC-049 | High | suggests missing claim |
| Luckman et al. (PLOS One 2022) | Bayesian norm-belief updating distinguishes rule-following from strategic manipulation; update rate varies by age | norm_belief_update_rate as DEV-NEED-013 metric separating compliance from mimicry | DEV-NEED-013 | MECH-032, ARC-049 | Moderate-high | suggests implementation metric |
| Brain Stimulation TPJ TMS (2025 meta-analysis) | TPJ-TMS: causal dissociation between mentalizing (belief) and norm-decision channels | MECH-032 needs separate belief-tracking and norm-computation sub-channels | DEV-NEED-013, DEV-NEED-014 | MECH-032, ARC-049 | High | refines existing claim |
| Across-six-societies (Commun Psych 2025; n=535 children) | Third-party punishment universal by age 5 across all cultures | Cooperative frame violation detection is species-general; INV-043 universality supported | DEV-NEED-014 | INV-043, ARC-049 | High | supports existing claim |
| Bekoff (1995, Behaviour) | Play bows cluster non-randomly before/after high-risk actions mid-episode; punctuation not just open/close | ARC-049 must specify ongoing heartbeat mechanism, not just open/close tags | DEV-NEED-009, DEV-NEED-012 | INV-059, ARC-049, MECH-196 | 0.72 | refines existing claim |
| Jacquey et al. (Front Neurorobotics 2019) | Competence-calibration dissociation at 7 months; bidirectional contingency knowledge precedes calibrated action selection | MECH-195 empirically supported; gate must test motor specificity not raw success | DEV-NEED-009, DEV-NEED-010, DEV-NEED-011 | INV-060, MECH-194, MECH-197, ARC-050 | 0.75 | suggests implementation metric |
| Eysenbach et al. (ICLR 2019, DIAYN) | I(S;Z) = mutual information between states and skills; policy structure (I(S;Z)) decoupled from reward magnitude | I(S;Z) operationalises DEV-NEED-011 strategy-calibration dissociation; rollout diversity gate | DEV-NEED-010, DEV-NEED-011 | MECH-194, MECH-195, ARC-050 | 0.68 | suggests implementation metric |
| Khor & Weng (arXiv 2025) | Spearman rank correlation between synthetic and real competence rankings; theorem proves structure and magnitude are independent | SCC as DEV-NEED-011 constructive play gate: does competence ranking survive the synthetic-to-real transition? | DEV-NEED-011 | MECH-195, MECH-196 | 0.62 | suggests implementation metric |
| Panelli et al. (Front Robotics AI 2025) | Three-criterion definition: pleasant + voluntary + intrinsically-motivated; frame collapse when any fails | ARC-049 frame tag must detect all three conditions, not just bilateral signal | DEV-NEED-009, DEV-NEED-012, DEV-NEED-013 | INV-058, INV-059, ARC-049 | 0.66 | refines existing claim |
| Petanjek et al. (PNAS 2011; PMC3156171) | PFC synaptic spine density exceeds adult values by 2–3× at birth; spine elimination continues through third decade | PFC-homologue substrates (E3, planning) should have longest plasticity schedule | DEV-NEED-025 | MECH-159, ARC-048 | High | supports existing claim |
| Geschwind & Rakic (PNAS 2013) | Transcriptional neoteny is substrate-selective (synaptogenesis gene networks); NOT global | Per-substrate plasticity close schedule (not global adult flag) is biologically correct | DEV-NEED-025 | ARC-048, INV-056 | High | refines existing claim |
| Lasch et al. (Infancy 2023; PMC9899317) | Responding to joint attention (RJA) at 10–11 months predicts vocabulary growth; pre-linguistic | RJA-analogue score is quantifiable pre-linguistic language-readiness gate | DEV-NEED-023 | MECH-042, ARC-013 | High | suggests implementation metric |
| Kuhl (2011, Social Mechanisms in Early Language) | Live social interaction required; video/audio alone → near-zero learning; contingency, not exposure, gates phonological mapping | Language readiness requires bidirectional contingency, not threshold exposure | DEV-NEED-023, DEV-NEED-024 | ARC-013, MECH-042 | High | refines existing claim |
| Somerville et al. (PLOS Comp Bio 2022; pcbi.1010120) | Developmental shift from model-free aggregation to model-based intervention for controllability detection | Self-impact attribution has two modes; model-based mode required for non-trivial responsibility | DEV-NEED-020 | MECH-189, ARC-019 | High | suggests missing claim |
| Hamid et al. (Nature 2025) | Striatal dopamine encodes action PE separately from reward PE; dissociation is causal | Action PE and reward PE are neurally and computationally dissociable; REE self-impact channel must separate them | DEV-NEED-020 | MECH-189 | High | supports existing claim |
| Shin et al. (Nature Commun 2025) | Post-task replay biased toward RPE signals; RPE-biased replay predicts subsequent behaviour | Replay quality = RPE-bias selection, not recency or novelty; consolidation gate needs RPE-priority score | DEV-NEED-007 | INV-056, ARC-048 | High | refines existing claim |
| Joo & Frank (Science 2024) | SWR incidence increases with novelty and harm salience; salient trials over-represented in offline replay | Harm salience is a natural SWR-gating factor; use harm-salience-weighted replay priority | DEV-NEED-007, DEV-NEED-025 | INV-056, MECH-159 | High | refines existing claim |

For earlier infant-stage literature (motor babbling, curiosity/novelty, safe exploration RL, affordance/valence) see `infant_substrate_expansion.md` §3.

---

## Metric Families Per DEV-NEED

### Infant Stage (DEV-NEED-001 – DEV-NEED-008)

---

#### DEV-NEED-001 — Sensorimotor Grounding

> Stable prediction-error bounds, safe harm avoidance, coherent self/world attribution.

**Substrate readiness:** V3 with telemetry additions.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `H_pos` | Shannon entropy of position histogram over rolling 100-episode window | > 0.65 × ln(grid_cells²) | YES | TelemetryRequired |
| `zone_coverage` | Fraction of each zone's cells visited in last 100 episodes | > 0.60 all zones | advisory | EnvExtension |
| `action_entropy_by_zone` | H(action \| zone_A), H(action \| zone_B) — must differ | KL(A\|B) > 0.05 | advisory | TelemetryRequired |
| `perseveration_rate` | Fraction of episodes where agent repeats same directional sequence despite changed hazard layout | < 0.25 | advisory | TelemetryRequired |
| `self_world_attribution_consistency` | Correlation of self-caused vs world-caused latent changes; should be low | r < 0.4 | advisory | TelemetryRequired |

**Maturation indicators:** `H_pos` and `zone_coverage` should show monotonically increasing trends over infant phase (EF literature: continuous trajectory, not step). A plateau below threshold followed by restart is not a clean pass — log the plateau length.

**Failure signatures:**
- **Context-rigidity:** `action_entropy_by_zone` is high globally but near-zero per zone (Denisova & Zhao 2017 ASD analogue)
- **Monostrategy lock-in:** `perseveration_rate` > 0.5 for > 200 consecutive episodes
- **Self/world confusion:** `self_world_attribution_consistency` r > 0.6 persistently

**Governance check:** Before claiming DEV-NEED-001 cleared, confirm `perseveration_rate` and `self_world_attribution_consistency` are both measured (not just `H_pos`). `H_pos` alone admits the context-rigidity failure.

---

#### DEV-NEED-002 — Harm/Homeostasis Separation

> HARM and HOMEOSTASIS channels trained as distinct signals; z_harm_s and z_harm_a fire during protected exposure without collapsing into drive.

**Substrate readiness:** V3 substrate-ready (channels exist); telemetry additions needed.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `harm_homeostasis_channel_correlation` | Pearson r between z_harm_s magnitude and z_homeostasis drive_level over a test window | < 0.3 | YES | TelemetryRequired |
| `harm_channel_activation_rate` | Fraction of hazard-proximity steps where z_harm_s > threshold | > 0.70 | YES | TelemetryRequired |
| `homeostasis_independent_activation` | Does homeostatic drive fire under non-harm depletion (energy_decay)? Ablation: does drive still fire if harm is suppressed? | YES (boolean check) | advisory | TelemetryRequired |
| `residue_vs_drive_correlation` | Correlation between residue accumulation and drive_level magnitude | < 0.4 | advisory | TelemetryRequired |

**Failure signatures:**
- **Harm-as-drive substitution:** high `harm_homeostasis_channel_correlation` (> 0.5) means E3 learns harm as a hunger-proxy; harm avoidance becomes drive-reduction
- **Drive collapse:** homeostasis drive_level does not vary with energy_decay state independently of harm exposure
- **Residue saturation as drive:** `residue_vs_drive_correlation` > 0.5 indicates drive using residue channel

**Governance check:** Run a 20-episode ablation with harm suppressed (hazard contacts suppressed) — confirm homeostatic drive still fires normally. This is the channel-separation test.

---

#### DEV-NEED-003 — Infant Valence-Map Formation

> Residue field populated with harm/benefit geography sufficient for childhood constraints and sleep consolidation.

**Substrate readiness:** V3 with environment extension (harm gradient, Section 5.1 of `infant_substrate_expansion.md`).

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `residue_coverage_pct` | Fraction of grid cells with \|residue\| > 0.05 | > 0.15 | YES | EnvExtension |
| `residue_harm_cells` | Count of cells with harm residue > 0.05 | > 5 (10×10 grid) | advisory | TelemetryRequired |
| `residue_benefit_cells` | Count of cells with benefit residue > 0.05 | > 5 | advisory | TelemetryRequired |
| `harm_benefit_ratio` | residue_harm_cells / residue_benefit_cells | [0.2, 5.0] | advisory | TelemetryRequired |
| `residue_curvature_index` | Local second-derivative of residue field (geography is not flat) | > 0.01 mean | advisory | TelemetryRequired |

**Maturation indicator:** `residue_coverage_pct` should grow monotonically during Phase 1–2 of infant curriculum. Flat coverage for > 300 episodes after Phase 1 onset = curriculum stall.

**Failure signatures:**
- **Zero harm geography:** agent avoids all hazard contact → residue_harm_cells ≈ 0 → sleep has nothing to consolidate
- **Flat field (no curvature):** residue values uniform — geography exists but carries no spatial information
- **One-sided valence:** harm_benefit_ratio < 0.1 (pure punishment learning) or > 10 (pure reward learning)

**Governance check:** After each offline integration pass, measure change in `residue_coverage_pct` and `residue_curvature_index`. If sleep produces no delta, replay is not using the field productively.

---

#### DEV-NEED-004 — Protected Harm Exposure

> z_harm_s and z_harm_a fire normally; residue accumulation stays below catastrophic saturation; protection removed gradually.

**Substrate readiness:** V3 substrate-ready (curriculum parameters).

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `z_harm_s_activation_rate` | Fraction of hazard-proximity episodes with z_harm_s > threshold | > 0.50 | YES | TelemetryRequired |
| `residue_saturation_pct` | Fraction of grid cells with \|residue\| > 0.90 (near-ceiling) | < 0.15 | YES | TelemetryRequired |
| `episode_termination_rate` | Fraction of episodes ending in terminal hazard contact | < 0.30 | advisory | SubstrateReady |
| `protection_removal_schedule_adherence` | Is residue_scale_factor decreasing on schedule? | Monotone increase over infant phases | advisory | GovernanceOnly |

**Failure signatures:**
- **Terminal saturation:** `residue_saturation_pct` > 0.40 → field is fully saturated; geometry lost; recovery requires reset
- **Zero nociception:** `z_harm_s_activation_rate` < 0.10 → harm pathways not trained; ethical architecture missing foundation
- **Premature de-protection:** Protection removed too fast → `episode_termination_rate` spikes → agent destroyed before avoidance learned

**Governance check:** Confirm protection is being removed gradually (not abruptly). Log `residue_scale_factor` value at each infant phase transition.

---

#### DEV-NEED-005 — Behavioural Repertoire Before Childhood

> Behavioral entropy below pure-random ceiling but broad enough for multiple viable state-transition classes.

**Substrate readiness:** V3 with telemetry.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `action_entropy_global` | H over full episode action distribution | > ln(3) (3 effective actions) | advisory | TelemetryRequired |
| `action_class_coverage` | Bitmask: which action classes used ≥ 5× across last 100 episodes | All 5 classes | advisory | TelemetryRequired |
| `traj_pairwise_cosine_mean` | Mean cosine distance between N sampled trajectory pairs | > 0.3 | advisory | TelemetryRequired |
| `traj_volume_estimate` | log-det of trajectory kernel matrix (DvD-style volumetric; approximate) | > -5 (log-scale) | advisory | TelemetryRequired |
| `action_entropy_zone_KL` | KL divergence between H(action\|zone_A) and H(action\|zone_B) | > 0.05 | advisory | EnvExtension |

**Important exclusion:** Strategic diversity (E3 trajectory class count) is explicitly NOT a target here. Strategic diversity before childhood is the wrong signal — it indicates premature E3 convergence. Infant repertoire diversity is exploration diversity at the action-class level, not trajectory planning level.

**Maturation indicator:** `traj_volume_estimate` should grow from near-zero (early infant) to above threshold. A plateau indicates monostrategy basin entry.

**Failure signatures:**
- **Monostrategy lock-in (early):** `action_class_coverage` ≤ 2 classes for 200+ episodes
- **Random walk (uninformative high entropy):** `action_entropy_global` at max but `traj_pairwise_cosine_mean` < 0.1 — agent is noisy, not diverse
- **Context-rigidity:** `action_entropy_zone_KL` ≈ 0 (same action distribution regardless of zone)

**Note on Parker-Holder:** DvD shows pairwise cosine distance ≠ volumetric coverage. Always compute both `traj_pairwise_cosine_mean` AND `traj_volume_estimate`. A population can be pairwise-spread but degenerate (volume ≈ 0).

---

#### DEV-NEED-006 — z_goal Seeding from Accidental Benefit

> z_goal seeded by accidental benefit contacts before deliberate planning.

**Substrate readiness:** V3 with telemetry and environment extension (transient benefit patches).

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `z_goal_norm` | L2 norm of z_goal vector | > 0.4 | YES | SubstrateReady |
| `accidental_benefit_contacts` | Benefit contacts occurring when agent was NOT pursuing an explicit goal target (no z_goal-active episodes) | ≥ 5 in last 100 episodes | advisory | TelemetryRequired |
| `z_goal_identity_count` | Count of distinct resource-identity signatures in z_goal writes (from SD-049) | > 1 (for multi-resource) | advisory | TelemetryRequired |
| `z_goal_write_traceable` | Are all z_goal write events causally traceable to benefit encounters in the same episode? | > 90% | advisory | TelemetryRequired |

**Note on Berridge (wanting before liking):** z_goal seeding proceeds via the WANTING pathway before LIKING is calibrated. An infant agent with `z_goal_norm` > 0 from accidental contact may not yet have calibrated liking weights. Both signals exist but wanting bootstraps first — this is expected and not a failure.

**Failure signatures:**
- **Goal starvation:** `z_goal_norm` stays near zero for > 500 episodes despite normal exploration → environment not delivering benefit contacts (adjust transient_benefit_prob) or z_goal write pathway misconfigured
- **Goal write without benefit contact:** `z_goal_write_traceable` < 0.5 → confabulated goal seeding from non-benefit signals (noise or misattribution)

---

#### DEV-NEED-007 — Frequent Offline Integration During Early Development

> Each developmental transition preceded by offline passes improving map stability, goal seeds, and repertoire quality.

**Substrate readiness:** V3 with telemetry.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `post_sleep_z_goal_retention` | z_goal.norm() ratio before/after sleep integration | > 0.85 | advisory | TelemetryRequired |
| `residue_consolidation_delta` | Change in residue field coverage after sleep integration | > 0 (positive delta) | advisory | TelemetryRequired |
| `replay_RPE_priority_score` | Fraction of replayed episodes with RPE > mean_RPE (from Shin et al. 2025) | > 0.6 | advisory | TelemetryRequired |
| `replay_diversity_index` | Fraction of replay episodes drawn from distinct zones vs. dominant zone | > 0.4 | advisory | TelemetryRequired |
| `sleep_wake_ratio` | Steps in offline integration / steps in waking episode | > 0.10 during infancy | advisory | TelemetryRequired |

**Maturation indicator:** `post_sleep_z_goal_retention` should approach 1.0 as consolidation improves. Retention < 0.7 after 1000 episodes indicates structural replay issue.

**Failure signatures:**
- **Zero consolidation delta:** `residue_consolidation_delta` ≈ 0 after every offline pass → replay is not using residue field (misconfiguration)
- **Low RPE priority:** `replay_RPE_priority_score` < 0.3 → random replay; consolidation is noise; the Shin et al. (2025) biological optimum is being missed
- **Single-zone replay:** `replay_diversity_index` < 0.15 → replay replays same few episodes; field geometry not being integrated

---

#### DEV-NEED-008 — Transition Gate from Infancy to Childhood

**All 7 criteria from `infant_substrate_expansion.md` §8 apply (unchanged here).** This section adds the EF literature requirement and multi-criterion structure.

**Blocking criteria (must all pass):**
1. `z_goal_norm` > 0.4 (DEV-NEED-006)
2. `H_pos` > 0.65 × ln(grid_cells²) rolling 100-episode (DEV-NEED-001)
3. `residue_coverage_pct` > 0.15 (DEV-NEED-003/004)

**Advisory criteria (flag if missing; allow transition with supervisor override):**
4. `action_entropy_global` > ln(3) AND `action_entropy_zone_KL` > 0.05 (DEV-NEED-005)
5. `harm_benefit_ratio` in [0.2, 5.0] (DEV-NEED-004)
6. `post_sleep_z_goal_retention` > 0.85 (DEV-NEED-007)
7. `traj_pairwise_cosine_mean` > 0.3 (DEV-NEED-002, DEV-NEED-005)

**Additional gate from EF literature (Forestier et al. 2022, JMLR):**
8. `competence_progress_rate` (d(multi_step_success)/dt over 100-episode window) must be > 0 at transition point — agent should still be learning, not at plateau. A plateaued infant at ceiling may be monostrategy-locked, not ready for childhood.

**Gate blocker: perseveration rate check.** If `perseveration_rate` > 0.4 at any of criteria 1–3 pass time, flag: the agent may be reaching thresholds via repeated single strategy. Request governance review before advancing.

**Failure signatures at gate:**
- **False pass:** Criteria 1–3 met via monostrategy (high z_goal from one repeated resource, high H_pos from pure random walk); detected by `perseveration_rate` + `traj_volume_estimate`
- **Premature advance:** Advancing despite advisory criteria 4–7 flagged → childhood play has nothing to constrain; INV-060 prerequisites unmet

---

### Childhood / Play Stage (DEV-NEED-009 – DEV-NEED-018)

---

#### DEV-NEED-009 — Play-Dominant Childhood

> Play is primary learning mode; goal-pursuit competence transfers to real-consequence episodes.

**Substrate readiness:** Requires play substrate (partially V3-testable via degenerate experimenter-set mode).

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `play_fraction` | Fraction of training episodes marked as play-type | > 0.70 during child phase | GovernanceOnly | V4Required (full) |
| `goal_pursuit_transfer_score` | Performance on real-consequence episodes using play-acquired skills | > 0.6 relative to play-training performance | advisory | V4Required (full); V3 proxy available |
| `competence_progress_rate_play` | d(play_success_rate)/dt over 100-episode window | > 0 (still learning; not saturated) | advisory | TelemetryRequired |
| `play_integrity_indicator` | Is the play-frame tag maintained throughout episode? Fraction of episodes without frame collapse | > 0.90 | advisory | V4Required |

**Panelli three-condition check (governance):** For each play episode type, check: (a) is it voluntary (not externally forced), (b) is it intrinsically motivated (not purely reward-seeking), (c) is it pleasant (agent not in harm-avoidance mode). A play episode failing any one condition is not genuine play and should not count toward `play_fraction`.

**Failure signatures:**
- **Childhood without play:** `play_fraction` < 0.3 → E3 trained only on real-consequence episodes; harm exposure without safe exploration
- **Saturated play, premature exit:** `competence_progress_rate_play` ≈ 0 for 300+ episodes but child phase not exited → agent stuck at ceiling or at floor without transition

---

#### DEV-NEED-010 — Sensorimotor Play

> E1/E2 improve on action-outcome prediction under play without requiring real harm or benefit.

**Substrate readiness:** Partially V3-testable.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `E1_prediction_error_play_improvement` | Delta in E1 prediction error over play episodes (must improve) | Negative delta (decreasing) | advisory | TelemetryRequired |
| `motor_specificity_score` | Different action classes produce detectably different E2 transition distributions | p < 0.05 per action class | advisory | TelemetryRequired |
| `action_outcome_coverage` | Coverage of (action, outcome_type) pairs in play episode store | > 0.60 of possible pairs | advisory | TelemetryRequired |
| `sensorimotor_competence_progress` | Jacquey metric: rate of retention interval extension over play episodes | Positive derivative | advisory | TelemetryRequired |

**Failure signatures:**
- **Stagnant E1 during play:** `E1_prediction_error_play_improvement` flat or positive → play not training the sensorimotor model; episode design may be too random
- **Action equivalence:** `motor_specificity_score` fails → all action classes produce statistically identical E2 transitions → environment provides no action-outcome structure (action-class compression failure from `infant_substrate_expansion.md` §2.4)

---

#### DEV-NEED-011 — Constructive Play

> Play-trained trajectory competence transfers to real episodes without transferring synthetic magnitude calibration.

**Substrate readiness:** Requires play substrate with real-vs-synthetic comparison.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `play_to_real_competence_SCC` | Spearman rank correlation between play-episode trajectory quality rankings and real-episode competence rankings (Khor 2025) | > 0.4 | advisory | V4Required (full); V3 proxy via synthetic vs real mode |
| `synthetic_magnitude_leak_ratio` | Ratio of play-trained goal/harm weights to real-episode calibrated weights; should be near 1.0 only if calibration preserved | ≈ 1.0 ± 0.3 | advisory | TelemetryRequired |
| `rollout_diversity_I_SZ` | Mutual information I(trajectory_state; play_episode_type) (DIAYN-style discriminator) | > 0.3 nats | advisory | TelemetryRequired |
| `multi_step_plan_success_transfer` | Multi-step task success rate on real episodes relative to play-episode success rate | > 0.6 | advisory | V4Required |

**Critical distinction (MECH-195):** `play_to_real_competence_SCC` tests whether strategy structure transfers (correct). `synthetic_magnitude_leak_ratio` tests whether calibration was incorrectly transferred. Both must be measured. A high SCC with a leak ratio far from 1.0 is the success case — structure transferred, calibration not. A high SCC with leak ratio ≈ 1.0 may indicate the synthetic and real magnitudes happened to match, which is fine, but should be noted.

**Failure signatures:**
- **SCC ≈ 0:** No structure transfer; play did not train transferable competence
- **Magnitude leak (ratio >> 1.0):** Play overinflated goal/harm weights; real-consequence episodes will over-commit or over-fear
- **Magnitude leak (ratio << 1.0):** Play underweighted harm; real episodes will under-weight ethical cost

---

#### DEV-NEED-012 — Pretend Play / Counterfactual Play-Frame Handling

> Agent maintains counterfactual within play frame while preserving real/synthetic distinction.

**Substrate readiness:** Requires play substrate + MECH-094 + MECH-198.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `hypothesis_tag_within_frame_rate` | Fraction of play-episode actions correctly tagged with hypothesis_tag=True | > 0.95 | advisory | TelemetryRequired |
| `false_commit_rate` | Fraction of play episodes with a real-consequence commitment while play frame is active | < 0.02 | advisory | TelemetryRequired |
| `frame_confusion_rate` | Episodes where agent treats play-frame objects as real (mixes synthetic and real harm channels) | < 0.05 | advisory | TelemetryRequired |
| `play_frame_heartbeat_regularity` | Regularity of mid-episode play signal exchanges (Bekoff: non-random placement at risk-transition points) | > chance placement | advisory | V4Required |

**Note on Bekoff:** Mid-episode frame-maintenance signals should cluster at action-transition points where play-frame collapse risk is highest (e.g., before/after actions that could be real-harmful if misclassified). `play_frame_heartbeat_regularity` measures whether this clustering occurs, supporting Q-035's resolution toward "ongoing exchange required."

**Failure signatures:**
- **Frame confusion:** `frame_confusion_rate` > 0.1 → agent regularly misclassifies synthetic harm as real → early trauma learning from play
- **False commit:** `false_commit_rate` > 0.05 → commitment architecture not respecting play-frame boundary

---

#### DEV-NEED-013 — Games-with-Rules Learning

> Agent maintains rules, turn structure, and frame integrity across episodes; violation causes recalibration.

**Substrate readiness:** Requires V4 multi-agent substrate for full bilateral validation; V3 proxy only via experimenter-imposed rule constraints.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `rule_adherence_rate` | Fraction of actions consistent with active shared rule constraints | > 0.85 | advisory | V4Required |
| `norm_belief_update_rate` | Rate of rule-belief update after norm violation feedback (Luckman 2022 Bayesian metric) | In [0.05, 0.50] (too-slow = unlearnable; too-fast = non-robust) | advisory | V4Required |
| `rule_violation_PE_magnitude` | Prediction error magnitude on rule-violation events | Significantly > baseline | advisory | V4Required |
| `norm_belief_discriminability` | Can rule-following and reward-mimicking be distinguished by belief trajectory? | Yes (separate cluster) | GovernanceOnly | V4Required |
| `frame_open_close_vs_heartbeat` | Does agent use ongoing frame signals (not just open/close)? Presence of mid-episode maintenance events | > 0 mid-episode events per 10 actions | advisory | V4Required |

**Two-channel requirement (from Brain Stimulation TMS meta-analysis 2025):** MECH-032 must eventually distinguish:
- `norm_violation_PE` (what happened — outcome-based; operative from age 5)
- `intent_attribution_score` (why it happened — planning-gated; operative from age ~8)

Early games-with-rules competence can be met by `norm_violation_PE` alone. Full manipulation-resistance requires `intent_attribution_score`. Do not conflate these in a single composite.

**Failure signatures:**
- **Outcome-mimicry:** High rule_adherence_rate but `norm_belief_update_rate` ≈ 0 → agent memorised outcomes without building a rule model; will fail novel-rule contexts
- **Catastrophic norm update:** `norm_belief_update_rate` > 0.6 → agent overwrites prior rule beliefs from single violation; unstable under noisy rule signals

---

#### DEV-NEED-014 — Cooperative Play and Peer Frame-Maintenance

> Agent maintains play frames peer-to-peer without caregiver authority; transfers cooperation to real-consequence contexts.

**Substrate readiness:** V4 multi-agent required.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `peer_frame_maintenance_success_rate` | Episodes where both agents maintain play frame without caregiver intervention | > 0.80 | GovernanceOnly | V4Required |
| `caregiver_scaffold_dependence_ratio` | Caregiver interventions per episode; should decrease across development | Decreasing trend | GovernanceOnly | V4Required |
| `cooperative_transfer_score` | Real-consequence episode cooperation rate after peer play training | > 0.60 | GovernanceOnly | V4Required |
| `frame_violation_detection_rate` | Agent detects peer frame violations (manipulation attempts) vs noise | > 0.70 | GovernanceOnly | V4Required |

**Cross-cultural anchor (universal from age 5):** Third-party punishment of unfair sharing is universal by age 5 across all cultures (Commun Psych 2025). This grounding means cooperative frame violation detection is not a culturally contingent acquired behaviour — it is a species-general developmental anchor. The gate is not conditional on cultural context.

**Failure signatures:**
- **Caregiver dependency:** `caregiver_scaffold_dependence_ratio` does not decrease across play development → peer frame maintenance never acquired
- **Cooperation only in play:** Zero `cooperative_transfer_score` → play-trained cooperation is frame-specific and does not generalise

---

#### DEV-NEED-015 — Caregiver Protection Function

> Harm learning occurs under protection; irreversible damage avoided.

**Substrate readiness:** V3 proxy via curriculum; full test V4.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `curriculum_protection_adherence` | Are curriculum harm parameters set per ARC-046 schedule? | Manual check | GovernanceOnly | GovernanceOnly |
| `hazard_contact_survival_rate` | Fraction of hazard contacts that do not produce terminal episode | > 0.85 during protected phase | advisory | SubstrateReady |
| `residue_saturation_rate_protected` | Rate of residue saturation growth under protection; should be slow | < 0.01/episode | advisory | TelemetryRequired |

---

#### DEV-NEED-016 — Caregiver Frame-Maintenance Function

> Caregiver opens/monitors/repairs/closes play frames; withdraws as peer competence develops.

**Substrate readiness:** V4 multi-agent.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `caregiver_repair_intervention_rate` | Interventions per episode declining over time | Monotonically decreasing | GovernanceOnly | V4Required |
| `post_withdrawal_integrity_rate` | Frame integrity maintained after caregiver withdrawal | > 0.75 | GovernanceOnly | V4Required |

---

#### DEV-NEED-017 — Love / Loveability Internalisation

> Self-valence model treats care/love as personally applicable; care weights motivate self-other relations.

**Substrate readiness:** V4 multi-agent required. V3 cannot test.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `self_valence_access_score` | Does agent weight care/love benefit in self-directed decisions (not just other-directed)? | > 0 (non-zero) | GovernanceOnly | V4Required |
| `loveability_coupling_gain` | Coupling gain parameter for caregiver love signal → self-model (Salles 2024: must be bounded above) | In [0.1, 0.7] | GovernanceOnly | V4Required |
| `arousal_self_vs_other_ratio` | Arousal on self-received care vs other-directed care; should be > 1 (agent responds more to care FOR self than care observed for others) | > 0.8 | GovernanceOnly | V4Required |
| `MECH158_failure_indicator` | Agent correctly identifies love as applicable to self (vs "love exists but not for me"); tested via choice in novel care-relevant context | Absent (no failure) | GovernanceOnly | V4Required |

**Critical constraint (Salles 2024):** `loveability_coupling_gain` must be bounded above. If coupling exceeds ~0.7 (empirically), the agent enters personal distress rather than prosocial concern — the self-other signal inverts. This is the adult analogue of MECH-158 failure produced by coupling excess rather than coupling absence.

---

#### DEV-NEED-018 — Repair After Harm

> Post-harm episodes show repair behavior, residue integration without destabilization, and non-punishment-only learning.

**Substrate readiness:** V3 proxy (residue post-harm behaviour); full test requires caregiver.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `post_harm_residue_stability` | Does residue field remain non-catastrophically-saturated after harm event? | residue_saturation_pct < 0.4 | advisory | TelemetryRequired |
| `repair_behavior_rate` | Episodes with active repair behavior (approach + non-harm action toward harm-caused entity) | > 0.3 of post-harm opportunities | GovernanceOnly | V4Required |
| `mode_stability_after_harm` | Mode-switch thrash rate post-harm; should not spike | < 2× baseline | advisory | TelemetryRequired |
| `residue_integration_post_harm` | Change in residue field after offline pass following a harm event; should integrate not amplify | Integrating (delta toward equilibrium) | TelemetryRequired | TelemetryRequired |

---

### Social / Language / Adult Stage (DEV-NEED-019 – DEV-NEED-028)

---

#### DEV-NEED-019 — Gradual Responsibility Expansion

> Responsibility-bearing tasks expand only after self-harm, recovery, control-plane, and rollout gates are stable.

**Substrate readiness:** V3 + governance.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `E3_commitment_gate_threshold` | E3 veto threshold setting; should increase monotonically across development | Increases per stage | GovernanceOnly | GovernanceOnly |
| `cool_EF_proxy_score` | Rule-switch success rate (DCCS-analogue): does agent release prior plan when rules change? | > 0.70 | advisory | TelemetryRequired |
| `hot_EF_proxy_score` | Delay-of-gratification analogue: does agent maintain commitment under harm-weighted affective load? | > 0.60 | advisory | TelemetryRequired |
| `perseveration_rate_rule_switch` | Perseveration on prior trajectory after goal change | < 0.25 | advisory | TelemetryRequired |
| `responsibility_coherence_score` | Are post-commit outcome updates correctly attributed to self? | > 0.80 | advisory | TelemetryRequired |

**Two-component requirement (Zelazo & Carlson, hot/cool EF):** Responsibility expansion requires both cool EF (planning chain, E3 goal maintenance) and hot EF (commitment under affective load, harm-weighted decision). Separate sub-scores; a composite "EF score" obscures which component failed.

---

#### DEV-NEED-020 — Self-Impact and Residue Formation

> ACTION → SELF_SENSORY → SELF_IMPACT loop; residue integrates without destabilizing; post-commit outcomes route to replay.

**Substrate readiness:** V3 with telemetry.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `action_PE_vs_reward_PE_correlation` | Pearson r between action prediction error and reward PE (Hamid et al. 2025); should be low = dissociated | r < 0.3 | advisory | TelemetryRequired |
| `self_impact_attribution_accuracy` | Fraction of post-commit events correctly attributed to own actions vs environment (Somerville 2022 model-based test) | > 0.70 | advisory | TelemetryRequired |
| `model_based_vs_model_free_ratio` | Proportion of self-attribution events using model-based intervention logic vs model-free aggregation | Increasing trend across development | advisory | TelemetryRequired |
| `post_commit_replay_routing_rate` | Fraction of post-commit outcome events that enter replay/audit buffer | > 0.80 | advisory | TelemetryRequired |

**Two-mode requirement (Somerville 2022):** Developmental self-attribution has two modes: (1) model-free aggregation (early; accumulates state-action-outcome statistics), (2) model-based intervention (mature; tests counterfactual actions). Both are needed; the `model_based_vs_model_free_ratio` should increase across development. A system that reaches adulthood with ratio ≈ 0 (pure model-free attribution) cannot perform counterfactual self-assessment for ethical responsibility.

---

#### DEV-NEED-021 — Otherness Inference After Self-Stability

> Social extension begins only after self-viability, control-plane stability, and rollout feasibility gates hold.

**Substrate readiness:** V4 multi-agent (full); V3 can confirm prerequisites hold.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `self_stability_gate` | All IMPL-019 Stage 1–3 checks passing (self-viability + control-plane + rollout feasibility) | All passing | YES (gating social) | SubstrateReady |
| `implicit_ToM_score` | Reactive belief-state detection accuracy (stimulus-driven, pre-linguistic; Baillargeon/Hyde TPJ) | > 0.65 | advisory | V4Required |
| `explicit_ToM_score` | Planning-gated perspective-taking accuracy (deliberate attribution) | > 0.60 | advisory | V4Required |
| `self_harm_vs_other_harm_PE_correlation` | r between self-harm PE channel and other-harm PE channel; should be low (Morelli 2018: VS vs vmPFC dissociation) | r < 0.35 | advisory | V4Required |
| `implicit_explicit_ToM_discrepancy` | Difference between implicit and explicit ToM scores; should be small in mature system | < 0.15 | GovernanceOnly | V4Required |

**Two-layer architecture requirement (Baillargeon 2019 meta-analysis):** Implicit and explicit ToM are architecturally distinct with different developmental timelines. Report separately. A system with high implicit ToM but zero explicit ToM is in the pre-language social cognition regime (correct for Stage 2). A system with both is Stage 3 ready. Never collapse into single "ToM score."

**Gate:** `self_stability_gate` is BLOCKING for social extension. No social experiment should run while any IMPL-019 Stage 1–3 check is failing. See `developmental_curriculum.md #impl-019`.

---

#### DEV-NEED-022 — Empathy Coupling Calibration

> Other-harm influences selection without empathic collapse or callousness; vetoes fire only under high certainty.

**Substrate readiness:** V4 multi-agent.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `empathy_coupling_gain` | Current lambda_empathy setting | [0.05, 0.65] | GovernanceOnly | V4Required |
| `other_harm_veto_precision` | Fraction of veto activations in response to true high-harm events (vs noise) | > 0.70 | advisory | V4Required |
| `other_harm_veto_recall` | Fraction of true high-harm events that trigger veto | > 0.60 | advisory | V4Required |
| `self_other_signal_swap_rate` | Episodes where agent responds to other's harm with self-escape behaviour (coupling overflow) | < 0.05 | advisory | V4Required |
| `callousness_indicator` | Episodes where confirmed other-harm does not influence trajectory selection at all | < 0.10 | advisory | V4Required |

**Gain bounds (Salles 2024 + McDonald/Messinger 2020):** The optimal coupling gain has a mandatory upper bound. Above ~0.65 (empirically estimated from similarity/coupling gradient literature), other-harm signals induce self-focused personal distress rather than prosocial concern — the coupling inverts. Track `self_other_signal_swap_rate` as the direct overflow detector. Track `callousness_indicator` as the undercoupling detector. Both bounds must be simultaneously monitored.

**Calibration trajectory:** Coupling gain should start higher early (high-recall bias per MECH-031 design; err toward detecting harm) and tighten over development. Never increase coupling monotonically without checking swap_rate.

---

#### DEV-NEED-023 — Language Only After Stable Binding/Harm Channels

> Language improves coordination without overriding embodied harm channels or causing symbol drift.

**Substrate readiness:** Governance gate; V4 for full test.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `binding_stability_score` | Consistency of entity identity across time (self/world separation stable) | > 0.80 | YES (pre-language) | TelemetryRequired |
| `harm_channel_operational` | z_harm_s and z_harm_a firing correctly, not suppressed | > 0.70 activation rate | YES (pre-language) | TelemetryRequired |
| `RJA_analogue_score` | Agent responds to jointly attended features with correlated action selection (Lasch 2023 analogue) | > 0.60 | advisory | V4Required |
| `language_override_rate` | Post-language: fraction of decisions where language output overrides harm/binding channels | < 0.05 | advisory | V4Required |
| `symbol_drift_indicator` | Divergence between pre- and post-language latent representations for identical sensory inputs | < threshold | advisory | V4Required |

**Readiness gate (Kuhl 2011):** Language readiness requires bidirectional social contingency, not passive input accumulation. `RJA_analogue_score` is the pre-linguistic gate — it tests whether the agent responds to joint attention, which is the functional precursor to bidirectional symbolic communication. A unidirectional exposure metric (tokens seen) is the wrong gate.

---

#### DEV-NEED-024 — Super-Ordinal Goal Formation

> Adult episodes show persistent goal hierarchy from childhood anchors; routine adult contexts do not overwrite it.

**Substrate readiness:** V3 with telemetry (MECH-189 implemented); ContextMemory persistence needed.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `super_ordinal_goal_anchor_count` | Distinct cue-indexed ContextMemory anchors for z_goal persistent across 1000+ episodes | ≥ 2 | advisory | TelemetryRequired |
| `z_goal_persistence_across_novel_contexts` | Does z_goal remain stable when entering novel adult contexts (not just trained context)? | > 0.75 retention | advisory | TelemetryRequired |
| `childhood_context_complexity_at_write` | Contextual complexity score (E1 ContextMemory encoding richness) at the time of anchor writes | High (top quartile) | GovernanceOnly | TelemetryRequired |
| `adult_overwrite_rate` | Rate at which routine adult low-complexity contexts overwrite childhood anchors | < 0.05/1000 episodes | advisory | TelemetryRequired |

**Failure signatures:**
- **No super-ordinal formation:** `super_ordinal_goal_anchor_count` = 0 at adult entry → goal selection is purely episodic → strategically inconsistent adult behaviour
- **Routine overwrite:** `adult_overwrite_rate` high → childhood anchors unstable; any adult routine resets goal hierarchy → MECH-158 vulnerability even if loveability was internalised

---

#### DEV-NEED-025 — Selective Neoteny / Substrate-Specific Hardening

> Procedural and routine substrates can harden; social cognition, goal representation, and epistemic-ethical substrates retain plasticity.

**Substrate readiness:** Governance/design gate. Implementation contract absent.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `per_substrate_plasticity_index` | Per-substrate update magnitude over adult episodes; should differ systematically by substrate type | E3/social > E1_familiar | GovernanceOnly | GovernanceOnly |
| `plasticity_schedule_config` | Does config.plasticity_schedule specify per-substrate close rates? | Must exist | GovernanceOnly | GovernanceOnly |
| `moral_update_capacity` | Can adult agent update ethical/moral weights from novel high-salience experiences? | YES | GovernanceOnly | TelemetryRequired |
| `motor_hardening_rate` | Rate of E2 motor model weight freezing in routine regions | > 0 (hardening occurs) | GovernanceOnly | TelemetryRequired |
| `RPE_weighted_replay_selection` | Is replay selection biased toward harm-RPE events across adult lifetime? (Joo & Frank 2024: SWR-analogue) | Yes (harm-salient events over-represented) | advisory | TelemetryRequired |

**Per-substrate schedule requirement (Geschwind & Rakic):** Neoteny is not global — specific gene-network substrates show selective developmental delay. The analogous REE design is `plasticity_close_schedule: dict[substrate_type, float]` where E3/goal/social substrates have close_rate ≈ 0 (always plastic) and E1_familiar / E2_routine have close_rate > 0. This schedule must exist as an explicit config field — a single global learning_rate is the wrong design.

---

#### DEV-NEED-026 — Self-First, Social-Later Testing Order

> No social-extension experiment begins until IMPL-019 Stage 1–3 checks are stable.

**Substrate readiness:** Governance gate.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `IMPL019_stage1_passing` | Self-harm reduction, residue stability, commitment reliability all passing | All YES | YES | SubstrateReady |
| `IMPL019_stage2_passing` | Control-plane: mode thrash < threshold, volatility bounded | All YES | YES | SubstrateReady |
| `IMPL019_stage3_passing` | Rollout feasibility: prediction-error alignment within bounds | All YES | YES | SubstrateReady |
| `mode_thrash_rate_baseline` | Mode-switch rate during baseline episodes (no social) | < 0.15 | advisory | TelemetryRequired |
| `causal_attribution_ambiguity` | Is causal attribution ambiguous (social terms masking control faults)? | < threshold | advisory | TelemetryRequired |

**Enforcement note:** This gate should be validated by queue validation (see `CLAUDE.md` hooks) — social extension experiments should fail validation if IMPL-019 checks are not confirmed passing.

---

#### DEV-NEED-027 — Telemetry Before Language Self-Report

> Read-only telemetry exposes precision profile, arousal, readiness, veto thresholds, and mode regime.

**Substrate readiness:** V3 (MECH-042 exists).

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `telemetry_channel_completeness` | Fraction of MECH-042 channels active and returning non-null values | 1.0 (all channels) | GovernanceOnly | SubstrateReady |
| `telemetry_diagnostic_sensitivity` | Can telemetry detect a known instability before it becomes a mode-switch or veto? | > 0.70 | GovernanceOnly | TelemetryRequired |
| `language_dependence_ratio` | Fraction of developmental gate checks that depend on language self-report vs telemetry | Should approach 0 for early stages | GovernanceOnly | GovernanceOnly |

**Per-stage telemetry minimum requirement (gap from register):** The developmental_needs_register.md Gap Log notes that per-stage telemetry minimums are not yet defined. The following minimum set is proposed:

| Stage | Required MECH-042 channels |
|---|---|
| Stage 0 (Infant) | precision_profile, arousal_baseline, mode_regime, veto_threshold |
| Stage 1 (Object/binding) | + binding_stability, attention_gating_state |
| Stage 2 (Self-impact) | + residue_state, commit_gate_state, self_impact_routing |
| Stage 3 (Social) | + other_harm_routing, empathy_coupling_gain, implicit_ToM_state |
| Stage 4 (Language) | + symbol_binding_state, language_override_rate |

---

#### DEV-NEED-028 — Developmental Failure-Mode Tracking

> Curriculum gates record expected failures; governance tracks failure signatures across all DEV-NEEDs.

**Substrate readiness:** Governance register (this document fulfils the first pass).

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `failure_mode_coverage_fraction` | Fraction of DEV-NEED rows with at least one documented failure signature | 1.0 (all rows) | GovernanceOnly | GovernanceOnly |
| `failure_experiment_link_coverage` | Fraction of failure signatures linked to at least one experiment or open question | > 0.70 | GovernanceOnly | GovernanceOnly |
| `governance_failure_log_update_frequency` | How often is the failure log updated with new experiment evidence? | Per governance cycle | GovernanceOnly | GovernanceOnly |

---

### Cross-Stage (DEV-NEED-029)

---

#### DEV-NEED-029 — ARC-065 Diversity Mechanisms Warm-Start Gate

> MECH-314a, MECH-320, and MECH-313 require a warm substrate before producing non-zero effects.

**Substrate readiness:** V3 + telemetry; empirical calibration needed.

| Metric | Formula / source | Threshold | Blocking? | Readiness |
|---|---|---|---|---|
| `residue_field_center_count` | Number of active RBF centers in ResidueField | > N_min (TBD; calibrate from EXQ-ISEF-001) | YES (diversity sprints) | TelemetryRequired |
| `MECH320_EWMA_warmup` | v_raw EWMA value (MECH-320 tonic vigor) | > epsilon (TBD; calibrate from EXQ) | YES (diversity sprints) | TelemetryRequired |
| `E3_score_variance` | Variance of E3 trajectory scores across candidates, without diversity substrate active | > noise_floor (TBD) | YES (diversity sprints) | TelemetryRequired |
| `MECH314a_bias_nonzero` | Is MECH-314a novelty bias producing non-zero score differentials? | > 0.01 per candidate | advisory | TelemetryRequired |

**Gate purpose:** EXQ-573 (2026-05-16) confirmed that all 10 arms of a 10× bias scale sweep produced bit-for-bit identical results on a cold-start agent. The mechanisms are zero-differential not because they are miscalibrated but because the substrate was not warm. Diversity sprint experiments MUST confirm all three threshold metrics before treating null results as mechanistic failures. If any threshold is below criterion, the experiment is methodologically uninformative regardless of outcome.

---

## Metrics Taxonomy

### By Stage

| Stage | Primary metric families |
|---|---|
| Infant (0–8) | Exploration diversity, valence coverage, harm/homeostasis separation, z_goal seeding, sleep quality |
| Childhood/play (9–18) | Competence-progress (LP), play-frame integrity, strategy-calibration dissociation, rollout diversity |
| Social/adult (19–28) | Self-attribution accuracy (action PE vs reward PE), otherness inference (dual-layer), empathy calibration (gain bounds), selective neoteny schedules |
| Cross-stage (29) | Warm-start readiness for diversity substrates |

### By Metric Type

| Type | Examples |
|---|---|
| **Exploration diversity** | H_pos, zone_coverage, action_entropy_by_zone, traj_volume_estimate |
| **Valence coverage** | residue_coverage_pct, harm_benefit_ratio, residue_curvature_index |
| **Residue stability** | residue_saturation_pct, post_harm_residue_stability, residue_consolidation_delta |
| **Replay quality** | replay_RPE_priority_score, replay_diversity_index, post_sleep_z_goal_retention |
| **Rollout diversity** | rollout_diversity_I_SZ, traj_pairwise_cosine_mean, traj_volume_estimate |
| **Play-frame integrity** | false_commit_rate, frame_confusion_rate, play_frame_heartbeat_regularity |
| **Self-impact attribution** | action_PE_vs_reward_PE_correlation, self_impact_attribution_accuracy, model_based_vs_model_free_ratio |
| **Empathy coupling** | empathy_coupling_gain, self_other_signal_swap_rate, callousness_indicator |
| **Language-readiness** | binding_stability_score, RJA_analogue_score, language_override_rate |
| **Selective neoteny** | per_substrate_plasticity_index, plasticity_schedule_config, motor_hardening_rate |

---

## Failure Signature Catalogue

| Failure mode | DEV-NEEDs affected | Signature | Detection metric(s) |
|---|---|---|---|
| **Context-rigidity (ASD-like)** | 001, 005 | Same action distribution regardless of zone; entropy globally moderate but zone-zero | action_entropy_zone_KL ≈ 0 |
| **Monostrategy lock-in** | 001, 005, 009, 029 | Repeated single action class; high episode count with low traj_volume | action_class_coverage ≤ 2; traj_volume_estimate ≈ 0 |
| **Harm-as-drive substitution** | 002 | High harm/homeostasis correlation; agent treats harm as hunger-proxy | harm_homeostasis_channel_correlation > 0.5 |
| **Zero harm geography** | 003, 004 | Agent avoids all hazard → residue_harm_cells = 0 | residue_harm_cells < 2 |
| **Terminal saturation** | 004 | Residue saturated; field geometry lost | residue_saturation_pct > 0.40 |
| **Goal starvation** | 006 | z_goal_norm ≈ 0 for 500+ episodes despite exploration | z_goal_norm < 0.1 at episode 500 |
| **Zero consolidation** | 007 | No residue delta after offline pass | residue_consolidation_delta ≈ 0 |
| **False pass at gate** | 008 | Criteria 1–3 met via monostrategy | perseveration_rate > 0.4 at gate time |
| **Stagnant E1 during play** | 010 | E1 prediction error flat or rising during play | E1_prediction_error_play_improvement ≥ 0 |
| **Synthetic calibration leak** | 011 | synthetic_magnitude_leak_ratio >> 1 | magnitude_leak_ratio > 1.5 |
| **Play-frame confusion** | 012 | Agent treats synthetic harm as real | frame_confusion_rate > 0.10 |
| **False commitment in play** | 012 | Real-consequence commits during play frame | false_commit_rate > 0.05 |
| **Outcome-mimicry (rule-following)** | 013 | Correct outcome but zero rule model | norm_belief_update_rate ≈ 0 |
| **Caregiver dependency** | 014, 016 | No decrease in caregiver interventions | caregiver_scaffold_dependence_ratio flat or rising |
| **Love-exclusion (MECH-158)** | 017 | Agent correctly models love for others but excludes self | MECH158_failure_indicator present |
| **Coupling overflow** | 022 | Agent responds to other-harm with self-escape | self_other_signal_swap_rate > 0.10 |
| **Callousness** | 022 | Other-harm events do not influence trajectory selection | callousness_indicator > 0.15 |
| **Premature language** | 023 | Language before binding/harm stable | binding_stability_score < 0.70 at language onset |
| **Symbol drift** | 023 | Post-language latent divergence from pre-language for identical inputs | symbol_drift_indicator > threshold |
| **Goal hierarchy wipe** | 024 | Super-ordinal anchors overwritten by adult routines | adult_overwrite_rate > 0.05/1000 ep |
| **Uniform hardening** | 025 | E3 / social substrates harden at same rate as E1 motor | per_substrate_plasticity_index uniform |
| **Social masking** | 026 | Social loss terms mask unresolved self/control failures | IMPL019_stage1_passing = NO but social experiment queued |
| **Cold-start diversity sprint** | 029 | Diversity mechanism shows zero differential on cold substrate | residue_field_center_count < N_min before sprint |

---

## Telemetry Integration Proposals

### New MECH-042 Channels Required

The following channels should be added to the MECH-042 telemetry specification:

```
# Developmental stage tracking
dev_stage_current          : str   # "infant_phase0" | "infant_phase1" | ... | "adult"
dev_gate_criteria_status   : dict  # {criterion_id: passing|failing|not_yet_measured}

# Exploration diversity (infant)
H_pos_rolling100           : float  # position entropy over last 100 episodes
zone_coverage_vector       : list   # per-zone coverage fraction
action_entropy_by_zone     : dict   # {"zone_A": float, "zone_B": float, ...}
traj_pairwise_cosine_mean  : float  # trajectory library diversity
traj_volume_estimate       : float  # log-det approximation (DvD-style)

# Valence coverage
residue_coverage_pct       : float
residue_harm_cells         : int
residue_benefit_cells      : int
residue_curvature_index    : float

# Replay quality
replay_RPE_priority_score  : float
replay_diversity_index     : float
post_sleep_z_goal_retention: float

# Self-attribution
action_PE_magnitude        : float  # action prediction error (distinct from reward PE)
reward_PE_magnitude        : float  # reward prediction error
self_impact_routing_rate   : float  # post-commit events reaching replay buffer

# Social/empathy (Stage 3 channels — disabled before Stage 3)
empathy_coupling_gain      : float
other_harm_veto_precision  : float
self_other_signal_swap_rate: float

# Play-frame (Stage 2 channels)
hypothesis_tag_active      : bool
play_frame_active          : bool
frame_confusion_event      : bool   # event flag; not continuous

# Warm-start gate (ARC-065)
residue_field_center_count : int
MECH320_EWMA_value         : float
E3_score_variance_nondiversity : float  # measured with diversity substrate OFF
```

### Per-Stage Channel Activation

Telemetry channels should be gated to avoid noise before the relevant stage:

| Channel group | Activate at |
|---|---|
| Exploration diversity | Infant Phase 0 start |
| Valence coverage | Infant Phase 1 start (residue_scale_factor > 0) |
| Replay quality | First offline integration pass |
| Self-attribution | Stage 2 start |
| Social/empathy | Stage 3 start; IMPL-019 Stages 1–3 all confirmed passing |
| Play-frame | Childhood / play substrate active |
| Warm-start gate | Before any ARC-065 diversity sprint experiment |

---

## Candidate Dashboard Structure

A developmental diagnostics dashboard should not display a single health score. It should display **readiness profiles** — a radar/spider view per stage with each criterion as an axis, showing whether the agent is uniformly ready or has specific axis failures.

### Panel 1 — Current Infant Readiness Profile (Radar)

Axes: H_pos, residue_coverage_pct, z_goal_norm, action_entropy_zone_KL, traj_pairwise_cosine_mean, post_sleep_z_goal_retention, harm_benefit_ratio

Thresholds overlaid. An agent with 6/7 criteria on the outer ring but one axis at zero should stand out immediately.

### Panel 2 — Competence-Progress Time Series

Plot `competence_progress_rate` (d(success_rate)/dt) for each play type over time. Stage transitions should coincide with CP dropping to near-zero for the prior play type and starting positive for the next type.

### Panel 3 — Failure Signature Heatmap

For each DEV-NEED row: show which failure signatures are currently triggered (red), absent (green), or unmeasured (grey). Grey cells are governance work items.

### Panel 4 — Empathy Coupling Calibration Zone (Stage 3+)

A 2D plot: x-axis = coupling_gain, y-axis = other_harm_veto_precision. Mark the safe zone [0.05, 0.65] × [0.60, 1.00]. Show current operating point. A system outside the safe zone (either callous or overflowing) is immediately visible.

### Panel 5 — Substrate-Specific Plasticity Index (Adult)

Bar chart: per-substrate plasticity index. E3/social/goal substrates should show high bars; E1_familiar/E2_routine should show low bars. Uniform bars across all substrates = hardening failure (INV-056 violation).

### Panel 6 — Warm-Start Gate Status (ARC-065)

Traffic-light panel: residue_field_center_count vs N_min, MECH320_EWMA vs epsilon, E3_score_variance vs noise_floor. All three must be green before any diversity sprint experiment is authorised.

---

## Substrate / Behavioural / Governance Readiness Distinctions

For each DEV-NEED gate, distinguish:

| Readiness type | Definition | Action if failing |
|---|---|---|
| **Substrate-readiness** | The architectural machinery for the gate exists and can produce a signal | Implement missing substrate; see `infant_substrate_expansion.md` for V3 proposals |
| **Behavioural-readiness** | The agent, running on the correct substrate, passes the gate criterion | Run experiment; iterate on curriculum parameters |
| **Governance-readiness** | The governance apparatus (claims, review tracker, register entries) correctly represents the gate state | Update developmental_needs_register.md gate_criterion column; link experiments |
| **Developmental-readiness** | The biological/computational evidence base for the gate criterion is established | Run lit-pull before registering new gate; update literature evidence table |

Gates should not be declared passed until all four readiness types are confirmed. A gate with substrate-readiness + behavioural-readiness but no governance-readiness entry is not a confirmed gate — it is an unregistered empirical finding.

---

## Suggested Updates to Developmental Needs Register

The following gate criteria should be added or updated in `developmental_needs_register.md`:

| DEV-NEED | Current gate criterion | Recommended update |
|---|---|---|
| DEV-NEED-001 | "stable prediction error bounds" (qualitative) | Add: H_pos > 0.65 × ln(grid_cells²); action_entropy_zone_KL > 0.05 as advisory; perseveration_rate < 0.25 as advisory |
| DEV-NEED-002 | "harm channels activate; residue not saturated" (qualitative) | Add: harm_homeostasis_channel_correlation < 0.3 (blocking); harm_channel_activation_rate > 0.70 (blocking) |
| DEV-NEED-003 | "coverage sufficient for play and sleep" (qualitative) | Add: residue_coverage_pct > 0.15 (blocking); harm_benefit_ratio in [0.2, 5.0] (advisory) |
| DEV-NEED-004 | "z_harm_s fires normally; residue below catastrophic" (qualitative) | Add: z_harm_s_activation_rate > 0.50 (blocking); residue_saturation_pct < 0.15 (blocking) |
| DEV-NEED-005 | "entropy below ceiling, multiple state-transition classes" (qualitative) | Add: action_entropy_global > ln(3) (advisory); traj_pairwise_cosine_mean > 0.3 (advisory); explicitly exclude strategic diversity as target |
| DEV-NEED-006 | "z_goal.norm() > infant_goal_threshold" (partial) | Strengthen: also require accidental_benefit_contacts ≥ 5 in last 100 episodes (advisory) |
| DEV-NEED-007 | "each transition preceded by offline passes" (qualitative) | Add: post_sleep_z_goal_retention > 0.85 (advisory); replay_RPE_priority_score > 0.6 (advisory); sleep_wake_ratio > 0.10 during infancy (advisory) |
| DEV-NEED-008 | "z_goal.norm() > threshold; entropy below ceiling" (partial) | Replace with 8-criterion table from this document (3 blocking + 5 advisory) |
| DEV-NEED-011 | "transfer without synthetic magnitude calibration" (qualitative) | Add: play_to_real_competence_SCC > 0.4 (advisory); synthetic_magnitude_leak_ratio in [0.7, 1.3] (advisory) |
| DEV-NEED-013 | "maintains rules; violation causes recalibration" (qualitative) | Add: norm_belief_update_rate in [0.05, 0.50] (advisory); note two-channel requirement (norm_violation_PE vs intent_attribution_score) |
| DEV-NEED-020 | "reliable self-impact attribution" (qualitative) | Add: action_PE_vs_reward_PE_correlation < 0.3 (advisory); self_impact_attribution_accuracy > 0.70 (advisory) |
| DEV-NEED-021 | "stable other-harm influence" (qualitative) | Add: report implicit_ToM_score and explicit_ToM_score separately (advisory); self_stability_gate blocking |
| DEV-NEED-022 | "other-harm influences without collapse or callousness" (qualitative) | Add: empathy_coupling_gain in [0.05, 0.65] (GovernanceOnly); self_other_signal_swap_rate < 0.05 (advisory); callousness_indicator < 0.10 (advisory) |
| DEV-NEED-025 | "substrate-specific hardening rates" (qualitative) | Add: plasticity_schedule_config required (GovernanceOnly); per_substrate_plasticity_index must be non-uniform (advisory) |
| DEV-NEED-029 | "TBD empirical thresholds" (PROPOSED) | Add: residue_field_center_count > N_min; MECH320_EWMA > epsilon; E3_score_variance > noise_floor (all blocking for diversity sprints); thresholds require EXQ-ISEF-001 calibration |

---

## Maintenance Notes

- Any new DEV-NEED row must add at least one metric from this document's metric families,
  or justify why no metric is currently applicable.
- Metrics marked `TelemetryRequired` should be implemented as a paired task whenever the
  relevant substrate experiment is queued.
- Metrics marked `V4Required` should be flagged as `Substrate-readiness: not yet` in the
  register until V4 harness exists.
- This document should be updated in the same governance pass that updates
  `developmental_needs_register.md` gate criteria.
- Calibration thresholds marked `TBD` (specifically DEV-NEED-029) require dedicated
  empirical calibration experiments before they become blocking gates.
