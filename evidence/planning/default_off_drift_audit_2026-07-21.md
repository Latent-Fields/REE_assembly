# Default-off drift audit — claims registry vs `REEConfig` defaults

**Session:** `reverent-lamport-d18a32`
**Date:** 2026-07-21T23:47:52Z
**Scope:** `ree-v3/ree_core/utils/config.py` (default-off knobs) x `REE_assembly/docs/claims/claims.yaml` (status `stable` / `active` / `provisional` / `implemented`)
**Prompted by:** the SD-020 exemplar verified 2026-07-21 by session `confident-pare-9273f1`, written up in `evidence/planning/thought_intake_2026-06-10_z_harm_a_saturation_decoupling.md`.

## What "default-off drift" means here

A claim whose registered `status` implies the mechanism is settled architecture, but whose implementing
mechanism sits behind a config knob that defaults to `False`/`0`, so **no default-configured agent
exercises it**. The hazard is not that the knob exists — it is that the registry reading and the
substrate reading diverge, and the registry reading is what gets cited in governance and in any V3
closure account.

**This is orthogonal to `design_implementation_audit_2026-07-09.md` and its
`tests/test_flag_inertness.py` harness.** That audit asks *"the flag is ON — does the mechanism
actually do anything?"* (inertness, F-C1..F-P6). This one asks *"is the flag ever ON at all, and does
the claim's status admit that it isn't?"* The two intersect in exactly one place, noted at ARC-004
below, and that intersection is the worst cell in the matrix.

## Method

1. Parsed `config.py` lines 78–4660 (the dataclass field region; the `from_dims` block at 4780+ mirrors
   the same names and was excluded to avoid double-counting). Found **288** `bool`/numeric fields
   defaulting to `False`/`0`/`0.0`; **202** carry a claim id in their preceding comment block.
2. Joined knob → claim on those comment-block ids, keeping claims at status
   `stable` / `active` / `provisional` / `implemented` → **63 candidate claim/knob pairs**.
3. For each knob, counted how many files under `ree-v3/experiments/` and `ree-v3/tests/` ever set it
   `= True`. **This enablement count is the load-bearing discriminator** — it operationalises "nothing
   since turns it on" directly, rather than inferring it from claim prose.
4. Read the evidence run named in each claim's `live_status.evidence.from` and checked whether that
   run actually exercised the knob.

Step 4 is where the audit earns its keep: **several PASS-verdict runs never touched the knob their
claim is now filed under.** That is a sharper failure than the prompt anticipated, and it is described
per-claim below.

## (c) — the real drift list

Ranked by severity. `exp/test` = number of files under `experiments/` and `tests/` that set the knob `True`.

### Tier 1 — settled-architecture status, mechanism effectively never run

| # | Claim | Status | Knob (file:line) | exp/test | Evidence run |
|---|-------|--------|------------------|----------|--------------|
| 1 | **SD-020** | `stable` | `harm_surprise_pe_enabled` — [config.py:2306](../../../ree-v3/ree_core/utils/config.py) | **1 / 0** | `v3_exq_324b_sd020_harm_surprise_pe_20260419T045630Z_v3` (`supports/PASS`) |

The exemplar, and worse than recorded. The **only** experiment that ever sets
`harm_surprise_pe_enabled=True` is `v3_exq_324_sd020_harm_surprise_pe.py` — the **superseded**
predecessor. The run SD-020's `live_status` actually cites, **324b**, never references the flag: it
trains the affective encoder in a script-local loop (`v3_exq_324b_...py:212-222`,
`if pe_enabled: target_val = harm_pe`), bypassing `compute_harm_accum_loss`
([agent.py:8598](../../../ree-v3/ree_core/agent.py), PE branch at 8641-8642) and the substrate flag
entirely. So SD-020 is `stable` on evidence from a **script-local prototype of the mechanism, not the
substrate path** — flipping the flag today would not reproduce the validated configuration, it would
exercise a code path no PASS run has ever covered. Meanwhile the default agent trains `z_harm_a`
against the EMA accumulated-harm target SD-020 argues against, and V3-EXQ-664's affective saturation
is the predicted consequence.

