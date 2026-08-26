# Wave-of-groups for `/thought-digestion` -- design investigation

**Date:** 2026-08-26 · **Session:** `thoughtdig-grouping-7fd98a` (design only)
**Status:** DESIGN / RESEARCH. No `SKILL.md` edited, no digestion wave run.
**Motivating observation (user, 2026-08-26):** running the live backlog through
`/thought-digestion`, claims analysed *together as a group* produced results that were
richer and better able to self-correct and disambiguate than the same claims analysed
one-at-a-time. Claims that looked similar or overlapping got clarified against each
other in a way isolated per-claim analysis did not achieve.

**What the current skill actually does (confirmed by reading Step 4):** a wave is
*N isolated agents*, default 5, dispatched in parallel, each holding exactly ONE claim.
An agent sees a sibling claim only if the orchestrator happened to paste it into the
prompt by hand. Agents never see each other's claims or drafts. All cross-claim
reconciliation happens either (i) in the orchestrator's manual pre-supply of context, or
(ii) post-hoc in the human's Step 5 review. So the property the user observed is real
but is currently produced *outside* the drafting stage, where it cannot change a draft.

---

## 1. The population this must work on

Measured from `docs/assets/data/claims.json` + `docs/claims/claims.yaml`, 2026-08-26:

| quantity | value |
|---|---|
| claims in registry | 1061 |
| stance split | `believed` 857 · `asked` 119 · `shown` 85 |
| **undigested backlog** (`asked`/`believed` with empty `what_would_answer`) | **553** |
| of which `believed` / `asked` | 552 / 1 |
| carrying a `digestion_note` (Step-3 exclusion) | 8 -> working set **545** |
| by id prefix | MECH 324 · ARC 60 · SD 55 · INV 31 · IMPL 27 · GOV 20 · SENT 15 · Q 12 · EXT 9 |

**At the current 5-isolated-claims-per-wave rate the backlog is ~111 waves.** That is the
throughput case for grouping, independent of the quality case the user raised.

Note the backlog is essentially *all* `believed`, not `asked` -- 552 vs 1. The skill's
Step 3 diet describes (a) `asked` missing `what_would_answer` first; in practice that
bucket is empty and the real work is (b) `believed` assertions.

---

## 2. Grouping key evaluation -- every single existing field FAILS alone

This is the central negative result. There is no `cluster` field, and none of the
plausible substitutes works as a primary key.

### 2.1 `subject` -- degenerate (unique key, not a group key)
1051 **distinct** `subject` values across 1061 claims. Grouping on `subject` produces
groups of 1 almost everywhere. Unusable.

### 2.2 `subject` namespace (first dotted segment) -- bimodal, and unnormalised
198 namespaces. Size histogram is barbell-shaped: **95 namespaces contain exactly one
claim**, while the head is `governance` 55, `control_plane` 46, `policy` 38,
`hippocampus` 36. Within the backlog: 77/553 claims sit in a singleton namespace, while
the head is 36/24/24/22. Neither end is a usable group -- one degenerates, the other is
far too large for a single agent's context.

**Worse, the namespaces are not normalised:** `hippocampus` (36) and `hippocampal` (36)
are separate namespaces denoting the same subject -- 46 backlog claims split across a
spelling difference. Keying groups off raw namespace would silently sever a real family.
Any implementation must singular/stem-normalise, and even then this is a weak signal.

### 2.3 `source_thought` -- correct in principle, far too sparse
Only **32 of 553** backlog claims (5.8%) carry it, across 19 thoughts. This is the
*semantically ideal* key -- `/thought-ingestion` mints a wired-together set from one raw
thought (worked example: `ARC-128`, `MECH-497`, `MECH-498`), so a `source_thought` batch
is a genuine cohesive group by construction. But at 5.8% coverage it cannot be primary.
**It should be a strong booster, and `/thought-ingestion` should be made to populate it
consistently so this key improves over time** (see Open Question 4).

