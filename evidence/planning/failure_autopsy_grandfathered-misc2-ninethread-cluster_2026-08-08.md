# Failure Autopsy: ARC-021/MECH-069, MECH-072, MECH-029, MECH-113, MECH-093/135, MECH-098/SD-007, MECH-128/Q-002, MECH-075/163, MECH-188/INV-054/Q-034 -- 43 nominal / 30 formal targets

**Generated:** 2026-08-08T19:22:21Z
**Scope:** cluster (9 threads, round-4 grandfathered-backlog sweep, largest batch)
**Status:** confirmed (Step 8 interactive gate: user confirmed folding the four-thread seeding-density gap into ONE shared substrate-queue note rather than four independent entries)

## Coverage-check methodology note

A full-corpus grep (not just the round-3 named files) was necessary and found real coverage the narrower search missed: `108` is effectively covered by `failure_autopsy_V3-EXQ-108a_2026-08-02.json`'s own cross_reference_note naming it as the original FAIL it replicates (not a PASS, as initially suspected), and `396a` (all 3 timestamps) is covered by `failure_autopsy_V3-EXQ-032-family_2026-07-26.json`, a file outside the four round-3 grandfathered files. Recommend future rounds always do a full-corpus sweep.

## Thread 1 -- ARC-021/MECH-069 incommensurability (1 run, genuinely new)

`004` (2026-03-16): no autopsy target exists, though already directly indexed as evidence in ARC-021's claims.yaml note (2026-08-06 auto-tagging, `mixed`, conf 0.5). 5/6 criteria met; the absolute/negative-control criterion (C1, SEPARATE calibration_gap) fails at near-zero. Claim's own note is explicit: the load-bearing test (isolating channel separation as the causal factor) has never been run. **MECH-069 has no targeted biology review at all** -- genuine `/lit-pull` gap. Recommended: `measurement_gap`, `mixed` (unchanged), routing `/queue-experiment` (the actual merged-vs-separate ablation) + `/lit-pull` (MECH-069).

## Thread 2 -- MECH-072 world-delta gating (2 near-duplicates)

Both `180545Z` variants (prefix-dir and suffix-dir on-disk copies) are `metrics.json` byte-identical (excl. run_id/timestamp) to the already-covered `082932Z` target in `failure_autopsy_grandfathered-superseded-batch1_2026-08-08.json`. MECH-072's claim note already cites this exact defect and has since moved through EXQ-213 PASS and EXQ-877 FAIL (confirmed 2026-08-03) refining the same discriminator-gate question. `governance-note-only`, extend existing disposition.

## Thread 3 -- MECH-029 default-mode/breath-oscillator (3 runs, part of the shared seeding-gap note)

`065`, `080` (superseded by `201` same-day family), `201` (explicit `supersedes: V3-EXQ-080`): all three show `n_uncommitted_steps=0` -- the ARC-016 commitment gate never releases into the divergent/uncommitted-mode window the claim predicts higher variance in. Claim's own note already states this precisely: substrate-limited, non-informative, `evidence_direction: unknown (scoring_excluded)`. See the shared substrate-gap finding below.

## Thread 4 -- MECH-113 self-maintenance (3 runs, genuinely new, DISTINCT from the shared note)

`075d`, `142`x2: the strongest structural pattern in the batch -- **SELF_MAINT_ON and SELF_MAINT_ABLATED produce numerically identical D_eff trajectories in all three runs** (1.00x, 0.997x, ~1.00x respectively). The ablation flag appears to have zero functional effect on the substrate -- an implementation stub, not a fair test of the homeostatic-maintenance claim. `075d` (chronologically first, same signature) is not yet folded into the claim note, which currently cites only the two `142` runs. No existing `substrate_queue.json` entry for MECH-113. Recommended: `competence_implementation_gap`, `weakens`, routing `/implement-substrate` (`create` -- wire the ablation flag to actually disable the mechanism). **This is a genuinely distinct implementation gap** from the era-specific seeding-density confound affecting Threads 3/7/8/9 -- do not fold it into the shared note.

## Thread 5 -- MECH-093/MECH-135 heartbeat/rollout (3 runs)

