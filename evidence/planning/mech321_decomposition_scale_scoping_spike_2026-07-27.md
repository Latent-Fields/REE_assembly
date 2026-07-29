# MECH-321 scoping spike -- is "decomposition depth" the right control parameter?

**Date:** 2026-07-27
**Session:** `vigilant-bell-13230c`
**Owns:** the design question flagged-but-not-settled in MECH-321's `evidence_quality_note`
(2026-07-27 provenance correction, REE_assembly `6833a97d20`), final paragraph.
**Debt class:** `complex (probe-gated)` on entry; resolved to `puzzle (known rules)` on the
heterogeneity half (a specific missing fact, obtainable by a named instrument) and to
`complicated (buildable)` on the depth half.

**Changes no claim status, confidence, live_status or v3_pending.** Recommendation only.

**STATUS 2026-07-29 -- both halves CLOSED.** The heterogeneity half's named probe ran as
**V3-EXQ-830** and returned `slow_never_fires_on_rollout` (row 2 of the 5b decision table):
answer **(a)** stands, the design question is closed, and the 5c extension sketch is
**retired**. No follow-on experiment was queued -- see the resolution note in section 5b for
why the mid-execution re-run was specifically declined (`midexec_dilution_frac = 0.0`).

---

## Verdict in one paragraph

The question splits into two, and the halves get different answers. **The depth parameter is
answer (a), on a much firmer footing than "engineering choice":** `decomposition_depth_cap` is
not a free scalar over an abstraction axis at all -- it is a *derived mirror* of ARC-071's
`chunk_max_depth`, and at the configuration every MECH-321 run has actually used it is a
**binary switch**, not a depth. Badre & Nee's dissolution of the unidimensional gradient does
not touch the construct it indexes, because that construct is a learned compositional
hierarchy, not an abstraction gradient. **The heterogeneity half is answer (c), for a concrete
and fixable reason:** REE already has the "small set of operators at distinct scales" that
Koechlin's cascade would motivate -- MECH-288 ships two qualitatively different detectors on
two latent streams at two timescales -- but MECH-321 consumes exactly **one** of them, and
collapses even that to a boolean. There is therefore no data on scale-differentiation to
decide from. The probe that decides it is named in §5, it is cheap, and it is the first
increment of (b) if it comes back positive.

---

## 1. What `depth_cap` actually indexes in the built substrate

The spike's premise -- "a scalar recursion depth may be a parameter on a construct that does
not exist" -- is half right, and the wrong half is the one that matters. Reading the code
rather than the title:

| Site | Fact |
|---|---|
| [`policy_chunking.py:1215`](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/policy/policy_chunking.py) | `_depth_for(seq) = 1 + deepest chunk it contains` |
| [`policy_chunking.py:412`](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/policy/policy_chunking.py) | ARC-071 `max_depth: int = 3` -- chunks **cannot be minted** above this |
| [`module.py:883`](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/hippocampal/module.py) | MECH-321's `depth` is read straight off `traj.metadata["chunk_depth"]` |
| [`policy_decomposition.py:427`](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/policy/policy_decomposition.py) | `if depth >= depth_cap: mark unreliable` |

So MECH-321's `depth` is *not* a recursion counter it increments itself. It is the ARC-071
composition depth of the chunk handed to it, and it is bounded above by ARC-071's ceiling as a
hard structural fact. Three consequences the current framing obscures:

1. **`decomposition_depth_cap >= chunk_max_depth + 1` is inert.** No chunk can ever reach
   depth 4, so the mark-unreliable-by-cap branch is unreachable, and `_recursive_leaf_tiles`'s
   `iterations < depth_cap` bound stops binding. Setting it to 4, or to 100, is the same run.
2. **`decomposition_depth_cap = 1` disables decomposition entirely** (every chunk has depth
   >= 1, so every triggering chunk is dropped rather than re-tiled). MECH-321 degenerates to a
   pure withholding mechanism.
