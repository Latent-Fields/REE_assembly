# Targeted Review: Multi-Axis Homeostatic-Deficit Aggregation Combiners

**Compiled:** 2026-05-31T13:59:15Z
**Trigger:** SD-049 Phase 3 SD-032 consumer cascade landed 2026-05-31 (ree-v3 main `3d276e5`, REE_assembly master `aa6c43a637`). Seven consumers now accept an optional `per_axis_drive` vector + per-consumer combiner config knob, with first-pass defaults set on best-guess biological intuition. This synthesis reviews the multi-deprivation literature to confirm or revise those defaults.
**Author/session:** `lit-pull-sd049-phase3-multi-axis-combiners-20260531T135349Z`
**Scope:** governance-input for the next `/governance` cycle that processes SD-049 Phase 3. Does NOT modify `claims.yaml`, `ree-v3` code, or `substrate_queue.json`.

---

## 1. Question

When an organism is concurrently deprived along multiple homeostatic axes (e.g. hunger + thirst + thermal stress + nociceptive arousal), does each downstream consumer of a multi-axis deficit vector:

| Combiner | Computation | Biological reading |
|---|---|---|
| `max` | `output = f(max(per_axis_drive))` | worst-pressing axis dominates; labelled-line or threshold-crossing readout |
| `sum` | `output = f(sum(per_axis_drive))` | additive integration; total allostatic load |
| `mean` | `output = f(mean(per_axis_drive))` | normalised allostatic load; central-tendency readout |
| `precision_weighted` | `output = f(sum(precision_i * per_axis_drive_i))` | uncertainty-weighted predictive-coding integration |

The current SD-049 Phase 3 defaults are:

| Consumer | Default combiner | Strength label in design doc |
|---|---|---|
| AIC | max | FIRST APPROXIMATION |
| PCC | mean | Solid (Leech & Sharp 2013) |
| pACC | sum | Solid (Baliki 2012 allostatic load) |
| dACC | max | FIRST APPROXIMATION |
| Salience | max | FIRST APPROXIMATION |
| Override | max | FIRST APPROXIMATION |
| MECH-295 | max (fallback); per_axis_drive[goal_axis_idx] when supplied | Strong (Berridge identity-specific incentive salience) |

This review focuses on the four FIRST APPROXIMATION defaults: AIC, dACC, Salience, BroadcastOverride. PCC and pACC are already lit-anchored in the design doc; MECH-295's axis-matched routing is the strongest of the seven (Berridge & Robinson 2003 / Berridge & Kringelbach 2015 already in the lit corpus).

---

## 2. Headline finding

**Two-stage architecture is robust across all four FIRST APPROXIMATION consumers.** The biology consistently shows:

1. **Input stage:** additive convergence of multi-axis homeostatic signals onto integrator neurons (SUM-like at the synapse), modulated by precision/uncertainty estimates where state-dependent gain control exists.
2. **Output stage:** winner-take-all / switch / option selection (MAX-like over discrete modes), enforced by mutual inhibition between functionally opposed populations or by softmax-like option arbitration.

Neither pure-`max` nor pure-`sum` is consistent with the literature for any of the four consumers in isolation. The right question is **which stage each REE consumer corresponds to** — and that determines whether `max` or a richer combiner is the load-bearing default.

This re-framing changes the verdict for two of the four:

- **AIC `max`:** weakly anchored. The mature biology says precision-weighted integration at the population level (Allen et al 2020), with state-gated reconfiguration under a dominant axis (Livneh et al 2017). Pure `max` is a defensible **coarse approximation** of the dominant-axis case but loses the precision-weighting signal. Confidence in `max` as best-feasible-default: 0.55.
- **dACC `max`:** weakly anchored, arguably wrong. The canonical EVC formalism (Shenhav et al 2013) is explicitly **additive** in the control-demand input, with softmax across options at the decision stage. The per-axis deficit vector feeds the *input* stage of EVC, not the option-selection stage. SUM is the biology-anchored default; `max` under-uses the per-axis signal. Confidence in `sum` over `max`: 0.70. **Recommended revision.**
- **Salience `max`:** moderately well-anchored at the OUTPUT stage (network switching, Sridharan et al 2008). The input combiner is poorly characterised. `max` is defensible because the consumer's output IS a mode-switch decision. Confidence in `max`: 0.65.
- **BroadcastOverride `max`:** moderately well-anchored. The mature orexin/LH biology (Karnani et al 2020, González et al 2016) is SUM at single-cell inputs but **mutual-inhibition winner-take-all between opposing populations (ORX vs MCH)**. Since the BroadcastOverride consumer outputs a discrete override decision (the population-level competition), `max` is defensible. Confidence in `max`: 0.65.

