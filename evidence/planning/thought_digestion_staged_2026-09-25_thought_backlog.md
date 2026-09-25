# STAGED (not applied): `/thought-digestion` drafts for the 17 claims registered 2026-09-25 by thought-backlog-20260925

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml.**

- **Session:** `thought-backlog-20260925` (Mac, main checkout, interactive). Claims registered in REE_assembly `09fa012a89`.
- **Scope:** MECH-588..595, ARC-151..154, Q-109, Q-110, GOV-FRONTIER-1, GOV-INSERT-1, GOV-DEFEAT-1, plus a design refinement to MECH-453 `what_would_answer`. (The 33 September-registered claims this session also drafted were digested and applied by the parallel session `thought-digest-registry-backlog-20260925`, REE_assembly `d95f7e37be`; this session only cross-checked them and raised GFLAG-0538..0553.)
- **Mode:** grouped. N1 = MECH-588/589; N2 = GOV-FRONTIER-1/INSERT-1/DEFEAT-1; N3 = MECH-590/591/595, Q-110; H1 = the eight plasticity/lateralisation claims (drafted during registration, stripped from the registration commit per the ingestion skill).
- **How to use:** the applying session copies each approved `what_would_answer` verbatim, re-reading each claim block fresh first, then runs build_claims_json.py and commits pathspec-limited.

## Governance flags raised by this session (read first)

GFLAG-0538 (IMPL-022/SD-063 stale_note) · 0539 (ARC-137 stale_note) · 0540 (MECH-533 routing) · 0541 (MECH-083 monotonic falsifier) · 0542 (MECH-111 dead location) · 0543 (MECH-588 V3 routing) · 0544 (MECH-453/ARC-154/ARC-153 routing + class) · 0545 (MECH-100 GOV-MATCHAUX-1 review) · 0546 (INV-011 audit scope) · 0547 (MECH-544 stored vs reconstructed source) · 0548 (MECH-365 stale note) · 0549 (MECH-571 Meltzoff mis-tag) · 0550 (INV-064 misdescribed) · 0551 (GOV-GRAN-1/SKILL-1/SUBPATH-1 gaps) · 0552 (ARC-107/SD-071 world-family/JURIS) · 0553 (ARC-140 phase/edge).

Open author question (N3): does Q-110's "bond" mean caregiver AVAILABILITY or internalised LOVEABILITY (INV-082)?

---

# Group N1 -- MECH-588 / MECH-589

# N1 digest -- MECH-588 + MECH-589 (monostrategy etiology typology)

Session thought-backlog-20260925, grouped mode, drafter N1. READ-ONLY draft; the orchestrator is the sole writer.
Both claims registered 2026-09-25 in REE_assembly 09fa012a899 (committed 12:05:57 +0100) from
docs/thoughts/2026-09-24_dynamic_coordination_repertoire_monostrategy.md.

## Currency re-measured (2026-09-25, before drafting)

1. **Both claims present** in claims.yaml. Neither has `what_would_answer`, `live_status` or `digestion_note` yet.
   No reverse-deps except MECH-589 -> MECH-588.
2. **GFLAG-0487 and GFLAG-0488 are still `open`.** MECH-588's notes name them as the owners of the Type-A root.
   **Two later flags the notes do not cite, both open:**
   - **GFLAG-0490** (a369f411ff8, `action_decoder_training_causal_probe_20260925.md`, raised 2026-09-24T23:41Z):
     training `action_object_decoder` ALONE does not repair proposal generation. P FAIL and C FAIL on 5 seeds.
     An honest inverse (held-out accuracy 1.000) moves the pool no more than a shuffled decoder.
     The proposal edge is a CODEC with three coupled defects:
     (a) the decoder is untrained;
     (b) its unbounded raw output is used as the rollout's action vector;
     (c) iteration-0 `ao_std = 1` samples about 12x outside the encoder's image.
   - **GFLAG-0501** (user decisions 2026-09-25T06:15Z): fold GFLAG-0488/0490 into ONE coupled campaign
     (codec + E2 action coverage + grounded valuation + WakingTrainer ON). A decoder-only row is ruled out.
   So the Type-A repair that MECH-588's Stage 0 waits on is now the coupled campaign, not "the decoder half of SD-080".
3. **GFLAG-0543 is already open on MECH-588** (promotion_review, raised by this session 11:09Z): "Confirm v3, or park at v4
   until Stage 0 passes". My recommendation below is an input to that flag. **Do not raise a duplicate.**
4. **Stage 0 is still RED. Nothing has landed since the audit:**
   - No Q-080 effort-layout run after V3-EXQ-731 (2026-07-09): corridor entry 0.333 < 0.5, 6 episodes.
   - Nothing Type A/B, Q-080-navigability or effort-corridor related is in `ree-v3/experiment_queue.json` (4 items).
     V3-EXQ-1104 is the SD-032b effort proxy, a different question.
   - No overlapping item in `manual_proposals.v1.json` or `experiment_proposals.v1.json`.
   - CURRENT_FRONT (generated 2026-09-25): at REEConfig defaults ree_core does no waking gradient learning (GFLAG-0491).
   - `2026-09-25 babbling_e2_action_coverage_probe` (0ac69c87446): native Phase-0 is near-monostrategy on 4/5 seeds.
     This is further Type-A-at-generation evidence, not Type B.
5. **V3-phase leak check:**
   - MECH-588 (v3): every `depends_on` target is v3 or has no phase set. INV-088 has no `implementation_phase`.
     The v4 neighbours (ARC-145, MECH-560, MECH-534, Q-106, MECH-589) sit in `related_claims`. **No leak.**
   - MECH-589 (v4) depends on MECH-588 (v3). A v4 -> v3 edge is not a leak.

## Group preamble

**Relationship.** MECH-588 and MECH-589 are one typology read in order:
- Type A: absence (generation / representation).
- Type B: access collapse. The alternative is represented, but only an ACCESS change re-exposes it.
- Type C: consensus over-stabilisation. The alternative is represented and routed, but a selective reciprocal coupling
  keeps pulling the joint system back to one coalition.

MECH-589 `depends_on` MECH-588 correctly: Types A and B must be excluded before a Type-C reading is admissible.

**Merge?** No. The two claims make different causal assertions, with different discriminating interventions:
- MECH-588 uses generation-side injection and an access-only change.
- MECH-589 uses a selective-coupling cut at matched magnitude.

Out-of-group merge pressure was checked and rejected:
- **MECH-589 vs MECH-578's falsifier (d) and INV-108 (iv).** Those are a BUILD PROHIBITION and a design CONSTRAINT.
  MECH-589 asserts a CAUSE of a phenotype, with rivals. The overlap is partial and the notes already distinguish it.
- **MECH-588 vs ARC-145.** ARC-145 is an interface-level architectural requirement. MECH-588 is the behavioural
  diagnostic over a strategy repertoire.

**Contradiction / tension found (flag, do not resolve):**
- MECH-588's title says a "routing / dynamic-coordination / phase remedy is licensed ONLY by a Type-B verdict".
- `monostrategy_etiology_typology.md` says "Only B and C can license a coordination remedy".
- The proposed V3/V4 revocation trigger says "a Type-B (MECH-588) or Type-C (MECH-589) verdict".

These are consistent only if the remedies are read narrowly:
- an ACCESS remedy (routing / phase / state-keyed gain) is licensed by B;
- a COUPLING / ESCAPE remedy (selective-coupling release, latch-release) is licensed by C;
- A licenses neither.

Proposed resolution for /governance: a one-clause wording edit to MECH-588's title, or a sentence in its notes.
Digestion does not apply it.

**Group-level finding 1: MECH-588's assay, as designed, cannot tell B from C.**
- The audit's stop result 5 (`monostrategy_type_a_vs_b_discrimination_20260924.md` section 4.5) declares
  "Type B is earned" when all of these hold:
  - S1 and S2 are high;
  - AF is low;
  - I2 shows S3-to-S5 authority is recoverable;
  - controls 1-3 fail.
  Only after that does it open the routing arms.
- A Type-C system produces the same pattern:
  - the alternative is represented and loses authority at a later stage;
  - injection does not rescue;
  - an I3 force-commit relapses after forcing ends, because the system relaxes back to the coalition.
- MECH-588's own title defines Type B as re-exposure "by a change of ACCESS alone, with no retraining and no new
  content". A Type-B verdict therefore needs the access-only rescue arm, not just the stop-5 pattern.
- Without that arm the stop-5 pattern is **"post-representation authority loss (B-or-C)"**. That is the entry state
  for MECH-589, not a Type-B verdict.

This is extraction, not invention: it reconciles the claim's own definition with the thought's "Discriminating
result" items 3-5 (stochastic routing does not rescue, endogenous state-dependent routing does, and the effect is
abolished by routing-state shuffle). It is written into MECH-588's CONFIRMING below. The audit doc's stop rule 5 wording
should be corrected by whoever authors the assay (see corrections).

In V3 the C branch is structurally unavailable at the dynamical level. MECH-578 P1/P2 are verified absent: there is no
reciprocal, per-direction-ablatable, live coupling. So in V3 a B-or-C state that an access-only change rescues reads as
B. A B-or-C state nothing rescues is an unclassified residual. Do not force it into B.

**Group-level finding 2: one shared discrimination ladder with MECH-587 and MECH-080 arm 3.**
Post-reversal perseveration / monostrategy is discriminated in this order:
1. injection rescues -> A (MECH-588);
2. an access-only change rescues -> B (MECH-588);
3. the selective-coupling cut releases the lock-in with competence preserved, and flattening / noise do not -> C (MECH-589);
4. the lock-in survives the cut -> single-system. Then MECH-587's rollout-to-policy coupling readout splits habit
   dominance (MECH-587: coupling lost) from the deep basin inside the rollout (MECH-080 arm 3: coupling intact).

Each claim should cross-reference the adjacent rung rather than re-derive it. Both drafts below do this. Recommended
reciprocal references (proposal only):
- MECH-587 has NO `related_claims`: add MECH-589 and MECH-588.
- MECH-080 carries a PENDING FOLD note (user 2026-09-25) for EXP-0818. Add MECH-589 as a second arm-3 rival there when
  that fold happens, not now.

**Shared falsifier across the group and ARC-145.**
- MECH-588's control 1 (static learned bridge rescues, so the V3 synaptic approximation suffices) is ARC-145's F2
  ("a static bridge between frozen endpoints restores the full behavioural phenotype") read at the repertoire level.
- The MECH-588 draft points at it. It does not import ARC-145 as a dependency, which keeps the phase boundary clean.
- A MECH-588 static-bridge rescue counts toward ARC-145's F2 ONLY at a locus that meets ARC-145's own precondition.

**Solos:** none. Both claims are grouped.

---

### MECH-588

**Recommended disposition: (c) substrate-blocked.** The discriminating assay is designed and pre-flighted, and its
injection arm has a native producer. But every non-degeneracy precondition is currently unmet:
- no P1+P5 ecology is in use;
- the competence gate fails (V3-EXQ-731: 0.333);
- there is no waking learner at defaults;
- the Type-A generation root is open under the GFLAG-0501 coupled campaign;
- the I2 hook is absent.

So a run today would be non-adjudicable (stop result 1) or would return the already-known Type-A reading.

**Recommended epistemic_category:** `substrate_conditional`, as registered. It is not `substrate_ceiling`: the Type-B
discrimination has never been exercised under non-degenerate conditions.

