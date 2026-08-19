# Why four cooldown fixes have not held: the gate is mis-sited one layer too deep

**Status: AWAITING USER REVIEW**

Chip `chip-20260819-metaworker-learning-cooldown-4-fixes-failed`, routed here by the user's
2026-08-19 `AskUserQuestion` decision on `chip-20260819-usagelimit-cooldown-not-holding-5th`
("diagnose first, don't patch a 5th time"). `/metaworker-learning` Step 3 output. No code
changed by this session -- diagnosis and design only, per the chip's explicit constraint.

---

## 1. The question

`scripts/dispatch_usage_cooldown.py` exists to stop `metaworker-dispatch` from re-attempting
a headless launch every 5 minutes through an account-wide API usage-limit outage. Four chips
against this mechanism are `done`:

| # | chip | landed | surface |
|---|------|--------|---------|
| 1 | `chip-20260817-dispatch-usagelimit-noattempt-cooldown` | REE_Working `b8310c9c` + `74201b3c73` | built the gate (`check`) + stamp (`stamp`), wired into SKILL.md Step 4-pre (gate) and Step 4b (stamp) |
| 2 | `chip-20260818-cooldown-stamp-by-construction` | REE_Working `2c26adda`/`6bbb4e73`/`376102b4` | made the stamp automatic: `check_deferral_exit.py` calls `dispatch_usage_cooldown.autostamp()` itself on a USAGE-LIMIT verdict |
| 3 | `chip-20260818-cooldown-gate-observed-at-misparse` | REE_Working `27cb76dd`/`552c84b7`/`704d6135` | fixed the observation-instant allowlist + ISO reset-time parsing inside that same gate |
| 4 | `chip-20260818-cooldown-clear-cannot-clear-ledger-trigger` | REE_Working `419263d1` | fixed `clear`'s watermark semantics on the ledger-prose fallback path |
| (4b) | `chip-20260818-doa-classify-unconditional-at-launcher` | REE_Working `75d05b97` | made Step 4c's *child-worker* DOA classification unconditional (`scripts/check_worker_launch.py`) |

Despite all five landing, the gate has now failed to hold a **5th** time: `chip-20260819-usagelimit-cooldown-not-holding-5th`
reported 68+ no-op cycles against a weekly limit (resets 2026-08-21T18:00Z) that was never
stamped into `metaworker_dispatch_cooldown.json` at all -- the live state file's newest
observation is still the 2026-08-18T22:27:35Z *session*-limit stamp, already expired.

The user's question, verbatim: is the mechanism **mis-sited** (an advisory/in-session
instruction rather than a launcher-side gate), or were the four fixes each correct for a
*different surface*?

## 2. Answer: mis-sited. All five fixes share one surface; the dominant failure lives one layer up.

**All five landed fixes operate entirely inside SKILL.md-instruction-driven, in-session
logic** -- `dispatch_usage_cooldown.py`'s `check`/`autostamp`, and `check_deferral_exit.py`
which calls it. That logic can only run in two circumstances:

- **(a)** the metaworker-dispatch **dispatcher's own** `claude -p` session survives long
  enough to read and execute SKILL.md Step 4-pre ("run this FIRST, before 4a" --
  `.claude/skills/metaworker-dispatch/SKILL.md:772`), or
- **(b)** that (living) dispatcher session, executing Step 4c, launches a **child** worker
  and later classifies that child's death via `check_deferral_exit.py` /
  `check_worker_launch.py`.

Every one of the five fixes improved (a)/(b)'s *fidelity* -- built it (1), made the stamp
automatic instead of advisory *within* (b) (2), fixed its text-parsing correctness (3), fixed
its `clear` semantics (4), closed the one remaining copy-and-skip gap in the Step 4c
*child-launch* probe (4b). Each is genuinely correct for the surface it touches -- none of
them is a bad fix.

**None of the five touches the actual launcher: `/usr/local/bin/ree_metaworker_dispatch.sh`**,
the systemd-timer-invoked bash wrapper that launches the **dispatcher's own** `claude -p`
session in the first place (verified: `grep -n "dispatch_usage_cooldown" /usr/local/bin/ree_metaworker_dispatch.sh`
and the canonical repo copy `ree-v3/coordinator/deploy/ree-metaworker-dispatch.sh` both return
zero hits). That wrapper:

1. Launches `claude -p "Run exactly ONE cycle of the metaworker-dispatch skill..."`
   **unconditionally**, every 5 minutes, with **no pre-flight check** against
   `metaworker_dispatch_cooldown.json` -- unlike its own PAUSED/THROTTLED branches (coordination-plane
   pause, memory/session-count guard), which *do* short-circuit before spending an invocation.
2. Already **detects** a usage-limit death of that outer session, via `ree_metaworker_heartbeat.py`'s
   `classify_session_output()` -- which anchors the exact same banner text
   (`"You've hit your weekly limit ..."`) that `check_deferral_exit.py` parses for a child, and
   whose own docstring says so explicitly: *"This is the same event seen from the DISPATCHER's
   side, where no transcript path is known and the stdout already exists."* (`scripts/ree_metaworker_heartbeat.py:753`)
3. **Never calls `dispatch_usage_cooldown.autostamp()` from that detection.** The classification
   feeds only the heartbeat's `health="dead-on-arrival"` field. The cooldown file is never
   written from this vantage point, and the wrapper never asks it anything either.

**When the account is genuinely exhausted, it is overwhelmingly the dispatcher's own outer
session -- not a Step 4c child -- that dies**, because the dispatcher's own launch is the
*first* `claude -p` invocation of the cycle and Step 4-pre would be the *very first thing* a
surviving session does. A dead-on-arrival dispatcher never reaches Step 1, let alone Step
4-pre or Step 4c. `ree_metaworker_heartbeat.py`'s own `STALL_THRESHOLD_CYCLES` comment
supplies the scale: replaying all 3128 committed cycles of `ree-cloud-5.json`
(2026-08-02 -> 2026-08-19) found **1578 of 2706 completed cycles carried the usage-limit
banner in the dispatcher's own stdout** (1430 of those exiting 0 -- the banner, not the exit
code, is the signal). Against that, `metaworker_dispatch_cooldown.json`'s entire git history
holds exactly **two** real writes: one manual `clear` (correcting the 2026-08-18 misparse
incident) and one genuine `autostamp()` (2026-08-18T23:22:48Z, a **session**-limit observed
from a **child** worker's death). The in-session mechanism the five fixes hardened has almost
never had the chance to fire, because the majority-share failure mode kills the very session
that would have run it.

## 3. Why this reading is right and the "shared vs. per-account" hypothesis is not

The dispatching session that raised the 5th recurrence flagged a plausible alternative:
`metaworker_dispatch_cooldown.json` is git-tracked/shared while the fleet has moved to
per-account Keychain tokens (`scripts/claude_account.py`), so a single shared cooldown file
might be wrong by construction if different boxes are on different accounts.

**Checked directly and refuted as the primary driver.** `claude_account.py status`, run live
during the 2026-08-18T23:52Z handover build (`WORKSPACE_STATE.md` same timestamp), resolved
**both** `ree-cloud-4` and `ree-cloud-5` to the same account (`nooarche@pm.me`) -- the
deliberate outcome of a "three-machine handover," not an accident of independent per-box
tokens. The design's steady state *is* one shared account across the fleet, so a single
shared cooldown file is the right shape, not a mismatch.

**What actually explains "Mac healthy at 08:10Z while ree-cloud-5 was blocked":**
`chip-20260819-account-handover-misses-systemd-token-sites` (open, found by a later dispatch
cycle same day). The 2026-08-18 handover wrote the new token to
`/etc/systemd/system/ree-metaworker.service.d/auth.conf` -> `/etc/ree/claude_auth.env`, but
`ree-cloud-5` *also* carried an older `override.conf` -> `/etc/ree-metaworker-token.env`
drop-in (mtime 2026-08-16), and systemd drop-ins load alphabetically with the **last one
winning** -- `override.conf` silently beat `auth.conf`. Result: `ree-cloud-5`'s resident
dispatcher authenticated as the **old, already-exhausted** account (weekly limit, resets
2026-08-21T18:00Z) for ~12.5 hours (2026-08-19T04:07:36Z onward, ~150 no-op cycles) while the
Mac and `ree-cloud-4` -- correctly on the new account -- were fine. That is a real,
already-largely-fixed, one-time credential-routing defect (old token archived, `override.conf`
removed, `ree-cloud-4` independently verified already-correct) with its own open procedural
follow-on (enumerate every systemd `EnvironmentFile` site in the handover skill, verify the
service-resolved fingerprint rather than the file written). **It is a distinct finding and
should not be conflated with this one** -- it explains *which* account ree-cloud-5 was
reading, not *why the cooldown gate never engaged regardless of which account it was*. Even
with the credential correctly routed, the wrapper still has no pre-flight check and the
heartbeat still never stamps: the same 150 cycles would have been wasted (though at least
gated after cycle 1, once the fix in Section 4 exists) against a *correctly-routed* but
*genuinely* exhausted account too.

The "Aug 21 18:00 UTC" figure that made the accounts look confusingly entangled came from a
**third, unrelated** source: a 2026-08-19T07:12Z account-handover-hygiene session probing old
leaked tokens found in `~/.zsh_history` (unrelated security scrub, not a live dispatch
observation) -- one of those leaked tokens happened to be the *same* stale credential
`override.conf` was pinning ree-cloud-5 to, so the two investigations converged on the same
number from different directions. Coincidence of timing, not evidence of a structural
per-account design flaw.

## 4. The concrete gap, and the (not-yet-authorized) durable fix

**Gap.** `/usr/local/bin/ree_metaworker_dispatch.sh` (and its canonical copy
`ree-v3/coordinator/deploy/ree-metaworker-dispatch.sh`) launches the dispatcher's own
`claude -p` session with no pre-flight consultation of `dispatch_usage_cooldown.py`, and its
paired `ree_metaworker_heartbeat.py` detects a dispatcher-level usage-limit death (already
computes the right `outcome="usage-limit"` and extracts the banner line) but never arms the
gate from that detection.

**Proposed fix, in outline (not built by this session):**

1. **Wrapper pre-check**, alongside the existing PAUSED / THROTTLED early-exit branches (the
   wrapper already has this shape -- `STATE="paused"` / `STATE="throttled"` -- so this is one
   more branch of the same kind, not a new pattern): before the `claude -p` launch line, call
   `dispatch_usage_cooldown.py check` (or its Python `check()` entry point directly, matching
   how `coordination_plane.is_coordination_plane_paused()` is already imported inline). Exit
   3 (WITHHELD) -> skip the launch, emit the heartbeat as `state="withheld"` (mirroring
   `"paused"`/`"throttled"`), log the withheld line, done for this cycle.
2. **Wrapper/heartbeat-side stamp**: when `classify_session_output()` returns
   `outcome == "usage-limit"`, call `dispatch_usage_cooldown.autostamp()` with the same banner
   line and an observed-at instant (the wrapper already has a reliable instant available: `ts()`
   at the moment the dead session was observed) -- the exact mirror of what
   `check_deferral_exit.py` already does for a child worker, just invoked from the wrapper's
   vantage point instead of a session's.

Both reuse `dispatch_usage_cooldown.py`'s existing `check()`/`autostamp()` functions
unchanged -- no new fail-open properties to prove, no new self-clearing logic to design. The
module's PROBE_GAP/MAX_COOLDOWN_H clamp, its refuse-on-uncertainty rules, and its
never-permanently-block guarantee all carry over intact; the wrapper would just be a second,
earlier call site, exactly as `check_deferral_exit.py` is a call site today.

**Not decided here, and deliberately left for the decision chip:** the exact call shape
(shell-out to the existing CLI vs. a small inline python `-c`, matching the wrapper's existing
`coordination_plane` import style), whether to add a `source="wrapper dispatcher-own-session
USAGE-LIMIT"` tag to `dispatch_usage_cooldown.autostamp()`'s `source` field so a future reader
can tell the two call sites apart, and whether `ree-cloud-4`'s dual-role branch (which can skip
the claude launch entirely when the runner owns the box) needs the same check ahead of its own
`elif` chain.

