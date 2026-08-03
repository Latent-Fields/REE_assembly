---
closure_plan:
  id: substrate_stability_and_drift_detection
  # Infrastructure/tooling lane, not V3 substrate science -- owns no scientific
  # claims, so it is segmented out of the V3 closure % the same way
  # arm_reuse_fingerprint_plan is (see that plan's own generation note).
  generation: process
  title: "Substrate Stability + Claim-Drift Detection (freeze substrate per run; detect when it has moved since a claim's evidence was recorded)"
  registered: 2026-08-03
  last_updated: 2026-08-03
  scope_claims: []
  sibling_plans:
    - arm_reuse_fingerprint_plan.md
  nodes:
    - id: "substrate_stability:P0-detector"
      title: "Phase 0 -- instrument only: check_substrate_staleness_candidates.py. Scans claim-tagged flat manifests, recomputes the current substrate hash over the same globs arm_fingerprint.py already uses, reports drift candidates. Read-only; never writes a manifest field."
      phase: 0
      status: done
      severity: medium
      owner_exq: null
      last_updated: 2026-08-03
      completion_note: "REE_assembly/scripts/check_substrate_staleness_candidates.py landed + unit-tested (test_check_substrate_staleness_candidates.py). Reuses ree-v3/experiments/_lib/arm_fingerprint.py's compute_substrate_hash unmodified against a throwaway detached worktree at origin/main (never reimplements the hash algorithm). Zero validity risk -- prints a report only; the existing pending_retest_after_substrate / superseded_by_substrate gate in build_experiment_indexes.py (landed 2026-06-02, predates this plan) is the sole consumer and is unchanged."
    - id: "substrate_stability:P1-scope-schema"
      title: "Phase 1 -- optional per-claim substrate_scope declarations in claims.yaml (same glob format arm_fingerprint/substrate_scope_guard already use), narrowing the detector from whole-tree to declared scope to cut noise."
      phase: 1
      status: done
      severity: low
      owner_exq: null
      last_updated: 2026-08-03
      completion_note: "check_substrate_staleness_candidates.py extended: load_claim_substrate_scopes() reads optional substrate_scope off claims.yaml; a drift candidate whose diffed changed-file list does not intersect a claim's declared scope moves to a new 'filtered OUTSIDE declared substrate_scope' bucket (per-claim, not per-manifest -- other claims on the same manifest are unaffected). 2 pilot claims declared (MECH-471, MECH-321), both derived from an actual read of the claim's own dependency (the V3-EXQ-875 autopsy for MECH-471; the claim's own implementation_note for MECH-321), not guessed. 9 new unit tests (_file_in_scope correctness incl. the zero-intervening-dirs / false-prefix-match traps a naive '**'->'*' substitution would get wrong) + the end-to-end fixture extended to exercise both the in-scope and out-of-scope branches for real. REAL FINDING running against the actual corpus (see section 4.5): 0 of the 2 pilots' diffable candidates were filtered -- both legitimately declare a dependency on ree_core/agent.py, which ~half of recent substrate-touching commits touch, so scope narrowing alone provides no noise reduction for hub-file-dependent claims. Motivates P1b."
    - id: "substrate_stability:P1b-default-off-filter"
      title: "Phase 1b -- a changed file whose diff is confined to code reachable only under a still-default-off config flag this run's driver never references downgrades from a drift candidate to informational (3-valued/Kleene formula evaluation over pure AND/OR/NOT-of-flag conditions, textual proxy for flag-enablement since manifests don't record actual REEConfig field values)."
      phase: 1
      status: done
      severity: medium
      owner_exq: null
      last_updated: 2026-08-03
      completion_note: "check_substrate_staleness_candidates.py extended: load_default_off_knob_names() reuses default_off_drift_guard.parse_knobs() unmodified; inert_line_ranges()/_eval_flag_formula() find if-bodies whose test is a pure boolean formula over default-off flags that evaluates to definite False (Kleene logic -- one confirmed-disabled flag resolves an AND short-circuit to False even beside an unrelated/unresolvable operand, matching real Python and-semantics); flag_status_from_driver_source() is a conservative textual proxy (a flag counts confirmed-disabled only if its name never appears anywhere in the driver source at the recorded commit; a mention in either direction stays Unknown, never guessed). 26 new unit tests including a real 2-commit git fixture. Found and fixed a real bug during testing: importing default_off_drift_guard.py without registering it in sys.modules before exec_module silently broke (@dataclass needs sys.modules[cls.__module__] to resolve), which the broad except would have swallowed into a silent, permanent no-op -- same class of bug this repo's own test_substrate_staleness_gate.py _load_indexer() pattern already works around. REAL FINDING running against the actual corpus (section 4.6): 0 pairs filtered for either pilot, again -- traced to a genuine, different limitation than Phase 1's: this repo's actual recent default-off additions (SD-092's notify_subgoal_attainment, etc.) are new hook METHODS added to agent.py whose flag check lives in a DIFFERENT file's callee (GoalState.credit_subgoal_attainment in ree_core/goal.py), not an in-place `if flag:` wrapping existing code in the same file -- structurally invisible to a same-file AST analysis. Catching that pattern would need interprocedural reachability analysis (expensive, fragile) or actually running the code (the arm_fingerprint call-trace guard's approach) -- out of scope for a lightweight governance script. Phase 1b is correct and tested for the pattern it targets; that pattern is just not what's common in this codebase's recent history."
    - id: "substrate_stability:P2-governance-surface"
      title: "Phase 2 -- surface Phase-0/1 candidates in /governance or morning-digest (pending_review.md-style derived report or an IGW workset item), gated on Phase 0/1 first proving the signal is low-noise enough to be worth a human's attention every cycle."
      phase: 2
      status: open
      severity: low
      owner_exq: null
      last_updated: 2026-08-03
      completion_note: ""
    - id: "substrate_stability:P1c-prospective-recording"
      title: "Prospective-only recording of enabled default-off REEConfig flags into future manifests, via a new reusable helper (generalizing q081_profile.py's _read_flag pattern) + reuse of the EXISTING agent= kwarg already threaded through stamp_recording_core/write_flat_manifest for z_goal_stream. Cannot retroactively cover manifests already on disk (see section 6)."
      phase: 1
      status: done
      severity: medium
      owner_exq: null
      last_updated: 2026-08-03
      completion_note: "ree-v3/experiments/_lib/manifest_core.py: enabled_default_off_flags(config) (recursive dataclass-field walk, generalizing q081_profile.py's 4-holder hardcoded _read_flag) + enabled_default_off_flags_for_agents(agent) (pools one-or-many agents, same normalisation as z_goal_stream_stats) + wired into stamp_recording_core() as a new best-effort block reusing the EXISTING agent= parameter -- no new kwarg needed on write_flat_manifest at all, since it already forwards agent= for z_goal_stream and that threading is already live for ~28 of 565 stepping drivers today. 24 new pytest tests in tests/contracts/test_recording_standard.py (fixture dataclasses, no torch/ree_core import needed, matching manifest_core.py's own stdlib-only posture), plus a real end-to-end smoke against the actual REEConfig. FOUND AND FIXED A REAL PRECISION GAP mid-implementation, before landing: the first draft followed z_goal_stream's 'omit when nothing to report' convention, which for THIS field silently collapsed two different, important cases into the same omission -- 'no agent passed' (never measured) and 'agent passed, nothing enabled' (measured, legitimately all-defaults) -- indistinguishable to a downstream consumer that needs the second case to say 'every other known flag is confirmed disabled,' not 'unknown.' Fixed: enabled_default_off_flags_for_agents returns None (omit) only when no config-bearing agent was found at all, and an actual (possibly empty {}) dict otherwise -- caught and corrected by writing the consumer-side test before shipping, not by manual review. Consumer side: check_substrate_staleness_candidates.py's flag_status_from_recorded_config() reads the field when present (matching parse_knobs()'s bare field names against the recorded dict's trailing dotted-path segment, e.g. 'goal.use_hierarchical_goal_credit' -> 'use_hierarchical_goal_credit') and main() prefers it over the textual driver-source proxy whenever a manifest has it; also fixed the existing default_off_cache (keyed by commit+experiment_type+path) to route AROUND that cache for recorded-config lookups, since -- unlike the driver-source proxy -- the recorded status is manifest-specific, not a pure function of that key (two arms of one experiment_type at one commit could genuinely record different enabled flags). 6 new unit tests for the consumer function + 1 integration test proving the recorded path succeeds where the proxy has nothing to read (55 tests total in the suite). REAL corpus run confirms this is genuinely prospective, as designed: 0 of 621 manifests have the new field yet (no driver has been updated to adopt it), so 0 pairs used it -- exactly the expected result for a feature that only benefits FUTURE runs, not a null finding like P1/P1b's. Landing this into new /queue-experiment drivers (so it actually starts accumulating coverage) is the natural next step, not done this session."
    - id: "substrate_stability:P1d-interprocedural-hop"
      title: "One-hop interprocedural extension to Phase 1b: build a corpus-wide function index, resolve a changed function's calls by name to their definitions, and treat the change as inert when the caller has no direct side effect AND every resolved callee is confirmed inert by its own top-of-body guard clause. Also fixed _eval_flag_formula to recognise the getattr(obj, name, default) gate idiom (622 occurrences in ree_core/, the dominant shape -- previously unrecognised entirely)."
      phase: 1
      status: done
      severity: medium
      owner_exq: null
      last_updated: 2026-08-03
      completion_note: "check_substrate_staleness_candidates.py extended with: (1) _eval_flag_formula now recognises getattr(obj, \"name\", default) as a flag reference (previously only direct attribute access) -- a real, valuable, retroactive fix to Phase 1b itself, not just P1d, since this is the dominant gate idiom in ree_core (622 occurrences measured). (2) build_function_index() (name -> every FunctionDef/AsyncFunctionDef across the current substrate scope, built once per report run), _has_disqualifying_side_effect() (scope-respecting -- found and fixed a real bug during testing: a naive ast.walk-based nested-function exclusion only skips the FunctionDef node itself, not its descendants, since ast.walk flattens across scope boundaries; fixed with a proper ast.iter_child_nodes recursion that never descends into a nested def/lambda/class), _guard_clause_confirms_inert() (a callee's own first-statement `if <formula>: return <cheap>` confirmed to always fire), _function_is_one_hop_inert(), and one_hop_inert_line_ranges(), unioned with Phase 1b's existing if-body ranges. 25 new unit tests including the ACTUAL real-world shape (notify_subgoal_attainment calling credit_subgoal_attainment across files) as a positive control -- confirmed working IN ISOLATION. 87 tests total in the suite. REAL corpus run: STILL 0 pairs filtered for either pilot -- but for a THIRD, deeper root cause than P1/P1b's, not a repeat: traced (not guessed) via direct debugging that use_hierarchical_goal_credit resolves as Unknown, not confirmed-False, for MECH-471's driver, because default_off_drift_guard.py's parse_knobs() ONLY parses ree_core/utils/config.py -- and GoalConfig (which declares that flag) is defined in ree_core/goal.py, a different file, imported in as a nested REEConfig field. Confirmed exactly 2 of 10 nested config classes (GoalConfig, SerotoninConfig) live outside config.py and are therefore invisible to parse_knobs() entirely -- this is a real, bounded, well-scoped gap in default_off_drift_guard.py itself, one layer below everything built this session, and P1c's own runtime-introspection recording (enabled_default_off_flags(), which walks the LIVE dataclass structure regardless of which file declares each nested class) does NOT share this limitation -- confirming the asymmetry is specific to the AST-based knob-name approach Phase 1b/1d both depend on. Also confirmed even accounting for this, 183 of 236 changed lines in ree_core/agent.py for the MECH-471 candidate remain uncovered (use_coalition_controller DID resolve correctly, confirmed False, since it lives in config.py directly) -- other gating idioms (e.g. a cached state check like `if self.coalition is not None:`, which is a derived-at-init-time proxy for a flag rather than a direct flag reference) are not recognised by any analysis built this session and would need actual data-flow tracking to close. See section 7.4 for the full writeup. Not fixed here -- extending parse_knobs() to cover nested-config classes declared outside config.py is a well-scoped, separate follow-on, flagged not built."
    - id: "substrate_stability:ISO-design"
      title: "Structural isolation design (freeze substrate for a run's own duration, distinct from the after-the-fact drift detector above): pause-the-puller mutex (recommended default) vs. pinned git worktree per run (for high-value/long-running experiments) vs. rsync snapshot (rejected -- duplicates a documented .git-file-vs-directory trap for no benefit over the worktree option). Designed in section 3; not built."
      phase: 0
      status: open
      severity: medium
      owner_exq: null
      last_updated: 2026-08-03
      completion_note: ""
    - id: "substrate_stability:parse-knobs-file-coverage"
      title: "Teach REE_assembly/scripts/default_off_drift_guard.py's parse_knobs() to follow each REEConfig field(default_factory=XConfig) reference to wherever XConfig is actually declared (an import resolution, not a hardcoded second/third file path), so nested config classes declared outside ree_core/utils/config.py (confirmed: GoalConfig, SerotoninConfig) are no longer invisible to it. Discovered as the real blocker behind P1d's still-0 real-corpus result (section 7.4), not built this session -- a separate, well-scoped follow-on one layer below everything else in this plan."
      phase: 1
      status: open
      severity: medium
      owner_exq: null
      last_updated: 2026-08-03
      completion_note: ""
