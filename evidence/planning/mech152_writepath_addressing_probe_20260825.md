# MECH-152: the 21 Aug HOLD's owed work -- gate re-check, and the control the redesign is missing

**Status: PROBE FINDINGS, AWAITING USER/GOVERNANCE REVIEW. Nothing here was written to
`claims.yaml`, `experiment_queue.json`, or `substrate_queue.json`. This file promotes
nothing and demotes nothing.**

- **Generated:** 2026-08-25T07:49:24Z
- **Session:** `mech-152-measurement-redesign-d5bf26`
- **Chip:** `chip-20260818-mech152-redesign-queue-gated` (left OPEN -- see section 1)
- **Mandate:** the 2026-08-21 governance HOLD on MECH-152 (`gov-20260821-0203`, GFLAG-0044):
  *"Owed work is a measurement redesign gated on the corrupting write-path"*
- **Probe script:** `mech152_writepath_addressing_probe_20260825.py`
- **Raw results:** `mech152_writepath_addressing_probe_20260825.results.json`

---

## 1. Gate re-check: STILL CLOSED, and `V3-EXQ-939` is no longer free

The STOP-CHECK in `mech152_measurement_redesign_gated_20260818.md` section 4, re-run
against `origin/master` today:

| # | Condition | Result |
|---|---|---|
| 1 | entry is `implemented`/`implemented_validated`/`validated` | **NO** -- `implemented_pending_validation`, which that doc and the chip both state is not a clearing state |
| 2 | `ContextMemory.write()` no longer addresses by hard argmin | **NO by default** -- both fixes landed but `contextmemory_write_usage_balancing=False` and `contextmemory_write_selection="argmin"` (config.py:458, 507); no driver in `ree-v3/experiments/` sets either |
| 3 | `> 2 of 16` slots occupied under a low-variance stream | **NO under the default path** -- see section 3 |
| 4 | `task_claim.py check --resources ree-v3/experiment_queue.json` | **exit 3** -- owned by `queue-conversion-ceiling-gate-f2545f`, with `f-dominance-regime-retest-ddbe10` also queued behind it |
| 5 | re-verify next free EXQ id | **`V3-EXQ-939` IS NOW TAKEN** by `v3_exq_939_mech303_proximity_gated_contextual_safety_vigilance_release.py`. Max id is now 948; next free is **949** |
| 6 | MECH-152 not already queued | confirmed -- 0 hits in `experiment_queue.json` |

**The chip stays open.** Item 5 is a correction the chip and the redesign doc both need:
any successor must queue as `V3-EXQ-949`, not `939`.

## 2. What the prior step actually is -- and it is NOT another experiment

The chip's 2026-08-23 state update says the gate is waiting on a human governance call on
"whether occupancy-without-addressing (BIAS) or the k+1 eligibility floor (REFRACTORY)
closes the corrupting 1-slot-bank defect". That is still true, but the picture has moved
since it was written, and the movement is not recorded anywhere the gate can see it:

- **`V3-EXQ-943`** (2026-08-20, PASS, autopsy confirmed 2026-08-21) settled **occupancy**.
  Its own autopsy states plainly that occupancy cannot choose between the two modes.
- **`V3-EXQ-946`** (2026-08-23, PASS, `context_informative_address_found_at_operating_point`)
  settled **addressing informativeness** -- the exact question the human call turns on --
  on a real REEAgent, with a blockwise-permutation order-only null and both a positive and
  a negative (pure-clock) instrument control, both met.

**`V3-EXQ-946`'s result has not reached anything that gates on it.** It is:
- not in `review_tracker.json` `reviewed_run_ids`;
- not in `pending_review.md` (that file was generated **2026-08-22T13:45:22Z**, i.e. before
  946 ran -- it is stale, not silent; 946 has a `runs/` pack and will index on the next regen);
- targeted by **no** `failure_autopsy_*.json`;
- absent from the substrate_queue entry, which carries `validation_record_943` and no 946 record.

Because 946 is `experiment_purpose: diagnostic`, it needs a **confirmed `/failure-autopsy`**
before it may drive governance action. So the prior step, stated precisely, is:

> **regen the evidence index, then autopsy `V3-EXQ-946`, then put the human call to the user
> with 946's numbers in front of them.** No new experiment is owed for the write path.

Per the CLAUDE.md chip-exception rule, `/failure-autopsy` work is reported inline and not
chipped, which is why this file reports it rather than raising a chip.

### What 946 actually found (numbers, since the call turns on them)

