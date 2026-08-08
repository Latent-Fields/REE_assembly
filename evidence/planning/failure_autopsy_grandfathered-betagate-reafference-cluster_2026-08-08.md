# Failure Autopsy: MECH-090/MECH-098/MECH-102/ARC-016 cluster (40 nominal / ~35 deduped, 4 threads)

**Generated:** 2026-08-08T17:37:36Z
**Scope:** cluster (4 independent threads, 2026-03-19 to 2026-05-08)
**Status:** confirmed (Step 8 interactive gate: user confirmed closure for 3 threads, `/implement-substrate` for MECH-098)

## Global finding

Three of four threads already substantially adjudicated: **ARC-016** by a 2026-07-25 `/claim-synthesis` rescore (nearly the whole population re-stamped `non_contributory`/superseded/mis-scoped); **MECH-102** by two confirmed cluster autopsies (`V3-EXQ-032-family`, `V3-EXQ-059c-533`); **MECH-090** by its own evidence_quality_note narrating the 048->049e bug-fix lineage as already fully resolved. **MECH-098 has zero prior formal autopsy content** and zero re-derive-brake hits ever -- this is the thread where the batch genuinely is the operative evidence.

## Deduplication and dry-run gate

40 nominal -> ~35 distinct runs: 2 exact prefix/suffix naming duplicates (048, 049), 2 byte-identical runner re-emission groups (`110` x3 -> 1, `079`/`080`-depletion pair -> 1). All 40 confirmed clean (`dry_run: false`); `v3_exq_059_arc016_beta_gate_fixed_threshold` already confirmed-autopsied in `failure_autopsy_grandfathered-superseded-batch1_2026-08-08.json`; `396a` x3 already confirmed inside `V3-EXQ-032-family`.

## Thread A -- MECH-090 (BetaGate), 9 distinct runs

Progressive bug-fix lineage 048->048b->049->049b->049d, already fully narrated in `MECH-090.evidence_quality_note` and resolved by EXQ-049e (PASS, not in batch -- "MECH-090 fully confirmed"). Root-cause chain: gate bypassed -> variance not populated on inference path -> fixed but over-corrected -> resolved by a two-condition redesign. 062/062a (surprise gate) and 321/321a (bistable gate) are later, distinct redesigns, already corroborated (062b PASS) or self-diagnosed (321: `total_committed_steps=0`, precondition unmet). **119 and 321a flagged as needing an individual read not covered by the existing note** -- recommended for a future session, not blocking this closure.

**Routing**: `governance-note-only` for 048/048b/049/049b/049d/062/062a (cite existing narrative). 321 already correctly self-stamped precondition_unmet. 119/321a flagged for later individual review.

## Thread B -- MECH-098 (reafference), 6 distinct runs -- THE FRESH FINDING

**Structural finding, source-confirmed**: all available driver scripts (069, 082, 099a, 110, 529, 099) call **only `agent.sense()`** in their training loops -- zero `act()`/`act_with_split_obs()`/`record_transition()` calls anywhere. Same convention-class defect already diagnosed in `V3-EXQ-032-family` for E1/E2-self tick-omission. For MECH-098 this produces a genuinely undertrained `ReafferencePredictor`:
- **099a**: self-diagnoses `R2_test=-0.0274` against a `threshold=0.70` -- "requires a higher-quality predictor before the discriminative test is meaningful."
- **069**: predictor R2=0.3389 clears its own weak bar, but core selectivity criterion still fails.
- **082**: interpretation text hypothesizes "the implicit E2 training signal is insufficient to train the ReafferencePredictor."

**This is likely one structural property, not 6 independent bugs** -- an undertrained self-motion predictor from a sense()-only training-loop convention, running 03-23 through 05-06 (~1.5 months) without ever fixing the underlying gap.

**Routing (confirmed): `/implement-substrate`** for the training-loop convention across the reafference-predictor family (wire `act()`/`record_transition()` into the loop or otherwise give the predictor a real optimizer step) -- `epistemic_category: competence_implementation_gap`, not `substrate_ceiling` (this is fixable, not an information ceiling). Check at write time whether the `V3-EXQ-032-family` autopsy's substrate_queue entry already covers this (amend, not create). This is the one thread where granularity-debt/recurrence does NOT fire (0 targets ever `weakened` formally -- this is the first `weakened`-capable formal read).

