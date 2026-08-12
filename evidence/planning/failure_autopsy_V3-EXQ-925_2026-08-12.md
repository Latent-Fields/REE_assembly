# Failure Autopsy: V3-EXQ-925 (E3 F-dominance frozen-replay causal harness)

**Generated:** 2026-08-12T16:47:22Z
**Scope:** single target
**Status:** confirmed
**Session:** pensive-franklin-1e285b (worktree), user-directed `/failure-autopsy V3-EXQ-925`
**Trigger:** `experiment_purpose: "diagnostic"`, `claim_ids: []`, `outcome: PASS`, no adjudication flag — the skill's second trigger (a claim-free diagnostic PASS still requires autopsy; 2026-08-07 correction). This is not a FAIL post-mortem.

## 1. Dry-run gate (Step 2a)

No `dry_run` key present on the manifest (absent = falsy). `elapsed_seconds = 8030.75` (~2.23h), consistent with 3 seeds x (60 P0 + 40 P1) episodes x 200 steps at real budget — not a smoke's truncated schedule. `queue_id V3-EXQ-925` is already absent from `ree-v3/experiment_queue.json` (removed on completion, per standard queue-completion behaviour). `check_dry_run_citations.py` returned `UNKNOWN` only because the manifest is not yet materialised on disk in the shared `REE_assembly` checkout (see "Recovery/access note" below) — not because of genuine ambiguity. Manually confirmed real run: dry_run absent, elapsed_seconds matches full budget, `per_seed_event_counts` non-trivial (`{"42": 1186, "43": 0, "44": 1307}`).

`dry_run_checked: true`. No dry runs excluded (single real target).

**Recovery/access note.** The shared `REE_assembly` main checkout was diverged (14 ahead / 9 behind `origin/master`) when this autopsy started, with several other sessions' uncommitted derived-artifact edits sitting in the working tree. The V3-EXQ-925 manifest existed only in an unmerged `origin/master` commit (`84b8fb51bf`). Rather than merge/rebase the shared checkout (out of scope for this autopsy, and risky against concurrent sessions), the manifest was read directly via `git show origin/master:<path>` into a scratch file for analysis. `claims.yaml` was verified byte-identical between local HEAD and `origin/master` before being read from disk directly. No write touched the shared checkout's divergence; that resolution is left to whichever session/`/session-land` cycle owns it next.

## 2. Facts reconstruction

**Run:** `v3_exq_925_e3_fdominance_frozen_replay_causal_harness_20260812T090142Z_v3`, ran on `ree-worker-3` (linux-x86_64-py3.10-torch2.12.0+cpu), substrate commit `9bcde4cb63` (clean), `substrate_hash` present and `substrate_stable_across_run: true`.

**Recording provenance:** `validate_recording.py --paths <manifest>` reports 0 always-core gaps, 0 thin-pack drops, 0 schema warnings — `recording_schema`, `substrate_hash`, `machine`/`machine_class`, `elapsed_seconds`, full `config`, and explicit `seeds` are all present. No recording-debt finding on this run.

**Design.** P0 trains SD-056 (E2 world-forward action-conditional divergence, the validated V3-EXQ-643a recipe) for 60 episodes per seed so E3's candidates genuinely differentiate in `z_world` space. P1 captures 40 episodes of *genuine fresh* E3 selections (latch-cleared per V3-EXQ-924's fix) and replays six counterfactuals **inline**, arithmetically, on the captured per-candidate score vectors — C0 (factual self-consistency), C1 (literal-F lesion, `f_weight=0`), C2 (F-association scramble), C3 (attenuation ladder), C4 (MECH-448 eligibility-envelope toggle), C5 (competitor/`gated_policy` lesion). Independent criterion: env-native ground-truth distance to the nearest hazard after the candidate's first action (never a network output).

