---
nav_exclude: true
---

# Thought Intake: Context Inference as an Active, Persistent Control Process

**Raw thought file:** `docs/thoughts/2026-08-19_context-inference-active-persistent-control.md`
**Session:** thought-intake-20260819-fresh, 2026-08-20
**Status:** processed, claims registered (MECH-493, MECH-494, Q-094)
**Sibling intake:** `evidence/planning/thought_intake_2026-08-19_hippocampal-episodic-organisation.md`
(the two raw thoughts were captured together and the second explicitly cross-references this one;
they should be read as a pair)

---

## Verbatim prompt

See `docs/thoughts/2026-08-19_context-inference-active-persistent-control.md` for the full text.

Core proposition, condensed: ContextMemory should not be treated as passive nearest-match
lookup. The operative question is not "which stored context looks most similar?" but "which
latent situation best explains what is happening, and is the evidence strong enough to justify
changing the currently active interpretation?" That reframing implies a set of coupled
functions -- explanatory-fit assessment, uncertainty over competing contexts, epistemic-deficit
detection, active orienting for discriminating evidence, candidate comparison, **hysteresis**,
an **exploitation window**, and a new-context-formation criterion -- arranged as a loop
(active context -> prediction/behaviour -> mismatch -> uncertainty -> orienting -> candidate
comparison -> retain/switch/create -> temporary commitment to action) that spans existing
modules rather than requiring a new executive one.

---

## What's New vs. Existing REE Docs (novelty table)

