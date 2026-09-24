# Does training the action_object_decoder break the proposal collapse? (pre-registered causal probe)

- **STATUS: INTERIM (seeds 52, 53 of 52-56).** 2026-09-24T23:26:55Z. Final verdicts pending the remaining three seeds; the per-seed numbers below will not change.
- Session `bt0925-decoder-probe` (Worker J, breakthrough integration pass `orchestrate-20260924-breakthrough`), chip_ref `chip-20260925-decoder-training-causal-probe`. Probe only: nothing lands in ree_core, nothing queued, no registry touched.
- Code under test: ree-v3 `origin/main` @ `863d23d65a` (private detached worktree; same sha as Worker I's replication, whose record confirms no diff against ADDENDUM 3's `44c55300ca` on hippocampal/E3/env/harness files).
- Probe: `.scratch/breakthrough-20260924/decoderprobe/decoder_probe.py` -- a copy of ADDENDUM 3's `probes/rollout/partitioned_repair_probe.py`, with everything through the CHOICE block unchanged (same P0 warmup, replay, heads, choice cells), plus the decoder-training step, the three pre-registered arms, the outcome decomposition and the discrimination measure. Summarizer `summarize_dec.py`. Raw JSON `results/DEC_s{seed}.json`.

## PRE-REGISTRATION (verbatim from the brief, fixed before any run)

- Seeds: 52, 53, 54, 55, 56 (fresh). Record each seed's NATIVE early-termination rate over the first 600 steps and classify it hazard-trapped (>= 10 early terminations) or benign BEFORE looking at the other arms; report results stratified.
- Arms: NATIVE; DEC (trained decoder); DEC-SHUF (same objective, same data, action labels permuted across timesteps -- same class marginals). R5b/R2/tiebreak OFF in all arms (native regime). 600 closed-loop steps after the same warmup.
- Criterion P (proposal): the CEM pool's majority first-action class varies across 20 probe states in >= 4/5 seeds under DEC, AND in <= 1/5 under both NATIVE and DEC-SHUF.
- Criterion C (coverage): under DEC, every action class makes up >= 5% of executed actions in >= 4/5 seeds, AND E2 world-head action discrimination (the addendum-1 metric, trained on the agent's own DEC-arm replay, same budget) beats the NATIVE-replay head on >= 4/5 seeds.
- Outcome (reported, NO success criterion): env reward per 100 steps, TRUE harm contacts and hazard-proximity steps decomposed from the start, consumptions, early terminations, action entropy. Flag undirected noise explicitly.
- No additional arms, no tuning, no re-running seeds except a clearly-labelled post-hoc diagnostic whose numbers never replace the pre-registered ones.

## Decoder objective (my choice, stated in the probe's docstring before any run)

- **Trace candidate 1, the smallest one.** `CE(action_object_decoder(o), a)`, with `o = E2.action_object(z_t, onehot(a_t), action_bias)` computed under `no_grad`. The encoder, E1 and E2 are frozen, so only the decoder moves. It gets its OWN Adam optimizer (lr 1e-3, batch 64, 2000 steps, 80/20 held-out split, fit threshold >= 0.5 held-out).
- **Why this objective.** The CEM samples in O, decodes with `action_object_decoder` (`ree_core/hippocampal/module.py:178-182`, called via `_decode_action_objects` at `:2280`), then re-encodes the rolled-out actions with `E2.action_object` (`ree_core/predictors/e2_fast.py:660-691`, called inside `rollout_with_world` at `:812-813`) and refits in that encoder's image (`module.py:2466-2477`). A decoder that inverts the encoder is therefore exactly what makes decode(refit mean) mean "the action the elites took".
- **Cue bias.** `action_bias` is the E1 cue bias the live agent passes (`agent.py:6421-6426`, `:6601`). E1 has no `world_query_proj` in this config, so it is None; measured `bias_present: false` on every seed.
- **Data.** The harness's existing post-P0 uniform-random-policy episodes (`rnd`: RandomPolicy, the SD-070 warmup policy, encoded by the post-warmup encoder; ~1,650-1,690 steps, ~uniform over 5 classes). These are the agent's own executed actions, with no reward or env internals, so no privileged information.
  - The agent's native waking replay was NOT used. ADDENDUM 2 showed it lacks 1-2 action classes entirely, so a decoder trained on it could not emit them: failure by construction, not a test.
- **DEC-SHUF.** Identical inputs, optimizer and budget; targets permuted across timesteps with a fixed generator.
- **Arm setup.** Each arm is a fresh agent from the same seed, with the master's encoder and the own-replay head A loaded (ADDENDUM 3's native regime; COV/R5b/R2 off). DEC loads the trained decoder, whose init is byte-identical to NATIVE's because the seed is the same. An in-run check confirms the decoder weights are unchanged by the closed loop.
- **Measures.**
  - P: the harness's own `m4_proposal` over 20 states of the arm's own log; "varies" = >= 2 distinct majority classes.
  - C-coverage: min class share of executed actions.
  - C-discrimination: `encoding_vs_objective_probe.evaluate` (the ADDENDUM 1 metric). Executed action closest at **h = 1 is the comparison, fixed before running**; h = 3 and 5 are reported. Heads are trained per arm by `balanced_replay_probe.train_arm` (3000 updates, the ADDENDUM 2/3 budget) from the same init on that arm's ~590 closed-loop transitions, and evaluated on one held-out uniform-random test set per seed (`build_B(seed+23)`, 1,500 steps, 300 starts).
  - Outcomes: split by `info["transition_type"]`. True contacts = `{agent_caused_hazard, env_caused_hazard, env_caused_multisource}` (Worker F); proximity = `hazard_approach`; consumption = `resource`. Early termination = an episode that ends before 200 steps.

