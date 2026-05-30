# IGW Auto-Spawn Routine Log

One line per hourly tick. ASCII only.

2026-05-25T16:25:10Z skip IGW-20260525-037: no fresh runner heartbeat (experiment-lane item would just sit in queue)
2026-05-25T16:33:03Z disposition IGW-20260525-021 hash=1233895f3a19 decision=DEFER: V3-EXQ-455a planning-stub; substrate moved past gating reasoning; subsumed by be
2026-05-25T16:33:04Z disposition IGW-20260525-022 hash=1df196a0d68b decision=RESOLVE: V3-EXQ-544 manifest PASS underneath phantom ERROR (sentinel-protocol-race 2026-0
2026-05-27T05:55:42Z no eligible item (skipped 34): IGW-20260527-001:skill /governance not allowed; IGW-20260527-026:user-dispositioned (hash bfbc5eb3356f); IGW-20260527-027:collides with active TASK_CLAIMS resources: REE_assembly/docs/claims/claims.yaml
2026-05-27T06:11:46Z disposition IGW-20260527-001 hash=085c3522a523 decision=RESOLVE: 2 indexed pending in pending_review.md are intentionally held for /failure-autop
2026-05-29T06:13:17Z disposition IGW-20260529-037 hash=2b4c3b827f61 decision=BLOCKED_SUBSTRATE: ARC-046 retest gate (claims.yaml 13379-13412) has 2/3 substrate prerequisites unmet -- (b) goal-pipeline/training-regime enrichment (V3-EXQ-603c FAILED 2026-05-27, routed to /implement-substrate) and (c) InfantCurriculumScheduler Phase 0->1 exit-gate retune (routed to /implement-substrate). V3-EXQ-591 marked reviewed. Stale 2026-05-27 IGW-027 TASK_CLAIMS entry (same auto-spawn, ~36h) cleared.
2026-05-29T06:46:33Z no eligible item (skipped 52): IGW-20260529-001:skill /governance not allowed; IGW-20260529-037:skill /implement-substrate not allowed; IGW-20260529-039:skill /implement-substrate not allowed
2026-05-30T01:04:35Z SPAWN IGW-20260530-038 skill=/queue-experiment prio=28 uuid=987e19f6-61dc-49b4-b060-33c61f847d30 pid=75047 worktree=igw-038-retest-after-substrate-inv-074
2026-05-30T02:05:29Z SPAWN IGW-20260530-038 skill=/queue-experiment prio=28 uuid=b43b219b-ffb1-4331-b246-2a92bc2c0c2c pid=88233 worktree=igw-038-retest-after-substrate-inv-074
2026-05-30T03:06:25Z SPAWN IGW-20260530-038 skill=/queue-experiment prio=28 uuid=70015fee-5107-4701-94ee-5c57b2d1efc0 pid=98657 worktree=igw-038-retest-after-substrate-inv-074
2026-05-30T04:07:19Z SPAWN IGW-20260530-038 skill=/queue-experiment prio=28 uuid=550f31f3-f4d6-429b-9eda-178d29d486eb pid=11519 worktree=igw-038-retest-after-substrate-inv-074
2026-05-30T05:08:15Z skip IGW-20260530-038: no fresh runner heartbeat (experiment-lane item would just sit in queue)
2026-05-30T06:08:16Z skip IGW-20260530-038: no fresh runner heartbeat (experiment-lane item would just sit in queue)
2026-05-30T07:08:18Z skip IGW-20260530-038: no fresh runner heartbeat (experiment-lane item would just sit in queue)
2026-05-30T08:08:15Z skip IGW-20260530-036: no fresh runner heartbeat (experiment-lane item would just sit in queue)
2026-05-30T09:08:17Z skip IGW-20260530-036: no fresh runner heartbeat (experiment-lane item would just sit in queue)
2026-05-30T10:08:19Z skip IGW-20260530-036: no fresh runner heartbeat (experiment-lane item would just sit in queue)
2026-05-30T11:08:22Z skip IGW-20260530-036: no fresh runner heartbeat (experiment-lane item would just sit in queue)
2026-05-30T13:09:17Z SPAWN IGW-20260530-020 skill=/implement-substrate prio=25 uuid=2de39d78-e892-4436-8cac-ac0878564e41 pid=54011 worktree=igw-020-substrate-ready-mech-302
2026-05-30T14:10:25Z SPAWN IGW-20260530-020 skill=/implement-substrate prio=25 uuid=a250152c-8460-4bb0-9fad-7aef7eba9086 pid=66489 worktree=igw-020-substrate-ready-mech-302
2026-05-30T15:11:28Z SPAWN IGW-20260530-020 skill=/implement-substrate prio=25 uuid=43badd82-f4ab-4b0c-9d8f-b662768e79c2 pid=77868 worktree=igw-020-substrate-ready-mech-302
2026-05-30T16:12:34Z SPAWN IGW-20260530-020 skill=/implement-substrate prio=25 uuid=4cd18dc0-327b-4166-8b8a-fd5bf1812f65 pid=89606 worktree=igw-020-substrate-ready-mech-302
2026-05-30T17:13:38Z SPAWN IGW-20260530-021 skill=/implement-substrate prio=25 uuid=058289f8-5e78-4bc6-94ef-3e152b3d9837 pid=5503 worktree=igw-021-substrate-ready-mech-302
2026-05-30T18:14:37Z SPAWN IGW-20260530-023 skill=/implement-substrate prio=25 uuid=2437b3fa-b445-4459-888f-8b4e51745271 pid=28901 worktree=igw-023-substrate-ready-mech-302
2026-05-30T18:19:01Z disposition IGW-20260530-023 hash=994434ce5e5b decision=NO-OP: MECH-302 and MECH-303 already have substrate implementations (SD-050 SufferingDerivativeComparator and SD-052 contextual passive safety) with v3_pending=false and V3-EXQ-517c PASS evidence. Skill /implement-substrate does not exist and is not needed. This IGW item has been spawning hourly since IGW-20260530-020 (13:09Z) due to incorrect workset generation flagging implemented claims as needing substrate work. Recommend investigating workset generation logic to prevent future spurious substrate-lane assignments for claims with existing substrate + v3_pending=false.
