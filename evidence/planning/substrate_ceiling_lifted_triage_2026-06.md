# Substrate-ceiling "ceiling-may-have-lifted" triage -- 2026-06-19

**Author:** session `substrate-ceiling-lifted-triage-20260619T1924Z`
**Generated:** 2026-06-19T19:36:21Z
**Source:** `scripts/check_substrate_ceiling_audit.py` (governance Step 6a-v) "ceiling-may-have-lifted (ACTIONABLE)" bucket.
**Status of this doc:** ANALYSIS + bucketing. No claim `status` / `v3_pending` changed. No experiments queued.

---

## Why these 15 were flagged, and the one thing the audit cannot see

The audit puts a `substrate_ceiling` claim in **ceiling-may-have-lifted** when it is *mapped*
(some `substrate_queue` entry lists it in `unblocks_claims`) **and** that entry is now
`status=implemented` **and** the claim still owes a retest (`pending_retest_after_substrate: true`).

That match is **substrate-id == implemented only**. It does **not** verify that the implemented
substrate actually delivers the distinction *this* claim needs. Across all 15, the verdict is:

> **0 of 15 are genuinely lifted by their named substrate.** Every "lift" is either a spurious
> `unblocks_claims` listing (the implemented substrate is the wrong one / only cleared a confound),
> or the named substrate delivers the *plumbing* but a downstream gate (overwhelmingly the
> **F-dominance / committed-action-diversity conversion ceiling, MECH-439**) still blocks the
> distinction.

Triage split:

| Verdict | Count | Claims |
|---|---|---|
| **(a) genuinely lifted** | 0 | -- |
| **(b) still ceilinged -> parked deferral marker** | 11 | SD-015, SD-049, MECH-295, MECH-294, MECH-280, MECH-281, MECH-262, MECH-189, SD-032b, ARC-046, MECH-334 |
| **(c) already handled (retest running today)** | 4 | ARC-062, SD-033b, MECH-263, MECH-309 |

The recurring root for the (c) cohort and several (b) cases is the **MECH-439 F-dominance
conversion ceiling** (forward-model F ~88-89% of E3 selection variance, V3-EXQ-571): a modulatory
/ rule / OFC channel reaches the accumulator with real range, but cannot carve *committed* action
against F. The only conversion PASS is **V3-EXQ-569i** (top-k shortlist, tagged ARC-065,
**env-conditional** per `failure_autopsy_V3-EXQ-625d_2026-06-18`), and it is the constant now wired
into the live per-claim retests below.

---

## Audit-tooling finding (acted on this pass)

A deliberate-defer marker (`ceiling_decision: deferred`) was **inert** for every claim in this
bucket, because the audit's bucket precedence checked `ceiling_may_have_lifted` and `mapped`
**before** `parked`. Since all 15 are mapped+implemented+retest-owed, a marker could not move them.

That defeats the parking convention's stated purpose ("stop re-flagging intentionally-parked
ceilings every cycle"). Fix applied in this pass: **`parked` is now checked first** in
`check_substrate_ceiling_audit.py` (`audit()` precedence reorder + docstring update). A claim the
operator has explicitly deferred is bucketed `parked` regardless of substrate status; remove the
marker to re-route. This only affects claims carrying an explicit `ceiling_decision: deferred`
marker, so the four (c) cohort claims (no marker) correctly stay in `ceiling_may_have_lifted`.

Post-fix expected buckets: **15 parked** (4 pre-existing MECH-440/441/443/444 + the 11 below),
**4 ceiling-may-have-lifted** (the (c) cohort, retests in flight), **1 self-handled** (SD-037),
0 orphaned.

---

## (c) ALREADY HANDLED -- retest running today (NOT parked; do not duplicate)

These four correctly remain in `ceiling-may-have-lifted`: a retest **is** owed and **is in flight**
as of 2026-06-19, arming the 569i top-k conversion mechanism. Let them score; governance reconciles
`pending_retest_after_substrate` afterward. **Do not queue duplicates.**

| Claim | Live retest | Tagging / DV | Note |
|---|---|---|---|
| **ARC-062** | V3-EXQ-654g (ree-cloud-4, claimed) | claim_ids=[MECH-309, ARC-062]; PRIMARY DV committed-class entropy lift >=2/3 | ports GAP-B falsifier onto the 569i top-k shortlist + matured CRF stack. Known thin-margin risk (569i 2/3-seed). If C2 fails -> deeper F-dominance ceiling (still (b)), not a falsification. |
| **MECH-309** | V3-EXQ-654g (same run) | co-tagged | SD-056 (named substrate) is one fixed prerequisite, not the lift; real ceiling is F-dominance conversion. |
| **SD-033b** | V3-EXQ-485h (ree-cloud-2, claimed) | claim_ids=[SD-033b, MECH-263] | records devalued-state + per-context OFC bias range (T-vs-F disambiguator) + optional live-E3 (authority-ON) arm. V3-EXQ-485g showed a genuine 0.171 bias range with ZERO behavioural conversion -- the conversion ceiling. Will NOT promote by design (below-floor -> substrate_not_ready_requeue). |
| **MECH-263** | V3-EXQ-485h (same run) | co-tagged | adjudicated together with SD-033b. |

