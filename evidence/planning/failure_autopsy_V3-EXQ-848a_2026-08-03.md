# Failure Autopsy: V3-EXQ-848a (ARC-005, precision-only decoupled ladder, calibrated retest)

**Generated:** 2026-08-03T09:01:56Z
**Scope:** single
**Status:** confirmed (user-confirmed routing 2026-08-03)

## 1. Dry-run gate

`check_dry_run_citations.py v3_exq_848a_arc005_precision_only_decoupled_ladder_calibrated_20260802T120712Z_v3 V3-EXQ-848a` -> `0 dry cited, 1 clean`. Not a smoke; a real 30-cell (6 arms x 5 seeds) run, `elapsed_seconds=11225.29` (~3.1h).

## 2. Facts

**Manifest** (`REE_assembly/evidence/experiments/v3_exq_848a_arc005_precision_only_decoupled_ladder_calibrated_20260802T120712Z_v3.json`, also mirrored to the `runs/` pack):

- `queue_id`: V3-EXQ-848a · `claim_ids`: `[ARC-005]` · `outcome`: FAIL · `overall_pass`: False
- `evidence_direction`: mixed (self-routed, matches the driver's own pre-registered decision rule) · `non_degenerate`: True
- `criteria`: `C_precision_monotonicity` (load-bearing) — **passed: false**
- `analysis.n_satisfied` = **1 of 10** units (need >=7). Per-unit `rho_log10_precision`:
  - Content A: seed0=0.5, seed1=0.5, seed2=**1.0** (satisfied), seed3=0.5, seed4=-0.5
  - Content B: seed0=0.5, seed1=-0.5, seed2=0.5, seed3=0.5, seed4=0.0
  - Sign count: **7 positive** (6 at exactly 0.5, 1 at 1.0), 1 zero, 2 negative (both -0.5).
- `interpretation.label`: `precision_channel_authority_weak_calibrated`. All readiness preconditions (`precision_cross_seed_sd`, `n_salience_ticks>=150`, `channel_state_delta_vs_L0`) met on all 6 arms — `per_arm_gate.all_green: true`, no vacuous arms.
- `diagnostics.total_dacc_bias_calls`: **25,289** (nonzero — the calibrated pathway is confirmed genuinely engaged, unlike its predecessor).
- Recording provenance: `validate_recording.py --paths <manifest>` -> OK, 0 always-core gaps. `substrate_hash` present (`78c5ae3b...`), full `config`/`seeds` present. No recording gap.

**Script** (`ree-v3/experiments/v3_exq_848a_arc005_precision_only_decoupled_ladder_calibrated.py`): successor to V3-EXQ-848, identical design (channels 1 [5-HT + dACC goal-readout] + 2 [phasic-burst temperature] laddered L0/L1/L2, channels 3/4 fixed at L0, 2 content sets x 5 seeds = 10 units), differing ONLY in setting `dacc_goal_readout_weight=0.5` + `dacc_goal_readout_normalize=True` (848 silently defaulted both to inert values). A build-time guard asserts these flags actually threaded into the constructed `REEConfig` before any cell runs — guards against a repeat of 848's exact failure mode. Pre-registered criterion (unchanged from 848, script docstring): `|Spearman rho| >= 0.60` in `>=7/10` units -> supports; all-10-units-near-zero `[-0.1,0.1]` -> non_contributory (informative negative); otherwise ("some real but sub-threshold trend") -> **mixed**. This run landed exactly the pre-registered "otherwise" branch.

**Queue entry**: `supersedes_note` states plainly that 848's own manifest evidence is *not* invalidated by this fix (it reflects channel 1's pre-existing serotonin pathway + channel 2, unaffected by the calibration), and that this run is "the FIRST run in which the dACC goal-readout channel is genuinely LIVE and CALIBRATED."

**Expected vs observed**: expected either a clean pass (if the calibration fix let a real effect through cleanly) or a clean near-zero null (if the channel genuinely carries no authority). Observed neither: a **weak, majority-positive, sub-threshold trend** — the failed criterion is **discrimination** (an absolute/negative-control precondition all pass; the discrimination criterion itself is what fails).