| # | Claim | Status | Knob (file:line) | exp/test | Evidence run |
|---|-------|--------|------------------|----------|--------------|
| 2 | **SD-032e** | `stable` | `use_pacc_analog` — config.py:2580<br>`pacc_offline_decay` — config.py:2602 | 2 / 3<br>**0 / 0** | `v3_exq_453_mech261_write_gate_landing_20260420T062156Z_v3` (`diagnostic/PASS`) |

The pACC write-back is the claim's whole content ("the write-back channel that slowly updates the
baseline itself"). Its validating check is UC5, explicitly framed *"With pACC enabled"* — i.e. the
non-default arm. Two experiments in the entire corpus enable it, and the decay constant that governs
the "longer timescales than a single action cycle" behaviour is never set anywhere.

| # | Claim | Status | Knob (file:line) | exp/test | Evidence run |
|---|-------|--------|------------------|----------|--------------|
| 3 | **SD-006** | `implemented` | `use_backward_credit_sweep` — config.py:1955 | **0 / 1** | *(no `live_status.evidence` at all)* |

Status literally reads `implemented`. **No experiment has ever enabled it** — the sole experiment
reference (`v3_exq_490k_mech295_modulatory_sufficiency.py:235`) sets it to `False`. One contract test
(`test_mech_293_ghost_probes.py:473`) turns it on as a gate for an unrelated assertion. There is no
evidence record on the claim whatsoever.

| # | Claim | Status | Knob (file:line) | exp/test | Evidence run |
|---|-------|--------|------------------|----------|--------------|
| 4 | **MECH-089** | `active` | `use_multi_content_theta_packet` — config.py:2193 | **0 / 2** | `decision:MECH-089@2026-03-19` (`promote_to_provisional/applied`) |

Zero experiments. The only exercise is its own contract file, whose C1 is *"default-OFF no-op /
bit-identical"* — the test suite's own statement that the default agent does not run this. Note also
the status/decision mismatch: the recorded decision promoted it to `provisional`, but the registry
now reads `active`.

### Tier 2 — `stable`, PASS evidence, but the validated path is not the default path

| # | Claim | Status | Knob (file:line) | exp/test | Evidence run |
|---|-------|--------|------------------|----------|--------------|
| 5 | **MECH-259** | `stable` | `use_pcc_analog` — config.py:2549<br>(`use_aic_analog` :2508) | 3 / 3<br>7 / 4 | `v3_exq_447_sd032d_pcc_stability_20260423T204632Z_v3` (`supports/PASS`) |

Clean flag-on evidence — 447 sets `use_pcc_analog=True` and `use_salience_coordinator=True`
explicitly (lines 211-212) — and nothing since turns the PCC path on. This is the textbook (c) shape:
the switch-threshold claim is `stable` on a run whose configuration three experiments in the corpus
reproduce. (The coordinator itself is widely enabled at 56; the PCC-analog stability modulation that
MECH-259 names as governing the threshold is not.)

| # | Claim | Status | Knob (file:line) | exp/test | Evidence run |
|---|-------|--------|------------------|----------|--------------|
| 6 | **SD-035** | `stable` | `use_amygdala_analog` — config.py:3974<br>`override_pfc_eta_gain` — config.py:4143 | 11 / 3<br>**0 / 0** | `v3_exq_501_sd035_amygdala_analog_vs_binary_20260429T192730Z_v3` (`supports/PASS`) |

Same shape as SD-020, milder. `v3_exq_501` imports `BLAAnalog`/`CeAAnalog` directly and drives them
with synthetic `z_harm_a` vectors — it never constructs an agent, so `use_amygdala_analog` is not in
the causal path of the PASS. The claim is `stable` on **module-level unit validation**, and the
agent-integrated configuration it describes is exercised by 11 experiments and no default.

| # | Claim | Status | Knob (file:line) | exp/test | Evidence run |
|---|-------|--------|------------------|----------|--------------|
| 7 | **MECH-117** | `stable` | `goal_weight` — config.py:552<br>`benefit_terrain_enabled` — config.py:1980 | **0 / 0**<br>8 / 3 | `decision:MECH-117@2026-04-04` (`promote_to_stable/applied`) |

