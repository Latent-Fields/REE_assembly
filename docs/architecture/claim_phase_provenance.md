---
title: Claim Phase Provenance and Dependency-Driven Reclassification
parent: "Foundations & Rationale"
grandparent: Architecture
nav_order: 2
---

# Claim Phase Provenance and Dependency-Driven Reclassification

**Status:** design proposal + landed checker, 2026-06-09
**Motivating defect:** the inter-governance-workset generator's `ready` classifier
is phase-blind (`scripts/generate_inter_governance_workset.py` never consults
`implementation_phase`), and nothing mechanically enforces the project's
"phase label follows dependency" principle. Claims surface in the wrong phase
lane.
**Checker:** `scripts/check_claim_phase_consistency.py` (report-only; does not
mutate `claims.yaml`).
**Canon:** `memory/feedback_phase_label_follows_dependency.md`,
`evidence/planning/commitment_closure_plan.md` GAP-9, `docs/architecture/invariant_types.md`.

---

## 1. The principle this enforces

`implementation_phase` (`v3` / `v4` / `v5` ...) is a **prediction** about when a
claim is expected to be built. It is **not a permission gate**. Two corollaries:

1. **Dependency forces phase earlier.** If a V3-scope claim genuinely *depends
   on* a claim labelled `v4+`, that dependency reclassifies the dependency to V3
   **by definition**. A thing needed to build a V3 commitment is, definitionally,
   V3 work. Only the *sequencing / readiness* is open -- never the
   *scope-permission*. A `v4` label on a V3-necessary prerequisite is a
   bookkeeping error, not a deferral decision.

2. **Phase does not leak upward through instantiation.** A `v4` claim whose only
   reverse-dependents are themselves `v4`, and which merely *instantiates* a `v3`
   parent cluster, stays `v4`. The canonical case is **SD-033e** (frontopolar
   parallel-goal-deliberation module): its reverse-dependents MECH-264 / MECH-265
   are both `v4`; it `instantiates: SD-033` (a `v3` parent) but nothing `v3`
   depends on it. It stays `v4`. Its V3 obligation -- registering existing
   mechanisms under the subdivision -- is **graph-registration**, a *separate
   axis* from implementation phase (commitment_closure_plan.md GAP-9).

The defect is that nothing checks (1), and the GAP-9 case shows (2) is easy to
conflate with a phase obligation. This document specifies a provenance schema to
record *why* a claim carries its phase, and a checker that finds violations of
(1) without committing violations of (2).

---

## 2. Phase-provenance schema (proposed `claims.yaml` fields)

These are **proposed** additions for human governance review. The checker does
**not** require them to run -- it computes derivation from the dependency graph
live. The fields make a governance *decision* durable and auditable once a human
accepts a reclassification, and let the checker distinguish "already adjudicated"
from "newly leaking".

```yaml
- id: MECH-xxx
  implementation_phase: v3           # the EFFECTIVE phase (unchanged field)
  phase_provenance: assigned         # assigned | derived          (default: assigned)
  phase_derived_from: ARC-036        # set iff provenance == derived; the v3 build
                                     # commitment whose dependency forced this phase
  phase_locked: false                # default false; true = author asserts the phase
                                     # is intrinsic and must NOT be auto-derived earlier
```

Field semantics:

| field | values | meaning |
|-------|--------|---------|
| `phase_provenance` | `assigned` \| `derived` | `assigned` = author chose this phase as the claim's intrinsic design scope. `derived` = the phase was forced earlier than its intrinsic scope by a dependency from a lower-phase build commitment. Absent => `assigned`. |
| `phase_derived_from` | claim id | Required when `derived`; the V3 build commitment (or nearest root) whose prerequisite edge forced the phase. Provides the audit trail "this is V3 *because* X needs it." |
| `phase_locked` | bool | `true` = the author asserts the phase is intrinsic (e.g. a genuinely V4 frontopolar module). The checker will NOT propose silent reclassification; if a V3 build commitment nonetheless depends on it, that is surfaced as a **CONFLICT** for human adjudication, not an auto-derive. Default `false`. |