### 2.4 `registered_utc` (ingestion-date proxy) -- half-populated, bimodal
269/553 (49%) populated, 50 distinct dates. Again barbell: one bucket of **56**, then
22/19/18/15..., and 15 dates with a single claim. A 56-claim "group" is not a group.

### 2.5 `depends_on` connected components -- percolation collapse
`depends_on` is well-populated (1039/1061), so this looks like the principled choice.
Restricted to the backlog it yields 210 components -- but the size distribution is the
classic hairball-and-dust failure:

- **two giant components of 116 and 76 claims** (192 = 35% of the backlog), and
- **156 singletons** (28% of the backlog),
- with only ~55 components in the usable 2-13 range.

Raw connected components are therefore unusable. This is expected: on a dense semantic
dependency graph, transitive closure percolates.

### 2.6 Conclusion
**Grouping requires derived machinery -- a composite affinity plus a *bounded* clustering
rule -- not a `GROUP BY` on any existing field.** The percolation result in 2.5 is the
reason the bound is load-bearing rather than a convenience.

---

## 3. Proposed mechanism: composite affinity + bounded clustering

### 3.1 Affinity function
Pairwise score, deliberately dominated by *structural* signals with lexical similarity as
a tie-breaker only:

| signal | weight | rationale |
|---|---|---|
| explicit `depends_on` edge (either direction) | **3.0** | hard structural evidence |
| same `source_thought` | **3.0** | same raw thought = same source material |
| same 2-level `subject` path (`pfc.frontopolar*`) | 2.0 | the granularity that actually clusters |
| same normalised namespace (singular-stemmed) | 1.0 | weak; fixes `hippocampus`/`hippocampal` |
| same `registered_utc` date | 0.75 | ingestion-batch proxy where present |
| idf-weighted title+subject token overlap | 0..3.0 | catches unwired siblings; capped |
| same `claim_type` | 0.25 | mild |

### 3.2 The floor is the quality gate; the cap is only an upper bound
Measured sweep over the 545-claim working set (cap=5):

| floor | groups | mean size | solos | mean edge affinity |
|---|---|---|---|---|
| 1.0 | 117 | 4.66 | 8 | 4.62 |
| 2.0 | 138 | 3.95 | 29 | 4.82 |
| **3.0** | **189** | **2.88** | **78** | **5.29** |
| 4.0 | 270 | 2.02 | 158 | 6.09 |
| 5.0 | 329 | 1.66 | 228 | 6.79 |

**Recommended default: `cap=5`, `floor=3.0`.** The knee is at 3.0, and 3.0 is chosen for a
*semantic* reason, not a curve-fitting one: **3.0 is exactly the weight of one structural
edge** (a `depends_on` link or a shared `source_thought`). So at floor=3.0 every member of
every group is joined by at least one nameable, structural reason -- never by lexical
resemblance alone. That property is what lets the dispatch prompt *state why each claim is
in the group*, which is what the agent needs in order to look for the relationship.

Below 3.0 the "fill-to-cap" failure appears: groups pad to size 5 with loosely-related
passengers, manufacturing false cohesion. A tight group of 3 is better than 5 with 2
passengers -- the cap must never be a target.

### 3.3 Clustering rule: edge-first agglomeration, NOT greedy seed-and-grow
Two bounded algorithms were compared on the real backlog (cap=5):

| floor | greedy seed-and-grow | edge-first agglomerative |
|---|---|---|
| 2.0 | 144 groups, 33 solos | 142 groups, **22** solos |
| 3.0 | 193 groups, 84 solos | 187 groups, **69** solos |
| 4.0 | 269 groups, 158 solos | 262 groups, **146** solos |

