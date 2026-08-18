#!/usr/bin/env python3
"""Tests for verify_literature_identifiers.py and its commit-gate wiring.

Time-independent and OFFLINE: every corpus and every API response is built in a
tempdir from literal dicts, no clock is read, and nothing touches the network.
The response cache is a fixture directory, so the resolver's cache-first path is
exercised for real rather than stubbed -- which matters, because the cache key
normalisation (DOIs are cached lower-cased) is itself load-bearing and has bitten
before.

ROUGHLY HALF OF THESE ARE NEGATIVE CONTROLS, and that is the point. This checker
gates commits, so its expensive failure is not missing a bad identifier -- the
whole-corpus audit still finds those -- it is firing on a CORRECT record, because
a gate that fires on ordinary work gets switched off and then protects nothing.
The 2026-08-14 audit documents four false-positive classes by name, and every one
of them is pinned here as a record that must NOT produce a verdict:

    test_subtitle_truncation_alone_does_not_fire          subtitle truncation
    test_short_subtitle_truncation_agrees                 (the SHORT-title form,
                                                          which the first cut of
                                                          this file got wrong and
                                                          shipped as a live false
                                                          positive -- see
                                                          test_unengaged_mind_*)
    test_o_slash_surname_agrees                           non-ASCII surnames
    test_dotless_i_surname_agrees                         non-ASCII surnames
    test_author_name_change_alone_does_not_fire           author name changes
    test_preprint_author_order_alone_does_not_fire        preprint author order
    test_legacy_apa_double_slash_is_not_a_mismatch        the 2-of-9 cross-check
                                                          false positive

plus the fail-open contract, which is the other half of not getting switched off:

    test_unresolvable_identifier_fails_open
    test_offline_fails_open_and_names_what_it_skipped
    test_network_budget_spent_fails_open_and_names_it
    test_record_without_declared_authors_fails_open
    test_empty_scope_is_a_noop_not_a_whole_corpus_scan

If a later change widens any predicate, the negative half fails before the
widening ships. If a later change narrows the fail-open contract, the same.

The true positives are the real defects the check found in this corpus, kept as
literal fixtures so they cannot regress: the near-miss DOI (Engel & Fries), the
wrong PMID (Ferrand), the DOI recovered from a correct PMID (Michelet), and the
both-wrong-and-mutually-inconsistent case (Craig).
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import urllib.error
import urllib.request
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import audit_literature_bibliographic_accuracy as audit  # noqa: E402
import verify_literature_identifiers as V  # noqa: E402

REPO_ROOT = SCRIPTS_DIR.parent


# --------------------------------------------------------------------------
# fixture helpers


def crossref_payload(title, authors, year, venue="A Journal", **extra):
    """A Crossref /works message, in the shape audit.crossref_view reads."""
    message = {
        "title": [title],
        "author": [{"family": a} for a in authors],
        "issued": {"date-parts": [[year]]},
        "container-title": [venue],
        "type": "journal-article",
    }
    message.update(extra)
    return {"ok": True, "message": message}


def pubmed_payload(title, authors, year, doi=None, venue="A Journal", pmc=None,
                   pmc_only_in_pmcid=False, **extra):
    """An esummary record, in the shape audit.pubmed_view reads.

    ``pmc`` adds the PMC crosswalk fields. Real esummary records carry the id
    TWICE -- cleanly under idtype ``pmc``, and wrapped in prose under idtype
    ``pmcid`` (``pmc-id: PMC8497431;manuscript-id: NIHMS1731801;``) -- so both
    are emitted, and ``pmc_only_in_pmcid`` builds the fallback-only shape the
    handful of records that serve one and not the other actually have.
    """
    ids = [{"idtype": "pubmed", "value": "1"}]
    if doi:
        ids.append({"idtype": "doi", "value": doi})
    if pmc:
        if not pmc_only_in_pmcid:
            ids.append({"idtype": "pmc", "value": pmc})
        ids.append({"idtype": "pmcid", "value": "pmc-id: %s;" % pmc})
    message = {
        "title": title,
        "authors": [{"name": a, "authtype": "Author"} for a in authors],
        "pubdate": "%d Jan" % year,
        "fulljournalname": venue,
        "articleids": ids,
    }
    message.update(extra)
    return {"ok": True, "message": message}


def arxiv_payload(arxiv_id, title, authors, year):
    """An arXiv entry, in the shape V._parse_arxiv_atom produces.

    The ``id`` carries a VERSION SUFFIX because the real API always does -- a
    query for ``2307.07176`` is answered with ``.../abs/2307.07176v3`` -- and
    ``arxiv_entry_is_faithful`` has to see through that or it refuses every hit
    it is given.
    """
    return {"ok": True, "message": {
        "id": "http://arxiv.org/abs/%sv2" % arxiv_id,
        "title": title,
        "authors": list(authors),
        "published": "%d-03-15T07:27:12Z" % year,
    }}


def openlibrary_payload(title, authors, year, subtitle=None,
                        publisher="A Press"):
    """An OpenLibrary /api/books record, in the shape V.openlibrary_view reads.

    ``authors`` for an edited volume is its EDITORS, which is exactly why
    verdict 8 is report-only -- see TestIsbnIsNotOnTheGatePath.
    """
    message = {
        "title": title,
        "authors": [{"name": a} for a in authors],
        "publish_date": str(year),
        "publishers": [{"name": publisher}],
    }
    if subtitle:
        message["subtitle"] = subtitle
    return {"ok": True, "message": message}


class Fixture:
    """A throwaway REE_assembly-shaped corpus plus a response cache."""

    def __init__(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="lit_ident_test_"))
        self.repo = self.tmp / "REE_assembly"
        self.lit = self.repo / "evidence" / "literature"
        self.cache = self.tmp / "cache"
        self.lit.mkdir(parents=True)
        self.cache.mkdir()

    def close(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def record(self, entry, source, literature_type="targeted_review_x",
               summary="# Summary\n\nbody\n"):
        entry_dir = self.lit / literature_type / "entries" / entry
        entry_dir.mkdir(parents=True, exist_ok=True)
        (entry_dir / "record.json").write_text(json.dumps({
            "schema_version": "literature_evidence/v1",
            "literature_type": literature_type,
            "entry_id": entry,
            "timestamp_utc": "2026-08-14T00:00:00Z",
            "claim_ids_tested": ["MECH-001"],
            "source": source,
            "evidence_class": "theoretical_review",
            "evidence_direction": "supports",
            "confidence": 0.5,
            "confidence_rationale": "fixture",
            "summary_path": "summary.md",
            "tags": ["fixture"],
        }, indent=1), encoding="utf-8")
        (entry_dir / "summary.md").write_text(summary, encoding="utf-8")
        return entry_dir / "record.json"

    # Mirror the module's own key normalisation rather than restating it: a test
    # that hardcodes the key passes even when the key rule changes, which is the
    # failure mode this dict exists to prevent. Every entry is the SAME callable
    # the module uses on the fetch path, never a re-implementation of it.
    KEY_NORMALISERS = {
        "crossref": lambda i: str(i).lower(),
        "doiorg": lambda i: str(i).lower(),
        V.PUBMED_AID_CACHE_KIND: staticmethod(V.aid_cache_key),
        V.ARXIV_CACHE_KIND: staticmethod(V.normalise_arxiv_id),
        V.OPENLIBRARY_CACHE_KIND: staticmethod(V.canonical_isbn),
        V.PMC_CACHE_KIND: staticmethod(V.normalise_pmc),
    }

    def cache_put(self, kind, ident, payload):
        normalise = self.KEY_NORMALISERS.get(kind)
        if normalise is not None:
            normalise = getattr(normalise, "__func__", normalise)
            key = normalise(ident)
        else:
            key = str(ident)
        path = audit.cache_path(self.cache, kind, key)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload), encoding="utf-8")

    def resolver(self, **kwargs):
        kwargs.setdefault("offline", True)
        return V.Resolver(self.cache, **kwargs)


class FixtureCase(unittest.TestCase):
    """Base case that repoints the module at a throwaway corpus and restores it."""

    def setUp(self):
        self.fx = Fixture()
        self._saved = (V.REPO, audit.REPO, audit.LIT_ROOT)
        V.set_repo(self.fx.repo)
        self.addCleanup(self._restore)
        self.addCleanup(self.fx.close)

    def _restore(self):
        V.REPO, audit.REPO, audit.LIT_ROOT = self._saved

    def verdicts_for(self, record_path, **resolver_kwargs):
        targets = V.collect_scoped_targets([str(record_path)])
        resolver = self.fx.resolver(**resolver_kwargs)
        out = []
        for target in targets:
            out.extend(V.verify_target(target, resolver))
        return out, resolver

    def assertNoVerdict(self, record_path, **kwargs):
        verdicts, _ = self.verdicts_for(record_path, **kwargs)
        live = [v for v in verdicts if not v.kind.startswith("waived:")]
        self.assertEqual(
            [], [v.kind for v in live],
            "expected no verdict, got: %s"
            % "; ".join("%s: %s" % (v.kind, v.detail) for v in live))

    def assertVerdict(self, record_path, kind, **kwargs):
        verdicts, _ = self.verdicts_for(record_path, **kwargs)
        kinds = [v.kind for v in verdicts]
        self.assertIn(kind, kinds, "expected %r, got %r" % (kind, kinds))
        return [v for v in verdicts if v.kind == kind][0]


# --------------------------------------------------------------------------
# titles_agree -- the subtitle-truncation false positive and its traps


class TestTitlesAgree(unittest.TestCase):

    def test_identical_titles_agree(self):
        self.assertIs(True, V.titles_agree("A Study of Things",
                                           "A Study of Things"))

    def test_subtitle_truncation_alone_does_not_fire(self):
        # The audit's own documented example. Crossref stores only the main
        # title for many publishers; the ratio is 0.24, so ONLY containment can
        # save this.
        self.assertIs(True, V.titles_agree(
            "The p Factor",
            "The p Factor: One General Psychopathology Factor in the Structure "
            "of Psychiatric Disorders?"))

    def test_unengaged_mind_short_subtitle_truncation_agrees(self):
        # THE LIVE FALSE POSITIVE the first cut of this file shipped.
        # norm_title("The Unengaged Mind") is 18 characters, below the
        # 20-character free-substring floor, so containment was refused and the
        # pair fell through to a 0.48 ratio and produced a verdict on a
        # perfectly correct record. Fixed by the affix rule at 12 characters.
        self.assertIs(True, V.titles_agree(
            "The Unengaged Mind",
            "The Unengaged Mind: Defining Boredom in Terms of Attention."))

    def test_prepended_section_heading_agrees(self):
        # The reverse direction: PubMed prepends a section heading, so the
        # declared title is a SUFFIX of the authoritative one.
        self.assertIs(True, V.titles_agree(
            "Social psychology. Just think: the challenges of the disengaged mind",
            "Just think: the challenges of the disengaged mind"))

    def test_markup_and_accents_do_not_prevent_agreement(self):
        self.assertIs(True, V.titles_agree(
            "<i>Naive</i> realism and the illusion of objectivity",
            "Naive realism and the illusion of objectivity"))

    # -- negative controls ------------------------------------------------

    def test_short_prefix_does_not_agree(self):
        # 'Pain' is 4 characters. Containment here is coincidence, and treating
        # it as agreement would silence a real wrong-identifier finding.
        self.assertIs(False, V.titles_agree(
            "Pain", "Pain and the Brain: Specificity and Plasticity"))

    def test_short_word_prefix_does_not_agree(self):
        self.assertIs(False, V.titles_agree(
            "Learning", "Learning to see the wood for the trees"))

    def test_word_boundary_is_required_for_containment(self):
        # 'the p factor' is 12 characters and IS a raw prefix of
        # 'the p factorial design of experiments', but not a whole-word one.
        # Without the space padding this would agree, and it must not.
        self.assertIs(False, V.titles_agree(
            "The p Factor", "The p Factorial Design of Experiments in Genetics"))

    def test_genuinely_different_works_do_not_agree(self):
        # The real Berridge pair the cross-check found: two 2009 papers by the
        # same author, one recorded for the other.
        self.assertIs(False, V.titles_agree(
            "Dissecting components of reward: 'liking', 'wanting', and learning",
            "'Liking' and 'wanting' food rewards: brain substrates and roles in "
            "eating disorders"))

    def test_empty_title_is_none_not_false(self):
        # None means "nothing to compare", which the callers treat as a PASS.
        # Returning False here would block every record whose identifier
        # resolves to a title-less Crossref stub.
        self.assertIsNone(V.titles_agree("", "A Real Title"))
        self.assertIsNone(V.titles_agree("A Real Title", None))


# --------------------------------------------------------------------------
# name folding -- the non-ASCII-surname false positive


class TestNameFolding(unittest.TestCase):

    def test_o_slash_surname_agrees(self):
        # o-slash is not decomposed by NFKD, so audit.strip_accents leaves it
        # and a correct ASCII transliteration reads as a mismatch.
        self.assertIs(True, V.first_authors_agree(["Hoydal OA"],
                                                  ["Høydal"]))

    def test_dotless_i_surname_agrees(self):
        self.assertIs(True, V.first_authors_agree(
            ["Rodriguez, Ana"], ["Rodrı́guez"]))

    def test_ligature_and_sharp_s_agree(self):
        self.assertIs(True, V.first_authors_agree(["Aeby"], ["Æby"]))
        self.assertIs(True, V.first_authors_agree(["Gross"], ["Groß"]))

    def test_initials_only_form_agrees(self):
        # The corpus mixes 'Colosio M' and 'Marco Colosio'.
        self.assertIs(True, V.first_authors_agree(["Colosio M"],
                                                  ["Marco Colosio"]))

    def test_comma_form_agrees(self):
        self.assertIs(True, V.first_authors_agree(["Murray, Lynne"], ["Murray"]))

    # -- negative controls ------------------------------------------------

    def test_different_surnames_do_not_agree(self):
        self.assertIs(False, V.first_authors_agree(["Berridge"], ["Gilmore"]))

    def test_empty_author_list_is_none_not_false(self):
        self.assertIsNone(V.first_authors_agree([], ["Berridge"]))
        self.assertIsNone(V.first_authors_agree(["Berridge"], []))

    def test_consortium_only_author_is_none_not_false(self):
        # Crossref sometimes carries a single-token consortium name that yields
        # no usable surname token. That must pass, not block.
        self.assertIsNone(V.first_authors_agree(["Smith"], ["A"]))


# --------------------------------------------------------------------------
# DOI normalisation -- the legacy APA double-slash false positive


class TestNormaliseDoi(unittest.TestCase):

    def test_legacy_apa_double_slash_collapses(self):
        # 2 of the cross-check's 9 raw disagreements were ONLY this.
        self.assertEqual(V.normalise_doi("10.1037//0022-006x.64.2.295"),
                         V.normalise_doi("10.1037/0022-006x.64.2.295"))

    def test_case_is_folded(self):
        self.assertEqual(V.normalise_doi("10.48550/ARXIV.2301.00001"),
                         V.normalise_doi("10.48550/arxiv.2301.00001"))

    def test_resolver_prefixes_are_stripped(self):
        for form in ("https://doi.org/10.1/a", "http://dx.doi.org/10.1/a",
                     "doi:10.1/a", "10.1/a", "10.1/a."):
            self.assertEqual("10.1/a", V.normalise_doi(form), form)

    def test_empty_is_none(self):
        self.assertIsNone(V.normalise_doi(None))
        self.assertIsNone(V.normalise_doi(""))

    def test_near_miss_dois_are_not_equal(self):
        # The whole defect class. If normalisation ever collapsed these, the
        # gate would pass exactly what it exists to catch.
        self.assertNotEqual(V.normalise_doi("10.1016/j.conb.2010.02.014"),
                            V.normalise_doi("10.1016/j.conb.2010.02.015"))
        self.assertNotEqual(V.normalise_doi("10.3390/jcm11082204"),
                            V.normalise_doi("10.3390/jcm11082210"))


class TestPlaceholderDoi(unittest.TestCase):

    def test_known_placeholders_are_detected(self):
        for doi in ("10.0000/example-doi", "10.1234/example",
                    "10.1234/placeholder-1", "10.1234/TODO",
                    "10.1234/xxxxx", "10.1234/"):
            self.assertTrue(V.is_placeholder_doi(doi), doi)

    def test_real_dois_are_not_placeholders(self):
        for doi in ("10.1038/nrn894", "10.1523/JNEUROSCI.4718-06.2007",
                    "10.48550/arXiv.2301.00001", "10.1163/156853995X00649",
                    "10.1037//0022-006x.64.2.295"):
            self.assertFalse(V.is_placeholder_doi(doi), doi)

    def test_placeholder_needs_no_network(self):
        self.assertFalse(V.is_placeholder_doi(None))


# --------------------------------------------------------------------------
# verdict 1 -- the record's own two identifiers contradict each other


class TestDoiPmidMismatch(FixtureCase):

    def test_mismatch_fires(self):
        # The real Ferrand shape: the DOI is right, the PMID is a different
        # paper in the same journal and issue.
        rec = self.fx.record("ferrand2022", {
            "title": "Which Actigraphy Dimensions Predict Longitudinal Outcomes "
                     "in Bipolar Disorders?",
            "authors": ["Ferrand, Lisa"], "year": 2022,
            "venue": "Journal of Clinical Medicine",
            "doi": "10.3390/jcm11082204", "pmid": "35456302"})
        self.fx.cache_put("crossref", "10.3390/jcm11082204", crossref_payload(
            "Which Actigraphy Dimensions Predict Longitudinal Outcomes in "
            "Bipolar Disorders?", ["Ferrand"], 2022))
        self.fx.cache_put("pubmed", "35456302", pubmed_payload(
            "Chronological Analysis of Primary Cervical Spine Infection.",
            ["Sung MJ"], 2022, doi="10.3390/jcm11082210"))
        verdict = self.assertVerdict(rec, "doi_pmid_mismatch")
        self.assertIn("10.3390/jcm11082210", verdict.detail)

    def test_agreement_is_silent(self):
        rec = self.fx.record("good2022", {
            "title": "A Study of Things", "authors": ["Ferrand, Lisa"],
            "year": 2022, "doi": "10.3390/jcm11082204", "pmid": "35456294"})
        self.fx.cache_put("crossref", "10.3390/jcm11082204", crossref_payload(
            "A Study of Things", ["Ferrand"], 2022))
        self.fx.cache_put("pubmed", "35456294", pubmed_payload(
            "A Study of Things.", ["Ferrand L"], 2022,
            doi="10.3390/jcm11082204"))
        self.assertNoVerdict(rec)

    def test_legacy_apa_double_slash_is_not_a_mismatch(self):
        # NEGATIVE CONTROL for the documented cross-check false positive: PubMed
        # serves 10.1037//..., the record declares 10.1037/....
        rec = self.fx.record("jacobson1996", {
            "title": "A Component Analysis of Cognitive-Behavioral Treatment",
            "authors": ["Jacobson, Neil S."], "year": 1996,
            "doi": "10.1037/0022-006x.64.2.295", "pmid": "8871414"})
        self.fx.cache_put("crossref", "10.1037/0022-006x.64.2.295",
                          crossref_payload(
                              "A Component Analysis of Cognitive-Behavioral "
                              "Treatment", ["Jacobson"], 1996))
        self.fx.cache_put("pubmed", "8871414", pubmed_payload(
            "A component analysis of cognitive-behavioral treatment.",
            ["Jacobson NS"], 1996, doi="10.1037//0022-006x.64.2.295"))
        self.assertNoVerdict(rec)

    def test_pubmed_without_a_doi_does_not_fire_verdict_one(self):
        # Verdict 1 must stay silent so verdict 2 can speak; asserting a
        # mismatch from a missing field would be a fabricated finding.
        rec = self.fx.record("nodoi", {
            "title": "A Study of Things", "authors": ["Smith, A"], "year": 2001,
            "doi": "10.1/a", "pmid": "999"})
        self.fx.cache_put("crossref", "10.1/a",
                          crossref_payload("A Study of Things", ["Smith"], 2001))
        self.fx.cache_put("pubmed", "999", pubmed_payload(
            "A Study of Things.", ["Smith A"], 2001, doi=None))
        verdicts, _ = self.verdicts_for(rec)
        self.assertNotIn("doi_pmid_mismatch", [v.kind for v in verdicts])

    def test_doi_read_from_elocationid_when_articleids_lacks_one(self):
        rec = self.fx.record("eloc", {
            "title": "A Study of Things", "authors": ["Smith, A"], "year": 2001,
            "doi": "10.1234/wrong", "pmid": "999"})
        self.fx.cache_put("crossref", "10.1234/wrong",
                          crossref_payload("A Study of Things", ["Smith"], 2001))
        self.fx.cache_put("pubmed", "999", pubmed_payload(
            "A Study of Things.", ["Smith A"], 2001, doi=None,
            elocationid="doi: 10.1234/right"))
        self.assertVerdict(rec, "doi_pmid_mismatch")


# --------------------------------------------------------------------------
# verdict 2 -- both identifiers resolve, to different works


class TestCrossviewMismatch(FixtureCase):

    def _craig(self):
        # The real Craig case: doi is Nature front matter, pmid is a French
        # history-of-pharmacy article, and PubMed serves no DOI, so only
        # verdict 2 can see it.
        rec = self.fx.record("craig2003", {
            "title": "Interoception: the sense of the physiological condition "
                     "of the body.",
            "authors": ["Craig, A D"], "year": 2003,
            "venue": "Nature Reviews Neuroscience",
            "doi": "10.1038/nrn1153", "pmid": "12894801"})
        self.fx.cache_put("crossref", "10.1038/nrn1153",
                          crossref_payload("In This Issue", [], 2003))
        self.fx.cache_put("pubmed", "12894801", pubmed_payload(
            "[The Boulducs' dynasty, apothecaries in Paris].",
            ["Warolin C"], 2003, doi=None))
        return rec

    def test_crossview_fires_when_pubmed_serves_no_doi(self):
        verdict = self.assertVerdict(self._craig(), "crossview_title_mismatch")
        self.assertIn("In This Issue", verdict.detail)

    def test_crossview_silent_on_subtitle_truncation(self):
        # REGRESSION TEST for the live false positive: Crossref's main-title-only
        # record vs PubMed's full title, for the SAME work.
        rec = self.fx.record("eastwood2012", {
            "title": "The Unengaged Mind: Defining Boredom in Terms of Attention",
            "authors": ["Eastwood, John D."], "year": 2012,
            "doi": "10.1177/1745691612456044", "pmid": "26168505"})
        self.fx.cache_put("crossref", "10.1177/1745691612456044",
                          crossref_payload("The Unengaged Mind",
                                           ["Eastwood"], 2012))
        self.fx.cache_put("pubmed", "26168505", pubmed_payload(
            "The Unengaged Mind: Defining Boredom in Terms of Attention.",
            ["Eastwood JD"], 2012, doi=None))
        self.assertNoVerdict(rec)

    def test_crossview_silent_when_one_side_has_no_title(self):
        rec = self.fx.record("notitle", {
            "title": "A Study of Things", "authors": ["Smith, A"], "year": 2001,
            "doi": "10.1/a", "pmid": "999"})
        self.fx.cache_put("crossref", "10.1/a",
                          crossref_payload("", ["Smith"], 2001))
        self.fx.cache_put("pubmed", "999", pubmed_payload(
            "A Study of Things.", ["Smith A"], 2001, doi=None))
        self.assertNoVerdict(rec)


# --------------------------------------------------------------------------
# verdict 3 -- one identifier, and it names a different paper


class TestDeclaredVsIdentifier(FixtureCase):

    def test_near_miss_doi_fires(self):
        # The dominant defect class, in its canonical instance.
        rec = self.fx.record("engel2010", {
            "title": "Beta-band oscillations -- signalling the status quo?",
            "authors": ["Engel, Andreas K.", "Fries, Pascal"], "year": 2010,
            "doi": "10.1016/j.conb.2010.02.014"})
        self.fx.cache_put("crossref", "10.1016/j.conb.2010.02.014",
                          crossref_payload(
                              "Neuronal oscillations and visual amplification "
                              "of speech", ["Schroeder"], 2010))
        verdict = self.assertVerdict(rec, "identifier_names_a_different_paper")
        self.assertIn("Schroeder", verdict.detail)

    def test_subtitle_truncation_alone_does_not_fire(self):
        # NEGATIVE CONTROL 1 of 3 for the conjunction: title disagrees on the
        # ratio, author agrees -> no verdict.
        rec = self.fx.record("caspi2014", {
            "title": "The p Factor: One General Psychopathology Factor in the "
                     "Structure of Psychiatric Disorders?",
            "authors": ["Caspi, Avshalom"], "year": 2014, "doi": "10.1/p"})
        self.fx.cache_put("crossref", "10.1/p",
                          crossref_payload("The p Factor", ["Caspi"], 2014))
        self.assertNoVerdict(rec)

    def test_author_name_change_alone_does_not_fire(self):
        # NEGATIVE CONTROL 2 of 3, and the one no name normalisation can reach:
        # 'Benthem SD' and 'Sarah D. Cushing' are the same person. The TITLE is
        # verbatim correct, which is what saves it.
        rec = self.fx.record("benthem2020", {
            "title": "Impaired hippocampal-cortical interactions during sleep "
                     "in a mouse model of Alzheimer's disease",
            "authors": ["Benthem SD"], "year": 2020, "doi": "10.1/b"})
        self.fx.cache_put("crossref", "10.1/b", crossref_payload(
            "Impaired hippocampal-cortical interactions during sleep in a mouse "
            "model of Alzheimer's disease", ["Cushing"], 2020))
        self.assertNoVerdict(rec)

    def test_preprint_author_order_alone_does_not_fire(self):
        # NEGATIVE CONTROL 3 of 3: CURL is Srinivas-first on arXiv and
        # Laskin-first at ICML (equal contribution).
        rec = self.fx.record("laskin2020", {
            "title": "CURL: Contrastive Unsupervised Representations for "
                     "Reinforcement Learning",
            "authors": ["Laskin, Michael", "Srinivas, Aravind"], "year": 2020,
            "doi": "10.1/curl"})
        self.fx.cache_put("crossref", "10.1/curl", crossref_payload(
            "CURL: Contrastive Unsupervised Representations for Reinforcement "
            "Learning", ["Srinivas", "Laskin"], 2020))
        self.assertNoVerdict(rec)

    def test_year_mismatch_alone_does_not_fire(self):
        # The audit's bucket (a) is 30 records and almost all legitimate
        # (preprint year vs published year, online-first vs print issue). This
        # checker must not touch them: year is not one of its axes at all.
        rec = self.fx.record("barrett2017", {
            "title": "The theory of constructed emotion",
            "authors": ["Barrett, Lisa Feldman"], "year": 2017,
            "doi": "10.1/tce"})
        self.fx.cache_put("crossref", "10.1/tce", crossref_payload(
            "The theory of constructed emotion", ["Barrett"], 2016))
        self.assertNoVerdict(rec)

    def test_falls_back_to_pmid_when_doi_is_unresolvable(self):
        rec = self.fx.record("pmidonly", {
            "title": "A Study of Things", "authors": ["Smith, A"], "year": 2001,
            "doi": "10.1/gone", "pmid": "999"})
        self.fx.cache_put("crossref", "10.1/gone",
                          {"ok": False, "error": "http_404"})
        self.fx.cache_put("doiorg", "10.1/gone",
                          {"ok": False, "error": "http_404"})
        self.fx.cache_put("pubmed", "999", pubmed_payload(
            "Something Else Entirely.", ["Jones B"], 2001, doi=None))
        self.assertVerdict(rec, "identifier_names_a_different_paper")

    def test_arxiv_doi_resolved_via_doiorg(self):
        # Crossref 404s on a DataCite DOI. Treating that as a finding would
        # flag every arXiv preprint in the corpus.
        rec = self.fx.record("arxiv", {
            "title": "Learning Latent Dynamics for Planning from Pixels",
            "authors": ["Hafner, Danijar"], "year": 2018,
            "doi": "10.48550/arXiv.1811.04551"})
        self.fx.cache_put("crossref", "10.48550/arxiv.1811.04551",
                          {"ok": False, "error": "http_404"})
        self.fx.cache_put("doiorg", "10.48550/arxiv.1811.04551", {
            "ok": True, "message": {
                "title": "Learning Latent Dynamics for Planning from Pixels",
                "author": [{"family": "Hafner"}],
                "issued": {"date-parts": [[2018]]},
                "container-title": "arXiv", "type": "article"}})
        self.assertNoVerdict(rec)


# --------------------------------------------------------------------------
# the fail-open contract


class TestFailsOpen(FixtureCase):

    def test_unresolvable_identifier_fails_open(self):
        # 11 records in the corpus legitimately carry an unresolvable
        # identifier (ACM handles, pre-1997 articles Crossref never indexed).
        rec = self.fx.record("gone", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 1990, "doi": "10.5555/999999"})
        self.fx.cache_put("crossref", "10.5555/999999",
                          {"ok": False, "error": "http_404"})
        self.fx.cache_put("doiorg", "10.5555/999999",
                          {"ok": False, "error": "http_404"})
        self.assertNoVerdict(rec)

    def test_record_without_declared_authors_fails_open(self):
        rec = self.fx.record("noauthors", {
            "title": "A Study of Things", "authors": [], "year": 2001,
            "doi": "10.1/a"})
        self.fx.cache_put("crossref", "10.1/a",
                          crossref_payload("Something Else", ["Jones"], 2001))
        self.assertNoVerdict(rec)

    def test_record_without_declared_title_fails_open(self):
        rec = self.fx.record("notitle2", {
            "title": "", "authors": ["Smith, A"], "year": 2001, "doi": "10.1/a"})
        self.fx.cache_put("crossref", "10.1/a",
                          crossref_payload("Something Else", ["Jones"], 2001))
        self.assertNoVerdict(rec)

    def test_offline_fails_open_and_names_what_it_skipped(self):
        # Nothing cached at all: the resolver must pass AND report, so a silent
        # cap is impossible (CLAUDE.md, "No silent caps").
        rec = self.fx.record("uncached", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/never-fetched"})
        verdicts, resolver = self.verdicts_for(rec)
        self.assertEqual([], verdicts)
        self.assertTrue(resolver.skipped)
        self.assertTrue(any(why == "offline" for _, why in resolver.skipped))

    def test_network_budget_spent_fails_open_and_names_it(self):
        rec = self.fx.record("budget", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/never-fetched"})
        verdicts, resolver = self.verdicts_for(rec, offline=False, budget=0)
        self.assertEqual([], verdicts)
        self.assertTrue(any(why == "network budget spent"
                            for _, why in resolver.skipped))

    def test_unparseable_record_is_not_this_tools_finding(self):
        entry = self.fx.lit / "targeted_review_x" / "entries" / "broken"
        entry.mkdir(parents=True)
        (entry / "record.json").write_text("{not json", encoding="utf-8")
        self.assertEqual([], V.collect_scoped_targets([str(entry / "record.json")]))

    def test_record_with_no_identifier_is_not_a_target(self):
        rec = self.fx.record("noident", {
            "title": "A Study of Things", "authors": ["Smith, A"], "year": 2001})
        self.assertEqual([], V.collect_scoped_targets([str(rec)]))


# --------------------------------------------------------------------------
# scoping -- the gate must never widen to the whole corpus


class TestScoping(FixtureCase):

    def test_summary_path_resolves_to_its_record(self):
        # A staged summary.md must pull in its own record, the same way
        # validate_literature.resolve_scope_paths does.
        rec = self.fx.record("entry1", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a"})
        targets = V.collect_scoped_targets([str(rec.parent / "summary.md")])
        self.assertEqual([str(rec)], [str(t["path"]) for t in targets])

    def test_relative_paths_resolve_against_the_repo(self):
        rec = self.fx.record("entry2", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a"})
        rel = str(rec.relative_to(self.fx.repo))
        self.assertEqual([str(rec)],
                         [str(t["path"]) for t in V.collect_scoped_targets([rel])])

    def test_empty_scope_is_a_noop_not_a_whole_corpus_scan(self):
        # Getting this backwards would make an unrelated commit resolve and
        # check all 2072 records. Asserting on the TARGET LIST rather than the
        # printed output, because the no-op has to happen before any resolving.
        self.fx.record("entry3", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a"})
        self.assertEqual([], V.collect_scoped_targets([]))
        self.assertEqual([], V.collect_scoped_targets(
            [str(self.fx.repo / "docs" / "unrelated.md")]))

    def test_nonexistent_path_is_skipped_not_an_error(self):
        # A staged DELETION resolves to a record.json that is gone.
        self.assertEqual([], V.collect_scoped_targets(
            [str(self.fx.lit / "t" / "entries" / "gone" / "record.json")]))

    def test_duplicate_paths_yield_one_target(self):
        rec = self.fx.record("entry4", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a"})
        targets = V.collect_scoped_targets(
            [str(rec), str(rec), str(rec.parent / "summary.md")])
        self.assertEqual(1, len(targets))


# --------------------------------------------------------------------------
# waivers


class TestWaivers(FixtureCase):

    def test_waiver_downgrades_but_still_reports(self):
        # A waived finding must not vanish -- it stops BLOCKING, it does not
        # stop being visible.
        entry = "2026-03-29_arc_032_frontal_theta_hippocampus_reward_hyman2010"
        rec = self.fx.record(entry, {
            "title": "Frontal theta and hippocampal reward coding",
            "authors": ["Hyman, James M."], "year": 2010,
            "doi": "10.1002/hipo.20709"})
        self.fx.cache_put("crossref", "10.1002/hipo.20709", crossref_payload(
            "Exercising some control over the hippocampus", ["Christie"], 2009))
        verdicts, _ = self.verdicts_for(rec)
        self.assertEqual(1, len(verdicts))
        self.assertTrue(verdicts[0].kind.startswith("waived:"))
        self.assertIn("GFLAG-0029", verdicts[0].detail)

    def test_waiver_does_not_cover_a_different_identifier_value(self):
        # THE POINT OF KEYING ON THE VALUE: a NEW wrong identifier written into
        # a waived record still blocks. A path-keyed waiver would absorb it.
        entry = "2026-03-29_arc_032_frontal_theta_hippocampus_reward_hyman2010"
        rec = self.fx.record(entry, {
            "title": "Frontal theta and hippocampal reward coding",
            "authors": ["Hyman, James M."], "year": 2010,
            "doi": "10.1002/hipo.99999"})
        self.fx.cache_put("crossref", "10.1002/hipo.99999", crossref_payload(
            "Something Completely Different", ["Nobody"], 2009))
        verdicts, _ = self.verdicts_for(rec)
        self.assertEqual(["identifier_names_a_different_paper"],
                         [v.kind for v in verdicts])

    def test_every_waiver_states_a_reason(self):
        self.assertTrue(V.WAIVERS)
        for waiver in V.WAIVERS:
            self.assertTrue(waiver.get("entry"))
            self.assertTrue(waiver.get("reason"))
            self.assertTrue(waiver.get("doi") or waiver.get("pmid"),
                            "waiver must be keyed on an identifier VALUE, not "
                            "on the entry alone: %r" % waiver)

    def test_placeholder_is_deliberately_not_waived(self):
        # The habenula record (GFLAG-0031) must keep blocking. If someone
        # waives it, this fails and they have to say why here.
        for waiver in V.WAIVERS:
            self.assertFalse(V.is_placeholder_doi(waiver.get("doi")),
                             "a placeholder DOI must not be waived: %r" % waiver)


# --------------------------------------------------------------------------
# CLI


class TestCli(FixtureCase):

    def _run(self, argv):
        import io
        import contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = V.main(argv)
        return rc, buf.getvalue()

    def test_gate_exit_nonzero_only_on_a_live_verdict(self):
        good = self.fx.record("good", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a"})
        self.fx.cache_put("crossref", "10.1/a",
                          crossref_payload("A Study of Things", ["Smith"], 2001))
        rc, out = self._run(["--repo", str(self.fx.repo), "--cache",
                             str(self.fx.cache), "--offline", "--exit-nonzero",
                             "--paths", str(good)])
        self.assertEqual(0, rc)
        self.assertIn("OK", out)

        bad = self.fx.record("bad", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/b"})
        self.fx.cache_put("crossref", "10.1/b",
                          crossref_payload("Something Else", ["Jones"], 2001))
        rc, out = self._run(["--repo", str(self.fx.repo), "--cache",
                             str(self.fx.cache), "--offline", "--exit-nonzero",
                             "--paths", str(bad)])
        self.assertEqual(1, rc)
        self.assertIn("identifier_names_a_different_paper", out)

    def test_gate_without_exit_nonzero_chains_safely(self):
        bad = self.fx.record("bad2", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/b"})
        self.fx.cache_put("crossref", "10.1/b",
                          crossref_payload("Something Else", ["Jones"], 2001))
        rc, _ = self._run(["--repo", str(self.fx.repo), "--cache",
                           str(self.fx.cache), "--offline",
                           "--paths", str(bad)])
        self.assertEqual(0, rc)

    def test_repo_override_moves_the_corpus_scan_too(self):
        # set_repo must move audit.LIT_ROOT as well, or --cross-check would
        # silently scan the real checkout while reporting fixture paths.
        self.fx.record("x", {"title": "T", "authors": ["A"], "year": 2001,
                             "doi": "10.1/a", "pmid": "1"})
        V.set_repo(self.fx.repo)
        self.assertEqual(self.fx.repo / "evidence" / "literature",
                         audit.LIT_ROOT)
        self.assertEqual(1, len(V.collect_all_targets()))

    def test_env_var_supplies_the_cache_and_offline_defaults(self):
        bad = self.fx.record("bad3", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/b"})
        self.fx.cache_put("crossref", "10.1/b",
                          crossref_payload("Something Else", ["Jones"], 2001))
        old = (os.environ.get("REE_LIT_BIB_CACHE"),
               os.environ.get("REE_LIT_BIB_OFFLINE"))
        os.environ["REE_LIT_BIB_CACHE"] = str(self.fx.cache)
        os.environ["REE_LIT_BIB_OFFLINE"] = "1"
        try:
            rc, out = self._run(["--repo", str(self.fx.repo), "--exit-nonzero",
                                 "--paths", str(bad)])
        finally:
            for key, value in zip(("REE_LIT_BIB_CACHE", "REE_LIT_BIB_OFFLINE"),
                                  old):
                if value is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = value
        self.assertEqual(1, rc)
        self.assertIn("identifier_names_a_different_paper", out)

    def test_no_mode_is_an_error_not_a_silent_pass(self):
        with self.assertRaises(SystemExit):
            V.main(["--repo", str(self.fx.repo)])


# --------------------------------------------------------------------------
# commit-gate wiring
#
# These EXECUTE precommit_literature.sh against a real git repo with real staged
# content, rather than asserting on its source text. A test that greps the script
# passes when the script is wired to a renamed flag, a moved path, or a python
# that is not there -- which is exactly the class of silent breakage every gate in
# this repo is `[ -f ]`-gated into.


class TestPrecommitWiring(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.script = REPO_ROOT / "scripts" / "precommit_literature.sh"
        if not cls.script.exists():
            raise unittest.SkipTest("precommit_literature.sh not present")
        if shutil.which("git") is None:
            raise unittest.SkipTest("git not available")

    def setUp(self):
        self.fx = Fixture()
        self.addCleanup(self.fx.close)
        # A minimal REE_assembly-shaped git repo: the three scripts the gate
        # needs, plus the real schema, so stage 1 is genuinely exercised.
        (self.fx.repo / "scripts").mkdir(parents=True, exist_ok=True)
        for name in ("validate_literature.py",
                     "verify_literature_identifiers.py",
                     "audit_literature_bibliographic_accuracy.py"):
            shutil.copy2(REPO_ROOT / "scripts" / name,
                         self.fx.repo / "scripts" / name)
        schema_rel = Path("evidence/literature/schemas/v1/"
                          "literature_evidence.schema.json")
        (self.fx.repo / schema_rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO_ROOT / schema_rel, self.fx.repo / schema_rel)
        for cmd in (["init", "-q"],
                    ["config", "user.email", "t@example.com"],
                    ["config", "user.name", "t"]):
            subprocess.run(["git"] + cmd, cwd=self.fx.repo, check=True)

    def _stage_all(self):
        subprocess.run(["git", "add", "-A"], cwd=self.fx.repo, check=True)

    def _run_gate(self, **env_extra):
        env = dict(os.environ)
        env["REE_LIT_BIB_CACHE"] = str(self.fx.cache)
        env["REE_LIT_BIB_OFFLINE"] = "1"      # belt and braces: never the wire
        env.update(env_extra)
        return subprocess.run(
            ["bash", str(self.script)], cwd=self.fx.repo, env=env,
            capture_output=True, text=True, timeout=180)

    def test_clean_record_passes(self):
        self.fx.record("good", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a"})
        self.fx.cache_put("crossref", "10.1/a",
                          crossref_payload("A Study of Things", ["Smith"], 2001))
        self._stage_all()
        result = self._run_gate()
        self.assertEqual(0, result.returncode,
                         result.stdout + result.stderr)

    def test_wrong_identifier_blocks_with_exit_2(self):
        self.fx.record("bad", {
            "title": "Beta-band oscillations -- signalling the status quo?",
            "authors": ["Engel, Andreas K."], "year": 2010,
            "doi": "10.1016/j.conb.2010.02.014"})
        self.fx.cache_put("crossref", "10.1016/j.conb.2010.02.014",
                          crossref_payload("Neuronal oscillations and visual "
                                           "amplification of speech",
                                           ["Schroeder"], 2010))
        self._stage_all()
        result = self._run_gate()
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)
        self.assertIn("identifier_names_a_different_paper", result.stdout)
        self.assertIn("BLOCKING", result.stdout)

    def test_identifier_stage_can_be_made_report_only(self):
        self.fx.record("bad", {
            "title": "Beta-band oscillations -- signalling the status quo?",
            "authors": ["Engel, Andreas K."], "year": 2010,
            "doi": "10.1016/j.conb.2010.02.014"})
        self.fx.cache_put("crossref", "10.1016/j.conb.2010.02.014",
                          crossref_payload(
                              "Neuronal oscillations and visual "
                              "amplification of speech",
                              ["Schroeder"], 2010))
        self._stage_all()
        result = self._run_gate(REE_LITERATURE_IDENTIFIER_GATE_BLOCK="0")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("report-only", result.stdout)

    def test_identifier_stage_can_be_disabled_entirely(self):
        self.fx.record("bad", {
            "title": "Beta-band oscillations -- signalling the status quo?",
            "authors": ["Engel, Andreas K."], "year": 2010,
            "doi": "10.1016/j.conb.2010.02.014"})
        self.fx.cache_put("crossref", "10.1016/j.conb.2010.02.014",
                          crossref_payload(
                              "Neuronal oscillations and visual "
                              "amplification of speech",
                              ["Schroeder"], 2010))
        self._stage_all()
        result = self._run_gate(REE_LITERATURE_IDENTIFIER_GATE="0")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertNotIn("identifier_names_a_different_paper", result.stdout)

    def test_nothing_staged_under_literature_is_a_silent_pass(self):
        (self.fx.repo / "unrelated.txt").write_text("hello\n", encoding="utf-8")
        self._stage_all()
        result = self._run_gate()
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual("", result.stdout.strip())

    def test_an_unstaged_bad_record_does_not_block(self):
        # Scoping, end to end: the gate checks what the COMMIT touches. A bad
        # record already in the tree but not staged must not block an unrelated
        # commit -- this is what stops a corpus backlog wedging the fleet.
        self.fx.record("bad", {
            "title": "Beta-band oscillations -- signalling the status quo?",
            "authors": ["Engel, Andreas K."], "year": 2010,
            "doi": "10.1016/j.conb.2010.02.014"})
        self.fx.cache_put("crossref", "10.1016/j.conb.2010.02.014",
                          crossref_payload(
                              "Neuronal oscillations and visual "
                              "amplification of speech",
                              ["Schroeder"], 2010))
        (self.fx.repo / "unrelated.txt").write_text("hello\n", encoding="utf-8")
        subprocess.run(["git", "add", "unrelated.txt"], cwd=self.fx.repo,
                       check=True)
        result = self._run_gate()
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_a_staged_summary_pulls_in_its_own_record(self):
        # The deletion/edit case validate_literature's --paths resolution exists
        # for: only summary.md is staged, and the record it belongs to is bad.
        rec = self.fx.record("bad", {
            "title": "Beta-band oscillations -- signalling the status quo?",
            "authors": ["Engel, Andreas K."], "year": 2010,
            "doi": "10.1016/j.conb.2010.02.014"})
        self.fx.cache_put("crossref", "10.1016/j.conb.2010.02.014",
                          crossref_payload(
                              "Neuronal oscillations and visual "
                              "amplification of speech",
                              ["Schroeder"], 2010))
        self._stage_all()
        subprocess.run(["git", "commit", "-q", "-m", "base", "--no-verify"],
                       cwd=self.fx.repo, check=True)
        (rec.parent / "summary.md").write_text("# Summary\n\nedited\n",
                                               encoding="utf-8")
        subprocess.run(["git", "add", str(rec.parent / "summary.md")],
                       cwd=self.fx.repo, check=True)
        result = self._run_gate()
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)

    def test_missing_identifier_checker_skips_rather_than_errors(self):
        # Every gate in this repo is `[ -f ]`-gated and must degrade to no
        # check, never to a broken commit path.
        (self.fx.repo / "scripts" / "verify_literature_identifiers.py").unlink()
        self.fx.record("good", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a"})
        self._stage_all()
        result = self._run_gate()
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("SKIPPED", result.stderr)


# --------------------------------------------------------------------------
# the DOI -> PMID crosswalk (esearch `<doi>[AID]`)
#
# The dominant risk here is the OPPOSITE of the rest of this file. Every other
# check starts from an identifier that resolves; this one starts from a question
# PubMed usually answers "I have no such record" -- 1579 DOI-only records, of
# which arXiv preprints, ML-conference papers, book chapters and monographs are
# legitimately absent from PubMed entirely. Reading an empty esearch result as a
# finding would flag hundreds of CORRECT records, so `not_in_pubmed` being a
# silent, ordinary pass is the single most load-bearing assertion below.


def esearch_payload(idlist, translated=True, count=None, doi="10.1/a",
                    phrase=None):
    """An esearch response in the shape Resolver.pmids_for_doi reads.

    ``translated`` models the observed hit/miss signal: PubMed rewrites a DOI it
    indexes into a `"..."[Publisher ID]` phrase query, and leaves a DOI it does
    not index as the raw `<doi>[AID]` term.

    The phrase is DERIVED from the DOI by default, using the module's own
    tokeniser rather than a hardcoded string, so a fixture cannot accidentally
    encode a truncated query and pass the fidelity check by luck. ``phrase``
    overrides it, which is how the truncation cases below are built.
    """
    ids = [str(i) for i in idlist]
    body = " ".join(V._id_tokens(doi)) if phrase is None else phrase
    return {"ok": True, "message": {
        "count": str(len(ids) if count is None else count),
        "idlist": ids,
        "querytranslation": ('"%s"%s' % (body, V.AID_TRANSLATION_MARKER)
                             if translated else "%s[AID]" % doi),
    }}


class TestAidQueryFidelity(unittest.TestCase):
    """PubMed sometimes searches only a FRAGMENT of the DOI it was given."""

    def test_the_whole_doi_is_faithful(self):
        self.assertTrue(V.aid_query_is_faithful(
            '"10 1523 jneurosci 4718 06 2007"[Publisher ID]',
            "10.1523/JNEUROSCI.4718-06.2007"))

    def test_the_legacy_apa_double_slash_is_still_faithful(self):
        # Slash runs vanish under tokenisation, so this must not read as drift.
        self.assertTrue(V.aid_query_is_faithful(
            '"10 1037 0022 006x 64 2 295"[Publisher ID]',
            "10.1037//0022-006x.64.2.295"))

    def test_a_single_trailing_fragment_is_refused(self):
        # The live corpus case that would otherwise have produced a fabricated
        # mapping: 10.2307/1130099 was searched as just "1130099", which matched
        # exactly one unrelated 2023 paper.
        self.assertFalse(V.aid_query_is_faithful(
            '"1130099"[Publisher ID]', "10.2307/1130099"))
        self.assertFalse(V.aid_query_is_faithful(
            '"3"[Publisher ID]', "10.1207/s15516709cog1401_3"))
        self.assertFalse(V.aid_query_is_faithful(
            '"454"[Publisher ID]', "10.24963/ijcai.2023/454"))

    def test_an_untranslated_term_is_refused(self):
        self.assertFalse(V.aid_query_is_faithful(
            "10.48550/arXiv.2004.04136[AID]", "10.48550/arXiv.2004.04136"))

    def test_a_superset_phrase_is_refused_too(self):
        # The other direction of the phrase-containment trap.
        self.assertFalse(V.aid_query_is_faithful(
            '"10 1016 j conb 2010 02 014 suppl"[Publisher ID]',
            "10.1016/j.conb.2010.02.014"))


class TestAidCacheKey(unittest.TestCase):

    def test_key_is_lower_cased(self):
        self.assertEqual("10.1234/abcx", V.aid_cache_key("10.1234/ABCX"))

    def test_key_is_not_the_comparison_form(self):
        # normalise_doi collapses slash runs, which is right for COMPARING two
        # DOIs and wrong for a cache key: the legacy APA double-slash form is a
        # different string on the wire, so it must get its own cache entry
        # rather than being served the single-slash form's answer.
        self.assertEqual("10.1037//0022-006x.64.2.295",
                         V.aid_cache_key("10.1037//0022-006x.64.2.295"))
        self.assertNotEqual(V.aid_cache_key("10.1037//0022-006x.64.2.295"),
                            V.normalise_doi("10.1037//0022-006x.64.2.295"))


class TestPmidsForDoi(FixtureCase):

    def test_a_translated_hit_is_a_mapping(self):
        resolver = self.fx.resolver()
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.1/a",
                          esearch_payload(["17626209"]))
        self.assertEqual((["17626209"], "ok"), resolver.pmids_for_doi("10.1/a"))

    def test_empty_result_is_not_in_pubmed_not_a_failure(self):
        # THE COMMON CASE. Distinguishing this from "could not ask" is what
        # keeps the sweep from flagging every arXiv preprint in the corpus.
        resolver = self.fx.resolver()
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.48550/arxiv.2004.04136",
                          esearch_payload([], translated=False))
        self.assertEqual(([], "not_in_pubmed"),
                         resolver.pmids_for_doi("10.48550/arXiv.2004.04136"))

    def test_hits_from_an_untranslated_query_are_refused(self):
        # NEGATIVE CONTROL: ids from a term PubMed did not read as an identifier
        # lookup are free-text hits, not a crosswalk, and must not be trusted.
        resolver = self.fx.resolver()
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.1/a",
                          esearch_payload(["1", "2"], translated=False))
        self.assertEqual((None, "untranslated_query"),
                         resolver.pmids_for_doi("10.1/a"))

    def test_a_truncated_query_is_refused_even_with_one_hit(self):
        # THE dangerous shape, live in this corpus: PubMed searched only
        # "1130099" and returned exactly one PMID, for an unrelated paper. Count
        # is 1, the marker is present, and the mapping is still fabricated.
        resolver = self.fx.resolver()
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.2307/1130099",
                          esearch_payload(["36860389"], phrase="1130099"))
        self.assertEqual((None, "truncated_query"),
                         resolver.pmids_for_doi("10.2307/1130099"))

    def test_offline_and_uncached_fails_open_and_is_named(self):
        resolver = self.fx.resolver()
        self.assertEqual((None, "unfetched"), resolver.pmids_for_doi("10.1/never"))
        self.assertTrue(any(why == "offline" for _, why in resolver.skipped))

    def test_budget_spent_fails_open_and_is_named(self):
        resolver = self.fx.resolver(offline=False, budget=0)
        self.assertEqual((None, "unfetched"), resolver.pmids_for_doi("10.1/never"))
        self.assertTrue(any(why == "network budget spent"
                            for _, why in resolver.skipped))

    def test_cache_key_is_case_insensitive_end_to_end(self):
        # arXiv DOIs carry an uppercase X; a case-sensitive key would miss the
        # cache and re-fetch every time. Same bug class the crossref key had.
        resolver = self.fx.resolver()
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.48550/arxiv.1",
                          esearch_payload(["7"], doi="10.48550/arXiv.1"))
        self.assertEqual((["7"], "ok"),
                         resolver.pmids_for_doi("10.48550/arXiv.1"))


class TestFetchPubmedAidCaching(unittest.TestCase):
    """The one deviation from the audit's fetchers: failures are NOT cached."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="lit_aid_test_"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self._http_get = audit.http_get
        self.addCleanup(setattr, audit, "http_get", self._http_get)

    def test_a_success_is_cached(self):
        audit.http_get = lambda url, timeout=30: json.dumps(
            {"esearchresult": {"count": "1", "idlist": ["42"],
                               "querytranslation": '"x"[Publisher ID]'}})
        payload = V.fetch_pubmed_aid("10.1/a", self.tmp, audit.RateLimiter(1000))
        self.assertTrue(payload["ok"])
        self.assertTrue(audit.cache_path(self.tmp, V.PUBMED_AID_CACHE_KIND,
                                         "10.1/a").exists())

    def test_an_empty_result_IS_cached_because_it_is_an_answer(self):
        audit.http_get = lambda url, timeout=30: json.dumps(
            {"esearchresult": {"count": "0", "idlist": [],
                               "querytranslation": "10.1/b[AID]"}})
        V.fetch_pubmed_aid("10.1/b", self.tmp, audit.RateLimiter(1000))
        self.assertTrue(audit.cache_path(self.tmp, V.PUBMED_AID_CACHE_KIND,
                                         "10.1/b").exists())

    def test_a_transport_failure_is_NOT_cached(self):
        # An HTTP 429 from NCBI's rate limiter persisted as a cache entry would
        # remove that record from every future sweep, indistinguishably from a
        # real miss. The audit's fetchers cache failures; this one must not.
        def boom(url, timeout=30):
            raise urllib.error.URLError("connection reset")
        audit.http_get = boom
        payload = V.fetch_pubmed_aid("10.1/c", self.tmp, audit.RateLimiter(1000))
        self.assertFalse(payload["ok"])
        self.assertFalse(audit.cache_path(self.tmp, V.PUBMED_AID_CACHE_KIND,
                                          "10.1/c").exists())

    def test_an_http_error_is_NOT_cached_either(self):
        def boom(url, timeout=30):
            raise urllib.error.HTTPError(url, 429, "Too Many Requests", {}, None)
        audit.http_get = boom
        payload = V.fetch_pubmed_aid("10.1/d", self.tmp, audit.RateLimiter(1000))
        self.assertEqual("http_429", payload["error"])
        self.assertFalse(audit.cache_path(self.tmp, V.PUBMED_AID_CACHE_KIND,
                                          "10.1/d").exists())


