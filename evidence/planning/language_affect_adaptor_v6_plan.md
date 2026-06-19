---
closure_plan:
  id: language_affect_adaptor_v6
  generation: v6
  title: "Language-affect adaptor (parse affect from language as probabilistic hypotheses)"
  registered: 2026-06-10
  last_updated: 2026-06-10
  scope_claims: [MECH-373, ARC-009, INV-003, INV-007, ARC-010, MECH-031, Q-007, ARC-087]
  sibling_plans: [fast_empathy_v5, mirror_modelling_other_self_v5, multi_agent_ecology_v5, ethics_as_coherence_v5, object_representation_v4]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. V6 (the LINGUISTIC mind tier, the final
    tier of the V4-individual / V5-social / V6-linguistic partition) has no
    experiments yet, so nodes carry no owner_exq and the drift checker stays
    dormant against them. The spine is ARC-059: self -> objects -> others ->
    LANGUAGE. Language PRESUPPOSES the V5 social substrate (mirror modelling,
    joint attention, other-modelling) and the V4 object/self substrate; an
    adaptor that parses ANOTHER agent's affect from text is meaningless without a
    stable other-model to bind the parsed affect into. So every node here is
    gated behind BOTH the V5 social plans (fast_empathy_v5, mirror_modelling_-
    other_self_v5, multi_agent_ecology_v5, ethics_as_coherence_v5) AND the
    V4 object/self substrate AND the V3 MECH-163 multi-step hippocampal planning
    gate. generation: v6 keeps these nodes OUT of the V3 closure percentage
    (serve.py read_closure, generate_closure_snapshot.py, and
    check_closure_drift.py are all generation-aware). This is the empathy-input
    specialisation of the language tier: MECH-373 already names the adaptor (a
    lightweight LanguageAffectAdaptor turning text into UNCERTAIN affect
    estimates, NOT categorical truths, feeding the social/empathy layer). The
    plan sequences it and pins the central invariant the seed thought only
    implied -- parsed affect MUST enter as a hypothesis, never as ground truth.
    A node graduates from roadmap to closure-tracked by gaining an owner_exq once
    its first V6 experiment is queued.
  nodes:
    - id: "language_affect_adaptor_v6:LAA-1"
      title: "Pre-linguistic-grounding gate: no affect adaptor before object/self/other primitives exist (the load-bearing ordering)"
      phase: 1
      status: blocked
      ethical_metadata:
        welfare_relevance: low
        applicable_ethics_gates: [SENT-13]
        requires_welfare_review: false
        note: "Pre-linguistic-grounding ordering gate (SENT-13): no affect adaptor before object/self/other primitives exist."
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [MECH-373, INV-003]
      depends_on: []
      cross_plan_link: ["object_representation_v4:OBJ-5", "mirror_modelling_other_self_v5", "fast_empathy_v5"]
      blocking_on: "Language work must wait until the pre-linguistic primitives (object / action / self / other / rule) exist and are grounded. The adaptor parses ANOTHER agent's affect; with no stable other-model slot to deposit the parsed estimate into, the adaptor has no consumer and any probe is vacuous (MECH-373 epistemic_category substrate_conditional -- explicitly off the V3/GAP-7 path, 'no language interface exists in V3, so any probe would be vacuous')."
      readiness_gate:
        - "ARC-059 spine: self -> objects -> others -> LANGUAGE. Language is stage 4; it presupposes stages 1-3 are grounded"
        - "V5 other-model present: ARC-010 mirror modelling realised as a per-agent object-file slot (object_representation_v4:OBJ-5 / ARC-083); the parsed affect prior is deposited INTO this slot"
        - "V4 object/self substrate: object-permanence (object_representation_v4:OBJ-2) + a stable self (self_model_v4) -- DEV-NEED-021 otherness-inference prerequisites -- so 'whose affect is this text reporting?' is answerable"
        - "MECH-163 multi-step hippocampal planning (V3-completion / V4-social entry gate) -- shared upstream gate for all other-directed work"
      last_updated: 2026-06-10
      completion_note: "This is the ordering claim the whole plan rests on: an affect adaptor is a language-channel INPUT to the social layer, so it cannot precede the social layer. MECH-373's substrate_conditional tag already encodes this; this node makes the prerequisite chain explicit and cross-links the V5/V4 plans that must land first. Blocked, not open: the gate is a real upstream dependency, not merely a design choice."
    - id: "language_affect_adaptor_v6:LAA-2"
      title: "Uncertainty-propagation invariant: parsed affect enters as a hypothesis (distribution), NEVER as ground truth"
      phase: 1
      status: open
      ethical_metadata:
        welfare_relevance: moderate
        applicable_ethics_gates: [GOV-SEC-1, SENT-14, INV-007]
        requires_welfare_review: false
        note: "Safety invariant: language-parsed affect enters as a distribution, never ground truth; guards against language overriding internal harm-sensing."
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["INV-085"]
      depends_on: ["language_affect_adaptor_v6:LAA-1"]
      cross_plan_link: ["mirror_modelling_other_self_v5"]
      readiness_gate:
        - "Registrable now as a DESIGN INVARIANT (no substrate prerequisite): any affect the adaptor recovers from text MUST be carried as a probability distribution over affect states (an uncertain other-agent prior), never collapsed to a categorical emotion label fed as fact into agent-state modelling"
        - "Grounds in MECH-373 commitment (2): 'treat emotion labels as UNCERTAIN latent-state hypotheses, not categorical truths -- a probability distribution over affect, not a hard class' -- and the Q-007 constructionist reframe (Barrett 2017/2019: emotions are constructed categories, not natural kinds with fixed signatures)"
        - "Consistency with INV-007 (language cannot override embodied harm sensing): a confident text claim of another's state must not be able to override the agent's own grounded harm/threat streams -- the hypothesis status is what keeps the language channel subordinate"
      last_updated: 2026-06-10
      completion_note: "The genuine GAP the seed thought only implied: MECH-373 names the adaptor but the uncertainty-as-architecture commitment deserves its own invariant. It is a NEGATIVE architectural commitment (no categorical-truth path from text to agent-state) testable as such -- like INV-007 it constrains what the language channel may NOT do. Cheapest node; registrable alongside the adaptor design with no substrate gate."
    - id: "language_affect_adaptor_v6:LAA-3"
      title: "The adaptor itself: a lightweight LanguageAffectAdaptor (SLM-class) text -> distribution-over-affect"
      phase: 2
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [MECH-373]
      depends_on: ["language_affect_adaptor_v6:LAA-1", "language_affect_adaptor_v6:LAA-2"]
      cross_plan_link: ["object_representation_v4:OBJ-5", "fast_empathy_v5"]
      blocking_on: "MECH-373 is substrate_conditional: it depends on ARC-009 (a language interface) which does not exist in V3, plus a stable other-model (LAA-1) to consume the output. Build only once the language channel and the V5 other-slot both exist."
      readiness_gate:
        - "ARC-009 language as symbolic mediation/coordination layer ACTIVE design -- the channel the adaptor plugs into (active claim, but no V3 substrate implementation)"
        - "Implementation candidate from the seed: a small-language-model (SLM) emotion classifier as the lightweight adaptor (TDS 'How to Fine-Tune an SLM for Emotion Recognition' -- notes-level reference, NOT citable experimental evidence)"
        - "Output contract: when literal semantic content is insufficient to recover affect, emit a probability distribution over affect states (per LAA-2), tagged with source-agent identity for deposit into the LAA-1 other-slot"
        - "DISTINCTNESS guard: this is an INPUT adaptor on the language channel (sibling to ARC-087 sense-specific perceptual-manifold adaptors); it is NOT REE's internal affect representation (Q-007 z_beta) -- it supplies OTHER-agent priors, not own-affect"
      last_updated: 2026-06-10
      completion_note: "MECH-373 already exists; this node tracks building it. Positioned as a language-channel sibling of the ARC-087 perceptual adaptors: each external channel gets a shaping adaptor before shared-world-model entry. Design-only today; gated on the language interface + the V5 other-model. Flagged v5->v6 (see generation_flags): the adaptor parses LANGUAGE, so it belongs in the linguistic tier, not V5."
    - id: "language_affect_adaptor_v6:LAA-4"
      title: "Consumption wiring: parsed other-affect prior feeds the V5 empathy stream-binding layer (not a parallel path)"
      phase: 3
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: ["MECH-418", MECH-031]
      depends_on: ["language_affect_adaptor_v6:LAA-3"]
      cross_plan_link: ["fast_empathy_v5", "mirror_modelling_other_self_v5"]
      blocking_on: "Requires the V5 fast-empathy stream-binding mechanism (fast_empathy_v5:EMP-3) to exist as the SINGLE consumer of other-affect priors; the language channel must feed THAT layer, not establish a second, competing affect-attribution path."
      readiness_gate:
        - "fast_empathy_v5:EMP-3 stream-binding mechanism in place (routes own motivational-affective streams across the other-model slot) -- the language-parsed prior becomes one more EVIDENCE source updating that slot's affect estimate"
        - "MECH-031 (derived social tags / empathy coupling) is the agent-state tag layer the parsed estimate informs -- the parsed distribution is a prior over the other's tags, combined with non-linguistic cues (behaviour, mirror-modelling) by the same binding layer"
        - "Architectural constraint: language is ONE input among several (behaviour, expression, context), per the grammar/LLM 'turbocharger not engine' discipline -- the adaptor must not become the dominant or sole affect-attribution route"
      last_updated: 2026-06-10
      completion_note: "Ensures the language tier plugs INTO the V5 social machinery rather than duplicating it. The parsed-affect distribution is fused with non-linguistic evidence by the existing empathy-binding layer (EMP-3) -- consistent with the language/ToM dissociation intake (language and fast-empathy as separable but interfacing systems). NEWCLAIM proposed for the wiring commitment; MECH-031 named as the consumed tag layer."
    - id: "language_affect_adaptor_v6:LAA-5"
      title: "Falsifiable test: language-parsed affect must change other-directed behaviour vs literal-semantics-only baseline (and must remain overridable)"
      phase: 3
      status: blocked
      ethical_metadata:
        welfare_relevance: moderate
        applicable_ethics_gates: [GOV-SEC-1, INV-007]
        requires_welfare_review: false
        note: "The overridable clause is the INV-007 guard at the behaviour boundary; language-parsed affect must remain overridable by harm-sensing."
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-373, "INV-085"]
      depends_on: ["language_affect_adaptor_v6:LAA-3", "language_affect_adaptor_v6:LAA-4"]
      cross_plan_link: ["fast_empathy_v5"]
      blocking_on: "Needs the adaptor (LAA-3) and the empathy-binding consumer (LAA-4) live, or at minimum a scripted-partner V6 proxy emitting text whose literal content under-specifies affect. Do NOT queue until that substrate exists."
      readiness_gate:
        - "Design (two falsifiable arms): (A) affect-recoverable-only-from-tone text -- the adaptor arm should shift other-directed behaviour where a literal-semantics-only baseline does not (the adaptor adds signal); (B) text confidently asserting a benign other-state that CONTRADICTS grounded threat cues -- the agent must NOT let the parsed claim override its embodied harm/threat streams (INV-007 / LAA-2 hypothesis status holds)"
        - "Predicted dissociation: arm A confirms the adaptor carries non-literal affect signal; arm B confirms the uncertainty-propagation invariant (a confident text label does not become ground truth)"
        - "Lit anchor to commission: an SLM/text emotion-recognition calibration pull (does the SLM emit calibrated distributions, or overconfident hard labels?) -- per feedback_biology_before_formal_definitions, the uncertainty claim needs a calibration grounding before promotion beyond candidate"
      last_updated: 2026-06-10
      completion_note: "The standout deliverable: a single experiment that simultaneously tests MECH-373 (the adaptor adds signal) and the uncertainty invariant (the adaptor's output stays overridable). Arm B is the load-bearing safety test -- it is what makes 'hypothesis not truth' falsifiable rather than decorative. First V6 experiment candidate; owner_exq stays null until the language channel + scripted-partner proxy exist."
    - id: "language_affect_adaptor_v6:LAA-6"
      title: "Biology/calibration grounding for the language-affect adaptor (lit-pull)"
      phase: 2
      status: deferred
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-373, "INV-085"]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "Per project rule feedback_biology_before_formal_definitions: the text->affect mapping and the uncertainty-propagation invariant need a grounding pull BEFORE registration beyond candidate"
        - "Seed anchors already present in MECH-373 notes: Barrett 2017/2019 (constructed-emotion, why parsed labels must be probabilistic); the 2026-04-16 language/affect lateralisation intake (ventral affect-to-meaning binding); the 2026-05-04 language-vs-ToM dissociation intake (language and fast-empathy as separable specialist systems)"
        - "Targeted reviews to commission: (1) SLM/text emotion-recognition calibration (do fine-tuned classifiers emit calibrated distributions?); (2) human inference of affect from language when prosody/context is absent (how uncertain SHOULD the prior be?); (3) ventral language->affect binding substrate"
      last_updated: 2026-06-10
      completion_note: "Grounding-debt tracker. MECH-373 carries Barrett + the two interface intakes as anchors but has no dedicated calibration pull. Deferred (not blocked) because it can begin independently of the substrate, but it is a registration gate for LAA-2 (the uncertainty invariant) and LAA-3 (the adaptor) promotion beyond candidate."
