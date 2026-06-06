# Endogenous parasympathetic recovery / autonomic rebound -- lit-pull verdict

**Date:** 2026-06-06
**Question (a):** Is endogenous autonomic rebound / active parasympathetic recovery a
mechanistically distinct system worth a separate REE claim, or is it reducible to
(i) the passive MECH-219 `z_harm_a` `recovery_rate`, (ii) social soothing MECH-355, or
(iii) relief MECH-302?
**Question (b):** Smallest computational form + trigger -- is offset-detection (the `z_harm_a`
derivative going negative, the same signal MECH-302 relief detects) the right driver for a
transient boost to the MECH-219 `recovery_rate` / SD-032e `drive_bias` leak, with NO conspecific
and NO safety-prediction?
**Question (c):** V3-tractable scope confirmation.
**Feeds:** a candidate-claim registration decision (gated; NOT executed this session).
**Routing source:** `evidence/planning/mech_355_soothing_update_rule_and_scope_design_2026-06-05.md`
section 3.2 ("the parasympathetic-poor asymmetry"), which surfaced this sibling and gated it on
its own lit-pull.
**Failure mode guarded:** `feedback_biology_before_formal_definitions` -- do not register a
formal "recovery" mechanism that is really passive decay, relief, or social soothing under a new
name (the SD-010 -> SD-011 / SD-003 philosophy-right/mechanism-wrong trap).
**Source:** According to PubMed (4 entries, DOIs in each record). PubMed MCP available this
session; no web fallback needed.

---

## Headline

**(a) YES -- distinct, and registerable, with one important architectural nuance.** Active
parasympathetic recovery ("vagal rebound") is empirically dissociable from the passive decay of
the stress signal: it is a *sharp parasympathetic surge at stressor offset that occurs while
sympathetic drive is still elevated* (Mezzacappa 2001), driven by an *endogenous central
(prefrontal-vagal) system* (Thayer & Brosschot 2005), with its *own state-conditioned kinetics*
(Cunha 2015). It is NOT relief (relief is a reinforcement readout; rebound is the recovery process
itself) and NOT safety (no prediction over a horizon). The nuance: rebound and social soothing
(MECH-355) **converge on the same recovery variable** -- emotional support modulates vagal rebound
(Tung 2021) -- so the two are dissociable by **trigger** (internal offset vs conspecific), **not by
effector**. This validates, rather than undercuts, the design-pass recommendation: register the
endogenous rebound as a **sibling** of MECH-355 that shares the recovery target, not a fold-in and
not a duplicate. Confidence **0.74**.

**(b) YES -- offset-detection is the biology-correct trigger; smallest form is a transient,
state-scaled multiplier on the recovery side.** The canonical rebound fires "in the first minute of
recovery" -- i.e. at stressor offset (Mezzacappa 2001), which is exactly the `z_harm_a`-derivative-
negative event. Recovery has a tunable, baseline-conditioned *rate*, not an instantaneous reset
(Cunha 2015), so the minimal form is an offset-triggered transient boost to the MECH-219
`recovery_rate` and the SD-032e `drive_bias` leak, scaled by current accumulator/drive state. No
conspecific, no safety-prediction. **Shared-trigger note:** offset is the same event MECH-302 relief
consumes -- this is a feature: one upstream offset event fans out to a *reinforcement readout*
(relief) and a *recovery-rate boost* (rebound), distinct outputs from a shared trigger.

**(c) V3-tractable: confirmed.** Trigger (`z_harm_a` derivative) and both targets (MECH-219
`recovery_rate`, SD-032e `drive_bias` leak) already exist in V3; the central-driver framing
(Thayer CAN) maps onto REE's existing precision/PFC-analog control (ARC-016 / SD-033a) but the
minimal V3 form needs none of that.

---

## The reducibility test (question a, worked)

