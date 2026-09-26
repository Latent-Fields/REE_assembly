# Dynamic-control discrimination pass (DCD2): which of H1 / H2 / H3 is REE actually missing?

- **Written:** 2026-09-26T13:40Z by orchestrator `orchestrate-20260924-breakthrough-c2` (claim `orchestrate-20260924-breakthrough-c2-dcd2`), on the user's 2026-09-26 "post-governance dynamic-control discrimination pass" instruction.
- **Status:** plan of record for this pass. Two probes are launched from it (sec 4). **Nothing here changes `ree_core`, a gate, a preset, `claims.yaml` or a registered claim.** Results update ARC-155 / ARC-156 / Q-111 through the ordinary governance route, not here.
- **Inputs read:**
  - `docs/thoughts/2026-09-26_endogenous_operating_point_regulation_and_regime_coordination.md` and its intake (ARC-155, ARC-156, Q-111);
  - `dynamic_control_audit_20260926.md` (e3cafebab3; H0-H4) and `_inventory_` (a783e4744d6);
  - `commit_gate_read_int_vs_native_20260926.md` (a417b6f578);
  - autopsies V3-EXQ-1107, 1106, 1090, 1067 and 1104 (confirmed 2026-09-26);
  - `cea_onset_input_reprobe_20260925.md`;
  - the open chip `chip-20260926-pag-freeze-lock-confirmer`.
- **Governance state taken as authoritative.** The 14:21-14:23 (local) flag resolutions and the 13:48 batch of 8 applied autopsies are not re-opened here.

## 1. The question, restated so it can fail

The thought proposes three separable deficits:

- **H1 (operating-point scale):** a learned control quantity moves in scale while its consumer uses a fixed raw bar.
- **H2 (regime-surviving escape evidence):** a strong regime suppresses the evidence needed to leave it.
- **H3 (composition / arbitration):** individually valid controllers remove each other's substrate.

There is a fourth reading that the thought itself flags as distinct, and it must be tested **first**, because it sits upstream of all three:

- **H-SV (signal validity):** the control quantity does not carry the condition information at all, so no bar (H1), escape route (H2) or arbiter (H3) can make the regime appropriate. ARC-155 already states that "no denomination can restore information the producer has already lost". The CeA re-probe (GFLAG-0557) is a measured instance: relative gates on `z_harm_a` are negative against their own floor.

Rule for this pass: **trace each failing family along observation -> representation -> prediction -> evaluation -> control -> commitment -> action -> experience, and test the earliest edge first.** H1, H2 and H3 are only testable at a site where the upstream signal is shown to be information-bearing (D1). A rescue is credited to a mechanism only if an arm that changes behaviour *without* the claimed causal route fails to produce it.

## 2. The two live families, with their causal chains as measured today

### Family C: commitment (the only regime switch live at defaults)

