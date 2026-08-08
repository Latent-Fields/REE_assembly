> **RESCUED ARTIFACT -- provenance banner prepended 2026-08-08T06:35:28Z; everything below the
> horizontal rule is the original file, byte-for-byte unmodified.**
>
> **Status: AWAITING USER REVIEW. Nothing in this file has been written to `claims.yaml`,
> and nothing in it has been minted into `manual_proposals.v1.json`.** (The six
> `governance_flags.v1.json` entries described in §1 were landed separately by the
> original session and are already on `origin/master`; they are read-only-consumed by
> `/governance` and touch no claim.)
>
> **Provenance.** Written by the headless dispatch chip
> `chip-20260807-thoughtdigestion-trial-5` on 2026-08-08 as an UNTRACKED file at its own
> worktree root (`.claude/worktrees/metaworker-chip-20260807-thoughtdigestion-trial-5/THOUGHT_DIGESTION_REVIEW_5claims_2026-08-07.md`),
> following the `/thought-digestion` skill's generic "Unattended / overnight mode"
> scratchpad wording. It was believed lost -- see the Background of
> `chip-20260808-headless-durable-artifact-rule`, which asserts the worktree was removed
> and the content permanently unrecoverable. **That premise was WRONG.** The worktree was
> never removed; on `ree-cloud-5` at 2026-08-08T06:33Z the file was still present,
> untracked, 61838 bytes / 743 lines, complete through §4. This copy is that file, moved
> to a tracked path so the loss the chip was written to prevent cannot happen to it.
>
> Rescued by `chip-20260808-headless-durable-artifact-rule` (headless dispatch), which is
> also the chip that added HEADLESS WORKER CONTRACT rule 6 requiring exactly this.
>
> **Bearing on `chip-20260808-thoughtdigestion-trial2-5`** (status `open` at time of
> writing): that chip is a RE-RUN commissioned because this content was thought lost. It
> is not lost. Whether the re-run still has independent value is the user's call -- this
> session deliberately did not withdraw or alter that chip.

---

# Thought Digestion — TRIAL run, 5 claims, unattended draft-only

**Session:** `metaworker-chip-20260807-thoughtdigestion-trial-5` (headless `claude -p`, dispatched by metaworker-dispatch)
**Run window:** 2026-08-08T00:20Z → 2026-08-08T01:0xZ
**Chip:** `chip-20260807-thoughtdigestion-trial-5`
**Write policy:** draft-only-stage-for-review. **Nothing was written to `claims.yaml`. Nothing was minted into `manual_proposals.v1.json`.** The only things that landed anywhere are six additive `governance_flags.v1.json` entries (§1), which are read-only-consumed by `/governance` and touch no claim.

## How to use this file

Read §0 first (that is the trial verdict and the three things that actually matter). §1 is the governance flags — those are the findings with teeth, and they are already raised structurally so they will surface in `/governance` Step 1a whether or not you act on this file. §2 is the five per-claim drafts in full text, which is what you approve/edit/reject. §3 is systemic findings for you to decide whether to spin off as chips — **I deliberately spawned no chips for them**, per the trial brief.

Nothing here is applied. To apply a draft: re-read the claim's **whole** block in `claims.yaml` first (a field may already exist further down than you read), paste the `what_would_answer`, then `python scripts/build_claims_json.py` from `REE_assembly/` and pathspec-commit.

---

## §0 — Trial verdict, and the three things that matter

**Yield.** 5 claims dispatched, 5 returned usable drafts. **Zero deferrals to disposition (f)** — every claim in the wave yielded a falsification condition I would be willing to put in front of you. Recommended dispositions: **four (a) testable-now, one (c) substrate-blocked**.

That distribution is itself the headline, and it is not what I expected when I built the worklist. Three of the four (a)s are claims whose *own registry text* says they are blocked — and in all three cases the block had lifted and nobody had noticed. That is the digestion agents' standing "verify currency, do not assume it" instruction earning its place: the falsifiers are the routine output; **the stale gates are the valuable one.**

**The three things that matter, in order:**

1. **SD-020 is `status: stable` on the strength of a run that never executed the code it is about.** V3-EXQ-324b — named in SD-020's own `live_status.evidence.from` with `verdict: supports/PASS` — contains **zero** references to `REEAgent`, `harm_surprise_pe_enabled`, or `compute_harm_accum_loss`. It validated a standalone-encoder bench reimplementation. The one run that *did* drive the real flag (V3-EXQ-324: 3 `REEAgent` refs, 4 flag refs) **FAILED** at 1/5 seeds. I verified this myself by direct source read, not on the agent's word. → **GFLAG-0005**, and this is the one to look at tonight if you look at nothing else.

2. **MECH-295's substrate ceiling lifted seven weeks ago and the claim never found out.** Its `ceiling_routing_note` still describes `scaffolded_sd054_onboarding` as "in flight"; that substrate landed, and V3-EXQ-812 (2026-07-24) measured `p2_z_goal_norm_peak` **0.529** against V3-EXQ-490k's **0.193**. 812 nonetheless FAILED — but for a *new* reason (`INVALID_HARNESS`, whole per-candidate bias plane collapsed) whose confirmed autopsy recommends `measurement_test_design_defect`, not a ceiling, and routes `/queue-experiment`. Nothing has been queued in 15 days. Worse, 812 carries `claim_ids: []`, so the most informative run on this claim leaves **no trace in its evidence index** — a reader of `claims.yaml` alone concludes 490k was the last word. → **GFLAG-0007**.

3. **Two of five claims in this wave assert behaviour of a code path that no run in their evidence base ever switched on.** SD-020/SD-087 (above) and SD-086, whose title says E3 consumes `||z_harm_a||` "as an approximately constant gain" while both named consumers are flag-gated at `0.0` default and unset in *every* run of the lineage (664/856/857a). Two independent instances of one shape, in a wave of five, is a pattern rather than a coincidence — see §3.1. → **GFLAG-0008**.

**What I could NOT do, stated plainly.** The brief authorised applying objective, checkable corrections directly. I found several (stale `file:line` citations, a stale `live_status` marker, a stale governance routing) — **and applied none of them**, because every one lives in `claims.yaml`, which draft-only mode forbids me to write. The single correction outside `claims.yaml` is the hardcoded `config.py:2306` comment at `ree-v3/experiments/_lib/baselines/affective_fishtank.py:251`; I left that too, because it sits in a **baseline module whose hash is load-bearing for arm-reuse fingerprinting**, so a comment-only edit is not obviously free. That judgement is worth your override if you disagree — it is a one-line fix otherwise.

---

## §1 — GOVERNANCE FLAGS (raised structurally; act via `/governance`)

Six flags raised, all landed on `origin/master` (verified: `git show origin/master:evidence/planning/governance_flags.v1.json`). Raised as `thoughtdigestion-trial-5-headless-2026-08-07`.

| id | type | claims | one-line |
|---|---|---|---|
| **GFLAG-0005** | `contested_disposition` | SD-020, SD-087 | `stable` promoted by a run that never exercised the shipped code path |
| **GFLAG-0006** | `stale_note` | SD-087, Q-086 | governance routed an experiment for a question already answered by 856's ARM_ON |
| **GFLAG-0007** | `contested_disposition` | MECH-295 | `substrate_ceiling` gate lifted; autopsy says test-design defect; 15 days unactioned |
| **GFLAG-0008** | `evidence_discrepancy` | SD-086 | title asserts E3 consumption through two paths that are default-off and never enabled |
| **GFLAG-0009** | `stale_note` | Q-090, MECH-485 | a tracked "AWAITING USER REVIEW" staged draft is superseded by a lit-pull that landed 5h later |
| **GFLAG-0010** | `stale_note` | SD-086, SD-087, SD-020 | all cited `file:line`s have drifted; one by ~1150 lines |

### GFLAG-0005 — SD-020 `stable` rests on a bench, not the substrate *(highest severity)*

