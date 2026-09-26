# Dynamic-control / coordination-hole audit -- Step 5: biological solutions to regime selection

**Date:** 2026-09-26. **Worker:** DC-C (biology), chip `chip-20260926-dynctl-c-biology`, session `bt0926-dcc`,
orchestrator `orchestrate-20260924-breakthrough-c2`. **Scope:** DYNCTL_PLAN.md Phase 1 / audit step 5 only
("compare biological solutions, favouring distributed dynamic coordination over a homuncular executive").
Steps 1-4 and 6-9 belong to DC-A, DC-B and DC-D; this record does not attempt them.

**Read first, as instructed:** `docs/thoughts/2026-09-26_dynamic_control_coordination_hole.md` (the user's
9-step request, explicit constraint: do NOT begin by inventing a monolithic executive);
`evidence/planning/thought_intake_2026-09-26_dynamic_control_coordination_hole.md` (no new claims --
content owned by ARC-155/ARC-156/Q-111, siblings Q-112/ARC-157/MECH-597); `docs/claims/claims.yaml`
entries for those six ids (read in full above). This record builds on and cites them; it registers
nothing new in `claims.yaml`.

**Method:** literature already on file first (`evidence/literature/` currently holds ~3,070 entries;
`grep`-scoped counts per topic are given below), gaps filled by one verified PubMed lookup (metaplasticity)
per `/lit-pull` discipline -- cited in-record, no new `evidence/literature/` entry written (not required
by the brief when an existing corpus already covers a topic; the one gap found is cited directly, verified
against PubMed, not registered as a scored entry since that is a governance action outside this worker's
remit). No ree_core edits, no probes, no claims -- this is a read-only literature/architecture synthesis.

**Framing constraint carried through every section below:** none of these systems is, biologically, a
single supervisory node. Every one of them is implemented as (a) a broadcast source with many
independent receivers that locally decide how to respond, (b) two or more mutually-antagonistic
populations whose balance IS the state (not a third node reading them and issuing a verdict), or (c) a
threshold/comparator process running in parallel with, not on top of, the systems it gates. Where REE's
current code names a single node "SalienceCoordinator" or a single mode register, that is already a
narrower shape than the biology it is named after (see ARC-155/ARC-156 notes: MECH-266's per-mode
(enter,exit) pairs are a similar simplification against PBWM's opposing-pathway account, flagged below).
Treat every "REE analogue: none" cell as a candidate for a distributed mechanism, not a slot to fill with
one new module.

---

## 1. LC-NE adaptive gain theory (phasic/tonic, exploit/explore)

**On file:** 123 files reference LC-NE; canonical sources: `targeted_review_q_042/entries/2026-05-08_q042_aston_jones_cohen_2005`,
`targeted_review_arc_066_tonic_vigor/entries/2026-05-10_arc_066_lc_adaptive_gain_aston_jones_cohen_2005`,
`targeted_review_action_learning_bootstrap_class_choice/entries/2026-07-14_mech_457_adaptive_gain_lc_ne_astonjones_cohen2005`,
`targeted_review_connectome_mech_178/entries/2026-04-06_mech_178_lc_ne_behavioral_berridge2003`.

- **Trigger signal:** ACC/OFC-monitored task utility (a running estimate of how well the current policy is doing), read out and broadcast by LC.
- **Controlled variable:** gain/noise on cortical and BG processing -- policy sharpness/stochasticity, downstream population responsivity.
- **Timescale:** phasic burst locked to the decision-commit moment (sub-second); tonic baseline drifts over minutes-to-task-block.
- **What it switches between:** exploit (phasic mode, sharp, locked to the chosen action) vs explore (tonic mode, flat, disengaged).
- **Evidence strength:** high (D... in the literature's own terms this is a well-replicated primate + computational synthesis; for REE it is D0 -- no REE implementation exists to test).
- **REE analogue:** MECH-104 (phasic network-reset), MECH-313 (tonic NE noise floor), MECH-457/MECH-433/ARC-065 (explore/exploit competence-bootstrap family), ARC-016 (the running-variance operating point whose timing Q-042 already interrogates -- see next section).
- **Single vs distributed:** distributed at the receiving end (LC broadcasts one scalar-ish signal but every cortical/BG target reads and uses it locally; ACC/OFC compute the trigger, LC only relays); the ACC-to-LC-to-everywhere loop is nonetheless a single upstream broadcaster, which is the shape most at risk of being read as "build one exploit/explore switch."
- **What REE would need to endogenously measure:** a running utility/advantage estimate produced by REE's own critic/E3 (not an oracle reward), broadcast at ACTION-SELECTION time rather than only after outcome arrival -- this is exactly Q-042's live open question about where ARC-016's running-variance update should sit in the causal chain (currently inside `agent.update_residue()`, i.e. after outcome, per the Q-042 entry's own reading).

## 2. ACh expected-uncertainty vs NE unexpected-uncertainty (Yu & Dayan 2005)

**On file:** `targeted_review_q_045/entries/2026-05-11_q_045_ne_unexpected_uncertainty_yu_dayan2005`,
`targeted_review_arc_044/entries/2026-09-08_arc_044_uncertainty_neuromodulation_yu2005`,
`targeted_review_connectome_mech_002/entries/2026-09-08_mech_002_expected_unexpected_uncertainty_yu2005`,
`targeted_review_mech_063/entries/*yudayan2005*` (3 files), 35 files touch "expected uncertainty."

- **Trigger signal:** ACh -- known, signalled unreliability of a cue within an otherwise-stable generative model (e.g. an 80%-valid cue). NE -- an unsignalled context switch that makes recent predictions inconsistent with new outcomes (a change the model did not know to expect).
- **Controlled variable:** the balance between trusting the current model (down-weight incoming surprising evidence as noise) and revising it (up-weight surprising evidence as informative, trigger belief update / exploration).
- **Timescale:** ACh -- continuous, tracks a within-context noise estimate; NE -- event-triggered, fires at a detected regime change and decays over the re-learning period.
- **What it switches between:** exactly REE's "classify PE as noise vs model error vs environmental change" decision (ARC-155/Q-111 vocabulary) -- treat prediction error as expected variance (ACh regime) vs treat it as evidence the world changed (NE regime).
- **Evidence strength:** high as computational theory (canonical, heavily cited); the ACh/NE substrate mapping specifically is looser (see caveats in the on-file entries: MECH-313 is currently a tonic noise-floor primitive, not an unexpected-uncertainty trigger).
- **REE analogue:** MECH-104 (network reset), MECH-313 (NE floor), MECH-590 (learned PE-routing significance), ARC-037, MECH-585 -- this is the cluster the intake table already assigns to "trust vs interrogate the model; classify PE." **This is directly relevant to N5's failed shift detector** (per DYNCTL_PLAN's orchestrator notes): N5 needed exactly an unexpected-uncertainty signal -- "my recent prediction errors are inconsistent with my model of my own error statistics, not merely large" -- and the probe found neither raw nor action-contrastive surprise separated a genuine action-map shift from no-shift. That is the NE half of Yu & Dayan missing outright, not merely mis-tuned.
- **Single vs distributed:** genuinely two-substrate, two-signal, antagonistic/synergistic -- the paper's whole point is that collapsing ACh and NE into one "uncertainty" scalar loses the distinction between "the noise I already expect" and "the world changed." A homuncular reading would build one confidence dial; the biological reading requires two dissociable estimators with different temporal kernels.
- **What REE would need to endogenously measure:** a model of its OWN error statistics under the current regime (a running distribution of prediction error, not just its instantaneous value) so that "this error is large" (ACh-expected-uncertainty territory) can be told apart from "this error is inconsistent with my recent error distribution" (NE-unexpected-uncertainty territory). N5's failure is precisely the absence of this second, self-referential quantity -- surprise magnitude alone cannot substitute for it, which the probe result (spurious opens 5/5 with no shift) demonstrates empirically rather than only in theory.