## 3. Claim-layer mapping (ARC-005)

`claim_type`: architectural_commitment · `status`: active · `epistemic_category`: standard · `depends_on`: INV-008, INV-009, INV-014, ARC-004. Prior evidence: V3-EXQ-846 (occupancy, supports), V3-EXQ-802 (precision, standard/mixed-confounded), V3-EXQ-848 (precision, standard/mixed, silent-zero confound). ARC-005 is disjunctive at the architectural-commitment level (>=1 channel demonstrating causal authority already satisfies it via V3-EXQ-846's MODEPRIOR channel) — this run tests the narrower, already-`in-progress` GAP-A-precision-diagnostic sub-question, not the parent claim's live status.

**Did the experiment test the claim under conditions where it could express itself?** Yes, more fairly than any predecessor: 802 confounded 4 channels jointly; 848 never engaged the dACC-goal-readout pathway at all (silent zero weight); 848a is the first run where the pathway is both engaged (25,289 calls) and unit-calibrated (per-candidate-set normalized, not diluted by `||z_world||^2`). The build-time guard rules out a repeat of the exact 848 failure mode. So a further FAIL here is not attributable to the previously-diagnosed wiring/calibration bugs — those are closed.

## 4. Biological-reference triage

Channel 2 (phasic-burst gain, softmax temperature) already has an established biological anchor in `control_plane.md` (Aston-Jones & Cohen 2005 LC-NE adaptive-gain / phasic mode, reused via SD-069/MECH-104) and is *architecturally* argmax-invariant under this experiment's ~97%-committed deterministic selection regime — its expected null is a translation-correct prediction, not a gap. Channel 1 (5-HT rigidity, grounded in `control_plane.md`'s serotonin-as-stability/patience framing) now also carries the calibrated dACC goal-readout sub-pathway, whose closest mammalian correlate is dACC's role in **value-of-control / effort allocation scaling with goal proximity** (Shenhav, Botvinick & Cohen 2013 Expected Value of Control). No `targeted_review_ARC-005` or dACC-goal-proximity-specific literature entry currently exists in `evidence/literature/` — a secondary, lower-priority `/lit-pull` candidate, not required to resolve this autopsy (the failure here is not a biology-vs-formal-import divergence; the pathway's qualitative behavior, 7/10 units positive-signed, is consistent with the EVC-style graded-proximity story — the problem is the *instrument*, not the mechanism).

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | ARC-005 disjunctive commitment already satisfied elsewhere (V3-EXQ-846); this sub-question (which channel, how strongly) is narrower and unresolved, not weakened |
| Biological reference | clear (ch. 2, pre-existing) / partial (ch. 1 dACC sub-pathway, no dedicated lit entry yet) | qualitative direction (majority-positive rho) consistent with an EVC-style graded response |
| Developmental / dependency prerequisites | present | INV-008/009/014, ARC-004 all IMPLEMENTED per ree-v3/CLAUDE.md; no missing prerequisite implicated |
| Implementation completeness | complete | calibration fix (dacc_goal_readout_weight=0.5, normalize=True) confirmed engaged (25,289 bias calls) and build-time-guarded; no further wiring gap found |
| Environment adequacy | adequate | CausalGridWorldV2, same content/arena as 802/848/846, not implicated |
| **Measurement adequacy** | **under-instrumented — the load-bearing finding** | Spearman rho over a **3-point** ladder (L0/L1/L2) can only take values in {-1, -0.5, 0, 0.5, 1}. A threshold of `|rho|>=0.6` is therefore reachable ONLY by a perfect ordering (rho=1.0, |rho|=1) — the design cannot express "weak but real" vs "moderate" vs "strong" monotonic signal; both would show up identically at rho=0.5 or scatter into a sign flip under ordinary per-seed noise. 6 of 10 units land exactly at the design's second-highest achievable value (0.5), one below threshold by construction, not by a measured shortfall. |
| Integration adequacy | isolated, tested in isolation as designed (scope excludes ch. 3/4) | not implicated |
| Scale / capacity | not implicated | — |