---

# Substrate Stability + Claim-Drift Detection -- Design Plan

**Status:** Phases 0, 1, AND 1b of the drift detector LANDED (read-only, zero validity risk throughout -- mirrors `arm_reuse_fingerprint_plan.md`'s own Phase-0 posture). Both Phase 1 (section 4.5) and Phase 1b (section 4.6) surfaced real, load-bearing findings against the actual corpus, and both found the SAME result for a DIFFERENT reason: zero noise reduction for the 2 pilot claims. Phase 1 (scope narrowing) is defeated by legitimate dependence on a hub file (`ree_core/agent.py`); Phase 1b (default-off-diff filtering) is defeated by the dominant real pattern in this repo's recent history being new hook METHODS whose flag check lives in a different file's callee, not an in-place conditional in the same changed file -- structurally invisible to a same-file analysis. Neither is a bug in the filters (49 unit tests, including real git-repo fixtures, confirm both work correctly on the patterns they target); both are honest findings about what this codebase's actual change shape is. **P1c is now BUILT and LANDED** (section 6.5): `enabled_default_off_flags`/
`enabled_default_off_flags_for_agents` in `ree-v3/experiments/_lib/manifest_core.py`, wired into
`stamp_recording_core`'s EXISTING `agent=` parameter (no new kwarg needed -- simpler than
originally designed, since that threading already existed for `z_goal_stream`), plus a consumer
`flag_status_from_recorded_config` in `check_substrate_staleness_candidates.py` that `main()`
now prefers over the textual proxy. 30 new tests across both repos. Caught and fixed two real
correctness issues before landing (an omission-vs-empty-dict ambiguity, and a cache keyed on an
assumption that stopped holding once a manifest-specific flag source was added) -- see 6.5 for
both. Confirmed genuinely prospective on the real corpus: 0 of 621 manifests carry the field yet,
since no driver has adopted `agent=` for this reason specifically. **P1d is now BUILT** (section
7.4): a one-hop interprocedural extension (`build_function_index`, `_guard_clause_confirms_inert`,
`_function_is_one_hop_inert`) that follows a changed function's direct callees to find a gate
living in a different file, PLUS a real fix to the shared Kleene evaluator (recognising the
`getattr(obj, "name", default)` gate idiom -- 622 occurrences in `ree_core/`, previously
unrecognised entirely). 25 new tests confirm both work correctly on the exact real-world target
case IN ISOLATION. **Still 0 on the real corpus** -- but for a THIRD, deeper root cause, not a
repeat: `default_off_drift_guard.py`'s `parse_knobs()` (reused as ground truth throughout this
plan) only parses `ree_core/utils/config.py`, and 2 of REEConfig's 10 nested sub-config classes
(`GoalConfig` -- holding the exact flag this case needs -- and `SerotoninConfig`) are declared in
OTHER files, invisible to it entirely. P1c's runtime-introspection recording does not share this
limitation. Flagged as a well-scoped follow-on, not fixed here. The structural-isolation problem
(section 3) is designed but **not built** this session. Phase 2 (section 4.4) remains held
pending a human decision: land P1c into `/queue-experiment` so new
drivers start accumulating coverage, pursue P1d, or accept Phase-0's whole-tree ceiling.
**Created:** 2026-08-03T16:56Z
**Author session:** failure-autopsy-10b982
**Motivation chip:** user question during the V3-EXQ-875 (MECH-471) failure autopsy, 2026-08-03 -- "is there a way that the substrate could be updated as it will be as we develop ree but experiments keep stable substrate across their runs. Experiments should know their substrate build (as in we have versioning or similar for substrate) and updated substrate which is relevant could potentially become a reason to run experiments again?"

