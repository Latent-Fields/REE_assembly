# V3-EXQ-490c Successor Decision Tree

Pre-written 2026-04-29T06:01Z. Goal: when V3-EXQ-490c lands, the next
iteration is one `/queue-experiment` invocation away rather than one
`/diagnose-errors` plus one `/queue-experiment`.

V3-EXQ-490c (running on DLAPTOP-4.local at time of writing) tests
whether MECH-295 liking-bridge ON top of MECH-269b V_s gating ON unblocks
the EXQ-483 / EXQ-490b wired-but-inert phenotype (zero approach_commit,
zero dACC behavioural-adjustment).

## Outcome routing

For each combination of C1-C4 outcomes, this doc names the exact next
EXQ to queue (or substrate change to commission). All branches that lead
to an immediate next EXQ have the queue entry template ready below — no
new substrate work needed, only configuration / score-bias-composition
adjustment in the experiment script.

```
PASS (C1+C2+C3+C4)             -> queue V3-EXQ-495 (V3-full-completion-gate)
FAIL on C4 only                -> /diagnose-errors (wiring bug, NOT a new EXQ)
FAIL on C1 only                -> /diagnose-errors (config drift; 490b ON_ON arm no longer firing)
FAIL on C2/C3 with C1+C4 PASS  -> queue V3-EXQ-490d (cue_gain sweep)
                                  AND/OR V3-EXQ-490e (GoalState seeding)
                                  AND/OR V3-EXQ-490f (direct E3 injection)
                                  -- pick by sub-signature; see below
FAIL on C2 only with C3 PASS   -> queue V3-EXQ-490f (candidate-set vs bias)
FAIL on C3 only with C2 PASS   -> queue V3-EXQ-490d (bias magnitude)
                                  -- only happens if approach_commit
                                  -- climbed without dACC bundle moving
```

## Branch interpretation (by sub-signature)

After 490c lands, read the following manifest fields to select the
correct successor:

| Sub-signature                       | Reading                                    | Successor |
|-------------------------------------|--------------------------------------------|-----------|
| C2 FAIL, bridge_n_cue_fires_total > 0 in ON_ON, dacc_score_bias_mean > ON_OFF | bridge fires but bias too weak vs E3 cost  | **490d** cue_gain sweep |
| C2 FAIL, bridge_n_cue_fires_total ~ 0 in ON_ON, despite drive_weight=2.0 | upstream gate (drive < min_drive_to_fire OR goal_norm < min_z_goal_norm_to_fire) blocking bridge | **490e** GoalState seeding |
| C2 FAIL, bridge_n_cue_fires_total > 0, dacc_score_bias_mean ~ 0 | bridge cue write happens but isn't reaching score_bias | **490g** instrumentation probe |
| C2 FAIL, bridge_n_cue_fires_total > 0, ALL of 490d / 490e / 490f had been tried | candidate set lacks goal-approaching trajectories; bias can't help | escalate to substrate work on CEM proposer / E3 candidate generation |

## Branch 490d -- Cue-gain sweep (4-arm parametric)

**Trigger:** 490c FAIL on C2 with C1+C4 PASSing AND bridge_n_cue_fires_total > 0
in ON_ON AND ON_ON.dacc_score_bias_mean > ON_OFF.dacc_score_bias_mean
(non-zero delta but not enough to flip behaviour).

**Hypothesis:** liking-bridge cue-side bias magnitude is too small to
override other E3 cost terms. Sweeping mech295_liking_to_approach_cue_gain
upward should monotonically increase approach_commit if the bias
direction is correct.

**Substrate change required:** NONE. All knobs are in
REEConfig.from_dims.

**Arms (4):**
| Arm     | cue_gain | drive_to_liking_gain |
|---------|----------|----------------------|
| g050    | 0.5 (default) | 1.0 (default) |
| g100    | 1.0      | 1.0 |
| g200    | 2.0      | 1.0 |
| g500    | 5.0      | 1.0 |

