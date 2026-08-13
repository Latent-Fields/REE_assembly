# Failure autopsy -- V3-EXQ-436e (SD-017 / ARC-045 / MECH-166)

- **Generated (UTC):** 2026-08-13T04:19:12Z
- **Scope:** single
- **Status:** confirmed (user-adjudicated at the Step 8 gate, 2026-08-13)
- **Target run:** `v3_exq_436e_sd017_mech166_occupied_slot_retest_20260812T221724Z_v3`
- **Queue id:** V3-EXQ-436e (`supersedes` V3-EXQ-436d)
- **Claims:** SD-017 (stable), ARC-045 (candidate), MECH-166 (candidate)
- **Outcome as recorded:** FAIL, self-routed `non_contributory`, `interpretation.label = insufficient_occupancy_for_c1`
- **Machine:** ree-cloud-2, 1896.3 s, substrate `871c221933`, clean tree

**Headline.** The DV repair this run was commissioned to perform **succeeded**. It failed on a
different gate -- a slot-occupancy precondition -- and the cause is that the substrate which
unblocks these three claims **shipped one day before the run and was left switched off**. Nothing
needs building. The correct next action is a re-queue with the existing knobs armed.

---

## 1. Facts (no interpretation)

### 1a. Dry-run gate (Step 2a)

`scripts/check_dry_run_citations.py` over every run_id cited here -- 436e, 436d, 436c, 436b, 436a:
**0 dry cited, 0 dry in named families, 0 ambiguous, 5 clean, 0 unknown** (exit 0). No smoke enters
this diagnosis. `dry_run_checked: true`, `excluded_dry_run_ids: []`.

### 1b. Recording provenance

`ree-v3/validate_recording.py --paths <manifest>`: **OK -- 1 complete, 0 always-core gaps, 0
thin-pack provenance drops, 0 schema warnings.** `substrate_hash`, `substrate_commit`, `config`,
`seeds`, `machine` / `machine_class`, `elapsed_seconds` and `recording_schema` are all present. There
is **no recording debt in this run** -- a notable first for this lineage, whose 436b generation was
adjudicated precisely on a recording gap.

### 1c. What the run measured, and what happened

436e implements all six items of Recommendation #4 from
`failure_autopsy_V3-EXQ-436d-methodology-check_2026-08-07` (confirmed, user-confirmed): an
occupied-slots-only statistic tracking `write()`'s own `min_idx`; similarity and occupancy reported
separately rather than as a product; a real write path for WAKING_ONLY (`sd016_writepath_mode =
'sense_only'`, held constant across arms); Adam drift neutralised
(`context_memory.memory.requires_grad_(False)`); the baseline re-derived empirically at run time;
and a NO_WRITES negative control checked against that re-derived null.

**P0 gate -- 4 of 5 checks clear:**

| P0 check | Measured | Floor / tolerance | Met |
|---|---|---|---|
| `sws_context_memory_writes_occur` | 800.0 | >= 1.0 | yes |
| `rem_attribution_rollouts_occur` | 600.0 | >= 1.0 | yes |
| `waking_writepath_engaged` (new in 436e, the F1 fix) | 15428 | >= 1.0 | yes |
| **`sufficient_occupancy_for_c1`** (new in 436e, the F6 fix) | **2 seeds** | **>= 3 seeds** | **NO** |
| `adam_drift_neutralized` (new in 436e, the F5 check) | max abs z = 1.670 | <= 4.0 sigma | yes |

The NO_WRITES calibration arm executed exactly 0 write calls on all 5 seeds and its raw whole-bank
cosine sits inside the freshly-derived untouched-bank null (mean 1.92e-05, sd 7.79e-03, n=500), max
|z| = 1.670. The F5 confound identified in 436d is **demonstrably closed**.

**Per-seed occupancy and the primary DV:**

| Seed | WAKING occupied | SWS_THEN_REM occupied | WAKING write calls | SWS_THEN_REM write calls | `slot_cosine_sim_occupied_only` W -> S | C1 scoreable | C1 passes |
|---|---|---|---|---|---|---|---|
| 42 | 8 | 8 | 3022 | 4692 | 0.999017 -> 0.996564 (-0.00245) | yes | **yes** |
| 7 | **1** | **1** | 3209 | 4722 | undefined | no | -- |
| 13 | **1** | **1** | 3110 | 4832 | undefined | no | -- |
| 100 | **1** | **1** | 3019 | 4884 | undefined | no | -- |
| 200 | 9 | 10 | 3068 | 4623 | 0.967952 -> 0.831095 (-0.13686) | yes | **yes** |

