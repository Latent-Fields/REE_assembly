# Failure autopsy -- V3-EXQ-1010 (diagnostic adjudication)

- **Target:** `v3_exq_1010_zworld_overcapacity_decoder_sweep_20260909T195348Z_v3` (queue `V3-EXQ-1010`)
- **Outcome:** PASS -- `experiment_purpose: "diagnostic"`, self-route `H-F-confirmed`
- **Scope:** single. **Claims:** none (`claim_ids: []`); `bears_on` INV-088 / MECH-457
- **Question:** frozen-ledger `zworld_actor_adequacy_locus`, leg `H-F-content-discarded-at-encode`
- **Generated:** 2026-09-11T13:36:26Z  |  **Status: CONFIRMED** at the user gate 2026-09-11T13:58:15Z
- **Why an autopsy at all:** every `experiment_purpose: "diagnostic"` result needs a confirmed adjudication before governance acts on it, PASS or FAIL, flagged or not. The self-routed label is a hypothesis about what the run found, never a verdict.

---

## 1. Facts -- what ran and what it measured

**Dry-run gate (Step 2a), run before any metric was read.** `check_dry_run_citations.py` on the run_id and the queue_id: 0 dry cited, 0 dry in named families, 0 ambiguous, 1 clean, exit 0. The manifest carries `dry_run: false` and a non-dry `run_id` shape, so `_is_dry_run()` is false on both legs (the GOV-DRY-1 requirement -- not a raw field read). Criterion reachability: the driver's dry path sets `DRY_RUN_SEEDS` below `SEED_MAJORITY=2`, which forces `seeds_sufficient` False and makes **every** verdict branch structurally unreachable in a smoke, so a dry manifest of this driver could never be mistaken for this one.

**Recording provenance: complete.** `recording_schema` `rec/v1`, top-level `substrate_hash`, `substrate_commit` (`63aa9f2c`, clean, `main`), `machine`, `machine_class`, `elapsed_seconds` (92,211 s = 25.6 h), full `config`, explicit `seeds` `[42,43,44]`. **No recording gap** -- nothing this autopsy needed was missing from the manifest, which is why no part of the routing is "re-run it and record X".

**The design.** One thing is manipulated -- the decoder's capacity -- across five rungs spanning roughly 77,000x in action-path parameters (fitted linear 165 -> `mlp128` 21,381 -> `mlp512` 282,117 -> `mlp2048` 4,274,181 -> `deep2048x4` 12,666,885). Held fixed: representation, dataset, seeds, held-out episode split, standardiser, fit protocol, oracle labels. Four tracks, all read by the same ladder on the same stored steps:

| Track | What it is | Width |
|---|---|---|
| `rawfield_ceiling` | raw 25-dim resource field -- instrument positive control and gate (floor 0.60) | 25 |
| `ws250_pca` | train-split PCA of the encoder's **own** 250-dim `world_state` input -- calibration anchor (Guard 1) | **32** |
| `zworld_untrained` | the **same encoder architecture at random initialisation**, warmup skipped -- negative control | **32** |
| `zworld_off` | the frozen 978-OFF `z_world` -- **the subject** | **32** |

**DV:** held-out top-1 agreement between the decoder's argmax and the `local_view_greedy` oracle's discrete action. **Pre-registered verdict:** `best_agreement_over_capacity` (max over rungs, per track per seed) must clear **both** a 0.80 absolute bar and a 0.20 elevation over the strongest trivial predictor, on a seed majority (>=2 of 3).

**The numbers (all in-run).**

| Representation | seed 42 | seed 43 | seed 44 | mean | clears bar+elevation |
|---|---|---|---|---|---|
| raw 25-dim field | 0.9832 | — | 0.9735 (worst) | ~0.979 | instrument gate, green |
| **PCA-32 of the same 250-dim input** | 0.8836 | 0.8729 | 0.8763 | **0.8776** | **3/3** |
| **same architecture, random init** | 0.7155 | 0.6895 | 0.7084 | **0.7045** | 0/3 |
| **trained `z_world` (subject)** | 0.6839 | 0.6846 | 0.6656 | **0.6780** | **0/3** |
| trivial (prev-action) baseline | 0.5661 | 0.5803 | 0.5720 | 0.5728 | — |

