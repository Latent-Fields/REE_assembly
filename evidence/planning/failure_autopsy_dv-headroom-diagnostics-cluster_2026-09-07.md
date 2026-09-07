# Failure autopsy -- four owed diagnostics, 2026-09-07

**Scope:** cluster (4 targets). **Status:** confirmed (user gate held 2026-09-07).
**Generated:** 2026-09-07T19:05:21Z

Targets: V3-EXQ-1006, V3-EXQ-970a, V3-EXQ-972a, V3-EXQ-1009. All four are
`experiment_purpose: "diagnostic"` PASSes owed a confirmed autopsy; V3-EXQ-1009 additionally
carried the indexer's `vacuous_pass` adjudication flag. Scope was taken from a freshly
regenerated `pending_review.md` (0 FAIL, 0 ERROR, 0 unclaimed manifests pending).

## 0. Gates run before any metric was read

- **Dry-run gate (Step 2a):** `check_dry_run_citations.py` -- 4 clean, 0 dry, 0 ambiguous.
  No smoke manifests are cited anywhere in this artifact; every denominator below is a real-run
  denominator.
- **Recording provenance:** `validate_recording.py` -- 4 of 4 complete, 0 always-core gaps.
  No recording debt; `substrate_hash`, `config`, `seeds`, `machine_class`, `elapsed_seconds`
  present on all four.
- **Pre-routing checks (Step 7b):** `autopsy_pre_routing_checks.py` -- 0 fires. Recorded with the
  caveat that C1/C2/C3 are claim-keyed and three of the four targets carry `claim_ids: []`, so a
  quiet report here is partly structural blindness, not a clean bill.

## 1. The cluster finding -- a MIXED verdict on the dv_headroom convention

Three of the four targets carry a pass bar in tension with their DV's achievable range. The first
draft of this autopsy read that as "the dv_headroom instrument caught all three, three for three".
**The adversarial pass refuted that, and the corrected reading is more useful.**

| Run | Gate | What the headroom entry measured | Verdict on the entry |
|---|---|---|---|
| V3-EXQ-1006 Leg B | var bar 0.002 | achievable 0.00107 (ratio 0.54) | **clean catch** -- verified, correctly declared non-gating |
| V3-EXQ-1009 C1 | content floor 0.02 | ratios on `delta_dbar`, but C1 gates `projected_lineage_increment` | **right answer, wrong statistic** |
| V3-EXQ-972a T3 | margin 0.15 | `1 - MAX(control acc)` = 0.0806, but T3 tests the **MEAN** | **false positive** -- T3 was adequately ranged |
| V3-EXQ-970a H1 | NMI excess 0.1 | 0.872 / 0.860 (ratio 8.7 / 8.6) | clean control -- decisive positive, p=0.0039 |

So the honest count is **one clean catch, one right-for-the-wrong-reason, one false positive** --
not three for three. The convention is deployed and valuable, but this batch does not show it
working as designed: two of its three firings were computed on a quantity other than the one the
criterion gates.

**The sharpened rule is stronger than "measure headroom":**

> A `dv_headroom` entry MUST be computed on the same **statistic** *and* the same **order
> statistic** as the criterion it certifies.

And a cheap self-check falls out of the 972a case: **if any observed value of the test statistic
exceeds the asserted ceiling, the ceiling is mis-specified.** Two of 972a's eight paired diffs
(0.16135, 0.09297) exceeded its asserted 0.0806 ceiling; one exceeded the 0.15 requirement outright.

## 2. V3-EXQ-1006 -- sd_e1_var_bar portfolio

Six seeds, four arms, all GREEN. The only `load_bearing` criterion is C0 (`any arm green`);
C1-C5 are `load_bearing:false` classification labels by design, explicitly citing a prior
`vacuous_pass` lesson. That is a sound answer to that failure mode: the gate carries readiness,
the leg readings carry the science.

- **Leg A (H-fidelity-anchor)** -- unanimous 6/6 on all three sub-conditions (centroid in band 6/6;
  variance lift 7.6x-214x, all >= the 2x requirement; cr bar retained 6/6). Adjudicable.
- **Leg C (H-goal-orthogonal-dispersion)** -- unanimous 6/6 (goal-axis ratio 0.008-0.28, all well
  below the 0.5 boundary of the "within 2x" null). Adjudicable.
