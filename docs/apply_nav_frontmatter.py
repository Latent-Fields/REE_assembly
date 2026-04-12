"""
apply_nav_frontmatter.py
One-shot script: adds/updates Jekyll frontmatter on all docs/ files to produce
a clean Just-the-Docs nav structure.

Run from repo root:
  /opt/local/bin/python3 docs/apply_nav_frontmatter.py

Safe to re-run: it reads the current file, strips existing frontmatter if
present, then prepends the canonical block.
"""

import os
import re

DOCS = "/Users/dgolden/Documents/GitHub/REE_Working/REE_assembly/docs"
ARCH = os.path.join(DOCS, "architecture")

# ---------------------------------------------------------------------------
# Frontmatter spec
# Key = repo-relative path from DOCS root
# Value = dict of frontmatter keys (only the ones we want to set/overwrite)
# ---------------------------------------------------------------------------

SPEC = {}

# --- Top-level visible pages (ordered) ------------------------------------

# index.md is rewritten separately with Write tool -- skip here
# vignettes.md already has correct frontmatter -- skip

SPEC["invariants.md"]          = {"title": "Invariants",     "nav_order": 5}
SPEC["roadmap.md"]             = {"title": "Roadmap",        "nav_order": 6}
SPEC["glossary.md"]            = {"title": "Glossary",       "nav_order": 7}
SPEC["REE_failure_modes.md"]   = {"title": "Failure Modes",  "nav_order": 8}
SPEC["vignettes.md"]           = {"title": "Vignettes",      "nav_order": 9}

# --- Top-level hidden (accessible by link, not in sidebar) ----------------

for f in [
    "FINAL_OUTPUT.md",
    "MIGRATION.md",
    "REE_ARCHITECTURE_SNAPSHOT_2026-02-17.md",
    "REE_MIN_SPEC.md",
    "REE_overview.md",
    "V1_PROGRESS_AND_LEARNING.md",
    "changelog.md",
    "repo_meta.md",
    "README.md",
]:
    SPEC[f] = {"nav_exclude": True}

# --- Architecture: featured top-level pages (no parent) -------------------

SPEC["architecture/ethical_agency_derivation.md"] = {
    "title": "Why This Architecture?",
    "nav_order": 2,
}
SPEC["architecture/five_axioms_foundations.md"] = {
    "title": "Foundations",
    "nav_order": 4,
}

# --- Architecture: parent page --------------------------------------------

SPEC["architecture/overview.md"] = {
    "title": "Architecture",
    "nav_order": 3,
    "has_children": True,
}

# --- Architecture: visible children (under Architecture parent) -----------

SPEC["architecture/e1.md"]                 = {"title": "E1 -- Deep Predictor",       "parent": "Architecture", "nav_order": 1}
SPEC["architecture/e2.md"]                 = {"title": "E2 -- Fast Predictor",       "parent": "Architecture", "nav_order": 2}
SPEC["architecture/e3.md"]                 = {"title": "E3 -- Trajectory Selector",  "parent": "Architecture", "nav_order": 3}
SPEC["architecture/l_space.md"]            = {"title": "L-space",                    "parent": "Architecture", "nav_order": 4}
SPEC["architecture/control_plane.md"]      = {"title": "Control Plane",              "parent": "Architecture", "nav_order": 5}
SPEC["architecture/hippocampal_systems.md"]= {"title": "Hippocampal Systems",        "parent": "Architecture", "nav_order": 6}
SPEC["architecture/default_mode.md"]       = {"title": "Default Mode",               "parent": "Architecture", "nav_order": 7}
SPEC["architecture/residue_geometry.md"]   = {"title": "Residue",                    "parent": "Architecture", "nav_order": 8}

# --- Architecture: exclude everything else --------------------------------