## 5. Held-out check (CLAUDE.md "General Rules")

Three real historical cases, none used to derive the fix above, where the OLD design (no
wrapper-level check or stamp) and the proposed NEW design give **different** outcomes:

**(i) The 2026-08-02 -> 2026-08-19 dispatcher-death corpus itself (1578 of 2706 completed
cycles carrying the banner).** OLD: every one of those cycles is an unconditional, uncounted
`claude -p` invocation with zero memory across cycles -- structurally the same "no memory"
defect chip #1 fixed for child workers, just never fixed for the dispatcher's own launch.
NEW: the first dispatcher-death in an outage stamps the gate (from the wrapper, using the
banner text `classify_session_output()` already extracts); every subsequent cycle within
`PROBE_GAP`/`MAX_COOLDOWN_H` short-circuits before spending an invocation. Old and new differ
sharply and non-degenerately -- this is the corpus the original chip #1 measured for the
child-worker path (57 chips / ~200 cycles) but never for this one, which is >7x larger.

**(ii) `chip-20260819-account-handover-misses-systemd-token-sites`'s ~150-cycle incident
(2026-08-19T04:07:36Z onward).** OLD: `metaworker_dispatch_cooldown.json`'s git history shows
zero writes during this window -- confirmed by inspection, the file's newest commit is still
23:22:48Z the *prior* day. NEW: cycle 1's dispatcher death (banner: "You've hit your weekly
limit - resets Aug 21, 6pm (UTC)") would stamp on the wrapper's first observation, withholding
cycles 2 through ~148 rather than repeating the identical failure every 5 minutes for 12.5
hours. This case is additionally useful because it shows the fix helps even when the
*underlying* exhaustion is itself a misconfiguration (Section 3) -- the gate doesn't need to
know *why* the account is exhausted to stop re-attempting into it.

