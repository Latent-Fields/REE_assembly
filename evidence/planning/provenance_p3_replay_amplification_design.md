# Assay P3 — replay amplification: design and preregistration

**Date:** 2026-09-10
**Status:** design / preregistration scaffold only. This document does **not** register, promote, implement, queue or score a claim, does not modify any assay script, the ladder, or the supplement, and makes no diagnostic assertion about psychosis. It inherits the parent audit's no-build / no-queue / no-promote boundary.
**Ladder rung refined:** [`provenance_false_evidence_multiplication_experiment_ladder.md`](provenance_false_evidence_multiplication_experiment_ladder.md) — assay P3
**Audit that motivates it:** [`provenance_false_evidence_multiplication_campaign_supplement_20260910.md`](provenance_false_evidence_multiplication_campaign_supplement_20260910.md) §4 (Break B), §8 (P3-R1/R2/R3), §10 (four readouts), §11 (falsifiers), §12 (epistemic boundary)
**Campaign sources cited:** [`docs/thoughts/2026-09-09_hippocampal_campaign_adjudication.md`](../../docs/thoughts/2026-09-09_hippocampal_campaign_adjudication.md) §8, matrix rows E20, E30, E32, E42, E43
**Literature fold-in (2026-09-10, after this document landed):** [`provenance_judgment_class_literature_tranche.md`](provenance_judgment_class_literature_tranche.md) (REE_assembly `b682aed66f`). Two consequences for P3, folded in below: the Break B statement in §1 is **corrected** (§1.1) — step 5 is untested *for cardinality*, but a reactivation-strengthens-memory result does exist — and a third route to a replay-count effect is added as `P3-R8` (§8.1a). The premise is **strengthened**, not weakened.
**Harness dependency:** the descendant-generation and genealogy representation are owned by a sibling design (`provenance_harness_generated_ancestry_design.md`), which did **not** exist when this was written. This document is therefore written against the abstract eight-operation contract; see §9.

---

## 1. Why this rung, and why now

The audit's Break B is a stronger statement than "P3 is unwritten". It is that **step 5 of the chain — recursive amplification across replay — has no evidence in any direction, in any class**:

```text
grep -il replay scripts/convergence_signal_synthetic_assay_00*.py   ->  nothing
```

Re-verified 2026-09-10 with `/usr/bin/grep` against all six assay scripts: still nothing. No REE assay contains a replay loop. Neither the clinical nor the rodent literature measures evidence cardinality across replay cycles — C1 preparations cannot read cardinality at all, and the C3 judgment studies (Yousif 2019, Connor Desai 2022, Weaver 2007) present a fixed source structure once rather than iterating it.

So H2 is **unaddressed rather than weakly addressed**. Every other rung of the ladder has at least an adjacent result that constrains its prior; P3 has none. Stated plainly, as §8 of the audit requires: **P3 is the branch's highest-information unrun assay, and its information value does not sit behind P1.**

### 1.1 Correction to Break B — "no evidence in any direction, in any class" is too strong

**Corrected 2026-09-10 by the judgment-class tranche §6.2. The correction narrows the claim; it does not weaken the rung.**

The audit's Break B is right **for cardinality** and wrong **for strength**, and the distinction changes P3's control structure rather than its motivation.