| Reduce rebound to... | Verdict | Decisive evidence |
|---|---|---|
| **(i) passive MECH-219 `recovery_rate`** | NO -- not reducible | Mezzacappa 2001: vagal rebound rises *above baseline* and *despite still-elevated sympathetic drive*. Passive decay cannot produce an above-baseline overshoot while the stress side is still up; an active recovery process is required. Cunha 2015: the recovery rate is itself state-conditioned, not a fixed constant. |
| **(ii) social soothing MECH-355** | NO -- but they share the target | Tung 2021: emotional support *modulates* vagal rebound -- so social input is one driver of the recovery variable, but rebound is modelled as its own slope and fires endogenously at offset (Mezzacappa). Dissociable by trigger (internal offset vs conspecific), shared effector. |
| **(iii) relief MECH-302** | NO -- shared trigger, different output | Both are offset-triggered, but relief is a *reinforcement teaching signal* (writes value at the offset); rebound is the *autonomic recovery process* (speeds return-to-baseline). Different computational role; Thayer/Mezzacappa describe a regulatory restoration, not a reinforcer. |

**Conclusion:** the construct survives all three reduction attempts. It is a fourth, distinct member
of the offset/recovery neighbourhood: relief (reinforce the offset) / safety (predict absence) /
soothing (social down-regulation of present state) / **rebound (endogenous active recovery of
present state)**.

---

## Smallest computational form (question b)

Let `R(t) in [0,1]` be the endogenous-rebound drive.

- **Trigger:** offset-detection on the agent's own suffering trajectory -- `R(t)` rises when
  `d||z_harm_a||/dt < 0` (the SufferingDerivativeComparator signal MECH-302 already computes),
  optionally gated to fire only after a supra-threshold episode (so trivial fluctuations do not
  trigger it). NO conspecific input; NO predictive/safety input.
- **Effect (identical update rule to MECH-355 soothing -- decay-acceleration):**
  - MECH-219: `recovery_rate_eff = recovery_rate * (1 + nu_R * R)` (recovery side only; onset
    untouched -> a recovering agent still detects a fresh injury at full sensitivity).
  - SD-032e: `drive_bias *= (1 - leakR * R)` per waking tick (the active waking analog of the
    dormant `offline_decay` hook -- same negative-relaxation direction the cap permits).
- **State-scaling (load-proportionality, from Cunha + the MECH-355 design pass):** because the rule
  is multiplicative on existing accumulated state, `R` has zero effect on a calm agent -- inheriting
  the soothing design's "recovery != sedation" guarantee. Optionally scale `R` by current
  `||z_harm_a||` so the boost is largest exactly when there is most to recover from.
- **Never writes:** SD-012 base `drive_level` (a recovered agent is still hungry), `z_harm_s`
  (SD-010), `z_harm_un` (SD-019a) -- same nociceptive-detection-preserving discipline as MECH-355.
- **Transient:** `R(t)` decays back to 0 over a short window after offset (Mezzacappa's "first
  minute" -> a brief post-offset boost, not a standing change).
- **MECH-094:** waking-stream only; an offset detected during replay/simulation
  (`hypothesis_tag=True`) must not trigger rebound.

This is deliberately the **same effector/update rule as MECH-355** (decay-acceleration on the
recovery side of the two slow accumulators); only the **trigger** differs (endogenous offset vs
conspecific). That is the Tung-2021 "one recovery variable, multiple inputs" structure rendered as
two sibling claims.

---

## V3 scope (question c)

Fully V3-tractable. The trigger reuses the MECH-302 SufferingDerivativeComparator's offset signal;
the targets are live V3 parameters (MECH-219 `recovery_rate`, SD-032e `drive_bias` leak, with the
negative-relaxation direction already permitted by the SD-032e cap but never reached by the live
tick). The Thayer-CAN central-driver story maps onto ARC-016 precision / SD-033a lateral-PFC if a
richer version is ever wanted, but the minimal form needs none of it. This is the V3-side complement
that closes REE's **sympathetic-rich / parasympathetic-poor asymmetry** (dense escalation:
MECH-219 onset, SD-032e accumulation, SD-037 orexin override, MECH-091 urgency, MECH-279 PAG freeze;
thin recovery: only passive `recovery_rate` + offline-only `drive_bias` decay).

---

## Distinct-from grid (carry into claims.yaml at registration)

