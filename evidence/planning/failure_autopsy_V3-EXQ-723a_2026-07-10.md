# Failure Autopsy — V3-EXQ-723a (SD-064 J-lens discriminative-compactness; `no_compact_workspace_diffuse`)

- **Generated (UTC):** 2026-07-10T06:30:52Z
- **Target run_id:** `v3_exq_723a_jlens_discriminative_compactness_diagnostic_20260710T032445Z_v3`
- **Queue id:** V3-EXQ-723a · **supersedes:** V3-EXQ-723 · **machine:** ree-cloud-2
- **experiment_purpose:** diagnostic · **claim_ids:** [] (SD-064 global-workspace + MECH-191 signal-legibility referenced for CONTEXT only; EXCLUDED from governance scoring)
- **Outcome:** FAIL · **evidence_direction:** non_contributory · **self-route label:** `no_compact_workspace_diffuse`
- **Indexer adjudication:** VERIFIED / non-degenerate (all `criteria_non_degenerate` True; `readiness_met=True`)
- **Scope:** single (but the load-bearing signal is the **719a→724→732→723a convergent competence-floor cluster**)
- **Status:** confirmed (user-gated 2026-07-10)
- **Design ref:** `evidence/planning/global_workspace_jlens_plan.md` §2 (Experiment A), §5 status ledger
- **Cross-refs:** `failure_autopsy_V3-EXQ-723_2026-07-09` (predecessor measurement-gap autopsy); `failure_autopsy_V3-EXQ-719a_2026-07-08` (first competence measurement); `failure_autopsy_V3-EXQ-724_2026-07-09` (competence-localization); V3-EXQ-732 `H2_observation_interface_unlearnable` (walked in /governance 2026-07-10; separate autopsy chip pending); GATE-B AMEND (session frosty-thompson-d8f490, competence-localization dependency)

---

## 1. Verdict in one line

The diffuse read is a **CONFOUND / ARTIFACT of the V3 competence floor, not a genuine no-workspace
negative.** 723a's *measurement* is now sound (it fixed 723's non-discriminative gates), but it reads the
**same competence-limited all-ON substrate** that 719a/724/732 have shown forages ~0 because the
**observation interface is unlearnable** (732 = `H2`). A near-monostrategy, weakly-above-null-decodable policy
and a genuinely-diffuse (pluralist) workspace are **indistinguishable from this readout**. Adjudication:
**non_contributory** — PROMOTES / DEMOTES / WEIGHTS NOTHING; the compact-vs-diffuse question is **UNRESOLVED**;
SD-064 stays candidate / v3_pending, **UNWEAKENED** (this is NOT evidence for the pluralist reading). Dominant
diagnosis layer: **developmental / dependency prerequisites (missing)** → `epistemic_category: substrate_ceiling`
(V3 competence floor).

---

## 2. Facts (no interpretation)

**What the script measured.** Post-hoc, over an existing all-ON rollout (V3-EXQ-714 ARM_ON config, identical
to 719a/723; `use_candidate_rule_field=True`), a class-BALANCED weighted ridge readout
`z_t -> committed_class_{t+H}` at `H ∈ {1,3,5}` (PRIMARY_H=3), with DISCRIMINATIVE compactness =
a concentration curve (fraction of latent dims, top-influence-first, to recover 90% of above-chance balanced
accuracy) **vs the same curve under random dim orderings** (`concentration_ratio = frac_top / frac_random`;
LOAD-BEARING), plus a matched-rank random-subspace activity contrast, and GATED reactive-bypass (H1-vs-H5) +
broadcast-alignment contrasts.

