#!/usr/bin/env python3
"""Regression tests for check_unapplied_autopsy_recommendations.py (GOV-APPLY-1).

Hermetic and time-independent: every test builds a complete tmp REE_assembly
tree (`evidence/planning/failure_autopsy_*.json`, the run packs and their flat
siblings under `evidence/experiments/`, `claim_evidence.v1.json`, and a minimal
`docs/claims/claims.yaml`) and points `scan()` / `main()` at it via `--root`.
Nothing reads the real corpus, which moves under the tests daily.

WHAT THESE ARE PINNING
----------------------
The defect (diagnosed in `docs/plans/mech236_registry_integrity_20260819.md`):
`_reflects()` short-circuited True on a `live_status.evidence.from` prose
citation and never opened a manifest, while the indexer reads
`evidence_direction` off the MANIFEST. So a recommendation could be cited in
claims.yaml, unapplied where it counts, and certified applied here.

THE NEGATIVE CONTROLS ARE THE LOAD-BEARING HALF, and roughly half of these
tests are negative controls, because the failure mode of the fix is the mirror
image of the failure mode it repairs:

  * a genuinely-applied recommendation must NOT fire -- a detector that fires
    on applied work is noise, and an ignored report is the same failure as no
    report (this is the module's own stated design constraint, and the reason
    the 338-mismatch category-compare alternative was rejected);
  * `--strict`'s exit contract must be UNCHANGED by the new bucket, because
    governance.sh's Step 3h invocation and any CI gate predate it;
  * the direction vocabulary must track the INDEXER's, not a restated copy that
    drifts -- a direction missing here means silent under-reporting, which is
    the defect class this audit exists to catch;
  * scope must stay bounded: a claim the manifest does not tag, an unconfirmed
    autopsy, and a superseded adjudication must all stay out.

Run: /opt/local/bin/python3 scripts/test_check_unapplied_autopsy_recommendations.py
"""

import importlib.util
import io
import json
import re
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parent


def _load_module(name, filename):
    path = SCRIPTS_DIR / filename
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


M = _load_module("ree_check_unapplied_autopsy_recommendations",
                 "check_unapplied_autopsy_recommendations.py")

RUN = "v3_exq_914_mech236_channel_ablation_20260811T065911Z_v3"
TYPE = "v3_exq_914_mech236_channel_ablation"
CLAIM = "MECH-236"
SLUG = "failure_autopsy_V3-EXQ-914a_2026-08-13"


class Fixture:
    """A tmp REE_assembly tree built one piece at a time."""

    def __init__(self, root: Path):
        self.root = root
        self.planning = root / "evidence" / "planning"
        self.experiments = root / "evidence" / "experiments"
        self.planning.mkdir(parents=True)
        self.experiments.mkdir(parents=True)
        (root / "docs" / "claims").mkdir(parents=True)
        self._live = []
        self.write_claims([{"id": CLAIM, "status": "candidate"}])

    # ---- autopsy artifacts -------------------------------------------------
    def autopsy(self, slug=SLUG, status="confirmed", generated="2026-08-13T04:52:40Z",
                targets=None):
        (self.planning / ("%s.json" % slug)).write_text(json.dumps({
            "status": status, "generated_utc": generated,
            "targets": targets or [],
        }, indent=1))

    @staticmethod
    def target(run_id=RUN, claim_ids=(CLAIM,), recommended="non_contributory",
               per_claim=None, per_claim_recommendation=None):
        t = {"run_id": run_id, "claim_ids": list(claim_ids)}
        if recommended is not None:
            t["recommended_evidence_direction"] = recommended
        if per_claim:
            t["recommended_evidence_direction_per_claim"] = per_claim
        if per_claim_recommendation:
            t["per_claim_recommendation"] = per_claim_recommendation
        return t

    # ---- manifests ---------------------------------------------------------
    def pack(self, run_id=RUN, exp_type=TYPE, direction="weakens",
             claim_ids=(CLAIM,), note=None, per_claim=None, claims_key="claim_ids_tested"):
        d = self.experiments / exp_type / "runs" / run_id
        d.mkdir(parents=True, exist_ok=True)
        body = {"run_id": run_id, "evidence_direction": direction,
                claims_key: list(claim_ids)}
        if note:
            body["evidence_direction_note"] = note
        if per_claim is not None:
            body["evidence_direction_per_claim"] = per_claim
        (d / "manifest.json").write_text(json.dumps(body, indent=1))

    def flat(self, run_id=RUN, direction="weakens", claim_ids=(CLAIM,), note=None,
             per_claim=None, filename=None, exp_type=None, dry_run=None):
        body = {"run_id": run_id, "evidence_direction": direction,
                "claim_ids": list(claim_ids)}
        if dry_run is not None:
            body["dry_run"] = dry_run
        if note:
            body["evidence_direction_note"] = note
        if per_claim is not None:
            body["evidence_direction_per_claim"] = per_claim
        name = filename or ("%s.json" % run_id)
        target_dir = self.experiments if exp_type is None else self.experiments / exp_type
        target_dir.mkdir(parents=True, exist_ok=True)
        (target_dir / name).write_text(json.dumps(body, indent=1))

    # ---- derived index -----------------------------------------------------
    def live(self, claim_id=CLAIM, run_id=RUN, scoring_excluded=None):
        self._live.append({"claim_id": claim_id, "run_id": run_id,
                           "source_type": "experimental",
                           "scoring_excluded": scoring_excluded})

    def write_claim_evidence(self, present=True):
        if not present:
            return
        (self.experiments / "claim_evidence.v1.json").write_text(
            json.dumps({"entries": self._live}, indent=1))

    def write_claims(self, claims):
        import yaml
        (self.root / "docs" / "claims" / "claims.yaml").write_text(
            yaml.safe_dump({"claims": claims}))


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.fx = Fixture(Path(self.tmp.name))
        self.addCleanup(self.tmp.cleanup)

    def scan(self, write_evidence=True):
        self.fx.write_claim_evidence(write_evidence)
        return M.scan(self.fx.root)

    def directions(self, **kw):
        return self.scan(**kw)["unapplied_evidence_direction"]

    def live_rows(self, **kw):
        return [d for d in self.directions(**kw) if d["live"]]

    def run_main(self, *argv):
        self.fx.write_claim_evidence(True)
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = self._main(argv)
        return rc, buf.getvalue()

    def _main(self, argv):
        old = sys.argv
        sys.argv = ["check_unapplied_autopsy_recommendations.py",
                    "--root", str(self.fx.root)] + list(argv)
        try:
            return M.main()
        finally:
            sys.argv = old


# =========================================================================
# THE DEFECT -- prose citation vs the manifest
# =========================================================================
class ProseCitationTests(Base):

    def test_prose_citation_alone_does_not_certify_application(self):
        """MECH-236, exactly: claims.yaml cites the autopsy, the manifest still
        scores `weakens`. The old code returned True here and reported 0 hits."""
        self.fx.write_claims([{
            "id": CLAIM, "status": "candidate",
            "live_status": {"reading": "candidate",
                            "evidence": {"from": SLUG,
                                         "verdict": "non_contributory -- ..."}},
        }])
        self.fx.autopsy(targets=[self.fx.target(
            per_claim_recommendation={CLAIM: {
                "change": "weakens -> non_contributory",
                "recommended_evidence_direction": "non_contributory"}})])
        self.fx.pack(direction="weakens")
        self.fx.live()
        buckets = self.scan()
        self.assertEqual([r["claim_id"] for r in buckets["unapplied_disposition"]],
                         [CLAIM])
        self.assertEqual(len(buckets["unapplied_evidence_direction"]), 1)

    def test_applied_manifest_does_not_fire_even_without_a_citation(self):
        """NEGATIVE CONTROL, and the load-bearing one: the recommendation IS
        applied on the manifest, so nothing fires -- regardless of what prose
        claims.yaml does or does not carry."""
        self.fx.autopsy(targets=[self.fx.target(
            per_claim_recommendation={CLAIM: {
                "change": "weakens -> non_contributory",
                "recommended_evidence_direction": "non_contributory"}})])
        self.fx.pack(direction="non_contributory")
        self.fx.live()
        buckets = self.scan()
        self.assertEqual(buckets["unapplied_disposition"], [])
        self.assertEqual(buckets["unapplied_evidence_direction"], [])

    def test_claims_yaml_still_authoritative_for_category_dispositions(self):
        """NEGATIVE CONTROL: a non-direction disposition is a claims.yaml fact,
        and must still be answered from claims.yaml rather than a manifest."""
        self.fx.write_claims([{"id": CLAIM, "epistemic_category": "standard"}])
        self.fx.autopsy(targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {
                "change": "unset -> standard"}})])
        self.fx.pack(direction="weakens")
        self.assertEqual(self.scan()["unapplied_disposition"], [])

    def test_category_disposition_fires_when_claims_yaml_lacks_it(self):
        self.fx.write_claims([{"id": CLAIM, "epistemic_category": "substrate_ceiling"}])
        self.fx.autopsy(targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {"change": "unset -> standard"}})])
        self.fx.pack(direction="weakens")
        self.assertEqual(len(self.scan()["unapplied_disposition"]), 1)


