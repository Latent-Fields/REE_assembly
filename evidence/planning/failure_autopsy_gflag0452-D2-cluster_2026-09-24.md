# Failure autopsy (STAGING) -- GFLAG-0452 D2 cluster: 6 PASS manifests whose contrast or control cannot discriminate the claimed mechanism

- **Status:** `awaiting_human_confirmation` (staging mode; the Step 8 gate is held by the parent `/governance` session `governance-20260924`)
- **Generated:** 2026-09-24T09:11:28Z
- **Source:** GFLAG-0452, user decision rec-20260924-34e4e088. Skim input: `gflag0250_pass_driver_skim_20260924.{md,json}` (key `runs`)
- **Claims:** SD-035 (stable), ARC-065 (stable), MECH-033 (active)
- **Machine-readable companion:** `failure_autopsy_gflag0452-D2-cluster_2026-09-24.json`

These are evidence-purpose PASSes, re-adjudicated because the governance driver skim classed each one D2 (the contrast holds by construction, the control was not matched, or the ablation is confounded). This file does not edit claims.yaml, manifests, review_tracker, substrate_queue, governance flags or the hypothesis registry. Every write is a recommendation for `/governance` to apply.

## 1. Dry-run gate (Step 2a)

`scripts/check_dry_run_citations.py` was run over all 6 targets and the two sibling manifests:

| run_id | dry? | note |
|---|---|---|
| v3_exq_501_sd035_amygdala_analog_vs_binary_20260429T192730Z_v3 | clean | target |
| v3_exq_615_arc065_rung1_matched_entropy_20260531T093116Z_v3 | clean | target |
| v3_exq_615_arc065_rung1_matched_entropy_20260531T082211Z_v3 | **DRY** | excluded, not evidence. It is already direction-superseded. The prior autopsy (`failure_autopsy_MECH-341-cluster_2026-05-31`) wrongly described it as a real FAIL with 1/3 seeds: it ran 1 seed, p1=1, 10 steps. |
| v3_exq_171_mech033_kernel_chain_pair_20260329T213946Z_v3 | clean | target |
| v3_exq_171_mech033_kernel_chain_pair_20260330T070404Z_v3 | clean | byte-identical duplicate; already superseded |
| v3_exq_184_mech033_kernel_chain_pair_20260401T185611Z_v3 | clean | target |
| v3_exq_184_mech033_kernel_chain_pair_20260404T161554Z_v3 | clean | target |
| v3_exq_308_mech033_kernel_chain_discriminative_20260409T183908Z_v3 | clean | target |

**Recording provenance:** none of the 6 manifests has a top-level `substrate_hash` or `recording_schema`. All of them predate the 2026-07-12 recording standard, and 615 also has no `config`. These gaps do not block adjudication, because every defect below can be seen in the driver source and the recorded per-seed cells.

## 2. Per-target reconstruction and skim verification

### V3-EXQ-501 -- SD-035 (skim: D2_contrast_by_construction) -- **CONFIRMED, and stronger than the skim**

- There is no agent, no environment and no training. The approach logit is hand-authored in the driver (`:68-73`) and scored against `sigmoid(4*valence)` (`:75`). In `BINARY_SIGN_ONLY` (`:53-56`), every same-sign input becomes the constant 1.0.
- The substrate modules (`ree_core.amygdala` BLAAnalog/CeAAnalog) are called. On the positive half, though, harm_level=0, so mode_prior=fast_prime=0 and the logit is plain driver arithmetic (3*v).
- **Half-split recompute from `condition_results`, all 3 seeds:**
  - Positive half (substrate not engaged): ANALOG RMSE ~0.048 vs BINARY ~0.183.
  - Negative half (CeA/BLA engaged): ANALOG is slightly **worse**, 0.155-0.156 vs 0.148-0.153. CeA mode_prior stays at 0.0 below harm ~0.5, a dead zone.
  - The PASS margin (rmse_reduction 0.308/0.314/0.316) therefore comes entirely from the half where the substrate does nothing.
- The seeds are a deterministic grid plus a +/-0.015 jitter, so they are pseudo-replicates.
- The claim-layer question was not tested. SD-035's registered falsifiers are (A) CeA ON-vs-OFF on mode-switch latency with a zeroed-prior control and (B) live-loop BLA threat-vs-neutral recall. The claim's own `what_would_answer` already admits that 501 "substituted an ANALOG-vs-BINARY contrast instead".

