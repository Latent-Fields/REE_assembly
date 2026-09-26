# Thought-digestion staging -- 2026-09-26 thought-intake batch

**What this is.** Draft `what_would_answer` texts and recommended dispositions for the six candidate
claims registered on 2026-09-26 by session `thought-intake-20260926` from two raw thoughts:
`docs/thoughts/2026-09-26_endogenous_operating_point_regulation_and_regime_coordination.md`
(ARC-155, ARC-156, Q-111) and `docs/thoughts/2026-09-25_minimal_developmental_prior_problem.md`
(Q-112, ARC-157, MECH-597). They were drafted by read-only research agents during ingestion and are
reviewed with the user by `/thought-digestion` in the same session. Each section below records its
review outcome once decided. Provisional drafting ids were OP-1..3 / DP-1..3; the mapping is
OP-1=ARC-155, OP-2=ARC-156, OP-3=Q-111, DP-1=Q-112, DP-2=ARC-157, DP-3=MECH-597.

**Governance flags surfaced while drafting (for /governance; none applied here):**
- ARC-074: `evidence_quality_note` owed since GFLAG-0504 deferred it "to the W2a build" (W2a landed
  2026-09-25T19:45Z); its Garcia-Guzman 2026 gloss ("pre-reward Hebbian phase") may mis-describe the paper.
- MECH-461: WWA calls the primitive-basis half "untested"; the 2026-09-25 babbling probe is partial D1
  evidence on it (action coverage, not competence).
- Currency lag from today's confirmed autopsies: MECH-279 lacks the 1106/1107 lock; SD-032a / Q-041 lack
  1067 and the mode-trace one-switch lock; MECH-046 lacks GFLAG-0556/0557.
- Design-review rule candidate (signal validity): a gain/cost/cap sweep on a control term may not be offered
  as evidence that its producer is valid (GFLAG-0447 pattern; 1104 learning). Candidate homes: a clause on
  GOV-PATHVALID-1 or the /queue-experiment review checklist. User's call.
- D1 and D2 have no registered INV (`five_axioms_foundations.md` "pending INV"); Q-112 leg (c) leans on them.
- coupled_loop_repair_campaign_plan.md row N2 still reads "queued V3-EXQ-1108 ... await verdict"; 1108 ran
  and its autopsy is confirmed (orchestrator-owned row; not edited here).

---

# Digestion drafts -- endogenous operating point (ARC-155..Q-111)

**For merge into:** `evidence/planning/thought_digestion_staged_2026-09-26_thought_intake_batch.md` (section "endogenous operating point")
**Intake:** `evidence/planning/thought_intake_2026-09-26_endogenous_operating_point_regulation_and_regime_coordination.md`
**Status:** DRAFTED, NOT APPLIED. `/thought-digestion` reviews these and `/governance` routes them. Provisional ids are replaced by real ids at registration.
**Endogeneity rule (from the thought and its companion):** every mechanism arm below reads only signals the organism itself has. Condition labels (shift/no-shift, hazard-moved/stayed, checkpoint id) are used ONLY by the experimenter for post-hoc scoring and are never visible to the agent. Oracle arms are marked as oracle positive controls (GOV-INTERVENE-1) and are ceilings, not candidate mechanisms.

---

## ARC-155 -- scale-relative control operating points

