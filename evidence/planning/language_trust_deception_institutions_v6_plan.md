---
closure_plan:
  id: language_trust_deception_institutions_v6
  generation: v6
  title: "Language trust, deception, failure modes, and institutions"
  registered: 2026-06-10
  last_updated: 2026-06-10
  scope_claims: [INV-007, ARC-009, INV-003, MECH-012, MECH-013, MECH-015, MECH-031, INV-029, ARC-012]
  sibling_plans: [ethics_as_coherence_v5, relational_harm_moral_semantics_v5, mirror_modelling_other_self_v5, fast_empathy_v5, multi_agent_ecology_v5]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. V6 (the LINGUISTIC mind tier, final tier
    of the 3-tier partition: V4 individual / V5 social / V6 linguistic) has no
    experiments yet, so nodes carry no owner_exq and the drift checker stays
    dormant against them. Each node's readiness_gate lists the prerequisites that
    must land first -- the V5 social tier (multi_agent_ecology_v5,
    mirror_modelling_other_self_v5, fast_empathy_v5, ethics_as_coherence_v5,
    relational_harm_moral_semantics_v5), the V4 object/self tier, and the shared
    MECH-163 multi-step hippocampal planning gate -- before the V6 linguistic
    step is honest to build. generation: v6 keeps these nodes OUT of the V3
    closure percentage (serve.py read_closure, generate_closure_snapshot.py, and
    check_closure_drift.py are all generation-aware). The spine is ARC-059:
    self -> objects -> others -> LANGUAGE. Language PRESUPPOSES the V5 social
    substrate (mirror modelling, joint attention, other-modelling) and the V4
    object/self substrate; the pre-linguistic primitives (object/action/self/
    other/rule) must exist and be grounded first. This plan is the
    safety/social-integrity layer of language: it makes operational the ACTIVE
    invariant INV-007 (language is NOT a value source and cannot override
    embodied harm sensing) as an explicit guard mechanism, and sequences the
    trust-calibration, deception-detection, language-failure-mode, and
    institutional-coordination work that the three legacy language docs sketch.
    A node graduates from roadmap to closure-tracked by gaining an owner_exq
    once its first V6 experiment is queued.
  nodes:
    - id: "language_trust_deception_institutions_v6:LTI-1"
      title: "Language-cannot-override-harm as an explicit GUARD mechanism (operationalise INV-007)"
      phase: 1
      status: open
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["INV-007", "ARC-104"]
      depends_on: []
      cross_plan_link: ["ethics_as_coherence_v5", "relational_harm_moral_semantics_v5"]
      readiness_gate:
        - "INV-007 ('Language cannot override embodied harm sensing') is an ACTIVE universal invariant -- it is asserted but NOT yet realised as an architectural guard a design can violate. This node converts the invariant into an explicit mechanism: symbolic input may CONDITION priors but the harm/ethics substrate retains veto authority over any language-mediated update"
        - "No substrate prerequisite for the DESIGN CLAIM (registrable now as the spine of the plan, like ARC-012's 'E3 needs no explicit ethical cost term'); the guard is a negative architectural commitment -- there must be NO path by which symbolic/linguistic content overwrites or suppresses a harm signal"
        - "Realisation gate (the test that the guard holds) is V6: needs a language channel (ARC-009) feeding the world model AND the non-linguistic harm substrate (SD-011 dual-nociceptive streams, the V5 ethics_as_coherence + relational_harm_moral_semantics tiers) so a false harm claim can be cross-checked against embodied harm and world-model prediction"
      last_updated: 2026-06-10
      completion_note: "The CENTRAL safety contribution of the language-trust layer. INV-007 already exists as an invariant; this node makes it a guard mechanism the rest of the plan presupposes. trust_and_deception.md: 'symbolic input is informative but not authoritative' -- the guard is the architectural form of that sentence. Like ARC-012 it is testable as what must NOT exist (no language->harm-suppression path)."
    - id: "language_trust_deception_institutions_v6:LTI-2"
      title: "Trust-calibration over linguistic signals (sender-reliability estimate weights symbolic updates)"
      phase: 2
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["MECH-015"]
      depends_on: ["language_trust_deception_institutions_v6:LTI-1"]
      cross_plan_link: ["mirror_modelling_other_self_v5", "multi_agent_ecology_v5"]
      blocking_on: "Requires a stable per-sender other-model (mirror_modelling_other_self_v5; per-agent token-keyed object-file ARC-083) so reliability can be tracked PER sender, plus a language channel (ARC-009) and MECH-163 multi-step planning (V4 social-entry gate). No per-sender trust without a per-sender model."
      readiness_gate:
        - "MECH-015 (trust_and_deception.md) already names the receiver-side reliability estimate: consistency with observed outcomes, alignment with harm signals, calibration history (confidence vs accuracy). This node operationalises MECH-015 as a trust-weight that gates symbolic prior-updates"
        - "A stable per-sender other-model: mirror_modelling_other_self_v5 / ARC-083 others-as-object slot, so reliability is attached to a sender identity (gated on MECH-163 + DEV-NEED-021 object-permanence + stable self, both V4)"
        - "The harm-alignment input to the trust estimate is the LTI-1 guard plus the V5 ethics tier: 'does this sender's language align with embodied harm signals?' is a trust input, not an override"
      last_updated: 2026-06-10
      completion_note: "Operationalises MECH-015's receiver-side reliability estimate. The trust-weight is the positive mechanism that makes 'informative but not authoritative' computable: symbolic updates scale by reliability, and repeated miscalibration reduces the weight. Design-only today; gated on a per-sender other-model."
    - id: "language_trust_deception_institutions_v6:LTI-3"
      title: "Deception detection / honest-signal pressure (deception = modelling another model)"
      phase: 3
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["MECH-015"]
      depends_on: ["language_trust_deception_institutions_v6:LTI-1", "language_trust_deception_institutions_v6:LTI-2"]
      cross_plan_link: ["mirror_modelling_other_self_v5", "multi_agent_ecology_v5"]
      blocking_on: "Deception requires a sender to model the RECEIVER's model (a recursive other-model) and an ecology in which honest vs deceptive signalling can be selected. Both are V5: recursive mirror modelling (mirror_modelling_other_self_v5) and a multi-agent ecology (multi_agent_ecology_v5). Cannot be demonstrated until those substrates exist."
      readiness_gate:
        - "Recursive other-modelling: deception is literally modelling another agent's model and exploiting the gap (mirror_modelling_other_self_v5 must supply a model-of-the-other's-model, not just an other-state estimate)"
        - "A multi-agent ecology (multi_agent_ecology_v5) where false harm claims / false commitments / reputational laundering (the trust_and_deception.md attack surfaces) can actually be played and where honest-signal pressure can emerge from repeated interaction"
        - "The cross-check substrate from LTI-1/LTI-2: deception is detected by language-vs-embodied-harm and language-vs-world-model-prediction mismatch, penalised via reduced trust-weight (the MECH-015 prediction)"
      last_updated: 2026-06-10
      completion_note: "trust_and_deception.md attack surfaces (false harm claims, false commitments, ideological framing, reputational laundering) are the deception space. The deep point: deception is a SPECIALISATION of mirror modelling (modelling another model) -- it cannot precede the recursive other-model. Honest-signal pressure is the ecology-level emergent that the guard (LTI-1) + trust-weight (LTI-2) make selectable."
    - id: "language_trust_deception_institutions_v6:LTI-4"
      title: "Language failure modes as REE pathologies (rationalisation / ideological capture / bureaucratic dissociation / moral licensing / reputation substitution)"
      phase: 3
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: ["MECH-013"]
      depends_on: ["language_trust_deception_institutions_v6:LTI-1"]
      cross_plan_link: ["ethics_as_coherence_v5", "relational_harm_moral_semantics_v5"]
      blocking_on: "Each failure mode is a way the language channel decouples from embodied ethical signals; demonstrating (and guarding against) them requires the language channel (ARC-009) wired to the harm/residue substrate (LTI-1 guard) plus the V5 ethics/residue tiers. Cannot be exhibited without that wiring."
      readiness_gate:
        - "MECH-013 (language_failure_modes.md) already enumerates the five modes and maps them to REE pathologies: rationalisation = residue externalisation; ideological capture = precision misrouting; bureaucratic dissociation = harm abstracted until it stops registering; moral licensing + reputation substitution = moral residue replaced by social scoring. This node operationalises that mapping as DETECTABLE failure signatures"
        - "The residue substrate the failures corrupt: ethics_as_coherence_v5 + relational_harm_moral_semantics_v5 (moral residue, precision routing) -- a failure mode is a deviation FROM that substrate caused by language"
        - "The LTI-1 guard is the prophylaxis: each failure mode is a specific way language tries to suppress/displace a harm or residue signal, which the guard forbids; this node catalogues the failures the guard must block"
      last_updated: 2026-06-10
      completion_note: "MECH-013 maps the five language failure modes onto existing REE pathologies (residue externalisation, precision misrouting, other-model collapse, spurious narrative residue). The value here is turning that map into detectable signatures so the guard (LTI-1) and trust-weight (LTI-2) can be evaluated against named adversarial patterns rather than abstractly."
    - id: "language_trust_deception_institutions_v6:LTI-5"
      title: "Institutions as multi-agent linguistic coordination structures (residue absorb / diffuse / deny)"
      phase: 4
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: ["MECH-012"]
      depends_on: ["language_trust_deception_institutions_v6:LTI-2", "language_trust_deception_institutions_v6:LTI-4"]
      cross_plan_link: ["multi_agent_ecology_v5", "ethics_as_coherence_v5"]
      blocking_on: "An institution is a multi-agent linguistic coordination structure; it cannot be modelled before a multi-agent ecology (multi_agent_ecology_v5) AND a language channel (ARC-009) AND the residue substrate (V5 ethics tiers) all exist. It is the most downstream node -- collective-level language built on the per-agent trust/deception/failure layer."
      readiness_gate:
        - "MECH-012 (language_and_institutions.md): in collective systems language becomes the primary medium through which ethical residue is managed or displaced; institutions absorb (protect individuals) / diffuse (lose accountability) / deny (systemic harm) residue. This node operationalises institutions as that coordination structure"
        - "A multi-agent ecology (multi_agent_ecology_v5) with >2 agents so collective residue dynamics (diffusion of accountability) are expressible, plus per-agent trust-calibration (LTI-2) and failure-mode signatures (LTI-4) as the building blocks"
        - "The REE prediction to test: institutional ethical failure arises when symbolic language FULLY decouples from embodied harm signals and residue tracking -- i.e. the LTI-1 guard failing at the collective scale"
      last_updated: 2026-06-10
      completion_note: "MECH-012: institutions are language-mediated residue-coordination structures. The absorb/diffuse/deny trichotomy is the collective-scale image of the individual guard: a healthy institution preserves the language<->harm coupling (absorb), a failing one severs it (deny). The most downstream node -- collective linguistic ethics on top of the per-agent layer."
    - id: "language_trust_deception_institutions_v6:LTI-6"
      title: "Biology / social-science grounding for trust, deception, and institutional residue (lit-pull)"
      phase: 2
      status: deferred
      severity: medium
      owner_exq: null
      unblocks_claims: ["MECH-012", "MECH-013", "MECH-015"]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "Per project rule feedback_biology_before_formal_definitions: the trust-calibration, honest-signal, and institutional-residue claims instantiate formal concepts (signalling theory, reputation/indirect reciprocity, institutional economics) and need a grounding pull BEFORE registration beyond candidate"
        - "Targeted reviews to commission: costly/honest-signalling theory (Zahavi handicap; Spence signalling) for LTI-3; reputation + indirect reciprocity (Nowak & Sigmund) for LTI-2/LTI-5; deception detection + ToM-recursion development for LTI-3; moral disengagement (Bandura -- maps to MECH-013 moral licensing/rationalisation) and bureaucratic-dissociation literature for LTI-4"
        - "No substrate gate -- this can begin independently of the V5/V6 substrate; it is a REGISTRATION gate for promoting the new trust/deception/institution claims beyond candidate"
      last_updated: 2026-06-10
      completion_note: "Grounding-debt tracker. The three legacy language docs (MECH-012/013/015) carry NO biology/social-science lit-pull and were written as design prose. Deferred (not blocked) because it can start without the substrate, but it gates promotion of LTI-2..LTI-5 NEWCLAIMs beyond candidate, per the project's biology-before-formal-definitions rule."