# =========================================================================
# NAMED-FIELD / CITATION-STAMP SHAPES -- the 2026-08-29 repair
#
# governance-cycle-20260828 measured 10 confirmed-applied recommendations
# still reporting ACTIONABLE because `_target_state`'s derived value could
# never match one of the three hardcoded fields the old `_reflects` checked.
# Each class below is one of the shapes that produced a false positive on
# the real corpus (MECH-357, MECH-489, MECH-180/INV-050), reproduced here as
# a hermetic fixture, plus the negative controls that must still fire.
# =========================================================================
class NamedFieldAndCitationTests(Base):

    def test_colon_field_value_fires_when_unapplied(self):
        """MECH-357 shape: '... -> diagnostic_evidence_adjudicated: true'.
        Field present but wrong value -- still ACTIONABLE."""
        self.fx.write_claims([{"id": CLAIM, "diagnostic_evidence_adjudicated": False}])
        self.fx.autopsy(targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {
                "change": "no diagnostic_evidence_adjudicated field, so set one "
                          "-> diagnostic_evidence_adjudicated: true"}})])
        self.assertEqual(len(self.scan()["unapplied_disposition"]), 1)

    def test_colon_field_value_does_not_fire_once_applied(self):
        """NEGATIVE CONTROL, the load-bearing half of the MECH-357 fix: the
        claim's boolean field already matches -- nothing owed."""
        self.fx.write_claims([{"id": CLAIM, "diagnostic_evidence_adjudicated": True}])
        self.fx.autopsy(targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {
                "change": "no diagnostic_evidence_adjudicated field, so set one "
                          "-> diagnostic_evidence_adjudicated: true"}})])
        self.assertEqual(self.scan()["unapplied_disposition"], [])

    def test_colon_field_value_with_unrecognised_field_stays_actionable(self):
        """NEGATIVE CONTROL: a colon-shape clause naming a field the claim
        schema does not carry must not certify -- the false-positive bias is
        preserved for anything this cannot verify."""
        self.fx.write_claims([{"id": CLAIM}])
        self.fx.autopsy(targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {
                "change": "-> some_unmodeled_field: true"}})])
        self.assertEqual(len(self.scan()["unapplied_disposition"]), 1)

    def test_bare_boolean_field_fires_when_unapplied(self):
        """MECH-489 shape: 'pending_retest_after_substrate true -> false',
        no colon. Claim still carries the old value -- ACTIONABLE."""
        self.fx.write_claims([{"id": CLAIM, "pending_retest_after_substrate": True}])
        self.fx.autopsy(targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {
                "change": "pending_retest_after_substrate true -> false"}})])
        self.assertEqual(len(self.scan()["unapplied_disposition"]), 1)

    def test_bare_boolean_field_does_not_fire_once_applied(self):
        """NEGATIVE CONTROL, the load-bearing half of the MECH-489 fix."""
        self.fx.write_claims([{"id": CLAIM, "pending_retest_after_substrate": False}])
        self.fx.autopsy(targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {
                "change": "pending_retest_after_substrate true -> false"}})])
        self.assertEqual(self.scan()["unapplied_disposition"], [])

    def test_bare_boolean_shape_does_not_misattribute_to_the_first_word(self):
        """NEGATIVE CONTROL pinning the REJECTED alternative from the module
        docstring: 'status and epistemic_category unchanged -> standard'
        must not be checked against `status` (the first word) alone --
        `status` never holds a value like 'standard' and a single-field
        guess would wrongly stay ACTIONABLE forever. The widened blind
        field list must still find it via `epistemic_category`."""
        self.fx.write_claims([{"id": CLAIM, "status": "candidate",
                               "epistemic_category": "standard"}])
        self.fx.autopsy(targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {
                "change": "status and epistemic_category unchanged -> standard"}})])
        self.assertEqual(self.scan()["unapplied_disposition"], [])

    def test_citation_stamp_fires_when_unapplied(self):
        """MECH-180/INV-050 shape: '... stamp this cluster artifact ->
        failure_autopsy_X' naming a live_status.evidence.from target that
        the claim does not yet cite."""
        self.fx.write_claims([{
            "id": CLAIM,
            "live_status": {"evidence": {"from": "failure_autopsy_OLDER_2026-08-01"}},
        }])
        self.fx.autopsy(targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {
                "change": "currently cites failure_autopsy_OLDER_2026-08-01, "
                          "stamp this cluster artifact -> failure_autopsy_NEWER_2026-08-20"}})])
        self.assertEqual(len(self.scan()["unapplied_disposition"]), 1)

    def test_citation_stamp_does_not_fire_once_applied(self):
        """NEGATIVE CONTROL, the load-bearing half of the MECH-180/INV-050
        fix: live_status.evidence.from already cites the recommended slug."""
        self.fx.write_claims([{
            "id": CLAIM,
            "live_status": {"evidence": {"from": "failure_autopsy_NEWER_2026-08-20"}},
        }])
        self.fx.autopsy(targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {
                "change": "currently cites failure_autopsy_OLDER_2026-08-01, "
                          "stamp this cluster artifact -> failure_autopsy_NEWER_2026-08-20"}})])
        self.assertEqual(self.scan()["unapplied_disposition"], [])

    def test_stale_citation_stamp_moves_to_superseded_once_the_latest_applies(self):
        """THE EXACT MECH-180/INV-050 shape: three confirmed autopsies, each
        recommending a citation stamp naming itself, chained across three
        different runs. Only the latest is applied. The two older ones must
        move to superseded_disposition (WARN), not stay unapplied_disposition
        (ACTIONABLE) -- they are moot, not owed."""
        self.fx.write_claims([{
            "id": CLAIM,
            "live_status": {"evidence": {"from": "failure_autopsy_LATEST_2026-08-25"}},
        }])
        self.fx.autopsy(
            slug="failure_autopsy_OLDEST_2026-08-21", generated="2026-08-21T00:00:00Z",
            targets=[self.fx.target(
                run_id="run_a_v3", recommended=None,
                per_claim_recommendation={CLAIM: {
                    "change": "currently cites failure_autopsy_PRIOR_2026-08-01, "
                              "stamp this artifact -> failure_autopsy_OLDEST_2026-08-21"}})])
        self.fx.autopsy(
            slug="failure_autopsy_MIDDLE_2026-08-23", generated="2026-08-23T00:00:00Z",
            targets=[self.fx.target(
                run_id="run_b_v3", recommended=None,
                per_claim_recommendation={CLAIM: {
                    "change": "currently cites failure_autopsy_OLDEST_2026-08-21, "
                              "stamp this cluster artifact -> failure_autopsy_MIDDLE_2026-08-23"}})])
        self.fx.autopsy(
            slug="failure_autopsy_LATEST_2026-08-25", generated="2026-08-25T00:00:00Z",
            targets=[self.fx.target(
                run_id="run_c_v3", recommended=None,
                per_claim_recommendation={CLAIM: {
                    "change": "-> stamp failure_autopsy_LATEST_2026-08-25 as the final "
                              "citation for this portfolio"}})])
        buckets = self.scan()
        self.assertEqual(buckets["unapplied_disposition"], [])
        self.assertEqual(len(buckets["superseded_disposition"]), 2)
        self.assertEqual(
            {row["artifact"] for row in buckets["superseded_disposition"]},
            {"failure_autopsy_OLDEST_2026-08-21", "failure_autopsy_MIDDLE_2026-08-23"})

    def test_citation_stamp_with_no_live_status_stays_actionable(self):
        """NEGATIVE CONTROL: no live_status at all -- cannot verify, so it
        must not certify."""
        self.fx.write_claims([{"id": CLAIM}])
        self.fx.autopsy(targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {
                "change": "stamp this artifact -> failure_autopsy_NEWER_2026-08-20"}})])
        self.assertEqual(len(self.scan()["unapplied_disposition"]), 1)

    def test_bare_field_name_fires_when_unapplied(self):
        """MECH-135/INV-088 shape (failure_autopsy_V3-EXQ-954_2026-08-29):
        '... and set the flag the claim does not yet carry ->
        diagnostic_evidence_adjudicated' -- a bare field NAME with no colon
        and no value at all. Claim does not carry the flag -- ACTIONABLE."""
        self.fx.write_claims([{"id": CLAIM}])
        self.fx.autopsy(targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {
                "change": "set the flag the claim does not yet carry -> "
                          "diagnostic_evidence_adjudicated"}})])
        self.assertEqual(len(self.scan()["unapplied_disposition"]), 1)

    def test_bare_field_name_does_not_fire_once_applied(self):
        """NEGATIVE CONTROL, the load-bearing half of the bare-field-name fix
        and the exact real-corpus case (MECH-135, INV-088 both carry
        diagnostic_evidence_adjudicated: true on origin/master cdd772b0dd)."""
        self.fx.write_claims([{"id": CLAIM, "diagnostic_evidence_adjudicated": True}])
        self.fx.autopsy(targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {
                "change": "set the flag the claim does not yet carry -> "
                          "diagnostic_evidence_adjudicated"}})])
        self.assertEqual(self.scan()["unapplied_disposition"], [])

    def test_bare_field_name_stays_actionable_when_field_still_false(self):
        """NEGATIVE CONTROL: the field is present but still false -- must not
        be conflated with 'field absent' (both fall through to not-reflected
        the same way, but this pins the explicit-value case too)."""
        self.fx.write_claims([{"id": CLAIM, "diagnostic_evidence_adjudicated": False}])
        self.fx.autopsy(targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {
                "change": "set the flag -> diagnostic_evidence_adjudicated"}})])
        self.assertEqual(len(self.scan()["unapplied_disposition"]), 1)

    def test_bare_unrecognised_word_does_not_get_treated_as_a_field_name(self):
        """NEGATIVE CONTROL: a bare tail that is not one of the three boolean
        fields must not be promoted to a named-field comparison -- it stays
        on the pre-existing blind `_GENERIC_CLAIM_FIELDS` compare, which
        cannot match a claim carrying none of those fields."""
        self.fx.write_claims([{"id": CLAIM}])
        self.fx.autopsy(targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {
                "change": "-> some_unmodeled_bare_field"}})])
        self.assertEqual(len(self.scan()["unapplied_disposition"]), 1)

    def test_bare_epistemic_category_or_status_is_not_treated_as_implied_true(self):
        """NEGATIVE CONTROL: `_BOOLEAN_CLAIM_FIELDS` deliberately excludes
        epistemic_category/status -- a bare mention of either must not be
        read as an implied `true` (neither is boolean), so it must fall
        through to the blind compare exactly as before this fix."""
        self.fx.write_claims([{"id": CLAIM, "status": "candidate"}])
        self.fx.autopsy(targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {"change": "-> status"}})])
        self.assertEqual(len(self.scan()["unapplied_disposition"]), 1)


