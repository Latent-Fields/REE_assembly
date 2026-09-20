# INV-063 leg A: its three registered DVs are transforms of the quantity P1 gates on

**Status: AWAITING USER REVIEW. Nothing here has been written to claims.yaml or any other
registry. The four-arm ladder was NOT queued. `V3-EXQ-1071` is reserved, its driver is
written and landed on `origin/main`, and it is NOT in the queue.**

- Session `metaworker-science-20260919-inv063-four-arm-intake-ladder`, 2026-09-20.
- Found by the mandatory Step 4.5 red-team (fable 5.1, foreground), verdict **BLOCKING**,
  then verified against source before acting.

---

## 1. The finding

INV-063's C1 leg A names three DVs verbatim: "the count of VALENCE_SURPRISE residue writes
per waking period and the realised `surprise_weight` at the replay call fall monotonically
with intake, and the replay start-selection distribution collapses toward uniform".

**All three are transforms of `e3_prediction_error` -- which is exactly the scalar P1's
manipulation check (MEL) is computed from.** Verified:

1. `agent.py:10902` -- `metrics.update({f"e3_{k}": v for k, v in e3_metrics.items()})`. So
   the driver's MEL, `metrics["e3_prediction_error"]`, **is** `e3_metrics["prediction_error"]`.
2. `agent.py:10985-10987` -- MECH-205 reads that same `e3_metrics["prediction_error"]` and
   maintains `_pe_ema = (1-alpha)*_pe_ema + alpha*pe_mag`. So `_pe_ema` is an EMA of MEL.
3. `agent.py:10812-10814, :10848` -- **A2** `= drive_state[VALENCE_SURPRISE]
   = min(1.0, _pe_ema * 5.0)`. A2 is a monotone transform of EMA(MEL).
4. `agent.py:10988-10991` -- **A1** increments when `pe_mag - _pe_ema > pe_surprise_threshold`
   (1e-5, `config.py:3692`). A threshold-count of MEL against its own EMA. `agent.reset()`
   zeroes `_pe_ema` each episode, so within a 90-step episode the count is level-driven; and
   V3-EXQ-1069's landed MELs are 1.6e-5..4.3e-5, i.e. 1.6x-4.3x that threshold -- precisely
   that regime.
5. `config.py:3842-3843` -- `valence_harm_enabled` and `valence_liking_enabled` are both
   False by default and are not set by 798a's `_make_agent`, so **VALENCE_SURPRISE is the
   only valence channel written in this run**. **A3**'s priority is
   `dot(evaluate_valence(z), drive_state)`, whose surprise weight *is* A2 -- so A3 carries A2
   multiplicatively. The smoke magnitudes agree (A3 ~1e-9 ~= A2 1e-4 x surprise 1e-5).

## 2. Why that is blocking rather than merely inelegant

- **C1 leg A is P1 re-read.** P1 already requires MEL monotone across the arms. A monotone
  A1/A2/A3 follows up to sampling. A confirmed C1 leg A would be attributable to the
  manipulation check, not to starvation of offline function.
- **C2 -- the load-bearing knee -- becomes a test of MEL rung SPACING.** P1 constrains
  monotonicity and total spread; it says nothing about spacing. So C2 on leg A asks whether
  the interval values {10, 25, 60, 0} happen to be spaced with a bigger MEL step at the low
  end. Under either outcome nobody can say whether "offline function has a floor" or
  "interval 60->0 is a bigger MEL step than 10->25".
- **The reviewer's arithmetic on V3-EXQ-1069's LANDED MELs makes this concrete**: applying
  this script's own `_knee` rule to raw MEL already yields knee=True on seed 456 (excess
  9.6e-6 against a 9.4e-6 margin) and False on 42/123. The knee pattern exists in the
  manipulation check before any DV is read.

**This is a property of the REGISTERED claim text, not of the implementation.** The driver
measures exactly the three quantities INV-063 names. So the remedy is registry-side and is
/governance's and the user's, not mine -- which is why this is a stop rather than a fix.

## 3. Three further defects, all MINE and all fixable, recorded so they are not lost

They are moot while (1) stands, but whoever resumes should not have to re-find them.

- **The two registered P1 sub-controls are computed and never gated.** INV-063's P1 requires
  that "elevated PE must DECAY within a stationary window" and that "a matched-PE
  observation-noise arm must NOT reproduce the DV pattern -- otherwise the ladder is grading
  noise". The driver records `pe_decay_within_stationary_window` and
  `noise_arm_at_least_as_elevated_as_high` but neither reaches `gating_ok`, the criteria, or
  the label branch. **And the smoke shows both would fire**: the noise arm's A3 (1.46e-8)
  EXCEEDS the HIGH arm's (4.06e-9) at lower MEL, and `decay` is -5.45/-5.17, i.e. PE RISES
  in the stationary window. A verdict could be emitted with the claim's own grading-noise
  condition satisfied and unreported.
- **The refusal route is an all-four-arms AND.** `legb_all_negative = all(v < 0 ...)`, so one
  arm at >= 0 disables it and C1 leg B then routes to `F1_flat` / `weakens` -- the exact
  false F1 the route was ratified to prevent. Conversely a marginally positive HIGH arm with
  three negative arms in monotone order can reach F2/confirmed while sleep degrades the
  readout in 3 of 4 arms.
- **`need` is computed from `len(seeds)`, not scored seeds**, while the P1 gate passes at
  >= 1 seed. With one P1-passing seed the run proceeds and `n_monotone >= 2` is
  unsatisfiable, so the manifest carries `F1_flat` / `weakens` / "genuinely falsified".
  `non_degenerate` is False so the indexer excludes it from scoring, but the label and note
  contradict the docstring's "scores nothing".

Also noted, coverage not design: the `--dry-run` budget ends exactly at ARM_1_LOW's first
rule shift, so LOW is bit-identical to NONE in the smoke and only a three-rung ladder is
exercised.

## 4. Options

**(a) Re-specify leg A's DVs so they are not functions of MEL** -- a claims.yaml amendment,
so /governance's. The claim's own leg-A intent is "surprise-gating has nothing left to
prioritise", which wants a SELECTIVITY measure rather than a LEVEL one: e.g. the *share* of
replay starts captured by the top-priority bin, or the rank correlation between replay
priority and episode PE, both of which can fall while MEL rises. Not derivable from the
registered text -- hence this stop.

**(b) Run leg B alone** and drop leg A from C1/C2. But the tau bind (GFLAG-0382) already
leaves leg B liable to the `leg_b_dv_sign_inverted` refusal, so this likely yields no verdict
at all.

**(c) Convert INV-063 to `substrate_conditional`** via its own escape hatch. Four independent
measured preconditions have now failed: leg B's MSE readout degrades across sleep; the
InfoNCE readout trades headroom against direction with no overlap; P1 holds on only 2/3
seeds; and leg A's DVs are not independent of P1. The claim's text already calls this
conversion "a legitimate, useful outcome".

**(d) Run it anyway** and read leg A as a manipulation-spacing result, stating the
circularity in the manifest. Cheapest, and the least informative.

**Recommendation: (a) if INV-063 is to survive as a testable invariant, (c) otherwise.** I do
not recommend (d).
