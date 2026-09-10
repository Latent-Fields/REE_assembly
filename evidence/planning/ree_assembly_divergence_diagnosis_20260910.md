# Why REE_assembly's shared checkout chronically diverges from origin/master

Measured 2026-09-10, read-only. Checkout state at time of measurement: `[ahead 12, behind 17]`.
All paths absolute. All rates derived from `git log`, `git reflog show master`,
`git reflog show origin/master` (3815 entries), and read-only runs of
`ref_convergence.py --check` / `--audit`.

---

## 0. Headline

The divergence is **not unpushed work**. It is **orphaned duplicates of work that is
already on origin**.

All 12 of the current ahead-commits have a subject-twin on origin/master. 8 of the 12 are
byte-for-byte patch-identical to their twin. The checkout is ahead of origin by 12 commits
that contain, almost entirely, content origin already has.

The divergence is therefore self-inflicted by the landing mechanism, not by writers failing
to push. Every writer in REE_assembly pushes by default and pushes successfully; the pushes
land as *cherry-picked twins with new SHAs*, and nothing moves the local branch ref onto
them. That is a documented, known, designed-for residual — and the component built to clear
it (`ref_convergence.py`) is refusing, correctly but on a technicality, roughly once an hour.

---

## 1. Writer inventory (empirical, 30 days, 5224 commits)

### 1.1 Authors

| Identity | Commits/30d | Where it runs |
|---|---:|---|
| REE Cloud Worker | 2599 | ree-cloud-*, pushes straight to origin. **Never touches this checkout.** |
| REE Automation (Mac) | 1660 | **This checkout.** The dominant local writer. |
| nooarche (personal) | 817 | **This checkout.** Interactive sessions. |
| REE Automation (Hub) | 148 | Hub box, pushes straight to origin. |

Local writers on this checkout: **2477 commits/30d ≈ 83/day**.
Remote writers landing at origin: **2747/30d ≈ 92/day**.
Both sides move at comparable speed, all day. There is no quiet window in which a
convergence could happen for free.

### 1.2 Writer classes by commit-message prefix

| Prefix | 30d | Local writer | Origin-side twin rate (7d, `-x` backref) |
|---|---:|---|---:|
| `phase3-heartbeats` | 2265 | none (Cloud Worker only) | 0% |
| `igw-ledger` | 885 | Mac 793, Hub 89 | **17.0%** |
| `igw-workset` | 287 | Mac 226, Hub 58 | 0% (never reaches the retry path — see §4.3) |
| `governance-flag` | 271 | Mac 266 | **37.6%** |
| `phase3` | 136 | Cloud 132 | 0% |
| `planning` / `docs` / `thought-*` / `lit-pull` / `governance` | ~350 combined | nooarche (interactive) | 0% |

Over the last 7 days, **95 of 960 origin commits (9.9%) carry a `(cherry picked from ...)`
trailer** — i.e. one in ten commits landing on origin is a push-retry twin. Over 30 days it
is 1592/5229 = **30%**.

### 1.3 Does each writer push? — file:line evidence

Every automated writer **pushes by default**. There is no silent `--no-push`.

| Writer | Push decision | Evidence |
|---|---|---|
| `igw_routine_tick.py` (igw-ledger, igw-workset) | pushes unless `--no-push` | `/Users/dgolden/REE_Working/scripts/igw_routine_tick.py:529` — `PUSH_COMMITS = not (no_push_global or no_push)`; invoked at `:809` — `cmd += ["--push", "--retry-push-on-reject"]` |
| `governance_flag.py` (governance-flag) | pushes unless `--no-push` | `/Users/dgolden/REE_Working/scripts/governance_flag.py:883` — `args.push = not getattr(args, "no_push", False)`; `:529` — `cmd += ["--push", "--retry-push-on-reject"]`; docstring `:70` — "`raise` and `resolve` PUSH BY DEFAULT (2026-08-16)" |
| `task_claim.py` | pushes unless `--no-push` / orphan-push withhold | `/Users/dgolden/REE_Working/scripts/task_claim.py:5837` — `args.push = not no_push`; `:1305` — `cmd.append("--push")`; withhold documented `:5438` |
| `chip_ledger.py` | pushes by default | `/Users/dgolden/REE_Working/scripts/chip_ledger.py:2319` — `push=True, bot=True`; default gate at `:2429` |
| `confirmer_verdict.py` | pushes unless `--no-push` | `/Users/dgolden/REE_Working/scripts/confirmer_verdict.py:720`, `:393` |
| interactive `nooarche` sessions | push explicitly per skill | n/a — landed by hand or by `ree_commit.py --push` |

