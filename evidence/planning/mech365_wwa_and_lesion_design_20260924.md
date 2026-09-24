# MECH-365 phase-1 draft: what_would_answer + lesion falsifier design

Drafted 2026-09-24T08:09:53Z by a subagent of /governance session `governance-20260924`.
DRAFT ONLY. Nothing shared has been written: no claims.yaml, experiment_queue.json or ree-v3 edits.
Substrate state read at ree-v3 `44ddbfd` (origin/main).

---

## 0. Premise audit: brief vs current tree

Each premise in the brief was re-measured against the tree. Three need correcting before any
design builds on them.

1. **"The gate exists as a MODE BIT, not an explicit label field."** Only partly true. There are
   two kinds of gate. (a) Per-call mode arguments: `is_waking` on
   `HippocampalModule.update_familiarity` / `record_visitation` (module.py:1942-1990), and the
   `hypothesis_tag` argument on the ResidueField writers (field.py `accumulate`,
   `accumulate_benefit`, `accumulate_safety`, `update_valence`:847). (b) Labels that are **carried
   on the representation object itself**: `LatentState.hypothesis_tag` (latent/stack.py:765) and
   `Trajectory.hypothesis_tag` + `Trajectory.metadata` (predictors/e2_fast.py:63-70). Kind (b) is
   the V3 form of MECH-365's `committed_vs_imagined`. MECH-545's 2026-09-15 currency note is right
   that the literal string `committed_vs_imagined` has 0 hits; the field is named `hypothesis_tag`.

2. **"Force-dropping committed_vs_imagined at the replay -> consolidation boundary is a small
   edit" (MECH-545 notes).** No such boundary currently exists for imagined content, so there is
   nothing to drop the label at. What the tree actually does:
   - Waking `REEAgent._do_replay` (agent.py:10968) generates replay trajectories and **discards
     them**. `replay_trajs` is assigned and never used.
   - The REM pass `REEAgent.run_rem_attribution_pass` (agent.py:13184) is the one V3
     replay -> consolidation boundary. Its FORWARD replay (`hippocampal.replay()`, an E2 rollout
     of random actions from the latest `theta_buffer` z_world, i.e. imagined content) is only
     **scored**, read-only. Its REVERSE replay (`reverse_replay()` of real recorded MECH-165
     episodes) is the only content that reaches a consolidation writer:
     `HippocampalModule.spread_reverse_replay_wanting` (module.py:3668, MECH-217), which calls
     `ResidueField.update_valence(..., hypothesis_tag=trajectory.hypothesis_tag)` (module.py:3738).
   - So imagined content is kept out of committed history today by **routing exclusion**: it is
     never presented to a writer. It is not a label gate. MECH-365 asserts something different:
     imagined content that IS presented and usable is refused committed status because of its
     label.

3. **Latent defect: the label is not set on replay output.** `HippocampalModule.replay()`
   (module.py:2975) says in its docstring "All content carries hypothesis_tag=True", and its
   Returns line says "(all hypothesis_tag=True on caller side)". The code builds each trajectory
   with `e2.rollout_with_world`, which leaves the dataclass default
   `Trajectory.hypothesis_tag = False`. No caller sets it either. `diverse_replay()`'s
   forward/random steps delegate to `replay()` (module.py:3245) and inherit the same defect.
   The defect is harmless today only because of point 2. If forward replay were routed to the
   MECH-217 writer, the writer would accept it as real experience. That is the MECH-365 failure,
   latent in the shipped substrate.

4. **One-way-ness has a latent violation elsewhere (MECH-290).** This affects the claim, not just
   the design. There is exactly one site in ree_core that turns a tagged trajectory into an
   untagged one: `HippocampalModule.record_committed_trajectory` (module.py:3534), which sets
   `hypothesis_tag=False, metadata=None` and says "the executed trajectory IS real". It is called
   at **commit ENTRY** (agent.py:10235 and 10296), before execution, and it stores the E3 committed
   PROPOSAL's `world_states`. Those are E2's **predicted** states, not observed ones.
   `backward_credit_sweep` (module.py:3574) then writes VALENCE_WANTING along those predicted
   states. With `use_mech293_ghost_probes`, a committed proposal can be a ghost probe whose
   `world_states` begin at a REMOTE bank anchor's z_world (module.py:2890-2905), not the agent's
   position. Imagined states then acquire committed wanting credit. Both flags default OFF
   (config.py:3150, 3186), so production is clean, but under those flags the as-built gate is not
   one-way. This is a substrate non-conformance with MECH-365, not a refutation of it; see
   section 5.

