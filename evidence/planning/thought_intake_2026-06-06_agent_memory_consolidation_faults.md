# Thought Intake (Stage 2): Agent memory consolidation faults and raw episodes as first-class evidence

Raw thought file: [docs/thoughts/2026-06-06_agent_memory_consolidation_faults.md](../../docs/thoughts/2026-06-06_agent_memory_consolidation_faults.md)
Intake date: 2026-06-09
Source email date: 2026-05-17 (saved REE item, attribution Daniel Golden)
Primary source: VERIFIED (see Section 6)
Classification: memory-architecture thought; candidate-claim seed (NOT registered in claims.yaml by this intake)

---

## 0. One-line summary

An arXiv study finds that LLM agents which repeatedly rewrite their own memories into
polished "lessons" can get *less* reliable over time even when the source episodes were
useful; the durable REE extraction is that **raw episodes should remain first-class
evidence and consolidation should be gated, provenance-linked, auditable, and reversible
rather than automatic rewriting.**

---

## 1. Verbatim thought (as captured)

> A saved REE email pointed to a study on large language model (LLM) agent memory showing
> that agents can become less reliable when they repeatedly rewrite their own memories into
> polished lessons. The source was identified during intake as the arXiv paper: Dylan Zhang,
> Yanshan Lin, Zhengkun Wu, Yihang Sun, Bingxuan Li, Dianqi Li, Hao Peng. "Useful Memories
> Become Faulty When Continuously Updated by LLMs." arXiv:2605.12978.
>
> The paper reports that consolidated memories produced by current LLMs can be faulty even
> when derived from useful experience; memory utility may first rise and then degrade; and
> episodic-only controls retaining raw trajectories can remain competitive with or outperform
> repeated consolidation regimes.
>
> The useful REE idea is: raw episodes should remain first-class evidence, and consolidation
> should be gated, auditable, and reversible rather than automatic rewriting.
>
> This is directly relevant to REE because REE already distinguishes replay, residue, offline
> integration, and future action-landscape deformation. If consolidation overwrites or
> compresses the evidence too aggressively, the system may become less reliable while believing
> it has learned.
>
> [Proposed REE memory states: Episode retained -> indexed -> summarised -> Schema consolidated
> -> contested -> retired, with the key rule that `consolidation_output must not replace
> source_episode_evidence`. Proposed memory_record fields: raw_episode_pointer, source_provenance,
> transformation_history, consolidated_summary, confidence, contradiction_flags, retrieval_scope,
> action_authority.]
>
> Cautions: do not infer summarisation is always harmful; do not infer raw episodes alone are
> always sufficient; do not treat current LLM memory failures as proof consolidation is impossible;
> do not allow consolidated memory to become untraceable authority; do not let summaries overwrite
> raw experimental evidence.
>
> Guardrail for future agents: if a future agent tries to improve memory by repeatedly summarising
> and overwriting past traces, stop and reframe -- preserve raw episodes as first-class evidence
> and make consolidation gated, provenance-linked, and auditable.
>
> "Of course REE has multiple 'memory'-like parts which may make this entire point somewhat moot."

(Full original text in the raw thought file; this is the load-bearing extract.)

---

## 2. What's New vs Existing REE Docs

| Idea in this thought | Already in REE? | Where | Genuinely new? |
|---|---|---|---|
| Offline integration / consolidation exists and is required | YES | INV-039, INV-049, SD-017, MECH-017, MECH-121/122 | No |
| Consolidation is a fallible operator, not a clean compression | PARTIAL | MECH-068 (selectivity lives in the operator); MECH-124 (maladaptive consolidation / PTSD) | The *failure-by-iteration* framing (utility rises then degrades under repeated rewriting) is new emphasis |
| Raw episodes must be PRESERVED beneath abstraction (not overwritten) | IMPLICIT only | MECH-094 (sim-vs-real write profile), MECH-100/ARC-007 (residue/path store), ARC-020 (offline/commitment write-locus isolation) | **Yes** -- no claim states "consolidation_output must not replace source_episode_evidence" as a standing invariant |
| Consolidation must be GATED / write-authority-bounded | PARTIAL | SD-024 (offline consolidation protected by typed authority/write boundaries), MECH-261 (mode-conditioned write gating) | The *update-schedule sensitivity* and *anti-overwrite* angle is new |
| Consolidation must carry PROVENANCE + be auditable/reversible | PARTIAL | INV (provenance: Papez-like reality filtering), MECH-094 replay_origin audit flag, MECH-076 imagination tagging | **Yes** -- the explicit `transformation_history` + `contradiction_flags` + rollback ("Schema retired but source episodes remain") layer is not a current claim |
| Layered memory: episodic evidence vs consolidated abstraction | PARTIAL | MECH-273 (waking single-episode vs sleep Bayesian aggregate self-model), MECH-272 (state-gated routing) | The explicit 6-state lifecycle (retained/indexed/summarised/consolidated/contested/retired) is a new formulation |
| Separate retrieval-for-reflection from retrieval-for-action-authority | NO | -- | **Yes** -- `retrieval_scope` vs `action_authority` as distinct fields on a memory record is novel for REE |
| This is relevant NOW for REE-v3 (experiment history / traces), not just V4/V5 | n/a | -- | New framing: treat as a **memory-safety principle** governing REE_assembly's own evidence base, not a large new substrate feature |