## Harness checks (both seeds)

| seed | DEC grad non-None on all decoder params (step 0) | DEC fit held-out | DEC-SHUF fit held-out vs its targets / vs true action | O norm (per-dim std) | DEC logit norm on O |
|---|---|---|---|---|---|
| 52 | yes | **1.000** (all 5 classes 1.00) | 0.210 / 0.189 | 0.363 (0.024) | 6.25 |
| 53 | yes | **1.000** | 0.225 / 0.180 | 0.293 | 8.00 |

The decoder receives gradient and fits the inverse perfectly, so the dead-optimizer pattern is not present here. DEC-SHUF stays at chance, as a control should.

## Seed classification (from NATIVE only, recorded before the other arms were read)

| seed | NATIVE early terminations in 600 steps | class |
|---|---|---|
| 52 | 0 | benign |
| 53 | 0 | benign |

## Per-seed results (interim; benign stratum only so far)

| seed | arm | reward/100 | true contacts/100 | hazard-prox/100 | consumptions/100 | early terms | action entropy | min class share | executed-action norm | proposal majority class across 20 states | P varies |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 52 | NATIVE | +0.005 | 0.00 | 1.8 | 0.17 | 0 | 0.696 | 0.000 | 0.25 | {0:12, 2:8} | yes |
| 52 | DEC | -0.814 | 1.17 | 12.3 | 0.67 | 4 | 0.861 | 0.007 | **321** | {1:12, 2:4, 3:4} | yes |
| 52 | DEC-SHUF | -1.109 | 2.00 | 12.3 | 0.50 | 6 | 0.976 | 0.008 | 0.82 | {0:3, 2:17} | yes |
| 53 | NATIVE | -0.412 | 0.50 | 5.3 | 0.17 | 0 | 0.693 | 0.000 | 0.26 | {3:20} | no |
| 53 | DEC | -0.768 | 1.33 | 8.5 | 0.50 | 3 | 0.891 | 0.010 | **490** | {0:1, 1:7, 3:12} | yes |
| 53 | DEC-SHUF | -2.095 | 3.17 | 27.7 | 1.17 | 11 | 1.259 | 0.018 | 0.66 | {1:18, 3:1, 4:1} | yes |

