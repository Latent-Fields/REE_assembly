# review_tracker.json — Reference Summary

> Maintained manually alongside `review_tracker.json`. Update when adding run IDs.
> Purpose: lets Claude sessions know the tracker state without reading the full 47k-token file.

## Stats (last updated 2026-03-27)

- **Total reviewed run IDs**: ~1150
- **Last review UTC**: 2026-03-27T19:00:00Z
- **Discussed experiment dirs**: 36 entries (V1/V2 dirs and bare queue IDs not in run_id format)

## Coverage by experiment series

| Series | Run ID pattern | Status |
|--------|---------------|--------|
| V1/early synthetic | `2026-02-13T*` | All reviewed |
| V2 genuine (EXQ-014–028) | `*_v2` | All reviewed |
| V3 EXQ-001–068 | `v3_exq_0[0-6]*_v3` | All reviewed |
| V3 EXQ-066–100 | `v3_exq_0[6-9]*_v3`, `v3_exq_100*` | All reviewed (including 2026-03-27 evening batch) |
| V3 onboarding (Daniel-PC) | `v3_onboard_smoke_*` | All reviewed |
| V3 scale benchmark | `v3_scale_benchmark_*` | Reviewed 2026-03-23 |

## How to update review_tracker.json efficiently

Because the file is ~1400 lines, use targeted edits:

1. **Read only the tail** to find the last entry: `Read` with `offset=1385, limit=15`
2. **Edit** — replace the last entry + closing `]` with last entry + new IDs + `]`
3. **Update `last_review_utc`** — targeted Edit on line 3 only
4. Run `python scripts/generate_pending_review.py` to confirm 0 pending

Do NOT read the full file — use `offset` parameter.

## What NOT to look up in the tracker

The tracker is append-only and contains no decision content. To understand what an experiment
found, read the manifest JSON in `evidence/experiments/<dir>/`. The tracker only records
"was this discussed" — not what was decided.
