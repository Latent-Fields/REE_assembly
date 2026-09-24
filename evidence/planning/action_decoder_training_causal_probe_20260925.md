# Does training the action_object_decoder break the proposal collapse? (pre-registered causal probe)

- **STATUS: FINAL.** 2026-09-24T23:38:47Z. The interim record (seeds 52-53) is commit `12ed412fd07`; the seed 52-53 numbers are unchanged here.
- Session `bt0925-decoder-probe` (Worker J, breakthrough integration pass `orchestrate-20260924-breakthrough`), chip_ref `chip-20260925-decoder-training-causal-probe`. Probe only: nothing lands in ree_core, nothing queued, no registry touched.
- Code under test: ree-v3 `origin/main` @ `863d23d65a` (private detached worktree; same sha as Worker I's replication, whose record confirms no diff against ADDENDUM 3's `44c55300ca` on hippocampal/E3/env/harness files). All file:line citations are against `863d23d65a`.
- Probe: `.scratch/breakthrough-20260924/decoderprobe/decoder_probe.py` (in the umbrella checkout, not committed).
  - A copy of ADDENDUM 3's `probes/rollout/partitioned_repair_probe.py`, with everything through the CHOICE block unchanged (same P0 warmup, replay, heads, choice cells).
  - Plus: the decoder-training step, the three pre-registered arms, the outcome decomposition and the discrimination measure.
  - Summarizer `summarize_dec.py`; raw JSON `results/DEC_s{52..56}.json`; per-seed class sidecars `results/DEC_s*_CLASS.json`, each written when that seed's NATIVE arm finished.
  - Post-hoc diagnostic `cem_trace_diag.py` -> `results/POSTHOC_cemtrace_s{52..56}.json`.
- Regime B: CausalGridWorldV2 8x8, 2 hazards, 3 resources, `world_dim` 32 (the deployed value), `action_dim` 5, SD-070 P0 encoder (20x50, preservation 1000). Mac CPU, `torch.set_num_threads(2)`, ~2.7-4.3 min per seed.
- **Evidence domains reached.** D2 for P (an intervention on the decoder changes the native CEM pool). D2/D3 for C (the executed-action distribution, and E2 trained on the resulting replay). D3 for the outcome (descriptive only).

## Verdicts

- **Criterion P: FAIL.** DEC varies in 4/5 seeds (passes its half). But NATIVE varies in 2/5 and DEC-SHUF in 4/5, where both needed <= 1/5.
- **Criterion C: FAIL.** Every class at >= 5% under DEC: 0/5. DEC-replay head beats NATIVE-replay head at h = 1: 3/5 (needed 4/5).
- **Outcome (descriptive):** undirected noise is flagged on 4/4 benign seeds (52, 53, 54, 56). On the one hazard-trapped seed (55), DEC is marginally better than NATIVE on reward, with no change in true contacts.
- **Harness checks pass on all 5 seeds.** The DEC decoder receives gradient on every parameter and fits the inverse with 1.000 held-out accuracy. DEC-SHUF stays at chance. So these are results, not harness failures.

**Plain reading.**
- The untrained decoder IS what pins the CEM pool to one bias class: every decoder change moves the pool.
- But an *honest* inverse does no better than a *shuffled* one on proposal state-dependence.
- Neither gives the agent balanced action coverage.
- The reason is visible in the post-hoc trace: in the native CEM loop, an inverse-fit decoder's raw logits are fed back as action vectors and the O -> action -> O refit diverges (decoded norm 50 -> ~150-210 -> ~370-1080 over three CEM iterations, 5/5 seeds).
- **The decoder is a real defect but not the causal root of the collapse on its own. It is one of three coupled interface defects on this edge:**
  1. an untrained decoder;
  2. unbounded decoder output used as the rollout's action vector;
  3. iteration-0 sampling at unit scale in O, ~13x outside the encoder's image.

## PRE-REGISTRATION (verbatim from the brief, fixed before any run)

