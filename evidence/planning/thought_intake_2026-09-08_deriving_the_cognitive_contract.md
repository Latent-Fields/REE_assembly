# Thought intake -- Deriving the Cognitive Contract

**Date processed:** 2026-09-08
**Raw thought:** `docs/thoughts/2026-09-08_deriving_the_cognitive_contract.md` (792 lines, 23 sections)
**Session:** thought-ingest-cognitive-contract-20260908
**Companion read for context (already ingested, not re-derived):**
`evidence/planning/thought_intake_2026-09-07_mutual_legibility.md` (ARC-139, MECH-537..540, INV-105),
`docs/thoughts/2026-02-09_language.md` (ARC-009 / MECH-010), INV-104's registration notes.

The user's steer for this pass: *not just claim harvest -- some of these thoughts could lead to
new aspects of governance of REE_assembly, ideas to incorporate into REE itself, and more.* The
pass therefore registers one governance rule alongside the architecture, and records the
REE-design and programme-level consequences in section 7 rather than dropping them.

## 1. Verbatim core proposal

> **Unified cognition requires an invariant-preserving cognitive contract between representational
> systems.** The contract is not necessarily a common latent space. It may instead consist of a small
> set of relations or properties that must remain recoverable whenever information is compressed,
> decompressed or translated from one cognitive representation into another.

> The question is therefore not: *How do we force every engine to use the same latent space?* It is:
> *What must remain invariant across translation for multiple latent spaces to constitute one mind?*

> **Unity does not require representational sameness. It requires preservation of the relations that
> allow representations to remain about the same cognitive world.**

## 2. Novelty table

| Thread in the thought | Existing REE coverage | Verdict |
|---|---|---|
| Heterogeneous engines need not share a latent; integration via legibility not sameness (s.1-2, s.15) | **ARC-139** owns this exactly (registered yesterday from the mutual-legibility package); ARC-121 is the rival shared-object reading | **Already owned** -- cross-ref only; ARC-142 depends_on both, ARC-121 untouched |
| Compression must preserve organism-relevant distinctions on one path (s.11) | **INV-104** (five classes, observation -> z_world -> E1/E2, sender-side) | **Already owned as the single-path instance**; ARC-142 generalises it to every boundary and adds the contract/schema layering |
| Minimum bridge complexity as the measure of translation (s.11, s.14) | **MECH-538** | **Already owned** -- ARC-142 is the content side (what the bridge must carry) |
| Transition geometry must survive the map (s.10 temporal lesion) | **MECH-539** | **Already owned** -- named as one candidate invariant |
| Compression / decompression sites are where translation is exercised and tested (s.11) | **MECH-507**, **MECH-532**, SD-056 / SD-070 | **Already owned** -- cross-ref |
| Ontology / dimensionality free to change over development = the schema layer (s.4, s.13-14) | **INV-101**, **MECH-496**, INV-104's removable-scaffold clause | **Already owned** -- cross-ref |
| Reality-status distinction and the one-way provenance gate (s.10 reality lesion) | **MECH-094**, **MECH-365**, **MECH-271**, **ARC-092**, MECH-430 | **Already owned at content level** -- the boundary-lesion FORM is new (MECH-545) |
| Identity / agency / temporal / confidence distinctions individually | **ARC-080**, **MECH-256** + reafference lineage, **INV-035**, precision / MECH-123 lineage | **Already owned at content level** -- same |
| Failure modes indexed on cross-cutting latent axes (s.10 as a whole) | **ARC-086** (precision, provenance, agency, commitment, self-other, ... axes) | **Adjacent**: ARC-086 is the INDEX, the lesion assay is the forward INTERVENTION; 3/5 overlap logged as a convergence clue |
| Grammar mined, never imported; LLM never authority (s.7-8) | **ARC-100** | **Adjacent-but-distinct**: ARC-100 mines for primitive CUTS; this thought mines for BOUNDARY invariants and adds the A/B/C contamination taxonomy -> GOV-CONTRACT-1 |
| Language externalises functional states / is an interface / bootstraps from grounded ecology (s.12) | **ARC-048**, **ARC-114**, **ARC-101**, ARC-009, MECH-010, INV-003 | **Adjacent-but-distinct**: none predicts WHICH relational structure the channel converges on or why -> MECH-546 |
| Introspection generates, never validates alone (s.9 method) | **GOV-INTRO-1** | **Sibling governance rule** -- same shape, different generator (language) -> GOV-CONTRACT-1 |
| REE:Assembly analogies must be labelled (s.5: contract != claims machinery, convergence is a clue) | **GOV-ANALOGY-1** | **Already owned** -- GOV-CONTRACT-1 cites it for the section-5 discipline |
| Single cognifold as one interacting state-space; substrate-neutral primitives (s.15) | **ARC-089** | **Adjacent**: ARC-142 reads "one state-space" as one interpretable structure, not one geometry -- a reading recorded on the location doc, no amendment |
| Super-additivity over a shared latent (s.2.1) | **MECH-423** | **Adjacent**: must be read as shared FEATURES, not shared geometry; noted in ARC-142 |
| The contract itself as an architectural principle: relational invariants under lossy translation, above translation machinery, above schemas, recoverable relationships not a fixed ontology (s.1, 3, 4, 11, 14, 23) | none (`grep -i "cognitive contract"` -> 0) | **NEW -> ARC-142** |
| Triangulation across six evidence domains; A/B/C classification; linguistic universality alone inadmissible; preserve negative findings; derive independently of claims machinery; twelve-field ledger (s.5, 8, 9, 18, 19) | none as a rule | **NEW -> GOV-CONTRACT-1** |
| Contract-lesion assays with five pre-registered signatures at an inter-engine boundary (s.10, falsifiable claim 1) | none (`grep -i "lesion assay"` -> 0) | **NEW -> MECH-545** |
| Grammar inherits internal contract requirements; bidirectional test (s.7, 12, falsifiable claim 7) | none | **NEW -> MECH-546** |
| Cognifold vs braidling severance criterion (s.1, 16) | none (`grep -i braidling` -> 0 in claims.yaml and docs/) | **NEW -> Q-104** |
| Developmental differentiation of the contract: primitives -> derived -> schemas; developmental precedence as strongest evidence (s.13) | **ARC-059** stages, **MECH-277**, INV-101 are adjacent | **Folded**: clause in ARC-142; evidential weight in GOV-CONTRACT-1. Not a separate claim. |
| Cognitive Contract Specification as engineering output (s.20) | none | **Deliberately NOT registered** -- see section 6 |

