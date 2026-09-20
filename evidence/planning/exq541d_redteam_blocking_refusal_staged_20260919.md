**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or whichever registry).**

# V3-EXQ-541d REFUSED at /queue-experiment Step 4.5 -- red-team BLOCKING

- Date: 2026-09-19
- Session: `metaworker-science-20260919-mech204-541d-guard-validation` (headless, ree-cloud-4)
- Campaign: `science-20260919-mech204-541d-guard-validation`
- Chip: `chip-20260918-exq541d-mech204-f1-guard-validation` (handed back, NOT resolved done)
- Decision chip raised: `chip-20260919-exq541d-base-regime-blocking`
- Script authored, smoke-tested, red-teamed, and DELIBERATELY NOT QUEUED:
  `ree-v3/experiments/v3_exq_541d_mech204_f1_coldstart_guard_validation.py`
- EXQ id `V3-EXQ-541d` was reserved and is now RELEASED (never appended to the queue).

## 1. What was asked, and what was approved

The chip pre-specified the design and forbade redesign. The orchestrator's
pre-flight raised it AMBER-DECISION on one axis: the chip's numeric DV anchor
(`~255`) comes from the IGW-20260915-243 **realized-PE** setting, while the base
it names (V3-EXQ-541c) drives E3's running variance from a **synthetic** PE
stream. The user resolved that axis on 2026-09-19T22:12:50Z:

> DISPATCH on 541c's SYNTHETIC-PE base, with the criterion RE-ANCHORED to that
> regime by the rule the design gives (if none, one kind:decision chip). Do NOT
> rebuild on IGW-243's realised-PE base.

That instruction was followed. The design gives a rule -- the anchor is
`1/realized-PE-variance`, a formula, and `~255` is only its value in the other
harness -- so the re-anchoring was mechanical: measured in-run, `~3.24` here.

## 2. Why the run was nevertheless refused

The red-team pass (Step 4.5, run on `fable`, this session is Opus 5) returned
**BLOCKING**. Its findings were verified against source and against measured
data before being accepted -- a red-team finding is a lead, not a verdict.

### F1 -- the headline contrast is an arithmetic identity, CONFIRMED to 8e-5

The guard flag adds only a counter increment inside `REEAgent.sense()`
(`agent.py:4939`), consuming no RNG, so both arms see an identical trajectory.
E3's running variance is an EMA with `alpha = 0.05`, so after 200 waking ticks
the pre-episode value carries weight `0.95**200 = 3.5e-5`: the per-cycle honest
precision `p_j` is the same in both arms. With the F1 EMA
(`serotonin.py:390-397`, `persistent <- 0.9*persistent + 0.1*p`):

```
OFF_k - ON_k  ==  0.9**k * (SENTINEL - p_1)          exactly
```

Verified on a traced 16-cycle probe (seed 42, recal step 0.25):

| k | actual OFF-ON | predicted `0.9^k (2 - p_1)` | abs err |
|---|---|---|---|
| 1 | -1.330500 | -1.330470 | 3.0e-05 |
| 2 | -1.197400 | -1.197423 | 2.3e-05 |
| 3 | -1.077600 | -1.077681 | 8.1e-05 |
| 16 | -0.274000 | -0.273932 | 6.8e-05 |

Max abs error over all 16 cycles: **8.07e-05** (consistent with the probe's own
4-decimal rounding).

Consequence: criterion **D5**, the cross-arm anchor-gap contrast that the design
was relying on to carry the discriminating information, measures
`(SENTINEL - p_1)/anchor` times a fixed decay. It is **D1 restated with extra
steps**, not a measurement of the guard's benefit. Its value is a property of
the harness: re-parameterise `pe_scale` so `E[pe^2] = 0.5` and D5 FAILS with a
perfectly working guard; use IGW-243's `0.0039` and it reads ~100x.

### F2 -- the pre-registered FALSIFIER cannot fire on this base

The chip's falsifier is load-bearing and explicit: if with the guard ON the
target *still climbs monotonically away* from `1/realized-PE-variance` over the
first ~10 cycles, MECH-204 Option A must be **DEMOTED, not retuned**.

