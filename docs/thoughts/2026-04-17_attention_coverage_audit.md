# Attention Coverage Audit

Date: 2026-04-17
Status: scratch / exploratory — not a claim
Author: session dialogue with Daniel

Purpose: enumerate what the canonical functional-attention literature treats
as distinct mechanisms, and check each against existing REE claims/docs, to
find holes worth promoting to new claims or SDs.

---

## Current REE attention story (what is already claimed)

| ID | Title | Status | Scope |
|----|-------|--------|-------|
| INV-009 | Attention is precision modulation, not symbolic control | active | Foundational — attention is a control surface, not a content selector |
| MECH-007 | Attention must be fragmented across control axes | provisional | Precision / commitment / exclusivity are orthogonal; no unitary "attention" |
| MECH-004 | (subject: attention.mechanism) | active | Precision routing; paired with INV-009 |
| MECH-081 | NA as attentional snap and E1/E2 sampling ratio modulator | — | Exogenous bottom-up orientation via noradrenaline |
| MECH-089 | Theta-gamma nesting packages E1 updates for E3 | candidate | Temporal packaging; E3 never sees raw E1 |
| MECH-090 | Beta gates E3 -> action_selection propagation | candidate | Output gating; distinct from update gating |
| MECH-093 | z_beta modulates E3 heartbeat frequency | candidate | Rate control on the control plane |
| MECH-094 | Hypothesis tag as categorical phi(z) write gate | candidate | Source gating for writes; pre/post-commit separation |
| ARC-044 (+ INV discussing lapses) | Attentional lapses serve information-gathering | — | Exploration/exploitation allocation |
| ContextMemory (e3.md, vmPFC.md) | Q/K/V soft attention for associative retrieval | — | Memory retrieval, not online selection |

Summary of what REE already handles well:
- Attention as **control**, not content (INV-009) — strong.
- **Fragmentation across control axes** (MECH-007) — strong; distinguishes learning, action, belief.
- **Temporal scoping** (tau) and **representational scoping** (rho) — explicit in MECH-007 section 5/6.
- **Exogenous salience / bottom-up snap** — MECH-081 via NA.
- **Write gating** — MECH-094 (tag), plus beta-gated output (MECH-090).
- **Update packaging** — MECH-089 theta-gamma nesting.

---

## Canonical functional-attention checklist

Drawing from Posner/Petersen, Corbetta-Shulman, feature-integration theory,
global workspace theory, and predictive-processing/active-inference attention:

1. **Alerting / tonic readiness** — sustained arousal that modulates overall gain.
2. **Orienting / exogenous attention** — bottom-up, stimulus-driven capture.
3. **Orienting / endogenous attention** — top-down, goal-driven biasing.
4. **Executive / conflict resolution** — selection among competing representations under conflict.
5. **Feature integration / binding** — which features are bound into one object this cycle.
6. **Selection for access / broadcast** — what enters the "workspace" for report, planning, and memory encoding.
7. **Selection for action** — what is linked to motor planning (premotor biasing).
8. **Capacity / bottleneck** — limits on simultaneous deep processing.
9. **Attentional template / search set** — stored specification of what to look for.
10. **Attentional sampling rhythms** — quasi-rhythmic sampling of attended items (4–8 Hz theta).
11. **Predictive-processing precision weighting on prediction errors** — whose PE gets amplified.
12. **Attention-for-learning vs attention-for-action separation** — different gain on different registers.

---

## Claim-by-claim coverage

