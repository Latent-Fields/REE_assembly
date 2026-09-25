# Claim synthesis -- MECH-039: which veto signal, and does "emergency" need to be a mode?

- **Date:** 2026-09-25 (UTC 07:45)
- **Session:** orch0925-mech157-synth (supervised subagent of orchestrate-20260924-breakthrough)
- **Chip:** chip-20260925-mech157-mech039-claimsynth (user decision rec-20260925-cd2e8b3f)
- **Claim:** MECH-039 (`provisional`), "Modes are stable regions in control-channel space, not separate modules" -- `docs/architecture/control_plane.md#mech-039`
- **Blocked proposal:** **EXP-0787** / EVB-1405 (`blocked_substrate`). This is not EXP-0781, which is MECH-037. The source chip is `chip-20260902-mech039-control-channel-substrate-gap` (open, AMBER pre-flight).
- **Code state measured:** ree-v3 `main` @ `2ce89ce`
- **Scope:** design options plus one recommendation. **Nothing is applied here.** No `claims.yaml` edit, no build, no blocked_note edit.

## 0. Skill fit

There is no FAIL cluster. EXP-0787 has never run. The Step-3 class is **substrate-not-ready**, so **no child claims are proposed**. This is a design-option synthesis: Steps 4-6b applied to an unratified choice. The node is `complicated (buildable)` once chosen.

## 1. Premises re-measured against live code

