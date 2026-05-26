# MECH-314a Phase-2 Novelty-Source Design

**Status:** DESIGN. No code change, no claim registration, no experiment
queued. Recommendation requires user assent before any landing session.

**Authoring session:** mech314a-phase2-novelty-source-design-20260526T065005Z
(TASK_CLAIMS).

**Cross-refs:**

- Finding doc: [v3_exq_571_root_cause_2026-05-25.md](v3_exq_571_root_cause_2026-05-25.md)
  (REE_assembly master a79915151b).
- Substrate-queue entry: `evidence/planning/substrate_queue.json` MECH-314
  (`pending_retests[V3-EXQ-590b].gated_on[0]` -- corrected 2026-05-26 by
  session exq590a-gate-correction-20260526T061037Z to name the E2 collapse
  as the actual unmeetable upstream).
- Claim registry: `docs/claims/claims.yaml` MECH-314 (parent), MECH-314a/b/c,
  Q-044.
- Design doc (extended in this session by reference, not edited):
  `docs/architecture/mech_314_structured_curiosity_bonus.md`.
- Implementation: `ree-v3/ree_core/policy/structured_curiosity.py`
  (StructuredCuriosity, `_compute_novelty`).
- Score-bias landing site: `ree-v3/ree_core/predictors/e3_selector.py:737`
  (`scores = scores + bias_tensor`).
- ARC-062 GAP-B autopsy precedent: `ree-v3/CLAUDE.md` "ARC-062 GatedPolicy
  GAP-B head-input first-action one-hot augmentation" (2026-05-17), the
  canonical first-action one-hot bypass template for option B.

---

## 1. Empirical context

The finding doc establishes that MECH-314a's `_compute_novelty` is wired
correctly into the score_bias path -- composed into `dacc_score_bias` in
`REEAgent.select_action()`, passed as `score_bias` to `e3.select()`, added
to per-candidate scores at `e3_selector.py:737`, used by `argmin(scores)`
or `multinomial(softmax(-scores/T))`. If `score_bias[i]` varies across
`i in [K]`, argmin shifts. There is no plumbing-side bug.

Per-candidate spread is structurally zero in the current substrate for
two **independent** reasons. Each blocks the channel on its own.

### Failure mode F1 -- ResidueField is empty on untrained / harm-free runs

`ResidueField.accumulate()` only fires on `harm_occurred=True` AND a
committed trajectory (`e3_selector.py:894`). Untrained random-policy runs
have neither. From the finding doc's first driver
(`/tmp/verify_mech314a_propagation.py`), 30 waking ticks on a default
untrained agent with `use_structured_curiosity=True`,
`curiosity_novelty_weight=0.5`, `curiosity_bias_scale=1.0`:

- `residue_field.rbf_field.active_mask.sum() == 0` for every tick.
- `_compute_novelty` returns `None` (line 414 of `structured_curiosity.py`).
- `_bdc_curiosity` is identically `[0, 0, ..., 0]`.

This kills MECH-314a entirely for any first-encounter / harm-free episode,
including the entire EXQ-590-series Goldilocks calibration target regime.

### Failure mode F2 -- E2 world-forward collapses K candidates' first-step z_world

From the finding doc's second driver
(`/tmp/verify_mech314a_with_residue.py`), same agent with `residue_field`
manually seeded with 8 RBF centers so `cur_n_active=8`,
`last_novelty_norm=14.72`:

- Bias magnitude saturates the +/-1.0 clamp (`mean_bias=-1.0`).
- `std_bias = 0.0000` across K=32.
- `cand_world_pairwise_dist = 0.0000` across K=32, even though
  `cand_action_std = 0.034-0.044` and 2-3 unique argmax action classes
  exist in the candidate pool.

All K candidates produce the same z_world after one E2 world-forward
step despite differing in their first action. This is the same
bottleneck the 2026-05-17 ARC-062 GAP-B autopsy identified
(`ree-v3/CLAUDE.md`, verbatim):

> SP-CEM delivers ~5 distinct first-action classes but E2 world-forward
> compresses them to 0.22% of z_world magnitude before reaching the
> z_world-only GatedPolicy heads -- the heads are under-fed.

The GAP-B fix (`gated_policy_use_first_action_onehot`) was scoped only
to `GatedPolicy`. Every bias channel reading `cand_world_summaries`
(MECH-314a curiosity novelty, MECH-320 tonic_vigor, MECH-295 liking,
SD-033a lateral_pfc, SD-033b ofc) consumes the same compressed
first-step `z_world` and is doomed by the same upstream collapse.

### Why two failures matter for design

F1 and F2 are not redundant. F1 fires on every untrained / harm-free
episode regardless of E2 behaviour. F2 fires on every episode where
ResidueField has been populated, regardless of MECH-314a's own wiring.
A fix that addresses only one leaves the channel dead in the other
regime. Options below are evaluated against both.

---

## 2. Design question

Should MECH-314a source novelty from a richer signal -- one that
decouples it from BOTH failure modes -- so that the per-candidate
contribution is non-zero even on harm-free episodes and even while E2
world-forward collapses first-step z_world?