Subject elevations at its own best rung: 0.1178 / 0.1043 / 0.0936, against a 0.20 floor. `n_seeds_clearing_at_some_capacity = 0`.

**Which criterion failed.** Four load-bearing criteria all **passed** (`C_verdict_arms_ready`, `C_guard1_anchor_protocol_sound`, `C_guard2_overcapacity_memorises`, `C_hf_adjudicated`). The one criterion reading false, `C_off_clears_at_some_capacity`, is non-load-bearing and **is the discrimination criterion** -- the subject fails a bar the anchor clears 3/3 at the same width under the same protocol. Its falsity is the scientific content, not an instrument failure.

---

## 2. Why the null is a content finding and not an artifact -- four independent exclusions

Each is measured in-run, and each closes a different escape route. This is the part that makes the verdict safe, so it is set out separately rather than summarised.

1. **Not an under-powered reader.** Guard 2: the same ladder on the same latent **memorises the training split at 0.9996 / 0.9998 / 0.9998** (floor 0.95). A decoder that fits the training labels essentially perfectly and still generalises to 0.68 is telling you about generalisable content in the representation, not about fit capacity.
2. **Not an unsound fit protocol.** Guard 1: the anchor's max-capacity-minus-consumer degradation is **-0.0196** worst seed, inside the -0.10 tolerance. Note the statistic is *max-capacity minus consumer*, deliberately not *best minus consumer* -- the latter is `>= 0` by construction and could never fire. The guard can fire and does not.
3. **Not a blind instrument.** Raw field decodes the oracle at 0.9735-0.9832 against a 0.60 floor; the oracle's rule on the true field self-agrees at 1.0 with `true_field_flat_window_frac` 0.0; the oracle clears the competence floor on every seed (45.75 / 49.7 / 48.7).
4. **Not an under-sampled map.** The saturation witness refits the `mlp512` rung on **half** the training rows: held-out cost is only **0.0200 / 0.0136 / 0.0356**, against a mean **0.122** gap to the bar. More data does not plausibly close it.

**And a second, reader-free witness corroborates.** At every subject rung the run separately decodes the 25-dim field and applies **the oracle's own argmax rule** with no learned action head anywhere in the path. It tops out at **0.6546 / 0.6623 / 0.6478** per seed (maximum at `mlp512` on all three) against those same trivial baselines -- the same ~0.08-0.12 margin the learned head gets. Two structurally different readers agree, which is what separates "absent" from "this particular reader could not find it".

---

## 3. Claim layer

`claim_ids` is empty **by design** -- correctly so. INV-088 and MECH-457 are `bears_on` relations; neither claim's mechanism is exercised by a frozen-representation decode, and re-attaching either would increment a brake counter on a run that tests neither. Both claims already carry `epistemic_category: standard` and `diagnostic_evidence_adjudicated: true`, and neither status moves.

The `bears_on` tokens `["INV-088","MECH-457"]` are reused **verbatim** from the 1002 and 1008 artifacts so the GOV-DIAG-1 chain advances rather than starting a fresh count of 1.

---

## 4. Biological-reference triage

**Closest reference:** DiCarlo-style ventral-stream manifold untangling -- a hierarchy whose *functional role* is to progressively flatten and separate behaviourally relevant variables so a simple downstream readout can use them. The biological existence proof is for the **class**: a trained sensory cascade makes task-relevant structure *more* linearly accessible than its own input statistics would. `lit_status: present` for this reference (entries already carried by the lineage).

**Is REE's z_world a faithful translation or a formal import?** It is a genuine translation attempt, not a formal-definition import -- which is why the divergence below is load-bearing rather than a definitional artifact.