---

## 1. Drafted `what_would_answer` (house style, for merge into MECH-365)

```yaml
  what_would_answer: |
    SCOPE: the V3 half after the 2026-09-24 split. V3's committed_vs_imagined label is
    hypothesis_tag, carried on the representation object (Trajectory.hypothesis_tag /
    .metadata, LatentState.hypothesis_tag), not only passed as a per-call mode argument. The V3
    analogue of "committed history" is the ResidueField valence/residue terrain that later reads
    as experienced value. The full event-token schema on the ARC-085 store is MECH-365a (v4) and
    is not tested here. The safety property itself (simulation content must not accumulate as
    experience) is owned by MECH-094 / INV-011 / MECH-037, and their audits stand. This claim adds
    three testable specifics: (i) the label TRAVELS on the imagined representation to the
    consolidation boundary; (ii) the gate is SELECTIVE, blocking committed-status writes while
    imagined content is still presented and read (a gate, not a discard); (iii) it is ONE-WAY,
    stripping the label only on REALIZATION (observed states), never on commitment of predicted
    states.
    BIOLOGY: reality monitoring / source monitoring. Confabulation after ventromedial-orbitofrontal
    and basal-forebrain damage is a failure to filter currently-irrelevant or internally generated
    memory traces from what is taken as present reality (Schnider 2003 reality/temporal-context
    filtering, cited under MECH-094; Papez-loop provenance gating, MECH-037, Theze 2017). Source
    is multidimensional (Johnson, Hashtroudi & Lindsay 1993, cited under MECH-430). This claim
    tests only the single reality-status bit; per-dimension provenance is MECH-430.
    NON-DEGENERACY PRECONDITION: (P1) a real replay -> consolidation writer must be LIVE in the
    unlesioned arm: the MECH-217 REM wanting-spread (use_offline_wanting_spread, rem_enabled,
    sleep cycles firing) must make non-zero accepted writes from reverse (real) replay, as it did
    in V3-EXQ-842. (P2) Imagined content must actually be generated AND presented to that same
    writer. Today it is not (REM forward replay is scored read-only; waking _do_replay discards
    its output), so a routing flag is required, and without it every lesion is vacuous by
    construction. (P3) The imagined trajectories presented must carry non-zero source wanting at
    their start state (world_states[0]); otherwise spread_reverse_replay_wanting returns before
    reaching the gate and "no contamination" means "no write attempted". (P4) The contamination
    DV must have demonstrated range: a CANARY arm with the label suppressed at SOURCE must show
    imagined-sourced accepted writes > 0, or the instrument cannot detect a gate failure. (P5)
    The valence clamp must not be saturated (fraction of active centers at clamp_abs < 0.5 in the
    intact arm), or contamination is absorbed and under-read.
    CONFIRMING (all, >= 3 seeds, every seed): (C1) with the gate intact and imagined replay routed
    to the writer, imagined-sourced accepted write mass == 0 and the end-of-run VALENCE_WANTING
    map matches the unrouted reference arm to within 1e-6 relative L1. (C2) Dropping the label at
    the consolidation boundary (the sender's Trajectory keeps its label; only the translation into
    update_valence drops it) makes imagined-sourced mass > 0 and a relative-L1 wanting-map
    divergence from the intact arm D > theta, theta = max(3 * SD_seeds(D_sham), 0.05). (C3) A sham
    lesion that runs the same override code path on real (already-untagged) trajectories gives
    D_sham <= 0.01. (C4) SELECTIVITY: in the intact arm the imagined replay is still generated and
    read. Forward-replay scored count > 0 and equal to the reference arm, mean forward terrain score
    equal to within 1e-6, and forward trajectories reach the writer and are refused there (refused
    waypoint count > 0), not dropped upstream.
    ONE-WAY LEG (audit, separate from the lesion): re-derive from the CURRENT tree at run time every
    site that yields an untagged Trajectory / LatentState from a tagged source. CONFIRMING only if
    every such site strips on realization, i.e. it stores OBSERVED z_world, not a proposal's predicted
    states.
    FALSIFYING (any one): (F1) the label does not travel. The intact-gate arm accepts
    imagined-sourced writes (C1 fails with the P4 canary valid): the gate is not one-way at the
    only V3 consolidation boundary. (F2) The gate is not selective: making the label honoured also
    suppresses the read/scoring path (C4 fails), so the mechanism is a blackout, not a
    status gate, and the "usable for planning" leg fails. (F3) The label is not load-bearing:
    with P1-P5 met, the boundary lesion produces D <= theta in a majority of seeds. Imagined
    content then reaches committed history in no material amount, and the provenance label has no
    keep at this boundary. A sham with D_sham > 0.01 invalidates the run: instrument
    nondeterminism, no verdict.
    SUBSTRATE (verified 2026-09-24 at ree-v3 44ddbfd): ree_core/predictors/e2_fast.py Trajectory
    (hypothesis_tag default False, metadata); ree_core/latent/stack.py LatentState.hypothesis_tag;
    ree_core/hippocampal/module.py replay() (2975; DEFECT: output is not tagged despite its
    docstring), diverse_replay() (3193, forward/random steps delegate to replay()),
    reverse_replay() (3110), spread_reverse_replay_wanting() (3668; the sole ree_core reader of
    Trajectory.hypothesis_tag, at 3738), record_committed_trajectory() (3534; the sole
    tagged->untagged site), backward_credit_sweep() (3574); ree_core/residue/field.py
    update_valence() (847, the hypothesis_tag refusal); ree_core/agent.py _do_replay() (10968,
    output discarded), run_rem_attribution_pass() (13184, forward replay scored read-only, reverse
    replay spread). Harness precedent: experiments/v3_exq_842_mech217_offline_wanting_spread_readiness.py
    (PASS 2026-07-30, MECH-217 writer demonstrably live).
    CAVEATS, stated plainly: (a) The lesion leg is AUDIT-STRENGTH, like INV-011's. Once the label
    is stamped and honoured, C1 and C3 are structurally determined, and C2 is near-guaranteed
    given P3. The informative content is F1 (does the label travel: on the as-built tree it does
    NOT for replay() output), F2 (selectivity), and the MAGNITUDE of D (does the gate matter).
    It is not behavioural evidence that contamination changes later action. A behavioural follow-up
    (post-sleep wanting-gradient approach to imagined-only content) is owed before any promotion
    beyond candidate. (b) The one-way leg is currently VIOLATED latently at MECH-290
    (record_committed_trajectory strips the tag at commit entry on predicted world_states; with
    ghost probes those states start at a remote anchor). Both flags default OFF. This routes to
    substrate as a non-conformance (store observed states during execution, or keep the tag until
    realization); it does not refute the claim. (c) Evidence from this falsifier tags MECH-365
    only. It is NOT a MECH-545 contract-lesion result (no five-way dissociation, no
    random-projection floor, no acute/adapted separation) and NOT MECH-271 evidence (one
    destination, no differential routing).
    Disposition (draft): testable in V3 now for the carried-label + selectivity + boundary-lesion
    legs after a small, default-OFF substrate edit (label stamp + routing flag + lesion flag) --
    complicated (buildable). The one-way leg has a known latent non-conformance at MECH-290 --
    complicated (buildable).
```

