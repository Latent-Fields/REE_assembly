#!/usr/bin/env python3
"""Regression tests for validate_literature.py.

Every test builds a REAL literature tree in a tempdir -- a real schema file, real
entry directories, real record.json / summary.md -- and runs the real
collect_findings() / main() over it. Nothing is monkeypatched: the checks under
test are ABOUT the filesystem (which records the indexer's glob reaches, whether
summary_path resolves), so a mocked filesystem would test the mock.

Time-independent: no wall-clock reads, no dates derived from `now`. The one
timestamp-shaped assertion uses fixed literal strings.

Run: /opt/local/bin/python3 scripts/test_validate_literature.py
"""

import importlib.util
import io
import json
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parent
SCHEMA_REL = "evidence/literature/schemas/v1/literature_evidence.schema.json"


def _load_module(name, filename):
    path = SCRIPTS_DIR / filename
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


V = _load_module("ree_validate_literature_under_test", "validate_literature.py")


def valid_record(entry_id, literature_type):
    """A record that must validate cleanly. The baseline every test varies from."""
    return {
        "schema_version": "literature_evidence/v1",
        "literature_type": literature_type,
        "entry_id": entry_id,
        "timestamp_utc": "2026-05-16T10:00:00Z",
        "claim_ids_tested": ["MECH-001"],
        "source": {
            "title": "A Paper",
            "authors": ["Author, A."],
            "year": 2024,
            "doi": "10.1000/abc",
        },
        "evidence_class": "review",
        "evidence_direction": "supports",
        "confidence": 0.7,
        "confidence_rationale": "single well-powered study",
        "summary_path": "summary.md",
    }


