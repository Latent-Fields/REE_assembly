# "Matched capacity" in comparator falsifiers -- scoping and recommendation

- **Date:** 2026-09-22T19:08:01Z
- **Session:** `friendly-kalam-14981a` (chip `chip-20260922-matched-capacity-definition`)
- **Triggering finding:** `/thought-digestion` wave 2026-09-22 over ARC-149 / MECH-575 / MECH-576 /
  MECH-577 (session `compassionate-pike-fe9174-digest`), cross-cutting finding **A1**, archived at
  `evidence/planning/thought_digestion_staged_2026-09-22_affordance_consensus.md`.
- **Scope of this document:** SCOPES AND RECOMMENDS ONLY. No claim was amended; no status,
  confidence or `epistemic_category` was changed; no experiment was queued.

---

## Recommendation

**Option (c): no change. An existing convention already covers it, and it is already the
better-specified of the two candidate designs.**

Two things already exist, and the finding A1 missed both:

1. **ARC-149's `what_would_answer` precondition (d) already IS the rule A1 proposes to write**,
   in the per-claim pre-registration form -- option (b) -- and is already the shared gate for the
   whole affordance-bridge group, inherited by explicit forward reference.
2. **Registry-wide, the operative convention is "state the matching dimension by name, in the
   claim's own non-degeneracy precondition."** 43 of 48 in-scope claims already do this. The
   metric that is correct differs per claim, which is why a single global definition would be
   *worse* than what most of these claims already carry.

The recommended disposition is therefore to record the convention as already-held, and to close
the two genuine residue items (below) as ordinary documentation-currency work -- not to register a
new methodology invariant and not to amend INV-105.

---

## Step 1 -- the actual inventory (A1's list was not exhaustive, and contained one false positive)

Method: parsed `docs/claims/claims.yaml` (1180 claims) structurally, flattened every scalar field,
and matched capacity/resource-matching phrasings (`matched capacity`, `capacity-matched`,
`matched compute`, `matched parameter*`, `matched budget`, `equal/same/comparable capacity`, and
the hyphen/space variants in both orders). Bare `grep` counts were not used as the inventory --
they over-count (`at matched` alone returns 260 line hits, nearly all of them `matched seeds` /
`matched budget` and unrelated phrasings).

**50 claims carry a capacity/resource-matching phrase.** Two are false positives on inspection:

| Claim | Why it is not in scope |
|---|---|
| **INV-090** | `same-capacity decode` is used as a *degeneracy hazard* -- the evaluator being a same-capacity decode of its own target **entails** the PASS -- not as a comparator-matching requirement. Opposite polarity. |
| **MECH-323** | `capacity` means visuospatial working-memory capacity (Bo & Seidler 2009), a substantive construct from the literature pull, not comparator resourcing. |

**48 in-scope claims.** A1 named 5, of which one is wrong:

| A1's list | Verdict |
|---|---|
| ARC-149, MECH-575, MECH-576, MECH-577 | Correct -- and all four are already bound (see Step 2). |
| **ARC-145** | **False positive.** Its separability falsifier is a *timing/jurisdiction* test, not a capacity-matched-comparator test, and its matching conditions are already fully enumerated and are not capacity: "at matched message count, matched transmitted norm, matched receiver-local competence and matched episode phase". |

Breakdown of the 48:

| Bucket | N | Claims |
|---|---|---|
| **Hosts the definition** | 1 | ARC-149 (precondition (d)) |
| **Inherits ARC-149 by explicit forward reference** | 3 | MECH-575, MECH-576, MECH-577 |
| **Names >=1 concrete matching dimension inline** | 42 | ARC-017, ARC-018, ARC-025, ARC-113, ARC-135, GOV-DELETE-1, INV-023, INV-044, INV-049, INV-055, INV-088, INV-104, INV-105, INV-110, MECH-017, MECH-081, MECH-099, MECH-103, MECH-200, MECH-202, MECH-257, MECH-293, MECH-309, MECH-337, MECH-423, MECH-457, MECH-486, MECH-520, MECH-534, MECH-537, MECH-547, MECH-549, MECH-550, MECH-555, MECH-560, MECH-579, Q-103, Q-106, SD-010, SD-065, SD-082, SD-106 |
| **Residue -- under-specified** | 2 | MECH-430, MECH-548 |

A regex classifier put 13 claims in the residue bucket; **all 13 were hand-checked**, because a
"nothing found" bucket is a negative instrument (CLAUDE.md, *Negative instruments*) and the regex
had no way to recognise phrasings like "same capacity, seeds and harm exposure" or a named built
artifact. 11 of the 13 were false residue. The two survivors are given below.

---

## Step 2 -- the existing precedent (extraction beat invention on every one)

### 2a. ARC-149 precondition (d) -- verbatim