**Bottom line:** Three of four `max` defaults survive as defensible first approximations once the input-stage-vs-output-stage distinction is made explicit. The exception is dACC, where the literature points to SUM as the better default.

---

## 3. Per-consumer verdicts

### 3.1 AIC under multi-deprivation

**Current default:** `max`
**Verdict:** REVISE TO `precision_weighted` IDEALLY; HOLD AT `max` AS DEFENSIBLE COARSE APPROXIMATION
**Lit confidence:** 0.55 in `max` as best feasible default; 0.78 in `precision_weighted` as the biology-correct target if substrate can support it
**Recommended routing:** ALIGN-WITH-CAVEAT; mark as substrate-conditional revision target pending a precision-estimate substrate

**Anchors:**

1. **Craig 2009** — *Nature Reviews Neuroscience* `10.1038/nrn2555` (PMID 19096369). AIC as the interoceptive integration hub. Already in lit corpus at [targeted_review_cingulate_integration_substrate](../targeted_review_cingulate_integration_substrate/entries/2026-04-19_cingulate_aic_interoception_salience_craig2009/). Argues AIC constructs a "global emotional moment" by pooling multi-modal interoceptive streams — favours integration over single-axis dominance. **Weight:** establishes AIC as a multi-axis hub; does not adjudicate the specific combiner.

2. **Critchley et al 2004** — *Nature Neuroscience* `10.1038/nn1176` (PMID 14730305). Right AIC activity during heartbeat detection predicts interoceptive accuracy; grey-matter volume correlates with visceral awareness. **Weight:** confirms single-hub architecture; combiner-agnostic.

3. **Livneh et al 2017** — *Nature* 546:611-616, `10.1038/nature22375` (PMID 28614346). The decisive multi-deprivation paradigm. In mice, AgRP→PVT→BLA→IC circuit installs hunger-state-specific visual-cue selectivity in IC neurons. The selectivity is *state-gated* — hungry mice show food-cue bias, sated mice do not. **Weight:** strongest single anchor for the `max` reading. The IC representation is reconfigured by the dominant deficit, suggesting state-switched labelled-line rather than additive summation. **Caveat:** the paper does NOT test concurrent thirst + hunger, so it cannot dissociate "switched to hunger-mode" from "additively weighted toward whichever deficit dominates right now."

4. **Allen, Levy, Parr, Friston et al 2020** — *J. Neuroscience* 40(19):3827, `10.1523/JNEUROSCI.2904-19.2020` (PMID 32269104). AIC projection patterns scale with prior belief in a way that implements **precision-weighting** of bottom-up prediction error. **Weight:** strongest computational claim. Signals from different interoceptive axes compete on precision, not raw magnitude. Under sufficiently high precision priors this can functionally APPROXIMATE `max`, which is the rescuing argument for the current `max` default.

5. **Gehrlach et al 2019** — *Nature Neuroscience* 22:1424-1437, `10.1038/s41593-019-0469-1` (PMID 31455886). Posterior insula receives multimodal subcortical convergence; optogenetic perturbation alters multi-modal aversive behaviour across nociception, hunger-aversion, and social threat. **Weight:** posterior IC is a convergence zone, not a labelled-line. Closer to SUM-like integration; but pIC and AIC are distinct subdivisions, so the inference for AIC proper is indirect.

6. **Livneh & Andermann 2022** — *Neuron* 109(22):3576-3593. IC encodes hunger and thirst in *partially overlapping but distinguishable* population codes. Mid-posterior IC codes "need" regardless of modality. Behavioral evidence: thirst hierarchically suppresses hunger (dehydration-induced anorexia). **Weight:** the closest within-IC multi-axis review. Population overlap supports partial integration; behavioral precedence supports a MAX-like override regime above threshold. The cleanest within-AIC concurrent multi-axis dissociation has NOT been done.

