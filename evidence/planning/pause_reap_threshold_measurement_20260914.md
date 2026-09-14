# Pause-lock duration measurement vs PAUSE_REAP_HOURS -- 2026-09-14

chip-20260910-pause-reap-tail-measurement. Measurement + recommendation only --
`PAUSE_REAP_HOURS`, `audit_stale_claims.py`, and every skill are left untouched
by this session, per the chip's explicit scope.

## Question

`coordination_plane.PAUSE_REAP_HOURS = 24.0`. `audit_stale_claims.py` auto-reaps
a `governance-pause:` / `autopsy-pause:` / `metaworker-maint:` lock older than
that (bucket P). The 2026-09-10 concern: a session awaiting the user's answer
could legitimately wait **days**, which would make the threshold a measure of
the user's availability rather than of session health. Nobody had measured how
long real pauses actually last -- this document does.

## Method (re-runnable)

`TASK_CLAIMS.json` is coordinator-materialized with ~24h `done`-retention, so
the **live** file structurally cannot retain a long-closed pause. The
measurement therefore walks git history rather than the current file:

1. `git log -S<prefix> --format="%H %P" -- TASK_CLAIMS.json` for each of the
   three `PAUSE_LABEL_PREFIXES` (`governance-pause:`, `autopsy-pause:`,
   `metaworker-maint:`) -- pickaxe on the literal label prefix finds every
   commit where an occurrence of that string was ADDED (a pause claim newly
   opened) or REMOVED (a claim pruned out of the file once past its
   retention window). 208 distinct commits matched across the three prefixes.
2. For each matched commit, diff the PARENT's and the commit's own
   `TASK_CLAIMS.json` (both read via `git show <ref>:TASK_CLAIMS.json`),
   restricted to entries whose `session_label` starts with one of the three
   prefixes, keyed on `(session_id, claimed_at)`:
   - a key present in the commit but not the parent = an **OPEN** event,
     `claimed_at` read directly from the entry;
   - a key present in the parent but not the commit = the claim was just
     pruned; its `closed_at` / `status` / `completion_note` are read from the
     **parent's** copy (the last snapshot that still carried it);
   - a key present in BOTH parent and commit whose `status` flipped
     `active` -> `done` (label text unchanged, so pickaxe would not have
     flagged this commit on its own, but it is already in hand from the
     `added`/`removed` scan of a different key in the same commit) is also
     captured this way.
3. The live `HEAD` copy of `TASK_CLAIMS.json` is checked too, for any pause
   still open or freshly closed and not yet pruned.
4. OPEN and CLOSE events are merged by `(session_id, claimed_at)`; duration =
   `closed_at - claimed_at` in hours.

Script: ad-hoc, not committed (a one-off measurement, per the chip's own
scope -- not a standing tool). Re-run by re-deriving the ~60-line pickaxe +
diff walk above; total runtime was under 10 seconds against this repo's
~9,982 `TASK_CLAIMS.json` commits (the pickaxe narrowing is what makes this
cheap -- a naive walk of every commit would be two orders of magnitude
slower for no additional signal).

## Results

- **n = 113** pause locks with both an open and a close event found (0
  unresolved -- every open event this method found also found a matching
  close, which is itself a check that the method is not silently dropping
  transitions).