class TestPubmedHoldsDoi(unittest.TestCase):

    def test_matching_articleids_confirms(self):
        rec = pubmed_payload("T", ["A"], 2001, doi="10.1/a")["message"]
        self.assertIs(True, V.pubmed_holds_doi(rec, "10.1/a"))

    def test_a_different_doi_refuses(self):
        # The phrase-prefix trap: `[AID]` is a tokenised phrase search, so a
        # query can be contained by a LONGER Publisher ID. The round trip is
        # what rules that out.
        rec = pubmed_payload("T", ["A"], 2001,
                             doi="10.1016/j.conb.2010.02.014.suppl")["message"]
        self.assertIs(False, V.pubmed_holds_doi(rec, "10.1016/j.conb.2010.02.014"))

    def test_no_doi_at_all_is_unconfirmable_not_a_contradiction(self):
        rec = pubmed_payload("T", ["A"], 2001, doi=None)["message"]
        self.assertIsNone(V.pubmed_holds_doi(rec, "10.1/a"))

    def test_legacy_apa_double_slash_still_confirms(self):
        rec = pubmed_payload("T", ["A"], 1996,
                             doi="10.1037//0022-006x.64.2.295")["message"]
        self.assertIs(True, V.pubmed_holds_doi(rec, "10.1037/0022-006x.64.2.295"))


