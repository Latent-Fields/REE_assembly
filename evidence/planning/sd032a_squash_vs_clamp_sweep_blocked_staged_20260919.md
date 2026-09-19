**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or whichever registry).**

# V3-EXQ-1067 (SD-032a / MECH-266) squash-vs-clamp cap sweep -- REFUSED at /queue-experiment Step 4.5

- **Recorded**: 2026-09-19T22:50:33Z
- **Session**: `metaworker-science-20260919-sd032a-squash-clamp-cap-sweep` (headless, ree-cloud-4)
- **Chip**: `chip-20260919-sd032a-squash-vs-clamp-cap-sweep` (science campaign
  `science-20260919-sd032a-squash-clamp-cap-sweep`, user-approved for dispatch 2026-09-19T22:12:50Z)
- **Outcome**: script authored and reviewed; **NOT queued**. Red-team verdict **BLOCKING**,
  confirmed against source. A decision chip has been raised; see the end of this file.
- **Reserved but unconsumed**: `V3-EXQ-1067` (claim
  `metaworker-science-20260919-sd032a-squash-clamp-cap-sweep`, resource
  `ree-v3/experiment_queue.json/V3-EXQ-1067`). No queue entry was appended.

## What was built

`ree-v3/experiments/v3_exq_1067_mech266_squash_vs_clamp_cap_sweep.py` -- a successor to
`v3_exq_934_mech266_cap_sweep_mode_occupancy.py` crossing the affinity bounding OPERATOR
(`salience_affinity_bound_mode` in {clamp, squash}, sigma at the landed default None -> cap)
with 934's cap band `[0.75, 1.0, 1.25, 1.5, 1.75]`, on 934's seeds `[42, 43, 44]` and both of
its rail arms, at eval time on clones of one trained curriculum agent per seed.

It clears every earlier gate: `validate_experiments.py --strict` passes all 38 checks; the
re-derive brake (count 7 on both claims) is RELEASED because the named upstream substrate
(`mode-governance-engagement` item (1), `cingulate.salience_coordinator.affinity_bound_operator`)
shows IMPLEMENTED 2026-09-19 in `ree-v3/CLAUDE.md`; no open `corrupting` substrate_queue entry
overlaps its modules. The load-bearing occupancy criterion is the entry's own transcribed bar,
evaluated by `experiments/_lib/regime_occupancy_gate.py` called ONCE per (bound_mode, arm) over
ALL (seed, cap) cells with `seed` and `sweep_value` populated -- deliberately not 934's per-seed
call shape.

The script is committed for resumability and its docstring is headed with the blocked marker.
**It must not be queued as it stands.**

## THE BLOCKING FINDING (red-team: Fable; verified against source before recording)

**The squash is not "the clamp plus gradedness at the top end". It is also a large gain cut on
the affinity input that dominates this experiment's DV -- and the two effects are not separable
by anything the design records.**

### 1. The operator is applied to EVERY affinity signal, not only to unbounded ones

