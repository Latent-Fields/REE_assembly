# Failure Autopsy -- V3-EXQ-603l (SD-059 / MECH-358 escape-affordance bridge behavioural retest)

- **Generated (UTC):** 2026-06-10T16:21:34Z
- **Scope:** single
- **Status:** confirmed (user adjudicated 2026-06-10)
- **Run:** v3_exq_603l_escape_affordance_bridge_behavioural_retest_20260610T134941Z_v3
- **Queue id:** V3-EXQ-603l
- **Claims:** SD-059 (design_decision, candidate), MECH-358 (mechanism_hypothesis, candidate)
- **Manifest self-route:** outcome=FAIL, evidence_direction=weakens, interpretation.label=`bridge_insufficient_env_survivable`
- **Machine:** ree-cloud-2

## Self-route under adjudication

The pre-registered grid routed to `weakens` because `readiness_met=true` AND primary FAIL
AND `ARM_NAV_CONTROL` clears G_H (env survivable). This skill adjudicates that self-route:
the route conflates "the bridge added no measurable *binary-survival* headroom" with "the
bridge mechanism fails." It is not trustworthy. Correct reading: **non_contributory --
test-design + measurement ceiling.**

## 1. Facts (no interpretation)

Failed criterion = the **discrimination** criterion `best_bridge_G_H_frac > G_H_BASE_frac`.

| Arm | bridge | G_H_frac | hazard mean-ep-len (per seed) | relief credit | safety credit | approach fires |
|---|---|---|---|---|---|---|
| ARM_BASE_IA_ONLY | OFF | **1.0** | 69 / 138 / 87 (~98) | 0/0/0 | 0/0/0 | 0 |
| ARM_RELIEF_BRIDGE | relief | 0.667 | 92 / 44 / 123 | 299/69/426 | 0 | 3771/894/2868 |
| ARM_SAFETY_BRIDGE | safety | 0.667 | 115 / 74 / 76 | 0 | 1095/10/462 | 869/1238/954 |
| ARM_RELIEF_SAFETY_BRIDGE | both | **1.0** | **161 / 166 / 69 (~132)** | 351/400/73 | 2286/2880/18 | 7165/3494/6128 |
| ARM_NAV_CONTROL | OFF (spawn-in-reef) | 0.667 | 20 / 59 / 92 | 0 | 0 | 0 |

Key manifest flags: `readiness_met=true`, `pavlovian_reaction_present=true`, `gate_engaged=true`,
`bridge_halves_nonvacuous=true`, `nav_control_clears=true`, `best_bridge_clears=true`,
`best_bridge_beats_base=false`, `criteria_non_degenerate` all true.

Facts that matter:
- **Base is at the binary survival ceiling (G_H_BASE_frac = 1.0, 3/3).** The pre-registered
  PRIMARY requires `best_bridge > base`; with base at 1.0 this is **structurally
  unsatisfiable** -- a bridge arm can at best TIE (which the both-arm did).
- The bridge **fired non-vacuously** in every enabled arm (relief credit 299-426; safety
  credit up to 2880; approach bonus thousands of fires). Readiness preconditions met.
- **Continuous benefit the binary gate cannot see:** ARM_RELIEF_SAFETY_BRIDGE hazard-stage
  *mean* episode length ~132 (161/166/69) vs base ~98 (69/138/87) -- ~35% longer sustained
  survival, masked by the binary median>=75 gate saturating at 1.0 for both arms.
- Single-half arms each dropped one seed (0.667). This is seed-level survival noise around a
  hard hazard, scattered across ALL arms (base seed-43 only median 103; nav_control seed-42
  died) -- not a bridge-harm signature.
- **No reckless-approach signal:** more approach fires correlated with LOWER contact rate
  (both-arm 0.147/0.133 vs base 0.20-0.34) and LONGER survival -- the approach bonus steers
  toward escape-affordance classes, the opposite of risky approach-to-threat.

## 2. Claim-layer mapping

