# Failure autopsy -- V3-EXQ-943 (ContextMemory write-address, real-agent occupancy floor)

**Generated:** 2026-08-21T01:34:03Z
**Scope:** single
**Status:** `confirmed` 2026-08-21T01:56:34Z (Step 8: confirm as written).
Step 7c CONFIRMED (P0 min writes 2933; routing unchanged). Step 9b: no live
registry append (claim-free; occupancy cannot choose BIAS vs REFRACTORY).

**Companion:** `failure_autopsy_V3-EXQ-943_2026-08-21.json`

**Session:** `failure-autopsy-batch-20260821`

This is a claim-free diagnostic PASS. A clean diagnostic PASS still requires
this skill (2026-08-07 correction). Central question: did the PASS hold for a
real reason, or a degenerate/vacuous one?

`targets[]` covers ONLY
`v3_exq_943_contextmemory_write_selection_validation_20260820T115815Z_v3`.
Prior 436f / INV-044 / SD-017 artifacts are read-across, not retargeted
(R2 latest-wins).

---

## 0. Gates run before any metric was read

| Gate | Result |
|---|---|
| Already-done check (`check_autopsy_coverage.py`, content match) | AVAILABLE YES. 0 artifacts cover this queue_id or run_id. |
| `check_dry_run_citations.py` | **0 dry cited, 0 dry in named families, 0 ambiguous, 1 clean, 0 unknown**, exit 0. Manifest `dry_run` absent/null. |
| `validate_recording.py --paths <manifest>` | **1 complete, 0 always-core gaps.** `recording_schema rec/v1`, `substrate_hash`, `config`, `seeds`, `machine`/`machine_class`, `elapsed_seconds` present. `substrate_stable_across_run: true`. |
| `validate_experiments.py --checks dry_run_unreachable_criterion` | 11 corpus warnings, all `v3_exq_543` b-l. This driver silent. Manual read of the reduction block: dry path is 2 episodes x 5 steps x 1 seed; C1 requires >=3/5 seeds; `criteria_non_degenerate` is `len(seeds)>=2`. A smoke could not have produced this PASS. |
| Re-derive brake | N/A (`claim_ids: []`). Fired false. |
| Granularity-debt trigger | Does not fire (no tagged claim). |

Ran to completion (`outcome: PASS`, no traceback). Not an `/diagnose-errors` target.

---

## 1. Facts

`v3_exq_943_contextmemory_write_selection_validation_20260820T115815Z_v3`
PASS | `experiment_purpose: diagnostic` | `claim_ids: []` |
`ree-cloud-2`, `linux-x86_64-py3.10-torch2.12.0+cpu` | 147.924 s |
seeds `[42, 7, 13, 100, 200]` |
`substrate_hash 9fd8b2fbafdbff70...` | `substrate_commit b1f0d9f6f35200c6` dirty false |
`evidence_direction: non_contributory` (self-stamped) |
self-route `write_address_fix_validated_under_real_agent`.

Queue entry is absent from live `experiment_queue.json` (completed items are
removed). Driver: `ree-v3/experiments/v3_exq_943_contextmemory_write_selection_validation.py`.

**Design.** Three arms x five seeds, 436-family CausalGridWorldV2 + REEAgent
training loop (200 episodes x 150 steps, context switch every 5). Both write-address
flags set explicitly in every arm (architecture constraint 1). DVs are occupancy,
entropy, self_repeat, round_robin only -- not occupied-slot cosine, not cluster
Jaccard (constraint 2). Action policy is `_select_action_baseline` (E2 world_forward
+ E3 harm_eval). Writes fire from `sd016_writepath_mode="sense_only"` during
`agent.sense()`. No sleep. `sd016_enabled` left at default False.

| Arm | balancing | selection | k |
|---|---|---|---|
| LEGACY | False | argmin | 2 (unused) |
| BIAS | True | argmin | 2 (unused) |
| REFRACTORY | False | refractory | 2 |

