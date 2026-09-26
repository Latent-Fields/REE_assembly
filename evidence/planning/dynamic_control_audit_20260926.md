# Dynamic-control audit, synthesis (steps 4, 6-9): failure shape, smallest falsifiable hypotheses, A1 ordering, recommendation

- **Written:** 2026-09-26T12:31Z onward. Session `bt0926-dcd` (Worker DC-D, `orchestrate-20260924-breakthrough-c2`), chip_ref `chip-20260926-dynctl-d-synthesis`.
- **Scope:** steps 4, 6, 7, 8 and 9 of the user's audit (`docs/thoughts/2026-09-26_dynamic_control_coordination_hole.md`). Steps 1-2 are DC-A (`dynamic_control_audit_inventory_20260926.md`, a783e4744d6), step 3 is DC-B (`dynamic_control_audit_imposed_regimes_20260926.md`, 26eeccf71d), step 5 is DC-C (`dynamic_control_audit_biology_20260926.md`, 2e1f6a60e43).
- **Read-only, document only.** No `ree_core` edit, nothing queued, no chip, no build, no probe run, no `claims.yaml` edit, no gate or preset changed. The two candidate claims in sec E are **DRAFT, NOT REGISTERED**; `/governance` registers or rejects them.
- **Builds on, does not re-register:** ARC-155, ARC-156, ARC-157, Q-111, Q-112, MECH-596, MECH-597 and the intake's owner map (`thought_intake_2026-09-26_dynamic_control_coordination_hole.md` sec 2). A new claim is drafted only where a regime decision has no owner.
- **The user's constraints, carried throughout:** no monolithic executive; dynamic control is a hypothesis to test, not to implement; endogenous signals only, never oracle knowledge of the condition (condition labels are used only for post-hoc scoring and oracle ceilings); speculative mechanisms labelled; recommend, change nothing silently; no architecture or gate change to make behaviour look better.
- **Evidence domain of this record: D0.** It synthesises records. Where a record measured something (D1/D2/D3), the record is cited. Two spot code reads were made against ree-v3 `origin/main` @ `436a988742` (sec 0, P7, and the H1 trigger). REE_assembly `origin/master` @ `a783e4744d6` at writing.

## Executive summary (for the user)

