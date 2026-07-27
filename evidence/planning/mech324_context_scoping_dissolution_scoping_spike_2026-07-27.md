# MECH-324 -- CONTEXT-SCOPING OF DISSOLUTION: scoping spike

**Date:** 2026-07-27
**Session:** `optimistic-ellis-4357c6`
**Question owned:** the open Q-claim *"CONTEXT-SCOPING OF DISSOLUTION (blocks falsifier (b), renewal)"*
registered on MECH-324 by the 2026-07-27 dissolution-with-retention structural correction
(REE_assembly `0ffe3da26a`).
**Output class:** recommendation only. No status / confidence / `live_status` / `v3_pending`
change to MECH-323, MECH-324 or ARC-071.

---

## 1. The question as registered

> Is dissolution scoped to the `initiation_set` under which the variance was observed, or applied
> to the chunk globally? Formation is already context-conditioned via `initiation_set`, so the
> conservative-looking choice (global dissolution) is the one that makes renewal structurally
> impossible. Not a free parameter -- it decides whether a whole class of biological behaviour is
> expressible.

Falsifier (b) as registered: *FALSIFIED IF a chunk dissolved under context A fails to fire under
context B where its outcome statistics never degraded.*

## 2. Answer, in one line

**Yes on the design -- dissolution must be context-scoped, and "leave it global" is a substantive
commitment against the biology exactly as the Q-claim warns. But the build does NOT route to
`/implement-substrate` yet, because the premise the question rests on is false of the substrate:
formation is not context-conditioned either. Both halves are context-blind, and building the
scoped dissolution gate now would install a silent no-op that reads as renewal-capable.**

The Q-claim is therefore **answered in principle and re-gated in practice**. It stops being a
design choice between two implementable options and becomes a downstream consumer of an unbuilt
MECH-323 registered item.

## 3. Finding 1 -- `initiation_set` is declared but never populated

`ChunkedPrimitive.initiation_set` exists as a field
(`ree-v3/ree_core/policy/policy_chunking.py:283`), typed `frozenset`, defaulting to `frozenset()`.

- `ChunkAccumulator.mint()` accepts `initiation_set: Optional[frozenset] = None` (:656) and
  stores `frozenset()` when not passed (:661).
- **Both** call sites of `mint()` in the entire repo omit it: the MECH-322 replay path (:741) and
  the MECH-323 formation path (:1145).
- Repo-wide grep for `initiation_set` outside `policy_chunking.py` returns **zero** hits. Nothing
  reads it, and no selection, proposal or gating path consults it.
- The module's own docstring already concedes this: *"Empty set = unrestricted (the permissive
  default used by the substrate-readiness path, where context bucketing is not yet wired)"* (:251-253).

MECH-323 lists *"The initiation_set inference rule (collect the contexts in which the
accumulator's R_min executions occurred; predicate over discriminating context features)"* under
its **registered content**, and separately carries an open Q-claim on the *precision* of that
inference. The rule was registered; it was never built.

**Consequence for the Q-claim's framing.** The registered text asserts an asymmetry -- formation
context-conditioned, dissolution context-blind. In the substrate there is no asymmetry: **both are
context-blind.** Formation merely carries a reserved field. The renewal falsifier is blocked one
level further upstream than the Q-claim locates it.

## 4. Finding 2 -- the whole ARC-071 seam is context-free by signature

This is not a one-line change to the variance gate. Every entry point into the chunking operator
is context-free:

| Entry point | Signature | Context? |
|---|---|---|
| `ChunkAccumulator.record_step` | `(action_class: int, hypothesis_tag: bool)` | none |
| `PolicyChunking.note_outcome` | `(outcome_signal: float)` | none |
| `ChunkLibrary.note_real_execution` | `(sequence, outcome_variance: float)` | none |
| `ChunkLibrary.tick_maintenance` | `(variances: Dict[Tuple[int,...], float])` | keyed by sequence |
| `REEAgent.note_chunk_outcome` | `(outcome_signal: float)` | none |