- Seeds: 52, 53, 54, 55, 56 (fresh). Record each seed's NATIVE early-termination rate over the first 600 steps and classify it hazard-trapped (>= 10 early terminations) or benign BEFORE looking at the other arms; report results stratified.
- Arms: NATIVE; DEC (trained decoder); DEC-SHUF (same objective, same data, action labels permuted across timesteps -- same class marginals). R5b/R2/tiebreak OFF in all arms (native regime). 600 closed-loop steps after the same warmup.
- Criterion P (proposal): the CEM pool's majority first-action class varies across 20 probe states in >= 4/5 seeds under DEC, AND in <= 1/5 under both NATIVE and DEC-SHUF.
- Criterion C (coverage): under DEC, every action class makes up >= 5% of executed actions in >= 4/5 seeds, AND E2 world-head action discrimination (the addendum-1 metric, trained on the agent's own DEC-arm replay, same budget) beats the NATIVE-replay head on >= 4/5 seeds.
- Outcome (reported, NO success criterion -- the pre-registered expectation is that without grounded valuation more diverse proposals may be undirected): env reward per 100 steps, TRUE harm contacts and hazard-proximity steps decomposed from the start, consumptions, early terminations, action entropy. Flag undirected noise explicitly.
- No additional arms, no tuning, no re-running seeds except a clearly-labelled post-hoc diagnostic whose numbers never replace the pre-registered ones.

No seed was re-run. No arm was added. The only runs outside the five pre-registered ones are:
- one harness smoke on seed 99 (60 steps; used only to check that the script runs; `results/SMOKE_s99.json`);
- the post-hoc CEM trace below, which re-uses saved states and does not re-run any arm.

## Decoder objective (my choice, stated in the probe's docstring before any run)

- **Trace candidate 1, the smallest one.** `CE(action_object_decoder(o), a)`, with `o = E2.action_object(z_t, onehot(a_t), action_bias)` computed under `no_grad`. The encoder, E1 and E2 are frozen, so only the decoder moves. It gets its OWN Adam optimizer (lr 1e-3, batch 64, 2000 steps, 80/20 held-out split, fit threshold >= 0.5 held-out).
- **Why this objective.** The CEM samples in O, decodes with `action_object_decoder` (`ree_core/hippocampal/module.py:178-182`, via `_decode_action_objects` at `:2280`), then re-encodes the rolled-out actions with `E2.action_object` (`ree_core/predictors/e2_fast.py:660-691`, called inside `rollout_with_world` at `:813`) and refits in that encoder's image (`module.py:2476`). A decoder that inverts the encoder is exactly what makes decode(refit mean) mean "the action the elites took".
- **Cue bias.** `action_bias` is the E1 cue bias the live agent passes (`agent.py:6421-6426`, `:6601`). E1 has no `world_query_proj` in this config, so it is None; measured `bias_present: false` on every seed.
- **Data.** The harness's existing post-P0 uniform-random-policy episodes (`rnd`: RandomPolicy, the SD-070 warmup policy, encoded by the post-warmup encoder; 1,650-1,690 steps, ~uniform over 5 classes). These are the agent's own executed actions, with no reward or env internals, so no privileged information.
  - The agent's native waking replay was NOT used. ADDENDUM 2 showed it lacks 1-2 classes entirely (reconfirmed here: e.g. s56 replay 1,427 of 1,492 in class 0), so a decoder trained on it could not emit them: failure by construction, not a test.
- **DEC-SHUF.** Identical inputs, optimizer and budget; targets permuted across timesteps with a fixed generator.
- **Arm setup.** Each arm is a fresh agent from the same seed, with the master's encoder and own-replay head A loaded (ADDENDUM 3's native regime; COV/R5b/R2 off; tiebreak at the env default). DEC loads the trained decoder, whose init is byte-identical to NATIVE's because the seed is the same. The in-run check `decoder_changed_during_run` is false on every arm.
- **Measures.**
  - P: the harness's own `m4_proposal` over 20 states of the arm's own log; "varies" = >= 2 distinct majority classes.
  - C-coverage: min class share of executed actions (argmax).
  - C-discrimination: `encoding_vs_objective_probe.evaluate` (the ADDENDUM 1 metric). Executed action closest at **h = 1 is the comparison, fixed before running**; h = 3 and 5 are reported. Heads are trained per arm by `balanced_replay_probe.train_arm` (3000 updates, the ADDENDUM 2/3 budget) from the same init on that arm's 560-597 closed-loop transitions, and evaluated on one held-out uniform-random test set per seed (`build_B(seed+23)`, 1,500 steps, 300 starts).
  - Outcomes: split by `info["transition_type"]` from the start, on every arm and seed. True contacts = `{agent_caused_hazard, env_caused_hazard, env_caused_multisource}` (Worker F); proximity = `hazard_approach`; consumption = `resource`. Early termination = an episode that ends before 200 steps.

