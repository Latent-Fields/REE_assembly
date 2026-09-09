# Red-team DESIGN review -- V3-EXQ-1003 (EXT-004 / ARC-013 residue cross-context action suppression)

Reviewer model: **fable** (claude-fable-5-1). 2026-09-09T01:21:52Z. Read-only; no repository file edited.
Substrate: ree-v3 HEAD `35633e6`. Driver: `/Users/dgolden/REE_Working/ree-v3/experiments/v3_exq_1003_ext004_residue_cross_context_action_suppression.py` (line numbers below are from that file unless a path is given).

Two probes were run to measure rather than argue (scripts + raw logs in this directory:
`redteam_probe_1003_fable.py` -> `redteam_probe_1003_seed42.log` / `.json`; `redteam_clone_div_fable.py`; `redteam_clone_div2_fable.py`). Both import the driver's own `_build_agent`, `_step_episode`, `_context_b_phase`, `_detach_agent_buffers`, `_zero_residue_field`, `ScoreReadoutRecorder` so the path measured IS the driver's path. Probe 1: seed 42, the FULL 20x80 Context A, then five 160-step Context-B twins. Probe 2: seed 42, 3x40 Context A, then 2x40 Context B through `_context_b_phase` itself.

## VERDICT: BLOCKING

The load-bearing criterion C1 cannot discriminate under any outcome (F1 + F2 together): under the shipped procedure the ERASED-EXPOSED delta is dominated by torch-RNG-stream divergence between two Context-B runs (a measured null delta of 0.097 with NO manipulation, equal to the 0.10 bar), and under exact pairing the manipulation's own effect on the DV is 1e-4 to 3e-4 (measured twice, both Context-A scales). Separately, by the time any tick is scored, no Context-A residue geography exists in the field any more (F3), so what the arm contrast manipulates is not the quantity EXT-004/ARC-013 name.

---

## F1  [family 2/3; step: manipulation -> arm contrast -> C1]  The "paired twin" is not paired: ERASED runs on a different RNG stream, and the null delta of that alone equals the bar.

**Source.** `run_seed` seeds torch/numpy exactly twice -- line 1185 (before EXPOSED's Context A) and line 1304 (before NAIVE's Context A). The ERASED clone is taken at 1189-1190 and its Context B runs at 1240-1242, AFTER EXPOSED's Context B (1217-1219) has consumed the global torch RNG; `_context_b_phase` (1090) and `_step_episode` (799) never touch RNG state; no agent-held `torch.Generator` exists (grep of `ree_core/agent.py`, `hippocampal/module.py`, `e3_selector.py`, `residue/field.py`; the hippocampal `_rng` is the `random` module, `module.py:229`, used only on the replay path `:3068,:3109` which this driver never enters). CEM proposal noise and E3's uncommitted `multinomial` branch (`e3_selector.py:4249`) draw from that global stream. The docstring asserts the opposite at lines 244-246: "(c) the cross-seed SD of the per-cell MEAN was 0.098 ... the design is PAIRED within seed (ERASED is EXPOSED's own twin), which removes that" -- and the SE bound at 236-238 (paired delta SE <= 0.075, 6-seed mean SE <= 0.031) rests on it.

**Measured (probe 2, driver's own `_context_b_phase`, seed 42).** With torch+numpy+python RNG restored to the same state before each run: original agent p_approach 0.23713 (8 scored / 46 fresh / 34 latched, candidate share 0.2610); un-erased clone 0.23745 (8/46/34, 0.2610); ERASED clone 0.23731 (8/46/34, 0.2610). The same original agent run AGAIN on the continued stream (exactly what the driver's ERASED gets): 0.33444 (12/57/23, share 0.3697). So: identical agent, identical env seed, no manipulation, delta = **0.097**. Probe 1 at full Context-A scale gives the same picture: EXPOSED 0.3627; clone on continued stream (no erase) 0.4971; ERASED on continued stream 0.2549 -- sham deltas of +0.134 and -0.108 with nothing or everything erased.

**Unattributable result.** Any C1 value -- pass, fail, or reversed -- because the per-seed C1 delta is a draw from a distribution whose null width (~0.1-0.2 per seed at 160 steps; lock direction is per run, so 1600 steps does not average it) is the size of the bar, while the true paired effect is 1e-4 (F2). The `no_cross_context_action_level_suppression` text (1719-1737) would then be read as a precise "second and stronger null ... SE 0.031" when the instrument's own null spread per seed is ~4x that; and the split branch can fire on the same noise (F5).

