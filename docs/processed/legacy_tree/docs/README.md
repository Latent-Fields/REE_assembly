# REE Typed-Claims Documentation System

This README is executable guidance for AI coding agents. When invoked, agents must follow the quoted prompts exactly.

## Operating Procedure

1. Preserve history. Do not delete or overwrite prior formulations; add new material alongside and reference preserved sources.
2. Classify every change as an invariant, architectural commitment, mechanism hypothesis, open question, or implementation note.
3. Update canonical docs under `docs/` by extracting text from `docs/processed/legacy_tree/` and adding minimal glue text.
4. Update `docs/claims/claims.yaml` and `docs/claims/claim_index.md` for every new or modified claim.
5. If a conflict is detected, create or update a file in `docs/conflicts/` and link conflicting claim IDs.
6. Append a dated entry to `docs/changelog.md` describing what changed and where preserved content lives.

## THOUGHT INTAKE PROMPT (verbatim)

```text
You are GitHub Copilot (agent mode). I am going to describe a thought, concern, or new understanding about REE in free text.

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
You are GitHub Copilot (agent mode). I am resolving an explicitly documented conflict or fork in the REE documentation.

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
