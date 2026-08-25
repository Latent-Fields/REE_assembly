# MECH-152 measurement redesign -- DESIGNED, NOT QUEUED (gated on an open corrupting substrate defect)

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml, experiment_queue.json, or substrate_queue.json.**

- **Generated:** 2026-08-18T21:00Z
- **Session:** `metaworker-chip-20260816-mech152-measurement-redesign` (headless metaworker chip)
- **Chip:** `chip-20260816-mech152-measurement-redesign`
- **Source of the mandate:** confirmed `failure_autopsy_V3-EXQ-922a_2026-08-16` (Section 7 redesign spec), governance-applied 2026-08-16
- **Intended queue id:** `V3-EXQ-939` (next free; max in queue + coordinator = 938 at authoring time -- **RE-VERIFY at queue time**)
- **Intended script:** `ree-v3/experiments/v3_exq_939_mech152_terrain_modulation_depth.py`

---

## 1. Why this was designed but NOT queued

`/queue-experiment` **Step 2.5c (substrate-path overlap gate)** fires, at `severity: corrupting`:

| field | value |
|---|---|
| `sd_id` | `contextmemory-write-path-addressing-degeneracy` |
| `status` | `pending_implementation` (**open**) |
| `severity` | `corrupting` |
| `substrate_paths` | `ree_core/predictors/e1_deep.py` |
| `unblocks_claims` | SD-017, ARC-045, MECH-166 |

MECH-152's entire measured quantity is produced inside that file:
`terrain_weight = sigmoid(e1.cue_terrain_proj(cue_context))` (`e1_deep.py:495`), where
`cue_context = context_memory.output_proj(bmm(selection_weights, value_proj(memory)))`.
The overlap is not incidental -- it is the whole pathway.

The skill's rule for a `corrupting` overlap is a hard stop: do not write the script, do not
add a queue entry, route to `/implement-substrate`. That route is **already chipped and open**:
`chip-20260816-implsub-contextmemory-writepath-degeneracy`.

**Precedent, two days old and identical in kind.** The 2026-08-18 `/governance` cycle
deliberately declined to queue the SD-017 ceiling retest for exactly this reason, recording it
as `chip-20260818-sd017-ceiling-retest-gated`: *"Queueing an SD-017 retest onto that substrate
now risks producing evidence that LOOKS valid and is not, which is precisely what
severity=corrupting means."* MECH-152 runs on the same SD-016 production config and the same
module. GFLAG-0039 already flags that config against this defect (scoped to MECH-151).

**Why the stop is substantively right here, not merely procedural.** MECH-152 has now produced
two runs whose evidence looked valid and was not (EXQ-194's supporting `r_w_harm=0.70` and
V3-EXQ-922's `does_not_support`, both disqualified by the 922a autopsy as coming from the same
scale-invariant DV). A third run onto substrate carrying an open `corrupting` stamp -- where
`corrupting` is *defined* in that entry's own `severity_rationale` as "evidence that LOOKS
valid but is not" -- is the same error a third time, and this time it would look **more**
credible than the last two, because the measurement fix below is real and its preconditions
would pass.

**The gate is firing on a genuinely live entry, not an inert one.** `chip-20260816-step25c-inert-corrupting-stamp`
records that Step 2.5c's `CLOSED` substring test silently swallows `implemented_pending_validation`,
leaving three corrupting stamps inert. This entry is **not** one of them -- it is
`pending_implementation`, and that chip names it as the single live corrupting entry.

---

## 2. Probe findings (this session) -- the defect reproduces, AND a plausible over-reading is corrected

Two throwaway probes were run against the current substrate (`REEConfig.from_dims(sd016_enabled=True,
sd016_cue_slot_tagger=True, selection="soft", ctxdiv=0.5, world_dim=128)`, seed 42, 16 slots).
Neither is an experiment; neither wrote a manifest.

### 2a. An exact structural bound on attainable modulation depth

Selection weights are a softmax or one-hot, so they are non-negative and sum to 1; `value_proj`,
`output_proj` and `cue_terrain_proj` are linear, and `sigmoid` is monotone. Therefore
`cue_context` is a **convex combination** of the per-slot vectors, and the attainable range of
`w_harm` under **any** selection policy whatsoever is **exactly**

> `[ min_i sigmoid(cue_terrain_proj(output_proj(value_proj(memory_i)))) ,  max_i (same) ]`