| Arm | seeds clearing the order-only null (z >= 2.0) | observed MI (bits) |
|---|---|---|
| `BIAS_W1_0` (default weight) | **5/5 -- passes** | 0.00022 - 0.00058 |
| `BIAS_W0_1` | **3/5 -- passes** | 0.00029 - 0.00059 |
| `BIAS_W0_01` | 1/5 -- fails | 0.00005 - 0.04392 |
| `REFRACTORY` | 2/5 -- fails | 0.000006 - 0.01709 |

Two things must be said together, because either alone misleads:

1. **BIAS wins on this instrument and REFRACTORY loses it.** That is the opposite of the
   structural case for `refractory` written into `e1_deep.py`'s `_select_write_slot`
   docstring, and the opposite of the depth ranking in section 4 below. If the human call
   is made on addressing informativeness, it selects **BIAS**.
2. **The magnitude is minute.** 946's own positive control -- an address that is exactly a
   function of context -- measured **1.0 bits**. BIAS at default weight carries ~0.0005 bits,
   about **0.05% of that**. The result is "distinguishable from a clock", not "carries usable
   context". Reading 946 as "addressing is fixed" would be a category error of the same kind
   the 922a autopsy caught.

---

## 3. This probe, and what it measures

`mech152_writepath_addressing_probe_20260825.py`. A **probe, not an experiment**: no manifest,
no queue entry, no claim write. 10 seeds x 3 write modes, 3000 writes from a two-context
low-variance stream (context switching every 5 writes, matching the 436-family harness),
driving the real `ContextMemory.write()`. Per cell it measures the attainable MECH-152
modulation depth -- the redesign's own primary DV -- by training `cue_terrain_proj`
best-case on a **frozen** bank and scoring on a **disjoint held-out** half.

It exists because section 2c of the redesign doc established attainability **across slots**
(regressing per-slot targets directly, bypassing selection) and explicitly did not establish
attainability **across contexts**, which additionally requires the selection to route
different contexts to different slots. That gap is where the pending governance call sits.

Occupancy under the **default** (unfixed) path reproduces the defect: 1 slot on seeds 42 and
13, 2 on seed 4 -- STOP-CHECK item 3 is not met.

**Two of this probe's columns are not trustworthy and are marked descriptive-only in the
results file.** `nmi_context_slot` and `js_divergence_bits` measure I(slot; context) against
chance, which is precisely the trap `V3-EXQ-946`'s driver header identifies as having cost
this lineage six generations: a period-16 clock or a period-(k+1) cycle can produce non-zero
MI purely by aligning with the context block schedule. 946's blockwise-permutation null is
the correct instrument and supersedes them. They are retained only because they are cheap.

---

## 4. Finding A -- occupancy does not predict MECH-152 measurability

The raw correlation across all 30 cells is `r(depth, n_distinct) = -0.53`, but **that number
is confounded and should not be quoted**: the low-occupancy cells cluster on seeds 42/13/4,
which happen to have the largest per-slot spread (`bound_untrained` 0.012/0.040/0.058 against
~0.001-0.010 elsewhere), and spread independently predicts depth. The defensible statement is
the within-stratum one:

> **Among the 21 cells at full 16/16 occupancy, attainable depth ranges 0.0000 to 0.7310**
> (mean 0.194, sd 0.198).

Seed 100 makes it concrete -- all three modes at 16/16 occupancy, identical write stream:
LEGACY 0.4075, BIAS **0.0005**, REFRACTORY 0.7310. BIAS also returns exactly 0.0000 at seeds
1 and 5, at full occupancy.

So a 16/16 occupancy PASS -- which is what `V3-EXQ-943` gave BIAS on 5/5 seeds -- is
compatible with essentially **zero** MECH-152 measurability. Occupancy cannot license this
gate for this claim, whichever mode the human call selects.

On the legacy read path the mode ranking is REFRACTORY (median depth 0.329, band 3/10) >
BIAS (0.325, 1/10) > LEGACY (0.123, 1/10). Note this **disagrees with 946's ranking**; see
section 6.

---

## 5. Finding B -- the redesign's DV clears its band on a bank with no content in it

This is the load-bearing result, and it is a caution, not a green light.

The redesign would run the production config, which sets `cue_slot_tagger=True`. That
replaces the frozen q.k attention with a learned MLP `z_world -> slot logits`
(`e1_deep.py:513-517`), trained by the terrain_loss gradient -- i.e. it gives the selection a
learned route from context that the legacy path does not have. Adding an architecturally
matched tagger arm:

| write mode | legacy read path | tagger read path | **tagger, RANDOM bank** |
|---|---|---|---|
| LEGACY (unfixed argmin) | 0.123, band 1/10 | 0.900, band **10/10** | 0.900, band **10/10** |
| BIAS | 0.325, band 1/10 | 0.900, band **10/10** | 0.900, band **10/10** |
| REFRACTORY | 0.329, band 3/10 | 0.900, band **10/10** | 0.900, band **10/10** |

