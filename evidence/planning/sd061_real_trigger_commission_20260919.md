# SD-061 / MECH-343: what a GENUINE stuck-state trigger still needs

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml. It COMMISSIONS work; it does not perform it, and it queues no experiment.**

- Session: `metaworker-science-20260918-sd061-mech343-q056` (headless, ree-cloud-5)
- Written: 2026-09-19T02:32Z
- Authority: user decision 2026-09-19T02:31Z on `chip-20260919-q056-axis-choice-and-dv-reach-decision`
  -- **choice 1 = 1C** (do not queue Q-056 yet; build toward a genuine trigger first)
  and **choice 2 = 2C** (re-scope MECH-343's upstream-leg DV -- a claim-text amendment,
  routed to `/governance`, not done here).
- Substrate read at: ree-v3 `origin/main` (post `f372ce4207`), REE_assembly `origin/master`
- Related: `GFLAG-0352` (SD-061 temperature-lever inertness + absent detector axes),
  and the DV re-scope flag raised alongside this file.
- Prior record: `evidence/planning/exq1056_mech343_q056_upstream_leg_design_refusal_20260918.md`

---

## 1. Where this stands

Three SD-061 gaps were found and closed over 2026-09-18/19, all default-preserving and all
with the full remote suite green (6373 passed, hub, 30m42s):

| | what was wrong | fix | commit |
|---|---|---|---|
| (a) | the regulator's temperature half had no live consumer at any config its design record named | `dgpe_enable_differentiable_cem` + `sd061_temperature_half_inert` diagnostics | ree-v3 `6ba3eb96a1` |
| (b) | 2 of 4 declared detector axes never arrive; `use_dacc=True` is only 1 of 4 conditions | recorded the chain; axis-PRESENCE diagnostics | ree-v3 `6ba3eb96a1` |
| (c) | mean-over-PRESENT silently rescaled the attainable maximum of `stuck_score` | the **declared axis mask** | ree-v3 `f372ce4207` |

**What none of them fixed, and why Q-056 is still not queueable.** The mask makes the
trigger *declarable and attributable*. It does not make it *fire correctly*. Measured on the
baseline ecology (`ree-v3/experiments/_scratch/exq1056_probe7.py`, same seed throughout):

| `declared_axes` | `stuck_score` range | duty(`is_stuck`) | shape |
|---|---|---|---|
| `None` (legacy) | 0.0000 - 0.5000 | 0.000 | never fires |
| `("progress",)` | 0.0000 - 1.0000 | **0.980** | fires, peak on the **last** tick, **never decays** |
| `("progress","margin")` | 0.0000 - 0.5000 | 0.000 | never fires |
| `("progress","difficulty")` | -- | -- | REFUSED after 9 ticks (unwired) |

Only two axis sets are declarable at all, and **neither is a usable trigger, for opposite
reasons**: one never crosses threshold (G9 pole A), the other crosses on 98% of ticks and
never comes back down (G9 pole B). MECH-343 requires a peak that exceeds threshold **and
then decays**; a pinned-high score turns every arm contrast into a DOSE contrast rather than
the TIMING contrast the claim is about.

So there are exactly two things to build, and they are independent.

---

## 2. BUILD ITEM 1 -- an ecology in which goal progress RESUMES

### The defect, stated precisely

`_progress_deficit` measures `max(window) - window[0]` against `progress_stall_eps`. In the
current setup the agent's `goal_proximity` never improves after the opening ticks, so the
deficit saturates at **1.0 and stays there**. With `declared_axes=("progress",)` the evidence
is then a constant 1.0 and the asymmetric EMA (`rise` 0.3 vs `fall` 0.05) climbs to 1.0 and
holds. Nothing in the detector is wrong: it is faithfully reporting an agent that is stuck
and never becomes unstuck.

**MECH-343's leg (c) -- "both decay after goal progress resumes" -- is therefore not merely
unmet but UNMEASURABLE.** There is no resumption to observe. This is an ECOLOGY/CURRICULUM
property, not a detector property, which is why it is a separate build item and not a
parameter change.

### What the build must deliver

1. **A demonstrated resume.** In the ON-ecology, `goal_proximity` must show a genuine
   improvement episode *after* a stall episode, on >= 2/3 seeds -- measured on the agent's
   own `goal_proximity` series, not on an experimenter script.
2. **A duty cycle strictly inside (0.05, 0.80)** for `is_stuck` under
   `declared_axes=("progress",)`. Both poles are live failures here and the interval is the
   one MECH-527's G9 precondition already fixes for this family -- it is quoted, not
   invented.
3. **Peak-then-decay on >= 2/3 seeds**: `detector_peak >= stuck_threshold` followed by a
   fall of at least one `stuck_threshold`-width below the peak within the same episode.
   (This is MECH-343's own "exceed threshold and then decay" made countable. The *magnitude*
   of the required fall is NOT specified by the claim -- see the open question in s.4.)
4. **A negative control**: the goal-salience guard must still hold, i.e. with salience
   withdrawn the detector does not fire in the same ecology. SD-061's existing criterion (4).

### Candidate mechanisms, in the order I would try them

Recorded so the build session does not re-derive; none is pre-registered as *the* answer.

