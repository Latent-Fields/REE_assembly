# INV-063 leg B: the across-sleep frozen-battery DV is not readable as an IMPROVEMENT

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or any other registry).**

- Raised by: headless science chip `chip-proposal-exp-0736-paced`, campaign
  `science-20260919-inv063-four-arm-intake-ladder`, session
  `metaworker-science-20260919-inv063-four-arm-intake-ladder` (ree-cloud-4)
- Date: 2026-09-19
- Reserved but NOT used: `V3-EXQ-1063` (`ree-v3/experiments/v3_exq_1063_inv063_four_arm_intake_ladder.py`).
  No script was written and no queue entry was appended -- this refusal fired at
  `/queue-experiment` Step 2.5a (empirical confirmation), before authoring.
- Decision chip: `chip-20260919-inv063-legb-dv-direction`

---

## 1. What was asked, and how far it got

Design and queue INV-063's four-arm intake-ladder falsifier (`/queue-experiment`).
The pre-flight was GREEN: the orchestrator had upgraded scout2's AMBER on the ground
that V3-EXQ-1060 (PASS, 2026-09-19) discharged the one named blocker -- "leg B DV
structurally 0.0".

Every gate before Step 2.5a passed:

| gate | outcome |
|---|---|
| chip freshness / claim | open, unclaimed, claimed by this session |
| 2.4 GOV-REUSE-1 | decisive readouts absent from every compatible manifest -> run (see sec 6) |
| 2.5 substrate readiness | SD-MEL-PRODUCER `implemented`/ready; the 2026-09-17 world-forward trainer landed |
| 2.5b re-derive brake | count 0 for INV-063 (no autopsy target tags it at all) |
| 2.5c substrate-path overlap | handled as V3-EXQ-1060 handled it; P5 already excludes the Type-3 leg |
| claim_evidence | INV-063 has 5 literature entries and ZERO simulation runs; `implementation_phase` absent |

Step 2.5a -- "run a minimal throwaway probe to empirically confirm the experiment's
premise" -- is where it stopped.

## 2. The finding, in one line

**On the base regime INV-063's own P1 requires, a sleep cycle makes the frozen
held-out world-forward MSE WORSE, not better, in 9 of 9 cells -- so leg B's
"across-sleep IMPROVEMENT" DV is negative before any intake manipulation is
applied.**

## 3. The measurements

Three throwaway probes, on `ree-cloud-4`, torch 2.12.0+cpu, `ree-v3` at `origin/main`
(`e1ddd98c`). Sources and raw output are committed on the umbrella branch
`claude/metaworker-science-20260919-inv063-four-arm-intake-ladder` under
`scratch/probe_inv063_*.py` / `scratch/probe_v*.out`, and are reproduced in sec 8.

### 3a. Unconverged base -- V3-EXQ-1060's regime, the one that discharged the blocker

3 wake-sleep cycles x 2 episodes x 90 steps, real E3 selection path, sleep via
`SleepLoopManager`, frozen battery captured once pre-first-cycle (V3-EXQ-1060's
`_sample_probe_battery` form, held-out env seed+9973). Arms
`world_rule_shift_interval` {0, 60, 25, 10} at depth 2, plus a sigma=0.12
observation-noise arm. Seeds 42 / 123 / 456.

P4 liveness is fine: 211-341 MECH-205 surprise writes per cell, `_pe_ema`
0.0017-0.0065 so the realised `surprise_weight` is 0.008-0.033 and NOT pinned at
its 0.3 fallback, PE variance 1.3e-7..3.5e-6.
P2 is fine: realised (SWS, REM) budget is (5.0, 10.0) in EVERY arm -- zero
cross-arm variance, with the consumer off.
P3 is fine: 3/3 cycles fired in every cell.

**P1's manipulation check FAILS here.** Mean waking MEL (`e3_prediction_error`),
arms NONE / LOW / MED / HIGH:

| seed | NONE | LOW | MED | HIGH | monotone | rel. spread |
|---|---|---|---|---|---|---|
| 42  | 0.0046429 | 0.0048642 | 0.0049252 | 0.0051436 | yes | 0.097 |
| 123 | 0.0024251 | 0.0024487 | 0.0021907 | 0.0022722 | no  | 0.105 |
| 456 | 0.0075160 | 0.0081299 | 0.0083858 | 0.0078498 | no  | 0.104 |

Relative spread ~0.10 against P1's 0.25 floor on every seed; monotone on 1/3.
(V3-EXQ-798a, at the IDENTICAL arm settings but on a CONVERGED base, measured
0.483 / 0.659 / 0.685 and monotone 3/3 -- so the ladder is fine and the BASE is
wrong. The sigma=0.12 noise arm is also mis-calibrated here: MEL 0.004714 vs
HIGH's 0.005144 and NONE's 0.004643, i.e. it matches the FLOOR arm. 798a's 0.12
calibration was made against a converged base whose baseline MEL was ~1e-5.)

**Neither leg orders with intake here.** Summed across-sleep frozen-battery MSE
delta (leg B) and MECH-205 surprise-write count (leg A):