## Harness checks

| seed | DEC grad non-None, all decoder params (step 0) | DEC fit held-out | DEC-SHUF fit held-out vs its targets / vs true action | O norm | DEC logit norm on O | DEC-SHUF logit norm |
|---|---|---|---|---|---|---|
| 52 | yes | **1.000** | 0.210 / 0.189 | 0.363 | 6.25 | 0.23 |
| 53 | yes | **1.000** | 0.225 / 0.180 | 0.293 | 8.00 | 0.36 |
| 54 | yes | **1.000** | 0.198 / 0.224 | 0.364 | 8.49 | 0.31 |
| 55 | yes | **1.000** | 0.165 / 0.218 | 0.314 | 8.24 | 0.18 |
| 56 | yes | **1.000** | 0.227 / 0.171 | 0.357 | 7.81 | 0.24 |

- The encoder->decoder inverse is trivially learnable: per-class held-out accuracy is 1.00 for every class on every seed.
- The dead-optimizer pattern (trace Q1) is absent here: DEC's parameter delta norm is ~25 against ~5 for DEC-SHUF.

## Seed classification (from NATIVE only, written to a sidecar before the other arms were read)

| seed | NATIVE early terminations in 600 steps | class |
|---|---|---|
| 52 | 0 | benign |
| 53 | 0 | benign |
| 54 | 0 | benign |
| 55 | **15** | **hazard-trapped** |
| 56 | 2 | benign |

## Per-seed results, stratified (600 steps per arm)

| stratum | seed | arm | reward/100 | TRUE contacts/100 | hazard-prox/100 | consumptions/100 | early terms | action entropy | majority share | min class share | executed-action norm | proposal majority across 20 states | P varies |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| benign | 52 | NATIVE | +0.005 | 0.00 | 1.8 | 0.17 | 0 | 0.696 | 0.56 | 0.000 | 0.25 | {0:12, 2:8} | yes |
| benign | 52 | DEC | -0.814 | 1.17 | 12.3 | 0.67 | 4 | 0.861 | 0.71 | 0.007 | **321** | {1:12, 2:4, 3:4} | yes |
| benign | 52 | DEC-SHUF | -1.109 | 2.00 | 12.3 | 0.50 | 6 | 0.976 | 0.55 | 0.008 | 0.82 | {0:3, 2:17} | yes |
| benign | 53 | NATIVE | -0.412 | 0.50 | 5.3 | 0.17 | 0 | 0.693 | 0.72 | 0.000 | 0.26 | {3:20} | no |
| benign | 53 | DEC | -0.768 | 1.33 | 8.5 | 0.50 | 3 | 0.891 | 0.60 | 0.010 | **490** | {0:1, 1:7, 3:12} | yes |
| benign | 53 | DEC-SHUF | -2.095 | 3.17 | 27.7 | 1.17 | 11 | 1.259 | 0.49 | 0.018 | 0.66 | {1:18, 3:1, 4:1} | yes |
| benign | 54 | NATIVE | +0.037 | 0.00 | 0.7 | 0.17 | 0 | 0.000 | 1.00 | 0.000 | 0.29 | {2:20} | no |
| benign | 54 | DEC | -2.392 | 4.00 | 26.3 | 1.17 | 13 | 0.852 | 0.61 | 0.003 | **1200** | {0:10, 1:10} | yes |
| benign | 54 | DEC-SHUF | -1.449 | 2.17 | 19.0 | 0.83 | 8 | 1.094 | 0.61 | 0.015 | 0.77 | {3:20} | no |
| benign | 56 | NATIVE | -0.505 | 1.00 | 5.3 | 0.33 | 2 | 0.202 | 0.95 | 0.000 | 0.97 | {4:20} | no |
| benign | 56 | DEC | -0.761 | 1.33 | 9.2 | 0.33 | 4 | 0.884 | 0.57 | 0.007 | **567** | {3:20} | no |
| benign | 56 | DEC-SHUF | -1.658 | 2.33 | 20.5 | 0.67 | 9 | 1.218 | 0.42 | 0.005 | 0.70 | {1:1, 2:13, 3:6} | yes |
| trapped | 55 | NATIVE | -2.554 | 3.67 | 34.5 | 1.67 | 15 | 1.041 | 0.47 | 0.000 | 0.17 | {2:10, 3:10} | yes |
| trapped | 55 | DEC | -2.320 | 3.83 | 22.0 | 0.50 | 12 | 0.741 | 0.80 | 0.005 | **818** | {0:19, 4:1} | yes |
| trapped | 55 | DEC-SHUF | -7.688 | 16.00 | 46.5 | 1.67 | 39 | 1.182 | 0.48 | 0.000 | 0.40 | {2:14, 4:6} | yes |

