# REE Design & Implementation Audit — 2026-07-09

**Scope:** Full-stack review across `ree-v3` (substrate + coordinator + experiments), `REE_assembly` (governance pipeline + claims registry). Six parallel static audits, findings cross-checked against source and wiring; two registry findings independently re-verified in this session. No runtime execution — all findings are static + wiring review unless noted.

**Coverage:** ~56K LOC V3 substrate, ~13K LOC coordinator, ~6K LOC runner/protocol, the ~5.6K-line evidence indexer, the 48K-line claims registry, shared experiment helpers + the ~19 most-recent live experiment scripts. Older experiment corpus (pre-EXQ-700), `agent.py` full orchestration, and `e3_selector.py` internals were sampled, not exhaustively traced (see Coverage §).

---

## 1. Headline: the dominant failure mode

The single most consequential pattern — appearing **independently** in the cognition core, the control plane, and (in a different guise) the governance pipeline — is:

> **A config-gated mechanism is silently inert or silently wrong. It does not crash. When an experiment enables the flag to test the mechanism, it measures the wrong thing and returns a plausible-looking null — which then weights claim confidence as if it were a real negative result.**

This is worse than a crash. A crash gets caught and re-queued. A silent false-null looks like clean evidence, flows through the indexer, and can hold or demote a claim on the basis of a mechanism that never actually ran. At least **9 distinct instances** were found (F-C1, F-C2, F-C3, F-C4, F-C7, F-P1, F-P2, F-P3, F-P6 below). None affect default runs (all sit behind default-`False` switches), so they are invisible unless someone audits the enabled arm.

**Two systemic root-causes feed this pattern and are worth fixing structurally, not just instance-by-instance:**

- **No "flag-enabled but inert" self-check.** Nothing asserts that turning a flag on actually changes behaviour. Several flags are dead by construction (uniform scalar shift on an argmin; loss-multiplier under Adam; `range(settle_iters-1)` with default 1; a dead switch whose branches are byte-identical).
- **Copy-paste of methodology instead of shared helpers.** The correct SD-of-delta effect-size gate exists *inline* in the 680 lineage but was never extracted, so the live 700–725 falsifier lineage re-implements a bare fixed margin. Same shape as the inverted-U logic living in one module and being defeated by an aggregation line.

---

## 2. Priority triage