**Sign-count read (not a formal test, but informative):** 7 of 10 units positive-signed (majority), 1 zero, 2 negative — consistent with a real, weak, majority-positive tendency muddied by 3-point resolution, not a clean null (which would show near-symmetric sign scatter around 0, as 802's bit-identical-null channels did).

## 6. Learning extracted

1. **The calibration fix (IGW-20260801-199) works as designed and is now empirically confirmed engaged** — `total_dacc_bias_calls=25,289`, build-time guard held. This closes the wiring/calibration line of inquiry 848's autopsy opened; no further substrate work is indicated on this specific gap.
2. **848's own autopsy already predicted this exact outcome and its cause**, in its `learning_extracted`: *"A per-unit Spearman rho over only 3 ladder levels is a coarse, high-variance statistic — future redesigns wanting a cleaner discrimination between 'weak real effect' and 'noise' should consider more ladder levels (5+) rather than more seeds at 3 levels."* 848a was deliberately scoped ("this successor's purpose is to correct the CONFIGURATION, not the criterion") to fix only the calibration bug, not the measurement design — so this is the second, and now maximally clean, confirmation of a prediction already on record, not a new discovery.
3. **Recording-debt vs measurement-debt**: this is squarely measurement-debt, not recording-debt. Every quantity needed (per-unit rho, seed-level precision trajectories, engagement counters) was captured; the problem is that a 3-point ladder cannot express the needed resolution, no matter what is recorded from it.

## 7. Repair pathway

**Work-graph classification:** `complex (probe-gated) / mystery (known data)` at the level of "is there a real effect" (we already have the data; the 3-point frame cannot resolve it — more seeds at 3 levels would not help, per learning #2) resolving to a `complicated (buildable)` fix at the instrument level: a named, well-understood redesign (more ladder levels and/or a different statistic), not an open question.

**Routing: `/queue-experiment`**, same-question redesign (recommend letter `V3-EXQ-848b`, not a new number — the scientific question, substrate, and content/arena are unchanged; only the ladder granularity and/or statistic change). Recommended design: extend `CHANNEL_LEVELS` from `[0.0, 0.5, 1.0]` to 5 (or more) levels per channel (e.g. `[0.0, 0.25, 0.5, 0.75, 1.0]`), recompute `c_rho_abs_floor` for the finer resolution (a 5-point ladder's achievable Spearman values are much denser, so 0.6 becomes a meaningful — not structurally-unreachable-short-of-perfect — bar), and/or supplement/replace the per-unit rank correlation with a statistic that uses the *raw* log10-precision magnitudes directly (e.g. a linear regression slope with a seed-level significance test) rather than discarding magnitude information to ranks.

**NOT routed to `/implement-substrate`**: the substrate-level gap 848's autopsy identified (dacc_adapter response magnitude, later re-diagnosed as a units/calibration mismatch by IGW-199) is closed and confirmed working. No new substrate need is identified by this run.

**NOT a claim demotion**: ARC-005 stays `active`; this sub-question (GAP-A-precision-diagnostic) remains open, not weakened.

**Re-derive brake check**: ARC-005 has 0 `substrate_ceiling` hits under the R1-R3 convention (802: standard, 848: standard; this target: standard) — brake does not fire, consistent with routing to a design fix rather than `/implement-substrate`.

**Granularity-debt trigger**: `granularity_debt_cluster.py ARC-005` — 2 prior targets (802, 848), alignment distribution `intact=2` (no target reads `weakened`). Adding this target (`intact`) keeps the distribution `weakened`-free — trigger does NOT fire. This is measurement debt on one sub-question, not granularity debt on the claim.

**Draft `evidence_quality_note` for governance:**

> [2026-08-03 governance, V3-EXQ-848a, confirmed failure_autopsy_V3-EXQ-848a_2026-08-03, successor of V3-EXQ-848]: calibration fix (dacc_goal_readout_weight=0.5, dacc_goal_readout_normalize=True, IGW-20260801-199) confirmed genuinely engaged this run (25,289 dACC bias calls, build-time guard held) — the wiring/calibration line of inquiry 848 opened is CLOSED. C_precision_monotonicity still only 1/10 units satisfied, but the per-unit rho distribution (7/10 positive-signed, 6 at exactly 0.5) is the signature of a 3-point-ladder Spearman-rho resolution ceiling, not a clean null (802's genuinely-null channels showed bit-identical rho=0.0). Routed to `/queue-experiment` for a ladder-granularity redesign (V3-EXQ-848b: 5+ levels and/or a magnitude-based statistic), NOT to further substrate work. epistemic_category=standard (not substrate_ceiling). No status change (already active). PROMOTES/DEMOTES NOTHING.

## 8. Interactive gate (Step 8)

Presented to the user via AskUserQuestion 2026-08-03T09:0*Z: facts, claim-layer mapping, biological triage, four-layer table, recommended routing (`/queue-experiment` redesign, epistemic_category=standard). **User confirmed: "Agree: measurement redesign (Recommended)."**

## 9b. Hypothesis-space ledger

New question registered: `arc005_precision_channel_measurement_resolution` (claims: `[ARC-005]`). One hypothesis pre-registered and resolved in the same edit (single leg, no prior pre-registration existed): `H-arc005-calibrated-channel-monotonic`, resolved to **`alive`** (does not meet the elimination bar — `met_elimination_bar: false` — an inconclusive/non-discriminating result surfaces a measurement bottleneck for Dimension 4, per the skill's state-mapping table, rather than eliminating or confirming the hypothesis). `pre_registered_utc` set to the run's own completion date (2026-08-02T12:07:12Z), satisfying invariant 2. `initial_frozen_count == 1 == len(hypotheses)`, `initial_frozen_count_at_registration == 1` — new question, no fan-out growth. `decision.decidable: false`.

**`build_hypothesis_space.py` currently crashes for EVERY question, not just this one** — pre-existing, unrelated to this append: `evidence/planning/hypothesis_space_registry.v1.json`'s `inv088_evaluator_degeneracy_cause` question (written by another concurrent session's V3-EXQ-108b autopsy, landed in `43004f2`) carries a bare **string** in its `synthesis` field instead of the schema's `{surviving_label, text}` object; `_question_rollup()` calls `.get()` on it unconditionally and raises `AttributeError`, so no derive/audit output could be produced for this append either. Verified by diffing against `HEAD` before my edit — the corrupt entry pre-dates this session's write. Did NOT attempt to fix `inv088_evaluator_degeneracy_cause`'s data (out of scope — that question's `surviving_label`/`text` split needs its own authoring session's context, not a guess) or reimplement the script's defensiveness. Instead: manually verified my own question against the schema (every field present, `initial_frozen_count == len(hypotheses) == initial_frozen_count_at_registration == 1`, `pre_registered_utc <= resolved_utc`, `alive` state carries `met_elimination_bar: false` per the state-mapping table) and flagged + chipped the corruption as a standalone fix (it blocks every other session's `/failure-autopsy` Step 9b run too, not just this one).

## 10. Follow-on (reported, not chipped — per the autopsy's-own-routing rule)

- `/queue-experiment` a ladder-granularity redesign successor (candidate letter `V3-EXQ-848b`) once `/governance` ratifies this routing. Not chipped from this session per CLAUDE.md Session Land Protocol step 6 / SKILL.md Step 8's "do not spawn_task the routing's own follow-on" rule — governance chips it after Step 2b/4/6a ratification.
- Secondary, lower-priority: a `targeted_review_ARC-005` (or dACC-goal-proximity-specific) literature entry does not yet exist; noted for a future `/lit-pull`, not commissioned here (this autopsy's routing does not depend on it).
