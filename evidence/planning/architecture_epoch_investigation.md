# REE-v3 Architecture Epoch / Canonical Organism Investigation

**Session:** `sd-016-h3-algorithm-3370cd`
**Date:** 2026-08-12T06:52:35Z
**Type:** governance + architecture + experimental-provenance investigation. **No defaults changed, no epoch declared, no evidence retagged.**
**Status of this document:** design-now output. Final admission of anything touching E3 selection is explicitly gated on the in-flight F-dominance investigation (§15).

## Grounding

This is repository archaeology, not recollection. Six parallel research passes plus direct reads covered: `architecture_epoch` usage (source, manifests, indexer, governance); the `REEConfig` default-off surface (`ree-v3/ree_core/utils/config.py`, ~2,000 fields); the F-dominance/conversion-ceiling campaign status (`claims.yaml`, `substrate_queue.json`, `conversion_ceiling_campaign_plan.md`); concrete integration-failure cases (V3-EXQ-916/916a/917/920/922 and their autopsies); the manifest/provenance schema (`experiment_protocol.py`, `manifest_core.py`, `arm_fingerprint.py`); and a duplication check (`TASK_CHIPS.json`, `claims.yaml`, thought-intake, `ree-paper`). Two existing documents turned out to be direct, load-bearing prior art and are cited throughout rather than re-derived: `evidence/planning/default_off_drift_audit_2026-07-21.md` (and its now-standing regeneration, `scripts/default_off_drift_guard.py`, re-run live for this investigation) and `docs/architecture/version_layering_doctrine.md`.

---

## 1. What `architecture_epoch` currently means

It is a **hardcoded string literal, copy-pasted independently into ~1,316 experiment scripts** (`result["architecture_epoch"] = "ree_hybrid_guardrails_v1"`), backstopped by a shared constant in `ree-v3/experiments/pack_writer.py:47` that fills the field in if a script omits it. It is never derived from git commit, config hash, or topology — it is asserted by the author of each script, once.

Three real values exist in the live corpus (V1: `ree_v1_minimal_genuine_v1`; **V2 and V3 share `ree_hybrid_guardrails_v1`**; V4: `ree_self_model_v1`, 3 scripts so far, with `ree_multi_agent_v1` reserved as a documented future-track convention per `v4_spec.md:267`). So today it is best understood as a **coarse generation-family tag**, not a frozen-architecture-state guarantee: the `ARCHITECTURE_EPOCH` constant has been set exactly once since introduction, while `ree_core/utils/config.py` alone has taken 238 commits and `ree_core/` overall 350+ in the same window. Nothing checks that the string still describes current behaviour, and V2-era and V3-era evidence are **not distinguished by this field at all** — they collapse to the same string.

Cross-epoch filtering exists (`build_experiment_indexes.py`'s `scoring_excluded="stale_epoch"`, driven by `planning_criteria.v1.yaml`'s `epoch_start_utc`), but it does almost all its real work via a **timestamp cutoff**, not the epoch string — of 42 stale MECH-060 entries sampled, 40 were timestamp-excluded and only 2 were genuine string mismatches. Governance (`claims.yaml`) only consumes that flag; it has no epoch-aware promotion/demotion logic of its own.

Epoch identity today does **not** include config defaults or topology. It coexists with — but is structurally disconnected from — the newer provenance fields (`substrate_commit`, `substrate_hash`, `machine_class`, full `config` dump) introduced by the 2026-07-12 Recording Standard, which are written by an entirely separate code path and adopted in only 141–463 of 892 flat manifests so far. A config-default change does not require (and in 238-vs-1 commit practice, does not get) an epoch bump. Old experiments generally **cannot** be reconstructed exactly from `architecture_epoch` alone — it carries zero config information; reconstruction is only possible, for post-2026-07-12 runs, via `substrate_commit` + the full `config` dump, independently of the epoch string.

## 2. Whether an actual epoch-management mechanism already exists

**No single mechanism exists that lets you declare a new canonical baseline and enforce/replay it.** But nearly every component such a mechanism would need already exists in adjacent, disconnected form — this is substantially an integration problem, not a from-scratch build:

