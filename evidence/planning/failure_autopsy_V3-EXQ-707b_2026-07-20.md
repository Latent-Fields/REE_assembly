# Failure Autopsy (RE-ADJUDICATION) -- V3-EXQ-707b (ARC-110 loop-segregation C2 release)

- **Generated (UTC):** 2026-07-20T06:07:48Z
- **Session:** `festive-grothendieck-fe529d`
- **Scope:** single (with a propagation section -- the consequences are not confined to this run)
- **Status:** confirmed (user-gated 2026-07-20)
- **Run:** `v3_exq_707b_arc110_loop_segregation_c2_release_20260629T144004Z_v3`
- **Queue:** V3-EXQ-707b (supersedes 707a/707; diagnostic; PROMOTES NOTHING)
- **Claim:** ARC-110 (parallel segregated cortico-BG-thalamic loops)
- **Supersedes for adjudication:** [`failure_autopsy_V3-EXQ-707b_2026-06-29.md`](failure_autopsy_V3-EXQ-707b_2026-06-29.md)
- **Origin:** [`hold_weighted_e3_readout_corpus_sweep_2026-07-20.md`](hold_weighted_e3_readout_corpus_sweep_2026-07-20.md) sec 4a
  (REE_assembly `4ceb7d22f9`), which named 707b the highest-consequence contaminated run in the corpus.

> **One line.** The load-bearing conversion DV is a hold-weighted committed-class entropy under a
> +98% arm-exposure spread; the A1-vs-null contrast that makes the design "decisive" is
> **sign-inconsistent across all three divergent seeds** and eight times smaller than the
> demonstrated contamination floor. The `weakens` on ARC-110 -- and the narrowing derived from it --
> are **WITHDRAWN**. The readiness battery **STANDS**, with two corrections. The withdrawal
> propagates to the V3-EXQ-708 re-adjudication and to an **in-flight** V3-EXQ-708a.

**NO MANIFEST WAS EDITED.** This document re-adjudicates only; `/governance` applies.

---

## 1. Facts -- the defect, confirmed at both ends

`committed_class_counts` is accumulated in
[`v3_exq_707b_arc110_loop_segregation_c2_release.py:1023-1035`](../../../ree-v3/experiments/v3_exq_707b_arc110_loop_segregation_c2_release.py)
on **every P2 env step**, gated only by `is_p2`:

```python
committed_class = int(action[0].argmax().item())   # :1006
...
if is_p2:
    n_p2_ticks += 1
    committed_class_counts[committed_class] = committed_class_counts.get(committed_class, 0) + 1
```

There is no `ticks["e3_tick"]` guard. `ree_core/agent.py:5429` returns the **held / trajectory-stepped**
action when `not ticks["e3_tick"]`, before `e3.select()` is reached. Cadence defaults to 10
(`utils/config.py:2017`) and is MECH-093-modulated 5-20 (`heartbeat/clock.py:52-70`). The histogram is
therefore weighted by **hold duration**, and `committed_class_entropy_nats` is an entropy over that
hold-weighted histogram -- the DISQUALIFYING class in the sweep's triage table (a distribution-shape
statistic; replication reweights the distribution itself, which is exactly what entropy measures).

No diagnostics latch is touched, so `e3_diagnostics_staleness_lint` (form 1) is structurally blind
here. This is defect **form 2**.

### 1a. Arm exposure spread -- why the 663 calibration does not apply

`n_p2_ticks` per (seed, arm), and the A1-vs-A0 spread:

| seed | A0_SINGLE_ARENA | A1_LOOPS | ARM_NOISE | ARM_DROP_LIMBIC | A1/A0 spread |
|---|---|---|---|---|---|
| 42 | 1625 | 2434 | 1700 | 1409 | **+49.8%** |
| 43 | 18389 | 18183 | 18072 | 18658 | -1.1% |
| 44 | 1581 | 1692 | 1813 | 1733 | +7.0% |
| 45 | 3297 | 6515 | 6241 | 4826 | **+97.6%** |
| 46 | 2536 | 2703 | 3374 | 3751 | +6.6% |
| 47 | 5580 | 4251 | 4325 | 4935 | **-23.8%** |