**P0:** `writepath_engaged_every_cell` measured 2933.0 vs floor 200.0, met.
Per-seed write counts 2933 / 3043 / 3187 / 3152 / 3023. **Identical across all
three arms at each seed** (recomputed from `arm_results[]`).

**z_goal_stream:** `ticks_total` 0, `writer_calls` 0, `writer_defect` null,
`goal_state_present` false, `n_agents` 15. Expected: no goal-using agent. No
criterion depends on z_goal. Not the 861e writer-defect.

### Recomputed from cells (slot_write_counts occupancy and entropy match the manifest)

Seeds 42, 7, 13, 100, 200. Floor = occupied >= 2. `log2(16)=4`, `log2(3)=1.584963`.

**LEGACY** (descriptive, not load-bearing): occupied 8 / 1 / 1 / 1 / 9 -- floor **2/5**.
Entropy 2.637 / 0 / 0 / 0 / 2.059. Self-repeat 0.969 / 1.0 / 1.0 / 1.0 / 0.896.
Round-robin ~0. Seeds 7, 13, 100: single-slot lock. Same three seeds locked in
436e/436f.

**BIAS:** occupied 16 / 16 / 16 / 16 / 16 -- floor **5/5**.
Entropy 3.999995 / 3.999997 / 3.999997 / **4.0** / 3.999999.
Self-repeat 0.0 on 5/5. Round-robin 0.994886 / 0.995728 / 0.995293 / 0.993020 / 0.994707.
Seed 100: 197 writes in every slot (197 x 16 = 3152).

**REFRACTORY:** occupied 6 / 3 / 3 / 3 / 9 -- floor **5/5**.
Entropy 2.536 / **1.584962** / **1.584962** / **1.584962** / 2.072.
Self-repeat 0.0 on 5/5. Round-robin ~0.
Lock-seed occupancy is exactly k+1 = 3; those three entropies equal `log2(3)`.
Seed 200 tracks LEGACY (9 and 9). Seed 42 is 8 (LEGACY) vs 6 (REFRACTORY).

**Criteria:** C1_BIAS 5/5 passed (required 3, load-bearing). C1_REFRACTORY 5/5
passed (required 3, load-bearing). LEGACY_reference_reproduces_known_degeneracy
passed as descriptive (2/5 < 3). `criteria_non_degenerate` both true.

---

## 2. Claim layer

`claim_ids: []`. No claim tested. The driver states this validates substrate
readiness of `contextmemory-write-path-addressing-degeneracy`, not SD-017 /
ARC-045 / MECH-166. Those claims are read-across only (Section 8).

---

## 3. Biological-reference triage

Closest mechanisms: DeSieno 1988 frequency-sensitive competitive-learning
conscience bias, and an absolute refractory period on a recently-active unit.
Architecture doc names both. Not a formal-definition import. `lit_status: present`.
No `/lit-pull` owed. Divergence already named in-tree: at default weight the
conscience bias is occupancy without addressing (a global usage-EMA is not a
first-order neural property; refractory is).

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | claim-free |
| Biological reference | clear | DeSieno conscience; neuronal refractory. Divergence named, not a missing lit entry. |
| Developmental / dependency prerequisites | present | Both knobs landed, gated_content_write on, writepath P0 met. |
| Implementation completeness | partial | Flags reached `write()`. BIAS is occupancy-without-addressing (counter-driven period-16 cycle). REFRACTORY occupancy >= 2 is by construction for k=2. Neither is a learned write policy. |
| Environment adequacy | adequate | 436 harness, real latents, writepath engaged. Agent not using memory for action is by design of this diagnostic. |
| Measurement adequacy | partial | Right DVs (occupancy / entropy / self_repeat / round_robin). C1 floor of 2 cannot fail for REFRACTORY k=2 once P0 holds, and cannot fail for BIAS once the usage term dominates. Non-gating columns are what diagnose. |
| Integration adequacy | isolated | Writes are a `sense()` side-effect; action selection never consults ContextMemory. Write-count identity across arms is the fingerprint. |
| Scale / capacity | adequate | 16 slots, ~3000 writes/cell. Binding constraint is the address rule. |