All figures are median over 10 seeds, scored on held-out samples.

Three readings, in order of how much they should worry a successor:

1. **The tagger clears MECH-152's asserted band under every write mode, including the
   unfixed LEGACY path on its 1-slot-bank seeds.** On this measure the write-path defect is
   not what stands between MECH-152 and a band-clearing result.
2. **It also clears the band when the entire slot bank is replaced by random values**
   carrying no written content whatsoever -- 30/30 cells, at the same depth. The
   attribution control finds no difference between a real memory and noise.
3. Therefore **the DV is not measuring cue-indexed retrieval.** With a trainable router in
   front of it, between-context modulation depth measures the separability of the two input
   contexts and the capacity of the readout, and it reaches ceiling whether or not the
   memory contains anything.

**The redesign's existing OFF control does not catch this.** Element 4 scores `A0_OFF`, which
is cue-indexing/tagger OFF -- the legacy path, where depth is genuinely low (0.12-0.33). So a
run would show a low OFF arm and a band-clearing production arm and look like a clean
positive, while the contrast actually measured is *router present vs router absent*, not
*cue-indexed retrieval present vs absent*. That is the `corrupting` failure mode -- "evidence
that LOOKS valid and is not" -- arriving through a door the write-path gate does not cover.

### The sixth element this implies

Before `V3-EXQ-949` is queued, the redesign needs, pre-registered alongside its existing five:

> **Element 6 -- bank-content ablation control.** An arm identical to the production arm
> (tagger ON) but with slot contents randomised or shuffled. If it reaches the depth band at
> or near the production arm, the instrument is not measuring a cue-indexed pathway:
> self-route `non_contributory` on an instrument reading, exactly as element 4 does for
> `control_outperforms_experimental_arms`. **Do NOT route `mixed`.**

This is cheap (one extra arm) and it is the only control among the six that separates
retrieval from readout capacity.

---

## 6. Limits -- stated plainly, because two of them are load-bearing

1. **Best-case training is an upper bound, not a prediction.** Same caveat section 2c
   attached to its 0.6056: the tagger and head are trained 4000 Adam steps directly on the
   terrain objective with the bank frozen and no competing losses. A real phased loop has
   competing objectives, and `V3-EXQ-922a` measured actual `w_harm_std` of 3.8e-7 to 1.0e-2,
   six orders below. **What section 5 establishes is that the DV fails to CONSTRAIN the
   mechanism -- the ceiling is identical with and without content. It does not establish
   that a real run reaches that ceiling.** A real run might show a small effect for entirely
   different reasons; the point is that a large one would not be attributable.
2. **This is not a real agent.** Synthetic two-cluster stream, `ContextMemory` driven
   directly, and the tagger is an architecturally matched MLP over the latent vector rather
   than the real `z_world`. `V3-EXQ-946` is the real-agent measurement and should be
   preferred wherever the two speak to the same question.
3. **Sections 4 and 6's mode rankings disagree, and 946 should win.** This probe ranks
   REFRACTORY above BIAS on legacy-path depth; 946 ranks BIAS above REFRACTORY on addressing
   informativeness. 946 is a real agent with a validated order-only null; this probe's own
   addressing columns are the instrument 946 was built to replace. Where they conflict, take
   946. The disagreement is recorded rather than resolved here.
4. **Not measured:** whether the legacy (non-tagger) read path also clears on a random bank.
   If it does, finding B generalises beyond the production config; if it does not, the
   legacy path's lower ceiling is a capacity limit rather than a content effect.
5. `n=10` seeds, one environment regime, one `jitter` value. Nothing here is powered as an
   experiment and none of it should be cited as evidence for or against MECH-152 itself.
   It is evidence about whether MECH-152 is **measurable**, not about whether it is true.

---

## 7. Recommendation

1. **Do not queue `V3-EXQ-949` yet.** The gate is closed on its own terms, and section 5
   gives an independent reason not to queue even if it opened.
2. **Regen the evidence index and autopsy `V3-EXQ-946`.** That is the actual prior step; the
   write-path validation experiments have both run.
3. **Put the human call to the user with 946's numbers**, including the 0.0005-bits vs
   1.0-bit positive-control comparison, so the call is made on magnitude and not only on
   which arms cleared a null.
4. **Amend the redesign doc** with element 6 (section 5) and the `V3-EXQ-939 -> 949` id
   correction (section 1) before any successor queues it.
5. **Consider whether the write-path gate is the right gate for MECH-152 at all.** On the
   evidence here it is neither necessary (the tagger reaches the band without it) nor
   sufficient (the random-bank control clears it too). The binding constraint is the
   instrument, which is what the 922a autopsy said in the first place.