---

## 1. Problem statement

V3-EXQ-875 (MECH-471, autopsied same session: `failure_autopsy_V3-EXQ-875_2026-08-03.md`)
ran for ~20.5h wall-clock on `ree-worker-3`. Its manifest recorded
`substrate_stable_across_run: false`: the per-cell process-snapshot substrate hash differed
between its early cells (`strength=0`, hash `e001d2aa...`, 179 files) and its later cells
(`strength=25/50/150`, hash `b1fa9593...`, 181 files). Tracing this: six `ree_core`-touching
commits landed on `ree-v3` `main` during the run's window. It was benign this time (all six
added default-off config flags this experiment's config never enables, confirmed by the
manifest's own bit-identical determinism check across strength arms) -- but nothing
*structural* prevented it. The runner executes each experiment **in place**, inside the same
shared `ree-v3` checkout a co-resident heartbeat/runner loop periodically
`git pull --rebase --autostash`es against `origin/main` -- including while an experiment
subprocess is mid-execution, reading source files live from that same directory tree.

This surfaces two genuinely separate design problems, both raised by the user's question and
both real gaps once checked against what already exists:

1. **Isolation** -- can a single experiment's substrate be frozen for its own run duration,
   so a concurrent `main` commit landing mid-run cannot silently become part of what that run
   measured?
2. **Drift detection** -- once evidence is recorded against substrate S1, and the substrate
   later moves to S2, is there any way to notice that S1->S2 touched files a *specific claim's*
   evidence depended on, so a human can judge whether the claim's evidence should be re-tested?

## 2. What already exists (checked before designing anything new)

Substantial machinery already exists for both problems -- confirmed by reading source, not
assumed:

- **Per-run substrate identity.** `ree-v3/experiments/_lib/arm_fingerprint.py::compute_substrate_hash()`
  hashes the content of `ree_core/**/*.py`, `experiments/_harness.py`, `experiments/_metrics.py`,
  `experiments/_lib/**/*.py` (`_SUBSTRATE_GLOBS`) -- sorted, content-addressed, order-stable.
  It is pure stdlib (`hashlib` + `pathlib`; no `torch`/`numpy` import), so it is cheap to call
  from a lightweight governance-time script, not just from inside a running experiment.
- **Optional dependency-scoping.** The same function accepts a `scope` of author-declared globs,
  narrowing the hash to only the files a specific cell provably executes/reads-a-constant-from.
  `ree-v3/experiments/_lib/substrate_scope_guard.py` PROVES a declared scope is a safe
  over-approximation via two guards (call-trace + static AST data-closure) -- a scope that is
  too narrow trips loudly rather than silently under-hashing.
