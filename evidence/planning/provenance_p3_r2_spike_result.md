# P3-R2 -- result: the healthy-replay reachability spike

**Date:** 2026-09-10
**Design / preregistration source:** [`provenance_p3_replay_amplification_design.md`](provenance_p3_replay_amplification_design.md) section 5 (the gate), section 10 (the routing rule), sections 2.1-2.5, 7.2, 8.1a
**Driver:** [`scripts/provenance_p3_r2_reachability_spike.py`](../../scripts/provenance_p3_r2_reachability_spike.py)
**Harness:** [`scripts/provenance_genealogy_harness.py`](../../scripts/provenance_genealogy_harness.py)
**Contract reconciliation:** [`provenance_p3_harness_contract_reconciliation.md`](provenance_p3_harness_contract_reconciliation.md) -- H1-H8 verdicts and what was closed
**Status:** synthetic pilot spike. Seeds are pilot and discarded (design section 5). No claim registered or promoted, no queue entry, no confirmatory grid, no edit to the design note, the ladder or the supplement.

---

## 1. Verdict, up front

**The arm was unreachable as built, and is reachable once requirement H2 is fully implemented.**

| | Gate | Fidelity rise (r=0 -> r=16) | `N_eff` drift |
|---|---|---|---|
| **Stage 0** -- harness as landed | **FAIL** | **exactly 0.000000000** | 0.00 |
| **Stage 1** -- H2's missing half closed | **PASS** | **+0.056008** | **exactly 0.00e+00** |

Routing, in the design's own vocabulary (section 10):

> **The P3 rung's `complex (probe-gated)` precondition is discharged. The rung reduces to `complicated (buildable)`** -- but only behind a harness change that did not exist when the spike was written, so the honest full statement is: **as built the rung was `puzzle (known rules)`; the missing fact was a harness capability; it has been added; the rung is now `complicated (buildable)`.**

That two-step is the result, and collapsing it to "the spike passed" would misreport it. Section 10 anticipated exactly one of these branches and got both, in sequence.

---

## 2. What was preregistered, and when

All criteria were fixed in the driver's module docstring **before either stage ran**, and are evaluated by `evaluate_preregistered_criteria()` in the style of P1 and of `convergence_signal_synthetic_assay_001.py`.

**Primary gate** (all four, on `VERIDICAL / rehearsal / in_place`):

- **G1** mean retrieval fidelity over the rehearsed descendant set rises by at least **+0.02** from `r=0` to `r=16`, and the series is non-decreasing.
- **G2** `|N_eff(16) - N_eff(0)| <= 0.05`.
- **G3** trace count identical at every `r`.
- **G4** `VERIDICAL` rate is 1.00 at every `r`.

**Secondary, declared, reported, not part of the gate:** **S1** the fidelity rise under a corrupted-ancestry comparator is at most `0.5x` the `VERIDICAL` rise (**failure is a STOP, not a gate miss**); **S2** a gen-2 descendant saturates below a gen-1 one; **S3** confidence and calibration deltas at flat count, located against section 8.1a's three routes.

Two preregistration choices worth naming, both made in advance:

- **G1 gates on an absolute floor, never on a rank correlation.** Section 8.3 requires an absolute floor alongside any relative test, and P1's disclosure 2 is this branch's record of the specific trap: Spearman's rho is undefined on a constant series, which is *exactly* what Stage 0 produces. Had G1 gated on rho, Stage 0 would have failed for the wrong reason and the failure would have looked like a statistical artefact rather than the finding. `rho` is computed and reported at both stages and gates nothing. (Stage 0: `nan`, as predicted. Stage 1: `1.0000`.)
- **The +0.02 floor is design section 6's own matching tolerance**, reused as the minimum resolvable move rather than invented for this spike.

**Seeds are pilot and discarded**: content 101, dynamics 103, selection 107 -- deliberately not P1's authoritative 17/23, so no number here can be pooled with or mistaken for a confirmatory measurement. 600 episodes per `r`.

---

## 3. Stage 0 -- the arm as built

