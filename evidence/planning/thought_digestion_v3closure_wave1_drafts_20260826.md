# `/thought-digestion v3-closure` -- PILOT WAVE 1, drafts for review

**Date:** 2026-08-26 · **Session:** `thoughtdig-grouping-7fd98a-wave1`
**Status:** STAGED ONLY -- **no `claims.yaml` write has been made and none will be made by
this session.** `claims.yaml` is held by the concurrent live session
`insights-7fd98a-digestion`; this pilot is deliberately draft-only and read-only on the
registry. Dispositions are the user's call.

**Mode under test:** grouped (wave-of-groups), `cap=5 floor=3.0`, edge-first agglomerative,
scope = closure-core + 1 hop. One agent per GROUP, three groups in parallel.
**Design + measurements:** `thought_digestion_wave_grouping_design_20260826.md`.

**Wave 1 = 3 groups / 12 claims** (of the 31-claim scope; wave 2 = the remaining 19 in 9
groups, worklist already built). All 12 verified undigested (`what_would_answer` absent,
no `digestion_note`) and disjoint from the concurrent live session's own wave 1/2 claims.

| group | claims | closure-core | why grouped |
|---|---|---|---|
| G1 | MECH-312b, MECH-312c, MECH-316, MECH-317, MECH-318 | 5/5 | `subject: policy.arbitration*` + shared registration batch + `depends_on` |
| G2 | MECH-263, SD-033b, ARC-113, MECH-298 | 2/4 | MECH-263's title NAMES SD-033b; `pfc.*`; ARC-113/MECH-298 one `depends_on` hop |
| G3 | MECH-254, SD-027, SD-064 | 2/3 | SD-064 is the organising concept both instantiate; pulled in by the hop |

---

## PILOT FINDINGS -- mechanism defects found while ASSEMBLING the wave

These are findings about the grouped mode itself, independent of what the agents return.

### P1. `cap=5` splits lettered claim families -- CONFIRMED, and the fix is free
`MECH-312a` <-> `MECH-312b` = **6.00** and `MECH-312a` <-> `MECH-312c` = **6.00**, yet
312a was stranded as a **solo in a different wave**. Mechanism: edge-first agglomeration
consumes the strongest edges first (`316`<->`318` = 8.00, `317`<->`318` = 8.00,
`312b`<->`317` = 7.00), filling the group to cap=5 as {316,317,318,312b,312c}; 312a then
cannot join a full group.

Measured across the full backlog: **4 lettered families have >=2 undigested members, and 2
of the 4 (50%) are split** (`MECH-312a/b/c/d` across two groups; `SD-033b`/`SD-033c` across
two). **No family exceeds cap=5 on its own**, so the fix costs nothing:

> **Proposed refinement (not yet applied to SKILL.md):** pre-merge lettered families
> (same numeric stem, e.g. `MECH-312a..d`) into an ATOMIC unit before clustering, and let
> the cap flex to accommodate a family. Never split a family across groups or waves.

Confidence: the fix is free and clearly right in direction, but n=4 families is a small
base. Flagged rather than shipped.

### P2. The scope filter itself splits a family
`MECH-312d` is `MECH-312a`'s joint-top partner (**6.00**) and is **outside** the
closure-core+1hop scope, so the scoped run sees only 312a/b/c of a 4-member family. The
`depends_on` hop does not close over lettered families.

> **Proposed refinement:** when any member of a lettered family is in scope, pull the whole
> family into scope (a "family closure" rule alongside the `depends_on` hop), OR admit the
> absent members as read-only CONTEXT MEMBERS (design doc 7b.4) so the agent at least sees
> them.

### P3. Deviation from the skill text, deliberate, for evaluation
Step 4/G3 says embed each claim's full YAML block **verbatim in the agent prompt**. Here
the blocks were pre-extracted to a file the agent reads instead (G1 425 lines, G2 547, G3
239 -- 1211 lines total). Rationale: identical information, no 86,000-line registry search,
and prompts stay readable. **Whether this weakens the "extract before inventing"
instruction is an open question this pilot should answer** -- if agents drift toward
inventing, embed verbatim next time.

---

## Wave timing

- dispatched 2026-08-26T20:14:45Z

---

## GROUP RESULTS

*(agents in flight -- results appended on completion)*
