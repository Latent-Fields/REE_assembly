# Closure-Plan Drift Report

Generated: 2026-08-18T14:11:21Z

This report flags closure_plan nodes whose `owner_exq` has reached a terminal state (manifest landed and / or failure_autopsy artifact present) but whose `status` is still non-terminal. Nodes that self-tag as Case 3 (legitimately non-terminal pending upstream substrate or successor EXQs) and nodes whose owner_exq manifest is non-contributory / superseded / inconclusive are recorded under Suppressed instead, not Drifted. A separate date-aware section, `Stale since last update`, flags non-terminal nodes (including suppressed ones) where a later-lettered owner_exq sibling reached terminal state or a confirmed failure_autopsy touching the node's `unblocks_claims` post-dates the node's `last_updated` -- the class of staleness that hid goal_pipeline:GAP-2 on 2026-06-03. The report also flags plans missing a top-level `closure_plan.last_updated` field.

Warn-only -- this script never blocks the governance pipeline.

## Drifted nodes (0)

_None._

## Suppressed (legitimately non-terminal) (1)

Nodes whose `owner_exq` reached a terminal state but where suppression rules say the node is legitimately non-terminal (Case-3 self-tag or non-contributory manifest evidence_direction). Listed here for audit; not counted as drift.

| plan | node | status | owner_exq | suppress reason |
|------|------|--------|-----------|-----------------|
| self_attribution_plan.md | `self_attribution:GAP-1` | blocked | V3-EXQ-445h | case_3_self_tag |

## Stale since last update -- review (2)

Non-terminal nodes (including ones Suppressed above) where newer evidence landed that the node frontmatter may not have absorbed: a later-lettered owner_exq sibling reached terminal state (lineage advanced), and / or a confirmed failure_autopsy touching the node's `unblocks_claims` is dated after the node's `last_updated`. Review each: update owner_exq / status / resume_condition and bump `last_updated`, or (if the new evidence genuinely does not change the node) bump `last_updated` to acknowledge it. Not counted as drift.

| plan | node | status | owner_exq | node last_updated | why |
|------|------|--------|-----------|-------------------|-----|
| commitment_closure_plan.md | `commitment_closure:GAP-4` | in-progress | _none_ | 2026-08-16 | failure_autopsy_V3-EXQ-935_2026-08-18.json (2026-08-18) reclassified MECH-266 |
| commitment_closure_plan.md | `commitment_closure:GAP-4-battery` | in_progress | _none_ | 2026-08-16 | failure_autopsy_V3-EXQ-935_2026-08-18.json (2026-08-18) reclassified MECH-266 |

## Assembly frontier -- resting, not drift (10)

Nodes with status `assembling` / `open_by_design`: required for v3 but under construction. They are a stable resting state -- NOT counted as drift or stale, and they need no recurring re-stamp to stay quiet. Listed here for visibility only. A node flagged **revisit_due** has passed its optional `revisit_after` date and should be reviewed (resume / re-state / extend the date).

