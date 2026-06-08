# Failure autopsy -- V3-EXQ-603h (SD-058/MECH-357 Stage-H avoidance-gate insufficient)

**Generated:** 2026-06-08T06:56:26Z
**Scope:** single
**Status:** confirmed (user-reviewed 2026-06-08)
**Run:** `v3_exq_603h_instrumental_avoidance_stageh_validation_20260607T211923Z_v3` (ree-cloud-3)
**Outcome:** FAIL | `evidence_direction: non_contributory` | `experiment_purpose: diagnostic` | `claim_ids: []`
**Validates (not weakens):** SD-058 (architecture) + MECH-357 (ilPFC-analog freeze-suppression + instrumental-avoidance action pathway + eligibility-trace efficacy learning)
**Routing autopsy input:** user's personal hypothesis,
`evidence/planning/thought_intake_2026-06-07_relief_safety_escape_affordance_bridge.md`

---

## 1. Scope

Single-target adjudication of a substrate-readiness diagnostic. 603h is the literal
Moscarello & LeDoux lesion-vs-intact validation of SD-058/MECH-357 on the
scaffolded_sd054_onboarding Stage-H survival/hazard-avoidance leg (2 arms x 3 seeds;
both arms carry MECH-279 PAG tuned to z_harm_a~0.34 and the fed harm stream; the only
difference is the ilPFC instrumental-avoidance gate). It is claim-free
(`claim_ids: []`), so it weakens nothing in governance scoring; its output is a
substrate-gap discovery.

Pre-registered in the thought-intake routing table (Section 3): the
**engaged-but-insufficient** cell ("gate engaged + G_H fails") is the branch that
routes this thought as a candidate failure-autopsy. 603h landed exactly in that cell.

## 2. Reconstruction -- facts only

**Self-route is trustworthy (not a precondition_unmet / vacuous_pass case):**

- `readiness_met: true`. All three non-vacuity preconditions passed:
  - `pavlovian_freeze_reaction_present_on_lesion` -- measured 1.0 (PAG freezes on all
    LESION seeds; pag_n_commits 316/149/444; `pag_freeze_frac=1.0`).
  - `ilpfc_gate_engages_and_suppresses_freeze_on_intact` -- measured 1.0
    (`gate_engaged_frac=1.0`, `gate_freeze_suppressed_frac=1.0` on all INTACT seeds).
  - `stage0_forced_feed_lights_zgoal_on_intact` -- measured 0.667 (>= 2/3).
- `criteria_non_degenerate`: `both_arms_reached_hazard_stage`, `pavlovian_freeze_present`,
  `gate_active_on_intact` all true.
- **Load-bearing primary criteria FAILED:** `G_H_INTACT_clears_2of3 = false`
  (`g_h_intact_frac = 0.0`), `G_H_INTACT_beats_LESION = false` (both 0.0).

Failed criterion class: **discrimination** (the lesion-vs-intact survival contrast),
with all readiness/non-vacuity controls cleared. This is the substrate-ceiling /
engaged-but-insufficient fingerprint, not a vacuous test.

**Per-seed INTACT disambiguator (the load-bearing signal):**

| INTACT seed | avoidance_efficacy | n_credit | n_decay | n_freeze_suppressed | hazard median (last 10) | stage0 z_goal |
|---|---|---|---|---|---|---|
| 42 | ~0 (6.9e-44) | 6 | 15566 | 65 | 34.5 | lit |
| 43 | 0.633 | 1126 | 4198 | 268 | **11.0 (worst of all 6)** | NOT lit (0.3998) |
| 44 | 0.0 | 0 | 15356 | 75 | 22.5 | lit |

LESION hazard medians: 27.5 / 16.5 / 19.0. Gate-vs-no-gate survival is a wash
(INTACT marginally higher on 2/3 seeds, lower on seed 43).

Two facts read directly off `ree_core/pfc/infralimbic_avoidance_gate.py`:

1. **Freeze-suppression half works; relief/credit half is starved.** The gate's
   `should_suppress_freeze` fired on all 3 seeds (`n_freeze_suppressed` 65/268/75) --
   the agent *can* move under threat. But the efficacy-credit event in `update()`
   (a *directed* action under threat that *drops* z_harm_a: `delta = prev - z_now >
   efficacy_reward_floor`) almost never fired on 2/3 seeds (`n_credit` 6 and 0 vs
   `n_decay` ~15.5k). The relief event -- harm actually falling after a directed
   action -- essentially never occurred there, so `avoidance_efficacy` collapsed to ~0.

