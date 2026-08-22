# Failure autopsy -- V3-EXQ-944 (MECH-091, salient-event cycle boundary)

- **Run:** `v3_exq_944_mech091_salient_event_cycle_boundary_20260822T035234Z_v3`
- **Queue:** V3-EXQ-944 | **Claim:** MECH-091 | **Purpose:** evidence | **Outcome:** FAIL
- **Generated:** 2026-08-22T11:35:04Z | **Scope:** single | **Status:** confirmed
- **Machine:** ree-cloud-2 (`linux-x86_64-py3.10-torch2.12.0+cpu`) | **elapsed:** 4303.7 s
- **Routing:** `/queue-experiment` -- V3-EXQ-944a, same question, implementation/measurement repair

> **Read the AS-RAN substrate, not the working tree.** `ree_core/agent.py` was ` M` (being edited by
> another live session) *during* this autopsy: line 10026 read `self.clock.phase_reset()` at one point
> and `try:` minutes later. Every `agent.py` citation below is against **substrate_commit
> `751fc5e33d58095d9c59c056bf7f7790326a595d`** (`dirty: false`), and the baseline lib against ree-v3
> **`243a085`**. `experiments/_lib/baselines/mech091_phase_reset.py` is currently `M ` **staged** by the
> in-flight 944a session and is *not* the version that ran.

## 0. Dry-run gate (Step 2a)

`check_dry_run_citations.py`: **0 dry cited, 1 clean, 0 ambiguous**; `dry_run: false` on the manifest.
`excluded_dry_run_ids: []` -- no statistic here has a smoke in its denominator. The
`dry_run_unreachable_criterion` lint fires on 11 drivers, all the unrelated `v3_exq_543` lineage.

Recording provenance: `validate_recording.py` reports **complete** -- no always-core gap, so no
recording-debt route. Every number below was recomputable from the landed manifest without a re-run.

## 1. Facts -- every criterion passed; a readiness precondition failed

| | result |
|---|---|
| C1 manipulation check (not load-bearing) | **PASS** |
| C2 `straddle_frac(ALIGNED) <= 0.05` (load-bearing) | **PASS** |
| C3 `straddle_frac(RATE_MATCHED) - straddle_frac(ALIGNED) >= 0.50` (load-bearing) | **PASS** |
| C4 lag delta (corroborating) | **PASS** |
| `criteria_non_degenerate` | all four `true` |
| P1 `salient_events_per_cell_floor` (>=20) | met (89) |
| P2 `no_reset_control_shows_partial_integration` (>=0.50) | met (1.0) |
| **P3 `rate_match_holds` (max-over-seeds <= 0.35)** | **NOT met -- 0.914** |

`PASS iff (P1 AND P2 AND P3) AND C1 AND C2 AND C3`. P3 alone sank it.

| seed | rate(ALIGNED) | rate(RATE_MATCHED) | P3 dev | P3 | C3 delta | ep len AL/RM/NR |
|---|---|---|---|---|---|---|
| 42 | 0.5015 | 0.0431 | **0.914** | **FAIL** | 0.826 | 22.5 / 8.5 / 7.4 |
| 7 | 0.1210 | 0.1181 | 0.024 | pass | 1.000 | 69.7 / 64.1 / 68.3 |
| 13 | 0.1536 | 0.1477 | 0.039 | pass | 0.945 | 69.9 / 72.0 / 71.2 |
| 100 | 0.1477 | 0.1359 | 0.080 | pass | 0.948 | 72.0 / 53.5 / 47.4 |
| 200 | 0.2227 | 0.2188 | 0.018 | pass | 0.790 | 59.9 / 49.7 / 60.9 |

The rate match holds at **1.8-8.0%** on four seeds and collapses on one.

## 2. What broke -- the control degenerated into the arm it was meant to be distinguished from

RATE_MATCHED suppresses the reset at the event and re-issues it at `event_step + U{K..2K}`, K=10
(`mech091_phase_reset.py:301-313`). `clock._global_step` is zeroed at every `agent.reset()`
(`clock.py:225` via `agent.py:3214`), so it is a **within-episode** counter and the clamp's units are
coherent. *(An earlier hypothesis that the clamp mixed global and per-episode coordinates was checked
against the source and **refuted** -- recorded rather than deleted.)*

On seed 42 RATE_MATCHED executed **4 of 236** requests, and its `episode_lengths` are **element-wise
identical to NO_RESET for the first 21 of 30 episodes**. It did not fail to be built -- it *became*
NO_RESET, which is exactly the "drift back toward NO_RESET" the clamp comment says it exists to prevent.

### 2a. The collapse is TREATMENT-INDUCED, not a hostile seed

