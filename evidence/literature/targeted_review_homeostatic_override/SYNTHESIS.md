# SYNTHESIS -- Homeostatic Override Literature Pull

**Session:** cowork-2026-04-22-exq471-followup / wave_1 / lit-pull-homeostatic
**Date:** 2026-04-22
**Trigger:** V3-EXQ-471 fishtank visualization showed catatonic-locked agent with energy depleting to zero, no homeostatic override breaking the harm-stream lock-in.
**Target claims:** SD-012 (drive-modulated goal seeding), SD-036 (GABAergic cross-stream decay), MECH-279 (PAG GABAergic freeze gate), SD-032a (SalienceCoordinator).
**Coverage:** 13 papers across 6 neurobiological systems: LH/AgRP feeding circuits, LH-VTA/peri-LC foraging, orexin/hypocretin, parabrachial nucleus, VMHdm threat coding, insular interoception, and PWS/narcolepsy clinical knockouts.

---

## Architectural Question 1: Single broadcast vs multi-target competition

**Verdict: Both, layered. Broadcast at upstream sources, multi-target arbitration at downstream nodes.**

The convergent evidence:
- **Broadcast at upstream sources**: Wang/Lin 2015 shows VMHdm SF1+ cells send collaterals to multiple targets (dlPAG, AHN). Marino 2020 shows LH GABA fibres pass through VTA en route to peri-LC, dissociating from VTA dopamine. Cheung/Anderson 2025 shows VMHdm population coding broadcasts a continuous-valued imminence signal. Bjorness/Greene 2024 documents orexin neurons (~50,000 in mouse) projecting widely to VTA, LC, raphe, BLA, PFC, PAG, basal forebrain.
- **Arbitration at downstream nodes**: The same VMHdm broadcast produces freezing via dlPAG terminals and avoidance via AHN terminals. Burnett 2016 shows AgRP-driven feeding requires PVH oxytocin disinhibition. The peri-LC (Marino 2020) is dissociable from VTA reward.
- **Anti-correlated subpopulations within sources** (Cheung 2025): Even within VMHdm, threat-on and threat-off subpopulations are anti-correlated -- arbitration begins at the source level too.

**V3 implication:** SD-032a SalienceCoordinator should be modeled as a multi-node arbiter, not a single comparator. z_harm and drive_level are broadcast signals; the arbitration happens at multiple downstream targets in parallel, with each target weighting the broadcast streams differently.

---

## Architectural Question 2: Threshold vs continuous override

**Verdict: Continuous accumulation upstream, threshold-converted at commit gates.**

The convergent evidence:
- Cheung/Anderson 2025: VMHdm population dynamics encode predator imminence as a CONTINUOUS variable.
- Pyeon 2025: PBN CGRP neurons fire continuously with threat intensity (firing duration and amplitude scale with intensity).
- James/Aston-Jones 2017: Behavioural-economic analyses show orexin modulates demand elasticity (continuous parameter), not primary reinforcement.
- de Araujo Salgado 2023: Hunger-vs-predator behavioural switch is sigmoid-like at the BEHAVIOURAL level (commit threshold) but the upstream drive accumulation is graded.
- MECH-279 (PAG GABAergic gate): The convergent picture is that the freeze commit is a threshold operation downstream of continuous upstream signalling.

**V3 implication:** z_harm_a and drive_level should be continuous-valued; commit gates (freeze, flight, foraging-engagement) should implement threshold conversion. V3-EXQ-471's lock-in is likely a stuck commit gate, NOT a saturated upstream signal -- the fix should target the gate's reset condition, not the upstream signal itself.

---

## Architectural Question 3: Symmetry across drives

**Verdict: Asymmetric. Hunger-driven override is well-characterised; thirst, thermoregulation, sleep have distinct circuit substrates with different override authorities.**

