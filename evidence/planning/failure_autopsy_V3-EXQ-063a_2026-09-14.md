# Failure Autopsy: V3-EXQ-063a (ARC-029 commitment-mode confound)

- **Status:** `confirmed` -- Step 8 gate held with the user 2026-09-16 (account-handover walkthrough session; recorded 2026-09-16T12:08:10Z). See "Step 8 gate outcome" at the end. Originally staged headless: Status: AWAITING HUMAN CONFIRMATION. Written by a headless metaworker-dispatch session ...
(chip-20260910-gflag0148-arc029-commitment-confound-autopsy) with no live user to run the
Step 8 interactive gate. This is a draft — routing is not finalised. Confirm in an interactive
session or at the next `/governance` walk.

Generated: 2026-09-14T11:19:36Z
Provenance: GFLAG-0148 (`REE_assembly/evidence/planning/governance_flag_adjudication_20260909.md`
line 455; commissioned 2026-09-09/10 governance-flag-backlog adjudication).

## 1. Target

- `run_id`: `v3_exq_063a_arc029_committed_mode_harm_outcomes_rc_gate_20260602T172531Z_v3`
- `queue_id`: V3-EXQ-063a
- `claim_ids`: [ARC-029]
- Manifest status: **PASS** (5/5 criteria), `evidence_direction: "supports"`, `experiment_purpose: "evidence"`
- Supersedes: `v3_exq_063_arc029_committed_mode_harm_outcomes` (de-weighted 2026-06-02, stale substrate)
- Driver: `ree-v3/experiments/v3_exq_063a_arc029_committed_mode_harm_outcomes_rc_gate.py`

**Why this autopsy exists despite `experiment_purpose: "evidence"` + clean PASS** (normally
exempt): GFLAG-0148 explicitly commissioned a re-adjudication of a specific confound charge on
this run's internals — the same shape as GFLAG-0246's SD-024 case. Governance is not the venue
for adjudicating run-internal confounds; this skill is.

## 2. Pre-registered question (GFLAG-0148, verbatim)

> Does the ablation isolate commitment mode, or does it also remove whatever else the R-c gate
> controls -- and is a within-run committed/uncommitted contrast reachable AT ALL given
> n_uncommitted_active_stable = 0?

## 3. Facts

**Manifest metrics** (2-seed average; no per-seed breakdown survives — see recording gap below):

| Metric | Value |
|---|---|
| harm_gap_stable | 0.020515 |
| harm_gap_volatile | 0.010571 |
| gap_reduction_ratio | 0.515 |
| n_committed_active_stable | 1155.5 |
| n_uncommitted_active_stable | **0.0** |
| n_committed_ablated_stable | **0.0** |

**Recording-standard check** (`ree-v3/validate_recording.py`): missing `recording_schema`,
`substrate_hash`, `substrate_commit`, `machine_class`, `elapsed_seconds`, `config`, `seeds`. Run
pre-dates the Experimental Recording Standard (2026-07-12); no per-seed metrics recoverable —
this is recording-debt, not fixable by re-reading this run, only by a fresh recorded re-run.

**Dry-run check** (`check_dry_run_citations.py`): clean, 0 dry hits. **Autopsy coverage check**
(`check_autopsy_coverage.py`): no prior autopsy covers this run — AVAILABLE.

### 3a. Design, as documented

2x2 [gate_active / gate_ablated] x [stable / volatile]. Train one agent per seed on the standard
env until `agent.e3._running_variance` collapses below `commit_threshold` ("committed"). Then, for
each of 4 eval conditions:

- **gate_active**: nothing resets `_running_variance` during the eval episode.
- **gate_ablated**: before EVERY step's SELECT phase, the script forces
  `agent.e3._running_variance = commit_threshold + 0.1` and `agent.e3._committed_trajectory = None`.

### 3b. Code-confirmed mechanism (this autopsy's own trace, independent of the manifest)

