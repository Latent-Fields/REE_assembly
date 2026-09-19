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
