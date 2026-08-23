---
nav_exclude: true
---

# Landing / Integration Worker — Investigation and Decision

**Date:** 2026-08-10
**Status:** investigated, decided — no dedicated worker; one narrow follow-on chipped
**Scope:** `REE_Working`, `REE_assembly`, `ree-v3` concurrency/integration machinery

## Bottom line

REE does not need a dedicated landing/integration worker (no new cloud machine, no
dynamically-assigned "landing" role, no new coordinator/daemon). The evidence does not support
it, and the one piece of the stated payoff that *is* evidenced and cheap to fix — redundant
full-suite validation runs — is better solved as a narrow, reversible extension to the existing
`precommit_contracts.sh` / `ree_commit.py` machinery than as new infrastructure. That narrow
extension (a tree-content-hash-keyed validation cache) is recorded below and chipped separately;
this document is the design/synthesis + decision, not an implementation.

This finding itself is worth stating plainly because the prompt that motivated it explicitly
allowed for it: *"If recent history suggests little benefit, record that and do not build."*
The archaeology below shows real, dated, wall-clock-costing contention — but it is
overwhelmingly of a *different* shape than "duplicated expensive validation," and the existing
architecture (optimistic CAS + narrow incident-driven fixes) is already closing it, incident by
incident, without a serializing actor.

---

## 1. What exact contention/validation problem currently exists?

Two genuinely distinct problems get conflated in "high-contention periods cause wasted work,"
and they have different owners today:

**(a) Read-modify-write / CAS races that cause lost or duplicated *authoring* work.**
Concurrent sessions and automations (`sync_daemon` phase3 writers, the metaworker fleet, IGW
ledger writers, human/session `git commit`s) all touch a small set of shared JSON/YAML files
and the shared `ree-v3`/`REE_assembly` working trees. When two processes race the same
file or the same branch ref, one of them loses real work — a dropped commit, a swept-in stale
read, a reverted heartbeat, a rebase that corrupts a sibling's in-flight cherry-pick.

**(b) Duplicated *validation* — every session that trips the ~13-minute `ree-v3` contract
suite pays the full cost independently**, even when a concurrent or very-recent session already
validated an equivalent tree. Nothing today asks "has this content already been validated?"
before paying that cost again.

The investigation prompt's framing (serialize the "narrow expensive act of making a validated
combination canonical") targets mainly (b). The archaeology found (a) to be the dominant,
heavily-evidenced problem, and (b) to be real in principle but thin in direct evidence.

---

## 2. Which existing REE mechanisms already address parts of it?

Four parallel investigations (session-land/chip machinery, `ree_commit.py`/validation-tier
machinery, git-log archaeology, coordinator/cloud-dispatch machinery) converged on the same
picture. Summarized by mechanism:

| Mechanism | What it actually guarantees | What it does NOT do |
|---|---|---|
| `ree_commit.py` compare-and-swap (`update-ref <old> <new>`) | At most one commit wins any given `old_head`; losers re-read and retry | Does not prevent N sessions from each *successfully* landing in quick succession, each independently triggering full validation |
| `ree_commit.py` rebase lock (`_acquire_rebase_lock`, 2026-08-08) | Serializes the *push-retry-via-worktree* surgery on `.git/worktrees` state so two concurrent retries can't corrupt each other | Says nothing about, and doesn't touch, validation |
| `task_claim.py` arbitration (`open` exit 3, earliest-`claimed_at`-wins) | Total, asymmetric ownership verdict for *resource ownership*, breaking mutual-deference livelock | Not a landing-time gate — a session can own a resource and still race another owner's *unrelated* commit through CAS |
| `safe_adopt_ref.py` / `ref_move_guard.py` | Refuse a ref move that would silently discard local commits or desync worktree state | Orthogonal to validation cost |
| `chip_ledger.py` CAS on `TASK_CHIPS.json` (dispatch mutex, "ORIGIN FRESHNESS" fix 2026-08-09) | Exactly one dispatcher wins a given chip dispatch | Dispatch-time mutex only — chips still land fully independently once dispatched |
| `precommit_contracts.sh` Block 1/1b/1c/2 cascade | Coarse binary blast-radius classification: touches `ree_core/`/`experiments/_lib/` → full ~13min suite; touches only `experiments/*.py` → lint-only subset | **No tiering within Block 2** — every commit that trips it pays the identical full suite regardless of diff size; **no result cache** keyed on tree/path-set content |
| `remote_pytest.sh` auto-routing + staggered local-race fallback | Distributes *where* a given suite run executes (idle-box fall-through, lease-protected wake), and races local-vs-remote to finish one run faster | Never asks *whether* a run is needed — two sessions landing minutes apart are routed to different boxes (or queued) and each pays the full suite |
| Coordinator (`ree-v3/coordinator/db.py`) `try_claim` (`BEGIN IMMEDIATE` + conditional `UPDATE`) | A real, generic, table-agnostic atomic-claim primitive already proven at fleet scale for experiments | Every timing constant (`stale_hours`=6h, `fence_seconds`=1800s) is tuned for VM power-cycling and hours-long experiment runs, not a seconds-to-minutes landing role — would need new constants, not reuse, even if the DB file were shared |

