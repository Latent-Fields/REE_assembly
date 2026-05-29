# IGW Auto-Spawn Routine Log

One line per hourly tick. ASCII only.

2026-05-25T16:25:10Z skip IGW-20260525-037: no fresh runner heartbeat (experiment-lane item would just sit in queue)
2026-05-25T16:33:03Z disposition IGW-20260525-021 hash=1233895f3a19 decision=DEFER: V3-EXQ-455a planning-stub; substrate moved past gating reasoning; subsumed by be
2026-05-25T16:33:04Z disposition IGW-20260525-022 hash=1df196a0d68b decision=RESOLVE: V3-EXQ-544 manifest PASS underneath phantom ERROR (sentinel-protocol-race 2026-0
2026-05-27T05:55:42Z no eligible item (skipped 34): IGW-20260527-001:skill /governance not allowed; IGW-20260527-026:user-dispositioned (hash bfbc5eb3356f); IGW-20260527-027:collides with active TASK_CLAIMS resources: REE_assembly/docs/claims/claims.yaml
2026-05-27T06:11:46Z disposition IGW-20260527-001 hash=085c3522a523 decision=RESOLVE: 2 indexed pending in pending_review.md are intentionally held for /failure-autop
2026-05-29T06:13:17Z disposition IGW-20260529-037 hash=2b4c3b827f61 decision=BLOCKED_SUBSTRATE: ARC-046 retest gate (claims.yaml 13379-13412) has 2/3 substrate prerequisites unmet -- (b) goal-pipeline/training-regime enrichment (V3-EXQ-603c FAILED 2026-05-27, routed to /implement-substrate) and (c) InfantCurriculumScheduler Phase 0->1 exit-gate retune (routed to /implement-substrate). V3-EXQ-591 marked reviewed. Stale 2026-05-27 IGW-027 TASK_CLAIMS entry (same auto-spawn, ~36h) cleared.
2026-05-29T06:46:33Z no eligible item (skipped 52): IGW-20260529-001:skill /governance not allowed; IGW-20260529-037:skill /implement-substrate not allowed; IGW-20260529-039:skill /implement-substrate not allowed
