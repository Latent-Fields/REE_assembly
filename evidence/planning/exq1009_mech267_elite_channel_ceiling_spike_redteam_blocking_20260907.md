> **SUPERSEDED 2026-09-07T17:05Z -- THE SPIKE WAS SUBSEQUENTLY REPAIRED AND QUEUED AS `V3-EXQ-1009`.**
> This record refused the SECOND design iteration. A third iteration (user-directed) fixed all three
> BLOCKING findings and passed a second red-team pass (CONTESTED, findings fixed or dispositioned);
> the driver is queued and live on the coordinator (`ree-v3 dbf1beeb47`). What still stands here,
> and is why this file is kept rather than deleted: **sections 2 and 4 -- the three confirmed
> substrate findings**, two of which generalise well beyond this spike. What is superseded:
> section 1's "cannot be given a non-fitted gate" conclusion, section 3's repair narrative, and
> section 6's routing. The third iteration's own reasoning is in the driver docstring and in the
> queue entry `note`.
>
> The gate that iteration 3 found: the 1005 threshold is an INCREMENT over a sampling-noise
> baseline B, so a displacement d moves dbar by `sqrt(B^2+d^2)-B`, not by d. Measuring d cleanly
> (shared-seed regime, where dbar(CTRL) is structurally 0) and projecting it onto that scale using
> each cell's measured B inherits the 0.02 honestly -- which neither of the first two iterations
> managed.

# V3-EXQ-1009 (MECH-267 elite-channel ceiling 2x2 spike) -- DESIGN REFUSED at `/queue-experiment` Step 4.5 (red-team BLOCKING, confirmed)

**Status: NOT QUEUED. No queue entry, no coordinator row, no manifest. The design-complete driver and its three probes are landed under `ree-v3/experiments/_scratch/` so the paid-for work is recoverable; nothing here has been written to `claims.yaml`, `substrate_queue.json`, or `experiment_queue.json`. The chip that commissioned this spike is resolved with this record.**

- **Written:** 2026-09-07T16:24:12Z
- **Session:** `cool-sutherland-9d984d` (Mac `DLAPTOP`, umbrella worktree), from `chip-20260907-exq1005-elite-channel-ceiling-spike`, campaign W4-S2 follow-on.
- **Commissioning record:** `exq1005_mech267_location_dv_redteam_blocking_20260907.md` section 6 (which specified this spike).
- **Red-team model:** the session model (Opus 5). **`fable` was attempted first and failed with HTTP 429 out-of-credits**; per `/queue-experiment` Step 4.5 the pass was re-spawned once inheriting the session model, which the skill states is valid. One pass, foreground.
- **Verdict: BLOCKING.** Three findings, all **CONFIRMED against source by this session** before any action was taken.

---

## 1. Why this is refused, in one sentence

The spike could not be given a **pre-registered, non-fitted, discriminating gate**: the DV the commissioning record specified (`delta_dbar`) was measured to be unusable as a ceiling (it goes negative on the production reference cell itself), and the replacement DV that fixes that (`relocation_ratio`) makes the inherited 0.02 floor **vacuous** -- every cell including the production null clears it -- so any threshold that would discriminate would have to be derived from this run's own pilot data, which is gate-fitting.

The spike's substantive question was nevertheless **answered by the design-time measurements**, without the 30-seed run. See section 4.

---

## 2. The three BLOCKING findings, and the source that confirms each

### F1 -- the post-CEM synthetic-candidate injection contaminates the DV

`_inject_support_preserving_candidates` is called at `ree_core/hippocampal/module.py:2356`, **after** `all_trajectories = trajectories` (`:2325`), and `final_summary` (`:2494`) -- the source of `action_object_decoder_raw_output_stats` (`:2552`), which is the DV -- is computed from that pool. Its scaffolds are one one-hot step followed by exact zeros (`:1223-1230`), so each injected candidate drags one action dimension's mean by ~`1/(candidates*horizon)` = `1/64` = 0.0156, **an order of magnitude above the centroid displacement being measured**. Firing is conditional on the pool's first-action class count (`:1461`), which the ORACLE arm changes by construction, so it can fire **arm-asymmetrically** and manufacture the very displacement being read.

**Confirmed by this session** at the cited lines. Reviewer measured firing at 24/40 runs in FROZEN/floor0.2, 17/40 in GROUNDED/floor0.2, 0/40 in both floor0.0 cells, arm-asymmetric in 1/20 pairs; neutralising it flipped GROUNDED/floor0.2 from -0.004784 to +0.002043.

**Note this generalises beyond this spike:** any experiment reading `action_object_decoder_raw_output_stats` as a centroid inherits this contamination. The 1005 record's section 4 dismissed the injection as "deterministic and arm-independent" -- correct for 1005's arms, but that dismissal does **not** transfer to any design whose arms change elite selection.

### F2 -- the documented legacy opt-out triple is a THREE-factor change, not an ao_std-floor manipulation