### The strongest extraction

The thought's central proposal was registered **yesterday** from a different source: ARC-139
("Integration does not require representational sameness, it requires selective mutual legibility")
came from the 2026-09-07 mutual-legibility package, which reached the same principle from the
communication-subspace neuroscience literature. This thought reaches it from the architecture side
(what a unified mind needs) and adds the half ARC-139 lacks: *what* must be legible. INV-104 (2026-09-04)
is the same principle instantiated on the one path that is the live V3 wall. Three independent routes
in five days converging on one principle is itself the kind of consilience GOV-CONTRACT-1 asks for --
recorded as a clue, per GOV-ANALOGY-1, not as evidence.

## 3. Key formulations (verbatim)

- "**structured translatability**" -- neither representational identity nor unrestricted independence.
- "The invariant is therefore **semantic or relational rather than necessarily representational**."
- "Schema changes may alter what the organism knows. **Contract failure alters whether its cognitive
  systems can continue to understand one another.**"
- "deriving the cognitive contract from the existing claims machinery would be circular."
- "The goal is therefore to **derive and prune**, not to accumulate."
- "Language becomes an **inverse probe into cognitive interface requirements**."
- "Cross-linguistic universality therefore does not imply cognitive universality."
- "The strength of a candidate therefore comes from **consilience**, not from any single literature."
- "The strongest test of an invariant may not be whether it appears in successful cognition but **what
  happens when it is absent**."
- "`I(x_A) ~ I(x'_B)` ... The central mathematical problem is therefore not representation matching. It is
  **invariant preservation under lossy translation**."
- "The contract should therefore specify **recoverable relationships**, not fixed data structures."
- "**Preserve negative findings.**"

## 4. Affected existing claims

Cross-referenced via `depends_on` only. **No status, confidence, evidence record, or field of any
existing claim was touched in this pass.** In particular:

- **ARC-121** stays the untouched rival (as the mutual-legibility intake already required).
- **ARC-089** is *read*, not amended: the sharpened cognifold definition lives on the location doc.
- **INV-104** is cited as the first instantiated contract; nothing in its per-class readiness record moves.
- **MECH-423**'s "shared latent" wording is flagged in ARC-142's notes as needing the shared-features
  reading; a future /governance pass may want to sharpen MECH-423's wording -- not done here.
- **ARC-086** gains a forward-intervention counterpart (MECH-545) but is not edited.

## 5. Candidate claims -- REGISTERED this pass

All `status: candidate` (Q-104 `open`), `registered_utc: 2026-09-08`, location
`docs/architecture/cognitive_contract.md` (new stub, parent "Core Engines & Forward Models", nav_order 17).

| ID | Type | Phase | One line |
|---|---|---|---|
| **ARC-142** | architectural_commitment | v4 | The cognitive contract: a small set of relations preserved under lossy inter-engine translation, above translation machinery and above schemas; recoverable relationships, not a fixed ontology. |
| **GOV-CONTRACT-1** | governance_rule | v3 | Admissibility of contract invariants: >= 2-of-6-domain consilience, A/B/C/uncertain classification, linguistic universality alone inadmissible, negative findings preserved, derived independently of the claims machinery, twelve-field ledger. |
| **MECH-545** | mechanism_hypothesis | v4 | Contract-lesion assays: lesion the translation not the content; five pre-registered dissociable signatures. |
| **MECH-546** | mechanism_hypothesis | v6 | Grammar inherits the cognitive contract; two-directional test. |
| **Q-104** | open_question | v4 | Cognifold vs braidling: severance criterion; does the contract operationalise it? |

