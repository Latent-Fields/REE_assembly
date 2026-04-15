# Morning Agenda -- 2026-04-15

Generated: 2026-04-15T06:30:00Z

---

## Queue Status

- Total pending: **14** (any: 11 | Mac DLAPTOP-4.local: 3 | Daniel-PC: 0 | EWIN-PC: 0)
- **2 stale claimed items** (>6 hours old -- runner may have stopped):
  - V3-EXQ-330a: claimed by DLAPTOP-4.local at 2026-04-14T23:42Z (~6.5h stale)
  - V3-EXQ-328b: claimed by ree-cloud-1 at 2026-04-13T08:26Z (~2 days stale)
- runner_status.json shows `idle=True`, last_updated `2026-04-14T05:48:06Z` -- runner may not be running on any machine. Confirm before queueing work.
- Pending items by machine affinity:
  - **any (11):** EXQ-323a, EXQ-326a, EXQ-321a, EXQ-325a, EXQ-395, EXQ-375, EXQ-406, EXQ-407, EXQ-353, EXQ-418, EXQ-326
  - **DLAPTOP-4.local (3):** EXQ-396a (priority 7), EXQ-396 (priority 5), EXQ-397 (priority 5)
  - **ree-cloud-1 (0 pending):** EXQ-328b stale-claimed
  - **Daniel-PC (0)** | **EWIN-PC (0)**

---

## Experiments Awaiting Review (0 indexed / 0 runner-only)

All experiments reviewed. Nothing pending.

_(pending_review.md generated 2026-04-14T18:02:49Z -- governance.sh re-run was in progress at session open but sync_v3_results.py has not yet completed; last known state is 0 pending)_

---

## Errors to Diagnose (30 unresolved V3 ERRORs)

30 V3 experiments errored with no queued or completed lettered fix detected. Use `/diagnose-errors` for full triage. Summary by recency:

**Most recent cluster (no fixes queued):**
| EXQ ID | Claim(s) | Notes |
|--------|----------|-------|
| V3-EXQ-254b | INV-052 | offline consolidation -- needs /diagnose-errors |
| V3-EXQ-253b | MECH-188 | depressive consolidation via harm residue |
| V3-EXQ-251a | MECH-186 | replay deficit in depressive attractor |
| V3-EXQ-250a | INV-054 | waking forward model prerequisite |
| V3-EXQ-249a | INV-053 | depression attractor -- *EXQ-406 may supersede; confirm* |
| V3-EXQ-248a | Q-034 | harm stream causal independence |
| V3-EXQ-238b | SD-012 | homeostatic drive |
| V3-EXQ-237c | MECH-163 | VTA planned system |
| V3-EXQ-257a | SD-018 | resource proximity supervision |
| V3-EXQ-225b | MECH-112 | structured goal representation |

**Older unresolved cluster (260a/261a/262a, 225a, 237b, 238a, 253a, 254a, 071c, 051b, 074b/c/d, 075b/c, 076b/c, 084b/c):** may be superseded by later lettered runs not caught by ID prefix check. Run /diagnose-errors for prioritisation.

**Special:** V3-ONBOARD-smoke-EWIN-PC -- EWIN machine never onboarded successfully (errored 2026-04-06). No -b smoke queued. EWIN-PC unavailable until fixed.

---

## Governance Agenda -- URGENT (4 mandatory decision checkpoints, deadline 2026-04-17)

All 4 items have decision deadline **2026-04-17T19:01Z** -- 2 days away. Each requires a governance decision: `retain_ree | hybridize | retire_ree_claim`.

- **MECH-230** (candidate) -- mandatory_decision_checkpoint
  - *Claim:* E3 maintains a structured latent goal representation (positive attractor in z_goal sub-space)
  - Evidence: 2 exp, 0 lit | confidence: **0.597** | conflict_ratio: **1.00** (fully contested)
  - EXQ-328b FAIL (full run, 2026-04-14) and EXQ-328a FAIL are the only entries. Very thin evidence base. Decision required before continuing retest loop.

- **ARC-016** (provisional) -- mandatory_decision_checkpoint
  - *Claim:* Precision-to-commit threshold -- modes are control-plane regimes applied to shared predictive machinery
  - Evidence: 29 exp, 5 lit | 34 total | confidence: **0.782** | conflict_ratio: **0.966**
  - EXQ-396a queued (dual-bug fix: rv update in training + no eval reset). Pending retest. Decision required regardless of EXQ-396a result -- conflict ratio is very high.

