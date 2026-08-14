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


def pubmed_payload(title, authors, year, doi=None, venue="A Journal", **extra):
    """An esummary record, in the shape audit.pubmed_view reads."""
    ids = [{"idtype": "pubmed", "value": "1"}]
    if doi:
        ids.append({"idtype": "doi", "value": doi})
    message = {
        "title": title,
        "authors": [{"name": a, "authtype": "Author"} for a in authors],
        "pubdate": "%d Jan" % year,
        "fulljournalname": venue,
        "articleids": ids,
    }
    message.update(extra)
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

    def cache_put(self, kind, ident, payload):
        # Mirror the module's own key normalisation rather than restating it: a
        # test that hardcodes the key passes even when the key rule changes.
        key = str(ident).lower() if kind in ("crossref", "doiorg") else str(ident)
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