E2 world-head action discrimination (executed-action-closest at h = 1 / 3 / 5, chance 0.20; k = steps beating persistence, H = 5; each head trained on that arm's own closed-loop replay, 3000 updates, same init; one held-out uniform-random test set per seed):

| seed | NATIVE-replay head (replay classes) | DEC-replay head | DEC-SHUF-replay head | DEC > NATIVE at h=1? |
|---|---|---|---|---|
| 52 | 0.167 / 0.193 / 0.167, k 0 ({0,1,2}) | 0.283 / 0.247 / 0.263, k 5 | 0.220 / 0.220 / 0.207, k 0 | yes |
| 53 | 0.207 / 0.220 / 0.257, k 0 ({0,1,3,4}) | 0.277 / 0.260 / 0.200, k 5 | 0.327 / 0.337 / 0.333, k 5 | yes |
| 54 | 0.237 / 0.237 / 0.237, k 0 ({2} only) | 0.337 / 0.330 / 0.310, k 5 | 0.283 / 0.303 / 0.257, k 5 | yes |
| 55 (trapped) | 0.323 / 0.317 / 0.257, k 0 ({1,2,3,4}) | 0.297 / 0.317 / 0.293, k 5 | 0.297 / 0.250 / 0.273, k 1 | **no** |
| 56 | 0.280 / 0.203 / 0.203, k 0 ({0,1,2,4}) | 0.243 / 0.243 / 0.240, k 2 | 0.360 / 0.317 / 0.313, k 5 | **no** |

## Criterion P: FAIL

| | seeds where the proposal majority class varies across 20 states | requirement | met? |
|---|---|---|---|
| DEC | 52, 53, 54, 55 = **4/5** | >= 4/5 | yes |
| NATIVE | 52, 55 = **2/5** | <= 1/5 | **no** |
| DEC-SHUF | 52, 53, 55, 56 = **4/5** | <= 1/5 | **no** |

- The discriminating half fails on the control. **A decoder trained on permuted labels makes the proposal majority vary as often as the honest inverse does.**
- So the variation under DEC is not evidence that honest decoding restores state-dependence. It is evidence that the collapse is a property of the untrained decoder's specific, bias-dominated random geometry, which any retraining perturbs.
- NATIVE itself varies on 2/5 seeds (52 benign, 55 trapped), extending ADDENDUM 2's single s44 counter-case: the CEM stage is not always collapsed at native.

## Criterion C: FAIL

- **Coverage leg: 0/5.** Under DEC, executed actions remain concentrated on 1-2 classes (majority share 0.57-0.80). At least one class sits below 1% on every seed (min share 0.003-0.010). The shuffled control has the same shape (min share 0.000-0.018).
- **Discrimination leg: 3/5** (52, 53, 54). Against 55 and 56, DEC's head is worse than NATIVE's.
  - Where DEC helps, it follows coverage, not decoder honesty: the DEC-SHUF head beats the NATIVE head on 4/5 seeds too (52, 53, 54, 56), and beats the DEC head on 53, 56.
  - E2's gain comes from *any* broadening of the executed-action distribution (ADDENDUM 2's lesson), which a shuffled decoder also supplies.