> **(d) MATCHED CAPACITY must be DEFINED AND PRE-REGISTERED before the run, not argued after it:
> parameter count, latent dimensionality and optimiser budget each separately matched, or the
> mismatch stated. The entire content of this commitment is a matched-capacity contrast, so an
> unpinned capacity definition makes the result unfalsifiable in exactly the direction that
> matters -- the losing side can always claim the comparator was under-resourced.**

Finding A1's statement of the problem reproduces this paragraph's reasoning almost word for word
and reports it as a gap. It is not a gap: it is the registered rule, and it is already in the
*pre-registration* form A1 offers as option (b).

ARC-149's preamble makes the inheritance explicit -- "this is the SHARED gate for the whole
2026-09-18 affordance-bridge group -- MECH-575 / MECH-576 / MECH-577 reference this paragraph and
deliberately do not re-derive it" -- and each of the three carries the reciprocal pointer
("inherits ARC-149's phenotype-battery and matched-capacity gate in full -- see ARC-149's own
what_would_answer, do not re-derive it"). MECH-577 names the precondition by letter: "Both inherit
ARC-149's matched-capacity definition requirement (its precondition (d))".

### 2b. INV-105 has ALREADY declined to host a matched-capacity binding -- this is the governing precedent

INV-105's own notes, on MECH-547's third binding consequence:

> "Same disposition for MECH-547's third binding consequence (a receiver-conditioned bridge result
> is admissible only with a receiver-state permutation control AND a **sender-only matched-capacity
> baseline**): **it stays on MECH-547.** Revisit when MECH-548 matures."

So the exact move option (a) proposes -- hoisting a matched-capacity requirement onto INV-105 --
has already been considered for a matched-capacity binding and decided the other way, on INV-105
itself. This is the same forward-reference-over-amendment disposition as GFLAG-0235 (2026-09-10),
which chose forward reference rather than amending INV-105 for MECH-548's proposed rung.

INV-105's own bindings are also instructive as a *template*: they are never generic. They are
"correct-vs-mismatched-vs-zero-vs-**moment**-matched-random controls" and a
"**dimensionality**-matched RANDOM-PROJECTION floor" -- each names the precise quantity held
constant. INV-105's notes state the design philosophy directly: "REE already applies pieces of this
ad hoc ... The novelty is making the ladder explicit and naming the two controls as REQUIREMENTS,
so that the missing rung is visible when an experiment reports one." Naming the specific control,
per claim, is the practice; a generic definition is not.

### 2c. Harness-side precedent points the same way