Promoted straight to `stable` by decision record, with no run in `live_status`. The wanting-side
scoring weight is never set anywhere in the corpus.

| # | Claim | Status | Knob (file:line) | exp/test | Evidence run |
|---|-------|--------|------------------|----------|--------------|
| 8 | **ARC-004** | `active` | `use_iterative_inference` — config.py:175 | 2 / 2 | *(no `live_status.evidence` at all)* |

**The worst cell in the matrix, because both audits fire on it.** Default-off *and* known-inert:
finding **F-C4** of `design_implementation_audit_2026-07-09.md` records that
`use_iterative_inference=True` at the default `inference_settle_iters=1` runs `range(0)` — a no-op
that also emits a NaN `final_rel_delta`. So ARC-004 is `active` on a mechanism that is off by
default, and that does nothing when turned on unless a second knob is also changed. No evidence
record.

### Tier 3 — `provisional`, same shape, lower governance weight

Included for completeness; these carry less citation risk but are the same defect.

| Claim | Status | Knob (file:line) | exp/test | Evidence run | Note |
|-------|--------|------------------|----------|--------------|------|
| **SD-019** | `provisional` | `harm_nonredundancy_weight` — config.py:2298 | **0 / 0** | `v3_exq_323a_sd019_harm_nonredundancy_20260416T172811Z_v3` (`supports/PASS`) | Genuine flag-on PASS (323a:126 sets it via config, `1.0` vs `0.0` arms). Nothing since. |
| **SD-022** | `provisional` | `harm_suffering_body_damage_weight` — config.py:3716 | **0 / 0** | `v3_exq_323a_...` (`supports/PASS`) | **Borrowed evidence**: cites SD-019's run, which never references this knob. Attribution defect as well as drift. |
| **MECH-045** / **ARC-006** | `provisional` | `use_object_file_buffer` — config.py:3787 | 1 / 1 | `v3_exq_658_mech045_object_file_persistence_...` (`supports/PASS`) | Clean two-arm (`ARM_INTACT` on / `ARM_ABLATION_OFF` off); the sole enabling experiment is its own. |
| **MECH-319** | `provisional` | `use_simulation_mode_rule_gate` — config.py:3871<br>`..._admit_writes` — :3880 | 3 / 1<br>**0 / 1** | `v3_exq_668_mech319_...` (`supports/PASS`) | Flag-on evidence (668:206-207). |
| **MECH-232** | `provisional` | `use_da_modulated_rbf_density` — config.py:2039 | 3 / 1 | `failure_autopsy_V3-EXQ-766a_2026-07-16` (`supports/verified`) | |
| **MECH-048** | `provisional` | `salience_use_stability_temperature` — config.py:2440 | 1 / 0 | *(none)* | |

## (a) — deliberate / documented holds, NOT drift

The registry already records the hold, so a governance reader is not misled. **Do not annotate these.**

- **ARC-007, ARC-018, Q-007, MECH-059, MECH-267** — `live_status.evidence.verdict` is literally
  `hold_pending_v3_substrate/applied` or `hold_candidate_resolve_conflict/applied`. ARC-007, ARC-018
  and Q-007 are also on the V3-Pending Gate list in `CLAUDE.md`. The `active` status is doing
  different work here: it marks a live *question*, not a live *mechanism*.
- **`use_differentiable_cem`** (config.py:1768, backing ARC-007 and part of SD-016) — 0 experiments,
  0 tests, but this is deliberate and self-documenting: at least four experiment manifests record
  `"use_differentiable_cem": "NOT FLIPPED (default False; SD-055 safety note)"`. An explicitly held
  knob with the reason carried in the artifacts is the system working, not drifting.

## (b) — superseded by a different effective default, NOT evidence-invalidating

These knobs default off in `REEConfig()` but are turned on by **essentially every experiment**, so the
claim's evidence base is sound and the mechanism is genuinely exercised. The config default is a
backward-compatibility artifact, not a statement about the architecture.