If yes, what should that signal be? Does the resulting mechanism remain
faithful to MECH-314's biological / formal grounding (Wittmann 2008
ventral-striatum novelty response, Bellemare 2016 / Burda 2018
count-based / RND computational analog), or does it become something
different that warrants a new claim?

---

## 3. Options

Each option is evaluated against:

- **Cost**: low / medium / high (engineering work to land).
- **F1 fix**: does it produce non-zero spread on untrained / harm-free
  episodes?
- **F2 fix**: does it produce non-zero spread when E2 collapses
  first-step z_world?
- **Semantic fidelity to MECH-314**: how close is the result to the
  Wittmann-2008 striatal-novelty reading?
- **Registry implications**: does it modify MECH-314a's spec, motivate a
  new sub-claim, or open a new Q-claim?
- **Falsifier sketch**: what experiment tests whether the change actually
  produces non-zero per-candidate spread AND a behavioural effect on E3
  selection?

### Option A -- Rolling z_world visitation buffer always-on

**Mechanism.** Maintain a deque (or online k-means, or RBF resample) of
the last N z_world values from the agent's waking-tick stream. Compute
MECH-314a novelty as RBF distance against this buffer, either in
addition to or instead of the harm-residue centers.

Phase-1 trivial implementation: `collections.deque(maxlen=N)` of recent
z_world tensors, appended in `REEAgent.sense()` outside the
`harm_occurred + committed_trajectory` gate. `_compute_novelty` swaps
or composes the active-mask source from `residue_field.rbf_field` to
the visitation deque.

**Cost.** LOW. ~30-50 lines: deque on agent, append hook in
`sense()` after `update_per_stream_vs`, plumbing into
`_compute_novelty` (optional active source argument), config knob.

**F1 fix.** YES. Buffer populates on every waking tick regardless of
harm. MECH-314a has reference points from tick 1.

**F2 fix.** NO. The buffer stores past z_world states. The K candidates
still all map to the same first-step z_world under E2 compression, so
every candidate's distance to every buffer entry is identical. Per-
candidate spread is still zero.

**Semantic fidelity.** MEDIUM. Wittmann 2008 ventral-striatum novelty
fires on stimulus repetition irrespective of harm valence. Striatal
novelty signals do not require an aversive event to compute "is this
state novel?". A rolling visitation buffer is closer to the literal
Wittmann reading than the harm-coupled residue. **However**, it
converts MECH-314a from a "novelty against the harm landscape" signal
into a generic "novelty against recent agent history" signal -- which
is what classical count-based / RND analogs (Bellemare 2016, Burda
2018) actually instantiate.

**Registry implications.** This is a soft re-spec of MECH-314a's
signal source. The biological anchor (Wittmann 2008) and the
computational analog claims (Bellemare 2016, Burda 2018) survive
verbatim -- arguably the new wiring is **more** faithful to those
anchors. The current MECH-314a `evidence_quality_note` says: "Phase 1
signal source: minimum distance from candidate's first-step z_world to
the nearest ACTIVE ResidueField RBF center, normalised by candidate-
pool mean norm." This wording is Phase-1-specific; updating it to name
the rolling buffer is consistent with how MECH-314b/c carry similar
Phase-1 caveats. No new claim ID required.

A separate question: is the harm-coupling of the original wiring
semantically meaningful, or was it an implementation accident from
reusing ResidueField as the only available "states the agent has
seen" store? Reviewing `_compute_novelty`'s docstring -- it talks
about RBF centers, not specifically about harm centers. The harm
gating lives upstream in ResidueField, not in MECH-314a. So the
re-spec is an unblocking of an implementation accident, not a
deviation from the original architectural intent. **Strong reading**:
MECH-314a was never meant to be harm-coupled; the harm gating leaked
in via ResidueField's policy.

**Falsifier sketch.** Diagnostic experiment with `use_curiosity_novelty=True`,
`use_curiosity_uncertainty=False`, `use_curiosity_learning_progress=False`,
visitation buffer ON, on an untrained agent with no harm contact in the
first 100 ticks:

- C1: `_bdc_curiosity.std(dim=...) > 0` for at least 80% of waking ticks
  past tick 20 (buffer warmed).
- C2: `n_active_residue_centers == 0` AND `last_novelty_norm > 0` (the
  signal source is the visitation buffer, not residue).

This validates F1 fix. For F2 the experiment is degenerate -- it cannot
fire under E2 collapse (the per-candidate spread the diagnostic measures
is zero by construction at the candidate stage). Option A does not need
to clear F2 to be useful, but it cannot validate F2 either; F2 remains
a separate blocker.

### Option B -- First-action one-hot bypass (per GAP-B template)

**Mechanism.** Mirror the 2026-05-17 ARC-062 GAP-B fix at MECH-314a's
candidate-feature site. Concatenate each candidate's first-action
one-hot onto its z_world summary before the RBF-distance computation.
Each candidate's signature becomes `[z_world (collapsed) + first_action_onehot]`.
Under E2 collapse, z_world is identical across K but action one-hot
carries the per-candidate spread.

The GAP-B fix wired this on `GatedPolicy` only via
`gated_policy_use_first_action_onehot` (False default;
`head_in_dim = world_dim + action_dim` when True). The analogous flag
for MECH-314a would be `curiosity_use_first_action_onehot`.

