# Failure autopsy -- V3-EXQ-1023 (diagnostic adjudication, STAGING DRAFT)

**Status: AWAITING HUMAN CONFIRMATION.** This is a headless, staging-mode draft (metaworker
dispatch chip `chip-autopsy-v3-exq-1023`). Routing is NOT finalised; nothing in this artifact has
been applied to `claims.yaml` or `substrate_queue.json`. The next `/governance` walk (Step 1.5) or
an interactive session gates it.

- **Target:** `v3_exq_1023_sd106_bottleneck_preservation_validation_20260912T045319Z_v3` (queue `V3-EXQ-1023`)
- **Outcome:** FAIL -- `experiment_purpose: "diagnostic"`, self-route `sd106_below_pca32_parity`
- **Scope:** single. **Claims:** `SD-106`. No un-autopsied siblings share this claim this tick.
- **Generated:** 2026-09-14T16:50:52Z -- **Status: DRAFT, awaiting confirmation**. Revised once, after a Step 7c red-team pass CONTESTED the first draft's central claim (Sec. 2, Sec. 7).
- **Why an autopsy at all:** every `experiment_purpose: "diagnostic"` result needs a confirmed adjudication before governance acts on it, PASS or FAIL. The self-routed label is a hypothesis, not a verdict.

---

## 1. Facts -- what ran and what it measured

**Dry-run gate (Step 2a).** `check_dry_run_citations.py` on the run_id and queue_id: 0 dry cited, 0 dry in named families, 0 ambiguous, 1 clean, exit 0. Not a smoke.

**Recording provenance: complete.** `validate_recording.py`: OK, 0 always-core gaps, 0 thin-pack drops, 0 flat-scalar findings, 0 criteria-re-derivability findings. `recording_schema` `rec/v1`, `substrate_hash`, `substrate_commit` (`fe63dd68f5`, clean, `main`), `machine` (`ree-cloud-2`), `elapsed_seconds` 41,249 (~11.5h), full `config`, explicit `seeds` `[42,43,44]`.

**Criterion-reachability lint.** `validate_experiments.py --checks dry_run_unreachable_criterion`: no fire on this driver.

**The design.** V3-EXQ-1023 is SD-106's pre-set acceptance measurement (governance `gov-20260911`, from the CONFIRMED `failure_autopsy_V3-EXQ-1010_2026-09-11`). It imports V3-EXQ-1010's instrument WHOLESALE (capacity ladder, dataset recipe, standardiser, fit protocol, calibration anchor, thresholds -- `x1010._fit_track_cell` performs every cell) and adds one new track: `zworld_sd106`, an encoder warmed with SD-106's objective (`preservation_weight=200.0`, `use_world_encoder_skip=True`). Four tracks: `zworld_sd106` (subject), `zworld_off` (paired, re-warmed this run), `ws250_pca` (calibration anchor), `rawfield_ceiling` (instrument gate). Acceptance target, pre-set and not invented here: consumer-rung (`mlp128`) held-out oracle-action agreement >= 0.85 on a seed majority (2/3).

**All 5 readiness preconditions green:**

| Precondition | Measured | Threshold | Met |
|---|---|---|---|
| `instrument_rawfield_control_supra_floor` | 0.9735 | >= 0.60 | yes |
| `anchor_pca32_reaches_parity_bar_on_majority` | 3/3 seeds clear 0.85 | 2/3 | yes |
| `sd106_bypass_trained_off_zero` | \|\|W_skip\|\|=4.13 worst seed | > 1e-8 | yes |
| `sd106_encoder_trained_in_p0` | 4/4 world-encoder tensors changed | >= 1 | yes |
| `sd106_latent_not_collapsed` | participation ratio 8.13 worst seed | >= 2.0 | yes |

**C2 (manipulation engaged, non-degeneracy witness): passed.** The preservation head ran on every SD-106 cell and on no OFF cell (`p0a_used_preservation_head: true` on every SD-106 cell; the manipulation lives in `p0a_config.preservation_weight: 200.0`, not in `enabled_default_off_flags`, since it is a `ZWorldP0Config` field, not an agent flag).

