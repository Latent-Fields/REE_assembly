from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_experiment_profile.py"


def load_module():
    spec = importlib.util.spec_from_file_location("generate_experiment_profile", SCRIPT)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_v3_exq_825_profile_renders_required_sections(tmp_path):
    # generate_experiment_profile.py used to source its "pending" section
    # marker from pending_review.md, a generated/transient worklist that
    # drops each run's entry once governance reviews it -- so this test broke
    # on trunk the moment V3-EXQ-825 was reviewed (2026-08-16). The generator
    # now falls back to the append-only review_tracker.json once a run is
    # reviewed, so this drives the real post-review code path rather than
    # pinning a source that was always going to disappear.
    mod = load_module()
    target = mod.TARGETS["V3-EXQ-825"]
    profile_path, report_path = mod.write_outputs(target, tmp_path)

    text = profile_path.read_text(encoding="utf-8")
    report = report_path.read_text(encoding="utf-8")

    for section in (
        "Scientific Question",
        "Claim Under Test",
        "Competing Explanations",
        "Experimental Design",
        "What Would Falsify The Claim?",
        "What Actually Happened?",
        "Interpretation",
        "Limitations",
        "Reproduction",
        "Expected Outputs",
        "Provenance",
    ):
        assert f"## {section}" in text

    assert "TODO" not in text
    assert "source commit missing" not in text.lower()
    assert "/opt/local/bin/python3 experiments/v3_exq_825" in text
    assert "evidence_direction=supports" in text
    assert "synthetic GRU stand-in" in text
    assert "flat_manifest.source_commit" in report
    assert "run_pack.manifest.source_repo.commit" in report


def test_profile_validation_rejects_todo():
    mod = load_module()
    data = {
        "source_commit": "abc",
        "claim_id": "MECH-245",
        "evidence_direction": "supports",
    }
    bad = (
        "## Scientific Question\n\nTODO Sources: x\n\n"
        "## Claim Under Test\n\nText Sources: x\n\n"
        "## Competing Explanations\n\nText Sources: x\n\n"
        "## Experimental Design\n\nText Sources: x\n\n"
        "## What Would Falsify The Claim?\n\nText Sources: x\n\n"
        "## What Actually Happened?\n\nText Sources: x\n\n"
        "## Interpretation\n\nText Sources: x\n\n"
        "## Limitations\n\nsynthetic GRU stand-in Sources: x\n\n"
        "## Reproduction\n\n/opt/local/bin/python3 experiments/x.py Sources: x\n\n"
        "## Expected Outputs\n\nText Sources: x\n\n"
        "## Provenance\n\nText Sources: x\n"
    )
    try:
        mod.validate_profile(bad, data)
    except mod.ProfileError as exc:
        assert "TODO remains" in str(exc)
    else:
        raise AssertionError("validate_profile accepted a TODO")


def test_profile_validation_rejects_paragraph_without_source():
    mod = load_module()
    data = {
        "source_commit": "abc",
        "claim_id": "MECH-245",
        "evidence_direction": "supports",
    }
    sections = "\n\n".join(
        (
            f"## {name}\n\nsynthetic GRU stand-in Sources: x"
            if name == "Limitations"
            else f"## {name}\n\nText Sources: x"
        )
        for name in (
            "Scientific Question",
            "Claim Under Test",
            "Competing Explanations",
            "Experimental Design",
            "What Would Falsify The Claim?",
            "What Actually Happened?",
            "Interpretation",
            "Limitations",
            "Expected Outputs",
            "Provenance",
        )
    )
    bad = (
        sections
        + "\n\n## Reproduction\n\n"
        + "This paragraph has no provenance marker.\n\n"
        + "```bash\n/opt/local/bin/python3 experiments/x.py\n```"
    )
    try:
        mod.validate_profile(bad, data)
    except mod.ProfileError as exc:
        assert "paragraph lacks provenance" in str(exc)
    else:
        raise AssertionError("validate_profile accepted a paragraph without a source")
