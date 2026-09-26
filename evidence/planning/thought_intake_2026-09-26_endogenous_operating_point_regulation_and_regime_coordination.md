# Thought intake -- endogenous operating-point regulation and regime coordination

**Date:** 2026-09-26
**Raw thought:** `docs/thoughts/2026-09-26_endogenous_operating_point_regulation_and_regime_coordination.md` (user-written; 350 lines, read in full)
**Companion (sibling):** `docs/thoughts/2026-09-26_dynamic_control_coordination_hole.md` (same core hypothesis, captured earlier today by the coupled-loop orchestrator). Ingested in the same session on the user's instruction via its own short intake, `thought_intake_2026-09-26_dynamic_control_coordination_hole.md`, which registers nothing new and uses sec 6 below. Its 9-step AUDIT stays deferred until the coupled-loop campaign reaches a clean stop -- see section 7.
**Session:** `thought-intake-20260926`. Drafted by a read-only research agent (drafting ids OP-1..OP-3), reviewed and registered by the orchestrating session on 2026-09-26 as ARC-155, ARC-156, Q-111.
**Digestion drafts:** `evidence/planning/thought_digestion_staged_2026-09-26_thought_intake_batch.md` (section "operating point"; content drafted in the companion scratch file `digestion_operating_point.md`, to be merged into that staging doc and landed in the same commit as this intake)

---

## 1. Verbatim prompt (core proposal, tight paraphrase + quotes)

The recent confirmed failure autopsies suggest that REE's next deficit is not a missing subsystem. It is the absence of endogenous regulation of **when** existing mechanisms dominate, **how strongly** their signals count, **when** a regime should end, and **how** several controllers coexist without one nullifying another. The user frames this as a *distributed coordination problem*, explicitly not evidence for a central executive, and asks that three hypotheses be governed separately rather than the proposition "REE needs a dynamic controller":

- **H1 Adaptive control normalization** -- control quantities whose scale changes through learning, seed, development or state need endogenous normalization / operating-point regulation; fixed raw constants produce permanent crossing, permanent silence, saturation and scale-determined dominance.
- **H2 Regime-independent escape evidence** -- any strong regime that suppresses interaction or information gathering needs at least one endogenous termination source not itself eliminated by that regime (freeze is the canonical case; extends to habit, fixation, exploit-only, defence, suppressed plasticity, commitment, confident attractors).
- **H3 Distributed controller arbitration** -- simultaneously active controllers need some way to regulate relative causal authority so that one does not remove the behavioural or informational substrate another needs; need not be an executive module.

Plus a related-but-separate principle: **signal validity** ("A live signal is not necessarily a valid signal"; scaling cannot repair wrong semantics). And an experimental strategy: freeze-lock confirmer first, then minimal separate discriminators, endogenous information only, no oracle knowledge of condition; known regime-locking artefacts must be resolved or controlled before an integrated-organism failure is read as evidence against E1/E2/E3.

### 1a. Evidence the thought cites, mapped to the actual records (re-measured 2026-09-26)

The raw thought names no run ids. Its three cross-autopsy threads map as follows (all autopsies CONFIRMED 2026-09-26T10:43:53Z in batch `failure-autopsy-20260926-batch7`):

| Thought section | Record | What it actually shows |
|---|---|---|
| 1. Freeze self-locks; release source-starved | `failure_autopsy_V3-EXQ-1107_2026-09-26.md` (SD-032a/MECH-157 harness) + `failure_autopsy_V3-EXQ-1106_2026-09-26.md` (MECH-287 option-B Stage 0) | 1107: post-training `||z_harm_a||` 2.8-4.2 vs `theta_freeze` 0.8, `max_freeze_duration` 0 (never) -> lock provable from tick 1; 15/15 eval lives 6 steps; latent identical on all 90 eval ticks (input-insensitive, saturated encoder). 1106: option-B release path read 0 drive-steps-while-frozen on 3/3 seeds -- "A release path that reads movement-generated events cannot release a lock that stops movement; the path needs a movement-independent source." Both unmasked by the ree-v3 `1fc881692d` STAY-fix (GFLAG-0508, open). |
| 2. Operating points not invariant to learned scale | `failure_autopsy_V3-EXQ-1067_2026-09-26.md` (MECH-266/SD-032a squash-vs-clamp) + `failure_autopsy_V3-EXQ-1104_2026-09-26.md` (SD-032b effort proxy) + `mode_switch_cea_mechanism_trace_20260925.md` | 1067: `dacc_pe` exceeds the cap on 100% of ticks (abs max 11.2); the "graded" squash is the clamp at effective cap `c*v/(c+v)` -- a pure gain cut; "a fixed-sigma squash is not scale-free". 1104: effort term range 0.005-0.031 vs payoff range 15.8-161 (3-4 orders of magnitude). Mode trace sec 0.3: `dacc_pe` falls back to `||z_harm_a||` when `use_e2_harm_a` is off, so the switching alarm and the CeA gate read the SAME unanchored encoder magnitude (0.14-0.20 untrained vs 12-17 after the SD-011 `harm_accum` aux). |
| 3. Locally valid controllers behaviourally irrelevant | `failure_autopsy_V3-EXQ-1090_2026-09-26.md` (MECH-449 endogenous safety veto) | Veto fires (C1 3/3), is calibrated (C2), silent on control (C4) -- but executed action is 0 on 3,000/3,000 recorded ticks (freeze on, pre-STAY-fix), and on all-fired ticks the strongest-F vetoed candidate executes anyway ("inert alarm"). Learning: "A selection-layer veto validated on an agent whose executed action never varies validates arithmetic only; require an action-diversity precondition." |
| Signal validity | 1104 autopsy | "The fix is NOT a larger cost constant: scaling a model-error term until it dominates E3 selection would make selection noise-driven." GFLAG-0447 (open) already owns the producer-validity gate. |
| Important negative evidence | 1105a (MEASURES: under-induced positive control), 1099 (MEASURES + ENVIRONMENT: stale 231a baseline), 1108 (see note) | Consistent with the thought's own caution. |

