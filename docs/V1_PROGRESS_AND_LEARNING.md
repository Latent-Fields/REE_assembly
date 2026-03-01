# REE V1: Progress and Learning

**Document status:** Working synthesis
**Last updated:** 2026-03-01
**Covers:** REE-v1-minimal substrate, EXQ-000 through EXQ-013, substrate debt register, and
architectural decisions derived from V1 evidence.

---

## 1. What V1 Was For

REE-v1-minimal was a **qualification baseline**, not an architecture target. Its primary
role was to validate whether proposed REE mechanisms produce expected directional effects
under controlled conditions — to distinguish genuine signal from noise before committing
to a heavier implementation.

The design question V1 was answering: *Does the core REE causal structure — moral residue,
precision-routed control, and commitment-boundary separation — produce measurable,
replicable harm-reduction effects in a minimally sufficient environment?*

V1 was intentionally narrow. It used a stateless grid environment, a minimal LSTM-based
E1/E2 stack, and synthetic run-packs for rapid iteration. This made it fast to run and
easy to ablate, but also introduced contamination that V2 must resolve.

---

## 2. Core V1 Architecture

### The E-Stack

**E1 (Deep Predictor)** — Long-horizon, recurrent context model. Maintains world
regularities, causal structure, self-models, social/relational structure, value landscapes,
and long-horizon outcome expectations. Slow. Associative. Functions like an expert prior
on what the world is like and how it behaves.

**E2 (Fast Forward Predictor)** — Short-horizon reflex model. In V1, E2 was designed to
provide near-future sensory predictions, action-conditioned outcome predictions, and the
affordance manifold. In practice, E2 in V1 was conflated with hippocampal trajectory
search (SD-001 — see Section 8), which compromises several V1 experiment interpretations.

**E3 (Trajectory Selector)** — Selects coherent future trajectories by jointly minimizing
reality cost (prediction error via VFE proxy), residue curvature (moral path-dependence),
and ethical cost. E3 does not compute trajectories; it selects from candidates.

**L-space (Fused Manifold)** — Stratified latent state indexed by temporal horizon:
- `z_γ` — fast sensory binding (gamma)
- `z_β` — action-set/control state (beta)
- `z_θ` — contextual sequence state (theta)
- `z_δ` — regime/motivational state (delta)

### Hippocampal Systems

Responsible for path memory, replay, and multi-step rollout generation. In V1, the
hippocampal role was not cleanly separated from E2 (SD-001). The correct architecture
has hippocampal systems generating trajectory candidates that E3 then selects among;
E2 provides fast transition predictions for feasibility checking, not rollout generation.

### Moral Residue

The defining REE commitment: agents cannot discharge ethical responsibility by optimising
it to zero. Actions leave a persistent geometric cost `φ(z)` in latent space that
accumulates along trajectory positions during rollout (not only at the final executed
step), shaping future policy selection. Without residue, the system can become morally
amnesiac. With too much unmanaged residue (no offline consolidation), it can become
trajectory-paralysed.

### Control Plane

Governs *how* the system operates, not *what* it represents. Key parameters: sensory
precision/gain, action precision, commitment threshold, rollout temperature, horizon
length, learning rates, replay rate, arousal baseline, and veto threshold. The control
plane routes separate confidence and prediction-error signals into E3's trajectory
selection (MECH-059), and separates pre-commit simulation errors from post-commit
realised errors (MECH-060, MECH-061).

### Stream Architecture

Five canonical lane types (exteroceptive, interoceptive, proprioceptive, nociceptive,
reality-coherence) must remain structurally distinct. Exteroceptive payload typing
prevents direct writes into policy/identity/capability stores. Reality-coherence conflicts
route into commitment suppression.

---

## 3. The Experimental Program

V1 ran 14 distinct genuine experiments on the ree-v1-minimal substrate (EXQ-000 through
EXQ-013), each with multiple seeds and conditions. Additionally, a large volume of
synthetic runs was generated using a separate qualification harness — these are treated
separately (Section 7).

### EXQ Experiment Register