- **Date span:** `claimed_at` from 2026-08-02T18:36Z to 2026-09-14T21:57Z --
  **43 calendar days**, **33 distinct days** carrying at least one pause
  (i.e. this is not one busy week's data).
- **Median: 0.52h.** **p90: 4.89h.** **Max: 15.16h.**
- **n > 6h: 9. n > 12h: 1. n > 24h: 0. n > 48h: 0.**
- **106 of 113** pauses were claimed before `pending_decisions.py` landed
  (2026-09-10); only **7** since. Too small a post-landing sample to judge
  whether it has already reduced pause frequency or duration -- noted, not
  concluded.

Ten longest (hours, session, claimed -> closed):

| hours | session | claimed | closed |
|---|---|---|---|
| 5.53 | failure-autopsy-multi-20260819-pause | 2026-08-19T21:20:36Z | 2026-08-20T02:52:37Z |
| 7.02 | governance-20260902-0548 | 2026-09-02T05:48:50Z | 2026-09-02T12:50:01Z |
| 8.48 | governance-20260908-0703 | 2026-09-08T07:03:26Z | 2026-09-08T15:31:59Z |
| 8.51 | governance-20260905-autopsies | 2026-09-05T02:37:52Z | 2026-09-05T11:08:34Z |
| 8.74 | v3-exq-812-harness-repair-1f9438 | 2026-08-08T20:41:08Z | 2026-08-09T05:25:17Z |
| 8.75 | queue-depth-low-ops-aac785 | 2026-08-10T06:47:37Z | 2026-08-10T15:32:33Z |
| 8.78 | governance-20260905 | 2026-09-05T02:21:46Z | 2026-09-05T11:08:34Z |
| 8.99 | governance-paused-bb6e76 | 2026-08-18T08:17:26Z | 2026-08-18T17:16:54Z |
| 11.84 | governance-cycle-20260828 | 2026-08-28T06:35:43Z | 2026-08-28T18:26:14Z |
| 15.16 | gov-20260821-0203 | 2026-08-21T02:03:47Z | 2026-08-21T17:13:16Z |

All ten are ordinary interactive governance/autopsy cycles (regen + apply +
verify-on-origin), not blocked-on-user-response waits -- consistent with the
median being well under an hour and the tail being "a long working session",
not "the user went quiet for days".

## Was any pause ever REAPED rather than closed by its owner?

**Exactly one, and it predates the current threshold.**
`v3-exq-812-harness-repair-1f9438` (8.74h, 2026-08-08/09) is the single
confirmed bucket-P auto-reap in this dataset -- already documented inline in
`coordination_plane.py`'s own `PAUSE_REAP_HOURS` comment as the incident that
motivated raising the threshold from 6.0 to 24.0 on 2026-08-09. It was reaped
under the OLD 6h threshold; its own `completion_note` records the correction
after the fact ("the prior note was auto-generated by audit_stale_claims.py
bucket P, which reaped this claim as abandoned ... while the session was
still finishing").

Since that raise, **zero** of the other 112 measured pauses have been
auto-reaped, and none could have been: the maximum observed duration (15.16h)
never reaches the 24h threshold at all. So across the entire post-fix
regime this measurement covers, **the 24h threshold has fired zero times**
-- neither correctly (there has been nothing pathologically long to catch)
nor incorrectly (no repeat of the 2026-08-08/09 premature reap).

## What this measurement can and cannot tell you

**Can tell you:** in 43 days and 113 real pauses, nothing has come close to
24h under the current regime. The threshold is not currently trip-happy, and
the one historical false-positive it exists to prevent has not recurred.

**Cannot tell you:** whether the SCENARIO the chip raised -- the user
genuinely unavailable for multiple days, so a legitimate pause runs long --
has ever happened or will happen. The chip's own point stands and this
measurement does not undermine it: that scenario is **under-sampled by
construction**, because when the user is too busy to answer for three days
they are also too busy to START a governance/autopsy cycle in the first
place, so exactly the periods most likely to produce a genuinely long pause
are the periods least likely to generate a claim to measure. A frequency
count over realized pauses cannot see a tail that, by the mechanism that
would produce it, mostly does not get recorded. This is stated rather than
finessed: the absence of a >24h case in this data is evidence the threshold
has not been WRONG in this window, not evidence the underlying worry is
unfounded.

## Recommendation

**Leave `PAUSE_REAP_HOURS` at 24.0.** Reasoning:

1. The empirical record since the 2026-08-09 raise is clean -- 0 reaps,
   0 near-misses (max 15.16h, 63% of the threshold), across 113 cases and
   43 days. There is no evidence the current value is too tight.
2. Raising it further has a real cost the risk asymmetry in
   `coordination_plane.py`'s own comment already states: an abandoned pause
   held longer only defers cloud dispatch (recoverable, and surfaced by every
   session-startup audit well before any new ceiling), so there is no
   symmetric case for raising it "just in case" without a measured need.
3. `pending_decisions.py` (landed 2026-09-10) gives a governance session an
   alternative to holding a blocking pause at all -- record the decision and
   close cleanly instead. That should make the days-long scenario RARER going
   forward, not more common, which weakens (does not eliminate) the case for
   a pre-emptive raise. The post-landing sample (7 pauses) is too small to
   confirm this yet; worth re-measuring after a larger post-2026-09-10 sample
   accumulates.
4. If the user's specific worry (a multi-day wait) materializes even once,
   that single real case is worth more than any amount of re-analysis of this
   dataset, precisely because of the under-sampling point above -- treat a
   future long pause as the signal to revisit this number, not a further
   measurement of the past.

No held-out check is claimed for this document under CLAUDE.md's
GOV-HELDOUT-1 discipline, because no rule is being changed here -- this is a
measurement artifact with a "leave it" recommendation, not a standing-rule
edit. GOV-HELDOUT-1 applies if and when a future session proposes actually
changing `PAUSE_REAP_HOURS`.
