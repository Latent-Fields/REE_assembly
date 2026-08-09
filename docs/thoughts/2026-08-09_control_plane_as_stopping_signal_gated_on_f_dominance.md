Status: processed
Intake: evidence/planning/thought_intake_2026-08-09_control_plane_stopping_signal.md
Claims: MECH-488

---

## REE_assembly Thought

### Control Plane as a Stopping Signal: an STN-Hyperdirect Analogy, and Why It's Not Buildable Yet

---

### Origin

Prompted by noticing a structural parallel between REE_assembly's own coordination
plane (the meta-infrastructure that manages concurrent sessions -- `task_claim.py`
arbitration, governance/pause locks) and REE's cognitive control plane: the
coordination plane's biggest job is often *stopping other work elsewhere* --
default-permit until a conflict is detected, then a binary "you are not the owner,
stop" verdict, or a broad scope lock during a risky regen. That's not the
tonic-inhibition-with-selective-release shape of classic basal ganglia action
selection -- it's a fast, conflict-*triggered*, network-wide brake. Worth checking
whether REE's own control-plane design already has (or is missing) the analogous
mechanism.

---

### 1. Two distinct mechanisms in the literature, not one

**(a) Tonic inhibition + selective disinhibition** (the classic direct/indirect
pathway "selection" model): default state is broad suppression of all candidate
motor/cognitive programs, with focal release for the winner.
- Mink 1996, *Prog Neurobiol* 50(4):381-425.
- Redgrave, Prescott & Gurney 1999, *Neuroscience* 89(4):1009-23, "The basal
  ganglia: a vertebrate solution to the selection problem?"
- Gurney, Prescott & Redgrave 2001, *Biol Cybern* 84(6) (the GPR model, Parts I+II).

**(b) STN hyperdirect-pathway global brake** (a different circuit, not a variant of
(a)): a fast, conflict/novelty-triggered signal that raises the decision threshold
or pauses selection *network-wide*, rather than suppressing one channel.
- Aron & Poldrack 2006, *J Neurosci* 26(9):2424-33.
- Aron, Behrens, Smith, Frank & Poldrack 2007, *J Neurosci* 27(14):3743-52
  (tractography confirming the IFC-preSMA-STN hyperdirect network).
- Frank 2006, *Neural Netw* 19(8):1120-36, "Hold your horses" -- the
  computational, RL-relevant formalization: STN dynamically raises the decision
  threshold under response conflict.
- Wiecki & Frank 2013, *Psychol Rev* 120(2):329-55 -- the clearest existing
  computational precedent for combining BOTH mechanisms in one RL-style
  architecture: a frontal conflict signal projects to STN, which pauses/gates the
  per-channel selection machinery rather than replacing it.

The coordination-plane parallel maps onto (b), not (a): conflict-triggered,
global, binary-stop -- not tonic per-channel suppression.

---

### 2. REE already has both circuit types -- unintegrated

- **(a) in `ree-v3/ree_core/predictors/e3_selector.py`**: `_go_nogo_eligibility_gate`
  (MECH-449/ARC-107, line ~1563) + `_lateral_settle` (MECH-450/ARC-108, line
  ~1751) -- a Go/No-Go floor plus a learned surround-inhibition matrix between
  competing candidates, explicitly citing Mink 1996 in the source.
- **(b) in `ree-v3/ree_core/pag/freeze_gate.py`** (MECH-279): sustained
  `z_harm_a x duration` crossing `theta_freeze` commits the agent to a
  no-op/freeze state; exit requires GABAergic tone. `control_plane_signal_map.md`
  (MECH-004) already names this K10, "hard veto threshold: catastrophic
  interrupt trigger," functionally mapped to PAG.

They're separate regulators behind separate off-by-default flags. No shared
abstraction connects them. MECH-004's own signal taxonomy (S1 outcome, S1b
harm/benefit, S2 trajectory-stability, S3 aversive/interruptive, S4 safety
baseline/volatility, S5 reality-coherence conflict) has no slot for "how
contested was the last selection" -- there is no S6. K10 is fed only by S3/S4
(harm, safety-volatility), never by anything selection-internal.

---

### 3. The specific missing wire

`e3_selector.py` already computes exactly this kind of signal --
`_gap_scaled_commit_pick`'s `gap_norm` (the decision-gap between top candidates,
used to grade MECH-439's conflict-graded commit temperature). But it's built as a
private, local quantity: used once to set sampling temperature, then discarded.
MECH-449's own doc says the quiet part -- `_gap_scaled_commit_pick` is "no
parallel module," deliberately siloed on `E3TrajectorySelector`. It doesn't feed
MECH-449's own Go/No-Go gate, let alone the control plane's K10/K5.

