# Failure autopsy (lightweight, Step 9b Mode B) -- MECH-321 / ARC-070 hypothesis legs

**Status: CONFIRMED (dispositions ratified upstream; this pass WRITES them).**
Generated: 2026-08-18T05:17:40Z
Scope: `policy_decomposition_discrimination` legs `H-vs-proxy-saturation` and
`H-env-underdrives-uncertainty`, against V3-EXQ-816c / 816b / 816d.
Chip: `chip-20260816-mech321-hypothesis-legs-mode-b`. Flag: `GFLAG-0038`.

## 1. Why this is a Step 9b pass and not a governance edit

`/governance` is derive-only over `hypothesis_space_registry.v1.json` -- its Step 5c forbids
growing a second writer ("do NOT patch the registry inline at the walk"). The frozen ledger has a
single producer, `/failure-autopsy` Step 9b. `/governance` **ratified** these two dispositions in
its 2026-08-16 cycle (`GFLAG-0038`, recommended by
`govdiag1_repose_mech321_chain_2026-08-12.md` section 7); this pass **appends** them. That is the
residual case Step 5c names: "a leg whose adjudicating run is a clean PASS that clears inline with
no autopsy: route a lightweight /failure-autopsy".

No new experiment was run or needed. Both dispositions are earned by data already in the corpus.

### Staging-mode override, stated explicitly

This skill's "Staging mode (headless)" rule says a headless session must NOT write the registry and
must stage the blocks under `hypothesis_space_ledger_pending` instead. **That default is
deliberately overridden here**, on two grounds:

1. Its rationale is that "a scheduled autopsy is a draft for the user to confirm ... it never
   auto-applies" -- i.e. it guards *unratified* adjudications. These dispositions were ratified by
   a human governance cycle on 2026-08-16 before this session existed, and the chip brief instructs
   this session to write, not to decide.
2. Staging again would reproduce the exact failure this flag was raised to fix. The 2026-07-26
   autopsy (`failure_autopsy_816c-822_2026-07-26.json`) *did* stage a
   `hypothesis_space_ledger_pending` block, and it sat unapplied for three weeks because
   **nothing re-derives it** (816b/c/d are already autopsied so they never reach
   `pending_review.md`, and the integrity audit is deliberately silent on an unresolved leg).

## 2. Evidence

### (i) `H-vs-proxy-saturation` -> `confirmed`

V3-EXQ-816c (`experiment_purpose: diagnostic`, outcome **PASS**, `non_degenerate: true`,
self-route `vs_pe_decoupled_proxy_saturation`). All four preconditions met:

| precondition | measured | threshold |
|---|---|---|
| `vs_tracking_live` (worst cell, streams tracked) | 3 | > 1 |
| `forward_pe_varies` | 8.64e-07 | > 1e-09 |
| `forward_pe_bounded` | 0.008594 | < 1000 |
| `enough_paired_steps` | 1654 | > 30 |

`vs_tracking_live = true` is the load-bearing one: it rules out the degenerate constant-1.0
`region_vs` fallback, under which a "V_s flat" reading would be an artefact -- a false decoupling.

The pre-registered null was *"forward-PE heterogeneity present (PE-trigger fires) while V_s
heterogeneity absent (V_s-trigger silent) -> decoupled"*. The run took exactly that branch:
`pe_heterogeneous true` / `vs_heterogeneous false`, `decoupled true`, `not_saturated false`,
`region_vs_min_over_cells 0.9338` (var 0.000275), `total_low_vs_steps 0` of 1654,
`spearman_unc_vs_pe_mean_over_cells 0.0832` against a `spearman_coupled_floor` of 0.2, and
`pe_trigger_fires_total 13` vs `vs_trigger_fires_total 0` with `cofire_total 0`.

The 2026-07-26 adjudication left this leg alive on one **stated** condition -- that 816b might show
a harsher environment can drive region-V_s into a low band, keeping the proxy usable. That condition
was then tested at two doses and failed both: 816b `low_vs_produced false`
(`region_vs_min_over_cells_arm1` 0.9347) and 816d `low_vs_produced false` (0.9340). The
deferral's own trigger has fired, so the leg clears.

`met_elimination_bar` stays `false`: a confirmation is not an elimination (invariant 4).
`control_passed: true` is what invariant 5 requires. `resolved_utc` = 816d's completion
(2026-07-26T18:50:06Z), the last run discharging the deferral, and >= the leg's
`pre_registered_utc` (2026-07-26T05:38:01Z), satisfying invariant 2.

### (ii) `H-env-underdrives-uncertainty` -> ratified **superseded / moot**

Ratified reasoning: since region-V_s is decoupled from forward-PE, raising PE **cannot** lower V_s,
so even a successful future harshening would not restore the readout this leg exists to rescue. The
leg is no longer load-bearing for this question whatever its truth value.

**It was NOT written as a literal state, and that is the one judgement call this pass had to make.**
See section 3.

## 3. The schema gap -- `superseded` has no slot, and neither in-vocabulary alternative is honest

The ratified word cannot be written as `resolution.state`:

- **`"superseded"` as a literal state would be silently uncounted.** The derived vocabulary has
  exactly three buckets -- `ALIVE_STATES {alive, untested}`, `RESOLVED_OUT_STATES
  {eliminated, split}`, and `confirmed` (`build_hypothesis_space.py`). A state outside all three
  falls into none: the leg would vanish from `surviving` / `resolved_out` / `confirmed`
  arithmetic (6 legs, 5 accounted), and the question's `environment` axis family could never be
  marked closed. No flag would fire -- `check_hypothesis_space_integrity.py` only polices the
  `confirmed` and `eliminated`/`split` rules. A silent under-count in a governed ledger.
- **`"eliminated"` would require asserting `met_elimination_bar: true`, which is not earned.**
  816b's and 816d's own pre-registered elimination branch was "forward-PE elevated but V_s flat",
  and neither run took it: both recorded `pe_elevated false` (0.008594 and 0.008675 against the
  0.01 discrimination floor), so on the **literal** pre-registered null they read "dose
  insufficient, direction correct". Section 7(ii) surfaces the stronger reading (V_s did not move a
  little, it did not move at all -- `low_vs_produced false`, `lowvs_worst_arm1 0` at every dose --
  while PE did move) as *available and defensible* but as **stretching a pre-registered floor after
  the fact**, and therefore **explicitly recommends `superseded` over `eliminated`**.

Writing `eliminated` would have been this session over-riding a judgement call governance
deliberately declined to make, in the **over-counting** direction GOV-FROZEN-1 exists to prevent.

**Resolution taken:** the leg keeps `state: "alive"` and the full ratified disposition is written
into its `resolution.basis` and `resolving_runs` (Mode B-narrow -- the same shape this question's
own 2026-07-26 autopsy used). The basis opens by naming the disposition as SUPERSEDED / MOOT and
states in terms that the `alive` state is a **schema-vocabulary limit, not a scientific hedge**,
and that the leg **must not be re-queued for a fourth environment-axis dose escalation**. This is
the conservative under-count Step 5c explicitly blesses ("an unresolved leg simply keeps surviving in
the count until Step 9b resolves it -- a conservative under-count, not a Goodhart move").

**Residual, escalated not buried:** raised as a governance flag and as decision chip
`chip-20260818-hypothesis-registry-superseded-state` -- either add a `superseded` state to the
registry vocabulary and both derive scripts, or ratify `eliminated`. Until then the dashboard
reports this question as 5 surviving where the ratified reading is 4.

## 4. Ledger delta

| | before | after |
|---|---|---|
| alive | 6 | 5 |
| confirmed | 0 | 1 |
| surviving | 6 | 5 |
| `initial_frozen_count` | 6 | **6 (unchanged)** |
| `initial_frozen_count_at_registration` | 4 | **4 (unchanged)** |
| `convergence_class` | `scattering` | `refining` (`instrumentation` family closed) |
| `net_narrowing_ratio` | -0.50 | -0.25 |
| integrity flags | 0 | **0** (a=0 b=0 c=0 d=0) |

No hypothesis was added; the frozen set did not grow; no `pre_registered_utc` was touched. The
surviving-count drop is reported by the audit as *backed by 1 newly-confirmed hypothesis*, advisory,
not a violation.

The question's `decision` block had its **prose** refreshed (`observation_bottleneck`,
`distance_phrase`) because the old text -- "needs an env/measure-window producing low-V_s states"
-- is now directly contradicted by the confirmed leg. `decidable` (false), `live_gate` (null) and
`decision_log_ref` (null) were **not** touched: invariant 7, the human owns `decided`.

## 5. Section 3b (split the question) -- weighed, NOT applied

`govdiag1` section 3b argues the six legs are two sets (2 science: `policy`, `arbitration`;
4 instrument: `environment`, `measurement`, `representation`, `algorithm`) and that
"a frozen set mixing science and instrument hypotheses cannot be resolved by any run", citing
six-alive-after-six-runs as that structure's signature.

**Not applied**, on two grounds:

1. It is explicitly **passed on, not ratified** -- a structural change to a frozen set is exactly
   the class of edit that needs an interactive decision, and GOV-FROZEN-1 has no shrinkage or split
   operation for a registered question.
2. **This pass is partial evidence against its strong form.** An *instrument* leg
   (`H-vs-proxy-saturation`, axis `measurement`) has now been cleanly resolved by a run, and its
   resolution is what makes a second instrument leg moot -- closing the `instrumentation` family
   and moving the question's `convergence_class` from `scattering` to `refining`. The
   six-alive-after-six-runs signature was, at least in part, an unapplied-ledger artefact rather
   than purely a structural one: two of those six were resolvable from data already in hand.

   The weaker form of 3b still stands and is worth governance's attention: the two **science** legs
   remain unmeasured, and no environment-axis run can measure them. That is a
   `complex (probe-gated)` re-operationalization (govdiag1 section 5), not
   `complicated (buildable)` work on the existing readout.

## 6. Routing

- **Unblocks** `chip-20260814-mech321-pe-selectivity-repose`. Its STOP-CHECK (a) stops only if
  **BOTH** legs are still `alive`; `H-vs-proxy-saturation` is now `confirmed`, so the gating
  precondition is discharged. Its other two stop-checks had already passed on 2026-08-16.
- **Refuses** a fourth environment-axis dose escalation (816e or equivalent). 816/816b/816d
  converged within 0.0001 and 816c explains why.
- **To governance:** the `superseded`-state schema gap (section 3), and section 3b's weaker form
  (section 5).