On 541c's harness that quantity is `1/rv` of a **stationary** synthetic stream
(`pe_scale = 0.4 + 0.3*rng.random()`, a function of `rng` alone -- independent
of agent, episode, and prior WRITEBACK). There is no realized precision that
*can* drift. The IGW-243 climb the falsifier was written from
(`2 -> 27 -> 49 -> 69 -> 88`) was the agent's realized precision pulling the
sentinel EMA. Measured here: the guard-ON gap to the anchor is non-monotone
(`0.2395, 0.1966, 0.1769, 0.1006, 0.128, 0.1634, 0.078, 0.0671, ...`).

**So the single most scientifically load-bearing clause in the chip is
untestable on the base the chip names.**

### F3 -- D1 is a contract test, not a measurement

At the cold-start cycle C0, `_waking_ticks_since_capture == 0` by driver
construction, so `d1_cell_ok == (guard XOR captured)` is identically True
(`serotonin.py:385-392`). It duplicates contracts C1-C8 in
`tests/contracts/test_mech204_f1_coldstart_guard.py`. Confirmed by smoke:
10/10 cells PASS. Its "OFF captures *at the sentinel*" clause was additionally
never asserted -- `E3_SENTINEL_PRECISION` was recorded but never compared.

### F4/F5 -- the verdict grid collapses; one readiness gate certifies a constant

With D1 an identity, D2 pre-registered degenerate, D4 unable to fire and D5
pinned, every readiness-met path reaches `f1_coldstart_guard_validated`.
Readiness P2 bands `realized_pe_variance`, which is the driver's own
`E[pe^2] = 0.31` by construction and cannot fail.

## 3. What WAS established (positive results, worth keeping)

The work was not wasted -- the mechanism is now proven rather than inferred:

1. **The defect is real and precisely localised.** 541c's driver calls
   `agent.reset()` once *before* its episode loop; with `sleep_loop_episodes_K=1`
   that fires a full sleep cycle with ZERO waking ticks (C0). At C0's REM entry
   E3 has never seen a prediction error, so `current_precision` is the
   `precision_init` sentinel: `precision_init = 0.5` is a **variance**
   (`config.py:1126`), giving `1/(0.5+1e-6) = 1.999996`.
2. **The guard works, measured across the full arm structure.** Smoke, all five
   recal-step arms: guard OFF anchors `_persistent_zero_point` at `1.999996`;
   guard ON declines to capture (`None`). Cycle-1 target OFF `2.1478` reproduces
   541c's documented `2.148` and equals `0.9*2.0 + 0.1*(1/0.287498)` exactly;
   guard ON gives the honest `3.4783 = 1/0.287498`.
3. **The waking-tick producer is `REEAgent.sense()`**, verified on `origin/main`
   (`agent.py:4858` / call at `:4939`), and that comment block explicitly names
   `v3_exq_541c` as a driver it covers. **A STALE COMMENT should be corrected:**
   `serotonin.py:144` and `note_waking_tick()`'s own docstring both still say the
   producer is `REEAgent.update_residue()`. That is wrong on `origin/main`, and
   if it were right this guard would be a permanent kill switch on this base.
4. **The second defect instance is NOT present on this base.** The chip asks
   541d to be able to see a cycle issuing more than one `enter_rem()` call.
   Measured: exactly ONE `enter_rem` per sleep cycle (17 calls for 16 episodes =
   16 cycles + C0); `ree_core` has a single internal caller
   (`agent.py:12701`, reached once per `run_sleep_cycle`). That instance should
   be tested on a driver that multi-fires REM -- the `v3_exq_sd068_*` family
   calls `enter_rem_mode` directly.
5. **The reset ordering is safe** (`agent.py:3597` sleep before `:3626`
   serotonin reset), as the pre-flight said.

## 4. The decision now owed to the user

The AMBER the pre-flight raised was narrower than the real problem. It said D2
("within ~2x of the anchor") would read PASS in both arms. Correct -- but D4 and
D5 are *also* pinned, and that was not known at decision time. The honest
statement is:

