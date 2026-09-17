# V3-EXQ-1051 REFUSED at /queue-experiment Step 4.5 -- the gain-ladder design cannot adjudicate gradedness

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or whichever registry). No queue entry was added; no script was landed; `ree-v3` is untouched.**

Session `metaworker-science-20260917-mech268-gradedness` (headless), 2026-09-17.
Chip `chip-20260916-mech268-nonsaturating-harm-gradedness-queue`.
Red-team verdict: **BLOCKING** (Opus; the Fable override was rejected on a spend limit, so the
pass re-spawned on the session model per `/queue-experiment` Step 4.5).

This is the THIRD refusal on this item, and the first one that is not about a stale premise --
it is about the ratified design itself. The two user decisions behind it were sound given what
was known at the time; what the red-team found is that the resulting design's criteria are
arithmetic consequences of its own non-degeneracy gate.

## The three decisive findings, each re-verified against source by the authoring session

### F1 (BLOCKING). C1 is ENTAILED by the non-degeneracy gate -- it cannot fail on a gate-green run

`sat_factor = 1/(1 + strength*excess)` with `excess = max(0, n_rec - grace)` bounded to `[0,6]`
at `window=8, grace=2` (`ree_core/cingulate/dacc.py:245-252`). Because every rung of a seed shares
one trained snapshot and one pinned eval env, the excess series is shared, so the adjacent-rung
gap in mean `sat_factor` is a per-observation sum minimised at `excess = 1`:

| adjacent pair | min per-obs gap | max per-obs gap | guaranteed mean gap at interior >= 0.5 |
|---|---|---|---|
| 0.00 -> 0.15 | 0.1304 | 0.4737 | **0.0652** |
| 0.15 -> 0.30 | 0.1003 | 0.1714 | **0.0502** |
| 0.30 -> 0.50 | 0.1026 | 0.1263 | **0.0513** |

The gate (`interior_occupancy >= 0.5`) therefore GUARANTEES every gap `>= 0.0502`, while C1 only
requires `>= 0.03`. C1's failure region (`interior < 0.299`) lies strictly inside the region the
gate already declares red. **The gate excludes exactly and only the runs on which C1 could have
discriminated.**

C3 is worse: `(1 - sat_factor(s))` is strictly increasing in `s` for every `excess >= 1` and
`pe >= 0`, so a single interior observation with positive PE makes `R` strictly increasing; and
`R(S000) = 0` EXACTLY, because `strength = 0` gives `sat == 1.0` bit-identically, so the
`C3_ZERO_TOL = 1e-9` comparison is against an exact zero.

C2 is pinned too: `_apply_arm` writes `dacc_saturation_strength/window/grace` directly onto the
same `DACCConfig` object `_saturation_factor` reads, and the criterion's analytic reference
recomputes the same formula from the same returned `n_rec` -- so `max_abs_sat_fidelity_error` is
exactly `0.0` always. The docstring's claim that C2 catches the c7fc045 propagation gap is FALSE
for this script, which bypasses propagation by setting `DACCConfig` itself.