Verified by me directly:

```
v3_exq_324_sd020_harm_surprise_pe.py    REEAgent: 3   harm_surprise_pe_enabled: 4   → FAILED (1/5 seeds)
v3_exq_324a_sd020_harm_surprise_pe.py   REEAgent: 0   harm_surprise_pe_enabled: 0
v3_exq_324b_sd020_harm_surprise_pe.py   REEAgent: 0   harm_surprise_pe_enabled: 0   → PASSED, promoted SD-020 to stable
```

The lineage silently switched from the integrated agent to a standalone bench between 324 and 324a. 324b reimplements the target inline (`abs(mean_dmg - dmg_ema)` against a fresh `nn.Linear` `dmg_head`), with no precision weighting, no `z_harm_a_aux_loss_weight`, no `REEAgent`; it imports `REEConfig` only for `from_dims` dim validation. **No PASS has ever been obtained on the code SD-020 describes.**

Consequences beyond SD-020's status: **SD-020's `default_off_scope_note` and SD-087's own title are both factually wrong.** They say the 324b reading is "scoped to the flag-on configuration". 324b had no flag at all. The correct wording is that it is scoped to a *bench reimplementation that never exercised the shipped flag path*.

**Governance decision owed:** does `stable` survive a promoting run that did not test the claim's own implementation, or does SD-020 revert to `provisional` pending the production-path run drafted in §2.4?

### GFLAG-0006 — the routed experiment is already answered

SD-087's and Q-086's notes (2026-08-01/02/03) all say "the flag needs to be set from the START of training" is the one untested hypothesis, and 2026-08-03 governance routed `/queue-experiment` for a train-from-scratch-with-flag-ON run. **V3-EXQ-856's ARM_ON already did exactly that** — `make_agent_and_env(seed, harm_surprise_pe_enabled=...)` *then* `warmup_train`, so the flag was set at construction, before warmup, never post-hoc — and the 664 signature survived anyway (OFF CoV 0.007057 vs ON 0.007421, both ~7x below the 0.05 floor). This is recorded in `evidence/reanalysis/reanalysis_sd087_flag_from_start_already_tested_20260803T144516Z.json` (file exists, verified) and the paired chip resolved `done` with "no experiment queued". **Two agents found this independently** (one via the reanalysis artifact, one by reading 856's driver call ordering) — which is why I am confident in it. As written, the notes will send a future session to spend compute on a closed question.

The one surviving non-duplicative reading is "from the start of a *curriculum-trained* regime" (more than the ~50-episode raw warmup) — which is the shared scope condition, not a scratch-vs-post-hoc distinction. **Governance should decide which reading it meant before anything is built.**

### GFLAG-0007 — MECH-295: ceiling lifted, defect relocated, routing unactioned

V3-EXQ-812 manifest, read directly by me:

```
outcome: FAIL   evidence_direction: non_contributory   claim_ids: []
interpretation.label: INVALID_HARNESS
mean_proximity_range        0.0, 0.0, 0.0
mean_dacc_bias_range_mean   0.0, 0.0, 0.0      ← whole bias plane collapsed, not MECH-295's channel
p2_z_goal_norm_peak         0.529, 0.529, 0.409  ← vs 490k's 0.193: the named ceiling HAS lifted
candidate_summary_source    ABSENT from config   ← i.e. the "proposer" default
```

The agent's diagnosis (which I did not independently verify past the manifest, so treat as *plausible not confirmed*): under `candidate_summary_source="proposer"` the per-candidate summary is the trajectory's timestep-0 `z_world`, identical across candidates, so drive×proximity×gain is uniform and subtracting it cannot move an argmin **by construction** — the precondition is unsatisfiable and no result is interpretable. The remedy `candidate_summary_source="e2_world_forward"` is already shipped and in routine use by ~14 other drivers. The `mean_dacc_bias_range_mean = 0.0` in the same run is a strong corroborating negative control.

**Three decisions owed:** (i) is `substrate_ceiling` still the right category, or is the confirmed autopsy's `measurement_test_design_defect` correct? (ii) should the routed successor be queued? (iii) should 812 be re-tagged so MECH-295's evidence index stops being blind to it?

### GFLAG-0008 — SD-086 asserts consumption through paths that are off

Verified: `urgency_weight: float = 0.0` (`ree_core/utils/config.py:716`), `affective_harm_scale: float = 0.0` (`:723`); norm reads at `e3_selector.py:1182` and `:3128`, each gated on its flag; neither flag appears in `v3_exq_664`, `v3_exq_856`, `v3_exq_857a`, or the shared baseline module. **SD-086 warrants a `default_off_scope_note` of exactly the shape SD-020 already carries.**

### GFLAG-0009 — a live staged draft is superseded

`evidence/planning/thought_digestion_staged_2026-08-07_mech485_q090.md` (20,877 bytes, 2026-08-07 18:40) is tracked, committed, headed **AWAITING USER REVIEW**, and instructs a reader to paste two `what_would_answer` blocks into `claims.yaml`. Its Q-090 block was staged **five hours before** that claim's own targeted lit-pull landed (`evidence/literature/targeted_review_q_090`, 23:47Z), whose highest-confidence entry contradicts the two-horn framing the staged draft pre-registers. Neither Q-090 nor MECH-485 has `what_would_answer` today, so the file is still live and still applicable-looking. **Annotate or delete it before anyone applies a pre-lit-pull draft.** (Its MECH-485 block is unaffected by the lit-pull and still looks applicable as written.)

### GFLAG-0010 — every cited line number has drifted

Verified 2026-08-08 against `ree-v3` HEAD:

| claim | cited | actual |
|---|---|---|
| SD-087 title, SD-020 `default_off_scope_note` | `config.py:2306` | `ree_core/utils/config.py:2656` (wrong path **and** +350) |
| SD-087 `non_degeneracy_precondition` | `agent.py:8636-8642` | `ree_core/agent.py:9787`, fn `compute_harm_accum_loss` at `:9743` (+~1150) |
| SD-086 title | `e3_selector.py:1038`, `:2766` | `:1182`, `:3128` |

Also hardcoded at `ree-v3/experiments/_lib/baselines/affective_fishtank.py:251`. **The rate matters more than the instances:** the `agent.py` citation drifted a further ~190 lines in the five days since a 2026-08-03 reanalysis re-cited it. This lineage should cite **symbol names**, never line ranges. See §3.2 for the registry-wide count.

### Deliberately NOT flagged (and why)

**Q-020's `live_status` is stale** — it reads `reading: resolved`, `as_of: 2026-07-11`, `needs_review: false` while `status: candidate` and its `evidence_quality_note` records a 2026-07-25 reopening. I confirmed this directly. I did **not** raise a flag because it is **already machine-detected**: `evidence/planning/claims_live_status_drift.md` (generated 2026-08-07T18:49Z) lists Q-020 in the HARD "Reading drift" bucket *and* in event-provenance drift. Raising a per-claim flag on top of an existing generated tracker is exactly the second-and-staler-tracker failure the chip discipline warns about. It is one of a whole bucket; the remedy is `scripts/apply_live_status.py` under a claim on `claims.yaml`, run for the bucket, not for Q-020 alone. **Flagging it here in prose instead so it is visible without being double-tracked.**

---

## §2 — The five drafts, full text

Ranking method (skill Step 3, composite — not fan-in alone, not A→Z): fan-in from `depends_on` counts in `claims.yaml`; tractability up-rank for an existing `falsifier` / `non_degeneracy_precondition` field, a "Falsifiable:" clause in `functional_restatement`, a `pending_retest_after_substrate`, or a ceiling note; out-of-domain smell down-rank; `digestion_note` carriers excluded (9 claims: ARC-017, MECH-150, MECH-151, MECH-163, MECH-173, MECH-256, MECH-321, SD-014, SD-056). Courses (a) and (b) both represented; course (d) — status/stance contradictions — came back **empty** (zero claims with `status: resolved/closed` and `stance: asked`), which is a clean result.

