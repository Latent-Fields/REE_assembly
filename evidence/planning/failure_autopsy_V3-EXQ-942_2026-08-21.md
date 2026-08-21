# Failure autopsy -- V3-EXQ-942 (INV-013 E-ladder realised timescale separation)

- **Generated (UTC):** 2026-08-21T01:34:30Z
- **Scope:** single
- **Status:** confirmed 2026-08-21T01:56:34Z (Step 8: confirm as written). Step 7c CONFIRMED (C1 recomputes false from per_seed cells). Step 9b applied at confirmation: new qid `e-ladder-realised-timescale-separation`.
- **Session:** failure-autopsy-batch-20260821
- **Dry-run gate:** `check_dry_run_citations.py` on run_id + queue_id -- 0 dry cited, 1 clean. Manifest `dry_run` absent. `dry_run_unreachable_criterion` lint silent on this driver. This is a full production run, not a smoke.

Facts reconstruction (no verdict) lives at `_scratch/autopsy-batch-20260821/942/facts.md`.

## 1. The headline

**The self-route `substrate_not_ready_requeue` is the wrong reason this run FAILed. C1 was reachable, and it comes out inverted -- the same "content, not timescale" shape the three pre-run structural findings already predicted.**

The manifest voids the designed DV because the worst seed recorded 899 eval steps against a 3000 floor. That sentence is a claim about the data, and the same manifest contradicts it:

- Seeds 11 and 23 each recorded **3750** steps (25 episodes * 150, zero early `done`). That is 25% above the floor.
- Seed 37 recorded **899** steps across the same 25 eval episodes (~36 steps/episode) -- a survival under-run, not a truncated budget and not an untrained substrate.
- All three variance floors **met**, including on seed 37 (worst-seed var_dz_world 8.21e-5 vs 1e-8).
- Half-lives and lag-k autocorrelations are present and finite on every seed. Seed 37 has n_dz=874; C1's half-life only needs MAX_LAG+2=12 samples.
- Recomputing `_monotonic_verdict` from the manifest's own `per_seed` cells: **monotonic_ordering_confirmed = false** on all three seeds, and still false if seed 37 is dropped.

The 2026-08-20 V3-EXQ-939 autopsy rejected a `substrate_not_ready_requeue` self-route when the designed DVs had come out *clean*. This run's designed DV also came out -- as a FAIL of monotonic persistence, in the inverted direction, on the two fully-powered seeds independently. The self-route's implication that "nothing was measured" is false.

Unlike 939, the 3000 floor is **not** a lattice-defective / mis-aggregated copy of C1. It is a real worst-seed survival miss. It is still the wrong reason to void C1.

## 2. Was C1 reachable at 899 steps?

Yes. Three independent reachability checks, all from source + the manifest's own cells:

1. **Computational.** `_halflife` / `_compute_autocorr` require `len(series) >= lag+2`. At MAX_LAG=10 that is 12 samples. Seed 37 has 874 deltas. Every reported autocorr at lags 1, 2, 5, 10 is finite.
2. **On the two seeds that cleared 3000.** Seeds 11 and 23 never needed the 899-step series. Their half-lives are (4,3,3) and (3,3,2). C1 on those two alone: e1_to_e2 delta mean -0.5 (sd 0.5), e2_to_e3 delta mean -0.5 (sd 0.5), both margin_met false. Designed tau(E1)<tau(E2)<tau(E3) is inverted on both fully-powered seeds.
3. **C1 does not use n_steps as its statistic.** The load-bearing criterion is the mean of per-seed half-life *deltas*. The 3000 floor is EXQ-019's unmet C4, copied as a power preference. The driver's own `ANCHOR_REACHABILITY_EXEMPT` justifies the *variance* floors as the degeneracy definition; the step-count floor is extra, and it is what fired.

Seed 37's tau_e1=6 is an outlier vs 4 and 3, so the short seed adds noise -- it does not create the inversion. Dropping it leaves the inversion intact.

## 3. The gate vs 939 -- same self-route label, different defect

| 939 (REJECTED self-route) | 942 (this run) |
|---|---|
| Designed DVs **passed** | Designed C1, if scored, **fails** (inverted) |
| One cell missed a control by 0.0067 | One seed survived ~36 steps/episode vs 150 |
| Gate statistic = DV statistic, harsher aggregation (min vs mean) | Gate statistic (n_steps) is **not** C1's statistic (half-life delta) |
| Threshold unreachable on a 1/30 lattice | Threshold 3000 is reachable -- 2/3 seeds hit 3750 |
| MIN_VALID_SEEDS=4 was dead code | No per-seed tolerance exists at all (zero-tolerance min conjunction) |
| Substrate declared unready was already validated | Warmup ran; two seeds produced a frozen-policy full-horizon eval |

So: **not a 939-class defective gate.** It is a real budget/survival miss on seed 37, used as a P0 veto of a DV that does not depend on that miss. The self-route is **vacuous as a reading of C1**, not as a description of seed 37.