class TestCrosswalkDoi(FixtureCase):

    def _crosswalk(self, record_path, **resolver_kwargs):
        target = V.collect_scoped_targets([str(record_path)])[0]
        return V.crosswalk_doi(target, self.fx.resolver(**resolver_kwargs))

    def test_a_different_paper_is_a_finding(self):
        # The shape this check exists for: a DOI-only record whose DOI PubMed
        # maps to a paper the record does not describe. Verdict 1 and 2 cannot
        # see it -- there is no PMID in the record to cross-resolve against.
        rec = self.fx.record("engel2010", {
            "title": "Beta-band oscillations -- signalling the status quo?",
            "authors": ["Engel, Andreas K."], "year": 2010,
            "doi": "10.1016/j.conb.2010.02.014"})
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.1016/j.conb.2010.02.014",
                          esearch_payload(["20299205"], doi="10.1016/j.conb.2010.02.014"))
        self.fx.cache_put("pubmed", "20299205", pubmed_payload(
            "Neuronal oscillations and visual amplification of speech.",
            ["Schroeder CE"], 2010, doi="10.1016/j.conb.2010.02.014"))
        result = self._crosswalk(rec)
        self.assertEqual("names_a_different_paper", result["status"])
        self.assertEqual("20299205", result["pmid"])

        verdict = self.assertVerdictOfKind(
            rec, "doi_crosswalk_names_a_different_paper")
        self.assertIn("20299205", verdict.detail)

    def test_not_in_pubmed_is_silent(self):
        # THE COMMON CASE, and the assertion that stops this check flagging
        # hundreds of correct arXiv / ML-venue / book-chapter records.
        rec = self.fx.record("arxivrec", {
            "title": "Curl: Contrastive Unsupervised Representations",
            "authors": ["Srinivas, Aravind"], "year": 2020,
            "doi": "10.48550/arXiv.2004.04136"})
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.48550/arxiv.2004.04136",
                          esearch_payload([], translated=False))
        self.assertEqual("not_in_pubmed", self._crosswalk(rec)["status"])
        self.assertNoCrosswalkVerdict(rec)

    def test_subtitle_truncation_alone_does_not_fire(self):
        # NEGATIVE CONTROL, documented false-positive class 1: PubMed prepends
        # section headings and publishers register main titles only.
        rec = self.fx.record("subtitle", {
            "title": "The Unengaged Mind",
            "authors": ["Eastwood, John D."], "year": 2012,
            "doi": "10.1/a"})
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.1/a",
                          esearch_payload(["1"]))
        self.fx.cache_put("pubmed", "1", pubmed_payload(
            "The Unengaged Mind: Defining Boredom in Terms of Attention.",
            ["Eastwood JD"], 2012, doi="10.1/a"))
        self.assertEqual("agrees", self._crosswalk(rec)["status"])
        self.assertNoCrosswalkVerdict(rec)

    def test_author_name_change_alone_does_not_fire(self):
        # NEGATIVE CONTROL, documented false-positive class 3. The conjunction
        # is what makes this survivable -- the title is verbatim correct.
        rec = self.fx.record("namechange", {
            "title": "A Study of Things", "authors": ["Benthem, S D"],
            "year": 2020, "doi": "10.1/a"})
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.1/a",
                          esearch_payload(["1"]))
        self.fx.cache_put("pubmed", "1", pubmed_payload(
            "A Study of Things.", ["Cushing SD"], 2020, doi="10.1/a"))
        result = self._crosswalk(rec)
        self.assertEqual("agrees", result["status"])
        self.assertIs(False, result["author_ok"])
        self.assertNoCrosswalkVerdict(rec)

    def test_title_disagreement_alone_does_not_fire(self):
        rec = self.fx.record("titleonly", {
            "title": "Something Completely Different",
            "authors": ["Smith, A"], "year": 2001, "doi": "10.1/a"})
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.1/a",
                          esearch_payload(["1"]))
        self.fx.cache_put("pubmed", "1", pubmed_payload(
            "A Study of Things.", ["Smith A"], 2001, doi="10.1/a"))
        self.assertEqual("agrees", self._crosswalk(rec)["status"])
        self.assertNoCrosswalkVerdict(rec)

    def test_ambiguous_mapping_is_refused(self):
        # Two PubMed records for one DOI (a duplicate deposit, or a preprint and
        # its published version). Which one the record MEANT is exactly the
        # external judgement this tool refuses to make.
        rec = self.fx.record("ambig", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a"})
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.1/a",
                          esearch_payload(["1", "2"]))
        self.assertEqual("ambiguous", self._crosswalk(rec)["status"])
        self.assertNoCrosswalkVerdict(rec)

    def test_unconfirmed_mapping_is_refused(self):
        # The phrase-prefix trap end to end: esearch returns a PMID whose own
        # articleids name a LONGER DOI. Without the round trip this would be
        # read as a mapping and could produce a fabricated finding.
        rec = self.fx.record("prefix", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1016/j.conb.2010.02.014"})
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.1016/j.conb.2010.02.014",
                          esearch_payload(["1"], doi="10.1016/j.conb.2010.02.014"))
        self.fx.cache_put("pubmed", "1", pubmed_payload(
            "Some Other Paper Entirely.", ["Jones B"], 2010,
            doi="10.1016/j.conb.2010.02.014.suppl"))
        self.assertEqual("unconfirmed_mapping", self._crosswalk(rec)["status"])
        self.assertNoCrosswalkVerdict(rec)

    def test_pubmed_serving_no_doi_is_unconfirmed_not_a_finding(self):
        rec = self.fx.record("nodoiback", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a"})
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.1/a",
                          esearch_payload(["1"]))
        self.fx.cache_put("pubmed", "1", pubmed_payload(
            "Something Else Entirely.", ["Jones B"], 2001, doi=None))
        self.assertEqual("unconfirmed_mapping", self._crosswalk(rec)["status"])
        self.assertNoCrosswalkVerdict(rec)

    def test_placeholder_is_left_to_its_own_verdict(self):
        rec = self.fx.record("placeholder", {
            "title": "Midbrain dopamine and habenula interactions",
            "authors": ["Example Author A"], "year": 2024,
            "doi": "10.0000/example-doi"})
        self.assertEqual("placeholder", self._crosswalk(rec)["status"])

    def test_record_without_declared_fields_fails_open(self):
        rec = self.fx.record("nofields", {
            "title": "", "authors": [], "year": 2001, "doi": "10.1/a"})
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.1/a",
                          esearch_payload(["1"]))
        self.fx.cache_put("pubmed", "1", pubmed_payload(
            "Anything At All.", ["Jones B"], 2001, doi="10.1/a"))
        self.assertEqual("no_declared_fields", self._crosswalk(rec)["status"])
        self.assertNoCrosswalkVerdict(rec)

    def test_offline_fails_open(self):
        rec = self.fx.record("uncachedwalk", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/never"})
        self.assertEqual("unfetched", self._crosswalk(rec)["status"])
        self.assertNoCrosswalkVerdict(rec)

    def test_every_non_finding_status_is_declared(self):
        # A status the sweep does not know about would be printed as an unnamed
        # bucket, which is how a silent cap gets in (CLAUDE.md, "No silent caps").
        for status in ("not_in_pubmed", "ambiguous", "unconfirmed_mapping",
                       "no_declared_fields", "agrees", "placeholder",
                       "unfetched", "esearch_failed", "untranslated_query",
                       "pmid_unresolvable"):
            self.assertIn(status, V.CROSSWALK_NON_FINDING_STATUSES)

    # -- helpers -----------------------------------------------------------

    def assertVerdictOfKind(self, record_path, kind):
        target = V.collect_scoped_targets([str(record_path)])[0]
        verdict = V.check_doi_crosswalk(target, self.fx.resolver())
        self.assertIsNotNone(verdict, "expected %s, got nothing" % kind)
        self.assertEqual(kind, verdict.kind)
        return verdict

    def assertNoCrosswalkVerdict(self, record_path):
        target = V.collect_scoped_targets([str(record_path)])[0]
        verdict = V.check_doi_crosswalk(target, self.fx.resolver())
        self.assertIsNone(
            verdict, "expected no verdict, got: %s"
            % (verdict.detail if verdict else ""))


class TestCrosswalkIsNotOnTheGatePath(FixtureCase):
    """Staying off the gate is a MEASURED decision, not caution. Do not "fix" it.

    The obvious reading of this class is "the baseline has not been measured
    yet". It has been, over all 1579 DOI-only records (2026-08-14), and the
    verdict's whole-corpus baseline is 0 live findings -- clean enough to block.
    It stays off the gate for the OTHER measured reason: its marginal coverage
    over verdict 3 in this corpus is also zero. Every DOI that resolves through
    neither Crossref nor doi.org -- the blind spot the crosswalk would uniquely
    cover -- turns out to be absent from PubMed as well (10 of 10). So wiring it
    in would spend up to two extra network calls per record against a
    budget-bounded gate, buying nothing, and the budget it spent would come
    straight out of the coverage of the checks that do fire.

    That is a property of the corpus and not of the code. If a later pull adds a
    record whose DOI is unresolvable but IS indexed by PubMed, the arithmetic
    flips and this class should be revisited -- re-measure, do not assume.
    """

    def test_check_is_not_in_checks_networked(self):
        self.assertNotIn(V.check_doi_crosswalk, V.CHECKS_NETWORKED)

    def test_the_gate_stays_silent_on_a_crosswalk_only_defect(self):
        # Same record as test_a_different_paper_is_a_finding, but reached
        # through verify_target -- what the commit gate actually calls. The DOI
        # resolves NOWHERE except PubMed, so verdict 3 fails open and the gate
        # must report nothing at all.
        rec = self.fx.record("engel2010", {
            "title": "Beta-band oscillations -- signalling the status quo?",
            "authors": ["Engel, Andreas K."], "year": 2010,
            "doi": "10.1016/j.conb.2010.02.014"})
        self.fx.cache_put("crossref", "10.1016/j.conb.2010.02.014",
                          {"ok": False, "error": "http_404"})
        self.fx.cache_put("doiorg", "10.1016/j.conb.2010.02.014",
                          {"ok": False, "error": "http_404"})
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.1016/j.conb.2010.02.014",
                          esearch_payload(["20299205"], doi="10.1016/j.conb.2010.02.014"))
        self.fx.cache_put("pubmed", "20299205", pubmed_payload(
            "Neuronal oscillations and visual amplification of speech.",
            ["Schroeder CE"], 2010, doi="10.1016/j.conb.2010.02.014"))
        self.assertNoVerdict(rec)


