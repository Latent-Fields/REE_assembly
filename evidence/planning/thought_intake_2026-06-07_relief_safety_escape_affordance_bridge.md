# Thought intake: relief/safety escape-affordance bridge for avoidance learning

**Date:** 2026-06-07  
**Status:** thought intake / failure-autopsy candidate. Not a claim cluster yet.  
**Origin:** user asked whether REE has aversion/flee wiring, and whether an organism needs to learn relief from terror to learn to approach escape. Prompted by V3-EXQ-603h partial signal: intact SD-058/MECH-357 gate appears to engage/suppress freeze, but early Stage-H survival still fails.

**Related artifacts:**

- `docs/architecture/sd_058_instrumental_avoidance_acquisition.md`
- `experiments/v3_exq_603h_instrumental_avoidance_stageh_validation.py` in `ree-v3`
- `docs/architecture/affect_primitives.md` rows: MECH-302 Relief, MECH-303/304 Safety, MECH-353 blocked-agency, MECH-354 fatigue, MECH-356 autonomic rebound
- `evidence/literature/targeted_review_hazard_avoidance_learning/`
- `evidence/planning/failure_autopsy_V3-EXQ-603g-624c-651a_2026-06-07.md`

---

## 1. Core hypothesis

REE currently has pieces of threat, freeze, reflexive escape, relief, safety, and instrumental avoidance, but they may not yet be coupled into an **escape-affordance bridge**.

Working hypothesis:

> Avoidance learning may require not only aversion and freeze-suppression, but a circuit-level reinforcement bridge in which a directed action that reduces aversive state becomes tagged as an escape affordance: `threat high -> action reduces z_harm_a / terminates threat cue -> phasic relief + learned safety -> action/location/policy becomes approachable under future threat`.

This is **not** a claim that conscious terror or conscious relief are necessary. The modern LeDoux/Moscarello avoidance literature explicitly cautions that subjective fear/relief/hope may occur but are not the causal mechanism of avoidance learning. The relevant implementation target is circuit-level reinforcement from threat removal and/or safety acquisition.

---

## 2. Literature check verdict

Key literature points from quick pass:

1. **Avoidance is survival-relevant and active avoidance is action, not merely freezing.** LeDoux, Moscarello, Sears & Campese (2017, Molecular Psychiatry) define active avoidance as learning to prevent/minimise aversive events by action. They separate defensive reactions (e.g. freezing), defensive actions (avoidance), and defensive habits.
2. **Old two-factor theory framed avoidance as fear reduction / relief.** Mowrer/Miller theory treated Pavlovian fear reduction as the reinforcer for instrumental avoidance.
3. **Modern reconceptualisation: the reinforcer is not subjective relief, but circuit-level outcomes.** LeDoux et al. argue that negative reinforcement from threat removal and positive reinforcement from safety cues are complementary contributors to avoidance learning; subjective fear, hope, relief may occur but are not the cause of learning.
4. **Escape-from-threat paradigms show CS termination can reinforce instrumental learning.** A subject can learn to act to terminate a threat-predictive conditioned stimulus even when the unconditioned shock never occurs in that chamber.
5. **Safety signals may positively reinforce avoidance.** Response-produced safety cues / conditioned inhibitors can become the thing approached; avoidance of danger and approach to safety are necessarily entwined.
6. **Circuit hint: action pathway likely needs ventral striatal / nucleus accumbens bridge.** LeDoux et al. summarise avoidance action as involving an LA/BA -> NAcc pathway, with infralimbic prefrontal cortex suppressing CeA/PAG freezing so movement can occur.
7. **Human work is broadly consistent.** Boeke, Moscarello, LeDoux, Phelps & Hartley (2017, Journal of Neuroscience) are cited as showing active avoidance can attenuate Pavlovian conditioned responding in humans, with imaging implicating amygdala, nucleus accumbens, medial prefrontal cortex and striatal/habit circuitry.

REE translation:

- `MECH-279` / PAG freeze = defensive reaction.
- `SD-058` / `MECH-357` ilPFC analogue = freeze suppression + avoidance action-bias + efficacy learning.
- `MECH-302` Relief = phasic aversive-offset reinforcement.
- `MECH-303/304` Safety = learned predictor of threat absence.
- Missing candidate bridge = relief/safety-produced **escape-affordance tagging** into E3/action selection under threat.

---

## 3. Why this matters for 603h