- **Corlett, Cambridge, Gardner et al. 2013**, *Ketamine effects on memory reconsolidation favor a learning model of delusions*, PLoS One 8(6):e65088, [DOI 10.1371/journal.pone.0065088](https://doi.org/10.1371/journal.pone.0065088), PMID 23776445. Human, placebo-controlled, within-subjects (n=18). A **single unreinforced re-presentation** of a conditioned stimulus under ketamine produced a *stronger* memory at 24h than under placebo; the degree of strengthening correlated with individual vulnerability to ketamine's psychotogenic effects and with prediction-error brain signal. Partially replicated in an independent appetitive sample (n=8).
- **Honsberger, Taylor & Corlett 2015**, *Memories reactivated under ketamine are subsequently stronger*, Schizophr Res 164(1–3):227–233, [DOI 10.1016/j.schres.2015.02.009](https://doi.org/10.1016/j.schres.2015.02.009), PMID 25728834. Rodent homologue: pre- but not post-reactivation ketamine enhanced fear memory at 24h, absent at 3h, not generalising to a closely related contextual memory, and blocked by prior inhibition of a BLA destabilisation mechanism.

So a **reactivation-without-new-evidence → increased memory strength** effect exists, in two species, with a direct psychotomimetic link and a named mechanism (aberrant prediction error during reconsolidation).

**What survives, stated precisely.** Break B stands *for cardinality*: neither study measures effective source count or calibration, and neither concerns ancestry. The grep result above is unchanged, and no literature anywhere measures cardinality across replay cycles. What can no longer be said is that P3 has **no evidence in any direction for anything in its region** — the sentence above and §1's framing are corrected accordingly.

**Net effect on the rung: the premise is strengthened.** A mechanism that raises confidence through reactivation alone is now *documented* rather than merely hypothesised — which makes the rung more likely to produce a signal and simultaneously makes it easier to mis-attribute. That confound is `P3-R8` (§8.1a), and the ancestry × replay-count interaction (§8.3) is already the design's answer to it.

---

### P3 is not downstream of P1's verdict

P3 depends on P1's *harness* (the genealogy representation) but not on P1's *result*, and the distinction matters for sequencing. P1 fixes descendant cardinality at four. P3 varies it across `0, 1, 2, 4, 8, 16`. These are different points on the same axis, so:

- A P1 null bounds only the four-descendant point. It does **not** license "no amplification at higher cardinality" — an effect below threshold at four may be large at sixteen, which is precisely the shape H2 asserts.
- A P1 positive does not establish H2 either: a single-shot inflation that does not grow with descendant count is H1 without H2, and that dissociation is itself a result worth having.

The consequence for ordering: build the harness once, then run P1 and P3 against it; do not gate P3's *launch* on P1's *outcome*.

---

## 2. The replay loop itself

### 2.1 State and the freeze

The assay state at any time is an evidence graph `G` plus a reader:

```text
G  = nodes  : evidence items, each with content, retrieval fidelity, and a kind tag
     edges  : ancestry links, each with an integrity value
     H      : the latent proposition under test
world truth: the realised value of H, drawn at t0 and known only to the harness
reader     : a fixed inference rule mapping G -> (belief in H, effective source count)
```

`t0` is the freeze point. Before `t0` the harness draws world truth and emits the **seed evidence set** — the only nodes with a causal link to the world. After `t0`:

- **Frozen:** the seed evidence set; world truth; the reader's inference rule and all of its parameters; the ancestry-integrity treatment level; the replay-kind assignment; the retrieval-noise parameters pinned by the §6 titration.
- **Free to change:** the node set (descendants accumulate); per-node retrieval fidelity; association strength; the reader's effective independent-source count, belief and calibration; the integrity of ancestry links *created after t0*, and — in the compounding arm only (§2.4) — of links created before it.

**The freeze must be a harness primitive, not a convention.** Every node created after `t0` must be constructible only as a descendant of an existing node. A design in which the world generator remains callable after `t0` can leak a genuinely new observation through a coding error, and the resulting confidence rise would be *correct* inference misread as amplification. See §9, requirement H6.

### 2.2 What one replay event does

A replay event is a single call to contract operation 3 with four parameters:

```text
replay(kind, mode, selection, rng)
```

1. **`selection`** picks the source node(s) from `G` (§2.5).
2. **`kind`** determines what is produced (§3): rehearsal, relational link, or prediction.
3. **`mode`** determines whether the product is written **in place** onto the source node, or **appended** as a new descendant node carrying an ancestry link back to its parent(s).
4. Any ancestry link created is passed through the degradation process (contract operation 2) at the cell's fixed integrity treatment level.

Everything the hypothesis is about happens in step 3 and step 4. `mode = in_place` raises the source node's retrieval fidelity and adds no node — this is the shape a healthy consolidation has, and §5 shows why the arm is unreachable without it. `mode = append` adds a countable node whose independence from its parent depends entirely on whether the ancestry link survives step 4.

### 2.3 Realising the replay counts

Replay counts `0, 1, 2, 4, 8, 16` are the number of `replay()` calls executed between `t0` and the readout. They are log-spaced, so the predeclared analysis scale is `log2(1 + r)`, fixed in advance (§7.4). The readout is taken once, at the end of the schedule, with all four readouts of §6 read at that single point; per-`r` trajectories come from the six separate cells, not from repeated reads within one run, so that reading the graph cannot itself perturb it.

### 2.4 Accumulation and compounding are different hypotheses — split them

If replay events degrade *existing* ancestry links as well as creating new ones, then replay count and cumulative ancestry corruption vary together and no interaction can be attributed to either. That confound is not a bug to be removed — it is the mechanistically interesting version of H2 — but it must be separated from the version that is interpretable:

| Arm | Ancestry degradation applies to | What varies with `r` | Interpretability |
|---|---|---|---|
| **P3-A accumulation** (primary) | newly created links only, at a fixed per-link rate set by the cell's treatment | descendant count only | clean: an interaction is attributable to cardinality |
| **P3-B compounding** (secondary) | new links *and* re-encoded existing links | descendant count **and** cumulative corruption | confounded by construction; interpretable only against the matched P3-A cell |

**P3-A is primary and is the arm the §8 falsifier is stated against.** P3-B is where H2's *self-maintaining* clause could be observed, and it is reportable only as a delta from P3-A at the same `r` and treatment level. Reporting P3-B alone as evidence for H2 would be reporting a confound.

### 2.5 The selection policy is the self-maintenance feedback path

H2 asserts amplification "becomes self-maintaining". Self-maintenance requires a feedback loop, and in this design the only place one can exist is the replay selection policy. E32 (Gillespie 2021) shows replay content reflects selected past experience rather than a plan, and E42 (van de Ven 2016) shows offline reactivation dependence is selective by assembly stability — so a design that replays uniformly is not merely a simplification, it deletes the mechanism.

Two predeclared levels, crossed with the rest:

```text
uniform       : source node drawn uniformly from G
preferential  : source node drawn with probability proportional to current
                association strength (rich-get-richer; the E32/E42 shape)
```

Predeclaration: **amplification under `uniform` is accumulation; amplification present under `preferential` and absent (or materially weaker) under `uniform` is self-maintenance.** H2's strong form requires the second pattern. If the two are indistinguishable, report H2 as supported only in its weak (accumulation) form.

---

## 3. P3-R1 — stratify replay by kind

Per audit §8 and campaign rows E42/E32/E43. Replay is not one operation, and the three kinds have *different correct behaviour*, which is why a pooled main effect is not a result.

| Kind | What it produces | Parents | Correct behaviour under intact ancestry | Why it must not be pooled |
|---|---|---|---|---|
| **(a) content rehearsal** | a reinstatement of one episode; same content | 1 | fidelity ↑, count flat (with `mode=in_place`) | adds no content, so **any** count rise here is pure cardinality error — the cleanest positive signal |
| **(b) relational linking** | a relation between two episodes; the E43 (Zaki) operation | 2 | association ↑, count stays at the true number of distinct world events | E43 shows this is **adaptive**; a count rise here is the opposite failure — collapsing distinct sources — and must be detectable, not scored as a pass |
| **(c) prediction-generated** | a predicted observation derived from a node plus the model | 1 + model | calibration may legitimately ↑ (the E30 regime), count flat | a prediction has the *format* of an observation, so this is where legitimate computation (P1-R3) is hardest to distinguish from forbidden gain |

A pooled `r` main effect mixes a pure-error kind, an adaptive kind and a legitimate-gain kind, and its sign tells you nothing about which is driving it. **Kind is a between-cell factor. The primary interaction test is run per kind, and a result is reported per kind or not at all.**

---

## 4. Design matrix

```text
ancestry condition   x  replay count  x  replay kind   x  selection policy
{VERIDICAL, SOFT,       {0,1,2,4,8,16}   {rehearsal,      {uniform,
 ABSENT, FALSE_SPLIT}                     relational,      preferential}
                                          prediction}
```

`4 x 6 x 3 x 2 = 144` primary cells (P3-A), plus the same grid for P3-B (§2.4) where the compounding delta is wanted — which need not be the full grid; the predeclared P3-B subset is `{VERIDICAL, FALSE_SPLIT} x {0,4,16} x {rehearsal} x {uniform, preferential}` = 12 cells, sufficient to detect a compounding delta without quadrupling cost.

Ancestry conditions carry P1's semantics unchanged (`VERIDICAL` known, `SOFT` degraded probability, `ABSENT` unknown, `FALSE_SPLIT` incorrectly represented as independent families). Per audit §9 and Connor Desai 2022, `SOFT`/`ABSENT` are the scientifically loaded conditions, not `FALSE_SPLIT`: ambiguity about independence is the condition under which the human effect actually appears. A P3 in which amplification appears only under `FALSE_SPLIT` and not under `ABSENT` is diverging from the human pattern and should be **reported as a divergence**, not as a pass.

The unit of replication is the seed. Each seed draws its own world truth and seed evidence set, and the same seed is used across every cell so that ancestry treatment, replay count, kind and policy are crossed **at matched world draws** — which requires the harness to expose a world-generation RNG stream separate from the replay RNG stream (§9, requirement H7).

### Controls carried down from the global red-team list and P1

| Control | Cell | Predeclared correct result |
|---|---|---|
| no-replay | `r = 0`, every condition | the P1 baseline; any ancestry effect here is single-shot, not amplification |
| genuinely independent new observation | one arm that violates the freeze **deliberately and labelled**, adding a real second world observation before readout | count ↑ **and** confidence ↑ **with calibration preserved** — the positive control proving the count readout has dynamic range in the correct direction |
| correctly linked duplicate | duplicate content, ancestry intact | count flat, confidence flat |
| adaptive linking (E43) | kind (b), two genuinely distinct world events, `VERIDICAL` | association ↑, count = 2 |
| legitimate computation (E30 / P1-R3) | kind (c), `VERIDICAL`, fixed observation set | calibration ↑, count **unchanged** |
| healthy replay (§5) | kind (a), `VERIDICAL`, `mode=in_place` | fidelity ↑, count flat |

Without the independent-new-observation control a null under corruption is uninterpretable, because a flat count is indistinguishable from a dead instrument.

---

## 5. P3-R2 — a healthy-replay arm that can pass, treated as a gate

Audit §8: "P3 needs an arm in which replay improves retrieval fidelity while effective source count stays flat, and it must be possible for this arm to produce that result. If every replay arm inflates the count, the instrument is measuring replay exposure, not genealogy."

E20 (Kovács 2016, SWR blockade did not degrade CA1 map stability) and E30 (Rule & O'Leary 2022, self-healing codes track a drifting representation with no explicit lineage) are the two independent indications that offline processing improves representation **without adding evidence**. The arm exists to show the architecture can do the same.

**The reachability condition is mechanical, and it is a harness requirement.** The arm can only pass if content rehearsal under intact ancestry can improve a node *without appending a countable descendant* — i.e. if contract operation 3 supports `mode = in_place` (§2.2). If replay is descendant-generating only, then every replay event adds a node by construction, the count rises in every arm including `VERIDICAL`, and P3 measures replay exposure. **This is the single most likely way for P3 to be built unfalsifiable**, and it is invisible until the results are in.

Therefore:

> **Gate.** The healthy-replay arm is run **first**, as a standalone spike, on pilot seeds that are discarded. It must produce fidelity ↑ with effective source count flat under `VERIDICAL / rehearsal / in_place` before the confirmatory grid is launched. If it cannot, the instrument is not measuring genealogy and the correct action is to fix the harness, not to run the grid and interpret the output.

This is a precondition, not an arm to be assessed alongside the others after the fact.

---

## 6. P3-R3 — match retrieval quality prospectively

Audit §8: the ancestry × replay-count interaction is admissible **only at matched retrieval quality**; otherwise it is a retrieval effect wearing a provenance label. Corrupted-ancestry conditions can plausibly retrieve better (fewer constraints on reinstatement) or worse (degraded links degrade recall), and either direction produces a spurious interaction.

**Titrate prospectively; never condition on realised fidelity.**

1. **Pilot sweep, discarded seeds.** For each `(ancestry condition, replay count, kind)` cell, sweep the harness's exposed retrieval-noise parameter (contract operation 8 must be *settable*, not only readable — §9, requirement H5) and find the value at which mean retrieval fidelity matches the `VERIDICAL` reference cell at the same `r` and kind.
2. **Predeclared tolerance.** Matched means within `±0.02` on the fidelity scale **or** within one quarter of the pooled across-seed SD of fidelity, whichever is larger. Fixed before the confirmatory run.
3. **Match per replay count, not globally.** Fidelity trajectories can diverge with `r`; a single global match leaves the high-`r` cells unmatched, which is exactly where the interaction is read.
4. **Pin and freeze.** The confirmatory run uses the pinned parameters. Achieved match is written to the manifest per cell so a reader can audit it.
5. **Declared-in-advance exclusion.** If a cell cannot be matched within the parameter range, it is reported as unmatched and **excluded from the primary interaction test**, with the exclusion rule fixed before any interaction is computed.

**Prohibited:** selecting a fidelity-matched subsample after the run, or restricting the analysis to seeds whose realised fidelity happens to match. Retrieval fidelity is affected by the ancestry treatment, so it is a post-treatment variable; conditioning on it opens a collider path and can manufacture an interaction from nothing. A fidelity-as-covariate regression may be reported as a **clearly labelled secondary sensitivity analysis** only, never as the primary test.

---

## 7. Readouts, kept separate

Per audit §10, four readouts, reported separately and all four, at every cell:

```text
1. association strength                 (contract op 4)  -- did a relation form?
2. source attribution                   (contract op 5)  -- P(external | representation)
3. effective independent-source count   (contract op 6)  -- the cardinality variable
4. calibration against world truth      (contract op 7)  -- confidence vs realised H
```

Plus, in a distinct role: **retrieval fidelity** (contract op 8) — the §6 matching variable, *and* the §5 healthy-arm readout. It is used differently in each role and must be labelled accordingly in the manifest; it is not a fifth primary endpoint of the interaction test.

Optional secondary, carried from the ladder's P1 critical criterion: **additional-query demand**. Under H2 it should *fall* as replay count rises, since inflated confidence should reduce information-seeking. Reported, not gating.

### 7.1 Count and calibration are never derived from one another

Assay 001's own `N_eff` correction is well calibrated only at the topology endpoints and drifts between them (`shared_bias` +0.038 over-confident, `mixed` −0.027 under-confident). A count-derived confidence would bake that instrument error into the result.

### 7.2 The instrument-bias hazard specific to P3, and the fix

This is worse for P3 than for any other rung, and it is the design's most serious internal threat. As replay accumulates descendants of one lineage, the graph's dependence topology **moves** — from something near `independent` at `r = 0` toward something near `copies` at `r = 16`, passing directly through the `mixed` / `shared_bias` middle where the instrument is least trustworthy. **The manipulated variable moves the graph along the very axis on which the instrument's own bias is largest.** A monotone `N_eff` rise with `r` could therefore be instrument drift rather than amplification, and nothing in the raw readout distinguishes them.

The fix is to measure the instrument at the operating points the run actually visits:

1. **Instrument-bias ladder, measured in the same run.** Construct synthetic graphs of *known* true independent-source cardinality at each topology the replay trajectory passes through, read `N_eff` on them, and record the signed bias curve `bias(topology)`.
2. **Report both.** The raw `N_eff(r)` and the bias-corrected `N_eff(r) − bias(topology(r))` are both reported; the interaction test is predeclared on the corrected series, with the raw series shown alongside.
3. **True cardinality is read at every cell.** Contract operation 6 must be readable alongside the harness's known true independent-source count (§9, requirement H4), so the instrument's bias at that exact operating point is visible rather than interpolated from the ladder.

Without all three, a P3 positive is not separable from instrument drift, and should not be reported as a result.

---

## 8. Predeclared signatures and the falsifier

### 8.1 The dangerous signature (H2 supported)

```text
per replay kind, on P3-A, at matched retrieval quality, bias-corrected count:

  FALSE_SPLIT / ABSENT / SOFT :  count RISES with log2(1+r)
                                 confidence RISES
                                 calibration error GROWS
  VERIDICAL                   :  count FLAT
                                 confidence flat or slightly up
                                 calibration preserved or improved

  => a signed ancestry x log2(1+r) interaction on BOTH count and calibration error
```

Both must move. A count rise with calibration intact is not the hypothesis — it is an instrument reporting more sources without the belief following, which is a readout artefact or a reader that ignores its own count.

### 8.1a `P3-R8` — three routes to a replay-count effect, only one of which is H2 (tranche §6.2)

The dangerous signature above requires **both** count and calibration to move, which already excludes the confound named here. This section names it explicitly, gives it a literature anchor, and fixes its predicted signature in advance, because it is the reading a replay-count main effect will otherwise invite.

`P3-R2` (§5) covers the healthy route: replay improves fidelity, count flat. Corlett/Honsberger (§1.1) supply a **third** possibility that neither the dangerous signature nor the healthy arm was written to cover — replay raises confidence by *strengthening the representation*, with no ancestry involvement and no cardinality change, and does so **more** under conditions that model psychosis.

```text
strength route:      confidence up, effective source count FLAT, calibration DEGRADES
                     (Corlett/Honsberger analogue -- no ancestry variable)
cardinality route:   confidence up, effective source count RISES, calibration DEGRADES
                     (the branch's H2)
fidelity route:      confidence up, count flat, calibration IMPROVES
                     (healthy replay, P3-R2, sec 5)
```

The strength and fidelity routes are distinguished by **calibration direction** at flat count; the cardinality route is distinguished from both by **readout 3 moving at all**.

> **Predeclared, and binding: a replay-count main effect that raises confidence and degrades calibration is consistent with the strength route alone and is NOT evidence for H2.** It is admissible as evidence for H2 only via the signed ancestry × `log2(1+r)` interaction on **both** count and calibration error (§8.1).

Two further requirements this places on the run:

1. **The strength route must be reportable as itself.** It is a real result — a synthetic analogue of a documented human and rodent effect with a psychotomimetic link — and it must be recorded as the strength route rather than as an H2 null. `VERIDICAL` is the arm where it is cleanly visible, since ancestry is intact there by construction.
2. **Do not treat it as a nuisance to be regressed out.** Replay strength and replay count are the same manipulation; the separation is by *signature across readouts 3 and 4*, not by a covariate. A "controlled-for-strength" count effect is not a cleaner H2 test, it is a collider-conditioned one — the same prohibition §6 states for realised fidelity.

Boundary: Corlett 2013 and Honsberger 2015 are **design constraints and a named confound**, not evidence for H2 and not a psychosis inference. They measure memory strength, not cardinality and not calibration; the epistemic boundary of §11 applies to them unchanged, and the ketamine/psychotomimetic link is what makes the confound *plausible in this region*, not what licenses any clinical reading of a P3 result.

---

### 8.2 The other predeclared outcomes, each a real result

| Pattern | Reading |
|---|---|
| source attribution shifts with ancestry; count and calibration flat across `r` | **H0**, and per audit §11 still the most likely single outcome. Informative: it separates source monitoring from evidence cardinality, which the clinical literature has never done. |
| fidelity ↑, count flat, `VERIDICAL / rehearsal` | healthy replay. **Gate passed** (§5). |
| association ↑, count = 2, kind (b), distinct world events | E43 adaptive linking behaving correctly. |
| count ↑ in kind (b) with distinct world events | failure in the **opposite** direction — collapsing distinct sources. Must be reported, never scored as a pass. |
| calibration ↑, count unchanged, kind (c) | E30 / P1-R3 legitimate computation. Not the forbidden gain. |
| count ↑ with `r` in **every** ancestry condition including `VERIDICAL` | **instrument artefact — measuring replay exposure, not genealogy. STOP**, fix the harness, do not report. |
| amplification under `preferential` only | H2 in its self-maintaining form (§2.5). |
| amplification equal under `uniform` and `preferential` | H2 in its weak accumulation form only. |
| confidence ↑ with `r`, count FLAT, calibration DEGRADES, in **every** ancestry condition including `VERIDICAL` | **the strength route** (§8.1a) — a synthetic analogue of Corlett 2013 / Honsberger 2015. A real result, and **not** evidence for H2. Distinguished from the healthy-replay row above by calibration direction, and from H2 by readout 3 not moving. |
| P3-B delta ≈ 0 against matched P3-A | corruption does not compound with re-encoding; cardinality alone drives any effect. |

### 8.3 The falsifier

> **No ancestry × replay-count interaction, at fixed external evidence and matched retrieval quality, weakens H2.**

A null is only admissible as a falsifier if the design could have detected the effect. Two predeclared requirements:

1. **Minimum detectable interaction, with an absolute floor.** The PASS gate on the interaction is expressed both as a multiple of the across-seed SD of the per-seed slope delta **and** as an absolute floor on that delta — a difference of at least `0.25` effective sources per doubling of `r` between `FALSE_SPLIT` and `VERIDICAL`. A statistically significant interaction below the absolute floor is reported as a null. Both halves are fixed before the run.
2. **Seed count from the pilot.** The confirmatory seed count is chosen from the pilot's variance estimate to achieve the MDE above, and the *achieved* precision is reported alongside the null. A null with no reported precision is not a falsification.

---

## 9. Interface requirements on the harness

The sibling design `provenance_harness_generated_ancestry_design.md` owns the descendant-generation and genealogy representation and publishes a "Genealogy contract (for P3)". **That artifact did not exist when this was written** (checked 2026-09-10 against `REE_assembly/evidence/planning/`), so this design is written against the abstract eight-operation interface, and everything assumed is recorded here rather than resolved unilaterally. No competing representation is proposed.

### 9.1 What was assumed

The eight operations as stated: (1) create a descendant carrying an ancestry link; (2) degrade ancestry integrity as a *process*; (3) replay a descendant; (4) read association strength; (5) read source attribution; (6) read effective independent-source count; (7) read calibration against world truth; (8) read retrieval quality / fidelity of a descendant.

### 9.2 Sharpenings this design needs

Each is a refinement of an existing operation, not a new object. If the published contract already carries it, this section is satisfied by that; if not, it is the gap to close.

| # | Operation | Requirement | Why P3 fails without it |
|---|---|---|---|
| **H1** | 3 (replay) | takes a **`kind`** argument: `rehearsal` / `relational_link` / `prediction` | P3-R1 (§3). A single undifferentiated replay makes the main effect uninterpretable. |
| **H2** | 3 (replay) | takes a **`mode`** argument: `in_place` (improve the source node, add no node) vs `append` (create a descendant) | P3-R2 (§5). Without `in_place`, the healthy arm is unreachable **by construction** and P3 is unfalsifiable. **The highest-priority gap.** |
| **H3** | 3 (replay) | exposes a settable **selection policy** — `uniform` / `preferential` — rather than an internal default | §2.5. The selection policy is the only available feedback path, so H2's self-maintaining clause is untestable if it is hard-coded. |
| **H4** | 6 (count) | the **true** independent-source count, known to the harness, is readable alongside the estimate | §7.2. Otherwise the instrument's bias at each operating point is unmeasurable and a positive is not separable from drift. |
| **H5** | 8 (fidelity) | **settable as well as readable**, via an exposed retrieval-noise parameter | P3-R3 (§6). Prospective titration is impossible if fidelity can only be observed. **Most likely to be missing from a contract written from P1's needs alone** — P1 never has to match fidelity across conditions; P3 must. |
| **H6** | — (new, read-only companion to 1) | a **freeze primitive**: after `t0`, node creation is possible only as a descendant of an existing node; the world generator is not callable | §2.1. A leaked new observation produces a *correct* confidence rise that reads as amplification. Must be enforced, not conventional. |
| **H7** | — (new, companion to 3) | **separate RNG streams** for world generation and for replay | §4. Crossing treatments at matched world draws is otherwise impossible, and the design's power depends on it. |
| **H8** | 2 (degrade) | separable into (i) creation-time degradation of new links and (ii) optional re-encoding degradation of existing links | §2.4. Without the split, P3-A and P3-B cannot be distinguished and every interaction is confounded with cumulative corruption. |

### 9.3 Operation 8 specifically, as the chip flagged

Operation 8 (retrieval quality / fidelity) is what P3-R2 and P3-R3 both turn on, and it is the one a P1-derived contract is most likely to under-specify. P3 needs it to be **per-node, readable, settable, and on a scale on which "matched" is definable** (a bounded continuous scale with a documented reference, not an ordinal quality label). If the published contract exposes it only as a coarse or read-only quantity, §5's gate and §6's titration both fail, and the correct response is to close the gap in the harness rather than to weaken the matching requirement here.

### 9.4 Nothing else is needed

No operation beyond the eight and the two read-only companions (H6, H7) is required. In particular this design does **not** need a lineage-identifier scheme, an ancestry query language, or a genealogy serialisation format — those are the harness's to choose, and P3 is indifferent between any that satisfy H1–H8.

---

## 10. Feasibility verdict

In the work-graph debt vocabulary:

- **The assay build: `complicated (buildable)`.** It is a synthetic assay in the same family as convergence-signal assays 001–006, with no unknown blocking it. The statistics are standard, the cell count is large but each cell is cheap, and every readout already exists in some form in assay 001.
- **The instrument-bias ladder (§7.2): `complicated (buildable)`.** Constructing known-cardinality graphs at the visited topologies and measuring the bias curve is ordinary work; it is only load-bearing, not hard.
- **The one gated precondition: `complex (probe-gated)` — the P3-R2 reachability spike (§5).** Whether the healthy-replay arm can pass depends on whether the harness supports `mode = in_place` (requirement H2), which is not yet decided by anyone. The probe is small and well-defined: one cell, `VERIDICAL / rehearsal / in_place`, pilot seeds, check fidelity ↑ with count flat. Its outcome routes as follows — spike passes → the whole rung reduces to `complicated (buildable)`; spike fails → `puzzle (known rules)`, because the missing fact is a harness capability that can simply be added, not a reframing.
- **Not owned here:** the genealogy representation itself is the sibling chip's, and is `complicated (buildable)` on its side.

**Overall: `complicated (buildable)`, behind one `complex (probe-gated)` precondition.** The correct next step is the §5 spike, not the confirmatory grid.

---

## 11. Epistemic boundary

- **P3 is not a psychosis model, and no psychosis inference is drawn from any synthetic or rodent result here.** The audit's §12 records that the judgment-class finding is *deflationary* for the psychosis framing: treating one lineage as several independent witnesses is a documented healthy-human default under ancestry ambiguity (Yousif 2019; Connor Desai 2022; Weaver 2007), not a clinical signature. P3 tests an **architectural hypothesis about recurrent evidence reuse** — whether an inference system that reuses its own products accumulates evidential weight it has not earned.
- **The rodent sources are design constraints, not evidence for the hypothesis.** E20, E30, E32, E42 and E43 constrain what a replay operation is, supply the healthy-replay and adaptive-linking controls, and name the rival for P6. None of them supplies a cardinality or calibration readout, because no rodent preparation can. The direction of travel is one-way.
- **The C6 result, if positive, is a statement about a synthetic architecture.** It would establish that recurrent reuse of one's own descendants can inflate evidential cardinality in an inference system — which is the engineering rule the branch already holds (*a hypothesis must not cite its own descendants as independent witnesses*), given a quantitative demonstration and a mechanism. It licenses no clinical claim.

---

## 12. Recommendations to the ladder and supplement

Written here as recommendations only — this document does not edit either file.

1. **Ladder, P3.** The rung as written specifies the replay counts and the crossing with provenance condition but not replay *kind*, *mode*, or *selection policy*. All three are load-bearing (§3, §5, §2.5) and one of them (`mode`) determines whether the rung is falsifiable at all. Recommend the P3 section carry them.
2. **Ladder, P3.** Recommend the accumulation/compounding split (§2.4) be named in the rung, since running only the compounding form yields a confounded result that looks like a clean one.
3. **Supplement, §8.** P3-R2 is stated as "the healthy-replay arm is mandatory and must be able to pass". Recommend it be strengthened from an arm to a **gate run first on discarded seeds** (§5) — as an arm assessed after the fact, a failure is discovered only once the grid has run and been interpreted.
4. **Supplement, §10.** Recommend the instrument-bias hazard specific to P3 (§7.2) be recorded: the replay manipulation moves the graph along precisely the topology axis where assay 001's `N_eff` instrument drifts, which is a sharper problem for P3 than the general "do not derive one readout from the other" caution already stated.
5. **Sequencing.** Recommend it be stated explicitly that P3 is harness-dependent but not result-dependent on P1 (§1), so that a P1 null does not silently retire the rung.
6. **Supplement, §4 (Break B).** Recommend the "no evidence in any direction, in any class" formulation be narrowed to **"no evidence for cardinality in any class"** (§1.1). A reactivation-strengthens-memory result exists in humans and rodents with a psychotomimetic link; the cardinality half of Break B is untouched by it, but the unnarrowed sentence is false as written.
7. **Ladder / supplement, P3 controls.** Recommend `P3-R8` (§8.1a) be carried: the three-route separation, and the binding predeclaration that a replay-count main effect on confidence and calibration at flat count is the **strength** route and is not evidence for H2.

---

## Compact statement

> Freeze the world at `t0` and let the system rehearse. If belief in `H` climbs with the number of times the system has re-examined its own products — while no new observation has arrived, retrieval quality is matched, and the count instrument's own drift has been subtracted — then reuse has been converted into evidence. The rung is worth running because nothing, anywhere, has looked: no assay contains a replay loop, and no literature measures cardinality across cycles.