`use_support_preserving_cem` gates the refit clamp, **and also** stratified elite selection (`module.py:1312`) **and** the post-CEM injection (`module.py:1460`). Neither of the latter two reads `support_preserving_ao_std_floor`, and both act on the DV. So the sanctioned opt-out triple named in `config.py:2475-2476` -- which the commissioning record specified for the floor-OFF cells -- makes every level difference unattributable among three simultaneous changes.

**Confirmed by this session** at both gate sites.

**Clean single-factor alternative, also confirmed:** the refit gates on `use_support_preserving_cem AND _std_floor > 0.0` (`module.py:2305-2309`), so setting `support_preserving_ao_std_floor=0.0` while **leaving the flag True** disables exactly the clamp and nothing else. This repair was implemented in the driver and is worth carrying into any successor.

### F3 -- `delta_dbar` is not a ceiling and not an upper bound

`dbar` is a **between-mode** separation, and each mode's oracle direction is an independent random draw, so an oracle displacement enters it only to **second order** (`d^2/2R` for a random direction against `2d` for an aligned one -- 20-70x weaker at these magnitudes) and can reduce the separation as easily as raise it.

**Confirmed by this session's own runs**: `delta_dbar` is NEGATIVE on the production reference cell (-0.000009 at n=1, reviewer measured -0.000485 at n=5) and on GROUNDED/floor0.2 (-0.000318 at n=1, -0.004784 at n=5). **A quantity described as a CEILING or an upper BOUND cannot be negative.** Gating on it would route a bench whose channel genuinely widened to "no clear" because the random directions happened not to separate the modes.

---

## 3. The repair that was attempted, and why it also failed the gate test

The driver was rebuilt against all three findings: single-factor floor axis (F2), injection-free centroid recomputed from `source`-tagged filtering (F1), and a new primary DV (F3):

```
relocation_ratio = mean over modes of  ||mu_ORACLE - mu_CTRL|| / mean_spread(CTRL)
```

which is per-mode centroid relocation in that cell's own sampling-noise units, is first-order in the displacement, cannot go negative, and is self-normalising against the spread collapse the floor-OFF level induces.

**That DV is sound. The gate is not.** Measured at 1 seed on the rebuilt driver:

| cell | relocation_ratio | delta_dbar (secondary) | raw displacement | spread |
|---|---|---|---|---|
| FROZEN/floor0.2 (production reference) | **0.0313** | -0.0000088 | 0.001517 | 0.04999 |
| FROZEN/floor0.0 | 0.0379 | +0.023113 | 0.000334 | 0.00885 |
| GROUNDED/floor0.2 | 0.0276 | +0.001579 | 0.001307 | 0.04687 |
| GROUNDED/floor0.0 | 0.0363 | +0.012246 | 0.000606 | 0.01670 |

Every cell -- **including the production null** -- clears the inherited `CONTENT_FLOOR_ABS = 0.02`. C1 becomes a rubber stamp; all discrimination collapses onto the within-run contrast, and the four cells span only 0.028-0.038 (a ~20% spread, not the order of magnitude the 1005 design would need).

The 0.02 value was pre-registered **for `delta_dbar`**. Carrying it onto a different statistic is not "inheriting verbatim"; it is a number from another scale that happens to pass everything. Choosing a threshold that *would* discriminate means reading it off the table above -- fitting the gate to the data, which the standing rule forbids and which is exactly what the 1005 refusal exists to prevent.

**Two criteria formulations were tried and both failed, in opposite directions:**
- C1 on `delta_dbar` + C2 on raw displacement: the two pull in **opposite directions** along the floor axis (the collapse inflates the first and reduces the second), leaving the cleared branch close to dead.
- Both on `relocation_ratio`: no opposing-direction pathology, but the inherited floor is vacuous.

---

## 4. What the design-time measurements DO establish (this is the deliverable)

Across two DV formulations, four benches, 1-5 seeds, using an **oracle** elite chooser that is the strongest content-selective re-ranker available at the elite-selection call site:

**The elite-selection channel's reach is ~3% of the sampling spread on every bench tested, and neither manipulation moves it by more than ~20%.**

Specifically:
- Grounding E2's action-object head into genuine action-dependence (across-candidate ao std x2.99, validated) does **not** lift the channel -- GROUNDED/floor0.2 (0.0276) is if anything *below* production (0.0313).
- Removing the ao_std floor lifts `relocation_ratio` ~21% (0.0379 vs 0.0313) while *reducing* raw displacement 4.5x (0.000334 vs 0.001517) -- the ratio rises because the spread collapses faster than the numerator.
- The FROZEN/floor0.2 cell reproduces the archived probe-C magnitude (order 1e-5..1e-3), so the bench is the one that produced the 1005 refusal.

This is the same finding the commissioning record's **"no cell clears"** branch anticipated, reached at design time rather than after a 30-seed run. It routes where that branch says it routes (section 6 below).