class LiteratureTreeTestCase(unittest.TestCase):
    """Builds a tempdir repo with the REAL v1 schema copied in."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="ree_lit_validate_"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        schema_dst = self.tmp / SCHEMA_REL
        schema_dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPO_ROOT / SCHEMA_REL, schema_dst)
        self.lit = self.tmp / "evidence" / "literature"

    def write_entry(self, literature_type, entry_id, record=None,
                    summary=True, record_name="record.json", subdir=None):
        """Create entries/<entry_id>/record.json (+ summary.md) and return its dir."""
        entry_dir = self.lit / literature_type / "entries" / entry_id
        if subdir:
            entry_dir = entry_dir / subdir
        entry_dir.mkdir(parents=True, exist_ok=True)
        if record is None:
            record = valid_record(entry_id, literature_type)
        if record is not ...:
            (entry_dir / record_name).write_text(json.dumps(record, indent=2))
        if summary:
            (entry_dir / "summary.md").write_text("# summary\n")
        return entry_dir

    def findings(self, **kwargs):
        return V.collect_findings(self.tmp, **kwargs)

    def classes(self, **kwargs):
        found, _ = self.findings(**kwargs)
        return sorted({f.cls for f in found})


class ValidRecordTest(LiteratureTreeTestCase):
    def test_valid_record_produces_no_findings(self):
        self.write_entry("targeted_review_x", "2026-05-16_a")
        found, n_records = self.findings()
        self.assertEqual(found, [], "clean record must produce no findings: %s"
                         % [f.as_dict() for f in found])
        self.assertEqual(n_records, 1)

    def test_all_optional_blocks_populated_still_valid(self):
        record = valid_record("2026-05-16_a", "targeted_review_x")
        record.update({
            "evidence_direction_per_claim": {"MECH-001": "weakens"},
            "failure_signatures": ["sig_a"],
            "tags": ["method:fmri"],
            "mapping": {
                "source_claim_statement": "s",
                "ree_translation": "t",
                "mapping_caveat": "c",
            },
            "confidence_components": {
                "source_quality": 0.8,
                "mapping_fidelity": 0.6,
                "transfer_risk": 0.3,
            },
        })
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        self.assertEqual(self.classes(), [])


class NegativeControlTest(LiteratureTreeTestCase):
    """A null optional identifier MUST pass -- it is deliberate schema behaviour.

    The schema says so explicitly: "An optional identifier may be null, meaning
    'checked, none exists', which is more informative than omitting the key."

    This is a negative control, not a nice-to-have. A validator that rejected
    null here would push producers back toward OMITTING the key, destroying the
    distinction between "we looked and there is no DOI" and "nobody checked" --
    i.e. the gate would actively make the corpus less informative than no gate.
    """

    def test_null_identifiers_pass(self):
        record = valid_record("2026-05-16_a", "targeted_review_x")
        record["source"].update({
            "doi": None, "pmid": None, "pmc": None,
            "pmcid": None, "arxiv_id": None, "isbn": None, "url": None,
        })
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        self.assertEqual(self.classes(), [],
                         "a null optional identifier means 'checked, none "
                         "exists' and must validate")

    def test_absent_optional_identifiers_also_pass(self):
        record = valid_record("2026-05-16_a", "targeted_review_x")
        record["source"].pop("doi")
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        self.assertEqual(self.classes(), [])

    def test_null_is_not_accepted_for_a_required_descriptive_field(self):
        """The null allowance is scoped to IDENTIFIERS, not to title/authors/year."""
        record = valid_record("2026-05-16_a", "targeted_review_x")
        record["source"]["year"] = None
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        self.assertTrue(any(c.startswith("schema:source/year") for c in self.classes()),
                        "source.year is an integer field, not a nullable identifier")


class SchemaFailureClassTest(LiteratureTreeTestCase):
    def test_missing_required_top_level_field(self):
        record = valid_record("2026-05-16_a", "targeted_review_x")
        del record["confidence_rationale"]
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        self.assertIn("schema:<root>: 'X' is a required property", self.classes())

    def test_undeclared_key_on_source(self):
        record = valid_record("2026-05-16_a", "targeted_review_x")
        record["source"]["citation"] = "A. Author (2024) A Paper. J. 1:1-2."
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        self.assertIn(
            "schema:source: Additional properties are not allowed (...)",
            self.classes())

    def test_undeclared_key_at_top_level(self):
        record = valid_record("2026-05-16_a", "targeted_review_x")
        record["retagging_rationale"] = "prose that belongs in summary.md"
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        self.assertIn(
            "schema:<root>: Additional properties are not allowed (...)",
            self.classes())

    def test_evidence_direction_outside_the_closed_enum(self):
        record = valid_record("2026-05-16_a", "targeted_review_x")
        record["evidence_direction"] = "refines"
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        self.assertTrue(
            any(c.startswith("schema:evidence_direction") for c in self.classes()),
            "a non-enum direction is ingested as 'unknown' and must be rejected")

    def test_confidence_out_of_range(self):
        record = valid_record("2026-05-16_a", "targeted_review_x")
        record["confidence"] = 1.4
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        self.assertTrue(any(c.startswith("schema:confidence") for c in self.classes()))

    def test_wrong_schema_version_const(self):
        record = valid_record("2026-05-16_a", "targeted_review_x")
        record["schema_version"] = "literature_evidence/v2"
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        self.assertTrue(any(c.startswith("schema:schema_version") for c in self.classes()))

    def test_duplicate_claim_ids_rejected(self):
        record = valid_record("2026-05-16_a", "targeted_review_x")
        record["claim_ids_tested"] = ["MECH-001", "MECH-001"]
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        self.assertTrue(any(c.startswith("schema:claim_ids_tested")
                            for c in self.classes()))

    def test_arity_variants_of_additional_properties_collapse_to_one_class(self):
        """The class label must not fragment by how many keys each record carried."""
        one = valid_record("2026-05-16_a", "targeted_review_x")
        one["source"]["note"] = "x"
        many = valid_record("2026-05-16_b", "targeted_review_x")
        many["source"].update({"note": "x", "zenodo": "y", "code_repository": "z"})
        self.write_entry("targeted_review_x", "2026-05-16_a", record=one)
        self.write_entry("targeted_review_x", "2026-05-16_b", record=many)
        found, _ = self.findings()
        schema_classes = {f.cls for f in found if f.cls.startswith("schema:")}
        self.assertEqual(
            schema_classes,
            {"schema:source: Additional properties are not allowed (...)"},
            "1-key and 3-key additionalProperties failures are ONE defect")
        # ...but the actual offending keys survive on the detail lines.
        details = " ".join(f.detail for f in found)
        self.assertIn("zenodo", details)


class StructuralCheckTest(LiteratureTreeTestCase):
    def test_literature_type_mismatch(self):
        record = valid_record("2026-05-16_a", "targeted_review_x")
        record["literature_type"] = "targeted_review_SOMETHING_ELSE"
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        self.assertIn("literature_type_mismatch", self.classes())

    def test_entry_id_mismatch(self):
        record = valid_record("2026-05-16_DIFFERENT", "targeted_review_x")
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        self.assertIn("entry_id_mismatch", self.classes())

    def test_summary_path_names_a_missing_file(self):
        self.write_entry("targeted_review_x", "2026-05-16_a", summary=False)
        self.assertIn("summary_missing", self.classes())

    def test_summary_path_pointing_at_a_present_alternate_name_passes(self):
        record = valid_record("2026-05-16_a", "targeted_review_x")
        record["summary_path"] = "notes.md"
        entry = self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        (entry / "notes.md").write_text("# notes\n")
        self.assertEqual(self.classes(), [])

    def test_absent_summary_path_is_a_schema_finding_and_still_stats_the_default(self):
        """The indexer DEFAULTS summary_path to summary.md, so both must be checked."""
        record = valid_record("2026-05-16_a", "targeted_review_x")
        del record["summary_path"]
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record,
                         summary=False)
        classes = self.classes()
        self.assertIn("schema:<root>: 'X' is a required property", classes)
        self.assertIn("summary_missing", classes)

    def test_unparseable_json(self):
        entry = self.write_entry("targeted_review_x", "2026-05-16_a")
        (entry / "record.json").write_text("{not json")
        self.assertEqual(self.classes(), ["unparseable_json"])

    def test_timestamp_not_rfc3339(self):
        """The schema's `format: date-time` is inert here; this check replaces it."""
        record = valid_record("2026-05-16_a", "targeted_review_x")
        record["timestamp_utc"] = "16 May 2026"
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        self.assertIn("timestamp_not_rfc3339", self.classes())

    def test_rfc3339_variants_accepted(self):
        for stamp in ("2026-05-16T10:00:00Z",
                      "2026-05-16T10:00:00.123Z",
                      "2026-05-16T10:00:00+01:00",
                      "2026-05-16t10:00:00z"):
            with self.subTest(stamp=stamp):
                record = valid_record("2026-05-16_a", "targeted_review_x")
                record["timestamp_utc"] = stamp
                self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
                self.assertNotIn("timestamp_not_rfc3339", self.classes())


