"""serve.py's cusp-rail "substrate_ready" items must agree with the canonical
`_substrate_ready_items()` in scripts/generate_inter_governance_workset.py.

WHAT THIS PINS
---------------
serve.py's `_enrich_closure_v2()` used to build the cusp panel's
"substrate_ready" list by reading `implementation_status` ALONE, exact-matching
against `{"implemented", "done", "complete"}`, with no fallback to the
free-text `status` field. `implementation_status` is blank on the majority of
real substrate_queue.json entries (95/161 measured 2026-08-19); the real state
lives in `status`. So already-built substrate was advertised on the dashboard
as buildable-now work -- a 17x over-count (34 items) against the canonical
consumer's 2, confirmed against the live file the same day.

The fix (`_cusp_substrate_ready_items`, serve.py) delegates to
`generate_inter_governance_workset._substrate_resolved` /
`_substrate_implementation_complete` -- the same classifiers
`_substrate_ready_items()` itself uses -- so the two consumers cannot silently
diverge again. This file asserts that agreement directly, on both a synthetic
fixture covering the specific already-built shapes that were being
mis-surfaced and a differential check against the real repo file.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


def load_serve():
    """Import REE_assembly/serve.py under its own name (see
    tests/test_machines_canonical_identity.py for why: load by path so the
    import does not depend on the cwd pytest was invoked from)."""
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    spec = importlib.util.spec_from_file_location("serve", ROOT / "serve.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_igw():
    scripts_dir = ROOT / "scripts"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))
    spec = importlib.util.spec_from_file_location(
        "generate_inter_governance_workset", scripts_dir / "generate_inter_governance_workset.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def serve():
    return load_serve()


@pytest.fixture(scope="module")
def igw():
    return load_igw()


def _canonical_sd_ids(igw, tmp_path, entries) -> set[str]:
    """Run the real generator's `_substrate_ready_items()` over `entries` by
    pointing its module-level SUBSTRATE_QUEUE at a tmp fixture file -- the
    same file `_load_substrate_queue()` reads on every call (nothing there is
    cached)."""
    fixture = tmp_path / "substrate_queue.json"
    fixture.write_text(json.dumps({"queue": entries}), encoding="utf-8")
    orig = igw.SUBSTRATE_QUEUE
    igw.SUBSTRATE_QUEUE = fixture
    try:
        return {it.get("sd_id") for it in igw._substrate_ready_items()}
    finally:
        igw.SUBSTRATE_QUEUE = orig


def _cusp_sd_ids(serve, entries) -> set[str]:
    items = serve._cusp_substrate_ready_items({"queue": entries})
    assert all(it["kind"] == "substrate_ready" for it in items)
    return {it["sd_id"] for it in items}


# ---------------------------------------------------------------------------
# The defect: implementation_status blank, real state in `status`.
# ---------------------------------------------------------------------------

FIXTURE_ENTRIES = [
    # Already built, but implementation_status is blank -- the shape that was
    # being mis-surfaced (e.g. SD-047/SD-048 shape, measured 2026-08-19).
    {"sd_id": "SD-ALREADY-BUILT-1", "ready": True,
     "implementation_status": None, "status": "implemented"},
    {"sd_id": "SD-ALREADY-BUILT-2", "ready": True,
     "implementation_status": "", "status": "implemented_pending_validation"},
    # Genuinely buildable: ready, no terminal status anywhere.
    {"sd_id": "SD-GENUINELY-READY", "ready": True,
     "implementation_status": None, "status": None},
    # Not ready at all -- must never appear regardless of status.
    {"sd_id": "SD-NOT-READY", "ready": False,
     "implementation_status": None, "status": None},
    # Old exact-match shape (implementation_status == "implemented") --
    # the pre-fix code caught this one too; must stay suppressed.
    {"sd_id": "SD-OLD-SHAPE-BUILT", "ready": True,
     "implementation_status": "implemented", "status": None},
]


def test_cusp_matches_canonical_on_synthetic_fixture(serve, igw, tmp_path):
    cusp = _cusp_sd_ids(serve, FIXTURE_ENTRIES)
    canonical = _canonical_sd_ids(igw, tmp_path, FIXTURE_ENTRIES)

    assert cusp == canonical
    assert cusp == {"SD-GENUINELY-READY"}, (
        "already-built entries (status-only or implementation_status-only) "
        "must not be surfaced as buildable-now cusp work")


def test_blank_implementation_status_no_longer_leaks_through(serve):
    """The specific regression: implementation_status blank + status terminal
    used to be surfaced because the old code never consulted `status`."""
    cusp = _cusp_sd_ids(serve, [
        {"sd_id": "SD-REGRESSION", "ready": True,
         "implementation_status": None, "status": "implemented"},
    ])
    assert cusp == set()


def test_genuinely_ready_entry_still_surfaces(serve):
    cusp = _cusp_sd_ids(serve, [
        {"sd_id": "SD-STILL-READY", "ready": True,
         "implementation_status": None, "status": None},
    ])
    assert cusp == {"SD-STILL-READY"}


# ---------------------------------------------------------------------------
# Differential check against the real, live repo file.
# ---------------------------------------------------------------------------

def test_cusp_matches_canonical_on_the_real_repo_file(serve, igw):
    """Not just a shape check -- the two consumers must agree on the actual
    substrate_queue.json in this repo, which is what the dashboard renders."""
    sq_path = ROOT / "evidence" / "planning" / "substrate_queue.json"
    if not sq_path.exists():
        pytest.skip("substrate_queue.json not present in this checkout")
    sq = json.loads(sq_path.read_text(encoding="utf-8"))

    cusp = {it["sd_id"] for it in serve._cusp_substrate_ready_items(sq)}
    canonical = {it.get("sd_id") for it in igw._substrate_ready_items()}

    assert cusp == canonical