class TestWritePmid(FixtureCase):
    """The backfill. Every test here is about what it REFUSES to do."""

    def _source(self, record_path):
        return json.loads(Path(record_path).read_text(encoding="utf-8"))["source"]

    def test_writes_the_pmid_after_the_doi(self):
        rec = self.fx.record("backfill", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a", "url": "https://example.org/x"})
        self.assertEqual("written", V.write_pmid_into_record(
            rec, "12345", "10.1/a", "a note"))
        source = self._source(rec)
        self.assertEqual("12345", source["pmid"])
        self.assertEqual(["title", "authors", "year", "doi", "pmid", "url"],
                         list(source))

    def test_pmid_is_written_as_a_string(self):
        # The v1 schema declares pmid as ["string", "null"]; an int would
        # validate-fail on the very next commit.
        rec = self.fx.record("stringy", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a"})
        V.write_pmid_into_record(rec, 12345, "10.1/a", "a note")
        self.assertEqual("12345", self._source(rec)["pmid"])

    def test_an_existing_pmid_is_never_overwritten(self):
        rec = self.fx.record("haspmid", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a", "pmid": "999"})
        self.assertEqual("already_has_pmid", V.write_pmid_into_record(
            rec, "12345", "10.1/a", "a note"))
        self.assertEqual("999", self._source(rec)["pmid"])

    def test_a_doi_that_changed_under_us_is_refused(self):
        # The sweep resolves from a snapshot; a concurrent session repairing the
        # DOI between the sweep and the write must not get a PMID for the OLD one.
        rec = self.fx.record("moved", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/new"})
        self.assertEqual("doi_changed_under_us", V.write_pmid_into_record(
            rec, "12345", "10.1/old", "a note"))
        self.assertNotIn("pmid", self._source(rec))

    def test_dry_run_writes_nothing(self):
        rec = self.fx.record("dry", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a"})
        self.assertEqual("would_write", V.write_pmid_into_record(
            rec, "12345", "10.1/a", "a note", dry_run=True))
        self.assertNotIn("pmid", self._source(rec))
        self.assertNotIn(V.PROVENANCE_NOTE_HEADING,
                         (rec.parent / "summary.md").read_text(encoding="utf-8"))

    def test_a_provenance_note_is_appended_to_the_summary(self):
        rec = self.fx.record("noted", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a"})
        V.write_pmid_into_record(rec, "12345", "10.1/a",
                                 "derived from the DOI on 2026-08-14")
        text = (rec.parent / "summary.md").read_text(encoding="utf-8")
        self.assertIn(V.PROVENANCE_NOTE_HEADING, text)
        self.assertIn("derived from the DOI on 2026-08-14", text)
        self.assertTrue(text.startswith("# Summary"))

    def test_no_evidence_field_is_touched(self):
        # Provenance only. The standing constraint on every literature repair.
        rec = self.fx.record("untouched", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a"})
        before = json.loads(Path(rec).read_text(encoding="utf-8"))
        V.write_pmid_into_record(rec, "12345", "10.1/a", "a note")
        after = json.loads(Path(rec).read_text(encoding="utf-8"))
        for key in ("confidence", "evidence_direction", "claim_ids_tested",
                    "evidence_class", "confidence_rationale"):
            self.assertEqual(before.get(key), after.get(key), key)
        self.assertEqual({"pmid"}, set(after["source"]) - set(before["source"]))


class TestCrosswalkCli(FixtureCase):

    def _run(self, argv):
        import io
        import contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = V.main(argv)
        return rc, buf.getvalue()

    def test_crosswalk_reports_buckets_and_chains_safely(self):
        self.fx.record("arxivrec", {
            "title": "A Preprint", "authors": ["Smith, A"], "year": 2020,
            "doi": "10.48550/arXiv.1"})
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.48550/arxiv.1",
                          esearch_payload([], translated=False))
        rc, out = self._run(["--repo", str(self.fx.repo), "--cache",
                             str(self.fx.cache), "--offline", "--progress", "0",
                             "--exit-nonzero", "--doi-crosswalk"])
        self.assertEqual(0, rc)
        self.assertIn("not_in_pubmed", out)

    def test_crosswalk_exit_nonzero_only_on_a_finding(self):
        self.fx.record("bad", {
            "title": "Beta-band oscillations -- signalling the status quo?",
            "authors": ["Engel, Andreas K."], "year": 2010,
            "doi": "10.1/a"})
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.1/a",
                          esearch_payload(["20299205"]))
        self.fx.cache_put("pubmed", "20299205", pubmed_payload(
            "Neuronal oscillations and visual amplification of speech.",
            ["Schroeder CE"], 2010, doi="10.1/a"))
        rc, out = self._run(["--repo", str(self.fx.repo), "--cache",
                             str(self.fx.cache), "--offline", "--progress", "0",
                             "--exit-nonzero", "--doi-crosswalk"])
        self.assertEqual(1, rc)
        self.assertIn("names_a_different_paper", out)

    def test_a_both_identifier_record_is_out_of_scope(self):
        # --cross-check already covers those conclusively; re-asking PubMed for
        # a DOI whose PMID is declared would spend calls to learn nothing.
        self.fx.record("both", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a", "pmid": "999"})
        _, out = self._run(["--repo", str(self.fx.repo), "--cache",
                            str(self.fx.cache), "--offline", "--progress", "0",
                            "--doi-crosswalk"])
        self.assertIn("DOI-only records (the scope)    : 0", out)

    def test_write_pmid_defaults_to_none(self):
        rec = self.fx.record("nowrite", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a"})
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.1/a",
                          esearch_payload(["1"]))
        self.fx.cache_put("pubmed", "1", pubmed_payload(
            "A Study of Things.", ["Smith A"], 2001, doi="10.1/a"))
        self._run(["--repo", str(self.fx.repo), "--cache", str(self.fx.cache),
                   "--offline", "--progress", "0", "--doi-crosswalk"])
        self.assertNotIn("pmid", json.loads(
            Path(rec).read_text(encoding="utf-8"))["source"])

    def test_write_pmid_all_backfills_a_confirmed_agreeing_record(self):
        rec = self.fx.record("dowrite", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a"})
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.1/a",
                          esearch_payload(["1"]))
        self.fx.cache_put("pubmed", "1", pubmed_payload(
            "A Study of Things.", ["Smith A"], 2001, doi="10.1/a"))
        self._run(["--repo", str(self.fx.repo), "--cache", str(self.fx.cache),
                   "--offline", "--progress", "0", "--doi-crosswalk",
                   "--write-pmid", "all"])
        self.assertEqual("1", json.loads(
            Path(rec).read_text(encoding="utf-8"))["source"]["pmid"])

    def test_write_pmid_never_writes_where_the_title_disagrees(self):
        # The record's DOI may itself be the wrong one; writing PubMed's PMID
        # for it would bury that defect behind a self-consistent-looking pair.
        rec = self.fx.record("wrongdoi", {
            "title": "Something Completely Different", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a"})
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.1/a",
                          esearch_payload(["1"]))
        self.fx.cache_put("pubmed", "1", pubmed_payload(
            "A Study of Things.", ["Smith A"], 2001, doi="10.1/a"))
        self._run(["--repo", str(self.fx.repo), "--cache", str(self.fx.cache),
                   "--offline", "--progress", "0", "--doi-crosswalk",
                   "--write-pmid", "all"])
        self.assertNotIn("pmid", json.loads(
            Path(rec).read_text(encoding="utf-8"))["source"])

    def test_write_pmid_unresolvable_skips_a_doi_crossref_already_resolves(self):
        # The narrow default: only a DOI that resolves NOWHERE else gains
        # anything from a backfill, because only that record is currently
        # unreachable by every networked verdict.
        rec = self.fx.record("resolvable", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a"})
        self.fx.cache_put("crossref", "10.1/a",
                          crossref_payload("A Study of Things", ["Smith"], 2001))
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.1/a",
                          esearch_payload(["1"]))
        self.fx.cache_put("pubmed", "1", pubmed_payload(
            "A Study of Things.", ["Smith A"], 2001, doi="10.1/a"))
        self._run(["--repo", str(self.fx.repo), "--cache", str(self.fx.cache),
                   "--offline", "--progress", "0", "--doi-crosswalk",
                   "--write-pmid", "unresolvable"])
        self.assertNotIn("pmid", json.loads(
            Path(rec).read_text(encoding="utf-8"))["source"])

    def test_write_pmid_unresolvable_does_write_when_nothing_else_resolves(self):
        rec = self.fx.record("onlypubmed", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "doi": "10.1/a"})
        self.fx.cache_put("crossref", "10.1/a", {"ok": False, "error": "http_404"})
        self.fx.cache_put("doiorg", "10.1/a", {"ok": False, "error": "http_404"})
        self.fx.cache_put(V.PUBMED_AID_CACHE_KIND, "10.1/a",
                          esearch_payload(["1"]))
        self.fx.cache_put("pubmed", "1", pubmed_payload(
            "A Study of Things.", ["Smith A"], 2001, doi="10.1/a"))
        self._run(["--repo", str(self.fx.repo), "--cache", str(self.fx.cache),
                   "--offline", "--progress", "0", "--doi-crosswalk",
                   "--write-pmid", "unresolvable"])
        self.assertEqual("1", json.loads(
            Path(rec).read_text(encoding="utf-8"))["source"]["pmid"])


# --------------------------------------------------------------------------
# the secondary identifiers -- arxiv_id, pmc, isbn
#
# ROUGHLY HALF OF WHAT FOLLOWS IS NEGATIVE CONTROLS, for the same reason as the
# doi/pmid half above: these verdicts gate commits, so the expensive failure is
# firing on a CORRECT record. Each new axis brings its own false-positive shape
# and each is pinned here as a record that must NOT produce a verdict:
#
#   pmc     a PubMed record that is not in PMC at all (the common case across
#           PubMed as a whole) -- test_pubmed_without_a_pmc_id_fails_open
#   arxiv   preprint author order (the CURL case, MORE likely here than on the
#           DOI path) -- test_preprint_author_order_alone_does_not_fire
#           an initials-only declared author against arXiv's full given names
#           -- test_initials_form_author_agrees
#           a version suffix -- test_version_suffix_is_not_a_mismatch
#           a NON-arXiv doi sitting beside an arxiv_id
#           -- test_an_ordinary_doi_beside_an_arxiv_id_is_silent
#   isbn    a CHAPTER record against its containing volume's ISBN, which is the
#           measured false positive that kept verdict 8 off the gate entirely
#           -- TestIsbnIsNotOnTheGatePath


class TestNormalisePmc(unittest.TestCase):

    def test_the_prefix_is_normalised(self):
        self.assertEqual("PMC2801761", V.normalise_pmc("PMC2801761"))
        self.assertEqual("PMC2801761", V.normalise_pmc("pmc2801761"))
        self.assertEqual("PMC2801761", V.normalise_pmc("2801761"))
        self.assertEqual("PMC2801761", V.normalise_pmc(" PMC 2801761 "))

    def test_empty_is_none(self):
        self.assertIsNone(V.normalise_pmc(None))
        self.assertIsNone(V.normalise_pmc(""))
        self.assertIsNone(V.normalise_pmc("PMC"))

    def test_different_ids_are_not_equal(self):
        self.assertNotEqual(V.normalise_pmc("PMC2801761"),
                            V.normalise_pmc("PMC2801762"))


class TestPubmedDeclaredPmc(unittest.TestCase):

    def test_the_clean_pmc_field_is_read(self):
        rec = pubmed_payload("T", ["A"], 2010, pmc="PMC2801761")["message"]
        self.assertEqual("PMC2801761", V.pubmed_declared_pmc(rec))

    def test_the_pmcid_prose_form_is_the_fallback(self):
        # `pmc-id: PMC8497431;manuscript-id: NIHMS1731801;` -- a real shape.
        rec = pubmed_payload("T", ["A"], 2010, pmc="PMC8497431",
                             pmc_only_in_pmcid=True)["message"]
        self.assertEqual("PMC8497431", V.pubmed_declared_pmc(rec))

    def test_no_pmc_at_all_is_none_not_an_error(self):
        # The COMMON case across PubMed: most records are not in PMC.
        rec = pubmed_payload("T", ["A"], 2010)["message"]
        self.assertIsNone(V.pubmed_declared_pmc(rec))


class TestPmcPmidMismatch(FixtureCase):

    def _record(self, pmc, pubmed_pmc, **kwargs):
        rec = self.fx.record("pmcrec", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2010, "pmid": "19816984", "pmc": pmc})
        self.fx.cache_put("pubmed", "19816984", pubmed_payload(
            "A Study of Things.", ["Smith A"], 2010, pmc=pubmed_pmc, **kwargs))
        return rec

    def test_mismatch_fires(self):
        rec = self._record("PMC2801761", "PMC7282808")
        verdict = self.assertVerdict(rec, "pmc_pmid_mismatch")
        self.assertIn("PMC7282808", verdict.detail)
        self.assertIn("PMC2801761", verdict.detail)

    def test_agreement_is_silent(self):
        self.assertNoVerdict(self._record("PMC2801761", "PMC2801761"))

    def test_spelling_variation_is_not_a_mismatch(self):
        # NEGATIVE CONTROL. Both sides go through normalise_pmc, so a record
        # writing the id in a different case or without the prefix agrees.
        self.assertNoVerdict(self._record("pmc2801761", "PMC2801761"))
        self.assertNoVerdict(self._record("2801761", "PMC2801761"))

    def test_the_pmcid_fallback_still_cross_resolves(self):
        self.assertNoVerdict(self._record("PMC8497431", "PMC8497431",
                                          pmc_only_in_pmcid=True))

    def test_pubmed_without_a_pmc_id_fails_open(self):
        # NEGATIVE CONTROL and the big one: most PubMed records are not in PMC,
        # so "PubMed names no PMC id" must never read as a contradiction.
        rec = self.fx.record("nopmc", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2010, "pmid": "19816984", "pmc": "PMC2801761"})
        self.fx.cache_put("pubmed", "19816984", pubmed_payload(
            "A Study of Things.", ["Smith A"], 2010))
        self.assertNoVerdict(rec)

    def test_an_unresolvable_pmid_fails_open(self):
        rec = self.fx.record("badpmid", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2010, "pmid": "99999999", "pmc": "PMC2801761"})
        self.fx.cache_put("pubmed", "99999999", {"ok": False,
                                                 "error": "not_found"})
        self.assertNoVerdict(rec)

    def test_a_record_with_no_pmid_does_not_fire_verdict_five(self):
        # Nothing to cross-resolve against. check_pmc_declared_vs_identifier is
        # the (report-only) fallback for this shape.
        rec = self.fx.record("pmconly", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2010, "pmc": "PMC2801761"})
        self.assertNoVerdict(rec)

    def test_the_crosswalk_costs_ZERO_extra_network(self):
        # The load-bearing cost claim in the module docstring: verdict 5 reads
        # the esummary record verdict 1 has already fetched, so adding it to the
        # gate adds no calls at all. If a later change makes it fetch anything
        # of its own, this fails -- which is the point.
        rec = self._record("PMC2801761", "PMC7282808")
        target = V.collect_scoped_targets([str(rec)])[0]
        resolver = V.Resolver(self.fx.cache, offline=False)
        self.assertIsNotNone(V.check_pmc_pmid_mismatch(target, resolver))
        self.assertEqual(0, resolver.spent)
        self.assertEqual([], resolver.skipped)


class TestPmcFallbackIsNotOnTheGatePath(FixtureCase):
    """check_pmc_declared_vs_identifier is implemented and deliberately unwired.

    The obvious reading is "not finished yet". It is not: all 80 pmc-carrying
    records in this corpus also carry a pmid, so verdict 5 covers every one of
    them CONCLUSIVELY and for FREE, while this would spend an esummary call per
    record to reach a strictly weaker verdict-3-shaped conclusion. Wiring it in
    would cost budget and buy nothing.

    This is a property of the CORPUS, not of the code -- one pmc-only record
    flips it. Re-measure with --secondary-check; do not assume.
    """

    def test_check_is_not_in_checks_networked(self):
        self.assertNotIn(V.check_pmc_declared_vs_identifier, V.CHECKS_NETWORKED)
        self.assertIn(V.check_pmc_declared_vs_identifier, V.CHECKS_REPORT_ONLY)

    def test_the_gate_stays_silent_on_a_pmc_only_defect(self):
        rec = self.fx.record("pmconlybad", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2010, "pmc": "PMC2801761"})
        self.fx.cache_put(V.PMC_CACHE_KIND, "PMC2801761", {"ok": True,
            "message": pubmed_payload("Something Else Entirely.",
                                      ["Jones B"], 2010)["message"]})
        self.assertNoVerdict(rec)

    def test_but_the_check_itself_does_fire_when_asked(self):
        rec = self.fx.record("pmconlybad2", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2010, "pmc": "PMC2801761"})
        self.fx.cache_put(V.PMC_CACHE_KIND, "PMC2801761", {"ok": True,
            "message": pubmed_payload("Something Else Entirely.",
                                      ["Jones B"], 2010)["message"]})
        target = V.collect_scoped_targets([str(rec)])[0]
        verdict = V.check_pmc_declared_vs_identifier(target, self.fx.resolver())
        self.assertIsNotNone(verdict)
        self.assertEqual("pmc_names_a_different_paper", verdict.kind)