| Existing claim/doc | What it already covers | What this thought adds |
|---|---|---|
| **MECH-482** (`epistemic_deficit` accumulator) | A persistent, target-bound accumulator for unresolved, consequential, potentially-resolvable model inadequacy; explicitly distinguished from raw novelty (MECH-314a), raw uncertainty (MECH-314b), transient PE, and learning-progress (MECH-314c). Rises with importance x uncertainty x expected_resolvability x persistence. | Nothing new on the deficit signal itself -- this thought **consumes** MECH-482 rather than extending it. What is new is binding that deficit to a **specific arbitration target** (which latent context is active) rather than to a general information need. MECH-482 is target-bound but its targets are objects/questions, not the context variable. |
| **MECH-483** (orient/survey regime) | A third primitive behavioural regime alongside approach/avoid: diffuse, precedes cue identification, driven by accumulated `epistemic_deficit`. Its own pre-registered falsifier already worries about "orienting fires constantly (no informational gating)". | MECH-483 treats constant orienting as a **test artifact to be excluded**. This thought elevates the same phenomenon to a **design requirement with a named pathology**: a sufficiently uncertainty-sensitive agent becomes *permanently epistemic* -- continuously checking, rarely acting -- and the architecture must therefore contain a positive termination-and-protection mechanism, not merely avoid triggering spuriously. The exploitation window is the proposed mechanism; MECH-483 has no such construct. |
| **MECH-150** / **MECH-153** (E1 ContextMemory cue-indexed retrieval; supervised-training requirement) | ContextMemory implements soft-attention retrieval (query_proj + key_proj + output_proj) over a 16-slot bank; **queried with `z_world` alone, deliberately NOT the full `[z_self, z_world]` state** (MECH-150 title and rationale, "terrain weighting"). MECH-153 records that without a supervised context-labeling objective the representations stay near-identical (cosine_sim ~= 1.0), leaving the retrieval pathway functionally silent. | Two additions. **(a)** The retrieval **policy** is at issue, not just its training: nearest-match over stored keys is not the same operation as "which latent situation best explains observations *and their action consequences*". **(b)** The thought's final open question **directly contradicts MECH-150's z_world-only design decision** by asking whether the active context should include internal variables (current goal, bodily state, confidence, inferred social situation). That is a live, named design decision being challenged, not a gap -- registered as Q-094. |
| **MECH-288** (event segmenter) | A two-level hierarchical boundary detector emitting monotonic `outer.inner` segment IDs: PE-threshold on the fast scale (`z_world`+`z_self`), BOCPD-Gaussian latent change-point on the slow scale (`z_goal`). Already carries a persistence/change-point notion rather than raw-PE thresholding on the slow scale. Substrate exists (`ree_core/hippocampal/event_segmenter.py`). | MECH-288 produces **region keys for downstream consumers** (MECH-269 anchor sets, per-region V_s, MECH-284 staleness, MECH-287 broadcast trigger). It is a segmentation signal, not a **context-arbitration criterion**: nothing consumes its boundaries to decide retain-vs-switch-vs-create over stored contexts. This thought supplies the missing consumer, and sharpens the criterion with a term MECH-288 does not have -- explanatory failure over **action consequences**, not only over observations. Registered as MECH-494. |
| **MECH-106** / **MECH-047** / **MECH-105** family (commitment hysteresis, switching costs, asymmetric de-commitment) | REE has a well-developed hysteresis account -- `theta_high`/`theta_low`, dwell time, release/switch cost, asymmetric de-commitment on harm, explicitly framed as preventing pathological flip-flopping. Pre-commitment mode manager commits with hysteresis and switching costs (MECH-106). | All of this is hysteresis on the **action/mode commitment** variable. **Nothing applies commit-semantics to the CONTEXT variable.** This is the single largest structural gap the thought identifies: REE already knows how to make a commitment sticky and how to price a switch, and has simply never applied that machinery one level up, to the question of which situation the organism believes it is in. The thought's contribution is largely a **transfer** of an existing, validated REE pattern to a new variable -- which makes it unusually cheap to specify. Registered as MECH-493. |
| **ARC-062** (rule-apprehension weak reading: gated-policy architecture) | At least two policy heads sharing encoder features but receiving different gating from a **learned context discriminator** (e.g. reef-context vs open-context heads). The nearest existing thing to an explicit context variable with behavioural authority. | ARC-062's discriminator is a **soft, continuous, per-step gate** trained end-to-end. It has no dwell, no switch cost, no hysteresis, no exploitation window, and no create-new-context branch -- it cannot *hold* a context against transient evidence because holding is not represented anywhere in it. The thought is therefore not a competitor to ARC-062 but a statement about what ARC-062's gate would need in order to behave like an organism's context rather than a mixing weight. |
| **MECH-309** (monomodal policy collapse as the equilibrium without a rule-apprehender) | Without a non-Bayesian rule-creator proposing discriminative policy modes, the trainer collapses to the smoothest single regime good-enough across the whole state space. Monostrategy is the predicted output, not a bug. | Load-bearing caveat rather than novelty: **a context-arbitration loop built on top of a substrate that has already collapsed to monostrategy may show no behavioural benefit for reasons unrelated to whether the loop is correctly specified.** Any experiment against MECH-493/494 must either use the ARC-062 gated-policy substrate or pre-register MECH-309 collapse as an alternative explanation of a null. |
| **MECH-395** (pre-approach orienting/survey mode) | Cue-triggered, need-gated active sensing entered when directional/affordance confidence is too low; samples gradients until a directional vector stabilises, then exits to approach. **Has a termination criterion and an exit** -- the closest existing analogue to the exploitation window. | MECH-395's stabilise-then-exit is per-cue and per-approach-episode; it terminates orienting for **one directional decision**, and does not protect a subsequent action window from re-entry. The thought asks for termination plus **protection**: once a context is selected, inference is not merely finished but held closed for long enough to act on. |

