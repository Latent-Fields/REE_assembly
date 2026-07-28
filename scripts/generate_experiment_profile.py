#!/usr/bin/env python3
"""Generate external laboratory experiment profile pages.

Phase 1 is intentionally narrow: only V3-EXQ-825 / MECH-245 is supported.
The generator reads existing repository sources, emits explicit placeholders
for non-required provenance gaps, and fails on missing required legibility
fields rather than inventing scientific content.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
WORKING_ROOT = ROOT.parent
REE_V3_ROOT = WORKING_ROOT / "ree-v3"

DEFAULT_OUT_DIR = ROOT / "docs" / "experiment_profiles"
TEMPLATE_PATH = ROOT / "templates" / "experiment_profile.md"


class ProfileError(RuntimeError):
    """Raised for validation failures that must stop generation."""


@dataclass(frozen=True)
class Target:
    queue_id: str
    claim_id: str
    experiment_type: str
    run_id: str
    source_script: Path
    flat_manifest: Path
    run_manifest: Path
    run_metrics: Path
    run_summary: Path


TARGETS: dict[str, Target] = {
    "V3-EXQ-825": Target(
        queue_id="V3-EXQ-825",
        claim_id="MECH-245",
        experiment_type="v3_exq_825_mech245_generative_dominance_deafferentation",
        run_id=(
            "v3_exq_825_mech245_generative_dominance_deafferentation_"
            "20260726T152102Z_v3"
        ),
        source_script=(
            REE_V3_ROOT
            / "experiments"
            / "v3_exq_825_mech245_generative_dominance_deafferentation.py"
        ),
        flat_manifest=(
            ROOT
            / "evidence"
            / "experiments"
            / "v3_exq_825_mech245_generative_dominance_deafferentation_"
            "20260726T152102Z_v3.json"
        ),
        run_manifest=(
            ROOT
            / "evidence"
            / "experiments"
            / "v3_exq_825_mech245_generative_dominance_deafferentation"
            / "runs"
            / "v3_exq_825_mech245_generative_dominance_deafferentation_"
            "20260726T152102Z_v3"
            / "manifest.json"
        ),
        run_metrics=(
            ROOT
            / "evidence"
            / "experiments"
            / "v3_exq_825_mech245_generative_dominance_deafferentation"
            / "runs"
            / "v3_exq_825_mech245_generative_dominance_deafferentation_"
            "20260726T152102Z_v3"
            / "metrics.json"
        ),
        run_summary=(
            ROOT
            / "evidence"
            / "experiments"
            / "v3_exq_825_mech245_generative_dominance_deafferentation"
            / "runs"
            / "v3_exq_825_mech245_generative_dominance_deafferentation_"
            "20260726T152102Z_v3"
            / "summary.md"
        ),
    )
}


def _require_file(path: Path) -> None:
    if not path.exists():
        raise ProfileError(f"authoritative source cannot be located: {display_path(path)}")


def display_path(path: Path) -> str:
    path = path.resolve()
    if path.is_relative_to(ROOT):
        return f"REE_assembly/{path.relative_to(ROOT)}"
    if path.is_relative_to(REE_V3_ROOT):
        return f"ree-v3/{path.relative_to(REE_V3_ROOT)}"
    if path.is_relative_to(WORKING_ROOT):
        return str(path.relative_to(WORKING_ROOT))
    return str(path)


def source_ref(path: Path, line_range: str | None = None) -> str:
    suffix = f":{line_range}" if line_range else ""
    return f"`{display_path(path)}{suffix}`"


def read_json(path: Path) -> Any:
    _require_file(path)
    return json.loads(path.read_text(encoding="utf-8"))


def read_yaml(path: Path) -> Any:
    _require_file(path)
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def sha256_file(path: Path) -> str:
    _require_file(path)
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_lines(cwd: Path, *args: str) -> list[str]:
    try:
        cp = subprocess.run(
            ["git", *args],
            cwd=str(cwd),
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as exc:
        raise ProfileError(
            f"git command failed in {display_path(cwd)}: git {' '.join(args)}\n"
            f"{exc.stderr.strip()}"
        ) from exc
    return [line for line in cp.stdout.splitlines() if line.strip()]


def git_first_commit(cwd: Path, relpath: str) -> str:
    lines = git_lines(cwd, "log", "--format=%H", "--follow", "--", relpath)
    if not lines:
        raise ProfileError(f"source commit missing for {display_path(cwd / relpath)}")
    return lines[0]


def git_blob(cwd: Path, commit: str, relpath: str) -> str:
    lines = git_lines(cwd, "ls-tree", commit, relpath)
    if not lines:
        raise ProfileError(f"git blob missing for {commit}:{relpath}")
    parts = lines[0].split()
    if len(parts) < 3:
        raise ProfileError(f"could not parse git blob for {commit}:{relpath}")
    return parts[2]


def line_range_between(path: Path, start: str, end: str | None = None) -> str:
    _require_file(path)
    lines = path.read_text(encoding="utf-8").splitlines()
    start_idx = next((i for i, line in enumerate(lines) if start in line), None)
    if start_idx is None:
        raise ProfileError(f"source marker not found in {display_path(path)}: {start}")
    if end is None:
        return str(start_idx + 1)
    end_idx = next(
        (i for i, line in enumerate(lines[start_idx + 1 :], start_idx + 1) if end in line),
        None,
    )
    if end_idx is None:
        raise ProfileError(f"source end marker not found in {display_path(path)}: {end}")
    return f"{start_idx + 1}-{end_idx}"


def docstring_for(path: Path) -> str:
    _require_file(path)
    module = ast.parse(path.read_text(encoding="utf-8"))
    doc = ast.get_docstring(module)
    if not doc:
        raise ProfileError(f"source script has no docstring: {display_path(path)}")
    return doc


def extract_commands(doc: str) -> list[str]:
    commands = []
    for line in doc.splitlines():
        stripped = line.strip()
        if stripped.startswith("/opt/local/bin/python3 "):
            commands.append(stripped)
    return commands


def find_claim(claim_id: str) -> dict[str, Any]:
    claims_path = ROOT / "docs" / "claims" / "claims.yaml"
    claims = read_yaml(claims_path)
    if not isinstance(claims, list):
        raise ProfileError("claims.yaml did not parse as a list")
    for claim in claims:
        if isinstance(claim, dict) and claim.get("id") == claim_id:
            return claim
    raise ProfileError(f"claim missing: {claim_id}")


def find_proposal(queue_id: str, claim_id: str) -> dict[str, Any]:
    path = ROOT / "evidence" / "planning" / "experiment_proposals.v1.json"
    data = read_json(path)
    items = data.get("items") if isinstance(data, dict) else None
    if not isinstance(items, list):
        raise ProfileError("experiment_proposals.v1.json did not contain an items list")
    for item in items:
        if (
            isinstance(item, dict)
            and item.get("executed_queue_id") == queue_id
            and item.get("claim_id") == claim_id
        ):
            return item
    raise ProfileError(f"proposal missing for {queue_id} / {claim_id}")


def section_sources(target: Target) -> dict[str, str]:
    claims_path = ROOT / "docs" / "claims" / "claims.yaml"
    proposal_path = ROOT / "evidence" / "planning" / "experiment_proposals.v1.json"
    pending_path = ROOT / "evidence" / "experiments" / "pending_review.md"
    default_mode = ROOT / "docs" / "architecture" / "default_mode.md"

    return {
        "claim": source_ref(
            claims_path,
            line_range_between(claims_path, "- id: MECH-245", "- id: MECH-246"),
        ),
        "mech246": source_ref(
            claims_path,
            line_range_between(claims_path, "- id: MECH-246", "- id: MECH-247"),
        ),
        "mech247": source_ref(
            claims_path,
            line_range_between(claims_path, "- id: MECH-247", "Registered 2026-04-16"),
        ),
        "mech094": source_ref(
            claims_path,
            line_range_between(
                claims_path,
                "The functional requirement registered by MECH-094",
                "pharmacological_predictions",
            ),
        ),
        "default_mode": source_ref(default_mode, "81-86"),
        "script_asserts": source_ref(
            target.source_script,
            line_range_between(target.source_script, "What MECH-245 asserts", "Substrate map"),
        ),
        "script_substrate": source_ref(
            target.source_script,
            line_range_between(target.source_script, "Substrate map", "Design"),
        ),
        "script_design": source_ref(
            target.source_script,
            line_range_between(target.source_script, "Design", "DV-SYMMETRY"),
        ),
        "script_dv_symmetry": source_ref(
            target.source_script,
            line_range_between(target.source_script, "DV-SYMMETRY DECLARATION", "Pre-registered metrics"),
        ),
        "script_metrics": source_ref(
            target.source_script,
            line_range_between(target.source_script, "Pre-registered metrics", "Pre-registered pass criteria"),
        ),
        "script_criteria": source_ref(
            target.source_script,
            line_range_between(target.source_script, "Pre-registered pass criteria", "Phased training"),
        ),
        "script_limitations": source_ref(
            target.source_script,
            line_range_between(target.source_script, "Phased training", "Run with:"),
        ),
        "script_run": source_ref(
            target.source_script,
            line_range_between(target.source_script, "Run with:", '"""'),
        ),
        "script_manifest": source_ref(
            target.source_script,
            line_range_between(target.source_script, "manifest = {", "out_path = write_flat_manifest"),
        ),
        "flat_manifest": source_ref(target.flat_manifest, "1"),
        "run_manifest": source_ref(target.run_manifest, "1-49"),
        "metrics": source_ref(target.run_metrics, "1-18"),
        "summary": source_ref(target.run_summary, "1-3"),
        "proposal": source_ref(
            proposal_path,
            line_range_between(proposal_path, '"backlog_id": "EVB-0122"', '"why_now"'),
        ),
        "pending": source_ref(
            pending_path,
            line_range_between(pending_path, f"`{target.run_id}`", "## Diagnostic"),
        ),
        "template": source_ref(TEMPLATE_PATH),
        "generator": source_ref(Path(__file__)),
    }