class TestNormaliseArxivId(unittest.TestCase):

    def test_the_version_suffix_is_stripped(self):
        # Load-bearing: the API answers a query for 2307.07176 with
        # .../abs/2307.07176v3, so without this every hit is refused.
        self.assertEqual("2307.07176", V.normalise_arxiv_id("2307.07176v3"))
        self.assertEqual("2307.07176",
                         V.normalise_arxiv_id("http://arxiv.org/abs/2307.07176v3"))

    def test_prefixes_and_urls_are_stripped(self):
        for form in ("arXiv:2307.07176", "arxiv:2307.07176",
                     "https://arxiv.org/abs/2307.07176",
                     "https://www.arxiv.org/pdf/2307.07176.pdf"):
            self.assertEqual("2307.07176", V.normalise_arxiv_id(form), form)

    def test_old_style_ids_survive(self):
        self.assertEqual("cs.lg/0701001", V.normalise_arxiv_id("cs.LG/0701001"))

    def test_near_miss_ids_are_not_equal(self):
        # The defect class this whole file exists for, one identifier over.
        self.assertNotEqual(V.normalise_arxiv_id("1703.04977"),
                            V.normalise_arxiv_id("1703.04978"))

    def test_empty_is_none(self):
        self.assertIsNone(V.normalise_arxiv_id(None))
        self.assertIsNone(V.normalise_arxiv_id(""))


class TestArxivIdFromDoi(unittest.TestCase):

    def test_a_datacite_arxiv_doi_encodes_the_id(self):
        self.assertEqual("2106.03443",
                         V.arxiv_id_from_doi("10.48550/arXiv.2106.03443"))
        self.assertEqual("2106.03443",
                         V.arxiv_id_from_doi("10.48550/arxiv.2106.03443"))
        self.assertEqual("2106.03443",
                         V.arxiv_id_from_doi("https://doi.org/10.48550/arXiv.2106.03443"))

    def test_an_ordinary_doi_encodes_nothing(self):
        # NEGATIVE CONTROL. A journal DOI beside an arxiv_id is the normal shape
        # for a published preprint and must never be read as a crosswalk.
        self.assertIsNone(V.arxiv_id_from_doi("10.1016/j.conb.2010.02.014"))
        self.assertIsNone(V.arxiv_id_from_doi(None))
        self.assertIsNone(V.arxiv_id_from_doi(""))


class TestArxivDoiMismatch(FixtureCase):

    def _record(self, arxiv_id, doi):
        return self.fx.record("arxivrec", {
            "title": "Causal Influence Detection",
            "authors": ["Seitzer M"], "year": 2021,
            "doi": doi, "arxiv_id": arxiv_id})

    def test_mismatch_fires(self):
        rec = self._record("2106.03443", "10.48550/arXiv.2011.09464")
        verdict = self.assertVerdict(rec, "arxiv_doi_mismatch")
        self.assertIn("2011.09464", verdict.detail)

    def test_agreement_is_silent(self):
        self.assertNoVerdict(self._record("2106.03443",
                                          "10.48550/arXiv.2106.03443"))

    def test_case_difference_is_not_a_mismatch(self):
        self.assertNoVerdict(self._record("2106.03443",
                                          "10.48550/ARXIV.2106.03443"))

    def test_version_suffix_is_not_a_mismatch(self):
        # NEGATIVE CONTROL: an id recorded with its version against a DOI minted
        # without one is the SAME preprint.
        self.assertNoVerdict(self._record("2106.03443v2",
                                          "10.48550/arXiv.2106.03443"))

    def test_an_ordinary_doi_beside_an_arxiv_id_is_silent(self):
        # NEGATIVE CONTROL, and the important one: a published preprint carries
        # a journal DOI AND an arxiv_id, and those two are SUPPOSED to differ.
        self.assertNoVerdict(self._record("2106.03443",
                                          "10.1016/j.conb.2010.02.014"))

    def test_it_needs_no_network_at_all(self):
        rec = self._record("2106.03443", "10.48550/arXiv.2011.09464")
        target = V.collect_scoped_targets([str(rec)])[0]
        resolver = V.Resolver(self.fx.cache, offline=False)
        self.assertIsNotNone(V.check_arxiv_doi_mismatch(target, resolver))
        self.assertEqual(0, resolver.spent)