---

### §2.1 — Q-090 · course (a) · **disposition (c) substrate-blocked** · `substrate_conditional` (unchanged)

*Why in the wave:* one of only **two** `asked` claims in the whole registry missing `what_would_answer`; registered 2026-08-07; its own notes say the dissociable predictions were "left for a future /thought-digestion pass". This pass is that pass.

**Recommended disposition (c)** — every precondition MECH-485 leg 3 needs is still absent in `ree-v3` (re-verified today: `epistemic_deficit` zero hits in `ree_core/`; `cancel_window`/`veto_window` zero hits; `predicted_harm_delta` one write site, zero read sites; no retention of losing E3 candidates). The question is not askable yet — but its landed lit-pull already narrowed it from two horns to **three**, and the falsifier is worth registering now so the eventual build is pre-committed.

```
Answered by EXPERIMENT, once MECH-485's substrate exists: a factorial
over (predicted-harm magnitude) x (goal-match) x (confidence),
measuring which computed-but-not-acted-on alternatives actually get
retained. This is a question, not an assertion, so every horn has a
confirming signature; the failure mode here is a vacuous test, not a
wrong answer.

THE HORNS. The first two are the user's own (raw thought Addendum 5).
The third was added by this claim's OWN landed lit-pull (LIT-0568,
2026-08-07) and is not a hedge -- it is the pull's highest-confidence
entry, and it converges with the pull's sharpest disconfirmer.
-- SAME-SCALE: leg-3 admission is a second, lower cut-point on the
same predicted-harm magnitude the interrupt cuts high. Predicts
retained alternatives cluster just below the interrupt cut-point,
retention is MONOTONE in magnitude, and goal-match explains no
variance once magnitude is in the model.
-- INDEPENDENT-CRITERION: retention tracks goal-relevance instead,
via the MECH-292/293 cue system -- concretely SD-039's `goal_match`,
the SD-079-centered cosine between a live z_goal cue and a stored
goal-snapshot payload. Predicts dissociations the same-scale reading
cannot produce: low-magnitude/high-goal-match RETAINED, and
high-magnitude/goal-irrelevant NOT retained.
-- TWO-FACTOR PRODUCT (Mattar & Daw 2018; recorded `mixed`, conf
0.62, the highest in the pull): a normatively correct admission rule
is gain x need -- a magnitude-like term TIMES a relevance-like term,
multiplicative, so either factor at zero kills retention regardless
of the other. Note this paper is ALREADY MECH-292's own normative
anchor, so adopting it makes leg 3 and the ghost-goal bank two
applications of one principle rather than two independently-invented
rules that will drift apart.

NON-DEGENERACY PRECONDITION, in four parts. Part (2) is the one that
actually decides whether this question is askable.
(1) INHERITED -- everything MECH-485's own falsifier requires (Leg 0
cleared, magnitude computed AND consumed, confidence term exists,
leg-1 pathways wired, retention mechanism exists). Do NOT re-derive
it here; see MECH-485. Re-verified 2026-08-08 against live ree-v3:
all still unmet, so this question is not askable at all yet. A run
attempted before they are met self-routes to MECH-485's own
precondition report, not to a verdict on this claim.
(2) DECISIVE -- MAGNITUDE AND GOAL-MATCH MUST BE MEASURABLY
DECORRELATED IN THE TEST DISTRIBUTION. If harmful alternatives are
also goal-irrelevant in the environment used, all three horns make
IDENTICAL predictions and no outcome distinguishes them, however
clean the statistics look. The probe set must be deliberately
populated in the OFF-DIAGONAL cells -- (low-magnitude,
high-goal-match) and (high-magnitude, low-goal-match) -- with both
cells reported BY COUNT, not assumed present. A run whose
off-diagonal cells are empty or near-empty is VACUOUS and must be
reported as such rather than scored. This is the single most likely
way to answer this question wrongly-but-convincingly.
(3) GOAL-MATCH MUST BE LIVE AND DISCRIMINATING -- and the evidence
here is specific enough to dictate the BUILD ROUTE, not merely to
warn. `goal_match` exists, is centered per SD-079 (provisional,
three consecutive PASSes 806/807/823), and discriminates at two
levels already: unit level (V3-EXQ-494 UC5, goal-inactive anchors
0.0 vs goal-active 0.998, 3/3 replicates) and consumer-ranking level
(V3-EXQ-868 PASS -- a goal-relevant inactive anchor outranks a
goal-IRRELEVANT anchor of matched staleness, 4/7 comparable seeds at
a pre-registered 4/7 bar, `goal_match`-dominant on 3 of 4 direct
wins). So the (high-magnitude, low-goal-match) cell IS constructible
-- but build it the V3-EXQ-868 way, as goal-relevant vs
goal-irrelevant at matched staleness WITHIN one goal epoch. Do NOT
build it by contrasting DISTINCT GOAL EPOCHS: that route is
measured-degenerate (V3-EXQ-889 dry run, 2026-08-03 -- cue-centered
max pairwise cosine 0.99752 against a pre-registered 0.99
non-degeneracy bar, n_distinct_top1_anchors = 1.0, i.e. four
deliberately-distinct goal cues collapse onto one anchor). Note also
that the 868 margin is exactly at its bar, so treat the off-diagonal
as constructible-but-marginal and report cell counts and effect size
rather than a bare PASS.
(4) CONFIDENCE MUST BE MEASURED AND REPORTED, not just magnitude and
goal-match. Pupillo et al. 2023 nominate a third moderator -- whether
the prediction proved CORRECT -- which is a cousin of MECH-485's own
`epistemic_deficit` term. If confidence is left unmeasured, a
confidence-gated retention rule masquerades as whichever of the other
two horns happens to correlate with it in that environment.

CHEAP STRUCTURAL PRE-TEST, worth running before the full factorial
because it can kill one horn on its own: MONOTONICITY. A threshold on
a scalar is necessarily monotone -- more magnitude, weakly more
likely retained -- at every cut-point. So if retention probability is
NON-MONOTONE in magnitude, or its sign flips conditional on a second
variable, the same-scale horn is refuted structurally and no choice
of low cut-point rescues it. This is Pupillo et al.'s crossover
imported as a structural argument rather than as an effect size, and
it needs only the retention mechanism plus a magnitude, not the
goal-match arm.

CONFIRMING signature (same-scale horn upheld): retention is well
predicted by magnitude ALONE; adding `goal_match` explains no
significant additional variance; retention is monotone in magnitude
with no sign flip under any measured moderator; the off-diagonal
cells behave as magnitude alone predicts (low-magnitude/
high-goal-match NOT retained, high-magnitude/goal-irrelevant
RETAINED); and the fitted retention cut-point sits below the
interrupt cut-point on the same scale, the two moving TOGETHER when
that scale is rescaled.

FALSIFYING signature -- three distinct ways, each naming which horn
wins and what to do about it:
-- INDEPENDENT-CRITERION wins if `goal_match` explains retention
variance over and above magnitude; the off-diagonal cells dissociate
in its predicted direction (low-magnitude/high-goal-match RETAINED,
high-magnitude/goal-irrelevant NOT); and sweeping the interrupt
threshold moves the interrupt boundary while leaving the retention
boundary where it was. Remedy: give leg 3 its own relevance
criterion, sourced from MECH-292/293.
-- TWO-FACTOR PRODUCT wins if neither predictor suffices alone but
their PRODUCT fits, and specifically if the zero-factor prediction
holds: a high-magnitude alternative concerning a state the agent will
never re-enter is NOT retained, and a perfectly goal-matched
alternative that would change no future choice is NOT retained
either. That zero-killing asymmetry is what distinguishes a product
from any additive or single-factor rule, and it is the signature to
pre-register. Remedy: implement leg 3 as gain x need, and re-pose
Q-090 as "what are REE's two terms" rather than "which horn".
-- SAME-SCALE dies structurally, independent of the above, if the
monotonicity pre-test shows a sign flip. Record this separately: it
refutes one horn without electing either replacement.

THE QUESTION IS MALFORMED (report as such; do not force an answer)
if neither magnitude nor goal-match nor their product explains
retention above chance once the substrate exists -- retention driven
by something none of the horns names, e.g. recency or capacity
pressure, which is an informative finding about leg 3 and a reframe
of this question, not a null result. OR if the off-diagonal cells
cannot be populated in ANY available REE environment, making
precondition (2) structurally unachievable -- in which case the
admission criterion genuinely is a design stipulation after all,
contrary to the user's framing of it as empirically resolvable, and
that reframe must be recorded here explicitly rather than treated as
a failure to answer.

TWO DESIGN WARNINGS, from the lit-pull, that are not verdict criteria
but must not be lost:
-- OVER-ADMISSION HAS A NAMED PATHOLOGY. Mattar & Daw flag
dysfunction of this prioritisation as a candidate substrate for
rumination and craving. A leg-3 rule tuned toward admitting too much
yields an agent that cannot stop revisiting the roads it did not
take. Report the retained-set SIZE and its growth rate alongside any
verdict.
-- THE PRODUCT RULE MAY BE RIGHT ABOUT RETENTION AND WRONG ABOUT LEG
3's PURPOSE. Mattar & Daw's `gain` term says to DISCARD a large
predicted harm the agent could not have acted on. But leg 3 exists
for responsibility attribution, and the harms an agent holds itself
accountable for are not only the ones it could have re-optimised
around. So if the product rule fits retention while the retained set
turns out to be useless for counterfactual/responsibility evaluation,
that is a finding about what leg 3 is FOR -- and it should reopen
MECH-485's leg-3 statement, not be scored as a win for any horn here.
```

