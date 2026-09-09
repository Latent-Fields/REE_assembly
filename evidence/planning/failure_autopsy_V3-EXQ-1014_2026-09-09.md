# Diagnostic adjudication -- V3-EXQ-1014 (983-lineage stage-1 spike: does canonical E3 latch a single action class?)

- **Status:** `confirmed` (user gate 2026-09-09T00:55:13Z) -- drafted interactively by session `fa-20260909-batch`
  (DLAPTOP main checkout, batch with V3-EXQ-1015 and V3-EXQ-822f), red-teamed cross-model at
  Step 7c (**CONTESTED**, four findings, all applied; the draft's refusal of stage 2 is
  WITHDRAWN -- Section 9), Step 8 gate held (Section 9).
- **Generated (UTC):** 2026-09-09T00:26:26Z
- **Scope:** single
- **Run:** `v3_exq_1014_ext002_lineage_e3_latching_repertoire_spike_20260908T223415Z_v3`
- **Queue id:** V3-EXQ-1014 -- `experiment_purpose: diagnostic`, `claim_ids: []`,
  `bears_on: [actor_adequacy_monostrategy, residue_error_persistence_readout]` (the first is not a
  registry qid -- see Section 2), lineage "V3-EXQ-983 / V3-EXQ-983a stage-1 spike (NOT a letter,
  NOT a supersession)", campaign W5-S2b item 4, chip
  `chip-20260906-exq983-lineage-latching-spike-then-avoidance`.
- **Outcome:** PASS, `evidence_direction: diagnostic_no_direction`, self-route
  `repertoire_exists_stage2_proceeds`, `gate_green: true`, `non_degenerate: true`.
- **Ran:** 6785 s on `ree-cloud-2`, `linux-x86_64-py3.10-torch2.12.0+cpu`, substrate hash
  `f6fc776b61a1...` (all 8 cell fingerprints agree; `substrate_stable_across_run: false` only
  because the disk moved 6645 s after fingerprinting).
- **Dry-run gate:** clean (0 dry / 1 real; the smoke's manifest went to scratch and FAILed its own
  adjudicability floor as the docstring predicts).
- **Recording:** flat JSON complete (`config`, `seeds`, `elapsed_seconds`, `recording_schema`,
  `arm_results` with fresh AND executed action-class histograms, per-episode fresh histograms and
  survival curves, `control_policies`, `readout`, `stage2_routing`). Run-pack thin (`metrics.json`
  empty). 983a's recording gap (training-phase histogram) is closed by this run.

**Headline.** The PASS holds on its pre-registered statistic: strict single-class latching
(>= 0.95 of fresh decisions) holds on only 2/8 seeds, so the strict form of 983a's inference is
refuted. Two things narrow that. The label is **bar-sensitive** -- it flips at a bar of 0.75-0.78
-- and under a dominance reading the run **reproduces 983a's picture** on 5/8 seeds: stay-dominant
seeds die, constant-move-dominant seeds survive, and on the three stay seeds most episodes are
STAY at both fresh decisions with exactly the STAY control's survival. The recorded cells point to
the **selection** face (a fresh STAY choice inside the harm field), not to hold duration. The
casualty set is identical to 983a's, but 983a's ratified stage 2 already draws seeds until its
pooled floor is met; this run **prices** that draw (~1/8 pass rate under the ratified gates,
~27-38 h) rather than blocking it.

---

## 1. Facts (no interpretation)

### 1a. Design

Same 8 pinned 6x6 boards as 983a (seeds 42, 123, 456, 7, 11, 17, 23, 31; layout and start
rebuilt from the seed every episode), canonical E3 over 32 hippocampal CEM candidates, residue
intact, 40 episodes x 200 steps per seed. A FRESH decision = an `e3_tick` (nominal period 10,
MECH-093-modulated; realised 5.5-9.5 from the yield) or an episode's first step; only E3-selected
actions enter the repertoire histogram (0 fallbacks). Pre-registered readout over ADJUDICABLE
seeds (>= 30 fresh decisions): `latched_fraction` = share of seeds with one class at >= 0.95;
alternative label fires if >= 0.5, OR (>= 3 adjudicable casualties AND casualty-latched >= 0.5).
Casualty = >= 50% of episodes ended early. Yardstick: RANDOM_WALK, STAY, CONSTANT_0..3, 3 episodes
each per board. STAY is action index 4.

### 1b. Per-seed results

