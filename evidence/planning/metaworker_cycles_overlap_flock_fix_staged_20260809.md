# Metaworker dispatch reentrancy fix (ree-cloud-5) — staged install

**Status: AWAITING USER / INTERACTIVE-SESSION ACTION — one privileged install remains.**
Chip: `chip-20260809-metaworker-cycles-overlap`. Landed 2026-08-09 by headless session
`metaworker-chip-20260809-metaworker-cycles-overlap`.

The fix (design, tracked reference copies, and empirical validation) is complete and pushed.
The only remaining step is copying two already-validated files into system paths on the live
box and reloading systemd — three `sudo` commands. **A headless `claude -p` session cannot do
this: the auto-mode classifier blocks privileged writes to `/usr/local/bin` and
`/etc/systemd/system` over ssh** (home-directory `sudo` is allowed; system-path `sudo` is not),
and there is no interactive user in a headless run to authorize it. The commands below are
copy-pasteable for a human or an interactive session.

Until they are run, **the live box is NOT fixed** and cycle overlap can still occur.

---

## The bug (confirmed, do not re-derive)

`ree-metaworker.service` is `Type=oneshot` + `KillMode=process` + `TimeoutStartSec=280`. The
dispatch script runs `claude -p` in the foreground. A cycle running longer than 280s (4m40s)
has its **bash wrapper** SIGTERMed by systemd at the start timeout, but under
`KillMode=process` only the unit's main pid is signalled — the `claude -p` **child survives
orphaned**. The timer then starts a fresh instance 5 min later, so the surviving orphan of
cycle N overlaps cycle N+1. Each overlapping dispatcher independently computes the skill's
Step 4a `available_slots = 2 - in_flight`, so N dispatchers can each launch up to 2 workers on
a 2-core box. Confirmed live 2026-08-09T11:32Z: three dispatcher sessions
(cycles 1830/1831/1832) alive at once. `KillMode=process` itself is correct and deliberate
(its inline comment: the default `control-group` would SIGTERM live dispatched workers) — it is
**not** changed by this fix.

## The fix (two changes)

1. **`ree_metaworker_dispatch.sh`** — wrap the `claude -p` launch in
   `flock -n -E 99 "$LOCKFILE" timeout --signal=TERM --kill-after=60 "$DISPATCH_MAX_SEC" claude -p ...`
   where `LOCKFILE=$HOME/.ree_metaworker/dispatch.lock` and
   `DISPATCH_MAX_SEC=${REE_DISPATCH_MAX_SEC:-1500}`.
   - `flock -n` → a second cycle refuses to dispatch, returning **99** (distinct
     `--conflict-exit-code`), which the script logs as `LOCKED OUT` (state `locked-out`).
   - **The lock is held by the `flock` PROCESS, not by the script.** This is the load-bearing
     detail the chip flagged: a script-held lock (`exec 200>lock; flock 200`) releases the
     instant systemd SIGTERMs the wrapper at `TimeoutStartSec`, while the claude child lives
     on — re-opening the exact overlap window. `flock` as a child of the wrapper survives that
     SIGTERM (same reason the claude child does, under `KillMode=process`) and holds the lock
     for claude's whole lifetime.
   - `timeout` bounds a hung/orphaned claude (SIGTERM at `DISPATCH_MAX_SEC`, SIGKILL 60s
     later, rc **124**) so a wedged cycle releases the lock instead of pinning the box forever
     — necessary because `TimeoutStartSec`'s SIGTERM never reaches claude under
     `KillMode=process`.

2. **`ree-metaworker.service`** — `TimeoutStartSec=280 → 1800`. Real dispatch cycles
   legitimately run ~12 min when they do coordination-data repair, so 280s was below the
   normal ceiling. 1800s keeps a normal long cycle inside the service lifetime, so the unit
   stays active for its whole run and **systemd's own one-instance-per-oneshot-unit guarantee**
   prevents overlap directly (a timer trigger on an already-active oneshot unit is coalesced,
   not run as a second instance). The `flock`+`timeout` is the duration-independent backstop
   and the hard bound (1800s > 1500s claude cap + 60s kill-after + wrapper overhead). The
   timer (`OnUnitActiveSec=5min`) is unchanged.

Both changes are already committed to the tracked reference copies:
**ree-v3 `main` commit `5bb112223d`** — `coordinator/deploy/ree-metaworker-dispatch.sh` and
`coordinator/deploy/ree-metaworker.service`.