Edge-first (take the globally strongest admissible edge, merge, repeat, refusing merges
that would exceed the cap) strands materially fewer claims. The mechanism of the
difference is visible in the today's-waves test in §4.3: under greedy, `MECH-464` came out
**solo despite a 5.23 affinity to MECH-516**, because an earlier seed consumed its partner
first. **Greedy is also order-dependent, and the skill's ordering input is *ripeness*** --
so greedy would let the ripeness ranking silently determine the grouping. Edge-first is
order-invariant, which decouples the two concerns properly.

### 3.4 Coverage
At the recommended setting, roughly **187 groups covering 545 claims, with ~69 (13%)
genuine solos** -- a ~2.9x reduction in review passes, with the solos explicitly
identified rather than silently processed (see §6).

---

## 4. Held-out check (GOV-HELDOUT-1)

Standing rule: check a proposed skill change against >=3 historical cases the rule was
NOT written from, counting only cases where old and new behaviour give **different**
answers. Three found, all non-degenerate, all with real claim ids.

### 4.1 Case (i) -- `chip-20260807-thoughtdigestion-trial-5`, 2026-08-07
Wave: `Q-090, Q-020, MECH-295, SD-087, SD-086`. Mean intra-wave affinity **1.13**.
Exactly one pair clears the floor: **`SD-087` <-> `SD-086` at 5.00, with an explicit
textual cross-reference between them** -- two constraints on the *same* `z_harm_a`
readout, dispatched to two isolated agents who each had to re-derive the harm-stream
readout context independently. Old behaviour: two isolated drafts. New: one group.
**Different answer -> non-degenerate.**

Additionally `Q-020` ("Does ARC-007's no-value-computation constraint survive MECH-073?")
was digested **with none of its actual clarifying context present**: its top affinities in
the backlog are `MECH-144` (6.00, ventral CA1 *valence* encoding) and `MECH-143` (5.53,
dorsal CA1 *value-free* map). Q-020 is literally a question about whether those two
claims are mutually consistent. Alone it is near-unanswerable; with the group in view it
is close to trivial. `Q-020` still has **no `what_would_answer` today**.

### 4.2 Case (ii) -- `chip-20260808-thoughtdigestion-trial2-5`, 2026-08-08
Wave: `INV-004, SD-033e, MECH-264, INV-073, MECH-138`. Mean intra-wave affinity **1.04**.
One pair clears the floor and it is the strongest in either trial:
**`SD-033e` <-> `MECH-264` at 7.75** -- and `MECH-264`'s own *title* reads *"Frontopolar
counterfactual-value tracking: **SD-033e** maintains, in parallel..."*. A claim that names
another claim in its title was split across two isolated agents.

**The consequence is live in the registry right now:** `SD-033e` has a full, detailed
`what_would_answer`; `MECH-264` has **none**. The pair was half-digested, and MECH-264
could largely have inherited SD-033e's precondition text -- which is precisely the
"cross-reference sibling claims rather than re-deriving" the skill already asks for in
Step 5 but provides no mechanism to achieve at drafting time.
**Different answer -> non-degenerate.**

### 4.3 Case (iii) -- the user's own live session, 2026-08-26 (waves 1 and 2)
Wave 1: `ARC-133, MECH-516, MECH-517, MECH-518, MECH-521`.
Wave 2: `MECH-464, MECH-465, ARC-134, MECH-519, MECH-520`.

Scoring all 10 together: **8 of the 14 strongest pairs are SPLIT ACROSS THE TWO WAVES**,
including two with explicit textual cross-references --
`MECH-521` <-> `ARC-134` (6.18) and `MECH-516` <-> `MECH-464` (5.23). Wave 1's own draft
file records that MECH-516's notes dispute "the affect instance" of **MECH-464** -- a
claim sitting in wave 2, invisible to it.

Two independent confirmations from the session's own artifacts:
- `digestion_wave2_drafts_20260826.md` §0 opens: *"THE CROSS-CUTTING FINDING: REE's
  compression sites are systematically UNTRAINED. **Three independent agents, on three
  unrelated claims, each found the same shape.**"* -- 3x redundant discovery, the direct
  cost of isolation, and a generalisation the orchestrator had to assemble post-hoc.