| # | Premise (source) | Re-measured 2026-09-25 | Consequence |
|---|---|---|---|
| P1 | Action readiness has no public accessor (EXP-0787 blocked_note, 2026-09-02) | **False, and it was already false at the time.** `CommitReadiness.get_readiness()` (`ree_core/policy/commit_readiness.py:324`) and `get_state()` (`:366`) are public. `get_readiness()` is live-called in `agent.py` (now `:7588`). `use_commit_readiness` defaults to False. | Build item 1 is struck. What remains is a documentation task: the flag set that is safe to combine with `use_commit_readiness=True`. |
| P2 | "No veto concept exists anywhere in ree_core" (blocked_note, and the pre-flight's `grep veto`) | **False as of 2026-09-24.** The keyword grep misses three **veto-shaped producers that already exist**, all default OFF: (a) `PAGFreezeGate` (MECH-279, `ree_core/pag/freeze_gate.py`, `is_active` at `:381`): a freeze commit when `z_harm_a x duration` crosses a threshold. (b) **Habenula negative-RPE de-commit** (ARC-108 JOB-2(d), `use_habenula_decommit`, `ClosureOperatorConfig.habenula_abort_enabled` in `governance/closure_operator.py:191`): aborts an in-flight commitment when `delta_t` falls below a threshold. This is the MECH-053 analogue that `control_plane.md` ties explicitly to `v_veto`. (c) **MECH-449 endogenous safety No-Go** (`use_gng_endogenous_safety`, landed ree-v3 `da9221c`, 2026-09-24): per-candidate harm z-score >= +2 SD against a per-agent running scale vetoes that candidate, and the fail-open guard never overrides it. | The question is no longer whether to build a veto from nothing. It is **which of three existing producers to use, whether to combine them, or whether to build a fourth, general interrupt.** (c) matches the MECH-040 wording almost exactly ("veto triggers when harm predictions cross a catastrophic threshold"). |
| P3 | Emergency needs a mode (source chip item 3: "add emergency to the SalienceCoordinator enum, or narrow the claim") | The enum has 4 modes and no emergency (`salience_coordinator.py:75-80`). **But MECH-039's own claim is that modes are regions in channel space, NOT modules.** Adding `emergency` as a discrete coordinator mode would build the discrete-module reading the claim argues against. It would also make the test **circular**: the MECH-039 DV clusters channel vectors, and if a coordinator label switches the channels, the clusters come out of the label. | The two framings in the source chip leave out a third. Emergency can be a **condition-elicited region** that is identified by the manipulation, not by a coordinator label. |
| P4 | Arousal is assemblable from live proxies | Confirmed (pre-flight): `e3.volatility_estimate` + `clock.e3_steps_per_tick`. | No build. Document the combination. |
| P5 | 3 of 6 channels are live (precision, commitment threshold, replay scheduling) | Not re-measured here. Carried from the 2026-09-02 check (`8dff6ab6a0`). | -- |

**What the channels need, per MECH-039's falsifier:** each channel must be *independently measurable* with non-zero cross-condition variance. So the veto channel needs a **tick-level scalar** that a recorder can read. It does not have to be a new behaviour.

## 2. Common thread (Step 4)

The falsifier makes a distinctive prediction: transitions are continuous and channel-by-channel, **except** hard-veto interrupts, which appear as fast, forced, multi-channel jumps that override the current regime. To test that, a veto channel has to be **observable** and has to be something that **can** force a transition. The emergency region has to be **elicited by the environment**, not declared by the substrate. Both open items are about keeping the measurement honest. Neither is really a capability gap.

## 3. Literature grounding (Step 5)

Based on articles retrieved from PubMed, alongside the five MECH-039 entries already ingested (`evidence/literature/targeted_review_connectome_mech_039/`: Munn 2021 arousal energy landscape, Margulies 2016 principal gradient, Ashourvan 2017 attractor basins, all `supports`; Vidaurre 2017 discrete metastates and Taylor 2022 LC-NBM coupling, both `mixed`):

- **The veto as a global, fast, surprise-recruited stop.** Wessel & Aron 2017 propose that unexpected events of every kind recruit a fronto-basal-ganglia stopping network, projecting through the subthalamic nucleus, that exerts a *global* suppressive effect on ongoing action and cognition ([DOI](https://doi.org/10.1016/j.neuron.2016.12.013)). *Implication:* the biological veto is **one global interrupt with several triggers** (errors, unexpected outcomes, unexpected percepts). That favours one composite veto channel fed by several producers over a single-producer proxy.
- **The emergency state as a network reconfiguration driven by a neuromodulator.** Hermans et al. 2011 show that acute stress, through beta-adrenergic (noradrenergic) and not cortisol activation, raises coupling across a salience network: dACC, frontoinsula, amygdala, thalamus, hypothalamus, midbrain ([DOI](https://doi.org/10.1126/science.1209603)). *Implication:* "emergency" is a **state of the continuous control system**, entered through arousal/NE, with no dedicated module. That is MECH-039's own framing, and it supports Option E-A (no enum entry).
- **Arousal gain and modes of LC activity.** Aston-Jones & Cohen 2005 describe phasic LC activity (exploit) and tonic LC activity (disengage/explore) as regimes of a single system ([DOI](https://doi.org/10.1146/annurev.neuro.28.061604.135709)). *Implication:* the arousal channel has regimes inside it. The pre-registered emergency signature (high arousal) should say whether it means high tonic level or high phasic volatility. MECH-040 already splits these into baseline and volatility.

## 4. Options

The two sub-questions (veto signal, emergency) are packaged into four coherent options, because some pairings do not make sense together. E-B, for instance, needs a trigger that only V-C provides.

### Option 1 -- composite read-only veto channel + emergency as a condition-elicited region (RECOMMENDED)

- **Veto (V-A):** add a read-only, tick-level `v_veto` readout (for example in a `control_channel_snapshot()` accessor) that combines the three existing producers: `freeze_active`, `habenula abort fired this tick`, and `fraction of candidates safety-No-Go'd this tick`. Each constituent is also recorded on its own. **No behaviour changes.** Each producer keeps its own default-off flag, and the experiment arms turn them on.
- **Emergency (E-A):** no enum change. The experiment elicits emergency with a **hazard-onset manipulation** (a sudden harm/imminence spike), labels those ticks by manipulation, and tests whether the channel vectors form a stable high-arousal / high-readiness / high-veto cluster. Task-engaged and default-mode-like are labelled by condition in the same way.
- **Claim-text change (proposed, not applied):** a note-level clarification that "named modes are hypothesised channel-space regions identified by eliciting condition, not SalienceCoordinator enum entries". Title and falsifier unchanged.
- **Cost:** a small accessor and recorder, plus a driver design. It fits the Wessel & Aron picture of one global interrupt with many triggers.
- **Risk:** the composite has no single threshold `v_veto`. The "fast forced transition" prediction is tested on veto **onsets**, not on a tunable threshold. The first combined run turns on several default-off producers together, so it needs a flag-compatibility smoke test.

### Option 2 -- build a general hard-interrupt + add an `emergency` coordinator mode

- **Veto (V-C):** a new catastrophic-harm interrupt that forces a SalienceCoordinator transition and emits a superseding commit event (the `control_plane.md` I2 note: "post-dispatch emergency interruption ... emitted as a superseding commit event from fast safety lanes").
- **Emergency (E-B):** a 5th mode, `emergency`, triggered by high arousal + veto + readiness.
- **Cost:** a real `/implement-substrate` build with new behaviour. Every `DEFAULT_GATE_WEIGHTS` table (sd_033a..e, autonomic, hc_viability, sensory_buffer, and others) needs an emergency row, and SD-032a/MECH-261 semantics change.
- **Risk:** this is the **circularity problem (P3)**: the channels would be driven by the label that the test then clusters. It builds the discrete-module reading that MECH-039 exists to argue against.

### Option 3 -- MECH-449 safety No-Go as the veto + emergency as a condition-elicited region

- **Veto (V-B):** `v_veto := gng_safety_z_threshold`, with the channel read as `n_signal_fired` per tick from `gng_safety_diagnostics()`. This is the closest literal match to MECH-040 and has a single tunable threshold.
- **Emergency:** as in Option 1 (E-A).
- **Cost:** no build beyond a per-tick counter read.
- **Risk:** it is a per-candidate **pruning** veto, not an interrupt that overrides the regime, so the "fast forced transition" prediction may simply be untestable on it. It also needs the whole GNG arming chain (`use_go_nogo_constitution`, F-eligibility demotion or shortlist, a live modulatory accumulator, K >= 2), which is a heavy flag stack for a first combined run.

### Option 4 -- narrow the claim: PAG freeze as a caveated proxy, drop emergency

- **Veto (V-D):** `PAGFreezeGate.is_active` with stated caveats (freeze is immobility, which is narrower than a general veto).
- **Emergency (E-C):** narrow MECH-039's example-mode list to task-engaged and default-mode-like only.
- **Cost:** a claims.yaml text edit only.
- **Risk:** it throws away the claim's most distinctive prediction, the veto-forced exception. Freeze is also one specific defensive response, so a cluster found under it would say little about modes in general.

## 5. Decision block

| Option | Veto channel | Emergency | Claim-text change | Build | Tests the veto-exception prediction? | Circularity risk |
|---|---|---|---|---|---|---|
| **1 (rec)** | composite of 3 existing producers, read-only | condition-elicited region | note clarification | small | yes (onsets) | none |
| 2 | new general interrupt | 5th coordinator mode | none | large | yes | **high** |
| 3 | MECH-449 safety No-Go only | condition-elicited region | note clarification | tiny | weakly (pruning, not interrupt) | none |
| 4 | PAG freeze proxy | dropped | narrowing | none | weakly | none |

**Recommendation: Option 1.** It uses the three veto producers that were built after the 2026-09-02 audit, which P2 shows were missed. It keeps the measurement non-circular (P3). It matches the literature picture of one global, many-trigger interrupt and of emergency as a reconfiguration of a continuous system rather than a module. The only build is a read-only accessor. Option 3 is the cheap fallback if the user wants a single tunable threshold. Option 2 should be chosen only if the user wants the general interrupt *for its own sake* (MECH-040/053 behaviour). It should not be chosen to unblock MECH-039.

**Owed after the decision, whichever option is chosen (not done here):** (1) Update EXP-0787's blocked_note: strike item 1 (P1), and record that the veto is now a choice among the three P2 producers and that emergency follows the chosen option. The source chip's instruction to edit **EXP-0781** is wrong (that entry is MECH-037). (2) Document the `use_commit_readiness` safe-combination flag set. (3) If Option 1 or 3 is chosen, `/governance` applies the MECH-039 note clarification and `/implement-substrate` adds the accessor. (4) Resolve or re-scope `chip-20260902-mech039-control-channel-substrate-gap`.

## 6. Red-team (Step 6b)

See Section 7, appended after the adversarial pass.
