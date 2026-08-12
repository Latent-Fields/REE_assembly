# REE-v3 Developmental Readiness Investigation

**Date:** 2026-08-12T16:55Z–18:xxZ | **Session:** `ree-v3-developmental-readiness-47e33b` | **Status:** synthesis, no code/experiment changes made

**Relationship to concurrent work** (checked before writing anything, per instruction): this investigation is built *on top of*, not in competition with, three live/recent threads —
- `pensive-franklin-1e285b` (live, currently paused): `/failure-autopsy` of V3-EXQ-925 itself. Its committed output (`failure_autopsy_V3-EXQ-925_2026-08-12.md`) is the primary source for §1 below; that autopsy's own H1–H4 verdict (MIXED, all four left alive, new H0 registered) is treated as authoritative and not re-litigated here.
- `closure-map-work-sets-c70f21` (live): designed **and, mid-way through this investigation, landed** (`ree-v3@a91b3f4`, `REE_assembly@3618e791fe`, both 2026-08-12T17:40Z) the canonical-profile Option B+C mechanism. §6/§18/§22 build directly on this.
- `mech357-pressure-scoping-11e9c9`: stale claim, no F-dominance content found under that session id on disk (the only file matching that session id is an unrelated MECH-357 predator-pursuit doc). Treated as superseded by `pensive-franklin-1e285b`'s actual autopsy; not duplicated.

No million-tick experiment is proposed or queued. Per governing instruction: **do not explain failure by calling REE a baby; do not explain failure by calling REE broken; determine whether it possesses the machinery by which a baby could become something more mature.**

---

## 1. V3-EXQ-925 — what it actually shows

Design: 3 seeds (42/43/44), 60-episode SD-056 warm-up (P0) + 40-episode capture (P1), 200 steps/episode, 5 counterfactual arms (C0 self-consistency, C1 literal-F lesion, C2 F-association scramble, C3 attenuation ladder, C4 MECH-448 eligibility toggle, C5 competitor lesion). `elapsed_seconds=8030.75` — a real (non-smoke) run.