`criteria_non_degenerate.C1_monotonic_ordering_confirmed: false` is hardcoded in the `P0NotReady` branch (`v3_exq_942_...py:409`), not computed from `check_degeneracy`. The three variance series are all above floor. The degeneracy flag is the step-count conjunction wearing C1's name.

## 4. What the numbers actually say (the empirical half of the pre-run structural picture)

Three source-verified findings were already in hand before this run (planning doc 2026-08-20T06:34:48Z; WORKSPACE_STATE 2026-08-20T06:37:06Z). This run is the empirical half.

**Designed tick ladder (clock counters):** e1:e2 matches 1:3 exactly on the full seeds (3750:1250). e3 does **not** match 1:10 -- 572 / 633 / 354 ticks vs expected 375 / 375 / 90 -- because `e3_tick` also fires on MECH-091 phase reset (`clock.py:149-154`). The planning doc's "structurally guaranteed 1:3:10" is true of e1:e2 and false of e3. That ratio still does not answer the realised-persistence question.

**Realised persistence (C1, recomputed):** mean tau_e1 4.33 > tau_e2 3.00 > tau_e3 2.67 on all three seeds -- the **opposite** of tau(E1)<tau(E2)<tau(E3). Autocorr has decayed to ~0 by lag 10 on every channel, matching EXQ-019's underpowered E1-vs-E2 picture (both near zero by lag 5-10). The one genuinely E3-cadence discrete channel (`is_committed`) never flipped (`n_runs=1` on every seed, mean_run_length = n_steps): the secondary DV is stuck-committed, so it cannot speak to E3 persistence either.

**Tick-flag consumers, re-checked on the live tree:** `ticks["e1_tick"]` and `ticks["e3_tick"]` are consumed in `agent.py`. `ticks["e2_tick"]` is still dead -- computed, never read, no `_e2_tick` method. The agent module docstring still claims an E2 tick gated on N_e2.

This is the MECH-058/EXQ-019 fate, now measured with E3's selection machinery actually in the loop, on two fully-powered seeds plus one short one, with a substrate_hash. The structural prediction was that continuous state would not show loop-paced persistence. The empirical half agrees.

## 5. Claim layer -- INV-013 was the wrong tag for this DV

INV-013 is a **derivational** architectural audit: a mechanism for predictive / iterative / multi-timescale exists in the running substrate. Its own `what_would_answer` delegates "GENUINELY realized vs merely labeled" to ARC-001 / ARC-002 / ARC-004, and says INV-013 "only certifies that a mechanism for each of the three properties exists." Its falsifier is removal or dead-coding of the *only* mechanism realizing one of the three, not "autocorrelation half-lives are statistically indistinguishable."

C1 is ARC-004's criterion, pointed at E-loops rather than L-space. The run therefore:

- does **not** test INV-013 under conditions where INV-013 could be confirmed or falsified;
- **does** produce a diagnostic reading of realised E-loop persistence, which INV-013 explicitly does not own;
- **bears on** ARC-004 (same measurement, different layers), ARC-023 (three loops at characteristic rates -- functional analog), and SD-006 (implemented async multi-rate -- implemented as clock counters, not as rate-gated continuous state).

Those three are `read_across_not_adjudicated`. This artifact does not dispose them.