# =========================================================================
# THE 2026-09-01 REPAIR -- coincidental arrows, compound dispositions
#
# Shape A: a coincidental "->" (real prose, not the disposition marker) or a
# trailing clause after the real one hides the true target. Shape B: a
# disposition names TWO field changes and the free prose only carries an
# arrow for one of them. See the module docstring's "THE 2026-09-01 REPAIR"
# section for the real-corpus rows (ARC-045/SD-017/SD-078/SD-082/MECH-439,
# MECH-135/INV-088, MECH-482) each shape below reproduces.
# =========================================================================
class ClauseAndSetFieldTests(Base):

    def test_clause_narrowing_fires_when_the_real_target_is_unapplied(self):
        """ARC-045 shape: 'Withdraw weakens -> non_contributory. Nothing
        storable moves -- apply the corrected note' -- the old tail-extraction
        ran to the end of the sentence; narrowing to the immediate clause
        recovers 'non_contributory' as the real target."""
        self.fx.autopsy(targets=[self.fx.target(
            per_claim_recommendation={CLAIM: {
                "change": "Withdraw weakens -> non_contributory. Nothing "
                          "storable moves -- apply the corrected note",
                "recommended_evidence_direction": "non_contributory"}})])
        self.fx.pack(direction="weakens")
        self.assertEqual(len(self.scan()["unapplied_disposition"]), 1)

    def test_clause_narrowing_does_not_fire_once_applied(self):
        """NEGATIVE CONTROL, the load-bearing half."""
        self.fx.autopsy(targets=[self.fx.target(
            per_claim_recommendation={CLAIM: {
                "change": "Withdraw weakens -> non_contributory. Nothing "
                          "storable moves -- apply the corrected note",
                "recommended_evidence_direction": "non_contributory"}})])
        self.fx.pack(direction="non_contributory")
        self.assertEqual(self.scan()["unapplied_disposition"], [])

    def test_set_field_pattern_fires_when_unapplied(self):
        """SD-078/SD-082 shape: '-> set pending_retest_after_substrate
        false', a 'set ' prefix the bare-field-name match does not strip."""
        self.fx.write_claims([{"id": CLAIM, "pending_retest_after_substrate": True}])
        self.fx.autopsy(targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {
                "change": "the retest has now run -> set "
                          "pending_retest_after_substrate false"}})])
        self.assertEqual(len(self.scan()["unapplied_disposition"]), 1)

    def test_set_field_pattern_does_not_fire_once_applied(self):
        """NEGATIVE CONTROL, the load-bearing half."""
        self.fx.write_claims([{"id": CLAIM, "pending_retest_after_substrate": False}])
        self.fx.autopsy(targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {
                "change": "the retest has now run -> set "
                          "pending_retest_after_substrate false"}})])
        self.assertEqual(self.scan()["unapplied_disposition"], [])

    def test_coincidental_arrow_does_not_get_misread_as_the_disposition(self):
        """SD-017 shape: a scientific-notation arrow ('slot_cosine_sim ->
        1.0') appears LATER in the sentence than the real verdict and is
        the one `_target_state` would naively pick up. The prose-parse
        route must fail to produce anything checkable here -- this is
        pinning the NEGATIVE half (garbled tail stays unmatched by the
        prose route); the structured-fallback tests below cover recovery."""
        self.fx.write_claims([{"id": CLAIM, "epistemic_category": "substrate_ceiling",
                               "pending_retest_after_substrate": True}])
        self.fx.autopsy(targets=[self.fx.target(
            per_claim_recommendation={CLAIM: {
                "change": "own stated prediction (undifferentiated, ratio -> "
                          "1.0) is CONFIRMED by X = 0.9993; the manifest's "
                          "weakens is withdrawn. Category already substrate_"
                          "ceiling and status already stable, nothing "
                          "storable moves -- apply the corrected note",
                "recommended_evidence_direction": "non_contributory"}})])
        self.fx.pack(direction="weakens")
        # Not applied on the manifest -- must still be ACTIONABLE, not
        # silently miscertified via the coincidental arrow's garbage tail.
        self.assertEqual(len(self.scan()["unapplied_disposition"]), 1)

    def test_structured_fallback_certifies_a_coincidental_arrow_once_all_fields_agree(self):
        """THE FIX for the case above: once the manifest AND the structured
        `recommended_epistemic_category` / `pending_retest_after_substrate`
        fields on `rec` all agree with current state, the last-resort
        structured check certifies -- even though the prose route alone
        never parses a checkable value out of this text."""
        self.fx.write_claims([{"id": CLAIM, "epistemic_category": "substrate_ceiling",
                               "pending_retest_after_substrate": True}])
        self.fx.autopsy(targets=[self.fx.target(
            per_claim_recommendation={CLAIM: {
                "change": "own stated prediction (undifferentiated, ratio -> "
                          "1.0) is CONFIRMED by X = 0.9993; the manifest's "
                          "weakens is withdrawn. Category already substrate_"
                          "ceiling and status already stable, nothing "
                          "storable moves -- apply the corrected note",
                "recommended_evidence_direction": "non_contributory",
                "recommended_epistemic_category": "substrate_ceiling",
                "pending_retest_after_substrate": True}})])
        self.fx.pack(direction="non_contributory")
        self.assertEqual(self.scan()["unapplied_disposition"], [])

    def test_structured_fallback_stays_actionable_if_any_present_field_disagrees(self):
        """NEGATIVE CONTROL: the fallback requires ALL present structured
        fields to agree, not just the direction."""
        self.fx.write_claims([{"id": CLAIM, "epistemic_category": "standard",
                               "pending_retest_after_substrate": True}])
        self.fx.autopsy(targets=[self.fx.target(
            per_claim_recommendation={CLAIM: {
                "change": "own stated prediction (undifferentiated, ratio -> "
                          "1.0) is CONFIRMED by X = 0.9993; the manifest's "
                          "weakens is withdrawn. Category already substrate_"
                          "ceiling and status already stable, nothing "
                          "storable moves -- apply the corrected note",
                "recommended_evidence_direction": "non_contributory",
                "recommended_epistemic_category": "substrate_ceiling",
                "pending_retest_after_substrate": True}})])
        self.fx.pack(direction="non_contributory")
        self.assertEqual(len(self.scan()["unapplied_disposition"]), 1)

    def test_structured_fallback_does_not_layer_onto_an_already_successful_prose_match(self):
        """NEGATIVE CONTROL replicating the ORIGINAL V3-EXQ-604c/MECH-314b
        case this audit was built from: the prose ALREADY certifies via a
        clean direction match, and `recommended_epistemic_category` on the
        SAME rec disagrees with current state (legitimately superseded by
        independent, later governance work outside the autopsy pipeline).
        Requiring agreement here regressed 22 real corpus rows when tried."""
        self.fx.write_claims([{"id": CLAIM, "epistemic_category": "standard"}])
        self.fx.autopsy(targets=[self.fx.target(
            per_claim_recommendation={CLAIM: {
                "change": "mixed -> non_contributory",
                "recommended_evidence_direction": "non_contributory",
                "recommended_epistemic_category": "substrate_ceiling",
                "pending_retest_after_substrate": True}})])
        self.fx.pack(direction="non_contributory")
        self.assertEqual(self.scan()["unapplied_disposition"], [])

    def test_self_referential_stamp_fires_when_unapplied(self):
        """MECH-439/571b shape: 'must clear via the provenance stamp
        (live_status.evidence.from -> this artifact) rather than by a field
        match' -- names no literal slug because it means the recommending
        autopsy itself."""
        self.fx.write_claims([{
            "id": CLAIM,
            "live_status": {"evidence": {"from": "failure_autopsy_OLDER_2026-08-01"}},
        }])
        self.fx.autopsy(targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {
                "change": "must clear via the provenance stamp "
                          "(live_status.evidence.from -> this artifact) "
                          "rather than by a field match"}})])
        self.assertEqual(len(self.scan()["unapplied_disposition"]), 1)

    def test_self_referential_stamp_does_not_fire_once_applied(self):
        """NEGATIVE CONTROL, the load-bearing half: live_status.evidence.from
        already cites the RECOMMENDING autopsy's own slug."""
        self.fx.write_claims([{
            "id": CLAIM,
            "live_status": {"evidence": {"from": SLUG}},
        }])
        self.fx.autopsy(slug=SLUG, targets=[self.fx.target(
            recommended=None,
            per_claim_recommendation={CLAIM: {
                "change": "must clear via the provenance stamp "
                          "(live_status.evidence.from -> this artifact) "
                          "rather than by a field match"}})])
        self.assertEqual(self.scan()["unapplied_disposition"], [])

    def test_missing_epistemic_category_fires_even_when_the_prose_matches_a_different_field(self):
        """MECH-135/INV-088 shape (failure_autopsy_V3-EXQ-954_2026-08-29):
        `change` ends in a bare boolean field the claim already carries, but
        `recommended_epistemic_category` on the SAME rec names a field the
        claim has never carried at all -- ACTIONABLE regardless of the
        boolean match."""
        self.fx.write_claims([{"id": CLAIM, "diagnostic_evidence_adjudicated": True}])
        self.fx.autopsy(targets=[self.fx.target(
            per_claim_recommendation={CLAIM: {
                "change": "set the flag the claim does not yet carry -> "
                          "diagnostic_evidence_adjudicated",
                "recommended_evidence_direction": "non_contributory",
                "recommended_epistemic_category": "standard"}})])
        self.fx.pack(direction="non_contributory")
        self.assertEqual(len(self.scan()["unapplied_disposition"]), 1)

    def test_missing_epistemic_category_does_not_fire_once_backfilled(self):
        """NEGATIVE CONTROL, the load-bearing half: the exact real-corpus
        fix (REE_assembly 80f9a4bc5f backfilled INV-088's epistemic_category
        a day after this shape first shipped undetected)."""
        self.fx.write_claims([{"id": CLAIM, "diagnostic_evidence_adjudicated": True,
                               "epistemic_category": "standard"}])
        self.fx.autopsy(targets=[self.fx.target(
            per_claim_recommendation={CLAIM: {
                "change": "set the flag the claim does not yet carry -> "
                          "diagnostic_evidence_adjudicated",
                "recommended_evidence_direction": "non_contributory",
                "recommended_epistemic_category": "standard"}})])
        self.fx.pack(direction="non_contributory")
        self.assertEqual(self.scan()["unapplied_disposition"], [])

    def test_present_but_different_epistemic_category_is_not_gated_as_missing(self):
        """NEGATIVE CONTROL, the OTHER load-bearing half: a claim that
        ALREADY carries epistemic_category, even holding a value DIFFERENT
        from `recommended_epistemic_category`, must not be gated the same
        way an ABSENT field is -- that is the disagreement-vs-absence
        distinction the module docstring measures at 22 false positives."""
        self.fx.write_claims([{"id": CLAIM, "diagnostic_evidence_adjudicated": True,
                               "epistemic_category": "substrate_ceiling"}])
        self.fx.autopsy(targets=[self.fx.target(
            per_claim_recommendation={CLAIM: {
                "change": "set the flag the claim does not yet carry -> "
                          "diagnostic_evidence_adjudicated",
                "recommended_evidence_direction": "non_contributory",
                "recommended_epistemic_category": "standard"}})])
        self.fx.pack(direction="non_contributory")
        self.assertEqual(self.scan()["unapplied_disposition"], [])

    def test_missing_pending_retest_after_substrate_is_not_gated(self):
        """NEGATIVE CONTROL: `pending_retest_after_substrate` is deliberately
        EXCLUDED from the absent-field gate (measured corpus-wide: 12 of 13
        false positives from gating it were this field, on claims that had
        simply never carried the key at all)."""
        self.fx.write_claims([{"id": CLAIM, "diagnostic_evidence_adjudicated": True,
                               "epistemic_category": "standard"}])
        self.fx.autopsy(targets=[self.fx.target(
            per_claim_recommendation={CLAIM: {
                "change": "set the flag the claim does not yet carry -> "
                          "diagnostic_evidence_adjudicated",
                "recommended_evidence_direction": "non_contributory",
                "recommended_epistemic_category": "standard",
                "pending_retest_after_substrate": True}})])
        self.fx.pack(direction="non_contributory")
        self.assertEqual(self.scan()["unapplied_disposition"], [])