- **Within-run drift detection.** `arm_fingerprint.substrate_stability_report()` memoizes the
  hash at process start and re-checks it later in the same process, which is exactly what
  produced V3-EXQ-875's `substrate_stable_across_run: false` self-report.
- **A recording standard that makes this comparable across runs.** The Experimental Recording
  Standard's always-core fields (`evidence/planning/experimental_recording_standard_2026-07-12.md`
  section 3b) include a top-level `substrate_hash` and `substrate_commit` on the flat manifest,
  checked by `ree-v3/validate_recording.py`.
- **A claim-evidence staleness GATE that already exists and is already wired into scoring** --
  this was the biggest surprise checking existing infrastructure, and the main reason this plan
  is scoped narrower than the original sketch. `evidence/experiments/scripts/build_experiment_indexes.py`
  (added 2026-06-02, predates the arm-reuse-fingerprint plan) already reads four manually-settable
  manifest fields:
  - `pending_retest_after_substrate: bool` (run-level)
  - `superseded_by_substrate: "<SD-id>@<YYYY-MM-DD>"` (run-level ref string)
  - `pending_retest_after_substrate_per_claim: [claim_id]` (per-claim)
  - `superseded_by_substrate_per_claim: {claim_id: ref}` (per-claim ref)

  A flagged entry stays in the full audit log but is tagged `scoring_excluded="stale_substrate"`
  and does not feed claim confidence/conflict. `/failure-autopsy`'s own artifact schema already
  has a `pending_retest_after_substrate` field per target (used, correctly `false`, in this
  session's V3-EXQ-875 autopsy), and `generate_inter_governance_workset.py` also reads the field,
  so there is a complete path from "someone notices" through to "surfaced on the IGW workset."

**What is missing is narrower than originally scoped: nothing on the "someone notices" side is
automated.** The gate honors these four fields; nothing computes them. A human has to notice
that substrate moved in a way relevant to a specific claim and hand-edit the flat manifest.
That is the actual, confirmed gap this plan's section 4 fills -- a *producer* for fields whose
*consumer* is already built, tested, and live.

## 3. Problem 1 -- structural isolation (designed, not built this session)

| Option | Mechanism | Isolation strength | Cost |
|---|---|---|---|
| **A1 -- pinned git worktree per run** | Runner creates `git worktree add --detach <scratch>/<run_id> <pinned-commit>`, executes the driver there, syncs only the manifest back to the shared checkout on completion | Strong -- byte-identical for the run's whole life, immune to concurrent commits landing on `main` | Disk (one tree copy per in-flight run) + worktree bookkeeping/cleanup (this repo already has a documented orphaned-worktree hazard class to avoid repeating) |
| **A2 -- pause-the-puller mutex (recommended default)** | Before a "needs-stable-substrate" experiment starts, it takes a local lock (a worker-scoped analog of the `coordination_plane.py` pause pattern this session used for its own claim, but scoped to `ree_core/`/`experiments/_lib/` rather than the coordination-data plane); the heartbeat's `git pull --rebase --autostash` step checks the lock and defers while it is held | Strong against *new* drift; does not protect against dirt already uncommitted in the checkout at run start (rare on a worker, since workers do not normally carry live human edits) | Cheapest -- no new directories, no disk cost, a small addition to `experiment_runner.py`'s pull step |
| **A3 -- rsync snapshot per run (rejected)** | Full file copy, the pattern `scripts/remote_pytest.sh` already uses for pytest staging | Strong, sidesteps git-object-store contention on very long runs | Higher disk cost than A1 with no shared object store, and inherits the exact `.git`-file-vs-directory trap `remote_pytest.sh` had to fix (documented in `CLAUDE.md` "Running the test suite") for zero isolation benefit over A1 |

**Recommendation**: A2 as the default (V3-EXQ-875 showed drift is usually benign, and the cost
should match that), reserving A1 for experiments an author explicitly flags as expensive/
critical (long wall-clock, claim-decisive). A3 should not be built -- it is strictly dominated
by A1 for this use case.

**Why this section is not built this session**: it requires a change to
`ree-v3/experiment_runner.py`'s pull step, which is executable-code-plane infrastructure shared
by every worker and the hub, and per this repo's own git policy that class of change should be
staged (an `integration/<slug>` branch, tested on a cloud worker, before merging to `main`) --
not a same-session drive-by edit. Left as an open node (`substrate_stability:ISO-design`) for a
dedicated follow-on.

## 4. Problem 2 -- claim-drift detection (Phase 0 landed this session)

### 4.1 Design

A read-only report script, `REE_assembly/scripts/check_substrate_staleness_candidates.py`:

1. Scan flat claim-tagged manifests under `REE_assembly/evidence/experiments/*.json` (Phase 0
   scope note below on why flat-only).
2. For each with a recorded top-level `substrate_hash` (and, if present, `substrate_commit`):
   fetch `origin/main`, materialise a throwaway detached worktree at it, and call the REAL
   `compute_substrate_hash()` from `ree-v3/experiments/_lib/arm_fingerprint.py` **as found in
   that worktree** (never reimplemented -- reusing the actual function is what guarantees the
   comparison is meaningful, since a subtly different reimplementation could produce a false
   drift signal or a false all-clear).
3. Compare. A mismatch is a **drift candidate**, not an automatic flag -- nothing is written to
   any manifest. If `substrate_commit.commit` is present, additionally run
   `git diff --name-only <recorded-commit>..origin/main -- <the same four globs>` in `ree-v3`
   so the report names exactly which files changed, not just "something changed."
4. Manifests already carrying `pending_retest_after_substrate` / `superseded_by_substrate` (or
   whose `evidence_direction` is already `superseded`) are excluded from "new candidates" and
   reported separately as "already actioned" -- this report should never suggest re-flagging
   something governance has already handled.
5. Manifests with no recorded substrate identity (pre-recording-standard) are bucketed as
   "no substrate identity recorded, cannot assess" -- an honest limitation, not silently
   dropped (per this repo's no-silent-caps convention).
6. Group results by `claim_id` and print a plain-text report. Never writes a file, never
   mutates a manifest -- mirrors `arm_reuse_report.py`'s own Phase-0 posture exactly ("READ-ONLY",
   printed to stdout, run on demand).

### 4.2 Why flat-only, for now

`build_experiment_indexes.py` enumerates evidence from three sources: `*.json` (flat),
`*/*.json`, and `**/runs/**/manifest.json` (the pack -- the historical scoring source for
`arm_results`). Per that module's own comment, `/failure-autopsy` and operators edit the FLAT
file, never `runs/<run_id>/manifest.json` -- the flat file is the human-editable override layer.
Since `pending_retest_after_substrate` is exactly such an override, restricting Phase 0 to flat
manifests matches where a human would actually act on the report. Measured corpus scan
(2026-08-03): 641 flat claim-tagged manifests, 206 carry `substrate_hash`, 58 also carry
`substrate_commit`. A future phase can extend coverage to the `runs/` pack if flat-only proves
to miss too much (tracked as a Phase-1 refinement, not blocking Phase 0).

### 4.3 Noise control already built in, without needing new schema

The whole-tree default (`_SUBSTRATE_GLOBS`) is already `ree_core/**` + a handful of
`experiments/_lib`/`_harness`/`_metrics` files -- not the whole repo, so it does not fire on
every `experiments/v3_exq_*.py` driver addition or planning-doc edit the way a naive whole-repo
hash would. This keeps Phase 0's false-positive rate lower than the original worry in the design
sketch. No per-claim `substrate_scope` schema addition was needed to make Phase 0 useful; that
remains a real Phase-1 refinement (narrowing further, and filtering default-off-only diffs) but
is not a prerequisite for a first, honest, whole-tree-scoped report.

### 4.4 Phased rollout

- **Phase 0 (done)**: instrument-only report, run manually, zero validity risk, no schema
  change, no automatic flagging. Purpose: measure how noisy whole-tree drift detection actually
  is against the real corpus before committing to anything more automated. Result: ~93% of
  evaluable manifests read as "differs" -- too noisy to act on directly.
- **Phase 1 (done)**: optional per-claim `substrate_scope` in `claims.yaml` (reusing the exact
  glob format + `substrate_scope_guard`'s conservatism vocabulary already built for arm
  fingerprints -- author-declared here, not machine-proven the same way), narrowing the
  detector from whole-tree to declared scope per claim. Landed and unit-tested; real-corpus
  result in section 4.5 below.
- **Phase 1b (done)**: a changed file whose diff is confined to code reachable only under a
  still-default-off flag this run's driver never references downgrades to an informational
  note, not a candidate. Landed and unit-tested (26 tests incl. a real 2-commit git fixture);
  real-corpus result in section 4.6 below -- again zero reduction, for a different and equally
  real reason than Phase 1's.
- **Phase 2 (open, status uncertain -- see section 4.6's closing note)**: surface flagged
  candidates somewhere a human actually reads every cycle -- either a `pending_review.md`-style
  derived report, or an IGW workset item (reusing the workset generator's existing
  `pending_retest_after_substrate` read path). Never auto-requeues a re-test -- matches the
  interactive-governance philosophy used everywhere else in this repo. Originally gated on
  "Phase 1b proving low noise"; Phase 1b did not, so proceeding to Phase 2 now would surface a
  0%-actionable signal every cycle -- exactly the alarm-fatigue failure mode this repo's own
  NOTE-vs-finding conventions (`audit_vendored_copies.py`, `audit_worktree_skills.py`) exist to
  avoid. Held pending a human decision (section 4.6).

### 4.5 Phase 1's real-corpus result (the honest finding, not the hoped-for one)

Two pilot claims were scoped from an actual read of their own dependencies, not guessed:
`MECH-471` (from this session's own V3-EXQ-875 autopsy root-cause read of the
`_train_all_on_agent`/SD-070/SD-056 acquisition path) and `MECH-321` (from the claim's own
`implementation_note` naming its substrate and two wiring call sites). Running
`check_substrate_staleness_candidates.py` against the real corpus with both scopes declared:

```
claims with a declared substrate_scope: 2 (MECH-321, MECH-471)
...
    0  (claim, run) pair(s) filtered OUTSIDE a declared substrate_scope (Phase 1)
```

**Zero candidates were filtered for either pilot.** Both claims correctly declare a dependency
on `ree_core/agent.py` -- and `agent.py` is a genuine hub file: roughly half of the last 20
substrate-touching commits on `ree-v3` `main` touch it (SD-091, SD-092, SD-093, MECH-203,
MECH-122, ARC-071/MECH-090, MECH-324, MECH-217, MECH-321 itself, ...), because it is where
every new mechanism wires into the live agent loop. So a scope that honestly includes
`agent.py` -- which it must, for either claim -- inherits nearly all of `agent.py`'s churn as
"in scope," regardless of how tightly everything else in the declared scope is drawn.

This is not a bug in the scope-matching logic (verified separately by 9 unit tests plus a
controlled end-to-end fixture where the filter does correctly exclude an out-of-scope file);
it is a real property of the substrate. **Scope narrowing alone cannot help a claim that
legitimately depends on a hub file** -- the noise in `agent.py`'s diff is not "irrelevant
files," it is irrelevant *changes to a relevant file* (a new default-off flag another claim's
work added). That is exactly what Phase 1b is for, and why it is now the load-bearing next
step rather than "declare scope for more claims": more scope declarations would not have
changed this result for any claim that also, correctly, depends on `agent.py` (or another hub
file such as `ree_core/goal.py`, `ree_core/utils/config.py`).

### 4.6 Phase 1b's real-corpus result -- a DIFFERENT limitation, same empty answer

Running the extended script with default-off filtering enabled against the same 2 pilots:

```
   317  default-off knob(s) known
     0  (claim, run) pair(s) filtered as DEFAULT-OFF ONLY (Phase 1b)
```

**Zero pairs filtered again -- but for a genuinely different reason than Phase 1's, not a
repeat of it.** Traced to the actual recent commit dominating `agent.py`'s diff for both
pilots: SD-092's `notify_subgoal_attainment` (`ree_core/agent.py:8810`). Its own docstring says
plainly: "`use_hierarchical_goal_credit` is False -- `GoalState.credit_subgoal_attainment`'s own
gate (default -> bit-identical; not duplicated here so the flag has one source of truth)." The
method itself contains NO `if use_hierarchical_goal_credit:` anywhere -- it unconditionally
calls into `ree_core/goal.py`'s `credit_subgoal_attainment`, which does the gating. So the new
lines added to `agent.py` are not wrapped in an inert `if` block in the file where they appear;
they are a new, always-present hook whose downstream EFFECT is gated one file away. Phase 1b's
same-file AST analysis, by construction, cannot see across that call boundary -- and this is
the DOMINANT shape of this repo's actual recent default-off additions (a new hook method +
call-site wiring, not an in-place conditional retrofit onto existing code), not an edge case.