---
# Language Trust, Deception, Failure Modes, and Institutions -- V6 Forward Roadmap

**Registered:** 2026-06-10
**Generation:** v6 (forward roadmap; LINGUISTIC mind tier; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** sequence the safety/social-integrity layer of language around one
load-bearing guard -- INV-007, language cannot override embodied harm sensing --
and the trust-calibration, deception-detection, language-failure-mode, and
institutional-coordination work that the guard makes safe to build.

This is a **V6 (linguistic) tier** plan, the final tier of the 3-tier partition
(V4 = individual mind, V5 = social, V6 = linguistic). The spine is **ARC-059**:
self -> objects -> others -> **LANGUAGE**. Language PRESUPPOSES the V5 social
substrate (mirror modelling, joint attention, other-modelling) and the V4
object/self substrate; the pre-linguistic primitives (object / action / self /
other / rule) must exist and be grounded before any linguistic coordination work
is honest. It is a *forward roadmap*, not a closure map: V6 has no experiments
yet, so nodes carry no `owner_exq` and the drift checker stays dormant. The value
here is the **readiness gates** -- for each step, exactly which V5-social and
V4-individual prerequisites must land before the V6 linguistic step is buildable.

---

## One-line framing

> Language gives REE its most powerful coordination medium and, simultaneously,
> its most dangerous attack surface. The ACTIVE invariant INV-007 already asserts
> that language cannot override embodied harm sensing; INV-003 already asserts
> language emerges as functional self-representation, not a bolt-on. What is NOT
> done -- and is the whole of this plan -- is realising INV-007 as an explicit
> GUARD mechanism (symbolic input conditions priors but the harm/ethics substrate
> keeps veto authority), then building on that guard the receiver-side trust
> calibration (MECH-015), deception detection as a specialisation of mirror
> modelling (MECH-015), the catalogue of language failure modes as REE
> pathologies (MECH-013), and institutions as multi-agent linguistic
> residue-coordination structures (MECH-012). Every node presupposes a stable
> other-model and a working harm/residue substrate -- which is why this is V6, on
> top of V5, on top of V4.

---

## The trust/deception/institution stack (one guard, four consumers, one grounding debt)

| Step | Node | Claim | Phase leaning | The readiness gate |
|---|---|---|---|---|
| guard (no override) | LTI-1 | INV-007 + NEWCLAIM | V6 (registrable now) | none -- it is the guard design; realisation needs the language channel + harm substrate |
| trust calibration | LTI-2 | MECH-015 + NEWCLAIM | V6 (blocked) | per-sender other-model (mirror_modelling_other_self_v5 / ARC-083) + MECH-163 |
| deception detection | LTI-3 | MECH-015 + NEWCLAIM | V6 (blocked) | recursive other-model + multi_agent_ecology_v5 |
| language failure modes | LTI-4 | MECH-013 + NEWCLAIM | V6 (blocked) | language channel wired to harm/residue substrate (LTI-1 + V5 ethics) |
| institutions | LTI-5 | MECH-012 + NEWCLAIM | V6 (blocked) | multi_agent_ecology_v5 (>2 agents) + LTI-2 + LTI-4 |
| biology grounding | LTI-6 | (grounding debt) | cross-cutting | signalling / reputation / moral-disengagement lit-pulls |

---

## Why these are V6, not V5

The substrate this plan consumes -- a stable per-sender other-model, recursive
mirror modelling, a multi-agent ecology, a harm/residue ethics substrate -- is
genuinely V5 (social) on top of V4 (individual). But the SUBJECT of every node
here is intrinsically **linguistic**: symbolic input conditioning priors,
sender-reliability over LANGUAGE, deception via false harm CLAIMS / false
COMMITMENTS, ideological FRAMING, institutions as language-mediated coordination.
None of it exists without the language channel (ARC-009). That places the work in
the V6 linguistic tier, sitting on top of V5, sitting on top of V4. The
prerequisite chain is explicit in each readiness_gate. Per the grammar/LLM
thought, language work waits until the pre-linguistic primitives are grounded;
this plan honours that by gating every consumer node behind the V5 social tier.

---

## What this plan deliberately does NOT do

- **Does NOT weaken INV-007.** The guard (LTI-1) is the positive realisation of
  the invariant, not a relaxation. Any design that lets symbolic content suppress
  or overwrite a harm signal violates LTI-1.
- **Does NOT treat language as a value source.** Language conditions priors and
  carries trust-weighted information; it never originates value. The harm/ethics
  substrate (V5 ethics_as_coherence + relational_harm_moral_semantics) keeps
  value authority.
- **Does NOT pull anything into V3.** Registering this roadmap changes no V3
  behaviour. The first realisation step (testing the guard end-to-end) is V6,
  gated on the language channel + the V5 social/ethics substrate.
- **Does NOT re-build the other-model or the ecology.** Recursive mirror
  modelling is owned by `mirror_modelling_other_self_v5`; the multi-agent ecology
  by `multi_agent_ecology_v5`; the residue/ethics substrate by
  `ethics_as_coherence_v5` + `relational_harm_moral_semantics_v5`. This plan
  CONSUMES those and adds the linguistic safety layer on top.
- **Does NOT re-scope ARC-009 / INV-003 / INV-007.** Those are ACTIVE established
  design and stay as-is; this plan operationalises them, it does not move them.

---

## Source artefacts

| Artefact | Role |
|---|---|
| [docs/architecture/language/trust_and_deception.md](../../docs/architecture/language/trust_and_deception.md) | MECH-015: receiver-side trust-weight + deception attack surfaces (primary source for LTI-2/LTI-3) |
| [docs/architecture/language/language_failure_modes.md](../../docs/architecture/language/language_failure_modes.md) | MECH-013: the five failure modes -> REE pathologies map (primary source for LTI-4) |
| [docs/architecture/language/language_and_institutions.md](../../docs/architecture/language/language_and_institutions.md) | MECH-012: institutions as language-mediated residue coordination (primary source for LTI-5) |
| claims.yaml INV-007 | the ACTIVE universal invariant LTI-1 operationalises (language cannot override embodied harm) |
| claims.yaml INV-003 / ARC-009 | language emergence + symbolic-mediation layer (the channel every node presupposes) |
| claims.yaml MECH-012 / MECH-013 / MECH-015 | the existing candidate language claims this plan sequences (intrinsically linguistic -- see Reassignment flags) |
| claims.yaml MECH-031 | derived social tags + empathy coupling (the social-coupling seed the trust layer rides on) |
| claims.yaml INV-029 / ARC-012 | INV-029 (love as long-horizon coherence) as the value institutions absorb/deny; ARC-012 as the template for LTI-1 (an architectural commitment about what must NOT exist) |
| evidence/planning/ethics_as_coherence_v5_plan.md, relational_harm_moral_semantics_v5_plan.md, mirror_modelling_other_self_v5_plan.md, multi_agent_ecology_v5_plan.md | the V5 social/ethics substrate every consumer node is gated behind |

---

## Decision log

- **2026-06-10** -- Plan registered as the V6 (linguistic tier) safety/social-
  integrity forward-roadmap. Six nodes: LTI-1 (language-cannot-override-harm guard
  -- the spine, operationalising ACTIVE INV-007), LTI-2 (linguistic trust
  calibration, operationalising MECH-015), LTI-3 (deception detection as a
  specialisation of mirror modelling, MECH-015), LTI-4 (language failure modes as
  REE pathologies, MECH-013), LTI-5 (institutions as multi-agent linguistic
  residue coordination, MECH-012), LTI-6 (biology/social-science grounding debt).
  All consumer nodes gated behind the V5 social tier (mirror_modelling_other_self,
  multi_agent_ecology, ethics_as_coherence, relational_harm_moral_semantics) +
  MECH-163 + the V4 object/self substrate per ARC-059. Five NEW candidate claims
  proposed (the harm-override guard, linguistic trust calibration, deception
  detection / honest-signal pressure, the language-failure-mode taxonomy, the
  institutional residue-coordination mechanism). `generation: v6` set so the V3
  closure % is unaffected. No claims.yaml edits (orchestrator merges).
- **2026-06-10** -- Reassignment flags raised for MECH-012, MECH-013, MECH-015:
  all three are intrinsically LINGUISTIC (depend on ARC-009) candidate claims that
  carry NO implementation_phase tag; recommended_phase v6. ARC-009 / INV-003 /
  INV-007 deliberately NOT flagged (ACTIVE established design -- they are
  operationalised, not re-scoped). MECH-163 NOT flagged (V3 completion gate, stays
  v3). MECH-031 left as-is (social-coupling seed, consumed not re-scoped).
- **2026-06-10** -- MECH-373 (LanguageAffectAdaptor) reviewed for the v6 tier:
  it is intrinsically linguistic (language-channel input adaptor, depends on
  ARC-009) but currently implementation_phase v5 / version_relevance v4_v5.
  Flagged for recommended_phase v6 in generation_flags -- the affect adaptor is a
  language-interface component and belongs in the linguistic tier alongside this
  plan's trust/deception layer, though it is owned by the language-affect line,
  not this plan.
