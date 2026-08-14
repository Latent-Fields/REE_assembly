#!/usr/bin/env python3
"""Tests for audit_literature_duplicate_entries.py.

Time-independent: every corpus is built in a tempdir from literal dicts, no
clock is read, and nothing touches the network (the scan itself never does).

ROUGHLY HALF OF THESE ARE NEGATIVE CONTROLS, and that is the point. The
measured failure of this tool's first cut was the fuzzy-title route grading
seven pairs of DIFFERENT papers by the same author as duplicates, three of them
``double_counted`` on a live claim. So the tests that matter most are the ones
asserting a pair does NOT group:

    test_different_papers_same_author_same_year_do_not_group
    test_craig_style_containment_with_distinct_dois_is_not_a_candidate
    test_short_title_containment_does_not_group
    test_year_gap_suppresses_a_candidate
    test_fuzzy_pair_is_never_graded_double_counted
    test_candidates_alone_do_not_gate

If a later change widens any predicate, those fail before the widening ships.
"""

import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import audit_literature_duplicate_entries as dup  # noqa: E402


def record(entry_id, lit_type, claims, title=None, doi=None, pmid=None,
           authors=None, year=None, venue=None, confidence=0.75,
           direction="supports"):
    return {
        "entry_id": entry_id,
        "literature_type": lit_type,
        "claim_ids_tested": list(claims),
        "confidence": confidence,
        "evidence_direction": direction,
        "source": {
            "title": title,
            "authors": list(authors or []),
            "year": year,
            "venue": venue,
            "doi": doi,
            "pmid": pmid,
        },
    }