**So the answer to "who commits locally and never pushes?" is: nobody, by intent.**
The failure is downstream of the push, not at it.

### 1.4 Where a commit CAN silently stay local

Three places, all in `/Users/dgolden/REE_Working/scripts/ree_commit.py`:

1. **`:4011`** — primary push rejected → stderr `"ree_commit: push rejected:"`, then
   `:4013` calls `retry_push_via_worktree(...)`. If the retry also fails, `:4022` returns
   exit 1 with an explicit operator instruction. **This is loud, not swallowed.**
2. **`:3766`** — the throwaway-worktree cherry-pick merged cleanly but
   `verify_cherry_pick_faithful()` could not prove it preserved the box's edit → returns
   `"fatal"`, commit stays local. Reported on stderr only.
3. **`:2485` `_converge_after_push()` — FAIL-OPEN, and this is the one that matters.**
   Its own docstring: *"FAIL-OPEN IS THE POINT, not laziness. By the time this runs the
   caller's content is already on origin -- durability is achieved."* The push **succeeded**,
   so `ree_commit` returns **0**. The orphan commit that the cherry-pick just created is
   left on the local branch, and **no caller ever sees a non-zero exit for it.**

That is the swallowing. Not push failure — *convergence* failure. Every writer reports
success while the checkout silently accumulates +1 orphan.

---

## 2. Measured recurrence rate and duration

Reconstructed by pairing every `origin/master` reflog event with the `master` reflog value
in force at that instant, then computing ahead/behind. Window 2026-08-27 → 2026-09-10
(345.3 h), **1784 observations**.

### 2.1 State distribution

| State | Observations | Share |
|---|---:|---:|
| Converged (0/0) | 1015 | **56.9%** |
| Behind only | 131 | 7.3% |
| Ahead only | 5 | 0.3% |
| **Diverged (both ahead and behind)** | **633** | **35.5%** |

### 2.2 Magnitude when diverged

| | median | p75 | p90 | max |
|---|---:|---:|---:|---:|
| ahead | 10 | 22 | 35 | **76** |
| behind | 18 | 42 | 72 | **130** |

The observed 21/18, 15/12 and today's 17/12 sit almost exactly on the median. They are not
a bad day; they are the normal operating point.

### 2.3 Episode rate and duration

**57 divergence episodes in 14 days = ~4.1/day = one every 5.8 hours.**

| statistic | value |
|---|---|
| median episode duration | 0.02 h (~1 min) |
| mean episode duration | 1.48 h |
| max episode duration | 13.35 h |
| total time with ahead>0 | 87.6 h of 345.3 h = **25.4% of wall-clock** |

The distribution is strongly **bimodal**, and this is the important shape:

- ~35 episodes are **transient** (<5 min) — a push races another push, the retry lands the
  twin, `_converge_after_push` proves it by patch-id, ref moves, done. **The machine works.**
- ~10 episodes are **wedges** (>1 h). These carry essentially all the cost:

| episode | duration | max ahead / behind |
|---|---:|---|
| 08-31 13:58 → 09-01 03:19 | 13.35 h | 18 / 27 |
| 08-28 22:41 → 08-29 11:23 | 12.69 h | 24 / 130 |
| **09-09 21:24 → 09-10 09:36 (current)** | **12.21 h** | 20 / 23 |
| 09-09 10:49 → 09-09 19:26 | 8.61 h | 40 / 112 |
| 09-07 23:35 → 09-08 07:48 | 8.22 h | 76 / 76 |
| 08-28 12:52 → 08-28 19:41 | 6.80 h | 28 / 33 |
| 09-09 03:41 → 09-09 10:02 | 6.36 h | 46 / 54 |
| 09-07 16:06 → 09-07 20:37 | 4.52 h | 18 / 30 |
| 09-08 22:13 → 09-09 01:58 | 3.75 h | 23 / 33 |
| 09-08 17:39 → 09-08 20:48 | 3.15 h | 35 / 45 |

**~10 wedges/14 days ≈ 0.7/day, median wedge ~6.6 h.**
Frequency is rising: 6 of the 10 long wedges are in the last 4 days (09-07 → 09-10).