### V3-EXQ-615 -- ARC-065 (skim: D2_control_not_matched) -- **CONFIRMED and EXTENDED; re-adjudicates a confirmed prior autopsy**

- ARM_1 MATCHED_NOISE records entropy 0.0 with 1 class in all 3 seeds, identical to BASE_OFF. `MATCHED_NOISE_ALPHA=0.3` was never tuned (`:150-155`, "may need tuning"), so C2 (`:504-506`) reduces to ARM_2 minus 0.
- **Structural, not just mistuned.** The prior autopsy's own mechanism note says MECH-313 noise needs a multi-class candidate pool, and the non-SP-CEM proposer emits single-class pools. ARM_1 could not have matched ARM_2's entropy at any alpha. The FP-2 question (is the structure beyond entropy-matched noise?) could not be asked in this design.
- **New: episode-length confound.** Selected-action totals over 60 P1 episodes work out to:
  - ARM_2: about 26/21/11 steps per episode.
  - ARM_0/ARM_1: about 184-197 steps per episode on seeds 42/44.
  - `done = health_depleted or step cap` (`causal_grid_world.py:3354-3356`), and the P1 loop breaks on `done`. The ALL_ON agent dies about 7-17x sooner, so its "diversity" is measured over short episodes that end in harm.
  - Seed 43 ARM_0/ARM_1 averages only about 6 steps per episode, which is also anomalous.
- **Re-adjudication read.** I read `failure_autopsy_MECH-341-cluster_2026-05-31` in full. Its 615 reading is Measurement `adequate`, Implementation `complete` ("matched-noise control correctly isolates the architectural commitment"), claim_alignment `strengthened`, and "clean architectural-necessity discrimination". That is the "control that cannot discriminate by construction, graded adequate" failure. **What else this change moves:**
  - That artifact's cluster reading "Definitive positive answer to ARC-065 architectural-necessity question (615...)" loses its basis.
  - Its readings about MECH-341 and Q-054 (614b/616) are untouched.
- **Withdrawn-argument record.** The old reading was "MECH-313 alone cannot reproduce ALL_ON diversity, therefore the distributed pathway is necessary". It still holds as an implementation-layer fact: MECH-313 does nothing without a multi-class proposer. It is not a discrimination of structured diversity from noise.

### V3-EXQ-171 / V3-EXQ-184 (x2) / V3-EXQ-308 -- MECH-033 (skim: D2_ablation_confound) -- **CONFIRMED**

- **The ablation removes more than E2 seeding.** ABLATED/NO_CHAIN is `random.randint` (171 `:342`, 184 `:346`, 308 `:529`). It removes the trained HarmHead and the planner along with E2 seeding, so any harm-aware selector would beat it.
- **All four runs share one comparator.** The random arm is fixed by environment and seed and does not depend on any trained module. At seed 42 the harm_rate is 0.061516023781776445 with 4179 events: bit-identical in 171, 184-0401 and 184-0404, and equal to within 1e-16 in 308. Seeds 7 and 13 behave the same way across 184 x2 and 308.
- **There is no hippocampal module** (the encoders are inline Linear layers).
- **The "k=3 chain" is not a multi-step rollout.** It is one action followed by two forced STAY steps (`a_oh[ACTION_DIM-1]=1.0`), which amounts to one-action lookahead with persistence.
- **The claim asks for a different manipulation.** MECH-033's spec is "ablate the E2-kernel-to-hippocampal handoff while leaving rollouts and E3 scoring otherwise intact". These runs did the opposite.
- **184 double count.** 0401 and 0404 share the driver, the seeds 42/7/13 and a bit-identical NO_CHAIN arm. They are *not* byte duplicates: KERNEL_CHAIN differs through training nondeterminism (seed 7 has 13 vs 21 events). This differs from the 171 0329/0330 pair, which was byte-identical, and 0330 is already superseded. **Recommendation:** 0401 keeps the weight; 0404 -> `superseded`. One design x seed set is one weight unit, and the EXQ versioning policy does not treat a re-run under the same ID as a new replicate. The red-team alternative, non_contributory for both, is recorded below. Either way the weight effect is nil.
- **The rest of MECH-033's support.** V3-EXQ-055 is the only run with a real HippocampalModule and a matched-budget comparator (AO_CHAIN vs SELF_CHAIN). But:
  - It is a single seed (`--seed` default 0).
  - SELF_CHAIN harm is 0.0684, which is 91% of RANDOM's 0.0754.
  - cal_gap_self is 0.021, below 055's own C4 floor of 0.03.
  - So it is a weak discrimination too.