Harness at `062d774289` / `1d72f60073`, unmodified.

| `r` | fidelity | `N_eff` | true count | cardinality | VERIDICAL | confidence |
|---|---|---|---|---|---|---|
| 0 | 0.931338 | 1.094055 | 1.0000 | 5 | 1.00 | 0.6001 |
| 1 | 0.931338 | 1.094055 | 1.0000 | 5 | 1.00 | 0.5985 |
| 2 | 0.931338 | 1.094055 | 1.0000 | 5 | 1.00 | 0.5965 |
| 4 | 0.931338 | 1.094055 | 1.0000 | 5 | 1.00 | 0.5995 |
| 8 | 0.931338 | 1.094055 | 1.0000 | 5 | 1.00 | 0.5981 |
| 16 | 0.931338 | 1.094055 | 1.0000 | 5 | 1.00 | 0.5974 |

**G1 FAIL** (rise `0.000000000`), G2 PASS, G3 PASS, G4 PASS. **GATE FAIL.**

Fidelity is not merely flat, it is *identical to nine decimal places at every replay count*, because `replay(mode='in_place')` incremented a retrieval-event counter and touched no content. The small confidence wobble (0.6001 -> 0.5974, non-monotone) is read-noise sampling over a bit-identical store, not an effect.

**The failure is the informative half of this spike.** Section 5 predicted the arm could be unreachable and that it would be "invisible until the results are in"; that is what the measurement found, and it is *not* the shape section 5 was watching for. Section 5 feared an `append`-only replay in which the count rises everywhere. The actual build satisfied the cardinality half of the healthy arm perfectly -- count flat, cardinality flat, regime intact, three of four gates green -- and failed the fidelity half absolutely. A contract review checking only that a `mode` argument exists would have passed it.

---

## 4. Stage 1 -- with H2's missing half closed

`reinstate()` added: one in-place event pattern-completes the trace toward the ancestor **the architecture itself believes in**, scaled by its own binding strength (`REINSTATE_GAIN = 0.25`). Store-only; no `GroundTruth` in the signature. Rationale, endogeneity argument, and the two deliberate non-behaviours are in the reconciliation note section 3.2.

| `r` | fidelity | `N_eff` | true count | cardinality | VERIDICAL | confidence | accuracy | signed err |
|---|---|---|---|---|---|---|---|---|
| 0 | 0.931338 | 1.094055 | 1.0000 | 5 | 1.00 | 0.6001 | 0.7700 | -0.1699 |
| 1 | 0.938055 | 1.094055 | 1.0000 | 5 | 1.00 | 0.5985 | 0.7733 | -0.1749 |
| 2 | 0.944006 | 1.094055 | 1.0000 | 5 | 1.00 | 0.5967 | 0.7750 | -0.1783 |
| 4 | 0.954521 | 1.094055 | 1.0000 | 5 | 1.00 | 0.6015 | 0.7750 | -0.1735 |
| 8 | 0.970071 | 1.094055 | 1.0000 | 5 | 1.00 | 0.5999 | 0.7783 | -0.1784 |
| 16 | 0.987346 | 1.094055 | 1.0000 | 5 | 1.00 | 0.5983 | 0.7667 | -0.1684 |

**G1 PASS** (rise +0.056008 against a +0.02 floor; non-decreasing; rho 1.0000). **G2 PASS** (drift exactly `0.00e+00`). **G3 PASS** (cardinality 5 throughout). **G4 PASS** (VERIDICAL 1.00 throughout). **GATE PASS.**

This is design section 8.2's healthy-replay row -- *fidelity up, count flat, `VERIDICAL / rehearsal`* -- reached in the architecture rather than asserted of it. The scorer-side true source count (requirement H4, used exactly as section 7.2 point 3 asks) is flat at 1.0000 alongside the estimate, so "count flat" is not an instrument artefact at this operating point.

### 4.1 How much of this was structural, stated plainly

Half of the Stage 1 gate is close to determined once the mechanism exists, and the driver's docstring says so up front rather than letting a reader infer otherwise:

- **G2 and G3 are near-structural.** `effective_source_count` reaches content only through `shared_ancestry_prob`, which reads `edge_target` and `edge_w` and never `content`; `reinstate()` writes `content` only. The `0.00e+00` drift is a *confirmation of a decoupling assertion*, not a discovery. It is measured because that assertion is worth failing loudly if it ever stops being true.
- **G1 under Stage 1 is near-structural too.** Pulling a trace toward its bound ancestor raises a cosine against the seed that ancestor carries.
- **The informative measurements are Stage 0's G1 failure (section 3) and S1 below.**

### 4.2 S1 -- the check that was genuinely uncertain

A mechanism that raised fidelity *unconditionally* would let P3's healthy arm pass in every ancestry condition, making the confirmatory grid uninterpretable -- the mirror of section 8.2's STOP row for the count. S1 asks whether the rise is ancestry-**mediated**.

| condition | fidelity `r=0` | fidelity `r=16` | rise |
|---|---|---|---|
| `VERIDICAL` | 0.931338 | 0.987346 | **+0.056008** |
| corrupted (decay `tau=2.5`) | 0.931338 | 0.933440 | **+0.002102** |

**Ratio 0.0375, against a preregistered ceiling of 0.5. S1 PASS, with 13x of margin.**

Reinstatement repairs when the architecture's ancestry pointer is intact and does almost nothing when the binding has decayed -- because the step is scaled by `edge_w`, the architecture's own confidence in that pointer. This is what distinguishes a reinstatement mechanism from a fidelity-vending machine, and it was not guaranteed by construction. Note also the two conditions share an identical `r=0` fidelity (0.931338), which is `degrade()`'s content-invariance (P1's C1) showing up as a consistency check.

### 4.3 S2 -- depth bound: directionally confirmed, and weaker than expected

| | `r=0` | `r=16` |
|---|---|---|
| gen-1 | 0.9320 | 1.0000 |
| gen-2 | 0.8681 | 0.9996 |

**S2 PASS**, but the margin at `r=16` is 0.0004, and the honest reading is that the effect nearly cancels. The prediction was that reinstatement inherits its ancestor's own error, so a deeper descendant should saturate lower. It does -- but in this measurement *every* member of the chain is rehearsed, so the gen-2 node is completing toward a gen-1 node that is itself converging on the seed. The bound is therefore not "the ancestor's fidelity" but "the ancestor's fidelity **at the time of reinstatement**", which is a moving target when the whole lineage is replayed. A grid that rehearses selectively (design section 2.5's `preferential` policy) would separate these; this spike does not.

### 4.4 S3 -- and the one finding that should change the grid

Confidence moved **-0.0018** and signed error **+0.0015** across the full replay range, with count flat and true count flat -- both at noise (600 episodes; accuracy's SE is ~0.017, and the accuracy column's wobble 0.7700 -> 0.7783 -> 0.7667 sits inside it).

So fidelity rose by 0.056 and **confidence did not follow**. That is not a null result about the architecture; it is a missing channel, and it is structural: `confidence(votes, p_est, n_eff)` has **no fidelity term**. Retrieval fidelity can reach confidence only by flipping a vote.

This matters for the grid because design section 8.1a predeclares the **fidelity route** as "confidence up, count flat, calibration IMPROVES" and distinguishes it from the **strength route** by calibration *direction* at flat count. In this architecture that route is not reachable as written -- a correct healthy-replay result will present as flat confidence and read as a null against a route that was never available.

The harness does have a healthy-improvement channel that reaches confidence, but it is a **different mechanism**: P1-R3's read-noise averaging (`read_vote(n_reads=...)` raising `p`, measured there as confidence +0.0845 at `N_eff` exactly 1.000). Section 8.1a currently folds content fidelity and retrieval reliability into one route. They are two, and only one of them is wired to confidence. Recommendation 5 in the reconciliation note states the fix; it is not applied here.

---

## 5. Disclosures

