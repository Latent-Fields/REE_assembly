# MECH-287 option B: a hippocampal-invalidation -> PAG freeze-exit path (design)

- Session: `bt0925-mech287b` (subagent of orchestrate-20260924-breakthrough)
- Chip: `chip-20260925-mech287-anchor-freeze-exit-build`
- Governing decision: USER option B, 2026-09-25 ~08:00Z (ledger chip
  `chip-20260925-mech287-lock-dv-path-decision`): BUILD the missing path, then test it on the
  lock DV (option C, rec-20260925-b23d15b9).
- Motivating analysis: `mech287_lock_dv_inert_pag_path_20260925.md` (REE_assembly `dd0a0ef864`),
  GFLAG-0506. EXP-0371 stays blocked (`7adafa4286`).
- Substrate read: ree-v3 origin/main `2832fd2`, which includes the freeze no-op fix `1fc881692d`
  (GFLAG-0508: the freeze and orienting no-op is now the STAY class, not 0/UP).
- Written: 2026-09-25T10:19:44Z

## 1. The gap, restated and re-measured

The premises of the chip were re-checked against `2832fd2` before this design was written.

- `PAGFreezeGate.tick()` releases when `z_harm_a_norm < theta_freeze * override_factor * gaba_tone`
  (`ree_core/pag/freeze_gate.py`, step 5). This still holds.
- `pag_z_norm` is `||z_harm_a||` in this lineage. The LPB and MECH-219 redirects are off, and
  `z_harm_a` has no hippocampal input. This still holds.
- `gaba_tone` is 1.0 in practice. `set_gaba_tone` still has no caller in `ree_core`.
- `override_signal` is 0.0 because SD-037 is not constructed in the MECH-287 lineage. This still
  holds.
- The MECH-287 chain ends at `beta_gate.release()` (`agent.py`, the `use_vs_commit_release` hook).
  That releases the E3 commitment, not the PAG freeze. This still holds.
- The freeze no-op defect is FIXED on origin: ree-v3 `1fc881692d`, landed before this session. A
  behavioural lock-DV reading is therefore allowed on any commit at or after it. The V3-EXQ-475
  lock itself was recorded under the UP defect, so whether the lock reproduces with STAY is
  **unmeasured**. That is the job of the precondition gate in section 6.

So there is no path from the MECH-287 manipulation to any input of the PAG exit. This build adds
one.

## 2. Neuro grounding (brief)

Freezing is expressed through the ventrolateral PAG. Its expression is gated by context through a
hippocampal -> medial prefrontal -> PAG descending route:

- **Context gating of fear expression is hippocampus-dependent.** Conditioned freezing is
  context-specific, and extinction renews on a context change. The context representation that
  licenses or vetoes fear expression is hippocampal, and it is read out through vmPFC/IL/PL.
  Sources: Maren, Phan & Liberzon 2013 (Nat Rev Neurosci 14:417); Bouton's renewal literature.
- **Hippocampal input gates PFC fear output.** Sotres-Bayon et al. 2012 (Neuron 76:804):
  ventral-hippocampal and BLA inputs gate prelimbic fear output.
- **A direct prefrontal -> l/vlPAG projection discriminates safe from threat context and controls
  freezing.** Rozeske et al. 2018 (Neuron 97:898). This is the load-bearing reference: descending
  mPFC -> PAG activity tracks the context discrimination, and manipulating it changes freezing in
  the safe context.
- Mobbs et al. 2007 (Science 317:1079), already cited in claims.yaml, adds that vmPFC -> PAG
  control shifts with threat imminence.

**The REE mapping.** An anchor invalidation is the substrate's analogue of "the context this
schema was anchored to no longer holds". It covers a MECH-287 broadcast reset (T3) or a
MECH-284/269 hysteresis reset. The analogue carries that verdict down a descending route to the
PAG freeze-exit criterion, where it makes release easier. It does not force release, and it does
not touch the harm stream.

These references were cited from the existing literature record and memory, not re-pulled. No gap
is load-bearing for the build: the mapping is a modelling choice that the test below falsifies.
If governance registers a claim for this path, a `/lit-pull` for Rozeske 2018 and Sotres-Bayon
2012 is owed.