The Wiecki & Frank (2013) precedent says exactly what's missing: a decision-gap /
selection-conflict signal, propagated out of the local selection step and into the
global control layer (K5 control-allocation, K10 hard-veto), the way cortical
conflict detection feeds STN in biology.

---

### 4. Confirmed: both halves of this idea are currently dead, and for the SAME reason

Checked whether `gap_norm` and the PAG freeze-gate's non-engagement were
independent problems, or coupled. They are coupled -- to the same root cause,
and this is not a hypothesis, it's measured:

- **Receiving end (K10/PAG) doesn't engage ecologically.** MECH-280's claims.yaml
  entry: `pag_release_count_end = 0` across all 12 runs of V3-EXQ-483e;
  `z_harm_a` never crosses `theta_freeze` in situ. Both recalibration routes are
  closed or absorbed: axis (a) (`sd_037_axis_a_consumer_input_recalibration_plan.md`)
  is empirically unmeetable -- V3-EXQ-620 measured the input distribution
  *identically zero* at fishtank baseline (pooled n=2939), not just below
  threshold, so there's no upper tail to recalibrate against. Axis (b)
  (`sd_037_axis_b_sustained_threat_curriculum_plan.md`, drive the same signal
  harder via env curriculum) has since been consolidated into the MECH-439
  F-dominance / candidate-pool-collapse conversion-ceiling cluster -- the
  project's current single biggest standing blocker (`docs/roadmap.md`: "the live
  root choke").

- **Sending end (`gap_norm`) is also degenerate, and the project's own autopsy
  says why.** V3-EXQ-689 (2026-06-19, MECH-439's own first falsifier, the
  experiment built to test the conflict-grade levers) self-routed
  `substrate_not_ready_requeue`: `gap_spread_seeds = 0` across all 3 seeds, the
  F-gap "pinned in the near-tie bin." The confirmed autopsy
  (`failure_autopsy_V3-EXQ-689_2026-06-19.md`) states it directly: *"This
  near-tie concentration is itself a manifestation of the F-dominance MECH-439
  asserts."*

So this isn't two design gaps to route around each other. It's one design idea
(an STN-style conflict-triggered global brake) whose input signal and whose
receiving mechanism are *both* currently dead for the same documented reason.
Neither axis (a)/(b) recalibration plan nor MECH-449's design doc ever considered
wiring `gap_norm` into K10/K5 as a second, independent trigger -- grepped both
recalibration plans directly, zero mentions.

---

### 5. Implication

Not buildable now. It's a **prediction to check once MECH-439 clears**, not a
build to start: if/when candidate-pool diversity reaches committed action (the
active BG-commitment / F-dominance thread's own target),
`gap_norm` should stop pinning near-tie and the PAG freeze-gate should start
seeing real crossings -- both should un-stick together, because they're stuck
together. That would be the point to formalize an S6 "selection-conflict" signal
in MECH-004 and wire `gap_norm` into K5/K10, mirroring Wiecki & Frank's
architecture (STN as a modulator *over* the selection layer, not a replacement
for it). Trying to build the wiring before MECH-439 clears would be wiring a dead
signal into a gate that doesn't respond to it -- untestable by construction.

---

### 6. Open questions

1. Once MECH-439/V3-EXQ-689a-successor resolves, does `gap_norm` spread and PAG
   engagement recover *together*, confirming the shared-root-cause reading -- or
   does one recover without the other (which would mean they're not as coupled
   as the 689 autopsy's single data point suggests)?
2. Should K10 (hard veto) and K5 (control allocation) receive the conflict signal
   identically, or does biology's split (STN feeds both threshold-raising AND
   response-pausing via somewhat different projections) argue for two separate
   knobs rather than one?
3. Is there a lighter-weight test available now -- e.g. measuring `gap_norm`
   spread as a *diagnostic* alongside existing MECH-439 falsifiers, without
   wiring anything -- to get earlier signal on Q1 without waiting for full
   closure?

---

### Possible affected components

- E3 / `ree-v3/ree_core/predictors/e3_selector.py` (`_gap_scaled_commit_pick`,
  `_go_nogo_eligibility_gate`)
- Control plane / `docs/architecture/control_plane_signal_map.md` (MECH-004 --
  candidate S6 signal class, K5/K10 wiring)
- PAG / `ree-v3/ree_core/pag/freeze_gate.py` (MECH-279/MECH-280)
- MECH-439 F-dominance conversion-ceiling campaign (gating dependency, not this
  thought's to resolve)