**Purpose, explicitly claim-free by design:** discriminate among four causal hypotheses about *why* literal F appears to dominate E3 selection (this bears on MECH-439's own framing, but does not itself test MECH-439/ARC-062/ARC-107/108/110 — `claim_ids: []` is deliberate, not an oversight):

- **H1** literal-F dominance — F itself has candidate-specific causal authority sufficient to suppress useful competitors.
- **H2** primary-field dominance — not literal F specifically; the broader eligibility/pre-modulatory pathway retains privileged authority even when literal F is attenuated.
- **H3** upstream insufficiency — apparent dominance is mainly downstream of inadequate candidate differentiation; competing channels don't yet carry useful per-candidate signal.
- **H4** conditional specialisation — F controls where informative, competitors gain control where their information is useful; substantially appropriate, not a defect.

**Readiness.** 2/3 seeds cleared both floors (`cand_world_pairwise_dist_mean >= 0.02`, `gated_policy_std_across_K_mean >= 1e-6`): seed 42 (0.1239, 0.00119), seed 44 (0.1568, 0.00350). Seed 43 failed the *second* floor only (0.0239 pairwise-dist, clears; but `gated_policy_std_across_K_mean = 7.45e-9`, below floor) — its competitor channel carried essentially zero per-candidate signal despite SD-056 itself training adequately for that seed. This is a per-seed training-reliability gap in the competitor channel, not a design defect (`n_ready_seeds: 2`, `per_seed_event_counts: {"42": 1186, "43": 0, "44": 1307}`).

**Aggregate (2 ready seeds, 2493 fresh events, 2348 disagreement events, 94.2%):**

| Statistic | Value |
|---|---|
| `committed_fraction` | 0.000 |
| `selection_entropy_normalised_mean` | 0.99820 (1.0 = uniform) |
| `c1_total_variation_mean` (F-lesion) | 0.0005177 |
| `c1_delta_p_safer_mean`, disagreement-conditioned | -0.0000016 |
| `c1_frac_moved_toward_safer` | 0.3756 |
| `competitor_had_influence_factual_f_rate` | 0.0858 |
| `competitor_had_influence_lesioned_f_rate` | 0.0959 |
| `flip_prob_c4_eligibility_changes_winner` | 0.000 |
| `c0_probs_reconstruction_max_abs_err_worst` | 7.87e-09 (replay validity) |

`non_degenerate: true`, `degenerate_metrics: {}` — the degeneracy self-check passed; this is not a structurally-pinned null.

**Driver's own classification (`classify_hypotheses()`), verbatim structure, none of the four hard-threshold branches for H1/H2/H4 fired cleanly:**

1. *NEAR-UNIFORM SELECTION* — at `selection_entropy_normalised = 0.998` against `score_range_mean` vs `temperature_mean=1.0`, the softmax is essentially flat: **no channel, F included, meaningfully steers the choice**. This is explicitly flagged by the driver as materially different from "F dominates and suppresses competitors" — V3-EXQ-924 found F = ~96% of score **temporal variance**, but only **cross-candidate spread within a decision** can move a choice, and the two can diverge sharply.
2. *SELECTOR REGIME* — `committed_fraction = 0.000`: the selector predominantly **sampled** from `softmax(-scores/T)` rather than taking the committed argmin throughout. The driver's own note: *"MECH-439's 'committed-selection variance monopoly' framing presumes committed selection, and commitment was largely not engaged here."*
3. C1 moved the distribution (TV 0.0005) with **no consistent direction** toward or away from the independently-preferred candidate (`delta_p_safer ~ -0.0000`) — neither the H1-supportive branch (`delta_p_safer > 0.01` and `frac_toward > 0.5`) nor the H4-supportive branch (`delta_p_safer < -0.01`) fired.
4. MECH-448 eligibility toggling rarely changes the winner (0.0%) — no evidence for H2 as an independent locus of authority beyond literal F.
5. The H3-supportive branch (`competitor_tv < 1e-9 and competitor_influence_factual < 0.05`) did **not** fire — `competitor_influence_factual = 0.0858` narrowly exceeds the 0.05 threshold. Nor did the "near-zero in both conditions" branch fire (`competitor_influence_lesioned = 0.0959`, above 0.05). H3 is a **near-miss**: both factual and F-lesioned competitor influence sit in a weak, ambiguous middle zone (0.086, 0.096) rather than cleanly confirming or refuting upstream insufficiency.

## 3. Claim-layer mapping (Step 3)

**No claim is adjudicated by this run** (`claim_ids: []`, by design). This is not an oversight to correct — the driver's own docstring states explicitly it "does not test MECH-439/ARC-062/ARC-107/108/110 themselves." The four-layer table below therefore has `claim_alignment: n/a`.

For context (read, not written by this autopsy): MECH-439 is currently `status: candidate`, `epistemic_category: standard` (already demoted 2026-07-09 under GOV-CEIL-1 ceiling-exhaustion, hit count corrected to 9 as of 2026-08-10). ARC-062 is `epistemic_category: substrate_ceiling`, `v3_pending: true`. ARC-108/ARC-110 are `substrate_conditional`. MECH-448/449 are `standard`. None of these is touched by this run's `evidence_direction` (`"diagnostic"` on the manifest) — but the SELECTOR REGIME finding (item 2 above) speaks directly to the premise MECH-439's own evidence_quality_note rests on (see Section 7, candidate note).

## 4. Biological-reference triage (Step 4)

**Closest mammalian reference:** action-selection via competing channels feeding a common decision variable, arbitrated by a basal-ganglia-like gate, with commitment triggered by a variance/confidence threshold (accumulator/drift-diffusion-style dynamics — `committed = running_variance < commit_threshold` in `e3_selector.py`). Softmax-over-scores as a stochastic selection rule is a standard reduction of this class of model.

**Is this a faithful translation or a formal-definition import?** Both, layered: the variance-threshold commit gate is a biologically-motivated reduction (BG-style "wait until confident enough to commit"); the softmax-over-scores sampling when uncommitted is closer to a formal reduction (Luce choice / softmax exploration), used here as the fallback regime.

**Does the failure resemble a missing biological dependency?** Yes, and this is the load-bearing biological reading: in accumulator/DDM-style models, **near-uniform choice under low signal-to-noise (small score range relative to decision noise) is the expected signature of weak evidence, not a defect**. SD-056 training moved candidate differentiation from ~0.0000 (untrained, collapsed) to 0.12-0.16 (trained) — real, but modest relative to what a fully mature encoder might produce. Biologically, an organism whose candidate-action value estimates are only weakly differentiated *should* select close to uniformly among them; forcing "commitment" onto a weakly-differentiated evidence stream would be the less biologically faithful choice. This reading favours **H3 (upstream insufficiency)** as the qualitatively best-supported explanation even though the driver's own hard-threshold classifier didn't cross the line to confirm it (Section 2, item 5) — the numbers sit right at the boundary, consistent with "real but not yet strong" upstream signal rather than "genuinely absent."

**Lit status:** no dedicated biology/ML literature entry exists yet on "variance-share vs absolute steering authority in noisy multi-channel action selection" specifically for this substrate's mechanism (distinct from the existing SD-056 world-forward literature, which addresses representational collapse, not selection-scale). Not commissioning a `/lit-pull` from this autopsy alone (routing below is `/queue-experiment`, per the user's confirmed choice); flagged here as a gap a future `/lit-pull` on the discovered question could close.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | Deliberately claim-free; discriminates among causal explanations for MECH-439's mechanism without testing it |
| Biological reference | partial | Accumulator/DDM-style low-SNR near-uniform selection is the *expected* biological signature of weak evidence — favours H3 qualitatively, though not confirmed by the driver's own hard thresholds |
| Prerequisites | immature | SD-056 trains cleanly in aggregate (0.0165->0.1531 pairwise distance over 60 P0 episodes) but only 2/3 seeds cleared BOTH readiness floors; competitor-channel (`gated_policy`) training reliability across seeds is itself weak (one seed: std ~7e-9) |
| Implementation completeness | partial | Only 1 of ~7 documented modulatory channels exercised (`gated_policy`); `use_gap_scaled_commit_temperature` (the substrate's own mechanism for producing committed selection under narrow score gaps) left at its default `False` -- consistent with 1345/1348 experiments in the whole corpus, so not an unusual choice, but its absence is mechanically why commitment never engaged (`committed_fraction=0.000`) |
| Environment adequacy | adequate | `CausalGridWorldV2` config matches the validated 643a/604a/569d combination; not implicated |
| Measurement adequacy | adequate | Recording standard fully satisfied (0 gaps); replay reconstruction validated to 7.87e-9 vs the selector's own recorded distribution; degeneracy check passed |
| Integration adequacy | coupled, weakly differentiated | E2/E3/SD-056/MECH-448 all wired and firing; the joint effect of modest candidate differentiation x default temperature=1.0 produces near-flat selection -- not an integration failure per se |
| Scale / capacity | likely insufficient (candidate differentiation) | 0.12-0.16 achieved (real, vs ~0.0000 untrained) but modest; proximate cause of the near-uniform read |

### GOV-FAILLOC-1 failure-location classification

Applied here even though the outcome is `PASS` and `claim_ids=[]`, because the same discipline bounds how strong a read this run licenses about the underlying mechanism:

- **MECHANISM** (E3 selector authority mechanism itself): **not established** — Implementation completeness reads `partial` (untested `use_gap_scaled_commit_temperature` axis; only 1/7 competitor channels exercised).
- **MEASURES**: **established** — Measurement adequacy reads `adequate` (validated recording, replay reconstruction to 7.87e-9, degeneracy check passed).
- **ENVIRONMENT**: **established** for what this design intended (matches the validated 643a/604a/569d combination); the untested commit-temperature regime is a *design-axis gap*, not an environment-adequacy defect.

**Net classification: MIXED — this is not evidence that "REE's selector is broken," nor a clean confirmation of any single H1-H4 hypothesis.** Because Implementation reads `partial`, the correct read per the failure-location discipline is bounded: the near-uniform/uncommitted regime finding is real and informative on its own terms, but it does not licence eliminating or confirming H1, H2, or H4, and only weakly favours H3.

## 6. Cluster pattern

N/A — single target, not a cluster.

## 7. Learning extracted and repair pathway (Step 7)

**Node classification** (work-graph debt vocabulary): `complex (probe-gated) / puzzle (known rules)` — the H1-H4 frame is well-posed, but a missing fact (whether committed selection, once engaged, changes the picture) blocks a clean discrimination. This is a spike, not a build.

**Learning extracted:**
1. Variance-share (temporal, ~96% per V3-EXQ-924) and absolute cross-candidate steering authority can diverge sharply; F-dominance claims resting on variance-share alone are not licensed to claim behavioural authority without checking `selection_entropy_normalised` and `committed_fraction` directly.
2. This substrate, at its corpus-standard default configuration (`use_gap_scaled_commit_temperature=False`, temperature=1.0), essentially never engages committed (argmin) selection — `committed_fraction=0.000` across 2493 events, 2 seeds. MECH-439's own "committed-selection variance monopoly" framing presumes an operating regime this default configuration does not, in practice, occupy.
3. H1/H2/H4 are not eliminated by this run (numbers land in an ambiguous middle, and the regime confound means this may not have been a fair test of any of them under MECH-439's own premise). H3 is a near-miss, qualitatively favoured by the biological-reference reading (Section 4) but not confirmed by the driver's own hard thresholds.
4. Per-seed training reliability of the competitor channel is itself weak (1/3 seeds: zero per-candidate signal despite SD-056 clearing its own floor) — this bounds how much confidence any single-run competitor-influence reading can carry.

**User-confirmed disposition (Step 8 interactive gate, 2026-08-12):**

- **H1-H4 resolution:** leave all four **alive** in the frozen hypothesis-space ledger; register the SELECTOR REGIME / near-uniform-scale confound as a **new discovery leg (H0)**, since it was not one of the four pre-registered hypotheses and was only revealed once the counterfactual-replay arithmetic bug (fixed during this session's authoring, per the driver's own "Design evolution" notes) was corrected.
- **Routing:** `/queue-experiment` **same-question redesign** (new letter, not a new EXQ number) that engages committed selection — either by enabling `use_gap_scaled_commit_temperature` or by restricting the disagreement-conditioned analysis to committed-only ticks under an extended-training / wider-score-range configuration — **before** re-testing H1-H4. This is not a blind re-queue of the same configuration circling the same ceiling; it targets the specific regime gap this run surfaced. (Note: `claim_ids=[]` means the mechanical re-derive brake does not apply here — there is no claim to count ceiling-hits against — but the same spirit is honoured by design: the redesign changes what is tested, it does not repeat the identical config.)
- **MECH-439 note:** draft a candidate note (below) for `/governance`'s Step 2b/8 review. This autopsy does not write to `claims.yaml`; the decision whether/how to attach it is governance's.

**Candidate note for MECH-439's `evidence_quality_note`, drafted for `/governance` review only (not applied here):**

> 2026-08-12 (failure_autopsy_V3-EXQ-925_2026-08-12, informational, `claim_ids=[]` on the adjudicating run -- does not itself weaken or strengthen MECH-439): V3-EXQ-925's frozen-state causal-replay harness found `committed_fraction=0.000` across 2493 fresh E3 selections (2 seeds) at this substrate's corpus-standard default configuration (`use_gap_scaled_commit_temperature=False`, temperature=1.0) -- the selector predominantly sampled from a near-uniform softmax (`selection_entropy_normalised=0.998`) rather than taking a committed argmin. MECH-439's "committed-selection variance monopoly" framing presumes committed selection is the substrate's typical operating regime; this run's finding is that, at default configuration, it largely is not. This does not itself falsify or weaken MECH-439 (the run adjudicates no claim), but it bears on how strongly any PRIOR MECH-439 evidence resting on committed-selection assumptions should be read, IF that prior evidence also ran uncommitted -- an audit of the 9 confirmed `substrate_ceiling` autopsy hits' configurations was NOT performed by this autopsy and would be needed before drawing that conclusion. Recommend `/governance` weigh whether to (a) attach this note as-is, (b) commission an audit of the 9 hits' `committed_fraction`/temperature configuration before attaching anything, or (c) treat as informational only pending the queued regime-matched re-test (V3-EXQ-925's successor letter).

## 8. Hypothesis-space ledger (Step 9b)

New question registered: `e3_fdominance_causal_discrimination` (Mode B same-cycle registration for H1-H4, Mode C discovery for H0). See `hypothesis_space_registry.v1.json` and `hypothesis_space_integrity.md` (regenerated alongside this artifact). No `growth_restriction` applies (new question, not an addition to an existing one).

## 9. Re-derive brake / granularity-debt recurrence (Step 7 mechanics)

**N/A — `claim_ids=[]`.** Both mechanics operate over `targets[].claim_ids`; there is nothing to count. Noted for completeness, not skipped silently.

## 10. Recommended structured routing (JSON companion)

See `failure_autopsy_V3-EXQ-925_2026-08-12.json`. `routing: "queue-experiment"`. `recommended_substrate_queue_entry.action: "none"` (this is a test-design gap, not a substrate build gap -- the mechanisms needed, `use_gap_scaled_commit_temperature` and the eligibility envelope, already exist and are already built; MECH-448/449 are already `standard`).