**The divergence, measured rather than asserted.** In the reference, the cascade's *training* is what buys accessibility. Here training buys nothing: the trained latent sits **at or below its own architecture at random initialisation on 3/3 seeds** (`off_minus_untrained_best` = -0.0317 / -0.0049 / -0.0427). The divergence is not "REE untangles less well than a brain". It is that **REE's cascade does not untangle this variable at all relative to its own random init.**

**Does the failure look like a missing dependency of the reference mechanism?** Yes, and specifically: the reference's cascade is trained under pressure to *preserve and reformat its input*, and REE's observation->z_world path carries no such pressure. That is a discovered prerequisite, which is why this routes to a build rather than to a demotion.

**Honest statement of the effect size on the negative control.** The three paired differences are all negative but are 0.005-0.043, comparable to the seed spread within each track (best-over-capacity RANGE 0.0190 subject, 0.0261 untrained; SDs 0.0107 and 0.0135 -- given explicitly because 'spread' is ambiguous and this paragraph leans on it). The defensible claim is **"training is not better than random init on this axis; the point estimate is slightly worse"** -- not "training significantly destroys content". `n = 3` does not support the stronger version, and nothing in the routing needs it.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **n/a** | claim-free by design; `bears_on` only |
| Biological reference | **clear** | untangling reference present; divergence load-bearing and measured (sec. 4) |
| Dependency / developmental prerequisites | **present** | 89 preconditions, 0 red arms, 0 vacuous arms, every verdict arm green. Scope stated precisely: `zworld_encoder_trained_in_p0` is evaluated on the 5 `zworld_off` rungs only and `zworld_not_collapsed` on the 10 arms of the two z-tracks (correctly -- an arm with no encoder cannot have a trained one), and four specs carry a **global** worst-cell value replicated onto every arm rather than a per-arm measurement. x1002's inherited pattern, sound; recorded because "per arm on all 16" reads stronger than what is stored |
| Implementation completeness | **complete** | encoder genuinely trained: `n_latent_stack_changed` 7, `n_world_path_changed` 6, `n_world_encoder_changed` 4, `world_encoder_max_abs_delta` 0.293 -- against 0 / 0 / 0 / 0.0 on the untrained track; latent not collapsed (participation ratio 4.22-5.67); the reader is `x734.PPOPolicyNet` **itself**, not a look-alike |
| Environment adequacy | **adequate** | D3 hazard-free, oracle clears competence floor 3/3, and the decision is empirically determined by the observation (raw field decodes at 0.98) |
| Measurement adequacy | **adequate** | instrument gate + same-width anchor + same-architecture negative control + 5 capacity rungs + a reader-free second witness + saturation witness + per-rung divergence/collapse flags. **One flag actually fired** -- see below the table |
| Integration adequacy | **n/a** | frozen-representation read; no module interaction under test |
| Scale / capacity | **adequate, and bounded** | Guard 2 excludes an under-powered reader; saturation witness bounds under-sampling; residual uncovered space stated (feed-forward decoders only) |

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Reads from | Verdict |
|---|---|---|
| MECHANISM | Implementation completeness = `complete` | **established** |
| MEASURES | Measurement adequacy = `adequate` | **established** |
| ENVIRONMENT | Environment adequacy = `adequate` | **established** |
| **REE** | all three | **true** |

**A flag fired, and it is reported rather than passed over.** `guards.collapsed_witness_rungs` = `['ws250_pca/deep2048x4', 'zworld_off/deep2048x4']`. It is benign on two independent grounds: it fired on the **calibration anchor** as well as the subject, so it is a top-rung protocol property and not a subject-specific failure; and the reader-free witness's maximum sits at `mlp512` on all three seeds, so the collapsed rung never enters the reported statistic. `guards.diverged_rungs` is empty.

**Net classification: REE FAILED -- narrowly and precisely scoped.** All three non-REE buckets are genuinely excluded rather than merely unexamined, each with its own in-run positive control, and REE's observation->z_world encoding still did not deliver the predicted competence.