- **SD-059** (candidate, design_decision, epistemic_category=standard, v3_pending): the
  architecture adding an affordance-indexed relief/safety credit table over the MECH-357
  scalar gate. depends_on SD-058/MECH-357/MECH-302/303/304/SD-011/MECH-279 -- all implemented,
  validations 603h/603j/603k green.
- **MECH-358** (candidate, mechanism_hypothesis, standard, v3_pending): the bridge mechanism
  (relief half, safety half, threat-gated negative E3 approach bias). Same bridge as SD-059;
  they move together.
- **Did the test let the claim express itself? NO.** The base arm was raised to the binary
  survival ceiling by the readiness-enabling substrate fix (603k), removing the headroom the
  bridge needs to demonstrate added value, and the binary metric saturated. See Section 4.
- **claim_ids accuracy:** correct. SD-059/MECH-358 are the same bridge; the run genuinely
  exercises both. 603l is the ONLY scored evidence tagging either claim (603i/j/k were
  diagnostic, claim_ids=[]).

## 3. The two coupled confounds

**Confound A -- the readiness-enabling fix removed the deficit under test.**
SD-059's motivating deficit (V3-EXQ-603h: agent un-freezes but acquires no directed escape,
seed-43 scalar efficacy 0.633 -> WORST survival 11.0) was observed on an *untrained-harm-pathway*
substrate. V3-EXQ-603k harm-pathway training -- added so the nav/survival-competence ceiling
would clear and the test could run -- trains `E3.harm_eval(z_world)`. Per ARC-007-strict,
**E3's harm gradient is what picks the escape direction**; the SD-059/MECH-358 bridge only adds
an approach bonus on top of that gradient. So 603k alone restored directed escape and saturated
base survival. The fix that made the test *scorable* also removed the deficit the bridge
addresses -- a confound between the test-enabling substrate fix and the mechanism under test.

**Confound B -- binary G_H saturates (measurement ceiling).**
With base at 1.0 there is no binary headroom. The only graded benefit (both-arm ~35% longer
mean hazard-stage episode length) is invisible to the binary median>=75 gate.

Together these are the canonical substrate/test-design ceiling fingerprint: **absolute /
negative-control criteria pass (base survival 3/3; nav_control 2/3), the discrimination
criterion fails.**

## 4. Biological-reference triage

- Closest mechanism: **Moscarello & LeDoux 2013** active avoidance -- the LA/BA->NAcc
  relief/safety action-credit half that positively reinforces a SPECIFIC avoidance response
  (complementing the CeA/PAG reaction-suppression half). Supporting: Debiec & Sullivan 2017
  (gradual acquisition).
- This is a **faithful biological translation**, NOT a formal-definition import. The mechanism
  class has a working biological existence proof. Lit status: present (primary literature cited
  on both claims); no lit-pull commission needed.
- Does the failure match a missing-dependency signature? No -- it matches a *removed-deficit +
  saturated-metric* signature. The biology supports the mechanism class; the FAIL is a
  test-design / measurement gap, NOT a falsification. (Demotion threshold -- tested fairly +
  biology supports + still fails -- is NOT reached: the test was not fair, base was at ceiling.)

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (NOT weakened) | test could not let the claim express itself; base at ceiling, metric saturated |
| Biological reference | clear | Moscarello & LeDoux 2013 relief/safety action-credit; faithful translation; biology supports the class |
| Prerequisites | present (over-shot) | all depends_on green; the 603k readiness fix over-corrected, removing headroom |
| Implementation completeness | complete | relief + safety credit + approach bonus all fire non-vacuously; readiness met; gate engages; PAG freezes |
| Environment adequacy | wrong pressures / too easy | survivable by base alone on the 603k+603j substrate -- DOMINANT gap |
| Measurement adequacy | under-instrumented / misleading | binary G_H saturates; continuous metric shows the both-arm lift -- CO-DOMINANT gap |
| Integration adequacy | coupled | bridge integrates with E3 / MECH-357 gate; fires correctly |
| Scale / capacity | adequate | -- |