This corrects an earlier reading in this autopsy's own drafting. `diagnostics.warmup_episode_lengths_by_seed`
records a **shared, arm-independent** warmup (one P0 per seed, snapshot deep-copied into all three arms;
`warmup()` never patches `phase_reset`):

| seed | warmup (arm-independent) | ALIGNED | RATE_MATCHED | NO_RESET |
|---|---|---|---|---|
| **42** | **24.37** | **22.53** | **8.50** | **7.43** |
| 7 | 70.85 | 69.70 | 64.07 | 68.27 |
| 100 | 72.00 | 72.00 | 53.47 | 47.37 |

Seed 42's environment sustains ~24-step episodes and ALIGNED holds 22.53. The collapse to 7-8 appears
**only where the reset is withheld**. The mechanism is a **runaway feedback**:

> withhold the event-aligned reset -> episodes shorten -> a re-issue deferred by >=K can no longer fire
> before the episode ends -> still fewer resets execute -> episodes shorten further.

**Consequence for the successor, and it is the single most important line in this document:** episode
length and `n_events_with_following_tick` are **post-treatment outcomes**. Excluding cells on either --
the obvious "cell-adequacy precondition" fix -- discards precisely the cells where the manipulation bites
hardest and would bias 944a toward PASS. It must not be done, pre-registered or otherwise.

### 2b. The existing clamp is inert

`due = min(due, episode_step_budget)` with budget 72, while `drain()` runs *before* each of `range(72)`
steps -- so `_global_step` tops out at **71** and a clamped `due == 72` can **never** fire. Unclamped,
a `due` past the budget never fired either. The clamp changes **zero outcomes**; it would need
`episode_step_budget - 1`. The budget-overrun losses it was believed to prevent are therefore real and
unprevented, and form part of the execution shortfall on the healthy seeds (74/110, 93/186, 270/415).

## 3. Three mis-specified guards

**(i) P1 is denominated on the wrong quantity.** `straddle_frac` is computed over `len(lags)`, and events
with no following tick in the episode are **silently dropped** (`mech091_phase_reset.py:437-440`,
`if idx < len(tick_list)`). P1 floors `n_salient_events` instead -- though its own description says "the
DV is per-event, so a cell below this measured nothing usable".

| cell | n_salient_events | DV sample | coverage |
|---|---|---|---|
| ALIGNED/42 | 356 | 326 | 91.6% |
| RATE_MATCHED/42 | 236 | **23** | 9.7% |
| NO_RESET/42 | 235 | **10** | 4.3% |
| RATE_MATCHED/100 | 186 | 96 | 51.6% |

NO_RESET/seed42's DV sample is **10 -- below P1's own floor of 20** -- while P1 reported `met: true,
measured: 89.0`. *Direction of the resulting bias, checked not assumed:* an event with no following tick
is the most extreme straddle case and the exclusion hits the low-tick arms hardest, so it pushes
`straddle_frac` **down** in RATE_MATCHED and NO_RESET -- **against** C3. C3's PASS is robust to it.

**(ii) P3 is partially self-cancelling.** It compares ticks/step; RATE_MATCHED depresses numerator and
denominator together.

| seed | executed / requested | count ratio vs ALIGNED | P3 dev | verdict |
|---|---|---|---|---|
| 42 | 4 / 236 (1.7%) | 0.01 | 0.914 | FAIL |
| 7 | 74 / 110 (67.3%) | 0.83 | 0.024 | pass |
| 13 | 144 / 174 (82.8%) | 1.01 | 0.039 | pass |
| 100 | **93 / 186 (50.0%)** | **0.72** | **0.080** | **pass** |
| 200 | 270 / 415 (65.1%) | 0.89 | 0.018 | pass |

**(iii) P2 measures a constant.** `straddle_frac(NO_RESET)` is **exactly 1.0 in 5 of 5 cells** -- **0 of
618** events at lag 1 -- against the driver's declared "uniform-ish over [1, K]" model, under which
P(lag=1)=0.1 and P(0 of 618) ~ **5e-29**. Mean lag 8.55 vs 5.50 predicted. Events are phase-locked to
just-after-tick, so small lags are structurally depleted and P2 **cannot** fall below its floor.

This is *not* a rediscovery of the driver's declared C2 identity (that concerns ALIGNED and is disclosed);
P2 concerns NO_RESET, which the driver affirmatively declares as *varying*.

## 4. Claim layer -- MECH-091

`mechanism_hypothesis`, status `candidate`, `implementation_phase: v3`, `depends_on: [ARC-023, MECH-090]`,
`epistemic_category` **absent**. Un-parked six days ago: governance 2026-08-16 (GFLAG-0037 SPLIT) lifted
the SD-006-phase-2 deferral as **mis-scoped**, and `MECH091-SALIENT-EVENT-TRIGGER-WIRING` is now
`implemented`.