| seed | fresh hist {class: n} | top share | latched | executed STAY share | held frac | harm | harm on held (share) | harm / held tick | harm / fresh tick | mean steps | casualty |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 42 | {0:20, 4:62} | 0.756 | no | 0.754 | 0.829 | 390 | 310 (0.795) | 0.779 | 0.976 | 12.0 | yes |
| 123 | {0:12, 1:4, 3:3, 4:67} | 0.779 | no | 0.738 | 0.849 | 457 | 375 (0.821) | 0.778 | 0.953 | 14.2 | yes |
| 456 | {0:99, 2:27, 3:693} | 0.846 | no | 0.000 | 0.895 | 168 | 84 (0.500) | 0.012 | 0.103 | 194.9 | no |
| 7 | {1:1, 2:22, 3:42, 4:46} | 0.414 | no | 0.383 | 0.874 | 440 | 343 (0.780) | 0.445 | 0.874 | 22.0 | yes |
| 11 | {0:128, 1:156, 2:2, 3:87, 4:1} | 0.417 | no | 0.003 | 0.890 | 502 | 326 (0.649) | 0.108 | 0.471 | 84.7 | yes |
| 17 | {1:50, 3:5, 4:60} | 0.522 | no | 0.410 | 0.866 | 420 | 355 (0.845) | 0.478 | 0.565 | 21.4 | yes |
| 23 | {1:1, 4:80} | 0.988 | **yes** | 0.978 | 0.820 | 440 | 359 (0.816) | 0.976 | 1.000 | 11.2 | yes |
| 31 | {1:840} | 1.000 | **yes** | 0.000 | 0.895 | 120 | 80 (0.667) | 0.011 | 0.048 | 200.0 | no |

Per-episode alignment: episodes whose EVERY fresh decision was STAY -- seed 42: 22/40 (mean 10.0
steps; STAY control 10.0), 123: 24/40 (12.0; 12.0), 23: 39/40 (11.0; 11.0), 7: 6/40, 17: 9/40,
11: 0/40. Readout: `latched_fraction` 0.25, `casualty_latched_fraction` 1/6, 2x2 latched x died =
{latched casualty 1, latched survivor 1, diverse casualty 5, diverse survivor 1}. Readiness 4/4.
Yardstick on every board: CONSTANT_0..3 survive 200/200 (harm 0.0-0.015); STAY dies in 10-14 steps
(harm 1.0); RANDOM_WALK dies in 11-17 steps (harm 0.65-0.88). Bar sensitivity: at 0.80 latched
3/8 (null holds); at 0.75 latched {42, 123, 456, 23, 31} = 5/8 and the alternative label fires.

### 1c. The predecessor

983a's completion gate excluded seeds 42, 123, 7, 11, 17, 23 (steps_realized 0.056-0.116; seed 11
0.475) and pooled 456 and 31 -- **identical to this run's casualty set**, with per-seed
steps_realized_frac agreeing to two decimals. 983a's CONFIRMED routing_note for stage 2, verbatim:
"STAGE 2 (evidence, only if the repertoire exists): residue-frozen ablation with a hold-aware
revisit-AVOIDANCE DV (fresh-decision revisits to erred keys per unit exposure, early vs late, A0
minus A1), P7-style certification of DV freedom under a control policy BEFORE training, per-seed
gate on action-stream divergence > 0 and on action-class diversity, MIN_POOLED_SEEDS 3, seeds
drawn until the floor is met."

---

## 2. Claim layer

Claim-free. `bears_on` tokens carried VERBATIM from the manifest. **`actor_adequacy_monostrategy`
is not a registry qid** (the registry's actor-adequacy question is `zworld_actor_adequacy_locus`;
grep count 0 for the token), so GOV-DIAG-1 will key a chain on a token that resolves to nothing;
governance should add `zworld_actor_adequacy_locus` when applying. 983a's JSON target carried no
`bears_on`.

**Was the self-route a hypothesis that held for a real reason?** The *statistic* yes, under the
pre-registered rule, with the bar sensitivity disclosed. The *inference* ("stage 2 proceeds") is
also sound, for a reason the draft of this artifact got wrong: the ratified stage 2 is not pinned
to these 8 seeds.

---

## 3. Biological-reference triage