**Provenance:** horns 1–2 verbatim from the user's own `docs/thoughts/2026-08-07_responsibility_counterfactual_memory.md` Addendum 5 (lines 436–459); house structure from the superseded staged draft; horn 3, the monotonicity pre-test, the confidence moderator and both design warnings from the five entries under `evidence/literature/targeted_review_q_090/entries/`; the measured numbers in precondition (3) from `SD-039.what_would_answer` and the V3-EXQ-868 manifest. **Invented:** only the reorganisation (promoting the product reading from a fourth-place hedge to a pre-registered horn) and the standalone monotonicity pre-test.

**Also proposed:** add `SD-039` (and arguably `SD-079`) to Q-090's `depends_on`. **Open question the agent declined to settle:** Q-090's *title* still poses a strict binary and arguably should be widened to three horns — but retitling a registered claim is a governance action, not a digestion one.

**Caveat worth your attention:** the agent flags moderate-only confidence in promoting the product reading — it rests on one normative paper plus one fragile empirical crossover, and the Pupillo entry itself notes a PubMed article-type inconsistency ("Review" vs a described primary experiment) that should be checked before leaning on it.

---

### §2.2 — Q-020 · course (a) · **disposition (a) testable now** · `standard`

*Why in the wave:* the other of the two `asked` claims missing `what_would_answer`; fan-in 3.