This is a *tight* bound, not an upper bound. Consequence worth stating plainly: **`terrain_weight`
has no direct `z_world` path.** `z_world` enters only through the selection weights. This is the
sharp asymmetry with MECH-151 -- `action_bias` gets the EXQ-449a fix
(`cue_action_proj(cat([cue_context, z_world]))`) and so retains a raw `z_world` channel, which is
what GFLAG-0039 identifies as confounding MECH-151's attribution. MECH-152 has no such channel:
if slot selection carries no context, `terrain_weight` is constant, full stop.

That is directly visible in the 922a manifest and explains its most puzzling result. `A0_OFF`
sits at `sel_entropy_mean = 2.7726 = ln(16)` exactly -- the perfectly uniform saddle -- so
`cue_context` is provably constant, and indeed `w_harm_std = 3.75e-07`. The DV being
*monotonically decreasing* in cue-indexed selectivity follows: sharpening selection over a bank
whose slots carry no context organisation cannot help, and one-hot selection (`A1_PRODUCTION`,
`sel_entropy_mean = 1.1e-08`) removes even the averaging.

### 2b. The write-path defect reproduces on current substrate

3000 writes from a low-variance query stream (`base + N(0, 0.02)`, matching the entry's stated
regime), using the real `ContextMemory.write()`:

> **distinct slots ever addressed: 2 of 16** (slots 3 and 13); slots whose content changed: 2 of 16.

Independent corroboration of the substrate_queue entry's 436e/436f finding (which measured
1 of 16 on 3/5 seeds). Attainable `w_harm` depth on that bank, with `cue_terrain_proj` at init:
**0.0110**, i.e. **1.8% of the 0.6 swing MECH-152 asserts**.

### 2c. CORRECTION -- the defect does NOT make the asserted 0.6 swing unreachable

The tempting inference from 2a + 2b -- "bank degenerate, therefore depth structurally
impossible, therefore no measurement redesign can help" -- **is wrong, and this session
initially made it.** `cue_terrain_proj` is a *trainable linear map*: it can amplify an
arbitrarily small difference between two slot vectors until the sigmoid saturates. Measured,
under a best-case training regime (4000 Adam steps regressing `cue_terrain_proj` directly on
per-slot targets 0.8/0.2):

| bank | attainable `w_harm` depth | vs asserted 0.6 | `w_harm` range |
|---|---|---|---|
| defect bank (2 of 16 occupied), untrained | 0.0110 | 1.8% | [0.5033, 0.5142] |
| **defect bank, best-case trained** | **0.6056** | **100.9%** | **[0.1975, 0.8031]** |
| diverse bank (post-fix proxy), best-case trained | 0.6000 | 100.0% | [0.2000, 0.8000] |

So what the defect actually costs MECH-152 is **not attainable range**. It is:

1. **The number of representable contexts**, capped at the number of occupied slots (measured: 2).
   MECH-152's claim is a *binary* context distinction, so 2 is coincidentally just enough -- which
   is precisely why a run would look clean.
2. **Attribution.** The 2 occupied slots are selected by a deterministic `argmin` fixed point on a
   near-constant query stream; they are not *context*-organised. A positive result would then be
   attributable to the tagger having learned a 2-way split over a degenerate remnant, not to the
   cue-indexed terrain pathway MECH-152 asserts. That is exactly the `corrupting` failure mode.
3. **Conditioning**, since reaching the band requires large `cue_terrain_proj` weights to amplify a
   small slot difference.

**Scope of 2c, stated honestly:** the best-case training bypasses `z_world`, the tagger and the
selection entirely, regressing per-slot targets directly. It establishes *attainability in
principle*, NOT that the real phased training loop reaches it. Treat the 0.6056 figure as an
upper bound on what training could extract, not a prediction.

**Why this correction matters enough to record:** a future session reading the 922a autopsy
(flat output) plus the substrate entry (degenerate bank) would very reasonably conclude the depth
is unreachable and route MECH-152 to a substrate build or a demotion. Both would be wrong.
What is owed remains a measurement redesign -- it is merely *gated* on the fix, not superseded by it.

---

## 3. The redesign, fully specified (queue this once the gate clears)

All five elements the chip brief required, none dropped. New EXQ **number**, not a letter --
the question changes from "does `terrain_weight` *correlate* with hazard" to "does it *modulate*
at the claimed depth, and is that precision gain or magnitude scaling". **Do NOT set `supersedes`**:
194/194a/922/922a are disqualified, not superseded, and governance has recorded that on the claim.

