# Failure Autopsy -- V3-EXQ-610e (INV-074 crystallization necessity)

- **Generated (UTC):** 2026-06-05T11:11:49Z
- **Scope:** single (lineage cluster member; see Cluster section)
- **Status:** confirmed (interactive gate: routing = true-negative-control + threshold-sweep 610f; epistemic_category = measurement_test_design_defect)
- **Run:** `v3_exq_610e_inv074_crystallization_necessity_20260604T225319Z_v3` (machine ree-cloud-1, completed 2026-06-04T22:53:19Z)
- **Supersedes:** V3-EXQ-610d (transitively 610c)
- **Claims:** INV-074 (primary, universal invariant, candidate), MECH-334 (candidate, v3_pending, epistemic_category substrate_ceiling), MECH-333 (candidate, v3_pending)
- **experiment_purpose:** evidence

---

## 0. The one thing that changed since 610d

**610e is the first run where the crystallization machinery is verifiably LIVE.** The
8-result harness-no-op lineage (543h/i/k/l + 610a/b/c/d) -- in which the policy was never
trained, the expansion optimizer never stepped, and `ewc_penalty()` never entered the loss --
is **resolved**. `fix_verification` in the manifest proves all three fixes genuinely applied:

| Fix | Manifest field | Value | Verdict |
|---|---|---|---|
| FIX 1 policy trained | `fix1_policy_trained` / `fix1_init_entropy` -> `fix1_trained_entropy` | true / 0.410 -> 0.491 | trained, non-uniform |
| FIX 2 expansion stepped | `fix2_expansion_stepped` / `fix2_n_expansion_params` | true / 1249 | stepped (499 steps/seed phase 3) |
| FIX 3 EWC in loss | `fix3_ewc_penalty_in_loss` / `fix3_ewc_penalty_value` / `fix3_residue_grad_sum` | true / 0.268 / 1.072 | active; ARM_1 `ewc_penalty_last` = 803.1 / 335.0 / 283.9 |
| acceptance gate | `policy_trained_nonuniform` | true | passes the startup assertion fork-(d) guard |

So the failure has **relocated**: from 610d's harness no-op to a deeper, experiment-design
cause. This is genuine new information, not a repeat.

## 1. Facts (reconstruction, no interpretation)

2-arm discriminative test of INV-074's core claim: plasticity crystallization is necessary
for diversity persistence post-Phase-3. ARM_0 control (`crystallize_at_phase3=False`), ARM_1
test (`crystallize_at_phase3=True`). 3 matched seeds (42/43/44), 2500 episodes x 200 steps,
4-phase infant curriculum, Phase-3 destabilising pressure from IGW-20260601-023 (SD-047
multi-source + SD-048 interoceptive noise + accelerated drift).

Pre-registered acceptance (each Delta >= +0.10 nats; PASS = D1 AND D2 AND D3):

| Criterion | Requirement | Observed | Result |
|---|---|---|---|
| D1 crystallization preserves diversity | ARM_1 - ARM_0 phase-3 entropy >= +0.10 | **-0.00021** | FAIL |
| D2 control collapses | ARM_0 phase-2 - phase-3 entropy >= +0.10 | **-0.0105** (rose) | FAIL |
| D3 sanity (both diverse at phase-2) | both > 0.4 | 1.0283 / 1.0283 | PASS |

Per-seed phase-2 entropy is **identical** across arms (1.340 / 0.616 / 1.129; mean 1.0283),
confirming the arms are correctly matched through phase 2 (crystallization applied only at the
Phase-3 boundary). Control phase-3 per seed: 1.349 / 0.648 / 1.119 -- essentially unchanged
from phase 2 (entropy slightly *rises* on average). All seeds sit well below the ln(5)=1.609
uniform ceiling, and the mean 1.0283 is **below** the 610c/610d untrained band (1.04-1.12),
i.e. the policy is verifiably trained and non-uniform (`untrained_band_low=1.04`).

**Failed criterion:** discrimination (D1 + D2). The sanity/absolute criterion (D3) passes ->
substrate-ceiling fingerprint shape. **This is the pre-registered fork (c)** (script lines
107-120): D2 FAIL while the policy is verifiably trained and the wiring counters confirm
`n_policy_steps>0`, `n_expansion_steps_phase3=499`, `n_ewc_terms_phase3=499`,
`ewc_penalty_last>0`.

Contrast with 610d (untrained policy): control collapse there was **+0.047** (partial). With
the trained policy + active entropy bonus, 610e control collapse is **-0.0105** (none). The
entropy-maximizing objective counteracts the Phase-3 pressure.

## 2. Root cause (decisive) -- the negative control is confounded

The negative control (ARM_0) is **not a true negative**. Script lines 470-483 build the agent
in **both** arms with the full always-on diversity-preservation stack -- only
`crystallize_at_phase3` differs:

```python
# Diversity mechanisms (both arms).
...
# MECH-313 noise floor.
use_noise_floor=True,
noise_floor_weight=NOISE_FLOOR_WEIGHT,         # 0.3
# MECH-341 E3 score diversity preservation.
use_e3_score_diversity=True,
use_e3_diversity_entropy_bonus=True,
```

and the shared policy train step (lines 398-400) adds the policy entropy bonus, present in both
arms:

```python
policy_loss  = -(log_probs_t * advantages.detach()).sum()
entropy_bonus = -ENTROPY_BONUS_WEIGHT * entropies_t.sum()   # 0.02; subtract = maximize entropy
total_loss    = policy_loss + entropy_bonus
```

So ARM_0 retains **MECH-313** (stochastic noise floor / LC tonic analog, weight 0.3) +
**MECH-341** (E3 score-diversity preservation + diversity entropy bonus) + the policy
**entropy bonus** (0.02, actively maximizing action entropy). These constitute a robust,
always-on diversity FLOOR. A trained policy under an entropy-maximizing objective will not
collapse to monostrategy, and the IGW-023 Phase-3 pressure sits below the floor's resistance
threshold.

**Consequence:** INV-074's premise -- *collapse-without-crystallization* -- cannot be
instantiated, because diversity is **over-determined** in V3. Crystallization's marginal
necessity is unmeasurable while three other mechanisms independently guarantee the diversity
it is supposed to be necessary for. D1 then reads ~0 not because crystallization fails but
because there is nothing left to preserve.

## 3. Claim-layer map

| Claim | Type / status | Did the test let it express? |
|---|---|---|
| INV-074 | universal invariant, candidate | **No** -- premise (collapse-without-crystallization) never instantiated; **not weakened, not falsified** |
| MECH-334 | candidate, v3_pending, substrate_ceiling | No -- closure/EWC fires (`ewc_penalty_last`>0) but has no collapse to lock against |
| MECH-333 | candidate, v3_pending | No -- open-phase plasticity asymmetry has no winner-take-all dynamic to forestall |

`claim_ids` correctly tagged (inherited from 610d, and the machinery these claims assert IS
the machinery under test -- it is now live, just unable to express against a confounded
control). No mis-attribution.