def fmt_float(value: Any, digits: int = 6) -> str:
    if isinstance(value, (int, float)):
        return f"{value:.{digits}g}"
    return str(value)


def bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def metric_table(metrics: dict[str, Any], criteria: dict[str, Any], sources: dict[str, str]) -> str:
    rows = [
        ("Outcome", "PASS" if criteria.get("overall_pass") else "FAIL", sources["flat_manifest"]),
        (
            "C1 confidence collapse",
            f"{criteria['c1_confidence_collapse_seeds_pass']}/{criteria['n_seeds']} seeds",
            sources["metrics"],
        ),
        (
            "C2 divergence magnitude",
            f"{criteria['c2_divergence_magnitude_seeds_pass']}/{criteria['n_seeds']} seeds",
            sources["metrics"],
        ),
        (
            "C3 manipulation validity",
            f"{criteria['c3_manipulation_validity_seeds_pass']}/{criteria['n_seeds']} seeds",
            sources["metrics"],
        ),
        (
            "Primary mean final variance",
            fmt_float(metrics["primary_mean_final_variance"]),
            sources["metrics"],
        ),
        (
            "Ablation mean final variance",
            fmt_float(metrics["ablation_mean_final_variance"]),
            sources["metrics"],
        ),
        (
            "Variance delta primary minus ablation",
            fmt_float(metrics["variance_delta_primary_minus_ablation"]),
            sources["metrics"],
        ),
        (
            "Ablation-primary would-commit fraction delta",
            fmt_float(metrics["would_commit_delta_ablation_minus_primary"]),
            sources["metrics"],
        ),
        (
            "Ground-truth drift at end",
            (
                f"primary={fmt_float(metrics['primary_mean_ground_truth_drift'])}; "
                f"ablation={fmt_float(metrics['ablation_mean_ground_truth_drift'])}"
            ),
            sources["metrics"],
        ),
    ]
    lines = ["| Field | Value | Source |", "|---|---:|---|"]
    for label, value, source in rows:
        lines.append(f"| {label} | `{value}` | {source} |")
    return "\n".join(lines)