### 3.1 Fix the target contrast, and gate on it (required element 2)

The inherited absolute thresholds have been wrong twice in opposite directions (EXQ-194's 0.1
nearly never fired at this env's hazard floor ~0.22; 922/922a's 0.3/0.33 nearly always fires).
**Derive the split from the run's own hazard distribution**: sample `hazard_max` over a
calibration pass before P1 and set the threshold at its **median**, making the target bimodal by
construction and mutually anti-correlated across `w_harm` / `w_goal`, exactly as the claim states.

Load-bearing precondition, measured in **both** the training and the collection series:

```python
{"name": "terrain_target_balance_train", "description": "both terrain target states >=25% of steps",
 "measured": min(p_hi_train, 1 - p_hi_train), "threshold": 0.25, "met": ...}
{"name": "terrain_target_balance_collect", ..., "threshold": 0.25, "met": ...}
```

Below floor self-routes **`substrate_not_ready_requeue`**, never a mechanism verdict. Record
`label_balance` for the training label separately from the eval label (the 047m rule).

### 3.2 Modulation DEPTH as the primary DV (required element 1)

Primary criterion, stated on the claim's own band rather than on a correlation:

- `depth_w_harm = E[w_harm | hazard-context] - E[w_harm | resource-context]`
- `depth_w_goal = E[w_goal | resource-context] - E[w_goal | hazard-context]`
- **C1:** `E[w_harm | hazard] > 0.8` **and** `E[w_harm | resource] < 0.5`
- **C2:** `E[w_goal | resource] > 0.8` **and** `E[w_goal | hazard] < 0.5`
- Pearson `r_w_harm` / `r_w_goal` **retained as descriptive secondary readouts only**, explicitly
  not adjudication-gating. A scale-invariant statistic cannot adjudicate a magnitude claim.

Report per-seed values, never mean+/-std alone.

### 3.3 Functional non-degeneracy floor (required element 3)

Replace `terrain_weight_std_floor = 1e-9` (which `A0_OFF` cleared by ~375x while sitting ~1.6
million times below the asserted swing) with **`>= 0.05`**, one-tenth of the 0.6 band, referenced
to the claim's own asserted magnitude. Emit as a load-bearing precondition with numeric
`measured` + `threshold` so the indexer recomputes it.

### 3.4 SCORE the OFF control (required element 4)

`A0_OFF` must be scored on the **mechanism** criteria, not carried as context. 922a's five
pre-registered branches covered A2-vs-A1 exhaustively and the control not at all, so the one
outcome that actually occurred -- the control winning -- was unrepresentable.

Add an explicit pre-registered branch:

> **`control_outperforms_experimental_arms`** -- if `A0_OFF` meets the depth criteria at or above
> the selective arms, the instrument is measuring something other than a cue-indexed pathway.
> Self-route `non_contributory` under an instrument reading. **Do NOT route `mixed`** -- `mixed`
> connotes a measured weak effect, and nothing would have been measured.

### 3.5 Precision-gain vs magnitude-scaling discriminator (required element 5)

Named in MECH-152's own `what_would_answer` since 2026-04-02 (Kanashiro et al. 2017 gain-control
linkage) and measured by **no** run in the family. This is also the MECH-152-vs-ARC-016
discriminator, both subsumed by ARC-044.

The substrate applies `m = m * w_harm` (`e3_selector.py:1216-1218`) -- a pure multiplicative
scale. Three readouts, pre-registered together, separate the readings:

- **D1 (instrument positive control, analytically constrained).** Within a decision step, across
  candidate trajectories, the coefficient of variation of the harm term is **exactly invariant**
  to `w_harm` under `m * w_harm`. Declare it as such: if D1 moves, the probe is broken. This is a
  null that *must* hold, and its role is to validate the apparatus -- not to test the claim.
- **D2 (the real discriminator).** Harm-term share of across-candidate **score variance**:
  `var(lambda_eff * m * w_harm) / var(total score)`, in high- vs low-`w_harm` bins. Because the
  score is a *sum*, this rises with `w_harm` even under pure scaling -- i.e. the implementation
  delivers decision-level precision gain via *relative weighting* while not reducing the harm
  estimate's own variability. That distinction is the substance of the MECH-152/ARC-016 question.