**Net assessment.** Most individual legs of the proposed loop already exist in the registry as
separate, independently-motivated claims -- and several are already built
(`event_segmenter.py`, ContextMemory's attention path, the commitment-hysteresis family).
The genuinely new content is **three things, in decreasing order of confidence**:

1. **Context selection is itself a commitment-bearing act** and should inherit REE's existing
   commitment machinery (hysteresis, switch cost, protected dwell). This is a transfer of a
   validated in-repo pattern to a new variable, which is why it is the strongest of the three.
2. **The switch criterion is persistent structured explanatory failure over observations AND
   their action consequences**, explicitly not unsigned prediction-error magnitude -- with
   startle, noise, gradual drift and genuine latent transition required to dissociate.
3. **The active-context contents question** (internal state vs sensory scene identity), which
   is a direct challenge to MECH-150's standing z_world-only design decision.

The loop diagram as a whole is **framing, not a new module**, and the thought says so itself.
It should not be registered as an architectural commitment.

---

## Key formulations

**The loop (thought's own):**

```
active context -> prediction/behaviour -> mismatch -> uncertainty
  -> orienting/information acquisition -> candidate-context comparison
  -> retain/switch/create -> temporary commitment to action -> (back to active context)
```

**The bidirectional persistence requirement.** Stated explicitly in the raw thought and easy to
lose: context must not be abandoned too easily, *and* once selected the organism needs
uninterrupted time to exploit it. These are two different failure modes with two different
fixes (a switch threshold vs a protected window), and conflating them is how an architecture
ends up with only one of them.

**The named pathology:** *permanently epistemic* -- "continuously checking, rarely acting."
This is the falsifier-side of the exploitation window and is what makes MECH-493 testable in
the harmful direction as well as the beneficial one: adding uncertainty-sensitivity and
orienting without hysteresis should be **predicted to produce indecision**, not merely to fail
to help.

**The switch criterion:** not `|PE| > threshold`, but *persistent, structured evidence that the
currently inferred latent situation no longer explains observations or their action
consequences*. Three dissociating controls follow directly: transient surprise (high PE, should
NOT switch), gradual drift (low instantaneous PE, may warrant update-in-place rather than
switch), abrupt context change (should switch).

---

## Affected existing claims

- **MECH-150** -- its z_world-only ContextMemory query is directly challenged by Q-094. No
  change made to MECH-150; the challenge is registered as an open question against it, and
  MECH-150 is listed in Q-094's `depends_on`.
- **MECH-483** -- gains a named pathology (permanently-epistemic) and a proposed positive
  termination mechanism it currently lacks. Cross-referenced, not modified.
- **MECH-288** -- gains a consumer for its boundaries. Cross-referenced, not modified; note
  that MECH-494's criterion is strictly stronger than MECH-288's slow-scale BOCPD (adds the
  action-consequence term).
- **ARC-062** -- its context discriminator is the natural V3 host for a hysteresis/dwell
  wrapper. Cross-referenced.
- **MECH-106 / MECH-047** -- the source pattern being transferred. Cross-referenced.
- **MECH-309** -- pre-registered alternative explanation for a null result.

No existing claim's status, confidence, or text was changed by this intake.

---

## Candidate claims (REGISTERED)

- **MECH-493** -- context inference as an active, hysteresis-bearing arbitration loop with a
  protected exploitation window. `mechanism_hypothesis`, status `candidate`,
  `epistemic_category: substrate_conditional`, phase v3.
- **MECH-494** -- the context-switch criterion is persistent structured explanatory failure
  over observations and their action consequences, not unsigned prediction-error magnitude.
  `mechanism_hypothesis`, status `candidate`, `epistemic_category: standard`, phase v3.
- **Q-094** -- should the active context representation include internal variables (current
  goal, bodily state, confidence, inferred social situation), or is MECH-150's `z_world`-only
  query correct? `open_question`, status `open`.

---

## Next steps

1. **Do not queue an experiment yet.** MECH-493's falsifier needs the perceptually-similar /
   opposing-policy environment pair the raw thought describes, and the 2x2 design in the
   sibling intake is the better-specified version of the same substrate need. Build the
   environment once, for both.
2. **Precondition check before any run:** MECH-309 monostrategy collapse and MECH-153's
   undifferentiated-ContextMemory finding are both live and would each independently produce a
   null. A run that does not either use the ARC-062 gated-policy substrate or pre-register both
   as alternative explanations is not worth the compute.
3. **Targeted literature pull** on latent-state inference and context arbitration -- hidden
   Markov / change-point formulations of context switching, hysteresis in perceptual decision
   and bistable perception, and the exploration-exploitation dwell literature. The dissociation
   the thought asks for (startle vs drift vs true transition) has an established experimental
   vocabulary worth importing rather than reinventing.
4. **Q-094 is answerable cheaply and should go first.** Whether `z_self` belongs in the
   ContextMemory query is a substrate question testable against the existing bank without any
   new environment -- and MECH-150's own rationale for excluding it is recorded, so the
   comparison is well-posed.