class ReachabilityTest(LiteratureTreeTestCase):
    """The check nothing else in the repo makes: records the indexer never sees."""

    def test_record_nested_too_deep_under_entries_is_unreachable(self):
        # entries/<id>/<sub>/record.json -- matched by the indexer's glob but
        # dropped by its `entry_dir.parent.name != "entries"` guard.
        self.write_entry("targeted_review_x", "2026-05-16_a", subdir="extra")
        found, n_records = self.findings()
        self.assertIn("unreachable_record", {f.cls for f in found})
        self.assertEqual(n_records, 0, "an unreachable record is not ingested")

    def test_record_outside_any_entries_dir_is_unreachable(self):
        # A record.json at the literature_type root -- not matched by the glob
        # at all. This is the shape retired by REE_assembly e7e213dac5.
        root = self.lit / "targeted_review_x"
        root.mkdir(parents=True, exist_ok=True)
        (root / "record.json").write_text(
            json.dumps(valid_record("targeted_review_x", "targeted_review_x")))
        found, _ = self.findings()
        self.assertEqual([f.cls for f in found], ["unreachable_record"])

    def test_unreachable_is_reported_even_when_the_record_is_perfectly_valid(self):
        """The whole point: it looks fine, and contributes nothing.

        The misplaced record also empties its own entry directory, so the second
        reachability check fires too. Both are correct and both are about
        reachability -- what must NOT appear is a schema finding, because the
        record's content is flawless.
        """
        self.write_entry("targeted_review_x", "2026-05-16_a", subdir="extra")
        found, _ = self.findings()
        self.assertEqual(
            sorted({f.cls for f in found}),
            ["entry_dir_without_record", "unreachable_record"])
        self.assertFalse([f for f in found if f.cls.startswith("schema:")],
                         "the record is schema-valid; only reachability is wrong")

    def test_entry_dir_without_record(self):
        entry = self.lit / "targeted_review_x" / "entries" / "2026-05-16_a"
        entry.mkdir(parents=True)
        (entry / "summary.md").write_text("# orphan\n")
        self.assertEqual(self.classes(), ["entry_dir_without_record"])

    def test_reachable_record_is_not_flagged(self):
        self.write_entry("targeted_review_x", "2026-05-16_a")
        found, n_records = self.findings()
        self.assertNotIn("unreachable_record", {f.cls for f in found})
        self.assertEqual(n_records, 1)

    def test_ingested_predicate_matches_the_indexer_on_a_mixed_tree(self):
        self.write_entry("targeted_review_x", "2026-05-16_ok")
        self.write_entry("targeted_review_x", "2026-05-16_deep", subdir="extra")
        ingested, unreachable = V.iter_record_paths(self.lit)
        self.assertEqual([p.parent.name for p in ingested], ["2026-05-16_ok"])
        self.assertEqual([p.parent.name for p in unreachable], ["extra"])


