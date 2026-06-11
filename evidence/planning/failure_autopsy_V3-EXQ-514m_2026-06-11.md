# Failure Autopsy — V3-EXQ-514m (MECH-229 wanting≠liking = 0.0)

- **Generated (UTC):** 2026-06-11T14:19:54Z
- **Scope:** single target (MECH-229 axis of a mixed-direction run)
- **Status:** confirmed (user-adjudicated Step-8, 2026-06-11)
- **Run:** `v3_exq_514m_sd049_phase2_behavioural_curriculum_built_20260611T131105Z_v3`
- **Queue id:** V3-EXQ-514m · **supersedes** V3-EXQ-514l · **machine** DLAPTOP-4.local
- **Claims tagged:** MECH-229 (this autopsy), MECH-230 (supports — sound, not autopsied)

## Headline

**C_WL = 0.0 in V3-EXQ-514m is a vacuous FAIL, not a genuine MECH-229 weakening.** The two
valence channels the wanting≠liking DV compares (`VALENCE_WANTING` index 0, `VALENCE_LIKING`
index 1) have **no active write path** in this run's config and custom eval loop, so the
dissociation is structurally incapable of being expressed. The contact-guard non-vacuity gate
(the script's only readiness check) does not cover the WL DV's own degeneracy. The MECH-229
per-claim `weakens` is reclassified **non_contributory** (`measurement_test_design_defect`);
`pending_retest_after_substrate=[MECH-229]` retained. This confirms governance cycle #3's
scoring-exclusion of the MECH-229 weakens was correct.

MECH-230 (supports) is **unaffected** and sound — see below.

## Facts (manifest + script + agent code)

- Outcome FAIL / `evidence_direction=mixed`; `evidence_direction_per_claim`
  MECH-229=weakens, MECH-230=supports.
- Contact-guard non-vacuity **met**: 2/3 seeds pass (`per_seed_guard_pass=[true,true,false]`).
  Seed 42 contact_rate 0.293 / z_goal@contact 0.522; seed 43 0.369 / 0.414; seed 44 fails
  guard (z_goal@contact 0.395 < 0.4) → excluded from DV aggregation.
- **C_ID (identity recovery) PASS** — `mean_probe_acc_neighborhood`=0.926,
  `n_identity_samples_neighborhood_total`=3455 (≥30 floor, ≥0.6 floor). Genuine, contact-guarded.
- **C_ANOVA (per-axis drive) PASS** — `per_axis_drive_anova_f_max`=1096 ≫ F_crit 4.605.
- **C_WL (wanting≠liking) FAIL** — `mean_wanting_liking_dissoc_fraction`=**0.0**, and the
  per-seed `wanting_liking_dissoc_fraction` is **0.0 on all three seeds with zero variance**.
  DV2 = fraction of goal-active steps with
  `|evaluate_valence(z_world)[VALENCE_WANTING] − [VALENCE_LIKING]| > WL_DELTA(0.1)`.

## The decisive code trace

`_make_config` (514m script, lines 241–275) sets `cfg.residue.valence_enabled=True` but does
**not** set `valence_liking_enabled`, `tonic_5ht_enabled`, or `schema_wanting_enabled`.

In `ree-v3/ree_core/agent.py` the residue valence channels the DV reads are written only by
gated methods, all of which are disabled here:

- **VALENCE_WANTING** (index 0):
  - `update_benefit_salience` → `serotonin.benefit_salience(...)` (serotonin/tonic_5ht path) — **off**.
  - `update_schema_wanting` (MECH-216) — gated `schema_wanting_enabled` (agent.py:7102) — **off**.
  - MECH-290 `backward_credit_sweep` — gated `use_backward_credit_sweep` — **off**.
- **VALENCE_LIKING** (index 1):
  - `update_liking` — gated `valence_liking_enabled` (agent.py:7055) — **off**.
  - MECH-295 bridge liking write — gated `... and valence_liking_enabled` (agent.py:4219/4248) — **off**.

The experiment's **custom** `_run_behavioural_eval` loop (lines 351–470) never calls any
writer method (unlike `experiments/_harness.py:StepHarness`, which calls
`update_schema_wanting` at line 277). It only reads `evaluate_valence(latent.z_world)`.

Net: `VALENCE_WANTING ≡ 0` and `VALENCE_LIKING ≡ 0` at every node →
`|0 − 0| ≤ 0.1` → the dissociation step counter never increments →
`wl_fraction = 0.0` **deterministically**, on every seed, independent of behaviour. The
byte-identical 0.0 across all three seeds is the tell — a genuine behavioural dissociation
measure would show seed variance.

## The self-route is unverified (vacuous-criterion pattern)

The script's scoring (lines 660–683) sets `dir_mech229 = "supports" if c_wl else "weakens"`
whenever `non_vacuity_met=True`. But `non_vacuity_met` checks **only** the contact guard
(did the seed reach self-sustaining foraging contact) — it does **not** verify that the
wanting/liking channels were ever written. The contact guard correctly fixed 514l's
contact-starvation false-weakens, but has a blind spot: it does not gate the WL DV's own
degeneracy. This is the canonical "vacuous PASS/FAIL" hazard
(`feedback_diagnostic_self_route_is_hypothesis`; cf. V3-EXQ-642 vacuous comparator, 660a
saturated readout). The self-routed `weakens` is built on an unmet non-degeneracy assumption.

The pre-registered SD-049 verdict grid row
(`targeted_review_sd_049_encoder_identity_expansion/verdict.md:75`,
"identity-recovery PASS, wanting≠liking FAIL → trunk under-trained") **does not apply**: it
assumes the WL DV is a non-vacuous read of trunk similarity structure. That precondition is
unmet — the DV reads silent residue channels, not the trunk.

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | the test could not let MECH-229 express — wanting channel never written |
| Biological reference | clear | Berridge & Robinson 2003 wanting≠liking; working existence proof for the class |
| Prerequisites / dependency | present | the onboarding curriculum delivered foraging competence (514l's ceiling is lifted; 2/3 seeds clear contact) |
| Implementation | **partial (load-bearing)** | config omits `valence_liking_enabled`/`tonic_5ht_enabled`/`schema_wanting_enabled`; custom eval loop omits all writer calls |
| Environment | adequate | SD-049 Phase-2 multi-resource env present; identity + per-axis drive both genuinely measured |
| Measurement | **misleading (load-bearing)** | DV reads channels with no write path → 0.0 is an instrument artifact, not behaviour |
| Integration | n/a | — |
| Scale | adequate | n=3455 identity samples; contact achieved |

**Recommended `epistemic_category`:** `measurement_test_design_defect` (not `substrate_ceiling`
— the substrate is not the limiting factor; the instrumentation is).

## MECH-230 (not autopsied — recorded sound)

C_ID (neighborhood probe 0.926, n=3455) and C_ANOVA (F≈1019) are genuine and contact-guarded.
MECH-230=supports stands. Minor secondary note: the **consumption-phase** identity probe is
0.0 at n=5/6/8 — that is the `_identity_recovery_probe` n<10 floor (too few samples), a
distinct readout from the neighborhood probe that drives C_ID, and it does not bear on either
claim's direction. Not load-bearing; flagged for the 514n successor to instrument more samples.

## Learning extracted

1. **Discovered instrumentation gap:** the 514-lineage wanting≠liking DV depends on the SD-014
   residue valence channels being written, but 514m disables every `VALENCE_WANTING`/
   `VALENCE_LIKING` write path. A contact-guarded run can still produce a vacuous C_WL=0.0.
2. **Generalizable test-design rule:** the contact guard is necessary but insufficient for the
   WL DV — a **same-statistic WL-channel non-vacuity gate** is required (assert the wanting and
   liking targets were actually defined / channels nonzero before scoring C_WL, else
   `substrate_not_ready_requeue`, never a false weakens). Mirrors the V3-EXQ-643 same-statistic
   readiness lesson.
3. **Substrate-faithful redesign (user-confirmed direction):** the genuine, forward-compatible
   MECH-229 test on the current substrate is the **SD-057 object-bound wanting-target ≠
   liking-target** dissociation (`use_incentive_token_bank=True` is already on in 514m), not the
   legacy residue-valence magnitude read that the SD-049 verdict flagged as substrate-degenerate.
   This is the non-degenerate identity-distinct test the verdict pre-registered ("approach
   target_A while target_B is what it would consume for satiation"), and it sits on the live
   forward affect substrate (MECH-346 most-wanted z_goal pointer; the V4/V5 affect roadmap).

## Routing (user-confirmed)

- **MECH-229 = non_contributory** (was per-claim weakens). `measurement_test_design_defect`.
  Retain `pending_retest_after_substrate=[MECH-229]`. `narrow_supports_flag=true` (remaining
  supports EXQ-074f/234/354 are degenerate single-resource per the claim's own
  evidence_quality_note; no genuine multi-resource support exists).
- **Route: `/queue-experiment`** — a **V3-EXQ-514n** successor (alphabetic; same scientific
  question, corrected instrumentation) that:
  1. measures the **SD-057 bank** wanting-target (most-wanted z_goal pointer, MECH-346) vs
     liking-target (last-consumed object) dissociation directly; and
  2. adds a **same-statistic WL non-vacuity readiness gate** (bank populated ≥2 distinct object
     tokens at differing per-axis drives AND both wanting- and liking-targets defined on the
     scored steps) — below floor → `substrate_not_ready_requeue`, never a false weakens; and
  3. retains the 514m contact guard and increases consumption-phase identity sampling.
- **substrate_queue:** `action=none`. This is an instrumentation/test-design defect routed to
  `/queue-experiment`, not `/implement-substrate`. The SD-057 substrate is already landed
  (2026-06-04); no new substrate work is implied.
- **No demotion.** MECH-229 stays `provisional` (the mechanism is not refuted; it was not
  tested under conditions where it could express). Governance applies the manifest reclassify.

## Draft `evidence_quality_note` for governance to write (verbatim)

> 2026-06-11 (failure_autopsy_V3-EXQ-514m): the MECH-229 per-claim `weakens` is reclassified
> **non_contributory** (`measurement_test_design_defect`) and remains scoring-excluded.
> V3-EXQ-514m C_WL wanting≠liking dissoc = 0.0 on all 3 seeds (zero variance) is a **vacuous
> FAIL**: the DV compares the SD-014 residue `VALENCE_WANTING` (idx 0) and `VALENCE_LIKING`
> (idx 1) channels, but the run's config omits `valence_liking_enabled`/`tonic_5ht_enabled`/
> `schema_wanting_enabled` and the custom eval loop calls no valence-writer method, so both
> channels are identically zero at every node and `|w−l|>0.1` can never fire — independent of
> behaviour. The contact guard (the run's only non-vacuity gate) verifies foraging but not
> that the wanting/liking channels were written, so the self-routed `weakens` rests on an
> unmet non-degeneracy assumption (vacuous-criterion pattern; cf. V3-EXQ-642/660a). C_ID
> (0.926, n=3455) and C_ANOVA (F≈1019) are genuine and contact-guarded → MECH-230=supports
> stands. MECH-229 stays `provisional`, `pending_retest_after_substrate=[MECH-229]`,
> `narrow_supports_flag=true`; the prior 074f/234/354 supports are degenerate single-resource.
> Retest = V3-EXQ-514n: measure the SD-057 object-bound wanting-target ≠ liking-target
> dissociation (`use_incentive_token_bank` already on) with a same-statistic WL non-vacuity
> readiness gate. No demotion; no substrate_queue create/amend (instrumentation defect, not a
> substrate ceiling; SD-057 substrate already landed 2026-06-04).