3. **The two knobs are independent `REEConfig` fields with no coupling enforced anywhere**
   (`config.py:3622` and `config.py:3682`, both defaulting to 3). Nothing warns on an inert
   or a degenerate setting.

### 1a. In the campaign's actual configuration it is a binary switch

Every MECH-321 run to date seeds one chunk, `seeded_chunk_sequence: [0, 1, 2]`, minted via the
replay path, which mints at `depth=1` unconditionally (`policy_chunking.py:741`). No
chunk-of-chunks has ever formed in a MECH-321 run. At depth 1:

- `depth >= depth_cap` is false for any `depth_cap >= 2`;
- `decompose_sequence` skips the library phase at `depth <= 1` and tiles into raw depth-0
  actions;
- `_recursive_leaf_tiles` sees only depth-0 leaves and exits after one iteration.

**So `decomposition_depth_cap` ∈ {2, 3, 4, ...} are all byte-identical runs, and only 1
differs.** The default of 3 has never once behaved differently from 2 or from 100. The
"3-or-4" question that the provenance correction withdrew a citation for is, at the
configuration under which the parameter has ever run, not a question.

That is the strongest thing this spike found, and it is worth stating plainly: **the
literature argument was conducted over a parameter that has no observed degrees of freedom.**

---

## 2. Why Badre & Nee does not reach this parameter

Badre & Nee 2018 dissolves a *unidimensional abstraction gradient* -- an ordered axis whose
positions are qualitatively ranked by abstractness. The correction is right that a "cap at N"
needs such an axis to count along, and right that the citation was an over-read.

But the thing `depth_cap` counts is not that axis. It is the stratification of the ARC-071
ChunkLibrary: levels built by **repeated grounding**, content-specific, learned at runtime,
each level defined by which shorter chunks happen to tile it. That is a compositional
hierarchy, not an abstraction gradient. Nothing in Badre & Nee argues against compositional
hierarchies -- the paper's replacement model is *more* structured, not less, and it retains
"local and global hierarchical structure" explicitly.

So the provenance correction was correct to withdraw the citation and correct not to conclude
the cap is wrong. What it could not see without reading the substrate is that the cap was
never a parameter on the dissolved construct in the first place. **The citation was not merely
over-strong; it was describing a different object than the one it was attached to.**

---

## 3. Where the heterogeneity point does land -- and it lands hard

Koechlin's levels are heterogeneous in *what conditions the selection*: stimulus -> perceptual
context -> temporal episode. The right REE analog of that heterogeneity is not the depth of the
tiling. It is the **trigger**. And REE already has it, one layer down:

MECH-288 `EventSegmenter` ships a **two-scale, qualitatively heterogeneous** detector
(`config.py:1431`, `event_segmenter.py` module docstring):

| Scale | Algorithm | Streams | Timescale |
|---|---|---|---|
| `fast` | PE-threshold on sliding-window z-score | `z_world`, `z_self` | per-tick |
| `slow` | BOCPD-Gaussian | `z_goal` | hazard 1/40 |

Different algorithms, different latent streams, different characteristic timescales, with an
explicit cross-scale rule (slow fire resets inner and suppresses a same-tick fast event).
**That is already "a small set of decomposition operators at distinct scales."** It is built,
it is contracted, and it is what the spike hypothesised REE would need to acquire.

MECH-321 discards it twice over:

1. **Collapse at the interface.** `boundary_on()` reduces `List[BoundaryEvent]` to
   `fired: bool` (any scale) + `posterior: max` (`event_segmenter.py:617`). `.events` carries
   `.scale` per event; **MECH-321 never reads it** -- `evaluate()` uses only `boundary.fired`
   and `boundary.posterior` (`policy_decomposition.py:390`).
2. **The slow scale is structurally dead on the rollout stream.** The call site builds
   `latent_signature = {"z_world": ..., "z_self": ...}` with no `z_goal`
   (`module.py:737`). The BOCPD detector returns `(False, 0.0, [])` when none of its streams
   are present (`event_segmenter.py:258`). So the slow scale **cannot fire on rollout, ever,
   as currently wired.**