Basal-ganglia action selection over a passive-avoidance substrate (`targeted_review_ext_002`;
`targeted_review_commit_release_duration_latch` for the hold). The cells implicate the
**selection face**, as 983a inferred: the harm-on-held share (0.65-0.85 across casualties) equals
or sits slightly below the held-tick share of realised steps (0.82-0.89) -- the base rate of a
~10-step hold -- and per-tick harm is **lower** on held ticks than on fresh ticks on every
casualty (robust to dropping step-0 ticks on 5/6). On seeds 42/123/23, E3 re-deliberates at step
10 and chooses STAY again. The hold reproduces the lethal choice; it does not create it. No
`/lit-pull` owed.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | Statistic sound under the pre-registered rule; bar-sensitive (0.75-0.78); 983a's dominance picture reproduced 5/8. |
| Biological reference | **clear** | Selection face; hold duration not implicated by these cells. |
| Prerequisites | **present** | Residue live on every harm; E3 used 100%; candidates always present. |
| Implementation | **partial** | The actor: strict latching 2/8 (split 1/1 on survival); casualty longevity orders with falling STAY share (23 < 42 < 123 < 17 ~ 7 < 11: 11 -> 85 steps); survivors execute STAY on 0 steps; no executed histogram is near uniform. |
| Environment | adequate-but-unforgiving, not the lever | Constant movers 200/200 on all 8 boards. |
| Measurement | **partial** | (i) `closest_control_profile` is decided by harm rate alone when every policy dies (steps term <= 0.035): a 75%-STAY agent at harm 0.81 is labelled RANDOM_WALK -- uninformative. (ii) The harm-on-held figure is structural to the hold schedule (999a red-team F2 lesson). The discriminating recordings -- executed histogram, per-tick harm held vs fresh, per-episode fresh histogram aligned to survival -- are all present. |
| Integration | partially coupled | Residue accumulates every harm; E3 re-selects STAY at the next fresh decision; whether residue can shift a fresh selection is stage 2's question. |
| Scale | adequate | 8/8 adjudicable (82-840 fresh decisions). |

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Verdict |
|---|---|
| MECHANISM FAILED | **partial** -- selection-face reading supported by per-episode alignment and per-tick ratios, not manipulated |
| MEASURES FAILED | **partial** -- pre-registered bar honoured but flips at 0.75-0.78; yardstick profile uninformative |
| ENVIRONMENT FAILED | not established |
| REE FAILED | **false** |

**Net: MIXED, not chargeable to REE.** "REE dies faster than a constant mover on these boards" is
recorded as MIXED, never as REE FAILED.

### Recommended `epistemic_category`

`standard` (claim-free).

---

## 5. Learning extracted

1. **Strict latching is refuted on 6/8 under the pre-registered rule, but the rule is bar-sensitive**
   (flip at 0.75-0.78), and under a dominance reading 983a's picture holds on 5/8. State the
   sensitivity beside the label; a strict-bar null is not "the predecessor named the wrong mechanism".
2. **The harm-on-held figure is the base rate of the hold schedule** (0.65-0.85 vs held share
   0.82-0.89) and discriminates nothing; per-tick harm is lower on held ticks on 6/6 casualties;
   pure-STAY episodes equal the STAY control. The cells lean to the selection face. A readout tied
   to the hold schedule is confounded with the schedule for any agent.
3. **The yardstick profile is decided by harm rate alone** when every policy dies; it must not be
   read as "the actor is a random walk" -- no executed histogram is near uniform.
4. **The casualty set is identical to 983a's, and 983a's ratified stage 2 already anticipated it**
   ("seeds drawn until MIN_POOLED_SEEDS 3 is met", divergence + diversity gates, DV per unit
   exposure). This run prices the draw: ~1/8 pass rate under the gates (only 456 of 8; 31 is
   single-class with 983a divergence 0.00), ~12-24 draws, ~27-38 h at 983a's ~0.51 s/step
   (casualties are cheap). The pooled population will be constant-mover seeds -- a selection effect
   for governance to accept or reject explicitly.
5. **Casualty longevity orders with falling STAY share**; the most diverse casualty (11) is the
   longest-lived. "Diversity does not protect" is true of full-budget survival, not of longevity.
6. **Recording:** 983a's gap closed; pack thin; `experiment.md` TODO placeholders; the manifest's
   first `bears_on` token is not a registry qid.

### Re-derive brake / GOV-DIAG-1

Claim-free; no claim count. `bears_on` verbatim (Section 2). **Not refused:** stage 2 as ratified.
**Refused only:** a 983 letter keeping the repeat-rate DV or fresh-tick-only keys (unchanged from
983a).

---

## 6. Repair pathway and routing (confirmed at the gate)

**Node classification:** `complicated (buildable)` for stage 2 -- fully specified by the 983a
routing_note, no new fact needed; `complex (probe-gated) / puzzle (known rules)` for the
OPTIONAL casualty-mechanism probes.

**Routing: `queue-experiment`** -- stage 2 as ratified, plus optional diagnostics (governance chips;
this session spawns nothing).