**Note on V3-EXQ-1108** (`failure_autopsy_V3-EXQ-1108_2026-09-26.md`, confirmed 11:00:42Z): it is the N2 replay-policy probe (stored-z replay ruled out; re-encode fails (a)/(e) as registered), not a freeze/mode/veto run, and none of the thought's three threads rests on it. It is tangentially relevant to H1 only: under W6a the test-set norm rises x10.5-12.0 as the encoder trains, and its leg (e) is carried partly by the EMA zero-init artefact (GFLAG-0559/0560). That is further evidence that learned latent magnitudes drift by an order of magnitude within a lifetime, and further reason any H1 test must exclude near-reset ticks.

**Additional current evidence the thought does not cite but which bears on H1:** `cea_onset_input_reprobe_20260925.md` (GFLAG-0557, open). Relative gates on `z_harm_a` (rate, z-score) are NEGATIVE against their own floor in both env configs. The missing CeA onset information is a stream-choice / information-content problem, and scale-relative gating on the saturated stream does not recover it. This is exactly the thought's signal-validity boundary: normalization cannot restore information the producer has already destroyed. It is load-bearing for ARC-155's non-degeneracy precondition (below).

---

## 2. What's new vs existing REE claims (novelty table)

| Thread in the thought | Existing REE coverage | Verdict |
|---|---|---|
| "Correct machinery exists, but the organism does not autonomously create the conditions under which that machinery can be used" | **ARC-131** (installability: a component PASS "does not establish that the whole agent can enter the states in which the mechanism operates"; lists "scale/variance of competing signals" and "downstream action-space and commitment dynamics" as composition conditions). **ARC-130** (existence -> ... -> committed throughput -> ecological consequence). **ARC-120**. | **Already owned** as an audit/interpretation framework, near-verbatim. Cross-ref only. The thought's three hypotheses are the *constructive* requirements ARC-131 describes only as failure conditions. |
| Freeze lock: fixed threshold vs trained harm magnitude, no release -> catatonia | **MECH-279** (PAG freeze gate; "failure of exit produces sustained immobility characteristic of stuporous catatonia"). **SD-036** (GABAergic decay as missing regulator of harm-stream lock-in, EXQ-471). **MECH-202B** / catatonia route taxonomy in `psychiatric_failure_modes.md`. GFLAG-0508 (open). Substrate-queue `MECH-279` amendment from the 1107 autopsy; chip `chip-20260926-pag-freeze-lock-confirmer` (task_ad36ff97). | **Already owned** as a mechanism and a named failure mode. The confirmer the thought ranks "highest-value immediate" is already chipped. Cross-ref only. |
| Release pathway source-starved by the frozen state ("leave freeze when evidence changes -> evidence cannot change because frozen") | **MECH-287** option-B record (1106 learning: needs a movement-independent source; claims.yaml now records option A re-anchor). **MECH-280** (LH-PAG override: hunger raises theta_freeze -- an interoceptive, regime-surviving release input; `substrate_ceiling`, SD-037 override never built per GFLAG-0506). **MECH-356** (parasympathetic rebound on the z_harm_a derivative -- NOT regime-surviving when z_harm_a is pinned). **SD-099/MECH-489** (identification accumulator driven by decay of the triggering channel's excess-over-baseline). | Instance **owned**. MECH-280 is the registered regime-surviving freeze release. |
| **H2 generalised: any strong regime must not depend exclusively on consequences it suppresses for its own termination** | **ARC-128** (termination taxonomy -- records WHY a process ended; silent on WHERE termination evidence comes from). **MECH-497** (a persistent process degrades its OWN gating confidence -- evidence *corruption* by the process; OCD checking). **MECH-527 + MECH-482** (stuckness-triggered escape; the trigger is a persistence-integrating accumulator). **MECH-433** (LC-NE tonic shift licenses disengagement; v4). **MECH-354** (fatigue accumulator emits STOP). **MECH-266** (asymmetric exit threshold). None states the cross-regime requirement or names the evidence-*starvation* route. | **Adjacent but distinct -- register narrowly as ARC-156.** It is the evidence-STARVATION sibling of MECH-497's evidence-CORRUPTION route, and the unifying reason why MECH-280, MECH-482/527, MECH-354 and MECH-433 all integrate time or interoception. |
| dACC PE saturates fixed caps; effort 3-4 orders below payoff; CeA absolute threshold on unanchored latent | **Q-041** (does REE need a unified meta-level threshold supervisor, or do scattered adaptive loci -- ARC-016, SD-032c/d/e -- self-coordinate? Its WWA already demands the `dacc_pe_cap` be replaced by an adaptive one before coherence is measured). **ARC-016** (E3 precision = running variance of own PE: already scale-relative). Local scale-relative precedents: **SD-099** (excess-over-baseline), **MECH-449** (running-z veto), **SD-106** (scale-normalised reconstruction), **MECH-459** (return-scale invariance). **MECH-404** (gain inside an operating window; v5 social). **GOV-CRITBAR-1** (the governance-side analogue: a bar must be denominated on the run's own control, not an absolute from rationale). Substrate-queue `mode-governance-engagement` (margin-normalised cap rule, local). | **Adjacent but distinct -- register narrowly as ARC-155.** Q-041 asks whether cross-substrate thresholds need a *supervisor* for coherence under chronic load. ARC-155 makes a per-channel constructive claim: a control operating point that reads a *learned* quantity must be denominated on an endogenous scale estimate. It also carries the competing producer-anchoring account and the no-habituation constraint. REE already applies the principle piecemeal (ARC-016, SD-099, MECH-449). No claim states it, and the shipped PAG, CeA, dACC-cap and SD-032b constants violate it. |
| **H3 controllers nullify each other's substrate** (freeze nullifies veto; threat suppresses repair; habit nullifies deliberation; exploration vs commitment) | **Q-016** (tri-loop gate arbitration without coupling collapse; unannotated, active). **ARC-107 / MECH-449** (BG selector constitution: lawful access, not scalar dominance -- one candidate answer at the selection locus). **MECH-312a-d / MECH-235 / MECH-163** (habit vs deliberative arbitration weights). **MECH-534 / ARC-145** (authority field / jurisdiction; v4) and **Q-106**. **ARC-088** (partially independent gated evaluators as anti-collapse). **ARC-131** (composition failure, audit side). **Q-041** (supervisor vs scattered, thresholds only). | **Adjacent but distinct -- register as an open question, Q-111.** Every existing claim either supplies a *candidate mechanism* (ARC-107, MECH-534) or *describes* composition failure (ARC-131). None asks the thought's discriminating question: after per-controller scale (ARC-155) and escape-evidence (ARC-156) corrections, does substrate-removal interference persist? The thought's own falsifier makes this question-shaped. |
| Signal validity: a live signal is not a valid signal; scaling cannot repair wrong semantics | **GFLAG-0447** (open; effort producer derived from a harm model double-counts harm). **MECH-354** (effort decoupled from harm). **Q-080**. **INV-105** (encoded != ... != causally used != behaviourally beneficial). **ARC-130**. **MECH-449** / **ARC-107** ("not by any single louder channel"; "STRENGTH is necessary but not sufficient"). **GOV-PATHVALID-1**. 1104 autopsy learning. | **Owned** piecewise. **Not registered.** A design-review rule candidate is recorded in section 7 for /governance: a gain/cost sweep on a control term may not be used to establish the producer's validity. |
| Biological analogy: distributed neuromodulatory / thalamocortical / BG / salience / hippocampal-mismatch / LC / ACh / DA / 5-HT / oscillatory coordination; no global executive scalar | **ARC-065** (LC-NE tonic + FPC + striatal novelty + hippocampal sampling), **MECH-313**, **MECH-433** (LC explore/exploit gain), **MECH-398 / MECH-207** (ACh plasticity / surprise-buffer gates, v4; N5 P1: zero ree_core hits), **ARC-154** (DA-ACh coordination layer), **MECH-043** (DA precision), **MECH-204** (5-HT REM zero-point), **SD-032a / MECH-259** (salience network), **ARC-107** (BG), **MECH-534 / ARC-145 / MECH-560 / MECH-561** (routing / phase), **MECH-228 / MECH-270** (ephaptic, contributor only), **MECH-039** ("modes are regions in control-channel space, not separate modules"), **INV-022** (trust/precision allocation heterogeneous, not one scalar). | **Owned.** No claim. INV-022 + MECH-039 already carry "no single global scalar". |
| Ephaptic / field coordination only if simpler mechanisms fail | `v3_v4_phase_substrate_boundary.md` ("functional insufficiency, not biological completeness, is the trigger"); the MECH-588/589 revocation-trigger amendment owed to /governance (`thought_intake_2026-09-24_dynamic_coordination_repertoire_monostrategy.md` sec F1). | **Owned.** |
| Regime-locking artefacts must be resolved before an integrated-organism failure is charged to REE | **GOV-FAILLOC-1** (REE-failed only after mechanism, measures and environment are each established). **GOV-JURIS-1** / organism-validation doctrine. **Q-108** (non-oracular adaptive-recovery event). | **Owned.** The A1-ordering decision is the companion's audit step 8, and a governance decision rather than a claim. |
| "Don't govern 'REE needs a dynamic controller'" | **Q-041** carries the supervisor-vs-scattered alternative. ARC-155..Q-111 are drafted non-monolithic by construction. | Honoured. No executive/controller claim is registered. |

---

## 3. Key formulations (verbatim from the raw thought)

> REE may possess much of the machinery required for several cognitive regimes while lacking sufficiently endogenous regulation of the operating points, transitions and interactions that determine when the organism should become what.

> **leave freeze when evidence changes → evidence cannot change because the organism is frozen.**

> A strong cognitive regime should not depend exclusively on consequences suppressed by that regime to determine whether the regime should terminate.

> This suggests that some control variables may need to be defined relative to endogenous scale estimates rather than absolute raw magnitudes.

> Thus a mechanism can be: implemented; causally connected; locally responsive; and still irrelevant to organism-level behaviour.

> A live signal is not necessarily a valid signal.

> Scaling and arbitration cannot repair a control quantity whose semantics are wrong.

> The correct machinery exists, but the organism does not autonomously create the conditions under which that machinery can be used appropriately.

> **How strong should this signal count right now?** / **When should this regime end?** / **What happens when two valid controllers want incompatible things?**

> The important next move is therefore not to design the answer in advance. It is to make those questions experimentally unavoidable.

---

## 4. Affected existing claims

Proposed as `depends_on` / `related_claims` wiring only. **No existing claim's status, confidence, category, phase or evidence record is touched by this intake.**

- **ARC-131 / ARC-130 / ARC-120** -- the audit framework. ARC-155..Q-111 are the constructive requirements behind two of ARC-131's listed composition conditions. `depends_on` of all three.
- **MECH-279, MECH-280, SD-036, MECH-356, MECH-287** -- the freeze instance. ARC-156 cites MECH-280 as the registered regime-surviving release and MECH-287 option B (1106) as the measured counter-example. ARC-155 cites MECH-279's absolute `theta_freeze` as the first test site.
- **MECH-497 / ARC-128** -- ARC-156's siblings (evidence corruption vs evidence starvation; why vs from-where of termination). Both are v4, so they go in `related_claims` of the v3-scoped ARC-156 (the same phase-leak discipline as MECH-588 -> ARC-145).
- **MECH-527 / MECH-482 / MECH-354 / MECH-266 / MECH-433** -- existing regime-surviving or asymmetric-exit instances that ARC-156 unifies (MECH-433 in `related_claims`, v4).
- **Q-041** -- ARC-155 is distinguished from it (per-channel denomination vs cross-substrate supervisor coherence), and Q-111 from it (substrate-removal interference vs threshold coherence). ARC-155's corrected channels would supply Q-041's own non-degeneracy precondition (it asks for `dacc_pe_cap` to be replaced by an adaptive one).
- **ARC-016, SD-099, MECH-449, SD-106, MECH-459** -- local precedents that already implement ARC-155's principle. **GOV-CRITBAR-1** -- its governance-side analogue (`related_claims`).
- **MECH-046, SD-035, SD-032a, MECH-266, SD-032b, SD-011** -- shipped absolute operating points implicated by the 1067/1104/mode-trace evidence. SD-011 is included because the `harm_accum` aux is what inflates `||z_harm_a||` ~100x.
- **Q-016, ARC-107, MECH-449, MECH-312, MECH-163, MECH-235** -- candidate arbitration loci named by Q-111. **MECH-534, ARC-145, Q-106, MECH-589, ARC-154** in `related_claims` (v4).
- **GFLAG-0447, MECH-354, Q-080, INV-105** -- signal-validity owners. Not amended.

**Currency lag noticed (not a defect of this intake):** MECH-279's claims.yaml entry does not yet record the 1106/1107 lock finding. The autopsies were confirmed 10:43Z today, so /governance has not yet applied them. SD-032a and Q-041 do not yet record 1067 or the mode-trace "switch once then lock" finding. MECH-046 does not record GFLAG-0556/0557. All are routed through open flags or confirmed autopsies, so this intake raises no new flag.

---

## 5. Candidate claims -- REGISTERED this pass (ARC-155, ARC-156, Q-111)

Placement: a new stub `docs/architecture/endogenous_operating_point_regulation.md` holds all three. Proposed frontmatter: `title: Endogenous Operating-Point Regulation and Regime Coordination`, `parent: "Control, Precision & Neuromodulation"`, `grandparent: Architecture`, `nav_order: 24` (current max in that parent is 23), `status: candidate`, `status_asof: 2026-09-26`, `status_claim: ARC-155`. It gets one anchor per claim. `persistent_process_termination_taxonomy.md` gets a one-line cross-link to ARC-156 (its sec 2b already hosts MECH-497).

Registered ids (drafting id -> real): OP-1 -> **ARC-155** (architectural_commitment), OP-2 -> **ARC-156** (architectural_commitment), OP-3 -> **Q-111** (open_question). The blocks below are as registered.

### ARC-155 -- scale-relative control operating points

```yaml
- id: ARC-155
  title: 'A control operating point (threshold, cap, saturation constant, or cost weight) that reads a LEARNED
    quantity -- a latent magnitude, prediction error, salience, effort, confidence or threat signal whose
    distribution moves across training, seeds, developmental stage and state -- must be denominated on an
    endogenous estimate of that quantity''s own scale (or on a producer whose scale is anchored), not on an
    absolute raw constant; otherwise the regime it gates is determined by arbitrary numerical scale rather
    than information content, and degenerates to permanent crossing, permanent silence, saturation (a graded
    transform collapsing to a gain change), or scale-determined dominance between controllers. The
    denomination must preserve the condition-relevant discrimination of the signal: an operating point that
    stabilises regime occupancy by habituating to a chronically high signal (normalising real danger into
    ''baseline'') violates this claim rather than satisfying it, and no denomination can restore information
    the producer has already lost.'
  claim_type: architectural_commitment
  subject: control_plane.scale_relative_operating_points
  polarity: asserts
  status: candidate
  epistemic_category: substrate_conditional
  implementation_phase: v3
  version_relevance: v3_v4
  registered_utc: '2026-09-26'
  source_thought: docs/thoughts/2026-09-26_endogenous_operating_point_regulation_and_regime_coordination.md
  location: docs/architecture/endogenous_operating_point_regulation.md#arc-155
  depends_on:
  - ARC-131
  - ARC-130
  - Q-041
  - ARC-016
  - MECH-279
  - MECH-046
  - SD-032a
  - MECH-266
  - SD-032b
  - SD-011
  - SD-099
  - MECH-449
  related_claims:
  - GOV-CRITBAR-1
  - SD-106
  - MECH-459
  - MECH-404
  - INV-022
  - MECH-043
  source:
  - docs/thoughts/2026-09-26_endogenous_operating_point_regulation_and_regime_coordination.md
  - evidence/planning/thought_intake_2026-09-26_endogenous_operating_point_regulation_and_regime_coordination.md
  notes: |
    Registered from the 2026-09-26 thought (hypothesis H1, "adaptive control normalization"). The thought's
    evidence, re-measured: V3-EXQ-1107 (post-training ||z_harm_a|| 2.8-4.2 vs theta_freeze 0.8 -> freeze from
    tick 1); V3-EXQ-1067 (dacc_pe above the cap on 100% of ticks, abs max 11.2; the "graded" squash equals the
    clamp at effective cap c*v/(c+v), a pure gain cut); V3-EXQ-1104 (effort term 0.005-0.031 vs payoff range
    15.8-161); mode_switch_cea_mechanism_trace_20260925.md (CeA 0.5 threshold vs low_freq 0.14-0.20 untrained,
    12-17 after the SD-011 harm_accum aux). All four autopsies are confirmed 2026-09-26. V3-EXQ-1108 adds that
    the test-set norm rises x10.5-12 within a lifetime as the encoder trains.
    EXTENDS the piecemeal precedents REE already has: ARC-016 (E3 precision = running variance of its own PE),
    SD-099 (excess-over-baseline onset), MECH-449 (running-z veto), SD-106 (scale-normalised reconstruction),
    MECH-459 (return-scale invariance). It states them as one requirement that the shipped PAG (MECH-279), CeA
    (MECH-046), dACC cap (SD-032a/MECH-266) and SD-032b effort-cost constants currently violate.
    EXPLICITLY DISTINCT FROM Q-041: Q-041 asks whether cross-substrate adaptive thresholds need a SUPERVISOR
    for coherence under chronic load. ARC-155 is per-channel and supervisor-free: each operating point is
    denominated on its own signal's endogenous scale. ARC-155 is compatible with either Q-041 answer, and ARC-155's
    corrected channels supply the adaptive dacc_pe_cap that Q-041's own non-degeneracy precondition asks for.
    DISTINCT FROM ARC-131, which lists "scale/variance of competing signals" as a condition under which an
    installed mechanism fails to express itself (audit side). ARC-155 is the constructive requirement.
    DISTINCT FROM GOV-CRITBAR-1, the governance-side analogue (a criterion bar must be denominated on the
    run's own control arm, not on an absolute from rationale). ARC-155 is the organism-side form.
    COMPETING ACCOUNT, carried in the claim, not resolved: anchor the PRODUCER's scale (e.g. a
    magnitude-anchored encoder objective) rather than normalise at each CONSUMER. The mode-trace sec 0.3 finding
    that the switching alarm (dacc_pe fallback) and the CeA gate read the SAME unanchored z_harm_a encoder makes
    producer anchoring a live alternative for three of the four instances. If producer anchoring alone suffices,
    ARC-155 narrows to an encoder-anchoring claim; that is a narrowing, not a refutation.
    SIGNAL-VALIDITY BOUNDARY (built into the title): cea_onset_input_reprobe_20260925.md (GFLAG-0557) shows
    relative gates on z_harm_a fail below their own floor in both env configs, because the onset information
    is absent from the stream. V3-EXQ-1107's z_harm_a is identical on all 90 eval ticks. Scale-relative
    denomination cannot rescue a channel with no condition-relevant content, so a null on such a channel is
    uninterpretable, not evidence against ARC-155 (see the digestion draft, precondition P1). The 1067 autopsy's
    warning also stands: a normaliser does not by itself make a register graded. It moves the transition.
    Literature anchor: divisive normalisation (Carandini & Heeger 2012) is already on file via
    targeted_review_salience_gain_normalisation (cited in the 1067 autopsy). NOT yet verified against ARC-155's
    specific claim, which is scale-relative denomination with preserved discrimination. Biology normalises by
    pooled/contextual activity, not by pure self-z. The adaptation-vs-habituation tension needs a /lit-pull
    before hardening.
    VERSION ROUTING (flag for /governance, not decided here): registered v3 / v3_v4 because the failing
    instances are live V3 substrate and the cheapest test site (the PAG freeze gate, MECH-279) exists. It is
    sequenced behind chip-20260926-pag-freeze-lock-confirmer and behind a P1 information-content measurement on
    the channel under test. If P1 fails for z_harm_a, the test site moves to a channel with validated content
    (the raw hazard-proximity scalar GFLAG-0557 names is not yet exposed to the agent).
    DO NOT build a general normaliser or "operating-point regulator" module from this claim. DO NOT queue an
    experiment from it without a /governance routing decision. Any build is a default-OFF,
    single-operating-point change via /implement-substrate.
```

### ARC-156 -- regime-surviving termination evidence

```yaml
- id: ARC-156
  title: 'A strong regime that suppresses the organism''s normal interaction or information gathering (freeze,
    defensive mode, exploit-only or monostrategic policy, habitual dominance, attentional fixation, frozen
    plasticity, strong commitment, a high-confidence attractor) must have at least one endogenous termination
    input that continues to change DURING the regime -- time- or interoception-integrating accumulators,
    exogenous change the organism can sense without acting, or internally generated probes -- because a regime
    whose exit condition is a function only of evidence produced by the behaviour it suppresses is absorbing
    in any environment that does not change on its own. This evidence-STARVATION route to termination failure
    is distinct from evidence CORRUPTION (a process degrading its own gating variable, MECH-497); the two can
    co-occur, and a fix for one does not fix the other.'
  claim_type: architectural_commitment
  subject: control_plane.regime_surviving_termination_evidence
  polarity: asserts
  status: candidate
  epistemic_category: substrate_conditional
  implementation_phase: v3
  version_relevance: v3_v4
  registered_utc: '2026-09-26'
  source_thought: docs/thoughts/2026-09-26_endogenous_operating_point_regulation_and_regime_coordination.md
  location: docs/architecture/endogenous_operating_point_regulation.md#arc-156
  depends_on:
  - ARC-131
  - MECH-279
  - MECH-280
  - MECH-287
  - SD-036
  - MECH-356
  - MECH-527
  - MECH-482
  - MECH-354
  - MECH-266
  related_claims:
  - MECH-497
  - ARC-128
  - MECH-433
  - MECH-398
  - MECH-207
  - Q-108
  source:
  - docs/thoughts/2026-09-26_endogenous_operating_point_regulation_and_regime_coordination.md
  - evidence/planning/thought_intake_2026-09-26_endogenous_operating_point_regulation_and_regime_coordination.md
  notes: |
    Registered from the 2026-09-26 thought (hypothesis H2). MEASURED INSTANCE: V3-EXQ-1106 (MECH-287 option-B
    release path: 0 drive-steps-while-frozen on 3/3 seeds; the path's sources, new event boundaries and
    staleness H, cannot accrue while the agent does not move, and the build doc predicted the 0 in writing).
    The autopsy's own learning is "the path needs a movement-independent source". V3-EXQ-1107 supplies the
    lock (exit requires ||z_harm_a|| < 0.8, and ||z_harm_a|| is pinned while frozen next to a hazard). A SECOND
    live instance, not cited by the thought: n5_ach_gated_unfreeze_probe_20260926.md -- the on-policy stream of
    a concentrated (42-94% modal class), wall-pressing policy carries little information about an action-map
    shift, so surprise-based detection fires at base rate. The probe's proposed remedy, periodic active
    probing, is a regime-surviving evidence source in exactly ARC-156's sense (the wall-pressing mechanism is the
    probe's stated, unmeasured hypothesis, sec 4.2).
    DERIVATIONAL CORE: if the environment state relevant to the exit condition does not change without the
    agent's action, and the exit condition reads only observations whose change requires actions the regime
    removes, the regime is an absorbing state. The empirical content is (i) which REE regimes have that
    structure today and (ii) whether a surviving source terminates them APPROPRIATELY (condition-sensitive),
    not merely eventually (a timer).
    UNIFIES existing instances that already integrate time or interoception and therefore survive their
    regime: MECH-280 (LH-PAG hunger override of freeze; substrate_ceiling -- the SD-037 override is unbuilt,
    per GFLAG-0506); MECH-482 -> MECH-527 (the epistemic_deficit accumulator grows with persistence and
    triggers escape from a false-bottom attractor); MECH-354 (the fatigue accumulator emits STOP); MECH-433
    (LC tonic shift on waning utility; v4); SD-036 (decay). COUNTER-INSTANCES: MECH-356 (fires on a NEGATIVE
    z_harm_a derivative, which cannot occur while z_harm_a is pinned) and MECH-287 option B (above).
    EXPLICITLY DISTINCT FROM MECH-497, which is evidence CORRUPTION: checking degrades the confidence that
    gates stopping. ARC-156 is evidence STARVATION: the regime prevents the evidence from being generated at all.
    Both are self-referential termination failures reached by different causal routes, just as MECH-497 is
    itself distinguished from MECH-080's attractor-depth route.
    DISTINCT FROM ARC-128, which says every persistent process needs a termination taxonomy recording WHY it
    ended. ARC-156 constrains WHERE the terminating evidence may come from.
    DISTINCT FROM ARC-131, which describes the failure (the agent cannot enter the states in which a
    mechanism operates). ARC-156 is the constructive requirement for the special case where the regime itself
    blocks those states.
    DISTINCT FROM MECH-266 (asymmetric enter/exit thresholds): hysteresis on an exit threshold does not help
    if the exit input cannot move.
    NOT a licence for condition-blind termination: a fixed max-duration timer (pag_max_freeze_duration)
    guarantees exit but carries no evidence. The digestion draft uses it as the control arm ARC-156 must beat on
    appropriateness.
    Literature anchor (NOT verified for this claim): the MECH-280 anchors (de Araujo Salgado 2023, sustained
    hunger overrides predator avoidance; Marino 2020) cover the freeze instance. The cross-regime principle
    needs its own /lit-pull (tonic immobility termination; LC-mediated disengagement, Aston-Jones & Cohen
    2005; exploration under stuckness).
    VERSION ROUTING (flag for /governance): v3 / v3_v4 because both measured instances (1106 freeze, N5
    detection) are live V3/campaign substrate. The general cross-regime form is compass. DO NOT build a
    generic "escape evidence" module. DO NOT queue an experiment from ARC-156. The freeze leg's build question
    belongs to MECH-280 / SD-037 and the 1107 substrate-queue amendment. The N5 leg belongs to the coupled-loop
    campaign (N5b). Respect the MECH-287 option-A decision (rec-20260926-78ecb89a): ARC-156 does not reopen
    MECH-287b.
```

### Q-111 -- does substrate-removal interference survive per-controller correction?

```yaml
- id: Q-111
  title: 'Once each simultaneously active REE controller is individually validated, operating-point corrected
    (ARC-155) and given regime-surviving exit evidence (ARC-156), do the existing controllers compose without one
    removing the behavioural or informational substrate another needs (freeze removing the action freedom a
    safety veto acts over; threat mode suppressing the plasticity or exploration that model repair needs;
    commitment suppressing needed exploration and vice versa) -- or does destructive interference persist, so
    that REE needs an explicit DISTRIBUTED authority-regulation principle (reciprocal inhibition, precision or
    gain weighting keyed on the other controller''s state, basal-ganglia-like lawful access, state-dependent
    routing) that is not a central executive?'
  claim_type: open_question
  subject: control_plane.controller_composition_substrate_interference
  polarity: asserts
  status: candidate
  epistemic_category: substrate_conditional
  implementation_phase: v3
  version_relevance: v3_v4
  registered_utc: '2026-09-26'
  source_thought: docs/thoughts/2026-09-26_endogenous_operating_point_regulation_and_regime_coordination.md
  location: docs/architecture/endogenous_operating_point_regulation.md#q-111
  depends_on:
  - ARC-155
  - ARC-156
  - ARC-131
  - ARC-130
  - Q-041
  - Q-016
  - ARC-107
  - MECH-449
  - MECH-279
  - SD-032a
  - MECH-312
  - MECH-163
  related_claims:
  - MECH-534
  - ARC-145
  - Q-106
  - MECH-589
  - ARC-154
  - ARC-088
  - INV-022
  source:
  - docs/thoughts/2026-09-26_endogenous_operating_point_regulation_and_regime_coordination.md
  - evidence/planning/thought_intake_2026-09-26_endogenous_operating_point_regulation_and_regime_coordination.md
  notes: |
    Registered from the 2026-09-26 thought (hypothesis H3). Registered as an OPEN QUESTION, not an
    architectural commitment, because the thought's own falsifier is question-shaped: "If the existing
    controllers compose appropriately once their individual scales and inputs are corrected, then no
    additional arbitration principle is required." MEASURED MOTIVATING CASE: V3-EXQ-1090. The MECH-449 veto
    fires (3/3), is calibrated, and is silent on its control, yet the executed action is 0 on 3,000/3,000
    ticks (freeze on), and on all-fired ticks the strongest-F vetoed candidate executes anyway. The veto is
    "coupled but inert by STARVED UPSTREAM". SECOND CASE: mode_switch_cea_mechanism_trace_20260925.md sec 1. The
    coordinator's only salience source (dacc_pe) is also the dominant internal_planning affinity source, so the
    ticks that could fire a switch push the argmax away; one switch per life, then lock (0/0/0 reversals);
    reversals return only with an independent external-task input (0/0/0 -> 2/16/25). This is a shared-source
    coupling defect between two controller roles. It straddles ARC-156 (the exit evidence is not independent of
    the entry cause) and Q-111.
    EXPLICITLY NOT A MONOLITHIC EXECUTIVE (a constraint set by both the thought and its companion
    2026-09-26_dynamic_control_coordination_hole.md). The "principle", if needed, is asked to be distributed.
    Candidate loci are ALREADY registered and are answers to test, not new claims: ARC-107/MECH-449 (lawful
    access at the selection gate), MECH-312a-d/MECH-235/MECH-163 (habit vs deliberative arbitration weights),
    Q-016 (tri-loop gate arbitration), MECH-534/ARC-145 (authority field / jurisdiction, v4), ARC-154 (DA-ACh
    coordination, v4).
    DISTINCT FROM Q-041, which asks whether adaptive THRESHOLDS stay coherent across substrates without a
    supervisor (DV: co-movement of threshold series). Q-111 asks whether controllers destroy each other's
    action or information SUBSTRATE (DV: each controller's retained behavioural consequence in composition).
    The two can come apart in either direction.
    DISTINCT FROM ARC-131, which asserts that composition CAN defeat an installed mechanism (audit). Q-111 asks
    whether that defeat is removable by per-controller correction alone.
    DISTINCT FROM Q-016, which is scoped to tri-loop gate conflict and coupling collapse inside E3 commitment.
    Q-111 is cross-system (PAG, selection, mode register, plasticity gating).
    DISTINCT FROM MECH-589 (Type C consensus over-stabilisation): that is one attractor pulling alternatives
    back. Q-111 is about one controller removing another's operating substrate.
    VERSION ROUTING (flag for /governance): v3 / v3_v4. Its first leg (does the veto regain behavioural
    consequence once freeze no longer collapses the action space?) is a re-read of the already-routed 1090a
    (the action-diversity precondition) after the freeze-lock confirmer, so it needs no new substrate. DO NOT
    build an arbitration module. DO NOT queue an experiment from Q-111 until ARC-155/ARC-156 corrections exist for the
    controllers under test.
```

**Deliberately NOT registered:**
- "REE needs a dynamic controller / executive" (the thought and its companion both forbid it; Q-041 already carries the supervisor alternative).
- Signal validity as a claim (owned by GFLAG-0447, MECH-354, Q-080, INV-105, ARC-107/MECH-449; see the design-review rule candidate in sec 7).
- The biological analogy (owned; section 2).
- The freeze-lock confirmer and the A1/integrated-organism ordering (the confirmer is already chipped; the ordering is a governance decision and the companion's audit step 8).
- Any ephaptic or field claim (MECH-228/270 exist; the boundary rule stands).

---

## 6. Companion mergeable paragraph (for the later intake of `2026-09-26_dynamic_control_coordination_hole.md`)

The companion's core hypothesis ("REE may possess the machinery for multiple cognitive regimes while lacking the endogenous mechanism that determines when the organism should become what") is the same proposition as this thought's core observation. It is covered by **ARC-155 + ARC-156 + Q-111 taken together**, with no claim needed for the umbrella itself. When the companion is ingested after its deferred audit, it should register nothing for the following, which are already owned here or elsewhere:

- **Operating scale** ("alter representational precision or routing", saturated or unanchored signals): **ARC-155**.
- **Leaving a regime** ("enter or leave defensive/freeze states", "freeze learning versus reopen plasticity", "quarantine obsolete retained experience and relearn" -- N5's detection failure is ARC-156's second measured instance): **ARC-156**.
- **Coexistence** ("shift between habitual and deliberative", "alter which representations influence E3", the mode-switch one-switch lock): **Q-111**.
- Specific regime choices already owned elsewhere:
  - "trust vs interrogate the world model / treat PE as noise, action failure, model error or environmental change": **MECH-590** (learned PE routing significance), **ARC-037 / MECH-585**.
  - "exploit vs explore": **MECH-433, MECH-527/MECH-482, ARC-065, SD-061**.
  - "freeze learning vs reopen plasticity": **MECH-398, MECH-207, MECH-474** (learning-regime meta-selection).
  - "habit vs deliberative": **MECH-312a-d, MECH-235, SD-081, MECH-163**.
  - "enter/leave defensive states": **MECH-279, MECH-280, MECH-489/SD-099, MECH-357/SD-058**.
  - "change broad operating regime": **SD-032a, MECH-259, MECH-266, MECH-157**.
  - "the non-oracular adaptive-recovery target itself": **Q-108**.
  - "supervisor vs scattered loci": **Q-041**.
  - "mechanism exists but cannot be used": **ARC-131 / ARC-130**.

What the companion's audit may still legitimately add, and this intake deliberately did not attempt:
- (i) the inventory and causal-connectivity map (audit steps 1-2), an evidence artefact rather than a claim;
- (ii) a catalogue of experimenter-imposed regimes (step 3). If that catalogue reveals a regime choice with no owner in the list above, that is the only place a new claim should arise;
- (iii) the A1-ordering recommendation (step 8), a governance decision.

Its "no monolithic executive" constraint is already honoured by Q-111's wording.

---

## 7. Next steps

1. **Version routing for /governance (flagged, not decided).** All three are registered v3 / v3_v4 `substrate_conditional`, a deviation from the thought-intake default of v4, because the motivating failures are live V3 substrate. The recommended order follows the thought:
   - (a) the freeze-lock confirmer (already chipped: `chip-20260926-pag-freeze-lock-confirmer`);
   - (b) ARC-155's P1 information-content check on `z_harm_a` at the PAG gate;
   - (c) ARC-155 at the freeze gate;
   - (d) 1090a with its action-diversity precondition, which serves as Q-111's first leg;
   - ARC-156's freeze leg stays with MECH-280 / SD-037, and its N5 leg with the coupled-loop campaign's N5b.
2. **Design-review rule candidate (for /governance, not a claim).** Signal validity: a gain, cost or cap sweep on a control term may not be offered as evidence that its PRODUCER is valid. The producer's semantics must be validated first (GFLAG-0447 pattern; 1104 learning). The candidates are a clause on GOV-PATHVALID-1 or on the `/queue-experiment` design-review checklist. The ruling belongs to the user.
3. **Currency lag to fold at the next /governance cycle.** This comes through existing routes, and no new flag is raised: MECH-279 lacks the 1106/1107 lock; SD-032a/Q-041 lack 1067 and the mode-trace lock; MECH-046 lacks GFLAG-0556/0557.
4. **Literature (before hardening, not a prerequisite for registration).**
   - Divisive normalisation vs habituation for ARC-155 (Carandini & Heeger 2012 is on file; adaptation that preserves discrimination needs a pull).
   - Tonic-immobility termination and interoceptive override for ARC-156's cross-regime form (the MECH-280 anchors cover freeze only).
   - Per `feedback_lit_exp_decoupled`, none of this raises confidence.
5. **Architecture stub** `docs/architecture/endogenous_operating_point_regulation.md` to be written at registration, with a one-line cross-link from `persistent_process_termination_taxonomy.md` (ARC-156 next to MECH-497).
6. **Do not interrupt the coupled-loop campaign.** Nothing here should be queued, built or chipped into the orchestrator's live lane. The companion's audit stays deferred.
7. Raw thought marked `Status: processed`, `Claims registered: ARC-155, ARC-156, Q-111` (done at registration).

## 8. Digestion drafts

`what_would_answer` drafts and dispositions for ARC-155..Q-111 were produced this pass, NOT applied. They go in `evidence/planning/thought_digestion_staged_2026-09-26_thought_intake_batch.md` (section "endogenous operating point"), which lands in the same commit as this intake. Summary:
- ARC-155: (a) testable now in V3 at the PAG freeze gate, gated on the confirmer and on P1; it falls back to (c) if P1 fails for `z_harm_a`.
- ARC-156: (b) derivational core. Its empirical freeze leg is owned by MECH-280, which is (c) substrate_ceiling.
- Q-111: (f) defer until the ARC-155/ARC-156 corrections exist.