class TestArxivNamesADifferentPaper(FixtureCase):

    def _record(self, entry, source):
        return self.fx.record(entry, source)

    def test_a_near_miss_arxiv_id_fires(self):
        # Real: 1703.04977 is Kendall & Gal; 1703.04978 is "Lectures on EW
        # Standard Model" by Godbole. Exactly the near-miss defect class the
        # audit documented for DOIs, reachable here for the first time.
        rec = self._record("kendallgal", {
            "title": "What Uncertainties Do We Need in Bayesian Deep Learning "
                     "for Computer Vision?",
            "authors": ["Alex Kendall", "Yarin Gal"], "year": 2017,
            "arxiv_id": "1703.04978"})
        self.fx.cache_put(V.ARXIV_CACHE_KIND, "1703.04978", arxiv_payload(
            "1703.04978", "Lectures on EW Standard Model",
            ["Rohini M. Godbole"], 2017))
        verdict = self.assertVerdict(rec, "arxiv_names_a_different_paper")
        self.assertIn("Godbole", verdict.detail)

    def test_a_correct_id_is_silent(self):
        rec = self._record("ok", {
            "title": "Supervised Contrastive Learning",
            "authors": ["Khosla, Prannay"], "year": 2020,
            "arxiv_id": "2004.11362"})
        self.fx.cache_put(V.ARXIV_CACHE_KIND, "2004.11362", arxiv_payload(
            "2004.11362", "Supervised Contrastive Learning",
            ["Prannay Khosla", "Piotr Teterwak"], 2020))
        self.assertNoVerdict(rec)

    def test_initials_form_author_agrees(self):
        # NEGATIVE CONTROL, from the corpus: the record writes "Seitzer M" and
        # arXiv serves "Maximilian Seitzer".
        rec = self._record("initials", {
            "title": "Causal Influence Detection for Improving Efficiency in "
                     "Reinforcement Learning",
            "authors": ["Seitzer M", "Scholkopf B"], "year": 2021,
            "arxiv_id": "2106.03443"})
        self.fx.cache_put(V.ARXIV_CACHE_KIND, "2106.03443", arxiv_payload(
            "2106.03443",
            "Causal Influence Detection for Improving Efficiency in "
            "Reinforcement Learning",
            ["Maximilian Seitzer", "Bernhard Schoelkopf"], 2021))
        self.assertNoVerdict(rec)

    def test_preprint_author_order_alone_does_not_fire(self):
        # NEGATIVE CONTROL, documented false-positive class 4 -- and MORE likely
        # on this axis than on the DOI one, since the arXiv version IS the
        # preprint. The conjunction is what survives it: the title is correct.
        rec = self._record("curl", {
            "title": "CURL: Contrastive Unsupervised Representations for "
                     "Reinforcement Learning",
            "authors": ["Laskin, Michael"], "year": 2020,
            "arxiv_id": "2004.04136"})
        self.fx.cache_put(V.ARXIV_CACHE_KIND, "2004.04136", arxiv_payload(
            "2004.04136",
            "CURL: Contrastive Unsupervised Representations for "
            "Reinforcement Learning",
            ["Aravind Srinivas", "Michael Laskin"], 2020))
        self.assertNoVerdict(rec)

    def test_subtitle_truncation_alone_does_not_fire(self):
        # NEGATIVE CONTROL, documented false-positive class 1.
        rec = self._record("subtitle", {
            "title": "SafeDreamer",
            "authors": ["Weidong Huang"], "year": 2024,
            "arxiv_id": "2307.07176"})
        self.fx.cache_put(V.ARXIV_CACHE_KIND, "2307.07176", arxiv_payload(
            "2307.07176", "SafeDreamer: Safe Reinforcement Learning with "
            "World Models", ["Weidong Huang"], 2024))
        self.assertNoVerdict(rec)

    def test_a_confirming_arxiv_doi_skips_the_lookup_entirely(self):
        # The cost claim: 3 of the 5 arXiv records in the corpus need no call,
        # because their own DOI already establishes the id record-internally.
        rec = self._record("confirmed", {
            "title": "Supervised Contrastive Learning",
            "authors": ["Khosla, Prannay"], "year": 2020,
            "doi": "10.48550/arXiv.2004.11362", "arxiv_id": "2004.11362"})
        target = V.collect_scoped_targets([str(rec)])[0]
        resolver = V.Resolver(self.fx.cache, offline=False)
        self.assertIsNone(
            V.check_arxiv_names_a_different_paper(target, resolver))
        self.assertEqual(0, resolver.spent)

    def test_an_unresolvable_id_fails_open(self):
        rec = self._record("gone", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2020, "arxiv_id": "9999.99999"})
        self.fx.cache_put(V.ARXIV_CACHE_KIND, "9999.99999",
                          {"ok": False, "error": "not_found"})
        self.assertNoVerdict(rec)

    def test_an_answer_about_a_different_id_is_refused(self):
        # The arXiv-side twin of aid_query_is_faithful. An authority quietly
        # answering about a NEIGHBOURING record would turn a fail-open miss into
        # a confident wrong verdict.
        rec = self._record("unfaithful", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2020, "arxiv_id": "2004.11362"})
        self.fx.cache_put(V.ARXIV_CACHE_KIND, "2004.11362", arxiv_payload(
            "1703.04978", "Lectures on EW Standard Model",
            ["Rohini M. Godbole"], 2017))
        self.assertNoVerdict(rec)
        resolver = self.fx.resolver()
        self.assertEqual((None, "unfaithful_answer"),
                         resolver.arxiv_view("2004.11362"))

    def test_offline_fails_open_and_names_what_it_skipped(self):
        rec = self._record("offline", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2020, "arxiv_id": "2004.11362"})
        verdicts, resolver = self.verdicts_for(rec)
        self.assertEqual([], verdicts)
        self.assertIn(("arxiv:2004.11362", "offline"), resolver.skipped)

    def test_the_arxiv_fetch_budget_is_named_when_spent(self):
        # Not a silent cap: the per-kind budget exists so a bulk pull cannot
        # make `git commit` wait on arXiv's slow request rate, and whatever it
        # skips has to be reported (CLAUDE.md, "No silent caps").
        resolver = V.Resolver(self.fx.cache, offline=False, arxiv_budget=1)
        resolver._may_fetch("arxiv:a", kind="arxiv")
        self.assertFalse(resolver._may_fetch("arxiv:b", kind="arxiv"))
        self.assertIn(("arxiv:b", "arxiv fetch budget spent"), resolver.skipped)

    def test_the_arxiv_budget_does_not_cap_the_other_sources(self):
        resolver = V.Resolver(self.fx.cache, offline=False, arxiv_budget=1)
        resolver._may_fetch("arxiv:a", kind="arxiv")
        self.assertTrue(resolver._may_fetch("doi:10.1/a"))
        self.assertTrue(resolver._may_fetch("pmid:1"))

    def test_arxiv_budget_zero_means_no_cap(self):
        resolver = V.Resolver(self.fx.cache, offline=False, arxiv_budget=0)
        for i in range(20):
            self.assertTrue(resolver._may_fetch("arxiv:%d" % i, kind="arxiv"))


class TestIsbnChecksum(unittest.TestCase):

    def test_the_corpus_isbns_all_verify(self):
        # The measured baseline for verdict 4b: 0 findings of 5.
        for value in ("9780674458086", "9780691126241", "9780893912314",
                      "9780521633956", "978-0-465-02122-2"):
            self.assertIs(True, V.isbn_check_digit_ok(value), value)

    def test_a_transposed_digit_is_caught(self):
        self.assertIs(False, V.isbn_check_digit_ok("978-0-465-02122-3"))
        self.assertIs(False, V.isbn_check_digit_ok("9780674458087"))

    def test_isbn_10_with_an_x_check_digit_verifies(self):
        self.assertIs(True, V.isbn_check_digit_ok("089391231X"))
        self.assertIs(False, V.isbn_check_digit_ok("0893912311"))

    def test_a_wrong_length_is_none_not_false(self):
        # A shape problem is validate_literature.py's, not this file's, so it
        # fails OPEN rather than blocking a commit on a schema question.
        self.assertIsNone(V.isbn_check_digit_ok("12345"))
        self.assertIsNone(V.isbn_check_digit_ok(""))
        self.assertIsNone(V.isbn_check_digit_ok(None))

    def test_an_x_outside_the_check_position_is_none_not_false(self):
        self.assertIsNone(V.isbn_check_digit_ok("08X391231X"))

    def test_canonical_form_drops_separators(self):
        self.assertEqual("9780465021222", V.canonical_isbn("978-0-465-02122-2"))
        self.assertEqual("089391231X", V.canonical_isbn("0-89391-231-x"))


class TestIsbnMalformedVerdict(FixtureCase):

    def _record(self, isbn):
        return self.fx.record("book", {
            "title": "The Evolution of Cooperation",
            "authors": ["Robert Axelrod"], "year": 1984, "isbn": isbn})

    def test_a_bad_check_digit_fires(self):
        verdict = self.assertVerdict(self._record("978-0-465-02122-3"),
                                     "malformed_identifier")
        self.assertIn("check digit", verdict.detail)

    def test_a_good_check_digit_is_silent(self):
        self.assertNoVerdict(self._record("978-0-465-02122-2"))

    def test_it_needs_no_network(self):
        rec = self._record("9780674458087")
        target = V.collect_scoped_targets([str(rec)])[0]
        resolver = V.Resolver(self.fx.cache, offline=False)
        self.assertIsNotNone(V.check_isbn_malformed(target, resolver))
        self.assertEqual(0, resolver.spent)

    def test_a_wrong_length_isbn_fails_open(self):
        self.assertNoVerdict(self._record("12345"))


class TestIsbnIsNotOnTheGatePath(FixtureCase):
    """Verdict 8 is report-only, and this class holds the MEASUREMENT that says so.

    An ISBN identifies a VOLUME, not a chapter. So a CORRECT ISBN on a chapter
    record resolves to a different title by different people (the volume's
    editors) and trips verdict 3's conjunction -- the same conjunction that
    measures 0 false positives in 2060 records on the DOI path produces 1 in 5
    here, because the identifier's semantics are the problem, not the
    comparison. The `venue` disjunction rescues it, but that rule was written
    from the single record it rescues, so it stays off the gate.

    FLIP CONDITION (module docstring, verdict 8): >= 15 ISBN-carrying records,
    with the chapter-shaped ones separable by a rule not written from them.
    """

    def _chapter_record(self):
        # The real corpus record and the real OpenLibrary answer.
        rec = self.fx.record("murray1985", {
            "title": "Emotional regulation of interactions between "
                     "two-month-olds and their mothers",
            "authors": ["Murray, Lynne", "Trevarthen, Colwyn"], "year": 1985,
            "venue": "Social Perception in Infants",
            "isbn": "9780893912314"})
        self.fx.cache_put(V.OPENLIBRARY_CACHE_KIND, "9780893912314",
                          openlibrary_payload("Social perception in infants",
                                              ["Tiffany Field",
                                               "Nathan A. Fox"], 1985))
        return rec

    def test_check_is_not_in_checks_networked(self):
        self.assertNotIn(V.check_isbn_names_a_different_work,
                         V.CHECKS_NETWORKED)
        self.assertIn(V.check_isbn_names_a_different_work,
                      V.CHECKS_REPORT_ONLY)

    def test_the_gate_stays_silent_on_an_isbn_title_defect(self):
        rec = self.fx.record("wrongisbn", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "isbn": "9780893912314"})
        self.fx.cache_put(V.OPENLIBRARY_CACHE_KIND, "9780893912314",
                          openlibrary_payload("Social perception in infants",
                                              ["Tiffany Field"], 1985))
        self.assertNoVerdict(rec)

    def test_the_gate_never_contacts_openlibrary(self):
        # The fail-open argument: a third API in the commit path is a third way
        # to be unreachable, so verdict 8 keeps it off that path entirely.
        rec = self.fx.record("uncached", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "isbn": "9780893912314"})
        target = V.collect_scoped_targets([str(rec)])[0]
        resolver = V.Resolver(self.fx.cache, offline=False)
        V.verify_target(target, resolver)
        self.assertEqual(0, resolver.spent)

    def test_the_chapter_record_WOULD_fire_without_the_venue_disjunction(self):
        # This is the measurement, asserted rather than described: both axes of
        # the raw conjunction disagree on a record with nothing wrong with it.
        rec = self._chapter_record()
        target = V.collect_scoped_targets([str(rec)])[0]
        view, _ = self.fx.resolver().isbn_view(target["isbn"])
        self.assertIs(False, V.titles_agree(target["source"]["title"],
                                            view["title"]))
        self.assertIs(False, V.first_authors_agree(
            target["source"]["authors"], view["authors"]))

    def test_and_the_venue_disjunction_is_what_rescues_it(self):
        rec = self._chapter_record()
        target = V.collect_scoped_targets([str(rec)])[0]
        self.assertIsNone(V.check_isbn_names_a_different_work(
            target, self.fx.resolver()))

    def test_a_chapter_record_with_no_venue_is_NOT_rescued(self):
        # Honest about the limit: `venue` is not schema-enforced, so the rescue
        # is not general. Recorded as a test rather than left as a claim.
        rec = self.fx.record("noven", {
            "title": "Emotional regulation of interactions between "
                     "two-month-olds and their mothers",
            "authors": ["Murray, Lynne"], "year": 1985,
            "isbn": "9780893912314"})
        self.fx.cache_put(V.OPENLIBRARY_CACHE_KIND, "9780893912314",
                          openlibrary_payload("Social perception in infants",
                                              ["Tiffany Field"], 1985))
        target = V.collect_scoped_targets([str(rec)])[0]
        self.assertIsNotNone(V.check_isbn_names_a_different_work(
            target, self.fx.resolver()))

    def test_a_monograph_with_a_correct_isbn_agrees(self):
        rec = self.fx.record("axelrod", {
            "title": "The Evolution of Cooperation",
            "authors": ["Robert Axelrod"], "year": 1984,
            "venue": "Basic Books", "isbn": "978-0-465-02122-2"})
        self.fx.cache_put(V.OPENLIBRARY_CACHE_KIND, "978-0-465-02122-2",
                          openlibrary_payload("The evolution of cooperation",
                                              ["Robert M. Axelrod"], 1984))
        target = V.collect_scoped_targets([str(rec)])[0]
        self.assertIsNone(V.check_isbn_names_a_different_work(
            target, self.fx.resolver()))

    def test_an_isbn_openlibrary_does_not_hold_fails_open(self):
        # 1 of the 5 corpus ISBNs (Bratman 1987) is exactly this.
        rec = self.fx.record("absent", {
            "title": "Intention, Plans, and Practical Reason",
            "authors": ["Bratman, Michael E."], "year": 1987,
            "isbn": "9780674458086"})
        self.fx.cache_put(V.OPENLIBRARY_CACHE_KIND, "9780674458086",
                          {"ok": False, "error": "not_found"})
        target = V.collect_scoped_targets([str(rec)])[0]
        self.assertIsNone(V.check_isbn_names_a_different_work(
            target, self.fx.resolver()))