Two facts to hold together:

1. **Three seeds occupy exactly one slot of sixteen in BOTH arms**, despite 3,019-4,884 `write()`
   calls per arm. The collapse is **arm-independent** -- it is not something sleep does.
2. **On both seeds where the corrected instrument is defined, C1 passes in the predicted
   direction** (SWS_THEN_REM < WAKING_ONLY). 2/2, one of them by a wide margin (0.968 -> 0.831).
   The registered bar is >= 3/5 seeds, so with an effective denominator of 2 the criterion is
   **unsatisfiable by construction** -- the same structural shape 436d's F6 identified, arriving
   through a different door.

Secondary, non-gating: C4 (`slot_separation > 0.3` in SWS_THEN_REM) passes 2/5. Waking-phase
action-class entropy is healthy (1.198-1.240) on every seed and arm, so the monomodal-collapse
confound remains ruled out and `non_degenerate` is `true`.

### 1d. Which criterion failed

**Neither a discrimination criterion nor a negative control** -- both of those behaved. The failure is
at the **readiness (P0) layer**: a precondition on how many seeds carry a measurable DV at all. This
distinction matters for Step 3: a P0 failure cannot weigh on the claim in either direction.

---

## 2. Mechanism -- established by probe, with one hypothesis refuted

`ContextMemory.write()` (`ree-v3/ree_core/predictors/e1_deep.py:140-147`) addresses by **argmin**:

```python
query   = self.query_proj(state)
scores  = torch.mm(query, self.memory.t())
min_idx = scores.mean(0).argmin()                       # the LEAST-aligned slot
self.memory.data[min_idx] = 0.9 * self.memory.data[min_idx] + 0.1 * write_signal.mean(0)
```

**Hypothesis H-freeze (REFUTED -- recorded so it is not re-derived).** The obvious first reading is
that 436e's own F5 fix caused this: `requires_grad_(False)` freezes `context_memory.memory`, and
`sd016_diversification_weight = 0.5` pushes slots apart *by gradient on that same parameter*, so
freezing the bank to kill Adam drift would also disable the one force that spreads slots. Tested
directly against the real `ContextMemory` class: under a varied (iid) state stream the write path
fans out to **11-14 of 16 slots on every seed, frozen and unfrozen alike** (600 and 3000 write
loads, with and without the diversification step). Freezing is **not** the cause. The interaction is
real but inert at this operating point.

**Hypothesis H-degenerate-query (CONFIRMED).** The argmin rule locks iff the *query stream* is
near-constant. Holding the state at a fixed base vector plus jitter, occupancy after 3000 writes:

| jitter | s42 | s7 | s13 | s100 | s200 |
|---|---|---|---|---|---|
| 0.0 | **1** | 16 | 14 | **1** | **1** |
| 1e-3 | **1** | 16 | 14 | **1** | **1** |
| 1e-2 | **1** | 16 | 16 | **1** | **1** |
| 3e-2 | 3 | 16 | 16 | **1** | **1** |
| 0.078 (= state rms) | 5 | 16 | 16 | 3 | **1** |

This reproduces the observed phenomenon exactly in shape: a hard **1-vs-many bimodality**, seed-
dependent, insensitive to write count, appearing only as query variability falls. (The particular
seeds that lock differ from the real run because the synthetic base state is not the agent's actual
latent; the regime, not the seed list, is what transfers.)

**The discriminator is a sign test, and it predicts 5/5.** With a constant query, `score_i` moves
only through `memory_i`, so writing slot `i` changes its score by `0.1 * q . (write_signal -
memory_i)`. Negative -> the written slot sinks further, stays the argmin, and absorbs every
subsequent write:

| Seed | `delta = q . (write_signal - memory[argmin])` | Predicted | Observed occupancy |
|---|---|---|---|
| 42 | -0.003090 | LOCK | 1 |
| 7 | +0.048493 | rotate | 16 |
| 13 | +0.026820 | rotate | 14 |
| 100 | -0.001351 | LOCK | 1 |
| 200 | -0.017449 | LOCK | 1 |