`097`: C1 (rate-modulation-gap metric) fails in the wrong direction (-0.74 vs required >=2.0) while behavioral C2/C3 PASS cleanly -- a real downstream effect the metric mis-targets. MECH-093's claim has since accumulated strong PASS evidence (EXQ-396b, EXQ-505) isolating the same channel cleanly; this run is scientifically superseded, never formally tagged as such. `104`/`105` (095419Z/095425Z): empty pack metrics, pre-diagnostic early-same-day attempts ~3h before the already-covered later-same-day sibling family (`123736Z` group, `measurement_test_design_defect`/`superseded`). All three `governance-note-only`, extending existing dispositions.

## Thread 6 -- MECH-098/SD-007 c1fail cluster (4 runs, all effectively covered)

`110`x2: byte-identical to the already-covered `133711Z` emission (`failure_autopsy_grandfathered-betagate-reafference-cluster_2026-08-08.json`, "1 of 3 byte-identical emissions" -- these are the other two). `111`, `118`: identical-timestamp duplicates under shorter filenames, already covered by `failure_autopsy_grandfathered-goalseeding-cluster_2026-08-08.json` (self-documenting SD-007 precondition gates, not crashes). No fresh diagnosis.

## Thread 7 -- MECH-128/Q-002 E1 goal-conditioning (3 runs, part of the shared seeding-gap note)

