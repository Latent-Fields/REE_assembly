# Dormant / Chronic High-Conflict Watchlist

Generated: `2026-09-03T20:19:25.213972Z`

No-deadline visibility report. Lists claims with `conflict_ratio >= 0.55` and an unresolved decision, but invisible to the `mandatory_decision_checkpoint` (which requires `conflict_ratio >= 0.8` AND fresh recent batches). Deliberately carries no deadline -- see `evidence_backlog.v1.json` -> `dormant_high_conflict` for the source record and the full rationale in `build_experiment_indexes.py`.

- `dormant_low_activity` -- conflict is real but nobody has run enough recent evidence against the claim to meet the mandatory-checkpoint batch floor.
- `chronic_under_threshold` -- worked heavily, but `conflict_ratio` never quite crosses the mandatory bar, so it is reworked indefinitely without ever being forced to a decision.

Sorted worst-conflict-first.

| claim_id | pattern | conflict_ratio | current_status | recent_targeted_batches |
|---|---|---|---|---|
| `Q-084` | `dormant_low_activity` | 1 | `candidate` | 0 |
| `Q-090` | `dormant_low_activity` | 1 | `candidate` | 0 |
| `SD-031` | `dormant_low_activity` | 1 | `candidate` | 1 |
| `MECH-074d` | `chronic_under_threshold` | 0.857 | `candidate` | 6 |
| `MECH-295` | `chronic_under_threshold` | 0.833 | `candidate` | 16 |
| `ARC-024` | `chronic_under_threshold` | 0.783 | `provisional` | 15 |
| `SD-015` | `chronic_under_threshold` | 0.737 | `candidate` | 24 |
| `MECH-116` | `chronic_under_threshold` | 0.727 | `candidate` | 7 |
| `SD-007` | `chronic_under_threshold` | 0.692 | `implemented` | 18 |
| `ARC-073` | `dormant_low_activity` | 0.667 | `candidate` | 0 |
| `EXT-003` | `dormant_low_activity` | 0.667 | `candidate` | 1 |
| `EXT-004` | `dormant_low_activity` | 0.667 | `candidate` | 1 |
| `INV-047` | `chronic_under_threshold` | 0.667 | `candidate` | 10 |
| `INV-087` | `dormant_low_activity` | 0.667 | `candidate` | 1 |
| `MECH-073` | `chronic_under_threshold` | 0.667 | `provisional` | 3 |
| `MECH-112` | `chronic_under_threshold` | 0.667 | `candidate` | 23 |
| `MECH-118` | `chronic_under_threshold` | 0.667 | `candidate` | 4 |
| `MECH-130` | `dormant_low_activity` | 0.667 | `candidate` | 0 |
| `MECH-143` | `chronic_under_threshold` | 0.667 | `candidate` | 4 |
| `MECH-152` | `chronic_under_threshold` | 0.667 | `provisional` | 4 |
| `MECH-333` | `chronic_under_threshold` | 0.667 | `candidate` | 7 |
| `MECH-445` | `chronic_under_threshold` | 0.667 | `candidate` | 8 |
| `MECH-459` | `dormant_low_activity` | 0.667 | `candidate` | 1 |
| `MECH-466` | `dormant_low_activity` | 0.667 | `candidate` | 1 |
| `MECH-471` | `chronic_under_threshold` | 0.667 | `candidate` | 3 |
| `MECH-489` | `chronic_under_threshold` | 0.667 | `candidate` | 3 |
| `Q-001` | `dormant_low_activity` | 0.667 | `active` | 1 |
| `Q-007` | `chronic_under_threshold` | 0.667 | `active` | 5 |
| `Q-055` | `dormant_low_activity` | 0.667 | `open` | 0 |
| `Q-074` | `dormant_low_activity` | 0.667 | `candidate` | 0 |
| `Q-082` | `dormant_low_activity` | 0.667 | `candidate` | 0 |
| `SD-078` | `chronic_under_threshold` | 0.667 | `candidate_substrate_landed` | 6 |
| `MECH-090` | `chronic_under_threshold` | 0.625 | `active` | 24 |
| `MECH-093` | `chronic_under_threshold` | 0.615 | `provisional` | 19 |
| `SD-049` | `chronic_under_threshold` | 0.615 | `candidate` | 14 |
| `MECH-071` | `chronic_under_threshold` | 0.606 | `provisional` | 21 |
| `MECH-099` | `chronic_under_threshold` | 0.6 | `candidate` | 6 |
| `MECH-128` | `chronic_under_threshold` | 0.571 | `candidate` | 3 |