---

## (b) STILL CEILINGED -- parked deferral marker applied

Each keeps `substrate_ceiling` + `pending_retest_after_substrate`. A `ceiling_decision: deferred`
+ `ceiling_routing_note` marker was added (after `registered_utc`, or after
`pending_retest_after_substrate` where no `registered_utc` line exists). The note records the real
blocker so the audit does not re-derive it every cycle. **No claim status / v3_pending changed.**

### MECH-307 group (SD-015, SD-049, MECH-295) -- MECH-307 is a spurious / confound-only match

- **SD-015** -- MECH-307 only cleared the mixed-affect-stream confound on 514f/514k evidence; it
  does not deliver z_resource-encoder-driven goal navigation. Real blocker = foraging-competence +
  z_goal-formation quality on the SD-049 reef (~0.2% consumption, `failure_autopsy_V3-EXQ-514l`).
  Encoder representation is validated (085l prox_r2=0.908; EXQ-182a oracle 11.14x). Route to
  **/implement-substrate** (scaffolded_sd054 foraging scaffold port), not a MECH-307 retest.
- **SD-049** -- MECH-307 is orthogonal (anticipatory-affect amendment). Phase-2 V3-EXQ-514
  validation blocked on the same ~0.2% consumption. Cohort drive-coupling lineage (MECH-229/436,
  514n-514t) is live but SD-049's own 4-arm validation is deferred pending a foraging-competent
  policy. Route to **/implement-substrate** foraging scaffold.
- **MECH-295** -- `goal_pipeline:GAP-4` was **CLOSED 2026-06-09** (necessity reading falsified by
  V3-EXQ-490j; modulatory reading substrate-supported by 490j/493). The ceiling flags are retained
  only for the **optional, non-GAP-blocking** 490L modulatory-sufficiency retest, gated on
  scaffolded_sd054 (collapsed-candidate / weak z_goal), NOT on MECH-307. Cleanest deliberate-defer.

### SD-037 axis-b group (MECH-280, MECH-281) -- plumbing landed, zero baseline to act on

- **MECH-280** -- SD-037 `broadcast.override_regulator` is wired (483b PAG release 1.875x) but its
  multiplicative gain has a **zero committed-freeze baseline** -- PAG never engages at fishtank
  z_harm_a (483e: pag_release=0/12). Co-gated on the SD-037 axis-b thread
  (`sd_037_axis_b_sustained_threat_curriculum_plan.md`): terminal retest V3-EXQ-483f is
  reserved/blocked behind **V3-EXQ-625e** (GAP-A conversion-propagation-under-threat). 625d already
  FAILed/self-routed substrate_not_ready 2026-06-18.
- **MECH-281** -- co-gated with MECH-280. Consumer outputs (BLA/CeA/BetaGate) all zero at fishtank
  baseline (483e) so SD-037's gain has nothing to scale; cataplexy/PWS dissociation unreachable.
  Needs env enrichment driving z_harm_a above BLA/CeA input thresholds, not more fishtank runs.

### MECH-262 -- consumer implemented, upstream rule-creator missing

- **MECH-262** -- SD-033a `pfc.lateral_pfc_analog` (consumer) is implemented and PASSes
  distractor-resistance (484), but rule-**selective** persistence is untestable until an upstream
  rule-creator emits **differentiated (non-monomodal)** rule_state. That producer =
  `arc_062_rule_apprehension:GAP-B` / `behavioral_diversity_isolation:GAP-A` (V3-EXQ-598b C3 FAIL
  trainable_not_monomodal; latest GAP-B falsifier V3-EXQ-654f FAIL/non_contributory 2026-06-18,
  654g successor in flight). Retest only after a GAP-B PASS (acceptance ~598c). Do not requeue on
  SD-033a alone.

### Modulatory-bias group (MECH-294) -- scalar signal the authority cannot carve

- **MECH-294** -- modulatory-bias-selection-authority is implemented but cannot carve MECH-294:
  `currency_coherence` is a **scalar** (rescale-invisible), so the route-range authority and the
  569i top-k shortlist have no per-candidate range to act on (V3-EXQ-661: committed-distribution
  TV ~0 incl gate-ON vs gate-OFF). Needs a prior **/implement-substrate** wiring step (express
  binding-coherence as cross-candidate range) before any behavioural falsifier. Primary lit
  falsifier (Kay-2020 cross-cycle theta) is out-of-substrate for V3.

