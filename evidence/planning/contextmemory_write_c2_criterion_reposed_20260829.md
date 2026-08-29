# ContextMemory write-path C2 content-discrimination criterion: scoping spike

**Status: FINDINGS RECORDED. The substrate_queue entry's `implementation_hint` has been
amended (narrow structural edit) to point future work at this document. No claims.yaml
change, no status flip -- `contextmemory-write-path-addressing-degeneracy` stays
`implemented_pending_validation`, unchanged by this spike.**

**Chip:** `chip-20260829-contextmemory-c2-criterion-repose`
**Environment:** REE_assembly `0c3488a03c`, ree-v3 `30d5a6bc`
**Trigger:** two independent loss designs (MoE importance loss; gumbel_learned pairwise-
diversity loss, V3-EXQ-956, confirmed autopsy `failure_autopsy_V3-EXQ-956_2026-08-29.json`)
have now both failed the entry's C2 content-discrimination criterion. Per CLAUDE.md's
held-out-check framing: two designs failing one criterion is the mis-posed-criterion
signature, worth checking before a third design is built.

## Answer, up front

**The criterion is mis-posed as currently operationalized -- not because the numeric bar
is arithmetically unreachable (an oracle trivially clears it), but because the INSTRUMENT
(2-cluster occupied-slot-SET Jaccard, tiny within-cluster jitter, n=5 seeds) is a
known-aliasing, near-binary statistic that cannot distinguish learned content
discrimination from random luck of decision-boundary placement.** This is not a new
finding invented for this spike -- it is the *same* aliasing failure mode this codebase
already documented on 2026-08-19, for a different arm, with an explicit warning
("select a DV with a deterministic signal ... before queuing either") that was not
applied when V3-EXQ-956's C2 criterion was registered.