**The scope of that charge, stated explicitly** because an unscoped "REE failed" read off a claim-free diagnostic is exactly what GOV-FAILLOC-1 exists to prevent: it covers **one mechanism -- the observation->z_world encode at 32 dims on this rung -- and nothing else.** Not REE's architecture as a whole, not any claim in `claims.yaml` (the target is claim-free), not the competence-floor campaign's other roots. And the standard REE is held to is the weakest one available, set by the run's own control rather than by this autopsy: **parity with a task-agnostic PCA of the encoder's own input at the encoder's own width.**

**Recommended `epistemic_category`: `standard`.** Deliberately not `substrate_ceiling` -- that value sits in `_EPI_SUPPRESS_PROPOSAL` and additionally makes a claim not-v3-testable, and nothing here warrants starving INV-088 or MECH-457 of experiment lanes. The finding is that a named, buildable encoder change is owed, which is the *opposite* of a ceiling.

---

## 6. The read the manifest does not make -- and the one this autopsy withdrew

### 6a. The gap decomposes, and the decomposition names the build

**In THIS run**, best-over-capacity, the two comparators it carries both beat the trained latent **at every rung on 3/3 seeds**:

| Representation (250->32 unless noted) | best-over-capacity mean |
|---|---|
| raw 25-dim field (25) | 0.979 |
| PCA-32 of the same 250-dim input | **0.8776** |
| same architecture, random init | **0.7045** |
| **trained `z_world`** | **0.6780** |
| trivial (prev-action) | 0.5728 |

**The decomposition itself is computed entirely inside V3-EXQ-1008's own consumer-rung cells**, because that run carries a third comparator this one does not -- a random *orthonormal* 32-dim projection. V3-EXQ-1008 has **no capacity ladder at all** (`adapter_trunk_hidden: 128`, every arm single-rung), so its numbers are consumer-rung values and must not be mixed into a best-over-capacity series. Within that one run:

```
PCA-32          (fitted linear, variance-preserving) 0.8684
random orthonormal-32  (unfitted linear)            0.7725
untrained encoder net-32 (unfitted nonlinear)       0.6946
TRAINED z_world-32 (fitted, REE objective)          0.6686   <- LAST
```

- **-0.0959** -- what fitting a linear projection **for variance preservation** buys
- **-0.0779** -- what the encoder's **nonlinear architecture** costs at random init
- **-0.0260** -- what **REE's training objective** costs on top

Total **-0.1998**. The single largest term is a pressure **neither the architecture nor the objective contains**. That reframes the repair: not a better feature head, and not "objective vs architecture" -- **no bottleneck preservation pressure exists at all.**

> **Correction applied after the red-team pass.** The draft computed these terms as -0.106 / -0.067 / -0.027 by mixing 1008's single-rung random-orthonormal value into 1010's best-over-capacity series -- a category error, since 1008 has no ladder. Recomputed consistently inside one run, the signs, the ordering and the conclusion are unchanged; only the warrant is repaired. The draft's absolute "below a random orthonormal projection at **every** decoder capacity" is likewise withdrawn for that comparator -- it is a one-capacity result -- and retained, rung-verified 3/3, for the two comparators this run actually carries.

*Further caveat, stated rather than smoothed:* PCA is fitted while the random projections are not, so the -0.0959 term conflates "fitted" with "linear". This does not touch the conclusion, because the trained encoder **is** fitted and still loses to both unfitted projections.

### 6b. An argument this autopsy tested and WITHDREW -- recorded, not deleted

