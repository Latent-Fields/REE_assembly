# Detector False-Positive Campaign — staged design

**Status: AWAITING USER REVIEW** (presented live in session cycle-review-20260830-d2, user present)
**Skill:** /metaworker-learning · **Campaign chip:** chip-20260829-metaworkerlearning-detector-falsepositive-campaign
**Research:** three parallel subagents (full reports in the session transcript), 2026-08-30.

## The finding — one meta-pattern, but only for three of five classes

The suspected shared root ("predicates assume the pre-2026-08-28 write topology") holds for
classes 2-partial, 4, and weakly 3 — the honest statement is: **detectors that read "no local
git trace / no per-commit declaration" as evidence of loss or abandonment now live in a
topology where durable state routinely sits outside the local git view** (coordinator DB,
dispatcher runtime files, another box's disk). Classes 1 and 5 arrived in the same batch but
have unrelated roots (load-latency timeout classification; live-environment reads in tests).
They are NOT one root cause; each fix below is narrow and separately argued.

## Class-by-class: root cause → proposed fix → held-out check

### 1. chip-hookgating-* (9 chips, all in ONE 11.25h window, 2026-08-28/29)
**Root cause (mid-copy hypothesis REFUTED):** all 19 live findings across 8 chips were
5-second HANGs (zero exit-2 blocks, zero non-zero exits) — the hygiene tick tightened the
auditor's per-call timeout 20s→5s, and under that night's measured load 6.8-8.3 (unmutexed
parallel corpus runs, since mutexed) process-spawn latency stochastically exceeded 5s. Failing
sets differed every time (8 distinct digests); both GENUINE historical incidents (2026-08-15
exit-2 kill-switch; 2026-08-22 deterministic long-run) had the opposite signature. Zero
recurrences in the 25h after the load event. Baseline now: full 45-check audit = 1.84s.
**Fix (Proposal A):** `--confirm-live` in audit_hook_gating.py — on a live finding, re-run
that one hook×canary at the 20s timeout; report only if the retry also fails; store both
results. Hygiene tick passes the flag, and applies the same retry to the 90s outer-bound
wedge branch (the healer's re-run measured 2.68s). Latent structural check untouched.
**Held-out (4):** the 8-chip family → suppressed; the wedged chip → suppressed; 2026-08-15
kill-switch → STILL FIRES (deterministic exit 2, also caught by latent check); 2026-08-22
substring-fires-suite → STILL FIRES (fails the 20s retry deterministically).

### 2. chip-strandedwt-* (74 chips, FP rate ≥85%, ~4-6 genuine rescues)
**Two distinct FP modes:** (a) cutover mode — the safety test is whole-file blob identity vs
origin/master, which structurally cannot pass for a stale TASK_CLAIMS/TASK_CHIPS diff whose
rows are durably in the coordinator render (2 pure + 2 mixed confirmed FPs); (b) scratch-set
drift — the cloud-4 trio were dispatcher runtime files (`.worker_turn_*.md`,
`.worker_turns.jsonl`) not in METAWORKER_SCRATCH_FILES, already withdrawn by the Orchestrator
with an explicit handoff to this campaign. Historically (b)-type drift caused 38/61 of all FPs.
**Fix (a):** registry row-subsumption — for ` M TASK_CLAIMS.json`/`TASK_CHIPS.json` entries,
structural per-row compare against the live canonical copy (claims keyed (session_id,
claimed_at), chips by chip_ref); suppress ONLY when every worktree row exists live in an
equal-or-later state (status monotone, equal-or-later resolved_at/closed_at, notes preserved);
any unique row, field regression, or parse failure keeps the flag. Mechanizes the hand recipe
in cloud5_stale_scripts_wedge_staged_20260814.md §5-6.
**Fix (b):** add `.worker_parked.json` + `.worker_turns.jsonl` to the scratch set, a pattern
predicate for `.worker_turn_<epoch>.md`, and treat a present `.worker_parked.json` as live.
**Held-out (3):** the 2026-08-30 genuinely-stranded WORKSPACE_STATE commit → STILL FIRES
(non-registry path); abc2aefce4a2 (8 rows all subsumed) → suppressed; **the trap**: the
2026-08-15 audit's 15-of-33 genuinely-stranded registry rows + the amend-hollow-ack dropped
completion_note → STILL FIRE under per-row compare (and pin why a blanket basename
suppression is forbidden).

### 3. chip-staleclaim-* on the Orchestrator lease (10 chips, each a manual Healer review)
**Root cause (cutover mostly a RED HERRING):** dispatcher_control.json lease grants still land
as ordinary named commits, and TASK_CHIPS.json was already neutralized via SHARED_BASENAMES.
Actual drivers: (1) `mac_dispatch_load.json` — a machine-local untracked-by-design scratch
file named as a claim resource: dirty on the Mac (→ bucket D), missing on a cloud Healer box
(→ bucket C), explaining the observed C↔D flapping; (2) bucket L (the lease-liveness verdict)
is computed only inside the `_looks_landed` branch, structurally unreachable from C and D.
**Fix:** hoist the `_orchestrator_lease_signal` check ahead of the evidence chain (a live,
renewed, unexpired lease matched on requested_by == session_id buckets the claim L regardless
of evidence); exclude machine-local untracked scratch (small named set) from attributable/
missing/dirty with a printed warning. **Widens NO reaping** — apply_autoclose touches only
A/G/P; L stays report-only; absence of a lease signal changes nothing (heartbeat-stale-not-
abandoned respected).
**Held-out (3):** the 07:24Z C-verdict while lease commits were landing → old C, new L;
orchestrate-20260828-1940 after its session genuinely ended (lease lapsed) → STILL reported
C/D, correctly; **the -budgetcap trap**: orchestrate-labeled claim with no lease of its own
whose work genuinely never landed → C was CORRECT and the requested_by match keeps it C
(pins why "any orchestrate label + any lease" would be wrong).

### 4. chip-statusregress-* (52 lifetime chips, 100% FP, zero repairs ever)
**Root cause:** "declared" requires a per-ref `chips-mutated:` trailer or a per-mutation
subject — but post-cutover every coordinator-plane mutation reaches git only inside the
materializer's batch commit (empty body, generic subject), so no coordinator-mediated release
can ever be declared.
**Fix (ii of three evaluated):** on materializer-authored commits (subject
`^phase2b-registry: materialize`, author REE Automation (Hub)), treat claimed_by/resolved_at
CLEARS as declared (recording suppressed clears in the finding meta), but KEEP the
status-fallback arm — a terminal→open transition has no legitimate coordinator pathway, so on
a materializer commit it means DB corruption and must still fire.
**The suggested claim_note heuristic is REJECTED on evidence:** in the genuine 58d2532e
stale-snapshot sweep, the clobbered row's claim_note was REPLACED with the older epoch's
different, non-empty note — the heuristic reads exactly the incident class it exists to catch
as "declared". Fix (iii) (live-DB verification) collapses into (ii) for materializer commits
while adding a network dependency to a 5-min tick.
**Held-out (7-case table, agent report):** 3 FP classes flip to suppressed; 58d2532e,
f34963462f's resolve-revert, and 60a8d779cd (the one catch that led to a real repair) all
STILL FIRE (client-authored commits); one named residual blind spot (DB-side claim-wipe whose
only manifestation is a render) accepted and stated, partially covered by the kept status arm
+ the coordinator drift log.

### 5. Non-hermetic tests — ALREADY FIXED AND LANDED (REE_Working e21fd84d0)
Cooldown env injection (verified green under the currently-live cooldown), a real on-disk
`claude` shim replacing argv fakery macOS ps sees through, and a realpath fix for /var→
/private/var aliasing (a deterministic fixture bug, NOT an lsof flake — healer classification
corrected). 175 tests green. Test changes, not standing rules — landed without the gate.

## Residuals recorded, deliberately not built here
- statusregress DELETION blindness: f34963462f's 7-row destructive delete is invisible today
  and under every fix shape — needs its own arm with materializer aged-out-retention scoping.
- hygiene tick hookgating wedge-branch comment (90s bound rationale empirically wrong).
- sync_worktree_settings non-atomic worktree copy (un-evidenced hazard, two-line hardening).
- batch-flaky test_session_startup_checklist (passes standalone 17/17; parallel-runner
  contention; no cross-run mutex angle left — lives with the corpus runner).

## Counterweight (stated per GOV-HELDOUT-1)
The held-out checks above cost three subagent research passes (~570k tokens) and the fixes add
predicate complexity to three load-bearing detectors. The alternative — keep manually
triaging ~2-5 FP chips/day — costs a Healer review each and trains readers to ignore the
detectors, which is how a guard gets disabled. The trade favors building, but the four
detector fixes are each incident-scoped where stated, not general principles.
