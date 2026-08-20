# Failure autopsy -- V3-EXQ-932a (z_goal / residue_wanting coupling re-instrument)

- **Generated (UTC):** 2026-08-20T02:39:17Z
- **Scope:** single (claim-free diagnostic PASS -- autopsy mandatory by `experiment_purpose`)
- **Status:** confirmed (user gate 2026-08-20)
- **Session:** failure-autopsy-multi-20260819
- **Dry-run gate:** manifest checked, top-level `dry_run` absent -- not a smoke.

## 1. Scope

`claim_ids: []`, `experiment_purpose: diagnostic`, `evidence_direction:
non_contributory`, `non_degenerate: true`. It promotes nothing and weights no
governance, and its own note says so. **No claim-layer disposition is owed or
offered.** It is autopsied because a diagnostic-purpose run requires it regardless
of PASS/FAIL, and because a claim-free run's *prose* can still make an
organism-level assertion with no claims.yaml gate in front of it (GOV-FAILLOC-1).

**On that specific exposure: it is absent.** A full scan of the 2285-line driver
finds exactly one organism-level mention and it is a *question*, not an assertion
(`:10`). The manifest note independently disclaims causal inference, and the
predecessor autopsy's standing prohibition -- that none of this may be paraphrased
as *"wanting does not work in REE"* -- is respected. Recorded as a clean pass on
that test.

## 2. Facts

Lettered re-instrument of V3-EXQ-932, prescribed by
`failure_autopsy_931-932-wanting-authority-cluster_2026-08-16` section 8. Two arms
on `z_goal_seeding_gain`: `g1_emergent` (1.0) and `g4_seeded` (4.0). Seeds [0,1,2].
All four load-bearing criteria are **measurement-validity** criteria; coupling
detection is explicitly *"REPORTED, never gated"*.

The prescription had five items. Delivery: item 1 (drop/redefine `approach`) done;
item 2 (DV positive-rate floor) done; item 3 (per-seed + within-seed) done; **item 4
partial** -- partials are computed for wanting couplings but are null on every
`zgoal` coupling and on `wanting<->zgoal`, where the autopsy said *"and vice versa"*;
**item 5 deviated** -- the autopsy offered two options (adopt 931's forced config, or
declare the emergent-regime question a separate spike) and 932a took a third, a
2-arm dose on `z_goal_seeding_gain`, with a stated and defensible rationale (a
force-seeded z_goal is a lagged z_world EMA whose coupling would be an artifact of
the forcing). The deviation is documented, not concealed, but it is the parent's to
adjudicate rather than assume prescribed.

## 3. The two findings that matter

**(A) The label is carried by the NON-PRODUCTION arm.** `z_goal_seeding_gain` ships
at **1.0** (`ree_core/utils/config.py:6199`). In the production arm (g1) **no
wanting coupling clears the 0.15 floor on `r`**; the only one flagged `nontrivial`
qualifies on |rho| and is **negative** (r -0.132, rho -0.219) -- the opposite
direction to the incentive-salience reading the label evokes, and its within-seed
pooled r is **+0.541**, opposite again. Every positive floor-clearing coupling lives
in g4 at gain 4.0.

The label logic (`:1965-1977`) is `any(...)` across **both** arms and sign-agnostic
(`abs`), so a single nontrivial coupling in the non-production arm alone sets
`wanting_behaviour_coupling_detected`. It is also **ungated** -- the PASS would be
identical had every coupling come back trivial; only the label string would change.

