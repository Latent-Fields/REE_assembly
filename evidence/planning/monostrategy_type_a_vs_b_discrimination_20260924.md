# Monostrategy: repertoire absence (Type A) vs repertoire-access collapse (Type B) -- what landed evidence settles, and the assay that would decide the rest

- **Produced:** 2026-09-24 by `bt0924-repertoire-ab` (Worker C of `orchestrate-20260924-breakthrough`), chip `chip-20260924-repertoire-typeab-discrimination`.
- **Status:** DESIGN AND EVIDENCE AUDIT ONLY. Nothing was queued, no script was added to `ree-v3/experiments/`, and no registry was edited.
- **Specification:** `docs/thoughts/2026-09-24_dynamic_coordination_repertoire_monostrategy.md`. **Method:** `docs/thoughts/2026-09-24_experimental_learning_beyond_literature.md` (Frontier Mechanism Discovery Loop). **Intake:** `evidence/planning/thought_intake_2026-09-24_dynamic_coordination_repertoire_monostrategy.md`.
- **Code citations** are file:line against `ree-v3` `origin/main` @ `00210b5` (a throwaway detached worktree).
- **Evidence domains:** D0 code-read, D1 exists/decodable, D2 intervention moves a native consumer, D3 closed-loop behaviour.

## 0. Bottom line

1. **Verdict on current evidence: UNDETERMINED as a Type-B test, and leaning Type A wherever the monostrategy is sharpest.** The spec's Type-B verdict needs P1 to P6 together. **P5 has never been measured.** No landed run shows a fixed strategy doing measurably worse than switching, and no ree-v3 environment has a reversal or rule-switch schedule. So **P1 and P5 have never held jointly**. That is the FIRST unmet prerequisite, and the spec itself calls any coordination test uninterpretable until it holds.
2. **This session's probe decomposes the V3-EXQ-1061 "same action at 39-40/40 states" monostrategy.**
   - It is generation-stage concentration, not a selection-stage collapse.
   - The hippocampal pool is 31:1 or 30:2 in first-action class at **every** probe state.
   - The majority class is **the same class at all 40 states within a seed**, so the proposal is not conditioned on state.
   - The one or two off-class candidates are the support-preserving CEM floor's token (`config.py:2777-2795`, `hippocampal/module.py:1419-1432`).
   - E3 picks the pool-majority class at 97.5-100% of states. A token candidate never beats the best of the ~31 majority candidates (0/40 on 3/3 seeds), even though it beats the majority's MEAN score at 10-35% of states. That is an order-statistic effect of the imbalance, not evidence that E3 rejects a useful alternative.
   - In this regime the committed monostrategy is **Type A at generation**. Alternatives are never *formed* as refined candidates, only sampled as floor-mandated tokens. D1/D2 (section 2.3).
3. **Every Type-B-shaped signal in the record fails the adversarial duty or lacks P1/P5.** That covers 931, 654i/j, 947/949, 804, the 567 seed-43 row and 1014 (section 3). None can be credited as repertoire-access collapse.
4. **Consequence: dynamic coordination has not earned a build.** Phase, wave, ephaptic or authority-field machinery stays deferred at V4 under the spec's own "Result that would keep the V4 deferral intact" clause. The next work is to build the precondition:
   - `complicated (buildable)`: a block-reversal two-route ecology that satisfies P1 and P5 by construction, with a competence gate.
   - `complex (probe-gated)`: the generation link, whose first link is the pool's class-balance and state-conditioning.
   - The assay in section 4 is written to run on top of those, and it fails closed until they hold.
5. **Assay pre-flight grade: RED to run as a whole today; AMBER for its Stage 0 and Stage 1.** The environment gate is RED: no switching ecology exists, and the nearest one (Q-080 effort layout) measured agent corridor entry 0.333 < 0.5 in V3-EXQ-731. The clamp arm needs a default-off hook (AMBER). The injection arm has a native producer (GREEN).

