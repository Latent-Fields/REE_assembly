# Grounded main-channel valuation: frontier design and feasibility (E3 channel worth learned from experienced consequence)

- **STATUS: FINAL, 2026-09-24T22:12:42Z (commit time of `50b679abb8`).** The interim (steps 1-3) was `3553d59a13`. Changes since: premise P-c is CORRECTED (section 0), M1 and M3 are amended after the step-4 diagnosis (section 3a), and sections 4-6 are added.
- **Domain reached: D1.** The grounded signal and the channel votes exist, are measured and are attributable, open-loop, in 9 closed-loop arms (bit-identical canaries) plus 3 off-policy streams. **No candidate was run closed-loop.** D2/D3 is the battery's job (section 5).
- Session `bt0924-valuation` (Worker G, breakthrough integration pass `orchestrate-20260924-breakthrough`), chip_ref `chip-20260924-grounded-valuation-frontier-design`.
- **Design and feasibility only.** Nothing lands in ree_core, nothing is queued, no chips are spawned and no registry is edited.
- Edge under design: GFLAG-0487's "experienced consequence -> main-channel valuation weights". Follows from `e3_evaluation_edge_test_20260924.md` ADDENDUM 1-3 (origin `5e3c956b41`) and `e2_rollout_divergence_and_proposal_state_dependence_20260924.md` ADDENDUM 3.
- Code read: ree-v3 `origin/main` @ `44c55300ca`, in a private detached worktree. It is the same commit the whole chain used (re-fetched 2026-09-24; origin/main has not moved). All file:line citations are against it.
- Method: `docs/thoughts/2026-09-24_experimental_learning_beyond_literature.md`, the Frontier Mechanism Discovery Loop. The order is: classify L/S/F; state the phenomenon and falsifiers before any algorithm; propose deliberately different minimal rules, fixed ones first; then a hard-gated adjudication battery.

## 0. Premises re-measured (D0 code reads unless stated)

- **P-a. The main-channel weights are plain scalars read on every score call.**
  - They are `f_weight`, `lambda_ethical`, `rho_residue`, `benefit_weight` and `goal_weight` on `E3Config`, read inside `score_trajectory` (`e3_selector.py:1696-1770`).
  - `lambda_ethical` is multiplied by the SD-011 affective scale (`:1696-1699`).
  - Consequence: **a weight-learning candidate can be prototyped in a probe by writing those config fields between E3 ticks, without touching ree_core.** Nothing in the design needs a substrate change before adjudication.
- **P-b. Per-candidate, per-channel terms are readable without changing behaviour.**
  - `e3_score_decomp_enabled=True` fills `_last_traj_components` per candidate (`:1821-1834`) and `last_score_decomp["per_candidate"]` (`:3953-3957`).
  - It is diagnostics-only. A canary in step 4 checks that turning it on is behaviour-neutral.
- **P-c. E3 has two choice rules, and a channel weight only has authority on the committed one. CORRECTED in step 4: this does not bind here.**
  - A **committed** tick takes the argmin (`:4509`).
  - An **uncommitted** tick samples `softmax(-scores / T)` (`:3976`, `:4531`) with `T = 1.0`, passed by the harness (`_harness.py:321`). The measured normalised entropy of that softmax is 0.9999, so it is uniform.
  - **Measured:** 98.6-99.3% of E3 ticks are committed in every arm (section 4). So channel weights have authority on almost every tick in this regime. The interim's worry was real in mechanism but negligible in rate.
- **P-d. ARC-108 learned gating does not do this job.** This is inherited from `e3_evaluation_edge_test` ADDENDUM 3 and re-read here, not re-probed:
  - its `w_chan` re-weights only the modulatory accumulator (`config.py:1436-1437`);
  - its teaching signal is an internal evaluator proxy, `benefit_eval - harm_eval` (`e3_selector.py:4848-4855`);
  - it is unarmed in this regime.
- **P-e. The legitimate grounded signal already reaches the agent natively.**
  - The harness passes the env's scalar `harm_signal` to `agent.update_residue(harm_signal=...)` after every step (`_harness.py:358-365`). Residue accumulates from it.
  - Using that scalar as a valuation teaching signal therefore adds no information the agent does not already receive.
  - `transition_type`, hazard and resource positions, and cloned-env Q values are env internals. They are **privileged**: they are allowed in scoring and forbidden to every candidate.
- **P-f. Contact and proximity events are separable on the scalar alone,** by magnitude (code read):
  - hazard contact `-hazard_harm = -0.5` and resource contact `+0.3` (`causal_grid_world.py:273, 275`);
  - proximity shaping at most `0.05 x field` (harm) and `0.03 x field` (benefit) (`:339-340`).
  - A magnitude threshold on the received scalar is therefore a legitimate contact-only signal.
  - **Confirmed empirically** in 9,000 labelled steps (3 seeds): contacts have |r| of 0.33-0.583, and proximity steps have |r| of at most 0.083. The 0.1 threshold is clean on every seed.
- **P-g. The goal channel is dead in this regime (measured).** `goal_weight` is 1.0 here, but the goal term is 0.0 on every E3 tick in all 9 arms, because the goal state is never active (`e3_selector.py:1757`). The goal channel is excluded, so the battery calibrates FOUR channels: F, harm, residue and benefit.

## 1. Prior-art scope and classification: **Class S (synthesis-required)**

Searched on 2026-09-24 with web search and PubMed, time-boxed. What was read is stated per item: abstract, search-result summary, or known standard text. Nothing is cited beyond that level.