> On 541c's synthetic-PE base the cold-start guard's effect is a first-cycle
> transient with a **closed-form decay**. There is no criterion on this base
> that distinguishes "the guard removed a cold-start artefact" from
> "the guard did not capture at C0" -- because on this base those are the
> same proposition.

Options (the user's call; this session deliberately did not choose):

- **(A) Run it anyway as a pure CONTRACT/instrument confirmation.** Cheap and
  honest if re-scoped: drop D4 and D5, keep D1 + the C0 sentinel assertion,
  and tag it explicitly as a substrate contract check rather than a validation
  of the fix. Buys little beyond what C1-C8 already assert in the test suite.
- **(B) Rebuild on the IGW-20260915-243 realized-PE base.** The chip's numbers
  (`anchor ~255`, `rv -> 0.0039`) transfer, the falsifier becomes testable, and
  D5 stops being an identity because `p_j` is then agent-dependent and can
  drift. Cost: 541c's validated 16-cycle dose-response structure must be
  rebuilt. **This is the option the red-team's findings point at**, and it is
  exactly the option the 2026-09-19 approval ruled out -- on information that
  has now changed.
- **(C) Keep 541c's structure but replace its synthetic PE stream with a
  realized world-model PE**, giving a drifting `p_j` on the validated arm
  structure. Middle path; needs a check that the 541c dose-response survives
  the substitution.

**Recommendation: (B) or (C).** (A) does not validate the fix; it re-asserts a
contract that already has eight passing tests.

## 5. Provenance

- Red-team model: `fable` (session model is Opus 5). One pass, not iterated.
- `validate_experiments.py --strict --paths <script>` exits 0. One advisory
  `precondition-recomputability` warning remains: an AST heuristic firing on the
  two-sided-band shape itself. `met` was made worst-cell recomputable (value
  furthest from the band's geometric centre) and the prescribed per-arm
  non-gating diagnostic is emitted.
- Smoke: `--dry-run`, rc=0, 126.2s, 10/10 per-cell verdicts PASS, all three
  readiness preconditions met.
- Gates cleared before authoring: GOV-REUSE-1 (the lever landed 2026-09-18 and
  is default-off bit-identical, so no manifest can carry the readout -- not
  recoverable); re-derive brake on MECH-204 = 0; substrate-path overlap = no
  open `corrupting` entry (degrading overlaps noted: `SD-ZWORLD-SENSE-PATH-PARITY`
  on `REEAgent.sense`, `e2-world-forward-sleep-trainer` on `phase_manager`,
  `SD-018`, `SD-091`, `SD-106`, `sd061-resume-progress-ecology`,
  `SD-MECH303-THRESHOLD-SOURCING`); ethics preflight all-`false` / `allow`.
- The substrate record `ree-v3/docs/substrate/MECH-204-f1-coldstart-guard.md`
  states "V3-EXQ-541d (queued 2026-09-18)". **That sentence is still FALSE** and
  should be corrected -- it was written in anticipation. The STOP-CHECK was run
  against the live tree, not the doc.

---

# 6. SECOND REFUSAL (2026-09-20): the realised-PE rebuild is ALSO blocked, and the falsifier itself is the reason

- Session: `metaworker-science-20260919-mech204-541d-guard-validation` (resumed)
- User decision acted on: 2026-09-19T23:52:40Z -- "CHANGE THE BASE TO A DRIVER
  WITH REALISED PE", choosing between the IGW-20260915-243 base and the
  `v3_exq_sd068` multi-REM driver "by which one lets the pre-registered
  falsifier actually FIRE".
- Outcome: base selected, anchor re-measured, driver rebuilt, smoke green --
  then **red-team BLOCKING again**. Nothing queued. `V3-EXQ-541d` still free.

## 6a. The base choice was made, and sd068 was correctly rejected

`v3_exq_sd068_*` was rejected on the user's own criterion. It never touches the
F1 / `_persistent_zero_point` / `mech204` path (grep: zero hits across all eight
drivers), bypasses `SleepLoopManager` so no `mech204_*` WRITEBACK metrics exist,
reaches REM only via an unscored `drive_liveness_pass` wrapped in a bare
`except Exception`, and its precision target is **clamp-pinned** --
V3-EXQ-778c recorded `target_clamped` 1.0 with `calibration_error` fixed at the
constant 998.5009992509989, "degenerate at both rails". A clamp-pinned
precision is precisely not "realised and able to drift".

The IGW-243 base is the canonical **StepHarness** loop (K=1 sleep, F1 recal
step 0.25), matching V3-EXQ-794's substrate operating point.

## 6b. The anchor re-measurement the user required -- DONE, and it transfers

| quantity | measured on the realised base |
|---|---|
| realized PE variance | 0.003848 (probe) / 0.00380 (smoke) |
| **anchor = 1/realized-PE-variance** | **259.9 / 263.1 / 264.3** |
| C0 target, guard OFF | 1.999996000008 -- the `precision_init` sentinel, exactly |
| C0 capture, guard ON | none (`_persistent_zero_point` stays `None`) |

The chip's "~255 in the IGW-20260915-243 setting" **transfers**. 541c's 2.148
does not, and is used nowhere in the rebuilt driver. The design's own text
fixes the re-derivation rule (`1/realized-PE-variance`), so no decision chip was
owed on that axis.

## 6c. G1 -- the pre-registered FALSIFIER cannot fire on ANY base

The falsifier asks whether `|target - anchor|` **grows** monotonically over the
first ~10 cycles with the guard ON. Measured, every arm:

```
OFF targets: 2.12 2.31 2.56 2.83 3.17 3.91 4.47 4.98 5.58   (monotone INCREASING)
ON  targets: 3.16 3.29 3.55 3.88 4.30 5.26 6.00 6.66 7.45   (monotone INCREASING)
anchor = 259.9 -- every target is two orders of magnitude BELOW it
```

The target is an EMA of `p_k = 1/rv_k`; rv falls as the world model learns, so
the target RISES toward the anchor and `gap = anchor - target` **shrinks by
construction**. For the gap to grow, rv would have to RISE across cycles, which
requires realized PE > rv (~0.15, about 40x the measured 0.0038) for nine
consecutive cycles.

**This is a defect in the chip's falsifier TEXT, not in the base.** The chip
says the TARGET climbs away from `1/realized-PE-variance`, but the IGW-243
measurement it was written from says the target climbs `2.0 -> 27 -> 49 -> 69
-> 88`, which is climbing **toward** 255. What IGW-243 recorded as moving AWAY
is **rv**: *"recalibration pushes rv AWAY from calibration (0.0039 -> 0.0121)"*.
Target and rv were conflated when the falsifier was written.

Consequence: **the user's base-selection criterion cannot be satisfied by any
base**, because the quantity it names cannot move in the direction it names.

## 6d. G2 -- and the rebuilt driver's own rationale for E2 was WRONG

The rebuilt driver argued that a realised base breaks 541c's closed form
because "precision feeds selection feeds prediction error feeds precision".
**Measured: false.** Per-episode realized PE is **bit-identical** between the
two guard arms at every episode:

```
guard_off ep_mean_pe: [0.003832, 0.003786, 0.003852, 0.003862, 0.00386, 0.003958, ...]
guard_on  ep_mean_pe: [0.003832, 0.003786, 0.003852, 0.003862, 0.00386, 0.003958, ...]
anchor: 259.904 in BOTH arms
```

The guard changes rv; rv never reaches an action; the trajectories never
diverge. What actually makes `p_j` arm-dependent is the WRITEBACK's rv change
surviving into the next REM entry, decaying as `0.95^n` in ticks-per-episode.
At n~10 the carry-over is ~0.60 and the departure reads 4-10x; at n~200 it is
3.5e-5 and reads 1.00. **E2's verdict is a function of episode length.**

## 6e. G3 -- the run is not in the regime it declares

The driver specifies 30 episodes x 200 steps = 6000 waking ticks per cell.
Measured at grid 12: episodes end **by death in 6-15 ticks**
(`agent_health <= 0`), so the true figure is ~300. The readiness precondition
`min_waking_ticks_at_post_c0_rem_entry` read 7 and was interpreted as
"producer live -- MET"; it was in fact reporting the episode length. A red flag
was read as a green one. V3-EXQ-794 at this same nominal operating point
recorded `rv_final ~0.0054` (rv tracking PE), which needs ~60-100 ticks per
episode -- so either 794's agents survived and these do not, or the operating
points differ on an axis neither script records. Neither script records
episode length.

## 6f. THE UNSCORED RESULT THAT MATTERS

On essentially every cycle of BOTH arms the WRITEBACK moves rv **away** from
the realized PE variance:

| arm | cycles with `rv_after > rv_before` | rv range | realized PE | ratio |
|---|---|---|---|---|
| guard OFF | 9/9 | 0.0913 - 0.3165 | 0.003848 | 24-82x above |
| guard ON | 8/9 | 0.0688 - 0.3165 | 0.003848 | 18-82x above |

This is IGW-243's finding reproduced and generalised. It is the **substance**
of the falsifier, expressed on rv -- the quantity IGW-243 actually measured --
rather than on the target. Re-expressed that way the falsifier is both firable
**and appears already SATISFIED**, which per the chip's own pre-registration
would route MECH-204 Option A to **DEMOTE, not retune**.

Changing the falsifier is a user decision. This session did not make it.

## 6g. Options (the user's call)

- **(A) Re-express the falsifier on rv** -- "does the WRITEBACK move rv away
  from the realized PE variance?" -- and re-run. Firable, matches what IGW-243
  measured, and the probe suggests it fires immediately. This is the smallest
  change that makes the chip's own scientific question answerable.
- **(B) Fix the survival regime first** (P0 warmup / easier env / lower
  `hazard_harm`) so episodes last ~100+ ticks, then re-run. Needed regardless
  if any criterion is to be independent of episode length, and needed before
  this driver can honestly claim V3-EXQ-794's operating point.
- **(C) Both** -- (B) then (A). Recommended: (B) is a precondition for any
  clean reading of (A), and neither is meaningful alone.
- **(D) Stop and route MECH-204 Option A to governance on the rv evidence
  already in hand**, without a further run.

**Recommendation: (C), with (D) raised in parallel** -- the rv result is
already strong enough that governance should see it whether or not a further
experiment is queued.

## 6h. Two stops on one item -- the premise, not the design, is what failed

Per the dispatch brief's "two stops means stop": this is the second BLOCKING
refusal on `chip-20260918-exq541d-mech204-f1-guard-validation`. The first was
about the BASE; this one is about the FALSIFIER, which no base can satisfy.
That pattern says the item's premises are stale rather than its design being
unlucky: the chip pre-registered a falsifier on the wrong variable, and both
the orchestrator pre-flight and the first rebuild inherited that error without
checking it against the IGW-243 numbers the chip itself cites. The chip should
be re-specified before any third attempt.

---

# 7. THIRD/FOURTH REFUSAL (2026-09-20): the falsifier cannot fire without a drift source -- and that yields the actual answer

Session `metaworker-science-20260920-mech204-541d-cd`, executing the user's
2026-09-20T09:29:55Z decision (option C with D in parallel).

## 7a. What was delivered

- **D (done).** `GFLAG-0379` (contested_disposition, MECH-204) carrying the rv
  evidence, the proven cold-start mechanism (`precision_init` is a VARIANCE 0.5
  -> sentinel precision 1.999996; the pre-loop `agent.reset()` fires a
  zero-waking-tick cycle that anchors on it), and the wrong-variable finding.
  `claims.yaml` untouched.
- **B (done, by measurement).** Survivable regime selected. See 7b.
- **A (built, refused).** Falsifier re-expressed on rv; four red-team passes.

## 7b. Option B: the regime, chosen by measurement

Env-only survivability screen, 12 episodes x 12 seeds, 200-step cap:

| candidate | params changed | mean | median | frac >= 100 | terminal cause |
|---|---|---|---|---|---|
| BASE (794 point) | 0 | 11.9 | 12.5 | 0.000 | health_depleted |
| lower `hazard_harm` 0.01 | 1 | 11.9 | 12.5 | 0.000 | health_depleted |
| P0 warmup, 10 episodes | 0 | 12.5 | 9.5 | 0.000 | health_depleted |
| fewer hazards (1) | 1 | 17.5 | 12.0 | 0.000 | health_depleted |
| `proximity_harm_scale` 0.03 | 1 | 29.8 | 32.5 | 0.000 | health_depleted |
| prox 0.02 + contam 0.02 | 2 | 74.1 | 76.5 | 0.000 | health_depleted |
| prox 0.015 + contam 0.015 | 2 | 98.8 | 98.0 | 0.417 | health_depleted |
| **prox 0.01 + contam 0.01** | **2** | **149.2** | **148.5** | **1.000** | **health_depleted** |
| prox 0.005 + contam 0.005 | 2 | 200.0 | 200.0 | 1.000 | STEP CAP (immortal) |

**Selection rule, stated before the choice:** among candidates clearing the bar
(>= 100 ticks in >= 2/3 of episodes), take the one that (1) changes the fewest
env parameters from the IGW-243/794 operating point; (2) on a tie, perturbs the
measured realised-PE variance least; (3) on a further tie, preserves the
qualitative regime -- episodes must still end by `health_depleted`, so harm
remains a live constraint rather than being removed. Tie-break: prefer an env
parameter over a training-schedule change, since a schedule change alters the
agent's competence and therefore what regime is being measured.

**All three candidates the decision named were eliminated by measurement**, and
one instructively: lowering `hazard_harm` gives BYTE-IDENTICAL episode lengths,
because contact harm is not the binding constraint. The two real killers are the
continuous `hazard_approach` proximity drain (~0.10 health/tick at the 794
setting) and **`contaminated_harm`, which defaults to 0.4 PER CONTACT** and is
overridden by neither 794 nor any 541d build. That second killer was invisible
until measured, which is why it was not among the named candidates.

Only one candidate clears while still terminating by health depletion, so the
choice was forced and no decision chip was owed. Qualification: the table is a
RANDOM-POLICY screen; under the real driver the agent at prox 0.01 survives to
the 200-step cap. Rule (3) still discriminates correctly -- at 0.01 a random
policy still dies, so survival is EARNED; at 0.005 it is free.

**The regime achieved its purpose**, which was the point of B: rv now CONVERGES.
Measured `rv / realised-PE-variance = 1.0` in both arms (final rv 0.003807,
realised PE 0.003864, anchor 258.78 -- the chip's "~255" reproduced a third
time), against **18-82x** in the pre-survivable regime.

## 7c. Option A, and why it was refused twice more

Third pass (BLOCKING), both findings verified arithmetically:

- The falsifier scored as a COUNT of cycles moving rv away was NOISE. In a
  converged regime rv ~= R and the guard-ON target ~= 1/R, so the sign compares
  two ~1e-5 quantities; the smoke measured an ON away-fraction of exactly 0.5.
  **Fixed:** scored on MAGNITUDE instead -- OFF +1.547 vs ON -0.00104 in the
  smoke, a ~1500x separation.
- The old F2 ("is ON less de-calibrating than OFF?") COULD NOT FAIL: `rv_before`
  is identical in both arms, the sentinel in OFF's target is the only
  difference, and it is strictly de-calibrating. Verified: OFF relative
  displacement +2.029 / +0.980 / +0.319 / +0.101 / +0.009 at cycles
  1/2/5/10/19, against ON +0.0000 throughout. It restated the cold-start
  contract. **Fixed:** inverted into a POSITIVE CONTROL on the OFF arm.

Fourth pass (BLOCKING), on the revised criteria -- and this one is structural:

> **With the guard ON the recalibration target is an EMA of
> `current_precision = 1/rv` -- a LAGGED FUNCTION OF rv ITSELF. Recalibrating rv
> toward a lagged function of rv is near-idempotent, so it cannot de-calibrate a
> converged rv.**

Adversarial sweep over eight rv trajectories (stationary; 10x and 100x monotonic
decay; 5x step collapse; 5x step rise; alternating x3; 20x single spike;
sawtooth) gives guard-ON mean relative displacement in **[-0.15, +0.062]** --
never approaching the 0.25 firing bar. The `..._demote` branch is UNREACHABLE;
the run could only ever confirm.

(The same pass also flagged the OFF positive control as marginal at 19 cycles.
Re-derived independently: 19-cycle mean **2.013**, against a 0.25 bar -- ample
margin. That finding does not reproduce and is recorded as not-confirmed.)

**Root cause of this build's defect, owned plainly:** this driver dropped SD-076
(`use_waking_confidence_inflation`) to avoid depending on the unvalidated
`sd_waking_confidence_inflation_headroom` repair. That was a mistake. SD-076 is
the only substrate mechanism that makes rv diverge from realised PE while the
guard is on, and the user's own base-selection criterion had required the
precision be "realised AND ABLE TO DRIFT". Removing the drift source removed
exactly the property that criterion protected.

## 7d. THE RESULT -- what the four passes together establish

This is worth more than the queued run would have been:

> **MECH-204 Option A's recalibration can only de-calibrate rv when its target
> is CONTAMINATED or STALE** -- i.e. (a) the `precision_init` cold-start
> sentinel, which the landed F1 guard removes, or (b) rv far from its own lagged
> mean, i.e. a non-converged rv (short episodes) or an active drift source.
> **It is not de-calibrating in principle.**

Consequence for the disposition, and a correction I owe:

- The 9/9 and 18-82x figures in **GFLAG-0379** were measured in regime (b) --
  6-15-tick episodes where rv never converged. That flag's DEMOTE
  recommendation is **overstated**, and is corrected by **GFLAG-0384**.
- The evidence supports the guard FIXING the identified defect. It does not
  support demoting Option A.
- What remains genuinely untested is Option A against a real waking drift
  source. That is the owed experiment.

## 7e. The decision now owed

- **(A) Re-arm SD-076** at the repaired floor (`relative_frac` 0.2, `soft` mode)
  and re-run. This RESTORES compliance with the user's own "able to drift"
  criterion and makes the falsifier firable. Cost: reintroduces the dependency
  on `sd_waking_confidence_inflation_headroom`, which is `implemented` with
  ready FALSE and its own validation (V3-EXQ-794a) not yet queued -- a
  dependency the user has not yet been asked to accept.
- **(B) Queue V3-EXQ-794a first** (the headroom repair's own validation), then
  541d on top of a validated drift source. Slower, no borrowed risk.
- **(C) Accept a confirm-only instrument validation.** Honest if labelled as
  such, but it cannot falsify and duplicates contracts C1-C8.
- **(D) Treat 7d as the answer** and route MECH-204 Option A to governance on
  GFLAG-0379 + GFLAG-0384 without a further run.

**Recommendation: (B) then (A)**, with (D) proceeding in parallel since the
corrected disposition should reach governance either way. (A) alone is
defensible if the dependency is acceptable to the user.

## 7f. Red-team budget

Four passes on this item; the skill permits one pass plus one re-spawn when a
BLOCKING finding changes the causal chain. That budget is now spent, so this
session stopped rather than iterating to a clean verdict -- which is the
condition the "do not iterate to CLEAR" rule exists to prevent.

---

# 8. (2026-09-20) The B-then-A decision is not executable: V3-EXQ-794a already ran, and FAILED

User decision (orchestrate-20260920-1121): **(B)** queue V3-EXQ-794a to validate
the SD-076 headroom repair, **then (A)** 541d with SD-076 re-armed on the
validated drift source, **(D)** in parallel. The decision explicitly required a
STOP-CHECK of the existing `v3_exq_794a_*.py` before writing anything. That
STOP-CHECK is what found the premise false.

## 8a. V3-EXQ-794a is not unqueued -- it ran 2026-07-24 and FAILED

`REE_assembly/evidence/experiments/v3_exq_794a_mech204_phase7_sd076_calibration_loop_2x2_20260724T063301Z_v3.json`

| field | value |
|---|---|
| `outcome` / `result` | **FAIL** |
| `evidence_direction` | `inconclusive` |
| `interpretation.label` | **`drift_source_insufficient_dv_still_tautological`** |
| `supersedes` | `v3_exq_794_mech204_phase7_sd076_calibration_loop_2x2` |
| `claim_ids` | `MECH-204`, `SD-076` |

So **(B) cannot be performed**: the id is burned (a terminal row exists, so a
re-queue would be refused), and the question it was to answer is already
answered. And **(A)'s stated precondition -- "after 794a validates it" -- can
never be met by 794a**, which has already returned the opposite.

## 8b. What 794a actually established -- the repair works, the DRIFT SOURCE does not

Every precondition passed, in all six arms. The repaired scale-relative /
softplus rv floor is NOT the problem:

- `rv_live` 0.4815-0.4956 across arms
- `f1_recalib_engaged` 0.0059-0.0137
- `inflation_lowers_rv` 0.0014-0.0057 (SD-076 genuinely moves rv, and downward)
- `dose_levels_separated` 1.27e-4 / 2.86e-4 (no 794-style clamping)
- `broadcast_moves_rv`, `zero_point_populated` all met

What failed is the science:

| criterion | load-bearing | passed |
|---|---|---|
| `C1_inflation_creates_absolute_overconfidence` | **yes** | **False** |
| `C2_broadcast_corrects_under_drift` | **yes** | **False** |
| `C3_interaction_correction_larger_under_drift` | no | False |
| `C4_off_off_reproduces_774_ceiling` | no | True |
| `C5_asymmetry_dose_response_monotone` | no | True |

C1 failed at **both** the LO (0.6) and HI (0.8) asymmetry levels. V3-EXQ-794's
docstring pre-registered the route for exactly that outcome:

> "if C1 fails at BOTH levels the route is NOT 'sweep higher': it is that the
> **asymmetric-EMA form is the wrong drift source and a different SD-076
> mechanism is owed**."

## 8c. Consequence for MECH-204 Option A

Chaining this with section 7d gives a complete and, I think, final picture of
why this item has resisted four red-team passes:

1. Option A's recalibration target is an EMA of `1/rv` -- a lagged function of
   rv itself -- so it **cannot de-calibrate a converged rv** (7d).
2. The only thing that can make rv diverge from realised PE while the guard is
   on is a waking drift source.
3. The substrate's only drift source, SD-076, is **measured insufficient at
   both dose levels** (8b), and its own pre-registered route says the
   asymmetric-EMA *form* is wrong.

Therefore **MECH-204 Option A is not falsifiable on the current substrate at
all**, and the owed work is an `/implement-substrate` BUILD of a different
drift-source mechanism -- not another experiment. Queueing any 541d variant
before that build would reproduce the same unfirable falsifier.

## 8d. Root cause of the stale premise

`substrate_queue.json` entry `sd_waking_confidence_inflation_headroom` still
reads `validation_experiment: "V3-EXQ-794a (not yet queued)"` (with
`ready: False`). The `ready: False` is right; the stated reason is not -- the
validation is not pending, it is **done and negative**. That note is what
produced a user decision to sequence work that cannot be executed. Raised as
**GFLAG-0385** (`stale_note`); the registry was not hand-edited.

## 8e. What is owed now (the user's call)

- **(A) `/implement-substrate` a different waking drift-source mechanism**, per
  794's pre-registered route, then re-test Option A against it. The
  substantive path, and the only one that makes the falsifier firable.
- **(B) Re-scope 541d as an explicit instrument-confirmation** of the
  cold-start guard, labelled as unable to falsify. Cheap, honest, low value --
  contracts C1-C8 already cover it.
- **(C) Close MECH-204 Option A on the evidence in hand**: the cold-start
  defect is proven and fixed by the landed guard (GFLAG-0379 + GFLAG-0384),
  and the residual question is un-askable until a drift source exists. Route to
  `/governance` and stop spending experiment budget.

**Recommendation: (C) now, (A) when substrate budget allows.** (B) buys nothing
the contract suite does not already assert.
