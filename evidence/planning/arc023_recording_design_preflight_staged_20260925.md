**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or whichever registry).**

# ARC-023 recording-complete design -- pre-authoring measurements (2026-09-25)

- Session: `metaworker-science-20260925-orchc-arc023-recording` (campaign `science-20260925-orchc-arc023-recording`)
- Chip: `chip-20260924-arc023-recording-design`
- Reserved but NOT yet authored: `V3-EXQ-1098` (`ree-v3/experiments/v3_exq_1098_arc023_e3_cadence_recording_complete.py`)
- Probe host: `ree-cloud-4`, python `3.10.12` / torch `2.12.0+cpu`, ree-v3 `origin/main` + 3 unrelated
  uncommitted files from a concurrent session (`ree_core/agent.py` +175 lines PAG-only,
  `ree_core/pag/*`). Verified those edits touch **none** of `phase_reset` / `clock.` / `z_beta` /
  `_e3_tick` / `update_e3_rate` (`git diff HEAD -- ree_core/agent.py | grep -E '^[+-].*(...)'` -> empty),
  so the clock-path measurements below are unaffected by them.
- Probe: 400 env steps, UNTRAINED agent, `StepHarness`, V3-EXQ-942 ecological-load config
  (`size=10, num_hazards=1, num_resources=5, harm_history_len=10`, `alpha_world=0.9`), seed 11.
  Untrained on purpose: this is a wiring + dynamic-range probe, not a scientific measurement.

## 1. Pre-flight AMBER caveat: CONFIRMED real on the live tree

`experiments/_lib/baselines/mech091_phase_reset.resolve_trigger_sites()` classifies the
NCL-reassert call site as `commit_entry`, exactly as the pre-flight predicted:

```
TRIGGER_CLASSES = ('completion', 'harm', 'commit_entry')          # 3-way, ARC-023 needs 4-way
resolve_trigger_sites() -> {6821: 'completion', 7849: 'commit_entry',
                            10449: 'commit_entry', 10649: 'commit_entry', 11564: 'harm'}
  agent.py:6821  -> completion    ncl_context=False
  agent.py:7849  -> commit_entry  ncl_context=True     <-- the fold; must become `ncl_reassert`
  agent.py:10449 -> commit_entry  ncl_context=False
  agent.py:10649 -> commit_entry  ncl_context=False
  agent.py:11564 -> harm          ncl_context=False
```

The NAMED CHANGE's discriminator works and is specific: `_ncl_hold_reassert_count` appears in the
14 lines preceding 7849 and in none of the other four. Line numbers differ from the pre-flight's
(6523/7551/10125/10325/11234) and from `origin/main`'s (6646/7674/10274/10474/11389) purely by
line drift -- which is why `resolve_trigger_sites()` resolves at runtime and a hardcoded table
would be wrong. **Disposition: implement the 4-way classifier LOCALLY in the new
`_lib/baselines/arc023_e3_cadence.py`, do NOT edit `mech091_phase_reset.py`** -- that module is
inside the arm-fingerprint substrate glob, so editing it would bust V3-EXQ-944/944a/944b's
baseline reuse for no benefit. The NAMED CHANGE explicitly licenses "or a local copy".

## 2. `substrate_queue` row `mech005-endogenous-arousal-dynamic-range`: premise NOT reproduced here

That row (severity `degrading`, so not a Step 2.5c block) asserts endogenous `||z_beta||` spans
0.91% of its mean and that `e3_steps_per_tick` therefore has `n_distinct == 1` per arm at every
scale -- which, if true at this design's operating point, would make ARC-023's CONFIRMING leg (i)
("clock-driven E3 updates track `sum_t 1/_current_e3_steps(t)` within +/-15%") an arithmetic
identity rather than a measurement.

Measured here: **`_current_e3_steps` takes 7 distinct values `[8, 9, 10, 11, 12, 14, 16]`**, with
`||z_beta||` spanning 0.2227..0.7432 (**72.2%** of its mean). Leg (i) is therefore NOT inert on
this tree at this config, and leg (i) can genuinely fail (observed ratio 0.7047, outside the
+/-15% band, driven by reset-interference zeroing `_e3_phase_step`).

**The two measurements are not in conflict and the row is not wrong.** It measured a FULLY TRAINED
agent (P0=12/P1=12/SD-070 zP0=8), where `z_beta` converges to 0.7018..0.7082; this probe is
untrained. The arithmetic in that row checks out exactly (`t = clamp(||z_beta||*scale, 0, 1)`,
`steps = int(20 - 15t)`, so a one-integer within-arm swing needs `15*scale*spread >~ 1`).
**Consequence for the design, not a question:** whether leg (i) is non-degenerate depends on the
run's own trained operating point, so the driver must record `n_distinct(_current_e3_steps)` as an
explicit measured precondition and mark leg (i) `criteria_non_degenerate: false` when it is 1.
This needs no falsifier change -- the claim already REQUIRES per-step `_current_e3_steps` and
`|z_beta|` precisely so a reader can see it.

## 3. Trigger reachability by config (the BLOCKING question -- see the decision chip)

`phase_reset()` REQUESTS per 400 steps, by `(class, agent.py lineno)`:

| trigger class | site | production defaults | `beta_gate_bistable=True` | bistable + `use_natural_commit_latch_hold=True` |
|---|---|---|---|---|
| `harm` (NO onset gate) | 11564 | 106 | 45 | 45 |
| `commit_entry` (legacy elevate) | 10649 | 5 | 0 | 0 |
| `commit_entry` (readiness admission) | 10449 | 0 | 3 | 3 |
| `completion` | 6821 | **0 -- STRUCTURALLY unreachable** (`if self.config.heartbeat.beta_gate_bistable and ...`) | 0 (reachable in principle; untrained hippocampal completion signal never clears) | 0 |
| `ncl_reassert` | 7849 | **0 -- unreachable** (`_ncl_hold_active` False) | 0 | **0 even with the knob ON** |