Per [`failure_autopsy_V3-EXQ-699_2026-07-20.md`](failure_autopsy_V3-EXQ-699_2026-07-20.md) sec 4d, the
663 matched-replay calibration (+0.01% / +0.64% / -0.87%) bounds the defect **only** where arm symmetry
cancels it *and* the DV is a continuous magnitude. Both exclusions bind here on all three of 4d's
grounds: the DV is an **entropy over a class histogram**, not a magnitude; the arms differ in **hold
duration** (the very quantity doing the weighting), so it does not cancel; and the spread is **one to
two orders of magnitude** above the 663 artifact scale. The calibration explicitly does not cover this
run.

Uniform replication would cancel under normalisation. It is not uniform: hold duration is
**class-dependent** (`_ncl_hold_ticks`, beta-gate elevation, and `_committed_trajectory` horizon all
vary with the committed program), and exposure is **arm-dependent** by up to +98%. That conjunction is
the mechanism of the distortion.

---

## 2. The finding -- WITHDRAWN

### 2a. The decisive argument: the null contrast has no resolving power

The pre-registered DECISIVE-weakens branch requires a **valid null** *and* A1 failing to lift above
A0/the null. The null comparison is the load-bearing half. Per divergent seed (42/44/46 -- the only
seeds that clear the divergence gate on all three C1 arms):

| seed | A1_LOOPS | ARM_NOISE (null) | **A1 - null** | C1 shortfall |
|---|---|---|---|---|
| 42 | 0.9238 | 1.0411 | **-0.1173** | 0.2672 |
| 44 | 0.9988 | 1.0666 | **-0.0678** | 0.1178 |
| 46 | 0.9602 | 0.7915 | **+0.1687** | 0.2159 |
| *pooled mean* | 0.8385 | 0.8232 | *+0.0153* | -- |

(C1 shortfall = `max(A0, ARM_NOISE) + 0.05 - A1`, the margin the criterion actually demands.)

The A1-vs-null contrast is **sign-inconsistent across all three divergent seeds**, with per-seed
magnitudes of 0.068-0.169 nats -- every one **inside or adjacent to** the 0.115-0.134 nat band that
699 demonstrated hold-weighting alone can move on a comparable driver. The pooled mean contrast of
+0.0153 nats is **eight times smaller** than that demonstrated floor, and its sign is an artefact of
averaging across seeds whose individual signs disagree.

So the instrument cannot distinguish `A1 > null` (the PASS branch) from `A1 ~ null` from `A1 < null`.
**The branch the run took was unreachable with this instrument**, and this holds regardless of which
direction the bias runs -- it is an argument about resolving power, not about sign.

This is a stronger and more robust kill than the C1 shortfall comparison, because it does not require
assuming the contamination is large enough to close a specific gap. It only requires that the
contamination is larger than the gap being resolved, which is measured and not in dispute.

### 2b. Supporting: C1 and C2 margins

- **C1 shortfalls** 0.1178 (s44) / 0.2159 (s46) / 0.2672 (s42). The nearest sits **inside** 699's
  demonstrated-reachable band; the other two exceed its top by 1.6x and 2.0x. Note s42 -- the largest
  shortfall -- is also the divergent seed with by far the worst exposure asymmetry (+49.8%), which is
  consistent with (though not proof of) exposure-driven distortion.
- **C2** (`A1 strict-above ARM_DROP_LIMBIC`): DROP 0.9328 vs A1 0.8385, a gap of **0.0943 nats** --
  squarely inside the demonstrated band. C2's verdict is indefensible on its own.

### 2c. Not recoverable by reanalysis

Per 699 sec 4e, the replication factor is **unobservable from the recorded emission**. This manifest
carries no per-tick sink, no `n_fresh_select` / `n_latched` telemetry, and no per-tick class stream --
only per-(arm, seed) scalars. The contamination cannot be divided out post hoc. A corrected **re-run**
is required; reanalysis cannot substitute.

---

## 3. The readiness battery -- STANDS, with two corrections

Per the 699 precedent, a defective instrument can leave the PASS/readiness correct while destroying the
finding. Adjudicated gate by gate, against the sweep's triage test:

| gate | measured / threshold | class | verdict |
|---|---|---|---|
| `in_layer_null_live` | 3.0 / 2.0 seeds | **SAFE** | **SURVIVES** |
| `frac_pre_ge2` | exactly 1.0, all 24 cells | **SAFE** (saturated) | **SURVIVES** |
| `named_channel_routing_live` | 1.414214 / 0.001 | **SAFE** (binary, see 3a) | **SURVIVES**, framing corrected |
| `loops_carry_live_cross_loop_variance` | 0.372 / 0.05 (7.4x) | AT RISK | probably survives; **not certified** |
| `learning_engaged` (delta_t non-flat) | 0.00287 / 0.0001 (28.7x) | AT RISK | probably survives; **not certified** |
| `enough_divergent_seeds` | **3.0 / 3.0** | **AT RISK, zero margin** | **NOT SAFE** (see 3b) |