---

## 2. Lesion-experiment design sketch

**Working title:** `v3_exq_NNNN_mech365_provenance_gate_boundary_lesion` (proposed id in section 4).
**experiment_purpose:** `evidence`, claim_ids `["MECH-365"]` only. See caveat (a): record it as
audit-strength in the manifest interpretation. Pure `diagnostic` is also defensible. The parent
decides at /queue-experiment.

### 2.1 Harness (derived from V3-EXQ-842, which already proved the writer live)

- CausalGridWorldV2, fixed agent/resource layout via `env.reset_to`, **scripted** greedy walk to
  the resource. The waking path is identical across arms, so the RBF center set is identical
  across arms at a matched seed. That makes a per-center paired comparison valid.
- Terminus VALENCE_WANTING seeded directly on cycle 1 (`CONTACT_SEED_WANTING = 2.0`,
  `hypothesis_tag=False`); tonic_5ht off, so MECH-203 never writes.
- Near-zero RBF centers activated at every visited waypoint; `residue.num_basis_functions = 256`.
- `use_sleep_loop`/`sws_enabled`/`rem_enabled` ON; `use_offline_wanting_spread=True` at the landed
  gamma 0.9 / gain 0.1; `rem_attribution_steps = 10` (5 forward + 5 reverse per REM pass).
