"""Machine identity that is BLIND to macOS LocalHostName numeric-suffix drift.

WHY THIS EXISTS
---------------
macOS appends a numeric suffix to `LocalHostName` whenever the name it wants is
already claimed on the local network -- a stale Bonjour registration, or an
interface rejoining (this fleet runs a WireGuard mesh, so it happens). Through
Jul-Aug 2026 the Mac had no `HostName` set, so `socket.gethostname()` fell
through to that auto-suffixed name and DRIFTED: `DLAPTOP-4.local` ->
`DLAPTOP-5.local`.

STATE OF THE PIN, because the tense matters: `HostName` was explicitly set to
`DLAPTOP-4.local` by a human on 2026-08-15T07:17:02Z (the mtime of
`/Library/Preferences/SystemConfiguration/preferences.plist`; `scutil --set`
needs root, so it was neither the runner nor a session). So the drift is not live
as this is written. It cannot have been set earlier -- the 2026-07-25 .. 08-09
`DLAPTOP-5.local` manifests could not otherwise exist.

That pin is the fix at source and this module does not duplicate it. This module
exists because the pin is (a) retrospective -- it does nothing for the manifests
already written under the drifted name, and (b) revocable -- it is one unset,
OS update, or migration away from the identity splitting again, silently, exactly
as it did for three weeks. `LocalHostName` is STILL `DLAPTOP-5` today, so the
underlying collision has not gone away; only the name `gethostname()` reports has
been nailed down on top of it.

That is reasonable OS behaviour and this module does not try to prevent it. The
problem is that REE keys real coordination state on the STRING: heartbeat and
status FILENAMES (`runner_heartbeats/<machine>.json`), `machine_affinity` in the
queue, `claimed_by.machine`, and the `machine` field of every result manifest.
So when the suffix moved, the laptop's identity silently SPLIT IN TWO.

Measured on 2026-08-15, in `REE_assembly/evidence/experiments/`:

    99 manifests   "machine": "DLAPTOP-4.local"
    38 manifests   "machine": "DLAPTOP-5.local"
    468 manifests  "completed_by": "DLAPTOP-4.local"

-- one physical laptop, two identities, and the 38 attributed to a machine that
appears in no fleet table, no heartbeat file and no doc. The earliest affected
manifest is dated 2026-07-25, so this ran undetected for three weeks.

The coordinator DB proves the "one physical laptop" half far more strongly than
those counts do, and localises the split exactly (queried on the hub 2026-08-15
by session musing-napier-6f0817, DLAPTOP-4.local vs DLAPTOP-5.local):

    claim_log.machine               10533  vs  0
    commands.machine                  140  vs  0
    experiments.machine_affinity        9  vs  0
    experiments.claimed_by_machine      2  vs  0
    heartbeats.machine                  1  vs  0
    results.machine                    37  vs  12

A genuinely separate machine cannot claim 0 of 10533. So `DLAPTOP-5.local` was
never a second box, and the split is confined to `results.machine` -- the one
path that recorded the RAW reported hostname instead of the resolved identity.

That asymmetry has a cause worth knowing: the live heartbeat carried
`"machine": "DLAPTOP-4.local"` beside `"hostname": "DLAPTOP-5.local"`, meaning
the runner was being started with an explicit `--machine` override BY HAND as a
standing workaround. Undocumented, and one missed invocation from re-splitting
the identity. This module makes that automatic, which is the actual before/after.

It also SILENTLY DISARMED A FEATURE, which is the sharper cost. `experiment_runner`
auto-armed `--laptop-yield-to-cloud` by comparing RAW `socket.gethostname()`
against `LAPTOP_AUTO_YIELD_HOSTNAME`. Once the box began reporting
`DLAPTOP-5.local` that comparison was permanently False, so the laptop stopped
deferring to idle cloud workers -- contradicting the standing "prefer cloud over
the laptop" preference -- with no warning, no error, and no log line, because the
only observable is a banner that simply never prints. Note that site read
`socket.gethostname()` directly rather than the resolved identity, so passing
`--machine DLAPTOP-4.local` did NOT re-arm it; the fix had to be at the call
site, not only here.

WHY THIS IS AN ALLOWLIST AND NOT A REGEX -- DO NOT "SIMPLIFY" IT
----------------------------------------------------------------
The obvious implementation is "strip any trailing `-<digits>`". That is WRONG
here, and it would be a fleet-wide outage rather than a cosmetic bug:
`ree-cloud-1` .. `ree-cloud-5` and `ree-worker-1` .. `ree-worker-4` are DISTINCT
MACHINES whose trailing digit IS the entire identity. Collapsing them would give
the whole cloud fleet ONE shared heartbeat file, make every claim collide with
every other, and route every experiment's affinity to the wrong box.

So: only a base listed in `SUFFIX_BLIND_BASES` is collapsed, and every other name
is returned unchanged. Roughly half the tests in
`tests/contracts/test_machine_identity.py` are negative controls asserting that
the cloud fleet is NOT collapsed -- they exist to stop a later session widening
this predicate into that outage.

WHY THE CANONICAL VALUE IS `DLAPTOP`
------------------------------------
`DLAPTOP` is what the machine actually calls itself: it is `scutil --get
ComputerName`, the stable human-facing name, and the only one of the three macOS
names that has never drifted. `DLAPTOP-4.local` and `DLAPTOP-5.local` are both
LocalHostName accidents -- the `-4` has no more claim to being the real name than
the `-5` does, it is simply the accident that happened to be in force when most
of the evidence was written.

The cost of NOT choosing the historical string is one-off and bounded, because
the alias runs in the useful direction: `DLAPTOP-4.local` and `DLAPTOP-5.local`
both canonicalise FORWARD to `DLAPTOP`, so all 567 existing evidence rows and any
queue entry pinned to either name keep resolving to this machine. Nothing has to
be rewritten for them to keep matching.

The one genuine residue is telemetry FILENAMES. `runner_heartbeats/` and
`runner_status/` are keyed by the identity string, so the next runner start
writes `DLAPTOP.json` and leaves the old `DLAPTOP-4.local.json` behind as a box
that never reports again. (Historical: those files were materialised by the
Phase-3 heartbeat writer from the coordinator DB until 2026-09-01; the directories
left REE_assembly master on 2026-09-06, so the residue now lives only in the
coordinator `heartbeats` table, where a stale row under the old name simply ages
out.) Noted here rather than papered over.

Deliberately NOT done here: rewriting the 137 manifests that carry a `machine`
field. A result manifest is a record of what happened, and editing it to claim a
run occurred under a name the box was not reporting at the time is falsifying
provenance. They are aliased on READ, never rewritten.

RELATED PRIOR ART IN THIS FILE'S NEIGHBOURHOOD
-----------------------------------------------
`runner_remote_control._PHASE3_HUB_HOSTNAMES` already accepts BOTH `ree-cloud-1`
and `ree-worker-1` for the hub, for exactly this reason (the hub VM's
`socket.gethostname()` disagrees with its documented fleet name). This module is
the general form of that same accommodation.
"""