**Failure-location (GOV-FAILLOC-1):** MIXED, not chargeable to REE in either
direction. Mechanism `partial`, measures `partial`, environment `established`,
`ree: false`. Do not write that REE succeeded at diverse writing, or that REE
failed. The occupancy floor passed because the address function was swapped
and (for REFRACTORY) is analytically guaranteed.

---

## 5. Is the PASS real or vacuous?

**Mixed -- real wiring, vacuous as agent-level write selection.**

Real:

1. P0 is not config-only (min 2933 `write()` calls vs floor 200, 15/15 cells).
2. LEGACY still locks seeds 7/13/100 -- the 436e/436f operating point is
   reproduced, so the fix arms are not scored on an already-diverse query stream.
3. BIAS and REFRACTORY DVs match the independently pre-registered unit-level
   probe, which is the fingerprint that the knobs reached `write()` rather than
   a silent default-off path.
4. Instrumentation polls `last_write_index` (does not re-derive argmin). The
   436f tracker trap is not in play.

Vacuous as "the agent selected writes":

1. Writes are automatic `sense()` side-effects. The agent never chooses a write.
2. Action selection never reads ContextMemory. Write counts are identical
   across arms at each seed.
3. C1_REFRACTORY (>=2 occupied, k=2) is analytically guaranteed: occupancy
   >= k+1 = 3 by construction. Observed 3 on all three lock seeds, entropy
   exactly `log2(3)`.
4. C1_BIAS (>=2) is guaranteed once `usage_ema * sqrt(memory_dim)` dominates
   `mean_scores`. Observed 16/16, entropy ~4, round-robin 0.993-0.996,
   self_repeat 0 -- occupancy without addressing, already named in
   `contextmemory_write_address_selection.md`.
5. Self-route `write_address_fix_validated_under_real_agent` names a stronger
   claim than C1 can bear. Narrow reading: occupancy-floor validated under
   real-agent *latents*.

The indexer did not flag `vacuous_pass` because `criteria_non_degenerate` is
true for both C1 keys (5 seeds >= 2). It cannot see analytic guarantees in
the address function.

`ContextMemory.write()` / `_select_write_slot()` (ree-v3
`ree_core/predictors/e1_deep.py`) confirm: BIAS adds `w * usage_ema * sqrt(d)`
to the score then argmin; refractory masks the last k slots to +inf then
argmin among the rest. Architecture: occupancy cannot choose a winner;
neither mechanism is declared the winner; that was this experiment's job.
This experiment's registered gate was occupancy only, so it cannot declare
a winner either -- and it should not.

---

## 6. Re-derive brake

Fired **false**. `claim_ids: []`; recommended category `standard`, not
`substrate_ceiling`. A further occupancy-floor letter of 943 is refused on
design grounds (`mystery (known data)`: occupancy cannot choose; the
deterministic columns already exist), which is not a brake firing.

The 436f brake (SD-017, 3rd ceiling hit, 436g refused until the write-path
*build* lands) is a different artifact's field. This autopsy does not
re-stamp it. See Section 8.

---

## 7. Learning and routing

**Node class:** occupancy-floor question is answered (`complicated (buildable)`,
already built, now occupancy-validated). Which flag to ship as default is
`mystery (known data)` -- do not gather more occupancy runs.

**Learning.**

1. Occupancy floor holds for both fix arms under a REEAgent loop on the 436
   harness, with LEGACY still locking the same 3 seeds. Wiring is real.
2. BIAS under real latents is the same counter-driven period-16 cycle the
   unit probe measured.