1. `/governance` -- ratify: PASS holds on its statistic (strict latching refuted 6/8; bar-sensitive;
   983a's dominance picture reproduced 5/8); **stage 2 proceeds as designed** under its own seed
   draw, with an explicit decision on the selection effect this run prices (~1/8 pass rate,
   ~12-24 draws, ~27-38 h, constant-mover pooled population). Annotate
   `residue_error_persistence_readout`'s `live_gate`: stage 1 answered; stage 2 released with the
   draw priced.
2. `/queue-experiment` -- **stage 2 per the 983a routing_note**, NEW EXQ number (not a 983 letter),
   on a survival-screened draw.
3. OPTIONAL fan-out (GOV-FANOUT-1), if governance wants the casualty mechanism itself:

| leg | axis | probe sketch (no build needed) | null |
|---|---|---|---|
| H-stay-selection-dominance (leading; 983a's picture) | selection | STAY removed from / floored in the E3 candidate set vs canonical, 8 boards | casualties persist with STAY masked |
| H-held-commitment-lethality (cells lean against) | timescale-realised | `config.heartbeat.e3_steps_per_tick = 1` (used by v3_exq_066/123/124/827) vs canonical; optional de-commit-on-harm arm via the existing default-off `use_habenula_decommit` knobs | survival unchanged without the hold |
| H-actor-uninformative (unmeasured) | measurement | decision-tick-only scoring against the local hazard gradient, reusing V3-EXQ-999a's instrument (hazard-blind null + conditional oracle) | indistinguishable from the hazard-blind null |

4. `/governance` -- annotate the actor-adequacy line (`zworld_actor_adequacy_locus` / MECH-269 /
   MECH-341 / ARC-065) and `dv-dynamic-range-precondition-class` (the priced draw); resolve the
   `bears_on` token mismatch. Substrate queue: `none`.

**Explicitly not recommended:** refusing stage 2 or rewriting its `live_gate` on the withdrawn
"same 2-seed floor" premise; a 983 letter; gating stage 2 behind the probes;
`/implement-substrate` (the knobs exist); `/lit-pull`; reading "REE fails to survive" as REE
FAILED; reading `closest_control_profile` as evidence of a random walk.

---

## 7. Hypothesis-space ledger (Step 9b, applied after the gate)

New question `ext002_lineage_survival_lever` (claims [EXT-002, ARC-013], `pre_registered_utc` =
run date), Mode B: **H-latch-single-class-strict** `eliminated` at the pre-registered >= 0.95 bar
only (bar-qualified; flips at 0.75-0.78; yardstick controls ran; non_degenerate true). Mode A:
**H-stay-selection-dominance** (alive; supported 5/8 under a dominance reading; STAY-mask probe),
**H-held-commitment-lethality** (alive; cells lean against; hold = 1 probe),
**H-actor-uninformative** (alive; unmeasured; 999a-style probe). Axes `selection`,
`timescale-realised`, `measurement` -- all in `axis_families.map`. `residue_error_persistence_readout`
untouched except the human-owned `live_gate` text governance may update.

## 8. Mechanical checks

- Dry-run gate: clean. Recording: pack thin, flat complete. Lint: silent.
- Step 7b: **0 fires**; C1/C2/C3 structurally inapplicable (`claim_ids: []`).
- Step 7c: Section 9.

## 9. Step 7c red team and Step 8 gate

**Step 7c -- cross-model, read-only. Model Fable 5.1 (`claude-fable-5-1`). Verdict: CONTESTED.**
Findings file `redteam_1014.md` (session scratchpad). It reproduced every per-seed sum
(fresh + held = executed on all 8 seeds), the casualty-set identity with 983a, the STAY index, the
control profiles and the readout arithmetic. Four findings moved assertions or recommendations;
all applied:

| # | Finding | Disposition |
|---|---|---|
| F1 | the refusal of stage 2 rested on a misdescription: 983a's ratified stage 2 draws seeds until MIN_POOLED_SEEDS 3 with divergence + diversity gates | **APPLIED** -- refusal WITHDRAWN; run re-read as pricing the draw (~1/8, ~27-38 h); live_gate rewrite withdrawn |
| F2 | "held-commitment lethality" is the hold-schedule base rate; per-tick harm lower on held ticks on 6/6; pure-STAY episodes = STAY control | **APPLIED** -- mechanism reading reversed to the selection face; hold leg kept alive, leaning against |
| F3 | "983a named the wrong face" is an artefact of the 0.95 bar; label flips at 0.75-0.78; dominance reading supports 983a 5/8 | **APPLIED** -- bar sensitivity disclosed; "sign reversed" retracted; ledger elimination bar-qualified |
| F4 | `closest_control_profile` is a harm-rate nearest-neighbour that mislabels 75%-STAY seeds as RANDOM_WALK; H3 and learning 4 rested on it | **APPLIED** -- H3 basis rewritten as unmeasured; learning 4 rewritten |

Hygiene H1-H7 applied (65-85% range; `bears_on` token not a registry qid; existing knobs
`e3_steps_per_tick`, `use_habenula_decommit`, 999a instrument named; realised hold 5.5-9.5;
learning re-targeted; longevity ordering stated). The existing-work check on all three probes
passed: none is built, queued, or chipped.

**Step 8 gate -- user decision, binding (2026-09-09T00:55:13Z):**

> Stage 2 as ratified, accept the priced draw (Recommended) -- the three casualty-mechanism probes stay optional chips.

The routing above is confirmed as drafted; the hypothesis-space ledger moves in Section 7 are applied in this session.
