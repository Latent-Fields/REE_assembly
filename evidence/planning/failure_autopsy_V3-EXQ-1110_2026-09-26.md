# Failure autopsy -- V3-EXQ-1110 (SD-050 comparator event latch validation) -- STAGING DRAFT

- **Status:** `awaiting_human_confirmation` (staging mode; orchestrator `orchestrate-20260924-breakthrough-c2` holds the Step 8 gate with the user)
- **Generated:** 2026-09-26T18:26:46Z, session `bt0926-ap1110`
- **Target:** `v3_exq_1110_sd050_comparator_event_latch_validation_20260926T172044Z_v3` (manifest landed phase3 eac10b25d6), `experiment_purpose: diagnostic`, outcome PASS, `claim_ids: [SD-050]`
- **Trigger:** skill trigger 2 (every diagnostic, PASS or FAIL, needs a confirmed autopsy before governance acts on it; governance Step 1.5a)
- **Machine-readable twin:** `failure_autopsy_V3-EXQ-1110_2026-09-26.json`

## 0. Premises re-measured

1. *"SD-050 stays implemented_pending_validation."* **Corrected.** In `claims.yaml`, SD-050 is `status: candidate` (demoted provisional -> candidate 2026-09-25, governance-20260925-0548). `implemented_pending_validation` is the status of the substrate_queue entry `suffering-derivative-comparator-refractory`, which is the latch build this run validates. It is not SD-050's status.
2. *"GFLAG-0562: the MECH-094 relief tag-write half was never exercised."* **Holds, and it goes further.** The MECH-057a **beta-release** reuse site was also never exercised: `beta_releases_at_event = 0` in all 6 cells, over 100 shadow bursts across both arms (1,035 per-tick events). This is stronger than "never at an event tick". A red-team probe used the driver's own config, env and step function (seed 45, latch ON, 10 episodes, Mac torch 2.10). It found beta elevated on **0 of 3,000 ticks**, with 0 commit transitions. The harness forms no commitment at all (`beta_gate_bistable=False`, no closure coupling). The third native consumer of the event flag, the SD-051 ConditionedSafetyStore (MECH-304), was not enabled. **No native consumer of the relief-completion event moved in 1110.**
3. *"Check for a dry-run manifest and exclude it from denominators."* `check_dry_run_citations.py` was run over V3-EXQ-1110, the run_id, and `--family v3_exq_1110`: 0 dry, 1 real. Nothing was excluded. The real-run denominator is 1 run, 3 held-out seeds x 2 arms = 6 cells.

## 1. Facts (no interpretation)

**Substrate.** `substrate_commit` = ree-v3 `559dd6bc` (dirty=false). The latch commit `5d308b3` is an ancestor of it. `substrate_hash 595d332e...` was stable across the run. Machine ree-cloud-2, 3,042 s. The always-core recording fields are all present: `recording_schema`, `substrate_hash`, `machine_class`, `elapsed_seconds`, `config`, `seeds`.

**Design** (driver `ree-v3/experiments/v3_exq_1110_sd050_comparator_event_latch_validation.py` @ origin/main `8e41454`):
- Arms are `ARM_LATCH_OFF` and `ARM_LATCH_ON`, both with the comparator ON. The environment is CausalGridWorldV2 with SD-022 scheduled limb damage (interval 50, prob 0.5, magnitude 0.4), `num_hazards=1`, `contamination_spread=0.0`, `heal_rate=0.002`.
- Comparator settings: window 30, drop 0.005, min_initial_norm 0.01.
- Seeds 45/46/47 are held out. Thresholds were calibrated on seeds 42/43.
- The decisive DV is within-arm and paired: an unlatched SHADOW comparator ticks on the exact `z_harm_a` norm the agent's comparator sees, and its fires are grouped into bursts separated by gaps of at least 30 ticks.

| Criterion | Measured (worst seed) | Threshold | Pass |
|---|---|---|---|
| P0 shadow train ratio / bursts (ON arm) | 14.95 (s46) / 13 (s47) | >=2.0 / >=5 | yes |
| C1 latched fires per burst (load-bearing) | 1.00 (s46) | <=1.5 | yes |
| C2 latched fires per burst (no over-suppression) | 0.83 (s45) | >=0.5 | yes |
| C3 latched ticks are a subset of shadow ticks | 0 violations | ==0 | yes |
| C4 OFF arm tick-identical to the shadow | 0 violations | ==0 | yes |
| C5 relief-block CALLS == fires, each arm | 0 mismatch | ==0 | yes |