The convergent evidence:
- Burnett 2016: AgRP-PVH-oxytocin specifically for hunger; not the substrate for thirst (which uses SFO/OVLT) or sleep (which uses VLPO/POA).
- Bassetti 2019 (narcolepsy): Orexin loss produces system-wide failure (motor, emotional, metabolic, autonomic), supporting a single broadcast modulator -- but the deficit pattern shows that orexin couples drives to motor/arousal asymmetrically.
- Strigo/Craig 2016: Homeostatic emotions share insular substrate but each has dedicated lamina-I afferent routing.
- Brown 2022 (PWS): Hyperphagia is the dominant phenotype; thirst, temperature, sleep regulation also disrupted but secondarily.

**V3 implication:** drive_level should not be a single scalar. At minimum two channels are needed: an acute-foraging drive (peri-LC analog, episodic) and a slow-trend energy drive (PVH/AgRP analog, scaling benefit_exposure). Other drives (thirst, sleep pressure) likely need their own channels in V4. For V3, scope can stay limited to hunger but the architectural commitment must be made: drive_level is a vector, not a scalar.

---

## Architectural Question 4: Override AMPLIFIES vs REPLACES z_harm

**Verdict: Neither, exactly. Override REWEIGHTS z_harm in the arbitration, while z_harm itself remains broadcast.**

The convergent evidence:
- Burnett 2016: Hunger-driven AgRP activation does not silence threat circuits; it disinhibits feeding via oxytocin. Threat assessment continues in parallel.
- de Araujo Salgado 2023: The hunger-vs-predator switch is a behavioural-mode commit, not a perceptual override. The mouse still perceives the predator -- it just acts on hunger.
- Bjorness/Greene 2024: Orexin gain-modulates the integration of reward-seeking and arousal -- the underlying signals are not silenced, they are reweighted.
- Marino 2020: peri-LC GABA pathway drives stimulation-induced eating without affecting body weight regulation -- foraging engagement vs energy regulation are dissociable channels.

**V3 implication:** SD-036's GABAergic decay of z_harm under override is likely NOT the right mechanism in isolation. The biology supports a downstream-arbiter reweighting, where z_harm continues to be computed and broadcast but its weight in commit-gate decisions is modulated by an override authority. SD-036 (GABA decay) may be one component, but a parallel orexin-analog gain modulator on the drive-side weight is also needed. The SD-036-only fix to V3-EXQ-471 may be insufficient under stronger threat lock.

---

## Architectural Question 5: Bridge to z_goal seeding (SD-012)

**Verdict: Override authority is the missing link between drive_level and z_goal.**

The convergent evidence:
- James/Aston-Jones 2017: Orexin is recruited specifically when behaviour requires high effort or external demand. This is the override condition for goal pursuit under threat.
- Bjorness/Greene 2024: Orexin couples motivated arousal -- it is the COUPLING signal between drive and arousal/action selection, not a primary drive signal.
- Bassetti 2019 (narcolepsy): Orexin loss produces cataplexy (loss of motor tone triggered by emotion). This is a clean prediction of broadcast-coupling failure -- emotional input no longer recruits motor coupling.
- Marino 2020: The peri-LC GABA pathway is necessary for FORAGING ENGAGEMENT (acute action), dissociable from VTA reward and from energy homeostasis.

**V3 implication:** SD-012's drive_level should not directly seed z_goal. Instead, an intermediate override authority (orexin-analog) takes drive_level + threat context as input and produces a coupling signal that gates z_goal seeding. Currently V3 has drive_level -> benefit_exposure -> z_goal directly, with no intermediate gating. The proposed orexin-analog regulator sits at this bridge: it determines WHEN drive_level is allowed to seed z_goal under threat conditions.

---

## Proposed Claim Cluster

The literature converges on a missing architectural layer in V3: a broadcast override regulator that reweights z_harm vs drive_level at downstream arbitration nodes, dissociable from SD-036's GABAergic decay. This is the orexin-analog layer.