- `N_CYCLES = 6` wake -> `run_sleep_cycle()` -> `agent.reset()`. Order matters: sleep runs BEFORE
  reset so `theta_buffer.recent[-1]` is the contact terminus. REM forward replay therefore starts at
  a state with positive wanting (P3).
- Seeds: 5 (42-46). The minimum is 3. The run is cheap: 842 ran 3 seeds x 2 arms at this scale.

### 2.2 Arms (5; same seeds; RNG consumption identical across arms because the spread consumes none)

| Arm | forward replay routed to MECH-217 writer | replay() label stamped | boundary lesion | role |
|---|---|---|---|---|
| R0_unrouted | no (as shipped) | yes | off | reference committed-history map |
| A1_gate_intact | yes | yes | off | the claim's gate |
| A2_boundary_lesion | yes | yes | `drop_at_consolidation` | lesion: sender keeps the label, translation drops it |
| A3_sham | yes | yes | `sham_real_only` | matched negative control: same override path applied to real (already-untagged) reverse trajectories, so it changes nothing |
| A4_canary_source_unlabelled | yes | **no** (as-built defect reproduced) | off | P4 positive control: the instrument must detect a label failure |

A2 and A4 are predicted to give the same signature. That is instrument validation, not a
dissociation claim.

### 2.3 DVs (per seed, per arm)

- **M_img** (primary, gate-side): summed |spread| of ACCEPTED writes whose source trajectory is
  imagined (forward replay, identified by `metadata.source` or by routing branch). Also
  n_steps_refused_provenance and n_steps_accepted per source.
- **D** (primary, committed-history-side): relative L1 divergence of the end-of-run
  VALENCE_WANTING vector over the (identical) active-center set, `||W_arm - W_A1||_1 / ||W_A1||_1`.
- Read-path (selectivity): number of forward trajectories scored, and their mean and variance of
  terrain score (`_score_trajectory`) across the run.
- Descriptive only: 842's near/far/control-point wanting and near/far ratio (does contamination
  distort the MECH-217 gradient?), and the fraction of centers at clamp_abs (P5).

### 2.4 Preconditions (a failure gives `substrate_not_ready_requeue`, never a verdict)

- P1: reverse-sourced accepted spread writes > 0 in R0 and A1 (the writer is live).
- P2: forward trajectories presented to the writer >= 1 per REM pass in A1-A4 (routing is live).
- P3: >= 3 forward trajectories per seed with start-state wanting > 0 (the gate is actually reached).
- P4: M_img(A4) > 0 in every seed (the canary detects a source-side label failure).
- P5: fraction of active centers at clamp_abs in A1 < 0.5.

### 2.5 Pre-registered criteria

- **C1 (load-bearing):** every seed has M_img(A1) == 0 and D(R0 vs A1) <= 1e-6.
- **C2 (load-bearing):** every seed has M_img(A2) > 0 and D(A2) > theta, with
  theta = max(3 * SD_seeds(D(A3)), 0.05). The 5% absolute floor dominates when the sham SD is 0,
  which it is expected to be.
- **C3 (load-bearing control):** every seed has D(A3) <= 0.01.
- **C4 (load-bearing, selectivity):** forward-scored count A1 == R0 > 0; |mean forward score A1 -
  R0| <= 1e-6; n_steps_refused_provenance(A1) > 0.
