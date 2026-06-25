# Failure Autopsy — V3-EXQ-705 (MECH-314 curiosity-conversion under F→eligibility demotion ON)

- **Status:** confirmed (user-gated, interactive Step-8 2026-06-25T04:41Z)
- **Run:** `v3_exq_705_mech314_curiosity_conversion_demotion_20260625T033702Z_v3`
- **Queue:** V3-EXQ-705 · `experiment_purpose=evidence` · `claim_ids=[MECH-314]`
- **Outcome:** FAIL · `evidence_direction=non_contributory` · `non_degenerate=false` (scoring-excluded — **MECH-314 NOT weakened**)
- **Self-routed label:** `substrate_not_ready_requeue`
- **Machine:** ree-cloud-3
- **Generated:** 2026-06-25T04:41:04Z

---

## 1. Scope

Single-run autopsy of the brake-EXEMPT MECH-314 curiosity-conversion re-test routed by
`failure_autopsy_V3-EXQ-590c_2026-06-24`. 705 is a **different-substrate redesign** (the
MECH-448/ARC-107 rank-preserving F→eligibility demotion ON every arm), NOT another
590-lineage `curiosity_novelty_weight` sweep. The decisive readiness gate
(legC `f_eligibility_demotion_non_degeneracy`) failed, so the load-bearing
committed-diversity criterion could not fire. Deferred to autopsy by the
`/governance` cycle 2026-06-25T04:20Z (user directive: "fails need autopsies before we
decide"); the run was left PENDING with no `evidence_direction` that cycle.

## 2. Facts reconstruction (no interpretation)

3 arms × 3 seeds (42/43/44), all `use_f_eligibility_demotion=True`, MECH-314 curiosity
the SOLE modulatory channel, `curiosity_candidate_source=e2_world_forward` (GAP-A pool),
SD-056 online + rollout clamp, harm-free env (num_hazards=0). Fixed demotion config:
`f_eligibility_envelope_floor=0.30`, `f_eligibility_dn_sigma=0.0`,
`use_f_eligibility_adaptive_floor` **NOT set** (fixed absolute share floor).

Readiness legs (all read at ARM_CURIOSITY = the non-saturation w=0.25 arm):

| Leg | Statistic | Measured | Floor | Met? |
|---|---|---|---|---|
| A — GAP-A pool divergence | `cand_world_pairwise_dist_mean` | 0.210147 | 0.02 | **YES** (3/3) |
| B — curiosity per-candidate RANGE (non-saturation arm; 590c confound fix) | `curiosity_bias_range_mean` | 0.02129 | 1e-4 | **YES** (3/3) |
| **C — demotion non-degeneracy** | `f_eligibility_excluded_count_mean` (per seed >0) | mean 0.198, **1/3 seeds** | >0 on ≥2 seeds | **NO** |
| D — rolled-out z_world finite | `max cand_world_pairwise_dist` | 0.468 | <1e6 | YES |

Per-seed legC (ARM_CURIOSITY):

| Seed | `excluded_count_mean` | `envelope_size_mean` | `demotion_active_frac` | `rank_preserving_frac` | committed_class_entropy |
|---|---|---|---|---|---|
| 42 | **0.595** (excludes) | 31.40 | 1.0 | 1.0 | 1.3957 |
| 43 | **0.000** (all-admit) | **32.0** | 1.0 | 1.0 | 0.0 (1 class) |
| 44 | **0.000** (all-admit) | **32.0** | 1.0 | 1.0 | 0.7752 |

Per-arm `committed_class_entropy_mean`: ARM_CURIOSITY **0.7236** < ARM_FONLY = ARM_NOISE
= **0.89635** (identical). `rank_preserving_frac_on_mean` 1.0; `demotion_active_frac` 1.0
(the lever fires on every tick — it just doesn't EXCLUDE).

**Failed criterion class:** readiness precondition (`f_eligibility_demotion_non_degeneracy`),
i.e. the eligible-set the curiosity-vs-control contrast depends on **never formed** on
2/3 seeds. This is the discrimination-criterion-could-not-fire shape, not a
negative-control failure.

## 3. Claim-layer mapping (MECH-314)

`MECH-314` = `structured_curiosity_bonus` (frontopolar uncertainty-driven exploration +
expected-free-energy analog; striatal novelty Wittmann 2008 / Daw 2006), status
`candidate_substrate_landed`, `v3_pending=false`, `implementation_phase=v3`,
`depends_on=[ARC-065, MECH-313]`. The demotion (MECH-448/ARC-107) is the **enabling
substrate**, not the claim under test; `claim_ids=[MECH-314]` was re-evaluated from
scratch by the queue session (correct per the claim_ids-accuracy rule).

**Did the test let MECH-314 express itself?** No. On 2/3 seeds the demotion all-admitted,
so F was never removed from the committed argmin and the curiosity channel arbitrated over
a near-whole (≈31.8/32) eligible set. Its argmin then collapses to the single most-novel
candidate ⇒ monostrategy ⇒ committed entropy 0.7236 **below** the controls. The
below-control entropy is a **degeneracy symptom of the all-admit**, not evidence against
MECH-314 — `non_degenerate=false` correctly excludes it from scoring. **Claim alignment:
intact.**

## 4. Biological-reference triage

Closest mechanism: basal-ganglia / pallidal eligibility gating under divisive normalisation
(Mink 1996 focal-go + surround-no-go; Carandini & Heeger 2012 DN). The demotion grades
eligibility by F-merit share. The 705 failure — the envelope admitting ~everything on
near-tie-F seeds — maps to a **pallidal/STN threshold mis-set for the input distribution**,
not to the mechanism being wrong. Biology supports the mechanism; the gate simply did not
engage because the *fixed* share floor was calibrated for a different (more F-concentrated)
channel. This is a discovered config prerequisite, NOT a falsification.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | test could not let MECH-314 express — demotion didn't engage on 2/3 seeds |
| Biological reference | **clear** | BG eligibility / divisive-norm; failure = gate-threshold mis-set, not mechanism wrong |
| Prerequisites | **present but mis-configured** | MECH-448 demotion built; the channel-adaptive floor amend (`use_f_eligibility_adaptive_floor`) built + validated 2026-06-21 (689e) — just not enabled |
| Implementation | **complete** | demotion substrate + adaptive floor both implemented in `e3_selector.py` |
| Environment | **adequate** | GAP-A reef-bipartite divergent pool (legA 0.210) |
| Measurement | **adequate (instrument worked)** | the readiness legs correctly detected the all-admit and self-routed — the GOOD case |
| Integration | **partially coupled** | demotion + curiosity composition wired; eligible-set construction all-admitted |
| Scale / capacity | adequate | — |

**Dominant diagnosis → `substrate_not_ready` (V3-EXQ-642 invalid-precondition family).**
NOT `substrate_ceiling`: the substrate exists, works, and is validated; the gap is a fixed
vs channel-adaptive floor-calibration config the run did not select.

## 6. The decisive contrast (689d / 689e) — config artifact, not real property

The user's key question: is "demotion admits ~everything" a config artifact of THIS run or
a real property of the demotion on the GAP-A foraging substrate? The cross-references settle
it as **config artifact**:

- **689d** (MECH-448 falsifier, PASS / `supports`, **fixed** floor) excluded only
  `on_excluded_count_mean = 0.152` (envelope ~31.85) and STILL passed — so low *average*
  exclusion is not the failure. 705's failure is **per-seed complete all-admit**: seeds 43/44
  hit `excluded_count == EXACTLY 0.0`, `envelope_size == EXACTLY 32.0`. Cause: on the
  **harm-free** foraging pool (num_hazards=0, hazard_harm=0.0) the F-score over the
  curiosity-divergent candidates is near-tied → every candidate's merit-share falls below the
  **fixed 0.30 absolute floor** → empty-eligible → the WIDE all-admit fallback fires
  (`excluded_count == 0` by design). The pool is action-divergent (legA 0.21) but
  **goal/harm-flat**, so F cannot concentrate enough share for the fixed floor to bite.
- **689e** (channel-adaptive mean-relative floor, `use_f_eligibility_adaptive_floor`,
  **landed + validated 2026-06-21** precisely to fix this all-admit signature) excludes
  `adaptive_excluded_count_mean = 14.8–15.7` of 32 candidates **reliably** vs the fixed
  floor's 0.0–0.73 on the same channels. By construction `mean_factor ≥ 1.0` on any
  non-uniform field puts at least one candidate below the mean share → excludes
  (`excluded_count > 0`), and stays rank-preserving.

So the demotion **CAN** be made to exclude non-degenerately on this substrate — the validated
substrate to do it already exists; 705 simply ran with the wrong (un-adaptive) floor. This is
the off-ramp's negation: not a real property of the demotion, a missing config flag.

## 7. Learning extracted

- The fixed `f_eligibility_envelope_floor=0.30` mis-fires on flat-F / near-tie channels
  (harm-free foraging pool) — it all-admits where 689d's more F-concentrated bank did not.
  The channel-adaptive mean-relative floor (`use_f_eligibility_adaptive_floor`, 689e-validated)
  is the per-channel fix and should be the **default** for any MECH-448-demotion re-test on a
  flat-F substrate.
- A self-routed `substrate_not_ready_requeue` on legC all-admit is a *correctly-caught invalid
  precondition*, not a substrate ceiling — the demotion lever fired (`active_frac` 1.0) but
  the envelope didn't narrow.
- The below-control ARM_CURIOSITY entropy (0.7236 < 0.896) is a degeneracy of the all-admit
  (novelty argmin over a near-whole pool = monostrategy), NOT a MECH-314 weakening.

## 8. Routing decision (user-confirmed, interactive Step-8 gate)

**Routing = `queue-experiment` re-issue (V3-EXQ-705b, supersedes 705).** Enable the
689e-validated channel-adaptive floor (`use_f_eligibility_adaptive_floor=True`, mean-relative,
`f_eligibility_adaptive_mean_factor` ≈ 1.0) so the demotion produces a non-degenerate eligible
set on ≥2/3 seeds. Add a hardened legC readiness precondition: `excluded_count_mean > 0` on
≥ MIN_SEEDS seeds (the substrate-readiness gate) BEFORE the committed-diversity criterion is
scored — so a residual all-admit self-routes `substrate_not_ready_requeue` rather than
manufacturing a false reading. Keep the 590c confounded-precondition fix (legB read at the
non-saturation arm) and the channel-PRESENCE contrast (ARM_CURIOSITY w=0.25 vs ARM_FONLY w=0.0
vs ARM_NOISE flat-hot). `claim_ids=[MECH-314]`; `experiment_purpose=evidence`; PROMOTES NOTHING.

**Re-derive brake = NOT fired** (user-confirmed). 4 prior MECH-314 `substrate_ceiling` /
`non_contributory` autopsies (`EXQ-572-573`, `604a-624a-630`, `gapA-cluster-604b-648a-649`,
`590c`); this would be the 5th. The brake fires only on a **clean** ceiling reading at the
same granularity against the same exercised substrate. 705 is a **confounded /
un-exercised-substrate** reading (V3-EXQ-642 invalid-precondition family — the demotion the
590c autopsy routed to was not actually exercised on 2/3 seeds). Firing now would be
illusory-resolution (the precedent set by `failure_autopsy_V3-EXQ-701a` — confounded run,
brake held). The 590c autopsy correctly routed 705 as the brake-EXEMPT redesign; this autopsy
keeps the brake exempt because the redesign's enabling substrate did not engage.

**Brake-lock condition (recorded on the target):** if V3-EXQ-705b clears legC (the
channel-adaptive demotion genuinely excludes, `excluded_count>0` on ≥2/3 seeds, MECH-314
fairly tested under a narrowing demotion) AND committed_class_entropy STILL shows no lift over
the demotion-ON F-only control + matched-noise control → THAT is the genuine
`conversion_ceiling_persists_despite_demotion` off-ramp → fire the re-derive brake (6th) and
route the curiosity-conversion question to MECH-449 Go/No-Go (double-gated) / V4. Until then
the brake is held.

## 9. Governance hand-off

- `evidence_direction`: **non_contributory** (already self-emitted; `non_degenerate=false`
  scoring-excluded). No manifest correction needed — the run's self-route is SOUND.
- `recommended_epistemic_category`: **NOT** `substrate_ceiling` (this is a re-queue, not an
  enrichment) — leave MECH-314 untouched.
- MECH-314 stays `candidate_substrate_landed`; **PROMOTES NOTHING**, weakens nothing.
- No `substrate_queue` entry (`action: none`) — the substrate (channel-adaptive floor) is
  already built + validated (689e); the only owed work is the 705b re-queue with the flag set.
- `recommended_evidence_quality_note` (governance may append to MECH-314 if desired, but the
  run is already non_contributory so no scoring change): *"V3-EXQ-705 non_contributory
  (substrate_not_ready_requeue): the MECH-448 F→eligibility demotion all-admitted on 2/3 seeds
  (fixed envelope_floor=0.30 mis-calibrated for the near-tie F-merit of the harm-free foraging
  pool), so MECH-314 curiosity was not fairly tested under a narrowing demotion. Re-queue
  V3-EXQ-705b with use_f_eligibility_adaptive_floor (689e-validated) + a legC excluded_count>0
  readiness gate. NOT a MECH-314 weakening; re-derive brake held (V3-EXQ-642 invalid-precondition,
  not a clean ceiling)."*