MECH-321 is therefore a **single-scale consumer of a two-scale substrate**, and the single
scale it does consume is delivered to it as a boolean with the scale label stripped.

---

## 4. The campaign evidence says the trigger, not the depth, is the live problem

Checked before proposing anything, per the brief. The V3-EXQ-816 cluster has run
816 / 820 / 816b / 816c / 816d. **The queue currently holds no MECH-321 entry** (only
V3-EXQ-826a and 828) -- the campaign is stalled at 816d's own null-reading guide: *"consider a
third dose step or conceding the env axis."*

The numbers matter more than the outcomes:

| Metric | Value | Source |
|---|---|---|
| `arm1_vs_trigger_total` | **0** | 816d |
| `vs_trigger_fires_total` | **0** | 816c |
| `pe_trigger_fires_total` | 13 | 816c |
| `cofire_total` | 0 | 816c |
| `spearman(V_s, forward-PE)` | 0.083 (floor 0.2) | 816c |
| `region_vs` range | 0.934 -- 0.963 (threshold 0.4) | 816c/816d |
| `decomp_fired_frac_arm1` | **1.0** | 816d |

Read together: **MECH-321's declared PRIMARY trigger (V_s drop, R1) has never fired once
across the entire campaign.** Every decomposition ever observed was driven by the boundary
half of the OR -- i.e. by the fast scale alone -- and it fired on essentially every evaluation.

Both saturated ends are uninformative. A trigger that never fires and a trigger that always
fires carry the same amount of discriminative signal: none. The campaign has spent two env
doses (816b, 816d) trying to move the never-fires end and got 0.0086 against a 0.01 floor
twice. **Nobody has yet tried to resolve the always-fires end**, and that end is where the
scale structure is hiding: `decomp_fired_frac = 1.0` is opaque, but *"fast fires on 100% of
ticks, slow fires on 3%"* is a measurement.

This is why the probe below is not a duplicate of the live campaign. The campaign's two open
axes are trigger **sensitivity** (H-env-underdrives-uncertainty) and trigger **validity**
(H-vs-proxy-saturation). The scale question is a third axis -- trigger **composition** -- and
it is the one axis that attacks the saturated end rather than the silent one.

---

## 5. Recommendation

### 5a. Depth half -- (a), with the justification replaced

Keep the single tiling operator. Do **not** defend the cap on tractability grounds; defend it
on **structural derivation**, which is stronger and happens to be true:

> `decomposition_depth_cap` is not an independent parameter. It mirrors ARC-071's
> `chunk_max_depth` because the depth it tests is that hierarchy's depth. Values above
> `chunk_max_depth` are inert; the value 1 disables decomposition; the useful range is
> `[2, chunk_max_depth]`, and at `chunk_max_depth`-typical libraries (all chunks depth 1) even
> that range collapses to a single behaviour.

Two concrete follow-ons, both `complicated (buildable)`:

- **Couple or warn.** Either derive `decomposition_depth_cap` from `chunk_max_depth` by
  default, or emit a loud config warning when it is set inert (`> chunk_max_depth`) or
  degenerate (`== 1`). Currently both settings are silent. This is the same failure shape as
  [memory] `reference-reeconfig-from-dims-silent-kwargs`: a knob that looks live and is not.
- **Re-pose the open Q-claim.** MECH-321's hard-vs-soft depth-cap Q-claim is asking the wrong
  question while the parameter is inert. The live version is: *should `depth_cap` track
  `chunk_max_depth` automatically, and is `chunk_max_depth` -- the actual compute-bearing knob
  -- the one that should move as compute allows?* Solway's "should move with compute" point is
  right, but it applies to the composition side, not to MECH-321's mirror.

### 5b. Heterogeneity half -- (c) now, with the probe named; (b) if it comes back positive

