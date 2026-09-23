# Failure autopsy -- V3-EXQ-1043b (MECH-537, communication-subspace routing)

- **Run**: `v3_exq_1043b_mech537_communication_subspace_randrank_20260922T204547Z_v3`
- **Queue id**: V3-EXQ-1043b (`supersedes: V3-EXQ-1043a`)
- **Purpose**: `diagnostic` -- so this autopsy is owed on trigger 2 regardless of outcome
- **Manifest outcome**: `FAIL`, `evidence_direction: mixed`, label `routing_signature_incomplete_undetermined`
- **Machine**: ree-worker-3, `linux-x86_64-py3.10-torch2.12.0+cpu`, 65,650 s (18.2 h), 6 seeds (42-47)
- **Generated**: 2026-09-23T17:09:35Z
- **Autopsy verdict**: the headline label UNDERSTATES the run. One pre-registered hypothesis
  (H2-no-orientation) is decisively eliminated; the two load-bearing FAILs are a power limit the
  pre-registration itself predicted and a conjunct that is not reproducible on a fixed subspace.

---

## 1. Facts

**Dry-run gate (Step 2a).** `check_dry_run_citations.py --family v3_exq_1043` -> 0 dry / 3 real
(1043, 1043a, 1043b). Manifest `dry_run: false`, run_id is not of `_dry_` shape. No citation in this
artifact rests on a smoke. `dry_run_checked: true`, `excluded_dry_run_ids: []`.

**Recording provenance -- complete, with one stale pointer worth naming.** The always-record core is
present: `recording_schema`, `substrate_hash` (`d2977a14f3cb...`), `machine` / `machine_class`,
`elapsed_seconds`, full `config`, explicit `seeds`. But `substrate_stable_across_run` is **`false`**:
`substrate_identity` records `drifted_since_resolved: true`, `commit_describes_recorded_hash: false`
and `lag_seconds: 57098`, because the manifest was stamped 15.9 h after the cells resolved and the
worker's checkout had moved on (`hash_on_disk_at_stamp: 8aaf2224...`). **This does not touch the
run's validity**: `substrate_stability_detail.per_cell_hashes_disagree` is `false` and
`distinct_cell_substrate_hashes` contains exactly one hash, so every cell ran on one substrate. What
is stale is the PROVENANCE POINTER (the recorded commit does not describe the recorded hash), which
matters for anyone later trying to reconstruct the exact tree. Recorded rather than glossed, because
this autopsy leans on `substrate_hash` when it says a ceiling reading would have been falsifiable.

**All readiness gates GREEN (`gate_green: true`), including an explicit positive control:**

| gate | measured | threshold | met |
|---|---|---|---|
| `source_adequacy_ws250_full` (worst seed) | 0.9210 | >= 0.80 | yes |
| `source_elevation_over_strongest_trivial` (worst seed) | 0.3532 | >= 0.20 | yes |
| `rrr_heldout_r2_supra_floor` (worst seed) | 0.9968 | >= 0.50 | yes |
| `randrank_reference_nondegenerate_seed_count` | 6 of 6 | >= 1 | yes |

`non_degenerate: true`, `degeneracy_reason: ""`, all six entries of
`interpretation.criteria_non_degenerate` true, `n_seeds_nondegenerate: 6`,
`n_seeds_competent: 5`. So the run is NOT a precondition-unmet or vacuous-pass case: the
instrument was ready and the criteria could move.

**Scored criteria.**

| criterion | load-bearing | result | numbers |
|---|---|---|---|
| C1 target drops inside comm subspace | no (rank-confounded phenotype) | **PASS** 6/6 | mean 0.3792 vs floor 0.05 |
| C2 PRIMARY -- declared absolute-difference CI | **yes** | **FAIL** | 95% CI `[-0.01547, +0.07370]`, includes 0 AND 0.05 |
| C2 RANK CO-PRIMARY -- percentile vs random same-rank reference | **yes** | **PASS** | Fisher p = 2.19e-4 |
| C3 complement retains decodability | no (near-automatic by dimensionality) | PASS 6/6 | mean 0.0017 vs 0.05 upper |
| C4a coupling below matched null | no (`scored_as_conjunct: false`, retention-confounded) | PASS 6/6 | mean margin 0.9492 vs 0.15 |
| C4b coupling below absolute in-run ceiling | **yes** | **FAIL** 3/6 (needs 4) | mean 1.1368 vs ceiling 1.1495 |
| C5 single-subspace premise | **yes** | **PASS** | 0.6099 vs 0.2164 required (chance 0.0664) |

**The combination rule's path.** C5 holds, so the run is NOT routed away to MECH-547 / MECH-555.
The equivalence branch is unreachable (`n_seeds_equivalent_within_band: 0`; full sender 0.92-0.95
against comm 0.50-0.60). The confirming conjunction C1 AND C2 AND C3 AND C4 fails on C2-primary and
C4b. The dedicated falsification branch requires the C2 contrast to be genuinely non-positive
(mean <= 0 and a seed majority <= 0) and it is not (mean +0.0291, 4 of 6 seeds positive). So the
driver lands on `undetermined (mixed)`. **That is the correct application of the rule.**

---

## 2. What the headline label hides -- and the pre-registration said so in advance

