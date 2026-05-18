# Failure Autopsy — V3-EXQ-543h

- generated_utc: 2026-05-18T05:33:59Z
- scope: cluster (543f / 543g / 543h; continuous with the MECH-309 433e/523* family)
- status: confirmed (user scientific judgment applied 2026-05-18)
- target run_id: v3_exq_543h_arc062_crystallization_falsifier_20260518T000930Z_v3
- queue_id: V3-EXQ-543h | claim_ids: ARC-062, MECH-309, INV-074, MECH-334
- outcome: FAIL | exit_reason: ok | elapsed ~15580 s (cloud-4, 2026-05-17T19:49 -> 2026-05-18T00:09Z)
- provenance: ran on cloud-4, runner pushed queue-removal (29f090f) but never committed
  the manifest (experiment_runner.py:1394 silent-drop pattern); recovered recover-only
  in REE_assembly e8a2788f71. No second 543h run exists (runner_status: 0 hits;
  filesystem: 1 manifest; git history: only the recovery commit).

## 1. Facts (no interpretation)

The script `v3_exq_543h_arc062_crystallization_falsifier.py` is a 2x2x2 factorial
(use_gated_policy x use_dacc x crystallize_at_phase3), 8 arms x 3 seeds [0,1,2]. The
2x2 SP-CEM sub-design (P0=40 / P1=60 / P2=8, outcome-coupled REINFORCE, head_div term
removed, LAMBDA_DISC_VAR=0.1, INERT_GATING_THRESHOLD=0.05) is byte-for-byte the same
constant set as 543g; the only addition is the crystallize_at_phase3 third factor.

Pre-registered acceptance:
- PRIMARY  D2_xtal = ARM_7_both_xtal.reef - ARM_6_gated_only_xtal.reef >= +0.10
- SECONDARY repro  = ARM_2_gated_only.reef > ARM_3_both.reef ("543g signature")
- PASS = D2_xtal AND repro

Observed (metrics.acceptance):
- D2_xtal_delta_arm7_minus_arm6 = -0.1463  (needed >= +0.10) -> FAIL
- repro_543g_signature = True   (ARM_2 0.518 > ARM_3 0.250 -- sign only)
- overall_pass = False
- interpretation_branch = b_dacc_architecture_isolated_GAP-B_in_progress
- evidence_direction (manifest) = non_contributory overall;
  per_claim = {INV-074: weakens, MECH-334: weakens,
               ARC-062: non_contributory, MECH-309: non_contributory}

reef_fraction_per_arm: ARM_0 0.650, ARM_1 0.558, ARM_2 0.518, ARM_3 0.250,
ARM_6 0.574, ARM_7 0.428. (ARM_4==ARM_0 and ARM_5==ARM_1 bit-identical by
construction -- xtal has no effect on non-gated arms.)

Probe state on EVERY gated arm: probe_gate_arm{2,3,6,7}_failed = True;
n_inert_gating_seeds_arm{2,3,6,7} = 3 (all seeds inert). C2_state_dependence_pass
= False, C3_risk_type_dissociation_pass = False.

Failed criterion: discrimination (D2_xtal). But the load-bearing fact is the
**negative-control/absolute** failure beneath it: the inert-gating probe failed on
all gated arms and all seeds.

## 2. The central finding — the interpretation grid misfired (b) when the run is (c)

The script's own pre-registered grid:
- (b) D2_xtal FAIL + repro reproduced -> isolate to dACC architecture;
  {INV-074 weakens, MECH-334 weakens, ARC-062/MECH-309 non_contributory}.
- (c) repro NOT reproduced (OFF arms do not show the 543g signature) ->
  substrate / seed drift; treat run non_contributory across ALL claims.

Branch (b) is only valid if the xtal-OFF arms genuinely reproduced 543g. The script
decides "reproduced" solely via the sign ARM_2 > ARM_3. That sign survived
(0.518 > 0.250) while the substrate state INVERTED:

| | 543g `_144716Z` | 543h xtal-OFF |
|---|---|---|
| gated arms inert? | n_inert=0, probe_failed=False (gating ACTIVE) | n_inert=3 all seeds, probe_failed=True (gating INERT) |
| ARM_0 / ARM_1 / ARM_2 / ARM_3 reef | 0.278 / 0.174 / 0.444 / 0.243 | 0.650 / 0.558 / 0.518 / 0.250 |
| C2 / C3 | PASS / PASS | FAIL / FAIL |

