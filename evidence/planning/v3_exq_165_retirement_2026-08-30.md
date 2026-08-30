# V3-EXQ-165 dormant driver: RETIRED, not the MECH-144 retest vehicle

**Date:** 2026-08-30T08:58:43Z
**Session:** sci-c4-exq165-20260830 (chip-20260830-exq165-dormant-driver-decision)
**Decision:** RETIRE. Do not queue. Do not letter (`V3-EXQ-165a`).

## Context

Governance's 2026-08-30 Step 3 agenda (cycle governance-20260830-0630) named the dormant
`ree-v3/experiments/v3_exq_165_mech143_hippocampal_value_sensitivity.py` driver "the natural
vehicle" for a properly-powered MECH-144 retest, sequenced after
`chip-20260830-singleton-group-degeneracy-guard` (now landed: `ree-v3` `bad6467722`). This chip
was spawned to make that call after reading the driver in full. The call is RETIRE.

## What the driver actually does

`v3_exq_165_mech143_hippocampal_value_sensitivity.py` is a **standalone analog**: an inline 8x8
grid world and a hand-written `HippocampalTerrainNavigator` class, sharing no code with
`ree_core`. Its own docstring says so explicitly ("Inline 8x8 grid world (no ree_core agent
imports)"). It has run twice already (`f3319520`, `d2d314a9`, both 2 seeds, both `outcome=FAIL`,
`evidence_direction` "mixed"/"inconclusive") and both are already excluded from MECH-144's
scoring evidence.

## Why it structurally cannot inform the MECH-144 question, at any seed count

The `HippocampalTerrainNavigator.propose_action()` computes its action purely from
`residue_field` (accumulated harm) and Manhattan distance to the chosen goal position. It never
receives, and structurally cannot receive, the goal's *reward value* — the docstring is explicit:
"Does NOT receive or use reward values -- only goal positions." Both the `FIXED_VALUE` and
`SHUFFLED_VALUE` conditions run the *same* value-blind navigator; only a separate
`goal_selection_head` (deliberately reward-sensitive, by design) picks which goal to walk toward.

Consequence, verified against both existing manifests: criteria C1 (harm-rate diff), C2
(completion-rate diff), and C3 (post-shuffle harm spike) all **passed** on both runs
(`criteria_met: {"C1": true, "C2": true, "C3": true, "C4": false}`). The only failure was C4, a
data-quality gate (`n_shuffle_events > 4` per seed) that sits *exactly* at its own binomial
expectation (`K_SHUFFLE=50`, ~8 checkpoints over 400 episodes, `p=0.5` per checkpoint ->
`E[shuffles] = 4`) — a coin-flip-fragile threshold that happened to land on the wrong side of
its own strict inequality on both prior seeds. That is a second, independent design flaw (never
calibrated against measured baseline noise), but it is not the load-bearing one.

The load-bearing problem: by construction, the terrain-navigation component being scored
**cannot exhibit value-sensitivity**, ever, regardless of statistical power. Raising seed count
would only sharpen an already-foregone C1-C3 PASS into statistical significance — it would
harden the confirmation of MECH-143 (which has no lit conflict and doesn't need it) while
remaining permanently unable to produce `PARTIAL_VALUE_SENSITIVE`/weakens evidence for MECH-144,
because there is no code path through which the scored navigator could ever behave in a
value-sensitive way. A "properly-powered retest" on this design is not a retest of the
MECH-143-vs-MECH-144 question; it is a higher-N re-confirmation of a tautology.

This also means the driver cannot detect the failure mode that would make MECH-144 *true* in the
live substrate: implicit value leakage into computation that is supposed to be value-flat. This
codebase has a documented precedent for exactly that failure mode (SD-016/MECH-151: cue-context
leaking into supposedly value-independent action-object scoring). A hand-rolled navigator that
never receives value as an input parameter cannot leak it, so it cannot surface that mechanism
either.

Separately, and consistent with the above: the driver exercises none of `ree_core` (no
`HippocampalModule`, no `E3TrajectorySelector`, no `REEAgent`). ARC-007 STRICT is a claim about
those components; a parallel hand-written navigator can confirm only that the *experimenter's own
value-blind design* behaves as designed, not that REE's actual trajectory-proposal machinery is
value-flat under a value-value shuffle.

## Why "letter it" (V3-EXQ-165a) does not fix this

Per `CLAUDE.md`'s EXQ versioning convention, a letter is for a bug fix to the same scientific
question; a new number is for a different question or a substantially different design. Making
this driver capable of producing genuine MECH-144 evidence requires giving the scored
terrain-navigation component a value-sensitive code path to contrast against the value-blind one
— that is not a bug fix, it is a different experimental design. It would need a new EXQ number,
not a letter, and is out of scope for a "fix the dormant driver" decision.

## Right vehicle for the MECH-144 retest (not built here)

A properly-powered MECH-144 retest should probe **ree_core's actual substrate**, not a parallel
implementation:

- Build a `REEAgent` (or drive `HippocampalModule.propose_trajectories()` /
  `E3TrajectorySelector` directly) against a `CausalGridWorldV2`-style environment with the same
  FIXED_VALUE vs SHUFFLED_VALUE goal-value manipulation this driver used.
- Measure whether the *real* candidate-trajectory scoring / terrain preference (z_world-based CEM
  candidate evaluation, not a hand-coded Manhattan-distance navigator) shows sensitivity to
  shuffled goal values — i.e., test for the value-leakage failure mode directly, on the substrate
  where it could plausibly occur.
- Use enough seeds to clear the repo's standing effect-size convention (PASS margin scaled on the
  SD of the delta, plus an absolute floor), not the 2-seed count this driver used.
- Derive any data-quality/reachability threshold (analogous to the old C4 shuffle-count gate)
  from a measured baseline run, not from the criterion's own theoretical expectation — the C4
  gate here is a worked example of the mistake to avoid (`failure_autopsy_V3-EXQ-936a_2026-08-30.md`
  Section 7: "criterion reachability must be derived from the current regime").
- Feed any per-seed/per-condition grouping into non-degeneracy checks (e.g.
  `metric_groups_are_degenerate`) with arity >= 2 per group, per the now-landed singleton-group
  arity guard (`ree-v3` `bad6467722`) — this driver itself never called that function, so it
  carries no singleton-group risk to inherit, but a fresh design must not introduce one.

This is a new design (new EXQ number), scoped for a future `/queue-experiment` session — not
performed in this chip, which is scoped to the queue-or-retire decision only.

## Action taken

`ree-v3/experiments/v3_exq_165_mech143_hippocampal_value_sensitivity.py` marked `RETIRED -- DO
NOT REPAIR` in its module docstring (the existing codebase convention, e.g.
`v3_exq_263_mech216_e1_predictive_wanting.py`), pointing back to this document. The file is left
in place (not deleted/moved) so existing evidence manifests (`f3319520`, `d2d314a9`) that
reference it remain traceable, and so `autopsy_pre_routing_checks.py` and similar tooling can see
the retirement banner rather than re-flagging a silently-vanished script.

No experiment was queued. `ree-v3/experiment_queue.json` was not touched (a concurrent session,
`fable-autopsy-936a-20260830-pause`, held an active claim on it for the V3-EXQ-936a autopsy at
the time this decision was made).
