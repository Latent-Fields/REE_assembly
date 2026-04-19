# MCC / dACC Effort-Value Literature Pull — Synthesis

**Date:** 2026-04-19.
**Focus:** fleshing out SD-032b (dACC / aMCC-analog adaptive control) — the minimum-viable node in the cingulate integration substrate cluster (SD-032). Extends the initial cingulate lit-pull beyond Scholl/Kolling 2015 into the Rushworth-lab effort-value line and the Shenhav/Botvinick EVC line.
**Entries:** 5.

## Entries summary

| Paper | Core claim | Role for SD-032b |
|---|---|---|
| [Kolling 2012 Science (10.1126/science.1216930)](entries/2026-04-19_mcc_foraging_value_kolling2012/) | dACC encodes foraging-environment average value + search cost, in invariant reference frame | Positive hypothesis: SD-032b output should include an *environment-average-value* register |
| [Shenhav 2013 Neuron (10.1016/j.neuron.2013.07.007)](entries/2026-04-19_mcc_expected_value_of_control_shenhav2013/) | dACC computes Expected Value of Control: payoff − control-required × effort-cost | Computational specification: SD-032b output = EV_net(mode) for each candidate mode |
| [Shenhav 2016 CABN (10.3758/s13415-016-0458-8)](entries/2026-04-19_mcc_choice_difficulty_shenhav2016/) | dACC activity is better explained by *choice difficulty* than by foraging value specifically | Disciplining counter-weight: SD-032b must ALSO emit a difficulty/entropy signal |
| [Croxson 2009 J Neurosci (10.1523/JNEUROSCI.4515-08.2009)](entries/2026-04-19_mcc_effort_cost_benefit_croxson2009/) | dACC encodes reward × effort *interaction*; striatum encodes *net value* | Architectural separation: SD-032b does integration, not selection |
| [Scholl 2017 PLoS Biol (10.1371/journal.pbio.2000756)](entries/2026-04-19_mcc_serotonin_effort_learning_scholl2017/) | SSRI enhances reward AND effort learning signals (valence-independent gain control) | MECH-260: neuromodulatory gain on SD-032b learning rate prevents monostrategy lock-in |

## Where the field actually agrees (the load-bearing findings for ree-v3)

Across five papers, three architectural facts are strongly supported:

1. **dACC integrates reward and cost, it does not select.** Croxson 2009 dissociates this cleanly: ventral striatum emits net value, dACC emits the reward × effort interaction. This matters for ree-v3 because the initial cingulate lit-pull treated SD-032b as both integration and final decision. It should not. SD-032b's output is the integration term; the final mode selection happens in SD-032a (salience-network coordinator) reading SD-032b's signal along with other inputs.

2. **Cost is a first-class variable, not derived from reward.** Across Croxson, Kolling, Shenhav, and Scholl, effort/cost enters the dACC computation as its own term, not as a subtraction from reward. ree-v3 implementations that collapse cost into a single "discounted reward" scalar will not match biological dACC behaviour.

3. **The computation is neuromodulator-tunable.** Scholl 2017 shows serotonergic tone modulates the effort-learning gain. Whatever SD-032b outputs, its parameters (particularly learning rates) must be exposed to a system-state modulator; otherwise the agent will lock into monostrategy when the learning rate collapses.

## Where the field disagrees (the unresolved hypothesis space for SD-032b)

The central live debate is: **does dACC output foraging-value or expected-value-of-control or choice-difficulty?**

- Kolling 2012 says foraging-value.
- Shenhav 2013 says EVC.
- Shenhav 2016 re-analyses Kolling and says choice-difficulty explains more variance.
- Croxson 2009 pre-dates the debate and is compatible with all three.

This is *not* resolved, and ree-v3 should not pretend it is. The honest design response is a pluralistic specification: SD-032b emits multiple signals, not one, and later experiments will tell us which signal was doing the work.

**Recommended SD-032b output specification (multi-signal):**

```
SD-032b output = {
    mode_ev[M]:         # per candidate mode M
        expected_payoff(M)
        - control_required(M) * effort_cost,    # EVC decomposition (Shenhav 2013)
    mode_foraging_value:
        EV(search/switch) - EV(stay),           # Kolling 2012 signal
    mode_choice_difficulty:
        entropy(softmax(mode_ev)),              # Shenhav 2016 signal
    integration_signal:
        mode_ev[M_current] * z_harm_a,          # Croxson 2009 interaction signal
    learning_rate_gain:
        f(sd012_drive, modulator_state),        # Scholl 2017 neuromodulation
}
```

Several of these signals are redundant in most paradigms (they correlate); distinguishing them requires specifically designed experiments. ree-v3 can build all of them cheaply (they are all simple scalars over an already-computed mode_value vector) and let experiments disambiguate.

## How the synthesis feeds back into the SD-032 cluster

This lit-pull does not change the SD-032 cluster's shape. It sharpens specific claims:

- **SD-032b (minimum viable substrate):** output is *integration + difficulty + difficulty-gain*, NOT a final mode-choice signal. Integration is the Croxson 2009 interaction term; difficulty is the Shenhav 2016 entropy term; foraging value is the Kolling 2012 option-vs-search comparison. Selection happens downstream in SD-032a.
- **SD-032a (salience-network coordinator):** reads the SD-032b multi-signal bundle plus AIC-analog salience (SD-032c) and PCC-analog attention state (SD-032d), and emits the mode_switch_trigger. The *policy for combining these signals* is an open substrate design question; the literature does not commit us to a specific rule.
- **MECH-258 (precision-weighted pain PE):** the integration term (Croxson interaction) provides the coupling point — z_harm_a enters SD-032b specifically as a cost term that modulates whatever benefit-of-continuing-current-mode is being projected. z_harm_a should not directly emit a mode-switch signal; it should enter SD-032b's integration step.
- **MECH-259 (salience-network switch threshold):** should be gated by choice difficulty (Shenhav 2016). Easy decisions (low difficulty, large EV gap) switch readily; hard decisions (high difficulty, tight EV gap) require higher threshold to switch, preserving current commitment through genuine ambiguity.
- **MECH-260 (dACC bias suppression against monostrategy):** Scholl 2017 gives this a concrete biological substrate: the effort-learning-rate gain. Monostrategy is the failure mode of a collapsed learning rate; the biological unwedging mechanism is neuromodulatory modulation of the gain. ree-v3 should expose SD-032b's learning rate as a parameter gated by an analogue of neuromodulatory tone (tied to SD-012 drive variability).
- **MECH-261 (mode-conditioned write gating):** not directly informed by this pull; depends on whether mode-selection outputs (from SD-032a) propagate into write-gate state machinery downstream. That is governed by the earlier Menon/Uddin 2010 salience-network framework and the MECH-094 tag mechanism, not this effort-value pull.

## Open questions the lit-pull did NOT resolve

- **Is the foraging/EVC/difficulty distinction an artefact of task design?** None of these papers uses a closed-loop embodied agent; all use artificial cue-response tasks. ree-v3 could be a clean test-bed for seeing which signal emerges naturally from a richer task structure.
- **What is the temporal dynamics of SD-032b output?** All five papers use BOLD fMRI. The underlying temporal structure (phasic vs tonic, pre-choice vs post-outcome) is only loosely specified. MECH-259's threshold dynamics and SD-032b's integration timescale are both under-constrained by this pull.
- **Does neuromodulation on the learning rate actually prevent monostrategy?** Scholl 2017 shows a correlation between SSRI and enhanced learning signals. Whether the specific mechanism (neuromodulatory gain on learning rate) actually prevents monostrategy in a long-running agent is a testable ree-v3 claim, not an empirically validated one.
- **How does SD-032b interact with the anterior insula / AIC-analog?** The insula-dACC coupling is central to the broader cingulate lit-pull (Menon/Uddin, Craig) but this pull focuses narrowly on dACC/aMCC effort-value; the interaction is left for SD-032c work.

## Implementation recommendation

SD-032b's minimum viable implementation is now clearer:

1. Maintain a `mode_values[M]` vector over the (small) set of candidate operating modes. Update each mode's value via trial-by-trial prediction errors, with a learning rate parameter exposed to a neuromodulatory gain (Scholl 2017).
2. Emit a multi-signal bundle: `{mode_values, foraging_value_signal, choice_difficulty, integration_with_z_harm_a}`.
3. Do NOT select a mode from SD-032b alone — that is SD-032a's job, and SD-032a should use the full bundle plus AIC salience + PCC attention.
4. The learning rate gain is tied to SD-012 homeostatic drive (low drive → high gain → exploration-like learning; high drive → low gain → exploitation-like lock-in). This is the concrete realisation of MECH-260.

Minimum-viable cingulate substrate (steps 1-3 of SD-032 implementation order) therefore becomes more specifiable:

- Pain forward model + SD-020 + MECH-258: unchanged.
- SD-012 homeostatic drive: unchanged, but now also provides the neuromodulatory gain parameter for SD-032b.
- SD-032b: specified as above — multi-signal output, no final selection, neuromodulator-tunable learning rate.

This is all implementable in ree-v3 with existing primitives; the work is architectural plumbing rather than new substrates.

## Sources

According to PubMed:
- Kolling N, Behrens TEJ, Mars RB, Rushworth MFS. Neural mechanisms of foraging. *Science* 336(6077):95-98 (2012). [DOI](https://doi.org/10.1126/science.1216930)
- Shenhav A, Botvinick MM, Cohen JD. The expected value of control: an integrative theory of anterior cingulate cortex function. *Neuron* 79(2):217-240 (2013). [DOI](https://doi.org/10.1016/j.neuron.2013.07.007)
- Shenhav A, Straccia MA, Botvinick MM, Cohen JD. Dorsal anterior cingulate and ventromedial prefrontal cortex have inverse roles in both foraging and economic choice. *Cognitive, Affective & Behavioral Neuroscience* 16(6):1127-1139 (2016). [DOI](https://doi.org/10.3758/s13415-016-0458-8)
- Croxson PL, Walton ME, O'Reilly JX, Behrens TEJ, Rushworth MFS. Effort-based cost-benefit valuation and the human brain. *Journal of Neuroscience* 29(14):4531-4541 (2009). [DOI](https://doi.org/10.1523/JNEUROSCI.4515-08.2009)
- Scholl J, Kolling N, Nelissen N, Browning M, Rushworth MFS, Harmer CJ. Beyond negative valence: 2-week administration of a serotonergic antidepressant enhances both reward and effort learning signals. *PLoS Biology* 15(2):e2000756 (2017). [DOI](https://doi.org/10.1371/journal.pbio.2000756)
