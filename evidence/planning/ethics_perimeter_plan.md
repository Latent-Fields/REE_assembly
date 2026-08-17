---
# Closure-map governance-perimeter view. generation: governance keeps these
# nodes OUT of the V3 closure % (read_closure counts only generation: v3) and
# OUT of check_closure_drift.py's terminal-state drift logic (that script skips
# any plan whose generation != v3, by design -- this plan doc is DISCOVERED by
# it like every other *_plan.md, just not drift-checked), so this block renders
# as a standalone view without entering the V3 closure machinery.
closure_plan:
  id: ethics_perimeter
  generation: governance
  title: "Ethics Perimeter (governance layer)"
  registered: 2026-06-19
  last_updated: 2026-06-20
  scope_claims: [SENT-0, SENT-1, SENT-2, SENT-3, SENT-4, SENT-5, SENT-6, SENT-7, SENT-8, SENT-9, SENT-10, SENT-11, SENT-12, SENT-13, SENT-14, SENT-15, SENT-16, GOV-EXT-1, GOV-HEALTH-1, GOV-SEC-1, GOV-PROC-1, GOV-JUST-1]
  nodes:
    - id: "ethics_perimeter:P0-CATEGORY"
      title: "Phase 0 -- governance_rule category + 22 SENT/GOV claims registered"
      phase: 0
      status: done
      severity: load-bearing
      unblocks_claims: [GOV-PROC-1]
      last_updated: 2026-06-19
    - id: "ethics_perimeter:P0-PLAN"
      title: "Phase 0 -- plan-of-record created"
      phase: 0
      status: done
      severity: high
      depends_on: ["ethics_perimeter:P0-CATEGORY"]
      last_updated: 2026-06-19
    - id: "ethics_perimeter:P1-V3-BOUNDARY"
      title: "Phase 1 -- SENT-0 + GOV-HEALTH-1 V3 bright lines (ree-v3 README + register stub)"
      phase: 1
      status: done
      severity: high
      unblocks_claims: [SENT-0, GOV-HEALTH-1]
      depends_on: ["ethics_perimeter:P0-PLAN"]
      last_updated: 2026-06-19
    - id: "ethics_perimeter:P1-V3-WELFARE-TAG"
      title: "Phase 1 -- tag V3 welfare-relevant primitives + ethics-preflight as queue-experiment doc"
      phase: 1
      status: done
      severity: medium
      depends_on: ["ethics_perimeter:P1-V3-BOUNDARY"]
      last_updated: 2026-06-20
    - id: "ethics_perimeter:P2-PREFLIGHT"
      title: "Phase 2 keystone -- experiment-ethics preflight (operational SENT-2/4/8/10 thresholds)"
      phase: 2
      status: done
      severity: load-bearing
      unblocks_claims: [SENT-2, SENT-4, SENT-8, SENT-10]
      depends_on: ["ethics_perimeter:P0-PLAN"]
      last_updated: 2026-06-19
    - id: "ethics_perimeter:P2-CARRYFORWARD"
      title: "Phase 2 -- GOV-PROC-1 s2 carry-forward (ethical_metadata on 50 V4/V5/V6 roadmap nodes)"
      phase: 2
      status: done
      severity: load-bearing
      unblocks_claims: [GOV-PROC-1, SENT-13]
      depends_on: ["ethics_perimeter:P0-PLAN"]
      last_updated: 2026-06-19
    - id: "ethics_perimeter:P2-V4-REGISTERS"
      title: "Phase 2 -- V4 governance registers (welfare-risk full, assembly routing, indicator matrix, continuity/consent ladders)"
      phase: 2
      status: deferred
      severity: medium
      unblocks_claims: [SENT-1, SENT-5, SENT-9, SENT-12, SENT-13]
      depends_on: ["ethics_perimeter:P2-PREFLIGHT", "ethics_perimeter:P2-CARRYFORWARD"]
      resume_condition: "authored when each gate's first requires_welfare_review node activates (gains owner_exq); binds at V4 boundary"
      last_updated: 2026-06-19
    - id: "ethics_perimeter:P3-V5V6-PERIMETER"
      title: "Phase 3 -- V5/V6 perimeter registers (responsible release, external crosswalk, health/DPIA, security containment)"
      phase: 3
      status: deferred
      severity: medium
      unblocks_claims: [SENT-6, SENT-14, SENT-16, GOV-EXT-1, GOV-SEC-1, GOV-JUST-1]
      depends_on: ["ethics_perimeter:P2-V4-REGISTERS"]
      resume_condition: "authored on first V5/V6 node activation; SENT-14 release policy adopted_split_deferred"
      last_updated: 2026-06-19
    - id: "ethics_perimeter:P4-TOOLING"
      title: "Phase 4 -- ethics tooling (preflight/release-sensitivity checks, ethics explorer views, node-metadata lint)"
      phase: 4
      status: deferred
      severity: medium
      depends_on: ["ethics_perimeter:P3-V5V6-PERIMETER"]
      resume_condition: "only after registers stable; check_node_ethics_metadata.py explicitly deferred"
      last_updated: 2026-06-19