The draft argued that because V3-EXQ-1010 ran on **`darwin-arm64-py3.13`** while 1002 and 1008 both ran on **`linux-x86_64-py3.10`**, and the 978 warmup is re-run in-process through `e3_selector.py` (five live `torch.multinomial` call sites at substrate commit `63aa9f2`, and multinomial is the corpus's one documented cross-machine-class divergent op), the warmup must be an **independent draw** -- thereby supplying the second instance for `H-D-warmup-not-the-locus` that the 1008 autopsy explicitly declined to claim.

**Checked by measurement; it does not hold.** `zworld_participation_ratio`, 1008 -> 1010:

| track | seed 42 | seed 43 | seed 44 |
|---|---|---|---|
| OFF | 4.56505291002958 -> 4.565657594335131 | 4.222778806991767 -> 4.222780095432731 | 5.667190228544192 -> 5.665099767498349 |
| UNTRAINED | 7.492851658629209 -> 7.492853548294216 | 10.31264273380446 -> 10.312641567132374 | 10.011804177727937 -> 10.011799420895613 |

All six differ -- so **bit-identity is genuinely broken**. But the UNTRAINED track, whose construction contains no sampling at all, differs by ~1e-7 relative, and the OFF track by at most 3.7e-4. A different multinomial *category* would have sent the trajectory O(1%) away, not four decimal places. This is accumulated floating-point reordering, **not a re-draw**. H-D's registry entry needs no change: not a strengthening (there is still no independent instance), not a weakening (nothing contradicts it). Recorded so a later session does not re-derive the tempting version and bank it.

### 6c. What the machine-class change does cost, and what it unexpectedly buys

**Cost -- a provenance defect.** The driver docstring asserts that "the OFF latent this run reads is the same object 1002 and 1008 read", and separately corrects 1008 for wrongly claiming the machine classes differ, stating "IT DOES NOT -- both 1002 and 1008 declare `linux-x86_64-py3.10-torch2.12.0+cpu`." Both statements are true *of 1002 and 1008*; neither is true *of this run*, which declares `darwin-arm64-py3.13-torch2.12.0`. The bit-identity claim it rests on is false on 6 of 6 fingerprints. **Nothing downstream breaks** -- every threshold in the run is applied to in-run values, and the in-run reproduction band (0.60-0.75, measured 0.6626-0.6749) is what actually certifies the latent. Same family as `chip-20260908-exq1008-provenance-string`.

**Dividend, and it is larger than it first looks.** The OFF-latent shortfall reproduces to within **0.005** held-out agreement across **two simultaneous changes, not one**: a different OS, CPU architecture, Python and torch build, *and* the addition of `GRAD_CLIP_NORM` to the fit protocol (the driver says so explicitly, and it is visible in the anchor moving more than the subject did -- PCA `mlp128` seed 42: 0.8771 -> 0.8836). Given the corpus's documented cross-machine-class divergence hazard, an accidental cross-platform replication of a load-bearing null is worth banking rather than merely correcting.

---

## 7. Brake, granularity debt, diagnostic chain

**Re-derive brake (R1-R3, re-run 2026-09-11):** MECH-457 = **13**, INV-088 = **2** -- identical to what 978, 1002 and 1008 recorded. This target is **claim-free**, so the counter's `claim in target.claim_ids` test never reaches it and neither count moves. Both standing brakes remain fired, and this autopsy is consistent with them: it **refuses** a same-claim lettered re-queue against the same substrate.

**What this autopsy refuses on its own account:** a `V3-EXQ-1010b` that extends the ladder, adds seeds, adds episodes or adds adapter passes. The instrument converged, Guard 2 shows the reader was not under-powered, and the saturation witness shows the map was not under-sampled. The readings are not power problems, and more of the same is the loop the brake exists to stop.

**Granularity-debt recurrence trigger: DOES NOT FIRE.** Run with `granularity_debt_cluster.py` (targets whose own `claim_ids` name the claim, never a grep). MECH-457: 31 targets across 21 files. INV-088: 9 targets across 9 files. **This run adds a target to neither** -- `claim_ids` is empty, so it is invisible to the reader by construction. MECH-457 was in any case already decomposed 2026-07-22 into MECH-475 / MECH-476. Routing is not `/claim-synthesis`.

**Diagnostic-chain recurrence (GOV-DIAG-1): DOES NOT FIRE.** 26 `bears_on` work-streams carry pure-diagnostic no-verdict autopsies; 0 at the N>=3 ACTIONABLE threshold. This lineage's autopsies are verdict-*bearing*, so they do not accumulate as no-verdict hits.

---

## 8. Routing

**Node classification: `complicated (buildable)`.** The evidence names a build with no open question remaining.

- **Not `complex (probe-gated) / puzzle`:** the one fact a spike would fetch -- objective vs architecture -- is already computable from banked data (sec. 6a).
- **Not `mystery (known data)` in the routing sense** -- although the reframe that classification prescribes is exactly what sec. 6a performed. The frame "objective OR architecture" was wrong; the reframe ("no bottleneck preservation pressure exists at all") is what converts the node to buildable.
- **Not `aleatoric`:** 3/3 consistent on a converged instrument with four independent controls.

**A GOV-FANOUT-1 portfolio was drafted and withdrawn.** The draft proposed two legs -- "the objective supplies no gradient" (axis `learning-signal`) vs "the architecture caps content at 32 dims" (axis `intrinsic-architecture`). It was withdrawn on measurement: **both are true**, the decomposition is already in hand (sec. 6a, recomputed inside a single run after the red-team pass), the architecture term is ~3x the objective term, and the largest term is neither. Queueing a probe to split a decomposition already computed would be `mystery (known data)` mis-routed as a spike, and is precisely the letter-after-letter pattern the brake exists to stop.

**The ledger's own standing contrary statement, quoted and dismissed on the record.** This question's `decision.observation_bottleneck` says verbatim that *"no run localises WHERE in the observation->z_world path the content is lost; a layer-wise decode profile would convert a confirmed H-F from probe-gated to buildable at a named layer"*, and the driver's THIRD LIMIT names the same follow-on. Both are **correct**, and neither blocks this routing: they describe a *different, more surgical* build -- an intervention at a named layer -- whereas the build routed here does not need a layer localised first, and sec. 6a shows the dominant missing term is a pressure absent **everywhere** along the path rather than a loss at one point in it. The layer-wise probe remains a legitimate later refinement and is **not** refused by the re-derive brake; it is simply not the cheapest next step.

### Routing: `/implement-substrate` -- `amend` SD-018

`SD-018` (`encoder.resource_proximity_supervision`, status `amend_implemented_pending_validation`, priority 2, severity `degrading`) already carries three failure records for this lineage (948 `resolved`, 978 `superseded`, 1008 `open`). This appends a fourth; 1008's item stays `open` -- this run sharpens it, it does not close it. `severity` and `substrate_paths` are **unchanged** (this occurrence does not reclassify: the defect degrades a downstream reader's competence but does not produce evidence that looks valid and is not, and no new file is implicated).