- **D3 (the claim's literal wording).** Variability of the harm evaluation itself, high- vs
  low-`w_harm`. Under `m * w_harm`, `std` scales **up** with `w_harm` -- the opposite of "reduces
  variability". A confirmed D3 increase **falsifies the precision-gain reading in favour of simple
  magnitude scaling**, which per the claim's own `what_would_answer` would *not* support
  collapsing MECH-152 into ARC-016.

Declare per-arm DV-symmetry invariance in the queue `note`, per the skill's mandatory
declaration: the manipulation here is a per-context multiplicative scale on a *magnitude* DV
(between-context mean difference), which is not invariant under it -- unlike the rank/argmax DVs
that the broadcast-scalar rule warns about.

### 3.6 Carry-overs and recording

- Keep recording `w_harm_std` / `w_goal_std` / `final_terrain_loss` / `hazard_std` -- 922a's
  optional-field discipline is the only reason its diagnosis was possible. Make it the family default.
- **Add `n_occupied_slots`** and per-slot cosine similarity to the manifest. Nothing in the
  194/922/922a family recorded it, which is why the bank's state had to be inferred here rather
  than read. This is the single highest-value addition for any successor.
- Also record the **attainable-depth bound** of section 2a (a 3-line computation over the slot
  bank): it is the denominator against which any measured depth should be read.
- Phased training P0a/P1 as in 922a; `stamp_recording_core(...)` after `arm_results` is assembled;
  per-cell `arm_cell(...)` fingerprints with `include_driver_script_in_hash=False` on the OFF arm.
- `EXPERIMENT_PURPOSE = "diagnostic"`; `claim_ids = ["MECH-152"]` (single -- do not inherit
  922's MECH-150/151/ARC-041 tags).

---

## 4. Gate-clearing condition (the STOP-CHECK a successor should run)

Queue `V3-EXQ-939` only once **all** hold:

1. `substrate_queue.json` entry `contextmemory-write-path-addressing-degeneracy` is
   `implemented` / `implemented_validated` / `validated` -- **and** note the Step 2.5c substring
   defect: `implemented_pending_validation` is NOT a clearing state, whatever the gate's own
   `CLOSED` tuple currently does with it (see `chip-20260816-step25c-inert-corrupting-stamp`).
2. `ContextMemory.write()` no longer addresses by hard `argmin` (`e1_deep.py`, ~lines 135-147).
3. A re-run of the section 2b probe shows **> 2 of 16** slots occupied under a low-variance stream.
4. `task_claim.py check --resources ree-v3/experiment_queue.json` does not exit 3.
5. Re-verify the next free EXQ id (938 was max at authoring time).

---

## 5. What this session did NOT do, and why

- **Did not queue anything.** Step 2.5c hard stop (section 1).
- **Did not write the driver script.** The skill forbids it at a `corrupting` stop, and the
  design above is the deliverable a successor needs.
- **Did not open a substrate_queue entry.** The chip brief explicitly forbade it, and correctly:
  no *new* substrate work is owed. The blocking entry already exists and is already chipped.
- **Did not change MECH-152's status.** It remains `provisional`, `pending_retest_after_substrate: true`,
  re-scoped to a measurement redesign. The 2026-08-16 HELD demotion still should not be applied,
  and nothing here changes that: MECH-152 still has never been tested at the magnitude it asserts.
  **This file promotes nothing and demotes nothing.**

---

## 6. AMENDMENT 2026-08-25T07:50:49Z -- id correction, and a SIXTH required element

Appended by session `mech-152-measurement-redesign-d5bf26` while re-running the section 4
STOP-CHECK for `chip-20260818-mech152-redesign-queue-gated`. **The gate is still closed and
this amendment does not open it.** Evidence and method:
`mech152_writepath_addressing_probe_20260825.md` (+ `.py`, `.results.json`), REE_assembly
`c3bdc3c4cd`.

### 6.1 `V3-EXQ-939` IS TAKEN -- queue as `V3-EXQ-949`

Section 4 item 5 said to re-verify, and it does not hold: `939` is now
`v3_exq_939_mech303_proximity_gated_contextual_safety_vigilance_release.py` (with a `939a`).
Max queue id is **948**; next free is **949**. The intended script name becomes
`ree-v3/experiments/v3_exq_949_mech152_terrain_modulation_depth.py`. Everything else in
section 3 stands unchanged. Still a new **number**, still no `supersedes`.

### 6.2 The write-path validation has RUN -- the prior step is an AUTOPSY, not an experiment

Section 4's gate is written as though the write-path fix were still owed. Two runs have since
landed:

- **`V3-EXQ-943`** (2026-08-20, PASS, autopsy confirmed 2026-08-21) -- occupancy. Its autopsy
  states occupancy cannot discriminate BIAS from REFRACTORY.
- **`V3-EXQ-946`** (2026-08-23, PASS, `context_informative_address_found_at_operating_point`)
  -- addressing informativeness on a real REEAgent, against a blockwise-permutation order-only
  null, with positive and negative instrument controls both met. `BIAS_W1_0` clears 5/5 seeds;
  `REFRACTORY` clears 2/5 and fails. **But the magnitude is ~0.0005 bits against a 1.0-bit
  positive control** -- "distinguishable from a clock", not "carries usable context".

**`V3-EXQ-946` has not reached anything that gates on it**: absent from `review_tracker.json`,
absent from `pending_review.md` (generated 2026-08-22T13:45:22Z, i.e. stale -- it predates the
run), targeted by no `failure_autopsy_*.json`, and absent from the substrate_queue entry
(which carries `validation_record_943` only). Being `experiment_purpose: diagnostic`, it needs
a confirmed `/failure-autopsy` before it can drive the human call the chip is waiting on.

So section 4's gate should be read as: **regen the index, autopsy 946, then put the human call
to the user with 946's magnitudes in front of them.** No further write-path experiment is owed.

### 6.3 REQUIRED ELEMENT 6 -- bank-content ablation control

**This is the substantive addition, and section 3's five elements do not cover it.**

Measured this session (10 seeds x 3 write modes, best-case training on a frozen bank, scored on
held-out samples): under the production `cue_slot_tagger=True` read path, attainable
between-context modulation depth reaches **0.900 and clears the claim's band in 30/30 cells** --
under every write mode including unfixed LEGACY on its 1-slot-bank seeds, **and equally in
30/30 cells when the slot bank is replaced with random content carrying nothing written at
all**. On the legacy (tagger-off) path the same measurement gives 0.12-0.33 and clears the band
in 1-3 of 10.

The consequence for this design specifically: **element 4's OFF control does not catch it.**
`A0_OFF` is cue-indexing/tagger OFF, so a run would show a low OFF arm and a band-clearing
production arm and read as a clean positive -- while the contrast actually measured is *learned
router present vs absent*, not *cue-indexed retrieval present vs absent*. That is the
`corrupting` failure mode arriving through a door the write-path gate does not cover.

> **Element 6.** Add an arm identical to the production arm (`cue_slot_tagger=True`) but with
> slot contents **randomised or shuffled**. Pre-register: if that arm reaches the depth band at
> or near the production arm, the instrument is not measuring a cue-indexed pathway --
> self-route `non_contributory` under an instrument reading, exactly as element 4 does for
> `control_outperforms_experimental_arms`. **Do NOT route `mixed`.** Record its depth beside
> the production arm's; it is the denominator the measured depth should be read against, in the
> same role section 3.6 gives the section 2a attainable-depth bound.

Cost: one arm. It is the only one of the six that separates retrieval from readout capacity.

### 6.4 Scope of this amendment, and what it does NOT claim

- **Best-case training is an upper bound**, the same caveat section 2c attached to its 0.6056:
  4000 Adam steps directly on the terrain objective, bank frozen, no competing losses. What
  6.3 establishes is that the DV **fails to constrain** the mechanism -- the ceiling is
  identical with and without content -- **not** that a real phased run reaches that ceiling.
  `V3-EXQ-922a` measured real `w_harm_std` six orders lower.
- **Not a real agent**: synthetic two-cluster stream, `ContextMemory` driven directly, tagger
  matched architecturally rather than driven by real `z_world`. Where this probe and
  `V3-EXQ-946` disagree on mode ranking -- and they do, this probe favouring REFRACTORY on
  depth, 946 favouring BIAS on addressing -- **946 wins**: it is a real agent with a validated
  order-only null, and this probe's own MI columns are the instrument 946 was built to replace.
- **Promotes nothing, demotes nothing**, and does not change MECH-152's status,
  `pending_retest_after_substrate`, or the standing advice that the 2026-08-16 HELD demotion
  should not be applied.
- Open question worth one line in any successor: it was **not** measured whether the legacy
  (tagger-off) path also clears on a random bank. If it does, 6.3 generalises past the
  production config.