```
what_would_answer: |
  NON-DEGENERACY PRECONDITIONS (a null under any unmet one is uninterpretable, not evidence against):
    P1. INFORMATION CONTENT. The controlled channel carries condition-relevant information at EVERY
        checkpoint tested: e.g. for the PAG gate, raw ||z_harm_a|| separates hazard-adjacent (d<=1) from far
        (d>=2) states at d' >= 0.5 at each checkpoint. V3-EXQ-1107 recorded ||z_harm_a|| IDENTICAL on all 90
        eval ticks, and cea_onset_input_reprobe_20260925.md (GFLAG-0557) found relative gates on z_harm_a below
        their own floor, so P1 may be UNMET for z_harm_a after training. If it is unmet, the channel has a
        producer/validity problem, not an operating-point problem; move the test to a channel with validated
        content and do not score ARC-155 on it.
    P2. SCALE DRIFT. The channel's own running scale (median |x| over non-reset ticks) differs by >= 3x across
        the sampled checkpoints OR across seeds (measured magnitudes: 1107 2.8-4.2 vs theta 0.8; mode trace
        0.14-0.20 untrained vs 12-17 after the harm_accum aux; 1108 norm x10.5-12 within a lifetime). With no
        drift, a fixed and an adaptive operating point are equivalent by construction.
    P3. REACH. Either the regime occupancy itself is the DV, or the consumer's output varies the executed
        action (the 1090 action-diversity lesson).
    P4. HYGIENE. Post-STAY-fix code (GFLAG-0508). Near-reset ticks excluded, or the reset-init EMA fix ON
        (GFLAG-0559). The freeze-lock confirmer (chip-20260926-pag-freeze-lock-confirmer) has reported.

  DESIGN (first test site: MECH-279 PAG freeze gate; >= 3 training checkpoints x >= 5 seeds, same curriculum):
    A  shipped absolute operating point (theta_freeze 0.8).
    B  operating point denominated on an endogenous slow running scale estimate of the SAME signal
       (e.g. theta_eff = k x running high-quantile of the organism's own ||z_harm_a|| history, slow timescale,
       k fixed ONCE on checkpoint 1 of a calibration seed not scored). No condition labels.
    C  ORACLE ceiling: absolute theta hand-set per checkpoint from that checkpoint's distribution
       (GOV-INTERVENE-1 oracle positive control; not a candidate mechanism).
    D  COMPETING ACCOUNT: absolute theta, with the PRODUCER's scale anchored (a magnitude-anchored encoder
       objective, or harm_accum aux off). This tests whether consumer-side denomination is needed at all.
  DVs, scored post hoc by the experimenter from logged positions:
    (i)   occupancy: fraction of non-reset ticks in the regime, per checkpoint x seed; pre-registered band
          [0.02, 0.60] (neither never nor always).
    (ii)  discrimination: occupancy(hazard-adjacent) - occupancy(far) -- preserves absolute-danger meaning.
    (iii) seed dispersion of occupancy at each checkpoint.

  CONFIRMING: With P1-P4 met, B keeps occupancy inside the band on >= 4/5 seeds at EVERY checkpoint where A
  leaves it (pinned at ~0 or ~1). B's discrimination (ii) is >= 70% of C's at each checkpoint and above A's.
  B's advantage vanishes under a content-shuffled channel control (time-permuted ||z_harm_a|| fed to the
  gate): normalising an uninformative signal must NOT look like success.

  FALSIFYING (any one):
    (F1) With P2 met, A stays inside the band with discrimination at every checkpoint and seed (fixed raw
         points are stable after all).
    (F2) B stabilises occupancy only by erasing discrimination -- (ii) ~ 0, i.e. it habituates chronic
         danger into baseline.
    (F3) NARROWING, not demotion: D matches B on (i)-(iii). The defect is producer scale, and ARC-155 narrows
         to an encoder-anchoring claim.

  NOTE: the 1067 autopsy's warning applies. Do not score gradedness of a DISCRETE register (SD-032a is
  discrete by design); score occupancy and discrimination.
```

**Disposition: (a) testable now in V3**, but sequenced after the freeze-lock confirmer and a P1 measurement on `z_harm_a` at the checkpoints. If P1 fails, ARC-155 becomes **(c) substrate_conditional** on a channel with validated content: the raw hazard-proximity scalar GFLAG-0557 names is not exposed to the agent.
**Justification:** The test site (MECH-279), the drift (1107/1108) and the competing producer-anchoring arm (D) all exist in V3 today. Arm B is a small default-OFF change at one gate. The only live risk is that the channel no longer carries information (1107 constancy), and P1 turns that risk into a gate rather than a false negative.

---

## ARC-156 -- regime-surviving termination evidence