**Not decidable today**, and the reason is not epistemic modesty -- it is that the instrument
has never been switched on. The slow scale cannot fire on the rollout stream, so there is
literally no observation of scale-differentiated decomposition to reason from.

**PROBE -- scale-resolved rollout boundary diagnostic.** Default-off, no behaviour change,
no new claim:

1. Add `z_goal` to the `latent_signature` built in
   `HippocampalModule._evaluate_decomposition_ticks` (`module.py:737`), so the slow BOCPD
   scale has its stream on the rollout side. *This alone changes decisions* -- the slow scale
   can now contribute to `boundary.fired` -- so it must sit behind a flag.
2. Read `decision`-side per-scale detail from `boundary.events[].scale` rather than only
   `.fired`, and add `decomp_n_boundary_fires_fast` / `decomp_n_boundary_fires_slow` /
   `decomp_n_boundary_cofire` to `PolicyDecomposition.get_state()`.
3. Run it on the existing 816 harness. No new environment work -- this reads the stream the
   campaign is already generating.

**The question it decides:** *do the fast and slow scales fire at dissociable rollout
positions?*

| Outcome | Reading | Action |
|---|---|---|
| Dissociable (low cofire, distinct positions) | REE's own substrate exhibits heterogeneous distinct-scale segmentation on the imagination stream | Register **(b)** -- see 5c |
| Slow never fires on rollout | `z_goal` does not vary informatively within a rollout; one effective scale on the imagination stream | **(a)** stands; close the design question |
| Slow fires only coincident with fast | Two detectors, one signal; the heterogeneity is nominal | **(a)** stands; record the null |

All three are publishable readings, and the middle one is a genuine possibility worth naming
in advance: `z_goal` is an *integrator* (`config.py:1572`), so it may simply not move inside a
single short rollout. If so, that is itself the answer -- distinct scales require distinct
timescales, and a rollout may be too short to have two.

#### RESOLVED 2026-07-29 -- the probe ran, and the middle row is what came back

**V3-EXQ-830** (`v3_exq_830_mech321_scale_resolved_rollout_boundary_20260727T204927Z_v3`,
PASS / `non_contributory`, substrate `6b5f1090fa`) self-routed
`interpretation.label = slow_never_fires_on_rollout` -- **row 2 of the table above**. Per that
row: **(a) stands, the design question is CLOSED, and the 5c sketch below is RETIRED.**

The reading is load-bearing rather than starved, which is the thing worth checking about a
null. Both arm gates were green: instrumentation coverage 1.0, `zgoal_present_frac` 0.870,
and -- the gate that matters, because it asserts the same statistic the slow BOCPD detector
routes on -- `zgoal_norm_std` 0.070 against a 1e-4 floor. So the slow scale had a live,
*varying* z_goal stream on 87% of 2393 sweeps and still fired **zero** times across 5 seeds.
The anticipated mechanism in the paragraph above is exactly what was observed: z_goal moves
across sweeps but not informatively within one, so the rollout is too short to carry two
timescales. ARM_PROBE_OFF and ARM_PROBE_ON were behaviourally identical
(`n_seeds_action_seq_differs = 0`, identical net harm) -- the expected consequence of a slow
scale that never reaches `boundary.fired`, not evidence the manipulation failed to apply.

**No follow-on experiment was queued, and specifically the mid-execution run was not.** The
open question was whether the mid-execution asymmetry named in `follow_on_named_not_done` had
diluted the slow fraction enough to make the null an artifact. It had not, by the largest
possible margin: `decomp_n_evaluated_midexec = 0` in **all 10 cells** (5 seeds x 2 arms) while
`decomp_n_evaluated_precommit` ran 1862-2618, so `midexec_dilution_frac = 0.0` and the naive
and precommit-corrected slow fractions are already identical (both 0.0). The mid-execution
hook never executes on this harness, so `use_decomposition_scale_resolved_probe_midexec`
(ree-v3 `aaf5caac26`) has no tick to act on -- it is a structural no-op here, and a run with
it ON would reproduce this manifest. Recorded as a GOV-REUSE-1 reanalysis rather than compute:
`reanalysis_mech321_midexec_probe_no_run_needed_20260729T070712Z`.