V3-EXQ-603h tests whether adding SD-058/MECH-357 is sufficient to make the Stage-H hazard-avoidance survival leg train. The early heartbeat pattern was:

- lesion arm: PAG freeze active, no gate, fails as expected;
- intact arm: gate engages and suppresses freeze, but first visible Stage-H checkpoint still fails survival.

If final 603h outcome is:

| Outcome | Interpretation |
|---|---|
| readiness unmet | retune threat/PAG/gate engagement; this thought is not yet load-bearing |
| PASS | SD-058/MECH-357 sufficient; keep this bridge as later refinement only |
| gate engaged + G_H fails | SD-058 suppresses freeze but does not create enough approach-to-escape; route this thought as a candidate failure-autopsy branch |

The critical diagnostic is **engaged-but-insufficient**: if `n_credit+n_decay>0` and `n_freeze_suppressed>0`, but `G_H_INTACT < 2/3`, then REE may have learned to twitch away from freeze without learning that a particular action/location/policy is a relief/safety affordance.

---

## 4. Proposed computational bridge

Minimal candidate mechanism, if needed:

```
under threat:
  if action a_t causes d(z_harm_a)/dt < 0 or terminates threat-predictive cue:
      emit phasic relief tag r_relief_t  (MECH-302-consistent)
      update escape_affordance[action/location/policy] += relief_credit
      update safety_predictor[action/location/context] += threat_absence_credit  (MECH-303/304-consistent)

future threat:
  E3 score receives bounded approach bonus toward escape_affordance
  freeze/no-op suppression receives stronger learned-efficacy support
  action selection is biased toward 'go there / do that because harm falls there'
```

Design discipline:

- This should **not** directly increase generic wanting for food/resource.
- It should be **threat-context gated**: escape affordance is attractive under threat, not globally appetitive.
- It should be **bounded** so it does not create pathological avoidance/habit loops.
- It should remain distinct from reflexive escape (`SD-037` / `MECH-281`) and from generic relief (`MECH-302`) or safety (`MECH-303/304`) rows.
- It should use circuit-level reinforcement language, not subjective-terror language.

Potential row name if promoted:

- `escape_affordance_bridge`
- `relief_safety_avoidance_bridge`
- `threat_relief_action_credit`

Candidate dependencies:

- SD-011 / SD-019 / MECH-219: aversive load state (`z_harm_a`)
- MECH-279: freeze reaction to suppress
- SD-058 / MECH-357: instrumental avoidance gate
- MECH-302: phasic relief / aversive-offset reinforcement
- MECH-303/304: learned safety predictor / conditioned inhibition
- E3 selection authority / bounded modulatory score-bias machinery

---

## 5. Smallest discriminative test

If 603h fails with gate engaged, queue a narrow diagnostic before broad rewiring:

**Proposed experiment:** `V3-EXQ-603i_relief_safety_escape_affordance_bridge`

Arms:

1. `ARM_BASE_IA_ONLY`: SD-058/MECH-357 exactly as 603h intact.
2. `ARM_RELIEF_BRIDGE`: IA + relief credit from negative `d(z_harm_a)/dt` to the last directed action/location.
3. `ARM_SAFETY_BRIDGE`: IA + learned safety predictor for action/location/context after threat absence.
4. `ARM_RELIEF_SAFETY_BRIDGE`: both.

Acceptance:

- readiness: PAG freezes in lesion/control; IA gate engages; relief/safety bridge fires non-vacuously;
- primary: `G_H >= 2/3` and `G_H` improves over `ARM_BASE_IA_ONLY`;
- secondary: P1 survival transfer improves without pathological over-avoidance / no-resource starvation;
- safety guard: bridge bonus must be threat-context bounded and must not globally swamp food/goal approach.

Interpretation:

- Relief-only pass: missing phasic negative-reinforcement credit.
- Safety-only pass: missing learned threat-absence predictor / conditioned inhibitor.
- Both required: avoidance requires complementary relief + safety bridge.
- Neither helps: deeper motor/trajectory or survival affordance representation gap remains.

---

## 6. Routing verdict

Do **not** implement immediately before 603h completes. But if 603h final outcome is **gate engaged + G_H failure**, treat this thought as a high-priority failure-autopsy branch: REE may not be missing aversion or flee; it may be missing the bridge that makes an escape affordance become attractive under threat.

One-line goblin version:

> The toddler may not need more terror. It may need the felt/circuit-level discovery that *there is a way out*, and that moving toward the way out is what makes terror fall.
