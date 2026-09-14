# Failure Autopsy: V3-EXQ-861i (staging draft -- awaiting human confirmation)

**Status: AWAITING HUMAN CONFIRMATION.** This is a staged /failure-autopsy draft written by a headless session. Nothing here has been applied to `claims.yaml`, `substrate_queue.json`, or `hypothesis_space_registry.v1.json`. Routing is drafted, not finalised, per the skill's staging-mode rules. The confirming interactive session (or the next `/governance` walk) must run the Step 8 interactive gate before anything below is applied.

- **Run**: `v3_exq_861i_inv050_mech091_commit_attribution_pinned_confirmation_20260914T121029Z_v3`
- **Queue**: V3-EXQ-861i
- **Claims**: INV-050, MECH-180 (peripheral co-tag -- see below)
- **Purpose**: diagnostic (evidence_direction pinned `non_contributory` regardless of outcome)
- **Outcome**: PASS (label `mover_6293b23_confirmed_full_protocol_reproduces_recorded`)
- **Machine**: ree-cloud-2, linux-x86_64-py3.10-torch2.12.0+cpu
- **Generated**: 2026-09-14T22:03:20Z

## 1. What this run is

V3-EXQ-861i is the closing confirmation of a multi-run diagnostic portfolio (861e -> 861f/861g/861h -> 861i) investigating why V3-EXQ-861e's seed-271 `ARM_3_HIGH_ON` MEL `mean_duration_factor` collapsed from a recorded 1.007 (861g, historical substrate `f810969`) to 0.884 (861e, current substrate `17befb8c`). That portfolio's frozen hypothesis-space question (`qid inv050_mech180_861e_producer_vs_intervention_isolation`) is already fully resolved: H1 (measurement-RNG confound) eliminated by 861f, H3 (substrate/machine delta) confirmed by 861g+861f. The qid's own decision block explicitly scoped the residual **"WHICH of the 11 intervening ree_core commits is responsible"** question OUT of the frozen hypothesis set and into a substrate_queue entry instead -- an entry (`mel-f810969-vs-17befb8c-collapse-bisection`) that, per this autopsy's own check, was **never actually created**.

That residual question was instead answered by a separate desk bisect (`REE_assembly/evidence/planning/inv050_reecore_bisect_20260911.md`), which replayed 861e's agent+env as a short wake-only rollout against every commit in `f810969..17befb8c` and found one clean bitwise divergence point: **`6293b23`** ("MECH-091: wire task-completion and commitment-boundary-crossing triggers into `phase_reset()`"), excluding the standing alternative candidate `76cbf84` four independent ways. The bisect explicitly did not run training, calibration, or sleep -- so it could localise the divergence on the wake path but could not attribute the recorded 0.884 factor to it under the full protocol. **V3-EXQ-861i is that full-protocol confirmation.**

## 2. Design and facts (Step 2)