2. **Where efficacy DID accumulate, it did not buy survival.** Seed 43 reached
   efficacy 0.633 (n_credit 1126, n_freeze_suppressed 268) and survived **worst**
   (11.0). Structural reason: `compute_action_bias` only **penalises the no-op/freeze
   class** proportional to a **scalar** `effective_efficacy * threat_scale`, and by
   design *"does NOT compute the escape direction"* -- it leans on "E3's existing harm
   gradient" to pick among the directed candidates. So a high scalar efficacy un-freezes
   the agent and biases it to *act*, but binds no **specific** action/location/policy to
   relief. There is no escape *affordance*, only a global "avoidance works" scalar.

This is the user's Section 3 prediction verbatim: REE learned to **twitch away from
freeze without learning that a particular action/location/policy is a relief/safety
affordance.**

## 3. Claim-layer mapping

| Claim | Type | Status | What 603h shows |
|---|---|---|---|
| SD-058 | defensive_action architecture | candidate / v3_pending | gate engaged + suppressed freeze (readiness met) -- did what it claims |
| MECH-357 | ilPFC freeze-suppression + avoidance action pathway + efficacy trace | candidate / v3_pending | suppression half operative; scalar-efficacy half decoupled from survival |

The FAIL is **downstream of** SD-058/MECH-357, not against them. MECH-357 never
claimed to construct a directed escape -- it claims freeze-suppression + a scalar
acquisition trace, both confirmed present. Both claims stay candidate / v3_pending,
**unweakened** (and `claim_ids=[]` means nothing is touched in scoring regardless).
Do not let the survival FAIL falsify the freeze-suppression claim.

## 4. Biological-reference triage (core move)

Closest reference: **Moscarello & LeDoux 2013** active avoidance = ilPFC suppresses
CeA/PAG freezing **AND** an LA/BA -> **NAcc** action pathway where CS-termination /
response-produced safety positively reinforces a *specific* avoidance response. The
modern literature (LeDoux/Moscarello/Sears & Campese 2017; Boeke/Phelps/Hartley 2017)
frames the reinforcer as circuit-level threat-removal + safety acquisition, NOT
subjective relief -- complementary contributors.

REE implemented the **suppression** half (MECH-357 ilPFC gate). It did **not**
implement the **NAcc relief/safety-credit -> approachable-affordance** half. The 603h
FAIL **matches the missing-dependency signature** of the reference mechanism: with the
suppression intact but the directed-credit bridge absent, the animal un-freezes but
does not acquire a directed escape -- a discovered prerequisite, not a falsification.

**REE already owns the relief and safety primitives, but they are not wired to
avoidance:**

- MECH-302 / SD-050 (suffering-derivative comparator, "Relief"): fires on z_harm_a
  descent -> commitment-release + VALENCE_LIKING write at the **current** z_world.
- MECH-303 / SD-052 (contextual passive safety terrain) + MECH-304 / SD-051
  (cue-specific conditioned safety store): accumulate safety, gate commitment-release.

Neither tags an action / location / policy as an **escape affordance to be approached
under future threat**. The user's bridge is the missing wire:
`directed action reduces z_harm_a / terminates threat cue -> phasic relief (MECH-302)
+ learned safety (MECH-303/304) -> escape_affordance[action/location] += credit ->
threat-gated E3 approach bonus`. The pieces exist; the binding does not.

This is the canonical "philosophy-right / mechanism-incomplete" REE pattern resolved
the **correct** way (cf. SD-010/SD-011 stream-split), not the SD-003 way (28 FAILs
from treating a load-bearing divergence as a caveat).

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | gate engaged + suppressed (readiness met); FAIL is downstream of MECH-357, not against it |
| Biological reference | partial -> missing dependency | Moscarello/LeDoux NAcc relief/safety action-credit bridge absent; matches dependency-knockout signature |
| Developmental / dependency prerequisites | missing | escape-affordance bridge absent; MECH-302/303/304 exist but unwired to avoidance |
| Implementation completeness | partial | `avoidance_efficacy` is a SCALAR "avoidance works", not affordance-indexed; no-op penalty only, no directed-approach term |
| Environment adequacy | adequate | both arms reached hazard stage; freeze fired; harm stream fed (z_harm_a~0.34) |
| Measurement adequacy | adequate | engaged-but-insufficient cleanly captured; seed-43 efficacy/survival inversion is the disambiguator |
| Integration adequacy | partially coupled | gate suppresses freeze but is not coupled to relief/safety credit or E3 approach-under-threat |
| Scale / capacity | unknown (secondary, KEPT LIVE) | budget/competence could contribute; seed-43 (full efficacy, worst survival) argues structure over budget, but a deeper hazard-navigation gap is not yet ruled out |

**Recommended epistemic stance:** substrate-gap discovery (missing escape-affordance
bridge). Highly **contributory at the substrate-discovery layer**; reads
`non_contributory` only because the diagnostic is claim-free. Pair with
`pending_retest_after_substrate` semantics on the survival-leg cohort.