Chunk lifecycle state is a **single scalar per chunk** (`ChunkedPrimitive.state`,
`selection_weight`). Context-scoped dissolution requires state to become a **map** from context
bucket to lifecycle state, plus a context argument threaded through all five entry points above
and the `agent.py` call sites (:7880, :8147). That is a seam change, not a gate tweak, and it
changes the `get_state()` shape that contracts and manifests read.

Note the context *is* available at the seam -- `record_step` is called inside `select_action`,
where `z_world` and the full latent state are in scope. Nothing threads it. This is a wiring gap,
not an availability gap. Which matters, because it makes the naive build look easy.

## 5. Finding 3 -- THE TRAP: the naive build is a silent no-op that reads as renewal-capable

Two layers, and the second is the load-bearing one.

**Layer 1 (obvious).** Scoping dissolution to `initiation_set` while `initiation_set` is
universally `frozenset()` is a no-op. Every chunk shares one empty context, so every dissolution
is still global -- while a flag named for renewal is on and a code path for it exists. This is the
inert-flag failure class the repo has been bitten by repeatedly (`use_iterative_inference` with
`inference_settle_iters=1`; `REEConfig.from_dims` swallowing unknown kwargs).

**Layer 2 (the one that would survive a code review).** Populating `initiation_set` from raw
`z_world` does not fix it, and there is a **direct, already-measured precedent** for that:
`ree-v3/ree_core/policy/candidate_rule_field.py` implements exactly the primitive an
`initiation_set` inference rule would need -- `_context_bucket()` (:408), a sign pattern over the
leading 8 dims of the context vector, used as a recurrence key. Measured 2026-07-22 on the
V3-EXQ-669b Stage-0 nursery (155-160 contexts, seed 101, alpha_world=0.9), recorded at
`candidate_rule_field.py:255-274`:

```
raw world_obs   pairwise cosine min 0.3000   (60.2% of pairs < 0.8)   [control]
z_world         pairwise cosine min 0.9767   ( 0.0% of pairs < 0.8)
e2 ctx          pairwise cosine min 0.9426   ( 0.0% of pairs < 0.8)
```

`z_world` sits in a ~0.98-cosine common-mode cone (SD-008 z_world under-differentiation), so the
sign-pattern bucket is common-mode dominated and **collapses to `n_context_buckets = 1`**.

So a renewal experiment built on a raw-`z_world` initiation set would run against a substrate in
which **context B does not exist**. Every chunk dissolved "under context A" would be dissolved
under the only context there is. The run would return the registered FALSIFIED verdict --
*"a chunk dissolved under context A fails to fire under context B"* -- **by construction of the
instrument**, and that verdict would enter the ledger against Bouton 2012's biology rather than
against REE's context representation. This is the same class as the V3-EXQ-654b/654d autopsies,
which read a structural 1-bucket collapse as retire-churn.

**A renewal FALSIFIED verdict is uninterpretable until the bucket count is known to exceed 1.**

## 6. The route through -- SD-078, and what it inherits

The collapse has a solved fix in the same module: **SD-078** (`cue_centering`) subtracts a slow-EMA
common-mode baseline before every cue comparison. Measured effect on the same stream: **1 bucket
raw -> 20 buckets centered**; 1 rule -> 8 rules; `max_pairwise_rule_dist` 0.0000 -> 1.2581.

Two cautions carried from that entry, both explicit in the source:

- SD-078 is `candidate_substrate_landed` -- **built, not experimentally validated** -- and its
  flag is **default OFF** (`cue_centering: bool = False`). Claim status is not flag default.
- The two mitigations aimed at the same symptom that were measured **ineffective** are deliberately
  left in place and must not be re-tuned as the fix: raising `mature_mint_block_threshold` to 0.8
  does not clear a 0.94 floor, and `crf_context_from_e2_world_forward` routes to a context carrying
  the same offset.

So context-scoping of dissolution **inherits SD-008 z_world under-differentiation as its root
blocker** -- the same root as the monostrategy representation ceiling. It is not an independent
design choice about the dissolution gate.

## 7. Work-graph classification