`experiments/_lib/consolidation_lesion_harness.py`'s `rms_ref` is a per-call parameter that
documents exactly what the scale is referenced to ("`diffuse_perturb` references its scale to the
UNSCALED content (`rms_ref`)") -- matching against a named quantity, passed per assay. There is no
global capacity-matching or parameter-counting helper anywhere in `ree-v3` (searched for
`capacity_match` / `match_capacity` / `param_match` / `matched_capacity` / `count_param*`
definitions: none exist). The codebase has not converged on a global constant either.

### 2d. The registry's de facto convention, with examples

The dominant form is **"matched <NAMED DIMENSION>"**, stated in the claim's own non-degeneracy
precondition or control clause. Representative spread, from loosest to tightest:

- **MECH-103**: "at matched budget"
- **MECH-081**: "at matched compute and matched seeds"
- **ARC-025**: "holding parameters and training budget matched to the full system"
- **INV-049**: "matched waking exposure and matched total gradient budget ... a budget-matched
  online-only arm (same number of gradient steps, no replay)" -- operationalised to a countable
- **ARC-113** (2): "equal parameter count and equal information capacity across the manipulated
  boundary. Without this the comparison measures capacity, not boundary, and reproduces the
  ablation confound under a new name"
- **MECH-549**: "final capacity(B) = final capacity(D), architecture(B) ~= architecture(D),
  identical curriculum and seeds, matched compute" -- capacity as an equality relation at the
  trajectory endpoint
- **MECH-555**: "at frozen endpoints and matched capacity, data, optimisation and
  conditioning-channel width"
- **MECH-520**: "SD-070 IS THIS CLAIM'S MATCHED-CAPACITY CONTROL, already built, already
  contract-pinned (31 tests), already measured" -- the control is a named, built, tested artifact
- **INV-088 / MECH-457 / MECH-537 / INV-104 / SD-106**: "a capacity-matched supervised adapter
  (x734.PPOPolicyNet, **21381 action-path parameters**, identical to V3-EXQ-978's reader)" -- a
  named module at an exact parameter count, the tightest specification in the registry

MECH-486 additionally names the hazard by A1's own phrase and routes to its own text: "the
comparison is only meaningful at MATCHED capacity/compute, which a merged-vs-separated ablation
must control for explicitly. **See the matched-capacity trap in what_would_answer.**" The registry
is not unaware of this trap; it has a name for it.

---

## Step 3 -- why NOT option (a), on held-out evidence

The chip's guard requires that a proposed standing rule be checked against >=3 historical cases it
was not written from, counting only cases where the old and new wording give **different** answers.
ARC-149's (d) triple -- *parameter count, latent dimensionality, optimiser budget* -- is the only
concrete candidate for a registry-wide definition, so it is the one tested. The check is
non-degenerate and it **caught the over-broad rule**: in each case the global triple admits a run
the claim's own wording refuses.

| # | Claim (not among ARC-149/575/576/577) | Its own requirement | What the global triple would do |
|---|---|---|---|
| 1 | **ARC-113** (2) | "equal parameter count **and equal information capacity across the manipulated boundary**" | Cross-boundary information capacity is not latent dimensionality. A collapsed and a staged variant can match on parameter count and latent dim and still differ across the seam -- precisely the confound ARC-113 says "reproduces the ablation confound under a new name". **Global rule admits a refused run.** |
| 2 | **Q-106** | "at **matched output statistics**, matched parameters and matched compute" | Output-statistics matching is distributional, not a capacity metric, and is absent from the triple. Without it the closed-loop generator can win by emitting differently-distributed output. **Global rule drops a load-bearing control.** |
| 3 | **MECH-549** | "final capacity(B) = final capacity(D), **architecture(B) ~= architecture(D)**, identical curriculum and seeds, matched compute" | The triple is satisfied by two networks with equal parameter counts and different architectures -- which is arm D's confound exactly. The claim is about developmental ORDERING, so architecture must be held. **Global rule admits a refused run.** |
| 4 | **MECH-555** | "matched capacity, data, optimisation and **conditioning-channel width**" | Channel width is claim-specific and absent from the triple. |
| 5 | **MECH-547** | "matched capacity with **the conditioning channel's added capacity REPORTED**" | A reporting obligation on a specific quantity; the triple's "or the mismatch stated" is weaker and unaddressed to the channel. |

Five non-degenerate cases, three sufficient. All five fail in the same direction: **a registry-wide
definition would be looser than the per-claim ones and would license comparators those claims
explicitly refuse.** Option (a) is not merely unnecessary; it is a regression.

Option (b) -- a per-claim pre-registration requirement with no global default -- is the right
*shape*, and is exactly what ARC-149 (d) already states and what 43 of 48 claims already practise.
Registering it as a new standing rule would formalise an existing practice at the cost of a new
methodology invariant with no observed violation to justify it, against a registry whose own
precedent (2b) is to leave such bindings on the originating claim. Hence (c) rather than (b).

---

## The residue: two claims, documentation-currency only

Neither is a standing-rule problem. Both are single-claim wording items, and both are on
substrate-blocked claims that cannot run today, so neither is urgent.

1. **MECH-430** -- the genuine bare case. Its CONFIRMING line ends "...that the single bit cannot
   express, **at matched capacity**", and no field anywhere in the claim says matched on what.
   Status `candidate`, `substrate_conditional`, substrate-blocked as of 2026-09-15. **Suggested
   (governance's call):** name the dimension the comparison actually needs -- for a
   per-dimension-vs-single-bit provenance contrast the relevant quantity is source-vector width and
   the consumer's read capacity, not parameter count -- or forward-reference ARC-149 (d) as
   MECH-575/576/577 do.

2. **MECH-548** -- deliberately soft: "Assay (diagnostic, frozen endpoints, **matched capacity where
   possible** -- arms listed on the location doc)". This is a diagnostic assay, not a claim
   falsifier, and "where possible" may well be the honest wording for a cross-arm diagnostic whose
   arms differ structurally. **Suggested:** leave as is unless governance judges the assay is being
   read as adjudicating; flagged here only so the decision is recorded rather than defaulted.

---

## What was checked and what was not

- **Checked:** all 1180 claims in `claims.yaml` (structural parse, every scalar field); all 50
  phrase hits read in context; all 13 regex-residue candidates hand-verified; ARC-145 and ARC-149
  read in full; INV-105, MECH-558, and `consolidation_lesion_harness.py` checked as Step-2
  precedents; `ree-v3` searched for a global capacity-matching helper.
- **Not checked:** whether any *past experiment verdict* was in fact contested on
  comparator-resourcing grounds. The held-out check above is against registry wording, which is
  what a wording change would alter; a verdict-level audit would be a separate and larger piece of
  work, and nothing in the inventory suggested it is owed.
- **Not done, deliberately:** no claim amended, no `claims.yaml` write (this session held no claim
  on it and did not need one), no experiment queued, no status/confidence/category change.

---

## GOV-HELDOUT-1 record

**Outcome: CAUGHT AN OVER-BROAD RULE.** The proposed registry-wide definition (option (a), using
ARC-149 (d)'s triple as the global standard) was checked against 5 held-out claims it was not
written from -- ARC-113, Q-106, MECH-549, MECH-555, MECH-547 -- all non-degenerate (the global and
existing wordings give different answers on each). In every case the global rule was the weaker
one and would have admitted a comparator the claim's own precondition refuses. The rule was
therefore not shipped, and the recommendation moved from (a) to (c).