`criteria_non_degenerate` is true for C1-C5. Per cell, ON / OFF:

| seed | ON fires | shadow fires | bursts | ON fires/burst | OFF fires | suppressed | rearms | inner valence writes | beta releases at event | residue active |
|---|---|---|---|---|---|---|---|---|---|---|
| 45 | 15 | 424 | 18 | 0.83 | 424 | 409 | 7 | 0 / 0 | 0 / 0 | False |
| 46 | 19 | 284 | 19 | 1.00 | 284 | 265 | 10 | 0 / 0 | 0 / 0 | False |
| 47 | 12 | 281 | 13 | 0.92 | 281 | 269 | 5 | 0 / 0 | 0 / 0 | False |

Recomputed checks:
- `suppressed_count == shadow_fires - fires` in every ON cell (409 / 265 / 269), so the latch bookkeeping is internally consistent.
- Totals: ON 46 fires against 989 shadow fires, a 21.5x compression.

**Cross-arm identity (Step 7b C7, recomputed).** In every seed, these are bit-identical between OFF and ON: steps, per-episode lengths, shadow_fires, shadow_bursts, norm_min/max, max_window_drop and curriculum_injections. The driver warned that trajectories *may* diverge after the first event. They did not. The latch moved the event count from 989 to 46 and moved nothing the agent did.

**Expected vs observed.** Expected: about one event per descent with the latch ON. Observed: 0.83-1.00 events per shadow burst. A "descent" here means a shadow burst: shadow fires delimited by gaps of at least 30 ticks, as the driver pre-registered (docstring lines 29-35). It does not mean one damage event. On seed 45, 89 damage onsets with a norm rise produced 18 bursts and 15 events, and 3 of the 18 bursts produced no event (C2 = 0.83). C1 is not circular: the latch's re-arm rule (a rise of at least 0.005) is not the burst-gap rule, and a jitter re-arm would fire inside a burst and fail C1. No criterion failed. The only zeros are in the consumer-side readouts, which were recorded but not scored.

## 2. Claim-layer map

**SD-050** (`design_decision`, candidate, `epistemic_category: standard`, `v3_pending: false`; depends_on SD-011, MECH-057a, MECH-091, MECH-094).
- The claim is a comparator that fires a relief-completion event on a sustained drop, reusing the MECH-057a beta release and the MECH-094 VALENCE_LIKING write.
- Its registered **CONFIRMING** test needs a stream WITHOUT scheduled injection, a descent produced by the agent's own trajectory, and **both reuse-site effects on each fire**.
- 1110 tests none of those three things. It tests the latch amendment to the comparator's output. The test did let the *latch* express itself, and it did. It did not test the *claim*.
- `claim_ids` accuracy: SD-050 is the right tag for a comparator amendment. MECH-302 and MECH-304 are correctly left untagged, because neither was exercised.

## 3. Biological-reference triage

- **Latch half.** Relief is a phasic offset signal: one burst per pain or threat offset (Tanimoto 2004 opponent timing; Navratilova 2012 relief-evoked NAc-shell DA). A per-tick train of 9-24 events per descent was a translation artefact. The latch is a faithful correction, and 1110 shows it now behaves biologically at the output.
- **Tag-write half.** Relief tagging needs an existing trace to tag, and relief-driven commitment release needs a commitment in force. In the 1110 harness both are absent:
  - No residue center is ever activated, because the loop never calls `agent.update_residue`.
  - No commitment ever forms, so beta is elevated at 0 of 3,000 probe ticks.
