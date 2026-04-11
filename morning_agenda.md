# Morning Agenda — 2026-04-11

Generated: `2026-04-11T12:25:00Z`

---

## Queue Status

- **Total pending: 0** — **ALERT: Queue is EMPTY**
- Mac (DLAPTOP-4.local): 0 | PC (Daniel-PC): 0 | any: 0
- The queue was drained overnight. New experiments should be queued before the runner is started.
  Candidates based on today's pending reviews: EXQ-323b (SD-019 seed-variance replication, 3-seed
  threshold tweak or more seeds), EXQ-324b (SD-020 surprise-PE re-run on SD-022 substrate with
  >=100 harm events as predicted in governance-2026-04-11), EXQ-325b (SD-021 descending
  modulation fix if /diagnose-errors reveals a measurement gap), EXQ-266b if EXQ-266a still shows
  terrain-harm-rate ceiling effect.

---

## Experiments Awaiting Review (6 indexed / 1 runner-only)

> **Note:** Several of these runs correspond to experiments partially discussed in the
> governance-2026-04-11 session — but the run-pack conversion only completed today (governance.sh
> just synced 6 new run-packs). The session reviewed earlier sibling runs; these are new or
> follow-on runs that also need review_tracker.json entries to clear the pending list.

---

### [EXQ-266a] — v3_exq_266a_q020_valence_geometry_pair_fixed — FAIL (1/4)

- **Claims tested:** Q-020 (status: resolved, conf=0.672, entries: 1 sup / 5 wkn / 1 mix)
- **Key metrics:** harm_rate TERRAIN_SHAPED=0.0061 vs TERRAIN_FLAT=0.0061 (reduction=0.000,
  i.e. zero separation); terrain_harm_corr SHAPED=-0.4384 vs FLAT=0.8415; seed_pair_pass_harm=0
- **Classification:** evidence (bug-fix iteration of EXQ-266; ablation wiring fixed)
- **Context:** EXQ-266 used `valence_enabled=False` which only gated SD-014 valence vectors, not
  the basic harm scalar — so TERRAIN_FLAT inadvertently also accumulated harm. EXQ-266a gates
  `residue_field.accumulate()` by `terrain_shaped` flag directly. Despite the fix, harm rates
  are nearly identical (0.0061 both conditions) — suggesting a harm-rate ceiling or near-floor
  effect rather than a measurement-wiring bug.
- **Governance impact:** Q-020 is already **resolved** (Resolution A: ARC-007 and MECH-073
  co-true). This FAIL adds a does_not_support entry to an already-resolved question — the
  resolution stands, but the experimental arm is consistently failing. Worth noting as a design
  gap: the discriminative pair geometry may require a stronger terrain influence at current
  training depth, not just correct wiring.
- **Supersedes:** EXQ-266 (x2 runs, 20260410T023257Z + 034439Z — ablation wiring bug; already
  marked superseded in governance-2026-04-11)

---

### [EXQ-322] — v3_exq_322_sd015_resource_encoder_seeding — FAIL (0/3 seeds)

- **Claims tested:** SD-015 (status: candidate, conf=0.694, 4 sup / 2 wkn); MECH-112
  (status: candidate, conf=0.842, 12 sup / 4 wkn)
- **Key metrics:** seeds_passing=0; C1 resource_r_higher, C2 abs_resource_r>0.2,
  C3 benefit_not_worse — all failed
- **Classification:** evidence — but needs /diagnose-errors
- **Context:** The governance-2026-04-11 session reviewed the EARLIER sibling run
  (20260410T184213Z, reviewed) and found n_cosine_samples=0 (measurement gap — no cosine
  similarity samples were collected). This NEWER run (222041Z) is a re-run. Need to verify
  whether the n_cosine_samples=0 gap was fixed. If still zero: another measurement-gap
  /diagnose-errors case. If non-zero: genuine negative evidence for SD-015 / MECH-112.
- **Governance impact:** If genuine: adds does_not_support to SD-015 (would move from 4:2 toward
  4:3) and MECH-112 (12:4 -> 12:5). Both would remain above 0.6 threshold but with growing
  opposition. Recommend /diagnose-errors first.

---

### [EXQ-323] — v3_exq_323_sd019_harm_nonredundancy — FAIL (2/3 seeds — near-miss)

- **Claims tested:** SD-019 (status: candidate, conf=0.361, 0 sup / 1 wkn / 1 mix); SD-011
  (status: candidate, conf=0.834, 21 sup / 7 wkn)
- **Key metrics:** seeds_passing=2 (need 3); Seed 42: cosine_sq NONREDUNDANT=0.119 vs
  BASELINE=0.014 (C1 FAIL — nonredundant cosine unexpectedly HIGHER than baseline); Seeds
  43+44: cosine_sq 0.002 vs 0.004 and 0.012 vs 0.025 (both C1 PASS); all seeds C2+C3 PASS