# =========================================================================
# CROSS-RUN SUPERSESSION -- GOV-APPLY-1's own blind spot (2026-08-22)
#
# R2 (load_confirmed's `latest`) only dedups a re-adjudication of the SAME
# run_id. A claim re-adjudicated across a DIFFERENT run was invisible to
# that dedup, so an older per-claim disposition kept being compared against
# claims.yaml's CURRENT state -- which, correctly, reflects the LATER
# recommendation -- and reported ACTIONABLE forever. Real incident: 436e
# (run A) recommended `epistemic_category unset -> standard` for
# ARC-045/MECH-166/SD-017; 436f (run B, later) recommended
# `standard -> substrate_ceiling` instead; claims.yaml carries
# substrate_ceiling. 436e's stale disposition never applies and never can.
# =========================================================================
class CrossRunSupersessionTests(Base):

    OLDER = "failure_autopsy_older_2026-08-13"
    NEWER = "failure_autopsy_newer_2026-08-16"

    def _two_runs(self, older_change, newer_change, claim_epistemic_category=None):
        claim = {"id": CLAIM}
        if claim_epistemic_category is not None:
            claim["epistemic_category"] = claim_epistemic_category
        self.fx.write_claims([claim])
        self.fx.autopsy(
            slug=self.OLDER, generated="2026-08-13T04:19:12Z",
            targets=[self.fx.target(
                run_id="run_older_v3", recommended=None,
                per_claim_recommendation={CLAIM: {"change": older_change}})])
        self.fx.autopsy(
            slug=self.NEWER, generated="2026-08-16T18:24:28Z",
            targets=[self.fx.target(
                run_id="run_newer_v3", recommended=None,
                per_claim_recommendation={CLAIM: {"change": newer_change}})])

    def test_older_disagreeing_disposition_moves_to_superseded_when_later_is_applied(self):
        """THE FIX, replicating the real 436e/436f/ARC-045 shape exactly: two
        DIFFERENT runs, a later disagreeing recommendation, claims.yaml
        already reflecting the later one. Fails on the pre-fix code (the
        older disposition was reported unapplied forever)."""
        self._two_runs("unset -> standard", "standard -> substrate_ceiling",
                        claim_epistemic_category="substrate_ceiling")
        buckets = self.scan()
        self.assertEqual(buckets["unapplied_disposition"], [])
        superseded = buckets["superseded_disposition"]
        self.assertEqual(len(superseded), 1)
        self.assertEqual(superseded[0]["claim_id"], CLAIM)
        self.assertEqual(superseded[0]["artifact"], self.OLDER)
        self.assertEqual(superseded[0]["superseded_by"], self.NEWER)

    def test_older_disposition_stays_actionable_when_later_is_also_unapplied(self):
        """NEGATIVE CONTROL, and the load-bearing one (mirrors Q-044 /
        MECH-314b / MECH-314c from failure_autopsy_V3-EXQ-604c_2026-07-20,
        which must keep firing): a later recommendation existing is not
        enough to silence the older one -- it must actually be APPLIED.
        Neither is here, so both stay ACTIONABLE."""
        self._two_runs("unset -> standard", "standard -> substrate_ceiling",
                        claim_epistemic_category=None)
        buckets = self.scan()
        self.assertEqual(len(buckets["unapplied_disposition"]), 2)
        self.assertEqual(buckets["superseded_disposition"], [])

    def test_older_disposition_agreeing_with_latest_is_not_marked_superseded(self):
        """NEGATIVE CONTROL: supersession requires a DISAGREEING later
        recommendation. Two runs recommending the identical change are not a
        contradiction, so neither is demoted to the WARN bucket -- both stay
        ACTIONABLE until the (shared) target state is actually applied."""
        self._two_runs("unset -> standard", "unset -> standard",
                        claim_epistemic_category=None)
        buckets = self.scan()
        self.assertEqual(len(buckets["unapplied_disposition"]), 2)
        self.assertEqual(buckets["superseded_disposition"], [])

    def test_same_run_r2_dedup_is_unaffected(self):
        """NEGATIVE CONTROL: a re-adjudication of the SAME run still goes
        through the pre-existing R2 path (load_confirmed's `latest`), never
        the new cross-run one -- the superseded artifact is dropped before
        per_claim_recommendation is even read, so it produces neither an
        unapplied_disposition nor a superseded_disposition row."""
        self.fx.autopsy(slug="failure_autopsy_old_2026-01-01",
                        generated="2026-01-01T00:00:00Z",
                        targets=[self.fx.target(
                            recommended=None,
                            per_claim_recommendation={CLAIM: {"change": "unset -> standard"}})])
        self.fx.autopsy(slug="failure_autopsy_new_2026-08-13",
                        generated="2026-08-13T00:00:00Z",
                        targets=[self.fx.target(
                            recommended=None,
                            per_claim_recommendation={CLAIM: {"change": "standard -> substrate_ceiling"}})])
        self.fx.write_claims([{"id": CLAIM, "epistemic_category": "substrate_ceiling"}])
        buckets = self.scan()
        self.assertEqual(buckets["unapplied_disposition"], [])
        self.assertEqual(buckets["superseded_disposition"], [])

    def test_strict_contract_unaffected_by_a_superseded_disposition(self):
        """NEGATIVE CONTROL: --strict gates on unapplied_disposition only. A
        row that moves to superseded_disposition must not leave any residue
        in the exit code."""
        self._two_runs("unset -> standard", "standard -> substrate_ceiling",
                        claim_epistemic_category="substrate_ceiling")
        rc, out = self.run_main("--strict")
        self.assertEqual(rc, 0)
        self.assertIn("superseded claim disposition (WARN)     : 1", out)


# =========================================================================
# GOVERNANCE OVERRIDE -- a ratified decision that postdates the autopsy
# (THE 2026-09-11 REPAIR)
# =========================================================================
class GovernanceOverrideTests(Base):
    """Replicates the real ARC-037 shape: a confirmed autopsy recommends
    `epistemic_category: standard`, it WAS applied, and a later ratified pass
    deliberately set `substrate_conditional` instead."""

    SLUG = "failure_autopsy_V3-EXQ-1001_2026-09-04"
    GEN = "2026-09-04T14:11:17Z"

    def _case(self, override=None, slug=None, generated=None, category="substrate_conditional"):
        claim = {"id": CLAIM}
        if category is not None:
            claim["epistemic_category"] = category
        if override is not None:
            claim["governance_override"] = override
        self.fx.write_claims([claim])
        self.fx.autopsy(
            slug=slug or self.SLUG, generated=generated or self.GEN,
            targets=[self.fx.target(
                run_id="run_1001_v3", recommended=None,
                per_claim_recommendation={
                    CLAIM: {"change": "set one -> epistemic_category: standard"}})])

    @staticmethod
    def _override(supersedes="failure_autopsy_V3-EXQ-1001_2026-09-04",
                  decided="2026-09-06", reason="deliberate: precondition failure",
                  **extra):
        entry = {}
        if supersedes is not None:
            entry["supersedes_autopsy"] = supersedes
        if decided is not None:
            entry["decided_utc"] = decided
        if reason is not None:
            entry["reason"] = reason
        entry.update(extra)
        return [entry]

    # ---- THE FIX ---------------------------------------------------------
    def test_ratified_override_moves_row_from_actionable_to_warn(self):
        """THE FIX. Fails on the pre-2026-09-11 code, where this row was
        ACTIONABLE forever and three consecutive governance cycles re-derived
        it by hand."""
        self._case(override=self._override(
            field="epistemic_category", ratified_by="ada5d97af02"))
        buckets = self.scan()
        self.assertEqual(buckets["unapplied_disposition"], [])
        rows = buckets["overridden_disposition"]
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["claim_id"], CLAIM)
        self.assertEqual(rows[0]["artifact"], self.SLUG)
        self.assertEqual(rows[0]["decided_utc"], "2026-09-06")
        self.assertEqual(rows[0]["field"], "epistemic_category")
        self.assertEqual(rows[0]["ratified_by"], "ada5d97af02")
        self.assertIn("precondition", rows[0]["reason"])

    def test_same_day_ratification_is_honoured(self):
        """A ratification routinely lands the SAME day as the autopsy it
        supersedes (the real V3-EXQ-1010 shape). Day-granularity `>=` is why
        the gate is not a strict timestamp compare."""
        self._case(override=self._override(decided="2026-09-04"))
        self.assertEqual(len(self.scan()["overridden_disposition"]), 1)

    # ---- THE NON-RUBBER-STAMP PROPERTY -----------------------------------
    def test_override_does_not_suppress_a_DIFFERENT_autopsy(self):
        """THE LOAD-BEARING NEGATIVE CONTROL. An override is keyed to ONE
        (claim, autopsy) pair. A newer confirmed autopsy naming the same claim
        must still report ACTIONABLE -- a marker that suppressed the claim
        wholesale would silently re-create the blind spot this audit exists
        to close."""
        self._case(override=self._override(supersedes="failure_autopsy_SOMETHING_ELSE_2026-01-01"))
        buckets = self.scan()
        self.assertEqual(len(buckets["unapplied_disposition"]), 1)
        self.assertEqual(buckets["overridden_disposition"], [])

    def test_override_predating_its_autopsy_is_ignored(self):
        """NEGATIVE CONTROL: an override dated BEFORE the autopsy is not an
        override of it -- the autopsy is the later word."""
        self._case(override=self._override(decided="2026-09-01"))
        buckets = self.scan()
        self.assertEqual(len(buckets["unapplied_disposition"]), 1)
        self.assertEqual(buckets["overridden_disposition"], [])

    # ---- MALFORMED MARKERS ARE IGNORED, NEVER HONOURED -------------------
    def test_malformed_overrides_leave_the_row_actionable(self):
        """NEGATIVE CONTROL: the file-wide false-positive bias. A marker
        missing any of the three required fields cannot suppress anything --
        an override nobody can read is one nobody can audit."""
        for label, ov in (
                ("no slug", self._override(supersedes=None)),
                ("no date", self._override(decided=None)),
                ("no reason", self._override(reason=None)),
                ("empty reason", self._override(reason="   ")),
                ("not a list", "failure_autopsy_V3-EXQ-1001_2026-09-04"),
                ("list of junk", ["nope", 7]),
        ):
            with self.subTest(label):
                self._case(override=ov)
                buckets = self.scan()
                self.assertEqual(len(buckets["unapplied_disposition"]), 1, label)
                self.assertEqual(buckets["overridden_disposition"], [], label)

    def test_a_bare_dict_override_is_tolerated(self):
        """A single un-listed entry is accepted (YAML authors write both), but
        it is still slug-keyed and date-gated like any other."""
        self._case(override=self._override()[0])
        self.assertEqual(len(self.scan()["overridden_disposition"]), 1)

    # ---- ORDERING AGAINST THE EXISTING CHECKS ----------------------------
    def test_an_applied_disposition_is_not_reported_as_overridden(self):
        """NEGATIVE CONTROL: _reflects runs FIRST. A disposition that is
        simply APPLIED lands in no bucket at all -- the override must not
        dress an ordinary success up as a deliberate divergence."""
        self._case(override=self._override(), category="standard")
        buckets = self.scan()
        self.assertEqual(buckets["unapplied_disposition"], [])
        self.assertEqual(buckets["overridden_disposition"], [])

    def test_one_override_on_the_latest_row_clears_older_siblings(self):
        """The real INV-088 shape: a single un-certifiable NEWEST row pinned
        two older dispositions in ACTIONABLE, because the 2026-08-22 cascade
        demotes an older row only when the latest one is settled. An
        OVERRIDDEN latest counts as settled -- claims.yaml holds the ratified
        reading either way."""
        self.fx.write_claims([{
            "id": CLAIM,
            "epistemic_category": "standard",
            "governance_override": self._override(
                supersedes="failure_autopsy_newest_2026-09-11",
                decided="2026-09-11", reason="claim-free diagnostic; citation stays"),
        }])
        self.fx.autopsy(slug="failure_autopsy_older_2026-09-03",
                        generated="2026-09-03T19:00:24Z",
                        targets=[self.fx.target(
                            run_id="run_older_v3", recommended=None,
                            per_claim_recommendation={CLAIM: {
                                "change": "record by citation -> stamp failure_autopsy_older_2026-09-03"}})])
        self.fx.autopsy(slug="failure_autopsy_newest_2026-09-11",
                        generated="2026-09-11T13:36:26Z",
                        targets=[self.fx.target(
                            run_id="run_newest_v3", recommended=None,
                            per_claim_recommendation={CLAIM: {
                                "change": "note-only -> stamp failure_autopsy_newest_2026-09-11"}})])
        buckets = self.scan()
        self.assertEqual(buckets["unapplied_disposition"], [])
        self.assertEqual(len(buckets["overridden_disposition"]), 1)
        self.assertEqual(len(buckets["superseded_disposition"]), 1)
        self.assertEqual(buckets["superseded_disposition"][0]["artifact"],
                         "failure_autopsy_older_2026-09-03")

    # ---- REPORTING CONTRACT ---------------------------------------------
    def test_strict_contract_unaffected_by_an_override(self):
        """NEGATIVE CONTROL: --strict gates on unapplied_disposition only,
        exactly as it does for superseded_disposition."""
        self._case(override=self._override())
        rc, out = self.run_main("--strict")
        self.assertEqual(rc, 0)
        self.assertIn("overridden by ratified decision (WARN)  : 1", out)

    def test_suppressed_rows_are_named_in_the_report_not_silently_dropped(self):
        """A GOV-APPLY-1 printing zero ACTIONABLE rows must not read as
        'nothing is owed' when the truth is 'nothing except what someone
        ratified away'. The coverage block says so, and the row keeps its
        reason and its artifact."""
        self._case(override=self._override(
            reason="precondition failure yields substrate_not_ready",
            ratified_by="ada5d97af02"))
        rc, out = self.run_main()
        self.assertEqual(rc, 0)
        self.assertIn("suppressed by a ratified", out)
        self.assertIn("OVERRIDDEN by", out)
        self.assertIn("precondition failure yields substrate_not_ready", out)
        self.assertIn("ada5d97af02", out)
        self.assertIn(self.SLUG, out)

    def test_no_override_key_is_a_strict_no_op(self):
        """NEGATIVE CONTROL: the whole mechanism is inert on a corpus that
        carries no markers -- the row reports exactly as it did before."""
        self._case(override=None)
        buckets = self.scan()
        self.assertEqual(len(buckets["unapplied_disposition"]), 1)
        self.assertEqual(buckets["overridden_disposition"], [])