**Two lessons, not one, and they compound rather than duplicate:**
1. Phase 1 (scope) fails when a claim legitimately depends on a hub file, because the hub file
   is genuinely relevant and narrowing scope cannot un-relevant it.
2. Phase 1b (default-off) fails EVEN WHEN a hub file's change really is behaviourally inert for
   a given claim's config, because the inertness is expressed via a call into another file's
   gate rather than an in-place conditional in the file that changed.

Both filters are correct and tested for the pattern each targets (49 total unit tests across
both, including real git-repo fixtures demonstrating each filter firing on a constructed
positive case). Neither pattern is what this codebase's actual recent history looks like for
its two most-tested pilot claims. **This is not evidence the filters are broken; it is evidence
that "confined to one file's in-place conditional" is too narrow a definition of inert for a
codebase whose convention is new-hook-plus-callee-gate**, and closing that gap needs either (a)
interprocedural reachability analysis (trace whether a call chain from a changed line
ultimately bottoms out at a confirmed-disabled flag check in ANY file it reaches -- a real
static-analysis undertaking, not a governance-script afternoon), or (b) actually running the
code path (the same class of solution `arm_fingerprint`'s call-trace guard already uses for a
different problem), or (c) accepting Phase 0's whole-tree report as the practical ceiling for
hub-file-dependent claims and leaning on human judgment at that granularity instead.