class ScopeTest(LiteratureTreeTestCase):
    """--paths scoping, which is what makes a future blocking gate survivable."""

    def setUp(self):
        super().setUp()
        bad = valid_record("2026-05-16_bad", "targeted_review_x")
        bad["source"]["note"] = "undeclared"
        self.write_entry("targeted_review_x", "2026-05-16_good")
        self.write_entry("targeted_review_x", "2026-05-16_bad", record=bad)

    def _record(self, entry_id):
        return self.lit / "targeted_review_x" / "entries" / entry_id / "record.json"

    def test_unscoped_sees_both(self):
        found, n_records = self.findings()
        self.assertEqual(n_records, 2)
        self.assertEqual(len(found), 1)

    def test_scope_to_the_clean_record_reports_nothing(self):
        found, n_records = self.findings(scope=[self._record("2026-05-16_good")])
        self.assertEqual(found, [])
        self.assertEqual(n_records, 1)

    def test_scope_to_the_failing_record_reports_it(self):
        found, n_records = self.findings(scope=[self._record("2026-05-16_bad")])
        self.assertEqual(len(found), 1)
        self.assertEqual(n_records, 1)

    def test_a_non_record_entry_file_resolves_to_its_record(self):
        """The commit gate stages summary.md, not only record.json.

        A staged summary.md DELETION breaks the summary_path of a record that is
        not itself staged -- scoping to staged record.json files alone would miss
        exactly the defect the deletion caused.
        """
        summary = self._record("2026-05-16_bad").parent / "summary.md"
        resolved = V.resolve_scope_paths(self.tmp, [str(summary)])
        self.assertEqual(resolved, [self._record("2026-05-16_bad")])

    def test_repo_relative_and_absolute_inputs_agree(self):
        rel = ("evidence/literature/targeted_review_x/entries/"
               "2026-05-16_bad/summary.md")
        self.assertEqual(
            V.resolve_scope_paths(self.tmp, [rel]),
            V.resolve_scope_paths(self.tmp, [str(self.tmp / rel)]))

    def test_resolution_is_deduplicated_and_order_stable(self):
        entry = self._record("2026-05-16_bad").parent
        resolved = V.resolve_scope_paths(self.tmp, [
            str(entry / "summary.md"),
            str(entry / "record.json"),
            str(entry / "summary.md"),
        ])
        self.assertEqual(resolved, [self._record("2026-05-16_bad")])

    def test_a_record_outside_any_entries_dir_still_resolves_to_itself(self):
        """An unreachable record has no entry-directory ancestor to walk up to,
        and is precisely the case that must not be silently dropped."""
        stray = self.lit / "targeted_review_x" / "record.json"
        self.assertEqual(V.resolve_scope_paths(self.tmp, [str(stray)]), [stray])

    def test_a_literature_type_root_file_resolves_to_nothing(self):
        """A review-root summary.md implicates no single record -- and must not
        silently widen the scope to the whole corpus."""
        self.assertEqual(
            V.resolve_scope_paths(
                self.tmp,
                [str(self.lit / "targeted_review_x" / "summary.md")]),
            [])


