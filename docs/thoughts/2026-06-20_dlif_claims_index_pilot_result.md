# Claims-Index DLIF Pilot — Manual Pass Result

Status: processed
Processed in:
- `docs/claims/claims.yaml` (SD-062 `claims-index as a typed multi-axis structured-uncertainty graph` -- the surviving constructive outcome of the DLIF line, applied to the claims registry rather than to REE cognition. This file is cited in that claim's `sources`.)
- `docs/claims/claims.yaml` (Q-079 `structured_uncertainty_field_distinctness` -- the DLIF / structured-uncertainty field question; verdict ANSWERED-NEGATIVE: DLIF is NOT a distinct mathematical object, it decomposes into factor-graph unification + Bayesian-nonparametric structure learning + active inference + ARC-013 residue. This file is cited in that claim's `sources`.)


**Date:** 2026-06-20
**Status:** pilot_result / analysis (doc-only; no claims.yaml or evidence edits)
**Scope:** executes the manual Claims-Index DLIF pass prescribed in
`2026-06-20_dlif_next_action_claims_index_pilot_plan.md` over the 8-file DLIF /
structured-uncertainty-field thought cluster saved 2026-06-20.
**Primary benchmark note:** preserve the REE-v3 strict green-board target of
**Sunday 19 July 2026**. This pilot is doc-only triage; it adds no v3 implementation scope.

---

## 0. What this pilot is

The cluster's own next-action plan says the lowest-cost way to find out whether the
Dynamic Latent Information Field (DLIF) idea is *useful* is to run it once, by hand, over
its own thought cluster, and produce: a projected claim graph, a hidden-assumption list, a
conflict/residue report, scale recommendations, and a next-action recommendation — then
compare against an ordinary reading and apply the cluster's own kill criteria.

This document is that pass. It treats DLIF as a **method under test**, not an adopted
formalism. The honest verdict (Section 9) is the point.

### Field schema applied (from the pilot plan)

Each proposition gets coarse field values: `belief`, `uncertainty`, `salience`,
`coherence_cost` (tension against the rest of the registry), `residue` (unresolved
moral/epistemic structure that must persist), `scale`, `ownership` (already in
`claims.yaml` or not), `roadmap`. Scales: `fragment | claim | mechanism |
architecture_principle | governance_tooling | research_line | experiment`.

Values are H/M/L. I report them, then in Section 9 ask honestly whether the *numbers*
did any work the structural reading didn't.

---

## 1. Field-object inventory (the cluster decomposed)

| # | Proposition (source doc) | belief | uncert | salience | coherence_cost | residue | scale | ownership | roadmap |
|---|---|---|---|---|---|---|---|---|---|
| P1 | REE needs a structured-uncertainty layer = directed-update **+** cyclic-coherence (`structured_uncertainty_layer`) | H | L | H | L | L | architecture_principle | **owned** (the cognifold is this) | v4+ |
| P2 | Residue = persistent **field deformation**, not scalar/memory (`graphs_as_projections`, `capture`) | H | L | M | ~0 | L | architecture_principle | **owned — near-duplicate of ARC-013** | active claim |
| P3 | Field is primitive; graphs/claims/nodes are **projections** ("Latent-Fields" is the thesis) (`graphs_as_projections`) | M-H | M | H | L | M | architecture_principle | **owned** (ARC-084 single-state-space framing) | v4+ |
| P4 | A brain-native **hybrid inference object** is a distinct math object worth its own repo (`brain_native`, `capture`, `research_map`) | M | **H** | H | M | **M** | research_line | **NEW / unowned** | research / v4+ |
| P5 | The **claims index itself** should be a typed multi-axis structured-uncertainty graph (`claims_index_as_structured_uncertainty_graph`) | M-H | **M→L** (see §7) | H | L | L | governance_tooling | **NEW / unowned** | pre-v3 useful, light |
| P6 | DLIF minimal formal spec `(M,q,E,Π,C,A,R,S,P)` + 5 discriminating tests (`minimal_formal_specification`) | M | H | M | M | M | research_line | derivative of P4 | research / v4+ |
| P7 | DLIF must **narrow**: has ancestors, residue needs ablation, add kill criteria (`critical_review_and_learning`) | H | L | H | **negative** (lowers cluster cost) | — | meta | — | now |
| P8 | Run the manual claims-index pilot first (`next_action_plan`) | H | L | M | L | — | action | — | now (this doc) |

**Owned anchors the cluster lands on** (read from `claims.yaml`):
- **ARC-013** — "Residue is persistent latent-space curvature." `active`. Evidence path = V3-EXQ-587 (GAP-10). → absorbs **P2**.
- **ARC-084** — typed signed cognifold coupling; cognifold = single interacting state-space. `candidate`, `substrate_conditional`, `implementation_phase: v4`. → absorbs **P3** (and the field-vs-edge tension, see C1).
- **MECH-363** — diffuse long-range competitive coupling as a generative stability requirement. `candidate`, `substrate_conditional`, v4. Empirical anchor Luppi et al. 2026. → neighbours **P1**.

---

## 2. Projected claim graph

Nodes are propositions/claims; edges are typed. `=>` directed, `--` undirected coherence.

```text
                         [cognifold cluster — OWNED, v4, substrate_conditional]
                          ARC-084 (single state-space, signed edge)
                            ^         ^
              P3 refines ___/          \___ P1 instantiates
              (field is                     (structured-uncertainty
               projection)                   layer = the cognifold)
                                                     |
                                              MECH-363 -- (long-range
                                               competition = stability)
                          ARC-013 (residue = latent curvature) <== P2 duplicates
                                  |
                                  | open evidence: V3-EXQ-587 (GAP-10)
                                  v
                          [residue separability — RESIDUE R2, inherited not added]

   [NEW, unowned]                              [NEW, unowned]
   P5 claims-index-graph                       P4 DLIF research object
      |  (governance_tooling)                     ^   (research_line)
      |  ~80-90% already true (§7)                |  narrowed_by
      v                                           P7 (critical review)
   register as design_decision,                   |  refines / kills-overclaim
   near-done                                      v
                                          P6 formal spec (gated on lit-drill + this pilot)
                                                   |
                                                   x  hidden-cause gridworld  — DEFER to V4, do not build
```

Edge inventory (typed, as the cluster's own edge vocabulary would have it):
`P1 instantiates ARC-084/MECH-363`; `P2 duplicates ARC-013`; `P3 refines ARC-084`;
`P4 generalises P1+P3`; `P6 operationalises P4`; `P7 narrows P4/P6`;
`P5 dispatches_to governance_tooling`; `P8 tests the whole cluster (this doc)`.

**Graph reading:** the cluster has a **dense owned core** (P1/P2/P3 all land on the
existing cognifold cluster) and a **thin genuinely-new rim** of exactly two nodes —
**P5** (governance tooling) and **P4** (research object) — with **P7** acting as a
narrowing edge that pre-emptively deflates P4's novelty. That is the entire net-new
surface area. Everything else is cross-reference.

---

## 3. Hidden-assumption list

Assumptions the cluster relies on but does not state. These are what the field-projection
exercise is supposed to surface, and they are the pilot's most defensible output.

- **HA1 — "field" buys computation, not just ergonomics.** The cluster asserts field-first
  is *better* than graph-first, but the critical review's own "discrete-not-continuous"
  minimal object (`LatentCell` list + constraints + projections) **is isomorphic to a
  typed factor graph + a scale layer**. The likely truth: field-first buys
  *representational ergonomics* (it names pre-node ambiguity cleanly) but no new
  computational power over a typed dynamic factor graph. If so, P4's novelty is notational.
- **HA2 — residue is separable from salience + uncertainty.** The review *flags* the
  ablation (residue vs salience-only vs uncertainty-only) but *assumes* residue survives
  it. This is not a DLIF question — it is **ARC-013's open evidence question** (V3-EXQ-587).
  DLIF inherits it; it does not add evidence for it.
- **HA3 — the claims-index and the agent use the same object.** The cluster repeatedly
  asserts one object describes both cognition and the registry. "REE_assembly is
  externalised cognition" is a *methodological framing*, not a claim that the registry runs
  agent inference. Treating the symmetry as literal risks a pun (cf. the standing
  "triage real abstraction vs pun" discipline).
- **HA4 — granularity-zoom is one operator family.** The named scales run sensory →
  trajectory → goal → **ethical constraint**. Perceptual coarsening and ethical-precedence
  selection are not the same operation; one `coarsen()/refine()` axis conflates them.
- **HA5 — projection loss is measurable without a ground-truth field.** If the field is
  only ever *observed through* projections, `projection_fidelity` has no denominator. The
  review makes projection-loss "central" but never says what it is measured against.
- **HA6 — the literature drill can establish novelty.** The research map already shows 10
  formalisms each covering one needed capacity; "the gap is the combination" is a *weaker*
  novelty claim than "a new object," and a combination-of-known-pieces may be an
  engineering synthesis, not a mathematical discovery.

---

## 4. Conflict / residue report

**Conflicts (preserve, do not collapse):**
- **C1 — primitive edge (ARC-084) vs projected edge (P3).** ARC-084 makes the typed signed
  *edge* first-class; P3 makes the *field* primitive and the edge a projection. Resolvable
  by scale: ARC-084 is the v4 substrate *commitment*; P3 is a meta-claim about
  *representation*. They are not actually rivals — but the registry should record the
  tension rather than silently picking one.
- **C2 — "deserves its own repo" (P4) vs "don't create a folder until proven useful" (P8).**
  Self-aware in the cluster. Resolved by sequencing: this pilot gates the repo.

**Residue (must persist into later work — do not let enthusiasm erase):**
- **R1 — the novelty question (highest-value residue).** Is DLIF a *new mathematical
  object* or a *re-notation* of dynamic-factor-graphs + active-inference + ARC-013-residue?
  P7 deforms the cluster toward "narrow the claim" but does **not** resolve it. This residue
  must survive into the literature drill as its *first* question, not its conclusion. (See
  HA1, HA6.)
- **R2 — residue separability (inherited).** = HA2 = ARC-013's V3-EXQ-587. The cluster adds
  language for it; it adds no evidence. Keep the open marker on ARC-013, do not let the
  DLIF re-statement read as if it were independent confirmation.

---

## 5. Scale recommendations (fold / register / defer)

- **Fold (cross-ref, do NOT register new claims):** P1 → ARC-084/MECH-363; **P3 → ARC-084**.
  Add a `depends_on` / notes cross-ref and a `source_thought` pointer; no new ids.
- **Merge (do NOT register):** **P2 is a near-duplicate of ARC-013** in field language. Add
  a one-line note to ARC-013 ("residue-as-field-deformation = this; cf. DLIF cluster
  2026-06-20") and a `source_thought` pointer. Registering it would be the exact
  proliferation the discrimination gate exists to refuse.
- **Register (NEW, light):** **P5** (claims-index-graph) as a `design_decision` /
  governance-tooling claim — but **de-scoped to "near-done"** given §7. Its
  `what_would_answer` is the schema-audit + an explorer view, not a research programme.
- **Register (NEW, gated):** **P4** (DLIF research object) as a single `research_anchor` /
  `out_of_domain`-leaning claim, `version_relevance: v4_v5`, off the v3 board, with
  `what_would_answer` = R1 (the novelty falsifier) and a `depends_on` cross-ref to
  ARC-084/ARC-013. Do **not** refine into the full P6 tuple yet.
- **Defer (do NOT build):** the hidden-cause gridworld / DLIF agent substrate → V4.

---

## 7. claims.yaml axis-coverage audit (P5's real status)

P5 proposes nine "multi-axis claim state" axes. Audited against the live `claims.yaml`
(857 claims) + indexer-derived fields:

| P5 axis | Already in the registry? | Field(s) |
|---|---|---|
| truth confidence | partial | `confidence` (22); lit_conf in `claim_evidence.v1.json` |
| evidence strength | **yes** | exp_conf (`claim_evidence.v1.json`), `evidence`, `evidence_quality_note` (343), `literature_evidence` |
| implementation dependence | **yes** | `implementation_phase` (468), `depends_on` (844), `implementation_note` |
| conflict burden | **yes** (derived) | indexer conflict_ratio |
| roadmap relevance | **yes** | `version_relevance` (129), `implementation_phase`, `binds_at_version` (22) |
| experiment status | **yes** | `claim_evidence.v1.json`, `evidence_direction` |
| ethical risk | **partial** | no per-claim scalar; the SENT-*/GOV-* governance_rule layer exists separately |
| v3-blocking status | **yes** | `v3_pending` (288) **+ a literal `blocks_v3_green_board` field (22)** |
| dispatch status | partial | `location` (692), `instantiates` (19), substrate_queue / convergence_demand_queue |

Plus axes P5 didn't even ask for that already exist: `epistemic_category` (242),
derived `epistemic_stance`, `what_would_answer` (33), `claim_level` (259),
`pending_substrate_reconfirmation` (29), `lifecycle_stage`.

**Finding: ~7 of 9 axes are already first-class; the directed typed-edge backbone
(`depends_on`, 844 edges; plus `supersedes` via status, `instantiates`, `emergent_from`)
is already there.** P5's thesis — "the claims index should *become* a typed multi-axis
structured uncertainty graph" — is **already 80-90% true**. The genuine gap is small:
(1) an explicit per-claim **ethical-risk** axis (or a typed edge to the SENT-*/GOV-* layer),
and (2) richer **typed edge labels** beyond `depends_on` (the cluster lists `contradicts`,
`refines`, `tested_by`, `narrows`, `dispatches_to` — most are implicit today). This is a
schema tidy + maybe an explorer view, **not** a probabilistic-inference engine.

---

## 8. Next-action recommendation

1. **Track A registration (when the governance cycle releases `claims.yaml`):** register
   exactly **two** new claims — P5 (claims-index-graph, de-scoped to near-done
   design_decision) and P4 (DLIF research object, gated `research_anchor`) — and
   cross-ref P1/P2/P3 into ARC-013/ARC-084/MECH-363. Net new ids: **2**, not 8. This doc is
   the spec for that pass.
2. **Cheapest discriminating probe is NOT the gridworld** — it is the axis audit above,
   already done. It converts P5 from "research" to "small schema task," which is the single
   most useful governance output of the cluster.
3. **For P4, the next step is a literature drill with R1 as its first question**, not a toy
   build: *does any single formalism already combine directed-update + cyclic-coherence +
   latent-node birth/death + scale-shift?* (dynamic factor graphs + structure learning come
   closest). A `/lit-pull`, not an experiment. If the answer is "yes, mostly," P4 collapses
   to a synthesis note and the standalone repo is **not** warranted.
4. **Do not** create `docs/research/dlif/`, build the field engine, or touch v3 — all
   explicitly out of scope per every doc in the cluster.

---

## 9. Kill-criteria evaluation — did DLIF-as-method beat ordinary reading?

The cluster supplies its own kill criteria. Applied honestly to *this pass*:

| Kill criterion (from the plan) | Verdict on this pass |
|---|---|
| Performs no better than an ordinary claim graph | **Mixed** — see below |
| Residue predicts nothing beyond salience/uncertainty | **FIRED** — the residue/salience *numbers* in §1 predicted nothing the structural read didn't |
| Scale-shift adds vocabulary without improving decisions | **Partially fired** — scale labels helped triage (fold/register/defer); the numeric fields did not |
| Projection loss cannot be described/reviewed | **FIRED** — HA5: no denominator for fidelity |
| Outputs less clear than the source docs | **Did not fire** — the fold/merge/register/defer disposition + the §7 audit are clearer than the source |
| Creates scope creep for v3 | **Did not fire** — doc-only, 2 new claims, no code |

**Honest verdict — DLIF-as-method is *partially* useful, and useful in a specific,
narrow way:**

- **What earned its keep:** the *projection / scale / fold-vs-register vocabulary* forced
  the explicit owned-vs-new split (only P4 + P5 are net-new; P1/P2/P3 fold) and surfaced
  HA1 (field = re-notation risk) and HA3 (claims-index = agent pun risk) that an
  enthusiastic linear read would skate past. The §7 axis audit — prompted by taking P5's
  "multi-axis" claim literally and checking it against the schema — is the highest-value
  output and de-risked a whole "research project" down to a tidy.
- **What did not:** the **quantitative field substrate** (belief/salience/residue numbers
  per node) added nothing over a typed-claim-graph read. The dispositions followed from
  ordinary structural reasoning — *is it a duplicate? is it owned? is it falsifiable?* —
  not from the field values. **This is DLIF kill-criterion #2/#3 firing on DLIF itself.**

**Net:** the pilot SUCCEEDS as governance triage (the *vocabulary* is a useful lens) and
FAILS to justify the *field formalism as computation* over a typed dynamic factor graph
(HA1, R1 unresolved). That is exactly the discriminating result the cluster asked for, and
it routes cleanly:

- **Keep** the field/projection/residue *language* as a thinking aid and as cross-refs into
  the cognifold cluster.
- **Register** P5 (near-done) and P4 (gated on the R1 literature drill).
- **Do not** build the DLIF engine, the gridworld, or the standalone repo until the R1
  novelty question is answered against the literature — and treat HA1 as the live risk that
  it never will be.

---

## Open items handed forward

- **Track A** (this doc is its spec): register P4 + P5, cross-ref P1/P2/P3, when
  `claims.yaml` is free. Net-new ids: 2.
- **R1 literature drill** (`/lit-pull`): novelty falsifier for P4. First, not last.
- **R2 / HA2**: leave ARC-013's V3-EXQ-587 open marker untouched; the DLIF cluster is not
  independent evidence.
- Repo decision (`structured-uncertainty-fields`): **gated** on R1 + P5 utility; not now.
</content>
</invoke>
