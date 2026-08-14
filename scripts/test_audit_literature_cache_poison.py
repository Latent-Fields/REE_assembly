#!/usr/bin/env python3
"""Tests for audit_literature_bibliographic_accuracy.py --scan-poison.

Time-independent: every cache is built in a tempdir from literal dicts, no
clock is read, and nothing touches the network (the scan itself never does).

ROUGHLY HALF OF THESE ARE NEGATIVE CONTROLS, and for a specific reason. The
scan's failure mode is not missing poison, it is CALLING AN ANSWER POISON --
that deletes a perfectly good cached "no such DOI" and re-fetches it on every
sweep forever. Crossref's and doi.org's 404 IS an answer, and the tests that
assert so are the ones that stop a later session widening the predicate to "any
non-ok entry is poison":

    test_crossref_http_404_is_an_answer
    test_doiorg_http_404_is_an_answer
    test_ok_entries_are_never_poison
    test_pubmed_not_found_is_an_answer

The other direction has a worked example too. The first hand-written version of
this scan (in the chip brief that commissioned it) used one global answer set
containing ``http_404``, and therefore could not report a pubmed ``http_404`` --
even though its own comment said that case IS poison, because NCBI eutils
answers an unknown id with 200 + an error field and never 404s it. That is
``test_pubmed_http_404_is_poison``.

``test_answer_sets_are_derived_not_restated`` is the anti-drift assertion: it
mutates the fetchers' own ``DOI_ANSWER_HTTP_CODES`` and asserts the scan's
verdict follows. A hand-copied table would pass every other test here and
silently stop matching the fetchers the moment one of them changed.
"""

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import audit_literature_bibliographic_accuracy as audit  # noqa: E402


class CachePoisonScanTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="ree-cache-poison-"))
        self.cache = self.tmp / "lit_bib_cache"

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    # -- helpers ---------------------------------------------------------
    def write(self, kind, name, payload, raw=None):
        path = self.cache / kind / (name + ".json")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(raw if raw is not None else json.dumps(payload),
                        encoding="utf-8")
        return path

    def poisoned(self, kind):
        for scanned_kind, _total, bad in audit.scan_cache_poison(self.cache):
            if scanned_kind == kind:
                return [error for _path, error in bad]
        return None

    def totals(self):
        scanned = audit.scan_cache_poison(self.cache)
        return (sum(t for _k, t, _b in scanned),
                sum(len(b) for _k, _t, b in scanned))

    # -- negative controls: answers must NOT be graded poison -------------
    def test_crossref_http_404_is_an_answer(self):
        self.write("crossref", "10.1234_nope", {"ok": False, "error": "http_404"})
        self.assertEqual(self.poisoned("crossref"), [])

    def test_doiorg_http_404_is_an_answer(self):
        self.write("doiorg", "10.1234_nope", {"ok": False, "error": "http_404"})
        self.assertEqual(self.poisoned("doiorg"), [])

    def test_pubmed_not_found_is_an_answer(self):
        self.write("pubmed", "99999999", {"ok": False, "error": "not_found"})
        self.assertEqual(self.poisoned("pubmed"), [])

    def test_ok_entries_are_never_poison(self):
        for kind in ("crossref", "doiorg", "pubmed", "arxiv", "pmc",
                     "openlibrary", "pubmed_aid"):
            self.write(kind, "good", {"ok": True, "message": {"x": 1}})
        self.assertEqual(self.totals(), (7, 0))

    def test_openlibrary_and_arxiv_not_found_are_answers(self):
        self.write("openlibrary", "isbn", {"ok": False, "error": "not_found"})
        self.write("arxiv", "2307.07176", {"ok": False, "error": "not_found"})
        self.assertEqual(self.poisoned("openlibrary"), [])
        self.assertEqual(self.poisoned("arxiv"), [])

    def test_empty_cache_reports_nothing(self):
        self.assertEqual(audit.scan_cache_poison(self.cache), [])

    # -- positive: transport failures ARE poison --------------------------
    def test_pubmed_http_404_is_poison(self):
        """eutils never 404s an unknown id, so a 404 there is about the request."""
        self.write("pubmed", "12345678", {"ok": False, "error": "http_404"})
        self.assertEqual(self.poisoned("pubmed"), ["http_404"])

    def test_rate_limit_and_server_errors_are_poison_everywhere(self):
        self.write("crossref", "a", {"ok": False, "error": "http_429"})
        self.write("doiorg", "b", {"ok": False, "error": "http_503"})
        self.write("pubmed", "c", {"ok": False, "error": "http_429"})
        self.assertEqual(self.poisoned("crossref"), ["http_429"])
        self.assertEqual(self.poisoned("doiorg"), ["http_503"])
        self.assertEqual(self.poisoned("pubmed"), ["http_429"])

    def test_exception_text_is_poison(self):
        self.write("crossref", "a",
                   {"ok": False, "error": "URLError: <urlopen error timed out>"})
        self.assertEqual(len(self.poisoned("crossref")), 1)

    def test_any_non_ok_pubmed_aid_entry_is_poison(self):
        """esearch answers an unknown DOI with 200 + count=0, so it has no
        not-found answer to cache -- its answer set is empty on purpose."""
        self.write("pubmed_aid", "10.1_x", {"ok": False, "error": "not_found"})
        self.assertEqual(self.poisoned("pubmed_aid"), ["not_found"])

    def test_unparseable_entry_is_poison(self):
        self.write("crossref", "trunc", None, raw='{"ok": tru')
        self.assertEqual(self.poisoned("crossref"), ["UNPARSEABLE"])

    def test_unknown_cache_kind_is_reported_not_assumed_clean(self):
        self.write("semanticscholar", "x", {"ok": False, "error": "not_found"})
        kinds = [k for k, _t, _b in audit.scan_cache_poison(self.cache)]
        self.assertEqual(kinds, ["UNKNOWN:semanticscholar"])
        self.assertEqual(self.poisoned("UNKNOWN:semanticscholar"), ["not_found"])

    # -- anti-drift --------------------------------------------------------
    def test_answer_sets_are_derived_not_restated(self):
        """The table must follow the fetchers' constants, not copy them."""
        self.write("crossref", "a", {"ok": False, "error": "http_404"})
        self.assertEqual(self.poisoned("crossref"), [])
        original = audit.DOI_ANSWER_HTTP_CODES
        try:
            audit.DOI_ANSWER_HTTP_CODES = frozenset({410})
            audit.CACHE_ANSWER_ERRORS = dict(
                audit.CACHE_ANSWER_ERRORS,
                crossref=audit._http_errors(audit.DOI_ANSWER_HTTP_CODES))
            self.assertEqual(self.poisoned("crossref"), ["http_404"])
        finally:
            audit.DOI_ANSWER_HTTP_CODES = original
            audit.CACHE_ANSWER_ERRORS = dict(
                audit.CACHE_ANSWER_ERRORS,
                crossref=audit._http_errors(original))

    # -- purge + CLI -------------------------------------------------------
    def test_purge_deletes_only_poisoned_entries(self):
        answer = self.write("crossref", "keep", {"ok": False, "error": "http_404"})
        good = self.write("crossref", "ok", {"ok": True, "message": {}})
        bad = self.write("crossref", "drop", {"ok": False, "error": "http_429"})
        rc = audit.main(["--scan-poison", "--purge-poison",
                         "--cache", str(self.cache)])
        self.assertEqual(rc, 0)
        self.assertTrue(answer.exists())
        self.assertTrue(good.exists())
        self.assertFalse(bad.exists())

    def test_scan_alone_deletes_nothing(self):
        bad = self.write("crossref", "drop", {"ok": False, "error": "http_429"})
        audit.main(["--scan-poison", "--cache", str(self.cache)])
        self.assertTrue(bad.exists())

    def test_exit_nonzero_gates_on_poison_only(self):
        self.write("crossref", "keep", {"ok": False, "error": "http_404"})
        self.assertEqual(audit.main(["--scan-poison", "--exit-nonzero",
                                     "--cache", str(self.cache)]), 0)
        self.write("crossref", "drop", {"ok": False, "error": "http_429"})
        self.assertEqual(audit.main(["--scan-poison", "--exit-nonzero",
                                     "--cache", str(self.cache)]), 1)

    def test_purge_without_scan_is_refused(self):
        """--purge-poison alone must not fall through to --report."""
        with self.assertRaises(SystemExit):
            audit.main(["--purge-poison", "--cache", str(self.cache)])

    def test_missing_cache_dir_is_not_an_error(self):
        rc = audit.main(["--scan-poison", "--cache", str(self.tmp / "absent")])
        self.assertEqual(rc, 0)


if __name__ == "__main__":
    unittest.main()
