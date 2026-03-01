# Governance State

Generated: `2026-02-27`
Maintained: manually, updated after each governance cycle or major corpus change.

This file provides an honest snapshot of the current evidence corpus state so that
governance tooling and human reviewers can make correctly-calibrated decisions.

---

## Synthetic Evidence Contamination

All experiments conducted before 2026-02-26 used synthetic substrates:

- **ree-v2** (`_toyenv_internal_minimal` run_id suffix) — archived 2026-02-26
- **ree-experiments-lab** — archived 2026-02-26

These substrates generated plausible-looking statistical outputs but did not involve
the actual REE agent architecture. Their confidence scores, conflict ratios, and
direction counts in `claim_evidence.v1.json` are **unreliable as architecture evidence**.

The `promotion_demotion_recommendations.md` file now flags claims with zero genuine runs
with `⚠️ Synthetic data flag` and overrides the statistical recommendation with
`collect_genuine_evidence`. Do not promote or demote these claims based on the existing
confidence scores.

---

## Genuine Evidence Corpus (as of 2026-02-27)

The only valid experimental substrate is **ree-v1-minimal** (run_id suffix: `_ree_v1_minimal`).

### Completed Genuine Experiments

| EXQ | EVB | Claim(s) | Experiment | Result | Completed |
|-----|-----|----------|-----------|--------|-----------|
| EXQ-000 | EVB-0037 | MECH-059 | Control Plane Precision Separation | **PASS** | 2026-02-26T16:13Z |
| EXQ-001 | EVB-0039 | MECH-056 | Residue Trajectory Placement | **PASS** | 2026-02-26T20:52Z |
| EXQ-002 | EVB-0040 | MECH-058 | E1/E2 Timescale Ablation | **FAIL** (substrate resolution) | 2026-02-26T21:37Z |
| EXQ-003 | EVB-0041 | MECH-061 | Commitment Boundary Token Reclassification | **PASS** | 2026-02-26T22:24Z |
| EXQ-004 | EVB-0042 | MECH-057 | Control Completion Requirement | **FAIL** (informative baseline) | 2026-02-26T23:24Z |
| EXQ-005 | EVB-0043 | MECH-060, MECH-067 | **PASS** | Write-Locus Contamination | 2026-02-27T10:33Z |

### Genuine Run Counts per Claim

| Claim | Genuine Runs | Synthetic Runs | Reliable? |
|-------|-------------|----------------|-----------|
| MECH-056 | 2 | 163 | Partially — genuine PASS dominates |
| MECH-057 | 2 | 12 | Partially — genuine FAIL informative |
| MECH-058 | 2 | 156 | Partially — genuine FAIL (substrate limit) |
| MECH-059 | 2 | 164 | Partially — genuine PASS dominates |
| MECH-060 | 2 | 0 | **Yes** — genuine PASS (2 runs: smoke FAIL @5 eps, full PASS @200 eps) |
| MECH-061 | 2 | 10 | Partially — genuine PASS dominates |
| MECH-067 | 2 | 0 | **Yes** — genuine PASS (co-tested with MECH-060 in EXQ-005) |
| All other claims | 0 | varies | **Unreliable — all synthetic** |

Claims with 2 genuine runs have directionally meaningful signal but remain statistically
thin. The overall_confidence figures in `claim_evidence.v1.json` are dominated by the
larger synthetic entry counts and should be treated with caution.

---

## Claims with Reliable Status Changes (from Genuine Evidence)

| Claim | Previous Status | New Status | Basis |
|-------|----------------|------------|-------|
| MECH-059 | candidate | **active** (adjudicated) | EXQ-000 PASS + architecture decision retain_ree |
| MECH-056 | candidate | **provisional** | EXQ-001 PASS — residue placement confirmed |
| MECH-061 | candidate | **active** (adjudicated) | EXQ-003 PASS + commitment boundary confirmed |
| MECH-058 | candidate | candidate (unchanged) | EXQ-002 FAIL — substrate resolution issue |
| MECH-057 | candidate | candidate (unchanged) | EXQ-004 FAIL — informative baseline, redesign needed |
| MECH-060 | candidate | **provisional** | EXQ-005 PASS — write-locus separation confirmed (residue inflation 8520×, harm ordering met) |
| MECH-067 | candidate | **provisional** | EXQ-005 PASS — write-locus permission matrix confirmed (co-tested with MECH-060) |