class CliTest(LiteratureTreeTestCase):
    def _run(self, argv):
        out = io.StringIO()
        saved, sys.stdout = sys.stdout, out
        try:
            rc = V.main(argv)
        finally:
            sys.stdout = saved
        return rc, out.getvalue()

    def test_default_exits_zero_even_with_findings(self):
        """Chains safely -- same convention as audit_stashes/audit_vendored_copies."""
        record = valid_record("2026-05-16_a", "targeted_review_x")
        record["source"]["note"] = "undeclared"
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        rc, out = self._run(["--repo", str(self.tmp)])
        self.assertEqual(rc, 0)
        self.assertIn("1 finding(s)", out)

    def test_exit_nonzero_gates(self):
        record = valid_record("2026-05-16_a", "targeted_review_x")
        record["source"]["note"] = "undeclared"
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        rc, _ = self._run(["--repo", str(self.tmp), "--exit-nonzero"])
        self.assertEqual(rc, 1)

    def test_exit_nonzero_is_zero_on_a_clean_corpus(self):
        self.write_entry("targeted_review_x", "2026-05-16_a")
        rc, out = self._run(["--repo", str(self.tmp), "--exit-nonzero"])
        self.assertEqual(rc, 0)
        self.assertIn("OK", out)

    def test_empty_paths_is_a_noop_not_a_full_scan(self):
        """`--paths` with nothing staged must NOT fall through to the whole corpus."""
        record = valid_record("2026-05-16_a", "targeted_review_x")
        record["source"]["note"] = "undeclared"
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        rc, out = self._run(["--repo", str(self.tmp), "--exit-nonzero", "--paths"])
        self.assertEqual(rc, 0)
        self.assertIn("0 records in scope", out)

    def test_repo_relative_paths_are_resolved_against_repo(self):
        record = valid_record("2026-05-16_a", "targeted_review_x")
        record["source"]["note"] = "undeclared"
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        rel = "evidence/literature/targeted_review_x/entries/2026-05-16_a/record.json"
        rc, out = self._run(["--repo", str(self.tmp), "--exit-nonzero",
                             "--paths", rel])
        self.assertEqual(rc, 1)
        self.assertIn("1 finding(s)", out)

    def test_report_groups_by_class_not_one_line_per_record(self):
        for i in range(12):
            record = valid_record("2026-05-16_%02d" % i, "targeted_review_x")
            record["source"]["note"] = "undeclared"
            self.write_entry("targeted_review_x", "2026-05-16_%02d" % i, record=record)
        rc, out = self._run(["--repo", str(self.tmp)])
        self.assertEqual(rc, 0)
        self.assertIn("12  schema:source: Additional properties", out)
        self.assertIn("more (--list-failures for all)", out)
        self.assertLess(len(out.splitlines()), 20,
                        "12 failures must not print 12+ unabridged blocks")

    def test_list_failures_prints_them_all(self):
        for i in range(12):
            record = valid_record("2026-05-16_%02d" % i, "targeted_review_x")
            record["source"]["note"] = "undeclared"
            self.write_entry("targeted_review_x", "2026-05-16_%02d" % i, record=record)
        _, out = self._run(["--repo", str(self.tmp), "--list-failures"])
        for i in range(12):
            self.assertIn("2026-05-16_%02d" % i, out)

    def test_json_output_is_machine_readable(self):
        record = valid_record("2026-05-16_a", "targeted_review_x")
        record["source"]["note"] = "undeclared"
        self.write_entry("targeted_review_x", "2026-05-16_a", record=record)
        _, out = self._run(["--repo", str(self.tmp), "--json"])
        payload = json.loads(out)
        self.assertEqual(payload["records_checked"], 1)
        self.assertEqual(len(payload["findings"]), 1)
        self.assertEqual(payload["findings"][0]["class"],
                         "schema:source: Additional properties are not allowed (...)")

    def test_missing_literature_tree_is_not_a_crash(self):
        rc, out = self._run(["--repo", str(self.tmp)])
        self.assertEqual(rc, 0)
        self.assertIn("OK", out)