So the collapse is a **deterministic fixed point of the write-addressing rule under a degenerate
query stream**, decided by geometry at initialisation -- not a stochastic or training-duration
effect, and not attributable to the sleep manipulation.

---

## 3. Root cause -- already registered, and already fixed

The degenerate-query regime is **not a new discovery**. `substrate_queue.json`'s SD-016 entry
(`ContextMemory cue-indexed retrieval -- validation gated on env entropy precondition`) has recorded
since **2026-04-28** (V3-EXQ-418f + 418g):

> "...`action_class_entropy` stays at 1.105e-10 across all arms because **z_world produces
> near-identical queries (cosine 0.998 across batch)**. The substrate's mechanism (cue-indexed
> retrieval) requires distinguishable z_world cue patterns; the current CausalGridWorldV2 configs
> ... do not generate enough cross-context z_world entropy for any retrieval substrate to do work."

That is precisely the input regime the probe above shows makes argmin-write lock. Two independent
lines -- a 2026-04-28 attention/retrieval diagnostic and a 2026-08-12 write-occupancy failure --
converge on one substrate property.

**And the fix shipped the day before this run.** That same entry's
`status_note_addendum_20260811` records:

> "Implemented the combination in ree-v3: `E1DeepPredictor.compute_context_divergence_loss`
> (ree-v3 `110a2785b6`) ... Recommended production combination: `sd016_cue_slot_tagger=True`,
> `sd016_cue_slot_tagger_selection='gumbel'`, `sd016_context_divergence_weight=0.5`. ...
> **MECH-150/151/152/ARC-041/INV-040/SD-017 are now unblocked for their own validation
> experiments** (not run here ... queuing those is `/queue-experiment`'s job)."

`unblocks_claims` on that entry names **SD-017** explicitly.

**V3-EXQ-436e did not arm any of it.** Verified three ways:

- `git merge-base --is-ancestor 110a2785b6 871c221933` -> **true**. The fix IS in 436e's substrate
  commit. This is a configuration gap, not a stale checkout.
- The 436e config carries **only** `sd016_diversification_weight` and
  `sd016_writepath_mode_by_condition`. No `sd016_cue_slot_tagger`, no
  `sd016_context_divergence_weight`.
- `grep` over the 436e driver: **zero** occurrences of either knob.

Both default off (`sd016_cue_slot_tagger: bool = False`; `sd016_context_divergence_weight` default
0.0 = no-op, `ree_core/utils/config.py:442`). SD-016's landing note said SD-017 was unblocked;
436e was queued the next day against the unarmed default.

This is a textbook instance of the standing hazard "**claim status is not the flag default -- check
the knob first**". The chip that produced 436e
(`chip-20260812-v3exq436e-sd017-dv-repair`) was scoped tightly and correctly to the DV repair; the
SD-016 landing 20 hours earlier was simply never in its frame, and nothing mechanically connects
`substrate_queue.unblocks_claims` to the config of an experiment tagging that claim.

**Corpus exposure (recorded, deliberately not chipped -- see Step 8).** Only **5** drivers in
`ree-v3/experiments/` arm `sd016_cue_slot_tagger` and only **2** arm
`sd016_context_divergence_weight`; all five are SD-016's own lineage (418m, 898, 907, 908, 922). No
sleep-lineage driver arms either. Whether other claims listed in that entry's `unblocks_claims`
(MECH-150/151/152, ARC-041, INV-040) are similarly being tested against the unarmed default is an
open question this autopsy notes but does not investigate.

---

## 4. Claim-layer mapping

| Claim | Type | Status | Did the run let the claim express itself? |
|---|---|---|---|
| SD-017 | design_decision | stable | **No.** The SWS/REM passes fired (800 / 600), but the readout they write into could only differentiate on 2/5 seeds because cue-conditioned slot addressing was off. |
| ARC-045 | architectural_commitment | candidate | **No.** Same. Note additionally that ARC-045's own near-1.0 undifferentiated-baseline calibration was already retired by the 436d methodology check; 436e's empirically re-derived null replaces it correctly. |
| MECH-166 | mechanism_hypothesis | candidate | **No.** MECH-166 predicts slot *structure* must consolidate before slot-*filling* yields signal. With 1 occupied slot there is no structure to consolidate, on three of five seeds. |

`claim_ids` tagging is **accurate** -- all three make the same slot-differentiation prediction and the
run targets exactly that. No inherited-tag problem here.

**This run does not weigh against any of the three.** It is a precondition failure upstream of the
comparison. The 2/2 directional passes are genuine but under-powered and must not be read as
support either.

**Supersession.** 436e supersedes 436d. The `weakens` readings recorded from 436c and (initially)
436d are now doubly superseded -- first by the 2026-08-07 methodology check, and now by a run whose
instrument is sound. Nothing in this lineage currently constitutes evidence against SD-017 /
ARC-045 / MECH-166.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **untested** | P0 precondition failure; the comparison the claims predict was never reached on 3/5 seeds |
| Biological reference | **clear** | Hippocampus -> neocortex schema installation (Diekelmann & Born 2010); Sanders/Wilson/Gershman 2020 hidden-state prior. Not a formal-definition import -- no lit-pull owed |
| Prerequisites | **present but unarmed** | SD-016 cue-indexed retrieval landed 2026-08-11 and names SD-017 in `unblocks_claims`; run left it default-off |
| Implementation completeness | **complete** | Both the sleep passes and the SD-016 selection mechanism exist and are wired; this is a config gap, not a build gap |
| Environment adequacy | **too sparse (known)** | CausalGridWorldV2 z_world cross-context cosine 0.998; the SD-070 encoder recipe that lifts it (2.7-4.0x margin) was not applied |
| Measurement adequacy | **adequate** | First sound instrument in the lineage -- occupancy-masked, similarity and occupancy separated, null re-derived, negative control clean |
| Integration adequacy | **partially coupled** | Sleep writes and the ContextMemory readout are correctly coupled; the cue-conditioning that makes the readout differentiable is not engaged |
| Scale / capacity | **adequate** | 16 slots is not the binding constraint -- the probe fans out to 11-14 of them under adequate query variance |

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Established? | Basis |
|---|---|---|
| MECHANISM FAILED | **not_established** | Implementation reads complete-but-unarmed; the mechanism was never given the chance to fail |
| MEASURES FAILED | **not_established** | Measurement adequacy reads `adequate` -- the instrument is the one thing this run got right |
| ENVIRONMENT FAILED | **partial** | Known z_world entropy bottleneck, with a shipped recipe that was not applied |
| REE FAILED | **false** | Requires all three established; two are not |

**Net classification: MIXED -- not chargeable to REE.** Dominantly a configuration/precondition
failure with a known environment contribution.

### Recommended epistemic_category

**`standard`** for all three claims (user-adjudicated, Step 8 gate).

Rationale, stated explicitly because the alternative was live: `substrate_ceiling` would assert the
answer is gated on substrate work. It is not -- the substrate shipped 2026-08-11 and merely needs
switching on. Stamping `substrate_ceiling` would push SD-017 to a 3rd ceiling hit, **fire the
re-derive brake, refuse the very re-queue that is the correct action here**, and mark all three
not-v3-testable, starving them of experiment lanes. `standard` is behaviour-preserving and honest;
the diagnosis lives in the note fields, per the standing rule that a failure-mode diagnosis is not an
`epistemic_category`.

### Re-derive brake

**Does not fire.** Counted under the R1-R3 convention: SD-017 **2** ceiling hits
(`failure_autopsy_V3-EXQ-538a_2026-07-10` | `v3_exq_538a...`; `failure_autopsy_grandfathered-sleep-cluster_2026-08-08`
| `v3_exq_418d...`), ARC-045 **0**, MECH-166 **0**. Neither SD-017 hit is in the 436 lineage; every
436-family adjudication to date carries a `measurement_*` / `precondition_unmet` category, correctly
excluded by R3. This autopsy recommends `standard`, so it adds no hit and SD-017 remains at 2.

Independently of the count, the brake's own stated exemption applies: the substrate **is genuinely
being enriched between letters** (436c -> 436d added `gated_content_write`; 436d -> 436e added
occupancy masking, drift neutralisation and a negative control; 436e -> 436f arms SD-016 cue-slot
tagging). A same-question re-queue is therefore the intended path, not the loop the brake exists to
stop.

### Granularity-debt recurrence trigger

**Does not fire substantively.** `granularity_debt_cluster.py` reports **14 targets across 7 files**
for SD-017 and **6 targets across 6 files** each for ARC-045 and MECH-166. Alignment distribution:
`unclear` (436b, 436d batch, 538a), **`weakened`** (436c), `untested` (436d methodology-check),
`intact` (242, 436a).

The numeric precondition is met -- one target reads `weakened`, and the signatures do differ
structurally (recording gap -> write_gate payload defect -> metric confound -> occupancy /
configuration). But the substantive reading is against firing, on two grounds:

1. The single `weakened` target (436c) was **explicitly reversed** on 2026-08-07 by the methodology
   check, which found the whole DV confounded and re-scoped the lineage. Under latest-adjudication-wins,
   no live target reads `weakened`.
2. These are successive defects in **one apparatus being debugged layer by layer on one question**,
   not distinct facets of a claim that is secretly several claims. Granularity debt means the broad
   claim does not name a finer mechanism; here the claim has simply **never been tested**.

Routing `/claim-synthesis` on this cluster would inflate the believed tail on what is measurement and
configuration debt -- exactly the hazard that skill's own rails guard against.

---

## 6. Learning extracted

1. **The DV repair worked and should not be re-litigated.** All six methodology-check items landed
   and are empirically confirmed (drift z=1.67 inside a 4-sigma tolerance against a re-derived null;
   NO_WRITES arm at exactly 0 writes; waking writepath engaged at 15,428 calls). 436f inherits this
   instrument unchanged.
2. **`ContextMemory.write()`'s argmin addressing has a deterministic single-slot fixed point under a
   degenerate query stream**, with a closed-form sign discriminator (`q . (write_signal -
   memory[argmin]) < 0`) that predicted lock/rotate 5/5. This is a durable property of the write rule,
   worth knowing for every ContextMemory consumer, not only this lineage.
3. **Freezing the memory bank is NOT the cause** -- tested and refuted. Recorded so a later session
   does not re-derive it. The `requires_grad_(False)` / `sd016_diversification_weight` interaction is
   real but inert at this operating point.
4. **A substrate can be recorded as "landed and unblocking claim X" while every experiment testing X
   runs against its default-off flag.** `substrate_queue.unblocks_claims` is not mechanically
   connected to any experiment's config. 436e was queued 20 hours after SD-016 declared SD-017
   unblocked and armed none of it. Corpus-wide, 5 drivers arm the tagger and all 5 are SD-016's own.
5. **Two independent diagnostic lines converged on one substrate property**: the 2026-04-28
   attention/retrieval finding (z_world cross-batch cosine 0.998) and this run's write-occupancy
   collapse are the same degenerate-query regime seen from the read side and the write side.
6. **A P0 readiness failure is not a claim-layer result.** 436e is the third consecutive letter whose
   FAIL is upstream of the comparison; treating any of them as evidence about SD-017 / ARC-045 /
   MECH-166 would be a layer error.

---

## 7. Routing

**`/queue-experiment` -- V3-EXQ-436f** (user-confirmed at the Step 8 gate).

Same-question re-run, alphabetic suffix. The driver, conditions, seeds, training loop, DV and C1
shape are all inherited from 436e **unchanged**. The single change is to arm the SD-016 production
combination named by that substrate entry's own 2026-08-11 addendum:

```
sd016_cue_slot_tagger            = True
sd016_cue_slot_tagger_selection  = 'gumbel'
sd016_context_divergence_weight  = 0.5
```

Two properties make this the cheap and safe option: 436e already carries the
`sufficient_occupancy_for_c1` P0 gate, so if arming still fails to lift slot fan-out the run
**self-reports as a readiness failure** rather than producing a misleading scored result; and the
whole run is ~32 minutes of cloud compute.

Record in the 436f queue entry `note` that its predecessor failed on occupancy with SD-016 unarmed,
so the comparison 436f is making is legible without re-reading this artifact.

**Not routed** (and why):

- **Not `/implement-substrate`.** Nothing is owed as a build -- the mechanism exists and is on trunk.
- **Not `/lit-pull`.** The biological reference is clear and already grounded; this is not a
  formal-definition import.
- **Not `/claim-synthesis`.** See the granularity trigger above.
- **Not a governance demotion.** The demotion threshold requires the claim to have been tested
  fairly; it has not been tested at all.

### `recommended_substrate_queue_entry`

`action: amend`, `target_sd_id: SD-016` -- append a `failure_record` item recording that a claim
named in that entry's `unblocks_claims` was tested against the unarmed default one day after the
entry declared it unblocked. No `severity` / `substrate_paths` change: the SD-016 mechanism is not
defective, it was not switched on, so there is nothing for the Step 2.5c defect gate to protect other
experiments from.

### Draft `evidence_quality_note` (for governance to write -- identical text for all three claims)

> [2026-08-13 governance, V3-EXQ-436e, confirmed failure_autopsy_V3-EXQ-436e_2026-08-13, successor
> to V3-EXQ-436d]: fifth generation, and the FIRST with a sound instrument -- all six items of the
> 2026-08-07 methodology-check recommendation are implemented and empirically confirmed (occupancy-
> masked DV; similarity and occupancy reported separately; WAKING_ONLY given a real write path,
> 15,428 calls; Adam drift neutralised, NO_WRITES arm max |z| = 1.67 against a re-derived null of
> mean 1.9e-05 / sd 7.8e-03; baseline re-derived at run time). Recording standard complete, 0 dry
> runs, non_degenerate true. FAIL is at the P0 readiness layer, NOT the comparison: only 2/5 seeds
> carry >= 2 occupied ContextMemory slots (need 3), because seeds 7/13/100 occupy exactly ONE slot of
> 16 in BOTH arms despite 3,019-4,884 write() calls each -- arm-independent, therefore not an effect
> of sleep. On both seeds where the corrected DV is defined, C1 PASSES in the predicted direction
> (seed 42 0.99902 -> 0.99656; seed 200 0.96795 -> 0.83109), i.e. 2/2 directional but under-powered
> against the registered 3/5 bar. Root cause established by probe: ContextMemory.write() addresses by
> argmin(query . memory) and has a deterministic single-slot fixed point when the query stream is
> near-constant, predicted 5/5 by sign(q . (write_signal - memory[argmin])); an alternative
> hypothesis that 436e's own requires_grad_(False) freeze caused it was TESTED AND REFUTED (frozen and
> unfrozen both fan out to 11-14/16 slots under varied input). The degenerate-query regime is the
> long-registered SD-016 z_world bottleneck (cross-batch cosine 0.998, substrate_queue SD-016 entry,
> 2026-04-28), whose selection-mechanism fix LANDED 2026-08-11 (ree-v3 110a2785b6) with SD-017 named
> in its unblocks_claims -- and V3-EXQ-436e, queued 2026-08-12, armed none of it
> (sd016_cue_slot_tagger and sd016_context_divergence_weight both absent from the driver and config;
> the code IS in 436e's substrate commit 871c221933, verified by merge-base). non_contributory: the
> run is a precondition failure upstream of the comparison and weighs on the claims in NEITHER
> direction. epistemic_category standard, deliberately NOT substrate_ceiling -- the substrate is
> built and merely unarmed, so the answer is not gated on substrate work; stamping ceiling would fire
> the re-derive brake against the re-queue that is the correct action. pending_retest_after_substrate
> stays true, re-scoped from "after-DV-repair" to "after-SD-016-armed": V3-EXQ-436f is owed, identical
> to 436e but with sd016_cue_slot_tagger=True / selection='gumbel' /
> sd016_context_divergence_weight=0.5. Supersedes the 436c/436d weakens readings, which the 2026-08-07
> methodology check had already retired -- NOTHING in this lineage currently constitutes evidence
> against SD-017/ARC-045/MECH-166. PROMOTES/DEMOTES NOTHING this cycle.

---

## 8. Notes for the next session

- **`pending_retest_after_substrate` should stay `true`** on all three claims, re-scoped a second
  time: "after-substrate" (pre-2026-08-07) -> "after-DV-repair" (2026-08-07) -> **"after-SD-016-armed"**
  (2026-08-13). The task brief that opened this session described the blocker as the
  `sleep_substrate:GAP-2` closure node; that framing has been stale since 2026-08-07 and the closure
  node's own note has not tracked the re-scoping.
- **The V3-EXQ-436f chip is NOT spawned by this session**, per the standing rule that an autopsy does
  not chip follow-on its own recommendation names before `/governance` ratifies the routing. It is
  recorded here and in the session's closing report for governance to chip.
- **Corpus default-off exposure is recorded, not chipped** (user decision at the Step 8 gate): 5
  drivers arm `sd016_cue_slot_tagger`, all in SD-016's own lineage; MECH-150/151/152, ARC-041 and
  INV-040 are also named in that entry's `unblocks_claims` and may be in the same position.