**Did the experiment let the claim express itself?** On four of five seeds, yes -- and it produced the
**timing** half of the confirming signature. The claim is **not** weakened: nothing failed anywhere.

**Stale text (hygiene).** `what_would_answer` still carries the pre-2026-08-16 line "A run without SD-006
phase 2 self-routes substrate_not_ready", which the GFLAG-0037 decision in the *same claim's*
`evidence_quality_note` lifted. That is the likely source of the driver's coarse mapping `P unmet ->
substrate_not_ready_requeue`, which routes a **harness** defect to **substrate absence**. P1/P2 do guard
readiness; **P3 guards the harness's own control arm** and does not belong in that mapping.

## 5. Biological reference -- clear, and it already specified this control

Closest mechanism: stimulus-driven phase reset of ongoing cortical theta/alpha oscillations (P300
substrate). **Not a formal import** -- the claim's `functional_restatement` declares the ANN form as a
cycle-boundary marker and says the biological oscillator is not required. `lit_status: present` --
`targeted_review_connectome_mech_091` holds **5 entries**.

**Rizzuto 2003** (PNAS, intracranial) establishes genuine phase reset precisely by showing cross-trial
phase locking **without an increase in oscillatory power**. **Sauseng 2007**, in this claim's own review,
states that a V3 test of MECH-091 "should include controls that distinguish genuine phase shift ... from
amplitude injection". RATE_MATCHED is that *kind* of control -- hold the confound fixed, move the phase --
though the analogy is not exact: Sauseng separates phase from **amplitude**, RATE_MATCHED from **rate**.

So a broken RATE_MATCHED is **not** a bureaucratic gate trip: it is the loss of the one control that makes
this a *phase-reset* finding rather than a *replans-more-often* finding. Does the failure resemble a
missing biological dependency? **No** -- the mechanism fired 356 times on ALIGNED/seed42 and C1 passed
everywhere.

## 6. Is the harm stream's trace active and valid here?

Asked because an integration DV was under consideration. The answer splits.

**(1) Valid for what this run measured.** The harm salient-event trigger fires on `harm_signal < 0`,
documented at `agent.py:9850` (as-ran) as "**Harm from environment** (negative = harm)" -- a value passed
into `update_residue()`, **not** a learned head. It is therefore immune to head grounding and to the
EXQ-131 staleness artifact, exactly as the driver's pre-queue check claimed. It fired abundantly and
non-degenerately (**2779** harm triggers run-wide, 207-326/cell), and `post_event_harm_mean` spans
0.069-0.872 and responds to the arm.

**(2) NOT constructible for an INTEGRATION DV on this protocol.** `what_would_answer`'s second half
concerns harm/goal **estimates** -- learned heads -- and this lineage trains none of them:

- `warmup()` runs only `compute_prediction_loss() + compute_e2_loss()`, and `compute_e2_loss` trains E2's
  **z_self forward model** (`predict_next_self`, `agent.py:11221-11237`) -- **not** `E2_harm_s`.
- E3's `harm_eval` / `benefit_eval` are untrained, hence **random-init**. `agent.py:9690-9693`:
  that signal "is only meaningful once those heads are grounded (ARC-030 phased protocol) -- a validation
  using it **MUST first assert grounding on a positive control**." This run asserts none.
- The **goal** half is not instantiated at all: `z_goal_stream.goal_state_present: false`, with
  `writer_defect: null` -- configuration, not a defect.

**Therefore the integration question is `complex (probe-gated)`, not `complicated (buildable)`.** Bolting
an integration DV onto 944a would read an ungrounded random-init head and manufacture precisely the
vacuous measurement this autopsy is about.

## 7. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | nothing failed; 4/5 seeds show the timing signature |
| Biological reference | **clear** | 5 entries; RATE_MATCHED is the field's own confound-control shape |
| Prerequisites | **present** | wiring `implemented` and firing (harm 2779, commit_entry 448) |
| Implementation | **complete (mechanism) / partial (control arm)** | `phase_reset()` works; the deferral scheme self-destructs |
| Environment | **adequate** | warmup sustains 24.37 on seed 42; the collapse is post-treatment |
| Measurement | **under-instrumented** | P1 mis-denominated, P3 self-cancelling, P2 constant |
| Integration | coupled | not implicated |
| Scale | adequate | 30 episodes x 72-step budget suffices |

### Failure-location summary (GOV-FAILLOC-1)

- **MECHANISM FAILED -- not established.** Implementation complete *and* every criterion passed.
- **MEASURES FAILED -- established.** Control-arm construction plus three mis-specified guards.
- **ENVIRONMENT FAILED -- not established.** *(Corrected from an earlier draft.)* The arm-independent
  warmup shows the environment sustains the episodes; the collapse is an outcome of the treatment.
- **REE FAILED -- false.**

**Net: MEASURES -- not chargeable to REE, and not chargeable to MECH-091.**

## 8. Non-gating observation the criteria do not cover

The **survival effect** of the event-aligned reset, ALIGNED vs NO_RESET mean episode length: seed 42
**22.53 vs 7.43 (3.03x)**, seed 100 **72.00 vs 47.37 (1.52x)**, seed 7 1.02x, seed 13 0.98x, seed 200
0.98x. Large on 2 of 5, null/reversed on 3 of 5 -- **sign-inconsistent**, so it does not move
`evidence_direction`, and the driver had already de-gated behavioural readouts as noisy on an untrained
agent. Recorded because it is the run's most interesting unpre-registered signal and deserves proper
pre-registration on a protocol that grounds the heads.

## 9. Routing -- `/queue-experiment` (V3-EXQ-944a)

**Not `/implement-substrate`** (substrate built, `implemented`, firing -- `action: none`, no substrate
write owed). **Not `/lit-pull`** (5 entries, biology clear). **Not a demotion** (nothing failed). The
defect is in `experiments/_lib/baselines/mech091_phase_reset.py`, a harness file.

**944a must:**

1. **Not exclude cells on any post-treatment quantity** (episode length, DV sample, execution fraction). Report episode length as an **outcome**.
2. Replace/supplement P3 with a **count-based** guard, `n_resets_executed(RM)/n_resets_executed(ALIGNED)`.
3. Re-denominate **P1** on `n_events_with_following_tick`.
4. Replace **P2** with a guard that can fail, or demote it to a diagnostic.
5. Address the **runaway feedback** directly, not by clamping. If a clamp is kept it must be `episode_step_budget - 1` -- the current one is inert.
6. **Split the self-route mapping**: P1/P2 -> `substrate_not_ready_requeue`; **P3 -> a control-construction/measurement route**, not substrate absence.
7. Record the re-issue execution fraction and the count scheduled past episode end.

**944a must not** bolt on an integration DV -- see section 6.

**Separate, probe-gated follow-on** (not chipped here; `/governance` ratifies an autopsy's own routing
before it is spawned, per CLAUDE.md Session Land Protocol step 6): the **integration** half of
`what_would_answer` needs a cheap observability probe first -- the same discipline GFLAG-0037 applied
before 944 was queued -- establishing a protocol that grounds E3 `harm_eval` with a positive-control
assertion (or an integration readout on a head this protocol does train), and, if goal estimates are in
scope, the goal subsystem enabled.

**Re-derive brake: does not fire.** 0 ceiling hits for MECH-091 under R1-R3 -- the only two prior targets
(both EXQ-133 runs) are not `substrate_ceiling` under any reading. The driver conservatively
self-described 2 braking autopsies; the count is 0 and the brake was never armed.

**Granularity-debt trigger: does not fire.** 2 tagging targets across 1 file, alignment distribution
**intact=2**, no target reads `weakened` -> measurement/implementation debt.

## 10. Adjudication trail

- **Step 7b** mechanical pre-routing checks: **0 fires**, all five applicable.
- **Step 7c** adversarial red team: **CONTESTED**, three defects -- inverted causal direction, the inert
  clamp, and P2-measures-a-constant. **All three were independently re-verified by this session against
  the manifest cells and the as-ran source, and all three were adopted**; they changed the
  failure-location verdict and rewrote the successor spec. Every arithmetic claim in the pre-contest draft
  also reproduced. The science was never in dispute; the defects were in causal attribution and routing.
- **Step 8** interactive gate: user confirmed adoption of all three contests and the land-and-flag
  handling of the in-flight 944a collision, and asked the harm-trace question answered in section 6.
- **Step 9b** frozen hypothesis ledger: **nothing owed** -- no registry question references MECH-091, this
  autopsy emits no `fanout_recommendation` (it routes to one unambiguous repair), and it resolves no
  pre-registered leg. The registry was **not** modified.

## 11. Minor hygiene

1. `mech091_phase_reset.py:50` says `U{K..3K}`; `DECOUPLE_MAX_K = 2` makes it `U{K..2K}` (3K is the pre-queue probe figure).
2. **Flat-vs-pack disagreement on a prior run** (pre-existing; the brake reads the pack, so it is unaffected): `v3_exq_133_..._20260329T032233Z` flat manifest carries `evidence_direction: weakens` while its `runs/<run_id>/manifest.json` carries `non_contributory`. Worth a governance data-hygiene pass.
3. MECH-091's `what_would_answer` carries SD-006 language contradicted by GFLAG-0037 (section 4).
4. `commit_entry` is throttled by beta saturation -- its site requires `not beta_gate.is_elevated` while `beta_elevated_frac` is 0.969-0.996 in all 15 cells -- which explains ~1 firing per episode against harm's 207-326. Recorded for the substrate entry's benefit, not as a new failure record.