`in_layer_null_live` rests on `loop_noise_active_ticks > 0` -- a strict `>0` test, threshold-invariant
per the sweep's SAFE rule. The record is clean and binary: 1700 / 18072 / 1813 / 6241 / 3374 / 4325 on
ARM_NOISE, and hard **zero** on A0 and A1. Replication cannot manufacture a positive from an all-zero
record. The same-layer null the single arena could not construct (the 704b/706b binding constraint) was
genuinely constructed and is genuinely live. **This is a real, retained positive result.**

`frac_pre_ge2` is exactly 1.0 on every one of the 24 arm-seed cells -- saturated, nowhere to move.

### 3a. Correction 1 -- `named_channel_routing_live` survives, but not for the recorded reason

The gate is carried entirely by the `vigour` channel at **exactly 1.414214 = sqrt(2)**, on **every arm
and every seed** -- zero variance across the whole 24-cell design -- against `{}` / 0.0 when routing is
off:

```
s42 A0_SINGLE_ARENA  {}                                          live=False
s42 A1_LOOPS         {..., "ofc":0.727955, "vigour":1.414214}    live=True
s42 ARM_NOISE        {..., "ofc":0.431601, "vigour":1.414214}    live=True
s42 ARM_DROP_LIMBIC  {..., "ofc":0.367976, "vigour":1.414214}    live=True
```

`named_routed_ranges[name] = (_ov.max() - _ov.min())` over the routed projection from
`project_channel_range` (`e3_selector.py:1701`, projection at `:124`). A value pinned to sqrt(2) with
zero variance across 24 cells is a **structural constant of that projection**, not a measured substrate
property.

The consequence cuts **in favour of** survival: a constant cannot be reweighted by replication, so the
gate is strictly threshold-invariant -- it is a **binary liveness indicator (0 vs sqrt(2))**. But the
2026-06-29 framing "`named_channel_routing_live` 1.414 >> 0.001" reads as a 1414x margin on a graded
magnitude, and it is not one. It certifies **"routing is on and non-degenerate"** -- which is exactly
what it was built to do, and it does cleanly separate 707's vacuous `DROP == A1` byte-identity from
707b's live routing. It does **not** evidence that the limbic channel carries *substantial*
per-candidate competition. The 2026-06-29 note's "the limbic loop carried real per-candidate range
(1.414)" overstates this and should be restated as a liveness assertion.

### 3b. Correction 2 -- `enough_divergent_seeds` cleared at literally zero margin

Measured **3.0** against threshold **3.0**. Its input is
`consumed_summary_pairwise_dist_mean`, a continuous mean-of-magnitudes accumulated per env step from
**cached** candidates (`agent.py:4812` returns cached candidates on a non-E3 tick -- the same defect
family, MECH-057a). Per (seed, arm), against the 0.05 floor:

| seed | A0 | A1 | ARM_NOISE | divergent (all three > 0.05)? |
|---|---|---|---|---|
| 42 | 0.07976 | 0.13021 | 0.07542 | YES |
| 43 | 0.02710 | 0.06173 | 0.08149 | no |
| 44 | 0.12805 | 0.18622 | 0.08168 | YES |
| 45 | 0.04414 | 0.02339 | 0.03453 | no |
| 46 | 0.10031 | 0.10685 | 0.08200 | YES |
| **47** | **0.04936** | 0.10158 | 0.07145 | **no -- misses by 0.00064 (1.3%)** |

Seed 47 fails the gate on its A0 arm by **six ten-thousandths of a nat-equivalent, 1.3% of the floor**,
on a statistic drawn from the contaminated cache path, on the seed with the design's second-worst
exposure asymmetry (-23.8%). One seed crossing flips `n_divergent` 3 -> 4 and changes both the C1 and
C2 denominators. **The design had zero headroom on its own admission gate.**

