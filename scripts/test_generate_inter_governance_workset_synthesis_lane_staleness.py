#!/usr/bin/env python3
"""Regression test for FM3b -- the SECOND /implement-substrate emission path in
generate_inter_governance_workset.py
(chip-20260815-igw-workset-implemented-pending-validation-stale).

FM3 (2026-08-03, REE_assembly 2e08fcdf1e) fixed "already-built substrate is
offered as buildable" by adding `_substrate_implementation_complete` -- but it
placed the guard inside `_substrate_ready_items()`, a LOADER. That protects
only the loop which calls that loader (the "Substrate ready: <sd>" loop). The
retest-blocker SYNTHESIS loop ("Implement substrate: <sid> (unblocks <cid>)")
builds its items straight from `_retest_blockers`' structured blockers, so the
guard never reached it and the identical failure kept shipping by the second
route for twelve days.

Live at the time of the fix (verified by running build_workset() against the
real corpus, 2026-08-15):

    IGW-20260815-228  status=ready  skill=/implement-substrate
    "Implement substrate: MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION
     (unblocks ARC-045)"
    substrate_queue entry: status=implemented_pending_validation, ready=true

plus five further entries (SD-049, MECH-307, ARC-062,
f_dominance_conversion_ceiling, v4_loop_segregation) rendered as `blocked`
"Implement substrate" items for substrate that was likewise already built.
The `ready` one is the harmful case: igw_routine_tick.pick_candidate skips any
item whose status is not `ready`, so only that one could be staged as a
worktree, sit "awaiting human launch" because /implement-substrate is in
REQUIRES_HUMAN_SKILLS, and be GC-reaped unused.

WHY AN ALREADY-BUILT ENTRY REACHES THE SYNTHESIS LOOP AT ALL -- the mechanism
is counter-intuitive and is what made this survive FM3. `_substrate_ready_items()`
now EXCLUDES build-complete entries. Excluding it from loop 1 means loop 1 never
adds it to `emitted_substrate_sd_ids`, so the entry falls through to loop 2 with
nothing suppressing it. FM3's fix is therefore what HANDED the entry to the
unguarded path. `SuppressedEntryIsNotSilentlyPromotedTest` pins that shape
directly.

NOT the defect -- both were checked on 2026-08-15 and are pinned here so a later
session does not re-investigate them:

  (a) A "ready-flag bypass". The chip that raised this suspected the synthesis
      loop ignored the entry's own `ready` flag, because a workset item read
      `ready` while substrate_queue said `ready: false`. It does not:
      `_implement_substrate_blockers` returns a `ready=false (...)` blocker,
      which forces `sub_status="blocked"`. Pinned by
      `ReadyFlagIsRespectedTransitivelyTest`. The apparent contradiction was an
      artifact of comparing a workset generated at 2026-08-14T01:40Z against a
      substrate_queue read ~23h later; at generation time that entry was
      `pending_implementation, ready: true` and the generator was correct.

  (b) `implemented_commit_ree_v3` as a structural key in place of the status
      allowlist. Populated on 1 of 157 entries (already classified complete by
      status), so it adds zero coverage -- and it asserts "a commit landed", not
      "the build is complete", which is exactly the distinction
      `_status_implementation_complete`'s `partial` guard exists to preserve.
      Pinned by `ImplementedCommitFieldIsNotSufficientTest`.

THE TEST THAT MATTERS HERE IS THE PATH-INDEPENDENT ONE.
`NoBuildLandedSubstrateIsOfferedAnywhereTest` asserts the invariant over EVERY
/implement-substrate item build_workset() emits, without naming a loop. A test
written against the status value alone, or against one loop, would have passed
for the whole twelve days FM3b was live -- the FM3 suite did exactly that.
`EmissionSiteCountTest` is the companion: it fails when a FOURTH emission site
is added, which is the moment to apply the guard again.

Time-independent: no clock, no network, no git. Temp files only. The live-corpus
tests read the repo's own substrate_queue.json read-only and carry explicit
non-vacuity assertions, so they report "stopped exercising the bug" rather than
passing empty.

Run: /opt/local/bin/python3 scripts/test_generate_inter_governance_workset_synthesis_lane_staleness.py
"""

import importlib.util
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
GENERATOR_PATH = SCRIPTS_DIR / "generate_inter_governance_workset.py"