## 3. Claim-layer map

| Claim | type / status | Did the test let the claim express itself? | Stated-evidence problem |
|---|---|---|---|
| SD-035 | design_decision / stable, no epistemic_category | No. The contrast quantises the input; it does not remove the substrate. | `live_status.evidence.from` cites 501; `what_would_answer` lists 501 as "behavioral discrimination that the analog form is load-bearing" |
| ARC-065 | architectural_commitment / stable, epistemic_category standard | Partly. ALL_ON-vs-nothing ran; structured-vs-noise did not. | The evidence_quality_note leans on 569i "strict-above BOTH matched-noise AND the proposer" (see read-across) |
| MECH-033 | mechanism_hypothesis / active, no epistemic_category | No. There is no hippocampal stage and the ablation removes everything. | `what_would_answer` says "measured four times" / "fired four times"; the live_status source (grandfathered r5 autopsy) carries a "replicated 4x PASS" reading |

## 4. Biological-reference triage

- **SD-035:** BLA/CeA graded valence and salience coding. Literature is present (`targeted_review_sd_035`, `targeted_review_amygdala_analog`). Not a formal import. The failure is in the test harness, not the translation.
- **ARC-065:** distributed motor and behavioural variability (LC-NE tonic noise, frontopolar/striatal curiosity, hippocampal sampling). Literature is present (`targeted_review_arc_065_behavioral_diversity_generation`). Biologically, a noise channel with nothing to vary over is inert, which fits ARM_1's collapse. That makes it a design observation, not claim evidence.
- **MECH-033:** hippocampal forward sweeps and preplay seeded by action-conditioned forward models. Literature is present (`targeted_review_connectome_mech_033`). The runs contain no hippocampal stage to seed, so the mechanism is represented only symbolically.

## 5. Four-layer diagnosis

| Layer | 501 / SD-035 | 615 / ARC-065 | 171, 184x2, 308 / MECH-033 |
|---|---|---|---|
| Claim alignment | unclear (not expressed) | unclear (FP-2 untested) | unclear (not expressed) |
| Biological reference | clear | partial | clear |
| Prerequisites | present | present (ARM_2); absent for ARM_1's lever | present (E2 r2 0.95-0.99) |
| Implementation | substrate complete; harness is a driver-authored readout | partial: ARM_1 noise floor inert by DEFECT (neutralising default: single-class proposer) | partial: no HippocampalModule; the chain is one action plus STAYs |
| Environment | absent (synthetic sweep) | partial (~7-17x survival mismatch) | adequate for harm avoidance |
| Measurement | misleading (contrast by construction) | misleading (C2 = C1; no control-entropy precondition) | misleading (random ablation; shared constant comparator) |
| Integration | isolated | coupled but inert (ARM_1). To make it live, inject noise at the final selection or give ARM_1 SP-CEM with the structured channels off, and gate on \|H_ARM1 - H_ARM2\| <= 0.15 | isolated (inline toy, not REEAgent) |
| Scale | n/a (pseudo-replicate seeds) | adequate | adequate |

**Failure-location (GOV-FAILLOC-1).** Every target is MIXED: MEASURES failed and MECHANISM is partial, and 615 is also partial on ENVIRONMENT. **None of these is chargeable to REE.** These PASSes are also not evidence *for* the claims.

## 6. Cluster pattern

| Experiment | Claim | Absolute / positive criterion | Discrimination criterion | Read |
|---|---|---|---|---|
| 501 | SD-035 | analog RMSE low | analog vs binary: margin comes only from the substrate-free half | contrast by construction |
| 615 | ARC-065 | ARM_2 Rung-1 3/3 (short, harm-terminated episodes) | ARM_2 - ARM_1 with ARM_1 = 0.0 | control not matched (structurally) |
| 171 | MECH-033 | E2 r2 >= 0.2 | chain vs uniform random | ablation confound |
| 184-0401 / 184-0404 | MECH-033 | E2 r2 >= 0.2 | chain vs uniform random, same comparator | ablation confound + same-ID re-run |
| 308 | MECH-033 | E2 r2, prox r2 | chain vs uniform random, same comparator | ablation confound |

