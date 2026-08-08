# ARC-039 phase reclassification -- staged disposition

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or whichever registry).**

- **Date:** 2026-08-08
- **Session:** `metaworker-chip-20260808-arc039-phase-consistency-review` (headless, metaworker-dispatch)
- **Chip:** `chip-20260808-arc039-phase-consistency-review`
- **Landed alongside this file (already on `origin/master`):** `scripts/check_claim_phase_consistency.py`
  + `scripts/test_check_claim_phase_consistency.py` (26 tests), and
  `docs/architecture/claim_phase_provenance.md` Sections 1, 3.8, 5a.

**Why staged rather than applied.** `docs/claims/claims.yaml` was under an active
TASK_CLAIMS claim by `mech-322-evidence-confirm-bc9fbf` (the 2026-08-08
thought-digestion campaign, claimed 10:45:54Z, landing waves continuously).
`task_claim.py open` arbitrated and returned exit 3 naming that session as owner.
Per CLAUDE.md **Conflict resolution**, a non-owner verdict is binding, so no edit
to `claims.yaml` was made. Every proposed edit below is written out verbatim so
the owning session -- or a later `/governance` cycle -- can apply it directly.

---

## 1. Finding

ARC-039 ("Durable long-term storage of the hippocampal viability map requires a
hippocampal-entorhinal loop...") currently reads:

```yaml
implementation_phase: v3
phase_provenance: derived
phase_derived_from: MECH-261
```

while its own `notes` carry an explicit **"V4 scope justification"** listing three
architectural requirements that do not exist in V3 (a separate entorhinal grid
module; offline sleep-equivalent processing phases distinct from waking
micro-quiescence; a grid read-back mechanism), and its `evidence_quality_note`
records **"Hold at candidate (V4 scope maintained)"**.

This is **not a data-entry error**. It is `scripts/check_claim_phase_consistency.py`
Section 3.4's ROOT rule firing correctly on an incorrect input -- a single line in
MECH-261's dependency list:

```yaml
  - ARC-039          # entorhinal grid loop (offline consolidation target)
```

## 2. The edge is mistyped -- four independent lines of evidence

1. **The needer was built without the need.** MECH-261 reached `status: stable` in
   V3 (validated by V3-EXQ-446/455/453, 33 supports) while ARC-039's entorhinal
   circuit never existed and still does not. A prerequisite that was never built,
   for a claim that reached `stable`, was not a prerequisite.
2. **MECH-261's own implementation does not reference ARC-039.** Its
   `implementation_note` enumerates the eight write-gate targets in the landed
   `SalienceCoordinator` registry (`sd_033a`, `sd_033b`, `sd_033c`, `sd_033d`,
   `hc_viability`, `sensory_buffer`, `autonomic`, `e3_policy`). ARC-039 is in
   neither that list nor the `functional_restatement` write-target list.
3. **The comment describes a consumer, not a prerequisite.** A write gate's
   "target" is what the gate is applied *to* -- downstream of the gate. MECH-261
   supplies the `offline_consolidation` mode weight that ARC-039's loop would be
   gated *by*; the dependency runs the other way.
4. **The correct direction is already recorded on ARC-039**, and its own comment
   admits the symmetry:
   `depends_on: MECH-261  # ... the offline_consolidation mode vector is what
   licenses entorhinal-grid-loop engagement (symmetric with MECH-261.depends_on
   on ARC-039 as its offline consolidation target)`.

Point 4 is the root cause in one word: **"symmetric."** An *association* was
deliberately recorded in both directions, in a field the checker reads as a
*directed prerequisite*. `depends_on` has no symmetric reading, so the reverse
edge became a phase pull.

**Deletion is safe, and loses no information:** the true relation survives on
ARC-039's side (point 4), and MECH-261 is the **only** V3 build commitment that
depends on ARC-039. The two other dependents, MECH-148 and INV-039, are both `v4`
and therefore not drivers. So removing this one edge removes the entire pull.

## 3. Proposed edits (recommendation: (c), the combination)

### Edit 1 -- `MECH-261.depends_on`: DELETE the ARC-039 line

```yaml
# BEFORE
  depends_on:
    - SD-032a          # coordinator (source of operating_mode)
    - MECH-094         # hypothesis tag (the specific tag this generalises)
    - INV-049          # sleep necessity (coordinates with consolidation mode)
    - MECH-092         # micro-quiescence replay
    - ARC-038          # viability map (one write target)
    - ARC-039          # entorhinal grid loop (offline consolidation target)   <-- DELETE
    - SD-033a          # lateral-PFC-analog rule/goal substrate (primary write target)
    - SD-033b          # OFC-analog specific-outcome / state-space substrate (secondary write target)
    - SD-033c          # vmPFC-analog value substrate (gated under mode-specific rules)
```

**Delete, do not move to `instantiates`.** `instantiates` means "registers under a
parent cluster" (design doc Section 2 / GAP-9); MECH-261 does not instantiate
ARC-039, so moving it there would trade one mistyped edge for another. There is
no "is a downstream consumer of" edge type in this schema, and inventing one is
out of scope for this fix -- see Section 5.

Suggested replacement, so the relationship is not simply lost:

```yaml
    - ARC-038          # viability map (one write target)
    - SD-033a          # ... (unchanged)
```

and, in MECH-261's `notes`, a new paragraph:

> 2026-08-08 edge correction: `depends_on: ARC-039` was removed. It was recorded
> as a *symmetric* association ("offline consolidation target"), but `depends_on`
> is a directed build prerequisite, and MECH-261 reached `status: stable` in V3
> (V3-EXQ-446/455/453) while ARC-039's entorhinal circuit was never built -- so
> ARC-039 was never a prerequisite of MECH-261. ARC-039 is a future *consumer* of
> MECH-261's `offline_consolidation` mode weight; that true direction is recorded
> on ARC-039's own `depends_on: MECH-261`. The reversed edge had silently
> reclassified ARC-039 from its authored v4 scope to v3 via
> `check_claim_phase_consistency.py`.

### Edit 2 -- `ARC-039`: restore the authored V4 scope

```yaml
# BEFORE                          # AFTER
implementation_phase: v3          implementation_phase: v4
phase_provenance: derived         phase_provenance: assigned
phase_derived_from: MECH-261      # (remove the field entirely)
```

This restores exactly what ARC-039's own `notes` and `evidence_quality_note`
already assert. EXQ-214 (2026-04-03) is the empirical backing: the only V3 proxy
ever attempted, `ResidueField.integrate()`, was found to actively **degrade**
residue-hazard correlation (`mean_delta_accuracy=-0.283`) rather than consolidate
it -- so there is no V3-buildable substitute, and a v3 label promises work that
cannot be done.

### Edit 3 -- `ARC-039`: set `phase_locked: true`

```yaml
phase_locked: true   # intrinsic V4 scope: entorhinal grid module + offline
                     # processing phase + grid read-back, none of which exist in
                     # V3 (see notes 'V4 scope justification'); EXQ-214 showed the
                     # only V3 proxy attempted actively degrades. Any future V3
                     # dependency on this claim must route to CONFLICT for human
                     # adjudication, not a silent RECLASSIFY.
```

Belt-and-braces given Edit 1, but warranted on its own terms: it is the field's
exact designed purpose, and **it is currently set on 0 of 994 claims**, so the
CONFLICT path has never fired in the checker's lifetime. A documented escape hatch
with zero adoption is not protecting anything.

### After applying

Rebuild `docs/assets/data/claims.json` and commit via `scripts/ree_commit.py`
(CLAUDE.md: `claims.yaml` is `sync_daemon`-managed). Then re-run
`python scripts/check_claim_phase_consistency.py`; expected: ARC-039 absent from
both the candidate lists and the reciprocal-cycle list, load-bearing cycles 5 -> 4.

## 4. This is not a one-off -- 4 more instances

The same shape (a reciprocal `depends_on` pair where one direction drove a phase
reclassification) is now detected mechanically by the `reciprocal_prerequisite_cycles`
check landed with this work. Live count: **92 reciprocal pairs, 5 load-bearing.**

| pair | state | note |
|---|---|---|
| **ARC-039 <-> MECH-261** | applied: ARC-039 v3 `derived from` MECH-261 | adjudicated above |
| MECH-122 <-> MECH-121 | applied: MECH-122 v3 `derived from` MECH-121 | not investigated |
| MECH-209 <-> INV-062 | applied: MECH-209 v3 `derived from` INV-062 | not investigated |
| MECH-325 <-> ARC-072 | applied: MECH-325 v3 `derived from` ARC-072 | not investigated |
| MECH-265 <-> SD-033e | **live ROOT leak**, not yet applied | see below |

**MECH-265 <-> SD-033e deserves attention first**, because SD-033e is the design
doc's own canonical "correctly stays v4" worked example. That example has drifted:
SD-033e is now `v3` and MECH-264 is now `v3`, so the closed v4 triangle the
example rested on has opened, and SD-033e is now pulling MECH-265 (v4) via a
reciprocal edge -- phase flowing in the direction the example was written to rule
out. Recorded in the design doc Section 1 corollary 2. The `instantiates`
over-pull guard itself is unaffected and still works (pinned by
`test_instantiates_target_does_not_close_a_cycle`); only the illustration is stale.

The remaining four are flagged, **not** adjudicated -- each needs the same
four-point evidence check done above, which is claim-specific scientific
judgement. They are the natural next `/governance` items.

## 5. Deliberately not done

- **No new edge type.** The honest description of MECH-261 -> ARC-039 is "future
  downstream consumer", which this schema cannot express; `depends_on` and
  `instantiates` are the only two relations, and neither fits. Adding a third is a
  schema change affecting every consumer of the graph and is well outside a
  validator fix. Deleting the edge is correct and lossless *here* because the true
  direction is already recorded -- but if the other four cases turn out to need
  the same treatment and the information is NOT recoverable from the other side,
  that is the point to reconsider a `consumed_by` / `informs` relation.
- **`--strict` unchanged.** It still keys on candidates only. A reciprocal cycle
  is arguably more strict-worthy than a candidate (it is a proven defect, not a
  proposal), but `governance.sh` calls `--warn || true` and promoting the gate is
  a governance decision, not a side effect of adding a check.
- **Longer cycles.** Only 2-cycles are detected. Longer ones are common in a
  densely cross-referenced registry, are often legitimate ("these ideas are
  mutually constitutive"), and need judgement to triage. A 2-cycle needs none.
