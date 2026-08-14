#!/usr/bin/env python3
"""Tests for scripts/check_plan_frontmatter.py.

Time-independent (no clock read anywhere) and filesystem-isolated (every plan doc
is written to a tempdir and passed to check_file() by path, so nothing reads the
live evidence/planning/ tree).

The two positive regressions replay the two confirmed incidents, which are
DIFFERENT SHAPES and were previously handled by the same (wrong) code path:

  * 2026-06-19 commitment_closure_plan.md -- an UNQUOTED prose scalar containing
    ': '. Attribution and the double-quote suggestion were already correct here,
    and the tests pin that they stay correct.
  * 2026-08-13 arc_005_control_plane_routing_plan.md (e5927f8acb) -- an
    already-quoted scalar that was never CLOSED. The lint fired but named the
    key one line too far down and suggested double-quoting a value that was
    already quoted.

The negative controls carry as much weight as the positives, because the naive
detector for the second shape (odd count of unescaped '"' on a line) fires on a
LEGITIMATE multi-line double-quoted scalar too -- the real incident blob
contained two of each. A checker that "fixes" attribution by reporting valid
YAML as broken is worse than the off-by-one it replaces.

Run:
    /opt/local/bin/python3 scripts/test_check_plan_frontmatter.py
"""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import check_plan_frontmatter as mod  # noqa: E402


def plan_doc(node_lines: str) -> str:
    """A minimal but structurally faithful closure-plan doc.

    Frontmatter line numbering is deliberately explicit: line 1 is the opening
    '---', so a node key on frontmatter line N is on DOC line N+1, which is what
    the finding reports and what an operator's editor shows.
    """
    return (
        "---\n"
        "closure_plan:\n"
        "  id: demo_plan\n"
        "  nodes:\n"
        "    - id: GAP-A\n"
        + node_lines
        + "---\n"
        "\n"
        "# Demo plan\n"
    )


class Harness(unittest.TestCase):
    def check(self, text: str):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "demo_plan.md"
            path.write_text(text, encoding="utf-8")
            return mod.check_file(path)


class TestUnterminatedDoubleQuote(Harness):
    """The 2026-08-13 incident shape."""

    # Frontmatter lines: 1 closure_plan, 2 id, 3 nodes, 4 '- id: GAP-A',
    # 5 status, 6 outcome (BROKEN -- no closing quote), 7 queued.
    # Doc lines are +1 for the leading '---'.
    BROKEN = plan_doc(
        '      status: done\n'
        '      outcome_2026_08_13: "landed PASS/supports and was applied\n'
        '      queued_2026_07_31: "authored + queued via /queue-experiment."\n'
    )

    def test_it_is_detected_at_all(self):
        f = self.check(self.BROKEN)
        self.assertIsNotNone(f)
        self.assertEqual(f["kind"], "parse_error")
        self.assertEqual(f["shape"], "unterminated_double_quote")

    def test_names_the_key_that_is_actually_broken(self):
        """Regression: the walk-back named the FOLLOWING key.

        yaml's problem_mark lands on the line after the unterminated scalar, so
        offending_key() returned 'queued_2026_07_31'. The broken key is the one
        whose quote was never closed.
        """
        f = self.check(self.BROKEN)
        self.assertEqual(f["key"], "outcome_2026_08_13")
        self.assertNotEqual(f["key"], "queued_2026_07_31")

    def test_points_at_the_line_holding_the_missing_quote(self):
        # outcome_2026_08_13 is frontmatter line 6 -> doc line 7. The parser
        # trips one line later, on doc line 8.
        f = self.check(self.BROKEN)
        self.assertEqual(f["unterminated_doc_line"], 7)
        self.assertEqual(f["doc_line"], 8)

    def test_does_not_suggest_re_quoting_an_already_quoted_value(self):
        """Regression: suggest_fix() bailed to None here, so the operator got the
        generic 'double-quote the offending scalar value' -- wrong advice, since
        the value IS quoted and merely unclosed."""
        f = self.check(self.BROKEN)
        self.assertIsNone(f["suggestion"])

    def test_report_text_tells_the_operator_what_to_do(self):
        from io import StringIO
        from contextlib import redirect_stdout
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "demo_plan.md"
            path.write_text(self.BROKEN, encoding="utf-8")
            argv = sys.argv
            sys.argv = ["check_plan_frontmatter.py", "--file", str(path)]
            buf = StringIO()
            try:
                with redirect_stdout(buf):
                    rc = mod.main()
            finally:
                sys.argv = argv
        out = buf.getvalue()
        self.assertEqual(rc, 0, "warn-only must still exit 0")
        self.assertIn("outcome_2026_08_13", out)
        self.assertIn("missing closing double-quote", out)
        self.assertIn("END of line 7", out)
        self.assertNotIn("suggested fix (double-quote the value)", out)

    def test_strict_exits_1(self):
        argv = sys.argv
        from io import StringIO
        from contextlib import redirect_stdout
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "demo_plan.md"
            path.write_text(self.BROKEN, encoding="utf-8")
            sys.argv = ["check_plan_frontmatter.py", "--file", str(path), "--strict"]
            try:
                with redirect_stdout(StringIO()):
                    rc = mod.main()
            finally:
                sys.argv = argv
        self.assertEqual(rc, 1)