def provenance_table(rows: list[tuple[str, str, str]]) -> str:
    lines = ["| Item | Value | Source |", "|---|---|---|"]
    for item, value, source in rows:
        safe_value = value.replace("|", "\\|")
        lines.append(f"| {item} | `{safe_value}` | {source} |")
    return "\n".join(lines)


def build_profile_data(target: Target) -> tuple[dict[str, str], list[dict[str, str]]]:
    for path in (
        target.source_script,
        target.flat_manifest,
        target.run_manifest,
        target.run_metrics,
        target.run_summary,
        TEMPLATE_PATH,
    ):
        _require_file(path)

    claim = find_claim(target.claim_id)
    proposal = find_proposal(target.queue_id, target.claim_id)
    flat = read_json(target.flat_manifest)
    run_manifest = read_json(target.run_manifest)
    metrics_pack = read_json(target.run_metrics)
    doc = docstring_for(target.source_script)
    commands = extract_commands(doc)
    if not commands:
        raise ProfileError("reproduction command missing from source script docstring")

    if not claim.get("title"):
        raise ProfileError(f"claim missing authoritative wording: {target.claim_id}")
    if not flat.get("evidence_direction"):
        raise ProfileError("evidence direction missing from flat manifest")

    sources = section_sources(target)

    source_rel = "experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py"
    flat_rel = (
        "evidence/experiments/"
        "v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3.json"
    )
    source_commit = git_first_commit(REE_V3_ROOT, source_rel)
    result_commit = git_first_commit(ROOT, flat_rel)
    source_blob = git_blob(REE_V3_ROOT, source_commit, source_rel)
    flat_blob = git_blob(ROOT, result_commit, flat_rel)

    embedded_source_commit = (
        run_manifest.get("source_repo", {}).get("commit")
        if isinstance(run_manifest.get("source_repo"), dict)
        else None
    )

    missing: list[dict[str, str]] = []
    if not flat.get("source_commit"):
        missing.append(
            {
                "field": "flat_manifest.source_commit",
                "source": sources["flat_manifest"],
                "status": "missing in manifest; populated from git history fallback",
                "fallback": source_commit,
            }
        )
    if not embedded_source_commit:
        missing.append(
            {
                "field": "run_pack.manifest.source_repo.commit",
                "source": sources["run_manifest"],
                "status": "empty string in run pack; populated from git history fallback",
                "fallback": source_commit,
            }
        )
    for field in ("source_hash", "commit_sha", "code_hash"):
        if not flat.get(field):
            missing.append(
                {
                    "field": f"flat_manifest.{field}",
                    "source": sources["flat_manifest"],
                    "status": "absent; SHA-256 and git blob IDs computed from repository files",
                    "fallback": "computed content hash",
                }
            )
    env = run_manifest.get("environment", {})
    if isinstance(env, dict):
        for key in ("dynamics_hash", "reward_hash", "observation_hash", "config_hash"):
            if env.get(key) == "unknown":
                missing.append(
                    {
                        "field": f"run_pack.manifest.environment.{key}",
                        "source": sources["run_manifest"],
                        "status": "recorded as unknown; no fallback located",
                        "fallback": "not populated",
                    }
                )
    if "reproduction" not in run_manifest:
        missing.append(
            {
                "field": "run_pack.manifest.reproduction",
                "source": sources["run_manifest"],
                "status": "absent; command extracted from source script docstring",
                "fallback": commands[0],
            }
        )
    if "limitations" not in flat and "limitations" not in run_manifest:
        missing.append(
            {
                "field": "manifest.limitations",
                "source": f"{sources['flat_manifest']}; {sources['run_manifest']}",
                "status": "absent as a structured field; documented caveats extracted from source script",
                "fallback": sources["script_dv_symmetry"],
            }
        )

    metrics = metrics_pack.get("values", flat.get("metrics", {}))
    criteria = flat.get("criteria", {})
    thresholds = flat.get("registered_thresholds", {})
    config = flat.get("config", {})

    limitations = [
        (
            "The ABLATION arm's per-tick prediction error is a definitional "
            "self-comparison; the driver identifies the falsifiable content as "
            "PRIMARY's deprivation-driven prediction-error magnitude, the C1/C2 "
            "confidence-collapse margins, and ground-truth drift. Sources: "
            f"{sources['script_dv_symmetry']}."
        ),
        (
            "`would_commit_fraction` is reported for interpretation but is not a "
            "gating criterion because the commit threshold is calibrated to real RL "
            "z_world scale, not this synthetic scale. Sources: "
            f"{sources['script_metrics']}."
        ),
        (
            "The forward model is a synthetic GRU stand-in for the top-down "
            "generative pathway; the driver states no head is trained on real "
            "z_world, z_harm, or encoder output. Sources: "
            f"{sources['script_limitations']}."
        ),
        (
            "Embedded run-pack provenance is incomplete: `source_repo.commit` is "
            "empty and the environment dynamics, reward, observation, and config "
            "hashes are recorded as `unknown`; Git-history and content-hash "
            "fallbacks are listed below. Sources: "
            f"{sources['run_manifest']}."
        ),
    ]
    if not limitations:
        raise ProfileError("limitations absent")

    scientific_question = (
        "This experiment asks whether the MECH-245 hallucination pathway is "
        "reproduced when bottom-up grounding is absent and the system's own "
        "top-down prediction is substituted as the observation at E3's "
        "bottom-up mismatch-check call site. The driver states that PRIMARY "
        "keeps the mismatch check intact by feeding the last genuinely grounded "
        "observation, while ABLATION substitutes the model prediction as if it "
        "were received sensory input. Sources: "
        f"{sources['script_asserts']}; {sources['script_substrate']}; "
        f"{sources['script_design']}."
    )

    claim_quote = (
        f"Authoritative claim wording: \"{claim['title']}\" The claim notes specify "
        "that hallucination is a perceptual generation failure in which E1 top-down "
        "predictions propagate forward as if they were received sensory signals, "
        "bypassing or overwhelming the bottom-up mismatch check. Sources: "
        f"{sources['claim']}."
    )

    competing = bullet_list(
        [
            (
                "MECH-094 is documented as confabulation, a memory write-gate or "
                "source-monitoring failure, not the percept-generation pathway "
                f"tested here. Sources: {sources['script_asserts']}; {sources['mech094']}."
            ),
            (
                "MECH-244 is documented as a precision-weighting or belief-updating "
                "failure where bottom-up evidence is present but resisted. Sources: "
                f"{sources['script_asserts']}; {sources['claim']}."
            ),
            (
                "MECH-246 is documented as signal-degradation or pareidolia: "
                "bottom-up input is present but too degraded, sparse, or ambiguous "
                f"to constrain inference. Sources: {sources['mech246']}."
            ),
            (
                "MECH-247 is documented as trauma-shaped hypervigilant priors: "
                "pathological prior structure generates strong top-down predictions "
                f"from minimal threat-relevant signals. Sources: {sources['mech247']}."
            ),
        ]
    )

    design = bullet_list(
        [
            (
                "Manipulation: after a shared grounding phase, the deafferentation "
                "window removes sensory input; PRIMARY feeds E3 the last genuinely "
                "grounded observation, while ABLATION feeds E3 the model's own "
                f"rolled-forward prediction. Sources: {sources['script_design']}."
            ),
            (
                "Controls: both arms use the same seed, same trained forward model, "
                "same true trajectory continuation, and identical grounding phase, "
                "so they enter the manipulation window from the same confidence "
                f"state. Sources: {sources['script_design']}."
            ),
            (
                "Dependent variables: grounded operating variance, final running "
                "variance, current precision, deafferentation mean absolute "
                "prediction error, would-commit fraction, and ground-truth drift at "
                f"the end of the rollout. Sources: {sources['script_metrics']}."
            ),
            (
                "Discriminative logic: support requires PRIMARY uncertainty to rise "
                "under honest sensory absence while ABLATION sustains low variance "
                "and high confidence when top-down content is substituted for "
                f"bottom-up input. Sources: {sources['script_criteria']}; "
                f"{sources['flat_manifest']}."
            ),
        ]
    )

    falsification = bullet_list(
        [
            (
                f"C1 would fail if fewer than {criteria['min_seeds_required']} of "
                f"{criteria['n_seeds']} seeds show PRIMARY final variance / grounded "
                f"variance >= {thresholds['C1_PRIMARY_MIN_VARIANCE_RATIO']} and "
                "ABLATION final variance / grounded variance <= "
                f"{thresholds['C1_ABLATION_MAX_VARIANCE_RATIO']}. Sources: "
                f"{sources['script_criteria']}; {sources['flat_manifest']}."
            ),
            (
                f"C2 would fail if fewer than {criteria['min_seeds_required']} of "
                f"{criteria['n_seeds']} seeds show "
                "(primary_final_var - ablation_final_var) / grounded variance >= "
                f"{thresholds['C2_MIN_DIVERGENCE_RATIO']}. Sources: "
                f"{sources['script_criteria']}; {sources['flat_manifest']}."
            ),
            (
                f"C3 would fail if fewer than {criteria['min_seeds_required']} of "
                f"{criteria['n_seeds']} seeds show PRIMARY/ABLATION deafferentation "
                f"prediction-error ratio >= {thresholds['C3_MIN_PE_ARM_RATIO']} and "
                "PRIMARY deafferentation prediction error / grounded mean absolute "
                f"prediction error >= {thresholds['C3_MIN_SURPRISE_RATIO']}. Sources: "
                f"{sources['script_criteria']}; {sources['flat_manifest']}."
            ),
            (
                "Overall PASS requires C1, C2, and C3 in at least "
                f"ceil(n_seeds * {thresholds['PASS_FRACTION_REQUIRED']}) seeds; "
                "otherwise the manifest direction would be `weakens` rather than "
                f"`supports`. Sources: {sources['script_criteria']}; "
                f"{sources['script_manifest']}."
            ),
        ]
    )

    actual = (
        "The archived run records `outcome=PASS`, `result=PASS`, "
        "`evidence_direction=supports`, and all three criteria passing in 3/3 seeds "
        f"with 2 seeds required. Sources: {sources['flat_manifest']}; "
        f"{sources['metrics']}. \n\n"
        f"{metric_table(metrics, criteria, sources)}"
    )

    interpretation = (
        "The manifest summary states that PASS maps to "
        "`evidence_direction=supports`: PRIMARY sensory absence raised variance "
        "from the grounded operating point, while ABLATION sustained false "
        "confidence when the generative prediction was substituted for missing "
        "bottom-up input. This profile does not mark the run reviewed; "
        "`pending_review.md` still lists the run under PASS verify-and-close. "
        f"Sources: {sources['flat_manifest']}; {sources['pending']}."
    )

    reproduction = (
        "Run from `/Users/dgolden/REE_Working/ree-v3` with the exact command below. "
        "A fresh run writes a new timestamped flat manifest under "
        "`REE_assembly/evidence/experiments/`; the archived reference run is the "
        f"`{target.run_id}` output listed in Expected outputs. Sources: "
        f"{sources['script_run']}; {sources['script_manifest']}.\n\n"
        "```bash\n"
        f"{commands[0]}\n"
        "```\n\n"
        "Dry-run smoke command, documented by the same source, is available for "
        f"path validation. Sources: {sources['script_run']}.\n\n"
        "```bash\n"
        f"{commands[1] if len(commands) > 1 else commands[0] + ' --dry-run'}\n"
        "```"
    )

    provenance_rows = [
        ("Required repo", "ree-v3", sources["script_run"]),
        ("Required repo", "REE_assembly", sources["run_manifest"]),
        ("Driver source commit", source_commit, sources["generator"]),
        ("Result-pack commit", result_commit, sources["generator"]),
        ("Driver git blob", source_blob, sources["generator"]),
        ("Flat manifest git blob", flat_blob, sources["generator"]),
        ("Driver SHA-256", sha256_file(target.source_script), sources["generator"]),
        ("Flat manifest SHA-256", sha256_file(target.flat_manifest), sources["generator"]),
        ("Run-pack manifest SHA-256", sha256_file(target.run_manifest), sources["generator"]),
        ("Substrate hash", flat.get("substrate_hash", ""), sources["flat_manifest"]),
    ]

    expected = bullet_list(
        [
            (
                f"Archived flat manifest: `{display_path(target.flat_manifest)}` with "
                "`outcome=PASS` and `evidence_direction=supports`. Sources: "
                f"{sources['flat_manifest']}."
            ),
            (
                f"Archived run pack: `{display_path(target.run_manifest.parent)}` with "
                "`manifest.json`, `metrics.json`, and `summary.md`. Sources: "
                f"{sources['run_manifest']}; {sources['metrics']}; {sources['summary']}."
            ),
            (
                "Expected criteria shape for a fresh reproduction: C1, C2, and C3 "
                "all pass with the configured matched seeds `[0, 1, 2]`. Sources: "
                f"{sources['flat_manifest']}; {sources['metrics']}."
            ),
        ]
    )

    page_data = {
        "queue_id": target.queue_id,
        "claim_id": target.claim_id,
        "experiment_type": target.experiment_type,
        "run_id": target.run_id,
        "generated_by": f"{sources['generator']}; {sources['template']}",
        "scientific_question": scientific_question,
        "claim_under_test": claim_quote,
        "competing_explanations": competing,
        "experimental_design": design,
        "falsification": falsification,
        "actual": actual,
        "interpretation": interpretation,
        "limitations": bullet_list(limitations),
        "reproduction": reproduction,
        "expected_outputs": expected,
        "provenance": provenance_table(provenance_rows),
        "proposal_context": (
            "The experiment proposal records backlog EVB-0122 as executed by "
            "V3-EXQ-825, with objective `Reduce uncertainty for MECH-245 via "
            "targeted experiment runs.` Sources: "
            f"{sources['proposal']}."
        ),
        "source_commit": source_commit,
        "result_commit": result_commit,
        "evidence_direction": flat["evidence_direction"],
        "outcome": flat["outcome"],
        "report_path": (
            "v3_exq_825_mech245_generative_dominance_deafferentation.population_report.md"
        ),
    }
    return page_data, missing