ARCH_EXCLUDE = [
    "agency_responsibility_flow.md",
    "arc_033_e2_harm_s_forward_model.md",
    "arcuate_fasciculus.md",
    "astrocyte_regulatory_stack.md",
    "compact_consolidation_principle.md",
    "control_plane_heartbeat.md",
    "control_plane_signal_map.md",
    "developmental_curriculum.md",
    "diagram_views.md",
    "e1_e2_constraint_propagation.md",
    "efficiency_dimensionality_hypothesis.md",
    "entities_and_binding.md",
    "frontal_cue_integration.md",
    "goal_wanting_signal_chain.md",
    "hippocampal_braid.md",
    "hippocampal_literature_synthesis_2026.md",
    "hook_surface_contract.md",
    "jepa_e1e2_integration_contract.md",
    "jepa_ree_hybrid_diagram_spec.md",
    "language.md",
    "mode_manager.md",
    "modes_of_cognition.md",
    "neuromodulatory_control_planes.md",
    "papez_circuit.md",
    "path_authority_and_interrupts.md",
    "play_mode.md",
    "precision_control.md",
    "precision_scoping.md",
    "psychiatric_failure_modes.md",
    "ree_v2_repo_bootstrap_spec.md",
    "ree_v2_spec.md",
    "sd015_hippocampal_nav_session_prompt.md",
    "sd_003_experiment_design.md",
    "sd_004_sd_005_encoder_codesign.md",
    "sd_010_harm_stream_separation.md",
    "sd_011_dual_nociceptive_streams.md",
    "sd_012_homeostatic_drive.md",
    "sd_013_e2_harm_s_interventional_training.md",
    "sd_015_z_resource_encoder.md",
    "sd_016_frontal_cue_integration.md",
    "sd_017_sleep_phase_architecture.md",
    "sd_019_harm_nonredundancy.md",
    "sd_020_harm_surprise_pe.md",
    "sd_021_descending_pain_modulation.md",
    "sd_022_directional_limb_damage.md",
    "sd_023_environmental_gradient_texture.md",
    "sensory_stream_tags.md",
    "serotonin.md",
    "sleep.md",
    "social.md",
    "state.md",
    "streams.md",
    "temporal_dynamics.md",
    "three_loop_learning_channels.md",
    "tpj_agency_comparator.md",
    "trajectory_selection.md",
    "v2_v3_transition_roadmap.md",
    "v3_v4_transition_boundary.md",
    "valenced_hippocampal_map.md",
    "vmPFC.md",
    "why_attention_must_be_fragmented.md",
]

for f in ARCH_EXCLUDE:
    SPEC["architecture/" + f] = {"nav_exclude": True}

# Subdirectory files -- all excluded
for subdir in ["language", "sleep"]:
    subpath = os.path.join(ARCH, subdir)
    if os.path.isdir(subpath):
        for fname in os.listdir(subpath):
            if fname.endswith(".md"):
                SPEC["architecture/{}/{}".format(subdir, fname)] = {"nav_exclude": True}

# Claims and conflicts subdirectory files
for subdir in ["claims", "conflicts"]:
    subpath = os.path.join(DOCS, subdir)
    if os.path.isdir(subpath):
        for fname in os.listdir(subpath):
            if fname.endswith(".md"):
                SPEC["{}/{}".format(subdir, fname)] = {"nav_exclude": True}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def strip_existing_frontmatter(text):
    """Remove existing --- block if present. Returns (fm_dict, body)."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    fm_text = text[4:end]
    body = text[end + 5:]  # skip \n---\n
    fm = {}
    for line in fm_text.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    return fm, body


def render_frontmatter(fm):
    """Render a frontmatter dict to a --- block string."""
    lines = ["---"]
    for k, v in fm.items():
        if isinstance(v, bool):
            lines.append("{}: {}".format(k, str(v).lower()))
        elif isinstance(v, int):
            lines.append("{}: {}".format(k, v))
        else:
            # Quote strings that contain special chars
            if any(c in str(v) for c in [":", "{", "}", "[", "]", "#", "&", "*", "!", "|", ">", "'", '"', "%", "@", "`"]):
                lines.append('{}: "{}"'.format(k, str(v).replace('"', '\\"')))
            else:
                lines.append("{}: {}".format(k, v))
    lines.append("---")
    return "\n".join(lines) + "\n"


def apply(rel_path, new_keys):
    abs_path = os.path.join(DOCS, rel_path)
    if not os.path.exists(abs_path):
        print("SKIP (not found): {}".format(rel_path))
        return

    with open(abs_path, "r", encoding="utf-8") as f:
        text = f.read()

    existing_fm, body = strip_existing_frontmatter(text)

    # Merge: new_keys take precedence
    merged = dict(existing_fm)
    merged.update(new_keys)

    new_text = render_frontmatter(merged) + "\n" + body.lstrip("\n")

    with open(abs_path, "w", encoding="utf-8") as f:
        f.write(new_text)

    print("OK: {}".format(rel_path))


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    for rel_path, keys in SPEC.items():
        apply(rel_path, keys)
    print("\nDone. {} files processed.".format(len(SPEC)))