# =========================================================================
# MANIFEST RESOLUTION -- mirroring the indexer
# =========================================================================
class ResolutionTests(Base):

    def _one_target(self):
        self.fx.autopsy(targets=[self.fx.target()])
        self.fx.live()

    def test_flat_correction_without_a_note_is_not_in_effect(self):
        """The `_is_annotated` trap (indexer :1428/:1517). A flat copy corrected
        to non_contributory with NO note never overlays the pack, so the stale
        pack value goes on scoring and this MUST still fire."""
        self._one_target()
        self.fx.pack(direction="weakens")
        self.fx.flat(direction="non_contributory", note=None)
        rows = self.directions()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["effective_direction"], "weakens")
        self.assertEqual(rows[0]["manifest_source"], "pack")

    def test_annotated_flat_overlays_the_pack(self):
        """NEGATIVE CONTROL: with the note present the overlay fires, the
        correction is genuinely in effect, and nothing is reported."""
        self._one_target()
        self.fx.pack(direction="weakens")
        self.fx.flat(direction="non_contributory", note="reclassified, ff2e977acf")
        self.assertEqual(self.directions(), [])

    def test_annotated_pack_blocks_the_flat_overlay(self):
        """Overlay is `annotated(flat) and NOT annotated(pack)`. An annotated
        pack wins, so a disagreeing flat does not rescue it."""
        self._one_target()
        self.fx.pack(direction="weakens", note="stamped at record time")
        self.fx.flat(direction="non_contributory", note="reclassified")
        rows = self.directions()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["manifest_source"], "pack")

    def test_flat_sibling_must_be_named_for_the_run_id(self):
        """The residual finding: `_resolve_flat_sibling` looks up EXACT paths, so
        a correction in a file whose name omits the run_id's `_v3` suffix is
        unreachable by the indexer and must still be reported. Keying on the
        run_id FIELD instead would silently credit it (measured: 7 live rows)."""
        self._one_target()
        self.fx.pack(direction="weakens")
        self.fx.flat(direction="non_contributory", note="reclassified",
                     filename="%s.json" % RUN.replace("_v3", ""))
        rows = self.directions()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["effective_direction"], "weakens")

    def test_flat_sibling_found_in_the_experiment_type_subdirectory(self):
        """NEGATIVE CONTROL for the fallback half of the lookup."""
        self._one_target()
        self.fx.pack(direction="weakens")
        self.fx.flat(direction="non_contributory", note="reclassified", exp_type=TYPE)
        self.assertEqual(self.directions(), [])

    def test_top_level_flat_wins_over_the_subdirectory_copy(self):
        """ORDER IS LOAD-BEARING (indexer :1553). Top level is the surface
        governance annotates; preferring the subdirectory would suppress a
        correction that applies today."""
        self._one_target()
        self.fx.pack(direction="weakens")
        self.fx.flat(direction="non_contributory", note="the real correction")
        self.fx.flat(direction="weakens", exp_type=TYPE)
        self.assertEqual(self.directions(), [])

    def test_pack_claims_are_keyed_as_claim_ids_tested(self):
        """The pack uses `claim_ids_tested`; reading `claim_ids` alone yields an
        empty list and a silently vacuous check."""
        self._one_target()
        self.fx.pack(direction="weakens", claims_key="claim_ids_tested")
        resolved = M.ManifestResolver(self.fx.root).resolve(RUN)
        self.assertEqual(resolved.claim_ids, [CLAIM])
        self.assertEqual(len(self.directions()), 1)

    def test_per_claim_manifest_override_beats_the_run_level_field(self):
        """Indexer :3291. A run-level `non_contributory` does not save a claim
        whose per-claim override still says weakens."""
        self._one_target()
        self.fx.pack(direction="non_contributory", per_claim={CLAIM: "weakens"})
        rows = self.directions()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["effective_direction"], "weakens")

    def test_run_with_no_manifest_is_counted_but_not_reported(self):
        """NEGATIVE CONTROL: unresolvable is not the same as unapplied."""
        self._one_target()
        buckets = self.scan()
        self.assertEqual(buckets["unapplied_evidence_direction"], [])
        self.assertEqual(buckets["n_with_recommended_direction"], 1)
        self.assertEqual(buckets["n_direction_checkable"], 0)


# =========================================================================
# GFLAG-0243 -- the two coupled blind spots that kept a genuinely-applied
# recommendation reporting forever. BOTH halves are needed; each test below
# that asserts a CLEARED row fails if either fix is reverted.
#
# Half 1: ManifestResolver had no step 4 -- a run with no pack and no
#         exact-path flat copy resolved to None even when the indexer's own
#         flat-only orphan scan was scoring it.
# Half 2: `_reflects` routed the prose `-> evidence_direction: <dir>` to the
#         claims.yaml named-field branch, where it could never certify.
# =========================================================================
class FlatOnlyOrphanResolutionTests(Base):
    """Step 4 of the ManifestResolver precedence list."""

    def _one_target(self, recommended="non_contributory"):
        self.fx.autopsy(targets=[self.fx.target(recommended=recommended)])
        self.fx.live()

    def test_subdirectory_only_manifest_resolves_with_no_pack(self):
        """THE GFLAG-0243 INSTANCE, in miniature: the manifest exists ONLY at
        `<base>/<type>/<run_id>.json` -- no pack, no top-level flat copy. The
        indexer scores it via `_scan_flat_only_orphans`; before step 4 existed
        this resolved to None and the recommendation reported forever."""
        self._one_target()
        self.fx.flat(direction="non_contributory", exp_type=TYPE)
        resolved = M.ManifestResolver(self.fx.root).resolve(RUN)
        self.assertIsNotNone(resolved)
        self.assertEqual(resolved.source, "flat_only_orphan")
        self.assertEqual(resolved.for_claim(CLAIM), "non_contributory")
        self.assertEqual(self.directions(), [])

    def test_orphan_is_matched_by_run_id_field_not_filename(self):
        """The v3_exq_472 shape: the file is named `..._output.json`, so no
        exact-path lookup can reach it. The indexer's flat-only path keys on
        the run_id FIELD, so this one IS scored and must be checked."""
        self._one_target()
        self.fx.flat(direction="non_contributory", exp_type=TYPE,
                     filename="v3_exq_914_output.json")
        resolved = M.ManifestResolver(self.fx.root).resolve(RUN)
        self.assertIsNotNone(resolved)
        self.assertEqual(resolved.source, "flat_only_orphan")
        self.assertEqual(self.directions(), [])

    def test_orphan_still_reports_when_the_direction_disagrees(self):
        """NEGATIVE CONTROL, and the load-bearing one: newly RESOLVING a run
        must not mean newly CERTIFYING it. A resolvable orphan that still
        carries the old direction fires exactly as a pack would."""
        self._one_target()
        self.fx.flat(direction="weakens", exp_type=TYPE)
        rows = self.directions()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["effective_direction"], "weakens")
        self.assertEqual(rows[0]["manifest_source"], "flat_only_orphan")

    def test_a_pack_still_wins_over_a_field_matched_orphan(self):
        """PRECEDENCE: step 4 is consulted ONLY when 1-3 miss. With a pack
        present the orphan index is never reached, so the pack's stale
        direction still fires -- this is what makes the change additive."""
        self._one_target()
        self.fx.pack(direction="weakens")
        self.fx.flat(direction="non_contributory", exp_type=TYPE,
                     filename="something_else.json")
        rows = self.directions()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["effective_direction"], "weakens")
        self.assertEqual(rows[0]["manifest_source"], "pack")

    def test_exact_path_top_level_flat_still_wins_over_the_orphan_index(self):
        """PRECEDENCE, step 2 before step 4: the top level is the surface
        governance annotates, and preferring a subdirectory copy would
        suppress a correction that applies today (indexer :1553)."""
        self._one_target()
        self.fx.flat(direction="non_contributory")           # <base>/<run_id>.json
        self.fx.flat(direction="weakens", exp_type=TYPE)     # subdirectory copy
        self.assertEqual(self.directions(), [])

    def test_top_level_orphan_wins_over_the_subdirectory_orphan(self):
        """Within step 4 the glob order is top level first, mirroring
        `_scan_flat_only_orphans`. Both files are field-matched only (neither
        is named for the run_id), so only the ORDER can decide."""
        self._one_target()
        self.fx.flat(direction="non_contributory", filename="aaa_top.json")
        self.fx.flat(direction="weakens", exp_type=TYPE, filename="zzz_sub.json")
        self.assertEqual(self.directions(), [])

    def test_dry_run_smokes_are_not_resolved_by_the_orphan_index(self):
        """A dry smoke is never scored by the indexer, so resolving to one
        would certify against something that is not the scoring source. The
        run stays unresolvable -- counted, named, never certified."""
        self._one_target()
        self.fx.flat(direction="non_contributory", exp_type=TYPE,
                     filename="dry_smoke.json", dry_run=True)
        self.assertIsNone(M.ManifestResolver(self.fx.root).resolve(RUN))
        buckets = self.scan()
        self.assertEqual(buckets["n_direction_checkable"], 0)
        self.assertEqual(buckets["n_direction_unresolved"], 1)

    def test_claim_evidence_index_is_not_read_as_a_manifest(self):
        """`claim_evidence.v1.json` lives in the flat namespace and is not a
        run manifest (indexer `_FLAT_ONLY_NON_MANIFEST_NAMES`)."""
        self._one_target()
        self.assertIsNone(M.ManifestResolver(self.fx.root).resolve(RUN))

    def test_run_pack_manifests_are_not_reachable_via_the_orphan_index(self):
        """`runs/` is excluded from the orphan globs. A pack whose run_id
        FIELD differs from its directory name must not be field-matched into
        step 4 -- step 1 is the only path that may reach a pack."""
        self.fx.autopsy(targets=[self.fx.target(run_id="ghost_run_v3")])
        self.fx.live(run_id="ghost_run_v3")
        self.fx.pack(run_id="ghost_run_v3", exp_type=TYPE)
        # relabel the pack's run_id field, leaving the directory name alone
        d = self.fx.experiments / TYPE / "runs" / "ghost_run_v3" / "manifest.json"
        body = json.loads(d.read_text())
        body["run_id"] = "ghost_run_v3"
        d.write_text(json.dumps(body))
        resolved = M.ManifestResolver(self.fx.root).resolve("ghost_run_v3")
        self.assertEqual(resolved.source, "pack")


