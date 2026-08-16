# Failure autopsy -- V3-EXQ-436f + V3-EXQ-603u ("precondition/headroom unmet blocks the discrimination")

**Generated:** 2026-08-16T18:24:28Z
**Scope:** cluster (2 targets)
**Status:** `awaiting_human_confirmation` -- STAGING MODE. Steps 1-7 and 9 were run in
full; Step 8 (the interactive scientific-judgment gate) was NOT run because this session
has no user. Routing below is DRAFTED, not finalised. Step 9b was drafted only: nothing
was written to `hypothesis_space_registry.v1.json` or any `hypothesis_space_*` sibling;
the intended pre-registration/resolution is recorded under `hypothesis_space_ledger_pending`
in the companion JSON.

**Companion:** `failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16.json`

---

## 0. Gates run before any metric was read

| Gate | Result |
|---|---|
| Already-done check (by CONTENT, over `targets[].run_id` in every `failure_autopsy_*.json`) | 0 artifacts cover either run. Not a filename glob. |
| `check_dry_run_citations.py` (both run_ids) | **0 dry cited, 0 dry in named families, 0 ambiguous, 2 clean, 0 unknown**, exit 0. Neither target is a smoke; no dry run is cited anywhere in this artifact and no population statistic here includes one. |
| `validate_recording.py --paths <both manifests>` | **2 complete, 0 always-core gaps, 0 thin-pack provenance drops, 0 schema warnings.** `substrate_hash`, `config`, `seeds`, `machine`/`machine_class`, `elapsed_seconds`, `recording_schema: rec/v1` all present on both. **No recording gap on either target** -- the adjudication is not blocked by a missing readout. |
| `granularity_debt_cluster.py` | SD-017, ARC-045, MECH-166, MECH-357 -- see Section 7. |
| Re-derive brake, R1-R3 convention | See Section 6. |

Both targets ran to completion (`outcome: FAIL`, no traceback, full manifests). Neither
belongs to `/diagnose-errors`.

---

## 1. Facts -- Target 1: V3-EXQ-436f

`v3_exq_436f_sd017_mech166_sd016_armed_retest_20260814T194313Z_v3`
FAIL | `experiment_purpose: evidence` | `claim_ids: [SD-017, ARC-045, MECH-166]` |
`supersedes: V3-EXQ-436e` | `ree-cloud-4`, `linux-x86_64-py3.10-torch2.12.0+cpu` |
1328.5 s (~22 min) | seeds `[42, 7, 13, 100, 200]` |
`substrate_hash bcfa771e5682...` | `evidence_direction: non_contributory` (self-stamped) |
`non_degenerate: true`, `degeneracy_reason: ""` | self-route label
`insufficient_occupancy_for_c1`.

**Design.** Sixth generation of the 436 lineage. Sole manipulation is sleep
(`SWS_THEN_REM` vs `WAKING_ONLY`, plus a `NO_WRITES` calibration arm). Inherits 436e's
repaired instrument unchanged (occupied-slots-only `slot_cosine_sim`, tracking
`ContextMemory.write()`'s own `min_idx`; similarity and occupancy reported separately;
untouched-bank null re-derived at run time). The single change vs 436e is that the
SD-016 production combination is **armed** -- `sd016_enabled=True`,
`sd016_cue_slot_tagger=True`, `sd016_cue_slot_tagger_selection='gumbel'`,
`sd016_context_divergence_weight=0.5`, plus V3-EXQ-922's ctxdiv training-loop wiring --
held constant across all three conditions. A sixth P0 gate (`sd016_arming_engaged`) was
added specifically so an inert arming would self-report distinctly from an occupancy
collapse.

**P0 gate: 5 of 6 checks MET, one UNMET.**

| P0 check | measured | floor/tolerance | met |
|---|---|---|---|
| `sws_context_memory_writes_occur` | 800 | > 1 | yes |
| `rem_attribution_rollouts_occur` | 600 | > 1 | yes |
| `waking_writepath_engaged` | 15,078 | > 1 | yes |
| `adam_drift_neutralized` (max abs z, NO_WRITES arm) | 1.6696 | < 4.0 sigma | yes |
| **`sd016_arming_engaged`** (pooled applied ctxdiv loss) | **25,796.28** | > 1e-9 | **yes** |
| **`sufficient_occupancy_for_c1`** (seeds with >= 2 occupied slots in BOTH arms) | **2.0** | **>= 3.0** | **NO** |

**Occupancy, per seed (of 16 slots).** This is the whole finding:

| seed | WAKING_ONLY occupied | SWS_THEN_REM occupied | C1 scoreable |
|---|---|---|---|
| 42 | 11 | 10 | yes |
| 7 | **1** | **1** | no |
| 13 | **1** | **1** | no |
| 100 | **1** | **1** | no |
| 200 | 14 | 15 | yes |

Identical to 436e: the same 3 of 5 seeds collapse to exactly one occupied slot in BOTH
arms, i.e. arm-independent and therefore not an effect of sleep. **Arming the SD-016
read-path fix moved write-path occupancy by exactly zero seeds** (2/5 in 436e, 2/5 in
436f), while the arming demonstrably engaged (pooled applied ctxdiv loss 25,796, floor
1e-9).

**Which criterion failed.** A **readiness precondition**, not the discrimination and not
a negative control. C1 (`n_seeds_passed: 1`, required 3) is explicitly `scored: false`;
C4 (ARC-045 slot separation, 4/5 pass, non-gating) is also `scored: false`. Neither is
evidence in either direction.

**A caution that materially revises the 436e read.** On the 2 seeds where the DV is
defined, C1 now passes **1 of 2** (seed 42: 0.99809 -> 0.99697, passes; seed 200: 0.95391
-> 0.98744, **fails -- the sleep arm is now HIGHER**). 436e reported 2/2 in the predicted
direction on the same two seeds and that "2/2 directional" was cited in its autopsy as an
encouraging under-powered signal. A single configuration change flipped seed 200. **The
2-seed directional read is not stable and must not be carried forward as partial
support.**

**Recording provenance note (not a blocker).** `substrate_stable_across_run: false`, from
one `process_snapshot_drift` record: the substrate hash was resolved at 19:22:33Z and the
on-disk tree differed at manifest-write time (19:43:13Z, lag 1240 s). But
`per_cell_hashes_disagree: false` with exactly **one** distinct cell substrate hash, so
the run itself executed against a single, identified substrate. The drift is post-run disk
movement (a concurrent pull on the worker), not intra-run substrate change. Record it;
do not treat it as invalidating.