This is a **fifth instance** of the pattern the 2026-08-16 human gate already
flagged as CROSS-CLUSTER decision 4 ("a mechanism tested in a NON-PRODUCTION
configuration", four prior instances, warn-only authoring lint authorised). It
should be routed to that existing authorised lint, not to a new mechanism.

**(B) The production arm does not reproduce the predecessor's sole surviving
finding -- and the comparison is confounded.**

| | autopsy re-analysis of 932 (gain 1.0) | 932a g1_emergent (gain 1.0) |
|---|---|---|
| wanting -> moved pooled r | **+0.373** | **+0.081** |
| partial r given z_goal | **+0.432** (strengthens) | +0.070 (weakens) |
| seeds replicated | **3/3** (0.28/0.55/0.28) | 2/3 settled (0.169/0.037; third n=34, underpowered) |
| nontrivial vs floor 0.15 | yes | **no** |

The queue note calls g1_emergent *"932's operating point, byte-identical"*. That is
true of the **knob** and false of the **substrate**: `substrate_commit` moved
(`c38e083d` -> `196869ee`), `total_eval_steps` fell 1013 -> 753 (-26%) at identical
env settings, and z_goal liveness moved from seed 2 at `active_frac` 0.0087 to seed
0 at 0.4691 -- a different seed and a ~54x change. **So g1_emergent is not a clean
control for 932, and the non-replication cannot be attributed to instrument repair
rather than substrate drift from this manifest alone.**

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **n/a** | Claim-free by construction. |
| Biological reference | n/a | Observational coupling measurement, no mechanism translation under test. |
| Prerequisites | present | All 8 preconditions met across both arms. |
| Implementation | complete | The four prescribed repairs are real; 2 of 5 items partial/deviated (section 2). |
| Environment | **wrong pressures** | `approach` base rate is **0.000** in both arms -- the 932 defect (0/1013) fully reproduced -- and the new precedence-free `approach_raw` lands at 0.004-0.005, below the 0.05 floor. So the diagnostic question item 1 was built to answer ("can `approach` fire at all?") returns **no**, on both DV definitions. 6 of 10 couplings are `unsettable_dv_degenerate` in both arms. |
| Measurement | **improved but partial** | The instrument is materially better than 932's (an emitted 0.0 now means a measured zero, not a structural one), yet the label logic does not consult the instrument's own `pooled_without_within_seed_support` flag, and sign instability is systematic across three axes (pooled vs within-seed, r vs rho, arm vs arm). |
| Integration | n/a | |
| Scale | **insufficient** | Per-seed n 383/321/**34** (g1) and 423/275/**53** (g4). Seed 2 is below the pre-registered `MIN_COUPLING_N_PER_SEED = 50` in g1, so every g1 "within-seed" estimate rests on 2 seeds. |

### Failure-location summary (GOV-FAILLOC-1)

- **MECHANISM FAILED:** not_established.
- **MEASURES FAILED:** **established** -- label carried by an ungated, sign-agnostic, cross-arm `any()`.
- **ENVIRONMENT FAILED:** **established** -- `approach` unreachable on both DV definitions.
- **REE FAILED:** false.

**Net classification: MIXED -- not chargeable to REE**, matching the predecessor
cluster's own verdict for both its targets.

## 5. Hypothesis-space ledger (Step 9b)

Question `wanting_authority_vs_behavioural_coupling` (claim-free, 4 hypotheses,
`initial_frozen_count` 4, `growth_restriction` absent, 3 alive).

**932a resolves NOTHING, and that is the correct outcome.** The question's own
`observation_bottleneck` states that *"no run to date has measured a
wanting->behaviour coupling and a wanting-pathway ablation in the SAME run; 931
ablated without measuring coupling, 932 measured coupling without ablating."* 932a
measures coupling and does not ablate -- so the bottleneck **persists exactly as
stated**, and its `distance_phrase` ("one cheap discriminator away") remains
accurate and unchanged.

Recorded, not resolved: `H-shared-situation`, `H-alternative-effector` and
`H-reverse-writer-cadence` all stay `alive`. No growth event; `initial_frozen_count`
unchanged at 4.

## 6. Routing -- CONFIRMED at the user gate (2026-08-20)

**`governance`**, applying to the **manifest**, not to any claim -- the same
disposition the predecessor cluster used for its own claim-free targets, whose
`per_claim_recommendation` was deliberately `{}`.

- `evidence_direction` **stands** at `non_contributory`; `epistemic_category`
  `standard`. No claim is touched.
- **Route finding (A) to the existing authorised warn-only non-production-config
  lint** as a fifth instance. Do not mint new machinery.
- **Record finding (B) as an open question, not as a refutation of 932.** The
  predecessor autopsy's measurement-validity PASS for 932 stands and is not
  superseded; what is now in doubt is the *coupling narrative* at the production
  operating point, and the substrate drift means this run cannot settle it.
- **Do NOT queue a further coupling re-instrument.** The bottleneck is an ablation,
  not another measurement -- the question needs coupling and ablation in one run,
  which is `H-cem-scoring-authority`'s successor design, not a third letter of 932.
- `recommended_substrate_queue_entry.action: none`.

## 7. Learning extracted

1. **An `any()` across arms, sign-agnostic and ungated, is not a finding.** A label
   set by one nontrivial coupling in a non-production arm, whose production-arm
   counterpart is negative, cannot bear the reading its name invites.
2. **"Byte-identical config" is not "identical substrate."** A re-instrument's
   baseline arm is only a control for its predecessor if the substrate is also
   pinned; here `total_eval_steps` moved 26% and z_goal liveness moved 54x between
   the two runs.
3. **A re-instrument should state which prescription items it did not deliver.**
   Items 4 and 5 were partial and deviated respectively, both defensibly, but the
   manifest does not flag either as a deviation -- it took an autopsy to notice.
4. **A structurally unreachable DV stays unreachable when you redefine it.** The
   precedence-free `approach_raw` was added to test whether action-precedence caused
   `approach`'s 0/1013; it lands at 0.004-0.005, so the answer is no and the DV is
   simply not achievable in this env.