---
# Language-Affect Adaptor -- V6 Forward Roadmap

**Registered:** 2026-06-10
**Generation:** v6 (forward roadmap; LINGUISTIC mind tier; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** sequence the language-channel affect-input adaptor -- a lightweight
LanguageAffectAdaptor (MECH-373) that parses another agent's affect from text as
an UNCERTAIN probability distribution and feeds it to the V5 social/empathy
layer -- around one load-bearing ordering gate (no adaptor before the
pre-linguistic primitives exist) and one load-bearing invariant (parsed affect
enters as a hypothesis, never as ground truth).

This is a **V6 (linguistic) tier** plan, the final tier of the 3-tier partition
(V4 = individual mind, V5 = social, V6 = linguistic). The spine is **ARC-059**:
self -> objects -> others -> **LANGUAGE**. Language is stage 4 and presupposes
the V5 social substrate (mirror modelling, joint attention, other-modelling) and
the V4 object/self substrate. An adaptor that recovers ANOTHER agent's affect
from text is meaningless without a stable other-model to bind that affect into --
so every node here is gated behind the V5 social plans, the V4 object/self
substrate, and the shared **MECH-163** multi-step hippocampal planning gate. It
is a *forward roadmap*, not a closure map: V6 has no experiments yet, so nodes
carry no `owner_exq` and the drift checker stays dormant. The value here is the
**readiness gates** -- exactly which V5/V4/V3 prerequisites must land before the
language-affect step is honest to build.

---

## One-line framing

> The adaptor already EXISTS as a named claim (MECH-373): a small-language-model-
> class component that turns text into a distribution over the speaker's affect,
> feeding REE's other-agent modelling. What is NOT settled -- and is the genuine
> contribution of this plan -- is two architectural commitments: (1) the adaptor
> may not precede the pre-linguistic object/self/other substrate it depends on
> (ARC-059 ordering); and (2) whatever it recovers from text must enter as a
> HYPOTHESIS (a probability distribution over the other's state), never as a
> categorical emotion truth that could override the agent's own grounded harm
> sensing (INV-007). The adaptor is a language-channel sibling of the ARC-087
> sense-specific perceptual adaptors: every external channel gets a shaping
> adaptor before shared-world-model entry, and the language channel's special
> hazard is over-confidence.

---

## The adaptor stack (one ordering gate, one invariant, one mechanism, one test)

| Step | Node | Claim | Phase leaning | The readiness gate |
|---|---|---|---|---|
| pre-linguistic ordering gate | LAA-1 | MECH-373 / INV-003 / ARC-059 | V6 (blocked) | V5 other-model (OBJ-5) + V4 object/self + MECH-163 |
| uncertainty invariant | LAA-2 | NEWCLAIM (architectural_commitment) | V6 (registrable now) | none -- design invariant; grounds in Q-007 + INV-007 |
| the adaptor itself | LAA-3 | MECH-373 | V6 (blocked) | ARC-009 language channel + LAA-1 other-slot |
| consumption wiring | LAA-4 | NEWCLAIM (mechanism) + MECH-031 | V6 (blocked) | fast_empathy_v5:EMP-3 binding layer |
| falsifiable A/B test | LAA-5 | MECH-373 + NEWCLAIM | V6 (blocked) | LAA-3 + LAA-4 or scripted-partner proxy |
| biology/calibration grounding | LAA-6 | (grounding debt) | cross-cutting | SLM-calibration + language->affect lit-pulls |

---

## Why these are V6, not V5

MECH-373 is currently tagged `implementation_phase: v5`. But the SUBJECT of the
adaptor is intrinsically LINGUISTIC: it parses **language** (text) into affect.
The V5 social plans (fast_empathy_v5, mirror_modelling_other_self_v5) build the
other-model and the affect-binding layer the adaptor FEEDS, and they do so from
NON-linguistic cues (behaviour, expression, mirror-modelling). The moment the
input is text, the work is in the language tier. MECH-373 itself states the
adaptor "plugs into" ARC-009 (the language layer) -- it is a language-channel
component by construction. It is therefore flagged for reassignment v5 -> v6
(see below). The V5 social substrate is a PREREQUISITE (the consumer), not the
home tier.

The adaptor's distinctness is the reason it is its own node and not folded into
fast_empathy_v5: empathy stream-binding (EMP-3) operates on the other-model
regardless of input channel; this plan adds the LANGUAGE channel as one input to
that binding layer (LAA-4), with its own special hazard (over-confident text)
that the uncertainty invariant (LAA-2) and arm B of the test (LAA-5) guard
against.

---

## What this plan deliberately does NOT do

- **Does NOT build a language interface in V3.** MECH-373 is
  `substrate_conditional`: no language interface exists in V3, so any probe would
  be vacuous. Registering this roadmap changes no V3 behaviour.
- **Does NOT let text override grounded harm sensing.** That is the whole point
  of LAA-2 (the uncertainty invariant) and arm B of LAA-5. INV-007 (language
  cannot override embodied harm sensing) is the V3-era invariant this extends
  into the affect-parsing case.
- **Does NOT create a second affect-attribution path.** The adaptor feeds the
  existing V5 empathy-binding layer (fast_empathy_v5:EMP-3 / MECH-031), it does
  not establish a parallel route (LAA-4). Language is a turbocharger, not the
  engine.
- **Does NOT touch REE's OWN internal affect representation.** Q-007 (z_beta
  valence/arousal) is the orthogonal question of the agent's own affect; this
  adaptor supplies OTHER-agent priors only. The DISTINCTNESS guard is explicit
  in LAA-3.
- **Does NOT re-litigate the other-model itself.** The "is the other an object?"
  question is owned by object_representation_v4 (OBJ-5 / ARC-083) and the
  mirror-modelling plan; this plan consumes a stable other-slot and deposits a
  language-parsed affect prior into it.

---

## Source artefacts

| Artefact | Role |
|---|---|
| docs/thoughts/2026-06-07-language-affect-adaptor-slm-emotion-recognition.md | the seed thought (primary source; SLM emotion-recognition reference; the three design commitments) |
| claims.yaml MECH-373 | the adaptor claim (candidate / substrate_conditional / implementation_phase v5 -- flagged v5->v6) |
| claims.yaml ARC-009 / INV-003 / INV-007 | the language tier: symbolic mediation (active), emergence-not-bolt-on (active), cannot-override-harm (active) -- the established design this plan sits inside |
| claims.yaml ARC-010 / MECH-031 | the social consumer: mirror modelling + derived social tags / empathy coupling the parsed prior informs |
| claims.yaml Q-007 | the constructionist reframe (Barrett) that makes parsed labels necessarily probabilistic |
| claims.yaml ARC-087 | sibling sense-specific perceptual-manifold adaptor (the input-adaptor pattern the language adaptor follows) |
| claims.yaml ARC-059 / developmental_needs_register DEV-NEED-021 | the self -> objects -> others -> language maturational spine |
| evidence/planning/fast_empathy_v5_plan.md (EMP-3) | the V5 empathy stream-binding layer that consumes the parsed prior |
| evidence/planning/thought_intake_2026-06-05_grammar_llms_v5_primitive_mining.md | the language-after-grounding discipline ('turbocharger not engine'; mine after grounding) |

---

## Decision log

- **2026-06-10** -- Plan registered as a V6 (linguistic tier) forward-roadmap.
  Six nodes: LAA-1 (pre-linguistic ordering gate, the spine), LAA-2
  (uncertainty-propagation invariant -- parsed affect is a hypothesis, the
  genuine new claim), LAA-3 (the adaptor itself, MECH-373), LAA-4 (consumption
  wiring into the V5 empathy-binding layer), LAA-5 (falsifiable A/B test --
  adds-signal AND stays-overridable), LAA-6 (biology/calibration grounding
  debt). All substantive nodes gated behind the V5 social plans + V4 object/self
  substrate + MECH-163 per ARC-059. Two NEW candidate claims proposed (the
  uncertainty-propagation invariant; the language-feeds-empathy-binding wiring
  mechanism). `generation: v6` set so the V3 closure % is unaffected. No
  claims.yaml edits (orchestrator merges).
- **2026-06-10** -- Reassignment flag raised: MECH-373 is intrinsically
  LINGUISTIC (it parses language into affect) but is tagged
  `implementation_phase: v5`; recommended v6. The V5 social substrate is its
  prerequisite (consumer), not its home tier. ACTIVE language claims
  (ARC-009 / INV-003 / INV-007) deliberately NOT flagged -- they are established
  design. MECH-163 deliberately NOT flagged (it is the v3 completion gate and
  stays v3). ARC-010 / MECH-031 left as-is (V5 social consumers, consumed not
  re-scoped).
</content>
</invoke>
