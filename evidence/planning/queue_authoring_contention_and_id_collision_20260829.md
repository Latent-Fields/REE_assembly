# Queue-authoring contention and EXQ ID collision — measurement + fix record

**Date:** 2026-08-29
**Chip:** `chip-20260828-queue-authoring-contention-and-id-collision`
**Session:** `responsibility-epistemic-hygiene-d6f9d3` (DLAPTOP)
**Landed in:** `.claude/skills/queue-experiment/SKILL.md` + `.agents/` mirror (Steps 2, 4, 5, 8, Key rules)

---

## 1. What was reported

Two symptoms, both surfacing after `REE_Working 5575aae6` (the ingress fix) let cloud boxes
dispatch queue-ADD chips for the first time — which released a backlog and moved the
constraint one step downstream rather than removing it:

1. **Serialized claim on `ree-v3/experiment_queue.json`.** A completed authoring session
   (`metaworker-chip-20260825-e1-rollout-horizon-sweep-probe`, ree-cloud-4) could not perform
   its one remaining step — the queue append — because another session held an active
   TASK_CLAIMS claim on that file for 57+ minutes, two more queued behind it.
2. **Concurrent duplicate EXQ ID minting.** A live 3-way collision on `V3-EXQ-953`.

---

## 2. What was measured

### 2a. The whole-file claim confers NO mechanical protection

`ree-v3/experiment_queue.json` is **absent from every claim-consulting gate in the fleet**:

| gate | what it protects | covers the queue file? |
|---|---|---|
| `runner_remote_control._REE_V3_CODE_CLAIM_PREFIXES` (`experiment_runner._ree_v3_pull_blocked`) | the runner's `git pull --rebase --autostash` on the shared ree-v3 checkout | **NO** — `ree_core/`, `experiments/`, `tests/` only |
| `runner_remote_control._active_claim_on_evidence_dir` (`push_heartbeat` / `push_commands`) | REE_assembly `evidence/**` + `docs/claims/` | **NO** |

So the claim's only effect is `task_claim.py open` arbitration — exit 3 for the next session.
It is a pure serializer.

### 2b. Observed hold times on that resource

From `TASK_CLAIMS.json` at `origin/master`, 2026-08-29T09:25Z (the 24h-retained window; older
`done` entries are pruned):

```
n = 8 closed claims naming ree-v3/experiment_queue.json
median 81 min   mean 193 min   max 711 min   p90 473 min
  711m  governance-cycle-20260828
  473m  igw-236-confirm-evidence-mech-267-lit-0
   92m  failure-autopsy-20260828-diagbatch-pause
   84m  metaworker-chip-20260828-armedstack-exp0593
   79m  igw-auto-igw-236-confirm-evidence-mech-267-lit-0-20260828T214515Z
   54m  metaworker-chip-20260827-diagnose-mech269b-q040c-nonengagement
   29m  metaworker-chip-20260828-sd069-stepcap-rerun
   25m  chip-queuefloor-ree-cloud-5-since-2026-08-29t03-49-38z
```

Downstream cost on the 2026-08-28 evening alone: **five** authoring sessions committed a
finished, smoke-tested driver with `queue append pending ... experiment_queue.json contended`
in the commit message (ree-v3 `0dfee20`, `0def34b`, `d7cbf56`, `5b884c0`, `dc09b7f` — covering
EXQ 953/954, 956, 957, 958) while the runnable queue sat at **depth 1 against a floor of 3**.

### 2c. The append does not need a lock — confirmed empirically, not from a docstring

End-to-end repro against real git repos (bare origin + two clones, both branched from the same
base, `ree_commit.py --push --retry-push-on-reject`):

| case | result | evidence |
|---|---|---|
| two sessions append **different** `queue_id`s | **merges automatically** | `push-retry 1/3: cherry-pick hit a line-level conflict; re-applied the commit's per-entry delta onto origin/main structurally` → `pushed via throwaway worktree` → origin holds **both** entries |
| two sessions append the **same** `queue_id`, different content | **REFUSED, never silently merged** | `_merge_list` OVERLAP → `structural re-apply: ... an entry both sides changed differently ... this is a GENUINE conflict, staying fatal`; origin unchanged, commit safe locally |