- **(i) A solvable blocked path.** The current `scheduled_action_block` cancels the agent's
  move on a schedule with no way through. A block that *opens* -- a barrier with a period, or
  a detour that becomes reachable -- produces stall-then-resume from the ecology rather than
  from a script. Cheapest, and closest to Q-056's registered "hard-goal / blocked-path
  environment with matched easy-goal controls".
- **(ii) A trained-enough agent.** The stall may be partly competence, not blockage: an agent
  whose `z_world` is a barely-trained projection cannot improve `goal_proximity` reliably.
  A P0/P1 warmup (SD-070 / `zworld_p0_episodes`, the `_train_all_on_agent` family) may
  produce resumption with no environment change at all. **Try this before (i)** -- it is a
  driver change, not a substrate change, and if it suffices then BUILD ITEM 1 needs no
  substrate work at all.
- **(iii) Goal re-targeting.** A goal that moves on attainment gives repeated
  approach/stall/resume cycles within one episode, which is the shape the duty-cycle
  requirement wants. Larger change; consider only if (i) and (ii) fail.

**Do (ii) first and report it**, because it could dissolve this whole item. That ordering is
the single most cost-relevant thing in this document.

---

## 3. BUILD ITEM 2 -- the `diversity` axis, and its MECH-342 dependency

`committed_action_class` is the committed-action-class lock-in axis. It is, per the
2026-09-04 v3closure digestion, one of the **two axes MECH-527 names as the right trigger**
(stall + lock-in), as against the near-tie/ambiguity axes (`margin`, `difficulty`) that the
same analysis says should trigger nothing. So a trigger declared as `("progress","diversity")`
is the theoretically-preferred set -- and it is currently undeclarable.

**Why:** `agent.select_action` derives the class from `e3._committed_trajectory`, which
requires a commitment, i.e. a beta elevation. Measured 2026-09-18: **zero** beta rising edges
over the probe, `mech090_n_elevation_admitted` 0. Beta elevation gates on `_commit_for_beta`
from the E3 natural-commit path -- which is **MECH-342's registered open failure**
("no natural commit when score margins are flat", V3-EXQ-629), a connected failure MECH-343's
own `notes` already cite.

**This item is therefore GATED on MECH-342, not on SD-061.** It should not be attempted as an
SD-061 change. The honest options are:

- **(A) Wait for MECH-342.** Correct but open-ended.
- **(B) Establish whether commitment occurs at all under BUILD ITEM 1's ecology.** A trained
  agent with a resuming goal may commit where an untrained one on a saturated stall does not.
  This is a *measurement*, cheap, and it belongs inside BUILD ITEM 1's run rather than being
  its own job: record `mech090_n_elevation_admitted` and beta rising edges.
- **(C) Declare `("progress",)` only** and accept that MECH-527's preferred two-axis trigger
  is out of reach for now, recording that as a scope limit on whatever Q-056 eventually runs.

**Recommendation: (B) as a free rider on BUILD ITEM 1, then (A) or (C) on what it shows.**
Do not open a MECH-342 work item from here -- that is governance's call, not this file's.

---

## 4. What is NOT decided here, and must not be decided by a build session

Both of these change what gets measured and are therefore user/governance calls:

1. **The magnitude of the required decay** in s.2 item 3. MECH-343 says "exceed threshold and
   then decay" and fixes no number. The "one `stuck_threshold`-width below the peak" above is
   a *proposal*, not a pre-registration. If the build session needs a different figure, that
   is a `kind: decision` chip.
2. **The DV re-scope** (choice 2 = 2C): moving MECH-343's upstream leg (a) from
   candidate-first-action-class entropy to an action-object-space diversity measure. That is a
   **claim-text amendment**, routed to `/governance` via the flag raised alongside this file.
   A build session must not anticipate it by silently measuring the new DV.

---

## 5. Recommended `substrate_queue` entry

Added by this session as a CANDIDATE (`ready: false`) so the IGW routine stages the build as
its own consented chip rather than this session starting it. Severity is recorded honestly:
this is not a corrupting defect in shipped substrate -- SD-061 works as designed and is
default-off -- it is a MISSING CAPABILITY that blocks a registered falsifier.

```
sd_id                : sd061-resume-progress-ecology
severity             : degrading      (blocks Q-056; does not corrupt any shipped path)
ready                : false
substrate_paths      : ree_core/environment/causal_grid_world.py::CausalGridWorldV2.step,
                       experiments/_lib/allon_training.py::_train_all_on_agent
unblocks_claims      : MECH-343, Q-056
depends_on_unresolved: MECH-342 natural-commit failure (V3-EXQ-629) gates the `diversity`
                       axis; the decay-magnitude threshold is unset (s.4 item 1)
```

Full text as landed is in `substrate_queue.json`; this block is the rationale for it.

---

## 6. Provenance of every number in this file

| claim | source |
|---|---|
| duty cycles, score ranges, refusal at 9 ticks | `ree-v3/experiments/_scratch/exq1056_probe7.py`, run 2026-09-19 |
| lever reach ~1.2e-5, action-object only | `ree-v3/experiments/_scratch/exq1056_probe6.py`; contract `C13b` |
| axis presence 100/99/0/0 per 100 ticks | `ree-v3/experiments/_scratch/exq1056_probe4.py` + `exq1056_probe3.py` |
| zero beta rising edges, `mech090_n_elevation_admitted` 0 | `exq1056_probe3.py` |
| suite green 6373 passed | `remote_pytest.sh` on the hub, base ree-v3 `15a1ec35`+uncommitted |