Dead `e2_tick` is a live INV-013 *non-degeneracy* observation (a property satisfied only as a clock counter, never consumed). It does not by itself falsify INV-013: E1 vs E3 tick gating still exists, and sleep is the other half of the MULTI-TIMESCALE confirming example. Do not demote.

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (INV-013 not exercised) | Tagged claim is an existence audit; the DV is ARC-004's realised-timescale criterion on E-loops. |
| Biological reference | partial | Closest: thalamic-paced cortico-striatal loops / EEG-band analogy (ARC-023, SD-006). Mixed claim_level -- functional analog is distinct update rates, not literal oscillations. Lit present for ARC-023 (5) and SD-006 (2); none dedicated to INV-013. Not a formal-definition import. |
| Developmental / dependency prerequisites | present | Warmup ran (`warmup_train` 40 episodes). Two seeds produced full-horizon frozen-policy eval. Seed 37's early death is post-warmup survival variance, not a missing SD. |
| Implementation completeness | partial | Clock ladder exists. E3 discrete path is tick-gated. Continuous representations (z_world, z_self, E3 precision) update every env step. `e2_tick` is dead. |
| Environment adequacy | adequate | CausalGridWorldV2 is a sufficient bed for latent-delta autocorrelation. Two seeds survived the full 150-step horizon. Seed 37 dying early is not "the grid is too sparse for the DV." |
| Measurement adequacy | misleading (the recorded FAIL) / adequate (C1 itself) | Half-life at max_lag=10 is a fair instrument for this question. The P0 min-steps conjunction is what voided it. |
| Integration adequacy | partially coupled | E3 selection is in the loop (unlike EXQ-019's random actions). Continuous E3 precision is still the every-tick channel. |
| Scale / capacity | adequate for C1 | 3750 steps on two seeds; 874 deltas on the short seed, both well above the 12-sample computational floor. 3000 is a copied power preference, not a reachability bound. |

### Failure-location summary (GOV-FAILLOC-1)

- **MECHANISM FAILED:** `partial` -- the wiring does not rate-gate continuous state, and the inverted taus are what that wiring predicts. Implementation is not `complete`, so this is not a fair-test mechanism failure and is not chargeable as REE FAILED.
- **MEASURES FAILED:** `established` -- the recorded outcome FAIL is the P0 worst-seed step floor, which does not guard C1's statistic and voided a reachable DV. Not a 939 lattice defect; still a measurement-layer veto of a computed result.
- **ENVIRONMENT FAILED:** `not_established`.
- **REE FAILED:** false.

**Net classification: MIXED (MECHANISM partial + MEASURES established), not chargeable to REE alone.**

## 7. Recurrence

Granularity-debt trigger: **does not fire.** `granularity_debt_cluster.py INV-013` -- 0 tagging targets across 0 files, no `weakened` alignment to distribute. This would be the first tagging autopsy.

Re-derive brake (R1-R3): **does not fire.** INV-013 confirmed tagging runs 0, ceiling hits 0. This artifact stamps `standard` (blanket) / keeps INV-013 `derivational` (per-claim). Explicitly **do not** stamp `substrate_ceiling` -- that would take INV-013 from 0 to 1 and arm the brake against a claim this run did not test.

Same-question re-queue (V3-EXQ-942a with a lower floor, or more eval budget so seed 37 hits 3000): **declined**, as `complex (probe-gated) / mystery (known data)`. Two full-budget seeds already invert; more steps on the short seed cannot flip them. That refusal is the brake's *spirit*, not a brake firing.

## 8. Routing (confirmed 2026-08-21T01:56:34Z)

**`governance-note-only`.** INV-013 STANDS. Record the diagnostic reading (C1 inverted; structural findings empirically matched; self-route rejected as a C1 veto) in an `evidence_quality_note` if governance wants a paper trail; do not change status, category, or direction.

- `recommended_evidence_direction`: `non_contributory` (wrong layer for INV-013; diagnostic-purpose excluded from scoring anyway).
- `recommended_epistemic_category`: `standard` at target level (this run told us nothing that should suppress INV-013). Per-claim keep `derivational` -- already stored, and correct for an architectural existence audit. `change: STANDS`.
- `recommended_substrate_queue_entry.action: none`. Rate-gating latent updates by loop identity is a product decision for ARC-023/SD-006, not a fix INV-013 is owed, and the structural gap was already documented before this run.
- No `/queue-experiment` lettered successor on INV-013. A *different* question (ARC-004's own L-space layers; or a build that actually consumes `e2_tick`) is out of this target's claim_ids and is reported as read-across, not queued here.
- `pending_retest_after_substrate`: false for INV-013.

### Read-across, not adjudicated

- **ARC-004** -- this is its measurement, on the wrong layers. Its own caveat (shared EMA, MECH-058 fate) is now joined by an E-loop empirical inversion. Do not treat this run as ARC-004's missing first test.
- **ARC-023** -- functional analog (distinct update rates) is clock-real for e1/e3 discrete paths and not representation-real for continuous state. Category is already `substrate_conditional`.
- **SD-006** -- status implemented, "all five criteria met." This run does not reopen that implementation audit; it says implemented multi-rate does not imply realised persistence separation.

## 9. Learning extracted

1. A readiness gate whose statistic is not the DV's statistic can still void a reachable DV. 939 showed harsher aggregation of the *same* statistic; 942 shows a copied power floor (EXQ-019 C4) used as a degeneracy definition. Both self-route `substrate_not_ready_requeue`. Check the data.
2. "The mechanism could not express itself" is a claim about data. Here two seeds expressed a full-horizon frozen-policy eval and the half-lives are on the page.
3. A designed tick ratio is not a realised persistence ratio -- now measured, not only source-read. e3's extra phase-reset ticks are a separate, smaller correction to the planning doc's "structurally guaranteed 1:3:10."
4. Hardcoding `criteria_non_degenerate.C1_... = False` in the P0NotReady branch names C1 as degenerate when C1 was never scored. The variance floors -- the driver's own degeneracy definition -- all passed.
5. INV-013's registered scope (existence audit; realised-vs-labeled delegated) is what stops this inverted C1 from being a claim-layer weaken.

## 10. Step 7b / 7c

- 7b: `autopsy_pre_routing_checks.py --artifact ... --json` at generated_utc: **fire_count 0**, fires []. C6 and C7 inapplicable (single-arm diagnostic, no `arm_results`) -- expected, not a silence-as-all-clear on those checks. C1-strict does not apply (routing is `governance-note-only`). C2-strict does not apply (`action: none`). C3 does not fire (`lit_status: partial` with present ARC-023/SD-006 reviews; INV-013 has no dedicated entries).
- 7c: CONFIRMED. C1 recomputes false from `per_seed` cells. STANDS vs H-monotonic elimination does not conflict (different objects). Routing unchanged.
- Step 9b: applied at confirmation. New qid `e-ladder-realised-timescale-separation` (claims ARC-023 / SD-006 / ARC-004 -- not INV-013), two legs born resolved same-cycle from this run's C1 recompute.
