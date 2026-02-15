Status: processed

Processed in:
- `docs/architecture/e3.md` (MECH-061, MECH-062 implementation-gap contract)
- `docs/architecture/control_plane.md` (MECH-063 diagnostic regime clarification)
- `docs/architecture/agency_responsibility_flow.md` (MECH-060/061/062 responsibility-routing context already canonical)

---

## Thought intake draft for `REE_assembly`: **Commit gating, pre/post-commit error separation, and control-plane axes (anchored by missed-dose phenomenology)**

### 0) Anchor phenomenology (user-observed pattern)

* **Carry-over / lull after missed lisdexamfetamine**

  > "attention stays good but I am tired the next day and it takes a while for the bounce to come back but attention only wanes when bounce comes back."
* **Initiation / commitment friction**

  > "It’s difficult to initiate or commit to movements. A bit"
* **Reward substitution without mood collapse**

  > "Appetite might be more cravy rather than reduced. Like boredom eating"

**Interpretive hook for REE:** dissociation between (a) *cognitive monitoring / attention* and (b) *commitment-to-act*, plus a shift toward *low-effort reward selection* under reduced "precision/vigor" tone.

---

### 1) Architectural claim: basal ganglia as commitment gates (threshold arbiters)

* **Basal ganglia implement commitment gating** (not "world simulation"): release/disinhibit a selected cortical proposal via threshold crossing.
* **Key split:** *"thinking clearly but can’t start"* -> commitment threshold rises while representational quality remains acceptable.

**REE mapping:** commit gate is a **selector** operating over proposals produced upstream; intelligence lives upstream.

---

### 2) Critical boundary concept: **Commit Boundary** separates error classes

**Problem statement (user):**

> "if hippocampal path traces are held by frontal systems and if basal ganglia handle the actual commit then where separates the pre and past commit error signals"

**Proposed synthesis for REE:**

* **Pre-commit errors = evaluative / counterfactual** (simulation critique)

  * plausibility / coherence mismatch
  * conflict / effort cost
  * anticipated value deviation
* **Commit event = discrete boundary token**

  * converts "hypothetical" into "causal intervention"
* **Post-commit errors = attributable / responsibility-bearing**

  * reafference mismatch (predicted vs observed consequences of *my* output)
  * outcome value error (temporal difference-style)
  * credit assignment across modules/time

**Key REE claim:** the **commit token** is the minimal mechanism that reclassifies error signals into responsibility-relevant feedback.

---

### 3) E3 decomposition update (user decision)

> "we have split original E3 into hippocampal function, three basal ganglia functions and prefrontal cortex function"

**REE decomposition (roles):**

* **Hippocampal analogue:** trajectory/path generation (prospective rollouts, replay)
* **Prefrontal analogue:** working-set maintenance + constraints + goal holding
* **Basal ganglia family (3 gates):**

  1. motor gate
  2. cognitive-set update gate
  3. motivational/salience gate
* **(Implicit) credit engine:** post-commit causal attribution + learning distribution

**Why this matters:** avoids monolithic E3 doing "simulate + evaluate + gate + learn"; preserves biological-style specialization and keeps commitment gating computationally simple.

---

### 4) Multi-loop basal ganglia principle

* **Same gating algorithm, different streams/manifolds.**
  Motor / associative-cognitive / limbic-motivational loops apply similar thresholding over different proposal spaces.
* **Design implication:** avoid a single global gate that pathologically couples "movement suppressed" with "thought suppressed" or "motivation collapse halts rule updates."

---

### 5) Signal-routing emphasis: "what is gating vs what requires real inference"

**User question:**

> "So what signal streams are being listened to and fed where and what would need actual AI processing rather than mere gating."

**Useful REE distinction:**

* **AI-required:** state inference/uncertainty, generative rollouts, counterfactual evaluation, causal attribution, long-horizon credit assignment
* **Mostly gating/routing:** thresholding, winner-take-most arbitration, gain modulation knobs

(Your later "signal routing table" spec fragment can be referenced/embedded as-is in repo; this thought just needs to point to it as the interface map.)

---

### 6) Control-plane expansion beyond dopamine/serotonin

**User baseline:**