E2 world-head action discrimination (executed-action-closest, h = 1 / 3 / 5, chance 0.20; k = steps beating persistence):

| seed | NATIVE-replay head | DEC-replay head | DEC-SHUF-replay head |
|---|---|---|---|
| 52 | 0.167 / 0.193 / 0.167 (k 0; replay classes {0,1,2}) | **0.283** / 0.247 / 0.263 (k 5; 5 classes) | 0.220 / 0.220 / 0.207 (k 0) |
| 53 | 0.207 / 0.220 / 0.257 (k 0) | **0.277** / 0.260 / 0.200 (k 5) | 0.327 / 0.337 / 0.333 (k 5) |

## Interim reading (not a verdict)

- **Criterion P: already mathematically FAIL.** DEC-SHUF varies on 2 of 2 seeds, and the criterion allows <= 1 of 5. NATIVE also varies on seed 52 (the same counter-case ADDENDUM 2 found on s44). DEC does vary on 2 of 2.
- **Criterion C: already mathematically FAIL on its coverage leg.** Under DEC, every-class-at->=5% holds on 0 of 2 seeds; the minority classes sit at 0.7-2.5%. The discrimination leg holds on 2 of 2 so far.
- **Undirected noise is flagged on both seeds.** DEC raises entropy and lowers reward, with more true contacts, more proximity steps and more early terminations than NATIVE.
- **A large mechanistic signal, not pre-registered as a measure:** under DEC the executed action vector's norm is **321-490 vs 0.25** native. See the post-hoc diagnostic below.

## POST-HOC DIAGNOSTIC (not pre-registered; its numbers never replace the pre-registered ones)

`cem_trace_diag.py` (seed 52 only; `results/POSTHOC_cemtrace_s52.json`) wraps `_decode_action_objects` on the live instance and records, per CEM iteration, the input norm, the output norm and the first-step class of each decode call. It uses the same 20 states (from a NATIVE-decoder waking run) for all three decoders:

| decoder | iter 0: O-input norm -> decoded norm (max) | iter 1 | iter 2 | final-pool majority across 20 states |
|---|---|---|---|---|
| NATIVE (untrained) | 3.96 -> 0.52 (1.24) | 0.86 -> 0.24 | 0.85 -> 0.24 | {0:12, 2:8} |
| DEC | 3.96 -> **64** (155) | **8.7 -> 141** (440) | **18.6 -> 366** (1030) | {1:13, 2:2, 3:5} |
| DEC-SHUF | 3.96 -> 3.2 (16.6) | 1.01 -> 0.74 | 0.85 -> 0.74 | {0:4, 2:16} |

What this shows about the mechanism:

1. **CEM iteration 0 samples far outside the encoder's image.** `ao_std = torch.ones_like(ao_mean)` (`module.py:2151`), while the encoder's image has norm ~0.3 and per-dim std ~0.02-0.03. Iteration 0 is therefore ~13x out of distribution for any decoder fit to that image.
2. **With a trained decoder, the O->action->O loop diverges instead of contracting.** The CE-trained decoder returns large logits, which `_decode_action_objects` passes raw to E2 as the action vector (`module.py:2280-2287`). E2's encoder maps those large actions to larger O (8.7, then 18.6), and the refit follows them, so the decoded norm roughly doubles to triples per iteration.
   - The untrained decoder (small weights) and DEC-SHUF (near-flat logits) both contract toward norm ~0.24-0.74.
   - In the untrained decoder's case, that contraction is exactly the collapse ADDENDUM 3 described.
3. So "decoder untrained" is not the only defect on this edge. The CEM also treats the decoder's output as an unnormalized action vector and samples at a unit scale unrelated to the encoder's image. An inverse-fit decoder then produces class-diverse but magnitude-exploding, out-of-distribution candidates. That is consistent with the undirected behaviour above.