def render_template(data: dict[str, str]) -> str:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    return template.format(**data)


def render_report(target: Target, missing: list[dict[str, str]], data: dict[str, str]) -> str:
    lines = [
        f"# Population Report: {target.queue_id} / {target.claim_id}",
        "",
        (
            "This report lists fields that were absent, empty, or placeholder-valued "
            "in repository artifacts and therefore could not be populated directly "
            f"from their preferred structured location. Sources: {data['generated_by']}."
        ),
        "",
        "## Required Fields",
        "",
        "| Field | Value | Source |",
        "|---|---|---|",
        f"| source_commit | `{data['source_commit']}` | generator Git-history fallback |",
        f"| result_commit | `{data['result_commit']}` | generator Git-history fallback |",
        f"| claim | `{target.claim_id}` | claim registry |",
        f"| reproduction command | present | source script docstring |",
        f"| evidence_direction | `{data['evidence_direction']}` | flat manifest |",
        f"| limitations | present | source script caveat sections |",
        "",
        "## Missing Or Placeholder Fields",
        "",
    ]
    if not missing:
        lines.append("No missing or placeholder fields were detected.")
    else:
        lines.extend(["| Field | Repository status | Fallback used | Source |", "|---|---|---|---|"])
        for item in missing:
            lines.append(
                f"| `{item['field']}` | {item['status']} | `{item['fallback']}` | "
                f"{item['source']} |"
            )
    lines.append("")
    return "\n".join(lines)