> "We know we have precision signals (dopamine like) and tolerance for delay commitment (serotonin like) but we also have other control plane signals"

**Control-plane axes to include (compact set):**

1. **Precision / vigor** (dopamine-like): confidence-on-policy, commit threshold lowering, learning-rate modulation for value
2. **Delay tolerance / commitment persistence** (serotonin-like): plan stickiness, patience, reduced switching
3. **Arousal / interrupt priority** (noradrenaline (norepinephrine)-like): surprise-driven preemption, rapid replan, ready-vigilance
4. **Sustained threat mode** (stress-axis-like): conservative thresholds, safety bias, strong memory tagging
5. **Social openness / trust** (oxytocin-like): other-model weighting, prosocial priors
6. **Boundary defense / coalition vigilance** (vasopressin-like): distrust priors, social threat interpretation
7. **Curiosity / information gain drive** (acetylcholine-like): exploration-for-learning, representation growth
8. **Energy budget / fatigue** (metabolic/adenosine-like): throttle action rate, raise thresholds, force rest/consolidation

**Implementation note:** each knob has **tonic + phasic** components; modules read weighted mixtures to avoid collapse while permitting coupling.

---

### 7) Phenomenology-to-architecture bridge (why the missed-dose pattern matters)

Use the user-observed sequence as a **diagnostic probe** for REE control-plane and gating separation:

* **Day-after missed dose:**

  * down global precision/vigor -> **motor gate threshold up** (initiation hard)
  * motivational system defaults to **low-effort reward** (boredom eating)
  * cognitive monitoring can remain relatively intact briefly
* **Delayed bounce:**

  * precision/vigor returns -> initiation easier
  * but arousal may overshoot -> attention fragments when "bounce" returns

**REE takeaway:** you can get "focused-but-stuck" if **representation is stable** while **commit thresholds are high** and **energy budget is low**; this is a desirable capability for a biologically-inspired agent (it prevents spurious action under low precision).

---

### 8) Gaps to explicitly mark (placeholders for you to fill, not invented)

* **[GAP]** What exactly is the *commit token* format in REE (data structure, scope, broadcast rules, TTL)?
* **[GAP]** How do the three gates coordinate when proposals conflict across manifolds (motor vs cognitive vs motivational)?
* **[GAP]** What is the minimal credit-assignment interface required post-commit (mask types, causal graph assumptions, timescales)?
* **[GAP]** Where do you want "responsibility" to live formally: as an attribution ledger, a training signal router, or a stable self-model constraint?

---

## Abstracted layer (compressed)

* OBS: miss(stimulant) -> lull(attn_ok and drive_low) -> rebound(drive_high and attn_frag)
* ARCH: H(traj_gen) + PFC(hold/constraint) + BG_m/BG_c/BG_v(gate_m/gate_c/gate_v)
* BOUNDARY: commit_token => reclassify(err_pre:counterfactual -> err_post:attributable)
* CTRL: knobs = {pi(vigor/precision), sigma(delay_tolerance), nu(interrupt/arousal), tau(threat_sustain), omega(trust), upsilon(boundary_defense), kappa(curiosity), epsilon(energy_budget)} with tonic + phasic

---

### Footnotes

1. I’ve treated the quoted user lines as the *anchor data* and everything else as *architectural extraction*. None of the assistant’s earlier mechanistic claims are included here unless they directly served your REE-level decomposition request.
2. Basal ganglia is expanded here as **basal ganglia** (no abbreviation used); prefrontal cortex is expanded as **prefrontal cortex**; noradrenaline is expanded as **noradrenaline (norepinephrine)** on first use.
3. If you want this as an actual repo-ready file, the above can be pasted as `thoughts/commit_boundary_control_plane.md` with a short header/frontmatter.

**Training Data Confidence:** High (this is mostly structural extraction, not contested facts)
**Epistemic Confidence:** High (that the extracted points match the provided text and your stated REE moves)

Possible affected components:
- E3
- commitment boundary / token spec
- basal ganglia loop separation
- control plane axes
- docs/architecture/e3.md
- docs/architecture/control_plane.md
- docs/architecture/agency_responsibility_flow.md