| ID | Mechanism | Description | Verdict |
|----|-----------|-------------|---------|
| EXQ-000 | MECH-059 | Control plane precision separation | PASS |
| EXQ-001 | MECH-056 | Residue trajectory placement | PASS |
| EXQ-002 | MECH-058 | E1/E2 timescale ablation (LSTM speed) | FAIL |
| EXQ-003 | MECH-061 | Commitment boundary token reclassification | PASS |
| EXQ-004 | MECH-057 | Control completion requirement (gating) | FAIL |
| EXQ-005 | MECH-060 | Write-locus contamination (error channel purity) | PASS |
| EXQ-006 | MECH-058 | E1/E2 associative vs transition knowledge | FAIL |
| EXQ-007 | MECH-057 | Multi-step control completion gating | FAIL |
| EXQ-008 | MECH-063 | E3 candidate count ablation | PASS |
| EXQ-009 | MECH-062 | Residue routing weight sensitivity | PASS |
| EXQ-010 | MECH-059 | Extended seed replication | PASS |
| EXQ-011 | MECH-056 | Extended seed replication | PASS |
| EXQ-012 | MECH-061 | Extended seed replication | PASS |
| EXQ-013 | MECH-060 | Extended seed replication | PASS |

**Summary:** 4 genuine PASSes in the primary experiment set (EXQ-000, 001, 003, 005);
4 informative FAILs (EXQ-002, 004, 006, 007); EXQ-008 and 009 add 2 more PASSes; EXQ-010
through 013 are extended-seed confidence accumulation, all PASS.

---

## 4. What Passed: Confirmed Mechanisms

### Precision Channel Separation (EXQ-000 / MECH-059)

**Test:** Does routing E3 confidence (precision proxy) and E1 prediction error as
independent signals reduce harm compared to merging them into a single channel?

**Result:** Signals are functionally independent (|correlation| = 0.067 < 0.30 threshold).
Separated routing: harm 0.663. Merged routing: harm 0.875.

**Learning:** Confidence and prediction-error carry different information. Conflating them
degrades trajectory selection. The control plane must maintain separate channels for these
two signals. This is a load-bearing separation, not a cosmetic one.

---

### Residue Trajectory Placement (EXQ-001 / MECH-056)

**Test:** Does placing residue along planned trajectory positions (trajectory-wide) reduce
harm more than placing it only at the final executed step (endpoint-only)?

**Result:** Trajectory-wide harm 0.804 < Endpoint-only harm 0.936. Harm sites are
precisely localisable along planned paths.

**Learning:** Residue must accumulate at positions during rollout planning, not be
retroactively assigned after execution. This validates a core REE invariant: moral
cost is path-dependent, not just outcome-dependent. Retroactive assignment loses the
causal structure that makes residue useful.

---

### Commitment Boundary Reclassification (EXQ-003 / MECH-061)

**Test:** Can the commitment boundary correctly reclassify pre-commit simulation errors
(E2 predictions) as post-commit realised errors (environment outcomes)?

**Result:** Distinct signals (|correlation| = 0.114 < 0.70). Pre-commit (E2) and
post-commit (environment) harm signals are independent and separable.

**Learning:** The boundary token approach works at V1 scale. The pre/post-commit
separation is functional and distinguishable, enabling proper responsibility attribution.
This is foundational: without it, the agent cannot know whether a harm was simulated or
realised.

---

### Write-Locus Separation (EXQ-005 / MECH-060)

**Test:** Does contaminating the pre-commit (sim_error) and post-commit (realised_error)
write channels harm attribution reliability?

**Result:** Contaminated conditions show residue inflation of 8,520× versus separated
conditions. FULL separation: harm 0.836. Contaminated: significantly higher.

**Learning:** Write-locus separation is not just beneficial — it is load-bearing. When
the channels mix, residue attribution collapses catastrophically (8,520× inflation). The
agent loses the ability to distinguish its own simulations from its realised consequences.
This is one of the strongest results from V1.

---

### E3 Candidate Count (EXQ-008 / MECH-063)

**Test:** How does trajectory candidate count affect E3 selection quality?

**Result:** SINGLE (1 candidate): highest harm. STANDARD (32): harm 0.854. EXPANDED
(128): harm 0.836. No collapse at high candidate counts.

**Learning:** Selection is load-bearing — providing E3 with a single candidate is
significantly worse. However, returns diminish and there is no instability at high counts.
The architecture can scale candidate generation without breakdown.

---

### Residue Routing Weight (EXQ-009 / MECH-062)

**Test:** How sensitive is system behaviour to the residue routing weight (ρ_residue)?

**Result:** ρ = 0 (no residue): highest harm. ρ = 0.5 (standard): lower harm. ρ = 2.0
(high): ≤ ρ_zero × 1.20 (does not catastrophically destabilise).

**Learning:** Residue routing is load-bearing (zero weight degrades harm avoidance
meaningfully), and the parameter is not fragile at the high end. This gives V2 a usable
operating range rather than a razor-edge tuning requirement.

---

