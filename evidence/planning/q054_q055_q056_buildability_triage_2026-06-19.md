# Q-054 / Q-055 / Q-056 buildability triage

**Date:** 2026-06-19T19:07Z
**Author session:** Q-054/Q-055/Q-056 buildability triage (interactive)
**Mandate:** The three questions were carrying mechanical `hold_pending_v3_substrate`
recommendations applied from `implementation_phase: v3`. User framing: *"if we have enough
to build then we should do; otherwise look into what we can do to progress the issue."*
This doc replaces the blanket holds with a per-question disposition. **No claim status was
changed by this session** (open_questions stay `open`; dependency claims untouched). The
buildable experiments are *sketched, not queued* — queueing waits on user confirmation.

| Q | Disposition | One-line reason |
|---|---|---|
| **Q-054** | **BUILDABLE-NOW** (deferral is STALE) | Its 2026-06-16 deferral was gated on the GAP-A conversion ceiling; that ceiling was **lifted 2026-06-17** (V3-EXQ-569i PASS). |
| **Q-055** | **BUILDABLE-NOW** | Sleep substrate fully built with on/off + replay-ablation knobs; SD-017 STABLE, ARC-065 STABLE; the diversity DV is reachable. |
| **Q-056** | **BLOCKED-ON-SUBSTRATE** | Blocker part 1 (modulatory selection authority) is now implemented, but blocker part 2 (stuck-state detector + difficulty-gated proposal-entropy regulator) is genuinely unbuilt and not even on the substrate_queue. |

---

## Q-054 — ARC-062 minimum trajectory-class diversity floor

> *What is the minimum Rung-1 `first_action_entropy` floor for the ARC-062 context
> discriminator to learn a reliable reef-vs-foraging cut? Is the SP-CEM 0.497-nat lift
> sufficient, or is a higher floor needed?*

### Disposition: BUILDABLE-NOW — the hold is stale

The claim's `governance_2026_06_16` note **DEFERRED** narrowing as "PREMATURE" with an
explicit, single reason: *"Q-054's answerability is explicitly gated on the
behavioral_diversity_isolation:GAP-A conversion ceiling"* and at that time (569h
non_contributory) the ceiling persisted — *"committed behaviour does not move with the
channel range (569g/682), [so] discriminator accuracy cannot be read as a function of
realised first_action_entropy."*

**That precondition is now satisfied.** One day after the deferral:

- `behavioral_diversity_isolation_plan.md:12` — *"RESOLVED 2026-06-17 — V3-EXQ-569i PASS
  (the TOP-K shortlist conversion falsifier) cleared the conversion ceiling: committed-action
  diversity C_R1B strict-above BOTH matched-noise AND proposer ... The behavioural diversity
  REACHES committed action — GAP-A's conversion frontier is closed. ARC-065 substrate_ceiling
  LIFTED -> standard."*
- `substrate_queue.json` — "Modulatory score-bias selection authority at E3.select" =
  `status: implemented`.

So *realised* first-action entropy can now be made to move committed behaviour (via the
top-k shortlist conversion), which is the exact precondition the deferral said was missing.
The diversity-floor sweep is now readable.

### Substrate readiness
- ARC-062 `candidate`; its discriminator substrate is BUILT (`ree_core/policy/gated_policy.py`
  gated-policy heads + 3-stream context discriminator, exercised across the 654-series
  experiments). **ARC-062's candidacy does not block measuring its discriminator's floor** —
  this is a sweep over an existing substrate, not a promotion test.
- Entropy-injection knobs exist: `ree_core/policy/noise_floor.py`
  (`noise_floor_min_temperature`, `noise_floor_alpha`) and `structured_curiosity.py`
  (`curiosity_novelty_weight`) — the two levers named in `what_would_answer`.
- MECH-313 / MECH-314 = `candidate_substrate_landed`; ARC-065 = `stable`.

