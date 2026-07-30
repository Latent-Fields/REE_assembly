#!/usr/bin/env python3
"""Tests for scripts/check_plan_status_table_sync.py.

Time-independent (every date is a literal in a fixture) and filesystem-isolated
(every plan doc is written to a tempdir and passed to check_plan() by path, so
nothing reads the live evidence/planning/ tree).

The regression fixtures replay the six confirmed 2026-07-29 instances plus the
live positive control that the checker was required to flag. Two negative
controls matter as much as the positives: a reconciled plan must report CLEAN,
and a plan with in-cell '|' characters must parse rather than mis-compare.

Run:
    /opt/local/bin/python3 scripts/test_check_plan_status_table_sync.py
"""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import check_plan_status_table_sync as mod  # noqa: E402

HDR7 = ("| Gap | Phase | Status | Blocking on | Next action | Owner-EXQ | Last updated |\n"
        "|---|---|---|---|---|---|---|\n")


def plan_doc(nodes: str, table: str, plan_id: str = "demo") -> str:
    """Assemble a minimal but structurally faithful plan doc."""
    return (
        "---\n"
        "closure_plan:\n"
        f"  id: {plan_id}\n"
        '  title: "Demo"\n'
        "  last_updated: 2026-07-29\n"
        "  nodes:\n"
        f"{nodes}"
        "---\n"
        "\n# Demo plan\n\nSome prose.\n\n"
        "| Gap | Subject | Severity |\n|---|---|---|\n"
        "| GAP-1 | a decoy table that must NOT be read as the status table | high |\n"
        "\n## Status table\n\nThe resume primitive.\n\n"
        f"{table}"
        "\nStatus values: `open`, `done`.\n\n---\n\n## Test cohort\n\nmore prose\n"
    )


def node(nid: str, status: str, last_updated: str) -> str:
    return (f'    - id: "{nid}"\n'
            f"      status: {status}\n"
            f"      last_updated: {last_updated}\n")