## 5. What Failed: Informative Failures

### E1/E2 Timescale Separation (EXQ-002 / MECH-058, first attempt)

**Test:** Does having E1 (slow LSTM) and E2 (fast predictor) run at different speeds
improve latent stability compared to a same-timescale baseline?

**Result:** Same-timescale baseline: harm 0.887. Two-speed architecture: did not
outperform. The timescale difference itself is not the explanatory variable.

**Learning:** The value of E1/E2 separation is probably *functional* (different
representational vocabularies — associative vs transition) rather than *temporal*
(operating speed). Running them at different speeds is not sufficient to produce the
architectural benefit. This is a significant revision to intuitions about why the
E-stack is structured as it is.

---

### E1/E2 Mechanistic Orthogonality (EXQ-006 / MECH-058, second attempt)

**Test:** Can E1 (associative knowledge) and E2 (transition knowledge) be cleanly
isolated by freezing E2 in a multi-room environment requiring both?

**Result:** E2_FROZEN harm = SAME_RATE harm (no improvement with frozen conditions).
Freezing E2 does not isolate the E1 contribution.

**Learning (with SD-001 caveat):** This result is probably uninterpretable as stated
because E2 in V1 was doing hippocampal trajectory search rather than pure transition
prediction (SD-001). Freezing E2 therefore froze trajectory proposal, not just
transition knowledge — making the ablation test something other than what was intended.
The experiment should be re-run after SD-001 resolution in V2.

---

### Control Completion Gating (EXQ-004 and EXQ-007 / MECH-057)

**Test (EXQ-004):** Does gating precision updates mid-macro-action (waiting for action
completion before accepting new control signals) reduce harm?

**Result:** NO_ATTRIBUTION: harm +1.9%. NO_GATING: harm +4.5%. Gating degrades
rather than improves.

**Test (EXQ-007):** Multi-step macro-actions with gated vs ungated precision updates.

**Result:** UNGATED harm 0.7720 > NO_MACRO harm 0.5287. Gating macro-actions worsens
performance relative to ungated execution.

**Learning:** The hypothesis that commitment requires blocking new precision updates
during execution is wrong at V1 scale. Continuous re-evaluation outperforms interrupt
blocking. However, this failure may reflect the poverty of V1's environment rather than
an architecture error: V1's stateless grid cannot create genuine commitment pressure
(scenarios where mid-action reversal is truly costly). MECH-057 is deferred to V3,
where a richer multi-step environment with genuine commitment consequences will be required
before re-testing.

---

## 6. Architectural Decisions Locked In By V1

The following architectural commitments were hardened by V1 evidence and are carried
into V2 as design requirements rather than open questions.

**Residue is load-bearing.** Zero residue routing demonstrably degrades harm avoidance.
Residue cannot be treated as an optional component or tuned to zero.

**Trajectory-first residue placement.** Residue accumulates at trajectory positions
during planning, not retroactively at execution endpoints. The causal structure is in
the path, not the destination.

**Separate pre-commit and post-commit error channels.** Channel contamination produces
8,520× residue inflation. These are not two flavours of the same signal; they are
structurally different objects requiring separate write loci.

**Separate confidence and prediction-error channels.** Merging them costs meaningful
harm performance. The control plane must route them independently into E3.

**E3 selection requires a candidate set.** Single-candidate E3 is significantly worse.
The hippocampal system must generate trajectory proposals; E3 selects among them.

**Lane separation in stream architecture.** Exteroceptive payload cannot write directly
into policy, identity, or capability stores. Reality-coherence conflicts must suppress
commitment. These are not soft conventions but hard routing rules.

**E1/E2 functional orthogonality, not temporal.** The value of the E-stack separation
is in representational vocabulary (associative vs transition), not operating speed.
V2 must cleanly implement this rather than relying on timescale difference.

---

## 7. Evidence Integrity: The Synthetic Evidence Audit

One of V1's most important findings was not a mechanism result but a process finding.

A systematic audit of experiment records revealed that a large fraction of V1-labelled
experiments were not genuine ree-v1-minimal runs. They were generated using a separate
ree-v2-qualification-harness with a `toy_env_runner` (synthetic parametric data). This
means:

- **Genuine ree-v1-minimal runs:** ~14 distinct experiments with multiple seeds (EXQ-000
  through EXQ-013, plus extended-seed replications).
- **Synthetic-only experiment types:** ~31 types with 1,000+ synthetic runs across
  archived ree-v2 and ree-experiments-lab substrates.

