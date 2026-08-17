# MECH-489 `decision_counts` defect: root cause pinned, and why EXP-0033 is `blocked_substrate`

**Status: DIAGNOSIS COMPLETE (code-verified against `ree-v3` HEAD `f5837e9`). The recommended
substrate amend below is a PROPOSAL for an `/implement-substrate` session, not an applied change.**

**Generated:** 2026-08-17T03:28:54Z
**Session:** `metaworker-chip-proposal-exp-0033` (headless, `chip-proposal-exp-0033`)
**Proposal:** EXP-0033 / `backlog_id` EVB-0610, claim MECH-489
**Substrate entry:** `SD-ORIENTING-DECISION-SCALE` (`substrate_queue.json`, `implemented_pending_validation`)
**Predecessor autopsies:** `failure_autopsy_V3-EXQ-910_2026-08-10`, `failure_autopsy_V3-EXQ-910a_2026-08-11`

---

## 1. Disposition: EXP-0033 is `blocked_substrate`, not queueable

EXP-0033 asks for a `discriminative_pair` run generating decision-grade evidence for MECH-489
before a `2026-08-19T06:13:01Z` deadline. It is auto-generated from backlog signals
(`directional_conflict_alert`, `low_exp_conf`, `mandatory_decision_checkpoint`) and is unaware of
the governance disposition already recorded against this claim four days earlier.

`/queue-experiment` **Step 2.5 (substrate readiness)** stops it, on two independent, already-ratified records:

1. **`claims.yaml` MECH-489 carries an explicit gate.** `pending_retest_after_substrate: true`, with the
   inline reason: *"SD-ORIENTING-DECISION-SCALE amend owed (decision-logging defect,
   severity=degrading) before any further 489 retest is informative."*
2. **The confirmed 910a autopsy explicitly declined to route this experiment.** Its disposition reads:
   *"Routed /implement-substrate (SD-ORIENTING-DECISION-SCALE amend, severity=degrading) for the
   decision-logging defect; **explicitly NOT routing a fresh discriminating experiment until the
   corrected measurement is available**."*

The owed amend has **not** landed. `substrate_queue.json`'s `SD-ORIENTING-DECISION-SCALE` entry is
still `implemented_pending_validation`, and its second `failure_record` entry (the `decision_counts`
defect) is still `"resolved": "open"`. `git log --since=2026-08-11 -- ree_core/agent.py
ree_core/pag/defensive_orienting.py` contains no commit touching this path.

Other gates, checked and **not** the blocker (recorded so a later session need not re-run them):

| gate | result |
|---|---|
| Step 2.5b re-derive brake (MECH-489) | count **0** — both 910/910a autopsies are `recommended_epistemic_category: standard`, not `substrate_ceiling`. Brake does not fire. |
| Step 2.5c substrate-path overlap | `SD-ORIENTING-DECISION-SCALE` is open on `ree_core/agent.py::select_action` at `severity: degrading` → note, not block. |

So the blocker is Step 2.5 specifically: the claim's own substrate gate.

## 2. Root cause, pinned — sharper than the autopsy achieved

The 910a autopsy established *that* `decision_counts` is untrustworthy (sum 206 vs a theoretical max
of `n_overrides x orienting_post_override_bias_ticks` = 21 x 5 = 105, and byte-identical to 910's
total despite half the override count), but stated plainly: **"I could not fully pin the exact
failure mode"** — no per-step episode logs were retained for either run.

It can be pinned statically. Three facts, all verified in HEAD:

**(a) The orienting decision block runs on ~1 env step in 10.**
`REEAgent.select_action` spans `ree_core/agent.py:5815` to beyond 8300 with no intervening `def`.
At `agent.py:6509` it returns the held/stepped action early:
`if not ticks["e3_tick"] and self._last_action is not None:`. The entire orienting override +
decision-persistence block (`agent.py:8100-8254`) is **downstream** of that return.
`heartbeat.e3_steps_per_tick` defaults to **10** (`ree_core/utils/config.py:2564`,
`ree_core/heartbeat/clock.py:52`). So the block executes roughly once per 10 env steps.

**(b) The persistence countdown is measured in E3 ticks, but is written as if it were env steps.**
`_orienting_decision_ticks_remaining` is set to `orienting_post_override_bias_ticks` (**5**,
`config.py:5249`) at `agent.py:8212`, and decremented at `agent.py:8252` — inside the block from (a).
A nominal "5-tick window" therefore spans **~50 env steps**, not 5.

**(c) The driver reads both fields once per env step.**
`experiments/v3_exq_906b_full_stack_observational_fishtank.py:696-708` logs, every env step:
`orienting_override_fired` (from `agent._orienting_last_output.override_fired`) and
`orienting_decision` (from `agent._orienting_decision`). `_decision_alignment` in the 910/910a
drivers then counts both over all steps.