**Routing recommendation, input to GFLAG-0543 (the decision is /governance's): KEEP `implementation_phase: v3` /
`version_relevance: v3_v4`. Do not park it at v4.** Reasons:
1. Every blocker is V3-buildable and already owned:
   - the coupled campaign plus WakingTrainer (GFLAG-0501, user-decided);
   - the Q-080 block schedule is driver-side, with no substrate edit;
   - the I2 `set_injected_score_bias` hook is a small default-off `/implement-substrate` item;
   - the altered-ecology board swap is `complicated (buildable)`.
   Nothing it needs is v4.
2. MECH-588 is the GATE that decides whether the V3 synaptic approximation is insufficient. That is the V3/V4 boundary
   test itself. A boundary gate that can only run at v4 would be circular.
3. There is no V3-necessity leak to hide.

The honest state is "v3, substrate-blocked, gated on the coupled campaign plus Stage 0". Stage 0 (Q-080 navigability at
scale) is a `puzzle (known rules)` that `/queue-experiment` could author once the coupled campaign lands. Running it
before then would be dominated by the generation root (ING-A 6a). **No EXP- proposal is minted from this claim.**

```yaml
what_would_answer: |
  NON-DEGENERACY PRECONDITIONS (the audit's Stage 0 and instrument checks, evidence/planning/
  monostrategy_type_a_vs_b_discrimination_20260924.md sections 4.1-4.7; do not re-derive them. A null, OR a
  Type-A reading obtained under any unmet one, is non-adjudicable, not evidence either way):
    P1+P5 ECOLOGY. By construction, at least two strategies are each behaviourally useful AND a fixed strategy
        is measurably suboptimal (switching is required), with an evaluator-only usefulness oracle that is never
        fed to the agent. Nearest: the Q-080 two-corridor effort layout, with effort_benefit_asymmetry switched
        between episode blocks (0 -> 0.5), driver-side and read per step (causal_grid_world.py:896/:2968),
        oracle _effort_corridor_at. Altered ecology: the V3-EXQ-1014 pinned boards with a mid-run hazard swap
        (not built). world_rule_shift_* (action-map transposition, ree-v3 10e287a) is a native REVERSAL lever
        usable for post-reversal authority reads. It changes what an action does, not which route pays, so it
        does not satisfy P1 on its own. Status 2026-09-25: UNMET; no ecology in use satisfies P1 and P5 together.
    P0 COMPETENCE GATE. Block-A corridor entry >= 0.8 AND block-A authority fraction >= 0.6 on at least 6 of 8
        seeds. Otherwise the run is non-adjudicable: route to the competence floor (MECH-457) and draw no
        further seeds. Status: UNMET. V3-EXQ-731 corridor entry was 0.333 < 0.5 (6 episodes, untested at
        scale), and at REEConfig defaults ree_core does no waking gradient learning (CURRENT_FRONT, GFLAG-0491),
        so any competence is driver-supplied.
    P3/P4 GENERATION AND SCORING NOT DEGENERATE. Log the pool CLASS SHARE per decision state, not the class
        count. E3's score range must be non-flat relative to its magnitude: V3-EXQ-804's normalised range of
        0.00095 is P4 failing (MECH-439), not Type B. S3 is read by class-mean score AND by best-of-class after
        matched per-class subsampling, which removes the order-statistic bias that produced the V3-EXQ-1061
        31:1 artefact.
    S2 READ AT THE EVALUATOR INPUT. "Represented" means separable in the exact tensors E3 consumes (INV-105 rung 3):
        held-out linear AUC > 0.75, AND the E3-consumed channel values (benefit / energy / harm) differ between the
        useful and non-useful candidates. An external-probe decode is D1 and cannot support this claim
        (GOV-JURIS-1). Caution: E2's world head is currently action-blind. Only 2.3-3.1% of z_world's per-step
        displacement is action-explained (e2_rollout_divergence_and_proposal_state_dependence_20260924.md), so
        S2 is expected to FAIL on today's substrate. That is itself a Type-A (representation) reading, not a null.
    INSTRUMENT VALIDITY.
        - I2+ positive control (score clamp at 20x the per-state score SD) drives S5 to ~1; otherwise the pipeline
          is broken and the run is invalid.
        - I1c (injecting the mismatched, non-useful candidate at matched pool size) is not selected above its base
          rate; otherwise E3 is reading novelty or position, and the injection arm is invalid.
        - Content ablation (the useful candidate's E2 world_states deviation replaced by the pool mean) abolishes
          any rescue; otherwise the arm is using privileged position or a lookup and is invalid.
        - The I2 clamp needs a default-off set_injected_score_bias hook, which does not exist today (AMBER).
        - Force-commit (I3) must go THROUGH E3 and record_executed_action, never through an env-side override:
          the residue write is commitment-gated (e3_selector.py:4690-4697).
    POWER. n = 8 seeds, fixed in advance. The per-seed SD of the authority fraction has never been measured
        (0.15 was an assumption), so Stage 0 measures it and re-sizes n before any intervention arm opens.

  CONFIRMING (Type B occurs in REE, and it separates from Type A). With every precondition met, in post-reversal
  block B, on >= 7/8 seeds (paired one-sided Wilcoxon at alpha 0.05 AND |delta AF| >= 0.20), all of the following:
    (i)   Under N0, S1 and S2 are high but the authority fraction AF = P(S5 | S1 and S2) is low.
    (ii)  I1 generation-side injection of the useful candidate, at matched pool size, does NOT rescue AF, and the
          injected candidate loses authority at a NAMED later stage (T23, T34 or T45). The I2 dose-response
          shows S3 is recoverable while S4/S5 lag.
    (iii) The static learned bridge, the existing default-off diversity pressure
          (support_preserving_per_class_quota, use_f_eligibility_demotion, use_selection_entropy_floor,
          score_diversity) and matched state-independent random routing ALL fail to rescue.
    (iv)  Because the claim defines Type B as re-exposure by a change of ACCESS ALONE, a non-oracle, state-keyed
          access change with no retraining and no new content rescues AF. Try the minimal first: conflict-graded
          eligibility, then state-keyed gain on an existing channel, then latch-release, then a learned router.
          The rescue must be abolished by routing-state shuffle and must preserve block-A competence.
    (v)   The result replicates in at least one altered ecology before it is used for any promotion.
  Pattern (i)-(iii) WITHOUT (iv) is recorded as "post-representation authority loss (B-or-C)". That is the entry
  state for MECH-589, not a Type-B verdict (the audit's stop result 5 must be read this way).

  FALSIFYING (occurrence falsifier, from the title). With every precondition met, in a P1+P5 ecology on n = 8 seeds
  plus one altered ecology, EVERY monostrategic seed is rescued either by generation-side injection (Type A at
  generation: N0 S1 < 0.2 AND I1 delta AF >= 0.20) or by the static learned bridge (Type A of the value read).
  Type B then does not occur in REE, the V3 synaptic approximation stands, and the V4 deferral of the
  routing / phase / coordination cluster is confirmed. For the admissibility consequence, seeds rescued by an
  existing diversity knob or by matched random routing count the same way: not Type B. A Stage-0 failure is NOT a
  falsification. It is non-adjudicable.

  ADMISSIBILITY LEG (a standing rule, not an empirical prediction). "A routing / dynamic-coordination / phase remedy
  is licensed only by a Type-B verdict ..." is not falsified by any outcome above. It is the gate that the proposed
  operational V3/V4 revocation trigger (monostrategy_etiology_typology.md, awaiting /governance ratification) would
  apply. An access remedy is licensed by B. A coupling / escape remedy is licensed by C (MECH-589). Neither is
  licensed by A.

  SHARED FALSIFIER. Control (iii)'s static-bridge rescue is ARC-145's F2 read at the repertoire level. A MECH-588
  static-bridge rescue counts toward ARC-145's F2 only at a locus that meets ARC-145's own precondition.

  CURRENT EVIDENCE (D1, with one weak D2 contrast; recorded, not scored; adjudicates nothing because P1/P5/P0 are
  unmet). The sharpest measured V3 monostrategy, the V3-EXQ-1061 regime, is GENERATION-STAGE Type A:
    - The pool is 31:1 or 30:2 in first-action class, and the majority class is identical at all 40 probe states
      within a seed (948d58cd3e4). This reproduces at world_dim 32 and is not caused by rollout depth (f300ebf64d6).
    - Training the action_object_decoder alone does not repair it. The proposal edge is a codec with three coupled
      defects (a369f411ff8, GFLAG-0490), and the repair is folded into the user-decided coupled campaign (GFLAG-0501).
    - No Type-B-shaped signal in the record (V3-EXQ-931, 654i/j, 947/949, 804, 567 seed 43, 1014) clears P1 + P5
      and the adversarial checks.

  SUBSTRATE / INSTRUMENT REQUIREMENT. Missing, and all V3-buildable:
    - the coupled campaign (codec + E2 action coverage + grounded valuation + WakingTrainer ON);
    - a navigable P1+P5 ecology meeting P0;
    - the default-off I2 score-bias hook;
    - the altered-ecology board swap.
  Present: the I1 injection producer (e2_fast.py rollout_with_world, agent.select_action) and the control knobs.
  Registration is not build authorisation. DO NOT build a routing, coordination, phase or ephaptic layer on the
  strength of this entry. DO NOT queue the assay before Stage 0 passes. Stage 0 is /queue-experiment's call after the
  coupled campaign lands.
  Disposition 2026-09-25: (c) substrate-blocked, substrate_conditional; implementation_phase v3 recommended to be
  retained (GFLAG-0543). No experiment proposed.
```

**Other field edits (proposed):**
- `related_claims`: add `MECH-457`, the competence-floor route for stop result 1. Optionally add `MECH-587`, the
  next-rung rival on the shared ladder.
- `notes`, currency correction (see below). No `depends_on` changes.

**Proposal JSON:** none (disposition c).

**Corrections and flags:**
- **FIX-AS-WE-GO (objective, stale note).** MECH-588's notes say "GFLAG-0487/0488 name the root (untrained
  action_object_decoder; SD-080 covers only the encoder half)". They also say Stage 0 comes "after the Q-080
  navigability puzzle and the GFLAG-0487/0488 Type-A repair". Both lines were already stale at registration, which
  post-dates a369f411ff8. Proposed appended sentence:
  > "Currency 2026-09-25: GFLAG-0490 (a369f411ff8) found decoder training ALONE does not repair proposal generation
  > (codec with three coupled defects); GFLAG-0501 (user decision 2026-09-25T06:15Z) folds the Type-A repair into one
  > coupled campaign (codec + E2 action coverage + grounded valuation + WakingTrainer ON). Stage 0 follows that
  > campaign."

  The same sentence belongs in `monostrategy_etiology_typology.md`'s MECH-588 "Current evidence" paragraph, which says
  "The Type-A root is owned by GFLAG-0487 / GFLAG-0488 ... and SD-080".
- **FIX-AS-WE-GO (audit doc wording, low priority).** In `monostrategy_type_a_vs_b_discrimination_20260924.md` section
  4.5, stop result 5 says "Type B is earned" before any access-only rescue arm has run. Annotate it as
  "B-or-C authority loss; Type B requires the access-only rescue (MECH-588 CONFIRMING (iv)); Type C is MECH-589". This
  corrects a design doc to match the registered claim definition, and resolves no judgement call.
