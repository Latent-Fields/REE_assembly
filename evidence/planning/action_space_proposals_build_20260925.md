# W1-alt build record: ASP action-space proposals (default-OFF, integration branch)

- **Status: BUILT on `integration/coupled-loop-repair`**, default-OFF, bit-identical when OFF. Session `bt0925-w1alt` (headless build worker, `orchestrate-20260924-breakthrough`), chip_ref `chip-20260925-coupled-w1alt-asp-build`. Written 2026-09-25.
- **Design built:** `action_space_proposals_design_20260925.md` (`412882b845`), sec 2.1 (ASP-E), 2.4 (ASP-R, ASP-0), 3.1-3.3, 4 (G-ASP (a)-(d)).
- **Branch commit:** `1a16595` on `integration/coupled-loop-repair` (pushed 2026-09-25T19:21Z, fast-forward from `cc20be5`; exactly the 4 files: `ree_core/hippocampal/module.py`, `ree_core/utils/config.py`, `tests/contracts/test_action_space_proposals.py` (new), `tests/test_flag_inertness.py`). Built on origin/main `21c86cb` (MECH-157, MECH-287b, MECH-039, I1, the main-red fix). Commit gate: full `tests/contracts` run LOCALLY on the Mac (user-sanctioned 2026-09-25): 5836 passed, 0 failed, 25 skipped, 3 xfailed, 22m39s wall, 774 MB peak RSS. An earlier gate on ree-cloud-5 failed on one test (a token scan matching `action_objects` in a config comment; comment reworded). No docs, experiments or queue on the branch (plan sec 6).
- **Evidence domain: D1** for gates (a), (b), (d) (contract-level, untrained modules, deployed K/H/A/I and world_dim 32). Gates (e)/(f) out of scope (need W3, W4, I1).

## 1. Decisions taken (orchestrator delegation rec-20260924-fb429c72)

| id | decision | how it is built |
|---|---|---|
| U5 | BRANCH | as above |
| U2 | include ASP-0 behind the same knob family | `action_space_first_action_mode="stratified_uniform"`: stratified first action, uniform continuation, no refit, one draw |
| U4 | expose the CEM elite-scoring depth, default = current behaviour | `action_space_cem_score_horizon=None` -> full horizon (same window as the codec CEM) |
| U1, U6 | HELD for the user | not touched |

## 2. What was built (file:line at the branch commit)

