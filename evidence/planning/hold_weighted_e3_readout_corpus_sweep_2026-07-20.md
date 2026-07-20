# Hold-weighted E3 readout — corpus sweep and triage (defect form 2)

**Generated** 2026-07-20T05:52Z · **Session** `nostalgic-elbakyan-f95ab9`
**Lint** `ree-v3/validate_experiments.py::e3_hold_weighted_readout_lint` (ree-v3 `82f278212c`)
**Contracts** `ree-v3/tests/contracts/test_e3_hold_weighted_readout_lint.py`
**Origin** [`failure_autopsy_V3-EXQ-699_2026-07-20.md`](failure_autopsy_V3-EXQ-699_2026-07-20.md) sec 11.1
(REE_assembly `ac2fb64028`), which asked for exactly this re-sweep.

> **One line.** 150 of 1093 tracked scripts carry the defect; **91 of them are invisible to the
> existing stale-diagnostics gate**. 109 have landed manifests. Of the ~30 triaged in depth, the
> split is not uniform — readiness batteries overwhelmingly SURVIVE on threshold invariance while
> conversion DVs are DISQUALIFIED, and the single most consequential item is **V3-EXQ-707b**.

---

## 1. The defect, and why form 1 could not see it

`ree_core/agent.py:5430` returns the **held** action on `not ticks["e3_tick"]`, *before*
`e3.select()` is reached. `agent.generate_trajectories` (`agent.py:4812`) likewise returns
**cached** candidates on a non-E3 tick (MECH-057a). So any per-env-step statistic accumulated from
the `select_action` return value, from `agent.e3._last_selected_trajectory`, or from the candidate
list is weighted by **hold duration** — cadence default 10 (`utils/config.py:2017`), varying 5-20
under MECH-093 arousal (`heartbeat/clock.py:52-70`).

No diagnostics latch is touched, so `e3_diagnostics_staleness_lint` is **structurally blind**. On
699 it fired only on `:929` (incidental) and was silent on `:882` — the primary DV, and the site
that forced withdrawal of `levers_compound`.

The two gates are kept **separate, with separate pins**. Freshness and replication are independent
defects: 699's `active_frac == 1.0` is informative *because* its diagnostics are fresh, where 708's
identical 1.0 was vacuous. Conflating them mis-adjudicates in both directions.

## 2. The triage test (from the 699 and 708 autopsies)

**An inflated n is NOT sufficient for contamination.**

| Class | Test | Why |
|---|---|---|
| **SAFE** | threshold-invariant: a floor of literally `0.0` (strict `> 0`), an exact-zero reading, or a fraction saturated at exactly `1.0` | duplication cannot manufacture a positive from an all-zero record, nor collapse a genuine positive to exact zero; a saturated ratio has nowhere to move |
| **AT RISK** | a continuous margin against a non-trivial floor | replication shifts it by an unbounded, unobservable amount |
| **DISQUALIFYING** | a **distribution-shape** statistic — entropy, variance, histogram-derived, unique-count, occupancy | replication reweights the distribution itself, which is exactly what such statistics measure |

**Calibration, and its limits.** The matched replay on the `v3_exq_663_modulatory_channel_routing`
driver measured the cost at **+0.01% / +0.64% / −0.87%** — sub-1%, sign-varying (WORKSPACE_STATE
2026-07-20T06:25Z, ree-v3 `5433e3ab1c`), so 662/663's estimates stand. That bounds the defect
**only** where arm symmetry cancels it *and* the DV is a continuous magnitude. It does **not** bound
entropy DVs, nor cases where arms differ in hold duration (autopsy sec 4d). Both exclusions bind
across most of this corpus — measured arm exposure spreads reach **+152%**.

## 3. Sweep result

| | count |
|---|---|
| tracked `v3_exq_*.py` corpus | 1093 |
| **form-2 fires** | **150** |
| — with a landed manifest (completed; re-adjudication candidates) | **109** |
| — not yet run (preventable) | **41** |
| — **invisible to form 1** | **91** |
| form-1 fires (unchanged, pin holds) | 63 |

**None of the 41 not-yet-run scripts is queued or claimed** — nothing is about to execute with the
defect. They are idle/superseded historical drivers, all but 6 firing on `select_action` alone.

**Mechanical pre-screen of the 109 completed:** 100 carry a distribution-shape DV name. That is a
*ranking signal, not a verdict* — a name match does not establish that the statistic is accumulated
at the flagged site or is load-bearing. Sections 4-5 record verified verdicts; section 6 is the
un-verified remainder.

## 4. Verified verdicts — act on these

### 4a. V3-EXQ-707b — highest consequence, and it propagates

`evidence_direction: **weakens**` ARC-110 — the only **live directional verdict** in its lineage.
Load-bearing `C1_A1_loops_strict_above_A0_and_in_layer_null` is a `+0.05` nat margin on
`committed_class_entropy_nats` under a **+98% arm exposure spread**. DISQUALIFYING on both counts.

**It propagates.** The 708 re-adjudication (sec 5a, sec 10) explicitly recruited 707b to repair a
leg that 708's own withdrawal had broken, and to redirect 708a's design away from the
loop-segregation bet. That repair now rests on a contaminated instrument. The ARC-110 `weakens` and
the 708 autopsy's venue note should be treated as **jointly unsupported pending re-run**.

### 4b. MECH-448 / MECH-449 — the claim bases split

The 699 autopsy states both claims rest on 689d and 689g. They do not fare alike.