```
what_would_answer: |
  DERIVATIONAL CORE (no experiment needed): if the environment state that the exit condition depends on
  does not change without the agent's action, and the exit condition reads only observations whose change
  requires actions the regime removes, then the regime is an absorbing state. V3-EXQ-1106 is the measured
  instance: 0 release-source events while frozen on 3/3 seeds, predicted in writing by the build doc.
  The empirical claim is that REE's strong regimes need, AND benefit from, a source that survives the regime.

  NON-DEGENERACY PRECONDITIONS:
    P1. LEGITIMATE ENTRY. The regime is entered condition-sensitively, not by miscalibration: freeze entry
        rate is higher hazard-adjacent than far. The 1107 tick-1 lock fails P1. Apply the ARC-155 correction or
        the confirmer's recalibration first, otherwise "release" is only undoing a bad entry.
    P2. SUPPRESSION MEASURED. The candidate regime-SUPPRESSED release inputs are near-silent in-regime
        (e.g. MECH-287 option-B source events in-regime vs out-of-regime; 1106: 0 vs >0).
    P3. ECOLOGY WITH BOTH OUTCOMES. Episodes where termination is appropriate (the hazard departs or decays
        independently of the agent) and episodes where continuation is appropriate (the hazard stays). The
        hazard dynamics are agent-independent and never visible as a label.
    P4. A SURVIVING SOURCE EXISTS IN SUBSTRATE. Candidates: SD-012 drive_level (energy depletes while
        frozen); time-in-regime; MECH-482 epistemic_deficit; exteroceptive change sensed without moving
        (the z_harm_s / hazard field when the hazard itself moves). MECH-280, the registered freeze instance,
        is UNBUILT (substrate_ceiling; SD-037 override never built, GFLAG-0506), so P4 for the freeze leg
        currently requires a build decision owned by MECH-280.

  DESIGN (freeze leg; >= 5 seeds):
    A  exit reads only regime-suppressed evidence (the shipped MECH-279 exit and/or MECH-287 option B).
    B  A + one regime-surviving endogenous input (interoceptive drive or exteroceptive hazard change) in the
       exit condition.
    C  condition-blind terminator: fixed max duration (pag_max_freeze_duration), with its mean duration
       matched to B's.
    D  no release.
  DVs: termination appropriateness = P(terminate | hazard departed) - P(terminate | hazard stayed) within
  a window. Time-to-terminate. Post-release harm.

  CONFIRMING: A ~ D (both lock, or both terminate at chance). B's appropriateness exceeds C's by a
  pre-registered margin on >= 4/5 seeds. Ablating B's surviving input returns A's behaviour.

  FALSIFYING:
    (F1) A terminates appropriately from regime-generated signals alone -- the premise that this regime
         starves its own exit evidence is false.
    (F2) B's appropriateness is no better than C's -- the surviving input adds duration, not information,
         and termination here is a timer question.
    (F3) B terminates only by being condition-blind.

  SECOND LEG (N5, owned by the coupled-loop campaign, not queued from here): the N5b clamped-pair test of an
  active-probing detector vs on-policy surprise. The same logic applies: the probe is the regime-surviving
  source, and it must separate shift from no-shift where on-policy surprise does not.
```

**Disposition: (b) derivational** for the structural core. The empirical freeze leg is owned by MECH-279/MECH-280 and is **(c) substrate_ceiling** through MECH-280's unbuilt override. The N5 leg belongs to the coupled-loop campaign.
**Justification:** The absorbing-state argument follows from the exit condition's structure. 1106 already confirmed the prediction in the one regime that has been measured. What is not settled is whether a surviving source terminates appropriately, and that needs a source that does not yet exist for freeze. The claim must not reopen MECH-287b (option A stands, rec-20260926-78ecb89a).

---

## Q-111 -- controller composition after correction