## 3. Options weighed

| # | Option | Verdict |
|---|--------|---------|
| O1 | **Descending release raises the PAG exit threshold.** A decaying trace of hippocampal anchor-invalidation events multiplies `exit_threshold` by `(1 + alpha * r)`. | **CHOSEN.** Graded, and specific to the exit criterion. Mirrors the already-built SD-037 `alpha_override` factor, so it is an established consumer shape. Leaves `z_harm_a` untouched. |
| O2 | A real `gaba_tone` producer driven by anchor reset. | Rejected. `gaba_tone` also sets the SD-036 harm-state recurrence in the latent stack, so it would move `z_harm_a` itself. Freeze exit and the harm stream would then co-vary, and the DV would stop being attributable to the exit path. Biologically, GABA tone is a global modulator, not the context signal. |
| O3 | Hard release: an anchor reset clears the freeze, like `beta_gate.release()`. | Rejected. It is binary and bypasses the graded `z_harm_a` exit criterion. It would make freeze duration a pure function of broadcast timing, which is true by construction. |
| O4 | Feed invalidation into SD-037 `override_signal`. | Rejected. It constructs `BroadcastOverrideRegulator`, which has about six other consumers (salience, BLA, CeA, lPFC eta, replay seeding). That contamination is wide, and the result would not isolate the PAG path. |

Not built, recorded as a variant: descending suppression of freeze ENTRY (Rozeske's safe-context
effect covers expression generally). This build touches exit only, so entry dynamics and the
existing MECH-279 entry contracts are unchanged.

## 4. Specification (O1)

**Event source: invalidation, not ordinary remap.** An anchor that leaves the active set because a
new segment boundary installed its successor is ordinary segmentation. It fires in every
segmenter-on arm and would make the path independent of MECH-287. FIFO cap evictions are also
housekeeping. The drive therefore counts only two kinds of event:

- (T3) `HippocampalModule.apply_invalidation_broadcasts_to_regions`: a broadcast that marked at
  least one active anchor inactive contributes its `strength`.
- (H) `AnchorSet.tick_hysteresis`: each anchor fired by the V_s_anchor hysteresis contributes 1.0
  (MECH-284 staleness when `use_mech284_hysteresis`, otherwise the internal proxy).

`pag_descending_release_source = "invalidation"` (T3 + H, the default when the path is on) or
`"broadcast"` (T3 only). The two event kinds are also counted separately, so an analysis can split
them.

**Trace (per env step, in `sense()`):**
`d_t = min(1, sum_T3 strength + w_H * n_H)` and `r_t = max(r_{t-1} * decay, d_t)`, where
`w_H = 1` for "invalidation" and `0` for "broadcast", and `decay` is
`pag_descending_release_decay`, default 0.95/step (half-life about 13.5 env steps). The trace is
needed because the PAG gate ticks only on E3 ticks, while invalidations happen on env steps and
the broadcast queue is drained at the start of every `sense()`.

**Consumer (in `select_action()`, at the PAG tick):**
`exit_threshold = theta_freeze * override_factor * (1 + alpha_desc * r) * gaba_tone`, where
`alpha_desc` is `pag_descending_release_alpha`, default 1.0 when the path is on. The value is
recorded on `PAGFreezeGateOutput.descending_release`.

**Config (REEConfig, all three `from_dims` sites):**

| Param | Default | Purpose |
|-------|---------|---------|
| `use_pag_descending_release` | False | master switch: trace maintained and passed to the gate |
| `pag_descending_release_alpha` | 1.0 | gain on exit threshold (copied to `PAGFreezeGateConfig.alpha_descending`) |
| `pag_descending_release_decay` | 0.95 | per-env-step trace decay |
| `pag_descending_release_source` | "invalidation" | "invalidation" or "broadcast" |

**Bit-identity.** With the master switch off, nothing is computed and the gate receives 0.0. The
factor is `1 + 0 * 0 = 1.0` exactly, so the arithmetic path is unchanged. **With the master switch
on and `alpha = 0`, behaviour is also bit-identical.** A driver can therefore run warmup with
`gate.config.alpha_descending = 0` and switch it on at eval entry, which gives knob-pair warmups
that are identical by construction (section 6). The trace and counters use no RNG.

