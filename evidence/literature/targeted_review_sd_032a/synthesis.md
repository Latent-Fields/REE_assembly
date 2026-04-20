# SD-032a Targeted Literature Review -- Salience-Network Coordinator

**Claim:** SD-032a (salience-network coordinator; `ree_core/cingulate/salience_coordinator.py`).
**Entries:** 5.
**Pull date:** 2026-04-20.
**Mean confidence:** 0.796.

## Scope

This pull targets SD-032a specifically -- the salience-network coordinator substrate that aggregates dACC PE bundle + drive_level + offline-state into an `operating_mode` soft probability vector over {external_task, internal_planning, internal_replay, offline_consolidation} and emits a MECH-259 `mode_switch_trigger`. The parent SD-032 directory (`targeted_review_cingulate_integration_substrate/`, 9 entries) grounds the overall cingulate-integration substrate; this directory zooms in on the coordinator role specifically.

## Entries

1. **Sridharan, Levitin & Menon 2008** (PNAS) -- Granger-causal evidence that right fronto-insular cortex + dACC causes CEN/DMN switching. Foundational. Confidence 0.85.
2. **Goulden et al 2014** (NeuroImage) -- Independent DCM replication of Sridharan's finding. Confidence 0.78.
3. **Menon 2011** (Trends Cogn Sci) -- Triple-network model; SN as coordinator of CEN/DMN; transdiagnostic dysfunction signature. Confidence 0.78.
4. **Uddin 2015** (Nature Rev Neurosci) -- Insular cortex as multimodal salience integration hub. Confidence 0.80.
5. **Molnar-Szakacs & Uddin 2022** (Neurosci Biobehav Rev) -- AIC as gatekeeper of executive control; primacy-of-action framing. Confidence 0.77.

## Architectural license

Together, the five entries license SD-032a's architectural design at four levels:

- **A coordinator substrate exists in biology.** Sridharan 2008 + Goulden 2014 (two methodologically independent causal-inference studies).
- **The coordinator is load-bearing for transdiagnostic function.** Menon 2011 (triple-network psychopathology frame).
- **The coordinator integrates multimodal signals.** Uddin 2015 (insular integration of interoceptive + exteroceptive + cognitive saliency).
- **The coordinator is upstream of downstream reconfiguration.** Molnar-Szakacs & Uddin 2022 (primacy of action; gatekeeper).

## What the literature does NOT constrain

- The **specific aggregation rule** (softmax-over-affinity-logits is an ree-v3 design choice).
- The **four-mode discretisation** (external_task, internal_planning, internal_replay, offline_consolidation -- extends the biological two-network frame).
- The **hysteresis-based discrete-switch mechanism** (biology is observed in graded BOLD; the discrete-switch formulation is an implementation choice).
- The **tick-per-action integration** (biological coordinator operates on BOLD timescales; ree-v3 ticks per action).

These remain in scope for the V3-EXQ-446 validation experiment, which will test whether SD-032a's specific computational form produces the expected substrate signature (ablation to fixed external_task abolishes coordinated mode switching without affecting within-mode computations).

## Mapping rule of thumb

Treat these five papers as licensing the existence and architectural position of SD-032a -- not as biologically mandating its specific internal computation. The V3-EXQ-446 outcome is what tests whether the design decisions survive contact with data.
