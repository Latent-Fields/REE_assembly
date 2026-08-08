# Failure Autopsy: V3-EXQ-898 (SD-016 leg-A retest -- Path 3 tagger under the SD-070 encoder fix)

**Date:** 2026-08-08
**Scope:** single
**Status:** confirmed
**Target:** `v3_exq_898_sd016_lega_encoder_fix_retest_20260808T101631Z_v3` (queue V3-EXQ-898)
**Claim tagged:** none in the manifest (`claim_ids: []`, diagnostic purpose, matching the
V3-EXQ-418g/418m precedent for this exact acceptance-test shape). This autopsy targets **SD-016**
by prose/routing, not by manifest tag -- see "Note on recurrence tooling" below.

---

## 1. Facts

**dry_run check:** confirmed NOT a dry run (`check_dry_run_citations.py`: 0 dry cited, 1 clean).
**Recording provenance:** `validate_recording.py` reports 0 always-core gaps -- `recording_schema`,
`substrate_hash`, `machine`/`machine_class`, `elapsed_seconds`, `config`, `seeds` all present and
complete.

**Manifest.** `experiment_purpose: diagnostic`, `outcome: FAIL`, `evidence_direction: diagnostic`,
`interpretation.label: sd016_lega_tagger_insufficient_under_trained_encoder` -- the script's own
documented FAIL branch (see script excerpt below), not a manual read.

**Readiness preconditions (the "does the fix actually take" check) -- all 12 (2 arms x 3 seeds x
2 preconditions) MET, with wide margin, not marginal:**

| Precondition | Threshold (direction) | Range measured (both arms, 3 seeds) |
|---|---|---|
| `world_encoder_weights_moved` | >=1.0 (lower bound) | 5.0 (all 6 cells -- clean, not borderline) |
| `z_world_spread_lift` | >=1.3 (lower bound) | 3.53 -- 5.20 (2.7x -- 4.0x the floor) |

`n_seeds_ready: 3/3`. This matters because 418m (the prior autopsy on this exact substrate)
could **not** distinguish "tagger insufficient" from "z_world has nothing to select on" -- the
encoder was never meaningfully trained there. Here the positive control (`z_world_spread_lift`)
lands at the SAME magnitude V3-EXQ-783 independently measured for this identical SD-070 recipe
(contrast_ratio 1.7-1.9x), so the encoder fix is confirmed to actually take, on THIS run's own
apparatus, not merely asserted by reference to a different run.

**Acceptance checks -- C2 clean pass, C1/C1b clean fail, on every ready seed:**

| Criterion | Load-bearing | Result | Detail |
|---|---|---|---|
| C2 (control): OFF `sel_entropy_mean` > 2.65 | yes | **PASS** 3/3 seeds | OFF measured **2.7725870609 -- 2.772587299** across all 3 seeds -- indistinguishable from `ln(16) = 2.772588722` to 5 decimal places. The saddle is reproduced exactly, confirming the ablation isolates the tagger and the substrate is otherwise consistent with the 418-family. |
| C1 (primary): ON `sel_entropy_mean` < 2.5 | yes | **FAIL** 0/3 seeds | ON measured 2.7428 (seed 43) / 2.7461 (seed 44) / 2.7628 (seed 42) -- all within 0.03 of the OFF saddle, nowhere near the 2.5 threshold. |
| C1b (anti-degeneracy): ON `sel_context_divergence` > 0.1 | yes | **FAIL** 0/3 seeds | ON measured 0.0039 (seed 42) / 0.0513 (seed 43) / 0.0112 (seed 44) -- an order of magnitude below the 0.1 target on 2/3 seeds, and still well short on the best seed. |