- **PASS** = P1-P5 AND C1-C4. **FAIL** mapping: C1 fails (with P4 valid) -> F1; C4 fails -> F2;
  C2 fails in a majority of seeds with P1-P5 met -> F3. **Instrument invalid (no verdict):** C3
  fails, or P4 fails.

### 2.6 Exact code edits (none exist yet: grep for `mech365` / `drop_provenance` /
`force_tag` / `provenance_lesion` over ree_core returned 0 hits)

All three edits live in `ree_core/utils/config.py` `HippocampalConfig` (class at line 2608, next to
`use_offline_wanting_spread` at 3218). Each needs the known **three sites**: the dataclass field,
the `REEConfig.from_dims` kwarg, and the assignment (`from_dims` silently swallows unknown kwargs).

- **E1: label stamp (fixes the docstring/code mismatch; default = fixed).**
  `HippocampalModule.replay()` (module.py:2975): after each `rollout_with_world`, set
  `traj.hypothesis_tag = True` unless
  `config.mech365_suppress_replay_provenance_stamp` (**new flag, default False**, set True only in
  A4). Production is bit-identical because the only ree_core reader of `Trajectory.hypothesis_tag`
  is module.py:3738, which today receives only `reverse_replay()` output (a fresh Trajectory, tag
  False). Do NOT stamp `metadata` in replay(): `metadata` is read on CEM candidates (agent.py:7161,
  7617, 8926; module.py:1213). Identify the forward source by routing branch in agent.py instead.
- **E2: routing (default OFF).** `rem_route_forward_replay_to_consolidation: bool = False`.
  In `REEAgent.run_rem_attribution_pass()`, forward loop (agent.py ~13251): when the flag and
  `use_offline_wanting_spread` are both True, also call
  `self.hippocampal.spread_reverse_replay_wanting(traj)` on each forward trajectory, and
  accumulate separate metrics `rem_fwd_spread_n_accepted`, `rem_fwd_spread_n_refused`,
  `rem_fwd_spread_accepted_mass`. Leave the no-buffer `extra` forward branch unrouted and document
  that choice.
- **E3: lesion (default "off").** `mech365_provenance_lesion: str = "off"`, one of
  `{"off", "drop_at_consolidation", "sham_real_only"}`. In
  `HippocampalModule.spread_reverse_replay_wanting()` (module.py:3668-3740), compute
  `eff_tag = trajectory.hypothesis_tag`. For `drop_at_consolidation` with eff_tag True, set
  eff_tag = False and count `n_lesion_overrides`. For `sham_real_only` with eff_tag False, run the
  identical assignment on a real trajectory (a no-op) and count `n_sham_overrides`. Pass `eff_tag`
  to `update_valence`. **Never mutate the Trajectory object**: the sender keeps its label, so this
  is a boundary lesion, not a source lesion. Add return keys `n_steps_accepted`,
  `n_steps_refused_provenance` (a waypoint with eff_tag True is counted and not written) and
  `accepted_mass`. Existing keys stay unchanged.
- Contract tests: replay() outputs are tagged True (False only under the suppress flag);
  reverse_replay() outputs are False; with all three flags at default, the REM metrics and the
  wanting map are bit-identical to pre-edit on a fixed-seed smoke; under `drop_at_consolidation`
  the Trajectory object's tag is unchanged after the call.
- Route: E1-E3 is a small, default-OFF, single-session ree_core change. Land it on main with
  contract tests, and run `scripts/remote_pytest.sh` before queuing. It must not reuse MECH-271's
  planned names (`use_mech271_routing`, `force_tag_loss_rate`).

### 2.7 How this stays inside MECH-365 and does not become MECH-545's assay

- **One relation, one boundary, one predicted signature.** Only reality-status is lesioned, only
  at the REM replay -> MECH-217 consolidation writer. The predicted signature is imagined-sourced
  committed wanting. No identity, temporal, agency or confidence lesion. No claim that the
  signature is distinct from the other four. No random-projection floor. No acute vs adapted
  (ARC-140) phase separation. No contract-admissibility verdict under GOV-CONTRACT-1.
