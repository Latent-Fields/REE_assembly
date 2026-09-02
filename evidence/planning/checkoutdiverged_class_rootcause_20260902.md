# checkoutdiverged: class root-cause investigation

**Status: AWAITING USER REVIEW**

Date: 2026-09-02T22:11:43Z
Session: `learning-checkoutdiverged-20260902` (`/metaworker-learning`)
Chip: `chip-20260901-checkoutdiverged-rootcause-learning` (diagnosis only, no fix)
Sibling prior art: `refwedge_class_recurrence_investigation_20260826.md`

---

## 0. One-sentence finding

The class is not one defect but **two independent ones that arrived within 24 hours of each
other**: the 2026-08-28 coordinator cutover removed ~97% of the client-side git write traffic
that had been the de-facto follow-origin driver, and the detector added the next day to catch
the resulting drift **can fire at most once per (host, repo, branch) for all time** -- so the
class has been silent in the ledger since 2026-08-30 while continuing at ~2.9 episodes/day.

---

## 1. Recurrence is genuine (skill Step 1)

Required: >=2 occurrences of the same root cause, counted from resolution notes, not chip
existence. Established well past that.

| # | host | repo | observed | behind | ahead | shape |
|---|---|---|---|---|---|---|
| E1 | ree-cloud-5 | REE_assembly | 08-29T18:06Z | 8 | 2 | diverged |
| E2 | DLAPTOP | REE_Working | 08-29T19:08Z | 81 | 68 | diverged |
| E3 | ree-cloud-4 | REE_Working | 08-30T02:34Z | 16 | 0 | behind |
| E4 | ree-cloud-5 | REE_Working | 08-30T06:29Z | 50 | 0 | behind |
| E5-E7 | ree-cloud-5 | REE_Working / REE_assembly / ree-v3 | 08-30T15:05Z | 6 / 5 / 5 | 0 | behind |
| E8 | DLAPTOP | REE_Working | 09-01T15:29Z | 4 | 4 | diverged |
| E9 | ree-cloud-4 | REE_Working | 09-01T~15:50Z | **305** | 0 | behind |
| E10 | ree-cloud-5 | REE_Working | 09-02T20:08Z | 70 | 15 | diverged |
| E11 | ree-cloud-4 | REE_assembly | 09-02T21:14Z | -- | 5 | diverged (detached mid-rebase, 8 UU) |
| E12 | ree-cloud-4 | REE_Working | 09-02T~18:22Z | -- | 8 | diverged (stuck rebase) |

**12 episodes / 4.13 days = 2.90 episodes/day**, across 4 hosts and 3 repos. Six purely behind,
six genuinely diverged, and the split is **chronological**: the 08-30 cluster was all
`ahead == 0`; every 09-02 episode is `ahead > 0`. The framing carried in the escalation chips
("ahead=0, ordinary fast-forward each time") was true only for the middle of the window. The
class is widening in mechanism, not just recurring.

E9 is the cost statement: ree-cloud-4 sat **305 commits behind** with its dispatcher reading a
stale coordination-plane pause as active, refusing to dispatch for roughly two days, with no
alarm.

---

## 2. Root cause D1 -- the follow-origin driver was a side effect, and the cutover removed it

These checkouts had no dedicated puller for most of their life. They advanced as a **side effect
of their own push traffic**: an ordinary branch push gets rejected, `retry_push_via_worktree`
lands a twin on origin, and `_converge_after_push` -> `ref_convergence` -> `safe_adopt_ref`
fast-forwards the local ref. `ref_convergence.py:331-334` states the assumption in as many
words -- *"a checkout that is merely behind still converges on every push"*.

That assumption held only while the boxes were writing. Measured directly from
`origin/master` history (REE_Working), client-authored `claim:` / `chips:` commits per day:

| day | claim/chip client writes | hub materializer | total |
|---|---|---|---|
| 08-21 | 307 | 0 | 381 |
| 08-22 | 709 | 0 | 944 |
| 08-25 | 374 | 0 | 548 |
| 08-26 | 483 | 0 | 662 |
| 08-27 | 548 | 0 | 648 |
| **08-28 (cutover)** | **187** | **146** | 543 |
| 08-29 | **23** | 316 | 693 |
| 08-30 | 28 | 218 | 327 |
| 09-01 | 12 | 194 | 374 |
| 09-02 | 14 | 240 | 398 |

