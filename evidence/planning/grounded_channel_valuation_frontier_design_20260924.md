# Grounded main-channel valuation: frontier design and feasibility (E3 channel worth learned from experienced consequence)

- **STATUS: INTERIM (steps 1-3 of 6), 2026-09-24.** Steps 4-6 (feasibility measurement, adjudication battery, recommendation) follow in the FINAL version of this file.
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
- **P-c. E3 has two choice rules, and a channel weight only has authority on one of them.**
  - A **committed** tick takes the argmin (`:4507`).
  - An **uncommitted** tick samples `softmax(-scores / T)` (`:3976`, `:4531`) with `T = 1.0`, passed by the harness (`_harness.py`, `select_action(..., temperature=1.0)`).
  - Score spreads in this regime are about 0.001-0.05 (ADDENDUM 1-2). At T = 1, uncommitted sampling is therefore close to uniform, and channel weights barely move it.
  - **So any valuation rule acts mainly through committed ticks.** Credit assignment has to know which kind of tick it is crediting. The committed fraction is measured in step 4.
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
  - A magnitude threshold on the received scalar is therefore a legitimate contact-only signal. This is confirmed empirically in step 4.

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