7. **Pessoa & Adolphs 2010** — *Nature Reviews Neuroscience* (cited in current design doc) — argues against modality-segregated salience-network operation; favours distributed multi-modal integration.

**Verdict rationale (AIC):** The literature points to **precision-weighted integration** as the biology-correct combiner, not `max`. However, REE does not currently surface per-axis precision estimates as substrate. The `max` default is a defensible coarse approximation of the dominant-axis case (Livneh 2017 supports this empirically) and the deformation-under-high-precision argument (Allen 2020) means `max` is not actively WRONG, just lossy. The cleaner finding from the literature is that AIC has a *multi-axis* representation rather than a labelled-line per modality.

**Recommended routing:** HOLD `max` as default; ALIGN with lit-anchor note that `precision_weighted` is the biology-target if/when SD-049 Phase 4 surfaces a per-axis precision substrate. Flag for the next governance cycle as a substrate-conditional revision candidate.

### 3.2 dACC EVC under multi-deficit

**Current default:** `max`
**Verdict:** REVISE TO `sum`
**Lit confidence:** 0.70 in `sum` over `max`
**Recommended routing:** REVISE — substrate change in `ree_core/utils/config.py` default for `aic_per_axis_combiner` → `sum` once the user assents

**Anchors:**

1. **Shenhav, Botvinick & Cohen 2013** — *Neuron* 79(2):217-240, `10.1016/j.neuron.2013.07.007` (PMID 23889930). The Expected Value of Control (EVC) is explicitly formalised as `EVC(control_signal, state) = Σ p(outcome|signal, state) · value(outcome) − cost(signal)`. **The combination is additive: payoff terms sum, effort cost subtracts.** This is the canonical computational theory for dACC. **Weight:** decisive. The formalism does not contain a `max` operation over input deficit channels — it sums them into a scalar that then competes against effort cost.

2. **Croxson et al 2009** — *J. Neuroscience* 29(14):4531-4541, `10.1523/JNEUROSCI.4515-08.2009` (PMID 19357278). dACC BOLD signal encodes reward magnitude *discounted by effort* — scalar combination of multiple value/cost terms. **Weight:** consistent with additive EVC; treats effort as a subtractive cost rather than an independent dimension competing on max.

3. **Kolling et al 2016** — *Nature Neuroscience* 19(10):1280-1285, `10.1038/nn.4382`. dACC encodes multiple time-linked value representations (current vs alternative environments) used for stay/switch decisions. Multiple value streams are *simultaneously* represented, then **combined** for decision. **Weight:** supports parallel representation followed by integrative combination, not max-takes-all.

4. **Shackman et al 2011** — *Nature Reviews Neuroscience* `10.1038/nrn2994` (PMID 21331082). Already in lit corpus at [targeted_review_cingulate_integration_substrate](../targeted_review_cingulate_integration_substrate/entries/2026-04-19_cingulate_dacc_integration_shackman2011/). Coordinate-based meta-analysis across 380+ studies: dACC integrates pain + negative affect + cognitive-control demand into a behavioural-adjustment signal. The "adaptive control hypothesis" frames dACC as computing **how much** adjustment, not **which axis** needs adjustment. **Weight:** the magnitude framing favours additive integration over winner-take-all.

5. **Holroyd & Yeung 2012** — *Trends in Cognitive Sciences* 16(2):122-128, `10.1016/j.tics.2011.12.008` (PMID 22226543). ACC selects extended "options" via reward-based value computations using softmax-like comparison. **Critical nuance:** softmax across options at the **output stage**, but option *value* itself built additively at the **input stage**. dACC has **sum-within-option, softmax-across-options**. **Weight:** confirms the two-stage architecture. For the SD-049 per_axis_drive consumer, which feeds dACC's input stage (per-axis deficit magnitude → behavioural adjustment demand), the relevant stage is SUM.

6. **Behrens et al 2007** — *Nature Neuroscience* 10(9):1214-1221, `10.1038/nn1954` (PMID 17676057). ACC tracks volatility and adjusts learning rate optimally — weight on new evidence is set by precision estimate, not raw signal magnitude. **Weight:** dACC analog of the Allen 2020 AIC precision result. Supports precision-modulated integration over hard MAX.