Consequently: the two failed designs are **not strong evidence that content-conditioned
write-addressing is hard or wrong** -- they are weak-to-uninterpretable evidence, because
the instrument used to grade them has a substantial false-negative *and* false-positive
rate at n=5. A third loss design should not be built to satisfy the existing C2 as
written; either the instrument should be replaced, or (see "Relevance to SD-017/ARC-045/
MECH-166" below) the property may not need to be gated on this isolated component at all.

---

## 1. What does the "<=0.15" bar correspond to? Oracle / random / current, computed

The probe (`v3_exq_956...py::_probe_stream`/`_jaccard`, reusing
`test_contextmemory_write_address_selection.py::_stream`/`_jaccard`) draws `n=1500`
synthetic states (750 per cluster) from two Gaussian blobs (`base ~ N(0, 0.078^2)` per
cluster, `jitter=0.0078` within-cluster) in a 64-dim latent, feeds each through
`ContextMemory.write()` in eval mode (deterministic argmax on `write_addr_tagger`'s
scores, no Gumbel noise), and records which of 16 slots each write touched. Jaccard is
computed on the two clusters' occupied-slot **sets** (not counts):
`J = |A n B| / |A u B|`. The registered criterion (module docstring,
`v3_exq_956...py` lines 146-161) is `mean_jaccard(TRAINED) <= mean_jaccard(UNTRAINED) -
0.25` -- **a relative margin, not a fixed absolute bar**. "<=0.15" is that margin's
instantiation for this one run's empirical untrained baseline (0.400 - 0.25 = 0.150); a
different run's untrained baseline would yield a different absolute number. This matters:
the chip brief's framing ("is <=0.15 the right bar") is really asking about the
**instrument**, since the number itself is derived, not fixed.

**(a) Perfect content-addressed oracle** (e.g. cluster 0 -> slots {0-7}, cluster 1 ->
slots {8-15}, deterministically, zero leakage): `A n B = {}`, so `J = 0` on every seed,
every run, always. **The bar (0 or 0.15) is trivially reachable by construction** -- this
rules out "arithmetically unreachable" in the strict sense (unlike V3-EXQ-936a's C2 bar
or V3-EXQ-862b's DV, where the cited prior instances of this defect shape made the floor
itself impossible for *any* input).

**(b) Uniformly random write, content-blind** (slot chosen independently of state, no
memory of query at all): with 750 independent uniform draws over 16 slots,
`P(a given slot never drawn) = (15/16)^750 ~= 5e-22`, so each cluster's occupied set is
*all 16 slots* with near-certainty by the coupon-collector bound. `A = B = {0..15}`,
`J = 1.0`. **Fully content-blind-by-spreading also fails the bar**, appropriately -- this
is the "high-entropy but content-blind" failure mode and the instrument correctly flags
it as bad.

**(c) The current write mechanism, computed exactly from the V3-EXQ-956 manifest**
(`REE_assembly/evidence/experiments/v3_exq_956_contextmemory_write_gumbel_learned_
validation_20260829T014524Z_v3.json`, `arm_results`): neither GUMBEL_UNTRAINED nor
GUMBEL_TRAINED behaves like (a) or (b). Every single cell's **per-cluster occupied set
has cardinality 1-3** (out of a possible 16), despite 750 draws per cluster:

| seed | UNTRAINED occ(0) | occ(1) | J | | TRAINED occ(0) | occ(1) | J |
|---|---|---|---|---|---|---|---|
| A | {3} | {14} | 0.000 | | {4} | {4} | 1.000 |
| B | {4} | {4} | 1.000 | | {6,10} | {10} | 0.500 |
| C | {14} | {14} | 1.000 | | {7} | {2,7,8} | 0.333 |
| D | {8} | {7} | 0.000 | | {0} | {0,2} | 0.500 |
| E | {4} | {3} | 0.000 | | {9} | {9} | 1.000 |

i.e. **the deterministic eval-mode tagger maps essentially all 750 draws of a given
cluster to a single dominant slot** (jitter=0.0078 is far too small, relative to
whatever decision-boundary granularity a smooth-ish tagger function has, to make the
tagger visit more than 1-3 slots for one cluster). This is a *third* regime, distinct
from both (a) and (b): not a clean partition, and not content-blind saturation --
**a near-degenerate point-evaluation** of the tagger at (functionally) one representative
input per cluster, repeated 750 times.

## 2. Is 2-cluster probe Jaccard sensitive to the property being tested? No -- and this codebase already found that once

With per-cluster occupied sets of cardinality 1 (the overwhelming majority of observed
cells: 10/10 for UNTRAINED, 6/10 for TRAINED), Jaccard can only take values from a tiny
set of low-denominator fractions determined by whether the SAME slot(s) happen to
recur -- effectively **one bit of information per seed** ("did the fixed decision
function place these two specific test points on the same side of a boundary, or not").
This is precisely a **near-Bernoulli aliasing** failure, not a graded content-
discrimination readout, and it produces the exact bimodal signature seen twice now:

- **2026-08-19** (`contextmemory_write_selection_comparison_20260819.md` Section 6,
  pre-dating gumbel_learned by 10 days): the *landed conscience-bias* arm's period-16
  round-robin cycle "aliases against a 2-cluster alternation -- giving Jaccard exactly
  0.0 on 3/5 seeds and exactly 1.0 on the other 2, **a bimodal artifact whose mean
  (0.400) looks moderate**." That document's own conclusion: *"select a DV with a
  deterministic signal (occupancy, self-repeat, round-robin index), before queuing
  either [chip]."*
- **2026-08-29** (this spike, GUMBEL_UNTRAINED): mean 0.400, per-seed
  `[0.0, 1.0, 1.0, 0.0, 0.0]` -- **the identical bimodal pattern, the identical mean**,
  from a completely different mechanism (an untrained random-weight MLP tagger, not a
  usage counter). Two structurally unrelated mechanisms alias to the same signature
  because the aliasing is a property of the **instrument** (tiny-cardinality occupied
  sets under a 2-cluster set-overlap statistic), not of either mechanism.

The 2026-08-19 warning was explicit and on-the-record before V3-EXQ-956 was authored; its
recommended DV swap was not carried forward into the gumbel_learned C2 criterion. This
spike is, in effect, that warning firing a second time.

**Quantified consequence -- the instrument has a real false-positive rate.** Empirically,
an *untrained* (unlearned, randomly-initialized) tagger achieved a clean `J=0` (perfect-
looking separation) on 3 of 5 seeds, by chance alone -- "a generic property of applying
any smooth, if random, function to two distant point clouds," per the driver's own
docstring. A tagger that has learned nothing about content has a non-trivial chance of
*passing* `mean_jaccard <= 0.15` outright (needs ~4-5 of 5 seeds at J=0; empirically
observed base rate ~0.5-0.6 per seed gives roughly `0.6^5 ~= 0.08` for an all-5 sweep,
more if a small nonzero contribution is tolerated). **A criterion that an untrained
baseline could pass ~8% of the time by pure luck is not a safe gate for "this mechanism
learned to content-discriminate."**

**A second, exact, non-p-value observation the mean-based test buries:** of the 5
TRAINED seeds, **0 achieved a clean `J=0`** (best was 0.333); of the 5 UNTRAINED seeds,
**3 achieved `J=0`**. By exact hypergeometric test (10 cells, 3 "successes" total, split
5/5), `P(untrained group gets >=3 of the 3 successes | random split) = 0.083`. This is a
*different*, looser statistic than the autopsy's registered mean-margin test (which the
autopsy's own red team already correctly downgraded to "suggestive, p~0.24-0.28, not
established") -- it does not override that adjudication, which stands. It is offered here
only as corroborating texture for *why* the instrument is unreliable: even the more
favorable framing of the same data is weak.

## 3. What n would a decisive read need?

**For the existing (2-cluster, tiny-jitter, Jaccard-on-occupied-sets) design specifically:**
modeling each seed's outcome as approximately Bernoulli(p) (achieves clean separation or
not -- an approximation, since the true distribution has some intermediate mass, but the
observed data is close to this), a standard two-proportion power calculation
(alpha=0.05, power=0.80) to detect a shift from an untrained "lucky boundary" baseline
`p0` to a trained "learned separation" rate `p1`:

| p0 (baseline luck) | p1 (target) | n per arm |
|---|---|---|
| 0.50 | 0.90 | ~17 |
| 0.50 | 0.80 | ~36 |
| 0.60 | 0.95 | ~18 |
| 0.55 | 0.75 | ~85 |

So roughly **20-90 seeds per arm**, not 5, would be needed for a decisive read *of this
exact statistic* -- an order of magnitude more compute than V3-EXQ-956 spent, for a
statistic that (per Section 2) still would not distinguish "genuinely content-
discriminating" from "got lucky/unlucky many times over" in any principled way, because
it only ever probes ONE fixed pair of near-point test inputs.

**More seeds do not fix the underlying mis-posedness.** They only shrink the estimation
noise around a target quantity (the probability THIS mechanism's decision boundary
separates THESE TWO specific centroids) that was never the right thing to estimate.
**Recommended redesign instead of scaling n on the current design:** replace the
2-set-Jaccard DV with a statistic that uses the full per-draw assignment information
already computed by the probe rather than collapsing it to set membership -- e.g. mutual
information (or normalized/adjusted mutual information) between (assigned slot) and
(true content-cluster label) over all 1500 draws, optionally extended to K>=4-8 clusters
so the statistic aggregates over many cluster pairs instead of one. This is graded (not
near-binary), degrades gracefully (0 for content-blind, 1 for a perfect partition,
intermediate for partial discrimination), and does not alias against periodic/degenerate
selection the way set-Jaccard does -- because it is sensitive to the full **contingency
table**, not just which cells are nonzero. Under a graded statistic, n=5 seeds is far
more likely to already be adequate (each seed contributes a continuous estimate, not a
coin flip), though this spike does not attempt a full power calculation for a redesigned
instrument that does not exist yet -- that is follow-on `/queue-experiment` work, not
this spike's deliverable.

## 4. Relevance to SD-017 / ARC-045 / MECH-166 -- does the claim actually need this property from the isolated write path?

Reading the three claims this substrate entry unblocks:

- **SD-017**: "Without these offline [sleep] phases, hippocampal attribution mapping
  cannot converge and context representations remain globally undifferentiated."
- **ARC-045**: "Without bidirectional [sleep] flow, context representations remain
  globally undifferentiated despite locally coherent online encoding."
- **MECH-166**: "Slot structure must be consolidated during an SWS-analog phase before
  slot-filling during a REM-analog phase can yield reliable attribution signal" --
  slot-formation and slot-filling "cannot be co-computed in a single online pass."

All three claims are about differentiation **emerging from sleep consolidation**, and
MECH-166 explicitly predicts that a single online (pre-sleep) pass should *not* yet
produce well-organized slot structure. What actually blocked their retest (V3-EXQ-436e,
436f -- see this entry's `failure_record`) was **occupancy**, not addressing quality:
`"n_occupied_slots = 1 of 16 in BOTH arms ... despite 2,837-4,903 ContextMemory.write()
calls"` -- i.e. only one slot was EVER used, full stop, which makes it structurally
impossible for any downstream consolidation process to show differentiation (there is
nothing to differentiate between). All three implemented mechanisms (BIAS, REFRACTORY,
gumbel_learned) now clear this bar decisively (16/16, 6/3/3/3/9, and 16/16 slots
respectively) -- the precondition that actually blocked 436e/436f is already resolved.

**Demanding that the isolated write mechanism, probed with zero sleep/consolidation
machinery engaged, already behave as a near-perfect content-addressed oracle (C2) is a
stronger and differently-targeted property than what the downstream claims need**, and
arguably in tension with MECH-166's own prediction that pre-consolidation slot structure
should *not* yet be well-organized. What SD-017/ARC-045/MECH-166's retest actually needs
from the write path is: (i) non-degenerate occupancy (met), and (ii) enough raw material
(multiple slots genuinely in use, with *some* relationship to content, not necessarily
already fully partitioned) for the SWS/REM consolidation machinery to operate on and for
the retest's own DV (differentiation, measured end-to-end under the real SD-016 harness)
to have room to move. Whether consolidation *actually* produces differentiation from
that raw material is precisely the retest's own open question -- gating on the answer to
that question *before* running the retest, via an isolated pre-sleep unit probe, tests
the wrong stage of the pipeline.

## Recommendation

1. **Do not build a third write-addressing loss design against the current C2 as
   written.** Two designs failing an aliasing-prone instrument is not evidence the
   underlying property is hard to achieve; it is evidence the instrument should not be
   trusted as a gate.
2. **For the SD-017/ARC-045/MECH-166 retest specifically**: proceed on the occupancy
   floor already met (any of the three mechanisms), and treat content-discrimination as
   a **descriptive** readout inside that end-to-end retest (using a non-aliasing DV --
   occupancy, self-repeat, round-robin index, or a contingency-table statistic -- never
   2-cluster set-Jaccard at n=5), not as a precondition gate on the isolated write
   mechanism. This is a disposition call for governance/a human, not something this
   spike unilaterally applies -- `unblocks_claims` in the substrate entry is left
   unchanged.
3. **If content-discrimination is still wanted as a standalone, gating property of the
   write mechanism** (independent of the sleep retest), redesign the instrument first:
   replace 2-cluster occupied-SET Jaccard with a contingency-table statistic (mutual
   information / normalized or adjusted mutual information between assigned slot and
   true content label) computed over the existing per-draw data, ideally extended to
   K>=4-8 clusters. This is `/queue-experiment` follow-on work, not performed by this
   spike.
4. **Either way, this entry's own failure_record and implementation_note already
   correctly state "STATUS REMAINS implemented_pending_validation"** -- nothing here
   changes that disposition; it only redirects what "validation" should measure next.

## What this spike did NOT do

- Did not build or run a new loss design or a redesigned probe -- this is discovery debt
  (`complex (probe-gated)`), not a build.
- Did not touch `claims.yaml`, `unblocks_claims`, or `status` on the substrate entry.
- Did not resolve H1-H4 from the V3-EXQ-956 autopsy's fanout -- those hypotheses are
  about the *loss objective*; this spike is about the *measurement instrument* used to
  judge any loss objective's output, and is orthogonal to (compatible with) that fanout.