**Client write traffic fell ~97% on 2026-08-28**, the coordinator cutover date, while origin's
total advance rate held at ~400 commits/day (401 in the last 24h, 21.5/hour). The Mac's
`~/.ree_coordinator_client.json` carries `suppress_git_write: true`: `task_claim.py` and
`chip_ledger.py` now POST to the hub and make **no local git operation at all**. The writes did
not move to a different local path -- they stopped being local writes.

So the relationship inverted. Before the cutover the box that wrote was also the box that
pulled. After it, the **hub** authors the commits (246 of 406 in the last 24h are
`REE Automation (Hub)`, foreign to every client checkout) and the clients have almost nothing
left to push. The first checkoutdiverged episode is dated **2026-08-29**, the first full day
after the cutover.

This supersedes, without contradicting, the sibling investigation's account. That doc's LATCH
explains `refwedge`. It does not explain this class -- and note the two are near-inverses:
refwedge pins the ref via a *refusal* (`ahead` grows, `--check` exits 4), whereas
checkoutdiverged never asks the ref to move at all (`ahead == 0` actively **clears** wedge
state per `ref_convergence.py:308-310`, so `--check` reports healthy). `metaworker-repair`
SKILL.md:189 already records that asking the wrong one of those two questions was a confirmed
75-minute outage.

### D1a -- the pullers that do exist, and why they do not close it

| host | mechanism | cadence | covers REE_Working? | live? |
|---|---|---|---|---|
| DLAPTOP | `ree_git_sync_repair.sh` (launchd `com.ree.gitsyncrepair`) | **3h** | yes | yes, but see D2 |
| DLAPTOP | `serve.py:_auto_pull` | 5 min | **no** (REE_assembly + ree-v3 only) | only while serve.py runs |
| cloud-4/5 | `ree-metaworker-autosync.timer` -> `safe_adopt_ref.py` | 10 min | yes (umbrella only) | **yes**, deployed 2026-09-01 |
| cloud-4 | `ree-git-sync-repair.timer` | 30 min | **no** (REE_assembly + ree-v3 only) | timer active, **last journal entry 2026-07-28** |
| cloud-5 | `ree-git-sync-repair.timer` | -- | -- | **not installed at all** |

Two structural gaps fall straight out of that table:

- **Cadence inversion on the Mac.** The puller runs every **3h**; the detector fires at **1.0h**;
  trunk advances at 21.5 commits/hour. A chip is reachable on a *completely healthy* Mac
  between two successful pulls. The threshold was measured against p90 local-branch-advance
  gaps (30.1 / 55.8 min on the cloud boxes) -- i.e. against the pre-cutover write-driven cadence,
  not against the puller's period.
- **Nothing pulls the work repos on the cloud boxes.** `ree-metaworker-autosync.sh` is umbrella-only
  by design; the cloud `ree-git-sync-repair.sh` covers REE_assembly and ree-v3 but is dead on
  cloud-4 and absent on cloud-5. Episodes E1, E6, E7 and E11 are exactly that gap.

Live state at the time of writing (all three hosts, fetched fresh): DLAPTOP behind 3/0;
ree-cloud-4 REE_Working behind 6/0 and REE_assembly behind 3/0; ree-cloud-5 behind 1/0 and 0/0.
Small numbers -- but the detector's own state file shows its clock **currently running** on
this box (`first_seen_at: 2026-09-02T21:56:50Z`, behind 7).

---

## 3. Root cause D2 -- the Mac's puller is blocked by the very files the coordinator owns

`ree_git_sync_repair.sh` refuses to attempt the fast-forward when any *blocking* tracked dirt
exists (line ~285, `BEHIND_NOT_SYNCED`). Today's live log:

```
2026-09-02T08:43:35Z REE_Working BEHIND_NOT_SYNCED (ahead=0 behind=13) -- ff blocked by uncommitted tracked change(s): TASK_CLAIMS.json
2026-09-02T11:43:47Z REE_Working BEHIND_NOT_SYNCED (ahead=0 behind=1)  ... TASK_CLAIMS.json
2026-09-02T14:43:58Z REE_Working BEHIND_NOT_SYNCED (ahead=0 behind=6)  ... TASK_CLAIMS.json
2026-09-02T17:44:08Z REE_Working NEEDS_HUMAN (wedged: ahead=7 behind=17) -- uncommitted non-telemetry change: TASK_CLAIMS.json
2026-09-02T20:44:17Z REE_Working SYNCED (ff-only, was behind 6)
```

**Four of five runs today were blocked, every one of them on `TASK_CLAIMS.json`.** And
`TASK_CLAIMS.json` is precisely a file the coordinator now owns and the hub materializer
renders: since the cutover no session writes it directly (a blocking `PreToolUse` hook enforces
that), so a local modification to it is a HEAD/worktree skew artifact, never live work.

