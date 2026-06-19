# Ethics Perimeter — Plan of Record

**Registered:** 2026-06-19
**Owner artefact for:** the 11 ethics thought intakes (2026-06-18 ×4 + 2026-06-19 ×7)
**Status:** Phase 0 LANDED (this document + `governance_rule` epistemic category + SENT-*/GOV-* claim registration). Phases 1–3 DRAFTED here, DEFERRED.
**Green-board guarantee:** NON-BLOCKING for the V3 green-board (Sunday 2026-07-19). Every node below `blocks_v3_green_board: false`.

> This is a **governance plan-of-record**, not a closure plan. It is deliberately
> outside `check_closure_drift.py`'s allowlist, so it does not enter the V3
> closure %. It is the resume primitive for the ethics-perimeter work across
> sessions — read it before touching any SENT-*/GOV-* claim or any
> `docs/governance/` ethics register.

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
| 6 | `docs/thoughts/2026-06-19_responsible_release_private_higher_versions.md` | B perimeter | SENT-14 | **Capability release requires care release** |
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

All 20 register nodes are live in `docs/claims/claims.yaml` as
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
| GOV-EXT-1 external framework crosswalk | v4 | first public V4+ capability release |
| GOV-HEALTH-1 clinical-use prohibition | v3 | maintained now (author is a clinician) |
| GOV-SEC-1 security & misuse gate | v6 | language/tool/social/public capability release |
| GOV-PROC-1 ethics-as-process | v3 | this Phase-0 step IS its first increment |

---

## 4. Phased plan

### Phase 0 — Consolidate (DONE, 2026-06-19)

- [x] `governance_rule` epistemic category added to `scripts/validate_claims.py`
      (`VALID_EPISTEMIC_CATEGORIES`) and
      `evidence/experiments/scripts/build_experiment_indexes.py`
      (`EPISTEMIC_CATEGORIES` + resolver/gating docstrings).
- [x] `REE_assembly/CLAUDE.md` epistemic-category table row added.
- [x] 20 SENT-*/GOV-* claims registered in `claims.yaml` (844 entries total;
      validator strict exit 0, no SENT/GOV warnings).
- [x] This plan-of-record created.

### Phase 1 — V3 boundary (DEFERRED; lightweight, non-blocking; before 2026-07-19 if cheap)

- [ ] SENT-0 boundary statement into `ree-v3/README.md` and a new
      `docs/governance/sentience_welfare_risk_register.md`.
- [ ] Tag V3's welfare-relevant primitives (harm streams, residue,
      suffering-like accumulators, replay) as `welfare_relevant: true`
      (descriptive only, no gate).
- [ ] Add the ethics-preflight as **documentation** to `/queue-experiment`
      (most V3 fields are `false`/`n/a` — establishes the habit, does not enforce).
- [ ] GOV-HEALTH-1 bright-line note into `ree-v3/README.md` (no clinical use;
      no patient data in public repos).

### Phase 2 — V4 gates (DEFERRED; draft now, bind at V4 boundary)

- [ ] `docs/governance/sentience_welfare_risk_register.md` (SENT-0…12 full).
- [ ] `docs/governance/ethical_assembly_routing_map.md` (Class 0–5 +
      prohibited combinations; SENT-13).
- [ ] `docs/governance/ai_welfare_consciousness_indicator_matrix.md` (SENT-1/15).
- [ ] Draft `docs/governance/continuity_identity_reset_and_deletion_ethics.md`
      and `docs/governance/consent_assent_refusal_ladder.md` (SENT-9/12).

### Phase 3 — V5/V6 perimeter (DEFERRED; structural)

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