**Dependencies.** The path needs `use_anchor_sets`. The T3 half also needs `use_per_region_vs` and
`use_invalidation_trigger`. With these off, the drive is always 0: present but inert. The agent
records that state rather than raising, and the liveness counters in section 5 expose it.

**MECH-094.** The trace advances only in waking `sense()`. The PAG gate's `simulation_mode` path
already returns a zeroed output without updating state, and nothing on the replay path touches the
trace.

**Readouts (agent attributes, read-only):** `_pag_desc_release_trace`,
`_pag_desc_n_drive_steps`, `_pag_desc_n_drive_steps_while_frozen`, `_pag_desc_n_t3_events`,
`_pag_desc_n_h_events`. `_pag_desc_n_drive_steps_while_frozen` is the reach-in-regime
instrument. The accessor is `REEAgent.pag_descending_release_diagnostics()`.

**Build-time measurement (2026-09-25, added after the build): T3 is effectively redundant.**
A boundary's own dual-trace remap in `tick_anchor_set` deactivates the `segment_id_old` anchor
BEFORE `apply_invalidation_broadcasts_to_regions` runs. The broadcast born from that same boundary
therefore finds no active target. This was observed directly: broadcast `('fast', '0.0')` arrived
while the only active anchor was `('fast', '0.1')`. So the live reach is broadcast -> MECH-284
staleness -> hysteresis reset (H), which is the claim's own "trigger -> accumulator -> anchor
reset" chain. It is not the T3 shortcut. This is why "invalidation" (T3 + H) is the default source,
and why "broadcast" alone is expected to be near-silent. It also means the trigger-lesioned arms
still carry passive-proxy H resets, so P2 below is an interaction, not a contrast that is true by
construction. A short untrained V3-EXQ-1097 `D_BOTH_ON` rollout (2 x 200 steps, about 0.65 s per
step on the Mac) produced 0 T3 resets, 0 H resets and 0 freeze commits. Reach in the trained lock
regime is therefore wholly unmeasured.

## 5. Contracts (build gate)

- **C1 bit-identity OFF.** A fixed-seed rollout with the full MECH-287 lineage flags plus the
  freeze gate is compared across three configurations: path absent (defaults), master ON with
  alpha 0, and the same run hashed on actions, latents and RNG state. All three must be identical.
- **C2 gate-level reach (D2).** A matched `z_harm_a` trajectory that sits between `theta` and
  `theta * (1 + alpha)`. With a descending-release pulse the freeze releases earlier, and its
  duration is strictly shorter than in the matched control with no pulse. A positive control with
  alpha 0 gives equal durations, so the test is not vacuous.
- **C3 agent-level reach (D2).** Two agents are built identically on the same seed. In one, an
  injected broadcast invalidates an active anchor during `sense()`. That agent's trace becomes
  positive, and the next PAG tick's `exit_threshold` exceeds the matched control's.
- **C4 source exclusion.** An ordinary boundary remap (successor anchor installed) does not drive
  the trace. The "broadcast" source ignores hysteresis resets.
- **C5 liveness on a real rollout.** With the lineage flags on, a real env rollout shows the path
  moving a downstream number ON vs OFF. That number is the recorded `exit_threshold`, or the trace
  when invalidations occur. This follows /implement-substrate 5(b2).

## 6. Pre-registered lock-DV test (NOT queued this session)

**Stage 0: precondition gate (runnable, owed first).** On today's substrate (STAY no-op), run the
comparator arm (V3-EXQ-1097 `A_BOTH_OFF` lineage flags, path OFF) at 475 scale on at least 3
seeds. Record:

1. **Lock reproduces.** The eval freeze-active fraction is at least **0.80** on at least 2 of 3
   seeds. The 475 reference was 1.0, recorded under the UP defect. If this fails, the run is
   PRECONDITION-FAILED and the lock DV has no comparator. MECH-287's lock falsifier then routes
   back to the user (option A or C of the 2026-09-25 decision). It is not falsified.