**Two things flagged for governance rather than decided here:**

1. **The build the evidence names is a NEW SHAPE, not SD-018's implemented shape (a).** Shape (a) supervises one named feature (resource proximity) and V3-EXQ-978 returned it NULL. What the data says works is **generic variance/reconstruction preservation at the bottleneck**. Governance may prefer a new `sd_id` rather than growing SD-018 a third shape -- a Step 6a judgement this autopsy does not make. Flagged because the appended failure record would otherwise read as further evidence *for* the existing shape.
2. **Priority raised 2 -> 1** on the skill's own rule (a fresh failure record, and the entry already lists six unblocked items). Governance may decline; the rationale is stated so the decision is visible.

**Acceptance target -- and it is the first in this lineage set by an in-run control rather than by judgement:** the observation->z_world latent should reach **PCA-32 parity, >= 0.85 held-out oracle-action agreement at the consumer rung** on a seed majority, measured by re-running `experiments/v3_exq_1010_zworld_overcapacity_decoder_sweep.py` **unchanged**. The harness, dataset recipe, anchor and negative control all already exist and need no new build.

This **agrees** with the driver's own pre-registered null table ("CONFIRMED -> the repair is at the ENCODER'S OBJECTIVE") but arrives at a more specific and more measurable version of it.

---