**Net:** the thought is *mostly corroboration* of REE's existing offline/consolidation
commitments, with **four genuinely new threads**: (a) consolidation-as-fallible-iterative-operator
with overwrite risk; (b) an explicit raw-episode-preservation invariant; (c) a provenance +
contradiction + rollback layer on consolidated memory; (d) the retrieval-scope vs action-authority
split. The strongest single new candidate is the standing rule that abstraction must never delete
the evidence base.

---

## 3. Key formulations

- **Anti-overwrite invariant (candidate):** `consolidation_output MUST NOT replace source_episode_evidence`.
- **Memory lifecycle (6 states):** Episode *retained* -> *indexed* -> *summarised* -> Schema
  *consolidated* -> *contested* -> *retired* (abstraction de-authorised, source episodes remain).
- **memory_record fields:** `raw_episode_pointer, source_provenance, transformation_history,
  consolidated_summary, confidence, contradiction_flags, retrieval_scope, action_authority`.
- **Failure signature from the source:** memory utility first rises, then degrades below the
  no-memory baseline; the regression traces to the *consolidation step*, not the experience --
  the same trajectories yield qualitatively different memories under different update schedules,
  and small abstraction errors compound because each update rewrites the products of earlier updates.

---

## 4. Affected existing claims (REAL ids -- verified present in claims.yaml)

No claim is contradicted; several are *corroborated* or have a *latent gap surfaced*:

| Claim | Status | Relationship to this thought |
|---|---|---|
| **INV-049** | invariant | Offline-update necessity (general principle). This thought is the *complementary caution*: offline update is necessary BUT the update operator itself can corrupt. INV-049 says "you must reorganise offline"; this says "reorganisation can be the fault." |
| **INV-039** | invariant | Schema-primed assimilation rate gated by map stability. Source corroborates: update schedule / state-gating matters; aggressive consolidation onto an unstable map is exactly the degradation regime. |
| **SD-017** | design_decision | Minimal sleep-phase infra (SWS/REM analogs). The anti-overwrite rule is a constraint ON these replay phases (replay should not destroy the residue it replays). |
| **MECH-068** | candidate | "Consolidation selectivity lives in the consolidation operator." Directly on point -- the source is empirical evidence that a *bad* operator degrades utility; strengthens the case that the operator is the critical locus. |
| **MECH-094** | (write-profile / sim-vs-real) | Already carries a `replay_origin=True` audit flag with accelerated dissolution. This thought generalises the audit/provenance idea from sim-vs-real to *all* consolidation transformations. |
| **MECH-124** | (maladaptive consolidation / PTSD) | Existing precedent that consolidation can be pathological. The source is the LLM-agent analogue of the same failure mode. |
| **MECH-261** | mechanism_hypothesis | Mode-conditioned write gating (incl. `offline_consolidation` mode). The candidate "gated consolidation write-authority" likely amends MECH-261 rather than spawning a new gate. |
| **MECH-272 / MECH-273** | mechanism_hypothesis | State-gated routing + sleep-half Bayesian self-model aggregation. The 6-state lifecycle and contradiction-flag layer would refine these, not replace them. |
| **SD-024** (sleep.protected_offline_consolidation_boundary) | candidate | "Offline consolidation protected by typed authority/write boundaries." The nearest existing home for the gating half of this thought. |
| **ARC-007** | architectural_commitment | Hippocampal path store/replay -- the residue field IS the raw-episode-ish substrate that must not be overwritten by abstraction. |
| **ARC-020** (offline/commitment write-locus isolation) | invariant | Already isolates offline-consolidation writes from commitment writes; the anti-overwrite rule is an adjacent constraint within the offline locus. |