### Draft SD-NNN: Broadcast override regulator (orexin-analog)

**Statement:** A small, broadly-projecting gain-modulator population integrates internal homeostatic state (drive_level, sleep debt, glucose) and threat context (z_harm magnitude, sustained-vs-acute) to produce a coupling signal that reweights z_harm in downstream commit gates and gates z_goal seeding by drive_level. The regulator is dissociable from SD-036's GABAergic stream decay -- they are partially redundant in normal function but mechanistically distinct under sustained threat.

**Substrate prediction:** A scalar (or low-dimensional vector) override_signal that:
1. Modulates the weight of z_harm in commit-gate threshold computations (does not silence z_harm).
2. Gates whether drive_level is allowed to seed z_goal (the SD-012 bridge).
3. Recruited specifically under conditions of high effort, sustained threat, or metabolic demand (threshold-like recruitment, not continuous baseline modulation).

**Failure mode prediction (PWS-analog):** Saturated override_signal produces compulsive drive pursuit despite negative outcomes (Brown 2022).
**Failure mode prediction (narcolepsy-analog):** Loss of override_signal produces decoupling -- z_harm and drive_level both compute normally but fail to integrate into coordinated behaviour (Bassetti 2019, cataplexy as motor-emotion decoupling).

### Draft MECH-NNN.1: LH-PAG override projection

**Statement:** A direct projection from LH (orexin and/or peri-LC GABA analog) to PAG modulates the GABAergic freeze gate (MECH-279) under metabolic demand. The projection does not silence the freeze gate but raises its threshold, producing the behavioural transition from freeze to active foraging under sustained hunger + threat.

**Evidence anchor:** Marino 2020 (LH GABA -> peri-LC for foraging engagement); de Araujo Salgado 2023 (sustained hunger overrides predator avoidance via LH-PAG-relevant circuitry); Wang/Lin 2015 (PAG as downstream arbiter of broadcast threat signals).

### Draft MECH-NNN.2: Orexin gain modulation of drive-coupled arousal

**Statement:** An orexin-analog modulator gates the coupling between drive_level and arousal-relevant downstream targets (PFC, BLA, LC, raphe), producing motivated arousal as a coupled state rather than as independent drive + arousal signals. Loss of this coupling produces cataplexy-analog failure: emotional/drive input fails to recruit motor activation.

**Evidence anchor:** Bjorness/Greene 2024 (orexin as coupling signal); James/Aston-Jones 2017 (orexin recruitment under high effort/demand); Bassetti 2019 (narcolepsy as coupling-loss clinical model).

### Draft MECH-NNN.3: LPB interoceptive routing into harm-arbitration

**Statement:** The lateral parabrachial nucleus (LPB) routes interoceptive distress signals (visceral malaise, taste, pain, dyspnoea) into the harm-arbitration network via PBN-CGRP -> CeA -> PAG. This is the upstream broadcast arm of the threat-side architecture, parallel to VMHdm's predator-side broadcast. Both feed downstream arbiters where the override regulator (above) reweights them.

**Evidence anchor:** Palmiter 2018 (PBN CGRP general alarm review); Pyeon 2025 (PBN CGRP active defense modulation); Strigo/Craig 2016 (insular common-currency framing).

---

## Bottom line for V3-EXQ-471 follow-up

The SD-036-only fix to V3-EXQ-471 (GABAergic decay of z_harm) addresses one mechanism but leaves the broader architectural gap unfilled. The literature is convergent that a dedicated override authority -- not a side-effect of stream decay -- is what biology uses to break harm-stream lock-in under metabolic demand. The proposed SD-NNN + MECH-NNN.1-3 cluster sketches what this layer looks like and what failure modes it predicts (PWS-saturation, narcolepsy-decoupling). Next step before V4: experimental probe to dissociate SD-036 GABA decay from the proposed orexin-analog override under sustained-threat conditions.