### 2.4 Persisted refusal state (independent corroboration)

`/Users/dgolden/REE_Working/REE_assembly/.git/ree_ref_convergence_wedge.json`:

```
branch: master   reason: unproven-ahead-commits
first_refused_at: 2026-09-09T21:09:30Z
last_refused_at:  2026-09-10T06:05:57Z
refusal_count: 9      ahead_count: 20      unproven_count: 3
```

The converger **ran nine times in nine hours and refused nine times.** It is not absent,
not broken, not unscheduled. It is running on cadence and declining. Note also that this
state was last written at 06:05Z and the checkout has continued to churn since — the
persisted `ahead_count: 20` / `unproven_shas` are already stale relative to the live
`--audit` (12 ahead / 4 unproven), so `--check` under-reports the current shape.

---

## 3. Why pushes fail — the five hypotheses, discriminated

| Hypothesis | Verdict | Evidence |
|---|---|---|
| **Non-fast-forward rejection (someone else pushed first)** | **CONFIRMED — the trigger** | 09-07/08/09 show 37/72/61 `fetch: fast-forward` events on origin/master (vs 0–13 on 09-05/06), i.e. other machines advancing origin between this box's commit and its push. Those are exactly the days that carry 6 of the 10 long wedges. Origin advances ~92 commits/day from Cloud+Hub. |
| **A wedge** | **CONFIRMED — the amplifier** | `ree_ref_convergence_wedge.json` above: 9 consecutive refusals, 11.5 h. Documented as self-sustaining at `/Users/dgolden/REE_Working/scripts/ree_commit.py:2394` — *"Once ahead by one, EVERY subsequent push is rejected on the first try and comes back through here, adding another +1. Measured on ree-cloud-5 2026-08-14: [ahead 34] at 02:30Z -> [ahead 104] at 04:06Z, ~45 orphans/hour."* |
| **Credential failure** | **RULED OUT** | 115 successful `update by push` reflog events on 09-09, 23 on 09-10. Pushes authenticate fine. |
| **Deliberate `--no-push`** | **RULED OUT** | Every writer defaults to push — see §1.3 file:line table. |
| **Clinical-hours push hold** (plausible on paper — `.git/hooks/pre-push` holds any push containing a personal-identity commit, and `nooarche` authors 817 commits/30d) | **RULED OUT — guard file absent** | `/Users/dgolden/REE_Working/REE_assembly/.git/hooks/pre-push:18` — `[ -f "$GUARD" ] \|\| { [ -x "$0.local" ] && exec "$0.local" "$@"; exit 0; }`. `$GUARD` resolves to `/Users/dgolden/REE_Working/scripts/clinical_hours_guard.py`, **which does not exist**. The hook chains straight to `pre-push.local` and never holds. This is worth knowing independently: the clinical-hours guard is silently inoperative. |
| **Helper push is best-effort and fails open** | **PARTLY — but it is the CONVERGENCE that fails open, not the push** | `ree_commit.py:2485` `_converge_after_push` docstring: *"It is FAIL-OPEN: the content is already on origin by then, and a convergence problem must never turn a successful commit+push into a failure."* Push failure exits 1 (`:4022`). Convergence failure exits 0. |

**The causal chain, established:**
origin advances from Cloud/Hub → local push is non-fast-forward → `ree_commit` retries via
throwaway worktree and **lands the content successfully as a new-SHA twin** → local branch
keeps the original as an orphan → `_converge_after_push` tries to move the ref, is refused →
fail-open, exit 0, nobody notices → **next push is now also non-fast-forward** → +1 orphan.

---

## 4. Is there a converger, and why is it not converging?

Yes: `/Users/dgolden/REE_Working/scripts/ref_convergence.py` (1443 lines) delegating the ref
move to `/Users/dgolden/REE_Working/scripts/safe_adopt_ref.py` (433 lines). It is
well-designed and it is running. Live read-only audit of the current 12-commit ahead range:

```
ref_convergence: audit of master vs origin/master -- 12 ahead, 8 proven, 4 unproven
    PROVEN   e3fddf1c8f  patch-identical upstream   igw-ledger: update
    PROVEN   00eea816b4  patch-identical upstream   assay-c: correct the G-LIFE readiness gate
    PROVEN   725fcd8583  patch-identical upstream   assay-c: refined developmental Assay C spec
    PROVEN   67c5328e27  patch-identical upstream   governance-flag: close 3 residual flags
    PROVEN   29c1ea0a3e  patch-identical upstream   governance-flag: resolve 26 decision-docket flags
    PROVEN   798d816ed4  patch-identical upstream   igw-ledger: update
    PROVEN   06d4aca774  patch-identical upstream   governance-flag: resolve 50 flags
    PROVEN   be59b22b21  patch-identical upstream   governance: apply 54 adjudicated flag edits
    UNPROVEN 26708abc22  lit-pull: ARC-055 / ARC-056
    UNPROVEN c8116c399b  governance: apply 26 user-approved decision-docket flags
    UNPROVEN 43f6e5713e  igw-workset: regen -- 250 items, 29 ready, 0 in flight
    UNPROVEN 853e336bbb  docs: audit replay-dependent interface maintenance
```

**Partial proof is not proof: one unproven commit refuses the whole move** (stated at
`ref_convergence.py:56`). 8 of 12 provable, and the move is still refused.

### 4.1 Route-by-route: why each of the three proof routes fails here

**Route B (cherry-pick `-x` backreference) — proves 0 of 12.**
Measured directly: **none of the 11 origin-side twins carries a `(cherry picked from ...)`
trailer.** Yet 9.9% of all origin commits over 7 days do. The conclusion is specific: today's
twins were **not** produced by `ree_commit.py`'s push-retry path. They were produced by the
**hand throwaway-worktree cherry-pick** the 108-flag governance session used to land its work
after every push was rejected. A hand `git cherry-pick` without `-x` writes no backref, so
the primary go-forward proof route is blinded by the very workaround used to escape the wedge.
**The manual workaround manufactures the next wedge.**