`147`, `147a`, `229`: clean, well-powered, triple-replicated null -- interaction metric (does goal-conditioning selectively reduce goal-relevant E1 prediction error) is essentially zero across all three runs and multiple seeds each. Claim note cites "SD-005 not yet implemented" as blocker; **this is now stale** -- SD-005 status is `implemented`. Recommended: `measurement_gap`, `weakens`/`mixed`/`does_not_support` (matching each manifest's already-stamped value), routing `/queue-experiment` to rule out the sparse-goal-seeding confound before considering demotion, plus a flag that the SD-005 blocker citation needs re-checking against current state.

## Thread 8 -- MECH-075 novelty-loop + MECH-163 dual-system (5 runs, part of the shared seeding-gap note)

`192a`x2: consistent null, claim note already covers exactly these two runs with a biology-grounded LC-vs-VTA anatomical-targeting reframe (dorsal HPC gain is LC-mediated, not VTA-mediated -- not a falsification). `230`x2: summary.md header explicitly reads "Purpose: diagnostic" though the manifest's structured `experiment_purpose` field says "evidence" -- **treated as diagnostic-purpose regardless of the field mismatch**, per skill Key Rules. `033537Z` already carries a full note (`substrate_limitation`, novelty signal ~100x below C1 threshold, LC-VTA loop structurally disconnected); `162303Z` has bare `evidence_direction: diagnostic` with no note -- backfill from its sibling. `237a`: `non_contributory`, note already present (`goal_norm_long=0.011` below threshold) -- a distinct finding from MECH-163's already-tracked arc071 commit-latch cluster, genuinely new addition to that claim's evidence base.

## Thread 9 -- MECH-188/INV-054/Q-034 (11 runs, part of the shared seeding-gap note)

**Q-034 lineage (288 -> 451x2 -> 526): confirmed progressive**, not independent -- `451` explicitly `supersedes: V3-EXQ-288`; `526` explicitly `supersedes: V3-EXQ-451`. All three converge on identical monostrategy lock-in (`goal_reach_rate=0.0`, `action_entropy_bits=0.0` across every grid cell, both seeds). Already reclassified `non_contributory` at governance walks (2026-04-22, 2026-05-07). Root substrate gap already tracked (`substrate_queue.json` entry `MECH-269`, "proximal cause of monostrategy lock-in across V3-EXQ-433/445/451/452/454 cluster") -- `288`/`526` not yet named in its `failure_record` cluster list, recommend `amend`. **Flat/pack drift found on `451`@1776700328Z**: pack `manifest.json` still shows stale `weakens`; the flat sibling has the corrected `non_contributory` -- same pattern already documented for run 108 elsewhere in this batch, another instance not a new defect class.

**INV-054 lineage (278 -> 435x2): confirmed progressive.** Both `435` runs `supersedes: v3_exq_278`. `278` established depression state successfully (`z_goal_norm=0.0`) but graded, not discontinuous, recovery in 3/3 seeds both runs -- "ree-v3 substrate produces graded recovery by construction; has no bistable/discrete-mode primitive." Missing substrate already named and partially landed: claim note shows SD-032a+MECH-259 `v3_pending` lift confirmed (V3-EXQ-446/455 substrate PASSes) -- discrete `operating_mode` primitive now exists, blocker narrows to SD-032b specifically. `action: amend`.

**MECH-188 z_goal-injection (253x3):** `479111` and `494225` both note "Injection mechanism non-functional... Superseded by EXQ-253c" -- but **EXQ-253c never completed**: no manifest exists anywhere, not in the current queue, `git log` shows only `claim: V3-EXQ-253c -> EWIN-PC` with no result commit (EWIN-PC is a confirmed-dormant Windows runner box). **This "superseded" claim is unverified/phantom** -- flagged for governance correction rather than propagated. `556946` (third timestamp, `does_not_support`, no note) likely shares the same injection-wiring defect, recommend the same disposition pending a brief confirming read. Claim note independently confirms the substrate story: without baseline z_goal seeding (SD-012 not resolved at the time), injection could not demonstrate persistence of an absent goal -- SD-012+SD-018 are now implemented, opening a legitimate re-test path.

## Step 8: the shared substrate-gap finding (user-confirmed, recommended option)

Threads 3, 7, 8, and 9 all bottleneck on the same underlying substrate condition: insufficient/absent benefit or z_goal seeding density in the March-early-April 2026 experiment vintage (pre-dating later SD-012/SD-018/MECH-269/SD-032 landings). MECH-029 (commitment gate never releases), MECH-128/Q-002 (goal conditioning has no signal to act on), MECH-075/163 (`goal_norm_long=0.011`), MECH-188 (injection onto an absent baseline goal), Q-034 and INV-054 (monostrategy lock-in / graded-only recovery) are plausibly five faces of one era-specific seeding deficiency, several components of which the substrate has since partially addressed. **Decision (Step 8, recommended option confirmed)**: record this as **one shared substrate-queue note** (`era_specific_zgoal_benefit_seeding_density_gap_pre_sd012_sd018_mech269`) cross-referencing all four claim families, rather than four independent entries -- avoids the illusory-conflict-resolution trap of five claims each independently accumulating "weakens" for what may be one shared cause.

**MECH-113 (Thread 4) is explicitly NOT part of this shared note** -- its ablation-flag-inert defect is a distinct, claim-specific implementation-completeness gap, not a seeding-density issue.

## Biological-reference / literature triage

Every claim in this batch has a present `targeted_review_connectome_*`/`targeted_review_*` entry **except MECH-069** (only an unrelated `targeted_review_q_069` exists) -- genuine `/lit-pull` gap, commissioned via Thread 1's routing.

## Re-derive brake state (R1-R3)

Zero `substrate_ceiling` hits confirmed for every claim in this batch. None of this batch's recommended categories are `substrate_ceiling` (they land on `precondition_unmet`, `competence_implementation_gap`, `measurement_gap`, `measurement_test_design_defect`, or `superseded`). **The brake does not fire anywhere in this batch.**

## Recommended routing summary

- **Thread 1**: `/queue-experiment` + `/lit-pull` (MECH-069).
- **Thread 2**: `governance-note-only`, extend existing.
- **Thread 3**: `governance-note-only`, part of the shared seeding-gap note.
- **Thread 4**: `/implement-substrate` (`create`) -- distinct from the shared note.
- **Thread 5**: `governance-note-only`.
- **Thread 6**: no action, all covered.
- **Thread 7**: `/queue-experiment` (rule out seeding confound), part of the shared note.
- **Thread 8**: `governance-note-only`, part of the shared note; flag `experiment_purpose` field/header mismatch on 230.
- **Thread 9**: `governance-note-only`, part of the shared note; flag phantom supersession (253) and flat/pack drift (451) to governance for correction.

## Learning extracted

1. A full-corpus grep, not just the round's own named files, was necessary to find real coverage for `108` and `396a` -- confirms the same lesson the round's SD-003/MECH-112/dACC batch independently learned for the dACC lineage.
2. Five claims sharing one underlying substrate deficiency is exactly the illusory-conflict-resolution trap this skill warns against -- worth a standing check whenever multiple claims from the same experiment-vintage era all show precondition_unmet against the same missing substrate.
3. The flat-vs-pack manifest drift pattern (stale disposition in one copy, corrected in the other) recurred a second time within this same batch (108, then 451) -- likely a systemic sync gap worth a governance-side audit rather than treating each instance as independent.
4. A "superseded by X" citation is only as good as X actually having completed -- MECH-188's phantom-253c supersession shows this needs verification, not blind propagation.