## 1. Premises re-measured (CLAUDE.md "audit its premises")

| Premise (source) | Re-measured | Status |
|---|---|---|
| "Monostrategy traces to z_world under-differentiation" (memory `project_monostrategy_representation_ceiling_root`, 2026-07-13) | Its load-bearing inference is self-labelled a hypothesis. 750 (the diversity readout it proposed) was precondition-unmet. 748 behaviour cloning (z_world 32.72 > raw 20.93) argues against "z_world action-inadequate". 1010/1002/1008 argue for encoder discard, but they are probe-only D1. The conversion-ceiling registry's live roots are still `H-substrate-ceiling` and `H-observation-interface` (`hypothesis_space_registry.v1.json` qid `conversion_ceiling_root`). | **Not re-established.** Representation-side Type A is plausible but is D1-probe-only. It is not the cause of the sharpest monostrategy measured below, which sits upstream of E3 in the proposer. |
| "E3 commits the same action at 39-40/40 states" (MECH-131 addendum 4, 2026-09-19) | Reproduced exactly on the same config: selected-action entropy 0.1169 / 0.0 / 0.0 for seeds 11/23/37 at floor 0.2, matching the recorded values bit for bit. | **Holds, and is now decomposed** (section 2.3). |
| "F-dominance is the live selection root" (memory `project_conversion_ceiling_four_roots`, marked PARKED 2026-07-18) | 924 (2026-08-12) re-measures F's share at 0.960-0.961 with the fixed scorer. 804 (2026-07-23) finds `e3_score_gradient_without_selection_authority` (normalised range 0.00095; lesioning E3 leaves `committed_frac` 0.995). | Holds as a D1 description. It does not bear on P1/P5. |
| "Curiosity cannot generate diversity" (memory `project_curiosity_exploitation_amplifier_reframe`) | Not re-run. It is consistent with the generation-stage finding here, since nothing in the default path conditions the proposal's class mix on state. | Consistent; not re-measured. |
| "Some ree-v3 env satisfies P1 and P5" (the spec's prerequisite) | Searched CGW and all experiments: no reversal flag, no rule switch, no day/night regime, no forced relocation (the resource respawn at `_respawn_resource` is random). | **False.** This is itself a finding. |
| Orchestrator P4 "functional-organism preflight" exists | No 2026-09-2x preflight file under `evidence/planning/`. | Not written. It is independent of this record, but section 4.1 answers its environment question too. |

## 2. Evidence audit, P1 to P6

The table distinguishes D1 (present or decodable) from D2 (causally used). "Probe-only" means the result rests only on an external decoder.

| # | Prerequisite | Measured? | Run / record (path under `REE_assembly/evidence/`) | Value | Regime / substrate | Staleness |
|---|---|---|---|---|---|---|
| P1 | >=2 behaviourally useful alternatives exist in the ecology | **Partly, never together with P5** | 1014 `planning/failure_autopsy_V3-EXQ-1014_2026-09-09.md` | CONSTANT_0..3 survive 200/200 on all 8 pinned 6x6 boards; STAY dies in 10-14 steps | canonical E3, 32 CEM candidates, `ree-cloud-2`, substrate `f6fc776b61a1` | 15 d; this ecology does not require switching (a constant mover is optimal), so P5 fails |
| P1 | | partly | 522 `experiments/v3_exq_522_reef_monostrategy_break_20260505T064610Z_v3.json` | a heuristic on the SD-054 reef reaches reef 0.501 / forage 0.499 occupancy, 48.9 transitions/ep | heuristic policy, not the agent | 4.5 months; occupancy only, no payoff comparison |
| P1 | | by construction only | Q-080 effort layout, CGW `causal_grid_world.py:2039-2103`, `effort_benefit_asymmetry` :896/:2968 | two equal-length routes to one resource; asymmetry > 0 makes the high-effort route the better one | env lever exists | 731 (2026-07-09) **agent_reaches_corridor_early 0.333 < 0.5** and C2 (value term non-vacuous) failed 0/3, so the agent never used either route |
| P2 | alternatives represented / decodable | **mixed; E2 yes, E1 no, z_world contested** | 1082 `planning/failure_autopsy_V3-EXQ-1082_2026-09-24.md` | E2 world-forward action read 0.341/0.216/0.227 (CI>0 3/3); skill vs copy-input +0.35/+0.22/+0.21 | D1 native; alpha_world 0.9 | fresh; confirmed |
| P2 | | | 108b `planning/failure_autopsy_V3-EXQ-108b_2026-08-03.md`; 954 `..._V3-EXQ-954_2026-08-29.md` | E1 rollouts collapse: CR_rollout/CR_real ~3e-6; ~5,000x attenuation of per-action divergence inside E1 at depth 1 | D1 native | 4-7 weeks |
| P2 | | | 1010/1002/1008/1023a (autopsies 09-05..09-17) | trained z_world 0.678 < random-init 0.7045 < PCA-32 0.8776 on oracle-action agreement; transfer shortfall ~50x | **probe-only D1** | 1-3 weeks; 1041 shows the metric under-reads the code |
| P3 | candidate generation non-degenerate | **nominal yes, effective no in the sharpest regime** | 567 / 804 / 689j (foraging regimes) | SP-CEM pool support 2.80 (567); 2.43 classes (804); pool class entropy 1.33 with dominant-class share 0.67 (689j) | foraging GAP-A/B configs | 2-4 months |
| P3 | | | **this record, section 2.3** (probe) | 1061 regime: nominally 2.0-2.025 classes, but **31:1 or 30:2** (class entropy 0.139-0.163); majority class **identical at all 40 states** within each seed | 5x5 grid, world_dim 16, 20 warmup eps (NOT deployed dims) | today |
| P4 | E3 scoring non-flat across alternatives | **absolutely non-flat; relatively flat; F-monopolised** | 924 `planning/failure_autopsy_V3-EXQ-924_2026-08-12.md`; 571b; 804 | F share 0.960; inter-candidate score std ~1.75; 804 normalised range 0.00095, lesioning E3 leaves committed_frac 0.995 | D1 (571b clamp arm reaches D2 on score range only) | 3-8 weeks |
| P4 | | | this record | score spread 1.42-4.01 on abs ~24-40 (4-10%); class gap best-vs-second 1.34-3.84 | probe regime | today |
| P5 | ecology requires switching | **never measured** | none | no reversal / rule-switch / regime flag exists in CGW; 485j-m (OFC devaluation) measure probe-state TV, not reversal latency; 655 measures entropy, not switching payoff | -- | -- |
| P6 | alternative repeatedly fails between representation and authority | **Type-B-shaped signals only; none clears P1/P5 or the adversarial check** | section 3 | -- | -- | -- |

### 2.1 D1 vs D2 flags

- Every Type-A reading about z_world (1010, 1002, 1008, 1023a) is **probe-only D1**, and 748's behaviour-cloning D3 result points the other way. They must not be cited as "alternatives are not represented".
- The E2 read (1082) is **D1 native**: action alternatives do differ in E2's forward predictions. No run has shown a D2 intervention on that content changing E3 selection in a switching ecology.
- The only D2 signals on selection are channel-authority results (1012c eligibility knockouts R_ON 0.41-0.86; 1029 head flips 0.259 vs 0.170; 949 yoked divergence 0.3675). Each shows that a channel can move the argmin. None shows that a **useful** alternative, one that the ecology rewards, was blocked.

### 2.2 The crucial quantity is unmeasured

The spec's crucial quantity is the **fraction of useful represented alternatives that become causally used**. It has never been computed, because "useful" needs P1 and P5 in the same ecology and an evaluator-side oracle. Every existing diversity DV (committed-class entropy, selected-action entropy, TV across probe states) counts *difference*, not *usefulness*. The spec warns that difference alone is not the diagnostic.

### 2.3 Probe run this session: decomposing the 1061 monostrategy (D1 + one D2 contrast)

- **Script:** `evidence/planning/probes/repertoire/probe_p3p4_candidate_vs_selection.py`. It imports V3-EXQ-1061's own `build_agent`/`warmup_train` from the detached worktree @ `00210b5`.
- **Config:** 1061's intact arm; grid 5, 1 hazard, 2 resources; self_dim = world_dim = 16 (**not** the deployed world_dim 32); ao_std floor 0.2 (production); 20 warmup episodes x 100 steps; 40 probe states along a random walk; `torch.set_num_threads(2)`.
- **Seeds and runtime:** 11 / 23 / 37; 135 / 218 / 373 s on the Mac.
- **Per-seed outputs:** `probe_p3p4_seed{11,23,37}.json` in the same directory.

| seed | pool classes (nominal) | pool class entropy | off-class candidates per pool (mean/max) | majority class same at all 40 states? | E3 picks pool-majority | selected entropy (bare / full path) | off-class beats majority MEAN | off-class beats majority BEST |
|---|---|---|---|---|---|---|---|---|
| 11 | 2.025 | 0.163 | 1.25 / 3 | yes (class 2) | 0.975 | 0.1169 / 0.1985 | 0.354 | 0/40 |
| 23 | 2.000 | 0.139 | 1.00 / 1 | yes (class 1) | 1.000 | 0.0 / 0.0 | 0.100 | 0/40 |
| 37 | 2.000 | 0.141 | 1.03 / 2 | yes (class 0) | 1.000 | 0.0 / 0.0 | 0.150 | 0/40 |

**Reading.**

1. The bare-path selected entropies reproduce 1061's recorded 0.1169 / 0.0 / 0.0 exactly. This fidelity check shows the decomposition describes the same phenomenon.
2. The full agent path (`generate_trajectories` + `select_action` with a forced E3 tick, agent.py:6661 / :6969) gives the same picture, so the bare `e3.select` shortcut is not the cause.
3. The pool's majority first-action class is **invariant across state** within a seed. The proposer is not proposing state-appropriate alternatives. The only alternatives are the SP-CEM floor's tokens (`_support_preserving_target_class_count`, `hippocampal/module.py:1419-1432`; default target 2, `config.py:2778`).
4. A token beats a typical majority candidate at 10-35% of states. It never beats the best of ~31, which is what one sample against the minimum of 31 samples predicts under roughly exchangeable scores. **E3 is not shown to reject the alternative on content.** The imbalance alone produces the monostrategy.
5. Verdict for this regime: **Type A at generation** (the alternative is never elaborated). The link is **pool class balance and state-conditioning of the proposal**, not E3 and not commitment.
6. Limits:
   - Toy dimensions, 20 warmup episodes, and the 1061 undertraining caveat still applies.
   - No usefulness oracle exists in this ecology, so "useful alternative" is not assessed.
   - Domain: D1 on the pool; D2 only in the weak sense that bare vs full selection agree.

## 3. Adversarial audit of the Type-B-shaped signals

| Signal | Why it looks like Type B | Adversarial finding | Credit as Type B? |
|---|---|---|---|
| 931 (`planning/failure_autopsy_931-932-wanting-authority-cluster_2026-08-16.md`): 80% CEM argmin flips at W=5000, `mean_resource_proximity` bit-identical 0.6229773644254133 | proposer preference moves, behaviour does not | **Mere channel presence / architecture.** `select_action` re-scores the whole pool (agent.py:6969 onward), so the CEM elite pick is not a consumer path. Bit-identity is what non-connection predicts, not access collapse. The usefulness of the flipped pick is unmeasured (no P1/P5). | No |
| 654i / 654j (`..._V3-EXQ-654j_2026-06-22.md`): the selection face passes (689d ON 0.938 vs 0.371), committed-class entropy lift 1/3 | alternatives selected but not committed | **Diversity, not usefulness.** The DV is committed-class entropy, and more classes is not more useful classes. There is also a metric-suppression risk: 689d was later withdrawn over its hold-weighted DV and inert matched-noise control (`..._V3-EXQ-689d_2026-07-20.md`). | No (P1/P5 absent) |
| 947 / 949: trained MECH-314b head, 4.934/5 classes, yoked divergence 0/320, rising to 0.3675 with authority rescale | represented content without authority until gain changes | **Gain, not routing.** A static rescale fixes it, and the spec lists "a static learned bridge is sufficient" as a keep-V4-deferral result. Usefulness is unmeasured. | No (and it argues for the synaptic approximation) |
| 804: `e3_score_gradient_without_selection_authority` | E3 has a gradient but no authority | **This is P4 failing, not P6.** A normalised range of 0.00095 is effectively flat relative to magnitude, and the spec requires P4 before Type B. | No |
| 567 seed 43 / 569h-i single rows: pool 2.0-2.35 classes, commit ~1 | alternatives present, not committed | **Order-statistic / imbalance artifact** (section 2.3 mechanism). Those runs record class counts and entropy means per seed, not the per-state majority share, so this cannot be separated from a 31:1 imbalance (689j, which does record `pool_dominant_class_share_mean`, sits at 0.67). | No |
| 1014: STAY chosen inside the harm field while constant movers survive | a useful alternative (move) exists, the agent picks a lethal one | **The strongest candidate, and it still fails P5.** The ecology needs no switching, so this is a *selection-quality* failure (H-stay-selection-dominance, alive), not access to a latent strategy. The pool's move-class share at STAY decisions was not recorded, so a Type-A generation artifact is not excluded. **Punishment-avoidance risk:** STAY may be E3 minimising predicted harm on a mis-predicted field. | No; this is the best ecology to extend (section 4.1) |

No signal passes the checks for proxy reward, action removal, metric suppression, undirected noise, punishment avoidance, hard-coded lookup, privileged information, memorisation and channel presence **and** also has P1 and P5.

## 4. The discriminating assay (DESIGN ONLY -- not queued; no script in ree-v3/experiments)

### 4.1 Ecology: none existing satisfies P1 and P5 -- the nearest build

- **Finding:** no existing environment or curriculum satisfies P1 and P5 by construction.
- **Nearest, with a native lever:** the Q-080 two-corridor effort layout (`causal_grid_world.py:2039-2103`), with `effort_benefit_asymmetry` switched **between episode blocks**. The attribute is read per step (`:2968`), so a driver-side block schedule needs no substrate edit.
  - Block A (asymmetry 0): the low-effort corridor is optimal. Benefit is tied and energy cost is lower.
  - Block B (asymmetry 0.5, the value 731 used as its control): the high-effort corridor is optimal.
  - P1 holds by construction (two routes, each optimal in one block). P5 holds by construction (a fixed corridor is suboptimal in one block).
  - The oracle is evaluator-only: `_effort_corridor_at` (`:2173-2185`) labels the corridor.
- **Blocking gap:** the agent does not navigate this layout. 731 measured corridor entry 0.333 < 0.5 and value-term non-vacuity 0/3 at 6 episodes. The "locally attractive + delayed adverse" variant the orchestrator programme needs (a delayed hazard on one corridor) is **not built**.
- **Alternative:** the 1014 pinned boards, extended by a mid-run swap that makes the current constant-move direction hazardous. This inherits a recorded yardstick (constant movers 200/200, STAY 10-14 steps), but it needs a board-swap env build.
- **Recommendation:** start with the Q-080 block reversal. It is the only candidate that needs no env code. Gate everything on Stage 0.

### 4.2 Chain, stages and per-stage quantities

Take a decision state *d* = a fresh E3 tick at the bottom junction before corridor entry. `U(d)` = the block's optimal corridor class (oracle, evaluator-only, never fed to the agent).

| Stage | Quantity at *d* | Tensor it is read from |
|---|---|---|
| S1 proposer present | at least one candidate whose rollout enters the U corridor; also the U-class share of the pool | candidate `actions` (first lateral action) |
| S2 represented (reader input) | U and non-U candidates' E2-predicted `world_states` separable by a held-out linear read, AUC > 0.75, and the E3-consumed channel values (benefit / energy / harm terms) differ between them | the exact tensors E3 consumes, not an external encoder (avoids probe-only D1) |
| S3 evaluated | E3 ranks the U class best by **class-mean** score AND by best-of-class after **matched subsampling** (equal count per class), which removes the section 2.3 order-statistic bias | `SelectionResult.scores` (`e3_selector.py:114-132`) |
| S4 committed | E3 selects a U candidate with `committed=True` | `SelectionResult` |
| S5 executed | the executed first action is in the U class (no hold/latch/refractory override) | env step |

- Transmissions: T12 = P(S2|S1), T23 = P(S3|S2), T34 = P(S4|S3), T45 = P(S5|S4).
- **Primary endpoint:** authority fraction AF = P(S5 | S1 and S2) in block B (post-reversal), per seed.
- **Secondary endpoints:**
  - reversal latency: episodes to AF >= 0.5 after the switch;
  - baseline competence retained: block-A AF;
  - relapse: AF drop in a return-to-A block.

### 4.3 Interventions that make Type A and Type B predict different outcomes

All interventions are at matched pool size K (an injection *replaces* the worst-scoring candidate) and use matched seeds and RNG.

| Arm | Manipulation | Type A predicts | Type B predicts |
|---|---|---|---|
| N0 native | none | S1 or S2 low in block B | S1 and S2 high; AF low |
| I1 inject-useful | U-corridor action sequence rolled through native E2 (`e2_fast.py:746` `rollout_with_world`) into the pool before `select_action` (`agent.py:6969`; the seam is `act`, `agent.py:11032-11070`) | if generation is the only missing link: T23..T45 high on the injected candidate, **AF rescued** | T23 or T34 or T45 stays low (the injected candidate is represented but loses authority) |
| I1c inject-mismatched | same, but the non-U corridor (mismatched-content control) | not selected above its base rate | not selected above its base rate. If it IS selected as often as I1, E3 reads novelty/position, not content: the arm is invalid |
| I2 score clamp (dose) | additive per-candidate `score_bias` on the U candidate at 0, 0.5, 1, 2, 4 x the per-state score SD (`e3_selector.py:3182`) | S3 flips at a low dose and S4/S5 follow | S3 flips but S4/S5 lag; a dose-response gap between S3 and S5 localises the block to commit/execution |
| I2+ positive control | clamp at 20 x SD | S5 ~ 1 (otherwise the pipeline is broken and the run is invalid) | same |
| I3 native force-commit + retention | I1+I2 for the first 3 block-B episodes so E3 itself commits U; then unforced | AF rises only if experience reaches later selection (loop edge) | Type B with a pure access block: AF stays low after forcing ends, despite experienced benefit. Yoked control: force the non-U corridor at matched exposure |

**Why force-commit must go through E3 and not an env-side override:** residue accumulation is commitment-gated on `_committed_trajectory` (`e3_selector.py:4690-4697`). An override that bypasses `select` would silently remove the experienced-consequence write and confound retention. The driver must call `record_executed_action` (`agent.py:11539`) and name its trainers, with the runtime optimizer-coverage assertion that 1061 already carries.

### 4.4 Controls the spec requires BEFORE any coordination hypothesis

1. **Static learned bridge.** A fixed linear reader from candidate E2 `world_states` to an additive `score_bias`, trained offline on block A+B experience. The routing does not depend on state; only the content is read. If it rescues AF, then **STOP: the V3 synaptic approximation suffices.**
2. **Diversity pressure** (existing, all default-off):
   - `support_preserving_per_class_quota` (`config.py:2790`), which targets the section 2.3 imbalance directly;
   - `use_f_eligibility_demotion` (`config.py:1961`, MECH-448);
   - `use_selection_entropy_floor` (`config.py:5056`);
   - `score_diversity` (`predictors/e3_score_diversity.py`).
   If any of these rescues AF without losing block-A competence, then **STOP**.
3. **Matched random routing.** A random per-candidate `score_bias` with magnitude distribution and switching frequency matched to control 1's output, and independent of state. If it matches the best arm, the effect is undirected noise: **STOP**.
4. **Content ablation.** Zero the U candidate's E2 `world_states` deviation, replacing it with the pool mean. Any arm that still rescues is using something other than content, such as privileged position or a lookup. **The arm is invalid.**

### 4.5 Stop results (pre-registered, fail-closed, evaluated in order)

1. **Stage 0 competence gate fails**: block-A corridor entry < 0.8 or block-A AF < 0.6 on more than 2 of 8 seeds. The run is non-adjudicable. Route to the competence floor (MECH-457 / `competence_floor`); do not draw more seeds.
2. **N0 S1 < 0.2 AND I1 rescues AF** (ΔAF >= 0.2): **Type A at generation.** Next work is repertoire formation at the proposer (pool class balance and state-conditioning, then the MECH-314 / ARC-065 rarity drive already routed). Coordination is not earned.
3. **I1 does not rescue, and T23 is low while S2 is high**: a reader failure at E3. Test control 1 first. If the static bridge rescues, the result is Type A of the value-read (V3 sufficient).
4. **Any of controls 1-3 rescues**: V4 deferral stays intact.
5. **Only if** S1 and S2 are high, AF is low, I2 shows S3-to-S5 authority is recoverable, **and** controls 1-3 all fail: Type B is earned. Only then open the spec's routing arms B-D (stochastic / periodic / endogenous state-dependent), with routing-state shuffle as the causal check.

### 4.6 Seeds and power

- **Replication unit:** the seed (an independently trained agent). Pre-registered **n = 8 seeds**, fixed, never drawn until a floor is met. At least 150 junction decisions per seed per block.
- **Decision rule:** paired per-seed ΔAF (arm minus N0), one-sided Wilcoxon signed-rank at α = 0.05 (the exact minimum p at n=8 is 0.0039), **and** ΔAF >= 0.20 absolute **and** the same sign on at least 7/8 seeds.
- **Exclusions:** seeds failing Stage 0 are excluded and reported. More than 2 exclusions makes the run non-adjudicable.
- **Power:** the per-seed SD of AF is **not recorded anywhere**. Assuming SD 0.15 (an assumption, not a measurement), ΔAF 0.20 gives d ≈ 1.33, and the paired n = 8 power is about 0.85. Stage 0 must measure the SD and re-size n **before** Stage 2 opens.
- **Generalisation:** at least one altered ecology (the swapped 1014 board) before any promotion, per the spec's discriminating-result item 7.

### 4.7 Premise pre-flight against live code @ `00210b5` (read-only)

| Check | Producer (file:line) | Grade |
|---|---|---|
| Ecology P1+P5 by construction | `effort_benefit_asymmetry` CGW:896, read per step :2968; oracle `_effort_corridor_at` :2173 | **AMBER**: the lever is native and the block schedule is driver-side |
| Agent competence in that ecology | 731: corridor entry 0.333 < 0.5; C2 0/3 (`experiments/v3_exq_731_q080b_least_effort_prior_20260709T211800Z_v3.json`) | **RED**: the last measurement fails the Stage 0 gate (6 eps; untested at scale) |
| I1 injection has a native producer | `e2_fast.py:746` `rollout_with_world`; `agent.select_action(candidates, ...)` `agent.py:6969`; seam `agent.py:11032-11070` | **GREEN** |
| I2 clamp has a native producer | `E3Selector.select(score_bias=...)` `e3_selector.py:3182` exists, but `REEAgent.select_action` passes only its internal `dacc_score_bias` (`agent.py:9858`) and has no external setter | **AMBER**: needs a default-off `set_injected_score_bias` on the existing `set_injected_*` pattern (`agent.py:4237-4264`) via /implement-substrate, or a monkeypatch that skips agent-level channels (not acceptable for the primary arm) |
| I3 native commit path | commitment state `e3._committed_trajectory`; residue write gated at `e3_selector.py:4690-4697`; `record_executed_action` `agent.py:11539` | **AMBER**: depends on I2; the trainers must be named and coverage-asserted |
| The load-bearing criterion can fail | AF can be low under N0 (section 2.3 shows selection concentrating on a state-invariant class) and can be high under I2+ | **GREEN** in principle |
| DV signals live, not floor-pinned | selected-action entropy is floor-pinned (0.0-0.117) in the 1061 regime (recorded; reproduced here). Score spread is live (1.42-4.01, this record). Pool class share is live but imbalanced. | **AMBER**: AF is live only after Stage 0 passes; pool class share must be logged, not just class count |
| Controls exist | `support_preserving_per_class_quota` config.py:2790; `use_f_eligibility_demotion` :1961; `use_selection_entropy_floor` :5056 | **GREEN** |

**Overall: RED as a single experiment today** (the competence gate is measured failing and there is no switching ecology in use). **AMBER** for a Stage 0 run (block-reversal effort layout, N0 only, competence + S1/S2 logging + AF SD), which can be authored via /queue-experiment once the Q-080 navigation question is answered.

## 5. L/S/F classification and minimal rivals (if Type B were ever found)

- **The prerequisite problem** (does a useful alternative exist, is it proposed, is it used) is **Class L**. Proposal balancing, entropy regularisation, count-based / rarity drives (Bellemare 2016) and QD archives (MAP-Elites) are literature-specified. They should be adapted before anything else.
- **The dynamic-coordination rescue** is **Class S, possibly F**, as the spec says. Its biological components are literature-constrained; the REE learning/control rule for state-dependent causal access is not.
- **Minimal competing mechanisms**, all default-off and each instrumentable, simplest first per the Frontier Loop Step 2/7:
  1. static content-read bridge (control 1);
  2. conflict-graded eligibility width (the built MECH-448 envelope or top-k = f(gap));
  3. state-dependent gain on an existing channel keyed to an already-live signal (prediction error or harm-variance), with no new content;
  4. a two-state latch-release rule (dwell-time-dependent de-commit; root C of the conversion ceiling);
  5. only then a learned router.
  Each is judged on the section 4.5 battery. Rescue must come without new content entering, and it must be abolished by routing-state shuffle.

## 6. What this changes, and for whom

- **For the coordination thought:** it stays a hypothesis. The V4 deferral is intact on current evidence, and the V3 synaptic approximation has not been shown insufficient.
- **The sharpest measured monostrategy (1061 regime) is a generation-stage defect.** The proposal's class is invariant across states and alternatives exist only as floor tokens. This is a **new, citable D1 finding**. It sits upstream of both the F-dominance and the commitment roots, and it predicts that the 567-style "pool 2 classes, commit 1" rows are the same imbalance artifact.
- **Owed follow-on (reported to the orchestrator, not chipped here):**
  1. `puzzle (known rules)`: does the effort layout become navigable at scale (the 731 caveat)? This is the Stage 0 gate.
  2. `complicated (buildable)`: a board-swap / delayed-hazard ecology for the altered-ecology leg.
  3. `complex (probe-gated)`: a warmup-scale sweep of pool class share and state-conditioning on the 1061 driver (20/60/180 eps, one seed, about 30 min on the Mac per the MECH-131 cost table) to find whether the state-invariant proposal is undertraining or structural. This answers the untested caveat MECH-131 declined, with a cheaper DV.