The xtal-OFF arms did not reproduce 543g in any mechanistic sense — the gated policy
collapsed to inert on every gated arm and seed; only the qualitative sign coincided.
That is branch (c), not (b). Because crystallize() freezes head_0/head_1/discriminator,
crystallizing an already-collapsed (heads-identical) policy and adding a zero-init
expansion MLP cannot test MECH-334; D2_xtal = ARM_7 - ARM_6 is the difference between
two crystallized-INERT policies and measures nothing about the crystallization
mechanism. The `repro` acceptance check is a sign-only false positive: it must also
require n_inert_gating_seeds == 0 on the gated arms before branch (b) can be entered.

CONFIRMED reclassification (user, 2026-05-18): apply branch (c) — evidence_direction
non_contributory for ALL FOUR claims. Specifically correct INV-074 weakens ->
non_contributory and MECH-334 weakens -> non_contributory (ARC-062/MECH-309 already
non_contributory).

## 3. Cluster pattern

| Experiment | Claims | Gated-arm probe (abs/neg-control) | Discrimination | Read |
|---|---|---|---|---|
| V3-EXQ-543f | ARC-062, MECH-309 | INERT (n_inert=3, probe_failed) | all D fail | inert under trained policy |
| V3-EXQ-543g | ARC-062, MECH-309 | ACTIVE (n_inert=0, probe ok) | all D fail (D2 delta -0.200) | gating expressed; discrimination still failed (only "weakens ARC-062" in family) |
| V3-EXQ-543h | +INV-074, +MECH-334 | INERT (n_inert=3, probe_failed) | D2_xtal -0.146 | inert returned; crystallization untestable |

This is **one structural property, not three independent bugs**: GatedPolicy
head-differentiation does not robustly persist under outcome-coupled REINFORCE. The
head_div term was removed (543g/h, on a symmetric-cancellation argument); the
replacement disc_var@0.1 does not hold the two heads apart, so under REINFORCE the
heads collapse to identical action distributions (TV < 0.05). Activation is
RNG/init-sensitive: structurally identical 2x2, active in 543g, inert in 543f and
543h. This is continuous with MECH-309's already-documented family (V3-EXQ-522 PASS
under heuristic policy; 433e/433f/523/523a/523b non_contributory under trained policy
— "monomodal V_s monostrategy substrate-ceiling").

Two live readings, and which planning decision they force:
- substrate-instability (the gated substrate intermittently fails to carry
  differentiated behaviour under a trained policy) -> /implement-substrate.
- test-design ceiling (the `repro` check cannot distinguish functional from inert
  gating, so the falsifier is not decision-grade) -> redesign acceptance logic.
Both are real here; the substrate reading is primary (chosen routing), the
test-design reading is a mandatory secondary fix folded into the redesigned EXQ.

## 4. Biological-reference triage

- ARC-062 (rule-apprehension layer) / MECH-309 (substrate-purpose validation): the
  GatedPolicy two-head + discriminator is a computational stand-in for
  context-dependent policy arbitration (PFC-like task-set / contextual policy
  selection). Closest reference depends on a *formed, differentiated* policy
  repertoire being present before arbitration can be observed.
- MECH-334 (critical-period crystallization): biological model already identified in
  claims.yaml — PNN / Lynx1 / NgR1 three-brake architecture; lit pull completed
  2026-05-17 (lit PRESENT). This is NOT a formal-definition import lacking biology.
  The failure is therefore not biology-divergence and not falsification: it is a
  missing-prerequisite signature. Biologically, you cannot observe a critical-period
  brake consolidating a cortical map that never formed (no ocular-dominance columns
  -> nothing for PNN closure to stabilise). MECH-334 depends on a functional
  differentiated GatedPolicy (MECH-333 / INV-074); that substrate collapsed.

Verdict: lit_status = present (MECH-334); divergence = none; the FAIL matches a
missing-dependency signature, not claim pressure. (lit_conf and exp_conf reported
separately, never blended: lit is present/positive for MECH-334; exp is
non_contributory — this is a not-yet-testable cell, not an under-supported one.)

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (ARC-062/MECH-309) / intact-untested (INV-074/MECH-334) | gating inert -> claims could not express; crystallization never exercised. NOT weakened. |
| Biological reference | clear | PNN/Lynx1/NgR1, lit present; failure = missing-prerequisite signature |
| Prerequisites | MISSING | MECH-334 depends on MECH-333 + functional differentiated GatedPolicy; gated policy inert all arms/seeds |
| Implementation | partial | crystallize()/ResidueField EWC present (symbol-of-mechanism); the head-differentiation it locks is unstable; head_div removed, disc_var@0.1 insufficient |
| Environment | not the driver | same CausalGridWorldV2 where 543g gating DID activate |
| Measurement | misleading | `repro` = sign-only (ARM_2>ARM_3); misfired grid (b) vs (c); does not gate on n_inert |
| Integration | partially coupled but unstable | gating activation RNG/init-sensitive (active 543g, inert 543f/543h) |
| Scale / capacity | possibly insufficient | P1=60 ep without a head_div force may be too short to drive stable differentiation; unknown |