```
what_would_answer: |
  NON-DEGENERACY PRECONDITIONS:
    P1. Each controller in a tested pair is individually validated on its own terms (for the MECH-449
        veto: 1090's C1/C2/C4, fires / calibrated / silent on the untrained-head control).
    P2. ARC-155 and ARC-156 corrections are in place for each controller in the pair. Otherwise interference
        cannot be told apart from miscalibration or a self-locking regime.
    P3. Executed action varies on the evaluated agent: the modal action share is below a pre-registered
        ceiling (the 1090 action-diversity precondition). Otherwise no controller can show a consequence.
    P4. The ecology co-activates both controllers' domains on a pre-registered minimum count of ticks.

  DESIGN (pairwise composition; first pair freeze x veto, then threat-mode x plasticity/repair, then
  stuckness-exploration (SD-061/MECH-527) x commitment (BetaGate)):
    arms: controller X alone / Y alone / X+Y / X+Y with a distributed reciprocal authority term keyed on the
    OTHER controller's own endogenous state (e.g. veto No-Go pressure on the freeze no-op class when the
    veto fires; or precision attenuation of the dominant controller while the other's evidence is pending).
    No central module, and no condition labels.
  DV: each controller's retained behavioural consequence in composition relative to alone, i.e. ARC-130
  committed throughput and ecological consequence (for the veto: realised-harm change attributable to vetoed
  candidates not executing).

  CONFIRMING (an extra principle is needed): with P1-P4 met, at least one pair in which Y retains < 50% of
  its isolated consequence because X removes its action or information substrate. The reciprocal term
  restores >= 50% of that loss without reducing X's own consequence by more than a pre-registered margin.

  FALSIFYING (no extra principle; Q-111 answers "no"): with P1-P4 met, every tested controller retains
  >= 80% of its isolated consequence in every tested pair. Per-controller correction is then sufficient.

  NOTE: The first leg needs no new substrate. It is a re-read of the already-routed V3-EXQ-1090a (MECH-449
  with the action-diversity precondition), run after the freeze-lock fix.
```

**Disposition: (f) defer** until the freeze-lock confirmer and an ARC-155/ARC-156 correction exist for at least one controller pair. 1090a is its natural first leg.
**Justification:** P2 and P3 are unmet today: freeze collapses the action space in the very pair that motivates the question (1090: action 0 on 3,000/3,000 ticks). Measuring interference now would confound it with the miscalibration and self-lock that ARC-155 and ARC-156 address.


---

## Thought-digestion staging: minimal developmental prior problem (Q-112, ARC-157, MECH-597)

**What this is.** These are draft `what_would_answer` texts and recommended dispositions. They were produced in the same drafting pass as the Stage 2 intake `evidence/planning/thought_intake_2026-09-25_minimal_developmental_prior_problem.md`. The provisional ids Q-112..MECH-597 are mapped to real ids at write time. **Nothing here is applied.** They are staged for `/thought-digestion` review. The target file is `evidence/planning/thought_digestion_staged_2026-09-26_thought_intake_batch.md`, as the orchestrator's batch file.

**Premises re-measured for these drafts (2026-09-26):**
- `StructuredBabbler` is on ree-v3 main (`2ea0e3c`) and default-OFF.
- `WakingTrainer` is on main; its E2WorldMember and retained buffer are on `integration/coupled-loop-repair`.
- There is no separable self-action contingency-bias lever. E2's world head is action-conditioned by construction (`e2_fast.py` `world_action_encoder`).
- `ree_core` has zero ACh / MECH-398 / MECH-207 hits (N5 P1).
- V3-EXQ-1108 ran at 2026-09-26T10:02Z (FAIL); its autopsy was CONFIRMED later the same day (verdict NEITHER, non_contributory) -- see MECH-597's notes.

---

### Q-112 (open_question): the minimal developmental prior set

**Group context:**
- INV-073: the exploration epoch is necessary.
- ARC-074: Phase-0 epoch.
- MECH-461: innate primitive basis plus engagement drive.
- ARC-138: regulation-first.
- INV-095 / SD-012: valued self-state.
- GOV-INSERT-1: the derivational layer's insertion route.
- Q-108: the minimal-working-intelligence event, which is a different question.

**Draft `what_would_answer`:**