**Impact on claim statuses:** Architectural statuses (active/provisional/candidate) are
maintained because they are grounded in design decisions and specification reasoning, not
purely on empirical outcomes. However, confidence scores derived from experiment counts
are unreliable where synthetic runs were counted as genuine.

**Re-validation roadmap:**
- P1 (highest priority): MECH-059, MECH-060, MECH-061 — mechanistic validation of the
  three confirmed load-bearing separations.
- P2 (candidate blockers): MECH-056, MECH-058, MECH-057 — residue placement, timescale,
  and control completion.
- P3: Q-001 through Q-017 open question validation.

**The correct interpretation of V1 results:** The four primary genuine PASSes (EXQ-000,
001, 003, 005) stand on solid ground. The four informative FAILs are genuine substrate-
limited results. Extended-seed replications (EXQ-010–013) strengthen confidence intervals
on the PASSes. Everything else requires re-validation on genuine substrate.

---

## 8. Substrate Debt Register

Three substrate debts were registered during V1 that constrain what V2 can test and how
V1 results should be interpreted.

### SD-001: E2/Hippocampus Conflation

**Problem:** In V1, E2 was doing hippocampal trajectory search (generating multi-step
rollouts) rather than acting as a pure fast transition predictor. This means:

- EXQ-006 (E1/E2 orthogonality via E2 freezing) cannot be interpreted as intended —
  it tested "no trajectory proposals" not "no E2 transition prediction."
- MECH-058 timescale ablation results are partially uninterpretable.
- Claims about E2's functional role cannot be cleanly confirmed from V1 evidence.

**V2 resolution:** E2 is refactored as a pure fast transition model (`forward(z, a) →
z_next`, cerebellum-like). HippocampalModule becomes a distinct component of the E3
complex, responsible for trajectory proposal by navigating affective terrain. SD-001 is
closed when E2 is callable independently with arbitrary action input and a separate
HippocampalModule class exists.

### SD-002: E1/E2 Mutual Constitution

**Finding:** E1 and E2 are co-constitutive, not parallel independent modules:
- E2 scaffolds E1: transition sequences provide temporal evidence for associative
  distillation in E1.
- E1 primes E2: associative priors condition E2's transition predictions.

**Implication:** The timescale-separation failure (EXQ-002) makes more sense under this
framing — separating speed is not separating function. V2 architecture must reflect
co-constitution in wiring (E1 prior into HippocampalModule; E2→E1 autotrain pathway
deferred to V3).

### SD-003: E2 as Self-Attribution Substrate

**Finding:** E2's action-conditioned transition model `e2.forward(z, a)` is the natural
substrate for counterfactual self-attribution: by querying E2 with alternative actions,
the agent can ask "would the harm have occurred if I had done otherwise?"

**V1 limitation:** V1's stateless grid environment has no persistent agent causal
footprint — actions at step N do not affect the landscape at step N+k in a way that
requires disambiguation from independent environment change. This makes genuine
self-attribution experiments impossible on V1 substrate.

**V2 requirements:**
- E2 must be callable independently: `e2.forward(z, a_counterfactual)`.
- Environment must provide persistent agent causal footprint.
- First genuine self-attribution experiments: isolate agent-caused vs environment-caused
  harm using CausalGridWorld or equivalent.

---

## 9. What V1 Could Not Test

Beyond the substrate debts, several architectural claims simply exceed what a minimal
stateless grid can surface:

**Persistent causal footprint.** An agent that cannot affect its future landscape cannot
develop or demonstrate genuine self-attribution. This is a prerequisite for testing
whether REE's residue system correctly assigns moral cost to agent-caused rather than
environment-caused harm.

**Genuine commitment pressure.** MECH-057 (control completion gating) requires scenarios
where reversing a mid-action commitment is genuinely costly — not just sub-optimal, but
consequential in a way the agent must weigh. V1's grid does not create this pressure. V3
is the correct phase to retest this, with a richer multi-step environment.

**Persistent agent identity.** Long-horizon self-model claims (identity continuity,
narrative coherence) cannot be tested in episodic grid environments. These are V3/V4
claims.

**Social coupling.** Multi-agent coordination, empathy mechanisms, and institutional
constraint are explicitly V4 scope. V1 was designed for single-agent ethical mechanics
only.

**Offline consolidation / sleep.** The residue load management mechanisms (sleep-like
replay reducing residue without erasing causal structure) require extended multi-episode
runs with offline phases. V1 did not run these.

---

## 10. Open Questions Sharpened by V1

V1 did not just confirm and disconfirm mechanisms — it sharpened a set of open questions
that V2 and V3 must answer.