Recommended epistemic_category: **substrate_ceiling** (unstable-activation variant).
Consistent with ARC-062's existing `substrate_conditional` and MECH-309's documented
V_s-monostrategy substrate-ceiling.

## 6. Guardrail — narrow-supports / illusory-conflict check

Voiding 543h and not honoring its supersession of 543g leaves ARC-062 with
effectively zero contributory trained-policy evidence: 543g "weakens ARC-062" (active
gating), 543f non_contributory; MECH-309 family — 522 PASS heuristic-policy only,
433e/433f/523/523a/523b non_contributory under trained policy. ARC-062's contributory
base is **narrow / single-pathway**. Flagged per the illusory-conflict-resolution
rule; pending_retest_after_substrate = true. The non_contributory recommendation must
NOT be read as conflict resolution for ARC-062.

## 7. Learning extracted

1. New/strengthened dependency: MECH-334 (and any crystallization closure) is
   untestable until the GatedPolicy it freezes carries differentiated heads under the
   trained-policy regime (MECH-333 / INV-074 prerequisite). The FAIL is a discovered
   prerequisite, not falsification.
2. Substrate property: GatedPolicy head-differentiation under outcome-coupled
   REINFORCE is unstable / init-sensitive after head_div removal; disc_var@0.1 does
   not maintain divergence. A working impl must hold n_inert_gating_seeds == 0 across
   all seeds under trained policy.
3. Test-design gap: a `repro`/replication check that tests only a sign can misfire a
   pre-registered interpretation grid into the wrong branch and emit spurious
   `weakens`. Replication gates must assert substrate functionality
   (n_inert == 0), not just an inequality sign.
4. Supersession integrity: a `supersedes:` declaration must not be honored by the
   indexer when the superseding run failed to reproduce the predecessor's substrate
   state. 543h does not subsume 543g.

## 7b. Post-autopsy cross-machine confirmation (2026-05-18T05:44Z)

Per user direction, the flagged-but-uncommitted cloud-3 543g DUPLICATE
(`v3_exq_543g_arc062_outcome_coupled_falsifier_20260517T191536Z_v3`, ran cloud-3
15:55 -> 19:15) was retrieved read-only and compared. It runs the SAME 543g
script/config as the authoritative `_144716Z`, on a DIFFERENT machine.

Two construction-RNG hypotheses were first eliminated by static code reading:
(1) preflight-scaffolding RNG -- 543h re-seeds the global RNG per arm-seed
(`_make_agent_and_env` torch/np/random.seed(seed) at the top of every arm build),
so `_preflight_check()` consumption cannot perturb the arms; (2) crystallize
plumbing shifting init -- `GatedPolicy.expansion` is created lazily in
`crystallize()`, not `__init__` (gated_policy.py:284-285); config flags are inert
dataclass defaults, so xtal-OFF construction is bit-identical to 543g.

| Run | Machine | ARM_0 | ARM_1 | ARM_2 | ARM_3 | gating | ev_dir |
|---|---|---|---|---|---|---|---|
| 543g `_144716Z` (authoritative) | host-A | 0.278 | 0.174 | 0.444 | 0.243 | ACTIVE (n_inert=0) | weakens ARC-062 |
| 543g `_191536Z` (cloud-3 dup) | cloud-3 | 0.650 | 0.523 | 0.558 | 0.324 | INERT (n_inert=3) | non_contributory |
| 543h xtal-OFF | cloud-4 | 0.650 | 0.558 | 0.518 | 0.250 | INERT (n_inert=3) | non_contributory |

The same 543g code lands ACTIVE on host-A and INERT on cloud-3 AND cloud-4. This
is NOT a 543g->543h code drift (543g itself flips basins by machine). Near-
bifurcation fragility is now CONFIRMED by direct cross-machine replication, not
inferred. Bit-identical corroboration: cloud-3 543g ARM_0 =
0.6496934637947921 == 543h xtal-OFF ARM_0 = 0.6496934637947921 -- the INERT basin
is the common attractor (cloud-3 + cloud-4 land there identically); host-A's
ACTIVE landing is the rare outlier, 1 of 3 known runs.

