# GFLAG-0091: the edge-first policy is measured against a broken instrument

**Date:** 2026-09-01
**Session:** `govapply-20260901-edge`
**Status:** finding recorded; no policy applied. GFLAG-0091 remains open.
**Trigger:** the user, on being shown that a first measurement refuted the edge-first premise,
asked for deeper investigation before any policy was adopted.

---

## The one-line finding

**The state this policy is about has been machine-readable in the registry the whole time, and
every figure in circulation was produced by a keyword scan instead.** The correct measurement is
**314 unrouted of 352**, computable today with no backfill. Every previously quoted figure --
the flag's 121, the triage's 155, the first measurement's 127 -- is wrong in *magnitude*, not
merely precision.

## What was actually wrong

### 1. The detector does not measure the state

The keyword detector (`unrunnable_falsifier_population_20260828.md` section 6) scans
`what_would_answer + notes` for `substrate_conditional`, `substrate_not_ready`, and variants.
Measured on a random sample of 30 of its 189 hits:

- **~20% claim-level false positives**; **~37% of matches are non-evidential** even when the
  claim happens to be blocked.
- **Recall against `epistemic_category: substrate_conditional` is 32%** -- it misses 241 of 352.
- Four of its ten keywords match **zero** claims.

The dominant failure mode is not typos. It is that `substrate_not_ready` is overwhelmingly used
as a **conditional self-route instruction to a future run** ("if this comes out flat, don't score
it"), not as an assertion that anything is unbuilt now. Worked examples, all verbatim:

- `ARC-044`: *"A run in which either running_variance or w_harm shows negligible variance ...
  must self-route substrate_not_ready / non_contributory"* -- in a field that opens
  *"CONFIRMED live -- V3-EXQ-194/194a C1 PASS 3/3"*.
- `MECH-436`: matches the word inside the sentence recording that the label was **removed**
  (*"FLIPPED from an initial substrate_conditional"*).
- `INV-025`: matches inside a disclaimer arguing the opposite -- *"Do not apply
  substrate_conditional mechanically to every axiom claim."*
- `MECH-071`: precondition **since satisfied** -- `CausalGridWorldV2` exists
  (`ree_core/environment/causal_grid_world.py:40,90,197`), `hazard_field_view` is in z_world
  (`ree_core/latent/stack.py:134`), SD-007 is `implemented`.

The detector measures the density of routing vocabulary in prose. That correlates with the state
at roughly "usually", which is not a measurement.

### 2. The correct instrument already exists and is already populated

`resolve_assembly_state` (`scripts/build_claims_json.py:191-212`) derives
`assembly_state: awaiting_substrate` **one-to-one** from `epistemic_category:
substrate_conditional` (and `enriching` from `substrate_ceiling`). Nothing else feeds either, and
no claim sets `assembly_state` explicitly, so the derivation always runs.

Verified independently 2026-09-01 against the live registry (1086 claims, 166 queue entries):

| measure | value |
|---|---|
| `epistemic_category: substrate_conditional` | **352** |
| of those, joined to a `substrate_queue` entry via `unblocks_claims` | 38 |
| **unrouted** | **314 (89%)** |
| `substrate_ceiling` (`enriching`), for contrast | 31, of which 29 routed |

The contrast is the tell: `enriching` is 94% routed, `awaiting_substrate` is 11% routed. That is
a real, structural asymmetry, and no keyword scan was needed to see it.

### 3. The edge that "edge-first" would add has a 100% failure rate on every existing instance

`awaiting:` is the field the policy would populate. It is carried by **7 of 1086 claims, and all
7 point at nothing schedulable**:

| claim | `awaiting` | in claims.yaml? | in substrate_queue? |
|---|---|---|---|
| `MECH-260`, `SD-037`, `Q-045`, `MECH-439`, `MECH-449` | `ARC-107` | yes | **no** |
| `ARC-110` | `learned_cross_loop_arbitration_validation_falsifier` | no | **no** |
| `ARC-004` | free prose, no id at all | -- | -- |

Two aggravations. First, four of the five `ARC-107` pointers also carry a **hand-written**
`assembly_status: in_progress` (and `MECH-449`, `built`) -- unfalsifiable assertions about the
build state of an item with no queue entry to have one. Second, **`ARC-004`'s free-prose
`awaiting` was written by this very governance session, earlier today** -- which is the cleanest
possible demonstration that the convention invites the defect rather than merely tolerating it.

`validate_claims.py:528-529` states the field is deliberately unchecked: *"awaiting is a
free-form upstream pointer (no enum, no check)."* Scaling that to 314 claims scales the defect.

### 4. A dangling-reference lint would have caught none of this

Full pointer census over `awaiting`, `depends_on`, `emergent_from`, `superseded_by`,
`related_claims`, `distinct_from`, `instantiates`, `child_claims`, `supersedes`, `blocked_by`:
**zero dangling targets across 4172 id-shaped references.** Claims-side referential integrity is
clean.

The defect is a different shape: **a pointer that resolves perfectly and still aims at nothing
buildable.** All five `ARC-107` pointers resolve to a real claim row. The registry has excellent
hygiene against typos and none at all against *pointing at a claim when you meant a build item*.
Any lint built on resolvability would report 0 findings here.

The queue side is dirtier: **51 of 427 `unblocks_claims` entries dangle (12%), 49 distinct, 33 of
them recoverable** by taking the leading id -- values like `'MECH-269 anchor reset'` and
`'SD-032a hysteresis'`, where prose is glued to an id so the exact-dict join
(`build_claims_json.py:155-158`) can never match. That 33 is a genuine cheap fix, and it is the
only pure-edge work this audit endorses.

### 5. `built` is not trustworthy enough to support build-first either

- `MECH-269` -- the queue's self-declared *"single highest-priority substrate"*, unblocking 9
  claims -- is `implementation_status: implemented`, `ready: True`, and resolves to `built`,
  while carrying `post_implementation_validation_status: wired_but_inert`
  (*"read-side hooks ... are dead on this env"*). `_norm_assembly_status_token`
  (`build_claims_json.py:107-131`) reads `implementation_status`/`status`/`ready` and **never
  reads that field**. One known instance, not a pattern -- but it is the highest-priority one.
- `ARC-065` has `ready: False` with an open design decision in `ready_blocked_by`, yet its
  status string `ceiling_lifted_v3_exq_569i_pass` hits the `"ceiling_lifted" -> built` branch.
  Here `built` means "a ceiling was lifted", not "this is done".

## Why the "34 owners already built" statistic does not mean 34 retests are owed

The prior measurement's unlinked/ownerless split used a second keyword heuristic -- "the claim's
prose names an id that is a queue `sd_id`" -- and it inherits the same failure mode. Traced four
cases end to end:

| claim | named owner | what the mention actually is | owed action |
|---|---|---|---|
| `MECH-521` | `MECH-269` | a citation of a past split as **precedent** | nothing; the edge would be false |
| `MECH-395` | `MECH-295` | the **premise** of the gap, not its fix | nothing |
| `Q-067` | `MECH-302` | a **lineage tag** | genuinely ownerless -- see below |
| `MECH-121` | `ARC-065` | a real dependency | a stale-precondition fix; still unrunnable |

Only `MECH-121` benefits, and only partially: its precondition leg (1) is stale (ARC-065's
ceiling was lifted 2026-06-17 and landed in `ree-v3 c0e0ce8`), while leg (2) -- balanced replay
scheduling -- is still unbuilt, now tracked as `mech092-replay-consumer-missing`. The edge halves
the blocker list; it does not make the claim runnable.

## The one concrete build-side finding

**`Q-067` is genuinely ownerless and was misclassified as merely-unlinked.** Its stated blockers
are `MECH-375` / `MECH-376` (the trainable heads); both are registered `candidate` claims and
**neither has a `substrate_queue` entry**. `experimental_confidence: 0.0`, no runs. This is the
Kind-B orphan shape the 2026-08-28 addendum named -- and it was found by reading four claims, not
by running any detector.

## What this changes

- **Do NOT adopt edge-first as framed.** It is priced against two stacked keyword scans, and the
  edge convention it would scale fails on 7 of 7 existing instances.
- **Do NOT adopt build-first as framed** either, until `built` distinguishes "code exists" from
  "hooks fire". Sorting on a field that conflates them mis-prioritises by construction.
- **Do use `assembly_state == awaiting_substrate` joined against `unblocks_claims`** as the
  measurement. 314/352, no backfill, reproducible.
- **Do fix the 33 recoverable `unblocks_claims` values** (id + glued prose). Cheap, safe,
  strictly additive, and the only pure-edge work this audit supports.
- **Do not build a dangling-reference lint for this.** Measured: it would find 0 of the 5
  ARC-107 pointers. If a lint is wanted, the predicate is "resolves to a CLAIM where a BUILD ITEM
  was meant", which is a different and harder check.
- **Retire the keyword detector, or scope it explicitly to prose triage.** Its 189 and the
  registry's 352 are largely disjoint populations (overlap 111).

## Not established

- The provenance of the triage's 155/103 figures. Not reproducible by any stated method; they
  should not be cited again.
- Whether `MECH-269`'s `wired_but_inert` shape is a one-off or the first instance of a class.
  One instance is not a pattern, and this audit does not claim it is.
- The correct classification of `MECH-081` and `MECH-448` -- bare degeneracy guards with no
  corroborating field or run.