- **Knobs (4, all three config sites):** `use_action_space_proposals` (False), `action_space_first_action_mode` (`"stratified"` | `"refit"` | `"stratified_uniform"`), `action_space_prob_floor` (0.02, DRAFT), `action_space_cem_score_horizon` (None). `config.py:2945-2966` (dataclass), `:9118-9121` (from_dims kwargs), `:10820-10826` (assignment).
- **Branch point:** `propose_trajectories` sets `_asp_on` (`module.py:2539`); when on, `terrain_prior` is not called (`:2543`), the O-space CEM loop runs zero iterations (`:2625`) and `_propose_action_space` (`:1525`) supplies the pool and `cem_iteration_diagnostics` (`:2904`). Everything from the MECH-293 ghost block onward is unchanged; ASP summary diagnostics are merged at `:3189` (empty dict when OFF).
- **Algorithm:** stratified first action (K=32, A=5 -> 7/7/6/6/6), per-class per-step categorical continuation refit to that class's elites (`max(2, round(elite_fraction x n_c))`) over `num_cem_iterations`, `p <- (1 - floor x A) x elite_freq + floor`. Exact one-hot actions, `rollout_with_world(..., compute_action_objects=True)` so O's readers still get a tensor. Sampling is inverse-CDF over `torch.rand` (not `torch.multinomial`, which diverges across the fleet's machine classes); probabilities kept in float64 so the floor is exact. Candidates tagged `metadata["source"]="action_space_cem"`.
- **Exclusions (raise at construction, `_validate_action_space_proposal_config`, `:1435`):** `use_differentiable_cem`, `use_orthogonal_cem_seeding`, `mode_conditioning_enabled`, `use_mech293_ghost_probes` (the design's four) **plus `use_cem_modulatory_authority`** (added: its elite-stage rescale acts on the codec loop's score list, so under ASP it would be a silent no-op). Invalid mode, `floor < 0` or `floor x A >= 1`, and a score window outside `[1, horizon]` also raise. All checks are skipped when the master is OFF (sub-knobs unread).
- **Diagnostics (G-ASP in-run readouts, design E5):** `action_space_decoder_calls`, `action_space_terrain_prior_calls` (deltas of two plain-int counters incremented in `_decode_action_objects` / `_get_terrain_action_object_mean`), `action_space_max_action_norm`, `action_space_all_actions_one_hot`, `action_space_stratified_counts`, `action_space_step0_counts`, `action_space_min_categorical_prob`, `action_space_rollout_norm_ratio_median`, `action_space_rollout_max_step_growth_median/_max`; per iteration `action_space_continuation_entropy`, `action_space_step0_entropy` (refit), `action_space_refit_applied`.
- **Not a trainer member, no guard group** (design 3.5): ON adds no parameter (contract asserts the parameter list is unchanged).

## 3. Contracts (`tests/contracts/test_action_space_proposals.py`, 35 items)

| test | pins | pre-build | post-build (Mac, no-pytest runner) |
|---|---|---|---|
| knobs default + from_dims round trip | 3-site rule | FAIL (AttributeError) | PASS |
| OFF bit-identity, all sub-knobs non-default | sub-knobs unread when OFF; codec path still calls decoder K x I, terrain_prior 1 per call | FAIL (TypeError) | PASS |
| OFF RNG stream == pre-build codec stream | OFF consumes exactly K x I `randn([1,H,ao])` per call | PASS **by design** (a preservation pin); FAILS under mutation M4 (one extra `torch.rand` on the OFF path), which the within-tree identity test above does NOT catch | PASS |
| ON changes the pool | flag-inertness probe (`use_action_space_proposals` added to PROBED) | FAIL | PASS |
| G-ASP (a) x3 modes | no new params; terrain_prior 0 forwards; decoder never run with grad (only the no-grad round-trip diagnostic, <=1); backprop through world states, actions and O leaves both modules' grads None while `z_world` gets gradient | FAIL | PASS |
| G-ASP (b) x3 modes | exact one-hot at every step over 25 states; decoder calls 0; max norm 1.0 | FAIL | PASS (refit: over ASP-generated candidates; see xfail) |
| G-ASP (b) final refit pool (strict xfail) | finding F2 below | xfail | xfail |
| G-ASP (c) readout | diagnostics equal an independent recomputation | FAIL | PASS |
| G-ASP (d) stratified x2 modes x3 (K,A) | counts exactly floor/ceil(K/A), every class present, SP injector 0, over 20 states | FAIL | PASS |
| G-ASP (d) refit floor | every refit categorical >= floor, rows sum to 1 | FAIL | PASS |
| G-ASP (d) refit coverage >= 0.95 (strict xfail) | finding F1 below | xfail | xfail |
| refit moves the continuation, ASP-0 does not | non-vacuity of the refit | FAIL | PASS |
| score window reaches the scorer (None, 3) | U4 knob wiring | FAIL | PASS |
| sampler never draws a p=0 class | inverse-CDF sampler | FAIL | PASS |
| 5 exclusions raise; 6 invalid sub-knob values raise | 3.3 | FAIL | PASS |

**Mutation checks (test half, non-vacuity):** M1 zero continuations -> gate (b) fails 3/3; M2 a decoder call on the ASP path -> gate (a) fails 3/3; M3 unstratified counts -> gate (d) fails 6/6; M4 extra RNG draw on the OFF path -> the RNG-stream pin fails; M5 floor dropped from the refit -> the floor test fails. Scripts: `.scratch/breakthrough-20260924/w1alt/{mini_runner.py,mutate.py}` (umbrella, not committed).

**OFF bit-identity against the pre-build tree (Mac, torch 2.10):** 2 configs x 5 states x full pools (actions + world-state sequences) + final RNG state hash identically on `5f965cf`'s `ree_core` and the build: `ce0822dd...4cef5e` both (`w1alt/off_identity.py`).

**Cloud verification:** targeted `remote_pytest.sh tests/contracts/test_action_space_proposals.py tests/test_flag_inertness.py -q` -> **99 passed, 2 xfailed** (ree-v3 base `5f965cf` + the build, run_id `DLAPTOP-4-98601-20260925T140339Z-2648022676`). The first commit gate ran the full contracts suite on ree-cloud-5 (5777 passed, **1 failed**, 64 min). The failure was a token scan: `test_exp0155...::test_action_objects_have_no_consumer_outside_producer_hippocampus_and_e3` matched the literal `action_objects` in a `config.py` **comment**. It was not a consumer. The comment was reworded; that test and this file pass locally on the rebased tree, as does MECH-287b's new `test_pag_descending_release.py` (10/10). The second gate is in flight.

## 4. Member gate status (G-ASP, design sec 4)

| gate | status | evidence |
|---|---|---|
| (a) guard/trainer | **PASS (D1, contract)** for all three modes | contract (a); in-run: `action_space_decoder_calls`/`_terrain_prior_calls` = 0. The trainer-level G5 window reading needs the W6 preset |
| (b) action validity | **PASS for ASP-E and ASP-0**; **FAIL for ASP-R's final pool** (F2) | contract (b) |
| (c) bounded rollouts | **NOT ASSESSABLE before W3** (design: "read with the W3 head"). Readout built and verified. On an untrained E2 (deployed dims) the ASP pool grows x2.92 over H (median max step growth 1.154) and the codec pool x2.90 (1.153): the growth belongs to the untrained world head, not the proposer | `w1alt/asp_smoke.py`, `w1alt/codec_growth.py` (seed 0 module, seed 1 state) |
| (d) coverage/support | **PASS for ASP-E and ASP-0** (exact n_c, every class in 100% of pools); **ASP-R: floor PASS, coverage FAIL** (F1) | contract (d); `w1alt/refit_cov.py` |

## 5. Findings (reported, not acted on)

- **F1 -- ASP-R re-concentrates at the DRAFT floor.** With `action_space_prob_floor=0.02`, only 4/40 refit pools hold every first-action class after 3 iterations (floor 0.1 -> 37/40; 0.19 -> 40/40; K=32, A=5, untrained modules, seed 3). ASP-R is the non-recommended variant; it fails its own (d) at the draft constant. Pinned as a strict xfail.
- **F2 -- ASP-R collapse re-admits the design's P2 defect.** When ASP-R collapses to one class (1/25 states measured), the default-ON SP-CEM injector adds a scaffold token whose continuation is zero vectors, so the pool E3 receives is not all one-hot. ASP-E/ASP-0 never trigger it (every class present -> injector no-ops). The zero-continuation fix stays an owner decision (MECH-131 / ARC-065 / `/governance`, design sec 2.3). Pinned as a strict xfail.
- **F3 -- one extra exclusion.** `use_cem_modulatory_authority` was added to the design's four mutual exclusions (reason in sec 2).
- The ASP diagnostics are the in-run R1 readouts design edit E5 asks for; no I1 instrument was built here.

## 5a. Pool format homogeneity (orchestrator question, re GFLAG-0555 / `847544ac8e`)

- **ASP-E and ASP-0: the pool E3 receives is format-homogeneous at default post-CEM settings, and a contract asserts it.** Gate (b) runs on the FINAL pool, after the SP-CEM injector, scaffold, chunk splice and promotion gate. It requires every step of every candidate to be an exact one-hot: entries in {0,1} and row sum 1. That rules out zero tails and decoder-scale continuous vectors. Gate (d) asserts the SP injector added 0 candidates. `test_on_changes_the_pool` asserts every candidate carries `source="action_space_cem"`, so no decoder-output candidate is mixed in. So the construction-scale mismatch GFLAG-0555 names cannot arise inside an ASP-E pool: there are no decoder-scale candidates to compare against. No new contract was needed.
- **ASP-R is NOT homogeneous.** When it collapses to one class, the SP injector adds a unit-one-hot-then-zeros token (F2, strict xfail). That is the GFLAG-0555 construction, mixed into an otherwise one-hot pool.
- **Downstream consumers.** E3 scores only the pool it is handed, so under ASP-E it compares one-hot against one-hot. The executed action is a one-hot, as the env expects.
- **Open items (not checked here):**
  1. ARC-071 chunk injection (`use_chunk_proposal_injection`, default OFF) builds one-hot steps for the chunk's length and zeros after it (`_build_chunk_candidates`). With it ON, zero tails would re-enter an ASP pool.
  2. The R5b scaffold (`use_action_class_scaffold_candidates`, default OFF) has the same shape. The INT-ACT preset must keep it False.
  3. Any cross-tick consumer that compares an ASP candidate with a decoder-generated one (e.g. a habit/planned arbitration or replay comparison) is not audited.

## 6. Not done

- Gates (e)/(f) (need W3, W4, I1). No probe beyond the contract-scale measurements above. No A1 edits, no registry row (U6 held), no queue entry.
- The non-contract remainder suite (LANDER_NOTICE step 2) was not run: the change is default-OFF and pinned bit-identical; the commit gate ran the contracts.