Key property: `implementation_phase` continues to hold the **effective** phase
(what the rest of the pipeline -- the V3-pending gate, the indexer -- reads). The
provenance fields annotate *how that value was arrived at*. A reclassified claim
ends up with `implementation_phase: v3`, `phase_provenance: derived`,
`phase_derived_from: <root>` -- so a reader sees both that it is V3 work and that
its intrinsic design scope was later, deferred only by sequencing.

This is deliberately parallel to the existing `invariant_type` / `emergent_from`
pattern (invariant_types.md): a structural field (`phase_provenance`) plus a
provenance pointer (`phase_derived_from`) mirroring `emergent_from`.

### Registration-obligation axis (kept distinct from phase)

GAP-9 (SD-033c / SD-033d / SD-033e) shows a claim can be **V4 implementation**
yet carry a **V3 graph-completeness obligation** (register the existing
mechanisms that sit under the subdivision; finish the claim-graph wiring). These
must not be merged into `implementation_phase`. The registration obligation is
tracked where it already lives -- the closure plan's gap nodes
(`commitment_closure:GAP-9`) -- and, optionally, as a dedicated boolean that does
**not** affect phase:

```yaml
  graph_registration_pending: true   # OPTIONAL: a V3-scope claim-graph-completeness
                                     # task exists, INDEPENDENT of implementation_phase.
                                     # SD-033e: implementation_phase v4 AND this true.
```

The checker treats `graph_registration_pending` as orthogonal: it never reads it
as a phase signal and never proposes changing `implementation_phase` because of
it. This is the explicit guard against the GAP-9 conflation.

---

## 3. The dependency-closure checker

`scripts/check_claim_phase_consistency.py` walks the claim graph transitively and
reports reclassification candidates. It is **report-only**: it prints / emits
JSON, and (in `--strict`) sets a non-zero exit. It never edits `claims.yaml`.

### 3.1 Phase parsing

`implementation_phase` is free-text-tolerant in the live registry (`v3`, `v4`,
`v4)`, `v4).`, `v5`, and long records that begin with the phase token). The
checker extracts the leading `v?(\d+)`. A claim's **effective phase** is the
explicit `implementation_phase` if present, else `3` when `v3_pending: true`,
else unphased.

### 3.2 Edge semantics -- what propagates phase pressure

A "needer -> need" prerequisite edge propagates phase pressure (the needer cannot
be built before the need):

| edge | propagates? | rationale |
|------|-------------|-----------|
| `depends_on` | **yes** | a build prerequisite. |
| `emergent_from` | **yes, STRONGER** | the dependent invariant's *subject* is ill-formed without the substrate (invariant_types.md). A `v3` emergent invariant whose `emergent_from` substrate is `v4` is a hard leak. `emergent_from` is a subset of `depends_on`; the checker de-duplicates and marks the candidate `strength: strong`. |
| `instantiates` | **no** | a parent-cluster *registration* relation, not a build prerequisite, in **either** direction. The `instantiates` target is removed from the `depends_on` edge set. This is what keeps SD-033e from being over-pulled and keeps a `v3` child that instantiates a `v3` parent from spuriously "needing the parent built first." |

### 3.3 Driver gating -- which claims may *force* a reclassification

Only a **V3-scope build commitment** drives reclassification. A claim qualifies as
a driver iff all of:

- effective phase == 3,
- `status` not in {resolved, superseded, deprecated, retracted, withdrawn},
- `claim_type` is not `open_question`,
- `polarity` not in {asks, open, open_question}.

Open questions and pure answer-state claims do **not** force their prerequisites
to be built: being "V3" for a question means "we want to *answer* it in V3," which
a deferred-substrate answer ("the answer is: wait for V4") satisfies. These are
reported in a separate **informational** bucket, never as candidates. (`polarity:
denies` / `records` claims remain drivers -- they are still V3 commitments -- but
rarely have v4 deps.)

### 3.4 Two-phase model: ROOT vs CASCADE

Naively unioning drivers across a transitive walk conflates "directly needs X"
with "needs something three hops past X," producing useless 200-id driver lists.
The checker instead separates:

- **ROOT** -- a V3 build commitment depends **directly** (one prerequisite edge)
  on a `v4+` claim. This is the actual leak; its `direct_drivers` are the v3
  claims responsible and are what a human fixes first.