**Recommendation, not a decision this plan makes unilaterally**: hold Phase 2 rather than wire
a 0%-actionable-so-far signal into a cycle a human reads regularly. Whether to pursue (a), (b),
or (c) above is a real design fork worth a deliberate choice, not a default continuation.

## 5. Explicitly out of scope (this plan)

- Any change to `ree-v3/experiment_runner.py`'s git-pull behaviour (section 3's isolation design
  is deliberately left unbuilt this session -- see rationale there).
- Any automatic write of `pending_retest_after_substrate` / `superseded_by_substrate` -- the
  detector only ever reports; a human (governance) makes the call and edits the flat manifest,
  exactly as `/failure-autopsy` already does today for other reasons.
- Retro-fitting historical manifests with no recorded `substrate_hash` into comparability --
  matches `arm_reuse_fingerprint_plan.md` section 6's identical exclusion for the same reason
  (no substrate hash exists for them; unsafe to assume one).
- Cross-`machine_class` drift comparison -- Phase 0 compares content hashes only, not runtime
  behaviour across machine classes; that is `arm_reuse_fingerprint_plan.md`'s Regime B, a
  separate and harder problem.

## 6. Prospective-only recording of enabled default-off flags (P1c, designed 2026-08-03)

### 6.1 What it fixes, and what it does NOT fix

Phase 1b's `flag_status_from_driver_source` is a textual proxy: a flag is "confirmed disabled"
only if its name never appears anywhere in the driver source, because a bare substring hit
cannot distinguish "sets it True" from "sets it False" from "mentioned in a comment." This
recording feature replaces that proxy with the RUN'S ACTUAL `REEConfig` field values, recorded
at manifest-write time. It removes the "is this flag really off" uncertainty. **It does NOT, by
itself, solve section 4.6's finding** (a gate living in a different file than the one that
changed) -- that is a reach problem (can the analysis find the gate at all), not a precision
problem (is the value known for certain). The two are complementary; see section 7.

### 6.2 Why this is prospective-only, structurally, not by choice

Researched before designing (not assumed): no REEConfig object flows through the manifest-write
path today. `ree-v3/experiments/pack_writer.py:366` `write_flat_manifest(..., config=None, ...)`
and `ree-v3/experiments/_lib/manifest_core.py:430` `stamp_recording_core(..., config=None, ...)`
both type `config` as `Mapping[str, Any]` and forward it into the JSON verbatim -- it is the
driver's own experiment-level dict (env params, hyperparameters, schedule), never a live
REEConfig instance. `REEConfig` is constructed **inside** each driver (confirmed:
`v3_exq_875_...py:244`, `v3_exq_867a_...py:300`, both call `REEConfig.from_dims(...)` in a
per-cell helper), and of 1252 `experiments/v3_exq_*.py` drivers, **1072 construct their own
REEConfig directly**; only 11 use the shared `_train_all_on_agent` helper, which itself never
builds one. So there is no single choke point to retrofit -- adoption is necessarily per-driver
and opt-in, which is exactly what makes this prospective: a driver that already ran and wrote
its manifest cannot retroactively gain a field it never computed, and most drivers discard their
REEConfig/agent per cell once the result dict is built, so there is nothing left to introspect
after the fact even for a driver willing to adopt this today.

### 6.3 Design -- generalizing an existing pattern, not inventing one

`ree-v3/experiments/_lib/q081_profile.py` already does almost exactly this, for a hand-curated
flag list: `_read_flag(cfg, name)` (line 176) checks `cfg`, `cfg.latent`, `cfg.hippocampal`,
`cfg.goal` in turn for the named attribute, and `q081_substrate_declaration(config=None)`
(line 189) builds a `non_default_substrate` manifest block recording each flag's
`stock_default`/`profile_value`/`effective_value`. Called as
`q081_substrate_declaration(agent.config)` at `v3_exq_838_...py:512` -- proof the "thread
`agent.config` to manifest-build time" pattern already works in this codebase.

The new helper generalizes this from a hand-curated list to ALL default-off knobs
`default_off_drift_guard.parse_knobs()` already enumerates, and from a hardcoded holder list to
a recursive walk (`_read_flag`'s four hardcoded holders miss any current or future nested
sub-dataclass not on that list):

```python
def record_enabled_default_off_flags(config, knob_names: set[str]) -> dict[str, Any]:
    """{flag_name: actual_value} for every knob_names entry whose live value differs from its
    coded default -- i.e. was actually enabled for this run. Recurses into nested dataclass
    fields (config.latent, config.hippocampal, ...) generically via dataclasses.is_dataclass(),
    not a hardcoded holder list (q081_profile.py's _read_flag names exactly four; a fifth
    sub-config added later would silently miss every flag on it under that approach)."""
```

Wiring: an optional `config_obj=` kwarg on `stamp_recording_core`/`write_flat_manifest`
(additive, non-breaking, matches how `agent=`/`z_goal_stream_stats` were already added there) --
a driver that still holds its final `agent`/`config` at manifest-build time passes it and gets
the new field; one that has already discarded it (the common case today) gets nothing, exactly
as before. First real adoption should be **new** drivers authored via `/queue-experiment` going
forward (update that skill's template to call the helper when the driver's own design keeps a
live config reference), not a retrofit of the 1072 existing ones.