## 3. Dopamine (RPE, vigor, tonic/phasic)

**On file:** 629 files. Canonical: `targeted_review_sd_012/entries/2026-03-29_sd_012_dopamine_prediction_reward_schultz1997`
(phasic RPE), `targeted_review_arc_066_tonic_vigor/entries/2026-05-10_arc_066_tonic_dopamine_vigor_niv_2007`
(tonic/vigor), `targeted_review_connectome_mech_004/entries/2026-09-09_mech_004_dopamine_value_salience_alerting_brombergmartin2010`
(value vs salience dissociation), `targeted_review_mech_054/entries/2026-08-18_mech054_two_dopamine_channels_matsumoto2009`.

- **Trigger signal:** phasic -- moment-to-moment reward-prediction error (actual minus expected value). Tonic -- long-run average reward rate.
- **Controlled variable:** phasic -- which action/state representation gets credit (learning signal, gates plasticity at corticostriatal synapses). Tonic -- response vigor / willingness to act at all (opportunity cost of passivity).
- **Timescale:** phasic, sub-second, locked to outcome or its earliest predictor; tonic, slow, integrates over many trials.
- **What it switches between:** act-now-vigorously vs conserve energy (tonic); which candidate action/state gets its value updated (phasic). Not itself an exploit/explore switch (that is LC-NE's job per Aston-Jones & Cohen) -- a documented point of potential double-booking if REE conflates the two.
- **Evidence strength:** very high; among the most replicated results in systems neuroscience.
- **REE analogue:** ARC-155's own worked measurements are dopamine-territory in function even where not so named: V3-EXQ-1067 (dacc_pe saturated at cap, effectively a phasic-error signal that has lost its dynamic range) and V3-EXQ-1104 (effort term dominated by payoff range, a vigor/opportunity-cost computation whose scale is wrong). ARC-066 (tonic-vigor architectural commitment) is the direct claim-level home for the Niv et al. reading. MECH-433/MECH-482/MECH-527/SD-061 own the exploit/explore cluster in the intake table, though per the LC-NE section above that cluster's better biological anchor is NE, not DA -- worth DC-D flagging as a possible mis-assignment.
- **Single vs distributed:** distributed at the receiving end (VTA/SNc project broadly; downstream striatal/cortical targets each locally gate plasticity or vigor), but the RPE itself is typically modelled as a single scalar broadcast -- the cleanest case in this survey of "one signal, many local consumers," which is a defensible, non-homuncular shape IF REE keeps the consumers separate rather than routing DA's signal through one arbitration node.
- **What REE would need to endogenously measure:** its own expected value baseline (to compute a prediction error, not just raw reward) and its own running average reward RATE (a genuinely different, slower-timescale statistic from the value baseline) -- REE would need both, since Niv et al.'s vigor account and Schultz's RPE account are mathematically distinct uses of "prediction," easy to conflate into a single stale error term (the failure mode ARC-155 has already measured directly: dacc_pe saturated, effort term drowned in payoff scale).

## 4. Serotonin (patience, aversive, model-based/model-free)

**On file:** 115 files. Canonical: `targeted_review_connectome_mech_002/entries/2026-09-08_mech_002_serotonin_patience_miyazaki2014`,
`targeted_review_connectome_mech_188/entries/2026-04-06_mech_188_drn_pfc_patience_miyazaki2020`,
`targeted_review_inv_053/entries/2026-04-06_inv_053_qt_serotonin_inhibition_dayan2008`,
`targeted_review_connectome_mech_188/entries/2026-04-06_mech_188_serotonin_behavioral_control_cools2008`.

- **Trigger signal:** anticipated delay to reward / aversive context requiring sustained waiting or tolerance rather than immediate switching.
- **Controlled variable:** the threshold for abandoning the current trajectory (premature commitment / premature cessation of waiting); patience.
- **Timescale:** optogenetic activation shows effects within the waiting episode itself (seconds-to-tens-of-seconds); the receptor-level (5-HT1A vs 5-HT2A/2C) and PFC synaptic effects operate over longer windows.
- **What it switches between:** persist-with-current-trajectory vs abandon-and-switch; separately, model-based deliberation vs habitual responding (Cools 2008 cluster) and active vs passive coping (Dayan 2008's Pavlovian-instrumental transfer reading).
- **Evidence strength:** the causal optogenetic result (Miyazaki 2014) is strong but the entry on file marks the REE mapping itself weak (0.60): wait-duration is a behavioural readout degenerate with respect to mechanism (limiting precision escalation, raising abandonment cost, and slowing an internal timer are all consistent with longer waits, and the paradigm has no imagined-rollout analogue -- see entry caveats).
- **REE analogue:** the intake table lists MECH-433/SD-061/ARC-065 for exploit/explore generally; serotonin's specific "stabilise exploratory rollouts across a longer horizon without collapsing early" function does not yet have a named REE mechanism distinct from the DA/NE exploration cluster -- **candidate gap**, flag for DC-D.
- **Single vs distributed:** dorsal raphe is itself heterogeneous (the Miyazaki entry notes context-dependence discovered in the 2018 follow-up: the patience effect is conditional on reward probability and timing uncertainty, i.e. not a fixed gain but state-modulated) -- again a broadcast-with-local-and-context-dependent-uptake shape, not a single dial.
- **What REE would need to endogenously measure:** its own subjective estimate of remaining time-to-resolution for the current rollout/trajectory, and separately a running estimate of reward probability/timing uncertainty for that trajectory -- since biology's patience signal is itself gated by exactly that second quantity, a naive REE "patience scalar" that ignores context-dependent gating would already be a simplification the 2018 Miyazaki follow-up (cited in-entry, not separately filed) argues against.

## 5. Basal-ganglia/thalamocortical gating and routing

**On file:** 171 (BG) + 73 (thalamocortical) files. Canonical: `targeted_review_connectome_mech_266/entries/2026-04-21_mech_266_bg_gating_oreilly2006`
(PBWM), `targeted_review_tolerance_gated_rule_availability/entries/2026-06-04_arc_063_bg_gating_wm_updating_frank2001`,
`targeted_review_q_019/entries/2026-05-16_q_019_trn_attentional_gating_mcalonan2000` (TRN),
`targeted_review_q_019/entries/2026-04-28_q_019_thalamocortical_flexibility_scott2024`.

- **Trigger signal:** D1/D2-pathway balance in striatum (learned via RL, driven by phasic DA at the moment of a candidate update); separately, TRN sector activation driven by learned attentional allocation.
- **Controlled variable:** whether PFC working-memory content updates or is protected/maintained (BG gate); which thalamic relay channel reaches cortex at all (TRN gate).
- **Timescale:** trial-by-trial (BG gating decision); session-level learned topography (TRN attentional allocation).
- **What it switches between:** update vs hold (working memory); attend vs suppress (sensory channel selection) -- this is architecturally the clearest existing biological answer to "which representations effectively influence E3," one of the ten regime decisions the user named.
- **Evidence strength:** PBWM is a foundational, well-validated computational model; TRN gating has convergent Fos + more recent optogenetic (Ahrens 2015, cited in-entry) support.
- **REE analogue:** MECH-266 directly (SD-032a's mode register, currently four operating modes each with an independent (enter,exit) pair) -- and the on-file entry (`oreilly2006`) already flags the honest mismatch: PBWM's biology is ONE gate with opposing D1/D2 tone modulated by context, not N independently-parameterised per-mode gates. MECH-266's implementation is a documented departure from its own cited biology, open per V3-EXQ-464. Q-019's sensorium loop is the TRN analogue.
- **Single vs distributed:** genuinely distributed and adversarial by construction -- Go and NoGo are two separate pathways whose balance IS the gate state; there is no third node computing a verdict. This is the single cleanest existing biological counter-example to a homuncular executive in this survey, and MECH-266's per-mode-threshold shape is the one place in the current claim set closest to re-introducing exactly that homunculus (a lookup table of per-mode thresholds functions like a small executive deciding transitions, rather than emerging from two competing tonic drives).
- **What REE would need to endogenously measure:** a single tonic context signal (biology's dopamine tone) that shifts the SAME two-pathway balance across all modes, rather than a separately-tuned threshold per mode -- i.e. the audit's own architecture may already be carrying unnecessary degrees of freedom relative to its cited source.

## 6. Salience network / anterior insula-dACC switching

**On file:** 35 (salience network) + 144 (anterior insula) + 207 (dACC) files. Canonical:
`targeted_review_connectome_mech_259/entries/2026-04-20_mech_259_salience_network_switching_menon2010`,
`targeted_review_mech_019/entries/2026-09-17_mech_019_salience_network_switching_sridharan2008`,
`targeted_review_sd_032c/entries/2026-04-25_sd_032c_salience_network_switch_menon2010`.

- **Trigger signal:** precision-weighted interoceptive/exteroceptive/social salience integrated by anterior insula (AI).
- **Controlled variable:** which large-scale network is engaged -- central-executive network (task-focused, externally-oriented) vs default-mode network (internally-oriented) -- a genuine state SWITCH, not incremental reweighting.
- **Timescale:** the causal-outflow-hub finding (Sridharan 2008, Granger causality) puts AI activity ahead of CEN/DMN transitions by a short lag (seconds).
- **What it switches between:** broad cognitive/behavioural operating regime (the user's item 10) -- externally-engaged/task mode vs internally-oriented/default mode.
- **Evidence strength:** high and well-replicated for the network-level phenomenon; the entry itself flags that fMRI cannot distinguish a genuine discrete (Schmitt-trigger) switch from a very steep sigmoidal gain function, and that the model is a two-state toggle where MECH-259 proposes a richer multi-mode vector.
- **REE analogue:** SD-032a (mode coordinator), MECH-259 directly, MECH-266, MECH-157, MECH-039 (per the intake table's "which representations influence E3; broad regime change" row).
- **Single vs distributed:** this is the biological system that comes CLOSEST to a literal single-node executive (AI as "causal outflow hub"), which is exactly why the user's explicit constraint matters here: SD-032a as currently described risks being the most direct biological warrant for a homuncular reading in the whole survey. Two mitigating facts from the source itself temper this: (a) the hub still only triggers a switch between two OTHER, already-existing, genuinely distributed networks (CEN, DMN) -- it does not itself compute or hold task content; (b) more recent work the entry does not cover suggests the "hub" role is itself state- and task-dependent rather than a fixed anatomical seat of control.
- **What REE would need to endogenously measure:** an integrated, precision-weighted salience quantity that is genuinely cross-modal (spans interoceptive/exteroceptive/social) rather than a single-channel proxy -- and, per the caveat above, evidence on whether REE's switch should be graded (steep sigmoid) or genuinely discrete (Schmitt trigger) is not settled by this literature; that is a modelling choice REE would have to test empirically, not import.

## 7. Hippocampal novelty/mismatch (CA1 comparator, novelty-driven plasticity, LC/VTA loop)

**On file:** 63 (hippocampal novelty) + 394 (CA1) + 408 (mismatch) files. Canonical:
`targeted_review_inv_063/entries/2026-09-08_inv_063_ca1_generalized_novelty_signal_larkin2014`,
`targeted_review_mech_205/entries/2026-04-07_mech_205_ca1_mismatch_detector_duncan2011`,
`targeted_review_connectome_mech_189/entries/2026-06-09_mech_189_hippocampal_vta_novelty_gate_lismangrace2005`,
`targeted_review_hippocampal_planning_mechanisms/entries/2026-06-13_mech_149_hippocampal_vta_novelty_loop_lisman2005`.

- **Trigger signal:** mismatch between CA3-predicted and CA1-observed input (comparator function); propagates to VTA via subiculum/NAc.
- **Controlled variable:** hippocampal plasticity gain (more plastic on novelty) and VTA dopamine burst (novelty as an intrinsic reward-like signal that primes further encoding) -- the Lisman-Grace loop.
- **Timescale:** fast, per-event comparator (each new observation vs prediction); the VTA loop's downstream consequences (dopamine burst, plasticity gating) act on the following encoding window.
- **What it switches between:** encode-as-new vs treat-as-already-modelled; separately gates which material becomes eligible for offline replay (persisting into sharp-wave ripples per Larkin 2014).
- **Evidence strength:** the comparator idea is old and well-supported; Larkin 2014's specific finding (CA1 signal is a generalised "novelty is present somewhere" broadcast, NOT spatially specific to what changed, despite CA3 showing no such elevation) is a documented COMPLICATION for any REE design assuming novelty signals are content-specific rather than global broadcasts.
- **REE analogue:** MECH-205 (surprise-gated replay, direct architectural analogue of the CA1 comparator), Q-111's cross-controller-interference question sits directly downstream of this: if REE's own novelty signal is (like CA1's) undifferentiated across which specific representation changed, then any single controller reading it cannot itself distinguish "the world changed" from "some world changed," which bears on N5's detector-failed-to-recognise-the-shift problem from a different, representational-granularity angle than the ACh/NE gap in section 2.
- **Single vs distributed:** CA1 broadcasts, VTA reads and re-broadcasts a different downstream signal (dopamine burst) -- two-hop broadcast chain, no single arbitration node; but the content itself is undifferentiated (a genuine finding, not an REE design choice), so "distributed" here does not mean "informationally rich," it means "many receivers of one coarse signal."
- **What REE would need to endogenously measure:** a genuine prediction-vs-observation comparator with its own error signal (distinct from and upstream of any downstream scoring), and REE would need to decide -- as an empirical, falsifiable question, not a default -- whether its own novelty broadcast should stay similarly coarse (biology's answer) or whether REE actually needs the finer-grained "which representation changed" signal N5's failure suggests would help; the literature does not license assuming REE needs to out-perform the biological baseline here.

## 8. Arousal

**On file:** 367 files, largely overlapping with LC-NE (`targeted_review_connectome_mech_178/entries/2026-04-06_mech_178_lc_ne_behavioral_berridge2003`
is the canonical arousal-state entry) and homeostatic-override entries below.

- **Trigger signal:** integrated interoceptive/threat/metabolic state plus LC-NE tone; not a single dedicated arousal detector but a convergence point of several of the systems above.
- **Controlled variable:** global behavioural-state readiness (waking vs sleep-permissive states; inverted-U of NE level vs cognitive performance, per Berridge & Waterhouse 2003).
- **Timescale:** slow, state-level (minutes to hours), distinct from LC's fast phasic mode.
- **What it switches between:** waking-engaged vs sleep-permissive states; within waking, an inverted-U of performance vs arousal level (both insufficient and excess NE impair function).
- **Evidence strength:** high for the LC-as-arousal-driver claim; the entry itself flags that the sleep-specific pathway (elevated NE -> REM suppression) is a narrower, less directly evidenced sub-claim than the general waking-state claim.
- **REE analogue:** the intake table's "campaign presets" note (babbling phases, frozen/unfrozen retained sets set by the harness) is functionally an externally-imposed arousal/state variable -- REE currently has no endogenous global-state variable of this kind at all; this is a genuine, not just under-tuned, absence.
- **Single vs distributed:** arousal is explicitly a CONVERGENCE state, not a separate controller -- it is what several systems (LC-NE, homeostatic drives, threat circuitry) jointly produce, read out downstream by many consumers. Building one "arousal module" for REE would misrepresent the biology; the more faithful move is to let existing per-system signals (once each exists) sum or gate into a shared readout, not to add a new upstream node.
- **What REE would need to endogenously measure:** nothing NEW in principle -- arousal is a derived quantity over signals sections 1-4 already require REE to have. The gap is that REE presently lacks essentially all of the constituent per-system signals (native error-statistics model, tonic vigor estimate, threat integral with onset information -- CeA's onset re-probe found the fast threat route reads a slow saturated integral and carries no onset information at all), so there is currently nothing to converge.

## 9. Oscillatory/synchrony gating (communication-through-coherence, theta/gamma) -- CONTESTED, label accordingly

**On file:** 344 (oscillation) + 76 (synchrony) + 4 (communication-through-coherence, verbatim) + 71 (theta/gamma) files.
Canonical: `targeted_review_connectome_mech_499/entries/2026-08-25_mech_499_communication_through_coherence_fries2015`,
`targeted_review_connectome_mech_499/entries/2026-08-25_mech_499_theta_gamma_memory_matching_biel2021`,
`targeted_review_object_files_feature_binding/entries/2026-06-06_mech_044_communication_through_coherence_fries2015`.

- **Trigger signal:** relative phase-locking (synchrony) between a sending population's gamma rhythm and a receiving population's excitability cycle; slower alpha/beta carries top-down arbitration of which gamma channel wins; theta paces the overall sampling cycle.
- **Controlled variable:** which of several competing input streams is effectively TRANSMITTED to a shared downstream target (a routing/gating function, not content creation).
- **Timescale:** gamma cycle (tens of milliseconds) nested inside slower alpha-beta (attentional arbitration, hundreds of ms) and theta (sampling cycle).
- **What it switches between:** which candidate representation, among several converging on one downstream population, gets through -- the "which representations effectively influence E3" item on the user's list, at the level of a physical routing mechanism rather than a symbolic gate.
- **Evidence strength:** the CTC mechanism itself (phase-locked transmission is real and behaviourally consequential) is well-replicated primate visual-cortex work; the label CONTESTED applies specifically to any stronger claim that oscillatory coherence AGGREGATES or SYNTHESISES content across many streams into one composite state (the on-file entry marks this reading `mixed`, not `supports`: CTC is a filter/router, not a constructor, and the REE-adjacent claim MECH-499 makes is the stronger, unsupported reading).
- **REE analogue:** MECH-499 (explicitly, and explicitly flagged mixed -- do not cite as settled), MECH-270 (ephaptic/field-effect confidence/eligibility readout, a narrower and better-supported claim than MECH-499's).
- **Single vs distributed:** intrinsically distributed and competitive by construction (multiple presynaptic populations, one postsynaptic target, no third node computing a winner -- the winner is whichever input achieves tighter phase-lock) -- a strong biological argument AGAINST a homuncular router, but ALSO evidence against reading oscillatory coherence as a content-synthesising "now-state," which is the failure mode this section's source entry warns MECH-499 risks.
- **What REE would need to endogenously measure:** REE has no timing/phase representation of this kind at all currently (D0 -- no code exists to intervene on); if pursued, the minimal endogenous requirement would be a relative-timing or relative-priority signal between competing candidate representations converging on the same consumer, which is a much narrower ask than "a unified oscillatory field," and the literature itself argues against building the latter.

## 10. Threat circuitry (amygdala fast route, PAG freeze, defensive modes)

**On file:** 307 (amygdala) + 118 (PAG) + 108 (freeze) files. Canonical:
`targeted_review_threat_modulated_defensive_path_selection/entries/2026-08-01_mech_321_prefrontal_pag_imminence_shift_mobbs2007`,
`targeted_review_homeostatic_override/entries/2026-04-22_homeostatic_override_vmhdm_collateral_pathways_wang2015`,
`targeted_review_arc_121/entries/2026-09-04_arc_121_dissociable_amygdala_circuits_namburi2015`,
`targeted_review_connectome_mech_357/entries/2026-08-09_mech_357_il_pv_freeze_suppression_avoidance_ho2025`.

- **Trigger signal:** threat imminence/proximity (continuously varying), interacting multiplicatively with anticipated harm magnitude (Mobbs 2007's key finding: the vmPFC->PAG regime shift is steepest specifically under high anticipated pain, not proximity alone).
- **Controlled variable:** which brain region is IN CONTROL of defensive behaviour -- a genuine categorical handoff (vmPFC-dominant "cognitive" defensive planning at low imminence -> PAG-dominant reflexive action at high imminence), not merely a bigger response in the same system.
- **Timescale:** the vmPFC->PAG shift tracks imminence continuously but the CONTROL handoff itself is reported as a genuine regime change (a step, not a ramp) once imminence crosses into "contact anticipated."
- **What it switches between:** deliberative/distant threat-response vs reflexive/proximate threat-response; separately, VMHdm's single broadcast source fans out to PAG (freezing) vs AHN (avoidance) depending purely on which downstream target's threshold is crossed -- a clean broadcast-with-downstream-arbitration case, and MECH-279's dlPAG GABAergic gate is named as exactly this downstream node.
- **Evidence strength:** high (Mobbs 2007 is top-tier, precisely controlled human fMRI; Wang 2015's optogenetic terminal-stimulation dissociation is causal circuit-level rodent evidence).
- **REE analogue:** MECH-279, MECH-280, MECH-357, MECH-489/SD-099 (per the intake table's "enter/leave defensive states" row), ARC-156 directly. **Two of ARC-156's own measured instances are in this cluster**: V3-EXQ-1106 (MECH-287's release path needs a movement-independent source -- it cannot accrue while frozen, by the mechanism's own design) and V3-EXQ-1107 (the exit lock requires `||z_harm_a|| < 0.8`, and that quantity is pinned while frozen next to a hazard -- an exit condition that is a function only of evidence the suppressed behaviour itself would produce, which is precisely ARC-156's stated failure mode). CeA's onset re-probe (GFLAG-0556/0557, cited in the orchestrator's capture notes) found the fast threat route reads a slow, saturated integral with no onset information -- i.e. REE's current implementation lacks the FAST, onset-sensitive component (the amygdala's textbook "fast route") that this literature cluster treats as foundational, not optional.
- **Single vs distributed:** VMHdm/PAG/AHN is a clean broadcast-with-competing-downstream-thresholds architecture (Wang 2015); Namburi 2015 additionally shows the amygdala's INPUT stage already has two anatomically separate, synaptically opposed, causally competitive populations for positive vs negative association -- there is no single "threat evaluator" even at the earliest stage. The one partial counter-note: Ho 2025 found the specific infralimbic-PV freeze-suppression signal is present almost immediately after first shock and does NOT scale with learning, which argues that at least this one termination pathway is closer to a fixed, pre-wired switch than to a graded, learned controller -- a useful concrete caution against assuming every node in this system is itself adaptive.
- **What REE would need to endogenously measure:** a FAST, onset-sensitive threat estimate (currently absent per the CeA re-probe) as well as the slow integral REE already has; and, separately, at least one termination input that continues to change WHILE the organism is suppressed (time-integrating, interoceptive, or exogenous-but-sensed-without-acting) -- this is ARC-156's own already-stated requirement, independently re-derived here from the biology rather than assumed.

## 11. State-dependent coordination via ephaptic/field effects -- LABEL SPECULATIVE

**On file:** 23 (ephaptic) + 12 (field effect) files. Canonical:
`targeted_review_regulation_first_authority_field/entries/2026-09-08_mech_534_ephaptic_coupling_explains_trial_variability_pinotsis2026`,
`targeted_review_connectome_mech_270/entries/2026-04-21_mech_270_ephaptic_coupling_anastassiou2011`,
`targeted_review_connectome_mech_270/entries/2026-04-24_mech_270_field_effects_theta_sharpwave_anastassiou2010`.

- **Trigger signal:** local field potential fluctuations arising from population-level activity, which then feed back onto the membrane excitability of nearby neurons (a genuinely circular-causality claim, not merely emergent-and-inert).
- **Controlled variable:** trial-by-trial variability in cortical oscillatory power/excitability -- the field is proposed to act as an independent causal factor, not purely a readout.
- **Timescale:** fast (LFP-scale, sub-second) but with effects on excitability that could plausibly persist across a trial.
- **Evidence strength:** the newest, most directly relevant paper (Pinotsis & Miller 2026, verified above at confidence 0.62 on file) reports field-to-neuron coupling STRONGER than neuron-to-field coupling in prefrontal LFP during a delayed-saccade task -- the load-bearing empirical detail for any claim that the field is a causal medium rather than a summary statistic. This is genuinely one dataset with model-based coupling estimation, not an intervention on the field itself, and the paper's own alternative explanations (neuromodulation, uncertainty encoding, excitability -- i.e. exactly the precision machinery sections 1-4 already cover) are not excluded. **Label: SPECULATIVE.** The theoretical leap from "field effects are measurably real and directionally circular" to "field coherence functions as a distributed COORDINATION mechanism across REE's many latent streams" is not made or tested by any paper on file (see section 9's identical caution re MECH-499).
- **REE analogue:** MECH-534, MECH-270; the "regulation-first authority field" literature review directory name signals this is already recognised internally as the speculative end of the corpus.
- **Single vs distributed:** by construction distributed and emergent (a field arising from and acting back on a whole population, no localised source) -- the most naturally non-homuncular mechanism in this entire survey, BUT for exactly that reason also the hardest to operationalise as a testable REE mechanism (a field with no localised source is not easily gated, measured, or ablated on demand).
- **What REE would need to endogenously measure:** nothing exists in REE for this today (D0), and per the entry's own brake, the correct next step is NOT to build a field mechanism but to ask whether REE's existing, better-evidenced precision/gain machinery (sections 1-4) already accounts for the coordination the user is asking about, before reaching for the more speculative substrate. Recommend DC-D treat this as the lowest-priority candidate for the falsifiable-hypothesis step (audit step 6), explicitly because the alternative, non-speculative explanations are not yet exhausted.

## 12. Homeostatic/metaplastic plasticity gating

**On file:** homeostatic-override cluster is well covered (`targeted_review_homeostatic_override/` directory,
9 entries, e.g. `2026-04-22_homeostatic_override_orexin_motivated_arousal_bjorness2024`,
`2026-04-22_homeostatic_override_lh_gaba_vta_barbano2016`), but **metaplasticity specifically is a genuine
corpus gap** (0 hits for "metaplast", 1 loose hit for "homeostatic plasticity"). Gap filled below by one
verified PubMed lookup, per `/lit-pull` discipline, not filed as a new scored entry (a governance action
outside this worker's remit; cited here for DC-D/governance to file properly if adopted).

**New citation (verified via PubMed, not previously on file):** According to PubMed, Abraham WC (2008).
"Metaplasticity: tuning synapses and networks for plasticity." *Nature Reviews Neuroscience* 9(5):387.
[DOI](https://doi.org/10.1038/nrn2356), PMID 18401345. Abstract (verbatim from PubMed): activity-dependent
mechanisms collectively termed metaplasticity regulate WHEN and HOW MUCH synaptic plasticity itself is
permitted to occur, as distinct from plasticity's own magnitude/direction (the BCM sliding-threshold family
this paper reviews is the formal ancestor: the LTP/LTD threshold itself slides as a function of recent
average postsynaptic activity, so a synapse that has been very active recently requires MORE subsequent
activity to potentiate further, and vice versa).

- **Trigger signal:** recent history of postsynaptic activity (BCM) or, more generally, recent history of
  plasticity itself (has this synapse/circuit changed a lot recently, in either direction).
- **Controlled variable:** not the synaptic weight itself, but the THRESHOLD/GAIN governing whether the
  next candidate weight-change is permitted to proceed and by how much -- a plasticity-of-plasticity control,
  operating one level above the object-level learning signals sections 1-4 describe.
- **Timescale:** slower than any single learning event; integrates over the recent window of plasticity
  events themselves (hours-to-days in the biological literature, which for REE would map onto multiple
  training episodes rather than within-episode ticks).
- **What it switches between:** freely plastic vs protected/stabilised, and separately (via homeostatic
  synaptic scaling, the companion mechanism this literature usually reviews alongside BCM) globally
  up-scaled vs down-scaled synaptic gain in response to prolonged under- or over-activity -- directly the
  user's item "freeze learning versus reopen plasticity," at the mechanistic level rather than the
  behavioural-state level MECH-398/MECH-207 already cover.
- **Evidence strength:** high as a general principle (BCM is one of the best-supported plasticity-control
  theories, independently converged on via bidirectional plasticity data across many systems); the specific
  mapping to REE's plasticity-freeze mechanisms (MECH-398 ACh disinhibition, MECH-207 ACh encode/consolidate
  switch) is D0 -- no REE mechanism currently reads its OWN history of plasticity events as a control signal.
- **REE analogue: none currently identified.** MECH-398/MECH-207/MECH-474 (the intake table's own
  "freeze vs reopen plasticity" row) implement WHEN plasticity is gated by an external state signal (ACh
  level), not by the SYSTEM'S OWN recent plasticity history -- a genuinely distinct axis. This is the
  clearest concrete gap this survey turned up: N5's wholesale-quarantine-and-rebabble revision path is one
  data point suggesting REE currently has only a binary (frozen/unfrozen) plasticity control, with no
  graded, self-referential metaplastic layer that could have made the quarantine partial rather than total.
- **Single vs distributed:** distributed by construction -- metaplasticity is a LOCAL, per-synapse (or
  per-population, for homeostatic scaling) property; there is no metaplasticity "controller," only a
  local rule that reads local history.
- **What REE would need to endogenously measure:** a running account of ITS OWN recent plasticity events
  (magnitude and direction of recent weight changes to a given head/module), separate from and upstream of
  the ACh-style external gating signal MECH-398/MECH-207 already use -- this is a second, genuinely new kind
  of endogenous signal (self-referential over the learning process, not over the environment), not a
  relabelling of an existing one.

---

## Cross-cutting synthesis (bounded to this worker's remit -- full step-4/6-9 synthesis is DC-D's job)

**Tally, single-node vs distributed, across the 12 mechanisms above:** none are cleanly single-node in the
sense the user's constraint warns against. The closest candidates are (a) LC as a single anatomical
broadcast SOURCE (but with universally local, independent uptake -- section 1) and (b) the anterior-insula
"causal outflow hub" framing of the salience network (section 6), which is the one place in this survey
where the cited literature's own language ("switches," "hub") most directly risks licensing a homuncular
reading if lifted uncritically -- flagged explicitly above for DC-D. Every other mechanism is either
two-or-more mutually antagonistic populations whose BALANCE is the state (BG D1/D2, amygdala NAc-/CeM-
projectors), a broadcast-with-competing-downstream-thresholds fan-out (VMHdm->PAG/AHN, CA1->VTA), or a
purely local rule with no controller at all (metaplasticity, communication-through-coherence's routing).

**The recurring endogenous-measurement gap, stated once rather than eleven times:** the single fact this
survey turns up most often is that biological regime-selection signals are near-universally computed FROM
THE ORGANISM'S OWN STATISTICS OVER ITS OWN RECENT EXPERIENCE (its own error distribution, its own recent
plasticity history, its own reward-rate history, its own timing-uncertainty estimate) rather than from raw,
instantaneous, environment-facing quantities. N5's failure is the clearest existing REE instance of exactly
this gap (an instantaneous surprise magnitude standing in for a genuine unexpected-uncertainty estimate,
which by definition requires a model of what surprise SHOULD look like right now). This generalises: several
of the ARC-155-documented failures (dacc_pe saturated at its cap 100% of ticks; effort term drowned by
payoff scale) are the SAME shape of error -- an operating point set against a raw or externally-anchored
scale rather than against REE's own endogenous estimate of that quantity's distribution -- which is ARC-155's
claim restated from the biology side rather than derived independently. This literature corroborates
ARC-155/Q-111 rather than adding a new claim.

**One clear net-new gap for DC-D to weigh:** metaplasticity (section 12) is a mechanism class with no REE
analogue at all, distinct in kind from the "freeze vs reopen" binary REE already has (MECH-398/MECH-207),
because it is self-referential over the learning process itself rather than externally gated. Whether this
belongs in the falsifiable-hypothesis step (audit step 6) is DC-D's call, not this worker's -- flagged here
only because "REE analogue: none" for this one item is a genuine literature-corpus finding, not a search
failure (0 hits for "metaplast" is confirmed, not merely under-searched: the topic exists at the concept
level in `homeostatic_override` entries but none of those address plasticity-of-plasticity specifically).

**What this record does NOT do, restated:** it does not decide the shape of REE's dynamic-control failure
(audit step 4), does not propose REE hypotheses or falsifiers (step 6-7), and does not weigh in on A1
ordering (step 8). Those belong to DC-D, reading this alongside DC-A's causal-connectivity map and DC-B's
imposed-regime corpus.
