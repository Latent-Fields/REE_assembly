"""Steward integrity detectors (stage 1).

Each detector module exposes:

    DETECTOR_ID     str, e.g. "D-002"
    DETECTOR_TITLE  str
    run(ctx) -> (list[finding_dict], summary_dict)

Detectors are READ ONLY. Stage 1 has no auto-fix path: a detector reports, and
adjudication is a separate, human-routed step. Findings are built with
_common.finding() so the schema cannot drift between detectors.
"""

from . import (  # noqa: F401
    d001_phase_generation_mismatch,
    d002_orphan_v3_claim,
    d010_denominator_integrity,
)

# Registry order is report order. Keep D-002 first: it is the validated
# detector (precision 4/4) and the one the tier exists for.
DETECTORS = [
    d002_orphan_v3_claim,
    d001_phase_generation_mismatch,
    d010_denominator_integrity,
]
