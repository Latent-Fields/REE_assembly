# P3 interface requirements H1-H8, reconciled against the BUILT harness

**Date:** 2026-09-10
**Reconciles:** [`provenance_p3_replay_amplification_design.md`](provenance_p3_replay_amplification_design.md) section 9.2 (requirements H1-H8)
**Against:** [`scripts/provenance_genealogy_harness.py`](../../scripts/provenance_genealogy_harness.py) as landed at REE_assembly `062d774289` / `1d72f60073` (726 lines)
**Companion:** [`provenance_p3_r2_spike_result.md`](provenance_p3_r2_spike_result.md) -- the section 5 spike this reconciliation exists to unblock
**Status:** reconciliation + a minimal, spike-scoped harness change. No claim registered or promoted, no queue entry, no edit to the P3 design note, the harness design note, the ladder or the supplement. Recommendations to those documents are recorded in section 6 here and are **not** applied.

The P3 design was written against an abstract eight-operation contract because the harness did not exist yet (its own section 9 says so). It exists now. **Every verdict below was taken against the CODE, not against the harness design note's prose** -- twice they disagree, and both times the code is what binds.

---

## 1. Verdict, up front

| # | Requirement (design 9.2) | Verdict, as built | What settles it |
|---|---|---|---|
| **H1** | `replay` takes a `kind` argument | **GAP** -> closed for `rehearsal` only | `replay()` had no `kind` parameter; it hard-coded the descendant kind `"replay"` |
| **H2** | `replay` takes `mode` = `in_place` / `append` | **PARTIAL** -> closed | `mode` existed and `in_place` added no node -- but changed **no content**, so fidelity could not move |
| **H3** | settable selection policy (`uniform`/`preferential`) | **PARTIAL** -- deferred | no internal default to override (the caller passes `trace_id`), but no shared policy primitive either |
| **H4** | true source count readable alongside the estimate | **SATISFIED** | `true_effective_source_count(truth, trace_set)`, scorer-only -- and that is the side P3 needs |
| **H5** | fidelity **settable**, not only readable | **PARTIAL** -- deferred | `eta` sets a descendant's fidelity at creation; nothing sets an **existing** trace's |
| **H6** | freeze primitive, enforced not conventional | **GAP** -> closed | no freeze existed; `add_world_event` was callable after `t0` and demonstrably raised the true source count |
| **H7** | separate RNG streams for world vs replay | **SATISFIED** | `content_rng` vs `rng` are distinct parameters throughout |
| **H8** | `degrade` split creation-time vs re-encoding | **GAP** -- deferred, **and in tension with the endogeneity criterion** | `degrade()` has no way to restrict which links it touches, and the obvious fix is forbidden -- see 3.8 |