- The consumer silence therefore matches the missing-dependency signature exactly. It is not a latch failure. A secondary divergence is noted but not adjudicated: `update_valence` writes to the nearest active **harm**-residue center, not to a relief/safety-location trace.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | The latch amendment was tested fairly. SD-050's CONFIRMING test was not run (scheduled injection; neither reuse site exercised). |
| Biological reference | clear (latch) / partial (tag target) | One event per offset matches the biology; the nearest-harm-center tag target is untested. |
| Prerequisites | present (emission) / missing (consumers) | No active residue center; no commitment forms anywhere in this harness (0/3,000 elevated ticks; `beta_gate_bistable=False`). |
| Implementation completeness | complete (latch) | 5d308b3 is in the substrate; tripwires C3/C4 are clean. The consumer wiring (agent.py:8479-8497) is present. |
| Environment adequacy | adequate for count / wrong pressures for cause | Relief is passive heal of scheduled damage, not agent-produced (action-contingent-relief-provider, registration only). |
| Measurement adequacy | adequate (latch) | The paired shadow on the same stream is strong. C5 counts calls, which is trivially equal to fires. Consumer effects were recorded (0) but not scored. |
| Integration adequacy | **coupled but inert: STARVED UPSTREAM** | The event reaches the relief block, but the write no-ops (residue/field.py:944-946, 973-974) and the release branch is never entered. Missing links: an active residue center (no `update_residue` in the loop), and a commitment driver (none; 0 elevated ticks). |
| Scale / capacity | adequate | 3 seeds x 40 episodes x 2 arms; 50 bursts per arm. |

**Failure-location (GOV-FAILLOC-1).** This is not a failure. It is a validated PASS at the comparator-output edge. Mechanism is established and measures are established for the latch. Environment is partial: adequate for event count, inadequate for event cause. The consumer edges were never exercised, so no read of REE follows in either direction. `ree: false`.

**Evidence domain.**
- **D2** on the comparator-output edge: intervening on the latch flag changes the event flag that native consumers read, tick for tick against the paired shadow.
- **D0-D1** on every consumer edge: wired in code, none moved.
- **D3** is a measured **null by construction** in this harness: cross-arm trajectories are bit-identical. That is expected once neither arm has any event side effect, so it measures the harness, not the latch's reach in general.

**Recommended `epistemic_category`:** `standard`. The note reads: test_design scope, a substrate-readiness PASS that does not instantiate SD-050's CONFIRMING test, with no ceiling asserted and no build owed. **Recommended `evidence_direction`:** `non_contributory`, which is already the manifest value.

## 5. Learning extracted

1. **Dependency strengthened.** The SD-050 comparator is event-correct at its output with the latch ON: about one event per detected norm-descent (shadow burst), strict subset of the legacy train, latch-OFF tick-identical to legacy.
2. **Behavioural null by construction, in this harness.** Flipping the latch changed the event count 21x and changed nothing the agent did (bit-identical trajectories). In this harness the relief event has no native consumer.
3. **Integration gap (inert by starved upstream), not a defect.** In the 517/1110 harness shape, the VALENCE_LIKING write silently no-ops without an active residue center, and no commitment ever forms (`beta_gate_bistable=False`), so there is nothing to release. The superseded 517c "writes" metric and 1110's C5 both counted *calls*, not *effects*.
4. **Forward-only instrument lesson.** Any future SD-050 / MECH-302 / MECH-304 test must score consumer **effects**: inner rbf valence writes, LIKING mass delta at the written center, beta releases with beta elevated, and SD-051 prototype updates per descent. Counting relief-block calls is not enough.
5. **Design note (not adjudicated).** With no valence bounding by default, the pre-latch train would have written about 9-24 x +1.0 LIKING per descent onto a harm-residue center. The latch matters most in exactly the half 1110 did not exercise.

## 6. Scoping recommendation for SD-050 (the load-bearing caveat)

**Yes: scope the validation verdict to the latch, meaning comparator event emission.** It must not be read as validating the relief pipeline.

- **substrate_queue `suffering-derivative-comparator-refractory`:** move `implemented_pending_validation` -> **validated, scoped to event emission**. Mark the 517d failure_record item `resolved` for the EVENT-COUNT failure mode only. The validation note must state that the consumer side is NOT exercised and cite GFLAG-0562.
- **SD-050 (claims.yaml):** status stays `candidate`; direction `non_contributory`; category `standard`; `diagnostic_evidence_adjudicated: true`; `pending_retest_after_substrate: true`. Append the scoped note (draft in the JSON `recommended_evidence_quality_note`).
- **GFLAG-0562:** keep it **OPEN**. 1110 confirms it and widens it to the beta-release half. Resolve it only when the consumer half is exercised (option B), or when governance explicitly folds it into SD-050's CONFIRMING-test gate (option A).

## 7. Routing (proposal; governance ratifies and chips)

Node class: `complex (probe-gated) / puzzle (known rules)`. The frame is well posed; the missing fact is whether the latch changes the native consumers.