### Open risk to flag (does NOT block the build)
The 569i top-k conversion is the *validated PARTIAL* circumvention of the shared
MECH-439 F-dominance selection root, with a thin 2/3-seed margin. Whether it holds on the
ARC-062 / CRF rule-bias path *specifically* is the in-flight V3-EXQ-654g test (queued/owed,
not yet adjudicated; see `arc_062_rule_apprehension_plan.md`). The Q-054 sweep is robust to
this either way: if the discriminator stays at chance across **all** entropy levels, that
itself diagnoses a residual conversion ceiling (route to MECH-439), rather than producing a
vacuous null — so it is non-vacuous by construction. Optionally sequence after 654g
adjudication if we want the converting substrate confirmed on this path first.

### Experiment sketch (ready for /queue-experiment, pending confirmation)
- **Design:** graded entropy SWEEP (≥4 levels) on the SD-054 reef substrate, ARC-062
  gated-policy + 3-stream discriminator ON, **569i top-k shortlist conversion armed**
  (`use_modulatory_shortlist_then_modulate` + `modulatory_shortlist_mode=top_k`), MECH-341
  preserver ON. Sweep realised first-action entropy via `noise_floor_min_temperature`
  (and/or `curiosity_novelty_weight`) across e.g. {below 0.497, ≈0.497 (SP-CEM), 0.75, 1.0+ nats}.
- **DV:** ARC-062 context-discriminator accuracy (reef vs forage) **and** TV distance
  `TV(P(a|s_reef), P(a|s_forage))` at probe-state pairs, plotted against *measured* upstream
  first_action_entropy per arm.
- **PASS / answer condition:** the floor is bracketed — locate the entropy value below which
  discriminator accuracy is at chance and above which it rises monotonically; report whether
  0.497 nats sits above (sufficient) or below (insufficient) it.
- **Non-vacuity / readiness gates:** (R1) realised first_action_entropy actually varies
  across arms (range > floor) — else the sweep is vacuous, self-route
  `substrate_not_ready_requeue`; (R2) top-k conversion non-vacuous (committed-class entropy
  ARM-converted != collapsed proposer); (R3) discriminator is trained / non-degenerate
  (z-context variance > floor). If accuracy is flat-at-chance across all arms WITH R1–R3 met
  → residual conversion ceiling, route /implement-substrate (MECH-439), NOT a floor result.