## 9. Learning extracted

1. **At the encoder's own width, on the encoder's own input, and at every decoder capacity up to 12.67M parameters, REE's trained `z_world` is the worst 250->32 projection the lineage has measured.** Verified rung-by-rung 3/3 against the two comparators *this* run carries -- PCA-32 (0.8776) and its own architecture at random init (0.7045) both beat the trained latent (0.6780) at every rung. V3-EXQ-1008 additionally places a random orthonormal projection (0.7725) above it, at one capacity only.
2. **The gap decomposes and the decomposition names the build:** -0.0959 variance-fitting / -0.0779 architecture-at-random-init / -0.0260 objective. The largest term is a pressure neither contains.
3. **A capacity sweep converts "this reader couldn't find it" into "it isn't there" -- but only with a memorisation guard, and the guard is weaker than its framing.** Guard 2 is what licenses reading a flat held-out profile as a content statement, and without it the run is indistinguishable from an under-powered reader -- the ambiguity that kept this question open from 978 through 1008. But at 4.27M and 12.67M parameters against ~5,000 rows and 5 classes, memorisation is close to structurally assured, so the guard's live failure mode is really **optimiser divergence** (real, not hypothetical -- the driver's own dry smoke hit CE 4.38 > ln(5)), not under-power. The PCA anchor and the saturation witness do more discriminating work than Guard 2 does.
4. **A same-width, same-protocol, task-agnostic control is what makes a null fair.** The objection "a world-model objective owes nothing to a particular greedy rule" is fully answered by the PCA-32 anchor. Any future adequacy diagnostic on a learned representation should carry this control by default.
5. **A driver's provenance prose can go stale between authoring and execution, and the manifest is the only witness.** Recompute provenance from the manifest; never read it from the docstring.
6. **A load-bearing null accidentally replicated across two simultaneous protocol changes** (platform *and* `GRAD_CLIP_NORM`) to within 0.005.

## 10. Recommended writes (governance applies these -- this skill writes none of them)

- **Manifest:** `evidence_direction: non_contributory` -- **in BOTH copies, flat and pack.** The flat manifest carries no such field; the **run pack** carries `evidence_direction: "unknown"`, and the pack is the copy the indexer *scores*, so a flat-only write is inert. Both claims' existing notes already record this idiom verbatim as "non_contributory flat+pack".
- **INV-088, MECH-457:** direction, category and status all **unchanged**. Both storable fields already hold the recommended values, so the owed write is **note-only** -- append the V3-EXQ-1010 adjudication to `evidence_quality_note` and cite this artifact.
- **`substrate_queue.json`:** `amend` SD-018 per sec. 8.
- **Frozen ledger (Step 9b, this skill applies after the gate):** resolve `H-F-content-discarded-at-encode` -> `confirmed`.
- **Frozen ledger, additionally -- and nothing else will catch this:** the question's **`synthesis` block is two runs stale.** Its text still opens *"As of V3-EXQ-1002"* and its `surviving_label` still reads *"H-E channel-input capacity alive"* when V3-EXQ-1008 **eliminated** H-E on 2026-09-07. `decision.decidable` is already `true` (since 2026-09-05 -- the draft of this artifact wrongly said otherwise), and `decision.decision_log_ref` is still null, which is **human-owned** and not this skill's to write.
- **`review_tracker.json`:** mark the run reviewed once this artifact is confirmed.

---

## 11. Red-team pass (Step 7c)

**Verdict: CONTESTED -- 3 defects, 5 qualifications, 7 hygiene items. All applied.** Every finding was independently verified against source by the autopsy author before being acted on.

**Not a cross-model pass.** Fable was attempted first and the spawn failed with an API rate-limit error (HTTP 429, monthly spend limit, `claude-fable-5-1`); per the skill it was re-spawned once on the session model (`claude-opus-5`, the same model that drafted the autopsy). That is a valid pass but carries **no independence from the drafting model's priors** -- recorded so a later reader does not credit it with more than it has. Same failure mode and handling as `failure_autopsy_V3-EXQ-1008_2026-09-08`.