**Architectural pattern, stated explicitly by the session-land investigation:** REE's answer to
concurrency, everywhere it has been solved, is *optimistic CAS + retry on shared files*, not a
serializing actor. No document anywhere proposes or rejects a landing-worker concept — this
appears to be the first time it has been considered — but the codebase has a strong, consistent,
repeatedly-reinforced house style, and every existing fix (rebase lock, ORIGIN FRESHNESS,
skew detection, ref-move guard) extends that style rather than introducing a queue/actor.

---

## 3. What remains unsolved

Exactly three things, none of which require a dedicated worker to close:

1. **No validation-result cache/marker keyed on relevant-path-set content.** Confirmed absent
   by direct grep of `ree_commit.py`, `precommit_contracts.sh`, `remote_pytest.sh` for any
   cache/memoize/"already validated" pattern (the only hits are an unrelated 15s power-state
   cache and ordinary git-index reads).
2. **No sub-tiering inside the "full suite" trigger.** Block 2 fires as an all-or-nothing gate;
   a one-line comment-only change to `ree_core/` pays the same ~13 minutes as a 500-line
   `ree_core/agent.py` rewrite.
3. **No "candidate landed vs. not yet landed" state distinct from claim ownership.** `TASK_CLAIMS`
   tracks *who owns what*; `TASK_CHIPS.json` tracks *task done vs. open*; neither tracks
   "validated tree exists, not yet canonical." This gap is real but, per the archaeology, has not
   itself been the source of a confirmed incident — the CAS mechanism already makes "landed vs.
   not" observable via `git log`/`ree_commit.py`'s delta reporting.

---

## 4. Would centralized/serialized landing actually improve throughput?

**Not enough to justify the cost, on current evidence.** Two lines of reasoning:

**Evidence for the (a)-class problem (races that lose/duplicate authoring work) is strong, but
already being solved without a serializer** — and successfully: every incident below was closed
same-day or within days by a narrow CAS/lock/detection fix, not by adding a queue.

- **2026-08-08**: concurrent `retry_push_after_rebase()` invocations corrupted a sibling's
  in-flight cherry-pick (detached HEAD, `TASK_CLAIMS.json` `UU`, dangerous staged reverts of
  already-landed chip resolutions). Root cause: no lock around a shared-tree rebase. **Fixed
  same day** with a per-repo mkdir lock — a serialization primitive, but scoped to exactly the
  critical section that needed it (43 lines), not a new actor.
- **2026-07-28**: three sessions (`beautiful-elbakyan-245a58`, `silly-mayer-a60957`,
  `quirky-sinoussi-b9a180`) claimed the same file within 84 seconds, released by one landing.
  **Fixed** with `task_claim.py open`'s asymmetric arbitration verdict (owner=earliest
  `claimed_at`), not a queue.
- **2026-07-29 (`ree-v3` `346e9e3`→`13bfa2c`)**: a 1,020-line experiment script + queue entry
  (V3-EXQ-838) was dropped by a concurrent-rebase race and had to be fully re-landed **7.5 hours
  later**. This is the single most expensive confirmed incident found — genuine duplicated
  authoring effort, not validation compute.