class EvidenceDirectionProseRoutingTests(Base):
    """Half 2: `-> evidence_direction: <dir>` is a MANIFEST assertion."""

    def _disposition(self, change):
        self.fx.autopsy(targets=[self.fx.target(
            per_claim_recommendation={CLAIM: {
                "change": change,
                "recommended_evidence_direction": "non_contributory"}})])
        self.fx.live()

    def test_named_evidence_direction_is_checked_against_the_manifest(self):
        """The GFLAG-0243 prose shape. `evidence_direction` is not a
        claims.yaml field -- no claim in the corpus carries the key -- so
        routing it to the named-field branch could never certify."""
        self._disposition("only the 259 entry moves -> "
                          "evidence_direction: non_contributory")
        self.fx.pack(direction="non_contributory")
        self.assertEqual(self.scan()["unapplied_disposition"], [])

    def test_named_evidence_direction_still_fires_when_the_manifest_disagrees(self):
        """NEGATIVE CONTROL: the routing change moves WHERE the assertion is
        checked, never whether it must hold. A stale manifest still fires."""
        self._disposition("only the 259 entry moves -> "
                          "evidence_direction: non_contributory")
        self.fx.pack(direction="weakens")
        self.assertEqual([r["claim_id"] for r in self.scan()["unapplied_disposition"]],
                         [CLAIM])

    def test_named_evidence_direction_cannot_certify_without_a_manifest(self):
        """NEGATIVE CONTROL: unverifiable reports as unapplied, per the
        module's stated bias. No manifest anywhere -> still fires."""
        self._disposition("-> evidence_direction: non_contributory")
        self.assertEqual([r["claim_id"] for r in self.scan()["unapplied_disposition"]],
                         [CLAIM])

    def test_a_non_direction_named_field_still_routes_to_claims_yaml(self):
        """SCOPE BOUND: only `evidence_direction` moves. `epistemic_category`
        is a genuine claims.yaml field and must keep its own branch."""
        self._disposition("-> epistemic_category: substrate_ceiling")
        self.fx.pack(direction="non_contributory")
        self.fx.write_claims([{"id": CLAIM, "status": "candidate",
                               "epistemic_category": "substrate_ceiling"}])
        self.assertEqual(self.scan()["unapplied_disposition"], [])

    def test_named_evidence_direction_with_a_non_vocabulary_value_is_unchanged(self):
        """SCOPE BOUND: the manifest route is gated on the direction
        VOCABULARY, exactly as the bare-prose branch is. A value outside it
        keeps the old claims.yaml routing and cannot certify."""
        self._disposition("-> evidence_direction: not_a_direction")
        self.fx.pack(direction="not_a_direction")
        self.assertEqual([r["claim_id"] for r in self.scan()["unapplied_disposition"]],
                         [CLAIM])

    def test_both_halves_are_required_together(self):
        """THE FULL GFLAG-0243 SHAPE end to end: subdirectory-only manifest
        (needs half 1) named by prose as `evidence_direction:` (needs half 2).
        Reverting either fix re-breaks this."""
        self._disposition("only the 259 entry moves -> "
                          "evidence_direction: non_contributory")
        self.fx.flat(direction="non_contributory", exp_type=TYPE)
        self.assertEqual(self.scan()["unapplied_disposition"], [])


# =========================================================================
# UNRESOLVED reporting -- the class must not be able to hide again
# =========================================================================
class UnresolvedReportingTests(Base):

    def test_unresolvable_targets_are_counted_separately(self):
        """They are NOT folded into the coverage figure: a recommendation
        against a run with no manifest can never be certified applied, so
        silence there reads exactly like `applied`."""
        self.fx.autopsy(targets=[self.fx.target()])
        self.fx.live()
        buckets = self.scan()
        self.assertEqual(buckets["n_with_recommended_direction"], 1)
        self.assertEqual(buckets["n_direction_checkable"], 0)
        self.assertEqual(buckets["n_direction_unresolved"], 1)
        self.assertEqual(buckets["unresolved_run_ids"], [RUN])

    def test_a_resolvable_run_is_not_counted_unresolved(self):
        """NEGATIVE CONTROL."""
        self.fx.autopsy(targets=[self.fx.target()])
        self.fx.live()
        self.fx.pack(direction="weakens")
        buckets = self.scan()
        self.assertEqual(buckets["n_direction_unresolved"], 0)
        self.assertEqual(buckets["unresolved_run_ids"], [])

    def test_the_report_names_the_unresolvable_run_ids(self):
        self.fx.autopsy(targets=[self.fx.target()])
        self.fx.live()
        rc, out = self.run_main()
        self.assertEqual(rc, 0)
        self.assertIn("UNRESOLVED (not checked): 1 target(s) across 1 run(s)", out)
        self.assertIn(RUN, out)

    def test_the_report_says_nothing_when_everything_resolves(self):
        """NEGATIVE CONTROL: a line that always prints is noise, and noise is
        how a finding hides."""
        self.fx.autopsy(targets=[self.fx.target()])
        self.fx.live()
        self.fx.pack(direction="non_contributory")
        rc, out = self.run_main()
        self.assertNotIn("UNRESOLVED", out)

    def test_the_listing_is_capped_until_full(self):
        n = M.UNRESOLVED_DISPLAY_LIMIT + 3
        runs = ["v3_exq_%03d_unresolvable_v3" % i for i in range(n)]
        self.fx.autopsy(targets=[self.fx.target(run_id=r) for r in runs])
        for r in runs:
            self.fx.live(run_id=r)
        rc, out = self.run_main()
        self.assertIn("... and 3 more; re-run with --full", out)
        rc, out_full = self.run_main("--full")
        self.assertNotIn("re-run with --full to list them", out_full)
        for r in runs:
            self.assertIn(r, out_full)

    def test_unresolvable_targets_do_not_affect_the_strict_exit(self):
        """CONTRACT: governance.sh Step 3h's invocation predates this bucket."""
        self.fx.autopsy(targets=[self.fx.target()])
        self.fx.live()
        self.assertEqual(self.run_main("--strict")[0], 0)
        self.assertEqual(self.run_main("--strict-direction")[0], 0)


# =========================================================================
# unapplied_evidence_direction SCOPE -- the per_claim_recommendation gap,
# and its bounds
# =========================================================================
class DirectionBucketTests(Base):

    def test_target_without_per_claim_recommendation_is_still_checked(self):
        """THE COVERAGE FIX. `per_claim_recommendation` is present on 25 of 1194
        corpus targets; the 914-914a artifact has none, so
        unapplied_disposition skipped both its targets before any check ran.
        The target-level field covers 1175."""
        self.fx.autopsy(targets=[self.fx.target()])
        self.fx.pack(direction="weakens")
        self.fx.live()
        buckets = self.scan()
        self.assertEqual(buckets["n_with_per_claim_recommendation"], 0)
        self.assertEqual(len(buckets["unapplied_evidence_direction"]), 1)

    def test_live_row_is_actionable_and_excluded_row_is_warn(self):
        """Liveness is what separates a manifest that is merely wrong on disk
        from one producing a wrong number today."""
        self.fx.autopsy(targets=[
            self.fx.target(),
            self.fx.target(run_id="run_b_v3", claim_ids=(CLAIM,)),
        ])
        self.fx.pack(direction="weakens")
        self.fx.pack(run_id="run_b_v3", exp_type="type_b", direction="weakens")
        self.fx.live()
        self.fx.live(run_id="run_b_v3", scoring_excluded="stale_substrate")
        rows = self.directions()
        self.assertEqual(sorted(r["live"] for r in rows), [False, True])

    def test_missing_claim_evidence_degrades_to_warn_not_to_silence(self):
        """NEGATIVE CONTROL on the failure mode: without the derived index the
        audit must not claim a liveness it cannot establish, and must not drop
        the row either."""
        self.fx.autopsy(targets=[self.fx.target()])
        self.fx.pack(direction="weakens")
        buckets = self.scan(write_evidence=False)
        self.assertFalse(buckets["liveness_available"])
        rows = buckets["unapplied_evidence_direction"]
        self.assertEqual(len(rows), 1)
        self.assertIsNone(rows[0]["live"])

    def test_agreeing_direction_does_not_fire(self):
        """NEGATIVE CONTROL."""
        self.fx.autopsy(targets=[self.fx.target(recommended="non_contributory")])
        self.fx.pack(direction="non_contributory")
        self.fx.live()
        self.assertEqual(self.directions(), [])

    def test_over_exclusion_is_counted_not_listed(self):
        """NEGATIVE CONTROL: the reverse shape (inert on disk, a scoring
        direction recommended) UNDER-counts evidence rather than manufacturing
        it, so it is a total and never a listed row."""
        self.fx.autopsy(targets=[self.fx.target(recommended="weakens")])
        self.fx.pack(direction="non_contributory")
        self.fx.live()
        buckets = self.scan()
        self.assertEqual(buckets["unapplied_evidence_direction"], [])
        self.assertEqual(buckets["n_over_excluded"], 1)

    def test_claim_not_tagged_by_the_manifest_is_out_of_scope(self):
        """NEGATIVE CONTROL: a claim the manifest does not tag cannot score, so
        a recommendation about it is not a live scoring defect."""
        self.fx.autopsy(targets=[self.fx.target(claim_ids=(CLAIM, "MECH-999"))])
        self.fx.pack(direction="weakens", claim_ids=(CLAIM,))
        self.fx.live()
        rows = self.directions()
        self.assertEqual([r["claim_id"] for r in rows], [CLAIM])

    def test_only_the_latest_adjudication_of_a_run_counts(self):
        """NEGATIVE CONTROL for R2: a superseded adjudication must not fire."""
        self.fx.autopsy(slug="failure_autopsy_old_2026-01-01",
                        generated="2026-01-01T00:00:00Z",
                        targets=[self.fx.target(recommended="non_contributory")])
        self.fx.autopsy(slug="failure_autopsy_new_2026-08-13",
                        generated="2026-08-13T00:00:00Z",
                        targets=[self.fx.target(recommended="weakens")])
        self.fx.pack(direction="weakens")
        self.fx.live()
        self.assertEqual(self.directions(), [])

    def test_unconfirmed_autopsy_is_ignored(self):
        """NEGATIVE CONTROL: staged verdicts are not recommendations yet."""
        self.fx.autopsy(status="staged", targets=[self.fx.target()])
        self.fx.pack(direction="weakens")
        self.fx.live()
        self.assertEqual(self.directions(), [])

    def test_per_claim_recommendation_beats_the_target_level_field(self):
        self.fx.autopsy(targets=[self.fx.target(
            recommended="weakens",
            per_claim_recommendation={CLAIM: {
                "change": "weakens -> superseded",
                "recommended_evidence_direction": "superseded"}})])
        self.fx.pack(direction="weakens")
        self.fx.live()
        rows = self.directions()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["recommended_direction"], "superseded")


