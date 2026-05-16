# Project Insights — 2026-05-16

Generated: 2026-05-16T18:28:10Z

---

## Experiment Health

- **Total runs:** 708 (PASS: 157 | FAIL: 281 | ERROR: 77 | UNKNOWN: 193 | error rate: 10.9% | unknown rate: 27.3%)
- **Experiment queue depth:** 0 items currently queued

### High-iteration experiments (3+ lettered iterations)

68 chains across the full history. Top-10 by iteration count:

| Chain | Iters | Last result | Claims |
|-------|-------|------------|--------|
| V3-EXQ-085 | 14 | FAIL | MECH-071 |
| V3-EXQ-418 | 13 | ERROR | SD-016, SD-017 |
| V3-EXQ-514 | 10 | FAIL | SD-049 |
| V3-EXQ-047 | 9 | PASS | SD-005, MECH-095 |
| V3-EXQ-445 | 9 | UNKNOWN | -- |
| V3-EXQ-433 | 7 | UNKNOWN | SD-029 |
| V3-EXQ-540 | 7 | PASS | MECH-307 |
| V3-EXQ-002 | 6 | FAIL | SD-003 |
| V3-EXQ-020 | 6 | FAIL | MECH-100 |
| V3-EXQ-074 | 6 | PASS | MECH-112, MECH-117 |

### Recurring trouble spots (claim_ids in 2+ ERROR entries)

| Claim | ERROR count | Affected queue IDs |
|-------|------------|-------------------|
| MECH-112 | 4 | V3-EXQ-074, -074d, -225a, -225b |
| MECH-163 | 3 | V3-EXQ-237b, -237c, -495 |
| MECH-113 | 2 | V3-EXQ-075, -075c |
| MECH-116 | 2 | V3-EXQ-076, -076c |
| MECH-188 | 2 | V3-EXQ-253a, -253b |
| SD-003 | 2 | V3-EXQ-008, -071 |
| SD-012 | 2 | V3-EXQ-238a, -238b |
| SD-016 | 2 (+4 substrate failure records) | V3-EXQ-257, -257a |
| SD-018 | 2 | V3-EXQ-257, -257a |
| ARC-007 | 2 | V3-EXQ-046, -046b |
| INV-052 | 2 | V3-EXQ-254a, -254b |

### Claims with many FAILs (5+)

| Claim | FAILs | Status |
|-------|-------|--------|
| SD-003 | 26 | Ongoing -- self-attribution counterfactual pipeline |
| MECH-102 | 8 | Stalled, no active successor |
| MECH-100 | 7 | Stalled, no active successor |
| MECH-099 | 6 | Stalled, no active successor |
| SD-005 | 6 | Partially resolved |
| SD-007 | 6 | Partially resolved |
| SD-016 | 5 | implemented_but_failing_validation |

### Notable null result (2026-05-16)

V3-EXQ-573 (ARC-065 bias-scale 10-arm sweep, 1x/5x/10x scale factors): all 10 arms
bit-for-bit identical, zero differential. Root cause: MECH-313/314/320 biases are literally
zero at cold start -- warm-start gate (DEV-NEED-029) was never established. Documented in
behavioral_diversity_acceptance_criteria.md. Blocks all ARC-065 diversity experiments and
Q-043/044/045 retests until resolved.

---

## Substrate Bottlenecks

- **Total substrate items:** 85 | **Implemented:** 40 (47%)
- **Status breakdown:** implemented=40, unknown/untracked=40, implemented_but_failing_validation=2, substrate_landed_pending_validation=2, parked=1

### Ready SDs (all deps met, not yet fully implemented)

SD-037 (broadcast.override_regulator), MECH-204 (serotonergic withdrawal / REM precision),
MECH-307 (anticipatory affect conjunction -- substrate landed, validation pending),
INF-ENV-001 through INF-ENV-004 (environment infrastructure: harm gradient zones,
microhabitat zones, transient patches, stochastic attractor audit)

### Blocked SDs (25 total, representative sample)

| SD | Blocked on |
|----|-----------|
| SD-019b | MECH-219, Q-036 |
| SD-024 / SD-025 | SD-004 (action-objects hippocampal map) |
| SD-026 / SD-028 | INV-034 (goal maintenance) |
| SD-030 / SD-031 | MECH-256 (self-attribution) |
| SD-032 / SD-033 | MECH-094 (hypothesis tag) |
| SD-027 | MECH-089 (cross-frequency coupling) |

### SDs with most failure records

| Substrate | Failures | Key issue |
|-----------|----------|-----------|
| MECH-256 | 10 | Self-attribution single-pass comparison -- blocks SD-030 and SD-031 |
| SD-016 | 4 | ContextMemory cue-indexed retrieval -- implemented_but_failing_validation |
| MECH-307 | 3 | Anticipatory affect conjunction |
| SD-049 | 3 | Multi-resource heterogeneity |
| MECH-269b | 2 | Symmetric V_s gating on E1 / E2 |

MECH-256 is the highest-failure unresolved substrate (10 failures), blocking the
entire self-attribution pipeline (SD-030, SD-031).

---

## Governance State

- **Total claims:** 633 | **v3_pending claims:** 100 (16%)
- **Total decisions in recommendations table:** 169 (most applied)
- **Pending user decisions:** 13

