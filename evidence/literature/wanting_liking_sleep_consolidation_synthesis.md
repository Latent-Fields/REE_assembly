# Lit synthesis: anticipatory wanting + sleep-dependent schema consolidation

**Created:** 2026-05-08
**Type:** consolidation synthesis (no new fetches; cross-references existing corpus
entries to anchor two open design memos)
**Anchors:** `mech188_vs_mech295_dual_path.md`, `sustained_drive_anticipatory_wanting.md`,
EXQ-538 (sleep ablation of SD-049 Phase 2), EXQ-539+ (sustained-drive).

The corpus already contains targeted lit-pulls on every claim relevant to the
2026-05-08 EXQ-536/514f findings. This document consolidates them into a single
reading on (a) why the SD-012 multiplier needs a sustained-drive component and
(b) why SD-049 Phase 2 schema discrimination should depend on sleep
consolidation. It identifies the experimental gaps that EXQ-538 and EXQ-539
directly address.

## Part 1 — Sustained / anticipatory wanting (anchors Task 3 design memo)

### What the existing literature establishes

**Drive does not directly produce approach.** Drive routes through hedonic
value (liking) and learned anticipatory wanting before reaching action
selection. Foundational evidence:

- **Dickinson & Balleine 1994** *(Animal Learn Behav)* — drive-state shifts do
  NOT directly rewire instrumental responding without intervening outcome
  experience. The cleanest behavioural demonstration that drive must route
  through experienced hedonic value.
  Path: `targeted_review_mech295_liking_approach_bridge/entries/2026-04-26_mech_295_incentive_learning_dickinson1994/`
- **Berridge & Robinson 1998** *(Brain Res Rev)* — wanting/liking dissociation:
  dopaminergic wanting can be amplified without amplifying liking
  (DAT-knockdown in Pecina 2003); liking can change without changing wanting.
  Implication for SD-012: instantaneous-drive multiplier collapses when
  consumption restores energy, but wanting (the phasic motivational state) does
  not collapse on the same timescale.
  Path: `targeted_review_connectome_mech_117/entries/2026-03-29_mech_117_wanting_liking_dopamine_berridge1998/`
- **Smith, Berridge & Aldridge 2011** *(PNAS)* — VP single-unit recording
  during sodium depletion: drive state change does NOT directly rewire
  cue-evoked motivational firing. Palatability code recodes first; cue firing
  follows on subsequent trials. **The cleanest mechanistic version of "drive
  does not write directly to action selection."**
  Path: `targeted_review_mech295_liking_approach_bridge/entries/2026-04-26_mech_295_vp_hedonic_coding_smith2011/`
- **Berridge & Kringelbach 2015** *(Neuron)* — review-level architectural
  statement: liking is a necessary input to motivated approach, not a passive
  readout. The most explicit theoretical statement of the bridge architecture
  MECH-295 implements.
  Path: `targeted_review_mech295_liking_approach_bridge/entries/2026-04-26_mech_295_pleasure_systems_review_berridge2015/`

**Drive timescales are slower than instantaneous.** Two key entries from the
SD-012 corpus:

- **Schultz 1997** *(Science)* — phasic dopamine RPE has a sub-second temporal
  signature, but tonic dopamine encoding of motivational state operates over
  much longer windows (minutes-hours). Behaviourally, the operative wanting
  signal in operant tasks integrates over the latter.
  Path: `targeted_review_sd_012/entries/2026-03-29_sd_012_dopamine_prediction_reward_schultz1997/`
- **Keramati 2014** *(PLoS Comput Biol)* — homeostatic RL formalisation:
  drive-state-modulated reward is the integrated deviation from setpoint, not
  the instantaneous deviation. Keramati's formal derivation prescribes
  `drive_state * benefit` over a window, not instantaneous-drive ×
  instantaneous-benefit.
  Path: `targeted_review_sd_012/entries/2026-03-29_sd_012_homeostatic_rl_keramati2014/`
- **Cassidy 2017** *(Neuron / Mol Psychiatry)* — hunger-satiety modulation of
  reward sensitivity in human fMRI: BOLD anticipatory-cue response is
  hunger-modulated, but the modulation persists for tens of minutes after the
  cue, well past consummatory satiation. Direct evidence of post-consumption
  wanting persistence.
  Path: `targeted_review_sd_012/entries/2026-04-13_sd_012_hunger_satiety_reward_sensitivity_cassidy2017/`
