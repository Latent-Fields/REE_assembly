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
             per_claim=None, filename=None, exp_type=None):
        body = {"run_id": run_id, "evidence_direction": direction,
                "claim_ids": list(claim_ids)}
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