- **2/3 seeds ready** (floor: candidate-world pairwise distance ≥0.02 *and* `gated_policy` std ≥1e-6). Seed 43 failed **only** the second floor (7.45e-09, ~3 orders of magnitude short) despite SD-056 training adequately for that seed — a per-seed competitor-channel training-reliability gap, not a design defect.
- Candidate-world differentiation on ready seeds: **0.1239–0.1568** — "real, vs ~0.0000 untrained... but modest."
- E3 score range **0.328** vs temperature **≈1.0** → the softmax is "essentially flat, so no channel — literal F included — is meaningfully steering the choice" (the driver's own words).
- Normalised selection entropy **0.998** (1.0=uniform). **`committed_fraction = 0.000` across all 2493 events, both ready seeds** — the hard-argmin commitment path essentially never engages at this corpus-default configuration.
- F's *absolute* causal contribution (C1 lesion): total-variation shift **0.00052**, direction-conditioned delta **≈-0.0000016** (no consistent direction). F's *variance share* (V3-EXQ-924, same-day remeasurement after the E3-scorer bug fix): **96.0–96.1%**, *higher* than the historical pre-fix 88–89% figure — ruling out the scorer bug as the explanation for F-dominance.
- Competitor influence: 8.6% (factual) / 9.6% (lesioned) — just above the pre-registered 0.05 "H3" threshold on both sides: a genuine near-miss, not a clean confirmation.
- Eligibility-toggle (MECH-448/C4) never changes the winner (0.0%) → no evidence eligibility is an independent locus of authority.
- Independent ecological criterion (env-native nearest-hazard-distance, network-independent) validated the replay harness itself (reconstruction error 7.87e-09; non-degeneracy check passed).

**Autopsy verdict:** H1 (pathological F dominance) not confirmed; H2 (primary-field/eligibility dominance) not confirmed; H3 (upstream/global weak authority) *near-miss*, "biologically qualitatively favoured" but not confirmed by the pre-registered threshold; H4 (conditional specialisation) not confirmed. **New H0, discovery leg (not pre-registered): "selector regime" — at default config nothing steers selection, which is a different phenomenon from "F suppresses competitors."** Net GOV-FAILLOC-1 classification: **MIXED** — mechanism `partial`, measures `established`, environment `established`. Explicit: *"not evidence that REE's selector is broken, nor a clean confirmation of any single H1–H4 hypothesis."* User-confirmed disposition: leave H1–H4 alive, register H0. Routing: re-run with committed selection actually engaged (`use_gap_scaled_commit_temperature=True`), not yet built.

**This investigation's independent read, cross-checked against source (§7 below): the H0 finding is not an artifact of the diagnostic harness.** Two independent lines converge on the same mechanism: (a) the causal-replay data itself (`committed_fraction=0.000`, score-range/temperature≈0.33), and (b) direct source inspection showing `use_gap_scaled_commit_temperature=False` is the corpus-wide default (1345/1348 experiments) *and* that raw F-scores can reach ~1e32 in trained regimes (V3-EXQ-643) against a ~0.05–0.1 modulatory-bias magnitude — literally below float32 ULP. That second fact is a **numeric-precision ceiling**, not a weak-evidence-stream phenomenon: no amount of additional experience makes a 0.1-magnitude signal move an argmin against a 1e32-magnitude one. This is evidence *for* H4-flavoured lesion at the numeric-implementation layer, sitting underneath the more diagnostic-level H1–H4 discrimination the 925 autopsy itself is scoped to. See §18 for how this resolves the "immature vs lesioned" question for this specific channel.

---

## 2. The developmental causal loop, as REE-v3 actually implements it

Per source audit (`ree_core/`), the loop is **not** uniformly a single mechanism — different arrows are implemented by different, independently-flagged subsystems:

| Arrow | Mechanism | Ordinary-config status |
|---|---|---|
| world → perception | env observation pipeline | default-on (baseline substrate) |
| perception → action-conditional prediction (E2) | SD-056 (`e2_action_contrastive_enabled`) | **default OFF** — ordinary orgs run the pre-SD-056 collapse-to-identical-z_world regime |
| prediction → candidate valuation | E3 selector, residue cost term | residue term default-ON (`rho_residue=0.5`, non-None construction) |
| valuation → committed action | E3 commit gate | hard argmin, but softmax-flat at default temperature/score-range ratio; `use_modulatory_selection_authority` (fix for the numeric-ceiling problem) default OFF |
| committed action → memory/consequence | residue field | default-ON, reader+writer both wired, `reset()` explicitly does not clear it |
| memory → future candidate generation | hippocampal module → E3 residue cost | wired (`E3TrajectorySelector` constructed with non-None `residue_field`) |
| deficit → exploration (curiosity) | MECH-482/483/395 | **not implemented in V3 at all** ("DO NOT build in V3" in claims.yaml); MECH-489 (defensive orienting) implemented but default-OFF and its own most recent test (V3-EXQ-910) falsified the trigger-alignment sub-claim |
| threat → safety learning | MECH-303 contextual safety terrain | gated OFF by default (`use_contextual_safety_terrain=False`); even when enabled, the production-default threshold (0.05) is unreachable against a measured z_harm_a baseline of ~0.54–0.55 in both safe and unsafe contexts (V3-EXQ-764, V3-EXQ-917) |
| sleep → consolidation | `SleepLoopManager` | only fires at inter-**segment** boundaries (`notify_episode_end`, called once per `reset()`); **a true single-continuous-life driver has zero such boundaries by construction** (GAP-9) |

**The single most consequential finding for the whole investigation**, from the developmental-synthesis doc (`competence_via_lifelong_practice_and_sleep_synthesis_2026-08-10.md`): the 906-lineage observational "life" drivers — the standard vehicle for long-life Fishtank runs, including V3-EXQ-920 — execute `_observational_run()` under **`torch.no_grad()`**. **No weight update of any kind occurs during any of these observed "lives."** Whatever "experience" means in this loop, it is *not* gradient-based learning. Any within-life change must come from non-parametric arithmetic state: residue accumulation, EMAs, buffers (candidate: MECH-357's `avoidance_efficacy`, "REE's actual built candidate mechanism for the hypothesis that practice builds competence without weight updates" — but this has never had a fair test across 4 attempts, each blocked by a different environment-design confound).

This reframes the entire "give it more experience" question: **more ticks of a frozen policy cannot, by construction, produce the kind of maturation that a longer *training* run would.** Whether it can produce maturation via the non-parametric channel (residue, MECH-357) is a live, unresolved, and currently under-tested question — not a settled "no."

---

## 3. Developmental-readiness matrix (Levels 0–7)

Level definitions per task spec: 0 source exists, 1 reachable, 2 non-degenerate, 3 ecologically coupled, 4 plastic (experience alters it), 5 downstream-effective, 6 behaviourally effective (ablation changes behaviour), 7 developmentally necessary/contributory (longitudinal difference present vs absent).

| Mechanism | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| SD-056 action-conditional E2 | Y | N (default OFF) | N/A | N/A | N/A | N/A | N/A | N/A | ordinary orgs never reach this path at all |
| E3 candidate scoring (F channel) | Y | Y | Y | UNKNOWN | UNKNOWN | Y (dominates variance) | UNKNOWN | UNKNOWN | 96% variance share confirmed; behavioural/downstream ablation not run on ordinary (non-diagnostic) configs |
| E3 commitment (argmin) | Y | **N** at default config (`committed_fraction=0.000`) | — | — | — | — | — | — | V3-EXQ-925 |
| Modulatory selection authority | Y | **N** (numeric ceiling: bias ULP-below score range) | — | — | — | — | — | — | source (`e3_selector.py:2561-2568`) |
| Goal/wanting (`z_goal`, `residue_wanting`) | Y | Y (916a fix) | Y (0.078 / 0.568 std, non-degenerate in 916a) | UNKNOWN | UNKNOWN (only tested at one instant) | UNKNOWN (untested) | UNKNOWN (untested) | UNKNOWN | 916/916a autopsy: fix is instrumentation-only, no precedence/causal-influence test performed |
| Residue field (INV-001) | Y | Y (default-on, unconditional per-candidate cost) | Y (non-zero weight, real accumulation path) | UNKNOWN | Y-by-construction (arithmetic accumulation across life) | Y (feeds E3 cost every candidate) | UNKNOWN | UNKNOWN | source audit — the one channel with a genuinely closed ordinary-config loop through Level 5 |
| Hippocampal/memory | Y | Y (constructed, coupled to E3) | UNKNOWN | UNKNOWN | UNKNOWN | Y (feeds residue cost) | UNKNOWN | UNKNOWN | reader/writer coupling confirmed in code; no behavioural validation found |
| MECH-303 harm/safety | Y | **N** (default OFF; even enabled, threshold unreachable) | — | — | — | — | — | — | V3-EXQ-764/917, source |
| MECH-489 defensive orienting | Y | N by default (flag OFF) | Y when forced on | UNKNOWN | UNKNOWN | UNKNOWN | **N** — trigger-alignment falsified (V3-EXQ-910) | N | claims.yaml + source |
| MECH-482/483/395 curiosity | **N** (not implemented in V3) | — | — | — | — | — | — | — | claims.yaml: "DO NOT build in V3" |
| Sleep/consolidation (single continuous life) | Y | **N** (zero boundaries by construction in a true single-life driver) | N/A | N/A | N/A | N/A | N/A | N/A | GAP-9, `sleep_substrate_plan.md` |
| Sleep/consolidation (segmented drivers) | Y | Y (fires at segment boundaries) | **N** (`replay_diversity_index`=0.02, zero variance across 45 firings — likely structural bug) | UNKNOWN | UNTESTABLE with current data (no impoverished-experience contrast case exists) | N (V3-EXQ-909 found no clean behavioural signal; environment re-randomizes layout at the same boundary) | N (ablation underpowered, p=0.25, confounded) | UNKNOWN | sleep_transition_investigation, V3-EXQ-909/913 |
| Gradient-based weight learning during a "life" | Y (exists in the training pipeline generally) | **N within the observational-life driver family** (`torch.no_grad()`) | N/A | N/A | N/A | N/A | N/A | N/A | competence_via_lifelong_practice_and_sleep_synthesis doc |

---

## 4/5/6. Lesions: fixed / still active / configuration-dependent

**Fixed (this cluster, 2026-08-08–12):**
- Orphaned goal/wanting writer (`update_benefit_salience`/`update_schema_wanting` never called) — fixed in 916a. **Not retroactively applied** to predecessor runs (664/906/909/911/912/913/916) — their z_goal evidence remains suspect.
- `benefit_exposure` wrong-dict read + `use_proxy_fields` default-False gating it off — fixed in 916a only.
- E3-scorer untrained-noise bug (pre-`193bbec`) — fixed 2026-08-09; **increased** measured F-dominance, ruling this out as F-dominance's explanation.

**Still active:**
- E3 numeric-precision ceiling (`use_modulatory_selection_authority=False` default; raw scores can exceed modulatory bias by >30 orders of magnitude) — gated on F-dominance resolution before admission.
- MECH-303 harm/safety threshold unreachable at production sourcing (`damage_sourced`, AUC≤0.52) vs legacy `proximity_ema_sourced` (AUC 0.84–0.97) — routed to `/implement-substrate` as `SD-MECH303-THRESHOLD-SOURCING`, not yet built.
- Sleep-entry unreachable in true single-continuous-life drivers (GAP-9) — registered 2026-08-12, no code fix.
- Sleep replay degeneracy when sleep does fire (`replay_diversity_index=0.02` flat) — diagnosed as likely structural, not yet fixed.
- Queue `"seeds": N` never reaching driver CLI `--seeds` — chronic underpowering of multi-seed long-life runs (hit independently by V3-EXQ-912 and V3-EXQ-920); user declined a corpus-wide audit.
- MECH-357 (`avoidance_efficacy`, practice-without-weight-updates) — 4 attempts, 4 different confounds, "never had a fair test."

**Configuration-dependent (default-off but individually validated, listed by the architecture-epoch investigation's drift audit as high-confidence de-facto-canonical candidates):** `use_harm_stream`/`use_affective_harm_stream`, `use_resource_proximity_head`, `use_per_stream_vs`, `use_lateral_pfc_analog`, `use_dacc`, `use_salience_coordinator`, `use_structured_curiosity`, `sws_enabled`/`use_sleep_loop`, `use_event_classifier` — 341 default-off dataclass fields total, 132 candidate-tagged, 11 flagged worst-tier (zero enablement, no cited evidence).

---

## 7. Does SD-056 (the mechanism V3-EXQ-925 specially prepared) represent ordinary development?

**No.** `e2_action_contrastive_enabled` defaults False (confirmed at three separate source sites); the `curiosity_candidate_source` consumer defaults to `"proposer"`, not the SD-056-trained signature. Ordinary Fishtank organisms therefore run in the pre-SD-056 regime — the exact "candidate actions collapse to near-identical predicted z_world" failure mode the mechanism exists to fix. V3-EXQ-925's 60-episode SD-056 warm-up is a deliberate, non-default preparation; its 0.124–0.157 candidate-world differentiation is the *best case*, not the typical case. This confirms the task brief's stated suspicion directly.

## 8. Is E3's weak action authority developmental?

**Partially, and the parts split cleanly.** The *H3-near-miss* (competitor influence 8.6–9.6%, just above 5%) is genuinely ambiguous between "weak but real and growing with maturity" and "weak and structurally incapable of growing." But the **numeric-precision ceiling** (`use_modulatory_selection_authority`) is not ambiguous: a ~0.1-magnitude signal cannot move an argmin against a ~1e32-magnitude signal regardless of how much more experience refines either one — more training data does not change floating-point ULP arithmetic. **This one sub-mechanism is architecturally incapable as currently implemented, independent of organism age** — it needs a fix (already designed, gated on F-dominance governance review), not more life.

## 9. Is commitment expected to mature with experience under current architecture?

At `committed_fraction=0.000` and `use_gap_scaled_commit_temperature=False` default, commitment as currently gated is a **binary regime switch**, not a graded quantity that experience could shift along a continuum. More experience under the current default configuration would not be expected to move `committed_fraction` off zero — that requires either the temperature-softening flag or a score-range change, both configuration decisions, not developmental ones.

## 10. Can goal/wanting currently influence development and behaviour?

Existence and non-degeneracy: **yes**, post-916a (`chan_max_std_z_goal=0.078`, `residue_wanting=0.568`). Precedence and downstream causal influence: **untested** — the 916a fix's own PASS gates explicitly did not touch causal-influence questions. And in the one long-life run available (V3-EXQ-920), `residue_wanting` is flat at 0.0 for the *entire* 1475-step life — that driver is mechanistically disconnected from the 916a-repaired pathway entirely, so the repair's benefit has not yet reached the exact experimental context (long single-life Fishtank) this investigation cares most about.

## 11. Does memory demonstrably change later behaviour?

**Reader/writer coupling is real and default-on** (hippocampal → residue cost → every scored E3 candidate), which is the strongest "loop closes in ordinary config" finding in this whole investigation. But **behavioural change from that coupling has not been demonstrated** — no source or experiment evidence found showing memory content varying meaningfully with experience (Level 3+) or an ablation changing behaviour (Level 6). Existence + wiring ≠ demonstrated use.

## 12. Can curiosity/information-hunger generate useful developmental experience?

**Currently, no operative mechanism exists for this in V3.** MECH-482 (target-bound epistemic-deficit accumulator), MECH-483 (diffuse orient/survey), and MECH-395 (pre-approach orienting) are all explicitly unimplemented and marked "DO NOT build in V3" (V4-scoped). MECH-489 (defensive orienting) is implemented but off by default, and its own most recent test falsified the trigger-alignment sub-claim. Separately, `developmental_ecology_curiosity_foraging_correction` found the *environment itself* conflates the exploratory cue with ground-truth resource location, so even a working curiosity mechanism would currently have no genuinely uncertain-but-informative signal to exploit (91–97% of departures have no resource in sensory range; only 42–46% ever perceive one; the departure-mode classifier essentially never reads "explore"). This is a **double gap** — mechanism absent, and the environmental structure a mechanism would need is also not yet present.

## 13. Does lack of endogenous continuous-life sleep currently limit developmental interpretation?

**Yes, structurally, for exactly the experimental design this investigation is scoping.** A true single-continuous-life driver (`num_episodes=1`, e.g. V3-EXQ-920, and the natural shape of a long-age developmental study) has **zero** sleep-firing opportunities by construction (GAP-9) — not "sleep is rare," but "sleep cannot occur at all." Any proposed long-life developmental-age experiment run as a true single life will confound "long life" with "zero consolidation, ever," unless GAP-9 is addressed or the absence of sleep is explicitly documented as a controlled variable. Separately, even where sleep *does* fire (segmented drivers), its replay content is measured degenerate (flat diversity index), so "sleep is reachable" would not by itself mean "sleep is doing useful consolidation work" — a second, independent limitation.

## 14/15. Persistence map: what does "age" actually mean computationally today?

| Boundary | Residue | Hippocampal (per-stream V, event segmenter, anchor set, staleness, ghost-goal bank) | Sleep-eligible state |
|---|---|---|---|
| Tick | persists (accumulates) | persists | n/a |
| Episode/segment | **explicitly does not reset** (`reset()` docstring: "Does NOT reset residue") | individually flag-gated per-mechanism resets | sleep fires here (`notify_episode_end`, inside `reset()`, before per-episode clears — sees final waking state) |
| Body respawn | UNKNOWN from source (only env-level resource/waypoint respawn found; no distinct agent-body respawn boundary located) | UNKNOWN | UNKNOWN |
| Sleep boundary | persists through (sleep reads final waking state) | depends on per-mechanism flags | — |
| Process/experiment restart | UNKNOWN (no `save_checkpoint`/`load_checkpoint` on `REEAgent` found; likely external, script-level, not audited) | UNKNOWN | UNKNOWN |

**Practical consequence:** "cumulative lived ticks" is currently the only cleanly-defined age axis. "Cumulative learning updates" is presently **zero** for the observational-life driver family (no-grad). "Sleep cycles" is presently **zero** for true single-life drivers (GAP-9). A million-tick single-life run would still report age=1,000,000 ticks while age-by-learning-update and age-by-sleep-cycle both stay at zero — these are not currently interchangeable, and a future developmental-age experiment must pick (and report) which axis it means.

## 16. Do existing long-life logs already show developmental trajectories?

The one available continuous single-life trajectory, **V3-EXQ-920** (seed 0, 1475 of a 20,000-step budget — genuine uncensored `health_depleted` death, only 1/8 pre-registered seeds actually ran due to the same seeds→CLI wiring bug found in V3-EXQ-912):

- `z_goal`: exponential decay **0.355 → ~0** by ~step 300 (20% of the observed life), then flat near-zero for the remaining 80%.
- `drive`: rises monotonically to **ceiling (1.0)** and stays there for the final ~40% of the run.
- `energy`: monotonic decline to **exactly 0.0** by ~step 885 (60% mark) and stays at 0 for the final 40%.
- `is_committed`, `freeze`, `orienting_active`, `orienting_trigger_fired`: **flat at 0.0 across the entire life** — never fire once, from step 1 to step 1475.
- `residue_wanting`: **flat 0.0 the entire life** (this driver does not use the 916a-repaired pathway).
- `surprise`/`dread` do rise late — but concurrently with the zero-energy crisis, more plausibly a deterioration signature than developmental organization.
- Mode distribution narrows toward "neutral" near death — consistent with energy-forced default behaviour, not increasing behavioural sophistication.

**Read plainly: this is early plateau/saturation at degenerate values (60–80% of the life), not a still-organizing trajectory at termination.** But this is a single, severely underpowered data point (1 of 8 planned seeds, itself a symptom of an unrelated wiring bug), so it cannot license a general claim either way — it is evidence against "youth alone explains everything" for *this* run, not proof that longer/better-powered runs would show the same pattern.

## 17. Environmental adequacy

Real, but narrowly and precisely characterized as a **missing learnable intermediate structure**, not a blanket "environment is too poor" finding: the current ambient benefit field conflates the exploratory cue with the actual resource location (same variable, not two correlated-but-distinct ones), so there is currently no genuinely-uncertain-but-informative signal for a curiosity mechanism to exploit even once one exists. Quantified: 91–97% of departures have no resource within sensory range (this is *intended* — it's what makes exploration necessary rather than optional), but only 42–46% of excursions ever perceive a resource at all, and the departure-mode classifier reads "explore" on almost none of them (1/64, 3/67) — the environment doesn't yet expose enough intermediate, partially-informative cues to make exploration legible or learnable as distinct from wandering.

## 18. Overall characterization

**A mixture, and the mixture has structure — it does not resolve to one label.**

- **Architecturally incapable, locally and specifically:** the E3 numeric-precision ceiling (`use_modulatory_selection_authority` off, ULP mismatch) is a hard architectural fact, not something more experience touches. MECH-482/483/395 curiosity is simply not built in V3.
- **Developmentally lesioned, and partially repaired:** the goal/wanting orphaned writer (fixed, not retroactive), MECH-303's threshold sourcing (diagnosed, not yet fixed), sleep-entry in single-continuous-life (registered, not yet fixed), the queue seeds-wiring bug (known, declined for corpus audit).
- **Genuinely, and specifically, immature-but-intact:** the residue/hippocampal loop is wired, default-on, and reader-writer coupled through Level 5 in ordinary configuration — this is the one channel where "more experience" has an intact loop to run through, *if* the non-parametric (no-grad-compatible) mechanism it depends on (MECH-357-style practice) turns out to work, which remains untested.
- **A framing artifact, not evidence either way:** the observational-life driver family runs entirely under `torch.no_grad()`. Scaling tick-count on this driver family cannot produce gradient-learning-based maturation *by construction*, independent of whether the organism is "young" — this is a design fact about what kind of experiment is being run, not a finding about REE's capacity.

## 19. Minimum repairs/confirmations needed before a serious long-development experiment

1. **Decide what "life" is supposed to demonstrate** — gradient learning (requires a different driver architecture than the current no-grad observational family) vs. non-parametric practice-based competence (requires MECH-357's "fair test," never yet achieved across 4 attempts) vs. both. This single decision reframes everything downstream and does not yet have an owner.
2. Fix or explicitly control for GAP-9 (sleep unreachable in true single-continuous-life) before any long single-life run is treated as informative about consolidation.
3. Resolve, or explicitly bracket as out-of-scope, the E3 numeric-precision ceiling — otherwise a long-life run's selection behaviour is capped by a float-precision artifact no amount of experience will move.
4. Fix the queue `seeds→CLI` wiring bug, or hand-verify multi-seed args, before trusting any multi-seed long-life design (it has already silently underpowered two experiments).
5. Correct the environment's cue/resource-location conflation if curiosity-driven learning is a target readout — otherwise there is no learnable intermediate signal for any exploration mechanism (built or future) to use.
6. Retroactive-evidence caution: any pre-916a run's `z_goal`/`residue_wanting` data should not be used as a developmental baseline (known-broken instrumentation, not retroactively corrected).

None of these is "REE must be perfect" — several existing, unrelated gaps (MECH-489's falsified trigger claim, most default-off configuration knobs) are orthogonal and do not need to block a well-scoped study.

## 20. Proposed developmental-age experiment

**Not proposed yet — not justified by current evidence.** Per the task's own governing constraint, a long-age experiment is justified only once the mechanisms necessary for the phenomenon under study are sufficiently functional that age becomes an interpretable independent variable. Item 1 in §19 (what kind of "life," decided) is a hard precondition: without it, a logarithmically-scaled age sweep (1k→1M ticks) on the current no-grad observational driver would produce a curve in tick-count against a substrate that is not learning in the ordinary sense over that axis at all — the experiment would measure something, but not clearly "development." Once §19's items are resolved or explicitly bracketed, the natural design (matched-lineage snapshots, logarithmic ages grounded in observed timescales rather than the illustrative 1k/3k/10k/... ladder in the task brief, developmental-lesion controls per item 13 of the brief) can be designed as a follow-on — but that is future work, not this document's output.

## 21. Chips spawned

One new chip (see below) for the single genuinely novel, unaddressed synthesis gap this investigation surfaced: the "what does a developmental life demonstrate" architecture decision (§19 item 1), explicitly linking GAP-9 and MECH-357's untested status, neither of which currently names the other. Everything else substantive (E3 numeric ceiling, MECH-303 threshold, GAP-9 itself, queue-seeds bug, canonical-profile admission criteria) is already tracked by an existing chip, `/implement-substrate` entry, or governance gate — re-chipping would create a duplicate, staler tracker per this repo's own chip-discipline rule.

## 22. Feed into the canonical-organism/epoch decision

The `architecture_epoch_investigation.md` conclusion (§6: "there isn't one, by construction" — REE-v3 does not currently denote a unique canonical organism) is corroborated end-to-end by this investigation's own findings: SD-056, sleep, MECH-303, and the E3 modulatory-authority fix are all mechanisms that are individually validated but default-off or gated, exactly the "historically constrained subset assembled by experiment-specific flags" pattern the epoch investigation names in the abstract. This document adds one concrete new input to that decision: **the developmental-history-as-epoch-identity gap (already scoped, chip `chip-20260812-developmental-history-epoch-scoping`, unsolved) must also decide whether "raised without gradient learning" counts as a distinct epoch/profile axis from "raised with a given mechanism enabled/disabled"** — these are currently conflated in a single flat config-diff view, and they are not the same kind of fact about an organism's history.

---

## Answer to the governing question

*If we gave the current REE-v3 organism ten or one hundred times more meaningful lived experience, do we have good reason to expect its internal differentiation and behavioural organisation to mature — or would we mostly be giving more experience to machinery that cannot yet use it?*

**Mixed, and resolvable — not a shrug.** For the specific driver family used in the one long-life run we have data on (the no-grad observational Fishtank lineage), the honest answer is **the second option, and by design, not by immaturity**: that driver does not update weights during the observed "life" at all, so more ticks of it cannot produce gradient-learning-based maturation regardless of organism age. For the one channel that *is* wired for non-parametric within-life change in ordinary configuration (residue → E3 candidate cost), the loop is real and closes through Level 5, but whether it does anything behaviourally useful with more experience is untested, not refuted — this is the most promising specific target for "more experience might help." For E3's numeric-precision ceiling and the unimplemented curiosity mechanisms, more experience is confirmed **not** to help — these are architecture facts, not maturation facts, and need building/fixing rather than raising.

**The smallest set of investigations that would resolve the remainder:** (1) decide and instrument what "a developmental life" is meant to demonstrate (§19.1); (2) get MECH-357's avoidance-efficacy mechanism its first genuinely deconfounded test; (3) fix or bracket GAP-9 before treating any single-life run as informative about consolidation; (4) run a residue-specific ablation (with vs. without the residue cost term, same experience) to get the first behavioural-effectiveness (Level 6) data point for the one channel that already has a closed ordinary-config loop.