---

## 2. Facts -- Target 2: V3-EXQ-603u

`v3_exq_603u_instrumental_avoidance_agent_pursuit_20260815T020607Z_v3`
FAIL | `experiment_purpose: evidence` | `claim_ids: [MECH-357]` | `supersedes: null`,
`predecessor_queue_id: V3-EXQ-603s` | `ree-worker-1` (hub),
`linux-x86_64-py3.10-torch2.12.0+cpu` | **69,133 s (19.2 h)** | seeds `[42, 43, 44]`,
3 arms | `substrate_hash dcab912f6cbe...` | `evidence_direction: non_contributory`
(self-stamped) | self-route label `pressure_insufficient_lesion_ceiling_requeue`.

**Design.** The sixth and (per its own docstring) final pressure-mechanism candidate for
the MECH-357 Stage-H readiness test. `603u = 603s + directedness`: keeps 603s's
mobile-predator drift (`env_drift_interval=1`, `env_drift_prob=0.6`) and adds
`hazard_agent_pursuit=0.9` as the single isolated change, so a drifting hazard moves
toward the agent's current cell 90% of the time. Three arms -- `ARM_LESION` (PAG on, no
gate; negative control), `ARM_INTACT` (gate on), `ARM_POSCTRL` (gate on + reef spawn;
positive control) -- with a **two-sided discriminative-headroom guard**: LESION must FAIL
the survival gate (headroom from below) and POSCTRL must CLEAR it (survivability exists).

**Readiness: 4 of 5 checks MET, one UNMET.**

| Readiness check | measured | floor | met |
|---|---|---|---|
| `pavlovian_freeze_reaction_present_on_lesion` | 1.0 | >= 0.667 | yes |
| `ilpfc_gate_engages_and_suppresses_freeze_on_intact` | 1.0 | >= 0.667 | yes |
| `stage0_forced_feed_lights_zgoal_on_intact` | 0.667 | >= 0.667 | yes (exactly at floor) |
| **`discriminative_headroom_below_lesion_fails_gate`** (= 1 - G_H_LESION_frac) | **0.0** | **>= 0.3333** | **NO** |
| `survivability_exists_above_posctrl_clears_gate` | 1.0 | >= 0.667 | yes |

**Criteria.** `G_H_INTACT_clears_2of3` (load-bearing, absolute) **PASSED**
(`g_h_intact_frac = 1.0`). `G_H_INTACT_beats_LESION` (load-bearing, discrimination)
**FAILED** -- because `g_h_lesion_frac = 1.0` as well. `g_h_posctrl_frac = 1.0`.
**All three arms are at the ceiling.**

**The ceiling is the maximum, not merely a high value.** `hazard_stage_median_last_window`
(median episode length over the last 10 of 40 Stage-H episodes; gate is >= 75) reads
**exactly 200.0 in 7 of 9 arm-seeds**, which is the episode-length cap -- the two
exceptions are 103 and 102, both still clearing the 75 floor. The per-episode trajectories
are strongly **bimodal**: episode lengths are either exactly 200 (survived to cap) or 3-6
(died almost immediately), with little mass between. A median-over-10 against a 75-step
floor on a bimodal 200-capped distribution therefore discards nearly all the available
information and saturates at 1.0 for every arm.

**A SECOND, INDEPENDENT vacuity that the manifest records but the self-route does not
name.** The learned `mech357_avoidance_efficacy` has underflowed to numerical zero by the
scoring window on every gated seed:

| arm / seed | final `avoidance_efficacy` | `n_credit` | `n_decay` | decay:credit |
|---|---|---|---|---|
| INTACT 42 | 5.71e-120 | 405 | 34,761 | 86:1 |
| INTACT 43 | 4.58e-118 | 170 | 31,943 | 188:1 |
| INTACT 44 | 2.12e-123 | 285 | 34,209 | 120:1 |
| POSCTRL 42 | 3.96e-111 | 482 | 33,765 | 70:1 |
| POSCTRL 43 | 5.13e-111 | 208 | 31,031 | 149:1 |
| POSCTRL 44 | 6.50e-125 | 359 | 35,143 | 98:1 |

The `avoidance_efficacy_trajectory` shows the trace healthy early (0.07-0.79 in episodes
0-5) and below 1e-17 by episodes 36-39. `mech357_scaffold_floor` anneals 0.8 -> **0.0**,
and the gate consumes `max(avoidance_efficacy, scaffold_floor)` -- so once the scaffold
has annealed away, the effective efficacy is ~1e-120. Consistently,
`n_freeze_suppressed` **saturates** part-way through (INTACT seed 42: 202 at episode 36
and 202 at the end -- no further suppression events at all in the final episodes).

**So the INTACT arm is functionally lesioned inside the very window the DV measures.**
The two `readiness` checks that certify the gate (`gate_engaged`, `gate_suppresses`) are
computed over the whole run and read 1.0 on the strength of the early, scaffold-supported
episodes; they cannot see the late-window extinction. This is the "evidence that LOOKS
valid but isn't" shape.

The two vacuities are genuinely independent: the LESION arm has no gate at all, so its
ceiling at 1.0 is unaffected by the efficacy underflow. Each on its own is sufficient to
make the INTACT-vs-LESION comparison uninformative.

**Recording provenance note (not a blocker).** Same shape as 436f -- one
`process_snapshot_drift` record, recorded hash != on-disk at stamp,
`per_cell_hashes_disagree: false`. `z_goal_stream` is healthy (`active_frac` 0.99997,
`writer_defect: false`).

**Incidental datum worth recording:** `g1_transfer_intact_frac = 0.667` vs
`g1_transfer_lesion_frac = 1.0` -- the gated arm did marginally *worse* on the P1 transfer
leg. With n=3 and an extinct gate this is not interpretable; it is recorded so a later
session does not rediscover it as a surprise.

---

## 3. Claim-layer map -- did the experiment let the claim express itself?

| Claim | type | status | epistemic_category (stored) | `pending_retest_after_substrate` | Did this run test it? |
|---|---|---|---|---|---|
| SD-017 | design_decision | stable | `standard` | true | **No.** P0 readiness failure upstream of C1. |
| ARC-045 | architectural_commitment | candidate | `standard` | true | **No.** Same C1 gate. (C4 slot separation passed 4/5 but is explicitly non-gating and `scored: false`.) |
| MECH-166 | mechanism_hypothesis | candidate | `standard` | true | **No.** Same C1 gate. |
| MECH-357 | mechanism_hypothesis | candidate, `v3_pending` | `standard` | true | **No.** Readiness precondition R4 unmet; and the gate was numerically extinct in the scoring window. |