class TestUnquotedProseScalar(Harness):
    """The 2026-06-19 incident shape -- must keep working unchanged."""

    BROKEN = plan_doc(
        '      status: in-progress\n'
        '      owner_exq: V3-EXQ-485 the vacuity fix worked: OFC bias is real\n'
    )

    def test_detected_and_classified_as_the_other_shape(self):
        f = self.check(self.BROKEN)
        self.assertIsNotNone(f)
        self.assertEqual(f["shape"], "unquoted_scalar")

    def test_names_the_key_and_suggests_double_quoting(self):
        f = self.check(self.BROKEN)
        self.assertEqual(f["key"], "owner_exq")
        self.assertIsNotNone(f["suggestion"])
        self.assertIn('owner_exq: "', f["suggestion"])


class TestNegativeControls(Harness):
    def test_clean_plan_reports_nothing(self):
        self.assertIsNone(self.check(plan_doc(
            '      status: done\n'
            '      owner_exq: "V3-EXQ-846"\n'
            '      unblocks_claims: [ARC-005]\n'
        )))

    def test_legitimate_multiline_double_quoted_scalar_is_not_flagged(self):
        """The decisive negative control.

        This value spans three lines and has an ODD number of unescaped '"' on
        its opening line -- textually identical to the broken shape. It is valid
        YAML, and the incident blob contained two of these alongside the two
        real breaks, so a quote-counting detector would have reported 4 findings
        where there were 2.
        """
        self.assertIsNone(self.check(plan_doc(
            '      status: done\n'
            '      remedy_2026_08_03: "848a landed and was confirmed by the\n'
            '        autopsy artifact; the node closes here with no further\n'
            '        work outstanding."\n'
        )))

    def test_a_doc_with_no_frontmatter_is_skipped(self):
        self.assertIsNone(self.check("# Just a heading\n\nprose\n"))

    def test_frontmatter_without_closure_plan_is_skipped(self):
        self.assertIsNone(self.check("---\ntitle: something\n---\n\n# doc\n"))

    def test_closure_plan_not_a_mapping_is_reported(self):
        f = self.check("---\nclosure_plan: just a string\n---\n\n# doc\n")
        self.assertIsNotNone(f)
        self.assertEqual(f["kind"], "not_a_dict")


class TestUnterminatedHelperDirectly(unittest.TestCase):
    """unittest of the attribution helper, independent of check_file()."""

    def test_returns_none_when_there_is_no_such_scalar(self):
        fm = 'closure_plan:\n  id: demo\n  bad: value: with colon\n'
        self.assertIsNone(mod.unterminated_double_quote(fm, 3))

    def test_returns_key_and_1_based_frontmatter_line(self):
        fm = ('closure_plan:\n'
              '  a: "unterminated\n'
              '  b: "fine"\n')
        got = mod.unterminated_double_quote(fm, 3)
        self.assertEqual(got, ("a", 2))


class TestJsonMode(unittest.TestCase):
    def test_json_mode_emits_findings(self):
        import json
        from io import StringIO
        from contextlib import redirect_stdout
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "demo_plan.md"
            path.write_text(TestUnterminatedDoubleQuote.BROKEN, encoding="utf-8")
            argv = sys.argv
            sys.argv = ["check_plan_frontmatter.py", "--file", str(path), "--json"]
            buf = StringIO()
            try:
                with redirect_stdout(buf):
                    rc = mod.main()
            finally:
                sys.argv = argv
        self.assertEqual(rc, 0)
        data = json.loads(buf.getvalue())
        self.assertTrue(data["available"])
        self.assertEqual(len(data["findings"]), 1)
        self.assertEqual(data["findings"][0]["key"], "outcome_2026_08_13")
        self.assertEqual(data["findings"][0]["file"], "demo_plan.md")

    def test_json_mode_is_clean_on_a_good_file(self):
        import json
        from io import StringIO
        from contextlib import redirect_stdout
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "demo_plan.md"
            path.write_text(plan_doc('      status: done\n'), encoding="utf-8")
            argv = sys.argv
            sys.argv = ["check_plan_frontmatter.py", "--file", str(path), "--json"]
            buf = StringIO()
            try:
                with redirect_stdout(buf):
                    rc = mod.main()
            finally:
                sys.argv = argv
        self.assertEqual(rc, 0)
        self.assertEqual(json.loads(buf.getvalue())["findings"], [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
