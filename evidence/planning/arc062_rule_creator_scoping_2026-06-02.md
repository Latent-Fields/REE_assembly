# ARC-062 "Rule-Creator Substrate" Scoping — 2026-06-02

Session: insights-arc062-scoping-20260602T164144Z
Generated UTC: 2026-06-02T16:41:44Z
Trigger: 2026-06-02 `/insights` pass flagged ARC-062 as the project's single genuine
hard substrate ceiling (9 failure records, drives the EXQ-543 chain) and recommended
scoping a new "rule-creator/discriminator substrate."

## TL;DR (verdict)

**ARC-062 does NOT need a new substrate designed.** The "rule-creator/discriminator
substrate" language that fed the insights recommendation comes from the older
543l (2026-05-27) / 598b failure-record framing. That framing was **superseded by the
user-confirmed V3-EXQ-598 autopsy (2026-05-29)**, which re-read the entire EXQ-543/598
failure cluster as one structural property — *behavioral-diversity collapse* — owned by a
**foundational upstream substrate that already exists: ARC-065** (behavioral-diversity-
generation slot), with its key enabler **SD-056** (E2 action-conditional divergence
preservation) **landing and passing its falsifier two days ago** (V3-EXQ-569d + 617,
2026-05-31).

ARC-062's remaining work is therefore a **sequence of experiments downstream of the
diversity cluster** (`/queue-experiment`), not a new substrate design (`/implement-substrate`).

## 1. Why ARC-062 looked like a hard ceiling

- `substrate_queue` ARC-062 status `phase_1_implemented_evidence_gated_543k_598`, 9 failure
  records, `unblocks_claims: [MECH-309, SD-033a, MECH-262, SD-029]`.
- Failure pattern (consistent across 543/543b…543l): *"outcome-coupled REINFORCE on
  shared-return gated heads collapses to inert monomodal equilibrium regardless of
  structural pressure"* — `use_differential_heads`, `crystallize_at_phase3`, escalated
  floor+aux each **necessary AND none sufficient**.
- The 543l (2026-05-27) and 598b failure records described the exposed gap as *"a
  rule-creator/discriminator that would populate DIFFERENTIATED rule_state inputs to
  SD-033a (not just trainable bias heads)."* **This is the phrase the insights report
  inherited.**

## 2. The reframing (598 autopsy, 2026-05-29, user-confirmed)

`evidence/planning/failure_autopsy_V3-EXQ-598_2026-05-29.md` reclassified the cluster:

- C1 (frozen-silent) + C2 (trainable-nonzero) **PASS** — the SD-033a / gated-policy
  substrate *operates as specified*. Only C3 (behavioral reef-visit band) FAILs.
- C3 is a **downstream-integration metric**, not a clean substrate probe: it requires the
  policy to actually generate per-candidate first-action diversity and inhabit reef-side
  states. Under monomodal collapse it pins to ~0 regardless of any rule-bias machinery.
- Verdict (§5): **"one structural property across 6+ structurally-different claims"**
  (ARC-046, MECH-307, Q-045, MECH-314, SD-033a, + 490g cohort) — the *substrate-uniform
  family*. The competing "each experiment picked a bad metric" reading is explicitly
  rejected as implausible at that breadth.