This is independently corroborated: V3-EXQ-708a's queue note already flags the identical condition in
708 ("`enough_divergent_seeds` cleared at EXACTLY threshold in 708 (3.0/3.0, zero headroom) -- one lost
divergent seed self-routes requeue") and adds a guard for it. It is a **lineage-wide fragility**, not a
707b quirk, and 707c must guard it.

Neither correction overturns the readiness verdict. The substrate was built and is demonstrably live;
that remains a real positive datum about the `v4_loop_segregation` build. What is withdrawn is the
*conversion measurement made on top of it*.

---

## 4. Recording provenance -- an independent gap

`ree-v3/validate_recording.py --paths <manifest>`:

```
missing recording_schema, substrate_hash, machine_class, elapsed_seconds, config, seeds
```

Six always-core fields absent (`result.seeds` exists; the top-level field does not). **No
`substrate_hash`** means we cannot confirm which substrate executed -- so even the retained readiness
verdict is provenance-unpinned, and no arm reuse is possible from this run. This is the same gap 708
had ("708 recorded no substrate_hash at all while every cell fingerprint had one"), and 708a's repair
list already fixes it by hoisting `arm_results` to the manifest top level so the multi-arm hoist fires.
707c must do the same.

This is **recording-debt**, not measurement-debt: the fields existed at run time and were discarded.
The repair is *recording them*, per
[`experimental_recording_standard_2026-07-12.md`](experimental_recording_standard_2026-07-12.md)
sections 3b/3c.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear -- not tested** | ARC-110's single-arena-artefact hypothesis was never validly measured; it is neither weakened nor supported |
| Biological reference | **clear (unchanged)** | Alexander/DeLong/Strick parallel segregated loops; real and load-bearing. Untouched by this re-adjudication -- an instrument defect cannot bear on biology |
| Prerequisites / dependency | **unknown** | the DA-gated-arbitration inference was *derived from* the contaminated contrast; it does not survive as an empirical finding (see 6) |
| Implementation completeness | **partial, and demonstrated live** | loop structure built; `in_layer_null_live` + routing-live retained. Cross-loop arbitration remains static arithmetic -- a **design fact**, not a finding of this run |
| Environment adequacy | adequate | unchanged; same GAP-A reef-bipartite substrate as the matched 704b arms |
| Measurement adequacy | **DEFECTIVE (dominant)** | hold-weighted entropy DV; null contrast 8x below the demonstrated contamination floor; admission gate at zero margin |
| Integration adequacy | unknown | rested entirely on the withdrawn C1/C2 |
| Scale / capacity | adequate | not the binding constraint |

**Dominant diagnosis: `measurement_test_design_defect`.** Not `substrate_ceiling` -- the run never
validly measured the quantity whose ceiling was inferred.

---

## 6. What the withdrawal reaches (user-confirmed: finding AND narrowing)

The 2026-06-29 autopsy's routing #1 **narrowed** ARC-110 to "loop segregation is
necessary-but-not-sufficient; alone, with static arithmetic arbitration, it does not lift the
F-dominance ceiling; the conversion route requires coupling with learned/dopamine-gated cross-loop
arbitration (MECH-448/449/ARC-107)."

That narrowing is **also withdrawn**. Its empirical premise was precisely `A1_LOOPS ~ A0_SINGLE_ARENA`
-- the contaminated contrast. The DA-gated-arbitration argument remains a **live and well-motivated
biological hypothesis** (it is what the BG-assembly map independently predicts, and it is unaffected by
any instrument defect), but 707b is **not evidence for it**. It must be re-derived from a corrected run
or carried as a prior, not cited as an empirical finding.

ARC-110 therefore returns to **untested on this question** -- not narrowed, not weakened.

---

## 7. Propagation

### 7a. The V3-EXQ-708 repair leg -- UNSUPPORTED

[`failure_autopsy_V3-EXQ-708_2026-07-19.md`](failure_autopsy_V3-EXQ-708_2026-07-19.md) sec 5a
withdrew 708's DV, removing one of the two legs of the cluster's convergence argument, then repaired
the remainder by recruiting 707b verbatim:

> "...and V3-EXQ-707b subsequently returned a `non_degenerate: true` valid null concluding the
> conversion ceiling is **intrinsic to MECH-439 F-dominance, not a single-arena artefact**."

That repair now rests on a withdrawn instrument and **fails**.

### 7b. Illusory-conflict check (MANDATORY -- and this is the serious finding)

The standing rule requires checking what the *remaining* support looks like whenever a reading is
withdrawn. 708 sec 5a named the fallback: the ceiling reading "retains 700d plus the
700b / 700c / 704b-706b lineage."

Cross-referencing that fallback against the **same corpus sweep** (sec 4e):

| named fallback | sweep verdict | usable as ceiling support? |
|---|---|---|
| **700d** | "removed its script's only SAFE blocker via retune -- re-running uncorrected would turn **entirely** on a disqualified statistic" | **no** |
| **704b** | same retune finding as 700d | **no** |
| **700b** | "both load-bearing conversion criteria read PASS behind a disqualified readiness gate -- '700b nearly converted' **must not be cited in either direction**" | **no** |
| **700c** | verified SAFE -- but a **readiness requeue** (magnitude-matching gate violated 10x) | not a ceiling finding |
| **704** | verified SAFE -- but a **readiness requeue** (violated 44x) | not a ceiling finding |
| **706b** | not adjudicated in the sweep | unknown |
| **708** | withdrawn by its own re-adjudication | **no** |
| **707b** | withdrawn here | **no** |

**Conclusion: withdrawing 707b does not leave a single-legged convergence argument -- it leaves NO
uncontaminated positive leg.** The two SAFE members are readiness requeues, which establish that those
arms were not ready; they do not positively establish a ceiling. This is exactly the
illusory-conflict-resolution hazard the standing rule exists to catch: the remaining "supports" are
narrow, single-pathway, or absent.

The MECH-439 intrinsic-ceiling reading is **NOT REFUTED** -- no corrected run has tested it either way.
It is **currently unsupported by any uncontaminated run**, and must not be cited as established until
one exists. Recorded here so the narrowing is visible rather than silently absorbed.

### 7c. V3-EXQ-708a -- LIVE, and its venue narrowing rests on the withdrawn premise

`V3-EXQ-708a` is **`status: claimed`**, machine `ree-cloud-2`, claimed **2026-07-20T05:23:08Z**,
`estimated_minutes: 900`. It is running now. Its queue note states:

> "**VENUE: ARM_NOISE_LOOPSEG DROPPED (708 ran 4 arms, 708a runs 3)** -- V3-EXQ-707b returned
> `evidence_direction=weakens` on the single-arena-artefact sub-hypothesis with a valid
> `non_degenerate` null, concluding the conversion ceiling is intrinsic to MECH-439 F-dominance, so
> the route-to-ARC-110 outcome branch is **settled and is deliberately not offered**; ARC-110 is
> neither tagged nor tested."

An entire arm was dropped on 707b's authority. The same justification appears in the script docstring
and mirrors 708 sec 10's "Note on venue."

**Disposition (user-confirmed): LET IT RUN.** 708a tests **MECH-440**, not ARC-110, on a **repaired**
instrument (fresh-select-only DV, `n_fresh_select`/`n_latched` telemetry, per-arm-seed exposure
recording, a `fresh_selects_sufficient` readiness guard, `stamp_recording_core`). None of that is
touched by this withdrawal, so **708a's MECH-440 verdict will be sound**. Aborting a ~15-hour in-flight
run that will return a valid answer would destroy real work for no epistemic gain.

**What must change is the record, not the run.** The dropped-arm justification is now false in its
operative clause: the route-to-ARC-110 branch is **UNMEASURED, not settled**. Consequences:

1. 708a's result must **not** be read as bearing on ARC-110 or the loop-segregation route in either
   direction. It is silent on that question by construction.
2. The ARC-110 loop-segregation question is recovered by the corrected **707c** (section 8), **not** by
   re-running 708a and **not** by restoring the arm to 708a.
3. Governance should annotate the 708a queue note / manifest on landing so the "settled" clause does
   not propagate further. This autopsy is the citable basis.

### 7d. Scope flag -- NOT adjudicated here

- The pre-registered contingent `/claim-synthesis` on MECH-439 **did fire** on 707b's authority
  ([`claim_synthesis_MECH-439_2026-06-29.md`](claim_synthesis_MECH-439_2026-06-29.md), generated
  2026-06-29T19:35:04Z, 23 minutes after the 707b autopsy). Its verdict was **"REFUSE new-child
  decomposition -- the cluster is ALREADY METABOLIZED"**, so **nothing phantom entered the registry**
  and no child claim needs unwinding. Its closing recommendation ("apply the deferred 2026-06-20
  narrow-and-retain") did cite 707b as the supplying evidence, but MECH-439 was subsequently moved by a
  different mechanism -- the 2026-07-09 GOV-CEIL-1 ceiling-exhaustion demotion -- which supersedes that
  framing. Net live consequence: **none requiring action here.**
- **Flagged, not adjudicated:** MECH-439's GOV-CEIL-1 demotion rests on 10 confirmed
  `substrate_ceiling` hits (689a / 700 / 700a / 700b / 700c / 700d / 709 / 710 / 711 / 713). At least
  700b, 700d, 710, 711 and 713 appear in the sweep's contaminated or partially-withdrawn set. **707b is
  NOT in that list**, so this autopsy does not change the count and does not re-open the demotion. The
  sweep already routes 710 / 711 / 713 to their own autopsies; the demotion's evidential base should be
  re-totalled once those land. Out of scope for a 707b re-adjudication.

---

## 8. Routing -- `queue-experiment`, corrected re-run V3-EXQ-707c (NOT QUEUED HERE)

**Node class:** `complicated (buildable)` -- the fix is a named instrument repair with no open
question. Not `complex (probe-gated)`: nothing needs discovering to build 707c.

**NOT `implement-substrate`.** The substrate is built and was demonstrated live (section 3). This is
instrument repair of a run that never validly measured its DV -- the V3-EXQ-785 -> 785a and 708 -> 708a
shape, which the corpus already sanctions.

Same scientific question -> **alphabetic suffix, V3-EXQ-707c**. Required properties:

1. **Fresh-select-only DV.** Accumulate `committed_class_counts` only on a genuine E3 tick -- gate on
   `ticks["e3_tick"]`, or clear-and-check the latch immediately before every `select_action` and record
   only if repopulated (pattern:
   `experiments/v3_exq_785a_mech463_arousal_exogenous_urgency_decomp.py:525-543`).
2. **Emit the replication factor.** `n_fresh_select`, `n_latched`, `fresh_select_yield` per arm-seed, so
   it is visible in the manifest rather than inferred.
3. **Record per-arm-seed exposure.** `n_p2_ticks` and `exposure_imbalance_vs_A0` -- reported, never
   gating. The +98% spread is the mechanism of the distortion and must be on the record.
4. **`fresh_selects_sufficient` readiness guard** (>= 30 genuine fresh selects per arm-seed) so an
   honest-but-underpowered DV self-routes `substrate_not_ready_requeue`, **never a false weakens**
   (708a's pattern).
5. **Divergence-headroom guard -- NEW, from section 3b.** `enough_divergent_seeds` cleared at exactly
   3.0/3.0 with seed 47 missing by 1.3%. Require headroom (>= 4 divergent seeds), or report the per-seed
   margin and self-route requeue at zero headroom. Do not repeat a design whose admission gate has no
   slack.
6. **Instrument the limbic-routing gate as a graded quantity** (section 3a). The current statistic is
   pinned at sqrt(2) and carries only liveness. Add a magnitude readout so the C2 non-degeneracy claim
   rests on measured per-candidate competition, not a structural constant.
7. `supersedes: "V3-EXQ-707b"` on both the queue entry and the manifest.
8. `stamp_recording_core(...)` -- closing all six always-core gaps from section 4, hoisting
   `arm_results` to the top level so the multi-arm `substrate_hash` hoist fires.

**Re-derive brake: NOT FIRED**, following the 708 precedent exactly. The recommended category is
`measurement_test_design_defect`, so the counting rule (`substrate_ceiling` / `non_contributory`-as-
ceiling) is not met. The 2026-06-29 autopsy stamped `fired: false` with direction `weakens`; this
re-adjudication **withdraws** that reading rather than adding a second, so ARC-110's ceiling count moves
to **0, not 2**. A corrected re-run is not the behaviour the brake exists to prevent -- the brake stops a
claim being re-tested at the same granularity against the same ceiling letter after letter, whereas
707c is instrument repair of a run that never validly measured its DV.

**Granularity-debt recurrence trigger: NOT FIRED.** A prior autopsy on this target exists
(`failure_autopsy_V3-EXQ-707b_2026-06-29`), which is the literal trigger condition. But the trigger
looks for a *second failure signature circling the same claim* -- evidence the claim is several claims.
This is a **re-adjudication of the same run on instrument grounds**, not a second independent failure.
Recording it as granularity debt would be a false positive. Stamped honestly in the JSON so
`check_granularity_debt_recurrence.py` (GOV-GRAN-1) can see the reasoning.

**Hypothesis-space ledger (Step 9b): SKIPPED, cleanly.** No `fanout_recommendation` is emitted (the
bottleneck routes to one unambiguous re-run, the documented exemption), and 707b has **no pre-registered
leg** in `hypothesis_space_registry.v1.json` -- no question carries ARC-110, and no entry references
707b or the single-arena-artefact hypothesis. There is nothing to resolve and nothing to un-eliminate.
The registry was **not modified**.

---

## 9. Learning extracted

1. **A hold-weighted entropy DV can destroy a finding while leaving the readiness battery intact** --
   the 699 precedent, now confirmed a second time on a structurally different design. Adjudicate the
   two separately, always.
2. **Resolving power beats margin arithmetic as a withdrawal argument.** The decisive fact here was not
   "the shortfall is inside the contamination band" (true for only 1 of 3 seeds) but "the null contrast
   is sign-inconsistent and 8x below the contamination floor." The former needs an assumption about
   magnitude; the latter does not, and holds whichever way the bias runs.
3. **A gate with zero variance across an entire design is a structural constant, not a measurement.**
   `vigour = sqrt(2)` on all 24 cells. It survives contamination for exactly that reason -- but its
   margin language must not be read as evidential content. Zero variance is a prompt to check the
   generating expression, not a strong result.
4. **Check the admission gate's headroom, not just whether it passed.** `enough_divergent_seeds` at
   3.0/3.0 with a 1.3% miss on a fourth seed is a design with no slack, on a statistic from the
   contaminated cache path. The same zero-headroom condition independently appears in 708 -- it is a
   lineage-wide fragility.
5. **A withdrawal's illusory-conflict check must be run against the CURRENT corpus state, not the state
   at the time of the reading being repaired.** 708 sec 5a's fallback lineage was written before the
   corpus sweep existed; re-checking it against the sweep converts "single-legged" into "no
   uncontaminated leg." A repair that names a fallback is only as good as that fallback's own
   adjudication status at the time of the check.
6. **A withdrawn verdict can already be embedded in an in-flight experiment's DESIGN, not just in
   prose.** 708a dropped an arm on 707b's authority and is running now. Propagation audits must check
   the live queue and claimed items, not only the document corpus -- and the proportionate remedy is
   usually to annotate the record, not to abort a run whose own question is unaffected.
7. **A derived narrowing falls with the finding that derived it.** The DA-gated-arbitration hypothesis
   survives as biology, but 707b is not evidence for it.

---

## 10. Draft `evidence_quality_note` for ARC-110 (for `/governance`; NOT written here)

> **WITHDRAWN 2026-07-20** (`failure_autopsy_V3-EXQ-707b_2026-07-20`, user-confirmed; supersedes the
> 2026-06-29 autopsy and the note it produced). V3-EXQ-707b's `weakens` on the single-arena-artefact
> sub-hypothesis is withdrawn as a **measurement/test-design defect**, and the narrowing derived from it
> ("necessary-but-not-sufficient; requires learned/DA-gated cross-loop arbitration") is withdrawn with
> it. DEFECT: the load-bearing C1/C2 DV `committed_class_entropy_nats` is accumulated per ENV STEP from
> `int(action[0].argmax())` (driver :1023-1035) with no `e3_tick` guard, while `agent.py:5429` returns
> the HELD action before `e3.select()` -- so the class histogram is weighted by hold duration
> (defect form 2; `e3_diagnostics_staleness_lint` is structurally blind to it). DISQUALIFYING on both
> counts: an entropy over a class histogram is a distribution-shape statistic, and arm exposure differs
> by up to **+97.6%** (A1 vs A0: +49.8% s42, +7.0% s44, +6.6% s46 on the divergent seeds), so it does
> not cancel. The 663 calibration (<1%, sign-varying) explicitly does not apply (autopsy 699 sec 4d:
> different statistic class, different arm symmetry, 1-2 orders of magnitude). DECISIVE: the A1-vs-null
> contrast that the pre-registered DECISIVE branch depends on is **sign-inconsistent across all three
> divergent seeds** (-0.1173 s42, -0.0678 s44, **+0.1687** s46), every magnitude within/adjacent to the
> 0.115-0.134 nat band 699 demonstrated hold-weighting alone can move; the pooled +0.0153 nat contrast
> is **8x below** that floor. The instrument cannot distinguish A1>null from A1~null from A1<null, so the
> branch taken was unreachable regardless of bias direction. C1 shortfalls 0.1178/0.2159/0.2672; C2 gap
> 0.0943 (inside the band). NOT recoverable by reanalysis (no per-tick sink, no fresh-select telemetry).
> **READINESS BATTERY STANDS**: `in_layer_null_live` (strict >0 tick count, 1700-18072 on ARM_NOISE vs
> hard zero on A0/A1 -- threshold-invariant; the same-layer null the single arena could NOT construct
> was genuinely built and is genuinely live, a RETAINED positive result) and `frac_pre_ge2` (exactly 1.0,
> all 24 cells, saturated). `named_channel_routing_live` also survives but the "1.414 >> 0.001" framing
> is CORRECTED: it is carried by `vigour` at exactly sqrt(2) on every arm and seed (zero variance across
> 24 cells) vs 0.0 when off -- a structural constant of `project_channel_range`, hence a BINARY liveness
> indicator, not a graded magnitude. It certifies routing is on and non-degenerate (and does cleanly
> resolve the 707 vacuous DROP==A1); it does NOT evidence substantial limbic per-candidate competition.
> CAUTION: `enough_divergent_seeds` cleared at EXACTLY threshold (3.0/3.0) with seed 47 missing the 0.05
> floor by 0.00064 (1.3%) on a statistic drawn from the contaminated cache path (`agent.py:4812`) --
> zero headroom; the identical condition is flagged in 708. Substrate build itself SUCCEEDED (positive
> datum, unchanged). ARC-110 returns to **untested on the single-arena-artefact question** -- neither
> weakened nor narrowed. Stays candidate / substrate_conditional / PROMOTES NOTHING;
> `awaiting` -> corrected re-run V3-EXQ-707c. RECORDING GAP: 6 always-core fields absent
> (`recording_schema`, `substrate_hash`, `machine_class`, `elapsed_seconds`, `config`, `seeds`) -- no
> `substrate_hash`, so provenance is unpinned and no arm reuse is possible. PROPAGATION: the V3-EXQ-708
> re-adjudication (sec 5a) recruited 707b to repair the leg its own withdrawal broke, and (sec 10)
> redirected 708a's design away from the loop-segregation bet -- **both unsupported**. V3-EXQ-708a is
> IN FLIGHT (claimed ree-cloud-2 2026-07-20T05:23:08Z) having DROPPED ARM_NOISE_LOOPSEG (4 arms -> 3) on
> this now-withdrawn authority; it is correctly allowed to complete (its MECH-440 question and repaired
> instrument are unaffected), but the route-to-ARC-110 branch is **UNMEASURED, not settled**, and 708a
> must not be read as bearing on ARC-110 in either direction. ILLUSORY-CONFLICT CHECK: 708 sec 5a's
> named fallback (700d + the 700b/700c/704b-706b lineage) is itself largely disqualified by the same
> corpus sweep -- 700d and 704b turn entirely on a disqualified statistic, 700b must not be cited in
> either direction, 700c/704 are SAFE but are readiness requeues rather than ceiling findings, 706b
> unadjudicated. The MECH-439 intrinsic-ceiling reading therefore has **NO uncontaminated positive leg**;
> it is NOT refuted, but must not be cited as established pending 707c.

---

## 11. Recommended governance writes (NOT applied here)

| target | write |
|---|---|
| ARC-110 manifest record | `evidence_direction`: `weakens` -> **`non_contributory`**; `epistemic_category` -> **`measurement_test_design_defect`** |
| ARC-110 claim | replace `evidence_quality_note` with section 10; `awaiting` -> corrected re-run **V3-EXQ-707c**; status/confidence otherwise unchanged (`candidate` / `substrate_conditional` / PROMOTES NOTHING) |
| ARC-110 narrowing | **withdraw** the 2026-06-29 necessary-but-not-sufficient narrowing (section 6) |
| V3-EXQ-708 autopsy | annotate sec 5a + sec 10: the 707b repair leg and the 708a venue note are **unsupported**; the ceiling reading has no uncontaminated leg (section 7b) |
| V3-EXQ-708a | on landing, annotate the queue note / manifest: the ARC-110 branch is **unmeasured, not settled**; 708a is silent on ARC-110 by construction (section 7c) |
| MECH-439 | **no write from this autopsy.** 707b is not in the GOV-CEIL-1 10-hit set. Flag only: re-total the demotion's base once the sweep's 710/711/713 autopsies land (section 7d) |
| `review_tracker.json` | **no write** -- per standing rule, `/failure-autopsy` does not mark reviewed; that is governance Step 5's call |