### 6.4 Consumer-side change (small)

`flag_status_from_driver_source` gets a sibling `flag_status_from_recorded_config(manifest,
knob_names)` reading the new field when present; `main()` prefers it and falls back to the
textual proxy when absent -- so old manifests keep today's (weaker) proxy behaviour and new,
adopting manifests get exact flag-status resolution, with no change to the Kleene evaluator
itself (it already accepts a `flag_status: Dict[str, bool]` regardless of source).

### 6.5 Built and landed (2026-08-03) -- simpler than designed, plus a real bug caught

Turned out **simpler** than 6.3 anticipated: `write_flat_manifest`/`stamp_recording_core`
*already* threads an `agent=` parameter through for the `z_goal_stream` block (added earlier,
2026-07-something, for a different reason -- see that block's own docstring). No new
`config_obj=` kwarg was needed at all; `enabled_default_off_flags_for_agents(agent)` just reads
`.config` off whatever `agent` the caller already passes, so a driver adopting this needs to
change *nothing* about how it calls the writer -- if it already passes `agent=` for
`z_goal_stream` (roughly 28 of 565 stepping drivers today, per that block's own docstring
count), it gets this field automatically, immediately, no opt-in step at all.

**Caught a real precision gap while writing the consumer-side test, before landing.** The
first draft copied `z_goal_stream`'s "omit the block when there is nothing to report"
convention verbatim. For `z_goal_stream` that is safe (its stats are never all-zero unless
genuinely unmeasured). For THIS field it is not: "agent given, nothing enabled" is an
extremely common, entirely legitimate outcome (an all-defaults run), and omitting it made that
case indistinguishable from "no agent was ever given" -- exactly the ambiguity this feature
exists to remove. Fixed before landing: the helper returns `None` (omit) only when no
config-bearing agent was found at all, and an actual dict -- possibly `{}` -- otherwise. Caught
by writing the consumer test first (`flag_status_from_recorded_config` needs to tell these two
apart to correctly say "every other knob is confirmed disabled"), not by re-reading the code.

**A second correctness issue surfaced wiring the consumer into `main()`**: the existing
`default_off_cache` (Phase 1b) is keyed by `(commit, experiment_type, path)`, which is only a
valid cache key when `flag_status` is a pure function of that key -- true for the driver-source
proxy (same source, same commit+type), **false** for the recorded config, which is specific to
one manifest's own run (two arms of the same `experiment_type` at the same commit could
genuinely differ). Fixed by routing recorded-config lookups around that cache entirely rather
than risk a stale cross-manifest hit -- correctness over the (currently negligible, since no
manifest has this field yet) performance cost.

Real corpus run confirms the prospective framing precisely: **0 of 621 manifests carry the new
field**, so 0 pairs used it -- not a null finding the way Phase 1/1b's real-corpus results were,
just the expected state of a feature that has not been adopted by any driver yet. Landing it
into `/queue-experiment`'s template so *new* drivers start passing `agent=` is the natural next
step, and is what would actually start accumulating coverage -- not done this session.

## 7. One-hop interprocedural extension to Phase 1b (P1d, designed 2026-08-03, higher risk)

### 7.1 The gap this closes

Section 4.6's actual finding: `notify_subgoal_attainment` (`ree_core/agent.py:8810`)
unconditionally calls `self.goal_state.credit_subgoal_attainment(...)`; the
`use_hierarchical_goal_credit` gate lives entirely inside `GoalState.credit_subgoal_attainment`
in `ree_core/goal.py`, by the method's own docstring ("not duplicated here so the flag has one
source of truth"). A same-file AST walk cannot see this. Closing it needs the analysis to
follow at least one function call outside the changed file.

### 7.2 Design sketch -- deliberately narrow, not general call-graph analysis

For a changed function `F` whose body is not itself gated (per Phase 1b's existing check):
1. Restrict to the case where `F`'s body consists ENTIRELY of simple statements plus calls (no
   other logic) -- a narrow, checkable precondition, not "any function."