# =========================================================================
# VOCABULARY -- must track the indexer, not a drifting restatement
# =========================================================================
class VocabularyTests(unittest.TestCase):

    INDEXER = (REPO_ROOT / "evidence" / "experiments" / "scripts"
               / "build_experiment_indexes.py")

    def test_direction_vocabulary_matches_the_indexer_source(self):
        """A direction added there and not here means silent under-reporting --
        the defect class this audit exists to catch, turned on itself."""
        if not self.INDEXER.is_file():
            self.skipTest("indexer not present in this checkout")
        text = self.INDEXER.read_text()
        block = re.search(r"def _normalize_direction.*?allowed = \{(.*?)\}",
                          text, re.S)
        self.assertIsNotNone(block, "indexer's _normalize_direction moved")
        found = set(re.findall(r'"([a-z_]+)"', block.group(1)))
        self.assertEqual(found, M._DIRECTION_VOCAB)

    def test_does_not_support_normalizes_to_weakens(self):
        self.assertEqual(M._normalize_direction("does_not_support"), "weakens")

    def test_unrecognized_direction_normalizes_to_unknown(self):
        self.assertEqual(M._normalize_direction("gibberish"), "unknown")
        self.assertEqual(M._normalize_direction(None), "unknown")

    def test_inert_directions_are_the_indexer_exclusions(self):
        """NEGATIVE CONTROL on scope: supports/weakens/mixed/unknown all SCORE,
        so they must not be treated as inert."""
        self.assertEqual(M.INERT_DIRECTIONS,
                         {"non_contributory", "inconclusive", "superseded"})
        for scoring in ("supports", "weakens", "mixed", "unknown"):
            self.assertNotIn(scoring, M.INERT_DIRECTIONS)


# =========================================================================
# CONSUMER CONTRACT -- governance.sh Step 3h and any CI gate
# =========================================================================
class ContractTests(Base):

    def _live_hit(self):
        self.fx.autopsy(targets=[self.fx.target()])
        self.fx.pack(direction="weakens")
        self.fx.live()

    def test_existing_bucket_keys_are_preserved(self):
        """NEGATIVE CONTROL: the two documented buckets and both coverage
        counters must survive, or a consumer reading them breaks."""
        self.fx.autopsy(targets=[self.fx.target()])
        buckets = self.scan()
        for key in ("unapplied_disposition", "superseded_disposition", "superseded_citation",
                    "n_confirmed_targets", "n_with_per_claim_recommendation"):
            self.assertIn(key, buckets)

    def test_strict_exit_contract_is_unchanged_by_the_new_bucket(self):
        """NEGATIVE CONTROL, and the one most likely to be broken by a later
        'simplification': --strict is unapplied_disposition's gate. A live row
        alone must NOT make it exit 1, or every existing caller starts failing."""
        self._live_hit()
        rc, out = self.run_main("--strict")
        self.assertEqual(rc, 0)
        self.assertIn("unapplied evidence direction, LIVE (ACTIONABLE): 1", out)

    def test_strict_direction_exits_on_a_live_row(self):
        self._live_hit()
        self.assertEqual(self.run_main("--strict-direction")[0], 1)

    def test_strict_direction_is_clean_when_nothing_is_live(self):
        """NEGATIVE CONTROL."""
        self.fx.autopsy(targets=[self.fx.target()])
        self.fx.pack(direction="weakens")
        self.fx.live(scoring_excluded="degenerate")
        self.assertEqual(self.run_main("--strict-direction")[0], 0)

    def test_plain_invocation_always_exits_zero(self):
        """governance.sh Step 3h runs it warn-only; a non-zero default would
        change that step's meaning."""
        self._live_hit()
        self.assertEqual(self.run_main()[0], 0)

    def test_output_is_ascii(self):
        """House rule: printed output must survive a cp1252 terminal."""
        self._live_hit()
        out = self.run_main()[1]
        out.encode("ascii")

    def test_full_lists_every_run_and_the_default_truncates(self):
        n = M.DIRECTION_DISPLAY_LIMIT + 3
        targets = []
        for i in range(n):
            rid = "run_%03d_v3" % i
            targets.append(self.fx.target(run_id=rid))
            self.fx.pack(run_id=rid, exp_type="type_%03d" % i, direction="weakens")
            self.fx.live(run_id=rid)
        self.fx.autopsy(targets=targets)
        default_out = self.run_main()[1]
        self.assertIn("re-run with --full", default_out)
        self.assertNotIn("re-run with --full", self.run_main("--full")[1])


# =========================================================================
# THE 2026-09-22 REPAIR -- three detector defects that kept five rows
# ACTIONABLE with NO remaining claims-side action (GFLAG-0349, re-verified
# by governance cycle governance-20260922 row by row).
#
# The negative controls here carry the same weight as the positives, and
# more: the failure mode of this repair is a detector that tolerates a
# genuinely missing field. GFLAG-0349 and the script's own 2026-09-01 repair
# note both forbid that widening, because a missing
# `recommended_epistemic_category` is a real finding GOV-CAT-1 exists to
# catch. Every "still fires" test below is pinning that boundary.
# =========================================================================
class FalseRecommendationSatisfiedByAbsenceTests(Base):
    """Defects (2) and (3): a structured `recommended_*` key PRESENT on the
    recommendation with value `false`/`null` was read as "the claim must
    carry this key", so a row correctly asking for NO write could never
    clear. The real shape is MECH-547/MECH-548 from
    failure_autopsy_V3-EXQ-1044_2026-09-17 -- claim-free diagnostics
    (`claim_ids: []`) whose scope_note says in terms "do NOT set
    diagnostic_evidence_adjudicated (the run tagged no claim, so that flag
    would assert something untrue)" -- and SD-024 from
    failure_autopsy_V3-EXQ-900_2026-09-14 on the same flag."""

    SLUG_A = "failure_autopsy_stamped_2026-09-17"

    def _row(self, rec_extra, claim_extra=None, cites=None):
        claim = {"id": CLAIM, "status": "candidate"}
        claim.update(claim_extra or {})
        claim["live_status"] = {"evidence": {"from": cites or self.SLUG_A}}
        self.fx.write_claims([claim])
        rec = {"change": "NOTE-ONLY, no direction and no flag. Record the "
                         "instrument residuals -> stamp %s" % self.SLUG_A}
        rec.update(rec_extra)
        self.fx.autopsy(slug=self.SLUG_A, generated="2026-09-17T02:35:00Z",
                        targets=[self.fx.target(
                            run_id="run_1044_v3", recommended=None,
                            per_claim_recommendation={CLAIM: rec})])
        return self.scan()

    def test_false_diagnostic_flag_recommendation_is_satisfied_by_absence(self):
        """THE FIX (MECH-547 / MECH-548 exactly). `recommended_diagnostic_
        evidence_adjudicated: false` asks for the flag NOT to be written, so
        an absent key is what it asks for. Fails on the pre-fix code, which
        reported this row ACTIONABLE precisely because the key was correctly
        absent."""
        buckets = self._row({"recommended_diagnostic_evidence_adjudicated": False})
        self.assertEqual(buckets["unapplied_disposition"], [])

    def test_null_epistemic_category_recommendation_is_satisfied_by_absence(self):
        """Same shape on the other gated field: `recommended_epistemic_
        category: null` recommends no category at all."""
        buckets = self._row({"recommended_epistemic_category": None})
        self.assertEqual(buckets["unapplied_disposition"], [])

    def test_blank_epistemic_category_recommendation_is_satisfied_by_absence(self):
        """An empty string is the same non-recommendation as null."""
        buckets = self._row({"recommended_epistemic_category": "   "})
        self.assertEqual(buckets["unapplied_disposition"], [])

    def test_true_diagnostic_flag_recommendation_still_fires_when_absent(self):
        """NEGATIVE CONTROL, and the load-bearing one. A recommendation of
        `true` is a demand for a write, and an absent key does NOT satisfy
        it. This is the boundary GFLAG-0349 and the 2026-09-01 repair note
        both insist on: the fix is false/null-specific, never a general
        tolerance of missing fields."""
        buckets = self._row({"recommended_diagnostic_evidence_adjudicated": True})
        self.assertEqual(len(buckets["unapplied_disposition"]), 1)

    def test_real_epistemic_category_recommendation_still_fires_when_absent(self):
        """NEGATIVE CONTROL: a named category is a demand for a write. This
        is GOV-CAT-1's lane and must keep firing."""
        buckets = self._row({"recommended_epistemic_category": "standard"})
        self.assertEqual(len(buckets["unapplied_disposition"]), 1)

    def test_a_present_field_is_still_compared_against_a_false_recommendation(self):
        """NEGATIVE CONTROL on the last-resort structured check: `false`
        excuses ABSENCE, never a claim that carries the opposite value. With
        no parseable prose target, the last-resort comparator runs, and a
        claim holding `true` against a `false` recommendation is reported."""
        self.fx.write_claims([{"id": CLAIM, "status": "candidate",
                               "diagnostic_evidence_adjudicated": True}])
        self.fx.autopsy(slug=self.SLUG_A, generated="2026-09-17T02:35:00Z",
                        targets=[self.fx.target(
                            run_id="run_1044_v3", recommended=None,
                            per_claim_recommendation={CLAIM: {
                                "change": "NOTE-ONLY. Nothing storable moves.",
                                "recommended_diagnostic_evidence_adjudicated": False}})])
        buckets = self.scan()
        self.assertEqual(len(buckets["unapplied_disposition"]), 1)