class CorpusCase(unittest.TestCase):
    """Builds a literature tree and (optionally) a claim_evidence index."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="dupscan_"))
        self.lit = self.tmp / "literature"
        self.claim_evidence = self.tmp / "claim_evidence.v1.json"
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def write(self, records):
        for rec in records:
            entry = (self.lit / rec["literature_type"] / "entries" / rec["entry_id"])
            entry.mkdir(parents=True, exist_ok=True)
            (entry / "record.json").write_text(json.dumps(rec), encoding="utf-8")

    def write_index(self, pairs):
        """pairs: (literature_type, entry_id, claim_id) reaching the derived index."""
        self.claim_evidence.write_text(json.dumps({"entries": [
            {"source_type": "literature", "experiment_type": t,
             "run_id": e, "claim_id": c}
            for t, e, c in pairs
        ]}), encoding="utf-8")

    def analyse(self, keys=dup.ALL_KEYS):
        records = dup.load_records(self.lit)
        return dup.analyse(records, keys=keys, claim_evidence=self.claim_evidence)

    def groups(self, keys=dup.ALL_KEYS):
        return self.analyse(keys)[0]

    def candidates(self, keys=dup.ALL_KEYS):
        return self.analyse(keys)[1]

    def paths_of(self, finding):
        return sorted(Path(r["path"]).parent.name for r in finding["records"])


# --------------------------------------------------------------------------
# grouping routes -- positive


class TestGroupingRoutes(CorpusCase):

    def test_doi_variants_normalise_into_one_group(self):
        """Case, resolver prefix and the legacy APA double slash all collapse."""
        self.write([
            record("a", "rev_one", ["ARC-001"], title="T A",
                   doi="10.1037/0022-006X.64.2.295"),
            record("b", "rev_two", ["ARC-002"], title="T B",
                   doi="https://doi.org/10.1037//0022-006x.64.2.295"),
        ])
        self.write_index([])
        groups = self.groups()
        self.assertEqual(len(groups), 1)
        self.assertEqual(groups[0]["size"], 2)
        self.assertIn("doi", groups[0]["routes"])

    def test_pmid_route_groups_records_with_no_doi(self):
        self.write([
            record("a", "rev_one", ["ARC-001"], title="T A", pmid="9119582"),
            record("b", "rev_two", ["ARC-002"], title="T B", pmid=9119582),
        ])
        self.write_index([])
        groups = self.groups()
        self.assertEqual(len(groups), 1)
        self.assertIn("pmid", groups[0]["routes"])

    def test_exact_title_groups_a_preprint_and_its_published_version(self):
        """Different DOIs, same title -- the arXiv/journal pair. A real duplicate."""
        self.write([
            record("pre", "rev_one", ["ARC-001"],
                   title="Object-Centric Learning with Slot Attention",
                   doi="10.48550/arXiv.2006.15055", authors=["Francesco Locatello"],
                   year=2020),
            record("pub", "rev_two", ["ARC-002"],
                   title="Object-centric learning with slot attention",
                   doi="10.5555/3495724.3496404", authors=["Locatello, Francesco"],
                   year=2020),
        ])
        self.write_index([])
        groups = self.groups()
        self.assertEqual(len(groups), 1)
        self.assertIn("title", groups[0]["routes"])

    def test_routes_union_transitively(self):
        """A shares a DOI with B; B shares a title with C -- one group of three."""
        self.write([
            record("a", "rev_one", ["ARC-001"], title="Alpha", doi="10.1/x"),
            record("b", "rev_two", ["ARC-002"], title="Shared Title Here",
                   doi="10.1/x"),
            record("c", "rev_three", ["ARC-003"], title="Shared Title Here",
                   doi="10.2/y"),
        ])
        self.write_index([])
        groups = self.groups()
        self.assertEqual(len(groups), 1)
        self.assertEqual(groups[0]["size"], 3)
        self.assertEqual(sorted(groups[0]["routes"]), ["doi", "title"])

    def test_same_literature_type_is_flagged(self):
        self.write([
            record("a", "rev_one", ["ARC-001"], title="A", doi="10.1/x"),
            record("b", "rev_one", ["ARC-001"], title="B", doi="10.1/x"),
        ])
        self.write_index([])
        self.assertTrue(self.groups()[0]["same_literature_type"])


# --------------------------------------------------------------------------
# NEGATIVE CONTROLS -- the half that stops the tool over-reporting


class TestNegativeControls(CorpusCase):

    def test_different_papers_same_author_same_year_do_not_group(self):
        """THE control the chip named. Crapse 2008, two real papers, one author.

        Both titles start 'Corollary discharge', the author and year are
        identical, and a 0.60 title ratio alone called them the same work. The
        distinct registered DOIs are what says they are not.
        """
        self.write([
            record("crapse_kingdom", "rev_one", ["MECH-256"],
                   title="Corollary discharge across the animal kingdom.",
                   doi="10.1038/nrn2457", authors=["Crapse TB"], year=2008),
            record("crapse_primate", "rev_two", ["MECH-256"],
                   title="Corollary discharge circuits in the primate brain.",
                   doi="10.1016/j.conb.2008.09.017",
                   authors=["Crapse, Trinity B."], year=2008),
        ])
        self.write_index([("rev_one", "crapse_kingdom", "MECH-256"),
                          ("rev_two", "crapse_primate", "MECH-256")])
        groups, candidates, _ = self.analyse()
        self.assertEqual(groups, [], "distinct DOIs must not be merged by title")
        self.assertEqual(candidates, [],
                         "a distinct-DOI pair must not even be a candidate")

    def test_craig_style_containment_with_distinct_dois_is_not_a_candidate(self):
        """Containment is the subtitle rule; here it spans two different papers.

        Craig 2002's title CONTAINS Craig 2003's verbatim, so the containment
        branch of titles_agree fires with full confidence. Only the identifier
        conflict separates them.
        """
        self.write([
            record("craig2002", "rev_one", ["MECH-100"],
                   title=("How do you feel? Interoception: the sense of the "
                          "physiological condition of the body."),
                   doi="10.1038/nrn894", authors=["Craig AD"], year=2002),
            record("craig2003", "rev_two", ["MECH-100"],
                   title=("Interoception: the sense of the physiological "
                          "condition of the body."),
                   doi="10.1038/nrn1153", authors=["Craig, A D"], year=2003),
        ])
        self.write_index([])
        groups, candidates, _ = self.analyse()
        self.assertEqual(groups, [])
        self.assertEqual(candidates, [])

    def test_short_title_containment_does_not_group(self):
        """'Pain' inside 'Pain and the Brain' is coincidence, not a subtitle.

        Guarded upstream by TITLE_CONTAINMENT_MIN_CHARS in the identifier
        verifier; asserted here so a change there is caught by this tool's own
        suite rather than only by that one's.
        """
        self.write([
            record("a", "rev_one", ["ARC-001"], title="Pain",
                   authors=["Jane Doe"], year=2010),
            record("b", "rev_two", ["ARC-001"], title="Pain and the Brain",
                   authors=["Jane Doe"], year=2010),
        ])
        self.write_index([])
        groups, candidates, _ = self.analyse()
        self.assertEqual(groups, [])
        self.assertEqual(candidates, [])

    def test_year_gap_suppresses_a_candidate(self):
        """Borbely 1982 vs the 2016 'reappraisal': neither carries a DOI."""
        self.write([
            record("borbely1982", "rev_one", ["MECH-200"],
                   title="A two process model of sleep regulation",
                   authors=["Alexander A. Borbely"], year=1982),
            record("borbely2016", "rev_two", ["MECH-200"],
                   title="The two-process model of sleep regulation: a reappraisal",
                   authors=["Alexander A. Borbely"], year=2016),
        ])
        self.write_index([])
        groups, candidates, _ = self.analyse()
        self.assertEqual(groups, [])
        self.assertEqual(candidates, [])

    def test_a_missing_year_never_suppresses(self):
        """The year guard must fail OPEN -- an absent year is not evidence."""
        self.write([
            record("a", "rev_one", ["ARC-001"],
                   title="Critical Learning Periods in Deep Neural Networks",
                   authors=["Alessandro Achille"], year=None),
            record("b", "rev_two", ["ARC-002"],
                   title="Critical Learning Periods in Deep Networks",
                   authors=["Alessandro Achille"], year=2019),
        ])
        self.write_index([])
        self.assertEqual(len(self.candidates()), 1)

    def test_conflicting_pmids_suppress_a_candidate(self):
        self.write([
            record("a", "rev_one", ["ARC-001"],
                   title="Critical Learning Periods in Deep Neural Networks",
                   authors=["A Achille"], year=2019, pmid="111"),
            record("b", "rev_two", ["ARC-002"],
                   title="Critical Learning Periods in Deep Networks",
                   authors=["A Achille"], year=2019, pmid="222"),
        ])
        self.write_index([])
        self.assertEqual(self.candidates(), [])

    def test_records_with_no_identifier_and_no_title_never_group(self):
        self.write([
            record("a", "rev_one", ["ARC-001"]),
            record("b", "rev_two", ["ARC-001"]),
        ])
        self.write_index([])
        groups, candidates, _ = self.analyse()
        self.assertEqual(groups, [])
        self.assertEqual(candidates, [])

    def test_unparseable_record_is_skipped_not_crashed(self):
        """validate_literature.py owns malformed records; this tool must not die."""
        self.write([
            record("a", "rev_one", ["ARC-001"], title="T", doi="10.1/x"),
            record("b", "rev_two", ["ARC-002"], title="T2", doi="10.1/x"),
        ])
        bad = self.lit / "rev_bad" / "entries" / "broken"
        bad.mkdir(parents=True)
        (bad / "record.json").write_text("{not json", encoding="utf-8")
        self.write_index([])
        self.assertEqual(len(self.groups()), 1)


# --------------------------------------------------------------------------
# grading


class TestGrading(CorpusCase):

    def test_overlapping_claims_live_in_index_are_double_counted(self):
        """The GFLAG-0030 Bekoff shape, reproduced in miniature."""
        self.write([
            record("bekoff_a", "rev_devrobotics", ["ARC-049", "INV-059", "MECH-196"],
                   title="Play Signals as Punctuation", doi="10.1163/156853995X00649",
                   confidence=0.72, authors=["Marc Bekoff"], year=1995),
            record("bekoff_b", "rev_ethological", ["ARC-049", "INV-059", "Q-035"],
                   title="Play signals as punctuation", doi="10.1163/156853995x00649",
                   confidence=0.88, authors=["Marc Bekoff"], year=1995),
        ])
        self.write_index([
            ("rev_devrobotics", "bekoff_a", "ARC-049"),
            ("rev_devrobotics", "bekoff_a", "INV-059"),
            ("rev_ethological", "bekoff_b", "ARC-049"),
            ("rev_ethological", "bekoff_b", "INV-059"),
        ])
        groups = self.groups()
        self.assertEqual(len(groups), 1)
        finding = groups[0]
        self.assertEqual(finding["grade"], "double_counted")
        self.assertEqual(finding["double_counted_claims"], ["ARC-049", "INV-059"])
        self.assertEqual(finding["double_counted_claims_live_in_index"],
                         ["ARC-049", "INV-059"])

    def test_overlapping_claims_absent_from_index_grade_overlapping(self):
        """Same defect in the corpus, but nothing is being inflated today."""
        self.write([
            record("a", "rev_one", ["ARC-049"], title="T", doi="10.1/x"),
            record("b", "rev_two", ["ARC-049"], title="T2", doi="10.1/x"),
        ])
        self.write_index([])
        finding = self.groups()[0]
        self.assertEqual(finding["grade"], "overlapping")
        self.assertEqual(finding["double_counted_claims"], ["ARC-049"])
        self.assertEqual(finding["double_counted_claims_live_in_index"], [])

    def test_one_record_in_the_index_is_not_double_counting(self):
        """Inflation needs TWO entries reaching the index for the same claim."""
        self.write([
            record("a", "rev_one", ["ARC-049"], title="T", doi="10.1/x"),
            record("b", "rev_two", ["ARC-049"], title="T2", doi="10.1/x"),
        ])
        self.write_index([("rev_one", "a", "ARC-049")])
        self.assertEqual(self.groups()[0]["grade"], "overlapping")

    def test_disjoint_claim_sets_are_the_weakest_grade(self):
        """One paper cited for two different claims is ordinary, not a defect."""
        self.write([
            record("a", "rev_one", ["ARC-001"], title="T", doi="10.1/x"),
            record("b", "rev_two", ["MECH-002"], title="T2", doi="10.1/x"),
        ])
        self.write_index([("rev_one", "a", "ARC-001"), ("rev_two", "b", "MECH-002")])
        finding = self.groups()[0]
        self.assertEqual(finding["grade"], "disjoint_claims")
        self.assertEqual(finding["double_counted_claims"], [])

    def test_double_counted_claims_is_pairwise_not_the_group_intersection(self):
        """A claim named by 2 of 3 records IS double-counted.

        The all-group intersection drops exactly that case, which is why both
        are emitted and why the grade keys off the pairwise one.
        """
        self.write([
            record("a", "rev_one", ["ARC-049"], title="T", doi="10.1/x"),
            record("b", "rev_two", ["ARC-049"], title="T2", doi="10.1/x"),
            record("c", "rev_three", ["MECH-900"], title="T3", doi="10.1/x"),
        ])
        self.write_index([("rev_one", "a", "ARC-049"), ("rev_two", "b", "ARC-049")])
        finding = self.groups()[0]
        self.assertEqual(finding["size"], 3)
        self.assertEqual(finding["claim_intersection"], [])
        self.assertEqual(finding["double_counted_claims"], ["ARC-049"])
        self.assertEqual(finding["grade"], "double_counted")

    def test_unreadable_index_cannot_produce_a_double_counted_grade(self):
        """Fail toward 'ungraded', never toward 'nothing is wrong'."""
        self.write([
            record("a", "rev_one", ["ARC-049"], title="T", doi="10.1/x"),
            record("b", "rev_two", ["ARC-049"], title="T2", doi="10.1/x"),
        ])
        self.claim_evidence.write_text("{broken", encoding="utf-8")
        groups, _, reach = self.analyse()
        self.assertIsNone(reach)
        self.assertEqual(groups[0]["grade"], "overlapping")

    def test_findings_are_sorted_strongest_first(self):
        self.write([
            record("d1", "rev_a", ["ARC-001"], title="X", doi="10.9/a"),
            record("d2", "rev_b", ["MECH-002"], title="X2", doi="10.9/a"),
            record("s1", "rev_c", ["ARC-049"], title="Y", doi="10.9/b"),
            record("s2", "rev_d", ["ARC-049"], title="Y2", doi="10.9/b"),
        ])
        self.write_index([("rev_c", "s1", "ARC-049"), ("rev_d", "s2", "ARC-049")])
        grades = [f["grade"] for f in self.groups()]
        self.assertEqual(grades, ["double_counted", "disjoint_claims"])


# --------------------------------------------------------------------------
# fuzzy candidates


class TestFuzzyCandidates(CorpusCase):

    def _achille(self):
        self.write([
            record("a", "rev_one", ["Q-088"],
                   title="Critical Learning Periods in Deep Neural Networks",
                   authors=["Alessandro Achille"], year=2019),
            record("b", "rev_two", ["Q-088"],
                   title="Critical Learning Periods in Deep Networks",
                   authors=["Alessandro Achille"], year=2019),
        ])
        self.write_index([("rev_one", "a", "Q-088"), ("rev_two", "b", "Q-088")])

    def test_a_fuzzy_pair_becomes_a_candidate_not_a_group(self):
        self._achille()
        groups, candidates, _ = self.analyse()
        self.assertEqual(groups, [])
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["shared_claim_ids"], ["Q-088"])

    def test_fuzzy_pair_is_never_graded_double_counted(self):
        """Both records reach the index for Q-088 -- and it is STILL not a finding.

        This is the whole reason the route was demoted: three of the measured
        false positives had exactly this shape.
        """
        self._achille()
        groups, candidates, _ = self.analyse()
        self.assertEqual([f["grade"] for f in groups], [])
        self.assertNotIn("grade", candidates[0])

    def test_dropping_title_fuzzy_from_keys_removes_candidates(self):
        self._achille()
        self.assertEqual(self.candidates(keys=("doi", "pmid", "title")), [])

    def test_a_pair_already_grouped_exactly_is_not_re_reported(self):
        self.write([
            record("a", "rev_one", ["ARC-001"], title="Identical Title Value",
                   doi="10.1/x", authors=["Jane Doe"], year=2020),
            record("b", "rev_two", ["ARC-002"], title="Identical Title Value",
                   doi="10.1/x", authors=["Jane Doe"], year=2020),
        ])
        self.write_index([])
        groups, candidates, _ = self.analyse()
        self.assertEqual(len(groups), 1)
        self.assertEqual(candidates, [])

    def test_candidates_are_sorted_shared_claims_first(self):
        self.write([
            record("s1", "rev_one", ["ARC-050"],
                   title="Learning Periods in Deep Neural Networks",
                   authors=["Alessandro Achille"], year=2019),
            record("s2", "rev_two", ["ARC-050"],
                   title="Learning Periods in Deep Networks",
                   authors=["Alessandro Achille"], year=2019),
            record("d1", "rev_three", ["ARC-060"],
                   title="Predictive Coding in the Visual Cortex Explained",
                   authors=["Rajesh Rao"], year=1999),
            record("d2", "rev_four", ["ARC-061"],
                   title="Predictive Coding in the Visual Cortex",
                   authors=["Rajesh Rao"], year=1999),
        ])
        self.write_index([])
        candidates = self.candidates()
        self.assertEqual(len(candidates), 2)
        self.assertTrue(candidates[0]["shared_claim_ids"])
        self.assertFalse(candidates[1]["shared_claim_ids"])


# --------------------------------------------------------------------------
# CLI surface and conventions


class TestCli(CorpusCase):

    def _double_counted_corpus(self):
        self.write([
            record("a", "rev_one", ["ARC-049"], title="T", doi="10.1/x"),
            record("b", "rev_two", ["ARC-049"], title="T2", doi="10.1/x"),
        ])
        self.write_index([("rev_one", "a", "ARC-049"), ("rev_two", "b", "ARC-049")])

    def _run(self, extra=()):
        argv = ["--lit-root", str(self.lit),
                "--claim-evidence", str(self.claim_evidence)] + list(extra)
        buf = io.StringIO()
        stdout, sys.stdout = sys.stdout, buf
        try:
            code = dup.main(argv)
        finally:
            sys.stdout = stdout
        return code, buf.getvalue()

    def test_exit_zero_by_default_even_with_findings(self):
        self._double_counted_corpus()
        code, out = self._run()
        self.assertEqual(code, 0)
        self.assertIn("DOUBLE_COUNTED", out)

    def test_exit_nonzero_gates_on_a_finding(self):
        self._double_counted_corpus()
        self.assertEqual(self._run(["--exit-nonzero"])[0], 1)

    def test_exit_nonzero_is_clean_on_a_clean_corpus(self):
        self.write([record("a", "rev_one", ["ARC-001"], title="T", doi="10.1/x")])
        self.write_index([])
        self.assertEqual(self._run(["--exit-nonzero"])[0], 0)

    def test_candidates_alone_do_not_gate(self):
        """A candidate is a question. A question must never fail a caller."""
        self.write([
            record("a", "rev_one", ["Q-088"],
                   title="Critical Learning Periods in Deep Neural Networks",
                   authors=["Alessandro Achille"], year=2019),
            record("b", "rev_two", ["Q-088"],
                   title="Critical Learning Periods in Deep Networks",
                   authors=["Alessandro Achille"], year=2019),
        ])
        self.write_index([])
        code, out = self._run(["--exit-nonzero"])
        self.assertEqual(code, 0)
        self.assertIn("UNCONFIRMED CANDIDATES", out)

    def test_output_is_ascii_only(self):
        """CLAUDE.md: printed output must survive a cp1252 terminal."""
        self.write([
            record("a", "rev_one", ["ARC-049"], title="Theta-gamma coupling",
                   doi="10.1/x", authors=["Nikolai Axmacher"], year=2010),
            record("b", "rev_two", ["ARC-049"], title="Theta gamma coupling",
                   doi="10.1/x", authors=["Axmacher, N"], year=2010),
        ])
        self.write_index([("rev_one", "a", "ARC-049"), ("rev_two", "b", "ARC-049")])
        out = self._run()[1]
        out.encode("ascii")

    def test_json_mode_carries_groups_and_candidates(self):
        self._double_counted_corpus()
        target = self.tmp / "out.json"
        self._run(["--json", str(target)])
        data = json.loads(target.read_text(encoding="utf-8"))
        self.assertEqual(data["n_records"], 2)
        self.assertTrue(data["claim_evidence_readable"])
        self.assertEqual(data["counts"]["double_counted"], 1)
        self.assertIn("unconfirmed_candidates", data)
        self.assertEqual(data["groups"][0]["double_counted_claims"], ["ARC-049"])

    def test_max_groups_names_what_it_dropped(self):
        """CLAUDE.md 'No silent caps' -- truncation must be visible."""
        self.write([
            record("a", "rev_one", ["ARC-001"], title="T", doi="10.1/x"),
            record("b", "rev_two", ["ARC-002"], title="T2", doi="10.1/x"),
            record("c", "rev_three", ["ARC-003"], title="U", doi="10.2/y"),
            record("d", "rev_four", ["ARC-004"], title="U2", doi="10.2/y"),
        ])
        self.write_index([])
        out = self._run(["--max-groups", "1"])[1]
        self.assertIn("not shown", out)

    def test_only_overlapping_hides_and_says_so(self):
        self.write([
            record("a", "rev_one", ["ARC-001"], title="T", doi="10.1/x"),
            record("b", "rev_two", ["MECH-002"], title="T2", doi="10.1/x"),
        ])
        self.write_index([])
        out = self._run(["--only-overlapping"])[1]
        self.assertIn("hidden by --only-overlapping", out)

    def test_unknown_key_is_rejected(self):
        self._double_counted_corpus()
        with self.assertRaises(SystemExit):
            self._run(["--keys", "doi,isbn"])

    def test_keys_can_restrict_to_one_route(self):
        self.write([
            record("a", "rev_one", ["ARC-001"], title="Same Title Here",
                   doi="10.1/x"),
            record("b", "rev_two", ["ARC-002"], title="Same Title Here",
                   doi="10.2/y"),
        ])
        self.write_index([])
        self.assertEqual(self.groups(keys=("doi",)), [])
        self.assertEqual(len(self.groups(keys=("title",))), 1)


class TestHelpers(unittest.TestCase):

    def test_normalise_pmid_forms(self):
        self.assertEqual(dup.normalise_pmid("PMID: 9119582"), "9119582")
        self.assertEqual(dup.normalise_pmid(9119582), "9119582")
        self.assertEqual(dup.normalise_pmid("0009119582"), "9119582")
        self.assertIsNone(dup.normalise_pmid(None))
        self.assertIsNone(dup.normalise_pmid("  "))

    def test_normalise_doi_is_reused_not_reimplemented(self):
        """Guards against a fork of the legacy APA double-slash rule."""
        import verify_literature_identifiers as ident
        self.assertIs(dup.ident.normalise_doi, ident.normalise_doi)

    def test_identifiers_conflict_only_on_two_present_and_different(self):
        def rec(doi=None, pmid=None):
            return {"doi": doi, "pmid": pmid}
        self.assertTrue(dup._identifiers_conflict(rec(doi="a"), rec(doi="b")))
        self.assertTrue(dup._identifiers_conflict(rec(pmid="1"), rec(pmid="2")))
        self.assertFalse(dup._identifiers_conflict(rec(doi="a"), rec(doi="a")))
        self.assertFalse(dup._identifiers_conflict(rec(doi="a"), rec()))
        self.assertFalse(dup._identifiers_conflict(rec(), rec()))


if __name__ == "__main__":
    unittest.main(verbosity=2)
