# Consolidated Update Plan — 2026-08-30

**Status:** plan-of-record (user-requested). **Author:** session `cycle-review-20260830`.

## Progress ledger (updated 2026-08-30T09:25Z, same session + science-front peer)

**DONE by the ops session (`cycle-review-20260830`):** C.0 corpus pins re-pinned (ree-v3
`aeb3a566b8` — commit gate unblocked fleet-wide); C.2 chip_ledger fail-open loss fix, consumer
half + docs (`68fd89a41b`-adjacent, `e8288a2872`); C.4 task_claim stale-arbitration fix
(`68fd89a41b`); D.3 cloud-5 healer deployed (IN-SYNC); D.4 ree-git-sync-repair vendored (ree-v3
`172eb13665`); D.5 hysteresis re-measured (CONFIRMED, flap pairs −85%, no retune); D.6
fleet-idle watcher predicate fixed + vendored (`c6ff439f26`; SD-018 surfaced as refill
backlog); F.1 lit-schema 0-failing restored (`b8e5b62593`); F.2 30 stale IGW manual
assignments audited + released (`0bf1d7da55`); F.3 evidence ladder v1 — sweep found no rung
changes, empty rungs strengthened (`9acaf6d104`); F.4 Step 5c prose escape hatch, GOV-HELDOUT-1
run and recorded (`5ad32f754f`); F.5 UA graph claustrum+preservation coverage (ree-v3
`56f41525e4`).

**DONE by the science-front session (reported via coordination channel):** 936a autopsy
confirmed+landed (`b0c0b8df72`); A.1 singleton-degeneracy guard (`bad6467722` — MECH-144 gate
open); A.2 963 manifest queue_id repaired; SD-018 adopted into A.6.