---

# Ethics Perimeter — Plan of Record

**Registered:** 2026-06-19
**Owner artefact for:** the 11 ethics thought intakes (2026-06-18 ×4 + 2026-06-19 ×7)
**Status:** Phase 0 LANDED (this document + `governance_rule` epistemic category + SENT-*/GOV-* claim registration). Phases 1–3 DRAFTED here, DEFERRED.
**Green-board guarantee:** NON-BLOCKING for the V3 green-board (Sunday 2026-07-19). Every node below `blocks_v3_green_board: false`.

> This is a **governance plan-of-record**, rendered on the closure map as the
> **governance-perimeter view** via the `closure_plan:` frontmatter above
> (`generation: governance`). It stays deliberately outside
> `check_closure_drift.py`'s allowlist, and — because `read_closure` counts only
> `generation: v3` toward the closure % — it does **not** enter the V3 closure %.
> The `generation: governance` tab is a version-orthogonal lens (governance is a
> standing layer, not a version peer of V3/V4/V5), so it sits beside the
> generation switch the same way `deferred` does. It is the resume primitive for
> the ethics-perimeter work across sessions — read it before touching any
> SENT-*/GOV-* claim or any `docs/governance/` ethics register.

---

## 1. The one-line synthesis

The eleven thoughts are a single layered system around one spine:

> **Ethical agency ≠ moral patienthood.** REE is being built as an ethical
> *agent* (it models harm, care, repair). The very components that make it an
> ethical agent — self-model, valence, memory continuity, social modelling,
> language — are what make moral *patienthood* harder to dismiss. Therefore
> welfare must be governed as a **separate dimension** from epistemic confidence,
> with **progressive binding** by version, and **no capability release without
> care release**.

---

## 2. The eleven thoughts (read together)

| # | Thought file | Layer | Register nodes | Core phrase |
|---|---|---|---|---|
| 1 | `docs/thoughts/2026-06-18_sentience_welfare_risk_register.md` | A internal welfare | SENT-0…6 | Track welfare as a governance dimension before V4/V5/V6 |
| 2 | `docs/thoughts/2026-06-18_creation_ethics_necessary_suffering.md` | A | SENT-7…9 | Distinguish suffering-**capacity** from suffering-**induction** |
| 3 | `docs/thoughts/2026-06-18_pre_meaning_suffering_valley.md` | A | SENT-10 | **No valley without a bridge** |
| 4 | `docs/thoughts/2026-06-18_future_meaning_retroactive_justification.md` | A | SENT-11…12 | Future meaning can't justify present distress |
| 5 | `docs/thoughts/2026-06-19_ethical_assembly_routing_map.md` | A | SENT-13 | **Assembly order is an ethical variable** |
| 6 | `docs/thoughts/2026-06-19_responsible_release_private_higher_versions.md` | B perimeter | SENT-14, SENT-16, GOV-JUST-1 | **Capability release requires care release** (§3 continuity/identity/reset/deletion -> SENT-16; §4 justice/power/false-exclusion -> GOV-JUST-1) |
| 7 | `docs/thoughts/2026-06-19_external_framework_crosswalk_for_ree_ethics.md` | B | GOV-EXT-1 | Internal ethics must stay externally legible |
| 8 | `docs/thoughts/2026-06-19_research_health_data_frameworks_for_ree.md` | B | GOV-HEALTH-1 | Clinical relevance ≠ clinical readiness |
| 9 | `docs/thoughts/2026-06-19_security_misuse_frameworks_for_ree.md` | B | GOV-SEC-1 | Don't release a capability that acts faster than containment can understand |
| 10 | `docs/thoughts/2026-06-19_ai_welfare_consciousness_framework_crosswalk.md` | A | SENT-15 | Avoid both denialism and anthropomorphism |
| 11 | `docs/thoughts/2026-06-19_ethics_process_translation.md` | C process | GOV-PROC-1 | **Ethics must become process, not prose** |