## Outcome (descriptive, no criterion)

- **Benign stratum (52, 53, 54, 56): DEC is worse than NATIVE on reward on 4/4**: +0.005 -> -0.814; -0.412 -> -0.768; +0.037 -> -2.392; -0.505 -> -0.761.
  - More TRUE contacts on 4/4: 0 -> 1.17; 0.50 -> 1.33; 0 -> 4.00; 1.00 -> 1.33.
  - More hazard-proximity steps and early terminations on 4/4; higher action entropy on 4/4.
  - **Undirected noise flagged on all four**, with NATIVE entropy 0.696 / 0.693 / 0.000 / 0.202.
  - Consumptions rise slightly (DEC 0.33-1.17 vs NATIVE 0.17-0.33 per 100). That is consistent with more movement, not with directed benefit seeking: harm rises more.
- **Hazard-trapped stratum (55, n = 1): DEC is marginally better than NATIVE on reward** (-2.32 vs -2.55): fewer proximity steps (22.0 vs 34.5) and early terminations (12 vs 15), but TRUE contacts unchanged (3.83 vs 3.67) and fewer consumptions (0.50 vs 1.67). DEC's entropy here is *lower* than NATIVE's (0.74 vs 1.04), so it is not the noise pattern.
  - DEC-SHUF is much worse on 55 (-7.69; 16.0 true contacts; 39 early terminations).
  - One seed; no claim.
- DEC-SHUF is worse than NATIVE on reward on 5/5 seeds, and worse than DEC on 4/5 (not 54).
- This matches the pre-registered expectation, and Worker I's replication: more diverse action without grounded valuation is mostly undirected, and in the benign stratum it buys harm. E3's default J still has no benefit channel and no trained harm head (ADDENDUM 3 read-out 3), and nothing here changes that.

## POST-HOC DIAGNOSTIC (not pre-registered; numbers never replace the pre-registered ones)

**Why it was run.** The executed-action norm under DEC (321-1,200) was ~1,000-5,000x NATIVE's (0.17-0.97). That was visible in the smoke on seed 99 before the pre-registered runs, and it was deliberately NOT acted on: the pre-stated objective was kept.

**Method.** `cem_trace_diag.py` loads each seed's saved states (encoder, head A, DEC and DEC-SHUF decoders), runs 200 NATIVE-decoder waking steps to get 20 states, and for each decoder calls the native `propose_trajectories` at those same states. `_decode_action_objects` is wrapped on the live instance to record, per CEM iteration (3 iterations, `config.py:2720`), the median O-input norm and median decoded norm (first step). Nothing else is changed.

| seed | NATIVE: iter 0 / 1 / 2 (O norm -> decoded norm) | DEC | DEC-SHUF |
|---|---|---|---|
| 52 | 3.96->0.5 / 0.86->0.2 / 0.85->0.2 | 3.96->**64** / 8.7->**141** / 18.6->**366** | 3.96->3.2 / 1.01->0.7 / 0.85->0.7 |
| 53 | 3.91->0.5 / 0.83->0.3 / 0.81->0.3 | 3.91->**50** / 10.8->**153** / 34.0->**577** | 3.91->2.3 / 0.90->0.6 / 0.82->0.6 |
| 54 | 3.91->0.5 / 0.88->0.3 / 0.86->0.2 | 3.91->**56** / 11.5->**212** / 54.8->**1081** | 3.91->2.4 / 0.92->0.6 / 0.86->0.6 |
| 55 | 4.09->0.4 / 0.83->0.2 / 0.83->0.2 | 4.09->**56** / 10.9->**207** / 35.2->**986** | 4.09->1.3 / 0.83->0.3 / 0.82->0.3 |
| 56 | 3.90->0.6 / 0.87->0.3 / 0.85->0.3 | 3.90->**59** / 10.7->**198** / 31.8->**875** | 3.90->1.9 / 0.90->0.5 / 0.84->0.5 |