## Thread C -- MECH-102 (depletion ordering / terminal correction), 4 distinct runs + 059 mini-thread

**Correction to task framing**: MECH-102 is NOT "resource depletion/energy homeostasis" -- claims.yaml states the claim is **"Violence as terminal error-correction mechanism"** (ethics domain; frustration-aggression theory, Berkowitz 1989; General Aggression Model, Anderson & Bushman 2002; Axelrod 1984; Aloyo 2015 just-war-as-last-resort). "Depletion" refers to coordination-*option* exhaustion, not energy reserves. Nearest biological reference is aggression/frustration circuitry, not hypothalamic homeostasis.

**Structural finding**: `080`/`083`/`123`/`059`-triple all share the identical sense()-only defect diagnosed for the `032` family -- **this autopsy extends the already-known finding's scope beyond what the 07-26 autopsy covered** (it flagged `059c` as unverified for `533`; this read now independently confirms `080`/`083`/`123`/`059`-triple also share it).

**Routing**: extend the `V3-EXQ-032-family` cluster reading (`competence_implementation_gap`), `amend` not `create` a substrate_queue entry. `governance-note-only`. Note the biological-reference correction explicitly in the write-up.

## Thread D -- ARC-016 (precision commitment) + SD-010/SD-011 satellites, 9 distinct runs

Already adjudicated by the 2026-07-25 rescore. Two distinct failure mechanisms, both correctly excluded: (1) 088/100/101 mis-scoped to ARC-029 (a 2026-03-22 claim split); (2) 396a/396b/454/454a/530/530c -- train-vs-eval variance mismatch, the eval-time commitment threshold never engages under the tested harness. 530/530c additionally found `agent.update_residue()` never called in the driver loop. Campaign never closed the eval-time engagement gap within this batch (spans 03-23 to 05-08) -- only the later, non-batch `v3_exq_818` (2026-07-25) achieved it, driving the provisional->stable promotion.

**Routing**: `governance-note-only` for the whole cluster, formalizing the existing rescore. Fold `396b` into `V3-EXQ-032-family` via `amend` (shares its identical mechanism, never individually confirmed by name). Consider a `recommended_substrate_queue_entry` note for 530's specific `update_residue()` finding if not already captured.

## Re-derive brake state (R1-R3)

MECH-090: 7 hits (brake long fired, all from later unrelated autopsies, none from this batch). MECH-098: 0 hits. MECH-102: 0 hits (`competence_implementation_gap`/`measurement_test_design_defect` only -- correctly NOT `substrate_ceiling`, deliberately reclassified 2026-06-18). ARC-016: 0 hits. None of this batch's 40 runs are themselves counted `substrate_ceiling` hits anywhere.

## Recommended routing summary

- **Thread A**: `governance-note-only`, cite existing narrative; 119/321a flagged for future individual read.
- **Thread B**: **`/implement-substrate`** for the shared training-loop defect (not chipped, recorded for `/governance` Step 2b ratification).
- **Thread C**: `governance-note-only`, extend `V3-EXQ-032-family`'s scope (`amend` substrate_queue), correct biological-reference framing.
- **Thread D**: `governance-note-only`, formalize the 2026-07-25 rescore, fold `396b` into the existing cluster.

## Learning extracted

1. MECH-098's reafference-predictor lineage is the batch's genuinely fresh finding: zero prior autopsies despite 1.5 months of iteration, and a clean, source-verified structural defect (sense()-only training loop).
2. MECH-102's biological reference was mis-assumed (energy/depletion) by this autopsy's own initial task framing -- corrected to aggression/frustration theory. A reminder that experiment-name keywords ("depletion") can mislead about the actual claim domain.
3. Thread C's structural finding extends the scope of a prior confirmed autopsy (`V3-EXQ-032-family`) beyond what it originally covered -- worth a governance note rather than a fresh cluster file.
4. Threads A/D are both cases where a formal artifact's main value is citing and formalizing already-correct governance prose, not fresh diagnosis.