| # | Functional role | REE coverage | Gap? |
|---|-----------------|--------------|------|
| 1 | Alerting / tonic arousal | Implicit in NA (MECH-081) and serotonin (MECH-006); no named alerting claim | MILD — not a named mechanism; absorbed into neuromodulators |
| 2 | Exogenous orienting | MECH-081 (NA snap) | COVERED |
| 3 | Endogenous orienting | Not explicitly named; residue-geometry biasing (valenced_hippocampal_map.md) and SD-016 (frontal cue integration) gesture at it | **HOLE** — no claim specifies E3/vmPFC -> E1 attentional *template* propagation |
| 4 | Executive conflict resolution | MECH-007 exclusivity axis (serotonin-like) addresses the *belief* side; action-side conflict handled by beta gate (MECH-090) | PARTIAL — no claim on representational-conflict resolution *within a heartbeat cycle* (dACC-style) |
| 5 | Feature integration / binding | entities_and_binding.md, hippocampal_relational_binding thought doc | COVERED conceptually; no mechanism claim on attentional control *of* binding |
| 6 | Selection for access / broadcast | MECH-089 theta-gamma packaging is the closest; no global-workspace-style claim | **HOLE** — no claim names an access gate, i.e. what enters the content that E3 deliberates over |
| 7 | Selection for action | MECH-090 beta gate (E3 -> action) | COVERED |
| 8 | Capacity / bottleneck | Implicit in fragmentation (MECH-007) — no explicit capacity mechanism | PARTIAL — bottleneck is asserted by distributed design; never instantiated as a constraint |
| 9 | Attentional template / search set | Not named; loosely carried by z_goal (INV-034/037/038) and residue geometry | **HOLE** — goal-maintenance claims exist, but the *biasing operation on E1 sampling* is not a claim |
| 10 | Attentional sampling rhythms | MECH-089 (theta packaging), MECH-093 (beta -> heartbeat rate), control_plane_heartbeat.md | COVERED |
| 11 | PE precision weighting | INV-008/009, MECH-004, precision_scoping.md, precision_control.md | COVERED — this is the backbone of the story |
| 12 | Attention-for-learning vs attention-for-action | MECH-007 section 4.1 — dopamine (learning), NA (action), 5-HT (belief) | COVERED |

---

## The three substantive holes

### H1. Endogenous top-down attentional biasing from E3 / vmPFC back to E1 sampling

**What's missing:** Frontoparietal-style goal-driven templates that bias *perceptual sampling* before stimuli arrive. REE has:
- MECH-081 for *exogenous* snap (NA, bottom-up).
- Residue geometry and z_goal for *what matters* (goal content).
- SD-016 for frontal cue *integration* (how external cues get into planning).

But there is no claim for the operation "E3/vmPFC writes a precision template into E1 so that E1 pre-amplifies goal-relevant features." This is the standard Corbetta-Shulman dorsal-attention story and also the active-inference
"expected precision" story.

**Why it matters:** without this, goal-directed perception is entirely downstream of what E1 happens to sample. REE currently leans on E1's own residue-influenced priors to do this work, but the control pathway is not named — so it is also not experimentally targeted.

**Possible claim shape:**
- ARC: "E3 writes an expected-precision prior to E1 such that goal-relevant features receive amplified PE weighting before they arrive."
- MECH: the specific channel (likely via vmPFC -> hippocampal map -> E1 prior), possibly coupled to MECH-089 packaging.

### H2. Selection for access / workspace broadcast

**What's missing:** a named mechanism for "which of the many E1/E2 active contents reach E3 for deliberation *this cycle*."

MECH-089 specifies that E3 gets theta-cycle-averaged summaries of E1. That's *packaging*, not *selection*. It does not answer: among many currently-active latents, which ones are summarised, and which are discarded?

REE's distributed design *assumes* this happens via precision-weighted competition, but that is a derivation, not a claim. The literature treats this as a distinct capacity-limited access gate (global workspace, ignition, frontal access).

**Why it matters:**
- Capacity limits are real and important for alignment arguments (you cannot attend to everything, so the *selection rule* matters).
- Hallucination, rumination, and inattentional blindness are different failure modes of *this gate*, not of precision weighting per se.
- REE already gestures at "micro-DMN" (MECH-092) — which only makes sense against the backdrop of an access gate that is sometimes quiescent.

**Possible claim shape:**
- MECH or ARC: "A capacity-limited access gate selects a small number of E1/E2 summaries for E3 consumption per heartbeat cycle; selection weights are the precision vector modulated by z_goal and NA."

