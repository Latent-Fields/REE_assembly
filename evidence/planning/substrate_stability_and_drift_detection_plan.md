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
    - id: "substrate_stability:ISO-design"
      title: "Structural isolation design (freeze substrate for a run's own duration, distinct from the after-the-fact drift detector above): pause-the-puller mutex (recommended default) vs. pinned git worktree per run (for high-value/long-running experiments) vs. rsync snapshot (rejected -- duplicates a documented .git-file-vs-directory trap for no benefit over the worktree option). Designed in section 3; not built."
      phase: 0
      status: open
      severity: medium
      owner_exq: null
      last_updated: 2026-08-03
      completion_note: ""
---

# Substrate Stability + Claim-Drift Detection -- Design Plan

**Status:** Phases 0, 1, AND 1b of the drift detector LANDED (read-only, zero validity risk throughout -- mirrors `arm_reuse_fingerprint_plan.md`'s own Phase-0 posture). Both Phase 1 (section 4.5) and Phase 1b (section 4.6) surfaced real, load-bearing findings against the actual corpus, and both found the SAME result for a DIFFERENT reason: zero noise reduction for the 2 pilot claims. Phase 1 (scope narrowing) is defeated by legitimate dependence on a hub file (`ree_core/agent.py`); Phase 1b (default-off-diff filtering) is defeated by the dominant real pattern in this repo's recent history being new hook METHODS whose flag check lives in a different file's callee, not an in-place conditional in the same changed file -- structurally invisible to a same-file analysis. Neither is a bug in the filters (49 unit tests, including real git-repo fixtures, confirm both work correctly on the patterns they target); both are honest findings about what this codebase's actual change shape is. The structural-isolation problem (section 3) is designed but **not built** this session. Phase 2 (section 4.4) is designed but not built; given two independent filters have now both come up empty on real data, Phase 2 should not proceed until a human decides whether a THIRD lever (interprocedural reachability, or recording actual REEConfig values prospectively) is worth building, or whether whole-tree Phase-0 reporting is simply the ceiling for this approach on hub-file-dependent claims.
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

## Status table

| Gap | Phase | Status | Blocking on | Next action | Owner-EXQ | Last updated |
|---|---|---|---|---|---|---|
| P0-detector | 0 | done | -- | none; run on demand via `/opt/local/bin/python3 scripts/check_substrate_staleness_candidates.py` | null | 2026-08-03 |
| P1-scope-schema | 1 | done | -- | none; 2 pilot claims declared (MECH-471, MECH-321). Real corpus result: 0/2 pilots' candidates filtered -- see section 4.5 | null | 2026-08-03 |
| P1b-default-off-filter | 1 | done | -- | none; real corpus result: 0/2 pilots' candidates filtered, for a DIFFERENT reason than P1 (same-file conditionals aren't this repo's actual pattern -- see section 4.6) | null | 2026-08-03 |
| P2-governance-surface | 2 | open | A human decision (section 4.6): pursue interprocedural analysis, real-flag recording (prospective-only), or accept Phase-0 whole-tree as the practical ceiling for hub-file claims | Do NOT wire a 0%-actionable signal into a regular human-facing cycle by default; get a decision first | null | 2026-08-03 |
| ISO-design | 0 | open | A dedicated follow-on session (executable-code-plane change to `experiment_runner.py`, needs `integration/<slug>` staging per this repo's git policy) | Build option A2 (pause-the-puller mutex) behind a flag, test on a cloud worker before merging to `main` | null | 2026-08-03 |