- **A. Scope-and-fold.** Apply the scoping in section 6 and fold the consumer half into SD-050's existing CONFIRMING-test gate. That gate needs an agent-produced descent plus both reuse sites, and it is itself gated on the registration-only `action-contingent-relief-provider` (priority 4, design doc owed). No experiment now. Cost: GFLAG-0562's question waits on an unscheduled env design.
- **B. Scope-and-probe (recommended).** Everything in A, plus one **new-number** `/queue-experiment` diagnostic, latch ON vs OFF, on a bed that has both prerequisites:
  - **Bed:** the natural candidate is **V3-EXQ-916a's**. It runs the comparator ON (`:378`), sets `beta_gate_bistable=True` (`:389`), and calls `agent.update_residue` in the loop (`:688`, `:874`). Its run had 60 relief fires; seed 1 had 0, which is a seed risk for the precondition.
  - **1110's bed cannot serve the beta half.** It forms no commitment, so the precondition would fail deterministically. Keeping it needs an explicit commitment lever (bistable latch plus a commit driver, or a scripted `beta_gate.elevate()` arm), or the beta half must be dropped.
  - **DVs:** inner VALENCE_LIKING writes per event and LIKING mass delta at the written center; beta releases at events with beta elevated, plus the elevated-tick denominator that 1110 did not record; optionally SD-051 prototype updates per descent.
  - **Precondition:** at least 1 active center and at least N beta-elevated relief ticks per seed, else `substrate_not_ready`.
  - **What it buys:** D2 on the consumer edges now, decoupled from action-contingency, which stays SD-050's CONFIRMING test. It is not a duplicate: 916a scored no consumer effects, and nothing queued or built tests them. Recommended because the breakthrough pass credits native causal reach, and 1110's harness gave the latch nothing to reach.

This is not a re-derive of the same question. It is a different question (consumer reach, not event count), which is why it gets a new EXQ number. Re-derive brake: SD-050 count = 0 before this artifact, and this PASS does not count. **Not fired.** No same-claim re-queue is refused, because none is proposed.

**Granularity-debt recurrence trigger: does not fire.** `granularity_debt_cluster.py SD-050` finds 1 prior tagging target, `gflag0452-D1-cluster#517d`, with alignment `other`, reading "strengthened at implementation level". No target reads weakened.

**Step 9b (frozen ledger):** does not apply. There is no fan-out, and the latch was never a registered hypothesis-space question. `hypothesis_space_registry.v1.json` was **not** written; the staging `hypothesis_space_ledger_pending.applies = false`.

**Read-across (not adjudicated):**
- **MECH-302:** its reuse-of-completion-machinery half remains untested.
- **MECH-304:** `ConditionedSafetyStore.update` keys on `event_fired` (agent.py:6996-7002). Historical comparator-ON MECH-304 runs therefore ran on per-tick trains, roughly 9-24 prototype updates per descent. Flag this for the MECH-304 owner.

## 8. Step 7b / 7c

- **7b.** 1 fire, **C7** (shadow_fires identical across arms). **Acted on, not dismissed.** It shows cross-arm trajectories never diverged, which strengthens the scoping and does not touch C1/C2 (those are within-ON-arm comparisons). Re-run with this `.md` present: C5 applicable and did not fire; C7 only.
- **7c.** Red-team ran on **fable** (cross-model; this draft is on Opus). Verdict: **CONTESTED**, with three verdict-moving findings, all on routing option B's specification and the beta-half wording:
  - **F1.** B's "run the full select_action path" was a no-op; 1110 already does this, and the probe shows 0/3,000 beta-elevated ticks. Confirmer: `grep beta_gate_bistable` in the 1110 driver (0 hits) vs 916a `:389`.
  - **F2.** "No commitment at relief ticks" should read "no commitment at any tick".
  - **F3.** 916a's bed already has both prerequisites.

  All three are incorporated above. The red-team **confirmed** the PASS and the arithmetic (all load-bearing numbers recomputed from cells), the scoping, the SD-050 disposition (the `diagnostic_evidence_adjudicated` tail is not already true), the substrate status move, and the GFLAG-0562 handling. Hygiene findings F4/F11/F12 are fixed. The red-team was not re-run after incorporation.

## 9. Draft evidence_quality_note (SD-050)

See `recommended_evidence_quality_note` in the JSON. It is applied verbatim by `/governance` after the user confirms.