**Meta-point (the author's own caveat):** REE already has *multiple* memory-like parts
(residue field, hippocampal store, viability map, schema buckets, incentive/ghost-goal banks).
The novelty here is not "add a memory store" but "add a **provenance + anti-overwrite + rollback
discipline** across the ones that already exist," plus a possible audit of REE_assembly's own
evidence base.

---

## 5. Candidate claims FOR FUTURE REGISTRATION (NOT registered here)

Register only if a later session + the user judge them warranted. Likely amendments to
existing claims rather than new INV/MECH:

1. **`memory.consolidation.raw_episode_preservation`** (candidate invariant or amend ARC-020/MECH-094):
   a consolidated abstraction must retain a pointer to, and must not delete, its source episodes.
2. **`memory.consolidation.gated_write_authority`** (likely amend **MECH-261** / **SD-024**):
   consolidation is not automatic-after-every-interaction; it fires under explicit gating
   (state, map-stability per INV-039, schedule), and over-frequent rewriting is a failure mode.
3. **`memory.consolidation.provenance_required`** (likely amend **MECH-094** audit-flag family):
   every consolidated summary carries `transformation_history` + `contradiction_flags`; a
   summary that conflicts with its source episode is flagged, not silently authoritative.
4. **`memory.retrieval_scope_vs_action_authority`** (NEW -- no current home): retrieval for
   reflection is distinct from retrieval that confers action authority; a consolidated
   abstraction lacking source-episode grounding may inform reflection but not unilaterally
   drive committed action.

**Gating note for governance:** all four are `substrate_conditional` / V3-leaning *principles*,
not testable-today on the current V3 substrate without a memory-lifecycle store. Do NOT queue
discriminative experiments before the substrate exists (known vacuous-probe risk). The
near-term value is as a **memory-safety design principle**.

---

## 6. External anchors (source-check status)

**Primary source -- VERIFIED 2026-06-09 (web search):**
- Dylan Zhang, Yanshan Lin, Zhengkun Wu, Yihang Sun, Bingxuan Li, Dianqi Li, Hao Peng.
  "Useful Memories Become Faulty When Continuously Updated by LLMs." arXiv:2605.12978
  (Univ. Illinois Urbana-Champaign + Tsinghua, 2026.05).
  https://arxiv.org/abs/2605.12978 · project page https://dylanzsz.github.io/faulty-memory/
- **Confirmed claims:** memory utility first rises then degrades, can fall below the no-memory
  baseline; even consolidating from ground-truth solutions, GPT-5.4 fails 54% of ARC-AGI problems
  it had previously solved without memory; the regression traces to the *consolidation step*
  (same trajectories -> qualitatively different memories under different update schedules; errors
  compound because each update rewrites prior updates); in a controlled ARC-AGI Stream environment,
  agents that **preserve raw episodes by default double the accuracy** of forced-consolidation
  counterparts, and disabling consolidation entirely matches the raw-episode regime.
- These independently corroborate the note's summary -- the note did not overstate the paper.

**Secondary source cited in the note -- NOT independently re-verified this session (low priority):**
- "How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior."
  arXiv:2505.16067 (cited in the raw note for experience-following / error-propagation / misaligned
  replay). Title plausible; not fetched. Verify if it becomes load-bearing for a registered claim.

**Adjacent corroborating literature surfaced during verification (not in the note, FYI for any future lit-pull):**
- "Governing Evolving Memory in LLM Agents ... SSGM Framework" (arXiv:2603.11768) -- semantic drift /
  procedural drift / consolidation-update risk taxonomy.
- "Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers" (arXiv:2603.07670).
- "From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms" (arXiv:2605.06716).

---

## 7. Relation to sibling thought intakes (all present in docs/thoughts/)

- `2026-06-06_sleep_timing_multiday_memory_eligibility_window.md` -- replay/consolidation should be timing/state gated.
- `2026-06-06_learning_onset_single_connection_gate.md` -- not all exposure should become write-eligible learning.
- `2026-06-06_ca3_development_sparse_structured_connectivity.md` -- mature memory needs structured sparse retrieval, not one over-powerful abstraction.
- `2026-06-06_hyperthymesia_autobiographical_temporality.md` -- autobiographical/future memory needs provenance + committed-vs-imagined tags.

Common thread across all five: **memory architecture should separate evidence, indexing,
abstraction, replay, consolidation, and action-authority.**

---

## 8. Next steps (proposed -- none executed by this intake)

1. **(optional, low priority)** Lit-pull confirming arXiv:2505.16067 and folding the SSGM /
   survey papers above if/when a memory-consolidation claim is registered. Do via `/lit-pull`.
2. **(optional, design)** Architecture note `docs/architecture/memory_evidence_and_consolidation_authority.md`
   answering: what counts as raw-episode evidence in REE; when consolidation is allowed; what
   provenance every summary must retain; whether a consolidated abstraction can drive action
   authority without source evidence; how summary-vs-source contradiction is handled.
3. **(deferred)** Register candidate claims (Section 5) only on explicit user decision -- they are
   amendments to MECH-094/MECH-261/SD-024/ARC-020, not new substrate; do NOT register from this intake.
4. **(no experiments)** Substrate-conditional; a discriminative probe before a memory-lifecycle
   store exists would be vacuous.

---

## 9. Guardrail (carried from the raw note)

If a future agent tries to "improve memory" by repeatedly summarising and overwriting past
traces, STOP and reframe. Correct extraction: **preserve raw episodes as first-class evidence
and make consolidation gated, provenance-linked, and auditable.** Incorrect: compress all past
experience into polished lessons and discard the originals. This applies as much to REE_assembly's
own evidence base (raw experiment manifests, thought files) as to any future REE-agent memory store.