1. **The hole is not one missing executive, and it is not mainly working parts that fail to coordinate.** At default settings REE has exactly one live regime switch (commit vs sample in E3), and it is stuck "on" in trained agents. Most of the other regime machinery is switched off, has no input, or is wired to nothing.
2. **Where the machinery is switched on, individual controllers fail in two repeated ways.** Their thresholds sit on the wrong numerical scale (ARC-155), or their exit depends on evidence that the regime itself stops producing (ARC-156). A few signals are genuinely missing. The biggest is noticing that the world has changed (N5: surprise fired just as often without a change).
3. **Today the experimenter is the controller.** The episode reset (1156 of 1559 drivers) ends frozen and locked states, restarts every baseline, and in effect tells the agent the world changed. Harness schedules decide when to babble, learn, freeze memory and sleep.
4. **The common fix is local, not central.** Each control signal should be judged against the organism's own running statistics of that signal ("is this error unusual for me?"). The biology says the same (Yu & Dayan; ARC-155). Each channel does this for itself, and no new module is needed.
5. **Five small tests are specified (H0-H4).** Each compares the harness-imposed regime, an endogenous version, and a control that would pass for the wrong reason. Three are cheap Mac probes that need no `ree_core` change: H0 (does the episode reset do hidden control work?), H2 (the N5b shift detector, with an unexpected-uncertainty statistic added) and H3 (end babbling on the agent's own learning progress). H1 needs one precondition check first. H4 is blocked on a build decision.
6. **A1 ordering.** A dynamic controller is *not* a prerequisite for A1. A1's world never changes its rules, episodes reset every 200 steps or fewer, and A1 has no threat stack or mode coordinator. But A1 also *cannot* find a missing controller: it has no regime-contrast arm, so its failures would be blamed on the learning members. Recommendation: do not block A1 on a controller, and do not wait on A1 to find one. Run the cheap probes now. A1 is held for its own reasons anyway.
7. **Two things found here should be checked before A1 is queued (D0; not measured).** (a) The one live controller inside A1, the commit gate's absolute 0.40 bar, reads a quantity that the INT trainer changes in scale. (b) As written, the EMA reset-init knobs are ON in the INT arms but OFF in NATIVE. Either could make INT differ from NATIVE for reasons other than learning.
8. **Recommended user decision:** ship W6 with the retained set FROZEN (no unfreeze path) for A1. A1's dynamics never shift, so an unfreeze controller could only fire spuriously there (N5: 5/5 spurious opens).
9. **The real organism-level test comes after A1:** one continuous life with no reset and a hidden rule change (Q-108, class AR-3). Nothing in this record changes architecture, gates or presets. Every such choice is listed in sec D as a user or governance decision.

## 0. Premises re-measured before synthesising

| # | premise (source) | re-measured | verdict |
|---|---|---|---|
| P1 | "REE increasingly appears to have many of the mechanisms ... a dynamic-control hole: machinery exists" (user thought) | DC-A: 13 of 174 rows are live at defaults, 106 are default-OFF (16 of those stay inert even when ON), and 16 are named concepts with zero code. The mode register has no behavioural consumer (DC-A O3/O4; modetrace sec 1c, D1-negative). The retained set has no unfreeze path (O19). The babbler has no in-core caller (O20). | **half right.** For about half of the ten decisions the machinery itself, not only its selector, is absent or unwired (sec A) |
| P2 | "wholesale quarantine plus re-babbling appears capable of relearning" (user thought; N5) | N5 sec 4.3: one exploratory seed (721), 0.523 on the shifted map, oracle-timed. The harness chose all three of timing, scope (the whole retained set) and dose (2,400 steps). FIFO revision failed 0/5. | **holds, qualified**: revision works only in its wholesale form, on 1 seed, when imposed |
| P3 | "reversals restored only by an external task drive, which is an imposed regime" (capture note) | DC-B P1: `external_task_drive` is computed endogenously (`agent.py:9106-9133`). The experimenter supplies the channel's existence and gain. After training it was about dead (0.00053, V3-EXQ-1067). | **corrected by DC-B**: an imposed channel over an endogenous signal |
| P4 | A1 is held (brief) | Plan row A1: held until INT-CODEC and INT-ACT pass their member gates. W1-alt gate (c) is still FAIL-majority (3/5) under the provisional decided statistic. W4 gate (a) stands (n3post: ROBUST; the fix-ON arm is 5/5). W6 is blocked on W2b (blocked: N5) and W5b (blocked: W5 parked after 1105a FAILed). The user asked to revisit all four 09:33Z provisional decisions before A1 is queued. | **holds** |
| P5 | A1 costs ~177-205 CPU-h (brief) | `a1_cost_remeasure_20260926.md` sec 8.4: about 177 CPU-h mid ABSENT and about 205 GROUNDED, with screen and reserves. `valuation_mode` is fixed to ABSENT while 1105a stands failed (A1 v3c sec 3). | **holds; the operative figure is about 177 CPU-h** |
| P6 | the freeze-lock confirmer (`chip-20260926-pag-freeze-lock-confirmer`) has reported (the ARC-155 WWA sequences on it) | No confirmer record under `evidence/planning/` at `a783e4744d6`. The files present are `failure_autopsy_V3-EXQ-1107_2026-09-26.*` and `mech287_anchor_freeze_exit_design_20260925.md`, and neither is the confirmer. | **not reported**; H4 stays blocked |
| P7 | an existing, endogenous, scale-relative commit bar is available for testing (DC-A #14) | `ree_core/predictors/e3_selector.py:912-1024` (`_variance_tracking_commit_bar`), `ree_core/utils/config.py:1510-1545` @ `436a988742`: a detrended q-quantile of the run's own log gate-variance. Default OFF; q and the window are raise-if-unset sentinels. The config comment reads "**Occupancy is then ~q by construction**". | **holds, with a design consequence**: under this bar occupancy is not an informative DV (H1 below) |
| P8 | A1 compares INT with NATIVE on equal reset hygiene | Plan decision log 2026-09-26T09:33Z (4): all four EMA reset-init knobs are "ON in the coupled-loop preset, **the A1 INT arms** and new campaign probes". The A1 draft (all text through v3c) defines NATIVE as "all flags off" and never mentions reset-init (grep: 0 hits). | **not established.** As written, NATIVE has reset-init OFF and INT has it ON. See sec C.4 |

## A. Step 4: the shape of the failure

### A.1 The ten regime decisions, decision by decision

Sources: DC-A secs 3-5 (rows #, live edges L#, ON-only edges O#), DC-B secs 2-3 (imposed rows R#, decision rank), the intake owner map, and the campaign records. "Live" means live at defaults under the canonical StepHarness.

| decision | existing owner claim(s) | live endogenous signal? | live controlled variable? | imposed by harness? | gap type |
|---|---|---|---|---|---|
| D1 trust vs interrogate the model | ARC-016, ARC-029, MECH-590, ARC-037, MECH-585 | **yes**: E3 running variance rv (L1). Its composition is in doubt: on E3 ticks it measures E2's *predicted displacement* (DC-A P6; a D1 check is owed) | **yes, but absorbing**: committed (L2/L3). Trained rv is 1e-6 to 1.6e-5 against a 0.40 bar, so the committed fraction is 1.0000 (GFLAG-0346). No "interrogate" state exists | yes: 6 drivers pin rv = 0.001 (R11); the reset-init preset (R26) | **ARC-155 mis-scaling of the one live loop, plus ARC-156** (argmin ignores every variability lever, O10). The corrected bar is written but default-OFF (#14) |
| D2 exploit vs explore | MECH-433, MECH-482, MECH-527, ARC-065, SD-061, MECH-313 | partial: own-action concentration is computable but read by nothing (R4). SD-061 is OFF. The volatility estimate is telemetry (#4) | partial: argmin vs sampling follows D1. T is a driver constant (1.0). Every T lever is OFF, and is disconnected while committed (O10) | heavily: 519 random-warmup drivers (R3), babbling epochs (R4), the MECH-457 clock (R12), fixed T (R21) | **disconnected levers plus unrecruited signals.** Counter-case: V3-EXQ-755's endogenous mode gate added nothing because capacity bound first (R12) |
| D3 precision / routing | ARC-155, ARC-016, INV-022 | mostly no: own-scale estimates exist only in ARC-016, SD-099, MECH-449 and AIC (DC-A sec 6). The arousal input has 0.91% range (L7) | the E3 cadence is live but flat (L7). alpha_world is a constant. MECH-157 is OFF | yes: alpha_world pinned to 0.9 in 796 drivers (R20); absolute thresholds everywhere (R19) | **ARC-155** (ARC-155's four measured instances) **plus no dynamic range** |
| D4 PE attribution (noise / action / model / world) | MECH-590, ARC-037, MECH-585, MECH-510, MECH-511 | **measured absent**: N5 5/5 (raw and action-contrastive surprise both fire at base rate); V3-EXQ-910 0/30 aligned | none (named concepts only, DC-A sec 7) | yes: R1 hands over a truthful "world changed" flag every episode (the env re-draws its layout, A1 Q13); N5 used oracle timing (R5) | **a genuinely missing signal**, the cleanest one. It is also ARC-156-shaped: the on-policy stream may carry no map information (N5 sec 4.2, unmeasured) |
| D5 freeze vs reopen plasticity | MECH-398, MECH-207, MECH-474 (ARC-152, MECH-511 adjacent) | none: no native gain (N5 P1). The only endogenous lr modulator is sleep-only and OFF (O17) | none in waking: member lr is fixed; `requires_grad` flips via a harness callback (#115) | the **most-imposed** decision (DC-B rank 1): train then eval, warmups, staged harm training, the trainer K | **missing producer and missing controlled edge** |
| D6 quarantine obsolete experience and relearn | MECH-398, MECH-207, MECH-474, MECH-597; ARC-156 (N5 is its second measured instance) | none (depends on D4) | none: the FROZEN retained set has no unfreeze or eviction path (O19) | rare (R5, R6), but decisive for W2b | **missing detector plus missing edge.** The revision machinery works only wholesale and oracle-timed (1 seed) |
| D7 habit vs deliberative | MECH-312a-d, MECH-235, SD-081, MECH-163, MECH-596 | half: SD-081 reads rv plus a novelty EMA that nothing updates (O13) | the blend weight is OFF | pinned for life: SD-081 is default-OFF (R27) | **an existing arbitrator, default-off and half-dead.** The corpus holds no imposed-vs-native contrast, so severity is unknown |
| D8 enter / leave defence or freeze | MECH-279, MECH-280, SD-099/MECH-489, MECH-357/SD-058 | entry: no input at defaults (harm_dim 0). When ON, `\|\|z_harm_a\|\|` is mis-scaled (V3-EXQ-1107: 2.8-4.2 vs theta 0.8; CeA fires never or always). Exit: nothing changes during a freeze (V3-EXQ-1106: 0 on 3/3) | STAY substitution (live when ON) | yes: R1 is the only exit. 124 drivers enable freeze. The scaffold floor is in 81 (R8). The withhold-to-random fallback is in 324 (R21) | **ARC-155 at entry, ARC-156 at exit, and Q-111 composition** (freeze masks the veto: V3-EXQ-1090, action 0 on 3,000/3,000 ticks). The surviving exit (MECH-280) is unbuilt |
| D9 which representations influence E3 | SD-032a, MECH-259, MECH-266, MECH-157, MECH-039 (ARC-108, MECH-261) | yes when ON (delta_t for ARC-108) | **consumer-less**: four MECH-261 gates have no reader, and the agent never passes `operating_mode` to the proposer (O3/O4) | yes: stage schedules decide the goal term's reach (R7); alpha_world (R20) | **consumer-less machinery** |
| D10 broad operating regime | SD-032a/MECH-259, Q-111, Q-041; sleep: SD-017, SD-SLEEP-ENTRY-PRESSURE; stages: ARC-019, ARC-074 (whose trigger: **no owner**) | the dACC signal is shared-source coupled (O1). external_task_drive is endogenous but default-OFF and about dead after training. MEL is noise-level in this env | the coordinator register (no behavioural reach, O3). Sleep entry is an H clock (R13) | yes: R1 in 1156 drivers; curricula (R7, R10); the sleep clock; mode pins (R18) | **shared-source coupling (Q-111), no consumer, and a harness-owned life boundary.** Two sub-decisions are **unowned** (DC-B F4): what a reset may wipe, and who triggers stage transitions |

### A.2 Tally: which gap types recur

| gap type | decisions | fix class |
|---|---|---|
| **Machinery absent or unwired**: no controlled edge, no consumer, no caller | D5, D6, D9, D10 (mode reach) | build or wiring (`complicated (buildable)` where a design exists) |
| **ARC-155 mis-scaling**: an absolute bar on a learned quantity | D1, D3, D8 entry, D10 (dACC cap) | the corrected forms already exist, default-OFF (DC-A sec 6) |
| **ARC-156 starvation or disconnection**: the exit reads what the regime suppresses | D1 (absorbing commit), D2 (argmin ignores T), D6 (no exit from FROZEN), D8 exit, D10 (one switch, then locked) | a surviving input per regime (freeze: MECH-280, unbuilt) |
| **Genuinely missing endogenous signal** | D4 (world-change / PE attribution), D5 (plasticity-gain producer) | `complex (probe-gated)`: no validated candidate |
| **Composition / shared source** (Q-111) | D8 (freeze masks veto), D10 (dACC is both alarm and affinity), the threat stack (one scalar feeds 7 controllers, O9) | cannot be measured yet: Q-111's P1/P2 are unmet for every pair |
| **Harness supplies the decision** | all ten; R1 alone covers D1, D4, D5, D8 and D10 | the decisions DC-B found unowned (sec E) |

### A.3 Decision

Of the four candidate shapes the brief names:

- **"One missing mechanism": rejected.** No single absent component accounts for more than two of the ten decisions. The one partial exception is a *form*, not a mechanism: an estimate of the organism's own running statistics of a signal. That form would serve D1, D3, D4, D6 and D8-entry, but each channel has to compute it locally (ARC-155 per channel; the Yu & Dayan unexpected-uncertainty statistic for D4). DC-C finds the same thing from the biology side: regime signals are computed "from the organism's own statistics over its own recent experience".
- **"Coordination between existing working mechanisms": not the primary shape, and not yet measurable.** Coordination defects are real: the dACC shared source (modetrace), freeze masking the veto (1090), and one threat scalar feeding seven controllers. But every one of them sits on top of controllers that fail alone first (ARC-155 or ARC-156), which is exactly why Q-111's preconditions P1/P2 are unmet. Coordination is the *third* layer, not the first.
- **"Several distributed missing mechanisms": correct, and it needs a qualification.** The gaps are distributed and fall into the recurring types in A.2. Only about two of them (D4 and D5) are genuinely missing *signals*. The rest are present-but-mis-scaled, present-but-starved, or present-but-unwired.
- **DC-A's reading, "mostly inert and disconnected": correct as the base layer.** At defaults REE has one live regime variable, and that variable is absorbing.

**The shape, stated in layers (bottom first):**

1. **L0, disconnection.** Most regime machinery is default-OFF, inputless (threat), consumer-less (modes) or harness-gated (plasticity, memory, babbling, sleep).
2. **L1, per-controller defects of two recurring structural types.** ARC-155 (scale) and ARC-156 (starved exit). Their corrected forms are mostly written and default-OFF.
3. **L2, two genuinely missing endogenous signals.** World-change / PE attribution (D4, which D6 depends on) and a waking plasticity-gain producer (D5).
4. **L3, composition (Q-111).** Real, but measurable only after L1.
5. **Throughout: the harness does the coordinating.** The episode boundary (R1) and the schedules currently perform, from outside, most of the regime selection the thought asks about.

**What this means for the user's framing.** "Revision machinery adequate, regime selection missing" holds for D6 (revision works when imposed wholesale), for D10 reversals (they appear once an independent input exists) and for D8 (a timer exit exists). It does **not** hold for D5 (no gain path exists to select), D9 and the mode half of D10 (a perfect mode selection would change no behaviour, O3), or D2 (the variability levers are cut off while committed). For roughly half the decisions, selection is not the first thing missing.

## B. Steps 6-7: the smallest falsifiable dynamic-control hypotheses

### B.0 Design rules common to every hypothesis

- **Three arms minimum.**
  - **IMPOSED**: the current harness regime, which is the comparison arm.
  - **ENDOGENOUS**: the trigger is computed only from quantities the agent itself produces.
  - **WRONG-REASON control**: a timer matched in mean duration, or the same trigger computed on a time-permuted copy of the agent's own signal. An endogenous "win" must beat "any change at this rate" and "any change of this duration".
- **Oracle arms** (the condition known exactly) are ceilings, labelled as GOV-INTERVENE-1 oracle positive controls. Condition labels (shift / no shift, change times) are used **only** by the experimenter for post-hoc scoring and are never visible to the agent.
- **Reset hygiene.** All four EMA reset-init knobs ON (the campaign convention, GFLAG-0559). Absolute-scale readouts exclude the first 8 ticks after a reset (GFLAG-0560; `w3_k_excluding_reset_ticks_20260926.md`). Every R1 event is logged.
- **Stop rule.** If a named precondition channel is degenerate, stop and report; do not interpret anything downstream of it (COMMON rule 10).
- **No `ree_core` edits.** Every trigger below is computed harness-side from agent-readable state. A positive result is design input for a later `/implement-substrate` decision, not a build authorisation.

### H0. The episode reset is a hidden regime controller (DC-B contrast 1; decision D10, and the exits for D1/D8)

- **Hypothesis.** Several regimes that look recoverable in multi-episode drivers end only because the harness resets controller state at the episode boundary. If the controllers keep their state across a body-only reset, those regimes stay absorbed.
- **Trigger information available to REE.** None is added. This removes an imposition and measures what the organism does without it.
- **Controlled variable.** The scope of the boundary reset.
- **Arms.**
  - **A (imposed):** the standard `agent.reset()`.
  - **B (body-only):** the harness snapshots the controller-state objects that `reset()` clears and restores them after `reset()` (`agent.py:4101-4552`; DC-B R1 lists about 55). The environment layout and the body still reset. If the probe covers only a subset, it must name that subset.
  - **C (wrong-reason):** B, plus a full controller reset at random times matched in rate to A's boundaries but uncorrelated with them. This asks whether the regime exits come from *clearing* per se or from clearing *at a world change*.
- **Ecology.**
  - The modetrace configuration (dACC ON, external_task_drive OFF), where `n_switches == n_episodes` was measured.
  - The commit gate (live everywhere; rv already persists, so it serves as the within-probe control).
  - The freeze leg only if the harm stack's P1 holds (ARC-155 WWA). Otherwise it is omitted and the omission is reported.
- **Expected behavioural consequence if true.** Under B:
  - about one mode switch per *life* rather than per episode;
  - higher absorbing-regime occupancy;
  - endogenous exits (regime exits more than k ticks from any env boundary) near zero.
  - A by-product: controllers that *benefit* from persisting (the SD-075 surprise baseline, pACC drive bias) become visible. That is the evidence a persistence policy needs (DRAFT-DCD-1).
- **Failure mode if REE lacked this dependence.** Not applicable: the hypothesis is about dependence on the harness.
- **Falsifier.** Under B, endogenous exits and absorbing occupancy are within the pre-registered noise band of A. Then R1 is not doing exit work for these regimes, ARC-156's instance list narrows, and DRAFT-DCD-1 loses its motivation for them.
- **Owner.** The general question is **unowned**, so it is drafted as DRAFT-DCD-1 (sec E). Partial owners: SD-075 (one EMA), GFLAG-0559/0560 (EMA init), ARC-156, and Q-108 (which forbids a world-changed flag inside its recovery test).
- **Cost and dependencies.** A Mac probe, harness-only, on ree-v3 main with an untrained agent: 3 seeds x 3 arms x about 600-1,200 ticks, roughly 20-30 min under the probe lock. Nothing needs to be built.
- **Domain reachable.** D2 (the reset scope changes native consumers: the mode register, commit and freeze). D3 if reward is read.

### H1. Commitment on the organism's own error scale withdraws when the model becomes wrong (decisions D1/D2)

- **Hypothesis.** When the commit bar is expressed on rv's own recent distribution rather than as an absolute constant, the agent de-commits (and so samples, i.e. explores) specifically after its world model becomes wrong, and stays committed when the model is right.
- **Trigger information available to REE.** E3's own running variance rv of its world-prediction error (live, endogenous, ARC-016). It is denominated on its own recent distribution by the existing default-OFF ARC-029(D) bar: a detrended quantile, `e3_selector.py:912-1024` @ `436a988742` (P7).
- **Controlled variable.** `committed`, which selects between argmin and softmax sampling (`e3_selector.py:4666/4688`, DC-A L3).
- **Expected behavioural consequence.**
  - After a world change (the natural case is the layout re-draw at an episode boundary, since rv is never reset per episode; the strong case is the N5 action-map shift), rv rises above its own recent distribution, so the agent de-commits and samples.
  - Action diversity rises in the window after model failure and not elsewhere.
  - With the trainer ON, E2's one-step error recovers at least as fast as under the imposed arm.
- **Failure mode if absent.** Measured: under the absolute bar commitment is absorbing (1.0000, GFLAG-0346). The agent exploits a model it has no reason to trust, and every temperature lever is disconnected (O10).
- **Arms.**
  - **A (imposed / current):** the absolute 0.40 bar.
  - **B (endogenous):** the ARC-029(D) bar, with q and the window pre-registered.
  - **C (wrong-reason):** commitment drawn at random with probability matched to B's occupancy. Under B occupancy is about q by construction (P7), so occupancy is **not** a DV.
  - **D (content-shuffled):** B's bar computed on a time-permuted rv history.
  - **E (oracle ceiling):** de-commit forced for k ticks after each known change.
- **DVs** (scored post hoc against the known change times):
  - appropriateness = P(uncommitted within k ticks after a change) minus P(uncommitted elsewhere);
  - action entropy inside vs outside those windows;
  - E2 error recovery half-life (trainer-ON runs only).
- **Falsifier.**
  - **(F1)** B's appropriateness is not above both C and D by the pre-registered margin on at least 4/5 seeds. Own-scale commitment is then occupancy-stable but content-blind. ARC-155 at this site is necessary but not sufficient, and "trust vs interrogate" needs H2's kind of signal.
  - **(F2)** A is already about as appropriate as E. The absolute bar is not the problem in that regime.
- **Preconditions.**
  - **P-a:** the DC-A P6 check. Log error_var on E3 vs non-E3 ticks. If rv mostly reflects predicted displacement rather than realised error, **stop**: the signal cannot be condition-sensitive for the reason under test.
  - **P-b:** a trained world head (the W3 protocol), so that rv lives in the drifting small-scale regime where A absorbs.
- **Not a re-run of the ARC-029 lineage.** V3-EXQ-1066, 1070 and 1070a test two-mode *occupancy* with a harm-variance bar and are stuck on env feasibility (`failure_autopsy_V3-EXQ-1070a_2026-09-22.md`). H1's DV is *appropriateness of de-commitment at a model failure*.
- **Owner.** ARC-016, ARC-029, ARC-155. No new claim. H1 would give ARC-155 a second first-test site whose information-content precondition (P1) is likelier to hold than z_harm_a's (1107 recorded z_harm_a constant over 90 eval ticks). Governance decides whether to adopt it.
- **Cost and dependencies.** A Mac probe on the branch W3 protocol (the flag exists; harness-side): about 10 min for P-a, then 5 seeds x 5 arms, about 1 h. Nothing needs to be built.
- **Domain reachable.** D2 (the bar changes the native choice rule), plus a partial D3 (action diversity). Reward is **not** a DV: E3's valuation stays at chance until W5 (N3-pre), so exploiting is not expected to pay.

### H2. An unexpected-uncertainty statistic, fed by regime-surviving probes, detects the shift that surprise missed (N5b; D4 then D6; Yu & Dayan as a candidate, not a given)

- **Hypothesis.** A shift can be told apart from no shift by a statistic that asks whether the organism's recent errors are *inconsistent with its own error distribution* (Yu & Dayan's unexpected uncertainty). Error *magnitude* (N5's detector) cannot do this. The statistic works only if it is fed evidence that survives the exploit regime: self-generated probe actions (ARC-156's surviving input).
- **Trigger information available to REE.**
  - (i) An **expected-uncertainty** model: the running distribution of the member's own action-contrastive one-step error (N5's `ac`), kept separately for on-policy and babble sources.
  - (ii) An **unexpected-uncertainty** statistic over that error sequence: change-point, CUSUM or likelihood-ratio, pre-registered.
  - (iii) The **evidence source**: short periodic structured-babbling probe bouts that cover all action classes. N5 sec 4.2 suggests (unmeasured) that the concentrated on-policy stream carries little map information.
- **Controlled variables.**
  - Stage 1: none (a detector-only test on a clamped pair).
  - Stage 2: the retained-set quarantine scope (the whole pre-onset set, the only form that relearned) plus a re-babble epoch.
- **Expected behavioural consequence.**
  - The detector fires within a pre-registered latency after the shift and rarely without one.
  - Stage 2, endogenously timed, relearns the shifted map to the W3 bar, as oracle-timed `shift_oraclefull` did on seed 721.
- **Failure mode if absent.** Measured (N5): the gate fires at base rate (spurious opens 5/5, 1,262-2,166 on-policy records flushed per seed) and the old map is kept.
- **Arms.**
  - **Stage 1, 2 x 2 factorial** under shift and under no shift, no unfreeze: {probe bouts ON / OFF} x {change-point statistic / N5 magnitude statistic}.
  - **Stage 1 wrong-reason control:** probe bouts ON, detector replaced by random triggers at the matched rate.
  - **Stage 2 comparison:** oracle-timed wholesale quarantine (the harness-imposed regime, N5X) vs endogenously timed.
- **DVs.**
  - Separation: hit rate minus false-alarm rate (or AUROC) within the latency window.
  - False opens per 1,000 steps without a shift.
  - Stage 2: the post-shift W3 bar on TE_shift; with no shift, retention on TE_orig.
- **Falsifier.**
  - **(F1)** With probes ON, the change-point statistic separates no better than the magnitude statistic. Unexpected uncertainty adds nothing here.
  - **(F2)** Separation appears with probes for *both* statistics equally. The gain belongs to the probe (the ARC-156 evidence source), not to the Yu & Dayan statistic, and the claim narrows to ARC-156.
  - **(F3)** Separation needs a probe budget above a pre-registered ceiling (for example 10% of steps). That amounts to continuous babbling, not detection.
  - **(F4)** Stage 2 fails when endogenously timed but succeeds when oracle-timed on the same seeds. Detection latency or false quarantine is then the defect.
- **Preconditions.**
  - **P-a:** the pre-shift W3 bar is met on each registered seed. N5 met it on only 2/5. Pre-screen, or run with reset-init ON, which raised W3 pass 9/15 to 13/15.
  - **P-b:** log per-step displacement on on-policy steps, to test N5's unmeasured wall-pressing account. If on-policy steps already carry map information, the probe arm is unnecessary and the design is re-planned before any registered seed.
- **Owner.** Existing, so no new claim:
  - ARC-156 (its applied WWA already names N5b as its second leg);
  - MECH-590, ARC-037 and MECH-585 (PE attribution);
  - MECH-398 and MECH-207 (the downstream gate, W2b).
  - Checked: MECH-104 is harm-specific and does not own a world-model shift detector.
- **Cost and dependencies.** A Mac probe at N5 scale: about 11-15 min per seed x 5 seeds, 1-1.5 h. Harness-only on the branch. **This is already the campaign's planned next step for W2b** (plan row W2b, "Next: probe N5b"). The audit adds two things: the change-point statistic as a pre-registered candidate, and the 2 x 2 that separates "probe" from "statistic".
- **Domain reachable.** D1 (detector separation). D2 at stage 2 (quarantine changes the head).

### H3. Development ends on the organism's own learning progress, not a fixed epoch (D2/D5; the stage-transition decision DC-B found unowned)

- **Hypothesis.** A babbling epoch ended by the organism's own learning progress develops the E2 world head at least as reliably as a fixed epoch, and the information comes from the timing, not from the duration.
- **Trigger information available to REE.** The E2WorldMember's own training loss on its babble stream (no held-out labels). Learning progress LP is the slope of a slow EMA of that loss. Babbling ends when LP falls below a pre-registered fraction of its early value for a pre-registered dwell.
- **Controlled variable.** The babbling source switch (branch `waking_trainer.py:771`, `set_e2_world_source("babble" -> "on_policy")`), and so the epoch length.
- **Expected behavioural consequence.** Durations vary per seed and end later on seeds that learn more slowly. At matched mean duration, gate (a) passes on at least as many seeds as under a timer.
- **Failure mode if absent.** An experimenter constant (2,400 steps, "DRAFT: plan's number, not grounded", A1 O9) sets development length for every seed alike.
- **Arms.**
  - **A (imposed):** a fixed 2,400 steps.
  - **B (endogenous):** end at the LP plateau.
  - **C (wrong-reason):** each seed's duration drawn from B's distribution, uncorrelated with that seed's own learning (ARC-156 F2 logic: information vs duration).
  - **D (oracle ceiling):** end at the step where held-out disc4 first crosses the bar.
- **DVs.** W3 gate (a) pass count (disc4 >= 0.47, the current disc4-only definition); disc4; retention (b) after the on-policy phase; the correlation of B's duration with each seed's post-hoc time-to-bar.
- **Falsifier.** B is no better than C at matched mean duration, **and** B's durations are uncorrelated with post-hoc time-to-bar. The organism's own LP then carries no readiness information here, and stage length is a timer question. If instead A already passes on every seed, the transition does not matter in this regime, which is a null for the question rather than a falsification.
- **Owner.** ARC-074 (the babbling epoch), ARC-157 ("reopen them when they stop predicting" is procedural), MECH-597. **Who triggers the transition is unowned**, so it is drafted as DRAFT-DCD-2. It is in tension with ARC-019's "explicit curriculum gates".
- **Cost and dependencies.** A Mac probe on the W3 protocol, about 3-5 min per seed per arm: 5 seeds x 4 arms, 1-1.5 h. Harness-only. Nothing needs to be built. **By-product:** whatever the verdict, it gives A1's ungrounded 2,400-step constant (O9) an evidence basis.
- **Domain reachable.** D1.

### H4. Freeze needs an exit input that survives the freeze (ARC-156 freeze leg; D8). Already specified; NOT runnable now

- The full design is ARC-156's applied WWA:
  - **A:** exit on suppressed evidence;
  - **B:** A plus a surviving input;
  - **C:** a duration-matched timer;
  - **D:** no release.
- ARC-155's WWA (PAG operating point) is its partner. This record adds only ordering and dependencies. Three blockers, all unmet:
  1. the freeze-lock confirmer has not reported (P6);
  2. ARC-155's P1 is unmeasured: does z_harm_a still carry hazard information after training? V3-EXQ-1107 found it constant over 90 eval ticks;
  3. the natural surviving input, MECH-280's LH-PAG override, is unbuilt. That is a build decision for MECH-280 and governance (GFLAG-0506).
- A1 has no threat stack, so H4 has no bearing on A1. **Cost:** cloud (trained harm stack). **Owner:** ARC-156, MECH-279, MECH-280.

### B.5 Considered and deliberately not proposed now

| candidate | why not now | where it lives |
|---|---|---|
| Mode-coordinator reversal from an independent endogenous input (Q-111's second case) | The mode register has no behavioural consumer (O3/O4, D1-negative). By the stop rule, testing whether a reversal is *appropriate* measures a quantity nothing reads | `mech019-operating-mode-enabled-consumer` first; then a Q-111 pair test |
| Metaplasticity: a gain driven by the member's own recent plasticity history (DC-C sec 12, the net-new biology gap) | N5's calibration: plasticity gain alone (g = 1, no unfreeze) did **not** revise (0.247). FIFO was too slow and wholesale quarantine worked. **The binding variable is the composition of the replay, not the learning rate.** Revisit after H2 stage 2. It is a mechanism for an *owned* decision (D5), so no claim is drafted | MECH-398, MECH-207, MECH-474 (ARC-152, MECH-511 adjacent) |
| Native sleep entry (DC-B contrast 3) | MEL is noise-level in CausalGridWorldV2. A1 has no sleep. An owner exists | SD-SLEEP-ENTRY-PRESSURE |
| Un-forced rv and no scaffold floor (DC-B contrast 4) | The rv half is folded into H1. The scaffold-floor half belongs to its lineage | MECH-357; the 603u cluster |
| Stuckness-triggered annealing | Named concept only; it needs a build | MECH-527 via MECH-482 |
| Habit vs deliberative arbitration | SD-081's habit-uncertainty fallback is never updated (O13): a wiring defect to fix before any test | SD-081, MECH-596 (plan row W1-both) |
| An explicit cross-controller authority principle | Q-111's P1/P2 are unmet for every pair. H1 and H4 are the per-controller corrections it waits on | Q-111 |
| Ephaptic / field coordination (**SPECULATIVE**, DC-C sec 11) | The better-evidenced explanations (sec A, layers L1-L2) are not exhausted | MECH-534, MECH-270 |

**The umbrella hypothesis stays falsifiable.** "REE lacks endogenous regime selection" is **weakened** if H0 finds endogenous exits without R1 and the endogenous arms of H1-H3 match their oracle or imposed arms. It is **confirmed decision by decision** where the endogenous arm fails and the imposed arm succeeds. Its organism-level test is the single-life recovery test in sec D, step 8.

## C. Step 8: A1 ordering

### C.1 What A1 is (re-measured)

- **Regime and length.** CausalGridWorldV2 8x8, `max_episode_steps` 200, and 3,000 closed-loop steps. So there are at least 15 episode resets per arm. The env re-draws its layout every episode (A1 Q13), so **A1 keeps R1**: both its exits and its truthful world-changed flag.
- **Phases.** A fixed 2,400-step developmental epoch, which is ungrounded (O9). The trainer is ON, except in FROZEN, where the harness switches it OFF for phase 3. That is a legitimate measurement contrast of the M class.
- **Arms.** 16 per seed in ABSENT mode, 18 in GROUNDED. `valuation_mode` is ABSENT while 1105a stands failed.
- **Presets.** NATIVE is "all flags off". The W6 preset contains the trainer members (HarmEval, E1, E2Self, W3, W6a), W4 and one proposer variant (A1 v3c sec 1). **No coordinator, threat stack, freeze, veto or sleep in any arm.**
- **Cost.** About 177 CPU-h mid (P5). Held for its own reasons (P4).
- **Critical path.** W6 is blocked on W2b. W2b *is* a dynamic-control capability (ACh-gated unfreeze, D5/D6), and N5 found it "not buildable as specified". So the ordering question is concrete: **does A1 wait for W2b?**

### C.2 The case that a minimal dynamic-control capability is a prerequisite

- A1 keeps R1. Absorbing regimes are cut short at 200 steps or fewer, and the world-changed signal comes from outside, so A1 cannot fail for lack of either.
- An A1 PASS would therefore certify the learning loop *under experimenter-supplied regimes*: harness exits, a fixed epoch, a fixed trainer schedule. Read without that caveat, "the loop closes" would overstate what was shown.
- The one live controller inside A1 is the commit gate. It uses the absolute 0.40 bar (ARC-155) and may behave differently in INT and NATIVE (sec C.4). An uncorrected controller inside the comparison can bias it.
- The plan already made one dynamic controller (W2b) a member of the tested preset. If it is part of what "the organism" means, A1 without it tests a different organism.

### C.3 The case for running A1 first

- A1 tests a narrower and prior question: does waking learning, with grounding, move real outcomes? Every D5/D6 controller operates on that learning loop. A shift detector is useless if nothing learns. So the learning loop is upstream of regime control for the decisions that matter most.
- **A1's dynamics are stationary.** The action-to-displacement map never changes, and only the layout does. An unfreeze controller therefore has nothing to do in A1 except fire spuriously: N5's gate opened spuriously on 5/5 seeds and flushed 1,262-2,166 on-policy records per seed. N5 also showed the FROZEN retained set is stable without a shift (retention 1.17-1.54, 5/5). So W2b is scientifically unnecessary for A1, not merely unavailable.
- The user's own constraint is to test dynamic control, not implement it. Building a controller to unblock A1 would implement one first.
- The V3-EXQ-755 counter-case: on that task, capacity bound before regime selection did.

### C.4 Can A1's readouts even detect a missing controller?

| decision | exercised in A1? | A1 readout that could show it | attributable to regime selection? |
|---|---|---|---|
| D1 trust / interrogate | yes: the commit gate is live in every arm | ARC-016 rv and commit rate (**reported, no criterion**, A1 sec 6.1) | partly: visible, but not contrasted |
| D2 explore / exploit | yes (argmin vs sampling; imposed babbling) | action entropy, class coverage, D-INIT modal share | no: no regime arm |
| D3 precision | pinned (alpha_world, constants) | none | no |
| D4 PE attribution | **no**: R1 supplies it; no perturbation | none | no |
| D5 plasticity | trainer ON vs FROZEN (imposed contrast, P4) | P4 FIRST-to-LAST change | tests *whether* learning helps, not *who decides when* |
| D6 quarantine | **no**: stationary dynamics | none | no |
| D7 habit / deliberative | SD-081 is off. W4 changes the scoring read, not arbitration | none | no |
| D8 defence | **no**: no threat stack | none | no |
| D9 representations into E3 | **no**: no coordinator, no ARC-108 | none | no |
| D10 broad regime | R1 and fixed phases | none | no |

**A1 can at most observe D1 and D2, and it can attribute neither.** It has no arm that supplies the correct regime, so a shortfall caused by a missing controller would look exactly like a shortfall caused by a weak member. A1's FAIL path localises failures through per-workstream readouts. It would blame members, not regimes. "Run A1 first and use its failures to identify the missing controller" therefore does not work *with A1 as designed*. Making it work would need regime-contrast arms: about 12-13 CPU-h per added INT arm across 24 seeds (0.47-0.54 h per arm per seed, `a1_cost_remeasure` sec 8.4), plus a pre-registration change. That is not recommended.

**Two observations, found here, that bear on A1's INT-vs-NATIVE comparison (D0; not measured; for the orchestrator and user):**

1. **The commit gate may be driven apart by the preset (an ARC-155 confound inside A1).**
   - rv is an EMA of the squared error `||z_world - E2 prediction||^2` (DC-A L1).
   - W6a raises z norms about 10-14x (plan row W6a). At a fixed relative error that scales rv by about 100-200x.
   - W3 trains the very E2 head rv reads, so INT's rv could move in the opposite direction.
   - Against an absolute 0.40 bar, INT and NATIVE can therefore sit in different commit regimes (argmin vs sampling) for reasons unrelated to what either arm has learned.
   - A1 reports rv and commit rate, so this would at least be *visible* after the run. It would not be *controlled*.
   - A cheap pre-A1 read (H1-lite: the rv trace and committed fraction for NATIVE vs the INT preset, 2 seeds, about 1,200 ticks, about 20 min on the Mac) settles it.
2. **Reset-init asymmetry (P8).**
   - As written, the four EMA reset-init knobs are ON in the INT arms and OFF in NATIVE.
   - Reset-init alone lifts z_world participation ratio about 3x at alpha 0.3 (`zworld_ema_reset_init_build_20260926.md`). It also changed W3 gate outcomes (9/15 to 13/15) and feeds rv through the zero-init transient (DC-A P7).
   - P3 (SHUF) and P4 (FROZEN) share the INT preset, so they are protected. **P1b, P1t and P2 (INT vs NATIVE) are exposed.**
   - Either option changes A1's preset or its NATIVE definition, so it is a user/orchestrator decision: NATIVE also gets reset-init ON, or the asymmetry is reported as a known confound.

### C.5 Recommendation and its main risk

- **Recommendation: neither strict order.**
  - (i) A dynamic-control capability is **not** a prerequisite for A1. Ship W6 with the retained set FROZEN (the N5 decision the user owns), because A1's dynamics never shift.
  - (ii) Do not wait on A1 to find the missing controller, because A1 cannot see one. Run H0, H2 and H3 now, on the Mac and harness-only. A1 is held for independent reasons, so they cost it nothing on the critical path.
  - (iii) Before A1 is queued, resolve the two C.4 observations (H1-lite plus the reset-init decision).
  - (iv) Attach a scope sentence to A1's verdict: "tests the learning loop under experimenter-supplied regime control (episode resets, fixed developmental epoch, fixed trainer schedule)". Adding it is text in the pre-registration, and so a user/orchestrator decision.
  - (v) After A1, the organism-level test of the dynamic-control hypothesis is an R1-free single-life adaptive-recovery run (Q-108 AR-3, the action-map reshuffle that is N5's shift). It needs a working learning loop (A1) and the H0/H2 infrastructure.
- **Main risk.** A1 PASSes and the PASS is read as "the organism closes its loop" when the harness chose its regimes. Or an INT-minus-NATIVE delta carried by the commit regime or the reset-init asymmetry is attributed to learning. Mitigations: (iii) and (iv).
- **Secondary risk.** The parallel probes compete with campaign probes for the shared Mac probe lock. Scheduling is the orchestrator's call.
- **The opposite choice's risk** (hold A1 until a controller exists). It blocks a roughly 177 CPU-h D3 test of the learning loop behind a detector no candidate has yet passed (N5 0/5). It also builds a controller before testing whether one is needed, which the user's constraint rules out.

## D. Step 9: what to do next, in order, and what stays a user decision

**Recommended sequence** (nothing below is queued, chipped or built by this record):

1. **Pre-A1, now, about 20 min on the Mac, report-only.** H1-lite: rv trace and committed fraction for NATIVE vs the INT preset (C.4 observation 1). In parallel, decide the reset-init asymmetry (C.4 observation 2).
2. **User decision already pending from N5:** ship W6 with the retained set FROZEN (recommended, C.3) or wait for W2b.
3. **H2 (N5b)** with the change-point statistic added as a pre-registered candidate and the probe-vs-statistic 2 x 2. It is the campaign's own next W2b step, and its result decides whether W2b ever becomes buildable. Its preconditions come first (displacement logging; seeds that meet the W3 bar).
4. **H0 and H3**, cheap and harness-only, in either order. H3 also grounds A1's 2,400-step constant.
5. **H1** in full, after its P-a precondition (what rv actually measures).
6. **H4** waits on the confirmer, ARC-155 P1, and the MECH-280 build decision.
7. **A1** proceeds when its own holds clear, with the C.5 (iii)/(iv) items settled.
8. **After A1:** design the R1-free single-life recovery test (Q-108 AR-3). Only there can "REE lacks endogenous regime selection" be confirmed or refuted at D3.
9. **Governance routing** (not applied here; route through `governance_flag.py` or `/governance`):
   - DRAFT-DCD-1 and DRAFT-DCD-2 (sec E);
   - a second ARC-155 test site (the commit gate, H1);
   - add the absorbing-commit and FROZEN-retained-set instances to ARC-156's instance list;
   - the ARC-019 tension;
   - DC-C's flag that the exploit/explore cluster is anchored on NE (MECH-433), not DA;
   - DC-C's salience-hub caution for SD-032a.

**Decisions that stay with the user (or governance). None is taken here:**

| # | decision | options | this record's recommendation |
|---|---|---|---|
| U1 | W6 retained-set policy for A1 (from N5) | ship FROZEN / wait for W2b | FROZEN (C.3) |
| U2 | NATIVE reset-init asymmetry (P8) | NATIVE also ON (NATIVE is then no longer "all flags off") / report it as a known confound / leave as is | ON in NATIVE, or at minimum report it. **This changes A1's preset definition.** |
| U3 | the commit gate inside A1, if H1-lite shows INT and NATIVE in different commit regimes | report only / ARC-029(D) bar in every arm / other | decide after H1-lite. **Any change alters A1's preset.** |
| U4 | a scope sentence in A1's verdict language | add / do not add | add (text only; no criterion changes) |
| U5 | whether to spend Mac probe-lock time on H0, H2 and H3 now | yes / after the campaign | yes: H2 is already the campaign's next W2b step |
| U6 | registering DRAFT-DCD-1 and DRAFT-DCD-2, or amending ARC-019 instead of registering DCD-2 | register / amend / reject | governance's call |
| U7 | MECH-280 build (the surviving freeze exit) | build default-OFF / defer | defer until ARC-155 P1 is measured |
| U8 | whether any endogenous regime controller ever becomes default-ON | always a separate decision | not before its hypothesis PASSes against the wrong-reason control |
| U9 | an R1-free single-life recovery test (Q-108) as the post-A1 organism milestone | design it / not yet | design after A1 |

**Explicitly not done:** no architecture change, no acceptance-gate change, no preset change, no default change, no build, no queue entry, no chip, no claims.yaml edit.

## E. DRAFT candidate claims (unowned decisions only). DRAFT -- NOT REGISTERED

Ownership was re-checked against `claims.yaml` @ `a783e4744d6`. A title regex for episode/life/reset boundary, cross-episode persistence and stage transition found only SD-075, which is scoped to one EMA (the SD-069 surprise baseline). ARC-019 asserts "explicit curriculum gates" without saying who reads them. ARC-157 classifies priors and orders rescue interventions, but does not own the transition trigger. The two DC-B F4 decisions remain unowned, so both are drafted below. DC-B's third item (R21, the withhold-to-random fallback) is harness hygiene and not claim-shaped. Metaplasticity is a mechanism for an owned decision (D5), so no claim is drafted for it.

**The `id` values are placeholders.** `/governance` assigns real ids at registration by checking the current max at write time (Q-112 at `a783e4744d6`).

```yaml
# DRAFT -- NOT REGISTERED. Placeholder id; /governance assigns the real id.
- id: DRAFT-DCD-1
  title: 'Which controller states may a life (episode/body) boundary legitimately re-initialise, and which must persist across it and be exited endogenously? REE''s harness currently calls agent.reset() at every episode end (1156 of 1559 drivers), clearing about 55 controller states -- mode register, commitment/beta state, freeze state, dACC/AIC/pACC and surprise baselines, invalidation and staleness accumulators, latent EMA state -- at a time the organism did not choose, while weights and the residue field persist. Does REE''s regime control survive a body-only boundary that resets body and environment but not controller state, or do its absorbing regimes currently terminate only because the harness clears them?'
  claim_type: open_question
  subject: control_plane.life_boundary_state_policy
  polarity: asserts
  status: candidate
  epistemic_category: answer_state
  implementation_phase: v3
  version_relevance: v3_v4
  source_thought: docs/thoughts/2026-09-26_dynamic_control_coordination_hole.md
  location: docs/architecture/endogenous_operating_point_regulation.md
  depends_on:
  - ARC-156
  - SD-075
  - Q-108
  - ARC-155
  related_claims:
  - Q-111
  - ARC-016
  - SD-032a
  - MECH-279
  - MECH-284
  source:
  - evidence/planning/dynamic_control_audit_imposed_regimes_20260926.md
  - evidence/planning/dynamic_control_audit_inventory_20260926.md
  - evidence/planning/dynamic_control_audit_20260926.md
  notes: 'Drafted by the dynamic-control audit synthesis (bt0926-dcd) from DC-B finding F4(i); NOT registered. WHY UNOWNED: SD-075 owns the continuity of one EMA (the SD-069 phasic surprise baseline); GFLAG-0559/0560 own EMA initial values only; ARC-156 requires a regime-surviving exit input but does not say what a boundary may clear; Q-108 forbids a world-changed flag inside its recovery test but does not govern ordinary drivers. MEASURED MOTIVATION: V3-EXQ-1107 freeze locks from tick 1 and the reset is its only exit; the mode coordinator switches once per episode (n_switches == n_episodes, mode_switch_cea_mechanism_trace_20260925.md sec 1a); the near-reset EMA transients carried W3''s k criterion (w3_k_excluding_reset_ticks_20260926.md, 6/6) and 84% of the gate-(c) failure (gate_c_with_ema_reset_init_20260926.md); in CausalGridWorldV2 the reset coincides with a layout re-draw, so it is also a truthful world-changed oracle (A1 draft Q13). CANDIDATE COMPANION (governance_rule shape, for /governance to decide, not drafted as a claim): runs that clear controller state at a boundary declare it as an experimenter-supplied regime intervention, and organism-level claims about regime termination, world-change detection or stage transition may not rest on evidence in which the boundary supplied the exit or the change signal. NOT A MONOLITHIC EXECUTIVE: the question is per-state persistence, answered state by state.'
  what_would_answer: 'NON-DEGENERACY PRECONDITIONS: (P1) the tested regimes are entered at least once per life under the standard reset (occupancy > 0), otherwise persistence has nothing to carry; (P2) the snapshot/restore set is read from reset() itself (agent.py:4101-4552) and a subset is named if partial; (P3) all EMA reset-init knobs ON so the zero-init transient is not the measured effect; (P4) exits are scored as endogenous only when more than k ticks from any env boundary (k pre-registered). DESIGN (audit hypothesis H0): arm A standard agent.reset(); arm B body-only reset (controller states snapshotted and restored, env and body reset); arm C B plus full controller resets at random times rate-matched to A''s boundaries but uncorrelated with them. Ecology: the modetrace config (dACC ON) and the E3 commit gate, plus the freeze leg only if ARC-155''s information-content precondition holds for z_harm_a. DVs: absorbing-regime occupancy; endogenous exit count; per-controller behaviour/outcome under persistence. CONFIRMING (the boundary does hidden regime control): under B, absorbing occupancy rises and endogenous exits fall to near zero relative to A on >= 4/5 seeds, and C restores A''s exits only when its resets land near world changes. FALSIFYING: B''s endogenous exits and absorbing occupancy are within the pre-registered noise band of A -- the regimes exit on their own, and the reset is bookkeeping for these controllers. A secondary, per-controller readout (does a controller''s behaviour improve when persisted?) informs which states SHOULD persist and is not a verdict. A failure under unmet preconditions is not evidence against the question.'

# DRAFT -- NOT REGISTERED. Placeholder id; /governance assigns the real id.
- id: DRAFT-DCD-2
  title: 'Must REE''s developmental stage transitions -- the end of structured babbling, a curriculum stage advance, the closure (freezing) of the retained developmental set -- be triggered by the organism''s own evidence (learning progress on its own training stream, its own action concentration, its own error statistics), or is an experimenter-set schedule an admissible part of the developmental architecture? Every current transition is set exogenously (the fixed 2,400-step babbling epoch, episode-floored curriculum phases, harness-called source switches and freeze).'
  claim_type: open_question
  subject: development.stage_transition_trigger_ownership
  polarity: asserts
  status: candidate
  epistemic_category: answer_state
  implementation_phase: v3
  version_relevance: v3_v4
  source_thought: docs/thoughts/2026-09-26_dynamic_control_coordination_hole.md
  location: docs/architecture/minimal_developmental_prior.md
  depends_on:
  - ARC-019
  - ARC-074
  - ARC-157
  - MECH-597
  related_claims:
  - Q-112
  - ARC-075
  - MECH-398
  - MECH-474
  source:
  - evidence/planning/dynamic_control_audit_imposed_regimes_20260926.md
  - evidence/planning/dynamic_control_audit_20260926.md
  notes: 'Drafted by the dynamic-control audit synthesis (bt0926-dcd) from DC-B finding F4(ii); NOT registered. WHY UNOWNED: ARC-019 (provisional) asserts staged training with explicit curriculum gates and does not say whose; ARC-074 requires a Phase-0 babbling epoch; ARC-075 requires plasticity asymmetry across phases; ARC-157 and Q-112 classify WHICH priors are general or necessary and order rescue interventions; none asks whether the TRANSITION must be read by the organism. IN TENSION WITH ARC-019: if gates must be explicit and exogenous, the dynamic-control hypothesis is pre-empted for development. ALTERNATIVE DISPOSITION for /governance: amend ARC-019 (notes or a narrowed restatement) instead of registering this question. EVIDENCE CONTEXT: the A1 pre-registration flags its own 2,400-step epoch as "DRAFT: plan''s number, not grounded" (open item O9); the infant curriculum''s metric gates read the agent''s own state but are harness-applied, one-way, behind episode floors (DC-B R10); an organism-read stage transition occurs in 0 drivers (DC-B F2).'
  what_would_answer: 'NON-DEGENERACY PRECONDITIONS: (P1) the fixed-schedule arm does not already pass on every seed, otherwise timing cannot matter in the regime tested; (P2) the endogenous trigger reads only the organism''s own training stream (no held-out labels); (P3) the held-out readout (W3 gate (a), disc4 >= 0.47) is scored post hoc only; (P4) reset-init ON (GFLAG-0559). DESIGN (audit hypothesis H3, first instance: the end of W2a babbling on the W3 protocol): arm A fixed 2,400 steps; arm B end when the E2WorldMember''s own loss learning-progress falls below a pre-registered fraction of its early value for a pre-registered dwell; arm C each seed''s duration drawn from B''s distribution, uncorrelated with that seed (information vs duration); arm D oracle end at the first held-out bar crossing (ceiling). CONFIRMING (organism-read transitions carry information): B passes gate (a) on more seeds than C at matched mean duration AND B''s per-seed duration correlates with post-hoc time-to-bar. FALSIFYING: B is no better than C and its durations are uncorrelated with time-to-bar -- the organism''s own progress signal carries no readiness information here, and a schedule is admissible for this transition. Further transitions (curriculum stage advance, retained-set closure) are separate legs with the same three-arm logic. A failure under unmet preconditions is not evidence against the question.'
```

## F. Limits and uncertainty

- **This record is D0.** The shape decision (sec A) rests on DC-A's code read (D0, with cited D1/D2 records), DC-B's census (regex, approximate) and DC-C's literature read. No hypothesis in sec B has been run.
- **Both C.4 observations are D0 inferences.** The rv-scale mechanism assumes relative error is roughly constant as the z norm grows. The reset-init asymmetry rests on the decision log and the draft text, not on a built A1 config. The skeleton's actual preset could differ, and an H1-lite run or a skeleton read would settle each.
- **The ten-decision classification is interpretive.** Several rows span more than one decision. The gap-type tally (A.2) would shift at a finer granularity, but the layer ordering (L0-L3) would not.
- **H2's Yu & Dayan candidate may lose to the probe alone.** That is outcome F2, and it is pre-registered as a narrowing to ARC-156, not as a failure of the audit.
- **Mac-cost estimates** scale from the N5, W3 and emainit records' measured per-seed times. They are not re-measured.