- **Classification:** evidence — with near-miss pattern
- **Context:** This is the EARLIER run (160857Z); a later sibling (184158Z) was already reviewed
  in governance-2026-04-11 and found collinear EMA substrate. The near-miss (2/3 seeds) is
  scientifically notable — Seed 42's inversion of the cosine direction is a potential
  initialization-sensitivity signal. Governance note: SD-011->non_contributory on the sibling
  run (collinear EMA substrate). Evidence direction may need to be consistent with the sibling.
- **Governance impact:** Adds mixed evidence to SD-019 (already at 0.361 conf, 0P/2F). Two
  consecutive near-misses suggest the mechanism is present but the experiment is
  underpowered or the 3-seed all-pass threshold is too strict given seed variance.

---

### [EXQ-324] — v3_exq_324_sd020_harm_surprise_pe — FAIL (1/3 seeds)

- **Claims tested:** SD-020 (status: candidate, conf=0.693, 4 sup / 1 wkn / 1 mix); SD-011
  (status: candidate, conf=0.834); Q-036 (status: open, conf=0.324)
- **Key metrics:** seeds_passing=1; C1 surprise_corr_higher, C2 abs_surprise_corr>0.15
- **Classification:** evidence — predicted re-run from governance-2026-04-11
- **Context:** The governance-2026-04-11 session reviewed the EARLIER run (220218Z, on
  2026-04-10) and classified SD-020 as mixed (confounds: n=10-20 harm events too few,
  harm_obs_a_variance too low due to EMA substrate). The prediction was to re-run on SD-022
  substrate with >=100 harm events. This newer run (050533Z, from 2026-04-11 05:05 — post-
  governance) is that re-run. It fails with 1/3 seeds — slightly better than before but still
  failing. The SD-022 substrate may not yet be providing the predicted harm event density.
- **Governance impact:** SD-020 has a **pending_user** decision (hold_candidate_resolve_conflict).
  This result should inform that decision: experimental evidence is weak (conf exp=0.362), but
  literature is very strong (conf lit=0.914). The 1/3 seed partial result is ambiguous — not a
  clean negative.

---

### [EXQ-325] — v3_exq_325_sd021_descending_pain_modulation — FAIL (0/3 seeds)

- **Claims tested:** SD-021 (status: candidate, conf=0.751, 4 sup / 1 wkn); MECH-090
  (status: active, conf=0.776, 9 sup / 5 wkn / 9 mix); SD-011 (status: candidate, conf=0.834)
- **Key metrics:** seeds_passing=0; C1 z_harm_s_ratio_reduced threshold, C2
  z_harm_a_selectivity>0.3, C3 committed_steps>10 — all failed
- **Classification:** evidence — but this experiment had UNKNOWN runner status before today's
  governance.sh sync. Also flagged as /diagnose-errors by governance-2026-04-11.
- **Context:** The governance-2026-04-11 session saw this as "runner-only V3-EXQ-325 UNKNOWN"
  and flagged /diagnose-errors. The sync_v3_results.py step today converted it to an indexed
  FAIL. The 0/3 seed result is a clean negative. SD-021 depends on MECH-090 (bistable latch,
  implemented 2026-04-10), SD-020 (surprise-PE), and SD-011 — all still candidates or failing.
  The 0/3 result may reflect SD-011 or SD-020 being the bottleneck, not SD-021 itself.
- **Governance impact:** SD-021 has a **pending_user** decision (hold_candidate_resolve_conflict).
  Literature confidence is 0.893 (4 entries in targeted_review_connectome_sd_021); experimental
  is 0.324 (0P/1F before this run). This FAIL adds another experimental weakens entry.
  Decision context: hold at candidate is strongly indicated — both experimental runs fail and
  upstream SDs are unvalidated.

---

### [EXQ-330] — v3_exq_330_sd013_contrastive_counterfactual — FAIL (7/10 criteria)

- **Claims tested:** SD-013 (status: candidate, conf=0.599, 1 sup / 1 wkn); SD-003 (status:
  validated, conf=0.747, 24 sup / 43 wkn); ARC-033 (status: candidate, conf=0.813, 12 sup / 4 wkn)
- **Key metrics:** C1 forward_r2 all seeds PASS (~0.997-0.999); C2 cf_gap_ratio 0/3 seeds PASS
  (ratios 1.29/1.29/1.40 vs threshold, presumably ~2.0); C3 sign_correct 3/3 seeds PASS
- **Evidence direction per claim:** SD-013: does_not_support; SD-003: does_not_support;
  **ARC-033: supports** (E2_harm_s forward model learns the prediction task correctly)
- **Classification:** evidence — partial PASS with clean per-claim split
- **Context:** This ran at 2026-04-11T02:37 — during the governance session. Was NOT reviewed.
  The pattern is informative: the forward model works (R2>0.99, sign correct) but the
  contrastive training signal is insufficient to produce a large enough cf_gap_ratio. This
  means ARC-033 (dedicated E2_harm_s forward model) gets its first experimental supports entry,
  while SD-013 (interventional training required) and SD-003 (causal signature delta) fail.