| edge | measured state | source |
|---|---|---|
| prediction -> control signal (rv's raw input) | **mixed semantics.** On an E3 tick it is E2's *predicted displacement* (z_t vs E2's prediction of z_{t+1}). One tick later it is a real one-step error. After that it is increasingly stale drift. Confirmed at D0 and D1 | commit-gate read sec 0/4; GFLAG-0486 |
| control signal -> operating point | rv p50 is 0.0026-0.0071 against a bar of 0.40, **two orders of magnitude apart**. The bar is never approached after the start. The crossing at env step 4 is fully set by `precision_init` 0.5, alpha 0.05 and the bar (0.95^5 x 0.5 < 0.40). It is an **initialisation artefact** of the same kind as the EMA zero-init (GFLAG-0559) | commit-gate read sec 2 |
| operating point -> regime | committed >= 98% from tick 5 in all 9 runs (NATIVE, INT-CODEC, NATIVE-NOKNOBS), including runs with no learning. Absorbing (GFLAG-0346) | commit-gate read sec 3 |
| regime -> action -> experience | Committed argmin settles into a self-consistent repeated-action loop whose one-step error is small **by construction**. The regime may therefore manufacture the low-error evidence that keeps it in place (an H2 shape), or the loop may still see a world change (H2 not needed). **Unmeasured** | commit-gate read sec 3 (NATIVE's flat k-profile) |

**Consequence:** "INT and NATIVE commit identically" says nothing yet about organismal confidence. The gate is dominated by its initialisation, EMA and bar geometry. No commitment behaviour is to be read as evidence about A1, self-preservation or mature deliberative commitment until probe C (sec 4.1) separates the measurement/control issue from the scientific claim.

### Family F: freeze -> release -> veto (the thought's clearest H2 and H3 cases)

| edge | measured state | source |
|---|---|---|
| observation -> representation (`z_harm_a`) | After training, `||z_harm_a||` is 2.8-4.2 and **identical on all 90 eval ticks**. It is unclear whether the encoder is saturated and input-insensitive, or whether its input simply stopped changing because the agent was frozen (a frozen agent sees an almost static scene). **This is the pivotal confound.** The CeA re-probe shows the onset information is lost by stream choice | 1107 autopsy; GFLAG-0557 |
| representation -> operating point | fixed `theta_freeze` 0.8 against 2.8-4.2, so frozen from tick 1; `max_freeze_duration` 0 means it never exits | 1107 |
| regime -> release evidence | the option-B release path read 0 drive-steps-while-frozen on 3/3 seeds. The release reads movement, and the lock stops movement | 1106 |
| regime -> another controller | the MECH-449 veto fires, is calibrated and is silent on its control, yet the executed action is 0 on 3,000/3,000 ticks (freeze on, pre-STAY-fix) | 1090 |

**Consequence:** if `z_harm_a` is input-insensitive even while the agent moves, the whole family is an H-SV failure at the representation edge. Recalibrating the PAG (H1), adding a release route (H2) or adding an arbiter (H3) would then be cosmetic, and the right target is the harm encoder or stream (MECH-279 amend is then the wrong target). Only if `z_harm_a` is input-sensitive when the agent moves do H1, H2 and H3 at this site become testable.

**Why these two families and not mode switching or effort:**
- **Mode switching:** the mode register has no behavioural consumer (DC-A O3/O4). A test there measures a quantity nothing reads.
- **Effort:** 1104 is signal validity by its own autopsy (a model-error term, not effort). Scaling it would make selection noise-driven.
- Both stay parked behind their owners (`mech019-operating-mode-enabled-consumer`; GFLAG-0447).

## 3. Discriminating logic (what each outcome would mean)

| probe | outcome | reading |
|---|---|---|
| **C0** signal validity | the realised-error input separates a hidden world change and the current mixed input does not | the earliest break in Family C is **signal provenance**. Fix it before any bar work. H1 at the commit site is tested on the realised input |
| C0 | neither input separates the change | H-SV at the E2 or representation edge. The commit gate cannot be made appropriate by any bar. H1 and H2 are untestable here, so stop and route to W3/E2 |
| **C1** operating point (valid input only) | a fixed bar tuned on seeds {0,1} at stage S1 keeps its appropriateness on held-out seeds and at stage S2 | **H1 weakened** at this site: scale is stable once upstream is fixed, and the 0.40 problem was a mis-set constant plus an init artefact, not a need for endogenous regulation |
| C1 | the tuned fixed bar loses appropriateness on transfer (seed or stage) and the own-scale bar keeps it | **H1 supported** at this site |
| C1 | own-scale bar is no better than its occupancy-matched random and time-shuffled controls | own-scale denomination is occupancy-stable but content-blind. ARC-155 is necessary but not sufficient here (audit H1 F1) |
| **C2** evidence availability | after a world change, the committed argmin policy's realised error rises about as much as under forced sampling | commitment does **not** starve its own exit evidence, so **H2 is not needed** at this site |
| C2 | the committed loop hides the change (error rises only under sampling), and sparse probe actions at <= 5% restore detection without globally weakening commitment | **H2 supported** at this site; the surviving evidence source is identified |
| **F0** representation validity | with freeze OFF (and under a scripted diversity policy), `z_harm_a` does not track hazard proximity | **H-SV** at the harm representation. Freeze, veto and CeA failures share an upstream cause. H1, H2 and H3 are not the right account of Family F yet |
| F0 | `z_harm_a` tracks hazard proximity when the agent moves | representation holds, and the 1107 constancy was frozen-input. Go to F1-F3 |
| **F1** lock confirmer | freeze-ON lives collapse and freeze-OFF lives do not | lock confirmed (the chip's rule) |
| **F3** composition (Q-111 leg-1 precondition data, **not** a Q-111 test) | with freeze OFF and executed-action diversity restored, the veto changes executed actions and hazard contact versus veto-OFF | 1090's inert veto was substrate removal by freeze. **H3 weakened:** fixing the upstream lock is enough and no arbitration principle is indicated |
| F3 | action diversity is restored but the veto still has no organism-level effect | a genuine composition or authority defect; H3 stays live |
| F3 | action diversity collapses with freeze OFF (for example into a committed argmin loop) | the veto is starved by **Family C** instead. The two families share a substrate-removal route through commitment. That is a concrete, measured H3 case, and the order of repair is C then F |

**Umbrella verdict rule:**
- "REE lacks endogenous operating-point regulation or regime coordination" is **weakened** wherever the earliest broken edge turns out to be signal validity, or wherever a correctly-fed fixed bar transfers.
- It is **supported only site by site**, where the valid-input own-scale arm beats the transferred fixed bar, or a surviving evidence source is needed and sufficient.
- Neither probe can support a central executive, and none is built.

## 4. Probes launched

### 4.1 Probe C: commit-gate discrimination (`bt0926-cgdisc`, Mac, harness-only)

- **Code:** branch `integration/coupled-loop-repair` @ `4070b0e` (archive tag). The W3 protocol provides a trained E2 world head; all four reset-init knobs are ON, per the provisional 09:33Z decision 4.
- **Constraint:** the realised-error input and the alternative bars are applied by **probe-side instrumentation in a private worktree**. No `ree_core` commit.
- **Hidden world change:** within one continuous life (no episode reset at the change), a mid-life change: the N5 action-map permutation, and as a second kind a layout redraw without reset. The change is used only for **scoring**. No controller sees it.
- **Factors:**
  - input {current mixed, realised one-step};
  - bar {0.40 absolute, fixed-tuned (calibrated on seeds 0-1 at stage S1, frozen), own-scale ARC-029(D) quantile};
  - policy clamp for C2 {native, forced-committed, forced-sampling, committed + <= 5% probe actions}.
- **Controls:** occupancy-matched random commitment; time-shuffled rv; oracle de-commit ceiling.
- **Stages:** S1 is W3 at its standard dose, S2 is a longer dose. Seeds are 5 fresh ones, with a W3 disc4 pre-screen.
- **Exclusions:** the first 8 ticks after any reset and the `precision_init` decay window are excluded from every DV.
- **DVs:**
  - separation (AUROC or hit minus false alarm within k ticks of the change);
  - appropriateness (P(uncommitted | within k after change) minus P(uncommitted | elsewhere));
  - occupancy stability across seeds and stages;
  - post-change realised error under each policy clamp.
- **Stop rule:** if C0 shows neither input separating the change, stop after C0 and report H-SV.

### 4.2 Probe F: freeze/veto earliest-edge probe (`bt0926-fzdisc`, cloud, via `/queue-experiment`)

This probe **absorbs `chip-20260926-pag-freeze-lock-confirmer`**, keeping its design and pre-registered decision rule, and adds the representation leg and the veto leg.

- **Harness:** the 1107 config on `ree-v3` main, trained harm stack, 3 seeds.
- **Arms:**
  - freeze {ON, OFF};
  - under freeze OFF, veto {ON, OFF} (MECH-449 endogenous);
  - a scripted random-walk diversity policy (training untouched) as the F0 representation reference.
- **Readouts:**
  - per-tick `||z_harm_a||` distribution;
  - a linear-probe R^2 of `z_harm_a` on true hazard distance (oracle used for **scoring only**), compared across untrained, trained-own-policy and trained-scripted;
  - freeze_active fraction, n_commits and n_releases;
  - episode lengths and contact rate;
  - executed-action entropy (the 1090 action-diversity precondition);
  - the veto's effect on executed action and hazard contact.
- **Pin:** `pin_recording_substrate` at process start.

## 5. What this pass will NOT do

- Build an arbitration module, executive or global controller.
- Change the 0.40 bar, `theta_freeze`, any preset or any acceptance gate.
- Treat a behavioural improvement from a hand-tuned constant as H1 support. Transfer is the test.
- Read commitment occupancy as a DV where the bar makes it about q by construction.
- Re-litigate governance's 2026-09-26 flag or autopsy adjudications.
- Queue a Q-111 test proper. F3 is recorded as precondition data, per Q-111's own note.

## 6. Follow-on, contingent (not launched)

| if | then |
|---|---|
| C finds H1 supported | the next step is a D2 behavioural test of the own-scale bar on the realised input in a no-reset single life, which is the Q-108 class. It is a candidate for the post-A1 organism test, not a change to A1's gates |
| C finds H2 supported | ARC-156 gains its commitment site. The probe-action surviving source is tried at the N5b detector (audit H2), where the same design applies |
| F0 finds H-SV | route to the harm-encoder or stream owner (SD-011 aux, GFLAG-0557 lineage). Do not amend MECH-279 |
| F0 finds the representation holds | ARC-155's PAG operating-point and ARC-156's surviving-input designs become runnable. H4 unblocks, apart from the MECH-280 build decision, which stays with the user and governance |
| H0 (running) | if the episode reset is doing the exit work, both families' regimes will look more recoverable in multi-episode drivers than they are. Probe C's single-life design already controls for this |