2. **Lock ratio.** The distribution of `z_harm_a_norm / (theta * gaba_tone)` on frozen eval ticks.
   It sets `alpha` by a rule fixed NOW: `alpha` is the smallest of {1, 2, 4} with
   `1 + alpha >= median lock ratio`. If the median exceeds 5, the path cannot reach the lock at a
   bounded gain. The result is then reported as INERT-BY-MAGNITUDE, and the test does not run.
3. **Reach in regime.** In the `D_BOTH_ON` arm with the path ON at alpha 0 (bit-identical
   behaviour), `_pag_desc_n_drive_steps_while_frozen > 0` in eval on at least 2 of 3 seeds. If it
   is zero, invalidations do not occur while frozen: the path is built but not reached in this
   regime. That is also not a falsification.
4. **Budget re-measure.** Wall-clock per warmup episode on a cloud worker. The old ~20 min/seed
   estimate is void: the 2026-09-25 Mac probe had not finished 20 warmup episodes after 12.5 min,
   and the worker reports warmup more than 10x slower. Size Stage 1 from this number.

**Stage 1: test (only if Stage 0 passes).** The design is 2 x 2 x at least 3 seeds.

- Factor one is the MECH-287 chain: `D_BOTH_ON` (intact) vs `A_BOTH_OFF` (lesioned).
- Factor two is the path: eval-only ON (alpha from Stage 0) vs OFF.
- The path is switched on at eval entry (`gate.config.alpha_descending = alpha` after warmup, with
  alpha 0 in warmup). The two knob levels within a chain arm therefore share a bit-identical
  warmup, which removes confound (a) of the motivating analysis from the path contrast.
- DV: the lock quantities. These are eval freeze-active fraction, lock persistence (the fraction of
  eval episodes ending frozen), and time-to-first-release, right-censored, with the censored
  fraction reported as its own cannot-determine category.

Criteria, all paired by seed:

- **P1 (path reaches the lock).** In `D_BOTH_ON`, ON minus OFF freeze-active fraction is at most
  **-0.15** on at least 2 of 3 seeds.
- **P2 (MECH-287 attribution: the interaction).** The ON-OFF effect in `D_BOTH_ON` exceeds the
  ON-OFF effect in `A_BOTH_OFF` by at least **0.10** on at least 2 of 3 seeds. The cross-chain
  main effect (D vs A with path ON) is reported, but it is NOT load-bearing, because the two chain
  arms' warmups diverge.
- **Readout of record.** P1 PASS with P2 PASS supports "the invalidation chain can release the
  lock through a descending route". P1 PASS with P2 FAIL means the path works but MECH-287's
  broadcast half adds nothing over passive hysteresis. P1 FAIL with Stage 0 met means the path is
  too weak or not reached. In none of these outcomes is the trigger-lesioned arm's silence
  load-bearing: that silence is true by construction (ADDENDUM 2026-09-25).

## 7. Falsifier-runnability trace (/implement-substrate 3h)

- **EVENT:** anchor invalidation (T3 or H) while frozen. Emitted by existing substrate, and this
  build connects it to the PAG. Whether it occurs while frozen is Stage 0 item 3, and it is
  measured, not assumed.
- **DV:** the lock quantities, read per eval step from `pag_freeze_gate.last_output`
  (`freeze_active`, `ticks_in_freeze`, `freeze_release`). They already exist.
- **INSTRUMENT:** the existing per-episode PAG readout plus this build's
  `pag_descending_release_diagnostics()`.
- **Shape at the shipped default:** INERT by design, because the master switch is off. The
  configuration at which the DV can move is: master ON, lineage flags as in V3-EXQ-1097, and alpha
  set by the Stage 0 rule. That configuration is carried into Stage 1 above.

## 8. Next step

1. Queue Stage 0 as a diagnostic via `/queue-experiment`, using the V3-EXQ-1097 helpers, the
   `A_BOTH_OFF` and `D_BOTH_ON` arms, the path ON at alpha 0, and 3 seeds.
2. Only on a Stage 0 PASS, queue Stage 1 and restate EXP-0371 against it.
3. Governance decides whether this path is registered as a claim. It is a candidate MECH:
   hippocampal-invalidation descending release of the PAG freeze. The build is recorded as a
   MECH-279 extension serving MECH-287, and no claim ID is minted here.