**Observation, NOT a tag change:** the control's non-collapse is *consistent* with a robust
**MECH-341 / MECH-313** diversity floor (the pre-registered fork-(c) "strengthens
MECH-341/313" reading). But MECH-341/313 are not in `claim_ids` and the experiment was not
designed to test them; adding a post-hoc positive-support entry would contaminate their
evidence records (claim_ids accuracy rule). Recorded here as an observation to be tested
cleanly in 610f, **not** as a governance write against MECH-341/313.

## 4. Biological-reference triage

Closest mechanism: **ocular-dominance critical-period plasticity** -- open-window competitive
plasticity (E/I balance shift, PV+ interneuron / GABA maturation; Fagiolini & Hensch 2000),
then active closure (PNN / Otx2 / Sema3A; Pizzorusso 2002). INV-074 is a **biology-faithful
translation, not a formal-definition import** -- divergence none on the claim side, lit present
(lit_conf 0.82). Monocular deprivation = monostrategy capture when the window never closes.

Critically: in real cortex there is **no always-on entropy regularizer** propping diversity up.
Critical-period closure IS necessary there precisely because nothing else holds the diverse
representation against competitive overwriting. The V3 substrate **diverges from biology on the
substrate side**: it carries redundant always-on diversity floors (MECH-313/341 + entropy
bonus) that the biological system lacks. The 610e FAIL is therefore the signature of a
**substrate that cannot reproduce the biological condition under which crystallization is
necessary** -- a confounded test bed, not a falsified claim.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | premise never instantiated; INV-074 not weakened |
| Biological reference | clear + faithful | OD critical-period / Hensch; lit present; divergence is substrate-side (always-on floors biology lacks) |
| Prerequisites | present-but-confounding | MECH-313 + MECH-341 + entropy bonus always-on in the control; they mask crystallization's necessity |
| Implementation | complete | **the genuine advance over 610d** -- all three fixes verified live (policy trained, expansion stepped 499x, EWC penalty 803/335/284) |
| Environment | adequate-but-sub-threshold | IGW-023 pressure present and partially worked in 610d (+0.047); here it sits below the trained-policy diversity floor (-0.0105) |
| Measurement | misleading | D1/D2 measure a distribution the always-on entropy bonus holds up; the negative control is not a true negative |
| Integration | n/a | |
| Scale | n/a | budget adequate (2500 ep x 200 steps, 3 seeds) |

**Recommended epistemic_category (user-confirmed):** `measurement_test_design_defect`. The
failure is a confounded negative control, fixable by experiment redesign **without** substrate
enrichment. Governance currently has `substrate_ceiling` on the manifest (applied 2026-06-05
before this autopsy) -- **recommend re-tag to `measurement_test_design_defect`** so the
next-step signal is "redesign the control," not "enrich the substrate." (Note: this is a
manifest-level diagnostic tag; INV-074's own claims.yaml `epistemic_category` stays as-is.)

## 6. Cluster

9th non_contributory crystallization-arm result in the **543h/i/k/l + 610a/b/c/d/e** lineage.
The lineage has **two structurally distinct sub-causes**, and 610e is the inflection point:

| Sub-lineage | Structural property | Status |
|---|---|---|
| 543h/i/k/l, 610a/b/c/d | harness no-op: a trained, WTA-prone policy was never actually placed under the crystallization mechanism (heads never differentiated / policy never trained / no collapse pressure stepped) | **RESOLVED in 610e** |
| **610e** | confounded negative control: the policy IS trained and crystallization IS live, but the control retains an always-on diversity floor (MECH-313/341 + entropy bonus) so it cannot collapse | **current** |

So 610e does NOT share 610d's cause -- it shares only the abstract sanity-passes /
discrimination-fails *shape*. The load-bearing finding is that **fixing the harness exposed
the next, deeper layer**: even a correctly-wired crystallization test cannot discriminate while
the control is protected by redundant diversity machinery.

**Not a member of the 632/634 cluster** (goal-pipeline foraging-competence ceiling,
scaffolded_sd054_onboarding, MECH-229/230) -- different substrate, claims, and structural
property.

## 7. Learning extracted

1. The harness no-op is genuinely fixed (verified) -- 610e is the first behaviorally-live
   crystallization run; the 8-result no-op lineage is closed.
2. Fixing the harness relocated the failure to a **confounded negative control**: the diversity
   stack (MECH-313 noise floor + MECH-341 E3 diversity + policy entropy bonus) is always-on in
   BOTH arms, so ARM_0 is not a true negative.
3. A trained policy under an active entropy-maximizing objective does not collapse to
   monostrategy under IGW-023 pressure (control collapse moved 610d +0.047 -> 610e -0.0105 as
   the policy went from untrained to trained-with-entropy-bonus).
4. INV-074's necessity premise is **untestable while diversity is over-determined**; the test
   must isolate crystallization as the *sole* diversity-preserving mechanism in the control.
5. INV-074 (universal invariant) is not weakened -- biology supports it; V3 simply cannot
   instantiate the collapse condition without stripping its own diversity floors.
6. The control's non-collapse is consistent with robust MECH-341/313 (fork-(c) positive
   reading) but cannot be scored against them -- they are untagged and untested-by-design.
7. D3-passes / D1+D2-fail is the substrate-ceiling *shape*; here the cause is a test-design
   confound, not a too-coarse substrate.

## 8. Repair pathway / routing

**Routing: `/queue-experiment` redesign V3-EXQ-610f** (user-confirmed at the interactive gate:
"True-negative control + threshold sweep"). 610f must:

- **Strip the diversity floor from the CONTROL** so crystallization is the only
  diversity-preserving mechanism: `entropy_bonus_weight=0`, `use_noise_floor=False`,
  `use_e3_diversity_entropy_bonus=False` (and any E3 score-diversity term) in ARM_0. ARM_1
  keeps crystallization as its diversity-preservation route.
- **Add an `entropy_bonus_weight` sweep** (e.g. {0.0, 0.005, 0.02}) to map the collapse
  threshold -- locate the floor weight at which the control starts to collapse, then test
  whether crystallization preserves diversity above that collapse.
- Carry forward the 610e startup assertion (all three fixes present) so the harness fix is not
  regressed.
- **Pre-register the fork:** (i) stripped control collapses AND crystallization preserves ->
  INV-074/MECH-333/MECH-334 supports; (ii) stripped control still does NOT collapse under
  Phase-3 pressure -> escalate pressure or revisit whether the V3 policy is WTA-prone at all
  (would weaken the *V3-applicability* of INV-074, not the universal invariant); (iii)
  crystallization fails to preserve a collapsing stripped control -> /diagnose-errors,
  weakens MECH-334.
- A clean stripped-control result also becomes the proper test bed for the MECH-341/313
  "robust diversity floor" reading -- run the floor-on vs floor-off contrast explicitly so
  those claims can be tagged and scored honestly.

**`recommended_substrate_queue_entry.action = none`** -- the substrate (IGW-023 env + the
crystallization machinery) is not the blocker; this is an experiment-design redesign. Leave
`substrate_queue.json` unchanged.

Draft `evidence_quality_note` for governance: see the JSON artifact
`recommended_evidence_quality_note`.

---

*Artifact pair: `failure_autopsy_V3-EXQ-610e_2026-06-05.{md,json}`. This skill produces the
diagnosis; `/governance` applies the manifest/claim writes; `/queue-experiment` produces 610f.*