**Cheap confirmer (minutes, already run, re-run for a second seed to be sure).** `torch.get_rng_state()/np.random.get_state()` immediately after the deepcopy at 1189 and restore before EACH arm's `_context_b_phase` (EXPOSED, ERASED, and NAIVE's Context B); then the ERASED-EXPOSED delta measures residue alone. Note this fix exposes F2.

## F2  [family 1; step: residue field -> Phi_R -> scores -> p_approach]  Under exact pairing, erasing the whole Context-A field moves p_approach by ~1e-4; the scoring channel cannot carry 0.10.

**Source.** `score_trajectory` applies `rho_residue * phi` (`e3_selector.py:1474,1507`), `phi = residue_field.evaluate_trajectory(world_seq)` (`:1206-1214`), which sums `rbf + 0.1*neural` along the horizon (`field.py:618-628`). `RBFLayer.forward` (`field.py:122-148`) is a sum of 32 Gaussians at `kernel_bandwidth` 1.0 (`config.py:3052`; the config's own comment at `:3086-3088` says 1.0 is "~15x too wide for the z_world residual scale").

**Measured.** Probe 1 (full Context A, seed 42, 24 scored ticks): all 32 Context-A centers lie within a ball of pairwise diameter 0.081 (norms 0.378-0.425) -- one bump, not a map. On EXPOSED scored ticks the RBF term's cross-candidate spread was 1.34 against a score range of 4.99, and its approach-minus-retreat mean was **-0.189** (the residue term is LOWER on approach candidates, i.e. it favours approach; total-score approach-minus-retreat was +0.079). Probe 2 and probe 1 both: with RNG paired, ERASED vs un-erased clone -> identical trajectory, |delta p_approach| = 1e-4 (probe 1, full scale: 0.56411 vs 0.56398; probe 2: 0.23745 vs 0.23731, max per-tick |delta| 0.0035). The driver's own dry-run recorded EXPOSED `residue_term_approach_minus_retreat_mean_b` = -0.00055 / -0.00107 (arm_results, seeds 42/43) against score ranges 4.5 / 12.1.

**Unattributable result.** A C1 PASS: it cannot come from the channel the docstring says it isolates ("p_approach conditions on the approach+retreat subset, so it isolates the scoring channel", line 58); it would have to come from the proposer channel changing WHICH ticks are scorable and the candidate composition (F4), or from F1.

**Cheap confirmer.** After the F1 fix, one seed: report `residue_term_approach_minus_retreat_mean_b` in score units next to the logit shift a 0.10 change in p_approach needs (~0.5 nat at T=1 from a 0.3 baseline). Already measured: 0.19 the wrong way at seed 42.

## F3  [family 1; step: Context A residue -> Context B field state at scored ticks]  Context-A geography is fully overwritten within the first Context-B episode; the arm contrast is a weight-mass (sensitisation) contrast on Context-B locations, not cross-context transfer.

**Source.** `RBFLayer.add_residue` (`field.py:165-180`): `idx = next_center_idx; centers.data[idx] = location; weights[idx] += intensity; next_center_idx = (idx+1) % num_centers` -- a round-robin slot recycle that MOVES the center to the new harm location while keeping the accumulated weight. `num_basis_functions = 32` (`config.py:3051`). Residue is written TWICE per committed harm step: `agent.update_residue` -> `residue_field.accumulate` (`agent.py:10747`) and `e3.post_action_update` -> `residue_field.accumulate(actual_z_world, harm_magnitude=1.0)` (`e3_selector.py:4424-4428`, called from `agent.py:10596`). Context B is hazard-live (`CONTEXT_B_ENV_KWARGS`, 554-558; `hazard_harm` default 0.5, `causal_grid_world.py:139`; proxy `hazard_approach` fires on 100% of cells per the 991 autopsy, docstring 121-128).

**Measured (probe 1).** Field `num_harm_events` 1111 -> 2323 after 80 Context-B steps (57 env harm events; ~2 writes per event). `centers_still_at_contextA` after 80 steps: **0 of 32**; after 160: 0. EXPOSED's weights at Context-B entry 2.84-4.97 per center (mean 3.89), so from step ~30 onward EXPOSED carries Context-B geography with Context-A weight mass; ERASED carries Context-B geography with Context-B mass only (RBF spread 0.26-0.34 vs EXPOSED 1.34). 20x80 = 1600 Context-B steps are scored; the first 80 already erase the transferred structure.

**Unattributable result.** A C1 PASS (were F1/F2 fixed) would be recorded as "residue acquired in one context suppresses action in a novel context" (label 1683, text 1685-1691) when the field at every scored tick contains no Context-A location at all; what differs is a gain on Context-B-acquired residue. Conversely the null-branch text (1728-1730) calls it "the first [null] on a construct-valid ... DV", but the construct (transfer of Context-A structure) is not present at measurement time.

**Cheap confirmer.** Record `centers_still_at_contextA` (compare `rbf_field.centers` against a snapshot taken at 1189) per Context-B episode; or make Context B harm-neutralised for the readout (the NAIVE kwargs, 539-549) so the field is frozen at its Context-A state while scored. Either is a few lines.

## F4  [family 2; step: candidate set -> scored-tick subset -> p_approach]  p_approach conditions on a subset the manipulation itself selects, and its uniform-score value IS candidate composition.

**Source.** `observe` drops a tick when it lacks both directions (685-686, counted in `n_unscorable_no_contrast`); the candidate set is a CEM search whose initial mean reads `residue_field.evaluate(z_world)` (`hippocampal/module.py:510`, no `rho_residue` gate; CEM candidates carry `world_states` from `rollout_with_world`, `module.py:2176`). Softmax at uniform scores gives p_approach = n_appr/(n_appr+n_retr) (docstring 165-167 says so). Dry-run: `n_unscorable_no_contrast_b` 33 / 19 / 13 and `candidate_approach_share_mean_b` 0.297 / 0.118 / 0.199 for EXPOSED / ERASED / NAIVE (seed 42) -- the arms are scored on different tick subsets with different compositions. Probe 1: p_approach tracked candidate share almost one-for-one across all five twins (0.363/0.375, 0.497/0.507, 0.564/0.556, 0.564/0.556, 0.255/0.258).

**Unattributable result.** A C1 or C2 delta is read as re-weighting of hazard-approaching candidates at the selection layer (text 1685-1691, 1699-1704), when it is a change in which ticks survive the filter and how many candidates decode to each direction -- with no scoring-channel involvement, and (F1) mostly no residue involvement. `candidate_approach_share` is recorded but nothing in `analyse` (1520-1599) uses it.

**Cheap confirmer.** Report `p_approach - candidate_approach_share` per cell (the scoring-channel residual); in every probe twin it is within 0.01.

## F5  [family 3; step: C2 -> split branch -> EXT-004 supports]  The split branch fires on the 6-seed C2 mean alone, with no consistency criterion, on an unpaired contrast.

**Source.** `c2 = bool(c2_mean >= THRESH_C2_OVERALL_GAP)` (1564); `elif analysis["c2_overall_gap_pass"]:` (1693) routes to `EXT-004: supports, ARC-013: weakens` with no C3/C4 analogue; C3/C4 qualify C1 only (1598). NAIVE differs from EXPOSED in its entire Context-A stream AND its RNG stream at Context-B entry (F1), and the per-seed null delta is ~0.1 (F1). The branch text (1705-1712) also declares "removing the residue field did NOT remove the effect" whenever C1 < 0.10, even when C1 is, say, 0.08 of a C2 of 0.11 -- i.e. when residue removal removed most of it.

**Unattributable result.** `cross_context_suppression_present_but_not_residue_attributable` -> EXT-004 `supports` on 1-2 seeds' lock-direction draws; and ARC-013 `weakens` on a C1/C2 ratio the branch never inspects.

**Cheap confirmer.** Apply C3/C4-style qualifiers to C2, and record C1/C2 in the split text. Two lines in `analyse`.

## F6  [family 4; step: gates -> non_contributory]  P5 is vacuous, H1 certifies a perturbation 100-1000x the manipulation's size, and H2 masks a reversed effect as "not ready".

**P5** (`residue_term_live_in_e3_scores`, 1421-1436, floor `RESIDUE_TERM_SPREAD_FLOOR = 0.0` at 525, strict `>`): the recorded `residue_weighted` includes `0.1*neural_field(z)` (`field.py:626`), which varies per candidate in every arm. Dry-run ERASED spread 0.0176 / 0.0042 and NAIVE 0.0102 / 0.0045 -- all > 0 with the RBF zeroed. Probe 1: neural spread 0.0027 in every twin. P5 cannot fail; it does not test that the manipulation differentiates candidates (contrast the docstring's own reasoning for dropping `naive_residue_empty`, 317-326).

**H1 / P4** (`instrument_positive_control`, 1067-1107; `pen[appr] += max(srange,1e-6)` at 698): the perturbation is +score_range (dry-run 3.2; probe ~5) on approach candidates. The residue term's directional signal is 5e-4 (dry-run) to 0.19 the wrong way (probe). H1 certifies that a softmax responds to a shift equal to its whole range; it says nothing about a shift 25-10,000x smaller.

**H2** (`build_headroom_checks` 1476-1500, `achievable = mean(ERASED)`): ERASED is one of the two arms C1 compares. Under a REVERSED effect (residue raises p_approach -- the direction probe 1's -0.189 and the dry-run's C1 = -0.090 both point), ERASED is the LOW arm, H2 fails, and the run is filed `substrate_not_ready_requeue / non_contributory` (1671-1679) instead of `weakens`. The dry-run did exactly this (`degeneracy_reason: ... dv_headroom_suppression_room`, H2 measured 0.0245 vs 0.2). A reversed result is unfalsifiable by construction.

**Cheap confirmer.** Route C1 <= -0.10 to an explicit reversed label before the gate; set P5's floor from the ERASED/NAIVE spread (the neural-only baseline) rather than 0; note H1's perturbation size next to the measured residue term.

## F7  [family 4; step: bar derivation]  The 0.10 bar's noise argument uses tick SD with n = scored ticks, on a bimodal, regime-locked per-tick series.

**Source.** Docstring 233-238: SE = 0.41/sqrt(60). The probe RESULTS.md the bar cites shows per-tick p_approach bimodal with IQR up to 0.90 (`item2_probe/RESULTS.md`, "FREE-POLICY RANGE OBSERVED") and a policy that holds one direction for whole stretches (executed-action histograms {0:218, 4:181} etc.), so consecutive scored ticks are not independent; and the two post-Context-A cells the ROOM figure (b) leans on had 31 and 23 scored ticks, below the C5 floor the same docstring calls a "real gate". Not independently blocking; it is why the F1 null width (0.1 per seed) is 4x the docstring's per-seed SE (0.075 -> 0.031 pooled).

**Cheap confirmer.** Per-cell block-bootstrap SE by episode, recorded in `summary()`.

---

## Things checked that are NOT findings
- The deepcopy is faithful: 6,219 tensors/scalars compared across the two object graphs, zero non-residue mismatches; 12-step lockstep with all RNGs restored is bit-identical (actions, z_world, scores). The copy is taken BEFORE EXPOSED's Context B (1189 precedes 1217), so nothing leaks between arms by reference. ARC-108 `w_chan` is a registered buffer (`e3_selector.py:668`) and is covered by the state_dict assertion at 1195-1208.
- `e3_score_decomp_enabled` is record-only and the per-candidate `residue_weighted` really is per candidate (`e3_selector.py:3055-3091`, batch=1 per `score_trajectory` call).
- `world_obs_dim` is size-independent (`causal_grid_world.py:1493-1521`, 5x5 local views), so the size-8 instrument agent and the size-10 cell agents share an architecture.
- The e3.select wrapper freshness gate holds: `n_align_mismatch` 0 everywhere, `eff_temp` exactly 1.0.

## Summary table

| # | Family | Severity | One line |
|---|---|---|---|
| F1 | 2/3 | **BLOCKING** | ERASED is not RNG-paired; measured null delta 0.097 = the bar |
| F2 | 1 | BLOCKING (with F1) | paired residue erasure moves p_approach 1e-4; term favours approach |
| F3 | 1 | CONTESTED (high) | 0/32 Context-A centers survive 80 B-steps; contrast is weight gain on B-locations |
| F4 | 2 | CONTESTED | p_approach = candidate share on a manipulation-selected subset |
| F5 | 3 | CONTESTED | split branch fires on unqualified C2 mean; ignores C1/C2 ratio |
| F6 | 4 | CONTESTED | P5 vacuous; H1 wrong scale; H2 masks a reversed effect |
| F7 | 4 | note | SE derivation ignores regime-locking of ticks |
