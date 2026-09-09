# V3-EXQ-1003 (EXT-004 / ARC-013 cross-context residue probe) -- REFUSED, not queued

**Session:** wizardly-meninsky-e6c09c (campaign W6-S5b item 2), 2026-09-09T01:54:02Z.
**Chip:** chip-20260903-exq991-redesign-action-level-dv.
**Disposition:** NOT QUEUED. The driver stays UNTRACKED at
`ree-v3/experiments/v3_exq_1003_ext004_residue_cross_context_action_suppression.py`
with a DO-NOT-QUEUE banner, as its 2026-09-04 predecessor draft did
(WORKSPACE_STATE 2026-09-04T20:17:01Z). Reserved id V3-EXQ-1003 is released.
**Governance flag:** evidence_discrepancy on EXT-004 + ARC-013 (see below).

## What was asked, and how far it got

The chip asked for an action-level readout with DEMONSTRATED free-policy range,
the range MEASURED FIRST and the bar derived from it. That was done, and it
succeeded on its own terms:

* The 2026-09-04 draft's DV (`approach_rate`, up-gradient EXECUTED moves per
  decision point) was re-confirmed FLOORED at 0.004-0.033 by a direction-locked
  policy (5 cells, seeds 42/43/45, fresh and post-Context-A).
* A PRE-COMMIT readout was measured instead: `p_approach` = softmax(-scores/T_eff)
  mass on approach candidates over approach+retreat candidates, read only on
  fresh E3 selections at decision points holding both directions. Free-policy
  range OBSERVED: per-cell means 0.10-0.40, within-cell SD 0.26-0.41, per-tick
  min 0.000-0.035 and max 0.945-0.999, 158/239 scored ticks strictly inside
  (0.05, 0.95), score range never zero. NOT degenerate.
* The driver was rebuilt on that DV (bars derived from the measured SD and room),
  migrated onto the shared `experiments/_lib/fresh_select.py` sentinel-key
  freshness helper, and passes `validate_experiments --strict` with 0 warnings,
  `validate_recording --strict` complete, and an end-to-end `--dry-run`.

The Step 4.5 red-team (fable, claude-fable-5-1) then returned **BLOCKING**, and
its three load-bearing findings were independently re-measured by this session
with the driver's own functions before being acted on. They are not threshold
problems, and they are not repairable by re-posing the bar.

## The three confirmed findings

Two independent measurements, at two Context-A scales, both seed 42, both using
the driver's own `_build_agent` / `_step_episode` / `_context_b_phase` /
`_detach_agent_buffers` / `_zero_residue_field` / `ScoreReadoutRecorder`:
the red-team's (FULL 20x80 Context A, 160-step Context-B twins) and this
session's confirmation (5x40 Context A, 40-step Context-B twins).

### F1 -- the "paired twin" was never RNG-paired; the artifact alone exceeds the bar

`run_seed` seeds torch/numpy only before each arm's CONTEXT A
(lines 1185-1186 EXPOSED, 1304-1305 NAIVE), and `_ArmCell.__enter__` resets all
RNG at each arm's entry. So EXPOSED's Context B begins 1600 Context-A steps into
the stream while the ERASED twin's begins at the fresh seed state. CEM proposal
noise and E3's uncommitted multinomial branch (`e3_selector.py:4249`) draw from
that global stream, and no agent-held generator isolates them.

| measurement | ERASED - EXPOSED, no true manipulation difference | C1 bar |
|---|---|---|
| red-team, 160-step twins, full Context A | 0.097 (and sham twins +0.134 / -0.108) | 0.10 |
| this session, 40-step twins | **-0.126** | 0.10 |

Pairing sanity, this session: with the RNG state restored before each run, the
UN-erased clone reproduces EXPOSED to -0.0013 (identical scored-tick counts,
identical candidate share). So the pairing fix works and the divergence above is
purely stream position.

### F2 -- under exact pairing, erasing the whole residue field does not move the DV

With the RNG state restored so the twins are genuinely paired, erasing the
ENTIRE Context-A residue field changes `p_approach` by:

| measurement | paired ERASED - EXPOSED | C1 bar | shortfall |
|---|---|---|---|
| red-team, full 20x80 Context A | 0.00013 (0.56411 vs 0.56398) | 0.10 | ~770x |
| this session, 5x40 Context A | **-0.00103** | 0.10 | ~97x |

Both are the WRONG SIGN for the hypothesis (C1 registers ERASED > EXPOSED). The
residue score term's own approach-minus-retreat mean was measured NEGATIVE in
both probes (-0.189 red-team at full scale; -0.021 this session), i.e. the
residue channel, where it acts at all, mildly FAVOURS approach candidates.