```
NON-DEGENERACY PRECONDITIONS (a null or a "removal costs nothing" reading under any unmet one is
uninterpretable, not evidence):
  P1. FULL-SET DEVELOPS. An over-provisioned general candidate set must first produce development on
      its own. The pre-registered developmental DVs must clear their bars:
        - E2 action discrimination (the disc4_h1 executed-closest metric, bar >= ~0.47, with fidelity
          k reported), retained under later on-policy training;
        - a closed-loop behavioural readout (A1-type).
      If the full set does not develop, every ablation is floored and says nothing about necessity.
  P2. EACH CANDIDATE IS A SEPARABLE LEVER. Each candidate must be a default-OFF, OFF-bit-identical
      switch that removes that element ONLY, and never enabling architecture with it.
      UNMET today for contingency sensitivity: E2's world head is action-conditioned by
      construction, so "remove contingency bias" currently also removes the action input.
      UNMET for viability grounding: there is no arm that removes valued self-state while keeping
      exploration and modelling.
      MET for structured action (StructuredBabbler) and for retention (the W3 retained buffer, on
      the integration branch).
  P3. >= 2 PREDECLARED WORLD FAMILIES (GOV-ECOL-1). Seeds alone cannot answer the generality leg.
  P4. DEVELOPMENTAL DVs, not endpoint reward (sec 15 of the source thought):
        - action-space coverage, and action->consequence MI;
        - world-model action discrimination;
        - persistence of developmental knowledge;
        - PE and PE reduction;
        - survival duration;
        - time to first model-based behaviour;
        - recovery after change;
        - E3 dependence on learned causal information.
      Each emergent capacity must also have a causal-path check (GOV-PATHVALID-1).

CONFIRMING (per leg):
  (a) NECESSITY. Each candidate necessity produces its OWN predicted failure when removed from the
      developing full set, and an accelerator ablation only slows or destabilises development.
      Predicted failures:
        - no structured endogenous action -> E2 discrimination stays at the on-policy baseline;
        - no retention -> the developmental gain decays under on-policy training;
        - no valued self-state -> no stable preservation or goal behaviour;
        - no contingency bias -> agency/controllability estimates fail to form.
      Restoring the removed element repairs development WITHOUT environment-specific content, i.e.
      the restored element is identical across world families.
  (b) GENERALITY. The same small set bootstraps development in both world families, with no
      environment-specific scaffold admitted. Orienting and curiosity-like behaviour emerge without an
      explicit orienting rule.
  (c) AXIOM MAPPING. Removing viability grounding (the A2/D1 implementation) abolishes stable
      preservation / goal behaviour, and no other source supplies it. This is consistent with A2/D1
      being developmental prerequisites (not proof of the axioms).

FALSIFYING (any one answers the question AGAINST the candidate as a necessity):
  - A candidate necessity is removed with no developmental cost across BOTH world families. It was
    an accelerator or redundant: reclassify under ARC-157.
  - Unstructured or native behaviour yields equally informative world models once other training
    defects are corrected. That would contradict the 09-25 D1 result at larger scale.
  - A candidate can only be "restored" by environment-specific content. It is then an ecological
    scaffold, not a general prior (ARC-157).
  - Leg (c): preservation / goal behaviour arises without any valued self-state or equivalent. A2's
    implementation then requires reconsideration, and the finding is routed to the derivational
    layer with GOV-INSERT-1 / GOV-HOTHER-1.

EXISTING EVIDENCE (bears on leg (a) only, D1, structured-action + retention elements):
  - babbling_e2_action_coverage_probe_20260925.md: native Phase-0 policy S FAIL 1/5, DR FAIL 0/5.
    The structured L2 source was sufficient pre-post 5/5, with retained replay 5/5 vs one-off 2/5
    (secondary, descriptive).
  - V3-EXQ-1108: pending review.
  Nothing yet on contingency, viability or generality.

SUBSTRATE / INSTRUMENT REQUIREMENT:
  - a separable contingency-bias lever;
  - a viability-grounding ablation arm;
  - a second declared world family;
  - an integrated closed-loop acceptance harness (campaign A1 is the nearest; it is HELD).
Consumer / boundary: developmental trajectory, not an adult-competence endpoint.
Existing ownership: INV-073, ARC-074, MECH-461, ARC-157, MECH-597, coupled_loop_repair_campaign_plan.md
(W2a, W3, A1).
```