| Neighbour | Time ref | Role | How rebound differs |
|---|---|---|---|
| **MECH-355 soothing** | present | state-gain recovery modulator | SAME effector/update rule; trigger is ENDOGENOUS offset, not a conspecific. Sibling, not fold-in. |
| **MECH-302 relief** | past (at offset) | reinforcement teaching signal | SHARED trigger (offset); rebound's output is recovery-rate boost, relief's is a value write. |
| **MECH-303/304 safety** | future | learned inhibitory predictor | rebound makes no prediction; acts on present accumulated state. |
| **MECH-219 passive recovery** | present | leaky decay | rebound is an ACTIVE, offset-triggered, transient boost ON TOP of the passive rate (Mezzacappa overshoot). |
| **SD-032e pACC accumulation** | present (slow) | autonomic sensitisation (write) | rebound is the LEAK/recovery side of the same `drive_bias`; SD-032e is the accumulation side. |
| **MECH-112 wanting** | -- | appetite | orthogonal. |

---

## Confidence components

- **Distinctness from passive decay:** high (Mezzacappa's above-baseline overshoot during
  residual sympathetic activation is decisive).
- **Endogenous-central-driver existence:** high as framing (Thayer & Brosschot canonical), moderate
  as direct test (it is a review).
- **Sibling-not-fold architecture:** high (Tung's support-modulates-rebound result is the exact
  shared-variable/distinct-trigger evidence).
- **Smallest-form / rate parameterisation:** moderate (Cunha solid on kinetics, but exercise-
  recovery transfer risk).
- **Net:** 0.74. The distinctness verdict is secure; the residual uncertainty is that no single
  paper isolates an endogenous, *non-social*, *aversive*-stressor rebound in one design (Mezzacappa
  is aversive + endogenous but cardiac; Tung is aversive but social; Cunha is endogenous but
  exercise). The convergence across the three covers the claim, but a clean single-paradigm
  isolation would raise confidence further.

---

## Recommendation (gated -- NOT executed this session)

1. **Register a candidate sibling claim** -- proposed `MECH-356`
   (`affect.endogenous_parasympathetic_recovery_autonomic_rebound` or similar). Status `candidate`;
   `implementation_phase: v3`; `v3_pending: true`; `epistemic_category: standard` (V3-tractable, so
   it earns experimental gating -- unlike MECH-355's `substrate_conditional`). `depends_on:`
   MECH-219, SD-032e, MECH-302 (shares its offset trigger), SD-011; `distinct_from:` MECH-355,
   MECH-302, MECH-303, MECH-304, MECH-112. Mirror the MECH-302 lit-pull precedent
   (`claim_type: mechanism_hypothesis`, `location ->` this verdict). **Do NOT fold into MECH-355.**
2. **Add an Extension-Register row** to `docs/architecture/affect_primitives.md` (V3-minimal,
   offset-triggered) explicitly cross-linked to the MECH-355 soothing row as its endogenous sibling
   that shares the recovery target.
3. **Smallest V3 experiment** (after registration, via `/queue-experiment`): drive a supra-threshold
   `z_harm_a` episode then release it; measure that rebound-ON returns `z_harm_a`/`drive_bias` to
   baseline faster than rebound-OFF, with **onset/peak unchanged** and **zero effect on a
   never-stressed control** (the load-proportionality falsifier) and **no conspecific present** (the
   MECH-355 confound control).
4. **Keep MECH-355 unchanged** -- it stays the V4-social, conspecific-gated claim
   (`substrate_conditional`). The two share an effector and differ by trigger.

## What this pull does NOT settle

- The exact `nu_R` / `leakR` magnitudes and the post-offset transient window length (Q-style
  calibration sweep, not lit).
- Whether the richer central-driver version (routing rebound through ARC-016 precision / SD-033a
  PFC-analog per Thayer CAN) is worth building beyond the minimal offset-triggered form -- defer
  until the minimal form is validated.
- Whether rebound and MECH-355 soothing should eventually be ONE module with two trigger inputs
  (engineering consolidation) vs two modules -- a post-validation refactor question, not a
  registration-time one.

## Cross-references
- `evidence/planning/mech_355_soothing_update_rule_and_scope_design_2026-06-05.md` (the design pass
  that surfaced this sibling; section 3.2 + section 5 "surfaced sibling").
- `claims.yaml`: MECH-355 (soothing, V4-social sibling), MECH-219 (recovery_rate target),
  SD-032e (drive_bias leak target), MECH-302/SD-050 (shared offset trigger + relief dissociation),
  MECH-303/304 (safety dissociation), SD-011/SD-019a/SD-019b (the harm streams), MECH-091 (urgency
  interrupt -- downstream beneficiary of faster z_harm_a decay), MECH-094 (waking-only write gate).