3. REFRACTORY hits the structural k+1=3 floor on every legacy-lock seed.
4. Write-count identity across arms plus a harm-eval policy that never reads
   memory means the "real agent" contributed a query stream, not a
   write-selection policy.
5. Self-route overclaims. Narrow it.
6. A 436-family sleep retest is occupancy-unblocked if a write-selection flag
   is ON. Prefer `refractory` so content argmin among eligible slots is
   preserved. BIAS would fill all 16 slots via a counter-driven cycle and
   would likely wash out context-conditioned slot sets a sleep DV needs.
7. z_goal ticks_total 0 is expected and is not the 861e writer-defect.

**Routing: `governance`.** Amend substrate_queue
`contextmemory-write-path-addressing-degeneracy`: append V3-EXQ-943 as a
validation record. Do **not** auto-flip `implemented_pending_validation` to
`implemented_validated`. Leave the 436f `failure_record` `resolved: open`
until a human decides whether occupancy-without-addressing (BIAS) or the
k+1 eligibility floor (REFRACTORY) closes the corrupting 1-slot-bank defect.

**Not routed:** `/lit-pull`; `/queue-experiment` for a 943b occupancy letter;
`/implement-substrate` (build already landed); `/claim-synthesis`;
governance-demotion; REE-succeeded prose.

**Follow-ons (reported, not chipped):**

1. The substrate_queue amend above -- this autopsy's own recommendation.
2. If occupancy-floor is accepted as closing the 1-slot corrupting defect:
   a 436-family sleep retest with `contextmemory_write_selection=refractory`
   (not BIAS), occupancy-masked cosine, 436e instrument. The 436f brake's
   "until the write-path build lands" condition is now met for occupancy.
   Sleep-vs-waking discrimination is still untested. Occupied-slot cosine
   still cannot discriminate *write-address arms* at 5 seeds (architecture
   probe); whether it can discriminate *sleep* once occupancy is
   non-degenerate is a different, open question. Whole-bank
   `sws_slot_diversity` remains prohibited.

**Draft `evidence_quality_note`:** see companion JSON
`recommended_evidence_quality_note` (manifest-level; no claim to write).

---

## 8. Read-across (not adjudicated)

This artifact does not supersede `failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16`
or `failure_autopsy_slot_cosine_sim_fanout_sweep_2026-08-13`.

**SD-017 / ARC-045 / MECH-166.** 436f stamped `substrate_ceiling` and
`pending_retest_after_substrate` re-scoped to after-WRITE-PATH-ADDRESSING-BUILD,
brake refusing 436g until that build. The build has landed (two default-off
knobs). This PASS shows the occupancy floor is met under real-agent latents
when a knob is on, which lifts the occupancy P0 that made 436f C1 unscorable
on 3/5 seeds. It does not score sleep-vs-waking occupied-slot cosine, does
not flip those claims off `substrate_ceiling`, and does not supersede 436f's
targets.

**INV-044.** Not moved. 943 computed neither occ_cos nor whole-bank cosine.
INV-044's experimental base is still V3-EXQ-429's whole-bank C1/C2 as
diagnosed by the slot_cosine sweep. Occupancy vs whole-bank similarity:
the sweep's finding is that an *empty* bank passes a diversity>eps gate
with P=1; 943's BIAS bank is *full* (16/16) via round-robin, which is a
different occupancy regime and still not a cosine measurement.

---

## 9. Step 7b

See companion JSON `pre_routing_checks`. Ran on the draft before the sibling
`.md` existed (C5 inapplicable then); re-ran after this file was written.
Every fire is disposed there. Step 7c skipped (parent).

---

## 10. Constraints observed

Staging mode. No TASK_CLAIMS mutation. No commit. No chip. No live registry
write. No `claims.yaml` / manifest / `review_tracker.json` /
`substrate_queue.json` / `hypothesis_space_registry.v1.json` edit.