The pre-registration
[`v3_exq_1043b_prereg_rank_coprimary_20260922.md`](v3_exq_1043b_prereg_rank_coprimary_20260922.md)
(REE_assembly `927cf907e49`, written and committed BEFORE the run) says, in its Finding 5:

> this document's own most-likely outcome -- H2 decisively falsified by the rank co-primary --
> **coexists with `outcome: FAIL`, `evidence_direction: mixed`,
> `routing_signature_incomplete_undetermined`**, byte-identical to what V3-EXQ-1043 landed. [...]
> **A reader adjudicating this run must read `interpretation.primary_agreement`, not
> `evidence_direction` alone.**

`interpretation.primary_agreement` reads:

```
label:                              orientation_contrast_not_positive_rank_significant_DISAGREEMENT_split
declared_primary_ci:                [-0.01547, +0.07370]   (excludes neither 0 nor 0.05)
rank_coprimary_significant_set_all:       true
rank_coprimary_significant_set_competent: true
primaries_agree:                    false
sets_disagree:                      false
rests_on_few_seeds_fisher_not_simes: false
split_declared:                     true
```

That is exactly the last row of the prereg's section-8 grid, with the `_split` suffix appended
mechanically. The driver applied the pre-registered grid correctly. The gap is only that the
top-level `interpretation.label` and `hypothesis_verdict` ("MECH-537 UNDETERMINED [...] no verdict
is claimed") carry the legacy option-A wording, so a consumer reading them -- or reading
`evidence_direction` alone -- sees no movement across three runs of this lineage while a decisive
adjudication of one registered leg sits one field away. **This is a reporting-surface limitation,
not an instrument defect, and the prereg declared it in advance rather than repairing it, because
repairing it would have meant loosening C4 to let a favoured statistic drive `evidence_direction`.**

---

## 3. Adjudication of the three pre-registered legs

The frozen-ledger question is `mech537_communication_subspace_orientation` (registered
2026-09-17, `initial_frozen_count: 3`, no `growth_restriction` -- the Step 9b growth-restriction
check therefore clears with nothing to do).

### H2-no-orientation -> **ELIMINATED**

Declared null, verbatim from the prereg: *"the observed C2 sits inside the reference null"*,
adjudicated by the RANK CO-PRIMARY, and *"a significant Fisher result falsifies H2's declared
null."* Measured:

| statistic | SET-ALL (n=6) | SET-COMPETENT (n=5) |
|---|---|---|
| Fisher | p = 2.19e-4 | p = 6.86e-5 |
| Simes (robustness) | p = 0.0060 | p = 0.0050 |
| leave-one-out Fisher (drop smallest p) | p = 0.0099 | p = 0.0038 |

All six clear alpha = 0.05. The two sets agree (`sets_disagree: false`), and the result survives
removal of the single most influential seed on both sets, so it does not rest on one extreme seed
(`rests_on_few_seeds_fisher_not_simes: false`). Elimination bar: `control_passed: true` (the
readiness positive controls above), `non_degenerate: true`, `met_elimination_bar: true`.

**Honest qualifier, carried into the ledger basis.** The per-seed percentiles are
`[0.0030, 0.1059, 0.0460, 0.8082, 0.7642, 0.0010]` -- 3 of 6 clear alpha individually, 4 of 6 are
positive, and 2 sit on the wrong side. What is eliminated is H2 **as stated** ("the fitted
communication subspace is **not meaningfully different** from a random subspace of the same rank at
this interface"): in at least some encoders it demonstrably is. The run does NOT establish that
orientation is uniform across encoders, and the `_split` suffix is the pre-registered record of
exactly that.

### H1-small-but-real -> **stays ALIVE** (not adjudicated)

Declared null: *"the CI excludes 0.05 (H1 falsified, not rescued)"*. The CI is
`[-0.01547, +0.07370]` and includes 0.05, so the null is not met and H1 is not falsified; it
includes 0 as well, so H1 is not confirmed either. The prereg predicted this before the run
("IT IS EXPECTED TO COME BACK UNDECIDED at n = 6, because the binding variance is the CROSS-SEED
sd ~0.038 rather than the draw noise this run removes") and instructed that it be reported as a
non-adjudication "with no upgrade". It is.

> **Corrected by the Step 7c red-team pass, and the correction changes a routing decision.** An
> earlier draft of this autopsy argued that H1 explains the two negative seeds "by chance": under one
> normal population with the run's own mean and sd, P(a seed lands negative) = 0.247, so
> P(>= 2 negatives) = 0.458. That arithmetic is right but the inference was wrong, and it was doing
> real work -- it was the stated reason for NOT recording an H-other event.
>
> The per-seed contrasts are **precisely measured**. Combining the reference-mean error
> (`sd_total`/sqrt(1000) = 0.0008) with the decoder-refit error (`sd_decoder_only`/sqrt(8) =
> 0.0020-0.0029) gives a per-seed measurement SE of **0.0021-0.0030**, against a cross-seed sd of
> **0.0425** -- a ratio of ~14. Seeds 45 and 46, at -0.0286 and -0.0166, therefore sit **8-12
> measurement-SE below zero**. They are real per-encoder properties, not noise. Under H1 *as
> originally registered* -- "consistently-positive", "every per-seed value positive" -- the
> probability of even one such seed is negligible.
>
> "By chance" is true only under a **random-effects** reading of H1 (true per-encoder effect drawn
> from N(0.029, 0.042^2)). But that reading is observationally identical, on every quantity this
> design records, to the new leg H4. So the split does NOT show that H1 already covered the data; it
> shows the frozen partition had no leg for a per-encoder mixture. **Mode D therefore FIRES** -- see
> section 6.

### H3-no-low-rank-bottleneck -> **stays ALIVE** (not adjudicated)

Declared null: *"C2 is flat in rank"*, adjudicated by the recorded rank ladder (C2 at the
parsimonious rank vs at rank 32). Measured **within this run** (like-for-like, both the single-fit
statistic):

| | seed42 | seed43 | seed44 | seed45 | seed46 | seed47 | mean |
|---|---|---|---|---|---|---|---|
| C2 @ selected rank 32 | 0.0615 | 0.0476 | 0.0219 | 0.0355 | 0.0176 | 0.0649 | 0.0415 |
| C2 @ parsimonious rank (9-11) | 0.0386 | 0.0573 | 0.0468 | -0.0245 | -0.0028 | 0.0537 | 0.0282 |
| paired diff | -0.0228 | +0.0097 | +0.0249 | -0.0600 | -0.0204 | -0.0112 | **-0.0133** |

Paired t = -1.108 (df 5, t_crit 2.571) -- **not distinguishable from zero**. So reading at the
parsimonious rank did NOT raise C2: rank is not what was hiding the orientation signal. There is
no pre-registered decision threshold for "flat", so this is recorded as a measurement, not scored
as an elimination, and H3 stays alive.

> **NOT "sign reversed" -- unresolvable. Corrected by the red-team pass.** An earlier draft read
> 1043a's opposite-sign value (+0.0155) as a reversal, qualified only by 1043a's red readiness. The
> sharper objection is that neither number is resolvable at all: the **rank-32 arm is a single draw
> with no reference distribution** in either run, and the 1043a -> 1043b replicate on **bit-identical
> encoders** (`agreements.ws250_full` reproduces to full float precision on 6/6 seeds) shows that arm
> moving by sd **0.025 per seed from decoder noise alone** -- comparable to the entire effect. Each
> run's H3 mean is ~1 SE from zero (1043a SE 0.017, 1043b SE 0.012). So the two runs are two draws
> from the same noise. **1043a's inherited ledger basis ("declared null NOT met: 0.0345 vs 0.0500")
> was itself an over-read of that noise and is corrected in this edit.** A successor must give the
> rank-32 arm its own reference distribution before H3 can be adjudicated at all.

**H3's structural premise is independently re-confirmed, and it cuts against H3's own conclusion.**
`rrr_rank_at_ladder_ceiling: true` and `selected_rank: 32` on 6 of 6 seeds, and
`rrr_heldout_r2_by_rank` is already 0.981 at rank 1 rising to 0.997 -- so z_world really is an
almost perfectly linear readout of world_state at low rank, exactly as H3 asserts. But the rank
co-primary is significant **at the parsimonious rank** (9-11 of 146 live sender dims), which means
the low-rank subspace IS oriented. H3's substantive claim -- that there is no low-rank channel to
be routed through -- is therefore weakened by this run without being eliminated by its declared
test.

> **The surviving set is coherent, and worth stating because it looks incoherent at first glance.**
> Eliminating H2 (there IS orientation) while H3's structural premise stands (z_world is a near-linear
> readout of world_state at any rank >= 8, so nothing is bottlenecked) is not a contradiction -- it is
> MECH-537's own story. The claim's registered text says the phenotype arises "with no information
> having been destroyed", and C3 measures exactly that and passes 6/6 (deleting the communication
> subspace costs the full sender 0.0017). A routing failure is a claim about what the consumer READS,
> not about information being lost upstream. So "no bottleneck" and "an oriented consumer-facing
> subspace" are the two halves of the same hypothesis, not rivals. What H3 additionally asserts --
> that the routing question is therefore *not instantiated at all* at this interface -- is the part
> the significant rank co-primary AT the parsimonious rank weakens.

---

## 4. The C4b ceiling -- discharging the item the prereg left owed

The prereg's Finding 5 records the C4b ceiling rule's unresolved weakness (1043a red-team M2, "the
effective per-unit bar rising toward 1.0 as F approaches I") as **"OWED to governance / a successor
autopsy"**. This is that successor autopsy, so it is discharged here rather than deferred again.

**(a) M2's degenerate regime did not obtain in this run.** The ceiling is the arithmetic midpoint of
a per-seed jacobian-aligned floor `F` (the rank-r subspace the encoder is most sensitive to) and an
isotropic reference `I`. M2 worried that as `F -> I` the bar becomes trivially passable. Measured
`F/I` per seed is `[0.533, 0.415, 0.420, 0.402, 0.410, 0.499]` and
`anchor_headroom_frac` is 0.47-0.60 on every seed, with `n_seeds_unreachable_anchor: 0`. There is
substantial headroom throughout; the degenerate regime is not present, and the resulting effective
per-unit bar sits at 0.70-0.77 of isotropic, not near 1.0. **M2 is real in principle and inert
here.**

**(b) The decisive problem is that C4b's per-seed verdict is NOT REPRODUCIBLE on the same subspace.**
This is the strongest form of the finding and it needs no re-weighting of the rule. V3-EXQ-1043a and
V3-EXQ-1043b ran on **bit-identical encoders** -- `config` matches field for field and
`agreements.ws250_full` reproduces to full float precision on all 6 seeds. On **seeds 43 and 44 the
parsimonious rank is also identical** across the two runs (11 and 10), and the RRR fit is
deterministic, so those two seeds are scoring *the same communication subspace twice*. The C4b probe
nonetheless returned:

| seed (same subspace) | 1043a measured | 1043b measured | move | 1043a verdict | 1043b verdict |
|---|---|---|---|---|---|
| 43 | 1.1633 | 0.9487 | **-0.215** | fail | **pass** |
| 44 | 1.1770 | 1.1264 | -0.051 | fail | **pass** |

The anchors moved too (`F`: 0.670 -> 0.631 and 0.646 -> 0.736; `I`: 1.531 -> 1.520 and 1.515 ->
1.753). A move of 0.215 is roughly half the entire `F`-to-`I` range the ceiling interpolates across.
The probe samples 32 Jacobian states (`pre_registered.n_jacobian_states`) out of
`config.n_sensitivity_states: 64` and is evidently unseeded, so this is replicate noise in the
instrument, not a change in the substrate. **A criterion whose per-seed pass/fail flips on a re-run
against the identical subspace cannot carry a conjunct**, and C4b's 3-of-6 is therefore close to a
coin flip in the literal sense.

**(c) Consistent with (b), the bar also happens to sit where the data sit.** The measurement's
position along `F -> I`, per seed, is `[0.655, 0.357, 0.384, 0.665, 0.321, 0.584]`, mean **0.494**,
while the midpoint rule places the bar at 0.500. Recomputing under alternative interpolation weights
gives 0/6 at `F` or `F + 0.25(I-F)`, 3/6 at the arithmetic midpoint and at the geometric mean, and
6/6 at `F + 0.75(I-F)` or at `I` alone.

> **Two cautions on (c), both raised by the red-team pass and both accepted.** First, recomputing a
> pre-registered criterion under five alternative rules *after seeing the numbers that fail it* is
> the soft form of exactly the re-anchoring move the pre-registration exists to refuse. It is kept
> only as a sensitivity note, and (b) -- which touches no threshold -- is what the routing rests on.
> Second, **"unanchored" was the wrong word** and is withdrawn: `criteria[C4b].ceiling_anchor` is
> `measured_in_run`, and anchoring the ceiling from a measured reference was precisely the prior
> autopsy's required change, correctly implemented. What is unjustified is narrower -- the choice of
> *interpolation weight* (why the arithmetic midpoint of `F` and `I`, rather than any other point
> between them). The earlier phrasing borrowed the 1043 autopsy's description of the OLD hand-set
> 0.5 constant and does not apply to this ceiling.

**So C4's FAIL carries almost no evidential weight in either direction**, and MECH-537's registered
confirming conjunction currently turns on it.

Note also the asymmetry the run already records: C4a, which scores the same coupling against a
properly rank-AND-support-matched random-subspace null, passes 6 of 6 with a mean margin of 0.949
(null ratio ~2.0 against a measured ~1.14). The conjunct that fails is the absolute one; the
matched-null one is decisive and is excluded as retention-confounded.

---

## 5. Four-layer diagnosis and failure location

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | The claim could express itself (all readiness green, C1 phenotype at 0.379, C5 premise held) and one registered rival was eliminated in its favour. NOT a weakening. |
| Biological reference | **clear** | Cortical communication subspace: Semedo et al. 2019 (V1->V2), Binish 2026 (human PFC->M1). Lit entries exist -- `evidence/literature/targeted_review_mutual_legibility_communication_subspaces/`. Not a formal-definition import: cross-validated RRR to the actual consumer input tensor is the same instrument the neurophysiology uses. No `/lit-pull` commission owed. |
| Prerequisites | **present** | Source adequacy 0.921, elevation over the strongest trivial predictor 0.353, RRR held-out R2 0.997, reference non-degenerate 6/6. |
| Implementation | **complete** | The prior autopsy's required change ("ANCHOR C4b's ABSOLUTE 0.5 CEILING from a measured reference") was implemented; the 1000-draw reference and the Fisher co-primary were built to the pre-registration. |
| Environment | **adequate** | The interface under test is instantiated and exercised. |
| Measurement | **under-instrumented** | THREE debts, the middle one decisive: (i) n = 6 cannot settle the magnitude CI (sem 0.0173 against a 0.05 floor) -- predicted pre-run; (ii) **C4b is not reproducible** -- on two seeds scoring a bit-identical encoder at an identical parsimonious rank, its verdict flipped between 1043a and 1043b (section 4b); (iii) H3's declared test is unresolvable -- the rank-32 arm is a single draw whose replicate noise matches the effect. |
| Integration | **coupled and exercised** | Not inert: the instrument drove the mechanism and the criteria moved. |
| Scale / capacity | **likely insufficient** | For a quantity with genuine cross-encoder variance, n = 6 is the binding limit. |

**Failure location (GOV-FAILLOC-1).**

- **MECHANISM FAILED -- not established.** Implementation reads `complete`, but the mechanism did not
  fail: the one rank-matched discrimination criterion PASSED and eliminated H2.
- **MEASURES -- partial (this is the binding bucket).** Measurement reads `under-instrumented` on
  both counts above.
- **ENVIRONMENT FAILED -- not established.** Environment adequate; nothing points here.
- **REE FAILED -- false.** Requires all three of implementation / measurement / environment to read
  adequate-or-complete. Measurement does not.

**Net classification: MEASURES -- threshold-calibration and power debt. Not chargeable to REE, and
not a mechanism failure.** Recorded explicitly because the manifest's `outcome: FAIL` plus
`hypothesis_verdict: "MECH-537 UNDETERMINED"` would otherwise read, three runs deep, as a
substantive negative about the architecture. It is not one.

**The failure signature is the INVERSE of the substrate-ceiling fingerprint.** The canonical ceiling
tell is "negative-control / absolute criterion passes, discrimination criterion fails". Here the
**discrimination** criterion (C2 rank co-primary, the only rank-matched contrast in the design)
PASSES, and the two **absolute** criteria (C2-primary against a 0.05 floor, C4b against an absolute
ceiling) fail. That is a threshold-calibration signature, not a substrate ceiling -- which is why
the recommended `epistemic_category` is `standard` and NOT `substrate_ceiling`.

---

## 6. Mechanical checks

**Re-derive brake (MOVE-3): DOES NOT FIRE.** MECH-537 counting autopsies under R1-R3 = **0**.
Both prior targets (`failure_autopsy_V3-EXQ-1043_2026-09-17`, `failure_autopsy_V3-EXQ-1043a_2026-09-20`)
read `standard` with instrument/measurement failure modes owing no build, so neither counts. This
target is `mixed` / `standard` and does not count either. A re-queue is therefore permitted --
but see section 7 for the shape it must NOT take.

> **A gap in the brake's coverage, recorded for governance rather than acted on here.** This is the
> **third consecutive MEASURES-attributed autopsy on MECH-537 with a fourth run now proposed**, and
> the brake counts zero -- correctly, by its own R3 predicate, which only counts `substrate_ceiling`
> categories and `non_contributory` directions. The brake is built to catch a claim re-tested against
> an unmoved SUBSTRATE; it is blind by construction to a claim re-tested against an unmoved
> INSTRUMENT. On this lineage the leg-level circling check (axis-family refinement vs circling,
> section 8) is the only automated guard, and it passes. Flagging the shape, not proposing a
> predicate change -- widening R3 is a governance decision with fleet-wide consequences, and
> `standard`-stamped instrument defects are the majority of the corpus.

**Granularity-debt recurrence trigger: DOES NOT FIRE.** `granularity_debt_cluster.py MECH-537`
reports 3 tagging targets across 3 files with alignment distribution `unclear=3` -- **no target
reads `weakened`**. Per the reader's own rule this is measurement or implementation debt, not
granularity debt, regardless of the count. No `/claim-synthesis` handoff.

**H-other / model-misspecification check (Mode D): FIRES.** Signals **(1)** no registered leg
explains the full outcome and **(2)** different seeds select incompatible legs -- seeds 42/44/47
select H1 (orientation present), seeds 45/46 select H2 (contrast inside the random reference), and
the per-seed values are precise enough (measurement SE 0.0021-0.0030 against a cross-seed sd of
0.0425) that the disagreement is a real property of the encoders rather than noise. The frozen
partition was posed as three GLOBAL statements about the interface and has no leg for a per-encoder
mixture.

**Response: `partition_expansion`**, recorded as an `h_other_events[]` entry on the question
*before* the leg it licenses, which is the order the registry's `h_other_route` invariant requires.
H4 is that response, not a free-standing new leg.

> **This reversed an earlier call in this same autopsy, and the reversal is the point.** The first
> draft recorded Mode D as NOT firing, on the argument that H1 explained the split by chance. The
> Step 7c red-team pass showed that argument only works under a random-effects H1 that is
> observationally identical to the very leg being added (section 3). Recorded rather than quietly
> corrected, because "a registered leg explains it" is exactly the reasoning that makes an H-other
> check rubber-stamp itself.

**Step 7b mechanical pre-routing checks**: `autopsy_pre_routing_checks.py` -> `fire_count: 0`.
C1/C2/C3 applicable (claim_ids non-empty) and silent; C3 in particular is consistent with the
measured finding that the literature IS present. C5 initially `inapplicable` (no sibling `.md` at
first run) and re-run against this narrative.

**Step 7c adversarial red-team**: see section 9.

---

## 6b. A prior recommendation was only PARTIALLY applied -- raised as GFLAG-0435

Checking this claim's current stored state against what the previous autopsy asked for turned up a
twice-dropped item, so it is recorded here rather than quietly re-requested a third time.

`failure_autopsy_V3-EXQ-1043a_2026-09-20` asked governance for three things. One was applied:
`live_status.evidence.from` was stamped to the 1043a artifact. Two were not:

1. **"Replace the 1043-era `evidence_quality_note` lead."** The note still leads with the
   `[2026-09-17 | V3-EXQ-1043 | failure_autopsy_V3-EXQ-1043_2026-09-17]` entry.
2. **"Resolve the standing 'DO NOT queue' vs EXP-1403 contradiction in notes."** MECH-537's `notes`
   field still ends: *"DO NOT queue an experiment from this entry. The read-only diagnostic harness
   (work programme ML-10/ML-12/ML-20) is the sanctioned next step and `/governance` owns whether it
   runs."* Three experiments have since been queued and run from this entry (1043, 1043a, 1043b --
   the last costing 18.2 h on ree-worker-3), and 1043b's own readiness gate cites **EXP-1403** as the
   sanctioning source-adequacy gate. The instruction is contradicted by what actually happened. It
   was named as owed by the V3-EXQ-1043 autopsy on 2026-09-17 and again by the V3-EXQ-1043a autopsy
   on 2026-09-20.

**Why this matters mechanically, not just as bookkeeping.** The partial application is what hid it:
stamping `live_status.evidence.from` satisfies GOV-APPLY-1's *provenance* clearing test, so the row
stopped being ACTIONABLE while two of the three requested edits were never made. A recommendation
that bundles a provenance stamp with substantive edits can therefore be closed by the cheapest of
its parts.

Routed as **GFLAG-0435** (`stale_note`, MECH-537, raised 2026-09-23) rather than edited here -- this
skill does not write `claims.yaml`. Both outstanding items are also carried explicitly in this
artifact's `per_claim_recommendation.MECH-537.change` so governance sees them at the walk.

---

## 7. Learning extracted and routing

**Learning extracted.**

1. **A pre-registered co-primary can decisively adjudicate a leg while the run's headline fields
   report nothing.** The reporting surface (`evidence_direction`, `interpretation.label`,
   `hypothesis_verdict`) is governed by the claim's registered CONFIRMING conjunction, which is a
   different and much higher bar than any single leg's declared null. Three runs of this lineage
   have now landed `mixed` / `undetermined` while the underlying hypothesis space actually moved.
2. **A pre-registered criterion can be non-reproducible on a FIXED subspace and still be scored as a
   conjunct.** C4b's verdict flipped on seeds 43 and 44 between 1043a and 1043b -- bit-identical
   encoders, identical parsimonious rank, deterministic RRR, so the same communication subspace
   scored twice -- because its 32-of-64 Jacobian state sample is unseeded. Measuring a ceiling
   in-run (the prior autopsy's required fix, correctly implemented) removed the *reachability*
   problem but left the *reproducibility of the statistic being compared to it* unmeasured. A
   secondary point survives from the first draft: the bar also happens to sit at 0.500 while the
   measurement's mean position along `F -> I` is 0.494.
6. **A newly added hypothesis can be observationally identical to the leg it is meant to rival.**
   H4 as first worded made the same prediction as a random-effects reading of H1 on every quantity
   this design records -- unadjudicable at any n. The fix is a declared null on *exchangeability*
   plus a named encoder-level covariate, with mechanically circular covariates excluded explicitly.
3. **Averaging over encoders may be the wrong estimand at this interface.** Within-encoder
   cross-stratum subspace agreement is 0.610 against a chance level of 0.066 (~9.2x chance), while
   cross-encoder agreement is 0.2610 (min 0.2170, max 0.2908) against the same chance level (~3.9x chance). Both are above
   chance, but replicate-specific structure is a large fraction of the communication subspace, so
   the cross-seed mean of C2 is a summary of a genuinely heterogeneous quantity.
4. **Negative result worth keeping:** C5 held at 0.610 vs 0.216 required, so the question stays
   with MECH-537 and is NOT re-routed to MECH-547 / MECH-555. Two runs have now cleared this
   premise.

**Routing: `/queue-experiment`, as a REDESIGN -- explicitly NOT a seed-count power bump.**

Work-graph classification: the node is `complex (probe-gated) / puzzle (known rules)` -- the frame
is well posed and a fact is missing. It is NOT `complicated (buildable)`: simply re-running the
same design with more seeds would narrow the CI on a mean whose estimand is in question (learning
3). The successor should carry, as a same-question lettered iteration (V3-EXQ-1043c):

- **(i) A discriminating seed increase, not a power bump.** n >= 18 sized on the observed cross-seed
  sd (0.034; sem at n=6 is 0.0173 against a 0.05 floor), reported so that it separates H1 (one
  population, small positive mean) from the newly pre-registered H4 (replicate-contingent
  orientation) -- e.g. a per-seed interval plot and a unimodality/dispersion read, not only a
  cross-seed mean. This is what converts more seeds from a power bump into a probe.
- **(ii) An anchored replacement for C4b.** Either justify the interpolation weight against
  something external, or -- preferable -- build a retention-matched version of C4a, which already
  discriminates 6/6 at a mean margin of 0.949 and fails only on the retention confound that
  currently excludes it from scoring. Do NOT simply loosen the weight until C4b passes; that is the
  re-anchoring move the pre-registration exists to refuse.
- **(iii) A reference distribution for the rank-32 arm**, without which H3's declared test is not
  resolvable at all (section 3): the arm is currently a single draw whose cross-run replicate noise
  (sd 0.025/seed) is comparable to the effect.
- **(iv) Seed the C4b probe's state sample and record its per-seed bootstrap sd.** It draws 32
  Jacobian states from 64 and is evidently unseeded, which is the direct cause of the
  non-reproducibility in section 4(b). This is the cheapest single fix in the list.
- **(v) Promote `interpretation.primary_agreement` to the reporting surface** so a leg-level
  adjudication is visible without reading the manifest body.

**Which survivor can the redesign actually adjudicate?** Stated explicitly, because a portfolio
routed at a set whose legs have no working instrument is the failure this autopsy is otherwise
warning about:

| leg | adjudicable by V3-EXQ-1043c as specified? |
|---|---|
| H1 vs H4 | **Yes** -- via the exchangeability test and its pre-registered covariate (section 8), which is what (i)+(ii) buy. |
| H3 | **Only if (iii) ships.** Without a rank-32 reference distribution its declared null is untestable, and it has been carried as `alive` through three runs on a statistic that is noise. |
| the C4 conjunct | **Only if (iv) ships**, and C4b should not be scored as a conjunct until it is reproducible on a fixed subspace. |

**Refused explicitly:** another lettered iteration at n = 6 against the same C4b ceiling. The
re-derive brake does not fire (count 0), so this refusal is a scientific judgement rather than a
mechanical gate, and it is recorded so a successor session does not read "brake not fired" as
licence for a fourth same-shape run. This lineage has spent three runs and ~18 h of worker time on
the most recent one alone.

**No `/lit-pull` commission** -- the biology is present and the translation is faithful (section 5).
**No substrate-queue entry** -- `action: none`; nothing here is substrate-blocked, and
`pending_retest_after_substrate` is false. grep of `substrate_queue.json` for MECH-537 returns 0,
consistent with that.

**Follow-on NOT chipped**, per CLAUDE.md: V3-EXQ-1043c depends on this autopsy's own not-yet-ratified
routing, so it is reported here for `/governance` Step 2b to ratify and chip.

---

## 8. Frozen-ledger delta (Step 9b)

Question `mech537_communication_subspace_orientation`. `growth_restriction` absent -> check clears.

- **An `h_other_events[]` entry is recorded FIRST** (Mode D, signal (1)+(2), response
  `partition_expansion`) -- the registry's `h_other_route` invariant requires the event to precede
  the growth it licenses, and the H4 entry below is that response.
- **H2-no-orientation**: `alive` -> **`eliminated` AS A GLOBAL CLAIM**, resolved by V3-EXQ-1043b, all
  three bar fields true, `evidence_direction: weakens`. The basis states the scope explicitly: the
  leg's PER-ENCODER content is true on seeds 45/46 and is carried forward inside H4, so this is
  **3 alive -> 2 alive + 1 expanded leg, not a clean 3 -> 2**. Writing "H2 eliminated, H4 added"
  without that sentence would launder a partition expansion into a narrowing.
- **H1-small-but-real**: stays `alive`; `resolving_runs` and `basis` updated with the CI and the
  P(>=2 negatives)=0.458 reading.
- **H3-no-low-rank-bottleneck**: stays `alive`; `basis` updated with the within-run paired rank test
  (t = -1.108, n.s.), the 6/6 re-confirmation of its structural premise, and the note that the rank
  co-primary's significance AT the parsimonious rank weakens its substantive claim.
- **H4-encoder-contingent-orientation**: **NEW leg, pre-registered (Mode A) as the
  `partition_expansion` response, not yet run.** Axis `learning-signal` (family `constitution` --
  already in `axis_families.map`, and a family not yet represented on this question, so this is
  refinement rather than circling). Basis: per-seed contrasts are measured to SE 0.0021-0.0030 yet
  differ across encoders by sd 0.0425 (~14x), with two seeds genuinely negative at 8-12 SE below
  zero; supported by within-encoder cross-stratum agreement 0.6099 vs cross-encoder 0.2610 against a
  common chance level of 0.0664 (~9.2x vs ~3.9x chance).

  **H4 carries a declared null that DISCRIMINATES it from H1, which the first draft did not.** A
  random-effects H1 and H4-as-first-worded predicted the same value for every quantity this design
  records, so H4 could not have been adjudicated at any n. The declared null is now
  *exchangeability*: H1 predicts the per-encoder C2 is exchangeable across encoders; H4 predicts a
  systematic encoder-level predictor exists. The pre-registered covariate is **cross-stratum
  data-span overlap at the parsimonious rank** (Spearman -0.886 against the de-noised C2 on these 6
  seeds -- registered as a CANDIDATE, explicitly not a finding, since 8 covariates were screened at
  n=6). One covariate is **excluded as circular and the exclusion is recorded** so a successor does
  not re-propose it: `ws250_comm_parsrank` correlates at -0.943, but C2 = D_randrank - D_comm and
  D_randrank is flat across seeds (Spearman -0.029), so that covariate is very nearly -C2 itself.
  Adjudicating run: V3-EXQ-1043c.
**Audit result (`check_hypothesis_space_integrity.py`).** This question appears ONLY in the
*Advisory -- labelled fan-out growth* section, "conditions (a)-(c) satisfied, advisory not a
violation". The report's 5 standing flags (b=2, c=3) are all pre-existing and on other questions
(`zworld_actor_adequacy_locus`, `mech467_legc_event_denominator_cause`,
`sd_e1_var_bar_readout_crush`); none is introduced here. `pre_registration_source` is
git-witnessed by this artifact.

**Convergence read**, which the audit instructs be taken from the derived payload rather than
assumed, re-derived after the Mode D revision: this growth event classifies as **`refining`** (`constitution` is a family not previously
represented; `re_entered: []`, so no circling). The QUESTION-level `convergence_class` is
**`scattering`** -- "legs added across families but no family has been closed out" -- because H1
(`measurement`) remains alive in the same `instrumentation` family from which H2 was eliminated.
That is an honest signal that this question has not converged, and it is the reason the routing
below insists the successor DISCRIMINATE rather than add power: another leg on fresh territory
without closing a family would keep the denominator growing.

- **Both ratios reported**, as `labelled_fanout_growth` (c) requires: surviving/at-registration
  **3/3**, surviving/current **3/4**.
- Invariant bookkeeping: `initial_frozen_count` 3 -> 4; `initial_frozen_count_at_registration`
  stays 3; a `fanout_growth_events[]` entry naming this artifact; `pre_registration_source` set on
  H4. H4's adjudicating run has not been queued, so pre-registration precedes adjudication
  (invariant 3a(a)) trivially and is git-witnessed by this artifact.

---

## 9. Adversarial red-team pass (Step 7c)

Run on a different model from the drafting session (drafted on Opus 5; red-team on Fable), with the
stated conclusion supplied and the drafting reasoning withheld.

**Verdict: CONTESTED.** Three findings changed what this artifact asserts or routes; all were
verified independently before adoption and all are now incorporated above rather than merely noted.
Every core number reproduced exactly (Fisher SET-ALL 2.191e-4, SET-COMPETENT 6.864e-5, Simes
0.005994, leave-one-out 0.009912, both CIs, the C4b ceiling construction and all six alternative-rule
pass counts).

| # | Finding | Disposition |
|---|---|---|
| F1 | An earlier draft's H4 premise compared a rank-9-11 cross-seed overlap against the **rank-32** chance level (0.22), making the replicates look independent when they overlap at 3.3-4.4x chance. | **Already corrected before the pass** -- caught while drafting; the artifact and ledger carry 0.2610 against the parsimonious-rank chance of 0.0664. Confirms the fix. |
| F2 | The seed split is the registry's Mode D signal (2) verbatim; the routing skipped the `h_other_events[]` entry that must precede registering a new leg. | **Accepted.** Mode D now FIRES, response `partition_expansion`, event recorded before the growth (sections 6, 8). |
| F3 | "H1 explains the negatives by chance" holds only under a random-effects H1 that is observationally identical to H4 -- so H4 had no discriminator and could not be adjudicated at any n. | **Accepted, and the most consequential.** Verified: per-seed SE 0.0021-0.0030 vs cross-seed sd 0.0425; seeds 45/46 are 8-12 SE below zero. Narrative corrected (section 3) and H4 given an exchangeability null with a named, non-circular covariate (section 8). |
| F4 | H3's "sign reversed vs 1043a" is two draws from the same noise; 1043a's inherited basis was already an over-read. | **Accepted.** Section 3 now reads "not resolvable"; 1043a's basis corrected in this edit; a rank-32 reference distribution added to the routing. |
| F5 | C4b item CONFIRMED and **strengthened** by a replicate the draft had not used; but "unanchored" contradicts `ceiling_anchor: measured_in_run`, and recomputing under alternative rules is the soft form of re-anchoring. | **Accepted.** Section 4 now leads with the same-subspace replicate (pass/fail flips on seeds 43/44), "unanchored" withdrawn and narrowed to the interpolation weight, the rule table demoted to a sensitivity note. |
| F6 | H2's elimination CONFIRMED, with the caveat that only the GLOBAL claim dies and its per-encoder content must be carried into H4 -- otherwise 3->3 is laundered as 3->2. | **Accepted.** Scope caveat written into the ledger basis; both ratios reported. |
| F7 | Surviving set not incoherent, but two of three survivors lacked a reachable discriminator. | **Accepted.** Section 7 now names, per leg, what the redesign can adjudicate and on which sub-item. |
| F8 / F9 / F10 | Fan-out growth legitimate in the F2 order; brake = 0 correct; readiness gates carry no self-anchoring defect. | **Confirmed**, no change. F9's observation that the brake is blind to a repeated-MEASURES shape is recorded in section 6. |

Hygiene items adopted: the stale substrate provenance pointer (section 1); "50.5%" corrected to the
per-seed mean position **0.494** (the 0.55 figure is `anchor_headroom_frac`, which is headroom
remaining, not position); the C4b probe's unseeded state sample added to the routing. Two further
hygiene notes are passed to governance rather than actioned here: `criteria[C2_RANK_COPRIMARY].n_seeds
= 4` records the seed-majority conjunct rather than the Fisher n and will misread on a skim, and the
driver's own `criteria[C4b].detail` prose ("under a genuine routing failure ... the ratio to ~0") is
contradicted by `per_seed_jacobian_aligned_floor >= 0.620` on every seed -- the attainable floor for
these encoders is ~0.7, never ~0.

**A note on what the pass did and did not do.** It confirmed the science (H2's global null is rejected
by every combiner it tried, including two the pre-registration did not name) and contested the
*routing and the ledger text* -- which is the documented pattern for this check. The single most
valuable finding, F3, overturned a piece of reasoning that had been used to SUPPRESS a required
registry step; a CONFIRMED verdict here would have left that in place.