**Route C (registry net-item containment) — proves 0 of 12, and is structurally inert in this repo.**
`ref_convergence.py`'s `REGISTRY_SPECS` is exactly:
```python
REGISTRY_SPECS = {
    "TASK_CHIPS.json":  RegistrySpec("json", "chips",  ("chip_ref",)),
    "TASK_CLAIMS.json": RegistrySpec("json", "claims", ("session_id", "claimed_at")),
}
```
**Neither file exists in REE_assembly.** Both live in the `/Users/dgolden/REE_Working` root
repo. Route C was designed and measured against the *umbrella* checkout (the 2026-08-18
"17 → 1" measurement in its docstring is explicitly *"on DLAPTOP /Users/dgolden/REE_Working
master"*), and it has **no allowlisted path in REE_assembly at all**. It cannot adjudicate
anything here. Corroborating symptom: the audit still emits
```
  Registry items NOT present upstream (2):
      TASK_CHIPS.json  :: unloadable at merge-base, tip or upstream
      TASK_CLAIMS.json :: unloadable at merge-base, tip or upstream
```
— two spurious "content a ref move would drop" lines for files that do not exist in this
repository. Any operator reading that audit is being told to worry about two phantom items.

**Route A (patch-id via `git cherry`) — proves 8 of 12, and is the only route working here.**
It carries the entire load, and it fails on exactly the shape REE_assembly is full of:
whole-file regenerated JSON.

### 4.2 Are the 4 refusals true or false negatives?

Tested by comparing every path each unproven commit touches against `origin/master`:

| Commit | paths | identical upstream | differ | verdict |
|---|---:|---:|---:|---|
| `43f6e5713e` igw-workset regen | 2 | **2** | 0 | **FALSE NEGATIVE** — content is byte-identical upstream; route A refuses only because the intermediate *diff* differed |
| `c8116c399b` governance apply 26 | 17 | **14** | 3 | **near-false negative** — the 3 are whole-file JSON registries (`claim_evidence.v1.json`, `substrate_status_snapshot.json`) and a generated `pending_review.md` |
| `26708abc22` lit-pull ARC-055/056 | 14 | **12** | 2 | **near-false negative** — the 2 are `claim_evidence.v1.json` (**261 local-only lines vs 261 origin-only lines — a reordering, not a content difference**) and a 1-line `INDEX.md` ordering difference |
| `853e336bbb` docs replay-dependent | 1 | 0 | 1 | **TRUE NEGATIVE** — `docs/thoughts/2026-09-09_hippocampal_replay_interface_maintenance_supplement.md`: **151 lines exist only locally**, 156 only upstream. Genuinely divergent prose. A ref move would destroy real work. |

**Score: 1 true negative, 1 clean false negative, 2 near-false negatives.**
`ref_convergence` is right to refuse — but it is right for **one** commit out of twelve, and
that one commit holds the other eleven hostage. This is the "ROUTE C IS A LARGE REDUCTION,
NOT A CURE" caveat in its own docstring playing out: *"One permanently-unprovable item still
refuses the whole move, by design."*

Note also that `853e336bbb` and its origin twin `38bf293cd9` are **two different sessions
independently writing the same prose document** — the local one committed at 07:34, the
origin one at 07:28. That is not a git problem at all; it is two writers racing on one file.

### 4.3 The file shape that defeats route A

`evidence/planning/inter_governance_workset.v1.json` is **490 KB**, and
`inter_governance_workset.md` is **297 KB**. A single `igw-workset: regen` commit rewrites
them wholesale — measured on `71e6394c30`: **1471 insertions, 1471 deletions across 2 files**,
i.e. a 100% rewrite. Two machines (Mac 226/30d, Hub 60/30d) regenerate this same derived
artifact on independent cadences. Two whole-file regenerations of the same logical state
**can never share a patch-id**, and being derived output they will never carry a `-x` backref
either. Every one of these is permanently unprovable by every route the converger has.

`igw-ledger` is the same shape at 4× the volume: **793 Mac + 89 Hub commits/30d**, 17% of
which already land as twins.

---

## 5. Why REE_assembly and not ree-v3

`/Users/dgolden/REE_Working/ree-v3` at the same moment: **`0 behind, 0 ahead`. Clean.**

| | REE_assembly | ree-v3 | ratio |
|---|---:|---:|---:|
| commits / 30d | **5224** | 785 | **6.7×** |
| local writers on this box / 30d | **2477** (Mac 1660 + nooarche 817) | 401 (Mac 146 + nooarche 255) | **6.2×** |
| distinct automated local writer classes | **≥5** (igw-ledger, igw-workset, governance-flag, lit-pull, thought-intake) | ~1 | |
| dominant prefix | `phase3-heartbeats` 2265 — **remote-only** | `phase3-queue` 299 — **remote-only** | |
| largest *local* writer | `igw-ledger` 885 | none comparable | |
| contested whole-file artifacts | `inter_governance_workset.v1.json` 490 KB, `claim_evidence.v1.json`, `governance_flags.v1.json`, `substrate_status_snapshot.json` | few | |
| route C allowlist coverage in-repo | **0 paths** | 0 paths | |

Three differences, in order of weight:

1. **REE_assembly has high-frequency *local* automated writers; ree-v3 does not.** ree-v3's
   bulk traffic (`phase3-queue`, 299) originates on the Cloud Worker and arrives by fetch.
   It only ever makes this checkout *behind*, which fast-forwards cleanly. REE_assembly's
   bulk traffic (`igw-ledger` 885, `igw-workset` 287, `governance-flag` 271 — **1443
   commits/30d, 48/day**) originates **here**, so every one is a chance to be
   non-fast-forwarded and turned into an orphan.
2. **Three machines write the same derived artifacts.** Mac + Hub both run the igw routine
   tick against the same 490 KB whole-file registries. ree-v3 has no equivalent.
3. **File shape.** Whole-file regenerated JSON defeats patch-id proof by construction, and
   route C's allowlist covers none of REE_assembly's registries.

---

## 6. Ranked root causes — by how much observed divergence each explains

**1. Orphan-twin generation by the push-retry path, uncleared by a refused converger. — explains ~90%+ of the *magnitude*.**
12/12 of the current ahead-commits are twins; 8/12 patch-identical; 11/11 checked twins are
already reachable from origin. This is not a contributing factor, it is essentially the
whole ahead-count. Documented as designed behaviour and as a known defect at
`/Users/dgolden/REE_Working/scripts/ree_commit.py:2323` (`retry_push_via_worktree`) and
`ref_convergence.py:14-38`. Direct measurement of the amplification is already in the
codebase: *~45 orphans/hour* once wedged.

**2. The all-or-nothing convergence gate meeting a single genuinely-divergent file. — explains the *duration*, i.e. why ~10 episodes/14d last 3–13 h instead of 1 minute.**
8 of 12 provable and the move still refused. Today the single blocker is one prose file
(`853e336bbb`) with 151 local-only lines. The gate is correct — but its all-or-nothing
structure converts one unprovable commit into an unbounded wedge. The 35 transient episodes
prove the converger works whenever the range happens to be 100% provable; the 10 long ones
are all "one commit spoiled it".

**3. Route B blinded by the manual escape hatch. — explains why wedges *recur* rather than clear.**
Zero `-x` backrefs on today's twins against a 9.9% baseline. Every time an operator escapes
a wedge by hand-cherry-picking (as the 108-flag session did), they land untraceable twins
that route B can never prove — seeding the next wedge. This is the recurrence engine, and it
matches the codebase's own observation that *"the wedge re-formed ~16 minutes after a hand
repair cleared it."*

**4. Whole-file regenerated registries written by two machines. — explains which commits become permanently unprovable.**
490 KB files rewritten 100% per commit, by Mac and Hub independently. No patch-id can match.
This is the steady supply of route-A-unprovable commits that cause (2) to fire.

**5. Route C structurally inert in this repo. — explains why the 2026-08-18 fix did not help here.**
`REGISTRY_SPECS` allowlists only `TASK_CHIPS.json` / `TASK_CLAIMS.json`, **neither of which
exists in REE_assembly**. The "17 → 1 unproven" improvement was measured on the umbrella repo
and delivers **zero** benefit here. Additionally it emits 2 spurious warnings per audit.

**6. Convergence failure is fail-open and invisible. — explains why nobody notices for hours.**
`_converge_after_push` (`ree_commit.py:2485`) returns success on convergence failure by
design. Nine consecutive refusals were recorded to a state file and surfaced to no one until
this morning's digest degraded. Detection latency, not cause — but it is why a 12-hour wedge
is possible.

**Not causes (actively ruled out):** credential failure (115 pushes succeeded 09-09);
deliberate `--no-push` (all writers push by default, §1.3); clinical-hours push hold
(`clinical_hours_guard.py` does not exist, hook is inoperative); writers that commit and
never push (none found).

### Where the evidence is ambiguous — stated plainly

- I measured a **single day's** ahead-range in twin/patch detail (12 commits, exhaustively).
  The 14-day *rate* is solid, but the claim "~90%+ of magnitude is twins" is extrapolated
  from today's 12/12 plus the 30-day 30% backref baseline. It is very likely right; it is
  not measured across all 57 episodes.
- The 8.22 h episode of 09-07/08 reached **76 ahead / 76 behind** — a symmetric shape I did
  not decompose. It may have a different cause (a rebase or a reset) than the twin loop.
- `--check`'s persisted state (20 ahead / 3 unproven, 06:05Z) and the live `--audit`
  (12 ahead / 4 unproven, 09:45Z) disagree because the persisted file is stale. I have not
  determined whether `--check` is *supposed* to refresh; if a monitor reads `--check`, it is
  reading hours-old numbers.

---

## 7. Coordinator-alignment assessment

Read: `/Users/dgolden/REE_Working/REE_assembly/evidence/planning/task_claim_chip_coordinator_migration_plan.md`
(PHASE-0 done 2026-08-26; PHASE-1 shadow done 2026-09-06). Stated direction: move
coordination data *"off per-machine git commits onto the Phase 3 coordinator (ree-cloud-1)…
GitHub becomes the materialization/fallback path, not the live check every session reads."*

The findings map onto that direction unusually cleanly, because **the writers causing the
divergence and the writers the plan wants to move are nearly the same set.**

### 7.1 Candidates to move behind the coordinator

| Writer | Local commits/30d | Why it qualifies |
|---|---:|---|
| **`igw-ledger`** (`igw_routine_tick.py`) | **793 (Mac)** | Pure coordination bookkeeping. Regenerated, not authored. 17% already land as twins. Largest single local writer in the repo. |
| **`igw-workset`** (`igw_routine_tick.py`) | **226 (Mac)** | Derived artifact — a 490 KB whole-file regeneration of state held elsewhere. Two machines regenerate it independently. **Permanently unprovable by every convergence route by construction.** Materialize to git on a cadence from the coordinator instead. |
| **`governance-flag`** (`governance_flag.py`) | **266 (Mac)** | A registry of open/resolved flags — coordination state, not scientific content. **37.6% twin rate, the highest measured.** The 108-flag session's total push failure was this writer. |

**Together: 1285 of the Mac's 1660 automated local commits (77%), and by the twin-rate
evidence the large majority of orphan production.** Moving these three behind the
coordinator would take the local automated commit rate from ~43/day to ~10/day and remove
the entire whole-file-regeneration class from git — which is precisely the class that
route A and route B cannot prove.

This is also the same shape as the migration already completed: `TASK_CLAIMS.json`,
`TASK_CHIPS.json` and `WORKSPACE_STATE.md` moved this way and now arrive as
`phase2b-registry` materializer commits from a **single** writer, which is why they no
longer appear anywhere in REE_assembly's local-writer inventory.

### 7.2 Writers that must stay local git writers

| Writer | Why it must stay |
|---|---|
| Interactive `nooarche` prose and evidence — `docs/thoughts/*`, `evidence/literature/*`, assay specs, `lit-pull` records, `thought-intake` | This is the **authored research content**, not coordination state. Git is the correct store: it needs review, history, and blame. Today's **single true-negative refusal (`853e336bbb`, 151 local-only prose lines) is exactly this class** — and the converger refusing to discard it is the system working correctly. |
| `scripts/`, skills, contracts | Executable code. `ref_convergence.py` explicitly states *"route C never adjudicates executable code."* Must stay under ordinary review. |
| `phase3-heartbeats`, `phase3` | Already coordinator-side (Cloud Worker). Correctly not local. No action. |

### 7.3 Against-the-grain calls — fixes that should be rejected

1. **Another local-push retry loop.** `retry_push_via_worktree` already retries 3× with a
   rebase lock. More retrying does not help: the pushes *succeed*. Adding retry attacks a
   step that is not failing.
2. **Adding `inter_governance_workset.v1.json` / `governance_flags.v1.json` /
   `claim_evidence.v1.json` to `REGISTRY_SPECS` so route C can adjudicate them.** This is
   the tempting fix — route C is inert here purely because its allowlist names two files
   that do not exist in this repo. But it means **building more convergence machinery around
   artifacts that the plan says should stop being per-machine git commits at all**, and it
   raises `MAX_UPSTREAM_SCAN_COMMITS` pressure on a 490 KB file (the cap comment already
   warns that an over-long scan *"MANUFACTURES the divergence it is trying to prove away"*).
   Legitimate as a **time-boxed stopgap**; call it out explicitly as against the grain, and
   do not let it become the answer.
3. **Any new local automated writer.** Straightforwardly against the plan.
4. **Auto-adopting with `--allow-discard`, or loosening the all-or-nothing gate.** Today's
   range contains one commit with 151 lines of prose that exist nowhere else. Loosening the
   gate destroys it. The gate is not the bug.

### 7.4 Two fixes that are *with* the grain and cheap

- **Make the manual escape hatch use `-x`.** Every hand cherry-pick that lands work around a
  wedge should carry `(cherry picked from ...)`. Zero backrefs on today's twins against a
  9.9% baseline is the recurrence engine (cause 3), and this closes it at essentially no
  cost — it makes route B work for exactly the commits it was designed for.
- **Surface the fail-open.** `ree_ref_convergence_wedge.json` recorded 9 refusals over 11.5 h
  and nothing read it until the digest degraded. Also fix or scope `--check`, which is
  reporting stale counts (20/3 vs the live 12/4). Detection only — it changes no write path.

---

## 8. One-paragraph answer

REE_assembly diverges because it is the only repo in the fleet with **high-volume automated
writers running on the shared checkout itself** (1443 coordination commits/30d from
igw-ledger, igw-workset and governance-flag, versus ree-v3 where the bulk traffic arrives by
fetch). Origin advances ~92 commits/day from Cloud and Hub, so those local pushes are
routinely non-fast-forward; `ree_commit.py` correctly lands them anyway as cherry-picked
twins, and correctly declines to move the branch ref onto origin while any discarded commit
is unproven. The result is a checkout that is ahead by commits origin already has — 12/12
twinned, 8/12 patch-identical today. That state is self-sustaining and clears only when the
converger can prove **every** commit in the range, which fails whenever one whole-file
regenerated registry or one genuinely-edited prose file is in the way. Measured: **35.5% of
observations diverged, ~4.1 episodes/day, ~0.7 multi-hour wedges/day, median wedge ~6.6 h,
25.4% of wall-clock spent ahead.** The three writers producing most of the orphans are all
coordination-data writers the coordinator migration plan already wants to move; the writers
that must stay in git are the authored research content — which is also, precisely, the one
commit that legitimately blocked convergence today.
