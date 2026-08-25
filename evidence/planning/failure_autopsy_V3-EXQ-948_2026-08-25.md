# Failure Autopsy: V3-EXQ-948 (draft, pending user confirmation)

**Run:** `v3_exq_948_observation_interface_re_representation_probe_20260825T142115Z_v3`
**Outcome:** PASS. **experiment_purpose:** diagnostic. **claim_ids:** [] (deliberately claim-free, `brake_exempt: true`).
**Indexer adjudication flag:** `vacuous_pass` (assessed below as a FALSE POSITIVE).

## 1. Facts

Four-arm design, learner (PPO) and objective (`W3_survival_zeroed`) held fixed, varying only the
observation vector, at hazard-free D3:

| Arm | Obs | obs_dim | mean res/ep (3 seeds) | per-seed | clears 1.0 floor (majority) |
|---|---|---|---|---|---|
| `ppo_ree_latent` | z_world only | 32 | 0.5 | 0.25, 0.5, 0.75 | NO (0/3) |
| `ppo_raw_obs` | body+world+harm | 373 | 9.033 | 12.05, 12.0, 3.05 | YES (3/3) |
| `ppo_latent_plus_localfield` | z_world + 25-dim resource field | 57 | **2.233** | 1.0, 2.55, 3.15 | **YES (3/3)** |
| `ppo_localfield_only` | resource field alone | 25 | 1.217 | 1.1, 0.7, 1.85 | YES (2/3) |

Arms 1 and 2 are exact per-seed replications of V3-EXQ-813's anchor pair (0.5 / 9.033) -- replicated
exactly, confirming comparability to 813. All readiness preconditions green (encoder trained in P0,
D3 oracle/local-view-greedy floor-achievable, `survival_linked_share` structurally zero, harm share
negligible on the positive control). `criteria_non_degenerate` all true; `non_degenerate: true`;
`dry_run: false` (confirmed via `check_dry_run_citations.py`); recording core complete (`validate_recording.py`
OK -- `substrate_hash`, `config`, `seeds`, `machine_class`, `elapsed_seconds` all present).

The driver's own alternative-outcomes block: "arm 3 clears -> H-observation-interface CONFIRMED, and
NAMED: the missing content is the resource gradient. Actionable at the substrate." Arm 3 clears
(majority, 3/3). Arm 4 also clears (2/3), so this is NOT the "arm 3 flat, arm 4 clears" active-
interference reading -- it is the plain positive-demonstration reading.

## 2. Adjudication of the `vacuous_pass` flag -- FALSE POSITIVE

`interpretation.criteria` tags **all four** criteria `load_bearing: true`, including
`C_latent_clears_floor` (passed: false). The indexer's (3b) check
(`build_experiment_indexes.py::_diagnostic_adjudication`) fires `vacuous_pass` whenever ANY
`load_bearing: true` criterion reads `passed: false` on an overall PASS. But the driver's own
`interpretation.combination_rule` states explicitly: "PASS is carried by ONE criterion --
C_latent_plus_localfield_clears_floor -- not by a conjunction. The other three load-bearing
criteria are expected to read passed=false ... or passed=true ... and their values select which
FAIL label is issued rather than gating PASS." `C_latent_clears_floor` is a REPLICATION ANCHOR
expected to read false (813 pinned it at 0.5); it is not a PASS-gating criterion. This is a fifth
sub-case of the same false-flag class the indexer's own docstring already documents for
V3-EXQ-783/830/906/908: a `load_bearing: true` tag used by the driver author to mean "important for
interpretation" rather than "necessary for a non-vacuous PASS." Read the run as **verified**, not
vacuous.

## 3. Claim-layer mapping