The 17:44 line is the compounding step: blocked repeatedly while behind, the checkout eventually
acquires local commits and crosses from `behind` into `ahead > 0` -- which is the observed
08-30 -> 09-02 escalation from the benign shape to the audit-requiring one. The mechanism is
self-aggravating, and being blocked is what aggravates it.

This is already on the record as owed work: `WORKSPACE_STATE.md:1195-1199`, repairing E9,
notes that `safe_adopt_ref`'s skew repair refused those two files -- *"right in general, but for
these two hub-rendered, coordinator-authoritative files a local modification is provably never
live work. **Worth encoding.**"*

---

## 4. Root cause D3 -- the detector can fire once per host, ever

This is why the class looks resolved and is not.

- `_divergence_findings` builds a **time-free, stable** ref:
  `chip-checkoutdiverged-<host>-<repo>-<branch>` (`hygiene_routine_tick.py:9199`).
- The finding dict sets no `episodic` key, so it takes the **non-episodic** mint path
  (`run_tick`, line 9414 branches on `f.get("episodic")`).
- `chip-checkoutdiverged-` is **not** in `_EPISODIC_STANDING_PREFIXES`
  (line 5217: `("chip-refwedge-", "chip-queuefloor-", "chip-daemondrift-")`), so it gets no
  generation minting, no `-g2`, no hysteresis.
- `chip_ledger.py:3062` is monotone: `"chip_ref %s already recorded -- not appending again"`.
- The prefix **is** in the absence-done set, so the chip auto-resolves when the condition clears.

Net: mint once -> auto-resolve -> **never mint again**. There are exactly three possible auto
chips for `REE_Working/master` (dlaptop, cloud-4, cloud-5); all three were minted and closed on
2026-08-29/30. The ref space is saturated and the detector is now permanently blind on every
host.

The system already caught itself doing this, in the ledger, on 2026-09-02
(`chip-20260902-refconverge-cloud5-master-wedge`): *"The fixed chip_ref
`chip-checkoutdiverged-ree-cloud-5-ree-working-master` already exists as status:done from
2026-08-30 and `chip_ledger.py record` refuses to reopen a duplicate chip_ref, so this instance
needed a new dated ref to be trackable."* Episodes E8-E12 all reached the ledger only because a
human or healer hand-minted a dated ref.