### 13 pending_user decisions

- MECH-314, MECH-314a, MECH-314b, MECH-314c, MECH-320 -- sleep-related,
  candidate_substrate_landed, hold_pending_v3_substrate
- ARC-066, ARC-067, ARC-068, ARC-070, ARC-071 -- non-deficit-drives /
  policy-granularity clusters, pending_design, v3_pending (registered 2026-05-10)
- Q-043, Q-044, Q-045 -- Q-claims from same cluster, v3_pending

- **Conflict-hold claims (hold_candidate_resolve_conflict):** 28
- **Pending experiment review:** 0 (all cleared 2026-05-16T18:25Z)

---

## Literature Coverage

- **Open lit-needed backlog items:** 1 (Q-019 -- Three-Gate BG Architecture extraction)
- **Targeted review directories:** 44+ under evidence/literature/ covering ARC-007 through
  ARC-071 series, MECH clusters, connectome pulls
- **Recent lit-pulls completed:** ARC-067 (boredom/idle-aversion, 8 entries,
  lit_conf=0.864, 2026-05-10)
- **Pending lit-pulls (flagged in session logs):** ARC-066 (tonic vigor) and ARC-068
  (opportunity cost) explicitly required before child MECH/SD design per
  biology-before-formal-definitions rule; ARC-070 / ARC-071 also expected

Coverage is strong. The single open backlog item (Q-019) is a long-standing low-priority
extraction task.

---

## Human-Intervention Patterns

### Recurring intervention triggers

- **Diagnose-errors sessions** -- appeared in 5+ of the last 30 session entries. Primary
  driver: 193 UNKNOWN results (27.3% of all runs) from cloud runner SIGTERM timeouts and
  the silent-drop bug at experiment_runner.py:1394. Each UNKNOWN batch triggers a
  diagnose-errors session with manual ID resolution.
- **Governance decisions (pending_user)** -- 13 currently awaiting user review. Each new
  claim cluster (non-deficit drives, policy granularity -- both 2026-05-10) generates a
  batch of pending_user decisions requiring user sign-off before the governance table
  finalises.
- **Calibration null results** -- EXQ-573 (bias-scale sweep null), EXQ-569 (entropy flat),
  EXQ-571 (F dominates 88-89%) each required a session to diagnose and document. The
  calibration debt program consistently produces unexpected nulls that need human
  interpretation before the next queuing decision.
- **SD-016 design failures** -- 4 failure records + implemented_but_failing_validation;
  each iteration required human decision on whether to rethink the design or continue
  sweeping parameters.
- **Substrate implementation sign-off** -- all 4 recent substrate implementations
  (SD-047, SD-019a, SD-033b, MECH-307 consumer) required plan-confirmation and
  multi-step contract verification pauses.

### Low-friction headless tasks

- **Lit-pulls** -- ARC-067 completed cleanly in one session (8 entries, no blockers).
  Literature sessions are reliable when the target claim is well-specified.
- **Governance index rebuilds** -- build_experiment_indexes.py + generate_pending_review.py
  run headlessly; 0 pending review is the steady state between sessions.
- **Documentation updates** -- calibration_debt_index.md, sleep_substrate_plan.md, and
  WORKSPACE_STATE.md updates are consistently clean single-pass writes.

---

## Recommendations

1. **Establish warm-start gate first (DEV-NEED-029 / EXQ-ISEF-001).** Per
   developmental_experiment_priorities.md (2026-05-16), EXQ-ISEF-001 (harm gradient
   injection) is Rank 1 and gates all downstream diversity experiments (ARC-065),
   Q-043/044/045 retests, and INV-049 retest. The EXQ-573 null proves that cold-start
   diversity experiments are uninformative -- any further ARC-065 sweep before
   this gate is resolved will produce the same null.

2. **Revisit MECH-256 design (10 failure records).** Self-attribution single-pass
   comparison has failed more times than any other substrate item. It blocks SD-030 and
   SD-031 (both blocked: MECH-256). A fresh architectural approach -- or explicit demotion
   with redesign as a new MECH -- would unblock the self-attribution pipeline more
   reliably than another iteration.

3. **Patch UNKNOWN result silent-drop (27.3% of runs).** The silent-drop bug at
   experiment_runner.py:1394 and Hetzner CX22 undersizing are the diagnosed causes.
   Each UNKNOWN batch triggers a diagnose-errors session. Fixing the silent-drop bug
   or migrating to better cloud hardware would eliminate the most common recurring
   headless intervention.

4. **Review 13 pending_user governance decisions.** The MECH-314 cluster (sleep-related,
   substrate landed) and ARC-066/067/068/070/071 (non-deficit drives + policy granularity,
   registered 2026-05-10) are all waiting. Clearing these closes the governance backlog
   and unblocks child MECH/SD design for the new clusters.

5. **Queue ARC-066 and ARC-068 lit-pulls.** ARC-067 (boredom) is complete. ARC-066
   (tonic vigor) and ARC-068 (opportunity cost) were explicitly flagged as the next
   required pulls at registration. Per the biology-before-formal-definitions rule,
   child MECH/SD design for these slots cannot proceed until all three family lit-pulls
   are done.