`live_status.evidence.from` on all three 436-lineage claims currently cites
`failure_autopsy_V3-EXQ-436e_2026-08-13`; MECH-357's cites
`failure_autopsy_V3-EXQ-603t_2026-08-13`. Claim tagging on both targets is **accurate** --
these are not inherited-without-re-evaluation tags; C1 is the pre-registered joint test of
all three 436 claims, and MECH-357 is the sole claim 603u tests.

**Neither target is a demotion candidate.** The Step 7 demotion threshold requires the
claim to have been tested fairly. In both cases the driver's own pre-registered guard
refused to score the comparison.

### A conditionally-stamped `epistemic_category` whose re-check trigger has now fired

Per the Step 5 rule ("check whether a claim's CURRENT stored `epistemic_category` is
itself conditional on this run"), the 436e autopsy stamped `standard` on all three 436
claims with an **explicit stated condition**, quoted verbatim from its
`recommended_epistemic_category_note`:

> "Deliberately NOT `substrate_ceiling` [...] `substrate_ceiling` asserts the claim's
> answer is gated on substrate work; here the substrate shipped 2026-08-11 and merely
> needs switching on."

**V3-EXQ-436f is the run that tests that condition, and the condition is falsified.** The
substrate that shipped 2026-08-11 (`ree-v3 110a2785b6`) is the SD-016 **read**-path
mechanism -- a cue-slot tagger MLP on `z_world` plus a context-divergence auxiliary loss.
436f armed it in full, the arming engaged (25,796 pooled applied loss), and write-path
occupancy did not move by one seed. The **write** path -- `ContextMemory.write()` in
`ree_core/predictors/e1_deep.py:135-147` -- is untouched by any of it and has no
non-degenerate selection mechanism at all. The 436e caveat therefore no longer holds and
the reading flips (Section 5).

---

## 4. Biological-reference triage

**436f (SD-017 / ARC-045 / MECH-166).** Closest reference: SWS hippocampus-to-neocortex
schema installation followed by REM-direction attribution filling (Diekelmann & Born 2010;
Sanders / Wilson / Gershman 2020 hidden-state prior). **Not a formal-definition import**;
lit status `present`; **no `/lit-pull` is owed.** Dependencies of the reference mechanism:
cue-distinguishable context representations, a write path that addresses distinct
substrates for distinct contexts, and offline replay passes. The failure matches a
**missing-dependency signature** precisely: in real cortex, pattern separation upstream of
the write is what makes distinct experiences land in distinct substrates -- the dentate
gyrus / CA3 separation stage exists exactly so that a near-identical input stream does not
collapse onto one engram. REE has the replay passes and the bank; it has no separation
stage on the write address. The FAIL is therefore a **discovered prerequisite**, and is
weak positive evidence for the dependency itself, not evidence against the sleep claims.

Concretely, the asymmetry is visible in one file. `ContextMemory.read()` addresses by
**softmax** over `query_proj(query) @ key_proj(memory).T` -- soft, distributed. But
`ContextMemory.write()` addresses by a hard `scores.mean(0).argmin()`, which under a
low-variance query stream is a **deterministic single-slot fixed point** (established by
the 436e autopsy with a closed-form sign discriminator `q . (write_signal -
memory[argmin])` that predicted lock-vs-rotate 5/5). Every SD-016 remedy shipped so far --
the Gumbel selection confirmed by V3-EXQ-908, the ctxdiv loss confirmed by V3-EXQ-907 --
lives on the read side or on a separate tagger. The write side never got the treatment.

**603u (MECH-357).** Closest reference: infralimbic PFC suppression of PAG-mediated
Pavlovian freezing to permit instrumental active avoidance (Moscarello & LeDoux 2013),
with an eligibility-trace efficacy learner as the acquisition mechanism. **Not a
formal-definition import**; lit status `present`; **no `/lit-pull` is owed.** The
paradigm's own precondition is a genuine **Pavlovian-instrumental conflict** -- freezing
must be *costly*. In a shuttle box the animal that freezes is shocked. In 603u's Stage-H
the ungated LESION animal survives to the episode cap in 3/3 seeds under four pursuing
hazards drifting every step at p=0.6 with pursuit 0.9. There is no conflict, so there is
nothing for the ilPFC analogue to arbitrate. This is an **environment/pressure**
divergence from the reference paradigm, not a translation-fidelity divergence in the
mechanism.

The efficacy-underflow half has its own biological reading, and it is the one that matters
for the fix: standard extinction theory requires an unreinforced **emission** of the
response to weaken it, not its mere non-occurrence. Charging decay on every freeze/no-op
tick -- which under sustained threat vastly outnumber directed attempts -- is not
extinction, it is a tick-count artefact. That is a genuine biology-to-implementation
divergence and it is **load-bearing**, which is why it is worth stating even though the
repair is already in flight (Section 8).

---

## 5. Four-layer diagnosis

### Target 1 -- V3-EXQ-436f

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **untested** | P0 readiness failure upstream of C1. Weighs on SD-017 / ARC-045 / MECH-166 in NEITHER direction. |
| Biological reference | **clear** | SWS schema installation + REM attribution. Not a formal import; lit present. Failure matches a missing pattern-separation dependency. |
| Prerequisites | **missing** | A non-degenerate write-address selection does not exist. SD-016's landed remedies are all read-side. This is now a BUILD gap, not (as at 436e) a configuration gap. |
| Implementation | **partial** | `read()` is soft/softmax; `write()` is a hard `argmin` with a deterministic fixed point. Symbol of the mechanism (a 16-slot bank, 3,000-4,900 write calls/arm) without its functional role (1 occupied slot). |
| Environment | **too sparse (known)** | z_world cross-context cosine 0.998, on the SD-016 substrate_queue entry since 2026-04-28. Not remedied here. |
| Measurement | **adequate** | 436e's repaired instrument, re-confirmed: occupancy-masked DV tracking write()'s own `min_idx`, similarity/occupancy reported separately, null re-derived at run time (n=500), NO_WRITES negative control at max abs z = 1.67 against a 4.0-sigma tolerance. The instrument is the one thing this lineage has now firmly got right. |
| Integration | **partially coupled** | Sleep writes and the ContextMemory readout are correctly coupled. The SD-016 cue conditioning is coupled to the read path only -- exactly as the driver's own docstring caveat predicted. |
| Scale / capacity | **adequate** | 16 slots is not the binding constraint; the path fans out to 10-15 of them on the two seeds with adequate query variance. |

**Failure-location summary (GOV-FAILLOC-1): MIXED -- MECHANISM + ENVIRONMENT. NOT
chargeable to REE.** Implementation reads `partial` and Environment reads `too sparse`;
only Measurement reads `adequate`. Two of the three required buckets are not adequate, so
`ree: false`. This is not a case where REE was given a fair chance and failed; the
comparison was never computable on 3 of 5 seeds.

### Target 2 -- V3-EXQ-603u

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **untested** | Readiness R4 unmet; and the gate is numerically extinct in the scoring window. MECH-357 is neither confirmed nor falsified. |
| Biological reference | **clear** | Moscarello & LeDoux 2013 active avoidance. Not a formal import; lit present. |
| Prerequisites | **present** | PAG freeze (MECH-279) commits 152-198 times/seed; the SD-059/MECH-358 escape bridge and the harm-pathway training amend are both on for every arm and were separately validated (603q, re-confirmed 866b). |
| Implementation | **partial** | The gate is built, wires up, engages and suppresses. But its eligibility trace decays ~86-188x more often than it credits and underflows to ~1e-120 by mid-Stage-H, so the mechanism is *present at the start and absent at the measurement*. |
| Environment | **wrong pressures** | Four hazards drifting every step at p=0.6 with pursuit 0.9 leave the UNGATED control surviving to the 200-step cap in 3/3 seeds. The pressure does not create the Pavlovian-instrumental conflict the paradigm requires. |
| Measurement | **misleading** | `median(last 10 episode lengths) >= 75` against a 200-step cap over a strongly bimodal (200 or 3-6) distribution. Saturates at 1.0 for all three arms and destroys the graded information that is actually in the data. |
| Integration | **coupled but unstable** | Gate, PAG, escape bridge and harm pathway are all coupled; the scaffold-floor anneal (0.8 -> 0.0) unmasks the trace decay exactly as the scoring window opens. |
| Scale / capacity | **adequate** | 40 Stage-H episodes; 31,000-35,000 gate updates per arm-seed. Budget is not the constraint. |

**Failure-location summary (GOV-FAILLOC-1): MIXED -- MECHANISM + MEASURES + ENVIRONMENT.
NOT chargeable to REE.** All three buckets read inadequate independently. This is the
least chargeable-to-REE shape available: the mechanism was extinct, the ruler was
saturated, and the pressure was absent, all at once.

### A convention note the reader needs

`failure_location.{mechanism, measures, environment}` are recorded here under the skill's
**literal** Step 5 rule -- a bucket is `established` iff its corresponding row reads
`adequate`/`complete`, which is what makes `ree: true` ("all three established")
self-consistent. Note that the immediate predecessor artifact
(`failure_autopsy_V3-EXQ-436e_2026-08-13`) used the **inverse** convention on its
`measures` field, setting `measures: not_established` while its own prose said the
measurement row read `adequate`. Both artifacts reach the same prose verdict (MIXED, not
chargeable to REE), so nothing downstream turns on it here, but the two are not
field-comparable. **Flagged for governance as a small corpus-consistency question**
(Section 10, item 4).

---

## 6. Re-derive brake (MOVE-3), R1-R3 convention

Counted mechanically with the skill's recipe: R1 the unit is the RUN (no `break`, every
target counts, per-target fallback key); R2 latest adjudication supersedes; R3 only
`substrate_ceiling` counts, `non_contributory` alone does not; per-claim category wins
over the blanket one. `status == confirmed` only. Counts are **before** this autopsy.