The counter was checked for inertness before the null was accepted, since a dead counter and
a never-taken branch both read 0. It is live: `policy_decomposition.py:534` increments it on
every `evaluate(hypothesis_tag=False)`, and
`tests/contracts/test_mech321_scale_resolved_boundary.py` asserts `>= 1` behind an explicit
anti-vacuity guard. That contract reaches the hook only by hand-injecting a committed
trajectory (`source=arc071_chunk`, `_committed_step_idx=1`, forced `beta_gate.elevate()`), so
it establishes that the hook works when its preconditions hold -- not that they ever arise
naturally. In 830 they never did.

**Scope.** Says nothing about the *observation* stream, where the slow scale is separately
contracted, and does not weaken MECH-288. Changes no claim status, confidence, `live_status`
or `v3_pending`; MECH-321 remains `candidate` / `v3_pending`.

**Left open, and not the same question:** MECH-321's R4 *second phase* (the mid-execution
re-evaluation) has now never executed in any real experiment on any harness -- 830 establishes
this as a fact about the 816 harness rather than a suspicion. That half of MECH-321's
functional restatement is therefore unmeasured, and the `_midexec` flag is correct,
contract-covered and unexercised. Closing the heterogeneity question does not close that one.

### 5c. If the probe is positive -- what (b) should and should not be -- RETIRED 2026-07-29

> **RETIRED.** The probe ran and came back negative (see the resolution note in 5b above):
> the slow scale never fires on the rollout stream, so there is no scale heterogeneity on the
> imagination stream for a scale-differentiated extension to be built on. Registering (b) is
> not merely premature now -- it is unsupported. Kept below as a record of the shape that was
> considered, not as pending work.

**Should not** be a new ARC-level commitment inventing a fresh operator set. The operators
already exist as MECH-288 scales; inventing parallel ones would duplicate substrate and
re-open a settled R2 shared-substrate commitment.

**Should** be a MECH-level extension of MECH-321: *scale-differentiated decomposition* --
fast/PE boundaries re-segment at fine grain (the current behaviour), slow/goal-BOCPD
boundaries trigger a coarser response (re-segment at chunk-boundary grain, or withhold the
whole trajectory rather than re-tile it). That is Koechlin's structure at REE's grain: the
kind of context-conditional information that failed determines the grain of the repair, rather
than one operator repairing everything the same way. MECH-321 becomes the fast-scale member.

Registering that is premature until the probe runs. Recorded here so the shape is on file.

---

## 6. Transfer caveats, carried forward unchanged

Both caveats from the brief survive this spike and neither is resolved by it:

- **Overt vs imagined.** Badre, Koechlin and Solway all measure externally cued overt
  performance; MECH-321 acts on the imagined trajectory. §5b's probe is the first measurement
  of scale structure *on the imagination stream* REE would have -- which is precisely why its
  negative outcome is informative rather than merely absent.
- **Solway declines to bound depth at policy grain.** Unchanged, and §5a makes it moot for
  MECH-321 specifically: there is nothing for the normative literature to bound, because the
  parameter is derived rather than free. It still bears on ARC-071's `chunk_max_depth`, which
  *is* free, *is* compute-bearing, and is where Solway's "move it as compute allows" argument
  should be re-attached.

---

## 7. Follow-on work surfaced (chipped, not done here)

- Scale-resolved rollout boundary diagnostic (§5b) -- `/implement-substrate`, then
  `/queue-experiment` on the existing 816 harness.
- `decomposition_depth_cap` inert/degenerate config warning + coupling to `chunk_max_depth`
  (§5a) -- `/implement-substrate`.
- The stalled 816 campaign's own next step (third env dose vs conceding the env axis) is
  **not** owned by this spike and is left to the campaign.