**Recommended disposition: (c) substrate-blocked, `epistemic_category: substrate_conditional`.**
- Two of the four legs lack a lever: contingency and viability. The generality leg needs a second world family.
- The structured-action and retention legs are V3-expressible now, and are carried by MECH-597 and the coupled campaign. They are not a reason to route the whole question to V3.
- Do NOT queue anything from this entry.

---

### ARC-157 (architectural_commitment): two-axis developmental-prior classification, least-environment-specific first

**Group context:**
- SD-090: functional-role classes, with no generality axis.
- GOV-ECOL-1: seeds vs world families.
- GOV-INSERT-1: the derivational-layer sibling.
- GOV-MATCHAUX-1: scaffold-removal admissibility.
- INV-101: environment-conditional crystallisation target.
- SD-032c / MECH-104 / ARC-046: the survival-interrupt mechanism the generality clause constrains.

**Draft `what_would_answer`:**

```
NON-DEGENERACY PRECONDITIONS:
  P1. At least TWO predeclared world families that differ along a stated ecological axis
      (GOV-ECOL-1). Without them "environment-general" cannot be measured, and the generality axis is
      vacuous by construction.
  P2. An ablation harness where each classified mechanism is a separable default-OFF lever (shared
      with Q-112 P2).
  P3. A pre-registered classification rule, fixed BEFORE results:
        - necessary = removal produces a specific predicted developmental failure;
        - accelerator = removal only changes rate, stability or variance;
        - general = its necessity/acceleration status is the same across both world families;
        - environment-specific = its status changes across families, or its content names an
          environment feature.
      Without the rule fixed first, the classification is post hoc labelling.

CONFIRMING:
  (i) The axes are independent. At least one mechanism lands in each of two OFF-DIAGONAL cells (e.g.
      a general accelerator such as retained replay or learning-progress curiosity, AND a mechanism
      whose necessity holds in one world family but not the other).
  (ii) The admission order does work. In a world family where the general set fails to develop, an
      environment-specific scaffold restores development, and that scaffold's necessity vanishes in
      the other family.
  (iii) The content-generality clause holds for the survival interrupt. An interrupt keyed to
      valued-self-state deterioration protects development in both families, while a feature-keyed
      interrupt protects it only in the family whose feature it names.

FALSIFYING:
  - The axes COLLAPSE. Every mechanism classifies identically across both world families (the
    generality axis carries no information), OR necessity and generality are perfectly confounded
    (every necessity is general and every accelerator is specific, or the reverse). Then one axis
    suffices and the two-axis commitment is wrong.
  - The admission order is VACUOUS. No general set ever develops without an environment-specific
    scaffold in any world family, so "least-specific first" never selects anything.
  - A feature-keyed survival interrupt transfers as well as a self-state-keyed one across families.
    The content-generality constraint is then unnecessary.

SUBSTRATE / INSTRUMENT REQUIREMENT:
  - a second world family, declared along an ecological axis;
  - the Q-112 ablation levers;
  - DEV-NEED register columns for necessity/accelerator and general/specific.
    That is a doc deliverable, and a prerequisite for (ii), because otherwise nothing records which
    scaffolds were admitted.
Existing ownership: SD-090, GOV-ECOL-1, GOV-INSERT-1, developmental_needs_register.md.
```

**Recommended disposition: (c) substrate-blocked, `epistemic_category: substrate_conditional`.**
- The claim is only measurable with world-family replication and a full ablation harness, and neither exists for developmental priors.
- It has design value NOW. It is the classification and admission rule to read before anyone adds an environment-specific prior to rescue a failed development run.
- If /governance instead treats the admission-order half as a governance rule, re-dispose that half as (b) derivational / governance_rule, with a "not an empirical pass/fail falsifier" WWA in the GOV-INSERT-1 shape.

---

### MECH-597 (mechanism_hypothesis): retained developmental replay is needed for durability