**Finding 1 — occupancy is frozen, not measured.** The only setter of `_running_variance` outside
the script's own overrides is `E3Selector.update_running_variance()`
(`ree-v3/ree_core/predictors/e3_selector.py:840-882`), reachable in the whole codebase **only**
via `E3Selector.post_action_update()` (`e3_selector.py:4389-4432`) `<-` `REEAgent.update_residue()`
(`ree_core/agent.py:10686`). The driver's `_eval_condition()`
(script lines 305-395) never calls `agent.update_residue()` — only `agent.sense`,
`agent.clock.advance`, `agent._e1_tick`, `agent.generate_trajectories`, `agent.select_action`,
`env.step`. **So in the gate_active arm, `_running_variance` is set once per episode
(`train_variance`, script line 333) and never touched again** — it is frozen low by construction,
not dynamically re-evaluated and happening to stay low. Symmetrically, the gate_ablated arm is
frozen high by the per-tick override (script lines 342-344), applied *before* `select_action` runs
each step.

**Consequence**: `n_committed_active_stable=1155.5` / `n_uncommitted_active_stable=0.0` /
`n_committed_ablated_stable=0.0` are a **tautological readout of the two forced-constant regimes
the script installs**, not an emergent measurement of gate dynamics. C3 ("committed cond has more
committed than uncommitted steps") and C4 ("ablated cond has zero committed steps") **cannot fail
under this construction regardless of whether the R-c gate does anything at all** — both are
non-degeneracy checks that are vacuous by construction. **This directly answers the second half of
the pre-registered question: no, a within-run committed/uncommitted contrast is not reachable at
all under this design** — not because the gate failed to produce one, but because nothing in the
eval loop lets `_running_variance` move.

**Finding 2 — the R-c readiness gate itself is exercised every tick in one arm and never in the
other.** `config.heartbeat.beta_gate_bistable` is never set by this driver and defaults `False`
(`ree_core/utils/config.py:3296`), so `select_action()` runs the **non-bistable legacy branch**
(`ree_core/agent.py:9866`, `else:`), which re-evaluates on **every** E3 tick:
```
_legacy_admit = (should_admit_elevation(...) and _readiness_admits) if result.committed else True
```
(`agent.py:9866-9882`), where `result.committed` is computed live each tick from
`commit_variance = self._running_variance` (`e3_selector.py:3843`) and
`committed = commit_variance < effective_threshold` (`e3_selector.py:3847`).
`effective_threshold` is verified constant at `commitment_threshold=0.40` for this run — the
BreathOscillator sweep is disabled by default, `urgency_weight=0.0`, `goal_state=None`: none of
the `effective_threshold` modulators are armed by this driver.

- **gate_active**: `_running_variance` frozen below threshold every tick -> `result.committed=True`
  every tick -> `should_admit_elevation()` (the R-c gate under test) fires on **every E3 tick for
  the whole episode**.
- **gate_ablated**: `_running_variance` forced above threshold every tick *before* `select_action`
  runs -> `result.committed=False` every tick -> the ternary short-circuits to `True` **without
  ever calling `should_admit_elevation()`** — zero times, for the entire episode.

This directly answers the first half of the pre-registered question: the ablation does not just
fail to isolate "commitment mode" as a clean single variable — in this specific driver, it removes
the R-c readiness gate from the ablated arm's execution path entirely (zero calls), while exercising
it far more heavily than a single elevation event in the active arm (every tick, not "once at
commit entry", because the bistable latch that would confine it to entry events is off).

**Finding 3 (precision confound, corroborating claims.yaml's own pre-existing P2 analysis) —
`current_precision = 1.0 / (self._running_variance + 1e-6)` (`e3_selector.py:815-817`) is the same
scalar as `_running_variance`.** Forcing `_running_variance` to a fixed `commit_threshold + 0.1 =
0.50` (`commitment_threshold` default 0.40, `ree_core/utils/config.py:1107`) therefore also pins
`current_precision` at a fixed ~2.0 for the entire ablated-arm episode — an arbitrary operating
point unrelated to what the agent's organically-uncommitted precision would be. The
precision-consuming dual-system arbitration path (`_arbitrate_dual_system`, `e3_selector.py:1623`)
is gated on `use_dualsystem_arbitration` (default `False`, not set by this driver) and is **not**
exercised here — so in this specific run the precision confound is carried structurally (via the
shared scalar and the shared gate check above), not through that particular downstream consumer.
This is the same confound *class* the 2026-06-03 autopsy (`failure_autopsy_604a-624a-630`) found on
the across-tick nav_competence axis of the same claim (V3-EXQ-630, non_contributory) — now
confirmed on the within-tick decisiveness (R-c) axis too.

**What is NOT a confound**: the action-generation mechanism genuinely differs between committed
and uncommitted steps (`select_action` early-return, `agent.py:7237-7253`: committed steps replay
a stored multi-step plan; uncommitted/ablated steps repeat the last action). This is the intended,
in-architecture content of "commitment" per ARC-029's own definition — candidate *scoring* itself
(`e3.select()`) is unconditional on commit state on E3-tick steps, so this is not an extra
side-confound beyond the occupancy/precision issues above.

## 4. Claim-layer mapping

**ARC-029**: "Committed and uncommitted operating modes produce measurably distinct harm
outcomes." `status: provisional`, `epistemic_category: standard`, `depends_on: [ARC-016, MECH-090]`
— both healthy (ARC-016 `stable`, MECH-090 `active`; neither implicated by this confound).

Prior experimental record (per claims.yaml `evidence_quality_note`):
- EXQ-063 (2026-03-22) PASS — later de-weighted, stale substrate (pre-MECH-090 R-c landing).
- EXQ-125 (2026-03-29 to 2026-04-04) — 3 runs, but only **2 non-superseded**: FAIL/weakens
  (2026-03-29) and FAIL/mixed (2026-04-03); the 3rd run (2026-04-04, different seed set) carries
  `evidence_direction: superseded` in its own flat manifest and is inactive evidence.
- V3-EXQ-227 (2026-04-05) diagnostic — non_contributory (substrate-drift explanation for EXQ-063
  vs EXQ-125 discrepancy; SD-010/011/012 cut harm rates ~100x).
- V3-EXQ-630 (2026-06-02, autopsied 2026-06-03) — non_contributory (across-tick nav_competence
  axis; SD-022 limb-damage-degrade/running_variance confound — **the sibling of this autopsy's
  finding, on the other MECH-090 axis**).
- **V3-EXQ-063a (2026-06-02) PASS — the one under adjudication here.** Per claims.yaml's own
  `evidence_quality_note` (not `status_note`, which still cites the original superseded EXQ-063),
  this run is the **sole currently-cited positive EXPERIMENTAL support** keeping ARC-029 at
  `provisional` ("ARC-029 separately supported by V3-EXQ-063a PASS ... 2026-06-02"). Confirmed
  independently against `claim_evidence.v1.json`: `genuine_exp_direction_counts` =
  `{supports: 1 (063a), weakens: 1}` — 063a is the only genuine-experimental support. **6
  literature entries also exist** (`literature_confidence: 0.785`) and are unaffected by this
  autopsy — see §9's note on what this does and does not imply for the indexer's confidence math.

**claims.yaml already carries a complete non-degeneracy analysis (`what_would_answer`, written
2026-09-09 governance cycle, before this autopsy ran) that independently reaches the same P1
(occupancy-vacuous) and P2 (precision-confound) conclusions this autopsy's own code trace
confirms.** This autopsy adds: (a) independent code-level verification via the update-path trace
and the R-c gate call-site trace (Finding 1/2 above — not previously spelled out mechanically
anywhere in the corpus), and (b) the formal failure-autopsy disposition GFLAG-0148 required.

## 5. Biological-reference triage

Closest mechanism: BG-like commitment/action-selection lock-in (Cisek-Kalaska affordance
competition collapsing to one selected plan); Humphries (2012) dopaminergic
exploitation/exploration framing already cited in ARC-029's own notes (`lit_status: present`).
The defect here is **not** a biological-translation divergence in the gate mechanism — it is the
choice of **ablation vehicle** (forcing the shared confidence/precision scalar directly, rather
than manipulating the commit threshold upstream of it). Biology gives no reason to prefer the
chosen vehicle; MECH-108's BreathOscillator (`ree_core/heartbeat/clock.py`) already implements a
threshold-side driver for exactly this purpose and is unused by this design.

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (protected) | the design never let ARC-029's own within-agent two-mode contrast express itself |
| Biological reference | partial | mechanism class well-grounded; ablation-vehicle choice is the defect, not translation fidelity |
| Prerequisites | present | MECH-090 active, ARC-016 stable — neither implicated |
| Implementation | complete | the gate, the R-c predicate, and the threshold-side alternative levers (BreathOscillator, `use_natural_commit_latch_hold`, etc.) all already exist and are unused by this driver |
| Environment | adequate | stable/volatile split is a reasonable operationalisation |
| Measurement | misleading | C3/C4 are structurally unfalsifiable by this driver's own construction |
| Integration | isolated | cannot assess within-agent committed/uncommitted x volatility interaction — both states are pinned constant per episode |
| Scale/capacity | adequate | not implicated |

**Failure-location (GOV-FAILLOC-1):** mechanism = not_established (i.e. not the cause — mechanism
implementation reads complete), measures = established (the defect), environment =
not_established. `ree: false`. **Net classification: MEASURES** — the ablation instrument and its
own non-degeneracy check are the defect; not chargeable to the commitment mechanism or the
environment design.

**Granularity-debt recurrence trigger: does NOT fire.**
`granularity_debt_cluster.py ARC-029` (run 2026-09-14): 3 prior targets, alignment distribution
`unclear=3` — no target reads `weakened`. This target also reads `unclear (protected)`. Per the
skill's own rule ("only fire when at least one target reads weakened"), this is measurement/
test-design debt, not granularity debt.

**Re-derive brake: does NOT fire.** Count after this target = 1 (threshold 2). Prior ARC-029
targets (V3-EXQ-630, EXQ-125 x2) are excluded from the R1-R3 count by the instrument-match /
direction-mismatch branches. See `re_derive_brake` in the JSON for the caveat this raises about
the corpus's INSTRUMENT-substring exclusion no longer literal-matching the enum-compliant
`standard` category value.

## 7. Learning extracted

1. A same-scalar ablation (forcing a shared commitment/precision variable to a fixed value)
   cannot isolate "commitment mode" as a single variable — it necessarily also pins precision.
   Now confirmed on **both** MECH-090 axes (across-tick: V3-EXQ-630; within-tick/R-c: this run) —
   the confound is a property of ARC-029's whole ablation-vehicle choice, not one substrate axis.
2. A per-episode-constant ablation override applied before every SELECT step makes a C3/C4-style
   occupancy "non-degeneracy" check structurally unfalsifiable — it verifies the override was
   applied, not that the gate does anything. Future ablation designs for gated/latching mechanisms
   should manipulate a driver *upstream* of the gate (here: `effective_threshold` via MECH-108's
   BreathOscillator, already implemented) so the gate's own decision logic is genuinely exercised.
3. claims.yaml's own `what_would_answer` field for ARC-029 already specifies a complete,
   ready-to-queue redesign spec (P1-P3 + confirming/falsifying criteria) using existing REEConfig
   levers — route to that spec directly.
4. **The never-queued `v3_exq_125a_arc029_committed_mode_redesign.py` driver (found by the Step 7b
   C1 check) does NOT fix this confound** — it addresses EXQ-125's statistical-power defect only
   and reuses the identical `_running_variance`-forcing ablation vehicle verbatim. A future
   `/queue-experiment` session must not queue it unmodified.

## 8. Routing

**`/queue-experiment`** — NOT a re-queue of the existing `v3_exq_125a` driver as-is (see §7.4).
A new redesign (or substantial amend of 125a) satisfying claims.yaml's ARC-029 `what_would_answer`:

- **P1** (occupancy): arm `use_natural_commit_latch_hold` (+ macro-program flags if applicable) so
  a single alternating-arm run sustains `committed_step_fraction` in [0.15, 0.85] with mean
  committed-run length >= 3 ticks on >= 4/5 seeds.
- **P2** (precision-invariance): drive the mode transition via MECH-108's BreathOscillator
  `effective_threshold` sweep (`clock.py:20-31`), leaving `_running_variance` and
  `current_precision` untouched by the manipulation itself — gate on `current_precision`
  distribution being statistically indistinguishable between the alternating arm and a static
  control.
- **P3** (harm DV off the floor): 063a's ~-0.055 harm/step is a demonstrated workable operating
  point — a calibration requirement already met, not an open problem.

## 9. Recommended `evidence_quality_note` (draft; governance writes it)

See `recommended_evidence_quality_note` in the JSON artifact — full text, ends with the concrete
claims-registry consequence: with 063a re-tagged, ARC-029's **genuine experimental record** has
zero surviving supports and should demote `provisional -> candidate` (recommendation only; this
skill does not edit claims.yaml).

**Caveat surfaced by the red-team pass (H1), incorporated above:** 6 literature entries
(`literature_confidence: 0.785`) remain and are untouched by this autopsy, so `overall_confidence`
will not collapse to zero and the indexer's own mechanical `conflict_ratio`-based demotion
threshold (`build_experiment_indexes.py`, needs `conflict_ratio >= 0.55`) will very likely **not**
fire automatically once 063a is re-tagged (estimated ratio ~0.14). **The demotion recommended here
is a governance judgment call on the experimental record specifically** — mirroring how this claim
was originally promoted `candidate -> provisional` on experimental grounds per its own
`status_note` — not something that follows mechanically from the indexer's confidence formula.
Say so explicitly when applying it.

## 10. Adversarial red-team pass (Step 7c)

**Verdict: CONFIRMED.** Run on `claude-fable-5-1` (cross-model from this drafting session,
`claude-sonnet-5`), independently, with the reasoning above withheld until after its own trace.

- Recomputed `harm_gap_stable`, `gap_reduction_ratio`, and the `commit_threshold + 0.1 = 0.50`
  arithmetic directly from the manifest/config — all matched.
- All five central claims (A: occupancy frozen; B: R-c gate every-tick-vs-never; C: precision
  confound; D: the 125a driver does not fix it; E: routing/demotion) were independently traced and
  **ACCEPTED**, with one basis correction on (E) — the "zero surviving support" framing, now fixed
  above (§9 caveat, and in the JSON's `recommended_evidence_quality_note` / `per_claim_recommendation`).
- Hygiene findings incorporated: two stale line citations (`e3_selector.py` 3838-3841 → 3843/3847;
  `agent.py` 9865 → 9866, both corrected throughout this document and the JSON); the "EXQ-125 x3"
  count corrected to 2 non-superseded runs (§4); the `evidence_quality_note` vs `status_note`
  attribution corrected (§4).
- Full disposition record: `red_team` block in the JSON artifact.

## 11. Governance-flag disposition

This autopsy is the discharge condition GFLAG-0148 names ("No governance edit discharges this. Run
`/failure-autopsy`..."). Once this artifact lands, GFLAG-0148 resolves via
`scripts/governance_flag.py resolve` citing this file — the claims.yaml status change itself is a
separate, follow-on governance action (subject to GOV-APPLY-1 tracking via `per_claim_recommendation`).

## Step 8 gate outcome -- CONFIRMED 2026-09-16T12:08:10Z

CONFIRMED INCLUDING THE DEMOTION: 063a's PASS re-tagged non_contributory (negative control failed: same-scalar ablation cannot isolate commitment mode; per-episode-constant override makes the occupancy non-degeneracy check vacuous), category standard, ARC-029 provisional -> candidate (063a was the sole surviving positive experimental support); routing queue-experiment (a design varying commitment mode within episode; governance chips it).