## 6. Learning extracted

1. **New dependency discovered:** instrumental avoidance needs a relief/safety
   **escape-affordance bridge** (affordance-indexed credit + threat-gated approach),
   not just ilPFC freeze-suppression + a scalar efficacy trace.
2. **Existing dependency localised:** REE's relief (MECH-302) and safety
   (MECH-303/304) substrates are built but **unwired to avoidance** -- the gap is
   wiring + affordance-indexing, not net-new affect machinery.
3. **Repair is structural, not parametric:** the seed-43 inversion (max scalar
   efficacy -> worst survival) is positive evidence that tuning the gate harder or
   raising the curriculum budget will not lift G_H; the missing thing is *which* action
   is the way out.
4. **Co-equal branch kept live (user directive):** a deeper hazard-navigation /
   survival-competence gap must be ruled out by the discriminative experiment before
   the full bridge is built -- if even the both-bridges arm fails to lift G_H while a
   navigation positive-control (oracle escape gradient) also fails, the gap is
   navigation, not the bridge.

## 7. Repair pathway

**Routing: implement-substrate (create), gated behind the smallest discriminative
experiment.** Build the escape-affordance bridge behind no-op-default flags
(bit-identical OFF), then validate + dissociate via the thought-intake Section 5 4-arm
design BEFORE any broad rewiring or governance promotion.

Discriminative experiment (thought-intake Section 5, with the user-mandated
nav-competence co-branch folded in):

- `ARM_BASE_IA_ONLY` -- SD-058/MECH-357 exactly as 603h INTACT (control).
- `ARM_RELIEF_BRIDGE` -- IA + relief credit from negative d(z_harm_a)/dt bound to the
  last directed action/location (MECH-302-consistent).
- `ARM_SAFETY_BRIDGE` -- IA + learned safety predictor for action/location/context
  after threat absence (MECH-303/304-consistent).
- `ARM_RELIEF_SAFETY_BRIDGE` -- both.
- **NAV-COMPETENCE control (added):** a positive-control readout (e.g. hand-shaped /
  oracle escape gradient, or reef-refuge reachability under threat) so a flat G_H
  across all bridge arms can be attributed to a navigation/survival-competence ceiling
  rather than to the bridge being wrong.

Acceptance (per thought-intake Section 5):
- readiness: PAG freezes on lesion/control; IA gate engages; relief/safety bridge fires
  **non-vacuously** (each enabled bridge half must actually credit);
- primary: `G_H >= 2/3` AND `G_H` improves over `ARM_BASE_IA_ONLY`;
- secondary: P1 survival transfer improves without pathological over-avoidance /
  resource starvation;
- safety guard: bridge bonus must be threat-context bounded and must not globally swamp
  food/goal approach.

Interpretation grid:
- Relief-only pass -> missing phasic negative-reinforcement credit.
- Safety-only pass -> missing learned threat-absence predictor / conditioned inhibitor.
- Both required -> avoidance needs complementary relief + safety bridge.
- Neither helps AND nav-control also fails -> deeper motor/trajectory or
  survival-affordance-representation gap (route to a navigation/competence substrate,
  NOT the bridge).

## 8. Draft evidence_quality_note (governance writes; not written here)

> V3-EXQ-603h (claim-free SD-058/MECH-357 Stage-H validation) FAIL adjudicated
> engaged-but-insufficient: the ilPFC gate engaged and suppressed PAG freeze on all
> INTACT seeds (readiness met) but G_H_INTACT was 0/3 and did not beat LESION. The
> scalar avoidance-efficacy trace is decoupled from survival (seed 43: efficacy 0.633,
> worst survival 11.0) because the gate only penalises the no-op class and binds no
> directed escape affordance. Discovered dependency: a relief/safety escape-affordance
> bridge (affordance-indexed credit wiring MECH-302/303/304 into threat-gated E3
> approach). SD-058/MECH-357 stay candidate/v3_pending, unweakened (freeze-suppression
> claim confirmed present). pending_retest_after_substrate on the goal_pipeline GAP-2
> survival-leg cohort. Nav-competence ceiling kept as a co-equal branch the 4-arm
> discriminative EXQ must rule out.

## 9. Routing decision (user-confirmed 2026-06-08)

- Diagnosis: **Yes, but flag nav-competence** -- bridge is the leading repair;
  hazard-navigation/survival-competence kept as a co-equal branch the discriminator
  must rule out.
- Substrate scope: **create** -- new substrate_queue entry for the relief/safety
  escape-affordance bridge, built behind no-op flags first, validated by the 4-arm EXQ.

See `failure_autopsy_V3-EXQ-603h_2026-06-08.json` for the machine-readable hand-off.