**Verdict rationale (dACC):** The EVC formalism (Shenhav 2013) is explicit and influential: dACC computes a scalar control-demand signal by additively combining multiple cost/benefit terms. The Shackman 2011 meta-analytic frame of "adaptive control magnitude" reinforces this. The Holroyd & Yeung 2012 caveat — that ACC behaves max-like at the option-selection stage — is correct but the SD-049 per_axis_drive consumer feeds the *input* stage, not the option-selection stage. The right combiner for input-stage dACC aggregation is `sum`.

**Recommended routing:** REVISE. The dACC consumer default in `ree_core/utils/config.py` (`dacc_per_axis_combiner: str = "max"`) should be flipped to `"sum"`. This is the biology-correct first approximation and does not require new substrate (the per_axis_drive vector already supports SUM aggregation via the shared helper). Bit-identical-OFF is preserved because the master flag `REEConfig.use_sd049_per_axis_consumer_cascade` gates all reads; the default change only affects master-ON consumers.

### 3.3 Salience network mode-arbitration under multi-axis input

**Current default:** `max`
**Verdict:** ALIGN — `max` is defensible at the output stage where the salience-coordinator consumer operates
**Lit confidence:** 0.65 in `max` as best feasible default
**Recommended routing:** ALIGN with lit-anchor note; flag the input-stage combiner as a genuine evidence gap

**Anchors:**

1. **Menon & Uddin 2010** — *Brain Structure & Function* `10.1007/s00429-010-0262-0` (PMID 20512370). Already in lit corpus at [targeted_review_cingulate_integration_substrate](../targeted_review_cingulate_integration_substrate/entries/2026-04-19_cingulate_salience_network_switching_menon2010/). The triple-network framework. Salience network's primary computational output is **mode selection** — switching between DMN, CEN, and task modes on salient events. **Weight:** establishes that the salience-coordinator's output stage IS a discrete mode-switch — which is functionally a `max` operation over modes.

2. **Seeley et al 2007** — *J. Neuroscience* 27(9):2349-2356, `10.1523/JNEUROSCI.5587-06.2007` (PMID 17329432). SN (dACC + orbital FI) and CEN (DLPFC + parietal) are dissociable intrinsic networks. Pre-scan anxiety correlated only with SN connectivity; executive performance only with CEN. **Weight:** architectural anchor. Doesn't itself dissociate MAX vs SUM at the input stage; establishes SN as the candidate site for any combiner.

3. **Sridharan, Levitin & Menon 2008** — *PNAS* 105(34):12569-12574, `10.1073/pnas.0800005105` (PMID 18723676). Right fronto-insular cortex causally drives switching between CEN and DMN across multiple task paradigms and stimulus modalities (Granger causality). **Weight:** decisive for the output-stage `max` reading. The SN's output is a winner-take-all switch over network modes — `max` over MODES, not over deficit axes.

4. **Goulden et al 2014** — *NeuroImage* 99:180-190, `10.1016/j.neuroimage.2014.05.052` (PMID 24862074). Replicates Sridharan 2008 with DCM on two independent resting-state datasets. SN → DMN/CEN switching effective connectivity is reliable. **Weight:** confirms SWITCH-output architecture.

5. **Honest flag — no clean multi-axis input-stage dissociation experiment identified.** Literature searches for SN response to simultaneous-vs-single salient inputs (varying the *number* of concurrent salient axes parametrically) returned anatomical and methodological replications but no paradigm that varies the number of concurrent salient axes and asks whether SN amplitude scales additively, saturates, or tracks the maximum. The Murphy lineage (pupillometry-EEG-fMRI 2014–2022) examines temporal dynamics of salience-network engagement but not multi-axis amplitude combination.

**Verdict rationale (Salience):** The salience-coordinator consumer's job in REE is to pick a mode (commit-elevation gate / replay trigger / urgency-interrupt). That output is structurally a winner-take-all decision — biology-aligned with `max`. The input-stage combiner (how multi-axis deficit pressure converts into salience-network drive before the switch decision) is genuinely under-characterised in the literature. Given that the output IS a switch and the SD-049 consumer is wired into that output decision, `max` is defensible.

**Recommended routing:** HOLD `max`. Lit-anchor note: well-anchored at the output stage (Sridharan 2008, Goulden 2014); input-stage combiner is an evidence gap. Flag for a future discriminative-pair experiment if the consumer's behavioural impact in V3 becomes load-bearing.