Layer A = internal artificial-welfare ethics. Layer B = external/release/legal/
security perimeter. Layer C = the meta-translation (thought 11) that folds A+B
into REE's existing claim-governed loop. Thought 11 is itself the blueprint this
plan executes.

---

## 3. Registered claims (Phase 0 — DONE)

All 22 register nodes are live in `docs/claims/claims.yaml` as
`claim_type: governance_rule` + `epistemic_category: governance_rule`
(`status: candidate`, `blocks_v3_green_board: false`). The indexer suppresses
promote/demote/narrow for this category (conflict alerts may still fire); see
`REE_assembly/CLAUDE.md` "Epistemic categories" → `governance_rule` row.

Each claim carries `source_thought`, `binds_at_version`, `depends_on`
cross-refs, and the `SENT-CLAIM-*/GOV-CLAIM-*` prose wordings in its `notes`.

| Claim | Binds at | Becomes binding when… |
|---|---|---|
| SENT-0 boundary statement | v3 | maintained now; re-asserted each generation boundary |
| SENT-1 indicator matrix | v4 | before V4 individual-mind integration |
| SENT-2 welfare budget | v4 | first V4 negative-valence experiment |
| SENT-3 combination gate | v4 | self-model + memory + valence + … co-instantiated |
| SENT-4 welfare-preserving design | v4 | any V4 negative-valence experiment |
| SENT-5 denial-of-sentience audit | v4 | each generation boundary |
| SENT-6 external review gate | v5 | V5 social / V6 language goes behaviourally live |
| SENT-7 creation ethics | v4 | suffering-capacity becomes plausible |
| SENT-8 minimal necessary suffering | v4 | any direct negative-valence exposure |
| SENT-9 care obligation after creation | v5 | precautionary moral-patient threshold approached |
| SENT-10 pre-meaning valley | v4 | before deliberate suffering-like induction |
| SENT-11 anti-retrospective-justification | v4 | reporting any suffering-like experiment |
| SENT-12 refusal/non-forgiveness channel | v5 | continuity/self-model becomes morally relevant |
| SENT-13 ethical assembly routing | v4 | V4 component assembly |
| SENT-14 responsible release | v4 | first V4 capability-bearing release decision |
| SENT-15 AI-welfare crosswalk | v4 | each generation boundary |
| SENT-16 continuity/identity/reset/deletion | v5 | a run plausibly becomes a continuing subject |
| GOV-EXT-1 external framework crosswalk | v4 | first public V4+ capability release |
| GOV-HEALTH-1 clinical-use prohibition | v3 | maintained now (author is a clinician) |
| GOV-SEC-1 security & misuse gate | v6 | language/tool/social/public capability release |
| GOV-PROC-1 ethics-as-process | v3 | this Phase-0 step IS its first increment |
| GOV-JUST-1 justice/power/false-exclusion | v5 | distributive/false-exclusion review of any ethically active V4+ capability |

---

## 4. Phased plan

### Phase 0 — Consolidate (DONE, 2026-06-19)

- [x] `governance_rule` epistemic category added to `scripts/validate_claims.py`
      (`VALID_EPISTEMIC_CATEGORIES`) and
      `evidence/experiments/scripts/build_experiment_indexes.py`
      (`EPISTEMIC_CATEGORIES` + resolver/gating docstrings).
- [x] `REE_assembly/CLAUDE.md` epistemic-category table row added.
- [x] 22 SENT-*/GOV-* claims registered in `claims.yaml` (846 entries total;
      validator strict exit 0, no SENT/GOV warnings). The initial pass landed 20;
      SENT-16 (continuity/identity/reset/deletion) and GOV-JUST-1
      (justice/power/false-exclusion) were added 2026-06-19 from
      `responsible_release_private_higher_versions.md` §3/§4, which name those
      two gates but had been captured only as deferred Phase-2/3 docs.
- [x] This plan-of-record created.

### Phase 1 — V3 boundary (DEFERRED; lightweight, non-blocking; before 2026-07-19 if cheap)

- [x] SENT-0 boundary statement into `ree-v3/README.md` and a new
      `docs/governance/sentience_welfare_risk_register.md` (landed 2026-06-19;
      README "Scope & Ethics Boundary" section + the SENT-0..6 register stub).