class SelfStampOwnSlugTests(Base):
    """Defect (1): `_STAMP_RE` (`stamp .*? (failure_autopsy_...)`) scans the
    WHOLE prose and takes the FIRST slug after any occurrence of the word
    "stamp". A row that narrates its own provenance move therefore demanded a
    stamp of the artifact it was moving AWAY FROM.

    The real shape is MECH-439 from failure_autopsy_V3-EXQ-1012a_2026-09-14:
    "...What governance should apply is the drafted evidence_quality_note ...
    and the citation stamp, so `live_status.evidence.from` moves off
    failure_autopsy_V3-EXQ-571b_2026-09-01 -> stamp this artifact"."""

    OLDER = "failure_autopsy_older_2026-08-13"
    NEWER = "failure_autopsy_newer_2026-09-14"

    def _self_stamp_row(self, cites):
        self.fx.write_claims([{"id": CLAIM, "status": "candidate",
                               "live_status": {"evidence": {"from": cites}}}])
        self.fx.autopsy(slug=self.NEWER, generated="2026-09-14T00:35:57Z",
                        targets=[self.fx.target(
                            run_id="run_newer_v3", recommended=None,
                            per_claim_recommendation={CLAIM: {
                                "change": "No claim-layer field moves. What governance "
                                          "should apply is the drafted evidence_quality_note "
                                          "and the citation stamp, so `live_status.evidence."
                                          "from` moves off %s -> stamp this artifact"
                                          % self.OLDER}})])
        return self.scan()

    def test_stamp_this_artifact_resolves_to_the_artifacts_own_slug(self):
        """THE FIX. The operative stamp is the LAST arrow's, and it is a
        self-reference -- so the target is this artifact, not the slug the
        prose says provenance is moving OFF. Fails on the pre-fix code,
        which demanded the older slug and could never be satisfied once the
        correct newer stamp was applied."""
        buckets = self._self_stamp_row(cites=self.NEWER)
        self.assertEqual(buckets["unapplied_disposition"], [])

    def test_the_narrated_earlier_slug_is_not_the_target(self):
        """NEGATIVE CONTROL, the pre-fix behaviour inverted: a claim still
        citing the OLD artifact has NOT had the stamp applied, so the row
        must stay ACTIONABLE."""
        buckets = self._self_stamp_row(cites=self.OLDER)
        self.assertEqual(len(buckets["unapplied_disposition"]), 1)

    def test_a_literal_trailing_stamp_slug_still_wins(self):
        """NEGATIVE CONTROL: the ordinary "-> stamp <slug>" form is
        untouched. `self.OLDER` appears earlier in the prose and must NOT be
        picked up in preference to the slug the arrow names."""
        self.fx.write_claims([{"id": CLAIM, "status": "candidate",
                               "live_status": {"evidence": {"from": self.NEWER}}}])
        self.fx.autopsy(slug="failure_autopsy_third_2026-09-20",
                        generated="2026-09-20T00:00:00Z",
                        targets=[self.fx.target(
                            run_id="run_third_v3", recommended=None,
                            per_claim_recommendation={CLAIM: {
                                "change": "live_status.evidence.from currently cites %s, "
                                          "stamp the newer one -> stamp %s"
                                          % (self.OLDER, self.NEWER)}})])
        buckets = self.scan()
        self.assertEqual(buckets["unapplied_disposition"], [])

    def test_whole_string_self_stamp_without_an_arrow_target_still_resolves(self):
        """NEGATIVE CONTROL on the fallback path (MECH-439's OTHER row, from
        failure_autopsy_V3-EXQ-571b_2026-09-01): the self-reference sits in
        mid-prose and the last arrow points at something else entirely, so
        the tail-first scan finds no stamp and the whole-string fallback --
        unchanged from 2026-09-01 -- must still resolve it to own_slug."""
        self.fx.write_claims([{"id": CLAIM, "status": "candidate",
                               "live_status": {"evidence": {"from": self.NEWER}}}])
        self.fx.autopsy(slug=self.NEWER, generated="2026-09-14T00:35:57Z",
                        targets=[self.fx.target(
                            run_id="run_newer_v3", recommended=None,
                            per_claim_recommendation={CLAIM: {
                                "change": "NOTE-ONLY. Nothing storable moves, so this row "
                                          "must clear via the provenance stamp "
                                          "(live_status.evidence.from -> this artifact) "
                                          "rather than by a field match. The occupant "
                                          "shifted f_weighted -> harm_weighted 4/4 seeds"}})])
        buckets = self.scan()
        self.assertEqual(buckets["unapplied_disposition"], [])


class NewerStampRetiresOlderStampRowTests(Base):
    """Defect (3): `live_status.evidence.from` holds ONE value, so once a
    newer confirmed autopsy's slug is stamped there, an older stamp-only row
    for the same claim can NEVER be satisfied. The real case is MECH-439's
    failure_autopsy_V3-EXQ-571b_2026-09-01 row once
    failure_autopsy_V3-EXQ-1012a_2026-09-14 was stamped.

    The newer row here is deliberately left UNAPPLIED in the positive test,
    because that is what isolates this route: the pre-existing cross-run
    supersession cascade only fires when the LATEST disposition reflects, so
    one un-certifiable newest row otherwise pins every older stamp row in
    ACTIONABLE forever."""

    OLDER = "failure_autopsy_older_2026-09-01"
    NEWER = "failure_autopsy_newer_2026-09-14"
    EARLIER = "failure_autopsy_earlier_2026-08-01"

    def _build(self, cites, newer_claim_ids=(CLAIM,), older_rec_extra=None,
               newer_change="unset -> substrate_ceiling"):
        self.fx.write_claims([{"id": CLAIM, "status": "candidate",
                               "live_status": {"evidence": {"from": cites}}}])
        older_rec = {"change": "NOTE-ONLY -> stamp %s" % self.OLDER}
        older_rec.update(older_rec_extra or {})
        self.fx.autopsy(slug=self.EARLIER, generated="2026-08-01T00:00:00Z",
                        targets=[self.fx.target(
                            run_id="run_earlier_v3", recommended=None,
                            per_claim_recommendation=None)])
        self.fx.autopsy(slug=self.OLDER, generated="2026-09-01T06:44:22Z",
                        targets=[self.fx.target(
                            run_id="run_older_v3", recommended=None,
                            per_claim_recommendation={CLAIM: older_rec})])
        self.fx.autopsy(slug=self.NEWER, generated="2026-09-14T00:35:57Z",
                        targets=[self.fx.target(
                            run_id="run_newer_v3", claim_ids=newer_claim_ids,
                            recommended=None,
                            per_claim_recommendation={
                                newer_claim_ids[0]: {"change": newer_change}})])
        return self.scan()

    def test_older_stamp_row_is_retired_when_a_newer_stamp_is_in_place(self):
        """THE FIX. The older row's ONLY unmet requirement is its own stamp,
        and the field now carries a strictly-newer confirmed artifact that
        adjudicates the same claim -- so the row is moot, not owed. It moves
        to the WARN bucket, which already means exactly that. The newer row
        is unapplied and correctly STAYS ACTIONABLE."""
        buckets = self._build(cites=self.NEWER)
        actionable = buckets["unapplied_disposition"]
        self.assertEqual([r["artifact"] for r in actionable], [self.NEWER])
        retired = [r for r in buckets["superseded_disposition"]
                   if r.get("retired_by_stamp")]
        self.assertEqual(len(retired), 1)
        self.assertEqual(retired[0]["artifact"], self.OLDER)
        self.assertEqual(retired[0]["superseded_by"], self.NEWER)

    def test_the_report_names_the_stamp_that_retired_it(self):
        """A WARN row nobody can act on is noise unless it says WHY. The
        report must name the newer stamp and the one-value constraint."""
        self.fx.write_claims([{"id": CLAIM, "status": "candidate",
                               "live_status": {"evidence": {"from": self.NEWER}}}])
        self.fx.autopsy(slug=self.OLDER, generated="2026-09-01T06:44:22Z",
                        targets=[self.fx.target(
                            run_id="run_older_v3", recommended=None,
                            per_claim_recommendation={
                                CLAIM: {"change": "NOTE-ONLY -> stamp %s" % self.OLDER}})])
        self.fx.autopsy(slug=self.NEWER, generated="2026-09-14T00:35:57Z",
                        targets=[self.fx.target(
                            run_id="run_newer_v3", recommended=None,
                            per_claim_recommendation={
                                CLAIM: {"change": "unset -> substrate_ceiling"}})])
        rc, out = self.run_main("--strict")
        self.assertEqual(rc, 1)  # the NEWER row is genuinely unapplied
        self.assertIn("retired by the newer stamp now in live_status.evidence.from: %s"
                      % self.NEWER, out)
        self.assertIn("holds ONE value", out)

    def test_not_retired_when_the_cited_artifact_is_older(self):
        """NEGATIVE CONTROL: retirement needs a STRICTLY NEWER stamp. A claim
        citing an EARLIER artifact has simply never had this row applied."""
        buckets = self._build(cites=self.EARLIER)
        self.assertIn(self.OLDER, [r["artifact"] for r in buckets["unapplied_disposition"]])

    def test_not_retired_when_the_cited_artifact_does_not_name_the_claim(self):
        """NEGATIVE CONTROL, and the tightest one: a later artifact that
        happens to be stamped there but does NOT adjudicate this claim
        cannot retire a real finding. This is the same join defect
        GFLAG-0405 records in the live_status projection itself -- the
        detector must not inherit it."""
        buckets = self._build(cites=self.NEWER, newer_claim_ids=("OTHER-001",))
        self.assertIn(self.OLDER, [r["artifact"] for r in buckets["unapplied_disposition"]])

    def test_not_retired_when_the_cited_slug_is_not_a_confirmed_autopsy(self):
        """NEGATIVE CONTROL: an unrecognised citation proves nothing."""
        buckets = self._build(cites="failure_autopsy_not_in_the_corpus_2026-09-30")
        self.assertIn(self.OLDER, [r["artifact"] for r in buckets["unapplied_disposition"]])

    def test_not_retired_when_the_row_also_owes_a_field_write(self):
        """NEGATIVE CONTROL: retirement applies only when the stamp is the
        row's SOLE unmet requirement. A row that also asks for a field the
        claim does not carry stays ACTIONABLE -- the field is still owed
        whatever the citation says."""
        buckets = self._build(
            cites=self.NEWER,
            older_rec_extra={"recommended_epistemic_category": "standard"})
        self.assertIn(self.OLDER, [r["artifact"] for r in buckets["unapplied_disposition"]])

    def test_not_retired_when_the_rows_own_stamp_is_the_one_in_place(self):
        """NEGATIVE CONTROL: a row whose own stamp IS applied certifies
        normally and never reaches the retirement route at all."""
        buckets = self._build(cites=self.OLDER)
        self.assertNotIn(self.OLDER, [r["artifact"] for r in buckets["unapplied_disposition"]])
        self.assertEqual([r for r in buckets["superseded_disposition"]
                          if r.get("retired_by_stamp")], [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