**C1 (load-bearing, the verdict): FAILED.** 0/3 seeds clear the parity bar.

| seed | SD-106 consumer agreement | OFF consumer agreement | PCA-32 anchor | SD-106 minus OFF | SD-106 minus PCA | preservation_holdout R^2 (in-training) |
|---|---|---|---|---|---|---|
| 42 | 0.7398 | 0.6676 | 0.8771 | +0.0722 | -0.1373 | 0.7490 |
| 43 | 0.7191 | 0.6749 | 0.8578 | +0.0442 | -0.1388 | 0.7464 |
| 44 | 0.6987 | 0.6621 | 0.8718 | +0.0366 | -0.1730 | 0.6999 |
| mean | 0.7192 | 0.6682 | 0.8689 | | | 0.7318 |
| min | 0.6987 | 0.6621 | 0.8578 | | | 0.6999 |

**Which criterion failed:** the discrimination criterion (does the subject reach PARITY with the anchor), not the instrument or the anchor itself -- both cleared their own gates.

---

## 2. The training-budget question (revised after Step 7c -- see Sec. 7)

**An earlier draft of this artifact treated `sd106_preservation_holdout_r2` (0.700-0.749) as directly
comparable to the SD-106 design doc's reported 0.9974/0.9978 "obs R^2" figures at the same weight,
and called the ~25-30 point gap between them the run's headline finding. A Step 7c cross-model
red-team pass (Fable 5.1) CONTESTED this: it is a category error, not a discrepancy.** Full
citations in Sec. 7; the corrected picture:

**The two numbers are different metrics.** `preservation_holdout.r2` is emitted only when
`self._preserve_head is not None` (`ree_core/latent/zworld_p0.py:645`) -- every OFF-track cell in
this manifest carries `p0a_preservation_holdout: null`. Yet the design doc's table reports an "obs
R^2" value for the **"shipped" (weight=0.0, no preserve head)** row and the **"PCA-32 anchor" (no
trainer at all)** row too -- neither can be `preservation_holdout.r2`. The design-time figures are a
**post-hoc linear-decodability probe** (the doc's own wording: "linear-decodable content"; same
methodology V3-EXQ-1008/1010 use elsewhere). `preservation_holdout.r2` is instead the R^2 of the
**jointly SGD-trained** `_preserve_head` -- competing for gradient with a 25-weighted variance
hinge, covariance, and grounding CE terms, at `Adam lr=1e-3` -- a different, more conservative
quantity. There is no established "reproduction gap" between 0.70-0.75 and 0.997.

**What the manifest's own cells DO show, and had not been read in the first draft: a real
training-budget shortfall.** The SD-106 preservation head trains inside the SD-070 "P0a" recipe,
which runs for `zworld_p0_episodes = ZWORLD_P0_EPISODES = 60` -- NOT the 200-episode `P0_WARMUP_EPISODES`
the first draft cited (that is the separate P0b e2 warmup, which does not touch the preservation
head). Reading `p0a_n_buffered` / `p0a_n_steps` directly from `arm_results[*].warmup_stats.zworld_p0`
for the SD-106 consumer-rung cells:

| seed | `p0a_n_buffered` | `p0a_n_steps` | `p0a_final_loss` (SD-106) | `p0a_final_loss` (OFF) |
|---|---|---|---|---|
| 42 | 2716 | 396 | 74.25 | 18.61 |
| 43 | 2671 | 396 | 65.91 | 18.94 |
| 44 | 2364 | 348 | 77.74 | 19.08 |