---

## Pending Genuine Experimentation

*No experiments currently pending. Queue is empty.*

---

## Governance Pipeline Health

### `build_experiment_indexes.py` Modes

| Mode | When to use | What it writes |
|------|-------------|----------------|
| `python3 build_experiment_indexes.py --index-only` | After ingesting new experiment results | `claim_evidence.v1.json`, `INDEX.md`, `TODOs.md`, `decision_state.md` |
| `python3 build_experiment_indexes.py` | After full governance review | All of the above + `evidence_backlog.v1.json`, `experiment_proposals.v1.json`, `architecture_gap_register.v1.json`, `promotion_demotion_recommendations.md`, `conflicts_report.md` |

**Use `--index-only` immediately after experiment ingestion** to update the evidence matrix
without regenerating the backlog or overwriting manually-maintained planning artefacts.

Reserve the full rebuild for explicit governance review sessions.

### Backlog Stability

`evidence_backlog.v1.json` is regenerated from scratch on each full build. EVB IDs are
positional — IDs shift if the sort order changes. Do not reference EVB IDs in persistent
cross-repo documents; use claim_ids instead.

Items with `pinned: true` are preserved across regeneration. Items from the ree-v1-minimal
`experiment_queue.json` (EVB-0039 through EVB-0043) are not in the auto-generated backlog
— they live in the experimental substrate repo and are tracked via `runner_status.json`.

### Promotion/Demotion Recommendations Reliability

| Recommendation type | Reliability |
|--------------------|-------------|
| `collect_genuine_evidence` (⚠️ synthetic flag) | **High** — derived from run_id patterns, not statistics |
| Recommendations for MECH-056/057/058/059/061 | **Medium** — genuine results exist but statistics still polluted by synthetic entries |
| All other recommendations (Q-*, ARC-*, IMPL-*, etc.) | **Low** — based entirely on synthetic evidence; do not act without genuine runs |

---

## Pending Governance Decisions

| Claim | Decision | Status | Notes |
|-------|----------|--------|-------|
| Q-012 | do_not_act_synthetic_basis | `resolved` | All 8 experimental entries are synthetic (_toyenv_internal_minimal). The 4:4 split is synthetic noise. Do NOT demote. Retain candidate pending genuine ree-v1-minimal runs. evidence_quality_note added to claims.yaml. |
| MECH-040 | collect_genuine_evidence | `pending_user` | Demotion recommendation was stale (synthetic data); wait for genuine run |
| MECH-046 | collect_genuine_evidence | `pending_user` | Same as MECH-040 |
| Q-015 | no_action_required | `resolved` | Resolved by MECH-061 PASS (EXQ-003): boundary token minimal contract verified. Q-015 remains active. No further action needed. |

---

## Architecture Epoch Registry

| Epoch ID | Description | Start UTC | Source Repo |
|----------|-------------|-----------|-------------|
| `ree_hybrid_guardrails_v1` | Current planning epoch (all post-adjudication entries) | 2026-02-15T15:31Z | N/A (planning criteria) |
| `ree_v1_minimal_genuine_v1` | Genuine ree-v1-minimal experiment results | 2026-02-26T00:00Z | ree-v1-minimal |

The build scanner reads `architecture_epoch` from `manifest.architecture_epoch` (top level)
or falls back to `current_architecture_epoch` from planning_criteria. Genuine EXQ manifests
now store `architecture_epoch: ree_v1_minimal_genuine_v1` at the top level (fixed 2026-02-27).
The contamination filter in `_genuine_run_count()` also accepts the `_ree_v1_minimal` run_id
suffix as a fallback for resilience.

---

## Three-Gate BG Architecture Hypothesis (Q-019)

*Registered 2026-02-27. Status: open architectural hypothesis. Formal claim: Q-019.*
*Updated 2026-02-27: corrected E2 role (cerebellum-like) and E3 complex scope (hippocampus included).*

### The Hypothesis