### H3. Attentional template as a first-class object

Related to H1, but distinct: the *template itself* — the stored specification of what to look for — is not a named entity in REE. Goal-maintenance claims (INV-034, INV-037/038) give us "there is a stored goal representation," but an attentional template is more specific: it is a *precision pre-specification on feature channels*, not a goal content.

**Why distinct from H1:** H1 is the channel; H3 is the data structure. You can have the channel (E3 -> E1 prior) without committing to what format the template takes, or vice versa.

**Possible claim shape:**
- A definitional claim that an attentional template is a vector in the precision space (not in the content space), stored in vmPFC-like circuits and written into E1 via the H1 channel.

---

## Two smaller gaps worth noting

- **Conflict resolution within a heartbeat** (item 4 of the checklist). MECH-007 covers the *axes* but not the within-cycle representational competition (dACC-style). Possibly subsumed by E3 selection mechanisms already, but not audited.
- **Capacity limit as a named design constraint** (item 8). If the access gate is added (H2), capacity falls out naturally. If not, it needs its own claim.

---

## Recommendation

The cleanest next step is H2 (access gate), because:
- It is the most structurally missing and it naturally constrains H1 and H3.
- It couples to existing heartbeat machinery (MECH-089/090/091/092) without requiring new substrate.
- It gives a sharp experimental target: measure whether E3 actually receives content selected under a capacity limit, and whether selection weights follow the predicted mixture of precision + z_goal + NA.

H1 and H3 should probably be designed together as a paired ARC/MECH because the channel and the data structure co-constrain each other.

If we decide to proceed: register as new candidate claims under a shared `attention.access_and_template` subject family, and flag a corresponding SD for the substrate work (likely V4-scoped, since current V3 substrate lacks the needed wiring).

---

## What this audit deliberately does NOT recommend

- Adding a unitary "attention module." MECH-007 rules this out normatively.
- Treating transformer Q/K/V as the canonical form. ContextMemory already uses it for retrieval; generalising it to online selection would collapse fragmentation.
- Promoting any of the above to active before substrate-level evidence. H1/H2/H3 are candidate-level at most.

---

## Open questions to resolve before writing claims