V_s rollout gating ON in all arms with the 490b smoke threshold override
(0.85/0.85/0.95). Bridge ON in all arms. Other config matches 490c
exactly.

**Acceptance:**
- C1: gate fires in all arms (re-verify 490b precondition, sanity check).
- C2: monotone increase in approach_commit_count across cue_gain in
  >=2/3 seeds (higher gain -> more approach behaviour).
- C3: at least one arm hits approach_commit > 0 in >=2/3 seeds.
- PASS = C1 AND C2 AND C3.

**FAIL branches:**
- C2 PASS but C3 FAIL -> bias direction is right but ceiling is reached
  before behaviour flips. Routes to 490f (direct injection) for stronger
  evidence the candidate set is the bottleneck.
- C2 FAIL (no monotone) -> bias direction or composition is wrong.
  Routes to 490g instrumentation probe.

**Queue entry template:**
```json
{
  "queue_id": "V3-EXQ-490d",
  "claim_id": "Q-040",
  "claim_ids": ["Q-040", "MECH-295"],
  "title": "MECH-295 liking-bridge cue_gain sweep (490c-FAIL successor: bias-magnitude branch)",
  "script": "experiments/v3_exq_490d_mech295_cue_gain_sweep.py",
  "experiment_purpose": "evidence",
  "machine_affinity": "any",
  "priority": 5,
  "estimated_minutes": 480,
  "episodes_per_run": 80,
  "seeds": 3,
  "conditions": 4,
  "status": "pending",
  "note": "Successor to V3-EXQ-490c FAIL on C2 with C1+C4 PASSing AND bridge fires but bias delta insufficient. Tests whether monotone increase in mech295_liking_to_approach_cue_gain unblocks approach_commit. claim_ids = ['Q-040', 'MECH-295'] -- 490d's monotone signature directly tests MECH-295 weak reading at the magnitude level (PASS supports MECH-295 cue-side biasing function; FAIL on monotone weakens it). experiment_purpose=evidence."
}
```

**evidence_direction_per_claim contract:** must include
`{"Q-040": ..., "MECH-295": ...}`; on monotone PASS both supports; on
non-monotone FAIL Q-040 inconclusive but MECH-295 weakens (the cue is
not behaving as a bias-magnitude lever).

## Branch 490e -- GoalState seeding strengthening (2-arm)

**Trigger:** 490c FAIL on C2 AND bridge_n_cue_fires_total ~= 0 in ON_ON
arm despite drive_weight=2.0 (so the bridge IS configured but never
fires). This means one of the upstream gates is blocking:
- `mech295_min_drive_to_fire` (default 0.1; effective_drive < 0.1)
- `mech295_min_z_goal_norm_to_fire` (default 0.05; goal_norm < 0.05)

**Hypothesis:** GoalState is not being seeded sufficiently from
z_resource for goal_norm to clear the floor. Lowering the floor and
verifying drive elevation should raise bridge fire count, after which
the C2/C3 question can be re-tested.

**Substrate change required:** NONE. All knobs in REEConfig.from_dims.

**Arms (2):**
| Arm     | min_drive_to_fire | min_z_goal_norm_to_fire | drive_to_liking_gain |
|---------|-------------------|--------------------------|----------------------|
| baseline | 0.1 (default)    | 0.05 (default)           | 1.0 (default) |
| relaxed  | 0.01             | 0.005                    | 2.0 |

V_s gating ON in both with 490b override. Bridge ON in both.

**Acceptance:**
- C1: gate fires in both arms.
- C2 (PROXY for "did relaxation reach the upstream gate"):
  bridge_n_cue_fires_total in relaxed arm > baseline arm by >=10x.
- C3: relaxed arm bridge_cue_bias_mean_max_abs > baseline arm.
- C4 (BEHAVIOURAL): relaxed arm approach_commit_count > 0 in >=2/3 seeds.
- PASS = C1 AND C2 AND C3 AND C4.