Four pinned cells, one child subprocess per pin (the parent never imports `ree_core`, so `substrate_pin`'s already-imported guard cannot silently no-op):

| cell | ree_core pinned to | role |
|---|---|---|
| ANCHOR_PRE_f810969 | `f810969` (861c/861g) | in-run anchor, pre-range endpoint |
| PIN_A_5f64a53f | `5f64a53f` (6293b23's parent) | commit boundary, before |
| PIN_B_6293b23 | `6293b23` | commit boundary, after |
| ANCHOR_POST_17befb8c | `17befb8c` (861e) | in-run anchor, post-range endpoint |

Decisive readout: `mean_mel` and `mel_reference` per cell over 6 measurement cycles; `D(x,y) = max(reldiff(mean_mel), reldiff(mel_reference))`, `reldiff(a,b) = |a-b|/max(|a|,|b|,1e-30)`.

**Recomputed independently (Step 7c red-team) directly from the manifest's `attribution.cells` block -- exact match to the manifest's own `readout`:**

| comparison | value | vs threshold |
|---|---|---|
| P1 D(ANCHOR_PRE, ANCHOR_POST) | 0.11153316700714966 | >= 0.01 floor (11.15x) -- **met** |
| C1 D(PIN_A, ANCHOR_PRE) (load-bearing) | 0.0 (bitwise equal) | <= 1e-4 -- **met** |
| C2 D(PIN_B, ANCHOR_POST) (load-bearing) | 0.0 (bitwise equal) | <= 1e-4 -- **met** |
| C3 D(PIN_A, PIN_B) (qualifier) | 0.11153316700714966 | > 1e-4 -- boundary cells correctly NOT equivalent |
| C4a D(ANCHOR_PRE, recorded 861g n10) (qualifier) | 0.0 | <= 1e-4 -- **met** |
| C4b D(ANCHOR_POST, recorded 861e) (qualifier) | 0.0 | <= 1e-4 -- **met** |
| C5 grading split (qualifier) | factor(A)=1.0070 > 1.0, factor(B)=0.8845 < 1.0 | **met** |

Combination rule: PASS iff P1 AND C1 AND C2. All three met -> **PASS**. C4 also met -> stronger tier: the RECORDED 861g/861e values (not just this run's own anchors) are reproduced, so the RECORDED 0.884 collapse -- not merely an in-run analogue of it -- is what gets attributed to 6293b23.

**Recording completeness**: `validate_recording.py` reports the manifest complete -- always-core fields present (`recording_schema`, top-level `substrate_hash`, `machine`/`machine_class`, `elapsed_seconds`, full `config`, explicit `seeds`), 0 gaps, 0 schema warnings.

**Dry-run check**: `check_dry_run_citations.py` over the target run and both cited recorded-anchor runs (861e, 861g n10) -- 0 dry, 3 clean.

**Pin verification (three independent checks per cell, all fatal on failure)** -- cross-checked three ways (driver docstring's marker-chain table, the manifest's own `pin_verification` block, and a direct Step 7c red-team `git show` at all four refs): all three sources agree on every cell, zero missing/extra/altered files (123 `.py` files per pin), `6293b23`'s sole parent is `5f64a53f` (`git log --format=%p`).

| ref | MultiArchive | agent.py phase_reset() lines | authority_spread_ratio |
|---|---|---|---|
| f810969 | absent | 1 | absent |
| 5f64a53f | present | 1 | absent |
| 6293b23 | present | 6 | absent |
| 17befb8c | present | 6 | present |

**Disclosure (Step 7c finding, not in the original manifest/driver output):** the parent process's live checkout advanced through four distinct commits during the 4486.65s run (the runner's auto-sync pulling `main` between the four child-process pins) -- load-bearing for the driver's own "same live harness across all four cells" design premise (docstring "WHY FOUR AND NOT TWO"). Verified harmless by content: `git diff --stat` across the full window touches no harness file (`experiments/_lib`, `experiment_protocol.py`, `experiments/pack_writer.py`, this driver itself) -- only unrelated drivers, contract tests, docs, and `ree_core` (which is pinned per-child and therefore irrelevant). The bitwise C1/C2/C4 results are also an empirical confirmation that harness identity held. Flagged for the driver's next revision to state explicitly; not a defect in this result.

## 3. Claim-layer mapping (Step 3) and biological triage (Step 4)

**INV-050** (invariant, emergent from SD-017, status candidate, epistemic_category standard) and **MECH-180** (mechanism_hypothesis, status candidate/v3_pending, epistemic_category standard) are tagged on this run purely for lineage continuity with the 861e/f/g/h portfolio. The driver's own docstring is explicit: *"WHAT A PASS DOES NOT MEAN: nothing about INV-050 or MECH-180 as claims... Neither claim's status, confidence or v3_pending may move on this run."* This is a code-provenance/commit-attribution question, not a biological-mechanism test -- no biological reference, no lit-pull applies, and both claims are a **peripheral co-tag** (`recommended_epistemic_category_per_claim: standard/standard`, `recommended_evidence_direction_per_claim: unknown/unknown`, matching the manifest's own pinned directions and identical to every predecessor in this lineage: 861b/861e/861f/861g/861h).

## 4. Four-layer diagnosis table (Step 5)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | pure provenance diagnostic; claim not exercised (peripheral co-tag) |
| Biological reference | n/a | instrumentation question, not a mechanism test |
| Prerequisites | present | P1 met 11x over floor; all 4 pins verified 3 ways, cross-checked a 4th way by red-team |
| Implementation | complete | subprocess-per-pin isolation correct; mid-run checkout drift disclosed and verified harmless |
| Environment | n/a | fixed decisive cell reused verbatim by design |
| Measurement | adequate | tolerance 1000x below effect, above only-ever-measured cross-machine-class noise; bitwise cross-check agrees |
| Integration | n/a | |
| Scale | n/a | |

**GOV-FAILLOC-1 failure-location**: not applicable -- this diagnostic does not evaluate REE's organism-level competence, mechanism completeness, or environment adequacy in any sense that table covers. `ree: false`, all three buckets `not_applicable`.

**Granularity-debt recurrence check** (`scripts/granularity_debt_cluster.py`, run 2026-09-14): MECH-180 -- 11 prior targets, alignment `unclear=8, intact=2, strengthened=2, other=1`, no target reads `weakened`. INV-050 -- 10 prior targets, alignment `unclear=8, intact=4`, no target reads `weakened`. **Trigger does NOT fire** for either claim; this is measurement/instrumentation debt, not granularity debt.

**Re-derive brake**: recommended_epistemic_category is `standard` for both claims (never `substrate_ceiling`), so R1-R3 counts do not advance. Consistent with the queue entry's own authoring-time disclosure (literal counter INV-050=7, MECH-180=5, released under the diagnostic "tests no claim hypothesis" clause already invoked by 861e/861f/861g/861h). **Brake does not fire.**

## 5. Learning extracted and repair pathway (Step 7)

1. **Commit attribution confirmed**: the recorded 861g-to-861e seed-271 `ARM_3_HIGH_ON` `mean_duration_factor` collapse (1.007 -> 0.884) is attributable in full to `6293b23`, under the full protocol, closing the 861e/f/g/h portfolio's residual open question.
2. `76cbf84` is excluded **over-determinedly**: its repair gates entirely on `contextmemory_write_usage_balancing` (default-off, never passed by any 861-family run), so it could not have moved this readout regardless of what any bisect or run measured. The 861f-cluster's "inversion candidate" reading does not hold, and was ill-posed against the actual config, not merely disconfirmed.
3. The 861f-cluster's `recommended_substrate_queue_entry` (`create`, `mel-f810969-vs-17befb8c-collapse-bisection`) was **never applied** -- absent from `substrate_queue.json` in HEAD and across its entire git history (`git log -S` on the sd_id, `f810969`, `17befb8c` all return zero commits). It is now **moot**: answered by a direct diagnostic path instead. **Governance should mark it superseded-by-direct-diagnosis, not create it**, and should update the qid's `decision.distance_phrase` to name V3-EXQ-861i as the answer rather than pointing at the never-created entry.
4. `claims.yaml` carries **no `diagnostic_evidence_adjudicated` field at all** on either INV-050 or MECH-180 (confirmed absent from both full claim blocks), despite a diagnostic-heavy lineage whose runs already carry governance stamps in both claims' `evidence_quality_note`. This is a claim-level field (adjudicates the claim's whole diagnostic-zero status, not a per-run entry) -- this artifact's recommendation to set it `true` now discharges that gap for the lineage as a whole.
5. Two facts already recorded in the lineage's own manifests (not new measurements by this run) temper how strongly 861e's "collapse" framing should be read: (i) the `f810969`->`17befb8c` factor delta is seed-**dependent in sign** (up for seeds 7 and 883, down only for seed 271) -- not a systematic MEL suppression; (ii) within `f810969` alone, raising calibration draws from 5 to 10 shifts seed 271's own HIGH `mean_mel` by 10.7%, the same order of magnitude as the 11.2% cross-commit "collapse". Seed 271 at this operating point sits within ordinary RNG-realisation noise of the factor=1.0 grading line. `6293b23` is nonetheless a genuine behavioural change (four new `phase_reset()` call sites, altering the RNG draw sequence per its own commit message), so "realisation shift" and "mechanism change" remain entangled in principle -- the standing `pending_retest_after_substrate` on both claims remains the correct owner of resolving that, not this run.
6. Mid-run live-checkout advance (Step 7c finding) -- verified harmless, flagged for the driver's next revision to disclose.

**Repair pathway**: none. This is a `puzzle (known rules)` node that a targeted spike (the desk bisect + this pinned confirmation) already resolved -- "just build it" does not apply (nothing to build), and neither does a re-queue (the question is answered, not open). **Routing: none** -- diagnostic closed, no further action owed from this target. The residual items above (861f substrate_queue moot-marking + qid distance_phrase update, corpus-wide `diagnostic_evidence_adjudicated` gap, standing pending_retest) are noted for governance, not routed as follow-on work from this artifact.

## 6. Step 7b -- mechanical pre-routing checks

`autopsy_pre_routing_checks.py` fired **1** check: **C2** -- three existing substrate_queue entries (SD-MEL-CONSUMER, SD-MEL-PRODUCER, MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION) already unblock INV-050/MECH-180 and were not mentioned. **Dismissed**: this target's `recommended_substrate_queue_entry.action` is `none`, so C2-strict (matching against a recommended `create`/`amend`) has nothing to match -- the fire is claim-keyed noise. Step 7c independently grepped all three entries for every run_id/commit-sha/metric term in this artifact and found nothing stale or owed.

## 7. Step 7c -- adversarial red-team pass

Run on a **different model** from the drafting session (drafting session: Sonnet 5; red-team: Fable 5.1), per the skill's cross-model requirement, with reasoning withheld from the reviewer until after it independently recomputed the load-bearing numbers and cross-checked the pin-verification chain against raw git state.

**Verdict: CONFIRMED. 0 contests.** Every load-bearing number recomputed exactly from the manifest's own cells; the marker chain is consistent three ways (docstring, manifest, git); all four pins verified with zero content drift; the PASS label is the correct tier under the driver's own grid. Both absolutes stress-tested ("attributable in full to 6293b23", "76cbf84 definitively excluded") held up -- the second turned out to be over-determined. "Never applied to substrate_queue.json" verified true in HEAD and full git history. `diagnostic_evidence_adjudicated` confirmed genuinely absent from both claim blocks by line-number grep. The `routing: none` decision confirmed correct.

Seven hygiene findings (H1-H4, O1-O3) were surfaced -- none moved the verdict off CONFIRMED, all have been folded into the final artifact above (mid-run checkout disclosure, a file-count typo, the diagnostic_evidence_adjudicated per-run/per-claim framing correction, the strengthened 76cbf84 exclusion, the seed-dependent-sign and RNG-consumption-magnitude facts, confirmation that the Step 7b C2 dismissal is sound, and a note that the hypothesis-registry qid text will need a follow-up edit once governance marks the 861f entry superseded).

## 8. Growth-restriction check / hypothesis-space ledger (Step 9b) -- not applicable, reasoning recorded

This run does not adjudicate a leg of `qid inv050_mech180_861e_producer_vs_intervention_isolation` (already fully decided; its own decision block scoped the "WHICH commit" question out to a substrate_queue entry that was never created) and is not a discrimination among live rival hypotheses (the desk bisect had already isolated one candidate, excluding the only other one, before this run was queued). `growth_restriction` on that qid is `null` in any case. No hypothesis-space write is made; the reasoning is recorded in the JSON's `hypothesis_space_ledger_pending` for the confirming session or governance to override if read differently, alongside a registry-hygiene note (update the qid's `decision.distance_phrase`).

## 9. Recommended disposition (drafted, not applied)

- **INV-050 / MECH-180**: `evidence_direction` per-claim `unknown` (unchanged), `epistemic_category` `standard` (unchanged), status/confidence/v3_pending **unchanged**. Set `recommended_diagnostic_evidence_adjudicated: true` for both (field currently absent entirely). Citation stamp: `failure_autopsy_V3-EXQ-861i_2026-09-14`.
- **Substrate queue**: no action. Note the 861f-cluster's unapplied, now-moot `create` recommendation for governance to mark superseded.
- **Hypothesis-space registry**: no write. Registry-hygiene note only (qid `decision.distance_phrase` update).
- **Re-derive brake**: not fired for either claim.
- **Granularity-debt trigger**: does not fire for either claim.

**Next step**: the Step 8 interactive gate is owed before any of the above is applied -- present this draft to the user (or the next `/governance` walk) for confirmation, per staging-mode rules.