**Recommended disposition (a)** — the 2026-07-25 reopening exposed an untested REE leg (Resolution A's *non-computation* half) which is decodable on built substrate with a wall-independent DV, so a falsifier can be drafted without re-running the behavioural contrast the C2 cluster has already shown collapses.

```
Q-020 is FUSED: one leg is neuroanatomy already answered by
literature, one leg is a live REE dissociation. Named separately.

OUT-OF-DOMAIN LEG (answered; not REE-testable): "does the biological
hippocampus COMPUTE value -- RPE, utility, outcome evaluation?"
Answered 2026-04-02 by literature synthesis (Resolution A): it does
not; it stores the geometrically-encoded result of computation
performed externally (Bittner 2017 BTSP plateau write-triggers;
Teyler & Rudy 2007 indexing; McGaugh 2004 / Dolcos 2004 BLA
write-depth modulation; Gauthier 2018 reward cells reread as stable
BLA-tagged relays). V3-EXQ-266b does not bear on this leg and did NOT
reopen it -- its own manifest says so. New evidence here routes
through /lit-pull, never through the experiment queue.

REE LEG (live -- this is what the 2026-07-25 reopening actually put
in question): Resolution A asserts a DISSOCIATION -- the map EMBODIES
value-shaped geometry (MECH-073) while the proposer navigating it
computes no value (ARC-007 STRICT; MECH-073's conflict_note calls it
"the value-flat hippocampal proposer"). Only the EMBODIMENT half has
ever been tested: V3-EXQ-375 PASS 3/3, VALENCE_GEOM probe-AUROC
0.982/0.923, VALENCE_ABLATED at chance. The NON-COMPUTATION half --
that the proposer adds no value information the terrain did not
already supply -- is UNTESTED, and it is the half that carries
ARC-007's constraint. That is Q-020's own content. The shaped-vs-flat
harm advantage V3-EXQ-266b measured is ARC-007/MECH-073's behavioural
leg, sits in the C2 harm_advantage_not_reproduced cluster (114a /
120a / 266b), and must NOT be re-run under this claim.

Answered by EXPERIMENT: a SOURCE-DISSOCIATION decoding probe over one
frozen trained agent, deliberately carrying NO behavioural DV, so the
C2 cluster's harm-advantage collapse cannot be re-derived as this
claim's verdict. Decode a per-step harm/safe label from:
(S1) MAP GEOMETRY -- residue_field.evaluate / evaluate_valence at the
visited z_world points;
(S2) PROPOSER STATE -- HippocampalModule.propose_trajectories output
as PROPOSED, read before E3's J(zeta) ranks it;
(S3) the INCREMENT S2 adds over S1 -- AUROC(S1 (+) S2) minus
AUROC(S1), with S2 residualised on S1 so shared variance is not
double-counted. S3 is the load-bearing statistic; S1 and S2 alone are
context.

NON-DEGENERACY PRECONDITION (all four; any failure self-routes
substrate_not_ready_requeue, NEVER a verdict):
(a) TERRAIN LIVENESS, RELATIVE NOT ABSOLUTE. V3-EXQ-266b's P2 floor
was an ABSOLUTE spread >= 1e-4 and passed GREEN at spread 0.0034637
on a probe mean of 17.586 -- a 0.02% modulation riding a large DC
offset, i.e. a constant field with numerical jitter. Register
spread/|mean| against a declared floor, not raw spread.
(b) DECISION RELEVANCE. The terrain term must be able to move
selection: fraction of steps at which argmax J(zeta) differs from
argmax J(zeta) with the residue term zeroed, against a registered
floor. A field with large spread that never flips a rank is inert at
the decision scale however green an absolute-spread gate reads.
(c) SPATIAL COVERAGE. Distinct residue cells visited per episode must
exceed 1 by a registered margin. V3-EXQ-266b measured
mean_cells_per_episode = 1.2 -- the agent barely left one cell, so
there was no positional contrast for geometry to embody, and a field
probed at effectively one location is not a landscape.
(d) DECODER FLOOR + SHUFFLED-LABEL CONTROL. Registered minimum harm
and safe sample counts per seed, plus a label-permuted arm that must
land at chance. This is the representational analogue of 266b's
A2_STATIC no-op control: a contrast without a control that CANNOT
succeed is not adjudicable.

CONFIRMING signature (Resolution A holds; ARC-007 STRICT survives
MECH-073): S1 AUROC above a registered floor, replicating V3-EXQ-375;
S3 increment at or below a registered epsilon and inside the
shuffled-label band, in all seeds. The proposer carries no value
information the geometry did not already supply -- it embodies, it
does not compute.

FALSIFYING signature (Resolution A fails; the conflict_note's A/B
fork reopens): S3 increment above the registered epsilon and above
the shuffled-label band in a majority of seeds. The proposer computes
value of its own, which is exactly what ARC-007's
no-value-computation constraint forbids. The S1 x S3 2x2 SELECTS
which fork: S1 high AND S3 high routes to option (A), revise ARC-007
(the hippocampal stage computes value after all, and INV-014's
representation/regulation separation comes into play); S1 at chance
AND S3 high routes to option (B), reject MECH-073 (value never
entered the geometry and the proposer is doing the work). Apply the
outcome to ARC-022's conflict_note in the same pass -- it names the
same fork and defers to this claim.
```

**Provenance:** the two-leg split, "embodies but does not compute", the phrase *"the value-flat hippocampal proposer"*, and the A/B fork are all lifted from Q-020's `resolution_note` / `evidence_quality_note` and MECH-073's and ARC-022's `conflict_note`s; the two-leg section pattern is copied from Q-019's own `what_would_answer`. All four preconditions derive from numbers in the 266b manifest, which I verified: `terrain_score_spread` 0.0034637 on `terrain_score_mean_probe` 17.586, `mean_cells_per_episode` 1.2. **Invented:** the S1/S2/S3 decoding design and residualised-increment statistic, precondition (b), and the wall-independent-DV choice.

**Two evidence observations that are not flags but that governance should see when it re-reads 266b:** (i) its readiness gate passed on an *absolute* spread floor, which a near-constant field clears; (ii) `per_seed_delta_harm_per_episode = [0.025, 0.100, 0.975]` — seed 456 supplies ~89% of the mean delta and ran a different behavioural regime (`mean_episode_len` 193.8 vs 8.9/7.8). A 39× spread under a same-sign rule is worth stating next to the 6.5% headline. Neither overturns the user-confirmed `weakens`.

**Currency:** SD-004 **has landed** (`status: implemented`), so the `conflict_note`'s "Gated on SD-004" paragraph is dead text. ARC-007's own falsifier ran (V3-EXQ-800) and returned all four arms gate-RED / `substrate_not_ready_requeue`, so Q-020 cannot lean on it as already-executed. Proposal EXP-0257 is `status: gated` awaiting a governance disposition — this draft deliberately targets a **different leg** and does not duplicate it.

**Dissent worth recording:** the agent gives medium-only confidence that S2 is implementable (it read `propose_trajectories`' call site but not `HippocampalModule` internals, so it has not verified a pre-scoring candidate representation is exposed) and that precondition (b) has a clean ablation point in `J(zeta)`. **A `/queue-experiment` pass must confirm both before minting.** If S2 is not separable from E3's scored output, the design does not stand and (f) becomes the honest fallback.

---

### §2.3 — MECH-295 · course (b) · **disposition (a) testable now** · `substrate_ceiling` → **`standard`**

*Why in the wave:* fan-in 4; ceiling note + `pending_retest_after_substrate` + a "Falsifiable:" clause in `functional_restatement` — maximum extraction, minimum invention.

**Category change proposed and worth reading carefully:** `substrate_ceiling` requires the mechanism to have been exercised under **non**-degenerate conditions with a downstream mechanism absorbing the signal. MECH-295 has still never been exercised non-degenerately — but the reason is no longer an absent enabling substrate (that would be `substrate_conditional`); the enabling substrate exists and is in routine use by sibling channels, and only the 812 driver failed to enable it. That is a test-design defect, which is `standard`.

```
ALREADY SETTLED -- do not re-litigate. The behavioural-NECESSITY
reading ("sever the bridge and drive amplification produces no
approach") is TERMINALLY FALSIFIED by V3-EXQ-490j: severed-bridge
ARM_0 still produced approach_commit_rate=1.0 in 3/3 seeds via
parallel architecturally first-class pathways (MECH-216 schema
readout, MECH-290 backward credit sweep, MECH-307 anticipatory
liking, serotonin tonic_5ht benefit_salience). The bridge's
substrate-side firing is likewise settled (V3-EXQ-493 6/6 isolation
PASS; 490j C6/C7/C9 PASS; V3-EXQ-812 C1 cue_fires 127 ON / 0 OFF).
Neither is the open question.

Answered by EXPERIMENT: on a non-degenerate E3 candidate pool, does
the liking-stream's per-candidate approach-cue score_bias actually
change WHICH candidate E3 commits to -- i.e. does the narrowed
MODULATORY reading carry selection authority over and above a
severed-bridge reference arm? The design is already specified and
already built: eval-time cue_gain natural vs 0.0 on the same
per-seed trained agent (the V3-EXQ-812 two-arm shape), scored as a
diff-in-diff on selected-minus-pool-mean goal_proximity.

NON-DEGENERACY PRECONDITION (pre-registered; the run self-routes to
substrate_not_ready_requeue, NEVER to a MECH-295 verdict, if unmet):
(i) mean_proximity_range > 1e-4 across E3 candidates in the cue-on
arm; (ii) mech295_liking_bias_range_mean > 0; (iii) >= 3 cue-fire
ticks, on >= 2/3 seeds. Reference points for what DEGENERATE looked
like: V3-EXQ-490k measured mech295_bias_range_mean = 0.0 with
goal_norm_peak = 0.193; V3-EXQ-812, on the enriched scaffolded
substrate with z_goal now healthy (p2_z_goal_norm_peak = 0.529,
harm_eval_range 0.248, P1 survival 3/3), STILL measured
mean_proximity_range = 0.0 and mech295_liking_bias_range_mean = 0.0,
with a C3 diff-in-diff of ~1e-9 -- and, tellingly,
mean_dacc_bias_range_mean = 0.0 in the same run, i.e. the whole
per-candidate bias plane was collapsed, not MECH-295's channel
specifically. The successor MUST therefore set
candidate_summary_source = "e2_world_forward" (ARC-065 GAP-A;
V3-EXQ-614e autopsy 2026-06-07). Under the default "proposer" the
per-candidate summary is the trajectory's timestep-0 z_world, which
is identical across candidates, so drive * proximity * gain is
uniform and subtracting it cannot move an argmin BY CONSTRUCTION:
the precondition is unsatisfiable and no result is interpretable.

CONFIRMING signature (modulatory reading carries authority): with
the precondition met, selected-minus-pool-mean goal_proximity lift
>= 0.01 in the cue-on arm AND exceeding the severed-bridge arm's
same statistic by >= 0.01 (diff-in-diff), plus a non-zero
argmin_flip fraction between the with- and without-MECH-295
counterfactual scorings, on >= 2/3 seeds.

FALSIFYING signature (modulatory reading fails at selection): with
the precondition met and the cue demonstrably firing, the
diff-in-diff sits at ~0 (indistinguishable from the severed arm)
and argmin_flip fraction is ~0 -- the bias reaches E3 carrying real
cross-candidate spread and still never changes the commit. That
would demote MECH-295 to a write-side-only anticipatory-liking
mechanism with no action-selection authority, leaving the narrowed
claim's "biases approach action scoring" clause unsupported.
Note that approach_commit_rate alone does NOT falsify: it is
saturated by the parallel pathways 490j identified, so it is an
informative-only sanity check, never the load-bearing DV.
```

**Provenance:** the opener restates `functional_restatement`'s "Falsifiable (primary, narrowed-modulatory reading)"; the precondition is the pre-registered `mech295_bias_range_mean>0` guard from `evidence_quality_note` plus 812's own C0/C2 gates; the CONFIRMING thresholds are 812's C3 verbatim; ALREADY SETTLED compresses the 2026-05-31 490j autopsy paragraph. **Invented:** only the causal attribution of the residual degeneracy to `candidate_summary_source` and the instruction to set `e2_world_forward` — derived from `agent.py:5387-5425`/`:6388-6412`/`:7000-7040` and `config.py:3525-3531`, not stated in any MECH-295 field.

**Confidence caveat that matters:** the agent gives only **medium** confidence that `e2_world_forward` alone clears the precondition — it produces spread in *world summaries*, and `goal_proximity = 1/(1+dist)` is a monotone map of those so spread *should* propagate, but no manifest measures `mean_proximity_range` non-zero under it. This is exactly why the precondition must stay pre-registered and self-routing. **If it fails again under `e2_world_forward`, the honest disposition reverts toward `substrate_ceiling` with a new and much more specific gate.**

Two defects to carry into any successor, from 812's own `arm_fingerprint.reuse_ineligible_reasons`: `incomplete_rng_reset` (repair) and `shared_trained_agent_eval_time_toggle_not_independently_trained` (deliberate and correct — severing during training would confound authority with a differently-adapted policy — but restate it as such).

---

### §2.4 — SD-087 · course (b) · **disposition (a) testable now** · `standard`

*Why in the wave:* top of the tractability ranking (carries both a `falsifier` and a `non_degeneracy_precondition`), plus fresh 2026-08-01/02/03 evidence.

**The steering premise I gave this agent was wrong, and it said so.** I briefed it that the live question was the governance-routed "flag from the start of training". It came back with: that is closed (GFLAG-0006), and the *real* live question is bench-vs-production-path (GFLAG-0005). This is the wave's best single result and it came from an agent contradicting its own brief.

```
Answered by EXPERIMENT + AUDIT. Two separable legs. The AUDIT leg is
dischargeable by inspection today; the EXPERIMENT leg is NOT the one
the 2026-08-03 governance routing names.

ALREADY SETTLED -- do not re-litigate:
(1) The flag default. harm_surprise_pe_enabled is still False by
    default (ree-v3/ree_core/utils/config.py:2656, verified
    2026-08-08), so default-trained agents do train z_harm_a against
    the EMA accumulated-harm target. Code fact; needs no run.
(2) Flag-from-start. V3-EXQ-856's ARM_ON already set the flag at
    construction, BEFORE its 50-episode warmup, and the signature
    survived anyway: OFF mean CoV 0.007057 vs ON 0.007421, both ~7x
    below the 0.05 floor, signature in 2/3 seeds in BOTH arms.
    Option (a) is CLOSED, not open. See evidence/reanalysis/
    reanalysis_sd087_flag_from_start_already_tested_20260803T144516Z
    .json. The routed "train-from-scratch-with-flag-ON" successor
    rests on a misreading of 856 and must NOT be queued.
(3) Environment. Q-086/V3-EXQ-857a eliminated environmental
    harshness -- ARM_BENIGN (num_hazards=0) stays CoV-saturated and
    z_harm_a is INVERTED higher, not lower, than ARM_HARSH --
    resolving to calibration_pathology_representational.
This claim owns the operational definition of that signature:
within-episode CoV(z_harm_a) below a 0.05 floor AND inverted
mode-level ordering (shelter > avoid > freeze), scored over
>= MIN_MODE_SAMPLES per mode. Sibling claims point here rather than
restate it. The raw-warmup curriculum scope is owned by SD-086.

AUDIT LEG (no experiment; answerable by source read today):
SATISFIED IN FORM, DEFECTIVE IN CONTENT. SD-020 does now carry a
default_off_scope_note pointing here, so the "scoping is not
recorded" half is discharged. But the recorded scoping is WRONG,
and so is this claim's own title. V3-EXQ-324b never set
harm_surprise_pe_enabled and never called
agent.compute_harm_accum_loss. It builds standalone HarmEncoder /
AffectiveHarmEncoder plus a fresh linear dmg_head and reimplements
the target inline as abs(mean_dmg - dmg_ema): no precision
weighting, no z_harm_a_aux_loss_weight, no REEAgent (REEConfig is
imported for dim validation only). ANSWERED = the corrected wording
lands on both SD-020's default_off_scope_note and this title, namely
that SD-020's stable reading is scoped not to "the flag-on
configuration" but to a BENCH REIMPLEMENTATION that never exercised
the shipped flag path.

EXPERIMENT LEG -- the live question: does SD-020's validated
PE-over-EMA benefit survive when driven through the PRODUCTION flag
path rather than the 324b bench? The lineage silently changed
substrate mid-stream. V3-EXQ-324 DID drive the real flag through
REEAgent and FAILED (1/5 seeds). 324a and 324b dropped to the
standalone bench, and it is 324b's PASS that promoted SD-020 to
stable. No PASS has ever been obtained on the code the claim
describes.
Design: re-run 324b's PE_TARGET vs EMA_TARGET contrast on the SD-022
substrate (limb_damage_enabled=True, num_hazards=8, harm_obs_a_dim=7,
seeds 42-46, EVAL_STEPS=400 with the reset-on-done fix), but drive
the arms via config.harm_surprise_pe_enabled through REEAgent and
compute_harm_accum_loss. Readout stays 324b's own: surprise_corr_pe
vs surprise_corr_ema, plus z_harm_a_mean_norm.

NON-DEGENERACY PRECONDITION (three gates, all must hold):
(i) BRANCH ENTRY -- the ON arm must demonstrably optimise a
    different loss than the OFF arm. self._harm_obs_ema is written
    ONLY inside the harm_surprise_pe_enabled branch of
    compute_harm_accum_loss, so a post-training _harm_obs_ema that
    is non-zero on every ON seed and exactly 0.0 on every OFF seed
    proves entry. This is the witness the 856 reanalysis validated.
    Cite the FUNCTION name, not a line range -- see the citation
    drift note on this claim.
(ii) ARC-016 COUPLING LIVE -- precision_norm =
    min(e3.current_precision/500, 3.0) must vary across steps
    (non-zero variance; not pinned at the 3.0 ceiling nor at 0).
    If it is constant, the production target collapses to a scaled
    copy of 324b's unweighted target and the run cannot distinguish
    the two implementations at all.
(iii) 324's OWN CONFOUNDS CLEARED -- >= 100 harm events per seed,
    and harm_obs_a variance above the 0.0003-0.0007 band that made
    324 uninterpretable. Both are named in SD-020's own
    evidence_quality_note as the preconditions for a clean re-run.
Any gate unmet -> self-route substrate_not_ready. A run failing (i)
tests nothing; a run failing (ii) silently re-tests 324b.

CONFIRMING signature (this claim upheld on its causal half): on the
production flag path, PE_TARGET does NOT beat EMA_TARGET by 324b's
own pre-registered bar -- fewer than 3/5 seeds satisfy C1
(surprise_corr_pe > surprise_corr_ema) AND C2 (surprise_corr_pe
>= 0.15) AND C3 (z_harm_a_norm > 0.01) -- while all three gates
hold. That reproduces 324's FAIL on a now-uncomfounded substrate and
leaves SD-020's stable status unsupported on its own subject.

FALSIFYING signature: the production flag path reproduces 324b --
>= 3/5 seeds passing C1+C2+C3 with surprise_corr_pe in a band
overlapping 324b's [0.44, 0.81]. SD-020's stable reading then does
transfer to the shipped configuration and the bench-vs-agent gap is
immaterial. Note this falsifies only the causal/validity half: the
default-off half survives either way, since the flag is off by
default regardless, and the claim then reduces to the (already
recorded) default_off annotation and should be closed.
```

**Provenance:** ALREADY SETTLED (2) from the reanalysis artifact; (3) from SD-087/Q-086's own notes; gate (i) is the existing `non_degeneracy_precondition` upgraded from a line range to a symbol + `_harm_obs_ema` witness; gate (iii) from SD-020's own `evidence_quality_note`; all CONFIRMING/FALSIFYING thresholds lifted from V3-EXQ-324b's pre-registered criteria, so the contrast is scored on the identical bar as the PASS it challenges. **Invented:** the entire bench-vs-production reframing, gate (ii), and the audit-leg finding that SD-087's own title is false.

**Dissent recorded:** the agent gives medium-only confidence on (a) vs **(f)**. The defensible alternative is: correct the two texts and SD-020's status *first*, then decide whether the production-path run is worth compute at all — because if Q-086's `calibration_pathology_representational` verdict is right, SD-020's benefit may be moot regardless. It chose (a) because the run is a merge of two existing drivers, not a new design, and is the only thing that can settle `stable`. **Unverified risk:** whether `e3.current_precision` actually varies on the SD-022 substrate. Gate (ii) is a genuine readiness risk, not a formality.

---

### §2.5 — SD-086 · course (b), sibling of SD-087 · **disposition (a) testable now** · `standard`

*Why in the wave:* deliberately paired with SD-087 to exercise the skill's sibling rule (shared `scope_note`, same 2026-06-10 intake, same `z_harm_a` mechanism). **The pairing worked** — the two agents converged on a clean ownership split with no drifting duplicate text (see below), and each independently corroborated the other's gate finding.

**Category reasoning:** not `substrate_conditional` (the head is **not** missing — `AffectiveHarmEncoder.harm_accum_head` exists at `stack.py:225-230`, is trained by `compute_harm_accum_loss`, and was live in 664/856/857a via `harm_history_len=10`); not `substrate_ceiling` (nothing downstream absorbs the signal, because the two E3 consumers have never been switched on at all). Hence `standard`.

```
Answered by EXPERIMENT: two arms on the V3-EXQ-664 affective-fishtank
lineage (experiments/_lib/baselines/affective_fishtank.py), matched
seeds and matched config slice, differing ONLY in how z_harm_a is READ
into E3. ARM_NORM keeps the incumbent ||z_harm_a|| read
(e3_selector.py:1182 lambda_eff amplification, :3128 commit-threshold
urgency). ARM_HEAD substitutes at those same two read sites the trained
scalar valuation AffectiveHarmEncoder.harm_accum_head already produces
(latent/stack.py:225-230, trained by agent.compute_harm_accum_loss,
surfaced as LatentState.harm_accum_pred and consumed by nothing today).
MATCHED AUTHORITY is mandatory: the head is Sigmoid-bounded to [0,1]
while ||z_harm_a|| runs ~7.18-7.42 on 664, so each readout must be
standardised (zero-mean/unit-SD over a shared calibration window)
before it enters lambda_eff and urgency, or the arms confound readout
FORM with readout GAIN and the result is uninterpretable either way.

NON-DEGENERACY PRECONDITION: three gates, all evaluated before the
scoring compute; ANY failure self-routes substrate_not_ready rather
than scoring the arms.
(1) LATENT INFORMATIVENESS. The z_harm_a LATENT must itself carry
decodable cross-state information: a linear decode of behavioural mode
(classify_mode) and of harm-event status from the 16-d z_harm_a VECTOR
must clear a pre-registered floor above its own label-shuffled null,
with non-zero cross-seed variance. If the latent is uninformative the
READOUT FORM is not the defect -- no head can recover what is not
there -- and the claim is untestable on this substrate.
(2) INSTRUMENTATION. That decode is NOT answerable from data already on
disk, and the intake routing that called it free re-analysis is wrong:
the lineage's eval_collect stores step_z_harm_a as a List[float] of
||z_harm_a|| only, never the vector. The run MUST persist the per-step
16-d z_harm_a vector alongside its norm; assert the stored array has
z_harm_a_dim columns before Phase 1 begins.
(3) CONSUMER ENGAGEMENT. Both E3 read sites are flag-gated:
affective_harm_scale (default 0.0) gates the lambda_eff amplification,
urgency_weight (default 0.0) gates the commit-threshold urgency, and
NONE of V3-EXQ-664 / 856 / 857a sets either. With both at 0.0 the
downstream conjunct below is VACUOUSLY UNSATISFIABLE -- the readout
range could move arbitrarily and nothing downstream could possibly
follow. Both arms must set both flags non-zero and IDENTICAL, and
engagement must be asserted positively: urgency_applied
(last_score_diagnostics, e3_selector.py:3191) and lambda_eff must each
be non-constant within an arm. An arm whose urgency_applied is
identically 0.0 tests nothing.

CONFIRMING signature: BOTH conjuncts, on the same run.
(a) RANGE. Cross-state dynamic range of the readout rises in ARM_HEAD
versus ARM_NORM by a margin scaled on the SD of the paired-by-seed
delta plus a pre-registered absolute floor. Report it as the same
within-episode CoV statistic the lineage already uses (COV_FLOOR 0.05)
plus the per-mode ordering, so the result is directly commensurable
with the 664 signature. Use a PAIRED-BY-SEED statistic: seeds are
shared identically across arms via torch.manual_seed(seed), and the
V3-EXQ-857/857a pair established that the unpaired pooled-SD form
discards a deterministic per-seed effect as noise and fails a gate the
paired form clears on the same data (0.388 versus 2.20).
(b) DOWNSTREAM. At least one live consumer moves measurably: the
commit-threshold distribution (effective_threshold / urgency_applied)
or the lambda_eff distribution shifts beyond the seed-noise band,
paired by seed.

FALSIFYING signature, three distinguishable outcomes.
(i) NO RANGE GAIN. ARM_HEAD's cross-state range does not clear the
margin: the trained scalar head is not a better readout and the claim's
own prescription fails on its own terms.
(ii) RANGE RISES BUT NOTHING DOWNSTREAM MOVES -- the informative
failure, and the one to report loudest. It does not say the readout is
unfixable; it says the readout is NOT LOAD-BEARING, i.e. E3's
consumption of z_harm_a is too weakly weighted for any readout
improvement to express itself, which relocates the defect from readout
FORM to consumer GAIN and is a WEAKENS for SD-086 as stated. It is
distinguishable from a precondition-(3) failure only because that
precondition demands urgency_applied and lambda_eff be demonstrably
non-constant first; without that assertion the two are confusable.
(iii) BOTH ARMS FLAT with precondition (1) met: points at the E3 read
path itself rather than at either readout form.

SCOPE (CANONICAL -- SD-087 and Q-086 should CROSS-REFERENCE this text
rather than restate it): every number in this lineage comes from a
~50-episode RAW warmup with scaffold_train_harm_pathway off and no
scaffolded_sd054_onboarding (the V3-EXQ-664 env and schedule,
reproduced verbatim by V3-EXQ-856 and 857a through the shared baseline
module). Conclusions are scoped to raw-warmup agents unless re-run on
the curriculum-trained configuration; see
project_stageh_harm_pathway_training and the 603i/603k harm-pathway
co-training. The 664 SATURATION-AND-INVERSION SIGNATURE is likewise
defined here and owned here: within-episode CoV of ||z_harm_a|| below
0.05 together with inverted mode-ordering (shelter > avoid > freeze),
measured on the harsh 664 environment (num_hazards=4,
hazard_food_attraction=0.7).
```

**GATE STATUS — the headline: RELEASED.** SD-086's notes say "should not be built until SD-087 and Q-086 report", and the intake states the gate's purpose explicitly: *"if the PE target alone restores range, no new head is needed."* Both probes have reported and the gate resolves **in SD-086's favour on both legs** — 856 showed the PE target does *not* restore range (closing the disjunct that would have made SD-086 unnecessary), and 857a eliminated environment, resolving positively to `calibration_pathology_representational`, which is precisely SD-086's territory: the claim that the pathology is in how the latent is **read**.

On the residual: SD-087's remaining hypothesis is a **training-schedule** claim; SD-086 is a **readout-form** claim. They are orthogonal, and SD-086's own precondition (1) is the seam — if the residual is right and the latent is uninformative, precondition (1) fails and the run self-routes `substrate_not_ready`, which is the correct cheap answer rather than a block.

**Sibling ownership split (this is the part to check, since drift between paired claims is what the rule exists to prevent):** both agents independently arrived at the same allocation, and it is coherent —

| text | owner | other side |
|---|---|---|
| raw-warmup curriculum-scope condition (full text) | **SD-086** | SD-087's `scope_note` already points at it correctly — **no change needed either side** |
| 664 saturation-and-inversion signature (operational definition + thresholds) | **SD-087** (it pre-registered `COV_FLOOR=0.05`, `MIN_MODE_SAMPLES`) | SD-086 references it as context only |

Both drafts above respect this: SD-087's says "The raw-warmup curriculum scope is owned by SD-086"; SD-086's marks its scope paragraph CANONICAL. **One open suggestion neither agent acted on:** Q-086 may be the better long-term owner of the *signature* definition, since its whole subject is explaining that signature and it holds the adjudicated verdict. That is a governance call.

**Provenance:** both conjuncts, the margin form, the named consumers, and the "range rises but nothing downstream moves = not load-bearing" case are lifted in substance from SD-086's existing `falsifier`; the decodability floor and `substrate_not_ready` self-route from its existing `non_degeneracy_precondition`. **Invented, all forced by the currency check:** precondition (2) (the lineage persists only the norm, so the existing precondition *cannot be evaluated at all as written*), precondition (3), the matched-authority standardisation, the paired-by-seed form, and failure cases (i)/(iii).

**Medium-confidence caveat:** whether the existing `harm_accum_head` is the right head to swap in. It is structurally what the claim asks for and already trained, making it the cheapest valid ARM_HEAD — but it is trained to predict accumulated harm, so it **may inherit the very calibration pathology it is meant to cure**. A purpose-trained valuation head is the alternative; the falsifier is agnostic, and the queue entry should state which and why.

**One more finding attached to this claim:** SD-050 carries a `readout_precondition_note` declaring its own falsifier uninterpretable while SD-086's decode-floor guard fails — and that guard has never been run and (per precondition (2)) **cannot be run retrospectively**, contrary to the 2026-06-10 intake's routing which called it "free" re-analysis. So SD-050's (and per the intake, MECH-302's) testability is blocked on an experiment that does not exist and is not queued. That dependency deserves an explicit governance decision rather than sitting implicit in a note.

---

## §3 — Systemic findings (NOT chipped — your call whether to spin these off)

Per the trial brief I spawned **no chips**. Each of these is a candidate; each needs its own first-step re-verification, because the counts below come from single scans.

### §3.1 — "validated against a code path no run ever enabled" may be a class, not two incidents

Two of five claims in this wave (SD-020/SD-087; SD-086) assert behaviour of a flag-gated path that is default-off and unset in every run of their own evidence base. SD-087's own `notes` already anticipated it: *"Consider a standing default_off annotation audit across other claims (intake next-step 4)."* This wave is evidence that suggestion is worth acting on.

**Why it is not merely cosmetic:** in the SD-020 case it produced a `stable` promotion. A claim can be individually well-evidenced and still be evidenced *about something else*. Nothing in the pipeline currently checks that a promoting run's config actually enabled the mechanism the claim names.

**Shape of the audit if you want it:** for each claim citing a config flag, resolve the flag's default and check whether the runs in its `live_status.evidence` / manifests set it. Mechanisable. **Re-verify the two instances above first** — a scan that over-flags will be ignored, exactly as the `grep -L REGISTERED` thought-intake heuristic did at 65× over-statement.

### §3.2 — 36 claims carry 76 `file.py:NNN` citations, and they drift fast

Measured today: **36 claims, 76 citations** of the form `<file>.py:<line>` (examples: `INV-006` `field.py:620`/`:884`; `ARC-001` `agent.py:3012`; `MECH-180` `ree_core/agent.py:10194`). Every one I checked in this wave had drifted; one by **~1150 lines**, and one drifted a further **~190 lines in five days**. A claim citing a stale `file:line` sends a reader to unrelated code with no error.

Bounded, mechanically checkable (resolve each citation, compare the symbol at that line to the surrounding claim text), and the fix is a convention change: **cite symbols, not lines.** GFLAG-0010 covers 3 of the 36.

### §3.3 — digestion's course (a) is exhausted; the remaining work is almost entirely course (b)

| stance | total | missing `what_would_answer` |
|---|---|---|
| `asked` | 98 | **2** (2%) — Q-020, Q-090, both digested in this wave |
| `believed` | 804 | **613** (76%) |
| `shown` | 92 | 79 (86%) |

**Planning consequence if you make this recurring:** after this wave, course (a) is **empty** — the next pass has no `asked` claims left to digest and must run entirely on course (b). That is fine (613 candidates, and the ripest are readily rankable), but it changes what "ripest-first" means: fan-in is flat across the believed pool (max 5), so **tractability signals do all the ranking work.** The signals that worked here, in order of yield: an existing `falsifier`/`non_degeneracy_precondition` field pair (near-free extraction), a "Falsifiable:" clause in `functional_restatement`, and a `ceiling_routing_note` + `pending_retest_after_substrate` (which reliably turned up *stale gates*, this wave's most valuable output).

**A second-order note on the skill's own Step 6 check.** Step 6 says to confirm "the missing-`what_would_answer` warning count dropped by EXACTLY the number of claims you digested". That check **cannot work for course (b)**: `validate_claims.py` only warns for *asked-bucket* claims (today: 2 warnings, Q-020 and Q-090). Digesting five `believed` claims would move that counter by zero. If you make this recurring, the wave-completion check needs a different statistic — e.g. a direct count of `what_would_answer` keys, which today is **300 / 994**.

### §3.4 — `TASK_CLAIMS.json` holds a malformed entry

Index 55 is literally `{"status": "active"}` — no `session_id`, no `claimed_at`, no `resources`. It counts as an active claim in any naive scan (it did in mine) and can never go stale, since staleness is computed from `claimed_at`. Trivial to remove; I did not, because hand-editing `TASK_CLAIMS.json` is against the standing rule (use `task_claim.py`), and `task_claim.py` has no verb for "delete a junk entry". Worth either a `task_claim.py prune-malformed` verb or a one-off fix.

### §3.5 — 17 `legacy` claims sit in the `believed` bucket

All 17 `status: legacy` claims derive to `epistemic_stance: believed`, several with titles that literally say *"Legacy: resolved in favour of…"* or *"Retired…"*. They are counted among the 804 `believed`. This is a stance-derivation question, not a data-entry error — should `legacy` short-circuit the derivation? Small and cosmetic next to §3.1/§3.2, recorded for completeness.

---

## §4 — Process notes on the trial itself

**What worked.** The wave of 5 returned 5 usable drafts with no deferrals. Steering each agent at a *specific unresolved question* (rather than "digest this claim") is what produced the currency findings — every one of the three stale gates came from the standing "verify, do not assume" instruction, not from the falsifier task. **The best single result came from an agent contradicting the premise I gave it** (§2.4), which is an argument for briefing agents with a stated premise *and* explicit licence to reject it.

**The sibling pairing (SD-086/SD-087) paid off** and is worth repeating: two claims sharing a mechanism, dispatched together with an explicit ownership instruction, produced a coherent split and mutual corroboration instead of two drifting descriptions.

**Deviation from the skill, deliberate:** agents were dispatched with `run_in_background: false`. A headless `claude -p` session has no later turn, so awaiting background notifications would have ended the process with the work uncommitted. Per the dispatcher's contract.

**Verification discipline:** I independently re-verified every load-bearing agent finding before raising a flag — the 324/324a/324b grep counts, the config defaults and line drifts, the `harm_accum_head` existence, the 812 manifest numbers, the 266b gate numbers, the reanalysis artifact, the staged-draft file. Two agent claims I did **not** independently verify are marked as such in §2.3 (the `candidate_summary_source` causal mechanism) and §2.2 (S2 implementability).

**Cost:** 5 agents, ~689k subagent tokens, ~7 min wall clock for the wave.