So the git plane is already correct in both directions. What was missing is that
`/queue-experiment` Step 8 did **not** pass `--retry-push-on-reject` (it is opt-in), so the
first case degraded to a manual pull/re-verify/retry loop instead of a no-op.

### 2d. The ID had no reservation anywhere

Step 2 read `experiment_queue.json` + `runner_status.json` only. Neither shows an ID a
concurrent session is *already building on*, because the headless-worker contract mandates
`wip:` script commits **hours** before any queue entry. Timeline of the actual 953 collision:

```
21:53Z  0dfee20  REE Cloud Worker      wip: V3-EXQ-953 E1 horizon sweep ... (queue-append pending)
22:13Z  0def34b  REE Cloud Worker      wip: rename V3-EXQ-953 -> V3-EXQ-954 (3-way ID collision)
22:47Z  d7cbf56  REE Automation (Mac)  V3-EXQ-953: E1 rollout horizon sweep ... (script only)
23:33Z  5b884c0  (third session)       V3-EXQ-953 (tentative id) ContextMemory gumbel_learned
01:18Z  580b1fd                        renamed 953 -> 956 due to live ID collision
```

Two of the three (`0dfee20`/`d7cbf56`) are **the same scientific question authored twice** by
two sessions that never saw each other — the collision cost was duplicated design work, not
just a rename. `git ls-tree origin/main experiments/ | grep v3_exq_953_` would have caught
claimants 2 and 3; only an atomic reservation catches a genuinely simultaneous pick.

---

## 3. What changed

1. **Step 2 — check three namespaces** (queue, `runner_status.json`, **and the `experiments/`
   script namespace on `origin/main`, after an explicit fetch**), then **RESERVE the ID** with a
   second `task_claim.py` entry naming `ree-v3/experiment_queue.json/V3-EXQ-NNN`.
2. **Step 4 (Before starting) — claim `ree-v3/experiments/` instead of the queue file.** The
   directory keeps the only protection that is mechanical (the autostash gate) while being a
   *scope* claim, so it reports rather than arbitrates.
3. **Step 8 — `--retry-push-on-reject` is now part of the documented command.**
4. Step 5's ID re-verify now also re-runs the script-namespace check and re-reserves on
   increment; pre-flight item 2 and Key rules updated to match.

### Why the slot spelling works with zero code change

`ree-v3/experiment_queue.json/V3-EXQ-NNN` is file-shaped (`is_scope_resource` → False, since it
has no trailing slash and is not an on-disk directory), so `resource_overlap` arbitrates it on
exact match, and containment gives the whole-file case a NOTE. Verified directly against
`task_claim.resource_overlap`:

| yours | rival's | verdict |
|---|---|---|
| `…/V3-EXQ-953` | `…/V3-EXQ-953` | **EXACT → arbitrated** |
| `…/V3-EXQ-953` | `…/V3-EXQ-954` | silent |
| `…/V3-EXQ-953` | `…json` (whole file) | scoped → **NOTE** |

**This is the answer to the chip's question (b) — "should the coordinator mint IDs?" — without
a new endpoint or a hub deploy.** Since the 2026-08-28 cutover, `task_claim.py open` on a
coordinator-mode box *is* server-side atomic (`BEGIN IMMEDIATE` before the rival check, pinned
by `coordinator/test_task_claim_chip_mutations.py`). The coordinator already mints exclusivity;
it was being asked about the wrong resource.

### Known cost, stated rather than papered over

A slot resource never exists on disk, so `audit_stale_claims.analyse_resources` records it as
`missing`, which disqualifies bucket A and drops the claim to `C_no_trace` (report-only). Effect:
a stale unclosed reservation is **reported to a human instead of auto-closed** — conservative,
and arguably right given the 2026-08-27 bucket-A mis-close of a live session — but it emits one
`path does not exist` warning per open reservation. Teaching `resolve()` about virtual slot
resources is a separate, separately-reviewable change to a delicate audit; not folded in here.

---

## 4. GOV-HELDOUT-1 check (mandatory; run 2026-08-29, PASSED)

Old wording: claim the whole queue file at Step 4, session-length, arbitrated.
New wording: claim `ree-v3/experiments/` (scope) + reserve the ID slot (arbitrated).
Only cases where the two give **different** answers count.