`claim_ids: []` by design -- this is a GOV-FANOUT-1 discrimination probe on the frozen hypothesis
ledger question `conversion_ceiling_root` (leg `H-observation-interface`, axis `representation`),
which bears on MECH-457/ARC-065 without itself tagging them (`brake_exempt_reason`: "promotes/demotes
nothing and adds no ceiling reading to MECH-457 or ARC-065").

## 4. Biological reference

Not a formal-definition import. Closest reference: general cognitive-map / world-model
representations (hippocampal/parietal allocentric maps) do not automatically carry every
behaviourally-relevant gradient signal; dedicated, parallel pathways (mesolimbic value coding,
hypothalamic interoceptive/homeostatic signalling) carry resource/reward gradients a general
spatial map does not guarantee to preserve. This CORROBORATES, not diverges from, REE's own prior
biologically-motivated decisions: SD-010/SD-011 (splitting z_world into z_self/z_world/z_harm_s) and
SD-015 (a dedicated z_resource encoder, built because z_world alone was inadequate for goal-directed
resource seeding). No new `/lit-pull` needed -- this replicates an already lit-grounded REE design
principle via a second, independent symptom.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | claim-free by design |
| Biological reference | clear | see above; corroborates SD-010/011/015 |
| Prerequisites | present | zworld_encoder_trained_in_p0 green on all 3 seeds |
| Implementation | partial | z_world encoder discards recoverable resource-gradient content present in its own input |
| Environment | adequate | hazard-free D3; oracle + local-view-greedy readiness gates both clear |
| Measurement | adequate | non-circular readiness gates (replacing 813's circular consumption_share gate); DV-symmetry declared and empirically confirmed |
| Integration | isolated | external PPO actor reading frozen z_world, not REE's own internal policy machinery |
| Scale | adequate | 3 seeds/arm, majority-of-seeds convention consistent with sibling legs |

Failure-location (GOV-FAILLOC-1): not applicable in the "REE failed" sense -- this is a PASS
confirming a fixable representational gap, not a failed-to-perform organism-level read.

## 6. Cross-reference: SD-018 (PRIMARY -- red-team-corrected) and SD-015 (secondary)

**Adversarial verification (Step 7c) found a real defect in the first draft of this section and
corrected it before this write-up reached the user.** `substrate_queue.json` SD-018
("encoder.resource_proximity_supervision") already trains z_world with an auxiliary MSE loss
against `max(resource_field_view)` -- a SCALAR resource-proximity target -- and, critically,
**`latent.use_resource_proximity_head=true` was already active in this very run's base config**
(`ree-v3/experiments/v3_exq_724_competence_localization_diagnostic.py:338`, shared by the whole
x734/737/808/948 family; loss wired at `ree_core/agent.py::compute_resource_proximity_loss`). So
948's finding is NOT "z_world has zero resource supervision" -- it is **"z_world, even with SD-018's
scalar proximity supervision already training it, still fails to expose enough structure for a
downstream reader to clear the floor."** The positive arm succeeds only when given the FULL 25-dim
directional field, not merely a scalar magnitude -- a sharper, more specific finding than the first
draft stated, and one that points at SD-018 (same encoder, same content) as the primary amend
target rather than a fresh substrate entry. Separately: SD-018's own `metric_trajectory` records only
its PRE-implementation baseline (r2=-0.004) and no post-implementation validation despite being
marked `implemented` since 2026-04-07 -- worth a governance note in its own right.

SD-015 ("Dedicated z_resource encoder for goal-directed navigation") remains a secondary,
more-tangential cross-reference: it targets a different consumer (z_goal cosine-seeding for MECH-112
wanting/liking, not general downstream foraging competence), and its own 2026-04-14 record found
z_world unexpectedly OUTPERFORMING z_resource for goal alignment, leaving an "action-selection
integration" bottleneck open. **Open judgment call, presented to the user rather than decided here**:
amend SD-018 (primary recommendation), amend SD-015, or create a new entry.

## 7. Routing

`implement-substrate`. Draft `recommended_substrate_queue_entry` in the JSON artifact now recommends
`action: "amend"`, `target_sd_id: "SD-018"` (red-team-corrected from an initial `"create"` that missed
SD-018 entirely), while flagging the SD-018-vs-SD-015-vs-new choice as open for governance.
`severity: degrading` (weakens confidence in any foraging/navigation-relevant claim read through
z_world's default encoding; does not corrupt existing evidence outright). `substrate_paths`:
`ree_core/agent.py::compute_resource_proximity_loss`, `ree_core/latent/stack.py`,
`ree_core/latent/zworld_p0.py`.

## 8. Hypothesis-space ledger (Step 9b)

Resolves `conversion_ceiling_root` / `H-observation-interface` from `alive` (evidence_direction
`supports`, awaiting positive demonstration) to **`confirmed`** (evidence_direction `supports`,
`control_passed: true`, `non_degenerate: true`, `resolved_utc` = this run's timestamp). Does NOT
eliminate `H-substrate-ceiling` or `H-f-dominance` (design does not test them). Recommend appending a
read-across note to `H-substrate-ceiling`'s own `basis` (it currently says 813 "corroborates via the
representation route"; 948 sharpens that from corroboration to a confirmed, actionable, NAMED
mechanism) and to the question's `decision` block, both presented at the gate rather than applied
unilaterally.

## 9. Learning extracted

See JSON `learning_extracted[]`. Headline: a concrete, actionable representational gap in z_world,
confirmed by a clean, well-controlled positive demonstration; likely the same substrate need as
SD-015's still-open integration bottleneck; and a false-positive `vacuous_pass` indexer flag worth a
small (out-of-charter) tooling fix.

## 9b. User confirmation (Step 8 gate, closed)

User confirmed both recommendations: (1) route `implement-substrate` as `action: amend`,
`target_sd_id: SD-018` (not SD-015, not a new entry); (2) leave `conversion_ceiling_root`'s
`decision.decidable` at `false` -- H-substrate-ceiling and H-f-dominance remain genuinely alive and
untested by this design, so 948 sharpens one leg without closing the question.

## 10. Claim contention note

A `/governance` session (`f-dominance-regime-retest-ddbe10`, `governance-pause: cycle 2026-08-25`,
claimed 2026-08-25T17:57:39Z) is concurrently active and already holds the coordination-plane pause
covering the same file set this autopsy's own pause claim would have named. `task_claim.py open`
for the `-pause` claim was refused (exit 3, not owner) because the two claims list an identical
coordination-plane path set. The metaworker is already paused via the other session's claim for the
duration of both sessions' work, so nothing is unprotected; no duplicate pause was forced. The
artifact-write claim (covering this file pair + the hypothesis registry) succeeded cleanly with only
a scope-overlap NOTE against the same session's directory-level `evidence/` claim. Given the
session-id `f-dominance-regime-retest-ddbe10` names the H-f-dominance leg of this SAME
`conversion_ceiling_root` question, the user should be told this governance cycle is running now.