**Cost.** LOW-MEDIUM. ~40-60 lines: config flag, agent-side wiring to
build per-candidate first-action one-hot tensor (already exists for
GatedPolicy -- can be lifted to a shared builder), `_compute_novelty`
signature extension to accept the augmented tensor, RBF-center
dimensionality extension or projection (centers currently live in
`world_dim`; augmented features live in `world_dim + action_dim`, so
either project or pad the centers).

The dimensionality mismatch is the non-trivial part. Padding centers
with zeros is the cheap choice (the action component contributes its
full norm to the candidate-to-center distance, which is **all** of
the per-candidate spread). Projecting back to `world_dim` collapses
the spread again and defeats the purpose.

**F1 fix.** NO. Action one-hots produce per-candidate spread within a
single tick, but without an active residue (or active visitation
buffer) the comparison set is empty. `_compute_novelty` still returns
`None` on `n_active == 0`. F1 must still be addressed by Option A or
similar.

**F2 fix.** YES. Per-candidate action one-hots carry spread by
construction; F2's z_world collapse no longer reaches the bias
output.

**Semantic fidelity.** LOW-to-MEDIUM. Wittmann 2008 ventral striatum
fires on **state** novelty, not on action novelty. "How novel is this
state, holding action constant?" is the Wittmann reading. "How novel
is taking this action from the current state?" is a different
biological substrate -- closer to action-conditional novelty (Schmidhuber
1991 compression-progress variants; Pathak 2017 ICM-style forward-
model PE; **not** Wittmann). MECH-314c (learning-progress curiosity)
is the existing claim that owns the action-conditional reading; its
biological anchor is explicitly different from MECH-314a's.

Action one-hot bypass would mean MECH-314a starts computing something
closer to MECH-314c than to its own Wittmann anchor. This is a real
semantic problem.

**Registry implications.** This is **not** a Phase-1-caveat-level
re-spec. It changes the signal source from "state novelty" to "state +
action novelty" -- biologically distinct readings. Two clean ways to
land it:

1. **Modify MECH-314a's spec** to encompass state-and-action novelty,
   weaken the Wittmann anchor (or strengthen the Bellemare/Burda
   analog which is action-conditional in many implementations), accept
   the conflation with MECH-314c at the substrate level, and let Q-044
   re-examine whether 314a and 314c are still distinct.
2. **Register a new sibling sub-claim** (MECH-314d: state-and-action
   novelty bonus) that is implemented in parallel with 314a, and
   leave the existing 314a wiring (state-only via residue / visitation)
   on a separate signal source. Q-044 would then become a four-arm
   ablation instead of three-arm.

Option 2 is cleaner registry-wise but introduces a new claim ID and a
new Q-044 redesign. Option 1 is cheaper but weakens the lit-anchored
sub-flavour split that Pull 1 R3 explicitly recommended NOT to collapse
prematurely.

**Falsifier sketch.** Three-arm experiment with state-only / state+action /
all-off ablation; metric is per-candidate bias spread on a fixed probe
state where E2 is known to collapse (any untrained random-policy
state, per the finding doc). State-only arm should produce zero
spread; state+action arm should produce non-zero spread proportional
to the entropy of the candidate pool's first-action distribution;
all-off arm should produce zero.

### Option C -- Candidate-pool relative rank