### Singletons (MECH-189, SD-032b, ARC-046, MECH-334)

- **MECH-189** -- INF-ENV-003 transient-benefit-patch **salience** is orthogonal to the real
  blocker, `goal_pipeline:GAP-2` z_world **context-diversity**: the super-ordinal anchor store
  saturates to <=1 via merge_similarity collapse on near-identical nursery contexts
  (`failure_autopsy_V3-EXQ-669a/669b`). No context-diversity substrate built or in flight.
- **SD-032b** -- MECH-269 per-region V_s landing is "implemented" but
  `post_implementation_validation_status: wired_but_inert` on this env and has been **superseded**
  as the operative blocker by the F-dominance conversion ceiling (MECH-439). dACC c2
  (committed-action-entropy shift) is floor-locked because committed-action diversity does not
  exist (445h: action_class_entropy=0.0 all arms). Retest gated on the live MECH-439/GAP-A top-k
  front (in flight as V3-EXQ-654g, though not SD-032b-tagged); never re-run on the 445h surface.
- **ARC-046** -- the own-id Phase-0->1 gate-fix substrate landed and its (c-2) crossing-count
  criterion was wired 2026-06-19 (591f; commit b4dc264), but GAP-14 STAYS blocked on (c-1) seed-46
  exploration-strength collapse -- the Q-043 magnitude lever is **exhausted** (V3-EXQ-667 FAIL:
  4/5 seeds byte-identical across 8x knob scaling -> zero E3 selection authority), blocked on
  modulatory-bias-selection-authority / GAP-A. Queue 667a first; do not queue EXQ-ISEF-005 on the
  (c-2)-cleared signal alone. **Side flag:** the 591 manifest still carries `does_not_support`
  (scored `weakens`, exp_conf 0.274) despite the claims.yaml `non_contributory` assertion -- a
  separate evidence-record drift to fix (chip spawned).
- **MECH-334** -- the test_bed_enrichment destabilising-pressure env was built but is **not** the
  operative blocker: crystallization-necessity cannot be exercised until ARC-062/MECH-333 produce a
  functionally-differentiated GatedPolicy at the Phase-3 boundary (same GAP-B front as MECH-309,
  654g). Also fix the recurring harness no-op (assert policy trained + `ewc_penalty` in loss +
  true-negative ARM_0: entropy_bonus=0 / noise-floor-off / E3-diversity-off) burned across
  610c-f / 655 (chip spawned).

---

## Recommended next actions (await user confirmation before any state change / queue)

1. **(c) cohort (ARC-062, SD-033b, MECH-263, MECH-309):** no action -- let V3-EXQ-654g / 485h score,
   then governance reconciles `pending_retest_after_substrate`.
2. **Substrate-build / wiring routes:** MECH-294 -> `/implement-substrate` (express binding-coherence
   as per-candidate range; do NOT queue an experiment first). SD-015 + SD-049 -> **CORRECTION
   (2026-06-19T19:51Z):** their foraging-competence scaffold is already BUILT --
   `scaffolded_sd054_onboarding` is `ready=true` (flipped 2026-06-11, V3-EXQ-603n PASS) and its
   substrate_queue note states the SD-049 Phase-2 / V3-EXQ-514l-successor validation is "now
   queueable". So the next action is `/queue-experiment` (the 4-arm SD-049 Phase-2 behavioural
   validation on the ready scaffold), NOT an `/implement-substrate` foraging-scaffold build.
   Spawned as chip `task_8d6d977b`. MECH-294 spawned as chip `task_e8bd8fee`.
3. **Gated-on-upstream (no action until the upstream front resolves):** MECH-280/281 (625e ->
   483f), MECH-262 (654g GAP-B PASS), SD-032b + ARC-046 (MECH-439 / GAP-A), MECH-334 (GAP-B + harness fix).
4. **Stalled / no owner:** MECH-189 needs a `goal_pipeline:GAP-2` context-diversity substrate that
   does not yet exist -- candidate for a future /implement-substrate design pass.
5. **MECH-295:** keep deferred (GAP-4 closed; only the optional 490L remains).
6. **Optional follow-up:** consider whether the 11 spurious `unblocks_claims` listings should be
   repointed in `substrate_queue.json` (substrate-design edit, out of scope here) so the audit stops
   matching the wrong substrate at the source -- the parked markers are the interim mitigation.

Two evidence-record side issues (ARC-046 591 manifest direction; MECH-334 harness no-op) are
spawned as separate background tasks.
