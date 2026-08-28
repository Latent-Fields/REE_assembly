# MECH-357 trajectory reanalysis -- WHY no pressure design ever reintroduces the Pavlovian-instrumental conflict

**Date:** 2026-08-28
**Session:** `metaworker-chip-20260827-mech357-trajectory-reanalysis` (headless, ree-cloud-5)
**Owns:** the zero-compute reanalysis substrate_queue entry `mech357-freeze-incompatible-pressure-mechanism`
(status `validated_negative`) names as the required precondition before any further pressure
mechanism is opened.
**Changes no claim status, confidence, `epistemic_category`, `evidence_direction`, or
`substrate_queue.json` field.** Reads already-recorded data and already-committed source code
only -- zero new compute, no code change, no queue entry. Explicitly routed as a proposal for
`/governance`.

---

## 0. This chip is NOT a stale duplicate -- what it adds beyond what already exists

`chip-20260827-mech357-trajectory-reanalysis` was flagged by
`failure_autopsy_V3-EXQ-603v_2026-08-28.md` SS"Read-across" as "appears to be an open stale
duplicate of the completed reanalysis" (`mech357_h2_graded_dv_reanalysis_2026-08-25.md`). That
hedge is checked here and does not hold, for a reason the autopsy itself half-states: the H2
reanalysis (2026-08-25) found the reversed-sign discrimination but explicitly left the causal
question open, naming two candidate stories, **neither tested**. The 603v autopsy (2026-08-28)
then reported new data -- G_H survival dropped 3/3 -> 2/3 post-fix with the trace live through
scoring -- that **weakens** the first of those two candidate stories, but the autopsy explicitly
declines to adjudicate further ("flagged for governance, NOT adjudicated here"). So as of this
session's start, the WHY question this chip's brief asks has a reanalysis that found the
*effect* (H2) and a diagnostic run that further constrains it (603v), but no synthesis that
actually answers it. This document is that synthesis, and it adds one new load-bearing
ingredient neither prior artifact used: **a direct read of the environment's harm-contact code**
(`ree-v3/ree_core/environment/causal_grid_world.py`), which turns out to settle the question
without needing new compute.

---

## 1. Verdict in one paragraph