- **Aponte 2011** *(Nat Neurosci)* — AgRP neuron optogenetics: AgRP firing
  drives sustained motivational seeking that persists past stimulation offset.
  Hunger drive is encoded as a slow-decay state, not an instantaneous read.
  Path: `targeted_review_sd_012/entries/2026-04-05_sd_012_agrp_hunger_goal_orchestration_aponte2011/`
- **Livneh 2017** *(Nature)* — hypothalamic-cortical hunger gating maintains
  cue-response amplification across longer-than-consummation windows.
  Path: `targeted_review_sd_012/entries/2026-04-05_sd_012_homeostatic_gate_cue_response_livneh2017/`
- **Stuber 2023** *(Cell)* — review of motivation neurocircuits emphasising
  the slow-state nature of drive integration.
  Path: `targeted_review_sd_012/entries/2026-04-13_sd_012_neurocircuits_motivation_stuber2023/`
- **Ye 2023** *(Neuron)* — zona incerta dopamine encodes vigour as an
  integrated state variable.
  Path: `targeted_review_sd_012/entries/2026-04-13_sd_012_zona_incerta_dopamine_vigor_ye2023/`

### Implication for SD-012 amendment

The existing literature **strongly supports** Option 1 (sustained-drive EMA) in
the design memo. The multiplier-with-instantaneous-drive form
`(1 + drive_weight * drive_level)` does not match how any of the cited
mechanisms operate. The animal data (Aponte 2011, Livneh 2017, Cassidy 2017)
is consistent with a trace half-life on the order of minutes — in our 200-step
episodes, that maps to roughly 30-60 steps trace decay. The 35-step half-life
proposed in the design memo (`alpha_drive_trace = 0.02`) is within that range.

**Lit-grounded acceptance for EXQ-539:**
- Predicted `mean_drive_on_contact` lift under ARM_TRACE: from 0.005 (instantaneous
  collapse) to >= 0.10 (slow-trace persistence). This is what Aponte / Livneh /
  Cassidy predict for any consumption-followed-by-cue regime.
- Failure mode if alpha is too aggressive (~0.5): trace collapses too fast,
  outcome resembles ARM_OFF. Failure mode if alpha is too slow (~0.001): trace
  becomes constant, loses regime selectivity.

### Open lit gap (worth a future fresh pull)

The exact post-consumption wanting persistence half-life in operant studies
under different deprivation regimes is not consolidated in our corpus. The
existing entries establish the *direction* (sustained > instantaneous) but not
the *quantitative window*. A future pull on PIT (Pavlovian-Instrumental
Transfer) decay-time data would tighten the EMA setpoint. Tag this as
**LIT-PULL-PENDING-PIT-DECAY-TIME** for the planning queue.

## Part 2 — Sleep-dependent schema consolidation (anchors EXQ-538)

### What the existing literature establishes

The SD-017 corpus already has the foundational hippocampal-replay-necessity
papers:

- **Girardeau et al. 2009** *(Nat Neurosci)* — selective SWR suppression
  during post-task sleep impairs spatial memory consolidation. **The
  load-bearing causal evidence that sleep replay is not optional for schema
  formation.**
  Path: `targeted_review_sd_017/entries/2026-04-05_sd017_girardeau_2009_ripple_suppression_spatial/`
- **Ego-Stengel & Wilson 2010** *(Hippocampus)* — independent replication of
  Girardeau using a different ripple-disruption protocol. Robust replication
  of necessity.
  Path: `targeted_review_sd_017/entries/2026-04-05_sd017_ego_stengel_wilson_2010_ripple_disruption/`
- **Wikenheiser & Redish 2015** *(Nat Neurosci)* — hippocampal theta-sequences
  encode goal-directed trajectory rollouts; these are the same sequences SWR
  replay re-instantiates offline. Bridges waking-hippocampal goal coding to
  sleep replay.
  Path: `targeted_review_sd_017/entries/2026-04-05_sd017_wikenheiser_2015_theta_goal_sequences/`
- **Aleman-Zapata 2022** *(Nat Comm)* — closed-loop SWR-triggered replay
  manipulation. The most direct intervention-style evidence.
  Path: `targeted_review_sd_017/entries/2026-04-05_sd017_aleman_zapata_2022_sleep_ripple_necessity/`