**Two facts about the substrate were also established that outlive this spike:**
1. **No loss anywhere in `ree_core` trains `action_object_head`** -- it is referenced only at its construction site (`e2_fast.py:144`) and its forward call (`:602`). SD-080's frozen-random-projection defect is therefore **production**, not a bench artifact, and the commissioning record's suggested "trained E2 from the 978/1006 warmup path" would have produced a **vacuous cell** (that path leaves the head at init).
2. **V3-EXQ-817a's grounding objective does not transfer to an untrained-`world_forward` bench.** Its ABSOLUTE next-state target is action-diluted here because `world_forward` carries a `z_t` skip term (`e2_fast.py:222`), so grounding onto it *lowers* across-candidate action-object std (0.063 -> 0.029, x0.5). The world-effect **delta** target raises it (x2.6-3.9). Not a criticism of 817a, whose agent-side `z_world` is a learned encoder output.

---

## 5. Disposition of each finding

| # | severity | disposition |
|---|---|---|
| F1 | BLOCKING | **CONFIRMED** at `module.py:2325/2356/2494/2552/1223-1230/1461`. **Repaired** in the driver (source-tag filtering + arm-symmetry precondition). Generalises: any experiment reading `action_object_decoder_raw_output_stats` as a centroid inherits it. |
| F2 | BLOCKING | **CONFIRMED** at `module.py:1312/1460`. **Repaired**: floor-only manipulation with the flag left True (`module.py:2305-2309`). Carry into any successor. |
| F3 | BLOCKING | **CONFIRMED** by this session's own runs (negative on the production reference). Repaired by replacing the DV -- but the repair invalidated the inherited threshold, which is why this is refused rather than queued. |
| grounding scale (CONTESTED) | -- | Partially confirmed: the x2.99 raw lift coexists with a falling scale-free action share. A scale-free companion statistic was added and is recorded per cell. Not resolved; a successor should gate on the scale-free form. |
| reference-cell exactness (CONTESTED) | -- | Confirmed and **corrected in the docstring**: this driver rebuilds residue terrain on its own RNG stream, so it reproduces the archived probe-C *magnitude*, not its digits. The precondition asserts a band, not a point match. |

---

## 6. The gap, in work-graph vocabulary, and where it routes

The node remains **`complex (probe-gated)`**, but the probe-gate has moved. It is no longer "does the ceiling lift on a grounded bench" -- measured, section 4, it does not. It is now: **is there any pre-registrable statistic on which the elite-selection channel's reach is separable from the sampling floor?** Two formulations have now been tried and both fail the non-fitted-gate test.

**Routing, which this session deliberately does NOT execute** (registering a build ahead of governance's ratification is the `complicated`-before-`complex` inversion, and the commissioning record is explicit that the autopsy/spike does not register its own recommendation):

- **To `/governance`, on `GFLAG-0224`** (open, raised 2026-09-07, MECH-267, `evidence_discrepancy`): the section-4 measurements are the evidence that MECH-267's `what_would_answer` CONFIRMING branch presumes a content measurement no proposal-output-centroid instrument on this substrate can make. Governance's call is to narrow `what_would_answer` to the breadth channel, or to register a `complicated (buildable)` `substrate_queue.json` entry -- **E2 action-object action-dependence** is now the better-supported of the two candidates, since the ao_std floor axis was measured not to help.
- **A successor spike, if governance wants one, has a named principled repair**: make the oracle directions **maximally separating along a shared axis** rather than independent per-mode random draws. That makes `delta_dbar` a genuine upper bound (first-order, non-negative) and lets the **original pre-registered 0.02 floor be inherited honestly**, which is the one route that dissolves the gate problem rather than relocating it. Not attempted here: `/queue-experiment` Step 4.5 permits one re-spawn of the red-team pass, and it was spent.

---

## 7. Identifiers and where things are

| item | state |
|---|---|
| `V3-EXQ-1009` | never reached `experiment_queue.json` or the coordinator DB; **not burned**. A successor may reuse the number, since no evidence was recorded under it. |
| driver | `ree-v3/experiments/_scratch/v3_exq_1009_mech267_elite_channel_ceiling_spike.py` (design-complete, smoke-green, validator-clean, refused). Moved out of `experiments/` so `audit_unqueued_experiment_scripts.py` does not report it as a forgotten script. |
| probes | `ree-v3/experiments/_scratch/exq1009_probe_readiness.py` (config knobs, clamp behaviour, oracle reachability, grounding), `exq1009_probe_delta.py` (absolute-vs-delta grounding target), `exq1009_pilot_dv.py` (the 2x2 DV pilot) |
| red-team findings | `_scratch_exq1009/redteam_findings.md` in the session worktree (not landed; the confirmed substance is section 2 above) |
| `V3-EXQ-1005` | still never queued, still not burned; unchanged by this record |
| chip | `chip-20260907-exq1005-elite-channel-ceiling-spike` resolved `done` citing this record |
| claims | `cool-sutherland-9d984d` and `cool-sutherland-9d984d-exq-1009` closed NOT LANDED (no queue entry) |