**Consequence — the two counters are inflated by *different* factors, which is exactly the observed
decoupling.** `_orienting_last_output` is **replaced wholesale on every E3 tick** (`agent.py:8160`),
so a single genuine override latches `override_fired=True` for ~10 env steps. `_orienting_decision` is a
**separate variable with its own 5-E3-tick countdown**, so the same override latches a decision value
for ~50 env steps. The predicted ratio is therefore `decision_counts / n_overrides ~ 5`.

Measured: **910 gives 206/42 = 4.90.** The model predicts the headline anomaly to within 2%.
910a gives 206/21 = 9.81, ~2x the prediction — consistent with additional persistence from (d) below,
or with overrides re-arming the window before it expires. *(The exact byte-identical 206 across both
runs remains unexplained by this model alone and is left as an open observation, not a claim.)*

This is a textbook instance of the latched-diagnostic pseudo-replication class already documented in
`/queue-experiment` Step 3.5 ("Sample-size integrity — latched substrate diagnostics"), same
`e3_steps_per_tick = 10` cadence, same read-once-per-env-step shape. That section's warning applies
verbatim here: **"COMMITMENT CONFIG DOES NOT EXCULPATE THIS"** — the inflation is a property of the E3
cadence, not of the beta gate or of commitment configuration.

**(d) A second, independent leak: a `"resume"` decision is permanently sticky.**
Outside `reset()` (`agent.py:3462`), the **only** clear of `_orienting_decision` is `agent.py:8254`,
nested inside a block gated (`agent.py:8226-8231`) on all five of:
`_orienting_decision_ticks_remaining > 0`; `_orienting_decision in ("approach", "withdraw")`;
`_orienting_trigger_z_world is not None`; `len(candidates) > 0`; `all(c.world_states for c in candidates)`.

A `"resume"` decision sets `ticks_remaining = 0` (`agent.py:8212-8216`) and is excluded by the second
condition. It therefore **can never reach the reset** and persists for the remainder of the episode.
Likewise, any tick on which `candidates` is empty or lacks `world_states` freezes the countdown
without clearing the decision, so 5 E3 ticks is a *lower* bound on persistence, not a bound.

**This leak is forward-critical and is the reason it must be fixed before, not after, the retest.**
The retest's entire purpose is to detect a non-degenerate approach/withdraw/**resume** mix. Both runs
to date recorded `resume = 0`, so the leak has never yet fired — it becomes active precisely at the
moment the substrate fix starts working. A retest run against HEAD would therefore corrupt its own
counter *only in the branch that indicates success*, biasing the measurement toward the null in a way
no reader could detect from the manifest.

## 3. Recommended amend to `SD-ORIENTING-DECISION-SCALE` (proposal — for an `/implement-substrate` session)

The defect is split across substrate and driver; both halves are needed.

**Substrate — `ree_core/agent.py::select_action`:**
- Move the `_orienting_decision = None` clear so it is reachable for a `"resume"` decision and on ticks
  where the score-bias gate does not open. Suggested shape: decrement/expire the window in its own
  unconditional step, gated only on `_orienting_decision is not None`, with the score-bias application
  left conditional as it is today.
- Decide explicitly whether `orienting_post_override_bias_ticks` is denominated in **E3 ticks** (current
  behaviour, ~50 env steps) or **env steps** (what its name and the design doc imply), and state it in
  `docs/architecture/sd_orienting_decision_scale.md`. This is a semantic choice, not a bug fix, and it
  changes behaviour — so it belongs to whoever owns the design, not to a measurement repair.

**Driver — the 910-lineage `_decision_alignment`:**
- Count the decision **at the override tick only**, in the same synchronous block that increments
  `n_overrides` — the readout the 910a autopsy already identified as trustworthy ("set once,
  synchronously, in the same `if _do_out.override_fired:` block"). This yields exactly `n_overrides`
  classifications and is immune to (a), (b) and (d).
- Emit `n_latched_ticks` alongside the row count, per the `/queue-experiment` Step 3.5 convention, so
  the true denominator is auditable rather than inferred from `len(rows)`.

A retest queued **after** both halves land is informative; one queued now is not, which is the
disposition the 910a autopsy already reached and this document confirms with a pinned mechanism.

## 4. Note on the `blocked_substrate` writeback

`build_experiment_indexes.py:6279-6293` carries forward a **whitelist** of fields for any proposal whose
status is not `"proposed"`: `status`, `executed_by`, `executed_queue_id`, `gated_at_utc`,
`gated_by_session`, `gating_reason`, `predecessor_disposition`, `release_condition`, `superseded_by`.

`blocked_by` and `blocked_note` — the two fields `/queue-experiment` Step 2.5 instructs an author to
write — are **not on that list**, so they are wiped on the next governance regen, leaving a
`blocked_substrate` status with no recorded reason. (This is visible in the existing corpus: EVB-0579
is `blocked_substrate` and carries neither field.) EVB-0610 has therefore been written with **both**
the skill-prescribed fields (for an immediate reader) **and** the persisting `gating_reason` /
`release_condition` / `gated_at_utc` / `gated_by_session` fields, so the reason survives regen.

The skill/indexer mismatch itself is chipped separately.