`overall_pass: false`. `criteria_non_degenerate: {C1: true, C1b: true, C2: true}` -- the
script's own comment is explicit and correct on why: non-degeneracy is established by the
readiness gate (a criterion cannot pass here for the "z_world is constant" reason that would
make it vacuous, because the readiness preconditions already proved z_world varies on this
cell's own trained encoder).

**p0a_holdout diagnostics** (not gating, but corroborating): both arms' encoders decode
hazard/resource presence and distance at `balanced_accuracy` 0.95-0.99 (mean_lift ~0.55-0.57)
from a held-out probe -- the trained z_world genuinely carries retrievable structure. The
bottleneck is not "the encoder learned nothing"; it is "the tagger cannot select on what the
encoder learned."

**Script.** `ree-v3/experiments/v3_exq_898_sd016_lega_encoder_fix_retest.py`
(commit `46fc4f78baa4f6d0e1038cdd32f175aa66dac48f`). 2 arms (A0_OFF legacy q.k attention, A1_ON
Path-3 feedforward tagger) x 3 seeds [42,43,44]. Per-cell: P0a encoder warmup (SD-070 recipe,
world_dim=128, matching V3-EXQ-783's D128_TRAINED config) -> readiness gate -> P1 (E1-only
training on `z_world.detach()`, phased -- the encoder optimiser is never stepped in P1, a
correction relative to 418g/i/m which trained E1+encoder jointly). The script's own docstring
states the routing explicitly in advance:

> "C1/C1b FAIL with C2 PASS -> the encoder fix does not, by itself, let Path 3 clear
> selectivity; route to /failure-autopsy (tagger capacity / training-signal under a
> genuinely-varying z_world, a strictly narrower question than the 418m result, which could not
> distinguish 'tagger insufficient' from 'nothing to select on')."

That is exactly the observed outcome, and exactly this autopsy's job.

**Queue entry** (`ree-v3` commit `46fc4f7`, `claim_id: SD-016`, priority 20). Note field: "GOV-REUSE-1:
checked V3-EXQ-783 (PASS, Q-002/SD-031) for this exact readout -- not recorded there (scoped to
encoder contrast only, never read back onto SD-016 own criteria, per claims.yaml)." Chip
`chip-20260808-sd016-leg-a-retest` (already resolved `done` per WORKSPACE_STATE.md, prior
session).

**Expected vs observed.** Expected (per claims.yaml's own `what_would_answer` text for SD-016
leg A, written before this run existed): re-run the 418g/418m-shaped test under an encoder
config already shown to raise z_world contrast, and see whether retrieval selectivity emerges.
Observed: the encoder fix works (confirmed on-apparatus, not by reference), but selectivity does
not emerge -- **C2 passes cleanly, C1 and C1b fail cleanly.** This is the textbook "negative
control passes, discrimination fails" fingerprint, but critically it is happening on a
substrate that this run itself proves has non-trivial cross-context structure to select on.

## 2. Claim-layer mapping

**SD-016** (`claim_type: design_decision`, `status: implemented`, `epistemic_category:
substrate_ceiling`, `depends_on: [SD-005, SD-010, ARC-035]`). The claim text asserts E1 must
expose a z_world-only cue-indexed query path producing an action-affordance bias and a terrain
precision weight. This is an *architectural* assertion (the pathway should exist) already
`status: implemented`. This run does not test whether the pathway should exist -- it tests
whether the CURRENT selection-mechanism implementation inside that pathway (Path-3 feedforward
tagger) achieves the retrieval-selectivity property the architecture requires.

**claims.yaml's own text already anticipated this exact retest as the decisive leg-A
instrument**, and explicitly states the non-degeneracy bar this run had to clear before
attributing a FAIL to the selection mechanism rather than to z_world: "must independently
confirm... that the environment/encoder configuration under test actually clears cross-context
z_world separation before attributing a pass or fail to the selection mechanism itself." This
run clears that bar (readiness gate, wide margin, on-apparatus). So per the claim's own stated
standard, **this FAIL legitimately attributes to the selection mechanism, not to z_world
non-variance** -- a materially different, narrower reading than 418m could support.

**A 2026-08-07 governance note already on this claim entry instructs exactly this autopsy**:
"Flagged for /failure-autopsy to produce an enrichment recommendation targeting the SELECTION
mechanism question above, rather than routing here inline from the ceiling stamp alone." That
is the deliverable below (Section 5 / routing).

**Did the test let the claim express itself?** Yes for the narrow retrieval-selectivity
sub-question (leg A) -- a fair, well-controlled, non-degenerate test. No conclusion is drawn
here about leg B (downstream exploitation by E2/E3), which remains untested and separately
gated (cue_action_proj wiring, SD-055 differentiable CEM) per claims.yaml.

## 3. Biological-reference triage

**Closest mammalian reference:** hippocampal indexing / pattern separation -- dentate gyrus
sparse coding via lateral inhibition, CA3 competitive/autoassociative retrieval (Marr 1971;
O'Reilly & McClelland 1994 CLS-adjacent competitive-learning framing). The functional job SD-016
assigns to the tagger (given a context cue, select which of several stored associations is
relevant) is structurally the same job biological pattern separation performs: turn a
continuously-varying input into a sparse, context-selective output.

**Is the REE mechanism a faithful translation or a formal-definition import?** A formal-definition
import. The Path-3 tagger (like the q.k attention path before it) is a plain feedforward
network trained end-to-end via downstream task losses (`terrain_loss`, `cue_action_loss`) with
**no local competitive dynamics** (no lateral inhibition, no k-winner-take-all, no explicit
sparsification pressure) and **no training objective that directly rewards context-CONDITIONED
divergence**. Biological pattern separation does not wait for a downstream task loss to demand
sparsity -- it is a structural property of the circuit (sparse activation ratios, competitive
inhibition) that exists independently of what the retrieved content is later used for.

**Convergent evidence this is a structural gap, not a one-off tuning failure.** Three
independently-designed selection mechanisms have now hit the identical uniform saddle
(`ln(16) = 2.7726`) under three different training regimes:

| Attempt | Mechanism | Training signal | Result |
|---|---|---|---|
| 418d/e/i (Path 1) | q.k attention + auxiliary diversification loss (weights 0.5/1.0/2.0/5.0) | Explicit population-level slot-diversity loss | C1 attention-entropy FAIL at every weight (`2.7724-2.7726`); C2 slot-diversity (population-level) DID pass at high weight |
| 418m (Path 3, untrained encoder) | feedforward tagger | `terrain_loss` only, no dedicated signal | C1 FAIL 0/3, C1b FAIL 0/3, entropy moved a cosmetic 0.019 off ceiling |
| **898 (Path 3, SD-070-trained encoder)** | feedforward tagger | `terrain_loss` only, no dedicated signal | C1 FAIL 0/3, C1b FAIL 0/3, even with z_world now confirmed varying |

The one attempt that used an *explicit* differentiation-promoting loss (Path 1's diversification
loss) achieved population-level slot diversity but was never measured against CONTEXT-conditioned
divergence (C1b did not exist as an instrument yet at that point in the lineage) -- so **no
tested mechanism has ever been given a training signal that specifically rewards the
safe-vs-dangerous selection distributions differing from each other**, as opposed to differing
from uniform in aggregate. That is a plausible, and currently untested, root cause.

**Lit status: absent for this specific sub-question.** `evidence/literature/targeted_review_sd_016/`
exists but its 3 entries (Bechara 1999 anticipatory SCR, Dunn 2005 somatic-marker critique,
Lichtenberg 2017 BLA-OFC cue-expectation) all address the **downstream valuation** side of
SD-016 (leg B: does retrieved content get used behaviourally) -- none address the **retrieval
selection/indexing mechanism itself** (leg A, this run's question). `targeted_review_hippocampal_subfield_architecture`
exists but its entries (McClelland 1995 CLS theory, Lengyel 2008 hippocampal Dyna, Kumaran 2016
CLS update) are about memory consolidation and replay, not competitive pattern-separation
dynamics for indexing/retrieval selection specifically. **No existing lit entry grounds the
mechanism this autopsy is now recommending as a candidate fix** (competitive/local
retrieval-indexing dynamics). This is a genuine gap, not a refinement of existing coverage.

**Does the failure resemble a missing biological dependency?** Yes: biological pattern
separation depends on local competitive/inhibitory circuitry that has no counterpart in the
current substrate. The substrate has an input that varies (proven this run) and a differentiable
function that could in principle learn to select on it, but nothing in the training signal or
architecture supplies the competitive pressure that makes non-uniform selection the preferred
solution over the uniform-mixing local optimum the loss landscape apparently favours (C2's exact
`ln(16)` reproduction across every OFF cell, to 5 decimal places, is itself evidence that
uniform selection is a genuine, stable attractor of this loss landscape, not merely
"unconverged").

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened (selection-mechanism sub-question only) | SD-016's architectural assertion is untouched; the current Path-3 implementation does not achieve required selectivity even under a fair test |
| Biological reference | partial | correct target mechanism identified (hippocampal indexing/pattern separation) but never previously named as a lit-pull target for SD-016's selection sub-question |
| Developmental / dependency prerequisites | present | SD-070 (encoder fix) is landed and validated on this apparatus, wide margin |
| Implementation completeness | partial | tagger exists structurally (a differentiable function from z_world to slot logits) but has no training objective or architecture demanding context-conditioned divergence -- symbol of the mechanism, not its functional role |
| Environment adequacy | adequate | readiness gate confirms z_world genuinely varies across contexts on this apparatus |
| Measurement adequacy | adequate | two load-bearing instruments (entropy + context-divergence) plus a clean control, non-degeneracy independently established by the readiness gate, not assumed |
| Integration adequacy | isolated | leg A only; leg B (downstream E2/E3 exploitation) remains untested and separately gated |
| Scale / capacity | likely insufficient, untested directly | random-init feedforward MLP given only 40 P1 episodes and an indirect, weak downstream gradient; never tested against a larger budget or an explicit competitive/sparsifying architecture |

**Recording-debt vs measurement-debt:** neither applies here -- all decisive readouts
(`sel_entropy_mean`, `sel_context_divergence`, the readiness preconditions) were both computed
AND recorded. This is a genuine measurement result, not a recording gap.

**Epistemic category recommendation:** `substrate_ceiling`, but explicitly **relocated**, not
repeated. 418m's `substrate_ceiling` reading was about the encoder (z_world does not vary).
This run's `substrate_ceiling` reading is about the training signal available to the selection
mechanism (nothing tested has ever rewarded context-conditioned divergence specifically). Per
CLAUDE.md's guidance on conditional prior categories: 418m's own condition for revisiting
("revisit ONLY after (a) z_world cross-context separation is demonstrated AND (b) under
separated z_world, slot selection is proven semantically arbitrary") has (a) now satisfied by
this run, and this run's own evidence bears directly on (b) -- see Section 5.

## 5. Learning extracted and repair pathway

**Learning extracted:**
1. The SD-070 encoder fix, read back onto SD-016's own criteria for the first time (per
   claims.yaml's explicit request), genuinely restores cross-context z_world variance on this
   apparatus -- not merely by reference to V3-EXQ-783's different apparatus.
2. Retrieval selectivity still does not emerge, and the FAIL now cleanly attributes to the
   selection mechanism (per claims.yaml's own stated non-degeneracy bar).
3. Across three independently-designed selection mechanisms and three different training
   regimes, none has ever been given a training signal that specifically rewards
   context-CONDITIONED divergence (as distinct from population-level slot diversity, which one
   of them did achieve). This is a positive, actionable finding, not a dead end.
4. `SD-016`'s `substrate_queue.json` entry is stale: it still describes the 2026-04-28
   "env-entropy precondition" diagnosis, superseded by 418j/k (environment enrichment does not
   help) and now by this run (the encoder-level fix, SD-070, does help -- the gap has moved to
   the selection-mechanism training signal).

**Node classification** (work-graph debt vocabulary): `complex (probe-gated) / puzzle (known
rules)`. The frame is well-posed (retrieval selectivity is the target, the substrate now
supplies a genuinely-varying input) but the deciding fact -- WHICH of several plausible fixes
actually breaks the saddle -- is missing. >=2 live rival hypotheses -> GOV-FANOUT-1 portfolio,
not a single sequential re-pose.

**Live hypotheses (fan-out, three design axes):**
- **H1 (drive/objective axis):** No tested mechanism has been given an explicit
  context-CONDITIONED differentiation objective. Path 1's diversification loss rewarded
  population-level slot diversity, not the safe-vs-dangerous divergence C1b actually measures.
  Candidate probe: add an auxiliary loss term directly maximising `sel_context_divergence`
  (or an equivalent context-contrastive objective) during P1, on top of the now-varying
  SD-070-trained encoder.
- **H2 (representation axis):** The 16 undifferentiated slots may be the wrong retrieval unit --
  418m's own prior autopsy proposed hippocampal event/state/outcome-node indexing
  (MECH-044/ARC-006/007/MECH-267) as the alternative. Checked this session: all four remain
  `status: provisional`, unbuilt -- this is a longer-horizon leg, not a cheap probe, and should
  be informed by the recommended lit-pull before committing to a build.
- **H3 (algorithm axis):** The tagger is a soft, end-to-end differentiable gate with no
  competitive/sparsifying mechanism. Candidate probe: replace the soft feedforward gate with a
  hard/competitive selection mechanism (Gumbel-softmax with annealed temperature, or explicit
  top-k gating) that structurally forces sparsification rather than hoping gradient descent
  discovers it.

**Note on recurrence tooling (transparency, not a fix requested here).** `granularity_debt_cluster.py
SD-016` and the re-derive-brake counting recipe both return 0 hits for SD-016, because this
target's `claim_ids` is `[]` (matching the 418g/418m diagnostic-purpose precedent, and matching
the manifest itself). Mechanically, this autopsy is invisible to the automated
recurrence/re-derive-brake counters even though it is, by content, the second `substrate_ceiling`
reading circling this exact substrate. I am treating this AS a re-derive-brake case IN SPIRIT:
**I am explicitly refusing to recommend a same-shape re-queue** (e.g., a Path-4 tagger variant
with no new training signal) and routing instead through a literature commission and a
discrimination portfolio, per the brake's intent. This is a known, accepted characteristic of
the diagnostic-purpose `claim_ids=[]` convention, not something I am changing unilaterally here.

**Routing (three-part, all confirmed by the user at the Step 8 gate):**

1. **`/lit-pull`** commission: hippocampal competitive/local retrieval-indexing mechanisms
   (dentate gyrus sparse coding, CA3 pattern separation/completion, lateral inhibition /
   winner-take-all dynamics) as the biological reference for what a fix mechanism should look
   like. Target: `targeted_review_sd_016` (new entries) or a new `targeted_review_hippocampal_pattern_separation`
   -- lit-pull's own scoping call.
2. **`/queue-experiment`** GOV-FANOUT-1 portfolio: H1 (drive) and H3 (algorithm) as near-term
   diagnostic probes; H2 (representation) informed by the lit-pull result before committing to a
   build, given its dependency claims are all unbuilt.
3. **`substrate_queue.json` amend** (below): correct the stale SD-016 entry metadata and append
   this run's `failure_record` entry.

**Draft `evidence_quality_note` for SD-016** (governance to apply, not written here):

> V3-EXQ-898 FAIL (2026-08-08, diagnostic, autopsy-confirmed): SD-016 leg-A retest under the
> SD-070 encoder fix (world_dim=128, matching V3-EXQ-783's D128_TRAINED recipe). Readiness
> preconditions (world_encoder_weights_moved, z_world_spread_lift) cleared on all 3 seeds with
> wide margin (2.7-4.0x the floor) -- the encoder fix genuinely takes on this apparatus, resolving
> 418m's open ambiguity. C2 control passed cleanly (OFF reproduces ln(16)=2.772589 exactly, 3/3
> seeds). C1/C1b (load-bearing) both FAILED cleanly on all 3 seeds (ON entropy 2.743-2.763 vs
> <2.5 needed; ON context-divergence 0.004-0.051 vs >0.1 needed). Per claims.yaml's own stated
> non-degeneracy bar, this FAIL now legitimately attributes to the selection mechanism, not to
> z_world non-variance -- a narrower and more actionable finding than 418m could support.
> `epistemic_category` remains `substrate_ceiling`, relocated from the encoder (418m's reading)
> to the selection-mechanism training signal: no tested mechanism (q.k attention, feedforward
> tagger, or Path-1's diversification loss) has ever been given a training objective that
> specifically rewards context-CONDITIONED divergence, as distinct from population-level slot
> diversity. Routed to a 3-hypothesis GOV-FANOUT-1 discrimination portfolio (drive / algorithm /
> representation axes) informed by a lit-pull commission on hippocampal
> pattern-separation/competitive-indexing mechanisms, per `failure_autopsy_V3-EXQ-898_2026-08-08`.
> `pending_retest_after_substrate: true`.

## 6. `substrate_queue.json` amend (drafted, not applied here)

Current entry is stale (`last_seen_session: governance-cycle-20260606T0431Z`, i.e. immediately
after 418m, never updated for SD-070/783/898). Recommended amend:

- `status`: `parked_pending_env_entropy_precondition` -> `parked_pending_selection_mechanism_fix`
  (the environment/encoder precondition is now satisfied; the gap has moved downstream)
- `blocked_on`: replace "z_world cross-context separation precondition not yet satisfied..."
  with "selection mechanism (Path 3 tagger, or any successor) has no training signal rewarding
  context-conditioned divergence; z_world separation itself is confirmed satisfied as of
  V3-EXQ-898 (2026-08-08)"
- `implementation_hint`: append a note that the 2026-04-28 env-entropy diagnosis is superseded
  (per claims.yaml's own text, confirmed by 418j/k and by this run) and that the open question is
  now which fix mechanism (H1/H2/H3 above) restores selectivity
- `failure_record`: append this run (see JSON `recommended_substrate_queue_entry.failure_record_entry`)
- `validation_experiment` / `validation_precondition`: update once the GOV-FANOUT-1 portfolio is
  queued

## 7. User-confirmed disposition

At the Step 8 interactive gate, the user confirmed:
1. The diagnosis read: training-signal gap, not claim falsification (`substrate_ceiling`,
   relocated/narrowed, not a demotion of SD-016).
2. The routing: lit-pull + GOV-FANOUT-1 portfolio + `substrate_queue.json` amend, all three.

Both `AskUserQuestion` outcomes logged to `RECOMMENDATION_LOG.jsonl` per CLAUDE.md's
recommendation-agreement ledger requirement.