- **CASCADE** -- a `v4+` claim not directly needed by any v3 build commitment, but
  which becomes V3-necessary **once a ROOT is reclassified** (it is a prerequisite
  of a root, reached through other to-be-reclassified `v4` nodes). `follows_from`
  names the root(s). Cascade closure **stops at `phase_locked` nodes** -- a
  contested node must not silently cascade.

### 3.5 Verdicts

- **RECLASSIFY** (`phase_locked` false): propose `implementation_phase: v3`,
  `phase_provenance: derived`, `phase_derived_from: <root driver>`.
- **CONFLICT** (`phase_locked` true on a claim a V3 build commitment needs): the
  lock and the dependency contradict. A human must either sever / replace the
  dependency or clear the lock. Never auto-reclassified; never cascaded through.

### 3.6 Edge cases handled

- **instantiates vs depends_on** -- instantiation edge dropped (3.2); a child
  instantiating a `v3` parent is not a `v3` dependency, and SD-033e is not
  over-pulled.
- **polarity asserts vs questions** -- questions excluded from drivers (3.3),
  routed to informational.
- **emergent / universal / grey_zone invariants** -- `emergent_from` is a strong
  pulling edge; universal invariants carry no `emergent_from` and so never pull;
  grey_zone invariants pull only via whatever `depends_on` they declare (no
  special casing -- their uncertainty is about classification, not dependency).
- **cycles** -- each walk carries a per-seed `visited` set; cyclic `depends_on`
  terminates.
- **dangling deps** -- a `depends_on` id with no matching claim is reported under
  "Dangling dependency references" (hygiene), never silently dropped.
- **registration obligation** -- never read as a phase signal (Section 2).
- **idempotency** -- a claim already at `implementation_phase: v3` with
  `phase_provenance: derived` is simply a V3 claim and never re-flagged; the
  schema is stable under re-running the checker after a governance decision lands.

### 3.7 CLI

```
python scripts/check_claim_phase_consistency.py            # human report, exit 0
python scripts/check_claim_phase_consistency.py --json     # machine report, exit 0
python scripts/check_claim_phase_consistency.py --warn     # one WARN line per ROOT, exit 0
python scripts/check_claim_phase_consistency.py --strict   # exit 1 if any candidate
```

Importable API (for the generator / governance.sh):

```python
from check_claim_phase_consistency import load_claims, reclassification_candidates
report = reclassification_candidates(load_claims())
leak_ids = set(report["candidates"])     # {claim_id: {verdict, kind, ...}}
```

---

## 4. Integration

### 4.1 governance.sh (recommended: warn-only first, mirroring validate_claims)

Add a non-blocking step after the strict claims validation, so every governance
cycle surfaces phase leaks in its log without blocking the pipeline:

```bash
echo "--- Step 0b: Claim phase-consistency (warn-only) ---"
"$PYTHON" scripts/check_claim_phase_consistency.py --warn || true
```

Promote to `--strict` (blocking) once the current backlog of leaks (Section 5) is
adjudicated -- exactly the trajectory `validate_claims.py` took (warn-only ->
strict gate at the top of governance.sh). Until then, blocking would wedge every
cycle on a pre-existing backlog.

### 4.2 inter-governance-workset generator (the leak point)

`generate_inter_governance_workset.py` decides `ready` without consulting
`implementation_phase`. Recommended minimal patch (documented here rather than
applied inline, because the generator is high-contention and was last edited by a
concurrent session): import the checker's candidate set once in `build_workset()`
and annotate / down-rank any item whose `claim_ids` intersect a RECLASSIFY/CONFLICT
candidate:

```python
# near the top of build_workset()
try:
    from check_claim_phase_consistency import (
        load_claims as _load_claims_full,
        reclassification_candidates,
    )
    _phase_leaks = set(reclassification_candidates(_load_claims_full())["candidates"])
except Exception:
    _phase_leaks = set()

# in add(...) or the post-build enrichment loop, for each item:
leaked = [c for c in (item.get("claim_ids") or []) if c in _phase_leaks]
if leaked:
    item["phase_leak"] = sorted(leaked)
    # a phase-leaking claim is not cleanly 'ready' -- its phase lane is contested
    if item.get("status") == "ready":
        item["status"] = "blocked"
        item.setdefault("blocked_by", []).append(
            f"phase-consistency: depends on phase-leaking claim(s) {', '.join(leaked)} "
            f"-- run check_claim_phase_consistency.py"
        )
```