- **Generation-family tagging** (§1) — coarse, unenforced, real.
- **Evidence-applicability / stale-epoch filtering** — real time-based filtering; epoch-string filtering is currently a no-op between V2 and V3 since they share a string.
- **The 2026-07-12 Recording Standard** (`manifest_core.py`) — genuine reproducibility provenance (`substrate_commit`, `substrate_hash`, `machine_class` — now torch-version-aware since 2026-07-19, contra a stale note in `CLAUDE.md` — full `config` dump, `seeds`), soft-warned rather than mandatory, partially adopted.
- **`arm_fingerprint.py`'s content-addressed hashing** (`compute_substrate_hash`, `machine_class`, `config_slice`) — a real fingerprint mechanism, but scoped to baseline-reuse cache-key eligibility, explicitly "**persisted NOWHERE**" as a named artifact, with no migration path if the tag scheme changes.
- **`version_layering_doctrine.md` (2026-06-17)** — the closest existing thing to real epoch-boundary protection, but scoped narrowly to keeping V4/V5 changes from silently altering V3's *default* behaviour (the 654e incident: an unconditional V4 call-site broke the V3 critical path). Its three guards — conditional call-sites, a `v3_parity_smoke` regression battery run both at startup and in-process after every `git pull`, and a no-op/bit-identical contract test — are a **proven, directly reusable pattern** for exactly the "does admitting this flag break the default path" qualification a canonical-profile mechanism needs (see §12).
- **`default_off_drift_audit_2026-07-21.md`**, now a **standing, re-runnable guard** (`scripts/default_off_drift_guard.py`, confirmed to exist and re-run live for this investigation, see §3) — already answers most of "which default-off mechanisms does the registry treat as settled" with a machine-checkable, re-derivable method.
- **No** existing `CanonicalConfig`, `config_profile`, `profile_version`, or "constitution document" mechanism — confirmed zero hits. This is the genuine gap: naming, freezing, and admitting a canonical bundle.

## 3. How many scientifically meaningful default-off V3 mechanisms exist

`REEConfig` and its nested sub-configs carry **~2,000 typed fields, 540 of them boolean, 445 defaulting to `False`**. A keyword-filtered pass over those (excluding debug/log/instrumentation names) surfaces **248 candidates** that look architecturally meaningful.

The tighter, claim-linked measure is more useful and now has a **live, re-run number**: `scripts/default_off_drift_guard.py`, executed for this investigation (2026-08-12), currently parses **341 default-off dataclass fields** (up from 288 on 2026-07-21 — the corpus and the parser's own coverage both grew), **243 carrying a claim id** in their comment block, joined against claims at status `stable`/`active`/`provisional`/`implemented` to yield **132 candidate claim/knob pairs** (up from 63). The guard currently exits non-zero (**11 rows are the worst tier**: zero corpus enablement *and* no cited evidence run at all — e.g. `SD-010`/`gaba_harm_state_recurrence`, `SD-006`/`use_backward_credit_sweep`, `ARC-016`'s two eval-derived-precision knobs). Of the July snapshot's original 63 pairs, roughly a third were genuine registry/substrate divergence (Tier 1/2/3 below), a similar fraction were deliberate documented holds, and the rest were "off by default, on by convention" (benign — see §4).

