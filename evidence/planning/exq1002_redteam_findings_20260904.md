# V3-EXQ-1002 (978 oracle-adapter discriminator) -- second red-team pass, 2026-09-04

**Status: STAGED FINDINGS for the redesign session (chip-20260904-exq1002-momentum-shortcut-redesign). Verdict CONTESTED. Reviewed the CURRENT untracked driver (1891 lines, mtime 2026-09-04T18:37:22Z, 4 arms, AGREEMENT_BAR=0.70, elevation over max(majority, repeat-previous-action), untrained negative-control arm with 0.10 margin) -- i.e. the state AFTER the momentum-shortcut repair was applied by the (stopped) resume agent. Preserved verbatim from a session-scoped scratchpad by science-wave-coord-20260904; not edited.**

Headline: (1) the 0.70 bar was calibrated against a LINEAR untrained readout (0.590) but the criterion uses the 2x128 MLP, which reaches 0.68-0.70 on the untrained latent -- the absolute bar sits ON the shortcut and the effective bar is the ~0.78-0.80 conjunct; (2) the verdict grid labels an H-B-supporting outcome (trained 0.74 vs untrained 0.69) as H-C geometry mismatch -- carry beats_untrained into the label or restate interpretation.question; (3)-(5) minor: headroom gate passes by 0.02-0.03; untrained control never consults its own non-degeneracy gate; ARM_FEATURE_DIVERGENCE_EPS 1e-6 is below the latent's per-dim std. Cleared: the last-action leak is real but measured inert (0.677 -> 0.677 with body_state[5:9] scrambled).

---

# Red-team design review: V3-EXQ-1002 (zworld_actor_adequacy_oracle_adapter)

Reviewed 2026-09-04T18:40Z against the CURRENT file:
`/Users/dgolden/REE_Working/ree-v3/experiments/v3_exq_1002_zworld_actor_adequacy_oracle_adapter.py`
(untracked, 1891 lines, mtime 2026-09-04T18:37:22Z). All line numbers below are from that version.

RED-TEAM VERDICT: CONTESTED

The design as it now stands can reach an attributable H-B (PASS is protected by the paired
untrained-control margin plus elevation over the repeat-previous-action baseline) and an
attributable H-C in its core region. The defects are: an absolute bar calibrated against the
wrong readout so that it sits AT the untrained shortcut rather than above it; a verdict grid whose
H-C / "undetermined" labels absorb results that support the REGISTERED H-B; a headroom gate
that passes by 0.02-0.03; and two non-degeneracy gaps on non-verdict paths. Plus one process
finding: the smoke manifest supplied to this review is from a 3-arm predecessor of the script.

---

## Measurements made for this review (all on rung D3_hazard_free, the run's own env/oracle/adapter)

Scratch scripts in this directory: `rt1002_autocorr_probe.py`, `rt1002_history_leak_probe.py`,
`rt1002_leak_quant.py`, `rt1002_matched_difficulty.py`, `rt1002_untrained_fullscale.py`.

| quantity | seed 42 | 43 | 44 | note |
|---|---|---|---|---|
| repeat-previous-action (trivial) baseline, held-out, run's exact split | 0.566 | 0.580 | 0.572 | matches docstring 0.568/0.582/0.573 |
| majority-class baseline, held-out | 0.250 | 0.248 | 0.246 | |
| headroom 1 - trivial vs required 0.40 (margin 2.0) | 0.434 | 0.420 | 0.428 | ratio 1.05-1.09 |
| UNTRAINED z_world, run's PPOPolicyNet adapter, 60 passes, full BC scale, held-out | **0.688** | **0.681** | **0.695** | docstring cites 0.590 -- that is the LINEAR readout |
| UNTRAINED z_world, turn states only | 0.609 | 0.616 | 0.623 | genuine state reading, not persistence |
| UNTRAINED z_world, random-driven states | 0.613 | 0.636 | 0.631 | |
| UNTRAINED z_world, train split | 0.828 | 0.828 | 0.821 | train/held-out gap 0.13-0.15 |
| raw field, run's adapter, held-out / train | 0.985/0.997 | 0.980/0.992 | 0.973/0.986 | |
| raw field passed through fixed random 25->32 tanh re-embedding, held-out / train | 0.953/0.980 | 0.959/0.978 | 0.958/0.972 | instrument learns a non-axis-aligned smooth map at this n/passes |
| effective PASS threshold per seed = max(0.70, trivial+0.20, untrained+0.10) | 0.788 | 0.781 | 0.795 | |

