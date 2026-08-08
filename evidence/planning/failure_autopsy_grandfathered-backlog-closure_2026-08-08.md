# Grandfathered-backlog closure: the final 7, and a tooling gap

**Generated:** 2026-08-08T20:30:37Z
**Scope:** closure note (round 7 of the 2026-08-08 `/failure-autopsy` grandfathered-backlog sweep)
**Status:** confirmed — zero new diagnosis; this is a verification-only round

## Finding

Of the original 547 grandfathered run_ids (`REE_assembly/evidence/experiments/fail_autopsy_grandfather.json`), all 547 are now accounted for. The 7 that `pending_review.md` still lists as "outstanding" are **not un-adjudicated** — every one was already correctly identified as a `--dry-run` smoke or degenerate-config invocation and recorded in `excluded_dry_run_ids` by a prior round's confirmed artifact:

| run_id | Already excluded in |
|---|---|
| `v3_exq_138a_arc030_go_nogo_pair_20260403T043647Z_v3` | `failure_autopsy_grandfathered-sd029-arc030-cluster_2026-08-08.json` (degenerate manual sanity invocation, warmup=2/eval=1) |
| `v3_exq_238_20260404T185519Z_v3` | `failure_autopsy_grandfathered-wanting-liking-cluster_2026-08-08.json` (`experiment_purpose: "smoke_test"`, self-declared "Not a real experiment run") |
| `v3_exq_328_mech112_zgoal_structured_latent_dry_20260410T155804Z_v3` | `failure_autopsy_grandfathered-sd003-mech112-dacc-cluster_2026-08-08.json`, `failure_autopsy_grandfathered-wanting-liking-cluster_2026-08-08.json` |
| `v3_exq_328a_mech112_zgoal_structured_latent_dry_20260412T102503Z_v3` | `failure_autopsy_grandfathered-wanting-liking-cluster_2026-08-08.json` |
| `v3_exq_328a_mech112_zgoal_structured_latent_dry_20260412T111655Z_v3` | `failure_autopsy_grandfathered-wanting-liking-cluster_2026-08-08.json` |
| `v3_exq_330a_sd013_contrastive_counterfactual_frac05_dry_20260412T102042Z_v3` | `failure_autopsy_grandfathered-arc024-arc033-sd005-cluster_2026-08-08.json` |
| `v3_exq_331_arc030_approach_avoidance_balance_dry_20260410T160253Z_v3` | `failure_autopsy_grandfathered-sd029-arc030-cluster_2026-08-08.json`, `failure_autopsy_grandfathered-doingmode-arc032-arc038-cluster_2026-08-08.json` |

Verified by direct grep against every `failure_autopsy_*.json` in the corpus — all 7 strings match verbatim (no citation-truncation defect this time, unlike round 6's finding).

## Root cause: a tooling gap, not a citation error

`REE_assembly/scripts/generate_pending_review.py`'s `load_confirmed_autopsy_run_ids()` builds its "covered" set by reading only `targets[].run_id` from confirmed artifacts. It never reads `excluded_dry_run_ids`. Separately, `load_dry_run_run_ids()` builds a dry-run exclusion set by reading each manifest's own `dry_run: true` flag directly off disk — which the `/failure-autopsy` skill itself documents as frequently **absent** on pre-2026-07 manifests (exactly why the skill requires manual content verification in the first place, per its own Step 2a).

The result: a run whose `dry_run` flag was never set on the manifest, and which is correctly excluded via `excluded_dry_run_ids` in a confirmed artifact, has **no path to ever clearing the blind-spot net** — the manifest-flag check misses it (flag absent), and the artifact-citation check misses it (field never read). A future session repeatedly re-discovering "these 7 are outstanding," re-confirming they're dry, and re-recording the same `excluded_dry_run_ids` entries would loop forever without this script consulting that field.

This is the same failure shape round 6 found (a correct diagnosis invisible to the automated coverage check) but a **different root cause** — round 6 was citation-string truncation inside `targets[].run_id`; this is a field the checker never reads at all. Chipped separately (`chip-20260808-autopsy-dryrun-coverage-gap`) rather than fixed inline here, since editing `generate_pending_review.py` is outside `/failure-autopsy`'s own scope (analysis + handoff only) and deserves its own review.

## Bottom line

**The 547-run grandfathered backlog is functionally closed as of this round.** Zero run_ids remain without either a confirmed `targets[].run_id` diagnosis or a confirmed `excluded_dry_run_ids` dry-run determination. `pending_review.md` will keep reporting "7 outstanding" until the tooling-gap chip lands; that number does not reflect any remaining scientific work.

## Learning extracted

1. A write-only field (`excluded_dry_run_ids`, populated faithfully by every round of this sweep per the skill's own Step 2a instructions) that nothing downstream reads is functionally equivalent to not recording the finding at all, from the perspective of any tool that only trusts the read path. Worth a standing check whenever a skill instructs writing a field: confirm at least one consumer actually reads it.
2. This closes a 6-round, 547-run backlog sweep (2026-08-08, session `failure-autopsy-9e8737`) started fresh and finished the same day. Total formal targets written across rounds 1-7: on the order of several hundred, spanning every claim family with historical grandfathered evidence.