The sleep-phase-mechanisms corpus extends this to schema integration and
homeostatic balance:

- **Diekelmann & Born 2010** *(Nat Rev Neurosci)* — review-level statement of
  hippocampus-leads-neocortex replay during NREM consolidation. The
  schema-integration framing closest to what SD-049 Phase 2 needs.
  Path: `targeted_review_sleep_phase_mechanisms/entries/2026-04-05_mech121_nrem_replay_hippocampus_neocortex_diekelmann2010/`
- **Tononi & Cirelli 2014** *(Neuron)* — synaptic homeostasis hypothesis (SHY):
  SWS down-scales synapses globally to preserve signal-to-noise. The
  computational implication is that classifier heads benefit from
  global down-scaling pressure between training episodes — exactly what 514f
  did NOT have (the classifier loss diverged in P0 with no offline
  recalibration).
  Path: `targeted_review_sleep_phase_mechanisms/entries/2026-04-05_mech120_shy_synaptic_normalisation_tononi2014/`
- **Staresina 2015** *(Nat Neurosci)* — spindle-coordinated theta-gamma
  coupling in human NREM. The mechanism by which slow-wave activity coordinates
  precise hippocampal replay events with neocortical schema slots.
  Path: `targeted_review_sleep_phase_mechanisms/entries/2026-04-05_mech122_spindle_coordination_theta_gamma_staresina2015/`
- **Walker 2009** *(Curr Opin Neurobiol)* — REM-dependent precision
  recalibration. Sleep is not just SWS consolidation; REM contributes
  generalisation pressure that schema discrimination needs.
  Path: `targeted_review_sleep_phase_mechanisms/entries/2026-04-05_mech123_rem_precision_recalibration_walker2009/`
- **Hobson 2012** *(Front Neurosci)* — REM as offline prior reset under
  free-energy framing. Bridges Walker 2009 to active-inference / predictive
  coding architecture.
  Path: `targeted_review_sleep_phase_mechanisms/entries/2026-04-05_mech123_rem_free_energy_prior_reset_hobson2012/`
- **Lansink et al. 2009** *(PLoS Biol)* — hippocampus-leads-striatum SWR
  replay (this is the paper I cited in the EXQ-538 docstring; it is in the
  corpus elsewhere — `targeted_review_systems_consolidation_waking_propagation/`
  entries reference it. Verify path during next governance walk.)

### Implication for EXQ-538

The existing literature **strongly supports** the EXQ-538 hypothesis. Five
distinct lines of evidence converge on the prediction that turning sleep on
should recover SD-049 Phase 2 identity discrimination:

1. **Causal sleep-replay necessity** (Girardeau 2009, Ego-Stengel & Wilson
   2010, Aleman-Zapata 2022): without offline replay, schema encoding is
   structurally incomplete. 514f ran with sleep OFF; it should fail by
   construction under this prediction. **Confirms.**
2. **Hippocampus-cortex schema integration** (Diekelmann & Born 2010): the
   resource-identity classifier head is exactly the kind of "neocortical
   schema slot" that needs hippocampal-led replay to consolidate.
3. **Synaptic homeostasis** (Tononi & Cirelli 2014): the classifier-loss
   divergence in 514f's P0 (loss 2.92 → 3.97) is the signature of an
   undampened, perpetually growing weight space — exactly what SHY downscaling
   would prevent.
4. **REM generalisation** (Walker 2009, Hobson 2012): probe accuracy is a
   generalisation test; REM is the literature's best candidate phase for
   generalisation-pressure during identity-discrimination training.
5. **Striatum-cortex consolidation propagation** (Lansink 2009): the bridge
   between hippocampal replay and the systems where the classifier weights
   live.

**Lit-grounded acceptance for EXQ-538:**
- C3a (probe_acc_neighborhood >= 0.6 in any sleep arm) is the critical
  experimental gap: no existing study tests an SD-049-class identity
  classifier under sleep-on vs sleep-off in a controlled environment. EXQ-538
  is novel evidence on this axis.
- C3b (classifier loss converges in any sleep arm) follows directly from
  Tononi 2014 SHY prediction and is the most lit-saturated criterion.
- C4 (≥0.10 absolute probe lift over ARM_OFF) is the effect-size threshold
  for "real, not noise."

### Open lit gaps for EXQ-538 follow-ups