1. Does the H2 access gate live inside E3 or at the E1/E2 -> E3 boundary? (Probably the boundary, per MECH-089's packaging framing.)
2. Is the H1 channel a separate signal from residue geometry, or is residue geometry the *output* of an H1-style template? (If the latter, H1 is already implicit and needs only a claim to name it.)
3. Does the existing INV-037/038 "stored vs active" distinction already carry the H3 data-structure role, or is "stored goal" different from "attentional template"?

---

## Resolutions (2026-04-17 session)

**Q1.** Boundary, not inside E3. Anatomical name: **pulvinar-TRN access gate**. TRN provides capacity-limited gating via inhibitory shell; pulvinar mediates higher-order cortical-cortical relay. Together they are the biological referent for H2.

**Q2.** H1 distinct from residue. Anatomical name: **dorsal attention network (DAN)** -- FEF + IPS writing feedback to V1/V4. Anatomically separates from H3 (vmPFC-dlPFC template compiler).

**Q2 pressure-test.** H1 survives. Five reasons distinctness holds:
1. Direction of causality: residue is retrospective (outcomes), H1 is prospective (intent).
2. Biological substrates and neuromodulation differ: hippocampal-cortical/DA vs DAN/ACh+NA.
3. Double dissociation: amnestics form templates; frontal patients lose template deployment with intact residue.
4. Representational format: episodic specificity vs cross-situational feature generality.
5. Ethical-commitment (REE-specific, strongest): INV-012 requires deliberate attention to be distinguishable from reflexive residue-driven attention, else no mechanism for willed perception.

Concession: both channels probably write the same downstream register (E1 prior) via additive combination. Same register, distinct sources and dynamics.

**Q3.** Sleep differentiation is real and strengthens the cluster. SWS consolidates goal-value error to stored goals; REM with varied associative replay consolidates template-performance error to template compilation. Phase separation is what *creates and maintains* the stored/template distinction over time. Stronger form of INV-010 and a natural extension of INV-049.

**V3/V4 scoping:**
- H1 (DAN write channel): **V3** -- part of completing SD-012. Without it, z_goal is behaviorally inert even when it seeds (as EXQ-085h-l demonstrated).
- H2 (pulvinar-TRN gate): **V3/V4 boundary** -- simple fixed-capacity selector retrofittable to V3, full dynamic version is V4.
- H3 (template as first-class object): **V4** -- requires vmPFC-dlPFC decomposition V3 lacks.
- Sleep differentiation (MECH-252): **V4** implementation, can be drafted now.

---

## Draft claim entries (for review before commit to claims.yaml)

Next IDs: SD-026, MECH-251, MECH-252. Max checked 2026-04-17T17:39Z: SD-025, MECH-250, ARC-057, INV-072.

### SD-026 (draft v2) -- H1 write channel

```yaml
- id: SD-026
  title: "Goal-directed perception requires a prospective precision-template write channel from z_goal to the E1 prior, anatomically analogous to the dorsal attention network (FEF/IPS -> V1) feedback, distinct from residue-geometry (history-driven) sampling bias."
  claim_type: design_decision
  subject: attention.prospective_precision_write_channel
  polarity: asserts
  status: candidate
  implementation_phase: v3
  claim_level: architectural
  registered_utc: 2026-04-17
  depends_on:
    - SD-012           # z_goal seeding prerequisite
    - SD-014           # z_resource separation -- without crisp resource representation, template has nothing to amplify
    - INV-034          # goal maintenance necessary for ethical agency
    - INV-037          # stored vs active distinction
    - INV-038          # EVR pattern
    - INV-009          # attention is precision modulation
    - MECH-007         # attention fragmentation
  functional_restatement: >
    SD-012 establishes that drive-scaled benefit can seed z_goal. EXQ-085f/g
    confirmed z_goal_norm > 0.1 is achievable. EXQ-085h through 085l then
    failed navigation (benefit_ratio) consistently: seeding works, but
    z_goal is behaviorally inert because no channel exists by which it
    biases E1 sampling toward goal-relevant features. Residue geometry
    (ARC-007) biases sampling toward previously-mattering locations
    (history-driven) but cannot bias toward prospective template features
    (goal-driven). Without a prospective write channel, z_goal can only
    affect behavior via E3 trajectory re-ranking after the fact; perception
    itself remains goal-agnostic.

    Proposed mechanism (V3 minimum): z_goal is projected through a
    template projection into a precision-space vector, written additively
    to the E1 prior via a dedicated dan_feedback channel with fast decay
    (tau ~ seconds). Residue geometry retains its slow decay. Both channels
    write to the same E1-prior register via additive combination; sources
    and dynamics are distinct.

    SEPARABLE-FROM (not a dependency, a boundary): ARC-007 (residue
    geometry). ARC-007 and SD-026 share the E1-prior register but are
    distinct sources with distinct dynamics -- ARC-007 writes from
    retrospective outcomes with slow decay; SD-026 writes from prospective
    intent with fast decay.

    STRUCTURAL LOAD-BEARING FOR: INV-012 (responsibility through
    commitment). Without a prospective channel, REE has no mechanism
    for *willed* perception -- only reflexive residue-driven attention.
    INV-012's coherence requires deliberate vs reflexive attention to be
    mechanistically distinguishable; SD-026 is the mechanism that makes
    that distinction possible. See INV-012 depends_on update.
  notes: >
    Anatomical grounding: Corbetta & Shulman (2002) dorsal attention
    network (FEF + IPS) writes feedback to V1/V4 producing prospective
    gain modulation before stimuli arrive. Moore & Armstrong (2003): FEF
    stimulation produces V4 selectivity shifts for attended features.
    Summerfield et al. (2006): prospective template distinct from
    reactive adjustment. In predictive-processing terms, DAN writes
    "expected precision" on specified feature channels.

    Decomposition (see docs/thoughts/2026-04-17_attention_coverage_audit.md):
    H3 (template as first-class precision-space object, compiled from
    stored goal by vmPFC-dlPFC) is deferred to V4. SD-026 is the V3
    minimum: a differentiable projection z_goal -> template_vec ->
    additive prior bias is sufficient to validate the channel exists
    and is separable from residue.

    Boundary vs neighboring claims:
    - MECH-081 (NA as attentional snap): MECH-081 is EXOGENOUS / bottom-up
      stimulus-driven salience. SD-026 is ENDOGENOUS / top-down goal-driven
      template. Both may write gain to E1 but sources are orthogonal;
      they are complementary, not redundant. Full attention system = NA
      snap (MECH-081) + DAN template (SD-026) + fragmentation across
      control axes (MECH-007).
    - ARC-044 (attentional lapses for exploration): ARC-044 governs the
      TEMPORAL gating of attention engagement (when to release into
      exploration). SD-026 governs the CONTENT of attention when
      engaged (what to amplify). Orthogonal axes -- ARC-044 can release
      a SD-026 template, and SD-026 templates can be re-engaged after
      ARC-044 lapses. Neither subsumes the other.
    - ARC-007 (residue geometry): see SEPARABLE-FROM above.

    Pressure-tested against residue-redundancy hypothesis: distinct on
    direction of causality (retrospective vs prospective), neuromodulation
    (DA-gated vs ACh/NA-gated), clinical dissociation (amnestic vs frontal
    syndromes), representational format (episodic specificity vs
    cross-situational feature generality), and REE-specific ethical
    commitment argument (INV-012 requires deliberate vs reflexive
    attention to be distinguishable).
  evidence_quality_note: |
    No direct experiments yet. Testing is gated on SD-014 (z_resource
    separation): without a crisp resource representation, a DAN template
    ablation is confounded -- template quality and target quality cannot
    be disentangled. Do not queue SD-026 validation EXQ until SD-014 is
    at least provisional.

    Predicted failure mode in EXQ-085h-l navigation (z_goal seeds but
    does not bias sampling) is consistent with SD-026 being the missing
    piece. First validation experiment (queued post-SD-014) should:
    (a) verify z_goal seeds (SD-012), (b) verify z_resource separates
    (SD-014), (c) enable/disable dan_feedback channel as ablation,
    (d) measure benefit_ratio against random baseline, (e) measure
    feature-channel precision on goal-relevant vs irrelevant dimensions.
    Prediction: dan_feedback=on lifts benefit_ratio substantially;
    dan_feedback=off replicates EXQ-085h-l behavior (seed-but-inert).
```

### INV-012 edit (proposed) -- add SD-026 as load-bearing dependency

INV-012 currently has `depends_on: []`. Add SD-026 with an explanatory note:

```yaml
- id: INV-012
  title: "Responsibility arises through commitment, not prediction alone."
  claim_type: invariant
  subject: commitment.epistemology
  polarity: asserts
  status: active
  depends_on:
    - SD-026           # willed vs reflexive attention must be mechanistically distinguishable; SD-026 is that mechanism
  location: docs/invariants.md#inv-012
  source:
    - docs/processed/legacy_tree/docs/invariants.md
  notes: >
    Added depends_on SD-026 (2026-04-17): INV-012's coherence requires
    a mechanism by which deliberate/willed attention can be distinguished
    from reflexive/residue-driven attention. Without such a mechanism,
    "commitment" reduces to "whatever was already conditioned," and the
    invariant loses its ethical content. SD-026 (prospective precision
    template write channel, DAN analogue) is that mechanism.
```


### MECH-251 (draft) -- write mechanism

```yaml
- id: MECH-251
  title: "z_goal projects to a precision template vector that is additively written to the E1 prior via the dan_feedback channel with fast exponential decay, separable in dynamics and source from residue-geometry bias."
  claim_type: mechanism_hypothesis
  subject: attention.dan_feedback_precision_write
  polarity: asserts
  status: candidate
  implementation_phase: v3
  claim_level: mechanistic
  registered_utc: 2026-04-17
  depends_on:
    - SD-026
    - ARC-007
    - INV-009
  functional_restatement: >
    Implementation for SD-026. template_vec = template_proj(z_goal) where
    template_proj is Linear(goal_dim, prior_dim). effective_prior =
    alpha_residue * residue_bias + alpha_dan * template_vec, with
    alpha_dan decaying exponentially from the last z_goal update (tau on
    the order of seconds in env-steps). Residue bias retains its slow
    timescale (episodes). Both contribute additively to precision weights
    in the E1 encoder. Ablation toggle: sd026_enabled (default off during
    initial validation).
  notes: >
    Deliberately minimal for V3. Does not commit to vmPFC-dlPFC template
    compilation (H3, deferred to V4). Does not commit to capacity-limited
    selection (H2, V3/V4 boundary, pulvinar-TRN gate). Tests only whether
    a separable prospective channel is necessary for z_goal to produce
    behavioral lift. Falsifiable: if dan_feedback=off still produces
    benefit_ratio lift once z_goal seeds, SD-026 is wrong and residue
    alone suffices.
```

### MECH-252 (draft) -- SWS consolidates stored-goal content

```yaml
- id: MECH-252
  title: "SWS hippocampal-neocortical replay consolidates goal-value prediction error into updates of stored goal representations (content update), not into attentional-template parameters."
  claim_type: mechanism_hypothesis
  subject: sleep.sws_stored_goal_consolidation
  polarity: asserts
  status: candidate
  implementation_phase: v4
  claim_level: mechanistic
  registered_utc: 2026-04-17
  depends_on:
    - SD-017           # sleep phase architecture
    - INV-010          # offline integration required
    - INV-049          # sleep mathematically necessary for model-building
    - INV-037          # stored vs active
    - INV-038          # EVR pattern
  functional_restatement: >
    During daytime operation, goal-value prediction error is accumulated:
    did pursuing goal G actually satisfy homeostatic drive / produce
    predicted benefit? This error is long-horizon, episodic, sparse.
    Its legitimate update target is the *stored goal representation*
    (what the agent wants), not the attentional template (how the agent
    finds it).

    Proposed mechanism: SWS hippocampal-neocortical replay selectively
    routes goal-value error to stored-goal parameters. Slow oscillations
    and sharp-wave ripples coordinate cortical consolidation of
    drive-outcome associations (Balleine & Dickinson 1998; Diekelmann
    & Born 2010). The specificity is substrate-level: SWS replay has
    access to episodic outcome structure but lacks the varied associative
    replay characteristic of REM, making it well-suited to content
    updates and ill-suited to feature-generality updates.
  notes: >
    Paired with MECH-253 (REM template consolidation). Together they
    constitute the phase-separated consolidation that creates and
    maintains the stored-goal vs attentional-template distinction.

    Clinical prediction: SWS disruption should produce selective
    goal-value instability -- the agent continues to search effectively
    for previous goals but shows noisy/shifting preferences. Dissociable
    from REM disruption predictions under MECH-253.

    No evidence expected until SD-017 implementation complete. Registered
    in the pre-implementation claim matrix per user policy of capturing
    ideas at time of insight.

    V4-scoped: depends on full sleep-phase architecture (SD-017) being
    implemented.
```

### MECH-253 (draft) -- REM consolidates template parameters

```yaml
- id: MECH-253
  title: "REM sleep, with varied associative replay and attenuated noradrenergic tone, consolidates template-performance prediction error into updates of z_goal -> attentional-template projection weights (feature-specification update), not into stored-goal content."
  claim_type: mechanism_hypothesis
  subject: sleep.rem_template_consolidation
  polarity: asserts
  status: candidate
  implementation_phase: v4
  claim_level: mechanistic
  registered_utc: 2026-04-17
  depends_on:
    - SD-017           # sleep phase architecture
    - SD-026           # H1 write channel; REM updates its projection weights
    - INV-010          # offline integration required
    - INV-049          # sleep mathematically necessary for model-building
    - INV-037          # stored vs active
  functional_restatement: >
    During daytime operation, template-performance error is accumulated:
    did the deployed precision template successfully identify goal-relevant
    content during search? This error is within-episode, denser, and
    cross-situational. Its legitimate update target is the *template
    projection weights* (template_proj in MECH-251), not stored goal
    content.

    Proposed mechanism: REM sleep's varied associative replay, combined
    with attenuated noradrenergic tone (which reduces the fidelity
    penalty on replay divergence), consolidates template-performance
    error into template_proj updates. REM's cross-situational variance
    is exactly what feature-generality learning requires: the same
    stored goal paired with different contextual instantiations across
    replay episodes lets the projection learn which features are
    goal-diagnostic vs situational.
  notes: >
    Paired with MECH-252 (SWS stored-goal consolidation). Phase-separated
    consolidation creates and maintains the stored-goal / template
    distinction. Without REM, template projection drifts toward stored
    goal content (template collapses into retrieval); without SWS, stored
    goals drift toward whatever the template currently finds (goals
    collapse into salience).

    Clinical prediction: REM disruption should selectively impair
    goal-directed search quality (template performance) before producing
    goal-amnesia. Partial REM deprivation should degrade template-driven
    search with relative sparing of stored-goal retrieval. Dissociable
    from MECH-252 predictions. Consistent with long-standing findings
    that REM deprivation impairs procedural / implicit learning more
    than declarative recall (Smith 2001; Diekelmann & Born 2010).

    No evidence expected until SD-017 implementation complete. Registered
    in the pre-implementation claim matrix per user policy.

    V4-scoped: depends on SD-017 phase architecture and SD-026 template
    channel being implemented.
```

---

## Proposed commit plan (v2, post-review 2026-04-17)

1. Commit **SD-026 + MECH-251** to claims.yaml (V3, testing gated on SD-014).
2. Commit **MECH-252 + MECH-253** to claims.yaml (V4 candidate, pre-implementation matrix; sleep-phase-separated consolidation, split by phase).
3. **Edit INV-012** in claims.yaml to add `depends_on: [SD-026]` with explanatory note -- INV-012's coherence is load-bearing on the deliberate/reflexive attention distinction that SD-026 provides.
4. Run `python scripts/build_claims_json.py` to rebuild site tooltip data.
5. Update WORKSPACE_STATE.md Recent Work with the attention-cluster registration.
6. **Do NOT queue an EXQ yet** for SD-026. Gated on SD-014 being at least provisional.
7. When SD-014 lands: queue V3-EXQ-SD026a (dan_feedback ablation on SD-014-separated z_resource substrate).
8. Follow-up (future session): sketch H2 (pulvinar-TRN access gate) and H3 (vmPFC-dlPFC template compiler) once SD-026 has evidence. Not registering these yet; premature without the H1 validation.

## Summary of dependency graph changes

New edges introduced:
- SD-026 -> {SD-012, SD-014, INV-009, INV-034, INV-037, INV-038, MECH-007}
- MECH-251 -> {SD-026, ARC-007, INV-009}
- MECH-252 -> {SD-017, INV-010, INV-049, INV-037, INV-038}
- MECH-253 -> {SD-017, SD-026, INV-010, INV-049, INV-037}
- INV-012 -> {SD-026}  # NEW edge into a formerly dep-free invariant

Notable: INV-012 previously had `depends_on: []`. This edit makes it depend on a V3 SD, which is structurally unusual (invariants are typically substrate-independent). The justification is that INV-012 is not merely *compatible with* but *load-bearing on* the existence of a prospective attention mechanism. Worth flagging to governance if this pattern should be generalised (other invariants may have similar implicit substrate requirements).