from __future__ import annotations

# Bases whose trailing `-<digits>` is macOS suffix drift rather than identity.
# ONE ENTRY PER PHYSICAL MACHINE THAT ACTUALLY DRIFTS. Adding a base here asserts
# "every numbered variant of this name is the same computer" -- which is true for
# a laptop being re-suffixed by Bonjour, and catastrophically false for a fleet of
# numbered VMs. Read the module docstring before adding one.
SUFFIX_BLIND_BASES: dict[str, str] = {
    # base (lowercased, no suffix, no .local) -> canonical identity to emit.
    # The canonical value is `scutil --get ComputerName`, i.e. what the machine
    # calls itself, NOT whichever LocalHostName suffix was in force when the
    # evidence happened to be written.
    "dlaptop": "DLAPTOP",
}

# Exact-string aliases that are not suffix drift -- one machine genuinely known by
# two unrelated names. Kept separate from the suffix rule so the two cannot be
# confused when either is edited.
EXACT_ALIASES: dict[str, str] = {}


def _split_suffix(name: str) -> tuple[str, str | None]:
    """Split `DLAPTOP-5` into `("dlaptop", "5")`; `ree-cloud-2` into the same
    shape. Returns the lowercased base and the trailing digit-run, or None when
    the name has no trailing `-<digits>` at all.

    This deliberately makes NO judgement about whether the suffix is meaningful.
    That judgement belongs to SUFFIX_BLIND_BASES and nowhere else.
    """
    base, sep, tail = name.rpartition("-")
    if sep and tail.isdigit() and base:
        return base.lower(), tail
    return name.lower(), None


def canonical_machine_name(raw: str | None) -> str:
    """Return the stable identity for a reported hostname.

    Blind to macOS numeric-suffix drift for the bases in SUFFIX_BLIND_BASES, and
    an exact passthrough for everything else -- notably the whole numbered cloud
    fleet. Trailing `.local` is tolerated on input. An empty or None input is
    returned as the empty string rather than raising, because every caller here
    sits on a telemetry path where a hard failure is worse than a blank.
    """
    if not raw:
        return ""
    name = raw.strip()
    if not name:
        return ""

    stem = name[: -len(".local")] if name.lower().endswith(".local") else name

    exact = EXACT_ALIASES.get(stem.lower())
    if exact:
        return exact

    base, suffix = _split_suffix(stem)
    if base in SUFFIX_BLIND_BASES:
        return SUFFIX_BLIND_BASES[base]
    # A bare, unsuffixed base still canonicalises (`DLAPTOP` -> `DLAPTOP-4.local`),
    # which is what makes ComputerName and LocalHostName agree.
    if suffix is None and stem.lower() in SUFFIX_BLIND_BASES:
        return SUFFIX_BLIND_BASES[stem.lower()]

    return name


def same_machine(a: str | None, b: str | None) -> bool:
    """True when two reported names denote the same physical machine.

    Use this instead of `==` anywhere a hostname decides behaviour. Two empty
    names are NOT the same machine -- an unknown identity must never satisfy a
    host-gated branch by accident.
    """
    ca, cb = canonical_machine_name(a), canonical_machine_name(b)
    return bool(ca) and ca == cb