| Claim | tagging targets | prior ceiling hits | prior hit artifacts |
|---|---|---|---|
| **SD-017** | 15 | **2** | `failure_autopsy_V3-EXQ-538a_2026-07-10` (run `v3_exq_538a_sd049_phase2_with_sleep_...`); `failure_autopsy_grandfathered-sleep-cluster_2026-08-08` (run `v3_exq_418d_sd016_writepath_modes_comparison_...`) |
| ARC-045 | 6 | **0** | -- |
| MECH-166 | 6 | **0** | -- |
| MECH-357 | 3 | **0** | 603r `measurement_test_design_defect`, 603s `standard`, 603t `standard` -- all correctly excluded by R3 |

### The brake FIRES on SD-017

This autopsy recommends `substrate_ceiling` for SD-017 (Section 8), making it the **3rd**
hit against `RE_DERIVE_BRAKE_THRESHOLD = 2`. Consequences, applied:

- Routing for 436f **is** `implement-substrate` on the named upstream substrate, with a
  filled `recommended_substrate_queue_entry` (`action: create`).
- **A same-claim test re-queue is REFUSED.** No V3-EXQ-436g may be queued that re-poses
  the C1 slot-differentiation question against the current `ContextMemory.write()`
  addressing -- not another read-path letter, not a seed-count bump, not a lowered
  occupancy floor. Seven generations (436, 436a-436f) have now circled this question; the
  last three failed at the same P0 occupancy gate. The exemption the 436e autopsy invoked
  ("the substrate IS genuinely being enriched between letters") no longer applies, because
  436f is precisely the letter that showed the enrichment does not reach the write path.
- A **redesign of a different mechanism** (new EXQ number, different `claim_ids`) remains
  permitted, as does a commitment-free read. The retest of C1 is permitted only **after**
  the write-path build lands.

Note the brake and the correct routing **agree** here. This is unlike 436e, where stamping
a ceiling would have refused the very re-queue that was then correct -- the reason that
autopsy chose `standard`.

### One place a human could legitimately move the SD-017 count -- flagged, not applied

Under the peripheral-co-tag rule (2026-07-21), a target whose own artifact says a claim was
peripheral or not exercised should carry `recommended_epistemic_category_per_claim` rather
than the blanket ceiling. `failure_autopsy_V3-EXQ-538a_2026-07-10` tags **five** claims
(`SD-049, SD-015, SD-017, MECH-229, MECH-230`) and its SD-017 `claim_alignment` reads
"unclear (untested)". SD-017's own `claims.yaml` note about that run is blunter still:
*"The manifest's per-claim SD-017 'supports' was SWS/REM-write liveness only -- vacuous,
NOT counted. SD-017 stays STABLE / unchanged."*