| seed | leg B NONE/LOW/MED/HIGH | mono | leg A NONE/LOW/MED/HIGH | mono |
|---|---|---|---|---|
| 42  | 0.004366 / 0.002498 / 0.002947 / 0.003879 | no | 211 / 272 / 211 / 235 | no |
| 123 | 0.000344 / -0.000825 / 0.000864 / 0.000327 | no | 314 / 301 / 250 / 269 | no |
| 456 | 0.006241 / 0.005927 / 0.005109 / 0.006281 | no | 222 / 263 / 232 / 211 | no |

0/3 seeds monotone on either leg. Leg B's within-seed cross-arm range is ~0.002
while its cross-seed range is 0.0003..0.0063 -- the DV is dominated by seed, not
by intake. C2's own margin (`max(2 x pooled cross-seed SD of the arm-to-arm delta,
20% of the highest arm's DV)`) is at least 0.2 x 0.0063 = 0.0013 on seed 456,
against realised arm-to-arm deltas of 0.0001-0.0009. Unreachable.

A first probe in V3-EXQ-1060's exact 3-episode single-cycle form (no E3 path)
agreed: per-seed leg B 0.00327 / 0.00347 / 0.00336 / 0.00336 across the four arms
-- a 6% cross-arm range on a DV whose cross-seed range is 30x larger.

### 3b. Converged base -- the regime INV-063's P1 presupposes. THIS IS THE FINDING.