**Two of the three starting hypotheses carried into this task were wrong, and the wrong one matters most.** H2 was expected to be SATISFIED (section 10 calls it "the one gated precondition", so a SATISFIED verdict would have discharged the rung's `complex (probe-gated)` node on the spot). It was not satisfied. H7 and H4 were expected SATISFIED and are. H5 was expected to be a real gap and is -- partially, and not in the way the design predicted.

---

## 2. The finding: H2 was half-built, and the missing half is invisible

`replay(mode='in_place')` existed, was exercised by P1-R7, and did exactly one thing:

```python
if mode == "in_place":
    store.retrieval_events[trace_id] += n
    return []
```

It incremented a counter. It did not touch `store.content`. `retrieval_fidelity` reads `store.content[trace_id]` against the true seed, so **fidelity was bit-identical at every replay count** -- measured, not inferred: after 16 in-place replays the content array compares `np.array_equal` True and the fidelity delta is exactly `0.000000e+00`.

Design section 2.2 states the requirement in two halves: "`mode = in_place` raises the source node's retrieval fidelity **and adds no node**". The build had the second half and not the first. Nothing in P1 could have caught this, because P1-R7 uses `in_place` to hold cardinality fixed while moving retrieval *events* -- it never reads fidelity across replay counts. The half that P1 needed was built; the half only P3 needs was not.

**This is the same failure shape section 5 warns about, in the mirror direction.** Section 5 fears an `append`-only replay, where the count rises in every arm and P3 measures replay exposure. The actual build gave a `mode` argument that satisfies the *cardinality* half of the healthy arm perfectly and the *fidelity* half not at all -- so the arm was unreachable, and, exactly as section 5 predicts, "invisible until the results are in". A contract review reading only for the presence of a `mode` argument would have passed it.

---

## 3. Requirement by requirement

### 3.1 H1 -- `replay(kind=...)`: GAP, closed for `rehearsal` only

`replay()`'s signature was `(store, truth, trace_id, n, content_rng, mode, t, eta)`. No `kind`. In `spawn` mode it hard-coded the descendant kind `"replay"`.

Note the two taxonomies are genuinely different and must not be collapsed: `DESCENDANT_KINDS` (`replay` / `prediction` / `retrieved_memory` / `ambiguous_perception`) names how a trace's **content** was produced; P3's `REPLAY_KINDS` (`rehearsal` / `relational_link` / `prediction`) names what the replay event is **for**.

Closed to the extent the spike needs: `kind` is now a parameter defaulting to `"rehearsal"` (which reproduces the previous behaviour exactly). `rehearsal` works in both modes; `prediction` works in `spawn` only; `relational_link` raises. **The unimplemented kinds raise rather than aliasing to rehearsal** -- a kind that quietly behaved like another would let P3-R1 report a stratification difference it never tested.

### 3.2 H2 -- `mode`: PARTIAL, closed

See section 2. Closed by `reinstate()` (harness line 460), one in-place reinstatement event:

```python
content[i] <- content[i] + gain * edge_w[i] * (content[ancestor(i)] - content[i])
```

`REINSTATE_GAIN = 0.25`, declared as a module constant rather than a per-call argument so it is a property of the architecture and not a per-arm tuning knob.

**Endogeneity (harness design note section 3) holds, and by signature.** `reinstate(store, trace_id, gain)` takes no `GroundTruth` and cannot be given one. Every term is a quantity the architecture holds in its own right: its own content, its own ancestry pointer, its own binding strength.

The objection worth answering explicitly: for a first-generation descendant the scorer's fidelity target *is* numerically the seed trace, so does pulling toward the stored ancestor amount to reading ground truth? No. That coincidence is a property of how fidelity is **defined** (reconstruction quality against the true seed), not a channel. The architecture is never told which trace is the seed; it follows its own ancestry pointer, which the dynamics are free to have decayed or re-pointed. The step is scaled by `edge_w` -- the architecture's own confidence in that pointer -- so under intact ancestry reinstatement repairs, under decayed ancestry it does nothing, and under a re-pointed edge it pulls toward the wrong trace and fidelity **falls**.

That is not a hoped-for property. It is the spike's S1 check, and it is the one part of the spike that was genuinely uncertain: measured 0.0560 rise under `VERIDICAL` against 0.0021 under heavy decay, a ratio of 0.0375 against a preregistered ceiling of 0.5.

Two deliberate non-behaviours, both load-bearing:

- **It does not touch the ancestry edge set.** `degrade` owns that (contract op 2), and harness design note section 6 requires `degrade` and `replay` to stay orthogonal. Letting reinstatement strengthen `edge_w` would couple them **and** would move `N_eff` -- the variable the healthy arm must hold flat. Whether reconsolidation *should* strengthen the binding is a real question; it is P3's to answer, and it is recorded as recommendation 4 below rather than settled here.
- **It adds no noise.** The minimal closure is deterministic given the store, so the spike's fidelity movement is attributable to reinstatement alone. Noisy reinstatement is what an in-place fidelity **knob** would need -- which is H5, and is deferred with it.

### 3.3 H3 -- selection policy: PARTIAL, deferred

The requirement's stated fear is a hard-coded internal default. That is **not** the situation: `replay()` takes `trace_id` explicitly, so selection is entirely the caller's, and both `uniform` and `preferential` are implementable today with no harness change (the spike implements `uniform` driver-side). What is missing is a *shared* primitive, so that P3's two predeclared levels are defined once rather than re-implemented per driver.

Cost to close: a ~10-line `select_source(store, policy, rng)` reading association strength for the `preferential` level. Not needed by a single-cell spike.

### 3.4 H4 -- true count alongside the estimate: SATISFIED, and the tension is not real

`true_effective_source_count(truth, trace_set)` exists and is **scorer-only** by signature, as the harness walls ground truth away from the inference path by type.

The question this raises -- does P3 need it inference-side, which would breach endogeneity, or scorer-side, which is already true? -- resolves cleanly to **scorer-side**. Design section 7.2 point 3 asks for it so that "the instrument's bias at that exact operating point is visible rather than interpolated from the ladder": that is bias correction in the **reporting** path, computed by the experimenter over a finished run, never fed back into the architecture's state. The instrument-bias ladder of section 7.2 is scorer work throughout.

So H4 is satisfied and must **stay** scorer-only. Had P3 needed it inference-side, the correct response would have been to report the conflict, not to breach the criterion. The spike reads it scorer-side and reports it alongside the estimate, which is exactly the section 7.2 shape.

### 3.5 H5 -- fidelity settable: PARTIAL, deferred

`retrieval_fidelity` is read-only. There **is** an exposed content-noise parameter, `eta`, and it moves descendant fidelity over a wide range (measured: `eta` 0.1 / 0.4 / 0.9 -> mean fidelity 0.9953 / 0.9308 / 0.7387), so a P3-R3 titration over *newly spawned* descendants is possible today.

What does not exist is any knob on the fidelity of an **existing** trace -- which is precisely the population the in-place arm operates on. So the design's prediction in section 9.3 is upheld but needs sharpening: the gap is not that operation 8 is read-only in general, it is that it is read-only **for the in-place path**, where `eta` has no purchase.

Cost to close: a `noise` argument on `reinstate()` (reinstatement that overshoots or undershoots), giving a continuous, bounded, per-node fidelity dial on the same scale section 9.3 requires. Not needed by a single-cell spike, which matches nothing against anything.

### 3.6 H6 -- freeze primitive: GAP, closed

There was no freeze, and the leak was live: `add_world_event` was callable at any time and, demonstrated directly, moved the true independent-source count 1.00 -> 2.00 after `t0`.

Closed with `freeze(store)` (harness line 266) and a `frozen` flag on the store that survives `copy()`. Two things are refused once frozen:

1. `add_world_event`;
2. an `ambiguous_perception` descendant with `alpha < 1`.

The second is the subtle one and is the reason a boolean was not enough on its own. `ambiguous_perception` is the single declared exception to "no generator reads the world", so it is the one remaining path by which fresh world information can enter a frozen episode -- in proportion to `1 - alpha`. At `alpha = 1` it carries no world term and stays legal.

**This is the one requirement closed that the spike does not strictly need**, and the justification is narrow: the spike's central claim is "fidelity rose while no new evidence arrived". Without the freeze that claim rests on the driver's discipline; with it, it is refused by construction. Six lines converts an assertion into an assertion-by-construction, and design section 2.1 asks for exactly that ("must be enforced, not conventional"). There is deliberately no `unfreeze`.

### 3.7 H7 -- separate RNG streams: SATISFIED

`new_episode`, `spawn_descendant` and `replay` take `content_rng`; `degrade` and `read_vote` take `rng`. They are distinct parameters and the drivers pass independently-seeded generators (P1: content 17, dynamics 23). The spike adds a third, `SELECT_SEED`, for replay selection, which is the H7 separation applied to the axis H3 introduces.

### 3.8 H8 -- degrade split: GAP, deferred, and the obvious fix is forbidden

`degrade()` selects edges by `store.t[i] <= step` and has no argument restricting which links it touches, so P3-A (new links only) and P3-B (new plus re-encoded) cannot be separated. Real gap.

**And it is in direct tension with the endogeneity criterion, which the design does not notice.** The natural closure -- an `only_ids` or `edges` argument naming which links to degrade -- is exactly what the harness design note section 3 forbids: "`degrade()` takes NO ancestry-indexed argument. Its signature cannot express one." An `only_ids` argument *is* an ancestry-indexed argument, and adding one would reopen the stipulation route that probe P0 was built to close.

The legal closure is a **time-window** argument (`since_t`): a time is not an ancestry index, the store already carries per-trace timestamps, and "degrade only links created after `t0`" is expressible without naming an edge. Recorded as recommendation 2 below. Not needed by the spike, which runs `VERIDICAL` and does not degrade at all.

---

## 4. What was closed, and why only that

Closed: **H1** (for `rehearsal`), **H2**, **H6**. Deferred: **H3**, **H5**, **H8**. Already satisfied: **H4**, **H7**.

Design section 10 is explicit that "the correct next step is the section 5 spike, not the confirmatory grid", so the closure is scoped to what one cell of `VERIDICAL / rehearsal / in_place` actually exercises. H3, H5 and H8 are all confirmatory-grid requirements: a single cell has no second selection policy to cross against, no second condition to match fidelity against, and no degradation to split.

**Deferred items, with cost:**

| # | What is missing | Cost to close |
|---|---|---|
| H1 (rest) | `relational_link` and in-place `prediction` replay kinds | wire `link()` into replay stratification; decide what a predictive replay reinstates in place (a design question, not only code) |
| H3 | named `uniform` / `preferential` primitive | ~10 lines: `select_source(store, policy, rng)` over association strength |
| H5 | fidelity dial on an existing trace | a `noise` argument on `reinstate()`, plus a titration sweep in the driver |
| H8 | P3-A / P3-B split | a `since_t` window argument on `degrade()` -- **not** `only_ids`, see 3.8 |

**Regression evidence.** The harness is a landed dependency of the P1 assay, so P1 was re-run before and after on content-seed 17 / dynamics-seed 23. Every preregistered criterion still passes (MAIN M1-M4, R2, R3, R4, R7, C1), and the check is stronger than that: **the entire results payload is byte-identical**, as is that of the third consumer, `provenance_p1r5_retrieval_attribution_arm.py`. That is structural rather than lucky -- both existing `in_place` call sites replay `trace_id = 0`, the world event, whose `edge_target` is `-1`, so ancestry-mediated reinstatement is a guaranteed no-op there. Full numbers in the spike result note, section 5.

---

## 5. What the reconciliation could not settle

- **Whether `REINSTATE_GAIN = 0.25` is the right magnitude.** It was fixed before any spike run, from first principles (a quarter of the remaining gap per event, scaled by binding), and never adjusted. It sets how fast fidelity saturates, so it interacts with P3's replay-count grid `{0,1,2,4,8,16}` -- at this gain, `VERIDICAL` fidelity is essentially saturated by `r = 16`. The confirmatory grid should choose it deliberately, and the spike result note records the measured trajectory it would be choosing against.
- **Whether the harness's fidelity scale meets section 9.3's "matched is definable" requirement.** It is a bounded continuous cosine on `[-1, 1]` with a documented reference (the true seed content), which satisfies the stated criterion on its face. Whether `+/-0.02` is achievable as a *matching* tolerance across ancestry conditions is a P3-R3 question and was not tested here.
- **The harness has no test file.** Its three consumers are assay drivers, and verification in this branch is by their preregistered criteria -- the established convention, so this reconciliation followed it rather than departing from it. The new primitives were checked directly (18 assertions: freeze refusals, kind dispatch, `reinstate` endogeneity and its edge-set / cardinality / `N_eff` invariances) and the checks are reproduced in the spike result note section 5. A permanent test file for the state layer is worth someone's chip; it was not this one's.

---

## 6. Recommendations to the P3 design note (recorded, NOT applied)

This document does not edit `provenance_p3_replay_amplification_design.md`.

1. **Section 9.2, H2 -- state the requirement as two clauses and check them separately.** "Takes a `mode` argument" is satisfiable while the arm stays unreachable. The two clauses are *adds no node* and *raises the source node's fidelity*; the built harness had the first without the second, and a reviewer reading section 9.2's one-line form would have marked H2 satisfied.
2. **Section 9.2, H8 -- name the legal closure.** The requirement as written invites an ancestry-indexed argument to `degrade()`, which the harness design note section 3 forbids outright. Recommend it specify a time-window split, so the requirement and the endogeneity criterion stop pointing in opposite directions.
3. **Section 9.3 -- narrow the operation-8 prediction.** It predicts a read-only fidelity. What was actually found is a *creation-time* dial (`eta`) with real range and no dial at all on the in-place path. The sharpened form is the more useful requirement, and it is the one P3-R3 will hit.
4. **Sections 2.2 / 8.2 -- say whether reinstatement may strengthen the ancestry binding.** The design specifies what in-place replay does to fidelity and to node count, and is silent on `edge_w`. That silence is load-bearing: strengthening the binding would move `N_eff` -- the variable the healthy arm must hold flat -- in the *protective* direction, which is not an artefact but is also not nothing. This build declines to touch it, and the reason (op 2 owns the edge set; section 6 requires the two orthogonal) is a build decision that should be ratified or reversed in the design.
5. **Section 8.1a -- the "fidelity route" needs a channel that does not currently exist, and this is the sharpest finding for the grid.** The route is predeclared as "confidence up, count flat, calibration IMPROVES". In this architecture `confidence(votes, p_est, n_eff)` has **no fidelity term**, so raising retrieval fidelity cannot raise confidence except by flipping a vote. Measured in the spike: fidelity `0.9313 -> 0.9873` while confidence moved `-0.0018` and signed error `+0.0015` -- both at noise. The harness *does* have a healthy-improvement channel that reaches confidence, but it is the read-noise averaging of P1-R3 (`read_vote(n_reads=...)` raising `p`), which is a different mechanism from content fidelity. Recommend section 8.1a distinguish the two explicitly, and that the grid either give operation 7 a per-trace reliability term derived from fidelity, or predeclare that the fidelity route is expected to show **flat** confidence -- otherwise a correct healthy-replay result will read as a null against a route that was never reachable.

---

## 7. Epistemic boundary

- Nothing here is evidence about psychosis, and nothing here is claim evidence. This is a contract reconciliation and a synthetic harness change.
- The verdicts are about the harness **as landed at `062d774289` / `1d72f60073`** and about the stored-tag route only (P1-R5, predeclared). A read-time-attribution architecture is a different system.
- H2's closure is one mechanism -- ancestry-mediated pattern completion toward the bound ancestor. It is a reasonable reading of what "reinstatement" means and it satisfies the design's stated requirement; it is not the only mechanism that could, and the spike result is a result about this one.