**FAIL branches:**
- C2 FAIL with C1 PASS -> upstream gate is NOT the blocker; the bridge
  is silent for some other reason. Route to 490g instrumentation probe.
- C2 PASS C4 FAIL -> bridge fires more often but still doesn't move
  behaviour. Compose with 490d (gain sweep).

**Queue entry template:**
```json
{
  "queue_id": "V3-EXQ-490e",
  "claim_id": "Q-040",
  "claim_ids": ["Q-040"],
  "title": "MECH-295 liking-bridge GoalState seeding strengthening (490c-FAIL successor: upstream-gate branch)",
  "script": "experiments/v3_exq_490e_mech295_seeding_strengthening.py",
  "experiment_purpose": "evidence",
  "machine_affinity": "any",
  "priority": 5,
  "estimated_minutes": 240,
  "episodes_per_run": 80,
  "seeds": 3,
  "conditions": 2,
  "status": "pending",
  "note": "Successor to V3-EXQ-490c FAIL on C2 with bridge_n_cue_fires_total ~ 0 (upstream gate blocking the bridge). Lowers mech295_min_drive_to_fire and mech295_min_z_goal_norm_to_fire and raises drive_to_liking_gain to verify the gate is what's silencing the bridge. claim_ids = ['Q-040'] only -- the relaxation is a config probe, not a hypothesis test of MECH-295's weak reading. experiment_purpose=evidence (architectural Q-040b test)."
}
```

## Branch 490f -- Direct E3 goal-proximity injection (2-arm)

**Trigger:** 490c FAIL on C2 with C1+C4 PASSing AND 490d cue_gain sweep
already showed monotone-but-insufficient response (or as a parallel
discriminator alongside 490d when compute is available).

**Hypothesis:** the candidate set itself doesn't include
goal-approaching trajectories at sufficient density. The bridge can't
move behaviour by biasing toward candidates that don't exist. Bypassing
the bridge and injecting goal_proximity DIRECTLY into the E3 score_bias
isolates whether the bottleneck is bias magnitude OR candidate
generation.

**Substrate change required:** NONE -- the direct injection happens at
the script level (inside select_action analog inside the eval loop, or
via a custom override on E3.select). No agent code changes.

**Arms (2):**
| Arm           | bridge_active | direct_e3_goal_bias_active | direct_gain |
|---------------|---------------|----------------------------|-------------|
| bridge_only   | True          | False                      | 0.0         |
| direct_only   | False         | True                       | 5.0 (or whatever 490d found maximally effective) |

Both arms with V_s gating ON + 490b threshold override.

The direct injection in arm B computes goal_proximity per candidate
(same formula MECH-295 uses internally) and adds -direct_gain *
proximity directly to the dacc_score_bias before E3.select(). No
upstream gates, no goal_norm floor, no drive multiplier.

**Acceptance:**
- C1: gate fires in both arms.
- C2: direct_only arm produces approach_commit > 0 in >=2/3 seeds.
- C3 (DIAGNOSTIC, not a pass criterion):
  - C2 PASS in direct_only AND C2 FAIL in bridge_only -> bridge magnitude
    is the bottleneck, not the candidate set. Route to 490d cue_gain
    increase (or commission MECH-295 magnitude tightening as a substrate
    change).
  - C2 FAIL in direct_only too -> candidate set is the bottleneck.
    Escalate to substrate work on CEM proposer / E3 candidate
    generation (bigger work; not a config-only fix).