P1's own text says the 701c absolute floor "is structurally unreachable **on a
converged base**", and V3-EXQ-798a validated the MEL ladder only in that regime.
So the probe was repeated with a recon-only P0 first (3600 steps of Adam on
`agent.e2.world_forward` over buffered one-step `(z0, a, z1)` transitions from the
STABLE no-shift env -- 798a's `_e2_train_step` form). Convergence reached:
`conv_rel_drop` 0.9980 / 0.9967 / 0.9992, post-P0 frozen-battery MSE 5.0e-6..6.7e-6.

Summed across-sleep frozen-battery MSE delta (positive = sleep IMPROVED the head):

| seed | NONE | MED | HIGH |
|---|---|---|---|
| 42  | **-0.000336** | **-0.000410** | **-0.000667** |
| 123 | **-0.000679** | **-0.000276** | **-0.000293** |
| 456 | **-0.002006** | **-0.001369** | **-0.000621** |

**Negative in 9 of 9 cells; 25 of the 27 individual cycles are negative.** The
degradation is 3e-4 to 2e-3 against a converged battery error of ~5e-6 -- sleep
moves the head 60x to 400x its own converged error level, in the wrong direction.

### 3c. Why -- and it is already written down

V3-EXQ-1060's module docstring states the mechanism verbatim:

> "compute_e2_world_loss minimises the SD-056 InfoNCE CONTRASTIVE loss, while the
> 701b frozen-probe DV is per-element MSE RECONSTRUCTION error. InfoNCE is
> insensitive to a global scale/shift of the prediction, so it can improve while
> frozen-battery MSE does not move."

1060 measured that gap on an UNCONVERGED head, where both fall together
(MSE rel improvement 0.2504, InfoNCE rel improvement 0.0023 -- already a 100x
divergence in favour of MSE, which is what an untrained head gives you for free).
Once the head is MSE-converged there is no shared descent direction left: optimising
InfoNCE necessarily moves an MSE-optimal head OFF the MSE optimum. The sign flip is
the predicted consequence of a mismatch the corpus had already named but never
measured past convergence.

## 4. Why this is a STOP and not a judgement call

INV-063's C1 leg B is "the ACROSS-SLEEP **improvement** in world-forward prediction
error ... falls monotonically with intake", and C2 requires the knee "in the SAME
direction on BOTH legs". A DV that is negative in every arm and seed before the
manipulation is applied cannot be read as an improvement that falls with intake --
so:

- a FLAT or non-monotone leg B would route to **F1**, which INV-063 pre-registers as
  "the invariant is genuinely falsified rather than substrate-confounded". That
  reading would be wrong: it would be substrate-confounded, by an objective mismatch
  in the sleep trainer.
- a false F1 against a claim with zero prior simulation evidence is the expensive
  failure here, not the wasted compute.

Every available repair changes WHAT GETS MEASURED -- the DV, the falsifier, or
whether to run at all -- so under the campaign's consent rule it is the user's call.

## 5. Options (recommendation first)

**(B) RECOMMENDED -- queue a cheap leg-B DV-DIRECTION diagnostic before the
falsifier.** Two arms (sleep-world-forward lever ON/OFF) x a converged/unconverged
base contrast x >= 3 seeds, recording BOTH frozen-battery readouts (MSE and InfoNCE)
across sleep, purpose `diagnostic`, no claim verdict. Its whole job is to establish
which readout, if either, moves in the direction INV-063 asserts, and at which base
convergence -- i.e. to produce the threshold 1060 deliberately declined to invent.
This is the same sequencing the orchestrator already applied once on this chip
(1060 before the falsifier), and it is cheap: the probes above ran 9-15 cells in
well under an hour on a 2-core box.

**(A) Run the four-arm falsifier as pre-registered anyway.** Defensible -- the design
IS ratified and F2 is pre-registered as the likeliest outcome -- but on the evidence
above it will return a leg B that cannot support C1 or C2, and the run would have to
be adjudicated as substrate-confounded rather than read as F1.

**(C) Re-point leg B's DV from 701b's MSE to the SD-056 InfoNCE the trainer actually
minimises.** Makes the DV commensurate with the optimiser, but it is NOT the
instrument INV-063 names by name, and 1060 measured InfoNCE moving only 0.23% in the
regime where MSE moved 25% -- so its dynamic range against C2's 20%-of-highest-arm
floor is unestablished. A claims.yaml change, so `/governance`'s.

**(D) Convert INV-063 to `substrate_conditional`** via the claim's own escape hatch,
on the ground that its two legs' preconditions are not simultaneously satisfiable on
today's substrate. The claim already contemplates this conversion and calls it "a
legitimate, useful outcome". Cheapest, and loses the least if (B) would have come
back red anyway.

## 6. Recorded alongside (not part of the decision)

1. **GOV-REUSE-1 (Step 2.4) outcome, for the audit trail.** Readouts looked for:
   per-arm MECH-205 surprise-write count / realised `surprise_weight` / replay
   start-selection spread (leg A), and across-sleep frozen-battery world-forward
   MSE delta (leg B), over a four-arm `world_rule_shift` ladder with the MEL
   CONSUMER OFF. Checked `v3_exq_798a_...20260730T010651Z_v3` (producer validation,
   no sleep at all), `v3_exq_845_...20260731T235634Z_v3` and
   `v3_exq_901_...20260808T152754Z_v3` (both consumer-ON sleep-QUANTITY runs, the
   opposite question), `v3_exq_1026_...20260914T111100Z_v3` and
   `v3_exq_1060_...20260919T012511Z_v3` (two-arm lever liveness, not a ladder).
   None carries the readout -> not recoverable -> run. That verdict stands; the stop
   is downstream of it.

2. **`substrate_queue.json` entry `e2-world-forward-sleep-trainer` is stale.** It
   still reads `status: pending_implementation` with its single `failure_record`
   marked `resolved: open`, although the build landed (ree-v3 `4610133`, 2026-09-17)
   and V3-EXQ-1060 PASSed against it on 2026-09-19. A later session reading
   readiness from that entry gets the wrong answer. Owed to `/governance` 6a-iv.

3. **Three drifted pointers in INV-063's `what_would_answer`,** all verified against
   `ree-v3` `origin/main` today. Raised as a governance flag rather than edited here.
   - P2 tells the run to assert `cumulative_sws_writes` / `cumulative_rem_rollouts`
     from output. **Neither name exists anywhere in `ree_core/`** -- they appear only
     inside a `ree_core/sleep/mel_consumer.py` docstring quoting V3-EXQ-677's DV. The
     real merged-metric keys a sleep cycle emits are **`sws_n_writes`** and
     **`rem_n_rollouts`** (confirmed by dumping the merged dict: see sec 8).
   - P3 cites `use_sleep_aggregation_cluster` at `config.py:6263`; it is at
     **`config.py:6709`**.
   - P2 cites `use_mel_consumer` / `use_entry_pressure` at `config.py:6291/6337`;
     they are at **`config.py:6737`** and **`config.py:6808`**, with
     `use_within_life_sleep_trigger` at **`config.py:6783`**.
   P4's own correction note (GFLAG-0203) is the precedent for fixing these in place.

4. **GFLAG-0355** (leg B label E1 -> E2) is already open with `/governance` and was
   not touched. This session took leg B to be E2.world_forward throughout, per
   V3-EXQ-1060's documented chain.

## 7. What was NOT done

No experiment script was written. No `experiment_queue.json` entry was appended.
`claims.yaml`, `substrate_queue.json` and `experiment_proposals.v1.json` are
untouched. `V3-EXQ-1063` is reserved but unused and can be released or re-used.

## 8. Reproduction

```
# on a box with torch, from a checkout of the umbrella branch above
/home/ree/.venv/ree/bin/python scratch/probe_inv063_v2.py   # sec 3a, ~30 min on 2 cores
/home/ree/.venv/ree/bin/python scratch/probe_inv063_v3.py   # sec 3b, ~45 min on 2 cores
```

`probe_inv063_v2.py` also prints the full merged sleep-metric key list that
establishes `sws_n_writes` / `rem_n_rollouts` (sec 6.3).

**Caveat stated rather than papered over.** The converged-base probe's P0 uses a
random-action rollout, where V3-EXQ-798a's uses the full E3 selection path over 5400
steps. Its MEL column is therefore NOT comparable to 798a's and this file makes no
claim about P1's monotonicity on a converged base -- 798a's landed 3/3 stands. The
leg-B sign result does not depend on that difference: it is measured against the
same frozen battery the P0 converged, at `conv_rel_drop` 0.997-0.999.