**Consequence:** the run's only empirical content is whether the live recurrence stream is
non-degenerate -- and the design put that fact in the GATE and filled the CRITERIA with its
arithmetic consequences. The pre-registered null ("a step function on {floor, 1.0} with no
gain-dependence") is not a state the substrate can occupy: `dacc.py:249-252` contains no binary
branch, so the null is refuted by reading five lines rather than by running 15 cells.

### F5 (BLOCKING, and an authoring bug). The interior gate does not catch 729's degeneracy

The gate's description says "strictly between the rung's FLOOR and 1.0"; the implementation counts
`0.0 < s < 1.0`. At `strength=0.5, window=8, grace=2` the floor is `1/(1+0.5*6) = 0.25` -- exactly
the value V3-EXQ-729 was pinned at in all 6x2 cells. A constant series at the floor scores
`interior_occupancy = 1.000` and **passes** the gate. Verified: `[0.25]*270 -> interior 1.000`.

So the gate has ONE working leg (`n_rec_distinct >= 4`), not two -- and the leg that F1's
entailment runs through is the one whose code does not match its own description.

### F2 (CONTESTED, verified). C3 measures the harness multiplying its own two readouts

`pe_post` is computed by the driver as `pe_unsaturated * sat_factor`, not read from the substrate.
The real post-saturation value is already published at `dacc.py:227` / `dacc.py:450`
(`bundle["pe"]`, reachable as `agent._dacc_last_bundle["pe"]`) and the script never reads it. So
"the graded factor reaches the PE readout" is true by construction rather than by measurement.

Worse, the documented action-selection channel is CLOSED in this config: `dacc_weight` defaults to
`0.0` (`ree_core/utils/config.py:3725`) and `DACCtoE3Adapter.forward`'s own docstring states "All
multipliers default to 0, so with default config the bias is the zero vector regardless of bundle
content" (`dacc.py:523-527`). The saturated PE therefore has **provably zero** reach into
`E3.select` via `dacc_score_bias` here.

### F3 (CONTESTED, verified). Every non-scientific failure records `weakens` against MECH-268

`evidence_direction` is set unconditionally to `supports if overall_pass else weakens`, while
`seed_pass` includes the gate and the C2 wiring check. So a red gate or a wiring regression both
record `weakens` -- contradicting the script's own interpretation grid, which routes those to
`/failure-autopsy` and `/diagnose-errors` respectively. The degeneracy net does not rescue it: its
interior floor is `0.01`, fifty times below the gate's `0.5`, so a run with `interior = 0.20` in
every rung records `FAIL / weakens / non_degenerate: true` and is counted by the indexer.

### F4 (CONTESTED, not independently re-verified). No behavioural readout distinguishes the two readings

`sat_factor` reaches behaviour through the salience coordinator (`dacc_pe` input signal) even with
`dacc_weight = 0`. The manifest records no behavioural quantity at all (no return, no
harm-encounter count, no action distribution, no outcome-class sequence; `n_respawns` is computed
and then dropped from the flat readout). If the rungs stayed behaviourally matched the run is a
unit test in an eval loop; if they diverged, C1's gaps mix the gain with a different recurrence
stream. Nothing recorded lets a reader tell which. Cheap confirmer the red-team names: hash
`nrec_series` and the spy's class sequence per rung, and surface `n_respawns`.

## What is and is not salvageable

**Salvageable and verified working** (the machinery is sound; it is the inference that is not):
- The E3 latch fix. Realised period measured 8.57-8.93; the clear-before-call idiom plus
  `n_latched_ticks` works (smoke: 25 fresh, 195 latched out of 220).
- Pinned per-seed eval env (GFLAG-0299 Finding 5) and the shared-snapshot training reuse.
- The `record_outcome` spy installed before the eval loop (GFLAG-0299 Finding 2).
- The regime-conditioned `applies_to` scoping of the interior precondition off the zero-gain rung.
- The empirical ladder itself, which behaves exactly as the arithmetic predicts
  (smoke: 1.0000 / 0.6189 / 0.4739 / 0.3774; R = 0 / 0.4084 / 0.5628 / 0.6649).

**Not salvageable without a new measurement question:** the inference. A gain ladder on a
deterministic arithmetic function, gated on that same function being exercised, cannot
discriminate "graded" from "binary cap" -- because the substrate has no binary-cap branch to
discriminate against. The null is not a state the code can be in.

## What a successor would need to decide (NOT decided here)

The session raised two decision chips on this item already and is not raising a third; per the
campaign brief's "two stops means stop", this is reported instead. The open question is what a
LIVE-LOOP gradedness test could falsify at all, given that `f_sat`'s functional form is fixed in
source. Candidate framings, none ratified:

1. **Make the recurrence stream the measurement, not the gate.** The only contingent quantity is
   the live `n_rec` distribution. A design whose criteria are about THAT -- its shape, its
   dependence on ecology, whether it occupies the graded region under conditions where a binary
   cap would not care -- has something that can fail.
2. **Test the DOWNSTREAM claim instead.** MECH-268 says graded learning-rate ADAPTER. With
   `dacc_weight = 0` nothing downstream is adapted at all. A run with `dacc_weight > 0` measuring
   whether behaviour varies gradedly with the gain would test the registered property rather than
   the arithmetic.
3. **Option C from the prior round, now more attractive:** closure cadence as the ecological dose
   (chip raised separately), which makes the FIFO-clearing mechanism -- the thing actually shown
   to drive interior occupancy -- the manipulation.

## Provenance

- Prior measurement record: REE_assembly `e64d57908f`
  (`evidence/planning/mech268_gradedness_lever_remeasurement_staged_20260917.md`), GFLAG-0327.
- Decisions: `chip-20260917-mech268-gradedness-dose-variable-decision` (Option 1) and
  `chip-20260917-mech268-gradedness-nondegeneracy-gate-decision` (Option A), both user-ratified
  through the Orchestrator decision lane 2026-09-17.
- Authority for the item: CONFIRMED `failure_autopsy_V3-EXQ-729_2026-09-14`, user gate
  2026-09-16T12:08:10Z, applied by governance-20260916 (REE_assembly `db6d20ebee`).
- MECH-268's status is untouched (`provisional`). GFLAG-0299 remains OPEN.