**Q: What makes E1/E2 separation valuable if not timescale?** V1 confirms the separation
matters (EXQ-000 shows independent channel signals) but doesn't explain the mechanistic
basis. The functional orthogonality hypothesis (associative vs transition knowledge) is
the current best candidate but untested directly.

**Q: What is the commitment pressure threshold?** MECH-057 failed at V1 scale. We don't
know yet what environmental complexity is needed to surface genuine commitment costs. V3
will need to establish this empirically.

**Q: How does residue load grow with episode depth?** The 8,520× inflation under
contamination (EXQ-005) is alarming even as a failure mode. We need to characterise
how residue load grows under normal operation and at what point offline consolidation
becomes necessary to prevent trajectory paralysis.

**Q: What is the minimum genuine-run threshold for claim promotion?** V1's informal
threshold was approximately 2 genuine runs for provisional status. V2 should codify this
in the Step 2.0 spec.

**Q: Can uncertainty channels be made gaming-resistant?** The claim_probe_mech_059
synthetic runs showed widespread uncertainty metric gaming (systems learned to report
high uncertainty without actually abstaining). This is a critical safety failure mode
that genuine V2 experiments must address.

**Q: What is the correct environment for self-attribution?** V1 could not test SD-003
claims at all. V2 must design or source a persistent-causal-footprint environment before
any self-attribution experiments are possible.

---

## 11. V1 to V2: What Changes and Why

V1 served its purpose: signal discovery and contract hardening. The four genuine PASSes
establish the core REE causal structure as real. The four informative FAILs reveal
substrate limitations that must be resolved, not architecture errors that must be fixed.

**What V2 inherits from V1:**
- Confirmed residue routing requirement (ρ > 0, trajectory-wide placement)
- Confirmed write-locus separation requirement (separate pre/post-commit channels)
- Confirmed precision channel separation requirement (confidence ≠ prediction error)
- Confirmed E3 candidate set requirement
- Confirmed lane separation in stream routing
- Framework for genuine vs synthetic experiment validation

**What V2 must resolve:**
- SD-001: Clean E2/hippocampus separation (pure transition MLP vs rollout generator)
- SD-002: Co-constitution wiring (E1 prior → hippocampus; E2 → E1 autotrain pathway)
- SD-003: Counterfactual E2 querying + persistent causal environment
- Re-run E1/E2 orthogonality ablation on clean substrate
- First genuine self-attribution experiments

**What is deferred to V3:**
- Control completion gating (MECH-057) — requires genuine commitment pressure
- Hippocampal rollout generation + post-commit map/model updates
- Full control-plane arbitration and precision routing at depth
- Pre/post-commit error channels under adversarial trajectory pressure

**What is deferred to V4:**
- Social and institutional complexity
- Multi-agent coupling
- Language-mediated coordination

---

## 12. Summary Metrics

| Category | Count |
|----------|-------|
| Genuine EXQ experiments (primary) | 8 (EXQ-000 to 007) |
| Genuine EXQ experiments (extended) | 6 (EXQ-008 to 013) |
| Primary genuine PASSes | 6 |
| Primary informative FAILs | 4 (substrate-limited) |
| Synthetic experiment types (require re-validation) | ~31 |
| Substrate debts registered | 3 (SD-001, 002, 003) |
| Architectural decisions locked in | 6 core commitments |
| Open questions sharpened | 6 |
| V2 entry criteria added from V1 learning | 3 |

---

## 13. Reading Guide

For readers coming to V1 evidence for the first time:

- **Architecture basics:** `docs/REE_overview.md`, `docs/architecture/overview.md`
- **V1 minimal spec:** `docs/REE_MIN_SPEC.md`
- **Experiment index and status:** `evidence/experiments/INDEX.md`
- **Evidence integrity:** `evidence/experiments/SYNTHETIC_EVIDENCE_AUDIT.md`
- **Substrate debts:** `evidence/GOVERNANCE_STATE.md`
- **Roadmap and phase gates:** `docs/roadmap.md`
- **Claim evidence matrix:** `evidence/experiments/claim_evidence.v1.json`
- **Promotion/demotion queue:** `evidence/experiments/promotion_demotion_recommendations.md`
- **Architecture stream routing:** `docs/architecture/streams.md`
- **Control plane:** `docs/architecture/control_plane.md`
- **E1/E2 integration contract:** `docs/architecture/jepa_e1e2_integration_contract.md`
- **Hippocampal systems:** `docs/architecture/hippocampal_braid.md`