**(iii) The 2026-08-17T17:01:05Z cycle 2617 entry (`WORKSPACE_STATE.md`).** The dispatcher's
own session was alive that cycle (not a dispatcher-level death) but chose, by manually tailing
several worktrees' `claude.log` files "verified the account-wide weekly API usage limit is
still in effect," to skip Step 4c entirely -- the exact "improvised check" shape
`chip-20260818-doa-classify-unconditional-at-launcher`'s own held-out cases already document
at the *child*-classification level, here recurring one level up as a dispatcher reasoning
about *aggregate* prior deaths rather than consulting a gate. OLD: a full model invocation is
spent doing this by-eye triage each such cycle, with nothing persisted for the next cycle to
reuse. NEW: had cycle N's dispatcher (or child) death been stamped per (i)/(ii) above, cycle
2617 would have hit the wrapper's pre-check WITHHELD *before spending any invocation at all*,
which is strictly cheaper and removes the by-eye judgment call entirely.

**Negative control (degenerate, correctly excluded):** an ordinary healthy cycle with no
usage-limit anywhere in view -- old and new agree (launch normally, no gate consulted, nothing
to stamp). Not counted toward the three.

**Honest counterweight, stated per CLAUDE.md rather than skipped:** this design doc's own
held-out check is unusually one-sided -- all three cases are large, clean wins for the
proposed direction, and I did not find a case where the wrapper-level check would give the
*wrong* answer. That absence is itself worth flagging rather than treated as proof of
robustness: the check surveyed only cases already visible in `WORKSPACE_STATE.md`/`TASK_CHIPS.json`
resolution notes (the corpus this skill's Step 2 directs research to), not, for instance, a
case where a **false** usage-limit banner match in the dispatcher's own stdout (e.g. a
dispatched child's summary text discussing a usage limit in prose, printed to the dispatcher's
own stdout before it exits normally) could cause a *wrong* stamp from the wrapper side. The
existing `_USAGE_BANNER_RE` regex is anchored (start-of-line, tail-scoped to the last 4000
chars) specifically to reduce this, and `autostamp()`'s own refuse-on-uncertainty rules would
catch most failure shapes, but this specific interaction (wrapper-observed banner immediately
followed by real work in the same stdout tail) was not stress-tested here and should be in any
implementation's test suite.

## 6. Disposition

No code changed by this session. Per the routing decision, this design is handed to a
`kind: decision` chip (`chip-20260819-cooldown-wrapper-gate-decision`, raised alongside this
doc) asking whether to build Section 4 as outlined. The credential-routing procedural fix
(`chip-20260819-account-handover-misses-systemd-token-sites`) remains open, separate, and is
**not** superseded or duplicated by this diagnosis -- it should proceed independently.