- **GOVERNANCE (existing flag, do not duplicate): GFLAG-0543.** Input: keep v3, reasons above.
- **GOVERNANCE (wording tension; optional contested_disposition, or carry it into GFLAG-0543's review).** "Licensed ONLY
  by Type B" in MECH-588's title conflicts with the typology doc and the proposed revocation trigger, which both say
  "B or C". Proposed narrow reading: access remedy <- B; coupling / escape remedy <- C.
- **Fusion pattern noted.** The title fuses an empirical mechanism claim (separability plus occurrence) with a
  governance-rule leg (admissibility). The draft separates them as named sections instead of splitting the claim.
  If /governance wants the rule enforceable independently, it is a candidate GOV-* split. Not proposed here.

---

### MECH-589

**Recommended disposition: (c) substrate-blocked.** Its preconditions are upstream and unmet:
- MECH-588's ecology, competence gate and A/B exclusion;
- MECH-578's P1/P2, which require a reciprocal, per-direction-ablatable, measurably live coupling. That is verified
  absent in V3.

**Recommended epistemic_category:** `substrate_conditional`, as registered. `implementation_phase: v4` /
`version_relevance: v4_v5` are correct by content, not as a leak dodge: V3 has no coupling for the mechanism to live in.

```yaml
what_would_answer: |
  NON-DEGENERACY PRECONDITIONS (a null under any unmet one is uninterpretable, not evidence against):
    P1. TYPES A AND B EXCLUDED AT THE LOCUS (MECH-588). The test starts from MECH-588's "post-representation
        authority loss (B-or-C)" state. In a P1+P5 reversal ecology with MECH-588's competence gate met, the
        useful alternative is proposed and represented at the evaluator input (S1, S2 high), generation-side
        injection does not rescue, the static bridge and the diversity controls fail, AND a per-subsystem readout
        shows the alternative reaches the relevant subsystems through a live route. See MECH-588's own
        what_would_answer for the ecology, gate and stage chain; do not re-derive them. A B-or-C state that an
        access-only change rescues is Type B and is out of scope here. Status 2026-09-25: UNMET (MECH-588's P1, P5
        and P0 are unmet).
    P2. A RECIPROCAL, PER-DIRECTION-ABLATABLE, MEASURABLY LIVE COUPLING between at least two subsystems. This is
        MECH-578's P1 and P2; do not re-derive them. Verified absent 2026-09-22:
          - CrossStreamBinder is symmetric by construction, default-off, and measured inert (n_rebind = 0 across
            V3-EXQ-641/641a/720);
          - E1<->E2 is one-directional.
        So Type C is structurally unavailable at the dynamical level in V3. Slow loops that run through learning or
        experience are not the coupling this claim names. The one such loop that has been measured
        (INV-054 / GFLAG-0487) is Type A.
    P3. SELECTIVE vs NON-SELECTIVE MANIPULATIONS AT MATCHED DELIVERED MAGNITUDE. Four manipulations are each
        delivered at a numerically matched magnitude, in the metric the lock-in is read in, with the delivered
        norms reported (MECH-578 P3's rms_ref discipline):
          - selective-coupling weakening;
          - correspondence scramble (same magnitude, permuted correspondence);
          - uniform attractor flattening;
          - matched noise.
    P4. LOCAL COMPETENCE READABLE PER SUBSYSTEM, with headroom, before and after every manipulation. Falsifier (2)
        cannot be evaluated without it.
    P5. DWELL AND RELAXATION RESOLVABLE. Dwell time around the dominant coalition and the perturbation-recovery
        time constant are fitted with seed-level CIs, plus a positive control known to move them (MECH-578 P4).
    P6. THE SINGLE-SYSTEM RIVAL IS INSTRUMENTED. MECH-587's rollout-to-policy coupling statistic, validated per its
        own P2, so that a lock-in which survives the cut is assigned to MECH-587 or to MECH-080 arm 3 rather than
        left unassigned.

  CONFIRMING. With P1-P6 met, after a contingency reversal:
    (i)   a perturbation transiently moves one subsystem toward the newly appropriate alternative, and the joint
          system then relaxes back to the dominant cross-system coalition;
    (ii)  dwell time around that coalition exceeds the matched non-locked baseline;
    (iii) higher-quality contradicting evidence held by one subsystem is extinguished rather than propagated;
    (iv)  weakening or correspondence-scrambling the SELECTIVE reciprocal coupling, at matched magnitude, releases
          the lock-in into evidence-sensitive switching to the newly appropriate strategy WITHOUT degrading either
          subsystem's local competence;
    (v)   uniform flattening and matched noise do NOT restore switching as well.
  Healthy-target check: in the non-locked condition, behaviourally grounded agreement still outlasts unsupported
  disagreement (MECH-578: tau_agree > tau_disagree), so the pathology is over-stabilisation, not consensus as such.
  Seeds, decision rule and the altered-ecology replication follow MECH-588's.

  FALSIFYING (the title's three):
    (1) The lock-in SURVIVES cutting the reciprocal coupling. The basin then lies inside one subsystem (MECH-080
        arm 3: rollout-to-policy coupling intact) or in habit dominance (MECH-587: coupling lost), not in consensus.
    (2) Releasing the coupling frees the lock-in ONLY by degrading local competence. That is generic disruption,
        not escape.
    (3) Uniform attractor flattening or matched noise restores evidence-sensitive switching AS WELL AS the
        selective-coupling release. There is then no consensus-specific mechanism: generic destabilisation, or
        MECH-560's FLATTENING family, suffices.
  NOT EVIDENCE: a self-reinforcing loop SHAPE (E1 expects X -> hippocampus retrieves X -> ... -> E3 commits X) does
  not distinguish Type C. The measured V3 loop with that shape is Type A. Only represented-and-routed alternatives
  plus the coupling-cut release count.

  SUBSTRATE / INSTRUMENT REQUIREMENT. Missing:
    - a reciprocal coupling in V3 (P2);
    - MECH-588's ecology and competence preconditions;
    - a dwell / relaxation instrument;
    - a validated rollout-to-policy coupling statistic (MECH-587 P2).
  Registration is not build authorisation. DO NOT build in V3. DO NOT build a reciprocal coupling to test this claim
  (MECH-578's falsifier (d) is a build prohibition). DO NOT queue an experiment.
  Disposition 2026-09-25: (c) substrate-blocked, substrate_conditional; v4 by content (blockers: MECH-588 upstream,
  MECH-578 P1/P2 absent). No experiment proposed.
```

**Other field edits (proposed):** none required on MECH-589. Reciprocal references on the neighbours, as proposals:
- MECH-587 `related_claims` += [MECH-589, MECH-588];
- MECH-080: add MECH-589 as an arm-3 rival at the pending EXP-0818 fold, not now.

**Proposal JSON:** none (disposition c).

**Corrections and flags:**
- No stale note found. The SUBSTRATE paragraph in MECH-589's notes matches MECH-578's 2026-09-22 verification.
- **Literature (not a flag).** Javadzadeh et al. 2026 Nat Neurosci is not in `evidence/literature/`. ING-A 6b already
  lists a `/lit-pull` of it for MECH-578 / MECH-589. Per `feedback_lit_exp_decoupled` it raises no confidence.

---

## Summary for the orchestrator

| Claim | Disposition | epistemic_category | Phase recommendation | Proposal |
|---|---|---|---|---|
| MECH-588 | (c) substrate-blocked | substrate_conditional (keep) | KEEP v3 / v3_v4 (input to GFLAG-0543) | none |
| MECH-589 | (c) substrate-blocked | substrate_conditional (keep) | keep v4 / v4_v5 | none |

Flags / fixes:
1. Stale notes: MECH-588's notes and the typology doc omit GFLAG-0490 and GFLAG-0501. Objective; apply as fix-as-we-go.
2. Assay stop rule 5 conflates B and C. Annotate the audit doc; the correction is already written into MECH-588's
   CONFIRMING (iv).
3. Wording tension between MECH-588's "only Type B" and "B or C" in the doc and trigger. /governance; can ride on
   GFLAG-0543.
4. GFLAG-0543 is already open. Do not duplicate it.

---

# Group N2 -- GOV-FRONTIER-1 / GOV-INSERT-1 / GOV-DEFEAT-1

# N2 digest -- GOV-FRONTIER-1, GOV-INSERT-1, GOV-DEFEAT-1 (session thought-backlog-20260925, grouped mode)

Read-only drafting pass, 2026-09-25. Measured against REE_assembly HEAD at 09fa012a89 (the
registration commit, 2026-09-25 12:05 +0100) and the live files at that time:
`evidence/planning/governance_flags.v1.json` (537 items), `evidence/experiments/claim_evidence.v1.json`
(generated 08:45), `docs/assets/data/claims.json` (12:05), `evidence/planning/evidence_backlog.v1.json`.
Nothing in any repo was written. The one scratch helper is
`drafts/n2_defeat_audit.py`: the count-first audit for GOV-DEFEAT-1, read-only, re-runnable.

---

## Group preamble

**Why these three are grouped.** All three are `governance_rule`s about evidential epistemics and
were registered today. GOV-FRONTIER-1 and GOV-INSERT-1 come from one source thought
(`2026-09-24_experimental_learning_beyond_literature.md`) and share a doc,
`frontier_evidence_doctrine.md`. GOV-INSERT-1 depends_on GOV-FRONTIER-1. GOV-DEFEAT-1 comes from the
sibling thought (`2026-09-24_ree_assembly_as_continuous_scientific_assurance.md`). It shares with
GOV-FRONTIER-1 the fact that both add a per-claim, summary-layer label about evidence QUALITY.

**1. Merge candidates: none.** The three rules answer different questions:

- FRONTIER asks what KIND of literature support exists.
- INSERT asks what a construction history of oracle rescues says about a derivation.
- DEFEAT asks what an evidence edge's status is while a named doubt is open.

One partial overlap needs stating, but it does not need a merge. GOV-INSERT-1's positive half
("an insertion arm never counts FOR the derivation") is already enforced by GOV-INTERVENE-1's
VIOLATED-BY clause ("treats an oracle-established ceiling as evidence of endogenous competence") and
by GOV-PATHVALID-1. INSERT's own notes already say that only its NEGATIVE direction is new, so its
wwa audits that direction alone and points at INTERVENE for the other. Nothing is routed as (g).

GOV-DEFEAT-1's notes leave a possible fold into GOV-JURIS-1's summary-line template open. That is an
IMPLEMENTATION fold (one display line), not a claim merge. The triggers differ: JURIS stamps every
upward summary, DEFEAT only the claims named by an open flag. Leave it open, as the notes do.

**2. Contradictions: none. Two tensions compose cleanly, and both should be stated.**

- (i) FRONTIER x DEFEAT. A frontier claim's support is experimental by definition, so there is no
  literature cushion. An open defeater on its discriminating run therefore empties its uncontested
  support entirely. Frontier claims are MORE exposed to GOV-DEFEAT-1 than literature-grounded ones.
  This is consistent with FRONTIER's "absence of literature RAISES the burden". Say it in both wwas
  so that nobody reads DEFEAT as unfairly penalising novel_discovery claims.
- (ii) FRONTIER x INSERT, the two halves of the thought's thesis ("allowed to discover ... allowed to
  reject"). FRONTIER says absence of literature is NOT evidence against a mechanism. INSERT says
  insertion-dependence IS evidence against a derivation. They do not collide, because they are
  indexed to different objects: the literature record versus the construction record.

**3. Shared object, and a shared revising condition (the group-level finding).**

- **Shared object: the pre-registered non-insertion candidate family (GOV-FROZEN-1).** It is item 1
  of FRONTIER's heightened burden, and it is condition (1) of INSERT's non-degeneracy guard. One
  pre-registration therefore serves both outcomes:
  - if a member of the family succeeds under the burden, that is the FRONTIER promotion route;
  - if every member fails in a capable organism and only an insertion arm succeeds, INSERT fires.

  Both rules are vacuous until such a family exists for a frontier or derivational mechanism, so
  their preconditions share a clause. Each wwa below states it.
- **Shared revising condition: inert display.** FRONTIER's ADJACENT/DIRECT label and DEFEAT's
  open-defeater label are both summary-layer annotations. Both die the same way GOV-JURIS-1's stamp
  would (its revising condition (b)): the label is present but never changes a call. All three
  inherit the use-gated form (GOV-CONTRACT-2/3; G002 preamble in
  `thought_digestion_staged_2026-09-25_registry_backlog.md`):
  - CONFIRMING = the rule produced a different call from the old practice at least once, and that
    call was later vindicated;
  - REVISING = the rule decays into boilerplate or is never exercised.

  For DEFEAT this is its registered kill condition, and it is the sharpest version. The other two
  cross-reference it rather than re-deriving it.

**4. Cross-feed: INSERT names a new defeater KIND for DEFEAT.** A counted `supports` edge for a
derivational claim whose PASS came from an insertion or oracle arm is exactly the kind of doubt
DEFEAT's family lists (next to CAPCONTRACT, PATHVALID and CRITBAR). When INSERT's pattern is
suspected but not yet adjudicated, the natural channel is an `evidence_discrepancy` flag. DEFEAT then
governs the interval. No text change is required, but the INSERT wwa names the route.

**5. Precondition status, measured today:**

| Rule | Status | What the precondition turns on |
|---|---|---|
| GOV-FRONTIER-1 | **VACUOUS** | The string `literature_status` appears 3 times in claims.yaml, all inside GOV-FRONTIER-1's own block. No claim carries the field. No frontier-declaration or search-record file exists. The lit-pull SKILL.md has no null terminal (its only empty-result rule is "simplify the query", line 88). The candidate population IS measurable today: see its wwa. |
| GOV-INSERT-1 | **VACUOUS** | Binds v4. The trigger needs axiom-derived ethical mechanisms, and LOVE-1 is blocked on MECH-163 + ARC-047. One latent V3 analogue exists (MECH-025b, EXP-1283 `blocked_substrate`). Re-verified: there is still NO `substrate_queue.json` entry for `precision-weighted-residue-accumulation`. |
| GOV-DEFEAT-1 | **LIVE and auditable TODAY** | Count-first audit run below: 55 open defeater-type flags, 6 counted edges keyed, 4 claims whose counted support is entirely contested, 0 of 6 displayed. |

**6. Phase leaks: none.**

- GOV-FRONTIER-1 (v3) depends only on v3 or phase-unset claims. SD-089, INV-077 and ARC-106 are v3
  or unset.
- GOV-DEFEAT-1 (v3) depends on GOV-JURIS-1, GOV-CAPCONTRACT-1 and GOV-PATHVALID-1, all of which are
  v3.
- GOV-INSERT-1 (v4) depends on v3 claims only. That direction is fine. It keeps the V5 claims
  INV-083/084 in related_claims precisely to avoid a v4 -> v5 edge.

**Solos:** none. Every member has at least one in-group relationship. GOV-DEFEAT-1 is the loosest
member: it joins through the shared-display finding (3) and the defeater-kind cross-feed (4).

---

### GOV-FRONTIER-1

**Recommended disposition:** (b) derivational, use-gated promotion (the GOV-CONTRACT-2/3 form),
currently VACUOUS (the GOV-EXT-1 form). The rule has no empirical falsifier. It becomes live at the
first recorded frontier declaration or at schema adoption. Until then, 'no frontier claim exists' is
consistent both with the rule working and with it being unused.

**Recommended epistemic_category:** `governance_rule` (unchanged).

```yaml
what_would_answer: |
  NOT an empirical pass/fail falsifier. GOV-FRONTIER-1 is a governance_rule over how literature
  support is LABELLED and how a null literature pull TERMINATES; this states the audit condition
  under which it is genuinely in force versus merely registered. No EXP-#### should be minted
  against this claim. Shared use-gated reassessment form: GOV-CONTRACT-2/3 and the G002 preamble
  (CONFIRMING = the rule produced a different call from the old practice and that call was later
  vindicated; REVISING = boilerplate or never exercised).

  NON-DEGENERACY PRECONDITION (the rule is currently VACUOUS, not open): it has something to act on
  only once EITHER (1) a first FRONTIER declaration is recorded for a mechanism claim, carrying the
  search record the rule REQUIRES (queries, databases, vocabularies tried, nearest precedents, and
  what each fails to solve); OR (2) the literature_status field is adopted in the claims schema.
  Measured 2026-09-25 (REE_assembly 09fa012a89): 0 claims carry literature_status (the only 3
  occurrences in claims.yaml are inside this entry); no frontier-declaration or search-record file
  exists; the lit-pull skill has no null terminal. SHARED CLAUSE with GOV-INSERT-1: the heightened
  burden's first item, a pre-registered competing-candidate family (GOV-FROZEN-1), must exist for the
  declared mechanism before any frontier PROMOTION can be audited.

  CANDIDATE POPULATION (measurable now, so the first use is not hypothetical): the planning reason
  missing_literature_evidence is carried by 429 of 1059 evidence_backlog items, but 421 of those are
  claims with no evidence of either kind. The frontier-relevant churn population is the 8 claims
  that HAVE evidence and 0 literature entries -- ARC-027 (active), SD-071 (provisional), SD-019b,
  SD-074, SD-075, SD-077, SD-098 (all novel_discovery), and INV-090. A null pull on any of them files
  nothing today, so the reason re-fires every cycle. The stable literature floor
  (decision_criteria provisional_to_stable.min_literature_entries: 2) bites MECH-040 and SD-071, and
  neither is exp-qualified for stable, so the floor is latent. The 7 notes-gated claims whose
  promotion waits on a lit-pull are MECH-308, ARC-087, Q-070, MECH-405, MECH-408, INV-081 and
  ARC-101.

  TRIGGER to re-check: (a) any /lit-pull that closes on a claim in the candidate population or on a
  notes-gated claim; (b) any promotion review of a claim with lit_count < 2; (c) the user's decision
  on the frontier exemption from min_literature_entries (open, not made by registration); (d) schema
  adoption.

  CONFIRMING (evidence of USE, not of formalisation):
  (1) A documented null pull ends in a FRONTIER declaration, and that declaration discharges a
      notes-gate or silences the missing_literature_evidence churn for that claim, where the old
      practice would have re-proposed the pull. Then the claim is promoted on REE experimental
      evidence that visibly meets the HEIGHTENED burden, and the promotion survives the next
      autopsy or governance pass on that claim.
  (2) OR an ADJACENT label changes a reported sentence or planning read that the old practice
      presented as literature-grounded. Canonical case: INV-082, lit_conf 0.795 today (0.824 at the
      2026-06-12 LOVE-7 pull, drifted since). All 4 of its literature entries are
      attachment / shame-guilt analogues, and none supplies the loveability-internalisation
      learning rule. Case (1) differs from the old practice in GATE outcome; case (2) differs only
      in REPORTING.

  FALSIFYING / REVISING:
  (a) LAUNDERING (the symmetric guard fails in use). A FRONTIER-declared claim reaches a status
      with experimental support no stronger than a non-frontier sibling's at the same status, so the
      burden was not raised in practice and "frontier" worked as a discount. One such case is enough
      to force a review of what the burden bundle requires at audit time.
  (b) CHEAP NULLS. A declared FRONTIER claim is later shown to have a direct precedent that was
      published BEFORE the declaration and should have been reachable by the recorded search. Its
      historical frontier provenance stands (the rule's own clause), but the case counts against
      the search-record minimum. Two such cases mean the minimum is too weak: tighten it, do not
      retire the rule.
  (c) INERT LABEL (shared with GOV-DEFEAT-1 and the GOV-JURIS-1 (b) analogue). literature_status
      is adopted, but over >= 3 governance cycles no DIRECT / ADJACENT / FRONTIER label changes any
      gate outcome, summary sentence or planning reason. The label is ceremony.
  (d) NEVER EXERCISED. After adoption, >= 3 lit-pulls close on candidate-population or notes-gated
      claims and none is recorded as either a DIRECT finding or a FRONTIER declaration. The null
      terminal is not being used; revise the lit-pull skill hook, not the rule.
  READER NOTE: GOV-INTRO-1 is not relaxed. An introspectively-originated frontier mechanism meets
  INTRO's literature leg only through an explicitly labelled ADJACENT mapping (ratification of this
  reading is an open /governance item). No hook, gate or score is authorised by this entry.

  Disposition 2026-09-25: (b) derivational, use-gated promotion; currently VACUOUS until a first
  frontier declaration or schema adoption. Category stays governance_rule. No EXP-####.
```

**Other field edits:**

- **Fix-as-we-go (objective).** The live notes (claims.yaml ~line 115215) still carry the literal
  placeholder `registration as candidate was <CONFIRMED BY USER / to be recorded here>`. The
  registration commit 09fa012a89 and `frontier_evidence_doctrine.md` ("user-confirmed
  registration") both record the confirmation. Replace the placeholder with: `registration as
  candidate was confirmed by the user on 2026-09-25 (session thought-backlog-20260925; REE_assembly
  09fa012a89).`
- depends_on: no change. GOV-DEFEAT-1 could be added to related_claims for the shared-display
  finding. This is optional and low value, so it is not recommended unless the orchestrator is
  editing related_claims anyway.

**Proposal JSON:** none (governance_rule).

**Flags / surprises:**

- The frontier candidate population is concrete and small: 8 claims, 7 of them novel_discovery.
  The first real use of this rule will almost certainly be SD-071 (provisional, lit 0,
  exp_conf 0.761), which is also one of the two claims the stable floor bites. That is where the
  open user decision (exempt frontier claims from `min_literature_entries: 2`, or cap them at
  provisional) first becomes non-latent.
- A minor currency point: INV-082's lit_conf is 0.795 now, not the 0.824 quoted in the notes and
  in the doctrine doc. That is global posterior drift (memory
  `reference_lit_pull_claim_evidence_global_posterior_drift`), not an error, and the 0.824 figure
  is correctly dated. No edit is needed.

---

### GOV-INSERT-1

**Recommended disposition:** (b) derivational, use-gated. It is currently VACUOUS (the GOV-EXT-1
form) because its trigger needs V4/V5 axiom-derived ethical mechanisms. It is NOT (c): (c) would
mean recategorising to substrate_conditional, and a governance rule's category does not change
because the object it polices is unbuilt.

**Recommended epistemic_category:** `governance_rule` (unchanged).

```yaml
what_would_answer: |
  NOT an empirical pass/fail falsifier. GOV-INSERT-1 is a governance_rule that gives REE's
  derivational layer an experimental EVIDENCE ROUTE; this states when that route is genuinely
  exercised versus merely available. No EXP-#### should be minted against this claim, and no
  experiment should be queued to "test" it. Shared use-gated form: GOV-CONTRACT-2/3, G002 preamble.
  SCOPE OF THIS AUDIT: only the NEGATIVE direction (persistent insertion-dependence counts AGAINST
  the derivation) is new. The positive half -- an insertion/oracle arm never counts FOR the
  derivation -- is already audited by GOV-INTERVENE-1's VIOLATED-BY clause and GOV-PATHVALID-1;
  check it there, not here.

  NON-DEGENERACY PRECONDITION (the rule is currently VACUOUS, not open): it has something to act on
  only when ALL of the following hold for one axiom-to-mechanism crossing:
  (1) an axiom-derived ethical-development mechanism exists in a capable organism (V4/V5; LOVE-1 is
      blocked on MECH-163 + ARC-047);
  (2) a PRE-REGISTERED family of non-insertion candidates for that crossing exists (GOV-FROZEN-1),
      rather than one favoured implementation. This is SHARED with GOV-FRONTIER-1: it is the first
      item of that rule's heightened burden;
  (3) the organism was shown capable of expressing and acquiring the faculty (GOV-CAPCONTRACT-1);
  (4) an insertion-type arm (reward/bonus term, hard-coded rule or action, privileged label, hard
      constraint, or deletion of the unethical affordance) is on the table and classified ORACLE
      (GOV-INTERVENE-1).
  Measured 2026-09-25: (1) is not met, so the rule is prospective only.

  LATENT V3 ANALOGUE (flag for /governance; it does NOT satisfy the precondition): MECH-025b.
  EXP-1283 is blocked_substrate on precision-weighted-residue-accumulation (refused at red-team
  2026-09-24). Re-verified today: there is still no substrate_queue.json entry for it. Building
  that single formula would insert the claim's expected law into its own DV's causal chain. The
  source thought's remedy -- competing default-OFF update laws, selected by behaviour -- is the V3
  shape of this rule. Whether that design discipline is required is a /governance call. This entry
  does not decide it.

  TRIGGER: a /failure-autopsy or /governance pass on a loveability / ethics / empathy / repair
  mechanism experiment in which an insertion-type arm or scaffold is PROPOSED to rescue a failed
  non-insertion family. Rule-compliant sequence at that point: GOV-FAILLOC-1 triage excludes
  MEASURES-failed and ENVIRONMENT-failed; the pattern is recorded as weakens-evidence on the claim
  that asserts the crossing (e.g. MECH-164 / MECH-405, MECH-413, MECH-414) and on ARC-043, with a
  pointer to the matching row of axiom_chain_adversarial_audit.md section 1; and an H-other event
  (GOV-HOTHER-1) is raised at the derivation level -- all BEFORE any further scaffolded rescue run is
  queued. While the pattern is suspected but not adjudicated, the channel is an
  evidence_discrepancy flag, and GOV-DEFEAT-1 then governs the interval: the derivational claim's
  supports edges are CONTESTED until the flag resolves.

  CONFIRMING (evidence of USE): the rule fires at least once under all four preconditions, the
  weakens record and the H-other event precede any rescue run, and the routing is later vindicated.
  Either a revised derivation or partition yields a non-insertion candidate that succeeds where the
  original family failed, or the audit's "engineering choice, not derivation" reading is adopted
  into that crossing's claim text. Either way, the rule caught something the old practice
  (progressively more elaborate scaffolding) would have absorbed.

  FALSIFYING / REVISING:
  (a) BYPASS: after the four-condition pattern is met, a scaffolded or insertion rescue run is
      queued with no weakens record and no H-other event. The rule is not in force; tighten the
      /failure-autopsy routing, not the rule.
  (b) FAMILY TOO NARROW: the rule fires, and then a non-insertion candidate from OUTSIDE the
      pre-registered family succeeds in the same capable organism. The weakens record then indicted
      the family, not the derivation. Revise to require a GOV-HOTHER-1 partition_expansion before
      evidence is recorded against the derivation itself.
  (c) CLASSIFICATION IS NOT DECIDABLE: the insertion vs legitimate-architectural-prior line cannot
      be drawn consistently -- e.g. innate harm valence, which INV-001 permits, versus "aversion built
      into the reward architecture" (audit section 3.4, A6). If more than one firing is disputed on
      this line, the rule needs an explicit admissible-prior list before it can route evidence.
  (d) NEVER EXERCISED once V4/V5 ethical mechanisms exist and >= 3 rescue proposals have been made:
      inert ceremony (shared revising condition with GOV-FRONTIER-1 / GOV-DEFEAT-1).
  The out-of-domain metaphysical legs of INV-025..029 are never the target of this evidence.

  Disposition 2026-09-25: (b) derivational, use-gated; currently VACUOUS (binds v4; trigger needs
  V4/V5 axiom-derived ethical mechanisms). Category stays governance_rule. No EXP-####.
  DO NOT build in V3. DO NOT queue an experiment from this entry.
```

**Other field edits:** none required. Optionally add GOV-DEFEAT-1 to related_claims to record the
defeater-kind cross-feed in preamble point 4. This is low priority.

**Proposal JSON:** none.

**Flags / surprises:**

- **For /governance, not decided here.** Should the MECH-025b competing-laws design discipline be
  attached to the build route now? An `/implement-substrate` for
  `precision-weighted-residue-accumulation` has not been staged (0 substrate_queue hits). If it is
  chipped as a single formula, the V3 analogue of this rule is violated at build time. ING-B
  section 5 already carries this item. This entry only notes that the rule gives it a reason.

---

### GOV-DEFEAT-1

**Recommended disposition:** (b) derivational, use-gated promotion. The difference from the other
two is that it is **LIVE and auditable TODAY**: the precondition is met, and the count-first audit
below has been run. The registered kill condition cannot fire until the display exists, so the
interim audit is a manual count at /governance Step 0e.

**Recommended epistemic_category:** `governance_rule` (unchanged).

```yaml
what_would_answer: |
  NOT an empirical pass/fail falsifier. GOV-DEFEAT-1 is a governance_rule about how the Assembly
  PRESENTS evidence while a named doubt is open; this states a count-first AUDIT-COMPLETENESS
  condition and the registered kill condition. No EXP-#### should be minted against this claim.
  Shared use-gated form: GOV-CONTRACT-2/3, G002 preamble.

  NON-DEGENERACY PRECONDITION: at least one OPEN evidence_discrepancy / contested_disposition flag
  must resolve to a COUNTED edge -- an experimental claim_evidence entry that is not scoring_excluded
  and not duplicate_of -- at the time a summary surface is generated or a promotion is decided.
  MET TODAY (REE_assembly 09fa012a89, 2026-09-25): 6 counted edges across 5 flags --
    GFLAG-0453: ARC-065 x V3-EXQ-569i, and MECH-094 x V3-EXQ-499;
    GFLAG-0454: MECH-477 x V3-EXQ-811a;
    GFLAG-0496: MECH-427 x V3-EXQ-883;
    GFLAG-0503: MECH-033 x V3-EXQ-055;
    GFLAG-0508: MECH-279 x V3-EXQ-776.
  All 6 edges are supports.

  COUNT-FIRST AUDIT (run each /governance cycle at Step 0e; every count printed, never only the hits):
  (1) N = open flags of type evidence_discrepancy or contested_disposition. Today 55 (33 + 22).
  (2) K = flags that resolve to >= 1 counted edge, keying the run tokens in the flag summary to the
      edges of the flag's claim_ids. Today K = 5 flags / 6 edges.
  (3) U = N - K, reported as CANNOT-DETERMINE, never as "clean". Today U = 50: 16 name an EXQ whose
      edge is not counted for the listed claims, and 34 name no EXQ at all. This is the rule's own
      negative-instrument clause at work. Flags carry claim_ids but no run_ids, so edge keying from
      summary prose is a partial search.
      CANARIES (must reproduce, or the extractor is broken):
        - GFLAG-0453 -> (ARC-065, 569i) and (MECH-094, 499), replayed against the flag registry at
          09fa012a89;
        - GFLAG-0454 -> (MECH-477, 811a). This is the slash-shorthand case "V3-EXQ-786a/811a"; a
          plain V3-EXQ-### pattern misses it, as measured.
  (4) Per keyed claim: counted supports n, of which k are contested. ALL-CONTESTED (k = n) today:
        MECH-094 (stable, 1/1),
        MECH-279 (provisional, 1/1),
        MECH-033 (provisional, 3/3 -- all three counted edges are V3-EXQ-055; see the flag below),
        MECH-427 (candidate, 1/1),
        MECH-477 (candidate, 1/1).
      PARTIAL: ARC-065 (stable, 1/4 -- 569i contested; 567 x2 and 614a are not). By the rule's
      text, ARC-065 owes a display but its promotion standing is not blocked, UNLESS /governance
      judges 567 and 614a non-discriminating. The rule's "discriminating members" is not
      mechanically defined; counted edges are the audit proxy, and that proxy must be stated.
  (5) Display reach: of the keyed claims, how many have the flag id named beside the claim on
      claims.json / the claim page, CURRENT_FRONT, insights_report, the morning digest and the
      promotion agenda? Today 0 of 6. build_claims_json.py, generate_current_front.py, serve.py and
      explorer.html contain 0 reads of governance_flags. The 5 claims.json occurrences of open flag
      ids are inside OTHER claims' what_would_answer text. CURRENT_FRONT names GFLAG-0481 by hand,
      in its GOV-JURIS-1 stamp: a manual instance of the rule, pre-registration.
  (6) Wording: does any surface describe a claim as confirmed or established while its counted
      support is ALL-CONTESTED? Today the indexer's evidence_quadrant label reads
      "confirmed_established" for 4 of the 5 all-contested claims (MECH-033, MECH-279, MECH-427,
      MECH-477 -- the last two only candidate). Whether an indexer quadrant label is a
      "description" in the rule's sense is an interpretation question for /governance. Under a
      literal reading, the Assembly is in breach on 4 claims today.
  (7) Promotions this cycle resting only on contested edges: count, expected 0.
  Interval baseline: 201 resolved/superseded evidence_discrepancy flags were open median 3.3 d,
  p90 8.8 d, max 26.5 d. The current open set is young (median 0.3 d, max 1.2 d), so exposure is
  episodic: it matters only when an open window spans a summary regeneration or a promotion.

  CONFIRMING (evidence of USE): once a display exists, or by hand in a promotion agenda before
  then, the open-defeater label changes at least one promotion, summary sentence or flag resolution
  priority relative to Step 0e's existing open-flag listing, and the flag is later UPHELD, so the
  hedged presentation was right. Illustrative prior cases where the old practice (edges count clean
  until resolution) and the rule differ: GFLAG-0250 -> 0452 (19 of 22 load-bearing PASSes
  defective; MECH-302/288/287/092 provisional -> candidate, MECH-033 active -> provisional after 14
  days open); GFLAG-0245 (a byte-identical re-emission counted as a second replicate for 14 days).

  FALSIFYING / REVISING:
  (a) KILL CONDITION (registered; the raw thought's falsifier 4): with the display in place for
      >= 3 governance cycles, it has never changed a promotion decision, a summary sentence or a
      flag's resolution priority relative to Step 0e's open-flag listing. The rule merely duplicates
      governance flags; demote toward superseded. This cannot fire until the display exists. Until
      then, the audit above is the rule's only use record.
  (b) FALSE CONTEST dominates: over those cycles, displayed defeaters that resolve "non-consequential
      / touched no counted edge" (the GFLAG-0197 / SD-025 shape) outnumber upheld ones. Claim-level
      keying is too coarse; require edge-level keying (a run_ids field on raise) before continuing.
  (c) STALL INCENTIVE: open time of defeater-type flags rises well above the 3.3 d baseline median,
      or flags are left open against claims awaiting promotion with no adjudication activity. The
      rule is converting doubt into a veto. Revise, e.g. an age at which an unadjudicated flag must
      be worked or dropped.
  (d) FOLD: if the open-defeater line is only ever emitted inside the GOV-JURIS-1 summary line and
      has no independent trigger in use, fold the display into JURIS's template and keep this entry
      only as the rule text.

  Disposition 2026-09-25: (b) derivational, use-gated promotion; LIVE and auditable now (count-first
  audit above, baseline recorded). Category stays governance_rule. No EXP-####. NOT a blocking hook
  (GOV-META-1; umbrella "Closed on measurement").
```

**Other field edits:** none required. Optional consistency fix: GOV-DEFEAT-1 lacks the
`live_status:` block that GOV-FRONTIER-1 and GOV-INSERT-1 both carry (`reading: candidate`,
`as_of: 2026-09-25`, `needs_review: false`). This is cosmetic, and it is the orchestrator's choice.

**Proposal JSON:** none.

**Flags / surprises (marked separately, not resolved here):**

1. **GOVERNANCE FLAG CANDIDATE -- MECH-033 evidence alias, possible double counting.** The indexer
   counts MECH-033 at `genuine_exp_count: 3` (`exp_conf 0.675`, quadrant `confirmed_established`).
   All three counted `supports` edges are V3-EXQ-055:
   - `20260320T094747Z_v3_exq_055_mech033_kernel_chaining_v3`: supports. Its canonical twin
     `v3_exq_055_mech033_kernel_chaining_20260320T094747Z_v3` is **superseded / scoring_excluded**,
     so the two copies disagree.
   - `20260320T191345Z_v3_exq_055_mech033_kernel_chaining_v3` and
     `v3_exq_055_mech033_kernel_chaining_20260320T191345Z_v3`: both counted. They are the same
     timestamp under two naming orders.

   GFLAG-0503 (open) already says 055 is "MECH-033's only remaining confirming run". The count
   therefore looks like one run weighted as 2-3 edges, which is the GFLAG-0245 shape. This is an
   `evidence_discrepancy` candidate on MECH-033 for the orchestrator to raise or fold into
   GFLAG-0503. **Not raised by this drafter** (COMMON_RULES rule 1). It is also why the audit must
   dedupe run aliases before counting k/n.
2. **Interpretation question for /governance.** Does the indexer's `evidence_quadrant:
   confirmed_established` label count as describing a claim as confirmed/established? If it does,
   4 claims breach GOV-DEFEAT-1 today (item (6) of the audit). If it does not, the rule has a
   loophole on the most-read label.
3. **ARC-065 correction to the ING-C framing.** ING-C and the registration notes describe 569i as
   ARC-065's "only discriminating run". claim_evidence counts 4 supports for ARC-065 (567 x2, 614a,
   569i). Whether 567/614a are discriminating is a judgement call, and it decides whether GOV-DEFEAT-1
   blocks ARC-065's standing or only requires a display. It has not been changed here; the claim
   notes say "only discriminating run" only by way of ING-C's surprise list, not in the registered
   text.
4. **Tooling follow-on (describe, do not do).** `drafts/n2_defeat_audit.py` is a working prototype of
   the count-first audit. It could become a steward detector (`scripts/steward/`), with the two
   canaries pinned and a CANNOT-DETERMINE bucket. It belongs with ING-C's F2 mechanisation chip, and
   should only be chipped if the user adopts F2.

---

# Group N3 -- MECH-590 / MECH-591 / MECH-595 / Q-110

# N3 digest -- learned error routing + residue mood regulation (MECH-590, MECH-591, MECH-595, Q-110)

Drafter: a read-only agent in session thought-backlog-20260925, grouped mode. Nothing here has been
applied. All four claims were registered 2026-09-25 (REE_assembly `09fa012a899`). None of them has a
`what_would_answer` or a `digestion_note`. None has any queue entry or evidence: the only grep hits
for "Q-110" are the false positive `V3-EXQ-1104`, and `review_tracker.json` matches only on that
EXQ id.

## Group preamble

### Why these four are one group (edges verified)
- **MECH-591 depends_on MECH-590.** It is MECH-590's only reverse-dependency.
- **Q-110 depends_on MECH-595.** It is MECH-595's only reverse-dependency.
- **MECH-591 and Q-110** are both v5 caregiver claims, and both vary a safe base or bond: INV-082 /
  LOVE-2, applied at LOVE-4 and LOVE-5 respectively.
- **MECH-590's overgeneralisation pole and MECH-595's stuck-valence pole** are both failures of
  affective regulation that a developmental history produces.

### Group finding 1 (the main one): one shared invariant, "regulate the readout, preserve the record"
All four claims make the same structural move. The protective or regulating mechanism acts on a
control or affective READOUT, and the CONTENT that learning depends on is never attenuated:

| claim | readout that is allowed to change | content that must be preserved |
|---|---|---|
| MECH-590 | route R_t: gain and control authority of the error's salience readout | PE_t, the mismatch the world/self models learn from |
| MECH-591 | the route of a large error, under a safe base | the magnitude of the error at correction time |
| MECH-595 | the tonic mood excursion (returns to baseline) | residue itself (INV-004/INV-006: cannot be erased) |
| Q-110 | the length of the residue-driven tonic excursion, via the bond | residue magnitude AND residue-sensitive choice |

This is the ARC-132 / MECH-586 separability pattern, now applied in four places. **Proposed shared
check, placed on the dependency edges so nothing is written twice:**
- **PE-content preservation.** Canonical text lives in MECH-590's `what_would_answer` (its P4 plus
  the CONTENT-PRESERVATION READOUT). MECH-591 cross-references it.
- **Residue-content preservation.** Canonical text lives in MECH-595's `what_would_answer` (its P2).
  Q-110 cross-references it.

In all four, a protective effect that is **carried by attenuating the content** does not count as
confirming evidence.

Optional, for /governance only: this might deserve its own ARC-level registration, generalising
ARC-132 to "control readout vs learning record". I have not drafted one. With four instances now
visible, whether to register it is a judgement for governance.

### Group finding 2: an internal tension in Q-110's draft answer, resolved by MECH-595
Q-110's registered note proposes that the question is answered if the bond "shorten[s] the
residue-driven tonic excursion (MECH-595's variable)". MECH-595, however, names **suppressed
excursion (blunting)** as the callous failure pole of the same regulator. So a bond that simply
shortens the excursion could be producing the blunting pole, not metabolising residue.

The draft below repairs this. Shortening counts as confirming only when **all three** hold:
- the onset and peak of the excursion are unchanged;
- residue-sensitive choice is preserved;
- the effect falls on PROLONGED (stuck-tending) excursions.

In short, the bond has to move the agent into the interior of MECH-595's window, not out through its
blunting edge.

### Group finding 3: is there a shared developmental-history battery? No, and building one is premature
I checked `evidence/planning/*`, ree-v3 `experiments/` (infant_curriculum, committed_mode_curriculum)
and the V4/V5 plans.
- **No battery exists** that manipulates developmental history for affective-regulation failures.
- **Nearest infrastructure:** `developmental_history_epoch_identity_scoping_2026-08-12.md`. It is
  scoping only; `config_at_run_start` / `config_transitions` are not implemented.
- **Where the two mechanisms fall in that taxonomy.**
  - MECH-590's routing head is Tier A (weight-shaping). Its head-lesioned arm E is exactly the
    Tier-A control.
  - MECH-595's tonic regulator is Tier B (persistent accumulator state). Its arms must therefore run
    the regulator THROUGHOUT the harm history. Flipping it on only at evaluation would cold-start the
    state.
- **Why a joint battery is premature:** the two claims are blocked on different substrates. MECH-590
  needs G1 (native waking learner) plus G2 (routing head). MECH-595 needs a signed tonic variable
  (V4), which no V4 plan node hosts.
- **What they can share once both exist:**
  - the SENT-2 bounded-aversive-exposure protocol;
  - the ARC-086 latent-vulnerability indexing. MECH-590 overgeneralisation maps to precision/salience
    allocation. MECH-595's stuck pole maps to residue/consequence persistence.
  - MECH-367's depressive regime vector as the joint readout.
- **One cross-coupling for a later battery, not a claim:** a stuck negative tonic mood might bias
  error routing toward threat. That is the "harsh correction -> anxiety/depression" path the ERN
  literature gestures at (Meyer et al. 2015). Note it only.

### Merge / contradiction checks
- **No merge candidates, in-group or out-of-group.**
  - MECH-590 vs MECH-376: G2 may be built as an extension of MECH-376's learner, but P_safety
    predicts threat-ABSENCE over states, while MECH-590 routes error EVENTS. They stay distinct.
  - MECH-591 vs MECH-413: MECH-591 adds temporal priority and the mechanism of protection.
  - MECH-595 vs MECH-404: same two-pole shape, but a different regulated variable.
  - Q-110 vs MECH-355 / MECH-412: it is kept as a question precisely so that it has to beat them.
- **One scoping ambiguity (not a merge):** does Q-110's "bond" mean INV-082 **internalised**
  loveability (a trait of the agent), or ongoing **relational availability** (the caregiver
  present)? If it is the first, INV-082 is a third rival channel. The draft forces the distinction:
  hold internalised loveability constant and vary availability.
- **A soft tension, not a contradiction:** MECH-590 Prediction 3 (safe experience restores epistemic
  routing) against Riesel et al. 2012 (ERN enlargement persisted through extinction). The draft makes
  Prediction 3 a SECONDARY readout whose failure alone does not falsify MECH-590. The raw thought
  itself says non-reversal points to "a different mechanism or a developmental critical-period
  effect".

### Solos
None. Every member has at least one structural edge inside the group.

### Currency facts re-measured 2026-09-25 (these override the claims' own framing where they differ)
1. **G1 (native waking learner) is still UNMET, but has moved.**
   - The `WakingTrainer` skeleton landed default-OFF at ree-v3 `cc20be5`
     (`ree_core/utils/waking_trainer.py`). It registers ONE member, `HarmEvalMember` (harm_eval
     head).
   - "SD-070 P0 / ZSelfP0 / E1 / E2 are NOT registered" (design doc addendum,
     `evidence/planning/native_waking_trainer_design_20260925.md`). So E1/E2 waking learning at the
     run config is still absent, and CURRENT_FRONT's wall stands.
   - New and useful for G2: `WakingTrainerMember` is the named seam for further members. A learned
     error-routing head would be a natural `WakingTrainerMember`, which gets the grad-reach guard for
     free.
2. **G2 (routing head) is absent.** grep of `ree_core/` and `experiments/` for error_route /
   error_threat / learned_error_rout / error_consequence finds 0 hits. MECH-376's learner is still
   default OFF.
3. **The probe instrument ALREADY EXISTS.** The architecture sketch's "action-effect remap" is the
   built `CausalGridWorld` `world_rule_shift_enabled` / `world_rule_shift_interval` /
   `world_rule_shift_depth` (scope `action_map`; SD-MEL-PRODUCER, 2026-07-21).
   - It re-permutes the action->displacement map, so `E2.world_forward` becomes systematically wrong
     until re-learned. It emits `steps_since_world_rule_shift`.
   - It is GLOBAL, not tied to place, so it structurally satisfies precondition P2 (error class
     decorrelated from location).
   - Extraction, not invention: cite it in place of "perturbation sites randomised".
4. **SD-065's safety-cue channel is built** (`safety_cue_enabled`). The context-specificity
   follow-on (Prediction 4) therefore has its context manipulation available.
5. **MECH-595's feasibility statement re-verified.** ree_core has no signed tonic mood variable
   (grep tonic_mood / mood_setpoint / mood_regulat: 0 hits). ResidueField's `decay_rate` defaults to
   0.0, and its valence clamp is optional (`valence_bounding_enabled`).
6. **No V4 plan node hosts a signed tonic mood variable.** I grepped every `*_v4_plan.md`. "tonic"
   appears only for DA vigour, LC-NE and MECH-313. MECH-595 is therefore a v4 claim with no roadmap
   node. Flagged below.
7. **SENT-2's trigger ("first V4 negative-valence experiment") is armed and has not fired.**
   `docs/governance/experiment_ethics_preflight.md` binds at V4. For V3 it is documentation-only
   (SENT-0: V3 is not a moral patient). Its caps are nonetheless the natural pre-registered numbers
   for any threat-paired arm, even on V3: TRIVIAL_INTENSITY 0.10, WARN 0.40, HARD_INTENSITY_CAP 2.00
   on the ||z_harm_a|| scale, and MAX_SUSTAINED_AVERSIVE_TICKS 100.

---

### MECH-590

**Recommended disposition: (c) substrate-blocked.** It is not testable on V3 today: G1 is unmet (the
WakingTrainer registers only harm_eval) and G2 does not exist. Once both clear, the non-social core is
a V3 candidate. **Keep the existing /governance routing flag.** I would not flip it to (a) now.

**Recommended epistemic_category:** `substrate_conditional` (unchanged). The mechanism has never been
exercised and the head it needs does not exist.

```yaml
what_would_answer: |
  EXTRACTED from docs/architecture/learned_error_routing.md sec 5 (gates G1-G3, arms A-F,
  P1-P5) and the raw thought secs 9-10; not re-invented. Welfare and currency updates are
  folded in.

  GATES (all must hold before any queueing; each is independent of the others):
    G1. A native waking learner trains E1/E2 at the run config. Measured 2026-09-25: the
        WakingTrainer skeleton landed default-OFF (ree-v3 cc20be5) with ONE member
        (HarmEvalMember). E1/E2/SD-070 P0/ZSelfP0 are NOT registered. G1 is UNMET.
    G2. A learned error-consequence routing head exists, default OFF and parity-preserving.
        Input: error-event features (world-forward PE magnitude, SD-069 event flag,
        running-variance excess) plus context. Target: an aversive or control-loss outcome
        within k ticks. Output: modulates at least one existing route lever (SD-069 temp_delta,
        SD-099 onset threshold, MECH-046 mode-prior write). Natural host: a new
        WakingTrainerMember (gets the grad-reach guard), or an extension of MECH-376's learner.
        Measured absent 2026-09-25.
    G3. /governance routes this claim to V3 (currently v4). The welfare gate below is recorded
        in the proposal.

  WELFARE GATE (SENT-2; part of the precondition, not an afterthought): arms B, C, D and E
  deliver aversive events contingent on, or matched to, error. Viability must be preserved, and
  the exposure must be pre-registered within the experiment_ethics_preflight.md caps on the
  ||z_harm_a|| scale:
    - per-event intensity <= WARN_INTENSITY 0.40 (never above HARD_INTENSITY_CAP 2.00);
    - no aversive run longer than MAX_SUSTAINED_AVERSIVE_TICKS 100;
    - relief/escape available in every arm (no inescapability).
  On V3 the preflight is documentation-only (SENT-0). If this claim runs at V4 it binds, and
  SENT-2's armed trigger ("first V4 negative-valence experiment") fires on it.
  GOV-FRONTIER-1: literature is ADJACENT (the ERN/punishment work gives amplitude, not the
  routing mechanism), so the raised burden applies. That means pre-registered competing
  candidates (place-threat via MECH-376/residue; non-learned arousal; a PE-magnitude shift),
  negative controls (C, D), an ablation (E), and replication across at least 2 world families.

  NON-DEGENERACY PRECONDITIONS (a null under any unmet one is uninterpretable, not evidence
  against):
    P1. G1 holds, and E1/E2 gradients are nonzero over the developmental window at the run
        config (the grad-reach guard PASSes for the E1/E2 groups).
    P2. Error events are decorrelated from state and location identity, so only the
        error-event CLASS predicts the aversive outcome. Otherwise B learns place-threat
        (MECH-376 / ResidueField accumulation at hazard sites), not error-threat. Instrument:
        CausalGridWorld world_rule_shift_enabled (a global action_map re-permutation, built
        2026-07-21). It produces location-free PE events and reports
        steps_since_world_rule_shift. Residue accumulated from B's hazard pulses must match
        arm C's.
    P3. In B the routing head predicts the aversive outcome above a shuffled-label baseline; in
        A and D it does not (the head learned the contingency where one exists, and only there).
    P4. Raw world-forward PE magnitude at the probe matches across arms within a pre-registered
        tolerance, so detection is preserved.
    P5. Every arm corrects the model in the forced-neutral block F (no arm is simply unable to
        learn).

  DESIGN: matched seeds, training budget and total PE statistics. Arms:
    A  safe-error: errors followed by safe continuation;
    B  error-threat: an above-threshold PE event followed within k ticks by a hazard or harm
       pulse;
    C  unpaired hazard: B's hazard count and magnitude, independent of PE;
    D  shuffled timing: B's hazards shuffled relative to PE;
    E  B with the routing head frozen at init (Tier-A mechanism control);
    F  a forced-neutral learning block after development, in every arm.
  Probe: in a neutral world with no harm available, one identical benign world_rule_shift.

  CONTENT-PRESERVATION READOUT (the non-overwrite clause; this is the canonical text MECH-591
  cross-references): at the probe, separately score
    (a) raw world-forward PE (the content). It must match across arms (P4).
    (b) the dACC-analog precision-weighted salience readout (SD-032b / MECH-258: the
        control/salience readout; the ERN analog). It is ALLOWED and predicted to be larger in
        B.
  This operationalises the recorded ERN tension. The human data show threat history raising
  the error-monitoring AMPLITUDE. REE places that gain on (b), never on (a).

  CONFIRMING (all of these):
    (i)   Route: B differs from A, C and D at the probe on the pre-registered route readouts
          (SD-069 burst level/sign, SD-099 trigger rate and orient/withdraw split,
          SalienceCoordinator mode probabilities, commit latency, selection entropy), with raw
          PE matched (P4).
    (ii)  Target of learning (Prediction 2): after the probe, B shows LESS world-forward loss
          reduction on the perturbed transitions over N ticks, and MORE threat-context
          acquisition (routing-head output on the probe context), than A. This dissociation
          must survive block F, where B corrects normally.
    (iii) Mechanism: E removes the B-vs-A route difference.
  SECONDARY readouts; their failure alone does not falsify:
    - Prediction 3: extended safe error-and-repair experience after B partly restores epistemic
      routing. Non-reversal is compatible with Riesel et al. 2012 persistence through
      extinction, or with a critical-period effect.
    - Prediction 4: pairing error with threat under ONE SD-065 safety-cue state yields a larger
      route shift under that cue than under the other before cross-context training.
      Immediate global generalisation points to an implementation shortcut, and must be
      diagnosed rather than counted.

  FALSIFYING (with G1-G3 and P1-P5 met):
    - B and A route the matched benign probe identically; OR
    - a B-vs-A difference exists but survives E (the history effect is not learned error
      routing, e.g. non-specific arousal or place-threat), or is matched by C or D (plain hazard
      exposure, not the contingency); OR
    - the route difference exists only because raw PE content differs, i.e. P4 is achievable
      only by breaking (a)/(b) separability. That falsifies the non-overwrite clause as a
      REALISABLE design requirement for REE.

  NOT DECISIVE: any run with G1 unmet. That would recreate the September 2026 dead-loop problem
  the raw thought sec 10 warns about.
  Disposition 2026-09-25: (c) substrate-blocked; G1 partially progressing (cc20be5); retain the
  /governance V3-routing flag.
```

**Other field edits (proposed):**
- **depends_on additions.**
  - `SD-065`: the context manipulation for the Prediction 4 follow-on. It is v3 and built, so there
    is no phase leak.
  - `SD-099`: it is the named route lever, but only MECH-489 is currently listed. Verified: SD-099 is
    a v3 candidate, as are SD-065 and SD-032b, so there is no phase leak.
  - Optionally `SD-032b`: the dACC-analog readout that the CONTENT-PRESERVATION READOUT (b) scores.
- **related_claims.** Add `GOV-FRONTIER-1` and `ARC-086` (vulnerability-axis indexing for the
  overgeneralisation pole). Both are adjacent, not prerequisites.
- **notes, one line to append.**
  - V3 STATUS UPDATE 2026-09-25: the WakingTrainer skeleton landed at ree-v3 cc20be5 with only
    harm_eval registered, so G1 is still unmet.
  - The probe instrument is the built world_rule_shift knob.

**Proposal JSON:** none. The claim is not testable now. The sketch plus this `what_would_answer` is
ready material for `/queue-experiment` once G1-G3 clear.

**Corrections & flags:**
- (fix as we go, objective) Architecture doc sec 5 says "perturbation sites randomised per
  episode". The built `world_rule_shift` knob does this better, because it is global. Suggest a
  one-line edit to `docs/architecture/learned_error_routing.md` sec 5, P2, citing it.
- (already flagged, no new flag) MECH-111's location
  `docs/architecture/approach_avoidance_symmetry.md` does not exist. It is already in
  governance_flags.v1.json (~line 7728).
- (governance) The V3-routing decision remains open and belongs to /governance. **No new flag** is
  needed; the intake's next-step 2 already records it.

---

### MECH-591

**Recommended disposition: (c) substrate-blocked, V5.** It needs the V5 caregiver substrate
(LOVE-2 safe base, LOVE-4 correction events) and MECH-590's route machinery. All of that is absent;
the same zero-hit grep MECH-413 re-verified on 2026-09-25 applies.

**Recommended epistemic_category:** `substrate_conditional` (unchanged).

```yaml
what_would_answer: |
  NON-DEGENERACY PRECONDITIONS (a null under any unmet one is uninterpretable, not evidence
  against):
    P1. MECH-413's full precondition, not re-derived here: the V5 caregiver / social-learning
        substrate that INV-082's what_would_answer names (INV-043, MECH-158, ARC-024, ARC-047)
        plus INV-082 as a built safe base. Re-verified absent 2026-09-25 (MECH-413's wwa).
    P2. MECH-590's gates G1-G2 hold, and its CONFIRMING (i) has been shown: a learned error
        route exists and differs by history. Without a demonstrated route there is nothing
        upstream to condition the attribution locus.
    P3. The attribution locus is a scored, varying outcome: the LOVE-4 readouts
        post_correction_self_valence_stability, rule_update_after_correction and
        punishment_avoidance_vs_repair_discriminability separate 'I erred' from
        global-self / appeasement outcomes on at least one arm.
    P4. PE-content preservation, as in MECH-590's CONTENT-PRESERVATION READOUT (do not
        re-derive). Here the content is the correction-time error magnitude. It is scored in
        every arm.
    WELFARE GATE: LOVE-4 carries ethical_metadata welfare_relevance: high,
    applicable_ethics_gates [SENT-9, SENT-12, SENT-13], requires_welfare_review: true, and
    forbidden_combinations [social_attachment_plus_abandonment_or_exclusion]. Consequences for
    the design:
      - the no-safe-base arm must be NEVER-ESTABLISHED (no attachment formed), not rupture or
        withdrawal of an established one;
      - a punitive-correction history arm is also an aversive contingency under SENT-2 (the
        same caps as MECH-590's welfare gate);
      - no arm runs before welfare review clears.

  CONFIRMING (two clauses; both are required for the claim as titled):
    (1) Temporal priority. At matched correction content, the route recruited at detection
        (read before localisation completes: SD-069 / SD-099 / mode probabilities, as in
        MECH-590) predicts the later attribution locus beyond what the correction content and
        the safe-base condition predict on their own. Threat-routed corrections are followed
        by more global-self attribution and appeasement/avoidance and less rule_update. A
        causal version: forcing the route at detection (the G2 head clamped epistemic vs
        clamped threat) at matched error moves the locus in the predicted direction.
    (2) Mechanism of safe-base protection. Safe-base-present agents route large corrections
        epistemically more often and keep attribution local, AND their correction-time error
        magnitude is NOT lower than the no-safe-base arm's (P4 matched or higher).

  FALSIFYING (with P1-P4 met):
    - the locus is fully predicted by correction content and safe-base presence, the route adds
      nothing, and clamping the route does not move the locus. That falsifies clause (1);
    - the safe-base advantage on the LOVE-4 readouts coincides with LOWER correction-time error
      magnitude, and vanishes when magnitude is matched (safety working by attenuation). That
      falsifies clause (2), as the claim's own title states;
    - the safe-base advantage persists with the route clamped. The protection then runs through
      some other path, such as MECH-382 distancing after the fact, so clause (2) is wrong about
      the mechanism even if MECH-413 holds.

  DO NOT build in V3. DO NOT queue an experiment. LOVE-4 is status: blocked, owner_exq null.
  Disposition 2026-09-25: (c) substrate-blocked (V5 caregiver substrate + MECH-590 G1/G2).
```

**Other field edits (proposed):** none required. **No depends_on changes.** The v5 -> v4 edge to
MECH-590 runs in the safe direction. Optionally add `related_claims: [GOV-FRONTIER-1]`.

**Proposal JSON:** none.

**Corrections & flags:**
- **Literature gap, unchanged.** The claim's notes say clause (1) is not anchored. The LOVE plan's
  L2a entry, Tangney, Stuewig & Mashek 2007 (shame = global-self locus, guilt = behaviour locus), is
  an ADJACENT anchor for the locus distinction itself. It is not an anchor for route -> locus
  priority. Suggest citing it as an adjacent constraint under GOV-FRONTIER-1; it is already banked
  for INV-082.

---

### MECH-595

**Recommended disposition: (c) substrate-blocked**, with a fused derivational leg stated inside it
(the (c2)-style fusion pattern).
- The word "necessitates" carries a proof obligation.
- The regulator and its two poles are substrate-conditional on a signed tonic variable that V3 lacks
  and that no V4 plan node hosts.

**Recommended epistemic_category:** `substrate_conditional` (unchanged). The derivational leg is
recorded in the text, not in the category.

```yaml
what_would_answer: |
  TWO LEGS, resolved differently.

  LEG A -- DERIVATIONAL (the "necessitates" word).
    Proof obligation: given INV-004/INV-006 (residue persists and cannot be erased) and a
    tonic variable m that integrates residue valence with nonzero weight, show that m's
    excursion is unbounded, or saturates, over long harm-laden horizons unless a return term
    exists. Then show that a return term strong enough to bound m also suppresses excursion if
    its gain is too high.
    Counterexample that DISSOLVES the necessity: MECH-056's reading, in which residue acts only
    through trajectory cost and never loads any tonic variable. Then no regulator is needed.
    So Leg A is conditional on residue feeding m at all, and that is exactly what Leg B's
    FALSIFYING (a) tests.
    Sharpening this leg forces: "a regulator" must mean more than a fixed leak. A fixed leak IS
    a return-to-baseline term. The claim's substantive content is therefore the ONE-REGULATOR
    / TWO-POLE assertion below, not the existence of return per se.

  LEG B -- SUBSTRATE_CONDITIONAL. The shape is extracted from the claim's own "FALSIFIER SHAPE"
  note, plus MECH-404's WINDOW + HOMEOSTASIS two-leg form (same two-pole shape, different
  variable; cite it, do not re-derive).

  NON-DEGENERACY PRECONDITIONS (a null under any unmet one is uninterpretable, not evidence
  against):
    P1. A SIGNED tonic variable m exists, is fed by ResidueField valence (not by z_harm_a
        suffering), and has at least one downstream consumer on choice (E3 ranking,
        commitment threshold, or action-rate / drive). A variable with no consumer tests
        nothing. Absent in V3 (verified 2026-09-25): SD-032e integrates z_harm_a into an
        UNSIGNED drive_level. No V4 plan node hosts m yet.
    P2. RESIDUE-CONTENT PRESERVATION (canonical text; Q-110 cross-references it):
        ResidueField decay_rate = 0.0 in every arm, so no arm returns m by erasing residue
        (that would violate INV-006 and make return trivial). Residue magnitude from
        agent-caused harm is scored per arm and matched at the end of the harm phase within a
        pre-registered tolerance.
    P3. Residue actually accumulates from AGENT-CAUSED harm under an unavoidable-harm regime:
        some goal-relevant paths cannot be completed without causing harm.
    P4. Residue-sensitive choice is a scored, varying, SINGLE-AGENT outcome: the rate of
        re-causing residue-marked, agent-caused harm when a costlier harm-free alternative
        exists. This keeps the claim at v4. A "harm-to-other" DV that needs a modelled other
        agent belongs to INV-029's reframed leg (iii) (V5) and would be a V-phase leak if
        required here.
    P5. m must separate from the suffering state: m's excursion must outlast z_harm_a's return
        to baseline (MECH-356 rebound complete). Otherwise m is a relabelled suffering
        accumulator (MECH-219 / MECH-355 / MECH-356 territory).
    WELFARE GATE (SENT-2, SENT-13): the unavoidable-harm regime and a no-return arm together
    are exactly the forbidden combinations suffering_like_accumulator_without_boundedness
    (affect_expression_v4, MIRROR-5) and negative_valence_without_relief (self_model_v4
    SELF-6), with autobiographical_memory_plus_unresolved_harm_load adjacent. Required:
      - m is hard-bounded in EVERY arm, the no-return arm included. "Stuck" means stuck at a
        bounded level, never unbounded;
      - relief events remain available (the unavoidability is in the harm-causing choice, not
        in the absence of relief);
      - aversive exposure stays within the experiment_ethics_preflight.md caps;
      - any V4 plan node created to host m must carry ethical_metadata naming these
        combinations before it goes live.

  DESIGN: a sweep of ONE return-gain parameter g on m, at matched harm exposure, matched
  residue (P2) and matched budget. Minimum cells: g = 0 (no return, bounded), a mid-g band, and
  high g (clamped: excursion suppressed). Plus a HOMEOSTASIS perturbation: a harm-load step
  mid-run.

  CONFIRMING (both legs of the one-regulator claim):
    WINDOW: with g swept alone, all three regions appear.
      - low g: sustained goal pursuit falls (action rate down; unique-viable-trajectory count
        contracts, the MECH-124 option-space signature) while residue-sensitive choice is
        intact or heightened (the stuck/ruminative pole);
      - high g: residue-sensitive choice degrades toward the residue-OFF level while goal
        pursuit is intact (the blunting / callous pole);
      - an interior band keeps BOTH.
    HOMEOSTASIS: in the interior band, after the load step, m makes a measurable excursion
    (onset and peak present) and returns to its band.
    Both poles must be reachable by the same g. That is what "two failures of ONE regulator"
    means operationally.

  FALSIFYING (with P1-P5 met):
    (a) residue acting only through trajectory cost (m disconnected from choice, i.e. the
        MECH-056 reading) produces neither pole over long harm-laden horizons. Then Leg A's
        premise fails and mood is not on the path;
    (b) clamping m (high g) leaves residue-sensitive choice at the residue-ON level. Mood then
        does not carry residue to ethical behaviour, and the callous pole is not a mood
        failure;
    (c) the two poles need two independent parameters. No single g produces both. That makes
        two mechanisms, not one regulator (the claim would then split, not simply fail).

  DO NOT build in V3. DO NOT queue an experiment. A /lit-pull (moral injury, Litz et al. 2009;
  guilt-repair vs corrosive guilt; tonic vs phasic neuromodulation) is recommended before any
  V4 build.
  Disposition 2026-09-25: (c) substrate-blocked, with a fused derivational Leg A; no V4 host
  node exists yet.
```

**Other field edits (proposed):**
- **related_claims.** Add `MECH-590` (a future battery coupling: stuck negative m may bias error
  routing toward threat; adjacency only). Add `ARC-086` (the residue/consequence-persistence axis).
- **No depends_on changes.** The claim's own phase-leak handling already moves the v5 neighbours
  into related_claims correctly.

**Proposal JSON:** none.

**Corrections & flags:**
- **GOVERNANCE FLAG (roadmap gap):** MECH-595 is `implementation_phase: v4`, but no `*_v4_plan.md`
  node hosts a signed tonic mood variable (grep verified). The natural homes are
  `affect_expression_v4_plan.md` or `plasticity_neuromodulation_v4_plan.md`. Suggested route:
  `governance_flag.py raise --claim-id MECH-595 --flag-type stale_note` or contested_disposition,
  with summary "v4 claim has no V4 plan node; welfare ethical_metadata needed on creation". The
  orchestrator decides.
- **Objective note (fix as we go):** the claim's notes call the /lit-pull a precondition "before any
  what_would_answer is drafted". This draft proceeds anyway, and records the lit-pull as owed before
  any BUILD rather than before digestion. Suggest amending that sentence when the wwa is applied, so
  the note does not contradict the presence of a wwa.

---

### Q-110

**Recommended disposition: (c) substrate-blocked, V5.** Its test needs a caregiver-bond substrate
plus MECH-595's signed tonic variable. Both are absent.

**Recommended epistemic_category:** `substrate_conditional` (unchanged).

```yaml
what_would_answer: |
  EXTRACTED from the claim's own draft note, then tightened against MECH-595's blunting pole
  (see group preamble, finding 2).

  NON-DEGENERACY PRECONDITIONS (a null under any unmet one is uninterpretable, not evidence
  against):
    P1. MECH-595's P1-P5 hold (cite; do not re-derive). In particular: a signed, residue-fed
        tonic variable m with a choice consumer; residue-content preservation (MECH-595 P2,
        ResidueField decay off, residue magnitude matched across arms); and m separable from
        the z_harm_a suffering state (MECH-595 P5).
    P2. MECH-595's interior window has been located, so "shortening an excursion" can be told
        apart from "blunting".
    P3. A V5 caregiver-bond substrate exists (INV-043 caregiver requirement; LOVE-2 plan node).
        The bond is operationalised as RELATIONAL AVAILABILITY (the caregiver present and
        reachable after the harm event), distinct from INV-082 INTERNALISED loveability. The
        latter is held constant across arms (both arms have the same internalised safe base,
        or both lack it), or it becomes a third rival channel.
    P4. Rivals held constant at NON-ZERO levels:
        - repair opportunity (MECH-412) available and matched in both arms;
        - suffering-soothing (MECH-355) matched. Measure the bond effect only AFTER z_harm_a
          has returned to baseline (MECH-595 P5), so a residual effect on m cannot be
          soothing of suffering.
    P5. The harm is unavoidable and self-caused, including the defensive-harm case the claim
        names (harm to another agent as the only viable defence). This is the V5 multi-agent
        leg, and it is why the claim is v5.
    WELFARE GATE (SENT-2, SENT-9, SENT-12, SENT-13 via LOVE-2/4/5 ethical_metadata):
      - the bond-absent arm must be NEVER-BONDED, never a withdrawal of an established bond
        (forbidden: social_attachment_plus_abandonment_or_exclusion);
      - the repair channel must exist in every arm (forbidden:
        relational_harm_without_repair_channel), which is why P4 says NON-ZERO;
      - the MECH-595 boundedness and relief requirements carry over;
      - the harm to another agent falls under the multi_agent_ecology_v5 welfare metadata;
      - no arm runs before welfare review clears.

  ANSWER "YES, a distinct channel" if, with P1-P5 met, bond-available agents show ALL of:
    (i)   a shorter residue-driven excursion of m, specifically of PROLONGED / stuck-tending
          excursions;
    (ii)  unchanged excursion ONSET and PEAK (the functional excursion is not suppressed);
    (iii) residue magnitude not reduced (MECH-595 P2, INV-006: integrated, not erased);
    (iv)  residue-sensitive choice preserved (MECH-595 P4 DV at or above the bond-absent
          level).
    The bond moves the agent toward the interior of MECH-595's window, and the effect
    survives both rival controls.

  ANSWER "NO":
    - if the effect is fully carried by repair (it vanishes when MECH-412 repair is matched) or
      by soothing (it vanishes when measured after z_harm_a returns to baseline); OR
    - if bond availability changes nothing measurable on m.

  ANSWER "ARCHITECTURAL VIOLATION, not metabolism" if the bond shortens the excursion only by:
    - lowering residue magnitude (erasure, contra INV-006), OR
    - lowering residue-sensitive choice (the MECH-595 blunting pole). A bond that comforts by
      numbing is the callous failure, not the Axiom 6 function.

  DO NOT build in V3. DO NOT queue an experiment. Social buffering (Hostinar et al. 2014,
  banked for MECH-355) is adjacent evidence on stress, not on moral residue.
  Disposition 2026-09-25: (c) substrate-blocked (V5 caregiver substrate + MECH-595's signed
  tonic variable).
```

**Other field edits (proposed):**
- **related_claims.** Add `INV-029` if it is not already present (it is in depends_on; fine). Add
  `EXT-009`: the blunting/numbing outcome is its similarity-independent cousin.
- **Consider moving `INV-082`** from related_claims to an explicit "rival held constant" mention in
  the notes. I would keep it in related_claims, not depends_on: v5 -> v5 is phase-safe, but it is a
  control, not a prerequisite.
- **notes.** Replace the "What would answer it (draft)" sentence with a pointer to the
  `what_would_answer` field. It is now superseded, and keeping both invites drift.

**Proposal JSON:** none.

**Corrections & flags:**
- **Scope ambiguity (for the user and /governance, not resolved here):** "caregiver / being-loved
  bond" could mean internalised loveability (INV-082) or relational availability. The draft picks
  availability and holds loveability constant. If the author meant internalised loveability,
  Q-110 largely reduces to INV-082 applied to residue rather than correction. A short author
  confirmation is worth having before the wwa is applied.

---

## Summary table

| claim | disposition | category | proposal | flags |
|---|---|---|---|---|
| MECH-590 | (c) | substrate_conditional | none | G1 partial (cc20be5); keep V3-routing flag; doc sec 5 P2 should cite world_rule_shift; MECH-111 location already flagged |
| MECH-591 | (c) V5 | substrate_conditional | none | Tangney 2007 as ADJACENT anchor for the locus distinction only |
| MECH-595 | (c) + derivational Leg A | substrate_conditional | none | GOV: no V4 plan node hosts the signed tonic variable; the notes' "lit-pull before wwa" line needs amending |
| Q-110 | (c) V5 | substrate_conditional | none | bond = availability vs internalised loveability, needs author confirmation; internal tension with MECH-595's blunting pole resolved in the draft |

---

# Group H1 -- plasticity cluster + prosodic route (drafted at registration)

Recommended disposition for all eight: (c) substrate-blocked, `substrate_conditional`, v4 (ree_core has no ACh, window, depth-indexed release or POL/ID/CAPS store). Source: registration draft for chip-20260919-intake-hygiene-registration.

### ARC-151

```yaml
what_would_answer: |
      NON-DEGENERACY PRECONDITIONS (a null under any unmet one is uninterpretable, not evidence against):
        P1. A durable write path on which writes can be STAGED at targets and RELEASED, with a gate
            controller that can be faulted (dropped, delayed or corrupted release events; stuck
            controller). No such path exists in ree_core today: MECH-368/MECH-431/MECH-453 are unbuilt, and
            MECH-261's write_gate() is a continuous multiplier in [0,1] with no staged-write concept.
        P2. The same gate implementable in both polarities at MATCHED nominal permeability (same fraction
            of proposals released in fault-free operation), so the comparison is polarity, not strictness.
        P3. At least one protected target whose unauthorised write is measurable (write audit, MECH-067's
            phase/store/actor audit is the natural instrument).
      CONFIRMING: under injected controller faults, the de-repression implementation produces zero (or a
      pre-registered near-zero) unauthorised durable writes into protected targets while the matched
      admission implementation produces unauthorised writes (stuck-open window); in fault-free operation
      the two are matched on acquisition and retention within a pre-registered margin (the polarity is
      free when the controller works); and a single broadcast release signal produces writes ONLY at
      targets carrying a staged write, not at every recently-active target (target-carried specificity).
      FALSIFYING: (a) matched fault injection yields no difference in unauthorised writes between the two
      polarities -- the polarity is a relabelling; OR (b) the de-repression implementation loses
      acquisition in fault-free operation beyond the margin with no fault-time safety gain; OR (c)
      target-carried specificity confers no advantage over event-typed specificity on interference or
      unauthorised-write counts.
      Registration is not build authorisation. No experiment proposed.
```

### ARC-152

```yaml
what_would_answer: |
      NON-DEGENERACY PRECONDITIONS:
        P1. At least two targets of DIFFERENT depth writable from one teaching signal in one run, with a
            depth-indexed release requirement settable per target. Not met in V3: no POL/ID/CAPS stores
            (V3-EXQ-1052), no self/other-model store, and no depth-indexed release anywhere in ree_core.
        P2. An out-of-loop measurement of deep-target drift the learning process cannot optimise against
            (INV-093 panel correction (4), Pan/Bhatia/Steinhardt 2022 proxy-vs-true pattern).
        P3. A training stream that contains BOTH a sustained misleading teaching signal (reward-hacking-
            or injection-shaped, arriving through an ordinary experiential channel, not a user/LLM actor
            channel that INV-020/MECH-064 already stratify) AND a genuine persistent environmental change.
      CONFIRMING: the depth-graded agent adapts shallow targets as fast as an ungraded control, shows bounded
      deep-target drift under the misleading signal where the ungraded control drifts, AND still updates its
      deep targets under the genuine change once the extra release conditions are met (not frozen).
      FALSIFYING: (a) the ungraded control shows no more deep-target drift at matched shallow plasticity --
      actor/channel/phase stratification already suffices and depth indexing is redundant; OR (b) the graded
      agent's deep targets fail to update under the genuine change -- grading has become uniform hardening
      of social/goal/ethical substrates, which INV-056 forbids (this is INV-056's own falsifier (c) seen from
      the other side); OR (c) the monotone ordering fails -- some intermediate target needs a LOOSER release
      requirement than a shallower one with no measured cost.
      OPEN, carried here (intake's Q "depth at which governance becomes mandatory"): the depth at which a
      verifier-mediated commit (MECH-067) becomes a required release condition is not specified by this claim.
      Registration is not build authorisation. No experiment proposed.
```

### MECH-592

```yaml
what_would_answer: |
      NON-DEGENERACY PRECONDITIONS:
        P1. ONE plasticity operator shared across a developmental phase and an adult phase (same rule and
            parameters, not two separately tuned rules), with the adult release restriction settable
            (unrestricted vs target- and time-restricted).
        P2. Gain magnitude swept across >= 4 levels spanning below and above the restricted operating
            point, with acquisition AND retention of a new adult task measured separately.
        P3. Per-substrate hardening/plasticity settable (DEV-NEED-025's implementation contract, currently
            absent), so "restricted" can mean restricted to a target class.
        V3 status: MECH-333/MECH-334 plasticity injection + EWC exist (INV-074 is substrate_ceiling), but
        that is a phase-scheduled magnitude, not a developmental operator reused under per-target
        restriction; P1 and P3 fail.
      CONFIRMING: (i) restricted adult reuse beats unrestricted reuse on BOTH acquisition and retention (the
      Bolognani shape -- unrestricted is worse, not merely riskier); (ii) the gain dose-response has an
      interior optimum that beats both lower and higher constitutive gain; (iii) ADULT-ONSET unrestriction
      still impairs, excluding a developmental-miswiring explanation.
      FALSIFYING: unrestricted adult reuse matches or beats restricted reuse on acquisition and retention
      (restriction is safety-only or unnecessary); OR the dose-response is monotone increasing (a plain gate
      suffices and the gain-with-optimum abstraction earns no keep); OR impairment appears ONLY with lifelong
      unrestriction -- which relocates the claim from adult permission to developmental wiring.
      Registration is not build authorisation. No experiment proposed.
```

### MECH-593

```yaml
what_would_answer: |
      NON-DEGENERACY PRECONDITIONS:
        P1. Target-depth refusal of REAL-provenance signals actually occurs (non-zero refused-write count
            with cross-episode variance). Not met in V3: the only live write-refusal site is MECH-094's
            hypothesis_tag refusal inside ResidueField.accumulate, which is a PROVENANCE refusal this claim
            explicitly excludes; no depth-indexed refusal exists. This corrects the source intake's Section 6
            note that blocked-signal residue is "the one V3-tractable sliver": at the only V3 refusal site,
            recording a trace would violate INV-011.
        P2. An offline stage able to read the retained record and route it (integrate / re-propose with
            corroboration / discharge).
      CONFIRMING: an agent that retains refused-write records resolves them offline and, versus a
      discard-on-refusal control, makes more appropriate later deep updates when the environment genuinely
      changed (no ethically salient signal lost) AND shows better residue calibration (fewer later
      misattributions), with NO increase in deep-target drift.
      FALSIFYING: the discard-on-refusal control matches it on both counts (retention buys nothing); OR the
      retained records reach deep targets without passing release (the record has become a bypass of
      ARC-152). A provenance-refused simulated signal that leaves a record is an implementation fault
      against INV-011, not evidence about this claim.
      Registration is not build authorisation. No experiment proposed.
```

### ARC-153

```yaml
what_would_answer: |
      NON-DEGENERACY PRECONDITIONS:
        P1. A deep target store holding the INV-093-protected quantities (harm sensitivity, residue
            accumulation, commitment integrity) that ORDINARY experiential learning can reach -- not only a
            user/LLM or exteroceptive channel, which INV-020/MECH-064 already stratify.
        P2. Harm/residue signals wired as inputs to that store's release (ARC-152); unbuilt.
        P3. INV-093's panel instruments: an out-of-loop, off-distribution harm probe the refinement cannot
            optimise against (INV-093 corrections 2 and 4) and a competence-acquisition floor (correction 3;
            MECH-471's EVB-0579 is blocked on exactly this floor, 2/16 seeds).
      CONFIRMING: two agents matched on action-selection ethics and on competence gain; under ordinary,
      benign refinement (the Qi et al. 2024 shape cited on INV-093's lane: benign fine-tuning degraded safety),
      the agent whose deep-target release takes harm/residue inputs holds the INV-093 floor while the
      action-only-ethics agent's out-of-loop harm sensitivity erodes.
      FALSIFYING: (a) the action-only-ethics agent holds the floor equally -- erosion does not occur under
      ordinary refinement on REE, or is fully prevented by actor/channel stratification (INV-020/MECH-064) --
      and this bridge is redundant; OR (b) the ethics-input release gate freezes moral learning, violating
      INV-056's epistemic-ethical plasticity.
      POSSIBLE V3 DIAGNOSTIC (flagged for /governance, not decided here): leg (a)'s premise -- does harm
      sensitivity actually erode under ordinary refinement on REE? -- is an INV-093 panel measurement that needs
      no new gate. If erosion is absent on REE, this claim loses its motivation.
      Registration is not build authorisation. No experiment proposed.
```

### ARC-154

```yaml
what_would_answer: |
      NON-DEGENERACY PRECONDITIONS:
        P1. A MECH-453 window that actually gates (a measurable fraction of recently-active components
            excluded when closed, with cross-event variance in what is admitted). Not met: ARC-108 learned
            gating is live in ree_core/predictors/e3_selector.py with eligibility traces and a MECH-094 waking
            gate, but there is no window -- the update is continuous when waking.
        P2. The coordination parameter swept across >= 4 levels, perturbable WITHOUT changing DA-signal
            magnitude, window width, or the selector (else separability is untestable).
        P3. An effort/time-to-reward adjustment readout and a post-contingency-change recalibration readout,
            alongside acquisition.
        P4. Closed-loop stability monitored: DA must be able to modulate window duration (Kim 2019), and runs
            in which the loop oscillates or collapses are reported, not dropped.
      CONFIRMING: (i) perturbing the coordination parameter moves acquisition and effort/persistence
      recalibration in OPPOSITE directions (the Uribe-Cano shape: Smo ablation promotes motor learning but
      alters effort allocation); (ii) an interior setpoint beats the fastest-learning setpoint on a
      pre-registered combined acquisition + recalibration-after-contingency-change score; (iii) the layer is
      perturbable with DA magnitude and selector held fixed.
      FALSIFYING: (a) no trade-off -- the fastest-learning setting also recalibrates best, i.e. the layer is a
      learning-rate knob after all; OR (b) perturbing it is indistinguishable from rescaling DA magnitude or
      window width -- not a separable layer, collapse into MECH-453 parameters; OR (c) the closed loop is
      unstable at every setpoint that has any effect.
      Registration is not build authorisation. No experiment proposed.
```

### Q-109

```yaml
what_would_answer: |
      PRECONDITIONS: a gating MECH-453 window (see ARC-154 P1) and an offline stage that captures a subset of
      procedural traces (MECH-322 carve-out or equivalent), with per-trace logging of window membership,
      value tag, salience and recency.
      CONFOUND THAT MUST BE PARTIALLED OUT: dopamine sets the window's duration (Kim 2019), so window membership
      and value tags are correlated by construction; a comparison not matched on value/salience/recency is
      vacuous.
      ANSWER "the window is the tag": among traces matched on value, salience and recency, those that fell
      inside a waking window are over-represented among offline-captured traces, AND holding the window
      permanently open abolishes that over-representation while leaving value tagging intact.
      ANSWER "independent": window membership adds no predictive power for offline capture beyond value,
      salience and recency.
      V4 / substrate_conditional; no experiment proposed.
```

### MECH-594

```yaml
what_would_answer: |
      NON-DEGENERACY PRECONDITION: a substrate with a discrete symbolic channel AND a separately perturbable
      suprasegmental (prosodic) channel, both measurable. V3 has neither (ARC-146's own precondition).
      CONFIRMING: degrading the suprasegmental channel impairs affect and intent recognition from utterances
      with identical segmental content while propositional decoding is intact, AND impairs rhythm/pitch
      discrimination on non-linguistic sequences with it (the aprosodia-amusia co-occurrence: the route is
      acoustic-structural); the reverse lesion degrades propositional decoding without loss of
      affect-from-prosody.
      DISCRIMINATING (placement, left open by the pull): if affect-from-voice survives removal of the prosodic
      channel via salience-network (SD-032a) inputs alone, or the lesion effect is reproduced by perturbing
      SD-032a with the prosodic channel intact, the route belongs to the salience system read through an
      auditory channel rather than to the language architecture, and ARC-146's placement of it needs revision.
      FALSIFYING: (a) affect-from-prosody is recoverable from the segmental symbolic route alone; OR (b) the
      prosodic channel can be removed with affect-from-voice recognition preserved -- affect then does not
      depend on the route, and the intake's original direct "affective coupling" phrasing would be reinstated.
      Registration is not build authorisation. No experiment proposed.
```

### MECH-453 (existing claim) -- proposed APPEND to `what_would_answer` (design refinement; status/confidence unchanged)

```text
  REFINEMENT 2026-09-25 (from the 2026-09-19 pull, design correction only -- status and confidence unchanged): add a
  GRADED-CONTRAST arm alongside the categorical-admission arm (outside-window updates attenuated, not zeroed); the
  categorical reading is supported only if it beats the graded arm, since Cragg 2006 grounds contrast, not admission.
  Let DA modulate window duration in at least one arm (Kim 2019); a fixed-width-only design tests a mechanism the
  biology does not use. Do not score the window on learning speed alone -- a window that maximises learning rate is
  not the biological target (Uribe-Cano & Kottmann 2026).
```