- **The learning law is literature-specified.**
  - **Successor features and GPI** (Barreto et al., NeurIPS 2017, "Successor features for transfer in reinforcement learning"; Barreto, Hou, Borsa, Silver & Precup, PNAS 2020, "Fast reinforcement learning with generalized policy updates", doi:10.1073/pnas.1907370117).
    - The reward is modelled as r = phi(s,a)^T w, and **w is obtained by linear regression of observed reward on features**. Learning a new task then reduces to that regression. (Read at search-summary level.)
    - This is the closest published mechanism. It is candidate M2 below, with the features taken to be E3's channel terms.
  - **Gradient-bandit and REINFORCE credit for the parameters of a softmax choice rule** (Sutton & Barto, *Reinforcement Learning: An Introduction*, 2nd ed., sec. 2.8 and ch. 13; standard text, not re-read today). This covers candidates M1 and M3 in form.
  - **Human learning of feature/dimension weights from reward prediction error** (Niv et al., J Neurosci 2015, "Reinforcement learning in multidimensional environments relies on attention mechanisms", doi:10.1523/JNEUROSCI.2978-14.2015; abstract read via PubMed).
    - People learn which stimulus dimensions predict reward and weight them accordingly.
    - This is the behavioural analogue of learning which E3 channel is worth attending to.
- **Adjacent work that does NOT solve the REE problem.**
  - **Multi-objective RL scalarisation** (Hayes et al., "A practical guide to multi-objective reinforcement learning and planning", AAMAS 2022; search summary). It assumes a VECTOR reward with known, valid components, and the scalarisation weights usually encode a user utility. In REE the components are the agent's own learned estimates, of unknown validity, and there is ONE grounded scalar.
  - **Meta-gradient RL** (Xu, van Hasselt & Silver, NeurIPS 2018; abstract). It adapts return and objective parameters online by differentiating through the learner's update. It is heavier and needs a differentiable path from the weights to later behaviour. It is kept as an escalation option (frontier doc Step 7), not a first candidate.
  - **Neural common currency** (Levy & Glimcher, Curr Opin Neurobiol 2012, doi:10.1016/j.conb.2012.06.001; abstract via PubMed). A vmPFC/OFC common value scale exists. That establishes that integration happens, not how the exchange rates between attributes are learned.
  - **Opponent Go/NoGo value channels whose relative gain is modulated by dopamine** (Collins & Frank, "Opponent actor learning (OpAL)", Psychol Rev 2014, PMID 25090423; title-level only). This is the nearest biological analogue for learning the relative authority of a cost channel and a benefit channel from outcome. It is cited as an analogy, not as a specification.
- **What is REE-specific: the couplings, which are REE conjectures and must be tested directly.**
  1. **The features are fallible internal estimates.** SF/GPI assumes good features. Here a channel can be untrained, or trained on shuffled labels, and the commensurability operator already showed that spread-based schemes hand such channels full authority (ADDENDUM 2). So the weight rule must double as a **validity test of each channel**: down-weight a channel whose votes do not predict outcome.
  2. **Credit crosses commitment.** One E3 pick governs several env steps, and outcomes are sparse. Which window gets credited is a design choice, not a given.
  3. **The harm channel is ethically protected.** Driving `lambda_ethical` toward zero because harm-avoidance costs reward is exactly the reward-hacking failure REE must not permit. The literature has no counterpart to this floor constraint, so it is imposed as a hard bound, and a candidate that presses against it is flagged.
  4. **Residue is itself experience-derived memory,** accumulated from the same scalar. Learning its weight from that scalar risks double-counting harm evidence.
  5. **Channel authority lives only on committed ticks** (P-c).
- **Verdict: Class S.** The learning law is Class L (linear reward-weight regression; gradient or eligibility credit). The coupling, where the features are the agent's own fallible channel estimates under protected-harm, commitment-windowed, sparse grounded credit, is a REE conjecture with no direct precedent found. It must be tested as a coupling. It is not Class F: nothing about the law itself is new.

## 2. Phenomenon and falsifiers (stated before any algorithm)

**Contract.**
- **May read:**
  - the received scalar r_t (`harm_signal`) and its magnitude;
  - E3's own per-candidate channel terms at each tick;
  - the selected index and the committed flag;
  - the agent's own body state.
- **May write:** ONLY the scalar channel weights (F, harm, residue, benefit, goal), in log space. The bounds are a factor of 4 either side of their defaults, and harm has a hard floor at its default / 4.
- **Must NOT read:** `transition_type`, env positions, cloned-env Q, which head is trained or shuffled, or any label identity.
- **Must NOT write:** the heads, the residue field, the candidate set, the action set, or the commit threshold.
- **Forbidden shortcuts:**
  - hand-set weights;
  - per-seed tuning of the learning rate after seeing outcomes;
  - using the proximity-shaping stream to score success;
  - removing hazard affordances or actions.

**Regime.** The T2 regime of `e3_evaluation_edge_test` ADDENDUM 1: tie-break ON, R5b scaffold, COV head, R2 depth 2, and evaluators trained on own experience with the native benefit gate. T1 is the same with untrained evaluators. T3 is the same with evaluators trained on label-permuted data.

**Phenomenon (all three are required together).**
- **P1, behaviour.** Versus T1: resource consumptions + benefit-approach steps rise, AND harm CONTACTS are not worse (at most T1 + max(2, 20% of T1)). This must hold on at least 2 of 3 seeds of the primary ecology.
- **P2, valuation.** The learned weights discriminate channel validity.
  - With trained evaluators, the end weights of harm_eval and benefit_eval exceed their weights under the same rule with shuffled evaluators (T3 heads), on at least 2 of 3 seeds for each channel.
  - Residue's weight is not driven to its floor.
- **P3, causal.** On the same seed and state:
  - freezing the learned weights reproduces the P1 difference;
  - restoring the default weights removes it;
  - a random weight vector with the same log-norm displacement does not reproduce it.