Mechanism, at source: `score_trajectory` applies `rho_residue * phi`
(`e3_selector.py:1474,1507`) with `phi` a sum of 32 Gaussians at
`kernel_bandwidth = 1.0` -- a value `config.py:3086` itself documents as "~15x
too wide for the z_world residual scale". The red-team measured all 32
Context-A centers inside a ball of pairwise diameter 0.081: one broad bump, not
a map, so it barely differentiates candidates that differ in their first move.

### F3 -- the cross-context construct is absent at measurement time

`RBFLayer.add_residue` (`residue/field.py:165-180`) is a 32-slot ROUND ROBIN
that MOVES a center to the new harm location (`centers.data[idx] = location`)
while accumulating its weight. Context B is hazard-live
(`CONTEXT_B_ENV_KWARGS`), and residue is written twice per committed harm step
(`agent.py:10747`, `e3_selector.py:4425`).

| measurement | Context-B steps | Context-A centers surviving |
|---|---|---|
| red-team | 80 | 0 of 32 |
| this session | **40** | **0 of 32** (num_harm_events 310) |

The design scores 1600 Context-B steps per cell. Long before the first cell
finishes, the field holds Context-B geography with Context-A weight MASS. The
arm contrast is therefore a sensitisation-gain contrast on Context-B locations,
not the transfer of Context-A structure that EXT-004 and ARC-013 name.

Four further CONTESTED findings (F4 p_approach tracks candidate composition on a
manipulation-selected tick subset; F5 the split branch fires on an unqualified
C2 mean; F6 precondition P5 is vacuous, H1's perturbation is 25-10,000x the
manipulation's size, and H2 files a REVERSED effect as "not ready"; F7 the SE
derivation ignores regime-locking) are recorded in the red-team artifact and are
not what the refusal rests on.

## Why this is a refusal rather than a fix

F1 alone is a few lines (restore the RNG state before each arm's Context B), and
it would have been fixed and queued. But fixing F1 is what EXPOSES F2: the
honest paired effect of the entire manipulation on this DV is ~1e-3 against a
0.10 bar, in the wrong direction. Lowering the bar does not repair it -- at
1e-3 the between-arm difference is dominated by clone/float noise, which is the
same construct-validity failure class as the predecessor's, one layer further in.
F3 says that even a working readout would not be measuring cross-context
transfer. No pre-registered criterion of this design can discriminate.

## What this does and does not say about the claims

It does NOT weaken EXT-004 or ARC-013. Nothing here is a claim verdict: no
scored run was performed, and the correct reading is that the INSTRUMENT and the
CONSTRUCT are unavailable in this configuration, not that residue fails to carry
behaviour.

It DOES change the evidence picture in two ways a governance cycle should see:

1. **V3-EXQ-991's weak null needs re-scoping.** Its `harm_rate_B` was adjudicated
   `non_contributory` on construct-validity grounds and carried forward as a
   "weak, underpowered null" prior. F3 shows the cross-context construct is
   dissolved within tens of hazard-live Context-B steps on this substrate, so
   the 991 lineage's Context-B design -- not only its DV -- was never measuring
   transfer. The prior should be recorded as construct-unavailable, not weak.
2. **A residue-transfer probe needs substrate work first.** Two named,
   independently checkable items: (a) the readout must be taken with the field
   FROZEN at its Context-A state (a harm-neutralised Context B, i.e. the driver's
   own NAIVE kwargs, or a write-gated residue field), or the construct is gone
   before scoring; (b) at `kernel_bandwidth = 1.0` the RBF field does not
   differentiate candidate first-moves, which is the `sd_067_safety_terrain_bandwidth`
   question arriving from a second direction.

## What a valid successor would need (not designed here)

* RNG-paired arms (restore the stream state before every arm's read phase), with
  an un-erased clone as a pairing sanity arm asserted to reproduce EXPOSED.
* A frozen-field read phase, so what is scored is Context-A structure.
* A residue channel demonstrated, BEFORE the run, to move the readout by at
  least the registered bar under the real manipulation -- not under a synthetic
  score perturbation of the softmax's whole range (F6/H1).
* A pre-registered reversed-effect label, since the measured sign is negative.

## Reproduction

Both probes import the driver's own helpers. This session's confirmation script
is inlined below; it prints the three deltas and the surviving-center count.

```
seed 42; Context A = 5 x 40 steps (EXPOSED kwargs); Context B = 40 steps
1. build agent, run Context A, snapshot rbf_field.centers
2. _detach_agent_buffers -> deepcopy three clones (unerased, erased, erased_u)
3. S = (torch.get_rng_state(), np.random.get_state(), random.getstate())
4. EXPOSED Context B; restore S; unerased clone Context B; restore S; erased clone Context B
5. reseed to the bare seed; erased_u Context B   <- what the shipped driver does
6. compare p_approach; compare centers against the step-1 snapshot
```

Measured: pairing sanity -0.0013; paired erase effect -0.00103; unpaired
as-shipped -0.126; centers surviving 0/32; num_harm_events 310.