- `digestion_wave1_drafts_20260826.md` §0.1-0.2 is a **self-correction** ("That mechanism
  is wrong... but MECH-518's core assertion SURVIVES, via a different and better site")
  performed by the *orchestrator*, not by any agent -- exactly the property the user
  observed, arising only after drafting, where it cannot improve the drafts.
**Different answer -> non-degenerate.**

### 4.4 Negative control
Grouping must NOT be read as "always group". At the recommended setting (cap=5,
floor=3.0, edge-first) **69 of 545 claims come back solo**, and they are genuinely
isolated -- correctly staying solo is the right call, not a failure of the grouper.
Inspecting that set is informative: **9 of the 69 solos are `IMPL-*`
registry-infrastructure entries** -- `IMPL-002` "Repository metadata and contribution
process", `IMPL-018` "Claim index and navigation", `IMPL-006` "Legacy migration mapping"
-- which arguably should not be in a *scientific* digestion backlog at all. That is a
separate finding worth surfacing (Open Question 5).

(Exact solo counts by configuration, for reference: floor=2.0 greedy 28 / agglom 22;
floor=3.0 greedy 87 / agglom 69. The 69 figure is the recommended one; earlier drafts of
this note quoted the floor=2.0 set by mistake.)

---

## 5. Group dispatch mechanics

### 5.1 One agent per group (default), not N agents per group
The whole point is shared visibility, and shared visibility inside one context is what
produces the disambiguation. Fanning 2-3 agents onto the same group re-creates the
isolation problem one level up unless they can see each other, which they cannot.
**Default: one agent per group.** Multi-angle review of a single group is reserved for a
group flagged as high-stakes/contested by the user, and is an explicit opt-in, not a
default -- the cost is real and the benefit is unmeasured.

### 5.2 A wave is now N groups in parallel
Wave size should be governed by **claims under review**, not groups: the Step 5 review
pass is the human bottleneck and it scales with claims, not with agents. Current guidance
is ~5-8 claims per review pass. So a wave of **3 groups averaging ~3 claims (~9 claims)**
is the sensible starting point, adjustable down. This preserves the existing
"more than ~5-8 tends to overwhelm a single review pass" constraint while cutting the
number of *agent dispatches* roughly threefold.

### 5.3 Prompt shape
Same contract as today (read-only; extract before inventing; verify don't assume
currency; taxonomy up front) plus, and these are the load-bearing additions:

1. **All group members' full YAML blocks verbatim**, fetched by the orchestrator, as today
   but N of them.
2. **The reason each claim is in the group, stated explicitly** -- "MECH-264 is here
   because its title names SD-033e"; "SD-086/SD-087 share `subject: harm_stream.*` and
   both constrain the z_harm_a readout". This is what floor=3.0 buys: every membership has
   a nameable structural cause, so the agent is told what relationship to look for rather
   than being left to notice it.
3. **An explicit cross-claim mandate** -- four questions the per-claim prompt cannot ask:
   - Are any of these the **same claim** at different granularity (merge candidates)?
   - Do any two **contradict** each other, or does one's premise undercut another's?
   - Is there **one shared falsification condition** that covers several, so the others
     cross-reference it rather than re-deriving it?
   - Is there a **cross-cutting finding** true of the group as a whole? (The 2026-08-26
     "compression sites are untrained" finding is the worked example.)
4. **One shared falsifier where the group licenses it**, with the others pointing at it --
   directly implementing Step 5's existing "cross-reference sibling claims rather than
   re-deriving" instruction at drafting time.

---

## 6. Disposition and presentation

Step 5's per-claim taxonomy (a)-(f) survives unchanged and still applies **per claim** --
grouping changes what the agent can see, never who decides. Two additions:

**A group-level preamble before the per-claim dispositions**, stating: the relationships
found, any merge/duplicate proposals, any contradictions surfaced, and any shared
falsifier that several claims now point at. Without this the group's whole value is
invisible at review time.

**The taxonomy needs a genuine new option.** Today (e) *excrete (retire/merge)* exists but
is framed around retiring a pun or duplicate with `status: superseded`. It does not
cleanly express **"MECH-516 and MECH-464 are two readings of one claim; keep A, fold B's
content into it, repoint B's reverse-deps"** -- a *symmetric* merge proposal that only
becomes visible when both are read together, and which is therefore near-unreachable under
per-claim dispatch. Proposed **(g) merge with sibling**: names the surviving id, the
absorbed id, what text moves, and the reverse-deps needing repointing -- with (e)'s
existing guards (never delete, never orphan a dependent, surface any experimental
evidence) carried over intact.

---

## 7. Replace or augment?

**Augment -- a third course, not a replacement.** Reasons:

1. ~13% of the backlog is genuinely ungroupable at the recommended floor. Those claims
   need the existing per-claim path.
2. A group of 1 degenerates exactly to current behaviour, so the fallback is safe by
   construction -- but it should **not be silent**. A claim that reaches solo status
   should be *reported as ungroupable* at wave build time, because that fact is
   informative: it means either genuinely novel ground, or (as §4.4 shows) a claim that
   does not belong in the backlog at all.
3. Both existing operating modes compose with grouping unchanged: the interactive mode
   gains a group preamble in its Step 5 presentation; the unattended mode stages a group
   per section instead of a claim per section. The wave-plus-context-floor stopping rule
   is untouched -- **it must stay expressed in WAVES, not groups or claims**, or the
   floor's whole purpose (budgeting the close-out) is lost.

Selection logic: **grouped is the default when the worklist is a backlog sweep**
(the 553-claim case). Per-claim stays the default when `args` names a single claim or a
tiny user-specified set, and for any claim that comes back solo.

---

## 8. Open questions for the user

1. **Wave sizing.** Is ~9 claims across 3 groups the right review-pass load, or does a
   group-of-5 review cost more attention per claim than 5 isolated claims did (in which
   case waves should shrink)?
2. **Floor 3.0 vs 2.0.** 3.0 = every membership structurally justified, 189 groups, 78
   solos. 2.0 = 138 groups, only 29 solos, but admits lexical-only members. Which failure
   is worse for you: a passenger in the group, or a claim stranded solo?
3. **Is `(g) merge with sibling` wanted as a real disposition**, or should merges stay
   proposals routed to `/governance` rather than applied by digestion?
4. **Should `/thought-ingestion` be changed to always populate `source_thought`?** At 5.8%
   today it is the best key and nearly unused. This is a small upstream change with
   compounding downstream benefit -- but it is an edit to a *different* skill.
5. **The `IMPL-*` finding.** 27 `IMPL-*` claims are in the digestion backlog and several
   are pure registry housekeeping ("Claim index and navigation"). Should they be excluded
   from the diet in Step 3 outright?
6. **Where does the grouping computation live?** A helper script under
   `REE_assembly/scripts/` (auditable, re-runnable, testable) versus the orchestrator
   doing it inline by judgement. The measurements here used a throwaway script; a real
   implementation probably wants the former, which is a bigger change than a SKILL.md edit.

---

## 9. Provenance

All figures computed 2026-08-26 against `docs/claims/claims.yaml` (1061 claims) and
`docs/assets/data/claims.json`. Historical wave membership taken from
`WORKSPACE_STATE.md` (2026-08-18T04:23Z entry) and the staged artifacts
`evidence/planning/thought_digestion_staged_2026-08-07_trial5_5claims.md`,
`..._2026-08-08_trial2_5claims.md`, `digestion_wave1_drafts_20260826.md`,
`digestion_wave2_drafts_20260826.md`. Nothing in `claims.yaml` was modified by this
session.