**REMAINING (my lanes):** C.1 push-default adjudication (kind=decision — needs the user);
C.3 noop-record investigation (deep; partly gated on the Sep-4 refwedge re-measure);
C.5 chip-archive proof-route decision (analysis can be prepared, decision is the user's);
C.6 bashgate characterisation (possibly-don't-ship); D.1 RC-session termination path (design
handoff to the orchestrate lane); D.2 detector-FP /metaworker-learning campaign (now FIVE
classes; user-ratified but interactive — run user-present); E worktree GC (careful Mac
session); G user-present reviews. Science lane continues per its own programme.
**Purpose:** replace one-session-per-chip dispatch with a small number of **campaign sessions**, each of which claims a batch of related open chips at start and resolves each at close. Chips remain the durable index (nothing here retires the ledger or changes the chip-spawning rules); this document is the **router** that batches them, so token spend goes to the work instead of to 40 separate session-startup/land cycles.

**How to use:** pick a campaign, open ONE claim covering its resource set, `chip_ledger.py claim` every chip in the batch, work them in the stated order, resolve each chip individually with its own note as it completes, close with one `/session-land`. A campaign that can only get through part of its list resolves what it finished and leaves the rest claimed-released — the plan is re-entrant.

**Context at authoring:** experiment queue starved (depth 2, both claimed, pending 0; `chip-queuefloor-fleet`). Claude-worker dispatch frozen by the account usage limit (cooldown withheld until 2026-08-30T22:23Z; weekly reset 2026-09-01 04:00 Europe/Dublin). Experiments themselves are unaffected (no Claude API). So: **Campaign A is the highest-leverage first spend when capacity returns**, because it converts sessions into queued experiments the fleet can run unattended.

---

## Already discharged by the 2026-08-30 cycle-review session (not in any campaign)

Resolved with verification notes in the ledger:
- `chip-20260829-wrapperdeploy-check-missing-healer-arbiter` — satisfied by REE_Working `3b32be1ac` (enumerating checker).
- `chip-20260829-mac-dispatch-service-db-error` — fixed by ree-v3 `7812199cfd`; service verified healthy.
- `chip-checkoutdiverged-ree-cloud-5-ree-working-master` — healer FF'd; completed to 0 behind.
- `chip-igw-20260828-236`, `chip-igw-20260829-239` — sessions completed per IGW ledger.
- `chip-igw-20260829-240` — dead session, but scope superseded by lit-pull-am-20260830 (SD-069 lit 0 → 0.798).
- `chip-statusregress-0f179d90d1` — withdrawn, false positive (deliberate Orchestrator release); folded as 5th class into the detector-FP campaign chip.
- `chip-pausepressure-dlaptop` — resolved: this plan IS the structural-discharge window it recommended.

Skill patches landed the same session: `/governance` PASS-skim now requires threshold-arithmetic reading (V3-EXQ-936a class); `/failure-autopsy` staging-mode gate now keyed to user availability at gate time, not session framing.

---

## Campaign A — Science lane: queue refill + evidence integrity (P0)

One interactive-or-dispatched session, ordered — the order is load-bearing (item 1 gates item 3's successor):

1. `chip-20260830-singleton-group-degeneracy-guard` — fix V3-EXQ-961's driver + arity guard. **Gates the MECH-144 retest** (governance Step 3 decision: successor queued only after this lands, so it cannot inherit the singleton false-degeneracy idiom).
2. `chip-20260830-exq963-manifest-queueid-loss` — repair the dirty v3_exq_963 manifest sitting uncommitted in REE_assembly (queue_id dropped; blocks nothing else but is live read-modify-write exposure).
3. `chip-20260830-exq165-dormant-driver-decision` — queue-or-retire the dormant MECH-143/144 driver; governance named it the natural vehicle for the MECH-144 properly-powered retest. Queue it (after item 1) → **first queue refill**.
4. `chip-20260829-sd-e1-item1-validation-exq-b` — E1 action-conditioning ON-vs-OFF ablation → **second queue refill**.
5. `chip-20260830-mech320-ceiling-retest` — genuinely due (substrate landed; pending EXQ carries claim_ids=[] so cannot weight the claim) → **third queue refill**.
6. `chip-20260830-arc030-ceiling-retest` + `chip-20260830-sd017-ceiling-retest` — cheap due-ness ASSESSMENTS only (both claims' own notes say retest may be premature); record the decision, queue only if due.
7. `chip-queuefloor-fleet` — resolves itself once depth ≥ 3 (items 3–5).

Gated, stay open, do not start: `chip-20260814-queue-causal-sleep-matched-arm` (needs the 920 retrospective's constants), `chip-20260818-mech152-redesign-queue-gated` (needs the contextmemory write-path fix; GFLAG-0044).

## Campaign B — Substrate builds: resume, don't rebuild (P0, after A or parallel on cloud)

1. `chip-20260829-sd082-percandidate-summary-fix` — severity **corrupting**. Work is preserved, NOT lost: ree-v3 half on `integration/sd082-percandidate-summary` (`3aa45dea40`, on origin), REE_assembly half on cloud-4 local branch `preserve/sd082-assembly-20260830` (`7b3d88476c`). Start from those branches, drop the cosmetic re-serialisations, run the contract suite (never completed), merge integration→main, land assembly half normally. Releases the cloud-4 protective claim `healer-ree-cloud-4-20260830-protect-sd082-assembly-wip` when done.
2. `chip-20260827-mech482-accumulator-build` — both ORNT-2 gates cleared; note V3-EXQ-964's autopsy finding (n_targets==1 makes the readout constant) and the new `sd_epistemic_deficit_multitarget_readiness` substrate entry — build against multi-target readiness or the validation re-run hits the same wall.
3. `chip-20260827-capability-contract-plasticity-vocab` — mechanical swap per the inventory's mapping table.

## Campaign C — Coordination-plane hardening (P1, one session, main checkout)

Run `scripts/run_scripts_tests.sh --changed` before landing anything here.

0. `chip-20260829-ree-v3-trunk-corpus-pins-red` — **do first; blocks every session's commits** via the pre-commit contract gate. Adjudicate the two red corpus-count pins (expected addition vs genuine catch), re-pin deliberately.
1. `chip-20260830-pushdefault-adjudicate-three-dispatch-scripts` — per-script push-default decision; clears the `test_push_default_drift_guard` trunk red.
2. `chip-20260828-chipledger-failopen-loss-fix` — the 180s fail-open silent-loss window (reproduced 6/6); post-commit self-verification for five subcommands + stop failing open against a LIVE holder.
3. `chip-20260828-chipledger-noop-record-committed-destructive-delete` — investigation, not a one-liner (its obvious fix already failed a held-out check); may be partly subsumed by R1 — establish that first.
4. `chip-20260829-taskclaim-stale-arbitration` — stale-local NOT-THE-OWNER false contention, 2 confirmed occurrences; make the non-coordinator arbitration path refresh or qualify its verdict.
5. `chip-20260828-chiparchive-uncovered-by-every-proof-route` — needs a decision (new dict RegistrySpec kind vs reshape vs `--to-remote-tip`); one orphaned archive commit denies route C to whole ranges.
6. `chip-20260828-bashgate-shortcmd-unterminated-quote-underfire` — characterise over-fire first; "do not ship" is an acceptable outcome, record it either way.

Dated, keep out of the session until due: `chip-20260904-refwedge-r1-rate-cost-remeasure` (≥ 2026-09-04).

Added 2026-08-30 by the cutover durability review (coordinator_cutover_durability_review_20260828.md):
7. **C.7** — `renew` is the one suppressed verb with no coordinator-ack verification
   (task_claim.py:4893); add `verify_renew_coordinator_ack` per the hollow-ack pattern.
8. **C.8** — the `task_claim_chip_drift_log` has no programmatic reader; add a hygiene-tick
   source that chips on `diverged=1` (this is also the compensating channel the statusregress
   fix's accepted blind spot relies on).

## Campaign D — Metawork lifecycle + fleet deploy hygiene (P1)

1. `chip-20260829-rc-metawork-session-lifecycle` — the root cause of the Mac lockup (12 finished RC sessions running a day past done). Design the termination path; coordinate with the standing `/metaworker-orchestrate` owner (memory: leave orchestration machinery to it — this is a design handoff, not a unilateral build).
2. `chip-20260829-metaworkerlearning-detector-falsepositive-campaign` — already a bundled campaign, now FIVE classes (hook-gating, +2 folded by healer, non-hermetic tests, statusregress-on-deliberate-release). Run via `/metaworker-learning` as one root-cause pass.
3. `chip-20260830-cloud5-stale-healer-deploy` — 10-minute deploy + `check_metaworker_wrapper_deploy.py` re-run to verify.
4. `chip-20260830-stray-git-sync-repair-untracked` — vendor `/usr/local/bin/ree_git_sync_repair.sh` into a repo (follow the committed-template convention used by the launchd plists).
5. `chip-20260821-heartbeat-hysteresis-remeasure` — measurement only.
6. `chip-20260826-fleet-idle-watcher-validation-candidate-false-negative` — audit the 37 exclusions.
7. **D.7 (from the durability review, awaiting the user's go)** — retire the hub from the
   experiment pool: graceful runner stop after V3-EXQ-959 completes, then disable ree-runner on
   cloud-1. The review ties hub load directly to render-visibility durability (F4), and the
   user proposed exactly this on 2026-08-30.

## Campaign E — Worktree GC (P2, Mac, careful)

1. `chip-20260826-worktree-graveyard-triage-and-gc` — 92 worktrees, 50 with unlanded commits; per-commit CONTENT audit before any removal (never by shape — the coin-flip rule), LIVE/DIRTY never removed.
2. `chip-metaworkergc-sweep-1-7c5d680ca1c4e0fd` — subsume into 1 (its single candidate is in the same graveyard); resolve it pointing at the triage outcome.

## Campaign F — Governance/registry small-items batch (P2, one short session)

1. `chip-20260830-litschema-arc092-missing-summarypath` — 2 records, add missing `summary_path`.
2. `chip-20260829-igw-manual-assignment-staleness` — audit/release ~30 stale manual_ui assignments (oldest 2026-05-26).
3. `chip-20260827-evidence-ladder-v1-dirsweep` — directory-manifest sweep, update ladder either way.
4. `chip-20260828-step5c-registry-producer-rule` — run the GOV-HELDOUT-1 check on the prose-only exception before it becomes a rule.
5. `chip-20260828-ua-claustrum-scan-coverage` — fix the scanner scope (4 dropped source files).

## Campaign G — Reviews and design sessions (user-present, schedule when convenient)

- `chip-20260828-cutover-durability-review` — adversarial audit of the coordinator-ack write path; highest epistemic value of the batch given three coordination-plane loss chips in Campaign C stem from the same cutover.
- `chip-20260828-phase4-ws-soak-eval-flag-flip` — due ≥ 2026-08-31 (3-day soak from 08-28); evaluate section-7 criteria, flip `workspace_state_suppress_git_write` only if clean.
- `chip-20260828-skillarch-metaworker-dispatch` — skill archaeology on the 3,336-line dispatch skill (pure moves; Opus recommended).
- `chip-20260826-representation-authority-selection-bottleneck` — RC research session with the user.
- `chip-20260826-thought-digestion-wave-grouping-design` — RC design session with the user.

---

## Sequencing summary

```
now (usage-frozen):  C.0 corpus-pins-red (interactive Mac session; unblocks commits)
                     D.3 cloud5 healer deploy (ssh, minutes)
after 22:23Z / Sep1: A (queue refill)  ->  B (substrate resume)
then:                C, D as single campaign sessions
anytime short:       F;  E when a careful Mac session is free
user-present:        G, one item per sitting
```

Chip count at authoring: 47 open → 39 after this session's discharge → target ≤ 10 after campaigns A–D, with the gated/dated four (sleep-matched-arm, mech152, refwedge-remeasure, phase4-flip) as the legitimate residue.