**Nothing was tuned after seeing numbers.** The criteria, thresholds, seeds, replay grid and `REINSTATE_GAIN = 0.25` were all fixed before Stage 0 ran; Stage 0 ran, then Stage 1 ran, and neither the harness nor the criteria were touched in between. `REINSTATE_GAIN` was chosen from first principles (a quarter of the remaining gap per event, scaled by binding strength), not fitted. There is no pre-adjustment/post-adjustment pair to report, because no adjustment was made.

**The two stages differ only in the harness.** The driver is byte-identical across them: it detects `hasattr(H, 'reinstate')` and records `harness_has_reinstate` in its payload. Stage 0 ran against `git show HEAD:scripts/provenance_genealogy_harness.py`.

**P1 regression -- byte-identical, and structurally so.** The harness is a landed dependency of the P1 assay, re-run before and after on content-seed 17 / dynamics-seed 23:

```text
MAIN M1 M2 M3 M4   PASS -> PASS      n_eff inflation 3.752641 -> 3.752641
R2  R3  R4  R7     PASS -> PASS      instrument floor 0.221454 -> 0.221454
C1                 PASS -> PASS      HEADLINE attributable -> attributable
full results payload: BYTE-IDENTICAL
```

The third consumer, `provenance_p1r5_retrieval_attribution_arm.py`, is also byte-identical (its `A5/A6/A8/A9 = false` are that arm's own pre-existing route findings, confirmed unchanged against the pristine harness, not regressions). This is structural rather than lucky: both pre-existing `in_place` call sites replay `trace_id = 0`, the world event, whose `edge_target` is `-1`, so ancestry-mediated reinstatement is a guaranteed no-op there.

**New harness primitives were checked directly** -- 18 assertions, all passing: `freeze()` refuses `add_world_event` and refuses `ambiguous_perception` at `alpha < 1` while allowing `alpha = 1`, and survives `copy()`; `replay(kind=...)` raises `NotImplementedError` for the two declared-gap kinds and `ValueError` for an unknown one; `reinstate()` has no `GroundTruth` in its signature, raises fidelity, and leaves `edge_w`, `N_eff` and cardinality exactly unchanged, no-opping on a seed and on a zero binding.

**Known limitation of the S1 comparator.** The corrupted condition is decay to `ABSENT` (binding -> 0), where reinstatement is expected to *do nothing*. It does not test the `FALSE_SPLIT` case, where a re-pointed edge should make fidelity **fall** -- a sharper prediction, and one the grid should check. Out of scope for a one-cell reachability spike.

---

## 6. What this does and does not license

- **Licensed:** proceeding to the P3 confirmatory grid design (section 4), which section 10 gated on this spike. The `complex (probe-gated)` precondition is discharged.
- **Not licensed:** treating any number here as evidence. Pilot seeds, one cell, 600 episodes, and the design requires discarded pilot seeds precisely so these cannot be pooled.
- **Not licensed:** treating the Stage 1 pass as evidence that `reinstate()` is the *right* reinstatement mechanism. It is *a* mechanism satisfying the design's stated requirement, with the ancestry-mediation property S1 checked for. Whether reconsolidation should also strengthen the binding is open (reconciliation recommendation 4).
- **Still owed before the grid:** H3, H5 and H8 (reconciliation section 4), plus the section 8.1a fidelity-route channel question raised in 4.4 above -- the last of which is a design decision, not a build task.

---

## 7. Epistemic boundary

- Nothing here is evidence about psychosis, and nothing here is claim evidence. This is a synthetic reachability probe of a harness capability, not a measurement of anything the harness would measure.
- The spike measures no ancestry corruption effect, no cardinality inflation and no confidence inflation, by design. It says nothing about whether recurrent reuse inflates evidential weight -- that is the grid's question, and this spike's only contribution is that the healthy-replay control against which it would be read is now reachable by construction rather than by assumption.
- The result is about the **stored-tag** route only (P1-R5, predeclared).
- The rodent sources behind P3-R2 (E20 Kovacs 2016, E30 Rule & O'Leary 2022) are design constraints that motivate the healthy-replay arm's existence. They supply no fidelity or cardinality readout and none is claimed from them; the direction of travel is one-way.