## Empirical validation (run on ree-cloud-5, 2026-08-09)

- **Lock survives parent SIGTERM (the critical property):** a wrapper running
  `flock -n -E 99 LOCK timeout ... sleep`, then SIGTERM to *only* the wrapper main pid
  (mimicking `KillMode=process`): the wrapper died, but `flock`/`timeout`/`sleep` all survived
  and a second `flock -n LOCK true` reported the lock **still held** (PROBE2 PASS). After the
  `timeout` window the lock was **free** (PROBE3 PASS) — a hung dispatcher self-releases.
- **Guard construct returns the expected codes:** two concurrent
  `flock -n -E 99 LOCK timeout ... sleep` invocations → the second returned **99** (locked
  out) and did not run its payload; the `timeout` path returned **124**; the lock released
  cleanly. Both rc branches the script handles are thus confirmed produced by the exact
  construct.
- `bash -n` clean on the modified script (locally and on the box).

## What was already done ON THE BOX

- Live files backed up to `/home/ree/.ree_metaworker/backups/`:
  `ree_metaworker_dispatch.sh.20260809T120049Z`, `ree-metaworker.service.20260809T120049Z`
  (use these for rollback).
- The two new files were scp'd to `/tmp/` on the box:
  `/tmp/ree-metaworker-dispatch.sh`, `/tmp/ree-metaworker.service`
  (these may be cleared on reboot; the authoritative source is the ree-v3 commit above).

## REMAINING STEP — run on ree-cloud-5 (ssh ree@46.224.127.182), as a human or interactive session

If the staged `/tmp` files are still present (verify with `sha256sum /tmp/ree-metaworker-dispatch.sh`
== `5c27a4a341a71a1fd748a1b26cb5ee12a7980619e180ad3eee983c630218d6d3`):

```bash
sudo install -o root -g root -m 755 /tmp/ree-metaworker-dispatch.sh /usr/local/bin/ree_metaworker_dispatch.sh
sudo install -o root -g root -m 644 /tmp/ree-metaworker.service      /etc/systemd/system/ree-metaworker.service
sudo systemctl daemon-reload
```

If `/tmp` was cleared, refresh from the tracked copies first (the box does NOT autosync ree-v3):

```bash
# from the Mac (REE_Working):
scp ree-v3/coordinator/deploy/ree-metaworker-dispatch.sh ree-v3/coordinator/deploy/ree-metaworker.service ree@46.224.127.182:/tmp/
# then the three install commands above.
```

**Verify after install (do NOT disturb any running cycle — install is safe while a cycle runs;
the new files take effect on the next timer tick):**

```bash
systemctl cat ree-metaworker.service | grep -E 'TimeoutStartSec|KillMode'   # expect 1800 + process
grep -n 'flock -n -E 99' /usr/local/bin/ree_metaworker_dispatch.sh          # expect the guard line
sha256sum /usr/local/bin/ree_metaworker_dispatch.sh                          # expect 5c27a4a3...
# after the next few 5-min ticks:
tail -30 ~/ree_metaworker_dispatch.log        # 'LOCKED OUT' lines are the guard working, not an error
pgrep -af 'cycle .* on machine ree-cloud-5' | wc -l   # should stay 1 even across a long cycle
```

## Rollback (if the fix misbehaves)

```bash
sudo cp /home/ree/.ree_metaworker/backups/ree_metaworker_dispatch.sh.20260809T120049Z /usr/local/bin/ree_metaworker_dispatch.sh
sudo cp /home/ree/.ree_metaworker/backups/ree-metaworker.service.20260809T120049Z     /etc/systemd/system/ree-metaworker.service
sudo systemctl daemon-reload
```

## Relationship to the sibling chip

`chip-20260809-cloud5-umbrella-stale-claim-gate` is the **ledger-sync** half (the
`chip_ledger.py` claim gate computing against a stale local ledger, and `ree_commit`'s
retry-push giving up on a JSON conflict). This chip is the **process-count** half. They are
disjoint fixes: this one touches only the host-local systemd unit + dispatch wrapper and no
`scripts/` code; the sibling touches `scripts/chip_ledger.py` / `ree_commit.py` /
`audit_coordination_plane_dirt.py`. Both reduce double-dispatch pressure from different
directions; neither subsumes the other.