### 3.4 BroadcastOverrideRegulator / Orexin-LH multi-deficit recruitment

**Current default:** `max`
**Verdict:** ALIGN — `max` is defensible at the population-output stage where the consumer operates
**Lit confidence:** 0.65 in `max` as best feasible default
**Recommended routing:** ALIGN with lit-anchor note

**Anchors:**

1. **Mileykovskiy et al 2005** — *Neuron* 46(5):787-798. Already in lit corpus at [targeted_review_sd_037_orexin_kinetics](../targeted_review_sd_037_orexin_kinetics/entries/2026-04-26_mech_280_orexin_active_waking_mileykovskiy2005/). Orexin neurons fire phasically at the onset of active waking, motor activation, and reward-anticipation. **Weight:** establishes orexin neurons as a behavioural-state recruitment signal; combiner-agnostic on the input side.

2. **Sakurai 2014** — Review. Already in lit corpus at [targeted_review_sd_037_orexin_kinetics](../targeted_review_sd_037_orexin_kinetics/entries/2026-04-26_mech_280_orexin_motivated_behaviour_sakurai2014/). Orexin neurons integrate metabolic (leptin, ghrelin, glucose), stress (CRF), circadian, and autonomic afferents on the same cells. **Weight:** the strongest qualitative claim for **multi-input convergence on single orexin cells** — i.e., SUM at the single-cell input stage.

3. **Yamanaka et al 2003** — *Neuron* 38(5):701-713, `10.1016/S0896-6273(03)00331-3` (PMID 12797956). Orexin neurons fire in response to leptin / ghrelin / glucose state. Energy-balance signals modulate firing rate as a graded function of metabolic deficit. **Weight:** establishes gradedness on a single axis; consistent with SUM-into-rate-code at the orexin neuron level.

4. **Tyree, Borniger & de Lecea 2018** — *Frontiers in Neurology* 9:413, `10.3389/fneur.2018.00413` (PMID 29928253). Review establishing orexin/hypocretin neurons as a **central integration hub** receiving and combining metabolic, stress, circadian, and autonomic afferents. The same neurons respond to hunger, cold, stress, and arousal demand. **Weight:** the strongest qualitative claim for additive combination across deficit axes anywhere in the four consumers. Orexin neurons explicitly co-receive and pool signals from multiple homeostatic streams.

5. **Karnani et al 2020** — *Current Biology* 30(19):3805-3812.e4, `10.1016/j.cub.2020.07.023` (PMID 32822604). Within-LH local connectivity is sparse and includes **mutual inhibition** between functionally opposed cell types (ORX ↔ MCH; VGLUT2 ↔ VGAT). **Weight:** decisive for the output-stage MAX reading. The LH output is closer to MAX over modes (rest-vs-seek) even though individual orexin neurons sum their inputs.

6. **González, Iordanidou, Strom, Adamantidis & Burdakov 2016** — *Nature Communications* 7:11395, `10.1038/ncomms11395` (PMID 27102565). In vivo recording shows orexin and MCH populations are anti-correlated in firing; brain-wide afferent maps overlap substantially. **Weight:** reinforces the picture: shared inputs (SUM at input), opponent outputs (MAX over modes).

7. **Burnett et al 2016** — *Cell* (already in lit corpus at [targeted_review_homeostatic_override](../targeted_review_homeostatic_override/entries/2026-04-22_homeostatic_override_hunger_competition_burnett2016/)). Hunger circuits compete with predator-defence circuits; mutual inhibition determines which behaviour wins. **Weight:** consistent with the mutual-inhibition / winner-take-all output story.

**Verdict rationale (BroadcastOverride):** The orexin/LH literature has the clearest two-stage architecture in the four consumers. Individual orexin neurons sum multi-axis homeostatic inputs (SUM at input). Population-level mutual inhibition between ORX and MCH enforces winner-take-all dynamics (MAX over modes). The REE BroadcastOverrideRegulator consumer outputs a discrete override decision (recruit / not-recruit broadcast modulation), which sits at the population-output stage. `max` is the biology-anchored combiner for that stage.

**Recommended routing:** HOLD `max`. Lit-anchor note: well-anchored at the population-output stage (Karnani 2020, González 2016, Burnett 2016) where the consumer operates. The single-cell input stage is SUM (Sakurai 2014, Yamanaka 2003, Tyree 2018), but the REE consumer is not wired into that stage — it reads the population-level competition outcome.