**Group context:**
- ARC-074: one-off epoch.
- INV-073: early deficits permanent, the opposite direction.
- MECH-334: plasticity-reduction closure on the policy plane.
- MECH-165: sleep-replay diversity.
- MECH-207 / MECH-398: the unfreeze half, v4, excluded.
- Campaign W3 / N2 / N5.

**Draft `what_would_answer`:**

```
NON-DEGENERACY PRECONDITIONS (a null under any unmet one is not evidence against):
  P1. A GAIN TO RETAIN. The post-developmental head must first beat the on-policy baseline head (B0)
      by the pre-registered margin on the held-out uniform-random test set:
        - disc4_h1, margin max(0.05, SD of B0 across seeds);
        - the retention ratio (post - B0)/(pre - B0) must have a positive denominator.
      The 09-25 probe shows why this matters: the NATIVE Phase-0 source had no gain on 4/5 seeds,
      so R was CANNOT_DETERMINE. The source must be the structured (L2 / StructuredBabbler) form.
  P2. NARROWER LATER EXPERIENCE. The on-policy phase's measured action-class entropy is below the
      developmental source's. Its update exposure is at least 3x the developmental training
      exposure, so forgetting pressure is real.
  P3. INFORMATION, NOT REGULARISATION. A label-shuffled retained-replay twin (fixed class
      permutation, class marginals kept) is run. It must FAIL the bar; otherwise any retention is a
      replay-as-regulariser effect.
  P4. READ-PATH REGIME DECLARED. State whether the encoder is frozen or trained through the read
      path (and whether replay stores raw observations re-encoded, or stored latents). The claim is
      asserted for the frozen regime. The trained regime is the open generalisation.

CONFIRMING: At matched on-policy exposure and matched seeds (>= 5, fresh):
  - the retained-replay arm (25% of world-head batches from the protected developmental set) keeps
    retention >= 0.5 AND the discrimination bar on >= 4/5 seeds;
  - the one-off arm fails retention on >= 2/5;
  - the shuffled twin fails the bar.
Strengthened by a monotone DOSE response over the retained fraction {0, 10, 25, 50%}.

FALSIFYING (any one):
  - the one-off arm retains >= 0.5 on >= 4/5 seeds at matched exposure (rehearsal is not needed);
  - the retained-replay arm fails to retain;
  - the shuffled twin retains as well as the real replay (it is a regulariser, not developmental
    information).
If retention holds frozen but not with a trained encoder, NARROW the claim to the frozen read path
rather than count it against the claim.

EXISTING EVIDENCE (D1; not tagged to this id; /governance decides tagging):
  - Babbling probe secondary readout (descriptive, pre-registered as secondary): L2R 5/5 (1.31-1.53)
    vs one-off L2 2/5.
  - Campaign W3 member gate (b): 5/5 (0.96-1.71), frozen encoder; shuffled twin (a) 0/5.
  - V3-EXQ-1108 (FAIL, pending review):
      - frozen arm (a) 4/5, (b) 5/5;
      - re-encode arm with encoder training (a) 3/5, (e) 1/5;
      - stored-latent arm 0/5.
    This fits the frozen-regime scope. The trained-encoder generalisation is not supported at that
    dose. Adjudication belongs to its autopsy.

SUBSTRATE / INSTRUMENT REQUIREMENT:
  - Present: StructuredBabbler (main, default-OFF); E2WorldMember retained buffer
    (integration/coupled-loop-repair); probe harness probes/babble + probes/w3 + probes/n2.
  - Missing for the dose leg: a pre-registered replay-fraction sweep. That is one queue entry via
    /queue-experiment, not a build.
Consumer / boundary: the E2 world head's action discrimination. Whether retained discrimination
reaches E3 (D2) or behaviour (D3) is out of this claim's scope: see campaign W4 and A1.
```

**Recommended disposition: (a) testable now in V3, `epistemic_category: standard`.**
- The substrate exists (generator on main, member on the integration branch), and most of the answer is already in D1 evidence.
- What remains is a /governance routing decision on v3, whether to tag the W3 gate / V3-EXQ-1108 frozen arm to this id, and optionally a replay-fraction dose sweep.
- Do NOT re-open the unfreeze half here. W2b / N5 own it, and it is blocked.