That reads like a peripheral co-tag. **This autopsy has NOT re-attributed it**, because the
binding rule is that the fix direction is the ARTIFACT and re-attribution requires the
538a artifact's own prose to say peripheral/not-exercised, and this session may not edit a
confirmed artifact. If governance judges 538a's SD-017 tag peripheral and amends that
artifact, SD-017 drops to 2 and this brake does not fire. **The routing would be unchanged
either way** -- `implement-substrate` on the write path is correct on the diagnosis alone.
Only the formal refusal of a re-queue turns on it.

### MECH-357: the brake does NOT fire, but its spirit is loudly engaged

R3 gives 0, correctly -- none of 603r/603s/603t was stamped `substrate_ceiling`, and this
autopsy recommends `standard` for MECH-357 (Section 8), so it stays 0. But the letter of
the brake should not be allowed to hide the pattern: **603u is the sixth consecutive
inconclusive Stage-H run for MECH-357** (603h, 603k, 603r, 603s, 603t, 603u), the fourth
distinct pressure design, and it cost **19.2 hours of hub compute**. The manifest's own
self-route recommends "re-calibrate UP (raise `env_drift_prob` / `num_hazards`)".

**This autopsy REJECTS that self-route on routing grounds** (the self-route is a hypothesis,
never a verdict). A seventh same-question pressure recalibration is not recommended and
should not be queued: (a) the `mech357_avoidance_efficacy_plan.md` closure node already
records that config-only pressure levers are exhausted across three designs, and 603u
exhausts the fourth and last named candidate; (b) a pressure increase cannot fix the
independent efficacy-underflow vacuity, so a 7th run would repeat a 19-hour measurement
with the INTACT arm still extinct in the scoring window; (c) the cheapest live hypothesis
(H2 below) needs **no new compute at all**.

---

## 7. Granularity-debt recurrence trigger

Counted with `granularity_debt_cluster.py` (targets whose own `claim_ids` name the claim),
not a filename grep.

**SD-017 -- does NOT fire.** 15 targets / 8 files; alignment distribution `unclear=9,
intact=2, untested=2, weakened=2`. The numeric precondition is met and a `weakened` target
exists, so the count alone would fire it -- but the structural test does not. The two
`weakened` targets are `436c` (`measurement_test_design_defect`, explicitly reversed by the
2026-08-07 methodology check, which found the whole DV confounded) and `418d`
(`substrate_ceiling`, the SD-016 write-path modes comparison -- the *same* write-path
defect this autopsy diagnoses, i.e. convergent, not a distinct facet). The differing
signatures across the 436 lineage (recording gap -> write-gate payload defect -> metric
confound -> occupancy collapse -> read-path arming insufficient) are **successive defects
in ONE apparatus being debugged layer by layer on ONE question**, not several claims
hiding inside a coarse one. Routing `/claim-synthesis` here would inflate the believed tail
on what is measurement, configuration, and now substrate debt. Same conclusion as the 436e
autopsy, reached independently.

**ARC-045 / MECH-166 -- do NOT fire.** 6 targets / 6 files each; same distribution
(`unclear=3, untested=2, intact=1, weakened=1`), the single `weakened` being the reversed
436c. Same reasoning.

**MECH-357 -- does NOT fire.** 3 targets / 3 files; alignment distribution `unclear=3`.
**NO target reads `weakened`.** Per the binding rule, a cluster in which no target reads
`weakened` is measurement or implementation debt, not granularity debt, however many
autopsies exist. This is exactly that case, and 603u makes it four.

---

## 8. Learning extracted and repair pathway

### Target 1 -- V3-EXQ-436f

**Node class: `complicated (buildable)`.** The cause is established with a closed-form
discriminator (436e) and the fix has a proven component already in the repo. There is no
open empirical question standing between here and the build, so a spike would only
re-confirm what is known.

**Learning.**

1. **The SD-016 read-path fix does not lift write-path occupancy, and this was a
   pre-registered discrimination that resolved.** The 436f driver's own INTERPRETATION GRID
   states it in advance: *"the joint reading `sd016_arming_engaged`=MET with
   `insufficient_occupancy_for_c1`=UNMET is the diagnostic signal that the read-path SD-016
   fix did not lift write-path slot occupancy -> route to a WRITE-path successor
   (query_proj / z_world entropy), not another read-path letter."* Exactly that joint
   reading occurred. **436f is therefore not a bare precondition failure -- it is a
   successful, pre-registered read/write discrimination**, and that is its contribution.
2. **The named build.** `ContextMemory.write()` (`ree_core/predictors/e1_deep.py:135-147`)
   addresses by a hard `scores.mean(0).argmin()` while `read()` (lines 124-133) addresses by
   softmax. The write side needs the same non-degenerate selection treatment the read side
   received -- the annealed Gumbel-softmax selection that **V3-EXQ-908 already CONFIRMED**
   works (3/3, genuine context-conditioned sparsification), applied to the write address; or
   an occupancy/usage-balancing term on the address so the fixed point cannot form.
   Secondary/alternative lever: raise `z_world` entropy (the SD-070 encoder recipe, 2.7-4.0x)
   so the query stream stops being near-constant. The two are complementary, not rival: the
   first makes the write robust to a degenerate query stream, the second removes the
   degeneracy. Build the first; the second is a separate, larger programme.
3. **A durable, cross-consumer substrate property.** Every ContextMemory consumer that
   writes under a low-variance query stream silently gets a 1-slot bank while `write()`
   returns normally and thousands of calls are logged. Nothing errors. This is a
   **`corrupting`** defect in the Step 2.5c sense: it produces evidence that looks valid
   (writes happened; the bank exists; the readout is well-formed) and is not.
4. **436e's "2/2 directional" partial signal did not survive one config change** (now 1/2;
   seed 200 reversed). Do not carry an n=2 directional read forward as encouragement.
5. **A substrate can be recorded as landed-and-unblocking-claim-X, be armed in full, and
   still not reach the failing path.** 436e's learning was "unblocks_claims is not
   mechanically connected to any experiment's config". 436f sharpens it: **it is not
   mechanically connected to the failing MECHANISM either.** SD-016's addendum named SD-017
   unblocked; the remedy is read-side; the block is write-side.

**Routing: `implement-substrate`.** `recommended_substrate_queue_entry.action = create`
(new entry `contextmemory-write-path-addressing-degeneracy`; SD-016's own entry is
`implemented` and scoped to cue-indexed *retrieval*, so this is its write-side sibling
rather than an amend). Full fields in the companion JSON, including
`severity: corrupting` and `substrate_paths: ["ree_core/predictors/e1_deep.py"]`.