---

## 4. MECH-295 axis-matched routing (out of scope but noted)

The current MECH-295 default is `max` (fallback) plus `per_axis_drive[goal_axis_idx]` when a goal axis index is supplied. The Berridge & Robinson 2003 / Berridge & Kringelbach 2015 incentive-salience literature directly supports this design: wanting and liking are axis-identity-specific (the rat wants sugar when sugar-deprived, not whatever happens to be the maximal deficit). The `goal_axis_idx` routing is therefore the biology-correct primary path; `max` fallback is for cases where no goal axis has been resolved yet (cold-start, simulation_mode, novelty-driven approach). No revision needed.

---

## 5. PCC and pACC (already lit-anchored, brief affirmation)

- **PCC `mean`:** Leech & Sharp 2013 (already in lit corpus at [targeted_review_cingulate_integration_substrate](../targeted_review_cingulate_integration_substrate/entries/2026-04-19_cingulate_pcc_arousal_attention_leech2013/)). PCC computes arousal-attention level averages over ongoing input; `mean` is the right combiner for a normalised allostatic-load readout. No revision needed.
- **pACC `sum`:** Baliki et al 2012 (allostatic-load anchor cited in current design doc). pACC encodes cumulative drive-pressure as additive value-bias on goal trajectories. No revision needed.

---

## 6. Cross-consumer pattern: integrate-then-arbitrate

The convergent reading across all four FIRST APPROXIMATION consumers is that biology uses a **two-stage architecture**:

| Stage | Computation | REE-relevant substrates |
|---|---|---|
| Input convergence | SUM (additive synaptic) modulated by precision-weighting (Allen 2020 AIC, Behrens 2007 dACC) | dACC EVC input, AIC interoceptive pooling, orexin neuron input integration |
| Output arbitration | Winner-take-all / mode-switch via mutual inhibition or softmax over options | Salience network DMN/CEN switching, LH ORX↔MCH competition, dACC option-selection |

REE's current Phase 3 consumer cascade assigns a single combiner per consumer based on the consumer's primary output role. The verdict from this review is that **three of the four FIRST APPROXIMATION `max` defaults survive once you recognise that those consumers' outputs ARE arbitration-stage decisions** (mode-switch, override-recruit, option-select). The exception is dACC, where the per_axis_drive vector feeds the EVC input stage rather than the option-selection output stage — and the input stage is SUM.

This two-stage finding is the most generalisable insight from the review and could be encoded as architecture documentation in `docs/architecture/sd_049_multi_resource_heterogeneity.md` rather than per-consumer notes.

---

## 7. Outcome routing summary

| Consumer | Current default | Lit-anchored verdict | Action |
|---|---|---|---|
| AIC | `max` | `precision_weighted` ideally; `max` defensible coarse approximation | HOLD `max`; flag for substrate-conditional Phase-4 revision |
| dACC | `max` | `sum` | **REVISE TO `sum`** in `ree_core/utils/config.py` (default change; bit-identical OFF preserved) |
| Salience | `max` | `max` at output stage (where consumer operates); input stage uncharacterised | ALIGN; flag input-stage gap for future discriminative experiment if needed |
| Override | `max` | `max` at population-output stage; input stage is SUM but consumer not wired there | ALIGN |
| PCC | `mean` | `mean` (Leech 2013) | ALIGN |
| pACC | `sum` | `sum` (Baliki 2012) | ALIGN |
| MECH-295 | `max` fallback + axis-matched routing | `goal_axis_idx` routing (Berridge identity-specific) | ALIGN |

**Recommended next-step routing:**

1. **/governance cycle:** record the four verdicts above in the SD-049 Phase 3 governance entry. Flag dACC as the single revision target with `recommended_substrate_queue_entry` for an /implement-substrate session.
2. **/implement-substrate session (post-governance):** flip `dacc_per_axis_combiner` default `"max"` → `"sum"` in `ree_core/utils/config.py`. Add lit-anchor note to `docs/architecture/sd_049_multi_resource_heterogeneity.md` Phase 3 follow-on section recording the four verdicts. Add a contract test confirming the new default. Confirm bit-identical OFF under the master flag.
3. **Substrate-conditional follow-on (deferred):** the AIC `max` → `precision_weighted` revision target requires a per-axis precision substrate that does not yet exist. Open as a substrate_queue entry tagged `substrate_conditional` rather than `pending_implementation`.