**Mechanism.** Compute novelty per candidate as a function of where it
sits in the current K-candidate distribution. Concrete choices: (a)
distance from the candidate-pool mean ("how unusual is this candidate
among the current proposals"); (b) percentile rank of the candidate's
z_world norm or its action argmax frequency; (c) inverse k-NN density
among the candidates.

No external reference store. The signal is purely intra-pool.

**Cost.** LOW. ~20-30 lines: replace the `_compute_novelty` body with
intra-pool arithmetic, drop the residue dependency entirely.

**F1 fix.** YES on untrained episodes **only if** the K candidates
themselves have non-zero spread at the pre-E2 stage. Under SP-CEM with
support-preserving stratification, the candidate pool does carry
first-action class diversity at the pre-E2 stage; that diversity then
gets compressed by E2. If we compute the relative-rank novelty
**before** the E2 forward step, the spread survives.

**F2 fix.** Same answer -- YES only when computed on pre-E2 candidates.
Effectively this option requires moving MECH-314a's signal computation
upstream of E2's forward step, computing on raw candidate first-action
one-hots or hippocampal action-object proposals.

**Semantic fidelity.** LOW. This is a diversity-bonus, not a novelty-
bonus. Wittmann 2008 ventral-striatum responds to state-novelty against
the **agent's history of encounters**, not against the **current
proposal pool**. Bellemare 2016 / Burda 2018 count-based / RND analogs
also compute against a history, not against an in-pool reference.

There is a legitimate biological reading that could host Option C
(some BG / lateral PFC diversity-bias literature), but it is not the
Wittmann reading. MECH-314a's lit anchor does not survive this option.

**Registry implications.** Option C should NOT be landed under
MECH-314a's name. It is closer to a parent-level diversity-bonus that
sits alongside MECH-313 / MECH-314, not a sub-flavour of 314. A new
ARC-065-child MECH-claim would be appropriate (call it MECH-CC).
Q-044's three-arm ablation would be unaffected; a separate Q-claim
would ask whether MECH-CC is independently useful from MECH-313 /
MECH-314.

**Falsifier sketch.** Same diagnostic protocol as A or B; the
contrastive arm is "diversity-bonus vs novelty-bonus" rather than
ablating MECH-314a entirely. Acceptance criterion is monotonicity of
selected-candidate diversity in the diversity-bonus weight, holding
MECH-314a off (so we are not double-counting).

### Option D -- Hybrid harm-residue + rolling visitation

**Mechanism.** Keep the harm-residue RBF as the **primary** "what to
avoid" novelty signal (its biological reading is preserved). Add a
**small** additive rolling-visitation term so the channel is never
literally zero on harm-free episodes. Per-channel weights `w_harm`
and `w_visit` are configurable.

`_compute_novelty` returns a sum of two terms when both signal sources
have non-empty centers:

```
novelty = w_harm * min_dist_to_harm_centers / mean_norm
        + w_visit * min_dist_to_visitation_buffer / mean_norm
```

with `w_harm` defaulting to 1.0 and `w_visit` defaulting to a smaller
value (e.g. 0.3) so visitation-based novelty cannot dominate the
harm-coupled signal when both are available.

**Cost.** MEDIUM. ~50-80 lines: visitation buffer (per Option A) plus
weighted composition inside `_compute_novelty` plus two new config
weights.

**F1 fix.** YES (via the visitation term).

**F2 fix.** NO (same as Option A -- z_world collapse defeats both
distance computations).

**Semantic fidelity.** HIGH. The harm-coupled reading is preserved as
the primary signal; the visitation term is explicitly secondary and
configurable. Could be framed as "MECH-314a fires on harm-residue when
available, falls back to visitation-history novelty when not" --
biologically plausible (striatal novelty signals do not actually require
harm, but harm-coupled landscapes are a special case where the signal
is strongly active).

**Registry implications.** This is a Phase-1-caveat-level update to
MECH-314a (add visitation as a secondary signal source) plus
config-level documentation. No new claim required. Pull 1 R3 sub-
flavour split is preserved.

**Falsifier sketch.** Two-tier diagnostic:

- Tier 1 (harm-free): residue empty, visitation populated -- check
  per-candidate spread non-zero, harm-component contribution zero,
  visitation-component contribution non-zero.
- Tier 2 (harm-populated): both signal sources active -- check
  harm-component dominates when `w_harm > w_visit`, both contribute,
  weighting behaves as expected.

### Option E -- Defer pending E2 world-forward fix

**Mechanism.** Do nothing in MECH-314a. Wait for the proper
architectural fix to land at E2 world-forward (preserving per-action
z_world divergence), then re-evaluate whether MECH-314a needs any
re-wiring at all.

Concurrent improvements likely also fix the residue-empty F1 case:
once the E2 fix exposes the per-candidate spread, MECH-314a's existing
wiring against the harm-residue centers would produce non-zero spread
on any episode where the residue has been populated. The F1 case
(harm-free episodes) remains dead, but those are not the regime the
current pending experiments (V3-EXQ-590-series Goldilocks, ARC-065
behavioural-diversity validation) target -- they assume some training
has occurred and the residue is non-empty.

**Cost.** LOW now (zero work in MECH-314a). HIGH later (the E2 fix is
likely a much larger piece of work than rewiring MECH-314a, and it
unblocks several downstream calibrations -- V3-EXQ-590-series, ARC-065
behavioural-diversity validation, MECH-320 tonic_vigor calibration,
SD-033a lateral_pfc behavioural validation, MECH-295 liking bridge
behavioural validation -- so the work is justified at a higher
architectural level, just not via MECH-314a's failure alone).

**F1 fix.** NO (residue-empty case stays dead).

**F2 fix.** YES, transitively, when the E2 fix lands.

**Semantic fidelity.** PERFECT (no spec changes).

**Registry implications.** None. Status quo. Substrate-queue MECH-314
`pending_retests` block stays gated on the E2 fix exactly as worded
post-2026-05-26 correction. Q-044 stays blocked.

**Falsifier sketch.** N/A -- no MECH-314a change to test. The
falsifiable hypothesis is at the E2 level: "preserving per-action
z_world divergence at first-step E2 forward causes per-candidate bias
spread to become non-zero across all consumers (MECH-314a, MECH-320,
MECH-295, SD-033a, SD-033b) without further per-consumer changes."

### Option F (additional, surfaced during evaluation) -- Action-object identity at hippocampal proposal stage

**Mechanism.** Source novelty from the hippocampal trajectory
proposer's per-candidate action-object identity (the index into
HippocampalModule's action-object space O, MECH-074 / ARC-007), not
from z_world at all. Each candidate is identified by its initial
action-object index; novelty is the RBF distance in action-object
space against either a rolling buffer of recently-proposed action
objects or a harm-coupled action-object residue (parallel to the
existing z_world ResidueField, but at the action-object grain).

**Cost.** HIGH. Requires either a new ResidueField-like store at the
action-object grain or a rolling buffer in action-object space, plus
agent-side plumbing to expose per-candidate action-object indices to
`_compute_novelty`.

**F1 fix.** Conditional on parallel store population (harm-coupled
fails F1; rolling-action-object buffer fixes F1).

**F2 fix.** YES. Action-object identity is set before E2's forward
step and is genuinely per-candidate.

**Semantic fidelity.** MEDIUM. This is what some implementations of
striatal novelty do (count-based bonus over discrete action-object
hashes). Closer to Wittmann's "novel stimulus" than Option C's
intra-pool diversity but further than Option D's harm-residue
reading.

**Registry implications.** Substantial. Action-object-grain residue is
its own architectural piece (would interact with ARC-007 strict
"hippocampal proposals are value-flat" boundary). Probably warrants
a new MECH-claim sibling to MECH-314a rather than a re-spec.

**Falsifier sketch.** Same shape as B's three-arm. Lower priority
than A / B given the higher implementation cost; surfaced for
completeness.

---

## 4. Recommendation

**Recommended option: A (rolling z_world visitation buffer always-on),
landed BEFORE the E2 fix.**

### Reasoning

1. **A is the smallest semantically-faithful change.** It uses
   z_world as MECH-314a already does, just sourced from a buffer
   that always populates rather than from a harm-gated residue. The
   biological / formal anchors (Wittmann 2008, Bellemare 2016, Burda
   2018) survive -- arguably with **higher** fidelity, because the
   harm-gating in the current implementation was an accidental
   side-effect of reusing ResidueField, not part of MECH-314a's
   spec.

2. **A fixes F1 (the harm-free / untrained regime).** The Goldilocks
   calibration target regime (V3-EXQ-590-series) deliberately runs
   on untrained agents to measure the substrate's response to
   novelty-bonus-weight sweeps before any policy has shaped the
   visitation distribution. F1 is currently the **dominant** blocker
   in this regime -- the residue is empty, so even if E2 collapse
   were fixed tomorrow, the substrate would still be silent. Option
   E does not fix F1.

3. **A is silent on F2.** This is acknowledged, not denied. F2
   remains a real architectural blocker for the post-training regime
   where the residue IS populated but per-candidate spread is still
   killed by E2 compression. **A is a necessary-but-not-sufficient
   fix**; F2 must be addressed separately, ideally at the E2 level
   (Option E's target).

4. **A does NOT preclude later landing of B or the E2 fix.** If A
   lands and Goldilocks calibration becomes meaningfully testable,
   the next failure-mode encountered (post-training, F2 regime)
   either gets the E2 fix or layers Option B on top. The two are
   compatible: A populates a buffer that B's augmented signature
   uses for distance computation, and the E2 fix transparently
   restores the harm-residue path that A still queries.

5. **Option E (defer) is rejected** because (a) the E2 fix is open-
   ended scope that may take many sessions to land; (b) the
   downstream calibrations blocked behind it are already 6+ weeks
   stale (EXQ-590a was a wasted run), and (c) Option A is cheap
   enough (~30-50 lines) that the cost of landing it is dwarfed by
   the cost of one more wasted calibration cycle. The "do nothing
   in MECH-314a" framing rests on F1 being addressable transitively
   via the E2 fix -- but it isn't, because F1 is a residue-population
   issue, not an E2-collapse issue.

6. **Option D (hybrid) is the close runner-up.** It preserves the
   harm-residue reading as primary and adds visitation as a secondary
   fallback. The downside is slightly more code and two new config
   weights; the upside is symbolic preservation of the original
   harm-coupling. If user assent on Option A includes concern that
   the harm-coupling has independent biological value worth preserving,
   D is the natural extension and could be landed as Phase-2a (A) +
   Phase-2b (the D composition layer added afterwards).

7. **Option B (first-action one-hot) is parked for after A lands.**
   B is the GAP-B template, biologically distinct from MECH-314a, and
   requires either a new sibling claim or a more substantial re-spec.
   If F2 must be addressed at the per-consumer layer rather than at
   E2, B becomes the right shape of fix, but it should be staged after
   A clears F1 so we know which blocker we're actually testing
   against.

8. **Option C (intra-pool rank) is rejected as a MECH-314a re-spec**
   because the semantic break from Wittmann is too sharp. It may still
   be worth registering as a new claim, but not under MECH-314a's
   identity.

9. **Option F (action-object identity)** is rejected for cost, not
   architectural objection. Worth re-examining in V4 when
   action-object-grain residues are likely to land for other reasons
   anyway.

### What Option A specifically commits to

- Add a per-agent rolling z_world visitation buffer (deque,
  configurable length, default ~256 ticks).
- Append in `REEAgent.sense()` after `update_per_stream_vs`, gated by
  MECH-094 hypothesis_tag (waking-only writes; replay/DMN ticks do not
  contribute to the buffer).
- Extend `StructuredCuriosity._compute_novelty` to accept an alternate
  active-source argument; agent-side wiring passes the visitation
  deque when `use_curiosity_novelty=True` AND
  `curiosity_novelty_source="visitation"`.
- Config: `curiosity_novelty_source: Literal["residue", "visitation",
  "auto"]` (default `"auto"` -- residue when non-empty, fallback to
  visitation; `"residue"` preserves bit-identical legacy behaviour;
  `"visitation"` is a pure replacement).
- New config knobs: `curiosity_visitation_buffer_len` (int, default
  256), `curiosity_novelty_source` (literal, default `"residue"` for
  the bit-identical-OFF default; experiments opt in to `"auto"` or
  `"visitation"`).

### What Option A does NOT commit to

- No change to MECH-314a's biological anchor (Wittmann 2008 still
  applies; visitation buffer is consistent with that anchor).
- No change to MECH-314b or MECH-314c.
- No change to ResidueField's harm-coupling policy.
- No new claim ID; Q-044's three-arm ablation framing survives.
- No new experiment queued in this session.

---

## 5. Proposed registry hook

### Draft Q-claim YAML

To be reviewed and committed in a separate governance session. Drafted
here for completeness; **do not commit to claims.yaml in this session**.

```yaml
- id: Q-NEW
  title: "Does sourcing MECH-314a novelty from a rolling z_world visitation buffer (always populated on waking ticks, independent of harm + commitment gating) produce per-candidate bias spread on untrained / harm-free episodes without breaking the Wittmann 2008 striatal-novelty biological anchor?"
  claim_type: open_question
  subject: policy.curiosity.mech314a_phase2_signal_source
  polarity: open
  status: open
  implementation_phase: v3
  claim_level: mechanistic
  registered_utc: "<TO_FILL_AT_COMMIT>"
  depends_on:
    - MECH-314a   # the signal source being respec'd
    - MECH-314    # parent
    - ARC-065     # grandparent architectural commitment
  notes: >
    Two independent failure modes block MECH-314a per-candidate
    novelty in the current substrate (see evidence/planning/
    v3_exq_571_root_cause_2026-05-25.md REE_assembly master
    a79915151b, and evidence/planning/mech_314a_phase2_novelty_source_design.md):

    F1 -- ResidueField only accumulates on harm_occurred=True AND
    a committed trajectory. Untrained / harm-free episodes have an
    empty residue and `_compute_novelty` returns None, so the
    channel contributes zero. Targets the V3-EXQ-590-series
    Goldilocks calibration regime.

    F2 -- E2 world-forward predictor compresses K diverse
    first-action candidates to identical first-step z_world
    (cand_world_pairwise_dist=0.0000 across K=32 with 2-3 unique
    action argmax classes). Same root cause as 2026-05-17 ARC-062
    GAP-B autopsy; the GAP-B fix `use_first_action_onehot` was
    scoped only to GatedPolicy.

    The design-doc recommendation is to source novelty from a
    rolling z_world visitation buffer that always populates on
    waking ticks. This fixes F1; F2 remains addressable separately
    (E2 fix or option-B per-consumer first-action one-hot bypass).

    Resolution path: diagnostic experiment per the design doc's
    "Falsifier sketch" for Option A. Acceptance:
      (a) on a harm-free untrained agent, _bdc_curiosity has
          non-zero std across K for >=80%% of waking ticks past tick 20.
      (b) per-candidate bias signal traceable to visitation buffer
          (n_active_residue_centers=0 AND last_novelty_norm>0).
      (c) Bit-identical OFF when curiosity_novelty_source="residue".

    Q-044 three-arm ablation framing is preserved; the visitation
    buffer is a Phase-1-caveat-level update to MECH-314a's signal
    source, not a new sub-flavour.
  location: evidence/planning/mech_314a_phase2_novelty_source_design.md
```

### Alternative -- candidate MECH-claim (NOT preferred)

If user assent during a follow-up session prefers to register the
visitation-buffer mechanism as a new sub-claim rather than a re-spec
(e.g. because they prefer to preserve MECH-314a's harm-coupling
verbatim and treat visitation as a distinct mechanism), draft below.
The recommendation above is the Q-claim path.

```yaml
- id: MECH-NEW
  title: "policy.curiosity.visitation_buffer_novelty -- per-candidate RBF distance against a rolling buffer of recently-visited z_world states, populated every waking tick independent of harm or commitment gating. Sibling to MECH-314a striatal_novelty (harm-residue-coupled) and to MECH-313/314b/314c. Phase-2 substrate authored to unblock the F1 (harm-free episodes) failure mode of MECH-314a."
  claim_type: mechanism_hypothesis
  subject: policy.curiosity.visitation_buffer_novelty
  polarity: asserts
  status: candidate
  implementation_phase: v3
  v3_pending: true
  claim_level: mechanistic
  registered_utc: "<TO_FILL_AT_COMMIT>"
  depends_on:
    - MECH-314    # parent structured-curiosity-bonus claim
    - MECH-314a   # sibling (harm-residue source for the same novelty signal)
    - ARC-065     # grandparent architectural commitment
  functional_restatement: >
    A rolling-buffer variant of striatal novelty. Where MECH-314a
    sources the comparison set from ResidueField centers
    (harm-gated), MECH-NEW maintains an always-populated buffer of
    the agent's recent z_world history. Per-candidate novelty is the
    RBF distance to the nearest buffer entry, normalised by the
    candidate-pool mean norm.

    Falsifiable independently of MECH-314a: in untrained / harm-free
    runs MECH-314a is silent by construction; MECH-NEW should fire.
    In trained runs with populated residue, MECH-314a should
    dominate and MECH-NEW should produce smaller-magnitude
    contributions; ablating MECH-NEW should leave trained-regime
    behaviour qualitatively intact.
  evidence_quality_note: >
    Sister of MECH-314a in the striatal-novelty family. Bellemare
    et al. 2016 NeurIPS pseudo-count exploration bonus is the
    closest computational analog for the buffer-rolling form.
    Wittmann et al. 2008 Neuron substrate carries through (ventral
    striatum responds to stimulus novelty; rolling-buffer source
    is closer to the literal biological reading than harm-coupled
    residue, which was an implementation accident of reusing
    ResidueField).

    Phase-2 implementation site: ree-v3/ree_core/policy/structured_curiosity.py
    StructuredCuriosity._compute_novelty extended to accept an
    alternate active-source argument. Bit-identical to MECH-314a
    when curiosity_novelty_source="residue" (default).
  location: docs/architecture/mech_314_structured_curiosity_bonus.md
```

The Q-claim is preferred over the new MECH-claim because (a) the
harm-coupling in current MECH-314a appears to be an implementation
accident rather than a deliberate architectural choice (see the
"Strong reading" note in Option A's registry implications, section 3);
(b) registering a sibling MECH-claim for what is arguably a re-spec
of the same architectural slot proliferates claim IDs without adding
new content; (c) Pull 1 R3's sub-flavour split was about distinct
biological substrates (striatum / frontopolar / ML-tradition), not
about distinct novelty stores at the same biological substrate.

---

## 6. Experiments to design once Option A lands

Do NOT queue any of these in this session. List for the landing session
to draft:

1. **V3-EXQ-NEW-1 (MECH-314a F1 substrate-readiness diagnostic).** UC1-UC5
   structured per the MECH-314 V3-EXQ-545 template. Acceptance:
   `_bdc_curiosity.std() > 0` on >=80% of waking ticks on an untrained
   harm-free random-policy agent; `n_active_residue_centers=0` AND
   `last_novelty_norm>0` to confirm the signal source is the visitation
   buffer; bit-identical OFF preserved at default
   `curiosity_novelty_source="residue"`. Sub-test for MECH-094
   simulation_mode gate (visitation buffer does not accumulate on
   replay/DMN ticks).

2. **V3-EXQ-590b (Goldilocks calibration, retest).** With Option A
   landed and `curiosity_novelty_source="visitation"` set, the
   V3-EXQ-590 weight sweep across `novelty_bonus_weight in {0.1, 0.3,
   0.5, 0.7, 1.0}` should produce monotone or single-peaked variation
   of joint metrics (mean_h_pos, mean_coverage, mean_novelty_ema). The
   V3-EXQ-590a `do_not_adopt.goldilocks_weight=0.1` constraint is
   preserved -- the new run must pick a weight by signal, not tiebreak.
   Substrate-queue gating on V3-EXQ-590b's first `gated_on` condition
   ("Per-candidate bias signal has non-zero spread across K") is
   cleared by the Option A landing PASS of EXQ-NEW-1; the second
   `gated_on` ("ARC-065 behavioural-diversity landed") remains
   in-flight via the V3-EXQ-608 P2 diagnostic.

3. **V3-EXQ-NEW-2 (Q-044 three-arm ablation, rescoped).** Q-044's
   three-arm ablation (314a-OFF / 314b-OFF / 314c-OFF + all-on) becomes
   testable on harm-free regimes once Option A lands. The substrate-
   queue Q-044 entry currently lists "structurally indistinguishable
   from broadcast-scalar 314b/c while upstream collapse persists" as
   the blocker -- post-Option-A, 314a contributes per-candidate spread
   on harm-free episodes, so the ablation can distinguish it from
   314b/c which remain broadcast-scalar in Phase 1.

4. **V3-EXQ-NEW-3 (MECH-314a F2 follow-on, conditional).** If Option A
   lands cleanly and the F2 (post-training E2 collapse) blocker
   becomes the dominant blocker for downstream calibrations (ARC-065
   behavioural-diversity validation, MECH-320 tonic_vigor calibration),
   queue a follow-on that EITHER tests Option B layered on top OR
   waits for the E2 fix. Decision deferred to that point.

---

## 7. Claims / plan docs / substrate_queue entries to update on landing

Do NOT update any of these in this session. List for the landing
session:

1. **`docs/claims/claims.yaml` MECH-314a `evidence_quality_note`.**
   Update the "Phase 1 signal source: minimum distance from
   candidate's first-step z_world to the nearest ACTIVE ResidueField
   RBF center" wording to acknowledge the visitation-buffer Phase-2
   signal source as an optional path. Add cross-reference to the
   landing session and the design doc.

2. **`docs/claims/claims.yaml` MECH-314 parent `functional_restatement`.**
   The "Phase 1 signal source: minimum distance from candidate's first-
   step z_world to the nearest ACTIVE ResidueField RBF center" wording
   in the parent claim's evidence_quality_note table (column "Phase 1
   signal source", row MECH-314a) should be updated identically.

3. **`docs/claims/claims.yaml` Q-NEW (new entry).** Commit the Q-claim
   YAML drafted in section 5.

4. **`docs/claims/claims.yaml` Q-044 notes.** Add a paragraph noting
   that the three-arm ablation framing was unblocked at the F1 level
   by Option A landing (with a session ID + commit reference); the
   F2-level blocker (E2 world-forward z_world per-candidate
   divergence) remains pending.

5. **`docs/architecture/mech_314_structured_curiosity_bonus.md`.** Extend
   the "Three sub-flavours" table for MECH-314a's "Phase 1 signal
   source" cell to name the visitation-buffer alternative. Add a new
   section "Phase 2: visitation-buffer signal source" describing
   Option A's implementation and the falsifier acceptance criteria.

6. **`evidence/planning/substrate_queue.json` MECH-314 entry.** Update
   `pending_retests[V3-EXQ-590b].gated_on[0]` status from
   `pending_upstream_substrate_fix` to `partially_cleared` (or similar
   semantic, to be decided in the landing session). The F1 leg is
   cleared by Option A; the F2 leg (E2 collapse) remains. Refine the
   `requires` field to distinguish F1 (cleared) from F2 (pending).

7. **`evidence/planning/substrate_queue.json` ARC-065 entry.** The
   `pending_retests_downstream` cross-link to MECH-314 should mirror
   the gate-status update.

8. **`evidence/planning/v3_exq_571_root_cause_2026-05-25.md`.** Add a
   resolution note at the bottom of the document referencing this
   design doc and the landing session, so future readers walking the
   trail from the root-cause finding to the resolution can find the
   chain.

9. **`evidence/experiments/review_tracker.json`.** Once V3-EXQ-NEW-1
   runs and PASSes, the standard review-tracker discharge applies.

10. **`MEMORY.md` (auto-memory).** Update the entry for
    `feedback_diagnostic_experiment_descriptions.md` or similar if the
    landing session surfaces a meta-lesson about diagnostic-vs-
    behavioural staging. Probably not needed for this work; flagged
    here for the landing session to evaluate.

---

## 8. Out of scope (deferred)

- The actual E2 world-forward per-action z_world divergence fix.
  Separate architectural work; affects MECH-314a, MECH-320, MECH-295,
  SD-033a, SD-033b uniformly. Probably motivates a new SD-claim or
  modification to SD-004 / SD-005 / E2 spec.
- Option B (first-action one-hot bypass on MECH-314a). Parked for
  after Option A lands; only relevant if F2 must be addressed at the
  per-consumer layer rather than at E2.
- Option C (intra-pool relative rank as MECH-CC sibling claim).
  Separate registration if it is to land at all.
- Option F (action-object identity novelty). V4-or-later.
- MECH-314b/c Phase-2 per-candidate refinement (E1 forward-variance
  head, per-candidate learning-progress estimate). Existing parent
  claim already flags this as deferred to Phase 2; the Option A
  landing of MECH-314a does not change that timeline.
- V3-EXQ-590b queue entry. Drafted in section 6 but not queued in any
  session yet; queueing happens after V3-EXQ-NEW-1 PASS and explicit
  user instruction.

---

## 9. Recommendation summary

| Aspect                | Choice                                                     |
|-----------------------|------------------------------------------------------------|
| Recommended option    | A (rolling z_world visitation buffer always-on)            |
| Cost                  | LOW (~30-50 lines)                                         |
| F1 fix                | YES (untrained / harm-free regime)                         |
| F2 fix                | NO (E2 collapse still defeats the channel)                 |
| Semantic fidelity     | MEDIUM-HIGH (Wittmann/Bellemare anchors survive)           |
| Registry hook         | Q-claim (Q-NEW) -- design doc + Phase-1-caveat update      |
| New claim ID          | NO (re-spec of MECH-314a signal source, not a new sub-flavour) |
| Blocks cleared by A   | F1 only; V3-EXQ-590b first `gated_on` condition (partial)  |
| Blocks remaining      | F2 (E2 collapse); V3-EXQ-590b second `gated_on` (ARC-065)  |
| Follow-on if F2 dominates | Option B (per-consumer first-action one-hot bypass) OR E2 fix |
| Runner-up             | D (hybrid harm + visitation), if harm-coupling preservation is judged important |
| Rejected              | C (intra-pool, semantic break too sharp), E (defer, F1 not addressable transitively), F (cost) |

Pending user assent to Option A, the next session should:

1. Land the implementation in `ree-v3/ree_core/policy/structured_curiosity.py`
   + `ree-v3/ree_core/agent.py` per section 4's specification.
2. Add config knobs `curiosity_novelty_source` and
   `curiosity_visitation_buffer_len` to `REEConfig.from_dims()`.
3. Add contract test in `tests/contracts/test_mech_314_curiosity.py`
   covering bit-identical OFF, visitation buffer population gated by
   MECH-094, and per-candidate spread on harm-free episodes.
4. Queue V3-EXQ-NEW-1 substrate-readiness diagnostic.
5. After V3-EXQ-NEW-1 PASS, queue V3-EXQ-590b.
6. After V3-EXQ-590b PASS, run the registry / plan-doc / substrate-
   queue updates listed in section 7.