def _load_generator():
    spec = importlib.util.spec_from_file_location(
        "ree_igw_generator_synthesis_lane_test", GENERATOR_PATH
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


GEN = _load_generator()

# A claim id that really is in the retest set, so the synthesis loop runs on it
# without having to fake claims.yaml. ARC-045 is the claim the live incident
# item (MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION) named.
RETEST_CLAIM = "ARC-045"

IMPLEMENT_SKILL = "/implement-substrate"


def _sd_id_of(item: dict) -> str | None:
    """Recover the substrate sd_id an /implement-substrate item refers to.

    Deliberately parses the TITLE rather than reading a field, because the
    title is the only thing the three emission sites have in common -- and
    parsing all three title shapes is what makes this test path-independent.
    """
    title = item.get("title") or ""
    for prefix in ("Substrate ready: ", "Substrate (blocked): "):
        if title.startswith(prefix):
            return title[len(prefix):]
    if title.startswith("Implement substrate: "):
        return title[len("Implement substrate: "):].split(" (unblocks")[0]
    return None


class _FixtureQueue(unittest.TestCase):
    """Base: run build_workset() against a substrate_queue we fully control.

    Only SUBSTRATE_QUEUE and _claim_retest_ids are patched. Everything else --
    claims.yaml, the governance recommendations, the ree-v3 queue -- is read
    live, so the loop under test runs in its real surroundings rather than
    against a mock of itself.
    """

    QUEUE: list[dict] = []

    def setUp(self):
        self._orig_path = GEN.SUBSTRATE_QUEUE
        self._orig_retest = GEN._claim_retest_ids
        fh = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
        fh.close()
        self._path = Path(fh.name)
        self._path.write_text(
            json.dumps({"queue": self.QUEUE}, indent=2), encoding="utf-8"
        )
        GEN.SUBSTRATE_QUEUE = self._path
        GEN._claim_retest_ids = lambda: {RETEST_CLAIM}
        self.items = GEN.build_workset()["items"]

    def tearDown(self):
        GEN.SUBSTRATE_QUEUE = self._orig_path
        GEN._claim_retest_ids = self._orig_retest
        self._path.unlink(missing_ok=True)

    def implement_items(self) -> dict[str, dict]:
        out = {}
        for it in self.items:
            if it.get("skill") != IMPLEMENT_SKILL:
                continue
            sd = _sd_id_of(it)
            if sd:
                out[sd] = it
        return out


class SynthesisLoopBuildLandedTest(_FixtureQueue):
    """The FM3b board: build-complete prerequisites must not be offered.

    Every entry here has `ready: true` and no unresolved dependencies, which is
    what makes them reach the synthesis loop as `ready` rather than `blocked`.
    The two chip fixtures are carried verbatim, plus the live incident entry.
    """

    QUEUE = [
        # --- the live incident (IGW-20260815-228) -------------------------
        {
            "sd_id": "MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION",
            "status": "implemented_pending_validation",
            "ready": True,
            "unblocks_claims": [RETEST_CLAIM],
        },
        # --- the two entries named by the chip ----------------------------
        {
            "sd_id": "mech357-freeze-incompatible-pressure-mechanism",
            "status": "implemented_pending_validation",
            "implementation_status": "implemented_pending_validation",
            "ready": True,
            "unblocks_claims": [RETEST_CLAIM],
        },
        {
            "sd_id": "SD-MECH303-THRESHOLD-SOURCING",
            "status": "implemented_pending_validation",
            "ready": False,
            "unblocks_claims": [RETEST_CLAIM],
        },
        # --- negative controls: real build work, must SURVIVE -------------
        {
            "sd_id": "SD-GENUINELY-UNBUILT",
            "status": "pending_implementation",
            "ready": False,
            "unblocks_claims": [RETEST_CLAIM],
        },
        {
            "sd_id": "SD-PARTIAL",
            "status": "partially_implemented_pending_consumer_wiring",
            "ready": False,
            "unblocks_claims": [RETEST_CLAIM],
        },
    ]

    def test_the_live_incident_item_is_no_longer_emitted(self):
        """IGW-20260815-228, the one that could actually be staged.

        This is the assertion that fails against the pre-FM3b generator.
        """
        self.assertNotIn(
            "MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION",
            self.implement_items(),
            "the confirmed FM3b incident item is being offered as buildable again",
        )

    def test_neither_chip_fixture_is_offered_as_buildable(self):
        for sd in (
            "mech357-freeze-incompatible-pressure-mechanism",
            "SD-MECH303-THRESHOLD-SOURCING",
        ):
            with self.subTest(sd_id=sd):
                self.assertNotIn(sd, self.implement_items())

    def test_implementation_status_field_is_honoured_not_just_status(self):
        """mech357 carries the marker on BOTH fields; SD-MECH303 on `status`
        only and `implementation_status` absent. Both must be suppressed, so a
        fix that reads only one field does not pass."""
        entries = {e["sd_id"]: e for e in self.QUEUE}
        self.assertIsNone(
            entries["SD-MECH303-THRESHOLD-SOURCING"].get("implementation_status"),
            "precondition: this fixture must exercise the status-only field",
        )
        self.assertNotIn("SD-MECH303-THRESHOLD-SOURCING", self.implement_items())

    def test_genuinely_unbuilt_substrate_still_surfaces(self):
        """The lane's whole purpose. If this goes empty the guard has
        over-suppressed, which is a strictly worse failure than the one being
        fixed -- real build work would vanish silently."""
        emitted = self.implement_items()
        self.assertIn("SD-GENUINELY-UNBUILT", emitted)
        self.assertIn(
            "SD-PARTIAL",
            emitted,
            "partially_implemented_pending_consumer_wiring names remaining BUILD "
            "work -- it must stay implementable",
        )


class SuppressedEntryIsNotSilentlyPromotedTest(_FixtureQueue):
    """The exact shape that made FM3b invisible to the FM3 suite.

    A build-complete entry with `ready: true` and no dependencies is EXCLUDED
    from `_substrate_ready_items()` by FM3 -- which means loop 1 never registers
    it in `emitted_substrate_sd_ids`, and it lands in loop 2 completely
    unguarded. Pre-FM3b it came back out as `ready`. So FM3's own fix is what
    routed the entry into the hole.
    """

    QUEUE = [
        {
            "sd_id": "SD-COMPLETE-READY-NO-DEPS",
            "status": "implemented_pending_validation",
            "ready": True,
            "unblocks_claims": [RETEST_CLAIM],
        },
    ]

    def test_loop_one_excludes_it(self):
        """Precondition, not the assertion: FM3 is doing its job."""
        self.assertEqual(
            [e.get("sd_id") for e in GEN._substrate_ready_items()],
            [],
            "precondition: FM3 should already keep this out of loop 1",
        )

    def test_and_loop_two_does_not_pick_it_up(self):
        self.assertNotIn("SD-COMPLETE-READY-NO-DEPS", self.implement_items())

    def test_it_is_not_emitted_as_ready_under_any_title(self):
        """Belt and braces: catch a future variant that renames the title but
        keeps offering the work."""
        offending = [
            it for it in self.items
            if it.get("skill") == IMPLEMENT_SKILL and it.get("status") == "ready"
        ]
        self.assertEqual(
            offending, [],
            "a build-complete entry is being offered as ready build work",
        )


class DependsOnUnresolvedCarveOutIsPreservedTest(_FixtureQueue):
    """FM3 deliberately lets an entry with unresolved prerequisites STAY in the
    lane rendering `blocked`, rather than vanish. FM3b reuses the same predicate
    precisely so that carve-out is not quietly dropped on the second path."""

    QUEUE = [
        {
            "sd_id": "SD-COMPLETE-BUT-BLOCKED",
            "status": "implemented",
            "ready": True,
            "depends_on_unresolved": ["SD-GENUINELY-UNBUILT still to build"],
            "unblocks_claims": [RETEST_CLAIM],
        },
        {
            "sd_id": "SD-GENUINELY-UNBUILT",
            "status": "pending_implementation",
            "ready": False,
            "unblocks_claims": [RETEST_CLAIM],
        },
    ]

    def test_entry_with_unresolved_deps_is_still_shown_as_blocked(self):
        item = self.implement_items().get("SD-COMPLETE-BUT-BLOCKED")
        self.assertIsNotNone(
            item,
            "the depends_on_unresolved carve-out was dropped -- an entry with "
            "unresolved prerequisites must render 'blocked', not vanish",
        )
        self.assertEqual(item.get("status"), "blocked")


class ReadyFlagIsRespectedTransitivelyTest(_FixtureQueue):
    """Refutes hypothesis (a) from the chip: the synthesis loop does consult the
    entry's own `ready` flag, via `_implement_substrate_blockers`."""

    QUEUE = [
        {
            "sd_id": "SD-NOT-READY",
            "status": "pending_implementation",
            "ready": False,
            "ready_blocked_by": "design question open",
            "unblocks_claims": [RETEST_CLAIM],
        },
    ]

    def test_ready_false_renders_blocked_not_ready(self):
        item = self.implement_items().get("SD-NOT-READY")
        self.assertIsNotNone(item, "precondition: the entry should be emitted")
        self.assertEqual(
            item.get("status"), "blocked",
            "substrate_queue says ready=false; the item must not render ready",
        )
        self.assertTrue(
            any("ready" in b for b in (item.get("blocked_by") or [])),
            "the ready=false reason should be surfaced in blocked_by",
        )


class ImplementedCommitFieldIsNotSufficientTest(unittest.TestCase):
    """Refutes hypothesis (b): `implemented_commit_ree_v3` must NOT be treated
    as proof the build is complete. A commit having landed is not the same as
    the build being finished -- which is the distinction the `partial` guard in
    `_status_implementation_complete` exists to preserve."""

    def test_a_commit_sha_does_not_override_remaining_build_work(self):
        entry = {
            "sd_id": "SD-PARTIAL-WITH-COMMIT",
            "status": "partially_implemented_pending_consumer_wiring",
            "implemented_commit_ree_v3": "deadbeef1234",
            "ready": True,
        }
        self.assertFalse(
            GEN._substrate_implementation_complete(entry),
            "a recorded commit sha must not promote partially-built substrate "
            "to 'build complete'",
        )


class NoBuildLandedSubstrateIsOfferedAnywhereTest(unittest.TestCase):
    """THE path-independent invariant, over the LIVE corpus.

    Names no loop and no status string: for every /implement-substrate item the
    generator emits, the substrate_queue entry it points at must not be
    build-complete. This is the assertion that would have caught FM3b on the day
    FM3 shipped, and the one that will catch a fourth emission site.
    """

    @classmethod
    def setUpClass(cls):
        cls.items = GEN.build_workset()["items"]
        cls.by_id = GEN._substrate_by_id()

    def test_no_implement_item_points_at_build_complete_substrate(self):
        offenders = []
        for it in self.items:
            if it.get("skill") != IMPLEMENT_SKILL:
                continue
            sd = _sd_id_of(it)
            entry = self.by_id.get(sd) if sd else None
            if entry and GEN._substrate_implementation_complete(entry):
                offenders.append(
                    "%s [%s] %s (substrate_queue status=%r)"
                    % (it.get("id"), it.get("status"), it.get("title"),
                       entry.get("implementation_status") or entry.get("status"))
                )
        self.assertEqual(
            offenders, [],
            "already-built substrate is being offered as /implement-substrate "
            "work:\n  " + "\n  ".join(offenders),
        )

    def test_the_invariant_is_actually_exercised(self):
        """Non-vacuity. If the live corpus stops containing a build-complete
        entry that some retest names as a blocker, the test above goes green for
        the wrong reason -- so say so instead of passing quietly."""
        complete = [
            e for e in self.by_id.values()
            if GEN._substrate_implementation_complete(e)
        ]
        self.assertTrue(
            complete,
            "no build-complete substrate_queue entries remain -- the invariant "
            "above is now vacuous; re-point this test at a fixture corpus",
        )


class EmissionSiteCountTest(unittest.TestCase):
    """FM3 and FM3b are one defect found twice: a guard put in a LOADER protects
    only the loop that calls it. There are three `skill="/implement-substrate"`
    emission sites. When a fourth is added, this fails -- which is the moment to
    decide whether it needs the build-landed guard too."""

    KNOWN_SITES = 3

    def test_emission_site_count_is_unchanged(self):
        src = GENERATOR_PATH.read_text(encoding="utf-8")
        # Anchored to a full indented keyword-argument line so the module
        # docstring -- which quotes this same string while describing the three
        # sites -- is not itself counted as a fourth one.
        found = len(
            re.findall(
                r'^[ \t]+skill="/implement-substrate",$', src, flags=re.MULTILINE
            )
        )
        self.assertEqual(
            found, self.KNOWN_SITES,
            "the number of /implement-substrate emission sites changed "
            "(%d -> %d). A new site does NOT inherit the FM3/FM3b build-landed "
            "guard -- `_substrate_implementation_complete` lives in a loader and "
            "in the synthesis loop, not in `add()`. Apply it, then update "
            "KNOWN_SITES." % (self.KNOWN_SITES, found),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