Leak test (dry-scale warmup, seed 42, 21 train eps): scrambling `body_state[5:9]` (the one-hot
last action) before replay changes z_world-adapter held-out agreement 0.677 -> 0.677 and
random-driven agreement 0.614 -> 0.621. The body->z_self_init->z_beta->beta_to_split->world_topdown
pathway into z_world exists (`ree_core/latent/stack.py:1361-1362, 1387-1388, 966-967`, EMA at
`:1543`) but its measured contribution to the DV is zero at two decimals; and the untrained
control carries the identical pathway, so the differential cancels it in any case.

---

## Finding 1 (family 2 -- criterion calibrated against a different instrument): CONTESTED

**Citation.** Constants block lines 436-452 (`AGREEMENT_BAR = 0.70`, comment: "(2) an UNTRAINED
z_world ... supports 0.590 held-out under a LINEAR readout ... 0.70 sits above both shortcuts with
margin"); docstring line 237 ("UNTRAINED z_world -> oracle action (LINEAR): 0.590") and line 251
("`AGREEMENT_BAR = 0.70` sits above BOTH measured shortcuts (0.57, 0.59)"). The criterion is
evaluated with `_make_adapter` = `x734.PPOPolicyNet` (2x128 tanh MLP, line ~840) trained by
`_train_adapter` for 60 passes, not a linear readout.

**What the run would misreport.** With the run's own adapter the untrained random-projection
z_world reaches 0.681-0.695 held-out (table above). The absolute bar of 0.70 therefore does NOT
sit above the untrained shortcut; it sits on it. The docstring's statement that the bar "stays
inside the demonstrated achievable range" measures the range against the RAW FIELD ceiling
(0.97), which is not a z_world reader's ceiling. Consequences: (a) the absolute bar carries no
shortcut protection -- every bit of discrimination rests on `AGREEMENT_ELEVATION_MIN` (over
~0.57) and `UNTRAINED_CONTROL_MARGIN`; (b) the effective PASS threshold is ~0.78-0.80 per seed,
51-56% of the way across the (trivial, raw ceiling) range, not the "well below" the text claims.
A reader of the constants block would believe a 0.72 verdict-arm result had cleared a
shortcut-safe bar by 0.02; in fact it is within 0.03 of what a random projection achieves.

**Cheap confirmer.** Rerun `rt1002_untrained_fullscale.py` (~3 min), or in the real run read
`per_arm.zworld_untrained.per_seed_oracle_action_agreement`: any value >= 0.68 confirms. Fix is
textual + numeric: re-state the untrained ceiling as the MLP figure and either raise
`AGREEMENT_BAR` above it or state explicitly that the absolute bar is inert and the differential
criteria are the only load-bearing ones.

## Finding 2 (family 3 -- verdict grid re-scopes the registered question): CONTESTED

**Citation.** Interpretation grid lines 1631-1651: `elif off_clears and beats_untrained` -> H-B
(1635); `elif off_clears and not beats_untrained` -> `substrate_not_ready_requeue` / undetermined
(1639-1647); `else` -> H-C (1648-1651). `null_reading` (c) at lines 1738-1749 ("the DV cannot
separate 'this representation supports the mapping' from 'any projection of this observation
does'"). H-C null_reading lines 1750-1754 ("still cannot reproduce the oracle from frozen
z_world"). The hypotheses as registered (docstring lines 25-33 and the queue brief): H-B = "the
frozen latent DOES support the representation-to-action mapping; the deficit is in the RL
consumer's LEARNING"; H-C = "the geometry does not make the mapping accessible".

**What becomes unattributable.** The redesign changed the operative question from "does 978's
frozen latent support the mapping?" to "did the WARMUP add actionability beyond a random
projection?". Under the REGISTERED H-B, a random projection of world_state supporting 0.69 and the
trained latent supporting 0.74-0.79 is evidence FOR H-B (978's PPO consumer got 0.267 res/ep from
a latent whose untrained precursor a supervised reader already decodes at 0.69 -- the locus is the
consumer). The grid records that as:
- `zworld_off` in [0.70, trivial+0.20 ~ 0.77): label `zworld_geometry_blocks_oracle_mapping_h_c_geometry_mismatch`
  (line 1650). The label and null_reading say the geometry blocks the mapping; the manifest says the
  reader reproduces the oracle from it at 0.70-0.77 while a random projection does 0.69.
- `zworld_off` in [~0.78, untrained+0.10 ~ 0.79-0.80): undetermined, with text claiming "an
  UNTRAINED latent does just as well" (1640-1641) -- at 0.78 vs 0.69 it does not.
- Only >= ~0.79-0.80 on 2/3 seeds is recorded as H-B.
Nobody reading `hypothesis_verdict` alone can tell "trained latent is no more actionable than a
random projection" (a real finding about the WARMUP) from "z_world lacks accessible directional
structure" (the registered H-C), and the H-C corroborator (rotation/reweighting) would be queued
against the wrong reading in the first case.

**Cheap confirmer.** Arithmetic on the table above: per-seed PASS thresholds 0.788/0.781/0.795;
H-C region is everything below trivial+0.20 regardless of `beats_untrained`. One extra dry-run
assertion: feed synthetic rows (off=0.74, untrained=0.69, trivial=0.57) through the grid and check
which label comes out. Suggested repair: carry `beats_untrained` into the H-C label/null_reading
(H-C-proper = fails bar AND does not beat untrained; "partial support" otherwise), and state in
`interpretation.question` that the run now adjudicates warmup-added actionability, or restore the
registered question.

## Finding 3 (family 4 -- headroom gate passes by 0.02-0.03 on a statistic no arm controls): CONTESTED (minor)

**Citation.** `dv_headroom_agreement_elevation`, lines 1391-1410: control values are the
per-seed `trivial_baseline` (= repeat-previous-action, 0.566-0.582), `statistic="ceiling_headroom"`,
`margin=2.0` (line 1406) -> required 0.40. `instrument_ready` (line 1411) ANDs `dv_gate_green`, and
the z_world arm loop (lines 1454-1460) is gated on it.

**What it does.** Measured headroom is 0.418-0.434 vs 0.40 required (ratio 1.05-1.09). A seed
whose 12-episode test split realises persistence >= 0.60 routes the WHOLE run to
`substrate_not_ready_requeue` before any z_world arm runs, on a property of the oracle's walk, not
of any representation. Not a misattribution (it is an honest refusal), but the margin-2.0
declaration is satisfied only nominally and the run is one unlucky split from answering nothing.

**Cheap confirmer.** 1 - 0.582 = 0.418 vs 0.40, from the docstring's own numbers (line 232-236).

## Finding 4 (family 4 -- differential criterion never checks its comparator's gate): CONTESTED (minor)

**Citation.** `_untrained_by_seed` (line 1558) is built from `all_rows` with no reference to
`gate["red_arms"]`; `arm_criteria_non_degenerate` (lines 1653-1657) files
`C_verdict_arm_beats_untrained_control` under `ARM_OFF`, so its non-degeneracy tracks the VERDICT
arm's gate, not the CONTROL arm's. `zworld_not_collapsed` is declared to apply to the control (line
1537-1540) but its result is never consulted where the margin is computed.

**What it does.** A collapsed untrained projection (PR < 2) yields a low untrained agreement and
hands the verdict arm a free 0.10 margin -> H-B PASS, with the criterion still flagged
non-degenerate. Measured PR of the untrained latent is 7.5-10.3 so the risk is small in practice,
but the gap is structural.

**Cheap confirmer.** grep: no `ARM_UNTRAINED` / `red_arms` reference between lines 1556-1575. One
extra dry-run assertion: mark the untrained arm `structurally_vacuous` and check that
`criteria_non_degenerate["C_verdict_arm_beats_untrained_control"]` flips to False.

## Finding 5 (family 4 -- secondary criterion's non-degeneracy check cannot fail): CONTESTED (minor, non-verdict)

**Citation.** `ARM_FEATURE_DIVERGENCE_EPS = 1e-6` (line 454); check at lines 1668-1674
(`mean_abs_feature_delta > ARM_FEATURE_DIVERGENCE_EPS`). Frozen z_world per-dim std is
0.005-0.010 (manifest `feature_standardisation.raw_per_dim_std_*`). In the 18:37Z smoke the OFF/ON
delta was 5.4e-5 (0.8% of a feature std) with `mean_argmax_disagreement_frac = 0.0` and identical
agreement rows, yet the flag reads non-degenerate. Only `C_sd018_supervision_changes_accessibility`
is affected (reported, never gating).

**Cheap confirmer.** manifest ratio `zworld_arm_feature_divergence.mean_abs_feature_delta /
feature_standardisation.raw_per_dim_std_median` alongside `mean_argmax_disagreement_frac`.

## Finding 6 (process -- the evidence handed to this review describes a different script)

- Header lines 1-24 carry a prior pass's "DO NOT QUEUE ... BLOCKING" plus an INTEGRITY NOTE that
  code was added during the review window by a session that did not author it, and that nothing
  is committed. The file is untracked (`git status`: `??`).
- The smoke manifest cited in the task (`..._20260904T182557Z_v3.json`) was produced by the
  1655-line, 3-arm version: its `arm_results` has no `zworld_untrained` row and no
  `prev_action_agreement` / `trivial_baseline` fields. A later manifest
  (`..._20260904T183741Z_v3.json`, 4 arms, new criteria) exists and matches the current file.
- The draft queue entry says `conditions: 3`; the current script runs 4 arms.
- The task's "PRE-REGISTERED CONSTANTS" (bar 0.50, elevation over the majority class) are the
  superseded constants; the current file has 0.70 / elevation over max(majority, prev-action) /
  untrained margin 0.10.

## Checked and cleared (no finding)

- **Shortcut via label autocorrelation / last-action leak.** Persistence is 0.57-0.58 and the
  majority-class baseline cannot detect it (a label-MARGINAL statistic is blind to a label-TRANSITION
  statistic; the marginal is near-uniform while the transitions are sticky). The current file now
  elevates over `max(majority, prev_action)` (`_score_cell`, line 1152) and records turn-state
  agreement. The leak pathway into z_world is real but measured inert (0.677 -> 0.677 on scramble),
  and the untrained control shares it.
- **Oracle rule trivially recoverable from few features.** Yes -- argmax over 4 destination cells
  (`capability_eval.py:271-281`) -- so the raw-field control is an easy mapping. But the same
  adapter/dataset/passes learn a fixed random 25->32 tanh re-embedding of the field at 0.95-0.96
  held-out, so an H-C null cannot be explained by "the instrument cannot learn any non-axis-aligned
  mapping at this n". A z_world train/held-out gap (0.83/0.69 untrained) is therefore a property
  of the latent's geometry, which is H-C-consistent, not an instrument artefact.
- **Frozen latent = 978's draw.** `arm_cell` runs `reset_all_rng(seed)` on entry
  (`arm_fingerprint.py:765, 810`); 978 reseeded with the same `seed` immediately before
  `_make_agent` (978 lines 725-728). OFF, ON and UNTRAINED at a seed share one init; the only
  difference is the P0a weight / warmup skipped.
- **Untrained arm vs `assert_no_structurally_unsatisfiable_gate`.** `zworld_encoder_trained_in_p0`
  is scoped to `trained_encoder` (line 597); the untrained arm stays scorable.
- **Standardiser leakage.** Fitted on the train split only; applied identically per arm.