- **MECH-449 — INTACT.** `v3_exq_689g` is **structurally immune**: zero occurrences of
  `agent.select_action` / `clock.advance` / `env.step`. It drives `selector.select(...)` directly on
  synthetic candidate banks — one fresh selection per bank, no cadence, no env loop, no replication
  possible. Its criteria are additionally threshold-invariant (`safety_violations == 0`). ARC-107's
  share is likewise intact.
- **MECH-448 — COMPROMISED.** `v3_exq_689d` (**PASS / supports**) accumulates
  `selected_class_counts[int(action[0].argmax())]` per env step at `:598`. Its only finding-bearing
  criterion `C_PRIMARY` is a class-histogram entropy passing on **exactly 2 of 3 seeds**, weaker
  survivor margin **0.187 nats**, across arms whose exposure differs **7-fold**. Fails the test on
  all three counts. Its readiness / rank-preservation / safety criteria **survive** on threshold
  invariance — so the substrate is demonstrably built and doing real work; the *conversion finding*
  that moved MECH-448 toward `supports` has no uncontaminated basis.
  **Second, independent defect:** its matched-noise control is **bit-identical** to the baseline it
  was meant to be distinguished from, and the pre-registered guard `matched_noise_verified_lifting:
  false` fired **without blocking the PASS**.

### 4c. The clean split — findings that are two claims joined at a seam

V3-EXQ-**711** and **713** carry interpretation labels that are literally two conjoined claims, and
they split exactly along the triage seam:

| | survives (SAFE) | withdrawn (DISQUALIFYING) |
|---|---|---|
| 711 | "ascending spiral gain **lets limbic win**" — a `>0` tick count; weight movement 4897.8 vs 1e-06 | "**does not convert** the ceiling" — 0.0993-nat shortfall, +65% exposure spread |
| 713 | "**bounded parity win**" — parity band on 4 seeds; saturation **exactly 0.0** | "**does not convert**" — shortfalls 0.0147 / 0.0511 nats |

V3-EXQ-**709** is **PASS-SAFE, no action owed**: its route rests on a strict `>0` count with
hard-zero seeds (708 sec 11 stands unchanged); the C1 conversion DV underneath is disqualified but
never became the finding. Note 709 carries **both** defect forms.

### 4d. Wholly disqualified findings

**710** (`weakens MECH-140/MECH-450`) — worst exposure asymmetry in the corpus (**+152%**), *and* its
ablation control `A2_ABLATED` is **bit-identical to `A0_OFF` on all six seeds** in entropy and tick
count, so the intended MECH-450 dissociation **was never measured at all**. A corrected DV alone
will not repair that.
**654f, 654g, 654i, 654j** — substantive `conversion_ceiling_persists` conclusions on the
disqualified `C2_committed_class_entropy_lift`. **654j seed 43 is 0.000102 from flipping the run to
PASS**; 654 seed 44 at 0.049953 and 654i seed 42 at 0.049605 are likewise inside contamination
scale. The "ceiling persists" reading is **not** protected by margin arithmetic.
**707, 707a** — same lineage, but already `superseded`: no live exposure.
**614c** — both verdict-bearing criteria are two-sided bands on a shape statistic.

**Directional note (654 family).** The bias here is *conservative*: ARM_ON carries the perturbation,
so if it perseverates less, a corrected measurement pushes lifts **down**, deepening the observed
nulls. That is an argument about the **sign**, not a rescue — per autopsy sec 4e the replication
factor is unobservable from these manifests, so the magnitude is unbounded.

### 4e. Verified SAFE — no action

**689g, 689e, 616, 614e, 643, 643a**, plus **700c** and **704** (requeued on SAFE magnitude-matching
gates violated by 10x and 44x — those verdicts stand independently). **614d** is the inverse of the
usual split: its **PASS** rests on a disqualified two-sided entropy band, while its substantive
**null** is SAFE (all arms identically 1.056572 — the committed stream is literally unchanged, so no
reweighting can manufacture a lift).

**700-family caution:** 700d and 704b each *removed* their script's only SAFE blocker via retune, so
re-running them uncorrected would turn **entirely** on a disqualified statistic. 700b is the sharp
one — both load-bearing conversion criteria read PASS behind a disqualified readiness gate, so
"700b nearly converted" must not be cited in either direction.

## 5. Recommended routing

1. **`/failure-autopsy` V3-EXQ-707b** — first, and note the 708 dependency.
2. **`/failure-autopsy` V3-EXQ-689d** — MECH-448's evidential base; alongside 699.
3. **710** — plus the independent bit-identical-ablation vacuity, which survives a DV fix.
4. **654f/g/i/j**, then **711/713** partial withdrawals (the "does not convert" halves only).
5. **614c/614d C1** — lower stakes; 614c already `non_contributory` and superseded.

**No manifest was edited.** Completed runs are re-adjudicated via `/failure-autopsy`, never
rewritten. This document records findings only.

## 6. Coverage and limits

- **~30 of 109** completed scripts were verified in depth (sections 4a-4e). The remaining ~79 are
  ranked candidates from the mechanical pre-screen and are **not** adjudicated here.
- The lint is a static AST scan sharing form 1's limitation class: exemptions are detected
  file-wide, and taint is **not** followed through user-defined helpers — so it **under-fires**
  rather than over-fires. 150 is a **lower bound**.
- The lint reports; it does not block. WARN-only in both modes.
- Three separate **vacuity signatures** turned up that are independent of hold-weighting and would
  survive a DV repair: 689d's matched-noise control, 707/707a's `A1_LOOPS ≡ ARM_DROP_LIMBIC`, and
  710's `A0_OFF ≡ A2_ABLATED`. All three are the 699 sec 11.6 tell — *two nominally independent
  readouts agreeing exactly is a defect signature, not a validation.*