| ID | Finding | Area | Severity | Effort |
|----|---------|------|----------|--------|
| **P0-1** | Coordinator `/result`: crash between DB row and spool write permanently loses a manifest from origin; client retry can't recover | Infra | High / data-loss | S |
| **P0-2** | PFC escape-affordance learner truncates its state vector (update-order vs frozen `_state_dim`) → corrupts a live experimental arm into a false negative | Substrate | High / training | S–M |
| **P0-3** | Governance: a claim being **unanimously refuted** never triggers demotion and never appears in the conflicts report (conflict_ratio=0 for unanimous evidence is the only demotion trigger) | Governance | High / scoring | S |
| **P0-4** | CLAUDE.md "V3-Pending Gate" held-claims list is stale AND off by ~218 (verified: 218 claims carry `v3_pending:true`; none of the 6 named do; 2 are explicitly `false`) | Registry | High / stale-gate | S |
| **P1-5** | Effect-size PASS gates use a bare fixed nat margin (no SD-of-delta scaling); the correct impl exists only inline in the 680 lineage, never extracted to a shared helper | Methodology | High (systemic) | M |
| **P1-6** | `dacc_foraging_weight` is dead-by-construction on the E3 path (uniform scalar shift is argmin-invariant) — re-introduces a pattern already deleted once as MECH-111 | Substrate | High / control-flow | S |
| **P1-7** | Lit-consistency uses the direction-blind `abs()` formula already fixed on the experimental side → literature that *refutes* a claim reads as literature *support* | Governance | Med-High / scoring | S |
| **P1-8** | 22–24 claim blocks have duplicate YAML keys; `safe_load` keeps the last, silently dropping values (incl. MECH-033's governance-critical superseded-evidence note) | Registry | Med-High / integrity | S |
| **P1-9** | MECH-074a BLA encoding-gain pinned to `gmax` on every above-threshold tick → documented inverted-U collapses to a step function; falling arm is dead code | Substrate | High (if enabled) | S |
| **P1-10** | 4 substrate-blocked claims (MECH-088/178/179/191) carry no machine-readable block marker → promotable with no guard | Registry | Med-High / integrity | S |
| **P1-11** | `commitment_closure:GAP-4` re-presents an already-built + validated substrate (`use_closure_commit_entry`, 460o/p PASS) as "under active build" | Docs | High / stale | S |
| **P2** | dACC saturation never fed live; iterative-inference no-op+NaN; PAG freeze can't sustain; blocked-agency streak; lit bypasses exclusion gates; conflict-ratio gate uses the "spurious" count; n=3 seed power; missing clamps; ghost double-scoring; inert learn-rate knobs; stale conversion-ceiling trackers | Mixed | Med–Low | Varies |

Effort: S = <1 day, M = a few days.

---

## 3. Findings by area

### 3A. V3 substrate — cognition core

**F-C1 (High, training-bug) — Escape-affordance learner corrupts its state vector.**
`ree_core/pfc/trainable_escape_affordance_learner.py:244-245` truncates state to a frozen `_state_dim`; update ordering in `agent.py:3669` (learner) precedes `:3720` (linker), the reverse of the contract asserted at `agent.py:2450-2451`. With both `use_trainable_escape_affordance_learner` and `use_e2_escape_linker_for_relief_safety` on, the learner freezes its width *before* the linker's 32-d slot exists; once the linker builds, every state vector is truncated — deleting `[z_norm, threat_scale]` and 30/32 linker dims and mis-slotting the rest. Both training and live-control (`compute_approach_bias`, `agent.py:6459`) consume the scrambled vector. The arm reads as a clean negative.
- *Options:* (a) swap the two `update()` blocks so linker updates first; (b) build the learner at fixed width with a reserved zero-filled linker slot; (c) make `_coerce_state_vector` assert on size change instead of truncating; (d) fix the false docstring.

**F-C2 (High, control-flow) — `dacc_foraging_weight` dead-by-construction on E3.**
`cingulate/dacc.py:521-523`: `bias = bias + dacc_foraging_weight * fv` where `fv` is a scalar → adds the same constant to every candidate. E3 selection (`argmin`/`softmax(-cost)`) and variance-space commitment are invariant to a uniform additive shift. The codebase already deleted an identical MECH-111 broadcast (`e3_selector.py:934`, "dead-by-construction"). An ablation enabling only the foraging term is byte-identical to OFF → false "foraging has no effect." (Signal still acts via `SalienceCoordinator`; only the adapter→E3 leg is inert.)
- *Options:* route foraging into a genuine absolute lever (commit threshold / softmax temperature), or delete the adapter branch + fix docs.

**F-C3 (Med-High, missing-wiring) — MECH-268 dACC conflict-saturation never fed live.**
`cingulate/dacc.py:203-249` reads `_outcome_history`, populated only by `record_outcome(...)` — which has **zero callers in `ree_core/`** (grep-confirmed; only `reset_outcome_history` is wired, into the closure path). With `dacc_saturation_enabled=True`, saturation is always 1.0; habituation/rumination attenuation never fires. Experiment `v3_exq_463b:278` manually calls `record_outcome` each step to compensate — confirming live-path population was intended but omitted.
- *Options:* call `self.dacc.record_outcome(...)` each waking tick near the `dacc(...)` call; or document config as experiment-only and drop the misleading reset hook.

**F-C4 (Med, off-by-one→NaN) — `use_iterative_inference` inert at default `settle_iters=1`.**
`latent/stack.py:1300-1336`: `for _ in range(settle_iters - 1)` = `range(0)` when default `inference_settle_iters=1` (`config.py:179`) → latents never re-settle (== OFF), and MECH-423 R2 readout emits `final_rel_delta=NaN`, `converged=False`. An experiment enabling the flag to measure convergence, without also raising `settle_iters`, gets a NaN-poisoned false negative.
- *Options:* raise/set-default when flag-on but `settle_iters<2`; or bump default to a real value and document `settle_iters=1 == OFF`.

**F-C5 (Med) — CrossStreamBinder projections never frozen; coupling not detached.** `latent/cross_stream_binder.py:123-166`. The "byte-identical fixed field" and "no gradient leak to E1/E2" guarantees rest on caller discipline only (no `requires_grad_(False)`, no `no_grad`/detach on the coupling read in `e2_fast.py:729,738`). Does not fire in current 720/725 configs (no optimizer over E2, no rollout backprop) but is structurally unguarded. *Options:* `requires_grad_(False)` in `__init__` when not learned; detach fixed-mode `factor()` inputs; wrap coupling read in `no_grad`.

**F-C6 (Med, wasted-compute) — Ghost-mix eviction scores every trajectory twice.** `hippocampal/module.py:1386-1391` calls `_score_trajectory` (a real residue-field forward pass) in both the guard and the ternary → `2×len(value_flat)` evaluations per tick on the default-on MECH-293 path. Result correct, cost doubled. *Options:* bind the score once.

**F-C7 (Med, training-config) — `escape_*_learn_rate` knobs inert under Adam.** `e2_escape_affordance_linker.py:494` multiplies loss by `learn_rate` before an AdamW step (Adam normalises it out); learner's `relief_/safety_learn_rate` act as loss weights, not rates, and are inert when equal (default 0.1/0.1). Sweeping them expecting learning-speed effects yields nothing; manifests report a "learn rate" that isn't one. *Options:* fold into `optimizer_lr` and drop the multiplier, or rename to `*_loss_weight`.

**F-C8 (Med, validity) — SD-063 conditional-precision gate compares mismatched scales.** `predictors/e3_selector.py:2678`: `commit_variance` (conditional predictive variance, `(IQR/2.5631)^2` over z_world) is compared against `effective_threshold` calibrated for the E2 prediction-error EMA — a different quantity/scale. Flipping the flag can systematically over/under-commit from scale alone, confounding V3-EXQ-716. Off by default. *Options:* recalibrate threshold for the conditional-variance scale, or normalise both to a common scale; note in the 716 protocol.

**Low (cognition):** CEM refit `ao_std` NaN on single survivor (`module.py:1103`, `unbiased=True` over 1 elem); `goal_proximity=None` → full ghost suppression (`persistence_appraisal_compute.py:63`); E2-linker fallback dim mismatch silently padded (`e2_escape_affordance_linker.py:309`); bridge "per-tick" leak only under threat (`escape_affordance_bridge.py:308`); per-axis drive skips `[0,1]` clamp (`pcc_analog.py:214`, `aic_analog.py:212`, `salience_coordinator.py:369`); stuck-detector metric vs header mismatch; `ThetaBuffer.summary()` batch-1 on empty; shuffled-control degeneracy at short history; `TPJComparator.compute_agency_loss` unbounded (currently uncalled); diagnostic softmax temps unclamped.

### 3B. V3 substrate — control plane

**F-P1 (High if enabled, sign/mechanism) — MECH-074a BLA encoding-gain pinned to `gmax`.**
`amygdala/bla.py:355-356,399-400`: `_window_onset_step` is reset to `now` on *every* above-threshold tick, so `elapsed` is always 0, `window_decay = 0.5**0 = 1.0`, and `window_tail = gmax`. The final `max(immediate_gain, window_tail)` therefore returns `gmax` (2.5) for every above-threshold arousal — the computed inverted-U (rising/falling arms) is dead code. Encoding gain becomes a step function, not the documented inverted-U. Trips MECH-074a's own falsification signature: a panic-level write that should be poorly consolidated gets full boost.
- *Options:* (a) gate `window_tail` to contribute only when `z_norm < thr` (the code comment already states this intent); (b) store achieved peak at onset and decay from that, not hard-coded `gmax`.

**F-P2 (Med, High if relied on) — PAG freeze gate commits then releases next tick.**
`pag/freeze_gate.py:236-253`: entry compares an accumulated product `z * duration` to `theta_freeze`; exit compares instantaneous `z` to `~theta_freeze * override * tone`. Freeze commits at low instantaneous `z` (compensated by duration) but can't stay frozen because instantaneous `z` never exceeded the exit threshold. With default `min_freeze_duration=0`, freeze releases the tick after commit and cycles — contradicting the module's "committed sustained immobility" premise.
- *Options:* compare exit on the same instantaneous scale that fed the accumulator; and/or set a non-zero default `min_freeze_duration`.

**F-P3 (Med, control-loop) — Blocked-agency "consecutive" streak not reset mid-block.**
`affect/blocked_agency.py:268-275`: no branch for `external_block AND z_block_assert < decommit_bound`. When the block persists but the assert dips below bound, the streak is left unchanged instead of reset, so non-consecutive above-bound ticks fire a decommit the contract says requires N *consecutive* ticks — releasing the commitment early.
- *Options:* change `elif not external_block:` to a plain `else:` so any failing tick resets the streak.

**Low (control plane):** BLA `override_encoding_gain` has no ceiling clamp (`bla.py:408`, CeA's analog does re-clip); `mech295_liking_bridge.tick()` double-counts fire diagnostics (`:465-468`); `vs_rollout_gate.unknown_stream_passes` is a dead no-op (both branches identical, `:369-375`). Plus doc/impl mismatches (blocked-agency "EMA" is linear ramp; `broadcast_override` ~0.377 resting bias; `gabaergic_decay` half-life label; `conditioned_safety_store` sigmoid at 0).

**Verified clean (control plane):** sleep Bayesian aggregator, MEL consumer, cross-module consolidation, phase manager; `causal_grid_world` (nav_bias correctly absent, harm/benefit signs, clamps, 5-tuple `step()` return); beta-gate + closure-operator refractory bookkeeping; `goal.py`; residue field; CeA; serotonin; harm-suffering accumulator.

### 3C. Coordinator + runner infrastructure

**F-I1 (High, data-loss) — `/result` spool write gated behind `fresh`.**
`coordinator/app.py:602-621`: `fresh = db.record_result(...)` commits the DB row (auto-commit, `isolation_level=None`) *before* `if fresh: manifest_spool.write_manifest(...)`. A crash / disk-full / `OSError` between the row insert and the spool write leaves a `results` row (blocking recovery) with no spool bytes → `phase3_git_writer` never commits it → `committed_at` stays NULL forever. A client re-POST hits idempotency (`db.py:413`) → `fresh=False` → skips `write_manifest`, so retry can't fix it. The runner reports once with no retry (`experiment_runner.py:930`). The `manifest_spool.py:77-82` "acceptable, runner still has it" comment is **stale under Phase-3-live** — `PHASE3_DISABLE_RUNNER_RESULT_PUSH=1` makes the spool the sole route to origin. No test exercises the `if fresh` gate with a pre-existing row.
- *Options:* (a) spool **before** `record_result` (write is atomic tmp+rename, idempotent); (b) re-spool when `fresh=False` and the spool entry is missing; (c) `phase3_git_writer` reconciles NULL-`committed_at` rows with no spool entry into a loud WARN.

**F-I2 (Low, db-integrity) — `record_result` not wrapped in `BEGIN IMMEDIATE`.** `db.py:409-424` does a bare SELECT-then-INSERT with no transaction/`try`, unlike sibling helpers (`try_claim`/`release_claim`/`ack_command` all use `BEGIN IMMEDIATE`). Two simultaneous same-`run_id` POSTs under the threading server can both INSERT; the second raises uncaught `IntegrityError` → 500/reset instead of the designed idempotent no-op. *Options:* `BEGIN IMMEDIATE` or `INSERT OR IGNORE`, or catch `IntegrityError` and return `False`.

**F-I3 (Low, git) — heartbeat writer can strand its own unpushed commit.** `sync_daemon.py:2508-2524` skip-path returns before any "ahead>0 → push existing commit" branch that the result/queue writers have. With liveness interval at 86400, a rejected push can strand a commit up to 24h (drained opportunistically by the next result-writer HEAD push). Telemetry staleness only — acceptable by design, but an asymmetry trap. *Options:* mirror the other writers' ahead-check in the skip path, or comment the intended drain.

**Confirmed correctly in place (good news):** cloud-scaler hub-skip + HELD_BY_SELF + SIGTERM transient-exit-codes; phantom-completion synthesised ERROR manifest; queue-writer conflict self-heal (`PHASE3_QUEUE_CONFLICT_RECOVERY`); foreign-commit push guard; pathspec-drop structurally avoided (clean-tree precondition, no autostash in writer paths); stale-claim recovery respects fresh heartbeats; path-traversal defenses.

### 3D. Governance / claims indexing

**F-G1 (High, scoring) — Unanimous refutation never demotes and never reports.**
`build_experiment_indexes.py:2854-2872`: the only demotion trigger is `demote_on_conflict`, gated on `conflict_ratio >= 0.55`. But `_direction_conflict_ratio = 2*min(supports,weakens)/total` is **0 for unanimous evidence**. A stable claim accumulating consistent refutation (supports=0, weakens=N) has ratio 0 → never demoted, even as `exp_conf` collapses. `_collect_conflicts:3291` requires `supports>0 AND weakens>0`, so it also never appears in the conflicts report. The recommendation engine is blind exactly on the falsification case.
- *Options:* add a refutation-keyed demotion trigger (`net_direction = (supports-weakens)/directional < -T`, independent of conflict_ratio); add a `refutation_ratio` + distinct "falsified" recommendation; emit a "consistent_weakening" conflicts row.

**F-G2 (Med-High, scoring) — Lit consistency uses the direction-blind `abs()` formula.**
`build_experiment_indexes.py:1549`: literature uses `abs(supports-weakens)/directional` — the exact bug fixed on the experimental branch (`:1529-1534`, comment: "old formula gave abs(0-N)/N=1.0 regardless of direction"). Literature that unanimously *weakens* yields consistency 1.0 → inflated `lit_conf`; `_evidence_quadrant` never checks lit direction, so a refuted claim is labelled literature-*supported*.
- *Options:* mirror the experimental fix (`net=(s-w)/dir; consistency=(net+1)/2`); or make quadrant require lit majority==supports.

**F-G3 (Med, supersession) — Literature entries bypass every exclusion gate.** `:1863-1882` (comment admits it): lit entries are appended unconditionally — no `superseded`/`non_contributory`/`inconclusive`/stale filtering — and still count toward the `lit_entries>=2` promotion gate. A superseded/non-contributory lit record can help *promote* a claim. *Options:* apply the `scoring_excluded` filter to lit entries; at minimum exclude those directions from the promotion-gate count.

**F-G4 (Med, conflict-ratio) — Promote/demote gate uses the "spurious" conflict count.** `:2791-2792` computes the gate's conflict_ratio over *all* scored entries incl. non-genuine experimental, while the planning path (`:4121-4128`) deliberately rebuilds from `genuine_exp + lit` "because synthetic entries inflate conflict signals spuriously." The load-bearing gate is exposed to the inflation the codebase elsewhere guards against, and disagrees with the planning output for the same claim. *Options:* consume `genuine_exp+lit` in `_recommendation_for_claim`; or compute conflict_ratio once and store one field.

**Low (governance):** per-claim `superseded` direction is scored not excluded (`:1799` checks run-level only); block-scalar `evidence_quality_note` truncates on internal blank lines (`:1984`).

**Confirmed correct:** indexer scores the `runs/` pack copy with a guarded flat-override; run-level `superseded` and experimental `non_contributory`/`inconclusive` excluded; `does_not_support→weakens`; enum inline-comment parser is fixed; `governance.sh` is derive-only, no auto-promotion; experimental consistency is direction-aware; `arm_results` indexed by explicit keys (seed-major hazard N/A here).

### 3E. Experiment methodology

**F-M1 (High, systemic) — Fixed-margin effect-size gates, correct impl never extracted.**
The project standard (per its own 680b→680c autopsy) is `margin = max(k*SD(paired delta), floor)`. That is implemented **only inline** in the 680 superadditivity lineage (`v3_exq_680c:825-828`). The live conversion-falsifier lineage hard-codes a bare fixed 0.05-nat margin with no `k*SD(delta)` term: e.g. `v3_exq_714:237`, `713:155`, `705b/706b/707b/708/709/710/711`, `715a:247` (`DECOMMIT_MIN_DROP_FRAC=0.10`). Mitigated in practice by per-seed pairing + a same-layer noise control + majority-vote, so it runs conservative today — but a noisier future metric in the family can false-PASS, and these are `experiment_purpose="evidence"`. (Note: a raw grep flags ~126 scripts using a fixed margin, but that over-counts — many older scripts legitimately threshold *bounded* quantities and several 700-series scripts *also* carry an SD term for a different sub-metric. The actionable core is the un-extracted helper, not all 126.)
- *Options:* extract `_metrics.paired_delta_gate(deltas, k, floor)` returning `max(k*pstdev(deltas), floor)` + seed-pass count, and route the 700–725 lineage through it; keep the floor as the absolute-floor component and add the SD term via `max`; add a paired Wilcoxon across seeds.

**F-M2 (Low-Med, power) — n=3 seeds at a 2-of-3 gate on evidence-tier falsifiers.** `v3_exq_714:284`, `715a:163`, `705b/706b` use `SEEDS=[42,43,44]` with `MIN_SEEDS_FOR_PASS=2` — one seed's noise flips the verdict, compounding F-M1. Siblings are properly powered (713: 6, 717: 12, 725: 6). *Options:* raise evidence-tier falsifiers to ≥5–6 seeds; or mark 2/3 results provisional.

**Low (methodology):** 721 lag "distribution" percentiles computed over per-seed medians, degenerate at `n_measurable=1` (`:939`, gate allows 1); 706b leg-G magnitude-match ratio is ~1.0 by construction (logs target not realised range, `:462`).

**Verified clean:** `arm_fingerprint`/`arm_reuse` (refuse-by-default, `include_driver_script_in_hash=False` discriminator correct, content-hash over `ree_core/**` so a substrate change flips the hash — no false cache-HIT path found); `_harness` single-`sense()` invariant; ISO-8601 timestamps everywhere; seed pairing correct; no joint-when-phased; zero ASCII violations in sampled scripts; diagnostics frame `interpretation.label` as hypothesis with empty `claim_ids`.

### 3F. Claims registry ↔ substrate consistency

**F-R1 (High, stale-gate) — V3-Pending held-claims list stale + off by ~218.** *(re-verified this session)* CLAUDE.md names ARC-007/016/018, MECH-025/033, Q-007 as held; the registry shows **none** carry `v3_pending:true`, two are explicitly `false` with V3 evidence in, while **218 other claims** carry `v3_pending:true` (309 carry `implementation_phase:v3`). Any agent trusting the section mis-gates ~218 claims. *Options:* replace the hardcoded list with a pointer to the derived set; add a consistency assertion that fails on divergence.

**F-R2 (High, stale-doc) — `commitment_closure:GAP-4` re-presents built substrate as owed.** `evidence/planning/commitment_closure_plan.md:52-60` marks the P2 closure-commit-entry node `in-progress`/"under active build", frozen at 460l — but `use_closure_commit_entry` is implemented (`agent.py:1046`, `config.py:3206`) and validated (460o/p PASS 2026-06-24; de-commit falsifiers 715/715a/717 terminal 2026-07-07). A reader of GAP-4 alone rebuilds an existing substrate. *Options:* flip GAP-4 to validated, re-point owner to 460o/p, add the 715/717 record; cross-check GAP nodes against their campaign-plan root each governance pass.

**F-R3 (Med-High, integrity) — Duplicate YAML keys silently drop values in ~22–24 claim blocks.** *(re-verified this session; first at line 1839)* `safe_load` keeps the last of a repeated mapping key. For MECH-033 the *dropped* value is the governance-critical caveat "EXQ-124 evidence superseded 2026-05-08 … Awaiting StepHarness re-run" — invisible to any tool reading parsed YAML. Affected IDs include MECH-033/073/095, SD-005/034/036/037, ARC-041/060/068, MECH-118/135/204/220/266/269/279/295/320/436, Q-040. *Options:* add a duplicate-key linter (SafeLoader subclass raising on repeats) to the validator; manually merge the 22 blocks.

**F-R4 (Med-High, integrity) — 4 substrate-blocked claims carry no machine-readable marker.** MECH-088/178/179/191 are `status: candidate` with no `epistemic_category`, `v3_pending`, or `evidence_quality_note`; substrate genuinely absent (no DA/NA/ACh control-plane classes; no legibility channel). "Substrate-blocked" lives only in project memory, so governance can't gate. Two block-reason fixes while annotating: a REM analog *does* exist (`sleep/phase_manager.py` `SleepPhase.REM_ANALOG`), so MECH-178's blocker is solely the missing NA plane and MECH-179's is solely the missing error-type channel. *Options:* add `epistemic_category: substrate_ceiling` + a one-line note naming the missing plane to each.

**Med/Low (registry/docs):** conversion-ceiling phase0 tracker 19 days stale, its four-root taxonomy now incomplete vs the live competence gate V3-EXQ-724 (`conversion_ceiling_phase0_synthesis_2026-06-18.md`); ARC-062 `ceiling_routing_note` points at superseded 700b + a reversed V4 escape hatch (`claims.yaml:30294`); INV-050 substrate-block stale in *memory* only (registry correct — landed 2026-07-07); ad-hoc `evidence_direction` manifest values (`inconclusive_measurement`, `non_informative`) not in `NON_CONTRIBUTORY_DIRECTIONS` (`check_closure_drift.py:186`); `substrate_queue.json:4802` f_dominance status-label tail contradicts its own body.

**Verified clean:** no duplicate claim *IDs* (875 blocks); no dangling `depends_on`/`supersedes`; `invariant_type` schema valid (all emergent list `emergent_from`); ~14 high-value claim→substrate spot-checks all present; no queued experiment depends on absent substrate.

---

## 4. Recommended sequencing

**Do first (small, high-value, low-risk):**
1. **F-I1** — reorder the spool write before `record_result` (or spool unconditionally). Stops silent permanent data loss. Add a regression test through the `if fresh` gate.
2. **F-G1 + F-G2** — add the refutation demotion trigger and mirror the experimental consistency fix to the lit branch. ~15 lines each; closes a governance blind spot on falsification.
3. **F-R1, F-R3, F-R4** — regenerate the V3-Pending list (or replace with a derived pointer), add the duplicate-key linter to the validator, annotate the 4 substrate-blocked claims. All small, all reduce silent registry corruption. F-R3's linter prevents recurrence.
4. **F-R2, F-R11-class docs** — flip GAP-4 and the stale conversion-ceiling trackers; cheap, prevents a rebuild-what-exists waste.

**Do next (structural, prevents recurrence):**
5. **F-M1** — extract the SD-of-delta gate to `_metrics` and route the live lineage through it.
6. **Flag-inertness harness** — the highest-leverage structural fix. A small test/CI check that, for each `use_*` flag, asserts enabling it changes *some* observable output vs OFF on a smoke config. This single mechanism would have caught F-C2, F-C3, F-C4, F-C7, F-P1, F-P6 at once.
7. **F-C1, F-C2, F-P1** — the substrate bugs that actively corrupt an enabled experimental arm into a false null. Fix before any experiment that enables those arms weights governance. **Before fixing:** check whether any *already-reviewed* experiment ran these arms and fed a null into claim confidence — if so, those results need re-scoring (this intersects the "reviewed ≠ autopsy-applied" gap).

**Verify-impact pass (do alongside):** for F-C1/F-C2/F-C3/F-C4/F-P1, grep the experiment queue + evidence manifests for runs that enabled the affected flags. Any such run that is already `reviewed` and weighting a claim is a candidate for supersession/re-run. This is the concrete blast-radius question the audit can't answer statically.

---

## 5. Coverage & confidence

- **Static only.** No runtime execution; no experiment was re-run. Findings are source + wiring review. Instances gated behind default-`False` flags were confirmed by code order + logic, not by a live enabled run.
- **Not exhaustively audited:** `agent.py` full `select_action`/`sense` orchestration (484 KB — most likely place a *correct* primitive is wired with a wrong argument); `e3_selector.py` internals beyond the parity/Go-No-Go/commit/SD-063 sites; `candidate_rule_field.py`, `event_segmenter.py` BOCPD math; the ~1000 pre-EXQ-700 experiment scripts; the indexer's `_write_planning_outputs` proposal generator; serve.py/explorer parsing; systemd/WireGuard/auth config; semantic (vs presence) correctness of claim→code mappings.
- **What passed audit is real signal:** the coordinator's documented incident-fixes are genuinely in place; the sleep subsystem, arm-reuse fingerprinting, seed pairing, and the core env API are clean; the substrate's gradient-isolation discipline (detach/no_grad on stop-gradient boundaries) is correct where audited. The bugs cluster in *optional, recently-added, flag-gated* mechanisms — not in the load-bearing default path.

---

## 6. Blast-radius verdict (verified in-session)

For each substrate false-null finding, I searched the experiment corpus for runs that enabled the affected flag, then checked their outcome, `evidence_direction`, `claim_ids`, and whether they weight governance. **Headline: no claim rests on a clean false-positive from any of these bugs.** The worst cases are *over-claim / under-test*, not *false PASS*.

| Finding | Runs that enabled it | Contaminated claim? | Verdict |
|---------|----------------------|---------------------|---------|
| **F-C1** escape-learner truncation | **0** (no experiment sets either flag; 653 references but doesn't enable) | None | No live exposure. Guard before first use. |
| **F-C2** `dacc_foraging_weight` inert on E3 | 14 (SD-032 dACC family: 445*, 446, 453*, 455, 595, 597*) | Flat manifests carry **empty `claim_ids`**; salience path (primary route) intact | Low. E3-adapter leg inert but not the load-bearing route; no direct claim-id weight. |
| **F-C3** dACC saturation never fed live | 463b (PASS/supports MECH-268); 468b/c/d/e/f (all FAIL) | **463b self-compensates** — it manually calls `record_outcome` every step (`:278`); 468* are all `non_contributory` → excluded by the indexer | MECH-268 not over-credited. But saturation is validated only via **synthetic injection**; the live wiring is missing, so the mechanism has never fired in a real agent loop. |
| **F-C4** iterative-inference no-op + NaN | 676, 679 (MECH-423 readiness) | Both `experiment_purpose="diagnostic"` with **empty `claim_ids`** → weight nothing | No claim contamination. |
| **F-P1** BLA inverted-U → step function | **659** (PASS/supports/**evidence**/MECH-074a) | 659's PASS gate tests the **monotonic** "higher arousal → higher gain → preferential replay" (`AOR>0`, PRIMARY>ABLATION) — which the step-function **preserves** | **Partial.** The monotonic replay-bias PASS is robust to the bug. But the inverted-U **falling arm** (panic → poorer consolidation) is *untested by 659 and broken in code* (empirically confirmed below). MECH-074a is over-credited if its claim asserts the full inverted-U. Re-run 659 (or add a falling-arm arm) after the fix. |

**F-P1 empirically confirmed this session** (fresh `BLAAnalog`, default config): pre-fix, `encoding_gain` at arousal 0.0/0.3 = 1.0 (floor); at 0.4/0.7/1.0/2.0/4.0 = **2.5 (gmax) uniformly** — a pure step at the threshold, both arms absent.

**F-P1 FIXED this session** (`ree_core/amygdala/bla.py`): the post-event window now decays from the *achieved* peak gain and acts only as a below-threshold residual floor, so the instantaneous inverted-U governs above threshold. Post-fix trace: 1.0 (≤0.4) → **1.75 (0.55)** → **2.5 (peak 0.7)** → 1.0 (≥1.0) — rising and falling arms restored. All 32 BLA-relevant contract/preflight tests pass. **Follow-up owed:** re-run V3-EXQ-659 (its PASS survives, but the falling-arm claim is now demonstrable) and clear MECH-074a's inverted-U caveat once it does.

**Two governance follow-ups this surfaces (not code bugs, but claim-hygiene):**
1. **MECH-074a** — its inverted-U component is asserted but only the monotonic direction is evidenced; the falling arm is unimplemented. Flag the claim's inverted-U sub-assertion as *not yet demonstrated* pending the F-P1 fix + a re-run.
2. **MECH-268** — conflict-saturation is validated only by 463b's synthetic `record_outcome` injection; the live path never populates it. The claim should carry a note that the *ecological* (live-loop) demonstration is outstanding until F-C3 is wired.

## 7. Regression harness (added this session)

`ree-v3/tests/test_flag_inertness.py` — the structural recurrence-guard recommended in §4. Three parts (current state: **2 passed, 1 xfailed**):
- **Behavioural probes** for the confirmed bugs, tied to a finding id. Known-broken ones are marked `xfail(strict=True)`: the suite stays green, and when the bug is fixed the probe XPASSes, the strict marker fails, and the fixer is forced to delete the marker — a fixed bug cannot silently un-fix.
  - `test_fp1_bla_encoding_gain_is_an_inverted_u_not_a_step` — asserts a rising arm (gain just above threshold strictly between floor and gmax) and a falling arm (panic arousal < peak). **Now PASSES** (F-P1 fixed this session; xfail marker removed — the regression latch worked as designed).
  - `test_fc3_dacc_saturation_is_fed_from_the_live_path` — spies on `DACC.record_outcome` across a live episode; confirmed 0 calls over 5 steps (inert for the right reason, not a masked crash). *(xfail: F-C3 — held, see below)*
- **`test_flag_registry_is_current`** — enumerates all 99 top-level `use_*`/`*_enabled` flags on `REEConfig` and fails if a new/uncategorized flag appears (or a listed flag was removed). Verified it bites on a simulated new flag. This is the guard that makes "is this flag actually wired?" a required checkbox — the thing whose absence let F-C2..F-P6 slip in.

Not yet probed behaviourally (documented in the file's `KNOWN_INERT`): **F-C1** (zero exposure — guard-before-use), **F-C2** (`dacc_foraging_weight`, a float lever, argmin-invariant), **F-C4** (`latent.use_iterative_inference`), **F-P6** (`vs_rollout_gate.unknown_stream_passes`).

**F-C3 HELD — coordination block.** The fix is one `record_outcome` call in the dACC section of `agent.py`, but `agent.py` is under an active (not-yet-stale) TASK_CLAIMS claim (`SD-033e`, frontopolar de-commit lever). Per the concurrency rules I did not edit it. The `xfail` latch stays in place so the moment it's wired the probe flips and forces the marker's removal. Spawn a chip / do it once SD-033e lands.

Code changed this session: `ree_core/amygdala/bla.py` (F-P1 fix) + `tests/test_flag_inertness.py` (new). No governance/registry code touched.

*Generated 2026-07-09T07:43:53Z; blast-radius + harness sections added 2026-07-09T08:09:54Z. Six parallel audit agents; registry findings F-R1/F-R3 and substrate finding F-P1 independently re-verified in-session; flag-inertness harness added and green.*