Recomputes exactly from `zworld_p0.py`'s own arithmetic (`n_train = round(0.8 * n_buffered)`,
`n_steps = (n_train // 64) * 12`; e.g. seed 42: round(0.8*2716)=2173, 2173//64=33, 33*12=**396**).
This is **below** the SD-106 design doc's own stated reference point ("a realistic P0 step count
(600 steps, 4000 buffered observations)") -- this run trained the preservation head for 58-66% of
that budget on 59-68% of the observations. The final training loss (74-78) sits far above the paired
OFF arm's (19) -- consistent with, though not conclusive proof of, the preservation term not having
converged within this budget. Directional and not statistically forceful at n=3: the seed with the
fewest steps (44: 348) also has the lowest in-training R^2 (0.6999) and the lowest consumer-rung
agreement (0.6987).

**What remains a genuine, separate finding: a recording gap at the design stage.** The design-time
proxy figures (0.9974/0.9978, and the 0.9652 "shipped recipe" figure they are compared against --
both from the SD-106 landing session's own measurement, NOT from any committed V3-EXQ script) were
never captured as a reproducible experiment artifact: no script under `experiments/`, no manifest, no
`substrate_hash`. This is independent of the metric-mismatch correction above and stands as a
learning item (Sec. 9).

**Net effect on the diagnosis:** the DV shortfall cannot yet be cleanly attributed to "the objective's
philosophy is wrong" (Sec. 4's biology-divergence question) OR confidently attributed to "the
mechanism just needs more training budget" (this section's finding) -- both are live, and the second
is cheaply testable before reasoning further about the first. See Sec. 8 for the resulting probe.

---

## 3. Claim layer

`claim_ids: ["SD-106"]`. SD-106 (`claim_type: design_decision`, `status: implemented`, `epistemic_category: standard`) is itself the subject under test -- there is no separate parent claim to misattribute a FAIL to. Two stale cross-references, both data-hygiene fixes rather than evidentiary ones:

- `claims.yaml`'s SD-106 entry carries `validation_experiment: "V3-EXQ-1015"`, which is wrong: V3-EXQ-1015 is an unrelated MECH-465 warmup-budget-dispersion experiment (confirmed `failure_autopsy_V3-EXQ-1015_2026-09-09`). Should read `"V3-EXQ-1023"`, matching `substrate_queue.json`'s SD-106 entry.
- `ree-v3/docs/substrate/SD-106-generic-bottleneck-variance-preservation.md` line 19 similarly says "Validation experiment: V3-EXQ-1015 queued" -- same fix owed.

`bears_on: ["zworld_actor_adequacy_locus"]` -- the frozen-ledger question V3-EXQ-1010's H-F leg (now `confirmed`) belongs to; SD-106 is the build that question's confirmed diagnosis named. (Not required since `claim_ids` is non-empty, carried for lineage traceability only.)

---

## 4. Biological-reference triage

**Closest reference:** DiCarlo-style ventral-stream manifold untangling (same reference V3-EXQ-1010's autopsy used; `lit_status: present` there -- `targeted_review_sd_015/2026-04-02_sd_015_object_untangling_dicarlo2007`, `targeted_review_perceptual_manifold_adaptors/2026-06-12_arc_087_ventral_stream_manifold_untangling_dicarlo2012`).

**Is SD-106 a faithful translation or a formal import?** A formal import: SD-106 implements task-agnostic, generic (1 - R^2) variance/reconstruction preservation via a separate linear decoder, as a proxy for "the encoder should not discard input structure." The biological reference's untangling is driven by *task/behavioural* pressure, not literal generic-variance retention. Whether generic preservation is a sufficient stand-in for task-relevant/selective compression (efficient-coding / information-bottleneck framings) is a real, open, lit-groundable question -- **no entry in `REE_assembly/evidence/literature/` addresses it directly** (checked: nothing under a bottleneck/coding/compression/information-theoretic naming pattern besides the two untangling entries above and two unrelated ones, `targeted_review_mech_317_behavioural_pattern_compression` and `targeted_review_pain_predictive_coding_substrate`).

**This question is real but premature to adjudicate here.** Section 2's training-budget question means we do not yet know whether the *implemented* generic-preservation objective, given a fair training budget, would close (part of) the gap. Judging "generic is the wrong target" while an under-training explanation is still live and cheaply testable would risk a biology-level conclusion resting on an artifact of the P0a schedule. A `/lit-pull` on this question is recommended as a **follow-on**, not the primary routing.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened (partial) | tested fairly; general direction mildly supported (SD-106 beats OFF); specific built shape does not meet its own acceptance target |
| Biological reference | partial | untangling reference present; generic-vs-task-relevant question open and lit-groundable, but premature given Sec. 2 |
| Dependency / prerequisites | present | 5/5 readiness preconditions green |
| Implementation completeness | **complete** | mechanism built, engaged, and trained: skip weight off zero, 4/4 tensors changed, no collapse, C2 witness clean. (Revised from an earlier "partial" -- see Sec. 7 D1.) |
| Environment adequacy | adequate | identical, previously-validated environment/dataset/oracle |
| Measurement adequacy | **adequate** | the acceptance-DV instrument is adequate (imported, red-teamed). (Revised from an earlier "partial" -- see Sec. 7 D1; the recording gap belongs in learning_extracted, not this row.) |
| Integration adequacy | isolated | frozen-representation-style read, no cross-module interaction under test |
| Scale / capacity | **likely insufficient, or unknown** | P0a trained 348-396 steps on 2364-2716 buffered observations -- below the design doc's own 600-step/4000-observation reference point; final loss (74-78) far above the OFF arm's (19). (Revised from an earlier "adequate" -- the first draft did not read these cells; see Sec. 7 D2.) |

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Reads from | Verdict |
|---|---|---|
| MECHANISM | Implementation completeness = `complete` | **established** |
| MEASURES | Measurement adequacy = `adequate` | **established** |
| ENVIRONMENT | Environment adequacy = `adequate` | **established** |
| **REE** | requires all three | by the letter of the three-bucket rule, **reachable** |

**Net classification: left open for the Step 8 gate, not forced here.** The three GOV-FAILLOC-1
buckets each read established, which would literally license "REE FAILED" -- but the Scale/capacity
row (a fourth, recognised axis in the skill's own four-layer table, not one of the three
GOV-FAILLOC-1 buckets) reads "likely insufficient" given the training-budget shortfall in Sec. 2.
Calling this "REE FAILED" would attribute the shortfall to the mechanism/design while a concrete,
cheaply-testable training-budget confound is still live and unexcluded -- the same caution V3-EXQ-1010's
own Guard 2 (the memorisation check) existed to enforce before that autopsy could safely call a null
a content finding. **Two readings are both defensible pending the probe in Sec. 8: narrowly-scoped
"REE FAILED" (SD-106 at weight=200, <=396 P0a steps, does not reach parity) vs "MIXED, grounded on
Scale/capacity".** This autopsy states the tension rather than picking one with more confidence than
the evidence supports; the Step 7c red-team pass explicitly left this call to the human gate.

**Recommended `epistemic_category`: `standard`.** Not `substrate_ceiling` -- nothing here asserts a substrate limit; the finding is an open, buildable/probeable question, the opposite of a ceiling. `re_derive_brake` count for SD-106 under R1-R3 is **0** prior ceiling hits (this reading does not add one either), so the brake does not fire (threshold 2) and is not the mechanism refusing further work here -- the refusal below rests on the driver's own `null_reading`, not the brake.

---

## 6. Step 7b -- mechanical pre-routing checks

`autopsy_pre_routing_checks.py --artifact <draft> --json`: **1 fire (C7), 1 inapplicable (C5, no sibling prose at draft time).**

- **C7** (`sd106_preservation_holdout_r2` is bit-identical across every arm within a seed): expected and dismissed, confirmed correct by the Step 7c pass. This field is an *encoder-level* readout captured once per seed during P0 warmup, before the decoder ladder is applied -- it is constant across the five capacity rungs *by construction*, not a discrimination target. It is cited in this autopsy specifically as a *cross-run* (design-time vs. this run) comparison, never as a *within-run cross-arm* discriminator, so C7's predicate does not apply to the use made of it here.

---

## 7. Step 7c -- adversarial red-team pass

**Reviewer: Fable 5.1** (`claude-fable-5-1`, cross-model from the drafting session, Sonnet 5). Read
order: draft JSON first (withholding the drafting session's reasoning), then raw evidence (manifest
cells, driver, `zworld_p0.py`, SD-106 substrate doc, landing commit, `claims.yaml`,
`substrate_queue.json`, the V3-EXQ-1010 autopsy, the git range 616e7136..fe63dd68), recomputing
load-bearing numbers directly from the manifest, and only then the draft `.md`.

**Verdict: CONTESTED.** The DV result itself was found sound (every per-seed number, delta, mean, and
R^2 recomputes exactly from the manifest cells). What did not survive: the first draft's
self-declared "headline finding" that the preservation term's holdout R^2 "did not reproduce" a
design-time value "on the exact same metric, computed by the exact same code path."

**Defects confirmed (verified independently against source by the autopsy author before acting, per
the skill's "a finding is a lead, not a verdict"):**

| # | Defect | Citation | Cheap confirmer used |
|---|---|---|---|
| D1 | "Same metric, same code path" is false -- design-time figures are a post-hoc linear probe; `preservation_holdout.r2` is the SGD-trained head's own holdout metric, null on every OFF cell | `zworld_p0.py:645` gate; design doc "shipped"/"PCA-32 anchor" rows (lines 117-122) cannot be `preservation_holdout.r2`; manifest `arm_results[*].warmup_stats.zworld_p0.p0a_preservation_holdout: null` on every OFF cell | Read the gate line + the design table; confirmed by re-querying the manifest directly |
| D2 | "Same ~600-step/~4000-observation budget" is false -- P0a actually ran 348-396 steps on 2364-2716 buffered observations, driven by `ZWORLD_P0_EPISODES=60`, not the 200-episode P0b budget the first draft cited | manifest `arm_results[*].warmup_stats.zworld_p0.{p0a_n_steps,p0a_n_buffered}`; recomputes from `zworld_p0.py`'s own `n_train`/`n_steps` arithmetic | Re-queried the manifest directly; recomputed `n_train`/`n_steps` by hand and matched exactly |
| D3 | The originally-recommended probe (bare re-read of `preservation_holdout.r2` under identical seeds/code) is deterministic (`bgen` seeded at `cfg.seed+1`, `zworld_p0.py:579`) and cannot discriminate; its "if low -> mechanism defect" inference does not follow | `zworld_p0.py:579`; the design-time comparator is a different metric (D1) | Same seed/code path -> reproduces 0.749 to within the cross-platform drift band (<=3.7e-4) V3-EXQ-1010's autopsy already measured for this pipeline |
| D4 | `resolved: "superseded"` on the prior V3-EXQ-1010-derived failure_record item misapplies the skill's verb -- this is "a new, independent failure on the same substrate", which the skill says to leave `open` | `.claude/skills/failure-autopsy/SKILL.md` (Step 7, `resolves_prior_failure_record` guidance) | Read the skill section directly; the prior item is left untouched (default `open`) and this artifact appends a new `failure_record_entry` rather than filling `resolves_prior_failure_record` |

**All four disposed of by revising this artifact** (this is the revised version; the pre-red-team draft is not retained as a separate file, per the skill's "record withdrawals rather than deleting them" -- the withdrawal is recorded here, in this section, rather than as a diff against a discarded document).

**Verified sound (tried to break, could not):** every per-seed DV number and delta; the git range
`616e7136..fe63dd68` is genuinely empty over the relevant substrate paths (14 commits, none touching
`zworld_p0.py`/`stack.py`/`config.py`/`agent.py`/the P0-warmup libs); the C7 dismissal; `standard` as
the recommended epistemic category; the re-derive brake's 0 count and its non-firing; the recording
gap on the design-time figures (genuinely no committed producer, confirmed by corpus grep);
`recommended_evidence_direction: mixed`; the `claims.yaml` staleness flag.

**Not adjudicated (left to the human gate):** whether the SGD-trained head would approach the
post-hoc OLS R^2 given more P0a budget (the probe's job); the net GOV-FAILLOC-1 call (Sec. 5); whether
the `/lit-pull` should be promoted to primary if the probe's metric-mismatch-only outcome obtains.

---

## 8. Routing (DRAFT -- not yet confirmed)

**Node classification: `complex (probe-gated) / puzzle (known rules)`.** The frame is well-posed (a
preservation objective at a pre-registered weight should preserve some verifiable fraction of
`world_obs` variance), but a fact is missing: at the shipped P0a training budget, does the SD-106
latent's TRUE linear-decodable content (a post-hoc probe, matching the design-time methodology)
already sit near the design-time figure -- in which case the DV shortfall is a genuine objective-choice
question -- or does it also fall short, rising or not with more budget. This is answerable by a
cheap probe.

**Not `complicated (buildable)`:** there is no named build with no open question -- we do not yet
know WHAT to build (more P0a budget? a different interaction between the preservation term and the
rest of the P0 loss? nothing, and the objective is already fine at this budget?).

**Refused: a same-weight-bump or different-weight re-queue, and a bare re-read of the existing
metric.** The driver's own `null_reading` states this explicitly ("NOT to an automatic re-queue at
another weight"), and this autopsy agrees independently. This refusal is NOT the re-derive brake
(SD-106's ceiling-hit count is 0, well under threshold) -- it rests on the driver's own stated design
intent. Separately, per Sec. 7 D3, a bare re-read of `preservation_holdout.r2` under identical
seeds/code is deterministic and would not discriminate among the live explanations -- the probe below
is specified to avoid that trap.

**Recommended primary routing: `/queue-experiment` -- a cheap, targeted, two-metric diagnostic.** On
the same frozen SD-106 latent, at `preservation_weight=200.0`, read BOTH (a) `preservation_holdout.r2`
(already reported) and (b) a post-hoc OLS linear-probe R^2 matching the design-time methodology
(SD-106 substrate doc's "Measured effect" section), across a step-budget arm: as-shipped
(348-396 steps), ~600 steps (matching the design doc's own reference point -- raise
`zworld_p0_episodes` or `epochs`), and ~1200 steps. No decoder ladder, no oracle-adapter dataset
collection, no P1/RL phase -- cheap relative to the ~11.5h full V3-EXQ-1023-shaped run. Three
attributable outcomes:

1. **Post-hoc R^2 already ~0.99 at the shipped budget.** The metrics were simply never comparable; the mechanism and budget are both fine, and the DV shortfall is a genuine objective-choice question -- promote the `/lit-pull` (Sec. 4) to primary.
2. **Post-hoc R^2 low but rising with budget.** Under-budgeted P0a -- fix the budget, then re-run the acceptance measurement (a new lettered iteration, not a bare weight bump).
3. **Post-hoc R^2 low and flat across budget.** A genuine mechanism/implementation defect -- needs a build fix before any further validation.

**Secondary, deferred routing: `/lit-pull`** on generic vs. task-relevant/selective compression in sensory encoding bottlenecks (efficient coding / information bottleneck theory), per Section 4. Recommended as a follow-on once outcome (1), (2), or (3) above is known -- not as the primary output of this autopsy.

**`recommended_substrate_queue_entry`: `amend` SD-106.** A new `failure_record_entry` (this run's numeric result, the training-budget finding, and the corrected metric framing) is appended; per Sec. 7 D4, the prior V3-EXQ-1010-derived placeholder item is left untouched at its default `open` (this is a new, independent failure on the same substrate, not a supersession). `severity`/`substrate_paths` unchanged (`degrading`; `ree_core/agent.py::compute_resource_proximity_loss`, `ree_core/latent/stack.py`, `ree_core/latent/zworld_p0.py`) -- this occurrence does not reclassify the defect. `priority_suggested: 1` (unblocks 6 claims; rule already satisfied by the existing entry).

**Frozen hypothesis ledger (Step 9b): does not apply.** No hypothesis in `hypothesis_space_registry.v1.json` references SD-106, V3-EXQ-1023, or `sd106` (checked by grep); this target is not part of the `zworld_actor_adequacy_locus` question's live-hypothesis set (that question resolved fully at V3-EXQ-1010 with 0 alive legs) and does not open a new one -- SD-106's own acceptance measurement is an implementation-validation gate, not itself a rival explanatory hypothesis in that portfolio. Nothing to pre-register or resolve.

---

## 9. Learning extracted

1. SD-106-ON improves consumer-rung oracle-action agreement over the paired OFF arm by 0.037-0.072 absolute on all 3 seeds -- some bottleneck-preservation pressure helps, consistent with V3-EXQ-1010's diagnosis -- but the specific built shape (`preservation_weight=200` + skip) falls ~0.14 short of the PCA-32 anchor and clears the pre-set 0.85 bar on 0/3 seeds.
2. The SD-106 preservation head's P0a training budget in this run (348-396 steps on 2364-2716 buffered observations, driven by `ZWORLD_P0_EPISODES=60`) is well below the SD-106 design doc's own stated reference point (600 steps, ~4000 buffered observations); the head's final training loss (74-78) sits far above the OFF arm's baseline (19). Whether this budget shortfall explains the DV shortfall is open and cheaply testable.
3. The SD-106 design doc's headline proxy figures (0.9974/0.9978) are a post-hoc linear-decodability probe, methodologically distinct from `preservation_holdout.r2` (the in-training SGD-trained head's own holdout R^2, null on every OFF cell in this manifest). Conflating the two -- as an earlier draft of this artifact did -- is a category error; caught by a Step 7c cross-model red-team pass on a one-line read of the code gate and the design table's own rows. Recorded so a later reader does not re-derive the same conflation.
4. The design doc's proxy-calibration figures (both the 0.9974/0.9978 table and the 0.9652 comparator) were never captured as a reproducible, committed experiment artifact -- no script, no manifest, no `substrate_hash`. This recording gap is real and independent of item 3; a future design decision resting on a proxy number should mint a minimal committed script for it, per the Experimental Recording Standard.
5. Whether the untangling reference calls for generic or task-relevant/selective compression remains open and lit-groundable, but resolving it before item 2's training-budget question is answered would risk drawing a biology-level conclusion from what may simply be an under-trained P0a warmup.

## 10. Recommended writes (governance applies these -- this skill writes none of them)

- **`claims.yaml` SD-106:** append to `evidence_quality_note`, citing this artifact (see per-claim `change` field). Also correct the stale `validation_experiment: "V3-EXQ-1015"` to `"V3-EXQ-1023"` (Sec. 3) -- a data-hygiene fix, not an evidentiary one.
- **`ree-v3/docs/substrate/SD-106-generic-bottleneck-variance-preservation.md` line 19:** same stale-reference fix ("V3-EXQ-1015 queued" -> "V3-EXQ-1023 ran, see failure_autopsy_V3-EXQ-1023_2026-09-14").
- **`substrate_queue.json` SD-106:** `amend` per Sec. 8 -- new `failure_record_entry`; prior item left `open`.
- **`review_tracker.json`:** mark the run reviewed once this artifact is confirmed.
- **Follow-on for governance to chip (not this session, per CLAUDE.md Session Land Protocol -- this skill records but does not spawn):** the `/queue-experiment` two-metric diagnostic in Sec. 8, and (deferred, conditional on that probe's outcome) the `/lit-pull` commission.

---

## 11. Step 8 gate -- STAGING MODE, NOT YET RUN

This is a headless staging draft. The interactive gate (verdict, routing, SD-shape, ledger writes) is owed to the next `/governance` walk or an interactive confirming session, per `/failure-autopsy` SKILL.md "Staging mode". The gate should in particular resolve the Sec. 5 tension (narrowly-scoped "REE FAILED" vs "MIXED, grounded on Scale/capacity") and confirm or amend the Sec. 8 probe spec before it is queued.
