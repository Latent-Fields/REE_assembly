# Thought Intake Audit Report

Generated: `2026-08-09T18:12:01.981598Z`

Ground-truth cross-check of both thought-intake paths against `docs/claims/claims.yaml` -- not a keyword/marker check. See `docs/thoughts/README.md` for what the two paths are and `docs/thoughts/scripts/thought_intake_audit.py` module docstring for the method.

## Stage 1 (raw capture, this folder) -- broken `Processed in:` links

A thought marked `processed` that points at a claim ID no longer in `claims.yaml` (renamed, merged, retracted since the link was written). `thought_sweep.py` cannot see this -- it only checks the link block exists, never that its targets are real.

- _none -- every `Processed in:` claim reference resolves._

## Stage 2 (structured analysis, evidence/planning/thought_intake_*.md)

| metric | count |
|---|---|
| total structured intakes | 80 |
| orphaned / explicitly unregistered | 1 |
| candidate section present, no IDs named (needs a human read) | 1 |
| all named candidate IDs registered | 53 |
| no candidate-claims section (nothing to check) | 25 |

### Orphaned / unregistered -- action needed

- `thought_intake_2026-08-07_dynamic_goal_structure_relational_possibility_topology.md` -- explicit "not registered" prose, no concrete IDs named yet

### Needs a human read -- candidate section present, no ID to check

- `thought_intake_2026-08-09_failure_autopsy_failure_location_buckets.md`

Caveat: this audit only catches candidates that were given a claim-shaped ID (real or placeholder). A file with no 'Candidate claims'-style header at all is assumed to have nothing pending (per the README, some intakes are folded directly into canonical docs with no separate candidate list) -- that assumption is not independently verified here.