The basal ganglia may implement **three functionally distinct gating loops**, not a single
action gate with three evaluation criteria:

| Loop | Biological substrate | Oscillatory signature | Function |
|------|---------------------|-----------------------|----------|
| **Sensorium gate** | Limbic loop (nucleus accumbens → VTA/VP → MD thal → vmPFC) | Beta (~15–30 Hz): high beta = suppress change, beta desync precedes new percept | Gates what the system attends to — selecting from environment AND ongoing sensorimotor loops for E3 complex attention. No trajectory generation. |
| **Thought gate** | Associative loop (caudate → GPi/SNr → MD thal → DLPFC) | Theta (~4–8 Hz): theta phase slots organise WM capacity | Gates which hippocampal trajectory proposals are maintained in working memory for E3 tactical evaluation. The E3 complex operates here. |
| **Action gate** | Sensorimotor loop (putamen → GPi/SNr → VL thal → motor cortex) | Beta desynchronisation precedes movement | Gates action execution. E3 commitment boundary. Automaticity gradient: learned tasks migrate here over time, reducing thought-loop overhead. |

**DMN relationship**: The thought loop running unconstrained (no sensorium input, no
action pressure) is the functional correlate of the Default Mode Network — hippocampal-mPFC
episodic future projection free-running in rest/prospective mode. Task onset = sensorium gate
opens, DMN activity suppresses.

**Structural re-use**: The loops are not fully separate hardware. The reticular nucleus of
the thalamus acts as an inter-loop routing switch, preventing thought-loop activity from
bleeding back into sensorium processing. Shared thalamic substrate: mediodorsal thalamus
(sensorium + thought loops), VL thalamus (action loop). The residue field spans all loops —
harm accumulated wherever it occurs.

**Control plane gates (separate from BG loops)**: The E1 update gate and E2 update gate
live in the control plane. They govern precision/salience routing — what gets to update the
slow world model (E1) and what gets to update the fast transition model (E2). These are
distinct mechanisms from the BG sensorium gate, operating on a different axis: model update
eligibility vs attentional selection for thought-loop processing.

### E3 Complex (Revised Scope — Now Large)

The E3 complex spans both the thought and action loops and is larger than previously
described:

| Component | Role |
|-----------|------|
| **Hippocampal map** | Affectively-weighted map of viable trajectory space, shaped by the residue field. Proposes paths by navigating this terrain — not by running transition predictions. Forward/backward replay during offline integration consolidates the map. |
| **Trajectory proposal** | Hippocampus nominates candidate trajectories into working memory (thought loop). |
| **Tactical evaluation** | Uses E1 (long-horizon world model context) and E2 (fast local transition checks, `state + action → next_state`). E2 is cerebellum-like — a fast forward predictor, NOT a trajectory generator. |
| **Commitment gating** | E3 commit boundary — the action loop gate. Authorises irreversible action execution. |
| **Back-projections** | Suppress thought-loop trajectory candidates that fail commitment criteria before full evaluation. This feedback path does not exist in current ree-v1-minimal. |

### REE Pipeline Implications

Current ree-v1-minimal implements the **single-gate model** — E3 applies all gating at
action selection time. If the three-gate model is correct:

```
Control plane (separate from BG loops):
  E1 update gate — precision/salience routing for slow world model updates
  E2 update gate — motor error signal routing for fast transition model

env.step() → [SENSORIUM BG GATE] → LatentStack.encode()
              ↕ selects from env AND ongoing sensorimotor loops
         → [THOUGHT BG GATE / E3 complex]:
              hippocampal map (residue-weighted terrain) proposes trajectories
              E2 provides fast transition checks; E1 provides long-horizon context
              tactical evaluation under E3 oversight
              ← back-projections suppress failing candidates (not in ree-v1-minimal)
         → [ACTION COMMITMENT GATE / E3 complex]:
              commit boundary → motor execution
              feedback: improved metrics → task migrates to sensorimotor loop
                       → less sensorium BG gate overhead (automaticity)
                         error residue re-elevates for deliberate oversight
```