**Honest evidence gaps surfaced:**

- The cleanest within-AIC concurrent multi-axis dissociation experiment (factorial hunger + thirst + thermal + nociception varying parametrically) has NOT been run in any species (`Livneh & Andermann 2022` flags this gap).
- The salience-network INPUT-stage combiner is uncharacterised — Sridharan 2008 and Goulden 2014 establish *that* it switches, not *how* it pools multi-axis input before deciding.
- The orexin/LH literature is qualitative on the cross-axis combiner — no experiment concurrently elevates hunger + thirst + thermal + nociceptive drive and asks whether orexin firing tracks max, sum, or sigmoidal saturation.
- Three of the four FIRST APPROXIMATION defaults survive the review on the strength of *output-stage* anchoring; if future REE work routes per_axis_drive into a *different* stage of any of these consumers, the verdict could change.

---

## 8. Anchor count audit

- **AIC:** 7 anchors (Craig 2009, Critchley 2004, Livneh 2017, Allen 2020, Gehrlach 2019, Livneh & Andermann 2022, Pessoa & Adolphs 2010). >= 4: PASS.
- **dACC:** 6 anchors (Shenhav 2013, Croxson 2009, Kolling 2016, Shackman 2011, Holroyd & Yeung 2012, Behrens 2007). >= 4: PASS.
- **Salience:** 4 anchors (Menon & Uddin 2010, Seeley 2007, Sridharan 2008, Goulden 2014). >= 4: PASS.
- **BroadcastOverride:** 7 anchors (Mileykovskiy 2005, Sakurai 2014, Yamanaka 2003, Tyree 2018, Karnani 2020, González 2016, Burnett 2016). >= 4: PASS.

**Total: 24 anchors across 4 consumers under review.** Acceptance criterion (>=16) met. Multi-deprivation paradigms prioritised where they exist (Livneh 2017 hunger-specific, Livneh & Andermann 2022 hunger/thirst overlap, Tyree 2018 multi-input convergence). Where the literature is silent on dissociation, the gap is named explicitly rather than papered over.

---

## 9. Confidence and methodology notes

This synthesis is medium-confidence. Most anchors are well-cited reviews and primary-data papers; the verdicts are reasoned aggregates rather than direct dissociation evidence (because the clean concurrent multi-deprivation experiment has not been run in any of the four consumers). The two-stage integrate-then-arbitrate framing is the most defensible reading I can extract from the literature; it is a synthesis of multiple lines of evidence rather than a single dissociation result.

`lit_conf` per consumer following the Phase 3 lit/exp decoupling regime (`REE_assembly/CLAUDE.md` §"Lit/Exp Decoupling"):

- AIC: 0.55 in `max` as best feasible; 0.78 in `precision_weighted` as ideal
- dACC: 0.70 in `sum` as best default (revision recommendation)
- Salience: 0.65 in `max` at output stage
- Override: 0.65 in `max` at population-output stage
- PCC, pACC, MECH-295: not under review; existing anchors hold.

The lit/exp decoupling regime treats `lit_conf` and `exp_conf` as parallel signals (not blended). The verdicts above are lit-side judgements; experimental confidence on the SD-049 Phase 3 consumer cascade will come from V3-EXQ-514 (Phase 2 hybrid encoder validation) and any follow-on Phase 3 behavioural validation.

---

## 10. References to existing lit-corpus entries

The following anchors already exist as full record.json + summary.md in the lit corpus and are referenced rather than duplicated:

- [Craig 2009 (AIC)](../targeted_review_cingulate_integration_substrate/entries/2026-04-19_cingulate_aic_interoception_salience_craig2009/)
- [Shackman 2011 (dACC)](../targeted_review_cingulate_integration_substrate/entries/2026-04-19_cingulate_dacc_integration_shackman2011/)
- [Menon & Uddin 2010 (salience)](../targeted_review_cingulate_integration_substrate/entries/2026-04-19_cingulate_salience_network_switching_menon2010/)
- [Leech 2013 (PCC)](../targeted_review_cingulate_integration_substrate/entries/2026-04-19_cingulate_pcc_arousal_attention_leech2013/)
- [Scholl 2015 (dACC effort)](../targeted_review_cingulate_integration_substrate/entries/2026-04-19_cingulate_dacc_effort_learning_scholl2015/)
- [Vogt 2005 (ACC subdivisions)](../targeted_review_cingulate_integration_substrate/entries/2026-04-19_cingulate_acc_subdivisions_vogt2005/)
- [Seymour 2019 (pain precision)](../targeted_review_cingulate_integration_substrate/entries/2026-04-19_cingulate_pain_precision_signal_seymour2019/)
- [Mileykovskiy 2005 (orexin)](../targeted_review_sd_037_orexin_kinetics/entries/2026-04-26_mech_280_orexin_active_waking_mileykovskiy2005/)
- [Sakurai 2014 (orexin)](../targeted_review_sd_037_orexin_kinetics/entries/2026-04-26_mech_280_orexin_motivated_behaviour_sakurai2014/)
- [Burnett 2016 (hunger override)](../targeted_review_homeostatic_override/entries/2026-04-22_homeostatic_override_hunger_competition_burnett2016/)

Additional anchors cited in this synthesis without existing record.json entries (could be backfilled as separate `targeted_review_*` entries if a future governance cycle requires them):

- Critchley et al 2004 *Nature Neuroscience* — AIC interoceptive accuracy
- Livneh et al 2017 *Nature* — AgRP→PVT→BLA→IC hunger-state gating (DECISIVE multi-deprivation anchor; backfill recommended)
- Allen et al 2020 *J. Neuroscience* — AIC projection precision-weighting
- Gehrlach et al 2019 *Nature Neuroscience* — pIC multimodal aversive convergence
- Livneh & Andermann 2022 *Neuron* — IC hunger/thirst partial overlap (key multi-axis review; backfill recommended)
- Shenhav, Botvinick & Cohen 2013 *Neuron* — EVC formalism (DECISIVE dACC anchor; backfill recommended)
- Croxson et al 2009 *J. Neuroscience* — dACC effort discounting
- Kolling et al 2016 *Nature Neuroscience* — dACC multiple value streams
- Holroyd & Yeung 2012 *Trends Cognitive Sciences* — ACC option selection
- Behrens et al 2007 *Nature Neuroscience* — ACC volatility precision-weighting
- Seeley et al 2007 *J. Neuroscience* — salience-network anatomy
- Sridharan, Levitin & Menon 2008 *PNAS* — rFIC causal switch (DECISIVE salience anchor; backfill recommended)
- Goulden et al 2014 *NeuroImage* — DCM replication of SN switching
- Pessoa & Adolphs 2010 *Nature Reviews Neuroscience* — distributed salience integration
- Yamanaka et al 2003 *Neuron* — orexin energy-balance graded firing
- Tyree, Borniger & de Lecea 2018 *Frontiers in Neurology* — orexin multi-input hub
- Karnani et al 2020 *Current Biology* — LH sparse mutual inhibition (DECISIVE override anchor; backfill recommended)
- González et al 2016 *Nature Communications* — ORX/MCH anti-correlation

Four candidate backfills tagged DECISIVE: Livneh 2017, Livneh & Andermann 2022, Shenhav 2013, Sridharan 2008, Karnani 2020. If governance flags the dACC revision as load-bearing, Shenhav 2013 should be the first backfill.

---

## 11. Out-of-scope, NOT touched

- `claims.yaml` — no claim status changes. Lit confidence above is governance input only.
- `ree-v3/ree_core/utils/config.py` — no default flip in this session. The dACC `sum` revision recommendation is queued for a follow-on /implement-substrate session.
- `substrate_queue.json` — no new SD entries. The AIC substrate-conditional revision target is flagged in §7 routing notes for the next governance cycle to register if it chooses.
- `experiment_queue.json` — no new EXQ. Future discriminative-pair experiments (e.g. a 4-arm AIC combiner sweep under concurrent hunger+thirst+thermal) are flagged but not queued.
- Individual record.json files in the lit corpus — the four DECISIVE backfill candidates (Livneh 2017, Shenhav 2013, Sridharan 2008, Karnani 2020) are noted but not created in this session; they should be filed under their own /lit-pull sessions if governance requires the full record schema rather than synthesis-level citation.