Not `complicated (buildable)`. The node is **`puzzle (known rules)`**: the rules are known
(SD-078's centering method plus its measurement protocol), and one missing fact gates the build --

> **Over the chunking regime's own context stream, how many distinct centered-`z_world` buckets
> occur, and do the real executions of a single chunk distribute across more than one of them?**

If that number is 1, renewal is inexpressible whatever the dissolution gate does, and the correct
move is to say so on the falsifier rather than to build a gate that cannot be exercised. If it
exceeds 1, the build becomes `complicated (buildable)` and the MECH-323 initiation-set inference
rule (with its own registered precision Q-claim, suggested ">=80% of the variance across R_min
execution contexts") is the thing to build -- **before** the dissolution gate, not after.

Note the bucket count must be measured on the **chunking** stream specifically, not inherited from
the 669b nursery number: the 155-160-context nursery is a different regime, and chunk formation
requires R_min repetitions of a *stable* sequence, which plausibly selects for context homogeneity
independently of the common-mode problem. That is precisely why it is a puzzle and not an
assumption.

## 8. Recommendation

1. **Do not route to `/implement-substrate` for context-scoped dissolution now.** The build order
   is inverted relative to the Q-claim's framing: the blocker is MECH-323's unbuilt initiation-set
   inference and SD-008's z_world cone, not MECH-324's gate.
2. **Do not queue falsifier (b) renewal.** Its FALSIFIED verdict is uninterpretable until the
   bucket-count puzzle is resolved, and entering it into the ledger would misattribute an
   instrument artefact to the biology.
3. **Falsifier (a) rapid reacquisition is unaffected and remains the correct next move.** It is
   context-free by construction -- it re-presents the same regime rather than changing context --
   and the retention substrate it needs (`use_chunk_dissolution_retention`,
   `chunk_reacquisition_repetition_factor`) landed 2026-07-27 under session
   `cranky-blackburn-d11b32`. Verified present in the working tree at spike time:
   `ChunkState` dormancy, `ChunkedPrimitive.reacquisition_repetitions`, `ChunkLibrary.revive()`,
   `PolicyChunking._attempt_reacquisition()`, `reacquisition_min_repetitions`. Confirmed **not yet
   queued** -- zero chunking entries in `ree-v3/experiment_queue.json`.
4. **The cheap next probe** is the bucket-count measurement in section 7, run over the chunking
   context stream with `cue_centering` both OFF and ON. It is a diagnostic, not an experiment: it
   measures the instrument, not the hypothesis.

## 9. Transfer limits (carried, load-bearing, not boilerplate)

Carried verbatim in force from the MECH-324 registration. The sources for the retention correction
are **rodent T-maze procedural learning** (Barnes et al. 2005) and **single-response operant
contingencies** -- a rat pressing a lever for food (Bouton et al. 2012). In both, the extinguished
object is much simpler than a composed chunked primitive, and REE's outcome dimension is an
E3-score-receipt over policy primitives rather than a food reward.

**Whether a MULTI-ELEMENT COMPOSED SEQUENCE shows context-dependent extinction with the same
asymmetry is EXTRAPOLATION, NOT EVIDENCE.** This bears on the present question specifically and
not only on the falsifiers: the entire argument that dissolution *ought* to be context-scoped rests
on Bouton's demonstration that instrumental extinction installs new **context-dependent** learning
alongside the old. That demonstration is at the single-response level. A chunk is by construction
not a single response, and it is an open empirical question -- not answered by either source --
whether the context-dependence of extinction survives composition, or whether a composed sequence
extinguishes context-independently because its elements were acquired across heterogeneous
contexts. Section 7's bucket-count puzzle is, incidentally, the same measurement that would begin
to tell us: a chunk whose R_min formation executions span several context buckets is already a
counter-example to the naive single-context reading.

## 10. Provenance

- Substrate read at `ree-v3` working tree, 2026-07-27T06:47Z (`main`, with the
  `cranky-blackburn-d11b32` retention work present and uncommitted).
- `candidate_rule_field.py` measurements are quoted from the in-source record at :255-274, dated
  2026-07-22, V3-EXQ-669b Stage-0 nursery. **Not re-measured by this spike.**
- No experiment was run. No substrate file was modified. `policy_chunking.py` was **read only** --
  it was under an active TASK_CLAIMS claim by `cranky-blackburn-d11b32` for the whole session.