class TestSecondaryFetchers(unittest.TestCase):
    """Answers are cached; TRANSPORT failures are not. Same split as fetch_pubmed_aid.

    An HTTP 503 persisted as though it were an answer would silently remove that
    record from every future check, indistinguishably from a real miss.
    """

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="lit_secondary_test_"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self._http_get = audit.http_get
        self.addCleanup(setattr, audit, "http_get", self._http_get)

    ATOM = ("<?xml version='1.0' encoding='UTF-8'?>"
            "<feed xmlns='http://www.w3.org/2005/Atom'><entry>"
            "<id>http://arxiv.org/abs/2307.07176v3</id>"
            "<title>SafeDreamer</title>"
            "<published>2023-07-14T06:00:08Z</published>"
            "<author><name>Weidong Huang</name></author>"
            "</entry></feed>")

    EMPTY_ATOM = ("<?xml version='1.0' encoding='UTF-8'?>"
                  "<feed xmlns='http://www.w3.org/2005/Atom'>"
                  "<opensearch:totalResults xmlns:opensearch="
                  "'http://a9.com/-/spec/opensearch/1.1/'>0"
                  "</opensearch:totalResults></feed>")

    def test_arxiv_success_is_cached_and_parsed(self):
        audit.http_get = lambda url, timeout=30: self.ATOM
        payload = V.fetch_arxiv("2307.07176", self.tmp,
                                audit.RateLimiter(1000))
        self.assertTrue(payload["ok"])
        self.assertEqual("SafeDreamer", payload["message"]["title"])
        self.assertEqual(["Weidong Huang"], payload["message"]["authors"])
        self.assertTrue(audit.cache_path(self.tmp, V.ARXIV_CACHE_KIND,
                                         "2307.07176").exists())

    def test_arxiv_no_such_id_IS_cached_because_it_is_an_answer(self):
        audit.http_get = lambda url, timeout=30: self.EMPTY_ATOM
        payload = V.fetch_arxiv("9999.99999", self.tmp,
                                audit.RateLimiter(1000))
        self.assertFalse(payload["ok"])
        self.assertEqual("not_found", payload["error"])
        self.assertTrue(audit.cache_path(self.tmp, V.ARXIV_CACHE_KIND,
                                         "9999.99999").exists())

    def test_arxiv_transport_failure_is_NOT_cached(self):
        def boom(url, timeout=30):
            raise urllib.error.HTTPError(url, 503, "Service Unavailable",
                                         {}, None)
        audit.http_get = boom
        payload = V.fetch_arxiv("2307.07176", self.tmp,
                                audit.RateLimiter(1000))
        self.assertEqual("http_503", payload["error"])
        self.assertFalse(audit.cache_path(self.tmp, V.ARXIV_CACHE_KIND,
                                          "2307.07176").exists())

    def test_arxiv_unparseable_body_is_not_a_crash(self):
        audit.http_get = lambda url, timeout=30: "<not xml"
        payload = V.fetch_arxiv("2307.07176", self.tmp,
                                audit.RateLimiter(1000))
        self.assertFalse(payload["ok"])

    def test_openlibrary_empty_object_is_a_not_found_answer(self):
        # OpenLibrary answers an unknown ISBN with {} and HTTP 200.
        audit.http_get = lambda url, timeout=30: "{}"
        payload = V.fetch_openlibrary("9780674458086", self.tmp,
                                      audit.RateLimiter(1000))
        self.assertEqual("not_found", payload["error"])
        self.assertTrue(audit.cache_path(self.tmp, V.OPENLIBRARY_CACHE_KIND,
                                         "9780674458086").exists())

    def test_openlibrary_success_is_cached_under_the_canonical_isbn(self):
        audit.http_get = lambda url, timeout=30: json.dumps(
            {"ISBN:9780465021222": {"title": "The evolution of cooperation",
                                    "authors": [{"name": "Robert M. Axelrod"}],
                                    "publish_date": "1984"}})
        payload = V.fetch_openlibrary("978-0-465-02122-2", self.tmp,
                                      audit.RateLimiter(1000))
        self.assertTrue(payload["ok"])
        self.assertTrue(audit.cache_path(self.tmp, V.OPENLIBRARY_CACHE_KIND,
                                         "9780465021222").exists())

    def test_openlibrary_transport_failure_is_NOT_cached(self):
        def boom(url, timeout=30):
            raise urllib.error.URLError("connection reset")
        audit.http_get = boom
        V.fetch_openlibrary("9780465021222", self.tmp, audit.RateLimiter(1000))
        self.assertFalse(audit.cache_path(self.tmp, V.OPENLIBRARY_CACHE_KIND,
                                          "9780465021222").exists())

    def test_pmc_transport_failure_is_NOT_cached(self):
        def boom(url, timeout=30):
            raise urllib.error.HTTPError(url, 429, "Too Many", {}, None)
        audit.http_get = boom
        payload = V.fetch_pmc("PMC2801761", self.tmp, audit.RateLimiter(1000))
        self.assertEqual("http_429", payload["error"])
        self.assertFalse(audit.cache_path(self.tmp, V.PMC_CACHE_KIND,
                                          "PMC2801761").exists())

    def test_pmc_success_is_cached_under_the_normalised_id(self):
        audit.http_get = lambda url, timeout=30: json.dumps(
            {"result": {"2801761": {"title": "Disruption of ripples.",
                                    "authors": [{"name": "Ego-Stengel V",
                                                 "authtype": "Author"}],
                                    "pubdate": "2010 Jan"}}})
        payload = V.fetch_pmc("PMC2801761", self.tmp, audit.RateLimiter(1000))
        self.assertTrue(payload["ok"])
        self.assertTrue(audit.cache_path(self.tmp, V.PMC_CACHE_KIND,
                                         "PMC2801761").exists())


class TestPrimaryFetcherCaching(unittest.TestCase):
    """The audit's THREE original fetchers, held to the same answer-vs-transport
    split ``fetch_pubmed_aid`` and ``TestSecondaryFetchers`` already pin.

    Until 2026-08-14 all three ended in an unconditional ``path.write_text``
    that ran for EVERY exception, so a 429 from NCBI's rate limiter or a dropped
    connection was persisted as a permanent verdict about that identifier. Every
    fetcher returns early on ``path.exists()``, so nothing ever re-asked: one bad
    network window silently and permanently removed an arbitrary set of records
    from the commit gate's coverage, and they were not even named in
    ``resolver.skipped`` -- from the resolver's point of view the question had
    been asked and answered.

    HALF OF THESE ARE NEGATIVE CONTROLS, and they are the half that matters
    most. Refusing to cache a real 404 would be its own regression: Crossref and
    doi.org answer "I do not know this DOI" with a 404, that IS an answer, and
    re-fetching every dead DOI on every sweep is exactly what the caching is for.
    The bug was never "it caches failures", it was "it cannot tell the two
    apart".
    """

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="lit_primary_test_"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self._http_get = audit.http_get
        self.addCleanup(setattr, audit, "http_get", self._http_get)
        # fetch_doiorg builds its own Request (it needs the CSL Accept header)
        # rather than going through audit.http_get, so it has to be stubbed one
        # level lower. Restored by addCleanup either way.
        self._urlopen = urllib.request.urlopen
        self.addCleanup(setattr, urllib.request, "urlopen", self._urlopen)

    def _cached(self, kind, ident):
        return audit.cache_path(self.tmp, kind, ident).exists()

    def _stub_doiorg(self, body=None, exc=None):
        class _Resp:
            def __enter__(self_inner):
                return self_inner

            def __exit__(self_inner, *a):
                return False

            def read(self_inner):
                return body.encode("utf-8")

        def fake(request, timeout=30):
            if exc is not None:
                raise exc
            return _Resp()

        urllib.request.urlopen = fake

    # -- crossref ---------------------------------------------------------

    def test_crossref_success_is_cached(self):
        audit.http_get = lambda url, timeout=30: json.dumps(
            crossref_payload("A Paper", ["Smith"], 2001))
        payload = audit.fetch_crossref("10.1/a", self.tmp,
                                       audit.RateLimiter(1000))
        self.assertTrue(payload["ok"])
        self.assertTrue(self._cached("crossref", "10.1/a"))

    def test_crossref_404_IS_cached_because_it_is_an_answer(self):
        # NEGATIVE CONTROL. "Crossref does not know this DOI" is a real answer
        # and must stay cached -- this is the case the pre-fix unconditional
        # write got right, and the reason these fetchers cache HTTP errors at all.
        def boom(url, timeout=30):
            raise urllib.error.HTTPError(url, 404, "Not Found", {}, None)
        audit.http_get = boom
        payload = audit.fetch_crossref("10.1/gone", self.tmp,
                                       audit.RateLimiter(1000))
        self.assertEqual("http_404", payload["error"])
        self.assertTrue(self._cached("crossref", "10.1/gone"))

    def test_crossref_429_is_NOT_cached(self):
        def boom(url, timeout=30):
            raise urllib.error.HTTPError(url, 429, "Too Many Requests", {}, None)
        audit.http_get = boom
        payload = audit.fetch_crossref("10.1/b", self.tmp,
                                       audit.RateLimiter(1000))
        self.assertEqual("http_429", payload["error"])
        self.assertFalse(self._cached("crossref", "10.1/b"))

    def test_crossref_503_is_NOT_cached(self):
        def boom(url, timeout=30):
            raise urllib.error.HTTPError(url, 503, "Service Unavailable",
                                         {}, None)
        audit.http_get = boom
        audit.fetch_crossref("10.1/c", self.tmp, audit.RateLimiter(1000))
        self.assertFalse(self._cached("crossref", "10.1/c"))

    def test_crossref_403_is_NOT_cached(self):
        # Crossref needs no authentication, so a 403 is about the REQUESTER --
        # rate limiting dressed as a 403, a WAF, an intercepting proxy -- never
        # about the DOI. Decided explicitly rather than left to fall through.
        def boom(url, timeout=30):
            raise urllib.error.HTTPError(url, 403, "Forbidden", {}, None)
        audit.http_get = boom
        audit.fetch_crossref("10.1/d", self.tmp, audit.RateLimiter(1000))
        self.assertFalse(self._cached("crossref", "10.1/d"))

    def test_crossref_urlerror_is_NOT_cached(self):
        # The exact shape of the live reproduction: an unreachable network
        # persisted as "URLError: connection refused" against a real DOI.
        def boom(url, timeout=30):
            raise urllib.error.URLError("connection refused")
        audit.http_get = boom
        payload = audit.fetch_crossref("10.1/e", self.tmp,
                                       audit.RateLimiter(1000))
        self.assertFalse(payload["ok"])
        self.assertIn("URLError", payload["error"])
        self.assertFalse(self._cached("crossref", "10.1/e"))

    def test_crossref_malformed_body_is_NOT_cached(self):
        # A 200 carrying garbage is a broken service, not a verdict about the DOI.
        audit.http_get = lambda url, timeout=30: "{not json"
        payload = audit.fetch_crossref("10.1/f", self.tmp,
                                       audit.RateLimiter(1000))
        self.assertFalse(payload["ok"])
        self.assertFalse(self._cached("crossref", "10.1/f"))

    def test_crossref_returns_None_when_already_cached(self):
        # NEGATIVE CONTROL on the change itself: the cached-early-return
        # contract is what every caller distinguishes "wrote nothing" by, and
        # the fix adds a second uncached return path beside it.
        audit.http_get = lambda url, timeout=30: json.dumps(
            crossref_payload("A Paper", ["Smith"], 2001))
        audit.fetch_crossref("10.1/g", self.tmp, audit.RateLimiter(1000))
        audit.http_get = lambda url, timeout=30: self.fail("re-fetched a cached DOI")
        self.assertIsNone(audit.fetch_crossref("10.1/g", self.tmp,
                                               audit.RateLimiter(1000)))

    # -- doi.org ----------------------------------------------------------

    def test_doiorg_success_is_cached(self):
        self._stub_doiorg(body=json.dumps(
            {"title": "A Paper", "author": [{"family": "Smith"}],
             "issued": {"date-parts": [[2001]]}}))
        payload = audit.fetch_doiorg("10.2/a", self.tmp,
                                     audit.RateLimiter(1000))
        self.assertTrue(payload["ok"])
        self.assertTrue(self._cached("doiorg", "10.2/a"))

    def test_doiorg_404_IS_cached_because_it_is_an_answer(self):
        # NEGATIVE CONTROL, and the conclusive one: doi.org negotiates against
        # every registration agency, so its 404 means the DOI is registered
        # nowhere.
        self._stub_doiorg(exc=urllib.error.HTTPError(
            "https://doi.org/x", 404, "Not Found", {}, None))
        payload = audit.fetch_doiorg("10.2/gone", self.tmp,
                                     audit.RateLimiter(1000))
        self.assertEqual("http_404", payload["error"])
        self.assertTrue(self._cached("doiorg", "10.2/gone"))

    def test_doiorg_429_is_NOT_cached(self):
        self._stub_doiorg(exc=urllib.error.HTTPError(
            "https://doi.org/x", 429, "Too Many Requests", {}, None))
        audit.fetch_doiorg("10.2/b", self.tmp, audit.RateLimiter(1000))
        self.assertFalse(self._cached("doiorg", "10.2/b"))

    def test_doiorg_urlerror_is_NOT_cached(self):
        self._stub_doiorg(exc=urllib.error.URLError("connection refused"))
        payload = audit.fetch_doiorg("10.2/c", self.tmp,
                                     audit.RateLimiter(1000))
        self.assertFalse(payload["ok"])
        self.assertFalse(self._cached("doiorg", "10.2/c"))

    # -- pubmed -----------------------------------------------------------

    def test_pubmed_success_is_cached(self):
        audit.http_get = lambda url, timeout=30: json.dumps(
            {"result": {"9": pubmed_payload("A Paper", ["Smith"],
                                            2001)["message"]}})
        payload = audit.fetch_pubmed("9", self.tmp, audit.RateLimiter(1000))
        self.assertTrue(payload["ok"])
        self.assertTrue(self._cached("pubmed", "9"))

    def test_pubmed_not_found_IS_cached_because_it_is_an_answer(self):
        # NEGATIVE CONTROL. eutils does not 404 an unknown id -- it answers 200
        # with an `error` field. That is where a real PubMed negative lives, and
        # it is why no HTTP STATUS is an answer for this endpoint.
        audit.http_get = lambda url, timeout=30: json.dumps(
            {"result": {"404404": {"error": "cannot get document summary"}}})
        payload = audit.fetch_pubmed("404404", self.tmp,
                                     audit.RateLimiter(1000))
        self.assertEqual("not_found", payload["error"])
        self.assertTrue(self._cached("pubmed", "404404"))

    def test_pubmed_429_is_NOT_cached(self):
        # NCBI's rate limiter is the single likeliest way this cache could ever
        # have been poisoned: the corpus holds ~1500 PMIDs and the sweep is
        # threaded.
        def boom(url, timeout=30):
            raise urllib.error.HTTPError(url, 429, "Too Many Requests", {}, None)
        audit.http_get = boom
        payload = audit.fetch_pubmed("11", self.tmp, audit.RateLimiter(1000))
        self.assertEqual("http_429", payload["error"])
        self.assertFalse(self._cached("pubmed", "11"))

    def test_pubmed_404_is_NOT_cached_unlike_crossref(self):
        # The one place the two endpoints deliberately disagree, so it is pinned
        # rather than left to be "tidied" into a single shared set. A 404 from
        # eutils means the request or the service is wrong, not the PMID.
        def boom(url, timeout=30):
            raise urllib.error.HTTPError(url, 404, "Not Found", {}, None)
        audit.http_get = boom
        audit.fetch_pubmed("12", self.tmp, audit.RateLimiter(1000))
        self.assertFalse(self._cached("pubmed", "12"))

    def test_pubmed_urlerror_is_NOT_cached(self):
        def boom(url, timeout=30):
            raise urllib.error.URLError("connection refused")
        audit.http_get = boom
        audit.fetch_pubmed("13", self.tmp, audit.RateLimiter(1000))
        self.assertFalse(self._cached("pubmed", "13"))


class TestTransportFailureIsReportedNotSilent(unittest.TestCase):
    """A transport failure must be NAMED, never collapsed into ``unresolvable``.

    Both fail open at the gate, so this changes no verdict -- it changes what the
    run SAYS. ``unresolvable`` asserts the question was asked and answered, and a
    record dropped from coverage by a 429 must not be able to hide inside that
    word. Before the fix it could: the poisoned cache entry made the failure
    indistinguishable from a real negative on the very next read.
    """

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="lit_report_test_"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self._http_get = audit.http_get
        self.addCleanup(setattr, audit, "http_get", self._http_get)
        self._urlopen = urllib.request.urlopen
        self.addCleanup(setattr, urllib.request, "urlopen", self._urlopen)

        def boom(*a, **kw):
            raise urllib.error.URLError("connection refused")
        audit.http_get = boom
        urllib.request.urlopen = boom

    def test_a_doi_transport_failure_is_skipped_not_unresolvable(self):
        resolver = V.Resolver(self.tmp)
        view, why = resolver.doi_view("10.1/x")
        self.assertIsNone(view)
        self.assertNotEqual("unresolvable", why)
        self.assertTrue(any("10.1/x" in label for label, _ in resolver.skipped))
        self.assertTrue(any("10.1/x" in label for label, _ in resolver.errors))

    def test_a_pmid_transport_failure_is_skipped_not_silent(self):
        resolver = V.Resolver(self.tmp)
        self.assertIsNone(resolver.pubmed_record("12345"))
        self.assertTrue(any("12345" in label for label, _ in resolver.skipped))
        self.assertTrue(any("12345" in label for label, _ in resolver.errors))

    def test_a_real_negative_is_still_unresolvable_and_still_silent(self):
        # NEGATIVE CONTROL. A DOI both resolvers genuinely do not know is an
        # ANSWER: it must keep the `unresolvable` reason and must NOT be counted
        # as an unchecked record, or the gate's "N not checked" line becomes
        # noise and stops being read.
        for kind in ("crossref", "doiorg"):
            path = audit.cache_path(self.tmp, kind, "10.1/dead")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps({"ok": False, "error": "http_404"}),
                            encoding="utf-8")
        resolver = V.Resolver(self.tmp)
        view, why = resolver.doi_view("10.1/dead")
        self.assertIsNone(view)
        self.assertEqual("unresolvable", why)
        self.assertEqual([], resolver.skipped)
        self.assertEqual([], resolver.errors)

    def test_a_transport_failure_leaves_the_cache_untouched(self):
        # The whole point: the next run gets to ask again.
        resolver = V.Resolver(self.tmp)
        resolver.doi_view("10.1/y")
        resolver.pubmed_record("999")
        self.assertEqual([], sorted(self.tmp.rglob("*.json")))