**One structural property, not N independent bugs.** Three claims show three design shapes, and one gate is missing from all of them. No pre-registered precondition asserted that the control or ablation arm differs from the treatment **only** in the named mechanism, or that the matched control reached its matched value. Each PASS was then read as support for the mechanism. The planning decision this forces has two parts:
- (a) evidence-weight correction for all three claims;
- (b) a candidate design-review rule: a matched or ablation control must carry a precondition gate, or the run self-routes to precondition_unmet. This is the parent's call; it is not proposed as a standing-rule edit here.

## 7. Learning extracted

- An ablation that quantises the INPUT tests how much information the input carries. It does not test the substrate.
- A random-action ablation removes every learned component at once and cannot isolate one link in a chain.
- A deterministic random comparator reused across runs makes N runs one comparison.
- A matched control needs a precondition gate on the matched quantity. A "matched" control at zero entropy should be precondition_unmet, not PASS.
- A noise lever acting on a single-class pool is inert by construction.
- Entropy compared across arms whose survival differs by 7-17x is not comparable.

## 8. Recommended dispositions (for the Step 8 gate)

| Run | Recommended direction | epistemic_category | `change` tail |
|---|---|---|---|
| 501 | non_contributory | standard | `-> epistemic_category: standard` (SD-035 has no category today) |
| 615 | non_contributory (supersedes the 615 disposition in failure_autopsy_MECH-341-cluster_2026-05-31) | standard (already set on ARC-065) | `-> stamp this cluster artifact` |
| 171 | non_contributory | standard | `-> non_contributory` |
| 184-0401 | non_contributory (canonical; keeps weight) | standard | `-> non_contributory` |
| 184-0404 | superseded (by 184-0401) | standard | `-> superseded` |
| 308 | non_contributory | standard | `-> epistemic_category: standard` (MECH-033 has no category today) |