**Not routed:** `/lit-pull` (biology clear, not a formal import); `/queue-experiment`
(refused by the fired brake for the same question; permitted only after the build);
`/claim-synthesis` (Section 7); `governance-demotion` (the claims have not been tested at
all).

### Target 2 -- V3-EXQ-603u

**Node class: mixed.** The gating build is `complicated (buildable)` **and already in
flight**. The live scientific question is a `complex (probe-gated)` discrimination, of
which the most promising leg is `mystery (known data)` -- the data already exists and the
frame is wrong.

**Learning.**

1. **Agent-directed hazard pursuit does NOT produce discriminative headroom.** This
   discharges, with a negative answer, the probe-gated question the substrate_queue entry
   `mech357-freeze-incompatible-pressure-mechanism` and the
   `mech357_avoidance_efficacy:BUILD` closure node were opened to ask. Its status
   (`implemented_pending_validation`) is now stale: it is validated, and the answer is no.
   All four named pressure designs -- static field, undirected mobile drift, scheduled
   discrete adjacency, agent-directed pursuit -- are now exhausted.
2. **The DV saturates and is the strongest remaining suspect.** 7 of 9 arm-seeds sit at
   exactly the 200-step cap on a bimodal distribution, measured through a median-of-10
   against a 75-step floor. The design has been asking a saturated binary of a graded
   phenomenon for six runs. **The 603s / 603t / 603u per-episode trajectories are already
   recorded** -- a graded re-read (mean episode length, survival fraction, time-to-first-
   death, hazard-contact rate) costs zero compute and can say whether a discrimination was
   present all along.
3. **The eligibility trace underflows to ~1e-120 by the scoring window, so the INTACT arm
   was functionally lesioned when it was measured.** Quantified here for the first time
   (decay:credit 70:1 to 188:1; `n_freeze_suppressed` saturating mid-run; scaffold floor
   annealing 0.8 -> 0.0 to unmask it). The `gate_engaged` / `gate_suppresses` readiness
   checks are whole-run aggregates and **cannot see** this -- they read 1.0 on the strength
   of the early scaffold-supported episodes. **Any readiness check certifying a mechanism is
   live must be evaluated over the SCORING WINDOW, not the whole run.** That is a
   generalisable methodological lesson beyond MECH-357.
4. **The biology names the fix, and the fix has already landed today.** Charging decay on
   freeze/no-op ticks is not extinction (which requires an unreinforced emission). The
   working tree of `ree-v3/ree_core/pfc/infralimbic_avoidance_gate.py` already carries an
   uncommitted change dated **2026-08-16** -- "MECH-357 credit-eligibility windowing: a
   freeze/no-op tick does not decay `avoidance_efficacy`" -- with a new `_n_freeze_noop`
   counter, authored by the session holding the active claim
   `closure-maps-correctness-807268`.