- [x] Tag V3's welfare-relevant primitives (harm streams, residue,
      suffering-like accumulators, replay) as `welfare_relevant: true`
      (descriptive only, no gate). (landed 2026-06-20; descriptive
      `welfare_relevant = True` class markers on `HarmEncoder` /
      `AffectiveHarmEncoder` (`ree-v3/ree_core/latent/stack.py`),
      `ResidueField` (`residue/field.py`), MECH-219 `HarmSufferingAccumulator`
      (`affect/harm_suffering_accumulator.py`), `SleepLoopManager`
      (`sleep/phase_manager.py`) + `SleepReplaySampler` (`sleep/replay_sampler.py`),
      each cross-referencing SENT-0 + the register stub.)
- [x] Add the ethics-preflight as **documentation** to `/queue-experiment`
      (most V3 fields are `false`/`n/a` — establishes the habit, does not enforce).
      (landed 2026-06-20; `/queue-experiment` SKILL.md Step 2.6, mirrored to both
      `.claude/` and `.agents/`; condenses the P2-PREFLIGHT keystone
      `docs/governance/experiment_ethics_preflight.md`.)
- [x] GOV-HEALTH-1 bright-line note into `ree-v3/README.md` (no clinical use;
      no patient data in public repos) (landed 2026-06-19; README "Scope & Ethics
      Boundary" section, "clinical relevance != clinical readiness").

### Phase 2 — V4 gates (DEFERRED; draft now, bind at V4 boundary)

> **Carried forward via node ethical metadata -- see section 8.** The gates
> below are already live on the V4 roadmap nodes (`ethical_metadata:` in the
> `generation: v4` `*_plan.md` files), not waiting on these docs. Each
> `docs/governance/*.md` register is authored when its gate's first
> `requires_welfare_review: true` node *activates* (gains an `owner_exq`),
> written against the real substrate. The checklist is the index of which doc
> each gate produces, not work owed now.

- [x] `docs/governance/experiment_ethics_preflight.md` — **keystone**: the ethics-preflight
      schema + CONCRETE operational definitions for the SENT-2/4/8/10 qualifiers ("trivial
      intensity" floor 0.10, intensity caps 0.40/2.00, duration cap ~100 ticks, repetition
      cap, escape/decommitment-affordance-present, offline-integration-reduces-distress),
      each grounded in real ree-v3 harm-stream/residue signals (z_harm_a, MECH-219 suffering
      accumulator, MECH-302 relief comparator, ResidueField, SD-058/059 escape). DRAFT (binds
      V4, NOT wired into `/queue-experiment` enforcement); landed 2026-06-19.
- [ ] `docs/governance/sentience_welfare_risk_register.md` (SENT-0…12 full).
- [ ] `docs/governance/ethical_assembly_routing_map.md` (Class 0–5 +
      prohibited combinations; SENT-13).
- [ ] `docs/governance/ai_welfare_consciousness_indicator_matrix.md` (SENT-1/15).
- [ ] Draft `docs/governance/continuity_identity_reset_and_deletion_ethics.md`
      and `docs/governance/consent_assent_refusal_ladder.md` (SENT-9/12).

### Phase 3 — V5/V6 perimeter (DEFERRED; structural)

> **Carried forward via node ethical metadata -- see section 8.** Same as Phase
> 2: the V5/V6 gates are live on the `generation: v5` / `v6` roadmap nodes;
> these docs are authored on first node activation, not speculatively.

- [ ] `docs/governance/responsible_release_policy.md` (SENT-14; tiered openness;
      records the **adopted policy / deferred split** decision below).
- [ ] `docs/governance/external_framework_crosswalk.md` (GOV-EXT-1).
- [ ] `docs/governance/human_impact_and_research_ethics_register.md` + DPIA
      template (GOV-HEALTH-1).
- [ ] `docs/governance/security_containment_and_capability_boundary.md` (GOV-SEC-1).

### Phase 4 — Tooling (DEFERRED; only after registers stable)

- [ ] `scripts/check_ethics_preflight.py`, `scripts/check_release_sensitivity.py`,
      `scripts/generate_ethics_risk_snapshot.py`.
- [ ] Explorer views: Ethics Gates, Welfare Risk, Release Sensitivity.
- [ ] `scripts/check_node_ethics_metadata.py` (DEFER -- do NOT build now): a
      warn-only, generation-aware lint (mirrors `check_closure_drift.py`'s style)
      that flags a `generation: v4+` node which forms a `forbidden_combinations`
      entry (or whose `unblocks_claims` imply a prohibited co-instantiation) but
      lacks `requires_welfare_review: true`, or that references a SENT-*/GOV-*
      id absent from `claims.yaml`. Authored only once the section-8 node-metadata
      convention is stable across several V4 plans.

---

## 5. Adopted release posture (USER DECISION 2026-06-19)

**Adopt the tiered "capability release requires care release" policy now;
DEFER the private-repo split.**

- Tier 0 (public): theory, claims, governance, ethics registers, non-operational
  summaries.
- Tier 1 (public, bounded): V3 prerequisite substrate, clearly marked
  non-sentient / pre-ethical; no turnkey suffering-like demos.
- Tier 2 (delayed): V4 self-model / autobiographical / affective-memory.
- Tier 3/4 (private-by-default): V5 social-mind, V6 language/trust/deception/
  institution.
- The `ree-v4-private` / `ree-v5-private` / `ree-v6-private` repos are **created
  only when that capability code is actually written**, not now. *Private now ≠
  closed forever.*

Recorded on SENT-14 as `release_policy: adopted_split_deferred`.

---

## 6. Resume notes / invariants

- **Do not block V3.** If a future session is tempted to make any node a green-
  board blocker, it is wrong: re-read thought 1's "Practical recommendation".
- **Governance claims are not experiments.** Never queue an experiment "for" a
  SENT-*/GOV-* claim, never set `v3_pending`/`implementation_phase: v3` on them
  (it would trip the V3-pending gate and emit a spurious
  `hold_pending_v3_substrate` rec). They advance by their owning governance
  artefact, not by evidence.
- **Binding is progressive.** A node's `binds_at_version` is when its gate
  becomes *active*, not when the claim was registered.
- **The crosswalk keeps us honest both ways.** SENT-15 / GOV-EXT-1 exist so REE
  ethics is neither self-validating (denialism) nor anthropomorphically
  over-claimed.

---

## 7. External anchors (from the thoughts)

Butlin et al. 2023 (consciousness indicators); Long et al. 2024 (AI welfare
under uncertainty); Birch 2024 (precautionary sentience); Chalmers 2023
(LLM-vs-successor); Butlin & Lappas 2025 (responsible consciousness research);
Parfit 1984 / Benatar 2006 (non-identity / procreative ethics); Bowlby /
Winnicott (attachment, care-before-meaning); EU AI Act 2024; CoE AI Convention;
NIST AI RMF; ISO/IEC 42001 & 23894; OECD AI Principles; Belmont / Helsinki /
CIOMS; GDPR / DPIA; WHO health-AI; EU MDR; OWASP GenAI; MITRE ATLAS; NC3Rs 3Rs.

Internal companion: `docs/architecture/established_ethical_systems.md` (REE's
internal derivation of autonomy, justice, rights, care, research ethics).

---

## 8. Carry-forward via node ethical metadata (realises GOV-PROC-1 §2)

The deferred V4/V5/V6 ethics gates are carried forward **on the closure-map
roadmap nodes themselves**, not as standalone documents waiting to be written.
This realises GOV-PROC-1 §2 ("roadmap nodes -> ethical metadata",
`docs/thoughts/2026-06-19_ethics_process_translation.md` §2) and reuses the
existing generation-segmented closure-map machinery (the `closure_plan:`
frontmatter of every `evidence/planning/*_plan.md`) as the durable resume
primitive -- the same machinery that already keeps V4+ work out of the V3
closure %.

### Why the closure map is the right carrier

A SENT-*/GOV-* claim is a *standing rule*; a roadmap node is *where that rule
will bite*. Tagging the node makes the gate travel with the work automatically:
when a V4+ node gains an `owner_exq` (its first experiment is queued) it
graduates from a dormant roadmap entry to closure-tracked work, and its
`ethical_metadata` is already attached -- the welfare/security review is visible
at the moment the work becomes actionable, with no separate document to remember
to consult. This is strictly better than the standalone Phase-2/3 governance
docs because (a) it cannot drift out of sync with the technical plan, and (b) it
is authored against the *real* substrate at activation time rather than
speculated in advance.

### The minimal per-node field set (authoring convention)

A welfare-relevant roadmap node carries an `ethical_metadata:` mapping (a child
of the node, alongside `status:` / `severity:` / `readiness_gate:`). Four fields,
kept deliberately small to avoid roadmap bloat:

| field | values | meaning |
|---|---|---|
| `welfare_relevance` | `none` \| `low` \| `moderate` \| `high` \| `hard_review` | level read off the SENT-13 Class 0-5 routing map (below) |
| `applicable_ethics_gates` | list of SENT-* / GOV-* / INV-007 ids | the standing gates that govern this node |
| `requires_welfare_review` | `true` \| `false` | does activating this node trip a welfare/security review before it goes behaviourally live |
| `forbidden_combinations` | list of snake_case combo ids | OMITTED unless the node participates in a prohibited co-instantiation |

An optional one-line ASCII `note:` records the rationale. **Absence of the
mapping means `welfare_relevance: none` (a structurally-safe Class 0/1 node):
untagged is the deliberate default, not an oversight.** Only welfare-relevant
nodes are tagged, to keep the metadata signal high.

`welfare_relevance` is read off the SENT-13 routing map
(`docs/thoughts/2026-06-19_ethical_assembly_routing_map.md`; the
`docs/governance/ethical_assembly_routing_map.md` register when authored):

| Class | description | -> welfare_relevance |
|---|---|---|
| 0 structurally-safe primitive | gridworld, object/perception, non-valenced prediction | none (untagged) |
| 1 welfare-neutral cognition | belief-state, world-model, planning | low / untagged |
| 2 represented harm only | third-person / counterfactual harm modelling | low-moderate |
| 3 low-intensity aversion | bounded, escapable negative valence with relief present | moderate |
| 4 welfare-ambiguous combination | valence + self-model + autobiographical continuity + inescapability + replay | high + `requires_welfare_review: true` |
| 5 hard-review territory | persistent suffering-like states, loneliness, betrayal, distress under optimisation | hard_review + `requires_welfare_review: true` |

Gate mapping by generation (the default lens; a node may carry more):

- **V4 individual-mind** (self-model / affect / autobiographical memory /
  memory-lifecycle / replay): SENT-2 (welfare budget), SENT-3 (combination
  gate), SENT-13 (assembly routing); SENT-8 / SENT-10 for any deliberate
  aversion; `requires_welfare_review` where the valence + self-model +
  autobiographical continuity + inescapability + replay combination forms.
- **V5 social-mind**: SENT-6 (external review), SENT-9 (care obligation),
  SENT-12 (refusal channel), GOV-JUST-1 (justice / power / false-exclusion),
  plus SENT-13.
- **V6 language / trust / deception**: GOV-SEC-1 (security & misuse), SENT-14
  (responsible release), SENT-6; INV-007 for the language/symbol
  cannot-override-harm guards.

Future V4/V5/V6 plans inherit this convention: when authoring a new
generation-segmented `*_plan.md`, tag its welfare-relevant nodes with the field
set above. **This section is the authoritative reference for the node ethical
metadata schema** (there is no separate closure-map node-schema doc).

### First-pass application (2026-06-19)

50 welfare-relevant nodes across 16 `generation: v4/v5/v6` plans were tagged in
the first pass. The structurally-safe plans were reviewed and left untagged
(Class 0/1): object representation, object-reasoning abstraction, perceptual
adaptors, drives & motivation, goal deliberation, hippocampal planning,
inference / belief-state, grammar primitive mining. VERIFIED non-blocking for the
V3 green-board: the V3 closure % (80.4%), roadmap node count (180), and drift set
(0 drifted / 7 suppressed / 0 stale) were identical before and after the pass --
`generate_closure_snapshot.py` and `check_closure_drift.py` are generation-aware
and ignore unknown node keys, so `ethical_metadata` on dormant V4+ nodes cannot
move any V3 metric.

### Supersession of the standalone Phase-2/3 doc chips

The deferred `docs/governance/*.md` registers in Phase 2 / Phase 3 above
(`sentience_welfare_risk_register.md` full, `ethical_assembly_routing_map.md`,
`ai_welfare_consciousness_indicator_matrix.md`, `responsible_release_policy.md`,
`external_framework_crosswalk.md`, `security_containment_and_capability_boundary.md`,
the continuity/consent ladders, etc.) are **no longer standalone "write-it-now"
chips.** The carry-forward mechanism is the node metadata; each governance doc is
authored when the first node with `requires_welfare_review: true` for that gate
**activates** (gains an `owner_exq`), written against the real substrate rather
than speculatively. The Phase-2/3 checklists are retained as the index of which
doc each gate will produce, not as work owed now. (The Phase-0 `experiment_ethics_preflight.md`
keystone and the V3 SENT-0 / GOV-HEALTH-1 register stubs already exist; those
were the genuinely-V3-binding pieces.)