What this shows (5/5 seeds, D1/D2 on the CEM internals):

1. **CEM iteration 0 samples far outside the encoder's image.** `ao_std = torch.ones_like(ao_mean)` (`module.py:2151`) gives iteration-0 samples of norm ~3.9, while the encoder's image has norm ~0.29-0.36 and per-dim std ~0.02-0.03. Any decoder fit to the encoder's image is ~12x out of distribution on the first iteration.
2. **The decoder's raw output is the rollout's action vector.** `_decode_action_objects` returns `action_object_decoder(flat)` unnormalized (`module.py:644-647`), which is passed to `E2.rollout_with_world` (`:2280-2287`). The rollout then re-encodes it with `action_object_head` (`e2_fast.py:813`) and the refit follows those codes (`module.py:2476`).
   - The untrained decoder (small weights) and DEC-SHUF (near-flat logits) both **contract** the loop, toward O norm ~0.8 and decoded norm 0.2-0.7.
   - With the untrained decoder, that contraction toward a small ball is exactly the bias-class pinning ADDENDUM 3 described.
   - A CE-trained inverse emits confident logits (norm 6-8 on in-distribution O; ~55 on iteration-0 samples). E2 encodes those large "actions" to larger O, and the loop **diverges** (roughly x3 per iteration).
   - DEC candidates are therefore class-diverse, but their rollouts are driven by action vectors hundreds of times larger than anything E2's world head was trained on (one-hot).
3. **So the edge has three coupled defects, and training the decoder alone fixes one of them:**
   - (a) the decoder is untrained (trace Q1);
   - (b) nothing constrains decoded output to the action space the rollout and world head assume;
   - (c) iteration-0 `ao_std = 1` is not calibrated to the encoder's image.

   (b) and (c) were latent while the decoder was untrained, because its small weights happened to contract. They become the binding problem the moment the decoder is made to invert.

This diagnostic does not change either verdict. It explains why an honest inverse does not produce clean, state-conditioned proposals in the native loop, and why its behaviour looks like noise.

## Domain, and what this does NOT show

- **D2** for the P edge (intervening on the decoder changes the native CEM pool) and for C (the executed-action distribution, and E2 trained on it). **D3 descriptive** for outcome. Regime B only; one encoder budget; 600 steps; 5 seeds, 4 benign + 1 trapped (the trapped stratum is n = 1).
- It does not test a decoder with bounded output, a jointly trained encoder-decoder codec (trace candidate 2), or a calibrated `ao_std`. Each would be a new design, and none was run, per the no-tuning rule.
- It does not show that a well-conditioned codec would restore state-dependent proposals. It shows that this edge cannot be closed by training the decoder alone, and that proposal "variation" is a weak signal here: a shuffled decoder produces as much of it.
- Executed actions are argmax of continuous vectors in every arm. Head training uses the argmax class (the same mismatch ADDENDUM 2/3 noted).

## Read-out for the orchestrator

1. **Stale premise corrected.** The brief's hypothesis was "the untrained decoder is the causal root of the proposal collapse".
   - Re-measured: it is *a* cause of the specific bias-class pinning, because any change to it moves the pool.
   - But an honest inverse is not better than a shuffled one on state-dependence (P fails on the control), and it does not give class coverage (C fails, 0/5).
   - The O-space interface around it also has to change: bounded decoded actions and iteration-0 scale matched to the encoder image.
2. **Work-graph classification: `complicated (buildable)`.** It covers SD-080's encoder half, the decoder (trace), and now (b) + (c) above as one codec repair. Its scope is a design decision for governance, not a missing fact.
3. **Consistent with Worker I and ADDENDUM 3.** Every intervention that diversifies action in the benign stratum (R5b there, DEC and DEC-SHUF here) buys harm, not benefit. The binding constraint for behaviour is downstream: E3's valuation has no grounded benefit term and an untrained harm head.