- **claim_ids:** `[ARC-062]` (discriminator floor is what's directly tested); cross-ref
  ARC-065 / MECH-313 / MECH-314 as the entropy-source substrates. (Tag conservatively per the
  claim_ids accuracy rule — this tests the discriminator floor, not ARC-065 promotion.)
- **Naming:** Rung-2 lineage successor (acceptance-criteria doc names V3-EXQ-543b for the
  4-arm Rung-2 test); a floor-sweep variant gets a new EXQ number under /queue-experiment.

---

## Q-055 — Sleep consolidation: preserve or erode ARC-065 diversity?

> *Does SD-017 SWS-phase consolidation preserve the trajectory-class diversity ARC-065
> achieves during waking, or does Hebbian winner-take-all replay erode it?*

### Disposition: BUILDABLE-NOW

### Substrate readiness — fully built
- SD-017 = `stable` (acceptance-criteria doc: "Rung 5", read-side consumer confirmed by
  V3-EXQ-565 PASS). ARC-065 = `stable` (the diversity-to-be-eroded is demonstrated, and now
  reaches committed action via 569i). MECH-120 = `candidate` (the Hebbian-erosion RISK this
  question tests). INV-049 = `candidate`.
- Sleep substrate built: `ree_core/sleep/{phase_manager, replay_sampler,
  cross_module_consolidation, routing_gate, bayesian_aggregator, self_model_aggregator,
  sleep_onset_gate}.py`.
- **Ablation knobs all present** in `ree_core/utils/config.py`: `sws_enabled`, `rem_enabled`
  (sleep ON/OFF), `sws_consolidation_steps`, `replay_diversity_enabled`,
  `reverse_replay_fraction`, `random_replay_fraction`, `surprise_gated_replay`. `phase_manager`
  honours `require_sleep_passes_enabled` + the `sws_enabled`/`rem_enabled` gates, so a clean
  sleep-OFF control is a config toggle.

### Scoping note (the one nuance)
The acceptance-criteria doc sequences **Rung 3** (persistence) *after Rung 2* (TV switching),
and Rung 2 (V3-EXQ-543b ≈ the Q-054 floor work) is **not yet cleared**. So the *full* Rung-3
TV-switching persistence check should ideally wait on Rung 2. **However**, the user's actual
question — does sleep erode ARC-065's trajectory-class diversity — is answerable *now* on the
**committed-action-class diversity DV (TrajDiv / C_R1B)**, which IS cleared (569i, ARC-065
stable). Run on that DV; add the TV-switching persistence leg once Rung 2 lands.

### Scientifically interesting prior to state up front
ARC-065's diversity now reaches committed action via the **569i top-k shortlist conversion**,
which is a *selection-layer* mechanism, not learned synaptic weights. Sleep replay strengthens
*weights* (Hebbian). So the erosion pathway MECH-120 predicts may not even touch a
selection-layer diversity source — a genuine, falsifiable open prediction the experiment will
settle (and a clean way to dissociate "diversity lives in weights" vs "diversity lives in the
selector").

### Experiment sketch (ready for /queue-experiment, pending confirmation)
- **Design (Rung-3 persistence, acceptance-criteria doc):** run agent to convergence with
  ARC-065 ON + 569i conversion armed; measure diversity DVs at convergence (t0); +200 episodes
  with forced exploration OFF, measure (t1); +5 SLEEP CYCLES (`sws_enabled=True`), measure (t2).
- **Arms:** (A) sleep-ON (`sws_enabled=True`) vs (B) sleep-OFF (`sws_enabled=False`) — the
  "must hold WITH sleep active" criterion makes the OFF arm the control; (C) replay-diversity
  ablated (`replay_diversity_enabled=False` / `random_replay_fraction=0`) to test the
  counter-mechanism that replay is *designed* to sample diverse trajectories.
- **DV:** TrajDiv / committed-action-class diversity (C_R1B) at the three time points; ≥3 seeds.
- **PASS:** diversity at t2 within 50% of t0 AND not collapsed to a single dominant class,
  WITH sleep active. **Erodes** → falsifies MECH-120-as-protective, supports an erosion risk
  (ARC-065 must also operate during consolidation → new MECH). **Preserves** → supports
  SD-017 + INV-049. **Increases** → broader episodic-replay sampling (surprising).
- **Non-vacuity gates:** (R1) sleep cycles actually fire (consolidation write-passes > 0,
  `sws_enabled` effective); (R2) t0 diversity is supra-floor (there is diversity TO erode —
  else vacuous); (R3) the sleep-OFF arm differs from sleep-ON on *some* consolidation metric
  (else the knob is inert).
- **claim_ids:** `[SD-017, MECH-120]` primary (preserve-vs-erode is the direct test);
  cross-ref ARC-065 / INV-049.

---

## Q-056 — Stuck-state-gated proposal entropy beats off AND always-high?

> *Does stuck-state-GATED proposal entropy outperform BOTH entropy-off and always-high
> entropy? (MECH-343 main prediction.)*

### Disposition: BLOCKED-ON-SPECIFIC-SUBSTRATE

This is the genuine blocked case — do **not** queue a 3-arm experiment against a mechanism
that does not exist. MECH-343's own `evidence_quality_note` names the block:
`epistemic_category=substrate_conditional` ... blocked on (1) the
modulatory-bias-selection-authority gap AND (2) *"a difficulty-gated proposal-entropy
regulator (stuck-state detector + transient CEM temperature/candidate-count gain + decay)
**not yet designed**."*

### Status of the two blockers (verified this session)
1. **Modulatory-bias-selection-authority gap — NOW RESOLVED.** `substrate_queue.json`:
   "Modulatory score-bias selection authority at E3.select" = `implemented` (the 569i top-k
   shortlist conversion / E3.select authority). So part (1) no longer blocks.
2. **Difficulty-gated proposal-entropy regulator — GENUINELY UNBUILT.** Confirmed by code +
   queue search:
   - **No** stuck-state detector and **no** difficulty-gated entropy hook anywhere in
     `ree-v3/ree_core/` (grep: `stuck` / `impasse` / `gated_entropy` / `difficulty_gat` →
     no module).
   - **No** matching `substrate_queue.json` entry (search on
     difficulty/stuck/proposal_entropy/impasse/entropy_regulator → none).
   - What *does* exist is **adjacent but not the mechanism**: `cingulate/dacc.py` computes a
     `choice_difficulty` scalar (std of per-candidate EVs) and `salience_coordinator.py`
     routes a `dacc_difficulty` signal toward an `internal_planning` bias — a difficulty
     *signal*, but no closed loop that gates PROPOSAL entropy on a stuck-state. And
     `policy/noise_floor.py` (MECH-313) is the **wrong locus**: it is *state-independent*
     (uniform temperature lift every waking tick) and lifts the **action-selection** softmax,
     not **proposal-generation** entropy — explicitly distinct from difficulty-gating per its
     own docstring and per MECH-343's notes.

### Named missing substrate → route to /implement-substrate
Two coupled components, to be added as a new `substrate_queue.json` entry:

1. **Stuck-state / impasse detector.** Integrate existing signals — repeated goal-progress
   stall, dACC `choice_difficulty` (built), low E3 score margin (MECH-090 admission predicate
   exists), low committed-action diversity — into a graded/binary "stuck" gate, guarded by
   preserved goal salience (stuck-WITH-goal, not goal-abandoned). Ingredients exist
   (`dacc.choice_difficulty`, `salience_coordinator`); the integrated detector emitting a
   stuck signal does not.
2. **Difficulty-gated proposal-entropy regulator.** A transient gain on **proposal-layer**
   entropy — ARC-018 hippocampal/CEM candidate-set widening + within-class sampling
   temperature — gated ON by detector (1), held under goal/harm scoring, with commitment
   deferred until a candidate clears the score-margin threshold (MECH-090 / MECH-342) and
   entropy **decay** once goal progress resumes. Locus = CEM / hippocampal-rollout proposal
   generation, NOT `noise_floor.py`.

### After the substrate lands (then, and only then, /queue-experiment)
The discriminating 3–4-arm experiment (EXP-0176 /
`docs/thoughts/2026-06-03_difficulty_gated_proposal_entropy.md`):
- **Arms:** (1) entropy-gating OFF; (2) entropy-gating ON under stuck-state; (3) entropy
  ALWAYS high; (4) entropy high with goal/harm constraints ablated (diagnostic only, if safe).
- **Env:** hard-goal/blocked-path with **matched easy-goal controls**.
- **Metrics:** candidate proposal entropy, committed-action entropy, score-margin
  distribution, # arbitration cycles before commitment, goal progress, harm rate, action
  churn, time-to-first-workable-path, entropy reduction after success.
- **PASS:** arm 2 > arms 1 and 3 on goal progress, no harm/churn increase, post-success
  entropy narrowing.
- **claim_ids:** `[MECH-343]` (+ cross-ref MECH-341 / ARC-018).

---

## Routing summary

- **Q-054** → present sketch for confirmation → on confirm, `/queue-experiment` (floor sweep,
  569i conversion armed). The stale `governance_2026_06_16` deferral should be retired next
  governance cycle (do not narrow-suppress on the lifted-ceiling reason any more). *No status
  change here.*
- **Q-055** → present sketch for confirmation → on confirm, `/queue-experiment` (Rung-3
  persistence, sleep ON/OFF + replay-ablation, committed-class-diversity DV).
- **Q-056** → `/implement-substrate`: stuck-state detector + difficulty-gated proposal-entropy
  regulator (add substrate_queue entry). Do **not** queue the 3-arm experiment until that
  substrate lands + a contract/smoke validates. *MECH-343 stays candidate / substrate_conditional
  / v3_pending — unchanged.*

> If a buildable experiment (Q-054 / Q-055) is queued and runs, it may itself clear the
> mechanical hold on the next governance cycle — noted, but NO claim status was changed by this
> session.