- **SD-015** (candidate) -- mandatory_decision_checkpoint
  - *Claim:* Goal-directed navigation requires dedicated z_resource encoder (object-type features, location-invariant)
  - Evidence: 24 exp, 6 lit | 30 total | confidence: **0.732** | conflict_ratio: **0.933**
  - EXQ-326a PASS (2026-04-14, correct wiring) supports. EXQ-322a FAIL (z_world beats z_resource 0.99 vs 0.39-0.86). EXQ-326a is most recent.

- **SD-012** (candidate) -- mandatory_decision_checkpoint
  - *Claim:* Homeostatic drive modulation: z_goal seeding demands non-zero drive_level to produce above-threshold benefit_exposure
  - Evidence: 31 exp, 8 lit | 39 total | confidence: **0.728** | conflict_ratio: **0.889**
  - EXQ-328b FAIL (C3 ablation failed, 2026-04-14). Multiple prior FAIL iterations. drive_weight=2.0 default fix is implemented. EXQ-238a/238b both ERROR (no fix queued). Most experiments on this claim are inconclusive or failing.

---

## Literature Pull Candidates (Top 5 of 22)

All 22 items are `medium` priority with no existing targeted review directories:

| # | Claim | Subject | Priority | Existing lit dirs |
|---|-------|---------|----------|------------------|
| 1 | Q-036 | What additional variables beyond temporal integration are required for affective harm encoding? | medium | 0 |
| 2 | SD-019 | Affective harm nonredundancy constraint (C-fiber / A-delta causal independence) | medium | 0 |
| 3 | SD-022 | Directional limb damage / genuine z_harm_s vs z_harm_a causal independence | medium | 0 |
| 4 | ARC-028 | HippocampalModule trajectory completion signal wired to BetaGate | medium | 0 |
| 5 | MECH-057 | Attribution completion gating | medium | 0 |

_SD-019 and SD-022 are highest-relevance given active experimental work (EXQ-323a/325a queued). Q-036 is directly relevant to the SD-012/SD-019 decision cluster._

---

## Serve.py Status

- **RUNNING on port 8000** (pid 48099, started Sun 02AM, running caffeinated)

---

## Blocked Items

1. **governance.sh incomplete at session open**: `sync_v3_results.py` (pid 33285) was scanning ~5240 JSON files via sequential I/O (started 05:20AM, ~CPU 0.35s after 65+ minutes -- slow macOS disk cache warming). governance.sh was started in the background and may complete later. Updated `promotion_demotion_recommendations.md` and `claims.json` will not be available until it finishes.

2. **ree-v3 remote pull failed**: `fatal: bad object refs/heads/main 2` -- corrupt packfile. Fix: `git remote prune origin` then `git fetch` in REE_Working/ree-v3. Local state appears current (HEAD = `9a6d84b` "claim: V3-EXQ-330a -> DLAPTOP-4.local", 2026-04-14).

3. **V3-ONBOARD-smoke-EWIN-PC ERROR**: EWIN-PC (Eoin's machine) never completed onboarding. Original smoke errored 2026-04-06. No -b smoke queued. EWIN-PC cannot claim experiments until resolved.

4. **2 stale claims need clearing**: EXQ-330a (DLAPTOP-4.local) and EXQ-328b (ree-cloud-1). Both runner.json shows idle. If runner is not running, clear claims manually from experiment_queue.json so these experiments can be re-claimed.

---

## Recent Work (2026-04-14)

| Session | Summary |
|---------|---------|
| governance-2026-04-14 | 6 experiments reviewed; MECH-231 promoted candidate->provisional (164x E2/E1 slope ratio); MECH-230 hold_candidate confirmed; 0 pending after rebuild |
| claims-2026-04-14-valence-terrain | MECH-232, MECH-233, ARC-057 registered (hippocampal valence asymmetry) |
| litpull-2026-04-14-valence-terrain | 5 lit entries for ARC-007/SD-004; ARC-007 lit_conf 0.852 |
| sd019-323a-2026-04-14 | V3-EXQ-323a queued: SD-019 nonredundancy on SD-022 substrate (1200 eps, any affinity) |