class DegradedValidatorTest(unittest.TestCase):
    """The draft-07 fallback is deliberate; the guard against it hiding a miss is not."""

    def test_validator_class_is_available(self):
        cls, name = V.get_validator_cls()
        self.assertIn(name, ("Draft202012Validator", "Draft7Validator"))

    def test_live_schema_uses_no_post_draft7_keyword(self):
        """If this fails, the draft-07 fallback has started silently under-checking."""
        schema = json.loads((REPO_ROOT / SCHEMA_REL).read_text())
        self.assertEqual(V.schema_needs_2020_12(schema), [])

    def test_post_draft7_keyword_is_refused_rather_than_ignored(self):
        _, name = V.get_validator_cls()
        if name == "Draft202012Validator":
            self.skipTest("installed jsonschema supports 2020-12; no degrade to guard")
        tmp = Path(tempfile.mkdtemp(prefix="ree_lit_validate_draft_"))
        self.addCleanup(shutil.rmtree, tmp, True)
        schema_dst = tmp / SCHEMA_REL
        schema_dst.parent.mkdir(parents=True, exist_ok=True)
        schema = json.loads((REPO_ROOT / SCHEMA_REL).read_text())
        schema["properties"]["tags"]["unevaluatedItems"] = False
        schema_dst.write_text(json.dumps(schema))
        (tmp / "evidence" / "literature").mkdir(parents=True, exist_ok=True)
        with self.assertRaises(SystemExit) as ctx:
            V.collect_findings(tmp)
        self.assertIn("unevaluatedItems", str(ctx.exception))


class LiveCorpusTest(unittest.TestCase):
    """One smoke test against the REAL corpus -- it must RUN, not that it is clean.

    Asserting a finding COUNT here would fail on every legitimate literature pull,
    which is how a check gets deleted. The baseline belongs in the commit message
    and the report, not in a test.

    NON-VACUITY (oracle-vacuity audit 2026-08-18). "It must run" is only
    meaningful if it ran over SOMETHING. The prior shape asserted `rc == 0` and
    that the output contained "validate_literature:", both of which hold on an
    EMPTY corpus -- measured GREEN under `iter_record_paths -> []` and
    `collect_findings -> ([], 0)`, i.e. it could not tell 2213 records from 0.
    The guard below therefore asserts the record COUNT is non-zero, which is a
    statement about coverage and NOT about cleanliness -- it stays true after
    every legitimate literature pull, however many findings that pull produces.
    """

    def test_runs_over_the_real_corpus_and_exits_zero(self):
        out = io.StringIO()
        saved, sys.stdout = sys.stdout, out
        try:
            rc = V.main(["--repo", str(REPO_ROOT)])
        finally:
            sys.stdout = saved
        text = out.getvalue()
        self.assertEqual(rc, 0, "default mode must exit 0 even with findings")
        self.assertIn("validate_literature:", text)

        # Non-vacuity guard. Both report branches name the record count:
        #   "OK (N records checked, 0 findings)"
        #   "K finding(s) in M of N record(s), ..."
        m = re.search(r"\((\d+) records checked", text) or \
            re.search(r"of (\d+) record\(s\)", text)
        self.assertIsNotNone(
            m, "could not read a record count out of the report; if the report "
               "format changed, re-point this guard rather than deleting it:\n%s"
               % text)
        self.assertGreater(
            int(m.group(1)), 0,
            "the live literature corpus resolved to ZERO records, so this smoke "
            "test asserted nothing. Either the tree moved or iter_record_paths "
            "stopped finding it -- do not soften this guard.")

    def test_the_live_corpus_is_actually_reachable(self):
        """Standalone coverage check, independent of the CLI's output format.

        Reads the count straight from collect_findings so a report-format change
        cannot silently disarm the guard above.
        """
        _findings, n_records = V.collect_findings(REPO_ROOT)
        self.assertGreater(
            n_records, 0,
            "collect_findings saw zero records under %s" % REPO_ROOT)


if __name__ == "__main__":
    unittest.main(verbosity=2)