**Kill conditions per candidate.** Any one of these kills the candidate. They are hard gates; a high aggregate score cannot compensate.
- **K1, blind to validity.** Trained and shuffled heads end with weights that do not differ in the predicted direction (fails P2).
- **K2, no calibration.** The benefit gain comes with harm contacts above the P1 tolerance. That is the ungrounded T2 failure again.
- **K3, reward hacking.** The harm weight sits at its floor for more than 25% of ticks, or its trajectory is monotone-down while harm contacts rise.
- **K4, no better than the null.** It does not beat M4, matched random drift, on P1 and P2.
- **K5, shaping gamed.** The gain appears only in proximity-shaped reward (approach steps), with consumptions not up and contacts not down.
- **K6, no transfer.** Weights learned on the primary ecology, frozen, and run on an altered ecology (a different seed family or board) lose the P1 advantage over T1 on that ecology.

**Programme-level falsifier.** No candidate beats M4 on P2 within the budget in section 5. That would mean the channel votes at depth 2 carry no attributable information about grounded outcome at this substrate, and the binding constraint sits upstream again, in representation or prediction. That is itself a result, and it routes back to GFLAG-0487's chain.

## 3. Candidates: deliberately different minimal rules (simplest first)

**Notation.**
- At E3 tick t there are candidates k = 1..K.
- x_{k,c} is channel c's RAW term, the weighted term divided by the current weight w_c.
- s_c is the channel's sign in J: +1 for costs (F, harm, residue), -1 for benefit and goal.
- The chosen candidate is k*.
- **Channel vote** v_c(t) = -s_c (x_{k*,c} - mean_{k != k*} x_{k,c}). v_c > 0 means channel c favoured what was chosen.
- **Outcome window** R_t = the sum of r over the env steps from tick t up to the step before tick t+1, i.e. the steps E3's pick governs.
- Weights are w_c = w0_c exp(theta_c), with theta_c clipped to [-ln 4, +ln 4]. Harm additionally has theta >= -ln 4 as its hard floor.
- Every candidate updates ONLY on committed ticks, per P-c. Uncommitted ticks are logged, not credited. This is a stated design choice; section 5 includes a variant that credits all ticks.

**Grounded signal.** Two legitimate variants, both computed from the received scalar alone (P-e, P-f):
- **G-all:** r_t as received, including proximity shaping.
- **G-contact:** r_t kept only when |r_t| > 0.1, i.e. contacts and consumptions only.

They are designed to disagree on K5. Every candidate is run with both.

- **M1 -- sparse sign rule (fixed, interpretable).**
  - On a committed tick with R_t != 0, and for each channel with |v_c| above that channel's running median |v|: theta_c += eta1 * sign(R_t) * sign(v_c).
  - A channel that voted for a pick followed by good outcome gains weight; one that voted for a pick followed by bad outcome loses it.
  - It ignores magnitudes and zero-outcome ticks, and is order-dependent and online.
  - **Predicted signature:** fast, noisy, and vulnerable to rare-event luck.
- **M2 -- reward regression on channel votes (SF/GPI-style; batch, confidence-gated).**
  - Online ridge regression of R_t on the vote vector v(t) over all committed ticks, zero-outcome ticks included: R_t ~ b + sum_c beta_c v_c(t).
  - The weights follow the evidence: theta_c = clip(kappa * t_c), where t_c = beta_c / SE(beta_c).
  - It is order-invariant, uses magnitudes and null outcomes, and does not move a weight until the evidence exists.
  - **Predicted signature:** slow, but a principled null. An uninformative (shuffled) channel's t-statistic stays near 0, so its weight stays at default rather than being actively down-weighted.
  - That is its specific weakness against P2. It can fix harm-overshoot only by RAISING residue or harm, never by LOWERING a bad channel below default unless beta < 0.
- **M3 -- grounded three-factor eligibility on MAIN channels (the ARC-108 rule, transplanted).**
  - Per env step: e_c <- lambda * e_c + v_c(t_tick) (injected at committed ticks; lambda = 0.9 per step); V <- V + beta (r_t - V) with beta = 0.05; delta_t = r_t - V; theta_c += eta3 * delta_t * e_c * asym(delta), where asym is 1.0 for delta > 0 and 0.5 for delta < 0.
  - The eta, lambda, beta and asym values are the ARC-108 constants (`config.py:1445-1449`), deliberately reused.
  - Credit is temporally extended across the commitment window, baseline-subtracted and continuous. It differs from ARC-108 in exactly two respects: (a) it targets the MAIN channels, and (b) its delta comes from the GROUNDED scalar rather than the evaluator proxy.
  - **Predicted signature:** it credits delayed consequences (a hazard contact 3 steps after the pick) that M1 and M2 attribute only through R_t.
- **M4 -- null: matched random drift.** theta_c performs a zero-mean random walk on the same tick schedule and within the same bounds. Its per-tick increment SD per channel is matched to the realised per-tick |delta theta_c| of the candidate it controls for, and its noise seed is independent. Any real mechanism must beat it on P1 and P2 (K4).
- **M0 -- frozen defaults (= T2).** This is the reference for P1 and P3.

**Why these four disagree.** They disagree on:
- whether a shuffled channel is actively DOWN-weighted (M1, M3) or merely left alone (M2);
- whether delayed outcomes are credited (M3) or only in-window ones (M1, M2);
- whether single rare events move weights (M1) or only accumulated evidence does (M2).

Section 5 places the arms where those differences change the P1/P2 readout.

**Learning rates and feasibility:** measured in section 4 (FINAL), from the event rates that are actually available.

### 3a. Amendments forced by the step-4 diagnosis (made before any candidate was run closed-loop)

The frontier doc's Step 6 ("diagnose failures and synthesize successors") applied at D1. Two structural defects showed up in the recorded streams (section 4.3). Each is fixed here, and the unfixed rule is kept as a control.

- **Votes are one-sided.** The chosen candidate is the argmin of the summed score, so a dominant channel votes FOR the pick on almost every tick. In T2, the fraction of committed ticks on which each channel voted for the pick (F / harm / residue / benefit) was:
  - s42: 0.39 / 0.99 / 0.58 / 0.97;
  - s43: 0.59 / 0.69 / 0.38 / 0.68;
  - s44: 0.83 / 0.14 / 0.38 / 0.87. On s44 benefit overrides harm on 86% of ticks, which is the domination itself.