## 6. Deliberately NOT registered

- **The Cognitive Contract Specification** (s.20: declared encodings, translator discovery, tolerated
  reconstruction error, drift monitoring, low-translation-confidence behaviour, add/retire rules). It is the
  programme's engineering OUTPUT, conditional on the ledger having entries; registering it now converts a
  discovery programme into standing architecture, which s.18 explicitly forbids.
- **The 22-item candidate inventory as individual claims.** Each becomes claim-shaped only when it has a
  ledger record and a lesion prediction. The inventory is recorded verbatim in ARC-142's notes and on the
  location doc as a research inventory.
- **Thoughts 2-4** (candidate invariants synthesis; compression/decompression and the cognifold; mathematics
  of invariant-preserving translation). Authoring programme, not claims -- tracked below.
- **The developmental primitives** (`self-caused / not`, `here / not-here`, `now / not-now`) as separate
  claims: ARC-059 / MECH-256 / MECH-277 already own stage-1 self-attribution; the primitives are a clause
  in ARC-142.

## 7. What this pass routes beyond the registry (the user's "governance, REE itself, and more")

**Governance of REE_assembly.**
1. GOV-CONTRACT-1 is registered. It is warn-only until the ledger exists. It composes with ARC-100 and
   GOV-INTRO-1 and cites GOV-ANALOGY-1 for the section-5 discipline.
2. **Ledger scaffold owed:** `evidence/planning/cognitive_contract_invariant_ledger.v1.json`, one record
   per candidate with the twelve fields in GOV-CONTRACT-1. Nothing writes it yet. Chipped (see WORKSPACE_STATE).
3. **Held-out check recorded on GOV-CONTRACT-1** (GOV-HELDOUT-1): three prior cases, one of which
   (INV-104 class 5) gets a different answer under the new rule, so the check is non-degenerate.
4. A standing observation for /governance: this is the **third** independent route in five days
   (INV-104 2026-09-04, ARC-139 2026-09-07, ARC-142 2026-09-08) to "unity via preserved relations, not
   shared geometry". That is a claim-synthesis signal -- three candidates on one principle at three grains --
   and /claim-synthesis may want to record the recurrence rather than let it stay implicit in `depends_on`.

**Ideas for REE itself (not built, recorded for the substrate roadmap).**
1. Every inter-engine boundary in `ree_core` (E1<->E2, E2->hippocampal CEM, E1/E2->E3 scoring, waking->offline
   consolidation) is a contract site. The first two already have instruments queued or owed by the
   mutual-legibility programme (ML-10..ML-15); the E3 scoring boundary and the replay->consolidation
   boundary do not. The reality-status boundary (MECH-365's `committed_vs_imagined` at replay->consolidation)
   is the cheapest V3-buildable lesion cousin -- flagged on MECH-545 for /governance routing, not decided.
2. "Behaviour when translation confidence is low" (s.20 item 9) is a genuine substrate gap: no REE
   mechanism today represents *confidence in a translation* as distinct from confidence in content.
   Not registered (no mechanism proposed yet); recorded here so the Thought-3 author sees it.
3. Representational drift monitoring across a boundary (s.20 item 8) is the natural consumer of MECH-538's
   bridge complexity over checkpoints -- an instrument, owned by ML-13 once built.

**And more.**
- The cognifold/braidling criterion (Q-104) has an ethics-perimeter consequence (is a braidling of REE
  agents one moral patient or several) that belongs to SENT-* / GOV-PRESERVE-1 downstream. Noted, not routed.
- MECH-546 is the first REE claim that predicts *why* grammar is worth mining (ARC-100 only licenses it).

## 8. Next steps

1. **Lit-pull owed before any external reference is cited as SUPPORT.** The thought names no specific
   papers; the domains it invokes (grammaticalisation typology, pre-linguistic developmental cognition,
   emergent-communication agents, comparative cognition) were NOT searched in this pass. Per
   `feedback_lit_exp_decoupled`, corroboration will not raise any claim's confidence.
2. **Version routing belongs to /governance.** ARC-142 / MECH-545 / Q-104 default to v4; MECH-546 to v6 per
   ARC-100; GOV-CONTRACT-1 is v3 because governance rules apply now. The one V3-tractable cousin (reality-status
   boundary lesion) is flagged on MECH-545, not decided.
3. **Hardening deferred by design.** No `what_would_answer` drafted for any of the five (/thought-digestion).
   Q-104's severance assay and MECH-545's within-boundary control are the obvious first digestion targets.
4. **Thoughts 2-4 are the user's authoring programme.** Thought 2 (candidate invariants synthesis) is the
   one that populates the ledger and is the natural next raw thought; a /lit-pull fan-out across the six
   domains for the five lesion-named invariants would feed it. Chipped as a lit-pull, not as authoring.
5. **Do not collapse the four thoughts prematurely** -- the raw thought says so explicitly (s.21).