Dominant diagnosis: **environment adequacy + measurement adequacy (coupled)**. Recommended
`epistemic_category`: **standard (unchanged)** -- this is a test-design gap, not a
substrate-too-coarse condition, so `substrate_ceiling` is NOT the right tag.

## 6. Learning extracted

1. A readiness-enabling substrate fix can silently remove the deficit the experiment is meant
   to measure. When P0/scaffold training trains a pathway (here E3.harm_eval) that *is* the
   competence under test, the base arm saturates and the mechanism under test loses its
   headroom. Future bridge/add-on retests must keep the base arm at the deficit level the
   add-on targets (or isolate the add-on against the un-fixed base).
2. A binary survival gate (median episode length >= 75) saturates exactly where a graded
   benefit lives. Add-on mechanisms that improve *sustained* survival need a continuous metric
   (mean/median hazard-stage episode length, time-to-first-death, AUC-survival).
3. The both-arm's longer mean episode length + lower contact rate is positive (if seed-thin)
   evidence the bridge works as designed -- it should not be discarded as a weakens.

## 7. Repair pathway (user-confirmed 2026-06-10)

- **evidence_direction: `non_contributory`** (NOT weakens). Governance corrects the manifest
  direction + adds the note below; rebuild the index.
- **Routing: `/queue-experiment` redesign** carrying BOTH fixes (user choice "Both"):
  (a) **headroom** -- harder / intermediate hazard regime (or partial harm-pathway training)
      so ARM_BASE_IA_ONLY sits at G_H ~0.33-0.67 with measurable headroom; and
  (b) **continuous survival metric** -- mean/median hazard-stage episode length (and/or
      time-to-first-death) as the primary discrimination metric, supplementing binary G_H.
  New letter (603m / 603n already taken -> 603o or governance/queue-experiment assigns).
- **Illusory-conflict check:** SD-059/MECH-358 have ZERO other scored evidence; reclassifying
  this weakens to non_contributory does not resolve any conflict (no opposing supports pile).
  The claims remain `candidate` / unproven. `narrow_supports_flag: true`,
  `pending_retest_after_substrate: true` (retest is a test-design REDESIGN, not new substrate --
  see note).
- No substrate_queue entry, no lit-pull.

### Draft `evidence_quality_note` (governance to write -- do not write here)

> V3-EXQ-603l (first scored evidence) self-routed `weakens` (bridge_insufficient_env_survivable)
> but is reclassified `non_contributory` by failure_autopsy_V3-EXQ-603l_2026-06-10: the
> discrimination criterion `best_bridge_G_H > G_H_BASE` was structurally unsatisfiable because
> the readiness-enabling 603k harm-pathway-training fix raised ARM_BASE_IA_ONLY to the binary
> survival ceiling (3/3), removing the bridge's headroom, and the binary G_H gate saturated.
> The bridge fired non-vacuously (relief/safety credit + approach bonus) and ARM_RELIEF_SAFETY_BRIDGE
> showed ~35% longer mean hazard-stage episode length than base -- a graded benefit invisible to
> the binary gate. Biology (Moscarello & LeDoux 2013 active-avoidance relief/safety action-credit)
> supports the mechanism class; demotion threshold not reached. NOT promotable; retest pending a
> REDESIGN EXQ (headroom-restoring hazard regime + continuous survival metric), not new substrate.

## 8. Routing summary

| Field | Value |
|---|---|
| failed_criterion | discrimination (`best_bridge_G_H_frac > G_H_BASE_frac`) |
| recommended_evidence_direction | non_contributory |
| recommended_epistemic_category | standard (unchanged) |
| dominant diagnosis | environment adequacy + measurement adequacy (coupled test-design ceiling) |
| biological verdict | faithful translation; class supported; not falsified |
| routing | queue-experiment (redesign: headroom + continuous metric) |
| substrate_queue | none |
| narrow_supports_flag | true (zero other scored evidence) |
| pending_retest_after_substrate | true (redesign retest, not substrate) |