- **2026-08-09 (new finding)**: `ree-cloud-5`'s heartbeat writer's own rebase-retry failed **182
  of 267 attempts (68%)**, collapsing to **8% success on 2026-08-08** once an uncommitted regen
  artifact wedged the shared checkout — the identical class of problem (stuck behind trunk, real
  work piles up unpushed) via a *different* code path than the `ree_commit.py` incident above.
  Not yet fixed as of this writing (flagged as follow-on below, but out of this investigation's
  scope — it's a heartbeat-writer bug, not a landing-worker gap).
- **2026-07-31 (`REE_assembly` `b0975a714d`)**: a same-day stale-read fixup on
  `substrate_queue.json` — the general read-modify-write contamination pattern, a fresh instance.
- **Live, right now (2026-08-10)**: `audit_stale_claims.py --json` shows two active sessions
  genuinely contending for `claims.yaml` at this moment — contention is not merely historical.

None of these would have been *prevented* by a landing worker in the sense the prompt describes
(a serializer for the git-commit act) — they are races in different code (heartbeat writers,
rebase retries, claim files), most already hardened by targeted, narrow, in-place fixes matching
the existing "optimistic CAS + retry" idiom. A landing worker would be a second, parallel answer
to a problem class the codebase already has a working answer for.

**Evidence for the (b)-class problem (duplicated ~13-20 minute validation runs from near-
simultaneous landings) is real in principle but thin in direct measurement.** The only concretely
measured instance is the already-fixed 2026-08-01 hub-contention incident (2h+ vs. 13m53s), and
that was closed by `precommit_contracts.sh`'s staggered local-race fallback — a routing fix, not
a dedup fix, but it removed the *symptom* (a session stuck waiting) even though the *duplication*
(both runs still happen) remains unaddressed. No second, independent incident of two full-suite
runs firing on equivalent content within the same window was found. Given ~3,000-4,300 commits/
month on `ree-v3`+`REE_assembly` trunk combined (overwhelmingly machine-written coordination
data that never trips the precommit gate at all) and no confirmed measurement of duplicate-suite
wall-clock loss, **a serializing landing queue is not evidenced as paying for itself** — but a
cheap, narrow validation-result cache (below) captures the same payoff without needing to know
whether the duplication is common; it costs nothing when there's no duplication to skip.

**Conclusion:** centralized/serialized landing would not measurably improve throughput beyond
what a narrow cache achieves, and it would add a new component with its own failure modes
(single point of contention, or — if made non-single — its own concurrency problem) to solve a
problem the codebase's existing idiom already handles incident-by-incident.

---

## 5. Should it be a dedicated cloud machine, ephemeral role, or software queue?

**None of the above — see §4.** But since the prompt asks explicitly: if this *were* built, the
evidence points at *queue consumed by whichever session/box is already there* (the existing CAS
idiom, generalized) over a dedicated actor, for three concrete reasons found in the coordinator
investigation:

- **No dynamic worker-role concept exists anywhere in the fleet.** `cloud-scaler.py`'s `WORKERS`
  list is a hardcoded static tuple; every worker is unconditionally an experiment runner. The
  only "role-like" primitive is the pytest lease (a shutdown veto, not a role claim). Building
  "assign the landing role dynamically" would be genuinely new infrastructure, not an extension.
- **The hub (`ree-worker-1`/`ree-cloud-1`) is the only real idle-and-scaler-immune candidate**,
  and it is measured *faster* than the bigger workers for this workload (single-threaded, shared
  vCPUs don't help) — but colocating any git-writing landing role there directly risks the
  **exact, extensively-documented dirty-tree-blocks-phase3-writer hazard** that already required
  giving the experiment runner its own isolated second checkout (`~/REE_Working_runner`) to avoid
  wedging `sync_daemon`. A landing worker would need the same isolation, which erodes most of the
  "it's already idle and free" argument.
- **The coordinator's `try_claim` primitive is reusable in principle** (table-agnostic atomicity)
  but every existing timing constant is tuned for hours-long, power-cycled experiment runs, not a
  seconds-scale landing lease — reuse would mean a new table with new constants sharing only the
  DB file, which is a small win, not a large one.

So: if evidence ever justifies revisiting this, the answer is *"extend the existing CAS idiom
with a shared, content-addressed cache"* — never a dedicated machine or role.

---

## 6. What is the minimum implementation?

**One narrow, reversible extension — chipped, not built in this session** (see Follow-on below):
a validation-result marker keyed on **(relevant-path-set content hash, machine-class + toolchain
identity, validation tier)**, consulted by `precommit_contracts.sh`'s Block 2 before paying the
full ~13-minute suite.

- **Key, not commit SHA.** Keying on the *content hash of the files Block 2's own trigger already
  reads* (`ree_core/` + `experiments/_lib/`) means irrelevant commits (docs, evidence, queue
  entries) never invalidate a cache hit — this is strictly narrower and safer than keying on tree
  SHA or commit SHA.
- **Machine-class + toolchain scoped, not global.** The already-confirmed cross-machine-class
  divergence (`torch.multinomial` differs `darwin-arm64`/torch 2.10.0 vs `linux-x86_64`/torch
  2.11.0+cpu) means a hit recorded on one machine class must never certify a different one. Cache
  entries carry the same `machine_class` fields already used elsewhere in the codebase (noting
  the known gap that `machine_class` omits torch version — the cache record should NOT repeat
  that gap; it must include it explicitly, since this is precisely the axis that has already
  caused real divergence).
- **Bounded freshness (TTL), not indefinite.** A hit older than a short window (e.g. 30–60
  minutes) is treated as a miss — this is a conservative default to bound exposure to any residual
  test nondeterminism beyond the already-identified and already-fixed `multinomial` cases, and
  can be loosened later with evidence.
- **Storage: reuse the existing high-contention-file pattern, not a new ledger type.** A single
  small JSON record (e.g. `ree-v3/.contract_validation_cache.json` or similar), written via
  `ree_commit.py` with an explicit path list exactly like every other shared JSON file in this
  codebase — no new concept, no new script category.
- **Never a silent skip.** Every cache hit must be loudly logged (which record, which hash, which
  commit it was recorded against) so a hit is auditable exactly the way `ree_commit.py`'s
  per-item delta reporting already is. This is validation *reuse*, not validation *bypass* — the
  content genuinely was already tested; the record just avoids re-paying for a test that would
  necessarily reproduce the same result.

This is deliberately **not** a candidate-lifecycle schema, batching, or a landing queue — those
are the "large distributed integration service" the prompt explicitly warns against building
without evidence, and the evidence doesn't support them.

---

## 7. Safety invariants that must not regress

All preserved, because nothing here touches the mechanisms that provide them:

- **Path-scoped/intended-file commits, CAS, no silent dropping, no force-push, no bypass of
  required tests** — untouched; the cache only ever *skips a redundant re-run of a test that
  already passed against equivalent content*, never *skips running a test that hasn't run*.
- **Governance/scientific-evidence semantics** — untouched by construction. The cache is scoped
  to `ree-v3` contract-suite validation only; it says nothing about, and cannot be consulted for,
  scientific claim promotion, `claims.yaml` disposition, or evidence direction. Engineering
  landing and scientific closure remain fully separate, as they are today.
- **Experiment-runner autocommits** — untouched. Phase-3 writers (`sync_daemon`) do not have
  `precommit_contracts.sh`'s hook installed at all (by design — see CLAUDE.md's Coordinator
  section on why hooks are absent from the hub/workers), so this cache is invisible to and cannot
  interact with the experiment-result commit path. No new coupling is introduced there.
- **No new single point of failure.** The cache is a shared file, not a service — if it's stale,
  missing, or corrupted, every consumer fails open to "run the full suite," identical to today's
  behavior. This mirrors every other fail-open guard already documented in this codebase.

---

## 8. How to measure whether the follow-on chip was worth doing

Once the validation cache lands, instrument it (in the chip itself, not as a separate experiment)
to log, per invocation: hit/miss, cache key, age of the hit if any, and wall-clock minutes saved
on a hit. After 2–4 weeks of real usage:

- **Hit rate.** Nonzero and recurring hits are the direct evidence this investigation's evidence
  was too thin to gather ahead of time (no measurement tool for this existed before the cache
  itself).
- **Minutes saved vs. minutes spent building/maintaining it.** The break-even bar is low (the
  implementation is small), so this is mostly a sanity check, not a hard gate.
- **Zero false-positive skips** (a hit that turned out to certify a different behavior than a
  fresh run would have) — this is the one metric that would justify tightening the TTL/scoping
  or abandoning the cache outright, and should be checked by occasionally letting a hit-eligible
  run execute anyway and diffing results.

If hit rate stays near zero after a real trial period, that itself is the answer to "was
centralized/serialized landing worth it" for the (b)-class problem: **no**, and this document's
conclusion holds without needing to build anything larger.

---

## Follow-on (chipped, not built in this session)

Two durable chips spawned, per the project's default of chipping engineering follow-on rather
than building it inline in an already-large investigation turn. See `TASK_CHIPS.json` /
`WORKSPACE_STATE.md` for the live reference.

1. **`chip-20260810-validation-cache`** — the narrow validation-cache implementation described
   in §6. This is the landing-worker investigation's own deliverable.
2. **`chip-20260810-cloud5-heartbeat-rebase-fix`** — the `ree-cloud-5` 68%-failing
   heartbeat-writer rebase-retry (§4), a correctness bug uncovered incidentally during this
   archaeology and out of scope for the landing-worker question itself. Initially left
   unchipped and only flagged in this document; corrected at `/session-land` close, since this
   codebase's chip-by-default convention (chip everything that isn't `/governance` or
   `/failure-autopsy` work) applies to it too, and a diagnosis doc with a concrete recommended
   fix already existed (`REE_assembly/evidence/planning/ree_cloud5_push_lag_diagnosis_2026-08-09.md`).