- **So M1's raw rule, sign(R) x sign(v), mostly measures the OUTCOME BASE RATE, not channel validity.**
  - On a harm-dominated stream (T2 s42: 38 negative vs 5 positive contact windows), it pushes every dominant channel down, harm included.
  - Measured drift per event: harm -0.33, benefit -0.37, residue -0.19, F -0.16. That is the K3 reward-hacking direction, produced by a common mode rather than by evidence.
  - **M1 raw is therefore kept as the POSITIVE CONTROL for the K3 detector:** the battery must see it fire.
  - **M1c** (the candidate) uses a centred vote, v_c minus its running mean (EMA 0.05), and a centred outcome, sign(R_t - Rbar), where Rbar is the running mean contact outcome per committed tick.
- **M3 with the ARC-108 asymmetry (depression x0.5) has a potentiation bias.**
  - With a baseline-subtracted delta of about zero mean, halving the negative half makes net drift proportional to the mean vote, so dominant channels are potentiated.
  - Open-loop z on T2 s42 was 3.4 to 4.1 on ALL four channels at asym 0.5, and 0.06 to 2.0 at asym 1.0. On s44 it was -2.5 to 2.5 at asym 0.5, and -0.2 to 0.5 at asym 1.0.
  - **M3n** (the candidate) uses asym 1.0, and votes normalised by each channel's running mean |v| so the weight step is scale-free. That is needed because at ARC-108's eta = 0.01 with raw votes, theta moved at most 0.018 in 600 steps (section 4.4).
  - Normalising votes does NOT reintroduce ADDENDUM 2's noise-gets-a-vote defect. Here the normalised vote only sets step size, and the SIGN of the step comes from the grounded delta. A channel whose vote does not covary with delta random-walks, and M4 bounds that walk.
- **M2 gains action-class fixed effects:** R_t ~ b_{a(t)} + sum_c beta_c v_c(t), where a(t) is the first-action class of the pick.
  - Off-policy, an UNTRAINED head's vote predicted consumptions at t = 2.73 without fixed effects (s43), and at 1.74 with them.
  - The mechanism: any head's vote is partly a fixed function of the action class, so it inherits per-action base rates. Fixed effects remove that route.
- **Section 5 runs the amended candidates:** M1c, M2 (with fixed effects), M3n, and M4 matched to each. M1 raw is the K3 positive control, and M0 = T2 is the frozen reference.

## 4. Feasibility (measured; D1, open-loop on recorded streams)

**Probes:**
- `probes/valuation/valuation_feasibility_probe.py` re-runs ADDENDUM 1's TB regime with a read-only tap on `E3.select`: the per-candidate channel terms, selected index and committed flag per tick, plus the per-step reward and transition type.
- `probes/valuation/analyze_feasibility.py` computes the tables below.
- `probes/valuation/offpolicy_vote_probe.py` + `analyze_offpolicy.py`: a uniform-random-action stream of 1,500 steps per seed. At each state the 5 scaffold candidates are rolled out once by E2 (COV head, depth 2) and scored under untrained, trained and shuffled heads. Votes for the executed action are regressed on the grounded outcome.
- `probes/valuation/common_mode_check.py` backs section 3a.
- To re-run, copy `probes/rollout/*.py` and `probes/evaluation/evaluation_edge_probe.py` next to these scripts, together with a detached ree-v3 worktree at `ree-v3-wt/` (@ `44c55300ca`). Run `valuation_feasibility_probe.py --seed s` and `offpolicy_vote_probe.py --seed s` for s in 43 44 42, then the two analyzers.
- Settings: seeds 42/43/44; world_dim 32 (deployed); Mac CPU, 2 threads, one process at a time. The TB closed loop costs **17-20 s of wall time per 600 steps**, plus a 90-120 s preamble per seed per process.
- Raw per-tick JSON (`VF_s*.json`, `OP_s*.json`, 1-2 MB each) is kept in the session scratch dir `.scratch/breakthrough-20260924/valuation/results/`. The committed `VF_analysis.json` and `OP_analysis.json` carry every number cited here.

**Canary: the tap is inert.** All 9 closed-loop arms reproduce `TB_s{42,43,44}.json` bit-for-bit: harm contacts, hazard-proximity steps, consumptions, approach steps, reward and episodes.

### 4.1 E3 tick structure and grounded event rates (per 600 closed-loop steps; seeds 42 / 43 / 44)

| arm | E3 ticks | committed | env steps per tick | ticks whose window has R != 0, G-all | same, G-contact | contact steps, harm- / benefit+ |
|---|---|---|---|---|---|---|
| T1 FULL | 87 / 82 / 83 | 98.8-98.9% | 6.9 / 7.3 / 7.2 | 19 / 21 / 9 | **7 / 9 / 5** | 8-0 / 5-4 / 6-0 |
| T2 FULL+EVAL | 135 / 81 / 127 | 98.8-99.3% | 4.4 / 7.4 / 4.7 | 85 / 25 / 73 | **43 / 7 / 24** | 39-7 / 6-1 / 22-5 |
| T3 FULL+SHUF | 81 / 71 / 85 | 98.6-98.8% | 7.4 / 8.5 / 7.1 | 7 / 4 / 13 | **2 / 1 / 4** | 2-1 / 1-0 / 3-3 |

- 32 candidates per tick (the R5b scaffold plus the CEM pool).
- Uncommitted ticks (0.7-1.4%) sample from a uniform softmax (normalised entropy 0.9999).
- **Consumption is the scarce event:** 0-7 per 600 steps in every arm.

### 4.2 What the candidates would credit: channel spreads and votes at the chosen candidate (T2; s42 / s43 / s44)