**Material revision to the autopsy:** the authoritative 543g `_144716Z`
"weakens ARC-062" is itself a minority lucky-basin artifact (1/3 runs ACTIVE).
The honest status is **543g as a whole is non_contributory** (2/3 runs
INERT/non_contributory; the ACTIVE/weakens landing is not reproducible). ARC-062
therefore has **zero reliable contributory trained-policy evidence** -- not even
the 543g "weakens." The narrow_supports flag (Sec. 6) is confirmed at the
strongest level. 543g `_144716Z` should NOT continue to weight ARC-062 governance
as "weakens"; it is a fragile-substrate artifact.

Safety copy of the at-risk single-VM uncommitted cloud-3 manifest + runner signal
taken to local /tmp/cloud3_543g_safety/ (read-only; no push). Committing the
cloud-3 duplicate to origin as preserved evidence is a governance/user decision
(it is the same anti-double-count item flagged in the recover-stranded-543h
WORKSPACE_STATE entry); not done here.

## 8. Routing decision (user-confirmed 2026-05-18)

- Reclassification: branch (c) — evidence_direction non_contributory for ARC-062,
  MECH-309, INV-074, MECH-334. Correct INV-074 weakens -> non_contributory and
  MECH-334 weakens -> non_contributory in governance.
- Supersession: 543h's `supersedes: V3-EXQ-543g` is VOIDED — not to be honored by the
  indexer. REVISED post-cross-machine (Sec. 7b): 543g `_144716Z` "weakens ARC-062" is
  a minority lucky-basin artifact (1/3 runs ACTIVE); **543g as a whole is
  non_contributory** and should NOT weight ARC-062 governance as "weakens." There is
  no reliable interim ARC-062 evidence to preserve. A forthcoming **V3-EXQ-543i will
  supersede BOTH V3-EXQ-543g and V3-EXQ-543h** (queued only after the substrate is
  stabilised so head-differentiation is a strong attractor reproducibly across
  machines).
- Primary routing: **/implement-substrate** — substrate_queue failure-record:
  stabilise GatedPolicy head-differentiation so n_inert_gating_seeds == 0 across all
  seeds under outcome-coupled REINFORCE before any crystallization retest.
- Secondary routing: **/queue-experiment** for V3-EXQ-543i (supersedes 543g + 543h),
  gated behind the substrate fix; the redesign MUST replace the sign-only `repro`
  check with an n_inert == 0 precondition for branch (b).
- pending_retest_after_substrate: true. narrow_supports_flag (ARC-062): true.

## 9. Draft evidence_quality_note text (for /governance to write — NOT written here)

ARC-062 / MECH-309:
> V3-EXQ-543h non_contributory (autopsy 2026-05-18). The 2x2x2 crystallization
> falsifier's gated policy collapsed to inert on all gated arms and all 3 seeds
> (n_inert_gating_seeds=3, probe_gate failed). The script's `repro_543g_signature`
> check is sign-only (ARM_2>ARM_3) and returned True while the substrate inverted from
> active (543g) to inert; this misfired the pre-registered interpretation grid into
> branch (b). Correct branch is (c): non_contributory across all claims. ARC-062
> contributory trained-policy evidence remains narrow (543g weakens [active gating],
> 543f non_contributory); pending_retest_after_substrate.

INV-074 / MECH-334:
> V3-EXQ-543h does NOT weaken INV-074 or MECH-334 (autopsy 2026-05-18, correcting the
> manifest's branch-(b) per_claim weakens). Crystallization freezes
> head_0/head_1/discriminator; the gated policy was inert before the closure fired, so
> the PNN/Lynx1/NgR1-analog crystallization mechanism was never exercised. Missing
> prerequisite (functional differentiated GatedPolicy = MECH-333/INV-074), not claim
> pressure. evidence_direction = non_contributory; pending_retest_after_substrate.

Supersession (indexer):
> Do NOT honor V3-EXQ-543h `supersedes: V3-EXQ-543g`. Cross-machine replication
> (2026-05-18, Sec. 7b) shows the 543g config is near-bifurcation fragile: ACTIVE on
> host-A (`_144716Z`), INERT on cloud-3 (`_191536Z`) and cloud-4 (543h xtal-OFF). The
> `_144716Z` "weakens ARC-062" is a 1/3 minority-basin artifact -> treat 543g overall
> as non_contributory for ARC-062 (do not weight the "weakens"). No reliable interim
> ARC-062 evidence exists. V3-EXQ-543i supersedes BOTH once the substrate is stabilised.
