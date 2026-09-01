"""`validate_claims.validate_terminal_dependencies` -- a LIVE claim must not
silently carry a depends_on edge to a claim the registry has since retired.

WHAT THIS PINS
--------------
Nothing in the pipeline noticed this class. `build_experiment_indexes.py` reads
`depends_on` for the MRF graph and for gating without ever checking the target
claim's own status, so an edge to a superseded claim keeps asserting a live
dependency indefinitely. Measured 2026-09-01 (GFLAG-0064): SD-003 went
`superseded` on 2026-04-18 with successors [MECH-256, SD-029], and SIXTEEN
claims still depended on it four months later. The flag that surfaced it named
three of the sixteen -- nobody was counting, because nothing was checking.

THE TWO EXCLUSIONS ARE THE DESIGN, and they are what this file mostly asserts.
On the 2026-09-01 corpus, 32 edges pointed at a terminal-status target but only
26 were defects. Without the exclusions the check would fire on 6 of 32 (19%)
pieces of perfectly correct work, and a lint that fires on correct work gets
switched off -- which is the failure mode, not a cosmetic one:

  (a) TERMINAL SOURCE. A legacy/retired claim depending on another legacy or
      retired claim is frozen history, correctly preserved. The real corpus has
      an IMPL-020 -> IMPL-021 -> IMPL-022 -> IMPL-024 chain, every link legacy.
      Only a still-live claim can hold a *stale* edge.
  (b) SUCCESSOR PROVENANCE. A claim named in its target's own `superseded_by`,
      depending on the claim it superseded, is recording provenance. Real case:
      MECH-448 -> MECH-447, where MECH-447.superseded_by names MECH-448.

WHY SYNTHETIC FIXTURES, NOT THE LIVE REGISTRY. The check currently reports 26
real violations. A test asserting that number against claims.yaml would pass
today and FAIL the moment somebody actually fixes the backlog this check exists
to surface -- punishing the repair. Every case below is therefore built in
memory; the shapes are drawn from the real corpus but the test does not depend
on the registry's current state.

WARN-ONLY IS ALSO PINNED. `governance.sh` runs `validate_claims --strict`, and
there are 26 live violations, so emitting ERROR here would wedge the governance
pipeline for everyone on a backlog this check is meant to report rather than
gate. Elevation to ERROR is a separate, deliberate decision once the count
reaches 0 (the stabilise-then-elevate posture epistemic_category and
assembly_state both shipped under).
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))

from validate_claims import validate_terminal_dependencies  # noqa: E402


def _issues(claims):
    return validate_terminal_dependencies(claims)


def _messages(claims):
    return [msg for _lvl, msg in _issues(claims)]


class TestTerminalDependencyLint(unittest.TestCase):

    # ---------- the defect it exists to catch ----------

    def test_live_claim_depending_on_superseded_target_warns(self):
        claims = [
            {"id": "SD-003", "status": "superseded", "superseded_by": ["MECH-256", "SD-029"]},
            {"id": "MECH-341", "status": "provisional", "depends_on": ["SD-003"]},
        ]
        msgs = _messages(claims)
        self.assertEqual(len(msgs), 1, msgs)
        self.assertIn("MECH-341", msgs[0])
        self.assertIn("SD-003", msgs[0])
        self.assertIn("superseded", msgs[0])

    def test_message_names_the_successors_so_the_fix_is_actionable(self):
        claims = [
            {"id": "SD-003", "status": "superseded", "superseded_by": ["MECH-256", "SD-029"]},
            {"id": "INV-076", "status": "candidate", "depends_on": ["SD-003"]},
        ]
        msg = _messages(claims)[0]
        self.assertIn("MECH-256", msg)
        self.assertIn("SD-029", msg)

    def test_message_warns_against_a_blind_repoint(self):
        """The message must not imply repointing is always right -- it offers DROP too."""
        claims = [
            {"id": "SD-003", "status": "superseded", "superseded_by": ["MECH-256", "SD-029"]},
            {"id": "SD-013", "status": "provisional", "depends_on": ["SD-003"]},
        ]
        msg = _messages(claims)[0]
        self.assertIn("DROP", msg)

    def test_message_does_NOT_offer_a_cycle_as_the_reason(self):
        """CORRECTED 2026-09-01, same day it shipped. The first version of this hint told
        the reader to check whether the successor already depends on the claim, "which
        would make a repoint a cycle" -- treating a cycle as disqualifying.

        That is wrong here and would have sent readers chasing a non-issue. Measured on
        the live registry the same day: the claims graph ALREADY CONTAINS 153 CYCLES over
        3915 depends_on edges, including a DIRECT 2-hop one (ARC-007 <-> ARC-018), and the
        indexer's loopy belief propagation converges over it. It is a conceptual dependency
        web, not a build DAG.

        So the hint must steer to the SEMANTIC question (is the successor actually what
        this claim depends on?) and must not present cyclicity as the blocker."""
        claims = [
            {"id": "SD-003", "status": "superseded", "superseded_by": ["MECH-256", "SD-029"]},
            {"id": "SD-013", "status": "provisional", "depends_on": ["SD-003"]},
        ]
        msg = _messages(claims)[0]
        self.assertIn("SEMANTICALLY", msg)
        self.assertIn("does NOT disqualify", msg)
        self.assertNotIn("would make a repoint a cycle", msg)

    def test_target_without_superseded_by_gets_the_other_hint(self):
        claims = [
            {"id": "Q-008", "status": "legacy"},
            {"id": "IMPL-017", "status": "active", "depends_on": ["Q-008"]},
        ]
        msg = _messages(claims)[0]
        self.assertIn("no superseded_by recorded", msg)

    def test_retired_and_legacy_and_rejected_all_count_as_terminal(self):
        for status in ("superseded", "retired", "legacy", "rejected"):
            with self.subTest(status=status):
                claims = [
                    {"id": "T-1", "status": status},
                    {"id": "L-1", "status": "candidate", "depends_on": ["T-1"]},
                ]
                self.assertEqual(len(_messages(claims)), 1, status)

    def test_status_matching_is_case_and_whitespace_insensitive(self):
        claims = [
            {"id": "T-1", "status": "  Superseded  "},
            {"id": "L-1", "status": "candidate", "depends_on": ["T-1"]},
        ]
        self.assertEqual(len(_messages(claims)), 1)

    # ---------- exclusion (a): frozen history ----------

    def test_terminal_source_to_terminal_target_is_silent(self):
        """The real IMPL legacy chain. Both ends retired: nothing is stale."""
        claims = [
            {"id": "IMPL-020", "status": "legacy"},
            {"id": "IMPL-021", "status": "legacy", "depends_on": ["IMPL-020"]},
            {"id": "IMPL-022", "status": "legacy", "depends_on": ["IMPL-021"]},
            {"id": "IMPL-024", "status": "legacy", "depends_on": ["IMPL-020", "IMPL-022"]},
        ]
        self.assertEqual(_messages(claims), [])

    def test_terminal_source_is_excluded_for_every_terminal_status(self):
        for status in ("superseded", "retired", "legacy", "rejected"):
            with self.subTest(status=status):
                claims = [
                    {"id": "T-1", "status": "retired"},
                    {"id": "S-1", "status": status, "depends_on": ["T-1"]},
                ]
                self.assertEqual(_messages(claims), [], status)

    # ---------- exclusion (b): successor provenance ----------

    def test_successor_depending_on_what_it_superseded_is_silent(self):
        """MECH-448 -> MECH-447, where MECH-447.superseded_by names MECH-448.
        That is provenance, not a stale edge."""
        claims = [
            {"id": "MECH-447", "status": "superseded", "superseded_by": ["MECH-448", "MECH-449"]},
            {"id": "MECH-448", "status": "candidate", "depends_on": ["MECH-447"]},
        ]
        self.assertEqual(_messages(claims), [])

    def test_successor_exclusion_handles_a_bare_string_superseded_by(self):
        """MECH-058.superseded_by is a plain string, not a list -- the real corpus
        carries both shapes."""
        claims = [
            {"id": "MECH-058", "status": "retired", "superseded_by": "MECH-069"},
            {"id": "MECH-069", "status": "active", "depends_on": ["MECH-058"]},
        ]
        self.assertEqual(_messages(claims), [])

    def test_a_NON_successor_still_warns_on_the_same_target(self):
        """Negative control for exclusion (b): the exclusion must be scoped to the
        successor itself, not to every dependant of a claim that has successors."""
        claims = [
            {"id": "MECH-447", "status": "superseded", "superseded_by": ["MECH-448"]},
            {"id": "MECH-448", "status": "candidate", "depends_on": ["MECH-447"]},
            {"id": "OTHER-1", "status": "candidate", "depends_on": ["MECH-447"]},
        ]
        msgs = _messages(claims)
        self.assertEqual(len(msgs), 1, msgs)
        self.assertIn("OTHER-1", msgs[0])

    # ---------- negative controls ----------

    def test_live_to_live_is_silent(self):
        claims = [
            {"id": "A-1", "status": "active"},
            {"id": "B-1", "status": "candidate", "depends_on": ["A-1"]},
        ]
        self.assertEqual(_messages(claims), [])

    def test_dangling_target_is_not_this_check_s_business(self):
        """A depends_on naming an id that is not in the registry is a different and
        worse defect. It measured 0 in the corpus, so there is nothing to validate a
        check against -- deliberately out of scope rather than shipped unverified."""
        claims = [{"id": "B-1", "status": "candidate", "depends_on": ["NOPE-999"]}]
        self.assertEqual(_messages(claims), [])

    def test_missing_or_malformed_depends_on_does_not_crash(self):
        claims = [
            {"id": "T-1", "status": "retired"},
            {"id": "NO-DEPS", "status": "candidate"},
            {"id": "NULL-DEPS", "status": "candidate", "depends_on": None},
            {"id": "STR-DEPS", "status": "candidate", "depends_on": "T-1"},
        ]
        self.assertEqual(_messages(claims), [])

    def test_claim_with_no_status_is_treated_as_live_and_still_checked(self):
        claims = [
            {"id": "T-1", "status": "superseded"},
            {"id": "NOSTATUS", "depends_on": ["T-1"]},
        ]
        self.assertEqual(len(_messages(claims)), 1)

    # ---------- level ----------

    def test_every_issue_is_WARN_never_ERROR(self):
        """governance.sh runs validate_claims --strict and there are 26 live
        violations; an ERROR here would wedge the pipeline on the very backlog this
        check exists to report."""
        claims = [
            {"id": "SD-003", "status": "superseded", "superseded_by": ["MECH-256"]},
            {"id": "X-1", "status": "candidate", "depends_on": ["SD-003"]},
            {"id": "X-2", "status": "stable", "depends_on": ["SD-003"]},
        ]
        levels = {lvl for lvl, _msg in _issues(claims)}
        self.assertEqual(levels, {"WARN"})

    def test_one_issue_per_offending_edge_not_per_claim(self):
        claims = [
            {"id": "T-1", "status": "retired"},
            {"id": "T-2", "status": "legacy"},
            {"id": "SRC", "status": "candidate", "depends_on": ["T-1", "T-2"]},
        ]
        self.assertEqual(len(_messages(claims)), 2)


if __name__ == "__main__":
    unittest.main()