This closes the leak going forward: a work package that touches a claim whose
phase lane is contested no longer surfaces as cleanly `ready` -- it is marked
`blocked` with a pointer to the checker, exactly as substrate-blocked retests are
today. The annotation is keyed on the checker's authoritative candidate set, so
the two never drift.

---

## 5. Live results (against `docs/claims/claims.yaml`, 2026-06-09)

`python scripts/check_claim_phase_consistency.py` over 685 claims / 249 V3
build-commitment seeds finds **12 ROOT leaks, 3 CASCADE candidates, 0 CONFLICTs**
(plus 10 dangling `MECH-057` references -- a deleted/renamed claim still named in
`depends_on`). SD-033e is correctly **absent** (closed v4 triangle with
MECH-264 / MECH-265; over-pull guard holds).

### ROOT leaks (act on these first)

| candidate (now) | directly needed by V3 build commitment(s) | proposed |
|-----------------|-------------------------------------------|----------|
| ARC-031 (v4) | MECH-205, MECH-208 | -> v3 derived from MECH-205 |
| ARC-039 (v4) | MECH-261 | -> v3 derived from MECH-261 |
| ARC-053 (v4) | ARC-054 | -> v3 derived from ARC-054 |
| ARC-072 (v4) | SD-055 | -> v3 derived from SD-055 |
| INV-062 (v4) | MECH-213 | -> v3 derived from MECH-213 |
| MECH-121 (v4) | MECH-165, MECH-203, MECH-205, MECH-212 | -> v3 derived from MECH-165 |
| MECH-123 (v4) | MECH-204, MECH-213 | -> v3 derived from MECH-204 |
| MECH-124 (v4) | ARC-036, MECH-208 | -> v3 derived from ARC-036 |
| MECH-210 (v4) | MECH-213 | -> v3 derived from MECH-213 |
| MECH-274 (v4) | ARC-059 | -> v3 derived from ARC-059 |
| MECH-308 (v4) | MECH-330 | -> v3 derived from MECH-330 |
| MECH-326 (v4) | SD-055 | -> v3 derived from SD-055 |

### CASCADE candidates (become V3-necessary once the roots above are reclassified)

| candidate (now) | follows from root(s) | example path |
|-----------------|----------------------|--------------|
| MECH-122 (v4) [strong: emergent_from] | ARC-031, ARC-039, MECH-121, MECH-123, MECH-124, ... | MECH-121 -> MECH-122 |
| MECH-209 (v4) | INV-062, MECH-210 | INV-062 -> MECH-209 |
| MECH-325 (v4) | ARC-072, MECH-326 | ARC-072 -> MECH-325 |

These are **candidates for human governance review**, not automatic edits. Each
proposed reclassification should be confirmed in a `/governance` cycle (is the
dependency real, or should the *edge* be cut?). The checker's job is to make every
such leak visible and attributable; the adjudication -- reclassify the dependency,
or sever the dependency, or `phase_locked` the prerequisite and re-scope the
needer -- stays with governance.

The MECH-121..124 cluster (the "epistemic / consolidation" mechanism block) and
ARC-039 are foundational emergent-substrate references depended on widely; they are
the highest-value items to adjudicate first because their resolution determines the
cascade.

---

## 6. What this is not

- Not an auto-migrator. It proposes; governance disposes. No `claims.yaml` field
  is written by the checker.
- Not a change to confidence scoring, the V3-pending gate, or substrate promotion.
- Not a merge of implementation phase with the graph-registration obligation --
  Section 2 keeps them on separate axes by construction (the GAP-9 guard).
- Not a claim that `v4` is "wrong." A `v4` label is right until a `v3` build
  commitment depends on it; then, by the principle, only the *label* was a
  prediction that the dependency has overtaken.