**Queue entry template:**
```json
{
  "queue_id": "V3-EXQ-490f",
  "claim_id": "Q-040",
  "claim_ids": ["Q-040"],
  "title": "Direct E3 goal-proximity injection vs MECH-295 bridge (490c-FAIL successor: candidate-set-vs-bias branch)",
  "script": "experiments/v3_exq_490f_direct_e3_goal_bias.py",
  "experiment_purpose": "diagnostic",
  "machine_affinity": "any",
  "priority": 5,
  "estimated_minutes": 240,
  "episodes_per_run": 80,
  "seeds": 3,
  "conditions": 2,
  "status": "pending",
  "note": "Successor to V3-EXQ-490c FAIL on C2 with C1+C4 PASSing. Discriminates whether the bottleneck is bridge magnitude (PASS direct_only AND FAIL bridge_only) or the candidate set itself (FAIL both). Direct injection bypasses MECH-295 module; bias added at script level inside eval loop. claim_ids = ['Q-040'] only. experiment_purpose=diagnostic (this is a discrimination probe between competing root causes, NOT a claim hypothesis test)."
}
```

**Note on diagnostic classification:** 490f is `diagnostic` even though
it produces an interpretable signal for Q-040, because the direct
injection is a non-biological probe (no MECH-295 substrate) used to
discriminate between two upstream causes. evidence_direction_note must
explicitly flag this; per claim direction = "non_contributory" or
"inconclusive" depending on outcome.

## Branch 490g -- Instrumentation probe (NOT auto-queued)

**Trigger:** 490c or 490d/e produces a metric pattern that doesn't fit
any of the above interpretations -- e.g.:
- bridge_n_cue_fires_total > 0 AND dacc_score_bias_mean ~ 0 (bridge
  writes but bias doesn't compose into the dACC bundle).
- bridge_n_cue_fires_total > 0 in ON_OFF arm (severance broken;
  C4 FAIL with bridge gain=0 not zeroing the cue path).
- vs_gate_total_held in either arm has flipped relative to 490b ON_ON.

**Action:** route to `/diagnose-errors`. NOT pre-queued. The diagnosis
will produce either a code-level fix to MECH-295 or VsRolloutGate, OR a
bespoke instrumentation EXQ tagged on Q-040 + the affected MECH claim.

## Branch on-PASS -- Queue V3-EXQ-495 V3-full-completion-gate

**Trigger:** 490c PASS (C1+C2+C3+C4 all PASS).

**Action:** queue V3-EXQ-495 (V3-full-completion-gate, MECH-163 dual
systems test, currently deferred per `update-docs-nightly` 2026-04-29).

V3-EXQ-495 was pending on the V_s + bridge combined-cluster validation;
490c PASS clears that gate. The 495 design is already drafted in
ree-v3/CLAUDE.md V3 full completion gate section; one /queue-experiment
invocation lifts it from drafted to queued.

If 490c PASSes via 490d/490e/490f instead of directly, the same path
applies after the successor lands.

## Substrate-change escalation paths (NOT immediate)

If multiple successors fail, escalation routes that require substrate
work (NOT immediate /queue-experiment):

1. **MECH-295 magnitude tightening** (commission as SD-???-extension if
   490d cue_gain sweep saturates without behavioural payoff): re-design
   the cue-side write to use a different per-candidate signal (e.g.,
   z_goal latent inner product with first-step z_world rather than
   GoalState.goal_proximity) or compose multiplicatively rather than
   additively with dACC score_bias.

2. **CEM proposer goal-conditioning** (commission if 490f shows
   candidate-set bottleneck): extend HippocampalModule.propose_trajectories
   to bias proposal toward goal-approaching trajectories (not just via
   E3 evaluation but at the proposal stage). MECH-293 ghost-goal probes
   already do this for inactive anchors; extending to the active
   GoalState would be an analogous substrate move.

3. **Phase 2 forward-predictor V_s** (commission if smoke threshold
   override is itself the confound; see MECH-269b strong-reading
   discussion in 490b note): wire the staleness_accumulator into
   VsRolloutGate.gate() before the threshold comparison so MECH-269b
   stale-stream-discrimination becomes testable without smoke
   thresholds. This is the path-3 escalation flagged in 490b's
   `evidence_direction_note`.

These escalations are out of scope for the immediate successor tree; if
reached, they require `/implement-substrate` runs first.