- **Leg B (H-readout-saturation)** -- **NOT adjudicable, and this is the finding.** Its declared
  null is "real-endpoint goal_proximity variance >= 0.002 on a majority of seeds". On the
  **from-reset (Phase 4b)** endpoint set all **6/6** seeds clear 0.002 (0.0047-0.0196) -- null met,
  hypothesis eliminated. On the **same-start (Phase 4d)** set the driver adopted, **4/6** fall below
  -- null not met, hypothesis supported. **The two admissible denominators invert the verdict.**

The driver disclosed the switch and argued for it. Note the justification must be stated
**geometrically, not empirically**: "the from-reset set is an upper bound" is falsified by one of
this run's own cells -- on **seed7** the same-start variance *exceeds* the from-reset variance
(0.0239158 vs 0.0196255); it holds 5 of 6. The load-bearing argument is that at h=1, 40 rollouts
from ONE start reach at most `n_actions` distinct endpoints, so the same-start set isolates
rollout-attributable variance while the from-reset set adds start dispersion. That argument stands.

**An asymmetry to carry into the governance decision:** the manifest's own
`interpretation.branched_same_start_note` says *"the registered legs read Phase 4b so this run stays
comparable with 1000"* -- yet the same-start substitution was applied to **Leg B only**. Leg C still
reads Phase 4b, and Leg B is the only leg whose verdict the switch changes. I checked whether this
is results-driven and it is **not**: on the same-start denominator Leg C still reads
`rsd_goal_orthogonal` (5 below / 1 above). But the asymmetry is unexplained.

Both denominators are recorded, so **settling Leg B needs no new run** -- it is
`complex (probe-gated) / mystery (known data)`: the frame is missing, not the data.

**User gate disposition: Leg B stays ALIVE**, with both denominators and the asymmetry recorded.
Legs A and C resolve `confirmed`.

This run also discharges the question's recorded `observation_bottleneck`
("real-endpoint goal_proximity variance never recorded").

`substrate_stable_across_run: false` here is **benign**: `process_snapshot_drift` is empty and the
two distinct per-cell hashes are the reusable OFF baseline minted with
`include_driver_script_in_hash=False`. (There is no `disagreement_kind` field on this manifest --
an earlier draft cited one; it does not exist.)

## 3. V3-EXQ-970a -- ContextMemory write-content H1, redesigned MI instrument