Derived shares (400 steps):

| | defaults | bistable ON | bistable + NCL |
|---|---|---|---|
| realized `_e3_tick` share | 0.3600 | 0.2300 | 0.2300 |
| clock-driven share | 0.0850 | 0.1050 | 0.1050 |
| reset-driven share | **0.2625** | **0.1175** | **0.1175** |
| leg (i) observed/expected | 0.7047 | 0.8580 | 0.8580 |
| E2 configured share | 0.3333 | 0.3333 | 0.3333 |

`use_natural_commit_latch_hold=True` changes nothing -- consistent with `config.py`'s own recorded
note that the latch-hold "NEVER armed (`ncl_hold_reassert_total=0`)". So **NCL re-assert looks dead
at every reachable config**, and `completion` is code-gated off at production defaults.

Note `beta_gate_bistable` is **outcome-determining for CONFIRMING leg (iii)** (`reset-driven share
<= 0.10`): 0.2625 vs 0.1175 across the two settings. The flag is set nowhere in ARC-023's
`what_would_answer`, in the chip prompt, or in the pre-flight. V3-EXQ-942 (the run the tightened
tolerances were calibrated against) ran at the **default False**; the canonical MECH-091 lineage
module `mech091_phase_reset.py` sets it **True**, commented as "what makes ... MECH-091's
completion trigger reachable at all".

## 4. Separate finding: the TIGHTENED FALSIFYING leg looks effectively unreachable

Not a blocker and not a choice this session has to make -- recorded because it qualifies what any
run of this falsifier can conclude, and because GFLAG-0443's option-A tightening was raised to
cure exactly this defect in the previous wording.

FALSIFYING requires `clock-driven share + ONSET-GATED reset-driven share >= 1/3 = 0.3333`.

- `update_e3_rate_from_beta` clamps `new_steps >= beta_rate_min_steps = 5`, so **clock-driven share
  can never exceed 0.20**; at the measured endogenous max `||z_beta|| = 0.743` the attainable cap is
  `1/int(20 - 15*0.743) = 1/8 = 0.125`.
- So the leg needs onset-gated reset share `>= 0.208` realistically (`>= 0.133` even at the
  unattainable clamp ceiling).
- Measured onset-gated reset share (commit-entry; completion and NCL contribute 0): **0.0075-0.0125**
  -- 17-28x short. A trained agent commits MORE stably, which moves this down, not up.
- The only trigger with the volume to reach the bar is `harm` (0.113-0.265 on its own), which the
  tightened leg explicitly EXCLUDES and routes to PARTIAL/MECH-091.

So GFLAG-0443 option A replaced an unreachable bar (share 1.0) with a reachable-LOOKING bar (1/3)
while simultaneously restricting qualifying resets to the onset-gated triggers -- removing the very
signal (V3-EXQ-942 seed 37, share 0.394, harm-driven) that made 1/3 look reachable. The practical
consequence is that a recording-complete run discriminates **CONFIRMING vs PARTIAL**, not
CONFIRMING vs FALSIFYING. PARTIAL is still directly actionable (it routes to MECH-091's onset gate),
so this does not make the run worthless -- it makes a CONFIRM weaker than it reads. Raised as a
governance flag rather than decided here.

## 5. Gates cleared (for the record)

- **GOV-REUSE-1 (Step 2.4):** decisive readouts absent. `reanalysis_query.py` over 1077 manifests:
  0 carry `reset_driven_share` / `e3_share_realized` / `current_e3_steps` / `trigger_counts` /
  `clock_driven_e3_updates`. Instrument canary: readout `e3` with no claim filter DOES return hits,
  so the zeros are real, not a broken search. V3-EXQ-942's own manifest carries
  `claim_ids: ['INV-013']` (not ARC-023, which is why a claim-filtered scan reads 0) and contains
  none of `current_e3_steps` / `z_beta` / `phase_reset` / `trigger` / `reset_driven` / `e3_share`.
  -> not recoverable, run.
- **Step 2.5:** SD-006 `implemented`; MECH-089/090 `active`; MECH-091 IMPLEMENTED 2026-08-17
  (`docs/substrate/MECH-091-mech091-salient-event-trigger-wiring.md`); MECH-093 `provisional`.
  All five `phase_reset()` sites and `update_e3_rate_from_beta` read directly from source.
- **Step 2.5b (re-derive brake):** ARC-023 count **0** (one autopsy occurrence, V3-EXQ-942, which
  does not count). Not braked.
- **Step 2.5c:** one `corrupting` overlap, `SD-PP-B5-z-world-per-step-displacement-range`
  (`ree_core/environment/causal_grid_world.py`). Its own `severity_rationale` scopes the corruption
  to `use_world_interventional` (default **False**, `config.py:908`) -- this driver never enables it
  and reads no world-forward quantity, so the overlap is config-unreachable here; to be recorded in
  the queue note. `mech005-endogenous-arousal-dynamic-range` is `degrading` -> note, not block
  (section 2).
- **Step 2.6 ethics:** all-`false` / `decision: allow` (SENT-0, routine V3).
- **Pending review:** 5 items outstanding at 2026-09-25T01:08Z (FAIL 1083/1089; PASS 1085/1087/1093;
  1087 flagged `vacuous_pass`) -- surfaced per the skill's Before-starting step 3, untouched here.