- **Phase A K-cycle period (K=3) literature anchor:** the 503 corpus uses
  K=1 (every-episode); biology typically integrates over 4-12 episodes.
  Pull on inter-bout sleep-cycle pressure in operant or maze training.
  Tag: **LIT-PULL-PENDING-INTER-BOUT-SLEEP-CYCLE-PRESSURE**.
- **Identity-classifier specifically (vs general spatial / temporal memory):**
  the SD-049 case is a multi-class discrimination task, not the spatial-memory
  task most ripple-disruption studies use. Worth a focused pull on whether
  multi-class concept learning shares the same SWR-dependence as spatial.

## Part 3 — Cross-cut: how Tasks 2, 3, 4 fit together

The diagnostic from EXQ-536a (drive-vs-benefit anti-correlation) and the
diagnostic from EXQ-514f (classifier divergence under reef) both have the
same architectural shape: **online learning under prediction-loss-dominated
gradients fails to build the right structure**. The literature names this
explicitly across two different domains:

- For motivation: Berridge / Smith 2011 / Dickinson & Balleine show that
  online drive does not directly write to action selection — there is a
  necessary intermediate (liking, learned wanting) that integrates over a
  longer window than the consummatory pulse.
- For schema: Tononi / Diekelmann / Walker show that online weight updates do
  not build correct schema discrimination — there is a necessary offline
  consolidation that down-scales noise and integrates evidence across episodes.

REE-V3 has the substrate for both (MECH-216 schema readout, MECH-186 valence
floor, SD-017 sleep, Phase A SleepLoopManager) but is currently running
behavioural experiments with both off. The corpus literature predicts these
experiments should fail under those configurations. **They do.** The
proposed EXQ-538 (turn sleep on) and EXQ-539 (turn sustained drive on) are
direct, lit-grounded, falsifiable interventions.

## Recommended evidence_quality_note additions

To the candidate claims that the design memos depend on:

- **MECH-306 (sustained_drive_trace, proposed)** — register with
  evidence_quality_note: "Lit anchors: Schultz 1997, Aponte 2011, Livneh 2017,
  Cassidy 2017, Keramati 2014. Aggregate lit_conf ~0.78 across SD-012 corpus.
  Animal data supports trace half-life on the order of 30-200 environment
  steps. EXQ-539 is the V3 falsifiability test. PIT decay-time gap noted as
  LIT-PULL-PENDING."
- **SD-017 (sleep substrate)** — already at exp_conf=0.775 / lit_conf=0.901
  per spec section 0; the EXQ-538 design pre-registers the next
  behavioural-class evidence on this claim. No update needed until 538 lands.
- **MECH-295 (weak liking-bridge)** — the existing 6-entry pull's
  recommended evidence_quality_note already covers strong vs weak necessity.
  EXQ-536c/d/e (per `mech188_vs_mech295_dual_path.md`) is the missing
  symmetric-blockade test. No update needed until 536c-e land.

## Confidence verdict

Aggregate lit confidence on the two design directions:
- **Sustained-drive amendment (EXQ-539)**: ~0.78 (mean of SD-012 corpus
  entries directly supporting the slow-trace direction).
- **Sleep ablation of SD-049 Phase 2 (EXQ-538)**: ~0.85 (mean of sd_017 +
  sleep-phase-mechanisms entries supporting the schema-consolidation
  prediction).

Both are well above the 0.6 floor for "design proceed." Neither is at the
~0.95 ceiling that would let us promote on lit alone. Both are exactly the
kind of well-anchored experimental questions that should produce strong
governance signal when the V3 evidence lands.

## See also (cross-references)

- `targeted_review_mech295_liking_approach_bridge/` (6 entries, 2026-04-26)
- `targeted_review_sd_012/` (8 entries, 2026-03-29..2026-04-13)
- `targeted_review_sd_017/` (4 entries, 2026-04-05)
- `targeted_review_sleep_phase_mechanisms/` (5 entries, 2026-04-05)
- `targeted_review_connectome_mech_117/` (2 entries)
- `targeted_review_connectome_mech_186/`, `_mech_187/`, `_mech_216/` for
  adjacent prior art on valence/wanting
- `targeted_review_systems_consolidation_waking_propagation/` for the
  Lansink-class striatal-replay bridge
- `targeted_review_mech285_sleep_replay_seed/` for the V_s-staleness sleep
  replay sampler this could later feed