**This is the third occurrence of the identical defect in this codebase.** `chip-20260816-refwedge-chipref-recurrence`
("hygiene ref_convergence_wedge chip_ref cannot flag a RECURRING wedge") and
`chip-20260817-hygienetick-refwedge-recurrence-fix` ("monotone resolution silently blocks
re-chipping a recurring wedge") are the same bug in `refwedge`, fixed by W5a generation minting
which landed 2026-08-28/29. **Source 25 was written on 2026-08-29 -- the day after the fix -- and
did not adopt it.** That, not the drift itself, is the properly *recurring* thing here, and it is
what makes this a `/metaworker-learning` job rather than another repair.

Two narrower detector gaps, same source:

- `_DIVERGENCE_REPOS = ("REE_Working",)` -- REE_assembly and ree-v3 are unmonitored, though 4 of
  12 episodes were on them (E1, E6, E7, E11), including the class's *first* observed instance.
- `scan["ahead"]` is used only in the prompt and tldr text, never in the fire decision. A
  zero-risk fast-forward and a loss-hazard audit arrive under one title and one chip_ref. (The
  prompt does branch correctly on `ahead == 0`, so this is a triage/priority defect, not a
  safety one.)

---

## 5. Candidate remedies (NOT built -- for decision)

Ordered by measured evidence, not by ease.

- **R1 -- episodic-ise source 25.** Add `chip-checkoutdiverged-` to
  `_EPISODIC_STANDING_PREFIXES` and set `episodic` on the finding, so the class re-mints as
  `-g2`, `-g3` with the existing hysteresis, exactly as `refwedge` does. Smallest change,
  restores visibility, and re-uses machinery already proven on a sibling class. **Until this
  lands, every other measurement of this class is unreliable, because the detector cannot
  observe recurrence.** Recommended first, alone.
- **R2 -- unblock the Mac's fast-forward on coordinator-owned registries.** Teach
  `ree_git_sync_repair.sh`'s blocking-dirt gate to consult per-row subsumption rather than
  treating `TASK_CLAIMS.json` / `TASK_CHIPS.json` dirt as blocking. **See the held-out check
  below: this must reuse `hygiene_routine_tick._registry_rows_subsumed` (line 4288), never a
  basename exemption.** Addresses the measured 4-of-5 daily block rate and the behind -> diverged
  escalation.
- **R3 -- cadence.** Mac puller 3h vs detector 1.0h vs trunk 21.5 commits/hour. Either raise the
  puller to the 10-min cadence already deployed on cloud-4/5, or re-derive the threshold against
  the post-cutover advance rate. Cheap; needs a decision on which side moves.
- **R4 -- cover the work repos on the cloud boxes.** `ree-git-sync-repair` is dead on cloud-4
  (last run 2026-07-28) and absent on cloud-5; `ree-metaworker-autosync` is umbrella-only. E1,
  E6, E7, E11 sit in this gap.
- **R5 -- extend `_DIVERGENCE_REPOS`** past REE_Working. Only meaningful after R4, or it just
  chips a condition nothing can repair.

**Deliberately not proposed:** relaxing `safe_adopt_ref`'s refusal, or any heuristic
already-upstream proof route. CLAUDE.md forbids the latter by name, and the 2026-08-15
measurement (15 of 26 commits argued content-safe *by shape* were genuinely stranded) is the
standing reason.

---

## 6. Held-out check (CLAUDE.md "General Rules"; GOV-HELDOUT-1)

Run against **R2**, the only proposal that relaxes an existing safety refusal and therefore the
only one where getting it wrong loses work. Cases are ones R2 was not written from; each is one
where the naive form and the per-row form give **different** answers.

| # | case | old (block on any dirt) | naive R2 (exempt by basename) | per-row R2 | verdict |
|---|---|---|---|---|---|
| 1 | 2026-08-15 route-A audit: 15 of 26 commits argued content-safe by shape were **genuinely stranded** | blocks; safe but stalls | proceeds; can discard genuinely-local rows | refuses -- rows not subsumed | naive form **FAILS** |
| 2 | detector-FP campaign fix 2a (`d82e75808`, 2026-08-30) | blocks | basename suppression -- the commit message pins this as the trap | per-row proof, "status monotone, closure stamps equal-or-later, notes preserved" | naive form **FAILS**; per-row already adopted elsewhere |
| 3 | `chip-20260828-taskclaim-amend-hollow-ack`: local row differs only in note content | blocks | proceeds; silently drops the amended note | flagged -- the amend-hollow-ack shape is explicitly still caught | naive form **FAILS** |
| C | today's Mac log: TASK_CLAIMS.json dirty, all rows hub-rendered | blocks (4 of 5 runs) | proceeds | proceeds | **degenerate control** -- does not discriminate; named, not counted |

Three differing cases, one named degenerate control. **The check changed the proposal**: R2 was
first drafted as a basename exemption for the two registry files, which case 1 and case 3 both
falsify, and case 2 shows the codebase already learned this and built `_registry_rows_subsumed`
for exactly it. R2 as it now stands reuses that function rather than re-deriving the judgement.

**Honest counterweight:** this check cost roughly 25 minutes of archaeology and it is not free.
It is worth it here specifically because R2 relaxes a refusal that guards uncommitted work; R1,
R3, R4 and R5 add or re-time detection and repair without weakening any guard, and I did not run
a separate held-out check on those. If the decision is to take R1 alone, no held-out check was
required for it.

---

## 7. What this investigation did NOT establish

- **No before/after rate comparison is offered, deliberately.** Source 25 was added 2026-08-29,
  one day after the coordinator cutover. Any rate computed across that boundary measures the
  detector, not the class -- the same methodological trap the sibling investigation documented
  for the 2026-08-18 refwedge detector change. The 2.90/day figure is a **lower bound** over a
  single post-detector window, assembled partly from prose in chip prompts, and it under-counts
  wherever nobody hand-minted a ref.
- **The R1-aggravation hypothesis is unresolved.** The sibling investigation's R1 (remote-tip
  gated on ahead-and-not-wedged) landed 2026-08-28T12:34Z and routes more writes onto the
  remote-tip path, which by design never moves the local ref. That would aggravate this class.
  It is confounded beyond separation with the coordinator cutover the same day, and the
  write-volume collapse measured in section 2 is much the larger effect, so I did not attempt to
  apportion between them.
- **`chip-20260904-refwedge-r1-rate-cost-remeasure`** (due ~2026-09-04) is the sibling class's
  own falsifiable re-measure and is still open. It should not be folded into this class.