**Non-degenerate held-out cases — 6, all predating the motivating incident:**

| # | case | OLD | NEW | NEW correct? |
|---|---|---|---|---|
| HO-1 | 2026-08-22 01:30→04:43Z, `metaworker-chip-20260821-igw-234-mech091-confirm` held the queue file ~3h13m; `chip-20260820-cem-authority-readiness-validation` and `chip-20260821-exq861e-h1-h3-fanout` both blocked, self-unclaimed, re-dispatched later | 2 chips blocked ~3h | 3 distinct IDs → no contention → all 3 append | yes (2c) |
| HO-2 | 2026-08-22T15:27Z — `exq861e (lost arbitration on experiment_queue.json)` | blocked | own slot uncontended → proceeds | yes |
| HO-3 | 2026-08-23T09:01Z — owner `worktree-agent-a53b125a2ecbdbfa7`, ~3h15m old, not stale, "correctly not re-claimed" | blocked ~3h15m | different IDs → proceed | yes |
| HO-4 | 2026-08-25T07:56Z — "contention flagged ... owned by `queue-conversion-ceiling-gate-f2545f`; **no queue write was needed**" | spurious contention report | no slot claimed when no queue write is planned → no report | yes (removes a false alarm) |
| HO-5 | 2026-08-23 — "`task_claim.py` named `mech-152-redesign-queue-971c65` owner **by 5 seconds**; proceeded under `--allow-overlap` (different claim, different experiment)" | needed the escape hatch | correct answer natively, no hatch | yes — **and this is independent field corroboration that file grain was already known to be wrong** |
| HO-6 | 2026-08-22 — `experiment_queue.json` REFUSED, owner `igw-auto-igw-229-proposal-for-sd-099`, 16 min ahead; "moot given the gate" | refusal on an unrelated proposal | silent | yes |

**Negative controls — must give the SAME answer (they do):**

- **NC-1** The 2026-07-28 three-session collision on `ree-v3/runner_remote_control.py`. A code
  file, not the queue. Unchanged → still arbitrated, still exactly one owner. The change is
  scoped to the queue file's ID-slot structure and does **not** weaken arbitration generally.
- **NC-2** V3-EXQ-603d (2026-06-01) dropped-file race. Commit-machinery hazard; claim grain is
  irrelevant. Unchanged → must **not** be read as fixing it.
- **NC-3** Same-ID collision. The *safety* answer is identical under both (the merge REFUSES
  either way, §2c). What changes is only the **timing of discovery** — Step 2 seconds in,
  versus Step 8 after a full session of design/review/smoke. Describe the gain as earlier
  discovery, never as new safety.
- **NC-4** `governance-cycle-20260828` holding the whole file 711m. A governance cycle still
  claims the whole file (it is not appending one ID), so its own posture is unchanged; only
  queue-authoring sessions move from refusal to NOTE.

Per CLAUDE.md, adopting this practice is **not** evidence GOV-HELDOUT-1 works. Recording it as
one instance where the check was actually run: it **passed** (6 differing cases found, well over
the floor of 3), it did **not** cause a narrowing, and it cost roughly one `grep` over
`WORKSPACE_STATE.md` plus the reasoning above — but it *did* produce NC-3, which changed how the
fix is described in the skill (earlier discovery, not new safety).

---

## 5. Residue / follow-on

- **`experiments/v3_exq_953_mech135_inv088_e1_horizon_sweep_action_divergence_probe.py` (ree-v3
  `d7cbf56`) is a duplicate authoring of V3-EXQ-954 and must NOT be queued** — 954 carries a
  horizon-matched `CR_real(h)` reference that 953 lacks. Recorded in 954's queue `note`; the
  script itself was left on `origin/main` (deleting another session's landed work is out of
  scope for this chip).
- **EXQ 956, 957, 958** are authored, smoke-tested, tracked on `origin/main` and **still
  unqueued**, each stranded by the same contention. They belong to their own chips.
- `audit_stale_claims.resolve()` does not understand virtual slot resources (§3, "Known cost").
- Nothing here changes the ID *convention* (`/queue-experiment` Step 2 naming rules,
  CLAUDE.md "EXQ Versioning and Supersession Policy") — only how an ID is reserved.