All three defects were in the **recommendation layer**; the science survived every attack in the brief. The reviewer independently recomputed 20 quantities from the manifest's own 48 `arm_results` cells rather than from the pre-aggregated blocks: 18 matched exactly, one was defect 2, one was a hygiene inconsistency.

| # | Defect | Effect |
|---|---|---|
| D1 | The draft said `decision.decidable` "reads false" and sent a flip to the gate. It reads **true**, and has since 2026-09-05. | A no-op gate question was displacing the writes actually owed -- the stale `synthesis` block and the null `decision_log_ref`. Corrected; both now in sec. 10. |
| D2 | The gap decomposition mixed 1008's **single-rung** random-orthonormal value into a best-over-capacity series; 1008 has no ladder. | Recomputed inside one run (sec. 6a). Signs, ordering, conclusion unchanged -- the fan-out refusal **stands**, its warrant repaired. One prose absolute withdrawn. |
| D3 | "the manifest carries no `evidence_direction` field" is true only of the **flat** manifest. | The run pack reads `unknown`, and the pack is what the indexer scores. Recommendation now specifies flat+pack. |

**Verified sound** (a non-exhaustive list of what the pass tried and failed to break): `zworld_untrained` really is the same architecture at random init (both tracks call `x1002._make_agent`; the untrained one simply skips the training call -- corroborated by `n_latent_stack_changed: 0` and `world_encoder_max_abs_delta: 0.0`); PCA-32 really is 32-wide, train-split-only, fitted per seed and read by the same ladder, so the "weakest possible standard" framing is fair; the machine-class withdrawal in sec. 6b was correct **in both directions**; all three non-REE failure-location buckets survive; SD-018 is the right `amend` target and **no other entry among 178** covers a reconstruction/preservation build; the brake counts match 1008 byte-for-byte; and both `-> stamp ...` change tails are a valid form and the correct note-only route against live `claims.yaml`.

**Not adjudicated by the reviewer:** the scientific reading itself, and the `synthesis` rewrite text -- both went to the Step 8 gate.

---

## 12. Step 8 gate -- CONFIRMED 2026-09-11T13:58:15Z

Four questions put to the user; three carried a `(Recommended)` option and **all three recommendations were accepted**.

| Question | Decision | Declined alternatives |
|---|---|---|
| Verdict | **Accept as drafted** -- H-F CONFIRMED; failure-location REE FAILED, narrowly scoped | soften to MIXED; drop the organism-level read |
| Routing | **Build now -- `/implement-substrate`** *(recommended)* | layer-wise localisation probe; the withdrawn objective-vs-architecture fan-out |
| SD shape | **Amend SD-018 AND flag the new shape** *(recommended)* | create a new `sd_id`; amend without flagging |
| Ledger | **Refresh the stale `synthesis`, resolve H-F, leave `decision_log_ref` null as human-owned** *(recommended)* | user logs the decision now; resolve H-F only |

**Ledger writes applied in this same commit.** H-F `alive` -> `confirmed` (`control_passed` true, `non_degenerate` true, `met_elimination_bar` false -- the state is `confirmed`, not eliminated/split, and H-C's split already attributes part of the gap to geometry, so H-F is confirmed but **not exclusive**); `synthesis` rewritten to the post-1010 state. **No growth**: no Mode A, no Mode C, no `fanout_growth_events` entry, `initial_frozen_count` stays 5 = `len(hypotheses)`, `initial_frozen_count_at_registration` stays 2. The question now reads **`alive: 0`** -- fully resolved. `decision.decidable` was already true and was not touched; `decision.decision_log_ref` remains null and human-owned.

**Integrity audit after the append: `a=0 b=0 c=1 d=0` -- identical to the pre-append baseline**, and the single `(c)` flag belongs to a different question (`sd_e1_var_bar_readout_crush`/`H-readout-saturation`). This append added no flags.