- Root cause (from the 571 root-cause analysis, embedded in ARC-065's failure record):
  **E2 world-forward compresses K diverse first-action candidates to an identical
  first-step z_world** (`cand_world_pairwise_dist=0.0000` across K=32). Bias channels are
  correctly wired but have nothing differentiated to act on.

Three fix options were named: (i) extend the GAP-B first-action one-hot bypass to all
bias-channel consumers; (ii) **fix the E2 world-forward predictor to preserve per-action
z_world divergence**; (iii) source per-candidate novelty from non-z_world signals.

## 3. What has LANDED since the 598 autopsy

| Substrate | Role | Status (origin/master 2026-06-02) | Evidence |
|---|---|---|---|
| **SD-056** | E2 action-conditional divergence preservation (= fix option **ii**) | `implemented` | **V3-EXQ-569d PASS** (`sd056_action_contrastive_diversity_falsifier`, c1_pass=true, 2/3 seeds clear floor across 3 arms) + **V3-EXQ-617 PASS** (2026-05-31) |
| **ARC-065** | Behavioral-diversity-generation architectural slot — *"Foundational upstream cluster of ARC-062 (top-down rule selection presupposes diversity to choose between)"* | `phase_1_implemented`, `ready:false` | gated on Q-043/Q-044/Q-045 ablations |
| **MECH-341** | E3 score-diversity preservation retune | `amend_implemented_pending_validation`, `ready:true` | retest V3-EXQ-614d queued (prio 250) |

The `arc_062_rule_apprehension_plan.md` dependency table states this directly:
`ARC-065 (foundational, depends_on []) -> ARC-062 (top-down rule selection)`, and
*"arc_062 GAP-B … is already in the V3-EXQ-543b pickup … GAP-C/GAP-D are downstream of
GAP-B PASS."*

## 4. The real dependency chain

```
ARC-065  (behavioral diversity)            <- foundational, depends_on []
  └─ enabled by SD-056 (E2 action-divergence)  ✅ landed + falsifier PASS (569d/617)
  └─ gated on Q-043 (weight calib) / Q-044 (3-arm) / Q-045 (4-arm) ablations
        ↓
ARC-062  GAP-B  (mode-conditioned policy breaks monomodal collapse)
  └─ owner falsifier = 543-series successor, re-run on SD-056/ARC-065 substrate
        ↓
ARC-062  GAP-C / GAP-D  (Phase-3 wiring: LateralPFCAnalog.update() source vector +
                          bias-head params into E3 optimiser)
        ↓
unblocks MECH-309, SD-033a (598c successor w/ redesigned metric), MECH-262, SD-029
```

## 5. Remaining gates (in dependency order)

1. **ARC-065 ablations — IN FLIGHT.** Q-045 4-arm = **V3-EXQ-603e** (queued, prio 250);
   MECH-341 retune = **V3-EXQ-614d** (queued, prio 250). Q-043/Q-044 calibration to confirm.
   These are experiments, already in the live queue.
2. **ARC-062 GAP-B re-falsifier — NOT YET QUEUED.** Once ARC-065 produces non-degenerate
   per-candidate first-action diversity (SD-056 569d PASS is the readiness signal), re-run
   the 543-series GAP-B monomodal-collapse falsifier on the SD-056/ARC-065 substrate. This
   is the load-bearing next ARC-062 experiment. Author via `/queue-experiment`.
3. **ARC-062 GAP-C/GAP-D Phase-3 wiring — downstream of GAP-B PASS.** Already partly
   implemented (Phase-1 module `ree_core/policy/gated_policy.py` + SD-033a routing landed
   2026-05-17). The remaining wiring is small and is `/implement-substrate` *only after*
   GAP-B contributory PASS confirms the diversity substrate breaks collapse.
4. **SD-033a successor (598c)** needs a **redesigned metric** (598 autopsy Learning #2):
   direct `rule_state` cosine probes on held-out rule-context pairs, not the reef-visit-band
   integration metric. Independent of the substrate work.

## 6. What is NOT needed

- **No new "rule-creator/discriminator substrate."** That gap is the behavioral-diversity
  problem, already owned by ARC-065 + SD-056. Designing a separate rule-creator substrate
  now would duplicate ARC-065 and re-introduce the same monomodal blocker one layer up.
- **No `/implement-substrate` for ARC-062 right now.** The next action is experimental
  (GAP-B re-falsifier), gated on the ARC-065 ablations already in queue.

## 7. Recommended next action

**Sequence, no new substrate design:**

1. Let the queued ARC-065 ablations run (V3-EXQ-603e, 614d) → confirm ARC-065 produces
   non-degenerate behavioral diversity in default config.
2. On that PASS, author the **ARC-062 GAP-B re-falsifier** (543-series successor) via
   `/queue-experiment`, on the SD-056/ARC-065 diversity-preserving substrate, with the
   `dacc_weight>0` + non-degeneracy pre-flight assertion the 543e autopsy required.
3. Only after GAP-B contributory PASS: small `/implement-substrate` pass for GAP-C/GAP-D
   Phase-3 wiring + the SD-033a 598c metric redesign.

## 8. The one genuine open decision for the user

ARC-065's gate is three ablations (Q-043 weight calibration, Q-044 three-arm, Q-045
four-arm). **Q-045 (603e) and the MECH-341 retune (614d) are queued; Q-043/Q-044 are not
clearly in the live queue.** Decision: confirm whether Q-043/Q-044 still need authoring, or
whether 603e/614d subsume them — that determines whether ARC-065 can clear on the current
queue or needs one more `/queue-experiment` pass before the ARC-062 GAP-B re-falsifier
becomes meaningful.

## References

- `evidence/planning/failure_autopsy_V3-EXQ-598_2026-05-29.md` (the reframing)
- `evidence/planning/failure_autopsy_V3-EXQ-543l_2026-05-27.md` (older "rule-creator" framing)
- `evidence/planning/arc_062_rule_apprehension_plan.md` (GAP-A/B/C/D plan + ARC-065 sibling note)
- `evidence/planning/v3_exq_571_root_cause_2026-05-25.md` (E2 per-candidate z_world collapse root cause)
- `evidence/experiments/v3_exq_569d_sd056_action_contrastive_diversity_falsifier_floor_recal_20260531T053648Z_v3.json` (SD-056 falsifier PASS)
- substrate_queue entries: ARC-062, ARC-065, SD-056, MECH-341