This is the instrument redesign the 2026-09-03 cluster autopsy demanded ("instrument redesign, not
another leg"), and **it discharges that demand on all three named defects**:

- near-binary Jaccard DV (72/89 cells could only score 0.0 or 1.0) -> NMI-excess with **8.6-8.7x
  headroom**;
- attainable p-grid floor above alpha -> floor **0.0039** now below alpha **0.0125**;
- tie saturation -> **0 tied pairs** on 8 paired seeds.

**Result:** the contrastive objective raises generalising content conditioning in **both** regimes
(Regime A real-agent latents 0.018 -> 0.312, 8/8 seeds, p=0.0039; Regime B synthetic 0.067 -> 0.259,
p=0.0039). **The necessity half of H1 is refuted:** in Regime B the *content-blind* `DIVERSITY_956`
arm also raised the DV (+0.244, p=0.0039) and beat the contrastive arm on 6/8 seeds. In Regime A it
did not move (-0.007, p=0.51). So content reference is **not required** -- and the regime split is
the informative part.

**Scope limit that must travel with this result:** the tagger's `z_world` input is a **frozen random
projection**. The driver detaches `z_world` at `:887`, and V3-EXQ-972a measures zero `latent_stack`
delta on 8/8 seeds for this harness family. This is evidence that a tagger can learn
content-conditioned addressing *from* a frozen projection -- not that a trained encoder was involved.

**Provenance caveat:** `substrate_stable_across_run: false` with a **non-empty**
`process_snapshot_drift` (the `ree-v3` worktree was mutated twice mid-run, 14:27:07Z and 14:38:51Z)
and `commit_describes_recorded_hash: false`. Unlike V3-EXQ-1006's benign driver-fold divergence,
this one means the exact substrate state behind these numbers is not pinned.

## 4. V3-EXQ-972a -- SD-070 held-out linear probe (the load-bearing target)

This is the "cheap upgrade" the 2026-09-03 autopsy prescribed by name, and **it overturns its
predecessor's reading on the first attempt.** V3-EXQ-972 reported write-stream separability 0.0281
under an uncentred cosine contrast and that fed a "no structure" reading. The held-out linear probe
finds the stream **linearly decodable**: zworld32 probe excess **0.335** over a shuffle null, 8/8
seeds, p=0.0039, **84.4% mean balanced accuracy**. Structure exists; it is simply **off the raw
axis**.

**SD-070 is NOT weakened -- but not for the reason this autopsy first gave.** The first draft called
T3 "structurally starved". The adversarial pass refuted that and I confirmed the refutation by
recomputation:

- T3's pass condition is on the **mean** paired diff (`>= 0.15`). The mean-matched achievable
  ceiling is `1 - mean(LINEAGE accuracy) = 1 - 0.844437 = 0.155563` -- **ratio 1.037, adequate.**
- The driver's `dv_headroom_T3_above_lineage_accuracy` reports `0.0806 = 1 - MAX(accuracy) =
  1 - 0.91935` -- a **mismatched order statistic**.
- Decisively: **2 of the 8 observed paired diffs exceed that asserted ceiling** (0.16135, 0.09297),
  and one exceeds the 0.15 requirement outright. A ceiling the data exceeds is not a ceiling.

So T3 is a **genuine, adequately-ranged null**: mean -0.0105, p=0.625, 4+/4-. It reads
`non_contributory` for SD-070 because it probes **a readout SD-070 does not assert** -- SD-070's own
validation is grounding-head balanced-accuracy lift and z_world participation ratio, and its
registered `validation_experiment` is V3-EXQ-783, not this run. The `SD070_WARMED`
participation-ratio drop 7.50 -> 3.42 is in-family with SD-070's own registered validation
(9.21 -> 5.19) and is not counter-evidence.

The mismatched headroom entry is itself a **minor driver defect worth recording** -- and it is the
inverse of the lesson the first draft drew from it.

### The finding that reframes the portfolio

`lineage_encoder_frozen_by_construction`, confirmed by a hash-verified identity control:

- **LINEAGE latents are bit-identical to UNTRAINED_ENCODER latents on 8/8 seeds**
  (`collection_latent_hash`), and their per-seed probe excesses are identical value-for-value.
- **0 of 49 `latent_stack` parameters receive gradient**; 8/8 LINEAGE cells read zero delta.
- Mechanism, verified independently in source: `standard_params`
  (`v3_exq_970a...py:984-986`) *includes* the encoder -- it excludes only `harm_eval_head` and
  `context_memory.memory` -- so the optimizer **looks** like it trains the encoder. The graph is
  severed upstream by the detach at `:887`, so the parameters are optimised over but never move.

**Consequence, scoped exactly.** The buffered-detach training pattern is **code-verified in four
drivers** -- V3-EXQ-970, 971, 972 and 970a -- and **measured** only in 972a's own LINEAGE arm.
**V3-EXQ-956 and 969 do NOT carry the pattern** (independently confirmed: zero occurrences of the
detach-cat into a training pool) and are **not** covered by this finding. An earlier draft asserted
"every leg"; that over-reached, and the manifest's own note says "the 956/970/972 harness".

`SD070_WARMED` is the one arm whose encoder genuinely moved (participation ratio 7.50 -> 3.42;
class latent norms 0.4-0.5 -> 1.2-1.8), and it did **not** raise linear decodability.

**Gate disposition:** amend the substrate entry, and annotate the still-alive legs **H2
(operating-point)** and **H3 (task-pressure)** in the ledger that their adjudicating runs measured a
frozen projection -- without re-adjudicating them here.

This is why T1 and T4 are numerically identical: the "lineage" arm and the "untrained" baseline are
the same object with respect to the representation under test.

## 5. V3-EXQ-1009 -- MECH-267 elite-channel ceiling spike

Commissioned after V3-EXQ-1005 was refused at red-team, to separate two candidate causes of the
elite-selection ceiling (untrained E2 action-object head vs the support-preserving `ao_std` floor).
**It discriminated neither, and its own manifest records why.**

**Argued on C1's OWN statistic.** C1 gates `projected_lineage_increment = sqrt(B^2+d^2)-B`, and the
per-cell `shortfall_factor_vs_floor` against the 0.02 floor is:

| cell | shortfall on C1's statistic |
|---|---|
| FROZEN/floor0.2 | 43.03x |
| **FROZEN/floor0.0** | **2.31x  <- the marginal cell** |
| GROUNDED/floor0.2 | 8.69x |
| GROUNDED/floor0.0 | 4.72x |

No cell is near-clearing; the closest is 2.31x short.

**Two corrections the adversarial pass forced, both of which I confirmed:**

1. **Do not quote `dv_headroom.headroom_ratio_by_cell` as C1 headroom.** Those ratios
   (0.5709 / 0.5588 / **0.9973** / 0.4531) are computed on `delta_dbar`, not on the statistic C1
   gates. The 0.9973 figure belongs to GROUNDED/floor0.2 -- a cell that is **8.69x short** on C1.
   The first draft put that number in the durable failure record, where it would have read as
   "one cell almost cleared" and invited exactly the re-attempt the record exists to forbid.
2. **Drop "unreachable by construction".** The manifest's own
   `red_team_dispositions_iter3.oracle_is_greedy_not_exhaustive` records that the oracle is a greedy
   chooser, not an argmax over all C(16,3)=560 elite subsets, so **the measured ceiling is a LOWER
   bound on the true oracle ceiling** -- which is incompatible with "by construction".

The defensible claim is bounded and still decisive: **at this oracle's strength the elite-selection
channel does not come within 2.31x of the floor on any of four benches**, and the oracle directly
optimises the axis the DV measures, so a real mode-conditioned arm is very unlikely to do better.

The self-routed label `elite_channel_ceiling_confirmed_all_benches` **over-reads on exactly this
point** and must not be applied as a confirmed bench-independent ceiling. The driver's own
`what_a_null_does_not_mean` already states the correct, narrower reading ("a statement about what
the proposal-output centroid readout can see, NOT evidence against MECH-267"), and `claim_ids` is
deliberately empty for that reason. The discipline here is good; only the label is too strong.

**C2 is degenerate downstream of C1, not a co-failure.** The driver computes
`c2_cells = [lab for lab in c1_cells if clears_c2(lab)]`, so an empty C1 *entails* an empty C2; the
driver scores `criteria_non_degenerate.C2 = false` and routes on C1 alone. C2 was in fact
**satisfied on its own statistic** for GROUNDED/floor0.2
(`joint_satisfiability_of_c1_and_c2.clears_c2_beats_production: true`). Reporting "both criteria
failed" double-counts one failure.

**On the `vacuous_pass` flag:** mechanically correct. `outcome = "PASS"` is assigned in **three of
four** branches of the driver's decision tree; only a readiness-precondition failure yields FAIL. So
PASS is a driver convention meaning "the diagnostic ran and produced an interpretable null", not a
criterion result. Read it as *informative null on a starved DV*, not as a degenerate result.

**Two design choices I checked and found sound, not defects:**
- `mode_conditioning_enabled=False` in every cell is deliberate -- "the oracle IS the content
  manipulation here", so no mode-conditioned knob is engaged and the cells differ only along the two
  declared axes. The oracle is a strictly stronger stand-in.
- The 24.17s runtime is fully accounted for: a proposer-only synthetic bench, no env, no agent, no
  rollout. Nothing is stubbed.

### Re-derive brake: FIRES

MECH-267 stands at **4 ceiling hits** under R1-R3 against a threshold of 2
(869, 869a, 923, 927-928-cluster) -- recomputed and confirmed. This target is not claim-tagged, so
it does not itself increment the count -- but it is the **fifth probe of the same claim against the
same substrate**.

**A further proposal-output-centroid re-test of MECH-267 is REFUSED.** A redesign on a *different*
readout, or work on the already-confirmed breadth channel, remains permitted.

**Stated honestly: that specific refusal is prose, not machine-enforceable.** The
`/queue-experiment` consumer gate keys on (claim, substrate) and has **no readout dimension**, so it
cannot see "proposal-output-centroid" as a distinguishing feature. It costs nothing here -- the gate
already refuses MECH-267 re-tests on the pre-existing count of 4 -- but the refusal rides on that
count, not on this target.

### Bears on: a stale ledger gate

While adjudicating this run: the `mech267_content_persistence_cem_refit` ledger entry's
`decision.live_gate` still says the remaining work is to "flip `mode_partitioned_cem` from its
**False** default". **That flip landed 2026-08-26** (ree-v3 `376d563`,
SD-MECH267-CEM-SELECTION-FIX); the config now reads `mode_partitioned_cem: bool = True`. The gate
text is stale on its own terms and should be corrected to name the open residual instead --
V3-EXQ-928's finding that the **ordered four-mode gradient is still not restored** (only the
extreme-pair contrast is rescued). Recorded here as a bears-on note; governance owns the edit.

## 6. Failure-location summary (GOV-FAILLOC-1)

| Target | Mechanism | Measures | Environment | REE | Net |
|---|---|---|---|---|---|
| V3-EXQ-1006 | established | partial | established | **false** | NOT A FAILURE -- informative portfolio; Leg B is MEASURES-partial |
| V3-EXQ-970a | established | established | established | **false** | NOT A FAILURE -- positive result on a successfully redesigned instrument |
| V3-EXQ-972a | not_established | **established** | established | **false** | MIXED -- MECHANISM-untested for the portfolio; measurement is adequate, T3 included (corrected after red team) |
| V3-EXQ-1009 | not_established | not_established | established | **false** | MEASURES -- DV came no closer than 2.31x to its own floor under a greedy oracle |

**No target reaches REE FAILED, and none comes close.** In every case at least one of Measurement or
Mechanism is not independently adequate, so nothing here is chargeable to REE.

## 7. Routing

| Target | Routing | New experiment owed? |
|---|---|---|
| V3-EXQ-1006 | governance decides the Leg-B denominator | **No** -- both denominators already recorded |
| V3-EXQ-970a | governance records the result + its frozen-encoder scope limit | **No** |
| V3-EXQ-972a | `implement-substrate` -- amend `contextmemory-write-path-addressing-degeneracy`; annotate ledger H2/H3 | Not yet -- the harness defect is a build |
| V3-EXQ-1009 | `implement-substrate` -- amend SD-MECH267-CEM-SELECTION-FIX; governance narrows MECH-267's `what_would_answer` | **No -- same-readout re-queue REFUSED** |

Two prior `failure_record` items are marked **superseded** (not resolved -- nothing was fixed, a
better instrument overturned the read): `v3_exq_972_...` by 972a's linear probe, and
`v3_exq_970_...` by 970a's MI instrument.

## 8. Learning extracted (portfolio level)

1. **A `dv_headroom` entry must be computed on the same STATISTIC and the same ORDER STATISTIC as
   the criterion it certifies.** Two of this batch's three headroom firings were not: 1009 measured
   on `delta_dbar` while C1 gates `projected_lineage_increment`; 972a measured on
   `1 - MAX(control accuracy)` while T3 tests the mean. One produced a misleading durable record,
   the other a false "starved instrument" reading.
2. **Cheap self-check for any headroom claim: if an observed value of the test statistic exceeds the
   asserted ceiling, the ceiling is mis-specified.** Two of 972a's eight paired diffs did.
3. **Add a latent-identity control to any experiment whose claim is about a learned
   representation.** One hash comparison between a nominal treatment arm and an untrained control
   exposed, in a single criterion, what four prior legs of the portfolio could not see.
4. **An optimizer's parameter list is not evidence that a parameter trains.** The encoder sat in
   `standard_params` and never moved, because the loss was computed on detached buffered latents.
5. **A durable failure record must quote the number a future reader will act on.** The first draft's
   record quoted a 0.9973 headroom ratio for a cell that is 8.69x short on the gating statistic --
   the record would have invited the re-attempt it was written to prevent.

## 9. Adversarial pass (Step 7c)

Verdict **CONTESTED**, run on the inherited session model (Fable was unavailable -- out of usage
credits -- and the skill's single re-spawn was used). Five contested findings and seven hygiene
findings were raised; **every contested finding was independently re-verified by this session before
acceptance**, and all were accepted. Two changed an adjudication (972a's T3; 1009's statistic), one
corrected the headline cluster reading, one corrected a substrate path that did not reach the code
it blamed, and one reconciled a routing field with the brake it invoked.

Recorded because it is the point of the exercise: **the science in the first draft was not wrong --
the recommendations and the durable records were.** That matches the measured pattern across prior
autopsies.