**The 723→723a redesign (all three fixes landed).** FIX 1 discriminative compactness via matched-null
baselines (kills 723's trivially-passable `jspace_activity_fraction<0.10` and `retention>=0.80`);
FIX 2 gate (not merely report) the reactive-bypass + broadcast-alignment contrasts; FIX 3
committed-action-balanced eval over EFFECTIVE classes (≥25 train / ≥8 test), require ≥3 effective classes
(guards 723's seed-43 near-binary degeneracy), longer P2 (9000 ticks). Same substrate as 723; **no new
mechanism.**

**Readiness — all MET (recomputed from manifest preconditions):** P2 ticks (min 7603 ≥ 4500); train-pairs
(min 4062 ≥ 1500); ≥3 effective classes (3 seeds); above-null signal with margin (3 seeds); non-degenerate
random-ordering control (min `frac_dims_90_random` 0.836 ≥ 0.25); estimable-majority (3 seeds). So the readout
is estimable and the negative control is non-degenerate → a compact/diffuse branch is *licensed* (this is NOT a
`substrate_not_ready_requeue`).

**Aggregate DVs:**

| DV | Value | Read |
|---|---|---|
| `primary_bal_acc_full_mean` | 0.466 | weak — vs `primary_null_p95_mean` 0.289 |
| `primary_frac_dims_90_top_mean` | 0.762 | top-influence dims need ~76% of dims |
| `primary_frac_dims_90_random_mean` | 0.944 | random ordering needs ~94% — control is non-degenerate |
| `primary_concentration_ratio_mean` | **0.795** | > 0.5 ceiling → **NOT discriminative → diffuse** |
| `mean_resources_per_episode_mean` | **0.158** | **<< 1.0 competence floor** (the confound, measured) |

**Per-seed (foraging competence + concentration):**

| seed | ready | n_eff_classes (H3) | res/ep | bal_acc_full | null_p95 | concentration_ratio | reactive_bypass |
|---|---|---|---|---|---|---|---|
| 42 | yes | 5 | 0.124 | 0.418 | 0.222 | 1.00 | no (gap 0.0) |
| 43 | **no** | **2** | **0.000** | — | — | — | n/a |
| 44 | yes | 3 | 0.477 | 0.615 | 0.356 | 0.798 | no (gap 0.0) |
| 45 | yes | 4 | 0.030 | 0.366 | 0.290 | 0.587 | **yes (gap 0.205)** |

**Which criterion failed:** the LOAD-BEARING **discrimination** criterion
`concentration_discriminative_majority` (0/3 ready seeds passed; needs `ratio < 0.5` AND `frac_top < 0.15`).
`matched_rank_activity_discriminative_majority` passed (non-load-bearing corroboration).
`reactive_bypass` and `broadcast_reportability` did not pass (1/3 and 0/3 assessable respectively;
non-load-bearing). Branch selected: `diffuse_branch=True`, `compact_core_branch=False`.

---

## 3. The self-route is a hypothesis — adjudicated CONFOUNDED

The manifest self-routes `no_compact_workspace_diffuse` and pre-registers its own reading as
"evidence toward the SD-027-original pluralist / no-single-workspace reading … route to /failure-autopsy."
**That inference is BLOCKED here**, for a reason the readiness gates cannot catch:

- The readiness preconditions guarantee the *readout is estimable* (enough ticks, pairs, classes, above-null
  signal, non-degenerate control). They say **nothing about whether the agent is behaviourally competent.**
- 723a forages **0.158 res/ep aggregate** (0.124 / 0.0 / 0.477 / 0.030), below the 1.0 competence floor on
  every seed — the **same** competence-limited substrate 719a first measured (0.065/0.0/0.455) and 724/732
  localized. Seed 43 is a monostrategy seed (2 effective classes, 0.0 res/ep) that fails readiness outright.
- The action-predictive signal the concentration statistic operates on is itself **weak** (`bal_acc_full`
  0.47 vs null 0.29). "Top-influence dims need about as many dims as a random ordering" (`ratio ≈ 0.8`) is the
  *expected* geometry when there is little concentrated action-predictive structure to find — which is exactly
  what an incompetent, near-monostrategy policy produces, **whether or not** a compact workspace would exist on
  a competent agent.

So the two readings — **(a)** genuinely diffuse / pluralist workspace, and **(b)** competence-limited policy
with little action-predictive structure to concentrate — are **confounded from this readout**. This is
precisely the confound the plan's GATE-B `decision_live` note pre-registered on 2026-07-09 ("a compact J-space
and a near-monostrategy policy are indistinguishable from that readout"), now **measured rather than
hypothesized** (732 resolved the competence root to `H2_observation_interface_unlearnable`).

**Contrast with 723.** The 723 autopsy diagnosed a **measurement gap** (non-discriminative gates). 723a FIXED
that (`criteria_non_degenerate` all True; the concentration control is genuinely non-degenerate at
`frac_dims_90_random ≈ 0.94`). The diagnosis has therefore **moved down one layer** — from *measurement*
(723) to *prerequisite / substrate competence* (723a). Having removed the measurement artifact, the confounder
that remains is the competence floor. That progression is clean and non-circular; it is **not** another
letter circling the same measurement fault.

---

## 4. Claim-layer map

`claim_ids=[]`; SD-064 and MECH-191 are context-only, so no claim can be numerically weakened. But the
substantive mapping matters:

- **SD-064** (global-workspace access channel; candidate / v3_pending). Experiment A is SD-064's *first*
  REE-internal test. Because the substrate is competence-limited, the diagnostic **cannot let SD-064 express
  itself** — it neither raises nor lowers the prior. **SD-064 remains evidentially UNTESTED in V3**
  (Experiment A confounded; Experiment B substrate-blocked). It is NOT "supported-minus-one-artifact" and NOT
  "weakened toward pluralist" — it is untested. (Guardrail: do not manufacture illusory conflict resolution by
  reclassifying a substrate-limited read as a real negative.)
- **SD-027 / MECH-254** (selection-for-broadcast gate; the Experiment-B build target). The plan gates the
  SD-027 V3 top-k access-gate retrofit build on a **clean positive** Experiment A. A confounded read is not a
  positive → **does NOT greenlight the build.** (It also was already independently gated behind
  competence-localization per GATE-B AMEND.)
- **MECH-191** (cross-architecture legibility, substrate-blocked): the dispositional readout is still a
  candidate legibility instrument, but a competence-confounded run cannot confirm it resolves the tonic-channel
  gap. Node stays open.

---

## 5. Biological-reference triage

- **Closest reference:** Baars' Global Workspace (access-consciousness, Block's sense). The J-lens *method* is
  a formal interpretability import (Anthropic 2026 Jacobian lens). SD-064 makes the access-functional claim.
- **Import type:** the DV is a **ported measurement**, not a biology translation — so the FAIL is **not** an
  SD-003-style biology divergence, and **no `/lit-pull` is owed** (the design note already exists; 723's
  autopsy already established this).
- **Missing-dependency signature (present).** In brains you cannot read a workspace's action-coupled geometry
  off an animal that has not learned to competently act — the dispositional readout is *undefined* before
  behavioural competence exists. This is the same prerequisite 719a named for the conversion-ceiling DV. The
  723a FAIL therefore matches a **discovered-prerequisite** signature (competent committed action), not a
  falsification of SD-064.

---

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (untested) | claim_ids=[]; SD-064 cannot express itself on a competence-limited substrate; UNWEAKENED, NOT evidence-against |
| Biological reference | clear | Baars GWT / Anthropic J-lens; ported *measurement*, not a biology divergence; missing-dependency (competent action) signature present |
| **Prerequisites** | **MISSING (DOMINANT)** | competent committed action is an unstated prerequisite of a meaningful action-coupled-compactness read; agent forages 0.158 << 1.0 (719a/724; 732 → observation interface unlearnable) |
| Implementation completeness | complete (measurement) | 723a's discriminative gates are now sound — the readout is well-instrumented; the gap is UPSTREAM of the measurement |
| Environment adequacy | partial | seed 43 near-degenerate (2 effective classes); more fundamentally the observation interface is unlearnable at this scale (732), impoverishing committed-action diversity |
| Measurement adequacy | **adequate** | criteria_non_degenerate all True; concentration negative control non-degenerate (frac_dims_90_random ≈ 0.94) — the 723 measurement fault is FIXED; the FAIL is a trustworthy measurement of a confounded substrate |
| Integration adequacy | n/a | single-module post-hoc readout |
| Scale / capacity | insufficient (symptom) | action-predictive signal weak (bal_acc 0.47 vs null 0.29) — a downstream symptom of the competence floor |

**Recommended `epistemic_category`:** `substrate_ceiling` — the **V3 competence floor** (732-localized to the
observation encoding), NOT a genuine "no-workspace" negative and NOT (any longer) a measurement gap.

---

## 7. Cluster pattern (the load-bearing signal)

723a is the **4th diagnostic in one lineage of structurally-different questions, all bottoming out on the same
competence floor** — the convergent shape /governance already flagged on 2026-07-10 ("724/731/732/723a all
bottom out on ONE root, the V3 competence floor, integrated all-ON agent forages ~0").

| Experiment | Question asked | Readiness / negative control | Load-bearing discrimination | Read |
|---|---|---|---|---|
| V3-EXQ-719a | is committed action state-appropriate vs collapsed? | MI-estimability MET (6005 ticks, 3/3) | state→commitment MI (debiased+above-null) | dissociation UNDEFINED; forages 0.065/0.0/0.455 |
| V3-EXQ-724 | *why* is the all-ON agent incompetent? (OFAT) | oracle 6.05>1.0; baseline reproduces 0.25 | single-factor recovers competence | `competence_deficit_diffuse` (no OFAT factor recovers) |
| V3-EXQ-732 | is it the policy stack or the observation interface? | oracle 6.05>1.0; B0 reproduces 0.2 | REE-head OR vanilla-RL clears floor | `H2_observation_interface_unlearnable` (neither clears) |
| **V3-EXQ-723a** | **does REE have a compact J-space workspace?** | **estimability MET; control non-degenerate** | **concentration discriminative (top << random)** | **`no_compact_workspace_diffuse` — but forages 0.158 << 1.0** |

**These are ONE structural property, not four independent results:** the integrated all-ON agent cannot
competently commit, because its observation encoding is unlearnable at this scale (732). Every committed-action
DV — dissociation (719a), competence localization (724/732), and now *workspace compactness* (723a) — is
**undefined until competence exists.** 723a extends the wall from behavioural-DV territory into the
interpretability/workspace-geometry readout: even a *post-hoc geometric* read of the latent state inherits the
competence confound, because the geometry it measures is the geometry of an incompetent policy's action
coupling.

---

## 8. Learning extracted

1. **A post-hoc geometric readout does not escape the competence confound.** 723a fixed 723's measurement
   fault and still cannot answer compact-vs-diffuse, because the *object* it measures (action-coupled latent
   geometry) is impoverished by the same competence floor that undefines the behavioural DVs. Interpretability
   instruments need a competent substrate as much as behavioural ones do.
2. **Readiness/estimability gates ≠ competence gates.** 723a's readiness preconditions (ticks, pairs, effective
   classes, above-null signal, non-degenerate control) are all MET, yet the read is confounded. A future
   Experiment-A re-read should carry an explicit **competence readiness precondition** (forage ≥ floor on a
   majority of seeds) — the same instrumentation lesson 719a §7 raised for the dissociation DV.
3. **The 723→723a redesign genuinely worked as a *measurement* fix.** The concentration control is now
   non-degenerate; the diffuse verdict is a trustworthy statement *about this substrate*. The residual problem
   is upstream, not in the lens. That is real progress: it removes the measurement escape-hatch and isolates
   the competence floor as the sole remaining confound.
4. **Convergence is the finding.** Four structurally-different diagnostics converging on the observation-encoding
   competence floor is stronger evidence for that root than any single run — and it re-scopes SD-064's
   Experiment A into the competence campaign, not a standalone workspace probe.

---

## 9. Repair pathway (user-confirmed 2026-07-10)

**Adjudication:** `non_contributory` / **confounded**. The diffuse read PROMOTES / DEMOTES / WEIGHTS NOTHING;
compact-vs-diffuse **UNRESOLVED**; SD-064 stays candidate / v3_pending, UNWEAKENED; the read is **NOT** evidence
for the pluralist reading and **NOT** a measurement gap.

**Governance consequence (confirmed):** does **NOT** greenlight the SD-027 / MECH-254 Experiment-B (access-gate)
build — it saves/defers it, exactly as plan §2/§5 pre-register. A compact read would have greenlit it (subject
to the GATE-B competence-localization gate).

**Routing:** `implement-substrate` (upstream) — **re-gate Experiment A behind competence-localization + a
competent all-ON substrate before any re-read.** The build target is the **732-localized observation-encoding
competence gap** (owned by the competence cluster / `f_dominance_conversion_ceiling` /
`ree_ai_design_critique_plan` WS-1). Experiment A's re-read is `blocked_by` that build. A J-lens read on a
COMPETENT agent is the clean Experiment-A baseline; Experiment B's integration-DV also needs competence to be
non-vacuous.

**Re-derive brake — FIRED (substantive).** Mechanically the brake counts **0** for SD-064 / SD-027 / MECH-254 /
MECH-191 (the whole J-lens diagnostic lineage carries `claim_ids=[]`, so the claim-count trigger cannot fire).
But the **substance** the brake exists to stop is present: this is the 4th diagnostic (719a→724→732→723a) on the
**same competence ceiling**, and a 723b would circle it letter-after-letter. Therefore:

- **REFUSE a same-substrate 723b** (another J-lens read on the current competence-limited all-ON agent would
  return the same confounded diffuse verdict — the loop the brake forbids).
- A redesign that tests a **different mechanism** (new EXQ number, different claim_ids) or a J-lens read on a
  **competent** substrate is exempt.
- Recorded on the target as `re_derive_brake.fired: true` with the substantive basis noted.

**No substrate_queue write from this autopsy** (`recommended_substrate_queue_entry.action = none`): the
observation-encoding competence build target is exactly what V3-EXQ-732's autopsy (chip pending) + the
competence cluster own and are materializing; 723a only records that Experiment A's re-read now shares that
dependency. Governance should link Experiment A (`global_workspace_jlens:A`) `blocked_by` the same
observation-encoding competence build when it lands.

**No `/lit-pull`** (ported measurement, design note exists). **No `/claim-synthesis`** (SD-064 is not a coarse
claim being re-falsified in structurally-different ways; it is untested behind a competence floor).

**Draft `evidence_quality_note` (governance writes; do NOT write from this skill):**

> V3-EXQ-723a J-lens discriminative-compactness diagnostic (SD-064 Experiment A; supersedes V3-EXQ-723;
> diagnostic, claim_ids=[], non_contributory; PROMOTES/DEMOTES/WEIGHTS NOTHING). Adjudicated CONFOUNDED by
> failure_autopsy_V3-EXQ-723a_2026-07-10. The 723→723a redesign FIXED 723's non-discriminative gates: the
> concentration control is now non-degenerate (frac_dims_90_random ~0.94) and criteria_non_degenerate are all
> True, so the load-bearing concentration_discriminative FAIL (0/3 ready seeds; concentration_ratio ~0.80 >
> 0.50 ceiling) → self-route no_compact_workspace_diffuse is a trustworthy MEASUREMENT. BUT it reads the same
> competence-limited all-ON substrate (V3-EXQ-714 config) that 719a/724/732 showed forages ~0 because the
> observation interface is unlearnable (732 = H2_observation_interface_unlearnable); 723a itself forages 0.158
> res/ep (< 1.0 floor) with a weak action-predictive signal (bal_acc 0.47 vs null 0.29). A near-monostrategy
> incompetent policy and a genuinely-diffuse workspace are indistinguishable from this readout, so the diffuse
> verdict is NOT a genuine no-workspace negative and does NOT support the SD-027-original pluralist reading —
> compact-vs-diffuse is UNRESOLVED. Does NOT greenlight the SD-027/MECH-254 Experiment-B access-gate build
> (plan §2/§5); does NOT weaken SD-064 (stays candidate/v3_pending, evidentially UNTESTED in V3). 4th
> diagnostic (719a→724→732→723a) to bottom out on the V3 competence floor. Experiment A re-read RE-GATED behind
> the 732-localized observation-encoding competence build (implement-substrate); same-substrate 723b REFUSED
> (re-derive brake fired substantively; claim_ids=[] so the claim-count trigger is 0). pending_retest_after_substrate.

---

## 10. Routing summary for /governance

- **evidence_direction:** `non_contributory` (KEEP; annotate with the §9 note).
- **Does NOT** greenlight SD-027 Experiment-B build. **Does NOT** weaken SD-064 (untested, not negative).
- **Route:** `implement-substrate` (upstream) — re-gate Experiment A (`global_workspace_jlens:A`) `blocked_by`
  the 732-localized observation-encoding competence build; **REFUSE 723b** (re-derive brake fired substantively).
- **substrate_queue:** `action = none` (build owned by the competence cluster / V3-EXQ-732 autopsy + WS-1).
- **No** lit-pull; **no** claim-synthesis.
- Plan touch (governance-applied, not here): mark `global_workspace_jlens:A` re-gated on competence; keep
  GATE-B / B blocked; SD-064 stays candidate / v3_pending.
