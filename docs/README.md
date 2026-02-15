# REE Typed-Claims Documentation System

**Claim Type:** implementation_note  
**Scope:** Documentation operating procedure and prompts  
**Depends On:** None  
**Status:** stable  
**Claim ID:** IMPL-013
<a id="impl-013"></a>

This README is executable guidance for AI coding agents. When invoked, agents must follow the quoted prompts exactly.

## Operating Procedure

1. Preserve history. Do not delete or overwrite prior formulations; add new material alongside and reference preserved sources.
2. Classify every change as an invariant, architectural commitment, mechanism hypothesis, open question, or implementation note.
3. Update canonical docs under `docs/` by extracting text from `docs/processed/legacy_tree/` and adding minimal glue text.
4. Update `docs/claims/claims.yaml` and `docs/claims/claim_index.md` for every new or modified claim.
5. If a conflict is detected, create or update a file in `docs/conflicts/` and link conflicting claim IDs.
6. Append a dated entry to `docs/changelog.md` describing what changed and where preserved content lives.
7. Place unprocessed thoughts in `docs/thoughts/` and record resolutions in `docs/conflicts/resolutions/`.
8. For REE-v2 docs and user-facing text, use JEPA-first wording with inline REE translation (`JEPA term (REE term)`) per `docs/notes/jepa_language_policy.md`.

## Dependency Semantics

`depends_on` edges in `docs/claims/claims.yaml` represent conceptual prerequisites only and must remain acyclic.
Runtime information flow may be cyclic (feedback, replay, recurrent loops), but those loops belong in architecture/interface/flow docs, not as cyclic claim dependencies.

## Synthesis Pass (Lightweight)

Use this when a subsystem feels fragmented or the claims list is growing without convergence. This is not a refactor.

1. Pick one subsystem document (e.g., control plane, residue, hippocampal systems).
2. Identify 3–6 **core claims** that define the subsystem’s identity.
3. Mark remaining claims as **supporting** in prose (do not delete or rewrite them).
4. Update the subsystem doc’s opening summary to reflect the core set.
5. If necessary, adjust claim statuses:
   - Promote candidates that have solidified (→ provisional).
   - Reframe shaky mechanisms as open questions.
6. Record a short synthesis note in `docs/notes/synthesis_passes.md`.

## Conflict Compression (Lightweight)

Use this to keep conflict files readable without resolving them.

1. Ensure each conflict file has a short “canonical summary” paragraph at the top.
2. Name the core axis of tension (what two formulations cannot both hold).
3. Link the key claim IDs involved.

## Promote/Demote Rhythm (Lightweight)

Use this periodically to prevent candidate claims from accumulating forever.

1. Review candidate mechanism hypotheses (MECH-*) for maturity.
2. Promote to provisional if the mechanism now has stable dependencies and clear role.
3. Demote or reframe as open questions if it remains speculative or under-specified.
4. Update `docs/claims/claims.yaml`, `docs/claims/claim_index.md`, and `docs/claims/subsystem_map.yaml` as needed.
5. Note the review in `docs/notes/synthesis_passes.md` or `docs/changelog.md`.

## Subsystem Abstract (Per Doc)

Each subsystem doc should open with a short paragraph summarising its essence and the 3–6 core claims that define it.
This keeps the subsystem coherent without removing detail or history.

## Consistency Checklist (Lightweight)

Run this check implicitly after any change:

1. Every new or modified claim has a matching entry in `docs/claims/claims.yaml` with correct `location`, `depends_on`, and `status`.
2. The claim appears in `docs/claims/claim_index.md` with the correct anchor link.
3. Claim status in the document header matches the registry (or the mismatch is explicitly noted).
4. No invariant depends on a mechanism hypothesis; no circular dependencies introduced.
5. Any contradiction triggers or updates a file in `docs/conflicts/` with linked claim IDs.
6. Preserved sources are cited; no prior wording is deleted or overwritten.
7. Subsystem map coverage is updated in `docs/claims/subsystem_map.yaml` for new or moved claim locations.

## THOUGHT INTAKE PROMPT (verbatim)

```text
You are the AI agent maintaining the REE repository (Codex in this session). I am going to describe a thought, concern, or new understanding about REE in free text.

Your job is to:
1) Infer the scope and affected components.
2) Determine whether this introduces or modifies:
   - an invariant,
   - an architectural commitment,
   - a mechanism hypothesis,
   - or an open question.
3) Update the canonical REE docs incrementally (do NOT refactor the whole repo).
4) Preserve all prior formulations; do not delete or overwrite history.
5) If this thought conflicts with existing claims:
   - represent the conflict explicitly in docs/conflicts/
   - do NOT resolve it.
6) Update the claim registry, glossary (if needed), and changelog.
7) Run an implicit consistency check and surface any new tensions created.

I will now write the thought in natural language.

BEGIN THOUGHT:
<PASTE YOUR THOUGHT HERE>
END THOUGHT
```

## CONFLICT RESOLUTION PROMPT (verbatim)

```text
You are the AI agent maintaining the REE repository (Codex in this session). I am resolving an explicitly documented conflict or fork in the REE documentation.

Your job is to:
1) Locate and read the referenced conflict file(s) in docs/conflicts/.
2) Identify the conflicting claim IDs, their types, scopes, and dependencies.
3) Apply my resolution decision carefully and minimally.
4) Update the canonical documentation, claim registry, and dependency graph to reflect the resolution.
5) Preserve historical record:
   - Do NOT delete superseded claims.
   - Mark them as legacy or deprecated with clear rationale.
6) Ensure the repo is internally consistent after resolution.
7) Surface any new tensions created by this change.
8) Update docs/changelog.md with a clear record of what was resolved and why.

BEGIN CONFLICT RESOLUTION:

Conflict reference(s):
- <PASTE docs/conflicts/*.md PATHS OR CLAIM IDs>

Resolution decision (free text):
<DESCRIBE THE RESOLUTION IN YOUR OWN WORDS>

END CONFLICT RESOLUTION
```

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- IMPL-013

## References / Source Fragments

- `docs/processed/legacy_tree/docs/README.md`