Notable finding not in the July snapshot but present in the live re-run: **`MECH-090`** (status `active`, the BG-style beta-gate arbitration mechanism central to E3's committed-action readout) now shows **eight** constituent flags in the drift table — `beta_gate_bistable`, `use_commit_readiness_gate`, `use_vs_commit_release`, `use_coalition_controller`, `use_mech090_readiness_conjunction`, `use_modulatory_selection_authority`, `use_e3_reselection_shortcircuit`, `use_difficulty_gated_proposal_entropy` — most citing the same 2026-08-03 autopsy (`non_contributory/competence_implementation_gap`) rather than a clean PASS. This is directly relevant to §15: it is architecturally the F-dominance campaign's own territory.

## 4. How many appear default-off primarily for historical compatibility

Grepping `ree_core/` for stated rationale: **"backward compat"/"backward-compat" 174 hits, "legacy" 254, "V4-deferred" 7, "deprecated" 4**, across `config.py` and 63 other files (`agent.py` alone carries 61). Backward compatibility dominates the stated-rationale surface by roughly 20–30x over V4-deferred and deprecated combined — it is overwhelmingly the reason given, in comments, for why a meaningful mechanism defaults off.

But the drift audit's own three-way split is the more precise answer, and it matters for what to *do* with the count, not just report it:

- **(a) Deliberate, documented holds — not drift.** `ARC-007`, `ARC-018`, `Q-007`, `MECH-059`, `MECH-267` (`hold_pending_v3_substrate`/`hold_candidate_resolve_conflict`, already on the V3-Pending Gate). `use_differentiable_cem` is the clean case: 0 experiments enable it, but at least four manifests record `"use_differentiable_cem": "NOT FLIPPED (default False; SD-055 safety note)"` — the system working as designed, not drifting.
- **(b) Benign — off by config default, on by universal practice.** `use_harm_stream` (434 enablements), `use_affective_harm_stream` (402), `use_resource_proximity_head` (273), `use_per_stream_vs` (135), `use_lateral_pfc_analog` (143), `use_dacc` (149), `use_salience_coordinator` (57), `use_structured_curiosity` (45), `sws_enabled`/`use_sleep_loop` (40–47), `use_event_classifier` (38). The mechanism is genuinely exercised; only the *dataclass default* is stale. This is the largest bucket by enablement volume and is exactly the set that §14 marks HIGH CONFIDENCE.
- **(c) Genuine drift — registry says settled, substrate practice disagrees.** `SD-020` (its cited PASS run bypasses the flag entirely via a script-local prototype of a *superseded* predecessor script), `SD-032e`, `SD-006`, `MECH-089` (status/decision mismatch: promoted to `provisional` by decision record, registry now reads `active`), `MECH-259`, `SD-035` (evidence is module-level unit validation, never an agent-integrated run), `MECH-117`, `ARC-004` (the worst cell in the whole matrix — default-off *and* independently confirmed inert-when-on by `design_implementation_audit_2026-07-09.md`'s F-C4: at the default `inference_settle_iters=1` it runs `range(0)`, a no-op that also emits NaN).

## 5. Concrete examples where this has caused scientific/integration problems

Honest framing first: **explicit multi-mechanism "combination" experiments are rare** — direct grep found roughly 3–5 in the whole project history (916/916a's three-flag safety bundle, 922's three-knob SD-016 combo, 906/906a's full-stack showcase, 714's full-stack falsifier) against hundreds of single-axis experiments. This is not a rampant failure mode by volume. But of that small set, most of the recent ones hit real problems:

- **V3-EXQ-916 → confirmed autopsy** (`failure_autopsy_V3-EXQ-916-916a-917-920-fishtank-cluster_2026-08-12.md`): the driver was "the first to enable" `use_suffering_derivative_comparator`/`use_conditioned_safety_store`/`use_contextual_safety_terrain` together. The autopsy traces a **recording gap across the entire 664-derived lineage (7 prior experiments)**: `update_benefit_salience()`/`update_schema_wanting()` were never called from this driver family's step loop, *and* `benefit_exposure` was gated on `use_proxy_fields=True`, left at its default `False` by every 664-derived driver including this one — making the channel **structurally 0.0 across seven experiments** before anyone noticed. PASS outcome survived (non-load-bearing channel), but the gap was real for months and was only surfaced by the act of combining mechanisms for the first time.
- **V3-EXQ-917, same cluster**: the **production-default** MECH-303 safety threshold (0.05) never clears chance-level discrimination (AUC ≤0.52 across 18 tested values) under the sourcing convention every production driver (764, 520, 916) actually uses — only a non-production "legacy" sourcing mode reaches AUC 0.84–0.97. The autopsy explicitly warns its own supporting result "should NOT be read as validating the production default." Already routed (`SD-MECH303-THRESHOLD-SOURCING`) and currently tracked by open chip `chip-20260812-mech303-sourcing-mode-reconciliation` — not duplicated here.
- **V3-EXQ-920, same cluster**: queue declared `"seeds": 8`; the runner only ever consumes an explicit `--args` field for seed count, which this entry lacked, so the driver's own 1-seed default silently governed the run — an underpowered FAIL mislabeled by a hardcoded self-route string. Not a `REEConfig` flag, but the identical "declared configuration ≠ actual configuration, silently" shape.
- **V3-EXQ-922** (`sd016_mech151_152_arc041_production_combo`): queue note is explicit — "this exact three-knob combination has NEVER been run together." Outcome: **FAIL**, dissociated (only MECH-151 confirmed of the predicted MECH-151/152 dual pathway). **No confirmed autopsy yet** (listed in `pending_review.md` and named as an open candidate in a sibling autopsy). This is surfaced here, not chipped — adjudicating an un-autopsied FAIL is `/failure-autopsy` work, which CLAUDE.md's chip-exception list keeps inline/governance-owned, not something this session spawns.
- **Registry-level instance of the same failure class**: the drift audit's own Tier-1 finding that `SD-020` (`stable`) is cited to a PASS run whose actual causal path never touches the substrate flag at all — a claim describing a configuration nobody runs is the "Interpretive ambiguity" failure class operating at the governance layer, not just the experiment layer.

## 6. Whether "REE-v3" currently denotes a unique canonical organism

**No.** At least four genuinely different things could each be called "REE-v3" today, and they diverge substantially:

1. **Bare `REEConfig()` defaults** — 445/540 booleans off, including validated mechanisms (`ARC-027`/`SD-010` harm stream, most of `MECH-090`'s gating triad, the `MECH-302/303/304` safety triad).
2. **The `ree_hybrid_guardrails_v1`-tagged corpus** — spans *both* V2 and V3 by the field's own current semantics (§1), so it isn't even internally a single generation.
3. **Any given script's hand-assembled bundle** — 916/916a/925/922 each independently reassemble overlapping but non-identical ~10–20-flag bundles (925's is the largest at 20 explicit overrides; 922 explicitly turns sleep *off* even inside a "production combo").
4. **The empirically-converged "on by convention" set** — drift-audit bucket (b): the flags effectively everyone turns on (harm stream, resource proximity, per-stream VS, lateral PFC, dACC, event classifier, sleep loop). This is the closest thing to a de facto canonical bundle, but it has never been written down; it exists only as a statistical pattern across independently-authored scripts, discoverable only by re-running the drift guard.

None of these is official, and they are not interchangeable — (1) excludes mechanisms the registry calls settled; (3) varies experiment to experiment; (4) is unwritten. This is the concrete answer to "what is the current REE-v3 organism": there isn't one, by construction.

## 7. Options for fixing the problem

Evaluated against: reproducibility; accidental-omission risk; interpretability; implementation complexity; interaction with existing manifests; historical replay; ablation ergonomics; governance burden; silent-change risk; V3↔V4 interaction; developmental-experiment support.

**Option A — flip global dataclass defaults at an epoch boundary.** Omission risk is low (it's global — nothing to individually remember), but historical replay is where this fails: only post-2026-07-12 manifests carry a full config dump to pin against a defaults change, so flipping defaults would silently change the *effective* configuration of the ~85% of the corpus without recorded config, with nothing to notice. It is also structurally the exact shape `version_layering_doctrine.md` exists to guard against (a shared-code default change breaking things by default) — just pointed at "new V3 vs old V3" instead of "V4 vs V3," with no equivalent guard built for that direction. Not recommended as primary.

**Option B — canonical organism profile** (`REEV3CanonicalConfig(epoch=...)` or similar, layered above unchanged backward-compatible `REEConfig()` defaults). Cleanly separates the two planes already implicit in the archaeology: bare-defaults-as-historical-compatibility-surface vs. profile-as-what-organism-level-experiments-actually-run. Ablation ergonomics are exactly the "epoch E organism minus mechanism X" model the investigation brief itself proposes. Buildable directly on `arm_fingerprint`'s existing `config_slice`/`compute_substrate_hash` machinery for identity, and on `manifest_core`'s existing full-config-dump field for recording. Governance burden is moderate — one profile object to curate per admission criteria (§9), not a global flip.

**Option C — immutable epoch config-bundle, hash-addressed.** Strongest reproducibility guarantee; it is literally `arm_fingerprint`'s existing pattern (`config_slice` + `compute_substrate_hash`) elevated from an ephemeral arm-reuse cache key to a persisted, named, versioned artifact. Highest implementation complexity of the concrete options, because that module explicitly has **no migration path today** ("persisted NOWHERE... a fingerprint tag change is a hard cut"). Best read as the mechanics *underneath* B, not a rival to it: B names/curates the profile, C is how you freeze and hash it.

**Option D — governance-state-generated canonical config** (assembled live from `claims.yaml` admission status). Rejected as the primary mechanism: a claim's status is not a stable identity — the `MECH-089` decision/registry mismatch (promoted to `provisional`, registry now reads `active`) already exists in the corpus *without* this option even being built. Auto-assembling a live organism definition from a registry that already has unreconciled status drift would propagate that instability directly into the thing defining reproducibility. Governance status can still feed a human-curated profile update (B) as an *input*, just not as a live auto-assembly rule.

**Option E — existing project mechanism, if better.** `version_layering_doctrine`'s three-guard pattern is the strongest existing candidate, but it solves a narrower, different problem (protect V3 defaults from V4 bleed-through). It is not itself sufficient as a full Option E — but its **guard pattern**, especially the `v3_parity_smoke` regression battery and the no-op/bit-identical contract test, is directly reusable as the qualification-battery backbone for B/C (§12), rather than building a new battery from scratch.

## 8. Recommended architecture for epoch/canonical-profile management

**B+C combined, not A, not D.**

- A versioned, named, human-curated canonical profile sits **above** the unchanged, backward-compatible `REEConfig()` bare defaults — historical replay and `version_layering_doctrine`'s existing V3-vs-V4 guarantee stay untouched.
- Each declared profile version is frozen and content-hashed using `arm_fingerprint`'s existing `compute_substrate_hash`/`config_slice` machinery, this time **persisted** as a named artifact (e.g. under `REE_assembly/docs/architecture/canonical_profiles/<name>.json`) with a human-readable constitution doc alongside it (§14 of the brief; chipped in §16).
- New organism-level/whole-organism experiments construct their config from the profile rather than hand-re-deriving 10–20 overrides per script — directly fixing the 916/916a/925/922 divergent-bundle pattern found in §5/§6.
- **`architecture_epoch` is not further overloaded**, per the brief's own explicit instruction. It keeps its current, coarse "generation family" meaning (V1/V2+V3/V4). A new, orthogonal manifest field pair — `canonical_profile` + `canonical_profile_hash` — records which curated bundle (if any) a run used. This resolves the "what does the epoch string even guarantee" confusion (§12 of the brief) by not asking one field to do all the work: `architecture_epoch` answers "which generation," `canonical_profile` answers "which curated organism, if any."
- Qualification for declaring or updating a profile reuses the `version_layering_doctrine` guard pattern (§12).

## 9. Proposed admission criteria

Multi-dimensional, not binary implemented-vs-canonical, and explicitly reusing the drift guard's already-proven discriminators rather than inventing new ones:

1. Substrate implemented (trivial gate).
2. **Corpus enablement count** (`default_off_drift_guard.py`'s load-bearing discriminator) — near-zero enablement despite `stable`+ status is a red flag for admission *regardless of paper status* (the `SD-020`/`MECH-089`/`SD-035`/`MECH-117`/`ARC-004` pattern, §4c).
3. **The cited evidence run actually exercises the same flag/path the claim describes** — must be checked, not assumed from status text (`SD-020`/`SD-035` both fail this: script-local prototype and module-level unit test respectively, not an agent-integrated run).
4. **Non-degenerate / no catastrophic disruption of unrelated core function**, via the `version_layering_doctrine` Guard-C pattern generalized from "V4/V5 off" to "profile-candidate flag off vs. on."
5. **Known-interaction check** against other admitted candidates in the same subsystem — at minimum the already-known-risky combinations found in §5 (MECH-303's threshold/sourcing mismatch, SD-016's three-knob dissociation) must gate admission of anything touching the same subsystem until re-verified *under the actual combination*, not just individually.
6. Claim status ≥ `provisional`, `stable`/`active`/`implemented`/`candidate_substrate_landed` preferred — necessary but explicitly **not sufficient** given criteria 2–3.
7. Do **not** require zero open governance debt to admit — that reproduces the paralysis the brief warns against. Use the category structure below instead of a binary gate.

Categories (per the brief's own proposed structure, now populated — see §14): **Canonical core**; **Canonical but context-dependent**; **Experimental substrate**; **Diagnostic-only**; **Deprecated/superseded**; **V4-deferred**.

## 10. Proposed historical-reproducibility rules

The needed machinery mostly already exists (§2) and is under-enforced rather than missing:

- **Make `substrate_commit` + full `config` dump mandatory** on every manifest, not soft-warned via `missing_core_fields` — currently only 141–463 of 892 flat manifests (and a minority of 2,821 pack manifests) carry it, despite `manifest_core.py`'s own docstring stating this was built precisely because "0% of flat manifests record a substrate hash, which is precisely why no historical baseline can be safely reused." This is a much cheaper fix than a new mechanism — it closes a gap the project already diagnosed and half-fixed. (Chipped, §16.)
- `architecture_epoch` continues recording the coarse generation tag, unchanged.
- New `canonical_profile` + `canonical_profile_hash` fields record which curated bundle (if any) a run used — null/absent for ad hoc or historical runs, which is the honest signal that such a run's config identity exists only as a raw dump, not a small reproducible hash.
- Comparison/aggregation tooling should refuse or flag when pooling manifests whose `architecture_epoch` **or** `canonical_profile_hash` differ, absent an explicit cross-epoch annotation (§11) — currently **nothing does this**: no comparison/plotting tool with any epoch-awareness exists in either repo.

## 11. Proposed cross-epoch evidence rules

- Extend the existing `scoring_excluded="stale_epoch"` / `evidence_applicability` mechanism in `build_experiment_indexes.py` + `planning_criteria.v1.yaml` — this is the right place, not a new subsystem.
- Fix the identified gap explicitly: today it filters almost entirely by timestamp, and the V2/V3 shared epoch string makes epoch-based filtering a no-op between those two generations. Recommend **not** forking `ree_hybrid_guardrails_v1` retroactively (that would be exactly the kind of after-the-fact overload §1 warns against) — instead document that the string is intentionally V2+V3-spanning, and use the new `canonical_profile` field (§8) for any V3-internal boundary that actually needs distinguishing.
- Require an explicit "cross-epoch comparison" annotation whenever a report or governance note intentionally compares across `canonical_profile` boundaries (e.g. "does mechanism X's effect replicate under the new profile") — no such convention exists anywhere today.

## 12. Proposed integration qualification

Reuse `version_layering_doctrine`'s guard pattern rather than building a new battery:

- **`run_v3_parity_smoke()` + `tests/preflight/test_v3_parity_smoke.py`** — today proves "all V4/V5 flags off ⇒ bit-identical to the pre-V4 baseline." The same harness shape, pointed at a candidate profile instead of `assert_all_off`, proves "profile-candidate flags on ⇒ still runs, contract suite still green, no catastrophic regression."
- **`test_version_layering_noop_default.py`**'s C1–C4 structure generalizes directly: default-off assertion → path-resolves-on-real-config → bit-identical-when-off → runs-without-error.
- Distinguish, per the brief's own framing: **catastrophic regression** (non-learning, NaN, degenerate, immobile — reuse `design_implementation_audit_2026-07-09.md`'s per-flag inertness findings, e.g. `ARC-004`'s confirmed `range(0)` no-op) vs. **expected architectural change** (a metric moves because an admitted mechanism genuinely changes behaviour — must be explained, not auto-rejected) vs. **scientific regression** (a previously-validated capability silently disappears) vs. **measurement incompatibility** (a metric's meaning changed).
- Existing reusable components beyond the doctrine's own guards: the ~3,500-test contract suite (routed to cloud per `CLAUDE.md`'s pytest-routing rules), `test_flag_inertness.py` (does the flag do anything when on?), the Fishtank whole-organism smoke pattern already exercised by the 906/916 family, and the channel-non-degeneracy / core-channel PASS gates already used in 916a's autopsy.
- **The one genuinely missing piece**: nothing today runs this battery specifically *keyed to a profile change* as a qualification gate. That is the one new integration point needed (chipped, §16) — everything it depends on already exists.

## 13. Whether developmental history must be part of epoch identity

**Real, and not already represented anywhere in the repository** — confirmed no existing machinery, doc, or claim addresses whether "enabled at test time" is scientifically equivalent to "developed with the mechanism present." Concrete grounded reasons to think it matters here specifically, not just in the abstract:

- Sleep mechanisms (`sws_enabled`/`rem_enabled`/`shy_enabled`, `SD-017`/`MECH-120`) are explicitly master-switched, off by default, and only reach ~40/47 enablement even in the "on by convention" bucket — a consolidation mechanism whose effects are plausibly history-dependent by construction.
- `MECH-090`'s gating triad governs which actions get consolidated into committed behaviour — enabling it only at evaluation time is not obviously equivalent to having the organism's action-selection history run under it.
- The `MECH-302/303/304` safety triad governs *conditioned* safety learning — explicitly experience-dependent by definition; a mechanism that learns from exposure is not fully characterized by a test-time flag flip.

The `config` manifest field (a single dict, current-value-only) has **no way to represent a developmental history** even if the question were answered — this points toward a probable future Recording-Standard extension, not something to design now. **Chipped as a scoping question** (§16), per the brief's own instruction to chip it if real and unrepresented.

## 14. Candidate mechanisms for the next canonical epoch, grouped by confidence

**HIGH CONFIDENCE — already de facto canonical by practice, just unwritten** (drift-audit bucket (b), admitting these mostly formalizes existing behaviour): `use_harm_stream`/`use_affective_harm_stream` (`SD-010`/`ARC-027`, 434/402 enablements), `use_resource_proximity_head` (`SD-018`, 273), `use_per_stream_vs` (`SD-007`, 135), `use_lateral_pfc_analog` (`MECH-261`, 143), `use_dacc` (`SD-032a`, 149), `use_salience_coordinator` (`SD-032a`, 57), `use_structured_curiosity` (`ARC-065`, 45), `sws_enabled`/`use_sleep_loop` (`SD-017`, 40–47), `use_event_classifier` (`MECH-100`, 38).

**MEDIUM CONFIDENCE — validated substrate, real but limited exercise, admit as "canonical but context-dependent" pending broader combination testing:** `use_pcc_analog`/`use_aic_analog` (`MECH-259`), `use_amygdala_analog` (`SD-035` — agent-integrated form specifically, not the module-level-only evidence). The `MECH-302/303/304` safety triad (`use_suffering_derivative_comparator`/`use_conditioned_safety_store`/`use_contextual_safety_terrain`) belongs here **only conditional on** the already-chipped `chip-20260812-mech303-sourcing-mode-reconciliation` landing — §5 found the production-default threshold does not currently work.

**LOW CONFIDENCE / REAL DRIFT — do not admit without re-verification against §9's criteria first:** `SD-020`'s `harm_surprise_pe_enabled`, `SD-032e`'s pACC write-back, `SD-006`'s `use_backward_credit_sweep`, `MECH-089`'s `use_multi_content_theta_packet` (also carries an unresolved status/decision mismatch), `MECH-259`'s narrow `use_pcc_analog` reading, `SD-035`'s pure module-level reading, `MECH-117`'s `goal_weight`, `ARC-004`'s `use_iterative_inference` (confirmed inert at default settle-iters — do not admit without fixing the paired knob).

**DIAGNOSTIC-ONLY / DELIBERATE HOLD — do not admit:** everything behind `use_differentiable_cem` (`ARC-007`/`SD-016`/`SD-055`) — a documented, self-annotating hold, not drift; leave it on its own resolution track.

**V4-DEFERRED:** anything in `version_layering.py`'s `GENERATION_FLAGS` registry (DR-12's `e3.use_pe_confidence_weighting` and siblings) — explicitly out of scope for a V3 profile by the doctrine's own invariant.

**GATED ON F-DOMINANCE, do not admit regardless of individual status** (§15): `MECH-090`'s full gating triad and anything touching `ree_core/predictors/e3_selector.py`'s committed-action readout — this is the live, contested campaign's own territory.

## 15. Which elements should wait for the F-dominance investigation

**Status as of 2026-08-12**: F-dominance (`MECH-439`, the "conversion ceiling" — F monopolises ~88–89% of E3's committed-selection variance) is a live, multi-week campaign (`conversion_ceiling_campaign_plan.md`), most recently governance-reviewed 2026-08-08 as `assembly_status: ran_exhausted_for_substrate` with its **re-derive brake fired** ("do NOT re-queue any conversion or de-commit falsifier" on the current substrate). A fresh causal-localisation sub-investigation is actively in-flight *today* (claim `mech357-pressure-scoping-11e9c9`, discriminating four rival hypotheses H1–H4 via a not-yet-built diagnostic, `V3-EXQ-925`), and a same-session remeasurement (`V3-EXQ-924`, completed 2026-08-12) found the most recent E3-scorer fix **increases** rather than resolves F's dominance. None of the campaign's own claims (`MECH-439/448/449/450/451/457`, `ARC-107/108/110`) carry a strong/confirmed status; all remain `candidate`/`provisional`.

**Wait for F-dominance**: final admission of anything touching E3 selection/arbitration (`MECH-090`'s gating triad and neighbours, §14); any integration-qualification run that exercises committed-action selection under a candidate profile (it would need repeating post-resolution regardless); the final epoch/profile *declaration* itself; and — because Option B doesn't require it — **changing global defaults is not needed to proceed with the rest of this design, so nothing here should be read as blocked on F-dominance by default.**

**Not gated**: the profile mechanism's plumbing (manifest fields, persisted fingerprint, admission-criteria doc, qualification-battery wiring, constitution-doc template) — none of it depends on knowing F-dominance's outcome, only on there *being* an outcome to plug in later.

## 16. New chips/tasks created

Checked against `TASK_CHIPS.json` (540 entries, zero hits on epoch/canonical/profile/fingerprint terms), `claims.yaml`, thought-intake, and `WORKSPACE_STATE.md` before spawning — see dedup findings above. Two follow-on items found already in flight and **not** duplicated: `chip-20260812-mech303-sourcing-mode-reconciliation` (open, covers §5/§14's MECH-303 gate) and V3-EXQ-922's pending autopsy (governance/`/failure-autopsy` work, reported not chipped, per CLAUDE.md's exception list).

Chips spawned this session (recorded via `chip_ledger.py` immediately after each `spawn_task` call, per Concurrency Rules):

1. Design + prototype the canonical-profile mechanism (Option B+C plumbing: profile object, persisted `arm_fingerprint`-based hash, new manifest fields).
2. Write the admission-criteria doc + constitution-document template for the eventual profile.
3. Scope the developmental-history-as-epoch-identity question (§13).
4. Make Recording Standard `substrate_commit`/`config` fields mandatory; close the manifest-coverage gap.
5. Build a `canonical_profile`/`architecture_epoch`-aware aggregation guard in the indexer/comparison tooling.

All five spawned and recorded in `TASK_CHIPS.json` (2026-08-12T06:56–06:59Z): `chip-20260812-canonical-profile-mechanism-design`, `chip-20260812-canonical-profile-admission-criteria`, `chip-20260812-developmental-history-epoch-scoping`, `chip-20260812-recording-standard-mandatory-provenance`, `chip-20260812-cross-epoch-aggregation-guard`. Each prompt opens with a first-action instruction to claim its own resources and self-reports at `/session-land` via `chip_ledger.py resolve --chip-ref <ref>`.

## 17. What should trigger the actual epoch-declaration decision

Not a calendar date or a flag-count threshold. Recommend the decision be triggered when **all** of the following hold:

1. F-dominance's causal-localisation work (§15) reaches a governance-reviewed disposition — resolved, or explicitly deferred with a stated reason — for at least the `MECH-090` gating triad and the campaign's own claims.
2. The chips in §16 have landed: the profile mechanism exists and is wired into manifest recording; an admission-criteria pass has been run against the then-current `default_off_drift_guard.py` output; a constitution-doc draft exists.
3. A qualification run (§12) against the candidate profile is green: contract suite, `v3_parity_smoke`-pattern battery, no catastrophic regression, and any expected architectural changes are explained rather than silently absorbed.
4. The developmental-history question (§13) has at least a scoped answer — not necessarily solved, but not silently begged either.

At that point, use the draft second-stage prompt below to adjudicate and, if justified, declare.

---

## Recommended transition plan (not executed)

1. Land chips 1–2 (§16): mechanism + admission-criteria/constitution-doc design.
2. Run admission criteria (§9) against a fresh `default_off_drift_guard.py` pass; sort every candidate flag into the six categories (§9/§14); draft the profile's first-cut member list from HIGH + eligible MEDIUM confidence tiers only.
3. Land chip 4 (§16): make provenance fields mandatory, so the profile's own qualification runs are themselves fully reproducible.
4. Build and run the qualification battery (§12) against the draft profile on a machine with capacity (per `CLAUDE.md`'s cloud-routing guidance) — expect and explain architectural changes, treat catastrophic regressions as blocking.
5. Wait on §15's F-dominance gate before admitting anything E3-adjacent; re-run qualification once that's resolved if the draft profile needs amendment.
6. Land chip 3 (§16) in parallel — the developmental-history scoping does not block 1–5.
7. Land chip 5 (§16) — wire the aggregation guard before the profile sees its first real cross-epoch comparison, not after.
8. Only then: run the second-stage adjudication prompt below, with a human governance decision to actually declare.

## Draft second-stage prompt (for use after F-dominance concludes)

```
REE-v3 Canonical Epoch Adjudication (post-F-dominance)

Context: architecture_epoch_investigation.md (2026-08-12) designed but did not
execute a canonical-profile mechanism (Option B+C: a versioned, curated
REEV3CanonicalConfig layered above unchanged backward-compatible REEConfig()
defaults, frozen and content-hashed via arm_fingerprint's existing machinery,
recorded via new canonical_profile/canonical_profile_hash manifest fields
alongside the unchanged architecture_epoch generation tag).

The F-dominance/conversion-ceiling investigation (MECH-439 and campaign) has
now reached [STATE: resolved / explicitly deferred -- fill in]. Re-verify this
claim against current claims.yaml and substrate_queue.json before proceeding --
do not trust this prompt's framing if the repository now says otherwise.

Do:
1. Re-run scripts/default_off_drift_guard.py fresh; re-apply the admission
   criteria in architecture_epoch_investigation.md Section 9 to the current
   corpus (not the 2026-08-12 snapshot -- numbers will have moved).
2. Resolve MECH-090's gating triad and neighbours (beta_gate_bistable,
   use_commit_readiness_gate, use_vs_commit_release, use_coalition_controller,
   use_mech090_readiness_conjunction, use_modulatory_selection_authority,
   use_e3_reselection_shortcircuit, use_difficulty_gated_proposal_entropy)
   against whatever the F-dominance investigation concluded -- these were
   explicitly gated in Section 15 and are not yet re-evaluated.
3. Draft the profile's member list per Section 14's category structure,
   updated with current evidence.
4. Run the qualification battery (Section 12) against the draft profile.
   Classify every observed change as catastrophic regression / expected
   architectural change / scientific regression / measurement incompatibility
   -- do not auto-accept or auto-reject; explain each.
5. If qualification is clean (or all deltas are explained architectural
   change): present the draft profile, its constitution doc, and the
   qualification report to the user for an explicit go/no-go decision on
   declaring it canonical. Do not declare unilaterally.
6. If declared: write the epoch-transition record this investigation's
   Section 15 (item 15 of the original governance prompt) deferred --
   documenting not "defaults changed" but "the project changed the organism
   it regards as its current integrated baseline" -- and flag the ree-paper
   historical-archaeology dependency without writing that history yet.

Do not: flip global REEConfig() defaults; bulk-retag existing evidence;
rewrite old manifests; run large integration batteries beyond the
qualification battery; declare the epoch without an explicit user decision.
```