**Status recommendations (recommend only, not applied):**
- **SD-035: stays stable.** 501 was never load-bearing for its status (473/474/659/762/888 carry it). Re-point `live_status.evidence.from` and correct the `what_would_answer` line.
- **ARC-065: stays stable for now, flagged for review.** Its remaining matched-noise discrimination, V3-EXQ-569i, has the same inert-control shape (read-across below). If 569i is confirmed D2, recommend stable -> provisional.
- **MECH-033: recommend active -> provisional.** This is an evidence-weight correction, not a falsification. Once 171/184/308 are non_contributory and 184-0404 superseded, only V3-EXQ-055 remains: one seed, with a near-random SELF_CHAIN comparator. Alternative: hold at active with `live_status.needs_review: true` until the fan-out reports. Also recommended: `governance_flag.py raise --flag-type stale_note` for the "measured four times" wording and the r5-autopsy "replicated 4x" reading (the parent's call).

**Draft evidence_quality_notes:** exact text is in the JSON per target (`recommended_evidence_quality_note`).

**Read-across, not adjudicated here:** in V3-EXQ-569i (`v3_exq_569i_..._20260616T224009Z_v3`), ARM_2_MATCHED_NOISE (proposer at T=2.5) is bit-identical to ARM_0_PROPOSER in all 3 seeds, down to `selected_class_counts`.
- **Mechanism:** proposer-summary arms have route_range 0.0, so the top-k pick `softmax(-mod_eligible/T)` (`e3_selector.py:4344-4347`) is uniform at every T on the same RNG stream.
- **The driver agrees:** 569i's own `negative_control` note says the control does not gate the verdict.
- **Consequence:** ARC-065's "strict-above BOTH" reading reduces to "above the proposer" (ARM_1 beat it in 2/3 seeds by ~0.08-0.10 nats and scored 0.0 on seed 43).
- **Recommendation:** add 569i to the GFLAG-0452 D2 population.

## 9. Routing (proposal; the parent ratifies at Step 2b; no chips spawned)

- **SD-035 / 501:** governance-reclassification only. An optional, not-owed literal EXQ-A (CeA ON-vs-OFF mode-switch latency with a zeroed-prior control) goes through `/queue-experiment` if governance wants the letter of SD-035's registration closed. 7b pointer: substrate entry `item-level-recall-probe-central-vs-peripheral` may be the instrument for the literal EXQ-B.
- **ARC-065 / 615: GOV-FANOUT-1 portfolio** (`queue-experiment`, routed by governance). Live hypotheses:
  - H1-structured: diversity has structure beyond entropy-matched noise.
  - H2-entropy-equivalent: diversity is indistinguishable from matched noise.
  - H3-survival-artefact: diversity is thrash in short, harm-terminated episodes.

  Legs, each with a declared null:
  - (measurement) action-context mutual information at matched entropy, with a precondition gate `|H_noise - H_ALL_ON| <= 0.15`;
  - (algorithm) SP-CEM-only plus per-seed temperature tuned to ALL_ON entropy;
  - (environment) survival-matched entropy window.

  Settle the 569i read-across first.
- **MECH-033 / 171-184-308: GOV-FANOUT-1 portfolio.** Live hypotheses:
  - H1-chaining: multi-step chaining carries the effect (the claim).
  - H2-one-step: one E2 forward step is enough.
  - H3-no-E2: the HarmHead alone is enough.

  Legs:
  - (representation) k=0 HarmHead-greedy;
  - (algorithm) k=1 vs k=3 with policy-driven continuation instead of STAY;
  - (integration) E2-scrambled with the HarmHead and planner intact, which is the claim's own specified manipulation;
  - (instrumentation) a full REEAgent HippocampalModule seeded by E2 vs random kernels at matched CEM budget, after first checking 055's SELF_CHAIN for random-level degeneracy.

  A single new letter on the old design is refused because it would inherit the confound.
- **Re-derive brake:** does not fire. No target reads substrate_ceiling; each is an instrument/test-design defect that owes no build (R3 step 2).
- **Granularity-debt trigger:** does NOT fire.
  - MECH-033: 0 tagging targets (+2 superseded).
  - SD-035: 0.
  - ARC-065: 16 targets, alignment intact=9 / unclear=4 / strengthened=2 / coarse=1, none `weakened`.
  - Nothing in this cluster reads `weakened` either.

## 10. Step 7b / 7c

- **7b** (`autopsy_pre_routing_checks.py`, first draft): 2 C2 fires.
  - 501 -> `item-level-recall-probe-central-vs-peripheral`: dismissed for routing, but kept as a pointer for SD-035's literal EXQ-B.
  - 615 -> MECH-314a-Phase-2-impl / INF-ENV-002 / SD-056 / q092 umpire harness: dismissed, because none of them provides a matched-entropy control. q092 is nearest for the measurement leg.
  - C5 and C7 were inapplicable.
  - A re-run on the final draft gave 0 fires.
- **7c red-team** was run cross-model on **fable**; the drafting session is on Opus 5.5. **Verdict: CONTESTED (narrow).**
  - **The contest:** the 184-0404 "duplicate manifest" rationale was false, because the KERNEL_CHAIN cells differ. I checked this with a per-seed diff. The rationale is now corrected. The superseded disposition is kept, and the red-team alternative (non_contributory for both) goes to the gate.
  - **Hygiene accepted:**
    - the 501 half-split finding;
    - the 615 ratio, now 7-17x;
    - 308's random arm is equal to within 1e-16, not bit-identical;
    - the 184-0401 tail trimmed;
    - a MECH-033 category tail added;
    - 055 stated as n=1;
    - the second stale-note site named;
    - the prior autopsy's wrong description of the 615 dry sibling.
  - **Confirmed:** every D2 verdict, the episode-length confound, the 569i read-across with its mechanism, and the MECH-033 status call (neither over- nor under-reaching).

## 11. Hypothesis-space ledger (Step 9b) -- PENDING, not written

None of the 6 runs is a registered leg, so there are no Mode B resolutions. Two **Mode A new questions** are drafted under `hypothesis_space_ledger_pending` in the JSON, each with 3 legs, alive, with pre-registration set at apply time:
- `mech033_kernel_chaining_isolation`
- `arc065_structured_vs_noise_diversity`

No existing `qid` is touched, so no growth_restriction check applies. Every axis value is already in `axis_families.map`. Mode D (H-other) did not fire, because no pattern-level signal outside a partition applies to non-discriminating PASSes.

## 12. Routing decision confirmed by the user

**PENDING.** The parent `/governance` session holds the Step 8 gate.