| Knob | exp/test | Claims at in-scope status |
|------|----------|---------------------------|
| `use_harm_stream` (:86) | **382** / 5 | SD-010 `implemented`, ARC-027 `active` |
| `use_affective_harm_stream` (:97) | **353** / 8 | SD-011 `stable`, SD-010 `implemented` |
| `use_resource_proximity_head` (:142) | **249** / 2 | SD-018 `implemented`, SD-009 `provisional` |
| `use_per_stream_vs` (:1781) | 126 / 5 | SD-007 `implemented`, MECH-101 `provisional` |
| `use_lateral_pfc_analog` (:2687) | 127 / 8 | MECH-261 `stable` |
| `use_dacc` (:2363) | 123 / 12 | SD-032a `stable` |
| `use_e3_score_diversity` (:3187) | 76 / 1 | MECH-314a, MECH-341 `provisional` |
| `sws_enabled` (:2257) / `use_sleep_loop` (:4191) | 39 / 29 | SD-017 `stable` |
| `use_event_classifier` (:134) | 34 / 0 | MECH-100 `stable`, SD-009 `provisional` |

One more (b), of a different kind — **mis-attributed knob**:

- **MECH-104** (`active`, evidence `v3_exq_365_mech104_surprise_gate_pair_...`, `supports/PASS`).
  `use_phasic_burst` (config.py:2932, 2 exps) carries MECH-104 in its comment, but 365 does not
  reference it: the experiment manipulates `_ema_alpha` on the running-variance path, which is **on by
  default**. The claimed mechanism is exercised by default; the knob is context in a comment, not the
  implementer. No action needed beyond not counting it as drift.

**(b) is benign for evidence validity but is still a documentation hazard.** "No default-configured
agent exercises the harm stream" is *literally true* of `REEConfig()`. A V3 closure account that
describes the dual nociceptive stream as settled architecture is describing the experiment harness's
effective default, not the substrate's declared one. That is worth one sentence somewhere, but it is
not a claims-registry defect and should not be fixed by touching claim status.

## Proposed follow-up (NOT applied in this session)

`claims.yaml` was held by session `stoic-blackwell-756d3a` throughout this audit, and per the task
brief nothing here was applied unilaterally. Two options, in preference order:

1. **A `default_off` annotation on the claim** — a small block recording the knob, its
   `file:line`, and the evidence run's enablement status. Example for SD-020:

   ```yaml
   default_off:
     knob: harm_surprise_pe_enabled
     location: ree-v3/ree_core/utils/config.py:2306
     evidence_run_enabled_knob: false   # 324b trains the PE target script-locally
     note: >
       Default agents train z_harm_a against the EMA accumulated-harm target
       this claim argues against. Status `stable` describes the flag-on
       configuration only.
   ```

   This is machine-checkable, which matters more than the prose: a small script could regenerate the
   enablement counts in this report and fail when a claim at `stable` acquires a zero-enablement knob.
   That converts a one-off audit into a standing guard, in the same spirit as
   `test_flag_inertness.py::test_flag_registry_is_current`.

2. **A `live_status` scope note** — cheaper, no schema change, e.g.
   `reading: stable (flag-on configuration only; default agents run the EMA target)`. Weaker, because
   free text does not survive a grep-driven closure account as reliably as a field.

Either way the **status values themselves should not be demoted on the strength of this audit alone**.
Tier 1 and Tier 2 claims are not necessarily *wrong* — SD-020's PASS is a real result about a real
mechanism. What is wrong is that the registry does not record that the result is about a
configuration nobody runs. Demotion is a governance decision on separate evidence; annotation is the
fix for the ambiguity this audit found.

Third item, separable and cheap: **SD-022's borrowed evidence pointer** (it cites SD-019's run, which
never exercised SD-022's knob) is an attribution error independent of the drift question and can be
corrected on its own.

## Reproducing this

The enablement counts are the part worth re-running as the corpus grows:

```bash
cd /Users/dgolden/REE_Working/ree-v3
grep -rlE "use_pacc_analog[\"']?[[:space:]]*[:=][[:space:]]*True" experiments/ | wc -l
```

Claim→knob attribution came from claim ids in `config.py` field comments; that mapping is only as good
as the comments, and MECH-104 above is a worked example of it producing a false positive. Any
automated guard built on this should treat a comment-derived pairing as a candidate to verify against
the evidence run, not as ground truth.