def validate_profile(markdown: str, data: dict[str, str]) -> None:
    if "TODO" in markdown:
        raise ProfileError("validation failed: TODO remains in generated page")
    required_sections = [
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
    ]
    for section in required_sections:
        if f"## {section}" not in markdown:
            raise ProfileError(f"validation failed: missing section {section}")
    required_fields = {
        "source_commit": "source commit missing",
        "claim_id": "claim missing",
        "evidence_direction": "evidence direction missing",
    }
    for key, message in required_fields.items():
        if not data.get(key):
            raise ProfileError(f"validation failed: {message}")
    if "/opt/local/bin/python3 experiments/" not in markdown:
        raise ProfileError("validation failed: reproduction command missing")
    if "## Limitations" not in markdown or "synthetic GRU stand-in" not in markdown:
        raise ProfileError("validation failed: limitations absent")
    for para in _paragraphs(markdown):
        if _requires_source_marker(para) and "Sources:" not in para and "Source:" not in para:
            raise ProfileError(f"validation failed: paragraph lacks provenance: {para[:120]}")


def _paragraphs(markdown: str) -> list[str]:
    chunks: list[str] = []
    current: list[str] = []
    in_code = False
    for line in markdown.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if not line.strip():
            if current:
                chunks.append("\n".join(current).strip())
                current = []
            continue
        current.append(line)
    if current:
        chunks.append("\n".join(current).strip())
    return chunks


def _requires_source_marker(paragraph: str) -> bool:
    if not paragraph:
        return False
    if paragraph.startswith("#"):
        return False
    if paragraph.startswith("|"):
        return False
    return any(ch.isalpha() for ch in paragraph)


def write_outputs(target: Target, out_dir: Path) -> tuple[Path, Path]:
    data, missing = build_profile_data(target)
    markdown = render_template(data)
    validate_profile(markdown, data)

    out_dir.mkdir(parents=True, exist_ok=True)
    profile_path = out_dir / f"{target.experiment_type}.md"
    report_path = out_dir / f"{target.experiment_type}.population_report.md"
    profile_path.write_text(markdown, encoding="utf-8")
    report_path.write_text(render_report(target, missing, data), encoding="utf-8")
    return profile_path, report_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue-id", default="V3-EXQ-825", choices=sorted(TARGETS))
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    args = parser.parse_args(argv)

    target = TARGETS[args.queue_id]
    try:
        profile_path, report_path = write_outputs(target, args.out_dir)
    except ProfileError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Wrote {display_path(profile_path)}")
    print(f"Wrote {display_path(report_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