| channel | weighted cross-candidate std | mean abs vote (raw units) |
|---|---|---|
| harm_eval | 0.0064 / 0.0182 / 0.0304 | 0.0088 / 0.0138 / 0.0613 |
| benefit_eval | 0.0057 / 0.0216 / 0.0577 | 0.0052 / 0.0167 / 0.1327 |
| residue | 0.0012 / 0.0002 / 0.0041 | 0.0025 / 0.0002 / 0.0126 |
| F | 0.0008 / 0.0010 / 0.0028 | 0.0008 / 0.0006 / 0.0050 |

The evaluator terms out-spread residue about 5-95x. This re-measures ADDENDUM 2's closed-loop domination at the tick level.

### 4.3 Direction previews on the agent's own T2 stream (open loop, G-contact; what each rule WOULD do)

| rule | harm | benefit | residue | F |
|---|---|---|---|---|
| M2 vote-regression t (no fixed effects) | **+1.65 / +1.59 / +2.44** | +0.46 / -1.76 / -2.13 | +1.39 / -0.98 / +2.11 | +0.10 / +2.27 / -0.05 |
| M1 raw, mean drift per contact event | -0.33 / +0.29 / +0.67 | **-0.37 / -0.43 / -0.58** | -0.19 / -0.57 / +0.58 | -0.16 / +0.57 / -0.21 |
| M3 (ARC-108 constants) open-loop z | +4.11 / +2.27 / -2.51 | +3.70 / +0.78 / +2.48 | +3.59 / -2.09 / -1.01 | +3.41 / -0.37 / +0.69 |

- **Every rule that looks at its own T2 stream says to trust harm_eval more and benefit_eval less** (M2 on harm 3/3 seeds and benefit 2/3; M1 raw on benefit 3/3). That is exactly the correction T2 needs: its harm rise is the benefit channel overriding harm (s44: harm votes for the pick on only 14% of ticks).
- M3 at ARC-108 constants disagrees on benefit (positive on 3/3). Section 3a traced that to its asymmetry bias.
- **The candidates therefore genuinely diverge on this stream.** That is the point of the battery.

### 4.4 Can a weight move within budget? (T2 regime)

- **Harm channel: FEASIBLE on-policy.**
  - M2 needs 84-197 committed ticks for |t| = 2, about **400-930 env steps**.
  - M1c at eta 0.05 needs about 23-46 contact events to move theta by ln 2, about **600-3,000 steps** (s43 slowest, at 7 contact ticks per 600). This is estimated from M1 raw's drift magnitudes of 0.3-0.6 per event; M1c's own drift was not computed.
  - M3n (normalised votes, eta 0.01) needs roughly 25-250 events. That is a D0 estimate from the |delta| (0.3-0.6) and eligibility (1-5) magnitudes seen here, not measured.
- **M3 at the literal ARC-108 constants: INFEASIBLE.** theta moved at most 0.018 in 600 steps (typically 1e-5 to 2e-3). Moving it by ln 2 would take more than 20,000 steps. Hence M3n.
- **Benefit channel at CONSUMPTION grain: INFEASIBLE on-policy.**
  - The pooled off-policy evidence (4.5) reaches t = 1.6 at 132 consumptions.
  - T2's own policy yields 1-7 consumptions per 600 steps, so reaching |t| = 2 on-policy would take about 20,000-100,000 steps.
  - Benefit calibration is feasible only via (a) G-all, where approach steps number 56-98 per 600 but K5 exposure applies, or (b) an off-policy or exploration fraction feeding the weight learner.
- **The shuffled arm cannot be judged by raw end weights.** T3 yields 1-4 contact ticks per 600, so any rule barely moves there. "The shuffled heads got lower weights" could be won by INACTION. P2 must therefore be judged event-normalised against the M4 null band (V3 below). This is a negative-instrument trap: a comparison whose numerator and denominator come from the same starved search.

### 4.5 Does a channel's vote carry the grounded consequence at all? (off-policy M2b; action fixed effects; 1,500 random steps per seed; t in the valid direction)

| evaluator set | harm vote -> fewer harm contacts, s42 / s43 / s44 (pooled z) | benefit vote -> consumptions (pooled z) |
|---|---|---|
| trained (T2 heads) | +2.51 / +0.85 / +2.00 (**+3.09**) | -0.17 / +2.02 / +0.99 (**+1.64**) |
| shuffled (T3 heads) | +1.90 / -0.74 / -2.22 (-0.61) | +0.09 / -1.07 / -0.16 (-0.66) |
| untrained (T1 heads) | +0.23 / -0.74 / +3.42 (+1.68) | -0.43 / +1.74 / +0.09 (+0.81) |