**Current mislabelling in ree-v1-minimal**: `E2FastPredictor.generate_candidates()` is
doing hippocampal trajectory-proposal work under a cerebellum label. E2 should be a pure
fast transition model (`state + action → next_state`). Future refactoring will separate:
- **E2** → fast transition prediction (cerebellum-like, primarily sensorimotor loop)
- **Hippocampal module** (part of E3 complex) → trajectory proposal + affective terrain map

**MECH-057 scope**: "Control completion" may operate in both the thought loop (hippocampal
trajectory sequence completion before promotion to action consideration) and the action loop
(motor completion before new precision updates). Currently MECH-057 is scoped to action loop
only. See MECH-057 `evidence_quality_note` for scope-revision flag.

### Literature to Extract (EVB-PINNED-Q019)

**Status: COMPLETED 2026-02-27.** All 6 papers extracted to `evidence/literature/targeted_review_q_019/entries/`. 97 total literature entries in index.

| Paper | Evidence direction | Entry ID |
|-------|-------------------|----------|
| O'Reilly & Frank (2006) PBWM | supports | 2026-02-27_q019_oreilly_frank_2006 |
| Hazy, Frank, O'Reilly (2007) | supports (strongest) | 2026-02-27_q019_hazy_frank_oreilly_2007 |
| Aron et al. (2007) IFC-STN hyperdirect | supports | 2026-02-27_q019_aron_2007 |
| Brittain & Brown (2013) beta oscillations | supports | 2026-02-27_q019_brittain_brown_2013 |
| Buckner et al. (2008) default network | mixed (indirect) | 2026-02-27_q019_buckner_2008 |
| Crick (1984) TRN searchlight | supports | 2026-02-27_q019_crick_1984 |

---

## Substrate Debt Register

Implementation misapprehensions that have accumulated and affect experiment interpretation.
Tracked here to prevent knowledge drift and guide future refactoring.

### SD-001: E2FastPredictor.generate_candidates() labelled as E2 but doing E3/hippocampal work

**Filed:** 2026-02-27
**Priority:** medium
**Blocking:** architectural redesign of hippocampal module in ree-v1-minimal

E2's role in REE architecture is a **fast cerebellum-like transition model**: `f(z_t, a_t) → z_{t+1}`. It should predict what latent state results from taking action `a` from state `z`.

Currently `E2FastPredictor.generate_candidates()` performs **hippocampal trajectory proposal** — enumerating and evaluating multiple full action sequences. This is E3 complex work (hippocampal map navigation) incorrectly housed in E2. Consequences:

- EXQ-006 E2_FROZEN condition tests "no trajectory proposal" rather than "no transition prediction"
- MECH-058 experiments cannot cleanly separate E2 transition accuracy from E3 trajectory planning
- Any experiment comparing E1 vs E2 roles is partially conflated

**Future separation needed:**
- `E2FastPredictor` → pure fast transition: `forward(z, a) → z_next` (action-conditioned MLP, cerebellum-like)
- `HippocampalModule` (new, part of E3 complex) → trajectory proposal by navigating affective terrain, not by running transition predictions

**Impact on current results:** EXQ-006 and EXQ-007 results remain valid as behavioral baselines. The PASS/FAIL verdicts measure system-level harm reduction; the substrate debt affects mechanistic interpretation only.

### SD-002: E1/E2 relationship — mutually constitutive, not merely orthogonal

**Filed:** 2026-02-27
**Priority:** low (documentation/framing; architectural implication for training)
**Blocking:** nothing currently — framing update + future E2→E1 autotrain pathway

MECH-058's `latent_stack.e1_e2_timescale_separation` label is incomplete. The correct framing has two layers:

**Layer 1 — Knowledge orthogonality:**
- **E1 = associative engine** ("register of what IS"): action-unconditioned LSTM, learns what latent states associate with across timescales — harm patterns, affective valence, semantic context (e.g. "arm-up associates with throwing"). No action input.
- **E2 = transition model** ("how things change"): action-conditioned `f(z_t, a_t) → z_{t+1}`. Learns kinematic sequences — "neutral → raising → peak → extension → release." Fast feedforward MLP.

**Layer 2 — Mutual constitution (confirmed 2026-02-27):**
E1 and E2 are not simply parallel systems with orthogonal outputs. They are co-constitutive:

1. **E2 scaffolds E1**: E2's transition sequence is the temporal evidence stream from which E1 distills associations. The association "arm-up → throwing" only becomes learnable because E2 provides the ordered kinematic chain that instantiates it. Without transition structure, the association would require many raw observations to converge. E2 narrates the transition; E1 registers the pattern.

2. **E2 autotrains E1** (aspiration, not yet implemented): E2's forward predictions can generate synthetic temporal sequences that E1 learns from, without waiting for ground-truth observations. This is the "autotrain" pathway: E2 rolls out a simulated trajectory, E1 updates its associative model on that rollout. Currently E1 is trained only on actual observations (`compute_prediction_loss()`); the E2→E1 autotrain path is future work.

3. **E1 primes E2**: E1's associative prior conditions E2's transition predictions. Knowing "this is a throwing pattern" (E1 association) lets E2 anticipate upcoming transitions more accurately — arm extension predicts release, not retraction. The current architecture partially implements this: E1 generates a prior that is passed to E2's rollout. The full bidirectional loop is:
   ```
   E2 transitions → temporal scaffolding → E1 association distillation
   E1 association → predictive prior → E2 transition smoothing/context
   ```

**Implication for EXQ-006:** The E1_FROZEN condition breaks not only E1's associative learning but also the E1→E2 prior conditioning. The E2_FROZEN condition breaks not only transition predictions but also the temporal scaffolding that would train E1. Results should be interpreted at the system level (harm reduction) rather than as clean isolation of individual components.

**Action:** Update `docs/architecture/e2.md` to capture mutual constitution. Add E2→E1 autotrain as a future architectural item. Update MECH-058 claim scope if EXQ-006 yields clean results.

### SD-003: E2 as self-attribution substrate — isolatability requirement not captured

**Filed:** 2026-02-28
**Priority:** high (V2 design requirement)
**Blocking:** V2 entry criteria, any experiment testing self-attribution or counterfactual reasoning

E2 as a pure transition model `f(z_t, a_t) → z_{t+1}` is not merely a predictive
sub-component — it is the architectural substrate for:

1. **Counterfactual self-attribution**: "what would have happened if I had acted
   differently?" requires running E2 forward with a counterfactual action. This is
   the mechanism by which the system distinguishes agent-caused from
   environment-caused transitions — the foundation of self-modelling.

2. **Self-modelling**: the agent's causal footprint in the world is precisely what
   E2 encodes. Without an isolatable E2, there is no clean substrate for the agent
   to model its own contribution to observed outcomes.

3. **Attribution reliability extension**: MECH-060/067 (write-locus contamination,
   PASS) confirmed that harm attribution requires clean signal separation between
   pre-commit and post-commit channels. E2 provides the action-conditioned baseline
   for that separation. Counterfactual E2 queries extend this to retrospective
   attribution across completed action sequences.

**Why V1 cannot test this:**
- SD-001 conflates E2 with hippocampal trajectory generation — E2 is not isolatable
  as a pure transition model in the current codebase
- V1 environment (stateless hazard grid) has no persistent agent causal footprint —
  there is no regime where agent-caused and environment-caused transitions need to be
  disambiguated, so the self-attribution signal cannot arise
- Counterfactual querying requires E2 to be a clean forward model callable with an
  arbitrary action; currently it is entangled with trajectory selection logic in E3

**V2 entry requirement (added):**
E2 must be implemented as an isolatable pure transition model before self-attribution
experiments can be designed. Counterfactual E2 querying (`e2.forward(z, a_counterfactual)`)
must be architecturally possible and independently testable. The environment used for
V2 qualification must include persistent agent causal footprint — actions at step N
should affect the landscape at step N+k in ways that require disambiguation from
independent environment change.

**Interpretation caution for V1 evidence:**
Any V1 claim that touches agent contribution to outcomes (MECH-057 control completion,
MECH-058 E1/E2 roles, MECH-063 candidate selection) should be interpreted with the
caveat that self-attribution capability was not testable on this substrate. The
behavioural verdicts stand; the mechanistic interpretation of *why* they hold or fail
is incomplete without an isolatable E2.