2. For each `Call` in `F`'s body, resolve a candidate target by NAME ONLY (the called
   attribute/function name, e.g. `credit_subgoal_attainment`) -- true type-directed resolution
   (knowing `self.goal_state`'s static type) is real static analysis this script's stdlib-only,
   no-torch posture cannot support cheaply.
3. Search every `.py` file in the current substrate globs for a function/method definition
   matching that name. **Conservative by construction, mirroring Phase 1b's own safety rule**:
   if more than one candidate definition exists anywhere in scope, ALL of them must
   independently resolve to a confirmed-inert top-of-body gate (via the SAME
   `_eval_flag_formula`/Kleene logic already built) for the call to count as inert; if even one
   candidate is ungated or unresolvable, treat the whole call -- and therefore `F` -- as NOT
   confirmed inert. A wrong resolution must fail toward "stays a candidate," never toward a
   false all-clear.
4. `F` is inert only if EVERY call in its body resolves this way (an AND across calls, same
   safety direction as everything else in this plan).

### 7.3 Why this is scoped as higher-risk and not committed yet

Name-based resolution is a real approximation: two unrelated classes with a same-named method
(`step`, `reset`, `close` are common enough) would force "ALL candidates must agree," which
could make the filter over-conservative to the point of rarely firing -- the opposite failure
mode from a false all-clear, but still worth measuring before investing further. Recommend
prototyping against the SAME two pilot claims' actual candidates (a small, known corpus) before
generalizing, rather than building it corpus-wide on faith. Complementary to, not blocked by,
section 6 -- P1c sharpens `flag_status` regardless of which file the gate lives in; P1d extends
WHERE the gate can be found, for whichever flag-status source (proxy or recorded) is in use.

### 7.4 Built, tested, and correct for its target shape -- STILL 0 on the real corpus, for a
### third and deeper reason (2026-08-03)

Built as designed: `build_function_index()`, `_has_disqualifying_side_effect()` (found and
fixed a real bug during testing -- a naive `ast.walk`-based scope exclusion only skips the
nested `FunctionDef` node itself, not its descendants, since `ast.walk` flattens across scope
boundaries regardless; fixed with a proper `ast.iter_child_nodes` recursion that never
descends into a nested def/lambda/class), `_guard_clause_confirms_inert()`,
`_function_is_one_hop_inert()`, `one_hop_inert_line_ranges()`. Also fixed, in the SAME pass, a
real gap in the Kleene evaluator this extension (and Phase 1b) both depend on: `getattr(obj,
"name", default)` -- the DOMINANT gate idiom in `ree_core/` (622 occurrences measured), not an
edge case -- was not recognised as a flag reference at all before this session; now is. 25 new
unit tests, including the ACTUAL real-world case (`notify_subgoal_attainment` calling
`credit_subgoal_attainment` across two files) as a positive control, confirmed working IN
ISOLATION.

**Running it against the real corpus: still 0 pairs filtered for either pilot.** Debugged
directly rather than accepted at face value. `use_hierarchical_goal_credit` -- the exact flag
`credit_subgoal_attainment`'s guard clause tests -- resolves as **Unknown**, not
confirmed-False, for the MECH-471 candidate. Traced to a THIRD, deeper root cause, one layer
below everything built this session: `default_off_drift_guard.py`'s `parse_knobs()` -- reused
unmodified throughout this whole plan as the source of truth for "what is a default-off knob"
-- only parses `ree_core/utils/config.py`. `GoalConfig` (which declares
`use_hierarchical_goal_credit`) is defined in `ree_core/goal.py`, a completely different file,
and is only *used* by `config.py` as a nested field (`goal: GoalConfig =
field(default_factory=GoalConfig)`). `parse_knobs()`'s AST walk never reads `goal.py`, so this
flag -- and every other field `GoalConfig` declares -- is invisible to it entirely, not merely
unresolved. Confirmed the scope of this precisely: **exactly 2 of REEConfig's 10 nested
sub-config classes** (`GoalConfig`, `SerotoninConfig`) are declared outside `config.py`; the
other 8 (`LatentStackConfig`, `E1Config`, `E2Config`, `E3Config`, `HippocampalConfig`,
`ResidueConfig`, `HeartbeatConfig`, `EnvironmentConfig`) are declared directly in it and are
correctly covered.

**This is a real, bounded gap in infrastructure this plan has treated as ground truth, not a
bug in anything built this session** -- `default_off_drift_guard.py` predates this plan
entirely (it is the tool `_default_off`/`Knob` etc. were deliberately reused from, per this
plan's own "never reimplement" principle throughout). Worth naming precisely for whoever picks
it up: fixing it means teaching `parse_knobs()` to follow each `field(default_factory=XConfig)`
reference to wherever `XConfig` is actually declared (via an import resolution, not another
hardcoded file list), not just adding `goal.py`/`serotonin.py` as two more hardcoded paths --
REEConfig could grow an 11th nested config in a third location tomorrow.

**Notably, P1c does NOT share this limitation.** `enabled_default_off_flags()` (section 6)
walks the LIVE dataclass structure at runtime via `dataclasses.fields()`, which correctly
reaches every nested sub-config regardless of which file declares its class -- the AST-parse
vs. runtime-introspection distinction is exactly what makes P1c's producer side more complete
than Phase 1b/1d's consumer-side flag enumeration, a real asymmetry worth knowing about rather
than assuming the two "know about the same flags."

**Even fixing this would likely not fully close the gap.** Debugged one level further: of the
236 changed lines in `ree_core/agent.py` for the MECH-471 candidate, `use_coalition_controller`
(SD-091's flag, declared directly in `config.py`) DOES resolve correctly (confirmed False), yet
183 of 236 lines remain uncovered even so. Reading the diff: some of SD-091's own consumer
sites gate not on a direct flag read but on a CACHED STATE CHECK derived from it at
initialization time -- `if self.coalition is not None:` -- which is a *proxy* for the flag
(`self.coalition` is only ever non-`None` when `use_coalition_controller` was true at
`__init__`), not a reference to the flag itself. No analysis built this session recognises
this pattern; doing so would need actual data-flow tracking (does this attribute's value
trace back to a confirmed-disabled flag at every assignment site), a materially harder problem
than anything attempted here, and not recommended as a next step without first fixing the
narrower `parse_knobs()` gap above and re-measuring what's actually left.

**Net assessment**: both fixes built this session (getattr recognition, one-hop resolution)
are real, correct, and independently useful -- the getattr fix in particular retroactively
improves Phase 1b for any future candidate whose gate uses that idiom in-file. Neither changes
today's practical result for the 2 pilots, because the actual blocker turned out to be one
layer further down the stack (which flags are even known to exist) than either fix addresses.
Flagged, not fixed: extending `parse_knobs()`'s file coverage is a well-scoped, separate
follow-on with a clear owner and a clear test (does `use_hierarchical_goal_credit` newly
resolve).

## Status table

| Gap | Phase | Status | Blocking on | Next action | Owner-EXQ | Last updated |
|---|---|---|---|---|---|---|
| P0-detector | 0 | done | -- | none; run on demand via `/opt/local/bin/python3 scripts/check_substrate_staleness_candidates.py` | null | 2026-08-03 |
| P1-scope-schema | 1 | done | -- | none; 2 pilot claims declared (MECH-471, MECH-321). Real corpus result: 0/2 pilots' candidates filtered -- see section 4.5 | null | 2026-08-03 |
| P1b-default-off-filter | 1 | done | -- | none; real corpus result: 0/2 pilots' candidates filtered, for a DIFFERENT reason than P1 (same-file conditionals aren't this repo's actual pattern -- see section 4.6) | null | 2026-08-03 |
| P1c-prospective-recording | 1 | done | -- | none; 0 of 621 manifests carry the field yet (genuinely prospective) -- next real step is updating /queue-experiment's template so new drivers pass agent= for this reason | null | 2026-08-03 |
| P1d-interprocedural-hop | 1 | done | -- | none; real corpus result: still 0/2 pilots' candidates filtered, for a THIRD reason (default_off_drift_guard.py's parse_knobs() misses config classes declared outside config.py) -- see section 7.4 | null | 2026-08-03 |
| parse-knobs-file-coverage | 1 | open | Section 7.4's finding | Teach default_off_drift_guard.py's parse_knobs() to follow field(default_factory=XConfig) to wherever XConfig is actually declared, not a hardcoded single-file scan | null | 2026-08-03 |
| P2-governance-surface | 2 | open | P1c accumulating real coverage (needs new/re-run drivers), and/or the parse_knobs file-coverage fix landing with a re-measured result | Do NOT wire a 0%-actionable signal into a regular human-facing cycle by default; get a decision first | null | 2026-08-03 |
| ISO-design | 0 | open | A dedicated follow-on session (executable-code-plane change to `experiment_runner.py`, needs `integration/<slug>` staging per this repo's git policy) | Build option A2 (pause-the-puller mutex) behind a flag, test on a cloud worker before merging to `main` | null | 2026-08-03 |