- **Governance impact:** ARC-033 gaining supports pushes it toward promotion territory (12:4 -> 13:4,
  conf currently 0.813). SD-003 adds another opp to an already heavily contested record (24:43).
  SD-013 remains at 1:2 (split). The per-claim split is clean and interpretable — recommend
  reviewing with per-claim overrides in place (already set in the flat JSON).

---

## Errors to Diagnose (0 unresolved)

All 51 ERROR entries in runner_status.json have completed successors or lettered fix runs.
No unresolved ERRORs require /diagnose-errors at this time.

> EXQ-322 (second run) should still be checked for n_cosine_samples=0 measurement gap (see
> Experiments section above) — this is a potential measurement bug, not a runner ERROR.

---

## Governance Agenda (2 pending_user recommendations)

- **SD-020** (candidate) — Recommendation: **hold_candidate_resolve_conflict** — pending_user
  - Evidence: 4 sup, 1 wkn, 1 mix (6 total); exp_conf=0.362, lit_conf=0.914, overall=0.693
  - EXQ-324 (latest run, 2026-04-11): 1/3 seeds — still failing after predicted SD-022 re-run
  - Suggested action: hold at candidate. Strong literature backing but experimental arm has
    not found a passing run. The 1/3 seed partial pass warrants another iteration (EXQ-324b)
    with confirmed harm event density >=100 before decision.

- **SD-021** (candidate) — Recommendation: **hold_candidate_resolve_conflict** — pending_user
  - Evidence: 4 sup, 1 wkn (5 total); exp_conf=0.324, lit_conf=0.893, overall=0.751
  - EXQ-325 (today): 0/3 seeds — clean experimental negative
  - Suggested action: hold at candidate. Upstream dependencies (SD-011, SD-020, MECH-090)
    all still failing or active. Cannot test SD-021 cleanly until its substrate is validated.
    The literature basis is solid but experimental implementation is blocked upstream.

---

## Literature Pull Candidates (Top 5)

| # | Claim | Subject | Priority | Existing entries | Notes |
|---|-------|---------|----------|-----------------|-------|
| 1 | Q-036 | What variables beyond temporal integration drive affective harm? | medium | 0 | No targeted_review dir exists yet; Q-036 exp_conf=0.324, no lit evidence at all |
| 2 | SD-019 | Affective harm nonredundancy constraint | medium | 0 | No targeted_review_sd_019 dir; currently 0 lit evidence, 2 experimental FAILs |
| 3 | SD-022 | SD-022 directional limb damage (provisional) | medium | 0 | No standalone targeted_review_sd_022 dir; SD-022 promoted to provisional 2026-04-11 with zero lit grounding |
| 4 | ARC-028 | (ARC-028 architectural claim) | medium | 0 | No targeted_review dir; exp_conf=0.428, 0 lit |
| 5 | SD-020 | z_harm_a affective surprise PE encoding | medium | 4 | targeted_review_connectome_sd_020 exists (1 file); 4 lit entries already in evidence index — consider extending this review |

> Note: SD-020 and SD-021 both have small existing connectome-focused targeted reviews (1 file
> each) but only 4 lit entries each in the full evidence index (high-quality; Crawford et al.
> 2021, Hoskin et al. 2023, etc.). Both would benefit from an expanded pull given their
> pending_user governance status.

---

## Serve.py Status

- **RUNNING on port 8000** (Python process confirmed listening)

---

## Blocked Items

None. No TASK_CLAIMS collision — all prior claims were `"done"` at session start.
governance.sh ran normally (6 new run-packs converted: EXQ-266a, 322, 323, 324, 325, 330).

---

## Session Recommendations

1. **Queue experiments immediately** — queue is empty and runner has nothing to do. Priority:
   - EXQ-324b: SD-020 surprise-PE on SD-022 substrate, confirmed harm event density >=100
   - EXQ-323b (or additional seeds): SD-019 nonredundancy, investigate seed-42 cosine inversion
   - EXQ-325b: SD-021 descending modulation — needs /diagnose-errors on EXQ-325 substrate first
   - EXQ-330b: SD-013 contrastive — the cf_gap_ratio threshold may be achievable with longer training or different hyperparameters

2. **Mark today's pending reviews in review_tracker.json** — add all 6 run IDs to
   `reviewed_run_ids` after discussing. Then re-run `python scripts/generate_pending_review.py`.

3. **Pending_user governance decisions** — SD-020 and SD-021 both have pending_user status.
   Recommend: hold both at candidate. SD-021 is cleanly blocked upstream. SD-020 has a
   plausible re-run path.

4. **/diagnose-errors for EXQ-322 (second run)** — verify whether n_cosine_samples=0 gap
   persists in the newer run or whether this was genuine negative evidence.

5. **Consider lit pull for SD-022** — promoted to provisional 2026-04-11 with zero literature
   grounding. The literature base is important for a provisional claim.