`ree_core/cingulate/salience_coordinator.py:616-636` loops over all of
`self.config.affinity_weights` and bounds each signal's raw value. `ree_core/agent.py:2760-2765`
registers `external_task_drive` as one of those signals, at
`external_task_drive_affinity_weight` (3.0 in this driver's config) into the `external_task` mode.

### 2. At sigma = cap, the squash attenuates sub-cap signals substantially

`bound_affinity_input(x, cap, "squash")` with `sigma=None` is `cap*x/(cap+|x|)`
(`salience_coordinator.py:184,195`). Measured against the real function:

| input | squash / clamp ratio |
|---|---|
| 0.25 x cap | 0.800 |
| 0.50 x cap | 0.667 |
| 1.00 x cap | **0.500** |

The ratio is scale-free (identical at all five swept caps). A signal AT the cap is **halved**.

### 3. Consequence: the dominant effect of the operator swap is on the wrong signal

`external_task_drive` engagement is clipped to [0,1] at `agent.py:7881`, and the still-open
boolean commitment latch at `agent.py:7870` pins it at **exactly 1.0** whenever
`beta_gate.is_elevated`. So the common case is engagement = 1.0, and:

| cap | ext_task logit contribution, clamp -> squash (w=3.0) | delta | dacc_pe=16 bounded, clamp -> squash | delta |
|---|---|---|---|---|
| 0.75 | 2.250 -> 1.286 | **-0.964** | 0.750 -> 0.716 | -0.034 |
| 1.00 | 3.000 -> 1.500 | **-1.500** | 1.000 -> 0.941 | -0.059 |
| 1.25 | 3.000 -> 1.667 | **-1.333** | 1.250 -> 1.159 | -0.091 |
| 1.50 | 3.000 -> 1.800 | **-1.200** | 1.500 -> 1.371 | -0.129 |
| 1.75 | 3.000 -> 1.909 | **-1.091** | 1.750 -> 1.577 | -0.173 |

The "degeneracy fix" on `dacc_pe` -- the effect the run exists to test -- is **8x to 28x smaller
than the gain cut on the external_task drive**, and the gain cut pushes occupancy *away from*
external_task at every swept cap.

### 4. Why that makes both outcomes unattributable

- **A PASS** (squash grades where clamp did not) is indistinguishable from what a CLAMP arm
  would do with `external_task_drive_affinity_weight` lowered from 3.0 to `3*cap/(cap+1)`
  (~1.5-1.9). It would not show that a graded bound admits a mixed regime; it could equally
  show that reducing an over-strong drive does.
- **A NULL** routes `SD-032a: weakens` and is pre-registered as isolating the commitment latch --
  but it is equally explained by the squash halving the drive and pushing occupancy to 0. The
  attribution the campaign brief was explicitly designed to secure ("a third occupancy failure
  is attributable to the cap-independent commitment-term latch rather than to the operator") is
  exactly what this destroys.
- **The telemetry cannot rescue it.** The driver records the *pre-bound*
  `_input_signals["external_task_drive"]`, so the manifest would report
  `et_drive_saturated_frac ~ 1.0` while the coordinator actually consumed 0.43-0.64. No
  post-bound per-signal contribution is recorded.

### 5. The ratified record's stated rationale is wrong on this point

`substrate_queue.json` `mode-governance-engagement`
`implementation_log.squash_sigma_decision_2026_09_19.why_sigma_equals_cap` says, verbatim:

> "At sigma == cap that slope is exactly 1, so every SUB-cap signal passes through precisely as
> the legacy box clamp passes it and the ONLY behavioural change is at the top end, where the
> clamp was degenerate. That is what lets a validation sweep attribute an effect to the operator
> change rather than to a simultaneous gain change."

The premise is true (the derivative at the ORIGIN is exactly 1). The inference is false: slope 1
at the origin does not make the map an identity over `[0, cap]`, and it measurably is not
(table in section 2). The final sentence -- the stated licence for this very sweep -- therefore
does not hold. This is an error in the justification recorded for the 2026-09-19T09:45Z OPTION 1
(sigma = cap) decision, not necessarily in that decision itself.

Note the tradeoff is INTRINSIC to the chosen operator family, not a sigma mis-set:
`cap*x/(sigma+|x|)` is bounded strictly inside `(-cap, +cap)`, so it can never pass a signal
through at the cap under any sigma. Smaller sigma moves the cap-value output closer to cap but
makes the origin slope `cap/sigma > 1` (amplification -- which the record separately flags as an
unintended behavioural change, citing Ohshiro 2011 inverse effectiveness).

## Two further CONTESTED findings (verified, lower severity, same fix window)

- **`operator_manipulation_landed` is vacuous as written.** It compares `ext_margin_mean` between
  operators at matched (seed, cap, arm) and passes on a difference > 1e-6. But the cells are not
  RNG-paired: `torch.manual_seed` is set once per seed, the shared `dual_env` is built once per
  seed with `_derive_env_seed(None, ...) -> None` (OS entropy) and its RNG advances across all 20
  cells, and E3 selection samples stochastically. Banked 934 data shows two cells differing only
  in rails (which do not touch the soft vector) already differ by 1.7e-3 -- three orders of
  magnitude above the threshold. The guard would pass even if the override never reached `tick()`.
- **Operator is confounded with cell order on a stateful shared env.** The driver nests
  `bound_mode` outermost, so all 10 clamp cells run before all 10 squash cells on one `dual_env`
  that is never rebuilt, and `CausalGridWorldV2.harm_obs_a_ema` is not reset between episodes.
  Every squash cell sees accumulated env state no clamp cell saw.

Both are straightforwardly fixable (interleave the operator innermost / rebuild or re-seed the
env per cell; pair cells on a per-cell RNG reset) -- but they are only worth fixing once the
blocking question below is answered, because that answer may change the arm structure.

## THE DECISION THIS NEEDS (raised as `chip-20260919-sd032a-squash-confounded-gain-cut`)

The fix changes WHAT IS MEASURED -- the arms, and what the contrast means -- so it is not this
session's to pick. Options as put to the user:

- **(A) Add a gain-matched clamp control arm.** Third arm: clamp with
  `external_task_drive_affinity_weight` scaled to `3*cap/(cap+1)` per cell, so the gain-cut
  component is measured separately from the gradedness component. Cost: +50% eval cells
  (20 -> 30 per seed, ~9h -> ~13h).
- **(B) Scope the operator to unbounded signals only.** Apply the squash only where it is
  motivated (`dacc_pe`), leaving already-bounded signals on the clamp. This is a SUBSTRATE
  change to `mode-governance-engagement` item (1), not an experiment-side choice, and would
  re-open an item the record calls complete.
- **(C) Run as designed and accept the confound**, recording it explicitly so neither outcome is
  read as operator evidence. Cheapest; produces a result that cannot answer the question the
  campaign was dispatched for.
- **(D) Re-open the sigma decision** in light of section 5, since its stated rationale does not
  hold.

**Recommendation: (A).** It is the only option that keeps the occupancy criterion the user
ratified as load-bearing, preserves the V3-EXQ-934 clamp baseline unchanged, needs no substrate
change, and makes the third-failure attribution the campaign was dispatched to secure actually
valid. Its cost is compute, which is the cheap resource here.

Whatever is chosen, section 5 should reach `/governance` on its own account: the
`why_sigma_equals_cap` rationale recorded against a real user decision is mathematically wrong
and is being cited as the licence for downstream validation design.