class Harness(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def run_doc(self, nodes: str, table: str, plan_id: str = "demo") -> dict:
        p = self.tmp / f"{plan_id}_plan.md"
        p.write_text(plan_doc(nodes, table, plan_id), encoding="utf-8")
        return mod.check_plan(p)

    def kinds(self, res: dict) -> set[str]:
        return {f["kind"] for f in res["findings"]}

    def find(self, res: dict, kind: str, node_key: str) -> dict | None:
        for f in res["findings"]:
            if f["kind"] == kind and f["node"] == node_key:
                return f
        return None


class TestCleanPlan(Harness):
    def test_agreeing_plan_is_clean(self):
        """NEGATIVE CONTROL: a reconciled plan must produce zero findings."""
        res = self.run_doc(
            node("demo:GAP-1", "done", "2026-06-15") + node("demo:GAP-2", "blocked", "2026-05-17"),
            HDR7
            + "| GAP-1 | 1 | done | none | act | EXQ-1 | 2026-06-15 |\n"
            + "| GAP-2 | 2 | blocked | up | act | EXQ-2 | 2026-05-17 |\n",
        )
        self.assertEqual(res["findings"], [], f"unexpected findings: {res['findings']}")
        self.assertEqual((res["n_nodes"], res["n_rows"]), (2, 2))

    def test_row_date_newer_than_node_is_not_a_finding(self):
        """The reconcile-marker convention post-dates the node on purpose."""
        res = self.run_doc(
            node("demo:GAP-1", "done", "2026-06-15"),
            HDR7 + "| GAP-1 | 1 | done | none | act | EXQ-1 | "
                   "2026-07-29 (row reconcile; node record 2026-06-15) |\n",
        )
        self.assertEqual(res["findings"], [])

    def test_decoy_table_before_the_heading_is_not_used(self):
        """A Gap-keyed table OUTSIDE the Status-table section must be ignored.

        plan_doc() puts a `| Gap | Subject | Severity |` table above the heading;
        it has no Status column, and picking it up would misreport every row.
        """
        res = self.run_doc(
            node("demo:GAP-1", "done", "2026-06-15"),
            HDR7 + "| GAP-1 | 1 | done | none | act | EXQ-1 | 2026-06-15 |\n",
        )
        self.assertEqual(res["n_rows"], 1)
        self.assertEqual(res["findings"], [])


class TestStatusMismatch(Harness):
    def test_goal_pipeline_gap4_live_positive_control(self):
        """The case the checker was REQUIRED to flag.

        goal_pipeline:GAP-4 -- row in-progress / 2026-05-29 while the node has
        been done / 2026-06-09 since 2026-06-09. Still open after 7e60b8a675.
        """
        res = self.run_doc(
            node("goal_pipeline:GAP-4", "done", "2026-06-09"),
            HDR7 + "| GAP-4 | 4 | in-progress | 2-fork | act | V3-EXQ-490g | 2026-05-29 |\n",
            plan_id="goal_pipeline",
        )
        sm = self.find(res, "status_mismatch", "GAP-4")
        self.assertIsNotNone(sm, "GAP-4 status mismatch not flagged")
        self.assertEqual((sm["row_value"], sm["node_value"]), ("in-progress", "done"))
        ds = self.find(res, "date_stale", "GAP-4")
        self.assertIsNotNone(ds, "GAP-4 stale row date not flagged")
        self.assertEqual((ds["row_value"], ds["node_value"]), ("2026-05-29", "2026-06-09"))

    def test_confirmed_2026_07_29_status_pairs(self):
        """Replay the confirmed instances' status pairs; each must flag."""
        cases = [
            ("GAP-7", "blocked_pending_substrate", "done"),       # goal_pipeline
            ("GAP-8", "in-progress", "assembling"),               # commitment_closure
            ("GAP-D", "in-progress", "done"),                     # arc_062
            ("GAP-I", "partial", "blocked_pending_substrate"),     # arc_062
            ("GAP-J", "open", "blocked"),                          # arc_062
        ]
        for key, row_status, node_status in cases:
            with self.subTest(node=key):
                res = self.run_doc(
                    node(f"demo:{key}", node_status, "2026-06-23"),
                    HDR7 + f"| {key} | 2 | {row_status} | b | a | E | 2026-06-23 |\n",
                )
                self.assertIsNotNone(
                    self.find(res, "status_mismatch", key),
                    f"{key}: row '{row_status}' vs node '{node_status}' not flagged",
                )

    def test_blocked_is_not_accepted_for_blocked_pending_substrate(self):
        """No semantic coarsening -- the repair convention writes the exact status.

        Aliasing these would mask the arc_062:GAP-I class of drift outright.
        """
        res = self.run_doc(
            node("demo:GAP-1", "blocked_pending_substrate", "2026-06-23"),
            HDR7 + "| GAP-1 | 1 | blocked | b | a | E | 2026-06-23 |\n",
        )
        self.assertIn("status_mismatch", self.kinds(res))


class TestStatusNormalisation(Harness):
    def test_normalisation_equivalences(self):
        """Case, '_' vs '-', generation qualifier and trailing prose are noise."""
        for row_status, node_status in [
            ("in_progress", "in-progress"),
            ("in-progress", "in_progress"),
            ("DONE", "done"),
            ("done ", "done"),
            ("deferred V4", "deferred"),
            ("done (lit gate); superseded by X", "done"),
            ("**done**", "done"),
            ("`done`", "done"),
        ]:
            with self.subTest(row=row_status):
                res = self.run_doc(
                    node("demo:GAP-1", node_status, "2026-06-15"),
                    HDR7 + f"| GAP-1 | 1 | {row_status} | b | a | E | 2026-06-15 |\n",
                )
                self.assertEqual(
                    res["findings"], [],
                    f"'{row_status}' should normalise to '{node_status}': {res['findings']}",
                )

    def test_blocked_prefix_is_not_truncated(self):
        """Longest-first vocabulary matching: 'blocked-pending-substrate' must
        not collapse to 'blocked' (which would make the two look equal)."""
        self.assertEqual(mod.norm_status("blocked_pending_substrate"),
                         "blocked-pending-substrate")
        self.assertEqual(mod.norm_status("upstream-blocked"), "upstream-blocked")
        self.assertEqual(mod.norm_status("blocked"), "blocked")


class TestMembership(Harness):
    def test_missing_row_with_mis_keyed_hint(self):
        """arc_062:GAP-I-absorption existed in frontmatter with NO table row.

        The sibling row key is the literal 'GAP-I-', so the hint must pair them.
        """
        res = self.run_doc(
            node("arc_062:GAP-I", "blocked_pending_substrate", "2026-06-23")
            + node("arc_062:GAP-I-absorption", "deferred", "2026-06-23"),
            HDR7
            + "| GAP-I | 2-3 | blocked_pending_substrate | b | a | E | 2026-06-23 |\n"
            + "| GAP-I- | 2-3 | deferred | b | a | E | 2026-06-23 |\n",
            plan_id="arc_062",
        )
        mr = self.find(res, "missing_row", "GAP-I-absorption")
        self.assertIsNotNone(mr, "GAP-I-absorption missing row not flagged")
        self.assertIn("GAP-I-", mr["detail"])
        self.assertIsNotNone(self.find(res, "orphan_row", "GAP-I-"))
        # 'GAP-I-' must NOT be normalised to 'GAP-I' -- that would silently
        # satisfy the real GAP-I row and hide the truncated key.
        self.assertEqual(mod.row_key("GAP-I-"), "GAP-I-")

    def test_hint_prefers_the_longest_prefix(self):
        """'GAP-11b' should hint at 'GAP-11', not the useless 'GAP-1'."""
        self.assertEqual(mod.near_miss("GAP-11b", ["GAP-1", "GAP-11", "GAP-2"]), "GAP-11")

    def test_key_cell_carrying_a_title(self):
        """infant_substrate rows read 'GAP-1 Harm gradient env'."""
        res = self.run_doc(
            node("infant_substrate:GAP-1", "done", "2026-05-16"),
            "| Gap | Status | Owner EXQ | Last updated |\n|---|---|---|---|\n"
            "| GAP-1 Harm gradient env | done | V3-EXQ-1 | 2026-05-16 |\n",
            plan_id="infant_substrate",
        )
        self.assertEqual(res["findings"], [])
        self.assertEqual(res["n_rows"], 1)
        self.assertEqual(mod.row_key("GAP-11 EXQ-ISEF-002"), "GAP-11")

    def test_duplicate_row(self):
        res = self.run_doc(
            node("demo:GAP-1", "done", "2026-06-15"),
            HDR7
            + "| GAP-1 | 1 | done | b | a | E | 2026-06-15 |\n"
            + "| GAP-1 | 1 | done | b | a | E | 2026-06-15 |\n",
        )
        self.assertIn("duplicate_row", self.kinds(res))


class TestInCellPipes(Harness):
    def test_literal_pipes_in_a_prose_cell_do_not_break_the_comparison(self):
        """CONFIRMED PRE-EXISTING: arc_062 GAP-B carries |PE_t-PE_{t-K}| in its
        'Next action' cell (9 cells on a 7-column header) and sleep GAP-2 carries
        two such pairs. The row must still compare CLEAN, and the overflow must
        be reported as a NOTE rather than silently mis-read.
        """
        res = self.run_doc(
            node("arc_062:GAP-B", "in-progress", "2026-05-20"),
            HDR7 + "| GAP-B | 2 | in-progress | retest | the |PE_t-PE_{t-K}| term "
                   "and |x| too | V3-EXQ-543k | 2026-05-20 |\n",
            plan_id="arc_062",
        )
        self.assertEqual(res["findings"], [],
                         f"in-cell pipes broke the comparison: {res['findings']}")
        self.assertTrue(any("literal '|' inside a cell" in n for n in res["notes"]),
                        f"overflow not noted: {res['notes']}")

    def test_overflow_row_still_detects_a_real_mismatch(self):
        """The anchoring must not mask drift on an overflowed row."""
        res = self.run_doc(
            node("demo:GAP-B", "done", "2026-07-09"),
            HDR7 + "| GAP-B | 2 | in-progress | r | the |PE| term | E | 2026-05-20 |\n",
        )
        self.assertIn("status_mismatch", self.kinds(res))
        self.assertIn("date_stale", self.kinds(res))


class TestOutOfScope(Harness):
    def test_plan_with_no_status_table_is_a_note_not_a_finding(self):
        """~42 plans have nodes and no table -- no second representation."""
        p = self.tmp / "no_table_plan.md"
        p.write_text(
            "---\nclosure_plan:\n  id: nt\n  nodes:\n"
            + node("nt:GAP-1", "done", "2026-06-15")
            + "---\n\n# No status table here\n\nprose only\n",
            encoding="utf-8",
        )
        res = mod.check_plan(p)
        self.assertEqual(res["findings"], [])
        self.assertTrue(any("no 'Status table' heading" in n for n in res["notes"]))

    def test_non_node_keyed_status_table_is_skipped(self):
        """behavioral_diversity_isolation keys on Theory, e3_fresh_select on Call
        site, ree_ai_design_critique on WS -- out of scope, never flagged."""
        p = self.tmp / "theory_plan.md"
        p.write_text(
            "---\nclosure_plan:\n  id: th\n  nodes:\n"
            + node("th:GAP-1", "done", "2026-06-15")
            + "---\n\n## Status table\n\n"
              "| Theory | Layer | Claim | Substrate status | Falsifier |\n"
              "|---|---|---|---|---|\n"
              "| T1 | L1 | C1 | landed | F1 |\n",
            encoding="utf-8",
        )
        res = mod.check_plan(p)
        self.assertEqual(res["findings"], [])
        self.assertTrue(any("no node-keyed table" in n for n in res["notes"]))

    def test_decision_log_heading_does_not_hijack_the_search(self):
        """A heading that merely CONTAINS the phrase must not bound the search.

        Live shape in arc_062 / self_attribution:
          '### 2026-07-29 - Status-table reconcile: five rows were reporting ...'
        A 'contains' test matched that heading, and because it sits in the
        decision log it bounded the search to a section with no table at all.
        """
        p = self.tmp / "declog_plan.md"
        p.write_text(
            "---\nclosure_plan:\n  id: dl\n  nodes:\n"
            + node("dl:GAP-1", "done", "2026-06-15")
            + "---\n\n"
              "## Decision log\n\n"
              "### 2026-07-29 - Status-table reconcile: rows reported completed work\n\n"
              "prose, no table here\n\n"
              "## Status table\n\n"
            + HDR7
            + "| GAP-1 | 1 | done | none | act | E | 2026-06-15 |\n",
            encoding="utf-8",
        )
        res = mod.check_plan(p)
        self.assertEqual(res["n_rows"], 1, f"real table not found: {res['notes']}")
        self.assertEqual(res["findings"], [])

    def test_numbered_and_qualified_headings_are_accepted(self):
        """'## 5. Status table' and '## Status table (resume primitive)' are live."""
        for heading in ["## 5. Status table", "## Status table (resume primitive)",
                        "## Status table"]:
            with self.subTest(heading=heading):
                p = self.tmp / "h_plan.md"
                p.write_text(
                    "---\nclosure_plan:\n  id: h\n  nodes:\n"
                    + node("h:GAP-1", "done", "2026-06-15")
                    + f"---\n\n{heading}\n\n" + HDR7
                    + "| GAP-1 | 1 | done | none | act | E | 2026-06-15 |\n",
                    encoding="utf-8",
                )
                res = mod.check_plan(p)
                self.assertEqual(res["n_rows"], 1, f"{heading!r} not recognised")

    def test_non_closure_plan_is_ignored(self):
        p = self.tmp / "plain_plan.md"
        p.write_text("# no frontmatter at all\n\n## Status table\n\n"
                     "| Gap | Status | Last updated |\n|---|---|---|\n"
                     "| GAP-1 | done | 2026-01-01 |\n", encoding="utf-8")
        res = mod.check_plan(p)
        self.assertEqual(res["findings"], [])
        self.assertEqual(res["n_nodes"], 0)

    def test_broken_frontmatter_is_left_to_check_plan_frontmatter(self):
        """An unquoted ': ' scalar is check_plan_frontmatter.py's finding, not
        ours -- we must not double-report it as a sync failure."""
        p = self.tmp / "broken_plan.md"
        p.write_text('---\nclosure_plan:\n  id: b\n  title: bad: value here\n---\n\n'
                     "## Status table\n\n| Gap | Status | Last updated |\n|---|---|---|\n"
                     "| GAP-1 | done | 2026-01-01 |\n", encoding="utf-8")
        res = mod.check_plan(p)
        self.assertEqual(res["findings"], [])


class TestDateParsing(unittest.TestCase):
    def test_reconcile_marker_takes_the_leading_date(self):
        """'2026-07-29 (row reconcile; node record 2026-06-15)' -> 2026-07-29.

        Taking the trailing date instead would report the row as never updated.
        """
        d = mod.parse_date("2026-07-29 (row reconcile; node record 2026-06-15)")
        self.assertEqual((d.year, d.month, d.day), (2026, 7, 29))
        d = mod.parse_date("2026-07-29 (row added; node record 2026-06-23)")
        self.assertEqual(d.isoformat(), "2026-07-29")

    def test_yaml_date_objects_and_strings_both_parse(self):
        import datetime as dt
        self.assertEqual(mod.parse_date(dt.date(2026, 6, 15)).isoformat(), "2026-06-15")
        self.assertEqual(mod.parse_date(dt.datetime(2026, 6, 15, 9, 30)).isoformat(), "2026-06-15")
        self.assertEqual(mod.parse_date("2026-06-15").isoformat(), "2026-06-15")

    def test_unparseable_dates_return_none(self):
        for bad in [None, "", "TBD", "soon", "2026-13-45"]:
            self.assertIsNone(mod.parse_date(bad), f"{bad!r} should not parse")


class TestLivePlanningDir(unittest.TestCase):
    """Guardrails against the live tree. Deliberately does NOT pin a finding
    count -- that changes every time someone reconciles a row, and a test that
    fails on a legitimate fix would just get deleted."""

    def test_live_tree_parses_without_exploding(self):
        if not mod.PLANNING_DIR.exists():
            self.skipTest("evidence/planning not present")
        plans = sorted(mod.PLANNING_DIR.glob("*_plan.md"))
        self.assertGreater(len(plans), 10)
        compared = 0
        for p in plans:
            res = mod.check_plan(p)  # must never raise
            if res["n_rows"]:
                compared += 1
        self.assertGreater(compared, 0, "no plan yielded a node-keyed status table")

    def test_a_reconciled_plan_reports_clean(self):
        """self_attribution_plan.md was reconciled by 7e60b8a675. If this starts
        failing, either the checker regressed or that plan drifted again."""
        p = mod.PLANNING_DIR / "self_attribution_plan.md"
        if not p.exists():
            self.skipTest("self_attribution_plan.md not present")
        res = mod.check_plan(p)
        self.assertEqual(res["findings"], [],
                         f"self_attribution_plan.md is no longer clean: {res['findings']}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