**IN-FLIGHT WORK -- DO NOT DUPLICATE.** The active TASK_CLAIMS entry
`closure-maps-correctness-807268` ("implement-substrate: MECH-357 avoidance-efficacy
eligibility trace") holds `ree-v3/ree_core/pfc/infralimbic_avoidance_gate.py`, and its
change is present and uncommitted in the shared tree. This autopsy read that file but
**did not touch it**, and **recommends no build against it**. What this autopsy contributes
instead is the empirical failure record that entry has been missing: the substrate_queue
item `mech357-avoidance-efficacy-eligibility-trace-imbalance` (added 2026-08-14T06:55:01Z,
`pending_implementation`) currently carries **`failure_record: []`** -- zero entries. 603u
supplies the first, with numbers.

**Routing: `implement-substrate`** -- because the blocking node is that eligibility-trace
build, which must land before any MECH-357 retest is non-vacuous. But the routing note is
explicit that the build is already in flight and that this autopsy's own new work is
(a) the two substrate_queue amends and (b) the zero-compute H2 reanalysis in the
`fanout_recommendation`.

`recommended_substrate_queue_entry.action = amend`, primary target
`mech357-freeze-incompatible-pressure-mechanism` (status correction + 4th failure record),
with an `additional_amend_entries` block for
`mech357-avoidance-efficacy-eligibility-trace-imbalance` (first failure record + a proposed
`severity` upgrade `degrading -> corrupting`).

**GOV-FANOUT-1 applies to 603u.** The remaining question is a genuine discrimination among
three live hypotheses, not one named build, and routing a single sequential re-pose would
inherit the same confound for a seventh time. The portfolio (each leg on a different design
axis, each with a declared null) is in the companion JSON:

| H | axis | probe sketch | declared null |
|---|---|---|---|
| H1 pressure genuinely insufficient in MAGNITUDE (mechanism exhausted, only scale left) | world | short titration sweep over `num_hazards` / `proximity_harm_scale` on the LESION arm ONLY, scoring a GRADED survival DV; find whether any operating point yields `G_H_LESION < 2/3` while POSCTRL still clears | no operating point yields two-sided headroom -> the Stage-H env cannot host this paradigm; redesign the test bed, do not re-tune it |
| **H2 the DV saturates and destroys a discrimination that is already present** | measurement | **reanalysis only, ZERO new compute** -- re-read the recorded 603s/603t/603u per-episode trajectories with a graded DV (mean episode length, survival fraction, time-to-first-death, hazard-contact rate) | graded DVs also show INTACT ~= LESION -> the ceiling was not the obstruction, and H1/H3 carry the weight |
| H3 the gate is numerically extinct in the scoring window, so INTACT == LESION regardless of pressure | instrumentation | after the in-flight credit-eligibility windowing fix lands, re-run 603u UNCHANGED and check `avoidance_efficacy` in the last 10 episodes plus a scoring-window-scoped `gate_live` readiness check | efficacy still underflows post-fix -> the imbalance is not the freeze-tick accounting and needs its own diagnosis |

**Run H2 first.** It is free, it is `mystery (known data)`, and its result determines
whether H1 is worth 19 hours at all.

**Not routed:** `/lit-pull` (biology clear and already grounded; the extinction-theory
point is a divergence *recorded as load-bearing*, not a literature gap);
`/queue-experiment` for a 7th pressure recalibration (refused, Section 6);
`/claim-synthesis` (Section 7); `governance-demotion` (never fairly tested).

---

## 9. Cluster pattern -- testing the parent session's grouping

The two targets were grouped on a shared surface fingerprint: *an absolute/readiness
criterion passes while the DISCRIMINATION criterion fails, with an unmet occupancy/headroom
precondition as the proximate cause.* Testing that grouping, as instructed:

| Experiment | Claim | Absolute / negative-control criterion | Discrimination criterion | Read |
|---|---|---|---|---|
| V3-EXQ-436f | SD-017, ARC-045, MECH-166 | P0: 5 of 6 gates MET (writes 800, rollouts 600, waking 15,078, drift z 1.67 < 4.0, ctxdiv 25,796 > 0) | C1 `slot_cosine_sim_occupied_only` -- **never computed** on 3/5 seeds; `scored: false` | Independent variable is **degenerate**: 1 occupied slot of 16 in both arms. No variance to compare. |
| V3-EXQ-603u | MECH-357 | `G_H_INTACT_clears_2of3` PASSED (1.0); PAG freeze 1.0; gate engages+suppresses 1.0; POSCTRL 1.0 | `G_H_INTACT_beats_LESION` -- computed and **FAILED** because LESION also = 1.0 | Dependent variable is **saturated** at its maximum. No dynamic range to discriminate in. |

**Verdict: the parent's grouping is PARTLY confirmed. These are TWO INDEPENDENT BUGS at
the proximate-cause layer, sitting at OPPOSITE ends of the measurement pipeline, over ONE
shared structural property at the substrate layer.**

- **The proximate causes are different layers and must not be conflated.** 436f's
  occupancy shortfall is a collapse of the *independent variable* -- the manipulation had
  nothing to act on, and the discrimination statistic was mathematically undefined on 3/5
  seeds. 603u's headroom shortfall is a saturation of the *dependent variable* -- the
  manipulation may well have acted, and the statistic was computed, but the ruler had no
  range left. One is "nothing to measure"; the other is "the ruler is pegged". A fix for
  either does nothing for the other.
- **The skill's substrate-ceiling fingerprint ("negative control passes, discrimination
  fails") applies cleanly to 603u only.** It does NOT apply to 436f, where the
  discrimination was never *computable*, not computed-and-null. Reading 436f through that
  fingerprint would misdescribe it.
- **The shared structural property, stated as narrowly as the evidence supports:** in both
  cases the REE substrate instantiates the mechanism's STRUCTURE while failing to sustain
  the DYNAMIC RANGE the mechanism's readout requires. ContextMemory has 16 slots and 3,000-
  4,900 write calls per arm and occupies 1. The ilPFC gate logs 31,000-35,000 updates and
  405 credit events and holds an efficacy of 1e-120. Both pass every liveness/engagement
  check that counts *events*; both are functionally absent on the quantity that matters.
  This is "symbol of the mechanism, not its functional role" specifically at the level of
  **magnitude**, and it is invisible to any readiness check built from counters.
- **A second, positive shared property worth recording.** Both drivers carried a
  pre-registered two-sided guard (436f: `sd016_arming_engaged` vs
  `sufficient_occupancy_for_c1`; 603u: LESION-below plus POSCTRL-above), and in both cases
  the guard fired correctly and **refused to score a vacuous comparison** rather than
  emitting a false claim-layer verdict. Both FAILs are informative refusals. This is a
  methodological maturity signal in the lineages, and it is the reason both runs are
  `non_contributory` rather than spurious `weakens`.
- **The planning decision this forces:** do not treat these as one gap with one fix. They
  need two independent builds with no shared component -- a write-address selection
  mechanism in `e1_deep.py`, and an eligibility-trace credit/decay rebalance in
  `infralimbic_avoidance_gate.py` (already in flight). The one thing they *do* share is a
  cheap, generalisable methodological repair: **liveness/engagement preconditions must be
  evaluated over the scoring window and on magnitudes, not as whole-run event counts.**
  Both runs would have self-reported their true state one gate earlier had they done so.

---

## 10. What must go to the human at the Step 8 confirmation gate

1. **436f: flip SD-017 / ARC-045 / MECH-166 from `standard` to `substrate_ceiling`?** This
   is the load-bearing judgment. FOR: 436e's `standard` was stamped on the explicit,
   now-falsified condition that the substrate "shipped and merely needs switching on"; the
   write path is genuinely unbuilt, so the claims' answer *is* gated on substrate work.
   AGAINST: it moves all three claims out of the v3-testable pool
   (`_claim_v3_testable`) and into `_EPI_SUPPRESS_PROPOSAL`, and the run is still formally
   a precondition failure, the family the skill maps to `standard` by default. The
   recommendation is `substrate_ceiling`; the consequence is real and should be accepted
   knowingly.
2. **The SD-017 re-derive brake fires at 3 and REFUSES a V3-EXQ-436g same-question
   re-queue.** Confirm the refusal. Note the routing is `implement-substrate` regardless of
   whether the brake fires.
3. **Should `failure_autopsy_V3-EXQ-538a_2026-07-10`'s SD-017 tag be re-attributed as
   peripheral?** SD-017's own `claims.yaml` note calls that run's SD-017 support "vacuous,
   NOT counted". If governance amends that artifact with
   `recommended_epistemic_category_per_claim`, SD-017 drops to 2 and the brake does not
   fire. Not applied here -- a confirmed artifact may not be edited by this session.
4. **`failure_location` convention drift.** This artifact uses the skill's literal rule
   (`established` iff the row reads adequate/complete); `failure_autopsy_V3-EXQ-436e` used
   the inverse on `measures`. Worth one governance decision so the corpus is
   field-comparable.
5. **603u: upgrade `mech357-avoidance-efficacy-eligibility-trace-imbalance` from
   `severity: degrading` to `corrupting`?** Justification: the defect produced a run in
   which every readiness check certified the gate as live while the gate was extinct in the
   scoring window -- evidence that looks valid and is not. Consequence: `/queue-experiment`
   Step 2.5c would then BLOCK new unrelated experiments touching
   `ree-v3/ree_core/pfc/infralimbic_avoidance_gate.py` until it closes. The fix is in
   flight, so the block should be short-lived, but it is a real gate and the human should
   decide.
6. **603u: this autopsy REJECTS the manifest's own self-route** ("re-calibrate UP"). No 7th
   pressure recalibration. Confirm, and confirm that H2 (zero-compute reanalysis) runs
   before any new Stage-H compute is spent.
7. **Nothing is chipped from this session** (`/failure-autopsy` does not `spawn_task` its
   own not-yet-ratified routing; and this is a staging run under the parent's claim).
   `/governance` chips the follow-on after Step 2b ratifies it -- and must first check
   `igw_routine_ledger.json` / `igw_assignments.json`, and the open chip
   `chip-20260813-implsub-mech357-hazard-pursuit`, so it does not duplicate work already
   staged or in flight.

---

## 11. Draft `evidence_quality_note` text (for governance to write -- NOT written here)

**SD-017 / ARC-045 / MECH-166** (append, identical text to all three):

> [2026-08-16 governance, V3-EXQ-436f, failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16, successor to V3-EXQ-436e]: sixth generation. The 436e instrument is re-confirmed sound (P0 5/6 gates MET: SWS writes 800, REM rollouts 600, waking writepath 15,078 calls, NO_WRITES Adam-drift max |z| = 1.67 against a 4.0-sigma tolerance on a run-time-derived null). Recording standard complete, 0 dry runs, non_degenerate true. The single change vs 436e -- arming the full SD-016 production combination (cue_slot_tagger + gumbel selection + context_divergence_weight 0.5 + 922's ctxdiv training-loop wiring) -- ENGAGED, confirmed by the new sd016_arming_engaged gate (pooled applied ctxdiv loss 25,796 against a 1e-9 floor), and moved write-path slot occupancy by EXACTLY ZERO seeds: 2/5 scoreable in 436e, 2/5 in 436f, with the same seeds 7/13/100 occupying exactly 1 of 16 slots in BOTH arms despite 2,837-4,903 write() calls each. C1 was therefore never computed on 3/5 seeds and is scored:false; C4 (4/5) is non-gating and also scored:false. This is the joint reading the 436f driver PRE-REGISTERED in its own interpretation grid as the signal to route to a WRITE-path successor -- so 436f is a successful read/write discrimination, not a bare precondition failure. Root cause (established at 436e by a closed-form discriminator that predicted 5/5): ContextMemory.write() addresses by a hard scores.mean(0).argmin() (ree_core/predictors/e1_deep.py:144) with a deterministic single-slot fixed point under a near-constant query stream, while read() addresses by softmax -- every SD-016 remedy shipped to date (908 gumbel selection, 907 ctxdiv) lives on the read side or a separate tagger and does not touch the write address. epistemic_category standard -> substrate_ceiling: the 436e stamp of `standard` was explicitly conditioned on the substrate having "shipped and merely needing switching on", and V3-EXQ-436f is the run that tested that condition and falsified it -- the write-path selection mechanism does not exist and must be built. non_contributory: a P0 readiness failure upstream of the comparison, weighing on the claims in NEITHER direction. CAUTION: 436e's "2/2 directional on the scoreable seeds" did NOT survive this single config change (now 1/2 -- seed 200 reversed from 0.96795->0.83109 to 0.95391->0.98744); do not carry that n=2 read forward as partial support. pending_retest_after_substrate stays true, re-scoped a THIRD time: after-DV-repair -> after-SD-016-armed -> after-WRITE-PATH-ADDRESSING-BUILD. Re-derive brake FIRES for SD-017 (3rd substrate_ceiling hit, threshold 2): a same-question V3-EXQ-436g re-queue is REFUSED until the write-path build lands. PROMOTES/DEMOTES NOTHING this cycle.

**MECH-357** (append):

> [2026-08-16 governance, V3-EXQ-603u, failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16, successor to V3-EXQ-603s/603t]: sixth consecutive inconclusive Stage-H run (603h/k/r/s/t/u), fourth distinct pressure design, 19.2 h hub compute. Readiness 4/5 MET (PAG freeze on LESION 1.0; gate engages AND suppresses freeze on INTACT 1.0; Stage-0 z_goal 0.667 at floor; POSCTRL survivability 1.0). The load-bearing ABSOLUTE criterion G_H_INTACT_clears_2of3 PASSED (1.0); the load-bearing DISCRIMINATION criterion G_H_INTACT_beats_LESION FAILED because G_H_LESION_frac = 1.0 as well -- agent-directed hazard pursuit (hazard_agent_pursuit=0.9 on top of 603s's every-step drift at p=0.6) did NOT reintroduce the Pavlovian-instrumental conflict. This DISCHARGES, with a negative answer, the probe-gated question that substrate_queue mech357-freeze-incompatible-pressure-mechanism and closure node mech357_avoidance_efficacy:BUILD were opened to ask; that entry's status implemented_pending_validation is now stale. All four named pressure designs are exhausted. TWO INDEPENDENT vacuities, only one of which the self-route names. (1) DV SATURATION: hazard_stage_median_last_window = exactly 200.0 (the episode cap) in 7 of 9 arm-seeds, on a strongly bimodal (200 or 3-6) distribution, measured through a median-of-10 against a 75-step floor -- the ruler is pegged for all three arms. (2) GATE EXTINCTION IN THE SCORING WINDOW: mech357_avoidance_efficacy underflows to 5.7e-120 / 4.6e-118 / 2.1e-123 on the INTACT seeds, with decay:credit ratios of 86:1 / 188:1 / 120:1 and n_freeze_suppressed SATURATING mid-run, while mech357_scaffold_floor anneals 0.8 -> 0.0 and unmasks it -- so the INTACT arm was functionally LESIONED inside the very window the DV measures. The gate_engaged / gate_suppresses readiness checks are whole-run aggregates and cannot see this. epistemic_category STAYS standard (deliberately NOT substrate_ceiling: the unblocking eligibility-trace build is already in flight and the claim must keep its v3 experiment lane). non_contributory: neither confirmed nor falsified; the mechanism was extinct, the ruler saturated and the pressure absent, simultaneously. Failure-location MIXED across mechanism+measures+environment, NOT chargeable to REE. The manifest's own self-route ("re-calibrate UP") is REJECTED: a 7th same-question pressure recalibration is refused, since a pressure increase cannot fix the efficacy underflow and the cheapest live hypothesis (a graded re-read of the ALREADY-RECORDED 603s/603t/603u per-episode trajectories) costs zero compute. pending_retest_after_substrate stays true, scoped to after-the-eligibility-trace-fix AND a graded, scoring-window-scoped DV. PROMOTES/DEMOTES NOTHING this cycle.

---

*Staging-mode artifact. Step 8 not run; routing drafted, not finalised. No claims.yaml,
manifest, review_tracker.json, substrate_queue.json, hypothesis_space_* file,
TASK_CLAIMS.json entry, chip, or commit was written by this session.*