**None of the four pressure-mechanism designs (static field 603h/603r, mobile-predator drift
603s, scheduled discrete adjacency 603t, agent-directed pursuit 603u at directedness 0.9) could
ever have made LESION's freeze/no-op policy costly, because the environment's dominant harm
channel (`contact_harm`, default 0.5 per event) fires only when the AGENT's own step lands on a
hazard's cell -- and hazards are structurally blocked from ever moving onto the agent's occupied
cell** (`_drift_hazards` only advances a hazard into a grid cell typed `"empty"`; the agent's cell
is permanently typed `"agent"` while occupied). Freeze is implemented as action index 4, `(dx,
dy) = (0, 0)` -- a literal no-move -- so a frozen agent's own step always re-evaluates its
*current* cell, which by the same invariant can never be typed `"hazard"`. **A perfectly frozen
agent cannot take a `contact_harm` hit, in any of the four pressure designs, at any hazard
density or pursuit-directedness setting**, because none of those parameters touch the one
invariant that matters (hazards cannot occupy the agent's cell). The only channel a frozen agent
is exposed to is `proximity_harm` (scale 0.1 in 603u, evaluated softly off the diffused
`hazard_field` value at the agent's current cell each tick) -- roughly 5x smaller per-tick than a
single contact event and requiring sustained close range to matter. Meanwhile the gated arms
(INTACT/POSCTRL) are the ones being *forced to move* (freeze-suppression + action-bias,
especially early in Stage-H when the protective-scaffold floor is high) -- movement is exactly
what exposes an agent to the one channel capable of a fast kill. **The pressure-mechanism family
was pressing on a parameter (hazard proximity/pursuit intensity) that cannot make freezing
costly by construction, while the mechanism itself imposes a real per-step movement-contact
risk on the arms it is supposed to protect.** This is sufficient, on its own, to produce the
reversed-sign result the H2 reanalysis found (gated arms surviving *shorter*, not longer) and to
explain why escalating pursuit aggression four times running never budged `G_H_LESION_frac` off
the ceiling.

---

## 2. The code trail, with line references

All in `ree-v3/ree_core/environment/causal_grid_world.py` (the shared engine behind both legacy
and `CausalGridWorldV2` mode -- confirmed by grep: there is exactly one class, `CausalGridWorld`
at line 90; "V2" names `use_proxy_fields=True` mode of the same class, not a subclass. Stage-H's
`_build_env(phase="hazard")` in `scaffolded_sd054_onboarding.py:2602` constructs this same class
for all three arms in every one of 603h/k/r/s/t/u).

1. **Action space** (`:113-115`): `ACTIONS = {0: (-1,0), 1: (1,0), 2: (0,-1), 3: (0,1), 4: (0,0)}`
   -- index 4 is the literal stay/no-move action, distinct from the four directional moves.
2. **Freeze IS this action** -- `infralimbic_avoidance_gate.py:109`: "The passive / no-op action
   class index (matches MECH-279 / MECH-320)." MECH-279's freeze default and MECH-357's
   suppression target are both defined against this same no-op class; the gate's whole job
   (`:28-32`) is to override "the MECH-279 freeze no-op" with an instrumental action instead.
3. **`step()` movement resolution** (`:2299`): `dx, dy = self._action_map[action]`; for action 4,
   `dx=dy=0`, so `new_x, new_y = self.agent_x, self.agent_y` (`:2301-2306`) -- the agent's step
   re-evaluates its own current cell.
4. **Contact harm is keyed on the destination cell's type** (`:2393-2411`): `target_type =
   self.grid[new_x, new_y]`; `contact_harm` (constructor default `hazard_harm=0.5`, `:139`) fires
   only `if target_type == self.ENTITY_TYPES["hazard"]`. For a frozen agent, `new_x, new_y` is its
   own cell, whose grid type is `ENTITY_TYPES["agent"]` (`:1550`, `:1857`, `:1988`, `:2660`),
   never `"hazard"` while occupied.
5. **Hazards cannot move onto the agent's cell** (`_drift_hazards`, `:5015-5081`): every candidate
   direction is filtered by `self.grid[nx, ny] == self.ENTITY_TYPES["empty"]` (`:5065`,
   `:5075`) before a hazard is allowed to step there. The agent's occupied cell is never typed
   `"empty"`, so this is an unconditional block -- confirmed independent of `hazard_agent_pursuit`
   (`:5050-5056`, which only *biases the ordering* of candidate directions toward the agent, not
   whether the occupancy check is honoured) and independent of `env_drift_prob` (which only gates
   *whether* a hazard attempts to move at all this tick, `:5033`).
6. **The only channel left is proximity harm**, evaluated at the agent's own cell when
   `transition_type == "none"` (`:2485-2509`): `harm_signal = -proximity_harm_scale *
   hazard_field[new_x, new_y]`. In 603u's config this scale is 0.1 (vs. `contact_harm=0.5` plus
   its own additive proximity term, `:2396-2401`) -- a single contact event is worth roughly 5+
   ticks of maximum-field proximity exposure, and the field value at any one cell is rarely
   saturated (it is a diffused gradient, not a binary "hazard here" flag).
7. **Episode termination** (`:3121-3123`): `done = (agent_health <= 0.0) or (steps >=
   max_episode_steps)`. `agent_health` starts at 1.0 (`:1548` etc.) and only decreases via the
   two harm channels above. There is no other way to end an episode early.

Net: for the frozen/LESION policy, the *only* route to `agent_health <= 0` before the 200-step
cap is the soft proximity channel, which requires many consecutive close-range ticks; the fast,
decisive route (two `contact_harm` hits) is structurally unreachable while stationary, in every
one of the four pressure designs, because none of them touch the occupancy-block invariant.

---

## 3. Cross-check against the already-recorded per-episode data

This reproduces the shape already reported by `mech357_h2_graded_dv_reanalysis_2026-08-25.md`
(SS2-SS3 there; not re-derived from scratch here, cited for continuity) and reads it through the
mechanism above rather than leaving it unexplained:

- **LESION mostly survives near the 200-step ceiling** across 603s/603t/603u (whole-run means
  107-151 in 7 of 9 cells) -- consistent with a policy that is rarely forced to move into
  hazard-occupied cells, so it rarely pays the fast `contact_harm` route. LESION is not immune
  (2 of 9 whole-run cells drop into the 6-107 range, and several last-10-window cells collapse to
  5-6 steps) -- consistent with an occasional blunder (LESION still moves under its own
  non-gated policy some of the time; freeze is a threat-triggered response, not a permanent
  state) landing directly on a hazard cell, which the fast contact route punishes hard (a 5-6
  step death matches roughly one contact event, not a slow proximity bleed, which would take on
  the order of 10+ ticks at max field value to zero out health from 1.0).
- **INTACT/POSCTRL survive *shorter*, not longer**, in 16 of 18 pre-fix cells and 6 of 6 whole-run
  averages (H2 SS2-SS3) -- consistent with the freeze-suppression + action-bias forcing these
  arms into more directed movement, especially during the early Stage-H episodes when the
  protective-scaffold floor (`floor_start` toward `floor_end`, annealing across the 40-episode
  budget, `scaffolded_sd054_onboarding.py:2635-2648`) keeps `effective_efficacy` artificially
  high and suppression near-total before the policy has learned safe navigation. Every
  suppressed freeze is a forced step into an unlearned action distribution, i.e. a real per-tick
  chance of stepping onto one of `num_hazards=4` cells that a stationary agent would never have
  risked.
- **V3-EXQ-603v (2026-08-27/28) does not rescue this story, and helps rule out the H2 doc's own
  first candidate explanation.** The H2 doc's causal story (a) was "the gated arms pay an early
  cost for a mechanism that has gone numerically extinct by the scoring window" -- i.e., the
  damage is done early, then the (dead) mechanism no longer even tries to help. 603v repaired
  the eligibility trace (learned `avoidance_efficacy` now holds non-trivial last-10-window
  medians of 0.494 / 0.924 / 0.033 across seeds, no longer numerically extinct) and reran the
  identical Stage-H config. If story (a) were the whole explanation, a *live* trace through
  scoring should recover some of the deficit. Instead **G_H survival dropped further, 3/3 -> 2/3,
  with the highest-trace seed (43) collapsing to ~6-step episodes** (autopsy SS"Facts"). This is
  exactly what the movement-exposure mechanism above predicts and the extinct-mechanism story
  does not: a *working* gate is not obviously protective in an environment where movement itself
  is the dominant risk, and can still net negative, because every suppressed freeze remains a
  real per-tick contact-risk roll regardless of whether the trace behind it is alive or dead.

---

## 4. Discriminating the three candidate answers named in the task brief

**(a) "Freeze is never the lesioned agent's dominant response in this env class, so
freeze-incompatible pressure has nothing to suppress."** -- Not quite as literally stated
(readiness checks across 603s/t/u report `pag_freeze_lesion_frac=1.0`, i.e. freeze *does* fire on
LESION), but the underlying intuition is correct and now has a specific mechanism: freeze does
not need to be LESION's *dominant* response to make freeze-incompatible pressure ineffective --
it only needs to be **cheap** in this environment, and it structurally is, regardless of how
often it fires, because the harm model cannot punish immobility through its dominant channel.
Reframe as: **freeze is not costly here, not because it is rare, but because the environment
makes it (near-)costless by construction.**

**(b) "The G_H readout itself is the wrong frame."** -- TRUE, and independently confirmed by the
already-completed H2 graded-DV reanalysis (median-of-10 ceiling saturation at exactly 200.0 in
21 of 27 arm-seed cells hides real, gradedstructure). This is a real, compounding confound, but
it is not the *root* cause: a perfect graded DV would still show the reversed-sign effect,
because the effect is mechanistic (movement risk), not a measurement artifact. Fixing the DV
alone (episode_lengths persistence for all arms, the amendment the 603v autopsy already names as
owed) would make the existing effect legible, not change its sign or its cause.

**(c) "A measurable precondition is never met."** -- **CONFIRMED, and now specifically named**:
the precondition is *hazard-initiated contact with a stationary agent*, and it is unmeetable by
any parameter combination in the current environment code -- not a tuning problem, a structural
one. `hazard_agent_pursuit` (0.0 -> 0.9 across the four designs) only biases which direction a
hazard *attempts* to drift when its per-tick `env_drift_prob` roll succeeds; it cannot lift the
occupancy-block invariant (`:5065`/`:5075`) that keeps hazards off the agent's own cell. A 5th or
6th pressure-mechanism attempt at any magnitude would hit the identical wall, which is
independent confirmation of the same refusal the 603u autopsy already gave a 7th
same-question pressure recalibration ("a pressure increase cannot fix the efficacy underflow" --
true of the efficacy underflow, and, this document adds, equally true of the discrimination
target itself for a different, structural reason).

---

## 5. What this does and does not settle

**Settled, by direct code inspection (zero compute, zero uncertainty from noise or seed
variance):** the four already-tried pressure-mechanism designs could never have produced
freeze-incompatibility, because none of them can alter the one invariant (hazards cannot occupy
the agent's cell) that makes freeze cheap. This is a **probe-gated question converted to known
data / known rules** -- it did not need a fifth experiment to answer, it needed a read of
`_drift_hazards` and `step()`, which this session did.

**Not settled here, and explicitly a governance/design call, not this session's to make:**
- **Whether to fix the environment or reframe the claim's test.** SS6 below lays out both options
  as a proposal; this document does not choose.
- **Whether 603s/603t/603u's `evidence_direction` should be re-read as `weakens`.** The 603v
  autopsy already flagged this as owed to governance and this document does not re-litigate it,
  but does supply the missing causal account the autopsy said was needed to close it: the
  reversed-sign effect is not noise and not an artifact of the (also real) DV-saturation
  confound -- it has a specific, code-verified mechanism, which should weigh toward `weakens`
  being the more accurate read of what these runs actually showed (a real, reproducible
  behavioural cost of the suppression mechanism as currently scaffolded) rather than
  `non_contributory` (implying the runs showed nothing).
- **Whether this generalises beyond Stage-H's specific `CausalGridWorld` harm model.** This
  session did not check whether P1/P2 (the later, non-isolated curriculum phases) or any other
  environment class in the substrate implements hazard contact differently (e.g. a design where
  hazards CAN occupy the agent's cell, or where a co-location check runs independently of either
  party's last move). If such an environment already exists elsewhere in the substrate, it would
  be a much cheaper fix than modifying `causal_grid_world.py` -- worth a governance-directed
  grep before committing to option 1 in SS6.

---

## 6. Recommendation

**Reframe MECH-357's fair test; do not queue a further pressure-mechanism magnitude increase.**
The existing refusal of a 7th same-question pressure recalibration (603u autopsy) already covers
this, and SS4(c) above gives it a second, independent, structural reason: no pressure-mechanism
parameter in the current environment code can ever make freeze costly, so escalating any of them
further is not merely unlikely to work, it is provably incapable of working.

Two live options for the next `/governance` cycle to weigh (not act on here):

1. **Environment-mechanism fix (buildable, small, well-scoped).** Add a symmetric contact check:
   when `_drift_hazards` (or a new post-drift pass) finds a hazard's new position coincides with
   the agent's current position -- or, more conservatively, add a passive "hazard adjacent for N
   consecutive ticks" lethality channel distinct from the diffused proximity-field trickle -- so
   that a genuinely immobile agent is not structurally safe. This is `complicated (buildable)` in
   the CLAUDE.md vocabulary: the mechanism (occupancy-blocked drift) is fully understood, and the
   fix is a few lines in `_drift_hazards`/`step()`, gated behind a new no-op-default flag so every
   existing recorded run stays bit-identical. This is the only route that lets the *original*
   pressure-mechanism family (density, drift probability, pursuit directedness) actually mean
   what the paradigm needs them to mean. A retest under this fix would need: (i) this env change,
   (ii) the already-fixed eligibility trace (603v, landed), (iii) the graded scoring-window DV
   (proven workable by the H2 reanalysis) rather than the saturating median gate, (iv)
   `episode_lengths` persisted for all three arms (the 603v autopsy's already-named amendment,
   currently missing for LESION) so the comparison is symmetric. This is exactly the retest shape
   the 603v autopsy's own routing already sketches ("NEW letter combining... a restored ARM_LESION
   comparator"); this document supplies the reason (i) is a needed addition to that list, not
   optional.
2. **Route to demotion / claim-level reframing**, if governance judges the environment fix is out
   of scope or not worth building: record that MECH-357's survival prediction cannot be fairly
   tested in the `CausalGridWorld` Stage-H harness as currently specified (freeze is structurally
   near-costless there, independent of the mechanism under test), and either find or design a
   different environment where hazard lethality is not movement-gated before attempting another
   discrimination run. `pending_retest_after_substrate`'s blocking dependency would then be an
   **environment precondition**, not a mechanism-engagement or eligibility-trace precondition.

This document's preference, stated but not acted on: **option 1** is small, well-scoped, and
directly addresses the actual gap (the pressure-mechanism family was aimed at the wrong lever)
rather than abandoning six runs' worth of curriculum/scaffold investment. But this is a design
judgment call for governance/`/implement-substrate` scoping, not a zero-compute-reanalysis
verdict -- flagged as a proposal only.

---

## Provenance

- **Zero new compute.** No experiment run, no queue entry, no dry-run.
- **Files read:** `ree-v3/ree_core/environment/causal_grid_world.py` (constructor defaults,
  `ACTIONS`, `step()` ~2240-2520, `_drift_hazards()` ~5015-5081, termination ~3121-3123, entity
  types ~90-128) -- the new ingredient this session adds; `ree-v3/ree_core/pfc/
  infralimbic_avoidance_gate.py` (freeze/no-op class cross-reference, ~1-260);
  `ree-v3/experiments/scaffolded_sd054_onboarding.py` `run_hazard_avoidance()` (~2530-2709,
  scaffold-floor anneal) and `_build_env()` (~1729-1780); the three flat manifests
  `v3_exq_603{s,t,u}_..._v3.json` (config blocks, confirming `env_drift_prob=0.6`,
  `hazard_agent_pursuit=0.9`, `num_hazards=4`, `proximity_harm_scale=0.1` for 603u);
  `mech357_h2_graded_dv_reanalysis_2026-08-25.md` (full, cited not repeated for SS2-SS3 numbers);
  `failure_autopsy_V3-EXQ-603v_2026-08-28.md` (full, the 3/3->2/3 finding and its read-across);
  `docs/claims/claims.yaml` MECH-357 entry (current note history, as of governance commit
  `5444c5cdb0`, read via `origin/master` -- this box's local `REE_assembly` checkout was 127
  commits behind origin at session start and was not disturbed; all reads in this document are
  via `git show origin/master:<path>`, never a local reset).
- **Files deliberately NOT written:** `docs/claims/claims.yaml`, `evidence/planning/
  substrate_queue.json`, `TASK_CLAIMS.json` (status field), any experiment manifest, any
  `ree-v3` code. This session does not set `epistemic_category`, `evidence_direction`, or
  `diagnostic_evidence_adjudicated`, and does not queue a new experiment.
- **TASK_CLAIMS:** opened under this session's own id, covering this plan doc, before any file
  was read (chip `chip-20260827-mech357-trajectory-reanalysis`).