- Totals: 375 harm contacts and 132 consumptions over 4,500 steps.
- **Pooled across seeds, the grounded signal separates trained from shuffled heads on both channels.** That is the programme-level falsifier's premise: the feature end is not empty.
- **Per seed, the noise floor is |t| of about 2-3.4.** The untrained harm head reaches +3.42 on s44. So any P2 decision on a single seed is unsafe, and the battery needs pooled seeds plus a permutation null.
- **The votes are computed on E2-PREDICTED depth-2 states,** which barely separate the one action that enters a hazard or resource cell (ADDENDUM 1-2's action-blindness). That caps how much consequence any valuation rule can attribute to a channel: grounded valuation can only calibrate what the features already carry.

## 5. The adjudication battery (design; not run)

**Mechanics.**
- Every candidate runs INSIDE THE PROBE. A wrapper on `E3.select` applies the pending weight update to the four `E3Config` weight fields BEFORE the tick's scoring. It then records the new tick's votes, and accumulates the window outcome from the received scalar until the next tick.
- Nothing is written to ree_core. OFF (M0) is bit-identical by construction.
- **Learning phase:** 3,000 closed-loop steps with the rule online. Then the weights are frozen and evaluated for 600 steps in a fresh env of the primary ecology (seed s+500), and for 600 steps in the ALTERED ecology (3 hazards / 2 resources, seed s+1000).

**Arms per seed.** Head sets × rules:
- Head sets: {trained, shuffled, untrained}.
- Rules: {M0, M1c, M2, M3n, M4 matched to each of M1c/M2/M3n}.
- Signal: G-contact for all of those. M2 and M3n also run on G-all, to expose K5.
- Positive control: **M1 raw** on trained heads.
- **P3 causal re-runs, for survivors only:** frozen-learned weights, default weights, and a random weight vector with the same log-norm displacement, each evaluated in both ecologies.

**Hard validity conditions.** These are non-compensable: any breach voids a PASS, whatever the aggregate.
- **V1, no immobility or affordance removal.**
  - Evaluation action entropy must be at least 0.5x T1's on the same seed.
  - All 5 action classes must be executed at least once.
  - Consumptions must not fall below T1's.
  - A harm reduction bought by freezing (the s43 signature, entropy 0.05) is a FAIL.
- **V2, scoring independence.** Success is scored ONLY on env-internal transition types (harm contacts, consumptions), and no candidate ever reads them. Approach steps are reported but never count as benefit success (K5).
- **V3, event-normalised validity.**
  - For each channel, weight displacement per grounded event is compared with M4's null distribution at the SAME event count.
  - The shuffled and untrained channels must be at or below the null median.
  - The trained harm channel must be above the null 95th percentile, and trained benefit likewise if the arm has at least 30 consumption events. Otherwise benefit is declared under-powered, not passed.
  - Significance comes from a within-run permutation of R_t across ticks (at least 200 permutations), pooled over seeds.
- **V4, harm floor (K3).**
  - theta_harm at its floor on more than 25% of ticks is a FAIL, and so is theta_harm monotone-down while contacts rise.
  - **The M1 raw positive control MUST trigger this detector. If it does not, the battery itself is invalid** (a negative instrument must prove it can fire).
- **V5, transfer (K6).** Frozen weights must keep P1 versus T1 in the altered ecology. The T1/T2 baselines are measured fresh there, because none exist yet.
- **V6, canary.** M0 arms must reproduce `TB_s*.json` T2/T3 bit-for-bit, as the tap did here.
- **V7.** The residue weight must not hit its floor. Residue is the harm memory FULL relies on.

**Adversarial checks** (frontier doc Step 5, mapped):

| check | where it sits in the battery |
|---|---|
| proxy reward / metric gaming | G-all vs G-contact (K5), and V2 |
| punishment avoidance / freezing / self-erasure | V1 |
| removing the unethical affordance | V1; the action set and candidate set cannot be written by contract |
| channel presence without content | shuffled and untrained heads, V3 |
| hard-coded lookup | only 4 scalars are writable |
| train/test memorisation | V5 |
| seed luck | pooled seeds plus the permutation null |
| common-mode credit | M1 raw control plus M4 |

**Where the candidates are predicted to disagree** (the arms exist to test these predictions):

| setting | M1c | M2 | M3n | M1 raw |
|---|---|---|---|---|
| trained heads, harm-dominated stream | harm up, benefit down | harm up, benefit down (on-policy t) | harm and benefit weights set by delayed contacts (sign open) | ALL down, so K3 fires |
| shuffled heads | actively down, but only if events arrive | stays at default (t about 0) | random-walks, cannot beat M4 | follows the base rate |

- Across all candidates, benefit at consumption grain is under-powered on-policy.
- M3n alone credits contacts 3-8 steps after the pick across tick boundaries.

**Pre-flight of the battery's own premises** (read-only, this session):

| quantity the battery reads | producer (file:line @ `44c55300ca`) | grade |
|---|---|---|
| received scalar r_t | `experiments/_harness.py:354` (env.step), fed to `update_residue` `:361` | GREEN (measured) |
| contact vs proximity by magnitude | `causal_grid_world.py:273, 275, 339-340`; 9,000 labelled steps | GREEN (measured, clean) |
| per-candidate channel terms | `e3_selector.py:1821-1834`, `:3953-3957` (decomp) | GREEN (inert on 9/9 arms) |
| selected index / committed flag | `SelectionResult`, `e3_selector.py:113-133`; argmin `:4509` | GREEN (98.6-99.3% committed) |
| writable weights F / harm / residue / benefit | read per call at `e3_selector.py:1710-1732`, `:1737-1751` | GREEN. The benefit gate needs `benefit_weight > 0` (`:1738`), which the x4 bound keeps. |
| lambda_eff = lambda_ethical | `config.py:1376` `affective_harm_scale` 0.0 | GREEN |
| goal channel | `e3_selector.py:1757` (goal_state inactive) | **RED**: dead in this regime, so excluded |
| benefit gate native | `e3_selector.py:695`, `:1737-1739`; gate_n 737-1136 | GREEN |
| altered ecology | `CausalGridWorldV2(num_hazards=3, num_resources=2)`: obs dims 250/12/5, identical | AMBER: dims verified; no baselines yet; the encoder was trained on regime B |
| on-policy event counts | section 4.1 | AMBER: harm is adequate; benefit consumption and shuffled-arm counts are too low. Mitigated by V3 and the under-powered declaration. |
| feature informativeness | section 4.5 | AMBER: pooled only; E2 action-blindness caps it |

**Budget.**
- Per seed, the full grid is about 3 head sets × 8 rule-signal arms + 1 control + P3 re-runs, about 30 arms × 4,200 steps, about 60 min of CPU.
- 5 seeds (42-46) come to about 5 CPU-hours. **That is a cloud run.** COMMON rule 4 caps a Mac probe at about 10 min.
- **A Mac-sized smoke fits:** 1 seed, trained heads, M0 / M2 / M4, L = 1,500, about 6-8 min. It proves the in-probe weight writer, the M0 bit-identity and the K3 detector wiring.

## 6. Recommendation (a proposal for the user; not a decision)

1. **Prototype M2 first:** reward regression on channel votes, action fixed effects, t-gated. Run it with its matched M4 null and the M1-raw K3 positive control, on G-contact. Three reasons:
   - It is the only candidate that is free of common-mode credit by construction.
   - It has a principled null behaviour on uninformative channels.
   - Its on-policy direction preview (harm t +1.6 to +2.4 on 3/3 T2 seeds) matches the calibration T2 needs, and it is feasible at harm grain within about 400-930 steps.
2. **Run M1c and M3n alongside it,** as the deliberately different rivals.
3. **Where to run it:**
   - **Mac smoke first** (1 seed, about 8 min). It checks the weight writer, M0's bit-identity and that the K3 control fires.
   - **Then the full battery on a cloud worker** (about 5 CPU-hours; about 1 h wall time if parallel per seed).
4. **Honest expectation.**
   - The most likely first result is a HARM-vs-BENEFIT TRADE-OFF calibration: harm and residue up relative to benefit, recovering T1's harm level while keeping part of T2's approach gain.
   - It is NOT expected to learn benefit VALIDITY. At consumption grain the grounded signal is data-starved on-policy (4.4).
   - Learning benefit validity needs either an exploration or random fraction feeding the weight learner off-policy (M2b pooled t = 1.6 at 4,500 steps), or the G-all signal under the K5 guard.
   - That is a named sub-edge: **benefit consumption coverage**. ADDENDUM 1 only partly closed it, since its new positives are approach steps.
5. **The smallest honest build, IF a candidate survives the battery.** This is `complicated (buildable)` once the battery picks the rule. Choosing the rule is `complex (probe-gated)` today.
   - A default-OFF E3Config flag (for example `use_grounded_channel_valuation`).
   - About 60-100 lines in E3:
     - a per-tick vote capture reusing the existing score-decomposition terms;
     - an outcome accumulator fed by the harm_signal the agent already receives through `update_residue`;
     - the surviving rule, writing ONLY the four weight fields in bounded log space with the harm floor.
   - Contracts: OFF bit-identity; bounds and floor enforced; no read of env info or transition types; the M1-raw K3 detector as a regression test.
   - Validation then goes through `/queue-experiment`.
6. **Named options for the user:**
   - **(A)** Mac smoke, then the cloud battery. **Recommended.**
   - **(B)** Mac smoke only, then decide.
   - **(C)** Raise benefit consumption coverage first (an exploration fraction), since benefit validity is data-starved. The battery would then learn both trade-off and validity.
   - **(D)** Park the edge. GFLAG-0487 then stays open with this record as its design.

## Done / not done

- **DONE:**
  - Prior-art scope and Class S classification.
  - Pre-registered phenomenon, falsifiers K1-K6 and contract.
  - Four candidates plus two controls, amended after the D1 diagnosis.
  - Feasibility in 9 closed-loop arms (bit-identical canaries) and 3 off-policy streams.
  - The battery design, with a graded pre-flight.
- **NOT DONE:**
  - No candidate was run closed-loop (D2/D3 is the battery's job).
  - No permutation null has been computed yet; the off-policy t values are parametric.
  - No altered-ecology baselines.
  - Seeds beyond 42-44.
  - M3n's step-size estimate is D0.
- **Limits:**
  - Open-loop previews ignore feedback: as weights change, event rates change. A harm-down calibration slows its own learning, which is self-limiting.
  - 600-step closed-loop streams.
  - The off-policy votes use one-hot scaffold rollouts from the COV head, not the agent's CEM pool.
  - Heads were trained on argmax one-hots (inherited).

## ADDENDUM 1 (2026-09-24T22:25Z, session `bt0924-valuation-b`): Mac smoke -- a HARNESS VALIDATION, not evidence for any candidate

- **Scope.** The orchestrator, under the user's standing delegation, authorised the Mac smoke ONLY. The cloud battery is not authorised; option A vs C is the user's call.
- **Evidence domain.** One seed, D1-D2 at most. Nothing below counts for or against M2, M1 or M4 as mechanisms.
- **Code:** ree-v3 `44c55300ca`, unchanged, in a private detached worktree.
- **Probe:** `probes/valuation/valuation_smoke_probe.py --seed 42 --steps 1500`, with results in `probes/valuation/results/SMOKE_s42.json`. Wall time 514 s, of which the preamble took 261 s under laptop contention.
- **Regime:** T2 exactly as in `e3_evaluation_edge_test` ADDENDUM 1: tie-break ON, R5b scaffold, COV head, R2 depth 2, trained evaluators, and the native benefit gate at 1136.
- **Arms:** trained heads only, with a fresh agent per arm and 1,500 learning steps each.
  - **M0:** frozen weights.
  - **M1RAW:** the raw sign rule at eta 0.05, as the K3 positive control.
  - **M2:** regression of the contact outcome on channel votes, with action-class fixed effects. theta = clip(0.35 t), once at least 20 committed windows exist.
  - **M4:** a random walk. Its per-channel increment SD is matched to M2's realised per-tick change in theta (F 0.031, harm 0.053, residue 0.058, benefit 0.042), and its noise seed is independent.
  - All rules use the G-contact signal (|r| > 0.1, from the received scalar only).
- **Why seed 42.** It was chosen and written into the probe docstring before the run, because it is the harm-heavy stream on which section 4.3 predicted that M1RAW drives harm down.
- **Pre-registration.** The detector thresholds and M2's predicted direction were fixed in the docstring before the run.

### Pass conditions

**(1) The weight writer changes E3's score composition: PASS.**
- On M2's first update tick (env step 69), theta = [F +0.191, harm +0.739, residue +0.454, benefit -0.238]. The writer set the weights to w = [1.211, 2.093, 0.787, 0.788]; the defaults are [1.0, 1.0, 0.5, 1.0].
- Before the live select, the same 32 candidates were re-scored under DEFAULT weights on a deep copy of E3, with RNG state restored.
- **Chosen candidate (index 3), weighted F / harm / residue / benefit terms:**
  - default: 0.0075 / 1.036 / 1.222 / 1.255;
  - live: 0.0091 / 2.169 / 1.924 / 0.990.
- **The per-channel live/default ratio (median over candidates) is 1.2105 / 2.0935 / 1.5749 / 0.7882.** That equals w_now / w_default to 4 decimals on every channel.
- M1RAW's first update (step 22: harm +0.05, residue -0.05) shows the same exact match, at 1.0513 / 0.9512.
- **Caveat:** the sum F + harm + residue - benefit picked the same candidate under both weight sets on both demo ticks. So this shows the composition changes, not a pick flip on those ticks. Behavioural reach is shown only indirectly, by the M1RAW, M2 and M4 counts diverging from M0 after their first updates.

**(2) M0 frozen reproduces T2 bit-identically: PASS.**
- M0's first 600 steps give reward -2.0661 per 100 steps, 39 harm contacts, 25 hazard-proximity steps, 98 benefit-approach steps and 7 consumptions.
- That is identical to `TB_s42.json` T2. The weight writer (which rewrites the defaults every tick) plus the tap is inert when frozen.

**(3) The harm-floor detector fires on the raw-rule control: FAIL.** **Per the design, the battery is therefore invalid as designed.**
- **What M1RAW did.** It drove theta_harm to the hard floor: -0.70 by step 329, -1.15 by step 690, and **-1.386 = -ln 4 by the end**.
  - 82% of its 44 nonzero harm updates were negative.
  - It also dragged every other channel down: F -1.0, residue -1.29, benefit -1.386.
  - That is exactly the common-mode reward-hacking signature section 3a predicted.
- **Why the detector stayed silent.** Both of its clauses missed:
  - the harm weight sat at the floor on only 14% of ticks, because it arrived late, below the 25% threshold;
  - the "harm contacts rise" conjunct was false: contacts fell from 55 in the first half to 24 in the second.
- **That second conjunct is the design error.** Contacts fall in the second half in EVERY arm (M0 48 -> 33, M2 44 -> 25, M4 48 -> 6), because residue accumulates within a run. So "contacts rise" can almost never be true inside a 1,500-step learning phase, and it vetoes the detector.
- **Candidate repair, NOT validated.** It is fitted post hoc on this one seed and needs fresh seeds before use:
  - drop the contacts conjunct;
  - FIRE if theta_harm reaches the floor at ANY tick, OR if the final theta_harm is below -0.5 with more than 75% of nonzero harm updates negative.
  - On this smoke it would fire on M1RAW (floor reached, 82% negative) and on neither M4 (final -0.72, but only 53% negative) nor M2 (-0.16, 52%).
  - **M4's harm weight reached -1.10 by random drift alone**, so any displacement-only threshold would false-alarm on the null. The negative-update fraction is what separates them here, on one seed.

**(4) M2 and M4 weight trajectories: REPORTED. The direction of M2's harm weight was NOT confirmed.**

| env step | M2 theta F / harm / residue / benefit | M4 theta F / harm / residue / benefit |
|---|---|---|
| about 69 (M2's first update) | +0.19 / **+0.74** / +0.45 / -0.24 | -- |
| about 280-300 | +0.46 / +0.13 / +0.47 / -0.17 | -0.27 / -0.15 / +0.59 / -0.41 |
| about 630 | +0.62 / +0.17 / +0.55 / -0.44 | -0.22 / -0.64 / +1.06 / -0.11 |
| about 1,000-1,070 | +1.03 / +0.03 / +1.09 / -0.58 | -0.03 / -0.98 / +0.94 / -0.14 |
| end (1,492) | +1.17 / **-0.16** / +1.06 / -0.51 | +0.08 / -0.72 / +0.49 / -0.21 |

- **The prediction was theta_harm UP.** M2's harm weight went up first (+0.74 at its first estimate, then +0.13 to +0.17 through step 630), then decayed to about 0 and ended at **-0.16**.
- **So the direction is not confirmed by the end.** Over the whole run it spanned -0.20 to +0.74, inside M4's pure-noise band of -1.10 to +0.16.
- M2's clearest movements were residue UP (+1.06) and benefit DOWN (-0.51), which fits "trust the residue harm memory, distrust the benefit head". F also rose (+1.17), which no prior measurement predicted.
- **Mechanism note.** As built, M2 re-sets theta from the CURRENT t-statistic on each tick; it does not integrate. So its weights track a noisy running estimate, and one seed cannot separate that noise from signal. This is the design as stated in section 3, now seen to be jumpy. Integrating or shrinking the estimate is a design option for the battery, not a result.

**Behaviour, reported but NOT evidence** (all 1,500 steps; harm contacts / consumptions / approach steps / reward per 100):

| arm | harm contacts | consumptions | approach steps | reward / 100 |
|---|---|---|---|---|
| M0 | 81 | 11 | 186 | -1.72 |
| M1RAW | 79 | 10 | 188 | -1.77 |
| M2 | 69 | 8 | 155 | -1.52 |
| M4 | 54 | 8 | 139 | -1.14 |

**The random-drift null has the fewest harm contacts.** That is why a single-seed behavioural difference means nothing here, and why V3's event-normalised null comparison is mandatory.

### What this changes for the battery (for the user's A vs C decision)

1. **The harness works.** The in-probe weight writer is exact, frozen weights are bit-identical, and the per-tick trajectories are logged. The mechanical parts of the battery are validated on one seed.
2. **The K3 / V4 detector is broken as designed and must be repaired before any battery run.**
   - Replace it with the trajectory-only rule above, or a stronger one.
   - Then **re-validate it on at least 2 fresh seeds**, requiring it to fire on M1RAW and stay silent on M4.
   - Until then, "no reward hacking" cannot be certified. The negative-instrument rule applies: this detector had exactly the silent false negative the positive control exists to catch.
3. **M2 as specified is jumpy**, because it re-sets from a running t. A shrunk or integrated variant should be pre-registered before the battery, not tuned on its results.
4. **Nothing here favours option A or option C.** The smoke says nothing about benefit coverage.

**Stopped here, as instructed.** No further arms or seeds.