class TestSecondaryTargetCollection(FixtureCase):
    """A record whose ONLY identifier is secondary must be in scope.

    It was not until 2026-08-14: both collectors filtered on doi/pmid, so an
    arxiv-only or isbn-only record fell out of scope silently -- the gate
    printed an OK line and checked nothing. 7 records in this corpus are that
    shape.
    """

    def test_an_arxiv_only_record_is_a_target(self):
        rec = self.fx.record("arxivonly", {
            "title": "SafeDreamer", "authors": ["Weidong Huang"],
            "year": 2024, "doi": None, "arxiv_id": "2307.07176"})
        targets = V.collect_scoped_targets([str(rec)])
        self.assertEqual(1, len(targets))
        self.assertEqual("2307.07176", targets[0]["arxiv_id"])

    def test_an_isbn_only_record_is_a_target(self):
        rec = self.fx.record("isbnonly", {
            "title": "The Reasons of Love", "authors": ["Frankfurt, Harry G."],
            "year": 2004, "doi": "", "isbn": "9780691126241"})
        self.assertEqual(1, len(V.collect_scoped_targets([str(rec)])))

    def test_a_pmc_only_record_is_a_target(self):
        rec = self.fx.record("pmconly", {
            "title": "A Study", "authors": ["Smith, A"], "year": 2010,
            "pmc": "PMC2801761"})
        self.assertEqual(1, len(V.collect_scoped_targets([str(rec)])))

    def test_a_record_with_no_identifier_at_all_is_still_not_a_target(self):
        rec = self.fx.record("none", {
            "title": "A Study", "authors": ["Smith, A"], "year": 2010,
            "doi": None, "pmid": None, "isbn": None})
        self.assertEqual([], V.collect_scoped_targets([str(rec)]))

    def test_collect_all_targets_sees_the_secondary_records(self):
        self.fx.record("arxivonly", {
            "title": "SafeDreamer", "authors": ["Weidong Huang"],
            "year": 2024, "arxiv_id": "2307.07176"})
        self.fx.record("doirec", {
            "title": "A Study", "authors": ["Smith, A"], "year": 2010,
            "doi": "10.1/a"})
        self.assertEqual(2, len(V.collect_all_targets()))

    def test_the_doi_pmid_population_is_still_addressable_separately(self):
        # --cross-check keeps printing the 2072 the findings doc quotes.
        self.fx.record("arxivonly", {
            "title": "SafeDreamer", "authors": ["Weidong Huang"],
            "year": 2024, "arxiv_id": "2307.07176"})
        self.fx.record("doirec", {
            "title": "A Study", "authors": ["Smith, A"], "year": 2010,
            "doi": "10.1/a"})
        self.assertEqual(
            1, len(V.collect_all_targets(keys=("doi", "pmid"))))


class TestSecondaryWaivers(FixtureCase):
    """Waivers are value-keyed on the secondary identifiers too, and normalised.

    A waiver that quietly stops matching is a waiver that quietly starts
    blocking, so the match goes through the same normalisers the verdicts
    compare with -- otherwise a waiver written `PMC2801761` would miss a record
    spelling it `pmc2801761`.
    """

    def _waive(self, **entry):
        entry.setdefault("entry", "waived")
        entry.setdefault("reason", "fixture")
        saved = V.WAIVERS
        V.WAIVERS = [entry]
        self.addCleanup(setattr, V, "WAIVERS", saved)

    def test_a_pmc_waiver_downgrades_but_still_reports(self):
        self._waive(pmc="PMC2801761")
        rec = self.fx.record("waived", {
            "title": "A Study", "authors": ["Smith, A"], "year": 2010,
            "pmid": "19816984", "pmc": "PMC2801761"})
        self.fx.cache_put("pubmed", "19816984", pubmed_payload(
            "A Study.", ["Smith A"], 2010, pmc="PMC7282808"))
        verdicts, _ = self.verdicts_for(rec)
        self.assertEqual(["waived:pmc_pmid_mismatch"],
                         [v.kind for v in verdicts])

    def test_a_pmc_waiver_is_normalised_not_string_matched(self):
        self._waive(pmc="pmc2801761")
        rec = self.fx.record("waived", {
            "title": "A Study", "authors": ["Smith, A"], "year": 2010,
            "pmid": "19816984", "pmc": "PMC2801761"})
        self.fx.cache_put("pubmed", "19816984", pubmed_payload(
            "A Study.", ["Smith A"], 2010, pmc="PMC7282808"))
        verdicts, _ = self.verdicts_for(rec)
        self.assertTrue(all(v.kind.startswith("waived:") for v in verdicts))

    def test_an_isbn_waiver_matches_the_hyphenated_form(self):
        self._waive(isbn="9780465021223")
        rec = self.fx.record("waived", {
            "title": "A Book", "authors": ["Smith, A"], "year": 1984,
            "isbn": "978-0-465-02122-3"})
        verdicts, _ = self.verdicts_for(rec)
        self.assertEqual(["waived:malformed_identifier"],
                         [v.kind for v in verdicts])

    def test_an_arxiv_waiver_ignores_the_version_suffix(self):
        self._waive(arxiv_id="2106.03443v2")
        rec = self.fx.record("waived", {
            "title": "A Study", "authors": ["Smith, A"], "year": 2021,
            "doi": "10.48550/arXiv.2011.09464", "arxiv_id": "2106.03443"})
        verdicts, _ = self.verdicts_for(rec)
        self.assertEqual(["waived:arxiv_doi_mismatch"],
                         [v.kind for v in verdicts])

    def test_a_waiver_does_not_cover_a_different_secondary_value(self):
        # The whole point of value-keying: a waived record that later gains a
        # DIFFERENT wrong identifier still blocks.
        self._waive(pmc="PMC0000001")
        rec = self.fx.record("waived", {
            "title": "A Study", "authors": ["Smith, A"], "year": 2010,
            "pmid": "19816984", "pmc": "PMC2801761"})
        self.fx.cache_put("pubmed", "19816984", pubmed_payload(
            "A Study.", ["Smith A"], 2010, pmc="PMC7282808"))
        self.assertVerdict(rec, "pmc_pmid_mismatch")


class TestReportOnlyKinds(FixtureCase):
    """REPORT_ONLY_KINDS must cover every kind a CHECKS_REPORT_ONLY check emits.

    The sweep prints findings under a "never blocks" heading based on this set,
    so a kind missing from it would be printed as advisory while actually being
    a gating verdict -- wrong in the direction that matters. Each check is run
    against a fixture that makes it FIRE, so adding a report-only check without
    listing its kind fails here rather than at the next sweep.
    """

    def _firing_targets(self):
        out = {}
        rec = self.fx.record("pmconlybad", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2010, "pmc": "PMC2801761"})
        self.fx.cache_put(V.PMC_CACHE_KIND, "PMC2801761", {"ok": True,
            "message": pubmed_payload("Something Else Entirely.",
                                      ["Jones B"], 2010)["message"]})
        out[V.check_pmc_declared_vs_identifier] = \
            V.collect_scoped_targets([str(rec)])[0]

        rec = self.fx.record("isbnbad", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "isbn": "9780893912314"})
        self.fx.cache_put(V.OPENLIBRARY_CACHE_KIND, "9780893912314",
                          openlibrary_payload("Social perception in infants",
                                              ["Tiffany Field"], 1985))
        out[V.check_isbn_names_a_different_work] = \
            V.collect_scoped_targets([str(rec)])[0]
        return out

    def test_report_only_kinds_covers_every_report_only_check(self):
        targets = self._firing_targets()
        resolver = self.fx.resolver()
        # NON-VACUITY GUARD (oracle-vacuity audit 2026-08-18). The loop below
        # iterates a registry defined by the module under test, so emptying
        # CHECKS_REPORT_ONLY runs the body zero times and this test passes
        # against nothing -- measured GREEN under `CHECKS_REPORT_ONLY -> []`.
        # Same guard TestWaivers.test_every_waiver_states_a_reason already uses
        # for V.WAIVERS. Raise the floor when a report-only check is added.
        self.assertGreaterEqual(
            len(V.CHECKS_REPORT_ONLY), 2,
            "CHECKS_REPORT_ONLY holds %d check(s); this test asserts nothing "
            "on an empty registry" % len(V.CHECKS_REPORT_ONLY))
        for check in V.CHECKS_REPORT_ONLY:
            self.assertIn(check, targets,
                          "%s has no firing fixture here -- add one"
                          % check.__name__)
            verdict = check(targets[check], resolver)
            self.assertIsNotNone(verdict,
                                 "%s did not fire on its fixture"
                                 % check.__name__)
            self.assertIn(verdict.kind, V.REPORT_ONLY_KINDS,
                          "%s emits %r, which is not in REPORT_ONLY_KINDS"
                          % (check.__name__, verdict.kind))

    def test_no_gating_check_emits_a_report_only_kind(self):
        # The other direction: a gating verdict whose kind landed in this set
        # would be printed as advisory by the sweep.
        #
        # NON-VACUITY GUARD (oracle-vacuity audit 2026-08-18): this is an
        # assertNotIn over two registries owned by the module under test, so it
        # passes vacuously if EITHER side empties -- measured GREEN under both
        # `CHECKS_REPORT_ONLY -> []` and `CHECKS_NETWORKED/OFFLINE -> []`.
        self.assertGreaterEqual(
            len(V.CHECKS_REPORT_ONLY), 2,
            "CHECKS_REPORT_ONLY is empty; the assertNotIn below is vacuous")
        self.assertTrue(
            V.CHECKS_NETWORKED and V.CHECKS_OFFLINE,
            "a gating registry is empty (networked=%d offline=%d); the "
            "assertNotIn below is vacuous"
            % (len(V.CHECKS_NETWORKED), len(V.CHECKS_OFFLINE)))
        self.assertNotIn(V.check_doi_crosswalk, V.CHECKS_NETWORKED)
        for check in V.CHECKS_NETWORKED + V.CHECKS_OFFLINE:
            self.assertNotIn(check, V.CHECKS_REPORT_ONLY)


class TestSecondaryCheckCli(FixtureCase):

    def _run(self, argv):
        from io import StringIO
        out, sys.stdout = sys.stdout, StringIO()
        try:
            rc = V.main(argv)
            return rc, sys.stdout.getvalue()
        finally:
            sys.stdout = out

    def _base(self):
        return ["--repo", str(self.fx.repo), "--cache", str(self.fx.cache),
                "--offline", "--secondary-check"]

    def test_a_clean_corpus_reports_zero_and_chains_safely(self):
        self.fx.record("ok", {
            "title": "A Study", "authors": ["Smith, A"], "year": 2010,
            "pmid": "19816984", "pmc": "PMC2801761"})
        self.fx.cache_put("pubmed", "19816984", pubmed_payload(
            "A Study.", ["Smith A"], 2010, pmc="PMC2801761"))
        rc, out = self._run(self._base())
        self.assertEqual(0, rc)
        self.assertIn("GATING verdicts                 : 0", out)

    def test_a_gating_finding_sets_exit_one_with_exit_nonzero(self):
        self.fx.record("bad", {
            "title": "A Study", "authors": ["Smith, A"], "year": 2010,
            "pmid": "19816984", "pmc": "PMC2801761"})
        self.fx.cache_put("pubmed", "19816984", pubmed_payload(
            "A Study.", ["Smith A"], 2010, pmc="PMC7282808"))
        rc, out = self._run(self._base() + ["--exit-nonzero"])
        self.assertEqual(1, rc)
        self.assertIn("pmc_pmid_mismatch", out)

    def test_a_REPORT_ONLY_finding_never_sets_exit_one(self):
        # The assertion that stops --exit-nonzero quietly promoting verdict 8.
        self.fx.record("isbnbad", {
            "title": "A Study of Things", "authors": ["Smith, A"],
            "year": 2001, "isbn": "9780893912314"})
        self.fx.cache_put(V.OPENLIBRARY_CACHE_KIND, "9780893912314",
                          openlibrary_payload("Social perception in infants",
                                              ["Tiffany Field"], 1985))
        rc, out = self._run(self._base() + ["--exit-nonzero"])
        self.assertEqual(0, rc)
        self.assertIn("isbn_names_a_different_work", out)
        self.assertIn("REPORT-ONLY", out)

    def test_a_doi_only_record_is_out_of_scope(self):
        self.fx.record("doionly", {
            "title": "A Study", "authors": ["Smith, A"], "year": 2010,
            "doi": "10.1/a"})
        rc, out = self._run(self._base())
        self.assertIn("records in scope here           : 0", out)

    def test_the_sweep_writes_json(self):
        self.fx.record("bad", {
            "title": "A Study", "authors": ["Smith, A"], "year": 2010,
            "pmid": "19816984", "pmc": "PMC2801761"})
        self.fx.cache_put("pubmed", "19816984", pubmed_payload(
            "A Study.", ["Smith A"], 2010, pmc="PMC7282808"))
        out_path = self.fx.tmp / "sweep.json"
        self._run(self._base() + ["--json", str(out_path)])
        data = json.loads(out_path.read_text(encoding="utf-8"))
        self.assertEqual(1, len(data["gating"]))
        self.assertEqual("pmc_pmid_mismatch", data["gating"][0]["kind"])


class TestSecondaryPrecommitWiring(unittest.TestCase):
    """End-to-end: a staged record with a wrong secondary identifier blocks.

    The point is not that the verdict fires -- that is tested above -- but that
    the SCOPED path list the hook builds actually reaches these records. A
    record whose only identifier is secondary used to fall out of
    collect_scoped_targets entirely, so the gate printed OK and checked nothing.
    """

    @classmethod
    def setUpClass(cls):
        cls.script = REPO_ROOT / "scripts" / "precommit_literature.sh"
        if not cls.script.exists():
            raise unittest.SkipTest("precommit_literature.sh not present")
        if not shutil.which("git"):
            raise unittest.SkipTest("git not available")

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="lit_secondary_hook_"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.repo = self.tmp / "REE_assembly"
        self.lit = self.repo / "evidence" / "literature"
        self.lit.mkdir(parents=True)
        self.cache = self.tmp / "cache"
        self.cache.mkdir()
        for script in ("validate_literature.py",
                       "verify_literature_identifiers.py",
                       "audit_literature_bibliographic_accuracy.py"):
            src = REPO_ROOT / "scripts" / script
            if not src.exists():
                raise unittest.SkipTest("%s not present" % script)
            (self.repo / "scripts").mkdir(exist_ok=True)
            shutil.copy(src, self.repo / "scripts" / script)
        subprocess.run(["git", "init", "-q"], cwd=self.repo, check=True)
        subprocess.run(["git", "config", "user.email", "t@e.st"],
                       cwd=self.repo, check=True)
        subprocess.run(["git", "config", "user.name", "T"],
                       cwd=self.repo, check=True)

    def _record(self, entry, source):
        entry_dir = self.lit / "targeted_review_x" / "entries" / entry
        entry_dir.mkdir(parents=True, exist_ok=True)
        (entry_dir / "record.json").write_text(json.dumps({
            "schema_version": "literature_evidence/v1",
            "literature_type": "targeted_review_x",
            "entry_id": entry,
            "timestamp_utc": "2026-08-14T00:00:00Z",
            "claim_ids_tested": ["MECH-001"],
            "source": source,
            "evidence_class": "theoretical_review",
            "evidence_direction": "supports",
            "confidence": 0.5,
            "confidence_rationale": "fixture",
            "summary_path": "summary.md",
            "tags": ["fixture"],
        }, indent=1), encoding="utf-8")
        (entry_dir / "summary.md").write_text("# Summary\n\nbody\n",
                                              encoding="utf-8")
        return entry_dir / "record.json"

    def _cache_put(self, kind, ident, payload):
        normalise = Fixture.KEY_NORMALISERS.get(kind)
        if normalise is not None:
            normalise = getattr(normalise, "__func__", normalise)
            key = normalise(ident)
        else:
            key = str(ident)
        path = audit.cache_path(self.cache, kind, key)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload), encoding="utf-8")

    def _run_gate(self):
        subprocess.run(["git", "add", "-A"], cwd=self.repo, check=True)
        env = dict(os.environ)
        env["REE_LIT_BIB_CACHE"] = str(self.cache)
        env["REE_LIT_BIB_OFFLINE"] = "1"
        env["REE_LITERATURE_GATE_BLOCK"] = "0"   # stage 1 is not under test
        return subprocess.run(
            ["bash", str(self.script)], cwd=self.repo, env=env,
            capture_output=True, text=True)

    def test_a_wrong_pmc_blocks_with_exit_2(self):
        self._record("badpmc", {
            "title": "A Study", "authors": ["Smith, A"], "year": 2010,
            "pmid": "19816984", "pmc": "PMC2801761"})
        self._cache_put("pubmed", "19816984", pubmed_payload(
            "A Study.", ["Smith A"], 2010, pmc="PMC7282808"))
        result = self._run_gate()
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)
        self.assertIn("pmc_pmid_mismatch", result.stdout)

    def test_a_correct_pmc_passes(self):
        self._record("okpmc", {
            "title": "A Study", "authors": ["Smith, A"], "year": 2010,
            "pmid": "19816984", "pmc": "PMC2801761"})
        self._cache_put("pubmed", "19816984", pubmed_payload(
            "A Study.", ["Smith A"], 2010, pmc="PMC2801761"))
        result = self._run_gate()
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_an_arxiv_only_record_reaches_the_gate_at_all(self):
        # The scoping regression this class exists for: before 2026-08-14 this
        # record was not a target, so the gate reported OK having checked
        # nothing at all.
        self._record("badarxiv", {
            "title": "A Study", "authors": ["Smith, A"], "year": 2021,
            "doi": "10.48550/arXiv.2011.09464", "arxiv_id": "2106.03443"})
        result = self._run_gate()
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)
        self.assertIn("arxiv_doi_mismatch", result.stdout)

    def test_a_malformed_isbn_blocks_offline(self):
        # Verdict 4b needs no network at all, so it holds on a box with none.
        self._record("badisbn", {
            "title": "A Book", "authors": ["Smith, A"], "year": 1984,
            "isbn": "978-0-465-02122-3"})
        result = self._run_gate()
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)
        self.assertIn("malformed_identifier", result.stdout)

    def test_a_valid_isbn_only_record_passes_without_touching_openlibrary(self):
        self._record("okisbn", {
            "title": "A Book", "authors": ["Smith, A"], "year": 1984,
            "isbn": "978-0-465-02122-2"})
        result = self._run_gate()
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