- claim_ids = `["MECH-365"]`. MECH-545 is not tagged, and nothing here counts toward its five-way
  dissociation. MECH-545's "DO NOT build / DO NOT queue" covers its own assay and is not engaged.
  If MECH-545 is ever routed, it may cite this as the reality-status single-lesion cousin, in the
  STRONG form its 2026-09-15 currency note asked for: a status carried on the Trajectory across the
  boundary and dropped by the translation, not merely a forced-open write gate.
- It is not MECH-271's four-arm routing test either. There is one destination and no
  anchored-vs-probe differential routing, so MECH-271 is not tagged.

---

## 3. Runnability self-check

| Criterion | Can pass? | Can fail? | Vacuity risk / note |
|---|---|---|---|
| P1 writer live | yes (842 PASS, near wanting 17.0 ON vs 1.0 OFF) | yes, if the sleep loop or buffer does not fire | low |
| P2 routing live | yes after E2 | yes, if E2 is not landed or the flag is off | **vacuous without E2**: on the current tree imagined content never reaches a writer |
| P3 source wanting > 0 | likely: forward replay starts at `theta_buffer.recent[-1]` = seeded terminus | yes, if wanting decays below 0 or cycle 1 has an empty theta buffer | must be measured, not assumed |
| P4 canary | yes: A4 reproduces the as-built defect | yes | this is what makes a C1 pass mean something |
| C1 gate holds | yes after E1 | **yes**: fails on the as-built tree (A4 shows that), and would also fail if any stamp is missed | structurally determined once E1 lands (caveat a) |
| C2 lesion contaminates | yes | yes, if forward writes land on clamped centers or mass < 5% | near-guaranteed given P3; the magnitude is the information |
| C3 sham inert | yes | only via hidden nondeterminism | inert by construction; it guards the instrument, not the claim |
| C4 selectivity | yes | yes, if the gate were implemented as a routing blackout | the only criterion that separates "gate" from "discard" |

Things that would make the run vacuous: E2 not landed (no imagined content at the writer); P3 not
met (the spread returns before the gate); a saturated clamp; reading `Trajectory.hypothesis_tag` of
the source instead of what `update_valence` received; mutating the Trajectory in the lesion (that
turns it into a source lesion identical to A4).

**Verdict:** runnable in V3 after a small, default-OFF substrate edit (E1-E3). It is not runnable
on the current tree: every criterion would be vacuous because no imagined content reaches a
consolidation writer. The informative outcomes are F1, F2 and the D magnitude. C1 and C3 are
audit-strength.

---

## 4. Next EXQ id (not reserved, not queued)

- experiment_queue.json max = V3-EXQ-1067 (1 item queued).
- origin/main git log, last 30: max = V3-EXQ-1082.
- The working tree has **untracked** `experiments/v3_exq_1083_sd081_adaptive_vs_fixed_allocation.py`
  and `v3_exq_1084_sdppb9_harm_pe_source_probe.py`. Those are live claims by other sessions.
- **Proposed: V3-EXQ-1085.** Re-check the max at write time; ids are being consumed fast today.

---

## 5. Findings for the parent session (not actioned here)

1. **Latent MECH-365 defect in shipped code:** `HippocampalModule.replay()` output is not tagged,
   contrary to its docstring. It is harmless only because of routing exclusion. E1 fixes it.
2. **Latent one-way violation at MECH-290:** `record_committed_trajectory` strips the tag at commit
   ENTRY on the proposal's PREDICTED world_states. `backward_credit_sweep` then credits wanting
   along imagined states. With `use_mech293_ghost_probes`, those states start at a remote anchor.
   Both flags default OFF. This is a candidate /implement-substrate follow-on (record observed
   z_world during execution), probably with a governance_flag against MECH-290/MECH-293
   (`implementation_gap`). Out of scope for this falsifier.
3. The brief's framing "the V3 gate is a mode bit" should be corrected wherever it is recorded:
   V3 carries the label on the object (`Trajectory`/`LatentState.hypothesis_tag`). MECH-545's notes
   line "MECH-365 gate exists; force-dropping ... is a small edit" is only true after the routing
   edit E2, because the boundary it names carries no imagined content today.