| plan | node | status | awaiting | assembly_status | revisit_after | revisit_due |
|------|------|--------|----------|-----------------|---------------|-------------|
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-K` | assembling | _unset_ | blocked_on_upstream | _none_ | no |
| commitment_closure_plan.md | `commitment_closure:GAP-8` | assembling | _unset_ | built | _none_ | no |
| conversion_ceiling_campaign_plan.md | `conversion_ceiling_campaign:CAMPAIGN` | assembling | _unset_ | ran_exhausted_for_substrate | _none_ | no |
| conversion_ceiling_campaign_plan.md | `conversion_ceiling_campaign:P-comp` | assembling | _unset_ | ran_non_contributory | _none_ | no |
| conversion_ceiling_campaign_plan.md | `conversion_ceiling_campaign:P2-rootC` | assembling | _unset_ | ran_exhausted_for_substrate | _none_ | no |
| conversion_ceiling_campaign_plan.md | `conversion_ceiling_campaign:P3-ofc` | assembling | _unset_ | built | _none_ | no |
| conversion_ceiling_campaign_plan.md | `conversion_ceiling_campaign:FULLSTACK` | assembling | _unset_ | ran_exhausted_for_substrate | _none_ | no |
| conversion_ceiling_campaign_plan.md | `conversion_ceiling_campaign:P4-learned-gating` | assembling | _unset_ | blocked_on_upstream | _none_ | no |
| conversion_ceiling_campaign_plan.md | `conversion_ceiling_campaign:GENERATION` | assembling | _unset_ | blocked_on_upstream | _none_ | no |
| sd_037_axis_b_sustained_threat_curriculum_plan.md | `sd_037_axis_b:P1b` | assembling | conversion_ceiling_campaign:FULLSTACK -- 625e's confirmed au | in_progress | _none_ | no |

## Status-plane drift -- projected `live` != stored `live` (19 of 99 collapsed node(s))

SHP-2 two-plane nodes carry a stored `live:` head that is a pure projection over the append-only event log. This section re-projects each and flags any whose stored head has gone stale vs the events (a new autopsy / PASS manifest / decision landed, or the reconcile / brake state moved). In a governance cycle it is self-healing: Step 3c-pre-heal (scripts/heal_status_plane_drift.py) re-stamps every fully-collapsed drifted plan IN PLACE before this check runs (leaving the edited plan file uncommitted for a human to review + commit pathspec-limited), so a residual count here is normally a MIXED plan that still has un-collapsed blob nodes -- re-stamp it manually with `scripts/shp2_collapse_and_verify.py --plan <plan>` once collapsed (the collapse step re-projects already-collapsed drifted nodes in place, then re-runs this check as gate 4), or `scripts/shp2_collapse_plan.py --plan <plan>` for the re-stamp without the gates. Both regenerate `live:`+`join:` via the one projection path and are byte-identical no-ops on up-to-date nodes. Nodes with no `live:` block are not yet collapsed and are not checked here.

| plan | node | stored from | projected from | drifted fields |
|------|------|-------------|----------------|----------------|
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-A` | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | needs_review_reasons: stored=['newest_forward_predates_later_manifest_event(s)'] projected=['newest_forward_predates_later_decision+manifest_event(s)'] |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-B` | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | needs_review_reasons: stored=['newest_forward_predates_later_manifest_event(s)'] projected=['newest_forward_predates_later_decision+manifest_event(s)'] |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-C` | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | needs_review_reasons: stored=['newest_forward_predates_later_manifest_event(s)'] projected=['newest_forward_predates_later_decision+manifest_event(s)'] |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-C-build` | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | needs_review_reasons: stored=['newest_forward_predates_later_manifest_event(s)'] projected=['newest_forward_predates_later_decision+manifest_event(s)'] |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-D` | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | needs_review_reasons: stored=['newest_forward_predates_later_manifest_event(s)'] projected=['newest_forward_predates_later_decision+manifest_event(s)'] |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-E` | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | needs_review_reasons: stored=['newest_forward_predates_later_manifest_event(s)'] projected=['newest_forward_predates_later_decision+manifest_event(s)'] |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-F` | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | needs_review_reasons: stored=['newest_forward_predates_later_manifest_event(s)'] projected=['newest_forward_predates_later_decision+manifest_event(s)'] |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-G` | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | needs_review_reasons: stored=['newest_forward_predates_later_manifest_event(s)'] projected=['newest_forward_predates_later_decision+manifest_event(s)'] |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-H` | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | needs_review_reasons: stored=['newest_forward_predates_later_manifest_event(s)'] projected=['newest_forward_predates_later_decision+manifest_event(s)'] |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-I` | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | needs_review_reasons: stored=['newest_forward_predates_later_manifest_event(s)'] projected=['newest_forward_predates_later_decision+manifest_event(s)'] |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-J` | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | needs_review_reasons: stored=['newest_forward_predates_later_manifest_event(s)'] projected=['newest_forward_predates_later_decision+manifest_event(s)'] |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-K` | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16#V3-EXQ-436f | needs_review_reasons: stored=['newest_forward_predates_later_manifest_event(s)'] projected=['newest_forward_predates_later_decision+manifest_event(s)'] |
| conversion_ceiling_campaign_plan.md | `conversion_ceiling_campaign:CAMPAIGN` | failure_autopsy_V3-EXQ-937-937a-cluster_2026-08-18#V3-EXQ-937a | failure_autopsy_V3-EXQ-937-937a-cluster_2026-08-18#V3-EXQ-937a | needs_review: stored=False projected=True; needs_review_reasons: stored=[] projected=['newest_forward_predates_later_decision_event(s)'] |
| conversion_ceiling_campaign_plan.md | `conversion_ceiling_campaign:P-comp` | failure_autopsy_V3-EXQ-937-937a-cluster_2026-08-18#V3-EXQ-937a | failure_autopsy_V3-EXQ-937-937a-cluster_2026-08-18#V3-EXQ-937a | needs_review: stored=False projected=True; needs_review_reasons: stored=[] projected=['newest_forward_predates_later_decision_event(s)'] |
| conversion_ceiling_campaign_plan.md | `conversion_ceiling_campaign:P2-rootC` | failure_autopsy_V3-EXQ-937-937a-cluster_2026-08-18#V3-EXQ-937a | failure_autopsy_V3-EXQ-937-937a-cluster_2026-08-18#V3-EXQ-937a | needs_review: stored=False projected=True; needs_review_reasons: stored=[] projected=['newest_forward_predates_later_decision_event(s)'] |
| conversion_ceiling_campaign_plan.md | `conversion_ceiling_campaign:P3-ofc` | failure_autopsy_V3-EXQ-937-937a-cluster_2026-08-18#V3-EXQ-937a | failure_autopsy_V3-EXQ-937-937a-cluster_2026-08-18#V3-EXQ-937a | needs_review: stored=False projected=True; needs_review_reasons: stored=[] projected=['newest_forward_predates_later_decision_event(s)'] |
| conversion_ceiling_campaign_plan.md | `conversion_ceiling_campaign:FULLSTACK` | failure_autopsy_V3-EXQ-937-937a-cluster_2026-08-18#V3-EXQ-937a | failure_autopsy_V3-EXQ-937-937a-cluster_2026-08-18#V3-EXQ-937a | needs_review: stored=False projected=True; needs_review_reasons: stored=[] projected=['newest_forward_predates_later_decision_event(s)'] |
| conversion_ceiling_campaign_plan.md | `conversion_ceiling_campaign:P4-learned-gating` | failure_autopsy_V3-EXQ-937-937a-cluster_2026-08-18#V3-EXQ-937a | failure_autopsy_V3-EXQ-937-937a-cluster_2026-08-18#V3-EXQ-937a | needs_review: stored=False projected=True; needs_review_reasons: stored=[] projected=['newest_forward_predates_later_decision_event(s)'] |
| conversion_ceiling_campaign_plan.md | `conversion_ceiling_campaign:GENERATION` | failure_autopsy_V3-EXQ-937-937a-cluster_2026-08-18#V3-EXQ-937a | failure_autopsy_V3-EXQ-937-937a-cluster_2026-08-18#V3-EXQ-937a | needs_review: stored=False projected=True; needs_review_reasons: stored=[] projected=['newest_forward_predates_later_decision_event(s)'] |

## Plans missing `closure_plan.last_updated` (0)

_None._

